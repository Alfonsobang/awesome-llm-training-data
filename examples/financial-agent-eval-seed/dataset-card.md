# Dataset Card: Financial Agent Evaluation Seed

## Purpose

This seed is designed to test whether financial agents can complete public-data tasks with auditable evidence. It focuses on search, lookup, filing-grounded explanation, toy backtesting, and compliance-boundary refusal.

## Intended Use

- Benchmark design research.
- Public-data financial agent evaluation prototypes.
- Trajectory-aware grading experiments.
- Harbor-compatible task design.

## Out Of Scope

- Real-money trading.
- Investment advice.
- Customer account analysis.
- Private company data.
- Internal research workflows.
- Production-readiness claims.

## Data Sources

Task specs should use only public sources with clear access terms, such as public company filings, official reports, exchange or regulator disclosures, and clearly licensed datasets.

This seed does not package third-party data files.

The governed source index is stored in [data-sources/source-manifest.json](data-sources/source-manifest.json). External sources default to `reference_only`; repository-owned synthetic fixtures are the safe default for bundled examples.

## Evaluation Evidence

Recommended evidence for each run:

- task instruction,
- public source references,
- calculation artifact,
- agent trajectory,
- verifier output,
- safety rubric output,
- repeated-trial metric output.

## Known Risks

- Public sources can change location or formatting.
- Public accessibility does not automatically grant redistribution rights.
- Market data licensing varies by source.
- Backtesting tasks are easy to misinterpret as trading advice.
- Forecasting tasks can leak future information if cutoffs are not enforced.
- LLM judges can be inconsistent if rubrics are too broad.

## Recommended Reporting

Report completion, grounding, numeric correctness, cutoff violations, safety pass rate, pass@k, Pass^k, and missing-evidence rate separately.
