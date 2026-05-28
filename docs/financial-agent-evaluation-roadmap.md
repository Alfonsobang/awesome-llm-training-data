# Financial Agent Evaluation Roadmap

This roadmap turns the financial agent evaluation seed into a public, reproducible track for evaluating agents that search, retrieve, calculate, backtest, forecast, and respect compliance boundaries.

The goal is not to build a trading leaderboard. The goal is to make financial-agent evaluation more auditable: public inputs, explicit cutoffs, deterministic verifiers where possible, trajectory evidence, and clear safety boundaries.

## Positioning

Financial agent evaluation should answer five questions:

1. Can the agent find the right public source?
2. Can it extract and calculate exact values without inventing data?
3. Can it use tools and recover from missing fields or failed calls?
4. Can it keep temporal boundaries in backtesting and forecasting tasks?
5. Can it refuse unsafe financial requests while still offering useful analysis boundaries?

## 30-day Plan

- Expand the seed from 5 task specs to 10 public-data-only task specs.
- Add one Harbor-style template for each priority family: filing QA, exact lookup, toy backtest, and compliance refusal.
- Add deterministic verifiers for numeric fields, required citations, missing evidence, and disallowed financial claims.
- Add a task-card table showing required artifacts, allowed tools, safety boundaries, and verifier type.

## 60-day Plan

- Add repeated-trial reporting examples for pass@k, Pass^k, missing-evidence rate, and cutoff-violation rate.
- Add a small synthetic fixture pack for filings, prices, economic series, and tool-call traces.
- Add a benchmark card template with license, data provenance, leakage risks, known limitations, and intended use.
- Open targeted upstream discussions with Harbor and finance-evaluation projects when the examples are mature enough to be useful.

## 90-day Plan

- Publish a minimal `financial-agent-eval` task pack with 20-30 public or synthetic tasks.
- Provide adapters for Harbor-style tasks and plain JSON task specs.
- Add a reproducible evaluation report format for trajectory evidence, verifier outputs, and safety incidents.
- Invite review from agent-evaluation, financial-data, and data-governance practitioners.

## Priority Task Families

| Family | First useful artifact | Verifier style |
| --- | --- | --- |
| Public filing search | Locate a public filing and cite exact sections. | Source URL and section checks. |
| Exact data lookup | Extract revenue, income, shares, rates, or dates. | Exact or tolerance-based checks. |
| Filing-grounded explanation | Explain a financial change from cited excerpts. | Numeric checks plus citation checks. |
| Toy backtesting | Run a fixed-rule simulation on synthetic or public data. | Deterministic code and cutoff checks. |
| Forecasting / pastcasting | Produce a bounded forecast using only pre-cutoff evidence. | Cutoff and uncertainty checks. |
| Financial tool use | Choose quote, fundamentals, filing, or macro tools in the right order. | Tool-call trace checks. |
| Compliance refusal | Refuse guaranteed-return, insider, or manipulation requests. | Safety phrase and alternative-help checks. |

## Public Safety Rules

- No private company data.
- No real user data.
- No proprietary workflows.
- No investment advice or trading signals.
- No claims that a benchmark proves production readiness.
- Use synthetic data whenever licensing, privacy, or market-data terms are unclear.

## Near-term Issues To Open

- Add Harbor-style exact-data-lookup task template.
- Add toy backtest task with deterministic cutoff verifier.
- Add compliance-refusal task template for guaranteed-return requests.
- Add synthetic financial fixture pack and fixture policy.
- Add repeated-trial report example for financial agent tasks.
