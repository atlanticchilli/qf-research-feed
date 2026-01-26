---
authors:
- Elisa Botteghi
- Martino S. Centonze
- Davide Pastorello
- Daniele Tantari
doc_id: arxiv:2601.16805v1
family_id: arxiv:2601.16805
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Network Security under Heterogeneous Cyber-Risk Profiles and Contagion
url_abs: http://arxiv.org/abs/2601.16805v1
url_html: https://arxiv.org/html/2601.16805v1
venue: arXiv q-fin
version: 1
year: 2026
---


Elisa Botteghi
  
Martino Centonze
  
Davide Pastorello
  
Daniele Tantari

###### Abstract

Cyber risk has become a critical financial threat in today’s interconnected digital economy. This paper introduces a cyber-risk management framework for networked digital systems that combines the strategic behavior of players with contagion dynamics within a security game. We address the problem of optimally allocating cybersecurity resources across a network, focusing on the heterogeneous valuations of nodes by attackers and defenders, some areas may be of high interest to the attacker, while others are prioritized by the defender. We explore how this asymmetry drives attack and defense strategies and shapes the system’s overall resilience. We extend a method to determine optimal resource allocation based on simple network metrics weighted by the defender’s and attacker’s risk profiles. We further propose risk measures based on contagion paths and analyze how propagation dynamics influence optimal defense strategies. Numerical experiments explore risk versus cost efficient frontiers varying network topologies and risk profiles, revealing patterns of resource allocation and cyber deception effects. These findings provide actionable insights for designing resilient digital infrastructures and mitigating systemic cyber risk.

## 1 Introduction

Cyber risk refers to the potential for damage to digital systems and infrastructure, whether in terms of functionality or data integrity, resulting from security breaches.

