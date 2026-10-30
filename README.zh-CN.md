# Project Continuity

**跨 Agent、跨会话、跨项目的工作连续性工具。**

Project Continuity 是一套轻量的项目记忆与任务交接协议。它让一项尚未完成的工作能够从 AGY 交给 Codex、从 Codex 交回其他 Agent，或在几天后由新的会话继续推进。

它不试图同步模型的隐藏推理，也不负责启动或编排 Agent 进程。它只持久化真正有助于继续工作的内容：目标、背景、结论、证据、已完成事项、当前状态、下一步和验收标准。

**语言：** [English](README.md) | 简体中文

## 核心能力

- **项目记忆：** 使用 PROJECT.md、STATE.md、DECISIONS.md 和 OPEN_QUESTIONS.md 保存长期背景、当前状态、重要决策和未解决问题。
- **持久化任务：** 需要跨会话或跨 Agent 延续的重要工作，保存为独立的 Markdown Work Item。
- **交接即任务：** 同一份 Work Item 同时承担任务记录和交接包，不重复维护 TASK.md 与 HANDOFF.md。
- **可靠恢复：** 接手的 Agent 先检查实际文件、Git 状态、依赖和验证结果，再从未完成的步骤继续。
- **角色灵活：** 不预设某个 Agent 负责研究、另一个负责编码。任务由谁承担、下一步交给谁，都在 Work Item 中按实际情况记录。
- **跨工具可移植：** 基于 Markdown、Git 和 Agent Skills，不依赖数据库、守护进程、MCP Server 或特定模型厂商。
- **证据优先：** 保存可见结论、来源、假设、决策和结果，不保存模型隐藏推理。
- **高保真交接：** 保留原始工作成果和明确来源，给接手 Agent 一个唯一、可执行的下一步。
- **一致性检查：** 任务创建或关闭时，检查项目状态和关联问题是否过时。

## 六种操作

| 操作 | 用途 |
|---|---|
| init | 为新项目初始化项目记忆和工作记录结构。 |
| adapt | 检查已有项目，以最小改动补充连续性结构，避免重复已有权威文档。 |
| handoff | 将当前讨论或未完成工作整理成可由其他 Agent 或后续会话接手的任务。 |
| resume | 核对项目真实状态，继续已有任务。 |
| update | 将有长期价值的进展整理到项目记忆。 |
| status | 查看当前项目状态和未完成任务。 |

不必记住这些命令。直接用中文描述需求，Agent 也可以根据意图选择操作。

### Codex CLI 示例

~~~text
$project-continuity init
$project-continuity adapt
$project-continuity handoff
$project-continuity resume W-20261030-short-title
$project-continuity update
$project-continuity status
~~~

### Antigravity CLI（AGY）示例

~~~text
/project-continuity init
/project-continuity adapt
/project-continuity handoff
/project-continuity resume W-20261030-short-title
/project-continuity update
/project-continuity status
~~~

也可以直接说：

- “先读取项目记忆，告诉我目前进展。”
- “把这轮讨论整理成交接任务，交给 Codex。”
- “这个任务还没完成，保存进度和下一步。”
- “读取上次的 Work Item，核对状态后继续。”
- “检查本次工作是否产生需要长期保存的决策。”

只有真正需要跨会话、跨 Agent 或跨人员延续的工作才需要创建 Work Item。简单问答和一次性小修改不必建任务。

## 安装

### Codex CLI 和 Antigravity CLI

先克隆仓库：

~~~bash
git clone https://github.com/HiJean99/project-continuity.git
cd project-continuity
~~~

检查并安装：

~~~bash
./scripts/validate.sh
./scripts/install-global.sh
~~~

安装脚本会将同一份 Skill 安装到两个 CLI 各自的全局目录：

- **Codex CLI：** $CODEX_HOME/skills/project-continuity/，默认是 ~/.codex/skills/project-continuity/。
- **Antigravity CLI：** ~/.gemini/antigravity-cli/skills/project-continuity/。

如果 CLI 没有立即发现 Skill，重新启动对应 CLI。

检查全局安装副本是否与当前仓库一致：

~~~bash
./scripts/install-global.sh check
~~~

安装脚本不会覆盖没有由本项目安装标记的同名目录。

### 更新

在仓库目录中执行：

~~~bash
git pull
./scripts/validate.sh
./scripts/install-global.sh
~~~

更新后重新启动 CLI（如果当前会话尚未重新发现 Skill）。

### 其他 Agent Runtime

Skill 源码位于标准项目级目录：

~~~text
.agents/skills/project-continuity/
~~~

支持 Agent Skills 格式的其他 Runtime 可以复用同一份 Skill。将该目录安装或链接到对应 Runtime 文档规定的全局 Skills 目录即可。

当前安装脚本只适配 Codex CLI 和 Antigravity CLI，不会猜测其他工具的安装路径。

## 项目文件结构

新项目可以采用以下结构：

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

Skill 会先检查项目现有文档。若已有 README、架构说明、路线图、决策记录、Issue Tracker 或研究记录承担相同职责，就优先复用并建立链接，不会为了符合模板而复制一份。

### 项目记忆

