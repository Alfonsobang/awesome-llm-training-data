# 金融 Agent 评测多赛道地图

这个页面把仓库从单一 Awesome List 转成一个多赛道的金融 Agent 评测项目组合。

核心仍然是可运行的 [Financial Agent Eval Seed](../examples/financial-agent-eval-seed)。周边页面服务不同人群：Agent 评测工程师、金融 RAG 团队、数据治理负责人、标注与偏好数据团队，以及 Agent 框架维护者。

## 为什么需要多赛道

金融 AI 评测不是一道题，也不是一个榜单。真实系统会同时涉及搜索、查数、引用、计算、预测、工具调用、拒答边界、数据治理和人工复核。一个可信的开源项目应该把这些问题拆成多个清晰入口，让贡献者可以先改进其中一个模块，而不是一上来理解整个体系。

## 赛道

| 赛道 | 适合读者 | 应产出的东西 | 当前入口 |
| --- | --- | --- | --- |
| 金融搜索与查数 | RAG 工程师、Agent 工程师 | 来源选择任务、精确字段查数、引用支撑检查。 | [Search and Lookup Evaluation Playbook](financial-search-and-lookup-evaluation-playbook.md) |
| 金融计算与回测 | 评测工程师、量化相关开发者 | 可复现 toy backtest、回撤和波动率检查、假设审查。 | [Backtesting Evaluation Playbook](financial-backtesting-evaluation-playbook.md) |
| 预测与时间边界 | 预测任务设计者、Benchmark 设计者 | 截止日期约束、未来数据泄漏检查、不确定性表达。 | [Forecasting Evaluation Playbook](financial-forecasting-evaluation-playbook.md) |
| 工具调用与轨迹评测 | Agent 框架维护者 | 工具顺序、观测结果引用、失败调用恢复、多次运行稳定性。 | [Tool-use Evaluation Playbook](financial-tool-use-evaluation-playbook.md) |
| 治理与 Benchmark Card | 数据负责人、合规审查者 | 来源清单、再分发边界、泄漏风险审查、benchmark card。 | [Benchmark Card Template](financial-benchmark-card-template.md) |
| 标注与偏好质量 | 标注负责人、奖励数据团队 | 多维度复核记录、仲裁触发条件、偏好数据质量检查。 | [Annotation and Preference Quality for Finance](annotation-preference-quality-finance.md) |

## 当前可运行覆盖

种子项目目前覆盖：

- 公开来源搜索。
- 精确数据查找。
- 财报引用检查。
- 基于财报证据的解释。
- Toy backtesting。
- 预测截止日期检查。
- 风险计算。
- 金融工具调用轨迹。
- 合规拒答。

运行方式：

```bash
python examples/financial-agent-eval-seed/run_finance_eval.py
```

## 什么样的赛道值得继续扩展

一个赛道值得继续投入，至少要能产出：

- 公开安全的任务规格。
- 可见 fixture 或公开来源引用。
- 一个通过的参考答案。
- 一个能以清楚原因失败的反例。
- 确定性的 verifier 或 schema。
- 一个不运行代码也能阅读的简短报告。

## 贡献方向

好的贡献应该窄、具体、可验证：

- 增加一个新任务家族。
- 给现有任务增加一个失败样例。
- 增加一个能抓住真实金融错误的 verifier 检查。
- 增加一个改进来源、泄漏或安全审查的 benchmark-card 字段。
- 增加一条让公开示例更可复现的数据治理规则。

不要加入泛泛的 AI 趋势评论、私有数据、不可验证说法、生产可用性暗示或投资建议式内容。

