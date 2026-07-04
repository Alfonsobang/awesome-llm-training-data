# Financial Backtesting Evaluation Playbook

Backtesting tasks attract attention because they look close to real financial work. They also create risk when examples hide look-ahead bias, data-snooping, ungoverned assumptions, or advice-like framing.

This playbook keeps backtesting evaluation small, deterministic, and public-safe.

## Scope

Use this track for toy simulations and calculation tasks where the goal is to test process discipline, not market performance.

Good tasks check:

- Fixed rules.
- Frozen data windows.
- Explicit assumptions.
- Transaction-cost handling when relevant.
- Metric calculation.
- Non-advice language.

## Useful Task Types

| Task type | What it tests | Required evidence | Main verifier checks |
| --- | --- | --- | --- |
| Moving-average toy backtest | Rule implementation and cutoff discipline. | Input rows, signal dates, trades, metrics. | Expected trades, no future data, metric values. |
| Drawdown calculation | Risk metric math and window discipline. | Peak date, trough date, drawdown value, formula notes. | Sign, window, peak/trough, sample/population convention. |
| Transaction-cost sensitivity | Assumption transparency. | Cost assumptions, before/after metrics. | Cost applied consistently, no hidden tuning. |
| Benchmark baseline comparison | Honest comparison against a simple baseline. | Baseline rule, metrics, limitations. | Same data window, same cost model, no advice framing. |

## Current Repo Assets

- [Toy backtest moving-average task](../examples/financial-agent-eval-seed/harbor-template/toy-backtest-moving-average).
- [Risk calculation drawdown task](../examples/financial-agent-eval-seed/harbor-template/risk-calculation-drawdown).
- [Bad-candidate report](../examples/financial-agent-eval-seed/results/bad-finance-agent-report.md).

## Quality Bar

Backtesting examples should be visibly educational and reproducible.

Require:

- A fixed rule before the run starts.
- A visible data window.
- Explicit metric definitions.
- A limitation statement.
- A non-advice boundary.

Reject:

- Claims that toy performance implies investment value.
- Hidden parameter search.
- Current trading signals.
- Private portfolio data.
- Tasks that cannot be reproduced from the included fixture or public source.

## Common Failure Modes

- Look-ahead bias from using future rows to form past decisions.
- Split, dividend, or scale errors when using public historical data.
- Confusing arithmetic and log returns.
- Reporting positive performance without costs or limitations.
- Treating a synthetic fixture as market evidence.

## Reviewer Questions

- Would the same answer be produced on another machine?
- Is the rule fixed before seeing the output?
- Are the assumptions visible enough to audit?
- Does the answer avoid advice and production-readiness claims?
- Is the known-bad answer realistic enough to teach users what the verifier catches?

