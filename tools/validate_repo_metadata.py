#!/usr/bin/env python3
"""Validate desired repository metadata and optionally compare it with GitHub."""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
METADATA_PATH = ROOT / ".github" / "repo-metadata.json"
REQUIRED_FIELDS = {"repository", "description", "homepage", "topics", "must_not_claim", "notes"}
REQUIRED_TOPIC_HINTS = {"agent-evaluation", "financial-ai", "rag-evaluation", "data-governance"}
DISALLOWED_DESCRIPTION_TERMS = {
    "best",
    "official harbor",
    "production-ready",
    "investment advice",
    "trading signals",
    "guaranteed",
}


def load_metadata(path: Path = METADATA_PATH) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError(f"Missing metadata spec: {path}") from None
    except json.JSONDecodeError as exc:
        raise ValueError(f"{path}: invalid JSON: {exc}") from None


def validate_spec(metadata: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    missing = sorted(REQUIRED_FIELDS - set(metadata))
    if missing:
        return [f"repo metadata: missing fields: {', '.join(missing)}"]

    description = metadata["description"]
    if not isinstance(description, str) or not description.strip():
        errors.append("description must be a non-empty string.")
    elif len(description) > 160:
        errors.append("description should fit GitHub's short repository description field.")

    desc_lower = str(description).lower()
    for term in ("financial", "agent", "evaluation"):
        if term not in desc_lower:
            errors.append(f"description should mention {term}.")
    for term in DISALLOWED_DESCRIPTION_TERMS:
        if term in desc_lower:
            errors.append(f"description contains disallowed term: {term}")

    topics = metadata["topics"]
    if not isinstance(topics, list) or not topics:
        errors.append("topics must be a non-empty list.")
    elif not all(isinstance(topic, str) and topic.strip() for topic in topics):
        errors.append("topics must contain non-empty strings.")
    else:
        normalized_topics = [topic.strip().lower() for topic in topics]
        if normalized_topics != sorted(normalized_topics):
            errors.append("topics should be sorted for stable diffs.")
        if len(normalized_topics) != len(set(normalized_topics)):
            errors.append("topics must not contain duplicates.")
        missing_topics = sorted(REQUIRED_TOPIC_HINTS - set(normalized_topics))
        if missing_topics:
            errors.append(f"topics missing required hints: {', '.join(missing_topics)}")

    must_not_claim = " ".join(str(item).lower() for item in metadata["must_not_claim"])
    for term in ("official harbor", "production", "investment advice", "trading signals", "adoption"):
        if term not in must_not_claim:
            errors.append(f"must_not_claim should include {term}.")

    return errors


def fetch_live_repo(repository: str) -> dict[str, Any]:
    url = f"https://api.github.com/repos/{repository}"
    request = urllib.request.Request(url, headers={"User-Agent": "repo-metadata-validator"})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        raise ValueError(f"GitHub API returned {exc.code} for {url}") from exc
    except urllib.error.URLError as exc:
        raise ValueError(f"Could not reach GitHub API: {exc.reason}") from exc


def validate_live(metadata: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    live = fetch_live_repo(metadata["repository"])
    if live.get("description") != metadata["description"]:
        errors.append(
            "live description mismatch: "
            f"expected {metadata['description']!r}, got {live.get('description')!r}"
        )
    live_topics = sorted(str(topic).lower() for topic in live.get("topics", []))
    desired_topics = sorted(str(topic).lower() for topic in metadata["topics"])
    if live_topics != desired_topics:
        errors.append(
            "live topics mismatch: "
            f"expected {desired_topics}, got {live_topics}"
        )
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--live",
        action="store_true",
        help="Also compare .github/repo-metadata.json with live GitHub repository metadata.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        metadata = load_metadata()
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    errors = validate_spec(metadata)
    if args.live and not errors:
        try:
            errors.extend(validate_live(metadata))
        except ValueError as exc:
            errors.append(str(exc))

    if errors:
        print("Repository metadata validation failed:", file=sys.stderr)
        print("\n".join(errors), file=sys.stderr)
        return 1

    mode = "live metadata" if args.live else "metadata spec"
    print(f"Validated repository {mode}: {metadata['repository']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

