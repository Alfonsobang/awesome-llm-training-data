# Upstream Contribution Shortlist

This shortlist identifies public projects where future contributions could be useful for LLM data engineering practitioners. It is intentionally conservative: each idea should be small enough for maintainers to review, connected to public documentation, and free of private company context.

## Contribution Principles

- Read the target project's `CONTRIBUTING` guide and recent merged PRs before opening a PR.
- Prefer documentation, examples, metadata clarification, reproducibility notes, or testable quality checks.
- Avoid drive-by formatting changes.
- Avoid claims based on private workflows, internal metrics, or unnamed production experience.
- Open at most one PR per project until maintainers respond.

## Shortlist

### Hugging Face DataTrove

- Link: [huggingface/datatrove](https://github.com/huggingface/datatrove)
- Why it fits: DataTrove is directly relevant to large-scale corpus processing, filtering, and deduplication.
- Possible contribution: Add or improve documentation around dataset-quality audit checkpoints in web-data pipelines, such as provenance, deduplication level, language filtering, and output metadata.
- Maintainer value: Helps users treat data-processing pipelines as reviewable engineering artifacts rather than one-off scripts.
- First step: Review current examples and open a small issue proposing a documentation addition before sending a PR.

### ModelScope Data-Juicer

- Link: [modelscope/data-juicer](https://github.com/modelscope/data-juicer)
- Why it fits: Data-Juicer focuses on data processing for foundation models and welcomes contributions such as operators, recipes, documentation, and usage feedback.
- Possible contribution: Add a practical recipe or documentation note for evaluating filtering results with a data-quality rubric.
- Maintainer value: Connects operator usage to dataset review decisions, which is useful for teams building repeatable data pipelines.
- First step: Read the developer guide and identify whether a docs page or example recipe is the smallest acceptable contribution.

### Argilla

- Link: [argilla-io/argilla](https://github.com/argilla-io/argilla)
- Why it fits: Argilla is closely aligned with annotation, feedback, preference data, and human-in-the-loop dataset curation.
- Possible contribution: Improve documentation or examples around annotation QA workflows, including guideline calibration, disagreement review, and adjudication.
- Maintainer value: Helps users move from collecting labels to managing label quality over time.
- First step: Review the contributor guide and recent documentation PRs to match the project's tone and structure.

### Ragas

- Link: [explodinggradients/ragas](https://github.com/explodinggradients/ragas)
- Why it fits: Ragas is relevant to RAG evaluation, including retrieval and generation quality.
- Possible contribution: Propose documentation that separates evaluation data design from metric selection, especially for citation faithfulness and regulated-domain use cases.
- Maintainer value: Helps users avoid treating RAG metrics as a substitute for well-designed evaluation datasets.
- First step: Review current docs and examples for an existing page where a short "evaluation data design" note would fit.

### MLCommons Croissant

- Link: [mlcommons/croissant](https://github.com/mlcommons/croissant)
- Why it fits: Croissant is relevant to dataset metadata and governance.
- Possible contribution: Add examples or notes that make LLM dataset documentation easier to connect with provenance, license, and maintenance metadata.
- Maintainer value: Strengthens the bridge between dataset metadata standards and practical LLM data governance.
- First step: Review issue tracker and examples to avoid duplicating existing metadata patterns.

## Near-term Plan

1. Start with one documentation-focused issue in DataTrove or Argilla.
2. Wait for maintainer signal before opening a PR.
3. Use the flagship repository to document the public rationale and final contribution link.
4. Prefer a small accepted contribution over many unreviewed PRs.

