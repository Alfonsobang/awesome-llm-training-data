# Financial Agent Evaluation Agenda

This agenda defines a large, public, finance-focused evaluation track for LLM agents. The goal is to evaluate complex financial workflows without publishing private company data, real user data, trading signals, or investment advice.

The central question:

> Can an agent search, retrieve, calculate, backtest, forecast, explain uncertainty, respect compliance boundaries, and leave auditable evidence?

## Scope

This track focuses on public-data, reproducible financial-agent evaluation tasks:

- financial search and source selection,
- structured data lookup,
- filing and statement extraction,
- backtesting and strategy simulation,
- forecasting and pastcasting,
- event and news interpretation,
- portfolio/risk calculation,
- compliance-aware refusal and boundary handling,
- evidence-grounded reporting.

It does not evaluate real-money trading, private portfolios, customer accounts, internal research, investment recommendations, or production readiness.

## Task Families

| Family | What the agent does | Example public-data task | Primary evidence |
| --- | --- | --- | --- |
| Financial search | Finds relevant filings, disclosures, news, or market data sources. | Locate the latest annual report and identify revenue segment tables. | Source URLs, retrieval trace, citation quality. |
| Data lookup | Retrieves exact values from public structured or semi-structured sources. | Find a company's fiscal-year revenue, net income, and shares outstanding. | Extracted values, source fields, timestamp. |
| Filing QA | Answers questions grounded in 10-K, 10-Q, annual report, prospectus, or earnings materials. | Explain why operating margin changed year over year from cited filings. | Cited passages, calculations, refusal on unsupported claims. |
| Backtesting | Implements a simple, public, historical simulation with fixed rules. | Backtest a moving-average strategy on public adjusted close prices. | Code, data window, assumptions, metrics, no trading advice. |
| Forecasting / pastcasting | Makes a time-bounded forecast or reconstructs a past forecast from historical information. | Forecast next-quarter revenue using only data available before a cutoff date. | Cutoff enforcement, feature trace, uncertainty statement. |
| Risk calculation | Computes volatility, drawdown, factor exposure, VaR-style toy metrics, or stress scenarios. | Calculate maximum drawdown for a public asset over a fixed period. | Formula, data source, reproducible notebook or script. |
| Tool-use reliability | Chooses and calls financial tools correctly. | Use a quote, fundamentals, and filings API in the right order. | Tool-call trajectory, errors, recovery behavior. |
| Compliance boundary | Refuses or reframes unsafe requests. | User asks for guaranteed trade advice or insider-like inference. | Refusal quality, safe alternative, policy rationale. |
| Evidence report | Produces an audit-friendly answer. | Create a short analyst-style note from public sources. | Citations, assumptions, limitations, calculation appendix. |

## Evaluation Dimensions

### 1. Completion

- Did the agent answer the task?
- Were required fields, calculations, or files produced?
- Did the final answer match the verifier or reference evidence?

### 2. Source Grounding

- Are all material claims tied to public sources?
- Are source dates, report periods, and retrieval timestamps visible?
- Does the agent avoid citing irrelevant or stale material?

### 3. Numeric Correctness

- Are formulas correct?
- Are units, currencies, split adjustments, and time windows handled?
- Are rounding and missing values documented?

### 4. Temporal Integrity

- Does a forecasting or backtesting task enforce the information cutoff?
- Does the agent avoid look-ahead bias?
- Are training, validation, and test windows separated?

### 5. Tool-use Process

- Did the agent choose appropriate tools?
- Did it recover from failed calls or missing fields?
- Did it over-call tools, hallucinate tool outputs, or ignore returned data?

### 6. Safety and Compliance

- Does the agent avoid investment advice, guarantees, and unsupported recommendations?
- Does it distinguish analysis from advice?
- Does it refuse private-data, insider-information, or market-manipulation requests?

### 7. Robustness

- Does performance repeat across attempts?
- Does the agent remain stable under minor prompt variation?
- Are missing rewards, malformed artifacts, and failed tool traces counted?

## Suggested Metrics

| Metric | Purpose |
| --- | --- |
| Completion rate | Share of tasks with successful final outputs. |
| Source-grounded rate | Share of material claims with valid citations. |
| Numeric accuracy | Exact or tolerance-based score for calculations. |
| Cutoff violation rate | Share of forecasting/backtesting runs that leak future data. |
| Tool success rate | Share of required tool calls completed with valid outputs. |
| Process-safety pass rate | Share of runs without prohibited actions. |
| Pass@k | Whether the agent can solve a task within k attempts. |
| Pass^k / all-attempts-pass | Whether the agent solves the task consistently across attempts. |
| Missing-evidence rate | Share of runs without usable trajectory, artifact, or verifier evidence. |

## Public Data Sources To Prefer

- SEC EDGAR filings and company annual reports.
- Exchange or regulator public disclosures.
- Open benchmark datasets with clear licenses.
- Public market data sources suitable for examples and toy evaluations.
- Public economic time series where terms allow use.
- Synthetic tasks with clearly labeled synthetic data.

Avoid private market feeds, customer account data, internal reports, scraped paywalled content, and unverifiable social-media rumors.

## Benchmark Design Principles

- Separate retrieval, calculation, and judgment.
- Keep time cutoffs explicit for forecasting and backtesting.
- Use deterministic verifiers where possible.
- Use LLM or agent judges only for clearly scoped qualitative criteria.
- Store trajectories and artifacts as first-class evidence.
- Report missing evidence instead of silently dropping failed runs.
- Never present toy backtests as investment recommendations.

## Example Task Spec

```yaml
task_id: public-filing-margin-qa-001
family: filing_qa
instruction: >
  Using only the provided public annual reports, explain the year-over-year
  change in operating margin. Cite the exact source passages and show the
  margin calculation.
allowed_sources:
  - public annual report PDFs
prohibited:
  - investment recommendation
  - future stock-price prediction
  - uncited financial claims
required_evidence:
  - source citations
  - calculation table
  - agent trajectory
  - verifier output
metrics:
  - completion
  - source_grounding
  - numeric_correctness
  - compliance_boundary
```

## Roadmap

1. Build task cards for the nine task families.
2. Add a public-data-only dataset card template.
3. Add Harbor-compatible examples for repeated-trial metrics.
4. Add a trajectory-aware financial compliance rubric.
5. Draft a minimal public benchmark seed with 10-20 tasks.
6. Invite feedback from agent-evaluation and financial-data practitioners.

Initial seed work is available in [Financial Agent Evaluation Seed](../examples/financial-agent-eval-seed).

## Related Resources

- [Financial-domain LLM Evaluation Checklist](financial-domain-llm-evaluation-checklist.md)
- [2026 Agent Evaluation Radar](2026-agent-evaluation-radar.md)
- [Claw-style Agent Evaluation Notes](claw-style-agent-evaluation-notes.md)
- [Harbor repeated-trial metric example](../examples/harbor-repeated-trial-metric)
- [Financial Agent Evaluation Seed](../examples/financial-agent-eval-seed)
- [中文版本](financial-agent-evaluation-agenda.zh-CN.md)
