#!/usr/bin/env python3
"""Generate and validate the Harbor-style finance task-pack manifest."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
TEMPLATE_DIR = ROOT / "harbor-template"
SPEC_DIR = ROOT / "task-specs"
MANIFEST_PATH = TEMPLATE_DIR / "task-pack-manifest.json"

REQUIRED_TASK_FILES = {
    "README.md",
    "instruction.md",
    "task.toml",
    "solution/answer.json",
}
REQUIRED_TOP_LEVEL = {
    "manifest_version",
    "task_pack",
    "status",
    "generated_from",
    "public_safety_boundary",
    "tasks",
}
REQUIRED_TASK_FIELDS = {
    "task_id",
    "template_path",
    "task_spec",
    "family",
    "risk_level",
    "source_refs",
    "fixture_paths",
    "solution_path",
    "verifier_paths",
    "task_metadata_path",
    "safety_boundary",
}


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError(f"Missing file: {path}") from None
    except json.JSONDecodeError as exc:
        raise ValueError(f"{path}: invalid JSON: {exc}") from None


def display_path(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def template_dirs() -> list[Path]:
    return sorted(path for path in TEMPLATE_DIR.iterdir() if path.is_dir())


def spec_by_task_id() -> dict[str, dict[str, Any]]:
    specs = {}
    for path in sorted(SPEC_DIR.glob("*.json")):
        spec = load_json(path)
        specs[spec["task_id"]] = {**spec, "_path": path}
    return specs


def task_id_for_template(template_name: str, specs: dict[str, dict[str, Any]]) -> str:
    if template_name in specs:
        return template_name
    aliases = {
        "compliance-refusal": "compliance-refusal-guaranteed-return",
        "exact-data-lookup": "exact-data-lookup-public-filing",
        "filing-margin-explanation": "filing-grounded-margin-explanation",
        "public-source-search": "public-filing-search",
    }
    return aliases.get(template_name, template_name)


def discover_fixture_paths(task_dir: Path) -> list[str]:
    fixtures_dir = task_dir / "fixtures"
    if not fixtures_dir.exists():
        return []
    return sorted(display_path(path) for path in fixtures_dir.rglob("*") if path.is_file())


def discover_verifier_paths(task_dir: Path) -> list[str]:
    tests_dir = task_dir / "tests"
    if not tests_dir.exists():
        return []
    return sorted(display_path(path) for path in tests_dir.glob("test_*.py"))


def build_manifest() -> dict[str, Any]:
    specs = spec_by_task_id()
    tasks = []
    for task_dir in template_dirs():
        task_id = task_id_for_template(task_dir.name, specs)
        spec = specs[task_id]
        tasks.append(
            {
                "task_id": task_dir.name,
                "task_spec": display_path(spec["_path"]),
                "template_path": display_path(task_dir),
                "family": spec["family"],
                "risk_level": spec["risk_level"],
                "source_refs": spec.get("source_refs", []),
                "fixture_paths": discover_fixture_paths(task_dir),
                "solution_path": display_path(task_dir / "solution" / "answer.json"),
                "verifier_paths": discover_verifier_paths(task_dir),
                "task_metadata_path": display_path(task_dir / "task.toml"),
                "safety_boundary": (
                    "public-safe example; no private company data, real user data, proprietary workflows, "
                    "investment advice, trading signals, or production-readiness claims"
                ),
            }
        )

    return {
        "manifest_version": "1.0",
        "task_pack": "financial-agent-eval-seed-harbor-style",
        "status": "public-safe-example-not-official-harbor-adapter",
        "generated_from": {
            "task_specs": "task-specs/",
            "templates": "harbor-template/",
            "source_manifest": "data-sources/source-manifest.json",
        },
        "public_safety_boundary": (
            "This manifest describes small Harbor-style task templates for evaluation engineering. "
            "It does not contain private company data, real user data, proprietary workflows, "
            "investment advice, trading signals, or production-readiness claims."
        ),
        "tasks": tasks,
    }


def validate_manifest(manifest: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    missing_top = sorted(REQUIRED_TOP_LEVEL - set(manifest))
    if missing_top:
        return [f"manifest: missing fields: {', '.join(missing_top)}"]

    if manifest["status"] != "public-safe-example-not-official-harbor-adapter":
        errors.append("manifest.status must state that this is not an official Harbor adapter.")

    boundary = str(manifest["public_safety_boundary"]).lower()
    for term in ("private company data", "real user data", "proprietary workflows", "investment advice", "trading signals"):
        if term not in boundary:
            errors.append(f"public_safety_boundary must mention {term}.")

    tasks = manifest["tasks"]
    if not isinstance(tasks, list) or not tasks:
        return errors + ["manifest.tasks must be a non-empty list."]

    task_dirs = {path.name for path in template_dirs()}
    manifest_task_ids = {task.get("task_id") for task in tasks if isinstance(task, dict)}
    missing_dirs = sorted(task_dirs - manifest_task_ids)
    extra_tasks = sorted(manifest_task_ids - task_dirs)
    if missing_dirs:
        errors.append(f"manifest.tasks missing task directories: {', '.join(missing_dirs)}")
    if extra_tasks:
        errors.append(f"manifest.tasks includes unknown task directories: {', '.join(extra_tasks)}")

    specs = spec_by_task_id()
    referenced_specs = set()
    for task in tasks:
        if not isinstance(task, dict):
            errors.append("manifest.tasks entries must be objects.")
            continue
        missing_fields = sorted(REQUIRED_TASK_FIELDS - set(task))
        if missing_fields:
            errors.append(f"{task.get('task_id', '<unknown>')}: missing fields: {', '.join(missing_fields)}")
            continue

        task_dir = ROOT / task["template_path"]
        for relative_file in REQUIRED_TASK_FILES:
            path = task_dir / relative_file
            if not path.exists():
                errors.append(f"{task['task_id']}: missing required file {display_path(path)}")

        if not task.get("fixture_paths"):
            errors.append(f"{task['task_id']}: fixture_paths must not be empty.")
        for fixture_path in task.get("fixture_paths", []):
            if not (ROOT / fixture_path).exists():
                errors.append(f"{task['task_id']}: missing fixture {fixture_path}")

        if not task.get("verifier_paths"):
            errors.append(f"{task['task_id']}: verifier_paths must not be empty.")
        for verifier_path in task.get("verifier_paths", []):
            if not (ROOT / verifier_path).exists():
                errors.append(f"{task['task_id']}: missing verifier {verifier_path}")

        for path_field in ("solution_path", "task_metadata_path", "task_spec"):
            if not (ROOT / task[path_field]).exists():
                errors.append(f"{task['task_id']}: missing {path_field}: {task[path_field]}")

        spec = load_json(ROOT / task["task_spec"])
        referenced_specs.add(spec["task_id"])
        if task["family"] != spec["family"]:
            errors.append(f"{task['task_id']}: family does not match task spec.")
        if task["risk_level"] != spec["risk_level"]:
            errors.append(f"{task['task_id']}: risk_level does not match task spec.")
        if sorted(task["source_refs"]) != sorted(spec.get("source_refs", [])):
            errors.append(f"{task['task_id']}: source_refs do not match task spec.")

        safety = str(task["safety_boundary"]).lower()
        for term in ("public-safe", "investment advice", "real user data"):
            if term not in safety:
                errors.append(f"{task['task_id']}: safety_boundary must mention {term}.")

    missing_specs = sorted(set(specs) - referenced_specs)
    if missing_specs:
        errors.append(f"manifest does not reference task specs: {', '.join(missing_specs)}")

    return errors


def write_manifest(path: Path) -> None:
    manifest = build_manifest()
    path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Regenerate task-pack-manifest.json before validation.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.write:
        write_manifest(MANIFEST_PATH)

    try:
        manifest = load_json(MANIFEST_PATH)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    errors = validate_manifest(manifest)
    if errors:
        print("Task-pack manifest validation failed:", file=sys.stderr)
        print("\n".join(errors), file=sys.stderr)
        return 1

    print(f"Validated task-pack manifest with {len(manifest['tasks'])} tasks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
