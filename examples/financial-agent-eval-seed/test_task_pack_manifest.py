import unittest

import validate_task_pack_manifest as manifest


class TaskPackManifestTests(unittest.TestCase):
    def test_manifest_matches_generated_shape(self):
        generated = manifest.build_manifest()
        checked = manifest.load_json(manifest.MANIFEST_PATH)
        self.assertEqual(
            [task["task_id"] for task in checked["tasks"]],
            [task["task_id"] for task in generated["tasks"]],
        )
        self.assertEqual(len(checked["tasks"]), 10)

    def test_manifest_validates(self):
        checked = manifest.load_json(manifest.MANIFEST_PATH)
        self.assertEqual(manifest.validate_manifest(checked), [])

    def test_manifest_declares_public_safety_boundary(self):
        checked = manifest.load_json(manifest.MANIFEST_PATH)
        boundary = checked["public_safety_boundary"].lower()
        self.assertIn("not contain private company data", boundary)
        self.assertIn("real user data", boundary)
        self.assertIn("investment advice", boundary)
        self.assertIn("not-official", checked["status"])


if __name__ == "__main__":
    unittest.main()
