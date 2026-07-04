import tempfile
import unittest
from pathlib import Path

import build_scorecard


class BuildScorecardTests(unittest.TestCase):
    def test_reference_report_gets_full_dimension_score(self):
        report = build_scorecard.load_report(build_scorecard.ROOT / "results" / "example-report.json")
        scorecard = build_scorecard.build_scorecard(report, "reference")
        self.assertEqual(scorecard["total_score"], scorecard["max_score"])
        self.assertEqual(scorecard["red_flags"], [])
        self.assertIn("not production evidence", scorecard["recommendation"])

    def test_known_bad_report_has_red_flags(self):
        report = build_scorecard.load_report(build_scorecard.ROOT / "results" / "bad-finance-agent-report.json")
        scorecard = build_scorecard.build_scorecard(report, "known-bad")
        self.assertLess(scorecard["total_score"], scorecard["max_score"])
        self.assertTrue(scorecard["red_flags"])
        self.assertIn("fail review", scorecard["recommendation"])

    def test_markdown_output_is_not_a_leaderboard(self):
        report = build_scorecard.load_report(build_scorecard.ROOT / "results" / "example-report.json")
        scorecard = build_scorecard.build_scorecard(report, "reference")
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "scorecard.md"
            build_scorecard.write_markdown(scorecard, output)
            text = output.read_text(encoding="utf-8")
        self.assertIn("not a leaderboard", text)
        self.assertIn("Source selection", text)


if __name__ == "__main__":
    unittest.main()
