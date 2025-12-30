---
authors:
- Zuoyou Jiang
- Li Zhao
- Rui Sun
- Ruohan Sun
- Zhongjian Li
- Jing Li
- Daxin Jiang
- Zuo Bai
- Cheng Hua
doc_id: arxiv:2512.23515v1
family_id: arxiv:2512.23515
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Alpha-R1: Alpha Screening with LLM Reasoning via Reinforcement Learning'
url_abs: http://arxiv.org/abs/2512.23515v1
url_html: https://arxiv.org/html/2512.23515v1
venue: arXiv q-fin
version: 1
year: 2025
---


Zuoyou Jiang
Shanghai Jiao Tong UniversityShanghaiChina
[zuoyou.jiang@sjtu.edu.cn](mailto:zuoyou.jiang@sjtu.edu.cn)
, 
Li Zhao
StepFunShanghaiChina
[zhaoli@stepfun.com](mailto:zhaoli@stepfun.com)
, 
Rui Sun
StepFunShanghaiChina
[sunrui@stepfun.com](mailto:sunrui@stepfun.com)
, 
Ruohan Sun
Shanghai Jiao Tong UniversityShanghaiChina
[ruohan.sun@sjtu.edu.cn](mailto:ruohan.sun@sjtu.edu.cn)
, 
Zhongjian Li
Shanghai Jiao Tong UniversityShanghaiChina
[zhongjian.li@sjtu.edu.cn](mailto:zhongjian.li@sjtu.edu.cn)
, 
Jing Li
StepFunShanghaiChina
[futureli@stepfun.com](mailto:futureli@stepfun.com)
, 
Daxin Jiang
StepFunShanghaiChina
[djiang@stepfun.com](mailto:djiang@stepfun.com)
, 
Zuo Bai
FinStep, StepFunShanghaiChina
[baizuo@finstep.cn, stepfun.com](mailto:baizuo@finstep.cn,%20stepfun.com)
 and 
Cheng Hua
Shanghai Jiao Tong UniversityShanghaiChina
[cheng.hua@sjtu.edu.cn](mailto:cheng.hua@sjtu.edu.cn)

###### Abstract.

Signal decay and regime shifts pose recurring challenges for data-driven investment strategies in non-stationary markets. Conventional time-series and machine learning approaches, which rely primarily on historical correlations, often struggle to generalize when the economic environment changes. While large language models (LLMs) offer strong capabilities for processing unstructured information, their potential to support quantitative factor screening through explicit economic reasoning remains underexplored. Existing factor-based methods typically reduce alphas to numerical time series, overlooking the semantic rationale that determines when a factor is economically relevant.

We propose Alpha-R1, an 8B-parameter reasoning model trained via reinforcement learning for context-aware alpha screening. Alpha-R1 reasons over factor logic and real-time news to evaluate alpha relevance under changing market conditions, selectively activating or deactivating factors based on contextual consistency. Empirical results across multiple asset pools show that Alpha-R1 consistently outperforms benchmark strategies and exhibits improved robustness to alpha decay. The full implementation and resources are available at <https://github.com/FinStep-AI/Alpha-R1>.

Large Language Models, Reinforcement Learning, Alpha Screening, Quantitative Trading

## 1. Introduction

The paradigm of factor investing has remained a cornerstone of modern asset management since the seminal work of Fama and French (FAMA19933). Theoretical evolution, ranging from the foundational CAPM (sharpe1964capitalassetprices) to multi-factor models (carhart1997persistence), coupled with the exponential growth of market data, has culminated in the high-dimensional phenomenon known as the Factor Zoo (feng2020taming).

At the same time, advancements in natural language processing (NLP) have empowered the extraction of valuable sentiment signals from extensive unstructured data sources, such as news and financial reports (lopezlira2023chatgpt). The field has witnessed a paradigm shift from general-purpose architectures toward domain-specific foundation models. Notable examples, including BloombergGPT (wu2023bloomberggptlargelanguagemodel) and FinGPT (liu2023fingpt), have validated the effectiveness of pre-training and fine-tuning on financial datasets, often leveraging efficient adaptation methods like LoRA (hu2021loralowrankadaptationlarge). These specialized models have set new performance standards (xie2023pixiulargelanguagemodel), demonstrating superior capabilities in tasks such as sentiment analysis and named entity recognition compared to generalist models (zhang2023instructfingptfinancialsentimentanalysis; lu2023bbtfincomprehensiveconstructionchinese; zhang2023xuanyuan20largechinese).

However, a key gap remains in unifying these data streams. Traditional numerical indicators and textual signals are often treated as separate modalities, combined through static weighting schemes or heuristic rules rather than within a unified framework that captures their semantic interactions in dynamic decision-making. Recent advances in large language models (LLMs) have substantially expanded the scope of automated reasoning. NLP has shifted from task-specific supervision toward promptable, general-purpose systems that, augmented with chain-of-thought reasoning and reinforcement learning, can address increasingly complex cognitive tasks.

The integration of these systems into factor investing is far from mature. The financial domain is characterized by inherent non-stationarity, noise, and high dimensionality (feng2020taming; he2025reinforcement), necessitating adaptive reasoning to navigate uncertainty, such as assessing the relative merit of value versus momentum factors under shifting macroeconomic conditions. These demands stand in stark contrast to the deterministic nature of coding or mathematical benchmarks typically employed for LLMs (hendrycks2021measuringmassivemultitasklanguage). Although alternative methodologies like sparsity-based machine learning (e.g., Lasso) are available (freyberger2020dissecting), they frequently suffer from poor interpretability and instability during market regime changes. Conversely, general-purpose LLMs typically lack alignment with financial principles, making it difficult to produce verifiable justifications for factor selection or transparent decision traces (tatsat2025blackboxinterpretabilityllms).

Current research on LLMs in finance has largely focused on factor mining, namely the discovery of novel signals from textual or multimodal data. This line of work is closely related to open-domain question answering, where the primary goal is information extraction. A growing literature leverages the generative capabilities of LLMs for this purpose. For instance, cheng2024quantumfinance showed that GPT-4 can generate factors with high Sharpe ratios supported by economic rationales, while wang2024llmfactorextractingprofitablefactors proposed prompt-based extraction methods for profitable factors. To further operationalize factor generation, cao2025chainofalpha introduced Chain-of-Alpha, a dual-chain architecture that generates seed factors and iteratively refines them using backtesting feedback. Related frameworks, including Alpha-GPT (Wang2025AlphaGPT; yuan2024alphagpt) and R&D-Agent-Quant (li2025rdagentquant), explore human-in-the-loop and multi-agent systems to bridge hypothesis generation and code implementation. To address alpha decay, Tang2025AlphaAgentLA proposed regularization based on abstract syntax trees to encourage factor originality. More recently, kou-etal-2025-automate utilize LLMs to extract trading signals from multimodal data, including financial text and market information.

