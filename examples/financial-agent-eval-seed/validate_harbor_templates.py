#!/usr/bin/env python3
"""Run verifier tests for every Harbor-style financial task template."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TEMPLATE_DIR = ROOT / "harbor-template"


def main() -> int:
    tests_dirs = sorted(path for path in TEMPLATE_DIR.glob("*/tests") if path.is_dir())
    if not tests_dirs:
        print(f"No Harbor template tests found in {TEMPLATE_DIR}", file=sys.stderr)
        return 1

    failures: list[str] = []
    for tests_dir in tests_dirs:
        template_name = tests_dir.parent.name
        print(f"Validating Harbor template: {template_name}")
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "unittest",
                "discover",
                "-s",
                str(tests_dir),
                "-p",
                "test_*.py",
            ],
            cwd=ROOT,
            check=False,
        )
        if result.returncode != 0:
            failures.append(template_name)

    if failures:
        print("Template validation failed: " + ", ".join(failures), file=sys.stderr)
        return 1

    print(f"Validated {len(tests_dirs)} Harbor-style financial task templates.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
