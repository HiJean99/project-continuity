# Operation Procedures

## init — establish continuity only when needed

1. Inspect the target path, Git state, README, AGENTS.md, architecture docs, ADRs, issue trackers, experiment records, and native orchestration tools.
2. Apply the decision guide in `when-to-use.md`.
3. If existing sources already preserve the needed context, make no changes and explain why Project Continuity is unnecessary.
4. If continuity is needed, identify the single missing information category and create only its corresponding record. Do not create the four memory files or `work/` bundle automatically.
5. Preserve all existing files and conventions. Mark unknown facts rather than inventing them.
6. Verify links and Git diff. Do not commit unless asked.

## adapt — improve an existing continuity setup minimally

1. Inspect project docs, instructions, trackers, orchestrator state (if relevant), and Git status.
2. Identify duplicated or missing durable context. Existing authoritative docs take precedence over Project Continuity templates.
3. If no meaningful gap exists, report a no-op; do not manufacture files or structure.
4. If a gap exists, present a short plan for non-trivial changes and make only additive, non-destructive changes authorized by the user.
5. Do not duplicate Orca Runs, Tasks, Dispatches, Worker messages, or Worktree state.
6. Verify links, paths, and Git diff. Do not commit unless asked.

## handoff — preserve cross-context unfinished work

1. Check whether the work is already represented by an issue, Orca Task, or authoritative project record. If so, use that system; do not create a duplicate Work Item.
2. Create/update a Work Item only if the receiving agent/person/session cannot reliably continue from existing records.
3. Capture the objective, useful visible context, accepted decisions, evidence, completed work, actual workspace snapshot, constraints, unresolved questions, acceptance criteria, and one immediate Next action.
4. Preserve exact work products at their source paths; link them rather than copying large artifacts.
5. Set `proposed` if authorization is unclear; use `ready` only when execution is approved.
6. Keep one active writer. Re-read the Work Item immediately before updating it.
7. Do not claim an Agent was launched. Handoff records context; the receiving tool/orchestrator controls execution.

## resume — continue a durable handoff

1. Use the supplied Work Item ID. If none is supplied, identify open items and ask only if multiple candidates are plausible.
2. Read the Work Item and only relevant project records.
3. Verify the actual workspace, Git state, artifacts, dependencies, and tests. Actual state outranks stale snapshots.
4. Continue the immediate Next action. Do not duplicate work already completed.
5. Record material progress only if it remains useful across a context boundary. If the work is now tracked in an orchestrator or issue tracker, use that system for live execution state.
6. Mark review/done according to the Work Item's durable handoff outcome, not a Worker status.

## update — consolidate durable knowledge

1. Identify what changed that will remain useful after the current session or execution ends.
2. Update the existing authoritative document (README, architecture doc, ADR, experiment record, etc.) first.
3. Use Project Continuity files only for information with no suitable existing home.
4. Keep STATE.md a concise verified snapshot, not a diary or orchestrator dashboard.
5. Append material decisions; do not rewrite history.
6. Do not copy transient Orca Run/Task/Dispatch/Worker status into continuity records.

## status — summarize continuity records

1. Read only the existing continuity records relevant to the request.
2. Do not infer live project/task/Worker status from stale Markdown.
3. If the user asks for live Orca or issue status, use that system directly rather than Project Continuity.
4. Do not modify files unless asked.