As factor generation capabilities improve, evaluation has emerged as a key bottleneck. To address this, Ding2025AlphaEval proposed AlphaEval, a five-dimensional framework that evaluates factors without backtesting. Nevertheless, a fundamental gap remains between broad factor mining and the path-dependent reasoning required for systematic factor screening. Recent efforts such as Trading-R1 (xiao2025tradingr1financialtradingllm), Fin-R1 (liu2025finr1largelanguagemodel), and FinO1 (qian2025fino1transferabilityreasoningenhancedllms) enhance reasoning capabilities in financial LLMs, yet factor screening decisions remain highly context-dependent and time-varying. A factor that performs well in an inflationary regime may become ineffective, or even harmful, during a recession.

To address these structural limitations, we propose Alpha-R1, a dynamic investment framework anchored by a specialized reasoning model trained via reinforcement learning. Distinct from generic LLM applications or purely agentic frameworks (hong2024metagptmetaprogrammingmultiagent; xiao2025tradingagentsmultiagentsllmfinancial), Alpha-R1 serves as the system’s cognitive core, designed to support the sequential reasoning required for dynamic factor screening. It inductively reasons over heterogeneous market information to assess the economic relevance of candidate factors and construct portfolios aligned with prevailing market conditions. In addition, Alpha-R1 attributes return sources in a structured manner, enabling transparent explanations of factor selection decisions. This design addresses both the opacity of traditional quantitative models and the static reasoning of existing financial LLMs, advancing regime-aware and interpretable portfolio construction.

Our primary contributions are as follows. First, we develop a practical investment framework that bridges static quantitative models and dynamic market environments. By synthesizing heterogeneous information, including macroeconomic indicators and news narratives, the framework enables regime-aware factor screening and dynamically adjusts portfolio exposure based on the semantic alignment between factor rationales and prevailing market conditions.

Second, we design a specialized reasoning core by adapting the reinforcement learning from human feedback (RLHF) paradigm to the financial domain. Instead of relying on subjective human preferences, we construct an objective reward signal based on realized market performance, such as volatility-adjusted returns. This design aligns the model’s reasoning process with realistic trading objectives and supports sequential decision-making under uncertainty.

Finally, we conduct extensive backtesting across multiple asset pools beyond standard market indices. The results show that Alpha-R1 consistently outperforms state-of-the-art benchmarks and traditional factor strategies, demonstrating robustness to alpha decay and the ability to deliver explainable, superior risk-adjusted performance across market regimes.

## 2. Related Work

### 2.1. LLMs in Quantitative Trading

#### 2.1.1. Financial Foundation Models and Adaptation

Before the advent of reasoning-centric approaches, the adaptation of LLMs to finance primarily focused on domain-specific pre-training and instruction tuning. BloombergGPT (wu2023bloomberggptlargelanguagemodel) established a benchmark by training on a massive mixed corpus of financial and general data. To democratize access, open-source efforts like FinGPT (liu2023fingpt) and Instruct-FinGPT (zhang2023instructfingptfinancialsentimentanalysis) utilized efficient fine-tuning techniques to adapt general-purpose models for financial tasks. Additionally, BBT-Fin (lu2023bbtfincomprehensiveconstructionchinese) and XuanYuan 2.0 (zhang2023xuanyuan20largechinese) have explored Chinese financial benchmarks, while PIXIU (xie2023pixiulargelanguagemodel) provided a comprehensive evaluation framework for these instruction-tuned models.

#### 2.1.2. LLMs for Alpha Factor Generation

The integration of LLMs has catalyzed a paradigm shift in quantitative trading, particularly within the domain of alpha factor mining, where models automate the discovery of novel, interpretable predictive signals. Contemporary research has evolved from simple signal generation to sophisticated agent-based frameworks. A prominent research trajectory focuses on mitigating alpha decay through iterative refinement. For instance, AlphaAgent (Tang2025AlphaAgentLA) introduces a framework that enforces factor originality and robustness using abstract syntax tree (AST) similarity measures. Complementing this, Chain-of-Alpha (cao2025chainofalpha) proposes a dual-chain architecture consisting of a factor generation chain and a factor optimization chain to iteratively refine candidate factors based on feedback from backtesting. Similarly, AlphaForge (Shi2024AlphaForgeAF) adopts a two-stage generative and predictive neural network to enhance the mining process. Beyond fully autonomous systems, recent work has also explored human-AI collaboration (Wang2025AlphaGPT; yuan2024alphagpt).

#### 2.1.3. LLM-based Quant Agents

Moving beyond the paradigm of discrete factor mining, the research frontier has expanded towards developing holistic, AI-driven agents capable of orchestrating the entire investment lifecycle. A primary research trajectory focuses on fine-tuning LLMs for direct return forecasting. Guo2024FineTuningLLM demonstrate that adapting models to unstructured data, such as news flow, substantially enhances stock selection capabilities, while also providing critical comparative insights into the efficacy of encoder-only (e.g., DeBERTa) versus decoder-only (e.g., Mistral) architectures.

To address the downstream complexities of execution and risk management, however, the field is increasingly pivoting towards multi-agent orchestration. kou-etal-2025-automate propose a hierarchical framework where LLMs function as specialized alpha generators, with distinct agents responsible for dynamic weight optimization. This architectural philosophy that segregates signal generation from risk control parallels the modular design of reinforcement learning systems such as QF-FRL (cheng2024quantumfinance) and general multi-agent frameworks like MetaGPT (hong2024metagptmetaprogrammingmultiagent). This trend culminates in comprehensive ecosystems like TradingGPT (li2023tradinggptmultiagentlayeredmemory), FinMem (li2024finmem), and FinAgent (Cao2025DeepLearningLLM; zhang2024multimodalfoundationagentfinancial), which employ multimodal perception (kou-etal-2025-automate) and collaborative agent workflows (e.g., TradingAgents (xiao2025tradingagentsmultiagentsllmfinancial)) to autonomously navigate the full spectrum of trading activities. Additionally, Koa\_2024 integrated self-reflection mechanisms to refine predictions, addressing hallucination issues common in these complex agents (ji2023mitigatinghallucinationlargelanguage).

### 2.2. Methods for Screening Alpha Factors

#### 2.2.1. Machine Learning in Regularized and Sparsity-Driven Selection

The most direct machine learning approach to addressing the Factor Zoo is the application of sparsity-inducing regularization, such as Lasso (tibshirani1996lasso). This method imposes sparsity by adding a penalty term, effectively shrinking the coefficients of irrelevant or redundant factors to zero. Building on this principle, mai2024factorinvestment adopt the Lasso method to address severe multicollinearity among feature indicators in the A-share market, finding that it yields superior stability and predictive accuracy compared to traditional unregularized linear methods.

#### 2.2.2. Machine Learning in Tree-Based and Non-Linear Screening

A second pathway leverages tree-based ensemble models. gu2020empiricalassetpricing provided a milestone comparison of ML methods, establishing that neural networks and regression trees demonstrate exceptional performance in capturing nonlinear interactions for return prediction. In this approach, factors are typically screened based on feature importance scores. mai2024factorinvestment employed tree-based models and deep feedforward Neural Networks to evaluate the efficacy of factors selected by Lasso. Their results confirmed the efficacy of non-linear models in portfolio management, consistently identifying key predictive factors such as momentum and earnings yield across varying market regimes.

