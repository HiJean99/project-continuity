## Project Continuity (optional)

Use the project-continuity Skill only when durable context must survive a meaningful session, agent, person, or tool boundary and existing project records do not already cover it.

- Prefer this repository's README, AGENTS.md, architecture docs, ADRs, issue tracker, experiment records, and native orchestration state as the sources of truth.
- Do not create Project Continuity files by default; add only the missing record.
- Do not duplicate ordinary tickets or Orca Tasks as Work Items. Orca owns live Runs, Tasks, Workers, messages, Worktrees, and execution state.
- Work Items are optional durable handoff notes, not a scheduler or general backlog.
- Record durable conclusions and decisions in their existing authoritative locations. Never store hidden reasoning, full transcripts, or secrets.
