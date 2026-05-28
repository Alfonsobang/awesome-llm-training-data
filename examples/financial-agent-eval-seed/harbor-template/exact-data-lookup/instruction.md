# Exact Financial Data Lookup

Use only the fixture at `/app/fixtures/financial_statement_excerpt.json`.

Write `/logs/artifacts/answer.json` with this shape:

```json
{
  "task_id": "exact-data-lookup",
  "company_id": "SYNTH-FIN-001",
  "fiscal_year": 2025,
  "currency": "USD",
  "values": {
    "revenue": 1250000,
    "net_income": 132000,
    "diluted_shares": 500000
  },
  "citations": [
    {
      "source": "financial_statement_excerpt.json",
      "path": "$.annual_facts[0]"
    }
  ],
  "limitations": ["short limitation statement"],
  "not_investment_advice": true
}
```

Requirements:

- Do not estimate missing fields.
- Do not use outside knowledge.
- Keep numeric values as numbers, not strings.
- Include a limitation that the fixture is synthetic and limited.
- Do not give investment advice, price targets, trading recommendations, guaranteed returns, or claims based on private information.
