# Harbor、OpenClaw 与 ATIF：面向金融 Agent 的轨迹评测

Harbor 当前主干已经包含 `openclaw` agent 集成，并生成 ATIF-v1.7 轨迹。对金融 Agent 评测来说，这提供了一个很有价值的基础：评测不只看最终答案，也能检查用户指令、工具调用、observation、来源元数据、时间边界和安全相关动作。

来源：

- [Harbor 仓库](https://github.com/harbor-framework/harbor)
- [OpenClaw agent 集成源码](https://github.com/harbor-framework/harbor/blob/main/src/harbor/agents/installed/openclaw.py)
- [ATIF RFC 0001](https://github.com/harbor-framework/harbor/blob/main/rfcs/0001-trajectory-format.md)
- [OpenClaw 集成 PR #1661](https://github.com/harbor-framework/harbor/pull/1661)

本文在 2026 年 5 月 31 日基于 Harbor 主干提交 [`eecd142`](https://github.com/harbor-framework/harbor/commit/eecd142) 核对。Harbor 仍在快速迭代，依赖具体实现细节前应再次确认。

## 为什么 ATIF 对金融评测重要

金融 Agent 的最终答案看起来正确，并不代表过程可信。例如：

- 答案没有来源证据，
- 工具调用读取了评测时间截点之后的数据，
- 回测任务静默使用了未来数据，
- observation 无法关联到对应工具调用，
- Agent 调用了私有数据或交易执行工具，
- 最终回答混淆了分析和投资建议。

ATIF 用结构化方式记录 step、tool call、observation 和元数据，使这些过程问题可以被审计。

## 建议的金融轨迹审计 Profile

| 检查项 | 意义 |
| --- | --- |
| 保留用户指令 | 确认轨迹包含真实任务边界。 |
| Step 连续性 | 保证审计链可重建。 |
| Tool call 与 observation 关联 | 将证据和失败归因到具体动作。 |
| 来源文档元数据 | 区分有来源检索和无依据结论。 |
| 评测时间截点 | 检测预测、检索和回测任务中的时间泄漏。 |
| 禁用工具调用 | 避免评测任务将交易执行或私有数据查询常态化。 |
| 非投资建议边界 | 区分分析示例和个性化金融建议。 |
| Copied-context 计数 | 在分析训练数据时区分保留上下文和新增交互。 |
| 非 LLM dispatch 计数 | 在 ATIF-v1.7 风格轨迹中显式呈现确定性编排。 |

## 公开示例

[Harbor OpenClaw Financial Trajectory Audit](../examples/harbor-openclaw-finance-trajectory-audit) 包含：

- 一条合成 OpenClaw 风格 ATIF-v1.7 轨迹，
- 一个零依赖审计脚本，
- 面向时间泄漏、禁用工具、缺失来源元数据和缺失非投资建议边界的确定性测试。
- 一个 repeated-trial 聚合示例，用于报告 pass rate、pass@k、Pass^k、缺失证据、时间截点违规和禁用工具调用。

## 不做出的声明

- 这不是 Harbor 官方 profile。
- 这不能替代 Harbor 的 ATIF schema validator。
- 这不用于评测真实交易系统。
- 这不能证明某个 Agent 已满足受监管生产环境要求。
