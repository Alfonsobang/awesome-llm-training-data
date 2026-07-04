# 公开发布说明

我正在把 `awesome-llm-training-data` 推进成一个公开安全、可复用的金融 Agent 评测方向。

这个方向的起点很简单：金融 Agent 可能给出看似合理的最终答案，但仍然在静态 Q&A 基准难以覆盖的地方失败。它可能选错来源、混淆单位、给出没有证据支撑的引用、在回测中泄漏未来数据、忽略失败的工具调用，或者滑向不安全的投资建议。

这个仓库把这些问题当作数据工程和评测工程问题来处理。

## 当前已经可运行的内容

当前 seed 包含公开安全的任务规格、合成 fixture、Harbor 风格任务模板、确定性 verifier、数据来源治理元数据和自动生成的报告。

可以从这里开始：

```bash
python examples/financial-agent-eval-seed/run_finance_eval.py
```

参考答案套件会通过当前所有任务，已知坏样例会失败。这个对比是有意设计的：在扩大 benchmark 之前，先把失败变得可见、可复现、可审计。

## 当前几条线

- [金融 Agent 评测任务矩阵](financial-agent-evaluation-task-matrix.md)：覆盖搜索、查数、公告问答、回测、预测、工具调用、拒答、偏好评审和治理。
- [金融 Agent 失败案例库](financial-agent-failure-gallery.md)：把常见失败模式转成可以测试的问题。
- [金融 RAG 评测手册](financial-rag-evaluation-playbook.md)：面向检索、引用、抽取、计算和拒答边界的检查项。
- [金融数据治理控制面](financial-data-governance-control-plane.md)：来源 manifest、打包策略、cutoff 控制与再分发边界。
- [Harbor 金融 task pack 蓝图](harbor-finance-task-pack-blueprint.md)：把金融任务沉淀为 Harbor 风格任务包的路线。
- [金融偏好评审 Schema](../schemas/finance-preference-review.schema.json)：面向金融偏好数据和人工反馈的多维评审结构。

## 这个项目不做什么

- 不是交易排行榜。
- 不是投资建议。
- 不声称可以证明生产可用。
- 不包含私有公司数据、真实用户数据或专有流程。
- 不是泛泛的 AI 链接收藏夹。

## 希望获得的反馈

- 哪些金融 Agent 任务家族最值得优先做成可运行样例？
- 严肃的金融 Agent benchmark 除了最终答案，还应该要求哪些证据？
- 多次运行的稳定性应该如何报告？
- 数据来源治理规则应该严格到什么程度，才既安全又不妨碍公开复用？
- Harbor 风格任务打包在哪些地方能帮助更多 Agent 评测团队复用？

## 简短分享文案

我正在 `awesome-llm-training-data` 中建设一个公开安全的金融 Agent 评测方向。

它关注静态金融 QA 常常覆盖不到的失败：错来源、错单位、无支撑引用、cutoff 泄漏、不稳定工具轨迹，以及不安全投资建议边界。

仓库目前已经包含可运行 seed 任务、合成 fixture、确定性 verifier、Harbor 风格任务模板、来源治理报告和金融偏好评审 schema。

Repo: https://github.com/Alfonsobang/awesome-llm-training-data
