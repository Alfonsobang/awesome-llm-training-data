# 2026 Agent Evaluation Radar

This radar tracks the agent-evaluation topics that are most likely to matter for LLM data and evaluation teams in 2026. It is intentionally practical: the goal is to help teams decide what to read, what to benchmark, and what evidence to collect.

It does not rank vendors, publish private benchmark results, or claim production readiness.

## The Shift

LLM evaluation is moving from answer-only grading to agent-run evaluation:

- Static QA is not enough for agents that use tools, shells, browsers, files, and subagents.
- The trajectory matters: tool calls, observations, artifacts, side effects, and unsafe intermediate actions can determine whether a run should be trusted.
- Repeated attempts matter: a single successful run may hide brittle behavior.
- Evaluation data must include process evidence, not just final text.

## Hot Topics To Watch

| Topic | Why it matters | Public entry points |
| --- | --- | --- |
| Harbor OpenClaw ATIF trajectories | Makes OpenClaw-style user messages, tool calls, observations, and metadata inspectable as structured evidence. | [Harbor OpenClaw financial ATIF audit](../examples/harbor-openclaw-finance-trajectory-audit), [OpenClaw integration](https://github.com/harbor-framework/harbor/blob/main/src/harbor/agents/installed/openclaw.py) |
| Trajectory-aware grading | Judges the full process, not only final output. | [Claw-Eval](https://github.com/claw-eval/claw-eval), [Harbor ATIF docs](https://harborframework.com/docs/agents/trajectory-format) |
| Repeated-trial robustness | Separates lucky success from consistent behavior. | [Harbor repeated-trial metric example](../examples/harbor-repeated-trial-metric), [Harbor pass@k utility](https://github.com/harbor-framework/harbor/blob/main/src/harbor/utils/pass_at_k.py) |
| Sandboxed agent environments | Makes tool-using agent runs reproducible and inspectable. | [Harbor](https://github.com/harbor-framework/harbor), [Terminal-Bench](https://github.com/laude-institute/terminal-bench) |
| Long-horizon real-world tasks | Tests agents beyond short coding or chat tasks. | [WildClawBench](https://github.com/InternLM/WildClawBench), [OSWorld](https://github.com/xlang-ai/OSWorld), [WebArena](https://github.com/web-arena-x/webarena) |
| State-conflict tasks | Tests whether agents can handle messy existing files, partial work, stale outputs, and conflicting artifacts. | [ClawForge paper](https://arxiv.org/abs/2605.14133) |
| Process safety and misuse evidence | Captures unsafe tool use, unauthorized access, and risky side effects. | [A3S-Bench paper](https://arxiv.org/abs/2605.22321), [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/) |
| Financial-domain agent evaluation | Needs reproducible public inputs, provenance, refusal behavior, and no investment-advice claims. | [Financial-domain LLM Evaluation Checklist](financial-domain-llm-evaluation-checklist.md) |

## What A Useful Agent Eval Dataset Should Contain

- Task instruction and expected user context.
- Environment definition, dependency versions, and fixture files.
- Allowed and forbidden tools.
- Verifier scripts and reward details.
- Agent trajectory logs.
- Artifacts proving final state.
- Repeated-run metadata.
- Safety and policy-violation annotations when relevant.
- Dataset card or README describing intended use and limitations.

## Metrics That Deserve Attention

| Metric | Question answered | Risk if used alone |
| --- | --- | --- |
| Mean reward | How well did runs score on average? | Hides task-level brittleness. |
| Task pass rate | Did each task succeed at least once? | Can overstate reliability. |
| Pass@k | Could the system solve the task within k attempts? | Rewards retry luck. |
| Pass^k / all-attempts-pass | Did the system pass every repeated attempt? | Conservative; may understate exploratory agents. |
| Safety pass rate | Did the process avoid prohibited behavior? | Needs clear safety rubric. |
| Missing-evidence rate | How often did the run fail to produce usable evidence? | Usually ignored, but operationally important. |

## Contribution Wedge

The most useful open-source contribution is not another leaderboard screenshot. It is a small, reproducible pattern that maintainers can review:

1. A task fixture.
2. A verifier.
3. A trajectory-aware safety rubric.
4. A repeated-trial metric.
5. A short write-up explaining what the metric does and does not prove.

This is why this repository now includes a [Harbor repeated-trial metric example](../examples/harbor-repeated-trial-metric) and an upstream Harbor proposal: [harbor-framework/harbor#1700](https://github.com/harbor-framework/harbor/issues/1700).

## Watchlist

- Harbor docs/cookbook response to trajectory-aware evaluation patterns.
- Claw-Eval follow-up releases, task format, and grading rubric visibility.
- New long-horizon computer-use and command-line agent benchmarks.
- Security benchmarks built from real trajectories.
- Standard schemas for process-safety violations and side-effect evidence.

## Related

- [Claw-style Agent Evaluation Notes](claw-style-agent-evaluation-notes.md)
- [Harbor, OpenClaw, and ATIF for Financial Agent Evaluation](harbor-openclaw-atif-financial-evaluation.md)
- [Harbor OpenClaw Financial Trajectory Audit](../examples/harbor-openclaw-finance-trajectory-audit)
- [Harbor Repeated-trial Metric Example](../examples/harbor-repeated-trial-metric)
- [Financial-domain LLM Evaluation Checklist](financial-domain-llm-evaluation-checklist.md)
- [中文版本](2026-agent-evaluation-radar.zh-CN.md)
