#!/usr/bin/env python3
"""Validate financial agent evaluation seed task specs."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SPEC_DIR = ROOT / "task-specs"

REQUIRED_FIELDS = {
    "task_id",
    "family",
    "risk_level",
    "instruction",
    "allowed_sources",
    "allowed_tools",
    "prohibited_actions",
    "required_evidence",
    "metrics",
    "known_failure_modes",
}

ALLOWED_RISK_LEVELS = {"low", "medium", "high"}
SAFETY_GUARDS = {
    "investment",
    "guaranteed",
    "private",
    "inside",
    "recommendation",
    "manipulation",
}


def validate_spec(path: Path) -> list[str]:
    errors: list[str] = []

    try:
        spec = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{path}: invalid JSON: {exc}"]

    if not isinstance(spec, dict):
        return [f"{path}: spec must be a JSON object"]

    missing = sorted(REQUIRED_FIELDS - set(spec))
    if missing:
        errors.append(f"{path}: missing fields: {', '.join(missing)}")

    if spec.get("risk_level") not in ALLOWED_RISK_LEVELS:
        errors.append(f"{path}: risk_level must be one of {sorted(ALLOWED_RISK_LEVELS)}")

    for field in ("allowed_sources", "allowed_tools", "prohibited_actions", "required_evidence", "metrics", "known_failure_modes"):
        if field in spec and not isinstance(spec[field], list):
            errors.append(f"{path}: {field} must be a list")

    task_id = spec.get("task_id")
    if isinstance(task_id, str) and path.stem != task_id:
        errors.append(f"{path}: filename must match task_id")

    prohibited_actions = " ".join(str(item).lower() for item in spec.get("prohibited_actions", []))
    if not any(guard in prohibited_actions for guard in SAFETY_GUARDS):
        errors.append(f"{path}: prohibited_actions should include at least one finance safety guardrail")

    return errors


def main() -> int:
    errors: list[str] = []
    spec_paths = sorted(SPEC_DIR.glob("*.json"))

    if not spec_paths:
        print(f"No task specs found in {SPEC_DIR}", file=sys.stderr)
        return 1

    for path in spec_paths:
        errors.extend(validate_spec(path))

    if errors:
        print("Financial agent eval seed validation failed:", file=sys.stderr)
        print("\n".join(errors), file=sys.stderr)
        return 1

    print(f"Validated {len(spec_paths)} financial agent evaluation task specs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
