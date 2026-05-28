# Financial Agent Evaluation Task Cards

These task cards turn the agenda into concrete benchmark-design units. They are intentionally public-data-only and do not contain real trading signals.

## Card 1: Public Filing Search

- **Goal**: Find the correct public filing or annual report for a company and period.
- **Skills tested**: search, source selection, citation, date handling.
- **Verifier evidence**: expected filing URL or accession number.
- **Common failure modes**: wrong fiscal year, stale source, unaudited blog summary, missing citation.

## Card 2: Exact Financial Data Lookup

- **Goal**: Retrieve exact financial values from public filings or structured data.
- **Skills tested**: table extraction, unit conversion, fiscal-period handling.
- **Verifier evidence**: value, unit, period, source.
- **Common failure modes**: wrong currency, trailing-twelve-month confusion, rounded value mismatch.

## Card 3: Filing-grounded Explanation

- **Goal**: Explain a change in a metric using cited filing passages.
- **Skills tested**: retrieval, summarization, numeric reasoning, evidence grounding.
- **Verifier evidence**: required citations and calculation table.
- **Common failure modes**: uncited causal claim, hallucinated management commentary, unsupported investment framing.

## Card 4: Toy Backtest

- **Goal**: Implement a fixed-rule backtest on public historical data.
- **Skills tested**: data loading, split adjustment, transaction-cost assumptions, metric calculation.
- **Verifier evidence**: code, input window, output metrics, reproducible run.
- **Common failure modes**: look-ahead bias, unadjusted prices, hidden parameter search, treating toy results as advice.

## Card 5: Cutoff-bound Forecast

- **Goal**: Make a forecast using only information available before a cutoff.
- **Skills tested**: temporal integrity, uncertainty, source filtering.
- **Verifier evidence**: cutoff date, allowed sources, feature trace, forecast interval.
- **Common failure modes**: future leakage, overconfident point forecast, undocumented features.

## Card 6: Financial Tool-use Workflow

- **Goal**: Use multiple financial tools in the right order.
- **Skills tested**: tool selection, error recovery, returned-data interpretation.
- **Verifier evidence**: tool-call trajectory, successful outputs, final answer.
- **Common failure modes**: calling wrong endpoint, ignoring failed call, hallucinating unavailable fields.

## Card 7: Compliance Refusal

- **Goal**: Refuse or safely redirect a prohibited financial request.
- **Skills tested**: policy boundary, helpful refusal, safe alternative.
- **Verifier evidence**: refusal text and allowed educational alternative.
- **Common failure modes**: direct investment advice, guaranteed return claim, insider-information inference.

## Card 8: Evidence-grounded Report

- **Goal**: Produce a concise report with citations, assumptions, limitations, and appendix.
- **Skills tested**: synthesis, source grounding, calculation transparency.
- **Verifier evidence**: citations, artifact files, calculation appendix, limitation statement.
- **Common failure modes**: unsupported conclusion, missing calculation appendix, weak provenance.

## Suggested Task Metadata

```yaml
task_id:
family:
risk_level: low | medium | high
public_sources:
allowed_tools:
prohibited_actions:
information_cutoff:
required_artifacts:
verifier:
metrics:
known_failure_modes:
```
