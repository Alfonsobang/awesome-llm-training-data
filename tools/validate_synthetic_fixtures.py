#!/usr/bin/env python3
"""Validate synthetic financial fixtures and reference answers."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = ROOT / "examples" / "financial-agent-eval-seed" / "harbor-template"

SYNTHETIC_MARKERS = {
    "synthetic",
    "fixture",
    "public-example-only",
    "benchmark scaffolding",
}

DISALLOWED_REFERENCE_PHRASES = {
    "production-ready",
    "price target",
    "buy recommendation",
    "sell recommendation",
    "guaranteed return",
    "will return",
    "cannot lose",
    "insider information should be used",
}

ALLOWED_REFERENCE_PHRASES_BY_TASK = {
    "compliance-refusal": {
        "guaranteed return",
    }
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def iter_fixture_files() -> list[Path]:
    return sorted(
        path
        for path in TEMPLATE_DIR.glob("*/fixtures/*")
        if path.is_file()
    )


def iter_reference_answers() -> list[Path]:
    return sorted(TEMPLATE_DIR.glob("*/solution/answer.json"))


def has_synthetic_marker(path: Path, text: str) -> bool:
    haystack = f"{path.name}\n{path.parent.name}\n{text}".lower()
    return any(marker in haystack for marker in SYNTHETIC_MARKERS)


def validate_fixture_files() -> list[str]:
    errors: list[str] = []
    fixtures = iter_fixture_files()
    if not fixtures:
        return [f"No fixture files found under {TEMPLATE_DIR}"]

    for path in fixtures:
        text = read_text(path)
        if not has_synthetic_marker(path, text):
            errors.append(f"{path}: fixture must be explicitly marked synthetic or fixture-only")

    return errors


def validate_reference_answers() -> list[str]:
    errors: list[str] = []
    answers = iter_reference_answers()
    if not answers:
        return [f"No reference answers found under {TEMPLATE_DIR}"]

    for path in answers:
        try:
            answer = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{path}: invalid JSON: {exc}")
            continue

        task_id = answer.get("task_id", path.parent.parent.name)
        if answer.get("not_investment_advice") is not True:
            errors.append(f"{path}: {task_id} must set not_investment_advice to true")

        limitations = answer.get("limitations")
        if not isinstance(limitations, list) or not limitations:
            errors.append(f"{path}: {task_id} must include non-empty limitations")
        else:
            joined_limitations = " ".join(str(value).lower() for value in limitations)
            if "synthetic" not in joined_limitations and "fixture" not in joined_limitations:
                errors.append(f"{path}: {task_id} limitations should mention synthetic fixture boundary")

        combined = json.dumps(answer, ensure_ascii=False).lower()
        allowed_phrases = ALLOWED_REFERENCE_PHRASES_BY_TASK.get(task_id, set())
        for phrase in sorted(DISALLOWED_REFERENCE_PHRASES):
            if phrase in allowed_phrases:
                continue
            if phrase in combined:
                errors.append(f"{path}: {task_id} contains disallowed reference phrase: {phrase}")

    return errors


def main() -> int:
    errors = []
    errors.extend(validate_fixture_files())
    errors.extend(validate_reference_answers())

    if errors:
        print("Synthetic fixture validation failed:", file=sys.stderr)
        print("\n".join(errors), file=sys.stderr)
        return 1

    print(
        "Validated "
        f"{len(iter_fixture_files())} synthetic fixture files and "
        f"{len(iter_reference_answers())} reference answers."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
