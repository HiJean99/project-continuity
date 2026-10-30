# Project Continuity

**Languages:** English | [简体中文](README.zh-CN.md)

A lightweight, agent-neutral protocol for preserving project context and continuing unfinished work across agents, sessions, and machines.

Project Continuity does not synchronize hidden model reasoning or manage agent processes. It records the information another person or agent needs to continue the work: goals, decisions, evidence, completed steps, current state, next actions, and acceptance criteria.

## What it provides

- **Project memory:** PROJECT.md, STATE.md, DECISIONS.md, and OPEN_QUESTIONS.md.
- **Durable work records:** one Markdown Work Item for each meaningful piece of work that must survive a session or agent change.
- **Handoff as a task:** the same Work Item is both the task record and the handoff package; no duplicate handoff summary is required.
- **Verified resumption:** the receiving agent checks the actual files, Git state, dependencies, and validation evidence before continuing.
- **Flexible ownership:** no fixed researcher/developer roles. The person or agent responsible for each task is recorded in that task.
- **Portable storage:** Markdown and Git; no database, daemon, MCP server, or model-vendor lock-in.
- **Evidence discipline:** preserve conclusions, sources, assumptions, decisions, and results—not hidden chain-of-thought.

## Operations

The project-continuity Skill supports six operations:

| Operation | Purpose |
|---|---|
| init | Initialize continuity files in a new project. |
| adapt | Inspect an existing project and add the smallest useful continuity layer without duplicating authoritative docs. |
| handoff | Turn unfinished work or a discussion into an actionable Work Item for another agent or a later session. |
| resume | Verify the current workspace and continue an existing Work Item. |
| update | Consolidate meaningful progress into durable project memory. |
| status | Summarize current project state and open Work Items. |

Use natural language or invoke the Skill directly:

~~~text
Codex: $project-continuity init
Antigravity CLI: /project-continuity init

Codex: $project-continuity handoff
Antigravity CLI: /project-continuity handoff

Codex: $project-continuity resume W-YYYYMMDD-short-title
Antigravity CLI: /project-continuity resume W-YYYYMMDD-short-title
~~~

Only create a Work Item when work genuinely needs to continue across sessions, agents, or people. Routine one-off questions do not need task records.

## Installation

### Codex CLI and Antigravity CLI

Clone the repository and run the installer:

~~~bash
git clone https://github.com/HiJean99/project-continuity.git
cd project-continuity

./scripts/validate.sh
./scripts/install-global.sh
~~~

The installer places the Skill in the user-level directories used by these two CLIs:

- Codex CLI: $CODEX_HOME/skills/project-continuity/ (default: ~/.codex/skills/project-continuity/).
- Antigravity CLI: ~/.gemini/antigravity-cli/skills/project-continuity/.

Restart the CLI after installation if the Skill is not discovered.

To check whether both installed copies match the repository version:

~~~bash
./scripts/install-global.sh check
~~~

The installer does not overwrite an existing directory unless it was previously installed by this project.

### Other Agent runtimes

The Skill source is in the standard project-local location:

~~~text
.agents/skills/project-continuity/
~~~

Any runtime that supports the Agent Skills format can use the same Skill. Install or link this directory into the runtime's documented user-level Skills directory. The included installer currently targets Codex CLI and Antigravity CLI; it does not assume paths for other runtimes.

## Project files

A new project can start with this structure:

~~~text
project/
├── AGENTS.md
├── PROJECT.md
├── STATE.md
├── DECISIONS.md
├── OPEN_QUESTIONS.md
└── work/
    ├── README.md
    └── items/
        └── W-YYYYMMDD-short-title.md
~~~

The Skill inspects the existing project before creating files. Existing authoritative documentation, roadmaps, decision logs, issue trackers, and research records should be reused and linked—not copied merely to match this template.

### Project memory

| File | Responsibility |
|---|---|
| PROJECT.md | Stable purpose, goals, scope, constraints, terminology, and sources of truth. |
| STATE.md | Current verified snapshot, active work, blockers, and next milestone. |
| DECISIONS.md | Append-only record of material decisions and their rationale. |
| OPEN_QUESTIONS.md | Unresolved questions that may affect direction or implementation. |

### Work Items

A Work Item under work/items/ is the durable record of one actionable outcome. It includes:

- objective and context;
- findings, decisions, and evidence;
- completed work;
- current workspace snapshot;
- ordered next actions;
- acceptance criteria;
- constraints, risks, and handoff/validation history.

The status lifecycle is:

proposed → ready → in_progress → review → done

A task can also become blocked or cancelled. done means the acceptance criteria have been verified or explicitly accepted; it does not merely mean an agent stopped working.

## Design boundaries

Project Continuity is a file protocol and Skill, not a full orchestration platform.

It does not:

- launch, supervise, or switch agent processes;
- synchronize provider-specific sessions or hidden reasoning;
- automatically execute another agent after a handoff;
- implement a general DAG scheduler or task dashboard;
- automatically commit or push project changes.

A read-only analysis agent may prepare a handoff, but persistence requires permission to write the single Work Item. Skill instructions are not an operating-system security boundary; use the runtime's permission controls when write isolation matters.

## Contributing

Keep the core protocol agent-neutral and project-type-neutral. Prefer small, additive changes. Do not add provider-specific behavior to the core Work Item format unless it is optional and preserves portability.

## License

MIT. See LICENSE.
