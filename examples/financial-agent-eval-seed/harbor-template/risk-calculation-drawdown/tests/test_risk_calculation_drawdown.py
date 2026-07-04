import json
import os
import unittest
from pathlib import Path


TASK_DIR = Path(__file__).resolve().parents[1]
DEFAULT_ARTIFACT = TASK_DIR / "solution" / "answer.json"
FIXTURE_PATH = TASK_DIR / "fixtures" / "synthetic_portfolio_values.csv"
ARTIFACT_PATH = Path(os.environ.get("FINANCE_AGENT_ARTIFACT", "/logs/artifacts/answer.json"))
if not ARTIFACT_PATH.exists():
    ARTIFACT_PATH = DEFAULT_ARTIFACT


def load_answer() -> dict:
    if not ARTIFACT_PATH.exists():
        raise AssertionError(f"Missing answer artifact: {ARTIFACT_PATH}")
    return json.loads(ARTIFACT_PATH.read_text(encoding="utf-8"))


class RiskCalculationDrawdownTests(unittest.TestCase):
    def test_required_shape(self):
        answer = load_answer()
        required = {
            "task_id",
            "data_window",
            "metrics",
            "formula_notes",
            "assumptions",
            "evidence",
            "limitations",
            "not_investment_advice",
        }
        self.assertTrue(required.issubset(answer), sorted(required - set(answer)))
        self.assertEqual(answer["task_id"], "risk-calculation-drawdown")
        self.assertIs(answer["not_investment_advice"], True)

    def test_data_window_and_source(self):
        answer = load_answer()
        window = answer["data_window"]
        self.assertEqual(window["start_date"], "2025-01-02")
        self.assertEqual(window["end_date"], "2025-01-10")
        self.assertEqual(window["rows_used"], 7)
        self.assertEqual(window["source"], "synthetic_portfolio_values.csv")
        self.assertTrue(FIXTURE_PATH.exists())

    def test_risk_metrics_are_correct(self):
        metrics = load_answer()["metrics"]
        self.assertEqual(metrics["total_return_pct"], 1.0)
        self.assertEqual(metrics["max_drawdown_pct"], -8.65)
        self.assertEqual(metrics["peak_date"], "2025-01-03")
        self.assertEqual(metrics["trough_date"], "2025-01-09")
        self.assertEqual(metrics["daily_return_volatility_pct"], 4.56)
        self.assertEqual(metrics["annualized_volatility_pct"], 72.33)

    def test_formula_and_assumptions_are_auditable(self):
        answer = load_answer()
        notes = " ".join(answer["formula_notes"]).lower()
        assumptions = " ".join(answer["assumptions"]).lower()
        self.assertIn("value / running_peak - 1", notes)
        self.assertIn("sample standard deviation", notes)
        self.assertIn("sqrt(252)", notes)
        self.assertIn("252 trading days", assumptions)
        self.assertIn("no private portfolio", assumptions)

    def test_evidence_and_safety_boundary_are_visible(self):
        answer = load_answer()
        evidence = answer["evidence"]
        self.assertEqual(evidence["source"], "synthetic_portfolio_values.csv")
        self.assertEqual(evidence["source_id"], "synthetic_fixture")
        self.assertEqual(evidence["unit"], "percent")
        self.assertIs(evidence["all_rows_used"], True)
        self.assertIs(evidence["sample_volatility_used"], True)

        combined = json.dumps(answer, ensure_ascii=False).lower()
        limitations = " ".join(answer["limitations"]).lower()
        self.assertIn("synthetic", limitations)
        self.assertIn("not a production risk model", limitations)
        disallowed = [
            "buy recommendation",
            "sell recommendation",
            "guaranteed return",
            "price target",
            "trading signal generated",
            "production-ready",
        ]
        self.assertFalse(any(term in combined for term in disallowed))


if __name__ == "__main__":
    unittest.main()
