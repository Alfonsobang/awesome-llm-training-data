# Harbor, OpenClaw, and ATIF for Financial Agent Evaluation

Harbor's current main branch includes an installed `openclaw` agent integration and ATIF-v1.7 trajectory generation. For financial agent evaluation, this creates a useful foundation: the evaluation can inspect not only the final answer, but also the user instruction, tool calls, observations, source metadata, time boundaries, and safety-relevant actions.

Source references:

- [Harbor repository](https://github.com/harbor-framework/harbor)
- [OpenClaw installed agent integration](https://github.com/harbor-framework/harbor/blob/main/src/harbor/agents/installed/openclaw.py)
- [ATIF RFC 0001](https://github.com/harbor-framework/harbor/blob/main/rfcs/0001-trajectory-format.md)
- [OpenClaw integration PR #1661](https://github.com/harbor-framework/harbor/pull/1661)

This note was checked against Harbor main commit [`eecd142`](https://github.com/harbor-framework/harbor/commit/eecd142) on May 31, 2026. Harbor is moving quickly, so confirm current behavior before relying on implementation details.

## Why ATIF Matters In Finance

A financial-agent run may look correct while still being untrustworthy. Examples:

- the answer cites no source,
- a tool call retrieves data after the evaluation cutoff,
- a backtest silently uses future rows,
- an observation cannot be linked to its originating tool call,
- the agent invokes a private-data or order-placement tool,
- the final response blurs analysis and investment advice.

ATIF makes these process questions inspectable because it records a structured sequence of steps, tool calls, observations, and metadata.

## Suggested Financial Audit Profile

| Check | Why it matters |
| --- | --- |
| Retained user instruction | Confirms that the trace includes the actual task boundary. |
| Sequential steps | Keeps the audit trail reconstructable. |
| Tool-call / observation linkage | Makes it possible to attribute evidence and failures to actions. |
| Source document metadata | Distinguishes grounded retrieval from unsupported claims. |
| Evaluation cutoff | Detects time leakage in forecasting, retrieval, and backtesting tasks. |
| Prohibited tool calls | Prevents evaluation tasks from normalizing trading execution or private-data lookup. |
| Non-advice boundary | Keeps analytical examples distinct from personalized financial advice. |
| Copied-context count | Helps separate retained context from new interactions when trajectories are used for training-data analysis. |
| Non-LLM dispatch count | Makes deterministic orchestration visible in ATIF-v1.7-style traces. |

## Public Example

The [Harbor OpenClaw Financial Trajectory Audit](../examples/harbor-openclaw-finance-trajectory-audit) includes:

- a synthetic OpenClaw-style ATIF-v1.7 trajectory,
- a zero-dependency audit script,
- deterministic tests for time leakage, prohibited tools, missing source metadata, and missing non-advice framing.
- a repeated-trial aggregation example for pass rate, pass@k, Pass^k, missing evidence, cutoff violations, and prohibited tool calls.

## What This Does Not Claim

- It is not an official Harbor profile.
- It does not replace Harbor's ATIF schema validator.
- It does not evaluate real trading systems.
- It does not prove that an agent is ready for regulated production use.
