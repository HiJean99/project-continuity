---
name: project-continuity
description: Preserve durable project context and handoffs when work spans sessions, agents, tools, repositories, or long-running research. Use when asked to initialize/adapt continuity, record durable decisions, hand off or resume unfinished cross-context work, or recover project context. Do not use for routine coding tasks, ordinary issue tracking, or multi-agent orchestration; use existing project documentation and native tools such as Orca instead.
---

# Project Continuity

Project Continuity is an **optional, lightweight context-preservation layer**. It is not a project manager, issue tracker, task scheduler, agent runtime, or orchestration engine. Do not add it to every repository by default.

Its purpose is to preserve only information that would otherwise be lost across meaningful context boundaries: stable project context, accepted decisions, verified state, unresolved questions, and handoff information that existing project systems do not already store.

## First decide whether Project Continuity is needed

Before creating or updating continuity files, inspect the project and its existing sources of truth.

Usually **do not use Project Continuity** when:

- this is an ordinary software repository with a useful README and AGENTS.md;
- the work is already represented in GitHub Issues, Jira, Linear, or another task tracker;
- an orchestrator such as Orca already owns the active Run, Tasks, dependencies, Worker messages, and execution state;
- the task is self-contained and can be completed in the current session;
- existing architecture docs, ADRs, experiment logs, or project notes already preserve the required context.

Consider Project Continuity when:

- a long-running research or engineering effort spans many sessions and agents;
- important decisions and evidence need to survive provider/tool changes;
- work crosses multiple repositories or systems with no single existing source of truth;
- a handoff must preserve exact unfinished work for a different agent, person, or later session;
- the project needs a durable context layer beyond the lifetime of an individual orchestrator Run.

If existing documentation and tools already cover the need, say so and make no changes. Do not create files merely to satisfy a template.

Read [references/when-to-use.md](references/when-to-use.md) when the fit is unclear.

## Boundaries

- **Project documentation** owns architecture, setup, stable conventions, and domain knowledge.
- **Issue trackers / native project tools** own ordinary backlog items and tickets.
- **Orca or another orchestrator** owns live Runs, Tasks, dependencies, Dispatches, Workers, messages, Worktrees, and execution state.
- **Git** owns source history, branches, commits, and merges.
- **Project Continuity** preserves durable cross-context knowledge only where the above sources are insufficient.

Never mirror an orchestrator's live task state into Work Items or Markdown execution logs. Never create a Project Continuity Work Item for every Orca Task. Do not create per-Run Execution Records in v1.3. Existing v1.2 Execution Records remain readable as legacy records; see [references/legacy-v1.2-orca-integration.md](references/legacy-v1.2-orca-integration.md).

## Select an operation

- `init`: establish a minimal continuity layer only after confirming it is needed.
- `adapt`: inspect an existing project and make the smallest useful additions; a no-op is a valid result.
- `handoff`: preserve unfinished work only when the receiving context cannot rely on an existing issue, orchestrator Task, or authoritative project record.
- `resume`: verify the workspace and continue an existing continuity handoff.
- `update`: consolidate durable project knowledge or decisions; do not record routine execution chatter.
- `status`: summarize continuity records only. Do not pretend to report live Orca or issue-tracker status unless those systems are actually queried.

If the user asks for ordinary coding, refactoring, testing, or multi-agent execution, do the work using the repository's existing instructions and native tools. Do not invoke Project Continuity just because a task is multi-step.

## General rules

1. Inspect the project root, Git state, existing docs, instruction files, and connected task/orchestration systems before writing.
2. Reuse existing authoritative sources. Do not create duplicate README, architecture, roadmap, ADR, issue list, experiment log, or execution dashboard.
3. Prefer updating the authoritative document over creating a Project Continuity record.
4. Keep durable context concise, factual, and evidence-backed. Separate verified facts, observations, hypotheses, inferences, and accepted decisions.
5. Never save hidden chain-of-thought, full chat transcripts, secrets, tokens, passwords, private keys, raw environment files, or sensitive personal data.
6. Preserve user work. Do not overwrite dirty changes or automatically commit, push, delete, rename, or move existing files.
7. Do not claim completion based only on an agent report; verify the relevant artifact and acceptance evidence.

## Project context

Project-level continuity files are **optional**, not a mandatory four-file bundle.

- `PROJECT.md`: create only if stable project purpose, scope, constraints, terminology, and authoritative locations are not already documented.
- `STATE.md`: create only if a concise cross-session snapshot is genuinely useful and no existing roadmap/status source serves that role. Never mirror live Orca status here.
- `DECISIONS.md`: create only if the project lacks an ADR or other decision record. Append material decisions; do not duplicate an existing ADR system.
- `OPEN_QUESTIONS.md`: create only if unresolved questions need a durable home and are not already managed by an issue tracker or research log.

For init/adapt, read [references/operations.md](references/operations.md) and [references/memory-model.md](references/memory-model.md). Use templates only for files that are actually needed.

## Work Items and handoff

A Work Item is an **optional durable handoff note**, not a general-purpose ticket, backlog item, scheduler, or replacement for Orca Task / GitHub Issue / Jira / Linear.

Create one only when all are true:

- the outcome must survive a meaningful session, agent, person, or tool boundary;
- the next owner cannot reliably continue from the existing issue, orchestrator Task, or authoritative project documentation;
- the handoff needs a durable snapshot of context, evidence, completed work, constraints, and one immediate next action.

If Orca already tracks the active work as a Task, use Orca's Task and messaging mechanisms for execution handoff. Do not create a duplicate Work Item. If a broader research or project outcome spans multiple Runs and needs durable context beyond Orca, a Work Item may capture that broader outcome, but it must not mirror the Run's Tasks or Dispatches.

For handoff/resume, read [references/operations.md](references/operations.md) and [references/work-item-format.md](references/work-item-format.md). New Work Items retain schema version 1.1 for compatibility and must pass `scripts/validate_work_item.py`.

Store Work Items in `work/items/` only when needed. Reuse an existing matching open item rather than creating duplicates. `depends_on` is informational and does not schedule work. Work Item status describes the durable handoff record, not live Worker state.

A handoff must be executable without reconstructing the conversation. Preserve exact work products at their authoritative locations; link to them or include only the exact excerpt needed. Include objective, context, findings, evidence/provenance, completed work, workspace snapshot where relevant, constraints, acceptance criteria, and exactly one immediate Next action. Do not duplicate large artifacts or transcripts.

For resume, verify actual files, Git state, dependencies, and validation evidence. Actual state outranks stale notes. Re-read a Work Item immediately before editing, keep one active writer, and preserve newer changes.

## Updating durable knowledge

- Update the existing authoritative documentation first.
- Keep project summaries short; link to detailed source records.
- Append accepted/rejected/superseding decisions to the existing decision log or ADR system.
- Do not turn `STATE.md` into a diary or an Orca dashboard.
- Do not copy Orca Run/Task/Dispatch/Worker status into Project Continuity. Record only durable conclusions that remain useful after the execution system is gone.
- Do not create an Execution Record for a normal Orca Run in v1.3.

Read [references/operations.md](references/operations.md) for operation procedures.

## Safety and completion

- Ask before expanding scope or making consequential changes not already authorized.
- If the project already has sufficient continuity, report that and stop without creating files.
- If a handoff cannot be safely persisted, return the complete artifact without claiming it was saved.
- Mark a Work Item done only when its durable handoff outcome is verified or explicitly accepted; this is separate from any orchestrator Task status.
