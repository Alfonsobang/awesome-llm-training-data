# Risk Calculation Drawdown

This Harbor-style template evaluates whether a financial agent can compute basic risk metrics from a small synthetic portfolio value series.

The task checks maximum drawdown, peak/trough dates, total return, daily sample volatility, annualized volatility, data-window integrity, and non-advice framing.

## What It Catches

- Wrong drawdown sign.
- Using absolute point loss instead of percentage drawdown.
- Wrong peak or trough date.
- Population volatility when sample volatility is requested.
- Missing annualization assumption.
- Advice-like language around risk metrics.

## Run The Verifier

From the repository root:

```bash
python -m unittest discover -s examples/financial-agent-eval-seed/harbor-template/risk-calculation-drawdown/tests -p "test_*.py"
```

Candidate artifacts should be written to `answer.json` with the same shape as `solution/answer.json`.
