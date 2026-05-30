#!/usr/bin/env python3
"""Aggregate repeated-trial finance-specific ATIF audit reports."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    """Load non-empty JSONL records."""
    records: list[dict[str, Any]] = []
    for line_number, line in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if not line.strip():
            continue
        record = json.loads(line)
        if not isinstance(record, dict):
            raise ValueError(f"{path}:{line_number}: record must be a JSON object")
        records.append(record)
    return records


def aggregate_records(records: list[dict[str, Any]]) -> dict[str, Any]:
    """Aggregate finance-specific audit rates across attempts and tasks."""
    attempts_total = len(records)
    attempts_passed = 0
    missing_evidence = 0
    cutoff_violations = 0
    prohibited_tool_calls = 0
    tasks: dict[str, list[bool]] = defaultdict(list)

    for record in records:
        task_id = str(record.get("task_id", "unknown-task"))
        report = record.get("audit_report") or {}
        missing_trajectory = record.get("missing_trajectory") is True

        if not isinstance(report, dict):
            raise ValueError("audit_report must be a JSON object when provided")

        failures = report.get("failures") or []
        if not isinstance(failures, list):
            raise ValueError("audit_report.failures must be a list")

        passed = report.get("verdict") == "pass" and not missing_trajectory
        tasks[task_id].append(passed)
        attempts_passed += int(passed)

        has_missing_evidence = missing_trajectory or any(
            str(failure).startswith("missing_") for failure in failures
        )
        missing_evidence += int(has_missing_evidence)
        cutoff_violations += int("evaluation_cutoff_violation" in failures)
        prohibited_tool_calls += int("prohibited_financial_tool_call" in failures)

    task_attempts = list(tasks.values())
    tasks_total = len(task_attempts)
    tasks_passed_at_least_once = sum(any(attempts) for attempts in task_attempts)
    tasks_passed_all_attempts = sum(all(attempts) for attempts in task_attempts)

    def rate(numerator: int, denominator: int) -> float:
        return round(numerator / denominator, 4) if denominator else 0.0

    return {
        "attempts_total": attempts_total,
        "attempts_passed": attempts_passed,
        "tasks_total": tasks_total,
        "tasks_passed_at_least_once": tasks_passed_at_least_once,
        "tasks_passed_all_attempts": tasks_passed_all_attempts,
        "metrics": {
            "attempt_pass_rate": rate(attempts_passed, attempts_total),
            "pass_at_k_task_rate": rate(tasks_passed_at_least_once, tasks_total),
            "pass_pow_k_task_rate": rate(tasks_passed_all_attempts, tasks_total),
            "missing_evidence_rate": rate(missing_evidence, attempts_total),
            "cutoff_violation_rate": rate(cutoff_violations, attempts_total),
            "prohibited_tool_call_rate": rate(prohibited_tool_calls, attempts_total),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Aggregate repeated-trial finance-specific ATIF audit reports."
    )
    parser.add_argument("audits", type=Path, help="Path to JSONL audit records.")
    parser.add_argument("--output", type=Path, help="Optional aggregate report path.")
    args = parser.parse_args()

    report = aggregate_records(load_jsonl(args.audits))
    rendered = json.dumps(report, indent=2, ensure_ascii=False)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