#### 2.2.3. Deep Learning in Factor Compression

In contrast to selecting a sparse subset of factors, deep learning techniques offer an alternative by compressing the high-dimensional factor universe into a low-dimensional set of latent representations. This is typically achieved through autoencoders or similar architectures. While effective at dimension reduction, a fundamental limitation lies in the opaque black box nature of these models, which often obscures the economic interpretation of the resulting latent factors. To address this, mai2024factorinvestment propose a hybrid CPCA framework that combines clustering with Principal Component Analysis (PCA) to construct lower-dimensional investment factors while maintaining a degree of interpretability often lost in purely deep learning-based approaches.

### 2.3. Reinforcement Learning for LLMs

Reinforcement learning has established itself as a cornerstone paradigm for aligning LLMs with human intent and augmenting their reasoning faculties (kaufmann2024surveyreinforcementlearninghuman). The dominant framework, reinforcement learning from human feedback (RLHF), was introduced to bolster instruction-following capabilities (ouyang2022traininglanguagemodelsfollow). This paradigm predominantly relies on proximal policy optimization (PPO) (schulman2017proximalpolicyoptimizationalgorithms), which utilizes a learned value function to estimate advantages and ensure training stability via a clipped surrogate objective. However, the requirement to maintain a value model incurs significant memory and computational overhead. Moreover, traditional RLHF faces challenges such as reward hacking and instability (casper2023openproblemsfundamentallimitations; lambert2024rewardbenchevaluatingrewardmodels). To mitigate these, alternative preference optimization methods like direct preference optimization (DPO) (rafailov2024directpreferenceoptimizationlanguage) and simple preference optimization (SimPO) (meng2024simposimplepreferenceoptimization) have been proposed to bypass explicit reward modeling.

To circumvent computational bottlenecks in reasoning-intensive tasks, recent methodological advancements have increasingly favored critic-free optimization paradigms. Notably, group relative policy optimization (GRPO) (shao2024deepseekmathpushinglimitsmathematical) has emerged as a robust alternative. Diverging from PPO, GRPO eschews the need for a separate value network by approximating the baseline via the mean rewards of a group of outputs sampled from the current policy. This group-relative formulation significantly reduces the computational footprint of RL training while preserving optimization stability. DeepSeek-R1 (guo\_deepseek-r1\_2025) exemplifies the efficacy of this paradigm in fostering self-evolving reasoning chains. This paradigm is now permeating the financial domain; for instance, Trading-R1 (xiao2025tradingr1financialtradingllm) utilizes a curriculum of supervised fine-tuning and RL to structure investment theses, while Fin-R1 (liu2025finr1largelanguagemodel) and FinO1 (qian2025fino1transferabilityreasoningenhancedllms) explore the transferability of reasoning capabilities to financial tasks. This directly motivates our adoption of this critic-free architecture for Alpha-R1, optimizing factor screening logic against objective market feedback.

## 3. Methodology

![Refer to caption](x1.png)


Figure 1. Alpha-R1 Framework Overview. The pipeline follows a sequential logic:
(a) Preparation: Abstracting raw technical indicators and financial news into atomic textual units to construct a global historical memory (Mg​l​o​b​a​lM\_{global}), coupled with systematic factor backtesting;
(b) Semantic Construction: Mapping quantitative performance metrics into structured semantic factor profiles (αd​e​s\alpha\_{des}) and synthesizing dynamic market states (StS\_{t});
(c) Reasoning & Optimization: Performing context-aware alpha screening via a reasoning core that evaluates αd​e​s\alpha\_{des} against StS\_{t}, with the policy iteratively refined through GRPO.

### 3.1. Data, Memory, and Factor Baselines

We establish the foundational data structures, historical context, and quantitative benchmarks through a systematic process.

#### 3.1.1. Raw Data Abstraction

We first transform heterogeneous raw data into structured textual atomic units.
At each time step tt, we construct two complementary market descriptors:

* •

  Price Market Description (StpriceS^{\text{price}}\_{t}): Summarizes information from technical indicators, trading volume, and sector rotation patterns.
* •

  News Market Description (StnewsS^{\text{news}}\_{t}): Encodes information from financial news and macroeconomic announcements to capture prevailing market sentiment.

#### 3.1.2. Iterative Memory Construction

We employ an iterative memory construction pipeline to capture long-term market context. This process aggregates the atomic textual units into a coherent historical narrative.
Let Iw={Stprice,Stnews}t∈wI\_{w}=\{S^{\text{price}}\_{t},S^{\text{news}}\_{t}\}\_{t\in w} denote the set of market descriptions within week ww. The weekly market summary MwM\_{w} is updated recursively using a large language model:

|  |  |  |  |
| --- | --- | --- | --- |
| (1) |  | Mw=FLLM​(Iw⊕Mw−1).M\_{w}=F\_{\text{LLM}}(I\_{w}\oplus M\_{w-1}). |  |

After iterating through the entire backtest period, we obtain the comprehensive backtest period market description (MglobalM\_{\text{global}}). This encapsulates the structural evolution and regime shifts of the market, forming the long-term historical memory required for the subsequent semantic profiling.

#### 3.1.3. Factor Backtesting

To establish the ground truth for factor behavior, we perform a backtest on the entire factor pool 𝒰\mathcal{U} over the historical window.
For each factor ii, we obtain a quantitative performance vector PiP\_{i}, which includes key metrics such as returns, volatility, and decay characteristics.
This dataset serves as the objective basis for linking market memory with factor effectiveness.

### 3.2. Profiling and State Description

Building on the prepared data foundation and long-term market memory, we construct the semantic state representations required for decision-making.

#### 3.2.1. Factor Semantic Descriptions

This stage maps quantitative signals into structured semantic representations. We combine the global market description from the backtest period, MglobalM\_{\text{global}}, with the factor-specific backtest results PiP\_{i}. An LLM then generates a semantic profile αdes,i\alpha\_{\text{des},i} for each factor ii:

|  |  |  |  |
| --- | --- | --- | --- |
| (2) |  | αdes,i=FLLM​(Mglobal,Pi).\alpha\_{\text{des},i}=F\_{\text{LLM}}(M\_{\text{global}},P\_{i}). |  |

Each profile articulates the factor’s underlying mechanism, its suitability across market regimes (e.g., high-volatility environments), and its limitations or failure conditions. These semantic descriptions serve as an instruction manual for the reasoning core in subsequent decision-making.

#### 3.2.2. Asset Pool State Description

To characterize the current investment environment, we construct an asset pool state description.
In contrast to the long-term market memory, this representation is generated dynamically for each decision day tt. Using the daily atomic units, (Stprice,StnewsS^{\text{price}}\_{t},S^{\text{news}}\_{t}), we synthesize the instantaneous market state:

|  |  |  |  |
| --- | --- | --- | --- |
| (3) |  | St=FLLM​(Stprice,Stnews).S\_{t}=F\_{\text{LLM}}(S^{\text{price}}\_{t},S^{\text{news}}\_{t}). |  |

The resulting state captures the prevailing index dynamics, dominant sector themes, and capital flow patterns, providing the situational context for subsequent factor selection decisions.

