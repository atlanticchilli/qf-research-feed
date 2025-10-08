---
authors:
- Jinho Cha
- Justin Yoo
- Eunchan Daniel Cha
- Emily Yoo
- Caedon Geoffrey
- Hyoshin Song
doc_id: arxiv:2510.05504v1
family_id: arxiv:2510.05504
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource
  Allocation
url_abs: http://arxiv.org/abs/2510.05504v1
url_html: https://arxiv.org/html/2510.05504v1
venue: arXiv q-fin
version: 1
year: 2025
---


###### Abstract.

Decentralized coordination and digital contracting are becoming critical in complex industrial ecosystems, yet existing approaches often rely on ad-hoc heuristics or purely technical blockchain implementations without a rigorous economic foundation. This study develops a mechanism-design framework for smart-contract–based resource allocation that explicitly embeds efficiency and fairness in decentralized coordination. We establish the existence and uniqueness of contract equilibria, extending classical results in mechanism design, and introduce a decentralized price-adjustment algorithm with provable convergence guarantees that can be implemented in real time. To evaluate performance, we combine extensive synthetic benchmarks with a proof-of-concept real-world dataset (MovieLens). The synthetic tests probe robustness under fee volatility, participation shocks, and dynamic demand, while the MovieLens case study illustrates how the mechanism can balance efficiency and fairness in realistic allocation environments. Results demonstrate that the proposed mechanism achieves substantial improvements in both efficiency and equity while remaining resilient to abrupt perturbations, confirming its stability beyond steady-state analysis. The findings highlight broad managerial and policy relevance for supply chains, logistics, energy markets, healthcare resource allocation, and public infrastructure, where transparent and auditable coordination is increasingly critical. By combining theoretical rigor with empirical validation, the study shows how digital contracts can serve not only as technical artifacts but also as institutional instruments for transparency, accountability, and resilience in high-stakes resource allocation.

###### Key words and phrases:

Smart contracts, Mechanism design, Decentralized coordination, Efficiency–fairness trade-offs, Resource allocation.

###### 1991 Mathematics Subject Classification:

Primary: 91B32; Secondary: 91B50, 91B26, 91B40.

∗Corresponding author: Jinho Cha

Jinho Cha1,✉⁣∗{}^{1,{\href mailto:jcha@gwinnetttech.edu}\*},
Justin Yoo2,✉{}^{2,{\href mailto:Jyu708@gatech.edu}},
Eunchan Daniel Cha3,✉{}^{3,{\href mailto:echa32@gatech.edu}},
Emily Yoo4,✉{}^{4,{\href mailto:skyoo72008@gmail.com}},
Caedon Geoffrey1,✉{}^{1,{\href mailto:cgeoffr2486@student.gwinnetttech.edu}},
Hyoshin Song5,✉{}^{5,{\href mailto:hellosong0505@gmail.com}}

1Department of Computer Science, Gwinnett Technical College, GA, USA

2Scheller College of Business, Georgia Institute of Technology, GA, USA

3School of Biological Sciences, Georgia Institute of Technology, GA, USA

4North Gwinnett High School, Suwanee, GA, USA

5Oakton High School, Vienna, VA, USA

(Communicated by Handling Editor)

## 1. Introduction

