---
authors:
- Valentin Mohl
- Sascha Frey
- Reuben Leyland
- Kang Li
- George Nigmatulin
- Mihai Cucuringu
- Stefan Zohren
- Jakob Foerster
- Anisoara Calinescu
doc_id: arxiv:2511.02136v1
family_id: arxiv:2511.02136
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning
  for High-Frequency Trading'
url_abs: http://arxiv.org/abs/2511.02136v1
url_html: https://arxiv.org/html/2511.02136v1
venue: arXiv q-fin
version: 1
year: 2025
---


Valentin Mohl
[valentin.mohl@cs.ox.ac.uk](mailto:valentin.mohl@cs.ox.ac.uk)
Department of Computer Science, University of OxfordUnited Kingdom
, 
Sascha Frey
Department of Computer Science, University of OxfordUnited Kingdom
, 
Reuben Leyland
Department of Engineering Science, University of OxfordUnited Kingdom
, 
Kang Li
Department of Statistics, University of OxfordUnited Kingdom
, 
George Nigmatulin
Department of Engineering Science, University of OxfordUnited Kingdom
, 
Mihai Cucuringu
Department of Mathematics, University of California Los AngelesUnited States
  
Department of Statistics & Oxford Man Institute of Quantitative Finance, University of OxfordUnited Kingdom
, 
Stefan Zohren
Department of Engineering Science, University of OxfordUnited Kingdom
, 
Jakob Foerster
Foerster Lab for AI Research, University of OxfordUnited Kingdom
 and 
Anisoara Calinescu
Department of Computer Science, University of OxfordUnited Kingdom

###### Abstract.

