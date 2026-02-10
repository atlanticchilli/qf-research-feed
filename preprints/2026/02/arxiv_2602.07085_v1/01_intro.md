---
authors:
- Jun Han
- Shuo Zhang
- Wei Li
- Zhi Yang
- Yifan Dong
- Tu Hu
- Jialuo Yuan
- Xiaomin Yu
- Yumo Zhu
- Fangqi Lou
- Xin Guo
- Zhaowei Liu
- Tianyi Jiang
- Ruichuan An
- Jingping Liu
- Biao Wu
- Rongze Chen
- Kunyi Wang
- Yifan Wang
- Sen Hu
- Xinbing Kong
- Liwen Zhang
- Ronghao Chen
- Huacan Wang
doc_id: arxiv:2602.07085v1
family_id: arxiv:2602.07085
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining'
url_abs: http://arxiv.org/abs/2602.07085v1
url_html: https://arxiv.org/html/2602.07085v1
venue: arXiv q-fin
version: 1
year: 2026
---


Jun Han1\*,
Shuo Zhang2\*,
Wei Li1\*,
Zhi Yang1\*,
Yifan Dong1,
Tu Hu2,
  
Jialuo Yuan3,
Xiaomin Yu2,
Yumo Zhu1,
Fangqi Lou1,
Xin Guo1,
Zhaowei Liu1,
  
Tianyi Jiang4,
Ruichuan An4,
Jingping Liu5,
Biao Wu2,
Rongze Chen2,
Kunyi Wang2,
  
Yifan Wang2,
Sen Hu2,4,
Xinbing Kong6†,
Liwen Zhang1†,
Ronghao Chen2,4†,
Huacan Wang2†
  
  
1SUFE,
2QuantaAlpha,
3Stanford,
4PKU,
5SYSU,
6SEU
  
\*These authors contributed equally to this work.
  
†Correspondence:
[xinbingkong@126.com](mailto:xinbingkong@126.com),
[zhang.liwen@shufe.edu.cn](mailto:zhang.liwen@shufe.edu.cn),
[chenronghao@alumni.pku.edu.cn](mailto:chenronghao@alumni.pku.edu.cn),
[wanghuacan17@mails.ucas.ac.cn](mailto:wanghuacan17@mails.ucas.ac.cn)
AIFin Lab: [aifinlab.sufe@gmail.com](mailto:aifinlab.sufe@gmail.com)QuantaAlpha: [quantaalpha.ai@gmail.com](mailto:quantaalpha.ai@gmail.com)

###### Abstract

Financial markets are noisy and non-stationary, making alpha mining highly sensitive to noise in backtesting results and sudden market regime shifts. While recent agentic frameworks improve alpha mining automation, they often lack controllable multi-round search and reliable reuse of validated experience. To address these challenges, we propose QuantaAlpha, an evolutionary alpha mining framework that treats each end-to-end mining run as a trajectory and improves factors through trajectory-level mutation and crossover operations. QuantaAlpha localizes suboptimal steps in each trajectory for targeted revision and recombines complementary high-reward segments to reuse effective patterns, enabling structured exploration and refinement across mining iterations.
During factor generation, QuantaAlpha enforces semantic consistency across the hypothesis, factor expression, and executable code, while constraining the complexity and redundancy of the generated factor to mitigate crowding. Extensive experiments on the China Securities Index 300 (CSI 300) demonstrate consistent gains over strong baseline models and prior agentic systems. When utilizing GPT-5.2, QuantaAlpha achieves an Information Coefficient (IC) of 0.1501, with an Annualized Rate of Return (ARR) of 27.75% and a Maximum Drawdown (MDD) of 7.98%. Moreover, factors mined on CSI 300 transfer effectively to the China Securities Index 500 (CSI 500) and the Standard & Poor’s 500 Index (S&P 500), delivering 160% and 137% cumulative excess return over four years, respectively, which indicates strong robustness of QuantaAlpha under market distribution shifts.

![[Uncaptioned image]](images/icon.jpg) QuantaAlpha: An Evolutionary Framework for LLM-Driven
  
Alpha Mining

Jun Han1\*,
Shuo Zhang2\*,
Wei Li1\*,
Zhi Yang1\*,
Yifan Dong1,
Tu Hu2,

Jialuo Yuan3,
Xiaomin Yu2,
Yumo Zhu1,
Fangqi Lou1,
Xin Guo1,
Zhaowei Liu1,

Tianyi Jiang4,
Ruichuan An4,
Jingping Liu5,
Biao Wu2,
Rongze Chen2,
Kunyi Wang2,

Yifan Wang2,
Sen Hu2,4,
Xinbing Kong6†,
Liwen Zhang1†,
Ronghao Chen2,4†,
Huacan Wang2†

1SUFE††thanks: AIFin Lab: [aifinlab.sufe@gmail.com](mailto:aifinlab.sufe@gmail.com),
2QuantaAlpha††thanks: QuantaAlpha: [quantaalpha.ai@gmail.com](mailto:quantaalpha.ai@gmail.com),
3Stanford,
4PKU,
5SYSU,
6SEU


\*These authors contributed equally to this work.


†Correspondence:
[xinbingkong@126.com](mailto:xinbingkong@126.com),
[zhang.liwen@shufe.edu.cn](mailto:zhang.liwen@shufe.edu.cn),
[chenronghao@alumni.pku.edu.cn](mailto:chenronghao@alumni.pku.edu.cn),
[wanghuacan17@mails.ucas.ac.cn](mailto:wanghuacan17@mails.ucas.ac.cn)

<https://github.com/QuantaAlpha/QuantaAlpha>

![Refer to caption](images/figure3.png)


Figure 1: Cumulative excess returns of different approaches on CSI 500 and S&P 500.

## 1 Introduction

