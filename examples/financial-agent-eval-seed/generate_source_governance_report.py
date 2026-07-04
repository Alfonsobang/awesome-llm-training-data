#!/usr/bin/env python3
"""Generate a financial data-source governance summary report."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MANIFEST_PATH = ROOT / "data-sources" / "source-manifest.json"
SPEC_DIR = ROOT / "task-specs"
DEFAULT_RESULTS_DIR = ROOT / "results"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_task_specs() -> list[dict]:
    return [load_json(path) for path in sorted(SPEC_DIR.glob("*.json"))]


def build_report() -> dict:
    manifest = load_json(MANIFEST_PATH)
    sources = manifest["sources"]
    specs = load_task_specs()
    source_by_id = {source["source_id"]: source for source in sources}

    packaging_counts = Counter(source["packaging_policy"] for source in sources)
    access_counts = Counter(source["access_method"] for source in sources)
    terms_review_required = sum(1 for source in sources if source["terms_review_required"])

    task_mappings = []
    family_counts = Counter()
    referenced_source_ids: set[str] = set()
    for spec in specs:
        family = spec["family"]
        family_counts[family] += 1
        for source_id in spec["source_refs"]:
            referenced_source_ids.add(source_id)
            source = source_by_id[source_id]
            task_mappings.append(
                {
                    "task_id": spec["task_id"],
                    "family": family,
                    "source_id": source_id,
                    "source_name": source["name"],
                    "packaging_policy": source["packaging_policy"],
                    "terms_review_required": source["terms_review_required"],
                }
            )

    sources_by_family: dict[str, list[str]] = defaultdict(list)
    for source in sources:
        for family in source["allowed_task_families"]:
            sources_by_family[family].append(source["source_id"])

    return {
        "report": "financial-data-source-governance",
        "manifest_version": manifest["manifest_version"],
        "reviewed_on": manifest["reviewed_on"],
        "sources_total": len(sources),
        "sources_referenced_by_tasks": len(referenced_source_ids),
        "tasks_total": len(specs),
        "task_source_mappings_total": len(task_mappings),
        "packaging_policy_counts": dict(sorted(packaging_counts.items())),
        "access_method_counts": dict(sorted(access_counts.items())),
        "terms_review_required_sources": terms_review_required,
        "task_family_counts": dict(sorted(family_counts.items())),
        "sources_by_allowed_family": {
            family: sorted(source_ids)
            for family, source_ids in sorted(sources_by_family.items())
        },
        "task_source_mappings": task_mappings,
        "policy_notes": manifest["policy"]["notes"],
        "safety_boundary": (
            "Public accessibility does not imply redistribution rights. "
            "The seed bundles synthetic fixtures by default and treats external sources as reference-only unless reviewed."
        ),
    }


def write_markdown(report: dict, path: Path) -> None:
    policy_rows = [
        "| Packaging policy | Source count |",
        "| --- | ---: |",
    ]
    for policy, count in report["packaging_policy_counts"].items():
        policy_rows.append(f"| `{policy}` | {count} |")

    mapping_rows = [
        "| Task | Family | Source | Packaging | Terms review |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in report["task_source_mappings"]:
        mapping_rows.append(
            "| `{task_id}` | `{family}` | `{source_id}` | `{packaging}` | `{terms}` |".format(
                task_id=item["task_id"],
                family=item["family"],
                source_id=item["source_id"],
                packaging=item["packaging_policy"],
                terms=str(item["terms_review_required"]).lower(),
            )
        )

    body = "\n".join(
        [
            "# Financial Data Source Governance Report",
            "",
            "This stable report is generated from the source manifest and task specs. It makes the seed's source policy inspectable without opening every JSON file.",
            "",
            f"- Manifest version: `{report['manifest_version']}`",
            f"- Reviewed on: `{report['reviewed_on']}`",
            f"- Sources total: {report['sources_total']}",
            f"- Sources referenced by tasks: {report['sources_referenced_by_tasks']}",
            f"- Tasks total: {report['tasks_total']}",
            f"- Task-source mappings: {report['task_source_mappings_total']}",
            f"- Sources requiring terms review: {report['terms_review_required_sources']}",
            "",
            "## Packaging Policies",
            "",
            *policy_rows,
            "",
            "## Task Source Mappings",
            "",
            *mapping_rows,
            "",
            "## Policy Note",
            "",
            report["policy_notes"],
            "",
            "## Safety Boundary",
            "",
            report["safety_boundary"],
            "",
        ]
    )
    path.write_text(body, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--results-dir",
        type=Path,
        default=DEFAULT_RESULTS_DIR,
        help="Directory for generated JSON and Markdown reports.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = build_report()
    args.results_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.results_dir / "source-governance-report.json"
    md_path = args.results_dir / "source-governance-report.md"
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_markdown(report, md_path)
    print(f"Wrote {json_path.relative_to(ROOT)}")
    print(f"Wrote {md_path.relative_to(ROOT)}")
    print(
        "Governance report: "
        f"{report['sources_total']} sources, "
        f"{report['tasks_total']} tasks, "
        f"{report['task_source_mappings_total']} mappings."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
