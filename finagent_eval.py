#!/usr/bin/env python3
"""Convenience CLI for the public-safe financial-agent evaluation seed."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SEED_DIR = ROOT / "examples" / "financial-agent-eval-seed"
RESULTS_DIR = SEED_DIR / "results"
RUNNER = SEED_DIR / "run_finance_eval.py"
SCORECARD_BUILDER = SEED_DIR / "build_scorecard.py"
DEFAULT_LATEST_REPORT = RESULTS_DIR / "latest-report.json"
DEFAULT_LATEST_SCORECARD = RESULTS_DIR / "latest-scorecard"


def display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def run_command(args: list[str], *, allow_failure: bool = False) -> int:
    print("$ " + " ".join(args))
    result = subprocess.run(args, cwd=ROOT, check=False)
    if result.returncode != 0 and not allow_failure:
        return result.returncode
    return 0


def command_demo(args: argparse.Namespace) -> int:
    report_path = args.report
    scorecard_prefix = args.scorecard_prefix
    run_args = [
        sys.executable,
        display_path(RUNNER),
        "--results-dir",
        display_path(report_path.parent),
    ]
    exit_code = run_command(run_args)
    if exit_code != 0:
        return exit_code

    scorecard_args = [
        sys.executable,
        display_path(SCORECARD_BUILDER),
        "--report",
        display_path(report_path),
        "--candidate",
        args.candidate,
        "--output-prefix",
        display_path(scorecard_prefix),
    ]
    exit_code = run_command(scorecard_args)
    if exit_code != 0:
        return exit_code

    print("")
    print("Generated:")
    print(f"- {display_path(report_path)}")
    print(f"- {display_path(report_path.with_suffix('.md'))}")
    print(f"- {display_path(scorecard_prefix.with_suffix('.json'))}")
    print(f"- {display_path(scorecard_prefix.with_suffix('.md'))}")
    print("")
    print("Safety note: this is a public-safe seed, not investment advice or production evidence.")
    return 0


def command_run(args: argparse.Namespace) -> int:
    cmd = [sys.executable, display_path(RUNNER)]
    if args.artifact_root:
        cmd.extend(["--artifact-root", display_path(args.artifact_root)])
    if args.results_dir:
        cmd.extend(["--results-dir", display_path(args.results_dir)])
    return run_command(cmd, allow_failure=args.allow_failure)


def command_scorecard(args: argparse.Namespace) -> int:
    cmd = [
        sys.executable,
        display_path(SCORECARD_BUILDER),
        "--report",
        display_path(args.report),
        "--candidate",
        args.candidate,
        "--output-prefix",
        display_path(args.output_prefix),
    ]
    if args.allow_red_flags:
        cmd.append("--allow-red-flags")
    return run_command(cmd)


def command_bad_demo(args: argparse.Namespace) -> int:
    report_prefix = RESULTS_DIR / "latest-bad-candidate-report"
    report_json = report_prefix.with_suffix(".json")
    scorecard_prefix = RESULTS_DIR / "latest-bad-candidate-scorecard"
    bad_artifacts = SEED_DIR / "candidate-artifacts" / "bad-finance-agent"

    run_args = [
        sys.executable,
        display_path(RUNNER),
        "--artifact-root",
        display_path(bad_artifacts),
        "--results-dir",
        display_path(RESULTS_DIR),
    ]
    run_command(run_args, allow_failure=True)

    latest_json = RESULTS_DIR / "latest-report.json"
    if not latest_json.exists():
        print(f"Expected known-bad report was not generated: {display_path(latest_json)}", file=sys.stderr)
        return 1
    latest_md = RESULTS_DIR / "latest-report.md"
    latest_json.replace(report_json)
    if latest_md.exists():
        latest_md.replace(report_prefix.with_suffix(".md"))

    scorecard_args = [
        sys.executable,
        display_path(SCORECARD_BUILDER),
        "--report",
        display_path(report_json),
        "--candidate",
        args.candidate,
        "--output-prefix",
        display_path(scorecard_prefix),
        "--allow-red-flags",
    ]
    exit_code = run_command(scorecard_args)
    if exit_code != 0:
        return exit_code

    print("")
    print("Generated known-bad demo artifacts:")
    print(f"- {display_path(report_json)}")
    print(f"- {display_path(report_prefix.with_suffix('.md'))}")
    print(f"- {display_path(scorecard_prefix.with_suffix('.json'))}")
    print(f"- {display_path(scorecard_prefix.with_suffix('.md'))}")
    print("")
    print("This command intentionally demonstrates failing behavior and red flags.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    demo = subparsers.add_parser("demo", help="Run the reference seed and generate a scorecard.")
    demo.add_argument("--candidate", default="reference-solutions")
    demo.add_argument("--report", type=Path, default=DEFAULT_LATEST_REPORT)
    demo.add_argument("--scorecard-prefix", type=Path, default=DEFAULT_LATEST_SCORECARD)
    demo.set_defaults(func=command_demo)

    run = subparsers.add_parser("run", help="Run deterministic verifiers for candidate artifacts.")
    run.add_argument("--artifact-root", type=Path, default=None)
    run.add_argument("--results-dir", type=Path, default=None)
    run.add_argument("--allow-failure", action="store_true", help="Exit 0 even if verifiers fail.")
    run.set_defaults(func=command_run)

    scorecard = subparsers.add_parser("scorecard", help="Generate a scorecard from a verifier report.")
    scorecard.add_argument("--report", type=Path, required=True)
    scorecard.add_argument("--candidate", default="candidate")
    scorecard.add_argument("--output-prefix", type=Path, default=DEFAULT_LATEST_SCORECARD)
    scorecard.add_argument("--allow-red-flags", action="store_true")
    scorecard.set_defaults(func=command_scorecard)

    bad_demo = subparsers.add_parser("bad-demo", help="Generate known-bad report and scorecard examples.")
    bad_demo.add_argument("--candidate", default="known-bad-finance-agent")
    bad_demo.set_defaults(func=command_bad_demo)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
