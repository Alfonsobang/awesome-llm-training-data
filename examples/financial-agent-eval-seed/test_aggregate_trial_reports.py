import tempfile
import unittest
from pathlib import Path

import aggregate_trial_reports as aggregate


class AggregateTrialReportsTests(unittest.TestCase):
    def test_default_reports_produce_stability_metrics(self):
        reports = [(path, aggregate.load_report(path)) for path in aggregate.DEFAULT_REPORTS]
        data = aggregate.build_report(reports)
        self.assertEqual(data["tasks_total"], 10)
        self.assertEqual(data["task_trials_total"], 20)
        self.assertEqual(data["per_attempt_pass_rate"], 0.5)
        self.assertEqual(data["task_pass_rate"], 1.0)
        self.assertEqual(data["task_all_attempts_pass_rate"], 0.0)
        self.assertEqual(data["pass_at_k"]["1"], 1.0)
        self.assertEqual(data["pass_at_k"]["2"], 1.0)
        self.assertEqual(data["pass_pow_k"]["2"], 0.0)
        self.assertIsNone(data["unsafe_output_rate"])

    def test_missing_evidence_detection(self):
        run = {
            "task_id": "example-task",
            "status": "fail",
            "artifact": "missing/answer.json",
            "stderr_tail": "Missing candidate artifact: missing/answer.json",
        }
        data = aggregate.build_report(
            [
                (
                    Path("missing-report.json"),
                    {
                        "benchmark": "financial-agent-eval-seed",
                        "runs": [run],
                    },
                )
            ]
        )
        self.assertEqual(data["missing_evidence_rate"], 1.0)

    def test_writes_markdown_report(self):
        reports = [(path, aggregate.load_report(path)) for path in aggregate.DEFAULT_REPORTS]
        data = aggregate.build_report(reports)
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "report.md"
            aggregate.write_markdown(data, output)
            text = output.read_text(encoding="utf-8")
        self.assertIn("Repeated-trial Report", text)
        self.assertIn("pass@k", text)
        self.assertIn("Pass^k", text)


if __name__ == "__main__":
    unittest.main()
