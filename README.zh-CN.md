# Awesome LLM Training Data

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Markdown Links](https://github.com/Alfonsobang/awesome-llm-training-data/actions/workflows/link-check.yml/badge.svg)](https://github.com/Alfonsobang/awesome-llm-training-data/actions/workflows/link-check.yml)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE.md)

一个面向 LLM 训练数据工程的精选资源列表，覆盖数据质量、标注、偏好数据、合成数据、数据治理、隐私合规与评测。

本项目面向需要选择、审计或治理 LLM 数据集的实践者，不是泛泛的 AI 资料收藏夹。

你可以用它来：

- 查找用于清洗、去重、检查、标注、偏好数据、合成数据和 RAG 评测的公开工具。
- 在建设内部数据流水线前，对比数据质量与治理方面的公开参考。
- 查找公开的金融领域 LLM 基准和数据集，同时避免混入私有或专有材料。

英文主文档：[README.md](README.md)。

> 免责声明：This repository does not contain private company data, real user data, or proprietary workflows.

## 为什么训练数据质量需要一流工程能力

LLM 的行为不仅由模型结构决定，也强烈受数据决策影响。数据采集、清洗、去重、标注、偏好建模、评测设计、隐私审查和治理流程，如果只被当作临时性工作，就会带来可复现性、安全性、领域可靠性和评测有效性的风险。训练数据质量需要一流工程能力，因为当模型行为发生变化时，团队必须能够解释数据发生了什么变化、为什么变化、以及这些变化是否可信。

## 范围

本列表聚焦能够帮助团队建设、评测、文档化或治理 LLM 训练与评测数据的公开资源。本项目不做厂商排名，不推荐私有数据集，不发布内部流程，也不把流行度等同于质量。

## 金融与强监管领域说明

金融领域资源应当是公开、可复现，并且对评测或数据工程有实际帮助的。本列表不收录投资建议、交易信号、私有业务数据，也不声称某个基准或数据集能够证明模型具备生产可用性。

## 质量门槛

- 不接受虚假链接。
- 不收录私有或专有资源。
- 不收录低质量 SEO 内容。
- 优先收录活跃、可复现的资源。
- 优先收录对真实 LLM 数据团队有用的资源。
- 优先收录一手来源、官方仓库、数据集卡、论文和标准。
- 只有当资源与 LLM 数据工程的关系清晰时才收录。
- 如果访问权限、许可证或使用限制会影响实践使用，需要在说明中写清楚。

## 目录

- [范围](#范围)
- [金融与强监管领域说明](#金融与强监管领域说明)
- [入门资源](#入门资源)
- [训练数据质量](#训练数据质量)
- [数据清洗与去重](#数据清洗与去重)
- [数据集检查工具](#数据集检查工具)
- [标注平台](#标注平台)
- [标注质量与一致性](#标注质量与一致性)
- [人类偏好数据](#人类偏好数据)
- [RLHF / DPO / RLAIF 数据](#rlhf--dpo--rlaif-数据)
- [合成数据](#合成数据)
- [RAG 评测数据](#rag-评测数据)
- [金融领域 LLM 数据](#金融领域-llm-数据)
- [实践指南](#实践指南)
- [数据治理](#数据治理)
- [隐私与合规](#隐私与合规)
- [论文](#论文)
- [开源工具](#开源工具)
- [报告与实践手册](#报告与实践手册)
- [贡献指南](#贡献指南)
- [许可证](#许可证)

## 入门资源

- [DataPerf](https://github.com/mlcommons/dataperf) - Tag: [benchmark] - MLCommons 的数据中心化机器学习基准，关注数据质量和数据改进对模型效果的影响。
- [DataComp-LM](https://github.com/mlfoundations/dclm) - Tag: [benchmark] - 用于研究语言模型预训练数据选择如何影响下游效果的数据中心化基准。
- [Hugging Face Datasets](https://huggingface.co/docs/datasets) - Tag: [tool] - 用于加载、处理、分享和版本化数据集的核心库与文档。
- [The Pile](https://arxiv.org/abs/2101.00027) - Tag: [paper] - 描述大型开放文本语料及其数据组成决策的论文。
- [Data-Centric AI Resources](https://github.com/daochenzha/data-centric-AI) - Tag: [report] - 数据中心化 AI 方向的论文、工具和基准精选列表。

## 训练数据质量

- [Data-Juicer](https://github.com/modelscope/data-juicer) - Tag: [tool] - 用于大规模多模态和文本数据分析、过滤与处理的开源工具包。
- [FineWeb](https://huggingface.co/datasets/HuggingFaceFW/fineweb) - Tag: [dataset] - 一个处理流程透明的大规模开放网页数据集，适合 LLM 预训练研究。
- [FineWeb-Edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu) - Tag: [dataset] - FineWeb 的教育内容过滤子集，适合研究面向质量的语料筛选。
- [Dolma](https://huggingface.co/datasets/allenai/dolma) - Tag: [dataset] - AI2 发布的开放语料，支持可复现的语言模型预训练研究。
- [RefinedWeb](https://arxiv.org/abs/2306.01116) - Tag: [paper] - 介绍 RefinedWeb 背后网页级过滤和语料构建策略的论文。
- [DataComp-LM Paper](https://arxiv.org/abs/2406.11794) - Tag: [paper] - 将 LLM 预训练数据选择表述为可控基准问题的论文。

## 数据清洗与去重

- [DataTrove](https://github.com/huggingface/datatrove) - Tag: [tool] - Hugging Face 的大规模网页数据抽取、过滤和去重处理库。
- [text-dedup](https://github.com/ChenghaoMou/text-dedup) - Tag: [tool] - 支持精确、近似和语义去重的文本数据集工具包。
- [datasketch](https://github.com/ekzhu/datasketch) - Tag: [tool] - 提供 MinHash、LSH 等概率数据结构的 Python 库，常用于近似去重流水线。
- [Trafilatura](https://github.com/adbar/trafilatura) - Tag: [tool] - 网页正文抽取库，可在数据过滤前将 HTML 转为更干净的文本。
- [jusText](https://github.com/miso-belica/jusText) - Tag: [tool] - 用于移除网页模板噪声并抽取主体文本的库。
- [tiktoken](https://github.com/openai/tiktoken) - Tag: [tool] - 高性能 tokenizer，可用于估算 token 分布、截断行为和语料规模。

## 数据集检查工具

- [Lilac](https://github.com/lilacai/lilac) - Tag: [tool] - 用于大规模文本数据集聚类、搜索、标注和检查的数据探索工具。
- [Renumics Spotlight](https://github.com/Renumics/spotlight) - Tag: [tool] - 用于交互式探索 embedding、元数据、标签和数据切片的工具。
- [FiftyOne](https://github.com/voxel51/fiftyone) - Tag: [tool] - 数据集可视化与策展平台，尤其适合多模态和视觉语言数据。
- [Cleanlab](https://github.com/cleanlab/cleanlab) - Tag: [tool] - 用于发现标签问题、异常值和数据质量问题的库。
- [whylogs](https://github.com/whylabs/whylogs) - Tag: [tool] - 用于跟踪数据统计特征和漂移的数据画像库。
- [Evidently](https://github.com/evidentlyai/evidently) - Tag: [tool] - 用于生成数据和模型质量报告的开源评测与监控工具包。

## 标注平台

- [Label Studio](https://github.com/HumanSignal/label-studio) - Tag: [platform] - 支持文本、图像、音频和多模态任务的开源数据标注平台。
- [Argilla](https://github.com/argilla-io/argilla) - Tag: [platform] - 面向人工反馈、LLM 反馈、数据策展和偏好数据流程的开源平台。
- [Doccano](https://github.com/doccano/doccano) - Tag: [platform] - 支持文本分类、序列标注和序列到序列任务的开源标注工具。
- [INCEpTION](https://github.com/inception-project/inception) - Tag: [platform] - 支持知识型和 NLP 标注项目的语义标注平台。
- [Label Sleuth](https://github.com/label-sleuth/label-sleuth) - Tag: [platform] - 带有主动学习流程的开源无代码文本分类标注工具。

## 标注质量与一致性

- [Cleanlab](https://github.com/cleanlab/cleanlab) - Tag: [tool] - 可用于发现疑似标签错误，并帮助优先安排标注复核。
- [NLTK Agreement](https://www.nltk.org/api/nltk.metrics.agreement.html) - Tag: [tool] - NLTK 中用于计算标注者一致性指标的模块。
- [scikit-learn Cohen Kappa](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html) - Tag: [tool] - Cohen's kappa 的参考实现，常用于双人标注一致性评估。
- [statsmodels Fleiss Kappa](https://www.statsmodels.org/stable/generated/statsmodels.stats.inter_rater.fleiss_kappa.html) - Tag: [tool] - Fleiss' kappa 的实现，适用于多标注者一致性评估。
- [fast-krippendorff](https://github.com/pln-fing-udelar/fast-krippendorff) - Tag: [tool] - Krippendorff's alpha 的高性能实现，用于衡量标注可靠性。

## 人类偏好数据

- [Anthropic HH-RLHF](https://huggingface.co/datasets/Anthropic/hh-rlhf) - Tag: [dataset] - 用于研究 helpful 和 harmless 助手行为的人类偏好数据集。
- [OpenAI summarize_from_feedback](https://huggingface.co/datasets/openai/summarize_from_feedback) - Tag: [dataset] - 用于训练和评估摘要偏好模型的人类反馈数据。
- [OpenAI WebGPT Comparisons](https://huggingface.co/datasets/openai/webgpt_comparisons) - Tag: [dataset] - 为网页浏览问答模型研究收集的比较数据。
- [Stanford Human Preferences](https://huggingface.co/datasets/stanfordnlp/SHP) - Tag: [dataset] - 基于 Reddit 问答互动构建的自然偏好数据集。
- [Chatbot Arena Conversations](https://huggingface.co/datasets/lmsys/chatbot_arena_conversations) - Tag: [dataset] - 来自 Chatbot Arena 的公开对话数据，可用于研究人类比较判断。
- [RewardBench](https://github.com/allenai/reward-bench) - Tag: [benchmark] - 用于评估偏好优化流水线中奖励模型的基准。

## RLHF / DPO / RLAIF 数据

- [UltraFeedback](https://huggingface.co/datasets/openbmb/UltraFeedback) - Tag: [dataset] - 常用于指令微调和偏好优化的大规模 AI 反馈数据集。
- [Argilla UltraFeedback Binarized Preferences](https://huggingface.co/datasets/argilla/ultrafeedback-binarized-preferences) - Tag: [dataset] - 面向 DPO 等训练方式处理后的 UltraFeedback 偏好对版本。
- [TRL](https://github.com/huggingface/trl) - Tag: [tool] - 支持 SFT、奖励建模、PPO、DPO 等偏好优化流程的训练库。
- [OpenRLHF](https://github.com/OpenRLHF/OpenRLHF) - Tag: [tool] - 覆盖奖励建模和对齐训练流水线的开源 RLHF 框架。
- [Direct Preference Optimization](https://arxiv.org/abs/2305.18290) - Tag: [paper] - 提出 DPO 的论文，是直接使用偏好对进行训练的重要方法。
- [Constitutional AI](https://arxiv.org/abs/2212.08073) - Tag: [paper] - 提出利用原则和 AI 反馈降低对直接人工标签依赖的框架。

## 合成数据

- [Self-Instruct](https://github.com/yizhongw/self-instruct) - Tag: [tool] - 使用自举提示从语言模型生成指令跟随数据的仓库。
- [distilabel](https://github.com/argilla-io/distilabel) - Tag: [tool] - 用于构建可复现合成数据和 AI 反馈流水线的框架。
- [DSPy](https://github.com/stanfordnlp/dspy) - Tag: [tool] - 可优化提示并为语言模型系统生成训练与评测数据的编程框架。
- [Awesome Synthetic Datasets](https://github.com/davanstrien/awesome-synthetic-datasets) - Tag: [report] - 覆盖文本和多模态任务的合成数据集与生成资源精选列表。
- [Self-Instruct Paper](https://arxiv.org/abs/2212.10560) - Tag: [paper] - 描述用自举方式生成指令数据来对齐语言模型的论文。
- [WizardLM / Evol-Instruct](https://arxiv.org/abs/2304.12244) - Tag: [paper] - 描述通过 Evol-Instruct 生成复杂指令数据的论文。

## RAG 评测数据

- [Ragas](https://github.com/explodinggradients/ragas) - Tag: [tool] - 提供检索和生成质量指标的 RAG 系统评测框架。
- [DeepEval](https://github.com/confident-ai/deepeval) - Tag: [tool] - 支持 RAG、LLM 和 Agent 评测工作流的开源评测框架。
- [BEIR](https://github.com/beir-cellar/beir) - Tag: [benchmark] - 常用于评估文档排序和检索组件的检索基准套件。
- [KILT](https://github.com/facebookresearch/KILT) - Tag: [benchmark] - 将知识密集型语言任务与可追溯语料连接起来的基准。
- [HotpotQA](https://hotpotqa.github.io/) - Tag: [dataset] - 多跳问答数据集，适合检索和证据链评估。
- [Natural Questions](https://ai.google.com/research/NaturalQuestions) - Tag: [dataset] - 常用于开放域问答、检索和 QA 评测的数据集。

## 金融领域 LLM 数据

- [FinEval](https://github.com/SUFE-AIFLM-Lab/FinEval) - Tag: [benchmark] - 用于评估 LLM 金融知识和安全性的中文金融领域基准。
- [PIXIU / FinBen](https://github.com/The-FinAI/PIXIU) - Tag: [benchmark] - 覆盖多类金融任务和数据集的金融 LLM 基准与框架。
- [FinGPT](https://github.com/AI4Finance-Foundation/FinGPT) - Tag: [tool] - 面向金融 LLM 研究、数据流水线和领域适配的开源项目。
- [FinNLP](https://github.com/AI4Finance-Foundation/FinNLP) - Tag: [tool] - 用于采集和处理金融文本数据的金融 NLP 工具包。
- [FinanceBench](https://github.com/patronus-ai/financebench) - Tag: [benchmark] - 基于公开披露文件评估 LLM 金融问答能力的基准。
- [FinQA](https://github.com/czyssrs/FinQA) - Tag: [dataset] - 面向金融报告数值推理的数据集。
- [TAT-QA](https://github.com/NExTplusplus/TAT-QA) - Tag: [dataset] - 围绕金融报告中表格与文本混合推理构建的问答数据集。

## 实践指南

- [LLM 训练数据质量 Rubric](docs/data-quality-rubric.md) - 用于审查公开 LLM 训练、微调、偏好、合成或评测数据集的实践清单。
- [金融领域 LLM 评测清单](docs/financial-domain-llm-evaluation-checklist.md) - 面向金融领域 LLM 评测的数据治理清单，避免私有数据和投资建议类表述。
- [标注质量与仲裁指南](docs/annotation-quality-guide.md) - 面向标注校准、一致性、仲裁、审核员漂移和偏好数据质量的实践指南。
- [偏好数据质量清单](docs/preference-data-quality-checklist.md) - 面向人类偏好数据、AI 反馈数据和 DPO/RLHF 数据适用性的审查清单。
- [金融领域 Benchmark 收录标准](docs/financial-benchmark-inclusion-criteria.md) - 用于收录金融领域 LLM benchmark 和数据集的保守标准。
- [上游贡献候选清单](docs/upstream-contribution-shortlist.md) - 面向公开 LLM 数据质量项目的谨慎贡献计划，优先选择对维护者有实际价值的小改动。

## 数据治理

- [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) - Tag: [paper] - 提出从动机、组成、收集和维护等维度结构化记录数据集的基础论文。
- [Data Cards Playbook](https://pair-code.github.io/datacardsplaybook/) - Tag: [report] - 用一致且负责任的方式记录数据集的实践指南。
- [Croissant](https://github.com/mlcommons/croissant) - Tag: [governance] - MLCommons 推出的机器学习数据集元数据格式。
- [DataHub](https://github.com/datahub-project/datahub) - Tag: [tool] - 用于数据发现、血缘和治理的开源元数据平台。
- [OpenMetadata](https://github.com/open-metadata/OpenMetadata) - Tag: [tool] - 面向数据资产的开源元数据和治理平台。
- [DVC](https://github.com/iterative/dvc) - Tag: [tool] - 用于可复现数据集发布的数据版本管理和流水线工具。

## 隐私与合规

- [Microsoft Presidio](https://github.com/microsoft/presidio) - Tag: [tool] - 用于检测和匿名化个人身份信息的开源框架。
- [scrubadub](https://github.com/LeapBeyond/scrubadub) - Tag: [tool] - 用于从自由文本中移除个人身份信息的 Python 库。
- [LLM Guard](https://github.com/protectai/llm-guard) - Tag: [tool] - 用于输入输出扫描的工具包，覆盖敏感数据和提示风险检查。
- [Google Differential Privacy](https://github.com/google/differential-privacy) - Tag: [tool] - 用于构建差分隐私数据分析流程的库和工具。
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Tag: [governance] - 与 AI 系统治理和文档化相关的风险管理框架。
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) - Tag: [governance] - LLM 应用开发和部署的安全风险参考。

## 论文

- [Training Language Models to Follow Instructions with Human Feedback](https://arxiv.org/abs/2203.02155) - Tag: [paper] - InstructGPT 论文，连接了监督数据、偏好数据和 RLHF。
- [Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2204.05862) - Tag: [paper] - 描述用于助手行为的人类偏好数据和 RLHF 训练方法。
- [Deduplicating Training Data Makes Language Models Better](https://arxiv.org/abs/2107.06499) - Tag: [paper] - 研究训练数据重复对语言模型行为影响的论文。
- [LIMA: Less Is More for Alignment](https://arxiv.org/abs/2305.11206) - Tag: [paper] - 研究小而精的监督数据集如何影响对齐行为的论文。
- [The BigScience ROOTS Corpus](https://arxiv.org/abs/2303.03915) - Tag: [paper] - 记录 BLOOM 训练语料 ROOTS 的多语言来源、治理和构建细节。
- [Direct Preference Optimization](https://arxiv.org/abs/2305.18290) - Tag: [paper] - 聚焦如何直接使用成对偏好数据进行训练的偏好优化论文。

## 开源工具

- [Hugging Face Datasets](https://github.com/huggingface/datasets) - Tag: [tool] - 用于数据集加载、转换、流式处理和分享的库。
- [DataTrove](https://github.com/huggingface/datatrove) - Tag: [tool] - 面向 LLM 语料准备的大规模文本数据处理框架。
- [Data-Juicer](https://github.com/modelscope/data-juicer) - Tag: [tool] - 面向 LLM 和多模态数据的数据处理与质量分析工具包。
- [Dolma Toolkit](https://github.com/allenai/dolma) - Tag: [tool] - AI2 用于构建和分析大规模预训练语料的工具包。
- [Label Studio](https://github.com/HumanSignal/label-studio) - Tag: [platform] - 通用开源标注平台。
- [Argilla](https://github.com/argilla-io/argilla) - Tag: [platform] - 面向 LLM 数据工作流的反馈和标注平台。
- [Ragas](https://github.com/explodinggradients/ragas) - Tag: [tool] - 用于检索和生成指标的 RAG 评测库。
- [TRL](https://github.com/huggingface/trl) - Tag: [tool] - 偏好优化和对齐训练库。

## 报告与实践手册

- [Data Cards Playbook](https://pair-code.github.io/datacardsplaybook/) - Tag: [report] - 用于透明数据集文档化的实践手册。
- [HELM](https://crfm.stanford.edu/helm/latest/) - Tag: [benchmark] - 面向语言模型整体评测的框架和报告。
- [NIST AI RMF Playbook](https://airc.nist.gov/AI_RMF_Knowledge_Base/Playbook) - Tag: [report] - 将 NIST AI 风险管理框架落地的操作手册。
- [FineWeb Blog](https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1) - Tag: [report] - Hugging Face 对 FineWeb 设计和过滤决策的说明。
- [The Turing Way: Research Data Management](https://book.the-turing-way.org/reproducible-research/rdm/rdm-data/) - Tag: [report] - 面向可复现研究数据管理的实践指南。

## 贡献指南

欢迎提交符合[质量门槛](#质量门槛)的资源。提交 issue 或 pull request 前，请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

本仓库采用 [CC BY 4.0](LICENSE.md) 许可证。被链接的第三方资源保留其各自的许可证和使用条款。
