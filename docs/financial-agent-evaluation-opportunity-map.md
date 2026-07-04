# Financial Agent Evaluation Opportunity Map

This page explains where the project can become useful in a crowded AI-evaluation market. It is intentionally conservative: no adoption claims, no benchmark superiority claims, and no investment claims.

## Market Shape

The public agent-evaluation space is moving from static answer grading toward runnable environments, tool trajectories, repeated attempts, and verifier evidence.

Finance is a strong domain for this shift because financial agents must handle public-source grounding, temporal cutoffs, numeric precision, data provenance, and regulated-domain refusal boundaries.

## Opportunity Lanes

| Lane | Why it is timely | What this repo can contribute |
| --- | --- | --- |
| Harbor-style task packs | Harbor exposes a visible framework for evaluating agents, sharing benchmarks/environments, and generating rollouts | public-safe finance task-pack examples, manifests, and verifier conventions |
| Financial RAG evaluation | finance QA frequently depends on exact document, table, period, and citation support | citation verifiers, source manifests, and table-text checks |
| Tool-use evaluation | financial agents often chain search, filings, quotes, calculators, and summaries | tool trajectory tasks and repeated-trial reporting |
| Forecasting and pastcasting discipline | finance tasks are vulnerable to future-data leakage and overconfident claims | cutoff-aware tasks, uncertainty checks, and non-advice language |
| Data governance for benchmarks | benchmark credibility depends on provenance, leakage controls, and redistribution boundaries | benchmark cards, source manifests, and CI validators |
| Preference data for finance | human feedback can reward confidence over evidence if the rubric is weak | finance preference-review schema and adjudication examples |

## Differentiation

This repo should not try to become the largest finance benchmark immediately. A better wedge is:

> small, inspectable, public-safe financial-agent evaluation tasks with deterministic verifiers and governance metadata.

That wedge is useful because it is easier to review, fork, adapt, and discuss upstream than a large opaque benchmark.

## What To Avoid

- Leaderboard theater before the task quality is mature.
- Live trading examples.
- Private data stories.
- Claims that a model is safe for production finance.
- Vague AI trend commentary without an artifact.
- Large lists of links without quality review.

## External Reference Points

- [Harbor](https://github.com/harbor-framework/harbor) for framework-level agent evaluation, benchmark/environment sharing, and rollouts.
- [Terminal-Bench](https://github.com/harbor-framework/terminal-bench) for environment-based agent evaluation.
- [Finance Agent Benchmark](https://arxiv.org/abs/2508.00828) for financial research task benchmarking.
- [FinAgentBench](https://arxiv.org/abs/2508.14052) for agentic retrieval in financial question answering.
- [FinMCP-Bench](https://arxiv.org/abs/2603.24943) for financial tool-use evaluation under MCP-style tooling.
- [Finance Agent v2](https://www.vals.ai/benchmarks/fabv2) as a current public finance-agent benchmark reference.

## Next Shareable Artifacts

1. A short blog-style README section: "Seven failures normal finance QA benchmarks miss."
2. Two scorecard examples: one passing candidate and one known-bad candidate.
3. A script that converts seed reports into a scorecard summary.
4. A task-pack compatibility note for Harbor maintainers.
5. A small issue series for the next three task families in the task zoo.
