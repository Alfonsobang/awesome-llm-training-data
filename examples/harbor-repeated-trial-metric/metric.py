#!/usr/bin/env python3
"""Custom Harbor metric for repeated-trial agent evaluation.

The script reads JSONL rewards and writes aggregate metrics as JSON.
It is intentionally dependency-free so it can run inside a Harbor metric hook.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from math import prod
from pathlib import Path
from typing import Any


def reward_to_binary(row: dict[str, Any] | None) -> int | None:
    if not row:
        return None

    value = row.get("reward")
    if value is None:
        numeric_values = [
            item for item in row.values() if isinstance(item, (int, float)) and item in (0, 1)
        ]
        if len(numeric_values) == 1:
            value = numeric_values[0]

    if isinstance(value, bool):
        return int(value)
    if isinstance(value, (int, float)) and value in (0, 1):
        return int(value)
    return None


def pass_at_k(successes: list[int], k: int) -> float:
    n = len(successes)
    c = sum(successes)

    if n == 0 or k <= 0:
        return 0.0
    k = min(k, n)
    if n - c < k:
        return 1.0

    return 1.0 - prod((n - c - i) / (n - i) for i in range(k))


def pass_pow_k(successes: list[int], k: int) -> float:
    if len(successes) < k or k <= 0:
        return 0.0
    return float(all(value == 1 for value in successes[:k]))


def load_rewards(path: Path) -> list[dict[str, Any] | None]:
    rows: list[dict[str, Any] | None] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_number}: invalid JSON") from exc
        if value is not None and not isinstance(value, dict):
            raise ValueError(f"{path}:{line_number}: expected a JSON object or null")
        rows.append(value)
    return rows


def compute_metrics(rows: list[dict[str, Any] | None]) -> dict[str, Any]:
    task_successes: dict[str, list[int]] = defaultdict(list)
    missing_rewards = 0

    for index, row in enumerate(rows):
        reward = reward_to_binary(row)
        if reward is None:
            missing_rewards += 1
            reward = 0

        task_name = (
            str(row.get("task_name") or row.get("task") or row.get("task_id"))
            if row
            else f"row-{index}"
        )
        if not task_name or task_name == "None":
            task_name = f"row-{index}"

        task_successes[task_name].append(reward)

    if not rows:
        return {
            "mean_reward": 0.0,
            "task_pass_rate": 0.0,
            "missing_reward_rate": 0.0,
            "pass_at_k": {},
            "pass_pow_k": {},
            "n_tasks": 0,
            "n_trials": 0,
        }

    all_rewards = [value for values in task_successes.values() for value in values]
    max_attempts = max(len(values) for values in task_successes.values())
    k_values = [k for k in (1, 2, 3, 5, 10) if k <= max_attempts]

    return {
        "mean_reward": sum(all_rewards) / len(all_rewards),
        "task_pass_rate": sum(any(values) for values in task_successes.values())
        / len(task_successes),
        "missing_reward_rate": missing_rewards / len(rows),
        "pass_at_k": {
            str(k): sum(pass_at_k(values, k) for values in task_successes.values())
            / len(task_successes)
            for k in k_values
        },
        "pass_pow_k": {
            str(k): sum(pass_pow_k(values, k) for values in task_successes.values())
            / len(task_successes)
            for k in k_values
        },
        "n_tasks": len(task_successes),
        "n_trials": len(rows),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-path", type=Path, required=True)
    parser.add_argument("-o", "--output-path", type=Path, required=True)
    args = parser.parse_args()

    metrics = compute_metrics(load_rewards(args.input_path))
    args.output_path.write_text(json.dumps(metrics, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
