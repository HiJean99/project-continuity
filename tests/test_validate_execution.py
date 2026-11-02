import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".agents/skills/project-continuity/scripts"))
from validate_execution import validate  # noqa: E402

VALID = '''---
id: E-20261102-model-review
work_item_id: W-20261102-model-refactor
backend: orca
backend_version: "1.4.246"
run_id: run-123
objective: Review the model implementation
status: active
created: 2026-11-02
updated: 2026-11-02
schema_version: "1.2"
revision: 1
---

# Model review execution

## Objective
Review one bounded phase.

## Run
- Run ID: run-123

## Task map
### Task: inspect
- Task ID: task-1

## Evidence and outputs
- None yet.

## Blockers and decisions
- None.

## Reconciliation
- Not yet reconciled.

## Next action
Check the worker receipt.

## History
- 2026-11-02 — planned.
'''


class ExecutionValidationTests(unittest.TestCase):
    def validate_text(self, text):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "E-20261102-model-review.md"
            path.write_text(text, encoding="utf-8")
            return validate(path)

    def test_valid_record(self):
        self.assertEqual(self.validate_text(VALID), [])

    def test_requires_run_id_after_planned(self):
        bad = VALID.replace("run_id: run-123", 'run_id: ""')
        self.assertTrue(any("run_id is required" in error for error in self.validate_text(bad)))

    def test_rejects_wrong_schema(self):
        bad = VALID.replace('schema_version: "1.2"', 'schema_version: "1.1"')
        self.assertTrue(any("schema_version" in error for error in self.validate_text(bad)))

    def test_requires_immediate_next_action(self):
        bad = VALID.replace("## Next action\nCheck the worker receipt.", "## Next action\n")
        self.assertTrue(any("Next action section is empty" in error for error in self.validate_text(bad)))

    def test_completed_can_omit_run_id_only_if_planned_no(self):
        bad = VALID.replace("status: active", "status: completed").replace("run_id: run-123", 'run_id: ""')
        self.assertTrue(any("run_id is required" in error for error in self.validate_text(bad)))


if __name__ == "__main__":
    unittest.main()
