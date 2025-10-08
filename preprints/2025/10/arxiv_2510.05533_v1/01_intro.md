---
authors:
- Weilong Fu
doc_id: arxiv:2510.05533v1
family_id: arxiv:2510.05533
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'The New Quant: A Survey of Large Language Models in Financial Prediction and
  Trading'
url_abs: http://arxiv.org/abs/2510.05533v1
url_html: https://arxiv.org/html/2510.05533v1
venue: arXiv q-fin
version: 1
year: 2025
---


Weilong Fu
Columbia University, USA. wf2232@columbia.edu

###### Abstract

Large language models are reshaping quantitative investing by turning unstructured financial information into evidence-grounded signals and executable decisions. This survey synthesizes research with a focus on equity return prediction and trading, consolidating insights from domain surveys and more than fifty primary studies. We propose a task-centered taxonomy that spans sentiment and event extraction, numerical and economic reasoning, multimodal understanding, retrieval-augmented generation, time series prompting, and agentic systems that coordinate tools for research, backtesting, and execution. We review empirical evidence for predictability, highlight design patterns that improve faithfulness such as retrieval first prompting and tool-verified numerics, and explain how signals feed portfolio construction under exposure, turnover, and capacity controls. We assess benchmarks and datasets for prediction and trading and outline desiderata-for time safe and economically meaningful evaluation that reports costs, latency, and capacity. We analyze challenges that matter in production, including temporal leakage, hallucination, data coverage and structure, deployment economics, interpretability, governance, and safety. The survey closes with recommendations for standardizing evaluation, building auditable pipelines, and advancing multilingual and cross-market research so that language-driven systems deliver robust and risk-controlled performance in practice.

Keywords large language models; financial prediction; return prediction; trading; portfolio construction

## 1 Introduction

