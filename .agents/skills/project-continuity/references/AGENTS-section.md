## Project Continuity

For work that spans conversations, sessions, or agents:

- Use the project-continuity Skill to initialize/adapt project context, hand off unfinished work, resume a Work Item, or consolidate durable progress.
- Read PROJECT.md and STATE.md when relevant; consult DECISIONS.md and OPEN_QUESTIONS.md as needed.
- Active and historical Work Items live in work/items/. A Work Item is the durable task and handoff record.
- Verify the actual files, Git state, and validation results before resuming. Do not rely on chat history as the only record.
- An analysis-only agent may create or update one Work Item under work/items/ only when explicitly preparing a handoff and only after the file write is approved. It must not edit source code or other project memory.
- Record conclusions, evidence, assumptions, decisions, completed work, and next actions; never store hidden reasoning or secrets.
