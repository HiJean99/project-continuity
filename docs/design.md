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


## Review of related projects and resulting changes

Reviewed the public designs of:

- seriousz158/project-continuity: a single current-state authority, revision compare-and-swap, writer leases, immutable receipts, evidence-backed completion, and conservative Git-drift checks.
- jumpifequal/handoff-skill: preserve settled decisions, exact work-in-progress, explicit provenance, and one immediate next action; avoid lossy prose summaries.
- uchimata2/handoff-skill: reconcile linked durable records when a handoff is created or closed so status indexes and memory do not become stale.
- stefan-jansen/coding-agent-toolkit: keep workflow state on disk and avoid wrapping one agent runtime inside another merely to transfer context.

Adopted for this personal, Markdown-first project:

1. One Work Item remains the canonical record for each unfinished outcome; no second handoff document.
2. Add schema_version and advisory revision metadata. Revision helps detect stale edits but is not a lock or compare-and-swap guarantee.
3. Require one immediate next action, while allowing a separate short list of later steps.
4. Preserve exact in-progress artifacts at their source location and link to them; include verbatim excerpts only when necessary.
5. Require explicit provenance and labels for verified facts, observations, hypotheses, inferences, and accepted decisions.
6. Reconcile STATE.md and linked open-question/index entries when tasks change or close.
7. Re-read a Work Item immediately before editing and keep one active writer per item. Hand off ownership instead of concurrent writes.

Deliberately not adopted:

- A JSON block embedded in Markdown as a second authoritative representation.
- A daemon, SQLite database, writer lease service, content-addressed receipt store, or export bundle.
- Full Git fingerprinting on every update.
- Automatic hooks or agent launching.

Those mechanisms solve multi-process and multi-agent concurrency at the cost of substantially more implementation and maintenance. For personal use, sequential ownership plus Git history and explicit revision checks are the simpler trade-off. If real concurrent edits become common, revisit a transactional state store rather than pretending a Markdown revision field is a lock.


## v1.2: optional Orca execution adapter

Version 1.2 keeps the v1.1 Work Item schema and adds an optional Orca adapter. Project Continuity remains agent- and backend-neutral: the Work Item is the durable outcome; an Execution Record under `work/executions/` captures one bounded backend execution phase. One Work Item may link to multiple Execution Records / Orca Runs. Each Run contains Tasks; each Task may have multiple Dispatch attempts.

Authority is split: Project Continuity owns project intent, acceptance, Work Item lifecycle, and canonical memory. Orca owns live Run, Task, Dispatch, Worker, and liveness state. The Coordinator is the single writer of canonical continuity files. Worker completion is not Work Item acceptance. The Coordinator reconciles evidence and moves the Work Item to review; done requires verified or user-accepted acceptance criteria.

The integration is opt-in and additive. Non-Orca projects continue unchanged. No daemon, database, polling loop, provider-specific session parser, or automatic commit/push is introduced. See the Skill references `orca-integration.md` and `execution-record-format.md`.
