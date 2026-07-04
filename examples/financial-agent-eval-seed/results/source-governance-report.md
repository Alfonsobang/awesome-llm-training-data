# Financial Data Source Governance Report

This stable report is generated from the source manifest and task specs. It makes the seed's source policy inspectable without opening every JSON file.

- Manifest version: `1.0`
- Reviewed on: `2026-05-31`
- Sources total: 6
- Sources referenced by tasks: 4
- Tasks total: 10
- Task-source mappings: 12
- Sources requiring terms review: 5

## Packaging Policies

| Packaging policy | Source count |
| --- | ---: |
| `bundled_synthetic_only` | 1 |
| `do_not_package_without_review` | 2 |
| `reference_only` | 3 |

## Task Source Mappings

| Task | Family | Source | Packaging | Terms review |
| --- | --- | --- | --- | --- |
| `compliance-refusal-guaranteed-return` | `compliance_boundary` | `synthetic_fixture` | `bundled_synthetic_only` | `false` |
| `exact-data-lookup-public-filing` | `data_lookup` | `sec_edgar_api` | `reference_only` | `true` |
| `filing-citation-check` | `filing_qa` | `sec_edgar_api` | `reference_only` | `true` |
| `filing-grounded-margin-explanation` | `filing_qa` | `sec_edgar_api` | `reference_only` | `true` |
| `financial-tool-use-trace` | `tool_use` | `synthetic_fixture` | `bundled_synthetic_only` | `false` |
| `forecasting-cutoff-check` | `forecasting` | `synthetic_fixture` | `bundled_synthetic_only` | `false` |
| `portfolio-boundary-refusal` | `compliance_boundary` | `synthetic_fixture` | `bundled_synthetic_only` | `false` |
| `public-filing-search` | `financial_search` | `sec_edgar_api` | `reference_only` | `true` |
| `public-filing-search` | `financial_search` | `hkexnews_title_search` | `do_not_package_without_review` | `true` |
| `public-filing-search` | `financial_search` | `cninfo_disclosure_portal` | `do_not_package_without_review` | `true` |
| `risk-calculation-drawdown` | `risk_calculation` | `synthetic_fixture` | `bundled_synthetic_only` | `false` |
| `toy-backtest-moving-average` | `backtesting` | `synthetic_fixture` | `bundled_synthetic_only` | `false` |

## Policy Note

Public accessibility does not automatically grant redistribution rights. Review current terms before collecting, storing, or redistributing third-party data.

## Safety Boundary

Public accessibility does not imply redistribution rights. The seed bundles synthetic fixtures by default and treats external sources as reference-only unless reviewed.
