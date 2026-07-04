# Financial Agent Evaluation Track Map

This page turns the repository into a multi-track evaluation portfolio instead of a single Awesome list.

The anchor remains the runnable [Financial Agent Eval Seed](../examples/financial-agent-eval-seed). The surrounding tracks make the work useful to different audiences: agent benchmark builders, finance RAG teams, data-governance reviewers, annotation leads, and agent-framework maintainers.

## Why A Multi-Track Shape

Financial AI evaluation is not one benchmark. Real systems combine search, lookup, extraction, calculation, forecasting, tool use, refusal boundaries, source governance, and human review. A credible public project should expose those surfaces separately so contributors can improve one piece without understanding the whole system first.

## Tracks

| Track | Who it helps | What it should produce | Current entry point |
| --- | --- | --- | --- |
| Financial search and lookup | RAG engineers, agent engineers | Source-selection tasks, exact-value lookup checks, citation support checks. | [Search and Lookup Evaluation Playbook](financial-search-and-lookup-evaluation-playbook.md) |
| Financial calculation and backtesting | Evaluation engineers, quant-adjacent builders | Reproducible toy backtests, drawdown and volatility checks, assumption review. | [Backtesting Evaluation Playbook](financial-backtesting-evaluation-playbook.md) |
| Forecasting and temporal integrity | Forecasting teams, benchmark designers | Cutoff-bound tasks, future-leakage tests, uncertainty checks. | [Forecasting Evaluation Playbook](financial-forecasting-evaluation-playbook.md) |
| Tool-use and trajectory evaluation | Agent-framework maintainers | Tool-order checks, observation linkage, failed-call recovery, repeated-trial reporting. | [Tool-use Evaluation Playbook](financial-tool-use-evaluation-playbook.md) |
| Governance and benchmark cards | Data leads, compliance reviewers | Source manifests, redistribution boundaries, leakage review, benchmark cards. | [Benchmark Card Template](financial-benchmark-card-template.md) |
| Annotation and preference quality | Annotation leads, reward-data teams | Multi-axis review records, adjudication triggers, preference-quality checks. | [Annotation and Preference Quality for Finance](annotation-preference-quality-finance.md) |

## Current Runnable Coverage

The seed currently covers these task families:

- Public-source search.
- Exact data lookup.
- Filing citation QA.
- Filing-grounded explanation.
- Toy backtesting.
- Forecasting cutoff checks.
- Risk calculation.
- Financial tool-use trace checks.
- Portfolio-boundary refusal.
- Compliance refusal.

Run them with:

```bash
python examples/financial-agent-eval-seed/run_finance_eval.py
```

## What Makes A Track Worth Expanding

A track is worth expanding when it can produce all of the following:

- A public-safe task spec.
- A visible fixture or public-source reference.
- A passing reference answer.
- A known-bad answer that fails for an understandable reason.
- A deterministic verifier or schema.
- A short report that a reader can inspect without running code.

## Contribution Targets

Good next contributions are narrow and testable:

- Add one new task family.
- Add one failure example to an existing task.
- Add one verifier check that catches a realistic finance-specific error.
- Add one benchmark-card field that improves provenance, leakage review, or safety review.
- Add one source-governance rule that keeps public examples reproducible.

Avoid broad trend commentary, private data, unverifiable claims, production-readiness language, or investment-advice framing.
