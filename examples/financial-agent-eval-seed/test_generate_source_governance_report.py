import unittest

import generate_source_governance_report as report


class SourceGovernanceReportTests(unittest.TestCase):
    def test_report_counts_current_sources_tasks_and_mappings(self):
        data = report.build_report()
        self.assertEqual(data["sources_total"], 6)
        self.assertEqual(data["tasks_total"], 6)
        self.assertGreaterEqual(data["task_source_mappings_total"], 6)
        self.assertEqual(data["packaging_policy_counts"]["reference_only"], 3)
        self.assertEqual(data["packaging_policy_counts"]["do_not_package_without_review"], 2)
        self.assertEqual(data["packaging_policy_counts"]["bundled_synthetic_only"], 1)

    def test_report_includes_governance_boundary(self):
        data = report.build_report()
        self.assertIn("redistribution rights", data["policy_notes"].lower())
        self.assertIn("synthetic fixtures", data["safety_boundary"].lower())
        self.assertIn("reference-only", data["safety_boundary"].lower())

    def test_task_mappings_include_citation_task(self):
        data = report.build_report()
        task_ids = {item["task_id"] for item in data["task_source_mappings"]}
        self.assertIn("filing-citation-check", task_ids)


if __name__ == "__main__":
    unittest.main()
