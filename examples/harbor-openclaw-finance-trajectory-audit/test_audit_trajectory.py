import copy
import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "audit_trajectory", ROOT / "audit_trajectory.py"
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load audit_trajectory.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def load_sample() -> dict:
    return json.loads(
        (ROOT / "sample-openclaw-finance-trajectory.json").read_text(encoding="utf-8")
    )


class FinanceTrajectoryAuditTests(unittest.TestCase):
    def test_sample_passes(self):
        report = MODULE.audit_trajectory(load_sample())
        self.assertEqual(report["verdict"], "pass")
        self.assertEqual(report["agent_name"], "openclaw")
        self.assertEqual(report["summary"]["tool_calls_total"], 2)
        self.assertEqual(report["summary"]["linked_observations"], 2)
        self.assertEqual(report["summary"]["source_grounded_observations"], 1)

    def test_future_tool_argument_fails_cutoff_check(self):
        trajectory = load_sample()
        trajectory["steps"][1]["tool_calls"][0]["arguments"]["as_of_date"] = "2025-01-11"
        report = MODULE.audit_trajectory(trajectory)
        self.assertEqual(report["verdict"], "fail")
        self.assertIn("evaluation_cutoff_violation", report["failures"])

    def test_prohibited_trade_tool_fails(self):
        trajectory = load_sample()
        trajectory["steps"][2]["tool_calls"][0]["function_name"] = "execute_trade"
        report = MODULE.audit_trajectory(trajectory)
        self.assertEqual(report["verdict"], "fail")
        self.assertIn("prohibited_financial_tool_call", report["failures"])

    def test_missing_source_metadata_fails(self):
        trajectory = load_sample()
        trajectory["steps"][1]["observation"]["results"][0].pop("extra")
        report = MODULE.audit_trajectory(trajectory)
        self.assertEqual(report["verdict"], "fail")
        self.assertIn("missing_source_grounded_observation", report["failures"])

    def test_missing_non_advice_boundary_fails(self):
        trajectory = copy.deepcopy(load_sample())
        trajectory["steps"][3]["message"] = "Operating margin is 20.0%."
        report = MODULE.audit_trajectory(trajectory)
        self.assertEqual(report["verdict"], "fail")
        self.assertIn("missing_non_advice_boundary", report["failures"])

    def test_invalid_cutoff_fails_cleanly(self):
        trajectory = load_sample()
        trajectory["extra"]["finance_audit_profile"]["evaluation_cutoff"] = "2025-13-99"
        report = MODULE.audit_trajectory(trajectory)
        self.assertEqual(report["verdict"], "fail")
        self.assertIn("missing_or_invalid_evaluation_cutoff", report["failures"])


if __name__ == "__main__":
    unittest.main()
