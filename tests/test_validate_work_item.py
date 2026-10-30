import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".agents/skills/project-continuity/scripts"))
from validate_work_item import validate  # noqa: E402

VALID = """---
id: W-20261030-example
title: Example task
status: ready
priority: normal
created: 2026-10-30
updated: 2026-10-30
created_by: AGY
assigned_to: Codex
next_agent: Codex
depends_on: []
source_session: ""
schema_version: "1.1"
revision: 1
---

# Example task

## Objective
Produce an outcome.

## Context
Why this matters.

## Findings and decisions
- Verified: a fact.

## Evidence and references
- source.md

## Completed
- [x] Analysis completed.

## Current state and workspace snapshot
- Branch: main

## Next action
Inspect the implementation.

## Acceptance criteria
- [ ] The implementation passes validation.

## Constraints, risks, and assumptions
- No production changes.

## Handoff log
- 2026-10-30: AGY to Codex.

## Validation log
- Not yet validated.
"""


class WorkItemValidationTests(unittest.TestCase):
    def validate_text(self, text):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "W-20261030-example.md"
            path.write_text(text, encoding="utf-8")
            return validate(path)

    def test_valid_item(self):
        self.assertEqual(self.validate_text(VALID), [])

    def test_rejects_missing_next_action(self):
        bad = VALID.replace("## Next action\nInspect the implementation.", "## Next action\n")
        self.assertTrue(any("Next action section is empty" in e for e in self.validate_text(bad)))

    def test_rejects_invalid_status(self):
        bad = VALID.replace("status: ready", "status: finished")
        self.assertTrue(any("invalid status" in e for e in self.validate_text(bad)))

    def test_rejects_old_schema(self):
        bad = VALID.replace('schema_version: "1.1"', 'schema_version: "1.0"')
        self.assertTrue(any("schema_version" in e for e in self.validate_text(bad)))

    def test_rejects_plural_next_actions(self):
        bad = VALID.replace("## Next action", "## Next actions")
        self.assertTrue(any("missing sections" in e or "use one" in e for e in self.validate_text(bad)))


if __name__ == "__main__":
    unittest.main()
