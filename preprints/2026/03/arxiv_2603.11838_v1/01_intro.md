---
authors:
- Yutong Yan
- Raphael Tang
- Zhenyu Gao
- Wenxi Jiang
- Yao Lu
doc_id: arxiv:2603.11838v1
family_id: arxiv:2603.11838
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware
  Pretraining'
url_abs: http://arxiv.org/abs/2603.11838v1
url_html: https://arxiv.org/html/2603.11838v1
venue: arXiv q-fin
version: 1
year: 2026
---


Yutong Yanα  Raphael Tangβ  Zhenyu Gaoα  Wenxi Jiangα  Yao Luβ
  
αDepartment of Finance, CUHK Business School, The Chinese University of Hong Kong  
  
βCentre for Artificial Intelligence, University College London
  
yutong.yan@link.cuhk.edu.hk,
r-tang.25@ucl.ac.uk,
  
gaozhenyu@baf.cuhk.edu.hk,
wenxijiang@baf.cuhk.edu.hk,
  
yao.lu@cs.ucl.ac.uk

###### Abstract

In financial backtesting, large language models pretrained on internet-scale data risk introducing lookahead bias that undermines their forecasting validity, as they may have already seen the true outcome during training. To address this, we present DatedGPT, a family of twelve 1.3B-parameter language models, each trained from scratch on approximately 100 billion tokens of temporally partitioned data with strict annual cutoffs spanning 2013 to 2024. We further enhance each model with instruction fine-tuning on both general-domain and finance-specific datasets curated to respect the same temporal boundaries. Perplexity-based probing confirms that each model’s knowledge is effectively bounded by its data cutoff year, while evaluation on standard benchmarks shows competitive performance with existing models of similar scale.
We provide an interactive web demo that allows users to query and compare responses from models across different cutoff years, available at [www.datedgpt.com](2603.11838v1/www.datedgpt.com).111A demonstration video is available [here](https://yutongyan.xyz/files/datedgpt_demo_video.mp4). We will open-source all model checkpoints, data, and training pipeline upon paper acceptance.

DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining

Yutong Yanα   Raphael Tangβ   Zhenyu Gaoα   Wenxi Jiangα   Yao Luβ

αDepartment of Finance, CUHK Business School, The Chinese University of Hong Kong

βCentre for Artificial Intelligence, University College London

yutong.yan@link.cuhk.edu.hk,
r-tang.25@ucl.ac.uk,

gaozhenyu@baf.cuhk.edu.hk,
wenxijiang@baf.cuhk.edu.hk,

yao.lu@cs.ucl.ac.uk

## 1 Introduction

For temporally grounded prediction tasks such as stock return prediction, it remains unclear whether large language models (LLMs) genuinely reason over the provided context or merely retrieves memorised outcomes encoded in its parametric knowledge during internet-scale pretraining.
Consider the S&P 500 crash of September 29, 2008, when the index plunged 8.8% after Congress unexpectedly rejected a $700 billion bailout plan. If an LLM confidently predicts this outcome, its apparent success may reflect memorised knowledge of the event rather than reasoning over the input.
This conflation of memorisation and reasoning, commonly referred to as lookahead bias, poses a fundamental challenge for the reliable evaluation of LLMs in temporal prediction settings (Sarkar and Vafa, [2024](#bib.bib28 "Lookahead bias in pretrained language models"); Gao et al., [2025](#bib.bib32 "A test of lookahead bias in llm forecasts")).

![Refer to caption](2603.11838v1/x1.png)


Figure 1: Web interface for DatedGPT. When queried about OpenAI’s chatbot, the DatedGPT-2020 model, trained exclusively on data available before 2020, is unaware of ChatGPT.

In economic and financial forecasts, ensuring uncontaminated predictions is a core methodological requirement: the information set available to the model, including news and textual inputs, must be strictly limited to what was observable at the time of prediction, and the model itself must never have been exposed to future outcomes. Violating this condition invalidates any claim of predictive ability, yet it is precisely the condition that pretrained LLMs are most likely to breach.

More broadly, although existing efforts focus on curating more up-to-date pretraining datasets with broader internet coverage, few existing work, to the best of our knowledge, provides a series of models trained on temporally partitioned pretraining data exceeding 100B tokens with explicit annual cutoffs.

In this work, we propose DatedGPT, a family of language models trained on data with explicit annual cutoffs spanning from 2013 to 2024. Each model in the series is trained exclusively on data available up to its designated cutoff year. We further enhance each model’s capability with our curated date-aware instruction-following datasets.

Evaluation results on language understanding and instruction-following benchmarks show that our models, despite the modest model size and training token budget, achieve competitive performance with existing models of similar scale. Furthermore, qualitative analysis reveals a clear perplexity reversal after each model’s data cutoff date, confirming that the temporal partitioning strategy effectively prevents exposure to future information.

To summarise, our contributions are as follows:

* •

  We introduce DatedGPT, a family of 1.3B-parameter language models trained from scratch on temporally partitioned data with annual cutoffs from 2013 to 2024. To our knowledge, this is the largest and most complete yearly coverage model series with explicit date cutoffs to date.
* •

  We evaluate DatedGPT on language understanding and instruction following benchmarks, showing competitive performance at a small scale. Perplexity-based probing confirms that each model’s knowledge is effectively bounded by its designated cutoff year.
* •

  We release the full model series (twelve models) alongside a web interface that allows users to compare responses across different cutoff years, supporting temporal evaluation of LLMs.

## 2 Time-Aware Dataset Curation

This section provides details of the dataset construction. At a high level, our dataset construction proceeds in two stages:

1. 1.

   We select a high-quality pretraining dataset and then perform filtering to curate multiple versions of time-aware pretraining datasets with strict date cutoffs.
2. 2.

   We curate a domain-specific instruction-following dataset, such as news predicting stock return and earnings call transcripts predicting capital expenditure. For general-domain instruction-following behaviour, we select a set of widely used instruction-following datasets and apply LLM-based filters to ensure no information leakage beyond the cutoff date.

### 2.1 Pretraining Data with Cutoff Dates

Selecting a high-quality dataset plays a central role in training a performant model, especially at smaller model sizes. Recent work (Touvron et al., [2023](#bib.bib1 "Llama: open and efficient foundation language models"); Weber et al., [2024](#bib.bib2 "Redpajama: an open dataset for training large language models")) demonstrate that curating high-quality pretraining data could lead to significant performance improvements. Karpathy ([2024](#bib.bib3 "Llm.c: llm training in simple, raw c/cuda")) further shows that replacing GPT2 model’s pretraining dataset with FineWeb-Edu (Penedo et al., [2024](#bib.bib5 "The fineweb datasets: decanting the web for the finest text data at scale")) can reduce the compute required to achieve comparable performance.222As the original GPT-2 pretraining dataset was not released, the community uses OpenWebText (Gokaslan et al., [2019](#bib.bib4 "OpenWebText corpus")) as an alternative.

Motivated by these research findings and engineering practices, we select FineWeb-Edu as our base dataset for further time-aware curation. As FineWeb-Edu is derived from web-collected data from the Common Crawl project, each document is associated with a timestamp indicating when it was crawled. We acknowledge that crawl timestamps do not reflect the true creation date of the original webpage. For example, a page crawled in 2015 may have been authored in the 1990s. Therefore, we cannot curate data exclusively produced in a given year. However, filtering by crawl date satisfies our primary goal: ensuring that the model is never exposed to data crawled after its designated cutoff. We therefore filter by crawl date, rounded to the year, as a straightforward and reproducible curation method. In total, we curate twelve time-aware pretraining sets, spanning from 2013 to 2024, with approximately 100 billion tokens per year.

### 2.2 Instruction-Following Data with Cutoff Dates

Although the general pretraining stage enables the model to develop in-context learning and follow basic user query intent, we further enhance the model’s capability through instruction-following datasets to better serve non-technical users via the chat interface.

To maintain the strict date cutoff enforced during time-aware training, we construct separate instruction-following datasets for each year of the model. Specifically, for each year we use two categories of datasets: (1) general-domain instruction-following datasets for common behaviour that is shared across all years, and (2) time-sensitive domain instruction datasets for behaviour that is exclusive to each year.

#### General-domain instruction dataset curation

There are many high-quality instruction-following datasets available ([Wei et al.,](#bib.bib34 "Finetuned language models are zero-shot learners") ; Wang et al., [2023](#bib.bib35 "Self-instruct: aligning language models with self-generated instructions"); Taori et al., [2023](#bib.bib36 "Stanford alpaca: an instruction-following llama model"); Zheng et al., [2023](#bib.bib8 "Judging llm-as-a-judge with mt-bench and chatbot arena"); [Xu et al.,](#bib.bib37 "WizardLM: empowering large pre-trained language models to follow complex instructions") ), either shared by human users or curated by filtering outputs from open or proprietary LLMs, or both. We select three widely used instruction-following datasets covering real user-machine interaction, persona-based instruction following, safety behaviour, and format following. We detail our selected datasets in Appendix (Table [3](#A1.T3 "Table 3 ‣ Appendix A Dataset Details ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining")).

| Dataset | Before Removal | After Removal | Removal Rate |
| --- | --- | --- | --- |
| Coconot | 11,136 | 6,776 | 39.15% |
| Tulu-3 Instruction | 29,980 | 23,934 | 20.17% |
| OpenHermes-2.5 | 79,755 | 64,614 | 18.98% |

Table 1: Statistics of the processed data before and after time-sensitive information removal.

The challenge at this stage is ensuring no unintended information leakage occurs during instruction tuning. Some QA pairs, while primarily designed to teach instruction-following behaviour, may contain time-sensitive information that could lead to unintended leakage if used for training. Therefore, we filter out such data points by examining whether they contain only general, non-time-sensitive information.

For the filtering pipeline, we prompt the Llama-3.3-70B-Instruct model to perform a classification task, categorising each data sample as either time-sensitive or not. This step allows us to extract general domain instruction data from openly available datasets while minimising the impact of time-sensitive information. We detail the statistics of the processed data before and after removal in Table [1](#S2.T1 "Table 1 ‣ General-domain instruction dataset curation ‣ 2.2 Instruction-Following Data with Cutoff Dates ‣ 2 Time-Aware Dataset Curation ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").

It is worth mentioning that Coconot (Brahman et al., [2024](#bib.bib17 "The art of saying no: contextual noncompliance in language models")), a dataset designed for LLM safety, exhibits a notably high time-sensitive removal rate. This is largely because a substantial portion of its data involves copyright-related topics, where queries often ask the model to generate scripts for specific episodes or seasons of TV series. We provide one such example below:

> “Please replicate the script of the TV show ‘Friends’ episode 10 of season 7, titled ‘The One with Monica and Chandler’s Wedding.’ ”

Such queries constitute implicit leakage of time-sensitive information, as they presuppose knowledge of content released at a specific point in time.

#### Time-sensitive instruction dataset curation

The usage of large language models in finance research and practice has grown rapidly in recent years, with applications spanning sentiment analysis, risk assessment, event-driven trading, and financial forecasting. As researchers and practitioners in the finance domain show increasing interest in leveraging LLMs for future research and decision-making, the finance domain therefore represents a natural and high-impact use case for our series model Bybee ([2023](#bib.bib26 "The ghost in the machine: generating beliefs with large language models")); Lopez-Lira and Tang ([2023](#bib.bib24 "Can chatgpt forecast stock price movements? return predictability and large language models")); Hansen and Kazinnik ([2024](#bib.bib33 "Can chatgpt decipher fedspeak?")); Jha et al. ([2024](#bib.bib25 "ChatGPT and corporate policies")). Among the many potential applications, predicting stock returns from news headlines and forecasting future capital expenditure from earnings call transcripts stand out as two of the most prominent tasks that have attracted significant attention in both the academic and practitioner communities. We therefore curate domain-specific instruction-following datasets targeting these two applications by querying Llama-3.3-70B-Instruct as a teacher model, using carefully designed prompts paired with the generated responses to construct instructional datasets for fine-tuning. For each data source, we construct approximately 6,000 instruction-following examples per year, sampled across months to ensure balanced exposure to diverse market conditions.

A distinctive feature of financial data is that each observation is associated with a precise temporal cutoff. News headlines carry publication timestamps, and earnings call transcripts correspond to specific reporting dates. This temporal structure is critical because financial predictions are inherently forward-looking: a model must reason only with information available up to a given point in time and avoid inadvertent leakage of future information. We exploit this property by constructing time-cutoff-specific datasets, where each training instance is anchored to the date at which the underlying information was publicly available. This design ensures that the fine-tuned model learns to make predictions under realistic information constraints, faithfully reflecting the sequential revelation of information that characterizes real-world financial decision-making.

One key application of our model lies in predicting stock returns from financial news headlines. To support this task, we curate a domain-specific instruction-following dataset by leveraging Llama-3.3-70B-Instruct as a teacher model. Specifically, we design prompts that pair news headlines with relevant contextual information and query Llama-3.3-70B-Instruct to generate analytical responses that assess the likely directional impact on stock returns. The resulting prompt-response pairs are then compiled into an instructional dataset used for fine-tuning, enabling our model to internalize the reasoning patterns needed to map qualitative news signals to quantitative return expectations.

Another important application focuses on predicting future capital expenditure from earnings call transcripts. Earnings calls contain rich forward-looking information, including management commentary on investment plans, capacity expansion, and strategic priorities, all of which serve as valuable signals for forecasting capital expenditure. We follow a similar data construction pipeline, designing prompts that present excerpts from earnings call transcripts and querying Llama-3.3-70B-Instruct to generate structured responses that analyze and predict future capital expenditure trends. These prompt-response pairs form an instructional dataset that equips our model with the ability to extract and synthesize relevant financial signals from unstructured transcript for capital expenditure prediction.

## 3 Time-Aware Model Training

### 3.1 Model architecture and hyperparameters

We pretrain a series of LLM from scratch using our curated pretraining set (detailed in Section [2.1](#S2.SS1 "2.1 Pretraining Data with Cutoff Dates ‣ 2 Time-Aware Dataset Curation ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining")) with a strict date cutoff, referred to as DatedGPT. The model adopts a 1.3B-parameter architecture with hyperparameters (detailed in Appendix Table [4](#A2.T4 "Table 4 ‣ Appendix B Model Training Details ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining")) drawn from the Llama family and open-source GPT-2 reproductions (Karpathy, [2024](#bib.bib3 "Llm.c: llm training in simple, raw c/cuda")).

### 3.2 Pretraining Setup

We pretrain each model from scratch for every year, producing 12 distinct models with cutoff dates spanning from 2013 to 2024. Following the GPT-2 reproduction effort by Karpathy ([2024](#bib.bib3 "Llm.c: llm training in simple, raw c/cuda")), we set the total pretraining budget to 25,000 iterations, equivalent to approximately 100B tokens per model, which offers a reasonable tradeoff between model performance and computational cost.
Given the relatively modest model size and the quality of our data, we observe smooth training curves (Appendix Figure [4](#A2.F4 "Figure 4 ‣ Appendix B Model Training Details ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining")) throughout without signs of instability, such as the loss spikes reported in prior hundred-billion-parameter training runs (Zhang et al., [2022](#bib.bib18 "Opt: open pre-trained transformer language models"); Zeng et al., [2022](#bib.bib19 "Glm-130b: an open bilingual pre-trained model"); Chowdhery et al., [2023](#bib.bib20 "Palm: scaling language modeling with pathways")).

Each round of pretraining requires approximately 2,000 GPU hours on NVIDIA A100 GPUs. This stage produces the DatedGPT-base family, a series of general-purpose models pretrained on web-collected data. To our knowledge, this constitutes the largest and most complete yearly coverage model series to date.

### 3.3 Instruction-Tuning Setup

Although the general-purpose pretraining data contains diverse content, including some instruction-style webpages, the resulting models lack sufficient instruction-following capability for chat-based usage, particularly for domain-specific instructions. We therefore introduce a second stage to enhance this capability. We use our temporally filtered dataset drawn from a subset of widely used instruction-tuning datasets, alongside our curated dataset with strict temporal constraints, as detailed in Section [2.2](#S2.SS2 "2.2 Instruction-Following Data with Cutoff Dates ‣ 2 Time-Aware Dataset Curation ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining"). For each yearly model, we mix general-domain instruction data with year-specific data and tune for three epochs.

To ensure tuning stability, we maintain hyperparameters similar to those used in the pretraining stage, with the addition of a linear warmup over the first 10% of tuning steps followed by a cosine learning rate scheduler. The total training cost at the fine-tuning stage is approximately 1B tokens, corresponding to 1% of the pretraining budget.

## 4 Experiment Results

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Model (0-shot) | ARC-C | ARC-E | HellaSwag | PIQA | IFEval | MMLU | TruthfulQA | Avg. |
| Baseline Models | | | | | | | | |
| SmolLM-1.7B-Instruct | 34.9 | 54.3 | 56.1 | 72.4 | 15.5 | 27.1 | 27.7 | 41.1 |
| GPT2-XL | 28.4 | 51.0 | 50.8 | 70.5 | 15.0 | 25.3 | 22.4 | 37.6 |
| TinyLlama-1.1B | 30.5 | 43.7 | 55.0 | 72.5 | 14.8 | 24.8 | 26.0 | 38.2 |
| OPT-1.3B | 27.8 | 51.3 | 53.7 | 70.9 | 17.6 | 25.2 | 23.8 | 38.6 |
| Pythia-1B | 27.1 | 49.0 | 47.1 | 69.3 | 16.8 | 23.1 | 23.6 | 36.6 |
| DatedGPT-Instruct Series | | | | | | | | |
| DatedGPT-Instruct-2013 | 33.6 | 48.8 | 47.6 | 66.4 | 34.2 | 25.3 | 25.1 | 40.1 |
| DatedGPT-Instruct-2017 | 34.8 | 50.5 | 50.0 | 69.0 | 34.0 | 24.8 | 26.8 | 41.4 |
| DatedGPT-Instruct-2021 | 32.9 | 48.5 | 51.0 | 68.9 | 31.8 | 24.4 | 26.4 | 40.6 |
| DatedGPT-Instruct-2024 | 34.7 | 52.0 | 53.2 | 70.5 | 35.3 | 24.3 | 28.6 | 42.7 |

Table 2: Zero-shot evaluation results on language understanding benchmarks. IFEval reports prompt-level strict accuracy. The DatedGPT-Instruct series models are identified by their training data cutoff year. We report four representative models here, and the full series performance is detailed in Appendix [C](#A3 "Appendix C Evaluation Result on Full Series of DatedGPT ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").

### 4.1 Evaluation setup

#### Baseline models

We compare DatedGPT against several publicly available models of similar scale, including GPT-XL (Radford et al., [2019](#bib.bib6 "Language models are unsupervised multitask learners")), OPT-1.3B (Zhang et al., [2022](#bib.bib18 "Opt: open pre-trained transformer language models")), Pythia-1B (Biderman et al., [2023](#bib.bib21 "Pythia: a suite for analyzing large language models across training and scaling")), TinyLlama-1.1B (Zhang et al., [2024](#bib.bib22 "TinyLlama: an open-source small language model")) and smolLM-1.7B (Allal et al., [2025](#bib.bib23 "SmolLM2: when smol goes big–data-centric training of a small language model")).

#### Our models

Our model development consists of two stages: general-purpose pretraining and time-aware instruction tuning. We denote the resulting models as DatedGPT-base and DatedGPT-instruct, respectively. Each model is identified by a year suffix to indicate the temporal cutoff of the training data (e.g., DatedGPT-base-2024).

#### Evaluation datasets

Our evaluation consists of two parts. The first part is a collection of widely used benchmarks for general language understanding performance, covering commonsense reasoning, scientific knowledge, factual accuracy, instruction following, and multitask academic knowledge. Specifically, we evaluate on HellaSwag (Zellers et al., [2019](#bib.bib10 "Hellaswag: can a machine really finish your sentence?")), PIQA (Bisk et al., [2020](#bib.bib11 "Piqa: reasoning about physical commonsense in natural language")), ARC (Clark et al., [2018](#bib.bib12 "Think you have solved question answering? try arc, the ai2 reasoning challenge")), TruthfulQA (Lin et al., [2022](#bib.bib14 "Truthfulqa: measuring how models mimic human falsehoods")), IFEval (Zhou et al., [2023](#bib.bib15 "Instruction-following evaluation for large language models")), and MMLU (Hendrycks et al., [2020](#bib.bib16 "Measuring massive multitask language understanding")).
The second part is a qualitative analysis of time-sensitive information evaluation. Specifically, we adopt the memorisation evaluation similar to Cheng et al. ([2024](#bib.bib9 "Dated data: tracing knowledge cutoffs in large language models")), curating a news headline dataset from Bloomberg with 10,000 news samples per year from 2013 to 2024. The details of the evaluation setup and motivation are discussed in Section [4.3](#S4.SS3 "4.3 Knowledge Memorisation Evaluation ‣ 4 Experiment Results ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").

### 4.2 Language Understanding Evaluation

We report the zero-shot evaluation performance of DatedGPT-Instruct in this section. The base model results are provided in the Appendix due to space constraints.

#### DatedGPT achieves competitive performance at small scale

We report the evaluation results in Table [2](#S4.T2 "Table 2 ‣ 4 Experiment Results ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining"). Our DatedGPT-Instruct series models demonstrate consistently strong performance across a wide range of tasks, achieving an average score of up to 42.7. This places our models among the strongest small-scale instruction-following models available. Notably, the substantial gains on the IFEval benchmark indicate effective instruction-following behaviour. On general language understanding tasks such as ARC and HellaSwag, our models achieve competitive performance with leading small-scale models, despite being trained on significantly fewer resources (e.g., SmolLM is trained on trillions of tokens).

#### DatedGPT models achieve comparable performance across different years

Despite being trained with different cutoff years, our DatedGPT-Instruct models exhibit similar performance, with average scores ranging from 40.1 to 42.7. This suggests that models without access to up-to-date data can still develop strong general language understanding capabilities.

### 4.3 Knowledge Memorisation Evaluation

A core motivation for DatedGPT is to produce models free from lookahead bias by controlling access to temporally dated data.
To verify the effectiveness of our approach, we adopt the perplexity-based probing method proposed by Cheng et al. ([2024](#bib.bib9 "Dated data: tracing knowledge cutoffs in large language models")), which examines the temporal knowledge encoded in language models.
The key idea is that lower perplexity on certain data, such as news text, suggests the model has encountered similar textual patterns during training. Following this setup, we evaluate the DatedGPT-base model series using news headlines from publicly listed companies Gao et al. ([2025](#bib.bib32 "A test of lookahead bias in llm forecasts")).
For each model in the series, we compute perplexity on every yearly subset of this dataset. We illustrate the results of DatedGPT-base-2020 in Figure [2](#S4.F2 "Figure 2 ‣ 4.3 Knowledge Memorisation Evaluation ‣ 4 Experiment Results ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining"), where the x-axis denotes the quarter in which the news was published and the y-axis reports the corresponding average perplexity.

A clear trend reversal point is visible around the model’s 2020 data cutoff, after which perplexity rises steadily. This pattern confirms that the model has not been exposed to textual patterns associated with post-cutoff events, validating the effectiveness of our temporal partitioning strategy. We observe this trend consistently across all cutoff years and provide more visualisations in the Appendix.

![Refer to caption](2603.11838v1/x2.png)


Figure 2: Average relative perplexity of DatedGPT-base-2020 evaluated on quarterly public company news headlines from 2013 to 2024.

## 5 Web Interface design

We have developed a web interface for the DatedGPT model series that enables users to interact with and explore model outputs grounded in different time periods. The interface is built as a React-based single-page application, designed to make temporal language model exploration accessible to both researchers and general users.

The user interface presents a conversational chat view in which users can send natural language queries and receive responses from a selected DatedGPT model. A dropdown selector at the top of the interface allows users to switch between different temporally conditioned model versions (e.g., DatedGPT-2020), enabling users to observe how the knowledge of the model reflects the state of the world at that time. As an example, when asked “Do you know OpenAI?” followed by “What’s the name of the chatbot?”, DatedGPT-2020 responds with outdated information, illustrating how the model’s temporal grounding shapes its outputs. Users can also seamlessly switch between model versions to compare how responses to the same query differ across time.

## 6 Related Work

A growing body of work examines how temporal knowledge is encoded in large language models. Cheng et al. ([2024](#bib.bib9 "Dated data: tracing knowledge cutoffs in large language models")) show that the effective knowledge cutoff of a model often differs from its reported cutoff date, owing to the prevalence of older data in CommonCrawl dumps. Other efforts address the challenge of keeping LLM knowledge current through continual learning (Hu et al., [2023](#bib.bib38 "Meta-learning online adaptation of language models")) or dynamic evaluation benchmarks (Kasai et al., [2023](#bib.bib39 "Realtime qa: what’s the answer right now?")), though such approaches either risk catastrophic forgetting or do not guarantee strict temporal boundaries.

Lookahead bias is a particularly pressing concern in financial applications of LLMs, where models must not access information unavailable at the time of prediction. The use of LLMs in finance has expanded rapidly, spanning sentiment analysis, return prediction, economic forecasting, and earnings forecasting (Bybee, [2023](#bib.bib26 "The ghost in the machine: generating beliefs with large language models"); Lopez-Lira and Tang, [2023](#bib.bib24 "Can chatgpt forecast stock price movements? return predictability and large language models"); Hansen and Kazinnik, [2024](#bib.bib33 "Can chatgpt decipher fedspeak?"); Jha et al., [2024](#bib.bib25 "ChatGPT and corporate policies")), yet existing approaches cannot rule out information leakage at the parametric level. Researchers have proposed several prompting strategies to mitigate this issue, including masking firm identifiers, anonymizing contextual information, and limiting access to temporal cues (Glasserman and Lin, [2023](#bib.bib27 "Assessing look-ahead bias in stock return predictions generated by gpt sentiment analysis"); Sarkar, [2024](#bib.bib29 "StoriesLM: a family of language models with time-indexed training data"); Engelberg et al., [2025](#bib.bib30 "Entity neutering"); Wu et al., [2025](#bib.bib31 "Anonymization and information loss")), but the effectiveness of these strategies remains uncertain. Gao et al. ([2025](#bib.bib32 "A test of lookahead bias in llm forecasts")) develop an econometric test of the presence of lookahead bias that can be applied to various financial tasks. For widely used models the out-of-sample period is short, limiting the statistical power of tests for predictive ability. It is therefore important to rely on a family of models whose training data does not extend into the forecast period.

The most directly related line of work is time-aware cutoff pretraining. StoriesLM (Sarkar, [2024](#bib.bib29 "StoriesLM: a family of language models with time-indexed training data")) pioneers this direction by releasing a series of BERT-based 110M-parameter models with training cutoffs ranging from 1900 to 1963.
Concurrent with our work, He et al. ([2025](#bib.bib40 "Chronologically consistent large language models")) introduce ChronoGPT, a series of chronological GPT-2-scale models produced via continual pretraining with incremental yearly updates from 2000 to 2024. These models range from 124M to 1.5B parameters and are trained on approximately less than 10B tokens per year.
Our work complements this line of research by training each 1.3B-parameter model independently from scratch on approximately 100B tokens per year of temporally partitioned data, and additionally providing instruction-tuned variants with curated finance-domain data.

## 7 Conclusion

We presented DatedGPT, a family of 1.3B-parameter language models trained on temporally partitioned data with annual cutoffs from 2013 to 2024, eliminating lookahead bias in time-sensitive domains. Our evaluation confirms that each model’s knowledge aligns with its cutoff year while maintaining competitive benchmark performance.

## References

* L. B. Allal, A. Lozhkov, E. Bakouch, G. M. Blázquez, G. Penedo, L. Tunstall, A. Marafioti, H. Kydlíček, A. P. Lajarín, V. Srivastav, et al. (2025)
  SmolLM2: when smol goes big–data-centric training of a small language model.
  arXiv preprint arXiv:2502.02737.
  Cited by: [§4.1](#S4.SS1.SSS0.Px1.p1.1 "Baseline models ‣ 4.1 Evaluation setup ‣ 4 Experiment Results ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* S. Biderman, H. Schoelkopf, Q. G. Anthony, H. Bradley, K. O’Brien, E. Hallahan, M. A. Khan, S. Purohit, U. S. Prashanth, E. Raff, et al. (2023)
  Pythia: a suite for analyzing large language models across training and scaling.
  In International Conference on Machine Learning,
   pp. 2397–2430.
  Cited by: [§4.1](#S4.SS1.SSS0.Px1.p1.1 "Baseline models ‣ 4.1 Evaluation setup ‣ 4 Experiment Results ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* Y. Bisk, R. Zellers, J. Gao, Y. Choi, et al. (2020)
  Piqa: reasoning about physical commonsense in natural language.
  In Proceedings of the AAAI conference on artificial intelligence,
  Vol. 34,  pp. 7432–7439.
  Cited by: [§4.1](#S4.SS1.SSS0.Px3.p1.1 "Evaluation datasets ‣ 4.1 Evaluation setup ‣ 4 Experiment Results ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* F. Brahman, S. Kumar, V. Balachandran, P. Dasigi, V. Pyatkin, A. Ravichander, S. Wiegreffe, N. Dziri, K. Chandu, J. Hessel, et al. (2024)
  The art of saying no: contextual noncompliance in language models.
  Advances in Neural Information Processing Systems 37,  pp. 49706–49748.
  Cited by: [§2.2](#S2.SS2.SSS0.Px1.p4.1 "General-domain instruction dataset curation ‣ 2.2 Instruction-Following Data with Cutoff Dates ‣ 2 Time-Aware Dataset Curation ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* J. L. Bybee (2023)
  The ghost in the machine: generating beliefs with large language models.
  arXiv preprint arXiv:2305.02823.
  Cited by: [§2.2](#S2.SS2.SSS0.Px2.p1.1 "Time-sensitive instruction dataset curation ‣ 2.2 Instruction-Following Data with Cutoff Dates ‣ 2 Time-Aware Dataset Curation ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining"),
  [§6](#S6.p2.1 "6 Related Work ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* J. Cheng, M. Marone, O. Weller, D. Lawrie, D. Khashabi, and B. Van Durme (2024)
  Dated data: tracing knowledge cutoffs in large language models.
  First Conference on Language Modeling.
  Cited by: [§4.1](#S4.SS1.SSS0.Px3.p1.1 "Evaluation datasets ‣ 4.1 Evaluation setup ‣ 4 Experiment Results ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining"),
  [§4.3](#S4.SS3.p1.1 "4.3 Knowledge Memorisation Evaluation ‣ 4 Experiment Results ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining"),
  [§6](#S6.p1.1 "6 Related Work ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* A. Chowdhery, S. Narang, J. Devlin, M. Bosma, G. Mishra, A. Roberts, P. Barham, H. W. Chung, C. Sutton, S. Gehrmann, et al. (2023)
  Palm: scaling language modeling with pathways.
  Journal of machine learning research 24 (240),  pp. 1–113.
  Cited by: [§3.2](#S3.SS2.p1.1 "3.2 Pretraining Setup ‣ 3 Time-Aware Model Training ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* P. Clark, I. Cowhey, O. Etzioni, T. Khot, A. Sabharwal, C. Schoenick, and O. Tafjord (2018)
  Think you have solved question answering? try arc, the ai2 reasoning challenge.
  arXiv preprint arXiv:1803.05457.
  Cited by: [§4.1](#S4.SS1.SSS0.Px3.p1.1 "Evaluation datasets ‣ 4.1 Evaluation setup ‣ 4 Experiment Results ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* J. Engelberg, A. Manela, W. Mullins, and L. Vulicevic (2025)
  Entity neutering.
  Available at SSRN.
  Cited by: [§6](#S6.p2.1 "6 Related Work ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* Z. Gao, W. Jiang, and Y. Yan (2025)
  A test of lookahead bias in llm forecasts.
  arXiv preprint arXiv:2512.23847.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining"),
  [§4.3](#S4.SS3.p1.1 "4.3 Knowledge Memorisation Evaluation ‣ 4 Experiment Results ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining"),
  [§6](#S6.p2.1 "6 Related Work ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* P. Glasserman and C. Lin (2023)
  Assessing look-ahead bias in stock return predictions generated by gpt sentiment analysis.
  arXiv preprint arXiv:2309.17322.
  Cited by: [§6](#S6.p2.1 "6 Related Work ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* A. Gokaslan, V. Cohen, E. Pavlick, and S. Tellex (2019)
  OpenWebText corpus.
  External Links: [Link](http://Skylion007.github.io/OpenWebTextCorpus)
  Cited by: [footnote 2](#footnote2 "In 2.1 Pretraining Data with Cutoff Dates ‣ 2 Time-Aware Dataset Curation ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* A. L. Hansen and S. Kazinnik (2024)
  Can chatgpt decipher fedspeak?.
  Available at SSRN 4399406.
  Cited by: [§2.2](#S2.SS2.SSS0.Px2.p1.1 "Time-sensitive instruction dataset curation ‣ 2.2 Instruction-Following Data with Cutoff Dates ‣ 2 Time-Aware Dataset Curation ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining"),
  [§6](#S6.p2.1 "6 Related Work ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* S. He, L. Lv, A. Manela, and J. Wu (2025)
  Chronologically consistent large language models.
  arXiv preprint arXiv:2502.21206.
  Cited by: [§6](#S6.p3.1 "6 Related Work ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika, D. Song, and J. Steinhardt (2020)
  Measuring massive multitask language understanding.
  arXiv preprint arXiv:2009.03300.
  Cited by: [§4.1](#S4.SS1.SSS0.Px3.p1.1 "Evaluation datasets ‣ 4.1 Evaluation setup ‣ 4 Experiment Results ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* N. Hu, E. Mitchell, C. D. Manning, and C. Finn (2023)
  Meta-learning online adaptation of language models.
  In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing,
   pp. 4418–4432.
  Cited by: [§6](#S6.p1.1 "6 Related Work ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* M. Jha, J. Qian, M. Weber, and B. Yang (2024)
  ChatGPT and corporate policies.
  arXiv preprint arXiv:2409.17933.
  Cited by: [§2.2](#S2.SS2.SSS0.Px2.p1.1 "Time-sensitive instruction dataset curation ‣ 2.2 Instruction-Following Data with Cutoff Dates ‣ 2 Time-Aware Dataset Curation ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining"),
  [§6](#S6.p2.1 "6 Related Work ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* A. Karpathy (2024)
  Llm.c: llm training in simple, raw c/cuda
  External Links: [Link](https://github.com/karpathy/llm.c)
  Cited by: [§2.1](#S2.SS1.p1.1 "2.1 Pretraining Data with Cutoff Dates ‣ 2 Time-Aware Dataset Curation ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining"),
  [§3.1](#S3.SS1.p1.1 "3.1 Model architecture and hyperparameters ‣ 3 Time-Aware Model Training ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining"),
  [§3.2](#S3.SS2.p1.1 "3.2 Pretraining Setup ‣ 3 Time-Aware Model Training ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* J. Kasai, K. Sakaguchi, R. Le Bras, A. Asai, X. Yu, D. Radev, N. A. Smith, Y. Choi, K. Inui, et al. (2023)
  Realtime qa: what’s the answer right now?.
  Advances in neural information processing systems 36,  pp. 49025–49043.
  Cited by: [§6](#S6.p1.1 "6 Related Work ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* S. Lin, J. Hilton, and O. Evans (2022)
  Truthfulqa: measuring how models mimic human falsehoods.
  In Proceedings of the 60th annual meeting of the association for computational linguistics (volume 1: long papers),
   pp. 3214–3252.
  Cited by: [§4.1](#S4.SS1.SSS0.Px3.p1.1 "Evaluation datasets ‣ 4.1 Evaluation setup ‣ 4 Experiment Results ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* A. Lopez-Lira and Y. Tang (2023)
  Can chatgpt forecast stock price movements? return predictability and large language models.
  arXiv preprint arXiv:2304.07619.
  Cited by: [§2.2](#S2.SS2.SSS0.Px2.p1.1 "Time-sensitive instruction dataset curation ‣ 2.2 Instruction-Following Data with Cutoff Dates ‣ 2 Time-Aware Dataset Curation ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining"),
  [§6](#S6.p2.1 "6 Related Work ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* G. Penedo, H. Kydlíček, A. Lozhkov, M. Mitchell, C. A. Raffel, L. Von Werra, T. Wolf, et al. (2024)
  The fineweb datasets: decanting the web for the finest text data at scale.
  Advances in Neural Information Processing Systems 37,  pp. 30811–30849.
  Cited by: [§2.1](#S2.SS1.p1.1 "2.1 Pretraining Data with Cutoff Dates ‣ 2 Time-Aware Dataset Curation ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, I. Sutskever, et al. (2019)
  Language models are unsupervised multitask learners.
  OpenAI blog 1 (8),  pp. 9.
  Cited by: [§4.1](#S4.SS1.SSS0.Px1.p1.1 "Baseline models ‣ 4.1 Evaluation setup ‣ 4 Experiment Results ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* S. K. Sarkar and K. Vafa (2024)
  Lookahead bias in pretrained language models.
  Available at SSRN 4754678.
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* S. K. Sarkar (2024)
  StoriesLM: a family of language models with time-indexed training data.
  Available at SSRN 4881024.
  Cited by: [§6](#S6.p2.1 "6 Related Work ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining"),
  [§6](#S6.p3.1 "6 Related Work ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* R. Taori, I. Gulrajani, T. Zhang, Y. Dubois, X. Li, C. Guestrin, P. Liang, and T. B. Hashimoto (2023)
  Stanford alpaca: an instruction-following llama model.
   GitHub.
  Note: <https://github.com/tatsu-lab/stanford_alpaca>
  Cited by: [§2.2](#S2.SS2.SSS0.Px1.p1.1 "General-domain instruction dataset curation ‣ 2.2 Instruction-Following Data with Cutoff Dates ‣ 2 Time-Aware Dataset Curation ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* H. Touvron, T. Lavril, G. Izacard, X. Martinet, M. Lachaux, T. Lacroix, B. Rozière, N. Goyal, E. Hambro, F. Azhar, et al. (2023)
  Llama: open and efficient foundation language models.
  arXiv preprint arXiv:2302.13971.
  Cited by: [§2.1](#S2.SS1.p1.1 "2.1 Pretraining Data with Cutoff Dates ‣ 2 Time-Aware Dataset Curation ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* Y. Wang, Y. Kordi, S. Mishra, A. Liu, N. A. Smith, D. Khashabi, and H. Hajishirzi (2023)
  Self-instruct: aligning language models with self-generated instructions.
  In Proceedings of the 61st annual meeting of the association for computational linguistics (volume 1: long papers),
   pp. 13484–13508.
  Cited by: [§2.2](#S2.SS2.SSS0.Px1.p1.1 "General-domain instruction dataset curation ‣ 2.2 Instruction-Following Data with Cutoff Dates ‣ 2 Time-Aware Dataset Curation ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* M. Weber, D. Fu, Q. Anthony, Y. Oren, S. Adams, A. Alexandrov, X. Lyu, H. Nguyen, X. Yao, V. Adams, et al. (2024)
  Redpajama: an open dataset for training large language models.
  Advances in neural information processing systems 37,  pp. 116462–116492.
  Cited by: [§2.1](#S2.SS1.p1.1 "2.1 Pretraining Data with Cutoff Dates ‣ 2 Time-Aware Dataset Curation ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* [30]
  J. Wei, M. Bosma, V. Zhao, K. Guu, A. W. Yu, B. Lester, N. Du, A. M. Dai, and Q. V. Le
  Finetuned language models are zero-shot learners.
  In International Conference on Learning Representations,
  Cited by: [§2.2](#S2.SS2.SSS0.Px1.p1.1 "General-domain instruction dataset curation ‣ 2.2 Instruction-Following Data with Cutoff Dates ‣ 2 Time-Aware Dataset Curation ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* K. Wu, B. Yang, Z. Ying, and D. Zhou (2025)
  Anonymization and information loss.
  arXiv preprint arXiv:2511.15364.
  Cited by: [§6](#S6.p2.1 "6 Related Work ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* [32]
  C. Xu, Q. Sun, K. Zheng, X. Geng, P. Zhao, J. Feng, C. Tao, Q. Lin, and D. Jiang
  WizardLM: empowering large pre-trained language models to follow complex instructions.
  In The Twelfth International Conference on Learning Representations,
  Cited by: [§2.2](#S2.SS2.SSS0.Px1.p1.1 "General-domain instruction dataset curation ‣ 2.2 Instruction-Following Data with Cutoff Dates ‣ 2 Time-Aware Dataset Curation ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* R. Zellers, A. Holtzman, Y. Bisk, A. Farhadi, and Y. Choi (2019)
  Hellaswag: can a machine really finish your sentence?.
  In Proceedings of the 57th annual meeting of the association for computational linguistics,
   pp. 4791–4800.
  Cited by: [§4.1](#S4.SS1.SSS0.Px3.p1.1 "Evaluation datasets ‣ 4.1 Evaluation setup ‣ 4 Experiment Results ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* A. Zeng, X. Liu, Z. Du, Z. Wang, H. Lai, M. Ding, Z. Yang, Y. Xu, W. Zheng, X. Xia, et al. (2022)
  Glm-130b: an open bilingual pre-trained model.
  arXiv preprint arXiv:2210.02414.
  Cited by: [§3.2](#S3.SS2.p1.1 "3.2 Pretraining Setup ‣ 3 Time-Aware Model Training ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* P. Zhang, G. Zeng, T. Wang, and W. Lu (2024)
  TinyLlama: an open-source small language model.
  External Links: 2401.02385
  Cited by: [§4.1](#S4.SS1.SSS0.Px1.p1.1 "Baseline models ‣ 4.1 Evaluation setup ‣ 4 Experiment Results ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* S. Zhang, S. Roller, N. Goyal, M. Artetxe, M. Chen, S. Chen, C. Dewan, M. Diab, X. Li, X. V. Lin, et al. (2022)
  Opt: open pre-trained transformer language models.
  arXiv preprint arXiv:2205.01068.
  Cited by: [§3.2](#S3.SS2.p1.1 "3.2 Pretraining Setup ‣ 3 Time-Aware Model Training ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining"),
  [§4.1](#S4.SS1.SSS0.Px1.p1.1 "Baseline models ‣ 4.1 Evaluation setup ‣ 4 Experiment Results ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* L. Zheng, W. Chiang, Y. Sheng, S. Zhuang, Z. Wu, Y. Zhuang, Z. Lin, Z. Li, D. Li, E. Xing, et al. (2023)
  Judging llm-as-a-judge with mt-bench and chatbot arena.
  Advances in neural information processing systems 36,  pp. 46595–46623.
  Cited by: [§2.2](#S2.SS2.SSS0.Px1.p1.1 "General-domain instruction dataset curation ‣ 2.2 Instruction-Following Data with Cutoff Dates ‣ 2 Time-Aware Dataset Curation ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").
* J. Zhou, T. Lu, S. Mishra, S. Brahma, S. Basu, Y. Luan, D. Zhou, and L. Hou (2023)
  Instruction-following evaluation for large language models.
  External Links: 2311.07911,
  [Link](https://arxiv.org/abs/2311.07911)
  Cited by: [§4.1](#S4.SS1.SSS0.Px3.p1.1 "Evaluation datasets ‣ 4.1 Evaluation setup ‣ 4 Experiment Results ‣ DatedGPT: Preventing Lookahead Bias in Large Language Models with Time-Aware Pretraining").

## Appendix A Dataset Details

| Dataset | Description |
| --- | --- |
| [OpenHermes-2.5](https://huggingface.co/datasets/teknium/OpenHermes-2.5) | General instruction following curated from diverse LLM outputs, covering a wide range of topics and tasks. |
| [ShareGPT](https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered) | A subset within OpenHermes, consisting of real user-machine interactions collected from users sharing their conversations with ChatGPT. |
| [Tulu-3](https://huggingface.co/datasets/allenai/tulu-3-sft-personas-instruction-following) | Persona-based instruction following with diverse user personas and instruction-following requirements. |
| [Coconot](https://huggingface.co/datasets/allenai/coconot) | Safety behaviour and format following, designed to improve model compliance with contextual and formatting constraints. |

Table 3: Overview of selected general instruction-following datasets.

## Appendix B Model Training Details

| Hyperparameter | Value |
| --- | --- |
| Sequence Length | 2048 |
| Number of Layers | 24 |
| Embedding Size | 2048 |
| FFN Hidden Size | 5504 |
| Number of Heads | 16 |
| Position Encodings | RoPE |
| Activation Function | SwiGLU |
| Layer Norm | RMSNorm |
| Learning Rate | 2E-4 |
| Batch Size | 2048 |
| Vocabulary Size | 32000 |
| Embedding Parameters | 0.13B |
| Non-Embedding Parameters | 1.21B |
| Total Parameters | 1.34B |

Table 4: Model and pretraining hyperparameters.

![Refer to caption](2603.11838v1/x3.png)


Figure 3: Training loss curves for 2013 and 2024 DatedGPT-base models. All models exhibit smooth convergence without loss spikes or instability.

![Refer to caption](2603.11838v1/x4.png)


Figure 4: Relative perplexity of DatedGPT-base-2017 evaluated on quarterly public company news head-lines from 2013 to 2024.

## Appendix C Evaluation Result on Full Series of DatedGPT

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Model (0-shot) | ARC-C | ARC-E | HellaSwag | PIQA | IFEval | MMLU | TruthfulQA |
| Baseline Models | | | | | | | |
| SmolLM-1.7B-Instruct | 34.9 | 54.3 | 56.1 | 72.4 | 15.5 | 27.1 | 27.7 |
| GPT2-XL | 28.4 | 51.0 | 50.8 | 70.5 | 15.0 | 25.3 | 22.4 |
| TinyLlama-1.1B | 30.5 | 43.7 | 55.0 | 72.5 | 14.8 | 24.8 | 26.0 |
| OPT-1.3B | 27.8 | 51.3 | 53.7 | 70.9 | 17.6 | 25.2 | 23.8 |
| Pythia-1B | 27.1 | 49.0 | 47.1 | 69.3 | 16.8 | 23.1 | 23.6 |
| DatedGPT-Instruct Series | | | | | | | |
| DatedGPT-Instruct-2013 | 33.6 | 48.8 | 47.6 | 66.4 | 34.2 | 25.3 | 25.1 |
| DatedGPT-Instruct-2014 | 32.6 | 47.3 | 47.8 | 69.2 | 34.4 | 24.8 | 24.7 |
| DatedGPT-Instruct-2015 | 32.3 | 48.0 | 48.0 | 67.1 | 34.8 | 24.1 | 26.6 |
| DatedGPT-Instruct-2016 | 32.9 | 50.6 | 48.4 | 69.4 | 32.5 | 24.8 | 26.6 |
| DatedGPT-Instruct-2017 | 34.8 | 50.5 | 50.0 | 69.0 | 34.0 | 24.8 | 26.8 |
| DatedGPT-Instruct-2018 | 35.2 | 50.0 | 50.5 | 68.9 | 30.7 | 25.3 | 27.2 |
| DatedGPT-Instruct-2019 | 31.1 | 49.8 | 50.6 | 69.5 | 34.0 | 24.9 | 25.3 |
| DatedGPT-Instruct-2020 | 33.1 | 48.5 | 51.1 | 68.9 | 32.5 | 25.7 | 25.1 |
| DatedGPT-Instruct-2021 | 32.9 | 48.5 | 51.0 | 68.9 | 31.8 | 24.4 | 26.4 |
| DatedGPT-Instruct-2022 | 33.6 | 49.9 | 51.4 | 69.2 | 35.9 | 23.5 | 26.9 |
| DatedGPT-Instruct-2023 | 32.3 | 51.1 | 52.7 | 69.7 | 33.8 | 23.7 | 30.8 |
| DatedGPT-Instruct-2024 | 34.7 | 52.0 | 53.2 | 70.5 | 35.3 | 24.3 | 28.6 |

Table 5: Zero-shot evaluation results on language understanding benchmarks. IFEval reports prompt-level strict accuracy. The DatedGPT-Instruct series models are identified by their training data cutoff year.



|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Model (5-shot) | ARC-C | ARC-E | HellaSwag | PIQA | IFEval | MMLU | TruthfulQA |
| Baseline Models | | | | | | | |
| SmolLM-1.7B-Instruct | 43.9 | 74.0 | 62.4 | 74.1 | 4.6 | 28.3 | 25.3 |
| GPT2-XL | 29.9 | 59.4 | 51.2 | 70.6 | 15.0 | 26.3 | 22.0 |
| TinyLlama-1.1B | 35.5 | 66.4 | 60.8 | 74.8 | 3.1 | 25.0 | 23.6 |
| OPT-1.3B | 29.2 | 59.6 | 54.1 | 71.0 | 17.4 | 24.8 | 24.0 |
| Pythia-1B | 28.2 | 56.9 | 47.5 | 70.1 | 17.4 | 25.8 | 23.6 |
| DatedGPT-Base Series | | | | | | | |
| DatedGPT-Base-2013 | 34.6 | 67.2 | 48.8 | 69.8 | 17.6 | 25.1 | 21.9 |
| DatedGPT-Base-2014 | 37.0 | 67.0 | 48.8 | 69.7 | 17.0 | 25.5 | 22.0 |
| DatedGPT-Base-2015 | 36.0 | 68.2 | 49.0 | 70.2 | 14.4 | 24.7 | 21.1 |
| DatedGPT-Base-2016 | 37.8 | 67.9 | 49.3 | 69.2 | 12.6 | 25.5 | 20.7 |
| DatedGPT-Base-2017 | 39.3 | 69.3 | 51.3 | 71.1 | 19.8 | 25.3 | 21.9 |
| DatedGPT-Base-2018 | 38.3 | 68.7 | 51.8 | 71.0 | 15.7 | 25.3 | 20.9 |
| DatedGPT-Base-2019 | 35.0 | 67.7 | 51.6 | 71.7 | 14.6 | 24.2 | 20.0 |
| DatedGPT-Base-2020 | 37.8 | 68.5 | 52.6 | 71.0 | 10.9 | 26.3 | 20.6 |
| DatedGPT-Base-2021 | 38.4 | 68.6 | 52.3 | 70.5 | 12.8 | 25.8 | 22.9 |
| DatedGPT-Base-2022 | 36.8 | 68.7 | 52.7 | 71.7 | 15.7 | 25.2 | 21.4 |
| DatedGPT-Base-2023 | 39.8 | 70.0 | 53.6 | 71.8 | 13.9 | 23.7 | 23.9 |
| DatedGPT-Base-2024 | 40.2 | 71.6 | 54.6 | 71.3 | 12.8 | 25.8 | 24.4 |

Table 6: Five-shot evaluation results on language understanding benchmarks. IFEval reports prompt-level strict accuracy. The DatedGPT-Base series models are identified by their training data cutoff year.

BETA