Financial markets are high-dimensional, non-stationary stochastic systems, where returns exhibit heavy tails Fama ([1965](https://arxiv.org/html/2602.07085v1#bib.bib33 "The behavior of stock-market prices")), time-varying volatility Engle ([1982](https://arxiv.org/html/2602.07085v1#bib.bib34 "Autoregressive conditional heteroscedasticity with estimates of the variance of united kingdom inflation")), and cross-sectional dependence Pesaran ([2021](https://arxiv.org/html/2602.07085v1#bib.bib35 "General diagnostic tests for cross-sectional dependence in panels")). Quantitative investment therefore relies on alpha mining to extract predictive signals from noisy observations. Recently, large language models (LLMs) Lopez-Lira and Tang ([2023](https://arxiv.org/html/2602.07085v1#bib.bib1 "Can chatgpt forecast stock price movements? return predictability and large language models")) and LLM-based agent frameworks Zhang et al. ([2024](https://arxiv.org/html/2602.07085v1#bib.bib2 "A multimodal foundation agent for financial trading: tool-augmented, diversified, and generalist")); Xiao et al. ([2024](https://arxiv.org/html/2602.07085v1#bib.bib3 "TradingAgents: multi-agents llm financial trading framework")) have been introduced into the factor research workflow. By leveraging advanced reasoning and code generation capabilities, these systems can automate factor construction and iteratively refine candidates through backtesting feedback.

![Refer to caption](images/Intro.jpg)


Figure 2: Comparison with existing methods: QuantaAlpha improves alpha discovery through trajectory-level self-evolution.

Representative agent frameworks for alpha mining simulate the workflow of human quantitative researchers by iteratively performing hypothesis generation, executable factor construction, and backtesting-based refinement, as illustrated in Figure [2](https://arxiv.org/html/2602.07085v1#S1.F2 "Figure 2 ‣ 1 Introduction ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining"). Under this paradigm, AlphaAgent Tang et al. ([2025b](https://arxiv.org/html/2602.07085v1#bib.bib4 "Alphaagent: llm-driven alpha mining with regularized exploration to counteract alpha decay")) imposes explicit regularization during factor generation to curb factor crowding and mitigate alpha decay, while RD-Agent Li et al. ([2025d](https://arxiv.org/html/2602.07085v1#bib.bib5 "R&D-agent-quant: a multi-agent framework for data-centric factors and model joint optimization")) targets full-stack automation with coordinated research and development agents, enabling joint factor–model co-optimization for robust strategy discovery. These frameworks reduce the trial-and-error costs of factor research while preserving interpretability relative to parameter-trained methods, making large-scale exploration practical.

However, under real-market non-stationarity and low signal-to-noise ratios, existing systems still face three limitations. (i) Fragile controllability: Iterative refinement is driven by noisy backtest feedback, which can induce semantic drift and steer updates toward spurious correlations, gradually deviating from the intended economic mechanism. (ii) Limited trustworthiness: Many methods rely on stochastic re-generation conditioned on transient contexts, without explicitly inheriting validated rationales across iterations. As a result, they lack a traceable lineage and the produced factors are harder to audit and trust. (iii) Constrained exploration: Search often over-exploits local neighborhoods around initial seeds, leading to redundancy and factor crowding, while providing limited systematic coverage of the broader hypothesis space and weakening long-horizon discovery.

To address these challenges, we propose QuantaAlpha, an evolutionary alpha mining framework that improves factor quality through trajectory-level self-evolution. Inspired by Lin et al. ([2025](https://arxiv.org/html/2602.07085v1#bib.bib17 "Se-agent: self-evolution trajectory optimization in multi-step reasoning with llm-based agents")), we view each end-to-end mining run as a mining trajectory and explicitly evolve trajectories rather than relying on unconstrained re-generation from noisy feedback. First, to mitigate local optimization, we introduce a Diversified Planning Initialization that generates multiple complementary research directions, yielding broad initial coverage in the hypothesis space. Second, to support controllable refinement and reliable reuse of validated experience, QuantaAlpha performs self-evolution via trajectory-level mutation and crossover. Mutation performs targeted revision by localizing the failure-causing step via self-reflection and rewriting only the corresponding segment, while keeping the rest of the trajectory intact. Crossover recombines complementary segments from high-reward parents to reuse validated hypothesis structures, construction patterns, and repair behaviors. We further apply generation constraints to enforce semantic consistency and constrain complexity and redundancy, preventing drift and crowding. Together, these mechanisms expand exploration while stabilizing refinement under real-market noise and non-stationarity. Extensive experiments on CSI 300 and cross-market transfer to CSI 500 and S&P 500 demonstrate consistent improvements in predictive power and strategy performance over strong baselines and prior agentic systems.

## 2 Related Work

##### Agents in Finance

Recent advances in financial LLMs (Liu et al., [2023](https://arxiv.org/html/2602.07085v1#bib.bib29 "Fingpt: democratizing internet-scale data for financial large language models"), [2025](https://arxiv.org/html/2602.07085v1#bib.bib27 "Fin-r1: a large language model for financial reasoning through reinforcement learning")) and evaluation benchmarks (Guo et al., [2025](https://arxiv.org/html/2602.07085v1#bib.bib30 "Fineval: a chinese financial domain knowledge evaluation benchmark for large language models"); Tang et al., [2025a](https://arxiv.org/html/2602.07085v1#bib.bib32 "Finmmr: make financial numerical reasoning more multimodal, comprehensive, and challenging")) have substantially expanded the scope of automated financial reasoning.
Building on these foundations, a growing line of work explores how agentic systems (Li et al., [2025a](https://arxiv.org/html/2602.07085v1#bib.bib28 "Investorbench: a benchmark for financial decision-making tasks with llm-based agent"); Yang et al., [2026](https://arxiv.org/html/2602.07085v1#bib.bib31 "FinVault: benchmarking financial agent safety in execution-grounded environments")) can move beyond financial understanding toward decision-oriented research workflows, including factor discovery and trading analysis.
In this context, the pursuit of alpha factors has evolved from manual engineering and heuristic search toward LLM-driven closed-loop discovery Li et al. ([2024b](https://arxiv.org/html/2602.07085v1#bib.bib25 "Can large language models mine interpretable financial factors more effectively? a neural-symbolic factor mining agent model")); Shi et al. ([2025b](https://arxiv.org/html/2602.07085v1#bib.bib22 "Navigating the alpha jungle: an llm-powered mcts framework for formulaic factor mining")); Chen et al. ([2025](https://arxiv.org/html/2602.07085v1#bib.bib23 "AlphaSAGE: structure-aware alpha mining via gflownets for robust exploration")); Wang et al. ([2025](https://arxiv.org/html/2602.07085v1#bib.bib24 "Alpha-gpt: human-ai interactive alpha mining for quantitative investment")).
Beyond search optimization, recent efforts emphasize workflow systematization. RD-Agent Li et al. ([2025d](https://arxiv.org/html/2602.07085v1#bib.bib5 "R&D-agent-quant: a multi-agent framework for data-centric factors and model joint optimization")) proposes a multi-agent framework that decouples the pipeline into research and development stages, enabling data-centric joint optimization of factors and models. To address market non-stationarity, AlphaForge Shi et al. ([2025a](https://arxiv.org/html/2602.07085v1#bib.bib6 "Alphaforge: a framework to mine and dynamically combine formulaic alpha factors")) focuses on the dynamic combination of mined factors,
while Alphafin Li et al. ([2024a](https://arxiv.org/html/2602.07085v1#bib.bib7 "Alphafin: benchmarking financial analysis with retrieval-augmented stock-chain framework")) and AlphaEval Ding et al. ([2025](https://arxiv.org/html/2602.07085v1#bib.bib8 "Alphaeval: a comprehensive and efficient evaluation framework for formula alpha mining")) establish standardized, task-oriented protocols for reproducible evaluation. Despite these advances, trading constraints (e.g., turnover, complexity) remain largely post-hoc filters rather than intrinsic objectives, leading to suboptimal generalization and interpretability in live trading.

##### Self-Evolving Agents

Self-evolving agents Fang et al. ([2025](https://arxiv.org/html/2602.07085v1#bib.bib20 "A comprehensive survey of self-evolving ai agents: a new paradigm bridging foundation models and lifelong agentic systems")); Zhai et al. ([2025](https://arxiv.org/html/2602.07085v1#bib.bib16 "Agentevolver: towards efficient self-evolving agent system")); Lin et al. ([2025](https://arxiv.org/html/2602.07085v1#bib.bib17 "Se-agent: self-evolution trajectory optimization in multi-step reasoning with llm-based agents")); Zhang et al. ([2026](https://arxiv.org/html/2602.07085v1#bib.bib26 "EvoFSM: controllable self-evolution for deep research with finite state machines")) represent a paradigm shift from static instruction-following to autonomous learning through interacting with environment.
AlphaEvolve Novikov et al. ([2025](https://arxiv.org/html/2602.07085v1#bib.bib9 "AlphaEvolve: a coding agent for scientific and algorithmic discovery")) demonstrates a coding-centric evolution where the agent employs evolutionary resampling to autonomously generate algorithms for scientific discovery. Building on this, CSE Hu et al. ([2026](https://arxiv.org/html/2602.07085v1#bib.bib10 "Controlled self-evolution for algorithmic code optimization")) introduces controllable self-evolution, facilitating a critical transition from stochastic generation to feedback-driven evolution.
The financial domain adapts this self-evolutionary framework to handle non-stationary and high-dimensional data. Research has converged on multi-agent coordination and structured feedback to guide evolution Li et al. ([2025b](https://arxiv.org/html/2602.07085v1#bib.bib18 "Hedgeagents: a balanced-aware multi-agent financial trading system")). TradingAgents Xiao et al. ([2024](https://arxiv.org/html/2602.07085v1#bib.bib3 "TradingAgents: multi-agents llm financial trading framework")) and FactorMAD Duan et al. ([2025](https://arxiv.org/html/2602.07085v1#bib.bib15 "FactorMAD: a multi-agent debate framework based on large language models for interpretable stock alpha factor mining")) utilize institutional-style debates to refine trading hypotheses, while QuantAgents Li et al. ([2025c](https://arxiv.org/html/2602.07085v1#bib.bib11 "QuantAgents: towards multi-agent financial system via simulated trading")) and ATLAS Papadakis et al. ([2025](https://arxiv.org/html/2602.07085v1#bib.bib12 "ATLAS: adaptive trading with llm agents through dynamic prompt optimization and multi-agent coordination")) incorporate simulated trading performance as a reward signal for dynamic prompt optimization. To ensure consistency over long horizons, FinMem Yu et al. ([2025](https://arxiv.org/html/2602.07085v1#bib.bib13 "Finmem: a performance-enhanced llm trading agent with layered memory and character design")) and FinCon Yu et al. ([2024](https://arxiv.org/html/2602.07085v1#bib.bib14 "Fincon: a synthesized llm multi-agent system with conceptual verbal reinforcement for enhanced financial decision making")) leverage hierarchical memory and conceptual reinforcement to retain and refine high-level trading experience.
Despite these advancements, the transition of self-evolving agents to finance is hindered by the low signal-to-noise ratio and non-stationary. To mitigate this, our QuantaAlpha employs stable optimization units with mutation and crossover operators, ensuring a robust, traceable evolution path through structured archiving of iteration logic.

## 3 Problem Setup

##### Alpha Mining

The alpha mining task aims to learn an alpha factor ff from a market feature tensor 𝐗∈ℝN×T×D\mathbf{X}\in\mathbb{R}^{N\times T\times D} for a stock universe 𝒮={s1,…,sN}\mathcal{S}=\{s\_{1},\ldots,s\_{N}\} and a time horizon 𝒯={t1,…,tT}\mathcal{T}=\{t\_{1},\ldots,t\_{T}\}.
At each time t∈𝒯t\in\mathcal{T}, the factor produces a signal from the feature slice 𝐗t∈ℝN×D\mathbf{X}\_{t}\in\mathbb{R}^{N\times D} that is used to predict the cross-sectional return 𝐲t+1∈ℝN\mathbf{y}\_{t+1}\in\mathbb{R}^{N}.
In notation, an alpha can be written as f​(𝐗t)→𝐲t+1f(\mathbf{X}\_{t})\rightarrow\mathbf{y}\_{t+1}, where 𝐲t+1\mathbf{y}\_{t+1} denotes the realized returns at time t+1t+1. Accordingly, we formulate alpha mining as the following optimization problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | f∗=arg⁡maxf∈ℱ⁡ℒ​(f​(𝐗),𝐲)−λ​ℛ​(f),f^{\*}=\arg\max\_{f\in\mathcal{F}}\ \mathcal{L}\big(f(\mathbf{X}),\mathbf{y}\big)-\lambda\mathcal{R}(f), |  | (1) |

where ℱ\mathcal{F} denotes the space of all possible factor expressions, 𝐲\mathbf{y} is the ground-truth return target (e.g., next-day returns), ℒ​(⋅)\mathcal{L}(\cdot) measures predictive effectiveness, ℛ​(⋅)\mathcal{R}(\cdot) is a regularization term that encourages simplicity and novelty of the expression, and λ\lambda balances utility and regularization.

##### Alpha Mining Trajectory

Distinct from purely data-driven pipelines, we introduce market hypotheses h∈ℋh\in\mathcal{H} to guide LLM-based factor construction.
Each alpha mining run follows an end-to-end workflow from hypothesis generation to factor generation and backtesting evaluation (see Section [4.1](https://arxiv.org/html/2602.07085v1#S4.SS1 "4.1 Alpha Mining Process ‣ 4 Method ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining")).
We represent each run by a mining trajectory, defined as an ordered sequence τ=(s0,a0,s1,a1,…,sn)\tau=(s\_{0},a\_{0},s\_{1},a\_{1},\ldots,s\_{n}), where s0s\_{0} denotes the initial mining context (e.g., market context and optional user-provided seeds), aia\_{i} is the action taken at step ii by the multi-agent system, and sns\_{n} is the terminal state containing the evaluated result of this run. The quality of a trajectory is measured by its terminal reward:

|  |  |  |  |
| --- | --- | --- | --- |
|  | R​(τ)=ℒ​(fτ​(𝐗),𝐲)−λ​ℛ​(fτ),R(\tau)=\mathcal{L}\big(f\_{\tau}(\mathbf{X}),\mathbf{y}\big)-\lambda\mathcal{R}(f\_{\tau}), |  | (2) |

where fτf\_{\tau} denotes the factor produced by trajectory τ\tau.

##### Objective

Our objective is to find a trajectory generation mechanism π\pi for the multi-agent system that maximizes the expected terminal reward of the generated mining trajectory:

|  |  |  |  |
| --- | --- | --- | --- |
|  | π∗=arg⁡maxπ⁡𝔼τ∼π​[R​(τ)],\pi^{\*}=\arg\max\_{\pi}\ \mathbb{E}\_{\tau\sim\pi}\bigl[R(\tau)\bigr], |  | (3) |

where τ∼π\tau\sim\pi denotes the trajectory induced by repeatedly applying π\pi from the initial state s0s\_{0}.

## 4 Method

As illustrated in Figure [3](https://arxiv.org/html/2602.07085v1#S4.F3 "Figure 3 ‣ 4 Method ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining"), our approach treats alpha mining as an agentic research workflow rather than a one-shot factor construction procedure.
Given market context and user-provided seeds, a multi-agent system produces a complete mining trajectory that records hypothesis generation, controllable factor construction, code implementation, and backtesting-based evaluation.
We first describe the end-to-end mining workflow that instantiates and evaluates a single trajectory (Section [4.1](https://arxiv.org/html/2602.07085v1#S4.SS1 "4.1 Alpha Mining Process ‣ 4 Method ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining")).
Building on these evaluated trajectories, we then introduce an evolutionary optimization scheme that iteratively improves mining quality via a self-evolution process (Section [4.2](https://arxiv.org/html/2602.07085v1#S4.SS2 "4.2 Evolutionary Alpha Mining ‣ 4 Method ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining")).

![Refer to caption](images/overview.jpg)


Figure 3: Overview of the QuantaAlpha framework. Our approach consists of four core components: (A) Diversified Planning Initialization to generate candidate hypotheses, (B) Factor Realization that iteratively instantiates hypotheses into executable factors with constraint gating, (C) Self-Evolution that applies mutation and crossover over evaluated trajectories, and (D) A Final Factor Pool that consolidates validated effective factors.

### 4.1 Alpha Mining Process

A standalone alpha mining process involves a sequential progression starting from hypothesis generation, followed by factor creation and concluding with backtesting-based evaluation. We translate this process into the collaborative efforts of multiple agents, each responsible for a specific task at different stages of the workflow.

#### 4.1.1 Hypothesis Generation

We use the idea agent 𝒜​i\mathcal{A}{i} to generate market hypotheses via structured knowledge integration. Conditioned on (i) observations from current market conditions or previous mining trajectories, (ii) domain priors from financial theories and empirical evidence, and (iii) parametric specifications (e.g., “10-day high/low”), 𝒜​i\mathcal{A}{i} produces actionable hypotheses that describe candidate market mechanisms and serve as the input to subsequent factor generation.

#### 4.1.2 Controllable Factor Construction

To effectively instantiate hypothesis-driven factors, we need a robust mechanism to align implementations with domain hypotheses. However, directly generating factor code is brittle, often suffering from syntax errors, dependency mismatches, and semantic drift, causing a mismatch between the code and the hypothesis.To address these limitations, We introduce an intermediate symbolic representation based on a standardized operator library 𝒪\mathcal{O} and an Abstract Syntax Tree (AST). This abstraction bridges high-level market intent and low-level implementation, enabling controllable construction, structural validation, and reliable compilation.

##### Factor Generation

Given a hypothesis h∈ℋh\in\mathcal{H} and raw features 𝒳\mathcal{X}, the factor agent 𝒜f\mathcal{A}\_{f} generates a symbolic expression f∈ℱf\in\mathcal{F} over the operator library and parses it into an AST as the intermediate representation. Concretely, it first maps hh to a structured semantic description dd that formalizes the intended mechanism into discrete operators, while concurrently instantiating operational parameters—such as look-back windows and thresholds—from either prescribed parameters in hh or heuristic defaults anchored in domain expertise.
Conditioned on dd, the agent then assembles an operator composition into a symbolic expression ff and parses it into an AST, denoted as T​(f)T(f). In T​(f)T(f), leaf nodes bind to raw feature fields (e.g., $high, $volume) and internal nodes correspond to operator instances from 𝒪\mathcal{O} (e.g., TS\_MIN(⋅\cdot), SMA(⋅\cdot), RANK(⋅)(\cdot)), thereby rendering the computational dependencies and data flow fully transparent.
Finally, the agent translates the validated symbolic form into executable code cc via compilation; when compilation fails due to implementation issues, an LLM-based repair step is triggered to regenerate a consistent implementation while preserving the semantics of ff. This design ensures that code generation remains anchored to an explicit symbolic specification rather than unconstrained free-form generation.

##### Consistency Verification

We enforce semantic consistency across representations to prevent drift during generation. Specifically, we apply an LLM-based verifier to assess (i) alignment among the hypothesis hh, semantic description dd, and symbolic expression ff, and (ii) faithfulness between the symbolic definition ff and the generated code cc. The verifier returns a consistency decision under fixed criteria. If it fails, we rewrite the inconsistent component(s) by regenerating dd and ff or repairing cc until the check passes or a maximum retry budget is reached.

##### Complexity and Redundancy Control

We further regularize factor generation with explicit structural constraints to promote parsimony and novelty. For complexity, we compute

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞​(f)=α1⋅S​L​(f)+α2⋅P​C​(f)+α3⋅log⁡(1+|Ff|),\mathcal{C}(f)=\alpha\_{1}\cdot SL(f)+\alpha\_{2}\cdot PC(f)+\alpha\_{3}\cdot\log\!\bigl(1+|F\_{f}|\bigr), |  | (4) |

where S​L​(f)SL(f) measures symbolic length, P​C​(f)PC(f) counts free parameters (e.g., window sizes), and FfF\_{f} is the set of raw features used by ff. For redundancy, we quantify structural similarity via AST matching. Given two factors fif\_{i} and fjf\_{j} with ASTs T​(fi)T(f\_{i}) and T​(fj)T(f\_{j}), we define s​(fi,fj)s(f\_{i},f\_{j}) as the size of their largest common isomorphic subtree:

|  |  |  |  |
| --- | --- | --- | --- |
|  | s​(fi,fj)=maxSi⊆T​(fi),Sj⊆T​(fj),Si≅Sj⁡|V​(Si)|.s(f\_{i},f\_{j})=\max\_{\begin{subarray}{c}S\_{i}\subseteq T(f\_{i}),S\_{j}\subseteq T(f\_{j}),S\_{i}\cong S\_{j}\end{subarray}}|V(S\_{i})|. |  | (5) |

Here, SiS\_{i} and SjS\_{j} range over subtrees of T​(fi)T(f\_{i}) and T​(fj)T(f\_{j}), respectively, Si≅SjS\_{i}\cong S\_{j} denotes subtree isomorphism, and |V​(Si)||V(S\_{i})| is the number of nodes in SiS\_{i}. For a candidate factor ff, we compute its maximum similarity against an existing alpha zoo 𝒵\mathcal{Z} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​(f)=maxϕ∈𝒵⁡s​(f,ϕ).S(f)=\max\_{\phi\in\mathcal{Z}}s(f,\phi). |  | (6) |

We reject and rewrite any factor that violates the prescribed complexity or redundancy limits, promoting parsimonious generation while avoiding near-duplicate structures.

#### 4.1.3 Factor Evaluation

The evaluation agent 𝒜e\mathcal{A}\_{e} assesses factors via a standardized backtesting system. The protocol covers three complementary aspects: predictive capability metrics for forecasting effectiveness, return performance metrics for profit-generating potential under a fixed execution setting, and risk control metrics for stability and robustness across market conditions. Beyond factor scoring, the agent maintains an evaluation history that records outcomes and summarizes systematic patterns among successful and failed factors.

### 4.2 Evolutionary Alpha Mining

We improve alpha discovery via iterative optimization over mining trajectories. Starting from user-provided seed factors, we generate a diversified set of initial hypotheses. We then run the end-to-end mining workflow in Section [4.1](https://arxiv.org/html/2602.07085v1#S4.SS1 "4.1 Alpha Mining Process ‣ 4 Method ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining") to turn each hypothesis into an evaluated mining trajectory, forming an initial trajectory pool 𝒯0={τ10,τ20,…,τNi​n​i​t0}\mathcal{T}\_{0}=\{\tau\_{1}^{0},\tau\_{2}^{0},\ldots,\tau\_{N\_{init}}^{0}\}. We then apply an iterative evolution process to obtain progressively improved factors.

#### 4.2.1 Diversified Planning Initialization

Let 𝒵0\mathcal{Z}\_{0} denote the user-provided seed factors (or seed ideas).
We employ an initialization agent 𝒜0\mathcal{A}\_{0} to propose a diversified set of initial hypotheses ℋ0={h10,…,hNi​n​i​t0}\mathcal{H}^{0}=\{h^{0}\_{1},\ldots,h^{0}\_{N\_{init}}\}. The agent is instructed to maximize complementarity among hypotheses at both semantic and structural levels, e.g., varying signal sources (price vs. volume), time scales (short-term vs. long-term), and mechanism types (momentum vs. mean-reversion or regime-conditioned triggers). For each hi0∈ℋ0h^{0}\_{i}\in\mathcal{H}^{0}, we run the mining workflow in Section [4.1](https://arxiv.org/html/2602.07085v1#S4.SS1 "4.1 Alpha Mining Process ‣ 4 Method ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining") and obtain a mining trajectory τi0\tau^{0}\_{i}.
This diversified initialization expands the effective search frontier by providing broad starting coverage in the hypothesis space. As a result, the subsequent evolutionary process can explore multiple promising regions in parallel, significantly reducing the risk of premature convergence to a suboptimal local optimum.

#### 4.2.2 Self-Evolution

The goal of self-evolutionary updates is to guide the alpha mining system to search for better trajectories based on existing ones. Specifically, we apply trajectory-level operators to existing mining trajectories to generate improved trajectories as demonstrations. These demonstrations provide imitation learning priors that bias subsequent trajectory generation toward effective decisions. In practice, we instantiate the update with two evolutionary primitives, Mutation and Crossover, which revise a single trajectory or recombine complementary sub-trajectories, respectively. Each iteration ii yields a new trajectory generation 𝒯i\mathcal{T}\_{i}, and factor quality improves progressively across iterations (see Figure [7](https://arxiv.org/html/2602.07085v1#S5.F7 "Figure 7 ‣ Case Study Setup ‣ 5.5 Case Study ‣ Evolutionary Alpha Mining Efficiency ‣ 5.4 More Analysis ‣ Ablation of Consistency, Complexity, and Redundancy Controls ‣ 5.3 Ablation Study ‣ 5.2 Main Results ‣ Baselines ‣ 5.1 Experimental Setup ‣ 5 Experiments ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining") in Appendix for a case study).

##### Mutation

Given a mining trajectory τ∈𝒯i−1\tau\in\mathcal{T}\_{i-1}, the primitive first performs self-reflection to diagnose sub-optimal decision node that most significantly accounts for the low terminal reward,
denoted by an index k∈{0,…,n−1}k\in\{0,\ldots,n-1\}.
We then rewrite only the localized action (or a short local segment) while keeping the remaining steps unchanged:

|  |  |  |  |
| --- | --- | --- | --- |
|  | τc​h​i​l​d=(s0,a0,…,sk,Refine​(ak),sk+1′,ak+1′,…,sn′),\tau\_{child}=\big(s\_{0},a\_{0},\ldots,s\_{k},\mathrm{Refine}(a\_{k}),s\_{k+1}^{\prime},a\_{k+1}^{\prime},\ldots,s\_{n}^{\prime}\big), |  | (7) |

where the prefix up to sks\_{k} is frozen, and the remaining steps are regenerated by the agent conditioned on this fixed prefix to preserve trajectory coherence. Depending on the localized fault, the rewrite may update the hypothesis, the symbolic expression under the operator library, or the compiled code, and can introduce mechanism-level changes such as altering the time scale, or adding regime conditions.

##### Crossover

Crossover aims to exploit and inherit validated components by recombining complementary sub-trajectories from high-quality parents. At iteration i−1i-1, we select a parent subset 𝒫i−1⊆𝒯i−1\mathcal{P}\_{i-1}\subseteq\mathcal{T}\_{i-1} based on trajectory reward (Eq. [2](https://arxiv.org/html/2602.07085v1#S3.E2 "Equation 2 ‣ Alpha Mining Trajectory ‣ 3 Problem Setup ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining")). Given kk parent trajectories τ(1),…,τ(k)∈𝒫i−1\tau^{(1)},\ldots,\tau^{(k)}\in\mathcal{P}\_{i-1}, Crossover synthesizes a new child trajectory by composing high-performing segments from different parents:

|  |  |  |  |
| --- | --- | --- | --- |
|  | τchild=Crossover​(τ(1),…,τ(k)).\tau\_{\mathrm{child}}=\mathrm{Crossover}\big(\tau^{(1)},\ldots,\tau^{(k)}\big). |  | (8) |

Operationally, the primitive identifies specific trajectory segments that consistently contribute to high cumulative rewards—such as hypothesis templates, factor construction patterns, or strategic repair actions—and merges them into a single, highly coherent sequence.
This recombination mimics the human practice of combining complementary strengths from different solutions, while providing a more credible lineage by explicitly inheriting decisions that have been validated in previously successful trajectories.

## 5 Experiments

Table 1: 
Performance comparison of different methods on CSI 300.
We report both factor predictive power and strategy-level performance metrics, where higher↑\uparrow values indicate better performance for all metrics (with the exception of MDD).
For each method category, the best result in each column is highlighted in bold,
while the second-best result is underlined.
Across all methods, the overall best-performing method is highlighted with a light blue background.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Methods | | Factor Predictive Power | | | | Strategy Performance | | | |
| IC | ICIR | Rank IC | Rank ICIR | IR (SHR\*) | CR | ARR (%) | MDD (%)↓\downarrow |
| \rowcolor[RGB]230, 230, 230    Classical Factor Mining | | | | | | | | | |
| Machine Learning | Linear | 0.0155 | 0.1174 | 0.0368 | 0.2834 | -0.3078 | -0.1407 | -2.67 | 18.97 |
| XGBoost | 0.0175 | 0.1336 | 0.0420 | 0.3417 | -0.5280 | -0.1488 | -4.24 | 28.50 |
| CatBoost | 0.0162 | 0.1203 | 0.0405 | 0.3289 | -0.2807 | -0.1077 | -2.30 | 21.35 |
| LightGBM | 0.0247 | 0.2055 | 0.0423 | 0.3726 | 0.0092 | 0.0032 | 0.07 | 21.80 |
| MLP | 0.0321 | 0.2780 | 0.0438 | 0.4088 | 0.1716 | 0.0804 | 1.46 | 18.15 |
| DoubleEnsemble | 0.0213 | 0.1670 | 0.0408 | 0.3372 | 0.2490 | 0.1233 | 1.85 | 15.00 |
| Deep Learning | GRU | 0.0321 | 0.2603 | 0.0442 | 0.3601 | 0.5302 | 0.2405 | 3.61 | 15.01 |
| Transformer | 0.0331 | 0.2702 | 0.0451 | 0.3801 | 0.4502 | 0.3773 | 5.21 | 13.81 |
| LSTM | 0.0331 | 0.2502 | 0.0451 | 0.3503 | 0.6802 | 0.4058 | 6.01 | 14.81 |
| TRA | 0.0421 | 0.3402 | 0.0511 | 0.4203 | 1.0502 | 0.8002 | 6.81 | 8.51 |
| Factor Libraries | Alpha158(20) | 0.0051 | 0.0329 | 0.0184 | 0.1177 | 0.5044 | 0.2087 | 4.63 | 22.19 |
| Alpha158 | 0.0131 | 0.0817 | 0.0334 | 0.2119 | 0.4099 | 0.2620 | 2.66 | 10.15 |
| Alpha360 | 0.0105 | 0.0636 | 0.0306 | 0.1889 | 0.6009 | 0.3550 | 4.09 | 11.52 |
| \rowcolor[RGB]230, 230, 230    LLM-based Agentic Factor Mining | | | | | | | | | |
| RD-Agent | Qwen3-235B | 0.0352 | 0.2850 | 0.0485 | 0.3950 | 0.6502 | 0.3591 | 7.20 | 20.05 |
| Deepseek-V3.2 | 0.0401 | 0.3250 | 0.0522 | 0.4250 | 0.8202 | 0.4332 | 7.81 | 18.03 |
| Gemini-3-pro-preview | 0.0481 | 0.3900 | 0.0583 | 0.4750 | 1.0202 | 0.5499 | 8.81 | 16.02 |
| Claude-4.5-sonnet | 0.0527 | 0.4250 | 0.0623 | 0.5050 | 1.2202 | 0.6488 | 9.81 | 15.12 |
| GPT-5.2 | 0.0531 | 0.4300 | 0.0633 | 0.5150 | 1.2502 | 0.6687 | 9.91 | 14.82 |
| AlphaAgent | Qwen3-235B | 0.0952 | 0.6632 | 0.1019 | 0.6471 | 2.1053 | 1.5945 | 15.10 | 9.47 |
| Deepseek-V3.2 | 0.0955 | 0.6637 | 0.0919 | 0.6450 | 1.9230 | 1.4746 | 14.51 | 9.84 |
| Gemini-3-pro-preview | 0.0804 | 0.5366 | 0.0784 | 0.5290 | 1.7821 | 1.4729 | 14.11 | 9.58 |
| Claude-4.5-sonnet | 0.1092 | 0.7718 | 0.1062 | 0.7596 | 2.2739 | 2.0246 | 16.48 | 8.14 |
| GPT-5.2 | 0.0966 | 0.6344 | 0.0942 | 0.6237 | 1.9328 | 1.2056 | 15.54 | 12.89 |
| QuantaAlpha | Qwen3-235B | 0.1252 | 0.8672 | 0.1226 | 0.8577 | 2.6114 | 2.2859 | 20.55 | 8.99 |
| Deepseek-V3.2 | 0.1338 | 0.8533 | 0.1300 | 0.8304 | 2.8797 | 2.6007 | 23.77 | 9.14 |
| Gemini-3-pro-preview | 0.1124 | 0.7391 | 0.1086 | 0.7205 | 2.5189 | 2.1503 | 20.32 | 9.45 |
| Claude-4.5-sonnet | 0.1111 | 0.6374 | 0.1077 | 0.6211 | 2.6459 | 3.2615 | 22.70 | 6.96 |
| GPT-5.2 | 0.1501 | 0.9110 | 0.1465 | 0.8909 | 3.3251 | 3.4774 | 27.75 | 7.98 |

### 5.1 Experimental Setup

##### Datasets and Metrics

We conduct experiments on the CSI 300 dataset, which covers 300 large-cap A-share stocks in the Chinese market. We adopt a chronological split with training (Jan. 1, 2016 to Dec. 31, 2020), validation (Jan. 1, 2021 to Dec. 31, 2021), and testing (Jan. 1, 2022 to Dec. 26, 2025). We evaluate performance from two complementary perspectives. Factor predictive power is measured by Information Coefficient (IC), IC Information Ratio (ICIR), Rank IC, and Rank ICIR. Strategy performance is measured by Annualized Return (ARR), Information Ratio (IR), Maximum Drawdown (MDD), and Calmar Ratio (CR). Further details are provided in Appendix [A.1](https://arxiv.org/html/2602.07085v1#A1.SS1 "A.1 Evaluation Metrics ‣ Appendix A Experiment Settings ‣ Acknowledgments ‣ 6 Conclusion ‣ Iteration Convergence ‣ 5.5 Case Study ‣ Evolutionary Alpha Mining Efficiency ‣ 5.4 More Analysis ‣ Ablation of Consistency, Complexity, and Redundancy Controls ‣ 5.3 Ablation Study ‣ 5.2 Main Results ‣ Baselines ‣ 5.1 Experimental Setup ‣ 5 Experiments ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").

##### Baselines

We compare QuantaAlpha against four baseline categories: traditional machine learning models, deep learning time-series models, classical factor libraries, and LLM-based factor research agents, including RD-Agent and AlphaAgent. More details are provided in Appendix [A.3](https://arxiv.org/html/2602.07085v1#A1.SS3 "A.3 Baselines ‣ Appendix A Experiment Settings ‣ Acknowledgments ‣ 6 Conclusion ‣ Iteration Convergence ‣ 5.5 Case Study ‣ Evolutionary Alpha Mining Efficiency ‣ 5.4 More Analysis ‣ Ablation of Consistency, Complexity, and Redundancy Controls ‣ 5.3 Ablation Study ‣ 5.2 Main Results ‣ Baselines ‣ 5.1 Experimental Setup ‣ 5 Experiments ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").

### 5.2 Main Results

Table [5](https://arxiv.org/html/2602.07085v1#S5 "5 Experiments ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining") reports the main results on the CSI 300 market over a four-year evaluation period. QuantaAlpha outperforms all baselines on both factor predictive power and strategy-level performance. Using GPT-5.2, QuantaAlpha achieves the best IC at 0.1501, delivers an ARR of 27.75%, and maintains a low MDD of 7.98%. From a real-world perspective, this performance indicates that the mined factors can support production trading under standard risk controls, rather than being artifacts of backtest noise. Similarly, we observe consistent gains across different base models, suggesting that the improvements are robust rather than model-specific.

Compared with RD-Agent, QuantaAlpha and AlphaAgent both incorporate generation-stage regularization, and this is reflected in stronger predictive power and strategy performance. Under GPT-5.2, QuantaAlpha improves IC by 0.0970 and ARR by 17.84% relative to RD-Agent while reducing MDD by 6.84%, suggesting that constraining hypothesis-to-factor construction with explicit intermediate representations and verification effectively reduces semantic drift and improves implementation reliability. Beyond these constraints, QuantaAlpha further improves upon AlphaAgent by 0.0535 IC and 12.21% ARR while reducing MDD by 4.91%, highlighting the added value of trajectory-centric self-evolution: mutation broadens exploration via mechanism-level variations, while crossover reuses validated trajectory segments and repair strategies, jointly increasing the yield and stability of high-quality factors under non-stationary market dynamics.

![Refer to caption](x1.png)


Figure 4: Ablation study of semantic consistency, complexity, and redundancy controls.

### 5.3 Ablation Study

##### Ablation of Evolutionary Mining Components

We conduct an ablation study to quantify the contribution of three components in evolutionary alpha mining: diversified planning initialization, trajectory mutation, and trajectory crossover. The results are summarized in Table [2](https://arxiv.org/html/2602.07085v1#S5.T2 "Table 2 ‣ Ablation of Evolutionary Mining Components ‣ 5.3 Ablation Study ‣ 5.2 Main Results ‣ Baselines ‣ 5.1 Experimental Setup ‣ 5 Experiments ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining"). Removing *planning* yields only marginal changes in IC and Rank IC, but substantially degrades strategy-level outcomes, with ARR decreasing by 7.78% and MDD increasing by 2.73%. This indicates that diversified initialization primarily improves the search frontier by providing broader and less correlated starting hypotheses, which stabilizes subsequent evolution. In contrast, removing *mutation* causes the largest drop in predictive power, decreasing IC by 0.0292 and Rank IC by 0.0284, and also leads to the largest reduction in ARR by 9.81%. This highlights mutation as the primary driver of effective exploration and trajectory repair, enabling the system to escape suboptimal regions and correct failure modes discovered during mining. Meanwhile, removing *crossover* leads to a smaller but consistent degradation. This supports the role of crossover in exploiting and inheriting complementary high-performing trajectory segments, improving efficiency and stability by recombining validated patterns from successful trajectories.

Table 2: Ablation study of evolutionary mining components.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Method | Key Metrics | | | |
| IC | Rank IC | ARR   (%) | MDD (%) ↓\downarrow |
| QuantaAlpha | 0.1493 | 0.1458 | 28.99 | 9.42 |
| Q - *w/o* Planning | 0.1488-0.0005 | 0.1452-0.0006 | 21.21-7.78 | 12.15+2.73 |
| Q - *w/o* Mutation | 0.1201-0.0292 | 0.1174-0.0284 | 19.18-9.81 | 9.85+0.43 |
| Q - *w/o* Crossover | 0.1423-0.0070 | 0.1381-0.0077 | 26.17-2.82 | 10.63+1.21 |

##### Ablation of Consistency, Complexity, and Redundancy Controls

We ablate three controls during factor generation that gate rewriting, including semantic consistency verification, complexity regularization, and redundancy filtering. As shown in Figure [4](https://arxiv.org/html/2602.07085v1#S5.F4 "Figure 4 ‣ 5.2 Main Results ‣ Baselines ‣ 5.1 Experimental Setup ‣ 5 Experiments ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining"), disabling any single control consistently degrades performance, confirming that each contributes non-trivially to robust factor generation. The *consistency* control prevents semantic drift between the hypothesis, symbolic specification, and implementation. The *complexity* control improves robustness by discouraging overly complex expressions that generalize poorly, and its removal leads to the most pronounced degradation at the strategy level, with the annualized excess return dropping by 8.44% and the maximum drawdown increasing by 2.57%. The *redundancy* control preserves exploration by filtering near-duplicate structures and mitigating factor crowding. Disabling all three yields the largest degradation, indicating that these controls are complementary and jointly needed for reliable generation.

### 5.4 More Analysis

##### Factor Generalizability

To evaluate factor robustness under significant market distribution shifts, we conduct a zero-shot transfer experiment where the factors mined and selected on CSI 300 are directly deployed on CSI 500 and the S&P 500 without any re-optimization or market-specific adaptation. As shown in Figure [1](https://arxiv.org/html/2602.07085v1#S0.F1 "Figure 1 ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining"), QuantaAlpha demonstrates substantially stronger out-of-distribution generalization than all baselines. A clear divergence emerges around December 2023, when competing methods begin to stagnate under shifts in market microstructure and volatility regimes, whereas QuantaAlpha sustains a stable upward trajectory. By the end of the evaluation period, it reaches a cumulative excess return of roughly 160% on CSI 500 and over 137% on the S&P 500. These results indicate that the discovered factors transfer beyond the source market and retain effectiveness under distribution shifts, rather than relying on market-specific historical patterns.

##### Alpha Decay

Figure [5](https://arxiv.org/html/2602.07085v1#S5.F5 "Figure 5 ‣ Alpha Decay ‣ 5.4 More Analysis ‣ Ablation of Consistency, Complexity, and Redundancy Controls ‣ 5.3 Ablation Study ‣ 5.2 Main Results ‣ Baselines ‣ 5.1 Experimental Setup ‣ 5 Experiments ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining") reports annual IC and Rank IC on the CSI 300 universe from 2021 to 2025. A pronounced performance collapse is observed for the baselines in 2023, coinciding with a major regime shift in the A-share market. The pre-2023 period is dominated by large-cap “core assets”, where institutional trading supports relatively stable trends and makes classical momentum or mean-reversion signals effective. In 2023, the market rotates toward small-cap and thematic stocks, together with higher intraday noise, more frequent overnight gaps, and weaker trend persistence. Baseline methods, whose factor libraries implicitly assume smooth trends and regular reversal patterns, fail to transfer to this out-of-distribution environment. QuantaAlpha, by comparison, maintains strong IC and Rank IC through the regime transition. It discovers more structural factors, such as Mean-Reverting Range Deviation and Overnight Gap Structure, that reflect persistent microstructure effects including volatility clustering and overnight information incorporation. These signals are less sensitive to capitalization style, enabling better temporal generalization.

![Refer to caption](images/figure4.png)


Figure 5: Annual IC and Rank IC comparison on the CSI 300.

Table [3](https://arxiv.org/html/2602.07085v1#S5.T3 "Table 3 ‣ Factor Semantics Aligned with Market Microstructure ‣ 5.4 More Analysis ‣ Ablation of Consistency, Complexity, and Redundancy Controls ‣ 5.3 Ablation Study ‣ 5.2 Main Results ‣ Baselines ‣ 5.1 Experimental Setup ‣ 5 Experiments ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining") provides a factor-level diagnosis of the alpha decay observed in 2023, grounding the analysis jointly in *market style changes*, *factor semantics*, and *empirical factor statistics*.
Rather than enumerating factor formulas, we focus on which information channels remain predictive under the 2022–2023 regime transition and why.

##### Market Style Transition and Its Implications

The CSI 300 market undergoes a pronounced style transition in 2023 relative to the training period (2016–2020).
The earlier regime is dominated by large-cap core assets, with high institutional participation, smooth intraday dynamics, and persistent short-horizon trends. Under such conditions, classical momentum, mean-reversion, and exhaustion-based factors are effective.In 2023, leadership rotates toward small-cap and thematic stocks. This shift is accompanied by increased intraday noise, frequent overnight gaps driven by call auctions, and rapid cross-style liquidity re-allocation. These changes weaken trend persistence and amplify path-dependent noise, directly challenging factor constructions that rely on stable intraday structure or fast mean reversion.

##### Factor Semantics Aligned with Market Microstructure

The empirical contrast between QuantaAlpha (QA) and AlphaAgent (AA) in 2023 reflects differences in the *semantic composition* of their factor libraries.

(i). Overnight and auction information.
Gap-based factors aggregate information released during non-trading hours and price discovery in the opening auction.
As shown in Table [3](https://arxiv.org/html/2602.07085v1#S5.T3 "Table 3 ‣ Factor Semantics Aligned with Market Microstructure ‣ 5.4 More Analysis ‣ Ablation of Consistency, Complexity, and Redundancy Controls ‣ 5.3 Ablation Study ‣ 5.2 Main Results ‣ Baselines ‣ 5.1 Experimental Setup ‣ 5 Experiments ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining"), multiple QA factors from this channel occupy the right tail of the 2023 Rank IC distribution, while maintaining near-complete coverage (Table [4](https://arxiv.org/html/2602.07085v1#S5.T4 "Table 4 ‣ Factor Semantics Aligned with Market Microstructure ‣ 5.4 More Analysis ‣ Ablation of Consistency, Complexity, and Redundancy Controls ‣ 5.3 Ablation Study ‣ 5.2 Main Results ‣ Baselines ‣ 5.1 Experimental Setup ‣ 5 Experiments ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining")). This indicates that overnight information becomes a dominant and stable signal when intraday predictability deteriorates.

Table 3: Representative factors and their performance metrics on the CSI 300 index in 2023.

|  |  |  |  |
| --- | --- | --- | --- |
| Factor (representative) | Rank IC | IC | Interpretation (short) |
| QA — strong performers (overnight/auction, trend-quality, and liquidity re-rating) | | | |
| GapZ10\_Overnight\_vs\_TR | 0.0793 | 0.0335 | Normalized overnight gap magnitude relative to recent true range; captures auction-driven shocks and subsequent adjustment. |
| Gap\_IntradayAcceptanceScore\_20D | 0.0744 | 0.0330 | ‘Acceptance vs. rejection” of an overnight gap using intraday direction, scaled by recent volatility. |
| Gap\_IntradayAcceptance\_VolWeighted\_20D | 0.0606 | 0.0314 | Gap acceptance score weighted by abnormal volume; emphasizes information-rich openings with high participation. |
| CleanTrend\_Continuation\_Score\_RS10\_WVMA5 | 0.0590 | 0.0267 | Trend continuation conditioned on high trend quality (low residual noise) and muted intraday/volume pressure. |
| OrderlyTrend\_x\_Absorption\_10D\_5D\_20D | 0.0465 | 0.0271 | ‘Orderly” short-horizon trend cross-validated by liquidity absorption (high dollar volume with low price impact). |
| QA — weak performers (overly rigid gates or noisy-path proxies under rotation) | | | |
| KineticLength\_AbsRetSum\_Z\_10D | -0.0720 | -0.0246 | Path-length proxy (choppiness): can behave like a noise detector, but may invert under fast style rotation. |
| Drawdown\_Gated\_NegCorr\_60D\_20D\_thr20pct | -0.0282 | -0.0095 | Hard regime gate based on deep drawdown; brittle when drawdowns cluster and cross-sectional regimes shift quickly. |
| HighClose\_Shock\_With\_VolSync\_60\_20 | -0.0274 | -0.0090 | ‘Shock-day” breakout quality (close-in-range, range shock, return–volume sync); sensitive to regime-dependent follow-through. |
| AA — strong performers (exhaustion/climax-style reversals) | | | |
| Exhaustion\_Intensity\_Index\_10D | 0.0323 | 0.0159 | Price displacement over 60D interacted with volume intensity ratio; targets potential exhaustion and reversal. |
| Climax\_Exhaustion\_Intensity | 0.0242 | 0.0160 | Variant using short-horizon volume climax vs. long-horizon baseline; aims to identify capitulation-like turns. |
| Exhaustion\_Volume\_Instability\_Index | 0.0121 | 0.0117 | Trend deviation combined with volume instability; highlights fragile price levels supported by unstable liquidity. |
| AA — weak performers (bottom-fishing under non-stationary liquidity) | | | |
| Relative\_Volume\_Calm\_Reversal | -0.0279 | -0.0188 | ‘Quiet-volume” regimes multiplied by momentum divergence; may fail when liquidity conditions change abruptly. |
| Volume\_Stability\_Momentum\_Divergence\_40D | -0.0247 | -0.0155 | Robust volume-stability proxy (MAD) times momentum spread; sensitive to turnover regime changes. |
| LVR\_Bottom\_Fishing\_20D | -0.0190 | -0.0144 | ‘Bottom-fishing” reversal with intraday rejection and volume surge; vulnerable when reversals are short-lived and crowded. |




Table 4: Summary statistics of annual factor predictability on the CSI 300 index in 2023.

|  |  |  |
| --- | --- | --- |
| Metric | QA | AA |
| Coverage ratio (valid metrics) | 0.98 | 0.80 |
| Share with Rank IC >0>0 | 0.626 | 0.594 |
| Mean Rank IC | 0.0057 | 0.0012 |
| Max Rank IC | 0.0793 | 0.0323 |
| Min Rank IC | -0.0720 | -0.0279 |
| Share with Rank IC >0.03>0.03 | 0.102 | 0.0156 |
| Share with Rank IC >0.05>0.05 | 0.0272 | 0.0000 |
| Mean IC | 0.0044 | 0.0015 |

(ii). Volatility structure and range-based signals.
Range deviation factors conditioned on volatility clustering capture abnormal variability rather than directional trends.
In 2023, these signals remain predictive despite elevated noise, consistent with the persistence of volatility clustering across market styles. Their contribution is reflected in the heavier positive Rank IC tail of QA relative to AA.

(iii). Trend quality and liquidity re-rating.
QA emphasizes trend continuation only when supported by low residual volatility and improving liquidity (e.g., rising dollar volume with limited price impact).
This conditioning filters out noise-driven pseudo-trends prevalent in small-cap rotation, explaining why QA retains a higher fraction of strong-performing factors, whereas raw momentum proxies degrade.

##### Factor Statistics as Supporting Evidence

The factor-level statistics in 2023 provide quantitative support for the semantic interpretation above.
QA achieves substantially higher coverage and a heavier right tail of Rank IC, including a non-trivial share of factors exceeding moderate predictability thresholds, whereas AA exhibits compressed tails and fewer robust signals.
These differences are consistent with the dominance of overnight, volatility-structure, and trend-quality channels under the 2023 market style.

A key distinction is that QA explicitly encourages semantic diversity through its factor mutation mechanism.
By generating and recombining heterogeneous primitives across multiple information channels, QA avoids concentration on a single market hypothesis.
This diversity increases the probability that a subset of factors remains aligned with the prevailing market microstructure after a style transition, thereby mitigating regime-specific alpha decay.
Overall, the 2023 diagnosis indicates that alpha robustness under distribution shift is driven by alignment between market style and factor semantics, supported by sufficient diversity across information channels.
QA’s ability to maintain performance arises not from fitting a specific regime, but from sustaining a broad and adaptive factor population whose predictive subsets persist across market style transitions.

##### Evolutionary Alpha Mining Efficiency

We analyze the iterative dynamics of factor mining by tracking the IC distribution across generation rounds.
As visualized in Figure [6](https://arxiv.org/html/2602.07085v1#S5.F6 "Figure 6 ‣ Evolutionary Alpha Mining Efficiency ‣ 5.4 More Analysis ‣ Ablation of Consistency, Complexity, and Redundancy Controls ‣ 5.3 Ablation Study ‣ 5.2 Main Results ‣ Baselines ‣ 5.1 Experimental Setup ‣ 5 Experiments ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining"), QuantaAlpha consistently maintains the highest IC across all five iterations, indicating that its evolutionary updates improve factor quality more effectively than both AlphaAgent and RD-Agent. Notably, QuantaAlpha exhibits a rapid gain in the early rounds and then remains stable at a high level, suggesting strong sample efficiency in converting early exploration into consistently predictive factors. In addition to the higher mean, QuantaAlpha shows a moderate but persistent spread of IC across rounds, reflecting sustained diversity in the explored factor candidates rather than premature collapse to a narrow region. By comparison, RD-Agent remains lower with relatively homogeneous IC profiles, consistent with weaker exploration and a higher risk of generating crowded signals. AlphaAgent improves over RD-Agent but remains consistently below QuantaAlpha, suggesting that our trajectory-level evolution more efficiently accumulates and reuses successful generation patterns across iterations.

![Refer to caption](images/figu.png)


Figure 6: The evolution of IC over the first five iterations.

### 5.5 Case Study

##### Case Study Setup

To make the evolution process concrete, we present a representative case study and trace how QuantaAlpha updates hypotheses and factors over five iterations. We run QuantaAlpha for a total of 15 iterations on CSI300, using Deepseek-V3.2 as the backbone LLM for all agents. To improve mining throughput, we set the factor-complexity constraints to symbol length ≤200\leq 200 and base features ≤4\leq 4. Each iteration consists of two phases: a Mutation phase followed by a Crossover phase.At the end of each iteration, we maintain a global high-quality factor pool using all factors generated up to that iteration. The maintenance rule is greedy and RankIC-driven: we sort all candidate factors by RankIC (descending) and add them into the pool in order, subject to a redundancy constraint. A factor is admitted only if its absolute correlation with every factor already in the pool is below 0.7. The pool size is capped at 50% of the total number of mined factors up to the current iteration.

![Refer to caption](x2.png)


Figure 7: A case study of iterative hypothesis and factor updates in QuantaAlpha.

##### Factor Example

Figure [7](https://arxiv.org/html/2602.07085v1#S5.F7 "Figure 7 ‣ Case Study Setup ‣ 5.5 Case Study ‣ Evolutionary Alpha Mining Efficiency ‣ 5.4 More Analysis ‣ Ablation of Consistency, Complexity, and Redundancy Controls ‣ 5.3 Ablation Study ‣ 5.2 Main Results ‣ Baselines ‣ 5.1 Experimental Setup ‣ 5 Experiments ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining") illustrates how QuantaAlpha refines hypotheses and factor expressions across iterations via the *mutation* and *crossover* phases. The highlighted factors in the figure are therefore representative nodes on different traces across iterations. The first iteration yields interpretable short-term reversal factors. The second broadens the mechanism via volatility-weighted momentum, but increased structural complexity coincides with weaker generalization. Subsequent iterations simplify the expression into a linear additive form, improving drawdown and stabilizing performance. The fifth iteration adds participant-differentiated behavioral signals, incorporating complementary information and further improving predictability. Throughout the evolution, QuantaAlpha maintains a cumulative factor pool. Its predictive performance does not saturate within the first five iterations and only begins to decay after roughly 15 iterations, indicating that the evolution sustains effective improvement over a substantial horizon before diminishing returns emerge.

##### Iteration Convergence

Figure [8](https://arxiv.org/html/2602.07085v1#S5.F8 "Figure 8 ‣ Iteration Convergence ‣ 5.5 Case Study ‣ Evolutionary Alpha Mining Efficiency ‣ 5.4 More Analysis ‣ Ablation of Consistency, Complexity, and Redundancy Controls ‣ 5.3 Ablation Study ‣ 5.2 Main Results ‣ Baselines ‣ 5.1 Experimental Setup ‣ 5 Experiments ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining") illustrates the predictive performance of the factor pool from the fifth iteration onwards. We observe that the predictive performance does not increase linearly with the number of iterations. The strategy’s return capacity and risk control ability are gradually optimized, reaching a balanced high level between return and maximum drawdown around the 11th to 12th iterations. Subsequent additional iterations fail to bring significant performance improvement; instead, they may introduce redundant information through newly generated factors, leading to reduced strategy robustness and deteriorated drawdown performance. Overall, the 11th to 12th iterations (approximately 350 factors in total) represent the optimal trade-off point between return level and risk control effect under this experimental setup.

![Refer to caption](images/iteration.png)


Figure 8: Factor Pool Performance by Iteration.

## 6 Conclusion

We present QuantaAlpha, a self-evolving framework for interpretable alpha mining that formulates factor discovery as a constrained multi-agent research process. Extensive experiments across both Chinese and U.S. equity markets show that QuantaAlpha consistently produces more stable and generalizable factors than all baselines. Beyond empirical performance, QuantaAlpha emphasizes three properties critical for real-world quantitative research: *diversity*, *controllability*, and *trustworthiness*. Diversity is promoted by broad hypothesis exploration and redundancy-aware evolution, improving robustness under non-stationarity; controllability is enabled by symbolic representations and synthesis-time gates that enforce consistency and limit complexity. Trustworthiness is further strengthened by trajectory-level inheritance, where crossover recombines high-performing segments from previously successful trajectories, providing a verifiable lineage of validated mechanisms and repair patterns. Future work will explore extending QuantaAlpha to multi-asset and cross-market settings, incorporating adaptive regime-aware evolution, and integrating the agentic discovery process more tightly with portfolio construction and risk management. More broadly, we believe that agentic evolution provides a promising paradigm for discovery problems in high-noise, non-stationary domains beyond finance.

## Acknowledgments

This work was supported by the National Social Science Fund of China Project under Grant No. 22BTJ031; and the Shanghai Engineering Research Center of Finance Intelligence under Grant No. 19DZ2254600. We acknowledge the technical support from the Qinghai Provincial Key Laboratory of Big Data in Finance and Artificial Intelligence Application Technology.

## References

* B. Chen, H. Ding, N. Shen, J. Huang, T. Guo, L. Liu, and M. Zhang (2025)
  AlphaSAGE: structure-aware alpha mining via gflownets for robust exploration.
  arXiv preprint arXiv:2509.25055.
  Cited by: [§2](https://arxiv.org/html/2602.07085v1#S2.SS0.SSS0.Px1.p1.1 "Agents in Finance ‣ 2 Related Work ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* H. Ding, B. Chen, J. Huang, T. Guo, Z. Mao, G. Shao, L. Zou, L. Liu, and M. Zhang (2025)
  Alphaeval: a comprehensive and efficient evaluation framework for formula alpha mining.
  arXiv preprint arXiv:2508.13174.
  Cited by: [§2](https://arxiv.org/html/2602.07085v1#S2.SS0.SSS0.Px1.p1.1 "Agents in Finance ‣ 2 Related Work ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* Y. Duan, C. Zhang, and J. Li (2025)
  FactorMAD: a multi-agent debate framework based on large language models for interpretable stock alpha factor mining.
  In Proceedings of the 6th ACM International Conference on AI in Finance,
   pp. 605–613.
  Cited by: [§2](https://arxiv.org/html/2602.07085v1#S2.SS0.SSS0.Px2.p1.1 "Self-Evolving Agents ‣ 2 Related Work ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* R. F. Engle (1982)
  Autoregressive conditional heteroscedasticity with estimates of the variance of united kingdom inflation.
  Econometrica: Journal of the econometric society,  pp. 987–1007.
  Cited by: [§1](https://arxiv.org/html/2602.07085v1#S1.p1.1 "1 Introduction ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* E. F. Fama (1965)
  The behavior of stock-market prices.
  The journal of Business 38 (1),  pp. 34–105.
  Cited by: [§1](https://arxiv.org/html/2602.07085v1#S1.p1.1 "1 Introduction ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* J. Fang, Y. Peng, X. Zhang, Y. Wang, X. Yi, G. Zhang, Y. Xu, B. Wu, S. Liu, Z. Li, et al. (2025)
  A comprehensive survey of self-evolving ai agents: a new paradigm bridging foundation models and lifelong agentic systems.
  arXiv preprint arXiv:2508.07407.
  Cited by: [§2](https://arxiv.org/html/2602.07085v1#S2.SS0.SSS0.Px2.p1.1 "Self-Evolving Agents ‣ 2 Related Work ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* X. Guo, H. Xia, Z. Liu, H. Cao, Z. Yang, Z. Liu, S. Wang, J. Niu, C. Wang, Y. Wang, et al. (2025)
  Fineval: a chinese financial domain knowledge evaluation benchmark for large language models.
  In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers),
   pp. 6258–6292.
  Cited by: [§2](https://arxiv.org/html/2602.07085v1#S2.SS0.SSS0.Px1.p1.1 "Agents in Finance ‣ 2 Related Work ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* T. Hu, R. Chen, S. Zhang, J. Yin, M. X. Feng, J. Liu, S. Zhang, W. Jiang, Y. Fang, S. Hu, et al. (2026)
  Controlled self-evolution for algorithmic code optimization.
  arXiv preprint arXiv:2601.07348.
  Cited by: [§2](https://arxiv.org/html/2602.07085v1#S2.SS0.SSS0.Px2.p1.1 "Self-Evolving Agents ‣ 2 Related Work ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* H. Li, Y. Cao, Y. Yu, S. R. Javaji, Z. Deng, Y. He, Y. Jiang, Z. Zhu, K. Subbalakshmi, J. Huang, et al. (2025a)
  Investorbench: a benchmark for financial decision-making tasks with llm-based agent.
  In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
   pp. 2509–2525.
  Cited by: [§2](https://arxiv.org/html/2602.07085v1#S2.SS0.SSS0.Px1.p1.1 "Agents in Finance ‣ 2 Related Work ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* X. Li, Z. Li, C. Shi, Y. Xu, Q. Du, M. Tan, and J. Huang (2024a)
  Alphafin: benchmarking financial analysis with retrieval-augmented stock-chain framework.
  In Proceedings of the 2024 joint international conference on computational linguistics, language resources and evaluation (LREC-COLING 2024),
   pp. 773–783.
  Cited by: [§2](https://arxiv.org/html/2602.07085v1#S2.SS0.SSS0.Px1.p1.1 "Agents in Finance ‣ 2 Related Work ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* X. Li, Y. Zeng, X. Xing, J. Xu, and X. Xu (2025b)
  Hedgeagents: a balanced-aware multi-agent financial trading system.
  In Companion Proceedings of the ACM on Web Conference 2025,
   pp. 296–305.
  Cited by: [§2](https://arxiv.org/html/2602.07085v1#S2.SS0.SSS0.Px2.p1.1 "Self-Evolving Agents ‣ 2 Related Work ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* X. Li, Y. Zeng, X. Xing, J. Xu, and X. Xu (2025c)
  QuantAgents: towards multi-agent financial system via simulated trading.
  arXiv preprint arXiv:2510.04643.
  Cited by: [§2](https://arxiv.org/html/2602.07085v1#S2.SS0.SSS0.Px2.p1.1 "Self-Evolving Agents ‣ 2 Related Work ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* Y. Li, X. Yang, X. Yang, M. Xu, X. Wang, W. Liu, and J. Bian (2025d)
  R&D-agent-quant: a multi-agent framework for data-centric factors and model joint optimization.
  arXiv preprint arXiv:2505.15155.
  Cited by: [§1](https://arxiv.org/html/2602.07085v1#S1.p2.1 "1 Introduction ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining"),
  [§2](https://arxiv.org/html/2602.07085v1#S2.SS0.SSS0.Px1.p1.1 "Agents in Finance ‣ 2 Related Work ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* Z. Li, R. Song, C. Sun, W. Xu, Z. Yu, and J. Wen (2024b)
  Can large language models mine interpretable financial factors more effectively? a neural-symbolic factor mining agent model.
  In Findings of the Association for Computational Linguistics ACL 2024,
   pp. 3891–3902.
  Cited by: [§2](https://arxiv.org/html/2602.07085v1#S2.SS0.SSS0.Px1.p1.1 "Agents in Finance ‣ 2 Related Work ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* J. Lin, Y. Guo, Y. Han, S. Hu, Z. Ni, L. Wang, M. Chen, H. Liu, R. Chen, Y. He, et al. (2025)
  Se-agent: self-evolution trajectory optimization in multi-step reasoning with llm-based agents.
  arXiv preprint arXiv:2508.02085.
  Cited by: [§1](https://arxiv.org/html/2602.07085v1#S1.p4.1 "1 Introduction ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining"),
  [§2](https://arxiv.org/html/2602.07085v1#S2.SS0.SSS0.Px2.p1.1 "Self-Evolving Agents ‣ 2 Related Work ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* X. Liu, G. Wang, H. Yang, and D. Zha (2023)
  Fingpt: democratizing internet-scale data for financial large language models.
  arXiv preprint arXiv:2307.10485.
  Cited by: [§2](https://arxiv.org/html/2602.07085v1#S2.SS0.SSS0.Px1.p1.1 "Agents in Finance ‣ 2 Related Work ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* Z. Liu, X. Guo, F. Lou, L. Zeng, J. Niu, Z. Wang, J. Xu, W. Cai, Z. Yang, X. Zhao, et al. (2025)
  Fin-r1: a large language model for financial reasoning through reinforcement learning.
  arXiv preprint arXiv:2503.16252.
  Cited by: [§2](https://arxiv.org/html/2602.07085v1#S2.SS0.SSS0.Px1.p1.1 "Agents in Finance ‣ 2 Related Work ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* A. Lopez-Lira and Y. Tang (2023)
  Can chatgpt forecast stock price movements? return predictability and large language models.
  arXiv preprint arXiv:2304.07619.
  Cited by: [§1](https://arxiv.org/html/2602.07085v1#S1.p1.1 "1 Introduction ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* A. Novikov, N. Vũ, M. Eisenberger, E. Dupont, P. Huang, A. Z. Wagner, S. Shirobokov, B. Kozlovskii, F. J. Ruiz, A. Mehrabian, et al. (2025)
  AlphaEvolve: a coding agent for scientific and algorithmic discovery.
  arXiv preprint arXiv:2506.13131.
  Cited by: [§2](https://arxiv.org/html/2602.07085v1#S2.SS0.SSS0.Px2.p1.1 "Self-Evolving Agents ‣ 2 Related Work ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* C. Papadakis, A. Dimitriou, G. Filandrianos, M. Lymperaiou, K. Thomas, and G. Stamou (2025)
  ATLAS: adaptive trading with llm agents through dynamic prompt optimization and multi-agent coordination.
  arXiv preprint arXiv:2510.15949.
  Cited by: [§2](https://arxiv.org/html/2602.07085v1#S2.SS0.SSS0.Px2.p1.1 "Self-Evolving Agents ‣ 2 Related Work ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* M. H. Pesaran (2021)
  General diagnostic tests for cross-sectional dependence in panels.
  Empirical economics 60 (1),  pp. 13–50.
  Cited by: [§1](https://arxiv.org/html/2602.07085v1#S1.p1.1 "1 Introduction ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* H. Shi, W. Song, X. Zhang, J. Shi, C. Luo, X. Ao, H. Arian, and L. A. Seco (2025a)
  Alphaforge: a framework to mine and dynamically combine formulaic alpha factors.
  In Proceedings of the AAAI Conference on Artificial Intelligence,
  Vol. 39,  pp. 12524–12532.
  Cited by: [§2](https://arxiv.org/html/2602.07085v1#S2.SS0.SSS0.Px1.p1.1 "Agents in Finance ‣ 2 Related Work ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* Y. Shi, Y. Duan, and J. Li (2025b)
  Navigating the alpha jungle: an llm-powered mcts framework for formulaic factor mining.
  arXiv preprint arXiv:2505.11122.
  Cited by: [§2](https://arxiv.org/html/2602.07085v1#S2.SS0.SSS0.Px1.p1.1 "Agents in Finance ‣ 2 Related Work ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* Z. Tang, J. Liu, Z. Yang, R. Li, Z. Rong, H. He, Z. Hao, X. Hu, K. Ji, Z. Ma, et al. (2025a)
  Finmmr: make financial numerical reasoning more multimodal, comprehensive, and challenging.
  In Proceedings of the IEEE/CVF International Conference on Computer Vision,
   pp. 3245–3257.
  Cited by: [§2](https://arxiv.org/html/2602.07085v1#S2.SS0.SSS0.Px1.p1.1 "Agents in Finance ‣ 2 Related Work ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* Z. Tang, Z. Chen, J. Yang, J. Mai, Y. Zheng, K. Wang, J. Chen, and L. Lin (2025b)
  Alphaagent: llm-driven alpha mining with regularized exploration to counteract alpha decay.
  In Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V. 2,
   pp. 2813–2822.
  Cited by: [§1](https://arxiv.org/html/2602.07085v1#S1.p2.1 "1 Introduction ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* S. Wang, H. Yuan, L. Zhou, L. Ni, H. Y. Shum, and J. Guo (2025)
  Alpha-gpt: human-ai interactive alpha mining for quantitative investment.
  In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations,
   pp. 196–206.
  Cited by: [§2](https://arxiv.org/html/2602.07085v1#S2.SS0.SSS0.Px1.p1.1 "Agents in Finance ‣ 2 Related Work ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* Y. Xiao, E. Sun, D. Luo, and W. Wang (2024)
  TradingAgents: multi-agents llm financial trading framework.
  arXiv preprint arXiv:2412.20138.
  Cited by: [§1](https://arxiv.org/html/2602.07085v1#S1.p1.1 "1 Introduction ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining"),
  [§2](https://arxiv.org/html/2602.07085v1#S2.SS0.SSS0.Px2.p1.1 "Self-Evolving Agents ‣ 2 Related Work ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* Z. Yang, R. Li, Q. Qiang, J. Wang, F. Lou, M. Li, D. Cheng, R. Xu, H. Lian, S. Zhang, et al. (2026)
  FinVault: benchmarking financial agent safety in execution-grounded environments.
  arXiv preprint arXiv:2601.07853.
  Cited by: [§2](https://arxiv.org/html/2602.07085v1#S2.SS0.SSS0.Px1.p1.1 "Agents in Finance ‣ 2 Related Work ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* Y. Yu, H. Li, Z. Chen, Y. Jiang, Y. Li, J. W. Suchow, D. Zhang, and K. Khashanah (2025)
  Finmem: a performance-enhanced llm trading agent with layered memory and character design.
  IEEE Transactions on Big Data.
  Cited by: [§2](https://arxiv.org/html/2602.07085v1#S2.SS0.SSS0.Px2.p1.1 "Self-Evolving Agents ‣ 2 Related Work ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* Y. Yu, Z. Yao, H. Li, Z. Deng, Y. Jiang, Y. Cao, Z. Chen, J. Suchow, Z. Cui, R. Liu, et al. (2024)
  Fincon: a synthesized llm multi-agent system with conceptual verbal reinforcement for enhanced financial decision making.
  Advances in Neural Information Processing Systems 37,  pp. 137010–137045.
  Cited by: [§2](https://arxiv.org/html/2602.07085v1#S2.SS0.SSS0.Px2.p1.1 "Self-Evolving Agents ‣ 2 Related Work ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* Y. Zhai, S. Tao, C. Chen, A. Zou, Z. Chen, Q. Fu, S. Mai, L. Yu, J. Deng, Z. Cao, et al. (2025)
  Agentevolver: towards efficient self-evolving agent system.
  arXiv preprint arXiv:2511.10395.
  Cited by: [§2](https://arxiv.org/html/2602.07085v1#S2.SS0.SSS0.Px2.p1.1 "Self-Evolving Agents ‣ 2 Related Work ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* S. Zhang, C. Yuan, R. Guo, X. Yu, R. Xu, Z. Chen, Z. Li, Z. Yang, S. Guan, Z. Tang, et al. (2026)
  EvoFSM: controllable self-evolution for deep research with finite state machines.
  arXiv preprint arXiv:2601.09465.
  Cited by: [§2](https://arxiv.org/html/2602.07085v1#S2.SS0.SSS0.Px2.p1.1 "Self-Evolving Agents ‣ 2 Related Work ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").
* W. Zhang, L. Zhao, H. Xia, S. Sun, J. Sun, M. Qin, X. Li, Y. Zhao, Y. Zhao, X. Cai, et al. (2024)
  A multimodal foundation agent for financial trading: tool-augmented, diversified, and generalist.
  In Proceedings of the 30th acm sigkdd conference on knowledge discovery and data mining,
   pp. 4314–4325.
  Cited by: [§1](https://arxiv.org/html/2602.07085v1#S1.p1.1 "1 Introduction ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining").

SUMMARY OF THE APPENDIX

This appendix contains additional details for the “QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining”. The appendix is organized as follows:

## Appendix Table of Contents

## Appendix A Experiment Settings

This section provides details of our experimental setup, including computational infrastructure, evaluation metrics, backtesting setup, and baselines.

### A.1 Evaluation Metrics

We evaluate predictive performance using two categories of metrics: factor predictive power and strategy-level performance.

Without loss of generality, the bar notation ⋅¯\bar{\cdot} denotes the mean, and σ​(⋅)\sigma(\cdot) denotes the standard deviation.

* •

  Information Coefficient (IC): Pearson correlation between factor values 𝐟t\mathbf{f}\_{t} and future returns 𝐫t+1\mathbf{r}\_{t+1}:

  |  |  |  |
  | --- | --- | --- |
  |  | ICt=(𝐟t−f¯t​𝟏)⊤​(𝐫t+1−r¯t+1​𝟏)‖𝐟t−f¯t​𝟏‖2⋅‖𝐫t+1−r¯t+1​𝟏‖2,\operatorname{IC}\_{t}=\frac{(\mathbf{f}\_{t}-\bar{f}\_{t}\mathbf{1})^{\top}(\mathbf{r}\_{t+1}-\bar{r}\_{t+1}\mathbf{1})}{\|\mathbf{f}\_{t}-\bar{f}\_{t}\mathbf{1}\|\_{2}\cdot\|\mathbf{r}\_{t+1}-\bar{r}\_{t+1}\mathbf{1}\|\_{2}}, |  |

  where 𝟏\mathbf{1} denotes a column vector of ones.
* •

  ICIR: Information ratio of IC, measuring consistency: ICIR=IC¯/σ​(IC)\operatorname{ICIR}=\overline{\operatorname{IC}}/\sigma(\operatorname{IC}).
* •

  Rank IC: Spearman correlation using rank vectors 𝐟~t=rank⁡(𝐟t)\tilde{\mathbf{f}}\_{t}=\operatorname{rank}(\mathbf{f}\_{t}) and 𝐫~t+1=rank⁡(𝐫t+1)\tilde{\mathbf{r}}\_{t+1}=\operatorname{rank}(\mathbf{r}\_{t+1}):

  |  |  |  |
  | --- | --- | --- |
  |  | RankICt=(𝐟~t−f~¯t​𝟏)⊤​(𝐫~t+1−r~¯t+1​𝟏)‖𝐟~t−f~¯t​𝟏‖2⋅‖𝐫~t+1−r~¯t+1​𝟏‖2,\operatorname{RankIC}\_{t}=\frac{(\tilde{\mathbf{f}}\_{t}-\bar{\tilde{f}}\_{t}\mathbf{1})^{\top}(\tilde{\mathbf{r}}\_{t+1}-\bar{\tilde{r}}\_{t+1}\mathbf{1})}{\|\tilde{\mathbf{f}}\_{t}-\bar{\tilde{f}}\_{t}\mathbf{1}\|\_{2}\cdot\|\tilde{\mathbf{r}}\_{t+1}-\bar{\tilde{r}}\_{t+1}\mathbf{1}\|\_{2}}, |  |

  where rank⁡(⋅)\operatorname{rank}(\cdot) is the rank function applied element-wise to its input vector in ascending order.
* •

  Rank ICIR: Information ratio of Rank IC: RankICIR=RankIC¯/σ​(RankIC)\operatorname{RankICIR}=\overline{\operatorname{RankIC}}/\sigma(\operatorname{RankIC}).

All strategy metrics are computed on excess returns after transaction costs, where rexcess,t=rportfolio,t−rbenchmark,t−ctransaction,tr\_{\text{excess},t}=r\_{\text{portfolio},t}-r\_{\text{benchmark},t}-c\_{\text{transaction},t}. Here, rportfolio,tr\_{\text{portfolio},t} represents the return of the strategy portfolio, rbenchmark,tr\_{\text{benchmark},t} denotes the return of the market benchmark, and ctransaction,tc\_{\text{transaction},t} accounts for the transaction costs incurred at time tt.

* •

  Information Ratio (IR\operatorname{IR}): IR=(rexcess¯/σ​(rexcess))×252\operatorname{IR}=(\overline{r\_{\text{excess}}}/\sigma(r\_{\text{excess}}))\times\sqrt{252}.
* •

  Annualized Return (ARR\operatorname{ARR}): Annualized excess return over benchmark.
* •

  Maximum Drawdown (MDD\operatorname{MDD}): Largest peak-to-trough decline in cumulative excess returns.
* •

  Calmar Ratio (CR\operatorname{CR}): CR=ARR/|MDD|\operatorname{CR}=\operatorname{ARR}/|\operatorname{MDD}|.

### A.2 Backtesting Setup

Backtesting is conducted using the Qlib framework across the CSI 300, CSI 500, and S&P 500 indices, with the data split detailed in Table [5](https://arxiv.org/html/2602.07085v1#A1.T5 "Table 5 ‣ A.2 Backtesting Setup ‣ Appendix A Experiment Settings ‣ Acknowledgments ‣ 6 Conclusion ‣ Iteration Convergence ‣ 5.5 Case Study ‣ Evolutionary Alpha Mining Efficiency ‣ 5.4 More Analysis ‣ Ablation of Consistency, Complexity, and Redundancy Controls ‣ 5.3 Ablation Study ‣ 5.2 Main Results ‣ Baselines ‣ 5.1 Experimental Setup ‣ 5 Experiments ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining"). Factor construction utilizes six basic features—open, high, low, close, volume, and vwap—to predict the next-day return, defined as yt=Pt+2close/Pt+1close−1y\_{t}=P\_{t+2}^{\text{close}}/P\_{t+1}^{\text{close}}-1, where PtcloseP\_{t}^{\text{close}} denotes the closing price at time tt. To ensure robustness against outliers, the preprocessing pipeline includes forward-filling missing values, replacing infinite values, dropping samples with missing labels, and applying cross-sectional rank normalization (CSRankNorm) to both features and labels.

Table 5: Data Split Periods for Train, Validation, and Test Sets across All Markets

|  |  |  |  |
| --- | --- | --- | --- |
| Market | Train | Valid | Test |
| CSI 300 | 2016-01-01–2020-12-31 | 2021-01-01–2021-12-31 | 2022-01-01–2025-12-26 |
| CSI 500 | 2016-01-01–2020-12-31 | 2021-01-01–2021-12-31 | 2022-01-01–2025-12-26 |
| S&P 500 | 2016-01-01–2020-12-31 | 2021-01-01–2021-12-31 | 2022-01-01–2025-12-26 |

### A.3 Baselines

We benchmark against four categories: (1) ML models: Linear Regression (Linear), Multi-Layer Perceptron (MLP), and gradient boosting decision trees including LightGBM, XGBoost, and CatBoost, along with DoubleEnsemble, an ensemble method for financial time series; (2) Deep learning: Recurrent networks such as Gated Recurrent Unit (GRU) and Long Short-Term Memory (LSTM), the attention-based Transformer, and Temporal Routing Adaptor (TRA); (3) Classical factors: Alpha158 and Alpha360, which are widely used sets of technical factors derived from price and volume; (4) LLM agents: RD-Agent and AlphaAgent, which utilize large language models for automated factor mining. For the LLM-agent baselines (RD-Agent and AlphaAgent), we evaluate multiple backbone LLMs, including Qwen3-235B, DeepSeek-V3.2, Gemini-3-Pro-Preview, Claude-4.5-Sonnet, and GPT-5.2. Unless otherwise specified, all other LLM-based experiments in this paper adopt DeepSeek-V3.2 for consistency and fair comparison.

## Appendix B Algorithm Configuration

This section details the evolution algorithm parameters, factor constraints, and trading strategy configuration.

QuantaAlpha employs an evolutionary algorithm with mutation and crossover operations, with LightGBM used as the downstream model for factor-based prediction. In the Planning Phase of the algorithm, we set ten parallel exploration directions to broaden the initial coverage of research space. For the experimental setup, beyond the original round, the algorithm follows a fixed iterative process: the main experiment consists of 5 total iterations, and each iteration comprises one Mutation phase followed by one Crossover phase—alternating between these two phases to iteratively refine high-quality hypotheses. Additionally, we set a rule that each hypothesis attempts to generate 3 factor expressions, ensuring a focused yet sufficient exploration of factor candidates under each research direction.

To prevent overfitting and ensure interpretability, factor expressions—built using the operators listed in Table [6](https://arxiv.org/html/2602.07085v1#A2.T6 "Table 6 ‣ Appendix B Algorithm Configuration ‣ Acknowledgments ‣ 6 Conclusion ‣ Iteration Convergence ‣ 5.5 Case Study ‣ Evolutionary Alpha Mining Efficiency ‣ 5.4 More Analysis ‣ Ablation of Consistency, Complexity, and Redundancy Controls ‣ 5.3 Ablation Study ‣ 5.2 Main Results ‣ Baselines ‣ 5.1 Experimental Setup ‣ 5 Experiments ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining")—are restricted by the following constraints: symbol length ≤\leq 250 characters, base features ≤\leq 6, free arguments ratio << 50

Table 6: List of Supported Operators for Factor Construction

|  |  |  |
| --- | --- | --- |
| Category | Operators | Description |
| Time-Series | DELTA, DELAY, TS\_MEAN, TS\_STD, TS\_VAR, TS\_MAX, TS\_MIN, TS\_SUM, TS\_RANK, TS\_CORR, TS\_COVARIANCE, TS\_ARGMAX, TS\_ARGMIN, TS\_SKEW, TS\_KURT, TS\_PCTCHANGE, TS\_ZSCORE, TS\_QUANTILE | Rolling statistics computed along time axis per instrument |
| Cross-Sectional | RANK, ZSCORE, SCALE, MEAN, STD, MEDIAN, MAX, MIN, SKEW, KURT | Statistics computed across stocks per datetime |
| Mathematical | ABS, SIGN, LOG, EXP, SQRT, POW, INV | Element-wise mathematical functions |
| Technical | SMA, EMA, WMA, MACD, RSI, BB\_UPPER, BB\_LOWER, DECAYLINEAR, REGBETA, REGRESI | Common technical indicators |
| Logical | GT, LT, GE, LE, AND, OR, WHERE | Comparison and conditional operators |
| Auxiliary | COUNT, SUMIF, FILTER, PROD, HIGHDAY, LOWDAY | Helper functions for complex expressions |

We employ a TopkDropout strategy for portfolio construction, as detailed in Table [7](https://arxiv.org/html/2602.07085v1#A2.T7 "Table 7 ‣ Appendix B Algorithm Configuration ‣ Acknowledgments ‣ 6 Conclusion ‣ Iteration Convergence ‣ 5.5 Case Study ‣ Evolutionary Alpha Mining Efficiency ‣ 5.4 More Analysis ‣ Ablation of Consistency, Complexity, and Redundancy Controls ‣ 5.3 Ablation Study ‣ 5.2 Main Results ‣ Baselines ‣ 5.1 Experimental Setup ‣ 5 Experiments ‣ QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining"). On each trading day, stocks are ranked according to their predicted scores; the ndropn\_{\text{drop}} lowest-scoring holdings are liquidated and replaced with the highest-ranked candidates to maintain a constant portfolio size with equal weighting.

Table 7: Parameters for the TopkDropout Trading Strategy

|  |  |  |
| --- | --- | --- |
| Parameter | Value | Description |
| Portfolio | | |
| topk | 50 | Number of stocks held |
| n\_drop | 5 | Stocks dropped per rebalance |
| Transaction Costs | | |
| Buying Fee | 0.05% | Commission |
| Selling Fee | 0.15% | Commission + stamp duty |
| Execution | | |
| Deal Price | Open | Next-day opening price |
| Limit Threshold | 9.5% | Price limit for halt |
| Benchmark | | |
| China | SH000300/SH000905 | CSI 300/CSI500 |
| U.S. | SPX | S&P 500 |

## Appendix C Case Study: Factor Evolution Trajectory

This appendix presents a detailed case study of factor evolution in QuantaAlpha. We trace the complete trajectory of a representative factor—Institutional\_Momentum\_Score\_20D—through the crossover phase, demonstrating how the evolutionary framework synthesizes complementary market hypotheses from parent trajectories.

QuantaAlpha’s evolution process operates in three phases: (1) Original phase where initial hypotheses are generated, (2) Mutation phase where existing trajectories are perturbed to explore diversified strategies, and (3) Crossover phase where high-performing parent trajectories are combined to synthesize offspring with potentially superior predictive power. The following factor card illustrates a Crossover operation.

### C.1 Factor Identity

The factor card below presents the basic information of the evolved factor, including its unique identifiers, evolution lineage, and mathematical formulation.

Institutional\_Momentum\_Score\_20D

Factor ID:
c57cace576a95356

Trajectory ID:
df5a496878f4

Evolution Round:
Round 10

Evolution Phase:
Crossover

Direction ID:
6
Factor Expression:


RANK(TS\_CORR(DELTA(close, 1)/close, DELTA(volume, 1)/volume, 20) \* TS\_MEAN((close - open)/close, 5))

Mathematical Formulation:



IMS20​D=RANK​(ρ20​(Δ​PP,Δ​VV)×(C−OC)¯5),\text{IMS}\_{20D}=\text{RANK}\left(\rho\_{20}\left(\frac{\Delta P}{P},\frac{\Delta V}{V}\right)\times\overline{\left(\frac{C-O}{C}\right)}\_{5}\right),
where ρ20​(⋅,⋅)\rho\_{20}(\cdot,\cdot) denotes the 20-day rolling correlation, Δ​P/P\Delta P/P is the daily return, Δ​V/V\Delta V/V is the volume change ratio, (⋅)¯5\overline{(\cdot)}\_{5} is the 5-day moving average, and CC and OO represent the closing and opening prices, respectively.
Factor Interpretation:
  
This factor captures institutional-driven momentum by measuring two key signals: (1) the correlation between price returns and volume changes, which indicates coordinated institutional trading when positive; and (2) the average intraday return pattern, reflecting institutional activity that typically influences closing prices. The cross-sectional ranking ensures comparability across stocks.

### C.2 Evolution Lineage

The crossover operation combines insights from two parent trajectories with complementary market hypotheses. Parent 1 focuses on identifying fragile momentum driven by retail speculation, while Parent 2 targets sustainable momentum supported by institutional activity. The LLM synthesizes these complementary perspectives into a unified framework.

Evolution Information

Parent Trajectories:


Parent 1: 1e6d57e38e89

Round:
Round 9

Phase:
Mutation

Rank IC:
0.0216

IC:
0.0059

IR:
1.297
Core Hypothesis:
  
When retail investors exhibit herd behavior and momentum chasing in stocks with high social media activity, but accompanied by declining institutional ownership and deteriorating fundamentals, the resulting price momentum is unsustainable and leads to mean reversion.


Parent 2: 47e0f0e55382

Round:
Round 8

Phase:
Crossover

Rank IC:
0.0246

IC:
0.0069

IR:
1.347
Core Hypothesis:
  
A regime-adaptive structural momentum factor combining institutional ownership-driven medium-term price trends with short-term microstructure regime validation, where coordinated accumulation/distribution patterns amplify momentum when confirmed by microstructure alignment.



Evolution Path Diagram:
Parent 1Round 9 MutationRank IC: 0.0216Parent 2Round 8 CrossoverRank IC: 0.0246Offspring FactorRound 8 CrossoverRank IC: 0.0311

### C.3 Synthesized Hypothesis

Through crossover, the LLM generates a new hypothesis that integrates the complementary insights from both parents, rather than simply averaging their factor expressions. This hypothesis-driven approach ensures that the offspring factor captures genuinely novel market dynamics.

Hypothesis

Core Hypothesis:
  
A regime-aware dual-source momentum factor that combines institutional-driven structural momentum (validated by healthy microstructure) and retail-driven speculative momentum (characterized by high attention and deteriorating fundamentals), dynamically weighted by market volatility: amplifying institutional signals in stable regimes and retail reversal signals in turbulent regimes, will generate superior predictive returns.




Component


Description



Observation


Parent strategies separately targeting institutional trends and retail herding show moderate predictive power (Rank IC ∼\sim0.02–0.025), suggesting combined signals could capture complementary market dynamics.



Justification


Sustainable price trends require institutional sponsorship and orderly trading, while retail-driven bubbles lack fundamental support and reverse under stress; a hybrid model exploiting both can enhance robustness across market regimes.



Domain Knowledge


Institutional accumulation with strong price-volume correlation and low volatility indicates sustainable momentum; retail herding with declining institutional ownership and high volatility signals fragile momentum prone to reversal.

### C.4 Backtest Performance

After factor construction, QuantaAlpha automatically backtests the generated factors using the Qlib framework. The results below compare the offspring factor against both parent trajectories and the baseline, demonstrating the effectiveness of the crossover operation.

Backtest Metrics

Metric
Offspring Factor
Baseline

IC
0.0126
0.0058

Rank IC
0.0311
0.0220

ARR (Excess)
7.80%
5.20%

IR
0.963
0.973

MDD (Excess)
−-11.37%
−-7.30%
Detailed Statistics:


Metric
Value
Metric
Value

Daily Excess Return (w/o cost)
0.0328%
Daily Excess Return (w/ cost)
0.0128%

Excess Return Std
0.52%
Turnover (FFR)
100%

L2 Train Loss
0.9936
L2 Valid Loss
0.9962

### C.5 Trajectory Summary

After evaluating backtest results, the LLM provides structured summary. This trajectory summary loop enables continuous improvement by learning from both successes and failures.

Evaluation & Summary

Observations:
  
The crossover operation demonstrates a trade-off between enhanced predictive accuracy and increased risk exposure compared to the baseline:

•



Significant improvement in annualized excess return and predictive metrics (IC and Rank IC), validating the effectiveness of synthesizing dual-source momentum signals.
•



Increased maximum drawdown and a marginal decline in the Information Ratio, suggesting that the offspring factor introduces higher volatility during certain market regimes.


Hypothesis Evaluation:
  
Results partially support the hypothesis. Improved annualized return and IC suggest that combining institutional and retail momentum signals has merit. However, deterioration in risk metrics indicates that without proper regime-adaptive weighting, the combined signals may amplify risks during turbulent periods. The full hypothesis requires all three components (institutional momentum, retail herding reversal, volatility-adaptive weighting) to work effectively.


Decision: REJECTED for direct deployment.


Recommendations:

1.

Use 20-day price-volume correlation as institutional momentum proxy;
2.

Use 5-day average intraday returns as retail attention proxy;
3.

Add volatility regime indicator (recent/historical volatility ratio) for dynamic weighting.
This summary will inform the next mutation round, guiding the LLM to simplify the factor expression while preserving the core dual-source concept.