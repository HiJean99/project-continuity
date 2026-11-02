# Work Item and Handoff Format

## Purpose and limits

A Work Item is an optional durable handoff artifact for one meaningful unfinished outcome that must survive a session, agent, person, or tool boundary. It is not a general issue tracker, project backlog, scheduler, or replacement for an Orca Task or ticket.

Do not create a Work Item when an existing issue tracker, Orca Task, or authoritative project record already carries the required context. Do not create one for every coding task or Orca Task.

## File name and metadata

Use W-YYYYMMDD-short-slug.md. If a same-day ID already exists, add a numeric suffix.

~~~yaml
---
id: W-YYYYMMDD-short-slug
title: Short outcome-oriented title
status: proposed
priority: normal
created: YYYY-MM-DD
updated: YYYY-MM-DD
created_by: AGY
assigned_to: unassigned
next_agent: unassigned
depends_on: []
source_session: ""
schema_version: "1.1"
revision: 1
---
~~~

Metadata rules:

- status: proposed, ready, in_progress, blocked, review, done, or cancelled. It describes the durable handoff record, not live Worker state.
- priority: low, normal, high, or urgent.
- created_by, assigned_to, and next_agent are free-form labels.
- depends_on contains Work Item IDs and is informational only; it does not schedule work.
- source_session is optional. Never put credentials or private URLs in metadata.
- schema_version remains 1.1 for backward compatibility.
- revision starts at 1 and increments on each material update. It is advisory, not a distributed lock.

## Required sections

### Objective
State the observable durable outcome.

### Context
Explain why the work must survive the current context boundary.

### Findings and decisions
Distinguish verified facts, hypotheses, inferences, and accepted decisions.

### Evidence and references
Link to project-relative files, code symbols, experiment IDs, citations, URLs, and source conversations.

### Completed
List only work actually completed, with output paths and evidence.

### Current state and workspace snapshot
When relevant, record working directory, Git branch/commit, dirty paths (names only), artifacts, and last validation. This is a snapshot, not live truth.

### Next action
State exactly one immediate action the receiving context can execute.

### Remaining steps (optional)
A short ordered checklist may describe later work.

### Acceptance criteria
Use observable conditions for the durable handoff outcome.

### Constraints, risks, and assumptions
Record permissions, safety constraints, unresolved assumptions, and escalation points.

### Handoff log
Append date, from/to, reason, key context, and status when ownership changes.

### Validation log
Append material checks and results.

## Status lifecycle

The status describes the continuity record only:

- proposed: captured, but not authorized for execution;
- ready: approved and available to a receiving context;
- in_progress: a named owner has adopted the handoff;
- blocked: continuation needs an external input or decision;
- review: the durable handoff outcome awaits acceptance;
- done: its acceptance criteria are verified or explicitly accepted;
- cancelled: no longer needed.

These statuses do not replace or mirror Orca Run/Task/Worker statuses or issue-tracker workflows.

## Fidelity and provenance

- Preserve accepted decisions and their evidence.
- Mark inherited or unverified claims explicitly.
- Keep exact work products at their source paths; link them rather than copying large artifacts.
- Separate completed work from proposed work.
- Do not save hidden reasoning, secrets, or full chat transcripts.
- Keep one active writer and re-read immediately before edits.