In today’s digital economy, cyber risk is inherently a financial risk. Firstly, cyber-attacks translates into financial losses because operational disruptions and data breaches directly impact assets of economic value [[15](https://arxiv.org/html/2601.16805v1#bib.bib46 "What are the actual costs of cyber risk events?")]: operability itself has financial worth, and data are increasingly treated as valuable commodities. Secondly, modern financial systems are tightly interwoven with digital infrastructures—commonly referred to as cyber-physical systems—where a cyber infection at the digital layer can escalate into the financial domain, potentially propagating across institutions and triggering systemic instability [[14](https://arxiv.org/html/2601.16805v1#bib.bib32 "Pirates without borders: the propagation of cyberattacks through firms’ supply chains"), [26](https://arxiv.org/html/2601.16805v1#bib.bib33 "The anatomy of cyber risk")].
For example, [[30](https://arxiv.org/html/2601.16805v1#bib.bib24 "Cyberattacks and financial stability: evidence from a natural experiment"), [31](https://arxiv.org/html/2601.16805v1#bib.bib25 "The propagation of cyberattacks through the financial system: evidence from an actual event")] document cases in which cyberattacks targeting technology service providers, such as digital payment platforms, led to liquidity crises within interbank networks. Additional spillover effects include adverse stock market reactions and reputational damage following cyber incidents. [[12](https://arxiv.org/html/2601.16805v1#bib.bib45 "A review of the economic costs of cyber incidents"), [22](https://arxiv.org/html/2601.16805v1#bib.bib29 "An event study analysis of the economic impact of it operational risk and its subcategories"), [45](https://arxiv.org/html/2601.16805v1#bib.bib31 "Informed trading in the options market surrounding data breaches"), [4](https://arxiv.org/html/2601.16805v1#bib.bib26 "Do firms underreport information on cyber-attacks? evidence from capital markets"), [25](https://arxiv.org/html/2601.16805v1#bib.bib30 "Cyberattacks and impact on bond valuation"), [3](https://arxiv.org/html/2601.16805v1#bib.bib27 "Hacking corporate reputations")]. As a result, effective cyber-risk management and strategic investment in cybersecurity are essential not only for digital resilience but also for the broader stability of financial systems.

As digital ecosystems become increasingly complex, the need to manage large amounts of data has led to infrastructures that are typically organized as networks of interconnected servers or units. While such interconnectivity enhances efficiency, scalability, and redundancy, it also introduces systemic vulnerabilities: a single breach can act as a gateway for contagion, allowing malicious activity to propagate and potentially compromise the entire system.

In this work, we propose a cyber risk management framework for digital networked systems, designed to identify an optimal investment strategy for allocating cybersecurity defenses across network nodes. The core components of our model include contagion across the network and the strategic behavior of cyber attacks.

For the first component, we draw inspiration from the extensive literature on complex networks [[42](https://arxiv.org/html/2601.16805v1#bib.bib39 "Networks"), [51](https://arxiv.org/html/2601.16805v1#bib.bib40 "Exploring complex networks"), [34](https://arxiv.org/html/2601.16805v1#bib.bib41 "Complex networks: principles, methods and applications")]. Complex network models of contagion have been widely applied to biological [[44](https://arxiv.org/html/2601.16805v1#bib.bib43 "Epidemic processes in complex networks"), [13](https://arxiv.org/html/2601.16805v1#bib.bib44 "Complex networks: structure, robustness and function")], social [[41](https://arxiv.org/html/2601.16805v1#bib.bib38 "Theory of rumour spreading in complex social networks"), [21](https://arxiv.org/html/2601.16805v1#bib.bib42 "Generalization of epidemic theory")], and financial systems [[19](https://arxiv.org/html/2601.16805v1#bib.bib37 "Contagion in financial networks"), [2](https://arxiv.org/html/2601.16805v1#bib.bib36 "Systemic risk and stability in financial networks"), [9](https://arxiv.org/html/2601.16805v1#bib.bib34 "Network models of financial systemic risk: a review"), [10](https://arxiv.org/html/2601.16805v1#bib.bib35 "Contingent convertible bonds in financial networks")], where the propagation of shocks or behaviors is mediated by the structure of interactions among agents.
Typically, these models assume that the initial trigger—be it the zero-patient of an epidemic, a financial shock, or a rumor—is exogenous and random, reflecting events that are unintentional and difficult to predict or control.

However, this assumption does not hold in the context of cybersecurity, where attacks are often strategic and targeted. To address this, we adopt a game-theoretic framework, building on the literature of security games [[52](https://arxiv.org/html/2601.16805v1#bib.bib56 "Security and game theory: algorithms, deployed systems, lessons learned"), [47](https://arxiv.org/html/2601.16805v1#bib.bib48 "A survey of game theory as applied to network security"), [36](https://arxiv.org/html/2601.16805v1#bib.bib47 "Game theory for network security"), [39](https://arxiv.org/html/2601.16805v1#bib.bib49 "Game theory meets network security and privacy")], which explicitly models the adversarial nature of cyber threats and the strategic allocation of defenses.

In particular, two players Stackelberg security games [[49](https://arxiv.org/html/2601.16805v1#bib.bib13 "Stackelberg security games: looking beyond a decade of success")]-in which a defender (leader) commits to a defensive strategy and an attacker (follower) responds accordingly- have received significant interest due to their wide range of applications including patrolling tasks [[48](https://arxiv.org/html/2601.16805v1#bib.bib50 "Protect: a deployed game theoretic system to protect the ports of the united states"), [8](https://arxiv.org/html/2601.16805v1#bib.bib51 "Leader-follower strategies for robotic patrolling in environments with arbitrary topologies"), [46](https://arxiv.org/html/2601.16805v1#bib.bib52 "Deployed armor protection: the application of a game theoretic model for security at the los angeles international airport")], environmental protection efforts [[17](https://arxiv.org/html/2601.16805v1#bib.bib53 "When security games go green: designing defender strategies to prevent poaching and illegal fishing."), [16](https://arxiv.org/html/2601.16805v1#bib.bib54 "Green security games: apply game theory to addressing green security challenges")] and defense coordination [[20](https://arxiv.org/html/2601.16805v1#bib.bib55 "Defense coordination in security games: equilibrium analysis and mechanism design"), [27](https://arxiv.org/html/2601.16805v1#bib.bib57 "Defender (mis) coordination in security games")]. Within this framework, security games that incorporate interdependencies among nodes—where insufficient protection of one node can undermine the defense of its neighbors—have been studied in [[38](https://arxiv.org/html/2601.16805v1#bib.bib63 "Multidefender security games"), [11](https://arxiv.org/html/2601.16805v1#bib.bib64 "Interdependent defense games with applications to internet security at the level of autonomous systems"), [35](https://arxiv.org/html/2601.16805v1#bib.bib65 "Defending with shared resources on a network")]. Multi-step attacks propagating through the system have been extensively studied using the formalism of attack graphs [[28](https://arxiv.org/html/2601.16805v1#bib.bib66 "Scalable min-max multi-objective cyber-security optimisation over probabilistic attack graphs"), [57](https://arxiv.org/html/2601.16805v1#bib.bib67 "Keep spending: beyond optimal cyber-security investment")].

Models that explicitly account for contagion phenomena, where threats propagate across the network, have been also examined in [[5](https://arxiv.org/html/2601.16805v1#bib.bib59 "Inoculation strategies for victims of viruses and the sum-of-squares partition problem"), [33](https://arxiv.org/html/2601.16805v1#bib.bib61 "Existence theorems and approximation algorithms for generalized network security games"), [1](https://arxiv.org/html/2601.16805v1#bib.bib1 "Network security and contagion"), [53](https://arxiv.org/html/2601.16805v1#bib.bib58 "Security games for controlling contagion"), [7](https://arxiv.org/html/2601.16805v1#bib.bib4 "Stackelberg security games with contagious attacks on a network: reallocation to the rescue"), [6](https://arxiv.org/html/2601.16805v1#bib.bib60 "Contagion and observability in security domains"), [23](https://arxiv.org/html/2601.16805v1#bib.bib62 "Attack, defence, and contagion in networks")]. Most of these models, still grounded in an epidemiological view of contagion, assume that the attacker’s objective is simply to maximize the spread of infection across the network. However, in cybersecurity settings, the attacker may instead aim to reach specific nodes or regions considered strategic or of higher value. Similarly, the defender may prioritize the protection of critical nodes while allowing others to be sacrificed.

In our work, building on the contagion mechanism of [[5](https://arxiv.org/html/2601.16805v1#bib.bib59 "Inoculation strategies for victims of viruses and the sum-of-squares partition problem"), [1](https://arxiv.org/html/2601.16805v1#bib.bib1 "Network security and contagion")], we therefore consider a heterogeneous network in which both attacker and defender assign values to each node and a corresponding target risk. The attacker and defender may assign different value/risk profiles to the nodes, reflecting their asymmetric information and differing perspectives on the system’s structure and strategic importance. The two players compete within a security game with limited budget: the defender strategically allocates cybersecurity resources across the network nodes, while the attacker determines an optimal probability distribution over potential targets.

The main contributions of this paper are organized as follows. In Section [2](https://arxiv.org/html/2601.16805v1#S2 "2 Model ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion"), we introduce the general setting. Section [2.1](https://arxiv.org/html/2601.16805v1#S2.SS1 "2.1 Contagion on Networks ‣ 2 Model ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion") defines the static contagion mechanism adopted. In Section [2.2](https://arxiv.org/html/2601.16805v1#S2.SS2 "2.2 Security Game Framework ‣ 2 Model ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion"), we present the security game framework, including the attacker’s and defender’s value/risk profiles. Section [2.3](https://arxiv.org/html/2601.16805v1#S2.SS3 "2.3 Stackelberg Equilibrium ‣ 2 Model ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion") recalls the Stackelberg formulation of the game and the corresponding definition of Strong Stackelberg Equilibria.

Section [3](https://arxiv.org/html/2601.16805v1#S3 "3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion") outlines the main analytical results. In Section [3.1](https://arxiv.org/html/2601.16805v1#S3.SS1 "3.1 Asymptotic Equilibrium and Emerging Network metrics ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion"), we provide a characterization of the Stackelberg equilibrium based on intuitive and naturally emerging network metrics. These metrics quantify the extent to which each node contributes to the overall protection of the system and are combined in a principled way according to the players’ respective risk profiles. Section [3.2](https://arxiv.org/html/2601.16805v1#S3.SS2 "3.2 Paths of contagion and scalable solutions ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion") introduces a class of risk measures defined in terms of the number of contagion paths, allowing for the inclusion of a dynamic parameter linked to propagation time.

Section [4](https://arxiv.org/html/2601.16805v1#S4 "4 Numerical results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion") discusses the numerical results. In Section [4.1](https://arxiv.org/html/2601.16805v1#S4.SS1 "4.1 Efficient frontier ‣ 4 Numerical results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion"), we use the efficient frontier to compare the overall system robustness to strategic attacks across different network topologies and risk profiles. Section [4.2](https://arxiv.org/html/2601.16805v1#S4.SS2 "4.2 Cyber-deception strategy effects ‣ 4 Numerical results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion") analyzes examples of optimal resource allocation patterns, with a focus on the emergence of cyber deception effects. In Section [4.3](https://arxiv.org/html/2601.16805v1#S4.SS3 "4.3 Contagion Dynamics ‣ 4 Numerical results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion"), we examine the robustness of the optimal strategies to model misspecifications across a range of different dynamic contagion mechanisms.

Finally, Section [Conclusions](https://arxiv.org/html/2601.16805v1#Sx1 "Conclusions ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion") presents the conclusions and outlines future research directions. The proof of the main theorem is provided in Appendix [5](https://arxiv.org/html/2601.16805v1#S5 "5 Appendix A: Proof of Theorem 3.1 ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").

## 2 Model

### 2.1 Contagion on Networks

Let us consider an undirected network 𝒢\mathcal{G} of nn interconnected nodes represented by its adjacency matrix 𝐀=(Ai​j)i<jn\mathbf{A}=(A\_{ij})\_{i<j}^{n}, Ai​j∈{0,1}A\_{ij}\in\{0,1\}, i,j=1,…,ni,j=1,\ldots,n. Each entry Ai​jA\_{ij} encodes the presence (Ai​j=1A\_{ij}=1) or absence (Ai​j=0A\_{ij}=0) of a link between the pair of nodes (i,j)(i,j).

Each node ss can be the target of a cyber-threat with a probability ϕs∈[0,1]\phi\_{s}\in[0,1], becoming the seed of a potential infection. Therefore, the cyber-attack distribution is represented by the vector ϕ=(ϕi)i=1n\bm{\phi}=(\phi\_{i})\_{i=1}^{n}, ∑i=1nϕi=1\sum\_{i=1}^{n}\phi\_{i}=1.

Nodes can be either immune or susceptible to cyber-attacks. We introduce the susceptibility vector 𝑿=(Xi)i=1n\bm{X}=(X\_{i})\_{i=1}^{n}, where each Xi∈{0,1}X\_{i}\in\{0,1\} indicates whether node ii is susceptible (Xi=1X\_{i}=1) or immune (Xi=0X\_{i}=0) to a cyber-threat. We model 𝑿\bm{X} as a random vector of independent Bernoulli variables, with ℙ​(Xi=0)=qi\mathbb{P}(X\_{i}=0)=q\_{i} and ℙ​(Xi=1)=1−qi\mathbb{P}(X\_{i}=1)=1-q\_{i}, where qi∈[0,1]q\_{i}\in[0,1]. The vector 𝒒=(qi)i=1n\bm{q}=(q\_{i})\_{i=1}^{n} represents the security level of the system, with qiq\_{i} denoting the security level of node ii. The vector 𝒒\bm{q} reflects how cybersecurity investments have been distributed across the network.

All model stochasticity is encoded in the probability space defined by the set of elementary events (s,𝑿)∈ℕn×{0,1}n=:Ω(s,\bm{X})\in\mathbb{N}\_{n}\times\{0,1\}^{n}=:\Omega together with the joint probability distribution

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(s,𝑿):=ϕs​∏i=1n(1−qi)Xi​qi1−Xi,p(s,\bm{X}):=\phi\_{s}\prod\_{i=1}^{n}(1-q\_{i})^{X\_{i}}q\_{i}^{1-X\_{i}}, |  | (1) |

where we assume that the seed location and the susceptibilities are independent random variables.

A security breach at a node poses a threat to its neighbors, potentially allowing a cyber-infection to spread throughout the entire system, starting from the initial seed. Since the infection propagates only through susceptible nodes, any susceptible node that is connected to the seed via a path consisting entirely of susceptible nodes will become infected. Alternatively, we can define the transmission network 𝒯​(𝑿)\mathcal{T}(\bm{X}) as the (random) sub-network of 𝒢\mathcal{G} consisting only of susceptible nodes. Then, a node ii becomes infected if and only if it belongs to the same connected component as the seed ss in the transmission network, i.e. if there exists a path i∼si\sim s between ii and ss entirely in 𝒯​(𝑿)\mathcal{T}(\bm{X}). The infection condition can be simply expressed by the following

###### Definition 1(Infected nodes)

Given a realization of the random vector 𝑿\bm{X} and a seed ss, a node ii is said to become infected if there exists ℓ∈ℕ\ell\in\mathbb{N} such that

|  |  |  |
| --- | --- | --- |
|  | (𝑨∘𝑿​𝑿T)i​sℓ≥1,\left(\bm{A}\circ\bm{X}\bm{X}^{T}\right)^{\ell}\_{is}\geq 1, |  |

where ∘\circ denotes the element-wise (Hadamard) product, i.e., (𝑨∘𝑿​𝑿T)i​j=Ai​j​Xi​Xj\left(\bm{A}\circ\bm{X}\bm{X}^{T}\right)\_{ij}=A\_{ij}X\_{i}X\_{j}.

Let us stress that 𝑨∘𝑿​𝑿T\bm{A}\circ\bm{X}\bm{X}^{T} is the adjacency matrix of 𝒯​(𝑿)\mathcal{T}(\bm{X}) so (𝑨∘𝑿​𝑿T)i​sℓ\left(\bm{A}\circ\bm{X}\bm{X}^{T}\right)^{\ell}\_{is} is the number of paths of length ll from ss to ii in 𝒯​(𝑿)\mathcal{T}(\bm{X}).
Note that the previous definition is entirely static, as it does not involve any specification of contagion dynamics or propagation time. Nonetheless, it can be interpreted as the asymptotic infection condition of any contagion dynamics—deterministic or stochastic—that propagates through the network links and that does not allow infected nodes to recover.

×\bm{\times}×\bm{\times}

×\bm{\times}


Figure 1: Representation of the contagion process. Left panel: a realization of the network showing susceptible nodes (orange) and immune nodes (blue) before the attack; Right panel: after the attack all the susceptible nodes connected to the seed become infected (red). Strategically placed immune nodes can block the spread and protect other susceptible nodes from infection.

### 2.2 Security Game Framework

On top of this environment we consider a two players extensive game involving an attacker and a defender. The attacker optimizes the cyber-attack distribution vector ϕ\bm{\phi}, strategically selecting the nodes where it is most advantageous to pose a threat. The defender allocates cyber defenses across the network by adjusting the system’s security vector 𝒒\bm{q}, aiming to identify an optimal cybersecurity investment strategy. Therefore, we refer to 𝒒\bm{q} and ϕ\bm{\phi} as defender and attacker strategies respectively.

The attacker’s utility function 𝒰a\mathcal{U}\_{a} and the defender’s loss function ℒd\mathcal{L}\_{d}, which are to be optimized, are defined with the following risk/cost structure:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒰a​(ϕ;𝒒)\displaystyle\mathcal{U}\_{a}(\bm{\phi};\bm{q}) | =∑inηi​ℛi​(q→,ϕ→;𝑨)−θ​𝒞a​(ϕ→),\displaystyle=\sum\_{i}^{n}\eta\_{i}\mathcal{R}\_{i}(\vec{q},\vec{\phi};\bm{A})-\theta\ \mathcal{C}\_{a}(\vec{\phi}), |  | (2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℒd​(q→;ϕ→)\displaystyle\mathcal{L}\_{d}(\vec{q};\vec{\phi}) | =∑inzi​ℛi​(q→,ϕ→;𝑨)+α​𝒞d​(q→).\displaystyle=\sum\_{i}^{n}z\_{i}\mathcal{R}\_{i}(\vec{q},\vec{\phi};\bm{A})+\alpha\ \mathcal{C}\_{d}(\vec{q}). |  | (3) |

The strategy costs incurred by the attacker and the defender are denoted by 𝒞a​(ϕ)\mathcal{C}\_{a}(\bm{\phi}) and 𝒞d​(𝒒)\mathcal{C}\_{d}(\bm{q}), respectively. While 𝒞d​(𝒒)\mathcal{C}\_{d}(\bm{q}) concretely measures the size of investments in cyber defenses, 𝒞a​(ϕ)\mathcal{C}\_{a}(\bm{\phi}) has to be interpreted more as an information cost that penalizes low entropy attacking strategies concentrated on a limited subset of nodes. In the following, we assume either quadratic cost functions of the form 𝒞d​(𝒒)=12​∑i=1nqi2\mathcal{C}\_{d}(\bm{q})=\frac{1}{2}\sum\_{i=1}^{n}q\_{i}^{2} and 𝒞a​(ϕ)=12​∑i=1nϕi2\mathcal{C}\_{a}(\bm{\phi})=\frac{1}{2}\sum\_{i=1}^{n}\phi\_{i}^{2}, for analytical tractability, or alternatively L1L^{1}-type penalizations to promote strategy sparsity. The hyperparameters α\alpha and θ\theta control the relative weight assigned to the cost terms and can be interpreted as Lagrange multipliers in a constrained optimization framework, where the attacker and the defender operate under limited budget constraints.

The vector 𝓡=(ℛi)i=1n\bm{\mathcal{R}}=(\mathcal{R}\_{i})\_{i=1}^{n} in ([2](https://arxiv.org/html/2601.16805v1#S2.E2 "In 2.2 Security Game Framework ‣ 2 Model ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion")−[3](https://arxiv.org/html/2601.16805v1#S2.E3 "In 2.2 Security Game Framework ‣ 2 Model ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion"))(\ref{eq:utility}-\ref{eq:loss}) measures the infection risk at each node, as a function of both the network structure 𝑨\bm{A} and the strategies adopted by the two players (𝒒,ϕ)(\bm{q},\bm{\phi}), thereby defining the system’s risk profile. In the following, we analyze two distinct risk measures: the first is based on the actual probability of a node being infected, while the second relies on the expected number of paths connecting the node to the infection seed. The former enhances the interpretability of the optimal solution, whereas the latter improves its scalability.

Most models addressing contagion dynamics on complex networks are inspired by epidemiological frameworks. They often tacitly assume that the attacker’s objective, either explicitly or as a natural consequence of viral replication, is to maximize damage to the network, merely intended as the overall size of the infection. In a cybersecurity context, a networked system is a heterogeneous collection of assets with varying levels of value. Consequently, each node contributes differently to the overall damage assessment. Moreover, the attacker and the defender may assign different values to the same node, either due to conflicting preferences or because of an information asymmetry between the node’s actual value and the attacker’s perceived value. For this reason, we introduced in ([2](https://arxiv.org/html/2601.16805v1#S2.E2 "In 2.2 Security Game Framework ‣ 2 Model ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion")−[3](https://arxiv.org/html/2601.16805v1#S2.E3 "In 2.2 Security Game Framework ‣ 2 Model ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion"))(\ref{eq:utility}-\ref{eq:loss}) the value profiles 𝜼=(ηi)i=1n,𝒛=(zi)i=1n∈ℝn\bm{\eta}=(\eta\_{i})\_{i=1}^{n},\bm{z}=(z\_{i})\_{i=1}^{n}\in\mathbb{R}^{n} to model the perceived importance of different nodes or regions of the network for the attacker and the defender, respectively. For example one may consider the case of uniform value profiles
𝜼=𝒛=𝟏\bm{\eta}=\bm{z}=\bm{1},
up to the extreme scenario where the profiles are maximally concentrated on single highly strategic nodes, i.e.
𝜼=𝒆i\bm{\eta}=\bm{e}\_{i}, 𝒛=𝒆k\bm{z}=\bm{e}\_{k} for some i,k=1,…,ni,k=1,\ldots,n. As before, 𝜼\bm{\eta} and 𝒛\bm{z} can be interpreted as Lagrange multipliers in a constrained optimization problem in which the two players operate targeting a given heterogeneous risk profile.

### 2.3 Stackelberg Equilibrium

An extensive game with perfect information is a model for sequential decision-making in which players act in a prescribed order and have complete knowledge of all previous actions taken by others. In particular, we consider a Stackelberg extensive game, where the defender moves first (leader) and the attacker makes their decision accordingly (follower).

In this setup, while the defender’ s strategy is defined by the choice of an action q∈Sd⊆[0,1]n\textbf{q}\in S\_{d}\subseteq[0,1]^{n}, the attacker’s strategy is determined by a response function

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ:Sd∋q→ϕ​(q)∈Sa,\phi:S\_{d}\ni\textbf{q}\rightarrow\phi(\textbf{q})\in S\_{a}, |  | (4) |

that assigns an action to any possible choice of the defender, where we denoted as Sa⊆[0,1]nS\_{a}\subseteq[0,1]^{n} the set of cyber-attack probability distributions over nn nodes. We denote the set of possible response functions as RaR\_{a}.

The proposed ordering is natural in our interpretation of the defender’s action as a cyber-security investment — placing defenses and enhancing system resilience in anticipation of potential future attacks. Conversely, the opposite ordering would be more appropriate to model scenarios in which the defender, reacting to an attack that has already occurred, actively executes a defensive strategy to block it or mitigate its impact on the system. Although not addressed in the present paper, there are several situations in which it is worthwhile to consider a Stackelberg formulation where the attacker moves first. For example in the case of a ransomwere attack through the network, the defender reacts by isolating compromised nodes or restoring data from backup [[55](https://arxiv.org/html/2601.16805v1#bib.bib21 "Deterrence, backup, or insurance: game-theoretic modeling of ransomware")]. In computer networks, after a data exfiltration attack, the defender reacts blocking nodes or filtering the suspicious traffic acting on links [[43](https://arxiv.org/html/2601.16805v1#bib.bib22 "A stackelberg game model for botnet data exfiltration")]. In the context of dynamic resource allocation, after a distributed denial-of-service moved saturating the network resources, the defender reacts reallocating resources [[37](https://arxiv.org/html/2601.16805v1#bib.bib20 "Stackelberg dynamic game-based resource allocation in threat defense for internet of things")]. Even cyber kill chain can be an example of Stackelberg attacker-first framework: the attacker starts with the first move sending malicious messages through network channels then the defender responds with countermeasures over the network such as blocking suspicious domains [[32](https://arxiv.org/html/2601.16805v1#bib.bib23 "Modelling cybersecurity strategies with game theory and cyber kill chain")].

In a Stackelberg extensive game, a natural definition for an optimal pair of strategies (𝒒∗,ϕ∗​(⋅))(\bm{q}^{\*},\bm{\phi}^{\*}(\cdot)) is given by the following

###### Definition 2(Strong Stackelberg equilibrium SSE)

In a Stackelberg game with utility functions 𝒰d\mathcal{U}\_{d} and ℒd\mathcal{L}\_{d}, a pair of strategies (q∗,ϕ∗​(⋅))(\textbf{q}^{\*},\bm{\phi}^{\*}(\cdot)), where q∗∈Sd\textbf{q}^{\*}\in S\_{d} is the defender’s strategy and Ra∋ϕ∗:Sd→SaR\_{a}\ni\bm{\phi}^{\*}:S\_{d}\rightarrow S\_{a} is the attacker’s response function, is a strong Stackelberg equilibrium (SSE) if:

1. 1.

   The attacker plays a best response in each subgame:

   |  |  |  |
   | --- | --- | --- |
   |  | 𝒰a​(ϕ∗​(q);q)≥𝒰a​(ϕ​(q);q),∀q∈Sd,∀ϕ∈Ra;\mathcal{U}\_{a}(\bm{\phi}^{\*}(\textbf{q});\textbf{q})\geq\mathcal{U}\_{a}(\bm{\phi}(\textbf{q});\textbf{q}),\ \ \ \forall\textbf{q}\in S\_{d},\forall\bm{\phi}\in R\_{a}; |  |
2. 2.

   The defender plays a best response:

   |  |  |  |
   | --- | --- | --- |
   |  | ℒd​(q∗;ϕ∗​(q∗))≤ℒd​(q;ϕ∗​(q)),∀q∈Sd;\mathcal{L}\_{d}(\textbf{q}^{\*};\bm{\phi}^{\*}(\textbf{q}^{\*}))\leq\mathcal{L}\_{d}(\textbf{q};\bm{\phi}^{\*}(\textbf{q})),\ \ \ \ \forall\textbf{q}\in S\_{d};\ \ \ \ \ \ \ \ \ \ \ \ |  |
3. 3.

   The attacker breaks ties optimality for the defender:

   |  |  |  |
   | --- | --- | --- |
   |  | ℒd​(q,ϕ∗​(q))≤ℒd​(q,𝒇∗),∀q∈Sd,𝒇∗∈Saq,\mathcal{L}\_{d}(\textbf{q},\bm{\phi}^{\*}(\textbf{q}))\leq\mathcal{L}\_{d}(\textbf{q},\bm{f}^{\*}),\ \ \ \ \ \forall\textbf{q}\in S\_{d},\bm{f}^{\*}\in S^{\textbf{q}}\_{a}, |  |

where we denoted SaqS^{\textbf{q}}\_{a} as the set of the attacker best responses to q, i.e.
Saq={𝒇∗∈Sa:𝒇∗=arg​maxϕ∈Sa⁡𝒰a​(ϕ;q)}.S^{\textbf{q}}\_{a}=\{\bm{f}^{\*}\in S\_{a}\,:\,\bm{f}^{\*}=\text{arg}\max\_{\bm{\phi}\in S\_{a}}\mathcal{U}\_{a}(\bm{\phi};\textbf{q})\}.

By definition, a Strong Stackelberg Equilibrium (SSE) is always a subgame perfect equilibrium [[18](https://arxiv.org/html/2601.16805v1#bib.bib16 "A course in game theory")] due to conditions 1 and 2. In the presence of multiple equilibria, given by the existence of multiple best response functions, condition 3 serves to select a subset of them. In general the Nash equilibrium of a two players strategic game differs from the SSE of the corresponding Stackelberg version of the game, meaning that the moves’ order is crucial [[29](https://arxiv.org/html/2601.16805v1#bib.bib15 "Stackelberg vs. nash in security games: an extended investigation of interchangeability, equivalence, and uniqueness")].

## 3 Results

### 3.1 Asymptotic Equilibrium and Emerging Network metrics

Let us define the risk measure of a node ℛi\mathcal{R}\_{i} as the probability that the node ii becomes infected, i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛi​(q,ϕ;𝑨):=ℙi​(q,ϕ;𝑨),\mathcal{R}\_{i}(\textbf{q},\bm{\phi};\bm{A}):=\mathbb{P}\_{i}(\textbf{q},\bm{\phi};\bm{A}), |  | (5) |

where

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | ℙi​(q,ϕ;𝑨)\displaystyle\mathbb{P}\_{i}(\textbf{q},\bm{\phi};\bm{A}) | :=\displaystyle:= | 𝔼𝑿,s​[𝕀​(i∼s∈𝒯​(𝑿))]\displaystyle\mathbb{E}\_{\bm{X},s}\left[\mathbb{I}\left(i\sim s\in\mathcal{T}(\bm{X})\right)\right] |  | (6) |
|  |  | =\displaystyle= | ∑s=1nϕs​𝔼𝑿​[𝕀​(i∼s∈𝒯​(𝑿))],\displaystyle\sum\_{s=1}^{n}\phi\_{s}\ \mathbb{E}\_{\bm{X}}\left[\mathbb{I}\left(i\sim s\in\mathcal{T}(\bm{X})\right)\right], |  |

and 𝕀​(⋅)\mathbb{I}(\cdot) denotes the indicator function of a set. The expression i∼s∈𝒯​(𝑿)i\sim s\in\mathcal{T}(\bm{X}) represents the event that node ii is connected to the seed node ss within the transmission subnetwork of susceptible nodes 𝒯​(𝑿)\mathcal{T}(\bm{X}), as in Definition [1](https://arxiv.org/html/2601.16805v1#Thmdefinition1 "Definition 1(Infected nodes) ‣ 2.1 Contagion on Networks ‣ 2 Model ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").

In this context, the optimal security investment q∗\textbf{q}^{\*} corresponding to a Strong Stackelberg Equilibrium (SSE) of the security game can be characterized using simple network metrics, which describe each node’s vulnerability based on its position within the network topology. Let us define the 11-point and 22-points network protection metrics as follows.

###### Definition 3(11-point protection)

Let 𝒢\mathcal{G} be a network of nn nodes. The 11-point protection is defined as the tensor 𝒑1={ai​kj}i,j,k=1n∈{0,1}n3\bm{p}^{1}=\{a^{j}\_{ik}\}\_{i,j,k=1}^{n}\in\{0,1\}^{n^{3}}, where each entry ai​kja^{j}\_{ik} is given by

|  |  |  |
| --- | --- | --- |
|  | ai​kj={1if ​i∼k​ in ​𝒢​ and ​i≁k​ in ​𝒢∖{j},0otherwise,a^{j}\_{ik}=\begin{cases}1&\text{if }i\sim k\text{ in }\mathcal{G}\text{ and }i\not\sim k\text{ in }\mathcal{G}\setminus\{j\},\\ 0&\text{otherwise},\end{cases} |  |

and 𝒢∖{j}\mathcal{G}\setminus\{j\} denotes the sub-network obtained by removing node jj from 𝒢\mathcal{G}. We define ai​ij=0a\_{ii}^{j}=0, ∀i≠j\forall i\neq j, and ai​jj=1a\_{ij}^{j}=1.

The 11-point protection encodes whether the removal of a single node jj can disrupt the connectivity between a pair of nodes (i,k)(i,k), initially connected, potentially blocking the spread of an infection between them. For example, in the network shown in Fig. [2](https://arxiv.org/html/2601.16805v1#S3.F2 "Figure 2 ‣ 3.1 Asymptotic Equilibrium and Emerging Network metrics ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion"), the potential contagion between nodes 33 and 66 can be prevented by removing (or immunizing) either node 55, so that a365=1a^{5}\_{36}=1, or node 11, resulting in a361=1a^{1}\_{36}=1. From the 11-point protection tensor, given two vectors 𝒗,𝒘∈ℝn\bm{v},\bm{w}\in\mathbb{R}^{n}, we define its weighted reductions as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | aij​(𝒗)\displaystyle a\_{i}^{j}(\bm{v}) | :=∑k=1nai​kj​vk=∑k=1nak​ij​vk\displaystyle:=\sum\_{k=1}^{n}a\_{ik}^{j}v\_{k}=\sum\_{k=1}^{n}a\_{ki}^{j}v\_{k} |  | (7) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ai​(𝒗,𝒘)\displaystyle a^{i}(\bm{v},\bm{w}) | :=∑j,k=1naj​ki​vj​wk=∑knaki​(𝒗)​wk=∑jnaji​(𝒘)​vj,\displaystyle:=\sum\_{j,k=1}^{n}a\_{jk}^{i}v\_{j}w\_{k}=\sum\_{k}^{n}a\_{k}^{i}(\bm{v})w\_{k}=\sum\_{j}^{n}a\_{j}^{i}(\bm{w})v\_{j}, |  | (8) |

where we used that ai​kj=ak​ija^{j}\_{ik}=a^{j}\_{ki} that also implies ai​(𝒗,𝒘)=ai​(𝒘,𝒗)a^{i}(\bm{v},\bm{w})=a^{i}(\bm{w},\bm{v}).

###### Definition 4(22-points protection)

Let 𝒢\mathcal{G} be a network of nn nodes. The 22-point protection is defined as the tensor 𝒑2={bk​s(i,j)}i,j,k,t=1n∈{0,1}n4\bm{p}^{2}=\{b^{(i,j)}\_{ks}\}\_{i,j,k,t=1}^{n}\in\{0,1\}^{n^{4}}, where each entry bk​s(i,j)b^{(i,j)}\_{ks} is given by

|  |  |  |
| --- | --- | --- |
|  | bk​s(i,j)={1if​k∼s​ in ​𝒢,ak​si=ak​sj=0,k≁s​ in ​𝒢∖{i,j},0otherwise,b^{(i,j)}\_{ks}=\begin{cases}1&\text{if}\ k\sim s\text{ in }\mathcal{G}\ ,\ a^{i}\_{ks}=a^{j}\_{ks}=0\ ,\ \ k\not\sim s\text{ in }\mathcal{G}\setminus\{i,j\},\\ 0&\text{otherwise},\end{cases} |  |

where ak​sja^{j}\_{ks} denotes the entries of the 11-point protection tensor 𝒑1\bm{p}^{1} of 𝒢\mathcal{G}, and 𝒢∖{i,j}\mathcal{G}\setminus\{i,j\} is the sub-network obtained by removing both nodes ii and jj from 𝒢\mathcal{G}.

Unlike the 11-point protection, the 22-point protection captures whether the simultaneous removal of a pair of nodes (i,j)(i,j) can disrupt the connectivity between another pair of nodes (k,s)(k,s), initially connected, in cases where the removal of either ii or jj alone is insufficient to cause such disruption. For example, in the network shown in Fig. [2](https://arxiv.org/html/2601.16805v1#S3.F2 "Figure 2 ‣ 3.1 Asymptotic Equilibrium and Emerging Network metrics ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion"), the removal (or immunization) of either node 22 or node 44 alone is not sufficient to prevent the potential contagion between nodes 33 and 66—that is, a362=a364=0a^{2}\_{36}=a^{4}\_{36}=0. However, the simultaneous removal of both nodes (2,4)(2,4) successfully blocks the connection, and thus b36(2,4)=1b^{(2,4)}\_{36}=1. For a given pair of vectors 𝒗,𝒘∈ℝn\bm{v},\bm{w}\in\mathbb{R}^{n}, we define

|  |  |  |  |
| --- | --- | --- | --- |
|  | bi​j​(𝒗,𝒘):=(1−δi​j)​∑k,s(bk​s(i,j)−ak​si​ak​sj)​vk​ws.b\_{ij}(\bm{v},\bm{w}):=(1-\delta\_{ij})\sum\_{k,s}\left(b^{(i,j)}\_{ks}-a^{i}\_{ks}a^{j}\_{ks}\right)v\_{k}w\_{s}. |  | (9) |

1234×\bm{\times}5

61×\times23×\times45

6


Figure 2: Illustration of 11- and 22-point protection in a network. The potential contagion between nodes 33 and 66 can be prevented by removing (or immunizing) either node 55 (left panel), so that a365=1a^{5}\_{36}=1, or node 11, resulting in a361=1a^{1}\_{36}=1. In contrast, the removal of either node 22 or node 44 alone is not sufficient to block the contagion—i.e., a362=a364=0a^{2}\_{36}=a^{4}\_{36}=0—but their simultaneous removal (right panel) successfully disrupts the connection, yielding b36(2,4)=1b^{(2,4)}\_{36}=1.

The 11- and 22-point protection metrics identify the most strategic and cost-effective locations in the network where a potential infection can be locally blocked. Since they rely on the removal (or immunization) of only one or two nodes, these metrics suggest defense strategies that are both targeted and resource-efficient. As such, they provide actionable guidance on where to concentrate cyber defense efforts and allocate investments.

However, many other approaches exist to assess node importance in terms of system vulnerability and contagion prevention. For instance the previous framework could be generalized to define kk-point protection for arbitrary values of kk, allowing for the study of more complex cooperative defense strategies involving multiple nodes.
Moreover, centrality-based measures—such as degree, betweenness, closeness, and k-core—have long been used to identify influential nodes [[50](https://arxiv.org/html/2601.16805v1#bib.bib17 "Identifying influential nodes in complex contagion mechanism")], and recent work has proposed multi-attribute decision-making methods that integrate several structural indicators to provide a more comprehensive assessment [[56](https://arxiv.org/html/2601.16805v1#bib.bib18 "Multi-attribute decision making method for node importance metric in complex network")]. What makes the 11- and 22-point protection metrics particularly relevant is that they emerge naturally from the analysis of Stackelberg equilibria in the security game introduced in this work. In fact, it holds the following

###### Theorem 3.1(Asymptotic SSE)

Consider a security Stackelberg game with contagion on a network 𝒢\mathcal{G} of nn nodes, defined by the attacker utility 𝒰a\mathcal{U}\_{a} ([2](https://arxiv.org/html/2601.16805v1#S2.E2 "In 2.2 Security Game Framework ‣ 2 Model ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion")), the defender loss ℒd\mathcal{L}\_{d} ([3](https://arxiv.org/html/2601.16805v1#S2.E3 "In 2.2 Security Game Framework ‣ 2 Model ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion")), a risk profile 𝓡\bm{\mathcal{R}} as in ([5](https://arxiv.org/html/2601.16805v1#S3.E5 "In 3.1 Asymptotic Equilibrium and Emerging Network metrics ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion")), and quadratic cost functions. If θ\theta is sufficiently large, a SSE security investment satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | q∗∼α(α​𝕀−𝑴)−1​𝒔,\textbf{q}^{\*}\sim^{\alpha}\left(\alpha\mathbb{I}-\bm{M}\right)^{-1}\bm{s}, |  | (10) |

where 𝐌=𝐌​(𝐳,𝛈;𝐩1,𝐩2)∈ℝn×n\bm{M}=\bm{M}(\bm{z},\bm{\eta};\bm{p}^{1},\bm{p}^{2})\in\mathbb{R}^{n\times n} and 𝐬=𝐬​(𝐳,𝛈;𝐩1,𝐩2)∈ℝn\bm{s}=\bm{s}(\bm{z},\bm{\eta};\bm{p}^{1},\bm{p}^{2})\in\mathbb{R}^{n} are defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | si​(𝒛,𝜼;𝒑1,𝒑2)\displaystyle s^{i}(\bm{z},\bm{\eta};\bm{p}^{1},\bm{p}^{2}) | :=ai​(𝟏/n,𝒛),\displaystyle:=a^{i}(\bm{1}/n,\bm{z}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Mi​j​(𝒛,𝜼;𝒑1,𝒑2)\displaystyle M\_{ij}(\bm{z},\bm{\eta};\bm{p}^{1},\bm{p}^{2}) | :=bi​j​(𝟏/n,𝒛)\displaystyle:=b\_{ij}(\bm{1}/n,\bm{z}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −1θ​∑k=1n(aki​(𝜼)​akj​(𝒛)−ai​(𝟏/n,𝜼)​aj​(𝟏/n,𝒛))\displaystyle-\frac{1}{\theta}\sum\_{k=1}^{n}\left(a^{i}\_{k}(\bm{\eta})a^{j}\_{k}(\bm{z})-a^{i}(\bm{1}/n,\bm{\eta})a^{j}(\bm{1}/n,\bm{z})\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −1θ​∑k=1n(aki​(𝒛)​akj​(𝜼)−ai​(𝟏/n,𝒛)​aj​(𝟏/n,𝜼))\displaystyle-\frac{1}{\theta}\sum\_{k=1}^{n}\left(a^{i}\_{k}(\bm{z})a^{j}\_{k}(\bm{\eta})-a^{i}(\bm{1}/n,\bm{z})a^{j}(\bm{1}/n,\bm{\eta})\right) |  | (11) |

The notation 𝐚∼α𝐛\bm{a}\sim^{\alpha}\bm{b} indicates that ‖𝐚−𝐛‖=o​(1/α2)\|\bm{a}-\bm{b}\|=o(1/\alpha^{2}) as α→∞\alpha\to\infty.

The proof of Theorem [3.1](https://arxiv.org/html/2601.16805v1#S3.Thmtheorem1 "Theorem 3.1(Asymptotic SSE) ‣ 3.1 Asymptotic Equilibrium and Emerging Network metrics ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion") is provided in Appendix [5](https://arxiv.org/html/2601.16805v1#S5 "5 Appendix A: Proof of Theorem 3.1 ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion") and builds upon a generalization of the results presented in [[1](https://arxiv.org/html/2601.16805v1#bib.bib1 "Network security and contagion")]. Theorem [3.1](https://arxiv.org/html/2601.16805v1#S3.Thmtheorem1 "Theorem 3.1(Asymptotic SSE) ‣ 3.1 Asymptotic Equilibrium and Emerging Network metrics ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion") offers an explicit approximation of the defender’s optimal cyber investment strategy, which becomes asymptotically exact in the limit α→∞\alpha\to\infty. This corresponds to a scenario in which the cost function dominates the optimization, and can therefore be interpreted as a low-budget regime for the defender. In fact, Eq. ([10](https://arxiv.org/html/2601.16805v1#S3.E10 "In Theorem 3.1(Asymptotic SSE) ‣ 3.1 Asymptotic Equilibrium and Emerging Network metrics ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion")) can be expanded as

|  |  |  |  |
| --- | --- | --- | --- |
|  | q∗=1α​𝒔+1α2​𝑴​𝒔+o​(1α2),\textbf{q}^{\*}=\frac{1}{\alpha}\bm{s}+\frac{1}{\alpha^{2}}\bm{M}\bm{s}+o\left(\frac{1}{\alpha^{2}}\right), |  | (12) |

indicating a vanishing optimal investment as α→∞\alpha\to\infty.

A key feature of this approximation is its dependence on the network topology solely through the network-based metric tensors 𝒑1\bm{p}^{1} and 𝒑2\bm{p}^{2}, which naturally emerge from the structure of the game and are combined properly according to the value profiles 𝒛\bm{z} and 𝜼\bm{\eta}.

Theorem [3.1](https://arxiv.org/html/2601.16805v1#S3.Thmtheorem1 "Theorem 3.1(Asymptotic SSE) ‣ 3.1 Asymptotic Equilibrium and Emerging Network metrics ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion") extends the results of [[1](https://arxiv.org/html/2601.16805v1#bib.bib1 "Network security and contagion")], which are recovered as special cases. For instance, in the limit as θ→∞\theta\to\infty, the utility function reduces to the cost 𝒞a​(ϕ)\mathcal{C}\_{a}(\bm{\phi}), compelling the attacker to adopt a uniform strategy ϕ∗=𝟏/n=(1/n,…,1/n)\bm{\phi}^{\*}=\bm{1}/n=(1/n,\ldots,1/n). In this regime, the problem simplifies to the social optimum under random, non-strategic attacks, as studied in [[1](https://arxiv.org/html/2601.16805v1#bib.bib1 "Network security and contagion")] for 𝒛=𝟏\bm{z}=\bm{1}.
Another special case arises by setting 𝒛=𝒆i\bm{z}=\bm{e}\_{i} and 𝜼=𝟏/n\bm{\eta}=\bm{1}/n. Under these conditions, we obtain aki​(𝒛)=ai​(𝟏/n,𝒛)=1a^{i}\_{k}(\bm{z})=a^{i}(\bm{1}/n,\bm{z})=1, and bi​j​(𝟏/n,𝒛)=−(1−δi​j)​aij​(𝟏/n)b\_{ij}(\bm{1}/n,\bm{z})=-(1-\delta\_{ij})a^{j}\_{i}(\bm{1}/n). Consequently, the matrix MM becomes

|  |  |  |
| --- | --- | --- |
|  | Mi​j=−(1−δi​j)​aij​(𝟏/n)−1θ​∑kaki​(𝟏/n)​(ai​kj−aij​(𝟏/n)),M\_{ij}=-(1-\delta\_{ij})a^{j}\_{i}(\bm{1}/n)-\frac{1}{\theta}\sum\_{k}a^{i}\_{k}(\bm{1}/n)(a^{j}\_{ik}-a^{j}\_{i}(\bm{1}/n)), |  |

which characterizes the Nash equilibrium under uniform strategic attack, as analyzed in [[1](https://arxiv.org/html/2601.16805v1#bib.bib1 "Network security and contagion")], where each node in the network acts as an individual player minimizing its own infection probability. Again in the limit as θ→∞\theta\to\infty we recover the Nash equilibrium under random uniform attack.

### 3.2 Paths of contagion and scalable solutions

The analytical expression provided by Theorem [3.1](https://arxiv.org/html/2601.16805v1#S3.Thmtheorem1 "Theorem 3.1(Asymptotic SSE) ‣ 3.1 Asymptotic Equilibrium and Emerging Network metrics ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion") offers a good approximation of the optimal investment in the small-budget regime. Nevertheless, it can serve as a benchmark strategy across a broader range of scenarios. Its main advantage lies in its computational simplicity, as it avoids solving the full optimization problem, which typically requires a costly numerical search for the true SSE.

The core challenge lies in computing the risk profile 𝓡\bm{\mathcal{R}} as in  ([5](https://arxiv.org/html/2601.16805v1#S3.E5 "In 3.1 Asymptotic Equilibrium and Emerging Network metrics ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion")), which in turn determines the utility and loss functions to be optimized. Introducing the random variable

|  |  |  |  |
| --- | --- | --- | --- |
|  | NiL​(s,𝑿;𝑨)=Card\displaystyle N^{L}\_{i}(s,\bm{X};\bm{A})=\mathrm{Card} | ({(i1=i,i2,…,iℓ=s)|Aik​ik+1=1,Xik=1,\displaystyle\left(\left\{(i\_{1}=i,i\_{2},\ldots,i\_{\ell}=s)\,\middle|\,A\_{i\_{k}i\_{k+1}}=1,\;X\_{i\_{k}}=1,\;\right.\right. |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ik∈ℕn,k∈ℕℓ−1,ℓ≤L})\displaystyle\quad\left.\left.i\_{k}\in\mathbb{N}\_{n},\;k\in\mathbb{N}\_{\ell-1},\;\ell\leq L\right\}\right) |  | (13) |

as the number of different paths of maximum length LL connecting a node ii to the seed ss in the transmission subnetwork 𝒯​(𝑿)\mathcal{T}(\bm{X}) of susceptible nodes, the infection probability can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙi​(q,ϕ;𝑨)\displaystyle\mathbb{P}\_{i}(\textbf{q},\bm{\phi};\bm{A}) | =𝔼𝑿,s​[𝕀​(i∼s∈𝒯​(𝑿))]\displaystyle=\mathbb{E}\_{\bm{X},s}\left[\mathbb{I}\left(i\sim s\in\mathcal{T}(\bm{X})\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼𝑿,s​[limL→∞Θ​(NiL​(s,𝑿;𝑨)−1)],\displaystyle=\mathbb{E}\_{\bm{X},s}\left[\lim\_{L\to\infty}\Theta\left(N^{L}\_{i}(s,\bm{X};\bm{A})-1\right)\right], |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =limL→∞𝔼𝑿,s​[Θ​(NiL​(s,𝑿;𝑨)−1)],\displaystyle=\lim\_{L\to\infty}\mathbb{E}\_{\bm{X},s}\left[\Theta\left(N^{L}\_{i}(s,\bm{X};\bm{A})-1\right)\right], |  | (14) |

where Θ​(⋅)\Theta(\cdot) denotes the Heaviside step function which returns one if the argument is greater than zero, i.e. NiL≥1N^{L}\_{i}\geq 1, and zero otherwise. In the second line of Eq. [3.2](https://arxiv.org/html/2601.16805v1#S3.Ex13 "3.2 Paths of contagion and scalable solutions ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion") we exploit the fact that, for a given i∈ℕni\in\mathbb{N}\_{n}, the sequence of random variables (Θ​(NiL−1))L≥0(\Theta(N^{L}\_{i}-1))\_{L\geq 0} converges pointwise to 𝕀​(i∼s∈𝒯​(𝑿))\mathbb{I}\left(i\sim s\in\mathcal{T}(\bm{X})\right). Intuitively, a node ii is connected to the seed in 𝒯​(𝑿)\mathcal{T}(\bm{X}) if there exists at least a path, of arbitrary large length LL, linking them. In the last line, the application of the dominated convergence theorem justifies the exchange of limit and expectation.
Following the definition of NiL​(s,𝑿;𝑨)N^{L}\_{i}(s,\bm{X};\bm{A}), let us observe that the parameter LL is not only a technical cut-off but admits a natural interpretation as propagation time. In fact, a path of length LL can be regarded as a sequence of LL successive transmissions of the infection through the network to which we can associate a unit of time. In this sense, the path length directly corresponds to the time required for the contagion to travel from the seed to another node. Considering paths of length at most LL is therefore equivalent to assuming that the infection can propagate only within a finite time interval. While, in the limit L→∞L\rightarrow\infty, the model recovers the regime in which the contagion has unlimited time to diffuse. In this sense, LL can be understood as the infection propagation time, which equips the model with an explicit dynamical dimension.

The form of Eq. [3.2](https://arxiv.org/html/2601.16805v1#S3.Ex13 "3.2 Paths of contagion and scalable solutions ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion") suggests the introduction of an entire class of risk measure defined in terms of a pair (f,L)(f,L) as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℛi(f,L)​(q,ϕ;𝑨)\displaystyle\mathcal{R}^{(f,L)}\_{i}(\textbf{q},\bm{\phi};\bm{A}) | =𝔼𝑿,s​[f​(NiL​(s,𝑿;𝑨))],\displaystyle=\mathbb{E}\_{\bm{X},s}\left[f\left(N^{L}\_{i}(s,\bm{X};\bm{A})\right)\right], |  | (15) |

where ff is an arbitrary non-decreasing activation function. If ff is bounded one can also consider the limit ℛif=limL→∞ℛi(f,L)\mathcal{R}\_{i}^{f}=\lim\_{L\to\infty}\mathcal{R}\_{i}^{(f,L)}.

In general, if the activation function ff is non linear, the expected value cannot be computed explicitly and must instead be evaluated numerically. The computational cost of this operation grows exponentially with the network size nn. Conversely, if we consider a linear activation function, then the risk is expressed as the expected number of paths from the node to the seed, i.e.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℛiL​(q,ϕ;𝑨)\displaystyle\mathcal{R}^{L}\_{i}(\textbf{q},\bm{\phi};\bm{A}) | =𝔼𝑿,s​[NiL​(s,𝑿;𝑨)]=𝔼𝑿,s​[∑ℓ=1L(𝑨∘𝑿​𝑿T)i​sℓ]\displaystyle=\mathbb{E}\_{\bm{X},s}\left[N^{L}\_{i}(s,\bm{X};\bm{A})\right]=\mathbb{E}\_{\bm{X},s}\left[\sum\_{\ell=1}^{L}\left(\bm{A}\circ\bm{X}\bm{X}^{T}\right)^{\ell}\_{is}\right] |  | (16) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼𝑿,s​[∑ℓ=1L∑i2,…,iℓ−1=1nAi​i2​Ai2​i3​⋯​Aiℓ−1​s​Xi​Xi2​⋯​Xiℓ−1​Xs]\displaystyle=\mathbb{E}\_{\bm{X},s}\left[\sum\_{\ell=1}^{L}\sum\_{i\_{2},\ldots,i\_{\ell-1}=1}^{n}A\_{ii\_{2}}A\_{i\_{2}i\_{3}}\cdots A\_{i\_{\ell-1}s}X\_{i}X\_{i\_{2}}\cdots X\_{i\_{\ell-1}}X\_{s}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑ℓ=1L∑i2,…,iℓ−1,s=1nϕs​Ai​i2​Ai2​i3​⋯​Aiℓ−1​s​∏k∈{i,i2,…,iℓ−1,s}(1)(1−qk),\displaystyle=\sum\_{\ell=1}^{L}\sum\_{i\_{2},\ldots,i\_{\ell-1},s=1}^{n}\phi\_{s}A\_{ii\_{2}}A\_{i\_{2}i\_{3}}\cdots A\_{i\_{\ell-1}s}\prod\_{k\in\{i,i\_{2},\ldots,i\_{\ell-1,s}\}^{(1)}}(1-q\_{k}), |  |

where we denoted with I(1)I^{(1)} the set of distinct occurrences of a set II.
This quantity can be computed as efficiently as a matrix multiplication. Empirically, we observe that the results exhibit very low sensitivity to the cut-off parameter LL. Therefore one can simply solve the optimization problem with 𝓡=𝓡L\bm{\mathcal{R}}=\bm{\mathcal{R}}^{L} with very small LL to obtain optimal strategies that scale efficiently to large systems.

## 4 Numerical results

### 4.1 Efficient frontier

For any given defender and attacker value profiles 𝒛\bm{z} and 𝜼\bm{\eta}, the optimal defender strategy at the Stackelberg equilibrium provides a quantitative measure of the vulnerability associated with a specific network topology. This insight can be leveraged to guide the selection of system architectures that offer greater robustness.

Inspired by the classical Markowitz portfolio selection theory [[40](https://arxiv.org/html/2601.16805v1#bib.bib19 "Portfolio selection, the journal of finance. 7 (1)")], we assess the robustness of different network topologies by computing the efficient frontier of the problem. Specifically, we scatter plot the system’s global risk at equilibrium,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛ∗​(α;𝑨):=∑i=1nzi​ℛi​(q∗​(α;𝑨),ϕ⋆​(q∗​(α;𝑨));𝑨),\mathcal{R}^{\*}(\alpha;\bm{A}):=\sum\_{i=1}^{n}z\_{i}\,\mathcal{R}\_{i}\left(\textbf{q}^{\*}(\alpha;\bm{A}),\,\phi^{\star}\left(\textbf{q}^{\*}(\alpha;\bm{A})\right);\,\bm{A}\right), |  | (17) |

highlighting its dependence on the network topology 𝑨\bm{A}, against the corresponding defender’s cost at equilibrium,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞d∗​(α;𝑨):=𝒞d​(q∗​(α;𝑨)),\mathcal{C}^{\*}\_{d}(\alpha;\bm{A}):=\mathcal{C}\_{d}\left(\textbf{q}^{\*}(\alpha;\bm{A})\right), |  | (18) |

for varying values of the Lagrange multiplier α\alpha. The resulting risk–cost plot illustrates the trade-off between investment and security: it shows the minimum cost the defender must incur to achieve a given level of system risk, or equivalently, the minimum achievable risk for a given admissible cost (i.e., the defender’s budget). The security performance of different network topologies can thus be evaluated by comparing their respective efficient frontiers. The efficient frontier also serves as a powerful tool to compare the impact of different value profiles—that is, different attacker targeting regions and defender protection priorities—on a fixed system topology. By varying the allocation of value across nodes, we can assess how the equilibrium risk–cost trade-off shifts, providing insight into which regions of the network are most critical to secure under different threat scenarios.

![Refer to caption](x1.png)

![Refer to caption](x2.png)

![Refer to caption](x3.png)

Figure 3: Efficient frontiers for a tree network with 121 nodes, branching ratio 33, and 44
levels, are shown for different defender’s value profile and attack distribution 𝒛\bm{z}, ϕ\bm{\phi} concentrated on specific levels of the tree. Colors distinguish the different levels targeted by the attacker (see inset of the Left Panel). Each panel corresponds to a different defender’s value profile, aiming to protect respectively the root (Left Panel), the first level (Central Panel), and the second level of the tree (Right Panel).

Fig. [3](https://arxiv.org/html/2601.16805v1#S4.F3 "Figure 3 ‣ 4.1 Efficient frontier ‣ 4 Numerical results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion") illustrates the efficient frontiers for a tree-structured network consisting of 121121 nodes organized across four levels, with a branching ratio of 33. The risk measure used is the infection probability ([5](https://arxiv.org/html/2601.16805v1#S3.E5 "In 3.1 Asymptotic Equilibrium and Emerging Network metrics ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion")) and costs are quadratic. We consider different value profiles 𝒛\bm{z} and attack distribution ϕ\bm{\phi}, each targeting a distinct level of the tree—from the root, i.e. 𝒛,ϕ=(1,0,…,0)\bm{z},\bm{\phi}=(1,0,\ldots,0), to intermediate levels such as 𝒛,ϕ=(0,1/3,1/3,1/3,0,…,0)\bm{z},\bm{\phi}=(0,1/3,1/3,1/3,0,\ldots,0), and finally to the leaves, i.e. 𝒛,ϕ=(0,…,1/81,…,1/81)\bm{z},\bm{\phi}=(0,\ldots,1/81,\ldots,1/81). One can observe that, it generally appears easier for the defender to protect levels that are closer to the root, as the efficiency frontiers tend to rise with the distance from the root in the defender’s value profile. However, the systemic risk is strongly affected by the attack distribution. In particular, the system appears less vulnerable when the attack start from inner levels than the one deemed most important by the defender. The reason is that a smaller subset of nodes must be immunized in order to prevent infection spread. In contrast, when the attack originates from peripheral levels, the risk vanishes once the defender’s budget is sufficient to immunize all nodes within the level of interest, regardless of the level targeted by the attacker.

![Refer to caption](x4.png)


Figure 4: Efficient frontiers for Erdos-Renyi random networks with different connectivity. The defender’s cost is linear and the risk is 𝓡=𝓡L=4\bm{\mathcal{R}}=\bm{\mathcal{R}}^{L=4}. The value profiles 𝒛=𝜼=𝟏\bm{z}=\bm{\eta}=\bm{1} are uniform.

Fig.  [4](https://arxiv.org/html/2601.16805v1#S4.F4 "Figure 4 ‣ 4.1 Efficient frontier ‣ 4 Numerical results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion") shows the efficient frontiers of random networks, generated as instances of the sparse Erdős–Rényi random graph model with connectivity cc, representing the average number of neighbors per node. In this experiment, we assume a linear defender’s cost and a risk 𝓡=𝓡L\bm{\mathcal{R}}=\bm{\mathcal{R}}^{L} as in Eq. ([16](https://arxiv.org/html/2601.16805v1#S3.E16 "In 3.2 Paths of contagion and scalable solutions ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion")) and the value profiles are uniform 𝒛=𝜼=𝟏\bm{z}=\bm{\eta}=\bm{1}. We examine the effect of network topology by varying the connectivity level. Clearly, highly interconnected systems are both more vulnerable and harder to defend, as infections can spread along multiple pathways and are difficult to contain.

![Refer to caption](x5.png)

![Refer to caption](x6.png)

Figure 5: 
Efficient frontiers for an Erdos-Renyi random network, with linear defender’s cost and risk 𝓡=𝓡L=4\bm{\mathcal{R}}=\bm{\mathcal{R}}^{L=4}. The defender’s value profile 𝒛=𝟏\bm{z}=\bm{1} is uniform while the attacker’s value profile changes: 𝜼∈{0,1}n\bm{\eta}\in\{0,1\}^{n}, |𝜼|:=∑iηi|\bm{\eta}|:=\sum\_{i}\eta\_{i}. Left panel: optimal risk for the defender ℛ∗​(𝒛)=∑izi​ℛi∗\mathcal{R}^{\*}(\bm{z})=\sum\_{i}z\_{i}\mathcal{R}^{\*}\_{i}. Right Panel: optimal risk for the attacker ℛ∗​(𝜼)=∑iηi​ℛi∗\mathcal{R}^{\*}(\bm{\eta})=\sum\_{i}\eta\_{i}\mathcal{R}^{\*}\_{i}



![Refer to caption](x7.png)

![Refer to caption](x8.png)

Figure 6: 
Efficient frontiers for an Erdos-Renyi random network, with linear defender’s cost and risk 𝓡=𝓡L=4\bm{\mathcal{R}}=\bm{\mathcal{R}}^{L=4}. The attacker’s value profile 𝜼=𝟏\bm{\eta}=\bm{1} is uniform while the defender’s value profile changes: 𝒛∈{0,1}n\bm{z}\in\{0,1\}^{n}, |𝒛|:=∑izi|\bm{z}|:=\sum\_{i}z\_{i}. Left panel: optimal risk for the defender ℛ∗​(𝒛)=∑izi​ℛi∗\mathcal{R}^{\*}(\bm{z})=\sum\_{i}z\_{i}\mathcal{R}^{\*}\_{i}. Right Panel: optimal risk for the attacker ℛ∗​(𝜼)=∑iηi​ℛi∗\mathcal{R}^{\*}(\bm{\eta})=\sum\_{i}\eta\_{i}\mathcal{R}^{\*}\_{i}

In Fig. [5](https://arxiv.org/html/2601.16805v1#S4.F5 "Figure 5 ‣ 4.1 Efficient frontier ‣ 4 Numerical results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion"), for a given Erdos-Renyi network and uniform defender value profile 𝒛=𝟏\bm{z}=\bm{1}, we investigate the effect of changing 𝜼\bm{\eta}. In particular we choose 𝜼∈{0,1}n\bm{\eta}\in\{0,1\}^{n}, for different |𝜼|:=∑iηi|\bm{\eta}|:=\sum\_{i}\eta\_{i}, measuring the size of the subset of nodes that are valuable for the attacker. We measure both the defender’s risk ℛ∗​(𝒛)=∑izi​ℛi∗\mathcal{R}^{\*}(\bm{z})=\sum\_{i}z\_{i}\mathcal{R}^{\*}\_{i} and the attacker’s risk ℛ∗​(𝜼)=∑iηi​ℛi∗\mathcal{R}^{\*}(\bm{\eta})=\sum\_{i}\eta\_{i}\mathcal{R}^{\*}\_{i}, meaning the risk associated with the specific portion of the network relevant to the different players. The results indicate that a more localized attacker value profile leads to a lower systemic risk. Furthermore, the phase transition to zero risk occurs at a smaller defender’s budget threshold.

Conversely, Fig. [6](https://arxiv.org/html/2601.16805v1#S4.F6 "Figure 6 ‣ 4.1 Efficient frontier ‣ 4 Numerical results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion") shows the opposite situation in which the attacker value profile 𝜼=𝟏\bm{\eta}=\bm{1} is uniform while the size of the subset of nodes that are valuable for the defender changes, i.e. 𝒛∈{0,1}n\bm{z}\in\{0,1\}^{n}, for different |𝒛|:=∑izi|\bm{z}|:=\sum\_{i}z\_{i}.
Again it appears easier for the defender to pretect portion of the netowrk of smaller size, at a given budget. However the risk for the rest of the network increases, since the defensive strategy becomes suboptimal against systemic risk.

### 4.2 Cyber-deception strategy effects

A detailed examination of the optimal defender’s strategy reveals how the investment is distributed across the various nodes of the network.

![Refer to caption](x9.png)

![Refer to caption](x10.png)

![Refer to caption](x11.png)

Figure 7: Optimal investment pattern 𝒒∗\bm{q}^{\*} in a community network composed by three groups of 10 nodes, connected through the links (10,1110,11) and (20,21)(20,21), for different value profiles 𝜼\bm{\eta} and 𝒛\bm{z}. Each panel corresponds to a
different defender’s value profile, aiming to protect respectively the whole system (Left Panel),
the first node (Central Panel), and the central community (Right Panel). Different colors refers to different attacker’s value profile.

In Fig. [7](https://arxiv.org/html/2601.16805v1#S4.F7 "Figure 7 ‣ 4.2 Cyber-deception strategy effects ‣ 4 Numerical results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion") for example we display the optimal investment pattern, computed used the approximation of Theorem [3.1](https://arxiv.org/html/2601.16805v1#S3.Thmtheorem1 "Theorem 3.1(Asymptotic SSE) ‣ 3.1 Asymptotic Equilibrium and Emerging Network metrics ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion") through protection metrics, in a network of 3030 nodes with assortative communities, for different value profile scenarios. Specifically, we analyze three cases: (i) all nodes in the network have equal value, i.e. 𝒛,𝜼=(1/30,…,1/30)\bm{z},\bm{\eta}=(1/30,\ldots,1/30); (ii) node 11, which is a random node of the first community, is more valuable than the others, i.e. 𝒛,𝜼=(1,…,0)\bm{z},\bm{\eta}=(1,\ldots,0); (iii) the entire central community is targeted, i.e. 𝒛,𝜼=(0,…,0,1/10,…,1/10,0,…,0)\bm{z},\bm{\eta}=(0,\ldots,0,1/10,\ldots,1/10,0,\ldots,0). Across the three plots, the defender’s value profile remains constant, whereas the attacker’s profile changes.

Nodes that serve as inter-community bridges tend to be the most strategic to protect, given their key role in halting the spread of infections when immunized. As expected, when the value profiles correspond to cases (i) or (iii), the investment pattern appears symmetric with respect to the central community. In contrast, this symmetry breaks when either 𝒛\bm{z} or 𝜼\bm{\eta} falls under case (ii). Furthermore, it is unsurprising that nodes in proximity to the defender’s most valuable assets attract greater security investment.

However, several unexpected effects become clearly observable. In particular, the attacker’s most valuable nodes consistently appear under-protected compared to others. Specifically, when node 1 becomes the most valuable for the attacker, its level of protection drops significantly (orange patterns); similarly, when the central community is the attacker’s primary target, its relative investment—compared to that of other communities—decreases (green pattern). These phenomena can be interpreted as instances of cyber-deception that favor the attacker, and are induced by the specific sequencing of actions in the Stackelberg framework. In fact, the attacker’s optimal strategy consists in avoiding a direct assault on the most valuable nodes. Instead, the attacker tends to select a seed that is relatively distant from them. This approach, combined with the sequential structure of the Stackelberg game, allows the attacker to mislead the defender, who ends up dispersing investments away from the actual targets. These effects arise because the defender does not have direct knowledge of the attacker’s specific value profile, having access only to the attacker’s optimal response function. Conversely, they are less pronounced when the attacker’s and defender’s value profiles—and thus their respective targets—coincide.

### 4.3 Contagion Dynamics

As previously discussed, optimal strategies have been derived within a game-theoretical framework that does not explicitly model contagion dynamics, but rather assumes that the epidemic has already reached its equilibrium, i.e. the infection has fully propagated through the transmission subnetwork of susceptible nodes.

However, our result can be evaluated under conditions of actual dynamic contagion, allowing us to assess its robustness against potential model misspecifications. To this end, we consider a benchmark class of epidemic models that describe the temporal evolution of infections across the network.
Specifically, we consider a Markovian dynamics for the state evolution of nodes. The state at time tt is defined by a vector 𝝈t∈{0,1}n\bm{\sigma}^{t}\in\{0,1\}^{n}, where σit\sigma^{t}\_{i} is equal to one if the ii-th node of the network is infected at time tt, and zero otherwise.

We consider a setting in which, in the absence of security investments, each susceptible node ((σit=0)(\sigma^{t}\_{i}=0)) faces a probability of infection proportional to β\beta at each time step, due to contact with each infected neighbors. At the same time, each infected node has a probability 1−γ1-\gamma to recover thanks to its baseline security defenses. We therefore consider a general class of possible contagion dynamics defined by the transition rule

|  |  |  |  |
| --- | --- | --- | --- |
|  | σit+1=Θ​[σit​(γ−u)+(1−σit)​(βdi​∑j=1nAi​j​σjt−Z)],\sigma^{t+1}\_{i}=\Theta\left[\sigma^{t}\_{i}(\gamma-u)+(1-\sigma^{t}\_{i})\left(\frac{\beta}{d\_{i}}\sum\_{j=1}^{n}A\_{ij}\sigma^{t}\_{j}-Z\right)\right], |  | (19) |

where di=∑jAi​jd\_{i}=\sum\_{j}A\_{ij} is the degree of the ii-th node, i.e. the number of neighbors, and u,Zu,Z are random variables. In particular, u∼U​(0,1)u\sim U(0,1) and ZZ is a convex combination of an uniform random variable and a deterministic threshold δ∈[0,1]\delta\in[0,1], i.e. Z=τ​δ+(1−τ)​uZ=\tau\delta+(1-\tau)u, τ∈[0,1]\tau\in[0,1].

For τ=1\tau=1, Eq. ([19](https://arxiv.org/html/2601.16805v1#S4.E19 "In 4.3 Contagion Dynamics ‣ 4 Numerical results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion")) represents a threshold contagion model [[24](https://arxiv.org/html/2601.16805v1#bib.bib69 "Threshold models of collective behavior"), [54](https://arxiv.org/html/2601.16805v1#bib.bib70 "A simple model of global cascades on random networks")], in which a susceptible node becomes infected if the fraction of infected neighbors exceeds a given threshold δ\delta. For τ=0\tau=0, it reduces to a SIS model [[44](https://arxiv.org/html/2601.16805v1#bib.bib43 "Epidemic processes in complex networks")] in which the probability of contagion is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ(σit+1=1|σit=0,𝝈\it)=1−∏i=1n(1−βAi​jσjt)=β∑j=1nAi​jσjt+o(β)\mathbb{P}\left(\sigma\_{i}^{t+1}=1|\sigma\_{i}^{t}=0,\bm{\sigma}\_{\backslash i}^{t}\right)=1-\prod\_{i=1}^{n}(1-\beta A\_{ij}\sigma^{t}\_{j})=\beta\sum\_{j=1}^{n}A\_{ij}\sigma^{t}\_{j}+o(\beta) |  | (20) |

and the contagion rate β\beta has been rescaled with the degree to ensure the r.h.s. term is in [0,1][0,1]. Finally, setting the recovery rate 1−γ1-\gamma to zero yields a classical SI model, where infected nodes remain infected indefinitely.

We assume that both players can influence the contagion dynamics. The defender mitigates the infection rate by investing in cyber-defense, which we model by rescaling the parameters as β→(1−qi)​β\beta\to(1-q\_{i})\beta. The attacker, on the other hand, determines the initial distribution of threats. Accordingly, we define the initial state of the Markov process as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(𝝈0)=∏i=1n(ϕi​(1−qi))σi0​(1−ϕi​(1−qi))1−σi0.\mathbb{P}(\bm{\sigma}^{0})=\prod\_{i=1}^{n}(\phi\_{i}(1-q\_{i}))^{\sigma^{0}\_{i}}(1-\phi\_{i}(1-q\_{i}))^{1-\sigma^{0}\_{i}}. |  | (21) |

Here, ϕi​(1−qi)\phi\_{i}(1-q\_{i}) represents the probability that node ii is initially infected, modulated by the defender’s investment level qiq\_{i}.

![Refer to caption](x12.png)


Figure 8:  SI contagion under different mitigation strategies: no protection, the proposed optimal strategy 𝒒∗\bm{q}^{\*} with uniform defender risk profile and a random reshuffling of the same budget. Left Panel: time evolution of the infection’s size (average activity). Right Panel: asymptotic infection size as a function of the defender’s budget.



![Refer to caption](x13.png)

![Refer to caption](x14.png)

Figure 9:  Infection dynamics under different propagation rules, protection strategies and defender budgets. Left panel: SIS dynamics with γ=0.8\gamma=0.8; Right Panel: threshold model with γ=0.9\gamma=0.9 and δ=0.2\delta=0.2. We compare three strategies: no protection (black), the proposed optimal strategy 𝒒∗\bm{q}^{\*} with uniform defender risk profile (full line) and a random reshuffling of the same budget (dashed line).

In Fig. [8](https://arxiv.org/html/2601.16805v1#S4.F8 "Figure 8 ‣ 4.3 Contagion Dynamics ‣ 4 Numerical results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion"), we illustrate the effect of a mitigation strategy in random network where the infection evolves according to a SI dynamics. We compare the evolution of the fraction of infected nodes in the absence of security investments with that mitigated by the optimal allocation 𝒒∗\bm{q}^{\*}, derived from the security game equilibrium under uniform value profiles and a fixed budget. The results clearly show that the infection spreads more slowly and remains less extensive. The mitigating effect of this strategy outperforms that of a random reshuffling of the same investment budget, demonstrating its robustness even under contagion mechanism misspecification. The benefit of adopting an optimized strategy is particularly evident in the medium-budget regime, where investments have the potential to reduce infection but are insufficient to fully immunize the system. In this setting, an effective allocation becomes decisive. Fig. [9](https://arxiv.org/html/2601.16805v1#S4.F9 "Figure 9 ‣ 4.3 Contagion Dynamics ‣ 4 Numerical results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion") shows that the previous results remain robust also under contagion dynamics governed by SIS and threshold models.

## Conclusions

In this paper, we considered a general class of security games with contagion to study the optimal allocation of cybersecurity investments across the nodes of a networked system subjected to strategic attacks. Our analysis focused on the role of asymmetry between the risk profiles targeted by the attacker and the defender, as well as their heterogeneity.

We showed that, in a low-budget regime, the Stackelberg equilibria of the game can be approximated using simple network metrics that capture each node’s ability to protect its neighbors and its value relative to the players’ objectives. We also proposed a risk measure based on the number of contagion paths, making the optimization problem scalable for larger networks.

From numerical experiments, we showed that, unlike standard security games, the presence of contagion mechanisms fosters the emergence of optimal strategies involving cyber deception. We analyzed efficient frontiers to compare systemic risk across networks with different topologies and to highlight how asymmetry and heterogeneity in risk profiles shape systemic resilience. Finally, we assessed the robustness of the proposed optimal strategies under alternative contagion dynamics.

Future perspectives will consider scenarios with incomplete or asymmetric information, examining how equilibrium strategies shift when defenders lack knowledge of the attacker’s objectives and vice versa. Moreover, both attacker and defender are assumed to have perfect information about the system’s architecture, which simplifies analysis but reduces realism. Assuming partial information on the network connections, especially for the attacker, would be a key perspective.

Another promising extension is a dynamic game formulation where the defender adapt their strategies as contagion unfolds. This could involve reallocating defenses across nodes or modifying the network topology, for example by disabling critical links. Coupling contagion dynamics with an iterative two-player game operating on different timescales would highlight a key missing element: the role of timing and the risks associated with delayed responses.

## 5 Appendix A: Proof of Theorem [3.1](https://arxiv.org/html/2601.16805v1#S3.Thmtheorem1 "Theorem 3.1(Asymptotic SSE) ‣ 3.1 Asymptotic Equilibrium and Emerging Network metrics ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion")

Before proving Theorem [3.1](https://arxiv.org/html/2601.16805v1#S3.Thmtheorem1 "Theorem 3.1(Asymptotic SSE) ‣ 3.1 Asymptotic Equilibrium and Emerging Network metrics ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion"), let us state some technical results. Throughout this appendix, let us denote ℙ​(q,ϕ;𝑨)\mathbb{P}(\textbf{q},\bm{\phi};\bm{A}) simply by ℙ​(q,ϕ)\mathbb{P}(\textbf{q},\bm{\phi}). By the definition ​​, we have the following decomposition of the probability that the node ii becomes infected:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙi​(q,ϕ)=(1−qi)​ℙ~i​(q−i,ϕ),\mathbb{P}\_{i}(\textbf{q},\bm{\phi})=(1-q\_{i})\tilde{\mathbb{P}}\_{i}(\textbf{q}\_{-i},\bm{\phi}), |  | (22) |

where (1−qi)(1-q\_{i}) is the probability that the node ii is susceptible and the marginal ℙ~i​(q−i,ϕ)\tilde{\mathbb{P}}\_{i}(\textbf{q}\_{-i},\bm{\phi}) is the probability that the infection reaches the node ii then it does not depends on the pointwise security investment qiq\_{i}, so q−i\textbf{q}\_{-i} denotes the security profile q without the entry qiq\_{i}. Therefore, the probability that the node jj, with j≠ij\not=i, becomes infected can be written as (Proposition 2, [[1](https://arxiv.org/html/2601.16805v1#bib.bib1 "Network security and contagion")]):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ~j​(q−j,ϕ)=ℙ~j​(q−{i,j},ϕ)+(1−qi)​Qj​i​(q−{i,j},ϕ),\tilde{\mathbb{P}}\_{j}(\textbf{q}\_{-j},\bm{\phi})=\tilde{\mathbb{P}}\_{j}(\textbf{q}\_{-\{i,j\}},\bm{\phi})+(1-q\_{i})Q\_{ji}(\textbf{q}\_{-\{i,j\}},\bm{\phi}), |  | (23) |

where ℙ~​(q−{i,j},ϕ)\tilde{\mathbb{P}}(\textbf{q}\_{-\{i,j\}},\bm{\phi}) is the probability that the infection reaches the node jj through a path that does not contain the node ii and Qj​i​(q−{i,j},ϕ)Q\_{ji}(\textbf{q}\_{-\{i,j\}},\bm{\phi}) is the probability that the infection reaches the node jj through a path that contains the node ii conditioned ii being susceptible. As a consequence, we obtain the following:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂∂qi​ℙj​(q,ϕ)=−δi​j​ℙ~i​(q,ϕ)−(1−δi​j)​(1−qj)​Qj​i​(q,ϕ),\frac{\partial}{\partial q\_{i}}\mathbb{P}\_{j}(\textbf{q},\bm{\phi})=-\delta\_{ij}\tilde{\mathbb{P}}\_{i}(\textbf{q},\bm{\phi})-(1-\delta\_{ij})(1-q\_{j})Q\_{ji}(\textbf{q},\bm{\phi}), |  | (24) |

where we have omitted the subscripts of q−i\textbf{q}\_{-i} and q−{i,j}\textbf{q}\_{-\{i,j\}} for convenience of notation.

###### Lemma 1

Given the security profile q and the attack distribution ϕ\bm{\phi}, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ~i​(q,ϕ)=1−∑j≠i∑tϕt​ai​tj​qj+o​(‖q‖∞),\tilde{\mathbb{P}}\_{i}(\textbf{q},\bm{\phi})=1-\sum\_{j\neq i}\sum\_{t}\phi\_{t}a\_{it}^{j}q\_{j}+o(\|\textbf{q}\|\_{\infty}), |  | (25) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1−qj)​Qj​i​(q,ϕ)=∑tϕt​(aj​ti+∑k≠i(bj​t(i,k)−aj​ti​aj​tk)​qk)+o​(‖q‖∞).(1-q\_{j})Q\_{ji}(\textbf{q},\bm{\phi})=\sum\_{t}\phi\_{t}\left(a^{i}\_{jt}+\sum\_{k\neq i}(b\_{jt}^{(i,k)}-a^{i}\_{jt}a^{k}\_{jt})q\_{k}\right)+o(\|\textbf{q}\|\_{\infty}). |  | (26) |

###### Proof

The claim is a direct generalization of Proposition 4 in [[1](https://arxiv.org/html/2601.16805v1#bib.bib1 "Network security and contagion")].

###### Proof(Theorem [3.1](https://arxiv.org/html/2601.16805v1#S3.Thmtheorem1 "Theorem 3.1(Asymptotic SSE) ‣ 3.1 Asymptotic Equilibrium and Emerging Network metrics ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion"))

Let us consider the optimization problem over the attacker’s utility, with risk function defined in ([5](https://arxiv.org/html/2601.16805v1#S3.E5 "In 3.1 Asymptotic Equilibrium and Emerging Network metrics ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion")) and quadratic cost function 𝒞a​(ϕ)=12​∑i=1nϕi2\mathcal{C}\_{a}(\bm{\phi})=\frac{1}{2}\sum\_{i=1}^{n}\phi\_{i}^{2}, in order to obtain the best response to the defender’s strategy 𝒒\bm{q}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxϕ⁡𝒰a​(ϕ;q)=maxϕ⁡(∑i=1nηi​ℙi​(q,ϕ)−θ2​∑i=1nϕi2)\max\_{\bm{\phi}}\mathcal{U}\_{a}(\bm{\phi};\textbf{q})=\max\_{\bm{\phi}}\left(\sum\_{i=1}^{n}\eta\_{i}\mathbb{P}\_{i}(\textbf{q},\bm{\phi})-\frac{\theta}{2}\sum\_{i=1}^{n}\phi\_{i}^{2}\right) |  | (27) |

subjected to the constraints ∑iϕi=1\sum\_{i}\phi\_{i}=1 and ϕi≥0\phi\_{i}\geq 0 ∀i=1,…,n\forall i=1,\ldots,n.
Let L=L​(𝒒,ϕ,λ,μ)L=L(\bm{q},\bm{\phi},\lambda,\mu) be the Lagrangian function, with parameters λ∈ℝ\lambda\in\mathbb{R} and μi∈ℝ+\mu\_{i}\in\mathbb{R}^{+} for all i=1,…,ni=1,\ldots,n, related to the considered constrained optimization problem:

|  |  |  |
| --- | --- | --- |
|  | L​(q,ϕ,λ,μ)=∑i=1nηi​ℙi​(𝒒,ϕ)−θ2​∑i=1nϕi2+λ​(∑i=1nϕi−1)+∑i=1nμi​ϕi.L(\textbf{q},\bm{\phi},\lambda,\mu)=\sum\_{i=1}^{n}\eta\_{i}\mathbb{P}\_{i}(\bm{q},\bm{\phi})-\frac{\theta}{2}\sum\_{i=1}^{n}\phi\_{i}^{2}+\lambda\left(\sum\_{i=1}^{n}\phi\_{i}-1\right)+\sum\_{i=1}^{n}\mu\_{i}\phi\_{i}. |  |

Requiring the optimality condition:

|  |  |  |
| --- | --- | --- |
|  | ∂∂ϕi​L​(q,ϕ,λ,μ)=ℙi​(q,𝜼)−θ​ϕi+λ+μi=0,∀i=1,…,n,\frac{\partial}{\partial\phi\_{i}}L(\textbf{q},\bm{\phi},\lambda,\mu)=\mathbb{P}\_{i}(\textbf{q},\bm{\eta})-\theta\phi\_{i}+\lambda+\mu\_{i}=0,\quad\forall i=1,...,n, |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙi​(q,𝜼)=∑s=1nηs​𝔼𝑿​[𝕀​(i∼s∈𝒯​(𝑿))],\mathbb{P}\_{i}(\textbf{q},\bm{\eta})=\sum\_{s=1}^{n}\eta\_{s}\mathbb{E}\_{\bm{X}}[\mathbb{I}(i\sim s\in\mathcal{T}(\bm{X}))], |  | (28) |

and imposing the constraints, we have that the best response ϕ∗​(q)=(ϕ1∗​(q),…,ϕn∗​(q))\bm{\phi}^{\*}(\textbf{q})=(\phi\_{1}^{\*}(\textbf{q}),...,\phi^{\*}\_{n}(\textbf{q})) of the attacker is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕi∗​(q)=1n+1θ​(ℙi​(q,𝜼)−1n​∑j=1nℙj​(q,𝜼)),i=1,…,n.\phi\_{i}^{\*}(\textbf{q})=\frac{1}{n}+\frac{1}{\theta}\left(\mathbb{P}\_{i}(\textbf{q},\bm{\eta})-\frac{1}{n}\sum\_{j=1}^{n}\mathbb{P}\_{j}(\textbf{q},\bm{\eta})\right),\quad i=1,...,n. |  | (29) |

Let us remark that the function in ([28](https://arxiv.org/html/2601.16805v1#S5.E28 "In Proof(Theorem 3.1) ‣ 5 Appendix A: Proof of Theorem 3.1 ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion")) directly relies the definition of the probability ([6](https://arxiv.org/html/2601.16805v1#S3.E6 "In 3.1 Asymptotic Equilibrium and Emerging Network metrics ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion")), however ℙi​(q,𝜼)\mathbb{P}\_{i}(\textbf{q},\bm{\eta}) is not a probability value since the weights η1,…,ηn\eta\_{1},\dots,\eta\_{n} are not convex coefficients in general.

In order to estimate the optimal strategy q∗\textbf{q}^{\*} of the defender, we are now interested in minimizing the defender’s loss, with quadratic cost function 𝒞d=12​∑i=1nqi2\mathcal{C}\_{d}=\frac{1}{2}\sum\_{i=1}^{n}q\_{i}^{2}, for ϕ=ϕ∗\bm{\phi}=\bm{\phi}^{\*}:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0\displaystyle 0 | =∂∂qi​ℒd​(q;ϕ∗)=∂∂qi​(∑s=1nzs​ℛs​(q,ϕ∗;𝑨)+α2​∑s=1nqs2).\displaystyle=\frac{\partial}{\partial q\_{i}}\mathcal{L}\_{d}(\textbf{q};\bm{\phi}^{\*})=\frac{\partial}{\partial q\_{i}}\left(\sum\_{s=1}^{n}z\_{s}\mathcal{R}\_{s}(\textbf{q},\bm{\phi}^{\*};\bm{A})+\frac{\alpha}{2}\sum\_{s=1}^{n}q\_{s}^{2}\right). |  | (30) |

Let 𝒆s\bm{e}\_{s} be the nn-dimensional vector with 1 in the ss-th entry and 0 elsewhere and 𝟏n\bm{1}\_{n} is the nn-dimensional vector with 1/n1/n in every entry. By definition ([6](https://arxiv.org/html/2601.16805v1#S3.E6 "In 3.1 Asymptotic Equilibrium and Emerging Network metrics ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion")), we have:

|  |  |  |
| --- | --- | --- |
|  | ℙi​(q,𝒆k)=𝔼𝑿​[𝕀​(i∼k∈𝒯​(𝑿))].\mathbb{P}\_{i}(\textbf{q},\bm{e}\_{k})=\mathbb{E}\_{\bm{X}}[\mathbb{I}(i\sim k\in\mathcal{T}(\bm{X}))]. |  |

Therefore, the derivative of ℒd\mathcal{L}\_{d} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂ℒd∂qi\displaystyle\frac{\partial\mathcal{L}\_{d}}{\partial q\_{i}} | =α​qi+∑k,szs​ϕk∗​∂ℙs​(q,𝒆k)∂qi+∑k,szs​ℙs​(q,𝒆k)​∂ϕk∗​(q)∂qi\displaystyle=\alpha q\_{i}+\sum\_{k,s}z\_{s}\phi^{\*}\_{k}\frac{\partial\mathbb{P}\_{s}(\textbf{q},\bm{e}\_{k})}{\partial q\_{i}}+\sum\_{k,s}z\_{s}\mathbb{P}\_{s}(\textbf{q},\bm{e}\_{k})\frac{\partial\phi\_{k}^{\*}(\textbf{q})}{\partial q\_{i}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | :=α​qi+xi+yi.\displaystyle:=\alpha q\_{i}+x\_{i}+y\_{i}. |  | (31) |

The term xix\_{i} is exactly the derivative computed for the social equilibrium in the random case, evaluated at ϕ∗\bm{\phi}^{\*}, while the term yiy\_{i} is due to the strategic nature of the problem and involves the derivative of ϕ∗=ϕ∗​(q)\bm{\phi}^{\*}=\bm{\phi}^{\*}(\textbf{q}). Let us compute the two terms applying ([24](https://arxiv.org/html/2601.16805v1#S5.E24 "In 5 Appendix A: Proof of Theorem 3.1 ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | xi\displaystyle x\_{i} | =∑k,szs​ϕk∗​∂ℙs​(q,𝒆k)∂qi\displaystyle=\sum\_{k,s}z\_{s}\phi^{\*}\_{k}\frac{\partial\mathbb{P}\_{s}(\textbf{q},\bm{e}\_{k})}{\partial q\_{i}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−zi​ℙ~i​(q,ϕ∗)−∑s≠izs​(1−qs)​Qs​i​(q,ϕ∗)\displaystyle=-z\_{i}\tilde{\mathbb{P}}\_{i}(\textbf{q},\bm{\phi}^{\*})-\sum\_{s\neq i}z\_{s}(1-q\_{s})Q\_{si}(\textbf{q},\bm{\phi}^{\*}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−zi​(1−∑j≠iaij​(ϕ∗)​qj)−\displaystyle=-z\_{i}\left(1-\sum\_{j\neq i}a^{j}\_{i}(\bm{\phi}^{\*})q\_{j}\right)- |  | (32) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −(∑j≠izj​aji​(ϕ∗)+∑j≠izj​∑s∑k≠iϕs∗​(bj​s(i,k)−aj​si​aj​sk)​qk)+o​(‖q‖∞)\displaystyle-\left(\sum\_{j\neq i}z\_{j}a^{i}\_{j}(\bm{\phi}^{\*})+\sum\_{j\neq i}z\_{j}\sum\_{s}\sum\_{k\neq i}\phi^{\*}\_{s}\left(b\_{js}^{(i,k)}-a^{i}\_{js}a^{k}\_{js}\right)q\_{k}\right)+o(\|\textbf{q}\|\_{\infty}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−∑jzj​aji​(ϕ∗)−∑j≠i∑s​kϕs∗​zk​(bk​s(i​j)−ak​si​ak​sj)​qj+o​(‖q‖∞)\displaystyle=-\sum\_{j}z\_{j}a^{i}\_{j}(\bm{\phi}^{\*})-\sum\_{j\neq i}\sum\_{sk}\phi^{\*}\_{s}z\_{k}\left(b^{(ij)}\_{ks}-a^{i}\_{ks}a^{j}\_{ks}\right)q\_{j}+o(\|\textbf{q}\|\_{\infty}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−ai​(ϕ∗,𝒛)−∑j≠ibi​j​(ϕ∗,𝒛)​qj+o​(‖q‖∞)\displaystyle=-a^{i}(\bm{\phi}^{\*},\bm{z})-\sum\_{j\neq i}b\_{ij}(\bm{\phi}^{\*},\bm{z})q\_{j}+o(\|\textbf{q}\|\_{\infty}) |  | (33) |

where we used the approximations for ℙ~\tilde{\mathbb{P}} and QQ provided by [1](https://arxiv.org/html/2601.16805v1#Thmlemma1 "Lemma 1 ‣ 5 Appendix A: Proof of Theorem 3.1 ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion"), aij=aij​(ϕ)a^{j}\_{i}=a^{j}\_{i}(\bm{\phi}), ai=ai​(ϕ,𝒛)a^{i}=a^{i}(\bm{\phi},\bm{z}), and bi​j=bi​j​(ϕ,𝒛)b\_{ij}=b\_{ij}(\bm{\phi},\bm{z}) are defined in ([7](https://arxiv.org/html/2601.16805v1#S3.E7 "In 3.1 Asymptotic Equilibrium and Emerging Network metrics ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion")), ([8](https://arxiv.org/html/2601.16805v1#S3.E8 "In 3.1 Asymptotic Equilibrium and Emerging Network metrics ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion")), and ([9](https://arxiv.org/html/2601.16805v1#S3.E9 "In 3.1 Asymptotic Equilibrium and Emerging Network metrics ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion")) respectively.
By inserting ϕ∗​(q)\bm{\phi}^{\*}(q), given in ([29](https://arxiv.org/html/2601.16805v1#S5.E29 "In Proof(Theorem 3.1) ‣ 5 Appendix A: Proof of Theorem 3.1 ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion")), and observing that

|  |  |  |
| --- | --- | --- |
|  | ϕk∗​(q)=1/n+∇ϕk∗​(0)⋅q+o​(q),\phi^{\*}\_{k}(\textbf{q})=1/n+\nabla\phi^{\*}\_{k}(0)\cdot\textbf{q}+o(\textbf{q}), |  |

we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | xi=−ai​(1/n,𝒛)−∑j≠ibi​j​(1/n,𝒛)​qj−∑j​kaj​ki​zj​∑s∂ϕk∗∂qs|q=0​qs+o​(‖q‖∞),x\_{i}=-a^{i}(1/n,\bm{z})-\sum\_{j\neq i}b\_{ij}(1/n,\bm{z})q\_{j}-\sum\_{jk}a^{i}\_{jk}z\_{j}\sum\_{s}\frac{\partial\phi^{\*}\_{k}}{\partial{q\_{s}}}\big|\_{\textbf{q}=0}q\_{s}+o(\|\textbf{q}\|\_{\infty}), |  | (34) |

where the first two terms are exactly the ones appearing in the random case.
The term yiy\_{i} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | yi\displaystyle y\_{i} | =∑k,szs​ℙs​(q,𝒆k)​∂ϕk∗​(q)∂qi=∑k,szs​(1−qs)​ℙ~s​(q,𝒆k)​∂ϕk∗​(q)∂qi\displaystyle=\sum\_{k,s}z\_{s}\mathbb{P}\_{s}(\textbf{q},\bm{e}\_{k})\frac{\partial\phi^{\*}\_{k}(\textbf{q})}{\partial{q\_{i}}}=\sum\_{k,s}z\_{s}(1-q\_{s})\tilde{\mathbb{P}}\_{s}(\textbf{q},\bm{e}\_{k})\frac{\partial\phi^{\*}\_{k}(\textbf{q})}{\partial{q\_{i}}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑k​szs​(1−qs)​(1−∑j≠sas​kj​qj)​∂ϕk∗​(q)∂qi+o​(‖q‖∞)\displaystyle=\sum\_{ks}z\_{s}(1-q\_{s})\left(1-\sum\_{j\neq s}a^{j}\_{sk}q\_{j}\right)\frac{\partial\phi^{\*}\_{k}(\textbf{q})}{\partial{q\_{i}}}+o(\|\textbf{q}\|\_{\infty}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑k​szs​(1−qs)​∂ϕk∗​(q)∂qi−∑k​szs​∑j≠sas​kj​qj​∂ϕk∗​(q)∂qi+o​(‖q‖∞)\displaystyle=\sum\_{ks}z\_{s}(1-q\_{s})\frac{\partial\phi^{\*}\_{k}(\textbf{q})}{\partial{q\_{i}}}-\sum\_{ks}z\_{s}\sum\_{j\neq s}a^{j}\_{sk}q\_{j}\frac{\partial\phi^{\*}\_{k}(\textbf{q})}{\partial{q\_{i}}}+o(\|\textbf{q}\|\_{\infty}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−∑k​szs​∑j≠sas​kj​qj​∂ϕk∗∂qi|q=0+o​(‖q‖∞),\displaystyle=-\sum\_{ks}z\_{s}\sum\_{j\neq s}a^{j}\_{sk}q\_{j}\frac{\partial\phi^{\*}\_{k}}{\partial{q\_{i}}}\big|\_{\textbf{q}=0}+o(\|\textbf{q}\|\_{\infty}), |  | (35) |

where we used that ∑kϕk∗=1\sum\_{k}\phi^{\*}\_{k}=1 and that only ∂qiϕk∗​(0)\partial\_{q\_{i}}\phi^{\*}\_{k}(0) contributes to the leading order. To make explicit xix\_{i} and yiy\_{i}, we just need to compute the term

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂ϕk∗∂qi|q=0\displaystyle\frac{\partial\phi\_{k}^{\*}}{\partial q\_{i}}\big|\_{\textbf{q}=0} | =∂∂qi​(1n+1θ​(ℙk​(q,𝜼)−1n​∑jℙj​(q,𝜼)))|q=0\displaystyle=\frac{\partial}{\partial q\_{i}}\left(\frac{1}{n}+\frac{1}{\theta}\left(\mathbb{P}\_{k}(\textbf{q},\bm{\eta})-\frac{1}{n}\sum\_{j}\mathbb{P}\_{j}(\textbf{q},\bm{\eta})\right)\right)\big|\_{\textbf{q}=0} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1θ​(∂ℙk​(q,𝜼)∂qi−1n​∑j∂ℙj​(q,𝜼)∂qi)|q=0\displaystyle=\frac{1}{\theta}\left(\frac{\partial\mathbb{P}\_{k}(\textbf{q},\bm{\eta})}{\partial q\_{i}}-\frac{1}{n}\sum\_{j}\frac{\partial\mathbb{P}\_{j}(\textbf{q},\bm{\eta})}{\partial q\_{i}}\right)\big|\_{\textbf{q}=0} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1θ(−δi​kℙ~i(q,𝜼)−(1−δi​k)(1−qk)Qk​i(q,𝜼)\displaystyle=\frac{1}{\theta}\left(-\delta\_{ik}\tilde{\mathbb{P}}\_{i}(\textbf{q},\bm{\eta})-(1-\delta\_{ik})(1-q\_{k})Q\_{ki}(\textbf{q},\bm{\eta})\right. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −1n∑j(−δi​jℙ~i(q,𝜼)−(1−δi​j)(1−qj)Qj​i(q,𝜼)))|q=0\displaystyle\left.-\frac{1}{n}\sum\_{j}\left(-\delta\_{ij}\tilde{\mathbb{P}}\_{i}(\textbf{q},\bm{\eta})-(1-\delta\_{ij})(1-q\_{j})Q\_{ji}(\textbf{q},\bm{\eta})\right)\right)\big|\_{\textbf{q}=0} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1θ​(−δk​i−(1−δk​i)​aki​(𝜼)+1n​∑j(δj​i+(1−δj​i)​aji​(𝜼)))\displaystyle=\frac{1}{\theta}\left(-\delta\_{ki}-(1-\delta\_{ki})a^{i}\_{k}(\bm{\eta})+\frac{1}{n}\sum\_{j}\left(\delta\_{ji}+(1-\delta\_{ji})a^{i}\_{j}(\bm{\eta})\right)\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =1θ​(ai​(1/n,𝜼)−aki​(𝜼)).\displaystyle=\frac{1}{\theta}\left(a^{i}(1/n,\bm{\eta})-a^{i}\_{k}(\bm{\eta})\right). |  | (36) |

By inserting it into ([5](https://arxiv.org/html/2601.16805v1#S5.Ex26 "Proof(Theorem 3.1) ‣ 5 Appendix A: Proof of Theorem 3.1 ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion")), we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | yi\displaystyle y\_{i} | =1θ​∑k​szs​∑j≠sas​kj​qj​(aki​(𝜼)−ai​(1/n,𝜼))+o​(‖q‖∞)\displaystyle=\frac{1}{\theta}\sum\_{ks}z\_{s}\sum\_{j\neq s}a^{j}\_{sk}q\_{j}\left(a^{i}\_{k}(\bm{\eta})-a^{i}(1/n,\bm{\eta})\right)+o(\|\textbf{q}\|\_{\infty}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1θ​∑k,s,jzs​as​kj​qj​(aki​(𝜼)−ai​(1/n,𝜼))+o​(‖q‖∞)\displaystyle=\frac{1}{\theta}\sum\_{k,s,j}z\_{s}a^{j}\_{sk}q\_{j}\left(a^{i}\_{k}(\bm{\eta})-a^{i}(1/n,\bm{\eta})\right)+o(\|\textbf{q}\|\_{\infty}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1θ​∑jqj​∑kakj​(𝒛)​(aki​(𝜼)−ai​(1/n,𝜼))+o​(‖q‖∞)\displaystyle=\frac{1}{\theta}\sum\_{j}q\_{j}\sum\_{k}a^{j}\_{k}(\bm{z})\left(a^{i}\_{k}(\bm{\eta})-a^{i}(1/n,\bm{\eta})\right)+o(\|\textbf{q}\|\_{\infty}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1θ​∑j(∑kaki​(𝜼)​akj​(𝒛)−ai​(1/n,𝜼)​aj​(1/n,𝒛))​qj+o​(‖q‖∞),\displaystyle=\frac{1}{\theta}\sum\_{j}\left(\sum\_{k}a^{i}\_{k}(\bm{\eta})a^{j}\_{k}(\bm{z})-a^{i}(1/n,\bm{\eta})a^{j}(1/n,\bm{z})\right)q\_{j}+o(\|\textbf{q}\|\_{\infty}), |  |

where, in the second line we used that we have zero if j=sj=s. Using the same type of computaion in Eq. ([34](https://arxiv.org/html/2601.16805v1#S5.E34 "In Proof(Theorem 3.1) ‣ 5 Appendix A: Proof of Theorem 3.1 ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion")) we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | xi=\displaystyle x\_{i}= | −ai​(1/n,𝒛)−∑j≠ibi​j​(1/n,𝒛)​qj\displaystyle-a^{i}(1/n,\bm{z})-\sum\_{j\neq i}b\_{ij}(1/n,\bm{z})q\_{j} |  | (37) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +1θ​∑j(∑kaki​(𝒛)​akj​(𝜼)−ai​(1/n,𝒛)​aj​(1/n,𝜼))​qj+o​(‖q‖∞).\displaystyle+\frac{1}{\theta}\sum\_{j}\left(\sum\_{k}a^{i}\_{k}(\bm{z})a^{j}\_{k}(\bm{\eta})-a^{i}(1/n,\bm{z})a^{j}(1/n,\bm{\eta})\right)q\_{j}+o(\|\textbf{q}\|\_{\infty}). |  | (38) |

Putting all together into ([5](https://arxiv.org/html/2601.16805v1#S5.Ex20 "Proof(Theorem 3.1) ‣ 5 Appendix A: Proof of Theorem 3.1 ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion")) we get:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂ℒd∂qi=\displaystyle\frac{\partial\mathcal{L}\_{d}}{\partial q\_{i}}= | α​qi−ai​(1/n,𝒛)\displaystyle\ \alpha q\_{i}-a^{i}(1/n,\bm{z}) |  | (39) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∑j≠ibi​j​(1/n,𝒛)​qj+1θ​∑j(∑kaki​(𝜼)​akj​(𝒛)−ai​(1/n,𝜼)​aj​(1/n,𝒛))​qj\displaystyle-\sum\_{j\neq i}b\_{ij}(1/n,\bm{z})q\_{j}+\frac{1}{\theta}\sum\_{j}\left(\sum\_{k}a^{i}\_{k}(\bm{\eta})a^{j}\_{k}(\bm{z})-a^{i}(1/n,\bm{\eta})a^{j}(1/n,\bm{z})\right)q\_{j} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +1θ​∑j(∑kaki​(𝒛)​akj​(𝜼)−ai​(1/n,𝒛)​aj​(1/n,𝜼))​qj+o​(‖q‖∞)\displaystyle+\frac{1}{\theta}\sum\_{j}\left(\sum\_{k}a^{i}\_{k}(\bm{z})a^{j}\_{k}(\bm{\eta})-a^{i}(1/n,\bm{z})a^{j}(1/n,\bm{\eta})\right)q\_{j}+o(\|\textbf{q}\|\_{\infty}) |  | (40) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | α​qi−si​(𝒛,𝜼;𝒑1,𝒑2)−∑jMi​j​(𝒛,𝜼;𝒑1,𝒑2)​qj+o​(‖q‖∞),\displaystyle\ \alpha q\_{i}-s^{i}(\bm{z},\bm{\eta};\bm{p}^{1},\bm{p}^{2})-\sum\_{j}M\_{ij}(\bm{z},\bm{\eta};\bm{p}^{1},\bm{p}^{2})q\_{j}+o(\|\textbf{q}\|\_{\infty}), |  |

where the vector 𝒔\bm{s} and the matrix 𝑴\bm{M} are defined in ([3.1](https://arxiv.org/html/2601.16805v1#S3.Ex8 "Theorem 3.1(Asymptotic SSE) ‣ 3.1 Asymptotic Equilibrium and Emerging Network metrics ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion")), as a consequence the equilibrium q∗\textbf{q}^{\*} satisfies ([10](https://arxiv.org/html/2601.16805v1#S3.E10 "In Theorem 3.1(Asymptotic SSE) ‣ 3.1 Asymptotic Equilibrium and Emerging Network metrics ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion")).

## References

* [1]
  D. Acemoglu, A. Malekian, and A. Ozdaglar (2016)
  Network security and contagion.
  Journal of Economic Theory 166,  pp. 536–585.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p8.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion"),
  [§1](https://arxiv.org/html/2601.16805v1#S1.p9.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion"),
  [§3.1](https://arxiv.org/html/2601.16805v1#S3.SS1.p7.1 "3.1 Asymptotic Equilibrium and Emerging Network metrics ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion"),
  [§3.1](https://arxiv.org/html/2601.16805v1#S3.SS1.p9.10 "3.1 Asymptotic Equilibrium and Emerging Network metrics ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion"),
  [§3.1](https://arxiv.org/html/2601.16805v1#S3.SS1.p9.9 "3.1 Asymptotic Equilibrium and Emerging Network metrics ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion"),
  [§5](https://arxiv.org/html/2601.16805v1#S5.p1.13 "5 Appendix A: Proof of Theorem 3.1 ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion"),
  [§5](https://arxiv.org/html/2601.16805v1#Thmproofx1.p1.1 "Proof ‣ 5 Appendix A: Proof of Theorem 3.1 ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [2]
  D. Acemoglu, A. Ozdaglar, and A. Tahbaz-Salehi (2015)
  Systemic risk and stability in financial networks.
  American Economic Review 105 (2),  pp. 564–608.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p5.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [3]
  P. Akey, S. Lewellen, I. Liskovich, and C. Schiller (2023)
  Hacking corporate reputations.
  Rotman School of Management Working Paper (3143740).
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p2.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [4]
  E. Amir, S. Levi, and T. Livne (2018)
  Do firms underreport information on cyber-attacks? evidence from capital markets.
  Review of Accounting Studies 23 (3),  pp. 1177–1206.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p2.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [5]
  J. Aspnes, K. Chang, and A. Yampolskiy (2006)
  Inoculation strategies for victims of viruses and the sum-of-squares partition problem.
  Journal of Computer and System Sciences 72 (6),  pp. 1077–1093.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p8.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion"),
  [§1](https://arxiv.org/html/2601.16805v1#S1.p9.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [6]
  Y. Bachrach, M. Draief, and S. Goyal (2013)
  Contagion and observability in security domains.
  In 2013 51st Annual Allerton Conference on Communication, Control, and Computing (Allerton),
  External Links: [Document](https://dx.doi.org/10.1109/Allerton.2013.6736610)
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p8.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [7]
  R. Bai, H. Lin, X. Yang, X. Wu, M. Li, and W. Jia (2023)
  Stackelberg security games with contagious attacks on a network: reallocation to the rescue.
  Journal of Artificial Intelligence Research 77,  pp. 487–515.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p8.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [8]
  N. Basilico, N. Gatti, F. Amigoni, et al. (2009)
  Leader-follower strategies for robotic patrolling in environments with arbitrary topologies.
  In Proceedings of the International Joint Conference on Autonomous Agents and Multi Agent Systems (AAMAS),
   pp. 57–64.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p7.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [9]
  F. Caccioli, P. Barucca, and T. Kobayashi (2018)
  Network models of financial systemic risk: a review.
  Journal of Computational Social Science 1 (1),  pp. 81–114.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p5.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [10]
  G. Calice, C. Sala, and D. Tantari (2023)
  Contingent convertible bonds in financial networks.
  Scientific Reports 13 (1),  pp. 22337.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p5.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [11]
  H. Chan, M. Ceyko, and L. Ortiz (2017)
  Interdependent defense games with applications to internet security at the level of autonomous systems.
  Games 8 (1),  pp. 13.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p7.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [12]
  E. V. Cobos and S. Cakir (2024)
  A review of the economic costs of cyber incidents.
  World Bank Group, Working Paper.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p2.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [13]
  R. Cohen and S. Havlin (2010)
  Complex networks: structure, robustness and function.
   Cambridge university press.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p5.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [14]
  M. Crosignani, M. Macchiavelli, and A. F. Silva (2023)
  Pirates without borders: the propagation of cyberattacks through firms’ supply chains.
  Journal of Financial Economics 147 (2),  pp. 432–448.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p2.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [15]
  M. Eling and J. Wirfs (2019)
  What are the actual costs of cyber risk events?.
  European Journal of Operational Research 272 (3),  pp. 1109–1119.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p2.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [16]
  F. Fang and T. H. Nguyen (2016)
  Green security games: apply game theory to addressing green security challenges.
  ACM SIGecom Exchanges 15 (1),  pp. 78–83.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p7.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [17]
  F. Fang, P. Stone, and M. Tambe (2015)
  When security games go green: designing defender strategies to prevent poaching and illegal fishing..
  In IJCAI,
  Vol. 15,  pp. 2589–2595.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p7.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [18]
  T. S. Ferguson (2020)
  A course in game theory.
   World Scientific.
  Cited by: [§2.3](https://arxiv.org/html/2601.16805v1#S2.SS3.p5.1 "2.3 Stackelberg Equilibrium ‣ 2 Model ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [19]
  P. Gai and S. Kapadia (2010)
  Contagion in financial networks.
  Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences 466 (2120),  pp. 2401–2423.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p5.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [20]
  J. Gan, E. Elkind, S. Kraus, and M. Wooldridge (2022)
  Defense coordination in security games: equilibrium analysis and mechanism design.
  Artificial Intelligence 313,  pp. 103791.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p7.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [21]
  W. Goffman and V. Newill (1964)
  Generalization of epidemic theory.
  Nature 204 (4955),  pp. 225–228.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p5.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [22]
  J. Goldstein, A. Chernobai, and M. Benaroch (2011)
  An event study analysis of the economic impact of it operational risk and its subcategories.
  Journal of the Association for Information Systems 12 (9),  pp. 1.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p2.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [23]
  S. Goyal and A. Vigier (2014)
  Attack, defence, and contagion in networks.
  The Review of Economic Studies 81 (4),  pp. 1518–1542.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p8.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [24]
  M. Granovetter (1978)
  Threshold models of collective behavior.
  American journal of sociology 83 (6),  pp. 1420–1443.
  Cited by: [§4.3](https://arxiv.org/html/2601.16805v1#S4.SS3.p4.3 "4.3 Contagion Dynamics ‣ 4 Numerical results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [25]
  S. R. Iyer, B. J. Simkins, and H. Wang (2020)
  Cyberattacks and impact on bond valuation.
  Finance Research Letters 33,  pp. 101215.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p2.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [26]
  R. Jamilov, H. Rey, and A. Tahoun (2021)
  The anatomy of cyber risk.
  Technical report
   National Bureau of Economic Research.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p2.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [27]
  A. X. Jiang, A. D. Procaccia, Y. Qian, N. Shah, and M. Tambe (2013)
  Defender (mis) coordination in security games.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p7.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [28]
  M. Khouzani, Z. Liu, and P. Malacaria (2019)
  Scalable min-max multi-objective cyber-security optimisation over probabilistic attack graphs.
  European Journal of Operational Research 278 (3),  pp. 894–903.
  External Links: [Document](https://dx.doi.org/10.1016/j.ejor.2019.05.041)
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p7.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [29]
  D. Korzhyk, Z. Yin, C. Kiekintveld, V. Conitzer, and M. Tambe (2011)
  Stackelberg vs. nash in security games: an extended investigation of interchangeability, equivalence, and uniqueness.
  Journal of Artificial Intelligence Research 41,  pp. 297–327.
  Cited by: [§2.3](https://arxiv.org/html/2601.16805v1#S2.SS3.p5.1 "2.3 Stackelberg Equilibrium ‣ 2 Model ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [30]
  A. Kotidis and S. Schreft (2022)
  Cyberattacks and financial stability: evidence from a natural experiment.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p2.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [31]
  A. Kotidis and S. Schreft (2024)
  The propagation of cyberattacks through the financial system: evidence from an actual event.
  Available at SSRN 5087787.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p2.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [32]
  R. Kour, R. Karim, and P. Dersin (2025)
  Modelling cybersecurity strategies with game theory and cyber kill chain.
  International Journal of System Assurance Engineering and Management,  pp. 1–12.
  Cited by: [§2.3](https://arxiv.org/html/2601.16805v1#S2.SS3.p3.1 "2.3 Stackelberg Equilibrium ‣ 2 Model ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [33]
  V. S. A. Kumar, S. Parameswaran, A. Srinivasan, and A. Vullikanti (2010)
  Existence theorems and approximation algorithms for generalized network security games.
  In Proceedings of the 2010 IEEE 30th International Conference on Distributed Computing Systems (ICDCS),
   pp. 132–143.
  External Links: [Document](https://dx.doi.org/10.1109/ICDCS.2010.20)
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p8.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [34]
  V. Latora, V. Nicosia, and G. Russo (2017)
  Complex networks: principles, methods and applications.
   Cambridge University Press.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p5.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [35]
  M. Li, L. Tran-Thanh, and X. Wu (2020)
  Defending with shared resources on a network.
  In Proceedings of the AAAI Conference on Artificial Intelligence,
  Vol. 34,  pp. 2046–2053.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p7.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [36]
  X. Liang and Y. Xiao (2012)
  Game theory for network security.
  IEEE Communications Surveys & Tutorials 15 (1),  pp. 472–486.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p6.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [37]
  B. Liu, H. Xu, and X. Zhou (2018)
  Stackelberg dynamic game-based resource allocation in threat defense for internet of things.
  Sensors 18 (11).
  External Links: [Link](https://www.mdpi.com/1424-8220/18/11/4074),
  ISSN 1424-8220,
  [Document](https://dx.doi.org/10.3390/s18114074)
  Cited by: [§2.3](https://arxiv.org/html/2601.16805v1#S2.SS3.p3.1 "2.3 Stackelberg Equilibrium ‣ 2 Model ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [38]
  J. Lou, A. M. Smith, and Y. Vorobeychik (2017)
  Multidefender security games.
  IEEE Intelligent Systems 32 (1),  pp. 50–60.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p7.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [39]
  M. H. Manshaei, Q. Zhu, T. Alpcan, T. Bacşar, and J. Hubaux (2013)
  Game theory meets network security and privacy.
  Acm Computing Surveys (Csur) 45 (3),  pp. 1–39.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p6.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [40]
  H. M. Markowitz (1952)
  Portfolio selection, the journal of finance. 7 (1).
  N 1,  pp. 71–91.
  Cited by: [§4.1](https://arxiv.org/html/2601.16805v1#S4.SS1.p2.3 "4.1 Efficient frontier ‣ 4 Numerical results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [41]
  M. Nekovee, Y. Moreno, G. Bianconi, and M. Marsili (2007)
  Theory of rumour spreading in complex social networks.
  Physica A: Statistical Mechanics and its Applications 374 (1),  pp. 457–470.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p5.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [42]
  M. Newman (2018)
  Networks.
   Oxford university press.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p5.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [43]
  T. Nguyen, M. P. Wellman, and S. Singh (2017)
  A stackelberg game model for botnet data exfiltration.
  In Decision and Game Theory for Security, S. Rass, B. An, C. Kiekintveld, F. Fang, and S. Schauer (Eds.),
  Cham,  pp. 151–170.
  External Links: ISBN 978-3-319-68711-7
  Cited by: [§2.3](https://arxiv.org/html/2601.16805v1#S2.SS3.p3.1 "2.3 Stackelberg Equilibrium ‣ 2 Model ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [44]
  R. Pastor-Satorras, C. Castellano, P. Van Mieghem, and A. Vespignani (2015)
  Epidemic processes in complex networks.
  Reviews of modern physics 87 (3),  pp. 925–979.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p5.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion"),
  [§4.3](https://arxiv.org/html/2601.16805v1#S4.SS3.p4.3 "4.3 Contagion Dynamics ‣ 4 Numerical results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [45]
  L. R. Piccotti and H. Wang (2023)
  Informed trading in the options market surrounding data breaches.
  Global Finance Journal 56,  pp. 100774.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p2.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [46]
  J. Pita, M. Jain, J. Marecki, F. Ordóñez, C. Portway, M. Tambe, C. Western, P. Paruchuri, and S. Kraus (2008)
  Deployed armor protection: the application of a game theoretic model for security at the los angeles international airport.
  In Proceedings of the 7th international joint conference on Autonomous agents and multiagent systems: industrial track,
   pp. 125–132.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p7.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [47]
  S. Roy, C. Ellis, S. Shiva, D. Dasgupta, V. Shandilya, and Q. Wu (2010)
  A survey of game theory as applied to network security.
  In 2010 43rd Hawaii international conference on system sciences,
   pp. 1–10.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p6.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [48]
  E. Shieh, B. An, R. Yang, M. Tambe, C. Baldwin, J. DiRenzo, B. Maule, and G. Meyer (2012)
  Protect: a deployed game theoretic system to protect the ports of the united states.
  In Proceedings of the 11th international conference on autonomous agents and multiagent systems-volume 1,
   pp. 13–20.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p7.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [49]
  A. Sinha, F. Fang, B. An, C. Kiekintveld, and M. Tambe (2018)
  Stackelberg security games: looking beyond a decade of success.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p7.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [50]
  J. Song and G. Wang (2023)
  Identifying influential nodes in complex contagion mechanism.
  Frontiers in Physics 11,  pp. 1046077.
  Cited by: [§3.1](https://arxiv.org/html/2601.16805v1#S3.SS1.p6.4 "3.1 Asymptotic Equilibrium and Emerging Network metrics ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [51]
  S. H. Strogatz (2001)
  Exploring complex networks.
  nature 410 (6825),  pp. 268–276.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p5.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [52]
  M. Tambe (2011)
  Security and game theory: algorithms, deployed systems, lessons learned.
   Cambridge university press.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p6.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [53]
  J. Tsai, T. Nguyen, and M. Tambe (2012)
  Security games for controlling contagion.
  In Proceedings of the AAAI Conference on Artificial Intelligence,
  Vol. 26,  pp. 1464–1470.
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p8.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [54]
  D. J. Watts (2002)
  A simple model of global cascades on random networks.
  Proceedings of the National Academy of Sciences 99 (9),  pp. 5766–5771.
  Cited by: [§4.3](https://arxiv.org/html/2601.16805v1#S4.SS3.p4.3 "4.3 Contagion Dynamics ‣ 4 Numerical results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [55]
  T. Yin, A. Sarabi, and M. Liu (2023)
  Deterrence, backup, or insurance: game-theoretic modeling of ransomware.
  Games 14 (2).
  External Links: [Link](https://www.mdpi.com/2073-4336/14/2/20),
  ISSN 2073-4336,
  [Document](https://dx.doi.org/10.3390/g14020020)
  Cited by: [§2.3](https://arxiv.org/html/2601.16805v1#S2.SS3.p3.1 "2.3 Stackelberg Equilibrium ‣ 2 Model ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [56]
  Y. Zhang, Y. Lu, G. Yang, and Z. Hang (2022)
  Multi-attribute decision making method for node importance metric in complex network.
  Applied Sciences 12 (4),  pp. 1944.
  Cited by: [§3.1](https://arxiv.org/html/2601.16805v1#S3.SS1.p6.4 "3.1 Asymptotic Equilibrium and Emerging Network metrics ‣ 3 Results ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").
* [57]
  Y. Zhang and P. Malacaria (2023)
  Keep spending: beyond optimal cyber-security investment.
  In 2023 IEEE 36th Computer Security Foundations Symposium (CSF),
   pp. 363–376.
  External Links: [Document](https://dx.doi.org/10.1109/csf57540.2023.00024)
  Cited by: [§1](https://arxiv.org/html/2601.16805v1#S1.p7.1 "1 Introduction ‣ Network Security under Heterogeneous Cyber-Risk Profiles and Contagion").