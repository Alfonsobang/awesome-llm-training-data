# Impact Backlog

This backlog turns the project's multi-track pages into concrete artifacts. It is intentionally small, public-safe, and biased toward runnable work.

The repository has not shown strong external feedback yet. The response is not to add more generic pages. The response is to convert each promising page into a task, verifier, schema, report, or issue that other practitioners can reuse.

Machine-readable source: [`impact/impact-backlog.json`](../impact/impact-backlog.json)

## Current Priorities

| Priority | Status | Track | Artifact | Why it matters |
| --- | --- | --- | --- | --- |
| P0 | Completed | Financial agent eval | Public-source search task | Search is the first tool-use failure surface in many financial agents. |
| P0 | Completed | Financial RAG eval | Citation verifier | Unsupported citations are common, concrete, and easy to evaluate. |
| P1 | Completed | Data governance | Source-governance report | Makes source policy visible to data leads and reviewers. |
| P1 | Planned | Synthetic data | Synthetic fixture validator | Keeps public examples useful without fake realism. |
| P1 | Planned | Annotation/preference | Finance preference-review rubric schema | Prevents preference data from rewarding unsupported confidence. |
| P2 | Planned | Distribution | Public launch note | Gives the project a crisp narrative for outreach. |

## Why This Backlog Exists

The project should not rely on a single bet. FinAgentBench Seed is the anchor, but several adjacent assets can attract different audiences:

- agent-eval engineers,
- RAG engineers,
- data-governance leads,
- synthetic-data builders,
- annotation and preference-data teams,
- and agent-framework maintainers.

Each item in the backlog must have:

- a source page,
- a next artifact path,
- a reason it matters,
- and concrete acceptance criteria.

## Next Best Issue To Open

Next:

> Add synthetic fixture authoring checks

The public-source search task, finance RAG citation verifier, and source-governance report are now implemented. The next highest-leverage item is synthetic fixture validation: it keeps public examples useful without creating fake realism.
