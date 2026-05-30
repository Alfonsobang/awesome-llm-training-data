# 2026 Agent Evaluation Radar

这份 radar 跟踪 2026 年最值得 LLM 数据和评测团队关注的 Agent 评测方向。它刻意偏实践：目标是帮助团队判断该读什么、该 benchmark 什么、该采集什么证据。

本文不做厂商排名，不发布私有 benchmark 结果，也不声称任何系统具备生产可用性。

## 核心变化

LLM 评测正在从只看答案，转向评估完整 Agent 运行过程：

- 对会使用工具、shell、浏览器、文件和 subagent 的 Agent，只做静态 QA 远远不够。
- 轨迹很重要：工具调用、观察结果、artifact、副作用和不安全的中间动作，都会影响一次运行是否可信。
- 多次运行很重要：单次成功可能只是偶然。
- 评测数据必须包含过程证据，而不仅是最终文本。

## 值得关注的热点

| 方向 | 为什么重要 | 公开入口 |
| --- | --- | --- |
| Harbor OpenClaw ATIF 轨迹 | 将 OpenClaw 风格用户消息、工具调用、observation 和元数据转成可检查的结构化证据。 | [Harbor OpenClaw 金融 ATIF 审计](../examples/harbor-openclaw-finance-trajectory-audit), [OpenClaw 集成源码](https://github.com/harbor-framework/harbor/blob/main/src/harbor/agents/installed/openclaw.py) |
| 轨迹感知评分 | 评估完整过程，而不只是最终输出。 | [Claw-Eval](https://github.com/claw-eval/claw-eval), [Harbor ATIF docs](https://harborframework.com/docs/agents/trajectory-format) |
| 多次运行鲁棒性 | 区分偶然成功和稳定能力。 | [Harbor 多次运行指标示例](../examples/harbor-repeated-trial-metric), [Harbor pass@k utility](https://github.com/harbor-framework/harbor/blob/main/src/harbor/utils/pass_at_k.py) |
| 沙箱化 Agent 环境 | 让工具型 Agent 运行可复现、可检查。 | [Harbor](https://github.com/harbor-framework/harbor), [Terminal-Bench](https://github.com/laude-institute/terminal-bench) |
| 长程真实任务 | 测试 Agent 在短代码或聊天之外的能力。 | [WildClawBench](https://github.com/InternLM/WildClawBench), [OSWorld](https://github.com/xlang-ai/OSWorld), [WebArena](https://github.com/web-arena-x/webarena) |
| 状态冲突任务 | 测试 Agent 是否能处理已有文件、部分完成工作、过期输出和冲突 artifact。 | [ClawForge paper](https://arxiv.org/abs/2605.14133) |
| 过程安全与滥用证据 | 捕捉不安全工具使用、未授权访问和高风险副作用。 | [A3S-Bench paper](https://arxiv.org/abs/2605.22321), [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/) |
| 金融领域 Agent 评测 | 需要公开可复现输入、来源 provenance、拒答行为，并避免投资建议类声明。 | [金融领域 LLM 评测清单](financial-domain-llm-evaluation-checklist.md) |

## 有价值的 Agent 评测数据集应包含什么

- 任务指令和预期用户上下文。
- 环境定义、依赖版本和 fixture 文件。
- 允许与禁止使用的工具。
- Verifier 脚本和 reward details。
- Agent 轨迹日志。
- 证明最终状态的 artifacts。
- 多次运行元数据。
- 相关时的安全或规则违规标注。
- 描述预期用途和局限性的数据集卡或 README。

## 值得关注的指标

| 指标 | 回答什么问题 | 单独使用的风险 |
| --- | --- | --- |
| Mean reward | 平均运行得分如何？ | 隐藏任务级脆弱性。 |
| Task pass rate | 每个任务是否至少成功一次？ | 容易高估可靠性。 |
| Pass@k | 系统是否能在 k 次内完成任务？ | 奖励重试带来的运气。 |
| Pass^k / all-attempts-pass | 系统是否每次重复运行都成功？ | 保守，可能低估探索型 Agent。 |
| Safety pass rate | 过程是否避免了禁止行为？ | 需要清晰的安全 rubric。 |
| Missing-evidence rate | 运行有多少比例没有产出可用证据？ | 常被忽略，但对落地很关键。 |

## 贡献切入点

最有价值的开源贡献不是又一张 leaderboard 截图，而是维护者可以审查的小型可复现模式：

1. 一个 task fixture。
2. 一个 verifier。
3. 一个轨迹感知安全 rubric。
4. 一个多次运行 metric。
5. 一段说明 metric 能证明什么、不能证明什么的短文档。

这也是本仓库新增 [Harbor 多次运行指标示例](../examples/harbor-repeated-trial-metric) 和 Harbor 上游提案 [harbor-framework/harbor#1700](https://github.com/harbor-framework/harbor/issues/1700) 的原因。

## Watchlist

- Harbor docs/cookbook 对轨迹感知评测模式的响应。
- Claw-Eval 后续发布、任务格式和评分 rubric 可见性。
- 新的长程 computer-use 与 command-line Agent benchmark。
- 基于真实轨迹构建的安全 benchmark。
- 过程安全违规和副作用证据的标准 schema。

## 相关内容

- [Claw-style Agent 评测笔记](claw-style-agent-evaluation-notes.zh-CN.md)
- [Harbor、OpenClaw 与 ATIF：面向金融 Agent 的轨迹评测](harbor-openclaw-atif-financial-evaluation.zh-CN.md)
- [Harbor OpenClaw 金融轨迹审计](../examples/harbor-openclaw-finance-trajectory-audit)
- [Harbor 多次运行指标示例](../examples/harbor-repeated-trial-metric)
- [金融领域 LLM 评测清单](financial-domain-llm-evaluation-checklist.md)
- [English version](2026-agent-evaluation-radar.md)
