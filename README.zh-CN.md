# Project Continuity

**版本：** 1.3.0 | **语言：** [English](README.md) | 简体中文

Project Continuity 是一套**可选、轻量、与 Agent 无关的项目上下文保存协议**，用于在不同会话、Agent、人员、工具和机器之间保留真正需要长期延续的信息。

它不是项目管理系统、Issue Tracker、任务调度器、Agent Runtime，也不是编排平台。不应该默认安装到每一个代码仓库。它只负责保存现有项目文档和工具没有妥善保存的长期上下文。

## v1.3 的核心原则

**不要重复建设 Git、项目文档、Issue Tracker 或编排器已经解决的能力。**

对于普通软件仓库，`README.md`、`AGENTS.md`、架构文档、ADR、测试、Git，以及 Orca 这样的编排器通常已经足够。直接使用这些工具即可。只有当重要上下文需要跨越单次会话、Agent、Issue 或编排 Run 长期保存，而且现有系统没有合适的位置时，才需要 Project Continuity。

## 什么时候使用

适合使用：

- 长期研究或工程项目持续多个会话、Agent 和工具；
- 重要决策和证据需要跨模型厂商或 Runtime 保存；
- 工作横跨多个仓库或系统，没有统一的信息来源；
- 需要把未完成工作交给其他 Agent 或人员，而现有记录不足以支持接手。

通常不需要使用：

- 单次会话内可以完成的普通代码修改；
- 已有完善 README、AGENTS.md、架构文档和 ADR 的软件仓库；
- 已由 GitHub Issues、Jira、Linear 等管理的任务；
- Orca 已经管理当前 Run、Tasks、依赖、Worker 消息和 Worktree；
- 现有研究记录或实验记录已经保存了所需上下文。

详细判断见 `.agents/skills/project-continuity/references/when-to-use.md`；v1.2 升级说明见 `docs/migration-v1.2-to-v1.3.md`。

## 系统职责边界

| 系统 | 负责内容 |
|---|---|
| 项目文档 | 项目目的、安装、架构、约定和领域知识 |
| ADR / 决策记录 | 已接受的技术和研究决策 |
| Issue Tracker | 待办、工单、负责人和流程状态 |
| Orca 或其他编排器 | 实时 Run、Task、依赖、Dispatch、Worker、消息、Worktree 和执行状态 |
| Git | 源码历史、分支、提交和合并 |
| Project Continuity | 其他系统没有妥善保存的跨上下文长期信息 |

Project Continuity 不负责配置 Orca、选择 Agent/模型、创建 Worker、调度 DAG、管理 Worktree、合并分支或监控执行。不要把 Orca Task 复制成 Work Item，也不要在 v1.3 中为每个 Run 创建 Execution Record。

## 六种操作

只有存在真实的连续性需求时，才使用这些操作：

| 操作 | 用途 |
|---|---|
| init | 检查现有资料后，建立最小必要的连续性记录。 |
| adapt | 补充真正缺失的上下文；不需要修改也是有效结果。 |
| handoff | 现有系统不足以支持接手时，保存跨上下文交接信息。 |
| resume | 核对真实工作区并继续已有交接。 |
| update | 将长期有价值的知识或决策更新到权威位置。 |
| status | 汇总连续性记录，不冒充实时 Orca 或 Issue 状态。 |

可以直接用自然语言，也可以调用 Skill：

~~~text
Codex: $project-continuity init
Antigravity CLI: /project-continuity init

Codex: $project-continuity handoff
Antigravity CLI: /project-continuity handoff

Codex: $project-continuity resume W-YYYYMMDD-short-title
Antigravity CLI: /project-continuity resume W-YYYYMMDD-short-title
~~~

Skill 必须先检查已有文档和工具。如果现有资料已经满足需求，应明确说明不需要 Project Continuity，并且不创建任何文件。

## 记录均为可选

以下四种项目记忆文件不是强制组合：

| 文件 | 仅在以下情况创建 |
|---|---|
| `PROJECT.md` | 项目长期背景尚未被其他文档记录 |
| `STATE.md` | 确实需要跨会话快照，且没有现有路线图/状态记录 |
| `DECISIONS.md` | 项目没有 ADR 或其他决策记录 |
| `OPEN_QUESTIONS.md` | 未解决问题需要长期保存，且没有 Issue/研究问题系统 |

Work Item 是可选的**交接记录**，不是通用 Backlog、调度器，也不是 Orca Task 或 Issue 的替代品。只有当工作必须跨越重要上下文边界，且接手方无法依赖现有记录时才创建。Work Item 继续使用 schema version 1.1，以保持兼容性。

## 安装

### Codex CLI 和 Antigravity CLI

~~~bash
git clone https://github.com/HiJean99/project-continuity.git
cd project-continuity
./scripts/validate.sh
./scripts/install-global.sh
~~~

安装位置：

- Codex CLI：`$CODEX_HOME/skills/project-continuity/`，默认 `~/.codex/skills/project-continuity/`。
- Antigravity CLI：`~/.gemini/antigravity-cli/skills/project-continuity/`。

检查安装副本：

~~~bash
./scripts/install-global.sh check
~~~

安装脚本不会覆盖非本项目管理的目录。若 CLI 未发现更新后的 Skill，请重新启动 CLI。

### 其他 Agent Runtime

通用 Skill 源码位于 `.agents/skills/project-continuity/`。支持 Agent Skills 的 Runtime 可以将其安装或链接到对应的全局 Skill 目录。

## 向后兼容

- 现有 v1.1 Work Item 继续有效。
- v1.2 的 Orca Execution Record 和校验器保留为**历史兼容功能**。v1.3 不再创建新的 Execution Record，也不把 Orca 视为 Project Continuity 的执行后端。
- 不会自动迁移、删除或重命名用户已有项目文件。

## 验证

~~~bash
./scripts/validate.sh
python3 scripts/validate_work_item.py work/items/W-YYYYMMDD-short-title.md
~~~

仅对历史 v1.2 Execution Record 使用：

~~~bash
python3 .agents/skills/project-continuity/scripts/validate_execution.py path/to/legacy-execution-record.md
~~~

## 设计

核心仍然基于 Markdown 和 Git。不要求数据库、守护进程、MCP Server、厂商专属会话解析器，也不会自动 Commit/Push。详细设计见 `docs/design.md` 和 Skill references。

## 贡献

保持核心可选、轻量、Agent 中立和项目类型中立。优先使用现有权威资料，不要把编排、任务管理或厂商专属功能加入核心。

## 许可证

MIT，见 LICENSE。