### 3.3. The Alpha-R1 Reasoning Model

The Alpha-R1 model serves as the central reasoning agent for factor screening and selection. At each decision time tt, a semantic decision context CtC\_{t} is constructed by combining two components:

|  |  |  |  |
| --- | --- | --- | --- |
| (4) |  | Ct={αdes,i}i∈𝒰⊕St,C\_{t}=\{\alpha\_{\text{des},i}\}\_{i\in\mathcal{U}}\oplus S\_{t}, |  |

where:

* •

  {αdes,i}\{\alpha\_{\text{des},i}\} denotes the set of semantic factor descriptions for the candidate pool 𝒰\mathcal{U}.
* •

  StS\_{t} is the contemporaneous semantic market state synthesized via FLLMF\_{\text{LLM}} as defined in Equation [3](https://arxiv.org/html/2512.23515v1#S3.E3 "In 3.2.2. Asset Pool State Description ‣ 3.2. Profiling and State Description ‣ 3. Methodology ‣ Alpha-R1: Alpha Screening with LLM Reasoning via Reinforcement Learning"), which encapsulates price dynamics and news narratives at time tt.

Based on this high-dimensional semantic context CtC\_{t}, Alpha-R1 performs inference to output the final selected factor list, denoted as 𝒜t\mathcal{A}\_{t}. We interpret this mechanism as a context-conditioned gating process where the LLM functions as a network that activates or deactivates factors based on semantic alignment between (i) factor mechanism profiles and failure conditions, and (ii) the current market state summarized from price dynamics and news narratives. This delegation of non-stationarity adaptation to the reasoning core allows the system to navigate regime shifts without the instability of purely numerical re-estimation.

Theoretically, we interpret our framework as a context-conditioned sparse linear model. The fixed linear scorer provides a stable, low-variance mapping from factor exposures to stock ranking. In regime-switching markets, the dominant error source is often model misspecification rather than within-regime estimation. While a purely dynamic linear model must re-estimate coefficients from limited and noisy samples—inducing high variance and overreaction to transient correlations—our approach reduces misspecification and estimation noise. By conditioning factor activation on richer state information and enforcing parsimonious selection, Alpha-R1 achieves more robust out-of-sample performance.

### 3.4. Reinforcement Learning via GRPO with Market Feedback

We optimize the Alpha-R1 reasoning model using reinforcement learning. This design enables learning directly from objective market feedback, adapting the RLHF paradigm to replace subjective human preferences with performance-based financial signals. The reward function combines quantitative portfolio outcomes with assessments of reasoning quality, and training is carried out using Group Relative Policy Optimization (GRPO) to ensure stable and efficient policy updates.

#### 3.4.1. Backbone Model and Stability

We adopt Qwen3-8B as the backbone model for its strong reasoning capabilities. This initialization accelerates convergence during reinforcement learning and improves the consistency and structure of generated outputs. In the absence of such a warm start, models are prone to overfitting superficial heuristics, leading to unstable or incoherent reasoning. The pre-trained backbone provides a stable foundation that preserves prior knowledge, allowing reinforcement learning to refine the model’s reasoning behavior.

#### 3.4.2. Multi-Component Reward Function with Market Feedback

We design a multi-component reward function that balances market performance with reasoning discipline:

|  |  |  |  |
| --- | --- | --- | --- |
| (5) |  | Rfinal=Radjusted−Pstructural,R\_{\text{final}}=R\_{\text{adjusted}}-P\_{\text{structural}}, |  |

where RadjustedR\_{\text{adjusted}} captures market-based performance feedback, and PstructuralP\_{\text{structural}} denotes the structural penalties that regulate action validity and sparsity. The reward components are computed through the following pipeline.

##### Rule-based Performance Reward

Market feedback is obtained via a backtesting procedure based on a linear factor model trained on four years of historical data.
We adopt a linear specification for three reasons: it provides a stable and interpretable mapping from factor exposures to expected returns, enables direct attribution of performance to selected factors, and avoids introducing non-stationarity into the reward signal during reinforcement learning by keeping the evaluation model fixed.

1. (1)

   Linear Model: We use fixed regression coefficients βi{\beta\_{i}} estimated from historical data.
2. (2)

   For each stock, predicted returns are computed using the selected factor set 𝒜t\mathcal{A}\_{t}:

   |  |  |  |  |
   | --- | --- | --- | --- |
   | (6) |  | R​e​t​u​r​npredicted=β0+∑i∈𝒜t(βi×Vi),Return\_{\text{predicted}}=\beta\_{0}+\sum\_{i\in\mathcal{A}\_{t}}(\beta\_{i}\times V\_{i}), |  |

   where ViV\_{i} denotes the previous-day value of factor ii, and unselected factors contribute zero.
3. (3)

   Portfolio Construction: Stocks are ranked by predicted returns, and the top NN are selected to form an equal-weighted portfolio.
4. (4)

   Base Reward Calculation: Compute the excess return over the benchmark over a holding period HH, scaled for the reward function:

   |  |  |  |  |
   | --- | --- | --- | --- |
   | (7) |  | Rbase=(Returnport​(𝒜t,H)−Returnbench​(H))×100,R\_{\text{base}}=\left(\text{Return}\_{\text{port}}(\mathcal{A}\_{t},H)-\text{Return}\_{\text{bench}}(H)\right)\times 100, |  |

   where HH denotes the holding period (e.g., H=5H=5 days) used for both the portfolio and the benchmark returns.

##### Quality-Adjusted Reward with LLM-as-Judge Evaluation

We incorporate reasoning quality into the reward through LLM-as-a-judge evaluation, in which an external large language model automatically assesses the model’s generated reasoning. A consistency penalty PconsistencyP\_{\text{consistency}} is computed as

|  |  |  |  |
| --- | --- | --- | --- |
| (8) |  | Pconsistency=FJudge​(Ct,𝒜t,response),P\_{\text{consistency}}=F\_{\text{Judge}}(C\_{t},\mathcal{A}\_{t},\text{response}), |  |

where FJudgeF\_{\text{Judge}} denotes a judge LLM (e.g., Claude 3.5 Haiku) that evaluates dimensions such as logical coherence, linguistic fluency, and information redundancy. The variable response represents the full textual output generated by the Alpha-R1 reasoning core, which encompasses both the chain-of-thought reasoning process and the final selected factor list 𝒜t\mathcal{A}\_{t}. The resulting score is normalized as Pnorm=Pconsistency/10.0P\_{\text{norm}}=P\_{\text{consistency}}/10.0 and applied asymmetrically to adjust the base reward:

|  |  |  |  |
| --- | --- | --- | --- |
| (9) |  | Radjusted={Rbase×(1−Pnorm)if ​Rbase>0Rbase×(1+Pnorm)if ​Rbase≤0.R\_{\text{adjusted}}=\begin{cases}R\_{\text{base}}\times(1-P\_{\text{norm}})&\text{if }R\_{\text{base}}>0\\ R\_{\text{base}}\times(1+P\_{\text{norm}})&\text{if }R\_{\text{base}}\leq 0\end{cases}. |  |

##### Structural Penalties

We incorporate a comprehensive structural penalty PstructuralP\_{\text{structural}} to enforce output discipline. This term qualitatively combines the requirements for parsimony and validity: it encourages the model to select a concise set of factors to avoid over-complexity, while strictly penalizing the generation of unparsable or non-existent factors to ensure the reasoning results are executable within the quantitative backtesting framework.

#### 3.4.3. GRPO Optimization with Market-Aligned Objectives

We employ Group Relative Policy Optimization (GRPO) to fine-tune the Alpha-R1 model. The normalized advantage estimate is computed as:

|  |  |  |  |
| --- | --- | --- | --- |
| (10) |  | A^i=ri−mean​(r)std​(r),ρt(i)​(θ)=πθ​(oi,t∣q,oi,<t)πθold​(oi,t∣q,oi,<t),\hat{A}\_{i}=\frac{r\_{i}-\text{mean}(r)}{\text{std}(r)},\quad\rho\_{t}^{(i)}(\theta)=\frac{\pi\_{\theta}(o\_{i,t}\mid q,o\_{i,<t})}{\pi\_{\theta\_{\text{old}}}(o\_{i,t}\mid q,o\_{i,<t})}, |  |

where ρt(i)​(θ)\rho\_{t}^{(i)}(\theta) denotes the probability ratio between the current and old policies. The GRPO objective function is defined as:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (11) |  | JGRPO​(θ)\displaystyle J\_{\text{GRPO}}(\theta) | =𝔼q,{oi}[1G∑i=1G1|oi|∑t=1|oi|min(ρt(i)(θ)A^i,\displaystyle=\mathbb{E}\_{q,\{o\_{i}\}}\Bigg[\frac{1}{G}\sum\_{i=1}^{G}\frac{1}{|o\_{i}|}\sum\_{t=1}^{|o\_{i}|}\min\Big(\rho\_{t}^{(i)}(\theta)\hat{A}\_{i}, |  |
|  |  | clip(ρt(i)(θ),1−ϵ,1+ϵ)A^i)]\displaystyle\qquad\qquad\text{clip}\left(\rho\_{t}^{(i)}(\theta),1-\epsilon,1+\epsilon\right)\hat{A}\_{i}\Big)\Bigg] |  |
|  |  | −β𝔼q[DKL(πθ(⋅∣q)∥πref(⋅∣q))],\displaystyle\quad-\beta\mathbb{E}\_{q}\left[D\_{\text{KL}}\left(\pi\_{\theta}(\cdot\mid q)\|\pi\_{\text{ref}}(\cdot\mid q)\right)\right], |  |

where:

* •

  qq represents the input context, including market state and factor descriptions;
* •

  oio\_{i} represents the ii-th response in the group of size GG;
* •

  πθ\pi\_{\theta}, πold\pi\_{\text{old}}, and πref\pi\_{\text{ref}} denote the current, sampling, and reference policies, respectively;
* •

  β\beta controls the KL-divergence regularization strength, and ϵ\epsilon is the clipping parameter.

The objective function consists of two primary components: (1) a clipped surrogate objective that encourages policy updates towards higher advantage, and (2) a KL-divergence regularization term preventing deviation from the reference model.
This ensures stable training while optimizing for the market-aligned reward defined in Equation [5](https://arxiv.org/html/2512.23515v1#S3.E5 "In 3.4.2. Multi-Component Reward Function with Market Feedback ‣ 3.4. Reinforcement Learning via GRPO with Market Feedback ‣ 3. Methodology ‣ Alpha-R1: Alpha Screening with LLM Reasoning via Reinforcement Learning").
Through this approach, Alpha-R1 learns to select factor combinations that not only generate superior excess returns but also exhibit coherent and interpretable reasoning patterns.

### 3.5. Portfolio Construction and Execution

To translate factor selection into realized market performance, we implement a practical execution mechanism that accounts for liquidity constraints and transaction costs. Given the factor set 𝒜t\mathcal{A}\_{t} selected by Alpha-R1, portfolio positions are constructed using a slot rotation strategy and executed via volume-weighted average price (VWAP)–based trading.

#### 3.5.1. Slot Rotation Mechanism

To mitigate the high turnover costs typically associated with daily rebalancing, we divide the total capital CC into HH independent sub-portfolios (referred to as slots), where HH corresponds to the holding period (e.g., H=5H=5 days).
On any given trading day tt, only the specific slot indexed by k=t(modH)k=t\pmod{H} undergoes rebalancing:

|  |  |  |  |
| --- | --- | --- | --- |
| (12) |  | Pt,k=Rebalance​(Pt−1,k,𝒜t),P\_{t,k}=\text{Rebalance}(P\_{t-1,k},\mathcal{A}\_{t}), |  |

where Pt,kP\_{t,k} represents the holdings of the kk-th slot.
The remaining H−1H-1 slots remain passive. This approach effectively smooths out the equity curve and reduces the average daily turnover rate to 1/H1/H, allowing for broader market coverage without incurring excessive friction costs.

#### 3.5.2. VWAP-based Execution and Constraints

Unlike simplified backtesting engines that assume execution at the opening price PopenP\_{\text{open}}, we employ a volume-weighted average price (VWAP) model to better approximate realized trading costs. For a selected stock ss, the execution price P^s,t\hat{P}\_{s,t} is computed using transaction data from the first 30 minutes of the trading session (09:31–10:00):

|  |  |  |  |
| --- | --- | --- | --- |
| (13) |  | P^s,t=∑i=130(P​r​i​c​es,t,i×V​o​l​u​m​es,t,i)∑i=130V​o​l​u​m​es,t,i.\hat{P}\_{s,t}=\frac{\sum\_{i=1}^{30}(Price\_{s,t,i}\times Volume\_{s,t,i})}{\sum\_{i=1}^{30}Volume\_{s,t,i}}. |  |

This interval corresponds to the period of highest market liquidity and provides a conservative estimate of execution slippage. To ensure market realism, the execution process enforces the following constraints:

* •

  Limit-Move Constraints: Buy orders are rejected if the stock hits the upper price limit (Limit-Up) during the execution window, and sell orders are deferred if the stock is locked at the lower price limit (Limit-Down).
* •

  IPO Exclusion: Stocks are strictly excluded from trading on their initial listing day to avoid extreme volatility distortions.
* •

  Transaction Costs: A transaction fee of 0.1% (10 bps) is applied to both buy and sell orders to account for commissions and slippage.

The daily portfolio return RtR\_{t} is computed as the aggregate return across all HH slots, providing an overall measure of execution-adjusted strategy performance.

## 4. Experiments

This section presents a comprehensive empirical evaluation of Alpha-R1. We benchmark Alpha-R1 against a range of traditional quantitative strategies and state-of-the-art large language models (LLMs) to assess its effectiveness in dynamic market environments. Our evaluation is guided by the following research questions:

Q1:  Does Alpha-R1 consistently outperform traditional machine learning baselines and reasoning LLMs across distinct asset pools?

Q2:  What are the contributions of individual components (e.g., news, price, semantic descriptions) to the model’s performance?

Q3:  Does the semantic gating mechanism of Alpha-R1 offer tangible advantages over traditional heuristic gating strategies?

Q4:  How sensitive is the model’s performance to hyperparameter variations?

Table 1. Main Experiment Results. Performance comparison of Alpha-R1 against baselines across two asset pools (Testing Period: 2025.01.01 – 2025.06.30). Results are reported as the average of 5 independent runs. CR: Cumulative Return, AR: Annualized Return, SR: Sharpe Ratio, MDD: Maximum Drawdown. The best results are highlighted in bold.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Type | Method | Asset Pool CSI 300 (In-Domain) | | | | Asset Pool CSI 1000 (Out-of-Domain) | | | |
| CR (%) | AR (%) | SR | MDD (%) | CR (%) | AR (%) | SR | MDD (%) |
| Non-LLM | Buy & Hold | 3.03 | 6.70 | 0.33 | 10.49 | 9.64 | 22.14 | 0.80 | 16.87 |
| PCA | -0.48 | 0.40 | -0.06 | 14.69 | 6.24 | 16.09 | 0.59 | 16.13 |
| XGBoost | -10.03 | -21.65 | -1.54 | 15.33 | 4.34 | 11.77 | 0.45 | 19.12 |
| LightGBM | -5.10 | -10.26 | -0.83 | 13.43 | -5.37 | -6.92 | -0.26 | 23.88 |
| A2C | -5.52 | -11.12 | -0.85 | 11.22 | 11.80 | 26.30 | 1.15 | 14.00 |
| PPO | 0.89 | 3.28 | 0.11 | 11.67 | -6.44 | -7.62 | -0.25 | 29.31 |
| LLM | Gemini 2.5 Pro Thinking | -7.04 | -14.45 | -1.01 | 15.08 | -8.73 | -15.38 | -0.58 | 28.37 |
| Claude 3.7 Sonnet Thinking | -5.41 | -10.23 | -0.63 | 13.58 | 3.80 | 13.26 | 0.43 | 16.98 |
| DeepSeek-R1 | -5.98 | -11.93 | -0.82 | 14.88 | -7.58 | -12.87 | -0.50 | 27.89 |
| Qwen3-8B | -6.32 | -12.41 | -0.77 | 16.35 | 2.73 | 10.23 | 0.29 | 21.78 |
| Alpha-R1 (Ours) | 12.99 | 27.59 | 1.62 | 6.76 | 42.49 | 78.18 | 4.03 | 9.25 |



![Refer to caption](images/nav/main_result_comparison.png)


(a) Net Value - Asset Pool CSI 300

![Refer to caption](images/nav/main_result_csi1000_comparison.png)


(b) Net Value - Asset Pool CSI 1000

Figure 2. Cumulative Net Value Curves. Comparison of wealth accumulation trajectories on the 2025 testing set. (a) On the CSI 300, Alpha-R1 outperforms all baselines with lower drawdown. (b) On the Out-of-Domain CSI 1000, Alpha-R1 demonstrates superior zero-shot transferability, whereas traditional RL models exhibit inconsistent performance: A2C shows improved returns but with higher volatility, while PPO suffers from significant drawdowns, indicating overfitting and limited generalization.

### 4.1. Experimental Setup

#### 4.1.1. Dataset and Dynamic Factor Zoo

We construct a dynamic factor zoo by filtering the Alpha101 library (kakushadze2016101), retaining 82 computationally feasible factors. To avoid look-ahead bias, the experiments are temporally segmented:

Pre-training Phase (2020.01.01 – 2023.12.31): Used solely to estimate the fixed coefficients βi\beta\_{i} for the linear reward model described in Section [3.4](https://arxiv.org/html/2512.23515v1#S3.SS4 "3.4. Reinforcement Learning via GRPO with Market Feedback ‣ 3. Methodology ‣ Alpha-R1: Alpha Screening with LLM Reasoning via Reinforcement Learning").

Training Phase (2024.07.01 – 2024.12.31): Using constituent stocks from the CSI 300, we simulate a high-turnover environment. To encourage semantic reasoning rather than factor memorization, we adopt a randomized factor augmentation scheme: for each trading date, 300 training samples are generated, each with a randomly selected subset of 40 factors drawn from the full pool of 82 as the state input.

Testing Phase (2025.01.01 – 2025.06.30): For strictly out-of-sample evaluation, we construct a fixed candidate set of 40 factors selected based on historical RankIC performance over 2023–2024. Evaluation is conducted on both the CSI 300 (large-cap, in-domain) and the CSI 1000 (small-cap, out-of-domain) universes to assess generalization across asset pools. While both are temporally out-of-sample, the CSI 1000 evaluates zero-shot spatial generalization.

#### 4.1.2. Baselines and Model Configuration

We compare Alpha-R1 against two classes of baselines. The first consists of traditional quantitative strategies, including statistical methods (PCA), tree-based ensembles (XGBoost and LightGBM), and deep reinforcement learning approaches (A2C and PPO). The second class comprises reasoning-enabled large language models, including Gemini 2.5 Pro Thinking, Claude 3.7 Sonnet Thinking, DeepSeek-R1, and the base model Qwen3-8B.

Consistent with the execution protocol described in Section [3.5](https://arxiv.org/html/2512.23515v1#S3.SS5 "3.5. Portfolio Construction and Execution ‣ 3. Methodology ‣ Alpha-R1: Alpha Screening with LLM Reasoning via Reinforcement Learning"), we employ a slot rotation strategy with a holding period of H=5H=5 days, managing five concurrent sub-portfolios. Each slot selects T​o​p​N=10TopN=10 stocks, and trades are executed using 30-minute VWAP prices with a fixed bilateral transaction cost of 0.1%.

To prevent data leakage and ensure a fair evaluation, all benchmark LLMs have pre-training data cutoffs strictly no later than December 31, 2024. Alpha-R1 adopts Qwen3-8B as its backbone model. Inference is performed deterministically with temperature=0 and top\_p=0.7.

#### 4.1.3. Evaluation Protocol

Performance is evaluated using cumulative return (CR), annualized return (AR), Sharpe ratio (SR), and maximum drawdown (MDD). To reduce the impact of random initialization, all reported backtesting results are averaged over five independent runs.

### 4.2. Performance Evaluation

We first evaluate the capacity of Alpha-R1 to generate excess returns. Table [1](https://arxiv.org/html/2512.23515v1#S4.T1 "Table 1 ‣ 4. Experiments ‣ Alpha-R1: Alpha Screening with LLM Reasoning via Reinforcement Learning") details the quantitative metrics, while Figure [2](https://arxiv.org/html/2512.23515v1#S4.F2 "Figure 2 ‣ 4. Experiments ‣ Alpha-R1: Alpha Screening with LLM Reasoning via Reinforcement Learning") visualizes the wealth accumulation trajectories.

#### 4.2.1. Comparative Analysis on In-Domain Testing (CSI 300)

As shown in Table [1](https://arxiv.org/html/2512.23515v1#S4.T1 "Table 1 ‣ 4. Experiments ‣ Alpha-R1: Alpha Screening with LLM Reasoning via Reinforcement Learning") and Figure [2(a)](https://arxiv.org/html/2512.23515v1#S4.F2.sf1 "In Figure 2 ‣ 4. Experiments ‣ Alpha-R1: Alpha Screening with LLM Reasoning via Reinforcement Learning"), Alpha-R1 achieves the strongest performance on the CSI 300 domain.

* •

  Comparison with tree-based models. Gradient boosting methods such as XGBoost, while effective on static prediction tasks, perform poorly in this setting (e.g., cumulative return of -10.03%). This highlights a critical limitation: in non-stationary markets, the dominant error source is often model misspecification rather than within-regime estimation. A purely dynamic model that re-estimates coefficients from limited and noisy samples induces high variance and can overreact to transient correlations as historical correlations deteriorate.
* •

  Comparison with reinforcement learning methods. Deep RL approaches such as A2C and PPO struggle to adapt to the non-stationary market environment. A2C achieves a negative cumulative return of -5.52% with a Sharpe ratio of -0.85, while PPO shows only marginal positive returns (0.89%) with a low Sharpe ratio of 0.11. This suggests that numerical RL agents, despite their ability to learn sequential decision-making, are vulnerable to distributional shifts and fail to capture the semantic relationships that govern factor effectiveness across different market regimes.
* •

  Comparison with generic reasoning LLMs. Models such as Claude 3.7 Sonnet and DeepSeek-R1 demonstrate strong general reasoning ability but lack domain-specific financial grounding. As a result, they fail to adequately account for risk constraints, leading to substantial drawdowns (approximately 15–16%) and negative Sharpe ratios.
* •

  Performance of Alpha-R1. By interpreting our framework as a context-conditioned sparse linear model, Alpha-R1 attains a Sharpe ratio of 1.62 while limiting maximum drawdown to 6.76%. The fixed linear scorer provides a stable, low-variance mapping, while the LLM reasoning core functions as a gating network that activates or deactivates factors based on semantic alignment. This allows for stable and risk-aware decision-making even as market regimes shift.

#### 4.2.2. Zero-Shot Generalization on Out-of-Domain (CSI 1000)

The CSI 1000 experiment (Figure [2(b)](https://arxiv.org/html/2512.23515v1#S4.F2.sf2 "In Figure 2 ‣ 4. Experiments ‣ Alpha-R1: Alpha Screening with LLM Reasoning via Reinforcement Learning")) evaluates the model’s ability to generalize under a zero-shot setting. Compared with the CSI 300, the CSI 1000 represents a small-cap universe with higher volatility and more pronounced idiosyncratic dynamics.

Numerical reinforcement learning agents, such as A2C and PPO, exhibit limited generalization beyond the training domain. On the CSI 300, A2C achieves a negative cumulative return of -5.52% with a Sharpe ratio of -0.85, while PPO shows marginal positive returns (0.89%) with a low Sharpe ratio of 0.11. When transferred to the CSI 1000, A2C shows improved performance (cumulative return of 11.80%) but PPO suffers significant degradation with a negative return of -6.44% and a maximum drawdown of 29.31%, indicating sensitivity to domain-specific statistical patterns and overfitting issues.

In contrast, Alpha-R1 maintains strong performance on the out-of-domain CSI 1000 universe, achieving a cumulative return of 42.49% and a Sharpe ratio of 4.03. This confirms the advantage of delegating non-stationarity adaptation to the LLM. By conditioning factor activation on richer state information (summarized from price dynamics and news narratives) and enforcing parsimonious selection, our approach reduces misspecification and estimation noise. This mechanism enables robust zero-shot transfer by capturing higher-level economic relationships rather than relying on noisy, domain-specific statistical regularities.

![Refer to caption](images/heatmap/csi300/sharpe_ratio_heatmap.png)


(a) CSI 300: Sharpe Ratio

![Refer to caption](images/heatmap/csi300/total_return_heatmap.png)


(b) CSI 300: Cumulative Return

![Refer to caption](images/heatmap/csi300/max_drawdown_heatmap.png)


(c) CSI 300: Max Drawdown

![Refer to caption](images/heatmap/csi1000/sharpe_ratio_heatmap.png)


(d) CSI 1000: Sharpe Ratio

![Refer to caption](images/heatmap/csi1000/total_return_heatmap.png)


(e) CSI 1000: Cumulative Return

![Refer to caption](images/heatmap/csi1000/max_drawdown_heatmap.png)


(f) CSI 1000: Max Drawdown

Figure 3. Parameter Sensitivity and Generalization Analysis. The heatmaps illustrate the impact of varying TopN and HoldingDays. Green regions indicate favorable performance (High Sharpe/Return, Low Drawdown), while Red regions indicate poor performance. The broad Green clusters across both asset pools confirm the strategy’s robustness.

### 4.3. Ablation Study

To dissect the contributions of individual components, we conduct a series of ablation experiments to isolate the impact of key modules in Alpha-R1. All ablation variants are trained from scratch using the modified framework to ensure a fair comparison.

#### 4.3.1. Ablation Variants

We consider the following four variants to evaluate the necessity of data inputs, factor representations, and the training objective:

* •

  w/o News: Removes market news information from the state space StS\_{t}, forcing the model to rely solely on price data and factor values.
* •

  w/o Market Price: Removes market price trends from StS\_{t}, retaining only news narratives and factor values.
* •

  w/o Semantic Description: Replaces the natural language descriptions of factors with their raw mathematical formulas to test if the LLM relies on semantic reasoning or pattern matching.
* •

  w/o RL Optimization: Uses the backbone model (Qwen3-8B) without the reinforcement learning alignment pipeline.

#### 4.3.2. Results and Analysis

Table 2. Ablation Study Results. Performance contribution of different components (Testing Period: 2025.01.01 – 2025.06.30 on CSI 300).

| Method | CR (%) | AR (%) | SR | MDD (%) |
| --- | --- | --- | --- | --- |
| Alpha-R1 (Full) | 12.99 | 27.59 | 1.62 | 6.76 |
| Buy & Hold (CSI 300 Index) | 3.03 | 6.70 | 0.33 | 10.49 |
| w/o Market Price | 10.24 | 22.42 | 1.24 | 12.87 |
| w/o News | 8.75 | 19.61 | 1.03 | 12.01 |
| w/o Semantic Description | 7.26 | 16.76 | 0.83 | 13.32 |
| w/o RL Optimization | -6.32 | -12.41 | -0.77 | 16.35 |

Table [2](https://arxiv.org/html/2512.23515v1#S4.T2 "Table 2 ‣ 4.3.2. Results and Analysis ‣ 4.3. Ablation Study ‣ 4. Experiments ‣ Alpha-R1: Alpha Screening with LLM Reasoning via Reinforcement Learning") provides a quantitative decomposition of the performance contributions attributable to each module within the Alpha-R1 framework. By systematically ablating key components, we elucidate the specific mechanisms driving the model’s superior risk-adjusted returns. The empirical evidence supports three principal conclusions regarding the architecture’s efficacy:

##### The Imperative of Reinforcement Learning Alignment.

The most profound performance disparity is observed between the full model and the w/o RL Optimization variant. The unaligned base model (Qwen3-8B) fails to generate positive alpha, yielding a Sharpe Ratio of -0.77, identical to the w/o RL Optimization case. This finding corroborates the hypothesis that general-purpose reasoning capabilities, while necessary, are insufficient for the stochastic and adversarial nature of financial markets. The RL alignment process acts as a crucial transformation layer, grounding the LLM’s broad semantic knowledge into specific, risk-aware actionable policies. Without this targeted optimization, the model’s latent reasoning capacity cannot be effectively translated into profitable trading decisions.

##### Semantic Reasoning Over Mathematical Memorization.

The degradation in performance observed in the w/o Semantic Description variant—where natural language factor descriptions are replaced by raw mathematical formulas—highlights the model’s reliance on semantic reasoning. The Sharpe Ratio declines by approximately 49% (from 1.62 to 0.83). This substantial gap suggests that Alpha-R1 does not merely memorize statistical patterns associated with factor formulas. Instead, it leverages the semantic richness of natural language to infer the economic rationale behind factors, enabling more robust selection in changing market regimes compared to purely symbolic processing.

##### Synergistic Integration of Multi-Modal Signals.

The ablation of informational inputs reveals the complementary nature of news narratives and price dynamics. Excluding market news (w/o News) results in a more severe deterioration of the Sharpe Ratio (dropping to 1.03) compared to removing price trends (1.24). This implies that qualitative news data serves as a superior leading indicator for detecting regime shifts than historical price momentum alone. However, the full model exhibits the lowest Maximum Drawdown (6.76%), significantly outperforming both data-truncated variants. This indicates a synergistic effect: while news provides high-level context, price dynamics offer granular trend confirmation, and their integration is essential for minimizing tail risk and ensuring robust execution.

In synthesis, the superior performance of Alpha-R1 is not attributable to any single isolated component but emerges from the holistic integration of semantic understanding, multi-modal context awareness, and rigorous RL-based alignment.

### 4.4. Semantic vs. Heuristic Gating Strategies

To validate the superiority of our semantic gating mechanism, we compare it against traditional heuristic gating strategies. We consider:

* •

  Lasso: A classic sparse linear model selecting factors via L1L\_{1} regularization.
* •

  IC Momentum: A momentum-based heuristic selecting the top 10 factors based on their recent average IC over a 20-day window.

Table 3. Gating Strategy Comparison. Performance of Alpha-R1 (Semantic Gating) versus heuristic gating methods (Lasso and IC Momentum) on the CSI 300 testing set.

| Method | CR (%) | AR (%) | SR | MDD (%) |
| --- | --- | --- | --- | --- |
| Alpha-R1 (Semantic Gating) | 12.99 | 27.59 | 1.62 | 6.76 |
| Lasso | 1.58 | 4.63 | 0.20 | 11.12 |
| IC Momentum | -6.33 | -12.55 | -0.80 | 13.29 |

As shown in Table [3](https://arxiv.org/html/2512.23515v1#S4.T3 "Table 3 ‣ 4.4. Semantic vs. Heuristic Gating Strategies ‣ 4. Experiments ‣ Alpha-R1: Alpha Screening with LLM Reasoning via Reinforcement Learning"), Alpha-R1 significantly outperforms both heuristic baselines. While Lasso achieves a small positive return (1.58%), it lags behind the semantic gating approach. IC Momentum performs poorly (-6.33% CR), likely because historical IC measures often fail to persist in highly dynamic regimes. In contrast, Alpha-R1’s semantic gating leverages market context to adaptively select factors, demonstrating superior robustness to regime shifts.

### 4.5. Robustness and Generalization

To assess the strategy’s resilience, we conduct a parameter sensitivity analysis visualized via heatmaps in Figure [3](https://arxiv.org/html/2512.23515v1#S4.F3 "Figure 3 ‣ 4.2.2. Zero-Shot Generalization on Out-of-Domain (CSI 1000) ‣ 4.2. Performance Evaluation ‣ 4. Experiments ‣ Alpha-R1: Alpha Screening with LLM Reasoning via Reinforcement Learning").

#### 4.5.1. Parameter Sensitivity (CSI 300)

The top row of Figure [3](https://arxiv.org/html/2512.23515v1#S4.F3 "Figure 3 ‣ 4.2.2. Zero-Shot Generalization on Out-of-Domain (CSI 1000) ‣ 4.2. Performance Evaluation ‣ 4. Experiments ‣ Alpha-R1: Alpha Screening with LLM Reasoning via Reinforcement Learning") visualizes performance metrics on the in-domain asset pool. We observe broad green regions indicating high Sharpe Ratios across a wide range of settings (e.g., Holding Days 3–10). Notably, performance remains stable even as T​o​p​NTopN increases from 5 to 20. This suggests that Alpha-R1 identifies a cluster of effective factors rather than relying on a single outlier signal, thereby reducing concentration risk.

#### 4.5.2. Zero-Shot Generalization (CSI 1000)

The bottom row of Figure [3](https://arxiv.org/html/2512.23515v1#S4.F3 "Figure 3 ‣ 4.2.2. Zero-Shot Generalization on Out-of-Domain (CSI 1000) ‣ 4.2. Performance Evaluation ‣ 4. Experiments ‣ Alpha-R1: Alpha Screening with LLM Reasoning via Reinforcement Learning") highlights the model’s performance on the out-of-domain CSI 1000 asset pool. Despite the significant shift in asset characteristics, the heatmaps display a consistent distribution of high-performance green clusters similar to the in-domain testing set. This confirms that Alpha-R1 possesses strong zero-shot generalization capabilities. Unlike traditional models that degrade rapidly outside their training distribution, Alpha-R1 leverages its semantic understanding of market regimes to dynamically adjust factor selections for the new asset pool, delivering robust risk-adjusted returns without retraining.

## 5. Conclusion

This paper introduces Alpha-R1, a semantics-driven approach to quantitative investment that shifts the focus from static factor mining to context-aware reasoning. Rather than relying solely on historical correlations, Alpha-R1 employs a reinforcement-learning–trained large language model to reason over the economic rationale underlying factor performance and its dependence on evolving market conditions.

By constructing a dual-layer semantic context that integrates long-term market memory with real-time information, Alpha-R1 connects unstructured data sources with quantitative decision-making in a unified manner. Methodologically, we develop a market-aligned reinforcement learning framework based on Group Relative Policy Optimization (GRPO), in which training is guided by objective market outcomes instead of subjective human feedback.

Extensive empirical results show that Alpha-R1 consistently outperforms traditional machine learning baselines and generic reasoning LLMs across multiple asset pools. Notably, Alpha-R1 demonstrates strong zero-shot generalization when transferred from the CSI 300 to the CSI 1000 universe, maintaining stable and profitable performance in a previously unseen, high-volatility environment, where conventional reinforcement learning agents experience marked degradation. These findings suggest that grounding factor selection in semantic reasoning and market feedback provides a viable approach for mitigating alpha decay and addressing non-stationarity in financial markets.