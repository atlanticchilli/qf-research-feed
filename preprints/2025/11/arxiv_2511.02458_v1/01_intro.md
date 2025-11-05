---
authors:
- Giulia Iadisernia
- Carolina Camassa
doc_id: arxiv:2511.02458v1
family_id: arxiv:2511.02458
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Prompting for Policy: Forecasting Macroeconomic Scenarios with Synthetic LLM
  Personas'
url_abs: http://arxiv.org/abs/2511.02458v1
url_html: https://arxiv.org/html/2511.02458v1
venue: arXiv q-fin
version: 1
year: 2025
---


Giulia Iadisernia
Banca d’ItaliaRomeItaly
 and 
Carolina Camassa
Banca d’ItaliaRomeItaly
[carolina.camassa@bancaditalia.it](mailto:carolina.camassa@bancaditalia.it)

(2025)

###### Abstract.

We evaluate whether persona-based prompting improves Large Language Model (LLM) performance on macroeconomic forecasting tasks. Using 2,368 economics-related personas from the PersonaHub corpus, we prompt GPT-4o to replicate the ECB Survey of Professional Forecasters across 50 quarterly rounds (2013-2025). We compare the persona-prompted forecasts against the human experts panel, across four target variables (HICP, core HICP, GDP growth, unemployment) and four forecast horizons. We also compare the results against 100 baseline forecasts without persona descriptions to isolate its effect. We report two main findings. Firstly, GPT-4o and human forecasters achieve remarkably similar accuracy levels, with differences that are statistically significant yet practically modest. Our out-of-sample evaluation on 2024-2025 data demonstrates that GPT-4o can maintain competitive forecasting performance on unseen events, though with notable differences compared to the in-sample period. Secondly, our ablation experiment reveals no measurable forecasting advantage from persona descriptions, suggesting these prompt components can be omitted to reduce computational costs without sacrificing accuracy. Our results provide evidence that GPT-4o can achieve competitive forecasting accuracy even on out-of-sample macroeconomic events, if provided with relevant context data, while revealing that diverse prompts produce remarkably homogeneous forecasts compared to human panels.

large language models, prompt engineering, monetary policy, central bank communication, financial forecasting

††copyright: acmlicensed††journalyear: 2025††copyright: acmlicensed††conference: 6th ACM International Conference on AI in Finance; November 15–18, 2025; Singapore, Singapore††booktitle: 6th ACM International Conference on AI in Finance (ICAIF ’25), November 15–18, 2025, Singapore, Singapore††doi: 10.1145/3768292.3770385††isbn: 979-8-4007-2220-2/2025/11††ccs: Computing methodologies Natural language processing††ccs: Applied computing Economics
![Refer to caption](figures/Prompting_for_policy_diagram.png)


Figure 1. Experimental pipeline for evaluating synthetic LLM personas in macroeconomic forecasting. Starting from the PersonaHub corpus of 370M domain expert descriptions, we apply multi-stage filtering to extract 2,368 relevant personas. Each persona is then prompted to simulate responses to the ECB Survey of Professional Forecasters across 50 quarterly rounds (2013-2025), generating forecasts for four key macroeconomic variables (HICP inflation, core HICP, real GDP growth, unemployment) at multiple forecast horizons. The resulting 118,400 AI-generated forecasts are compared against human expert predictions to evaluate forecasting accuracy and the contribution of persona prompting to LLM performance in economic tasks.††:

## 1. Introduction

Table 1. The ECB Survey of Professional Forecasters: data description

(a) Main macroeconomic variables included in the ECB’s Survey of Professional Forecasters

|  |  |
| --- | --- |
| Variable | Definition |
| HICP | Harmonized Index of Consumer Prices (inflation) |
| HICPX∗ | Core HICP (excl. energy, food, alcohol, tobacco) |
| rGDP | Real GDP growth rate (annual %) |
| UNR | Unemployment rate (% of labor force) |

∗HICPX is included in SPF rounds since 2016Q4.

(b) Dataset overview: number of human forecasts from ECB data VS simulated forecasts with AI

|  |  |  |  |
| --- | --- | --- | --- |
| Data source | SPF Rounds | Forecasters | Forecasts |
| *Human SPF* | | | |
| In-sample | 44 | 56.2∗ | ∼\sim2,473 |
| Out-of-sample | 6 | 58.4∗ | ∼\sim350 |
| *AI personas (per model)* | | | |
| With personas | 50 | 2,368 | 118,400 |
| No-persona baseline | 50 | 100 | 5,000 |

∗Average per round.

