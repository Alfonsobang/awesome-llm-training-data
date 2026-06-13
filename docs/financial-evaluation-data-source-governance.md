# Financial Evaluation Data Source Governance

Financial-agent evaluation needs a source-governance layer, not just a list of URLs. A task should make it clear which sources are allowed, what timestamps must be retained, which citation fields are required, and whether third-party data may be packaged or should remain reference-only.

The public seed now includes a machine-checkable [source manifest](../examples/financial-agent-eval-seed/data-sources/source-manifest.json).

## Core Policy

- Public accessibility does not automatically grant redistribution rights.
- External sources default to `reference_only`.
- Synthetic fixtures are the safe default when licensing, privacy, or market-data terms are unclear.
- Cutoff-sensitive tasks must retain source dates, retrieval timestamps, and vintage or period fields where applicable.
- Task specs should reference governed `source_id` values instead of relying only on prose.
- Terms and access requirements should be reviewed again before collecting or redistributing third-party data.

This is an engineering checklist, not legal advice.

## Manifest Fields

| Field | Purpose |
| --- | --- |
| `source_id` | Stable identifier used by task specs. |
| `source_type` | Regulator API, macro API, disclosure portal, or synthetic fixture. |
| `official_url` | Official documentation or portal entry point. |
| `access_method` | Public API, registered API key, manual search, or bundled fixture. |
| `packaging_policy` | Whether data is bundled, reference-only, or blocked pending review. |
| `terms_review_required` | Signals that current terms should be checked before use. |
| `allowed_task_families` | Limits where a source may be used. |
| `temporal_fields` | Dates and vintage fields needed for cutoff integrity. |
| `required_citation_fields` | Minimum evidence fields expected from a task run. |

## Current Public Source Index

The first manifest contains conservative references for:

- [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces)
- [FRED Series Observations API](https://fred.stlouisfed.org/docs/api/fred/series_observations.html)
- [World Bank Indicators API](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation)
- [HKEXnews Listed Company Information Title Search](https://www1.hkexnews.hk/search/titlesearch.xhtml?lang=en)
- [CNINFO Disclosure Portal](https://www.cninfo.com.cn/new/index)
- repository-owned synthetic fixtures

The manifest does not claim that every referenced source may be redistributed. It deliberately separates source discovery from benchmark packaging.

## Validation

Run:

```bash
python examples/financial-agent-eval-seed/validate_sources.py
```

The validator checks:

- unique `source_id` values,
- required governance fields,
- HTTPS official links for external sources,
- explicit packaging policies,
- temporal and citation fields,
- task-to-source mappings,
- whether a source allows the referenced task family.

## Why This Matters For Harbor Tasks

A Harbor task can verify outputs and retain trajectories, but a financial benchmark still needs source policy. For example:

- A filing-QA task should retain document period and retrieval time.
- A macro forecasting task should retain vintage or real-time fields.
- A toy backtest should prefer synthetic fixtures unless market-data redistribution terms are clear.
- A browser-search task should cite the document URL, publication date, and retrieval time.

This source layer complements task verifiers and ATIF trajectory audits.