Agent-based modelling (ABM) approaches for high-frequency financial markets are difficult to calibrate and validate, partly due to the large parameter space created by defining fixed agent policies. Multi-agent reinforcement learning (MARL) enables more realistic agent behaviour and reduces the number of free parameters, but the heavy computational cost has so far limited research efforts. To address this, we introduce JaxMARL-HFT (JAX-based Multi-Agent Reinforcement Learning for High-Frequency Trading),
the first GPU-accelerated open-source multi-agent reinforcement learning environment for high-frequency trading (HFT) on market-by-order (MBO) data. Extending the JaxMARL framework and building on the JAX-LOB implementation, JaxMARL-HFT is designed to handle a heterogeneous set of agents, enabling diverse observation/action spaces and reward functions. It is designed flexibly, so it can also be used for single-agent RL, or extended to act as an ABM with fixed-policy agents. Leveraging JAX enables up to a 240x reduction in end-to-end training time, compared with state-of-the-art reference implementations on the same hardware. This significant speed-up makes it feasible to exploit the large, granular datasets available in high-frequency trading, and to perform the extensive hyperparameter sweeps required for robust and efficient MARL research in trading. We demonstrate the use of JaxMARL-HFT with independent Proximal Policy Optimization (IPPO) for a two-player environment, with an order execution and a market making agent, using one year of LOB data (400 million orders), and show that these agents learn to outperform standard benchmarks. The code for the JaxMARL-HFT framework is available on [GitHub](https://github.com/vmohl/JaxMARL-HFT)111<https://github.com/vmohl/JaxMARL-HFT>.

limit order book, high-frequency trading, market making, JAX, multi-agent reinforcement learning

## 1. Introduction

Modelling financial markets at high frequency is an inherently difficult problem, as prices emerge endogenously from the interactions of millions of market participants, often acting with bounded rationality and imperfect information. Agent-based modelling (ABM) addresses this by specifying individual agents and allowing the aggregate market behaviour to arise implicitly from their interactions at the micro-level. In most financial contexts, this amounts to simulating behaviour at the most granular level, i.e. orders submitted to the limit order book (LOB), which is the collection of unmatched orders submitted by market participants. However, as such models are mostly based on pre-defined agent policies, previous approaches have been criticised for having too simplistic agent strategies and emergent behaviour. Reinforcement Learning (RL) has been proposed as a potential solution (Frey et al., [2023](https://arxiv.org/html/2511.02136v1#bib.bib13); Ardon et al., [2022](https://arxiv.org/html/2511.02136v1#bib.bib3); Spooner et al., [2018](https://arxiv.org/html/2511.02136v1#bib.bib31)), with most recent work focusing on single-agent RL. To build realistic and robust ABMs with intelligent agents – which learn from each other – we require multi-agent reinforcement learning (MARL) which aims to learn independent policies for a heterogeneous agent population. A natural first step is to successively train RL agents in the single-agent setting, progressively adding their learned policies to the pool of opponent strategies, a form of self-play with differing policy objectives (Mascioli et al., [2024](https://arxiv.org/html/2511.02136v1#bib.bib24)).

To allow for learning in an adversarial context, classical MARL has multiple agents independently collecting experiences and simultaneously updating their policies. To the best of our knowledge, there is no open-source framework for this in an HFT context. One reason for this is the computational restrictions and training instabilities common to MARL experiments, exacerbated by the very low signal-to-noise ratio in financial applications. To overcome these challenges, we require a highly efficient environment to enable large-scale MARL experiments. We therefore present JaxMARL-HFT, the first GPU-enabled MARL environment for HFT on the LOB. Leveraging the power of JAX (Bradbury et al., [2018](https://arxiv.org/html/2511.02136v1#bib.bib7)) and extending the parallelisation of JAX-LOB (Frey et al., [2023](https://arxiv.org/html/2511.02136v1#bib.bib13)) to the multi-agent setting, JaxMARL-HFT is able to achieve up to a 240x reduction in end-to-end training times compared to state-of-the-art implementations on the same hardware. This speed-up allows for extensive hyperparameter sweeps and the processing of tens of thousands of parallel environments, thus unlocking the potential of rich market-by-order (MBO) data sets, such as LOBSTER (Huang and Polak, [2011](https://arxiv.org/html/2511.02136v1#bib.bib17)). The environment is based on the JaxMARL framework (Rutherford et al., [2024](https://arxiv.org/html/2511.02136v1#bib.bib29)), to allow plug-and-play interactions with state-of-the-art MARL algorithms.
It opens up HFT at the most granular level as a complex testbed for evaluating the limits of MARL algorithms.

In Section [2](https://arxiv.org/html/2511.02136v1#S2 "2. Background ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading") we introduce the core concepts used in this paper, and in Section [3](https://arxiv.org/html/2511.02136v1#S3 "3. Related Work ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading") we present an overview of the existing frameworks. Section [4](https://arxiv.org/html/2511.02136v1#S4 "4. Design ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading") presents the design of our implementation, and an overview of the implemented agent archetypes (Section [4.1](https://arxiv.org/html/2511.02136v1#S4.SS1 "4.1. Different Agent Types ‣ 4. Design ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading")) and the changes made to the JaxMARL reference implementation of IPPO (Section [4.2](https://arxiv.org/html/2511.02136v1#S4.SS2 "4.2. IPPO and Heterogeneous Agent Types ‣ 4. Design ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading")). Results for the increased throughput compared to state-of-the-art implementations are discussed in Section [5.1](https://arxiv.org/html/2511.02136v1#S5.SS1 "5.1. Speed Benchmarking ‣ 5. Experimental Setup and Results ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading"). Section [5.2](https://arxiv.org/html/2511.02136v1#S5.SS2 "5.2. MARL: Independent PPO for High-Frequency Trading ‣ 5. Experimental Setup and Results ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading") reports training results and evaluations against baselines of a simple two-player setup. In Section [6](https://arxiv.org/html/2511.02136v1#S6 "6. Conclusion ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading"), we conclude with a summary of our contributions, and future work.

Our main contributions are summarised as follows:

1. (1)

   Extension of the JAX-LOB (Frey et al., [2023](https://arxiv.org/html/2511.02136v1#bib.bib13)) environment to the multi-agent setting, allowing for heterogeneous agents.
2. (2)

   Compatibility with, and extension of, JaxMARL (Rutherford et al., [2024](https://arxiv.org/html/2511.02136v1#bib.bib29)) algorithm implementations.
3. (3)

   Major throughput increase and memory optimisation allowing for training with multiple years of LOBSTER (Huang and Polak, [2011](https://arxiv.org/html/2511.02136v1#bib.bib17)) market-by-order data.
4. (4)

   The code for the JaxMARL-HFT framework is available on [GitHub](https://github.com/vmohl/JaxMARL-HFT)222<https://github.com/vmohl/JaxMARL-HFT>.
5. (5)

   A challenging environment with real-world applications to test the limits of MARL algorithm development.
6. (6)

   Preliminary results showing that, under certain conditions, policies can be learned to outperform baselines, though they require carefully crafted action spaces and reward functions.

## 2. Background

### 2.1. High-Frequency Trading

Limit order books (LOBs) (Gould et al., [2013](https://arxiv.org/html/2511.02136v1#bib.bib16); Bouchaud et al., [2018](https://arxiv.org/html/2511.02136v1#bib.bib6)) are the primary mechanism through which modern financial exchanges operate. Market participants can submit limit orders to express their intention to buy or sell a particular asset at a given price and quantity. As continuous double auction markets, LOBs collect buy and sell limit orders from market participants based on price and time priority, and match compatible orders. Populations of market participants sharing objectives are often classified by trading task. Despite significant intra-class heterogeneity, the formulations of market making, order execution and directional trading prove useful in understanding general population characteristics (Gould et al., [2013](https://arxiv.org/html/2511.02136v1#bib.bib16); Bouchaud et al., [2018](https://arxiv.org/html/2511.02136v1#bib.bib6)). These categories provide mathematical frameworks from which control solutions have been designed.

Market making refers to participants who provide liquidity to an exchange by quoting bid and ask prices, aiming to profit from the spread whilst minimising risks associated with accumulating an inventory of securities.

Order execution is a task performed by participants looking to buy or sell a specified quantity of a security over a pre-determined period. The participants in this task aim to minimise the costs associated with this transaction.

Directional trading refers to the general case where a participant aims to profit from short-term price movements by buying and selling a security without the explicit aim for liquidity provision as in the market making task.

### 2.2. Multi-Agent Reinforcement Learning (MARL)

Multi-agent reinforcement learning is reinforcement learning where multiple agents learn to act in a common environment simultaneously (Rutherford et al., [2024](https://arxiv.org/html/2511.02136v1#bib.bib29)). The increased computational requirements for training multiple agents simultaneously have typically limited MARL developments. Libraries such as JAX (Bradbury et al., [2018](https://arxiv.org/html/2511.02136v1#bib.bib7)) provide a Python interface through which researchers can easily implement hardware acceleration on the GPU and just-in-time (JIT) compilation. Developing MARL environments compatible with JAX acceleration is an active research domain, whilst traditionally environments were designed for the CPU. Rutherford et al. ([2024](https://arxiv.org/html/2511.02136v1#bib.bib29)) present the JaxMARL library to address this problem; they provide a range of open-source MARL environments leveraging JAX for GPU acceleration.

## 3. Related Work

Early research in the domain of agent-based modelling for financial markets demonstrates that interactions between basic zero-intelligence agents are sufficient to replicate some key market phenomena (Palmer et al., [1994](https://arxiv.org/html/2511.02136v1#bib.bib28); Gode and Sunder, [1993](https://arxiv.org/html/2511.02136v1#bib.bib15)) and are capable of explaining a substantial share of the cross-sectional variation in bid-ask spreads (Farmer et al., [2005](https://arxiv.org/html/2511.02136v1#bib.bib12)). However, later studies indicate that capturing certain more nuanced market dynamics, such as price impact (Cui and Brabazon, [2012](https://arxiv.org/html/2511.02136v1#bib.bib10)) or order flow correlation (Vyetrenko et al., [2021](https://arxiv.org/html/2511.02136v1#bib.bib36)), may require agents with more intelligent decision-making capabilities.

More recently, (deep) reinforcement learning has been increasingly applied to different financial trading problems, including in particular directional trading (Théate and Ernst, [2021](https://arxiv.org/html/2511.02136v1#bib.bib33); Liu et al., [2020](https://arxiv.org/html/2511.02136v1#bib.bib21)), market making (Spooner et al., [2018](https://arxiv.org/html/2511.02136v1#bib.bib31); Gašperov et al., [2021](https://arxiv.org/html/2511.02136v1#bib.bib14)) and order execution (Moallemi and Wang, [2022](https://arxiv.org/html/2511.02136v1#bib.bib25); Ning et al., [2021](https://arxiv.org/html/2511.02136v1#bib.bib27)). Some studies have already taken the first steps towards utilising the powerful learning capabilities of RL agents as a more sophisticated version of agent-based modelling for financial markets by leveraging MARL. Lussange et al. ([2021](https://arxiv.org/html/2511.02136v1#bib.bib22)) show that a trading simulation with multiple RL agents, based on daily stock-market data, can reproduce several market statistics, specifically price returns, volatility at different horizons, and autocorrelation metrics. In a subsequent study, they support these findings by extending their analysis to daily cryptocurrency closing price data (Lussange et al., [2024](https://arxiv.org/html/2511.02136v1#bib.bib23)). Ardon et al. ([2022](https://arxiv.org/html/2511.02136v1#bib.bib3)) train multiple RL agents that act either as liquidity takers or as liquidity providers, coupled with a stochastic background model following Cont and Muller ([2021](https://arxiv.org/html/2511.02136v1#bib.bib9)), and demonstrate that groups of agents can learn a wide spectrum of different behaviours. Extending this approach, Yao et al. ([2024](https://arxiv.org/html/2511.02136v1#bib.bib38)) also employ agents of those two types, but remove the background order‑book model. Using one day of tick‑level order book data from the LOBSTER dataset (Huang and Polak, [2011](https://arxiv.org/html/2511.02136v1#bib.bib17)), they show that the resulting simulation reproduces several stylised facts observed in the real data. Yao et al. ([2024](https://arxiv.org/html/2511.02136v1#bib.bib38)) also highlight the extensive computational resources required for their training setup. These computational requirements have generally limited the scale of previous MARL research for HFT, or enforced simplified approaches such as stochastic background models instead of data-driven development.

High computational cost and long training times are common problems in MARL applications beyond finance, motivating the development of JaxMARL (Rutherford et al., [2024](https://arxiv.org/html/2511.02136v1#bib.bib29)), a JAX‑based (Bradbury et al., [2018](https://arxiv.org/html/2511.02136v1#bib.bib7)) framework that provides a range of classical MARL algorithms and environments. Our work extends JaxMARL and unlocks the benefits of GPU-accelerated MARL for a real‑world–relevant and highly challenging application: modelling financial markets at HFT scales. Based on the JAX-LOB simulator (Frey et al., [2023](https://arxiv.org/html/2511.02136v1#bib.bib13)), we present a flexible MARL environment that delivers a substantial RL training speed‑up. Using GPU acceleration to advance MARL research has been used in application domains beyond the environments presented in JaxMARL, most notably for self-driving, where it has seen significant success (Cusumano-Towner et al., [2025](https://arxiv.org/html/2511.02136v1#bib.bib11); Kazemkhani et al., [2025](https://arxiv.org/html/2511.02136v1#bib.bib19)). Nevertheless, these examples were not implemented in JAX, but based on an engine (Shacklett et al., [2023](https://arxiv.org/html/2511.02136v1#bib.bib30)) written in C++ code compiled to the GPU.

We open-source our implementation, which places it within the current lineage of publicly available ABM frameworks for high-fidelity LOB trading, such as MAXE (Belcak et al., [2022](https://arxiv.org/html/2511.02136v1#bib.bib5)), ABIDES (Byrd et al., [2020](https://arxiv.org/html/2511.02136v1#bib.bib8)), and PyMarketSim (Mascioli et al., [2024](https://arxiv.org/html/2511.02136v1#bib.bib24)). These frameworks support heterogeneous agents that submit synthetic orders to a simulated limit‑order book, enabling controlled studies of market microstructure. ABIDES is complemented by the ABIDES‑gym extension (Amrouni et al., [2022](https://arxiv.org/html/2511.02136v1#bib.bib2)), which adds an interface for deep reinforcement learning and has already underpinned RL studies on optimal order execution (Karpe et al., [2020](https://arxiv.org/html/2511.02136v1#bib.bib18); Lin and Beling, [2021](https://arxiv.org/html/2511.02136v1#bib.bib20)) and market making (Vicente et al., [2022](https://arxiv.org/html/2511.02136v1#bib.bib35)). PyMarketSim (Mascioli et al., [2024](https://arxiv.org/html/2511.02136v1#bib.bib24)) also provides a limit‑order‑market environment populated by a range of heuristic traders and additionally offers training strategic agents with deep reinforcement learning. It also supplies a simplified MARL facility via the Policy‑Space Response Oracles procedure, whereby, in each iteration, a single best‑response policy is trained via reinforcement learning against the current mixed‑strategy equilibrium, then frozen and added to the global strategy pool before the equilibrium is recomputed. Overall, JaxMARL-HFT departs from existing ABM frameworks in two key aspects: it leverages GPU-acceleration for a significant RL training speed-up, and adopts a classical, fully concurrent MARL paradigm, enabling researchers to use existing algorithm implementations, such as those available in JaxMARL.

## 4. Design

We design JaxMARL-HFT as a LOB-level MARL environment in JAX (Bradbury et al., [2018](https://arxiv.org/html/2511.02136v1#bib.bib7)). It is built on JAX-LOB (Frey et al., [2023](https://arxiv.org/html/2511.02136v1#bib.bib13)) and it is compatible with JaxMARL (Rutherford et al., [2024](https://arxiv.org/html/2511.02136v1#bib.bib29)). It follows a classical MARL framework, enabling multiple reinforcement-learning agents to interact both with each other and with historical LOB message streams.

Leveraging JAX has three key performance advantages (Bradbury et al., [2018](https://arxiv.org/html/2511.02136v1#bib.bib7); Rutherford et al., [2024](https://arxiv.org/html/2511.02136v1#bib.bib29)). First, JAX’s vectorised mapping (vmap) allows for parallelisation across thousands of GPU threads. Second, the framework benefits from JAX’s just-in-time (JIT) compilation, which automatically fuses operations into an optimised kernel and eliminates Python overhead. Third, as both environment rollouts and learning updates are executed on the GPU, the data-transfer latency arising between CPU and GPU in conventional implementations is removed.

![Refer to caption](Plots/Design.png)


Figure 1. The two levels of parallelisation on the GPU with vectorised mapping (vmap) in JAX.

We employ the vmap parallelisation in two different ways, as illustrated in Figure [1](https://arxiv.org/html/2511.02136v1#S4.F1 "Figure 1 ‣ 4. Design ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading"). First, we partition the dataset into individual episodes. The start and the length of each episode can be chosen flexibly; episodes may even be specified to overlap. At the beginning of each episode, the LOB is initialised as described in Frey et al. ([2023](https://arxiv.org/html/2511.02136v1#bib.bib13)), using the current state of the book at that time. With vmap, we can then process these episodes in parallel. We make a significant improvement compared to JAX-LOB in how messages are loaded on the GPU memory at initialisation. Rather than loading the data in windows, as described in Figure 1 of Frey et al. ([2023](https://arxiv.org/html/2511.02136v1#bib.bib13)), we load all messages of the dataset in contiguous form and instead keep careful track of the indices where episodes start, and index the data at runtime. This avoids excessive padding and allows a year’s worth of pre-processed AMZN order data to occupy just 4GB of GPU memory, which was not possible in the original implementation.

Second, we parallelise across agents of the same type, at every step within an episode. The reason we do not vmap over all agents indiscriminately is JAX-specific: the underlying arrays of the functions (e.g. generating observations or constructing the LOB message based on the action of an agent) must have identical shapes across agents. Since JaxMARL-HFT is designed with the goal of maximum flexibility, allowing for heterogeneous observation spaces, action spaces and reward functions, this is generally not the case. One possible workaround would be the utilisation of padding, but we aim to keep the possibility for highly diverse agents, e.g. those whose observation spaces only contain a handful of hand-coded features versus those whose observations comprise tokenized messages that could be orders of magnitude larger. In these cases, padding would be extremely inefficient. To preserve flexibility, we iterate in an outer Python for-loop over agent types and vmap only over instances of the same type, as depicted in Figure [1](https://arxiv.org/html/2511.02136v1#S4.F1 "Figure 1 ‣ 4. Design ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading"). This procedure strikes a good balance: it makes use of the benefits of GPU parallelisation, while maintaining support for heterogeneous agents.

A single environment step is structured as follows:

1. (1)

   Action Conversion:
   Agent actions are transformed into LOB messages based on the chosen action space. Unless new messages are at the same price-level, cancellation messages are prepared for unmatched orders from the previous step.
2. (2)

   Random shuffling:
   All agent messages are randomly shuffled, so there is no ordering in how agents act.
3. (3)

   Augment with market-replay messages:
   The cancellation and action messages generated by the agents are concatenated with a background stream of historical messages, in this order. Because the environment is modular, these can be replaced by another background model, e.g. a generative model such as in Nagy et al. ([2023](https://arxiv.org/html/2511.02136v1#bib.bib26)), with some additional implementation.
4. (4)

   Processing by JAX-LOB: Orders are processed by the JAX-LOB simulator as described in (Frey et al., [2023](https://arxiv.org/html/2511.02136v1#bib.bib13)), and the resulting trades are recorded.
5. (5)

   Calculate step outcomes:
   Rewards, auxiliary information, termination flags, and observations are computed. These are used by the agents to determine their next action.

### 4.1. Different Agent Types

Two heterogeneous agent categories are implemented, covering three HFT tasks, each comprising a set of action spaces, observation spaces, and reward functions.

#### 4.1.1. Market Making

The market making agent implementation supports three action space configurations, providing a diverse set of strategies and a range of task complexities. The Spread-Skew action space is a simplified version of the action space used by Ardon et al. ([2022](https://arxiv.org/html/2511.02136v1#bib.bib3)), with tabular actions used in place of spread-skew parameters. The Fixed Quantity action space is inspired by the work of Spooner et al. ([2018](https://arxiv.org/html/2511.02136v1#bib.bib31)). Finally, the AvSt action space is a parametrised form of the optimal control solution presented by Avellaneda and Stoikov ([2008](https://arxiv.org/html/2511.02136v1#bib.bib4)), similar to the implementation in Ardon et al. ([2022](https://arxiv.org/html/2511.02136v1#bib.bib3)).

In these action spaces, the agent selects bid and ask prices to present to the market from a pre-determined selection of strategies. For example in the Fixed Quantity space, the agent has 8 options; (i) Not trading; (ii)/(iii) Posting 2 and 4, respectively, ticks away from the best prices; (iv) trading one tick into the spread; (v)/(vi) Posting 2 ticks away from the spread on either side of the book; (vii)/(viii) Posting 5 ticks away from the best price on one side, and 1 tick into the spread on the other.

The quantity associated with each order is fixed a priori through an environment configuration variable: the agents following these strategies will quote constant volumes associated with each bid and ask message. In practice, this quantity can be set to the minimum lot size, which, depending on the asset price, is often the most commonly used trade size by market participants, making this assumption reasonably realistic.

Similar to our approach to action spaces, we design flexible reward functions. We include rewards based on Vadori et al. ([2024](https://arxiv.org/html/2511.02136v1#bib.bib34)) and Spooner et al. ([2018](https://arxiv.org/html/2511.02136v1#bib.bib31)), which include spread and inventory PnL terms, with variable weights given to each term, to allow diverse agent risk tolerances. All functions are parameterised by adjustable hyperparameters, which presents the user with a highly diverse set of possible reward functions.

For the observation space, the market making agents are presented with a one-dimensional array containing statistics related to the agents’ task, such as the size of their current inventory. We implement multiple similar observation spaces, with a range of complexities, allowing the user to select an observation space with a level of detail appropriate for their use case.

#### 4.1.2. Order Execution

We base the order execution agent on the environment presented by Frey et al. ([2023](https://arxiv.org/html/2511.02136v1#bib.bib13)). We discretise the action space, so that rather than selecting a quantity to post at each of the four reference prices, the agent selects only at which price to submit an order of a quantity defined a priori. A more complex version extends this, to additionally allow orders with multiples of 2 or 5 of this quantity. The pre-defined order quantity is selected based on the execution task size and episode length.

#### 4.1.3. Directional Trading

Finally, we implement a directional trading action space as a configuration of the market making class, re-using all reward functions and observation spaces. The similarities between these tasks justify this approach; however, we develop a unique action space, to ensure diversity between the classes. The directional trading action space enables the agent to either send a bid or ask order at the best price, or do nothing at each step. All bid and ask messages quote a fixed quantity.

### 4.2. IPPO and Heterogeneous Agent Types

JaxMARL (Rutherford et al., [2024](https://arxiv.org/html/2511.02136v1#bib.bib29)) includes MARL algorithm implementations. Given the different classes of agents described previously, we need to extend these implementations to be compatible with our environment. This is relatively easy for an algorithm like independent PPO, as we simply maintain separate networks, observations, hidden states, and actions for each agent type, iterating over them during rollout and at update steps. Agents of the same type continue to benefit from efficient batch operations during training, as they do for environment rollouts. We opt not to go into great detail on the algorithmic details of IPPO, but highlight that all agents retain separate network weights, and thus only learn about adversarial behaviour from environment observations, not through shared weights.

## 5. Experimental Setup and Results

Table 1. Speed comparison between JaxMARL‑HFT, PyMarketSim, ABIDES, and CPU‑MARL. For JaxMARL-HFT, ABIDES-gym and CPU-MARL we used the RL pipeline with a random policy. We parallelise across 4000 environments (50 steps per environment) on a single GPU for JaxMARL-HFT and 64 CPU cores (one thread per core) for ABIDES-gym and CPU-MARL. For PyMarketSim, we use their non-parallelised, purely zero-intelligence (ZI) agents-based simulation on 1 CPU core, matching the number of ZI agents to the sum of messages and random-policy agents in the other settings. JaxMARL-HFT and the CPU-MARL employ 2 types of agents (with a varying number of agents), whereas for PyMarketSim and ABIDES there is only 1 agent. Since PyMarketSim and ABIDES-gym do not offer classical MARL, the corresponding entries for multiple agents per type are left blank.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| JaxMARL-HFT | | | | PyMarketSim | ABIDES-gym | CPU-MARL |
| Data Messages per Step | Agents per Type | Time (s) | Steps/s | Steps/s | Steps/s | Steps/s |
| 100 | 1 | 9.104 | 21969 | 463 | 734 | 1805 |
| 1 | 1 | 0.570 | 351119 | 10830 | 2979 | 4896 |
| 100 | 5 | 13.513 | 14801 | - | - | 84 |
| 1 | 5 | 2.246 | 89062 | - | - | 334 |
| 100 | 10 | 18.650 | 10724 | - | - | 30 |
| 1 | 10 | 4.140 | 48312 | - | - | 114 |

### 5.1. Speed Benchmarking

To properly evaluate our environment, we compare it to closely related state‑of‑the‑art implementations. Some of the most similar publicly available frameworks that support multi-agent simulations in HFT are ABIDES-gym (Amrouni et al., [2022](https://arxiv.org/html/2511.02136v1#bib.bib2)) and PyMarketSim (Mascioli et al., [2024](https://arxiv.org/html/2511.02136v1#bib.bib24)). Although these implementations permit simulations using multiple heterogeneous background agents with pre-defined policies, both focus on updating a single reinforcement learning agent; additional agents may interact with the learning agent but do not learn concurrently. Investigating the source-code of ABIDES-gym shows that future support for MARL was planned but does not seem currently supported. PyMarketSim takes a step closer to MARL through its policy‑space response oracles, which can be used to train successive RL agents, fixing their policies and adding them to a pool of possible policies, but does not allow for simultaneous learning. We compare to ABIDES-gym and PyMarketSim, despite the inexact match, as these represent the most similar open-source baselines. Additionally, to obtain an exact speed benchmark and to quantify the contribution of GPU acceleration, we implement a CPU version of our MARL environment, which we refer to as CPU-MARL.

We use the open-source code of ABIDES‑gym and PyMarketSim to compare all implementations on the same hardware. For our experiments, we use a fairly typical compute node for deep learning in academic contexts with up to 8 NVIDIA L40S GPUs and an AMD EPYC 9554 processor with 64 cores (256 threads) available.

#### 5.1.1. Speed of the Environment

Table [1](https://arxiv.org/html/2511.02136v1#S5.T1 "Table 1 ‣ 5. Experimental Setup and Results ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading") depicts the environment‑step throughput without learning updates. To ensure a fair comparison, we aim to harmonise the dynamics and configuration settings across frameworks, since they differ in several implementation details. In JaxMARL‑HFT, in each step both historical market‑replay LOBSTER data messages and messages generated by RL agents are processed. For JaxMARL-HFT and CPU-MARL, we consider a different number of agents of two different types: market making and order execution. In the results shown in Table [1](https://arxiv.org/html/2511.02136v1#S5.T1 "Table 1 ‣ 5. Experimental Setup and Results ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading"), these RL agents choose random actions and no learning updates are performed. PyMarketSim, by contrast, does not use market‑replay data. Instead, market activity is generated by background agents (e.g., zero‑intelligence agents) that submit orders. We therefore instantiate PyMarketSim with the same total number of zero‑intelligence agents as the sum of data messages and random RL agents in JaxMARL‑HFT and CPU-MARL. Because agent arrival times in PyMarketSim follow a geometric distribution, we adjust this distribution so that, in expectation, every agent acts in every step. The simulation using only background agents is not parallelised across CPU cores in PyMarketSim, however their reinforcement learning process - which is based on the Tianshou package of Weng et al. ([2022](https://arxiv.org/html/2511.02136v1#bib.bib37)) - is parallelised, and we report a comparison with their parallelised RL pipeline across 64 cores in Section [5.1.2](https://arxiv.org/html/2511.02136v1#S5.SS1.SSS2 "5.1.2. Speed of Multi-Agent Reinforcement Learning Training ‣ 5.1. Speed Benchmarking ‣ 5. Experimental Setup and Results ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading"). For ABIDES-gym, environment step frequency is not defined by number of messages, but by simulation time, we use the rmsc04 reference configuration and empirically adjust the inter-step time to have 1 and 100 orders processed on average. As illustrated in Table [1](https://arxiv.org/html/2511.02136v1#S5.T1 "Table 1 ‣ 5. Experimental Setup and Results ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading"), JaxMARL-HFT achieves a substantial speed-up relative to current state-of-the-art reference implementations and the comparable CPU-based MARL environment, which seems to increase with the number of agents.

#### 5.1.2. Speed of Multi-Agent Reinforcement Learning Training

![Refer to caption](Plots/rl_steps.png)


Figure 2. Speed Comparison of the Reinforcement Learning Training Pipeline††:

The key advantages of GPU-acceleration become apparent when considering the MARL training loop. Unlike current state-of-the-art frameworks, which typically execute environment rollouts on the CPU and perform policy updates on the GPU, our system carries out both the environment rollouts and the RL updates entirely on the GPU.

With respect to the results in Figure [2](https://arxiv.org/html/2511.02136v1#acmlabel1 "Figure 2 ‣ 5.1.2. Speed of Multi-Agent Reinforcement Learning Training ‣ 5.1. Speed Benchmarking ‣ 5. Experimental Setup and Results ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading"), it is important to emphasise that, in this comparison, only JaxMARL-HFT and CPU-MARL conduct MARL with several learning agents concurrently. By contrast, the results for PyMarketSim and ABIDES-gym each encompass only a single agent updating its policy. We endeavoured to make the comparison as fair as possible and to harmonise hyperparameters. All implementations perform their RL updates on an NVIDIA L40S GPU. ABIDES-gym, PyMarketSim, CPU-MARL additionally use an AMD EPYC 9554 processor for their environment rollouts (64 parallel environments on 64 cores with 1 thread per core, i.e. no simultaneous multithreading). For JaxMARL-HFT 4096 environments are used in parallel on the GPU.

Figure [2](https://arxiv.org/html/2511.02136v1#acmlabel1 "Figure 2 ‣ 5.1.2. Speed of Multi-Agent Reinforcement Learning Training ‣ 5.1. Speed Benchmarking ‣ 5. Experimental Setup and Results ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading") depicts the significant speed advantages of a fully GPU-accelerated framework. The performance benefit becomes particularly pronounced as the number of learning agents increases. While the speed-up for a single agent of each type is approximately 5x - 35x, it rises to 95x - 125x for five agents. For ten agents, we even observe a 200x - 240x speed improvement. Additionally, a JAX-based implementation makes it straightforward to distribute across multiple GPUs through leveraging JAX’s pmap capabilities. Comparing the implementations when the entire node is used, i.e. 8 GPUs and 256 workers benefiting from multi-threading, the throughput increases by a factor of 50 when comparing JaxMARL-HFT to ABIDES-gym in the single-agent case for 100 messages per step.

We notice significant differences in the increased throughput between implementations when varying the number of LOB messages processed per RL-step. For example, comparing 1 GPU to the next-best PyMarketSim, we see an increase in throughput of 5.5x versus 40x for 100 and 1 messages, respectively. This strongly underlines the obtained benefits when frequent model inference steps are required on the GPU: data does not need to be continuously transferred between devices in the JaxMARL-HFT implementation.

### 5.2. MARL: Independent PPO for High-Frequency Trading

#### 5.2.1. Training curves and learned policies

Using the adapted IPPO framework (Section [4.2](https://arxiv.org/html/2511.02136v1#S4.SS2 "4.2. IPPO and Heterogeneous Agent Types ‣ 4. Design ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading")), a two-player environment is considered, containing a market making and an execution agent, learning simultaneously in the MARL environment. An overview of the specifications for each of the agents is given in Table [2](https://arxiv.org/html/2511.02136v1#S5.T2 "Table 2 ‣ 5.2.1. Training curves and learned policies ‣ 5.2. MARL: Independent PPO for High-Frequency Trading ‣ 5. Experimental Setup and Results ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading"). We use a GRU-based network architecture to ensure recurrence can identify time-dependent patterns in the data, as described in (Frey et al., [2023](https://arxiv.org/html/2511.02136v1#bib.bib13)).

Table 2. Key parameters used by the agents considered in Section [5.2](https://arxiv.org/html/2511.02136v1#S5.SS2 "5.2. MARL: Independent PPO for High-Frequency Trading ‣ 5. Experimental Setup and Results ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading"), where square brackets indicate multiple options were considered in the presented results.

|  |  |
| --- | --- |
| Parameter | Value |
| Dataset | AMZN 2024 |
| Episode start frequency | Every 64 steps |
| Episode length | 64 steps |
| Data messages/step | 100 |
| JAX-LOB book capacity | 100 orders |
| MM: Action Spaces | [SpreadSkew, FixedQuant] |
| MM: Reward Functions | [BuySell, Spooner] |
| MM: Value reference price | [Mid Price, Best Price] |
| MM: Inventory penalty | [Quadratic, None] |
| MM: Quadratic penalty fact. ρ\rho | 50 |
| MM/EXEC: Order size | 10 |
| EXEC: Task direction | Uniformly sampled |
| EXEC: Action Space | Complex (Sec. [4.1.2](https://arxiv.org/html/2511.02136v1#S4.SS1.SSS2 "4.1.2. Order Execution ‣ 4.1. Different Agent Types ‣ 4. Design ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading")) |
| EXEC: Reward func. | See Frey et al. ([2023](https://arxiv.org/html/2511.02136v1#bib.bib13)) |
| EXEC: Reward λ\lambda | 0.0 |
| EXEC: Task size | 600 |
| EXEC: Unfilled order penalty | [0.1,0.05,0.01] |

The nature and relatively large number of parameters in Table [2](https://arxiv.org/html/2511.02136v1#S5.T2 "Table 2 ‣ 5.2.1. Training curves and learned policies ‣ 5.2. MARL: Independent PPO for High-Frequency Trading ‣ 5. Experimental Setup and Results ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading") illustrates one of the open problems with MARL for high-frequency financial applications: stable training is difficult with general-purpose action spaces and multidimensional observation spaces depicting the total state of the LOB. We therefore content ourselves, for the purpose of illustrating the functionality of JaxMARL-HFT, with strongly-simplified action and observation spaces. Multi-modality on the optimal actions is a reason for which the action spaces are discretised into a relatively small number of distinct classes, rather than allowing more general, continuous action space described in Frey et al. ([2023](https://arxiv.org/html/2511.02136v1#bib.bib13)).

![Refer to caption](Plots/TrainingCurves.png)


(a) Market making training curve showing portfolio value. Curves are shown for different reward functions and action spaces (Red/Green/Blue). Further, the effect of a quadratic inventory penalty term and the reference price for portfolio value calculation is considered.

![Refer to caption](Plots/SlippageExec.png)


(b) Execution agent training curve showing ablations over the end-of-episode reward penalty. Except for the first updates, there is no major difference as avoiding this penalty is learned very quickly.

Figure 3. Training curves using a proxy reward to aid comparison across reward functions. MARL experiment with a market making and an execution agent. ††:

Nevertheless, with such settings, we observe some promising results. Figure [3(a)](https://arxiv.org/html/2511.02136v1#S5.F3.sf1 "In Figure 3 ‣ 5.2.1. Training curves and learned policies ‣ 5.2. MARL: Independent PPO for High-Frequency Trading ‣ 5. Experimental Setup and Results ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading") shows the training curves for two of the more promising action-spaces (SpreadSkew and FixedQuant), for market making. It is important to note that in both cases, we show a proxy value to measure the ability of the agent to execute the given task, which is not necessarily the reward function. We use the portfolio value (P​VPV) ([1](https://arxiv.org/html/2511.02136v1#S5.E1 "In 5.2.1. Training curves and learned policies ‣ 5.2. MARL: Independent PPO for High-Frequency Trading ‣ 5. Experimental Setup and Results ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading")) as a measure for the market maker, and the Slippage ([2](https://arxiv.org/html/2511.02136v1#S5.E2 "In 5.2.1. Training curves and learned policies ‣ 5.2. MARL: Independent PPO for High-Frequency Trading ‣ 5. Experimental Setup and Results ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading")) adjusted for the direction of the execution task. This is because it allows for a comparison across different reward functions. Pr​e​fP\_{ref} is generally chosen to be the mid price, but we show an example in Figure [3(a)](https://arxiv.org/html/2511.02136v1#S5.F3.sf1 "In Figure 3 ‣ 5.2.1. Training curves and learned policies ‣ 5.2. MARL: Independent PPO for High-Frequency Trading ‣ 5. Experimental Setup and Results ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading") where the reference price is the far-touch price instead.

|  |  |  |  |
| --- | --- | --- | --- |
| (1) |  | P​V=Qi​n​v×Pr​e​f+C​a​s​hPV=Q\_{inv}\times P\_{ref}+Cash |  |

|  |  |  |  |
| --- | --- | --- | --- |
| (2) |  | S​l​i​p​p​a​g​e=(−1)d​i​r​∑jQj​(Pj−Pi​n​i​t)Slippage=(-1)^{dir}\sum\_{j}Q\_{j}(P\_{j}-P\_{init}) |  |

For example, in Figure [3(a)](https://arxiv.org/html/2511.02136v1#S5.F3.sf1 "In Figure 3 ‣ 5.2.1. Training curves and learned policies ‣ 5.2. MARL: Independent PPO for High-Frequency Trading ‣ 5. Experimental Setup and Results ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading") we show the differences in training when applying different reward functions: the ’Spooner’ reward ([3](https://arxiv.org/html/2511.02136v1#S5.E3 "In 5.2.1. Training curves and learned policies ‣ 5.2. MARL: Independent PPO for High-Frequency Trading ‣ 5. Experimental Setup and Results ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading")) from Spooner and Savani ([2021](https://arxiv.org/html/2511.02136v1#bib.bib32)) (in Red), and the ’BuySell’ reward based on instantaneous differences of trade prices to the mid price ([4](https://arxiv.org/html/2511.02136v1#S5.E4 "In 5.2.1. Training curves and learned policies ‣ 5.2. MARL: Independent PPO for High-Frequency Trading ‣ 5. Experimental Setup and Results ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading")) (in Blue). Following Spooner and Savani ([2021](https://arxiv.org/html/2511.02136v1#bib.bib32)), we define trading PnL terms as Ψb=∑(M¯−Pb)​Qb\Psi\_{b}=\sum(\bar{M}-P\_{b})Q\_{b} and Ψs=∑(Pa−M¯)​Qa\Psi\_{s}=\sum(P\_{a}-\bar{M})Q\_{a}, with M¯\bar{M} representing the average mid price over the previous step and QQ and PP representing bid or ask prices and quantities, respectively. We define the inventory PnL similarly as ΨINV=It​(Mt−Mt−1)\Psi\_{\text{INV}}=I\_{t}(M\_{t}-M\_{t-1}), where the configurable hyperparameter λ\lambda controls the relative weighting of positive and negative PnL, and MtM\_{t} and ItI\_{t} denote the mid price and inventory at time step tt.

|  |  |  |  |
| --- | --- | --- | --- |
| (3) |  | rSp=Ψb+Ψs+ΨINV−(1−λ)​max⁡(0,ΨINV)r\_{\text{Sp}}=\Psi\_{b}+\Psi\_{s}+\Psi\_{\text{INV}}-(1-\lambda)\max(0,\Psi\_{\text{INV}}) |  |

|  |  |  |  |
| --- | --- | --- | --- |
| (4) |  | rb​u​y−s​e​l​l=Ψb+Ψsr\_{buy-sell}=\Psi\_{b}+\Psi\_{s} |  |

Further, the effect of a quadratic reward penalty on the held inventory (Dark Blue/Red) is considered. We observe that such a penalty is beneficial, as is the use of the Spooner reward function, which itself depends on the held inventory. It is important to highlight that despite convergence of the loss and reward in both training and validation data, none of the learned strategies for market making are able to make net profits, but instead lose approximately 0.2 ticks on average. Section [5.2.2](https://arxiv.org/html/2511.02136v1#S5.SS2.SSS2 "5.2.2. Evaluation against baseline strategies ‣ 5.2. MARL: Independent PPO for High-Frequency Trading ‣ 5. Experimental Setup and Results ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading") shows that this is still a surprisingly good result. It is assumed that one of the hindering factors which makes profitable market making difficult is the fact that posted orders from previous steps are cancelled at each RL step. This is a marked disadvantage in a price-time priority LOB. Addressing this requires revisiting the environment design, and is left for future work.

Figure [3(b)](https://arxiv.org/html/2511.02136v1#S5.F3.sf2 "In Figure 3 ‣ 5.2.1. Training curves and learned policies ‣ 5.2. MARL: Independent PPO for High-Frequency Trading ‣ 5. Experimental Setup and Results ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading") shows the training evolution in the execution environment for different coefficients for the end-of-episode penalty when the given amount is not executed successfully. Clearly, a lower value implies a larger reward early on, but the network quickly learns to avoid the costly penalty, after which the difference is negligible.

![Refer to caption](Plots/action_distribution_plot.png)


(a) Market making action distribution for the three actions played with non-zero probability. Most commonly, the agent opts not to trade, this is exacerbated by an inventory penalty. The remaining time, the agent posts orders deep in the book on one side, and into the spread on the other. See Section [4.1.1](https://arxiv.org/html/2511.02136v1#S4.SS1.SSS1 "4.1.1. Market Making ‣ 4.1. Different Agent Types ‣ 4. Design ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading") for details.

![Refer to caption](Plots/Quant_Left_TrajPlot.png)


(b) Example for a single episode of the learned policy behaviour compared to the baseline. The agent learns to trade much more quickly, but still has lower execution costs than an aggressive TWAP strategy, likely capturing some of the spread on occasion.

Figure 4. Detailed plots considering the behaviour of the learned policies for each agent. Results are given for policies learned using the FixedQuant action space with the Spooner reward function and a Quadratic inventory penalty for the market maker.††:

Digging deeper into the learned policies, we see that the market makers (Figure [4(a)](https://arxiv.org/html/2511.02136v1#S5.F4.sf1 "In Figure 4 ‣ 5.2.1. Training curves and learned policies ‣ 5.2. MARL: Independent PPO for High-Frequency Trading ‣ 5. Experimental Setup and Results ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading")) learn to trade very infrequently, which explains the convergence towards zero portfolio value in Figure [3](https://arxiv.org/html/2511.02136v1#S5.F3 "Figure 3 ‣ 5.2.1. Training curves and learned policies ‣ 5.2. MARL: Independent PPO for High-Frequency Trading ‣ 5. Experimental Setup and Results ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading"). The only actions which are sampled with non-zero frequency are strong skews with orders deep into one side of the book, and into the spread on the other. One of the drawbacks of this family of reward functions is that they are not normalised by traded volume, as in this case, an optimal policy seems to be to never trade, thus guaranteeing no losses. Choosing an action space which forces the agent to submit orders at every step is an alternative, but considering the green line in Figure [3(a)](https://arxiv.org/html/2511.02136v1#S5.F3.sf1 "In Figure 3 ‣ 5.2.1. Training curves and learned policies ‣ 5.2. MARL: Independent PPO for High-Frequency Trading ‣ 5. Experimental Setup and Results ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading") showing results for the SpreadSkew action space suggests this will result in markedly reduced performance.

For execution, we see that the learned policy is generally far more aggressive than the TWAP baseline strategy (Figure [4(b)](https://arxiv.org/html/2511.02136v1#S5.F4.sf2 "In Figure 4 ‣ 5.2.1. Training curves and learned policies ‣ 5.2. MARL: Independent PPO for High-Frequency Trading ‣ 5. Experimental Setup and Results ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading")), likely due to the end-of-episode penalty still being significant. Section [5.2.2](https://arxiv.org/html/2511.02136v1#S5.SS2.SSS2 "5.2.2. Evaluation against baseline strategies ‣ 5.2. MARL: Independent PPO for High-Frequency Trading ‣ 5. Experimental Setup and Results ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading") shows that execution cost can be decreased by up to 20% of a tick on average as compared to TWAP, likely by trading more passively, whilst still guaranteeing execution.

#### 5.2.2. Evaluation against baseline strategies

![Refer to caption](Plots/pnl_baseline_vs_learned_triangular.png)


Figure 5. Evaluation of the learned agents when facing baseline implementations (TWAP and AvSt (Avellaneda and Stoikov, [2008](https://arxiv.org/html/2511.02136v1#bib.bib4))). The bottom left has both agents play a baseline policy, whilst the top right has both play a learnt policy. The bottom triangles represent the market maker portfolio value, whilst the top represent the slippage experienced by the execution agent. The learnt policies improve over the baseline, and the execution agent performs worse when facing a learnt market making policy than when facing the baseline.††:

Figure [5](https://arxiv.org/html/2511.02136v1#S5.F5 "Figure 5 ‣ 5.2.2. Evaluation against baseline strategies ‣ 5.2. MARL: Independent PPO for High-Frequency Trading ‣ 5. Experimental Setup and Results ‣ JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading") shows the respective improvements of the learned policies (L) using the Fixed Quant action space with the Spooner reward function and a quadratic inventory penalty term. The baselines (B) are TWAP in the case of the execution agent and the Avellaneda-Stoikov optimal market making model (Avellaneda and Stoikov, [2008](https://arxiv.org/html/2511.02136v1#bib.bib4)) in the case of the market making agent. Both baselines are outperformed by the learned agent in terms of their respective quality metrics (Portfolio Value and Slippage). Further, the matrix view shows that having a more strategic execution opponent decreases the performance, underlining the expected benefits of MARL when it comes to modelling indirect market impact. We leave an in-depth study of this adversarial behaviour for future work.

## 6. Conclusion

We present the first framework allowing for highly parallelised, GPU-accelerated MARL experiments for HFT. It provides a real-world-relevant and challenging multi-agent environment and is fully compatible with state-of-the-art MARL algorithms implemented in JaxMARL. The new framework contains heterogeneous implementations of the three main HFT agent tasks: order execution, market making, and directional trading. Compared to similar state-of-the-art implementations, throughput is increased by up to 240x allowing for larger models, bigger datasets, and more extensive hyperparameter sweeps. Early results show learned policies that outperform existing baseline policies and show some promising adversarial behaviour.

This novel comprehensive framework sets the stage for many future research directions: (i) Measuring the market impact obtained in simulation with learned agent policies; (ii) Moving to general-purpose action/observation spaces and only parametrising agent behaviour through the reward function; (iii) Replacing historical message data with generative models to train RL-agents in adversarial settings, even in the single-agent case; (iv) Removing historical message data after training, and considering the resulting price-series of a multi-agent model with learned agent policies; (v) As simulation allows the labelling of the origin of submitted orders, this facilitates new research in opponent shaping and market participant classification.

###### Acknowledgements.

AC acknowledges funding from a UKRI AI World Leading Researcher Fellowship (grant EP/W002949/1). AC and JF acknowledge funding from a JPMC Faculty Research Award. We thank Peer Nagy, Bidipta Sarkar and Zilin Wang for valuable feedback and discussions.

## References

* (1)
* Amrouni et al. (2022)

  Selim Amrouni, Aymeric Moulin, Jared Vann, Svitlana Vyetrenko, Tucker Balch, and Manuela Veloso. 2022.
  ABIDES-gym: gym environments for multi-agent discrete event simulation and application to financial markets. In *Proceedings of the Second ACM International Conference on AI in Finance* *(ICAIF ’21)*.
* Ardon et al. (2022)

  Leo Ardon, Nelson Vadori, Thomas Spooner, Mengda Xu, Jared Vann, and Sumitra Ganesh. 2022.
  Towards a fully RL-based market simulator. In *Proceedings of the Second ACM International Conference on AI in Finance* *(ICAIF ’21)*.
* Avellaneda and Stoikov (2008)

  Marco Avellaneda and Sasha Stoikov. 2008.
  High-frequency trading in a limit order book.
  *Quantitative Finance* 8, 3 (2008), 217–224.
* Belcak et al. (2022)

  Peter Belcak, Jan-Peter Calliess, and Stefan Zohren. 2022.
  Fast agent-based simulation framework with applications to reinforcement learning and the study of trading latency effects. In *Multi-Agent-Based Simulation XXII*, Koen H. Van Dam and Nicolas Verstaevel (Eds.). Springer International Publishing, Cham, 42–56.
* Bouchaud et al. (2018)

  Jean-Philippe Bouchaud, Julius Bonart, Jonathan Donier, and Martin Gould. 2018.
  *Trades, quotes and prices: financial markets under the microscope*.
  Cambridge University Press.
* Bradbury et al. (2018)

  James Bradbury et al. 2018.
  *JAX: composable transformations of Python+NumPy programs*.

  <http://github.com/jax-ml/jax>
* Byrd et al. (2020)

  David Byrd, Maria Hybinette, and Tucker Hybinette Balch. 2020.
  ABIDES: Towards high-fidelity multi-agent market simulation. In *Proceedings of the 2020 ACM SIGSIM Conference on Principles of Advanced Discrete Simulation* *(SIGSIM-PADS ’20)*. New York, NY, USA, 11–22.
* Cont and Muller (2021)

  Rama Cont and Marvin S Muller. 2021.
  A stochastic partial differential equation model for limit order book dynamics.
  *SIAM Journal on Financial Mathematics* 12, 2 (2021), 744–787.
* Cui and Brabazon (2012)

  Wei Cui and Anthony Brabazon. 2012.
  An agent-based modeling approach to study price impact. In *2012 IEEE Conference on Computational Intelligence for Financial Engineering & Economics (CIFEr)*. 1–8.
  [doi:10.1109/CIFEr.2012.6327798](https://doi.org/10.1109/CIFEr.2012.6327798)
* Cusumano-Towner et al. (2025)

  Marco Francis Cusumano-Towner et al. 2025.
  Robust Autonomy Emerges from Self-Play. In *Forty-second International Conference on Machine Learning*.

  <https://openreview.net/forum?id=yOXoJpG6Qy>
* Farmer et al. (2005)

  J Doyne Farmer, Paolo Patelli, and Ilija I Zovko. 2005.
  The predictive power of zero intelligence in financial markets.
  *Proceedings of the National Academy of Sciences* 102, 6 (2005), 2254–2259.
* Frey et al. (2023)

  Sascha Yves Frey, Kang Li, Peer Nagy, Silvia Sapora, Christopher Lu, Stefan Zohren, Jakob Foerster, and Anisoara Calinescu. 2023.
  JAX-LOB: A GPU-Accelerated limit order book simulator to unlock large scale reinforcement learning for trading. In *Proceedings of the Fourth ACM International Conference on AI in Finance*. 583–591.
* Gašperov et al. (2021)

  Bruno Gašperov, Stjepan Begušić, Petra Posedel Šimović, and Zvonko Kostanjčar. 2021.
  Reinforcement learning approaches to optimal market making.
  *Mathematics* 9, 21 (2021), 2689.
* Gode and Sunder (1993)

  Dhananjay K. Gode and Shyam Sunder. 1993.
  Allocative efficiency of markets with zero-intelligence traders: Market as a partial substitute for individual rationality.
  *Journal of Political Economy* 101, 1 (1993), 119–137.

  <http://www.jstor.org/stable/2138676>
* Gould et al. (2013)

  Martin D Gould, Mason A Porter, Stacy Williams, Mark McDonald, Daniel J Fenn, and Sam D Howison. 2013.
  Limit order books.
  *Quantitative Finance* 13, 11 (2013), 1709–1742.
* Huang and Polak (2011)

  Ruihong Huang and Tomas Polak. 2011.
  LOBSTER: Limit order book reconstruction system.
  *Available at SSRN 1977207* (2011).
* Karpe et al. (2020)

  Michaël Karpe, Jin Fang, Zhongyao Ma, and Chen Wang. 2020.
  Multi-agent reinforcement learning in a realistic limit order book market simulation. In *Proceedings of the First ACM International Conference on AI in Finance*. ACM, New York New York, 1–7.

  [doi:10.1145/3383455.3422570](https://doi.org/10.1145/3383455.3422570)
* Kazemkhani et al. (2025)

  Saman Kazemkhani, Aarav Pandya, Daphne Cornelisse, Brennan Shacklett, and Eugene Vinitsky. 2025.
  GPUDrive: Data-driven, multi-agent driving simulation at 1 million FPS. In *The Thirteenth International Conference on Learning Representations*.

  <https://openreview.net/forum?id=ERv8ptegFi>
* Lin and Beling (2021)

  Siyu Lin and Peter A. Beling. 2021.
  An agent-based market simulator for back-testing deep reinforcement learning based trade execution strategies. In *Neural Information Processing*. 644–653.
* Liu et al. (2020)

  Yang Liu, Qi Liu, Hongke Zhao, Zhen Pan, and Chuanren Liu. 2020.
  Adaptive quantitative trading: An imitative deep reinforcement learning approach. In *Proceedings of the AAAI conference on artificial intelligence*, Vol. 34. 2128–2135.
* Lussange et al. (2021)

  Johann Lussange et al. 2021.
  Modelling stock markets by multi-agent reinforcement learning.
  *Computational Economics* 57, 1 (2021), 113–147.

  [doi:10.1007/s10614-020-10038-w](https://doi.org/10.1007/s10614-020-10038-w)
* Lussange et al. (2024)

  Johann Lussange, Stefano Vrizzi, Stefano Palminteri, and Boris Gutkin. 2024.
  Modelling crypto markets by multi-agent reinforcement learning.
  *arXiv preprint arXiv:2402.10803* (2024).
* Mascioli et al. (2024)

  Chris Mascioli, Anri Gu, Yongzhao Wang, Mithun Chakraborty, and Michael Wellman. 2024.
  A financial market simulation environment for trading agents using deep reinforcement learning. In *Proceedings of the 5th ACM International Conference on AI in Finance* *(ICAIF ’24)*. New York, NY, USA, 117–125.
* Moallemi and Wang (2022)

  Ciamac C. Moallemi and Muye Wang. 2022.
  A reinforcement learning approach to optimal execution.
  *Quantitative Finance* 22, 6 (2022), 1051–1069.
* Nagy et al. (2023)

  Peer Nagy, Sascha Frey, Silvia Sapora, Kang Li, Anisoara Calinescu, Stefan Zohren, and Jakob Foerster. 2023.
  Generative AI for end-to-end limit order book modelling: A token-level autoregressive generative model of message flow using a deep state space network. In *Proceedings of the Fourth ACM International Conference on AI in Finance* *(ICAIF ’23)*. 91–99.
* Ning et al. (2021)

  Brian Ning, Franco Ho Ting Lin, and Sebastian Jaimungal. 2021.
  Double deep q-learning for optimal execution.
  *Applied Mathematical Finance* 28, 4 (2021), 361–380.
* Palmer et al. (1994)

  Richard G Palmer, W Brian Arthur, John H Holland, Blake LeBaron, and Paul Tayler. 1994.
  Artificial economic life: a simple model of a stockmarket.
  *Physica D: Nonlinear Phenomena* 75, 1-3 (1994), 264–274.
* Rutherford et al. (2024)

  Alexander Rutherford et al. 2024.
  JaxMARL: Multi-agent RL Environments and Algorithms in JAX.
  *Advances in Neural Information Processing Systems* 37 (2024), 50925–50951.
* Shacklett et al. (2023)

  Brennan Shacklett et al. 2023.
  An Extensible, Data-Oriented Architecture for High-Performance, Many-World Simulation.
  *ACM Trans. Graph.* 42, 4 (2023).
* Spooner et al. (2018)

  Thomas Spooner, John Fearnley, Rahul Savani, and Andreas Koukorinis. 2018.
  Market making via reinforcement learning. In *Proceedings of the 17th International Conference on Autonomous Agents and MultiAgent Systems*. 434–442.
* Spooner and Savani (2021)

  Thomas Spooner and Rahul Savani. 2021.
  Robust market making via adversarial reinforcement learning. In *Proceedings of the Twenty-Ninth International Joint Conference on Artificial Intelligence* *(IJCAI’20)*. Article 633, 7 pages.
* Théate and Ernst (2021)

  Thibaut Théate and Damien Ernst. 2021.
  An application of deep reinforcement learning to algorithmic trading.
  *Expert systems with applications* 173 (2021), 114632.
* Vadori et al. (2024)

  Nelson Vadori, Leo Ardon, Sumitra Ganesh, Thomas Spooner, Selim Amrouni, Jared Vann, Mengda Xu, Zeyu Zheng, Tucker Balch, and Manuela Veloso. 2024.
  Towards multi-agent reinforcement learning-driven over-the-counter market simulations.
  *Mathematical Finance* 34, 2 (2024), 262–347.

  [doi:10.1111/mafi.12416](https://doi.org/10.1111/mafi.12416)
* Vicente et al. (2022)

  Óscar Fernández Vicente, Fernando Fernández Rebollo, and Francisco Javier García Polo. 2022.
  Deep Q-learning market makers in a multi-agent simulated stock market. In *Proceedings of the Second ACM International Conference on AI in Finance* *(ICAIF ’21)*.
  [doi:10.1145/3490354.3494448](https://doi.org/10.1145/3490354.3494448)
* Vyetrenko et al. (2021)

  Svitlana Vyetrenko, David Byrd, Nick Petosa, Mahmoud Mahfouz, Danial Dervovic, Manuela Veloso, and Tucker Balch. 2021.
  Get real: realism metrics for robust limit order book market simulations. In *Proceedings of the First ACM International Conference on AI in Finance* *(ICAIF ’20)*.
  [doi:10.1145/3383455.3422561](https://doi.org/10.1145/3383455.3422561)
* Weng et al. (2022)

  Jiayi Weng, Huayu Chen, Dong Yan, Kaichao You, Alexis Duburcq, Minghao Zhang, Yi Su, Hang Su, and Jun Zhu. 2022.
  Tianshou: A highly modularized deep reinforcement learning library.
  *Journal of Machine Learning Research* 23, 267 (2022), 1–6.
* Yao et al. (2024)

  Zhiyuan Yao, Zheng Li, Matthew Thomas, and Ionut Florescu. 2024.
  Reinforcement learning in agent-based market simulation: Unveiling realistic stylized facts and behavior. In *2024 International Joint Conference on Neural Networks (IJCNN)*. IEEE, 1–9.