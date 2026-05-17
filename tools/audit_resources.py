#!/usr/bin/env python3
"""Audit Awesome list resource entries for basic quality rules."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path


ALLOWED_TAGS = {
    "tool",
    "paper",
    "dataset",
    "benchmark",
    "governance",
    "report",
    "platform",
}

RESOURCE_LINE_RE = re.compile(
    r"^- \[(?P<name>[^\]]+)\]\((?P<link>[^)]+)\) - Tag: \[(?P<tag>[^\]]+)\] - (?P<description>.+)$"
)

RESOURCE_SECTIONS = {
    "Start Here",
    "Training Data Quality",
    "Data Cleaning and Deduplication",
    "Dataset Inspection Tools",
    "Annotation Platforms",
    "Annotation Quality and Agreement",
    "Human Preference Data",
    "RLHF / DPO / RLAIF Data",
    "Synthetic Data",
    "RAG Evaluation Data",
    "Financial-domain LLM Data",
    "Data Governance",
    "Privacy and Compliance",
    "Papers",
    "Open-source Tools",
    "Reports and Playbooks",
    "入门资源",
    "训练数据质量",
    "数据清洗与去重",
    "数据集检查工具",
    "标注平台",
    "标注质量与一致性",
    "人类偏好数据",
    "RLHF / DPO / RLAIF 数据",
    "合成数据",
    "RAG 评测数据",
    "金融领域 LLM 数据",
    "数据治理",
    "隐私与合规",
    "论文",
    "开源工具",
    "报告与实践手册",
}


class AuditError(Exception):
    """Raised when the audit finds a blocking issue."""


def iter_section_lines(path: Path) -> list[tuple[int, str, str]]:
    current_section = ""
    rows: list[tuple[int, str, str]] = []

    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if raw_line.startswith("## "):
            current_section = raw_line[3:].strip()
        rows.append((line_number, current_section, raw_line))

    return rows


def audit_file(path: Path) -> list[dict[str, str | int]]:
    errors: list[str] = []
    resources: list[dict[str, str | int]] = []

    for line_number, section, line in iter_section_lines(path):
        if not line.startswith("- ["):
            continue

        in_resource_section = section in RESOURCE_SECTIONS
        has_tag = " - Tag: [" in line

        if in_resource_section and not has_tag:
            errors.append(f"{path}:{line_number}: resource item is missing required Tag format")
            continue

        if not has_tag:
            continue

        match = RESOURCE_LINE_RE.match(line)
        if not match:
            errors.append(f"{path}:{line_number}: resource item does not match required format")
            continue

        name = match.group("name").strip()
        link = match.group("link").strip()
        tag = match.group("tag").strip()
        description = match.group("description").strip()

        if tag not in ALLOWED_TAGS:
            errors.append(f"{path}:{line_number}: invalid tag [{tag}]")
        if not link.startswith(("https://", "http://")):
            errors.append(f"{path}:{line_number}: link must be an absolute HTTP(S) URL")
        if "example.com" in link or "OWNER/" in link:
            errors.append(f"{path}:{line_number}: placeholder link detected")
        if len(description.split()) < 5 and path.name == "README.md":
            errors.append(f"{path}:{line_number}: English description is too short")
        if name.lower() in {"todo", "tbd", "unknown"}:
            errors.append(f"{path}:{line_number}: placeholder resource name detected")

        resources.append(
            {
                "file": path.name,
                "line": line_number,
                "section": section,
                "name": name,
                "link": link,
                "tag": tag,
            }
        )

    if errors:
        raise AuditError("\n".join(errors))

    return resources


def audit_pair(english: list[dict[str, str | int]], chinese: list[dict[str, str | int]]) -> list[str]:
    errors: list[str] = []

    if len(english) != len(chinese):
        errors.append(f"README resource count mismatch: README.md={len(english)}, README.zh-CN.md={len(chinese)}")

    english_tags = Counter(str(item["tag"]) for item in english)
    chinese_tags = Counter(str(item["tag"]) for item in chinese)
    if english_tags != chinese_tags:
        errors.append(f"README tag distribution mismatch: README.md={english_tags}, README.zh-CN.md={chinese_tags}")

    english_links = Counter(str(item["link"]) for item in english)
    duplicate_links = sorted(link for link, count in english_links.items() if count > 2)
    if duplicate_links:
        errors.append("Links appear more than twice in README.md: " + ", ".join(duplicate_links))

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit Awesome LLM Training Data resource entries.")
    parser.add_argument("--root", default=".", help="Repository root")
    args = parser.parse_args()

    root = Path(args.root)
    readme = root / "README.md"
    readme_zh = root / "README.zh-CN.md"

    try:
        english_resources = audit_file(readme)
        chinese_resources = audit_file(readme_zh)
        pair_errors = audit_pair(english_resources, chinese_resources)
        if pair_errors:
            raise AuditError("\n".join(pair_errors))
    except AuditError as exc:
        print("Resource audit failed:", file=sys.stderr)
        print(exc, file=sys.stderr)
        return 1

    print("Resource audit passed.")
    print(f"README.md resources: {len(english_resources)}")
    print(f"README.zh-CN.md resources: {len(chinese_resources)}")
    print("Tag distribution:")
    for tag, count in sorted(Counter(str(item["tag"]) for item in english_resources).items()):
        print(f"  {tag}: {count}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
