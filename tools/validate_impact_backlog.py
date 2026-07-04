#!/usr/bin/env python3
"""Validate the impact backlog used to drive project work."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BACKLOG_PATH = ROOT / "impact" / "impact-backlog.json"

REQUIRED_TOP_LEVEL = {"schema_version", "updated_on", "positioning", "tracks"}
REQUIRED_TRACK_FIELDS = {
    "id",
    "title",
    "track",
    "priority",
    "status",
    "source_page",
    "next_artifact",
    "why_it_matters",
    "acceptance_criteria",
}
ALLOWED_PRIORITIES = {"P0", "P1", "P2"}
ALLOWED_STATUSES = {"planned", "in_progress", "completed"}


def load_backlog() -> dict:
    try:
        return json.loads(BACKLOG_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError(f"Missing backlog file: {BACKLOG_PATH}") from None
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {BACKLOG_PATH}: {exc}") from None


def validate_backlog(backlog: dict) -> list[str]:
    errors: list[str] = []

    if not isinstance(backlog, dict):
        return ["Backlog must be a JSON object."]

    missing = sorted(REQUIRED_TOP_LEVEL - set(backlog))
    if missing:
        errors.append(f"Missing top-level fields: {', '.join(missing)}")

    tracks = backlog.get("tracks")
    if not isinstance(tracks, list) or not tracks:
        errors.append("tracks must be a non-empty list.")
        return errors

    seen_ids: set[str] = set()
    p0_count = 0
    for index, item in enumerate(tracks, start=1):
        if not isinstance(item, dict):
            errors.append(f"tracks[{index}] must be an object.")
            continue

        missing_fields = sorted(REQUIRED_TRACK_FIELDS - set(item))
        if missing_fields:
            errors.append(f"{item.get('id', f'tracks[{index}]')}: missing fields: {', '.join(missing_fields)}")
            continue

        track_id = item["id"]
        if not isinstance(track_id, str) or not track_id:
            errors.append(f"tracks[{index}]: id must be a non-empty string.")
        elif track_id in seen_ids:
            errors.append(f"{track_id}: duplicate id.")
        else:
            seen_ids.add(track_id)

        priority = item["priority"]
        if priority not in ALLOWED_PRIORITIES:
            errors.append(f"{track_id}: priority must be one of {sorted(ALLOWED_PRIORITIES)}.")
        if priority == "P0":
            p0_count += 1

        status = item["status"]
        if status not in ALLOWED_STATUSES:
            errors.append(f"{track_id}: status must be one of {sorted(ALLOWED_STATUSES)}.")

        source_page = ROOT / item["source_page"]
        if not source_page.exists():
            errors.append(f"{track_id}: source_page does not exist: {item['source_page']}")

        criteria = item["acceptance_criteria"]
        if not isinstance(criteria, list) or len(criteria) < 3:
            errors.append(f"{track_id}: acceptance_criteria must contain at least three items.")
        elif not all(isinstance(value, str) and value.strip() for value in criteria):
            errors.append(f"{track_id}: acceptance_criteria must be non-empty strings.")

        for text_field in ("title", "track", "next_artifact", "why_it_matters"):
            if not isinstance(item[text_field], str) or not item[text_field].strip():
                errors.append(f"{track_id}: {text_field} must be a non-empty string.")

    if p0_count == 0:
        errors.append("At least one P0 item is required.")

    return errors


def main() -> int:
    try:
        backlog = load_backlog()
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    errors = validate_backlog(backlog)
    if errors:
        print("Impact backlog validation failed:", file=sys.stderr)
        print("\n".join(errors), file=sys.stderr)
        return 1

    print(f"Validated {len(backlog['tracks'])} impact backlog items.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
