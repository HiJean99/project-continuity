# Design Notes

## Problem statement

AGY and Codex maintain separate provider conversations. A conversation can contain useful analysis, decisions, code references, and unfinished work, but another agent cannot reliably continue from a chat transcript alone.

The system must preserve the work state in a portable form so any agent or person can resume it.

## Lessons adopted from Antumi

Design reference: the public flyhero/antumi README and docs/ARCHITECTURE.md.

1. **Separate conversations from tasks.** A conversation is an interaction history; a task is a durable unit of work with a lifecycle.
2. **Use explicit task states.** Antumi distinguishes pending, running, review, and done, and treats rework as an explicit transition.
3. **Handoff visible context, not model internals.** Antumi records visible user messages, final assistant replies, and an extra handoff note. Hidden reasoning and provider-specific capabilities cannot be transferred.
4. **Verify the workspace after handoff.** The receiving agent is instructed to inspect the current directory, Git state, and tests.
5. **Keep durable tasks separate from an agent's turn checklist.** Antumi stores user-facing todos outside provider conversation state. This project does not reproduce the full todo subsystem in v1; only meaningful multi-step work becomes a Work Item.
6. **Persist independently of the UI or agent process.** Antumi uses a core store and daemon. This project keeps the same separation of concerns but uses Markdown and Git rather than a database and background process.

## Deliberate simplifications

This project is a portable Skill and file protocol, not a task-management application.

It does not implement:

- Agent process launching or provider-session switching;
- full conversation transcript import;
- hidden-reasoning transfer;
- background daemon, SQLite, or web UI;
- automatic DAG scheduling;
- Git worktree management;
- a global todo dashboard.

A Work Item is the single source of truth for an unfinished outcome. It combines the durable task record and handoff package. Project memory remains separate and concise. To preserve an analysis-only AGY workflow, the only permitted write for a handoff is the single Work Item file; source code and other project memory remain read-only. If the CLI is in a hard read-only mode, the agent must ask for approval to write that file or return the artifact without claiming it is persisted. This is an instruction-level boundary, not an OS-enforced ACL; use per-operation approval/strict permission settings and approve only the Work Item write when stronger enforcement is required.

## Complement to native session learning

Antigravity CLI's /learn turns reusable corrections and procedures into rules or Skills after user approval. That is useful for durable operating knowledge, but it is not a task handoff: it does not by itself preserve an unfinished outcome, acceptance criteria, workspace snapshot, and next owner. Project Continuity handles that work state; it should not replace /learn for reusable agent lessons.

Codex and Antigravity CLI can resume their own provider conversations, but a provider-local resume does not transfer the task to the other provider. The Work Item is the portable cross-agent bridge.

## Shared Skill compatibility

The Skill follows the open Agent Skills directory format:

- Project scope shared by Codex and Antigravity CLI: .agents/skills/<skill-name>/.
- Codex CLI profile scope: $CODEX_HOME/skills/<skill-name>/ (default ~/.codex/skills/). Project scope: .agents/skills/<skill-name>/.
- Antigravity CLI user scope: ~/.gemini/antigravity-cli/skills/<skill-name>/.

Codex and Antigravity CLI have different global paths, so the optional installer copies the same canonical Skill to both. Other compatible clients can use the project-local .agents/skills/ copy or their documented global Skill directory.

Antigravity CLI reads workspace AGENTS.md and GEMINI.md; Codex reads AGENTS.md. The project initializer therefore uses a concise AGENTS.md pointer and preserves existing rules. The Skill itself does not require a particular project type, repository host, username, machine path, or fixed agent-role split.

## References

- Antumi: https://github.com/flyhero/antumi
- Antumi architecture: https://github.com/flyhero/antumi/blob/main/docs/ARCHITECTURE.md
- Agent Skills specification: https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx
- Codex Skills: https://learn.chatgpt.com/docs/build-skills
- Antigravity CLI Skills: https://antigravity.google/docs/skills
- Antigravity CLI rules: https://antigravity.google/docs/rules
