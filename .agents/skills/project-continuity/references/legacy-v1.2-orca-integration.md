# Legacy: Project Continuity v1.2 Orca Integration

**Status: deprecated in v1.3. Retained for historical reference only.**

Version 1.2 introduced an optional Orca Execution Record and described a workflow linking Work Items to Orca Runs. The v1.3 design supersedes that approach.

In v1.3, Orca is an independent orchestration system. It owns live Runs, Tasks, dependencies, Dispatches, Workers, messages, Worktrees, and execution state. Project Continuity does not configure, invoke, schedule, supervise, or mirror Orca.

Do not create new Orca Execution Records. Do not duplicate Orca Tasks as Work Items. Use Orca's installed, version-matched orchestration Skill and native state for live execution. Update project documentation only with durable conclusions or decisions that remain useful after the Run ends.

The remainder of this file is retained to explain the v1.2 format and must not be treated as the current v1.3 procedure.

---

# v1.2 historical procedure

Project Continuity v1.2 treated Orca as an optional execution backend. It separated durable Work Items from live Orca Runs, Tasks, Dispatches, and Workers, and stored bounded Run summaries in `work/executions/`.

Historical references:

- `legacy-v1.2-execution-record-format.md`
- `templates/LEGACY_V1.2_EXECUTION_RECORD.md`
- `scripts/validate_execution.py`

Existing v1.2 Execution Records may be kept and validated. They are archival artifacts, not live status dashboards.
