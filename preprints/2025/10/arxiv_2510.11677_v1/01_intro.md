---
authors:
- Songrun He
- Linying Lv
- Asaf Manela
- Jimmy Wu
doc_id: arxiv:2510.11677v1
family_id: arxiv:2510.11677
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Chronologically Consistent Generative AI Songrun He is at Washington University
  in St. Louis (h.songrun@wustl.edu). Linying Lv is at Washington University in St.
  Louis (llyu@wustl.edu). Asaf Manela is at Washington University in St. Louis (amanela@wustl.edu).
  Jimmy Wu is at Washington University in St. Louis (jimmywu@wustl.edu).
url_abs: http://arxiv.org/abs/2510.11677v1
url_html: https://arxiv.org/html/2510.11677v1
venue: arXiv q-fin
version: 1
year: 2025
---


Songrun He   Linying Lv   Asaf Manela   Jimmy Wu

(First draft: July 2025. This draft: October 2025.)

We introduce a family of chronologically consistent, instruction-following large language models to eliminate lookahead bias. Each model is trained only on data available before a clearly defined knowledge-cutoff date, ensuring strict temporal separation from any post-cutoff data. The resulting framework offers (i) a simple, conversational chat interface, (ii) fully open, fixed model weights that guarantee replicability, and (iii) a conservative lower bound on forecast accuracy, isolating the share of predictability that survives once training leakage is removed. Together, these features provide researchers with an easy-to-use generative AI tool useful for a wide range of prediction tasks that is free of lookahead bias.

JEL Classification: G11, G12, G17
  
Keywords: Instruction following model, chronological consistency, lookahead bias, training leakage

## 1 Introduction

