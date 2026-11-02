# Migrating from Project Continuity v1.2 to v1.3

Version 1.3 is a usage and architecture simplification. It does not require a destructive data migration.

## What changes

- Project Continuity is optional; do not add it to every repository.
- Orca is an independent orchestration system, not a Project Continuity backend.
- Orca owns live Runs, Tasks, dependencies, Dispatches, Workers, messages, Worktrees, and execution status.
- Do not create new per-Run Execution Records or duplicate Orca Tasks as Work Items.
- Work Items remain schema 1.1 but are limited to durable handoffs across contexts when existing sources are insufficient.
- Project-level memory files are optional; create only the missing record.

## What stays compatible

- Existing v1.1 Work Items remain valid and need no schema migration.
- Existing v1.2 Execution Records may remain in the repository as historical artifacts.
- `scripts/validate_execution.py` remains available to validate historical v1.2 records.
- Existing project files are not deleted, renamed, or rewritten automatically.

## Recommended transition

1. Update the Skill to v1.3 using the repository installer.
2. Review existing `work/items/` records. Keep meaningful cross-session handoffs; do not convert or delete them merely because of the version change.
3. Review existing `work/executions/` records. Treat them as historical snapshots, not live Orca status. Stop creating new ones.
4. For ordinary software projects, use README/AGENTS/architecture docs, ADRs, issue trackers, Git, and Orca directly.
5. If an existing `AGENTS.md` tells agents to create Work Items for every task or mirror Orca, update that local instruction manually after reviewing it.
6. Keep only the continuity files that preserve information not already stored in authoritative project sources.

No automatic migration script is provided because the correct minimal structure depends on each project's existing documentation and tools.