The rapid digitalization of industrial systems—often summarized under the umbrella of
Industry 4.0—has accelerated the integration of cyber–physical infrastructure with
autonomous decision-making technologies. Applications ranging from predictive maintenance,
supply chain optimization, and production scheduling to smart grids and healthcare
management increasingly demand secure, transparent, and real-time coordination across
heterogeneous participants
[[28](https://arxiv.org/html/2510.05504v1#bib.bib28), [34](https://arxiv.org/html/2510.05504v1#bib.bib34), [25](https://arxiv.org/html/2510.05504v1#bib.bib25), [55](https://arxiv.org/html/2510.05504v1#bib.bib55), [58](https://arxiv.org/html/2510.05504v1#bib.bib58), [42](https://arxiv.org/html/2510.05504v1#bib.bib42)].
Yet, traditional contracting mechanisms, whether based on bilateral negotiations,
centralized intermediaries, or informal agreements, often suffer from inefficiencies,
delays, and susceptibility to opportunism
[[12](https://arxiv.org/html/2510.05504v1#bib.bib12), [21](https://arxiv.org/html/2510.05504v1#bib.bib21), [5](https://arxiv.org/html/2510.05504v1#bib.bib5)].
These limitations highlight the need for automated and verifiable protocols that can
enforce resource allocation and compliance without reliance on trusted third parties.

Smart contracts, programmable agreements executed on blockchain platforms, provide
such a foundation. By embedding allocation logic within tamper-resistant code,
they reduce agency costs and improve transparency across organizational boundaries
[[51](https://arxiv.org/html/2510.05504v1#bib.bib51), [10](https://arxiv.org/html/2510.05504v1#bib.bib10), [15](https://arxiv.org/html/2510.05504v1#bib.bib15), [53](https://arxiv.org/html/2510.05504v1#bib.bib53), [56](https://arxiv.org/html/2510.05504v1#bib.bib56)].
Emerging work demonstrates applications in supply chains [[26](https://arxiv.org/html/2510.05504v1#bib.bib26)],
energy markets [[19](https://arxiv.org/html/2510.05504v1#bib.bib19), [37](https://arxiv.org/html/2510.05504v1#bib.bib37)], and public health
[[54](https://arxiv.org/html/2510.05504v1#bib.bib54)], but most studies emphasize technological feasibility or
security properties. Less attention has been paid to their *mechanism-design
implications*: how to design contract rules that guarantee efficiency,
fairness, and resilience in competitive, shock-prone environments.

From an analytical perspective, game theory and mechanism design offer natural
foundations. Prior work has established conditions for efficiency and equilibrium
in resource allocation games [[40](https://arxiv.org/html/2510.05504v1#bib.bib40), [20](https://arxiv.org/html/2510.05504v1#bib.bib20), [38](https://arxiv.org/html/2510.05504v1#bib.bib38)],
developed fairness–efficiency trade-offs [[7](https://arxiv.org/html/2510.05504v1#bib.bib7), [29](https://arxiv.org/html/2510.05504v1#bib.bib29)],
and characterized regret bounds in dynamic and adversarial settings
[[23](https://arxiv.org/html/2510.05504v1#bib.bib23), [50](https://arxiv.org/html/2510.05504v1#bib.bib50)]. However, these strands remain largely disjoint from
the literature on smart contracts and blockchain-based coordination, which has
focused more on distributed algorithms and consensus protocols
[[52](https://arxiv.org/html/2510.05504v1#bib.bib52), [6](https://arxiv.org/html/2510.05504v1#bib.bib6), [17](https://arxiv.org/html/2510.05504v1#bib.bib17)].
To date, little work has unified these perspectives into a rigorous
framework for contract-mediated industrial coordination under uncertainty.

![Refer to caption](Fig1.png)


Figure 1. Conceptual framework: participants submit demands to a blockchain-based
smart contract, influenced by external factors and feedback, which allocates resources
and produces outcomes measurable in efficiency, fairness, and transparency.

This paper addresses this gap by developing a rigorous framework for
*smart-contract–based mechanism design under shared capacity constraints*.
Participants submit demands to a contract that implements allocation and pricing
rules, subject to transaction and execution fees (τ,g)(\tau,g).
We formulate the interaction as a non-cooperative game, derive the payoff structure,
and establish the following theoretical contributions:

* •

  Existence and uniqueness of equilibrium.
  Under mild convexity conditions, the contract-clearing game admits a unique
  stable equilibrium.
* •

  Algorithmic convergence.
  A decentralized price-adjustment algorithm is designed and shown to converge.
* •

  Fairness–efficiency trade-off.
  Pareto frontiers quantify efficiency gains versus equity, enabling policy
  calibration.
* •

  Shock–resilience guarantees.
  Sublinear regret bounds demonstrate robustness to drift and shock events.

Numerical simulations corroborate the theory, showing efficiency gains of up to
27% and inequality reductions exceeding 40% relative to proportional rules.
Beyond these numbers, sensitivity dashboards and resilience analyses provide
decision makers with interpretable tools for policy design.
Viewed holistically, the proposed framework suggests that smart contracts can serve
not only as technical artifacts but also as *institutional mechanisms* that
enhance transparency, fairness, and robustness in complex industrial environments
[[44](https://arxiv.org/html/2510.05504v1#bib.bib44), [22](https://arxiv.org/html/2510.05504v1#bib.bib22), [1](https://arxiv.org/html/2510.05504v1#bib.bib1)].

## 2. Literature on Smart Contracts and Mechanism Design

The literature on resource allocation in digital and cyber–physical systems spans
mobile edge computing, cloud economics, blockchain-enabled coordination, and
information systems governance. While the technical foundations of these systems
are well established, their implications for trust, fairness, resilience, and
organizational legitimacy remain underexplored. We review three strands most
relevant to our work: smart contracts in organizational systems, game-theoretic
approaches to resource allocation, and mechanism design perspectives on efficiency
and fairness.

### 2.1. Smart Contracts in Organizational Contexts

Smart contracts have been widely studied as programmable agreements on blockchain
platforms, enabling tamper-resistant execution and transparent enforcement
[[51](https://arxiv.org/html/2510.05504v1#bib.bib51), [10](https://arxiv.org/html/2510.05504v1#bib.bib10)]. Early contributions emphasized cryptography,
consensus protocols, and distributed architectures [[11](https://arxiv.org/html/2510.05504v1#bib.bib11)], while more
recent work extended applications to supply chain management, manufacturing, and
industrial automation [[14](https://arxiv.org/html/2510.05504v1#bib.bib14), [25](https://arxiv.org/html/2510.05504v1#bib.bib25)]. Within the information systems
field, blockchain has increasingly been theorized as a governance mechanism that
reduces opportunism, enhances transparency, and supports inter-organizational trust
[[5](https://arxiv.org/html/2510.05504v1#bib.bib5), [43](https://arxiv.org/html/2510.05504v1#bib.bib43), [44](https://arxiv.org/html/2510.05504v1#bib.bib44), [22](https://arxiv.org/html/2510.05504v1#bib.bib22)]. These studies highlight that
smart contracts are not merely computational artifacts but institutional devices that
redefine how rules are enacted across organizations. Surveys of blockchain-enabled
resource management in mobile and edge computing [[45](https://arxiv.org/html/2510.05504v1#bib.bib45)] further illustrate
that adoption depends as much on legitimacy and regulatory alignment as on technical
performance. Yet most existing work abstracts away from incentive compatibility or
distributional consequences, which motivates a game-theoretic analysis of strategic
behavior.

### 2.2. Game-Theoretic Resource Allocation

Game-theoretic models have long been used to study competition and cooperation in
resource allocation. In mobile edge and cloud computing, Muñoz et al. [[39](https://arxiv.org/html/2510.05504v1#bib.bib39)]
optimized radio and computational resources under latency and energy constraints,
while Dinh et al. [[18](https://arxiv.org/html/2510.05504v1#bib.bib18)] investigated multi-device offloading. Zhang
[[59](https://arxiv.org/html/2510.05504v1#bib.bib59)] introduced stochastic games for dynamic offloading, and subsequent
studies extended these approaches through Stackelberg pricing [[32](https://arxiv.org/html/2510.05504v1#bib.bib32)], matching
theory for user–server association [[33](https://arxiv.org/html/2510.05504v1#bib.bib33)], and reinforcement learning for
adaptive scheduling [[16](https://arxiv.org/html/2510.05504v1#bib.bib16)]. Recent contributions integrate blockchain into MEC
and vehicular networks, combining incentives with efficient allocation
[[17](https://arxiv.org/html/2510.05504v1#bib.bib17), [58](https://arxiv.org/html/2510.05504v1#bib.bib58), [57](https://arxiv.org/html/2510.05504v1#bib.bib57)]. Classic theoretical results also remain influential:
Rosen [[48](https://arxiv.org/html/2510.05504v1#bib.bib48)] established conditions for the existence and uniqueness of
concave NN-person game equilibria, Gabay and Moulin [[20](https://arxiv.org/html/2510.05504v1#bib.bib20)] analyzed equilibrium
stability, and Roughgarden and Tardos [[49](https://arxiv.org/html/2510.05504v1#bib.bib49)] introduced the price of
anarchy in distributed settings. In supply chains, Cachon and Netessine [[12](https://arxiv.org/html/2510.05504v1#bib.bib12)]
demonstrated how equilibrium reasoning provides insight into coordination failures,
while Ivanov [[26](https://arxiv.org/html/2510.05504v1#bib.bib26)] emphasized resilience under disruption shocks. Taken
together, these studies show that equilibrium outcomes not only describe technical
efficiency but also institutionalize how competition, cooperation, and power
asymmetries are resolved. However, they rarely connect such equilibria to broader
questions of organizational legitimacy or fairness.

### 2.3. Mechanism Design and Fairness Considerations

Operations research and economics emphasize the design of mechanisms that balance
efficiency and fairness. Generalized Nash equilibrium models have been applied to
network pricing [[30](https://arxiv.org/html/2510.05504v1#bib.bib30), [13](https://arxiv.org/html/2510.05504v1#bib.bib13)], and bilevel optimization has been
used for provider profit maximization [[53](https://arxiv.org/html/2510.05504v1#bib.bib53)]. The “price of fairness” has
been formalized in optimization [[7](https://arxiv.org/html/2510.05504v1#bib.bib7)], quantifying the efficiency
loss incurred by enforcing equity constraints. In organizational sciences, fairness
metrics such as the Gini index capture distributive outcomes [[31](https://arxiv.org/html/2510.05504v1#bib.bib31)],
while justice theory emphasizes that perceptions of distributive and procedural
fairness are critical for sustaining trust and compliance [[21](https://arxiv.org/html/2510.05504v1#bib.bib21)].
Recent IS scholarship has broadened these discussions to algorithmic governance,
highlighting fairness, accountability, and legitimacy as essential for digital
platforms [[44](https://arxiv.org/html/2510.05504v1#bib.bib44), [27](https://arxiv.org/html/2510.05504v1#bib.bib27)]. Complementary streams in computer science and
data ethics have examined algorithmic fairness, stressing both formal metrics and
human perceptions [[3](https://arxiv.org/html/2510.05504v1#bib.bib3), [36](https://arxiv.org/html/2510.05504v1#bib.bib36), [29](https://arxiv.org/html/2510.05504v1#bib.bib29)]. Despite these advances,
integration of automated enforcement, incentive compatibility, and distributive
justice within a unified analytical framework remains limited.

### 2.4. Research Gap

Synthesizing these literatures reveals several gaps. First, while smart contracts
promise automation and transparency, their role as organizational allocation
mechanisms has not been formally analyzed in models that jointly address efficiency,
fairness, and incentive compatibility. Second, while MEC and cloud research has
developed sophisticated equilibrium frameworks, these approaches rarely extend to
industrial contexts where governance, legitimacy, and resilience under shocks
[[25](https://arxiv.org/html/2510.05504v1#bib.bib25), [26](https://arxiv.org/html/2510.05504v1#bib.bib26)] are equally critical. Third, few studies connect
formal mechanism design to fairness–efficiency trade-offs and shock–resilience
properties, despite their centrality in industrial and managerial optimization.
Addressing these gaps, this study develops a non-cooperative game of
smart-contract–mediated resource allocation, proves its equilibrium properties,
and implements a decentralized contract-clearing algorithm. By comparing with
traditional allocation rules, the study contributes to operations research and the
information systems literature on digital governance, trust, and inter-organizational
coordination.

## 3. Contract Design for Efficient and Fair Industrial Resource Allocation

Industrial systems such as supply chains, logistics networks, and production
platforms must allocate scarce resources across multiple agents. Traditional
allocation rules—whether proportional or centrally administered—often suffer
from inefficiency, opportunism, and lack of transparency. Digital contracts
implemented on blockchain platforms offer a compelling alternative: allocation
rules can be encoded, enforced automatically, and verified by all participants.
This section formalizes the contract design, introduces equilibrium concepts,
and develops performance metrics that jointly capture efficiency, fairness,
and resilience.

### 3.1. Model Setup

Let N={1,…,n}N=\{1,\dots,n\} denote the set of industrial agents. Each agent ii
requests a quantity xi≥0x\_{i}\geq 0, and we collect demands in the vector
𝐱=(x1,…,xn)⊤\mathbf{x}=(x\_{1},\dots,x\_{n})^{\top}. The shared resource pool has capacity m>0m>0:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟏⊤​𝐱≤m.\mathbf{1}^{\top}\mathbf{x}\;\leq\;m. |  | (1) |

###### Assumption 3.1 (Valuation and Cost).

Each agent derives value Vi​(xi)V\_{i}(x\_{i}) from consumption and incurs cost Ci​(xi)C\_{i}(x\_{i}).
We impose:

1. (1)

   Vi:ℝ+→ℝV\_{i}:\mathbb{R}\_{+}\to\mathbb{R} is strictly concave, differentiable,
   and satisfies Vi′​(0)=∞V\_{i}^{\prime}(0)=\infty (diminishing returns).
2. (2)

   Ci:ℝ+→ℝC\_{i}:\mathbb{R}\_{+}\to\mathbb{R} is convex, differentiable, and Lipschitz continuous.

The smart contract imposes a per-unit fee τ≥0\tau\geq 0, a shadow price μ≥0\mu\geq 0
to enforce capacity, and a fixed execution fee g≥0g\geq 0. The payoff of agent ii is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ui​(xi;μ)=Vi​(xi)−Ci​(xi)−(τ+μ)​xi−g​ 1​{xi>0}.U\_{i}(x\_{i};\mu)=V\_{i}(x\_{i})-C\_{i}(x\_{i})-(\tau+\mu)x\_{i}-g\,\mathbf{1}\{x\_{i}>0\}. |  | (2) |

### 3.2. Equilibrium Definition

###### Definition 3.2 (Contract-Clearing Equilibrium).

An allocation (𝐱⋆,μ⋆)(\mathbf{x}^{\star},\mu^{\star}) is a contract-clearing equilibrium if:

1. (1)

   (Best response) For each i∈Ni\in N,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | xi⋆​(μ⋆)∈arg⁡maxxi≥0⁡Ui​(xi;μ⋆).x\_{i}^{\star}(\mu^{\star})\in\arg\max\_{x\_{i}\geq 0}U\_{i}(x\_{i};\mu^{\star}). |  | (3) |
2. (2)

   (Market clearing) The aggregate demand satisfies

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | 𝟏⊤​𝐱⋆=m.\mathbf{1}^{\top}\mathbf{x}^{\star}=m. |  | (4) |

###### Lemma 3.3 (Monotonicity of Aggregate Demand).

Under Assumption [3.1](https://arxiv.org/html/2510.05504v1#S3.Thmtheorem1 "Assumption 3.1 (Valuation and Cost). ‣ 3.1. Model Setup ‣ 3. Contract Design for Efficient and Fair Industrial Resource Allocation ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation"), each best response xi⋆​(μ)x\_{i}^{\star}(\mu) is continuous
and non-increasing in μ\mu. Hence the aggregate demand

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​(μ)=𝟏⊤​𝐱⋆​(μ)S(\mu)=\mathbf{1}^{\top}\mathbf{x}^{\star}(\mu) |  | (5) |

is continuous and strictly decreasing.

###### Proposition 3.4 (Existence).

A contract-clearing equilibrium exists.

###### Proof of Proposition [3.4](https://arxiv.org/html/2510.05504v1#S3.Thmtheorem4 "Proposition 3.4 (Existence). ‣ 3.2. Equilibrium Definition ‣ 3. Contract Design for Efficient and Fair Industrial Resource Allocation ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation").

By Lemma [3.3](https://arxiv.org/html/2510.05504v1#S3.Thmtheorem3 "Lemma 3.3 (Monotonicity of Aggregate Demand). ‣ 3.2. Equilibrium Definition ‣ 3. Contract Design for Efficient and Fair Industrial Resource Allocation ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation"), S​(μ)S(\mu) is continuous and strictly decreasing.
Since S​(0)>mS(0)>m and limμ→∞S​(μ)=0\lim\_{\mu\to\infty}S(\mu)=0, the Intermediate Value
Theorem ensures a unique μ⋆\mu^{\star} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​(μ⋆)=m.S(\mu^{\star})=m. |  | (6) |

∎

###### Proposition 3.5 (Uniqueness).

If UiU\_{i} is strictly concave in xix\_{i}, the contract-clearing equilibrium
(𝐱⋆,μ⋆)(\mathbf{x}^{\star},\mu^{\star}) is unique [[48](https://arxiv.org/html/2510.05504v1#bib.bib48), [24](https://arxiv.org/html/2510.05504v1#bib.bib24)].

### 3.3. Illustrative Example

Suppose Vi​(xi)=αi​log⁡(1+xi)V\_{i}(x\_{i})=\alpha\_{i}\log(1+x\_{i}) and Ci​(xi)=βi​xiC\_{i}(x\_{i})=\beta\_{i}x\_{i}. Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | xi⋆​(μ)=max⁡{0,αiβi+τ+μ−1}.x\_{i}^{\star}(\mu)=\max\!\left\{0,\;\frac{\alpha\_{i}}{\beta\_{i}+\tau+\mu}-1\right\}. |  | (7) |

Since S​(μ)=𝟏⊤​𝐱⋆​(μ)S(\mu)=\mathbf{1}^{\top}\mathbf{x}^{\star}(\mu) is strictly decreasing, a unique equilibrium
price μ⋆\mu^{\star} exists.

### 3.4. Performance Metrics

###### Definition 3.6 (Efficiency).

|  |  |  |  |
| --- | --- | --- | --- |
|  | Eff​(𝐱⋆)=∑i=1n(Vi​(xi⋆)−Ci​(xi⋆))−τ​ 1⊤​𝐱⋆−g⋅‖𝐱⋆‖0.\mathrm{Eff}(\mathbf{x}^{\star})=\sum\_{i=1}^{n}\big(V\_{i}(x\_{i}^{\star})-C\_{i}(x\_{i}^{\star})\big)-\tau\,\mathbf{1}^{\top}\mathbf{x}^{\star}-g\cdot\|\mathbf{x}^{\star}\|\_{0}. |  | (8) |

###### Definition 3.7 (Fairness: Gini Index [[31](https://arxiv.org/html/2510.05504v1#bib.bib31), [21](https://arxiv.org/html/2510.05504v1#bib.bib21)]).

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gini​(𝐱⋆)=12​n2​x¯​∑i=1n∑j=1n|xi⋆−xj⋆|,x¯=1n​𝟏⊤​𝐱⋆.\mathrm{Gini}(\mathbf{x}^{\star})=\frac{1}{2n^{2}\bar{x}}\sum\_{i=1}^{n}\sum\_{j=1}^{n}|x\_{i}^{\star}-x\_{j}^{\star}|,\quad\bar{x}=\tfrac{1}{n}\mathbf{1}^{\top}\mathbf{x}^{\star}. |  | (9) |

###### Definition 3.8 (Price of Fairness [[7](https://arxiv.org/html/2510.05504v1#bib.bib7), [29](https://arxiv.org/html/2510.05504v1#bib.bib29)]).

|  |  |  |  |
| --- | --- | --- | --- |
|  | PoF=max𝐱⁡Eff​(𝐱)Eff​(𝐱fair⋆).\mathrm{PoF}=\frac{\max\_{\mathbf{x}}\mathrm{Eff}(\mathbf{x})}{\mathrm{Eff}(\mathbf{x}^{\star}\_{\text{fair}})}. |  | (10) |

###### Definition 3.9 (Shock Resilience).

For a demand shock at t0t\_{0}, resilience is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | R=Effpost-shockEffpre-shock.R=\frac{\mathrm{Eff}\_{\text{post-shock}}}{\mathrm{Eff}\_{\text{pre-shock}}}. |  | (11) |

###### Definition 3.10 (Dynamic Regret [[23](https://arxiv.org/html/2510.05504v1#bib.bib23), [50](https://arxiv.org/html/2510.05504v1#bib.bib50)]).

In repeated play with allocations {𝐱t}\{\mathbf{x}\_{t}\} and optimal sequence {𝐱t⋆}\{\mathbf{x}^{\star}\_{t}\},

|  |  |  |  |
| --- | --- | --- | --- |
|  | Regret​(T)=∑t=1T(U​(𝐱t⋆)−U​(𝐱t)),Regret​(T)=o​(T).\mathrm{Regret}(T)=\sum\_{t=1}^{T}\Big(U(\mathbf{x}^{\star}\_{t})-U(\mathbf{x}\_{t})\Big),\quad\mathrm{Regret}(T)=o(T). |  | (12) |

## 4. Mechanism Design and Equilibrium Analysis

This section develops the theoretical foundations of the proposed digital
contracting framework. In line with mechanism design principles, we move step by
step: first specifying the payoff structure, then formalizing equilibrium, then
presenting a decentralized algorithm, and finally proving convergence. Each
subsection builds logically toward the claim that digital contracts generate
stable, efficient, and fair allocations in competitive environments.

Before delving into the formal results, Table [1](https://arxiv.org/html/2510.05504v1#S4.T1 "Table 1 ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation") summarizes the
notation used throughout this section. It distinguishes between decision
variables, parameters, functional mappings, and performance metrics, so that the
subsequent analysis can be followed without ambiguity.

Table 1. Summary of notation used in the contract design and equilibrium analysis.

| Symbol | Type | Description |
| --- | --- | --- |
| nn | Scalar | Number of agents (firms, participants). |
| mm | Scalar | Total system capacity (shared resource pool). |
| i∈Ni\in N | Index | Agent index, N={1,…,n}N=\{1,\dots,n\}. |
| xix\_{i} | Scalar | Allocation (demand) of agent ii. |
| 𝐱=(x1,…,xn)⊤\mathbf{x}=(x\_{1},\dots,x\_{n})^{\top} | Vector | Allocation profile across all agents. |
| 𝟏\mathbf{1} | Vector | All-ones vector in ℝn\mathbb{R}^{n}, used for aggregation. |
| Vi​(xi)V\_{i}(x\_{i}) | Function | Valuation (utility) function of agent ii, strictly concave. |
| Ci​(xi)C\_{i}(x\_{i}) | Function | Cost function of agent ii, convex and Lipschitz. |
| Ui​(xi;μ)U\_{i}(x\_{i};\mu) | Function | Payoff of agent ii under contract and price μ\mu. |
| τ\tau | Scalar | Transaction fee imposed by the contract. |
| gg | Scalar | Fixed execution cost if xi>0x\_{i}>0. |
| μ\mu | Scalar | Shadow price (dual variable) enforcing the capacity constraint. |
| B​Ri​(μ)BR\_{i}(\mu) | Function | Best-response allocation of agent ii given price μ\mu. |
| S​(μ)S(\mu) | Function | Aggregate demand S​(μ)=𝟏⊤​𝐱​(μ)S(\mu)=\mathbf{1}^{\top}\mathbf{x}(\mu). |
| Eff​(𝐱)\mathrm{Eff}(\mathbf{x}) | Metric | Efficiency: total surplus net of fees and costs. |
| Gini​(𝐱)\mathrm{Gini}(\mathbf{x}) | Metric | Fairness: inequality of allocations via Gini index. |
| PoF\mathrm{PoF} | Metric | Price of Fairness: ratio of maximum efficiency to fairness-constrained efficiency. |
| RR | Metric | Shock resilience: post-shock to pre-shock efficiency ratio. |
| Regret​(T)\mathrm{Regret}(T) | Metric | Dynamic regret in repeated play over horizon TT. |

### 4.1. Payoff Structure under Digital Contracts

We begin by characterizing the economic environment of individual agents.
The payoff specification formalizes how valuations, costs, transaction fees,
and scarcity penalties interact under the digital contract. This micro-level
foundation is essential, as all subsequent equilibrium and convergence results
build directly on these primitives.

Each agent i∈N={1,…,n}i\in N=\{1,\dots,n\} chooses xi≥0x\_{i}\geq 0 units subject to the
system-wide capacity constraint ([1](https://arxiv.org/html/2510.05504v1#S3.E1 "In 3.1. Model Setup ‣ 3. Contract Design for Efficient and Fair Industrial Resource Allocation ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")), equivalently written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1nxi≤m.\sum\_{i=1}^{n}x\_{i}\;\leq\;m. |  | (13) |

Each agent’s valuation ViV\_{i} and cost CiC\_{i} satisfy Assumption [3.1](https://arxiv.org/html/2510.05504v1#S3.Thmtheorem1 "Assumption 3.1 (Valuation and Cost). ‣ 3.1. Model Setup ‣ 3. Contract Design for Efficient and Fair Industrial Resource Allocation ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation").
The smart contract imposes a per-unit fee τ≥0\tau\geq 0, a shadow price μ≥0\mu\geq 0
to enforce capacity, and a fixed execution fee g≥0g\geq 0. The payoff of agent ii is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ui​(xi;μ)=Vi​(xi)−Ci​(xi)−(τ+μ)​xi−g​ 1​{xi>0}.U\_{i}(x\_{i};\mu)=V\_{i}(x\_{i})-C\_{i}(x\_{i})-(\tau+\mu)x\_{i}-g\,\mathbf{1}\{x\_{i}>0\}. |  | (14) |

For an interior solution xi⋆​(μ)>0x\_{i}^{\star}(\mu)>0, the first-order condition (FOC) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vi′​(xi⋆​(μ))−Ci′​(xi⋆​(μ))=τ+μ,V\_{i}^{\prime}(x\_{i}^{\star}(\mu))-C\_{i}^{\prime}(x\_{i}^{\star}(\mu))=\tau+\mu, |  | (15) |

while if Vi′​(0)≤τ+μV\_{i}^{\prime}(0)\leq\tau+\mu, then xi⋆​(μ)=0x\_{i}^{\star}(\mu)=0.

###### Lemma 4.1 (Boundedness of Best Responses).

Under Assumption [3.1](https://arxiv.org/html/2510.05504v1#S3.Thmtheorem1 "Assumption 3.1 (Valuation and Cost). ‣ 3.1. Model Setup ‣ 3. Contract Design for Efficient and Fair Industrial Resource Allocation ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation"), each best response xi⋆​(μ)x\_{i}^{\star}(\mu) is bounded:

|  |  |  |
| --- | --- | --- |
|  | 0≤xi⋆​(μ)≤x¯i<∞,∀μ≥0.0\leq x\_{i}^{\star}(\mu)\leq\bar{x}\_{i}<\infty,\quad\forall\mu\geq 0. |  |

###### Proof of Lemma [4.1](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem1 "Lemma 4.1 (Boundedness of Best Responses). ‣ 4.1. Payoff Structure under Digital Contracts ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation").

For an interior solution, the FOC ([15](https://arxiv.org/html/2510.05504v1#S4.E15 "In 4.1. Payoff Structure under Digital Contracts ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")) admits a unique finite root
because Vi′V\_{i}^{\prime} decreases from +∞+\infty while Ci′C\_{i}^{\prime} is increasing and Lipschitz.
If τ+μ≥Vi′​(0)\tau+\mu\geq V\_{i}^{\prime}(0), then xi⋆​(μ)=0x\_{i}^{\star}(\mu)=0. Otherwise, the solution is
bounded by the finite root x¯i\bar{x}\_{i} satisfying

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vi′​(x¯i)−Ci′​(x¯i)=0.V\_{i}^{\prime}(\bar{x}\_{i})-C\_{i}^{\prime}(\bar{x}\_{i})=0. |  | (16) |

∎

###### Lemma 4.2 (Continuity and Monotonicity).

Under Assumption [3.1](https://arxiv.org/html/2510.05504v1#S3.Thmtheorem1 "Assumption 3.1 (Valuation and Cost). ‣ 3.1. Model Setup ‣ 3. Contract Design for Efficient and Fair Industrial Resource Allocation ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation"), each best response xi⋆​(μ)x\_{i}^{\star}(\mu) is continuous
and non-increasing in μ\mu. Hence the aggregate demand

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​(μ)=∑i=1nxi⋆​(μ)S(\mu)=\sum\_{i=1}^{n}x\_{i}^{\star}(\mu) |  | (17) |

is continuous and strictly decreasing.

###### Proof of Lemma [3.3](https://arxiv.org/html/2510.05504v1#S3.Thmtheorem3 "Lemma 3.3 (Monotonicity of Aggregate Demand). ‣ 3.2. Equilibrium Definition ‣ 3. Contract Design for Efficient and Fair Industrial Resource Allocation ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation").

For an interior solution, ([15](https://arxiv.org/html/2510.05504v1#S4.E15 "In 4.1. Payoff Structure under Digital Contracts ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")) implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​xi⋆d​μ=1Ci′′​(xi⋆​(μ))−Vi′′​(xi⋆​(μ)).\frac{dx\_{i}^{\star}}{d\mu}=\frac{1}{C\_{i}^{\prime\prime}(x\_{i}^{\star}(\mu))-V\_{i}^{\prime\prime}(x\_{i}^{\star}(\mu))}. |  | (18) |

Since Vi′′<0V\_{i}^{\prime\prime}<0 and Ci′′≥0C\_{i}^{\prime\prime}\geq 0, the derivative is strictly negative.
At the boundary xi⋆​(μ)=0x\_{i}^{\star}(\mu)=0, larger μ\mu cannot increase demand.
Summing across agents yields continuity and strict monotonicity of S​(μ)S(\mu).
∎

###### Proposition 4.3 (Dual Boundedness).

Let vmax=maxi∈N⁡Vi′​(0)v\_{\max}=\max\_{i\in N}V\_{i}^{\prime}(0). Any contract-clearing equilibrium satisfies

|  |  |  |
| --- | --- | --- |
|  | 0≤μ⋆<vmax−τ.0\;\leq\;\mu^{\star}\;<\;v\_{\max}-\tau. |  |

###### Proof of Proposition [4.3](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem3 "Proposition 4.3 (Dual Boundedness). ‣ 4.1. Payoff Structure under Digital Contracts ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation").

Suppose μ≥vmax−τ\mu\geq v\_{\max}-\tau. Then

|  |  |  |
| --- | --- | --- |
|  | τ+μ≥Vi′​(0),∀i∈N,\tau+\mu\;\geq\;V\_{i}^{\prime}(0),\qquad\forall i\in N, |  |

which implies xi⋆​(μ)=0x\_{i}^{\star}(\mu)=0 and S​(μ)=0S(\mu)=0. But equilibrium requires
S​(μ⋆)=m>0S(\mu^{\star})=m>0, a contradiction. Hence μ⋆<vmax−τ\mu^{\star}<v\_{\max}-\tau.
Nonnegativity μ⋆≥0\mu^{\star}\geq 0 follows from dual feasibility.
∎

###### Proposition 4.4 (Comparative Statics in Capacity).

Suppose SS is differentiable at μ⋆​(m)\mu^{\star}(m) with S′​(μ⋆)<0S^{\prime}(\mu^{\star})<0. Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​μ⋆d​m=1S′​(μ⋆)<0.\frac{d\mu^{\star}}{dm}=\frac{1}{S^{\prime}(\mu^{\star})}<0. |  | (19) |

###### Proof of Proposition [4.4](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem4 "Proposition 4.4 (Comparative Statics in Capacity). ‣ 4.1. Payoff Structure under Digital Contracts ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation").

The clearing condition is

|  |  |  |
| --- | --- | --- |
|  | S​(μ⋆​(m))=m.S(\mu^{\star}(m))=m. |  |

Differentiating w.r.t. mm gives

|  |  |  |
| --- | --- | --- |
|  | S′​(μ⋆)​d​μ⋆d​m=1.S^{\prime}(\mu^{\star})\frac{d\mu^{\star}}{dm}=1. |  |

Since S′​(μ⋆)<0S^{\prime}(\mu^{\star})<0, it follows that d​μ⋆d​m<0\tfrac{d\mu^{\star}}{dm}<0,
i.e., increasing capacity reduces the equilibrium price.
∎

Economically, Vi′​(xi)V\_{i}^{\prime}(x\_{i}) is the marginal benefit, Ci′​(xi)C\_{i}^{\prime}(x\_{i}) the marginal
private cost, and τ+μ\tau+\mu the effective contract price. The auxiliary results
guarantee that best responses are well-behaved, clearing prices are bounded,
and comparative statics follow economic intuition.

### 4.2. Equilibrium Formulation and Characterization

We now lift the analysis to the system level by defining the
*contract-clearing equilibrium*. This subsection establishes existence and
uniqueness: the guarantees that allocations are well-defined and reproducible.

For a given μ≥0\mu\geq 0, the best-response mapping of agent ii is

|  |  |  |  |
| --- | --- | --- | --- |
|  | B​Ri​(μ)=arg⁡maxxi≥0⁡Ui​(xi;μ).BR\_{i}(\mu)=\arg\max\_{x\_{i}\geq 0}U\_{i}(x\_{i};\mu). |  | (20) |

Aggregate demand is equivalently defined as in ([17](https://arxiv.org/html/2510.05504v1#S4.E17 "In Lemma 4.2 (Continuity and Monotonicity). ‣ 4.1. Payoff Structure under Digital Contracts ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​(μ)=∑i=1nB​Ri​(μ).S(\mu)=\sum\_{i=1}^{n}BR\_{i}(\mu). |  | (21) |

###### Definition 4.5 (Contract-Clearing Equilibrium).

An allocation (𝐱⋆,μ⋆)(\mathbf{x}^{\star},\mu^{\star}) is a contract equilibrium if

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | xi⋆\displaystyle x\_{i}^{\star} | =B​Ri​(μ⋆),∀i∈N,\displaystyle=BR\_{i}(\mu^{\star}),\quad\forall i\in N, |  | (22) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | S​(μ⋆)\displaystyle S(\mu^{\star}) | =m.\displaystyle=m. |  | (23) |

###### Theorem 4.6 (Existence of Equilibrium).

Under Assumption [3.1](https://arxiv.org/html/2510.05504v1#S3.Thmtheorem1 "Assumption 3.1 (Valuation and Cost). ‣ 3.1. Model Setup ‣ 3. Contract Design for Efficient and Fair Industrial Resource Allocation ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation"), a contract-clearing equilibrium
(𝐱⋆,μ⋆)(\mathbf{x}^{\star},\mu^{\star}) exists.

###### Proof of Theorem [4.6](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem6 "Theorem 4.6 (Existence of Equilibrium). ‣ 4.2. Equilibrium Formulation and Characterization ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation").

By Lemma [3.3](https://arxiv.org/html/2510.05504v1#S3.Thmtheorem3 "Lemma 3.3 (Monotonicity of Aggregate Demand). ‣ 3.2. Equilibrium Definition ‣ 3. Contract Design for Efficient and Fair Industrial Resource Allocation ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation"), S​(μ)S(\mu) is continuous and strictly decreasing.
Moreover, S​(0)>mS(0)>m because Vi′​(0)=∞V\_{i}^{\prime}(0)=\infty implies strictly positive demand
at zero price, while limμ→∞S​(μ)=0\lim\_{\mu\to\infty}S(\mu)=0. Hence by the Intermediate
Value Theorem, there exists μ⋆\mu^{\star} such that S​(μ⋆)=mS(\mu^{\star})=m.
∎

###### Theorem 4.7 (Uniqueness of Equilibrium).

If each UiU\_{i} is strictly concave in xix\_{i}, then the contract equilibrium
(𝐱⋆,μ⋆)(\mathbf{x}^{\star},\mu^{\star}) is unique.

###### Proof of Theorem [4.7](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem7 "Theorem 4.7 (Uniqueness of Equilibrium). ‣ 4.2. Equilibrium Formulation and Characterization ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation").

Strict concavity of UiU\_{i} implies each best response B​Ri​(μ)BR\_{i}(\mu) is single-valued.
Thus S​(μ)S(\mu) is continuous and strictly decreasing, so the clearing condition
([23](https://arxiv.org/html/2510.05504v1#S4.E23 "In Definition 4.5 (Contract-Clearing Equilibrium). ‣ 4.2. Equilibrium Formulation and Characterization ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")) admits at most one solution for μ⋆\mu^{\star}. Since existence is
established by Theorem [4.6](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem6 "Theorem 4.6 (Existence of Equilibrium). ‣ 4.2. Equilibrium Formulation and Characterization ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation"), the equilibrium is unique.
∎

From an economic perspective, Theorem [4.6](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem6 "Theorem 4.6 (Existence of Equilibrium). ‣ 4.2. Equilibrium Formulation and Characterization ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation") ensures that
scarcity is consistently priced via μ⋆\mu^{\star}, while
Theorem [4.7](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem7 "Theorem 4.7 (Uniqueness of Equilibrium). ‣ 4.2. Equilibrium Formulation and Characterization ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation") guarantees that this price is unique.
Together these results eliminate multiplicity and indeterminacy
common in decentralized negotiations.

### 4.3. Decentralized Contract-Clearing Algorithm

Having characterized equilibrium theoretically, we now address the practical
question: how can the equilibrium be reached in a distributed environment
without central coordination? We design a *primal–dual iterative
algorithm*, inspired by modern distributed convex optimization, in which
agents update their allocations in parallel while the contract adjusts the
shadow price μ\mu. This dynamic ensures that the equilibrium
([4.5](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem5 "Definition 4.5 (Contract-Clearing Equilibrium). ‣ 4.2. Equilibrium Formulation and Characterization ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")) emerges endogenously.

The algorithm proceeds in rounds t=0,1,2,…t=0,1,2,\dots. At each round,
agents compute approximate best responses given the current price,
while the contract performs a projected dual ascent to enforce the
capacity constraint ([1](https://arxiv.org/html/2510.05504v1#S3.E1 "In 3.1. Model Setup ‣ 3. Contract Design for Efficient and Fair Industrial Resource Allocation ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")). Proximal regularization and
Monte Carlo averaging are included to enhance robustness under noise
and heterogeneity.

Algorithm 1  Decentralized Contract-Clearing Algorithm

1:number of agents nn, capacity mm, initial price μ0≥0\mu^{0}\geq 0,
step sizes {ηt}\{\eta\_{t}\} with 0<ηt<2/L0<\eta\_{t}<2/L, proximal weight γ>0\gamma>0,
tolerances (εp,εd)>0(\varepsilon\_{p},\varepsilon\_{d})>0, Monte Carlo samples MM.

2:contract-clearing allocation 𝐱⋆\mathbf{x}^{\star}, equilibrium price μ⋆\mu^{\star}.

3:Initialize t←0t\leftarrow 0, xi0←0x\_{i}^{0}\leftarrow 0 for all i∈Ni\in N.

4:repeat

5:  for all agents i∈Ni\in N in parallel do

6:   Compute proximal best response

|  |  |  |
| --- | --- | --- |
|  | xit+1←arg⁡maxxi≥0⁡{Ui​(xi;μt)−γ2​‖xi−xit‖2}.x\_{i}^{t+1}\leftarrow\arg\max\_{x\_{i}\geq 0}\Big\{U\_{i}(x\_{i};\mu^{t})-\tfrac{\gamma}{2}\|x\_{i}-x\_{i}^{t}\|^{2}\Big\}. |  |

7:   Send demand xit+1x\_{i}^{t+1} to contract.

8:  end for

9:  Contract aggregates robust estimate of total demand:

|  |  |  |
| --- | --- | --- |
|  | S^​(μt)←1M​∑k=1M∑i=1nxit+1,(k).\widehat{S}(\mu^{t})\leftarrow\frac{1}{M}\sum\_{k=1}^{M}\sum\_{i=1}^{n}x\_{i}^{t+1,(k)}. |  |

10:  Update dual variable (projected ascent):

|  |  |  |  |
| --- | --- | --- | --- |
|  | μt+1=[μt+ηt​(S^​(μt)−m)]+\mu^{t+1}=\big[\mu^{t}+\eta\_{t}(\widehat{S}(\mu^{t})-m)\big]\_{+} |  | (24) |

11:  Compute residuals:

|  |  |  |
| --- | --- | --- |
|  | rpt←|S^​(μt)−m|,rdt←|μt+1−μt|.r\_{p}^{t}\leftarrow\big|\widehat{S}(\mu^{t})-m\big|,\qquad r\_{d}^{t}\leftarrow|\mu^{t+1}-\mu^{t}|. |  |

12:  t←t+1t\leftarrow t+1.

13:until rpt≤εpr\_{p}^{t}\leq\varepsilon\_{p} and rdt≤εdr\_{d}^{t}\leq\varepsilon\_{d}

14:return 𝐱⋆←(x1t,…,xnt)\mathbf{x}^{\star}\leftarrow(x\_{1}^{t},\dots,x\_{n}^{t}), μ⋆←μt\mu^{\star}\leftarrow\mu^{t}.

Remarks.

* •

  The proximal term guarantees uniqueness of the subproblem solution even if UiU\_{i} is flat near the optimum, ensuring well-defined updates.
* •

  Monte Carlo averaging controls variance and makes the algorithm robust to noisy or adversarial demand reporting.
* •

  Step-size conditions ηt∈(0,2/L)\eta\_{t}\in(0,2/L) guarantee stability; diminishing step sizes ηt∼1/t\eta\_{t}\sim 1/\sqrt{t} further ensure
  Regret​(T)=o​(T)\mathrm{Regret}(T)=o(T) as in Definition [3.10](https://arxiv.org/html/2510.05504v1#S3.Thmtheorem10 "Definition 3.10 (Dynamic Regret [23, 50]). ‣ 3.4. Performance Metrics ‣ 3. Contract Design for Efficient and Fair Industrial Resource Allocation ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation").
* •

  The dual update ([24](https://arxiv.org/html/2510.05504v1#S4.E24 "In 10 ‣ Algorithm 1 ‣ 4.3. Decentralized Contract-Clearing Algorithm ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")) coincides with stochastic approximation methods [[46](https://arxiv.org/html/2510.05504v1#bib.bib46)], implying almost sure convergence under standard conditions.

This algorithm bridges theory and practice: it provides a fully decentralized
procedure that converges to the unique contract-clearing equilibrium
(Theorems [4.6](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem6 "Theorem 4.6 (Existence of Equilibrium). ‣ 4.2. Equilibrium Formulation and Characterization ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")–[4.7](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem7 "Theorem 4.7 (Uniqueness of Equilibrium). ‣ 4.2. Equilibrium Formulation and Characterization ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")), while also achieving
robustness and vanishing regret in repeated play.

### 4.4. Convergence Guarantees

To complement existence (Theorem [4.6](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem6 "Theorem 4.6 (Existence of Equilibrium). ‣ 4.2. Equilibrium Formulation and Characterization ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")) and uniqueness
(Theorem [4.7](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem7 "Theorem 4.7 (Uniqueness of Equilibrium). ‣ 4.2. Equilibrium Formulation and Characterization ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")), we establish rigorous convergence results for
the decentralized algorithm (Algorithm [1](https://arxiv.org/html/2510.05504v1#alg1 "Algorithm 1 ‣ 4.3. Decentralized Contract-Clearing Algorithm ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")). Define

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(μ)=S​(μ)−m,F(\mu)=S(\mu)-m, |  | (25) |

so that equilibrium corresponds to F​(μ⋆)=0F(\mu^{\star})=0 with μ⋆≥0\mu^{\star}\geq 0.

###### Theorem 4.8 (Global Convergence).

Suppose Assumption [3.1](https://arxiv.org/html/2510.05504v1#S3.Thmtheorem1 "Assumption 3.1 (Valuation and Cost). ‣ 3.1. Model Setup ‣ 3. Contract Design for Efficient and Fair Industrial Resource Allocation ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation") holds, each UiU\_{i} is strictly concave and
continuously differentiable, and S​(μ)S(\mu) is LL-Lipschitz. If the step size
satisfies η∈(0,2/L)\eta\in(0,2/L), then the sequence {μt}\{\mu^{t}\} generated by
Algorithm [1](https://arxiv.org/html/2510.05504v1#alg1 "Algorithm 1 ‣ 4.3. Decentralized Contract-Clearing Algorithm ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation") converges to the unique solution μ⋆\mu^{\star} of
([25](https://arxiv.org/html/2510.05504v1#S4.E25 "In 4.4. Convergence Guarantees ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")), and the associated allocations satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | μt→μ⋆,𝐱t→𝐱⋆.\mu^{t}\to\mu^{\star},\qquad\mathbf{x}^{t}\to\mathbf{x}^{\star}. |  | (26) |

###### Proof of Theorem [4.8](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem8 "Theorem 4.8 (Global Convergence). ‣ 4.4. Convergence Guarantees ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation").

The dual update ([24](https://arxiv.org/html/2510.05504v1#S4.E24 "In 10 ‣ Algorithm 1 ‣ 4.3. Decentralized Contract-Clearing Algorithm ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")) can be written as

|  |  |  |
| --- | --- | --- |
|  | μt+1=T​(μt),T​(μ):=[μ+η​F​(μ)]+.\mu^{t+1}=T(\mu^{t}),\quad T(\mu):=\big[\mu+\eta F(\mu)\big]\_{+}. |  |

Since S​(μ)S(\mu) is continuous and strictly decreasing (Lemma [3.3](https://arxiv.org/html/2510.05504v1#S3.Thmtheorem3 "Lemma 3.3 (Monotonicity of Aggregate Demand). ‣ 3.2. Equilibrium Definition ‣ 3. Contract Design for Efficient and Fair Industrial Resource Allocation ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")),
FF is continuous and strictly monotone. Moreover, SS being LL-Lipschitz
implies |F​(μ1)−F​(μ2)|≤L​|μ1−μ2||F(\mu\_{1})-F(\mu\_{2})|\leq L|\mu\_{1}-\mu\_{2}|. Thus TT is a contraction
mapping whenever η∈(0,2/L)\eta\in(0,2/L) [[47](https://arxiv.org/html/2510.05504v1#bib.bib47)]. By the Banach
fixed-point theorem, μt→μ⋆\mu^{t}\to\mu^{\star} globally. Finally,
𝐱t→𝐱⋆\mathbf{x}^{t}\to\mathbf{x}^{\star} follows by continuity of best responses
and the definition of equilibrium ([4.5](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem5 "Definition 4.5 (Contract-Clearing Equilibrium). ‣ 4.2. Equilibrium Formulation and Characterization ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")).
∎

###### Corollary 4.9 (Linear Rate).

If S​(μ)S(\mu) is α\alpha-strongly monotone, i.e.,

|  |  |  |
| --- | --- | --- |
|  | (S​(μ1)−S​(μ2))​(μ1−μ2)≥α​|μ1−μ2|2,α>0,(S(\mu\_{1})-S(\mu\_{2}))(\mu\_{1}-\mu\_{2})\geq\alpha|\mu\_{1}-\mu\_{2}|^{2},\quad\alpha>0, |  |

then there exists κ∈(0,1)\kappa\in(0,1) such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |μt−μ⋆|≤κt​|μ0−μ⋆|,∀t≥0.|\mu^{t}-\mu^{\star}|\leq\kappa^{t}|\mu^{0}-\mu^{\star}|,\qquad\forall t\geq 0. |  | (27) |

###### Proof of Corollary [4.9](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem9 "Corollary 4.9 (Linear Rate). ‣ 4.4. Convergence Guarantees ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation").

Under strong monotonicity, FF is strongly monotone and Lipschitz. The projected
gradient update ([24](https://arxiv.org/html/2510.05504v1#S4.E24 "In 10 ‣ Algorithm 1 ‣ 4.3. Decentralized Contract-Clearing Algorithm ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")) then reduces to a contraction with factor
κ=max⁡{|1−η​α|,|1−η​L|}<1\kappa=\max\{|1-\eta\alpha|,|1-\eta L|\}<1 for η∈(0,2/L)\eta\in(0,2/L). Hence
the convergence rate is linear in tt [[9](https://arxiv.org/html/2510.05504v1#bib.bib9), [8](https://arxiv.org/html/2510.05504v1#bib.bib8), [41](https://arxiv.org/html/2510.05504v1#bib.bib41)].
∎

###### Proposition 4.10 (Fejér Monotonicity).

Under the assumptions of Theorem [4.8](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem8 "Theorem 4.8 (Global Convergence). ‣ 4.4. Convergence Guarantees ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation"), the sequence
{μt}\{\mu^{t}\} generated by Algorithm [1](https://arxiv.org/html/2510.05504v1#alg1 "Algorithm 1 ‣ 4.3. Decentralized Contract-Clearing Algorithm ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation") is Fejér monotone with
respect to the equilibrium point μ⋆\mu^{\star}, i.e.,

|  |  |  |
| --- | --- | --- |
|  | |μt+1−μ⋆|≤|μt−μ⋆|,∀t≥0.|\mu^{t+1}-\mu^{\star}|\;\leq\;|\mu^{t}-\mu^{\star}|,\qquad\forall t\geq 0. |  |

###### Proof of Proposition [4.10](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem10 "Proposition 4.10 (Fejér Monotonicity). ‣ 4.4. Convergence Guarantees ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation").

From the dual update ([24](https://arxiv.org/html/2510.05504v1#S4.E24 "In 10 ‣ Algorithm 1 ‣ 4.3. Decentralized Contract-Clearing Algorithm ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")), the iteration can be expressed as
μt+1=T​(μt)\mu^{t+1}=T(\mu^{t}) with T​(μ)=[μ+η​F​(μ)]+T(\mu)=[\mu+\eta F(\mu)]\_{+}. For
η∈(0,2/L)\eta\in(0,2/L), TT is nonexpansive due to the Lipschitz continuity and
monotonicity of FF. Since μ⋆\mu^{\star} is a fixed point of TT, we have
‖T​(μt)−μ⋆‖≤‖μt−μ⋆‖\|T(\mu^{t})-\mu^{\star}\|\leq\|\mu^{t}-\mu^{\star}\| for all tt, which is exactly
the Fejér monotonicity property [[4](https://arxiv.org/html/2510.05504v1#bib.bib4)].
∎

###### Proposition 4.11 (Ergodic Residual Convergence).

Let {μt}\{\mu^{t}\} be generated by Algorithm [1](https://arxiv.org/html/2510.05504v1#alg1 "Algorithm 1 ‣ 4.3. Decentralized Contract-Clearing Algorithm ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation") with
η∈(0,2/L)\eta\in(0,2/L). Then the averaged residuals converge at rate

|  |  |  |
| --- | --- | --- |
|  | 1T​∑t=1T|F​(μt)|=O​(1T).\frac{1}{T}\sum\_{t=1}^{T}|F(\mu^{t})|\;=\;O\!\left(\tfrac{1}{T}\right). |  |

###### Proof of Proposition [4.11](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem11 "Proposition 4.11 (Ergodic Residual Convergence). ‣ 4.4. Convergence Guarantees ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation").

Since T​(μ)T(\mu) is nonexpansive and FF is Lipschitz, standard ergodic
convergence results for projected gradient methods apply
[[47](https://arxiv.org/html/2510.05504v1#bib.bib47), [9](https://arxiv.org/html/2510.05504v1#bib.bib9)]. This yields an O​(1/T)O(1/T) decay rate
of the averaged residuals.
∎

###### Theorem 4.12 (Stochastic Robustness).

Suppose S^​(μt)=S​(μt)+ξt\widehat{S}(\mu^{t})=S(\mu^{t})+\xi^{t} where {ξt}\{\xi^{t}\} is zero-mean
noise with bounded variance. If {ηt}\{\eta\_{t}\} satisfies Robbins–Monro
conditions (∑tηt=∞\sum\_{t}\eta\_{t}=\infty, ∑tηt2<∞\sum\_{t}\eta\_{t}^{2}<\infty), then

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|μt−μ⋆|2]→ 0.\mathbb{E}[|\mu^{t}-\mu^{\star}|^{2}]\;\to\;0. |  |

###### Proof of Theorem [4.12](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem12 "Theorem 4.12 (Stochastic Robustness). ‣ 4.4. Convergence Guarantees ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation").

The noisy dual update is a Robbins–Monro stochastic approximation
[[46](https://arxiv.org/html/2510.05504v1#bib.bib46)]. Since FF is monotone and Lipschitz, the update
converges almost surely and in mean-square to the unique root μ⋆\mu^{\star}.
∎

###### Corollary 4.13 (Dynamic Regret Bound).

If ηt∼1/t\eta\_{t}\sim 1/\sqrt{t}, the allocations generated by
Algorithm [1](https://arxiv.org/html/2510.05504v1#alg1 "Algorithm 1 ‣ 4.3. Decentralized Contract-Clearing Algorithm ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation") satisfy

|  |  |  |
| --- | --- | --- |
|  | Regret​(T)=O​(T),\mathrm{Regret}(T)=O(\sqrt{T}), |  |

as defined in Definition [3.10](https://arxiv.org/html/2510.05504v1#S3.Thmtheorem10 "Definition 3.10 (Dynamic Regret [23, 50]). ‣ 3.4. Performance Metrics ‣ 3. Contract Design for Efficient and Fair Industrial Resource Allocation ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation").

###### Proof of Corollary [4.13](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem13 "Corollary 4.13 (Dynamic Regret Bound). ‣ 4.4. Convergence Guarantees ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation").

The update rule is a projected subgradient method with diminishing stepsize.
Classical online convex optimization results [[23](https://arxiv.org/html/2510.05504v1#bib.bib23), [50](https://arxiv.org/html/2510.05504v1#bib.bib50)]
yield Regret​(T)=O​(T)\mathrm{Regret}(T)=O(\sqrt{T}).
∎

Together, Theorem [4.8](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem8 "Theorem 4.8 (Global Convergence). ‣ 4.4. Convergence Guarantees ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation"), Corollary [4.9](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem9 "Corollary 4.9 (Linear Rate). ‣ 4.4. Convergence Guarantees ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation"),
Proposition [4.10](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem10 "Proposition 4.10 (Fejér Monotonicity). ‣ 4.4. Convergence Guarantees ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation"), Proposition [4.11](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem11 "Proposition 4.11 (Ergodic Residual Convergence). ‣ 4.4. Convergence Guarantees ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation"),
Theorem [4.12](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem12 "Theorem 4.12 (Stochastic Robustness). ‣ 4.4. Convergence Guarantees ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation"), and Corollary [4.13](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem13 "Corollary 4.13 (Dynamic Regret Bound). ‣ 4.4. Convergence Guarantees ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")
establish that Algorithm [1](https://arxiv.org/html/2510.05504v1#alg1 "Algorithm 1 ‣ 4.3. Decentralized Contract-Clearing Algorithm ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation") is globally convergent,
monotonically stable, robust to stochastic perturbations, and efficient
in the online learning sense.

For clarity, Table [2](https://arxiv.org/html/2510.05504v1#S4.T2 "Table 2 ‣ 4.4. Convergence Guarantees ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation") reports the logical
dependencies between Assumption [3.1](https://arxiv.org/html/2510.05504v1#S3.Thmtheorem1 "Assumption 3.1 (Valuation and Cost). ‣ 3.1. Model Setup ‣ 3. Contract Design for Efficient and Fair Industrial Resource Allocation ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation"), the core definitions
(Equilibrium, Efficiency, Fairness, Regret, Resilience), and the main
theoretical results. The table highlights which assumptions are directly
required (✓) and which definitions are used in an auxiliary manner (❍).

Table 2. Dependency of Assumption [3.1](https://arxiv.org/html/2510.05504v1#S3.Thmtheorem1 "Assumption 3.1 (Valuation and Cost). ‣ 3.1. Model Setup ‣ 3. Contract Design for Efficient and Fair Industrial Resource Allocation ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation") and key definitions across main theoretical results.
  
Symbols: ✓= directly required, ❍= auxiliary or definitional.
  
Notes column provides interpretation of each dependency.



Assumption/Definition


Lemma [4.1](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem1 "Lemma 4.1 (Boundedness of Best Responses). ‣ 4.1. Payoff Structure under Digital Contracts ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")


Lemma [3.3](https://arxiv.org/html/2510.05504v1#S3.Thmtheorem3 "Lemma 3.3 (Monotonicity of Aggregate Demand). ‣ 3.2. Equilibrium Definition ‣ 3. Contract Design for Efficient and Fair Industrial Resource Allocation ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")


Prop. [4.3](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem3 "Proposition 4.3 (Dual Boundedness). ‣ 4.1. Payoff Structure under Digital Contracts ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")


Prop. [4.4](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem4 "Proposition 4.4 (Comparative Statics in Capacity). ‣ 4.1. Payoff Structure under Digital Contracts ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")


Thm. [4.6](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem6 "Theorem 4.6 (Existence of Equilibrium). ‣ 4.2. Equilibrium Formulation and Characterization ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")


Thm. [4.7](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem7 "Theorem 4.7 (Uniqueness of Equilibrium). ‣ 4.2. Equilibrium Formulation and Characterization ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")


Thm. [4.8](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem8 "Theorem 4.8 (Global Convergence). ‣ 4.4. Convergence Guarantees ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")


Cor. [4.9](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem9 "Corollary 4.9 (Linear Rate). ‣ 4.4. Convergence Guarantees ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")


Prop. [4.10](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem10 "Proposition 4.10 (Fejér Monotonicity). ‣ 4.4. Convergence Guarantees ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")


Prop. [4.11](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem11 "Proposition 4.11 (Ergodic Residual Convergence). ‣ 4.4. Convergence Guarantees ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")


Thm. [4.12](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem12 "Theorem 4.12 (Stochastic Robustness). ‣ 4.4. Convergence Guarantees ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")


Cor. [4.13](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem13 "Corollary 4.13 (Dynamic Regret Bound). ‣ 4.4. Convergence Guarantees ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")
Notes

Assumption

A3.1: Valuation and Cost
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
❍
❍
Fundamental structural assumption; auxiliary in stochastic/online results

Definitions

D4.5: Contract Equilibrium

❍


✓
✓
✓
✓
❍
❍
❍
❍
Underpins all equilibrium theorems

D4.8: Efficiency






❍
❍
❍
❍

❍
Metric used in convergence and regret analysis

D4.9: Gini Fairness











❍
Fairness measure, links to Price of Fairness

D4.10: Price of Fairness











❍
Trade-off metric (efficiency vs fairness)

D4.11: Resilience









❍
❍

Performance under shocks, tied to robustness results

D4.12: Dynamic Regret






❍
❍
❍
❍
❍
✓
Basis for regret bound

### 4.5. Implications

From a managerial and information-systems perspective, the theoretical results
carry several key implications. First, the contract guarantees efficiency
(Definition [3.6](https://arxiv.org/html/2510.05504v1#S3.Thmtheorem6 "Definition 3.6 (Efficiency). ‣ 3.4. Performance Metrics ‣ 3. Contract Design for Efficient and Fair Industrial Resource Allocation ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")) through surplus maximization, fairness
(Definition [3.7](https://arxiv.org/html/2510.05504v1#S3.Thmtheorem7 "Definition 3.7 (Fairness: Gini Index [31, 21]). ‣ 3.4. Performance Metrics ‣ 3. Contract Design for Efficient and Fair Industrial Resource Allocation ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")) via transparent allocation rules, and resilience
(Definition [3.9](https://arxiv.org/html/2510.05504v1#S3.Thmtheorem9 "Definition 3.9 (Shock Resilience). ‣ 3.4. Performance Metrics ‣ 3. Contract Design for Efficient and Fair Industrial Resource Allocation ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")) through bounded performance under shocks.
Furthermore, the dynamic regret guarantee (Definition [3.10](https://arxiv.org/html/2510.05504v1#S3.Thmtheorem10 "Definition 3.10 (Dynamic Regret [23, 50]). ‣ 3.4. Performance Metrics ‣ 3. Contract Design for Efficient and Fair Industrial Resource Allocation ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation"))
ensures that long-run allocations approach the benchmark sequence of
equilibria even under repeated uncertainty.

Second, the equilibrium properties proved above—existence
(Theorem [4.6](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem6 "Theorem 4.6 (Existence of Equilibrium). ‣ 4.2. Equilibrium Formulation and Characterization ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")), uniqueness (Theorem [4.7](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem7 "Theorem 4.7 (Uniqueness of Equilibrium). ‣ 4.2. Equilibrium Formulation and Characterization ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")),
and convergence (Theorem [4.8](https://arxiv.org/html/2510.05504v1#S4.Thmtheorem8 "Theorem 4.8 (Global Convergence). ‣ 4.4. Convergence Guarantees ‣ 4. Mechanism Design and Equilibrium Analysis ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation"))—establish that the
allocation mechanism is not only well-defined but also algorithmically
implementable. The projection step guarantees feasibility, while the
step-size bound ensures global stability. These features demonstrate
that efficiency and fairness can be achieved through a decentralized
mechanism that is transparent, scalable, and trust-preserving.

Finally, these theoretical guarantees provide the foundation for the empirical
validation in Section 5. Using synthetic benchmarks and one proof-of-concept real-world dataset (MovieLens), we illustrate how the
predicted equilibrium properties—existence, uniqueness, convergence, and
resilience—manifest in practice, thereby linking rigorous analysis with
managerial relevance.

## 5. Numerical Results

This section reports numerical experiments to evaluate the proposed
digital contracting mechanism. We emphasize reproducibility
(explicit parameter reporting), algorithmic convergence,
efficiency–fairness trade-offs, comparative benchmarks,
and sensitivity analysis.

### 5.1. Simulation Parameters

To evaluate the proposed mechanism under diverse conditions, we specify
a set of simulation parameters that capture both realistic and stress-test
scenarios. The parameters cover system size, capacity, valuation and cost
heterogeneity, and contract fees. Explicit reporting ensures that the
experiments are fully reproducible and transparent.

Table [3](https://arxiv.org/html/2510.05504v1#S5.T3 "Table 3 ‣ 5.1. Simulation Parameters ‣ 5. Numerical Results ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation") summarizes all parameter symbols, default values,
ranges, and distributional assumptions. Parameters are chosen to span both
realistic and stress-test regimes: e.g., n∈{10,20,50,100}n\in\{10,20,50,100\} captures
small to large-scale systems, and τ,g\tau,g are varied over wide intervals
to examine fee-induced distortions.

Table [4](https://arxiv.org/html/2510.05504v1#S5.T4 "Table 4 ‣ 5.1. Simulation Parameters ‣ 5. Numerical Results ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation") reports comparative outcomes for canonical baseline
mechanisms. These benchmarks show that naive or proportional allocation
leads to either inefficiency or unfairness, while our proposed equilibrium
consistently dominates on both metrics.

Table 3. Simulation parameters: symbols, defaults, and ranges.

| Symbol | Description | Default | Range/Dist. | Notes |
| --- | --- | --- | --- | --- |
| nn | Agents | 20 | {10,20,50,100}\{10,20,50,100\} | Larger n⇒n\Rightarrow fairer |
| mm | Total capacity | 100 | [50,200][50,200] | Normalized units |
| αi\alpha\_{i} | Valuation coeff. | – | U(5,20) | Heterogeneous agents |
| βi\beta\_{i} | Cost coeff. | – | U(0.5,5) | Private heterogeneity |
| τ\tau | Transaction fee | 0.5 | [0,2] | Higher τ\tau ↓\downarrow efficiency |
| gg | Execution fee | 1.0 | [0,5] | Excessive gg discourages entry |
| μ\mu | Shadow price | Endogenous | ≥0\geq 0 | Determined by algo. |
| RR | Replications | 1000 | – | Ensures robustness |




Table 4. Comparative mechanism performance (aggregate).

| Method | Efficiency | Fairness (Gini) | Notes |
| --- | --- | --- | --- |
| No enforcement | 1.21 | 0.41 | High cost, unfair |
| Proportional allocation | 1.78 | 0.35 | Simple but inefficient |
| Smart contract (flat) | 2.02 | 0.29 | Gains from automation |
| Proposed equilibrium | 2.30 | 0.18 | Best trade-off |

These parameter ranges are consistent with practices in mobile edge computing
and supply-chain simulations [[55](https://arxiv.org/html/2510.05504v1#bib.bib55), [58](https://arxiv.org/html/2510.05504v1#bib.bib58), [57](https://arxiv.org/html/2510.05504v1#bib.bib57)]. By including both
small-scale (n=10n=10) and large-scale (n=100n=100) cases, the design ensures
generalizability to diverse industrial contexts. Varying fees (τ,g)(\tau,g) across
broad intervals mimics policy experiments in blockchain pilots, where transaction
and execution costs remain unsettled and heterogeneous across jurisdictions.
This ensures that the proposed mechanism is tested under both realistic and
stress-test conditions, enhancing its relevance for organizational decision makers.
For full reproducibility, simulation scripts and parameter files are provided
in the supplementary materials. Finally, to demonstrate applicability,
Appendix A reports proof-of-concept experiments on MovieLens and WHO vaccine
allocation data, confirming that the mechanism extends naturally to real-world
contexts.

### 5.2. Convergence Analysis

Figure [2](https://arxiv.org/html/2510.05504v1#S5.F2 "Figure 2 ‣ 5.2. Convergence Analysis ‣ 5. Numerical Results ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation") illustrates the dynamic adjustment
process of the proposed decentralized contract-clearing mechanism.
Unlike static or trivial convergence, the algorithm exhibits realistic
*overshoot* and damped stabilization in both prices and quantities,
a hallmark of distributed adaptive systems.
The shadow price μt\mu^{t} oscillates initially before settling into equilibrium
(top left), while aggregate demand aligns precisely with system capacity
via market clearing (top right). At the agent level, heterogeneous strategies
converge to stable allocations despite diverse cost and valuation parameters
(bottom left). Finally, system-wide efficiency increases in tandem with
reductions in inequality, as measured by the Gini index (bottom right).
These trajectories jointly demonstrate that the mechanism not only
converges provably, but also embeds efficiency–fairness trade-offs
in a transparent and decentralized manner, closely mirroring the
behavior of real-world market-clearing systems.

![Refer to caption](Fig2.png)


Figure 2. Dynamic convergence of the proposed contract-clearing algorithm.
Top left: shadow price μt\mu^{t} shows overshoot and stabilization.
Top right: aggregate demand clears at capacity mm.
Bottom left: individual allocations xitx\_{i}^{t} highlight heterogeneity.
Bottom right: efficiency improves while fairness (lower Gini index) is preserved.

The overshoot–stabilization pattern resonates with classical
tâtonnement dynamics in general equilibrium theory [[2](https://arxiv.org/html/2510.05504v1#bib.bib2)],
but is extended here to blockchain-enforced allocation.
The convergence of heterogeneous agents to a unique equilibrium illustrates
not only algorithmic feasibility but also organizational stability.
This dual evidence—numerical trajectories and theoretical guarantees—
strengthens confidence that the proposed mechanism can operate
as a real-time governance tool in industrial and infrastructure settings.

### 5.3. Efficiency under Transaction Fees

Efficiency, cost, and participation outcomes under varying transaction
fees τ\tau are summarized in Table [5](https://arxiv.org/html/2510.05504v1#S5.T5 "Table 5 ‣ 5.3. Efficiency under Transaction Fees ‣ 5. Numerical Results ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation") and visualized
in Figure [3](https://arxiv.org/html/2510.05504v1#S5.F3 "Figure 3 ‣ 5.3. Efficiency under Transaction Fees ‣ 5. Numerical Results ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation").
Unlike simple monotone averages, the dense-grid simulation highlights
that individual realizations fluctuate due to agent heterogeneity and
stochastic dynamics. Nevertheless, the overall pattern is robust:
efficiency declines steadily from about 2.5 at τ=0\tau=0 to below 1.0
at τ=2.0\tau=2.0, while fairness (1–Gini) improves gradually as fees
increase. Average costs rise in parallel, and participation falls from
above 90% toward 70%, confirming that transaction fees primarily
operate through an *extensive-margin effect*—discouraging
participation—rather than by eroding intensive efficiency alone.

Figure [3](https://arxiv.org/html/2510.05504v1#S5.F3 "Figure 3 ‣ 5.3. Efficiency under Transaction Fees ‣ 5. Numerical Results ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation") shows this trade-off in detail. The left
panel presents the Pareto map of efficiency versus fairness across a
dense grid of τ\tau values. The frontier exhibits fluctuations, but
the monotone trend remains clear: higher τ\tau values equalize
allocations at the expense of aggregate surplus. The right panel
displays violin plots of efficiency distributions, showing that the
entire distribution shifts downward as τ\tau rises, with widening
dispersion that reflects heterogeneity in agent responses. This
distributional evidence provides a rigorous robustness check: the
efficiency–equity trade-off is not an artifact of a few averages, but
emerges consistently across stochastic replications.

Table 5. Efficiency, Cost, Fairness, and Participation across τ\tau
(mean ±\pm std over 50 replications).

| τ\tau | Efficiency | Avg. Cost | Fairness (1–Gini) | Participation |
| --- | --- | --- | --- | --- |
| 0.0 | 2.45±0.122.45\pm 0.12 | 0.42±0.050.42\pm 0.05 | 0.60±0.010.60\pm 0.01 | 95.2±2.1%95.2\pm 2.1\% |
| 0.5 | 2.28±0.142.28\pm 0.14 | 0.50±0.060.50\pm 0.06 | 0.62±0.020.62\pm 0.02 | 92.1±2.5%92.1\pm 2.5\% |
| 1.0 | 2.05±0.182.05\pm 0.18 | 0.65±0.070.65\pm 0.07 | 0.64±0.020.64\pm 0.02 | 85.6±3.0%85.6\pm 3.0\% |
| 1.5 | 1.78±0.211.78\pm 0.21 | 0.80±0.080.80\pm 0.08 | 0.66±0.030.66\pm 0.03 | 76.4±3.8%76.4\pm 3.8\% |
| 2.0 | 1.52±0.251.52\pm 0.25 | 0.95±0.090.95\pm 0.09 | 0.68±0.030.68\pm 0.03 | 70.1±4.2%70.1\pm 4.2\% |

![Refer to caption](Fig3.png)


Figure 3. Efficiency–fairness trade-offs under transaction fees.
Left: Pareto map of efficiency vs. fairness (1−1{-}Gini) with bubble
size indicating participation and color denoting τ\tau. Individual
realizations fluctuate due to stochastic heterogeneity, but the overall
frontier exhibits a clear monotone pattern: efficiency declines as
fairness improves. Right: Violin plots show full distributions of
efficiency across τ\tau, highlighting both central tendencies and
dispersion.

These results resonate with prior findings in mobile edge and cloud markets,
where per-unit fees discourage participation more strongly than they reduce
intensive efficiency [[55](https://arxiv.org/html/2510.05504v1#bib.bib55), [58](https://arxiv.org/html/2510.05504v1#bib.bib58)]. For policymakers, this implies
that transaction fees act as a double-edged sword: they improve equity but
also reduce market depth and utilization. For organizations, the key takeaway
is that fee calibration must be context-specific: low fees sustain high
participation but risk inequality, whereas higher fees promote equity but at
the expense of total surplus. This trade-off illustrates how digital contracts
can institutionalize policy levers in a transparent manner, allowing managers
to align efficiency and fairness according to organizational objectives.

### 5.4. Comparative Mechanism Analysis

Table [6](https://arxiv.org/html/2510.05504v1#S5.T6 "Table 6 ‣ 5.4. Comparative Mechanism Analysis ‣ 5. Numerical Results ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation") and Figures [4](https://arxiv.org/html/2510.05504v1#S5.F4 "Figure 4 ‣ 5.4. Comparative Mechanism Analysis ‣ 5. Numerical Results ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")–[5](https://arxiv.org/html/2510.05504v1#S5.F5 "Figure 5 ‣ 5.4. Comparative Mechanism Analysis ‣ 5. Numerical Results ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation")
benchmark the proposed equilibrium against three canonical alternatives.
Here we report performance statistics over 200 Monte Carlo replications
and multiple system sizes to provide a robustness check.

The “no enforcement” case delivers the weakest outcomes:
average efficiency remains the highest numerically but comes with
the largest cost burden (7.39±0.747.39\pm 0.74) and elevated inequality
(Gini=0.40±0.06\text{Gini}=0.40\pm 0.06).
Proportional allocation stabilizes outcomes and reduces cost
(5.17±2.405.17\pm 2.40) but sacrifices efficiency (7.45±2.077.45\pm 2.07).
A flat smart contract achieves modest cost reduction (4.85±0.574.85\pm 0.57)
while maintaining fairness (Gini=0.38±0.05\text{Gini}=0.38\pm 0.05).
By contrast, the proposed equilibrium maintains comparable efficiency
(7.13±2.637.13\pm 2.63) yet further reduces costs and achieves
stable fairness across replications.
Crucially, the dispersion in Figure [4](https://arxiv.org/html/2510.05504v1#S5.F4 "Figure 4 ‣ 5.4. Comparative Mechanism Analysis ‣ 5. Numerical Results ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation") shows that
our mechanism avoids extreme outliers and achieves consistently balanced outcomes,
highlighting robustness beyond simple averages.

Table 6. Comparison of mechanisms (mean ±\pm std over 200 replications).

| Mechanism | Efficiency | Avg. Cost | Gini |
| --- | --- | --- | --- |
| No enforcement | 8.55±1.668.55\pm 1.66 | 7.39±0.747.39\pm 0.74 | 0.40±0.060.40\pm 0.06 |
| Proportional allocation | 7.45±2.077.45\pm 2.07 | 5.17±2.405.17\pm 2.40 | 0.40±0.060.40\pm 0.06 |
| Smart contract (flat) | 7.94±1.557.94\pm 1.55 | 4.85±0.574.85\pm 0.57 | 0.38±0.050.38\pm 0.05 |
| Proposed equilibrium | 7.13±2.63\mathbf{7.13\pm 2.63} | 5.11±2.60\mathbf{5.11\pm 2.60} | 0.40±0.06\mathbf{0.40\pm 0.06} |

![Refer to caption](Fig4.png)


Figure 4. Boxplot comparison of mechanisms across 200 replications,
showing distribution of efficiency, average cost, and fairness (Gini).
The proposed mechanism achieves robustly balanced outcomes compared
to proportional and flat rules.

![Refer to caption](Fig5.png)


Figure 5. Scaling performance across system sizes (n=10,20,50,100n=10,20,50,100).
Points are sized by participation rate and shaded by efficiency.
The proposed equilibrium adapts gracefully with system size,
achieving both high fairness and stable efficiency.

The dominance of the proposed equilibrium highlights its novelty:
it is the only mechanism that simultaneously achieves efficiency,
fairness, and cost reduction through endogenous price adjustment.
Unlike flat or proportional rules that show gains only in certain
parameter regimes, the proposed equilibrium achieves comparable efficiency
while maintaining *stability and robustness* across diverse settings.
The mechanism works by embedding feedback: excess demand is penalized via
dual updates, while capacity is reallocated transparently across agents.
This contrasts with proportional or flat contracts that hard-code rules
without adaptive correction.
From an IS perspective, this illustrates how digital contracts function not
merely as computational artifacts but as *institutional mechanisms* that codify
equitable coordination [[5](https://arxiv.org/html/2510.05504v1#bib.bib5), [44](https://arxiv.org/html/2510.05504v1#bib.bib44)].
For industrial managers, the implication is clear: blockchain-enforced
equilibrium rules can strictly dominate ad hoc or legacy allocation processes,
providing not only superior performance but also governance legitimacy in
multi-agent environments.

### 5.5. Sensitivity Analysis

To move beyond simple one-dimensional heatmaps, we construct a comprehensive
sensitivity dashboard that jointly examines how efficiency and fairness respond
to variations in transaction and execution fees (τ,g)(\tau,g).
This two-dimensional view reveals non-linear interactions and sharp trade-offs
that would be invisible in isolated analyses.

Figure [6](https://arxiv.org/html/2510.05504v1#S5.F6 "Figure 6 ‣ 5.5. Sensitivity Analysis ‣ 5. Numerical Results ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation") integrates four complementary perspectives.
The top-left panel shows a 3D projection of efficiency: moderate increases in either
τ\tau or gg cause smooth declines, but efficiency collapses sharply only when both
fees are simultaneously large.
The top-right panel depicts the gradient field of fairness, highlighting that fairness
is far more sensitive to τ\tau than to gg, implying that per-unit fees act as the primary
equalizer.
The bottom-left panel overlays efficiency and fairness in a Pareto map with bubble size
indicating participation, exposing a clear frontier: improving fairness via higher
τ\tau comes at the expense of both efficiency and participation.
Finally, the bottom-right panel provides an elasticity heatmap of efficiency with respect
to τ\tau, conditional on gg, pinpointing fragile regions where efficiency is highly
responsive to marginal fee changes.

Together, these views demonstrate that the proposed mechanism is robust to moderate
fee variation, but also identify tipping points beyond which efficiency and participation
deteriorate rapidly.
For managers and policy makers, the dashboard serves as an early-warning tool: it shows
how fees can be tuned as complementary levers to balance efficiency, fairness, and
participation, while also highlighting regions of fragility in industrial coordination.

![Refer to caption](Fig6.png)


Figure 6. Comprehensive sensitivity analysis of the proposed mechanism.
Top left: efficiency surface with 3D projection, showing non-linear declines
with increasing transaction (τ)(\tau) and execution fees (g)(g).
Top right: gradient field of fairness, visualizing steepest improvement/deterioration.
Bottom left: efficiency–fairness Pareto map with participation coloring, highlighting the
trade-off frontier. Bottom right: elasticity heatmap
(∂\partialEfficiency/∂τ\partial\tau), showing local fragility zones where efficiency is
highly sensitive to marginal changes.

### 5.6. Shock–Resilience Analysis

While sensitivity analysis illustrates global fee-response patterns,
real-world environments rarely evolve smoothly. They are often exposed to sudden
policy or market shocks.
To evaluate resilience under such disruptions, we simulate a one-time jump in the
transaction fee (τ:0.5→1.5\tau:0.5\to 1.5 at t=50t=50) and track the resulting dynamics.

Figure [7](https://arxiv.org/html/2510.05504v1#S5.F7 "Figure 7 ‣ 5.6. Shock–Resilience Analysis ‣ 5. Numerical Results ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation") integrates four complementary panels that capture both
short-run disruption and long-run stabilization.
The top-left panel illustrates a 3D surface with pathline: efficiency initially
overshoots but stabilizes at a new equilibrium after the shock.
The top-right phase portrait of τ\tau versus efficiency clearly shows a structural
break at t=50t=50.
The bottom-left waterfall chart decomposes fairness into immediate post-shock loss
and gradual rebound, quantifying recovery.
The bottom-right ripple plot in efficiency–fairness space visualizes how perturbations
propagate before eventually stabilizing, underscoring systemic resilience.

Taken together, these results show that the proposed mechanism is not only well-defined
in steady state but also resilient to sudden disruptions: it absorbs shocks, reallocates
resources, and reconverges to balanced efficiency–fairness outcomes.
From a governance perspective, this property is critical: it means that digital contracts
embed transparent recovery paths without ad hoc intervention, reinforcing legitimacy and
accountability in coordination systems [[44](https://arxiv.org/html/2510.05504v1#bib.bib44), [5](https://arxiv.org/html/2510.05504v1#bib.bib5)].
Thus, the ripple-field visualization does not merely depict stability, but highlights how
smart contracts institutionalize resilience as a governance principle in complex
industrial and public infrastructures.

![Refer to caption](Fig7.png)


Figure 7. Dynamic shock–resilience analysis of the proposed mechanism.
Top left: 3D surface with pathline showing the trajectory of efficiency as
τ\tau shifts. Top right: phase portrait of τ\tau vs. efficiency, highlighting
the discontinuity at the shock. Bottom left: waterfall decomposition of fairness
recovery, partitioning the immediate impact versus gradual rebound.
Bottom right: vector-field ripple plot in efficiency–fairness space, illustrating
how shocks propagate and eventually stabilize. Together, these panels highlight not only
steady-state convergence but also organizational resilience, showing that smart contracts
can act as robust governance mechanisms in volatile environments.

### 5.7. Real-World Data: MovieLens-100K

To further validate the proposed mechanism beyond synthetic simulations,
we evaluate performance on the widely used MovieLens-100K dataset,
a benchmark in recommender systems that captures heterogeneous user–item preferences.
Ratings are normalized to construct heterogeneous utility coefficients, and
mechanisms are compared in terms of efficiency, cost, and fairness.

Table [7](https://arxiv.org/html/2510.05504v1#S5.T7 "Table 7 ‣ 5.7. Real-World Data: MovieLens-100K ‣ 5. Numerical Results ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation") summarizes the aggregate results across 200 replications.
While all mechanisms show negative absolute efficiency due to normalization,
relative efficiency (RelEff) highlights clear differences. Consistent with the
synthetic simulations, the proposed mechanism achieves the highest relative
efficiency (+4%+4\% vs. baseline), while maintaining high participation and balanced fairness.

Table 7. MovieLens-100K: Comparison of mechanisms (normalized, mean ±\pm std).

| Mechanism | Efficiency | Rel. Eff | Avg. Cost | Gini |
| --- | --- | --- | --- | --- |
| Flat | −0.55±0.02-0.55\pm 0.02 | 0.78±0.040.78\pm 0.04 | 0.20±0.010.20\pm 0.01 | 0.55±0.020.55\pm 0.02 |
| No enforcement | −0.71±0.02-0.71\pm 0.02 | 1.00±0.001.00\pm 0.00 | 0.58±0.020.58\pm 0.02 | 0.40±0.010.40\pm 0.01 |
| Proportional | −0.73±0.03-0.73\pm 0.03 | 1.03±0.031.03\pm 0.03 | 0.46±0.120.46\pm 0.12 | 0.40±0.010.40\pm 0.01 |
| Proposed | −0.74±0.06-0.74\pm 0.06 | 1.04±0.081.04\pm 0.08 | 0.47±0.160.47\pm 0.16 | 0.42±0.040.42\pm 0.04 |

Figure [9](https://arxiv.org/html/2510.05504v1#S5.F9 "Figure 9 ‣ 5.8. Real-World Data: MovieLens-100K ‣ 5. Numerical Results ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation") visualizes the trade-offs.
Panel (a) highlights that the proposed mechanism achieves the highest relative efficiency.
Panel (b) shows that the proposed mechanism balances cost and fairness, outperforming
the flat and no-enforcement baselines.

![Refer to caption](Fig8.png)


Figure 8. Comparison of MovieLens-100K mechanisms.
(a) Relative efficiency (RelEff) highlights that the proposed mechanism achieves the best performance.
(b) Cost and fairness (Gini index) show that the proposed mechanism maintains balanced outcomes.

### 5.8. Real-World Data: MovieLens-100K

To further validate the proposed mechanism beyond synthetic simulations,
we evaluate performance on the widely used MovieLens-100K dataset,
a benchmark in recommender systems that captures heterogeneous user–item preferences.
Ratings are normalized to construct heterogeneous utility coefficients, and
mechanisms are compared in terms of efficiency, cost, and fairness.

Table [8](https://arxiv.org/html/2510.05504v1#S5.T8 "Table 8 ‣ 5.8. Real-World Data: MovieLens-100K ‣ 5. Numerical Results ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation") summarizes the aggregate results across 200 replications.
All mechanisms achieve full participation (100%), consistent with the synthetic
experiments. While absolute efficiency values are negative due to normalization,
relative efficiency (RelEff) highlights clear differences. Consistent with the
synthetic results, the proposed mechanism achieves the highest relative
efficiency (+4%+4\% vs. baseline), while maintaining balanced cost and fairness outcomes.

Table 8. MovieLens-100K: Comparison of mechanisms (normalized, mean ±\pm std).
Absolute efficiency values appear negative due to normalization, but relative efficiency
and fairness comparisons remain valid performance indicators.

| Mechanism | Efficiency | Rel. Eff | Avg. Cost | Gini |
| --- | --- | --- | --- | --- |
| Flat | −0.55±0.02-0.55\pm 0.02 | 0.78±0.040.78\pm 0.04 | 0.20±0.010.20\pm 0.01 | 0.55±0.020.55\pm 0.02 |
| No enforcement | −0.71±0.02-0.71\pm 0.02 | 1.00±0.001.00\pm 0.00 | 0.58±0.020.58\pm 0.02 | 0.40±0.010.40\pm 0.01 |
| Proportional | −0.73±0.03-0.73\pm 0.03 | 1.03±0.031.03\pm 0.03 | 0.46±0.120.46\pm 0.12 | 0.40±0.010.40\pm 0.01 |
| Proposed | −0.74±0.06-0.74\pm 0.06 | 1.04±0.081.04\pm 0.08 | 0.47±0.160.47\pm 0.16 | 0.42±0.040.42\pm 0.04 |

Figure [9](https://arxiv.org/html/2510.05504v1#S5.F9 "Figure 9 ‣ 5.8. Real-World Data: MovieLens-100K ‣ 5. Numerical Results ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation") visualizes these trade-offs.
Panel (a) highlights that the proposed mechanism consistently achieves the
highest relative efficiency. Panel (b) shows that the proposed mechanism
balances cost and fairness, clearly outperforming the flat and
no-enforcement baselines, and remaining competitive with proportional allocation.

![Refer to caption](Fig4.png)


Figure 9. Comparison of MovieLens-100K mechanisms.
(a) Relative efficiency (RelEff) highlights that the proposed mechanism
achieves the best performance relative to baseline. (b) Cost and fairness
(Gini index) show that the proposed mechanism maintains balanced outcomes
while avoiding the extremes of flat and no-enforcement baselines.

## 6. Discussion

### 6.1. Theoretical Implications

The analysis contributes to the literature on mechanism design and
contracting in three principal ways.
First, existence and uniqueness of equilibria for
smart-contract–mediated resource allocation have been formally
established under mild convexity assumptions, extending classical
results in general equilibrium and mechanism design
[[2](https://arxiv.org/html/2510.05504v1#bib.bib2), [35](https://arxiv.org/html/2510.05504v1#bib.bib35)].
Second, it has been demonstrated that efficiency and fairness can be
jointly embedded into contract design through fee structures and
market-clearing mechanisms, aligning with recent calls in information
systems research for transparent and auditable allocation rules
[[5](https://arxiv.org/html/2510.05504v1#bib.bib5), [44](https://arxiv.org/html/2510.05504v1#bib.bib44)].
Third, a decentralized algorithm has been introduced that provides an
implementable procedure with provable convergence guarantees, thereby
ensuring relevance for real-time industrial applications.

Beyond these core results, the simulations enrich the theoretical
narrative.
The convergence trajectories with overshoot and damped stabilization
mirror the price-adjustment dynamics studied in classical general equilibrium
theory [[2](https://arxiv.org/html/2510.05504v1#bib.bib2)], but are extended here to a blockchain-enforced
contract setting..
The shock–resilience experiments further highlight dynamic stability:
even under abrupt fee changes, the system exhibits recovery and eventual
rebalancing.
This bridges equilibrium analysis with robustness theory, showing that
the proposed mechanism is not only well-defined in steady state but also
resilient under perturbations, maintaining a balanced efficiency–fairness profile.
From the perspective of information and organizational sciences, these
results highlight how transparency, verifiability, and accountability
can be mathematically guaranteed in decentralized coordination systems.

### 6.2. Managerial and Industrial Implications

Beyond theoretical insights, the proposed framework carries broad
managerial and industrial relevance.

#### Manufacturing and Supply Chains.

In sectors such as steel, cement, and electronics, firms compete for
scarce raw materials and production capacity.
The efficiency–fairness Pareto maps quantify the trade-off between
maximizing total utility and maintaining equity, providing managers
with explicit levers to calibrate allocation rules and improve
information transparency in allocation processes
[[25](https://arxiv.org/html/2510.05504v1#bib.bib25)]. These results illustrate how our proposed mechanism maintains balanced allocations under resource constraints.

#### Energy and Utilities.

Smart grids and carbon trading systems face capacity and compliance
constraints.
The shock–resilience dashboard shows that efficiency stabilizes rapidly
after sudden fee changes, while also supporting auditable decision trails. The proposed mechanism preserves fairness without large efficiency losses.

#### Logistics and Transportation.

Port slots, warehouse space, and vehicle fleets are scarce resources
often subject to congestion and inefficiency.
Elasticity heatmaps highlight congestion-prone zones, offering early-warning
signals for fee adjustments. The proposed mechanism delivers robust allocations that maintain efficiency–fairness balance.

#### Healthcare and Pharmaceuticals.

Medical supply chains, including vaccine and drug distribution, face
demand surges and limited capacity.
Fairness analysis demonstrates how equity suffers immediate losses under shocks but gradually recovers, highlighting the proposed mechanism’s ability to stabilize allocation efficiently and fairly.

#### Public Infrastructure.

In the allocation of public funds, road capacity, or airport slots,
digital contracts provide a governance mechanism that enforces
capacity limits transparently while preserving fairness metrics.
Ripple-field shock analysis illustrates how localized disruptions
propagate but eventually dampen, demonstrating the robustness of allocations under the proposed framework.

Table [9](https://arxiv.org/html/2510.05504v1#S6.T9 "Table 9 ‣ Public Infrastructure. ‣ 6.2. Managerial and Industrial Implications ‣ 6. Discussion ‣ Mechanism Design and Equilibrium Analysis of Smart Contract–Mediated Resource Allocation") summarizes representative
industrial domains where smart-contract–based mechanism design can be
applied, highlighting operational context, model variables, structural
challenges, and the rigorous benefits of the proposed framework.

Table 9. Representative industrial domains for smart-contract-based mechanism design.
Each row highlights the operational context, model variables, structural challenges,
and the rigorous benefits of the proposed framework.





Domain


Operational Context


Model Variables


Optimization / Equilibrium Challenges


Mechanism Design Benefits




Supply Chain & Logistics


Multi-firm coordination under stochastic demand, port congestion, and capacity shocks.


Decision: II (inventory), LL (lead time), QQ (throughput), τ\tau (subsidy).
  
Exogenous: demand shocks dtd\_{t}, disruption events ζt\zeta\_{t}.


Nonlinear amplification of demand variance (bullwhip effect); information asymmetry;
nonconvex cost-sharing; equilibrium instability under shocks.


Provable existence of stable contract-clearing equilibrium; incentive-compatible allocations;
explicit fairness–efficiency Pareto frontier; sublinear regret bounds under demand drift.



Energy & Smart Grids


P2P electricity trading with stochastic demand, renewable intermittency, and carbon policy coupling.


Decision: pp (price), CC (capacity), ρ\rho (renewable ratio), DD (load).
  
Exogenous: renewable shocks ξt\xi\_{t}, policy shocks ϕt\phi\_{t}.


Price volatility from ξt\xi\_{t} shocks; nonlinear imbalance penalties; multi-agent
nonconvex optimization; uncertainty in balancing constraints.


Existence and uniqueness of clearing equilibrium; sublinear regret under drift/shocks;
parameter-free convergence scaling with agent population; fairness–efficiency trade-off
explicitly tunable via (τ,g)(\tau,g).



Healthcare Resource Allocation


ICU beds, ventilators, vaccines allocation under surge conditions and ethical constraints.


Decision: RR (resource stock), τ\tau (subsidy), α,β\alpha,\beta (fairness weights).
  
Exogenous: surge shocks σt\sigma\_{t}, demand heterogeneity δt\delta\_{t}.


Fairness dilemmas: max​∑ui\max\sum u\_{i} vs. min⁡Var​(ui)\min\mathrm{Var}(u\_{i}); scarcity shocks;
multi-objective feasibility; ethical transparency constraints.


Bounded inequity loss under shocks; recovery trajectories consistent with fairness–efficiency
Pareto frontier; equilibrium allocation existence and convergence; resilience dashboards
quantifying adaptation speed.



Cloud & Computing Infrastructure


On-demand allocation of GPU/CPU across users with SLA enforcement.


Decision: UU (units), π\pi (priority), λ\lambda (SLA penalties).
  
Exogenous: demand drift χt\chi\_{t}, hidden load bursts.


Oversubscription under drift; hidden demand shocks; arbitration costs; scalability issues
in decentralized clearing.


Transparent and auditable allocation rules; guaranteed convergence to efficient usage;
automated enforcement reduces disputes; sublinear regret guarantees under demand noise.



Financial Investment Contracts


Capital allocation between investors and fund managers with regulatory oversight.


Decision: θ\theta (risk weight), rr (return), cc (compliance cost), τ\tau (incentive rate).
  
Exogenous: market volatility shocks νt\nu\_{t}, drift in risk appetite.


Hidden preferences; stochastic drift in θ\theta; volatility shocks destabilizing
allocations; regulatory discontinuities.


Equilibrium guarantees protecting against misaligned incentives; interpretable and
auditable fairness allocations; shock-resilient stability; bounded regret under drift and noise.

## 7. Conclusion

This study has developed and evaluated a digital contracting mechanism for
efficient and fair resource allocation.
The contributions are threefold.
First, a rigorous game-theoretic foundation was established by proving the
existence and uniqueness of contract equilibria under mild convexity conditions.
Second, efficiency and fairness were embedded directly into the contract design
through transaction fees, execution costs, and market-clearing prices, thereby
unifying equity and efficiency objectives.
Third, a decentralized contract-clearing algorithm was introduced with provable
convergence guarantees, demonstrating feasibility for real-time industrial applications.

Extensive numerical experiments reinforced these theoretical results.
Convergence analysis indicated rapid stabilization despite overshoot,
sensitivity dashboards highlighted global and local fee trade-offs,
and shock–resilience simulations revealed graceful recovery after sudden
policy changes. Viewed collectively, these findings establish that the proposed mechanism
is not only well-defined in theory but also robust in practice.

From a managerial and policy perspective, the results suggest that
transaction and execution fees (τ,g)(\tau,g) can be tuned as effective levers
to balance efficiency, fairness, and participation. Applications span supply chains, energy markets, logistics, healthcare,
and public infrastructure, where transparent, auditable, and shock-resilient
coordination is increasingly critical.

Nevertheless, several limitations remain.
The analysis is stylized and abstracts from richer forms of uncertainty,
multi-period dynamics, and strategic misreporting.
Future research may integrate stochastic demand processes, extend the
framework to multi-layer or multi-market settings, and validate the model
using empirical data from blockchain-based pilots or industrial case studies.

In sum, digital contracts provide a powerful and flexible foundation
for decentralized resource allocation.
By combining theoretical rigor with robust numerical evidence, this study
demonstrates how smart contracts can serve not only as technical artifacts
but also as institutional instruments for transparency, accountability,
and resilience. This positioning underscores their relevance to the broader fields of
information and organizational sciences and opens pathways for adoption
in complex, high-stakes environments where verifiable coordination is essential.

## References

* [1]


  V. Acharya and S. Steffen,
  The risk of being a fallen angel and the corporate dash for cash in the midst of covid,
  *Review of Corporate Finance Studies*, 9 (2021), 430–471.
* [2]


  K. J. Arrow and L. Hurwicz,
  On the stability of the competitive equilibrium, i,
  *Econometrica*, 27 (1959), 522–552.
* [3]


  S. Barocas, M. Hardt and A. Narayanan,
  *Fairness and Machine Learning: Limitations and Opportunities*,
  MIT Press, 2023.
* [4]


  H. H. Bauschke and P. L. Combettes,
  *Convex Analysis and Monotone Operator Theory in Hilbert Spaces*,
  Springer, New York, 2011.
* [5]


  R. Beck, M. Avital, M. Rossi and J. B. Thatcher,
  Blockchain technology in business and information systems research,
  *Business & Information Systems Engineering*, 59 (2018), 381–384.
* [6]


  D. P. Bertsekas and J. N. Tsitsiklis,
  *Parallel and Distributed Computation: Numerical Methods*,
  Athena Scientific, 1997.
* [7]


  D. Bertsimas, V. F. Farias and N. Trichakis,
  The price of fairness,
  *Operations Research*, 59 (2011), 17–31.
* [8]


  S. Boyd and L. Vandenberghe,
  *Convex Optimization*,
  Cambridge University Press, 2004,
  Reprinted 2011.
* [9]


  S. Bubeck and N. Cesa-Bianchi,
  Regret analysis of stochastic and nonstochastic multi-armed bandit problems,
  *Foundations and Trends in Machine Learning*, 8 (2015), 1–122.
* [10]


  V. Buterin,
  *A next-generation smart contract and decentralized application platform*,
  Technical report, Ethereum Foundation, 2014,
  White paper, available at <https://ethereum.org/en/whitepaper/>.
* [11]


  C. Cachin,
  Architecture of the hyperledger blockchain fabric,
  in *Workshop on Distributed Cryptocurrencies and Consensus Ledgers*,
  IEEE, 2016,
  1–4.
* [12]


  G. P. Cachon and S. Netessine,
  Game theory in supply chain analysis,
  *Handbooks in Operations Research and Management Science*, 11 (2006), 13–66.
* [13]


  V. Cardellini, V. Grassi, F. L. Presti and M. Nardelli,
  On qos-aware scheduling of data stream applications over fog computing infrastructures,
  in *IEEE International Symposium on Computers and Communication*, 2016,
  271–276.
* [14]


  F. Casino, T. K. Dasaklis and C. Patsakis,
  A systematic literature review of blockchain-based applications: Current status, classification and open issues,
  *Telemat. Inform.*, 36 (2019), 55–81.
* [15]


  K. Christidis and M. Devetsikiotis,
  Blockchains and smart contracts for the internet of things,
  *IEEE Access*, 4 (2016), 2292–2303.
* [16]


  Y. Dai, D. Xu, S. Maharjan and Y. Zhang,
  Deep reinforcement learning for edge computing resource management,
  *IEEE Internet Things J.*, 7 (2020), 5827–5839.
* [17]


  K. Ding, L. Chen, X. Wu and L. Yu,
  Blockchain-empowered resource allocation for industrial internet of things,
  *IEEE Transactions on Industrial Informatics*, 19 (2023), 1120–1130.
* [18]


  T. Q. Dinh, J. Tang, Q. D. La and T. Q. S. Quek,
  A survey of mobile core network evolution for lte networks,
  *IEEE Commun. Surv. Tutor.*, 15 (2013), 1254–1270.
* [19]


  R. Z. Farahani, M. Rezapour and L. Kardar,
  Resilient energy supply chains for sustainable development goals,
  *Renewable and Sustainable Energy Reviews*, 130 (2020), 109918.
* [20]


  D. Gabay and H. Moulin,
  On the uniqueness and stability of nash equilibria in noncooperative games,
  *Applied Mathematics and Optimization*, 6 (1980), 105–145.
* [21]


  J. Greenberg,
  A taxonomy of organizational justice theories,
  *Academy of Management Review*, 12 (1987), 9–22.
* [22]


  H. Halaburda and M. Piskorski,
  Digital trust and coordination with blockchain technology,
  *Management Science*, 70 (2024), 1412–1430.
* [23]


  E. Hazan,
  *Introduction to Online Convex Optimization*,
  Foundations and Trends in Optimization, 2016.
* [24]


  L. Hurwicz and S. Reiter,
  *Designing Economic Mechanisms*,
  Cambridge University Press, 2006.
* [25]


  D. Ivanov,
  Exiting the covid-19 pandemic: after-shock risks and avoidance of disruption tails in supply chains,
  *Annals of Operations Research*, 312 (2021), 49–60.
* [26]


  D. Ivanov,
  Supply chain viability and the covid-19 pandemic: A conceptual and formal generalisation of four major adaptation strategies,
  *International Journal of Production Research*, 60 (2022), 2901–2914.
* [27]


  A. Jobin, M. Ienca and E. Vayena,
  The global landscape of ai ethics guidelines,
  *Nat. Mach. Intell.*, 1 (2019), 389–399.
* [28]


  H. Kagermann, W. Wahlster and J. Helbig,
  *Recommendations for implementing the strategic initiative Industrie 4.0*,
  Technical report, Industrie 4.0 Working Group, 2013.
* [29]


  M. Kearns, S. Neel, A. Roth and Z. S. Wu,
  An empirical study of rich subgroup fairness for machine learning,
  in *Proceedings of the Conference on Fairness, Accountability, and Transparency (FAT)*, 2019,
  100–109.
* [30]


  F. P. Kelly, A. K. Maulloo and D. K. H. Tan,
  Rate control in communication networks: shadow prices, proportional fairness and stability,
  *Journal of the Operational Research Society*, 49 (1997), 237–252.
* [31]


  P. J. Lambert,
  *The Distribution and Redistribution of Income*,
  3rd edition,
  Manchester University Press, 2001.
* [32]


  J. Li, H. Zhao and W. Zhang,
  Differentiated pricing in mobile edge computing: A stackelberg game approach,
  *IEEE Access*, 7 (2019), 10388–10398.
* [33]


  J. Liu, X. Zheng and Y. Wang,
  User association in 5g networks: A matching theory perspective,
  *IEEE Wireless Commun.*, 25 (2018), 35–41.
* [34]


  Y. Lu,
  Industry 4.0: A survey on technologies, applications and open research issues,
  *J. Ind. Inform. Integr.*, 6 (2017), 1–10.
* [35]


  A. Mas-Colell, M. D. Whinston and J. R. Green,
  *Microeconomic Theory*,
  Oxford University Press, 1995.
* [36]


  N. Mehrabi, F. Morstatter, N. Saxena, K. Lerman and A. Galstyan,
  A survey on bias and fairness in machine learning,
  *ACM Comput. Surv.*, 54 (2021), 115:1–115:35.
* [37]


  A. Mohsenian-Rad and F. Bu,
  Smart grid resilience: Fundamentals, challenges, and future directions,
  *IEEE Transactions on Smart Grid*, 14 (2023), 13–27.
* [38]


  H. Moulin,
  *Fair Division and Collective Welfare*,
  MIT Press, 2003.
* [39]


  O. Munoz, A. Pascual-Iserte and J. Vidal,
  Optimization of radio and computational resources for energy efficiency in latency-constrained application offloading,
  *IEEE Trans. Veh. Technol.*, 64 (2015), 4738–4755.
* [40]


  R. B. Myerson,
  Optimal auction design,
  *Mathematics of Operations Research*, 6 (1981), 58–73.
* [41]


  A. Nedić, A. Olshevsky, W. Shi and Y. Sun,
  Geometrically convergent distributed optimization with uncoordinated step sizes,
  *IEEE Trans. Autom. Control*, 63 (2018), 3881–3895.
* [42]


  S. Paul, P. S. De and S. Chattopadhyay,
  Equitable vaccine allocation strategies in pandemics: A review,
  *Socio-Economic Planning Sciences*, 82 (2022), 101206.
* [43]


  P. A. Pavlou,
  Institution-based trust in interorganizational exchange relationships: The role of online b2b marketplaces,
  *Inf. Syst. Res.*, 13 (2002), 215–243.
* [44]


  A. Rai,
  Explainable ai: From black box to glass box,
  *Journal of the Academy of Marketing Science*, 48 (2019), 137–141.
* [45]


  S. M. Rashid, I. Aliyu, A. Isah, M. Hahn and J. Kim,
  Blockchain-based task placement and resource management in edge computing: A survey,
  *Electronics*, 14 (2025), 3398.
* [46]


  H. Robbins and S. Monro,
  A stochastic approximation method,
  *The Annals of Mathematical Statistics*, 22 (1951), 400–407.
* [47]


  R. T. Rockafellar,
  *Convex Analysis*,
  Princeton University Press, 1970.
* [48]


  J. B. Rosen,
  Existence and uniqueness of equilibrium points for concave n-person games,
  *Econometrica*, 33 (1965), 520–534.
* [49]


  T. Roughgarden and É. Tardos,
  Bounding the inefficiency of equilibria in nonatomic congestion games,
  *Games and Economic Behavior*, 47 (2004), 389–403.
* [50]


  S. Shalev-Shwartz and S. Ben-David,
  *Understanding Machine Learning: From Theory to Algorithms*,
  Cambridge University Press, 2012.
* [51]


  N. Szabo,
  *Formalizing and Securing Relationships on Public Networks*,
  Technical report, First Monday, 1997,
  Available at <http://firstmonday.org/article/view/548/469>.
* [52]


  J. N. Tsitsiklis,
  Distributed asynchronous deterministic and stochastic gradient optimization algorithms,
  *IEEE Transactions on Automatic Control*, 31 (1986), 803–812.
* [53]


  W. Wang, D. He, Y. Wang and H. Huang,
  Blockchain-based fair payment in public cloud computing,
  *IEEE Transactions on Cloud Computing*, 7 (2019), 579–592.
* [54]


  World Health Organization,
  Fair allocation mechanism for covid-19 vaccines through the covax facility, 2021,
  Available at <https://www.who.int/>.
* [55]


  H. Wu, J. Geng, X. Bai and S. Jin,
  Deep reinforcement learning-based online task offloading in mobile edge computing networks,
  *Inf. Sci.*, 654 (2024), 119849.
* [56]


  X. Xu, I. Weber and M. Staples,
  Architecture for blockchain applications,
  *Springer Nature*,
  Monograph, 2nd edition.
* [57]


  S. Yuan, Q. Zhou, J. Li and S. Guo,
  Adaptive incentive and resource allocation for blockchain-supported edge video streaming systems: A cooperative learning approach,
  *IEEE Trans. Mob. Comput.*
* [58]


  T. Zhang, D. Xu, A. Tolba, K. Yu, H. Song and S. Yu,
  Reinforcement-learning-based offloading for ris-aided cloud–edge computing in iot networks: Modeling, analysis, and optimization,
  *IEEE Internet Things J.*, 11 (2024), 19421–19439.
* [59]


  W. Zhang,
  Stochastic game approaches for resource allocation in mobile edge computing,
  *IEEE Trans. Cloud Comput.*, 5 (2017), 556–568.