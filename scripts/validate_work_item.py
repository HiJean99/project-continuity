#!/usr/bin/env python3
"""Run the validator bundled with the installed/project-local Skill."""

from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / ".agents/skills/project-continuity/scripts/validate_work_item.py"
runpy.run_path(str(VALIDATOR), run_name="__main__")
