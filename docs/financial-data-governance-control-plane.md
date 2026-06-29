# Financial Data Governance Control Plane

Financial evaluation data needs governance before it needs scale. The evaluation harness should make source policy visible and machine-checkable.

## Governance Objects

| Object | Purpose |
| --- | --- |
| Source manifest | Defines official URLs, access method, packaging policy, citation fields, and allowed task families. |
| Dataset card | Explains fixtures, public references, limitations, and redistribution boundaries. |
| Task spec | States allowed sources, tools, prohibited actions, and required evidence. |
| Verifier | Turns governance rules into executable checks. |
| Report | Makes pass/fail reasons reviewable by maintainers. |

## Required Source Fields

Every source should declare:

- source id,
- official URL or fixture URI,
- source type,
- access method,
- packaging policy,
- review date,
- allowed task families,
- temporal fields,
- citation fields,
- and notes about terms or redistribution risk.

## Packaging Policies

Recommended policies:

- `bundled_synthetic_only`: safe to include because the fixture is synthetic.
- `reference_only`: public source may be referenced but not packaged.
- `do_not_package_without_review`: source requires manual review before bundling.

## Why This Matters

Finance teams often evaluate systems with mixed data sources, unclear terms, and implicit cutoffs. That creates evaluation leakage and compliance risk. A public benchmark seed can be small but still model better habits:

- make source assumptions explicit,
- separate public references from bundled fixtures,
- treat cutoff and citation fields as first-class metadata,
- and fail tasks when evidence is missing.

## Current Implementation

The seed already includes:

- [source-manifest.json](../examples/financial-agent-eval-seed/data-sources/source-manifest.json),
- [validate_sources.py](../examples/financial-agent-eval-seed/validate_sources.py),
- and [Financial Evaluation Data Source Governance](financial-evaluation-data-source-governance.md).

## Next Step

Add a source-governance badge or report section that summarizes:

- sources referenced,
- packaging policies,
- review dates,
- unsupported sources,
- and task-to-source mappings.
