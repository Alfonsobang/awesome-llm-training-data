# Awesome LLM Training Data & Agent Evaluation

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Markdown Links](https://github.com/Alfonsobang/awesome-llm-training-data/actions/workflows/link-check.yml/badge.svg)](https://github.com/Alfonsobang/awesome-llm-training-data/actions/workflows/link-check.yml)
[![Resource Audit](https://github.com/Alfonsobang/awesome-llm-training-data/actions/workflows/resource-audit.yml/badge.svg)](https://github.com/Alfonsobang/awesome-llm-training-data/actions/workflows/resource-audit.yml)
[![Financial Agent Seed](https://github.com/Alfonsobang/awesome-llm-training-data/actions/workflows/financial-agent-seed.yml/badge.svg)](https://github.com/Alfonsobang/awesome-llm-training-data/actions/workflows/financial-agent-seed.yml)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE.md)

A curated list of tools, papers, datasets, and best practices for LLM training data quality, annotation, preference data, synthetic data, data governance, and evaluation.

2026 focus: agent evaluation, trajectory-aware grading, Claw-style benchmarks, Harbor workflows, and the data evidence needed to make agent results auditable.

Built for practitioners who need to choose, audit, or govern LLM datasets and agent evaluation data. This is not a general AI bookmark dump.

Use this repo to:

- Find public tools for cleaning, deduplication, inspection, annotation, preference data, synthetic data, and RAG evaluation.
- Compare dataset-quality and governance references before building internal data pipelines.
- Locate public financial-domain LLM benchmarks and datasets without mixing in private or proprietary material.
- Track the fast-moving agent evaluation stack: Harbor, Claw-style trajectory scoring, repeated-trial metrics, and process-safety evidence.

Star this repo if you care about:

- Agent evaluation that inspects trajectories, not just final answers.
- Data quality and governance for training, tuning, preference, synthetic, RAG, and evaluation datasets.
- Practical examples that real LLM data and evaluation teams can reuse.

English first. Complete Chinese version: [README.zh-CN.md](README.zh-CN.md).

> Disclaimer: This repository does not contain private company data, real user data, or proprietary workflows.

## 2026 Agent Evaluation Radar

The hottest evaluation shift right now is from static answer grading to trajectory-aware agent evaluation: repeated attempts, process safety, verifier evidence, artifacts, and auditable traces.

- Start with the [2026 Agent Evaluation Radar](docs/2026-agent-evaluation-radar.md).
- Explore the [Financial Agent Evaluation Agenda](docs/financial-agent-evaluation-agenda.md).
- Inspect the [Financial Agent Evaluation Seed](examples/financial-agent-eval-seed).
- Review the [Financial Agent Evaluation Roadmap](docs/financial-agent-evaluation-roadmap.md).
- Adapt the [Harbor-style financial filing task template](examples/financial-agent-eval-seed/harbor-template/filing-margin-explanation).
- Read the [Claw-style Agent Evaluation Notes](docs/claw-style-agent-evaluation-notes.md).
- Try the [Harbor repeated-trial metric example](examples/harbor-repeated-trial-metric).
- Follow the upstream Harbor discussion: [harbor-framework/harbor#1700](https://github.com/harbor-framework/harbor/issues/1700).
- Share the repo using the [Launch and Share Kit](docs/launch-and-share-kit.md).
- Share the finance track using the [Financial Agent Evaluation Share Kit](docs/financial-agent-evaluation-share-kit.md).
- Start a community thread with the [Agent Evaluation Discussion Seed](docs/discussion-seed-agent-evaluation.md).

## Why Training Data Quality Deserves First-Class Engineering

LLM behavior is shaped as much by data decisions as by model architecture. Data collection, filtering, annotation, preference modeling, evaluation design, privacy review, and governance all create production risk when treated as ad hoc work. Training data quality deserves first-class engineering because it determines reproducibility, safety, domain reliability, evaluation validity, and whether teams can explain what changed when model behavior changes.

## Scope

This list focuses on public resources that help teams engineer, evaluate, document, or govern LLM training and evaluation data. It does not rank vendors, recommend private datasets, publish internal playbooks, or treat popularity as proof of quality.

## Financial and Regulated-Domain Note

Financial-domain resources should be public, reproducible, and useful for evaluation or data engineering. This list avoids investment advice, trading signals, private business data, and claims that a benchmark or dataset proves production readiness.

## Quality Bar

- No fake links.
- No private or proprietary resources.
- No low-quality SEO content.
- Prefer active and reproducible resources.
- Prefer resources useful to real LLM data teams.
- Prefer primary sources, official repositories, dataset cards, papers, and standards.
- Include a resource only when its relevance to LLM data engineering is clear.
- Include access, license, or usage constraints in the description when they are material.

The repository also runs a lightweight [resource audit](tools/audit_resources.py) to check resource format, allowed tags, placeholder links, duplicate-link risk, and English/Chinese resource-count consistency.

## Contents

- [Scope](#scope)
- [2026 Agent Evaluation Radar](#2026-agent-evaluation-radar)
- [Financial and Regulated-Domain Note](#financial-and-regulated-domain-note)
- [Start Here](#start-here)
- [Training Data Quality](#training-data-quality)
- [Data Cleaning and Deduplication](#data-cleaning-and-deduplication)
- [Dataset Inspection Tools](#dataset-inspection-tools)
- [Annotation Platforms](#annotation-platforms)
- [Annotation Quality and Agreement](#annotation-quality-and-agreement)
- [Human Preference Data](#human-preference-data)
- [RLHF / DPO / RLAIF Data](#rlhf--dpo--rlaif-data)
- [Synthetic Data](#synthetic-data)
- [RAG Evaluation Data](#rag-evaluation-data)
- [Agent Evaluation and Trajectory Data](#agent-evaluation-and-trajectory-data)
- [Financial Agent Evaluation](#financial-agent-evaluation)
- [Financial-domain LLM Data](#financial-domain-llm-data)
- [Practitioner Guides](#practitioner-guides)
- [Data Governance](#data-governance)
- [Privacy and Compliance](#privacy-and-compliance)
- [Papers](#papers)
- [Open-source Tools](#open-source-tools)
- [Reports and Playbooks](#reports-and-playbooks)
- [Contributing](#contributing)
- [License](#license)

## Start Here

- [DataPerf](https://github.com/mlcommons/dataperf) - Tag: [benchmark] - MLCommons benchmark suite focused on measuring the impact of data quality and data-centric ML work.
- [DataComp-LM](https://github.com/mlfoundations/dclm) - Tag: [benchmark] - A data-centric benchmark for studying how language-model pretraining data choices affect downstream results.
- [Hugging Face Datasets](https://huggingface.co/docs/datasets) - Tag: [tool] - Core library and documentation for loading, processing, sharing, and versioning datasets.
- [The Pile](https://arxiv.org/abs/2101.00027) - Tag: [paper] - Paper describing a large open text corpus and practical dataset composition decisions.
- [Data-Centric AI Resources](https://github.com/daochenzha/data-centric-AI) - Tag: [report] - A curated list of data-centric AI papers, tools, and benchmarks.

## Training Data Quality

- [Data-Juicer](https://github.com/modelscope/data-juicer) - Tag: [tool] - Open-source toolkit for analyzing, filtering, and processing large multimodal and text datasets.
- [FineWeb](https://huggingface.co/datasets/HuggingFaceFW/fineweb) - Tag: [dataset] - A large open web dataset with transparent processing choices for LLM pretraining research.
- [FineWeb-Edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu) - Tag: [dataset] - A filtered educational subset of FineWeb useful for studying quality-oriented corpus selection.
- [Dolma](https://huggingface.co/datasets/allenai/dolma) - Tag: [dataset] - An open corpus from AI2 designed to support reproducible language-model pretraining research.
- [RefinedWeb](https://arxiv.org/abs/2306.01116) - Tag: [paper] - Paper describing web-scale filtering and corpus construction choices behind the RefinedWeb dataset.
- [DataComp-LM Paper](https://arxiv.org/abs/2406.11794) - Tag: [paper] - Paper framing LLM pretraining data selection as a controlled benchmark problem.

## Data Cleaning and Deduplication

- [DataTrove](https://github.com/huggingface/datatrove) - Tag: [tool] - Hugging Face processing library for large-scale web data extraction, filtering, and deduplication.
- [text-dedup](https://github.com/ChenghaoMou/text-dedup) - Tag: [tool] - Toolkit for exact, near, and semantic deduplication of text datasets.
- [datasketch](https://github.com/ekzhu/datasketch) - Tag: [tool] - Python library for MinHash, LSH, and other probabilistic data structures often used in near-dedup pipelines.
- [Trafilatura](https://github.com/adbar/trafilatura) - Tag: [tool] - Web text extraction library useful for turning HTML pages into cleaner text before dataset filtering.
- [jusText](https://github.com/miso-belica/jusText) - Tag: [tool] - Boilerplate-removal library for extracting main textual content from web pages.
- [tiktoken](https://github.com/openai/tiktoken) - Tag: [tool] - Fast tokenizer library useful for estimating token distributions, truncation behavior, and corpus size.

## Dataset Inspection Tools

- [Lilac](https://github.com/lilacai/lilac) - Tag: [tool] - Dataset exploration tool for clustering, searching, labeling, and inspecting large text datasets.
- [Renumics Spotlight](https://github.com/Renumics/spotlight) - Tag: [tool] - Interactive tool for exploring embeddings, metadata, labels, and dataset slices.
- [FiftyOne](https://github.com/voxel51/fiftyone) - Tag: [tool] - Dataset visualization and curation platform especially useful for multimodal and vision-language data.
- [Cleanlab](https://github.com/cleanlab/cleanlab) - Tag: [tool] - Library for finding label issues, outliers, and data quality problems in ML datasets.
- [whylogs](https://github.com/whylabs/whylogs) - Tag: [tool] - Data profiling library for tracking dataset statistics and drift over time.
- [Evidently](https://github.com/evidentlyai/evidently) - Tag: [tool] - Open-source evaluation and monitoring toolkit for data and model quality reports.

## Annotation Platforms

- [Label Studio](https://github.com/HumanSignal/label-studio) - Tag: [platform] - Open-source data labeling platform supporting text, image, audio, and multimodal workflows.
- [Argilla](https://github.com/argilla-io/argilla) - Tag: [platform] - Open-source platform for human and LLM feedback workflows, dataset curation, and preference data.
- [Doccano](https://github.com/doccano/doccano) - Tag: [platform] - Open-source annotation tool for text classification, sequence labeling, and sequence-to-sequence tasks.
- [INCEpTION](https://github.com/inception-project/inception) - Tag: [platform] - Semantic annotation platform with support for knowledge-oriented and NLP annotation projects.
- [Label Sleuth](https://github.com/label-sleuth/label-sleuth) - Tag: [platform] - Open-source no-code text classification labeling tool with active learning workflows.

## Annotation Quality and Agreement

- [Cleanlab](https://github.com/cleanlab/cleanlab) - Tag: [tool] - Useful for surfacing likely label errors and prioritizing review work in annotated datasets.
- [NLTK Agreement](https://www.nltk.org/api/nltk.metrics.agreement.html) - Tag: [tool] - NLTK module for calculating inter-annotator agreement measures.
- [scikit-learn Cohen Kappa](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html) - Tag: [tool] - Reference implementation for Cohen's kappa, a common pairwise agreement metric.
- [statsmodels Fleiss Kappa](https://www.statsmodels.org/stable/generated/statsmodels.stats.inter_rater.fleiss_kappa.html) - Tag: [tool] - Implementation of Fleiss' kappa for agreement across multiple annotators.
- [fast-krippendorff](https://github.com/pln-fing-udelar/fast-krippendorff) - Tag: [tool] - Fast implementation of Krippendorff's alpha for measuring annotation reliability.

## Human Preference Data

- [Anthropic HH-RLHF](https://huggingface.co/datasets/Anthropic/hh-rlhf) - Tag: [dataset] - Human preference dataset for helpful and harmless assistant behavior research.
- [OpenAI summarize_from_feedback](https://huggingface.co/datasets/openai/summarize_from_feedback) - Tag: [dataset] - Human feedback data for training and evaluating summarization preference models.
- [OpenAI WebGPT Comparisons](https://huggingface.co/datasets/openai/webgpt_comparisons) - Tag: [dataset] - Comparison data collected for web-browsing question-answering model research.
- [Stanford Human Preferences](https://huggingface.co/datasets/stanfordnlp/SHP) - Tag: [dataset] - Preference dataset built from naturally occurring Reddit question-answer interactions.
- [Chatbot Arena Conversations](https://huggingface.co/datasets/lmsys/chatbot_arena_conversations) - Tag: [dataset] - Public conversation data from Chatbot Arena useful for studying comparative human judgments.
- [RewardBench](https://github.com/allenai/reward-bench) - Tag: [benchmark] - Benchmark for evaluating reward models used in preference optimization pipelines.

## RLHF / DPO / RLAIF Data

- [UltraFeedback](https://huggingface.co/datasets/openbmb/UltraFeedback) - Tag: [dataset] - Large-scale AI feedback dataset commonly used for instruction tuning and preference optimization.
- [Argilla UltraFeedback Binarized Preferences](https://huggingface.co/datasets/argilla/ultrafeedback-binarized-preferences) - Tag: [dataset] - Processed preference-pair version of UltraFeedback for DPO-style training.
- [TRL](https://github.com/huggingface/trl) - Tag: [tool] - Training library for SFT, reward modeling, PPO, DPO, and related preference optimization workflows.
- [OpenRLHF](https://github.com/OpenRLHF/OpenRLHF) - Tag: [tool] - Open-source RLHF framework covering reward modeling and alignment training pipelines.
- [Direct Preference Optimization](https://arxiv.org/abs/2305.18290) - Tag: [paper] - Paper introducing DPO, a widely used method for training directly from preference pairs.
- [Constitutional AI](https://arxiv.org/abs/2212.08073) - Tag: [paper] - Paper introducing a framework for using principles and AI feedback to reduce reliance on direct human labels.

## Synthetic Data

- [Self-Instruct](https://github.com/yizhongw/self-instruct) - Tag: [tool] - Repository for generating instruction-following data from language models with bootstrapped prompts.
- [distilabel](https://github.com/argilla-io/distilabel) - Tag: [tool] - Framework for building synthetic data and AI feedback pipelines with reproducible workflows.
- [DSPy](https://github.com/stanfordnlp/dspy) - Tag: [tool] - Programming framework that can optimize prompts and generate training/evaluation data for LM systems.
- [Awesome Synthetic Datasets](https://github.com/davanstrien/awesome-synthetic-datasets) - Tag: [report] - Curated list of synthetic datasets and generation resources across text and multimodal tasks.
- [Self-Instruct Paper](https://arxiv.org/abs/2212.10560) - Tag: [paper] - Paper describing bootstrapped instruction generation for aligning language models.
- [WizardLM / Evol-Instruct](https://arxiv.org/abs/2304.12244) - Tag: [paper] - Paper describing evol-instruct style generation for creating complex instruction data.

## RAG Evaluation Data

- [Ragas](https://github.com/explodinggradients/ragas) - Tag: [tool] - Evaluation framework for RAG systems with metrics for retrieval and generation quality.
- [DeepEval](https://github.com/confident-ai/deepeval) - Tag: [tool] - Open-source evaluation framework that supports RAG, LLM, and agent evaluation workflows.
- [BEIR](https://github.com/beir-cellar/beir) - Tag: [benchmark] - Retrieval benchmark suite often used to evaluate document ranking and search components.
- [KILT](https://github.com/facebookresearch/KILT) - Tag: [benchmark] - Knowledge-intensive language task benchmark connecting tasks to provenance-bearing corpora.
- [HotpotQA](https://hotpotqa.github.io/) - Tag: [dataset] - Multi-hop question-answering dataset useful for retrieval and evidence-chain evaluation.
- [Natural Questions](https://ai.google.com/research/NaturalQuestions) - Tag: [dataset] - Open-domain question-answering dataset frequently used in retrieval and QA evaluation.

## Agent Evaluation and Trajectory Data

- [Harbor](https://github.com/harbor-framework/harbor) - Tag: [tool] - Framework for running agent evaluations, collecting trajectories, and creating RL environments in sandboxed settings.
- [Claw-Eval](https://github.com/claw-eval/claw-eval) - Tag: [benchmark] - Autonomous-agent evaluation suite emphasizing trajectory-aware grading, safety assessment, and repeated-trial robustness.
- [Terminal-Bench](https://github.com/laude-institute/terminal-bench) - Tag: [benchmark] - Benchmark for evaluating agents on terminal-based tasks with executable environments and verifiers.
- [SWE-Bench](https://github.com/swe-bench/SWE-bench) - Tag: [benchmark] - Software engineering benchmark for evaluating agents on real GitHub issue resolution tasks.
- [WebArena](https://github.com/web-arena-x/webarena) - Tag: [benchmark] - Web-based agent benchmark for evaluating interactive task completion in simulated websites.
- [OSWorld](https://github.com/xlang-ai/OSWorld) - Tag: [benchmark] - Computer-use benchmark for evaluating multimodal agents in desktop operating-system environments.

## Financial Agent Evaluation

- [FinToolBench](https://github.com/Double-wk/FinToolBench) - Tag: [benchmark] - Runnable benchmark for evaluating financial tool-use agents across realistic task and regulatory-alignment dimensions.
- [Finance Agent Benchmark](https://arxiv.org/abs/2508.00828) - Tag: [paper] - Benchmark paper focused on real-world financial research tasks for LLM-driven finance agents.
- [FinAgentBench](https://arxiv.org/abs/2508.14052) - Tag: [paper] - Benchmark paper for agentic retrieval in financial question answering with multi-step reasoning.
- [QFBench](https://www.qfbench.com/) - Tag: [benchmark] - Quantitative finance benchmark for evaluating agents that write and execute numerical finance code.
- [CryptoBench](https://cryptobench.space/) - Tag: [benchmark] - Dynamic benchmark for expert-level crypto and market-intelligence agent workflows.
- [OpenBB](https://github.com/openbb-finance/OpenBB) - Tag: [tool] - Open-source financial data platform useful for building public-data lookup and analysis agents.
- [FinRL](https://github.com/AI4Finance-Foundation/FinRL) - Tag: [tool] - Open-source framework for financial reinforcement learning, market environments, and backtesting-style workflows.

## Financial-domain LLM Data

- [FinEval](https://github.com/SUFE-AIFLM-Lab/FinEval) - Tag: [benchmark] - Chinese financial-domain benchmark for evaluating LLM financial knowledge and safety.
- [PIXIU / FinBen](https://github.com/The-FinAI/PIXIU) - Tag: [benchmark] - Financial LLM benchmark and framework covering multiple financial tasks and datasets.
- [FinGPT](https://github.com/AI4Finance-Foundation/FinGPT) - Tag: [tool] - Open-source project for financial LLM research, data pipelines, and domain adaptation.
- [FinNLP](https://github.com/AI4Finance-Foundation/FinNLP) - Tag: [tool] - Financial NLP toolkit for collecting and processing finance-related text data.
- [FinanceBench](https://github.com/patronus-ai/financebench) - Tag: [benchmark] - Benchmark for evaluating LLM performance on financial question-answering tasks grounded in public filings.
- [FinQA](https://github.com/czyssrs/FinQA) - Tag: [dataset] - Dataset for numerical reasoning over financial reports.
- [TAT-QA](https://github.com/NExTplusplus/TAT-QA) - Tag: [dataset] - Table-and-text question-answering dataset built around hybrid reasoning over financial reports.

## Practitioner Guides

- [Claw-style Agent Evaluation Notes](docs/claw-style-agent-evaluation-notes.md) - Notes on trajectory-aware grading, repeated trials, safety evidence, and how Harbor maps to this evaluation pattern.
- [Financial Agent Evaluation Agenda](docs/financial-agent-evaluation-agenda.md) - A large-topic agenda for financial search, data lookup, backtesting, forecasting, compliance, and evidence-grounded agent evaluation.
- [Financial Agent Evaluation Seed](examples/financial-agent-eval-seed) - Public-data-only task specs, dataset card, and trajectory-safety rubric for a finance-focused agent benchmark seed.
- [Financial Agent Evaluation Roadmap](docs/financial-agent-evaluation-roadmap.md) - A staged public roadmap for turning the seed into a credible financial agent evaluation track.
- [Harbor-style Financial Filing Task Template](examples/financial-agent-eval-seed/harbor-template/filing-margin-explanation) - A runnable-style task scaffold with synthetic fixture data, JSON evidence, and deterministic verifier tests.
- [Financial Agent Evaluation Share Kit](docs/financial-agent-evaluation-share-kit.md) - Short English and Chinese copy for introducing the finance-focused evaluation track.
- [Harbor Repeated-trial Metric Example](examples/harbor-repeated-trial-metric) - A small `metric.py` example for reporting mean reward, pass@k, Pass^k, and missing-evidence rate.
- [LLM Training Data Operating Model](docs/llm-training-data-operating-model.md) - A practical operating loop for source review, profiling, filtering, annotation, evaluation, release, and governance.
- [LLM Training Data Quality Rubric](docs/data-quality-rubric.md) - A practical checklist for reviewing public LLM training, tuning, preference, synthetic, or evaluation datasets.
- [Financial-domain LLM Evaluation Checklist](docs/financial-domain-llm-evaluation-checklist.md) - A governance-oriented checklist for financial-domain LLM evaluation without private data or investment claims.
- [Annotation Quality and Adjudication Guide](docs/annotation-quality-guide.md) - A practical guide for calibration, agreement, adjudication, reviewer drift, and preference-data annotation quality.
- [Preference Data Quality Checklist](docs/preference-data-quality-checklist.md) - A review checklist for human preference data, AI feedback data, and DPO/RLHF dataset suitability.
- [Financial-domain Benchmark Inclusion Criteria](docs/financial-benchmark-inclusion-criteria.md) - Conservative criteria for including financial-domain LLM benchmarks and datasets.
- [Upstream Contribution Shortlist](docs/upstream-contribution-shortlist.md) - A conservative plan for useful future contributions to public LLM data-quality projects.

## Data Governance

- [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) - Tag: [paper] - Foundational paper proposing structured documentation for dataset motivation, composition, collection, and maintenance.
- [Data Cards Playbook](https://pair-code.github.io/datacardsplaybook/) - Tag: [report] - Practical guide for documenting datasets in a consistent and responsible way.
- [Croissant](https://github.com/mlcommons/croissant) - Tag: [governance] - MLCommons metadata format for machine learning datasets.
- [DataHub](https://github.com/datahub-project/datahub) - Tag: [tool] - Open-source metadata platform for dataset discovery, lineage, and governance.
- [OpenMetadata](https://github.com/open-metadata/OpenMetadata) - Tag: [tool] - Open-source metadata and governance platform for data assets.
- [DVC](https://github.com/iterative/dvc) - Tag: [tool] - Data versioning and pipeline tool useful for reproducible dataset releases.

## Privacy and Compliance

- [Microsoft Presidio](https://github.com/microsoft/presidio) - Tag: [tool] - Open-source framework for detecting and anonymizing personally identifiable information.
- [scrubadub](https://github.com/LeapBeyond/scrubadub) - Tag: [tool] - Python library for removing personally identifiable information from free text.
- [LLM Guard](https://github.com/protectai/llm-guard) - Tag: [tool] - Toolkit for input/output scanning, including sensitive-data and prompt-risk checks.
- [Google Differential Privacy](https://github.com/google/differential-privacy) - Tag: [tool] - Libraries and tools for building differentially private data analysis workflows.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Tag: [governance] - Risk management framework relevant to AI system governance and documentation.
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) - Tag: [governance] - Security and risk reference for LLM application development and deployment.

## Papers

- [Training Language Models to Follow Instructions with Human Feedback](https://arxiv.org/abs/2203.02155) - Tag: [paper] - InstructGPT paper connecting supervised data, preference data, and RLHF.
- [Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2204.05862) - Tag: [paper] - Paper describing preference data and RLHF training for assistant behavior.
- [Deduplicating Training Data Makes Language Models Better](https://arxiv.org/abs/2107.06499) - Tag: [paper] - Study showing why training-data duplication matters for language model behavior.
- [LIMA: Less Is More for Alignment](https://arxiv.org/abs/2305.11206) - Tag: [paper] - Paper studying how small, carefully curated supervised datasets can affect alignment behavior.
- [The BigScience ROOTS Corpus](https://arxiv.org/abs/2303.03915) - Tag: [paper] - Documentation of the multilingual corpus used to train BLOOM, including governance and sourcing details.
- [Direct Preference Optimization](https://arxiv.org/abs/2305.18290) - Tag: [paper] - Preference optimization paper focused on training from pairwise preference data.

## Open-source Tools

- [Hugging Face Datasets](https://github.com/huggingface/datasets) - Tag: [tool] - Library for dataset loading, transformation, streaming, and sharing.
- [DataTrove](https://github.com/huggingface/datatrove) - Tag: [tool] - Large-scale text data processing framework for LLM corpus preparation.
- [Data-Juicer](https://github.com/modelscope/data-juicer) - Tag: [tool] - Data processing and quality-analysis toolkit for LLM and multimodal data.
- [Dolma Toolkit](https://github.com/allenai/dolma) - Tag: [tool] - AI2 toolkit for building and analyzing large pretraining corpora.
- [Label Studio](https://github.com/HumanSignal/label-studio) - Tag: [platform] - General-purpose open-source annotation platform for multimodal labeling workflows.
- [Argilla](https://github.com/argilla-io/argilla) - Tag: [platform] - Feedback and annotation platform for LLM data workflows.
- [Ragas](https://github.com/explodinggradients/ragas) - Tag: [tool] - RAG evaluation library for retrieval and generation metrics.
- [TRL](https://github.com/huggingface/trl) - Tag: [tool] - Preference optimization and alignment training library.

## Reports and Playbooks

- [Data Cards Playbook](https://pair-code.github.io/datacardsplaybook/) - Tag: [report] - Practical playbook for transparent dataset documentation.
- [HELM](https://crfm.stanford.edu/helm/latest/) - Tag: [benchmark] - Holistic evaluation framework and reports for language model evaluation.
- [NIST AI RMF Playbook](https://airc.nist.gov/AI_RMF_Knowledge_Base/Playbook) - Tag: [report] - Operational playbook for applying the NIST AI Risk Management Framework.
- [FineWeb Blog](https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1) - Tag: [report] - Hugging Face write-up explaining the design and filtering choices behind FineWeb.
- [The Turing Way: Research Data Management](https://book.the-turing-way.org/reproducible-research/rdm/rdm-data/) - Tag: [report] - Practical guide to reproducible research data management.

## Contributing

Contributions are welcome if they meet the [Quality Bar](#quality-bar). Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or pull request.

## License

This repository is licensed under [CC BY 4.0](LICENSE.md). Linked third-party resources keep their own licenses and terms.
