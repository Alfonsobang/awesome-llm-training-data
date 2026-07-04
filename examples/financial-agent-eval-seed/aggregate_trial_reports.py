#!/usr/bin/env python3
"""Aggregate multiple financial-agent eval reports into repeated-trial metrics."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
DEFAULT_RESULTS_DIR = ROOT / "results"
DEFAULT_REPORTS = [
    DEFAULT_RESULTS_DIR / "example-report.json",
    DEFAULT_RESULTS_DIR / "bad-finance-agent-report.json",
]
DEFAULT_OUTPUT_JSON = DEFAULT_RESULTS_DIR / "repeated-trial-example-report.json"
DEFAULT_OUTPUT_MD = DEFAULT_RESULTS_DIR / "repeated-trial-example-report.md"
K_VALUES = (1, 2, 3, 5, 10)


def load_report(path: Path) -> dict[str, Any]:
    try:
        report = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError(f"Missing report: {path}") from None
    except json.JSONDecodeError as exc:
        raise ValueError(f"{path}: invalid JSON: {exc}") from None

    if not isinstance(report, dict):
        raise ValueError(f"{path}: report must be a JSON object")
    if not isinstance(report.get("runs"), list):
        raise ValueError(f"{path}: report must contain a runs list")
    return report


def is_pass(run: dict[str, Any]) -> bool:
    return run.get("status") == "pass"


def has_missing_evidence(run: dict[str, Any]) -> bool:
    text = " ".join(
        str(run.get(field, "")).lower()
        for field in ("status", "artifact", "stderr_tail")
    )
    missing_markers = (
        "missing candidate artifact",
        "missing evidence",
        "missing artifact",
        "no usable artifact",
    )
    return any(marker in text for marker in missing_markers)


def unsafe_output_flag(run: dict[str, Any]) -> bool | None:
    if isinstance(run.get("unsafe_output"), bool):
        return run["unsafe_output"]
    risk_flags = run.get("risk_flags")
    if isinstance(risk_flags, dict) and isinstance(risk_flags.get("unsafe_output"), bool):
        return risk_flags["unsafe_output"]
    return None


def pct(numerator: int | float, denominator: int | float) -> float:
    return round(numerator / denominator, 4) if denominator else 0.0


def build_report(reports: list[tuple[Path, dict[str, Any]]]) -> dict[str, Any]:
    task_trials: dict[str, list[dict[str, Any]]] = defaultdict(list)
    missing_evidence_count = 0
    unsafe_known = 0
    unsafe_count = 0

    for trial_index, (path, report) in enumerate(reports, start=1):
        trial_name = path.stem
        for run in report["runs"]:
            if not isinstance(run, dict):
                continue
            task_id = str(run.get("task_id", "")).strip()
            if not task_id:
                continue
            passed = is_pass(run)
            missing_evidence = has_missing_evidence(run)
            unsafe_flag = unsafe_output_flag(run)
            if missing_evidence:
                missing_evidence_count += 1
            if unsafe_flag is not None:
                unsafe_known += 1
                unsafe_count += int(unsafe_flag)
            task_trials[task_id].append(
                {
                    "trial_index": trial_index,
                    "trial_name": trial_name,
                    "report_path": display_path(path),
                    "passed": passed,
                    "status": "pass" if passed else "fail",
                    "artifact": run.get("artifact", ""),
                    "missing_evidence": missing_evidence,
                }
            )

    all_trials = [trial for trials in task_trials.values() for trial in trials]
    total_trials = len(all_trials)
    task_count = len(task_trials)
    max_attempts = max((len(trials) for trials in task_trials.values()), default=0)
    k_values = [k for k in K_VALUES if k <= max_attempts]

    pass_at_k = {}
    pass_pow_k = {}
    for k in k_values:
        eligible = [trials for trials in task_trials.values() if len(trials) >= k]
        pass_at_k[str(k)] = pct(
            sum(any(trial["passed"] for trial in trials[:k]) for trials in eligible),
            len(eligible),
        )
        pass_pow_k[str(k)] = pct(
            sum(all(trial["passed"] for trial in trials[:k]) for trials in eligible),
            len(eligible),
        )

    per_task = []
    for task_id, trials in sorted(task_trials.items()):
        passes = sum(trial["passed"] for trial in trials)
        per_task.append(
            {
                "task_id": task_id,
                "trials": len(trials),
                "passes": passes,
                "failures": len(trials) - passes,
                "ever_passed": passes > 0,
                "all_passed": passes == len(trials),
                "missing_evidence_trials": sum(trial["missing_evidence"] for trial in trials),
            }
        )

    return {
        "benchmark": "financial-agent-eval-seed",
        "report_type": "repeated-trial-aggregate",
        "input_reports": [display_path(path) for path, _ in reports],
        "reports_total": len(reports),
        "tasks_total": task_count,
        "task_trials_total": total_trials,
        "per_attempt_pass_rate": pct(sum(trial["passed"] for trial in all_trials), total_trials),
        "task_pass_rate": pct(sum(any(trial["passed"] for trial in trials) for trials in task_trials.values()), task_count),
        "task_all_attempts_pass_rate": pct(
            sum(all(trial["passed"] for trial in trials) for trials in task_trials.values()),
            task_count,
        ),
        "missing_evidence_rate": pct(missing_evidence_count, total_trials),
        "unsafe_output_rate": pct(unsafe_count, unsafe_known) if unsafe_known else None,
        "unsafe_output_observation_count": unsafe_known,
        "pass_at_k": pass_at_k,
        "pass_pow_k": pass_pow_k,
        "per_task": per_task,
        "notes": [
            "This aggregate is a repeated-trial reporting example, not a model leaderboard.",
            "unsafe_output_rate is null unless input reports provide explicit unsafe_output or risk_flags.unsafe_output fields.",
            "missing_evidence_rate is inferred from verifier report text and missing-artifact markers.",
        ],
    }


def display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        try:
            return path.resolve().relative_to(ROOT.parents[1]).as_posix()
        except ValueError:
            return path.as_posix()


def write_markdown(report: dict[str, Any], path: Path) -> None:
    pass_at = ", ".join(f"`{k}`: {value}" for k, value in report["pass_at_k"].items()) or "n/a"
    pass_pow = ", ".join(f"`{k}`: {value}" for k, value in report["pass_pow_k"].items()) or "n/a"
    unsafe_rate = report["unsafe_output_rate"]
    unsafe_text = "`null` (no explicit unsafe-output flags in input reports)" if unsafe_rate is None else str(unsafe_rate)

    rows = [
        "| Task | Trials | Passes | Failures | Ever passed | All passed | Missing evidence trials |",
        "| --- | ---: | ---: | ---: | --- | --- | ---: |",
    ]
    for item in report["per_task"]:
        rows.append(
            "| `{task_id}` | {trials} | {passes} | {failures} | `{ever}` | `{all_passed}` | {missing} |".format(
                task_id=item["task_id"],
                trials=item["trials"],
                passes=item["passes"],
                failures=item["failures"],
                ever=str(item["ever_passed"]).lower(),
                all_passed=str(item["all_passed"]).lower(),
                missing=item["missing_evidence_trials"],
            )
        )

    body = "\n".join(
        [
            "# Financial Agent Eval Seed Repeated-trial Report",
            "",
            "This report aggregates multiple deterministic verifier reports. It is a stability and evidence report, not a leaderboard.",
            "",
            f"- Input reports: {report['reports_total']}",
            f"- Tasks total: {report['tasks_total']}",
            f"- Task trials total: {report['task_trials_total']}",
            f"- Per-attempt pass rate: {report['per_attempt_pass_rate']}",
            f"- Task pass rate: {report['task_pass_rate']}",
            f"- Task all-attempts-pass rate: {report['task_all_attempts_pass_rate']}",
            f"- Missing-evidence rate: {report['missing_evidence_rate']}",
            f"- Unsafe-output rate: {unsafe_text}",
            f"- pass@k: {pass_at}",
            f"- Pass^k: {pass_pow}",
            "",
            "## Per-task Summary",
            "",
            *rows,
            "",
            "## Notes",
            "",
            "- `pass@k` reports whether a task has at least one passing attempt in the first `k` trials.",
            "- `Pass^k` reports whether all of the first `k` attempts pass.",
            "- The checked-in example intentionally combines the reference report and known-bad report to demonstrate that stability metrics reveal brittle behavior.",
            "- This report does not provide investment advice, trading signals, private data, real user data, or production-readiness claims.",
            "",
        ]
    )
    path.write_text(body, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--report",
        action="append",
        type=Path,
        dest="reports",
        help="Input JSON report from run_finance_eval.py. Can be provided multiple times.",
    )
    parser.add_argument(
        "--output-json",
        type=Path,
        default=DEFAULT_OUTPUT_JSON,
        help="Output JSON aggregate report.",
    )
    parser.add_argument(
        "--output-md",
        type=Path,
        default=DEFAULT_OUTPUT_MD,
        help="Output Markdown aggregate report.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report_paths = args.reports or DEFAULT_REPORTS
    reports = [(path, load_report(path)) for path in report_paths]
    aggregate = build_report(reports)

    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_md.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(aggregate, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_markdown(aggregate, args.output_md)

    print(f"Wrote {display_path(args.output_json)}")
    print(f"Wrote {display_path(args.output_md)}")
    print(
        "Repeated-trial report: "
        f"{aggregate['tasks_total']} tasks, "
        f"{aggregate['task_trials_total']} task trials, "
        f"pass@k={aggregate['pass_at_k']}, "
        f"Pass^k={aggregate['pass_pow_k']}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
