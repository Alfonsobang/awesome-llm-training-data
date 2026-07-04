#!/usr/bin/env python3
"""Validate finance preference-review examples against the local schema."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "finance-preference-review.schema.json"
EXAMPLE_DIR = ROOT / "examples" / "finance-preference-reviews"

AXIS_LABELS = {"pass", "partial", "fail", "not_applicable"}
OVERALL_PREFERENCES = {"prefer", "reject", "tie", "needs_adjudication"}
REVIEWER_ROLES = {
    "domain_reviewer",
    "data_quality_reviewer",
    "safety_reviewer",
    "adjudicator",
}
ADJUDICATION_TRIGGERS = {
    "safety_disagreement",
    "numeric_disagreement",
    "unsupported_citation",
    "manifest_source_violation",
    "trading_advice",
    "trace_missing",
    "reviewer_uncertainty",
}
REQUIRED_AXIS_KEYS = {
    "evidence_grounding",
    "numeric_correctness",
    "citation_support",
    "safety_boundary",
    "source_quality",
    "trace_quality",
    "limitation_quality",
}
REQUIRED_EVIDENCE_KEYS = {
    "source_ids_checked",
    "citation_paths_checked",
    "numeric_fields_checked",
    "unsafe_claims_found",
    "manifest_source_violation",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_schema_file() -> list[str]:
    errors: list[str] = []
    schema = load_json(SCHEMA_PATH)
    if schema.get("title") != "Finance Preference Review":
        errors.append(f"{SCHEMA_PATH}: unexpected schema title")
    if "axis_labels" not in schema.get("properties", {}):
        errors.append(f"{SCHEMA_PATH}: missing axis_labels property")
    if "evidence_checks" not in schema.get("properties", {}):
        errors.append(f"{SCHEMA_PATH}: missing evidence_checks property")
    return errors


def validate_review(path: Path) -> list[str]:
    errors: list[str] = []
    review = load_json(path)
    required = {
        "review_id",
        "task_id",
        "reviewer_role",
        "candidate_answer_id",
        "overall_preference",
        "axis_labels",
        "evidence_checks",
        "adjudication",
        "reviewer_notes",
    }
    missing = sorted(required - set(review))
    if missing:
        return [f"{path}: missing fields: {', '.join(missing)}"]

    if review["reviewer_role"] not in REVIEWER_ROLES:
        errors.append(f"{path}: unsupported reviewer_role: {review['reviewer_role']}")
    if review["overall_preference"] not in OVERALL_PREFERENCES:
        errors.append(f"{path}: unsupported overall_preference: {review['overall_preference']}")

    axis_labels = review["axis_labels"]
    if not isinstance(axis_labels, dict):
        errors.append(f"{path}: axis_labels must be an object")
    else:
        missing_axes = sorted(REQUIRED_AXIS_KEYS - set(axis_labels))
        extra_axes = sorted(set(axis_labels) - REQUIRED_AXIS_KEYS)
        if missing_axes:
            errors.append(f"{path}: missing axis labels: {', '.join(missing_axes)}")
        if extra_axes:
            errors.append(f"{path}: unsupported axis labels: {', '.join(extra_axes)}")
        for key, value in axis_labels.items():
            if value not in AXIS_LABELS:
                errors.append(f"{path}: axis {key} has unsupported value: {value}")

    evidence = review["evidence_checks"]
    if not isinstance(evidence, dict):
        errors.append(f"{path}: evidence_checks must be an object")
    else:
        missing_evidence = sorted(REQUIRED_EVIDENCE_KEYS - set(evidence))
        if missing_evidence:
            errors.append(f"{path}: missing evidence fields: {', '.join(missing_evidence)}")
        for list_field in ("source_ids_checked", "citation_paths_checked", "numeric_fields_checked", "unsafe_claims_found"):
            if list_field in evidence and not isinstance(evidence[list_field], list):
                errors.append(f"{path}: {list_field} must be a list")
        if not evidence.get("source_ids_checked"):
            errors.append(f"{path}: source_ids_checked must be non-empty")
        if not evidence.get("citation_paths_checked"):
            errors.append(f"{path}: citation_paths_checked must be non-empty")
        if "manifest_source_violation" in evidence and not isinstance(evidence["manifest_source_violation"], bool):
            errors.append(f"{path}: manifest_source_violation must be boolean")

    adjudication = review["adjudication"]
    if not isinstance(adjudication, dict):
        errors.append(f"{path}: adjudication must be an object")
    else:
        if not isinstance(adjudication.get("required"), bool):
            errors.append(f"{path}: adjudication.required must be boolean")
        triggers = adjudication.get("triggers")
        if not isinstance(triggers, list):
            errors.append(f"{path}: adjudication.triggers must be a list")
        else:
            for trigger in triggers:
                if trigger not in ADJUDICATION_TRIGGERS:
                    errors.append(f"{path}: unsupported adjudication trigger: {trigger}")
            if adjudication.get("required") is True and not triggers:
                errors.append(f"{path}: adjudication triggers required when adjudication.required is true")

    if not isinstance(review["reviewer_notes"], str) or len(review["reviewer_notes"].strip()) < 10:
        errors.append(f"{path}: reviewer_notes must be a useful non-empty string")

    return errors


def main() -> int:
    errors = validate_schema_file()
    paths = sorted(EXAMPLE_DIR.glob("*.json"))
    if not paths:
        errors.append(f"No review examples found in {EXAMPLE_DIR}")
    for path in paths:
        errors.extend(validate_review(path))

    if errors:
        print("Finance preference-review validation failed:", file=sys.stderr)
        print("\n".join(errors), file=sys.stderr)
        return 1

    print(f"Validated {len(paths)} finance preference-review examples.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
