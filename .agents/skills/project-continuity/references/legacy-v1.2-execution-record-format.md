# Legacy v1.2 Execution Record Format

**Status: deprecated in v1.3.** This format is retained only to read and validate existing records created under Project Continuity v1.2. Do not create new Execution Records under v1.3.

An Execution Record was a durable summary of one bounded Orca execution phase, linked to a Work Item and one Orca Run. In v1.3, Orca itself owns all execution state; Project Continuity stores only durable cross-context knowledge not already captured elsewhere.

The historical metadata and sections remain documented below for compatibility.

## File name and metadata

Use `E-YYYYMMDD-short-slug.md` for existing records.

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

Allowed historical statuses: `planned`, `active`, `blocked`, `review`, `completed`, `failed`, `cancelled`.

## Historical required sections

- `Objective`
- `Run`
- `Task map`
- `Evidence and outputs`
- `Blockers and decisions`
- `Reconciliation`
- `Next action`
- `History`

## Historical state semantics

Execution status described the Run phase, not the parent Work Item. Orca remained authoritative for live Run/Task/Dispatch/Worker state.
