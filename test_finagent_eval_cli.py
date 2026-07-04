import unittest

import finagent_eval


class FinAgentEvalCliTests(unittest.TestCase):
    def test_parser_exposes_expected_commands(self):
        parser = finagent_eval.build_parser()
        help_text = parser.format_help()
        self.assertIn("demo", help_text)
        self.assertIn("bad-demo", help_text)
        self.assertIn("scorecard", help_text)

    def test_display_path_uses_repo_relative_paths(self):
        path = finagent_eval.SEED_DIR / "run_finance_eval.py"
        self.assertEqual(
            finagent_eval.display_path(path),
            "examples/financial-agent-eval-seed/run_finance_eval.py",
        )


if __name__ == "__main__":
    unittest.main()
