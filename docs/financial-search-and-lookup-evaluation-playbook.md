# Financial Search And Lookup Evaluation Playbook

Financial agents often fail before reasoning begins: they choose the wrong source, use the wrong period, extract the wrong field, or cite a page that does not support the answer.

This playbook defines a practical public-safe slice for evaluating those failures.

## Scope

Use this track for tasks where the agent must:

- Select the right public source.
- Retrieve an exact value, date, period, field, or filing section.
- Preserve units and fiscal-period metadata.
- Explain why weaker sources were rejected.
- Produce citation evidence that can be checked deterministically.

## Useful Task Types

| Task type | Good prompt shape | Required evidence | Main verifier checks |
| --- | --- | --- | --- |
| Public-source search | "Find the correct source for company X and fiscal period Y." | Selected source ID, source type, period, citation path. | Official-source selection, period match, rejected weak sources. |
| Exact data lookup | "Return the revenue value for fiscal year Y from this source." | Value, unit, period, field path, source ID. | Numeric value, unit, field path, source match. |
| Citation support | "Answer using only the provided filing excerpt." | Cited section IDs and support notes. | Citation exists, cited text supports answer, no unsupported claim. |
| Source comparison | "Choose the most reliable source among candidates." | Ranking, rejection reason, source policy. | Official source preferred, stale or summary source rejected. |

## Current Repo Assets

- [Public-source search task](../examples/financial-agent-eval-seed/harbor-template/public-source-search).
- [Exact data lookup task](../examples/financial-agent-eval-seed/harbor-template/exact-data-lookup).
- [Filing citation check](../examples/financial-agent-eval-seed/harbor-template/filing-citation-check).
- [Source governance report](../examples/financial-agent-eval-seed/results/source-governance-report.md).

## Quality Bar

Strong tasks should make the wrong answer look plausible. Weak tasks only check whether the model can copy a number.

Require:

- A source manifest entry or clearly labeled synthetic fixture.
- A field path or section ID, not only a URL.
- Unit and period checks.
- A known-bad answer that fails for a realistic source, unit, period, or citation mistake.
- A visible limitation statement when sources are synthetic.

Reject:

- Blog summaries as ground truth when official filings or published source documents are available.
- Prompts that ask for current market facts without a frozen retrieval snapshot.
- Answers that cite a document but do not identify the supporting section or field.
- Examples that imply investment advice, trading signals, or production readiness.

## Reviewer Questions

- Could a verifier identify the exact source used?
- Could a reviewer reproduce the extracted value from the visible fixture?
- Does the answer preserve unit, scale, currency, and fiscal period?
- Does the model explain why weaker sources were not used?
- Is the task useful without private company data or real user data?

