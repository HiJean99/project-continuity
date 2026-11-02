# When to Use Project Continuity

Project Continuity is an optional context-preservation layer, not a required project scaffold.

## Decision table

| Situation | Use Project Continuity? | Preferred source of truth |
|---|---|---|
| One-off code change in one session | No | Current repo, Git, tests |
| Ordinary Python/TypeScript repository | Usually no | README, AGENTS.md, architecture docs |
| Multi-agent implementation already tracked in Orca | No duplicate task records | Orca Run / Tasks / messages / Worktrees |
| Backlog item already tracked in GitHub/Jira/Linear | No duplicate Work Item | Existing issue tracker |
| Long-running research across months and agents | Often yes | Existing research docs plus minimal continuity records |
| Cross-repository project with no common tracker | Often yes | Minimal project context and durable handoff |
| Agent/provider change with unfinished work not captured elsewhere | Yes, if a durable handoff is needed | One Work Item |
| Accepted technical decision not recorded elsewhere | Update the existing ADR/decision source; use DECISIONS.md only if none exists | ADR or decision log |

## Minimalism rules

1. Inspect before initializing.
2. If README, AGENTS.md, ADRs, issue trackers, experiment logs, and orchestrator state already cover the need, make no changes.
3. Add only the missing record. Do not create PROJECT.md, STATE.md, DECISIONS.md, OPEN_QUESTIONS.md, and `work/` as a mandatory bundle.
4. Do not mirror Orca Tasks in Work Items or Orca Runs in Execution Records.
5. Keep Work Items for cross-context handoffs and durable outcomes, not routine task tracking.
6. Prefer the project's existing documentation conventions and vocabulary.

## Relationship with Orca

Orca is an independent orchestration system. It owns the live execution lifecycle: Runs, Tasks, dependencies, Dispatches, Workers, messages, Worktrees, and execution status. Project Continuity does not define Agent Team Policies or model profiles, configure Orca, choose Agents or models, schedule Workers, merge Worktrees, or monitor Runs.

Use Orca directly for multi-agent software development. Update project documentation with durable architectural decisions or verified outcomes when useful. Only use Project Continuity if additional context must survive beyond the project docs and Orca's execution records.

## Examples

### Ordinary software refactor

A Python repository has README.md, AGENTS.md, tests, and Orca manages three Workers in a Run. Use Orca for planning/execution and Git for branches/merges. Do not initialize Project Continuity and do not create a Work Item or Execution Record for each Task.

### Long-running research programme

A materials research programme spans multiple repositories, experiments, and agent providers. Existing records do not provide a concise cross-session state or preserve unsettled decisions. Add only the missing context records and use Work Items for genuine cross-context handoffs.

### Cross-agent handoff outside an orchestrator

An analysis agent has produced a detailed conclusion and an implementation agent in another runtime must continue next week. If no issue tracker or project record can hold the exact context, create one Work Item with evidence, constraints, artifact links, and one immediate next action.
