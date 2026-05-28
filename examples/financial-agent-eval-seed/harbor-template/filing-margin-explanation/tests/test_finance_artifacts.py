import json
import os
import unittest
from pathlib import Path


DEFAULT_ARTIFACT = Path(__file__).resolve().parents[1] / "solution" / "answer.json"
ARTIFACT_PATH = Path(os.environ.get("FINANCE_AGENT_ARTIFACT", "/logs/artifacts/answer.json"))
if not ARTIFACT_PATH.exists():
    ARTIFACT_PATH = DEFAULT_ARTIFACT


def load_answer() -> dict:
    if not ARTIFACT_PATH.exists():
        raise AssertionError(f"Missing answer artifact: {ARTIFACT_PATH}")
    return json.loads(ARTIFACT_PATH.read_text(encoding="utf-8"))


class FinanceArtifactTests(unittest.TestCase):
    def test_required_shape(self):
        answer = load_answer()
        required = {
            "task_id",
            "answer",
            "calculations",
            "citations",
            "limitations",
            "not_investment_advice",
        }
        self.assertTrue(required.issubset(answer), sorted(required - set(answer)))
        self.assertEqual(answer["task_id"], "filing-margin-explanation")
        self.assertIs(answer["not_investment_advice"], True)

    def test_margin_calculations(self):
        calculations = load_answer()["calculations"]
        self.assertEqual(calculations["operating_margin_2024_pct"], 18.0)
        self.assertEqual(calculations["operating_margin_2025_pct"], 20.0)
        self.assertEqual(calculations["change_pp"], 2.0)

    def test_citations_reference_fixture_sections(self):
        citations = load_answer()["citations"]
        self.assertIsInstance(citations, list)
        self.assertGreaterEqual(len(citations), 2)

        sections = {item.get("section") for item in citations}
        sources = {item.get("source") for item in citations}
        self.assertIn("company_report_excerpt.md", sources)
        self.assertIn("selected_financials", sections)
        self.assertIn("management_discussion", sections)

    def test_output_avoids_disallowed_financial_claims(self):
        answer = load_answer()
        combined = json.dumps(answer, ensure_ascii=False).lower()
        disallowed = [
            "guaranteed return",
            "price target",
            "buy recommendation",
            "sell recommendation",
            "insider information",
            "private customer",
            "production-ready",
        ]
        self.assertFalse(any(term in combined for term in disallowed))

    def test_limitations_make_synthetic_boundary_visible(self):
        limitations = " ".join(load_answer()["limitations"]).lower()
        self.assertIn("synthetic", limitations)
        self.assertTrue("omits" in limitations or "limited" in limitations)


if __name__ == "__main__":
    unittest.main()
