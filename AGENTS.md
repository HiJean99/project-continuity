# Repository Guidance

This repository maintains a portable Agent Skill for project and work continuity.

- Keep the Skill vendor-neutral and role-neutral.
- Keep SKILL.md concise; put schemas and detailed procedures in references/.
- Treat Markdown work items as the durable source of truth for handoffs.
- Never instruct agents to save hidden chain-of-thought. Save conclusions, evidence, assumptions, decisions, progress, and next actions only.
- Preserve existing project documentation during adapt; never delete or rename user files as part of initialization.
- Do not add a daemon, database, MCP server, or provider-specific session parser unless a demonstrated requirement justifies it.
- Run scripts/validate.sh after changes.
