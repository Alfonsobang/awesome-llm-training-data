You are evaluating public-source search behavior for a financial agent.

Using only `fixtures/candidate_sources.json`, select the best source for answering questions about `SYNTH-FIN-001` fiscal year 2025 annual financial results.

Return a JSON artifact at `/logs/artifacts/answer.json` with:

- `task_id`
- `issuer_id`
- `fiscal_year`
- `selected_source_id`
- `selected_source_type`
- `citations`
- `rejected_source_ids`
- `selection_rationale`
- `limitations`
- `not_investment_advice`

Do not use internet access, private financial feeds, investment advice, trading signals, or unsupported claims.
