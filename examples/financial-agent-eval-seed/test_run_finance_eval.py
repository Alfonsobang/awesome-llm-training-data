import tempfile
import unittest
from pathlib import Path

import run_finance_eval


class FinanceEvalRunnerTests(unittest.TestCase):
    def test_discovers_current_task_templates(self):
        task_ids = {path.name for path in run_finance_eval.discover_task_dirs()}
        self.assertEqual(
            task_ids,
            {
                "compliance-refusal",
                "exact-data-lookup",
                "filing-margin-explanation",
                "toy-backtest-moving-average",
            },
        )

    def test_default_reference_artifacts_exist(self):
        for task_dir in run_finance_eval.discover_task_dirs():
            artifact = run_finance_eval.resolve_artifact(task_dir, artifact_root=None)
            self.assertTrue(artifact.exists(), artifact)

    def test_missing_candidate_artifact_fails(self):
        task_dir = next(iter(run_finance_eval.discover_task_dirs()))
        with tempfile.TemporaryDirectory() as tmp:
            artifact = run_finance_eval.resolve_artifact(task_dir, artifact_root=Path(tmp))
            result = run_finance_eval.run_task(task_dir, artifact)
        self.assertFalse(result.passed)
        self.assertIn("Missing candidate artifact", result.stderr)


if __name__ == "__main__":
    unittest.main()
