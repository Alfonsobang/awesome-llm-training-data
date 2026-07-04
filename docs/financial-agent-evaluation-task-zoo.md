# Financial Agent Evaluation Task Zoo

This page turns the broad financial-agent evaluation idea into concrete task families. The goal is to make the repo useful even for readers who only want one task pattern.

The task zoo avoids trading signals, private portfolios, private company workflows, and live market recommendations. Tasks should use public sources, synthetic fixtures, or clearly labeled toy data.

## Implemented Task Families

| Task family | What it tests | Strong verifier signal | Current asset |
| --- | --- | --- | --- |
| Public-source search | whether the agent selects the right public source before answering | selected source, period, source type, citation evidence | [public-source-search](../examples/financial-agent-eval-seed/harbor-template/public-source-search/README.md) |
| Filing citation check | whether citations actually support the answer | cited section IDs, quote support, unsupported-claim rejection | [filing-citation-check](../examples/financial-agent-eval-seed/harbor-template/filing-citation-check/README.md) |
| Forecasting cutoff check | whether the agent leaks post-cutoff evidence | cutoff date, pre-cutoff fields, prohibited evidence | [forecasting-cutoff-check](../examples/financial-agent-eval-seed/harbor-template/forecasting-cutoff-check/README.md) |
| Financial tool-use trace | whether tool calls are ordered and grounded in observations | required tool order, observation linkage, missing evidence | [financial-tool-use-trace](../examples/financial-agent-eval-seed/harbor-template/financial-tool-use-trace/README.md) |
| Risk calculation | whether deterministic finance math is correct | drawdown, volatility, window, unit checks | [risk-calculation-drawdown](../examples/financial-agent-eval-seed/harbor-template/risk-calculation-drawdown/README.md) |
| Toy backtesting discipline | whether the agent states assumptions and avoids overclaiming | lookback window, drawdown, non-advice language | [toy-backtest-moving-average](../examples/financial-agent-eval-seed/harbor-template/toy-backtest-moving-average/README.md) |
| Portfolio boundary refusal | whether the agent refuses personalized advice safely | refusal, educational alternative, no private-data request | [portfolio-boundary-refusal](../examples/financial-agent-eval-seed/harbor-template/portfolio-boundary-refusal/README.md) |

## High-Value Next Task Families

| Task family | Why it matters | Public-safe fixture idea | Suggested artifact |
| --- | --- | --- | --- |
| Multi-document financial lookup | agents often mix periods, issuers, or document types | synthetic filing snippets with issuer, period, and table metadata | `multi-document-lookup/` |
| Table-text reconciliation | finance answers often require reconciling a table value with narrative text | synthetic annual-report table and matching management discussion excerpt | `table-text-reconciliation/` |
| Earnings-call claim grounding | agents may cite a call transcript without supporting the exact claim | public transcript excerpts or synthetic transcript sections | `earnings-call-grounding/` |
| Corporate-action adjustment | split/dividend adjustments are easy to mishandle | synthetic price series with explicit corporate action | `corporate-action-adjustment/` |
| News-to-filing conflict handling | agents should prefer primary filings over stale secondary summaries | synthetic news item plus later filing correction | `source-conflict-resolution/` |
| Regulatory boundary classification | finance assistants need different behavior for education, analysis, and advice | synthetic user requests across boundary types | `regulatory-boundary-classification/` |
| Data freshness disclosure | agents should disclose stale or unavailable data instead of guessing | fixed as-of date with unavailable current field | `data-freshness-disclosure/` |
| Benchmark-card completeness | benchmark artifacts need visible provenance and limits | task metadata with missing fields | `benchmark-card-completeness/` |

## Verifier Principles

- Prefer deterministic checks over judge-only scoring.
- Check evidence before fluency.
- Check dates, units, periods, and source identity explicitly.
- Include one known-bad candidate for every task family.
- Report repeated-trial stability when tool trajectories are involved.
- Keep safety checks separate from answer correctness when possible.

## References

- [Harbor](https://github.com/harbor-framework/harbor) describes itself as a framework for evaluating and optimizing agents and language models, including benchmark and environment sharing.
- [Terminal-Bench](https://github.com/harbor-framework/terminal-bench) is a visible example of hard, environment-based agent evaluation.
- [Finance Agent Benchmark](https://arxiv.org/abs/2508.00828), [FinAgentBench](https://arxiv.org/abs/2508.14052), and [FinMCP-Bench](https://arxiv.org/abs/2603.24943) are useful external reference points for finance-agent task design.
