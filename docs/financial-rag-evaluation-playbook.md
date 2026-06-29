# Financial RAG Evaluation Playbook

Financial RAG evaluation should test more than whether an answer sounds plausible. It should test retrieval, citation, extraction, calculation, and refusal behavior under source and time constraints.

## What To Evaluate

| Layer | Question | Example check |
| --- | --- | --- |
| Retrieval | Did the system retrieve the right filing, report, or disclosure? | Source type, source date, issuer, and filing period match the task. |
| Citation | Does the cited evidence actually support the answer? | Citation references the section, table, field path, or excerpt used. |
| Extraction | Are values copied with correct units and scale? | Numeric type, unit, scale, and fiscal-period metadata are present. |
| Calculation | Are derived metrics reproducible? | Formula, inputs, and output are included. |
| Time boundary | Does the system respect the evaluation cutoff? | No source after cutoff; rows used are listed. |
| Refusal | Does the system refuse unsafe finance requests? | Refusal names the unsafe request and offers a safe alternative. |
| Trace | Can an evaluator replay or inspect the tool path? | Tool calls, observations, and answer fields are linked. |

## Minimal Artifact Schema

A finance RAG answer should prefer structured output:

```json
{
  "answer": "...",
  "values": {},
  "citations": [
    {
      "source": "...",
      "section": "...",
      "supports": "..."
    }
  ],
  "calculation_notes": [],
  "limitations": [],
  "not_investment_advice": true
}
```

## Known-Bad Patterns

- Answer cites a source but uses a value that does not appear in that source.
- Answer quotes a correct value but assigns the wrong fiscal period.
- Answer retrieves a relevant filing but uses market commentary for the final conclusion.
- Answer performs a ratio calculation without exposing inputs.
- Answer uses a post-cutoff source in a pre-cutoff task.
- Answer turns evidence extraction into a buy/sell recommendation.

## Relation To FinanceBench

[FinanceBench](https://github.com/patronus-ai/financebench) is an important reference for open-book financial QA. This project should not clone that scope. The opportunity here is to evaluate financial agents that use tools, traces, cutoffs, structured artifacts, and governance controls.

## Next Runnable Task

The next task to add should be a small financial search/RAG task:

- retrieve the correct synthetic filing excerpt,
- extract one value and one explanation,
- cite the exact section,
- reject unsupported investment advice,
- and emit a structured `answer.json`.