Macroeconomic forecasting has become increasingly critical for central bank communication and the transmission of monetary policy. The European Central Bank Survey of Professional Forecasters (ECB-SPF) (Angel, [2003](https://arxiv.org/html/2511.02458v1#bib.bib2)), conducted quarterly since 1999, represents one of the most systematic efforts to capture expert expectations of inflation, GDP growth, and unemployment in the euro area. Because these forecasts directly influence policy decisions and market expectations, producing accurate and consistent forecasts is essential for economic stability.

Large Language Models (LLMs) have emerged as promising tools for economic forecasting tasks, offering the potential to simulate expert judgment at scale. Yet, current applications face a key methodological limitation: most studies using LLMs to simulate economic forecasts (Hansen et al., [2025](https://arxiv.org/html/2511.02458v1#bib.bib11)) or model inflation expectations (Zarifhonarvar, [2024](https://arxiv.org/html/2511.02458v1#bib.bib20)) typically rely on one or few handcrafted “expert prompts”.
Despite the increasing adoption of LLMs in economic research (Ludwig et al., [2025](https://arxiv.org/html/2511.02458v1#bib.bib16)), and the fact that LLM output is highly sensitive to prompt content and even formatting (Sclar et al., [2024](https://arxiv.org/html/2511.02458v1#bib.bib18)), there is a lack of empirical evidence on how prompt design affects performance in economics tasks.

We build on this premise by producing the first systematic replication of the ECB Survey of Professional Forecasters using LLMs. Our main research question is: Do sophisticated persona descriptions—detailed biographical prompts designed to simulate specific expert types—improve LLM performance in a macroeconomic forecasting task?
We answer the question by extracting 2,368 economics-related synthetic biographies from the Persona Hub corpus111<https://huggingface.co/datasets/proj-persona/PersonaHub>.(Ge et al., [2024](https://arxiv.org/html/2511.02458v1#bib.bib9)).
We evaluate the performance of these personas on 50 quarterly rounds (2013Q1-2025Q2) of the Survey of Professional Forecasters. This results in 118,400 AI-generated forecasts for four key macroeconomic variables at multiple forecast horizons. Our experimental design includes both in-sample evaluation (2013Q1-2023Q4) and out-of-sample testing on 2024-2025 data, which falls outside the model’s training data.

Our study makes three main contributions. First, we conduct the first systematic replication of the ECB Survey of Professional Forecasters using LLMs, extending previous US-focused studies to European monetary policy contexts. Second, we implement a large-scale experimental design evaluating the macroeconomic forecasting performance of over 2,000 LLM-based synthetic personas. We compare these forecasts both to realized economic outcomes and, perhaps more interestingly, to the forecasting patterns of a panel of human experts. Third, we conduct a controlled ablation experiment to isolate the specific contribution of persona descriptions.
We observe two main results: while LLMs can achieve competitive forecasting performance alongside human experts, the sophisticated persona descriptions contribute negligible improvements over simple baseline prompts. This result has significant implications for practitioners, suggesting that computational resources may be better allocated to ensemble methods or model improvements rather than elaborate persona engineering.
These insights contribute to the growing understanding of LLMs as “synthetic forecasters” while providing practical guidance for central banks and financial institutions considering AI-augmented forecasting systems. Our results suggest that effective LLM-based forecasting may depend more on robust data integration and model architecture than on prompt engineering.

The remainder of this paper is organized as follows. Section [2](https://arxiv.org/html/2511.02458v1#S2 "2. Related work ‣ Prompting for Policy: Forecasting Macroeconomic Scenarios with Synthetic LLM Personas") reviews related work on LLM forecasting and prompt engineering. Section [3](https://arxiv.org/html/2511.02458v1#S3 "3. Data and experimental setup ‣ Prompting for Policy: Forecasting Macroeconomic Scenarios with Synthetic LLM Personas") describes our data and experimental setup, including the ECB Survey of Professional Forecasters, and the persona dataset. Section [3.4](https://arxiv.org/html/2511.02458v1#S3.SS4 "3.4. Scoring metrics ‣ 3. Data and experimental setup ‣ Prompting for Policy: Forecasting Macroeconomic Scenarios with Synthetic LLM Personas") outlines our evaluation methodology. Section [4](https://arxiv.org/html/2511.02458v1#S4 "4. Results ‣ Prompting for Policy: Forecasting Macroeconomic Scenarios with Synthetic LLM Personas") presents results on the effectiveness of persona prompting, forecasting accuracy and human vs AI panel performance. Section [5](https://arxiv.org/html/2511.02458v1#S5 "5. Future work ‣ Prompting for Policy: Forecasting Macroeconomic Scenarios with Synthetic LLM Personas") discusses future work, and Section [6](https://arxiv.org/html/2511.02458v1#S6 "6. Conclusion ‣ Prompting for Policy: Forecasting Macroeconomic Scenarios with Synthetic LLM Personas") concludes.

![Refer to caption](figures/F1B-range-bars/img/hicpx_t1_rangefill.png)


Figure 2. AI and human forecasters achieve remarkably similar accuracy across key macroeconomic variables. Time series comparison of realized outcomes (black), human expert forecasts from the ECB Survey of Professional Forecasters (orange), and AI forecasts using 2,368 synthetic personas (blue) for euro area core inflation (2016-2025). Despite using a variety of persona descriptions, LLM predictions converge to a much narrower forecast distribution compared to the human experts.††: Forecast comparison for euro area core inflation

## 2. Related work

#### Macroeconomic forecasting with Large Language Models

The application of large language models to macroeconomic forecasting has emerged as a significant research area at the intersection of artificial intelligence and economics. Recent studies have explored direct applications of LLMs to a variety of forecasting tasks. Several studies share our focus on macroeconomic variables: Carriero et al. ([2024](https://arxiv.org/html/2511.02458v1#bib.bib5)) examined LLM performance on macroeconomic time series, Bybee ([2023](https://arxiv.org/html/2511.02458v1#bib.bib4)) fed Wall Street Journal articles to an LLM to predict financial and macroeconomic variables, while Faria-e Castro and Leibovici ([2024](https://arxiv.org/html/2511.02458v1#bib.bib7)) demonstrated that Google’s PaLM model could generate competitive inflation forecasts.
Our work extends these existing studies primarily through our rigorous focus on persona prompting and the deployment of a panel of more than 2,000 ”synthetic forecasters”, which enables systematic comparison against both expert human panels and realized macroeconomic outcomes.
Beyond evaluating LLM performance in specific forecasting applications, ongoing research has investigated general methodological approaches to LLM-based forecasting. Lopez-Lira et al. ([2025](https://arxiv.org/html/2511.02458v1#bib.bib15)) investigated memorization effects in LLM-based economic forecasts, while Tan et al. ([2024](https://arxiv.org/html/2511.02458v1#bib.bib19)) compared language models to traditional time series methods. This methodological investigation connects to parallel efforts developing rigorous frameworks for LLM usage in economics research, which has become increasingly important as the field matures (Ludwig et al., [2025](https://arxiv.org/html/2511.02458v1#bib.bib16); Korinek, [2023](https://arxiv.org/html/2511.02458v1#bib.bib14)).

#### Simulating surveys responses

A related strand of research examines LLMs’ capacity to simulate human survey responses and expert judgment, similar to our comparison of human and AI panels in the Survey of Professional Forecasters. Zarifhonarvar ([2024](https://arxiv.org/html/2511.02458v1#bib.bib20)) investigated inflation expectations formation using generative AI, finding that LLMs replicate key behavioral patterns including the tendency to predict higher inflation than realized rates. Horton ([2023](https://arxiv.org/html/2511.02458v1#bib.bib12)) explored LLMs as ”simulated economic agents”, while Argyle et al. ([2023](https://arxiv.org/html/2511.02458v1#bib.bib3)) demonstrated that language models can replicate human samples in political surveys. Geng et al. ([2024](https://arxiv.org/html/2511.02458v1#bib.bib10)) and Fell ([2024](https://arxiv.org/html/2511.02458v1#bib.bib8)) examined LLMs’ ability to simulate social survey responses, though Dominguez-Olmedo et al. ([2024](https://arxiv.org/html/2511.02458v1#bib.bib6)) identified important limitations regarding ordering and labeling biases in LLM survey responses.
Most directly relevant to our investigation, Hansen et al. ([2025](https://arxiv.org/html/2511.02458v1#bib.bib11)) conducted the first systematic replication of the U.S. Survey of Professional Forecasters using LLMs, demonstrating comparable accuracy between AI and human forecasts. Their approach employed manually crafted forecaster personas based on SPF participant characteristics, in contrast with our larger extraction of persona prompts from the PersonaHub dataset.

#### Persona prompting

A parallel line of research has examined the effects of prompt design and expert personas on LLM behavior. LLMs are highly sensitive to prompt content, structure, and formatting, as demonstrated by Sclar et al. ([2024](https://arxiv.org/html/2511.02458v1#bib.bib18)), who show that even subtle variations in prompt phrasing can lead to large shifts in model output. This sensitivity complicates the interpretation of results in applied settings, where changes in tone, emphasis, or structure may unintentionally influence forecast quality. One strategy to improve LLM performance on reasoning tasks involves persona prompting or role-play. Kong et al. ([2024](https://arxiv.org/html/2511.02458v1#bib.bib13)) introduces a role-play prompting method in which LLMs are instructed to assume the identity of domain experts. This approach improves zero-shot performance across multiple benchmarks and has inspired further exploration of expert simulation in applied domains, including economics.
Persona prompting has also been used in macroeconomic forecasting experiments (Hansen et al., [2025](https://arxiv.org/html/2511.02458v1#bib.bib11); Zarifhonarvar, [2024](https://arxiv.org/html/2511.02458v1#bib.bib20)). Zarifhonarvar ([2024](https://arxiv.org/html/2511.02458v1#bib.bib20)) prompts LLM to adopt distinct persona attributes, such as political orientation, background, and socioeconomic characteristics. This induces realistic behaviors like partisan bias in inflation expectations, which mirror behaviors observed in actual human surveys. Hansen et al. ([2025](https://arxiv.org/html/2511.02458v1#bib.bib11)) construct detailed forecaster personas by manually gathering background data on SPF participants, including education, institutional affiliations, professional roles, and degrees. The study finds that removing these personas, i.e. replacing them with a generic forecaster prompt, leads to measurable drops in forecast accuracy, highlighting the value of role-based prompting. Interestingly, this is partially in contrast with our findings as presented in Section [4](https://arxiv.org/html/2511.02458v1#S4 "4. Results ‣ Prompting for Policy: Forecasting Macroeconomic Scenarios with Synthetic LLM Personas").

Table 2. Examples of economics-related blurbs contained in the PersonaHub dataset, evaluated on the three dimensions relevant to our study: EU-centrality, neutrality and monetary policy depth. Only one meets all three criteria and was retained for the experiments.

|  |  |  |  |
| --- | --- | --- | --- |
| Persona blurb (truncated) | EU centrality | Neutrality | Expertise |
| “A financial economist who specializes in the analysis of economic cycles and monetary policy. This person is interested in the degree of synchronisation of the euro area’s economic cycle with that of the US, and how this affects the implementation of monetary policies. They are also interested in the factors that contribute to the degree of synchronisation and how they differ between the euro area and the US.” | ✓\checkmark | ✓\checkmark | ✓\checkmark |
| “A global economist with Bank of America Merrill Lynch, with expertise in inflation and deflation, particularly in the context of the US and Europe. They are optimistic about the potential for economic growth in the US, but also recognize the potential for shocks that could trigger deflation.” | ✗ | ✗ | ✓\checkmark |
| “A technologist who is skeptical of the effectiveness of information technology in stimulating economic growth. This persona believes that technology must be implemented and funded in order to generate economic growth. They also believe that the central bank’s role in manipulating financial markets is a major impediment to economic growth.” | ✗ | ✗ | ✗ |

## 3. Data and experimental setup

### 3.1. Persona dataset

Starting from the Persona Hub corpus (Ge et al., [2024](https://arxiv.org/html/2511.02458v1#bib.bib9)), which is publicly available and contains ≈\approx 370 million descriptions of domain experts (pip\_{i}), we implement a multi-stage filtering pipeline to extract only the items relevant to our study. The Persona Hub dataset includes highly heterogeneous personas—from lawyers to artists and policy analysts—thus requiring several layers of domain-specific filtering. The steps below were applied in the order presented:

1. (1)

   Keyword search and domain filtering: retain entries containing ≥2\geq 2 tokens from a lexicon of terms related to monetary policy and the ECB (e.g., “central banking”, “monetary policy”, “Governing Council”). The dataset also includes four domain columns that were used as additional filtering dimensions. This step broadly excludes irrelevant personas while preserving those in macroeconomic or financial domains.
2. (2)

   Name filtering: using a named entity recognition (NER) algorithm, remove any description that directly mentions individuals (e.g., “Mario Draghi”) to avoid role-play blurbs. After the first two steps, the dataset was reduced to ≈200,000\approx 200,000 personas.
3. (3)

   Duplicate removal: drop overly similar personas by computing vector embeddings222sentence-transformers/all-mpnet-base-v2. and discard those with cosine similarity scores ≥0.90\geq 0.90, ensuring a diverse and representative subset of domain experts. This step reduced the dataset to ≈43,000\approx 43,000 personas.
4. (4)

   Zero-shot relevance rating: prompt an LLM (gpt-4o-mini) to evaluate each persona based on three independent binary criteria: EU-centrality, neutrality, and monetary policy depth (see Appendix A for the full prompt). Keep only those personas that satisfy all three (i.e., scorepi=3\textit{score}\_{p\_{i}}=3). For increased robustness, we run the evaluation three times with temperature T = 1 and apply majority voting to determine the final decision. To validate the model’s reliability, we randomly sampled 50 personas and had two human annotators rate them manually. Cohen’s kappa scores between human ratings and GPT ratings ranged from 0.610.61 to 0.810.81 across the three criteria, indicating substantial agreement and confirming that the model selections are consistent with human judgment.

Given the size of the starting dataset, a multi-step pipeline is necessary to exclude candidate prompts that would pass the initial keyword-based screening but are ultimately unsuitable for our study. This strategy yields a candidate pool P⋆P^{\star} containing 2368 biographies, representing a highly selective filter that retains approximately six personas per million from the initial dataset. Appendix B provides examples of economics-related persona descriptions from the PersonaHub dataset, illustrating how personas were evaluated and selected according to EU-centrality, neutrality, and monetary policy expertise.

### 3.2. ECB Survey of Professional Forecasters

The European Central Bank’s  Survey of Professional Forecasters (SPF) is a quarterly survey that collects forecasts from a panel of experts on key euro area macroeconomic indicators. These include HICP (Harmonised Index of Consumer Prices) inflation, real GDP growth, and the unemployment rate.
The survey covers multiple forecasting horizons: the current calendar year, the next year, two years ahead, rolling horizons, and a five-year outlook. Respondents provide both point forecasts and probability distributions.
For this study, we consider a total of 50 SPF rounds from 2013Q1 to 2025Q2 and only focus on four of the macroeconomic variables tracked by the survey (see Table [1](https://arxiv.org/html/2511.02458v1#S1.T1 "Table 1 ‣ 1. Introduction ‣ Prompting for Policy: Forecasting Macroeconomic Scenarios with Synthetic LLM Personas") for an overview of the dataset).

Table 3. Intra-panel dispersion comparison between AI persona-based and human forecasters. Values represent the median dispersion, measured with standard deviation (SD) and inter-quartile range (IQR), across all survey rounds. AI forecasts consistently exhibit substantially lower dispersion than human forecasters across all variables and horizons, while human forecasters display broader disagreement patterns typical of professional survey panels.

(a) HICP and HICPX

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Variable | Horizon | SD | | IQR | |
|  |  | AI | Human | AI | Human |
| HICP | CY | 0.030 | 0.164 | 0.000 | 0.200 |
|  | CY+1 | 0.041 | 0.243 | 0.000 | 0.300 |
|  | CY+2 | 0.039 | 0.255 | 0.000 | 0.270 |
|  | LT | 0.009 | 0.210 | 0.000 | 0.215 |
| HICPX | CY | 0.045 | 0.170 | 0.006 | 0.200 |
|  | CY+1 | 0.045 | 0.242 | 0.000 | 0.275 |
|  | CY+2 | 0.040 | 0.253 | 0.025 | 0.300 |
|  | LT | 0.012 | 0.257 | 0.000 | 0.285 |

(b) rGDP and UNR

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Variable | Horizon | SD | | IQR | |
|  |  | AI | Human | AI | Human |
| rGDP | CY | 0.040 | 0.183 | 0.000 | 0.200 |
|  | CY+1 | 0.048 | 0.257 | 0.000 | 0.300 |
|  | CY+2 | 0.042 | 0.262 | 0.000 | 0.300 |
|  | LT | 0.018 | 0.300 | 0.000 | 0.331 |
| UNR | CY | 0.047 | 0.194 | 0.050 | 0.177 |
|  | CY+1 | 0.046 | 0.296 | 0.000 | 0.300 |
|  | CY+2 | 0.043 | 0.417 | 0.000 | 0.419 |
|  | LT | 0.024 | 0.582 | 0.000 | 0.700 |

#### Training data leakage

When trying to simulate responses to past events, such as past inflation, it is essential to consider potential data leakage issues which could lead to the ”memorization problem” (Lopez-Lira et al., [2025](https://arxiv.org/html/2511.02458v1#bib.bib15); Ludwig et al., [2025](https://arxiv.org/html/2511.02458v1#bib.bib16)). We build an out-of-sample training set including SPF rounds from 2024-Q1 to 2025-Q2. This time period contains six editions of the ECB Survey of Professional Forecasters. These surveys occur after the training cutoff date for the gpt-4o model333Specifically, we prompt gpt-4o-2024-11-20., which is the object of this study (OpenAI, [2024](https://arxiv.org/html/2511.02458v1#bib.bib17)), ensuring the absence of data leakage.

### 3.3. Prompt architecture

The central element of each LLM prompt in this study is the persona description (pip\_{i}), which we evaluate for its impact on task performance. In addition to the persona, each prompt includes a set of standardized components necessary to perform the two experimental tasks. For each experimental call, the LLM receives:

* •

  System rules: date anchoring (TsT\_{s}), instructions for output formatting.
* •

  Persona blurb pi∈P⋆p\_{i}\in P^{\star}, unedited except for the controlled experiment settings—see below.
* •

  Monetary policy context: the full text of the latest ECB press release at time TsT\_{s}, plus a macro snapshot
    
  (πHICP,g​d​pnow,…)(\pi^{\text{HICP}},\;gdp^{\text{now}},\;\dots).
* •

  Task instruction:

  “Provide your forecasts for euro area HICP inflation, real GDP growth, and unemployment rate for the current quarter (t) the following time horizons t+1, t+2, t+3, t+4 (…) Format your response as numerical values: ’HICP (t): X.X%, HICP (t+1): X.X%, …’ etc.”.

To isolate the effect of the persona selection on performance, we test two variations of the persona blurb: (i) raw text: unedited, full pip\_{i}; (ii) empty persona: the persona description block is omitted, providing only the monetary policy context and the task instructions.
An example of the full prompt can be found in Appendix C.

![Refer to caption](figures/F1A-lineplots/img/hicp_t0.png)

![Refer to caption](figures/F1A-lineplots/img/hicpx_t0.png)

![Refer to caption](figures/F1A-lineplots/img/rgdp_t0.png)

![Refer to caption](figures/F1A-lineplots/img/unr_t0.png)

Figure 3. Comparison of AI persona-based and human forecasts for current-year horizon across four ECB-SPF variables (2013-2025): (a) HICP inflation, (b) HICP core inflation, (c) Real GDP growth, and (d) Unemployment rate. Gray shaded regions indicate out-of-sample evaluation period. AI-generated median forecasts often, but not always, match human forecasts; this occurs both in the in-sample and out-of-sample surveys.††: AI vs human forecasts for key macro variables

### 3.4. Scoring metrics

Evaluation is carried out *match-by-match*, where a *match* is the unique
combination of survey round rr, macro variable
v∈{HICP,​HICPX,​rGDP,​UNR}v\in\{\text{HICP,}\allowbreak\ \text{HICPX,}\allowbreak\ \text{rGDP,}\allowbreak\ \text{UNR}\}, and forecast horizon
h∈{t0, t1, t2, lt}h\in\{\text{t0, t1, t2, lt}\}.
For each match we collapse the ∼\sim2 000 persona completions of a given
LLM to a single forecast—its cross-sectional *median*—and compare it
with the published SPF-panel median. With the first real-time annual average
that becomes available after the reference year closes, we form the absolute errors

|  |  |  |
| --- | --- | --- |
|  | er​v​hAI=|y^r​v​hAI−yr​v​h|,er​v​hH=|y^r​v​hSPF−yr​v​h|.e^{\text{AI}}\_{rvh}=|\hat{y}^{\text{AI}}\_{rvh}-y\_{rvh}|,\qquad e^{\text{H}}\_{rvh}=|\hat{y}^{\text{SPF}}\_{rvh}-y\_{rvh}|. |  |

#### Point accuracy.

For each variable and horizon, we measure forecast accuracy against the realized yearly data with the mean-absolute error (MAE)

|  |  |  |
| --- | --- | --- |
|  | MAEv​hpanel=1nv​h​∑r=1nv​her​v​hpanel,\text{MAE}^{\text{panel}}\_{vh}=\frac{1}{n\_{vh}}\sum\_{r=1}^{n\_{vh}}e^{\text{panel}}\_{rvh}, |  |

with nv​hn\_{vh} being the number of available rounds. The score is reported in Table [4](https://arxiv.org/html/2511.02458v1#S3.T4 "Table 4 ‣ Relative performance (win–share). ‣ 3.4. Scoring metrics ‣ 3. Data and experimental setup ‣ Prompting for Policy: Forecasting Macroeconomic Scenarios with Synthetic LLM Personas"). The lower of the two numbers is
bold-faced.

#### Panel disagreement.

For each round we measure cross-sectional dispersion with the
inter-quartile range IQRr​v​h=q75​(y^∙r​v​h)−q25​(y^∙r​v​h)\text{IQR}\_{rvh}=q\_{75}(\hat{y}\_{\bullet rvh})-q\_{25}(\hat{y}\_{\bullet rvh}), computed separately for personas and for human respondents. Table
[3](https://arxiv.org/html/2511.02458v1#S3.T3 "Table 3 ‣ 3.2. ECB Survey of Professional Forecasters ‣ 3. Data and experimental setup ‣ Prompting for Policy: Forecasting Macroeconomic Scenarios with Synthetic LLM Personas") reports the *median* IQR and variance across rounds.

#### Relative performance (win–share).

For every match, we record
winr​v​h=𝟏​{er​v​hAI<er​v​hH},\mathrm{win}\_{rvh}=\mathbf{1}\!\{e^{\mathrm{AI}}\_{rvh}<e^{\mathrm{H}}\_{rvh}\},
so that win=1\mathrm{win}=1 denotes an AI victory over the SPF median.
Let wv​h=∑rwinr​v​hw\_{vh}=\sum\_{r}\mathrm{win}\_{rvh} and
nv​hn\_{vh} be the number of matches for variable vv and horizon hh.
The *win-share*

|  |  |  |
| --- | --- | --- |
|  | w¯v​h=wv​h/nv​h\bar{w}\_{vh}=w\_{vh}/n\_{vh} |  |

is reported alongside two p-values that address distinct questions:

* •

  One-tailed (H0:Pr⁡(win)=0.5H\_{0}\!:\Pr(\mathrm{win})=0.5 vs. HA:Pr⁡(win)>0.5H\_{A}\!:\Pr(\mathrm{win})>0.5).
    
  Answers “is the AI panel *strictly better* than humans?”.
* •

  Two-tailed tests the symmetric alternative
  HA:Pr⁡(win)≠0.5H\_{A}\!:\Pr(\mathrm{win})\neq 0.5 and answers
  “is there *any* systematic difference in accuracy?”.

The same procedure is applied both to the *panel-median* AI forecast and
to every *individual persona*:

1. (i)

   In-sample rounds (2013​Q​12013\text{Q}1–2023​Q​42023\text{Q}4;
   up to nv​h=44n\_{vh}=44).
   We approximate the null distribution by Monte-Carlo:
   N=10,000N=10{,}000 artificial panels
   Wj∗∼Binom​(nv​h,0.5)W\_{j}^{\*}\sim\mathrm{Binom}(n\_{vh},0.5).

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   | (1) |  | pv​h(1)\displaystyle p^{(1)}\_{vh} | =N−1​∑j𝟏​{Wj∗≥wv​h},\displaystyle=N^{-1}\sum\_{j}\mathbf{1}\{W^{\*}\_{j}\geq w\_{vh}\}, |  |
   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   | (2) |  | pv​h(2)\displaystyle p^{(2)}\_{vh} | =2​min⁡(pv​h(1),N−1​∑j𝟏​{Wj∗≤wv​h}).\displaystyle=2\,\min\left(p^{(1)}\_{vh},N^{-1}\sum\_{j}\mathbf{1}\{W^{\*}\_{j}\leq w\_{vh}\}\right). |  |

   With N=10,000N=10{,}000 the Monte-Carlo error never exceeds 0.005.
2. (ii)

   Out-of-sample rounds (2024​Q​12024\text{Q}1–2025​Q​22025\text{Q}2;
   nv​h≤6n\_{vh}\leq 6).
   We use the exact binomial:

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   | (3) |  | pv​h(1)\displaystyle p^{(1)}\_{vh} | =Pr⁡{W≥wv​h},\displaystyle=\Pr\{W\geq w\_{vh}\}, |  |
   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   | (4) |  | pv​h(2)\displaystyle p^{(2)}\_{vh} | =2​min⁡{Pr⁡(W≥wv​h),Pr⁡(W≤wv​h)},\displaystyle=2\,\min\{\Pr(W\geq w\_{vh}),\Pr(W\leq w\_{vh})\}, |  |

   where W∼Binom​(nv​h,0.5)W\sim\mathrm{Binom}(n\_{vh},0.5).

Stars in every table refer to the *one-tailed* p-value and mark
p∗≤0.10{}^{\*}\,p\leq 0.10, p∗∗≤0.05{}^{\*\*}\,p\leq 0.05, p∗⁣∗∗≤0.01{}^{\*\*\*}\,p\leq 0.01.

![Refer to caption](figures/ks_distribution.png)


Figure 4. Persona prompting yields statistically indistinguishable error distributions. Kernel density estimates of absolute forecast errors for GPT-4o with persona descriptions (blue) versus baseline prompts without personas (orange) across all variable-horizon-round combinations. The near-perfect overlap supports our null hypothesis (t=−1.02t=-1.02, p=0.31p=0.31; Kolmogorov-Smirnov D=0.05D=0.05, p=0.28p=0.28).



![Refer to caption](figures/F4A-ridgeplots/hicp_t0_ridge.png)


(a) HICP inflation, Current year

![Refer to caption](figures/F4A-ridgeplots/hicp_t2_ridge.png)


(b) HICP inflation, Two years ahead

![Refer to caption](figures/F4A-ridgeplots/rgdp_t0_ridge.png)


(c) Real GDP growth, Current year

![Refer to caption](figures/F4A-ridgeplots/rgdp_t2_ridge.png)


(d) Real GDP growth, Two years ahead

Figure 5. Distribution of forecast errors by variable and horizon. Each panel shows kernel density estimates of errors for AI forecasts (blue) and human SPF forecasts (orange) across selected survey rounds. Top row compares HICP inflation errors at current-year (t0) and two-years (t2) horizons. Bottom row shows the same comparison for real GDP growth. AI forecasts consistently exhibit lower dispersion and more concentrated error distributions than human forecasters across both inflation measures and forecast horizons.††: Distribution of AI vs human forecast errors




Table 4. Forecast accuracy (MAE) comparing AI persona-based forecasts (median of 2,368 personas) versus human SPF medians across 50 ECB-SPF rounds (2013-2025). In-sample: 2013-2023, out-of-sample: 2024-2025. Bold indicates better performance. All errors in percentage points.

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | In-sample | | | | | | | | Out-of-sample | | | |
| Horizon | CY | | CY+1 | | CY+2 | | Long-term | | CY | | CY+1 | |
|  | AI | Human | AI | Human | AI | Human | AI | Human | AI | Human | AI | Human |
| HICP | 0.20 | 0.19 | 0.95 | 1.00 | 1.02 | 1.03 | 0.75 | 0.74 | 0.10 | 0.01 | 0.13 | 0.19 |
| HICPX | 0.10 | 0.10 | 0.50 | 0.50 | 0.70 | 0.75 | 1.30 | 1.30 | 0.25 | 0.30 | 0.50 | 0.50 |
| rGDP | 0.50 | 0.50 | 0.50 | 0.50 | 0.60 | 0.90 | 0.85 | 0.85 | 0.17 | 0.20 | 0.20 | 0.20 |
| UNR | 0.20 | 0.10 | 0.47 | 0.42 | 0.70 | 0.70 | 1.00 | 1.00 | 0.05 | 0.15 | 0.05 | 0.02 |




Table 5. Win share of SPF and AI-generated forecasts (%). Win shares calculated as percentage of forecasting rounds where AI (or human) median strictly outperformed the other. Remaining percentage represents ties. ∗⁣∗⁣∗\ast\!\ast\!\ast p≤0.01p\leq 0.01

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Horizon | CY | | | CY+1 | | | CY+2 | | | Long-term | | |
|  | AI wins | Human wins | P-val | AI wins | Human wins | P-val | AI wins | Human wins | P-val | AI wins | Human wins | P-val |
| In-sample | | | | | | | | | | | | |
| HICP | 29 | 28 | ∗⁣∗⁣∗\ast\!\ast\!\ast | 30 | 31 | ∗⁣∗⁣∗\ast\!\ast\!\ast | 31 | 26 | ∗⁣∗⁣∗\ast\!\ast\!\ast | 5 | 11 | ∗⁣∗⁣∗\ast\!\ast\!\ast |
| HICPX | 31 | 20 | ∗⁣∗⁣∗\ast\!\ast\!\ast | 30 | 17 | ∗⁣∗⁣∗\ast\!\ast\!\ast | 26 | 13 | ∗⁣∗⁣∗\ast\!\ast\!\ast | 1 | 5 | ∗⁣∗⁣∗\ast\!\ast\!\ast |
| rGDP | 20 | 30 | ∗⁣∗⁣∗\ast\!\ast\!\ast | 16 | 34 | ∗⁣∗⁣∗\ast\!\ast\!\ast | 26 | 28 | ∗⁣∗⁣∗\ast\!\ast\!\ast | 17 | 9 | ∗⁣∗⁣∗\ast\!\ast\!\ast |
| UNR | 13 | 32 | ∗⁣∗⁣∗\ast\!\ast\!\ast | 19 | 17 | ∗⁣∗⁣∗\ast\!\ast\!\ast | 23 | 15 | ∗⁣∗⁣∗\ast\!\ast\!\ast | 14 | 9 | ∗⁣∗⁣∗\ast\!\ast\!\ast |
| Out-of-sample | | | | | | | | | | | | |
| HICP | 28 | 68 | ∗⁣∗⁣∗\ast\!\ast\!\ast | 70 | 25 | ∗⁣∗⁣∗\ast\!\ast\!\ast |  |  |  |  |  |  |
| HICPX | 32 | 40 | ∗⁣∗⁣∗\ast\!\ast\!\ast | 25 | 0 | ∗⁣∗⁣∗\ast\!\ast\!\ast |  |  |  |  |  |  |
| rGDP | 53 | 25 | ∗⁣∗⁣∗\ast\!\ast\!\ast | 10 | 50 | ∗⁣∗⁣∗\ast\!\ast\!\ast |  |  |  |  |  |  |
| UNR | 47 | 37 | ∗⁣∗⁣∗\ast\!\ast\!\ast | 3 | 40 | ∗⁣∗⁣∗\ast\!\ast\!\ast |  |  |  |  |  |  |

## 4. Results

We report results obtained with gpt-4o444Preliminary experiments using gpt-4o-mini and o3-mini showed qualitatively similar behavior. using temperature T = 1 for stochasticity. For out-of-sample survey rounds (2024Q1 to 2025Q2), we report accuracy and win-share results only for horizons where realized data is available: current year (CY) and next year (CY+1). For the HICPX variables, only 34 rounds are available as it was only introduced to the survey in 2016Q4.

### 4.1. Persona ablation effect

Our primary methodological contribution examines whether detailed persona descriptions improve forecasting accuracy.
We conduct a controlled ablation experiment comparing the results of our original prompt against 100 baselines in which we remove the persona description from the prompt. This results in a total of 5,000 forecasts which we can compare to the persona-enhanced ones.
The results show no statistically significant difference in forecasting performance. A paired t-test on match-level median absolute errors yields a mean difference of 0.01 percentage points (personas minus no-personas), with t=−1.02t=-1.02, p=0.31p=0.31. This finding is corroborated by a size-matched Kolmogorov-Smirnov test (D=0.05D=0.05, p=0.28p=0.28) showing that error distributions are statistically indistinguishable (see Figure [4](https://arxiv.org/html/2511.02458v1#S3.F4 "Figure 4 ‣ Relative performance (win–share). ‣ 3.4. Scoring metrics ‣ 3. Data and experimental setup ‣ Prompting for Policy: Forecasting Macroeconomic Scenarios with Synthetic LLM Personas")).
This null result has significant practical implications: sophisticated persona engineering provides no measurable forecasting advantage and can be omitted to reduce computational costs without sacrificing accuracy. The finding suggests that model performance depends primarily on data quality and task framing rather than prompt elaboration.

### 4.2. Panel disagreement

The dispersion of forecasts within each panel reveals a significant difference between the AI and human panels of forecasters, as shown in Table [3](https://arxiv.org/html/2511.02458v1#S3.T3 "Table 3 ‣ 3.2. ECB Survey of Professional Forecasters ‣ 3. Data and experimental setup ‣ Prompting for Policy: Forecasting Macroeconomic Scenarios with Synthetic LLM Personas"). AI personas exhibit near-zero disagreement, with median inter-quantile ranges (IQRs) mostly below 0.001 percentage points across all variables and horizons, roughly two orders of magnitude lower than human forecasters. Human forecasters, display substantially higher dispersion, with higher median IQRs ranging from 0.17 percentage points (UNR current-year) to slightly higher values at longer time horizons. The disparity is equally pronounced when measured by standard deviation, with AI personas exhibiting roughly one order of magnitude less variation than human forecasters across all variables and horizons. Both dispersion measures confirm that despite the variety of persona prompts, the model converges on mostly homogeneous forecasts, suggesting limited sensitivity to prompt variations in this task domain.

### 4.3. Point forecast accuracy

The mean absolute error results, reported in Table [4](https://arxiv.org/html/2511.02458v1#S3.T4 "Table 4 ‣ Relative performance (win–share). ‣ 3.4. Scoring metrics ‣ 3. Data and experimental setup ‣ Prompting for Policy: Forecasting Macroeconomic Scenarios with Synthetic LLM Personas"), show that AI and human forecasters often perform at remarkably similar levels, with identical errors observed in seven of sixteen in-sample comparisons and numerous cases where differences are minimal (within 0.05-0.10 percentage points). The largest performance gaps emerge in specific variable-horizon combinations: AI substantially outperforms humans for GDP growth at the CY+2 horizon (0.60 vs 0.90) and unemployment at current-year out-of-sample forecasts (0.05 vs 0.15), while humans show clear advantages for unemployment at current-year in-sample (0.10 vs 0.20) and HICP current-year out-of-sample (0.01 vs 0.10). The transition from in-sample to out-of-sample periods shows no systematic performance degradation. Despite the model forecasting economic conditions entirely absent from its training data (October 2023 cutoff), accuracy levels remain broadly comparable to the in-sample period, suggesting the model effectively utilizes the real-time economic context provided in prompts rather than relying purely on memorized patterns.

### 4.4. Win-share analysis

In addition to evaluating point accuracy, we compute win-share scores to compare AI and human performance net of ties. The aggregated results are shown in Table [5](https://arxiv.org/html/2511.02458v1#S3.T5 "Table 5 ‣ Relative performance (win–share). ‣ 3.4. Scoring metrics ‣ 3. Data and experimental setup ‣ Prompting for Policy: Forecasting Macroeconomic Scenarios with Synthetic LLM Personas"), both for in-sample and out-of-sample rounds. Appendix D additionally reports the win shares for each survey round by horizon and variable.
The results demonstrate statistically significant yet practically modest differences in forecasting accuracy, with performance patterns varying systematically across variables and horizons. Despite uniform statistical significance at the 1% level, many win rate differentials are relatively narrow—particularly for inflation forecasts where margins often fall within 1-5 percentage points. The data reveal variable-specific comparative advantages: AI consistently outperforms on core inflation (HICPX) across most horizons, while humans maintain advantages in short-term GDP and unemployment forecasting that gradually erode at longer horizons. The out-of-sample results show more unstable results, with some outcome reversals compared to the in-sample. The limited out-of-sample observations (N=4-6) make it difficult to determine whether these reversals reflect genuine performance differences, structural breaks in the post-2021 period, or simply small-sample volatility.

## 5. Future work

Having established that persona descriptions are expendable, future work should systematically ablate other prompt components—ECB policy communications, past SPF medians, and real-time macro data—to identify which contextual information genuinely drives forecasting performance versus merely increasing token costs.
Several other extensions merit investigation. First, evaluating density forecasts—which are included in the ECB SPF—rather than just point estimates would test whether LLMs can meaningfully quantify uncertainty. Second, alternative prompting strategies beyond personas, such as explicit chain-of-thought reasoning or adversarial perspectives, may prove more effective at generating forecast diversity. Finally, extending the out-of-sample evaluation beyond our limited six rounds would provide more robust evidence of generalization.

## 6. Conclusion

We present the first systematic replication of the ECB Survey of Professional Forecasters using LLMs, evaluating over 2,000 synthetic personas extracted from the PersonaHub corpus across 50 quarterly rounds.
Our controlled ablation experiment reveals that adding these descriptions to the prompt provides no measurable forecasting advantage, with statistical tests showing no significant difference between persona-enhanced and baseline approaches. However, we find that LLMs can achieve competitive accuracy with human forecasters, even on out-of-sample data from 2024-2025 that was entirely absent from model training.
These results have practical implications for AI-assisted forecasting systems. Rather than investing computational resources in elaborate persona engineering, practitioners should focus on robust data integration and model improvements. Our findings also reveal behavioral differences between AI and human forecasting panels: despite diverse prompting, LLMs exhibit very low dispersion and consensus-seeking behavior, in contrast with the heterogeneity observed in human expert panels.
Future research should explore density forecasting capabilities and scenario coherence across multiple variables, while investigating whether alternative prompt engineering approaches beyond persona descriptions can enhance LLM forecasting performance in economic applications.

## References

* (1)
* Angel (2003)

  Juan Angel, García. 2003.
  *An introduction to the ECB’s survey of professional forecasters*.
  Occasional Paper Series 8. European Central Bank.

  <https://EconPapers.repec.org/RePEc:ecb:ecbops:20038>
* Argyle et al. (2023)

  Lisa P Argyle, Ethan C Busby, Nancy Fulda, Joshua R Gubler, Christopher Rytting, and David Wingate. 2023.
  Out of one, many: Using language models to simulate human samples.
  *Political Analysis* 31, 3 (2023), 337–351.
* Bybee (2023)

  Leland Bybee. 2023.
  Surveying Generative AI’s Economic Expectations.
  [doi:10.48550/arXiv.2305.02823](https://doi.org/10.48550/arXiv.2305.02823)
  arXiv:2305.02823 [econ].
* Carriero et al. (2024)

  Andrea Carriero, Davide Pettenuzzo, and Shubhranshu Shekhar. 2024.
  Macroeconomic Forecasting with Large Language Models.
  *CoRR* (Jan. 2024).

  <https://openreview.net/forum?id=hNU5kFeo9r>
* Dominguez-Olmedo et al. (2024)

  Ricardo Dominguez-Olmedo, Moritz Hardt, and Celestine Mendler-Dünner. 2024.
  Questioning the Survey Responses of Large Language Models.

  <https://openreview.net/forum?id=Oo7dlLgqQX>
* Faria-e Castro and Leibovici (2024)

  Miguel Faria-e Castro and Fernando Leibovici. 2024.
  Artificial Intelligence and Inflation Forecasts.
  *Review* (2024).
  [doi:10.20955/r.2024.12](https://doi.org/10.20955/r.2024.12)
* Fell (2024)

  Michael J Fell. 2024.
  Energy social surveys replicated with Large Language Model agents.
  *Available at SSRN 4686345* (2024).
* Ge et al. (2024)

  Tao Ge, Xin Chan, Xiaoyang Wang, Dian Yu, Haitao Mi, and Dong Yu. 2024.
  Scaling Synthetic Data Creation with 1,000,000,000 Personas.
  [doi:10.48550/arXiv.2406.20094](https://doi.org/10.48550/arXiv.2406.20094)
  arXiv:2406.20094 [cs].
* Geng et al. (2024)

  Mingmeng Geng, Sihong He, and Roberto Trotta. 2024.
  Are large language models chameleons? An attempt to simulate social surveys.
  *arXiv preprint arXiv:2405.19323* (2024).
* Hansen et al. (2025)

  Anne Lundgaard Hansen, John J. Horton, Sophia Kazinnik, Daniela Puzzello, and Ali Zarifhonarvar. 2025.
  Simulating the Survey of Professional Forecasters.
  [doi:10.2139/ssrn.5066286](https://doi.org/10.2139/ssrn.5066286)
* Horton (2023)

  John J. Horton. 2023.
  Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?
  [doi:10.3386/w31122](https://doi.org/10.3386/w31122)
* Kong et al. (2024)

  Aobo Kong, Shiwan Zhao, Hao Chen, Qicheng Li, Yong Qin, Ruiqi Sun, Xin Zhou, Enzhi Wang, and Xiaohang Dong. 2024.
  Better Zero-Shot Reasoning with Role-Play Prompting. In *Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)*, Kevin Duh, Helena Gomez, and Steven Bethard (Eds.). Association for Computational Linguistics, Mexico City, Mexico, 4099–4113.
  [doi:10.18653/v1/2024.naacl-long.228](https://doi.org/10.18653/v1/2024.naacl-long.228)
* Korinek (2023)

  Anton Korinek. 2023.
  Language Models and Cognitive Automation for Economic Research.
  [doi:10.3386/w30957](https://doi.org/10.3386/w30957)
* Lopez-Lira et al. (2025)

  Alejandro Lopez-Lira, Yuehua Tang, and Mingyin Zhu. 2025.
  The Memorization Problem: Can We Trust LLMs’ Economic Forecasts?
  [doi:10.48550/arXiv.2504.14765](https://doi.org/10.48550/arXiv.2504.14765)
  arXiv:2504.14765 [q-fin].
* Ludwig et al. (2025)

  Jens Ludwig, Sendhil Mullainathan, and Ashesh Rambachan. 2025.
  *Large Language Models: An Applied Econometric Framework*.
  NBER Working Papers 33344. National Bureau of Economic Research, Inc.

  <https://ideas.repec.org/p/nbr/nberwo/33344.html>
* OpenAI (2024)

  OpenAI. 2024.
  GPT-4o Model Documentation.

  <https://platform.openai.com/docs/models/gpt-4o>
  Model released May 13, 2024. Knowledge cutoff: October 1, 2023.
* Sclar et al. (2024)

  Melanie Sclar, Yejin Choi, Yulia Tsvetkov, and Alane Suhr. 2024.
  Quantifying Language Models’ Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting. In *The Twelfth International Conference on Learning Representations*.

  <https://openreview.net/forum?id=RIu5lyNXjT>
* Tan et al. (2024)

  Mingtian Tan, Mike Merrill, Vinayak Gupta, Tim Althoff, and Tom Hartvigsen. 2024.
  Are language models actually useful for time series forecasting?
  *Advances in Neural Information Processing Systems* 37 (2024), 60162–60191.
* Zarifhonarvar (2024)

  Ali Zarifhonarvar. 2024.
  Evidence on Inflation Expectations Formation Using Large Language Models.
  [doi:10.2139/ssrn.4825076](https://doi.org/10.2139/ssrn.4825076)
  Place: Rochester, NY Type: SSRN Scholarly Paper.

## Appendix A Zero-shot Relevance Rating Prompt

This appendix presents the prompt used to evaluate personas according to three criteria: EU-centrality, neutrality, and monetary policy depth.

### A.1. System and Task Instructions

[⬇](data:text/plain;base64,WW91IGFyZSBhc3Nlc3NpbmcgZXhwZXJ0IHBlcnNvbmFzIGZvciB0aGVpciBzdWl0YWJpbGl0eSBpbiBldXJvLWFyZWEgbW9uZXRhcnktcG9saWN5IHJlc2VhcmNoLgpSZXR1cm4gb25lIEpTT04gb2JqZWN0IG9ubHktbm8gYWRkaXRpb25hbCB0ZXh0LgoKVEFTSwotIFJlYWQgdGhlIGJpb2dyYXBoeSBzdXBwbGllZCBieSB0aGUgdXNlci4KLSBFdmFsdWF0ZSBpdCBhZ2FpbnN0IHRoZSB0aHJlZSBwYXNzLWZhaWwgY3JpdGVyaWEgYmVsb3cuCi0gUHJvdmlkZSBhIGNvbmNpc2Ugb25lLXNlbnRlbmNlIHJlYXNvbiBmb3IgZWFjaCBkZWNpc2lvbi4=)

You are assessing expert personas for their suitability in euro-area monetary-policy research.

Return one JSON object only-no additional text.

TASK

- Read the biography supplied by the user.

- Evaluate it against the three pass-fail criteria below.

- Provide a concise one-sentence reason for each decision.

### A.2. Relevance Criteria

[⬇](data:text/plain;base64,Q1JJVEVSSUEKMS4gRXVyby1hcmVhIGNlbnRyYWxpdHkKICAgRmFpbDogRm9jdXMgaXMgbm9uLUVVIG9yIHB1cmVseSBnbG9iYWwgd2l0aCBubyBldXJvLWFyZWEgYW5jaG9yLgogICBQYXNzOiBUaGUgZXVybyBhcmVhIG9yIGFuIEVDQiBpbnN0aXR1dGlvbiBpcyBtZW50aW9uZWQKICAgICAgIC0gdGhpcyBpbmNsdWRlcyByZWZlcmVuY2VzIHRvIEVVIGNvdW50cmllcywgY2VudHJhbCBiYW5rcyBvciBFdXJvcGUgaW4gZ2VuZXJhbCwKICAgICAgIC0gcmVmZXJlbmNlcyB0byBvdGhlciBjb250ZXh0cyBhcmUgYWxsb3dlZCBhcyBsb25nIGFzIHRoZSBldXJvLWFyZWEgY29udGV4dCBpcyBtZW50aW9uZWQuCjIuIE1vbmV0YXJ5LXBvbGljeSBkZXB0aAogICBGYWlsOiBNb25ldGFyeSBwb2xpY3kgaXMgbm90IG1lbnRpb25lZCBhdCBhbGwsIG9yIG9ubHkgbWVudGlvbmVkIGluIHBhc3Npbmcgd2l0aCBub25lIG9mIHRoZSBhYm92ZSBzaWduYWxzIHByZXNlbnQuCiAgIFBhc3M6IFRoZSBiaW9ncmFwaHkgZW5nYWdlcyBzdWJzdGFudGl2ZWx5IHdpdGggbW9uZXRhcnkgcG9saWN5IGJ5IHNhdGlzZnlpbmcgYXQgbGVhc3Qgb25lIG9mOgogICAgICAgLSBuYW1lcyBhbiBvcGVyYXRpb25hbCB0b29sIChlLmcuLCBkZXBvc2l0IHJhdGUsIEFQUC9QRVBQLCBMU0FQKSwKICAgICAgICAtIGRpc2N1c3NlcyBhIHJlY29nbmlzZWQgcG9saWN5IHJ1bGUgb3IgZG9jdHJpbmUgKGUuZy4sIFRheWxvciBydWxlLCBtb25leS1ncm93dGggdGFyZ2V0aW5nLCBydWxlcyB2cy4gZGlzY3JldGlvbiksCiAgICAgICAtIGFuYWx5c2VzIGEgdHJhbnNtaXNzaW9uIGNoYW5uZWwgb3IgbWFjcm8gb3V0Y29tZSAoaW5mbGF0aW9uLCBvdXRwdXQsIGVtcGxveW1lbnQsIGV4Y2hhbmdlIHJhdGUsIGFzc2V0IHByaWNlcyksCiAgICAgICAtIHJlZmVyZW5jZXMgYW4gZW1waXJpY2FsIG1ldGhvZCB1c2VkIHRvIGV2YWx1YXRlIHBvbGljeSAoZXZlbnQgc3R1ZHksIFZBUiwgRFNHRSwgbmF0dXJhbCBleHBlcmltZW50KS4KMy4gTmV1dHJhbGl0eQogICAgRmFpbDogVGhlIGJpb2dyYXBoeSBleHByZXNzZXMgb3BpbmlvbiwgYWR2b2NhY3kgb3IgYmlhcy4gTG9vayBmb3I6CiAgICAgICAgLSBFbW90aXZlIG9yIHZhbHVlLWxhZGVuIHRlcm1zICgicmVja2xlc3MiLCAiZGFuZ2Vyb3VzIiwgInVuc3VzdGFpbmFibGUiKS4KICAgICAgICAtIEZyYW1pbmcgb2YgcGVyc29uYWwgYWR2b2NhY3kgb3IganVkZ21lbnQgKCJza2VwdGljYWwgb2YuLi4iLCAiYSBjcml0aWMgb2YuLi4iLCAib3B0aW1pc3RpYyBhYm91dC4uLiIpLgogICAgICAgIC0gQW55IGltcGxpY2l0IHN0YW5jZSB0aGF0IGdvZXMgYmV5b25kIGFuYWx5c2lzLgogICAgUGFzczogVG9uZSBpcyBkZXNjcmlwdGl2ZSwgYW5hbHl0aWNhbCwgb3IgZXhwbG9yYXRvcnksIHdpdGhvdXQgYW55IGp1ZGdtZW50LCBwcmVzY3JpcHRpb24sIG9yIHN0YW5jZS4=)

CRITERIA

1. Euro-area centrality

Fail: Focus is non-EU or purely global with no euro-area anchor.

Pass: The euro area or an ECB institution is mentioned

- this includes references to EU countries, central banks or Europe in general,

- references to other contexts are allowed as long as the euro-area context is mentioned.

2. Monetary-policy depth

Fail: Monetary policy is not mentioned at all, or only mentioned in passing with none of the above signals present.

Pass: The biography engages substantively with monetary policy by satisfying at least one of:

- names an operational tool (e.g., deposit rate, APP/PEPP, LSAP),

- discusses a recognised policy rule or doctrine (e.g., Taylor rule, money-growth targeting, rules vs. discretion),

- analyses a transmission channel or macro outcome (inflation, output, employment, exchange rate, asset prices),

- references an empirical method used to evaluate policy (event study, VAR, DSGE, natural experiment).

3. Neutrality

Fail: The biography expresses opinion, advocacy or bias. Look for:

- Emotive or value-laden terms ("reckless", "dangerous", "unsustainable").

- Framing of personal advocacy or judgment ("skeptical of...", "a critic of...", "optimistic about...").

- Any implicit stance that goes beyond analysis.

Pass: Tone is descriptive, analytical, or exploratory, without any judgment, prescription, or stance.

### A.3. Output Schema

[⬇](data:text/plain;base64,ewogICJldXJvX2FyZWFfY2VudHJhbGl0eSI6ICJwYXNzIiB8ICJmYWlsIiwKICAibW9uZXRhcnlfcG9saWN5X2RlcHRoIjogInBhc3MiIHwgImZhaWwiLAogICJuZXV0cmFsaXR5IjogInBhc3MiIHwgImZhaWwiLAogICJub3RlcyI6IHsKICAgICJldXJvX2FyZWFfY2VudHJhbGl0eSI6ICI8b25lLXNlbnRlbmNlIHJlYXNvbj4iLAogICAgIm1vbmV0YXJ5X3BvbGljeV9kZXB0aCI6ICI8b25lLXNlbnRlbmNlIHJlYXNvbj4iLAogICAgIm5ldXRyYWxpdHkiOiAgIjxvbmUtc2VudGVuY2UgcmVhc29uPiIKICB9Cn0=)

{

"euro\_area\_centrality": "pass" | "fail",

"monetary\_policy\_depth": "pass" | "fail",

"neutrality": "pass" | "fail",

"notes": {

"euro\_area\_centrality": "<one-sentence reason>",

"monetary\_policy\_depth": "<one-sentence reason>",

"neutrality": "<one-sentence reason>"

}

}

### A.4. User Biography

[⬇](data:text/plain;base64,VVNFUiBCSU9HUkFQSFkKCkEgcmVzZWFyY2hlciB3aG8gc3R1ZGllcyB0aGUgaW1wYWN0IG9mIHVuZW1wbG95bWVudCBvbiB0aW1lIGFsbG9jYXRpb24gYW5kIGl0cyBpbXBsaWNhdGlvbnMgZm9yIGhvdXNlaG9sZCBjb25zdW1wdGlvbiwgcGFydGljdWxhcmx5IGZvY3VzaW5nIG9uIHRoZSByb2xlIG9mIHVucGFpZCB3b3JrIGluIHRoZSBlY29ub215LiBUaGlzIGluZGl2aWR1YWwgaXMgbGlrZWx5IHRvIGJlIGludGVyZXN0ZWQgaW4gdW5kZXJzdGFuZGluZyBob3cgdGhlIEdyZWF0IFJlY2Vzc2lvbiBhZmZlY3RlZCBwZW9wbGUncyB0aW1lIGFsbG9jYXRpb24gcGF0dGVybnMgYW5kIHRoZSBwb3RlbnRpYWwgZWNvbm9taWMgY29zdHMgb2YgaW52b2x1bnRhcnkgdW5lbXBsb3ltZW50Lg==)

USER BIOGRAPHY

A researcher who studies the impact of unemployment on time allocation and its implications for household consumption, particularly focusing on the role of unpaid work in the economy. This individual is likely to be interested in understanding how the Great Recession affected people’s time allocation patterns and the potential economic costs of involuntary unemployment.

## Appendix B Persona Examples from PersonaHub Dataset

This appendix provides examples of the economics-related persona descriptions contained in the PersonaHub dataset, evaluated on the three dimensions relevant to our study: EU-centrality, neutrality, and monetary policy expertise. Only personas meeting all three criteria were retained for the experiments.

### B.1. Retained Persona Example

Financial Economist (EU-focused): A financial economist who specializes in the analysis of economic cycles and monetary policy. This persona is interested in areas such as the synchronisation of the euro area’s economic cycle with that of the US, and how this affects the implementation of monetary policies. They are also interested in the factors that contribute to the degree of synchronisation and how they differ between the euro area and the US. This persona meets our EU-centrality criterion through explicit focus on euro area dynamics, maintains neutrality by presenting balanced analytical perspectives, and demonstrates clear monetary policy expertise.

### B.2. Excluded Persona Examples

Global Economist (US-biased): A global economist with America Merrill Lynch, with expertise in inflation and deflation, particularly in the context of the U.S. and Europe. They are optimistic about the potential for economic growth but express caution about the risks of shocks that could trigger deflation. They are concerned about the risks of a European deflation, and the potential for a global financial crisis. This persona was excluded due to insufficient EU-centrality (primary focus on US markets) and non-neutral stance (explicit optimism bias).

Technology Skeptic (Non-expert): A technologist who is skeptical of the effectiveness of information technology in stimulating economic growth. This persona believes that technology must be implemented and funded in order to create economic growth. They also believe that the central bank’s role in manipulating financial markets is a major impediment to economic growth. This persona is interested in the impact of new technologies on economic growth and the role of savings in promoting capital formation. This persona was excluded for lacking EU-centrality, exhibiting strong ideological bias against central bank intervention, and having insufficient monetary policy expertise.ing economic growth. This persona believes that technology must be implemented and funded in order to create economic growth. They also believe that the central bank’s role in manipulating financial markets is a major impediment to economic growth. This persona is interested in the impact of new technologies on economic growth and the role of savings in promoting capital formation. This persona was excluded for lacking EU-centrality, exhibiting strong ideological bias against central bank intervention, and having insufficient monetary policy expertise.

## Appendix C Prompt

This appendix contains the complete prompt used to simulate responses to the European Central Bank’s Survey of Professional Forecasters (ECB-SPF).

### C.1. System Instructions and Persona Description

[⬇](data:text/plain;base64,U1lTVEVNOgpZb3UgYXJlIHBhcnRpY2lwYXRpbmcgaW4gdGhlIEV1cm9wZWFuIENlbnRyYWwgQmFuaydzIFN1cnZleSBvZiBQcm9mZXNzaW9uYWwgRm9yZWNhc3RlcnMgKEVDQi1TUEYpIGZvciByb3VuZDogMjAxM1ExLgpUb2RheSdzIGRhdGUgaXMgMTYvMDEvMjAxMy4KWW91IHdpbGwgYmUgYXNrZWQgdG8gcHJvdmlkZSBwb2ludCBmb3JlY2FzdHMgZm9yIGEgc2V0IG9mIGtleSBtYWNyb2Vjb25vbWljIGluZGljYXRvcnMgKGluZmxhdGlvbiwgY29yZSBpbmZsYXRpb24sIEdEUCBncm93dGggYW5kIHVuZW1wbG95bWVudCkgZm9yIHRoZSBldXJvIGFyZWEgYXQgZGlmZmVyZW50IHRpbWUgaG9yaXpvbnMuCgpZb3UgYXJlOiBBIHBvbGl0aWNhbCBlY29ub21pc3Qgd2hvIHNwZWNpYWxpemVzIGluIHRoZSBzdHVkeSBvZiBtYWNyb2Vjb25vbWljcyBhbmQgaW50ZXJuYXRpb25hbCB0cmFkZS4gVGhlaXIgcmVzZWFyY2ggaW50ZXJlc3RzIGluY2x1ZGUgdGhlIGltcGFjdCBvZiBtb25ldGFyeSBhbmQgZmlzY2FsIHBvbGljaWVzIG9uIGVjb25vbWljIGdyb3d0aCwgdGhlIGVmZmVjdHMgb2YgY3VycmVuY3kgZGV2YWx1YXRpb25zIG9uIHRyYWRlIGRlZmljaXRzLCBhbmQgdGhlIHJvbGUgb2YgaW50ZXJuYXRpb25hbCBjYXBpdGFsIGZsb3dzIGluIHNoYXBpbmcgZWNvbm9taWMgZGV2ZWxvcG1lbnQuIFRoZXkgYXJlIHBhcnRpY3VsYXJseSBpbnRlcmVzdGVkIGluIHRoZSBpbXBsaWNhdGlvbnMgb2YgdGhlIEV1cm96b25lIGZvciB0aGUgZWNvbm9taWVzIG9mIHRoZSBQSUlHUyBjb3VudHJpZXMsIHRoZSBlZmZlY3RzIG9mIGZpbmFuY2lhbCBjcmlzZXMgb24gZWNvbm9taWMgcmVjb3ZlcnksIGFuZCB0aGUgdXNlIG9mIG1vbmV0YXJ5IGFuZCBmaW5hbmNpYWwgcmVzdHJ1Y3R1cmluZyB0byBwcmV2ZW50IGRlZmF1bHQuIFRoZXkgaGF2ZSBleHBlcmllbmNlIGluIGFuYWx5emluZyB0aGUgaW1wYWN0cyBvZiB0cmFkZSBkZWZpY2l0cywgY3VycmVuY3kgZGV2YWx1YXRpb25zLCBhbmQgZmluYW5jaWFsIGNyaXNlcyBvbiBlY29ub21pYyBncm93dGggYW5kIGRldmVsb3BtZW50LCBhbmQgaGF2ZSBhIHN0cm9uZyBpbnRlcmVzdCBpbiB1bmRlcnN0YW5kaW5nIHRoZSBjb21wbGV4IGludGVycGxheSBiZXR3ZWVuIGRvbWVzdGljIGFuZCBpbnRlcm5hdGlvbmFsIGZhY3RvcnMgaW4gc2hhcGluZyBlY29ub21pYyBvdXRjb21lcy4=)

SYSTEM:

You are participating in the European Central Bank’s Survey of Professional Forecasters (ECB-SPF) for round: 2013Q1.

Today’s date is 16/01/2013.

You will be asked to provide point forecasts for a set of key macroeconomic indicators (inflation, core inflation, GDP growth and unemployment) for the euro area at different time horizons.

You are: A political economist who specializes in the study of macroeconomics and international trade. Their research interests include the impact of monetary and fiscal policies on economic growth, the effects of currency devaluations on trade deficits, and the role of international capital flows in shaping economic development. They are particularly interested in the implications of the Eurozone for the economies of the PIIGS countries, the effects of financial crises on economic recovery, and the use of monetary and financial restructuring to prevent default. They have experience in analyzing the impacts of trade deficits, currency devaluations, and financial crises on economic growth and development, and have a strong interest in understanding the complex interplay between domestic and international factors in shaping economic outcomes.

### C.2. Economic Context and Data

[⬇](data:text/plain;base64,RUNPTk9NSUMgQ09OVEVYVDoKLSBMYXRlc3QgcmVhbGl6ZWQgZGF0YToKVmFyaWFibGUgIFBlcmlvZCAgVmFsdWUKSElDUCAgICAgIDIwMTJEZWMgIDIuMjAKSElDUFggICAgIDIwMTJEZWMgIDEuNTAKVU5SICAgICAgIDIwMTJOb3YgIDEyLjAwClJHRFAgICAgICAyMDEyUTMgICAtMS4wMAoKLSBNZWRpYW4gZm9yZWNhc3RzIGZyb20gdGhlIHByZXZpb3VzIFNQRiByb3VuZDoKVmFyaWFibGUgIEhvcml6b24gIE1lZGlhbiBmb3JlY2FzdApISUNQICAgICAgMjAxMyAgICAgMS44MApISUNQICAgICAgMjAxNCAgICAgMS44MApISUNQICAgICAgMjAxNSAgICAgMS45MApISUNQICAgICAgMjAxNyAgICAgMi4wMApISUNQWCAgICAgMjAxMwpISUNQWCAgICAgMjAxNApISUNQWCAgICAgMjAxNQpISUNQWCAgICAgMjAxNwpVTlIgICAgICAgMjAxMyAgICAgMTIuMTAKVU5SICAgICAgIDIwMTQgICAgIDExLjkwClVOUiAgICAgICAyMDE1ICAgICAxMS40MApVTlIgICAgICAgMjAxNyAgICAgOS40MApSR0RQICAgICAgMjAxMyAgICAgLTAuMTAKUkdEUCAgICAgIDIwMTQgICAgIDEuMDIKUkdEUCAgICAgIDIwMTUgICAgIDEuNTAKUkdEUCAgICAgIDIwMTcgICAgIDEuNzAKCi0gRUNCIG1vbmV0YXJ5IHBvbGljeSBjb21tdW5pY2F0aW9uIGZyb20gdGhlIGxhdGVzdCBHb3Zlcm5pbmcgQ291bmNpbCBtZWV0aW5nIG9uIDIwMTMtMDEtMTA6CkxhZGllcyBhbmQgZ2VudGxlbWVuLCB0aGUgVmljZS1QcmVzaWRlbnQgYW5kIEkgYXJlIHZlcnkgcGxlYXNlZCB0byB3ZWxjb21lIHlvdSB0byBvdXIgcHJlc3MgY29uZmVyZW5jZS4KCkxldCBtZSB3aXNoIHlvdSBhbGwgYSBIYXBweSBOZXcgWWVhci4gV2Ugd2lsbCBub3cgcmVwb3J0IG9uIHRoZSBvdXRjb21lIG9mIHRvZGF5J3MgbWVldGluZyBvZiB0aGUgR292ZXJuaW5nIENvdW5jaWwuCgpCYXNlZCBvbiBvdXIgcmVndWxhciBlY29ub21pYyBhbmQgbW9uZXRhcnkgYW5hbHlzZXMsIHdlIGRlY2lkZWQgdG8ga2VlcCB0aGUga2V5IEVDQiBpbnRlcmVzdCByYXRlcyB1bmNoYW5nZWQuIEhJQ1AgaW5mbGF0aW9uIHJhdGVzIGhhdmUgZGVjbGluZWQgb3ZlciByZWNlbnQgbW9udGhzLCBhcyBhbnRpY2lwYXRlZCwgYW5kIGFyZSBleHBlY3RlZCB0byBmYWxsIGJlbG93IDIlIHRoaXMgeWVhci4gT3ZlciB0aGUgcG9saWN5LXJlbGV2YW50IGhvcml6b24sIGluZmxhdGlvbmFyeSBwcmVzc3VyZXMgc2hvdWxkIHJlbWFpbiBjb250YWluZWQuIFRoZSB1bmRlcmx5aW5nIHBhY2Ugb2YgbW9uZXRhcnkgZXhwYW5zaW9uIGNvbnRpbnVlcyB0byBiZSBzdWJkdWVkLiBJbmZsYXRpb24gZXhwZWN0YXRpb25zIGZvciB0aGUgZXVybyBhcmVhIHJlbWFpbiBmaXJtbHkgYW5jaG9yZWQgaW4gbGluZSB3aXRoIG91ciBhaW0gb2YgbWFpbnRhaW5pbmcgaW5mbGF0aW9uIHJhdGVzIGJlbG93LCBidXQgY2xvc2UgdG8sIDIlIG92ZXIgdGhlIG1lZGl1bSB0ZXJtLiBUaGUgZWNvbm9taWMgd2Vha25lc3MgaW4gdGhlIGV1cm8gYXJlYSBpcyBleHBlY3RlZCB0byBleHRlbmQgaW50byAyMDEzLiBJbiBwYXJ0aWN1bGFyLCBuZWNlc3NhcnkgYmFsYW5jZSBzaGVldCBhZGp1c3RtZW50cyBpbiBmaW5hbmNpYWwgYW5kIG5vbi1maW5hbmNpYWwgc2VjdG9ycyBhbmQgcGVyc2lzdGVudCB1bmNlcnRhaW50eSB3aWxsIGNvbnRpbnVlIHRvIHdlaWdoIG9uIGVjb25vbWljIGFjdGl2aXR5LiBMYXRlciBpbiAyMDEzIGVjb25vbWljIGFjdGl2aXR5IHNob3VsZCBncmFkdWFsbHkgcmVjb3Zlci4gSW4gcGFydGljdWxhciwgb3VyIGFjY29tbW9kYXRpdmUgbW9uZXRhcnkgcG9saWN5IHN0YW5jZSwgdG9nZXRoZXIgd2l0aCBzaWduaWZpY2FudGx5IGltcHJvdmVkIGZpbmFuY2lhbCBtYXJrZXQgY29uZmlkZW5jZSBhbmQgcmVkdWNlZCBmcmFnbWVudGF0aW9uLCBzaG91bGQgd29yayBpdHMgd2F5IHRocm91Z2ggdG8gdGhlIGVjb25vbXksIGFuZCBnbG9iYWwgZGVtYW5kIHNob3VsZCBzdHJlbmd0aGVuLiBJbiBvcmRlciB0byBzdXN0YWluIGNvbmZpZGVuY2UsIGl0IGlzIGVzc2VudGlhbCBmb3IgZ292ZXJubWVudHMgdG8gcmVkdWNlIGZ1cnRoZXIgYm90aCBmaXNjYWwgYW5kIHN0cnVjdHVyYWwgaW1iYWxhbmNlcyBhbmQgdG8gcHJvY2VlZCB3aXRoIGZpbmFuY2lhbCBzZWN0b3IgcmVzdHJ1Y3R1cmluZy4=)

ECONOMIC CONTEXT:

- Latest realized data:

Variable Period Value

HICP 2012Dec 2.20

HICPX 2012Dec 1.50

UNR 2012Nov 12.00

RGDP 2012Q3 -1.00

- Median forecasts from the previous SPF round:

Variable Horizon Median forecast

HICP 2013 1.80

HICP 2014 1.80

HICP 2015 1.90

HICP 2017 2.00

HICPX 2013

HICPX 2014

HICPX 2015

HICPX 2017

UNR 2013 12.10

UNR 2014 11.90

UNR 2015 11.40

UNR 2017 9.40

RGDP 2013 -0.10

RGDP 2014 1.02

RGDP 2015 1.50

RGDP 2017 1.70

- ECB monetary policy communication from the latest Governing Council meeting on 2013-01-10:

Ladies and gentlemen, the Vice-President and I are very pleased to welcome you to our press conference.

Let me wish you all a Happy New Year. We will now report on the outcome of today’s meeting of the Governing Council.

Based on our regular economic and monetary analyses, we decided to keep the key ECB interest rates unchanged. HICP inflation rates have declined over recent months, as anticipated, and are expected to fall below 2% this year. Over the policy-relevant horizon, inflationary pressures should remain contained. The underlying pace of monetary expansion continues to be subdued. Inflation expectations for the euro area remain firmly anchored in line with our aim of maintaining inflation rates below, but close to, 2% over the medium term. The economic weakness in the euro area is expected to extend into 2013. In particular, necessary balance sheet adjustments in financial and non-financial sectors and persistent uncertainty will continue to weigh on economic activity. Later in 2013 economic activity should gradually recover. In particular, our accommodative monetary policy stance, together with significantly improved financial market confidence and reduced fragmentation, should work its way through to the economy, and global demand should strengthen. In order to sustain confidence, it is essential for governments to reduce further both fiscal and structural imbalances and to proceed with financial sector restructuring.

[The complete ECB communication continues for several additional paragraphs and has been truncated here for space. The full text was included in the actual prompt.]

### C.3. Task Instructions and Output Requirements

[⬇](data:text/plain;base64,VEFTSzoKWW91IGFyZSBhc2tlZCB0byBwcm92aWRlIG9uZSAqKm51bWVyaWMgcG9pbnQgZm9yZWNhc3QqKiBmb3IgZWFjaCB0YXJnZXQgbWFjcm9lY29ub21pYyB2YXJpYWJsZSBsaXN0ZWQgYmVsb3csIGF0IG11bHRpcGxlIHRpbWUgaG9yaXpvbnMuIERvIG5vdCB1c2UgcmFuZ2VzIG9yIGNvbmZpZGVuY2UgaW50ZXJ2YWxzLgpBbGwgZm9yZWNhc3RzIHNob3VsZCBiZSBleHByZXNzZWQgaW4gcGVyY2VudCAoJSksIGRvIG5vdCBpbmNsdWRlIHVuaXRzIGluIHRoZSBhbnN3ZXIuCgpUQVJHRVRTOgpGb3IgZWFjaCBvZiB0aGUgZm9sbG93aW5nIHZhcmlhYmxlcywgcHJvdmlkZSBhIHBvaW50IGZvcmVjYXN0OgoKLSBISUNQOiBISUNQIGluZmxhdGlvbgotIEhJQ1BYOiBISUNQIGluZmxhdGlvbiBleGNsdWRpbmcgZm9vZCBhbmQgZW5lcmd5Ci0gUkdEUDogUmVhbCBHRFAgZ3Jvd3RoCi0gVU5SOiBVbmVtcGxveW1lbnQgcmF0ZQoKRWFjaCB2YXJpYWJsZSBzaG91bGQgYmUgZm9yZWNhc3QgYXQgdGhlIGZvbGxvd2luZyBob3Jpem9uczoKLSB0MDogY3VycmVudCBjYWxlbmRhciB5ZWFyICgyMDEzKQotIHQxOiBuZXh0IHllYXIgKDIwMTQpCi0gdDI6IHllYXIgYWZ0ZXIgbmV4dCAoMjAxNSkKLSBsdDogbG9uZy10ZXJtICgyMDE3KQoKT1VUUFVUIFNDSEVNQToKUmVzcG9uZCBzdHJpY3RseSBpbiB0aGUgZm9sbG93aW5nIEpTT04gZm9ybWF0Ogp7CiAgImZvcmVjYXN0cyI6IFsKICAgIHsKICAgICAgInZhcmlhYmxlIjogImhpY3AiLAogICAgICAiaG9yaXpvbiI6ICJ0MCIsCiAgICAgICJ2YWx1ZSI6ICI8PG51bWVyaWM+PiIKICAgIH0sCiAgICB7CiAgICAgICJ2YXJpYWJsZSI6ICJoaWNwIiwKICAgICAgImhvcml6b24iOiAidDEiLAogICAgICAidmFsdWUiOiAiPDxudW1lcmljPj4iCiAgICB9LAogICAgLi4uCiAgICB7CiAgICAgICJ2YXJpYWJsZSI6ICJ1bnIiLAogICAgICAiaG9yaXpvbiI6ICJsdCIsCiAgICAgICJ2YWx1ZSI6ICI8PG51bWVyaWM+PiIKICAgIH0KICBdCn0KClJlcGx5IG9ubHkgd2l0aCB0aGUgSlNPTiwgbm8gYWRkaXRpb25hbCB0ZXh0Lg==)

TASK:

You are asked to provide one \*\*numeric point forecast\*\* for each target macroeconomic variable listed below, at multiple time horizons. Do not use ranges or confidence intervals.

All forecasts should be expressed in percent (%), do not include units in the answer.

TARGETS:

For each of the following variables, provide a point forecast:

- HICP: HICP inflation

- HICPX: HICP inflation excluding food and energy

- RGDP: Real GDP growth

- UNR: Unemployment rate

Each variable should be forecast at the following horizons:

- t0: current calendar year (2013)

- t1: next year (2014)

- t2: year after next (2015)

- lt: long-term (2017)

OUTPUT SCHEMA:

Respond strictly in the following JSON format:

{

"forecasts": [

{

"variable": "hicp",

"horizon": "t0",

"value": "<<numeric>>"

},

{

"variable": "hicp",

"horizon": "t1",

"value": "<<numeric>>"

},

...

{

"variable": "unr",

"horizon": "lt",

"value": "<<numeric>>"

}

]

}

Reply only with the JSON, no additional text.

## Appendix D Win-share Analysis

This appendix presents heatmaps comparing the forecast accuracy of AI and human experts for each target variable (HICP, HICPX, rGDP, UNR) across different forecast horizons (t0, t1, t2, lt) and survey rounds. A win rate of 0% indicates that human forecasts strictly outperformed AI 100% of the time, while a win rate of 100% means AI forecasts were consistently better. Ties are excluded from the win share calculation. The figures reveal that, with some exceptions (for example, the HICP inflation rate between 2012 Q4 and 2015 Q1), AI does not consistently achieve higher win shares compared to human experts. Notably, for inflation forecasts over the long-term horizon, the results indicate that AI’s performance is not better than that of human forecasters, as AI’s win shares are nearly all 0%.

### D.1. HICP Inflation Rate

![Refer to caption](figures/heatmaps/complete_heatmap_hicp.png)


Figure 6. AI win share for HICP inflation rate forecasts across horizons and survey rounds.††: HICP heatmap: AI vs human forecasts

### D.2. HICP Core Inflation Rate

![Refer to caption](figures/heatmaps/complete_heatmap_hicpx.png)


Figure 7. AI win share for HICPX core inflation rate forecasts across horizons and survey rounds.††: HICPX heatmap: AI vs human forecasts

### D.3. Real GDP Rate

![Refer to caption](figures/heatmaps/complete_heatmap_rgdp.png)


Figure 8. AI win share for real GDP growth forecasts across horizons and survey rounds.††: Real GDP heatmap: AI vs human forecasts

### D.4. Unemployment Rate

![Refer to caption](figures/heatmaps/complete_heatmap_unr.png)


Figure 9. AI win share for unemployment rate forecasts across horizons and survey rounds.††: Unemployment heatmap: AI vs human forecasts