Large Language Models enable a shift from feature-centric text mining to end-to-end decision systems in markets. We refer to this emerging paradigm as the new quant, by which we mean investment processes where language models read and reason over heterogeneous disclosures, generate auditable hypotheses, interact with external tools and data, and translate textual understanding into risk-controlled positions. This survey concentrates on the pipeline components that matter most for investment outcomes, namely financial prediction with an emphasis on equity return prediction and trading with portfolio construction. We systematize advances from 2023 to 2025 through this lens [[128](https://arxiv.org/html/2510.05533v1#bib.bibx128), [49](https://arxiv.org/html/2510.05533v1#bib.bibx49), [74](https://arxiv.org/html/2510.05533v1#bib.bibx74), [58](https://arxiv.org/html/2510.05533v1#bib.bibx58), [46](https://arxiv.org/html/2510.05533v1#bib.bibx46), [109](https://arxiv.org/html/2510.05533v1#bib.bibx109)].

Transformer pretraining and instruction tuning produced general purpose models with non-trivial reasoning and tool use [[24](https://arxiv.org/html/2510.05533v1#bib.bibx24), [13](https://arxiv.org/html/2510.05533v1#bib.bibx13), [2](https://arxiv.org/html/2510.05533v1#bib.bibx2)]. Domain-specific financial language models and open weight ecosystems make finance-grade adaptation feasible under privacy, governance, and cost constraints [[105](https://arxiv.org/html/2510.05533v1#bib.bibx105), [85](https://arxiv.org/html/2510.05533v1#bib.bibx85), [95](https://arxiv.org/html/2510.05533v1#bib.bibx95), [94](https://arxiv.org/html/2510.05533v1#bib.bibx94), [69](https://arxiv.org/html/2510.05533v1#bib.bibx69)]. Efficient tuning through low-rank adaptation, quantization-sensitive fine-tuning, and one-bit optimization lowers the barrier to controlled deployment in trading environments [[33](https://arxiv.org/html/2510.05533v1#bib.bibx33), [22](https://arxiv.org/html/2510.05533v1#bib.bibx22), [67](https://arxiv.org/html/2510.05533v1#bib.bibx67)]. In parallel, task-level capabilities have matured across sentiment, information extraction and knowledge graphs, numerical question answering, long document understanding, multi-modal analysis, and agentic decision support. These capabilities feed, constrain, and explain predictive signals and trade decisions [[46](https://arxiv.org/html/2510.05533v1#bib.bibx46), [74](https://arxiv.org/html/2510.05533v1#bib.bibx74), [128](https://arxiv.org/html/2510.05533v1#bib.bibx128)].

Evidence already suggests that model derived views on news, filings, earnings calls, and policy communications can predict returns in certain settings, although evaluation practice often falls short of trading standards. Leakage control, stress testing, market microstructure realism, and cost or capacity reporting remain inconsistent. Governance and interpretability requirements, such as evidence-based rationales, audit logs, and a clear separation between signal generation and portfolio allocation, are likewise unevenly addressed.

Our contributions are fourfold. First, we frame the design space for the development of new quantitative and review models relevant to finance together with the efficiency techniques that make financial language models practical [[24](https://arxiv.org/html/2510.05533v1#bib.bibx24), [13](https://arxiv.org/html/2510.05533v1#bib.bibx13), [2](https://arxiv.org/html/2510.05533v1#bib.bibx2), [105](https://arxiv.org/html/2510.05533v1#bib.bibx105), [33](https://arxiv.org/html/2510.05533v1#bib.bibx33), [22](https://arxiv.org/html/2510.05533v1#bib.bibx22), [67](https://arxiv.org/html/2510.05533v1#bib.bibx67)]. Second, we offer a task taxonomy centered on prediction and trading that clarifies how the upstream natural language processing components feed tradable signals [[74](https://arxiv.org/html/2510.05533v1#bib.bibx74), [128](https://arxiv.org/html/2510.05533v1#bib.bibx128), [46](https://arxiv.org/html/2510.05533v1#bib.bibx46)]. Third, we synthesize the literature on return prediction in Section [4](https://arxiv.org/html/2510.05533v1#S4 "4 LLMs for return prediction ‣ The New Quant: A Survey of Large Language Models in Financial Prediction and Trading") and on trading with portfolio construction in Section [5](https://arxiv.org/html/2510.05533v1#S5 "5 LLM assisted trading systems and portfolio construction ‣ The New Quant: A Survey of Large Language Models in Financial Prediction and Trading"). We cover interpretable financial language models, retrieval augmented pipelines, time series aware prompting, and multi-agent trading systems. Fourth, we consolidate benchmarks and datasets in Section [6](https://arxiv.org/html/2510.05533v1#S6 "6 Benchmarks and datasets for prediction and trading ‣ The New Quant: A Survey of Large Language Models in Financial Prediction and Trading") and articulate challenges in Section [7](https://arxiv.org/html/2510.05533v1#S7 "7 Challenges and open problems in LLM based prediction and trading ‣ The New Quant: A Survey of Large Language Models in Financial Prediction and Trading") that involve temporal leakage, faithfulness, evaluation realism, cost and latency, and governance. The audience includes researchers who build financial language models for tradable use cases, quantitative practitioners who evaluate language model signals, and leaders who design audit-ready deployment strategies [[109](https://arxiv.org/html/2510.05533v1#bib.bibx109), [46](https://arxiv.org/html/2510.05533v1#bib.bibx46)].

## 2 Foundations for Prediction and Trading with FinLLMs

### 2.1 From transformers to tool using language models

The transformer replaced recurrent networks with attention and enabled scalable pretraining on large corpora [[96](https://arxiv.org/html/2510.05533v1#bib.bibx96)]. Decoder only GPT models demonstrated emergent in context and few shot abilities [[81](https://arxiv.org/html/2510.05533v1#bib.bibx81), [82](https://arxiv.org/html/2510.05533v1#bib.bibx82), [13](https://arxiv.org/html/2510.05533v1#bib.bibx13)]. Encoder only models such as BERT and RoBERTa delivered state of the art text understanding for classification and span extraction [[24](https://arxiv.org/html/2510.05533v1#bib.bibx24), [61](https://arxiv.org/html/2510.05533v1#bib.bibx61)]. The GPT 4 technical report and instruction tuning advances, as exemplified by FLAN, established language models as general purpose controllers with meaningful reasoning and tool use [[2](https://arxiv.org/html/2510.05533v1#bib.bibx2), [102](https://arxiv.org/html/2510.05533v1#bib.bibx102)].

### 2.2 Open models and efficient adaptation for finance

Open releases including BLOOM and the LLaMA families catalyzed a flourishing ecosystem that supports controlled adaptation and on premise deployment [[85](https://arxiv.org/html/2510.05533v1#bib.bibx85), [95](https://arxiv.org/html/2510.05533v1#bib.bibx95), [94](https://arxiv.org/html/2510.05533v1#bib.bibx94), [69](https://arxiv.org/html/2510.05533v1#bib.bibx69)]. Additional families such as Qwen, Baichuan, and InternLM expand the menu of base models [[7](https://arxiv.org/html/2510.05533v1#bib.bibx7), [8](https://arxiv.org/html/2510.05533v1#bib.bibx8), [35](https://arxiv.org/html/2510.05533v1#bib.bibx35)]. Efficient training and post training alignment through low rank adaptation, quantization aware finetuning, and one bit optimization enable domain tuned models with modest compute budgets, which aligns with privacy and reproducibility constraints that are common in trading environments [[33](https://arxiv.org/html/2510.05533v1#bib.bibx33), [22](https://arxiv.org/html/2510.05533v1#bib.bibx22), [67](https://arxiv.org/html/2510.05533v1#bib.bibx67)].

### 2.3 Financial PLMs and FinLLMs

Before instruction following language models, financial applications built on encoder style pretrained language models such as the FinBERT line and showed early domain transfer benefits [[4](https://arxiv.org/html/2510.05533v1#bib.bibx4), [113](https://arxiv.org/html/2510.05533v1#bib.bibx113), [62](https://arxiv.org/html/2510.05533v1#bib.bibx62)]. Recent finance specific language models include BloombergGPT [[105](https://arxiv.org/html/2510.05533v1#bib.bibx105)], PIXIU [[107](https://arxiv.org/html/2510.05533v1#bib.bibx107)], FinGPT [[112](https://arxiv.org/html/2510.05533v1#bib.bibx112), [59](https://arxiv.org/html/2510.05533v1#bib.bibx59)], InvestLM [[114](https://arxiv.org/html/2510.05533v1#bib.bibx114)], Instruct FinGPT [[123](https://arxiv.org/html/2510.05533v1#bib.bibx123)], DISC FinLLM [[16](https://arxiv.org/html/2510.05533v1#bib.bibx16)], and CFGPT [[51](https://arxiv.org/html/2510.05533v1#bib.bibx51)]. Language and market specific adaptations such as SilverSight and FinVisGPT tailor models to regional corpora and workflows [[131](https://arxiv.org/html/2510.05533v1#bib.bibx131), [101](https://arxiv.org/html/2510.05533v1#bib.bibx101)]. FinTral reports a multimodal family with performance at the reported level of general purpose models [[11](https://arxiv.org/html/2510.05533v1#bib.bibx11)]. New compact bases such as Mistral 7B have also been adopted in finance settings [[37](https://arxiv.org/html/2510.05533v1#bib.bibx37)].

### 2.4 Implications for prediction and trading

For return prediction, decoder models support rationale generation and in context composition over news, filings, and macro text, while encoder models remain strong for narrow sentiment or extraction tasks that feed signals. Hybrid systems that combine retrieval augmented language models, language driven graph or sequence models, and mixture of experts pipelines appear frequently, often coupled with faithfulness checks and backtesting aware evaluation [[46](https://arxiv.org/html/2510.05533v1#bib.bibx46), [74](https://arxiv.org/html/2510.05533v1#bib.bibx74)]. For trading, agentic frameworks with tool use, memory, and role specialization begin to structure research, critique, and execution under constraints, which motivates new benchmarks and simulation protocols that we discuss in later sections.

## 3 Task taxonomy for financial prediction and trading

This section codifies a taxonomy that maps language model capabilities to finance workflows and clarifies how prediction and trading depend on upstream natural language processing. We group tasks by the primary function they serve in production pipelines, while noting that deployed systems often combine several capabilities in a single workflow.

### 3.1 Sentiment and opinion as signal inputs

The objective is to infer polarity, stance, and intensity from heterogeneous sources such as news, social media, earnings calls, and analyst notes, and to transform these assessments into features for event studies, return prediction, or risk monitoring. Domain tuned encoders in the FinBERT line demonstrate strong transfer on finance texts [[4](https://arxiv.org/html/2510.05533v1#bib.bibx4), [113](https://arxiv.org/html/2510.05533v1#bib.bibx113), [62](https://arxiv.org/html/2510.05533v1#bib.bibx62)]. Instruction tuned language models can score sentiment and produce justifications and they sometimes outperform classical lexicon baselines on complex material [[63](https://arxiv.org/html/2510.05533v1#bib.bibx63), [89](https://arxiv.org/html/2510.05533v1#bib.bibx89), [65](https://arxiv.org/html/2510.05533v1#bib.bibx65)]. Work on FOMC minutes and ECB press conferences indicates that policy tone can be quantified and linked to market responses [[28](https://arxiv.org/html/2510.05533v1#bib.bibx28), [41](https://arxiv.org/html/2510.05533v1#bib.bibx41)]. Classic resources remain useful as baselines and diagnostic tools [[64](https://arxiv.org/html/2510.05533v1#bib.bibx64), [77](https://arxiv.org/html/2510.05533v1#bib.bibx77), [90](https://arxiv.org/html/2510.05533v1#bib.bibx90), [70](https://arxiv.org/html/2510.05533v1#bib.bibx70), [91](https://arxiv.org/html/2510.05533v1#bib.bibx91), [12](https://arxiv.org/html/2510.05533v1#bib.bibx12)]. In a trading context sentiment features must be timestamped, free of look ahead leakage, and aligned to realistic rebalancing schedules.

### 3.2 Information extraction and knowledge graphs for point in time signals

Information extraction converts unstructured documents into structured entities, relations, and events that can feed screens, factor engines, and retrieval modules. Datasets such as FiNER, FinRED, and REFinD support supervised training and enable point in time knowledge curation [[31](https://arxiv.org/html/2510.05533v1#bib.bibx31), [86](https://arxiv.org/html/2510.05533v1#bib.bibx86), [87](https://arxiv.org/html/2510.05533v1#bib.bibx87), [42](https://arxiv.org/html/2510.05533v1#bib.bibx42)]. Large language models can assist IE through prompting or lightweight finetuning for named entity recognition and relation extraction [[21](https://arxiv.org/html/2510.05533v1#bib.bibx21), [83](https://arxiv.org/html/2510.05533v1#bib.bibx83)]. Event detection and relation modeling in Chinese and English demonstrate cross market applicability [[92](https://arxiv.org/html/2510.05533v1#bib.bibx92), [97](https://arxiv.org/html/2510.05533v1#bib.bibx97)]. As institutions deploy knowledge graphs for research, LLMs act as controllers and generators that populate and query the graphs while surveys outline integration patterns and governance requirements [[111](https://arxiv.org/html/2510.05533v1#bib.bibx111), [39](https://arxiv.org/html/2510.05533v1#bib.bibx39), [75](https://arxiv.org/html/2510.05533v1#bib.bibx75), [76](https://arxiv.org/html/2510.05533v1#bib.bibx76), [54](https://arxiv.org/html/2510.05533v1#bib.bibx54), [56](https://arxiv.org/html/2510.05533v1#bib.bibx56), [134](https://arxiv.org/html/2510.05533v1#bib.bibx134)]. For prediction and trading these components provide upstream signal generation and retrieval that improves evidence quality.

### 3.3 Numerical question answering and reasoning for thesis validation

These systems execute multi step reasoning over tables, text, and formulas in filings, earnings calls, and macro releases and they answer questions while computing key performance indicators. Benchmarks such as FinQA, FinanceBench, BizBench, DocMathEval, and EconLogicQA probe numerical correctness, long document understanding, and economics logic that underlies valuation and surprise based signals [[18](https://arxiv.org/html/2510.05533v1#bib.bibx18), [36](https://arxiv.org/html/2510.05533v1#bib.bibx36), [45](https://arxiv.org/html/2510.05533v1#bib.bibx45), [129](https://arxiv.org/html/2510.05533v1#bib.bibx129), [79](https://arxiv.org/html/2510.05533v1#bib.bibx79)]. Retrieval augmented generation with layout aware encoders and tool calls improves verifiability and accuracy and verification or constrained decoding reduces hallucination risk [[78](https://arxiv.org/html/2510.05533v1#bib.bibx78), [88](https://arxiv.org/html/2510.05533v1#bib.bibx88), [5](https://arxiv.org/html/2510.05533v1#bib.bibx5), [98](https://arxiv.org/html/2510.05533v1#bib.bibx98)]. In production pipelines these systems are most valuable when they produce intermediate calculations and citations that can be audited before the trade decision.

### 3.4 Summarization and document understanding for evidence condensation

Abstractive and extractive hybrids and instruction tuned models can compress long financial narratives such as ten K filings, management discussion and analysis, and earnings calls, which accelerates research and supports hypothesis generation [[27](https://arxiv.org/html/2510.05533v1#bib.bibx27), [80](https://arxiv.org/html/2510.05533v1#bib.bibx80), [71](https://arxiv.org/html/2510.05533v1#bib.bibx71), [1](https://arxiv.org/html/2510.05533v1#bib.bibx1), [133](https://arxiv.org/html/2510.05533v1#bib.bibx133)]. Retrieval aware chunking and long document architectures reduce information loss and yield more stable summaries [[116](https://arxiv.org/html/2510.05533v1#bib.bibx116), [9](https://arxiv.org/html/2510.05533v1#bib.bibx9)]. For trading use the outputs should be materiality aware and time stamped and they should reference evidence spans that analysts can verify.

### 3.5 Multimodal cues for predictive signals

Beyond text, systems fuse audio from calls, visuals such as charts, or structured time series to inform predictive modeling. Datasets and models for multimodal analysis of earnings calls and policy communication supply prosodic and visual cues [[52](https://arxiv.org/html/2510.05533v1#bib.bibx52), [68](https://arxiv.org/html/2510.05533v1#bib.bibx68)]. FinVisGPT addresses chart reading and explanation, and language model informed graph or sequence models use textual context to guide stock movement prediction [[101](https://arxiv.org/html/2510.05533v1#bib.bibx101), [17](https://arxiv.org/html/2510.05533v1#bib.bibx17), [104](https://arxiv.org/html/2510.05533v1#bib.bibx104)]. RiskLabs illustrates multi source fusion for risk prediction [[14](https://arxiv.org/html/2510.05533v1#bib.bibx14)]. For trading deployment multimodal models must meet latency constraints and must ensure that any audio or visual evidence is available at decision time.

### 3.6 Agentic workflows for trading and execution

Agentic frameworks operationalize language models as decision support agents with memory, tools, and role specialization. TradingGPT introduces layered memory and distinct analyst characters and later systems expand tool use, multi agent debate, and evaluation in leakage controlled simulations [[55](https://arxiv.org/html/2510.05533v1#bib.bibx55), [125](https://arxiv.org/html/2510.05533v1#bib.bibx125), [118](https://arxiv.org/html/2510.05533v1#bib.bibx118), [100](https://arxiv.org/html/2510.05533v1#bib.bibx100), [99](https://arxiv.org/html/2510.05533v1#bib.bibx99), [119](https://arxiv.org/html/2510.05533v1#bib.bibx119)]. Surveys of LLM based agents, computational experiments, memory mechanisms, and trust or safety provide design guidance and highlight open problems such as planning reliability and tool misuse [[106](https://arxiv.org/html/2510.05533v1#bib.bibx106), [30](https://arxiv.org/html/2510.05533v1#bib.bibx30), [66](https://arxiv.org/html/2510.05533v1#bib.bibx66), [127](https://arxiv.org/html/2510.05533v1#bib.bibx127), [34](https://arxiv.org/html/2510.05533v1#bib.bibx34)]. In practice these agents should separate research from order routing and they should log prompts, retrievals, and tool calls for audit.

### 3.7 Governance functions that constrain trading systems

Financial institutions explore LLMs for auditing support, contradiction detection, and regulatory interpretation [[10](https://arxiv.org/html/2510.05533v1#bib.bibx10), [23](https://arxiv.org/html/2510.05533v1#bib.bibx23), [15](https://arxiv.org/html/2510.05533v1#bib.bibx15), [19](https://arxiv.org/html/2510.05533v1#bib.bibx19)]. These capabilities do not execute trades and they do shape acceptable model behavior, guardrails, and evidence requirements for production systems. Trading oriented deployments benefit from explicit policies that bind language to timestamped evidence and that restrict action when verification fails.

Table 1: Mapping of tasks to trading relevance

| Task | Representative artifacts | Typical outputs | Contribution to trading |
| --- | --- | --- | --- |
| Sentiment and opinion | FinBERT line, instruction tuned LLM scorers | Polarity, stance, justifications | Event features, risk monitoring, regime filters |
| Information extraction and knowledge graphs | FiNER, FinRED, REFinD, FinDKG, WeaverBird | Entities, relations, events, KG triples | Point in time factors, high precision retrieval, constraint checks |
| Numerical QA and reasoning | FinQA, FinanceBench, DocMathEval, EconLogicQA | Computed KPIs, verified answers, reasoning chains | Thesis validation, surprise based signals, audit trails |
| Summarization and document understanding | ECTSum, MultiLing FNS, Longformer, RAG chunking | Condensed briefs with citations | Faster research, explanation for signals and trades |
| Multimodal analysis | MAEC, MONOPOLY, FinVisGPT | Prosody features, chart readings, fused embeddings | Additional cues for selection or sizing under latency limits |
| Agentic workflows | TradingGPT, FinAgent, FinMem, QuantAgent | Tool calls, debate traces, memory states | Orchestration of research, verification, and execution |
| Governance and compliance | Audit and regulation tools | Contradiction flags, policy checks | Guardrails that shape allowable actions and documentation |

## 4 LLMs for return prediction

This section surveys how language models produce equity return signals and how those signals can be translated into investable decisions. We organize methods by evidence channels and modeling patterns and then discuss evaluation practice and practical guidance. We focus on studies from 2023 to 2025 with direct implications for trading.

### 4.1 Problem formulation and evidence channels

The objective is to map text and related modalities to expected returns at horizons that range from intraday to monthly. Common channels include news and social media, corporate disclosures and earnings calls, and policy communications and macro releases. Work using general purpose language models reports that zero or few shot prompts on event text can be predictive in some settings [[63](https://arxiv.org/html/2510.05533v1#bib.bibx63), [89](https://arxiv.org/html/2510.05533v1#bib.bibx89)]. Domain specific corpora such as earnings call transcripts provide richer cues in the narrative and question and answer segments and several studies evaluate models on this setting [[20](https://arxiv.org/html/2510.05533v1#bib.bibx20)]. Central bank statements and press conferences also encode information that matters for assets that are sensitive to interest rates and risk appetite [[28](https://arxiv.org/html/2510.05533v1#bib.bibx28), [41](https://arxiv.org/html/2510.05533v1#bib.bibx41)].

### 4.2 Modeling patterns for text to return signals

#### Zero and few shot scoring with general models

General purpose models can be prompted to classify event direction or to assign a return score together with a rationale. Early finance studies report out of sample predictability from such scores on news and social media [[63](https://arxiv.org/html/2510.05533v1#bib.bibx63), [89](https://arxiv.org/html/2510.05533v1#bib.bibx89)]. Practical systems often add calibration layers, confidence filtering, and symbol mapping before portfolio construction.

#### Domain and instruction tuned FinLLMs

Instruction tuning on finance instructions and curated corpora improves robustness and reduces prompt brittleness. Representative models include InvestLM, Instruct FinGPT, FinGPT and its high performance computing variants, and FinLlama [[114](https://arxiv.org/html/2510.05533v1#bib.bibx114), [123](https://arxiv.org/html/2510.05533v1#bib.bibx123), [112](https://arxiv.org/html/2510.05533v1#bib.bibx112), [59](https://arxiv.org/html/2510.05533v1#bib.bibx59), [47](https://arxiv.org/html/2510.05533v1#bib.bibx47)]. Value aligned or preference tuned variants have also been explored [[117](https://arxiv.org/html/2510.05533v1#bib.bibx117)]. These models typically strengthen sentiment and event classification and they can generate explanations that are easier to audit.

#### Retrieval augmented modeling and knowledge grounded signals

Retrieval augmented generation reduces hallucination risk and improves faithfulness by binding predictions to timestamped evidence. Financial pipelines add retrieval aware chunking and layout features for long documents [[116](https://arxiv.org/html/2510.05533v1#bib.bibx116), [98](https://arxiv.org/html/2510.05533v1#bib.bibx98)]. Knowledge graphs and retrieval over company specific graphs further structure the evidence and stabilize factor construction [[111](https://arxiv.org/html/2510.05533v1#bib.bibx111), [54](https://arxiv.org/html/2510.05533v1#bib.bibx54)]. RAG enhanced sentiment has been shown to improve downstream accuracy on finance tasks [[122](https://arxiv.org/html/2510.05533v1#bib.bibx122)].

#### LLM guided structured models

Language models can supply features or supervisory signals to graph and sequence models that are optimized for price movement prediction. Examples include graph neural networks whose edges or node priors are informed by language model judgments and vision language systems that read price charts [[17](https://arxiv.org/html/2510.05533v1#bib.bibx17), [104](https://arxiv.org/html/2510.05533v1#bib.bibx104)]. Risk oriented work fuses model derived signals with other sources to predict adverse events [[14](https://arxiv.org/html/2510.05533v1#bib.bibx14)].

#### Time series aware prompting and forecasting

Several studies examine how to connect language models to time series forecasting. Approaches include reprogramming prompts for temporal inputs, using language models as zero shot forecasters, and using specialized long horizon transformer architectures alongside language models for reasoning and explanation [[40](https://arxiv.org/html/2510.05533v1#bib.bibx40), [29](https://arxiv.org/html/2510.05533v1#bib.bibx29), [130](https://arxiv.org/html/2510.05533v1#bib.bibx130), [73](https://arxiv.org/html/2510.05533v1#bib.bibx73), [103](https://arxiv.org/html/2510.05533v1#bib.bibx103), [57](https://arxiv.org/html/2510.05533v1#bib.bibx57)]. Although these papers are not always finance specific, the techniques inform how to condition signals on regime and horizon.

#### Interpretable designs and auditability

Production systems require transparent rationales and clear provenance for each predicted effect. Interpretable pipelines generate structured explanations and highlight evidence spans and they expose ablation or counterfactual checks. Recent work proposes interpretable stock movement modeling with finance specific rationale templates and self reflective explanations [[93](https://arxiv.org/html/2510.05533v1#bib.bibx93), [44](https://arxiv.org/html/2510.05533v1#bib.bibx44)]. These designs help risk teams to understand when and why a signal should be trusted.

### 4.3 Evaluation protocols that meet trading standards

Return prediction requires time safe evaluation. We recommend rolling walk forward splits with document availability enforced at decision time and with an embargo to prevent label leakage from post event commentary. Report signal quality with correlation and calibration and report economics with returns that include explicit commission and spread assumptions, Sharpe and drawdown, turnover and capacity, and sensitivity to universe and rebalancing frequency. Given growing evidence of look ahead issues in pretrained models, evaluation should check for time machine effects using dated corpora and explicit filters [[84](https://arxiv.org/html/2510.05533v1#bib.bibx84), [26](https://arxiv.org/html/2510.05533v1#bib.bibx26)]. Baselines should include naive and factor models and trend benchmarks to avoid overstating the incremental value of language signals [[38](https://arxiv.org/html/2510.05533v1#bib.bibx38)].

### 4.4 What works when and practical guidance

Language signals often add value around identifiable events and narrative changes and they can complement price based factors during regime shifts. News and social media sentiment tends to matter at shorter horizons when coverage is fast and dense. Earnings call analysis matters at announcement and in the following days when management tone and detail resolve uncertainty. Policy communication sentiment is most relevant for rate sensitive sectors and for broad risk appetite proxies. In all cases the portfolio should separate signal generation from allocation and risk and it should include materiality filters, confidence gating, and exposure controls.

Table 2: Representative papers for equity return prediction with one sentence summaries

| Paper | Setting or channel | One sentence summary |
| --- | --- | --- |
| [[63](https://arxiv.org/html/2510.05533v1#bib.bibx63)] | News and filings | Zero and few shot scores from a general model predict cross sectional returns in several universes with controls for headline leakage. |
| [[89](https://arxiv.org/html/2510.05533v1#bib.bibx89)] | Social media | Microblog sentiment from a large model correlates with next day stock moves and improves on lexicon baselines. |
| [[20](https://arxiv.org/html/2510.05533v1#bib.bibx20)] | Earnings calls | Locally hosted language models score call tone and deliver signals that survive controls for known factors. |
| [[28](https://arxiv.org/html/2510.05533v1#bib.bibx28)] | Policy minutes | FinBERT tuned for policy text extracts sentiment from FOMC minutes that aligns with market responses. |
| [[41](https://arxiv.org/html/2510.05533v1#bib.bibx41)] | Press conferences | A sentiment indicator from ECB statements explains euro area asset movements and complements macro variables. |
| [[114](https://arxiv.org/html/2510.05533v1#bib.bibx114)] | Finance tuned LLM | Instruction tuned InvestLM improves investment specific judgments and produces auditable rationales. |
| [[123](https://arxiv.org/html/2510.05533v1#bib.bibx123)] | Finance tuned LLM | Instruct FinGPT strengthens finance sentiment and can act as a robust scoring component in pipelines. |
| [[112](https://arxiv.org/html/2510.05533v1#bib.bibx112), [59](https://arxiv.org/html/2510.05533v1#bib.bibx59)] | Open finance LLM | FinGPT provides open models and recipes that enable cost aware domain adaptation for finance tasks. |
| [[47](https://arxiv.org/html/2510.05533v1#bib.bibx47)] | Sentiment for trading | FinLlama demonstrates instruction tuned scoring for trading oriented sentiment classification. |
| [[117](https://arxiv.org/html/2510.05533v1#bib.bibx117)] | Preference tuned LLM | GreedLlama studies value alignment for financial reasoning and highlights the effect on moral or risk trade offs. |
| [[116](https://arxiv.org/html/2510.05533v1#bib.bibx116)] | Retrieval and chunking | Retrieval aware chunking improves long document question answering for filings and earnings analysis. |
| [[98](https://arxiv.org/html/2510.05533v1#bib.bibx98)] | Layout aware modeling | A layout aware generator improves numerical reasoning over tables and reduces errors in KPI extraction. |
| [[111](https://arxiv.org/html/2510.05533v1#bib.bibx111)] | Knowledge grounded RAG | A system that couples language models with a knowledge base and search engine improves decision support quality. |
| [[54](https://arxiv.org/html/2510.05533v1#bib.bibx54)] | Dynamic knowledge graphs | A dynamic finance knowledge graph supports point in time retrieval for research and signal construction. |
| [[17](https://arxiv.org/html/2510.05533v1#bib.bibx17)] | Text guided GNN | A graph neural network informed by language model judgments improves stock movement prediction. |
| [[104](https://arxiv.org/html/2510.05533v1#bib.bibx104)] | Vision language | A vision language approach uses chart images to detect granular market changes that relate to returns. |
| [[14](https://arxiv.org/html/2510.05533v1#bib.bibx14)] | Multi source risk | A multi source pipeline with a language model integrates diverse data to predict financial risk events. |
| [[40](https://arxiv.org/html/2510.05533v1#bib.bibx40)] | Time series prompting | A reprogramming approach adapts language models to time series forecasting and yields competitive accuracy. |
| [[29](https://arxiv.org/html/2510.05533v1#bib.bibx29)] | Zero shot forecasting | Large language models used as zero shot forecasters provide reasonable baselines for several temporal datasets. |
| [[130](https://arxiv.org/html/2510.05533v1#bib.bibx130)] | Long horizon TS | A frequency enhanced transformer delivers strong long horizon forecasting and can complement language signals. |
| [[73](https://arxiv.org/html/2510.05533v1#bib.bibx73)] | Tokenization for TS | A tokenization approach converts time series into compact sequences that are well suited to transformers. |
| [[93](https://arxiv.org/html/2510.05533v1#bib.bibx93)] | Interpretable stock movement | An interpretable finance specific model produces rationales that link text spans to predicted movement. |
| [[44](https://arxiv.org/html/2510.05533v1#bib.bibx44)] | Self reflective explanations | A method that uses self reflection yields explainable stock predictions with improved plausibility of rationales. |
| [[38](https://arxiv.org/html/2510.05533v1#bib.bibx38)] | Baseline for trends | A comprehensive study of trend models supplies strong baselines that are useful when measuring incremental value. |

## 5 LLM assisted trading systems and portfolio construction

This section analyzes how language models support trading decisions from idea generation to execution and how they interact with portfolio construction. We organize the discussion around the life cycle of a trade and we emphasize designs that produce auditable, time safe, and economically meaningful outcomes.

### 5.1 From assisted research to executable strategies

Agentic systems transform language models into research assistants that read disclosures, propose hypotheses, and coordinate tools such as retrieval, calculators, and backtesters. TradingGPT introduces layered memory and distinct analyst roles that debate and refine theses before handing off to tools [[55](https://arxiv.org/html/2510.05533v1#bib.bibx55)]. FinAgent expands the toolkit to include multimodal inputs and broker like actions under a tool governance layer [[125](https://arxiv.org/html/2510.05533v1#bib.bibx125)]. FinMem focuses on memory design that stabilizes multi day workflows and preserves analyst intent during iteration [[118](https://arxiv.org/html/2510.05533v1#bib.bibx118)]. QuantAgent explores self improvement loops that critique prompts and strategies and that then retest within a controlled simulator [[100](https://arxiv.org/html/2510.05533v1#bib.bibx100)]. Alpha GPT and its successor Alpha GPT 2.0 formalize analyst in the loop alpha discovery with critique, ranking, and evaluation gates to reduce overfitting [[99](https://arxiv.org/html/2510.05533v1#bib.bibx99), [119](https://arxiv.org/html/2510.05533v1#bib.bibx119)]. Together these systems show how assisted research can evolve into executable strategies while keeping human oversight in the loop.

### 5.2 Prompting and language to strategy

Several studies convert natural language descriptions into screen definitions, factor recipes, or backtest scripts. Work on code generation for trading strategies indicates that language models can scaffold usable code with human review and unit tests [[3](https://arxiv.org/html/2510.05533v1#bib.bibx3)]. Conversational research tools support exploratory analysis and rapid what if checks for fundamental and event driven theses [[121](https://arxiv.org/html/2510.05533v1#bib.bibx121)]. Effective practice includes canonicalizing prompts into machine readable templates, validating data access permissions, and compiling prompts and code into immutable artifacts that can be audited later.

### 5.3 Retrieval verified analysis loops

Hallucination and numerical brittleness motivate retrieval verified workflows. Retrieval aware chunking and layout aware modeling improve KPI extraction from filings and reduce reasoning errors in long documents [[116](https://arxiv.org/html/2510.05533v1#bib.bibx116), [98](https://arxiv.org/html/2510.05533v1#bib.bibx98)]. Systems that couple a language model with a curated knowledge base and a search engine demonstrate higher faithfulness for decision support [[111](https://arxiv.org/html/2510.05533v1#bib.bibx111)]. In trading contexts the loop proceeds as propose, retrieve, verify, and only then simulate or trade. Each step produces traces with timestamps and evidence spans to support review by risk and compliance.

### 5.4 From signals to orders and execution

Language models that score text still require a conversion to orders and an execution policy that respects market microstructure. A practical pattern separates signal generation from order placement and routing. Execution quality depends on latency, slippage, queue priority, and the balance between limit and market orders. Recent work on generative modeling for limit order book message flow offers realistic simulators for policy testing [[72](https://arxiv.org/html/2510.05533v1#bib.bibx72)]. Decision systems should log order intents, parameter choices, and realized costs to enable attribution and continuous improvement.

### 5.5 Portfolio construction with language model support

Portfolio construction benefits from language models in two ways. First, LLM derived signals enter a classical optimizer or a rules based allocator with exposure and turnover controls. Second, language models can assist with constraint elicitation and documentation by translating investment beliefs and policy rules into machine readable constraints. Studies that evaluate the impact of conversational assistance on portfolio choices suggest that language models can improve portfolio hygiene when paired with clear prompts and risk constraints [[43](https://arxiv.org/html/2510.05533v1#bib.bibx43)]. In production settings the optimizer and the signal engine should remain distinct services with independent monitoring and fallback policies.

### 5.6 Evaluation protocols and guardrails for live trading

Trading evaluation must be time safe and economically grounded. Walk forward backtests should enforce document availability and embargo periods and they should report returns with explicit cost and impact assumptions, Sharpe and drawdown, turnover and capacity, and sensitivity to universe and rebalancing cadence. Work on lookahead bias in pretrained models and on time machine effects underscores the need for dated corpora and strict filters during both training and evaluation [[84](https://arxiv.org/html/2510.05533v1#bib.bibx84), [26](https://arxiv.org/html/2510.05533v1#bib.bibx26)]. Cost and latency management are essential for live use and hybrid query routing can reduce spend while maintaining quality by steering easy queries to lightweight models and reserving high capacity models for hard cases [[25](https://arxiv.org/html/2510.05533v1#bib.bibx25)]. Safety and governance require agent constitutions and risk aware judges that flag unsafe tool uses or policy violations [[34](https://arxiv.org/html/2510.05533v1#bib.bibx34), [120](https://arxiv.org/html/2510.05533v1#bib.bibx120)]. Systems should also detect contradictions in reports and maintain audit logs to support regulatory reviews [[23](https://arxiv.org/html/2510.05533v1#bib.bibx23), [15](https://arxiv.org/html/2510.05533v1#bib.bibx15)]. Strong baselines such as trend models help contextualize the incremental value of language driven workflows [[38](https://arxiv.org/html/2510.05533v1#bib.bibx38)].

### 5.7 Design patterns and practical guidance

A robust design separates research and execution and binds language to verifiable evidence. Retrieval first prompting, tool verified numerics, and debate or critique before simulation reduce false positives. Confidence gating, materiality thresholds, and exposure caps stabilize portfolios. Human review remains important for new strategies, high impact actions, and regime changes. Regular stress tests and post trade analysis complete the loop and help teams decide when to promote a research signal into a production strategy.

Table 3: Representative papers for LLM assisted trading and portfolio construction with one sentence summaries

| Paper | Contribution or setting | One sentence summary |
| --- | --- | --- |
| [[55](https://arxiv.org/html/2510.05533v1#bib.bibx55)] | Multi agent research to trade | A layered memory and role based framework proposes, critiques, and verifies trade ideas before execution in a controlled simulator. |
| [[125](https://arxiv.org/html/2510.05533v1#bib.bibx125)] | Tool augmented multimodal agent | A generalist agent integrates text and visuals and coordinates broker like tools under governance to produce executable decisions. |
| [[118](https://arxiv.org/html/2510.05533v1#bib.bibx118)] | Memory design for trading agents | A layered memory with character design improves persistence of analyst intent and boosts performance across multi day workflows. |
| [[100](https://arxiv.org/html/2510.05533v1#bib.bibx100)] | Self improving agent loop | A system that critiques prompts and strategies and that retests within a simulator yields more stable trading policies. |
| [[99](https://arxiv.org/html/2510.05533v1#bib.bibx99)] | Human AI alpha mining | An interactive workflow uses critique and ranking to surface promising alphas with guardrails against overfitting. |
| [[119](https://arxiv.org/html/2510.05533v1#bib.bibx119)] | Human in the loop alpha mining | The second version formalizes review gates and improves reliability when promoting ideas to production. |
| [[60](https://arxiv.org/html/2510.05533v1#bib.bibx60)] | Trading in realistic environments | A benchmarked environment evaluates LLM based traders with market frictions and supports ablation studies. |
| [[3](https://arxiv.org/html/2510.05533v1#bib.bibx3)] | Code generation for strategies | An empirical study shows that language models can scaffold trading code that passes unit tests when supervised by practitioners. |
| [[116](https://arxiv.org/html/2510.05533v1#bib.bibx116)] | Retrieval aware analysis | A chunking method improves retrieval and long document analysis for filings and earnings research that feeds trading. |
| [[98](https://arxiv.org/html/2510.05533v1#bib.bibx98)] | Layout aware modeling | A layout aware generator improves numerical reasoning over tables which reduces errors in research that precedes trades. |
| [[72](https://arxiv.org/html/2510.05533v1#bib.bibx72)] | Limit order book simulation | A token level generative model of message flow produces realistic microstructure that is useful for execution policy testing. |
| [[25](https://arxiv.org/html/2510.05533v1#bib.bibx25)] | Cost and latency control | A hybrid routing approach reduces inference cost while maintaining answer quality which benefits live trading systems. |
| [[34](https://arxiv.org/html/2510.05533v1#bib.bibx34)] | Safety for agent systems | A constitution guided method constrains tool use and reduces unsafe actions during autonomous or semi autonomous operation. |
| [[120](https://arxiv.org/html/2510.05533v1#bib.bibx120)] | Risk aware judging for agents | A benchmark and judge detect unsafe patterns in agent traces which complements trading evaluation. |
| [[23](https://arxiv.org/html/2510.05533v1#bib.bibx23)] | Governance and auditing | A contradiction detection pipeline highlights inconsistencies in financial reports and contributes to audit readiness. |
| [[15](https://arxiv.org/html/2510.05533v1#bib.bibx15)] | Regulatory interpretation | A study outlines how language models can support interpretation of financial regulation which aids deployment governance. |
| [[38](https://arxiv.org/html/2510.05533v1#bib.bibx38)] | Baseline for execution value add | A comprehensive trend study provides strong baselines that help measure the incremental value of language driven trading. |

## 6 Benchmarks and datasets for prediction and trading

The growth of financial language models has outpaced the availability of standardized and time safe benchmarks that connect textual understanding to tradable decisions. We organize the landscape into prediction oriented reasoning benchmarks that produce signals, trading and agent benchmarks that evaluate decision quality under constraints, and corpora and datasets that supply supervision or retrieval evidence. Across categories three design principles are foundational. First, temporal integrity ensures point in time documents and rolling and non overlapping out of sample evaluation with embargoed validation. Second, economically grounded metrics require profit and loss with costs, Sharpe, drawdown, turnover and capacity, and hit rate at realistic rebalancing frequencies. Third, reproducibility demands seeded data releases, fixed symbol universes with survivorship bias controls, and code to reconstruct splits.

### 6.1 Prediction oriented reasoning and understanding

A first class of resources evaluates whether models can extract and reason over financial information that plausibly feeds return prediction. FinQA targets numerical reasoning over text and tables and signals derived from correct KPI computation are often used upstream of event driven strategies [[18](https://arxiv.org/html/2510.05533v1#bib.bibx18)]. FinanceBench and BizBench probe quantitative reasoning and business logic and they stress mathematical consistency that underlies valuation or surprise based signals [[36](https://arxiv.org/html/2510.05533v1#bib.bibx36), [45](https://arxiv.org/html/2510.05533v1#bib.bibx45)]. DocMathEval isolates long document numerical reasoning with tables which is a frequent failure point in earnings analysis [[129](https://arxiv.org/html/2510.05533v1#bib.bibx129)]. EconLogicQA evaluates economics sequential reasoning that matters for macro sensitive trade selection [[79](https://arxiv.org/html/2510.05533v1#bib.bibx79)]. The FinBen proposes a holistic financial benchmark that covers multiple tasks in finance [[108](https://arxiv.org/html/2510.05533v1#bib.bibx108)]. AlphaFin frames analysis as a retrieval augmented stock chain that aligns evaluation with multi step reasoning workflows [[53](https://arxiv.org/html/2510.05533v1#bib.bibx53)]. These resources are not trading simulators and they measure signal fidelity since a failure on numerical reasoning or economic logic makes the trade premise unsound.

### 6.2 Trading and agent evaluations

Benchmarks that are tailored to trading decisions remain emergent. Agent frameworks report simulation results using internal market environments together with layered memory and tool use such as retrieval, backtesting, and data application programming interfaces [[55](https://arxiv.org/html/2510.05533v1#bib.bibx55), [125](https://arxiv.org/html/2510.05533v1#bib.bibx125), [118](https://arxiv.org/html/2510.05533v1#bib.bibx118), [100](https://arxiv.org/html/2510.05533v1#bib.bibx100), [99](https://arxiv.org/html/2510.05533v1#bib.bibx99), [119](https://arxiv.org/html/2510.05533v1#bib.bibx119)]. These works advance methodology through role specialization, verifier checks, and reflection and two gaps persist. First, there is limited standardization of market microstructure such as latency, slippage, queue priority, and the limit or market order mix. Second, there is heterogeneous choice of universes and horizons that complicates cross paper comparisons. Safety risk awareness for agents is emerging through R Judge which can complement trading evaluations by detecting unsafe tool usage or risk insensitive actions [[120](https://arxiv.org/html/2510.05533v1#bib.bibx120)].

### 6.3 Domain corpora and supervision for predictive pipelines

Upstream datasets support sentiment, information extraction, event detection, and summarization that feed predictive engines. FiNER, FinRED, and REFinD supervise extraction of entities, relations, and events that populate knowledge graphs and enable cleaner point in time factors [[86](https://arxiv.org/html/2510.05533v1#bib.bibx86), [87](https://arxiv.org/html/2510.05533v1#bib.bibx87), [42](https://arxiv.org/html/2510.05533v1#bib.bibx42)]. ECTSum and MultiLing FNS provide summarization targets for earnings calls and reports, while MAEC and MONOPOLY supply multimodal earnings and policy material [[71](https://arxiv.org/html/2510.05533v1#bib.bibx71), [27](https://arxiv.org/html/2510.05533v1#bib.bibx27), [52](https://arxiv.org/html/2510.05533v1#bib.bibx52), [68](https://arxiv.org/html/2510.05533v1#bib.bibx68)]. FinSBD focuses on structural boundary detection in unstructured filings and DocLLM demonstrates layout aware modeling that improves numerical question answering and KPI retrieval [[6](https://arxiv.org/html/2510.05533v1#bib.bibx6), [98](https://arxiv.org/html/2510.05533v1#bib.bibx98)]. These resources help construct evidence grounded signals that can survive audit.

### 6.4 Multilingual and regional benchmarks

Financial markets are multilingual and regulatory regimes differ across regions. Several efforts broaden coverage to non English disclosures. CFBenchmark, FinEval, and CFLUE provide Chinese financial evaluation resources and SuperCLUE Fin offers a fine grained analysis of Chinese tasks [[50](https://arxiv.org/html/2510.05533v1#bib.bibx50), [124](https://arxiv.org/html/2510.05533v1#bib.bibx124), [132](https://arxiv.org/html/2510.05533v1#bib.bibx132), [110](https://arxiv.org/html/2510.05533v1#bib.bibx110)]. Hirano constructs a Japanese financial benchmark that expands regional testing [[32](https://arxiv.org/html/2510.05533v1#bib.bibx32)]. A study on bilingual prowess examines English and Spanish which is valuable for cross listings and American depositary receipts [[126](https://arxiv.org/html/2510.05533v1#bib.bibx126)].

### 6.5 Evaluation desiderata and a practical proposal

A prediction and trading benchmark should enforce time safe document availability, include standardized universes, rebalancing schedules, and cost models, and report both signal metrics and portfolio metrics with ablations for retrieval, verifiers, and tool latency. It should publish agent traces with evidence links for auditability and include stress periods and regime slices together with multilingual tracks. A practical path is to couple AlphaFin or The FinBen style reasoning tasks with an open microstructure simulator and R Judge style safety checks.

Table 4: Datasets and benchmarks that are most relevant to prediction and trading

| Resource | Modality | Primary task | Relevance to trading |
| --- | --- | --- | --- |
| FinQA [[18](https://arxiv.org/html/2510.05533v1#bib.bibx18)] | Text and tables | Numerical question answering | KPI correctness supports earnings surprise and event driven signals |
| FinanceBench [[36](https://arxiv.org/html/2510.05533v1#bib.bibx36)] | Text and numbers | Financial question answering | Valuation and logic checks help thesis validation |
| BizBench [[45](https://arxiv.org/html/2510.05533v1#bib.bibx45)] | Text and numbers | Quantitative reasoning | Business logic consistency matters for fundamental theses |
| DocMathEval [[129](https://arxiv.org/html/2510.05533v1#bib.bibx129)] | Long documents and tables | Numerical reasoning | Reduces miscalculation risk in filings driven research |
| EconLogicQA [[79](https://arxiv.org/html/2510.05533v1#bib.bibx79)] | Text | Economics sequential reasoning | Supports macro sensitive selection and hedging decisions |
| The FinBen [[108](https://arxiv.org/html/2510.05533v1#bib.bibx108)] | Multi task | Holistic finance evaluation | Broad coverage aligns with diverse production workflows |
| AlphaFin [[53](https://arxiv.org/html/2510.05533v1#bib.bibx53)] | RAG with stock chain | Financial analysis | Multi step reasoning for equity research with RAG |
| FiNER and FinRED and REFinD [[86](https://arxiv.org/html/2510.05533v1#bib.bibx86), [87](https://arxiv.org/html/2510.05533v1#bib.bibx87), [42](https://arxiv.org/html/2510.05533v1#bib.bibx42)] | Text | IE and NER and relation extraction | Populates knowledge graphs and supports time safe factors and retrieval |
| ECTSum and MultiLing FNS [[71](https://arxiv.org/html/2510.05533v1#bib.bibx71), [27](https://arxiv.org/html/2510.05533v1#bib.bibx27)] | Text | Summarization | Generates research briefs that accelerate analysis before trading |
| MAEC and MONOPOLY [[52](https://arxiv.org/html/2510.05533v1#bib.bibx52), [68](https://arxiv.org/html/2510.05533v1#bib.bibx68)] | Audio and video and text | Multimodal earnings and policy | Supplies prosodic and policy cues for selection and sizing |
| FinSBD and DocLLM [[6](https://arxiv.org/html/2510.05533v1#bib.bibx6), [98](https://arxiv.org/html/2510.05533v1#bib.bibx98)] | Text and layout | Structure detection and layout aware modeling | Stabilizes retrieval and improves numerical accuracy in long documents |
| CFBenchmark and FinEval and CFLUE and SuperCLUE Fin and JP benchmark [[50](https://arxiv.org/html/2510.05533v1#bib.bibx50), [124](https://arxiv.org/html/2510.05533v1#bib.bibx124), [132](https://arxiv.org/html/2510.05533v1#bib.bibx132), [110](https://arxiv.org/html/2510.05533v1#bib.bibx110), [32](https://arxiv.org/html/2510.05533v1#bib.bibx32)] | Text | Regional evaluation | Enables non English disclosures and cross market strategies |
| R Judge [[120](https://arxiv.org/html/2510.05533v1#bib.bibx120)] | Agent traces | Safety risk awareness | Adds guardrails for tool using agents during evaluation |
| TradingGPT and FinAgent and FinMem and QuantAgent and Alpha GPT [[55](https://arxiv.org/html/2510.05533v1#bib.bibx55), [125](https://arxiv.org/html/2510.05533v1#bib.bibx125), [118](https://arxiv.org/html/2510.05533v1#bib.bibx118), [100](https://arxiv.org/html/2510.05533v1#bib.bibx100), [99](https://arxiv.org/html/2510.05533v1#bib.bibx99), [119](https://arxiv.org/html/2510.05533v1#bib.bibx119)] | Agent frameworks | Trading simulations | Provide methodology and protocols without standard data releases |

## 7 Challenges and open problems in LLM based prediction and trading

### 7.1 Temporal leakage and time machine effects

Return prediction with general web pretraining risks look ahead leakage because models may memorize future facts and surface them during prompting. Recent critiques show that even without explicit future documents at inference time the latent knowledge can leak into answers [[84](https://arxiv.org/html/2510.05533v1#bib.bibx84), [26](https://arxiv.org/html/2510.05533v1#bib.bibx26)]. Effective mitigation combines corpora with strict publication cutoffs per evaluation fold, training data that is filtered by crawl date and source type, embargo windows for validation, and rationales that cite evidence published before the decision timestamp.

### 7.2 Evaluation realism and economic significance

Many studies report accuracy or correlation without a trading grade evaluation. Credible claims for language model signals require rolling walk forward backtests, conservative cost and impact models, turnover and capacity analysis, stress tests across regimes, and risk controlled performance with Sharpe, Sortino, drawdown, and tail loss. Benchmarks should include materiality filters so that statistically significant and economically trivial effects are not over interpreted.

### 7.3 Faithfulness, hallucination, and numerical robustness

Language models can produce confident but wrong rationales and can show brittle numerical reasoning. Evidence bound generation with citations to retrieved passages and tables, constrained tool use such as calculators and parsers, post hoc verification methods, and dual model cross checking reduce risk [[48](https://arxiv.org/html/2510.05533v1#bib.bibx48)]. For trading the system should never change risk based on unverifiable rationales.

### 7.4 Data coverage, point in time structure, and retrieval

Filings, press releases, calls, and macro statements have heterogeneous formats and chunking and indexing must be point in time and stable across refactors. Layout aware encoders improve KPI extraction, structure boundary detection stabilizes retrieval, and financial information extraction datasets support higher precision evidence graphs [[98](https://arxiv.org/html/2510.05533v1#bib.bibx98), [6](https://arxiv.org/html/2510.05533v1#bib.bibx6), [86](https://arxiv.org/html/2510.05533v1#bib.bibx86), [87](https://arxiv.org/html/2510.05533v1#bib.bibx87), [42](https://arxiv.org/html/2510.05533v1#bib.bibx42)]. Coverage gaps persist for small capitalization firms and non English issuers and multilingual resources help reduce these gaps.

### 7.5 Cost, latency, and deployment economics

Real time trading requires bounded latency and cost. Hybrid query routing can steer easy queries to cheaper models and reserve high capacity models for hard cases and low rank and quantized adaptation can further lower the footprint [[25](https://arxiv.org/html/2510.05533v1#bib.bibx25), [33](https://arxiv.org/html/2510.05533v1#bib.bibx33), [22](https://arxiv.org/html/2510.05533v1#bib.bibx22), [67](https://arxiv.org/html/2510.05533v1#bib.bibx67)]. System level reporting should include wall clock latency per decision and amortized compute cost per basis point of excess return.

### 7.6 Interpretability, governance, and regulatory alignment

Trading decisions must be explainable to risk, audit, and regulators. Desirable properties include rationales that are grounded in timestamped evidence, decomposition of effect that links evidence to predicted return, clear separation between signal generation and portfolio allocation, and audit logs for prompts, retrieved passages, and tool calls. Studies on regulatory interpretation and auditing support illustrate patterns for compliance ready pipelines [[15](https://arxiv.org/html/2510.05533v1#bib.bibx15), [10](https://arxiv.org/html/2510.05533v1#bib.bibx10), [23](https://arxiv.org/html/2510.05533v1#bib.bibx23)].

### 7.7 Security, privacy, and safety

Financial language models raise attack surfaces that include prompt injection and alignment breaking attacks and they create privacy concerns. Agent frameworks need constitutions and safety checks to prevent unauthorized orders, personal data leakage, or policy violations [[34](https://arxiv.org/html/2510.05533v1#bib.bibx34), [115](https://arxiv.org/html/2510.05533v1#bib.bibx115)]. Ethical codes and evolving artificial intelligence regulations should inform deployment gates and operational controls.

### 7.8 Robust generalization and regime shifts

Language model signals can overfit a disclosure style, sector, or macro regime. Techniques that help include domain adaptation with retrieval from diverse sources, regime aware training through explicit slicing or adversarial invariance, multilingual modeling for cross listed firms, and ensembling with classical factors to stabilize exposures. Reporting should include sector breakdowns and regime wise performance.

### 7.9 Data synthesis and augmentation

Language model based augmentation can improve label efficiency and synthetic data can introduce biases or leakage if generated with non time safe context. Synthetic examples should be marked, confined to training, and stress tested for bias. Evaluation sets should never contain synthetic items.

### 7.10 Minimum reporting standard

As a minimum reporting standard, studies should enforce time safe data and splits with document availability at the decision timestamp; present a full cost model with commissions, spreads, and market impact calibrated to the universe and size; report turnover, capacity, and the effect of transaction costs on net performance; analyze stress periods and regimes with sector level breakdowns; provide evidence grounded rationales and verified calculations for key examples; include ablations for retrieval, verifiers, and query routing together with wall clock latency and compute cost per decision; release seeds and code to reconstruct time splits and point in time indices or a protocol that supports replication; and compare against strong trend and factor baselines to quantify incremental value.

## 8 Conclusion

Large Language Models are redefining quantitative investing by turning unstructured financial information into auditable signals and coordinated actions. In the new quant, language models do not replace classical statistics or portfolio theory and they compose with them. Models read filings and calls, cite timestamped evidence, invoke calculators and parsers for numerics, and hand verified signals to risk aware allocation engines. Evidence accumulated in recent work suggests real potential for excess returns in selected regimes and universes, especially when models are domain adapted, retrieval grounded, and evaluated with trading grade procedures.

The field should adopt three practical principles. Separate concerns means keeping signal generation with retrieval and verification distinct from portfolio construction so that objectives and accountability remain clear. Bind language to evidence means requiring timestamped citations and tool verified calculations before any position changes and logging prompts, retrievals, and tool calls for auditability. Evaluate like a practitioner means enforcing time safe splits with document availability checks and realistic costs and slippage, reporting turnover and capacity, analyzing stress regimes, and disclosing latency and compute cost per decision rather than only reporting accuracy.

A focused research program follows from these principles. The community should design standardized prediction to trading benchmarks that couple reasoning tasks such as FinQA, FinanceBench, and AlphaFin with open and time safe market simulators and with safety audits that detect risky tool use [[18](https://arxiv.org/html/2510.05533v1#bib.bibx18), [36](https://arxiv.org/html/2510.05533v1#bib.bibx36), [53](https://arxiv.org/html/2510.05533v1#bib.bibx53), [120](https://arxiv.org/html/2510.05533v1#bib.bibx120)]. Training and evaluation should emphasize temporal robustness through filtered corpora, explicit publication cutoffs, and diagnostics for look ahead effects [[84](https://arxiv.org/html/2510.05533v1#bib.bibx84), [26](https://arxiv.org/html/2510.05533v1#bib.bibx26)]. Explainable financial language models should produce evidence anchored rationales that map to portfolio exposures to meet governance needs. Multilingual and low resource finance should receive sustained attention to support global coverage and cross listing dynamics. Systems should be cost aware through hybrid query routing and efficient adaptation methods such as low rank tuning, quantization aware finetuning, and one bit optimization [[25](https://arxiv.org/html/2510.05533v1#bib.bibx25), [33](https://arxiv.org/html/2510.05533v1#bib.bibx33), [22](https://arxiv.org/html/2510.05533v1#bib.bibx22), [67](https://arxiv.org/html/2510.05533v1#bib.bibx67)]. Human and AI collaboration should be central and analyst in the loop critique and debate agents can increase faithfulness without sacrificing speed while agent constitutions and judges improve safety [[34](https://arxiv.org/html/2510.05533v1#bib.bibx34), [120](https://arxiv.org/html/2510.05533v1#bib.bibx120)].

With transparent benchmarks, temporal discipline, and audit ready system design, financial language models can progress from promising prototypes to reliable building blocks in modern investment processes. The promise of the new quant is to translate textual understanding into robust, risk controlled, and economically meaningful trades.

## Disclosure

Portions of this paper were drafted or paraphrased with the assistance of ChatGPT (OpenAI).
The author reviewed, edited, and takes full responsibility for the intellectual content and conclusions presented in this work.

## References

* [1]
  Salah Abdaljalil and Houda Bouamor
  “An Exploration of Automatic Text Summarization of Financial Reports”
  In *Proceedings of the Third Workshop on Financial Technology and Natural Language Processing*, 2021
* [2]
  Josh Achiam
  “GPT-4 Technical Report”
  In *arXiv preprint arXiv:2303.08774*, 2023
  URL: <https://arxiv.org/abs/2303.08774>
* [3]
  Miguel Noguer Alonso and Hanane Dupouy
  “Evaluating LLMs in Financial Tasks: Code Generation in Trading Strategies”, SSRN Working Paper, 2024
* [4]
  Dogan Can Araci
  “FinBERT: Financial Sentiment Analysis with Pre-Trained Language Models”
  In *arXiv preprint arXiv:1908.10063*, 2019
* [5]
  Anirudh Arun, Aishwarya Dhiman, Mohit Soni and Yifeng Hu
  “Numerical Reasoning for Financial Reports”
  In *arXiv preprint arXiv:2312.14870*, 2023
  URL: <https://arxiv.org/abs/2312.14870>
* [6]
  William Au, Amine Ait-Azzi and Jaewoo Kang
  “FinSBD-2021: The 3rd Shared Task on Structure Boundary Detection in Unstructured Text in the Financial Domain”
  In *Companion Proceedings of the Web Conference 2021*, 2021
* [7]
  Junjie Bai
  “Qwen Technical Report”
  In *arXiv preprint arXiv:2309.16609*, 2023
* [8]
   Baichuan Inc.
  “Baichuan-13B”, <https://github.com/baichuan-inc/Baichuan-13B>, 2023
* [9]
  Iz Beltagy, Matthew E. Peters and Arman Cohan
  “Longformer: The Long-Document Transformer”
  In *arXiv preprint arXiv:2004.05150*, 2020
* [10]
  Alexander Berger et al.
  “Towards Automated Regulatory Compliance Verification in Financial Auditing with Large Language Models”
  In *2023 IEEE International Conference on Big Data (BigData)*, 2023, pp. 4626–4635
  DOI: [10.1109/BigData59044.2023.10386420](https://dx.doi.org/10.1109/BigData59044.2023.10386420)
* [11]
  Gautam Bhatia, El Moatez Billah Nagoudi, Huseyin Cavusoglu and Mohammad Abdul-Mageed
  “FinTral: A Family of GPT-4-Level Multimodal Financial Large Language Models”
  In *arXiv preprint arXiv:2402.10986*, 2024
* [12]
  Manash Pratim Bordoloi and Souvik Kumar Biswas
  “Sentiment Analysis: A Survey on Design Framework, Applications and Future Scopes”
  In *Artificial Intelligence Review*, 2023
* [13]
  Tom B. Brown and Benjamin Mann
  “Language Models are Few-Shot Learners”
  In *Advances in Neural Information Processing Systems*, 2020
* [14]
  Yuxin Cao and Zhen Chen
  “RiskLabs: Predicting Financial Risk Using Large Language Model Based on Multi-Sources Data”
  In *arXiv preprint arXiv:2404.07452*, 2024
* [15]
  Zheng Cao and Zachary Feinstein
  “Large Language Model in Financial Regulatory Interpretation”
  In *arXiv preprint arXiv:2405.06808*, 2024
* [16]
  Wei Chen and Qian Wang
  “DISC-FinLLM: A Chinese Financial Large Language Model Based on Multiple Experts Fine-Tuning”
  In *arXiv preprint arXiv:2310.15205*, 2023
* [17]
  Zhanying Chen and Lin Ning Zheng
  “ChatGPT Informed Graph Neural Network for Stock Movement Prediction”
  In *arXiv preprint arXiv:2306.03763*, 2023
* [18]
  Zheng Chen and Wenhu Chen
  “FinQA: A Dataset of Numerical Reasoning over Financial Data”
  In *arXiv preprint arXiv:2109.00122*, 2021
* [19]
  Gyu-Young Choi and Alexander G. Kim
  “Firm-Level Tax Audits: A Generative AI-Based Measurement”, Chicago Booth Research Paper No. 23-23, SSRN, 2024
  URL: <https://ssrn.com/abstract=4645865>
* [20]
  Thomas R. Cook, Sergey Kazinnik, Asger Lunde Hansen and Peter McAdam
  “Evaluating Local Language Models: An Application to Financial Earnings Calls”
  In *SSRN 4627143*, 2023
* [21]
  Eduardo Covas
  “Named Entity Recognition Using GPT for Identifying Comparable Companies”
  In *arXiv preprint arXiv:2307.07420*, 2023
* [22]
  Tim Dettmers, Artidoro Pagnoni, Ari Holtzman and Luke Zettlemoyer
  “QLoRA: Efficient Finetuning of Quantized LLMs”
  In *Advances in Neural Information Processing Systems*, 2024
* [23]
  Tobias DeuSSer and Daniel Leonhard
  “Uncovering Inconsistencies and Contradictions in Financial Reports Using Large Language Models”
  In *2023 IEEE International Conference on Big Data*, 2023
* [24]
  Jacob Devlin, Ming-Wei Chang, Kenton Lee and Kristina Toutanova
  “BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding”
  In *arXiv preprint arXiv:1810.04805*, 2019
  URL: <https://arxiv.org/abs/1810.04805>
* [25]
  Dawei Ding
  “Hybrid LLM: Cost-Efficient and Quality-Aware Query Routing”
  In *arXiv preprint arXiv:2404.14618*, 2024
* [26]
  Finley Drinkall, Ehsan Rahimikia, Janet B. Pierrehumbert, Stephen Roberts and Stefan Zohren
  “Time Machine GPT”
  In *arXiv preprint arXiv:2404.18543*, 2024
* [27]
  Mahmoud El-Haj
  “MultiLing 2019: Financial Narrative Summarisation”
  In *Proceedings of the MultiLing 2019 Workshop*, 2019
* [28]
  Samuel Gössi, Zhe Chen, Wonseok Kim, Benedikt Bermeitinger and Siegfried Handschuh
  “FinBERT-FOMC: Fine-Tuned FinBERT with Sentiment Focus Method for Enhancing Sentiment Analysis of FOMC Minutes”
  In *Proceedings of the ACM International Conference on AI in Finance*, 2023
* [29]
  Nate Gruver
  “Large Language Models Are Zero-Shot Time Series Forecasters”
  In *Advances in Neural Information Processing Systems*, 2024
* [30]
  Tianhao Guo, Xiang Chen, Yiming Wang, Ruocheng Chang, Shuai Pei, Nitesh V. Chawla, Olaf Wiest and Xiangliang Zhang
  “Large Language Model Based Multi-Agents: A Survey of Progress and Challenges”
  In *arXiv preprint arXiv:2402.01680*, 2024
  URL: <https://arxiv.org/abs/2402.01680>
* [31]
  Lennart Hillebrand
  “KPI-BERT: A Joint NER and Relation Extraction Model for Financial Reports”
  In *Proceedings of the 26th International Conference on Pattern Recognition*, 2022
* [32]
  Masaki Hirano
  “Construction of a Japanese Financial Benchmark for Large Language Models”
  In *arXiv preprint arXiv:2403.15062*, 2024
* [33]
  Edward J. Hu and Yelong Shen
  “LoRA: Low-Rank Adaptation of Large Language Models”
  In *arXiv preprint arXiv:2106.09685*, 2021
  URL: <https://arxiv.org/abs/2106.09685>
* [34]
  Weizhi Hua
  “TrustAgent: Toward Safe and Trustworthy LLM-Based Agents Through Agent Constitution”
  In *arXiv preprint arXiv:2402.01586*, 2024
* [35]
   InternLM
  “InternLM”, <https://github.com/InternLM>, 2024
* [36]
  Pritom Islam
  “FinanceBench: A New Benchmark for Financial Question Answering”
  In *arXiv preprint arXiv:2311.11944*, 2023
* [37]
  Albert Jiang
  “Mistral 7B”
  In *arXiv preprint arXiv:2310.06825*, 2023
* [38]
  Jin-Chuan Jiang, Bryan Kelly and Dacheng Xiu
  “(Re-)Imag(in)ing Price Trends”
  In *The Journal of Finance* 78.6, 2023, pp. 3193–3249
* [39]
  Xiaotao Jiang
  “On the Evolution of Knowledge Graphs: A Survey and Perspective”
  In *arXiv preprint arXiv:2310.04835*, 2023
* [40]
  Ming Jin
  “Time-LLM: Time Series Forecasting by Reprogramming Large Language Models”
  In *arXiv preprint arXiv:2310.01728*, 2023
* [41]
  Dimitrios Kanelis and Pierre L. Siklos
  “The ECB Press Conference Statement and a New Sentiment Indicator for the Euro Area”
  In *International Journal of Finance & Economics*, 2024
* [42]
  Simran Kaur
  “REFinD: Relation Extraction Financial Dataset”
  In *Proceedings of the 46th International ACM SIGIR Conference on Research and Development in Information Retrieval*, 2023, pp. 3054–3063
* [43]
  Hyeonjin Ko and Jinyoung Lee
  “Can ChatGPT Improve Investment Decisions from a Portfolio Management Perspective”
  In *Finance Research Letters*, 2024
* [44]
  Kai Jian Koa
  “Learning to Generate Explainable Stock Predictions Using Self-Reflective Large Language Models”
  In *arXiv preprint arXiv:2402.03659*, 2024
* [45]
  R. Koncel-Kedziorski
  “BizBench: A Quantitative Reasoning Benchmark for Business and Finance”
  In *arXiv preprint arXiv:2311.06602*, 2023
* [46]
  Yaxuan Kong
  “Large Language Models for Financial and Investment Management: Applications and Benchmarks”
  In *arXiv preprint arXiv:2402.09171*, 2024
  URL: <https://arxiv.org/abs/2402.09171>
* [47]
  Thomas Konstantinidis, George Iacovides, Mengjie Xu, Theodoros G. Constantinides and Danilo Mandic
  “FinLlama: Financial Sentiment Classification for Algorithmic Trading Applications”
  In *arXiv preprint arXiv:2403.12285*, 2024
  URL: <https://arxiv.org/abs/2403.12285>
* [48]
  Kalpesh Krishna
  “GenAudit: Fixing Factual Errors in Language Model Outputs with Evidence”
  In *arXiv preprint arXiv:2402.12566*, 2024
* [49]
  Jean Lee, Nathan Stevens, Seung Chul Han and Min Song
  “A Survey of Large Language Models in Finance (FinLLMs)”
  In *arXiv preprint arXiv:2402.02315*, 2024
  URL: <https://arxiv.org/abs/2402.02315>
* [50]
  Yue Lei
  “CFBenchmark: Chinese Financial Assistant Benchmark for Large Language Model”
  In *arXiv preprint arXiv:2311.05812*, 2023
* [51]
  Jian Li
  “CFGPT: Chinese Financial Assistant with Large Language Model”
  In *arXiv preprint arXiv:2309.10654*, 2023
* [52]
  Qian Li and Qi Zhang
  “A Unified Model for Financial Event Classification, Detection and Summarization”
  In *Proceedings of IJCAI*, 2020
* [53]
  Xiang Li, Zhen Li, Chao Shi, Yao Xu, Qiang Du, Ming Tan, Jun Huang and Wei Lin
  “AlphaFin: Benchmarking Financial Analysis with Retrieval-Augmented Stock-Chain Framework”
  In *arXiv preprint arXiv:2403.12582*, 2024
  URL: <https://arxiv.org/abs/2403.12582>
* [54]
  Xiang Victor Li
  “FinDKG: Dynamic Knowledge Graph with Large Language Models for Global Finance”
  In *SSRN*, 2023
  URL: <https://ssrn.com/abstract=4608445>
* [55]
  Yuhang Li and Yizhi Yu
  “TradingGPT: Multi-Agent System with Layered Memory and Distinct Characters for Enhanced Financial Trading Performance”
  In *arXiv preprint arXiv:2309.03736*, 2023
* [56]
  Yong Liang
  “Aligning Large Language Models to a Domain-Specific Graph Database”
  In *arXiv preprint arXiv:2402.16567*, 2024
* [57]
  Yue Liang
  “Foundation Models for Time Series Analysis: A Tutorial and Survey”
  In *arXiv preprint arXiv:2403.14735*, 2024
* [58]
  Junhua Liu
  “A Survey of Financial AI: Architectures, Advances and Open Challenges”
  In *arXiv preprint arXiv:2403.06761*, 2024
  URL: <https://arxiv.org/abs/2403.06761>
* [59]
  Xiao-Yong Liu and Jing Zhang
  “FinGPT-HPC: Efficient Pretraining and Finetuning Large Language Models for Financial Applications with High-Performance Computing”
  In *arXiv preprint arXiv:2402.13533*, 2024
* [60]
  Xin Liu and Chenyang Zhang
  “When AI Meets Finance (StockAgent): Large Language Model-Based Stock Trading in Simulated Real-World Environments”, Manuscript, 2024
* [61]
  Yinhan Liu and Myle Ott
  “RoBERTa: A Robustly Optimized BERT Pretraining Approach”
  In *arXiv:1907.11692*, 2019
  URL: <https://arxiv.org/abs/1907.11692>
* [62]
  Zhuang Liu
  “FinBERT: A Pre-Trained Financial Language Representation Model for Financial Text Mining”
  In *Proceedings of IJCAI*, 2021
* [63]
  Alejandro Lopez-Lira and Yuehua Tang
  “Can ChatGPT Forecast Stock Price Movements? Return Predictability and Large Language Models”
  In *arXiv preprint arXiv:2304.07619*, 2023
* [64]
  Tim Loughran and Bill McDonald
  “When Is a Liability Not a Liability? Textual Analysis, Dictionaries, and 10-Ks”
  In *The Journal of Finance* 66.1, 2011, pp. 35–65
* [65]
  Wenjie Luo and Di Gong
  “Pre-trained Large Language Models for Financial Sentiment Analysis”
  In *arXiv preprint arXiv:2401.05215*, 2024
* [66]
  Qiang Ma et al.
  “Computational Experiments Meet Large Language Model Based Agents: A Survey and Perspective”
  In *arXiv preprint arXiv:2402.00262*, 2024
  URL: <https://arxiv.org/abs/2402.00262>
* [67]
  Shibo Ma
  “The Era of 1-Bit LLMs: All Large Language Models Are in 1.58 Bits”
  In *arXiv preprint arXiv:2402.17764*, 2024
* [68]
  Ritwik Mathur
  “MONOPOLY: A Multimodal Dataset of Monetary Policy Press Conferences”
  In *Proceedings of LREC*, 2022
* [69]
   Meta AI
  “Introducing Meta Llama 3”, <https://ai.meta.com/blog/meta-llama-3/>, 2024
* [70]
  Kiril Mishev
  “Evaluation of Sentiment Analysis in Finance: From Lexicons to Transformers”
  In *IEEE Access* 8, 2020, pp. 131662–131682
* [71]
  Ritam Mukherjee
  “ECTSum: A New Benchmark Dataset for Bullet Point Summarization of Long Earnings Call Transcripts”
  In *arXiv preprint arXiv:2210.12467*, 2022
* [72]
  Peter Nagy
  “Generative AI for End-to-End Limit Order Book Modelling”
  In *Proceedings of the ACM International Conference on AI in Finance*, 2023
* [73]
  Yuqi Nie
  “A Time Series Is Worth 64 Words: Long-Term Forecasting with Transformers”
  In *arXiv preprint arXiv:2211.14730*, 2022
* [74]
  Yuqi Nie
  “A Survey of Large Language Models for Financial Applications: Progress, Prospects and Challenges”
  In *arXiv preprint arXiv:2404.01328*, 2024
  URL: <https://arxiv.org/abs/2404.01328>
* [75]
  Jeff Z. Pan
  “Large Language Models and Knowledge Graphs: Opportunities and Challenges”
  In *arXiv preprint arXiv:2308.06374*, 2023
* [76]
  Sihang Pan
  “Unifying Large Language Models and Knowledge Graphs: A Roadmap”
  In *IEEE Transactions on Knowledge and Data Engineering*, 2024
* [77]
  James W. Pennebaker, Martha E. Francis and Roger J. Booth
  “Linguistic Inquiry and Word Count: LIWC 2001”
  Lawrence Erlbaum Associates, 2001
* [78]
  Karan S. Phogat, Chandra Harsha, Sriram Dasaratha, Srinivasa Ramakrishna and S. Puranam
  “Zero-shot Question Answering over Financial Documents Using Large Language Models”
  In *arXiv preprint arXiv:2311.14722*, 2023
  URL: <https://arxiv.org/abs/2311.14722>
* [79]
  Yunliang Quan and Zichao Liu
  “EconLogicQA: A Question Answering Benchmark for Evaluating Large Language Models in Economic Sequential Reasoning”
  In *arXiv preprint arXiv:2405.07938*, 2024
* [80]
  Moreno La Quatra and Luca Cagliero
  “End-to-End Training for Financial Report Summarization”
  In *Proceedings of the 1st Joint Workshop on Financial Narrative Processing and MultiLing Financial Summarisation*, 2020
* [81]
  Alec Radford, Karthik Narasimhan, Tim Salimans and Ilya Sutskever
  “Improving Language Understanding by Generative Pre-Training”
  In *OpenAI Technical Report*, 2018
* [82]
  Alec Radford and Jeff Wu
  “Language Models are Unsupervised Multitask Learners”
  In *OpenAI Blog* 1.8, 2019
* [83]
  Prateek Kumar Rajpoot and Anuj Parikh
  “GPT-FinRE: In-Context Learning for Financial Relation Extraction Using Large Language Models”
  In *arXiv preprint arXiv:2306.17519*, 2023
* [84]
  Sourya Sarkar and Khashayar Vafa
  “Lookahead Bias in Pretrained Language Models”
  In *SSRN*, 2024
* [85]
  Teven Le Scao and Angela Fan
  “BLOOM: A 176B-Parameter Open-Access Multilingual Language Model”
  In *arXiv preprint arXiv:2211.05100*, 2023
  URL: <https://arxiv.org/abs/2211.05100>
* [86]
  Aaditya Shah and Rishabh Vithani
  “FiNER: Financial Named Entity Recognition Dataset and Weak-Supervision Model”
  In *arXiv preprint arXiv:2302.11157*, 2023
* [87]
  Shivam Sharma
  “FinRED: A Dataset for Relation Extraction in the Financial Domain”
  In *Companion Proceedings of The Web Conference*, 2022
* [88]
  Piyush Srivastava, Mudit Malik and Tathagata Ganu
  “Assessing LLMs’ Mathematical Reasoning in Financial Document Question Answering”
  In *arXiv preprint arXiv:2402.11194*, 2024
  URL: <https://arxiv.org/abs/2402.11194>
* [89]
  Robert Steinert and Sebastian Altmann
  “Linking Microblogging Sentiments to Stock Price Movement: An Application of GPT-4”
  In *arXiv preprint arXiv:2308.16771*, 2023
* [90]
  Philip J. Stone, Dexter C. Dunphy and Marshall S. Smith
  “The General Inquirer: A Computer Approach to Content Analysis”
  MIT Press, 1966
* [91]
  Liang Tan, Chee-Pun Lee and Kok-Ming Lim
  “A Survey of Sentiment Analysis: Approaches, Datasets, and Future Research”
  In *Applied Sciences* 13.7, 2023, pp. 4550
* [92]
  Chao Tian, Yan Zhao and Li Ren
  “A Chinese Event Relation Extraction Model Based on BERT”
  In *Proceedings of ICAIBD*, 2019
* [93]
  Hanyu Tong
  “Ploutos: Towards Interpretable Stock Movement Prediction with Financial Large Language Model”
  In *arXiv preprint arXiv:2403.00782*, 2024
* [94]
  Hugo Touvron
  “LLaMA 2: Open Foundation and Fine-Tuned Chat Models”
  In *arXiv preprint arXiv:2307.09288*, 2023
  URL: <https://arxiv.org/abs/2307.09288>
* [95]
  Hugo Touvron
  “LLaMA: Open and Efficient Foundation Language Models”
  In *arXiv preprint arXiv:2302.13971*, 2023
  URL: <https://arxiv.org/abs/2302.13971>
* [96]
  Ashish Vaswani and Noam Shazeer
  “Attention Is All You Need”
  In *Advances in Neural Information Processing Systems*, 2017
* [97]
  Qiang Wan
  “CFERE: Multi-Type Chinese Financial Event Relation Extraction”
  In *Information Sciences* 630, 2023, pp. 119–134
* [98]
  Dian Wang
  “DocLLM: A Layout-Aware Generative Language Model for Multimodal Document Understanding”
  In *arXiv preprint arXiv:2401.00908*, 2024
* [99]
  Shiqi Wang and Huan Yuan
  “Alpha-GPT: Human-AI Interactive Alpha Mining for Quantitative Investment”
  In *arXiv preprint arXiv:2308.00016*, 2023
* [100]
  Shiqi Wang and Huan Yuan
  “QuantAgent: Seeking Holy Grail in Trading by Self-Improving Large Language Model”
  In *arXiv preprint arXiv:2402.03755*, 2024
* [101]
  Zhen Wang and Yuxuan Li
  “FinVisGPT: A Multimodal Large Language Model for Financial Chart Analysis”
  In *arXiv preprint arXiv:2308.01430*, 2023
* [102]
  Jason Wei
  “Finetuned Language Models Are Zero-Shot Learners”
  In *arXiv preprint arXiv:2109.01652*, 2021
* [103]
  Qingsong Wen
  “Transformers in Time Series: A Survey”
  In *arXiv preprint arXiv:2202.07125*, 2022
* [104]
  Christian Wimmer and Nasser Rekabsaz
  “Leveraging Vision-Language Models for Granular Market Change Prediction”
  In *arXiv preprint arXiv:2301.10166*, 2023
* [105]
  Shijie Wu and Ozan Irsoy
  “BloombergGPT: A Large Language Model for Finance”
  In *arXiv preprint arXiv:2303.17564*, 2023
  URL: <https://arxiv.org/abs/2303.17564>
* [106]
  Zihan Xi et al.
  “The Rise and Potential of Large Language Model Based Agents: A Survey”
  In *arXiv preprint arXiv:2309.07864*, 2023
  URL: <https://arxiv.org/abs/2309.07864>
* [107]
  Qianqian Xie
  “PIXIU: A Large Language Model, Instruction Data and Evaluation Benchmark for Finance”
  In *arXiv preprint arXiv:2306.05443*, 2023
* [108]
  Qianqian Xie
  “The FinBen: An Holistic Financial Benchmark for Large Language Models”
  In *arXiv preprint arXiv:2402.12659*, 2024
* [109]
  Jun Xu
  “GenAI and LLM for Financial Institutions: A Corporate Strategic Survey”
  In *arXiv preprint arXiv:2403.03375*, 2024
  URL: <https://arxiv.org/abs/2403.03375>
* [110]
  Liang Xu
  “SuperCLUE-Fin: Graded Fine-Grained Analysis of Chinese LLMs on Diverse Financial Tasks and Applications”
  In *arXiv preprint arXiv:2404.19063*, 2024
* [111]
  Shuohang Xue
  “WeaverBird: Empowering Financial Decision-Making with Large Language Model, Knowledge Base, and Search Engine”
  In *arXiv preprint arXiv:2308.05361*, 2023
* [112]
  Hongyang Yang, Xiao-Yong Liu and Chaojun Wang
  “FinGPT: Open-Source Financial Large Language Models”
  In *arXiv preprint arXiv:2306.06031*, 2023
* [113]
  Yi Yang, Mark Christopher Siy Uy and Allen Huang
  “FinBERT: A Pretrained Language Model for Financial Communications”
  In *arXiv preprint arXiv:2006.08097*, 2020
* [114]
  Yifan Yang, Yifan Tang and K.. Tam
  “InvestLM: A Large Language Model for Investment Using Financial Domain Instruction Tuning”
  In *arXiv preprint arXiv:2309.13064*, 2023
* [115]
  Yizheng Yao
  “A Survey on Large Language Model Security and Privacy”
  In *High Confidence Computing*, 2024, pp. 100211
* [116]
  Antonio Jose Yepes and Yuxuan You
  “Financial Report Chunking for Effective Retrieval Augmented Generation”
  In *arXiv preprint arXiv:2402.05131*, 2024
* [117]
  Jingyuan Yu, Michael Huber and Kevin Tang
  “GreedLlama: Performance of Financial Value-Aligned Large Language Models in Moral Reasoning”
  In *arXiv preprint arXiv:2404.02934*, 2024
  URL: <https://arxiv.org/abs/2404.02934>
* [118]
  Yuxin Yu
  “FinMem: A Performance-Enhanced LLM Trading Agent with Layered Memory and Character Design”
  In *Proceedings of the AAAI Symposium Series*, 2024
* [119]
  Huan Yuan, Shiqi Wang and Jun Guo
  “Alpha-GPT 2.0: Human-in-the-Loop AI for Quantitative Investment”
  In *arXiv preprint arXiv:2402.09746*, 2024
* [120]
  Tianyi Yuan
  “R-Judge: Benchmarking Safety Risk Awareness for LLM Agents”
  In *arXiv preprint arXiv:2401.10019*, 2024
* [121]
  Tian Yue and David Au
  “GPTQuant’s Conversational AI: Simplifying Investment Research for All”, SSRN 4380516, 2023
* [122]
  Bo Zhang and Haohan Yang
  “Enhancing Financial Sentiment Analysis via Retrieval Augmented Large Language Models”
  In *Proceedings of the ACM International Conference on AI in Finance*, 2023
* [123]
  Bo Zhang and Haohan Yang
  “Instruct-FinGPT: Financial Sentiment Analysis by Instruction Tuning of General-Purpose LLMs”
  In *arXiv preprint arXiv:2306.12659*, 2023
* [124]
  Lei Zhang
  “FinEval: A Chinese Financial Domain Knowledge Evaluation Benchmark for Large Language Models”
  In *arXiv preprint arXiv:2308.09975*, 2023
* [125]
  Wei Zhang and Linqi Zhao
  “FinAgent: A Multimodal Foundation Agent for Financial Trading”
  In *arXiv preprint arXiv:2402.18485*, 2024
* [126]
  Xiang Zhang
  “Dólares or Dollars? Unraveling the Bilingual Prowess of Financial LLMs Between Spanish and English”
  In *arXiv preprint arXiv:2402.07405*, 2024
* [127]
  Zeyu Zhang, Xin Bo, Chen Ma, Ruoxuan Li, Xuanjing Chen, Qi Dai, Jun Zhu, Zhengdong Dong and Ji-Rong Wen
  “A Survey on the Memory Mechanism of Large Language Model Based Agents”
  In *arXiv preprint arXiv:2404.13501*, 2024
  URL: <https://arxiv.org/abs/2404.13501>
* [128]
  Huaqin Zhao et al.
  “Revolutionizing Finance with LLMs: An Overview of Applications and Insights”
  In *arXiv preprint arXiv:2401.11641*, 2024
  URL: <https://arxiv.org/abs/2401.11641>
* [129]
  Yiran Zhao
  “DocMathEval: Evaluating Numerical Reasoning Capabilities of LLMs in Understanding Long Documents with Tabular Data”
  In *arXiv preprint arXiv:2311.09805*, 2023
* [130]
  Tian Zhou
  “FEDformer: Frequency Enhanced Decomposed Transformer for Long-Term Series Forecasting”
  In *Proceedings of the International Conference on Machine Learning*, 2022
* [131]
  Yingyu Zhou
  “SilverSight: A Multi-Task Chinese Financial Large Language Model Based on Adaptive Semantic Space Learning”
  In *arXiv preprint arXiv:2404.04949*, 2024
* [132]
  Junkai Zhu
  “Benchmarking Large Language Models on CFLUE: A Chinese Financial Language Understanding Evaluation Dataset”
  In *arXiv preprint arXiv:2405.10542*, 2024
* [133]
  Nabil Zmandar
  “Joint Abstractive and Extractive Method for Long Financial Document Summarization”
  In *Proceedings of the 3rd Financial Narrative Processing Workshop*, 2021
* [134]
  Maksim Zwam
  “Knowledge Graphs for Financial Services”, <https://www2.deloitte.com/content/dam/Deloitte/de/Documents/operations/knowledge-graphs-pov.pdf>, 2020