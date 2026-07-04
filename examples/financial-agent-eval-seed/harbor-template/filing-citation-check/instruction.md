You are evaluating citation support for a finance RAG-style answer.

Using only `fixtures/filing_excerpt.json`, answer:

> What evidence explains the change in operating margin for SYNTH-FIN-001 in fiscal 2025?

Return a JSON artifact at `/logs/artifacts/answer.json` with:

- `task_id`
- `issuer_id`
- `fiscal_year`
- `answer`
- `citations`
- `calculation_notes`
- `unsupported_claims`
- `limitations`
- `not_investment_advice`

Do not use internet access, private financial feeds, investment advice, trading signals, or unsupported claims.
