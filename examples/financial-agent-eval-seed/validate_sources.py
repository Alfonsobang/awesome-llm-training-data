#!/usr/bin/env python3
"""Validate financial evaluation data-source governance metadata."""

from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parent
MANIFEST_PATH = ROOT / "data-sources" / "source-manifest.json"
SPEC_DIR = ROOT / "task-specs"

REQUIRED_SOURCE_FIELDS = {
    "source_id",
    "name",
    "source_type",
    "official_url",
    "access_method",
    "packaging_policy",
    "terms_review_required",
    "allowed_task_families",
    "temporal_fields",
    "required_citation_fields",
    "notes",
}
ALLOWED_PACKAGING_POLICIES = {
    "bundled_synthetic_only",
    "do_not_package_without_review",
    "reference_only",
}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate_manifest() -> tuple[dict, list[str]]:
    manifest = load_json(MANIFEST_PATH)
    errors: list[str] = []
    if not isinstance(manifest, dict):
        return {}, [f"{MANIFEST_PATH}: manifest must be a JSON object"]

    reviewed_on = manifest.get("reviewed_on")
    try:
        date.fromisoformat(reviewed_on)
    except (TypeError, ValueError):
        errors.append(f"{MANIFEST_PATH}: reviewed_on must be an ISO date")

    sources = manifest.get("sources")
    if not isinstance(sources, list) or not sources:
        errors.append(f"{MANIFEST_PATH}: sources must be a non-empty list")
        return manifest, errors

    seen_ids: set[str] = set()
    for index, source in enumerate(sources):
        prefix = f"{MANIFEST_PATH}: sources[{index}]"
        if not isinstance(source, dict):
            errors.append(f"{prefix}: source must be a JSON object")
            continue

        missing = sorted(REQUIRED_SOURCE_FIELDS - set(source))
        if missing:
            errors.append(f"{prefix}: missing fields: {', '.join(missing)}")
            continue

        source_id = source["source_id"]
        if not isinstance(source_id, str) or not source_id:
            errors.append(f"{prefix}: source_id must be a non-empty string")
        elif source_id in seen_ids:
            errors.append(f"{prefix}: duplicate source_id: {source_id}")
        else:
            seen_ids.add(source_id)

        if source["packaging_policy"] not in ALLOWED_PACKAGING_POLICIES:
            errors.append(
                f"{prefix}: unsupported packaging_policy: {source['packaging_policy']}"
            )
        if not isinstance(source["terms_review_required"], bool):
            errors.append(f"{prefix}: terms_review_required must be boolean")

        for field in (
            "allowed_task_families",
            "temporal_fields",
            "required_citation_fields",
        ):
            if not isinstance(source[field], list) or not source[field]:
                errors.append(f"{prefix}: {field} must be a non-empty list")

        official_url = source["official_url"]
        parsed = urlparse(official_url)
        if source["source_type"] == "synthetic_fixture":
            if parsed.scheme != "fixture":
                errors.append(f"{prefix}: synthetic fixtures should use fixture:// URI")
        elif parsed.scheme != "https":
            errors.append(f"{prefix}: external official_url must use https")

    return manifest, errors


def validate_task_source_refs(manifest: dict) -> list[str]:
    errors: list[str] = []
    sources = {
        source["source_id"]: source
        for source in manifest.get("sources", [])
        if isinstance(source, dict) and isinstance(source.get("source_id"), str)
    }

    for path in sorted(SPEC_DIR.glob("*.json")):
        spec = load_json(path)
        source_refs = spec.get("source_refs")
        if not isinstance(source_refs, list) or not source_refs:
            errors.append(f"{path}: source_refs must be a non-empty list")
            continue

        family = spec.get("family")
        for source_id in source_refs:
            source = sources.get(source_id)
            if source is None:
                errors.append(f"{path}: unknown source_ref: {source_id}")
                continue
            if family not in source["allowed_task_families"]:
                errors.append(
                    f"{path}: source_ref {source_id} does not allow task family {family}"
                )

    return errors


def main() -> int:
    manifest, errors = validate_manifest()
    errors.extend(validate_task_source_refs(manifest))

    if errors:
        print("Financial data-source validation failed:", file=sys.stderr)
        print("\n".join(errors), file=sys.stderr)
        return 1

    print(
        "Validated "
        f"{len(manifest['sources'])} governed financial data sources and "
        f"{len(list(SPEC_DIR.glob('*.json')))} task source mappings."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
