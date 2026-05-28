# Financial Agent Evaluation Share Kit

Short, practical copy for introducing the financial agent evaluation track in a restrained way.

## Short English Post

I am expanding `awesome-llm-training-data` with a finance-focused agent evaluation track.

The direction is not a trading leaderboard. It is about auditable financial-agent tasks: public filing search, exact data lookup, filing-grounded explanation, toy backtesting, forecasting cutoffs, tool-use traces, and compliance-boundary refusal.

Initial artifacts:

- Financial Agent Evaluation Agenda
- Financial Agent Evaluation Roadmap
- Public-data-only task specs
- Harbor-style filing task template with synthetic fixture data and deterministic verifier tests

The design principle is simple: no private data, no real user data, no investment advice, and no production-readiness claims. The useful benchmark is the one that leaves enough evidence for another evaluator to understand what happened.

Repo: https://github.com/Alfonsobang/awesome-llm-training-data

## 中文短帖

我正在把 `awesome-llm-training-data` 扩展成一个更聚焦的金融 Agent 评测方向。

这个方向不是交易策略排行榜，也不是投资建议评测，而是关注可审计的金融 Agent 任务：公开报表搜索、精确查数、基于报表证据的解释、玩具回测、预测任务的时间截点、工具调用轨迹，以及合规边界拒答。

目前已经补了几类初始 artifact：

- 金融 Agent 评测课题框架
- 金融 Agent 评测路线图
- 公开数据任务规格
- Harbor 风格金融报表任务模板，包含合成 fixture 和确定性 verifier tests

基本原则很清楚：不使用私有数据，不使用真实用户数据，不提供投资建议，不声称生产可用。真正有价值的金融 Agent benchmark，应该能留下足够证据，让另一个评测者看懂任务是怎么完成或失败的。

Repo: https://github.com/Alfonsobang/awesome-llm-training-data

## Discussion Prompt

What should a serious financial agent benchmark measure beyond final-answer correctness?

Useful dimensions I am starting with:

- source grounding,
- numeric correctness,
- temporal cutoff integrity,
- tool-use recovery,
- missing-evidence rate,
- compliance-boundary handling,
- repeated-trial stability.

## Pinned Issue Draft

Title: Build a public financial agent evaluation task pack

Body:

This issue tracks the next stage of the financial agent evaluation track.

Planned work:

- Add Harbor-style exact-data-lookup task template.
- Add toy backtest task with deterministic cutoff verifier.
- Add compliance-refusal task template for guaranteed-return requests.
- Add synthetic financial fixture pack and fixture policy.
- Add repeated-trial report example for financial agent tasks.

Safety boundary:

- No private company data.
- No real user data.
- No investment advice or trading signals.
- No proprietary workflows.
- No claims that the benchmark proves production readiness.
