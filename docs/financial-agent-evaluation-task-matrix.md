# Financial Agent Evaluation Task Matrix

This matrix turns the finance-agent evaluation agenda into concrete task families that can become runnable examples, Harbor-style tasks, issue cards, or benchmark slices.

The goal is to make the project useful to several audiences at once: agent-evaluation engineers, finance RAG teams, data-governance reviewers, annotation teams, and framework maintainers.

## Design Boundary

- Use public sources or clearly labeled synthetic fixtures.
- Keep every task reproducible from visible inputs.
- Treat tool traces, citations, cutoff dates, and verifier outputs as first-class evidence.
- Do not include private company data, real user data, proprietary workflows, investment advice, trading signals, or claims of production readiness.

## Task Matrix

| Task family | User-facing task | Required evidence | Main failure modes | Verifier style | Current artifact |
| --- | --- | --- | --- | --- | --- |
| Public-source search | Find the right filing, disclosure, market-data source, or regulatory document. | Candidate sources, selected source ID, source type, period, citation path. | Wrong source, stale source, irrelevant source, missing citation. | Deterministic source and metadata checks. | [`public-source-search`](../examples/financial-agent-eval-seed/harbor-template/public-source-search) |
| Exact data lookup | Retrieve exact revenue, income, shares, date, rate, or period fields. | Source field, value, unit, fiscal period, retrieval time. | Wrong unit, wrong period, rounded-away material field, hallucinated value. | Exact or tolerance-based field checks. | [`exact-data-lookup`](../examples/financial-agent-eval-seed/harbor-template/exact-data-lookup) |
| Filing citation QA | Answer from public filing excerpts with section-level citations. | Cited sections, quoted field IDs, answer support map. | Citation theater, unsupported claim, irrelevant excerpt, missing limitation. | Citation-path and support checks. | [`filing-citation-check`](../examples/financial-agent-eval-seed/harbor-template/filing-citation-check) |
| Filing-grounded explanation | Explain a financial change using cited public filing evidence. | Calculation table, cited passages, assumptions, limitations. | Plausible but unsupported causal claim, unit mismatch, missing denominator. | Numeric checks plus citation checks. | [`filing-margin-explanation`](../examples/financial-agent-eval-seed/harbor-template/filing-margin-explanation) |
| Toy backtesting | Run a fixed-rule historical simulation on synthetic or public-safe data. | Code, data window, cutoff date, assumptions, metrics. | Look-ahead bias, hidden parameter tuning, advice framing, missing costs. | Deterministic output and cutoff checks. | [`toy-backtest-moving-average`](../examples/financial-agent-eval-seed/harbor-template/toy-backtest-moving-average) |
| Forecasting / pastcasting | Produce a bounded forecast or reconstruct a past forecast using only pre-cutoff evidence. | Feature list, cutoff date, uncertainty statement, excluded future data. | Future-data leakage, overconfident prediction, missing uncertainty. | Cutoff, evidence-window, and language-boundary checks. | [`forecasting-cutoff-check`](../examples/financial-agent-eval-seed/harbor-template/forecasting-cutoff-check) |
| Financial tool use | Choose quote, fundamentals, filing, or macro tools in an auditable order. | Tool-call sequence, observations, errors, retries, final evidence map. | Wrong tool, ignored tool output, fabricated observation, unrecovered failure. | Trajectory and observation-linkage checks. | [`financial-tool-use-trace`](../examples/financial-agent-eval-seed/harbor-template/financial-tool-use-trace) |
| Compliance refusal | Refuse guaranteed-return, insider-data, manipulation, or personal-advice requests. | User request, refusal rationale, safe alternative, non-advice wording. | Unsafe advice, evasion, overly broad refusal, missing safe alternative. | Policy phrase and prohibited-claim checks. | [`compliance-refusal`](../examples/financial-agent-eval-seed/harbor-template/compliance-refusal) |
| Preference review | Review candidate answers across evidence, numeric, citation, safety, and trace dimensions. | Multi-axis labels, checked sources, adjudication triggers, reviewer notes. | Rewarding confident unsupported answers, single-label ambiguity. | Schema and review-record validation. | [`finance-preference-review.schema.json`](../schemas/finance-preference-review.schema.json) |
| Source governance | Confirm that task sources are public, licensed, packaged correctly, and mapped to tasks. | Source manifest, packaging policy, allowed task families, review date. | Ungoverned source, redistribution ambiguity, missing source owner. | Manifest and task-source mapping checks. | [`source-governance-report.md`](../examples/financial-agent-eval-seed/results/source-governance-report.md) |

## Evaluation Layers

| Layer | What it measures | Why it matters |
| --- | --- | --- |
| Final answer | Required fields, answer format, and user-visible output. | Static correctness still matters, but it is not enough. |
| Evidence | Citations, source IDs, source periods, field paths, and extracted values. | Finance answers need traceable support. |
| Process | Tool calls, observations, retries, cutoff decisions, and artifacts. | Many serious failures happen before the final answer. |
| Safety | Advice boundary, private-data refusal, prohibited tool calls, and uncertainty framing. | Financial examples should not normalize unsafe behavior. |
| Robustness | Repeated attempts, pass@k, Pass^k, missing-evidence rate, and cutoff-violation rate. | One lucky pass is weaker than stable behavior. |
| Governance | Source policies, synthetic labels, redistribution rules, and review dates. | Public benchmark data needs visible operating controls. |

## Next Task Gaps

These are the most useful gaps to turn into issues or PRs:

- Add a risk-calculation task for drawdown or volatility using public-safe fixture data.
- Add a portfolio-analysis refusal task that distinguishes general education from personalized advice.
- Add a benchmark-card template that describes provenance, leakage risks, allowed use, and known limits.

## Related Pages

- [Financial Agent Evaluation Agenda](financial-agent-evaluation-agenda.md)
- [Financial Agent Failure Gallery](financial-agent-failure-gallery.md)
- [Financial RAG Evaluation Playbook](financial-rag-evaluation-playbook.md)
- [Financial Data Governance Control Plane](financial-data-governance-control-plane.md)
- [Harbor Finance Task Pack Blueprint](harbor-finance-task-pack-blueprint.md)
