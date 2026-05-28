# Launch and Share Kit

This page exists for distribution. A good repository needs useful content, but growth also needs a clear message that people can understand and reshare quickly.

## One-line Positioning

A practical, bilingual resource hub for LLM data quality and 2026 agent evaluation: training data, preference data, governance, Harbor workflows, Claw-style trajectory grading, and repeated-trial metrics.

## Short Post

I am maintaining a public resource hub for LLM data quality and agent evaluation.

The 2026 shift I care about: agent evaluation is moving from final-answer grading to trajectory-aware evidence: repeated attempts, verifier outputs, artifacts, process safety, and auditable traces.

New additions:

- 2026 Agent Evaluation Radar
- Claw-style Agent Evaluation Notes
- Harbor repeated-trial `metric.py` example
- Bilingual English / Chinese documentation

Repo: https://github.com/Alfonsobang/awesome-llm-training-data

## Technical Post

Agent benchmarks are getting more serious. For tool-using agents, final-output grading is no longer enough.

A credible eval should ask:

- Did the agent complete the task?
- Did the trajectory show unsafe or unauthorized actions?
- Did the run produce verifier evidence and artifacts?
- Does success repeat across attempts?
- Are missing rewards or malformed traces counted?

I wrote a small Harbor-style repeated-trial metric example that reports mean reward, task pass rate, pass@k, Pass^k / all-attempts-pass, and missing-reward rate.

Example: https://github.com/Alfonsobang/awesome-llm-training-data/tree/main/examples/harbor-repeated-trial-metric

Full radar: https://github.com/Alfonsobang/awesome-llm-training-data/blob/main/docs/2026-agent-evaluation-radar.md

## Chinese Post

我在维护一个面向 LLM 数据质量和 Agent 评测的公开资源库。

我现在重点关注 2026 年的一个变化：Agent 评测正在从“只看最终答案”转向“轨迹感知证据”。

也就是要看：

- 是否完成任务；
- 过程里是否有不安全或未授权动作；
- 是否有 verifier 输出和 artifact；
- 多次运行是否稳定；
- 缺失 reward 或异常 trace 是否被计入。

新加了几块内容：

- 2026 Agent Evaluation Radar
- Claw-style Agent 评测笔记
- Harbor 多次运行 `metric.py` 示例
- 中英文双语文档

Repo: https://github.com/Alfonsobang/awesome-llm-training-data

## Places To Share

- GitHub profile README.
- Harbor issue thread when relevant.
- LinkedIn post with the technical framing.
- X thread with the short post and repo link.
- Chinese technical communities focused on LLM evaluation, agent systems, and data governance.
- GitHub Discussions or issue threads using [Discussion Seed: What Should Agent Evaluation Measure In 2026?](discussion-seed-agent-evaluation.md)

Do not spam maintainers or unrelated projects. Share only where the audience cares about agent evaluation, benchmark design, data quality, or governance.

## Reply Template

Thanks for checking it out. The repo is intentionally focused on practical data and evaluation work rather than a broad AI link dump. The current focus is Claw-style / trajectory-aware agent evaluation and Harbor-style repeated-trial metrics. Feedback on missing benchmarks, unclear quality criteria, or better reproducible examples is very welcome.
