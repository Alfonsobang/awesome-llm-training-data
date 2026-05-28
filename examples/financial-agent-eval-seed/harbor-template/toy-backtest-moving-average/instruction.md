# Toy Moving-average Backtest

Use only the synthetic price fixture at `/app/fixtures/synthetic_prices.csv`.

Task:

- Use a 3-day simple moving average.
- A signal is active when the close is greater than the 3-day moving average at the end of day `t`.
- If the signal is active at day `t`, hold the asset from close `t` to close `t+1`; otherwise hold cash.
- Use only rows on or before cutoff date `2025-01-06`.
- Start with equity `1.0`.

Write `/logs/artifacts/answer.json` with this shape:

```json
{
  "task_id": "toy-backtest-moving-average",
  "cutoff_date": "2025-01-06",
  "data_rows_used": 6,
  "strategy": "3-day SMA close greater than SMA, next-day close-to-close holding",
  "metrics": {
    "final_equity": 1.0095,
    "total_return_pct": 0.95,
    "exposure_days": 2
  },
  "evidence": {
    "source": "synthetic_prices.csv",
    "no_future_rows_used": true
  },
  "limitations": ["short limitation statement"],
  "not_investment_advice": true
}
```

Requirements:

- Round `final_equity` to four decimals.
- Round `total_return_pct` to two decimals.
- Do not use future rows after the cutoff.
- Do not present the result as a trading recommendation.
- Include a limitation that the fixture is synthetic and too small for investment conclusions.
