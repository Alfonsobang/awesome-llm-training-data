#!/usr/bin/env python3
"""Validate the compact JSONL task index."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TASK_INDEX = ROOT / "tasks.jsonl"
MANIFEST = ROOT / "harbor-template" / "task-pack-manifest.json"


class TaskIndexTests(unittest.TestCase):
    def test_task_index_matches_manifest(self) -> None:
        indexed_tasks = [
            json.loads(line)
            for line in TASK_INDEX.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        manifest_ids = {task["task_id"] for task in manifest["tasks"]}

        self.assertEqual(len(indexed_tasks), 10)
        self.assertEqual({task["task_id"] for task in indexed_tasks}, manifest_ids)
        for task in indexed_tasks:
            self.assertIn("family", task)
            self.assertIn("risk_level", task)
            self.assertIn("primary_failure_mode", task)
            self.assertTrue((ROOT / task["template_path"]).exists())
            self.assertTrue((ROOT / task["task_spec"]).exists())


if __name__ == "__main__":
    unittest.main()
