# Design Notes

## Current purpose (v1.3)

Project Continuity is an optional, lightweight context-preservation protocol. It exists for durable information that must survive meaningful session, agent, person, tool, or repository boundaries when the project's existing sources of truth do not already preserve it.

It is not a project-management application, issue tracker, task scheduler, agent runtime, or orchestration framework. It must not duplicate the responsibilities of project documentation, ADRs, issue trackers, Git, or an orchestrator.

## Source-of-truth boundaries

- Source code, configuration, and tests describe implementation reality.
- README.md and AGENTS.md describe project purpose, setup, conventions, and agent instructions.
- Architecture documents, ADRs, experiment logs, and domain-specific records preserve technical and research knowledge.
- Issue trackers own ordinary backlog items and ticket workflows.
- Orca or another orchestrator owns live Runs, Tasks, dependencies, Dispatches, Workers, messages, Worktrees, and execution state.
- Git owns source history, branches, commits, and merges.
- Project Continuity stores only durable cross-context information that has no suitable authoritative home in the systems above.

If existing systems already cover the need, Project Continuity should make no changes.

## When it is useful

Use it for long-running research/engineering programmes, cross-repository efforts without a shared tracker, provider/tool transitions, or handoffs where a receiving context cannot reliably reconstruct the unfinished work from existing records.

Do not use it for routine one-session coding, ordinary tickets, or multi-agent execution already managed by Orca. Do not create one Work Item per Orca Task. Do not create per-Run Execution Records in v1.3.

## Minimal data model

Project-level records are optional, not a mandatory four-file bundle:

- PROJECT.md only when stable project context is not already documented.
- STATE.md only when a cross-session snapshot is useful and no roadmap/status source serves that role.
- DECISIONS.md only when no ADR or decision log exists.
- OPEN_QUESTIONS.md only when no issue/research tracker is the appropriate home.

A Work Item remains schema 1.1 for compatibility, but is an optional durable handoff artifact. It is not a general backlog item, scheduler unit, or live execution status record. `depends_on` is informational only. The status lifecycle describes the continuity record, not an Orca Worker or issue status.

## Relationship with native agent capabilities

Provider-local session resume and learning features remain useful within their own runtimes. Project Continuity is only the portable bridge when work must cross those boundaries and the existing repository/issue/orchestrator records are insufficient. It must not replace reusable agent rules, native issue trackers, or orchestration systems.

## Deliberate non-goals

The project does not implement:

- Agent process launching, model selection, or provider-session switching;
- task scheduling, DAG execution, Worker supervision, or message routing;
- Git branch, Worktree, merge, or release management;
- full conversation transcript import or hidden-reasoning transfer;
- a daemon, SQLite database, MCP server, or web UI;
- automatic commits, pushes, or repository mutations.

## Version history

### v1.1

Established the agent-neutral Skill, project context files, Work Item schema 1.1, handoff/resume procedures, evidence/provenance discipline, and validators.

### v1.2 (historical)

Added an optional Orca integration and per-Run Execution Records. This proved useful for exploring the relationship between durable context and live orchestration, but it introduced unnecessary coupling and duplicated some execution concepts. The v1.2 references, template, and validator remain for existing records only.

### v1.3 (current)

Architectural simplification: Orca is fully independent. Project Continuity does not configure, invoke, schedule, supervise, or mirror it. Ordinary software projects should generally use README/AGENTS/ADRs, Git, issue trackers, and Orca directly. Project Continuity is opt-in and adds only missing durable context. Existing v1.1 Work Items and v1.2 Execution Records remain readable; no automatic migration or deletion occurs.

## References

- Antumi: https://github.com/flyhero/antumi
- Antumi architecture: https://github.com/flyhero/antumi/blob/main/docs/ARCHITECTURE.md
- Agent Skills specification: https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx
- Codex Skills: https://learn.chatgpt.com/docs/build-skills
- Antigravity CLI Skills: https://antigravity.google/docs/skills
- Antigravity CLI rules: https://antigravity.google/docs/rules
