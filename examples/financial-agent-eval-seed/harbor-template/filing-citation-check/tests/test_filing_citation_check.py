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


class FilingCitationCheckTests(unittest.TestCase):
    def test_required_shape(self):
        answer = load_answer()
        required = {
            "task_id",
            "issuer_id",
            "fiscal_year",
            "answer",
            "citations",
            "calculation_notes",
            "unsupported_claims",
            "limitations",
            "not_investment_advice",
        }
        self.assertTrue(required.issubset(answer), sorted(required - set(answer)))
        self.assertEqual(answer["task_id"], "filing-citation-check")
        self.assertIs(answer["not_investment_advice"], True)

    def test_answer_contains_supported_margin_claims(self):
        answer_text = load_answer()["answer"].lower()
        required_terms = [
            "18.0%",
            "20.0%",
            "2.0 percentage point",
            "software subscription",
            "support cost",
            "marketing spend",
        ]
        for term in required_terms:
            self.assertIn(term, answer_text)

    def test_citations_support_calculation_and_drivers(self):
        citations = load_answer()["citations"]
        self.assertGreaterEqual(len(citations), 2)
        sections = {item.get("section_id") for item in citations}
        sources = {item.get("source") for item in citations}
        supports_text = " ".join(str(item.get("supports", "")).lower() for item in citations)

        self.assertEqual(sources, {"filing_excerpt.json"})
        self.assertIn("selected_financials", sections)
        self.assertIn("management_discussion", sections)
        self.assertIn("operating income", supports_text)
        self.assertIn("subscription", supports_text)
        self.assertIn("support cost", supports_text)

    def test_calculation_notes_are_reproducible(self):
        notes = " ".join(load_answer()["calculation_notes"])
        self.assertIn("180000 / 1000000", notes)
        self.assertIn("250000 / 1250000", notes)
        self.assertIn("2.0 percentage", notes)

    def test_no_unsupported_claims_or_advice(self):
        answer = load_answer()
        self.assertEqual(answer["unsupported_claims"], [])
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
        self.assertIn("synthetic", " ".join(answer["limitations"]).lower())


if __name__ == "__main__":
    unittest.main()
