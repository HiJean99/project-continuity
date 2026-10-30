# Work Item and Handoff Format

## One record, two purposes

Each meaningful unfinished outcome has one Work Item file under work/items/. That file is both:

- the persistent task record; and
- the portable handoff package for another agent, person, or future session.

Do not create a separate HANDOFF file containing the same information. Add a new handoff-log entry to the existing Work Item when ownership changes.

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
---
~~~

Metadata rules:

- status: proposed, ready, in_progress, blocked, review, done, or cancelled.
- priority: low, normal, high, or urgent.
- created_by, assigned_to, and next_agent are free-form labels. They may be a person, agent name, role, or team.
- depends_on contains Work Item IDs. It is informational; this Skill is not a scheduler.
- source_session is optional. Never put credentials or private URLs in metadata.

## Required sections

### Objective

State the observable outcome, not just the topic.

### Context

Explain why the work exists and include only the background the next agent needs.

### Findings and decisions

List established conclusions and distinguish verified facts, hypotheses, inferences, and accepted decisions.

### Evidence and references

Link to project-relative files, relevant code symbols, experiment IDs, citations, URLs, and source conversations. Include enough provenance to verify important claims.

### Completed

List work that has actually been done, including output paths and validation evidence. Do not claim work based only on intention.

### Current state and workspace snapshot

When relevant, record:

- working directory / project;
- Git branch and commit;
- dirty paths (names only; do not dump secrets);
- important generated artifacts;
- tests or checks last run, with outcome and date;
- any environment assumptions.

This is a snapshot, not an authority over the current filesystem.

### Next actions

Write ordered, concrete actions. Prefer verbs and name the relevant files, commands, or outputs. A next agent should be able to start at item 1 without reconstructing the conversation.

### Acceptance criteria

Use observable conditions. "Looks good" is insufficient unless the user explicitly defines it that way.

### Constraints, risks, and assumptions

Record permissions, safety constraints, unresolved assumptions, known failure modes, and decisions that must be escalated to the user.

### Handoff log

Append a compact entry whenever the work changes hands or is paused for another agent/session:

- date;
- from / to;
- reason;
- what changed in the handoff;
- status.

### Validation log

Append material checks with date, command or method, and result. Avoid noisy logs.

## Status lifecycle

- proposed: captured, but not yet authorized to execute.
- ready: approved and ready for an owner to pick up.
- in_progress: an owner is actively working.
- blocked: cannot proceed until a dependency, decision, or external input is resolved.
- review: work appears complete; acceptance is pending.
- done: acceptance criteria verified or explicitly accepted.
- cancelled: no longer required.

Normal transitions:

- proposed → ready or cancelled;
- ready → in_progress;
- in_progress → ready (handoff), blocked, or review;
- blocked → ready, in_progress, or cancelled;
- review → in_progress or done.

Reopening a completed item requires a note explaining why; otherwise create a new Work Item and link the prior one.

## Handoff quality checklist

Before setting a task to ready, verify:

- The requested outcome is explicit.
- The next owner is optional but clear if known.
- Conclusions have provenance.
- Completed work is separated from proposed work.
- The current workspace snapshot is recorded where relevant.
- Next actions are executable.
- Acceptance criteria are testable.
- Required approvals and permissions are not assumed.
- No hidden reasoning, secrets, or irrelevant transcript dump is included.
