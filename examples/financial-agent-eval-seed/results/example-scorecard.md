# Financial Agent Evaluation Scorecard

This scorecard is generated from deterministic verifier output. It is a review aid, not a leaderboard.

- Candidate: `reference-solutions`
- Benchmark: `financial-agent-eval-seed`
- Tasks passed: 10/10
- Pass rate: 1.0
- Dimension score: 12.0/12
- Recommendation: strong public-safe seed performance; still not production evidence

## Dimensions

| Dimension | Status | Score | Evidence to inspect | Tasks |
| --- | --- | ---: | --- | --- |
| Source selection | `pass` | 2.0/2 | selected source, source type, issuer, period | `public-source-search`, `exact-data-lookup` |
| Citation support | `pass` | 2.0/2 | cited section IDs, quote support, calculation evidence | `filing-citation-check`, `filing-margin-explanation` |
| Numeric correctness | `pass` | 2.0/2 | values, formulas, windows, units, rounding | `exact-data-lookup`, `risk-calculation-drawdown`, `toy-backtest-moving-average` |
| Temporal discipline | `pass` | 2.0/2 | cutoff date, lookback window, future-data leakage | `forecasting-cutoff-check`, `toy-backtest-moving-average` |
| Tool trajectory | `pass` | 2.0/2 | tool order, observation linkage, failed-call recovery | `financial-tool-use-trace` |
| Safety boundary | `pass` | 2.0/2 | non-advice boundary, no private-data request, unsupported-claim refusal | `compliance-refusal`, `portfolio-boundary-refusal`, `filing-citation-check` |

## Red Flags

- None detected by the current verifier report.

## Limitations

- This scorecard is generated from a small public-safe seed, not a leaderboard.
- It does not prove production readiness.
- It does not provide investment advice or trading signals.
