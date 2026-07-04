# 金融 Agent 评测项目组合

这个项目不应该只押一个页面、一个 benchmark 想法，或一个上游框架。更稳的路线，是围绕同一个金融 Agent 评测主线，拆出多个可以被不同人群独立复用的公开安全 artifact。

## 核心判断

金融 Agent 评测横跨轨迹评测、RAG 引用支撑、数值校验、强监管领域安全边界、benchmark 打包和数据治理。一个真正有用的开源项目，应该让这些入口都清晰可见。

主锚点仍然是可运行的 [Financial Agent Eval Seed](../examples/financial-agent-eval-seed/README.md)，但仓库应该同时服务几类读者：

| 入口 | 主要读者 | 60 秒内应该获得什么 | 当前资产 |
| --- | --- | --- | --- |
| 可运行种子集 | Agent 评测工程师 | 本地 runner、确定性 verifier、已知坏样例报告 | [Financial Agent Eval Seed](../examples/financial-agent-eval-seed/README.md) |
| 任务设计 | benchmark 构建者 | 金融任务家族和失败模式 | [Task Zoo](financial-agent-evaluation-task-zoo.md) |
| 评测治理 | 数据负责人和评审者 | 来源策略、合成数据边界、benchmark card 检查 | [Benchmark Card](../examples/financial-agent-eval-seed/benchmark-card.yml) |
| Harbor/OpenCLAW 对齐 | 框架维护者 | task-pack 形态、manifest、多次运行报告 | [Harbor Task Pack Blueprint](harbor-finance-task-pack-blueprint.md) |
| 模型/团队评审 | 应用团队 | 保守的金融 Agent 评测 scorecard | [Scorecard](financial-agent-evaluation-scorecard.md) |
| 对外定位 | 读者和潜在贡献者 | 为什么这个项目值得存在、下一步做什么 | [Opportunity Map](financial-agent-evaluation-opportunity-map.md) |

## 为什么这样更有吸引力

用户给仓库 star 的理由并不相同：有人要可运行代码，有人要清晰 checklist，有人要能迁移的 benchmark 示例，也有人只想快速理解一个热门方向。

这个仓库应该同时满足这些需求，但不声称自己是 leaderboard、官方 Harbor adapter、投资工具或生产系统。

## 当前下注方向

| 方向 | 为什么可能成立 | 还需要加强什么 |
| --- | --- | --- |
| 金融搜索与查数 | 常见 Agent 工作流，容易解释，也容易验证 | 更多公开来源 fixture 和引用边界案例 |
| 金融 RAG 引用支撑 | 金融 QA 中非常常见的失败面 | 更多抽取、表格和计算检查 |
| 预测 cutoff 检查 | 直接打到未来数据泄漏问题 | 更多 pastcasting 样例和时间元数据 |
| 工具调用轨迹 | 与 Harbor 风格 rollout 证据天然相关 | 可导出的 task-pack 格式和多次运行样例 |
| 金融偏好数据 | 把评测和标注/反馈质量连接起来 | 更多样例 review 和仲裁案例 |
| 治理优先的 benchmark card | 对强监管领域团队更可信 | 为每个任务家族增加 CI 校验 |

## 公开安全边界

- 不使用私有公司数据。
- 不使用真实用户数据。
- 不发布专有流程。
- 不提供投资建议。
- 不提供交易信号。
- 不声称生产可用。
- 除非上游维护者明确确认，否则不声称官方 Harbor 支持。

## 近期扩展方向

1. 每次新增页面都尽量转成 fixture、verifier、schema、report 或 issue。
2. 增加两个 scorecard 示例：一个通过样例，一个已知坏样例。
3. 增加一个从评测报告生成 scorecard 摘要的小脚本。
4. Harbor/OpenCLAW 相关工作只描述兼容任务设计，不冒充官方集成。
5. 保持 GitHub 仓库描述和 topics 与金融 Agent 评测主线一致。
