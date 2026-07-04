#!/usr/bin/env python3
"""Validate the Financial Agent Eval Seed benchmark card."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SEED_DIR = ROOT / "examples" / "financial-agent-eval-seed"
CARD_PATH = SEED_DIR / "benchmark-card.yml"
SPEC_DIR = SEED_DIR / "task-specs"
REPORT_DIR = SEED_DIR / "results"
SOURCE_MANIFEST_PATH = SEED_DIR / "data-sources" / "source-manifest.json"

REQUIRED_TOP_LEVEL = {
    "name",
    "version",
    "owner",
    "status",
    "last_reviewed",
    "purpose",
    "task_scope",
    "data",
    "temporal_controls",
    "evaluation",
    "reports",
    "limitations",
    "visible_evidence",
}

REQUIRED_PURPOSE = {"summary", "intended_users", "out_of_scope"}
REQUIRED_TASK_SCOPE = {
    "task_families",
    "required_capabilities",
    "prohibited_behaviors",
    "safety_boundary",
}
REQUIRED_DATA = {
    "source_type",
    "source_manifest",
    "source_manifest_refs",
    "redistribution_policy",
    "private_data_used",
    "real_user_data_used",
    "proprietary_workflow_used",
}
REQUIRED_TEMPORAL_CONTROLS = {
    "cutoff_date",
    "evidence_window",
    "known_leakage_risks",
    "revision_policy",
}
REQUIRED_EVALUATION = {
    "answer_schema",
    "verifier",
    "metrics",
    "tolerance_policy",
    "known_failure_modes",
    "current_task_count",
    "known_bad_candidate",
}
REQUIRED_REPORTS = {
    "passing_report",
    "known_bad_report",
    "source_governance_report",
    "repeated_trial_report",
}
REQUIRED_LIMITATIONS = {
    "benchmark_limits",
    "domain_limits",
    "non_advice_statement",
}
REQUIRED_VISIBLE_EVIDENCE = {
    "task_specs",
    "harbor_style_templates",
    "reference_answers",
    "known_bad_answers",
    "source_manifest",
    "stable_reports",
}

DISALLOWED_CLAIMS = {
    "production-ready",
    "best benchmark",
    "state-of-the-art",
    "trading recommendation",
    "guaranteed return",
}


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError(f"Missing file: {path}") from None
    except json.JSONDecodeError as exc:
        raise ValueError(f"{path}: expected JSON-compatible YAML: {exc}") from None


def require_fields(container: dict, required: set[str], label: str) -> list[str]:
    missing = sorted(required - set(container))
    return [f"{label}: missing fields: {', '.join(missing)}"] if missing else []


def require_non_empty_list(value: object, label: str, min_items: int = 1) -> list[str]:
    if not isinstance(value, list) or len(value) < min_items:
        return [f"{label}: must be a list with at least {min_items} item(s)."]
    if not all(isinstance(item, str) and item.strip() for item in value):
        return [f"{label}: all entries must be non-empty strings."]
    return []


def load_task_specs() -> list[dict]:
    return [load_json(path) for path in sorted(SPEC_DIR.glob("*.json"))]


def validate_card(card: dict) -> list[str]:
    errors: list[str] = []
    errors.extend(require_fields(card, REQUIRED_TOP_LEVEL, "benchmark card"))
    if errors:
        return errors

    nested_requirements = [
        ("purpose", REQUIRED_PURPOSE),
        ("task_scope", REQUIRED_TASK_SCOPE),
        ("data", REQUIRED_DATA),
        ("temporal_controls", REQUIRED_TEMPORAL_CONTROLS),
        ("evaluation", REQUIRED_EVALUATION),
        ("reports", REQUIRED_REPORTS),
        ("limitations", REQUIRED_LIMITATIONS),
        ("visible_evidence", REQUIRED_VISIBLE_EVIDENCE),
    ]
    for field, required in nested_requirements:
        if not isinstance(card[field], dict):
            errors.append(f"{field}: must be an object.")
            continue
        errors.extend(require_fields(card[field], required, field))

    if card.get("status") not in {"draft", "active", "deprecated"}:
        errors.append("status: must be draft, active, or deprecated.")

    purpose = card["purpose"]
    task_scope = card["task_scope"]
    data = card["data"]
    evaluation = card["evaluation"]
    reports = card["reports"]
    limitations = card["limitations"]

    errors.extend(require_non_empty_list(purpose.get("intended_users"), "purpose.intended_users", 3))
    errors.extend(require_non_empty_list(purpose.get("out_of_scope"), "purpose.out_of_scope", 5))
    errors.extend(require_non_empty_list(task_scope.get("task_families"), "task_scope.task_families", 5))
    errors.extend(require_non_empty_list(task_scope.get("required_capabilities"), "task_scope.required_capabilities", 5))
    errors.extend(require_non_empty_list(task_scope.get("prohibited_behaviors"), "task_scope.prohibited_behaviors", 5))
    errors.extend(require_non_empty_list(data.get("source_manifest_refs"), "data.source_manifest_refs", 1))
    errors.extend(require_non_empty_list(evaluation.get("metrics"), "evaluation.metrics", 3))
    errors.extend(require_non_empty_list(evaluation.get("known_failure_modes"), "evaluation.known_failure_modes", 5))
    errors.extend(require_non_empty_list(limitations.get("benchmark_limits"), "limitations.benchmark_limits", 3))
    errors.extend(require_non_empty_list(limitations.get("domain_limits"), "limitations.domain_limits", 2))

    for flag in ("private_data_used", "real_user_data_used", "proprietary_workflow_used"):
        if data.get(flag) is not False:
            errors.append(f"data.{flag}: must be false.")

    non_advice = limitations.get("non_advice_statement", "").lower()
    safety_boundary = task_scope.get("safety_boundary", "").lower()
    for term in ("investment advice", "trading signals", "private data", "real user data", "proprietary workflows"):
        if term not in non_advice:
            errors.append(f"limitations.non_advice_statement: must mention {term}.")
        if term not in safety_boundary:
            errors.append(f"task_scope.safety_boundary: must mention {term}.")

    specs = load_task_specs()
    if evaluation.get("current_task_count") != len(specs):
        errors.append(
            "evaluation.current_task_count: "
            f"expected {len(specs)}, got {evaluation.get('current_task_count')}."
        )

    spec_families = {spec["family"] for spec in specs}
    card_families = set(task_scope.get("task_families", []))
    missing_families = sorted(spec_families - card_families)
    if missing_families:
        errors.append(f"task_scope.task_families: missing families from task specs: {', '.join(missing_families)}")

    manifest = load_json(SOURCE_MANIFEST_PATH)
    source_ids = {source["source_id"] for source in manifest["sources"]}
    missing_sources = sorted(set(data.get("source_manifest_refs", [])) - source_ids)
    if missing_sources:
        errors.append(f"data.source_manifest_refs: unknown source ids: {', '.join(missing_sources)}")

    for label, relative_path in reports.items():
        report_path = SEED_DIR / relative_path
        if not report_path.exists():
            errors.append(f"reports.{label}: missing report file: {relative_path}")

    passing_report = load_json(REPORT_DIR / "example-report.json")
    bad_report = load_json(REPORT_DIR / "bad-finance-agent-report.json")
    governance_report = load_json(REPORT_DIR / "source-governance-report.json")
    repeated_trial_report = load_json(REPORT_DIR / "repeated-trial-example-report.json")
    if passing_report.get("tasks_total") != len(specs) or passing_report.get("tasks_failed") != 0:
        errors.append("reports.passing_report: stable passing report must cover all tasks with zero failures.")
    if bad_report.get("tasks_total") != len(specs) or bad_report.get("tasks_passed") != 0:
        errors.append("reports.known_bad_report: known-bad report must cover all tasks with zero passes.")
    if governance_report.get("tasks_total") != len(specs):
        errors.append("reports.source_governance_report: task count must match task specs.")
    if repeated_trial_report.get("tasks_total") != len(specs):
        errors.append("reports.repeated_trial_report: task count must match task specs.")
    if "pass_at_k" not in repeated_trial_report or "pass_pow_k" not in repeated_trial_report:
        errors.append("reports.repeated_trial_report: must include pass_at_k and pass_pow_k.")

    combined = json.dumps(card, ensure_ascii=False).lower()
    for phrase in sorted(DISALLOWED_CLAIMS):
        if phrase in combined:
            errors.append(f"benchmark card contains disallowed claim: {phrase}")

    return errors


def main() -> int:
    try:
        card = load_json(CARD_PATH)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    errors = validate_card(card)
    if errors:
        print("Financial benchmark card validation failed:", file=sys.stderr)
        print("\n".join(errors), file=sys.stderr)
        return 1

    print(f"Validated financial benchmark card with {len(load_task_specs())} task specs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
