# Harbor-style Financial Task Templates

This directory contains small Harbor-style task scaffolds for financial agent evaluation. They are designed to be readable, deterministic, and safe to publish.

These templates use synthetic fixtures. They do not contain private company data, real user data, investment advice, trading signals, or proprietary workflows.

## Templates

| Template | What it evaluates | Main verifier checks |
| --- | --- | --- |
| [Compliance refusal](compliance-refusal) | Safe refusal of guaranteed-return, personalized-advice, and private-information requests. | Required refusal shape, unsafe request coverage, safe alternative, no trading instruction. |
| [Exact data lookup](exact-data-lookup) | Exact extraction from a financial statement fixture. | Required JSON shape, exact values, citations, numeric types, safety boundary. |
| [Filing margin explanation](filing-margin-explanation) | Filing-grounded explanation with margin calculations. | Margin values, citation sections, limitations, disallowed financial claims. |
| [Public source search](public-source-search) | Selection of the correct public-safe source from candidate sources. | Official source selection, rejected weak sources, citation path, safety boundary. |
| [Toy moving-average backtest](toy-backtest-moving-average) | Fixed-rule toy backtest with cutoff discipline. | Cutoff date, rows used, final equity, exposure days, non-advice framing. |

## Validate All Templates

From the repository root:

```bash
python examples/financial-agent-eval-seed/validate_harbor_templates.py
```

## Design Principles

- Keep fixtures small enough to inspect manually.
- Require structured artifacts, not prose-only answers.
- Prefer deterministic verifier tests for numeric and citation checks.
- Make safety boundaries visible in the expected output.
- Treat missing evidence as a measurable failure, not a silent omission.
