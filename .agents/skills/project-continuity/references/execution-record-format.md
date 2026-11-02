# Execution Record Format

An Execution Record is an optional, durable summary of one bounded execution phase. It links one Work Item to one Orca Run. It is not the Work Item, not a live dashboard, and not a transcript.

## File name and metadata

Use `E-YYYYMMDD-short-slug.md`; add a numeric suffix for same-day collisions.

```yaml
---
id: E-YYYYMMDD-short-slug
work_item_id: W-YYYYMMDD-short-slug
backend: orca
backend_version: "1.4.x"
run_id: ""
objective: Bounded execution objective
status: planned
created: YYYY-MM-DD
updated: YYYY-MM-DD
schema_version: "1.2"
revision: 1
---
```

Allowed statuses: `planned`, `active`, `blocked`, `review`, `completed`, `failed`, `cancelled`.

`run_id` may be empty while planned. Once a Run is created, record its exact ID. Never invent IDs. `backend_version` is informational; use the exact version when known.

## Required sections

- `Objective`: bounded phase outcome and relation to the Work Item.
- `Run`: exact backend, version, Run ID, objective, and creation context.
- `Task map`: one subsection per Task with exact Task ID, concise spec, dependencies, Worker/agent, Dispatch IDs/attempts, and outcome. Use `TBD` only before creation.
- `Evidence and outputs`: paths, commits, test results, experiment IDs, citations, and provenance.
- `Blockers and decisions`: unresolved issues and decisions escalated to the user.
- `Reconciliation`: what was verified, what was written back to the Work Item/project memory, and what remains.
- `Next action`: exactly one immediate action while status is not completed/cancelled.
- `History`: concise dated events; no raw transcript or hidden reasoning.

## State semantics

Execution status describes this Run phase, not the Work Item lifecycle. `completed` means the Run's required Tasks have settled and the Coordinator has reconciled the results. It does not mean the parent Work Item is done. A Work Item can have several completed Execution Records and remain in progress or review.

Keep Orca as the authority for live Run/Task/Dispatch/Worker state. Refresh this record on meaningful events and at reconciliation; do not poll or pretend the Markdown copy is live.
