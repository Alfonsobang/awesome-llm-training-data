# Financial-domain LLM Evaluation Checklist

Financial-domain LLM evaluation should test grounded reasoning, data governance, and risk controls. It should not be treated as investment advice, trading signal validation, or proof of production readiness.

## Evaluation Scope

- Define the task: financial QA, document understanding, table reasoning, compliance support, research summarization, customer-support assistance, or internal knowledge retrieval.
- Identify the user context: analyst, operations staff, compliance reviewer, product support, or general user.
- Separate knowledge evaluation from tool-use, retrieval, and workflow evaluation.
- State what the benchmark does not measure.

## Data Source Review

- Prefer public filings, public reports, public benchmark datasets, and documented synthetic examples.
- Record source date, document type, language, jurisdiction, and redistribution constraints.
- Avoid private customer data, account data, transaction data, employee communications, or internal business documents.
- Check whether examples require domain knowledge, numerical reasoning, table-text reasoning, or legal/compliance interpretation.

## Leakage and Freshness

- Check whether public benchmark questions may already appear in pretraining or instruction data.
- Keep time-sensitive questions separate from static knowledge questions.
- For public filings, record the filing date and evaluation date.
- Avoid asking questions whose answers depend on data unavailable at the stated time.

## Answer Quality

- Require citation or evidence when answers depend on source documents.
- Separate correct final answers from correct reasoning.
- Mark unsupported but plausible answers as failures.
- Track numerical errors, unit errors, currency errors, date errors, and entity confusion separately.

## Risk Categories

- Hallucinated facts, ratios, filings, or regulatory references.
- Unsupported investment recommendations.
- Confusion between company, ticker, subsidiary, product, or reporting period.
- Overconfident answers when source evidence is missing.
- Privacy or confidentiality leakage in prompts, retrieved context, or outputs.

## RAG-specific Checks

- Evaluate retrieval recall separately from answer generation.
- Include hard negatives with similar company names, reporting periods, or metrics.
- Test citation faithfulness: cited evidence must support the answer.
- Track whether the model uses retrieved context or falls back to memorized knowledge.

## Governance Requirements

- Document dataset provenance, license, and known limitations.
- Keep evaluation data versioned and reproducible.
- Define reviewer roles for domain, risk, compliance, and data quality review.
- Require human review before using evaluation results in high-impact decisions.

## Practical Output

For each evaluation dataset or benchmark, maintain:

- task definition.
- source summary.
- license and access notes.
- leakage risk.
- scoring method.
- known limitations.
- review owner.

