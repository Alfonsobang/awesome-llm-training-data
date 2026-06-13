#!/usr/bin/env python3
"""Run the local financial agent evaluation seed and write a small report."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TEMPLATE_DIR = ROOT / "harbor-template"
DEFAULT_RESULTS_DIR = ROOT / "results"


@dataclass(frozen=True)
class TaskRun:
    task_id: str
    artifact: str
    passed: bool
    duration_seconds: float
    stdout: str
    stderr: str

    @property
    def status(self) -> str:
        return "pass" if self.passed else "fail"


def discover_task_dirs() -> list[Path]:
    return sorted(
        path
        for path in TEMPLATE_DIR.iterdir()
        if path.is_dir() and (path / "tests").is_dir()
    )


def resolve_artifact(task_dir: Path, artifact_root: Path | None) -> Path:
    if artifact_root:
        return artifact_root / task_dir.name / "answer.json"
    return task_dir / "solution" / "answer.json"


def run_task(task_dir: Path, artifact: Path) -> TaskRun:
    if not artifact.exists():
        return TaskRun(
            task_id=task_dir.name,
            artifact=display_path(artifact),
            passed=False,
            duration_seconds=0.0,
            stdout="",
            stderr=f"Missing candidate artifact: {artifact}",
        )

    env = os.environ.copy()
    env["FINANCE_AGENT_ARTIFACT"] = str(artifact.resolve())
    start = time.perf_counter()
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "unittest",
            "discover",
            "-s",
            str(task_dir / "tests"),
            "-p",
            "test_*.py",
        ],
        cwd=ROOT,
        env=env,
        check=False,
        capture_output=True,
        text=True,
    )
    duration = time.perf_counter() - start
    return TaskRun(
        task_id=task_dir.name,
        artifact=display_path(artifact),
        passed=result.returncode == 0,
        duration_seconds=round(duration, 3),
        stdout=result.stdout.strip(),
        stderr=result.stderr.strip(),
    )


def display_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def build_report(runs: list[TaskRun], artifact_root: Path | None) -> dict:
    passed = sum(1 for run in runs if run.passed)
    total = len(runs)
    return {
        "benchmark": "financial-agent-eval-seed",
        "artifact_root": str(artifact_root) if artifact_root else "included reference solutions",
        "tasks_total": total,
        "tasks_passed": passed,
        "tasks_failed": total - passed,
        "pass_rate": round(passed / total, 4) if total else 0.0,
        "runs": [
            {
                "task_id": run.task_id,
                "artifact": run.artifact,
                "status": run.status,
                "duration_seconds": run.duration_seconds,
                "stderr_tail": tail(run.stderr),
            }
            for run in runs
        ],
    }


def tail(text: str, lines: int = 12) -> str:
    if not text:
        return ""
    return "\n".join(text.splitlines()[-lines:])


def write_markdown(report: dict, path: Path) -> None:
    rows = [
        "| Task | Status | Artifact | Duration |",
        "| --- | --- | --- | ---: |",
    ]
    for run in report["runs"]:
        rows.append(
            f"| `{run['task_id']}` | `{run['status']}` | `{run['artifact']}` | {run['duration_seconds']}s |"
        )

    body = "\n".join(
        [
            "# Financial Agent Eval Seed Report",
            "",
            "This report is generated from the local deterministic verifier suite. It is a starter report, not a leaderboard.",
            "",
            f"- Tasks total: {report['tasks_total']}",
            f"- Tasks passed: {report['tasks_passed']}",
            f"- Tasks failed: {report['tasks_failed']}",
            f"- Pass rate: {report['pass_rate']}",
            f"- Artifact root: {report['artifact_root']}",
            "",
            *rows,
            "",
            "Safety note: this seed uses synthetic fixtures and public-source task patterns. It does not provide investment advice, trading signals, private data, or production-readiness claims.",
            "",
        ]
    )
    path.write_text(body, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--artifact-root",
        type=Path,
        default=None,
        help="Optional directory containing <task-id>/answer.json candidate artifacts.",
    )
    parser.add_argument(
        "--results-dir",
        type=Path,
        default=DEFAULT_RESULTS_DIR,
        help="Directory for generated JSON and Markdown reports.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    task_dirs = discover_task_dirs()
    if not task_dirs:
        print(f"No financial task templates found in {TEMPLATE_DIR}", file=sys.stderr)
        return 1

    runs = [run_task(task_dir, resolve_artifact(task_dir, args.artifact_root)) for task_dir in task_dirs]
    report = build_report(runs, args.artifact_root)

    args.results_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.results_dir / "latest-report.json"
    md_path = args.results_dir / "latest-report.md"
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_markdown(report, md_path)

    print(f"Wrote {display_path(json_path.resolve())}")
    print(f"Wrote {display_path(md_path.resolve())}")
    print(f"Pass rate: {report['tasks_passed']}/{report['tasks_total']} ({report['pass_rate']})")
    return 0 if report["tasks_failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
