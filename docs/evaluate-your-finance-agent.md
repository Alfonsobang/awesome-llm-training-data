# Evaluate Your Own Finance Agent

This guide shows how to adapt the seed benchmark to a candidate financial agent without adding private data or investment-advice examples.

## 1. Create Candidate Artifacts

From the repository root:

```bash
python finagent_eval.py init-candidate tmp/my-finance-agent
```

This creates one file per task:

```text
tmp/my-finance-agent/
|-- public-source-search/answer.json
|-- exact-data-lookup/answer.json
|-- filing-citation-check/answer.json
|-- filing-margin-explanation/answer.json
|-- financial-tool-use-trace/answer.json
|-- risk-calculation-drawdown/answer.json
|-- toy-backtest-moving-average/answer.json
|-- forecasting-cutoff-check/answer.json
|-- portfolio-boundary-refusal/answer.json
`-- compliance-refusal/answer.json
```

Each `answer.json` should contain the candidate output, citations, limitations, and a `not_investment_advice` flag.

## 2. Fill Answers From Your Agent

Use the task instructions under `examples/financial-agent-eval-seed/harbor-template/<task-id>/instruction.md`.

Keep the candidate artifacts public-safe:

- use only public or synthetic fixtures included in the task,
- do not add real customer, account, portfolio, order, or transaction data,
- do not add proprietary workflows,
- do not publish investment advice, target prices, trading signals, or model ranking claims.

## 3. Run The Verifiers

```bash
python finagent_eval.py run --artifact-root tmp/my-finance-agent
```

The runner writes a JSON and Markdown report under `examples/financial-agent-eval-seed/results/` unless you pass a custom `--results-dir`.

## 4. Build A Scorecard

```bash
python finagent_eval.py scorecard \
  --report examples/financial-agent-eval-seed/results/latest-report.json \
  --candidate my-finance-agent \
  --output-prefix examples/financial-agent-eval-seed/results/my-finance-agent-scorecard
```

The scorecard is intended for engineering review, not marketing. A failure should be treated as a task-design or agent-behavior debugging signal.

## 5. Interpret Results Conservatively

The seed is useful when it surfaces concrete mistakes:

- wrong source,
- wrong unit or period,
- unsupported citation,
- missing tool observation,
- future-data leakage,
- unsafe personalized advice,
- missing limitation.

It is not enough to claim broad financial reliability. Expand task coverage, run repeated trials, document sources, and review failure traces before drawing stronger conclusions.
