# Annotation Quality and Adjudication Guide

Annotation quality is not only an inter-annotator agreement number. For LLM data work, it is an operational system: guidelines, reviewer calibration, task design, disagreement handling, adjudication, audit trails, and feedback loops.

This guide focuses on public-safe practices. It does not include private company workflows, real user data, or proprietary policies.

## 1. Define the Annotation Unit

Before assigning tasks, define what exactly is being judged.

- For classification: clarify whether the label applies to the whole document, one span, one turn, or one response.
- For ranking or preference: define the prompt, candidate responses, tie rules, and skip rules.
- For extraction: define span boundaries, normalization rules, and whether inferred values are allowed.
- For safety or compliance labels: separate observable content from policy interpretation.

## 2. Write Guidelines for Edge Cases

Good guidelines reduce avoidable disagreement.

- Include positive, negative, and borderline examples.
- Document tie-breaking rules.
- Explain when annotators should abstain, skip, or escalate.
- Keep version history when guidelines change.
- Avoid relying on tribal knowledge that cannot be audited later.

## 3. Calibrate Before Production Labeling

Calibration should happen before large-scale labeling begins.

- Run a small pilot batch with multiple annotators.
- Review disagreements in a structured meeting or written adjudication pass.
- Update guidelines before scaling up.
- Track whether disagreement comes from unclear instructions, ambiguous examples, or annotator mistakes.

## 4. Measure Agreement Carefully

Agreement metrics are useful, but they are not the full quality story.

- Use Cohen's kappa for two annotators when labels are categorical.
- Use Fleiss' kappa or Krippendorff's alpha for multiple annotators or more complex settings.
- Report raw agreement alongside chance-corrected metrics.
- Segment agreement by label, language, domain, source, and task type.
- Treat low agreement as a signal to inspect the task, not as proof that annotators are careless.

## 5. Adjudicate Disagreements

Adjudication should create better labels and better guidelines.

- Use senior reviewers or domain reviewers for high-impact disagreements.
- Record the adjudicated label and the reason for the decision.
- Feed recurring disagreement patterns back into guideline updates.
- Keep unresolved or ambiguous examples marked instead of forcing false certainty.

## 6. Watch for Reviewer Drift

Annotator and reviewer behavior changes over time.

- Reuse a small set of calibration examples across batches.
- Monitor label distribution shifts by annotator and time period.
- Review sudden changes in skip rate, tie rate, or positive-label rate.
- Rotate quality checks rather than relying on one static gold set forever.

## 7. Preference Data Specific Checks

Preference data has its own failure modes.

- Randomize response order where possible.
- Track position bias, verbosity bias, style bias, and safety-policy leakage.
- Define how to handle ties and both-bad examples.
- Keep rejected responses available when the license and privacy constraints allow it.
- Separate preference labels from explanation text when training methods require it.

## 8. Financial-domain Cautions

Financial-domain annotation needs extra care.

- Avoid private customer data, account data, transaction data, and internal documents.
- Separate factual extraction from investment interpretation.
- Require source evidence for answers based on filings or reports.
- Escalate ambiguous regulatory or compliance examples to qualified reviewers.
- Do not treat annotation agreement as proof that a model is safe for production use.

## 9. Minimal Quality Artifacts

For each annotation project, keep:

- guideline version.
- task definition.
- label schema.
- pilot results.
- agreement report.
- adjudication notes.
- known limitations.
- data access and privacy notes.

## 10. Review Outcome

Use operational decisions instead of vague quality labels:

- **Ready to use**: guidelines, agreement, adjudication, and known limitations are documented.
- **Use with constraints**: data is useful but has known ambiguity, coverage, or reviewer limitations.
- **Revise guidelines**: disagreement is driven by unclear instructions or missing examples.
- **Do not use**: privacy risk, unstable labels, unclear provenance, or unresolved high-impact ambiguity.

