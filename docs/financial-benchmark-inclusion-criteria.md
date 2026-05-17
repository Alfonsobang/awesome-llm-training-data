# Financial-domain LLM Benchmark Inclusion Criteria

Financial-domain LLM benchmarks are useful when they make evaluation more precise, reproducible, and risk-aware. They are weak when they collapse different financial tasks into a single score or imply that benchmark performance proves production readiness.

This document defines conservative inclusion criteria for financial-domain resources in this repository.

## Include a Resource When

- It is public and accessible through an official repository, paper, dataset card, or project page.
- It has a clear financial-domain task, such as financial QA, table-text reasoning, filing analysis, sentiment analysis, compliance-oriented QA, or RAG evaluation.
- It documents source data, task construction, or evaluation method.
- It is useful to practitioners evaluating LLM behavior, data quality, or financial-domain reasoning.
- Its limitations can be described without relying on private or unverifiable information.

## Exclude or Defer a Resource When

- The link is unverifiable, private, or only a marketing page.
- The dataset appears to include private customer data, account data, transaction data, or internal business documents.
- It mainly promotes investment advice, trading signals, or financial prediction products.
- It has no clear task definition, no evaluation method, or no public documentation.
- It makes unsupported production-readiness claims.
- The license or access terms are unclear enough that practical use would be risky.

## Required Description Fields

Each financial-domain item should make the practical use clear in one sentence:

- resource type: benchmark, dataset, tool, paper, or report.
- task type: QA, numerical reasoning, table-text reasoning, RAG, compliance, sentiment, or data processing.
- source basis: filings, reports, public benchmark data, synthetic examples, or public text.
- limitation note when important.

Example style:

```markdown
- [FinanceBench](https://github.com/patronus-ai/financebench) - Tag: [benchmark] - Benchmark for evaluating LLM financial QA grounded in public filings; it should not be treated as proof of production readiness.
```

## Task Taxonomy

Use this taxonomy when expanding the section:

- **Financial QA**: answering questions about financial concepts, companies, or documents.
- **Numerical reasoning**: calculating or comparing values from financial text or tables.
- **Table-text reasoning**: combining structured tables and narrative disclosure.
- **Filing-grounded RAG**: retrieving and citing public filings or reports.
- **Compliance-oriented QA**: answering policy, regulatory, or risk-control questions with clear source boundaries.
- **Sentiment and event analysis**: classifying public news, filings, or market commentary.
- **Data processing tools**: collecting, parsing, or preparing finance-domain text.

## Review Questions

- What exactly does the benchmark measure?
- What does it not measure?
- Are source documents public?
- Is evaluation time-sensitive?
- Could examples have leaked into training data?
- Does the benchmark require financial domain expertise to judge?
- Are answers source-grounded or based on model memory?
- Are licenses and access terms clear?

## Language and Jurisdiction

Financial evaluation is sensitive to language and jurisdiction.

- State whether the benchmark is Chinese, English, multilingual, or jurisdiction-specific.
- Avoid comparing scores across benchmarks that test different legal, accounting, market, or disclosure contexts.
- Treat regulatory and compliance examples as context-specific unless the source says otherwise.

## Production-readiness Disclaimer

Benchmarks can support model analysis, but they do not certify a model for financial production use. Production decisions require separate review of data rights, privacy, security, compliance, monitoring, human oversight, and business process controls.

