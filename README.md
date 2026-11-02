# Project Continuity

**Version:** 1.3.0 | **Languages:** English | [简体中文](README.zh-CN.md)

Project Continuity is an **optional, lightweight, agent-neutral protocol** for preserving durable project context across sessions, agents, people, tools, and machines.

It is not a project manager, issue tracker, task scheduler, agent runtime, or orchestration platform. It should not be installed into every repository by default. Its job is to preserve only the context that existing project documentation and tools do not already preserve.

## The v1.3 principle

**Do not build a second system for work that Git, project documentation, an issue tracker, or an orchestrator already manages.**

For an ordinary software repository, `README.md`, `AGENTS.md`, architecture docs, ADRs, tests, Git, and an orchestrator such as Orca are usually enough. Use those directly. Project Continuity becomes useful when important context must outlive an individual session, agent, issue, or orchestration Run and has no suitable existing home.

## When to use it

Use Project Continuity when:

- a long-running research or engineering effort spans many sessions, agents, or tools;
- important decisions and evidence must survive provider/runtime changes;
- work crosses multiple repositories or systems without a shared source of truth;
- a receiving agent/person needs a durable handoff that existing project records cannot provide.

Usually do **not** use it when:

- a coding task is self-contained in one session;
- the repository already has useful README, AGENTS.md, architecture docs, and ADRs;
- active work is already tracked in GitHub Issues, Jira, Linear, or another issue tracker;
- Orca already manages the active Run, Tasks, dependencies, Worker messages, and Worktrees;
- existing research/experiment records already preserve the relevant context.

See `.agents/skills/project-continuity/references/when-to-use.md` for the decision guide and `docs/migration-v1.2-to-v1.3.md` for the upgrade notes.

## System boundaries

| System | Owns |
|---|---|
| Project documentation | Purpose, setup, architecture, conventions, domain knowledge |
| ADR / decision log | Accepted technical and research decisions |
| Issue tracker | Backlog, tickets, owners, workflow status |
| Orca or another orchestrator | Live Runs, Tasks, dependencies, Dispatches, Workers, messages, Worktrees, execution state |
| Git | Source history, branches, commits, merges |
| Project Continuity | Durable cross-context knowledge not already represented elsewhere |

Project Continuity does not configure Orca, choose Agents/models, create Workers, schedule DAGs, manage Worktrees, merge branches, or monitor execution. Do not mirror Orca Tasks as Work Items or create per-Run Execution Records in v1.3.

## Operations

The Skill supports six operations, but only when there is a real continuity need:

| Operation | Purpose |
|---|---|
| init | Establish the smallest useful continuity layer after inspecting existing sources. |
| adapt | Fill a genuine continuity gap; a no-op is a valid result. |
| handoff | Preserve unfinished work across a context boundary when existing systems are insufficient. |
| resume | Verify the workspace and continue a durable handoff. |
| update | Consolidate durable knowledge or decisions in their authoritative location. |
| status | Summarize continuity records, not live orchestrator or issue status. |

Use natural language or invoke the Skill directly:

~~~text
Codex: $project-continuity init
Antigravity CLI: /project-continuity init

Codex: $project-continuity handoff
Antigravity CLI: /project-continuity handoff

Codex: $project-continuity resume W-YYYYMMDD-short-title
Antigravity CLI: /project-continuity resume W-YYYYMMDD-short-title
~~~

The Skill must inspect existing docs and tools first. If they already cover the need, it should report that Project Continuity is unnecessary and make no changes.

## Records are optional

The four common project-memory files are not a mandatory bundle:

| File | Create only when |
|---|---|
| `PROJECT.md` | Stable project context is not already documented |
| `STATE.md` | A cross-session snapshot is useful and no existing roadmap/status source serves that role |
| `DECISIONS.md` | No ADR or existing decision log exists |
| `OPEN_QUESTIONS.md` | Questions need a durable home and are not already issues/research questions |

A Work Item is an optional **handoff artifact**, not a general backlog item, scheduler, or replacement for an Orca Task or issue. Create one only when the outcome must survive a meaningful context boundary and the receiving context cannot rely on existing records. Work Items retain schema version 1.1 for compatibility.

## Installation

### Codex CLI and Antigravity CLI

~~~bash
git clone https://github.com/HiJean99/project-continuity.git
cd project-continuity
./scripts/validate.sh
./scripts/install-global.sh
~~~

The installer copies the Skill to:

- Codex CLI: `$CODEX_HOME/skills/project-continuity/` (default `~/.codex/skills/project-continuity/`).
- Antigravity CLI: `~/.gemini/antigravity-cli/skills/project-continuity/`.

Check installed copies:

~~~bash
./scripts/install-global.sh check
~~~

The installer does not overwrite an unmanaged directory. Restart the CLI if it does not discover the updated Skill.

### Other Agent runtimes

The portable Skill source is `.agents/skills/project-continuity/`. Install or link it to the runtime's documented Skill directory.

## Backward compatibility

- Existing v1.1 Work Items remain valid.
- v1.2 Orca Execution Records and their validator are retained as **legacy artifacts** for existing projects. v1.3 does not create new Execution Records or treat Orca as a Project Continuity backend.
- Existing project files are not automatically migrated, deleted, or renamed.

## Validation

~~~bash
./scripts/validate.sh
python3 scripts/validate_work_item.py work/items/W-YYYYMMDD-short-title.md
~~~

For historical v1.2 Execution Records only:

~~~bash
python3 .agents/skills/project-continuity/scripts/validate_execution.py path/to/legacy-execution-record.md
~~~

## Design

The core remains Markdown and Git based. No database, daemon, MCP server, provider-specific session parser, or automatic commit/push is required. See `docs/design.md` and the Skill references for detailed behavior.

## Contributing

Keep the core optional, minimal, agent-neutral, and project-type-neutral. Prefer existing sources of truth. Do not add orchestration, task-management, or provider-specific features to the core.

## License

MIT. See LICENSE.
