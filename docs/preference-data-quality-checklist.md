# Preference Data Quality Checklist

Preference data is not just a table of prompts, chosen responses, and rejected responses. It is a measurement system for human or AI judgments, and the quality of that system affects reward models, DPO-style training, evaluation, and downstream model behavior.

This checklist is for reviewing public preference datasets and preference-data pipelines. It does not include private company data, real user data, or proprietary review workflows.

## 1. Dataset Structure

- Are prompts, candidate responses, preference labels, and metadata clearly separated?
- Are chosen and rejected responses both available?
- Are ties, skips, and both-bad cases represented or documented?
- Are conversation turns, system messages, and tool outputs preserved when they affect the judgment?

## 2. Source and Provenance

- Is the source of prompts documented?
- Are response generators identified when responses are model-generated?
- Are collection dates or dataset versions available?
- Are licenses, access terms, or redistribution limits stated?

## 3. Judgment Design

- Is the preference question explicit?
- Are annotators judging helpfulness, harmlessness, correctness, style, factuality, safety, or overall preference?
- Are judgments single-turn or conversation-level?
- Are annotators allowed to use external evidence?

## 4. Bias Checks

- Was response order randomized?
- Is there a risk of position bias?
- Is there a risk of verbosity bias?
- Is there a risk of style bias, such as preferring confident or polished writing over correct writing?
- Is there a risk that safety-policy wording leaks into labels instead of measuring actual answer quality?

## 5. Annotation Quality

- Are guidelines public or summarized?
- Are annotator qualifications and calibration steps described?
- Are disagreement and adjudication rules documented?
- Are low-confidence judgments marked or removed?
- Are label distributions reported by task type, language, or domain?

## 6. AI Feedback and RLAIF

- If judgments come from models, are model names, prompts, and sampling settings documented?
- Are model-judge outputs validated against human judgments?
- Are known judge biases discussed?
- Are generated critiques separated from final labels?
- Is there a risk that the trained model learns the judge's style rather than the target behavior?

## 7. Training Suitability

- Is the dataset appropriate for SFT, reward modeling, DPO, evaluation, or analysis?
- Are prompts duplicated across train and evaluation splits?
- Are rejected responses realistic enough to teach useful preferences?
- Are examples filtered for privacy, toxicity, policy leakage, and malformed text?
- Are domain-specific examples separated when they require expert review?

## 8. Financial-domain Cautions

- Avoid preference data that includes private financial records, customer conversations, account activity, or transaction details.
- Separate factual correctness from investment advice or risk preference.
- Require source-grounded review when responses discuss filings, earnings, regulations, or market events.
- Do not use preference labels as proof that a model is safe for financial production use.

## 9. Minimal Documentation

For each preference dataset, record:

- dataset source.
- license and access terms.
- prompt source.
- response source.
- judgment criteria.
- annotator or judge type.
- tie and skip policy.
- known limitations.
- recommended use and non-use cases.

## Review Decision

- **Use**: source, license, judgment design, and limitations are clear.
- **Use with constraints**: useful data, but access, domain, or label-quality caveats must be documented.
- **Review further**: missing provenance, judge details, or annotation guidance.
- **Do not use**: unclear rights, privacy risk, severe label ambiguity, or no usable documentation.

