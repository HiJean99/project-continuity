import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents/skills/project-continuity"


class V13PolicyTests(unittest.TestCase):
    def test_version_is_1_3_0(self):
        self.assertEqual((SKILL / "VERSION").read_text(encoding="utf-8").strip(), "1.3.0")

    def test_skill_explicitly_excludes_orchestration(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Do not use for routine coding tasks", text)
        self.assertIn("not a project manager, issue tracker, task scheduler, agent runtime, or orchestration engine", text)
        self.assertIn("Do not create per-Run Execution Records in v1.3", text)

    def test_decision_guide_treats_orca_as_independent(self):
        text = (SKILL / "references/when-to-use.md").read_text(encoding="utf-8")
        self.assertIn("Orca is an independent orchestration system", text)
        self.assertIn("Do not mirror Orca Tasks in Work Items", text)

    def test_v12_execution_format_is_marked_legacy(self):
        text = (SKILL / "references/legacy-v1.2-execution-record-format.md").read_text(encoding="utf-8")
        self.assertIn("deprecated in v1.3", text)
        template = (SKILL / "templates/LEGACY_V1.2_EXECUTION_RECORD.md").read_text(encoding="utf-8")
        self.assertIn("Do not create new records", template)


if __name__ == "__main__":
    unittest.main()