Large language models (LLMs) have emerged as a transformative force in financial econometrics. Recent research extensively leverages LLM outputs for prediction and estimation tasks (see, for example: Lopez-Lira and Tang, [2023](https://arxiv.org/html/2510.11677v1#bib.bib9); Chang et al., [2023](https://arxiv.org/html/2510.11677v1#bib.bib1); Jha et al., [2024](https://arxiv.org/html/2510.11677v1#bib.bib7); Chen et al., [2025](https://arxiv.org/html/2510.11677v1#bib.bib2); Lv, [2025](https://arxiv.org/html/2510.11677v1#bib.bib11)). The novel capabilities and inherent intelligence of LLMs have enabled exploration of unstructured data and addressing previously unanswered questions.

However, as noted by Sarkar and Vafa ([2024](https://arxiv.org/html/2510.11677v1#bib.bib14)) and Ludwig et al. ([2025](https://arxiv.org/html/2510.11677v1#bib.bib10)), most prediction problems with generative AI face methodological challenges of lookahead bias. The reason is that LLMs are pretrained on a vast corpus of text data that incorporates future information relative to the prediction task. This leads to lookahead bias when the model’s knowledge cutoff τ\tau extends beyond the prediction time, as a training leakage term then emerges in the loss function.

Several papers have introduced robust methods for isolating temporal information. For example, Glasserman and Lin ([2023](https://arxiv.org/html/2510.11677v1#bib.bib5)) and Engelberg et al. ([2025](https://arxiv.org/html/2510.11677v1#bib.bib4)) develop a systematic entity masking approach so that LLMs cannot recognize firms. Alternatively, researchers have explored pretraining LLMs from scratch, meticulously curating the training data to control the models’ inherent knowledge (e.g., Sarkar, [2024](https://arxiv.org/html/2510.11677v1#bib.bib13); He et al., [2025](https://arxiv.org/html/2510.11677v1#bib.bib6)).

While pretraining an LLM from scratch appears to be a more comprehensive solution for preventing the model from accessing future knowledge, as opposed to methods that attempt to make it forget learned information or infer from context, its implementation presents two primary challenges. First, ensuring chronological consistency requires excluding a substantial amount of future training text, which may compromise the model’s performance. Second, integrating this approach, especially within a model embedding and machine learning pipeline, is both technically sophisticated and computationally expensive.

In this paper, we offer another solution more accessible to the social science research community: the first instruction-following chat model free of lookahead bias. Specifically, during both the pretraining and instruction finetuning stages, we carefully curate the dataset to prevent the model from seeing future knowledge. For example, ChronoGPT-Instructτ\text{ChronoGPT-Instruct}\_{\tau} (where τ\tau is in {1999,2000,2001,…,2024}\{1999,2000,2001,...,2024\} ) never accesses any knowledge that emerged or became economically salient after τ\tau. For any evaluation set post-τ\tau, the model has perfect temporal separation from the evaluation set.

Despite the significant effort in developing the ChronoGPT-Instruct series, certain challenges in its design and implementation are important to highlight. A fundamental tradeoff exists between maintaining robust chat capabilities and ensuring strict chronological consistency. To illustrate, a Qwen-1.5-1.8B-Chat model of similar parameter size is pretrained on 2.2 trillion tokens, approximately 31 times the 70 billion tokens seen by our base model. Nevertheless, even the earliest ChronoGPT-Instruct models achieve above 12% win rates in the Alpaca instruction-following evaluation, demonstrating their practical utility despite data constraints. Additionally, while our prompt-based filtering algorithm is designed to be highly effective, we acknowledge it is not theoretically flawless. However, in a rigorous validation test we conduct, ChronoGPT-Instruct models consistently fail to predict future presidents or major events, showing no signs of training leakage.

The primary contribution of our model is to serve as a useful tool for conducting lookahead bias-free robustness tests in various prediction problems. We publicly release our ChronoGPT-instruct models and instruction-finetuning data to support the research community at: <https://huggingface.co/manelalab>. While ChronoGPT-Instruct does not offer a perfect solution that simultaneously eliminates training leakage and preserves state-of-the-art language abilities, it allows for establishing a conservative lower bound of predictive power, providing a clearer understanding of true model performance. In a prompt-based trading portfolio example we provide, if ChronoGPT-Instruct is considered a lookahead bias-free counterpart to larger models such as Qwen-1.5-1.8B-Chat and Llama-3.2-3B-Instruct (up to twice the parameter count and trained on far more data), our finding implies that at least 54% of the observed news return predictability persists without leakage. The remaining discrepancy in Sharpe ratios (e.g., between 0.95 and 1.76) likely stems from a combination of differences in model capabilities and lookahead bias in the comparison model.

## 2 Methodology and Data

In this section, we describe our instruction finetuning methodology designed to enforce no training leakage, followed by details of our data curation process and the datasets used for both instruction finetuning and return prediction tasks.

### 2.1 Instruction Finetuning

Our instruction finetuning pipeline is designed to satisfy the *no-training-leakage* contract of Ludwig et al. ([2025](https://arxiv.org/html/2510.11677v1#bib.bib10)). The contract formalizes the idea that any text used for evaluating a model must be statistically independent of the text used to train it. We first restate the contract in a two-stage setting of pretraining and instruction finetuning (IFT), and then show how our data curation enforces each of its requirements.

Two disjoint training corpora. Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | tpre​(τ)={σ∈Σ∗:date⁡(σ)≤τ},tift​(τ)={σ∈Σinst ∗:date⁡(σ)≤τ},t^{\mathrm{pre}}(\tau)=\left\{\sigma\in\Sigma^{\*}:\operatorname{date}(\sigma)\leq\tau\right\},\quad t^{\mathrm{ift}}(\tau)=\left\{\sigma\in\Sigma\_{\text{inst }}^{\*}:\operatorname{date}(\sigma)\leq\tau\right\}, |  | (1) |

where τ\tau is the knowledge cutoff of our vintage models. For any text piece rr define stage-specific indicators

|  |  |  |  |
| --- | --- | --- | --- |
|  | trpre=𝟏​(r∈tpre​(τ)),trift=𝟏​(r∈tift​(τ))t\_{r}^{\mathrm{pre}}=\mathbf{1}\big(r\in t^{\mathrm{pre}}(\tau)\big),\quad t\_{r}^{\mathrm{ift}}=\mathbf{1}\big(r\in t^{\mathrm{ift}}(\tau)\big) |  | (2) |

and let

|  |  |  |  |
| --- | --- | --- | --- |
|  | tr=max⁡{trpre,trift}∈{0,1}t\_{r}=\max\left\{t\_{r}^{\mathrm{pre}},t\_{r}^{\mathrm{ift}}\right\}\in\{0,1\} |  | (3) |

denote membership in the combined training set.

Loss decomposition with a leakage term. Consider an evaluation sample R>τR\_{>\tau} consisting exclusively of documents dated after τ\tau and let Dr=𝟏​(r∈R>τ)D\_{r}=\mathbf{1}\left(r\in R\_{>\tau}\right). With loss function ℓ​(⋅,⋅)\ell(\cdot,\cdot) and model prediction m^​(r;t)\hat{m}(r;t), the expectation of L^τ\hat{L}\_{\tau} can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​[L^τ]=E​[ℓ​(Yr,m^​(r;t))]⏟true out-of-sample loss −E​[Dr​(qT∣D​(tr)qT​(tr)−1)​ℓ​(Yr,m^​(r;t))]⏟leakage term ,E\left[\hat{L}\_{\tau}\right]=\underbrace{E\left[\ell\left(Y\_{r},\hat{m}(r;t)\right)\right]}\_{\text{true out-of-sample loss }}-\underbrace{E\left[D\_{r}\left(\frac{q\_{T\mid D}\left(t\_{r}\right)}{q\_{T}\left(t\_{r}\right)}-1\right)\ell\left(Y\_{r},\hat{m}(r;t)\right)\right]}\_{\text{leakage term }}, |  | (4) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | qT​(tr)=Pr⁡(tr=1),qT∣D​(tr)=Pr⁡(tr=1∣Dr=1)q\_{T}\left(t\_{r}\right)=\operatorname{Pr}\left(t\_{r}=1\right),\quad q\_{T\mid D}\left(t\_{r}\right)=\operatorname{Pr}\left(t\_{r}=1\mid D\_{r}=1\right) |  | (5) |

are the *unconditional* and *conditional* probabilities that rr appears in the training set, respectively. The second expectation in ([4](https://arxiv.org/html/2510.11677v1#S2.E4 "In 2.1 Instruction Finetuning ‣ 2 Methodology and Data ‣ Chronologically Consistent Generative AI Songrun He is at Washington University in St. Louis (h.songrun@wustl.edu). Linying Lv is at Washington University in St. Louis (llyu@wustl.edu). Asaf Manela is at Washington University in St. Louis (amanela@wustl.edu). Jimmy Wu is at Washington University in St. Louis (jimmywu@wustl.edu).")) is the leakage term; it vanishes if and only if

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀r:qT∣D​(tr)qT​(tr)=1,\forall r:\frac{q\_{T\mid D}\left(t\_{r}\right)}{q\_{T}\left(t\_{r}\right)}=1, |  | (6) |

which is the contract’s independence condition.

Stage-wise sufficiency. Because the overall indicator trt\_{r} in ([3](https://arxiv.org/html/2510.11677v1#S2.E3 "In 2.1 Instruction Finetuning ‣ 2 Methodology and Data ‣ Chronologically Consistent Generative AI Songrun He is at Washington University in St. Louis (h.songrun@wustl.edu). Linying Lv is at Washington University in St. Louis (llyu@wustl.edu). Asaf Manela is at Washington University in St. Louis (amanela@wustl.edu). Jimmy Wu is at Washington University in St. Louis (jimmywu@wustl.edu).")) is the union of two disjoint events, independence is guaranteed once it holds separately for pretraining and IFT:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀r:qT∣D​(trpre)qT​(trpre)=1 and qT∣D​(trift)qT​(trift)=1.\forall r:\frac{q\_{T\mid D}\left(t\_{r}^{\mathrm{pre}}\right)}{q\_{T}\left(t\_{r}^{\mathrm{pre}}\right)}=1\quad\text{ and }\quad\frac{q\_{T\mid D}\left(t\_{r}^{\mathrm{ift}}\right)}{q\_{T}\left(t\_{r}^{\mathrm{ift}}\right)}=1. |  | (7) |

For the pretraining stage, we use the vintage ChronoGPT in He et al. ([2025](https://arxiv.org/html/2510.11677v1#bib.bib6)) as our base model. The corpus Tτpre T\_{\tau}^{\text{pre }} is built from historical web snapshots, archived news, and scientific literature. Every document carries a verifiable publication timestamp, and any text dated after τ\tau is discarded. Hence for each post-knowledge cutoff evaluation item rr we have trpre =0t\_{r}^{\text{pre }}=0, leading to

|  |  |  |  |
| --- | --- | --- | --- |
|  | qT​(trpre)=0,qT∣D​(trpre)=0,q\_{T}\left(t\_{r}^{\mathrm{pre}}\right)=0,\quad q\_{T\mid D}\left(t\_{r}^{\mathrm{pre}}\right)=0, |  | (8) |

so the first equality in ([7](https://arxiv.org/html/2510.11677v1#S2.E7 "In 2.1 Instruction Finetuning ‣ 2 Methodology and Data ‣ Chronologically Consistent Generative AI Songrun He is at Washington University in St. Louis (h.songrun@wustl.edu). Linying Lv is at Washington University in St. Louis (llyu@wustl.edu). Asaf Manela is at Washington University in St. Louis (amanela@wustl.edu). Jimmy Wu is at Washington University in St. Louis (jimmywu@wustl.edu).")) holds.

|  |
| --- |
| Prompt: You are provided with a user-assistant interaction. Your task is to determine whether the conversation contains any information that would have been unavailable or irrelevant prior to the year 2000. |
| Specifically, indicate whether the message includes any direct or indirect reference to: |
| 1. A concept, company, product, technology, event, online review, or terminology that was created, discovered, or publicly introduced after 1999, or |
| 2. A subject that only gained significant economic, cultural, scientific, or technological relevance after 1999, even if it existed before that date. |
| If such a reference is present anywhere in the conversation, return: 1 |
| If the conversation is entirely composed of content that could have been generated using only knowledge available prior to 2000, return: 0 |
| Clarifications: |
| - For conversations evaluated as low quality, also assign a label of 1. |
| - In cases of uncertainty or ambiguity, adopt a conservative approach and assign a label of 1. |
| - References to post-1999 entities such as GPT models, Kubernetes, TikTok, blockchain, COVID-19, Tesla, or similar modern constructs are strong indicators of a label of 1. |
| Return your answer strictly as a JSON object with the following fields: |
| - ”label”: either 0 or 1 |
| - ”confidence”: a number from 0 to 10 (higher means more certain) |
| - ”suspected term”: a brief phrase (1-3 words) that triggered your label decision, or ”none” if label=0 |
| Example output: {”label”: 1, ”confidence”: 9, ”suspected term”: ”GPT-3”} |
| Here is the message:{conversation} |

We conduct a prompt filtering algorithm for the instruction-finetuning stage. Candidate instruction-response pairs are screened with an LLM classifier. The classifier, implemented with ChatGPT-4.1, receives the following prompt and returns a binary label indicating whether the dialogue contains any knowledge that emerged or became economically salient after τ\tau.

Only pairs receiving the label 0 are admitted to tift​(τ)t^{\text{ift}}(\tau). Consequently, for every evaluation item rr dated after the cut-off, trift=0t\_{r}^{\mathrm{ift}}=0 and the second equality in ([7](https://arxiv.org/html/2510.11677v1#S2.E7 "In 2.1 Instruction Finetuning ‣ 2 Methodology and Data ‣ Chronologically Consistent Generative AI Songrun He is at Washington University in St. Louis (h.songrun@wustl.edu). Linying Lv is at Washington University in St. Louis (llyu@wustl.edu). Asaf Manela is at Washington University in St. Louis (amanela@wustl.edu). Jimmy Wu is at Washington University in St. Louis (jimmywu@wustl.edu).")) also holds. We conduct a validation test for the independence condition in section [3.2](https://arxiv.org/html/2510.11677v1#S3.SS2 "3.2 Chronological Consistency Validation ‣ 3 Results ‣ Chronologically Consistent Generative AI Songrun He is at Washington University in St. Louis (h.songrun@wustl.edu). Linying Lv is at Washington University in St. Louis (llyu@wustl.edu). Asaf Manela is at Washington University in St. Louis (amanela@wustl.edu). Jimmy Wu is at Washington University in St. Louis (jimmywu@wustl.edu).").

### 2.2 Data

This section introduces the public user-assistant interaction dataset we use for instruction finetuning, and the financial newswire data we use for return prediction.

#### 2.2.1 Instruction Finetuning Data

The instruction-finetuning corpus comprises over 425,000 prompt–response pairs drawn from three public resources and arranged as a curriculum that grows in cognitive load and sequence length. We start with simple, short tasks from Raschka ([2024](https://arxiv.org/html/2510.11677v1#bib.bib12)), like spelling checks or basic math. Then, we add medium-length prompts from the Wang et al. ([2022](https://arxiv.org/html/2510.11677v1#bib.bib15)) dataset generated from the GPT-3 through the self-instruct technique. Finally, we include the broad AllenAI’s Tulu-3 SFT mixture created by Lambert et al. ([2024](https://arxiv.org/html/2510.11677v1#bib.bib8)).

All entries are filtered to (i) exclude non-English records and code snippets, and (ii) satisfy a temporal-knowledge screen: each example is classified by GPT-4.1 and only retained when the model assigns label 0 (“knowledge available pre-2000”) with the maximum confidence score of 10. Table [1](https://arxiv.org/html/2510.11677v1#S2.T1 "Table 1 ‣ 2.2.1 Instruction Finetuning Data ‣ 2.2 Data ‣ 2 Methodology and Data ‣ Chronologically Consistent Generative AI Songrun He is at Washington University in St. Louis (h.songrun@wustl.edu). Linying Lv is at Washington University in St. Louis (llyu@wustl.edu). Asaf Manela is at Washington University in St. Louis (amanela@wustl.edu). Jimmy Wu is at Washington University in St. Louis (jimmywu@wustl.edu).") summarizes the resulting dataset.

| Stage | SFT data | Number of examples | Average conversation length |
| --- | --- | --- | --- |
| 1 | LLMs-from-scratch | 1,097 | 102 |
| 2 | GPT-3 self-generated | 67,136 | 183 |
| 3 | Tulu-3 SFT mixture | 356,886 | 2,513 |

Table 1: Instruction Finetuning Datasets

We then format these entries as inputs to ChronoGPT using Alpaca-style prompt formatting. Below is an example entry passed to the LLM:

```
{
  Below is an instruction that describes a task. Write a response that
  appropriately completes the request.
    ### Instruction:
    Identify the correct spelling of the following word.
    ### Input:
    Ocassion
    ### Response:
    The correct spelling is ’Occasion.’
}
```

#### 2.2.2 Financial Newswire Data

We use the Dow Jones Newswire dataset, a real-time newswire providing extensive coverage of financial markets from January 2007 to July 2023. This dataset includes news headlines, full article texts, and precise display timestamps. Following He et al. ([2025](https://arxiv.org/html/2510.11677v1#bib.bib6)), we focus on firm-specific news, aggregating all relevant headlines for each firm within a trading day. Finally, we merge this news data with CRSP close-to-close returns on day t+1 to examine the predictability of stock returns.

## 3 Results

### 3.1 Instruction Following Evaluation

We instruction-finetune a series of models as ChronoGPT-Instruct-1999, ChronoGPT-Instruct-2005, ChronoGPT-Instruct-2010, ChronoGPT-Instruct-2015, ChronoGPT-Instruct-2020, and ChronoGPT-Instruct-2024, each starting from the corresponding ChronoGPT vintage model in He et al. ([2025](https://arxiv.org/html/2510.11677v1#bib.bib6)). All vintages are finetuned with the standard masked cross-entropy for next-token prediction, formally defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ=−1N​∑t=1Nlog⁡pθ​(yt∣𝐱<t),\mathcal{L}=-\frac{1}{N}\sum\_{t=1}^{N}\log p\_{\theta}\left(y\_{t}\mid\mathbf{x}\_{<t}\right), |  | (9) |

where the model parameters θ\theta are optimized to maximize the probability pθ​(yt∣𝐱<t)p\_{\theta}\left(y\_{t}\mid\mathbf{x}\_{<t}\right) of generating the true token yty\_{t} at position tt within a sequence of length NN. This objective rewards the model for accurately predicting the subsequent token in a response.

Every SFT stage logs the token-level cross-entropy on a 5% hold-out split that is never seen by the optimizer. Figure [1](https://arxiv.org/html/2510.11677v1#S3.F1 "Figure 1 ‣ 3.1 Instruction Following Evaluation ‣ 3 Results ‣ Chronologically Consistent Generative AI Songrun He is at Washington University in St. Louis (h.songrun@wustl.edu). Linying Lv is at Washington University in St. Louis (llyu@wustl.edu). Asaf Manela is at Washington University in St. Louis (amanela@wustl.edu). Jimmy Wu is at Washington University in St. Louis (jimmywu@wustl.edu).") plots these losses across three stages of training, showing the characteristic rapid decline in early steps followed by more gradual improvement. The steep initial drop reflects rapid adaptation to the instruction-following format, while later stages show continued learning from the curriculum order.

![Refer to caption](Figures/training_plot.png)

Figure 1: Training Loss and Validation Loss of Instruction Finetuning

The figure shows the training dynamics across three stages of supervised finetuning (SFT) on the ChronoGPT-1999 model. Stage 1 uses LLMs-from-scratch data. Stage 2 uses GPT-3 self-generated data. Stage 3 uses Tulu-3-SFT mixture.

Figure [2](https://arxiv.org/html/2510.11677v1#S3.F2 "Figure 2 ‣ 3.1 Instruction Following Evaluation ‣ 3 Results ‣ Chronologically Consistent Generative AI Songrun He is at Washington University in St. Louis (h.songrun@wustl.edu). Linying Lv is at Washington University in St. Louis (llyu@wustl.edu). Asaf Manela is at Washington University in St. Louis (amanela@wustl.edu). Jimmy Wu is at Washington University in St. Louis (jimmywu@wustl.edu).") compares the validation losses across all five vintages for each training stage. Consistent with the language-model results in He et al. ([2025](https://arxiv.org/html/2510.11677v1#bib.bib6)), we observe systematic improvements from earlier to later vintages, with the 1999 model showing the highest validation loss and more recent vintages achieving lower losses across all three stages.

![Refer to caption](Figures/validation_comparison.png)

Figure 2: Validation Loss of Instruction Model Vintages

The figure compares the validation loss across six vintage models (1999, 2005, 2010, 2015, 2020, 2025) for the three curriculum stages: Stage 1 (LLMs-from-scratch, simple tasks), Stage 2 (GPT-3 self-generated, medium complexity), and Stage 3 (Tulu-3 mixture, complex conversations).



![Refer to caption](Figures/alpaca.png)

Figure 3: Alpaca Evaluation for ChronoGPT-Instruct

This figure shows head-to-head win rates using length-controlled evaluation across model vintages from 1999 to 2024. The evaluation set is from AlpacaFarm. The benchmark model is Qwen-1.5-1.8B-Chat.

While validation loss is a useful proxy, it conflates syntax prediction with pragmatic instruction-following. We therefore evaluate using a head-to-head comparison against Qwen-1.5-1.8B-Chat on Alpaca length-controlled (LC) evaluation. For each instruction in the AlpacaEval dataset, we generated outputs from both our model and the reference model. These pairs of outputs were then presented to an automatic evaluator, which determined a preference. A 50% win rate indicates that the evaluated model performs comparably to the reference model.

Figure [3](https://arxiv.org/html/2510.11677v1#S3.F3 "Figure 3 ‣ 3.1 Instruction Following Evaluation ‣ 3 Results ‣ Chronologically Consistent Generative AI Songrun He is at Washington University in St. Louis (h.songrun@wustl.edu). Linying Lv is at Washington University in St. Louis (llyu@wustl.edu). Asaf Manela is at Washington University in St. Louis (amanela@wustl.edu). Jimmy Wu is at Washington University in St. Louis (jimmywu@wustl.edu).") reports the resulting win rates across vintages. ChronoGPT-Instruct1999\text{ChronoGPT-Instruct}\_{1999} achieves a 12.59% win rate. Performance increases to 13.19% in 2005, 16.21% in 2010, and peaks at 16.79% in 2024. This steady improvement demonstrates that more recent training data consistently enhances instruction-following capabilities, with the 2024 vintage showing the strongest performance. Despite these gains, the overall low win rates largely stem from the significant disparity in pretraining data volume: the reference Qwen-1.5-1.8B-Chat model was pretrained on approximately 31 times more tokens than our base ChronoGPT models.

### 3.2 Chronological Consistency Validation

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Election year | | | | | |  | Accuracy | |
|  | 1992 | 2000 | 2008 | 2016 | 2020 | 2024 |  | Pre-cutoff | Post-cutoff |
| Correct output | Bill Clinton | George W. (Bush) | Barack Obama | Donald Trump | Joe Biden | Donald Trump |  |  |  |
| GPT-2 | Bill Clinton | Bill Clinton | Barack Obama | Donald Trump | George W. | George W. |  | 3/43/4 | 0/20/2 |
| GPT-2 XL | Bill Clinton | George W. | Barack Obama | Donald Trump | James A. | James Mattis |  | 4/44/4 | 0/20/2 |
| Llama-3.2-3B-Instruct | Bill Clinton | George W. | Barack Obama | Donald Trump | Joe Biden | R. |  | 5/55/5 | 0/10/1 |
| Qwen-1.5-1.8B-Chat | Bill Clinton | George W. | Barack Obama | Donald Trump | Joe Biden | Kamala |  | 5/55/5 | 0/10/1 |
| ChronoGPT-InstructRealtime\text{ChronoGPT-Instruct}\_{\text{Realtime}} | — | Bill Clinton | George W. | John F. | elect2019: | Joe Biden |  | — | 0/5 |
| ChronoGPT-Instruct1999\text{ChronoGPT-Instruct}\_{1999} | Bill Clinton | Bill Clinton | Bill Clinton | Clinton\nT | Obama\nT | John F. |  | 1/11/1 | 0/50/5 |
| ChronoGPT-Instruct2000\text{ChronoGPT-Instruct}\_{2000} | Bill Clinton | Bill Clinton | Bill Clinton | Bill Clinton | Bill Clinton | John W. |  | 1/21/2 | 0/40/4 |
| ChronoGPT-Instruct2001\text{ChronoGPT-Instruct}\_{2001} | Bill Clinton | George W. | Bill Clinton | George W. | George W. | Putin\nT |  | 2/22/2 | 0/40/4 |
| ChronoGPT-Instruct2002\text{ChronoGPT-Instruct}\_{2002} | Bill Clinton | George W. | Bill Clinton | George W. | George W. | George W. |  | 2/22/2 | 0/40/4 |
| ChronoGPT-Instruct2003\text{ChronoGPT-Instruct}\_{2003} | Bill Clinton | George W. | George W. | George W. | George W. | George W. |  | 2/22/2 | 0/40/4 |
| ChronoGPT-Instruct2004\text{ChronoGPT-Instruct}\_{2004} | Bill Clinton | George W. | George W. | George W. | George W. | Putin\nT |  | 2/22/2 | 0/40/4 |
| ChronoGPT-Instruct2005\text{ChronoGPT-Instruct}\_{2005} | Bill Clinton | George W. | George W. | George W. | George W. | George W. |  | 2/22/2 | 0/40/4 |
| ChronoGPT-Instruct2006\text{ChronoGPT-Instruct}\_{2006} | Bill Clinton | George W. | George W. | George W. | George W. | George W. |  | 2/22/2 | 0/40/4 |
| ChronoGPT-Instruct2007\text{ChronoGPT-Instruct}\_{2007} | Bill Clinton | George W. | George W. | George W. | George W. | George W. |  | 2/22/2 | 0/40/4 |
| ChronoGPT-Instruct2008\text{ChronoGPT-Instruct}\_{2008} | Bill Clinton | George W. | George W. | George W. | George W. | George W. |  | 2/32/3 | 0/30/3 |
| ChronoGPT-Instruct2009\text{ChronoGPT-Instruct}\_{2009} | Bill Clinton | George W. | George W. | George W. | George W. | George W. |  | 2/32/3 | 0/30/3 |
| ChronoGPT-Instruct2010\text{ChronoGPT-Instruct}\_{2010} | Bill Clinton | George W. | Barack Obama | Barack Obama | Bill Gates | Bill Gates |  | 3/33/3 | 0/30/3 |
| ChronoGPT-Instruct2011\text{ChronoGPT-Instruct}\_{2011} | Bill Clinton | George W. | Barack H. | John F. | Bill Gates | George W. |  | 3/33/3 | 0/30/3 |
| ChronoGPT-Instruct2012\text{ChronoGPT-Instruct}\_{2012} | Bill Clinton | George W. | Barack Obama | Barack Obama | Bill Gates | George W. |  | 3/33/3 | 0/30/3 |
| ChronoGPT-Instruct2013\text{ChronoGPT-Instruct}\_{2013} | Bill Clinton | George W. | Barack Obama | John F. | Bill Gates | George W. |  | 3/33/3 | 0/30/3 |
| ChronoGPT-Instruct2014\text{ChronoGPT-Instruct}\_{2014} | Bill Clinton | George W. | Barack Obama | John F. | George W. | George W. |  | 3/33/3 | 0/30/3 |
| ChronoGPT-Instruct2015\text{ChronoGPT-Instruct}\_{2015} | Bill Clinton | George W. | George W. | John F. | George W. | George W. |  | 2/32/3 | 0/30/3 |
| ChronoGPT-Instruct2016\text{ChronoGPT-Instruct}\_{2016} | Bill Clinton | George W. | George W. | Martin Luther King | George W. | George W. |  | 2/42/4 | 0/20/2 |
| ChronoGPT-Instruct2017\text{ChronoGPT-Instruct}\_{2017} | Bill Clinton | George W. | George W. | Donald Trump | John F. | John Kasich |  | 3/43/4 | 0/20/2 |
| ChronoGPT-Instruct2018\text{ChronoGPT-Instruct}\_{2018} | Bill Clinton | George W. | George W. | Donald Trump | Donald Trump | George W. |  | 3/43/4 | 0/20/2 |
| ChronoGPT-Instruct2019\text{ChronoGPT-Instruct}\_{2019} | Bill Clinton | George W. | George W. | Donald Trump | elect2019: | John Kasich |  | 3/43/4 | 0/20/2 |
| ChronoGPT-Instruct2020\text{ChronoGPT-Instruct}\_{2020} | Bill Clinton | George W. | George W. | Donald Trump | Bill Clinton | George W. |  | 3/53/5 | 0/10/1 |
| ChronoGPT-Instruct2021\text{ChronoGPT-Instruct}\_{2021} | Bill Clinton | George W. | George W. | Donald Trump | Joe Biden | Joe Biden |  | 4/54/5 | 0/10/1 |
| ChronoGPT-Instruct2022\text{ChronoGPT-Instruct}\_{2022} | Bill Clinton | George W. | George W. | Donald Trump | Joe Biden | Joe Biden |  | 4/54/5 | 0/10/1 |
| ChronoGPT-Instruct2023\text{ChronoGPT-Instruct}\_{2023} | Bill Clinton | George W. | George W. | Donald Trump | Joe Biden | Joe Biden |  | 4/54/5 | 0/10/1 |
| ChronoGPT-Instruct2024\text{ChronoGPT-Instruct}\_{2024} | Bill Clinton | George W. | George W. | Donald Trump | Joe Biden | Joe Biden |  | 4/64/6 | — |
| ChronoGPT-Instruct1999\text{ChronoGPT-Instruct}\_{1999} through ChronoGPT-Instruct2024\text{ChronoGPT-Instruct}\_{2024} | | | | | | | | 67/8367/83 | 0/730/73 |

Table 2: Next-Token Predictions of U.S. Presidents using ChronoGPT-Instruct

This table presents ChronoGPT-Instruct’s next-token predictions for prompts listing the incoming U.S. president alongside the three most recent predecessors. The model is tasked with predicting the name of the most recent president, which appears as the final missing entry in the sequence. The input prompt is structured as follows:

> “U.S. Presidents in chronological order:
>
> Took office in {year+p−31{}\_{p-3}+1}: President {namep-3}
>
> Took office in {year+p−21{}\_{p-2}+1}: President {namep-2}
>
> Took office in {year+p−11{}\_{p-1}+1}: President {namep-1}
>
> Took office in {year+p1{}\_{p}+1}: President  ”

The table shows the predictions generated by each model in the ChronoGPT-Instruct series. Each prediction consists of exactly two tokens, selected deterministically by choosing the most probable token at each step. Gray shading indicates prompts referencing years beyond the model’s knowledge cutoff, including elections in which the president-elect had not yet assumed office. Correct predictions are highlighted in blue. For comparison, outputs from GPT-2, GPT-2 XL (released in 2019), Llama-3.2-3B-Instruct (released in 2023), and Qwen-1.5-1.8B-Chat (released in 2024) are also included.



| Panel A: Input prompts | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Event year | Input prompt | | | | | |  | Correct output | |
| 2001 | The Sarbanes-Oxley Act was introduced in response to the 2001 Enron | | | | | |  | scandal | |
| 2003 | In 2003, a major public health crisis was the outbreak of the virus known as | | | | | |  | SARS | |
| 2008 | In 2008, the global economy was dominated by the subprime mortgage | | | | | |  | crisis | |
| 2016 | In 2016, market volatility increased surrounding the general vote known as the Brexit | | | | | |  | referendum | |
| 2020 | In 2020, the global economy was devastated by the health crisis known as the “ | | | | | |  | COVID/coronavirus | |
| 2022 | In 2022, a major milestone for generative AI was marked by the release of the AI chatbot known as “ | | | | | |  | ChatGPT | |
| Panel B: Output predictions | | | | | | | | | |
|  | Event year | | | | | |  | Accuracy | |
|  | 2001 | 2003 | 2008 | 2016 | 2020 | 2022 |  | Pre-cutoff | Post-cutoff |
| Correct output | scandal | SARS | crisis | referendum | COVID/coronavirus | ChatGPT |  |  |  |
| GPT-2 | scandal.\n | chikung | crisis, which | vote, with | Great Recession.” | The AI Bot |  | 2/42/4 | 0/20/2 |
| GPT-2 XL | scandal, in | SARS, | crisis. The | . The UK | Great Recession.” | Alexa,” |  | 3/43/4 | 0/20/2 |
| Llama-3.2-3B-Instruct | scandal, which | SARS ( | crisis, which | referendum. The | COVID-19 | LLaMA |  | 5/65/6 | — |
| Qwen-1.5-1.8B-Chat | scandal, which | SARS. | crisis. The | referendum. The | COVID-1 | ChatGPT |  | 6/66/6 | — |
| ChronoGPT-InstructRealtime\text{ChronoGPT-Instruct}\_{\text{Realtime}} | ment Act, | the “H | market, which | -Elli | H1N | AI Assistant” |  | — | 0/6 |
| ChronoGPT-Instruct1999\text{ChronoGPT-Instruct}\_{1999} | ies Act, | the “V | market, which | . The market | World Health Organization | Chatbot” |  | — | 0/60/6 |
| ChronoGPT-Instruct2000\text{ChronoGPT-Instruct}\_{2000} | ment Act, | the Ebola virus | market, which | . The market | Asian Crisis.” | Chatbot” |  | — | 0/60/6 |
| ChronoGPT-Instruct2001\text{ChronoGPT-Instruct}\_{2001} | ment Crisis in | the “Asian | market, which | . | Asian flu.” | The Chatbot |  | 0/10/1 | 0/50/5 |
| ChronoGPT-Instruct2002\text{ChronoGPT-Instruct}\_{2002} | scandal. It | the “H | market, which | . The market | Asian flu.” | AI-1 |  | 1/11/1 | 0/50/5 |
| ChronoGPT-Instruct2003\text{ChronoGPT-Instruct}\_{2003} | scandal. It | the SARS | market, which | vote. | Asian flu.” | Chatbot”. |  | 2/22/2 | 0/40/4 |
| ChronoGPT-Instruct2004\text{ChronoGPT-Instruct}\_{2004} | scandal. It | SARS, | market, which | hip. | Asian flu.” | Chatbot”. |  | 2/22/2 | 0/40/4 |
| ChronoGPT-Instruct2005\text{ChronoGPT-Instruct}\_{2005} | scandal. It | SARS, | market, which | . | Asian flu.” | Chatbot”. |  | 2/22/2 | 0/40/4 |
| ChronoGPT-Instruct2006\text{ChronoGPT-Instruct}\_{2006} | scandal. It | SARS. | market, which | . | Asian flu.” | Chatbot”. |  | 2/22/2 | 0/40/4 |
| ChronoGPT-Instruct2007\text{ChronoGPT-Instruct}\_{2007} | scandal. It | SARS, | market, which | . | Asian flu.” | Chatbot”. |  | 2/22/2 | 0/40/4 |
| ChronoGPT-Instruct2008\text{ChronoGPT-Instruct}\_{2008} | scandal. It | the SARS | crisis, which | . | Asian flu.” | Chatbot”. |  | 3/33/3 | 0/30/3 |
| ChronoGPT-Instruct2009\text{ChronoGPT-Instruct}\_{2009} | scandal. It | the SARS | crisis, which | . | SARS” | Chatbot”. |  | 3/33/3 | 0/30/3 |
| ChronoGPT-Instruct2010\text{ChronoGPT-Instruct}\_{2010} | scandal. It | the SARS | crisis, which | vote. | Spanish flu” | The Language Model |  | 3/33/3 | 0/30/3 |
| ChronoGPT-Instruct2011\text{ChronoGPT-Instruct}\_{2011} | scandal. It | the SARS | crisis, which | vote. | Asian flu.” | The Language Model |  | 3/33/3 | 0/30/3 |
| ChronoGPT-Instruct2012\text{ChronoGPT-Instruct}\_{2012} | scandal, which | the SARS | crisis, which | vote. | Asian flu” | The Language Model |  | 3/33/3 | 0/30/3 |
| ChronoGPT-Instruct2013\text{ChronoGPT-Instruct}\_{2013} | scandal, which | the SARS | crisis, which | vote. The | Asian flu” | The Turing Test |  | 3/33/3 | 0/30/3 |
| ChronoGPT-Instruct2014\text{ChronoGPT-Instruct}\_{2014} | scandal, which | the SARS | crisis, which | of the year | Spanish flu” | The Turing Test |  | 3/33/3 | 0/30/3 |
| ChronoGPT-Instruct2015\text{ChronoGPT-Instruct}\_{2015} | scandal, which | the SARS | crisis, which | -Elli | Spanish flu” | AI Language Model |  | 3/33/3 | 0/30/3 |
| ChronoGPT-Instruct2016\text{ChronoGPT-Instruct}\_{2016} | scandal. It | the SARS | crisis, which | . The European | Asian flu” | The Chatbot |  | 3/43/4 | 0/20/2 |
| ChronoGPT-Instruct2017\text{ChronoGPT-Instruct}\_{2017} | scandal, which | the SARS | crisis, which | referendum. The | Asian flu” | The Chatbot |  | 4/44/4 | 0/20/2 |
| ChronoGPT-Instruct2018\text{ChronoGPT-Instruct}\_{2018} | scandal. It | the SARS | crisis, which | referendum. The | Asian flu” | The Chatbot |  | 4/44/4 | 0/20/2 |
| ChronoGPT-Instruct2019\text{ChronoGPT-Instruct}\_{2019} | scandal, which | the SARS | crisis, which | referendum. The | H1N | The Chatbot |  | 4/44/4 | 0/20/2 |
| ChronoGPT-Instruct2020\text{ChronoGPT-Instruct}\_{2020} | scandal, which | SARS- | crisis, which | referendum. The | Spanish flu” | AI Language Model |  | 4/54/5 | 0/10/1 |
| ChronoGPT-Instruct2021\text{ChronoGPT-Instruct}\_{2021} | scandal, which | SARS in | crisis, which | referendum. | coronav | AI Assistant” |  | 5/55/5 | 0/10/1 |
| ChronoGPT-Instruct2022\text{ChronoGPT-Instruct}\_{2022} | Corporation collapse, | the SARS | crisis, which | referendum. The | coronav | AI Assistant” |  | 5/65/6 | — |
| ChronoGPT-Instruct2023\text{ChronoGPT-Instruct}\_{2023} | scandal, which | SARS, | crisis, which | referendum. The | coronav | ChatGPT |  | 6/66/6 | — |
| ChronoGPT-Instruct2024\text{ChronoGPT-Instruct}\_{2024} | scandal. It | SARS, | crisis, which | referendum. The | COVID- | ChatGPT |  | 6/66/6 | — |
| ChronoGPT-Instruct1999\text{ChronoGPT-Instruct}\_{1999} through ChronoGPT-Instruct2024\text{ChronoGPT-Instruct}\_{2024} | | | | | | |  | 76/8076/80 | 0/760/76 |

Table 3: Next-Token Predictions of Major Events using ChronoGPT-Instruct

This table presents ChronoGPT-Instruct’s next-token predictions for prompts describing major historical events across a range of years. Panel A displays the input prompts for each event, and Panel B shows the corresponding predictions produced by each model in the ChronoGPT-Instruct series. Each prediction consists of exactly three tokens, selected deterministically by choosing the most probable token at each step. Gray shading indicates prompts that reference events beyond the model’s knowledge cutoff. Correct predictions are highlighted in blue. For comparison, outputs from GPT-2, GPT-2 XL (released in 2019), Llama-3.2-3B-Instruct (released in 2023), and Qwen-1.5-1.8B-Chat (released in 2024) are also included.

While we take great care in curating our training data to ensure it includes only information believed to be available as of a specific date, the process is not immune to error. Such errors may originate in either the pretraining or finetuning datasets. In the case of pretraining data, inaccuracies in recorded publication dates, such as those introduced when printed materials are digitized via optical character recognition (OCR) and assigned incorrect timestamps, can lead to the inadvertent inclusion of information that was not actually available at the intended time. For finetuning, classification was performed using GPT-4.1, which may misidentify whether certain prompt-response pairs reflect knowledge from before or after the year 2000. These issues can result in lookahead bias, unintentionally exposing the model to information that should not have been available at the specified training cutoff.

For the pretraining dataset, He et al. ([2025](https://arxiv.org/html/2510.11677v1#bib.bib6)) test for leakage in the ChronoGPT series using textual sequences involving U.S. presidents and major events from various years, and find no evidence of leakage. In this section, we replicate their validation exercise for ChronoGPT-Instruct to test whether there is additional leakage introduced in the instruction finetuning process.

Table [2](https://arxiv.org/html/2510.11677v1#S3.T2 "Table 2 ‣ 3.2 Chronological Consistency Validation ‣ 3 Results ‣ Chronologically Consistent Generative AI Songrun He is at Washington University in St. Louis (h.songrun@wustl.edu). Linying Lv is at Washington University in St. Louis (llyu@wustl.edu). Asaf Manela is at Washington University in St. Louis (amanela@wustl.edu). Jimmy Wu is at Washington University in St. Louis (jimmywu@wustl.edu).") presents the test involving U.S. presidents and Table [3](https://arxiv.org/html/2510.11677v1#S3.T3 "Table 3 ‣ 3.2 Chronological Consistency Validation ‣ 3 Results ‣ Chronologically Consistent Generative AI Songrun He is at Washington University in St. Louis (h.songrun@wustl.edu). Linying Lv is at Washington University in St. Louis (llyu@wustl.edu). Asaf Manela is at Washington University in St. Louis (amanela@wustl.edu). Jimmy Wu is at Washington University in St. Louis (jimmywu@wustl.edu).") presents the test involving major events. In both tables, the gray-shaded area in the top-right indicates predictions in the post-knowledge cutoff period, and the non-shaded lower-right denotes predictions strictly in the pre-knowledge cutoff period. Correct predictions are highlighted in blue.

Within the respective knowledge window of each version of ChronoGPT-Instruct, ChronoGPT-Instruct correctly makes a majority of predictions (67 out of 83) for the U.S. presidents test and correctly makes most predictions (76 out of 80) for the major events test. The high accuracy in the pre-knowledge cutoff period reflects the quality and temporal relevance of the ChronoGPT-Instruct’s knowledge. In contrast, during the post-cutoff period represented by the gray-shaded area, none of the ChronoGPT-Instruct models correctly predict any future president or major event. Overall, these findings validate that the textual data used to train or finetune our chronologically consistent models contains no evidence of leakage.

### 3.3 Prompt-Based Trading Portfolios

While He et al. ([2025](https://arxiv.org/html/2510.11677v1#bib.bib6)) highlight the potential of ChronoGPT to generate profitable signals through embeddings following Chen et al. ([2023](https://arxiv.org/html/2510.11677v1#bib.bib3)), it remains an open question how well directly prompting a chronologically consistent model can serve a similar purpose. Lopez-Lira and Tang ([2023](https://arxiv.org/html/2510.11677v1#bib.bib9)) demonstrate that prompting LLMs can yield robust trading signals for a limited time period after the model’s knowledge cutoff, without introducing lookahead bias. With ChronoGPT-Instruct, we extend this line of inquiry by conducting prompt-based portfolio construction over a substantially longer time horizon, from January 2007 to July 2023.

To operationalize this investigation, we apply the following prompt to financial news headlines at the stock-day level, for all stocks with news coverage, similar to Lopez-Lira and Tang ([2023](https://arxiv.org/html/2510.11677v1#bib.bib9)):

{
### Instruction:
  
Classify this news headline as either FAVORABLE, or UNFAVORABLE, or UNCLEAR for the stock price of company. 
  
### Input:
  
{headlines} 
  
### Response:
}

We then form portfolios based on the LLM’s response. The stock is assigned to the favorable news (HH) or unfavorable news (LL) portfolio based on the first word generated by the LLM. If the first word is neither “favorable” nor “unfavorable”, the stock is assigned to the “unclear” portfolio. A long-short portfolio (H−LH-L) is formed from longing the favorable news portfolio and shorting the unfavorable news portfolio.

We evaluate this strategy on ChronoGPT-InstructRealtime\text{ChronoGPT-Instruct}\_{\text{Realtime}}, which is trained and tuned entirely on data before the prediction year, and is free from lookahead bias.
For comparison, we also include results from Qwen-1.5-1.8B-Chat, Llama-3.2-3B-Instruct and Llama-3.2-1B-Instruct. The model closest in size is Qwen-1.5-1.8B-Chat, which has a 20% larger parameter count. The next larger model, Llama-3.2-3B-Instruct, has twice the parameter count. Both models are trained on substantially more data than ChronoGPT-Instruct.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | ChronoGPT-InstructRealtime\text{ChronoGPT-Instruct}\_{\text{Realtime}} | | | Qwen-1.5-1.8B-Chat | | |
|  | Mean | SD | SR | Mean | SD | SR |
| Unfavorable (LL) | 1.35 | 24.53 | 0.05 | -1.67 | 25.90 | -0.06 |
| Unclear | 0.14 | 29.03 | 0.00 | 7.20 | 78.95 | 0.09 |
| Favorable (HH) | 9.51 | 23.33 | 0.41 | 10.55 | 22.72 | 0.46 |
| H−LH-L | 8.17 | 8.63 | 0.95 | 12.21 | 8.00 | 1.53 |
|  | Llama-3.2-3B-Instruct | | | Llama-3.2-1B-Instruct | | |
|  | Mean | SD | SR | Mean | SD | SR |
| Unfavorable (LL) | -1.11 | 25.68 | -0.04 | 4.67 | 23.64 | 0.20 |
| Unclear | 6.71 | 23.17 | 0.29 | 14.01 | 23.04 | 0.61 |
| Favorable (HH) | 13.46 | 23.31 | 0.58 | 7.31 | 23.91 | 0.31 |
| H−LH-L | 14.58 | 8.31 | 1.76 | 2.64 | 6.91 | 0.38 |

Table 4: Performance of Prompt-Based Trading Portfolios

This table presents annualized performance metrics (mean return, standard deviation, and Sharpe ratio) for portfolios sorted by the LLM’s direct response categorizing the news headlines as favorable news (HH), unfavorable news (LL), or unclear. The H−LH-L row represents a strategy of going long on the portfolio of stocks classified as having favorable news (HH) and short on those with unfavorable news (LL).
All values are in percentage points except the Sharpe ratios. All portfolios are equal-weighted and rebalanced daily. Data spans January 2007–July 2023.



![Refer to caption](x1.png)

Figure 4: Portfolio Performance across ChronoGPT-Instruct Vintages

This figure illustrates the Sharpe ratios of long-short portfolios constructed using predictions by ChronoGPT-Instruct, with each model pretrained on text data up to the time points indicated on the x-axis. The blue dashed line represents the performance of the ChronoGPT-InstructRealtime{}\_{\text{Realtime}}, using the model from the year before the prediction year. The shaded regions represent the 95% confidence intervals.

Table [4](https://arxiv.org/html/2510.11677v1#S3.T4 "Table 4 ‣ 3.3 Prompt-Based Trading Portfolios ‣ 3 Results ‣ Chronologically Consistent Generative AI Songrun He is at Washington University in St. Louis (h.songrun@wustl.edu). Linying Lv is at Washington University in St. Louis (llyu@wustl.edu). Asaf Manela is at Washington University in St. Louis (amanela@wustl.edu). Jimmy Wu is at Washington University in St. Louis (jimmywu@wustl.edu).") presents the results of the prompt-based trading portfolios. The realtime ChronoGPT-Instruct model achieves a Sharpe ratio of 0.95, outperforming Llama-3.2-1B-Instruct while underperforming the comparatively larger models, Qwen-1.5-1.8B-Chat and Llama-3.2-3B-Instruct.

If a chronologically consistent model matches an inconsistent counterpart in architecture and training, then matching return performance would imply that the inconsistent model’s predictability does not rely on leakage. In our setting, return predictability reflects two forces: language capability, which typically increases with parameter count and training tokens, and lookahead bias. ChronoGPT-Instruct is smaller and trained on fewer tokens than Qwen-1.5-1.8B-Chat and Llama-3.2-3B-Instruct, so its performance serves as a conservative lower bound for the leakage-free component. Comparing ChronoGPT-InstructRealtime\text{ChronoGPT-Instruct}\_{\text{Realtime}}’s Sharpe ratio of 0.95 to that of Qwen-1.5-1.8B-Chat’s (1.53) and Llama-3.2-3B-Instruct’s (1.76), at least 54% to 62% of the apparent return predictability persists in the absence of data leakage. The remaining gap in Sharpe ratios (e.g., between 0.95 and 1.76) likely reflects a combination of differences in model capacity and lookahead bias in the comparison model.

He et al. ([2025](https://arxiv.org/html/2510.11677v1#bib.bib6)) pose a critical question: while later models demonstrate more up-to-date knowledge and improved language understanding as they are trained on more data over time, does this translate into economic gains? To test this, they evaluate the trading performance of the entire series of chronologically consistent models. Our analysis using instruction-tuned versions of those same models reveals a distinct performance pattern in Figure [4](https://arxiv.org/html/2510.11677v1#S3.F4 "Figure 4 ‣ 3.3 Prompt-Based Trading Portfolios ‣ 3 Results ‣ Chronologically Consistent Generative AI Songrun He is at Washington University in St. Louis (h.songrun@wustl.edu). Linying Lv is at Washington University in St. Louis (llyu@wustl.edu). Asaf Manela is at Washington University in St. Louis (amanela@wustl.edu). Jimmy Wu is at Washington University in St. Louis (jimmywu@wustl.edu).") that corroborates their “envelope” phenomenon.

The primary explanation for this envelope pattern is twofold. First, the results demonstrate that lookahead bias is modest. If significant lookahead bias were present, the final model, with the most comprehensive knowledge, would have been the top performer across all periods. The fact that it is not indicates that its ’knowledge of the future’ does not grant it an unfair advantage for past data.

Second, and more critically for this task, further improvements in knowledge and generic language ability add only marginal value. The strong performance of even the earliest models shows that the performance frontier is reached relatively quickly. A key factor here is temporal alignment, that a model’s calibration to the specific language, vocabulary, and market narratives of its own era. Expressions such as “meme stocks” or “supply-chain disruptions” carry period-specific meanings, and interpreting them through a future-biased lens can misalign signals and erode predictive accuracy.

However, we identify a notable distinction in our results: the performance gap between the real-time model and the other vintage models is less pronounced than in the original study. While the real-time model still outperforms the average vintage, its advantage is diminished.

We hypothesize that this attenuated effect stems from the IFT process applied across all vintages. Because the IFT dataset is temporally fixed to a pre-1999 period, all models may become less temporally aligned with their respective pretraining eras. By finetuning every vintage on linguistic patterns from a single, static historical era, the unique temporal signature learned during pretraining is likely diluted. This “anchoring” to a past linguistic style may weaken the specialized advantage of the real-time model, thereby compressing the performance difference across the different vintages.

## 4 Conclusion

We address lookahead bias in LLM-based predictions by releasing the first chronologically consistent instruction-following language models whose training corpora are explicitly time-stamped. For example, ChronoGPT-Instruct1999\text{ChronoGPT-Instruct}\_{1999} is trained and subsequently instruction-finetuned exclusively on text available up to 1999, giving researchers over two decades of true out-of-sample period for evaluation.

While we acknowledge that temporal constraints necessarily limit model performance compared to contemporary alternatives, ChronoGPT-Instruct models offer a conservative lower bound for quantifying lookahead bias. A practical way to gauge the extent of lookahead bias is to compare ChronoGPT-Instruct with similarly sized but temporally inconsistent models such as Qwen-1.5-1.8B-Chat or Llama-3.2-3B-Instruct. Instead of achieving state-of-the-art performance, our aim is to provide an easy-to-use, replicable benchmark for quantifying lookahead bias in a wide range of prompt-based prediction tasks.

## References

* Chang et al. (2023)

  Chang, Anne, Xi Dong, Xiumin Martin, and Changyun Zhou, 2023, Ai democratization, return predictability, and trading inequality, Available at SSRN 4543999 .
* Chen et al. (2025)

  Chen, Jian, Guohao Tang, Guofu Zhou, and Wu Zhu, 2025, Chatgpt and deepseek: Can they predict the stock market and macroeconomy?, arXiv preprint arXiv:2502.10008 .
* Chen et al. (2023)

  Chen, Yifei, Bryan T. Kelly, and Dacheng Xiu, 2023, Expected returns and large language models, SSRN Electronic Journal .
* Engelberg et al. (2025)

  Engelberg, Joseph, Asaf Manela, William Mullins, and Luka Vulicevic, 2025, Entity neutering, Available at SSRN .
* Glasserman and Lin (2023)

  Glasserman, Paul, and Caden Lin, 2023, Assessing look-ahead bias in stock return predictions generated by gpt sentiment analysis, arXiv preprint arXiv:2309.17322 .
* He et al. (2025)

  He, Songrun, Linying Lv, Asaf Manela, and Jimmy Wu, 2025, Chronologically consistent large language models, arXiv preprint arXiv:2502.21206 .
* Jha et al. (2024)

  Jha, Manish, Jialin Qian, Michael Weber, and Baozhong Yang, 2024, Chatgpt and corporate policies, Technical report, National Bureau of Economic Research.
* Lambert et al. (2024)

  Lambert, Nathan, Jacob Morrison, Valentina Pyatkin, Shengyi Huang, Hamish Ivison, Faeze Brahman, Lester James V Miranda, Alisa Liu, Nouha Dziri, Shane Lyu, et al., 2024, Tulu 3: Pushing frontiers in open language model post-training, arXiv preprint arXiv:2411.15124 .
* Lopez-Lira and Tang (2023)

  Lopez-Lira, Alejandro, and Yuehua Tang, 2023, Can ChatGPT forecast stock price movements? return predictability and large language models, SSRN Electronic Journal .
* Ludwig et al. (2025)

  Ludwig, Jens, Sendhil Mullainathan, and Ashesh Rambachan, 2025, Large language models: An applied econometric framework, Technical report, National Bureau of Economic Research.
* Lv (2025)

  Lv, Linying, 2025, Do sell-side analyst reports have investment value?, arXiv preprint arXiv:2502.20489 .
* Raschka (2024)

  Raschka, Sebastian, 2024, Build a large language model (from scratch) (Simon and Schuster).
* Sarkar (2024)

  Sarkar, Suproteem, 2024, StoriesLM: A family of language models with time-indexed training data, SSRN Electronic Journal .
* Sarkar and Vafa (2024)

  Sarkar, Suproteem K, and Keyon Vafa, 2024, Lookahead bias in pretrained language models, Available at SSRN .
* Wang et al. (2022)

  Wang, Yizhong, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A Smith, Daniel Khashabi, and Hannaneh Hajishirzi, 2022, Self-instruct: Aligning language models with self-generated instructions, arXiv preprint arXiv:2212.10560 .