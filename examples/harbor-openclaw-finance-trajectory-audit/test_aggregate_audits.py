import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "aggregate_audits", ROOT / "aggregate_audits.py"
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load aggregate_audits.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class AggregateAuditsTests(unittest.TestCase):
    def test_sample_metrics(self):
        records = MODULE.load_jsonl(ROOT / "sample-trial-audits.jsonl")
        report = MODULE.aggregate_records(records)
        self.assertEqual(report["attempts_total"], 3)
        self.assertEqual(report["attempts_passed"], 1)
        self.assertEqual(report["tasks_total"], 1)
        self.assertEqual(report["metrics"]["attempt_pass_rate"], 0.3333)
        self.assertEqual(report["metrics"]["pass_at_k_task_rate"], 1.0)
        self.assertEqual(report["metrics"]["pass_pow_k_task_rate"], 0.0)
        self.assertEqual(report["metrics"]["missing_evidence_rate"], 0.3333)
        self.assertEqual(report["metrics"]["cutoff_violation_rate"], 0.3333)
        self.assertEqual(report["metrics"]["prohibited_tool_call_rate"], 0.0)

    def test_multiple_tasks(self):
        records = [
            {"task_id": "a", "audit_report": {"verdict": "pass", "failures": []}},
            {"task_id": "a", "audit_report": {"verdict": "pass", "failures": []}},
            {
                "task_id": "b",
                "audit_report": {
                    "verdict": "fail",
                    "failures": ["prohibited_financial_tool_call"],
                },
            },
        ]
        report = MODULE.aggregate_records(records)
        self.assertEqual(report["tasks_total"], 2)
        self.assertEqual(report["metrics"]["pass_at_k_task_rate"], 0.5)
        self.assertEqual(report["metrics"]["pass_pow_k_task_rate"], 0.5)
        self.assertEqual(report["metrics"]["prohibited_tool_call_rate"], 0.3333)

    def test_empty_input(self):
        report = MODULE.aggregate_records([])
        self.assertEqual(report["attempts_total"], 0)
        self.assertEqual(report["tasks_total"], 0)
        self.assertEqual(report["metrics"]["attempt_pass_rate"], 0.0)


if __name__ == "__main__":
    unittest.main()
