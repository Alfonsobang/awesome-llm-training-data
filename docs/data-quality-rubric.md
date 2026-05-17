# LLM Training Data Quality Rubric

This rubric is a practical checklist for reviewing public LLM training, tuning, preference, synthetic, or evaluation datasets. It is not a substitute for legal, privacy, security, or compliance review.

## 1. Provenance

- Is the data source clearly documented?
- Are collection dates, source types, and major filtering steps described?
- Are licenses, terms of use, or redistribution constraints visible?
- Are there known gaps between the public dataset description and the actual files?

## 2. Representativeness

- Does the dataset match the intended language, domain, task, and user context?
- Are important subdomains or edge cases missing?
- Are data sources over-concentrated in a small number of websites, publishers, tasks, or annotator groups?
- Is the dataset being used outside the context it was collected for?

## 3. Contamination and Leakage

- Could evaluation examples appear in training data?
- Are benchmark questions, answer keys, or explanations duplicated across splits?
- Are synthetic examples derived from held-out evaluation sets?
- Are train, validation, and test splits separated by source, time, entity, or document family when needed?

## 4. Deduplication

- Was exact deduplication performed?
- Was near-duplicate detection performed at document, passage, or example level?
- Are boilerplate, templates, repeated disclaimers, and crawler artifacts handled?
- Does deduplication preserve important rare examples instead of removing them blindly?

## 5. Annotation Quality

- Are annotation guidelines public or at least summarized?
- Are annotator qualifications, calibration steps, and adjudication rules described?
- Are inter-annotator agreement or disagreement patterns reported when relevant?
- Are ambiguous or low-confidence labels kept, removed, or marked?

## 6. Preference Data Quality

- Are prompts, candidate responses, preference labels, and tie/skip rules clearly defined?
- Are preference judgments calibrated across annotators or model judges?
- Is there evidence of position bias, verbosity bias, style bias, or safety-policy leakage?
- Are rejected responses available and usable under the dataset license?

## 7. Synthetic Data Quality

- Are generator models, prompts, sampling settings, and filtering steps documented?
- Is synthetic data mixed with human-written data in a traceable way?
- Are generated examples checked for factuality, diversity, duplication, and policy leakage?
- Is synthetic data used to evaluate models that may have generated it?

## 8. Privacy and Compliance

- Is personal data detection, redaction, or anonymization described?
- Are sensitive attributes, financial records, account data, or private conversations excluded?
- Are jurisdiction-specific privacy and data-export constraints considered?
- Is there a process for takedown, correction, or dataset deprecation?

## 9. Documentation and Maintenance

- Does the dataset have a dataset card, datasheet, README, or metadata file?
- Are version changes documented?
- Are known limitations stated plainly?
- Is there an issue tracker, maintainer contact, or update policy?

## 10. Operational Fit

- Can the dataset be loaded reproducibly?
- Are schemas, fields, and file formats stable?
- Are examples inspectable without special private tooling?
- Are compute, storage, and access requirements realistic for the intended team?

## Suggested Review Outcome

Use a simple decision instead of a vague quality score:

- **Use**: suitable for the intended public or internal experiment.
- **Use with constraints**: suitable only with documented filtering, privacy review, or evaluation caveats.
- **Review further**: promising but missing key provenance, license, privacy, or quality information.
- **Do not use**: unclear rights, private data risk, severe contamination, or low relevance to the task.

