#!/usr/bin/env python3
"""Tests for candidate artifact scaffolding."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import finagent_eval


class InitCandidateTests(unittest.TestCase):
    def test_init_candidate_creates_task_skeletons(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp) / "candidate"
            args = type("Args", (), {"output_dir": output_dir, "force": False})()

            result = finagent_eval.command_init_candidate(args)

            self.assertEqual(result, 0)
            answer_paths = sorted(output_dir.glob("*/answer.json"))
            self.assertEqual(len(answer_paths), 10)
            first = json.loads(answer_paths[0].read_text(encoding="utf-8"))
            self.assertIn("task_id", first)
            self.assertEqual(first["status"], "todo")
            self.assertTrue(first["not_investment_advice"])
            self.assertIn("instruction", first)


if __name__ == "__main__":
    unittest.main()