| 文件 | 职责 |
|---|---|
| PROJECT.md | 项目长期背景、目标、范围、约束、术语和权威资料入口。 |
| STATE.md | 当前已核实的状态、正在进行的工作、阻塞和下一里程碑。 |
| DECISIONS.md | 重要决策及理由，采用追加记录，不覆盖历史决策。 |
| OPEN_QUESTIONS.md | 可能影响项目方向或实现的未解决问题。 |

这些文件不是聊天记录。应保持简洁，详细研究、实验、代码和领域资料仍保存在项目原有的权威位置。

### Work Item：任务与交接的共同载体

每个需要持续推进的工作，使用 work/items/ 下的一份 Markdown 文件。

Work Item 应包含：

1. 目标和背景。
2. 已有发现、结论和决策。
3. 证据、来源和相关文件。
4. 已完成的工作。
5. 当前工作区快照（适用时包括 Git 分支、Commit 和未提交文件）。
6. 可直接执行的下一步。
7. 可验证的验收标准。
8. 约束、风险、假设和交接记录。

新版 Work Item 使用 schema version 1.1，并包含一个提示性 revision 版本号，用于发现可能的旧内容覆盖。它不是分布式锁；同一份 Work Item 应保持单一写入者，需要换 Agent 时先交接所有权，不要并发编辑。

仓库提供不依赖第三方库的 Work Item 校验器：scripts/validate_work_item.py。交接或标记完成前，可以运行：

~~~bash
python3 scripts/validate_work_item.py work/items/W-YYYYMMDD-short-title.md
~~~

Work Item 的状态：

| 状态 | 含义 |
|---|---|
| proposed | 已提出，但尚未批准执行。 |
| ready | 已批准，可以接手。 |
| in_progress | 正在执行。 |
| blocked | 等待依赖、决策或外部输入。 |
| review | 工作已完成，等待验收。 |
| done | 验收标准已经核实或由用户明确接受。 |
| cancelled | 不再需要。 |

典型流程：

~~~text
proposed -> ready -> in_progress -> review -> done
                         |
                         +-> blocked -> ready
                         |
                         +-> ready（交给另一个 Agent）
~~~

done 不代表 Agent 停止工作，而是代表验收条件已经得到验证或明确接受。

## 推荐的日常使用方式

### 1. 开始工作

让 Agent 先读取项目记忆和未完成任务：

~~~text
先读取项目记忆，检查当前状态和未完成任务，再开始处理我的需求。
~~~

### 2. 从 AGY 交给 Codex

在 AGY 中：

~~~text
/project-continuity handoff
~~~

或直接说：

~~~text
把刚才的分析整理成 Codex 可以直接执行的 Work Item。
保留重要结论、证据、已完成工作、未解决问题、
下一步操作和验收标准。只创建交接任务，不修改代码。
~~~

AGY 创建并读回 Work Item 后，在 Codex 中：

~~~text
$project-continuity resume W-YYYYMMDD-short-title
~~~

### 3. 从 Codex 交回 AGY

Codex 遇到需要独立分析的问题时，也可以整理当前实现、已有证据和待回答问题，交给 AGY：

~~~text
$project-continuity handoff
~~~

AGY 接手：

~~~text
/project-continuity resume W-YYYYMMDD-short-title
~~~

谁思考、谁执行、谁审查，由具体任务决定，不固定 Agent 角色。

### 4. 暂停并在以后继续

工作暂时不做时：

~~~text
保存当前任务进度、已经完成的内容、阻塞原因和下一步，
确保另一个会话可以直接接着做。
~~~

以后通过 resume 恢复，不需要依赖原来的聊天历史。

### 5. 重要工作完成后更新记忆

~~~text
/project-continuity update
~~~

或在 Codex 中：

~~~text
$project-continuity update
~~~

只整理有长期价值的进展、决策和状态变化，不要把每次对话都写进项目记忆。

## 权限与安全边界

- Skill 不会自动启动另一个 Agent，也不会自动替用户授权。
- 只读分析 Agent 可以准备交接内容；要持久化时，必须获得对目标 Work Item 的文件写入权限。
- 在严格只读模式下，Agent 应输出完整交接内容，不能声称已经保存。
- Skill 指令不是操作系统级安全隔离。需要强制限制写入范围时，应使用 Agent Runtime 自身的权限或沙箱机制。
- 不要把密码、Token、私钥、.env 内容或其他敏感信息写入项目记忆和 Work Item。
- 接手者必须核对真实工作区，不能盲目信任过期的状态快照。

## 设计边界

Project Continuity 是一套文件协议和 Skill，不是完整的 Agent 编排平台。它不负责：

- 启动、监控或切换 Agent 进程；
- 同步不同 Provider 的内部会话和隐藏推理；
- 在交接后自动启动另一个 Agent；
- 通用 DAG 调度、后台任务队列或可视化任务看板；
- 自动提交或推送项目代码。

## 贡献

保持核心协议跨 Agent、跨项目类型。优先采用小幅、向后兼容的改动。特定 Provider 的能力应保持可选，不要让核心 Work Item 格式依赖某一家厂商。

## 许可证

MIT License，详见 LICENSE。
