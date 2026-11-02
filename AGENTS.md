# Repository Guidance

This repository maintains a portable Agent Skill for project and work continuity.

- Keep the Skill vendor-neutral and role-neutral.
- Keep SKILL.md concise; put schemas and detailed procedures in references/.
- Treat Markdown Work Items as optional handoff artifacts, not a general task tracker or scheduler.
- Prefer existing project docs, ADRs, issue trackers, and orchestrator state; do not duplicate their records.
- Do not make Orca or any orchestrator a Project Continuity dependency. Project Continuity does not schedule or monitor Workers.
- Never instruct agents to save hidden chain-of-thought. Save conclusions, evidence, assumptions, decisions, progress, and next actions only.
- Preserve existing project documentation during adapt; never delete or rename user files as part of initialization.
- Do not add a daemon, database, MCP server, or provider-specific session parser unless a demonstrated requirement justifies it.
- Run scripts/validate.sh after changes.
