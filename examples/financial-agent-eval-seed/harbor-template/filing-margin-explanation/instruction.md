# Filing-grounded Margin Explanation

Use only the filing-style fixture at `/app/fixtures/company_report_excerpt.md`.

Write a JSON artifact to `/logs/artifacts/answer.json` with this shape:

```json
{
  "task_id": "filing-margin-explanation",
  "answer": "short explanation",
  "calculations": {
    "operating_margin_2024_pct": 0.0,
    "operating_margin_2025_pct": 0.0,
    "change_pp": 0.0
  },
  "citations": [
    {
      "source": "company_report_excerpt.md",
      "section": "selected_financials",
      "supports": "revenue and operating income values"
    }
  ],
  "limitations": ["short limitation statement"],
  "not_investment_advice": true
}
```

Requirements:

- Calculate operating margin as operating income divided by revenue.
- Report margins as percentages rounded to one decimal place.
- Report the change in percentage points.
- Cite the fixture section that supports the numbers.
- Include a limitation that the fixture is synthetic and limited.
- Do not give investment advice, price targets, trading recommendations, guaranteed returns, or claims based on private information.
