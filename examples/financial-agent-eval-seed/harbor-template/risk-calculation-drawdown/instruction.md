# Task

Calculate risk metrics from the provided synthetic portfolio value series.

Rules:

- Use every row in `synthetic_portfolio_values.csv`.
- Report total return, maximum drawdown, peak date, trough date, daily return volatility, and annualized volatility.
- Use sample standard deviation for daily return volatility.
- Annualize with `sqrt(252)`.
- Return a structured `answer.json`.
- Include formulas, assumptions, limitations, and a clear non-advice boundary.

This is a synthetic evaluation fixture. Do not present the result as investment advice, a trading signal, or a production risk model.
