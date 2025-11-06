---
authors:
- Haofei Yu
- Fenghai Li
- Jiaxuan You
doc_id: arxiv:2511.03628v1
family_id: arxiv:2511.03628
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'LiveTradeBench: Seeking Real-World Alpha with Large Language Models'
url_abs: http://arxiv.org/abs/2511.03628v1
url_html: https://arxiv.org/html/2511.03628v1
venue: arXiv q-fin
version: 1
year: 2025
---


Haofei Yu
  
 Fenghai Li
  
 Jiaxuan You
  
 University of Illinois, Urbana-Champaign
  
[![[Uncaptioned image]](figures/globe.png) trade-bench.live](https://trade-bench.live)
  
[![[Uncaptioned image]](x1.png) github.com/ulab-uiuc/live-trade-bench](https://github.com/ulab-uiuc/live-trade-bench)

###### Abstract

Large language models (LLMs) achieve strong performance across benchmarks—from knowledge quizzes and math reasoning to web-agent tasks—but these tests occur in static settings, lacking real dynamics and uncertainty. Consequently, they evaluate isolated reasoning or problem solving rather than decision-making under uncertainty. To address this, we introduce LiveTradeBench, a live trading environment for evaluating LLM agents in realistic and evolving markets. LiveTradeBench follows three design principles:
(i) Live data streaming of market prices and news, eliminating dependence on offline backtesting and preventing information leakage while capturing real-time uncertainty;
(ii) a portfolio-management abstraction that extends control from single-asset actions to multi-asset allocation, integrating risk management and cross-asset reasoning; and
(iii) multi-market evaluation across structurally distinct environments—U.S. stocks and Polymarket prediction markets—differing in volatility, liquidity, and information flow.
At each step, an agent observes prices, news, and its portfolio, then outputs percentage allocations that balance risk and return. Using LiveTradeBench, we run 50-day live evaluations of 21 LLMs across families. Results show that (1) high LMArena scores do not imply superior trading outcomes; (2) models display distinct portfolio styles reflecting risk appetite and reasoning dynamics; and (3) some LLMs effectively leverage live signals to adapt decisions. These findings expose a gap between static evaluation and real-world competence, motivating benchmarks that test sequential decision making and consistency under live uncertainty.

## 1 Introduction

Large language models (LLMs) have achieved near-saturation performance on diverse benchmarks–such as knowledge quizzes (hendrycks2020measuring; phan2025humanity; rein2024gpqa), math reasoning tests (cobbe2021training; 2023opencompass; quan2025codeelo), and instruction-following tasks (pyatkin2025generalizing; zhou2023instruction; jiang2023followbench).
However, these benchmarks are static, evaluating models on fixed inputs with single-turn reasoning. High scores on such tests do not necessarily reflect real-world intelligence, where agents must perceive, act, and adapt through feedback over time.

To move beyond static evaluation, recent work has introduced interactive environments that allow LLMs to perform sequential actions and observe feedback (jimenez2023swe; zhou2023sotopia).
Examples include web and computer-use agents (zhou2023webarena; koh2024visualwebarena; xie2024osworld; he2024webvoyager), which operate in discrete and deterministic environments—each action produces a predictable transition defined by backend logic.
These environments test perception and reasoning, but remain fully controllable and support tree-based searching (Koh2024TreeSFA; Putta2024AgentQAA; Aksitov2023ReSTMRA). In contrast, trading environments represent continuous and autonomous systems.
The world evolves independently of the agent, and actions only adjust the agent’s internal portfolio state rather than directly determining future observations.
Feedback is delayed and noisy, emphasizing adaptation over control.
This difference in environment structure—from deterministic systems to dynamic processes—defines a deeper frontier for evaluating LLM agents’ ability to reason and act in open-ended, real-world settings (GarridoMerchan2024DeepRLA; Li2024INVESTORBENCHABA).

Table 1: Comparison of LiveTradeBench with existing trading benchmarks. We compare our work with others through four dimensions: (1) sequential decision for whether its current trading actions rely on the previous actions; (2) portfolio management for whether its task is multi-asset portfolio management; (3) live trading for whether the evaluation belongs to backtest with historical market data or live test with real-time streaming data; (4) multi-market evaluation for whether it includes markets beyond the stock market.

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Benchmark | |  | | --- | | Sequential | | Decision | | |  | | --- | | Portfolio | | Management | | |  | | --- | | Live | | Trading | | |  | | --- | | Multi-market | | Evaluation | |
| FinQA (chen2021finqa) | ✗ | ✗ | ✗ | ✗ |
| ConvFinQA (chen2022convfinqa) | ✗ | ✗ | ✗ | ✗ |
| FLUE (shah2022flue) | ✗ | ✗ | ✗ | ✗ |
| FinEval (zhang2023fineval) | ✗ | ✗ | ✗ | ✗ |
| BizFinBench (bigeard2025finance) | ✗ | ✗ | ✗ | ✗ |
| FinAgentBench (bigeard2025finance) | ✗ | ✗ | ✗ | ✗ |
| FinSearchComp (hu2025finsearchcomp) | ✓ | ✗ | ✗ | ✗ |
| INVESTORBENCH (Li2024INVESTORBENCHABA) | ✓ | ✗ | ✗ | ✗ |
| StockBench (chen2025stockbench) | ✓ | ✓ | ✗ | ✗ |
| DeepFund (Li2025TimeTIA) | ✓ | ✓ | ✓ | ✗ |
| LiveTradeBench (ours) | ✓ | ✓ | ✓ | ✓ |

Despite this importance, current applications for building LLM-based trading agents remain oversimplified and disconnected from live market dynamics. Specifically, (1) most evaluation frameworks rely on offline backtesting, which is prone to information leakage and fails to capture the uncertainty, volatility, and feedback of real-world environments (Li2025TimeTIA; Li2025CanLFA; Li2025WillLBA; Papadakis2025StockSimADA); and (2) most trading agents model trading as low-level local actions (e.g., buy/sell/hold) on a single asset, neglecting higher-level reasoning and planning across multiple assets (Ma2025AgentTAA; Briola2021DeepRLA; Han2023MasteringPTA; Han2023SelectATA). This naturally raises a broader question: How can we effectively evaluate the trading ability of LLM-based agents under realistic market conditions at low cost?

To answer this question, we introduce LiveTradeBench, a live trading environment designed to address both limitations above.
(1) LiveTradeBench streams live market data, financial news, and social signals, eliminating the dependence on offline backtesting and thereby avoiding information leakage from the root while capturing real-world uncertainty and feedback.
(2) It adopts the portfolio management abstraction, framing trading as a strategic allocation process that integrates risk management, temporal reasoning, and decision consistency across multiple assets (Yu2024FinConASA; Kou2024AutomateSFA; Gu2024AdaptiveAEA).
At each step, the environment exposes dynamic observations—market conditions, contextual signals, and the agent’s historical decisions—and the LLM must output an updated portfolio allocation that balances risk and return over time.
By combining live data streaming with portfolio-level reasoning, LiveTradeBench offers a realistic, end-to-end platform to evaluate the true trading competence of LLM-based agents under evolving market dynamics.

Using this benchmark, we conduct two types of live trading evaluations: stock market (U.S. stocks) trading and prediction market (Polymarket111<https://polymarket.com/>) betting.
We compare 21 mainstream LLMs across multiple model families and capability tiers.
Our analysis yields three key findings:
(1) State-of-the-art models in LMArena (chiang2024chatbot) do not exhibit state-of-the-art trading performance—high benchmark scores in general reasoning do not translate to superior trading outcomes;
(2) LLMs display distinct portfolio management styles, differing in their risk appetite, asset selection patterns, and allocation dynamics; and
(3) LLMs can effectively leverage real-time market and news signals to make more informed and adaptive trading decisions.
Together, these results reveal a disconnect between conventional LLM evaluation and real-world financial competence, motivating the development of more adaptive and robust portfolio management agents.

## 2 Related Work

#### Evaluation of trading agents

The evaluation of LLM-based trading agents generally relies on three types of environments or benchmarks.
(1) Backtesting with historical market data is the mainstream approach (Xiao2024TradingAgentsMLA; Li2025CanLFA; Tian2025TradingGroupAMA; Tang2025AlphaAgentLAA). However, such evaluations often suffer from information leakage (Li2025WillLBA; Li2025ProfitMRA) and poor generalization across longer or multi-regime market periods (gao2024finbench; jiang2025finagent). To address these issues, several studies propose data contamination audits, entity anonymization, and temporal de-biasing protocols for fairer backtesting evaluation (he2024finmem; wu2025finllm).
(2) Market simulators provide an alternative by constructing synthetic or self-designed trading environments (Emmanoulopoulos2025ToTOA; Zhang2024WhenAMA; Papadakis2025StockSimADA; Chen2023PutYMA; LopezLira2025CanLLA). Yet, these simulators serve mainly as testbeds for behavioral analysis rather than producing realistic trading actions aligned with actual market dynamics.
(3) Live evaluation with real-time data represents an emerging direction. While widely explored in other domains such as question answering (Kasai2022RealTimeQWA; nie2025uqassessinglanguagemodels) and coding (liang2024livecodebench), this approach remains largely unexplored in trading (Li2025TimeTIA). Our work focuses on this live evaluation paradigm, which we argue offers the most faithful and future-proof assessment of LLM trading intelligence.

#### Action space design for trading agents

The design of trading tasks varies substantially across objectives, which can be formalized through differences in the action space of trading agents.
In stock markets, most LLM-based systems adopt a single-asset trading formulation, where actions are discrete decisions such as buy, hold, or sell (Zhang2024AMFA; Li2023TradingGPTMSA; Gao2024SimulatingFMA; Ma2025AgentTAA; Zhang2025FinWorldAAA).
While intuitive, this setup overlooks cross-asset dependencies and realistic portfolio interactions.
Other approaches focus on alpha prediction, producing continuous vectors of alpha signals that represent expected excess returns or relative performance across assets (Islam2025TheEOA; Zhang2020AutoAlphaAEA; Sun2024CombiningTBA; Heinrich2021FactorIAA).
However, these signals describe predictions rather than directly executable trading actions.
In betting markets, agents often output probability estimates for mutually exclusive outcomes (e.g., “Yes” vs. “No”) (Koning2022BettingMEA; DeHaven2024MinutebyMinuteFMA; Jumadinova2011AMPA), which can be interpreted as implicit portfolio positions in complementary assets.
We unify these perspectives under a portfolio management framework, where the agent outputs allocation ratios across multiple assets or outcomes (Ye2020ReinforcementLearningBPA; Sun2021ReinforcementLFA; Lucarelli2020ADQA).
This formulation generalizes discrete trading, alpha prediction, and probabilistic betting within a single continuous decision space that naturally emphasizes risk–return trade-offs and inter-asset correlations.

#### Framework for LLM-based trading agents

Various frameworks leverage LLMs to build trading agents in different styles. One line of research focuses on fine-tuning a single LLM with reinforcement learning (RL) to enhance decision-making and trading performance (wang2025tradingr1; Xiong2025FLAGTraderFLA; Koa2024LearningTGA; Zhang2025FinWorldAAA; Zha2025ANDA). Another line explores multi-agent systems, where agents collaborate or compete through role differentiation to simulate realistic market dynamics (xu2024tradingagent; li2025contesttrade; zhang2025tradinggroup).
In addition, capabilities such as tool use (e.g., API calls, data collectors) (Papadakis2025StockSimADA; Islam2025TheEOA), self-reflection (Koa2024LearningTGA), and memory (Yu2023FinMemAPA; Li2023TradingGPTMSA; Li2024INVESTORBENCHABA) have been recognized as key components for improving trading intelligence.
To provide a controlled yet extensible setup, we adopt a React-style (yao2022react) framework equipped with tool use and memory as our agent configuration.

## 3 Building Live Trading Environment for Portfolio Management

### 3.1 Definition of Portfolio Management

#### Problem definition

We formulate the portfolio management task as a partially observable Markov decision process (POMDP)
ℰ=⟨𝒮,𝒜,𝒪,𝒯,Ω⟩\mathcal{E}=\langle\mathcal{S},\mathcal{A},\mathcal{O},\mathcal{T},\Omega\rangle,
where 𝒮\mathcal{S} is the latent market state space, 𝒜\mathcal{A} the action space,
𝒪\mathcal{O} the observation space, 𝒯\mathcal{T} the transition dynamics,
and Ω\Omega the observation emission function.
At each timestep tt, the environment is in a latent state
𝐬t∈𝒮\mathbf{s}\_{t}\in\mathcal{S}, which encapsulates the true market condition,
including asset fundamentals, volatility, liquidity, and other unobserved factors.
The agent receives a partial observation

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐨t=(𝐪t,𝐩t,𝐜t)=Ω​(𝐬t),\mathbf{o}\_{t}=(\mathbf{q}\_{t},\mathbf{p}\_{t},\mathbf{c}\_{t})=\Omega(\mathbf{s}\_{t}), |  | (1) |

where 𝐪t∈ℝN\mathbf{q}\_{t}\in\mathbb{R}^{N} denotes the current asset holdings (including cash),
𝐩t∈ℝN\mathbf{p}\_{t}\in\mathbb{R}^{N} the observable market prices,
and 𝐜t\mathbf{c}\_{t} contextual signals such as news, sentiment, or macro indicators.
The total portfolio value is computed as vt=𝐪t⊤​𝐩tv\_{t}=\mathbf{q}\_{t}^{\top}\mathbf{p}\_{t}.
Conditioned on the observation history 𝐨≤t\mathbf{o}\_{\leq t},
the agent produces an action 𝐚t∈𝒜\mathbf{a}\_{t}\in\mathcal{A} representing
a target allocation vector, subject to ∑iat(i)=1\sum\_{i}a\_{t}^{(i)}=1.

#### State transition function

The environment transition captures the joint evolution of the market and the agent’s portfolio.It consists of two coupled processes:
an exogenous market-state evolution, governed by real-world dynamics and observable as (𝐩t,𝐜t)→(𝐩t+1,𝐜t+1)(\mathbf{p}\_{t},\mathbf{c}\_{t})\rightarrow(\mathbf{p}\_{t+1},\mathbf{c}\_{t+1}), and an endogenous portfolio adjustment induced by the agent’s allocation decision 𝐚t\mathbf{a}\_{t} under the new market state, leading to
𝐪t→𝐪t+1\mathbf{q}\_{t}\rightarrow\mathbf{q}\_{t+1}.
Concretely, after executing 𝐚t\mathbf{a}\_{t}, the market evolves according to 𝒯\mathcal{T},
producing new prices 𝐩t+1\mathbf{p}\_{t+1} and contextual signals 𝐜t+1\mathbf{c}\_{t+1}.
The portfolio is revalued and rebalanced under the new prices as

|  |  |  |  |
| --- | --- | --- | --- |
|  | vt+1−=𝐪t⊤​𝐩t+1,𝐪t+1=vt+1−​𝐚t𝐩t+1,vt+1=𝐪t+1⊤​𝐩t+1=vt+1−v\_{t+1}^{-}=\mathbf{q}\_{t}^{\top}\mathbf{p}\_{t+1},\qquad\mathbf{q}\_{t+1}=v\_{t+1}^{-}\frac{\mathbf{a}\_{t}}{\mathbf{p}\_{t+1}},\qquad v\_{t+1}=\mathbf{q}\_{t+1}^{\top}\mathbf{p}\_{t+1}=v\_{t+1}^{-} |  | (2) |

where division is element-wise.
The next observation 𝐨t+1\mathbf{o}\_{t+1} is emitted by Ω\Omega,
capturing the updated portfolio state and market context. Since we focus on highly liquid assets such as Nvidia (NVDA) stocks and trending Polymarket markets to make up the portfolio, the agent’s individual trades exert negligible influence on real-world prices.
This assumption justifies modeling the simulated transition function 𝒯\mathcal{T} as closely aligned with the real world.

#### From allocation decisions to executable trading actions

At each timestep tt, after outputing the allocation decision 𝐚t\mathbf{a}\_{t}, the agent can update its holdings from 𝐪t\mathbf{q}\_{t} to 𝐪t+1\mathbf{q}\_{t+1} through executable trading actions (BUY/SELL/HOLD). The executed trade vector is defined as Δ​𝐪t=𝐪t+1−𝐪t\Delta\mathbf{q}\_{t}=\mathbf{q}\_{t+1}-\mathbf{q}\_{t}, where a positive Δ​qt(i)>0\Delta q\_{t}^{(i)}>0 indicates buying Δ​qt(i)\Delta q\_{t}^{(i)} shares of asset ii, a negative Δ​qt(i)<0\Delta q\_{t}^{(i)}<0 indicates selling |Δ​qt(i)||\Delta q\_{t}^{(i)}| shares, and Δ​qt(i)=0\Delta q\_{t}^{(i)}=0 corresponds to holding the current position. Once these trades are executed, the portfolio transitions to the new holdings 𝐪t+1\mathbf{q}\_{t+1}, and the total portfolio value vt+1v\_{t+1} is updated according to Eq. [2](https://arxiv.org/html/2511.03628v1#S3.E2 "In State transition function ‣ 3.1 Definition of Portfolio Management ‣ 3 Building Live Trading Environment for Portfolio Management ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models").
This formulation provides a direct mapping from the high-level allocation action space to explicit buy, sell, and hold operations, without modeling low-level order execution mechanics.

![Refer to caption](x2.png)


Figure 1: Market selection in LiveTradeBench. The top panels show AAPL in the U.S. stock market (left) and the contract “OpenAI has the best AI model by the end of 2025” in the Polymarket prediction market (right). In prediction markets, the price directly reflects the probability of a given outcome. Both markets respond to news and historical price trends, but Polymarket exhibits sharper fluctuations, faster reactions, and higher sensitivity to external signals. The bottom panels display representative assets across various domains, including technology, finance, cryptocurrency, manufacturing, and politics.

### 3.2 Market Selection

We evaluate agents in two complementary environments (stock market and prediction market) designed to test their generalization across both structured and information-driven regimes.
This dual setup enables a comprehensive assessment of whether agents can perform consistently across markets that differ in structure, information flow, and reaction speed.
Importantly, these two markets demand distinct strategies and reasoning perspectives for profitability:
the stock market rewards long-horizon analysis and disciplined diversification,
whereas the prediction market requires short-horizon adaptation and event-driven belief updating.

#### U.S. stock market

The U.S. stock market represents a mature, institutionally regulated system where asset prices evolve smoothly, exhibit strong cross-sector correlations, and reflect aggregated fundamentals and macroeconomic signals over time.
Effective portfolio management in this environment requires capturing long-term dependencies, modeling hidden correlations, and maintaining diversified risk exposure.
We construct a representative portfolio of 15 equities and ETFs spanning major U.S. sectors to ensure diverse responses to external information and macroeconomic shifts.
The portfolio includes technology stocks—Apple (AAPL), Microsoft (MSFT), NVIDIA (NVDA), and Meta Platforms (META); financial stocks—JPMorgan Chase (JPM) and Visa (V); energy and industrial stocks—Exxon Mobil (XOM), Caterpillar (CAT), and Tesla (TSLA); consumer goods stocks—Procter & Gamble (PG), Coca-Cola (KO), Amazon (AMZN), and Walmart (WMT); and healthcare stocks—Johnson & Johnson (JNJ) and UnitedHealth Group (UNH).
In addition, a *cash asset* with a constant unit price and zero return rate is included to represent risk-free capital allocation.
This composition provides balanced exposure across key sectors in a highly liquid and regulated financial environment, and we collect real-time stock prices as the data source for evaluation.

#### Polymarket prediction market

In contrast, the Polymarket prediction market is decentralized, sentiment-driven, and characterized by loosely coupled contracts that respond sharply and asynchronously to real-time information.
These markets often move more abruptly and less coherently than stocks, reflecting shifts in collective belief rather than fundamentals.
As a result, effective portfolio management here demands rapid adaptation, event-driven reasoning, and sensitivity to evolving narratives.
We continuously track ten active binary prediction markets from Polymarket, focusing on betting markets related to politics, crypto, technology and finance—such as “Fed rate hike in 2025?”, “Tether insolvent in 2025?”, “U.S. recession in 2025?”, and “USDT depeg in 2025?”.
We hypothesize that prediction markets and stock markets respond to the same information with different latency and magnitude: stock markets integrate signals gradually through institutional consensus, while prediction markets react instantly and often overshoot due to speculative sentiment.
Together, the two environments—structured financial markets and decentralized prediction markets—offer complementary testbeds for evaluating agents under both stability and uncertainty.

![Refer to caption](x3.png)


Figure 2: Observation and action space for LiveTradeBench. We illustrate examples from both the U.S. stock market and the Polymarket prediction market to demonstrate the observation and action spaces. The observation space consists of three components: the agent’s position, market prices, and relevant news context. The action space represents the portfolio allocation decisions generated by the agent, which can be directly translated into executable trading actions.

### 3.3 Observation Space

At each timestep, the agent receives an observation 𝐨t=(𝐪t,𝐩t,𝐜t)\mathbf{o}\_{t}=(\mathbf{q}\_{t},\mathbf{p}\_{t},\mathbf{c}\_{t}) that encapsulates the current market condition, external context, and portfolio status.
This observation serves as the primary input for the agent’s decision-making process, integrating quantitative market signals, position information, and qualitative contextual cues.
Based on these dynamic inputs, the agent determines its next allocation action, adapting to evolving market trends and external developments. Details on the data collection process of the observation space are available in Appendix §[8](https://arxiv.org/html/2511.03628v1#S8 "8 Data Collection ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models").

#### Position 𝐪t\mathbf{q}\_{t}

The position observation 𝐪t\mathbf{q}\_{t} represents the agent’s current holdings across all assets, including cash. Each component qt(i)q\_{t}^{(i)} is a continuous, non-negative value indicating the number of units (or fraction thereof) of asset ii currently held in the portfolio. This formulation differs from discrete buy/hold/sell signals used in traditional trading formulations and instead provides a fine-grained representation of continuous capital allocation. The non-negativity constraint ensures that the agent cannot take short positions, reflecting realistic market restrictions and emphasizing capital distribution among long-only assets.

#### Market price 𝐩t\mathbf{p}\_{t}

The price observation includes the latest asset prices and corresponding timestamps for all instruments in the portfolio. For the stock market, 𝐩t\mathbf{p}\_{t} contains closing prices of the 15 selected equities; for the prediction market, it includes the real-time trading prices of 10 trending Polymarket markets. These values serve as the direct basis for portfolio valuation and allocation updates, enabling the agent to track how asset values evolve over time.

#### Market context 𝐜t\mathbf{c}\_{t}

The contextual observation 𝐜t\mathbf{c}\_{t} mainly provides real-time market news. We collect recent articles from Google News using asset- and topic-specific keywords (e.g., “Federal Reserve,” “inflation,” “NVIDIA stock”). Such information reflects short-term market sentiment, investor attention, and macro-level signals that often precede price movements. To enable the model to reason about these factors, we include the textual summaries of these news items directly in the prompt, allowing LLM-based agents to incorporate qualitative context—such as sentiment shifts, policy expectations, or company-related events—into their trading decisions.

### 3.4 Action Space

At each timestep tt, the agent makes an action 𝐚t∈𝒜\mathbf{a}\_{t}\in\mathcal{A}, where 𝒜\mathcal{A} denotes the probability simplex action space. Each component at(i)a\_{t}^{(i)} specifies the proportion of the total portfolio value vtv\_{t} allocated to asset ii, satisfying the budget constraint ∑iat(i)=1\sum\_{i}a\_{t}^{(i)}=1. By default, we assume a long-only setting where at(i)≥0a\_{t}^{(i)}\geq 0 for all ii. This continuous allocation-based formulation abstracts away low-level trading execution and focuses on high-level portfolio rebalancing, allowing agents to express smooth strategic shifts over time and directly optimize for portfolio-level objectives such as return, risk, and stability.

#### Stock market action

In the stock market environment, each action component at(i)a\_{t}^{(i)} represents the percentage of the total portfolio value vtv\_{t} to be allocated to stock ii.
This allocation determines the post-trade position 𝐪t+1\mathbf{q}\_{t+1} through proportional rebalancing and directly reflects the agent’s capital distribution across sectors.

#### Prediction market action

In the prediction market environment, each binary contract corresponds to two complementary assets—YES and NO. For kk active markets, the action vector 𝐚t\mathbf{a}\_{t} has 2​k2k components, where at,YES(k)a\_{t,\text{YES}}^{(k)} and at,NO(k)a\_{t,\text{NO}}^{(k)} denote the portfolio allocations to the YES and NO outcomes of market kk, respectively. The agent’s net exposure is defined as et(k)=at,YES(k)−at,NO(k)e\_{t}^{(k)}=a\_{t,\text{YES}}^{(k)}-a\_{t,\text{NO}}^{(k)}, where a positive value indicates higher confidence in the YES outcome.

## 4 Designing LLM-based Agents for Portfolio Management

![Refer to caption](x4.png)


Figure 3: Agent and environment framework in LiveTradeBench.
The left side illustrates the simulated environment, which continuously retrieves real-world market prices and news, updating its internal state accordingly. It also adjusts the agent’s portfolio position based on the executed actions.
The right side depicts the portfolio-management agent, equipped with analytical tools to process observations from the environment. The agent maintains a memory of past observations, enabling adaptive and context-aware decision-making.

In our framework, the agent is the central decision-making entity that transforms observed information into actionable portfolio allocations.
It serves as the bridge between the external market and its internal portfolio memory, continuously adapting its strategy to changing conditions.
The agent integrates three intertwined capabilities—*tool use*, *memory*, and *reasoning*—that together enable it to perceive, recall, and act, forming a closed loop of information acquisition, reflection, and execution.
Formally, at each timestep tt, the agent receives an observation 𝐨t\mathbf{o}\_{t}.
In addition, the agent maintains an internal memory state 𝐌t\mathbf{M}\_{t}, which stores the past observation beyond the current one.
Conditioned on both the current observation and memory, the agent produces an allocation

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐚t=fθ​(𝐨t,𝐌t),\mathbf{a}\_{t}=f\_{\theta}(\mathbf{o}\_{t},\mathbf{M}\_{t}), |  | (3) |

where fθf\_{\theta} is a parameterized policy defining the agent’s trading behavior. Details on how we construct the prompt for the agent are available in Appendix §[9](https://arxiv.org/html/2511.03628v1#S9 "9 Prompting Details ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models").

#### Tool use

The first tool-use component enables the agent to interact with the live environment we provide—fetching, filtering, and extract real-time market and contextual information.
While market prices 𝐩t\mathbf{p}\_{t} and contextual signals 𝐜t\mathbf{c}\_{t} are emitted by the environment, the tool-use module governs how the agent actively acquires and processes them.
It acts as the agent interface with the real world, transforming raw inputs into structured feature representations

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐨~t=h​(𝐨t),\mathbf{\tilde{o}}\_{t}=h(\mathbf{o}\_{t}), |  | (4) |

that capture both quantitative dynamics (e.g., price changes, returns, and volatility features derived from 𝐩t\mathbf{p}\_{t}) and qualitative cues (e.g., news relevant to specific markets extracted from 𝐜t\mathbf{c}\_{t}).
Through tool use, the agent extends its perception beyond static observations, dynamically gathering and refining evidence to inform its allocation decisions.

#### Memory

The second memory component maintains a compact representation of the agent’s recent observations and the outcome of its actions.
At each timestep, the agent stores a fixed-length sequence of past observations and concatenates them into a unified memory state:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐌t={𝐨τ∣t−Δ≤τ<t},\mathbf{M}\_{t}=\{\mathbf{o}\_{\tau}\mid t-\Delta\leq\tau<t\}, |  | (5) |

where Δ\Delta denotes the memory horizon.
This concatenated memory provides temporal context beyond the current observation, enabling the agent to capture dependencies such as volatility dynamics, allocation adjustments, and drawdown trends.
By conditioning its decisions on both 𝐨t\mathbf{o}\_{t} and 𝐌t\mathbf{M}\_{t}, the agent becomes adaptive to evolving market conditions over time.

#### Reasoning

The third reasoning component serves as the agent’s decision core.
It integrates information gathered through tool use with contextual knowledge retained in memory, forming a coherent understanding of the market at each moment.
Before executing any action, the agent engages in a reasoning process that follows the ReAct (yao2022react) framework, where it first generates intermediate thoughts to interpret signals, recall relevant experiences, and hypothesize about potential outcomes.
Similar to chain-of-thought prompting (wei2022chain), this step produces explicit reasoning traces that connect perception and decision.
Such interpretability allows the resulting actions to be analyzed and considered as rational responses to evolving market contexts.
Through this deliberate reasoning–then–acting cycle, the agent achieves both adaptability and transparency in portfolio management. Such reasoning rationales can be potentially used to help researchers understand the model behavior and utilized as resources to improve LLMs.

## 5 Evaluating LLM-based Agents under Live Test

In this section, we present detailed evaluation results and analyses of live trading conducted from August 18, 2025, to October 24, 2025—a total of 50 trading days—across trading agents built on 21 unique LLM backbones.
Section §[5.1](https://arxiv.org/html/2511.03628v1#S5.SS1 "5.1 Backbone LLMs for Evaluation ‣ 5 Evaluating LLM-based Agents under Live Test ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models") and  §[5.2](https://arxiv.org/html/2511.03628v1#S5.SS2 "5.2 Trading Metrics for Evaluation ‣ 5 Evaluating LLM-based Agents under Live Test ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models") describe the evaluation setup, including model backbones and performance metrics.
Section §[5.3](https://arxiv.org/html/2511.03628v1#S5.SS3 "5.3 Evaluation Results ‣ 5 Evaluating LLM-based Agents under Live Test ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models") reports the main results, and Section §[5.4](https://arxiv.org/html/2511.03628v1#S5.SS4 "5.4 Analysis and Discussion ‣ 5 Evaluating LLM-based Agents under Live Test ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models") provides in-depth analyses and discussions.

### 5.1 Backbone LLMs for Evaluation

To benchmark performance in the live trading environment, we evaluate a diverse set of mainstream LLMs as trading agents.
Specifically, we consider six representative model families.
These models are selected based on two main criteria:
(1) their state-of-the-art performance on general-purpose reasoning, knowledge and agentic benchmarks, and
(2) their diversity in model size, architecture, and performance levels, which allows us to study performance gradients across heterogeneous systems in financial decision-making tasks.

#### LLM family

We include the following representative models:
Claude family (Claude-Sonnet-3.7 (anthropic2024claude3), Claude-Opus-4 & Claude-Sonnet-4 (anthropic2024claude4), Claude-Opus-4.1 (anthropic2024claude41)),
Grok family (Grok-3 (grok3), Grok-4 (grok4)),
Qwen family (Qwen2.5-72B-Instruct (Yang2024Qwen25TR), Qwen3-235B-A22B-Instruct & Qwen3-235B-A22B-Thinking (yang2025qwen3)),
LLaMA family (Llama3.3-70B-Instruct-Turbo (llama33), Llama4-Scout & Llama4-Maverick (llama4)),
GPT family (GPT-5 (gpt5), GPT-4o (hurst2024gpt), GPT-4.1 (gpt41), GPT-o3 (gpto3)),
Kimi family (Kimi-K2-Instruct (team2025kimi)), and
DeepSeek family (DeepSeek-V3.1 (deepseek31), DeepSeek-R1 (guo2025deepseek)). Each model is wrapped in the same agentic framework that converts market observations into natural-language prompts and parses model outputs into structured portfolio allocation vectors.
This unified setup ensures that performance differences primarily reflect the models’ intrinsic reasoning and decision-making abilities rather than disparities in prompt formatting or execution. Details on the model selection are available in Appendix §[10](https://arxiv.org/html/2511.03628v1#S10 "10 Model Details ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models").

### 5.2 Trading Metrics for Evaluation

To evaluate the performance of trading agents, we employ four widely used financial metrics: cumulative return, volatility, Sharpe ratio, and maximum drawdown (MDD).
These metrics jointly capture profitability, risk exposure, risk-adjusted efficiency, and downside protection, offering a comprehensive view of trading performance across different markets.

#### Cumulative return (C​R=vT−v0v0CR=\frac{v\_{T}-v\_{0}}{v\_{0}})

It measures the overall profitability of an investment strategy over a given evaluation period.
Here, v0v\_{0} and vTv\_{T} denote the initial and final portfolio values, respectively, and TT is the total number of timesteps during evaluation.
A higher cumulative return C​RCR indicates stronger cumulative gains achieved by the trading agent.

#### Sharpe ratio (S​R=r¯−rfσSR=\frac{\bar{r}-r\_{f}}{\sigma})

It evaluates the efficiency of returns relative to the amount of risk taken.
Here, r¯\bar{r} denotes the mean return, rfr\_{f} is the risk-free rate representing the baseline return from a no-risk investment, and σ\sigma is the volatility of returns.
In the U.S. stocks, rfr\_{f} corresponds to the short-term Treasury yield (typically positive), whereas in the Polymarket, rfr\_{f} is set to 0 to reflect the absence of yield on stablecoin-denominated assets.
A higher Sharpe ratio S​RSR signifies that the strategy achieves greater reward per unit of risk, reflecting superior risk-adjusted performance.

Table 2: Comparison of trading performance across U.S. stock and Polymarket prediction markets.
We use five key metrics: cumulative return (CR), Sharpe ratio (SR), maximum drawdown (MDD), win rate (WR), and volatility (σ\sigma). The highest value in each column is highlighted in bold.

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Model | U.S. Stock Market | | | | | Polymarket Prediction Market | | | | |
|  | CR↑\uparrow | SR↑\uparrow | MDD↓\downarrow | WR↑\uparrow | σ\sigma↓\downarrow | CR↑\uparrow | SR↑\uparrow | MDD↓\downarrow | WR↑\uparrow | σ\sigma↓\downarrow |
| Claude-Sonnet-3.7 | 3.633.63 | 1.451.45 | 2.652.65 | 59.1859.18 | 10.2510.25 | 20.54 | 2.38 | 10.65 | 51.0251.02 | 44.6444.64 |
| Claude-Sonnet-4 | 2.452.45 | 0.720.72 | 3.233.23 | 53.0653.06 | 12.8612.86 | −40.32-40.32 | −2.40-2.40 | 51.1051.10 | 38.7838.78 | 92.1692.16 |
| Claude-Opus-4 | 3.933.93 | 1.721.72 | 2.112.11 | 63.2763.27 | 9.459.45 | −2.04-2.04 | 0.090.09 | 13.6713.67 | 46.9446.94 | 56.3856.38 |
| Claude-Opus-4.1 | 3.733.73 | 1.511.51 | 1.84 | 63.2763.27 | 10.1710.17 | −25.69-25.69 | −3.02-3.02 | 30.5330.53 | 48.9848.98 | 46.8146.81 |
| Grok-3 | 3.223.22 | 1.261.26 | 2.132.13 | 65.3165.31 | 10.1710.17 | −8.35-8.35 | −0.55-0.55 | 18.8018.80 | 53.0653.06 | 54.3554.35 |
| Grok-4 | 4.304.30 | 1.751.75 | 1.921.92 | 59.1859.18 | 10.4310.43 | 7.387.38 | 1.011.01 | 13.0413.04 | 46.9446.94 | 46.9246.92 |
| Qwen2.5-72B-Instruct | 5.155.15 | 2.182.18 | 2.222.22 | 65.3165.31 | 10.2410.24 | 1.631.63 | 0.430.43 | 7.46 | 59.18 | 30.36 |
| Qwen3-235B-A22B-Instruct | 3.523.52 | 1.321.32 | 2.042.04 | 61.2261.22 | 10.8910.89 | −54.24-54.24 | −2.97-2.97 | 54.2454.24 | 40.8240.82 | 112.37112.37 |
| Qwen3-235B-A22B-Thinking | 1.781.78 | 0.600.60 | 2.322.32 | 59.1859.18 | 9.28 | −57.62-57.62 | −1.81-1.81 | 72.1072.10 | 38.7838.78 | 166.92166.92 |
| Llama3.3-70B-Instruct-Turbo | 2.722.72 | 0.880.88 | 3.543.54 | 61.2261.22 | 11.9511.95 | 1.581.58 | 0.400.40 | 19.4119.41 | 57.1457.14 | 38.1538.15 |
| Llama4-Scout | 4.654.65 | 1.991.99 | 2.622.62 | 59.1859.18 | 9.989.98 | −16.05-16.05 | −1.18-1.18 | 24.8024.80 | 51.0251.02 | 60.3760.37 |
| Llama4-Maverick | 4.464.46 | 1.651.65 | 2.452.45 | 53.0653.06 | 11.5911.59 | −18.31-18.31 | −1.92-1.92 | 28.6328.63 | 34.6934.69 | 48.2148.21 |
| GPT-4o | 3.553.55 | 1.391.39 | 2.432.43 | 55.1055.10 | 10.3810.38 | −30.96-30.96 | −3.26-3.26 | 35.3135.31 | 30.6130.61 | 53.7553.75 |
| GPT-4.1 | 6.25 | 2.64 | 1.921.92 | 65.31 | 10.5110.51 | −33.69-33.69 | −1.74-1.74 | 37.9837.98 | 40.8240.82 | 95.2795.27 |
| GPT-5 | 5.315.31 | 2.192.19 | 2.532.53 | 65.3165.31 | 10.6010.60 | −23.96-23.96 | −0.49-0.49 | 38.9238.92 | 44.9044.90 | 130.37130.37 |
| GPT-o3 | 6.046.04 | 2.572.57 | 2.272.27 | 61.2261.22 | 10.4110.41 | −54.84-54.84 | −3.68-3.68 | 60.9960.99 | 40.8240.82 | 97.2797.27 |
| Gemini-2.5-Flash | 2.102.10 | 0.720.72 | 3.103.10 | 55.1055.10 | 11.2511.25 | −22.40-22.40 | −0.82-0.82 | 42.3542.35 | 38.7838.78 | 115.42115.42 |
| Gemini-2.5-Pro | 1.951.95 | 0.610.61 | 2.852.85 | 50.0050.00 | 10.9810.98 | −35.15-35.15 | −1.65-1.65 | 49.8049.80 | 34.6934.69 | 101.87101.87 |
| Kimi-K2-Instruct | 3.073.07 | 1.151.15 | 3.323.32 | 53.0653.06 | 10.5310.53 | −53.44-53.44 | −5.26-5.26 | 54.7454.74 | 28.5728.57 | 69.4169.41 |
| DeepSeek-V3.1 | 2.462.46 | 0.860.86 | 2.452.45 | 59.1859.18 | 10.6110.61 | −4.68-4.68 | −0.07-0.07 | 22.4322.43 | 48.9848.98 | 64.7464.74 |
| DeepSeek-R1 | 2.102.10 | 0.780.78 | 2.202.20 | 61.2261.22 | 9.119.11 | −13.19-13.19 | 0.140.14 | 44.1644.16 | 42.8642.86 | 143.25143.25 |

#### Maximum drawdown (M​D​D=maxt∈[1,T]⁡maxi∈[1,t]⁡vi−vtmaxi∈[1,t]⁡viMDD=\max\_{t\in[1,T]}\frac{\max\_{i\in[1,t]}v\_{i}-v\_{t}}{\max\_{i\in[1,t]}v\_{i}})

It quantifies the largest observed decline from a historical peak to a subsequent trough in portfolio value before a new peak is reached.
Here, vtv\_{t} represents the portfolio value at time step tt.
A smaller MDD indicates better downside protection and stronger resilience against severe losses.

#### Win rate (W​R=1T−1​∑t=2T𝕀​(rt>0)WR=\frac{1}{T-1}\sum\_{t=2}^{T}\mathbb{I}(r\_{t}>0))

It measures the proportion of profitable trading steps, capturing the agent’s consistency in generating positive returns.
Here, 𝕀​(⋅)\mathbb{I}(\cdot) equals 1 when the return rtr\_{t} is positive and 0 otherwise.
A higher win rate W​RWR indicates that the agent achieves gains more frequently, complementing cumulative and risk-adjusted metrics by reflecting short-term decision reliability.

#### Volatility (σ=1T−1​∑t=1T(rt−r¯)2\sigma=\sqrt{\frac{1}{T-1}\sum\_{t=1}^{T}(r\_{t}-\bar{r})^{2}})

It reflects the variability of returns and serves as a measure of investment risk.
Here, rt=vt−vt−1vt−1r\_{t}=\frac{v\_{t}-v\_{t-1}}{v\_{t-1}} represents the return at time step tt, r¯=1T​∑t=1Trt\bar{r}=\frac{1}{T}\sum\_{t=1}^{T}r\_{t} is the average return, and TT is the total number of evaluation timesteps.
Strategies with lower volatility σ\sigma exhibit more stable performance over time.

### 5.3 Evaluation Results

![Refer to caption](x5.png)

![Refer to caption](x6.png)

Figure 4: Correlation between LMArena score and Sharpe ratio across two markets.
(left) U.S. stock market. (right) Polymarket prediction market.
Models from different families are shown in different colors, and the dashed line indicates the linear regression fit.

#### Trading performance on one market does not generalize to another.

As shown in Table [2](https://arxiv.org/html/2511.03628v1#S5.T2 "Table 2 ‣ Sharpe ratio (𝑆⁢𝑅={𝑟̄-𝑟_𝑓}/𝜎) ‣ 5.2 Trading Metrics for Evaluation ‣ 5 Evaluating LLM-based Agents under Live Test ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models"), the Sharpe ratio correlation between the two markets is close to zero, indicating that success in one market does not imply success in the other. This highlights the need for market-specific trading strategies. For example, Qwen2.5-72B-Instruct and Grok-4 show relatively consistent performance across both the stock and prediction markets, suggesting more stable and low-volatility strategies. In contrast, GPT-4.1 achieves the highest cumulative return rate (>6%>6\%) in the stock market but performs poorly in Polymarket (return <−30%<-30\%), likely due to overreactive allocation changes under higher volatility. Overall, the prediction market exhibits faster dynamics, greater volatility, and deeper drawdowns (MDD), demanding more agile and risk-tolerant strategies.

#### High general LLM capability does not imply strong financial performance.

Figures [4](https://arxiv.org/html/2511.03628v1#S5.F4 "Figure 4 ‣ 5.3 Evaluation Results ‣ 5 Evaluating LLM-based Agents under Live Test ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models") show that general LLM ability, as measured by LMArena scores, has slightly negative correlation with trading abilities. In the stock market, the Spearman correlation between LMArena scores and cumulative returns is only 0.054—virtually no relationship. In Polymarket, the correlation drops to –0.38, meaning models with higher general language ability often perform worse in the dynamic market. Thus, state-of-the-art LLMs on general benchmarks do not necessarily translate to state-of-the-art performance in dynamic, real-world trading. It highlights the uniqueness and necessity of our environment.

#### Distinct portfolio management styles emerge across models.

Different models exhibit distinct management preferences. Claude-Opus-4.1 and Grok-4 adopt conservative strategies characterized by lower volatility and smaller drawdowns, prioritizing stability over aggressive gains. In contrast, Kimi-K2-Instruct and GPT-5 display more risk-seeking behaviors—accepting higher volatility and MDD in pursuit of greater returns. Beyond return and risk metrics, models also differ notably in their portfolio composition and cash management patterns. For instance, GPT-4o consistently focuses on a few core assets (AAPL, MSFT, NVDA), whereas GPT-5 diversifies across a broader range of stocks with smaller position ratios. Likewise, Llama4-Scout maintains a persistently high cash ratio (above 20%), reflecting a more cautious liquidity stance, while GPT-5 always keeps cash below 10% throughout trading except in extremely high risk. These behavioral patterns are not limited to a single market—similar management styles emerge consistently across both markets.

#### Large reasoning models do not confer trading advantages.

Consistent with findings from chen2025stockbench, models explicitly designed for reasoning—such as DeepSeek-R1, Qwen3-235B-A22B-Thinking, and GPT-o3—do not outperform others in trading performance. Instead, they exhibit substantially higher volatility (>>140 in Polymarket), implying over-adjustment during the decision process. The type of reasoning beneficial for mathematical or coding tasks does not straightforwardly transfer to financial or social reasoning. In fact, excessive deliberation observed in these models during trading can introduce instability and degrade trading consistency.

### 5.4 Analysis and Discussion

![Refer to caption](x7.png)


Figure 5: Rolling kk-delta analysis on U.S. stocks. We evaluate rebalance intervals k∈{1,2,4,8,16}k\in\{1,2,4,8,16\}. The black line denotes the mean performance across 21 models, and the shaded gray region indicates the 25–75% confidence interval.

![Refer to caption](x8.png)


Figure 6: Rolling kk-delta analysis on Polymarket. We also evaluate rebalance intervals k∈{1,2,4,8,16}k\in\{1,2,4,8,16\}. The black line denotes the mean performance across 21 models, and the shaded gray region indicates the 25–75% confidence interval.

![Refer to caption](x9.png)


Figure 7: Decision-making rationale analysis. Each bar indicates the proportion of reasoning traces that reference position, price, or news information. A single reasoning trace may include multiple information sources.

In this section, we quantitatively analyze two core questions that probe the fundamental capabilities of LLM-based trading agents.
(1) Are LLM-based agents merely random guessers? — This examines whether the agents’ trading behaviors reflect meaningful market understanding or simply random fluctuations.
(2) How do agents reason and make trading decisions? — This investigates the internal rationale behind their actions, revealing whether their decisions are grounded in coherent reasoning patterns. Together, these analyses shed light on both the effectiveness and interpretability of LLM-based agents in dynamic, uncertain market environments.

#### Are LLM agents just random guessing?

To verify that LLM-based trading agents exhibit genuine market awareness rather than random behavior, we design the rolling-kk delta (Δk\Delta\_{k}) analysis. The key idea is that if the agents’ decisions are random, delaying their actions by several days should not systematically affect performance. Conversely, if they truly adapt to changing market conditions, stale decisions should lead to measurable degradation.
For each trading day tt, we fix the portfolio position to the one taken kk days earlier, 𝐪t(k)=𝐪t−k\mathbf{q}^{(k)}\_{t}=\mathbf{q}\_{t-k}, and compute daily and cumulative returns as

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt(k)=(𝐪t−k)⊤​(𝐩t+1−𝐩t)(𝐪t−k)⊤​𝐩t,C​R(k)=∏t=kT−k−1(1+rt(k))−1.r^{(k)}\_{t}=\frac{(\mathbf{q}\_{t-k})^{\top}(\mathbf{p}\_{t+1}-\mathbf{p}\_{t})}{(\mathbf{q}\_{t-k})^{\top}\mathbf{p}\_{t}},\qquad CR^{(k)}=\prod\_{t=k}^{T-k-1}(1+r^{(k)}\_{t})-1. |  | (6) |

The rolling-kk delta is then defined as Δk=C​R(k)−C​R(0)\Delta\_{k}=CR^{(k)}-CR^{(0)}, capturing the cumulative return loss when the agent’s actions lag behind the market by kk days.
A negative Δk\Delta\_{k} indicates that more frequent rebalancing improves performance.
As shown in Figure [7](https://arxiv.org/html/2511.03628v1#S5.F7 "Figure 7 ‣ 5.4 Analysis and Discussion ‣ 5 Evaluating LLM-based Agents under Live Test ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models") and Figure [7](https://arxiv.org/html/2511.03628v1#S5.F7 "Figure 7 ‣ 5.4 Analysis and Discussion ‣ 5 Evaluating LLM-based Agents under Live Test ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models"), larger kk (slower updates) leads to higher degradation, confirming that timely decision updates are beneficial.
Interestingly, in the stock market, returns slightly improve to 0.03% when k=2k=2, suggesting smoother dynamics and lower time sensitivity compared to the Polymarket, where performance degrades 2% as kk increases.
Overall, these results demonstrate that LLM-based agents do not act randomly—their trading strategies depend on contemporaneous market signals, and delaying their actions systematically harms performance.

#### How do LLM agents reason and make decisions?

To investigate decision-making rationale, we employ LLM-based reasoning annotation.
For each day’s reasoning trace, another LLM automatically identifies whether the agent’s explanation references:
(1) portfolio position, (2) market price history, or (3) market news.
Figure [7](https://arxiv.org/html/2511.03628v1#S5.F7 "Figure 7 ‣ 5.4 Analysis and Discussion ‣ 5 Evaluating LLM-based Agents under Live Test ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models") summarizes the distribution of these factors.
In both markets, news emerges as the most frequently cited factor, followed by market price history, while position information is less dominant.
Moreover, the Polymarket agents rely more heavily on news signals, while stock-market agents emphasize price trends—validating our hypothesis that the two markets exhibit distinct dynamics.
Since the total percentage of reasoning references exceeds 100%, many decisions integrate multiple information sources, indicating complex reasoning processes.
Specifically, agents often mention “price momentum” when analyzing price history and focus on potential outcomes or implications when discussing market news.

## 6 Case Study

In this section, we show examples of both the U.S stock and Polymarket prediction markets by selecting representative assets among each of them and highlighting two distinct and extreme time points for each to analyze. This allows us to examine the reasoning behind the agents’ decisions and understand how their choices correlate with market conditions.

### 6.1 Cash Asset Dynamics in the U.S. Stock Market

In Figure [8](https://arxiv.org/html/2511.03628v1#S6.F8 "Figure 8 ‣ 6.1 Cash Asset Dynamics in the U.S. Stock Market ‣ 6 Case Study ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models"), we analyze the dynamics of cash assets in the portfolio and highlight two contrasting market scenarios—a positive (bullish) case and a negative (bearish) case—in the U.S. stock market. The cash ratio serves as an informative indicator of risk management: a higher cash ratio typically reflects greater risk aversion and a defensive stance, whereas a lower cash ratio suggests stronger market confidence and a more aggressive investment posture.

![Refer to caption](x10.png)


Figure 8: Case study for U.S. stock markets. (Left) The average cash ratio across 21 models over 50 trading days. (Right) A zoomed-in view of the sharp drawdown on October 10, during which portfolios exhibited a sudden increase in cash holdings. We visualize the market condition (price change) and present the reasoning traces of the best-performing model on October 10 (Gemini-2.5-Pro) and one of the worst-performing models on October 10 (DeepSeek-V3.1) for comparison.

#### Tech stock rally on August 28

On August 28, the average cash ratio across all 21 models declined steadily over three consecutive days, dropping from 17% to 7.5% within four trading days. This trend coincided with a strong rally in major technology stocks such as Meta (META), Apple (AAPL), and Microsoft (MSFT), which encouraged agents to invest more aggressively and reduce their cash holdings.
Notably, GPT-4.1, the agent achieving the highest cumulative return rate, provided the following rationale for its allocation decision:
“This allocation increases exposure to leading AI and tech growth stocks (NVDA, MSFT, META) following strong earnings momentum and positive analyst sentiment, while maintaining solid positions in diversified blue chips for stability and sector balance.”
This reasoning explicitly aligns with the observed decrease in the cash ratio during the bullish market phase.

#### Market drawdown on October 10

In contrast, the sharp market drawdown on October 10 induced the opposite behavior. Most of the stock prices dropped significantly—Tesla (TSLA) fell over 5%, while Amazon (AMZN) and Nvidia (NVDA) declined by more than 4%—leading to negative returns for all agents on that day. In response, most agents increased their cash holdings to mitigate risk, reflecting a collective shift toward a defensive strategy.
As shown on the right of Figure [8](https://arxiv.org/html/2511.03628v1#S6.F8 "Figure 8 ‣ 6.1 Cash Asset Dynamics in the U.S. Stock Market ‣ 6 Case Study ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models"), multiple agents provided similar reasoning related to “increasing CASH positions to protect against volatility.” Among them, Gemini-2.5-Pro, which maintained a relatively high cash position and converted additional assets to cash before the downturn, experienced the smallest loss that day.

### 6.2 Russia–Ukraine Ceasefire Market in Polymarket Prediction Market

We analyze the market “Russia × Ukraine ceasefire in 2025?” on Polymarket, focusing on how real-time news influences the decision-making of LLM-based agents. Polymarket’s high sensitivity to external information makes it a natural testbed to evaluate how models interpret and act on dynamic geopolitical signals.
We select this market for the case study because it experiences frequent fluctuations during the 50 trading days, resulting in distinct behaviors and returns across models. As shown in Figure [9](https://arxiv.org/html/2511.03628v1#S6.F9 "Figure 9 ‣ Reactive change on October 13 without profit ‣ 6.2 Russia–Ukraine Ceasefire Market in Polymarket Prediction Market ‣ 6 Case Study ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models"), the Grok-3 model is able to conduct belief-based reasoning, adjusting its internal estimate of the ceasefire probability from 0.15 on October 13 to 0.22 on October 17.

#### Reactive change on October 13 without profit

On October 13, most agents abruptly switched their portfolios from No to Yes positions after two optimistic news events: (1) Zelenskyy stated that “the Gaza deal brings hope for Ukraine,” and (2) reports surfaced that Trump shared U.S. intelligence to help Kyiv strike Russian energy targets. These headlines appeared relevant to the ceasefire, prompting agents to buy into the Yes position.
However, the Polymarket price showed little actual movement, and this reactive change produced no profit. The news turned out to have limited causal impact on the ceasefire likelihood. This case highlights a key challenge for LLM-based agents: distinguishing between attention-grabbing but non-decisive news and genuinely influential events. Acting on superficial correlations can lead to overreaction and unprofitable trades.

![Refer to caption](x11.png)


Figure 9: Case study in Polymarket prediction markets. (Left) The average holding ratios of “Yes” and “No” position ratios in the market “Russia × Ukraine ceasefire in 2025?” across 21 models. (Right) A zoomed-in view of two abrupt shifts (October 13 and October 17), along with the corresponding news events and the reasoning traces of Grok-3 explaining these allocation decisions.

#### Strategic hold on October 17 with profit

In contrast, on October 17, when news broke that Zelenskyy visited the White House, most agents strengthened their Yes positions and held them through the following day. This time, the Polymarket price steadily increased from October 17 to 18, leading to tangible profits.
Unlike the earlier overreaction, agents displayed more grounded reasoning—citing “recent diplomatic developments” and recognizing “a significant price jump to 0.18” as confirming evidence. This scenario illustrates that maintaining positions through credible, high-impact events can yield better outcomes than frequent reactive shifts based on weak signals.

## 7 Conclusion

In this work, we present LiveTradeBench, a live multi-market environment for evaluating LLM-based agents in realistic portfolio management tasks. LiveTradeBench introduces a new paradigm for assessing model intelligence beyond static benchmarks, enabling continuous interaction, reasoning, and adaptation within real-time stock and prediction markets. Through 50-day live experiments, we find that strong performance in one market does not generalize to others, underscoring the heterogeneity and specialization required across market types. Moreover, high scores on general-purpose benchmarks like LMArena do not necessarily translate into superior trading performance, highlighting a gap between text intelligence and dynamic decision-making. Finally, our analyses reveal that LLM-based agents rely jointly on historical price trends, market news, allocation history, exhibiting distinct behavioral patterns under extreme conditions. Overall, LiveTradeBench provides a foundation for studying how LLM-based agents perceive, reason, and act under uncertainty in live and realistic trading environments—paving the way for developing more adaptive, financially grounded, and socially intelligent agent systems.

## Limitation and Future Work

Despite demonstrating the feasibility of evaluating LLM-based trading agents in live multi-market environments, our framework still has thee main limitations that point to promising directions for future research and development.

#### Transaction costs and market frictions

Our current environment and evaluation do not account for transaction fees, bid–ask spreads, liquidity constraints, or other real-world trading frictions. Ignoring these factors may overestimate achievable returns, especially for strategies that rely on frequent rebalancing. Future work will incorporate more realistic cost models and slippage simulations to better approximate real trading conditions.

#### Limited observation and action space

The current framework constrains both the observation and action spaces due to the limited context length of existing LLMs.
For the *observation space*, the agent can only access a restricted temporal window of price, position, and news histories, and these are limited to a small set of markets in both the stock market and the prediction market.
Moreover, news inputs are truncated to titles and abstracts rather than full articles, preventing the agent from incorporating long-form textual information that may contain deeper market signals.
For the *action space*, the scope of possible trading actions is similarly constrained by the limited number of supported markets, reducing the complexity and richness of allocation decisions.
Future work could extend the framework to support longer temporal horizons, richer textual context, and dynamic market expansion—enabling agents to observe and act within more realistic, information-rich environments.

#### Simplified agent design

The current agent architecture integrates basic tool use and memory under the ReAct framework but remains limited in reasoning depth and temporal abstraction. Future work can enhance each component systematically. For tool use, agents can be equipped with more specialized analytical and retrieval tools for financial reasoning, news interpretation, and risk assessment. For memory, richer hierarchical and long-term memory mechanisms can be introduced to capture temporal dependencies and retain cross-market knowledge over extended horizons. Beyond the basic ReAct-based setups, the current framework can be extended to a multi-agent paradigm, such as TradingAgents (xiao2024tradingagents), to better model heterogeneous roles and market interactions. Finally, incorporating reinforcement learning (RL) to train trading agents (xiao2025trading) represents a promising direction for improving decision quality—enabling agents to learn from experience, refine their reasoning, and continuously adapt to dynamic market conditions.

## Open-source Application

To democratize research on LLM-based trading agents, we release an open-source Python package, live-trade-bench222<https://pypi.org/project/live-trade-bench/>
, which provides simple APIs for data collection, environment setup, and agent construction.
Building on this package, we also develop a web application that deploys our trading environment in real time, enabling live data streaming and interactive monitoring of agent performance.
Details of the user interface (UI) design are provided in Appendix §[11](https://arxiv.org/html/2511.03628v1#S11 "11 Frontend UI Details ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models").

\beginsupplement

## 8 Data Collection

We collect live prices and news signals to populate the observation space for both Stock market and Polymarket. Prices come from a public finance API (equities) and Polymarket CLOB endpoints (prediction markets); context comes from Google News and Reddit. All fetchers use randomized delays, a standard User-Agent, and exponential-backoff retries; JSON parsing is retried a small number of times with conservative timeouts. Retrieved items are bound to tickers or market IDs and presented to the agent alongside account history.

### 8.1 Market News Data

#### Source and window

For a trading day tt, we query Google News over a short window [t−3,t−1][t{-}3,t{-}1] to reduce same-day leakage while preserving timeliness. Results are ranked by proximity to tt when a target date is available, else by recency.

#### Query construction

For stocks we use <TICKER> stock news OR <Company Name>; for Polymarket we use the market *question* text. The fetcher pages through date-bounded results.

#### Normalization

We parse per-article *title*, *snippet*, *link* (Google redirect cleaned), *source*, and *timestamp*. Relative times (e.g., “3 hours ago”) and absolute dates (e.g., “Oct 12, 2025”) are normalized to UNIX time. Items lacking a valid timestamp are dropped. Remaining items are tagged with the originating symbol/question and sorted within the window.

### 8.2 Stock Price Data

#### Source and window

We retrieve U.S. equity prices from a public finance API (yfinance). For a trading day tt, we form a 10-day lookback ending at t−1t{-}1 to mitigate same-day leakage; if no date is given, we use the latest snapshot.

#### Universe and queries

We track a small, curated universe (default 15 tickers). For dated queries, we download daily bars over a half-open window [[start, end+1)) to match the provider’s convention; the current price is taken as the latest available trade/quote.

#### Normalization

We expose the current price together with a compact daily history containing *date*, *adjusted close*, and *volume*. If a dated close is unavailable, we fall back to the best available price within that day.

### 8.3 Polymarket Price Data

#### Source and window

We use public endpoints for market discovery and for prices/history. As with stocks, per-token history uses a 10-day lookback ending at t−1t{-}1 to reduce leakage.

#### Market discovery

We discover active (or date-filtered) markets and collect *question*, *category*, outcomes, token IDs, and URLs (constructing them from event slugs when missing). We further filter to a verified subset by deduplicating markets that share an event slug, requiring observable history, and removing near-flat series below a minimum price-range threshold.

#### Normalization

For each token, we expose the current price (on tt or latest) and a per-day history with *date* and *price*. Exchange quotes are normalized to probabilities in [0,1][0,1] (dividing by 100100 when endpoints return cents).

## 9 Prompting Details

In LiveTradeBench, each trading step is framed as a structured text prompt that guides the LLM’s decision-making process.
We define a market-specific *decision prompt*, which forms the full model input and consists of two components: a dynamic *context prompt* and a fixed *instruction header*.
The context prompt summarizes the agent’s current observation—market status, recent news, and account information—while the instruction header provides global objectives, portfolio principles, and output requirements.
Because the full text is lengthy, we present each market’s prompt across two tables (stocks: Tables [4](https://arxiv.org/html/2511.03628v1#S11.T4 "Table 4 ‣ 11 Frontend UI Details ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models"), [5](https://arxiv.org/html/2511.03628v1#S11.T5 "Table 5 ‣ 11 Frontend UI Details ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models"); Polymarket: Tables [6](https://arxiv.org/html/2511.03628v1#S11.T6 "Table 6 ‣ 11 Frontend UI Details ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models"), [7](https://arxiv.org/html/2511.03628v1#S11.T7 "Table 7 ‣ 11 Frontend UI Details ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models")).
The following subsections describe them in detail.

#### Stock context prompt

The context prompt mirrors the observation space and includes three elements: market analysis (current prices and short recent histories for each ticker), recent news grouped by ticker, and account information showing past allocations and cumulative performance (Table [4](https://arxiv.org/html/2511.03628v1#S11.T4 "Table 4 ‣ 11 Frontend UI Details ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models")).
This dynamic block provides the local state and external signals needed for decision reasoning.

#### Stock decision prompt

The decision prompt (Table [5](https://arxiv.org/html/2511.03628v1#S11.T5 "Table 5 ‣ 11 Frontend UI Details ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models")) combines the context above with a dated header, explicit trading objectives and evaluation criteria (risk-adjusted return, diversification, turnover awareness), portfolio principles, the list of tradable assets, and a JSON-only output schema specifying the fields reasoning and allocations (weights summing to 1.0 including CASH).
This forms the full prompt delivered to the model and constrains outputs to align with the portfolio action space.

#### Polymarket context prompt

For prediction markets, the context prompt organizes market analysis by question with YES/NO prices (implied probabilities) and short histories, recent news grouped by question, and account information showing allocations (including CASH) and performance (Table [6](https://arxiv.org/html/2511.03628v1#S11.T6 "Table 6 ‣ 11 Frontend UI Details ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models")).
This representation emphasizes the agent’s belief states and position history.

#### Polymarket decision prompt

The decision prompt (Table [7](https://arxiv.org/html/2511.03628v1#S11.T7 "Table 7 ‣ 11 Frontend UI Details ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models")) combines the contextual information with task-specific instructions: the agent may choose at most one side (YES or NO) per question, compare its internal belief (p) with the market probability pmktp\_{\text{mkt}} while considering transaction costs, and output allocations normalized to sum to 1.0 over available outcomes and CASH.
As in the stock setup, this constitutes the complete model input, enforcing executable portfolio allocations.

## 10 Model Details

We evaluate mainstream chat LLMs across families, using the same pool for both the stock and Polymarket settings. Table [3](https://arxiv.org/html/2511.03628v1#S11.T3 "Table 3 ‣ 11 Frontend UI Details ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models") summarizes the families and concrete variants included in our evaluation.

#### Provider routing

We invoke models through a thin client (LiteLLM) with automatic provider resolution. Model strings prefixed by vendor names are routed accordingly (e.g., openai/gpt-4o-mini, anthropic/claude-3-5-sonnet, gemini/gemini-2.5-pro, x-ai/grok-4); unprefixed names default to Together AI. For standard chat models we set temperature =0.3=0.3 and max\_tokens =16000=16000; for structured-reasoning styles (e.g., gpt-5, o3-2025-04-16) we omit these parameters to match provider defaults.

#### Response schema

All models are prompted to return a single JSON object with fields reasoning and allocations. Allocations must sum to 1.0 over the available assets and may include CASH. Responses are parsed and validated before application to accounts.

## 11 Frontend UI Details

In this section, we provide a detailed description of the LiveTradeBench front-end UI, which consists of six main pages. The first is the Leaderboard Page (Figure [10](https://arxiv.org/html/2511.03628v1#S11.F10 "Figure 10 ‣ 11 Frontend UI Details ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models")), which shows the ranking of each LLM model by the profit return rate. Each Stock model starts with 1000 USD and each Polymarket model starts with 500 USD. The second is the Stock Page (Figure [11](https://arxiv.org/html/2511.03628v1#S11.F11 "Figure 11 ‣ 11 Frontend UI Details ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models")), which shows all 21 LLM Stock models. On this page, there are detailed model cards (Figure [12](https://arxiv.org/html/2511.03628v1#S11.F12 "Figure 12 ‣ 11 Frontend UI Details ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models")) of each LLM Stock model. The third is the Polymarket Page (Figure [13](https://arxiv.org/html/2511.03628v1#S11.F13 "Figure 13 ‣ 11 Frontend UI Details ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models")), which shows the all 21 LLM Polymarket models. On this page, there are detailed model cards (Figure [14](https://arxiv.org/html/2511.03628v1#S11.F14 "Figure 14 ‣ 11 Frontend UI Details ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models")) of each LLM Stock model. The fourth is the News Page (Figure [15](https://arxiv.org/html/2511.03628v1#S11.F15 "Figure 15 ‣ 11 Frontend UI Details ‣ LiveTradeBench: Seeking Real-World Alpha with Large Language Models")), which shows the recents news of Stock-market and Polymarket.

Table 3: Model families and variants used in LiveTradeBench.

|  |  |
| --- | --- |
| Family | Models |
| OpenAI | GPT-5, GPT-4.1, GPT-4o, GPT-o3 |
| Anthropic | Claude-Opus-4.1, Claude-Opus-4, Claude-Sonnet-4, Claude-Sonnet-3.7 |
| Google | Gemini-2.5-Pro, Gemini-2.5-Flash |
| xAI | Grok-4, Grok-3 |
| Meta | Llama4-Maverick, Llama4-Scout, Llama3.3-70B-Instruct-Turbo |
| Qwen | Qwen3-235B-A22B-Instruct, Qwen3-235B-A22B-Thinking, Qwen2.5-72B-Instruct |
| DeepSeek | DeepSeek-R1, DeepSeek-V3.1 |
| Moonshot | Kimi-K2-Instruct |

Table 4: Example of stock context prompt.

|  |
| --- |
| Example of stock context prompt |
| ``` MARKET ANALYSIS: AAPL: Current price is $263.51   - 2025-10-24: close price $263.52 (Change: +3.94 (+1.52%))   - 2025-10-23: close price $259.58 (Change: +1.13 (+0.44%))   - 2025-10-22: close price $258.45 (Change: -4.32 (-1.64%))   - 2025-10-21: close price $262.77 (Change: +0.53 (+0.20%))   - 2025-10-20: close price $262.24 (Change: +9.95 (+3.94%))   - 2025-10-17: close price $252.29 (Change: +4.84 (+1.96%))   - 2025-10-16: close price $247.45 (Change: -1.89 (-0.76%))   - 2025-10-15: close price $249.34 (Change: +1.57 (+0.63%))   - 2025-10-14: close price $247.77 (Change: N/A) ... AMZN: ...   RECENT NEWS: • AAPL:   - Did Buffett Sell Apple and Bank of America too Early? (2025-10-23)     (0:30) - How Do You Know When To Sell Your Investments? (4:10)     - Breaking Down Warren Buffett’s     Recent Stock Moves; (12:00) - Should You Consider Selling......   - Apple (AAPL) Stock Rockets to Record High on iPhone 17 Hype   — What’s Next? (2025-10-23)     Apple (AAPL) Stock Rockets to Record High on iPhone 17     Hype — What’s Next? - TechStock²....   - AMZN, META and AAPL Forecast – Major US Stocks Look to Rally (2025-10-23)     Major U.S. tech stocks are showing signs of strength ahead of Friday’s session.     Amazon, Meta, and Apple all     point to continued bullish momentum,...... ... • AMZN: ...  ACCOUNT INFO:   Recent Historical Allocations under this account:     - Asset Allocation at 2025-10-10: {’AAPL’: ’0.08’,     ’MSFT’: ’0.11’, ’NVDA’: ’0.12’, ’JPM’: ’0.05’, ’V’:     ’0.04’, ’JNJ’: ’0.05’, ’UNH’: ’0.05’, ’PG’: ’0.04’,     ’KO’: ’0.03’, ’XOM’: ’0.04’, ’CAT’: ’0.05’, ’WMT’:     ’0.05’, ’META’: ’0.10’, ’TSLA’: ’0.05’, ’AMZN’:     ’0.08’, ’CASH’: ’0.06’} (Accumulated return rate: 3.6%) ...     - Asset Allocation at 2025-10-23: {’AAPL’: ’0.16’,     ’MSFT’: ’0.11’, ’NVDA’: ’0.11’, ’JPM’: ’0.04’, ’V’:     ’0.04’, ’JNJ’: ’0.04’, ’UNH’: ’0.04’, ’PG’: ’0.03’,     ’KO’: ’0.03’, ’XOM’: ’0.05’, ’CAT’: ’0.05’, ’WMT’:     ’0.04’, ’META’: ’0.10’, ’TSLA’: ’0.06’, ’AMZN’:     ’0.07’, ’CASH’: ’0.03’} (Accumulated return rate: 5.6%) ``` |

Table 5: Example of stock decision prompt.

|  |
| --- |
| Example of stock decision prompt |
| ``` Today is 2025-10-24 (US Eastern Time). You are a professional portfolio manager. Analyze the market data and generate a complete portfolio allocation. MARKET ANALYSIS: ... RECENT NEWS: ... ACCOUNT INFO: ... PORTFOLIO MANAGEMENT OBJECTIVE: - Improve total returns by selecting allocations with higher expected return per unit of risk. - Aim to outperform a reasonable baseline (e.g., equal-weight of AVAILABLE ASSETS) over the next 1–3 months. - Use CASH tactically for capital protection in unfavorable markets. EVALUATION CRITERIA: - Prefer allocations that increase expected excess return and improve risk-adjusted return. - Maintain sector and factor diversification. - Be mindful of turnover and liquidity. PORTFOLIO PRINCIPLES: - Diversify across sectors and market caps. - Consider market momentum and fundamentals. - Balance growth and value opportunities. - Maintain appropriate position sizes. - Total allocation must equal 1.0. - CASH is a valid asset.  AVAILABLE ASSETS: AAPL, MSFT, NVDA, JPM, V, JNJ, UNH, PG, KO, XOM, CAT, WMT, META, TSLA, AMZN, CASH  CRITICAL: Return ONLY valid JSON. No extra text. REQUIRED JSON FORMAT: {  "reasoning": "Brief explanation about why this allocation improves return rate",  "allocations": {    "AAPL": 0.25,    "MSFT": 0.20,    "NVDA": 0.15,    "CASH": 0.40  } } RULES: 1. Return ONLY the JSON object. 2. Allocations must sum to 1.0. 3. CASH allocation should reflect market conditions. 4. Use double quotes for strings. 5. No trailing commas. 6. No extra text outside the JSON. Your objective is to maximize return while considering previous allocations and performance history. ``` |

Table 6: Example of Polymarket context prompt.

|  |
| --- |
| Example of Polymarket context prompt |
| ``` MARKET ANALYSIS: Question: US recession in 2025?   - Betting YES current price: 0.050   - Betting NO current price: 0.930   - Betting YES History:   - 2025-10-21: 0.0600 (Change: +0.00 (+9.09%))   - 2025-10-20: 0.0550 (Change: +0.00 (+0.00%))   ...   - 2025-10-12: 0.0650 (Change: +0.00 (+0.00%))   - 2025-10-11: 0.0650 (Change: N/A)   - Betting NO History:   - 2025-10-21: 0.9400 (Change: -0.01 (-0.53%))   - 2025-10-20: 0.9450 (Change: +0.00 (+0.00%))   ...   - 2025-10-12: 0.9350 (Change: +0.00 (+0.00%))   - 2025-10-11: 0.9350 (Change: N/A) ... Question: Russia x Ukraine ceasefire in 2025?     ...  RECENT NEWS: • Fed rate hike in 2025?:   - Fed Interest Rate Predictions for the Next 3 Years: 2025-2027   (2025-10-20)     Expert analysis of interest rate predictions for 2025, 2026, and 2027.     Understand the factors driving rate changes and their impact on consumers and......   - Best CD rates Oct. 21, 2025 (2025-10-20)     Investors need to recognize that average CD rates rise and fall in close alignment     with Federal Reserve monetary policy changes, specifically fluctuations......   - Hawkish BOJ board member keeps up calls for more rate hikes (2025   -10-20)     Japan has a "prime opportunity" to raise interest rates as its economy is     weathering the hit from U.S. tariffs, central bank board member Hajime Takata     said...... ... • Russia x Ukraine ceasefire in 2025?:     ...  ACCOUNT INFO: Recent Historical Allocations under this account:     - Asset Allocation at 2025-10-07: {’Will Gold close under $2,500 at the end of 2025?     _No’: ’0.20’, ’Fed rate hike in 2025?_No’: ’0.15’, ’Tether insolvent in 2025?_No’:     ’0.15’, ’Will 1 Fed rate cut happen in 2025?_No’: ’0.15’, ’Will Google have the top     AI model on December 31?_Yes’: ’0.10’, ’Sundar Pichai out as Google CEO in     2025_No’: ’0.10’, ’USDT depeg in 2025?_No’: ’0.10’, ’CASH’: ’0.05’} (Accumulated     \return rate: -0.1%) ...     - Asset Allocation at 2025-10-20: ... ``` |

Table 7: Example of Polymarket decision prompt.

|  |
| --- |
| Example of Polymarket decision prompt |
| ``` Today is 2025-10-21 (UTC). You are a professional prediction-market portfolio manager. Analyze the market data and generate a complete portfolio allocation. MARKET ANALYSIS: ... RECENT NEWS: ... ACCOUNT INFO: ...  PORTFOLIO MANAGEMENT OBJECTIVE: - For each market, YES and NO are two assets. Allocate to only one at a time. CASH is also valid. - YES and NO prices represent public-implied probabilities. DECISION LOGIC: - Derive market probability p_mkt from price. - Go LONG {question}_YES if p > p_mkt + costs. - Go LONG {question}_NO if p < p_mkt - costs. - ...  PORTFOLIO PRINCIPLES: - Diversify across markets. - No simultaneous YES and NO allocations. - ...  AVAILABLE ASSETS: US recession in 2025?_Yes, US recession in 2025?_No, Tether insolvent in 2025?_Yes, Tether insolvent in 2025?_No, Fed rate hike in 2025?_Yes, Fed rate hike in 2025?_No, USDT depeg in 2025?_Yes, USDT depeg in 2025?_No, Sundar Pichai out as Google CEO in 2025?_Yes, Sundar Pichai out as Google CEO in 2025?_No, Fed emergency rate cut in 2025?_Yes, Fed emergency rate cut in 2025?_No, Russia x Ukraine ceasefire in 2025?_Yes, Russia x Ukraine ceasefire in 2025?_No, CASH  CRITICAL: Return ONLY valid JSON. No extra text. REQUIRED JSON FORMAT: {  "reasoning": "Brief explanation of the allocation",  "allocations": {    "US recession in 2025?_Yes": 0.25,    "Tether insolvent in 2025?_No": 0.15,    "CASH": 0.60  } }  RULES: 1. Return ONLY the JSON object. 2. Allocations must sum to 1.0. 3. Only one side (YES or NO) per question may be non-zero. 4. Use double quotes; no trailing commas. Your objective is to maximize portfolio return using past allocations and performance history. ``` |

![Refer to caption](appendix/pages/leaderboard.png)


Figure 10: Screenshot of the Leaderboard page. This page shows the ranking of each LLM models by profit return.

![Refer to caption](appendix/pages/Stock-Page.png)


Figure 11: Stock Page. This page shows the 21 different LLM Stock models.

![Refer to caption](appendix/pages/Stock-model-card.png)


Figure 12: Stock Model Card.A detailed view of one model card, showing current and historical allocations, profits, and LLM input/output.

![Refer to caption](appendix/pages/polymarket-page.png)


Figure 13: Screenshot of the Polymarket Page. This page shows the 21 different LLM Polymarket models.

![Refer to caption](appendix/pages/polymarket-model-card.png)


Figure 14: Polymarket Model Card. A detailed view of one model card, showing current and historical allocations, profits, and LLM input/output.

![Refer to caption](appendix/pages/news-page.png)


Figure 15: Screenshot of the News Page. This pages shows the news of Stock market and Polymarket. Each news card will direct to the original source.