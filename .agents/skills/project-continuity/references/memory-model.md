# Project Memory Model

## Purpose

Project memory is optional. It preserves durable context that would otherwise be lost across meaningful context boundaries. It is not a transcript archive, project-management database, task tracker, or mirror of an orchestrator.

## Source-of-truth priority

Prefer existing authoritative sources in this order:

1. Source code, configuration, tests, and reproducible outputs for implementation facts.
2. README.md and AGENTS.md for project purpose, setup, conventions, and agent instructions.
3. Existing architecture docs, ADRs, design docs, experiment logs, lab notebooks, and domain-specific records.
4. Existing issue trackers or orchestration systems for active tasks and execution state.
5. Project Continuity files only for durable context not already represented above.

Do not create duplicate sources of truth.

## Optional records

Create only what the project actually needs.

### PROJECT.md — stable context

Use only if the project purpose, scope, constraints, terminology, and authoritative locations are not already documented. Do not duplicate the README or architecture document.

### STATE.md — cross-session snapshot

Use only when a concise snapshot is useful across sessions and no existing status/roadmap/research source serves the same role. Keep it short: verified phase, durable milestones, blockers, and next milestone. Never mirror live Orca or issue-tracker state.

### DECISIONS.md — decision history

Use only if the project lacks an ADR or other decision record. Append material accepted/rejected/superseding decisions with context, rationale, consequences, and evidence. Do not create a second decision log.

### OPEN_QUESTIONS.md — unresolved questions

Use only if questions need a durable home and are not already issues, research questions, or entries in an authoritative tracker. A question is not automatically a task.

## Work Items are optional handoff artifacts

A Work Item preserves one unfinished outcome only when a receiving context cannot rely on existing project records, issue trackers, or orchestrator Tasks. It is not a general backlog item or scheduler. `depends_on` is informational. Do not duplicate Orca Tasks or issue-tracker tickets.

A Work Item may span sessions or tools, but should not mirror the live execution state of Orca. Keep project memory concise and link to the Work Item only when useful.

## Orca and other orchestrators

Orchestrators own live execution state: Runs, Tasks, dependencies, Dispatches, Workers, messages, workspaces, and liveness. Project Continuity does not create per-Run Execution Records in v1.3. Existing v1.2 Execution Records remain historical artifacts and can still be validated by the legacy validator.

Record only durable conclusions, accepted decisions, and artifacts that remain useful after the orchestrator Run has ended. Use the orchestrator directly for current task/Worker status.

## Evidence discipline

Use explicit labels where ambiguity matters:

- **Verified**: directly supported by a file, command result, reproducible experiment, or reliable source.
- **Observed**: seen in a particular run or environment, not necessarily universal.
- **Hypothesis**: plausible but unverified.
- **Inference**: reasoned from evidence; not directly observed.
- **Decision**: an accepted choice, with an owner and date where relevant.

Record provenance: relative file path, Git commit, experiment ID, citation, URL, page/section, or command used. Avoid unsupported claims such as "tested" when no test was run.
