# Work Items

Each meaningful unit of unfinished work lives in items/<work-id>.md.

A Work Item is both the task record and the cross-agent handoff package. Update the same file as work progresses or changes owner; do not create duplicate handoff summaries.

The YAML status field is authoritative:

- proposed: captured, not yet approved;
- ready: approved and ready to pick up;
- in_progress: being worked on;
- blocked: waiting for a dependency or input;
- review: awaiting acceptance;
- done: accepted and verified;
- cancelled: no longer required.

depends_on records dependencies but does not schedule or execute them. Agents must verify dependencies before proceeding.

An analysis-only agent may write a Work Item only as an explicitly requested handoff artifact and only with approval for that file. It must not modify source code or other project memory. The receiving agent verifies the snapshot and then continues the same Work Item.


## Optional executions

When this project uses Orca Orchestration, store one Execution Record per bounded Run under `executions/`. A Work Item may link to multiple Execution Records. See the Project Continuity Skill reference `execution-record-format.md`. This directory is optional; do not create it for projects that do not use Orca.
