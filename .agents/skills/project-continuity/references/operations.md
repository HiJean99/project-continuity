# Operation Procedures

## init — new project

1. Resolve the target path and project name. If the path does not exist, create it only when the user explicitly asked to create a project there.
2. Inspect the directory and Git state. Do not assume it is empty.
3. Create only missing continuity files using the templates.
4. Populate facts available from the user's request and existing files. Mark unknown fields as unknown or ask one focused question if the missing information blocks useful initialization.
5. Create work/README.md and work/items/.
6. Add a short Project Continuity section to AGENTS.md, preserving any existing instructions.
7. Summarize created files and unresolved information.

## adapt — existing project

1. Inspect the project tree, README, existing instruction files, documentation, task trackers, and Git status.
2. Map existing authoritative documents to the memory model. Do not create a second architecture document, roadmap, ADR log, issue list, or changelog if an existing source already serves that purpose.
3. Present a short adaptation plan when changes are non-trivial. For a clear user-authorized adaptation, make additive, non-destructive changes.
4. Create missing continuity files or add links to existing equivalents. Preserve user content and all unrelated dirty changes.
5. Add a small instruction pointer to AGENTS.md only if absent.
6. Verify links, file paths, and Git diff. Do not commit unless asked.

## handoff — capture unfinished work

1. Identify the work outcome. If an open Work Item already represents it, update that file instead of duplicating it.
2. Extract only the useful, user-visible context from the current conversation: goal, constraints, decisions, evidence, completed work, and remaining work.
3. Verify repository facts and capture the workspace snapshot where relevant.
4. Set status to proposed if authorization is unclear; set ready only when the user has approved the work.
5. Set next_agent or assigned_to only when the intended owner is known. Never assume the next agent based solely on vendor.
6. Update STATE.md with a link to the Work Item only if the current agent is authorized to update project memory. A handoff-only analysis agent writes only the Work Item; the receiving agent updates STATE.md when it adopts the work.
7. If the current agent is in a read-only/plan mode, do not claim persistence: request approval for the single Work Item write or return the complete Markdown artifact for the user to save. Do not broaden permission to source code or other project files.
8. Tell the user the Work Item ID and where it was saved. Do not claim that another agent was launched.

## resume — continue unfinished work

1. If the user gives an ID, use it. Otherwise list open Work Items and ask one question only if multiple candidates are plausible.
2. Read the selected Work Item and relevant project memory.
3. Verify the actual workspace and dependencies. Compare actual state with the saved snapshot.
4. If the snapshot is stale, reconcile it explicitly; do not overwrite current files to force them to match the old note.
5. Continue the first incomplete next action.
6. Record material progress, validation, blockers, and any ownership change in the same Work Item.
7. Update STATE.md when the project-level snapshot changes.
8. Set review or done only according to the status lifecycle and acceptance criteria.

## update — consolidate durable knowledge

1. Review changes and results since the last recorded state.
2. Update STATE.md as a current snapshot, not a transcript.
3. Append accepted/rejected/superseding decisions to DECISIONS.md.
4. Add or resolve OPEN_QUESTIONS.md entries only when the evidence supports the change.
5. Link detailed records rather than copying large logs or reports.
6. Leave uncertain findings labelled as hypotheses or inferences.

## status — show continuity state

1. Read STATE.md and list Work Items not in done or cancelled.
2. Group by status and identify the next actionable item.
3. Do not modify files unless the user asks for an update.
