# Public Launch Note

I am turning `awesome-llm-training-data` into a practical, public-safe track for financial agent evaluation.

The starting point is a simple observation: financial agents can produce plausible final answers while still failing in ways that static Q&A benchmarks miss. They may choose the wrong source, mix units, cite unsupported evidence, leak future data into a backtest, ignore failed tool calls, or drift into unsafe advice.

This repo focuses on those failure modes as data and evaluation engineering problems.

## What Is Already Runnable

The current seed includes public-safe task specs, synthetic fixtures, Harbor-style task templates, deterministic verifiers, source-governance metadata, and generated reports.

Start here:

```bash
python examples/financial-agent-eval-seed/run_finance_eval.py
```

The reference suite passes all current tasks, and the known-bad candidate fails them. That contrast is intentional: the first goal is to make failure visible and reproducible before growing the benchmark.

## Current Tracks

- [Financial Agent Evaluation Task Matrix](financial-agent-evaluation-task-matrix.md): task families for search, lookup, filing QA, backtesting, forecasting, tool use, refusal, preference review, and governance.
- [Financial Agent Failure Gallery](financial-agent-failure-gallery.md): concrete failure modes that should become tests.
- [Financial RAG Evaluation Playbook](financial-rag-evaluation-playbook.md): retrieval, citation, extraction, calculation, and refusal checks for finance RAG.
- [Financial Data Governance Control Plane](financial-data-governance-control-plane.md): source manifests, packaging policy, cutoff control, and redistribution boundaries.
- [Harbor Finance Task Pack Blueprint](harbor-finance-task-pack-blueprint.md): a practical path toward Harbor-style finance task packaging.
- [Finance Preference Review Schema](../schemas/finance-preference-review.schema.json): a multi-axis rubric for judging finance-specific preference and feedback data.

## What This Is Not

- Not a trading leaderboard.
- Not investment advice.
- Not a production-readiness claim.
- Not private company data, real user data, or proprietary workflows.
- Not a list of generic AI links.

## What I Would Like Feedback On

- Which financial-agent task families are most useful to make runnable next?
- What evidence should a serious finance-agent benchmark require beyond the final answer?
- How should repeated-trial stability be reported for agent runs?
- Which source-governance rules are strict enough without making public examples unusable?
- Where can Harbor-style task packaging make this easier for other agent-evaluation teams?

## Short Share Copy

I am building a public-safe financial agent evaluation track inside `awesome-llm-training-data`.

It focuses on failures that static finance QA often misses: wrong sources, wrong units, unsupported citations, cutoff leakage, unstable tool traces, and unsafe advice boundaries.

The repo now includes runnable seed tasks, synthetic fixtures, deterministic verifiers, Harbor-style task templates, source-governance reports, and a finance preference-review schema.

Repo: https://github.com/Alfonsobang/awesome-llm-training-data
