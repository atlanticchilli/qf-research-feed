---
authors:
- Maria Andraos
- Mario Ghossoub
doc_id: arxiv:2602.09967v1
family_id: arxiv:2602.09967
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection
url_abs: http://arxiv.org/abs/2602.09967v1
url_html: https://arxiv.org/html/2602.09967v1
venue: arXiv q-fin
version: 1
year: 2026
---


Maria Andraos
  
University of Waterloo
  
Mario Ghossoub
  
University of Waterloo
  
Maria Andraos: University of Waterloo – Department of Statistics and Actuarial Science – 200 University Ave. W. – Waterloo, ON, N2L 3G1 – Canada
[[mandraos@uwaterloo.ca](mailto:mandraos@uwaterloo.ca)](mailto:)
Mario Ghossoub: University of Waterloo – Department of Statistics and Actuarial Science – 200 University Ave. W. – Waterloo, ON, N2L 3G1 – Canada
[[mario.ghossoub@uwaterloo.ca](mailto:mario.ghossoub@uwaterloo.ca)](mailto:)

###### Abstract.

We study a monopolistic insurance market with hidden information, where the agent’s type θ\theta is private information that is unobservable to the insurer, and it is drawn from a continuum of types. The hidden type affects both the loss distribution and the risk attitude of the agent. Within this framework, we show that a menu of contracts is incentive efficient if and only if it maximizes social welfare, subject to incentive compatibility and individual rationality constraints. This equivalence holds for general concave utility functionals. In the special case of Yaari Dual Utility, we provide a semi-explicit characterization of optimal incentive-efficient menus of contracts. We do this under two different settings: (i) the first assumes that types are ordered in a way such that larger values of θ\theta correspond to more risk-averse types who face stochastically larger losses; whereas (ii) the second assumes that larger values of θ\theta correspond to less risk-averse types who face stochastically larger losses. In both settings, the structure of optimal incentive-efficient menus of contracts depends on the level of the social welfare weight. Moreover, at the optimum, higher types receive greater coverage in exchange for higher premia. Additionally, optimal menus leave the lowest type indifferent, with the insurer absorbing all surplus from the lowest type; and they exhibit efficiency at the top, that is, the highest type receives full coverage.

JEL Classification: D42, D61, D82, D86, G22.

Key Words and Phrases: Optimal insurance; asymmetric information; hidden types; individual rationality; incentive compatibility; Pareto optimality; incentive efficiency.

Mario Ghossoub acknowledges financial support from the Natural Sciences and Engineering Research Council of Canada (NSERC Grant No. 2024-03744).

## 1. Introduction

In insurance markets, contracts are written between two parties who generally do not share the same information about the underlying risk. In these markets, information asymmetry arises naturally because the agent typically knows more about their own exposure or behavior than the insurer can observe, as initially noted by Allais ([1953](https://arxiv.org/html/2602.09967v1#bib.bib2 "L’éxtension des Théories de l’Équilibre Économique General et du Rendement Social au Cas du Risque")). Two major obstacles for a smooth running of the insurance mechanism are moral hazard and adverse selection, which attracted the attention of economists. Both problems have been extensively studied for their implications on contract design and market efficiency.

Moral hazard arises when the outcome of a contract is partly influenced by the agent’s actions, and the insurer cannot, without incurring costs, observe or verify to what extent the reported losses are attributable to the agent’s behavior. Specifically, ex ante moral hazard occurs when the agent’s unobservable actions affect the probability of a loss before it occurs. This has been studied by Pauly ([1978](https://arxiv.org/html/2602.09967v1#bib.bib58 "Overinsurance and public provision of insurance: the roles of moral hazard and adverse selection")), Marshall ([1976](https://arxiv.org/html/2602.09967v1#bib.bib59 "Moral hazard")), Holmström ([1979](https://arxiv.org/html/2602.09967v1#bib.bib61 "Moral hazard and observability")) and Shavell ([1979](https://arxiv.org/html/2602.09967v1#bib.bib60 "On moral hazard and insurance")), among others. Ex post moral hazard, on the other hand, occurs when the agent can misreport or influence the realized magnitude of the loss after it occurs. This was first pointed out by Spence and Zeckhauser ([1978](https://arxiv.org/html/2602.09967v1#bib.bib62 "Insurance, information, and individual action")) and later studied by Townsend ([1979](https://arxiv.org/html/2602.09967v1#bib.bib63 "Optimal contracts and competitive markets with costly state verification")), for instance.

Our focus in this paper is on adverse selection, where the agent possesses private information about their risk characteristics and may use this hidden information to their own advantage. The insurer offers a menu of contracts designed in such a way that each agent type selects the contract intended for them, thereby revealing the agent’s private information through their contract choice. This self selection mechanism must satisfy incentive compatibility, ensuring that each agent prefers the contract designed for their own type over those intended for other types. Rothschild and Stiglitz ([1976](https://arxiv.org/html/2602.09967v1#bib.bib64 "Equilibrium in competitive insurance markets: an essay on the economics of imperfect information")) and Stiglitz ([1977](https://arxiv.org/html/2602.09967v1#bib.bib65 "Monopoly, non-linear pricing and imperfect information: the insurance market")) study insurance markets where the agent’s type, high risk or low risk, is the private information. They both assume that the agent is risk averse with expected utility preferences.
In particular, Rothschild and Stiglitz ([1976](https://arxiv.org/html/2602.09967v1#bib.bib64 "Equilibrium in competitive insurance markets: an essay on the economics of imperfect information")) consider a competitive market with multiple risk-neutral insurers, and they show that under information asymmetry, a separating equilibrium may arise. Different risk types are offered different insurance contracts tailored to their own characteristics. Low-risk agents receive partial coverage at a lower premium, while high-risk agents obtain full coverage but pay a higher premium.
In contrast, Stiglitz ([1977](https://arxiv.org/html/2602.09967v1#bib.bib65 "Monopoly, non-linear pricing and imperfect information: the insurance market")) considers a monopoly market with a single risk-neutral insurer offering a non-linear pricing menu subject to individual rationality and incentive compatibility constraints. He shows that under information asymmetry the equilibrium is also separating. In this setting, low-risk types may prefer not to purchase any coverage but if they do, they receive partial coverage; whereas high-risk types receive full coverage.
Chade and Schlee ([2012](https://arxiv.org/html/2602.09967v1#bib.bib66 "Optimal insurance with adverse selection")) extend the work of Stiglitz ([1977](https://arxiv.org/html/2602.09967v1#bib.bib65 "Monopoly, non-linear pricing and imperfect information: the insurance market")) by moving beyond the two-type framework, to a setting with a continuum of types. They show that in equilibrium, the monopolist insurer expects a strictly positive profit. The highest risk type receives full coverage, the lowest risk type is indifferent between insurance and no insurance, and all other types receive partial coverage.
Gershkov et al. ([2023](https://arxiv.org/html/2602.09967v1#bib.bib68 "Optimal insurance: dual utility, random losses, and adverse selection")) reexamine the classic monopoly insurance problem under adverse selection of Stiglitz ([1977](https://arxiv.org/html/2602.09967v1#bib.bib65 "Monopoly, non-linear pricing and imperfect information: the insurance market")), allowing for a continuum of privately known types, a type-dependent loss distribution hidden from the insurer, and Yaari’s dual utility for the agent’s preferences (Yaari ([1987](https://arxiv.org/html/2602.09967v1#bib.bib69 "The dual theory of choice under risk"))) rather than expected utility. This dual utility of Yaari is represented by a Choquet integral with respect to a distorted probability, where the distortion function represents the risk attitude (risk aversion) of the policyholder, and it is assumed to be known by the insurer. The monopolist risk neutral insurer’s problem is formulated as a constrained optimal contracting problem of expected-profit maximization subject to incentive compatibility and individual rationality constraints. They show that the optimal menu of contracts takes the form of a layered deductible indemnity schedule, under a regularity condition. Moreover, under specific technical conditions, the optimal menus consist of either linear deductible contracts or of upper-limit contracts. Consistent with the monopolist setting, they also show that, under asymmetric information, the insurer earns strictly positive profit.
Recently, Ghossoub et al. ([2025](https://arxiv.org/html/2602.09967v1#bib.bib67 "Optimal insurance in a monopoly: dual utilities with hidden risk attitudes")) consider a monopoly insurance market in which the insurer is risk neutral and profit maximizing. The agent’s preferences are given by Yaari’s dual utility, and the agent’s risk aversion level (or risk attitude) is his private information. Hence, in contrast to Gershkov et al. ([2023](https://arxiv.org/html/2602.09967v1#bib.bib68 "Optimal insurance: dual utility, random losses, and adverse selection")), the insurer observes the loss distribution but is unable to observe the agent’s risk attitude. They formulate the insurer’s problem as designing an incentive compatible and individually rational menu of contracts that maximizes expected profit. They show that the optimal menu consists of layered deductible contracts, insurance coverage and premia are monotone in the level of risk aversion, the most risk averse agent receives full coverage, and the insurer earns strictly positive profit.

Pareto efficiency under asymmetric information has been studied extensively in the literature.
For example, early contributions by Prescott and Townsend ([1984](https://arxiv.org/html/2602.09967v1#bib.bib73 "Pareto optima and competitive equilibria with adverse selection and moral hazard")), Jerez ([2003](https://arxiv.org/html/2602.09967v1#bib.bib74 "A dual characterization of incentive efficiency")), and Bisin and Gottardi ([2006](https://arxiv.org/html/2602.09967v1#bib.bib75 "Efficient competitive equilibria with adverse selection")) analyze constrained Pareto efficiency in environments with incentive compatibility, primarily in settings with finitely many types.
Ghossoub et al. ([2025](https://arxiv.org/html/2602.09967v1#bib.bib67 "Optimal insurance in a monopoly: dual utilities with hidden risk attitudes")) label this efficiency as incentive Pareto optimality. They show that any individually-rational and incentive-compatible menu that maximizes a social welfare function is incentive Pareto optimal, thereby providing a sufficient condition for incentive efficiency. Crucially, the necessity part of the equivalence between social welfare maximization and incentive Pareto efficiency was left unaddressed. This is arguably the more interesting, and the more complex result, which we establish in this paper.

In this paper, we consider a monopolistic insurance market, in which the agent’s type is private information, hidden from the insurer and drawn from a continuum Θ\Theta of types. The agent faces a type-dependent loss, with a continuous distribution function that is unknown to the insurer. Additionally, the agent’s utility functional UU is a function of the type θ\theta, in that θ\theta is a parameter of the agent’s utility evaluation of their welfare. Consequently, the agent’s type affects both the riskiness of the agent (the loss distribution) and the risk-attitude of the agent (e.g., their risk aversion, through a parameterization of the utility functional). We extend the notion of incentive efficiency (or incentive Pareto optimality) introduced in Ghossoub et al. ([2025](https://arxiv.org/html/2602.09967v1#bib.bib67 "Optimal insurance in a monopoly: dual utilities with hidden risk attitudes")) in the context of Yaari’s Dual Utility to arbitrary concave type-dependent utility functionals for both the policyholder and the insurer.

Our first main a novel contribution to the literature is to link the concept of incentive Pareto optimality to social welfare maximization under information asymmetry.
Theorem [3.8](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem8 "Theorem 3.8. ‣ 3.2. Social Welfare Maximization ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") formalizes this connection, and shows that a menu of contracts is incentive efficient if and only if it maximizes the social welfare, subject to individual rationality and incentive compatibility, in the presence of hidden information and a continuum of types. To the best of our knowledge, this is the first result to establish such equivalence that holds for arbitrary concave utility functionals of both the insurer and the agent, thereby providing the theoretical foundation for subsequent analysis.

As an application, we characterize optimal incentive-efficient menus of contracts in the specific case of Yaari’s Dual Utility. Specifically, in this special case of our general setup, we assume that both the insurer’s and agent’s preferences are represented by Yaari Dual Utility functionals, expressed as a Choquet integral with respect to a distorted probability. In this case, the insurer can observe neither the agent’s risk attitude nor their type-dependent loss distribution. We consider two orderings of the type space. In the first case, higher types are more risk averse and face stochastically larger losses. In the second case, higher types are less risk averse and face stochastically larger losses. In both cases, each type of agent is assumed to be weakly more risk averse than the monopolistic insurer.
We show in Theorem [4.17](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem17 "Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") that, depending on the social weight level and under some technical conditions, the optimal menu of contracts exhibits one of two distinct forms: either a layered marginal retention structure, or full coverage (zero retention).

Additionally, in both aforementioned orderings of the type space, the optimal incentive-efficient menu displays some desirable monotonicity properties. Specifically, in the first ordering of the type space, higher types facing stochastically larger losses receive more coverage at higher premia, and efficiency at the top holds: full coverage is provided to the highest type. This echoes the results of Chade and Schlee ([2012](https://arxiv.org/html/2602.09967v1#bib.bib66 "Optimal insurance with adverse selection")), Gershkov et al. ([2023](https://arxiv.org/html/2602.09967v1#bib.bib68 "Optimal insurance: dual utility, random losses, and adverse selection")), and Ghossoub et al. ([2025](https://arxiv.org/html/2602.09967v1#bib.bib67 "Optimal insurance in a monopoly: dual utilities with hidden risk attitudes")). The insurer absorbs the surplus from the lowest type leaving them indifferent between insuring and not insuring, and higher types derive lower utilities from the optimal menu. On the insurer’s side, the utility depends on the degree of loss transfer. Serving higher types who face stochastically larger losses does not necessarily yield higher utility for the insurer. In particular, Proposition [4.19](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem19 "Proposition 4.19. ‣ 4.5. Properties of the Optimal Menu ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") characterizes how the insurer’s utility from the optimal menu varies across types. Similar results hold for the second kind of ordering of the type space.

The rest of the paper is organized as follows. Section [2](https://arxiv.org/html/2602.09967v1#S2 "2. The Insurance Market ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") introduces the insurance market model. In Section [3](https://arxiv.org/html/2602.09967v1#S3 "3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), we define incentive-efficient menus of contracts and establish the equivalence between social welfare maximization and incentive efficiency, in the general case of concave type-dependent utility functionals. Section [4](https://arxiv.org/html/2602.09967v1#S4 "4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") provides a characterization of incentive efficient menus in the Yaari Dual Utility framework, under different assumptions on the ordering of the type space. Section [5](https://arxiv.org/html/2602.09967v1#S5 "5. Conclusion ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") concludes. Proofs and related analysis are given in the [Appendices](https://arxiv.org/html/2602.09967v1#LinkToAppendix "5. Conclusion ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").

## 2. The Insurance Market

Let (S,Σ,ℙ)(S,\Sigma,\mathbb{P}) be a probability space, and denote by B​(Σ)B(\Sigma) the space of bounded, real-valued, and Σ\Sigma-measurable functions. We consider an insurance market in which an agent is facing an insurable loss, modeled as an element of B​(Σ)B(\Sigma), and seeking coverage from a monopolist insurer, in return for a premium payment.

The agent has a type denoted by θ\theta, which is private information that is unobservable to the insurer. We assume that the agent’s type θ\theta is drawn from a continuum Θ=[θ¯,θ¯]\Theta=[\underline{\theta},\bar{\theta}] of types. Let ℬ​(Θ)\mathcal{B}(\Theta) denote the Borel sigma-algebra on the type space Θ\Theta, and equip the measurable space of types (Θ,ℬ​(Θ))(\Theta,\mathcal{B}(\Theta)) with the Lebesgue measure ℒ\mathcal{L}.

We assume that the loss faced by the agent is type dependent. Specifically, for θ∈Θ\theta\in\Theta, the type-θ\theta agent faces a nonnegative loss Lθ∈B​(Σ)L\_{\theta}\in B(\Sigma), which can be covered by an indemnity function Iθ​(Lθ)I\_{\theta}(L\_{\theta}), in exchange for a premium payment pθ∈ℝp\_{\theta}\in\mathbb{R}. The loss LθL\_{\theta} takes values in [0,L¯θ][0,\bar{L}\_{\theta}], for some L¯θ<+∞\bar{L}\_{\theta}<+\infty. For simplicity, one can assume that for each θ∈Θ\theta\in\Theta, the random variable LθL\_{\theta} takes values in the interval [0,L¯][0,\bar{L}], where L¯:=supθ∈Θ​L¯θ<+∞\bar{L}:=\underset{\theta\in\Theta}{\sup}\ \bar{L}\_{\theta}<+\infty is the uniform upper bound.

To rule pout potential ex post moral hazard, we impose the customary restriction that the market only offers indemnities that satisfy the no-sabotage condition of Carlier and Dana ([2003](https://arxiv.org/html/2602.09967v1#bib.bib55 "Pareto efficient insurance contracts when the insurer’s cost function is discontinuous")).

###### Assumption 2.1.

We restrict the set of admissible indemnities to the following set of 1-Lipschitz and non-decreasing functions:

|  |  |  |
| --- | --- | --- |
|  | ℐ={I:[0,L¯]→[0,L¯],I​(0)=0,0≤I​(l1)−I​(l2)≤l1−l2,∀ 0≤l2≤l1≤L¯}.\mathcal{I}=\{I:[0,\bar{L}]\to[0,\bar{L}],I(0)=0,0\leq I(l\_{1})-I(l\_{2})\leq l\_{1}-l\_{2},\ \forall\,0\leq l\_{2}\leq l\_{1}\leq\bar{L}\ \}. |  |

Not knowing the agent’s type, the insurer sets out to design a menu of contracts, from which the agent can select one single contract.

###### Definition 2.2.

A menu of contracts is a collection of contracts

|  |  |  |
| --- | --- | --- |
|  | (Iθ,pθ)θ∈Θ,(I\_{\theta},p\_{\theta})\_{\theta\in\Theta}, |  |

such that for each type θ∈Θ\theta\in\Theta, the contract (Iθ,pθ)(I\_{\theta},p\_{\theta}) consists of a feasible indemnity function Iθ∈ℐI\_{\theta}\in\mathcal{I} and an associated premium pθp\_{\theta}.

Preferences in this market are represented by functionals U,V:Θ×ℐ×ℝ→ℝU,V:\Theta\times\mathcal{I}\times\mathbb{R}\to\mathbb{R}, where for a given triplet (θ,I,p)∈Θ×ℐ×ℝ\left(\theta,I,p\right)\in\Theta\times\mathcal{I}\times\mathbb{R},

|  |  |  |
| --- | --- | --- |
|  | U​(θ,I,p)U\left(\theta,I,p\right) |  |

denotes the end-of-period utility of a type-θ\theta agent after purchasing the contract (I,p)(I,p); and

|  |  |  |
| --- | --- | --- |
|  | V​(θ,I,p)V\left(\theta,I,p\right) |  |

denotes the insurer’s utility from providing the contract (I,p)(I,p) to a type-θ\theta agent. All throughout, we make the following normalization:

|  |  |  |
| --- | --- | --- |
|  | V​(θ,0,0)=0,∀θ∈Θ.V(\theta,0,0)=0,\ \ \forall\,\theta\in\Theta. |  |

For notational convenience, we write

|  |  |  |
| --- | --- | --- |
|  | Uθ​(I,p):=U​(θ,I,p)andVθ​(I,p):=V​(θ,I,p),U\_{\theta}(I,p):=U(\theta,I,p)\ \ \text{and}\ \ V\_{\theta}(I,p):=V(\theta,I,p), |  |

where θ\theta captures type dependence in the loss riskiness and in the agent’s risk characteristics.

## 3. Efficiency under asymmetric information

In full information settings, classical Pareto efficiency ensures that no one can be made better off without making someone else worse off. However, under asymmetric information, this classical concept of efficiency is no longer appropriate, unless incentive compatibility is imposed. This is because without incentive compatibility, a type-θ\theta agent might misreport their type and select a contract intended for other types. In this section, we discuss the notion of incentive Pareto optimality previously examined by Ghossoub et al. ([2025](https://arxiv.org/html/2602.09967v1#bib.bib67 "Optimal insurance in a monopoly: dual utilities with hidden risk attitudes")), and we provide a social-welfare characterization thereof.

### 3.1. Incentive Pareto Optimality

Let μ\mu be a probability measure on the measurable space of types (Θ,ℬ​(Θ))(\Theta,\mathcal{B}(\Theta)) representing the distribution of agent types in the market. That is, μ​(B)\mu(B) denotes the proportion of agent types lying in BB, for any measurable set B∈ℬ​(Θ)B\in\mathcal{B}(\Theta). The cumulative distribution function over types is defined by,

|  |  |  |
| --- | --- | --- |
|  | Q​(θ)=μ​([θ¯,θ]),∀θ∈Θ,Q(\theta)=\mu([\underline{\theta},\theta]),\ \forall\theta\in\Theta, |  |

with corresponding density function qq, with respect to Lebesgue measure.

###### Assumption 3.1.

We assume that the probability measure μ\mu is absolutely continuous with respect to the Lebesgue measure ℒ\mathcal{L} with Radon-Nikodym derivative qq. That is,

|  |  |  |
| --- | --- | --- |
|  | μ​(B)=∫Bq​(θ)​𝑑θ,for all B∈ℬ​(Θ) .\mu(B)=\int\_{B}q(\theta)\ d\theta,\ \text{for all $B\in\mathcal{B}(\Theta)$ }. |  |

###### Assumption 3.2.

For any menu of contracts (Iθ,pθ)θ∈Θ(I\_{\theta},p\_{\theta})\_{\theta\in\Theta}, the mappings θ↦Uθ​(Iθ,pθ)\theta\mapsto U\_{\theta}(I\_{\theta},p\_{\theta}) and θ↦Vθ​(Iθ,pθ)\theta\mapsto V\_{\theta}(I\_{\theta},p\_{\theta}) are in L1​(Θ,μ)L^{1}(\Theta,\mu).

Assumption [3.2](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem2 "Assumption 3.2. ‣ 3.1. Incentive Pareto Optimality ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") is a technical condition that ensures that the agent’s and the insurer’s utilities are integrable over the type space Θ\Theta, for any menu of contracts. Consequently, aggregate utilities are well defined as Bochner integrals. We refer to Appendix [A.1](https://arxiv.org/html/2602.09967v1#A1.SS1 "A.1. Bochner Integrability ‣ Appendix A Mathematical Background ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") for a detailed discussion of Bochner spaces.

###### Definition 3.3.

A menu of contracts (Iθ,pθ)θ∈Θ(I\_{\theta},p\_{\theta})\_{\theta\in\Theta} is said to be individually rational IR if both of the following hold.

1. (P1)

   Each agent type is incentivized to participate in the market. That is,

   |  |  |  |
   | --- | --- | --- |
   |  | Uθ​(Iθ,pθ)≥Uθ​(Lθ,0),for each θ∈Θ,U\_{\theta}(I\_{\theta},p\_{\theta})\geq U\_{\theta}(L\_{\theta},0),\,\text{for each $\theta\in\Theta$}, |  |

   where Uθ​(Lθ,0)U\_{\theta}(L\_{\theta},0) denotes the utility of the type-θ\theta agent in the absence insurance.
2. (P2)

   The insurer is incentivized to participate in the market. That is,

   |  |  |  |
   | --- | --- | --- |
   |  | ∫ΘVθ​(Iθ,pθ)​𝑑μ≥∫ΘVθ​(0,0)​𝑑μ=0,\int\_{\Theta}V\_{\theta}(I\_{\theta},p\_{\theta})\,d\mu\geq\int\_{\Theta}V\_{\theta}(0,0)\,d\mu=0, |  |

   where Vθ​(0,0)V\_{\theta}(0,0) denotes the insurer’s utility when no insurance is provided to the type-θ\theta agent.

We denote by ℐ​ℛ\mathcal{I}\mathcal{R} the set of all individual rational menus.

###### Definition 3.4.

A menu of contracts (Iθ,pθ)θ∈Θ(I\_{\theta},p\_{\theta})\_{\theta\in\Theta} is said to be incentive compatible IC if no type θ\theta can benefit from choosing the contract of another type θ′\theta^{\prime}. That is,

|  |  |  |
| --- | --- | --- |
|  | Uθ​(Iθ,pθ)≥Uθ​(Iθ′,pθ′),for each θ,θ′∈Θ.U\_{\theta}(I\_{\theta},p\_{\theta})\geq U\_{\theta}(I\_{\theta^{\prime}},p\_{\theta^{\prime}}),\ \ \text{for each $\theta,\theta^{\prime}\in\Theta$}. |  |

Let ℐ​𝒞\mathcal{I}\mathcal{C} be the set of all incentive compatible menus.

###### Definition 3.5.

A menu (Iθ∗,pθ∗)θ∈Θ∈ℐ​ℛ∩ℐ​𝒞\left(I^{\*}\_{\theta},p^{\*}\_{\theta}\right)\_{\theta\in\Theta}\in\mathcal{I}\mathcal{R}\cap\mathcal{I}\mathcal{C} is said to be incentive efficient or incentive Pareto optimal (IPO), if there does not exist another menu (Iθ,pθ)θ∈Θ∈ℐ​ℛ∩ℐ​𝒞(I\_{\theta},p\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{R}\cap\mathcal{I}\mathcal{C} such that the following two conditions hold:

1. (1)

   For μ\mu-almost every θ∈Θ\theta\in\Theta,

   |  |  |  |
   | --- | --- | --- |
   |  | Uθ​(Iθ,pθ)≥Uθ​(Iθ∗,pθ∗),U\_{\theta}(I\_{\theta},p\_{\theta})\geq U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta}), |  |

   and in addition

   |  |  |  |
   | --- | --- | --- |
   |  | ∫ΘVθ​(Iθ,pθ)​𝑑μ≥∫ΘVθ​(Iθ∗,pθ∗)​𝑑μ.\int\_{\Theta}V\_{\theta}(I\_{\theta},p\_{\theta})\,d\mu\geq\int\_{\Theta}V\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\,d\mu. |  |
2. (2)

   At least one of the two following conditions holds:

   |  |  |  |
   | --- | --- | --- |
   |  | ∫ΘVθ​(Iθ,pθ)​𝑑μ>∫ΘVθ​(Iθ∗,pθ∗)​𝑑μ,\int\_{\Theta}V\_{\theta}(I\_{\theta},p\_{\theta})\,d\mu>\int\_{\Theta}V\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\,d\mu, |  |

   or

   |  |  |  |
   | --- | --- | --- |
   |  | μ​({θ∈Θ;Uθ​(Iθ,pθ)>Uθ​(Iθ∗,pθ∗)})>0.\mu\left(\left\{\theta\in\Theta\,;\,U\_{\theta}(I\_{\theta},p\_{\theta})>U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\,\right\}\right)>0. |  |

We denote by ℐ​𝒫​𝒪⊆ℐ​ℛ∩ℐ​𝒞\mathcal{I}\mathcal{P}\mathcal{O}\subseteq\mathcal{I}\mathcal{R}\cap\mathcal{I}\mathcal{C} the set of all incentive efficient menus.

### 3.2. Social Welfare Maximization

We now establish the link between incentive efficient menus of contracts and social welfare maximization. We start by imposing the following assumptions on utility functionals.

###### Assumption 3.6.

For each θ∈Θ\theta\in\Theta, the utilities UθU\_{\theta} and VθV\_{\theta} are concave on the convex set of admissible contracts ℐ×ℝ\mathcal{I}\times\mathbb{R}.

###### Assumption 3.7.

There exists p∈(1,+∞)p\in(1,+\infty) and M<+∞M<+\infty such that for every menu of contracts (Iθ,pθ)θ∈Θ∈ℐ​ℛ∩ℐ​𝒞(I\_{\theta},p\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{R}\cap\mathcal{I}\mathcal{C},
the map

|  |  |  |  |
| --- | --- | --- | --- |
|  | u:Θ\displaystyle u:\Theta | →ℝ2\displaystyle\to\mathbb{R}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | θ\displaystyle\theta | ↦u​(θ):=(Uθ​(Iθ,pθ),∫ΘVϑ​(Iϑ,pϑ)​𝑑μ)\displaystyle\mapsto u(\theta):=\Big(U\_{\theta}(I\_{\theta},p\_{\theta}),\int\_{\Theta}V\_{\vartheta}(I\_{\vartheta},p\_{\vartheta})\,d\mu\Big) |  |

belongs to the Bochner space111See Appendix [A.1](https://arxiv.org/html/2602.09967v1#A1.SS1 "A.1. Bochner Integrability ‣ Appendix A Mathematical Background ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") for a definition. Lp​(Θ;ℝ2)L^{p}(\Theta;\mathbb{R}^{2}), and sup‖u‖Lp≤M<+∞\sup\|u\|\_{L^{p}}\leq M<+\infty.

Assumption [3.7](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem7 "Assumption 3.7. ‣ 3.2. Social Welfare Maximization ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") ensures that the function uu that maps each type to the pair of the agent’s utility function and the insurer’s aggregate utility belongs to a Bochner LpL^{p} space. Together with Assumption [3.6](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem6 "Assumption 3.6. ‣ 3.2. Social Welfare Maximization ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), these conditions will be useful in proving Theorem [3.8](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem8 "Theorem 3.8. ‣ 3.2. Social Welfare Maximization ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), which provides necessary and sufficient conditions for a menu of contracts to be incentive Pareto optimal.

###### Theorem 3.8.

A menu of contracts (Iθ∗,pθ∗)θ∈Θ(I^{\*}\_{\theta},p^{\*}\_{\theta})\_{\theta\in\Theta} is incentive efficient if and only if there exists a probability measure η\eta on the measurable space of types (Θ,ℬ​(Θ))(\Theta,\mathcal{B}(\Theta)) that is equivalent to μ\mu, and some α∈(0,1]\alpha\in(0,1] such that (Iθ∗,pθ∗)θ∈Θ(I^{\*}\_{\theta},p^{\*}\_{\theta})\_{\theta\in\Theta} is optimal for the following problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup(Iθ,pθ)θ∈Θ∈ℐ​ℛ∩ℐ​𝒞​{α​∫ΘUθ​(Iθ,pθ)​𝑑η+(1−α)​∫ΘVθ​(Iθ,pθ)​𝑑μ}.\underset{(I\_{\theta},p\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{R}\cap\mathcal{I}\mathcal{C}}{\sup}\left\{\alpha\int\_{\Theta}U\_{\theta}(I\_{\theta},p\_{\theta})\,\,d\eta+(1-\alpha)\int\_{\Theta}V\_{\theta}(I\_{\theta},p\_{\theta})\,\,d\mu\right\}\,\,. |  | (1) |

###### Proof.

The proof can be found in Appendix [B.1](https://arxiv.org/html/2602.09967v1#A2.SS1 "B.1. Proof of Theorem 3.8 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
∎

We denote by Wη,α​((Iθ,pθ)θ∈Θ)W\_{\eta,\alpha}\big((I\_{\theta},p\_{\theta})\_{\theta\in\Theta}\big) the social welfare function that combines the agent’s and insurer’s aggregate utilities under some welfare weight α∈(0,1]\alpha\in(0,1] and a probability measure η\eta equivalent to μ\mu:

|  |  |  |
| --- | --- | --- |
|  | Wη,α​((Iθ,pθ)θ∈Θ)=α​∫ΘUθ​(Iθ,pθ)​𝑑η+(1−α)​∫ΘVθ​(Iθ,pθ)​𝑑μ.W\_{\eta,\alpha}\big((I\_{\theta},p\_{\theta})\_{\theta\in\Theta}\big)=\alpha\int\_{\Theta}U\_{\theta}(I\_{\theta},p\_{\theta})\,\,d\eta+(1-\alpha)\int\_{\Theta}V\_{\theta}(I\_{\theta},p\_{\theta})\,\,d\mu. |  |

Theorem [3.8](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem8 "Theorem 3.8. ‣ 3.2. Social Welfare Maximization ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") provides a valuable characterization of incentive Pareto optimality through an equivalence with social welfare maximization. This is a general result that holds for any well-defined concave utility functionals UU and VV satisfying assumptions [3.6](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem6 "Assumption 3.6. ‣ 3.2. Social Welfare Maximization ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") and [3.7](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem7 "Assumption 3.7. ‣ 3.2. Social Welfare Maximization ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").

###### Remark 3.9.

The equivalence between μ\mu and η\eta in Theorem [3.8](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem8 "Theorem 3.8. ‣ 3.2. Social Welfare Maximization ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") can be weakened for the sufficiency direction. In particular,
it is enough that the probability measure μ\mu be absolutely continuous with respect to η\eta, for an optimal menu to the social welfare maximization problem ([1](https://arxiv.org/html/2602.09967v1#S3.E1 "Equation 1 ‣ Theorem 3.8. ‣ 3.2. Social Welfare Maximization ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) to be incentive efficient. For the converse, the necessity direction constructs η\eta as an equivalent probability measure to μ\mu (see the proof of Theorem [3.8](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem8 "Theorem 3.8. ‣ 3.2. Social Welfare Maximization ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") in Appendix [B.1](https://arxiv.org/html/2602.09967v1#A2.SS1 "B.1. Proof of Theorem 3.8 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")).

### 3.3. Retention Functions

In this section, we represent menus of contracts using retention functions, rather than indemnification functions. This reformulation will be used in the remainder of this paper.

For θ∈Θ\theta\in\Theta, the end-of-period wealth of the type-θ\theta agent is given by

|  |  |  |
| --- | --- | --- |
|  | −pθ−Lθ+Iθ​(Lθ)=−pθ−Rθ​(Lθ),-p\_{\theta}-L\_{\theta}+I\_{\theta}(L\_{\theta})=-p\_{\theta}-R\_{\theta}(L\_{\theta}), |  |

where Rθ​(Lθ):=Lθ−Iθ​(Lθ)≥0R\_{\theta}(L\_{\theta}):=L\_{\theta}-I\_{\theta}(L\_{\theta})\geq 0 is the loss retained by the type-θ\theta agent, that is the part of the agent’s loss LθL\_{\theta} that is not covered by the insurer. The insurer’s end-of-period wealth after receiving pθp\_{\theta} from the type-θ\theta agent in exchange for Iθ​(Lθ)I\_{\theta}(L\_{\theta}), is given by

|  |  |  |
| --- | --- | --- |
|  | pθ−Iθ​(Lθ)=pθ−(Lθ−Rθ​(Lθ)).p\_{\theta}-I\_{\theta}(L\_{\theta})=p\_{\theta}-(L\_{\theta}-R\_{\theta}(L\_{\theta})). |  |

###### Remark 3.10.

An indemnity function II belongs to ℐ\mathcal{I} if and only if the associated retention function RR belongs to the set

|  |  |  |
| --- | --- | --- |
|  | ℛ={R:[0,L¯]→[0,L¯];R​(0)=0, 0≤∂R∂l≤1}.\mathcal{R}=\left\{R:[0,\bar{L}]\rightarrow[0,\bar{L}];\ R(0)=0,\ 0\leq\frac{\partial R}{\partial l}\leq 1\right\}. |  |

Definitions [3.3](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem3 "Definition 3.3. ‣ 3.1. Incentive Pareto Optimality ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), [3.4](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem4 "Definition 3.4. ‣ 3.1. Incentive Pareto Optimality ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), and [3.5](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem5 "Definition 3.5. ‣ 3.1. Incentive Pareto Optimality ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") can be restated using a menu of contracts (Rθ,pθ)θ∈Θ(R\_{\theta},p\_{\theta})\_{\theta\in\Theta}, where retention functions are taken to be in ℛ\mathcal{R}. Since Iθ​(Lθ)=Lθ−Rθ​(Lθ)I\_{\theta}(L\_{\theta})=L\_{\theta}-R\_{\theta}(L\_{\theta}) for each θ∈Θ\theta\in\Theta, we can write

|  |  |  |  |
| --- | --- | --- | --- |
|  | Uθ​(Iθ,pθ)=Uθ​(Lθ−Rθ​(Lθ),pθ):=U~θ​(Rθ,pθ),andU\_{\theta}(I\_{\theta},p\_{\theta})=U\_{\theta}(L\_{\theta}-R\_{\theta}(L\_{\theta}),p\_{\theta}):=\widetilde{U}\_{\theta}(R\_{\theta},p\_{\theta}),\ \text{and} |  | (2) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vθ​(Iθ,pθ)=Vθ​(Lθ−Rθ​(Lθ),pθ):=V~θ​(Rθ,pθ).V\_{\theta}(I\_{\theta},p\_{\theta})=V\_{\theta}(L\_{\theta}-R\_{\theta}(L\_{\theta}),p\_{\theta}):=\widetilde{V}\_{\theta}(R\_{\theta},p\_{\theta}). |  | (3) |

###### Remark 3.11.

Theorem [3.8](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem8 "Theorem 3.8. ‣ 3.2. Social Welfare Maximization ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") can be equivalently stated in terms of menus of contracts of the form (Rθ,pθ)θ∈Θ∈ℐ​ℛ∩ℐ​𝒞(R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{R}\cap\mathcal{I}\mathcal{C} using utility functionals U~θ​(Rθ,pθ)\widetilde{U}\_{\theta}(R\_{\theta},p\_{\theta}) and V~θ​(Rθ,pθ)\widetilde{V}\_{\theta}(R\_{\theta},p\_{\theta}) defined in ([2](https://arxiv.org/html/2602.09967v1#S3.E2 "Equation 2 ‣ 3.3. Retention Functions ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) and ([3](https://arxiv.org/html/2602.09967v1#S3.E3 "Equation 3 ‣ 3.3. Retention Functions ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")), respectively.

## 4. The Case of Dual Utilities

So far, the characterization of incentive efficiency in Theorem [3.8](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem8 "Theorem 3.8. ‣ 3.2. Social Welfare Maximization ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), which can be restated using menus of retentions by Remark [3.11](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem11 "Remark 3.11. ‣ 3.3. Retention Functions ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), has been established for general concave utility functionals. In this section, we specialize this general framework to Yaari’s Dual Utilities, and we provide a crisper characterization of the structure of these efficient menus.

### 4.1. Dual Utility Framework

The Dual Utility of Yaari ([1987](https://arxiv.org/html/2602.09967v1#bib.bib69 "The dual theory of choice under risk")) is defined as a Choquet integral with respect to a distorted probability.

###### Definition 4.1.

For a given random variable XX, the dual utility of XX is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | D​U​(X)\displaystyle DU(X) | =∫X​𝑑g∘ℙ:=∫−∞0(g​(1−ℙ​(X≤x))−1)​𝑑x+∫0+∞g​(1−ℙ​(X≤x))​𝑑x,\displaystyle=\int Xdg\circ\mathbb{P}:=\int\_{-\infty}^{0}\bigg(g\big(1-\mathbb{P}(X\leq x)\big)-1\bigg)dx+\int\_{0}^{+\infty}g\big(1-\mathbb{P}(X\leq x)\big)dx, |  |

where g:[0,1]→[0,1]g:[0,1]\rightarrow[0,1] is a distortion function, that is, an increasing function with g​(0)=0g(0)=0 and g​(1)=1g(1)=1.

###### Definition 4.2.

Let g1g\_{1} and g2g\_{2} be two distortion functions. We say that g1g\_{1} dominates g2g\_{2} if:

|  |  |  |
| --- | --- | --- |
|  | g1​(t)≥g2​(t),for all t∈[0,1].g\_{1}(t)\geq g\_{2}(t),\ \text{for all $t\in[0,1]$}. |  |

Unlike Expected Utility Theory, where risk aversion is captured by the curvature of the utility function, in Rank-Dependent Utility (RDU – e.g., Quiggin ([1993](https://arxiv.org/html/2602.09967v1#bib.bib71 "Generalized expected utility theory: the rank-dependent model"))), both the utility function and the distortion function contribute to risk aversion (e.g., Chew et al. ([1987](https://arxiv.org/html/2602.09967v1#bib.bib70 "Risk Aversion in the Theory of Expected Utility with Rank Dependent Pobabilities"))). Yaari’s Dual Utility is a special case of RDU, in which the utility function is linear and risk aversion is captured entirely by the distortion function. Hence, in our setting, strong risk aversion is equivalent to the distortion function gg being convex, and weak risk aversion requires g​(x)≤xg(x)\leq x, for all x∈[0,1]x\in[0,1]. See, for instance, Quiggin ([1993](https://arxiv.org/html/2602.09967v1#bib.bib71 "Generalized expected utility theory: the rank-dependent model")), Yaari ([1987](https://arxiv.org/html/2602.09967v1#bib.bib69 "The dual theory of choice under risk")), Chateauneuf and Cohen ([1994](https://arxiv.org/html/2602.09967v1#bib.bib1 "Risk seeking with diminishing marginal utility in a non-expected utility model")), or Chew et al. ([1987](https://arxiv.org/html/2602.09967v1#bib.bib70 "Risk Aversion in the Theory of Expected Utility with Rank Dependent Pobabilities")).

Moreover, it follows from Quiggin ([1993](https://arxiv.org/html/2602.09967v1#bib.bib71 "Generalized expected utility theory: the rank-dependent model")) and Ghossoub and He ([2021](https://arxiv.org/html/2602.09967v1#bib.bib72 "Comparative risk aversion in rdeu with applications to optimal underwriting of securities issuance")) that weak risk aversion in both RDU and DU can be characterized by the dominance relation between probability weighting functions. Specifically, if g1g\_{1} and g2g\_{2} are two distortion functions with associated Dual Utilities D​U1{DU}\_{1} and D​U2{DU}\_{2}, and if g1g\_{1} dominates g2g\_{2} in the sense of Definition [4.2](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem2 "Definition 4.2. ‣ 4.1. Dual Utility Framework ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), then D​U2{DU}\_{2} is weakly more risk averse than D​U1{DU}\_{1}.

In this section, we make the following assumptions on the utility functionals.

###### Assumption 4.3.

For each θ∈Θ\theta\in\Theta, the type-θ\theta agent has preferences that admit a representation in terms of a Yaari Dual Utility:

|  |  |  |
| --- | --- | --- |
|  | D​Uθ​(⋅)=∫⋅d​gθ∘ℙ,where gθ denotes the type θ’s distortion function.DU\_{\theta}(\cdot)=\int\cdot\,\,d\ g\_{\theta}\circ\mathbb{P},\ \text{where $g\_{\theta}$ denotes the type $\theta$'s distortion function.} |  |

Similarly, the monopolistic insurer’s preferences admit a representation in terms of the following Yaari Dual Utility functional:

|  |  |  |
| --- | --- | --- |
|  | D​UI​n​(⋅)=∫⋅d​gI​n∘ℙ,where gI​n denotes the insurer’s distortion function.DU^{In}(\cdot)=\int\cdot\ d\ g^{In}\circ\mathbb{P},\ \text{where $g^{In}$ denotes the insurer's distortion function.} |  |

###### Assumption 4.4.

For each t∈[0,1]t\in[0,1], and for all θ∈Θ\theta\in\Theta,

|  |  |  |
| --- | --- | --- |
|  | gI​n​(t)≥gθ​(t).g^{In}(t)\geq g\_{\theta}(t). |  |

Assumption [4.4](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem4 "Assumption 4.4. ‣ 4.1. Dual Utility Framework ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") states that the insurer’s distortion function gI​ng^{In} dominates each type’s distortion function gθg\_{\theta} for all θ∈Θ\theta\in\Theta. Consequently, D​UθDU\_{\theta} for each type-θ\theta agent is weakly more risk averse than D​UI​nDU^{In} of the monopolistic insurer.

Dual utilities are translation invariant, meaning that for any random variable XX and any constant cc, D​U​(X+c)=D​U​(X)+cDU(X+c)=DU(X)+c. The end-of-period utility of a type-θ\theta agent is therefore given by:

|  |  |  |
| --- | --- | --- |
|  | Uθ​(Rθ,pθ)=D​Uθ​(−pθ−Rθ​(Lθ))=−pθ+D​Uθ​(−Rθ​(Lθ)).U\_{\theta}(R\_{\theta},p\_{\theta})={DU}\_{\theta}(-p\_{\theta}-R\_{\theta}(L\_{\theta}))=-p\_{\theta}+{DU}\_{\theta}(-R\_{\theta}(L\_{\theta})). |  |

Since −Rθ​(Lθ)≤0-R\_{\theta}(L\_{\theta})\leq 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Uθ​(Rθ,pθ)\displaystyle U\_{\theta}(R\_{\theta},p\_{\theta}) | =−pθ+∫−∞0[gθ​(1−ℙ​(−Rθ​(Lθ)≤x))−1]​𝑑x\displaystyle=-p\_{\theta}+\int\_{-\infty}^{0}\left[g\_{\theta}\big(1-\mathbb{P}(-R\_{\theta}(L\_{\theta})\leq x)\big)-1\right]\,dx |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−pθ−∫0+∞[1−gθ​(ℙ​(Rθ​(Lθ)≤l))]​𝑑l\displaystyle=-p\_{\theta}-\int\_{0}^{+\infty}\left[1-g\_{\theta}\big(\mathbb{P}(R\_{\theta}(L\_{\theta})\leq l)\big)\right]\,dl |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−pθ−∫0L¯[1−gθ​(Fθ​(l))]​∂Rθ​(l)∂l​𝑑l,\displaystyle=-p\_{\theta}-\int\_{0}^{\bar{L}}\left[1-g\_{\theta}\big(F\_{\theta}(l)\big)\right]\,\frac{\partial R\_{\theta}(l)}{\partial l}\,dl, |  |

where Fθ​(l):=ℙ​(Lθ≤l)F\_{\theta}(l):=\mathbb{P}(L\_{\theta}\leq l) denotes the cumulative loss distribution function, for a given θ∈Θ\theta\in\Theta.

In the case of no insurance, the dual utility of a type-θ\theta agent is given by:

|  |  |  |
| --- | --- | --- |
|  | Uθ​(Lθ,0)=D​Uθ​(−Lθ)=−∫0L¯[1−gθ​(Fθ​(l))]​𝑑l.U\_{\theta}(L\_{\theta},0)=DU\_{\theta}(-L\_{\theta})=-\int\_{0}^{\bar{L}}\left[1-g\_{\theta}\left(F\_{\theta}(l)\right)\right]\ dl. |  |

Additionally, by translation invariance, the insurer’s end-of-period utility from providing a contract (Rθ,pθ)(R\_{\theta},p\_{\theta}) to the type-θ\theta agent is given by

|  |  |  |
| --- | --- | --- |
|  | Vθ​(Rθ,pθ)=D​UI​n​(pθ−Lθ+Rθ​(Lθ))=pθ+D​UI​n​(−Lθ+Rθ​(Lθ)),V\_{\theta}(R\_{\theta},p\_{\theta})={DU}^{In}(p\_{\theta}-L\_{\theta}+R\_{\theta}(L\_{\theta}))=p\_{\theta}+{DU}^{In}(-L\_{\theta}+R\_{\theta}(L\_{\theta})), |  |

Since −Lθ+Rθ​(Lθ)=−Iθ​(Lθ)≤0-L\_{\theta}+R\_{\theta}(L\_{\theta})=-I\_{\theta}(L\_{\theta})\leq 0, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vθ​(Rθ,pθ)\displaystyle V\_{\theta}(R\_{\theta},p\_{\theta}) | =pθ−∫0+∞[1−gI​n​(ℙ​(Lθ−Rθ​(Lθ)≤l))]​𝑑l\displaystyle=p\_{\theta}-\int\_{0}^{+\infty}\left[1-g^{In}(\mathbb{P}(L\_{\theta}-R\_{\theta}(L\_{\theta})\leq l))\right]\,dl |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =pθ−∫0Iθ​(L¯θ)[1−gI​n​(ℙ​(Iθ​(Lθ)≤l))]​𝑑l\displaystyle=p\_{\theta}-\int\_{0}^{I\_{\theta}(\bar{L}\_{\theta})}\left[1-g^{In}(\mathbb{P}(I\_{\theta}(L\_{\theta})\leq l))\right]\,dl |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =pθ−∫0L¯[1−gI​n​(Fθ​(l))]​(1−∂Rθ​(l)∂l)​𝑑l.\displaystyle=p\_{\theta}-\int\_{0}^{\bar{L}}\left[1-g^{In}(F\_{\theta}(l))\right]\left(1-\frac{\partial R\_{\theta}(l)}{\partial l}\right)\,dl. |  |

###### Proposition 4.5.

A menu of contracts (Rθ,pθ)θ∈Θ(R\_{\theta},p\_{\theta})\_{\theta\in\Theta} is individually rational if and only if it satisfies:

1. (1)

   ∫ΘVθ​(Rθ,pθ)​𝑑μ≥0\displaystyle\int\_{\Theta}V\_{\theta}(R\_{\theta},p\_{\theta})d\mu\geq 0; and,
2. (2)

   pθ≤∫0L¯[1−gθ​(Fθ​(l))]​[1−∂Rθ​(l)∂l]​𝑑lp\_{\theta}\leq\displaystyle\int\_{0}^{\bar{L}}\left[1-g\_{\theta}(F\_{\theta}(l))\right]\left[1-\frac{\partial R\_{\theta}(l)}{\partial l}\right]\,dl, for all θ∈Θ\theta\in\Theta.

Proposition [4.5](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem5 "Proposition 4.5. ‣ 4.1. Dual Utility Framework ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") is an immediate implication of the definition of individual rationality. Specifically, a menu of contracts is individually rational if and only if the insurer’s aggregate utility is non-negative and the associated premium does not exceed a certain upper bound at which the agent is indifferent.

###### Lemma 4.6.

Under Yaari’s Dual Utility framework, Assumption [3.7](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem7 "Assumption 3.7. ‣ 3.2. Social Welfare Maximization ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") is satisfied for every menu of contracts (Rθ,pθ)θ∈Θ∈ℐ​ℛ∩ℐ​𝒞(R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{R}\cap\mathcal{I}\mathcal{C}.

###### Proof.

The proof can be found in Appendix [B.3](https://arxiv.org/html/2602.09967v1#A2.SS3 "B.3. Proof of Lemma 4.6 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
∎

For a fixed type θ∈Θ\theta\in\Theta, the insurer’s and the agent’s utilities are both affine in the contract variables (Rθ,pθ)(R\_{\theta},p\_{\theta}), and therefore concave. Hence, Assumption [3.6](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem6 "Assumption 3.6. ‣ 3.2. Social Welfare Maximization ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") is satisfied. Together with Lemma [4.6](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem6 "Lemma 4.6. ‣ 4.1. Dual Utility Framework ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), Theorem [3.8](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem8 "Theorem 3.8. ‣ 3.2. Social Welfare Maximization ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") applies in this setting.

### 4.2. Type Ordering under Dual Utility

In this setting, the agent’s type affects their loss distribution and risk attitude.
The following assumptions impose an ordering on the type space Θ\Theta.

###### Assumption 4.7.

Let LθL\_{\theta} to be the loss faced by a type-θ\theta agent, with cumulative distribution function FθF\_{\theta}.

1. (1)

   The family of cumulative distribution functions {Fθ}θ∈Θ\{F\_{\theta}\}\_{\theta\in\Theta} is uniformly Lipschitz continuous in θ\theta, with common Lipshcitz constant c′<+∞c^{\prime}<+\infty.
2. (2)

   Type-dependent losses LθL\_{\theta} are ordered in the sense of first order stochastic dominance. Specifically, for θ1<θ2\theta\_{1}<\theta\_{2}, we have Lθ1≼F​O​S​DLθ2L\_{\theta\_{1}}\preccurlyeq\_{FOSD}L\_{\theta\_{2}}, that is, Fθ1​(l)≥Fθ2​(l)F\_{\theta\_{1}}(l)\geq F\_{\theta\_{2}}(l), for all l∈[0,L¯]l\in[0,\bar{L}]. Equivalently,

   |  |  |  |
   | --- | --- | --- |
   |  | ∂Fθ​(l)∂θ≤0,∀l.\frac{\partial F\_{\theta}(l)}{\partial\theta}\leq 0,\ \forall\,l. |  |

Assumption [4.7](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem7 "Assumption 4.7. ‣ 4.2. Type Ordering under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")-([2](https://arxiv.org/html/2602.09967v1#S4.I2.i2 "Item 2 ‣ Assumption 4.7. ‣ 4.2. Type Ordering under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) states that larger types face a stochastically larger loss, in the sense of first-order dominance.

###### Assumption 4.8.

1. (1)

   {gθ​(t)}θ∈Θ\{g\_{\theta}(t)\}\_{\theta\in\Theta} is uniformly Lipschitz continuous in t∈[0,1]t\in[0,1] with common Lipschitz constant δ<+∞\delta<+\infty. That is, for each θ∈Θ\theta\in\Theta,

   |  |  |  |
   | --- | --- | --- |
   |  | gθ′​(t)≤δ,∀t∈[0,1].g^{\prime}\_{\theta}(t)\leq\delta,\ \forall\,t\in[0,1]. |  |
2. (2)

   {gθ}θ∈Θ\{g\_{\theta}\}\_{\theta\in\Theta} is uniformly Lipschitz continuous in θ\theta, with common Lipschitz constant c<+∞c<+\infty.
3. (3)

   The type space Θ\Theta is ordered such that:

   |  |  |  |
   | --- | --- | --- |
   |  | ∂gθ​(t)∂θ≤0, for t∈(0,1). \frac{\partial g\_{\theta}(t)}{\partial\theta}\leq 0,\ \text{ for $t\in(0,1)$. } |  |

Assumption [4.8](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem8 "Assumption 4.8. ‣ 4.2. Type Ordering under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")-([3](https://arxiv.org/html/2602.09967v1#S4.I3.i3 "Item 3 ‣ Assumption 4.8. ‣ 4.2. Type Ordering under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) states that the distortion function gθg\_{\theta} is pointwise smaller for larger values of θ\theta. If θ1,θ2∈Θ\theta\_{1},\theta\_{2}\in\Theta are such that θ1≤θ2\theta\_{1}\leq\theta\_{2}, then gθ1​(t)≥gθ2​(t)g\_{\theta\_{1}}(t)\geq g\_{\theta\_{2}}(t) for t∈[0,1]t\in[0,1]. This means that the type θ2\theta\_{2}-agent is more weakly risk averse than the type θ1\theta\_{1}-agent.

Assumption [4.7](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem7 "Assumption 4.7. ‣ 4.2. Type Ordering under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")-([2](https://arxiv.org/html/2602.09967v1#S4.I2.i2 "Item 2 ‣ Assumption 4.7. ‣ 4.2. Type Ordering under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) and Assumption [4.8](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem8 "Assumption 4.8. ‣ 4.2. Type Ordering under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")-([3](https://arxiv.org/html/2602.09967v1#S4.I3.i3 "Item 3 ‣ Assumption 4.8. ‣ 4.2. Type Ordering under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) state that the type space Θ\Theta is ordered such that higher types (larger values of θ\theta) are more (weakly) risk averse and face stochastically larger losses.

###### Remark 4.9.

Note that gθ​(Fθ​(l))g\_{\theta}\big(F\_{\theta}(l)\big) can be written as the composed function (gθ∘Fθ)​(l)\big(g\_{\theta}\circ F\_{\theta}\big)(l), for θ∈Θ\theta\in\Theta and l∈[0,L¯θ]⊆[0,L¯]l\in[0,\bar{L}\_{\theta}]\subseteq[0,\bar{L}]. Hence,

|  |  |  |
| --- | --- | --- |
|  | ∂∂θ​[gθ​(Fθ​(l))]​∂gθ∂θ​(Fθ​(l))+gθ′​(Fθ​(l))​∂Fθ​(l)∂θ,\displaystyle\frac{\partial}{\partial\theta}\left[g\_{\theta}\big(F\_{\theta}(l)\big)\right]\frac{\partial g\_{\theta}}{\partial\theta}\big(F\_{\theta}(l)\big)+g^{\prime}\_{\theta}\big(F\_{\theta}(l)\big)\frac{\partial F\_{\theta}(l)}{\partial\theta}, |  |

where gθ′​(Fθ​(l)):=∂gθ∂t​(Fθ​(l))|t=Fθ​(l)g^{\prime}\_{\theta}\big(F\_{\theta}(l)\big):=\frac{\partial g\_{\theta}}{\partial t}\big(F\_{\theta}(l)\big)\bigg|\_{t=F\_{\theta}(l)}.

The composed function gθ∘Fθg\_{\theta}\circ F\_{\theta} is monotone in θ\theta for all ll:

|  |  |  |
| --- | --- | --- |
|  | ∂∂θ​[gθ​(Fθ​(l))]≤0,\frac{\partial}{\partial\theta}\left[g\_{\theta}\big(F\_{\theta}(l)\big)\right]\leq 0, |  |

which follows from Assumption [4.7](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem7 "Assumption 4.7. ‣ 4.2. Type Ordering under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") and Assumption [4.8](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem8 "Assumption 4.8. ‣ 4.2. Type Ordering under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), and since gθ​(t)g\_{\theta}(t) is increasing in tt for all θ\theta. Hence, as θ\theta increases, the composition gθ​(Fθ​(l))g\_{\theta}\big(F\_{\theta}(l)\big) decreases, for all ll. If θ1,θ2∈Θ\theta\_{1},\theta\_{2}\in\Theta are such that θ1≤θ2\theta\_{1}\leq\theta\_{2}, then gθ1​(Fθ1​(l))≥gθ2​(Fθ2​(l))g\_{\theta\_{1}}\big(F\_{\theta\_{1}}(l)\big)\geq g\_{\theta\_{2}}\big(F\_{\theta\_{2}}(l)\big), for all ll. In other words, higher types, who are more risk averse, assign lower distorted cumulative distribution functions to the loss, meaning that they distort their own perceived loss distributions more pessimistically.

### 4.3. Solution Characterization Under Dual Utility

Consider an incentive efficient menu of contracts (Rθ∗,pθ∗)θ∈Θ(R^{\*}\_{\theta},p^{\*}\_{\theta})\_{\theta\in\Theta}. It follows from Theorem [3.8](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem8 "Theorem 3.8. ‣ 3.2. Social Welfare Maximization ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") and Remark [3.11](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem11 "Remark 3.11. ‣ 3.3. Retention Functions ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") that there exists a probability measure η\eta equivalent to μ\mu, and some α∈(0,1]\alpha\in(0,1], such that (Rθ∗,pθ∗)θ∈Θ(R^{\*}\_{\theta},p^{\*}\_{\theta})\_{\theta\in\Theta} is optimal for

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup(Rθ,pθ)θ∈Θ∈ℐ​ℛ∩ℐ​𝒞​{α​∫ΘUθ​(Rθ,pθ)​𝑑η+(1−α)​∫ΘVθ​(Rθ,pθ)​𝑑μ}.\underset{(R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{R}\cap\mathcal{I}\mathcal{C}}{\sup}\left\{\alpha\int\_{\Theta}U\_{\theta}(R\_{\theta},p\_{\theta})\,\,d\eta+(1-\alpha)\int\_{\Theta}V\_{\theta}(R\_{\theta},p\_{\theta})\,\,d\mu\right\}. |  | (4) |

We aim to characterize the solutions of Problem ([4](https://arxiv.org/html/2602.09967v1#S4.E4 "Equation 4 ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")), under the Yaari’s Dual Utility framework. We start by presenting preliminary results about individual rationality and incentive compatibility. The proofs of all results are provided in Appendix [B](https://arxiv.org/html/2602.09967v1#A2 "Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").

###### Proposition 4.10.

If a menu of contracts (Rθ,pθ)θ∈Θ(R\_{\theta},p\_{\theta})\_{\theta\in\Theta} is incentive compatible, then for any θ∈Θ\theta\in\Theta, the premium pθp\_{\theta} is of the following form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | pθ\displaystyle p\_{\theta}\ | =pθ¯+∫0L¯[1−gθ¯​(Fθ¯​(l))]​∂Rθ¯​(l)∂l​𝑑l−∫θ¯θ∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​∂Rs​(l)∂l​𝑑l​𝑑s\displaystyle=p\_{\underline{\theta}}+\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\right]\,\,\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}\,dl-\int\_{\underline{\theta}}^{\theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\frac{\partial R\_{s}(l)}{\partial l}\,dl\,ds |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −∫0L¯[1−gθ​(Fθ​(l))]​∂Rθ​(l)∂l​𝑑l.\displaystyle\quad-\int\_{0}^{\bar{L}}\left[1-g\_{\theta}\big(F\_{\theta}(l)\big)\right]\,\,\frac{\partial R\_{\theta}(l)}{\partial l}\,dl. |  | (5) |

###### Definition 4.11.

A collection of retention functions {Rθ}θ∈Θ\{R\_{\theta}\}\_{\theta\in\Theta} is submodular if ∂Rθ​(l)∂l\frac{\partial R\_{\theta}(l)}{\partial l} is non-increasing in θ\theta, for all l∈[0,L¯θ]⊆[0,L¯]l\in[0,\bar{L}\_{\theta}]\subseteq[0,\bar{L}]. That is,
∂2Rθ​(l)∂θ​∂l≤0.\frac{\partial^{2}R\_{\theta}(l)}{\partial\theta\,\,\partial l}\leq 0.

As the agent’s type increases (representing more risk aversion), higher types are willing to pay higher premia for more coverage than less risk averse types are unwilling to pay.
Submodularity of retention functions provides a natural alignment between the agent’s risk attitude and the structure of coverage.
Definition [4.11](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem11 "Definition 4.11. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") says that if θ1,θ2∈Θ\theta\_{1},\theta\_{2}\in\Theta are such that θ1≤θ2\theta\_{1}\leq\theta\_{2}, then

|  |  |  |
| --- | --- | --- |
|  | ∂Rθ1​(l)∂l≥∂Rθ2​(l)∂l,∀l.\frac{\partial R\_{\theta\_{1}}(l)}{\partial l}\geq\frac{\partial R\_{\theta\_{2}}(l)}{\partial l},\ \forall l. |  |

This ensures that coverage becomes progressively more generous as risk aversion increases, higher types receive greater coverage, transferring a larger portion of loss to the insurer and retaining less to themselves. Consequently, each type pays a premium consistent with their own preferences.

###### Proposition 4.12.

Consider a submodular collection of retention functions {Rθ}θ∈Θ\{R\_{\theta}\}\_{\theta\in\Theta}. Then a menu of contracts (Rθ,pθ)θ∈Θ(R\_{\theta},p\_{\theta})\_{\theta\in\Theta} is in ℐ​𝒞\mathcal{I}\mathcal{C} if and only if {pθ}θ∈Θ\{p\_{\theta}\}\_{\theta\in\Theta} satisfies ([4.10](https://arxiv.org/html/2602.09967v1#S4.Ex41 "Proposition 4.10. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")).

The following proposition shows that an incentive compatible menu is individually rational if and only if the contract offered to the lowest type is individually rational.

###### Proposition 4.13.

If (Rθ,pθ)θ∈Θ∈ℐ​𝒞(R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{C} is such that ∫ΘVθ​(Rθ,pθ)​𝑑μ≥0\int\_{\Theta}V\_{\theta}(R\_{\theta},p\_{\theta})d\mu\geq 0, then (Rθ,pθ)θ∈Θ∈ℐ​ℛ(R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{R} if and only if (Rθ¯,pθ¯)(R\_{\underline{\theta}},p\_{\underline{\theta}}) satisfies the agent’s participation (P1) of Definition [3.3](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem3 "Definition 3.3. ‣ 3.1. Incentive Pareto Optimality ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").

###### Corollary 4.14.

Assume that the collection of retention functions {Rθ}θ∈Θ\{R\_{\theta}\}\_{\theta\in\Theta} is submodular. Then (Rθ,pθ)θ∈Θ∈ℐ​ℛ∩ℐ​𝒞(R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{R}\cap\mathcal{I}\mathcal{C} if and only both of the following conditions hold:

1. (1)

   The premia {pθ}θ∈Θ\{p\_{\theta}\}\_{\theta\in\Theta} satisfy ([4.10](https://arxiv.org/html/2602.09967v1#S4.Ex41 "Proposition 4.10. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")), with

   |  |  |  |
   | --- | --- | --- |
   |  | pθ¯≤∫0L¯[  1−gθ¯​(Fθ¯​(l))]​[1−∂Rθ¯​(l)∂l]​𝑑l.p\_{\underline{\theta}}\leq\int\_{0}^{\bar{L}}\left[\,\,1-g\_{\underline{\theta}}(F\_{\underline{\theta}}(l))\,\,\right]\left[1-\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}\right]\,\,dl. |  |
2. (2)

   The insurer’s participation (P2) of Definition [3.3](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem3 "Definition 3.3. ‣ 3.1. Incentive Pareto Optimality ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") is satisfied. That is,

   |  |  |  |
   | --- | --- | --- |
   |  | ∫ΘVθ​(Rθ,pθ)​𝑑μ≥0.\int\_{\Theta}V\_{\theta}(R\_{\theta},p\_{\theta})d\mu\geq 0. |  |

Let QηQ\_{\eta} and Q¯η\bar{Q}\_{\eta} denote respectively the cumulative and decumulative distribution functions over types induced by the probability measure η\eta. That is,

|  |  |  |
| --- | --- | --- |
|  | Qη​(θ):=η​([θ¯,θ]),and​Q¯η​(θ):=η​((θ,θ¯]),∀θ∈Θ.Q\_{\eta}(\theta):=\eta([\underline{\theta},\theta]),\ \text{and}\ \bar{Q}\_{\eta}(\theta):=\eta((\theta,\bar{\theta}]),\ \forall\,\theta\in\Theta. |  |

###### Assumption 4.15.

For all θ∈Θ\theta\in\Theta,

|  |  |  |
| --- | --- | --- |
|  | q​(θ)Q¯​(θ)≥qη​(θ)Q¯η​(θ).\frac{q(\theta)}{\bar{Q}(\theta)}\geq\frac{q\_{\eta}(\theta)}{\bar{Q}\_{\eta}(\theta)}\,\,. |  |

Assumption [4.15](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem15 "Assumption 4.15. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") states that the hazard rate over types under μ\mu is greater than or equal to the hazard rate over types under η\eta.
Consequently, the distribution over types under μ\mu is smaller in the hazard rate order than the one under η\eta. Moreover, we can show that Assumption [4.15](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem15 "Assumption 4.15. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") implies that Q¯η​(θ)Q¯​(θ)\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)} is non-decreasing in θ∈Θ\theta\in\Theta. Indeed,

|  |  |  |
| --- | --- | --- |
|  | (Q¯η​(θ)Q¯​(θ))′=−qη​(θ)​Q¯​(θ)+q​(θ)​Q¯η​(θ)Q¯​(θ)2=Q¯η​(θ)Q¯​(θ)⋅[q​(θ)Q¯​(θ)−qη​(θ)Q¯η​(θ)]≥0,∀θ∈Θ.\left(\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)}\right)^{\prime}=\frac{-q\_{\eta}(\theta)\bar{Q}(\theta)+q(\theta)\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)^{2}}=\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)}\cdot\left[\frac{q(\theta)}{\bar{Q}(\theta)}-\frac{q\_{\eta}(\theta)}{\bar{Q}\_{\eta}(\theta)}\right]\geq 0\,,\,\,\forall\,\theta\in\Theta. |  |

###### Remark 4.16.

Note that, at θ=θ¯\theta=\underline{\theta},

|  |  |  |  |
| --- | --- | --- | --- |
|  | Q¯η​(θ)Q¯​(θ)|θ=θ¯=1.\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)}\bigg|\_{\theta=\underline{\theta}}=1. |  | (6) |

Moreover, at θ=θ¯\theta=\bar{\theta} and applying L’Hospital’s rule, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | Q¯η​(θ)Q¯​(θ)|θ=θ¯=limθ→θ¯​Q¯η​(θ)Q¯​(θ)=limθ→θ¯​−qη​(θ)−q​(θ)=qη​(θ¯)q​(θ¯).\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)}\bigg|\_{\theta=\bar{\theta}}=\underset{\theta\to\bar{\theta}}{\lim}\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)}=\underset{\theta\to\bar{\theta}}{\lim}\frac{-q\_{\eta}(\theta)}{-q(\theta)}=\frac{q\_{\eta}(\bar{\theta})}{q(\bar{\theta})}\,. |  | (7) |

Since Q¯η​(θ)Q¯​(θ)\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)} is non-decreasing in θ\theta, it then follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | qη​(θ¯)q​(θ¯)≥1.\frac{q\_{\eta}(\bar{\theta})}{q(\bar{\theta})}\geq 1. |  | (8) |

The following result provides a characterization of incentive efficient menus.

###### Theorem 4.17.

Let (Rθ∗,pθ∗)θ∈Θ∈ℐ​𝒫​𝒪⊆ℐ​ℛ∩ℐ​𝒞(R^{\*}\_{\theta},p^{\*}\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{P}\mathcal{O}\subseteq\mathcal{I}\mathcal{R}\cap\mathcal{I}\mathcal{C} be optimal for Problem ([4](https://arxiv.org/html/2602.09967v1#S4.E4 "Equation 4 ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")), and assume that the probability measure η\eta satisfies Assumption [4.15](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem15 "Assumption 4.15. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"). Then the optimal menu (Rθ∗,pθ∗)θ∈Θ(R^{\*}\_{\theta},p^{\*}\_{\theta})\_{\theta\in\Theta} can be characterized as follows:

1. (1)

   If α∈(0,q​(θ¯)qη​(θ¯)+q​(θ¯))\alpha\in\left(0,\frac{q(\bar{\theta})}{q\_{\eta}(\bar{\theta})+q(\bar{\theta})}\right), and if the function θ↦Jθ,η​(l)\theta\mapsto J\_{\theta,\eta}(l) is non-decreasing in θ\theta for all ll, then there exists a solution (Rθ∗,pθ∗)θ∈Θ\left(R^{\*}\_{\theta},p^{\*}\_{\theta}\right)\_{\theta\in\Theta} such that the optimal retention function is characterized using the marginal retention as follows:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∂Rθ∗​(l)∂l={0Jθ,η​(l)>0,∈[0,1]Jθ,η​(l)=0,1Jθ,η​(l)<0,\frac{\partial R^{\*}\_{\theta}(l)}{\partial l}=\begin{cases}0&J\_{\theta,\eta}(l)>0,\\ \in[0,1]&J\_{\theta,\eta}(l)=0,\\ 1&J\_{\theta,\eta}(l)<0,\end{cases} |  | (9) |

   where the function Jθ,η​(l)J\_{\theta,\eta}(l) is defined as:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Jθ,η​(l)\displaystyle J\_{\theta,\eta}(l) | =(1−α)​[gI​n​(Fθ​(l))−gθ​(Fθ​(l))]\displaystyle=(1-\alpha)\left[g^{In}(F\_{\theta}(l))-g\_{\theta}(F\_{\theta}(l))\right] |  |
   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  |  | +Q¯​(θ)q​(θ)​[∂gθ∂θ​(Fθ​(l))+gθ′​(Fθ​(l))​∂Fθ​(l)∂θ]​[(1−α)−α​Q¯η​(θ)Q¯​(θ)].\displaystyle+\frac{\bar{Q}(\theta)}{q(\theta)}\left[\frac{\partial g\_{\theta}}{\partial\theta}(F\_{\theta}(l))+g^{\prime}\_{\theta}(F\_{\theta}(l))\frac{\partial F\_{\theta}(l)}{\partial\theta}\right]\left[(1-\alpha)-\alpha\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)}\right]. |  | (10) |

   Additionally, the premia {pθ∗}θ∈Θ\{p^{\*}\_{\theta}\}\_{\theta\in\Theta} satisfy the following:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | pθ∗\displaystyle p^{\*}\_{\theta} | =∫0L¯[1−gθ¯​(Fθ¯​(l))]​𝑑l−∫θ¯θ∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​∂Rs∗​(l)∂l​𝑑l​𝑑s\displaystyle=\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\right]\,\,dl-\int\_{\underline{\theta}}^{\theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\frac{\partial R^{\*}\_{s}(l)}{\partial l}\ dl\,ds |  |
   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  |  | −∫0L¯[1−gθ​(Fθ​(l))]​∂Rθ∗​(l)∂l​𝑑l.\displaystyle\quad-\int\_{0}^{\bar{L}}\left[1-g\_{\theta}\big(F\_{\theta}(l)\big)\right]\,\,\frac{\partial R^{\*}\_{\theta}(l)}{\partial l}\,\,dl. |  | (11) |
2. (2)

   If α∈[q​(θ¯)qη​(θ¯)+q​(θ¯),12]\alpha\in\left[\frac{q(\bar{\theta})}{q\_{\eta}(\bar{\theta})+q(\bar{\theta})},\frac{1}{2}\right], and if the function θ↦Jθ,η​(l)\theta\mapsto J\_{\theta,\eta}(l) is non-decreasing in θ\theta for all ll, then:

   1. (i)

      If θ<θα\theta<\theta\_{\alpha}, then Rθ∗R^{\*}\_{\theta} follows the form given in ([9](https://arxiv.org/html/2602.09967v1#S4.E9 "Equation 9 ‣ Item 1 ‣ Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"));
   2. (ii)

      If θ≥θα\theta\geq\theta\_{\alpha}, then Rθ∗=0R^{\*}\_{\theta}=0,

   where θα\theta\_{\alpha} is determined by the equation Q¯η​(θα)Q¯​(θα)=1−αα\frac{\bar{Q}\_{\eta}(\theta\_{\alpha})}{\bar{Q}(\theta\_{\alpha})}=\frac{1-\alpha}{\alpha}. The premia {pθ∗}θ∈Θ\{p^{\*}\_{\theta}\}\_{\theta\in\Theta} satisfy ([1](https://arxiv.org/html/2602.09967v1#S4.Ex49 "Item 1 ‣ Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")).
3. (3)

   If α∈(12,1]\alpha\in\left(\frac{1}{2},1\right], then Rθ∗=0R^{\*}\_{\theta}=0 and pθ∗=0p^{\*}\_{\theta}=0, for all θ∈Θ\theta\in\Theta.

Moreover, the collection of optimal retention functions {Rθ∗}θ∈Θ\{R^{\*}\_{\theta}\}\_{\theta\in\Theta} is submodular for a given η\eta and α\alpha.

###### Proof.

The proof is provided in Appendix [B.8](https://arxiv.org/html/2602.09967v1#A2.SS8 "B.8. Proof of Theorem 4.17 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
∎

Theorem [4.17](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem17 "Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") shows that the structure of incentive-efficient menus depends on the value of the social weight α\alpha.
Specifically, when α≤12\alpha\leq\frac{1}{2} and θ<θα\theta<\theta\_{\alpha}, that is when α\alpha satisfies cases ([1](https://arxiv.org/html/2602.09967v1#S4.I10.i1 "Item 1 ‣ Proposition 4.25. ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) and ([2](https://arxiv.org/html/2602.09967v1#S4.I10.i2 "Item 2 ‣ Proposition 4.25. ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"))-(i), a separating equilibrium emerges. The optimal retention function is submodular and is characterized by the marginal retention in ([9](https://arxiv.org/html/2602.09967v1#S4.E9 "Equation 9 ‣ Item 1 ‣ Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) ensuring that higher types receive more coverage.
If α\alpha satisfies case ([2](https://arxiv.org/html/2602.09967v1#S4.I10.i2 "Item 2 ‣ Proposition 4.25. ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"))-(ii), full coverage is offered to agent types θ≥θα\theta\geq\theta\_{\alpha}.
Finally, when α\alpha satisfies case ([3](https://arxiv.org/html/2602.09967v1#S4.I10.i3 "Item 3 ‣ Proposition 4.25. ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")), that is if a high weight is placed on agent welfare, a pooling equilibrium arises and all agent types are offered full coverage.

### 4.4. On the Monotonicity of the Function θ↦Jθ,η​(l)\theta\mapsto J\_{\theta,\eta}(l)

Consider now cases ([1](https://arxiv.org/html/2602.09967v1#S4.I10.i1 "Item 1 ‣ Proposition 4.25. ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) and ([2](https://arxiv.org/html/2602.09967v1#S4.I10.i2 "Item 2 ‣ Proposition 4.25. ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"))-(i), where α≤12\alpha\leq\frac{1}{2} and θ<θα\theta<\theta\_{\alpha}.
To achieve the separating layered equilibrium described by the marginal retention functions given in ([9](https://arxiv.org/html/2602.09967v1#S4.E9 "Equation 9 ‣ Item 1 ‣ Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")), we require the function Jθ,η​(l)J\_{\theta,\eta}(l) defined in ([1](https://arxiv.org/html/2602.09967v1#S4.Ex48 "Item 1 ‣ Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) to be non-decreasing in θ\theta. We examine in this section some sufficient condition for this monotonocity.

First, note that in this region, 1−α−α​Q¯η​(θ)Q¯​(θ)≥01-\alpha-\alpha\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)}\geq 0. Moreover, the partial derivative of Jθ,η​(l)J\_{\theta,\eta}(l) with respect to θ\theta is given by:

|  |  |  |
| --- | --- | --- |
|  | ∂Jθ,η​(l)∂θ=∂gθ∂θ​(Fθ​(l))​[(1−α)​((Q¯​(θ)q​(θ))′−1)−α​(Q¯​(θ)q​(θ)​Q¯η​(θ)Q¯​(θ))′]\displaystyle\frac{\partial J\_{\theta,\eta}(l)}{\partial\theta}=\frac{\partial g\_{\theta}}{\partial\theta}(F\_{\theta}(l))\,\left[(1-\alpha)\left(\left(\frac{\bar{Q}(\theta)}{q(\theta)}\right)^{\prime}-1\right)-\alpha\left(\frac{\bar{Q}(\theta)}{q(\theta)}\,\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)}\right)^{\prime}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | +(1−α)​∂Fθ​(l)∂θ​[gθ′​(Fθ​(l))​((Q¯​(θ)q​(θ))′−1)]+(1−α)​∂Fθ​(l)∂θ​[Q¯​(θ)q​(θ)​∂2gθ∂θ​∂t​(Fθ​(l))+gI​n⁣′​(Fθ​(l))]\displaystyle\quad+(1-\alpha)\frac{\partial F\_{\theta}(l)}{\partial\theta}\,\left[g^{\prime}\_{\theta}(F\_{\theta}(l))\left(\left(\frac{\bar{Q}(\theta)}{q(\theta)}\right)^{\prime}-1\right)\right]+(1-\alpha)\frac{\partial F\_{\theta}(l)}{\partial\theta}\,\left[\frac{\bar{Q}(\theta)}{q(\theta)}\frac{\partial^{2}g\_{\theta}}{\partial\theta\,\,\partial t}(F\_{\theta}(l))+g^{In\ \prime}(F\_{\theta}(l))\right] |  |
|  |  |  |
| --- | --- | --- |
|  | −α​∂Fθ​(l)∂θ​[gθ′​(Fθ​(l))​(Q¯​(θ)q​(θ)​Q¯η​(θ)Q¯​(θ))′+Q¯η​(θ)Q¯​(θ)​Q¯​(θ)q​(θ)​∂2gθ∂θ​∂t​(Fθ​(l))]\displaystyle\quad-\alpha\frac{\partial F\_{\theta}(l)}{\partial\theta}\,\left[g^{\prime}\_{\theta}(F\_{\theta}(l))\left(\frac{\bar{Q}(\theta)}{q(\theta)}\,\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)}\right)^{\prime}+\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)}\frac{\bar{Q}(\theta)}{q(\theta)}\frac{\partial^{2}g\_{\theta}}{\partial\theta\,\,\partial t}(F\_{\theta}(l))\right] |  |
|  |  |  |
| --- | --- | --- |
|  | +[1−α−α​Q¯η​(θ)Q¯​(θ)]​Q¯​(θ)q​(θ)​[gθ′​(Fθ​(l))​∂2Fθ​(l)∂θ2+∂2gθ∂θ2​(Fθ​(l))+gθ′′​(Fθ​(l))​(∂Fθ​(l)∂θ)2].\displaystyle\quad+\left[1-\alpha-\alpha\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)}\right]\frac{\bar{Q}(\theta)}{q(\theta)}\,\left[g^{\prime}\_{\theta}(F\_{\theta}(l))\frac{\partial^{2}F\_{\theta}(l)}{\partial\theta^{2}}+\frac{\partial^{2}g\_{\theta}}{\partial\theta^{2}}(F\_{\theta}(l))+g^{\prime\prime}\_{\theta}(F\_{\theta}(l))\left(\frac{\partial F\_{\theta}(l)}{\partial\theta}\right)^{2}\ \right]. |  |

Using the monotonicity implications of Assumptions [4.7](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem7 "Assumption 4.7. ‣ 4.2. Type Ordering under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), [4.8](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem8 "Assumption 4.8. ‣ 4.2. Type Ordering under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), and [4.15](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem15 "Assumption 4.15. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), when α\alpha satisfies cases ([1](https://arxiv.org/html/2602.09967v1#S4.I10.i1 "Item 1 ‣ Proposition 4.25. ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) or ([2](https://arxiv.org/html/2602.09967v1#S4.I10.i2 "Item 2 ‣ Proposition 4.25. ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"))-(i), the function Jθ,η​(l)J\_{\theta,\eta}(l) is non-decreasing in θ\theta if the following conditions hold:

1. (1)

   0≤(Q¯​(θ)q​(θ))′≤10\leq\left(\frac{\bar{Q}(\theta)}{q(\theta)}\right)^{\prime}\leq 1;
2. (2)

   The function θ↦Fθ\theta\mapsto F\_{\theta} is convex in θ\theta for all ll, that is, ∂2Fθ​(l)∂θ2≥0\frac{\partial^{2}F\_{\theta}(l)}{\partial\theta^{2}}\geq 0;
3. (3)

   The function θ↦gθ​(t)\theta\mapsto g\_{\theta}(t) is convex in θ\theta for all tt, that is, for Fθ​(l)∈[0,1]F\_{\theta}(l)\in[0,1], ∂2gθ∂θ2​(Fθ​(l))≥0\frac{\partial^{2}g\_{\theta}}{\partial\theta^{2}}(F\_{\theta}(l))\geq 0;
4. (4)

   The function t↦gθ​(t)t\mapsto g\_{\theta}(t) is convex in tt for all θ∈Θ\theta\in\Theta, that is, for Fθ​(l)∈[0,1]F\_{\theta}(l)\in[0,1], gθ′′​(Fθ​(l))≥0g^{\prime\prime}\_{\theta}(F\_{\theta}(l))\geq 0;
5. (5)

   The function g:(θ,t)↦gθ​(t)g:(\theta,t)\mapsto g\_{\theta}(t) is submodular such that

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∂2gθ∂θ​∂t≤0,\frac{\partial^{2}g\_{\theta}}{\partial\theta\partial t}\leq 0, |  | (12) |

   and satisfies the following:

   |  |  |  |
   | --- | --- | --- |
   |  | Q¯​(θ)q​(θ)​∂2gθ∂θ​∂t​(Fθ​(l))≤−gI​n⁣′​(Fθ​(l)).\frac{\bar{Q}(\theta)}{q(\theta)}\,\frac{\partial^{2}g\_{\theta}}{\partial\theta\partial t}(F\_{\theta}(l))\leq-g^{In\prime}(F\_{\theta}(l)). |  |

The ratio Q¯​(θ)q​(θ)\frac{\bar{Q}(\theta)}{q(\theta)} represents the inverse hazard rate and measures how many agent types are left above θ\theta relative to the density of the type-θ\theta agent. Condition [1](https://arxiv.org/html/2602.09967v1#S4.I6.i1 "Item 1 ‣ 4.4. On the Monotonicity of the Function 𝜃↦𝐽_{𝜃,𝜂}⁢(𝑙) ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") implies that the distribution over types is heavy tailed, placing more probability on larger θ\theta values.
Moreover, the growth of the inverse hazard rate is bounded and does not increase too quickly as θ\theta increases. As a result, the population of higher types does not thin out too rapidly.

Conditions [2](https://arxiv.org/html/2602.09967v1#S4.I6.i2 "Item 2 ‣ 4.4. On the Monotonicity of the Function 𝜃↦𝐽_{𝜃,𝜂}⁢(𝑙) ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") and [3](https://arxiv.org/html/2602.09967v1#S4.I6.i3 "Item 3 ‣ 4.4. On the Monotonicity of the Function 𝜃↦𝐽_{𝜃,𝜂}⁢(𝑙) ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") are respectively saying that as θ\theta increases, the loss distribution becomes riskier, and higher types become more risk averse at a decreasing rate.
Condition [4](https://arxiv.org/html/2602.09967v1#S4.I6.i4 "Item 4 ‣ 4.4. On the Monotonicity of the Function 𝜃↦𝐽_{𝜃,𝜂}⁢(𝑙) ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") reflects strong risk aversion through the convexity of the distortion function gθ​(t)g\_{\theta}(t) in tt for all θ\theta.
Condition [5](https://arxiv.org/html/2602.09967v1#S4.I6.i5 "Item 5 ‣ 4.4. On the Monotonicity of the Function 𝜃↦𝐽_{𝜃,𝜂}⁢(𝑙) ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") implies that the function gg is submodular.
In other words, higher types assign lower marginal weight to favorable probabilities, distorting them more pessimistically and reflecting greater risk aversion.

### 4.5. Properties of the Optimal Menu

###### Lemma 4.18.

Consider an incentive efficient menu of contracts (Rθ∗,pθ∗)θ∈Θ(R^{\*}\_{\theta},p^{\*}\_{\theta})\_{\theta\in\Theta}, as characterized in Theorem [4.17](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem17 "Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"). If the optimal premia {pθ∗}θ∈Θ\{p^{\*}\_{\theta}\}\_{\theta\in\Theta} satisfy ([1](https://arxiv.org/html/2602.09967v1#S4.Ex49 "Item 1 ‣ Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")), then the following hold:

1. (1)

   If ∂Rθ∗∂l≡0\frac{\partial R^{\*}\_{\theta}}{\partial l}\equiv 0, then ∫Θ∫0L¯gI​n​(Fθ​(l))​𝑑l​𝑑μ≥∫0L¯gθ¯​(Fθ¯​(l))​𝑑l\int\_{\Theta}\int\_{0}^{\bar{L}}g^{In}(F\_{\theta}(l))\,dl\,d\mu\geq\int\_{0}^{\bar{L}}g\_{\underline{\theta}}(F\_{\underline{\theta}}(l))\,dl.
2. (2)

   If ∂Rθ∗∂l≡1\frac{\partial R^{\*}\_{\theta}}{\partial l}\equiv 1, then Vθ​(Rθ∗,pθ∗)=0V\_{\theta}(R^{\*}\_{\theta},p^{\*}\_{\theta})=0, for all θ∈Θ\theta\in\Theta.
3. (3)

   If ∂Rθ∗∂l\frac{\partial R^{\*}\_{\theta}}{\partial l} takes values in (0,1)(0,1), then

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∫Θ∫0L¯gI​n​(Fθ​(l))​𝑑l​𝑑μ\displaystyle\int\_{\Theta}\int\_{0}^{\bar{L}}g^{In}(F\_{\theta}(l))\,dl\,d\mu | ≥∫0L¯gθ¯​(Fθ¯​(l))​𝑑l+∫ΘUθ​(Rθ∗,pθ∗)​𝑑μ−Uθ¯​(Rθ¯∗,pθ¯∗)\displaystyle\ \geq\ \int\_{0}^{\bar{L}}g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\,dl+\int\_{\Theta}U\_{\theta}(R^{\*}\_{\theta},p^{\*}\_{\theta})\,d\mu-U\_{\underline{\theta}}(R^{\*}\_{\underline{\theta}},p^{\*}\_{\underline{\theta}}) |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | +∫Θ∫0L¯[gI​n​(Fθ​(l))−gθ​(Fθ​(l))]​∂Rθ∗​(l)∂l​𝑑l​𝑑μ.\displaystyle\qquad\qquad+\int\_{\Theta}\int\_{0}^{\bar{L}}\left[g^{In}(F\_{\theta}(l))-g\_{\theta}\big(F\_{\theta}(l)\big)\right]\,\frac{\partial R^{\*}\_{\theta}(l)}{\partial l}\,dl\,d\mu. |  |

Moreover, if the optimal premium satisfies pθ∗=0p^{\*}\_{\theta}=0 for each θ∈Θ\theta\in\Theta, and Rθ∗=0R^{\*}\_{\theta}=0 for each θ∈Θ\theta\in\Theta, then gI​n​(Fθ​(l))=1g^{In}(F\_{\theta}(l))=1, for almost every θ∈Θ\theta\in\Theta and almost every l∈[0,L¯]l\in[0,\bar{L}].

###### Proof.

The proof can be found in Appendix [B.9](https://arxiv.org/html/2602.09967v1#A2.SS9 "B.9. Proof of Lemma 4.18 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
∎

Lemma [4.18](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem18 "Lemma 4.18. ‣ 4.5. Properties of the Optimal Menu ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") provides an immediate implication of the insurer’s participation constraint (P2) on the optimal menu of contracts (Rθ∗,pθ∗)θ∈Θ(R^{\*}\_{\theta},p^{\*}\_{\theta})\_{\theta\in\Theta}, characterized in Theorem [4.17](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem17 "Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"). Specifically,
when α\alpha satisfies cases ([1](https://arxiv.org/html/2602.09967v1#S4.I10.i1 "Item 1 ‣ Proposition 4.25. ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) and ([2](https://arxiv.org/html/2602.09967v1#S4.I10.i2 "Item 2 ‣ Proposition 4.25. ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"))-(i), the optimal premium satisfies ([1](https://arxiv.org/html/2602.09967v1#S4.Ex49 "Item 1 ‣ Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")), and a separating equilibrium emerges.
If full coverage is offered to the agent, then the insurer’s distorted expected loss aggregated over types is greater than or equal to the distorted expected loss of the lowest type agent. If zero coverage is offered, that is if the agent retains the entire loss, then the insurer receives a zero welfare gain and is there indifferent between participating and not participating in the market.
Moreover, if partial coverage is offered to the agent, i.e., if ∂Rθ∗∂l\frac{\partial R^{\*}\_{\theta}}{\partial l} takes values in (0,1)(0,1), then the insurer’s distorted expected loss aggregated over types must be greater or equal than the least risk averse agent’s distorted expected loss, plus the difference between the agent’s aggregate utility and the lowest agent type’s utility at the optimum, plus a non-negative term reflecting the reduction in the insurer’s distortion advantage over the agent due to incomplete loss transfer.

If α\alpha satisfies case ([2](https://arxiv.org/html/2602.09967v1#S4.I10.i2 "Item 2 ‣ Proposition 4.25. ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"))-(ii), then the optimal premium satisfies ([1](https://arxiv.org/html/2602.09967v1#S4.Ex49 "Item 1 ‣ Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) with full coverage offered, implying that the insurer’s distorted expected loss aggregated over types, is at least as large as the distorted expected loss of the least risk averse agent.

On the other hand, if α\alpha satisfies case ([3](https://arxiv.org/html/2602.09967v1#S4.I10.i3 "Item 3 ‣ Proposition 4.25. ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")), then the agent retains the entire loss and pays zero premium at the optimum, i.e., pθ∗=0p^{\*}\_{\theta}=0, for all θ\theta. The insurer’s aggregate utility must be equal to zero, making the insurer indifferent in participating in the market. Additionally, in this case, the insurer’s distortion function assigns full weight to almost all loss levels of almost every agent type.

###### Proposition 4.19.

Suppose that Jθ​(l)J\_{\theta}(l) given in ([28](https://arxiv.org/html/2602.09967v1#A2.E28 "Equation 28 ‣ B.8. Proof of Theorem 4.17 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) is non-decreasing in θ\theta, for all ll, and consider an optimal incentive efficient menu of contracts (Rθ∗,pθ∗)θ∈Θ(R^{\*}\_{\theta},p^{\*}\_{\theta})\_{\theta\in\Theta}, characterized in Theorem [4.17](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem17 "Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"). Then the following holds:

1. (1)

   If ∂Rθ∗∂l≡0\frac{\partial R^{\*}\_{\theta}}{\partial l}\equiv 0, then θ↦Vθ​(Rθ∗,pθ∗)\theta\mapsto V\_{\theta}(R^{\*}\_{\theta},p^{\*}\_{\theta}) is decreasing.
2. (2)

   If ∂Rθ∗∂l≡1\frac{\partial R^{\*}\_{\theta}}{\partial l}\equiv 1, then ∂∂θ​Vθ​(Rθ∗,pθ∗)=0\frac{\partial}{\partial\theta}V\_{\theta}(R^{\*}\_{\theta},p^{\*}\_{\theta})=0.
3. (3)

   If ∂Rθ∗∂l\frac{\partial R^{\*}\_{\theta}}{\partial l} takes values in (0,1)(0,1), then θ↦Vθ​(Rθ∗,pθ∗)\theta\mapsto V\_{\theta}(R^{\*}\_{\theta},p^{\*}\_{\theta}) is increasing whenever the following holds:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | [gθ​(Fθ​(l))−gI​n​(Fθ​(l))]​∂2Rθ∗​(l)∂θ​∂l≥−gI​n⁣′​(Fθ​(l))​∂Fθ​(l)∂θ​(1−∂Rθ∗​(l)∂l).\left[g\_{\theta}\big(F\_{\theta}(l)\big)-g^{In}(F\_{\theta}(l))\right]\,\frac{\partial^{2}R^{\*}\_{\theta}(l)}{\partial\theta\partial l}\geq-g^{In\,\prime}(F\_{\theta}(l))\frac{\partial F\_{\theta}(l)}{\partial\theta}\left(1-\frac{\partial R^{\*}\_{\theta}(l)}{\partial l}\right). |  | (13) |

###### Proof.

The proof can be found in Appendix [B.10](https://arxiv.org/html/2602.09967v1#A2.SS10 "B.10. Proof of Proposition 4.19 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
∎

Proposition [4.19](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem19 "Proposition 4.19. ‣ 4.5. Properties of the Optimal Menu ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") studies the insurer’s utility at the optimum, and shows that the monotonicity of this utility with respect to the agent’s type θ\theta depends on the optimal marginal retention. In particular, if full coverage is provided to the agent at the optimum, the insurer’s utility decreases with the agent’s type θ\theta. An implication of this is that for higher types, who are more risk averse and face stochastically larger losses, the insurer’s utility is lower than for lower risk types, as intuition would suggest. If, in contrast, zero coverage is provided to the agent, i.e., the agent retains the entire loss, we saw in Lemma [4.18](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem18 "Lemma 4.18. ‣ 4.5. Properties of the Optimal Menu ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") that the insurer’s utility in this case is equal to zero, and hence the participation constraint binds. Consequently, the insurer’s utility is neither increasing nor decreasing in the agent’s type. Finally, when partial coverage is provided, the insurer has a higher utility at the optimum from higher types, who are more risk averse, if ([13](https://arxiv.org/html/2602.09967v1#S4.E13 "Equation 13 ‣ Item 3 ‣ Proposition 4.19. ‣ 4.5. Properties of the Optimal Menu ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) holds.

###### Proposition 4.20.

Suppose that Jθ​(l)J\_{\theta}(l) given in ([28](https://arxiv.org/html/2602.09967v1#A2.E28 "Equation 28 ‣ B.8. Proof of Theorem 4.17 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) is non-decreasing in θ\theta, for all ll. Then the optimal incentive efficient menu of contracts (Rθ∗,pθ∗)θ∈Θ(R^{\*}\_{\theta},p^{\*}\_{\theta})\_{\theta\in\Theta}, characterized in Theorem [4.17](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem17 "Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), satisfies the following properties.

1. (1)

   Rθ∗R^{\*}\_{\theta} decreases with θ\theta, and pθ∗p^{\*}\_{\theta} increases with θ\theta.
2. (2)

   For θ=θ¯\theta=\bar{\theta}, Rθ¯∗​(l)=0R^{\*}\_{\bar{\theta}}(l)=0 for all ll.
3. (3)

   For θ=θ¯\theta=\underline{\theta}, Uθ¯​(Rθ¯∗,pθ¯∗)=Uθ¯​(Lθ¯,0)U\_{\underline{\theta}}(R^{\*}\_{\underline{\theta}},p^{\*}\_{\underline{\theta}})=U\_{\underline{\theta}}(L\_{\underline{\theta}},0).
4. (4)

   The function θ↦Uθ​(Rθ∗,pθ∗)\theta\mapsto U\_{\theta}(R^{\*}\_{\theta},p^{\*}\_{\theta}) is decreasing. Moreover, it is convex if the following holds:

   1. (a)

      gg is submodular, as in ([12](https://arxiv.org/html/2602.09967v1#S4.E12 "Equation 12 ‣ Item 5 ‣ 4.4. On the Monotonicity of the Function 𝜃↦𝐽_{𝜃,𝜂}⁢(𝑙) ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"));
   2. (b)

      gθ​(t)g\_{\theta}(t) is convex in θ\theta for all tt;
   3. (c)

      gθ​(t)g\_{\theta}(t) is convex in tt for all θ\theta;
   4. (d)

      FθF\_{\theta} is convex in θ\theta for all ll.

###### Proof.

The proof can be found in Appendix [B.11](https://arxiv.org/html/2602.09967v1#A2.SS11 "B.11. Proof of Proposition 4.20 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
∎

Proposition [4.20](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem20 "Proposition 4.20. ‣ 4.5. Properties of the Optimal Menu ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") provides some important properties of the optimal incentive-efficient menu of contracts (Rθ∗,pθ∗)θ∈Θ(R^{\*}\_{\theta},p^{\*}\_{\theta})\_{\theta\in\Theta}. Specifically, the optimal retention decreases with the agent’s type θ\theta, whereas the optimal premium increases with θ\theta. That is, higher types, who are more risk averse and face stochastically larger losses, receive more coverage for a larger premium. Additionally, the highest risk type (who is the most risk averse and faces the largest loss) receives full coverage at every possible loss level ll. This property, commonly referred to as efficiency at the top, was shown to hold by Chade and Schlee ([2012](https://arxiv.org/html/2602.09967v1#bib.bib66 "Optimal insurance with adverse selection")), and later by Gershkov et al. ([2023](https://arxiv.org/html/2602.09967v1#bib.bib68 "Optimal insurance: dual utility, random losses, and adverse selection")) and Ghossoub et al. ([2025](https://arxiv.org/html/2602.09967v1#bib.bib67 "Optimal insurance in a monopoly: dual utilities with hidden risk attitudes")). In contrast, the lowest risk type (the least risk averse) is indifferent in participating at the optimum, and the monopolist insurer absorbs all of the surplus from this agent.

Proposition [4.20](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem20 "Proposition 4.20. ‣ 4.5. Properties of the Optimal Menu ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") also shows that the agent’s utility at the optimum decreases with the agent’s type θ\theta. Moreover, if gg is submodular as in ([12](https://arxiv.org/html/2602.09967v1#S4.E12 "Equation 12 ‣ Item 5 ‣ 4.4. On the Monotonicity of the Function 𝜃↦𝐽_{𝜃,𝜂}⁢(𝑙) ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")), if both the agent’s distortion and the cumulative loss distribution are convex in type, and if the agent’s distortion is convex in tt for all types, then the agent’s utility is also convex in type.
While the monotonicity of the agent’s utility is consistent with the findings of previous literature (e.g., Chade and Schlee ([2012](https://arxiv.org/html/2602.09967v1#bib.bib66 "Optimal insurance with adverse selection")), Gershkov et al. ([2023](https://arxiv.org/html/2602.09967v1#bib.bib68 "Optimal insurance: dual utility, random losses, and adverse selection"))), Ghossoub et al. ([2025](https://arxiv.org/html/2602.09967v1#bib.bib67 "Optimal insurance in a monopoly: dual utilities with hidden risk attitudes")) assume that the agent’s type affects only their risk attitude, and they show that the agent’s utility decreases with risk type. Moreover, it is convex in type if convexity of the agent’s distortion in type is satisfied.

### 4.6. Special Cases of Social Weight

We can clearly notice the importance of the social weight α\alpha in the characterization of optimal solutions to Problem ([4](https://arxiv.org/html/2602.09967v1#S4.E4 "Equation 4 ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) given in Theorem [4.17](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem17 "Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
Particularly, when α\alpha is close to zero, the objective places almost all weight on the insurer’s aggregate utility, whereas if α\alpha is close to 11, then the objective in this case primarily reflects the agent’s aggregate utility.
Hence, we consider the two cases of α=0\alpha=0 and α=1\alpha=1, as they provide an examination of the maximization of aggregate utilities of the insurer alone, and the agent alone, respectively.

#### 4.6.1. Insurer’s Welfare Maximization

We consider α=0\alpha=0, and we study the following problem.

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup(Rθ,pθ)θ∈Θ∈ℐ​ℛ∩ℐ​𝒞​∫ΘVθ​(Rθ,pθ)​𝑑μ.\underset{(R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{R}\cap\mathcal{I}\mathcal{C}}{\sup}\ \int\_{\Theta}V\_{\theta}(R\_{\theta},p\_{\theta})\,\,d\mu. |  | (14) |

This reduces Problem ([4](https://arxiv.org/html/2602.09967v1#S4.E4 "Equation 4 ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) to the maximization of the insurer’s total utility subject to the incentive compatibility and individual rationality constraints, and no longer defines an IPO solution.

The following proposition provides a necessary condition for incentive compatibility, characterizing the insurer’s total utility.

###### Proposition 4.21.

If (Rθ,pθ)θ∈Θ∈ℐ​𝒞(R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{C}, then the monopolistic insurer’s total utility is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ΘVθ​(Rθ,pθ)​𝑑μ\displaystyle\int\_{\Theta}V\_{\theta}(R\_{\theta},p\_{\theta})d\mu | =pθ¯+∫0L¯[1−gθ¯​(Fθ¯​(l))]​∂Rθ¯​(l)∂l​𝑑l−∫Θ∫0L¯[1−gI​n​(Fθ​(l))]​q​(θ)​𝑑l​𝑑θ\displaystyle=p\_{\underline{\theta}}+\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\right]\,\,\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}\,\,dl-\int\_{\Theta}\int\_{0}^{\bar{L}}\left[1-g^{In}(F\_{\theta}(l))\right]q(\theta)\ dl\,d\theta |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −∫Θ∫0L¯Jθ​(l)​∂Rθ​(l)∂l​q​(θ)​𝑑l​𝑑θ,\displaystyle\quad-\int\_{\Theta}\int\_{0}^{\bar{L}}J\_{\theta}(l)\frac{\partial R\_{\theta}(l)}{\partial l}q(\theta)\,dl\,d\theta, |  | (15) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jθ​(l)=[gI​n​(Fθ​(l))−gθ​(Fθ​(l))]+Q¯​(θ)q​(θ)​[∂gθ∂θ​(Fθ​(l))+gθ′​(Fθ​(l))​∂Fθ​(l)∂θ].J\_{\theta}(l)=\left[g^{In}(F\_{\theta}(l))-g\_{\theta}\big(F\_{\theta}(l)\big)\right]+\frac{\bar{Q}(\theta)}{q(\theta)}\left[\frac{\partial g\_{\theta}}{\partial\theta}(F\_{\theta}(l))+g^{\prime}\_{\theta}(F\_{\theta}(l))\frac{\partial F\_{\theta}(l)}{\partial\theta}\right]. |  | (16) |

###### Proof.

The proof follows immediately by replacing α\alpha by 0 in the social welfare function in the proof of Theorem [4.17](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem17 "Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
∎

###### Theorem 4.22.

Let (Rθ∗,pθ∗)θ∈Θ∈ℐ​ℛ∩ℐ​𝒞(R^{\*}\_{\theta},p^{\*}\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{R}\cap\mathcal{I}\mathcal{C} be an optimal solution to ([14](https://arxiv.org/html/2602.09967v1#S4.E14 "Equation 14 ‣ 4.6.1. Insurer’s Welfare Maximization ‣ 4.6. Special Cases of Social Weight ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")). Suppose that the function Jθ​(l)J\_{\theta}(l) given in ([16](https://arxiv.org/html/2602.09967v1#S4.E16 "Equation 16 ‣ Proposition 4.21. ‣ 4.6.1. Insurer’s Welfare Maximization ‣ 4.6. Special Cases of Social Weight ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) is non-decreasing in θ\theta for all ll. Then, the optimal menu (Rθ∗,pθ∗)θ∈Θ(R^{\*}\_{\theta},p^{\*}\_{\theta})\_{\theta\in\Theta} can be characterized similarly to case ([1](https://arxiv.org/html/2602.09967v1#S4.I10.i1 "Item 1 ‣ Proposition 4.25. ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) of Theorem [4.17](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem17 "Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"). Specifically, for each θ∈Θ\theta\in\Theta, the optimal retention function Rθ∗R^{\*}\_{\theta} satisfies:

|  |  |  |
| --- | --- | --- |
|  | ∂Rθ∗​(l)∂l={0,Jθ​(l)>0,∈[0,1],Jθ​(l)=0,1,Jθ​(l)<0.\frac{\partial R^{\*}\_{\theta}(l)}{\partial l}=\begin{cases}0,&J\_{\theta}(l)>0,\\ \in[0,1],&J\_{\theta}(l)=0,\\ 1,&J\_{\theta}(l)<0.\end{cases} |  |

The corresponding premium pθ∗p^{\*}\_{\theta} is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | pθ∗\displaystyle p^{\*}\_{\theta} | =∫0L¯[1−gθ¯​(Fθ¯​(l))]​𝑑l−∫θ¯θ∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​∂Rs∗​(l)∂l​𝑑l​𝑑s\displaystyle=\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\right]\,\,dl-\int\_{\underline{\theta}}^{\theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\frac{\partial R^{\*}\_{s}(l)}{\partial l}\ dl\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫0L¯[1−gθ​(Fθ​(l))]​∂Rθ∗​(l)∂l​𝑑l.\displaystyle\quad-\int\_{0}^{\bar{L}}\left[1-g\_{\theta}\big(F\_{\theta}(l)\big)\right]\,\,\frac{\partial R^{\*}\_{\theta}(l)}{\partial l}\,\,dl. |  |

Moreover, the collection {Rθ∗}θ∈Θ\{R^{\*}\_{\theta}\}\_{\theta\in\Theta} of optimal retention functions is submodular.

###### Proof.

The proof can be found in Appendix [B.12](https://arxiv.org/html/2602.09967v1#A2.SS12 "B.12. Proof of Theorem 4.22 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
∎

Theorem [4.22](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem22 "Theorem 4.22. ‣ 4.6.1. Insurer’s Welfare Maximization ‣ 4.6. Special Cases of Social Weight ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") shows that, in this special case of α=0\alpha=0, the optimal menu of contracts consists of a collection of layered retention functions, under the assumption of monotonicity of Jθ​(l)J\_{\theta}(l).
Specifically, when Jθ​(l)>0J\_{\theta}(l)>0, full coverage is provided. Jθ​(l)<0J\_{\theta}(l)<0 corresponds to no coverage of this loss level, and when Jθ​(l)=0J\_{\theta}(l)=0, the optimal retention allows for some flexibility, as long as feasibility is maintained.

Note that

|  |  |  |
| --- | --- | --- |
|  | Jθ​(l)=Jθ,η​(l)|α=0,J\_{\theta}(l)=J\_{\theta,\eta}(l)\big|\_{\alpha=0}, |  |

and hence ∂Jθ​(l)∂θ\frac{\partial J\_{\theta}(l)}{\partial\theta} can be obtained by replacing α\alpha by 0 in ∂Jθ,η​(l)∂θ\frac{\partial J\_{\theta,\eta}(l)}{\partial\theta}. Conditions [1](https://arxiv.org/html/2602.09967v1#S4.I6.i1 "Item 1 ‣ 4.4. On the Monotonicity of the Function 𝜃↦𝐽_{𝜃,𝜂}⁢(𝑙) ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") to [5](https://arxiv.org/html/2602.09967v1#S4.I6.i5 "Item 5 ‣ 4.4. On the Monotonicity of the Function 𝜃↦𝐽_{𝜃,𝜂}⁢(𝑙) ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") of the monotonicity of Jθ,η​(l)J\_{\theta,\eta}(l) are also sufficient for Jθ​(l)J\_{\theta}(l) to be non-decreasing in θ\theta for all ll.

#### 4.6.2. Agent’s Welfare Maximization

When α=1\alpha=1, the objective places full weight on the agent’s aggregate utility, and the problem is reduced to the following:

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup(Rθ,pθ)θ∈Θ∈ℐ​ℛ∩ℐ​𝒞​∫ΘUθ​(Rθ,pθ)​𝑑μ.\underset{(R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{R}\cap\mathcal{I}\mathcal{C}}{\sup}\,\int\_{\Theta}U\_{\theta}(R\_{\theta},p\_{\theta})\,\,d\mu. |  | (17) |

It follows from Theorem [4.17](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem17 "Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") that Rθ∗=0R^{\*}\_{\theta}=0 and pθ∗=0p^{\*}\_{\theta}=0, for each θ∈Θ\theta\in\Theta. This result is not surprising. In fact, ([17](https://arxiv.org/html/2602.09967v1#S4.E17 "Equation 17 ‣ 4.6.2. Agent’s Welfare Maximization ‣ 4.6. Special Cases of Social Weight ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) describes the maximization of the agent’s aggregate utility subject to individual rationality and incentive compatibility, without accounting for the insurer. In this case, the agent’s welfare is maximized by full insurance, meaning zero retention. Moreover, with the insurer’s utility absent from the objective, the premium is chosen solely to maximize agent welfare. Any strictly positive premium lowers the value of the objective by reducing the agent’s utility without generating any compensating benefit. Hence, the optimal premium is zero.

### 4.7. Alternative Ordering

The results obtained so far rely on the type ordering assumptions of Subsection [4.2](https://arxiv.org/html/2602.09967v1#S4.SS2 "4.2. Type Ordering under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), under which higher types are more risk averse and face stochastically larger losses.
Alternatively, one may consider a setting in which higher types face stochastically larger losses but are less risk averse. We formalize this by the following assumption.

###### Assumption 4.23.

The distortion function gθg\_{\theta} is non-decreasing in θ\theta. That is,

|  |  |  |
| --- | --- | --- |
|  | ∂gθ∂θ​(t)≥0,∀t∈(0,1).\frac{\partial g\_{\theta}}{\partial\theta}(t)\geq 0,\ \forall\,t\in(0,1). |  |

Moreover, losses LθL\_{\theta} for θ∈Θ\theta\in\Theta are ordered in the first order stochastic dominance sense, such that for θ1,θ2∈Θ\theta\_{1},\theta\_{2}\in\Theta with θ1<θ2\theta\_{1}<\theta\_{2},
Lθ1≼F​O​S​DLθ2,or equivalently,​Fθ1​(l)≥Fθ2​(l).L\_{\theta\_{1}}\preccurlyeq\_{FOSD}L\_{\theta\_{2}},\ \text{or equivalently,}\ F\_{\theta\_{1}}(l)\geq F\_{\theta\_{2}}(l).
That is,

|  |  |  |
| --- | --- | --- |
|  | ∂Fθ​(l)∂θ≤0,∀l.\frac{\partial F\_{\theta}(l)}{\partial\theta}\leq 0,\ \forall\,l. |  |

###### Assumption 4.24.

|  |  |  |
| --- | --- | --- |
|  | gθ′​(Fθ​(l))​|∂Fθ​(l)∂θ|≥|∂gθ∂θ​(Fθ​(l))|,∀l.g^{\prime}\_{\theta}(F\_{\theta}(l))\left|\frac{\partial F\_{\theta}(l)}{\partial\theta}\right|\geq\left|\frac{\partial g\_{\theta}}{\partial\theta}(F\_{\theta}(l))\right|,\ \forall\,l. |  |

Assumption [4.24](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem24 "Assumption 4.24. ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") ensures that as the agent’s type increases, the effect of facing larger losses dominates the reduction in risk aversion.
Moreover, it follows that

|  |  |  |
| --- | --- | --- |
|  | ∂∂θ​[gθ​(Fθ​(l))]=∂gθ∂θ​(Fθ​(l))+gθ′​(Fθ​(l))​∂Fθ​(l)∂θ≤0.\frac{\partial}{\partial\theta}\left[g\_{\theta}\big(F\_{\theta}(l)\big)\right]=\frac{\partial g\_{\theta}}{\partial\theta}\big(F\_{\theta}(l)\big)+g^{\prime}\_{\theta}\big(F\_{\theta}(l)\big)\frac{\partial F\_{\theta}(l)}{\partial\theta}\leq 0. |  |

In this setting, the characterization of individually rational and incentive compatible menus follows exactly as in Subsection [4.3](https://arxiv.org/html/2602.09967v1#S4.SS3 "4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
We aim to find optimal incentive efficient menus of contracts that solve Problem [4](https://arxiv.org/html/2602.09967v1#S4.E4 "Equation 4 ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").

###### Proposition 4.25.

Suppose that η\eta satisfies Assumption [4.15](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem15 "Assumption 4.15. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"). Optimal incentive efficient menus satisfy the following form:

1. (1)

   If α∈(0,q​(θ¯)qη​(θ¯)+q​(θ¯))\alpha\in\left(0,\frac{q(\bar{\theta})}{q\_{\eta}(\bar{\theta})+q(\bar{\theta})}\right), and if the function θ↦Jθ,η​(l)\theta\mapsto J\_{\theta,\eta}(l) is non-decreasing in θ\theta for all ll, then there exists a solution (Rθ∗,pθ∗)θ∈Θ\left(R^{\*}\_{\theta},p^{\*}\_{\theta}\right)\_{\theta\in\Theta} such that the optimal retention function is characterized by:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∂Rθ∗​(l)∂l={0Jθ,η​(l)>0,∈[0,1]Jθ,η​(l)=0,1Jθ,η​(l)<0,\frac{\partial R^{\*}\_{\theta}(l)}{\partial l}=\begin{cases}0&J\_{\theta,\eta}(l)>0,\\ \in[0,1]&J\_{\theta,\eta}(l)=0,\\ 1&J\_{\theta,\eta}(l)<0,\end{cases} |  | (18) |

   where the function Jθ,η​(l)J\_{\theta,\eta}(l) satisfies ([1](https://arxiv.org/html/2602.09967v1#S4.Ex48 "Item 1 ‣ Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"))
   and the premia {pθ∗}θ∈Θ\{p^{\*}\_{\theta}\}\_{\theta\in\Theta} are given by ([1](https://arxiv.org/html/2602.09967v1#S4.Ex49 "Item 1 ‣ Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")).
2. (2)

   If α∈[q​(θ¯)qη​(θ¯)+q​(θ¯),12]\alpha\in\left[\frac{q(\bar{\theta})}{q\_{\eta}(\bar{\theta})+q(\bar{\theta})},\frac{1}{2}\right], and if the function θ↦Jθ,η​(l)\theta\mapsto J\_{\theta,\eta}(l) is non-decreasing in θ\theta for all ll, then:

   1. (i)

      If θ<θα\theta<\theta\_{\alpha}, then Rθ∗R^{\*}\_{\theta} follows the form given in ([18](https://arxiv.org/html/2602.09967v1#S4.E18 "Equation 18 ‣ Item 1 ‣ Proposition 4.25. ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"));
   2. (ii)

      If θ≥θα\theta\geq\theta\_{\alpha}, then Rθ∗=0R^{\*}\_{\theta}=0,

   where θα\theta\_{\alpha} is determined by the equation Q¯η​(θα)Q¯​(θα)=1−αα\frac{\bar{Q}\_{\eta}(\theta\_{\alpha})}{\bar{Q}(\theta\_{\alpha})}=\frac{1-\alpha}{\alpha}. The premia {pθ∗}θ∈Θ\{p^{\*}\_{\theta}\}\_{\theta\in\Theta} satisfy ([1](https://arxiv.org/html/2602.09967v1#S4.Ex49 "Item 1 ‣ Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")).
3. (3)

   If α∈(12,1]\alpha\in\left(\frac{1}{2},1\right], then Rθ∗=0R^{\*}\_{\theta}=0 and pθ∗=0p^{\*}\_{\theta}=0 for all θ∈Θ\theta\in\Theta.

Moreover, the collection of optimal retention functions {Rθ∗}θ∈Θ\{R^{\*}\_{\theta}\}\_{\theta\in\Theta} is submodular for a given η\eta and α\alpha.

Proposition [4.25](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem25 "Proposition 4.25. ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") can be proved similarly to Theorem [4.17](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem17 "Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"). In this setting, when α≤12\alpha\leq\frac{1}{2} and θ<θα\theta<\theta\_{\alpha}, that is when α\alpha satisfies cases ([1](https://arxiv.org/html/2602.09967v1#S4.I10.i1 "Item 1 ‣ Proposition 4.25. ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) and ([2](https://arxiv.org/html/2602.09967v1#S4.I10.i2 "Item 2 ‣ Proposition 4.25. ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"))-(i), a separating layered equilibrium emerges. Optimal retentions are submodular ensuring that higher types, facing larger losses, receive more coverage, despite being less risk averse. This is because the larger loss faced by a high-type agent dominates their lower risk aversion, so the agent still requires more coverage, as captured by Assumption [4.24](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem24 "Assumption 4.24. ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
If α≤12\alpha\leq\frac{1}{2} and θ≥θα\theta\geq\theta\_{\alpha}, full coverage is offered and optimal premia satisfy ([1](https://arxiv.org/html/2602.09967v1#S4.Ex49 "Item 1 ‣ Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")). Finally, if α>12\alpha>\frac{1}{2}, then all types receive full coverage and pay zero premium.

Next, we provide sufficient conditions that ensure the monotonicity of Jθ,η​(l)J\_{\theta,\eta}(l), when α\alpha satisfies cases ([1](https://arxiv.org/html/2602.09967v1#S4.I10.i1 "Item 1 ‣ Proposition 4.25. ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) and ([2](https://arxiv.org/html/2602.09967v1#S4.I10.i2 "Item 2 ‣ Proposition 4.25. ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"))-(i) .
Recall that in this region, we have 1−α−α​Q¯η​(θ)Q¯​(θ)≥01-\alpha-\alpha\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)}\geq 0. The partial derivative of Jθ,η​(l)J\_{\theta,\eta}(l) with respect to θ\theta is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂Jθ,η​(l)∂θ\displaystyle\frac{\partial J\_{\theta,\eta}(l)}{\partial\theta} | =(1−α)​((Q¯​(θ)q​(θ))′−1)​[∂gθ∂θ​(Fθ​(l))+gθ′​(Fθ​(l))​∂Fθ​(l)∂θ]\displaystyle=(1-\alpha)\left(\left(\frac{\bar{Q}(\theta)}{q(\theta)}\right)^{\prime}-1\right)\left[\frac{\partial g\_{\theta}}{\partial\theta}(F\_{\theta}(l))+g^{\prime}\_{\theta}\big(F\_{\theta}(l)\big)\frac{\partial F\_{\theta}(l)}{\partial\theta}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−α)​∂Fθ​(l)∂θ​[Q¯​(θ)q​(θ)​∂2gθ∂θ​∂t​(Fθ​(l))+gI​n⁣′​(Fθ​(l))]\displaystyle\quad+(1-\alpha)\frac{\partial F\_{\theta}(l)}{\partial\theta}\left[\frac{\bar{Q}(\theta)}{q(\theta)}\frac{\partial^{2}g\_{\theta}}{\partial\theta\,\,\partial t}(F\_{\theta}(l))+g^{In\ \prime}(F\_{\theta}(l))\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −α​[(Q¯η​(θ)Q¯​(θ)​Q¯​(θ)q​(θ))′​[∂gθ∂θ​(Fθ​(l))+gθ′​(Fθ​(l))​∂Fθ​(l)∂θ]+∂Fθ​(l)∂θ​Q¯η​(θ)Q¯​(θ)​Q¯​(θ)q​(θ)​∂2gθ∂θ​∂t​(Fθ​(l))]\displaystyle\quad-\alpha\left[\left(\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)}\frac{\bar{Q}(\theta)}{q(\theta)}\right)^{\prime}\left[\frac{\partial g\_{\theta}}{\partial\theta}(F\_{\theta}(l))+g^{\prime}\_{\theta}\big(F\_{\theta}(l)\big)\frac{\partial F\_{\theta}(l)}{\partial\theta}\right]+\frac{\partial F\_{\theta}(l)}{\partial\theta}\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)}\frac{\bar{Q}(\theta)}{q(\theta)}\frac{\partial^{2}g\_{\theta}}{\partial\theta\partial t}(F\_{\theta}(l))\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +[1−α−α​Q¯η​(θ)Q¯​(θ)]​Q¯​(θ)q​(θ)⋅[gθ′​(Fθ​(l))​∂2Fθ​(l)∂θ2+∂2gθ∂θ2​(Fθ​(l))+gθ′′​(Fθ​(l))​(∂Fθ​(l)∂θ)2].\displaystyle\quad+\left[1-\alpha-\alpha\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)}\right]\frac{\bar{Q}(\theta)}{q(\theta)}\cdot\left[g^{\prime}\_{\theta}(F\_{\theta}(l))\frac{\partial^{2}F\_{\theta}(l)}{\partial\theta^{2}}+\frac{\partial^{2}g\_{\theta}}{\partial\theta^{2}}(F\_{\theta}(l))+g^{\prime\prime}\_{\theta}(F\_{\theta}(l))\left(\frac{\partial F\_{\theta}(l)}{\partial\theta}\right)^{2}\ \right]. |  |

Using the monotonicity implications of Assumptions [4.15](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem15 "Assumption 4.15. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") and [4.23](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem23 "Assumption 4.23. ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), Jθ,η​(l)J\_{\theta,\eta}(l) is non-decreasing in θ\theta if the following conditions hold:

1. (1)

   0≤(Q¯​(θ)q​(θ))′≤10\leq\left(\frac{\bar{Q}(\theta)}{q(\theta)}\right)^{\prime}\leq 1;
2. (2)

   The function θ↦Fθ\theta\mapsto F\_{\theta} is convex in θ\theta for all ll, that is, ∂2Fθ​(l)∂θ2≥0\frac{\partial^{2}F\_{\theta}(l)}{\partial\theta^{2}}\geq 0;
3. (3)

   The function θ↦gθ​(t)\theta\mapsto g\_{\theta}(t) is convex in θ\theta for all tt, that is, for Fθ​(l)∈[0,1]F\_{\theta}(l)\in[0,1], ∂2gθ∂θ2​(Fθ​(l))≥0\frac{\partial^{2}g\_{\theta}}{\partial\theta^{2}}(F\_{\theta}(l))\geq 0;
4. (4)

   The function t↦gθ​(t)t\mapsto g\_{\theta}(t) is convex in tt for all θ∈Θ\theta\in\Theta, that is, for Fθ​(l)∈[0,1]F\_{\theta}(l)\in[0,1], g′′θ(Fθ(l))≥0g\prime\prime\_{\theta}(F\_{\theta}(l))\geq 0;
5. (5)

   The function g:(θ,t)↦gθ​(t)g:(\theta,t)\mapsto g\_{\theta}(t) satisfies

   |  |  |  |
   | --- | --- | --- |
   |  | ∂2gθ∂θ​∂t​(t)≤0,\frac{\partial^{2}g\_{\theta}}{\partial\theta\ \partial t}(t)\leq 0, |  |

   such that the following hold:

   |  |  |  |
   | --- | --- | --- |
   |  | Q¯​(θ)q​(θ)​∂2gθ∂θ​∂t​(Fθ​(l))≤−gI​n⁣′​(Fθ​(l)),and\frac{\bar{Q}(\theta)}{q(\theta)}\frac{\partial^{2}g\_{\theta}}{\partial\theta\ \partial t}(F\_{\theta}(l))\leq-g^{In\ \prime}\big(F\_{\theta}(l)\big),\ \text{and} |  |

   |  |  |  |
   | --- | --- | --- |
   |  | (Q¯η​(θ)Q¯​(θ)​Q¯​(θ)q​(θ))′​[∂gθ∂θ​(Fθ​(l))+gθ′​(Fθ​(l))​∂Fθ​(l)∂θ]≤−Q¯η​(θ)Q¯​(θ)​Q¯​(θ)q​(θ)​∂Fθ​(l)∂θ​∂2gθ∂θ​∂t​(Fθ​(l)).\left(\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)}\frac{\bar{Q}(\theta)}{q(\theta)}\right)^{\prime}\left[\frac{\partial g\_{\theta}}{\partial\theta}(F\_{\theta}(l))+g^{\prime}\_{\theta}\big(F\_{\theta}(l)\big)\frac{\partial F\_{\theta}(l)}{\partial\theta}\right]\leq-\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)}\frac{\bar{Q}(\theta)}{q(\theta)}\frac{\partial F\_{\theta}(l)}{\partial\theta}\frac{\partial^{2}g\_{\theta}}{\partial\theta\ \partial t}(F\_{\theta}(l)). |  |

Condition [1](https://arxiv.org/html/2602.09967v1#S4.I11.i1 "Item 1 ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") ensures that the population of higher types does not thin out too rapidly. As θ\theta increases, Condition [2](https://arxiv.org/html/2602.09967v1#S4.I11.i2 "Item 2 ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") ensures that the loss distribution becomes riskier at a decreasing rate, and Condition [3](https://arxiv.org/html/2602.09967v1#S4.I11.i3 "Item 3 ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") ensures that higher types become less risk averse at an increasing rate.
Condition [4](https://arxiv.org/html/2602.09967v1#S4.I11.i4 "Item 4 ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") guarantees strong risk aversion for each type. Condition [5](https://arxiv.org/html/2602.09967v1#S4.I11.i5 "Item 5 ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") implies submodularity of the function gg, meaning that as θ\theta increases, the marginal distortion decreases.
While Conditions [1](https://arxiv.org/html/2602.09967v1#S4.I11.i1 "Item 1 ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") to [4](https://arxiv.org/html/2602.09967v1#S4.I11.i4 "Item 4 ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") remain unchanged under the alternative type ordering compared to the sufficient conditions of monotonicity in Subsection [4.4](https://arxiv.org/html/2602.09967v1#S4.SS4 "4.4. On the Monotonicity of the Function 𝜃↦𝐽_{𝜃,𝜂}⁢(𝑙) ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), Condition [5](https://arxiv.org/html/2602.09967v1#S4.I11.i5 "Item 5 ‣ 4.7. Alternative Ordering ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") must be strengthened to preserve monotonicity.

The results obtained in Subsection [4.5](https://arxiv.org/html/2602.09967v1#S4.SS5 "4.5. Properties of the Optimal Menu ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") on the optimal incentive-efficient menu of contracts (Rθ∗,pθ∗)θ∈Θ(R^{\*}\_{\theta},p^{\*}\_{\theta})\_{\theta\in\Theta}, continue to hold in this setting. The insurer’s participation constraint has distinct implications on the optimal menu of contracts, depending on the value of the optimal marginal retention.
In particular, when the optimal premium satisfies ([1](https://arxiv.org/html/2602.09967v1#S4.Ex49 "Item 1 ‣ Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")), Lemma [4.18](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem18 "Lemma 4.18. ‣ 4.5. Properties of the Optimal Menu ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") implies that if the agent retains the entire loss, the insurer becomes indifferent between participating in the market or not. Otherwise, the insurer’s participation constraint imposes a lower bound on the insurer’s distorted expected loss aggregated over types.
If the optimal premium is zero and full coverage is provided to the agent, then the insurer’s distortion function assigns full weight to almost all loss levels of almost every agent type. Moreover, we see in Proposition [4.19](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem19 "Proposition 4.19. ‣ 4.5. Properties of the Optimal Menu ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") that, when full coverage is provided to the agent for all types θ∈Θ\theta\in\Theta, the insurer’s utility becomes lower for higher types, who are less risk averse and face stochastically larger losses. If partial coverage is provided, then the insurer’s utility increases with the agent’s type if ([13](https://arxiv.org/html/2602.09967v1#S4.E13 "Equation 13 ‣ Item 3 ‣ Proposition 4.19. ‣ 4.5. Properties of the Optimal Menu ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) holds.

Proposition [4.20](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem20 "Proposition 4.20. ‣ 4.5. Properties of the Optimal Menu ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") demonstrates that higher types of the agent, who are less risk averse and face stochastically larger losses, receive more coverage in exchange for higher premia. The highest type θ¯\bar{\theta}, who is the least risk averse but faces the largest loss, receives full coverage at every loss level. The lowest type θ¯\underline{\theta}, who is the most risk averse but faces the smallest loss, is indifferent between participating in the market and not participating. The agent’s utility decreases with the type, meaning that higher types, i.e, less risk-averse types facing stochastically larger losses, receive lower utilities at the optimum. Additionally, the agent’s utility is convex in types, if the same conditions of Proposition [4.20](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem20 "Proposition 4.20. ‣ 4.5. Properties of the Optimal Menu ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")-(4) hold.

## 5. Conclusion

This paper examines a monopolistic insurance market with hidden information, where the agent’s risk attitude and loss distribution are private information, and the agent’s type is drawn from a continuum. Within this framework, we study the concept of incentive Pareto optimality, which extends the classical Pareto efficiency to settings of information asymmetry, and is constrained by requirements of incentive compatibility and individual rationality on optimal menus of contracts.

Our first main result shows that, for general concave utility functionals, a menu of insurance contracts is incentive efficient if and only if it maximizes a social welfare function, subject to individual rationality and incentive compatibility constraints. This provides an important extension of the classical Negishi characterization of Pareto optima in insurance markets, to situations characterized by (i) general concave utility functionals, beyond Expected-Utility Theory; (ii) information asymmetry, whereby both the riskiness and the risk attitude of the agent is hidden information; and (iii) the type space is a continuum. To the best of our knowledge, this is the first result in this direction, and it provides a significant extension of the classical results.

Under Yaari’s Dual Utility, we characterize incentive-efficient menus of contracts, and we show that under two distinct assumptions on the ordering of the type space, and with some regularity conditions, the optimal contract can either provide full coverage, or exhibit a layered structure of marginal retention functions, depending on the level of the social weight. In addition, the optimal retention and the optimal premium are both monotone in the agent’s type, with higher types receiving more coverage at the optimum in exchange for higher premium payments. Efficiency at the top holds, whereby full coverage is provided to the highest type. The insurer extracts all of the surplus from the lowest type agent, who is indifferent between participating and not participating at the optimum. Moreover, we show that, as the agent faces stochastically larger losses, their utility from the optimal menu decreases. We also study the variation of the insurer’s utility across types at the optimum, when a separating equilibrium holds. Particularly, if the agent is offered full coverage, the insurer benefits more from lower types of the agent that face smaller losses. If, on the other hand, the agent retains the entire loss, the insurer is indifferent in participating in the market. Finally, when partial coverage is offered, the insurer benefits more from higher types if a certain condition holds.

## Appendix A Mathematical Background

Consider a finite nonnegative measure space (Θ,Ω,μ)(\Theta,\Omega,\mu) and a Banach space (X,∥⋅∥X)(X,\|\cdot\|\_{X}).

### A.1. Bochner Integrability

###### Definition A.1.

A function u:Θ→Xu:\Theta\to X is called μ\mu-measurable (or strongly measurable), if there exists a sequence of simple functions (un)n(u\_{n})\_{n}, where un:Θ→Xu\_{n}:\Theta\to X for each n≥1n\geq 1, such that limn→∞​un=u\underset{n\to\infty}{\lim}u\_{n}=u, pointwise on Θ\Theta.

###### Definition A.2.

A strongly measurable function u:Θ→Xu:\Theta\to X is Bochner integrable if there is a sequence of simple functions (un)n(u\_{n})\_{n} such that un→uu\_{n}\to u pointwise almost everywhere in Θ\Theta, and

|  |  |  |
| --- | --- | --- |
|  | limn→∞​∫Θ‖un​(θ)−u​(θ)‖X​𝑑μ=0\underset{n\to\infty}{\lim}\int\_{\Theta}\|u\_{n}(\theta)-u(\theta)\|\_{X}\,d\mu=0 |  |

The Bochner integral of uu is then defined as

|  |  |  |
| --- | --- | --- |
|  | ∫Θu​(θ)​𝑑μ:=l​i​mn→∞​∫Θun​(θ)​𝑑μ.\int\_{\Theta}u(\theta)\,d\mu:=\underset{n\to\infty}{lim}\int\_{\Theta}u\_{n}(\theta)\,d\mu. |  |

###### Definition A.3.

A strongly measurable function u:Θ→Xu:\Theta\to X is said to be Bochner integrable with respect to μ\mu if and only if ∫Θ‖u​(θ)‖X​𝑑μ<∞.\int\_{\Theta}\|u(\theta)\|\_{X}\,d\mu<\infty.

###### Definition A.4.

The Bochner space Lp​(Θ;X)L^{p}(\Theta;X), p∈[1,∞)p\in[1,\infty) is defined as the space of all strongly measurable functions u:Θ→Xu:\Theta\to X, with ∫Θ‖u​(θ)‖Xp​𝑑μ<+∞\int\_{\Theta}\|u(\theta)\|\_{X}^{p}\,d\mu<+\infty.
Lp​(Θ,X)L^{p}(\Theta,X) is endowed with the norm ∥⋅∥Lp\|\cdot\|\_{L^{p}} defined as follows:

|  |  |  |
| --- | --- | --- |
|  | ‖u‖Lp=(∫Θ‖u​(θ)‖Xp​𝑑μ)1p,u∈Lp​(Θ,X).\|u\|\_{L^{p}}=\left(\int\_{\Theta}\|u(\theta)\|\_{X}^{p}\,d\mu\right)^{\frac{1}{p}},\,\,u\in L^{p}(\Theta,X). |  |

We now consider the Banach space ℝ2\mathbb{R}^{2} and we assume hereafter that ℝ2\mathbb{R}^{2} is equipped with the Euclidean norm ∥⋅∥ℝ2\|\cdot\|\_{\mathbb{R}^{2}}.

By Definition [A.4](https://arxiv.org/html/2602.09967v1#A1.Thmtheorem4 "Definition A.4. ‣ A.1. Bochner Integrability ‣ Appendix A Mathematical Background ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), Lp​(Θ;ℝ2)L^{p}(\Theta;\mathbb{R}^{2}) for p∈(1,∞)p\in(1,\infty) denotes the Bochner space of all strongly measurable functions u:Θ→ℝ2u:\Theta\to\mathbb{R}^{2}, with ∫Θ‖u​(θ)‖ℝ2p​𝑑μ<∞\int\_{\Theta}\|u(\theta)\|\_{\mathbb{R}^{2}}^{p}\,d\mu<\infty.
Moreover, for u=(u1,u2)∈Lp​(Θ,ℝ2)u=(u\_{1},u\_{2})\in L^{p}(\Theta,\mathbb{R}^{2}) and θ∈Θ\theta\in\Theta, the Bochner integral of uu is given by:

|  |  |  |
| --- | --- | --- |
|  | ∫Θu​(θ)​𝑑μ=(∫Θu1​(θ)​𝑑μ,∫Θu2​(θ)​𝑑μ).\int\_{\Theta}u(\theta)\,d\mu=\left(\int\_{\Theta}u\_{1}(\theta)\,d\mu,\int\_{\Theta}u\_{2}(\theta)\,d\mu\right). |  |

###### Remark A.5.

By standard results on Bochner integration, Lp​(Θ;ℝ2)L^{p}(\Theta;\mathbb{R}^{2}) is a Banach space (Diestel and Uhl, [1977](https://arxiv.org/html/2602.09967v1#bib.bib53 "Vector measures"), Chap. 2). In particular, for u,v∈Lp​(Θ,ℝ2)u,v\in L^{p}(\Theta,\mathbb{R}^{2}), u+v∈Lp​(Θ,ℝ2)u+v\in L^{p}(\Theta,\mathbb{R}^{2}) and α​u∈Lp​(Θ,ℝ2)\alpha\,u\in L^{p}(\Theta,\mathbb{R}^{2}), for all α∈ℝ\alpha\in\mathbb{R}.

### A.2. Functional-Analytic Background

Consider any normed space NN, and denote by N∗N^{\*} (resp. N∗∗N^{\*\*}) the dual (resp. bidual) of NN.

###### Definition A.6.

Consider the canonical map

|  |  |  |  |
| --- | --- | --- | --- |
|  | JN:N\displaystyle J\_{N}:N | →N∗∗\displaystyle\to N^{\*\*} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | n\displaystyle n | ↦JN​(n),\displaystyle\mapsto J\_{N}(n), |  |

where JN​(n)​(f):=f​(n),∀f∈N∗J\_{N}(n)(f):=f(n),\ \forall f\in N^{\*}.
The normed space NN is said to be reflexive if the canonical map JNJ\_{N} is surjective, thereby establishing an isometric isomorphism between NN and N∗∗N^{\*\*}.

###### Remark A.7.

The following holds:

1. (1)

   Every finite dimensional normed space is reflexive.
2. (2)

   Every reflexive space is a Banach space.

The normed space ℝ2\mathbb{R}^{2} is finite dimensional since the basis of ℝ2\mathbb{R}^{2} is given by the set {e1=(1,0),e2=(0,1)}\{e\_{1}=(1,0),e\_{2}=(0,1)\}, and hence dim(ℝ2)=2\dim(\mathbb{R}^{2})=2. It follows from Remark [A.7](https://arxiv.org/html/2602.09967v1#A1.Thmtheorem7 "Remark A.7. ‣ A.2. Functional-Analytic Background ‣ Appendix A Mathematical Background ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") that ℝ2\mathbb{R}^{2} is reflexive.

###### Remark A.8.

If XX is reflexive and 1<p<∞1<p<\infty, then the space of XX-valued measurable functions Lp​(Θ,X)L^{p}(\Theta,X) is reflexive.

It follows from Remark [A.8](https://arxiv.org/html/2602.09967v1#A1.Thmtheorem8 "Remark A.8. ‣ A.2. Functional-Analytic Background ‣ Appendix A Mathematical Background ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") that Lp​(Θ,ℝ2)L^{p}(\Theta,\mathbb{R}^{2}) is reflexive for 1<p<∞1<p<\infty, since ℝ2\mathbb{R}^{2} is reflexive.

###### Theorem A.9.

The Banach space XX is reflexive if and only if the closed unit ball in XX is weakly compact.

The above Theorem follows from the Banach-Alaoglu theorem. See (Conway, [2019](https://arxiv.org/html/2602.09967v1#bib.bib54 "A course in functional analysis"), Chap. V, Theorem 4.2) for a proof.

###### Definition A.10.

A topological space is said to be a Hausdorff space if for any distinct elements uu and vv, there exists open neighborhoods H1H\_{1} and H2H\_{2}, such that u∈H1u\in H\_{1}, v∈H2v\in H\_{2}, and H1∩H2=∅H\_{1}\cap H\_{2}=\varnothing.

###### Definition A.11.

A topological vector space is said to be locally convex if it is Hausdorff and every neighborhood of 0 contains a convex neighborhood of 0.

###### Proposition A.12.

The space Lp​(Θ,ℝ2)L^{p}(\Theta,\mathbb{R}^{2}) of ℝ2\mathbb{R}^{2}-valued strongly measurable functions is a Hausdorff space. In addition, it is locally convex.

### A.3. Separation and Duality

###### Theorem A.13.

If K1K\_{1} and K2K\_{2} are two disjoint closed convex subsets of a locally convex Hausdorff linear space 𝒦\mathcal{K}, and if in addition K1K\_{1} is weakly compact, then there exists a continuous linear functional ψ\psi on 𝒦\mathcal{K} such that,

|  |  |  |
| --- | --- | --- |
|  | supk2∈K2​ψ​(k2)<infk1∈K1​ψ​(k1).\underset{k\_{2}\in K\_{2}}{\sup}\psi(k\_{2})<\underset{k\_{1}\in K\_{1}}{\inf}\psi(k\_{1}). |  |

The above Theorem states that any two closed convex subsets of a locally convex Hausdorff linear space 𝒦\mathcal{K} can be strictly separated by a continuous linear functional on 𝒦\mathcal{K}. This is due to Klee ([1951](https://arxiv.org/html/2602.09967v1#bib.bib52 "Convex sets in linear spaces")).

###### Definition A.14.

The Banach space XX is said to have the Radon-Nikodym property (RNP) with respect to the measure space (Θ,Ω,μ)(\Theta,\Omega,\mu) if for every XX-valued measure ζ\zeta of bounded variation that is absolutely continuous with respect to μ\mu, there exists a Bochner-integrable function δ\delta such that:

|  |  |  |
| --- | --- | --- |
|  | ζ​(A)=∫Aδ​𝑑μ,∀A∈ℬ​(Θ).\zeta(A)=\int\_{A}\delta\,d\mu,\,\,\forall\,A\in\mathcal{B}(\Theta). |  |

XX is said to have the Radon-Nikodym property if XX has the Radon-Nikodym property for each probability space.

###### Remark A.15.

If XX is reflexive then XX has the Radon-Nikodym property (see Diestel and Uhl ([1977](https://arxiv.org/html/2602.09967v1#bib.bib53 "Vector measures"))).

###### Theorem A.16.

The dual of Lp​(Θ,X)L^{p}(\Theta,X) is given by Lp​(Θ;X)∗=Lq​(Θ;X∗)L^{p}(\Theta;X)^{\*}=L^{q}(\Theta;X^{\*}), where 1p+1q=1\frac{1}{p}+\frac{1}{q}=1 if and only if X∗X^{\*} has the Radon-Nikodym property.

Moreover, when X∗X^{\*} has the Radon-Nikodym property, every continuous linear functional ℓ\ell on Lp​(Θ,X)L^{p}(\Theta,X) can be represented uniquely by some g∈Lq​(Θ;X∗)g\in L^{q}(\Theta;X^{\*}), as follows:

|  |  |  |
| --- | --- | --- |
|  | ℓ​(f)=∫Θ⟨g​(θ),f​(θ)⟩​𝑑μ,∀f∈Lp​(Θ;X),\ell(f)=\int\_{\Theta}\langle g(\theta),f(\theta)\rangle\,d\mu,\,\,\forall\,f\in L^{p}(\Theta;X), |  |

where ⟨g​(θ),f​(θ)⟩\langle g(\theta),f(\theta)\rangle is the dual pairing.

###### Proof.

Diestel and Uhl ([1977](https://arxiv.org/html/2602.09967v1#bib.bib53 "Vector measures")) Chapter 4, Theorem 1.
∎

###### Proposition A.17.

The dual of Lp​(Θ;ℝ2)L^{p}(\Theta;\mathbb{R}^{2}) is given by (Lp​(Θ;ℝ2))∗=Lq​(Θ;ℝ2),where 1p+1q=1;\left(L^{p}(\Theta;\mathbb{R}^{2})\right)^{\*}=L^{q}(\Theta;\mathbb{R}^{2}),\ \text{where $\frac{1}{p}+\frac{1}{q}=1$};
and every continuous linear functional ℓ\ell on Lp​(Θ;ℝ2)L^{p}(\Theta;\mathbb{R}^{2}) can be represented uniquely by some g=(g1,g2)∈Lq​(Θ;ℝ2)g=(g\_{1},g\_{2})\in L^{q}(\Theta;\mathbb{R}^{2}) such that:

|  |  |  |
| --- | --- | --- |
|  | ℓ​(f)=∫Θf1​(θ)​g1​(θ)​𝑑μ+∫Θf2​(θ)​g2​(θ)​𝑑μ,\ell(f)=\int\_{\Theta}f\_{1}(\theta)g\_{1}(\theta)\,d\mu+\int\_{\Theta}f\_{2}(\theta)g\_{2}(\theta)\,d\mu, |  |

for all f=(f1,f2)∈Lp​(Θ;ℝ2)f=(f\_{1},f\_{2})\in L^{p}(\Theta;\mathbb{R}^{2}) and θ∈Θ\theta\in\Theta. Moreover, |ℓ​(f)|<+∞|\ell(f)|<+\infty.

###### Proof.

Since ℝ2\mathbb{R}^{2} is reflexive, it has the Radon-Nikodym property, by Remark [A.15](https://arxiv.org/html/2602.09967v1#A1.Thmtheorem15 "Remark A.15. ‣ A.3. Separation and Duality ‣ Appendix A Mathematical Background ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
It follows from Theorem [A.16](https://arxiv.org/html/2602.09967v1#A1.Thmtheorem16 "Theorem A.16. ‣ A.3. Separation and Duality ‣ Appendix A Mathematical Background ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") that the dual space of Lp​(Θ,ℝ2)L^{p}(\Theta,\mathbb{R}^{2}) is given by Lq​(Θ,ℝ2)L^{q}(\Theta,\mathbb{R}^{2}), where 1p+1q=1\frac{1}{p}+\frac{1}{q}=1. By Theorem [A.16](https://arxiv.org/html/2602.09967v1#A1.Thmtheorem16 "Theorem A.16. ‣ A.3. Separation and Duality ‣ Appendix A Mathematical Background ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), this duality ensures that for the continuous linear functional ℓ\ell, there exists a unique g=(g1,g2)∈Lq​(Θ,ℝ2)g=(g\_{1},g\_{2})\in L^{q}(\Theta,\mathbb{R}^{2}) such that:

|  |  |  |
| --- | --- | --- |
|  | ℓ​(f)=∫Θ⟨f​(θ),g​(θ)⟩ℝ2​𝑑μ=∫Θf1​(θ)​g1​(θ)​𝑑μ+∫Θf2​(θ)​g2​(θ)​𝑑μ.\ell(f)=\int\_{\Theta}\left<f(\theta),g(\theta)\right>\_{\mathbb{R}^{2}}\,d\mu=\int\_{\Theta}f\_{1}(\theta)g\_{1}(\theta)d\mu+\int\_{\Theta}f\_{2}(\theta)g\_{2}(\theta)\,d\mu\,. |  |

Moreover,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |ℓ​(f)|=|∫Θ⟨f,g⟩ℝ2​𝑑μ|≤∫Θ|⟨f,g⟩ℝ2|​𝑑μ\displaystyle|\ell(f)|=\left|\int\_{\Theta}\left<f,g\right>\_{\mathbb{R}^{2}}\,d\mu\right|\leq\int\_{\Theta}\left|\left<f,g\right>\_{\mathbb{R}^{2}}\,\right|d\mu | ≤∫Θ‖f‖ℝ2​‖g‖ℝ2​𝑑μ,by Cauchy-Schwarz\displaystyle\leq\int\_{\Theta}\|f\|\_{\mathbb{R}^{2}}\ \|g\|\_{\mathbb{R}^{2}}\ d\mu,\ \text{by Cauchy-Schwarz} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤‖f‖Lp​‖g‖Lq​by Holder’s inequality,\displaystyle\leq\|f\|\_{L^{p}}\|g\|\_{L^{q}}\ \text{by Holder's inequality,} |  |

where ‖f‖Lp<+∞\|f\|\_{L^{p}}<+\infty and ‖g‖Lq<+∞\|g\|\_{L^{q}}<+\infty by Definition [A.4](https://arxiv.org/html/2602.09967v1#A1.Thmtheorem4 "Definition A.4. ‣ A.1. Bochner Integrability ‣ Appendix A Mathematical Background ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), since f∈Lp​(Θ;ℝ2)f\in L^{p}(\Theta;\mathbb{R}^{2}) and g∈Lq​(Θ;ℝ2)g\in L^{q}(\Theta;\mathbb{R}^{2}). Hence, |ℓ​(f)|<+∞|\ell(f)|<+\infty.
∎

## Appendix B Proofs of Main Results

### B.1. Proof of Theorem [3.8](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem8 "Theorem 3.8. ‣ 3.2. Social Welfare Maximization ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")

This theorem is proved in two directions.

The only if direction:
Assume that (Iθ∗,pθ∗)θ∈Θ∈ℐ​𝒫​𝒪(I\_{\theta}^{\*},p^{\*}\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{P}\mathcal{O}. We will show that there exists some α∈(0,1]\alpha\in(0,1], and a probability measure η\eta with μ\mu absolutely continuous with respect to η\eta, such that the menu (Iθ∗,pθ∗)θ∈Θ(I\_{\theta}^{\*},p^{\*}\_{\theta})\_{\theta\in\Theta} is optimal for the social welfare maximization ([1](https://arxiv.org/html/2602.09967v1#S3.E1 "Equation 1 ‣ Theorem 3.8. ‣ 3.2. Social Welfare Maximization ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")), subject to incentive compatibility and individual rationality.

We know from Assumption [3.7](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem7 "Assumption 3.7. ‣ 3.2. Social Welfare Maximization ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") that there exists p∈(1,+∞)p\in(1,+\infty) such that, for every menu of contracts (Iθ,pθ)θ∈Θ∈ℐ​ℛ∩ℐ​𝒞(I\_{\theta},p\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{R}\cap\mathcal{I}\mathcal{C}, the map

|  |  |  |  |
| --- | --- | --- | --- |
|  | u:Θ\displaystyle u:\Theta | →ℝ2\displaystyle\to\mathbb{R}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | θ\displaystyle\theta | ↦u​(θ):=(Uθ​(Iθ,pθ),∫ΘVϑ​(Iϑ,pϑ)​𝑑μ)\displaystyle\mapsto u(\theta):=\Big(U\_{\theta}(I\_{\theta},p\_{\theta}),\int\_{\Theta}V\_{\vartheta}(I\_{\vartheta},p\_{\vartheta})\,d\mu\Big) |  |

belongs to Lp​(Θ;ℝ2)L^{p}(\Theta;\mathbb{R}^{2}).
For this pp, define KK as the set of ℝ2\mathbb{R}^{2}-valued functions u∈Lp​(Θ,ℝ2)u\in L^{p}(\Theta,\mathbb{R}^{2}) of the above form. Specifically,

|  |  |  |
| --- | --- | --- |
|  | K:={u∈Lp​(Θ;ℝ2);u​(θ)=(Uθ​(Iθ,pθ),∫ΘVϑ​(Iϑ,pϑ)​𝑑μ),where​(Iθ,pθ)θ∈Θ∈ℐ​ℛ∩ℐ​𝒞}.K:=\left\{u\in L^{p}(\Theta;\mathbb{R}^{2})\,;u(\theta)=\left(U\_{\theta}(I\_{\theta},p\_{\theta}),\int\_{\Theta}V\_{\vartheta}(I\_{\vartheta},p\_{\vartheta})\,d\mu\right),\text{where}\,(I\_{\theta},p\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{R}\cap\mathcal{I}\mathcal{C}\right\}. |  |

Moreover, it follows from Assumption [3.7](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem7 "Assumption 3.7. ‣ 3.2. Social Welfare Maximization ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") that the set KK is bounded in Lp​(Θ,ℝ2)L^{p}(\Theta,\mathbb{R}^{2}). We define 𝒰\mathcal{U} to be the closed convex hull of the set KK. That is,

|  |  |  |
| --- | --- | --- |
|  | 𝒰=c​o¯​(K).\mathcal{U}=\bar{co}(K). |  |

We show that the set 𝒰\mathcal{U} is weakly compact.
First, since ℝ2\mathbb{R}^{2} is reflexive and p∈(1,+∞)p\in(1,+\infty), then Lp​(Θ,ℝ2)L^{p}(\Theta,\mathbb{R}^{2}) is also reflexive (Remark [A.8](https://arxiv.org/html/2602.09967v1#A1.Thmtheorem8 "Remark A.8. ‣ A.2. Functional-Analytic Background ‣ Appendix A Mathematical Background ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")).
The set 𝒰⊂Lp​(Θ;ℝ2)\mathcal{U}\subset L^{p}(\Theta;\mathbb{R}^{2}) is closed, convex by definition, and bounded since KK is bounded.
The boundedness of 𝒰\mathcal{U} implies that there exists some κ<+∞\kappa<+\infty, such that 𝒰⊂κ​B\mathcal{U}\subset\kappa B, where BB is the closed unit ball of Lp​(Θ,ℝ2)L^{p}(\Theta,\mathbb{R}^{2}).
In the reflexive Banach space Lp​(Θ,ℝ2)L^{p}(\Theta,\mathbb{R}^{2}), the closed unit ball BB is weakly compact (Theorem [A.9](https://arxiv.org/html/2602.09967v1#A1.Thmtheorem9 "Theorem A.9. ‣ A.2. Functional-Analytic Background ‣ Appendix A Mathematical Background ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")).
Therefore κ​B\kappa B is weakly compact. Hence 𝒰\mathcal{U} is a closed subset of a weakly compact set, and so 𝒰\mathcal{U} is weakly compact.

For a fixed ε>0\varepsilon>0, we define the convex set 𝒱ε\mathcal{V}\_{\varepsilon} as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒱ε\displaystyle\mathcal{V}\_{\varepsilon} | :={ϕ∈Lp​(Θ;ℝ2),ϕ​(θ)=(ϕ1​(θ),ϕ2​(θ));ϕ1​(θ)≥Uθ​(Iθ∗,pθ∗),ϕ2​(θ)≥Π∗+ε;μ​-a.e},\displaystyle:=\left\{\phi\in L^{p}(\Theta;\mathbb{R}^{2}),\,\phi(\theta)=\Big(\phi\_{1}(\theta),\phi\_{2}(\theta)\Big);\,\,\phi\_{1}(\theta)\geq U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\,\,,\,\,\phi\_{2}(\theta)\geq\Pi^{\*}+\varepsilon;\,\,\mu\text{-a.e}\right\}, |  |

where Π∗=∫ΘVϑ​(Iϑ∗,pϑ∗)​𝑑μ\Pi^{\*}=\int\_{\Theta}V\_{\vartheta}(I^{\*}\_{\vartheta},p^{\*}\_{\vartheta})d\mu.
We now show that 𝒱ε\mathcal{V}\_{\varepsilon} is closed.
Consider a sequence (ϕn)n∈𝒱ε(\phi\_{n})\_{n}\in\mathcal{V}\_{\varepsilon}, such that ϕn​→Lp​ϕ\phi\_{n}\underset{L^{p}}{\to}\phi, as n→∞n\to\infty. We show that ϕ∈𝒱ε\phi\in\mathcal{V}\_{\varepsilon}.
Since (ϕn)n∈𝒱ε(\phi\_{n})\_{n}\in\mathcal{V}\_{\varepsilon}, it follows that ϕn=(ϕn,1,ϕn,2)\phi\_{n}=(\phi\_{n,1},\phi\_{n,2}), such that for θ∈Θ\theta\in\Theta,

|  |  |  |
| --- | --- | --- |
|  | ϕn,1​(θ)≥Uθ​(Iθ∗,pθ∗),and​ϕn,2​(θ)≥Π∗+ε.\phi\_{n,1}(\theta)\geq U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta}),\ \text{and}\ \phi\_{n,2}(\theta)\geq\Pi^{\*}+\varepsilon. |  |

The limit of ϕn\phi\_{n} is given by ϕ=(ϕ1,ϕ2)\phi=(\phi\_{1},\phi\_{2}). Then, applying the limit as n→∞n\to\infty for both inequalities, it follows that for θ∈Θ\theta\in\Theta, ϕ1​(θ)≥Uθ​(Iθ∗,pθ∗)\phi\_{1}(\theta)\geq U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta}), and ϕ2​(θ)≥Π∗+ε\phi\_{2}(\theta)\geq\Pi^{\*}+\varepsilon. Hence ϕ∈𝒱ε\phi\in\mathcal{V}\_{\varepsilon}, and therefore 𝒱ε\mathcal{V}\_{\varepsilon} is closed.

The following Lemma provides a characterization of elements of 𝒱ε\mathcal{V}\_{\varepsilon}.

###### Lemma B.1.

Consider ϕ∈𝒱ε\phi\in\mathcal{V}\_{\varepsilon}, and some function h∈Lp​(Θ,ℝ2)h\in L^{p}(\Theta,\mathbb{R}^{2}), such that the ℝ2\mathbb{R}^{2}-valued function hh is given by h​(θ)=(h1​(θ),h2​(θ))≥(0,0)h(\theta)=(h\_{1}(\theta),h\_{2}(\theta))\geq(0,0), for all θ∈Θ\theta\in\Theta. Then, we have the following:

1. (1)

   ϕ+h∈𝒱ε\phi+h\in\mathcal{V}\_{\varepsilon}.
2. (2)

   For all θ∈Θ\theta\in\Theta, let ϕmin​(θ):=(Uθ​(Iθ∗,pθ∗),Π∗+ε)∈𝒱ε\phi\_{\min}(\theta):=\bigg(U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta}),\,\Pi^{\*}+\varepsilon\bigg)\in\mathcal{V}\_{\varepsilon}, where Π∗=∫ΘVϑ​(Iϑ∗,pϑ∗)​𝑑μ\Pi^{\*}=\int\_{\Theta}V\_{\vartheta}(I^{\*}\_{\vartheta},p^{\*}\_{\vartheta})\,d\mu.
   Then ϕ≥ϕmin\phi\geq\phi\_{\min}, for any ϕ∈𝒱ε\phi\in\mathcal{V}\_{\varepsilon}, and ϕ∈𝒱ε\phi\in\mathcal{V}\_{\varepsilon} if and only if

   |  |  |  |
   | --- | --- | --- |
   |  | ϕ=ϕmin+h,for some ​h∈ℋ,\phi=\phi\_{\min}+h,\,\,\hbox{for some }h\in\mathcal{H}, |  |

   where ℋ:={h∈Lp​(θ,ℝ2);h≥0}.\mathcal{H}:=\left\{h\in L^{p}(\theta,\mathbb{R}^{2});h\geq 0\right\}.

###### Proof.

Consider ϕ∈𝒱ε\phi\in\mathcal{V}\_{\varepsilon}, and h=(h1,h2)∈Lp​(Θ;ℝ2)h=(h\_{1},h\_{2})\in L^{p}(\Theta;\mathbb{R}^{2}) such that h1,h2≥0h\_{1},h\_{2}\geq 0.

(1) We may note first that ϕ+h∈Lp​(Θ,ℝ2)\phi+h\in L^{p}(\Theta,\mathbb{R}^{2}), since ϕ\phi and hh are in Lp​(Θ,ℝ2)L^{p}(\Theta,\mathbb{R}^{2}). Moreover, since ϕ∈𝒱ε\phi\in\mathcal{V}\_{\varepsilon}, it follows that for θ∈Θ\theta\in\Theta and for a fixed ε>0\varepsilon>0, we have:

|  |  |  |
| --- | --- | --- |
|  | ϕ1​(θ)≥Uθ​(Iθ∗,pθ∗),and​ϕ2​(θ)≥Π∗+ε.\phi\_{1}(\theta)\geq U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta}),\ \text{and}\ \phi\_{2}(\theta)\geq\Pi^{\*}+\varepsilon. |  |

For h∈Lp​(Θ,ℝ2)h\in L^{p}(\Theta,\mathbb{R}^{2}), h1,h2≥0h\_{1},h\_{2}\geq 0, the following holds:

|  |  |  |
| --- | --- | --- |
|  | ϕ1​(θ)+h1​(θ)≥Uθ​(Iθ∗,pθ∗)+h1​(θ)≥Uθ​(Iθ∗,pθ∗),\phi\_{1}(\theta)+h\_{1}(\theta)\geq U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})+h\_{1}(\theta)\geq U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta}), |  |

and

|  |  |  |
| --- | --- | --- |
|  | ϕ2​(θ)+h2​(θ)≥Π∗+ε+h2​(θ)≥Π∗+ε.\phi\_{2}(\theta)+h\_{2}(\theta)\geq\Pi^{\*}+\varepsilon+h\_{2}(\theta)\geq\Pi^{\*}+\varepsilon. |  |

This implies that ϕ+h∈𝒱ε\phi+h\in\mathcal{V}\_{\varepsilon}.

(2) Assume ϕ∈𝒱ε\phi\in\mathcal{V}\_{\varepsilon}. Then for each θ∈Θ\theta\in\Theta, and for a fixed ε>0\varepsilon>0,

|  |  |  |
| --- | --- | --- |
|  | ϕ1​(θ)≥Uθ​(Iθ∗,pθ∗),and​ϕ2​(θ)≥Π∗+ε.\phi\_{1}(\theta)\geq U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta}),\,\,\,\text{and}\,\,\,\phi\_{2}(\theta)\geq\Pi^{\*}+\varepsilon. |  |

That is,

|  |  |  |
| --- | --- | --- |
|  | ϕ1​(θ)≥ϕmin,1​(θ),and​ϕ2​(θ)≥ϕmin,2​(θ).\phi\_{1}(\theta)\geq\phi\_{\min,1}(\theta),\,\,\,\text{and}\,\,\,\phi\_{2}(\theta)\geq\phi\_{\min,2}(\theta). |  |

Therefore, there exists some h∈Lp​(Θ,ℝ2)h\in L^{p}(\Theta,\mathbb{R}^{2}), such that h≥0h\geq 0, that satisfies

|  |  |  |
| --- | --- | --- |
|  | ϕ1​(θ)=ϕmin,1​(θ)+h1​(θ)\phi\_{1}(\theta)=\phi\_{\min,1}(\theta)+h\_{1}(\theta) |  |

and,

|  |  |  |
| --- | --- | --- |
|  | ϕ2​(θ)=ϕmin,2​(θ)+h2​(θ).\phi\_{2}(\theta)=\phi\_{\min,2}(\theta)+h\_{2}(\theta). |  |

Hence, if ϕ∈𝒱ε\phi\in\mathcal{V}\_{\varepsilon}, then ϕ=ϕmin+h\phi=\phi\_{\min}+h, where h∈Lp​(Θ,ℝ2)h\in L^{p}(\Theta,\mathbb{R}^{2}) and h≥0h\geq 0.

Conversely, consider now ϕ=ϕmin+h\phi=\phi\_{\min}+h, where h∈ℋh\in\mathcal{H}, and ϕmin∈𝒱ε\phi\_{\min}\in\mathcal{V}\_{\varepsilon}, then by Lemma [B.1](https://arxiv.org/html/2602.09967v1#A2.Thmtheorem1 "Lemma B.1. ‣ B.1. Proof of Theorem 3.8 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")-([1](https://arxiv.org/html/2602.09967v1#A2.I1.i1 "Item 1 ‣ Lemma B.1. ‣ B.1. Proof of Theorem 3.8 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) it follows that ϕ∈𝒱ε\phi\in\mathcal{V}\_{\varepsilon}.
∎

We now show that the two sets 𝒰\mathcal{U} and 𝒱ε\mathcal{V}\_{\varepsilon} are disjoint.
We assume for the sake fo contradiction that there exists some ϕ∈𝒰∩𝒱ε\phi\in\mathcal{U}\cap\mathcal{V}\_{\varepsilon}. Then there exists βk≥0\beta\_{k}\geq 0, k∈{1,…,m}k\in\{1,\ldots,m\} such that ∑k=1mβk=1\sum\_{k=1}^{m}\beta\_{k}=1, and for θ∈Θ\theta\in\Theta:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ​(θ)\displaystyle\phi(\theta) | =∑k=1mβk​(Uθ​(Iθ(k),pθ(k)),Π(k))​ since ϕ∈𝒰, where Π(k)=∫ΘVϑ​(Iϑ(k),pϑ(k))​𝑑μ.\displaystyle=\sum\_{k=1}^{m}\beta\_{k}\left(U\_{\theta}(I^{(k)}\_{\theta},p^{(k)}\_{\theta}),\Pi^{(k)}\right)\,\,\text{ since $\phi\in\mathcal{U}$, where $\Pi^{(k)}=\int\_{\Theta}V\_{\vartheta}(I\_{\vartheta}^{(k)},p\_{\vartheta}^{(k)})\,d\mu$.} |  |

Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ​(θ)\displaystyle\phi(\theta) | =(∑k=1mβk​Uθ​(Iθ(k),pθ(k)),∑k=1mβk​Π(k))≥(Uθ​(Iθ∗,pθ∗),Π∗+ε)​ μ -a.e, since ϕ∈𝒱ε.\displaystyle=\left(\sum\_{k=1}^{m}\beta\_{k}U\_{\theta}(I^{(k)}\_{\theta},p^{(k)}\_{\theta}),\sum\_{k=1}^{m}\beta\_{k}\Pi^{(k)}\right)\geq\Big(U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta}),\Pi^{\*}+\varepsilon\Big)\ \text{ $\mu$ -a.e, \ since $\phi\in\mathcal{V}\_{\varepsilon}$}. |  |

That is:

|  |  |  |
| --- | --- | --- |
|  | ∑k=1mβk​Uθ​(Iθ(k),pθ(k))≥Uθ​(Iθ∗,pθ∗)​ and ​∑k=1mβk​Π(k)≥Π∗+ε;μ​-a.e.\sum\_{k=1}^{m}\beta\_{k}U\_{\theta}(I^{(k)}\_{\theta},p^{(k)}\_{\theta})\geq U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\,\,\text{ and }\,\,\sum\_{k=1}^{m}\beta\_{k}\Pi^{(k)}\geq\Pi^{\*}+\varepsilon;\,\,\mu\text{-a.e.} |  |

Let

|  |  |  |
| --- | --- | --- |
|  | I¯θ:=∑k=1mβk​Iθ(k)​ and p¯θ:=∑k=1mβK​pθ(k).\bar{I}\_{\theta}:=\sum\_{k=1}^{m}\beta\_{k}I\_{\theta}^{(k)}\ \text{ and }\ \ \bar{p}\_{\theta}:=\sum\_{k=1}^{m}\beta\_{K}p\_{\theta}^{(k)}\,. |  |

Then by concavity of UθU\_{\theta} and VθV\_{\theta} for each θ∈Θ\theta\in\Theta as per Assumption [3.6](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem6 "Assumption 3.6. ‣ 3.2. Social Welfare Maximization ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Uθ​(I¯θ,p¯θ)\displaystyle U\_{\theta}(\bar{I}\_{\theta},\bar{p}\_{\theta}) | =Uθ​(∑k=1mβk​Iθ(k),∑k=1mβk​pθ(k))≥∑k=1mβk​Uθ​(Iθ(k),pθ(k))≥Uθ​(Iθ∗,pθ∗),μ-a.e.,\displaystyle=U\_{\theta}\left(\sum\_{k=1}^{m}\beta\_{k}I\_{\theta}^{(k)},\sum\_{k=1}^{m}\beta\_{k}p\_{\theta}^{(k)}\right)\geq\sum\_{k=1}^{m}\beta\_{k}\,U\_{\theta}(I\_{\theta}^{(k)},p\_{\theta}^{(k)})\geq U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta}),\ \text{$\mu$-a.e.,} |  |

and,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ΘVθ​(I¯θ,p¯θ)​𝑑μ=∫ΘVθ​(∑k=1m(Iθ(k),pθ(k)))​𝑑μ\displaystyle\int\_{\Theta}V\_{\theta}\big(\bar{I}\_{\theta},\bar{p}\_{\theta}\big)\,d\mu=\int\_{\Theta}V\_{\theta}\left(\sum\_{k=1}^{m}(I\_{\theta}^{(k)},p\_{\theta}^{(k)})\right)\,d\mu | ≥∫Θ∑k=1mβk​Vθ​(Iθ(k),pθ(k))​d​μ\displaystyle\geq\int\_{\Theta}\sum\_{k=1}^{m}\beta\_{k}V\_{\theta}\left(I\_{\theta}^{(k)},p\_{\theta}^{(k)}\right)d\mu |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑k=1mβk​Π(k)≥Π∗+ε>Π∗,μ-a.e.,\displaystyle=\sum\_{k=1}^{m}\beta\_{k}\Pi^{(k)}\geq\Pi^{\*}+\varepsilon>\Pi^{\*},\ \text{$\mu$-a.e.}, |  |

since ε>0\varepsilon>0. Hence,

|  |  |  |
| --- | --- | --- |
|  | ∫ΘVθ​(I¯θ,p¯θ)​𝑑μ>∫ΘVθ​(Iθ∗,pθ∗)​𝑑μ.\int\_{\Theta}V\_{\theta}\big(\bar{I}\_{\theta},\bar{p}\_{\theta}\big)\,d\mu>\int\_{\Theta}V\_{\theta}\big(I^{\*}\_{\theta},p^{\*}\_{\theta}\big)\,d\mu. |  |

This contradicts the fact that the menu (Iθ∗,pθ∗)θ∈Θ(I^{\*}\_{\theta},p^{\*}\_{\theta})\_{\theta\in\Theta} is IPO. Consequently, 𝒰\mathcal{U} and 𝒱ε\mathcal{V}\_{\varepsilon} are disjoint.
Since 𝒰\mathcal{U} and 𝒱ε\mathcal{V}\_{\varepsilon} are two disjoint closed convex subsets of Lp​(Θ;ℝ2)L^{p}(\Theta;\mathbb{R}^{2}) with 𝒰\mathcal{U} weakly compact, then it follows from Theorem [A.13](https://arxiv.org/html/2602.09967v1#A1.Thmtheorem13 "Theorem A.13. ‣ A.3. Separation and Duality ‣ Appendix A Mathematical Background ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") that there exists a continuous linear functional ψ\psi on Lp​(Θ;ℝ2)L^{p}(\Theta;\mathbb{R}^{2}) such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | supϕ∈𝒱εψ(ϕ))<infu∈𝒰ψ(u).\underset{\phi\in\mathcal{V}\_{\varepsilon}}{\sup}\,\psi(\phi))<\underset{u\in\mathcal{U}}{\inf}\,\psi(u)\ . |  | (19) |

Furthermore, by Proposition [A.17](https://arxiv.org/html/2602.09967v1#A1.Thmtheorem17 "Proposition A.17. ‣ A.3. Separation and Duality ‣ Appendix A Mathematical Background ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") for this continuous linear functional ψ\psi, there exists a unique δ=(δ1,δ2)∈Lq​(Θ;ℝ2)\delta=(\delta\_{1},\delta\_{2})\in L^{q}(\Theta;\mathbb{R}^{2}) the dual of Lp​(Θ;ℝ2)L^{p}(\Theta;\mathbb{R}^{2}), such that for u∈𝒰u\in\mathcal{U}, and for ϕ∈𝒱ϵ\phi\in\mathcal{V}\_{\epsilon} we have respectively:

|  |  |  |
| --- | --- | --- |
|  | ψ​(u)=∫ΘUθ​(Iθ,pθ)​δ1​(θ)​𝑑μ+Π​∫Θδ2​(θ)​𝑑μ,since Π=∫ΘVϑ​(Iϑ,pϑ)​𝑑μ is a constant,\psi(u)=\int\_{\Theta}U\_{\theta}(I\_{\theta},p\_{\theta})\delta\_{1}(\theta)\,d\mu+\Pi\,\int\_{\Theta}\delta\_{2}(\theta)\,d\mu,\ \text{since $\Pi=\int\_{\Theta}V\_{\vartheta}(I\_{\vartheta},p\_{\vartheta})\,d\mu$ is a constant,} |  |

and,

|  |  |  |
| --- | --- | --- |
|  | ψ​(ϕ)=∫Θϕ1​(θ)​δ1​(θ)​𝑑μ+∫Θϕ2​(θ)​δ2​(θ)​𝑑μ.\psi(\phi)=\int\_{\Theta}\phi\_{1}(\theta)\delta\_{1}(\theta)\,d\mu+\int\_{\Theta}\phi\_{2}(\theta)\delta\_{2}(\theta)\,d\mu\,. |  |

###### Lemma B.2.

Consider the continuous linear functional ψ\psi, and δ=(δ1,δ2)∈Lq​(Θ;ℝ2)\delta=(\delta\_{1},\delta\_{2})\in L^{q}(\Theta;\mathbb{R}^{2}). Then, δ1≤0\delta\_{1}\leq 0 and δ2≤0\delta\_{2}\leq 0, μ\mu-a.s.

###### Proof.

For the sake of contradiction, assume that
μ​{θ;δ1​(θ)>0}>0\mu\{\theta;\delta\_{1}(\theta)>0\}>0 , and consider some h=(h1,0)∈Lp​(Θ,ℝ2)h=(h\_{1},0)\in L^{p}(\Theta,\mathbb{R}^{2}) where h1≥0h\_{1}\geq 0.
Let ϕmin​(θ)=(Uθ​(Iθ∗,pθ∗),Π∗+ε)∈𝒱ε,θ∈Θ\phi\_{\min}(\theta)=\bigg(U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta}),\Pi^{\*}+\varepsilon\bigg)\in\mathcal{V}\_{\varepsilon},\,\,\theta\in\Theta, and for some t>0t>0, we consider ϕt=ϕmin+t​h∈𝒱ε\phi\_{t}=\phi\_{\min}+t\,h\in\mathcal{V}\_{\varepsilon} by Remark [B.1](https://arxiv.org/html/2602.09967v1#A2.Thmtheorem1 "Lemma B.1. ‣ B.1. Proof of Theorem 3.8 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
For each θ∈Θ\theta\in\Theta, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕt​(θ)\displaystyle\phi\_{t}(\theta) | =ϕmin​(θ)+t​h​(θ)=(Uθ​(Iθ∗,pθ∗),Π∗+ε)+t​(h1​(θ),0)=(Uθ​(Iθ∗,pθ∗)+t​h1​(θ),Π∗+ε).\displaystyle=\phi\_{\min}(\theta)+t\,h(\theta)=\bigg(U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta}),\Pi^{\*}+\varepsilon\bigg)+t\,(h\_{1}(\theta),0)=\bigg(U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})+t\,h\_{1}(\theta),\Pi^{\*}+\varepsilon\bigg)\,. |  |

Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ​(ϕt)\displaystyle\psi(\phi\_{t}) | =∫ΘUθ​(Iθ∗,pθ∗)​δ1​(θ)​𝑑μ+∫Θt​h1​(θ)​δ1​(θ)​𝑑μ+(Π∗+ε)​∫Θδ2​(θ)​𝑑μ\displaystyle=\int\_{\Theta}U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\delta\_{1}(\theta)\,d\mu+\int\_{\Theta}t\,h\_{1}(\theta)\delta\_{1}(\theta)\,d\mu+\left(\Pi^{\*}+\varepsilon\right)\int\_{\Theta}\delta\_{2}(\theta)\,d\mu |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ψ​(ϕmin​(θ))+t​∫Θh1​(θ)​δ1​(θ)​𝑑μ.\displaystyle=\psi(\phi\_{\min}(\theta))+t\int\_{\Theta}\,h\_{1}(\theta)\delta\_{1}(\theta)\,d\mu\,. |  |

Letting t→∞t\to\infty, it follows that ψ​(ϕt)→∞\psi(\phi\_{t})\to\infty.
However, from Proposition [A.17](https://arxiv.org/html/2602.09967v1#A1.Thmtheorem17 "Proposition A.17. ‣ A.3. Separation and Duality ‣ Appendix A Mathematical Background ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), we know that |ψ​(ϕt)|<+∞|\psi(\phi\_{t})|<+\infty, which leads to a contradiction. Consequently, δ1≤0\delta\_{1}\leq 0, μ\mu-as.
Similarly, we obtain that δ2≤0\delta\_{2}\leq 0, μ\mu-as.
∎

###### Lemma B.3.

Consider the continuous linear functional ψ\psi, and ϕ\phi, ϕmin∈𝒱ε\phi\_{\min}\in\mathcal{V}\_{\varepsilon}. Then,

|  |  |  |
| --- | --- | --- |
|  | supϕ∈𝒱ε​ψ​(ϕ)=ψ​(ϕmin).\underset{\phi\in\mathcal{V}\_{\varepsilon}}{\sup}\,\psi(\phi)=\psi(\phi\_{\min}). |  |

###### Proof.

We know that any ϕ∈𝒱ε\phi\in\mathcal{V}\_{\varepsilon} can be written as ϕ=ϕmin+h\phi=\phi\_{\min}+h, where h∈ℋ⊂Lp​(Θ,ℝ2)h\in\mathcal{H}\subset L^{p}(\Theta,\mathbb{R}^{2}), by Remark [B.1](https://arxiv.org/html/2602.09967v1#A2.Thmtheorem1 "Lemma B.1. ‣ B.1. Proof of Theorem 3.8 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
Then applying ψ\psi to ϕ=ϕmin+h\phi=\phi\_{\min}+h, we obatin

|  |  |  |
| --- | --- | --- |
|  | ψ​(ϕ)=ψ​(ϕmin)+∫Θh1​(θ)​δ1​(θ)​𝑑μ+∫Θh2​(θ)​δ2​(θ)​𝑑μ,\psi(\phi)=\psi(\phi\_{\min})+\int\_{\Theta}h\_{1}(\theta)\delta\_{1}(\theta)\,d\mu+\int\_{\Theta}h\_{2}(\theta)\delta\_{2}(\theta)\,d\mu\,, |  |

with h1,h2≥0h\_{1},h\_{2}\geq 0, since h∈ℋh\in\mathcal{H} and δ1,δ2≤0\delta\_{1},\delta\_{2}\leq 0 μ\mu-as from Lemma [B.2](https://arxiv.org/html/2602.09967v1#A2.Thmtheorem2 "Lemma B.2. ‣ B.1. Proof of Theorem 3.8 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
Therefore, for any ϕ∈𝒱ε\phi\in\mathcal{V}\_{\varepsilon}, ψ​(ϕ)≤ψ​(ϕmin)\psi(\phi)\leq\psi(\phi\_{\min}), and hence supϕ∈𝒱ε​ψ​(ϕ)=ψ​(ϕmin)\underset{\phi\in\mathcal{V}\_{\varepsilon}}{\sup}\,\psi(\phi)=\psi(\phi\_{\min}).
∎

It follows from the above lemma that the strict inequality ([19](https://arxiv.org/html/2602.09967v1#A2.E19 "Equation 19 ‣ B.1. Proof of Theorem 3.8 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) can be rewritten as:

|  |  |  |
| --- | --- | --- |
|  | ψ​(ϕmin)<infu∈𝒰​ψ​(u)≤ψ​(u).\psi(\phi\_{\min})<\underset{u\in\mathcal{U}}{\inf}\,\psi(u)\,\,\leq\psi(u)\,. |  |

That is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ​(ϕmin)<ψ​(u),for u∈𝒰.\psi(\phi\_{\min})<\psi(u),\ \text{for $u\in\mathcal{U}$}. |  | (20) |

Moreover, since δ1,δ2≤0\delta\_{1},\delta\_{2}\leq 0 (Lemma [B.2](https://arxiv.org/html/2602.09967v1#A2.Thmtheorem2 "Lemma B.2. ‣ B.1. Proof of Theorem 3.8 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")), we introduce the following notation: δ~=−δ≥0\widetilde{\delta}=-\delta\geq 0, μ\mu-as. It then follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ~​(v)\displaystyle\widetilde{\psi}(v) | =∫Θv1​(θ)​δ~1​(θ)​𝑑μ+∫Θv2​(θ)​δ~2​(θ)​𝑑μ=−∫Θv1​(θ)​δ1​(θ)​𝑑μ−∫Θv2​(θ)​δ2​(θ)​𝑑μ=−ψ​(v),\displaystyle=\int\_{\Theta}v\_{1}(\theta)\widetilde{\delta}\_{1}(\theta)\ d\mu+\int\_{\Theta}v\_{2}(\theta)\widetilde{\delta}\_{2}(\theta)\ d\mu=-\int\_{\Theta}v\_{1}(\theta)\delta\_{1}(\theta)\ d\mu-\int\_{\Theta}v\_{2}(\theta)\delta\_{2}(\theta)\ d\mu=-\psi(v), |  |

for any v=(v1,v2)∈Lp​(Θ;ℝ2)v=(v\_{1},v\_{2})\in L^{p}(\Theta;\mathbb{R}^{2}). Then, flipping signs of ([20](https://arxiv.org/html/2602.09967v1#A2.E20 "Equation 20 ‣ B.1. Proof of Theorem 3.8 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")), we obtain: −ψ​(u)<−ψ​(ϕmin)-\psi(u)<-\psi(\phi\_{\min}); or equivalently,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ~​(u)<ψ~​(ϕmin).\widetilde{\psi}(u)<\widetilde{\psi}(\phi\_{\min}). |  | (21) |

We now consider some κ>0\kappa>0, such that (δ~1κ,δ~2)=(δ~1+κ,δ~2)(\widetilde{\delta}^{\kappa}\_{1},\widetilde{\delta}\_{2})=(\widetilde{\delta}\_{1}+\kappa,\widetilde{\delta}\_{2}), where δ~1+κ>0\widetilde{\delta}\_{1}+\kappa>0 and δ~2≥0\widetilde{\delta}\_{2}\geq 0.
Then for any v=(v1,v2)∈Lp​(Θ,ℝ2)v=(v\_{1},v\_{2})\in L^{p}(\Theta,\mathbb{R}^{2}), replacing (δ~1,δ~2)(\widetilde{\delta}\_{1},\widetilde{\delta}\_{2}) with (δ~1κ,δ~2)(\widetilde{\delta}^{\kappa}\_{1},\widetilde{\delta}\_{2}), we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ~κ​(v)\displaystyle\widetilde{\psi}^{\kappa}(v) | =∫Θv1​(θ)⋅(δ~1+κ)​𝑑μ+∫Θv2​(θ)​δ~2​𝑑μ=ψ~​(v)+κ​∫Θv1​(θ)​𝑑μ.\displaystyle=\int\_{\Theta}v\_{1}(\theta)\cdot(\widetilde{\delta}\_{1}+\kappa)\,d\mu+\int\_{\Theta}v\_{2}(\theta)\widetilde{\delta}\_{2}\,d\mu=\widetilde{\psi}(v)+\kappa\int\_{\Theta}v\_{1}(\theta)\,d\mu. |  |

We aim to show that the strict inequality ([21](https://arxiv.org/html/2602.09967v1#A2.E21 "Equation 21 ‣ B.1. Proof of Theorem 3.8 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) still holds for ψ~κ​(⋅)\widetilde{\psi}^{\kappa}(\cdot).
In particular for u∈𝒰u\in\mathcal{U} and ϕmin∈𝒱ε\phi\_{\min}\in\mathcal{V}\_{\varepsilon}, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ~κ​(u)\displaystyle\widetilde{\psi}^{\kappa}(u) | =∫ΘUθ​(Iθ,pθ)​(δ~1​(θ)+κ)​𝑑μ+Π​∫Θδ~2​(θ)​𝑑μ,\displaystyle=\int\_{\Theta}U\_{\theta}(I\_{\theta},p\_{\theta})\left(\widetilde{\delta}\_{1}(\theta)+\kappa\right)d\mu+\Pi\int\_{\Theta}\widetilde{\delta}\_{2}(\theta)d\mu, |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ~κ​(ϕmin)\displaystyle\widetilde{\psi}^{\kappa}(\phi\_{\min}) | =∫ΘUθ​(Iθ∗,pθ∗)​(δ~1​(θ)+κ)​𝑑μ+(Π∗+ε)​∫Θδ~2​(θ)​𝑑μ.\displaystyle=\int\_{\Theta}U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\left(\widetilde{\delta}\_{1}(\theta)+\kappa\right)d\mu+(\Pi^{\*}+\varepsilon)\int\_{\Theta}\widetilde{\delta}\_{2}(\theta)d\mu. |  |

Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ~κ​(ϕmin)−ψ~κ​(u)\displaystyle\widetilde{\psi}^{\kappa}(\phi\_{\min})-\widetilde{\psi}^{\kappa}(u) | =∫Θ[Uθ​(Iθ∗,pθ∗)−Uθ​(Iθ,pθ)]​(δ~1​(θ)+κ)​𝑑μ+(Π∗+ε−Π)​∫Θδ~2​(θ)​𝑑μ.\displaystyle=\int\_{\Theta}\left[U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})-U\_{\theta}(I\_{\theta},p\_{\theta})\right]\left(\widetilde{\delta}\_{1}(\theta)+\kappa\right)d\mu+(\Pi^{\*}+\varepsilon-\Pi)\int\_{\Theta}\widetilde{\delta}\_{2}(\theta)d\mu. |  |

For the sake of contradiction, suppose that ψ~κ​(ϕmin)−ψ~κ​(u)≤0\widetilde{\psi}^{\kappa}(\phi\_{\min})-\widetilde{\psi}^{\kappa}(u)\leq 0.
Since κ>0\kappa>0, δ~1​(θ),δ~2​(θ)≥0\widetilde{\delta}\_{1}(\theta),\widetilde{\delta}\_{2}(\theta)\geq 0, μ\mu-as for θ∈Θ\theta\in\Theta, then we must have

|  |  |  |
| --- | --- | --- |
|  | Uθ​(Iθ∗,pθ∗)≤Uθ​(Iθ,pθ),μ​-a.e.,U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\leq U\_{\theta}(I\_{\theta},p\_{\theta}),\ \,\mu\hbox{-a.e.,} |  |

and Π∗+ε≤Π\Pi^{\*}+\varepsilon\leq\Pi, which implies that Π∗<Π∗+ε≤Π\Pi^{\*}<\Pi^{\*}+\varepsilon\leq\Pi,
contradicting the fact that (Iθ∗,pθ∗)θ∈Θ(I^{\*}\_{\theta},p^{\*}\_{\theta})\_{\theta\in\Theta} is IPO. Hence, ψ~κ​(ϕmin)−ψ~κ​(u)>0\widetilde{\psi}^{\kappa}(\phi\_{\min})-\widetilde{\psi}^{\kappa}(u)>0, as desired. Equivalently,

|  |  |  |
| --- | --- | --- |
|  | ψ~κ​(u)<ψ~κ​(ϕmin).\widetilde{\psi}^{\kappa}(u)<\widetilde{\psi}^{\kappa}(\phi\_{\min}). |  |

This implies that

|  |  |  |
| --- | --- | --- |
|  | ∫ΘUθ​(Iθ,pθ)​(δ~1​(θ)+κ)​𝑑μ+∫ΘVθ​(Iθ,pθ)​𝑑μ​∫Θδ~2​(θ)​𝑑μ\displaystyle\int\_{\Theta}U\_{\theta}(I\_{\theta},p\_{\theta})\left(\widetilde{\delta}\_{1}(\theta)+\kappa\right)\,d\mu+\int\_{\Theta}V\_{\theta}(I\_{\theta},p\_{\theta})\,d\mu\,\int\_{\Theta}\widetilde{\delta}\_{2}(\theta)\,d\mu |  |
|  |  |  |
| --- | --- | --- |
|  | <∫ΘUθ​(Iθ∗,pθ∗)​(δ~1​(θ)+κ)​𝑑μ+(∫ΘVθ​(Iθ∗,pθ∗)​𝑑μ+ε)​∫Θδ~2​(θ)​𝑑μ.\displaystyle\quad<\int\_{\Theta}U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\left(\widetilde{\delta}\_{1}(\theta)+\kappa\right)\,d\mu+\left(\int\_{\Theta}V\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\,d\mu+\varepsilon\right)\int\_{\Theta}\widetilde{\delta}\_{2}(\theta)\,d\mu\,. |  |

Letting β:=∫Θδ~2​(θ)​𝑑μ≥0\beta:=\int\_{\Theta}\widetilde{\delta}\_{2}(\theta)\,d\mu\geq 0, we obtain:

|  |  |  |
| --- | --- | --- |
|  | ∫ΘUθ​(Iθ,pθ)​(δ~1​(θ)+κ)​𝑑μ+β​∫ΘVθ​(Iθ,pθ)​𝑑μ\displaystyle\int\_{\Theta}U\_{\theta}(I\_{\theta},p\_{\theta})\left(\widetilde{\delta}\_{1}(\theta)+\kappa\right)\,d\mu+\beta\int\_{\Theta}V\_{\theta}(I\_{\theta},p\_{\theta})\,d\mu |  |
|  |  |  |
| --- | --- | --- |
|  | <∫ΘUθ​(Iθ∗,pθ∗)​(δ~1​(θ)+κ)​𝑑μ+β⋅(∫ΘVθ​(Iθ∗,pθ∗)​𝑑μ+ε).\displaystyle\quad<\int\_{\Theta}U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\left(\widetilde{\delta}\_{1}(\theta)+\kappa\right)\,d\mu+\beta\cdot\left(\int\_{\Theta}V\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\,d\mu+\varepsilon\right)\,. |  |

Letting C:=∫Θ(δ~1​(θ)+κ)​𝑑μ>0C:=\int\_{\Theta}(\widetilde{\delta}\_{1}(\theta)+\kappa)\ d\mu>0, and defining η\eta such that:

|  |  |  |
| --- | --- | --- |
|  | d​η=(δ~1+κ)C​d​μ,d\eta=\frac{(\widetilde{\delta}\_{1}+\kappa)}{C}d\mu, |  |

yields

|  |  |  |
| --- | --- | --- |
|  | C​∫ΘUθ​(Iθ,pθ)​𝑑η+β​∫ΘVθ​(Iθ,pθ)​𝑑μ<C​∫ΘUθ​(Iθ∗,pθ∗)​𝑑η+β⋅(∫ΘVθ​(Iθ∗,pθ∗)​𝑑μ+ε).\displaystyle C\int\_{\Theta}U\_{\theta}(I\_{\theta},p\_{\theta})\ d\eta+\beta\int\_{\Theta}V\_{\theta}(I\_{\theta},p\_{\theta})\,d\mu<C\int\_{\Theta}U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\ d\eta+\beta\cdot\left(\int\_{\Theta}V\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\,d\mu+\varepsilon\right). |  |

Dividing both sides by C+β>0C+\beta>0 gives

|  |  |  |
| --- | --- | --- |
|  | CC+β​∫ΘUθ​(Iθ,pθ)​𝑑η+βC+β​∫ΘVθ​(Iθ,pθ)​𝑑μ<CC+β​∫ΘUθ​(Iθ∗,pθ∗)​𝑑η+βC+β⋅(∫ΘVθ​(Iθ∗,pθ∗)​𝑑μ+ε).\displaystyle\frac{C}{C+\beta}\int\_{\Theta}U\_{\theta}(I\_{\theta},p\_{\theta})\ d\eta+\frac{\beta}{C+\beta}\int\_{\Theta}V\_{\theta}(I\_{\theta},p\_{\theta})\,d\mu<\frac{C}{C+\beta}\int\_{\Theta}U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\ d\eta+\frac{\beta}{C+\beta}\cdot\left(\int\_{\Theta}V\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\,d\mu+\varepsilon\right). |  |

Let α=CC+β∈(0,1]\alpha=\frac{C}{C+\beta}\in(0,1] since C>0C>0. Then 1−α=1−CC+β=βC+β1-\alpha=1-\frac{C}{C+\beta}=\frac{\beta}{C+\beta}. Hence,

|  |  |  |
| --- | --- | --- |
|  | α​∫ΘUθ​(Iθ,pθ)​𝑑η+(1−α)​∫ΘVθ​(Iθ,pθ)​𝑑μ<α​∫ΘUθ​(Iθ∗,pθ∗)​𝑑η+(1−α)⋅(∫ΘVθ​(Iθ∗,pθ∗)​𝑑μ+ε).\displaystyle\alpha\int\_{\Theta}U\_{\theta}(I\_{\theta},p\_{\theta})\ d\eta+(1-\alpha)\int\_{\Theta}V\_{\theta}(I\_{\theta},p\_{\theta})\,d\mu<\alpha\int\_{\Theta}U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\ d\eta+(1-\alpha)\cdot\left(\int\_{\Theta}V\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\,d\mu+\varepsilon\right). |  |

Letting ε→0\varepsilon\to 0, we obtain the following:

|  |  |  |
| --- | --- | --- |
|  | α​∫ΘUθ​(Iθ,pθ)​𝑑η+(1−α)​∫ΘVθ​(Iθ,pθ)​𝑑μ<α​∫ΘUθ​(Iθ∗,pθ∗)​𝑑η+(1−α)​∫ΘVθ​(Iθ∗,pθ∗)​𝑑μ.\displaystyle\alpha\int\_{\Theta}U\_{\theta}(I\_{\theta},p\_{\theta})\ d\eta+(1-\alpha)\int\_{\Theta}V\_{\theta}(I\_{\theta},p\_{\theta})\ d\mu<\alpha\int\_{\Theta}U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\ d\eta+(1-\alpha)\int\_{\Theta}V\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\ d\mu. |  |

Consequently,

|  |  |  |
| --- | --- | --- |
|  | (Iθ∗,pθ∗)∈arg​sup(Iθ,pθ)∈ℐ​ℛ∩ℐ​𝒞​{α​∫ΘUθ​(Iθ,pθ)​𝑑η+(1−α)​∫ΘVθ​(Iθ,pθ)​𝑑μ}.(I^{\*}\_{\theta},p^{\*}\_{\theta})\in\underset{(I\_{\theta},p\_{\theta})\in\mathcal{I}\mathcal{R}\cap\mathcal{I}\mathcal{C}}{\arg\sup}\left\{\alpha\int\_{\Theta}U\_{\theta}(I\_{\theta},p\_{\theta})\,d\eta+(1-\alpha)\int\_{\Theta}V\_{\theta}(I\_{\theta},p\_{\theta})\,d\mu\right\}. |  |

It remains to verify that η\eta is a probability measure equivalent to μ\mu.
First, η\eta is a probability measure since it is non-negative and satisfies:

|  |  |  |
| --- | --- | --- |
|  | η​(Θ)=∫Θ𝑑η=∫Θ(δ~1​(θ)+κ)C​𝑑μ=1C​∫Θ(δ~1​(θ)+κ)​𝑑μ=CC=1.\eta(\Theta)=\int\_{\Theta}d\eta=\int\_{\Theta}\frac{(\widetilde{\delta}\_{1}(\theta)+\kappa)}{C}d\mu=\frac{1}{C}\int\_{\Theta}(\widetilde{\delta}\_{1}(\theta)+\kappa)\ d\mu=\frac{C}{C}=1. |  |

Moreover, it can be easily seen that η\eta is absolutely continuous with respect to μ\mu, since

|  |  |  |
| --- | --- | --- |
|  | d​η=δ~1+κC​d​μ, where δ~1+κC>0.d\eta=\frac{\widetilde{\delta}\_{1}+\kappa}{C}d\mu,\ \text{ where $\frac{\widetilde{\delta}\_{1}+\kappa}{C}>0$}. |  |

We still have to show that μ\mu is absolutely continuous with respect to η\eta. For any A∈ℬ​(Θ)A\in\mathcal{B}(\Theta), we can write:

|  |  |  |
| --- | --- | --- |
|  | η​(A)=∫Aδ~1​(θ)+κC​𝑑μ=1C​[∫Aδ~1​(θ)​𝑑μ+κ​μ​(A)]≥1C​κ​μ​(A).\eta(A)=\int\_{A}\frac{\widetilde{\delta}\_{1}(\theta)+\kappa}{C}\,d\mu=\frac{1}{C}\left[\int\_{A}\widetilde{\delta}\_{1}(\theta)\,d\mu+\kappa\,\mu(A)\right]\geq\frac{1}{C}\kappa\ \mu(A). |  |

If η​(A)=0\eta(A)=0, we obtain, 1C​κ​μ​(A)≤0\frac{1}{C}\kappa\,\mu(A)\leq 0, where C,κ>0C,\kappa>0. Then μ​(A)=0\mu(A)=0, and hence μ\mu is absolutely continuous with respect to η\eta.

The if direction:
We assume that there exists a probability measure η\eta on (Θ,ℬ​(Θ))(\Theta,\mathcal{B}(\Theta)), such that η\eta is equivalent to μ\mu, and α∈(0,1]\alpha\in(0,1] such that the menu of contracts (Iθ∗,pθ∗)θ∈Θ\left(I^{\*}\_{\theta},p^{\*}\_{\theta}\right)\_{\theta\in\Theta} is optimal for Problem ([1](https://arxiv.org/html/2602.09967v1#S3.E1 "Equation 1 ‣ Theorem 3.8. ‣ 3.2. Social Welfare Maximization ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")).
For the sake of contradiction, we assume that (Iθ∗,pθ∗)θ∈Θ∉ℐ​𝒫​𝒪\left(I^{\*}\_{\theta},p^{\*}\_{\theta}\right)\_{\theta\in\Theta}\notin\mathcal{I}\mathcal{P}\mathcal{O}. By Definition [3.5](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem5 "Definition 3.5. ‣ 3.1. Incentive Pareto Optimality ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") there exists (Iθ,pθ)θ∈Θ∈ℐ​ℛ∩ℐ​𝒞(I\_{\theta},p\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{R}\cap\mathcal{I}\mathcal{C} such that for μ\mu-almost every θ∈Θ\theta\in\Theta,

|  |  |  |
| --- | --- | --- |
|  | Uθ​(Iθ,pθ)≥Uθ​(Iθ∗,pθ∗)and∫ΘVθ​(Iθ,pθ)​𝑑μ≥∫ΘVθ​(Iθ∗,pθ∗)​𝑑μ.U\_{\theta}(I\_{\theta},p\_{\theta})\geq U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\ \ \hbox{and}\ \ \int\_{\Theta}V\_{\theta}(I\_{\theta},p\_{\theta})\,\,d\mu\geq\int\_{\Theta}V\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\,\,d\mu. |  |

In addition, at least one of the following two conditions holds:

|  |  |  |
| --- | --- | --- |
|  | ∫ΘVθ​(Iθ,pθ)​𝑑μ>∫ΘVθ​(Iθ∗,pθ∗)​𝑑μorμ​({θ∈Θ;Uθ​(Iθ,pθ)>Uθ​(Iθ∗,pθ∗)})>0.\int\_{\Theta}V\_{\theta}(I\_{\theta},p\_{\theta})\,\,d\mu>\int\_{\Theta}V\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\,\,d\mu\ \ \hbox{or}\ \ \mu\left(\left\{\theta\in\Theta\,;\,\,U\_{\theta}(I\_{\theta},p\_{\theta})>U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\,\right\}\right)>0. |  |

We consider the following two cases:

1. (1)

   Suppose that ∫ΘVθ​(Iθ,pθ)​𝑑μ>∫ΘVθ​(Iθ∗,pθ∗)​𝑑μ\int\_{\Theta}V\_{\theta}(I\_{\theta},p\_{\theta})d\mu>\int\_{\Theta}V\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})d\mu.
   Since μ\mu is equivalent to η\eta, and

   |  |  |  |
   | --- | --- | --- |
   |  | Uθ​(Iθ,pθ)≥Uθ​(Iθ∗,pθ∗), μ-a.e.,U\_{\theta}(I\_{\theta},p\_{\theta})\geq U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta}),\ \text{ $\mu$-a.e.,} |  |

   this inequality also holds η\eta-a.e. Moreover,

   |  |  |  |
   | --- | --- | --- |
   |  | α​∫ΘUθ​(Iθ,pθ)​𝑑η+(1−α)​∫ΘVθ​(Iθ,pθ)​𝑑μ>α​∫ΘUθ​(Iθ∗,pθ∗)​𝑑η+(1−α)​∫ΘVθ​(Iθ∗,pθ∗)​𝑑μ,\alpha\int\_{\Theta}U\_{\theta}(I\_{\theta},p\_{\theta})\,\,d\eta+(1-\alpha)\int\_{\Theta}V\_{\theta}(I\_{\theta},p\_{\theta})\,\,d\mu>\alpha\int\_{\Theta}U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\,\,d\eta+(1-\alpha)\int\_{\Theta}V\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\,\,d\mu, |  |

   contradicting the optimality of (Iθ∗,pθ∗)θ∈Θ(I^{\*}\_{\theta},p^{\*}\_{\theta})\_{\theta\in\Theta} for Problem ([1](https://arxiv.org/html/2602.09967v1#S3.E1 "Equation 1 ‣ Theorem 3.8. ‣ 3.2. Social Welfare Maximization ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")). Hence, (Iθ∗,pθ∗)θ∈Θ∈ℐ​𝒫​𝒪(I^{\*}\_{\theta},p^{\*}\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{P}\mathcal{O}.
2. (2)

   Suppose now that ∫ΘVθ​(Iθ,pθ)​𝑑μ=∫ΘVθ​(Iθ∗,pθ∗)​𝑑μ\int\_{\Theta}V\_{\theta}(I\_{\theta},p\_{\theta})d\mu=\int\_{\Theta}V\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})d\mu,
   and hence

   |  |  |  |
   | --- | --- | --- |
   |  | μ​({θ∈Θ;Uθ​(Iθ,pθ)>Uθ​(Iθ∗,pθ∗)})>0.\mu\left(\left\{\theta\in\Theta\,;\,\,U\_{\theta}(I\_{\theta},p\_{\theta})>U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\,\right\}\right)>0. |  |

   It follows that,

   |  |  |  |
   | --- | --- | --- |
   |  | η​({θ∈Θ;Uθ​(Iθ,pθ)>Uθ​(Iθ∗,pθ∗)})>0.\eta\left(\left\{\theta\in\Theta\,;\,\,U\_{\theta}(I\_{\theta},p\_{\theta})>U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\,\right\}\right)>0. |  |

   Therefore,

   |  |  |  |
   | --- | --- | --- |
   |  | α​∫ΘUθ​(Iθ,pθ)​𝑑η+(1−α)​∫ΘVθ​(Iθ,pθ)​𝑑μ>α​∫ΘUθ​(Iθ∗,pθ∗)​𝑑η+(1−α)​∫ΘVθ​(Iθ∗,pθ∗)​𝑑μ,\alpha\int\_{\Theta}U\_{\theta}(I\_{\theta},p\_{\theta})\,\,d\eta+(1-\alpha)\int\_{\Theta}V\_{\theta}(I\_{\theta},p\_{\theta})\,\,d\mu>\alpha\int\_{\Theta}U\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\,\,d\eta+(1-\alpha)\int\_{\Theta}V\_{\theta}(I^{\*}\_{\theta},p^{\*}\_{\theta})\,\,d\mu, |  |

   contradicting the optimality of (Iθ∗,pθ∗)θ∈Θ(I^{\*}\_{\theta},p^{\*}\_{\theta})\_{\theta\in\Theta} for Problem ([1](https://arxiv.org/html/2602.09967v1#S3.E1 "Equation 1 ‣ Theorem 3.8. ‣ 3.2. Social Welfare Maximization ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")). Hence, (Iθ∗,pθ∗)θ∈Θ∈ℐ​𝒫​𝒪(I^{\*}\_{\theta},p^{\*}\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{P}\mathcal{O}. ∎

### B.2. Proof of Proposition [4.5](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem5 "Proposition 4.5. ‣ 4.1. Dual Utility Framework ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")

Let (Rθ,pθ)θ∈Θ∈ℐ​ℛ(R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{R}. Then it follows from Definition [3.3](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem3 "Definition 3.3. ‣ 3.1. Incentive Pareto Optimality ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") that

|  |  |  |
| --- | --- | --- |
|  | Uθ​(Rθ,pθ)≥Uθ​(Lθ,0),∀θ∈Θ,and∫ΘVθ​(Rθ,pθ)​𝑑μ≥0.U\_{\theta}(R\_{\theta},p\_{\theta})\geq U\_{\theta}(L\_{\theta},0),\,\,\,\forall\,\theta\in\Theta,\ \ \hbox{and}\ \ \int\_{\Theta}V\_{\theta}(R\_{\theta},p\_{\theta})\,d\mu\geq 0. |  |

Moreover,

|  |  |  |
| --- | --- | --- |
|  | Uθ​(Rθ,pθ)=−pθ−∫0L¯[1−gθ​(Fθ​(l))]​∂Rθ​(l)∂l​𝑑l,U\_{\theta}(R\_{\theta},p\_{\theta})=-p\_{\theta}-\int\_{0}^{\bar{L}}\left[1-g\_{\theta}\big(F\_{\theta}(l)\big)\right]\,\,\frac{\partial R\_{\theta}(l)}{\partial l}\,dl, |  |

and

|  |  |  |
| --- | --- | --- |
|  | Uθ​(Lθ,0)=−∫0L¯(1−gθ​(Fθ​(l)))​𝑑l.U\_{\theta}(L\_{\theta},0)=-\int\_{0}^{\bar{L}}\left(1-g\_{\theta}\left(F\_{\theta}(l)\right)\right)\,dl. |  |

Using (P1), we obtain:

|  |  |  |
| --- | --- | --- |
|  | −pθ−∫0L¯[1−gθ​(Fθ​(l))]​∂Rθ​(l)∂l​𝑑l≥−∫0L¯[1−gθ​(Fθ​(l))]​𝑑l.-p\_{\theta}-\int\_{0}^{\bar{L}}\left[1-g\_{\theta}\big(F\_{\theta}(l)\big)\right]\,\,\frac{\partial R\_{\theta}(l)}{\partial l}\,\,dl\geq-\int\_{0}^{\bar{L}}\left[1-g\_{\theta}\left(F\_{\theta}(l)\right)\right]\,\,dl. |  |

Hence,

|  |  |  |
| --- | --- | --- |
|  | pθ≤∫0L¯[1−gθ​(Fθ​(l))]​[1−∂Rθ​(l)∂l]​𝑑l.p\_{\theta}\leq\int\_{0}^{\bar{L}}\left[1-g\_{\theta}\big(F\_{\theta}(l)\big)\right]\,\,\left[1-\frac{\partial R\_{\theta}(l)}{\partial l}\right]\,\,dl. |  |

Conversely, consider a menu (Rθ,pθ)θ∈Θ(R\_{\theta},p\_{\theta})\_{\theta\in\Theta} that satisfies ∫ΘVθ​(Rθ,pθ)​𝑑μ≥0\displaystyle\int\_{\Theta}V\_{\theta}(R\_{\theta},p\_{\theta})d\mu\geq 0 and

|  |  |  |
| --- | --- | --- |
|  | pθ≤∫0L¯[1−gθ​(Fθ​(l))]​[1−∂Rθ​(l)∂l]​𝑑l.p\_{\theta}\leq\int\_{0}^{\bar{L}}\left[1-g\_{\theta}\big(F\_{\theta}(l)\big)\right]\,\,\left[1-\frac{\partial R\_{\theta}(l)}{\partial l}\right]\,\,dl. |  |

The above inequality can be rewritten as:

|  |  |  |
| --- | --- | --- |
|  | pθ≤∫0L¯[1−gθ​(Fθ​(l))]​𝑑l−∫0L¯[1−gθ​(Fθ​(l))]​∂Rθ​(l)∂l​𝑑l,p\_{\theta}\leq\int\_{0}^{\bar{L}}\left[1-g\_{\theta}\big(F\_{\theta}(l)\big)\right]\,\,dl-\int\_{0}^{\bar{L}}\left[1-g\_{\theta}\big(F\_{\theta}(l)\big)\right]\,\,\frac{\partial R\_{\theta}(l)}{\partial l}\,\,dl, |  |

or equivalently,

|  |  |  |
| --- | --- | --- |
|  | pθ+∫0L¯[1−gθ​(Fθ​(l))]​∂Rθ​(l)∂l​𝑑l≤∫0L¯[1−gθ​(Fθ​(l))]​𝑑l,p\_{\theta}+\int\_{0}^{\bar{L}}\left[1-g\_{\theta}\big(F\_{\theta}(l)\big)\right]\,\,\frac{\partial R\_{\theta}(l)}{\partial l}\,\,dl\leq\int\_{0}^{\bar{L}}\left[1-g\_{\theta}\big(F\_{\theta}(l)\big)\right]\,\,dl, |  |

which implies that

|  |  |  |
| --- | --- | --- |
|  | Uθ​(Rθ,pθ)≥Uθ​(Lθ,0),∀θ∈Θ.U\_{\theta}(R\_{\theta},p\_{\theta})\geq U\_{\theta}(L\_{\theta},0),\,\,\,\,\forall\theta\in\Theta. |  |

Consequently, (Rθ,pθ)θ∈Θ∈ℐ​ℛ(R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{R} since it satisfies (P1) and (P2) of Definition [3.3](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem3 "Definition 3.3. ‣ 3.1. Incentive Pareto Optimality ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"). ∎

### B.3. Proof of Lemma [4.6](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem6 "Lemma 4.6. ‣ 4.1. Dual Utility Framework ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")

Consider a menu (Rθ,pθ)θ∈Θ∈ℐ​ℛ∩ℐ​𝒞(R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{R}\cap\mathcal{I}\mathcal{C}. We aim to show that the map

|  |  |  |  |
| --- | --- | --- | --- |
|  | u:Θ\displaystyle u:\Theta | →ℝ2\displaystyle\to\mathbb{R}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | θ\displaystyle\theta | ↦u​(θ):=(Uθ​(Iθ,pθ),∫ΘVϑ​(Iϑ,pϑ)​𝑑μ)\displaystyle\mapsto u(\theta):=\Big(U\_{\theta}(I\_{\theta},p\_{\theta}),\int\_{\Theta}V\_{\vartheta}(I\_{\vartheta},p\_{\vartheta})\,d\mu\Big) |  |

belongs to the Bochner space Lp​(Θ;ℝ2)L^{p}(\Theta;\mathbb{R}^{2}), for p∈(1,+∞)p\in(1,+\infty), and that it satisfies

|  |  |  |
| --- | --- | --- |
|  | sup‖u‖Lp≤M,for some constant M<+∞.\sup\|u\|\_{L^{p}}\leq M,\ \text{for some constant $M<+\infty$.} |  |

First, the map uu is ℝ2\mathbb{R}^{2}-valued and strongly measurable. Hence, to show that u∈Lp​(Θ;ℝ2)u\in L^{p}(\Theta;\mathbb{R}^{2}), it suffices to verify that

|  |  |  |
| --- | --- | --- |
|  | ∫Θ‖u​(θ)‖ℝ2p​𝑑μ<+∞,\int\_{\Theta}\|u(\theta)\|\_{\mathbb{R}^{2}}^{p}d\mu<+\infty, |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖u​(θ)‖ℝ2\displaystyle\|u(\theta)\|\_{\mathbb{R}^{2}} | =Uθ​(Rθ,pθ)2+(∫ΘVϑ​(Rϑ,pϑ)​𝑑μ)2≤|Uθ​(Rθ,pθ)|+|Π|,\displaystyle=\sqrt{U\_{\theta}(R\_{\theta},p\_{\theta})^{2}+\left(\int\_{\Theta}V\_{\vartheta}(R\_{\vartheta},p\_{\vartheta})\,d\mu\right)^{2}}\leq|U\_{\theta}(R\_{\theta},p\_{\theta})|+|\Pi|, |  |

and |Π|=|∫ΘVϑ​(Iϑ,pϑ)​𝑑μ||\Pi|=\left|\int\_{\Theta}V\_{\vartheta}(I\_{\vartheta},p\_{\vartheta})\,d\mu\right|. For some p∈(1,+∞)p\in(1,+\infty), we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ‖u​(θ)‖ℝ2p\displaystyle\|u(\theta)\|\_{\mathbb{R}^{2}}^{p} | =(Uθ​(Rθ,pθ)2+(∫ΘVϑ​(Rϑ,pϑ)​𝑑μ)2)p2≤(|Uθ​(Rθ,pθ)|+|Π|)p≤2p−1​(|Uθ​(Rθ,pθ)|p+|Π|p).\displaystyle=\left(U\_{\theta}(R\_{\theta},p\_{\theta})^{2}+\left(\int\_{\Theta}V\_{\vartheta}(R\_{\vartheta},p\_{\vartheta})\,d\mu\right)^{2}\right)^{\frac{p}{2}}\leq(|U\_{\theta}(R\_{\theta},p\_{\theta})|+|\Pi|)^{p}\leq 2^{p-1}(|U\_{\theta}(R\_{\theta},p\_{\theta})|^{p}+|\Pi|^{p}). |  | (22) |

It follows from Proposition [4.5](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem5 "Proposition 4.5. ‣ 4.1. Dual Utility Framework ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), that

|  |  |  |
| --- | --- | --- |
|  | |pθ|≤|∫0L¯[1−gθ​(Fθ​(l))]​[1−∂Rθ​(l)∂l]​𝑑l|≤∫0L¯|[1−gθ​(Fθ​(l))]​[1−∂Rθ​(l)∂l]|​𝑑l≤L¯.|p\_{\theta}|\leq\left|\int\_{0}^{\bar{L}}\left[1-g\_{\theta}(F\_{\theta}(l))\right]\left[1-\frac{\partial R\_{\theta}(l)}{\partial l}\right]\,\,dl\right|\leq\int\_{0}^{\bar{L}}\left|\left[1-g\_{\theta}(F\_{\theta}(l))\right]\left[1-\frac{\partial R\_{\theta}(l)}{\partial l}\right]\right|\,\,dl\leq\bar{L}. |  |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | |Uθ​(Rθ,pθ)|≤|pθ|+L¯≤2​L¯<+∞,|U\_{\theta}(R\_{\theta},p\_{\theta})|\leq|p\_{\theta}|+\bar{L}\leq 2\bar{L}<+\infty, |  |

and

|  |  |  |
| --- | --- | --- |
|  | |Vθ​(Rθ,pθ)|≤|pθ|+L¯≤2​L¯<+∞.|V\_{\theta}(R\_{\theta},p\_{\theta})|\leq|p\_{\theta}|+\bar{L}\leq 2\bar{L}<+\infty. |  |

Moreover, for p∈(1,+∞)p\in(1,+\infty),

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |Uθ​(Rθ,pθ)|p\displaystyle|U\_{\theta}(R\_{\theta},p\_{\theta})|^{p} | ≤(2​L¯)p,\displaystyle\leq(2\bar{L})^{p}, |  | (23) |

and since μ​(Θ)=1<+∞\mu(\Theta)=1<+\infty, we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |Π|p\displaystyle|\Pi|^{p} | =|∫ΘVθ​(Rθ,pθ)​𝑑μ|p≤(∫Θ|Vθ​(Rθ,pθ)|​𝑑μ)p≤(2​L¯)p.\displaystyle=\left|\int\_{\Theta}V\_{\theta}(R\_{\theta},p\_{\theta})d\mu\right|^{p}\leq\left(\int\_{\Theta}\left|V\_{\theta}(R\_{\theta},p\_{\theta})\right|d\mu\right)^{p}\leq(2\bar{L})^{p}. |  | (24) |

Integrating ([22](https://arxiv.org/html/2602.09967v1#A2.E22 "Equation 22 ‣ B.3. Proof of Lemma 4.6 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) over Θ\Theta, and using inequalities ([23](https://arxiv.org/html/2602.09967v1#A2.E23 "Equation 23 ‣ B.3. Proof of Lemma 4.6 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) and ([24](https://arxiv.org/html/2602.09967v1#A2.E24 "Equation 24 ‣ B.3. Proof of Lemma 4.6 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) yields

|  |  |  |
| --- | --- | --- |
|  | ∫Θ‖u​(θ)‖ℝ2p​𝑑μ≤∫Θ2p−1​(|Uθ​(Rθ,pθ)|p+|Π|p)​𝑑μ=2p−1​(∫Θ|Uθ​(Rθ,pθ)|p​𝑑μ+|Π|p)<+∞.\int\_{\Theta}\|u(\theta)\|\_{\mathbb{R}^{2}}^{p}d\mu\leq\int\_{\Theta}2^{p-1}\left(|U\_{\theta}(R\_{\theta},p\_{\theta})|^{p}+|\Pi|^{p}\right)d\mu=2^{p-1}\left(\int\_{\Theta}|U\_{\theta}(R\_{\theta},p\_{\theta})|^{p}d\mu+|\Pi|^{p}\right)<+\infty. |  |

Hence, the map uu belongs to the Bochner space Lp​(Θ,ℝ2)L^{p}(\Theta,\mathbb{R}^{2}).

For Assumption [3.7](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem7 "Assumption 3.7. ‣ 3.2. Social Welfare Maximization ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") to be satisfied, it remains to verify that sup‖u‖Lp≤M<+∞\sup\|u\|\_{L^{p}}\leq M<+\infty. Note that

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup‖u‖Lpp\displaystyle\sup\|u\|\_{L^{p}}^{p} | =sup∫Θ‖u​(θ)‖ℝ2p​𝑑μ≤sup(Rθ,pθ)θ∈Θ​ 2p−1​(∫Θ|Uθ​(Rθ,pθ)|p​𝑑μ+|Π|p)\displaystyle=\sup\int\_{\Theta}\|u(\theta)\|\_{\mathbb{R}^{2}}^{p}\,d\mu\leq\underset{(R\_{\theta},p\_{\theta})\_{\theta\in\Theta}}{\sup}\,2^{p-1}\left(\int\_{\Theta}|U\_{\theta}(R\_{\theta},p\_{\theta})|^{p}d\mu+|\Pi|^{p}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2p−1​(∫Θsup(Rθ,pθ)θ∈Θ​|Uθ​(Rθ,pθ)|p​𝑑μ+|Π|p),\displaystyle\leq 2^{p-1}\left(\int\_{\Theta}\underset{(R\_{\theta},p\_{\theta})\_{\theta\in\Theta}}{\sup}|U\_{\theta}(R\_{\theta},p\_{\theta})|^{p}d\mu+|\Pi|^{p}\right), |  |

where

|  |  |  |
| --- | --- | --- |
|  | sup(Rθ,pθ)θ∈Θ​|Uθ​(Rθ,pθ)|p≤(2​L¯)p.\underset{(R\_{\theta},p\_{\theta})\_{\theta\in\Theta}}{\sup}|U\_{\theta}(R\_{\theta},p\_{\theta})|^{p}\leq(2\bar{L})^{p}. |  |

Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup‖u‖Lpp\displaystyle\sup\|u\|\_{L^{p}}^{p} | ≤2p−1​((2​L¯)p+|Π|p)=m,\displaystyle\leq 2^{p-1}\left((2\bar{L})^{p}+|\Pi|^{p}\right)=m, |  |

where m<+∞m<+\infty is a constant.
Taking M=m1p<+∞M=m^{\frac{1}{p}}<+\infty, Assumption [3.7](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem7 "Assumption 3.7. ‣ 3.2. Social Welfare Maximization ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") is satisfied. ∎

### B.4. Proof of Proposition [4.10](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem10 "Proposition 4.10. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")

Consider an incentive compatible menu of contracts (Rθ,pθ)θ∈Θ∈ℐ​𝒞(R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{C}. First, we know that for θ∈Θ\theta\in\Theta,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Uθ​(Rθ,pθ)=−pθ−∫0L¯[1−gθ​(Fθ​(l))]​∂Rθ​(l)∂l​𝑑l.U\_{\theta}(R\_{\theta},p\_{\theta})=-p\_{\theta}-\int\_{0}^{\bar{L}}\left[1-g\_{\theta}\big(F\_{\theta}(l)\big)\right]\,\,\frac{\partial R\_{\theta}(l)}{\partial l}\,\,dl. |  | (25) |

We can also express the utility of a type-θ\theta agent using (Rθ′,pθ′)(R\_{\theta^{\prime}},p\_{\theta^{\prime}}), where θ′∈Θ,θ′≠θ\theta^{\prime}\in\Theta,\,\,\theta^{\prime}\neq\theta:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Uθ​(Rθ′,pθ′)\displaystyle U\_{\theta}(R\_{\theta^{\prime}},p\_{\theta^{\prime}}) | =−pθ′−∫0L¯[1−gθ​(Fθ​(l))]​∂Rθ′​(l)∂l​𝑑l.\displaystyle=-p\_{\theta^{\prime}}-\int\_{0}^{\bar{L}}\left[1-g\_{\theta}\big(F\_{\theta}(l)\big)\right]\,\,\frac{\partial R\_{\theta^{\prime}}(l)}{\partial l}\,dl. |  |

Moreover, it follows from Remark [4.9](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem9 "Remark 4.9. ‣ 4.2. Type Ordering under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | |∂Uθ​(Rθ′,pθ′)∂θ|\displaystyle\left|\frac{\partial U\_{\theta}(R\_{\theta^{\prime}},p\_{\theta^{\prime}})}{\partial\theta}\right| | =|∫0L¯[∂gθ∂θ(Fθ(l))+g′θ(Fθ(l))∂Fθ∂θ(l)]∂Rθ′​(l)∂ldl|.\displaystyle=\left|\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{\theta}}{\partial\theta}(F\_{\theta}(l))+g\prime\_{\theta}(F\_{\theta}(l))\frac{\partial F\_{\theta}}{\partial\theta}(l)\right]\,\frac{\partial R\_{\theta^{\prime}}(l)}{\partial l}\,\,dl\right|. |  |

Since Rθ′∈ℛR\_{\theta^{\prime}}\in\mathcal{R}, and by Assumption [4.7](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem7 "Assumption 4.7. ‣ 4.2. Type Ordering under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") and Assumption [4.8](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem8 "Assumption 4.8. ‣ 4.2. Type Ordering under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), we obtain

|  |  |  |
| --- | --- | --- |
|  | |∂Uθ​(Rθ′,pθ′)∂θ|≤∫0L¯|[∂gθ∂θ(Fθ(l))+g′θ(Fθ(l))∂Fθ∂θ(l)]∂Rθ′​(l)∂l|dl≤(c+c′δ)L¯<+∞.\left|\frac{\partial U\_{\theta}(R\_{\theta^{\prime}},p\_{\theta^{\prime}})}{\partial\theta}\right|\leq\int\_{0}^{\bar{L}}\left|\left[\frac{\partial g\_{\theta}}{\partial\theta}(F\_{\theta}(l))+g\prime\_{\theta}(F\_{\theta}(l))\frac{\partial F\_{\theta}}{\partial\theta}(l)\,\,\right]\frac{\partial R\_{\theta^{\prime}}(l)}{\partial l}\ \right|dl\leq(c+c^{\prime}\delta)\bar{L}<+\infty. |  |

Hence, Uθ​(Rθ′,pθ′)U\_{\theta}(R\_{\theta^{\prime}},p\_{\theta^{\prime}}) is Lipschitz continuous in θ\theta.
By the envelope theorem (e.g., Milgrom and Segal ([2002](https://arxiv.org/html/2602.09967v1#bib.bib56 "Envelope theorems for arbitrary choice sets"))), for any θ∈Θ\theta\in\Theta, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Uθ​(Rθ,pθ)=Uθ¯​(Rθ¯,pθ¯)+∫θ¯θ∂Us′​(Rs,ps)∂s′|s′=s​d​s=−pθ¯−∫0L¯[1−gθ¯​(Fθ¯​(l))]​∂Rθ¯​(l)∂l​𝑑l+∫θ¯θ∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​∂Rs​(l)∂l​𝑑l​𝑑s.\begin{split}U\_{\theta}(R\_{\theta},p\_{\theta})&=U\_{\underline{\theta}}(R\_{\underline{\theta}},p\_{\underline{\theta}})+\int\_{\underline{\theta}}^{\theta}\frac{\partial U\_{s^{\prime}}(R\_{s},p\_{s})}{\partial s^{\prime}}\bigg|\_{s^{\prime}=s}\,\,ds\\ &=-p\_{\underline{\theta}}-\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\right]\,\,\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}\,\,dl+\int\_{\underline{\theta}}^{\theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\frac{\partial R\_{s}(l)}{\partial l}\,dl\,ds.\end{split} |  | (26) |

Equating ([25](https://arxiv.org/html/2602.09967v1#A2.E25 "Equation 25 ‣ B.4. Proof of Proposition 4.10 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) and ([26](https://arxiv.org/html/2602.09967v1#A2.E26 "Equation 26 ‣ B.4. Proof of Proposition 4.10 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | pθ=pθ¯\displaystyle p\_{\theta}=p\_{\underline{\theta}}\,\, | +∫0L¯[1−gθ¯​(Fθ¯​(l))]​∂Rθ¯​(l)∂l​𝑑l−∫θ¯θ∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​∂Rs​(l)∂l​𝑑l​𝑑s\displaystyle+\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\right]\,\,\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}\,\,dl-\int\_{\underline{\theta}}^{\theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\frac{\partial R\_{s}(l)}{\partial l}\,dl\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫0L¯[1−gθ​(Fθ​(l))]​∂Rθ​(l)∂l​𝑑l.\displaystyle\quad-\int\_{0}^{\bar{L}}\left[1-g\_{\theta}\big(F\_{\theta}(l)\big)\right]\,\,\frac{\partial R\_{\theta}(l)}{\partial l}\,\,dl. |  |

∎

### B.5. Proof of Proposition [4.12](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem12 "Proposition 4.12. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")

We start by assuming that {Rθ}θ∈Θ\{R\_{\theta}\}\_{\theta\in\Theta} is submodular and {pθ}θ∈Θ\{p\_{\theta}\}\_{\theta\in\Theta} satisfies ([4.10](https://arxiv.org/html/2602.09967v1#S4.Ex41 "Proposition 4.10. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")). That is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | pθ=pθ¯\displaystyle p\_{\theta}=p\_{\underline{\theta}}\,\, | +∫0L¯[1−gθ¯​(Fθ¯​(l))]​∂Rθ¯​(l)∂l​𝑑l−∫θ¯θ∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​∂Rs​(l)∂l​𝑑l​𝑑s\displaystyle+\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\right]\,\,\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}\,\,dl-\int\_{\underline{\theta}}^{\theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\frac{\partial R\_{s}(l)}{\partial l}\,dl\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫0L¯[1−gθ​(Fθ​(l))]​∂Rθ​(l)∂l​𝑑l.\displaystyle-\int\_{0}^{\bar{L}}\left[1-g\_{\theta}\big(F\_{\theta}(l)\big)\right]\,\,\frac{\partial R\_{\theta}(l)}{\partial l}\,\,dl. |  |

We show that the menu (Rθ,pθ)θ∈Θ(R\_{\theta},p\_{\theta})\_{\theta\in\Theta} is incentive compatible. To do so, we aim to show that for θ,θ′∈Θ\theta,\theta^{\prime}\in\Theta, and θ′≠θ\theta^{\prime}\neq\theta, the following holds:

|  |  |  |
| --- | --- | --- |
|  | Uθ​(Rθ,pθ)≥Uθ​(Rθ′,pθ′).U\_{\theta}(R\_{\theta},p\_{\theta})\geq U\_{\theta}(R\_{\theta^{\prime}},p\_{\theta^{\prime}}). |  |

We first consider θ,θ′∈Θ\theta,\theta^{\prime}\in\Theta such that, θ<θ′\theta<\theta^{\prime}. We have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Uθ​(Rθ′,pθ′)\displaystyle U\_{\theta}(R\_{\theta^{\prime}},p\_{\theta^{\prime}}) | =−pθ′−∫0L¯[1−gθ​(Fθ​(l))]​∂Rθ′​(l)∂l​𝑑l.\displaystyle=-p\_{\theta^{\prime}}-\int\_{0}^{\bar{L}}\left[1-g\_{\theta}\big(F\_{\theta}(l)\big)\right]\,\,\frac{\partial R\_{\theta^{\prime}}(l)}{\partial l}\,\,dl. |  |

Substituting pθ′p\_{\theta^{\prime}} by the corresponding expression given by ([4.10](https://arxiv.org/html/2602.09967v1#S4.Ex41 "Proposition 4.10. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) for θ′∈Θ\theta^{\prime}\in\Theta, we obtain the following:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Uθ​(Rθ′,pθ′)\displaystyle U\_{\theta}(R\_{\theta^{\prime}},p\_{\theta^{\prime}}) | =−pθ¯−∫0L¯[1−gθ¯​(Fθ¯​(l))]​∂Rθ¯​(l)∂l​𝑑l+∫θ¯θ′∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​∂Rs​(l)∂l​𝑑l​𝑑s\displaystyle=-p\_{\underline{\theta}}-\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\right]\,\,\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}\,\,dl+\int\_{\underline{\theta}}^{\theta^{\prime}}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\frac{\partial R\_{s}(l)}{\partial l}\,dl\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0L¯[gθ​(Fθ​(l))−gθ′​(Fθ′​(l))]​∂Rθ′​(l)∂l​𝑑l.\displaystyle\quad+\int\_{0}^{\bar{L}}\left[g\_{\theta}\big(F\_{\theta}(l)\big)-g\_{\theta^{\prime}}\big(F\_{\theta^{\prime}}(l)\big)\right]\frac{\partial R\_{\theta^{\prime}}(l)}{\partial l}\,dl. |  |

Since θ¯≤θ<θ′\underline{\theta}\leq\theta<\theta^{\prime}, the third term can be written as

|  |  |  |
| --- | --- | --- |
|  | ∫θ¯θ∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​∂Rs​(l)∂l​𝑑l​𝑑s+∫θθ′∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​∂Rs​(l)∂l​𝑑l​𝑑s.\int\_{\underline{\theta}}^{\theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\frac{\partial R\_{s}(l)}{\partial l}\,dl\,ds+\int\_{\theta}^{\theta^{\prime}}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\frac{\partial R\_{s}(l)}{\partial l}\,dl\,ds. |  |

Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Uθ​(Rθ′,pθ′)\displaystyle U\_{\theta}(R\_{\theta^{\prime}},p\_{\theta^{\prime}}) | =Uθ​(Rθ,pθ)+∫θθ′∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​∂Rs​(l)∂l​𝑑l​𝑑s\displaystyle=U\_{\theta}(R\_{\theta},p\_{\theta})+\int\_{\theta}^{\theta^{\prime}}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\frac{\partial R\_{s}(l)}{\partial l}\,dl\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0L¯[gθ​(Fθ​(l))−gθ′​(Fθ′​(l))]​∂Rθ′​(l)∂l​𝑑l.\displaystyle\qquad+\int\_{0}^{\bar{L}}\left[g\_{\theta}\big(F\_{\theta}(l)\big)-g\_{\theta^{\prime}}\big(F\_{\theta^{\prime}}(l)\big)\right]\frac{\partial R\_{\theta^{\prime}}(l)}{\partial l}\,dl. |  |

That is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Uθ​(Rθ′,pθ′)\displaystyle U\_{\theta}(R\_{\theta^{\prime}},p\_{\theta^{\prime}}) | =Uθ​(Rθ,pθ)+∫θθ′∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​∂Rs​(l)∂l​𝑑l​𝑑s\displaystyle=U\_{\theta}(R\_{\theta},p\_{\theta})+\int\_{\theta}^{\theta^{\prime}}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\frac{\partial R\_{s}(l)}{\partial l}\,dl\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0L¯∫θθ′−∂∂s​(gs∘Fs)​(l)​d​s​∂Rθ′​(l)∂l​d​l\displaystyle\qquad+\int\_{0}^{\bar{L}}\int\_{\theta}^{\theta^{\prime}}-\frac{\partial}{\partial s}\big(g\_{s}\circ F\_{s}\big)(l)ds\,\,\frac{\partial R\_{\theta^{\prime}}(l)}{\partial l}\,dl |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Uθ​(Rθ,pθ)+∫θθ′∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​∂Rs​(l)∂l​𝑑l​𝑑s\displaystyle=U\_{\theta}(R\_{\theta},p\_{\theta})+\int\_{\theta}^{\theta^{\prime}}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\frac{\partial R\_{s}(l)}{\partial l}\,dl\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫θθ′∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​∂Rθ′​(l)∂l​𝑑l​𝑑s\displaystyle\qquad-\int\_{\theta}^{\theta^{\prime}}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\frac{\partial R\_{\theta^{\prime}}(l)}{\partial l}\,dl\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Uθ​(Rθ,pθ)+∫θθ′∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​[∂Rs​(l)∂l−∂Rθ′​(l)∂l]​𝑑l​𝑑s\displaystyle=U\_{\theta}(R\_{\theta},p\_{\theta})+\int\_{\theta}^{\theta^{\prime}}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\left[\frac{\partial R\_{s}(l)}{\partial l}-\frac{\partial R\_{\theta^{\prime}}(l)}{\partial l}\right]\,dl\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤Uθ​(Rθ,pθ).\displaystyle\leq U\_{\theta}(R\_{\theta},p\_{\theta}). |  |

The above inequality holds for the following two reasons. First, because {Rθ}θ∈Θ\{R\_{\theta}\}\_{\theta\in\Theta} is submodular, it follows that for θ<θ′\theta<\theta^{\prime}, we have ∂Rθ​(l)∂l\frac{\partial R\_{\theta}(l)}{\partial l} is non-increasing in θ\theta. Hence, for any s∈[θ,θ′]s\in[\theta,\theta^{\prime}]:

|  |  |  |
| --- | --- | --- |
|  | ∂Rs​(l)∂l−∂Rθ′​(l)∂l≥0.\frac{\partial R\_{s}(l)}{\partial l}-\frac{\partial R\_{\theta^{\prime}}(l)}{\partial l}\geq 0. |  |

Second, we know from Subsection [4.2](https://arxiv.org/html/2602.09967v1#S4.SS2 "4.2. Type Ordering under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") that ∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s≤0\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\leq 0.
Therefore,

|  |  |  |
| --- | --- | --- |
|  | [∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]⋅[∂Rs​(l)∂l−∂Rθ′​(l)∂l]≤0.\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\cdot\left[\frac{\partial R\_{s}(l)}{\partial l}-\frac{\partial R\_{\theta^{\prime}}(l)}{\partial l}\right]\leq 0. |  |

We can similarly prove that for θ<θ′\theta<\theta^{\prime}, Uθ′​(Rθ,pθ)≤Uθ′​(Rθ′,pθ′)U\_{\theta^{\prime}}(R\_{\theta},p\_{\theta})\leq U\_{\theta^{\prime}}(R\_{\theta^{\prime}},p\_{\theta^{\prime}}). Therefore, we conclude that (Rθ,pθ)θ∈Θ∈ℐ​𝒞(R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{C}. The converse follows immediately from Proposition [4.10](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem10 "Proposition 4.10. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"). ∎

### B.6. Proof of Proposition [4.13](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem13 "Proposition 4.13. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")

Let (Rθ,pθ)θ∈Θ∈ℐ​𝒞(R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{C} be such that ∫ΘVθ​(Rθ,pθ)​𝑑μ≥0\int\_{\Theta}V\_{\theta}(R\_{\theta},p\_{\theta})d\mu\geq 0. Assume that for the lowest type θ¯\underline{\theta}, the contract (Rθ¯,pθ¯)(R\_{\underline{\theta}},p\_{\underline{\theta}}) satisfies the agent’s participation (P1) of Definition [3.3](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem3 "Definition 3.3. ‣ 3.1. Incentive Pareto Optimality ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"). We show that (Rθ,pθ)θ∈Θ∈ℐ​ℛ(R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{R}.
Since (P2) of Definition [3.3](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem3 "Definition 3.3. ‣ 3.1. Incentive Pareto Optimality ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") is satisfied, it remains to show that

|  |  |  |
| --- | --- | --- |
|  | Uθ​(Rθ,pθ)≥Uθ​(Lθ,0),∀θ∈Θ.U\_{\theta}(R\_{\theta},p\_{\theta})\geq U\_{\theta}(L\_{\theta},0),\ \forall\theta\in\Theta. |  |

We have seen by the envelope theorem that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Uθ​(Rθ,pθ)\displaystyle U\_{\theta}(R\_{\theta},p\_{\theta}) | =Uθ¯​(Rθ¯,pθ¯)+∫θ¯θ∂Us′​(Rs,ps)∂s′|s′=s​d​s\displaystyle=U\_{\underline{\theta}}(R\_{\underline{\theta}},p\_{\underline{\theta}})+\int\_{\underline{\theta}}^{\theta}\frac{\partial U\_{s^{\prime}}(R\_{s},p\_{s})}{\partial s^{\prime}}\bigg|\_{s^{\prime}=s}\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥Uθ¯​(Lθ¯,0)+∫θ¯θ∂Us′​(Rs,ps)∂s′|s′=s​d​s\displaystyle\geq U\_{\underline{\theta}}(L\_{\underline{\theta}},0)+\int\_{\underline{\theta}}^{\theta}\frac{\partial U\_{s^{\prime}}(R\_{s},p\_{s})}{\partial s^{\prime}}\bigg|\_{s^{\prime}=s}\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Uθ¯​(Lθ¯,0)+∫θ¯θ∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​∂Rs​(l)∂l​𝑑l​𝑑s.\displaystyle=U\_{\underline{\theta}}(L\_{\underline{\theta}},0)+\int\_{\underline{\theta}}^{\theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\frac{\partial R\_{s}(l)}{\partial l}\,dl\,ds. |  |

Since ∂gs∂s(Fs(l))+g′s(Fs(l))∂Fs∂s(l)≤0\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g\prime\_{s}(F\_{s}(l))\frac{\partial F\_{s}}{\partial s}(l)\leq 0, and for any Rs∈ℛR\_{s}\in\mathcal{R}, 0≤∂Rs​(l)∂l≤10\leq\frac{\partial R\_{s}(l)}{\partial l}\leq 1, we have:

|  |  |  |
| --- | --- | --- |
|  | [∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​∂Rs​(l)∂l≥∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s.\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\frac{\partial R\_{s}(l)}{\partial l}\geq\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}. |  |

Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Uθ​(Rθ,pθ)\displaystyle U\_{\theta}(R\_{\theta},p\_{\theta}) | ≥Uθ¯​(Lθ¯,0)+∫θ¯θ∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​𝑑l​𝑑s\displaystyle\geq U\_{\underline{\theta}}(L\_{\underline{\theta}},0)+\int\_{\underline{\theta}}^{\theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]dl\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Uθ¯​(Lθ¯,0)+∫θ¯θ∂Us′​(Ls,0)∂s′|s′=s​d​s=Uθ​(Lθ,0).\displaystyle=U\_{\underline{\theta}}(L\_{\underline{\theta}},0)+\int\_{\underline{\theta}}^{\theta}\frac{\partial U\_{s^{\prime}}(L\_{s},0)}{\partial s^{\prime}}\bigg|\_{s^{\prime}=s}ds=U\_{\theta}(L\_{\theta},0). |  |

This implies that (Rθ,pθ)θ∈Θ∈ℐ​ℛ(R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{R}. Conversely, if (Rθ,pθ)θ∈Θ∈ℐ​ℛ(R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{R} then it is trivial that (Rθ¯,pθ¯)(R\_{\underline{\theta}},p\_{\underline{\theta}}) satisfies the agent’s participation (P1) of Definition [3.3](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem3 "Definition 3.3. ‣ 3.1. Incentive Pareto Optimality ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"). ∎

### B.7. Proof of Corollary [4.14](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem14 "Corollary 4.14. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")

Consider a collection of submodular retention functions {Rθ}θ∈Θ\{R\_{\theta}\}\_{\theta\in\Theta}. Assume that ∫ΘVθ​(Rθ,pθ)​𝑑μ≥0\int\_{\Theta}V\_{\theta}(R\_{\theta},p\_{\theta})d\mu\geq 0, and {pθ}θ∈Θ\{p\_{\theta}\}\_{\theta\in\Theta} satisfies ([4.10](https://arxiv.org/html/2602.09967v1#S4.Ex41 "Proposition 4.10. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) with,

|  |  |  |
| --- | --- | --- |
|  | pθ¯≤∫0L¯θ[ 1−gθ¯​(Fθ¯​(l))]​[1−∂Rθ¯​(l)∂l]​𝑑l.p\_{\underline{\theta}}\leq\int\_{0}^{\bar{L}\_{\theta}}\left[\,1-g\_{\underline{\theta}}(F\_{\underline{\theta}}(l))\,\right]\left[1-\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}\right]\,dl. |  |

It follows from Proposition [4.12](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem12 "Proposition 4.12. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") that (Rθ,pθ)θ∈Θ∈ℐ​𝒞(R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{C}.
It remains to show that (Rθ,pθ)θ∈Θ∈ℐ​ℛ(R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{R}. Since ∫ΘVθ​(Rθ,pθ)​𝑑μ≥0\int\_{\Theta}V\_{\theta}(R\_{\theta},p\_{\theta})d\mu\geq 0 and by Proposition [4.13](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem13 "Proposition 4.13. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), it is enough to show that condition (P1) of Definition [3.3](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem3 "Definition 3.3. ‣ 3.1. Incentive Pareto Optimality ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") holds for (Rθ¯,pθ¯)(R\_{\underline{\theta}},p\_{\underline{\theta}}).
We have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Uθ¯​(Rθ¯,pθ¯)\displaystyle U\_{\underline{\theta}}(R\_{\underline{\theta}},p\_{\underline{\theta}}) | =−pθ¯−∫0L¯[ 1−gθ¯​(Fθ¯​(l))]​∂Rθ¯​(l)∂l​𝑑l\displaystyle=-p\_{\underline{\theta}}-\int\_{0}^{\bar{L}}\left[\,1-g\_{\underline{\theta}}(F\_{\underline{\theta}}(l))\,\right]\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}\,dl |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥−[ 1−gθ¯​(Fθ¯​(l))]​[1−∂Rθ¯​(l)∂l]​d​l−∫0L¯[ 1−gθ¯​(Fθ¯​(l))]​∂Rθ¯​(l)∂l​𝑑l\displaystyle\geq-\left[\,1-g\_{\underline{\theta}}(F\_{\underline{\theta}}(l))\,\right]\left[1-\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}\right]\,dl-\int\_{0}^{\bar{L}}\left[\,1-g\_{\underline{\theta}}(F\_{\underline{\theta}}(l))\,\right]\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}\,dl |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−∫0L¯[ 1−gθ¯​(Fθ¯​(l))]​𝑑l=Uθ¯​(Lθ¯,0).\displaystyle=-\int\_{0}^{\bar{L}}\left[\,1-g\_{\underline{\theta}}(F\_{\underline{\theta}}(l))\,\right]dl=U\_{\underline{\theta}}(L\_{\underline{\theta}},0). |  |

Hence, (Rθ,pθ)θ∈Θ∈ℐ​ℛ(R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{R}. Conversely, assume that (Rθ,pθ)θ∈Θ∈ℐ​ℛ∩ℐ​𝒞(R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{R}\cap\mathcal{I}\mathcal{C}. It follows from Proposition [4.12](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem12 "Proposition 4.12. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), that {pθ}θ∈Θ\{p\_{\theta}\}\_{\theta\in\Theta} satisfies ([4.10](https://arxiv.org/html/2602.09967v1#S4.Ex41 "Proposition 4.10. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")).
Moreover, by individual rationality we know that

|  |  |  |
| --- | --- | --- |
|  | ∫ΘVθ​(Rθ,pθ)​𝑑μ≥0.\int\_{\Theta}V\_{\theta}(R\_{\theta},p\_{\theta})d\mu\geq 0. |  |

Additionally, by Proposition [4.13](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem13 "Proposition 4.13. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), (Rθ¯,pθ¯)(R\_{\underline{\theta}},p\_{\underline{\theta}}) satisfies (P1) of Definition [3.3](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem3 "Definition 3.3. ‣ 3.1. Incentive Pareto Optimality ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"). That is,

|  |  |  |
| --- | --- | --- |
|  | Uθ¯​(Rθ¯,pθ¯)≥Uθ¯​(Lθ¯,0),U\_{\underline{\theta}}(R\_{\underline{\theta}},p\_{\underline{\theta}})\geq U\_{\underline{\theta}}(L\_{\underline{\theta}},0), |  |

which implies that

|  |  |  |
| --- | --- | --- |
|  | pθ¯≤∫0L¯θ[ 1−gθ¯​(Fθ¯​(l))]​[1−∂Rθ¯​(l)∂l]​𝑑l.p\_{\underline{\theta}}\leq\int\_{0}^{\bar{L}\_{\theta}}\left[\,1-g\_{\underline{\theta}}(F\_{\underline{\theta}}(l))\,\right]\left[1-\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}\right]\,dl. |  |

∎

### B.8. Proof of Theorem [4.17](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem17 "Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")

The social welfare function is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wη,α​((Rθ,pθ)θ∈Θ)\displaystyle W\_{\eta,\alpha}\left((R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\right) | =α​∫ΘUθ​(Rθ,pθ)​𝑑η+(1−α)​∫ΘVθ​(Rθ,pθ)​𝑑μ\displaystyle=\alpha\int\_{\Theta}U\_{\theta}(R\_{\theta},p\_{\theta})\,d\eta+(1-\alpha)\int\_{\Theta}V\_{\theta}(R\_{\theta},p\_{\theta})\,d\mu |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =α​∫ΘUθ​(Rθ,pθ)​d​Qη​(θ)d​Q​(θ)​𝑑Q​(θ)+(1−α)​∫ΘVθ​(Rθ,pθ)​𝑑Q​(θ).\displaystyle=\alpha\int\_{\Theta}U\_{\theta}(R\_{\theta},p\_{\theta})\,\frac{dQ\_{\eta}(\theta)}{dQ(\theta)}dQ(\theta)+(1-\alpha)\int\_{\Theta}V\_{\theta}(R\_{\theta},p\_{\theta})\,dQ(\theta). |  |

That is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wη,α​((Rθ,pθ)θ∈Θ)\displaystyle W\_{\eta,\alpha}\left((R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\right) | =α​∫Θ[−pθ−∫0L¯[1−gθ​(Fθ​(l))]​∂Rθ​(l)∂l​𝑑l]​d​Qη​(θ)d​Q​(θ)​𝑑Q​(θ)\displaystyle=\alpha\int\_{\Theta}\left[-p\_{\theta}-\int\_{0}^{\bar{L}}\left[1-g\_{\theta}(F\_{\theta}(l))\right]\frac{\partial R\_{\theta}(l)}{\partial l}dl\right]\frac{dQ\_{\eta}(\theta)}{dQ(\theta)}dQ(\theta) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−α)​∫Θ[pθ−∫0L¯[1−gI​n​(Fθ​(l))]​[1−∂Rθ​(l)∂l]​𝑑l]​𝑑Q​(θ)\displaystyle\quad+(1-\alpha)\int\_{\Theta}\left[p\_{\theta}-\int\_{0}^{\bar{L}}\left[1-g^{In}\left(F\_{\theta}(l)\right)\right]\left[1-\frac{\partial R\_{\theta}(l)}{\partial l}\right]\,dl\right]\,dQ(\theta) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫Θ∫0L¯[(1−α)​[1−gI​n​(Fθ​(l))]−α​[1−gθ​(Fθ​(l))]​d​Qη​(θ)d​Q​(θ)]⋅∂Rθ​(l)∂l​𝑑l​𝑑Q​(θ)\displaystyle=\int\_{\Theta}\int\_{0}^{\bar{L}}\left[(1-\alpha)\left[1-g^{In}(F\_{\theta}(l))\right]-\alpha\left[1-g\_{\theta}(F\_{\theta}(l))\right]\frac{dQ\_{\eta}(\theta)}{dQ(\theta)}\right]\cdot\frac{\partial R\_{\theta}(l)}{\partial l}\,dl\,dQ(\theta) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫Θ[(1−α)−α​d​Qη​(θ)d​Q​(θ)]⋅pθ​𝑑Q​(θ)−(1−α)​∫Θ∫0L¯[1−gI​n​(Fθ​(l))]​𝑑l​𝑑Q​(θ).\displaystyle\quad+\int\_{\Theta}\left[(1-\alpha)-\alpha\frac{dQ\_{\eta}(\theta)}{dQ(\theta)}\right]\cdot p\_{\theta}\,dQ(\theta)-(1-\alpha)\int\_{\Theta}\int\_{0}^{\bar{L}}\left[1-g^{In}(F\_{\theta}(l))\right]\,dldQ(\theta)\,. |  |

For every (Rθ,pθ)θ∈Θ∈ℐ​𝒞(R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\in\mathcal{I}\mathcal{C} we know that the premium pθp\_{\theta} satisfies ([4.10](https://arxiv.org/html/2602.09967v1#S4.Ex41 "Proposition 4.10. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")). Substituting this premium into the social welfare function, we obtain

|  |  |  |
| --- | --- | --- |
|  | Wη,α​((Rθ,pθ)θ∈Θ)\displaystyle W\_{\eta,\alpha}\left((R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\right) |  |
|  |  |  |
| --- | --- | --- |
|  | =∫Θ∫0L¯[(1−α)​[1−gI​n​(Fθ​(l))]−α​[1−gθ​(Fθ​(l))]​d​Qη​(θ)d​Q​(θ)]⋅∂Rθ​(l)∂l​𝑑l​𝑑Q​(θ)\displaystyle\quad=\int\_{\Theta}\int\_{0}^{\bar{L}}\left[(1-\alpha)\left[1-g^{In}(F\_{\theta}(l))\right]-\alpha\left[1-g\_{\theta}(F\_{\theta}(l))\right]\frac{dQ\_{\eta}(\theta)}{dQ(\theta)}\right]\cdot\frac{\partial R\_{\theta}(l)}{\partial l}\,dl\,dQ(\theta) |  |
|  |  |  |
| --- | --- | --- |
|  | +∫Θ[(1−α)−α​d​Qη​(θ)d​Q​(θ)]⋅pθ¯​𝑑Q​(θ)\displaystyle\quad+\int\_{\Theta}\left[(1-\alpha)-\alpha\frac{dQ\_{\eta}(\theta)}{dQ(\theta)}\right]\cdot p\_{\underline{\theta}}\,dQ(\theta) |  |
|  |  |  |
| --- | --- | --- |
|  | +∫Θ[(1−α)−α​d​Qη​(θ)d​Q​(θ)]​∫0L¯[1−gθ¯​(Fθ¯​(l))]​∂Rθ¯​(l)∂l​𝑑l​𝑑Q​(θ)\displaystyle\quad+\int\_{\Theta}\left[(1-\alpha)-\alpha\frac{dQ\_{\eta}(\theta)}{dQ(\theta)}\right]\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\right]\,\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}\,dl\,dQ(\theta) |  |
|  |  |  |
| --- | --- | --- |
|  | −∫Θ[(1−α)−α​d​Qη​(θ)d​Q​(θ)]​∫θ¯θ∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​∂Rs​(l)∂l​𝑑l​𝑑s​𝑑Q​(θ)\displaystyle\quad-\int\_{\Theta}\left[(1-\alpha)-\alpha\frac{dQ\_{\eta}(\theta)}{dQ(\theta)}\right]\int\_{\underline{\theta}}^{\theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\frac{\partial R\_{s}(l)}{\partial l}\,dl\,dsdQ(\theta) |  |
|  |  |  |
| --- | --- | --- |
|  | −∫Θ[(1−α)−α​d​Qη​(θ)d​Q​(θ)]​∫0L¯[1−gθ​(Fθ​(l))]​∂Rθ​(l)∂l​𝑑l​𝑑Q​(θ)\displaystyle\quad-\int\_{\Theta}\left[(1-\alpha)-\alpha\frac{dQ\_{\eta}(\theta)}{dQ(\theta)}\right]\int\_{0}^{\bar{L}}\left[1-g\_{\theta}\big(F\_{\theta}(l)\big)\right]\,\frac{\partial R\_{\theta}(l)}{\partial l}\,dl\,dQ(\theta) |  |
|  |  |  |
| --- | --- | --- |
|  | −(1−α)​∫Θ∫0L¯[1−gI​n​(Fθ​(l))]​𝑑l​𝑑Q​(θ)\displaystyle\quad-(1-\alpha)\int\_{\Theta}\int\_{0}^{\bar{L}}\left[1-g^{In}(F\_{\theta}(l))\right]\,dldQ(\theta) |  |
|  |  |  |
| --- | --- | --- |
|  | =∫Θ∫0L¯[(1−α)​[1−gI​n​(Fθ​(l))]−α​[1−gθ​(Fθ​(l))]​d​Qη​(θ)d​Q​(θ)]⋅∂Rθ​(l)∂l​𝑑l​𝑑Q​(θ)\displaystyle=\int\_{\Theta}\int\_{0}^{\bar{L}}\left[(1-\alpha)\left[1-g^{In}(F\_{\theta}(l))\right]-\alpha\left[1-g\_{\theta}(F\_{\theta}(l))\right]\frac{dQ\_{\eta}(\theta)}{dQ(\theta)}\right]\cdot\frac{\partial R\_{\theta}(l)}{\partial l}\,dl\,dQ(\theta) |  |
|  |  |  |
| --- | --- | --- |
|  | +∫Θ[(1−α)−α​d​Qη​(θ)d​Q​(θ)]⋅[pθ¯+∫0L¯[1−gθ¯​(Fθ¯​(l))]​∂Rθ¯​(l)∂l​𝑑l]​𝑑Q​(θ)\displaystyle\quad+\int\_{\Theta}\left[(1-\alpha)-\alpha\frac{dQ\_{\eta}(\theta)}{dQ(\theta)}\right]\cdot\left[p\_{\underline{\theta}}+\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\right]\,\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}\,dl\right]\,dQ(\theta) |  |
|  |  |  |
| --- | --- | --- |
|  | −∫Θ[(1−α)−α​d​Qη​(θ)d​Q​(θ)]​∫θ¯θ∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​∂Rs​(l)∂l​𝑑l​𝑑s​𝑑Q​(θ)\displaystyle\quad-\int\_{\Theta}\left[(1-\alpha)-\alpha\frac{dQ\_{\eta}(\theta)}{dQ(\theta)}\right]\int\_{\underline{\theta}}^{\theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\frac{\partial R\_{s}(l)}{\partial l}\,dl\,dsdQ(\theta) |  |
|  |  |  |
| --- | --- | --- |
|  | −∫Θ[(1−α)−α​d​Qη​(θ)d​Q​(θ)]​∫0L¯[1−gθ​(Fθ​(l))]​∂Rθ​(l)∂l​𝑑l​𝑑Q​(θ)\displaystyle\quad-\int\_{\Theta}\left[(1-\alpha)-\alpha\frac{dQ\_{\eta}(\theta)}{dQ(\theta)}\right]\int\_{0}^{\bar{L}}\left[1-g\_{\theta}\big(F\_{\theta}(l)\big)\right]\,\frac{\partial R\_{\theta}(l)}{\partial l}\,dl\,dQ(\theta) |  |
|  |  |  |
| --- | --- | --- |
|  | −(1−α)​∫Θ∫0L¯[1−gI​n​(Fθ​(l))]​𝑑l​𝑑Q​(θ).\displaystyle\quad-(1-\alpha)\int\_{\Theta}\int\_{0}^{\bar{L}}\left[1-g^{In}(F\_{\theta}(l))\right]\,dldQ(\theta). |  |

Simplifying the first and fourth terms gives

|  |  |  |
| --- | --- | --- |
|  | Wη,α​((Rθ,pθ)θ∈Θ)\displaystyle W\_{\eta,\alpha}\left((R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\right) |  |
|  |  |  |
| --- | --- | --- |
|  | =∫Θ∫0L¯(1−α)​[gθ​(Fθ​(l))−gI​n​(Fθ​(l))]​∂Rθ​(l)∂l​𝑑l​𝑑Q​(θ)\displaystyle\quad=\int\_{\Theta}\int\_{0}^{\bar{L}}(1-\alpha)\left[g\_{\theta}(F\_{\theta}(l))-g^{In}(F\_{\theta}(l))\right]\frac{\partial R\_{\theta}(l)}{\partial l}\,dl\,dQ(\theta) |  |
|  |  |  |
| --- | --- | --- |
|  | +∫Θ[(1−α)−α​d​Qη​(θ)d​Q​(θ)]⋅[pθ¯+∫0L¯[1−gθ¯​(Fθ¯​(l))]​∂Rθ¯​(l)∂l​𝑑l]​𝑑Q​(θ)\displaystyle\quad+\int\_{\Theta}\left[(1-\alpha)-\alpha\frac{dQ\_{\eta}(\theta)}{dQ(\theta)}\right]\cdot\left[p\_{\underline{\theta}}+\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\right]\,\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}\,dl\right]\,dQ(\theta) |  |
|  |  |  |
| --- | --- | --- |
|  | −∫Θ[(1−α)−α​d​Qη​(θ)d​Q​(θ)]​∫θ¯θ∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​∂Rs​(l)∂l​𝑑l​𝑑s​𝑑Q​(θ)\displaystyle\quad-\int\_{\Theta}\left[(1-\alpha)-\alpha\frac{dQ\_{\eta}(\theta)}{dQ(\theta)}\right]\int\_{\underline{\theta}}^{\theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\frac{\partial R\_{s}(l)}{\partial l}\,dl\,dsdQ(\theta) |  |
|  |  |  |
| --- | --- | --- |
|  | −(1−α)​∫Θ∫0L¯[1−gI​n​(Fθ​(l))]​𝑑l​𝑑Q​(θ)\displaystyle\quad-(1-\alpha)\int\_{\Theta}\int\_{0}^{\bar{L}}\left[1-g^{In}(F\_{\theta}(l))\right]\,dldQ(\theta) |  |
|  |  |  |
| --- | --- | --- |
|  | =∫Θ∫0L¯(1−α)​[gθ​(Fθ​(l))−gI​n​(Fθ​(l))]​∂Rθ​(l)∂l​𝑑l​𝑑Q​(θ)\displaystyle=\int\_{\Theta}\int\_{0}^{\bar{L}}(1-\alpha)\left[g\_{\theta}(F\_{\theta}(l))-g^{In}(F\_{\theta}(l))\right]\frac{\partial R\_{\theta}(l)}{\partial l}\,dl\,dQ(\theta) |  |
|  |  |  |
| --- | --- | --- |
|  | +∫Θ[(1−α)−α​d​Qη​(θ)d​Q​(θ)]⋅[pθ¯+∫0L¯[1−gθ¯​(Fθ¯​(l))]​∂Rθ¯​(l)∂l​𝑑l]​𝑑Q​(θ)\displaystyle\quad+\int\_{\Theta}\left[(1-\alpha)-\alpha\frac{dQ\_{\eta}(\theta)}{dQ(\theta)}\right]\cdot\left[p\_{\underline{\theta}}+\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\right]\,\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}\,dl\right]\,dQ(\theta) |  |
|  |  |  |
| --- | --- | --- |
|  | −(1−α)​∫Θ∫θ¯θ∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​∂Rs​(l)∂l​𝑑l​𝑑s​𝑑Q​(θ)\displaystyle\quad-(1-\alpha)\int\_{\Theta}\int\_{\underline{\theta}}^{\theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\frac{\partial R\_{s}(l)}{\partial l}\,dl\,dsdQ(\theta) |  |
|  |  |  |
| --- | --- | --- |
|  | +α​∫Θ∫θ¯θ∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​∂Rs​(l)∂l​𝑑l​𝑑s​𝑑Qη​(θ)\displaystyle\quad+\alpha\int\_{\Theta}\int\_{\underline{\theta}}^{\theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\frac{\partial R\_{s}(l)}{\partial l}\,dl\,dsdQ\_{\eta}(\theta) |  |
|  |  |  |
| --- | --- | --- |
|  | −(1−α)​∫Θ∫0L¯[1−gI​n​(Fθ​(l))]​𝑑l​𝑑Q​(θ).\displaystyle\quad-(1-\alpha)\int\_{\Theta}\int\_{0}^{\bar{L}}\left[1-g^{In}(F\_{\theta}(l))\right]\,dldQ(\theta). |  |

Integrating the third and fourth terms by parts yields

|  |  |  |
| --- | --- | --- |
|  | Wη,α​((Rθ,pθ)θ∈Θ)\displaystyle W\_{\eta,\alpha}\left((R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\right) |  |
|  |  |  |
| --- | --- | --- |
|  | =∫Θ∫0L¯(1−α)​[gθ​(Fθ​(l))−gI​n​(Fθ​(l))]​∂Rθ​(l)∂l​𝑑l​𝑑Q​(θ)\displaystyle\quad=\int\_{\Theta}\int\_{0}^{\bar{L}}(1-\alpha)\left[g\_{\theta}(F\_{\theta}(l))-g^{In}(F\_{\theta}(l))\right]\frac{\partial R\_{\theta}(l)}{\partial l}\,dl\,dQ(\theta) |  |
|  |  |  |
| --- | --- | --- |
|  | +∫Θ[(1−α)−α​d​Qη​(θ)d​Q​(θ)]⋅[pθ¯+∫0L¯[1−gθ¯​(Fθ¯​(l))]​∂Rθ¯​(l)∂l​𝑑l]​𝑑Q​(θ)\displaystyle\quad+\int\_{\Theta}\left[(1-\alpha)-\alpha\frac{dQ\_{\eta}(\theta)}{dQ(\theta)}\right]\cdot\left[p\_{\underline{\theta}}+\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\right]\,\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}\,dl\right]\,dQ(\theta) |  |
|  |  |  |
| --- | --- | --- |
|  | +(1−α)​[∫θ¯θ∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​∂Rs​(l)∂l​𝑑l​𝑑s⋅Q¯​(θ)]θ=θ¯θ=θ¯\displaystyle\quad+(1-\alpha)\left[\int\_{\underline{\theta}}^{\theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\frac{\partial R\_{s}(l)}{\partial l}\,dl\,ds\cdot\bar{Q}(\theta)\right]\_{\theta=\underline{\theta}}^{\theta=\bar{\theta}} |  |
|  |  |  |
| --- | --- | --- |
|  | −(1−α)​∫Θ∫0L¯[∂gθ∂θ​(Fθ​(l))+gθ′​(Fθ​(l))​∂Fθ​(l)∂θ]​∂Rθ​(l)∂l​𝑑l​Q¯​(θ)​𝑑θ\displaystyle\quad-(1-\alpha)\int\_{\Theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{\theta}}{\partial\theta}(F\_{\theta}(l))+g^{\prime}\_{\theta}(F\_{\theta}(l))\frac{\partial F\_{\theta}(l)}{\partial\theta}\right]\frac{\partial R\_{\theta}(l)}{\partial l}\,dl\bar{Q}(\theta)d\theta |  |
|  |  |  |
| --- | --- | --- |
|  | −α​[∫θ¯θ∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​∂Rs​(l)∂l​𝑑l​𝑑s​Q¯η​(θ)]θ=θ¯θ=θ¯\displaystyle\quad-\alpha\left[\int\_{\underline{\theta}}^{\theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\frac{\partial R\_{s}(l)}{\partial l}\,dl\,ds\bar{Q}\_{\eta}(\theta)\right]\_{\theta=\underline{\theta}}^{\theta=\bar{\theta}} |  |
|  |  |  |
| --- | --- | --- |
|  | +α​∫Θ∫0L¯[∂gθ∂θ​(Fθ​(l))+gθ′​(Fθ​(l))​∂Fθ​(l)∂θ]​∂Rθ​(l)∂l​𝑑l​Q¯η​(θ)​𝑑θ\displaystyle\quad+\alpha\int\_{\Theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{\theta}}{\partial\theta}(F\_{\theta}(l))+g^{\prime}\_{\theta}(F\_{\theta}(l))\frac{\partial F\_{\theta}(l)}{\partial\theta}\right]\frac{\partial R\_{\theta}(l)}{\partial l}\,dl\bar{Q}\_{\eta}(\theta)d\theta |  |
|  |  |  |
| --- | --- | --- |
|  | −(1−α)​∫Θ∫0L¯[1−gI​n​(Fθ​(l))]​𝑑l​𝑑Q​(θ)\displaystyle\quad-(1-\alpha)\int\_{\Theta}\int\_{0}^{\bar{L}}\left[1-g^{In}(F\_{\theta}(l))\right]\,dldQ(\theta) |  |
|  |  |  |
| --- | --- | --- |
|  | =∫Θ∫0L¯(1−α)​[gθ​(Fθ​(l))−gI​n​(Fθ​(l))]​∂Rθ​(l)∂l​𝑑l​𝑑Q​(θ)\displaystyle=\int\_{\Theta}\int\_{0}^{\bar{L}}(1-\alpha)\left[g\_{\theta}(F\_{\theta}(l))-g^{In}(F\_{\theta}(l))\right]\frac{\partial R\_{\theta}(l)}{\partial l}\,dl\,dQ(\theta) |  |
|  |  |  |
| --- | --- | --- |
|  | +∫Θ[(1−α)−α​d​Qη​(θ)d​Q​(θ)]⋅[pθ¯+∫0L¯[1−gθ¯​(Fθ¯​(l))]​∂Rθ¯​(l)∂l​𝑑l]​𝑑Q​(θ)\displaystyle\quad+\int\_{\Theta}\left[(1-\alpha)-\alpha\frac{dQ\_{\eta}(\theta)}{dQ(\theta)}\right]\cdot\left[p\_{\underline{\theta}}+\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\right]\,\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}\,dl\right]\,dQ(\theta) |  |
|  |  |  |
| --- | --- | --- |
|  | −(1−α)​∫Θ∫0L¯[∂gθ∂θ​(Fθ​(l))+gθ′​(Fθ​(l))​∂Fθ​(l)∂θ]​∂Rθ​(l)∂l​𝑑l​Q¯​(θ)​𝑑θ\displaystyle\quad-(1-\alpha)\int\_{\Theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{\theta}}{\partial\theta}(F\_{\theta}(l))+g^{\prime}\_{\theta}(F\_{\theta}(l))\frac{\partial F\_{\theta}(l)}{\partial\theta}\right]\frac{\partial R\_{\theta}(l)}{\partial l}\,dl\bar{Q}(\theta)d\theta |  |
|  |  |  |
| --- | --- | --- |
|  | +α​∫Θ∫0L¯[∂gθ∂θ​(Fθ​(l))+gθ′​(Fθ​(l))​∂Fθ​(l)∂θ]​∂Rθ​(l)∂l​𝑑l​Q¯η​(θ)​𝑑θ\displaystyle\quad+\alpha\int\_{\Theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{\theta}}{\partial\theta}(F\_{\theta}(l))+g^{\prime}\_{\theta}(F\_{\theta}(l))\frac{\partial F\_{\theta}(l)}{\partial\theta}\right]\frac{\partial R\_{\theta}(l)}{\partial l}\,dl\bar{Q}\_{\eta}(\theta)d\theta |  |
|  |  |  |
| --- | --- | --- |
|  | −(1−α)​∫Θ∫0L¯[1−gI​n​(Fθ​(l))]​𝑑l​𝑑Q​(θ).\displaystyle\quad-(1-\alpha)\int\_{\Theta}\int\_{0}^{\bar{L}}\left[1-g^{In}(F\_{\theta}(l))\right]\,dldQ(\theta). |  |

Looking at the second term, we can see that [pθ¯+∫0L¯[1−gθ¯​(Fθ¯​(l))]​∂Rθ¯​(l)∂l​𝑑l]\left[p\_{\underline{\theta}}+\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\right]\,\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}\,dl\right] is independent of θ\theta. Hence,

|  |  |  |
| --- | --- | --- |
|  | Wη,α​((Rθ,pθ)θ∈Θ)\displaystyle W\_{\eta,\alpha}\left((R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\right) |  |
|  |  |  |
| --- | --- | --- |
|  | =∫Θ∫0L¯(1−α)​[gθ​(Fθ​(l))−gI​n​(Fθ​(l))]​∂Rθ​(l)∂l​𝑑l​𝑑Q​(θ)\displaystyle\quad=\int\_{\Theta}\int\_{0}^{\bar{L}}(1-\alpha)\left[g\_{\theta}(F\_{\theta}(l))-g^{In}(F\_{\theta}(l))\right]\frac{\partial R\_{\theta}(l)}{\partial l}\,dl\,dQ(\theta) |  |
|  |  |  |
| --- | --- | --- |
|  | +[pθ¯+∫0L¯[1−gθ¯​(Fθ¯​(l))]​∂Rθ¯​(l)∂l​𝑑l]⋅∫Θ[(1−α)−α​d​Qη​(θ)d​Q​(θ)]​𝑑Q​(θ)\displaystyle\quad+\left[p\_{\underline{\theta}}+\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\right]\,\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}\,dl\right]\cdot\int\_{\Theta}\left[(1-\alpha)-\alpha\frac{dQ\_{\eta}(\theta)}{dQ(\theta)}\right]dQ(\theta) |  |
|  |  |  |
| --- | --- | --- |
|  | −(1−α)​∫Θ∫0L¯[∂gθ∂θ​(Fθ​(l))+gθ′​(Fθ​(l))​∂Fθ​(l)∂θ]​∂Rθ​(l)∂l​𝑑l​Q¯​(θ)​𝑑θ\displaystyle\quad-(1-\alpha)\int\_{\Theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{\theta}}{\partial\theta}(F\_{\theta}(l))+g^{\prime}\_{\theta}(F\_{\theta}(l))\frac{\partial F\_{\theta}(l)}{\partial\theta}\right]\frac{\partial R\_{\theta}(l)}{\partial l}\,dl\bar{Q}(\theta)d\theta |  |
|  |  |  |
| --- | --- | --- |
|  | +α​∫Θ∫0L¯[∂gθ∂θ​(Fθ​(l))+gθ′​(Fθ​(l))​∂Fθ​(l)∂θ]​∂Rθ​(l)∂l​𝑑l​Q¯η​(θ)​𝑑θ−(1−α)​∫Θ∫0L¯[1−gI​n​(Fθ​(l))]​𝑑l​𝑑Q​(θ)\displaystyle\quad+\alpha\int\_{\Theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{\theta}}{\partial\theta}(F\_{\theta}(l))+g^{\prime}\_{\theta}(F\_{\theta}(l))\frac{\partial F\_{\theta}(l)}{\partial\theta}\right]\frac{\partial R\_{\theta}(l)}{\partial l}\,dl\bar{Q}\_{\eta}(\theta)d\theta-(1-\alpha)\int\_{\Theta}\int\_{0}^{\bar{L}}\left[1-g^{In}(F\_{\theta}(l))\right]\,dldQ(\theta) |  |
|  |  |  |
| --- | --- | --- |
|  | =∫Θ∫0L¯(1−α)​[gθ​(Fθ​(l))−gI​n​(Fθ​(l))]​∂Rθ​(l)∂l​𝑑l​𝑑Q​(θ)\displaystyle=\int\_{\Theta}\int\_{0}^{\bar{L}}(1-\alpha)\left[g\_{\theta}(F\_{\theta}(l))-g^{In}(F\_{\theta}(l))\right]\frac{\partial R\_{\theta}(l)}{\partial l}\,dl\,dQ(\theta) |  |
|  |  |  |
| --- | --- | --- |
|  | +[pθ¯+∫0L¯[1−gθ¯​(Fθ¯​(l))]​∂Rθ¯​(l)∂l​𝑑l]⋅[(1−α)​Q​(Θ)−α​Qη​(Θ)]\displaystyle\quad+\left[p\_{\underline{\theta}}+\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\right]\,\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}\,dl\right]\cdot\left[(1-\alpha)Q(\Theta)-\alpha Q\_{\eta}(\Theta)\right] |  |
|  |  |  |
| --- | --- | --- |
|  | −(1−α)​∫Θ∫0L¯[∂gθ∂θ​(Fθ​(l))+gθ′​(Fθ​(l))​∂Fθ​(l)∂θ]​∂Rθ​(l)∂l​𝑑l​Q¯​(θ)​𝑑θ\displaystyle\quad-(1-\alpha)\int\_{\Theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{\theta}}{\partial\theta}(F\_{\theta}(l))+g^{\prime}\_{\theta}(F\_{\theta}(l))\frac{\partial F\_{\theta}(l)}{\partial\theta}\right]\frac{\partial R\_{\theta}(l)}{\partial l}\,dl\bar{Q}(\theta)d\theta |  |
|  |  |  |
| --- | --- | --- |
|  | +α​∫Θ∫0L¯[∂gθ∂θ​(Fθ​(l))+gθ′​(Fθ​(l))​∂Fθ​(l)∂θ]​∂Rθ​(l)∂l​𝑑l​Q¯η​(θ)​𝑑θ−(1−α)​∫Θ∫0L¯[1−gI​n​(Fθ​(l))]​𝑑l​𝑑Q​(θ)\displaystyle\quad+\alpha\int\_{\Theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{\theta}}{\partial\theta}(F\_{\theta}(l))+g^{\prime}\_{\theta}(F\_{\theta}(l))\frac{\partial F\_{\theta}(l)}{\partial\theta}\right]\frac{\partial R\_{\theta}(l)}{\partial l}\,dl\bar{Q}\_{\eta}(\theta)d\theta-(1-\alpha)\int\_{\Theta}\int\_{0}^{\bar{L}}\left[1-g^{In}(F\_{\theta}(l))\right]\,dldQ(\theta) |  |
|  |  |  |
| --- | --- | --- |
|  | =∫Θ∫0L¯(1−α)​[gθ​(Fθ​(l))−gI​n​(Fθ​(l))]​∂Rθ​(l)∂l​𝑑l​𝑑Q​(θ)+(1−2​α)​[pθ¯+∫0L¯[1−gθ¯​(Fθ¯​(l))]​∂Rθ¯​(l)∂l​𝑑l]\displaystyle=\int\_{\Theta}\int\_{0}^{\bar{L}}(1-\alpha)\left[g\_{\theta}(F\_{\theta}(l))-g^{In}(F\_{\theta}(l))\right]\frac{\partial R\_{\theta}(l)}{\partial l}\,dl\,dQ(\theta)+(1-2\alpha)\left[p\_{\underline{\theta}}+\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\right]\,\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}\,dl\right] |  |
|  |  |  |
| --- | --- | --- |
|  | −(1−α)​∫Θ∫0L¯[∂gθ∂θ​(Fθ​(l))+gθ′​(Fθ​(l))​∂Fθ​(l)∂θ]​∂Rθ​(l)∂l​𝑑l​Q¯​(θ)​𝑑θ\displaystyle\quad-(1-\alpha)\int\_{\Theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{\theta}}{\partial\theta}(F\_{\theta}(l))+g^{\prime}\_{\theta}(F\_{\theta}(l))\frac{\partial F\_{\theta}(l)}{\partial\theta}\right]\frac{\partial R\_{\theta}(l)}{\partial l}\,dl\bar{Q}(\theta)d\theta |  |
|  |  |  |
| --- | --- | --- |
|  | +α​∫Θ∫0L¯[∂gθ∂θ​(Fθ​(l))+gθ′​(Fθ​(l))​∂Fθ​(l)∂θ]​∂Rθ​(l)∂l​𝑑l​Q¯η​(θ)​𝑑θ−(1−α)​∫Θ∫0L¯[1−gI​n​(Fθ​(l))]​𝑑l​𝑑Q​(θ)\displaystyle\quad+\alpha\int\_{\Theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{\theta}}{\partial\theta}(F\_{\theta}(l))+g^{\prime}\_{\theta}(F\_{\theta}(l))\frac{\partial F\_{\theta}(l)}{\partial\theta}\right]\frac{\partial R\_{\theta}(l)}{\partial l}\,dl\bar{Q}\_{\eta}(\theta)d\theta-(1-\alpha)\int\_{\Theta}\int\_{0}^{\bar{L}}\left[1-g^{In}(F\_{\theta}(l))\right]\,dldQ(\theta) |  |
|  |  |  |
| --- | --- | --- |
|  | =∫Θ∫0L¯(1−α)​[gθ​(Fθ​(l))−gI​n​(Fθ​(l))]​∂Rθ​(l)∂l​𝑑l​𝑑Q​(θ)+(1−2​α)​[pθ¯+∫0L¯[1−gθ¯​(Fθ¯​(l))]​∂Rθ¯​(l)∂l​𝑑l]\displaystyle=\int\_{\Theta}\int\_{0}^{\bar{L}}(1-\alpha)\left[g\_{\theta}(F\_{\theta}(l))-g^{In}(F\_{\theta}(l))\right]\frac{\partial R\_{\theta}(l)}{\partial l}\,dl\,dQ(\theta)+(1-2\alpha)\left[p\_{\underline{\theta}}+\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\right]\,\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}dl\right] |  |
|  |  |  |
| --- | --- | --- |
|  | −∫Θ∫0L¯[∂gθ∂θ​(Fθ​(l))+gθ′​(Fθ​(l))​∂Fθ​(l)∂θ]​∂Rθ​(l)∂l⋅[(1−α)​Q¯​(θ)−α​Q¯η​(θ)q​(θ)]​𝑑l​q​(θ)​𝑑θ\displaystyle\quad-\int\_{\Theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{\theta}}{\partial\theta}(F\_{\theta}(l))+g^{\prime}\_{\theta}(F\_{\theta}(l))\frac{\partial F\_{\theta}(l)}{\partial\theta}\right]\frac{\partial R\_{\theta}(l)}{\partial l}\cdot\left[\frac{(1-\alpha)\bar{Q}(\theta)-\alpha\bar{Q}\_{\eta}(\theta)}{q(\theta)}\right]\,dlq(\theta)d\theta |  |
|  |  |  |
| --- | --- | --- |
|  | −(1−α)​∫Θ∫0L¯[1−gI​n​(Fθ​(l))]​𝑑l​𝑑Q​(θ).\displaystyle\quad-(1-\alpha)\int\_{\Theta}\int\_{0}^{\bar{L}}\left[1-g^{In}(F\_{\theta}(l))\right]\,dldQ(\theta). |  |

Thus,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wη,α​((Rθ,pθ)θ∈Θ)\displaystyle W\_{\eta,\alpha}\left((R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\right) | =(1−2​α)​[pθ¯+∫0L¯[1−gθ¯​(Fθ¯​(l))]​∂Rθ¯​(l)∂l​𝑑l]−∫Θ∫0L¯Jθ,η​(l)​∂Rθ​(l)∂l​𝑑l​q​(θ)​𝑑θ\displaystyle=(1-2\alpha)\left[p\_{\underline{\theta}}+\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\right]\,\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}\,dl\right]-\int\_{\Theta}\int\_{0}^{\bar{L}}J\_{\theta,\eta}(l)\frac{\partial R\_{\theta}(l)}{\partial l}\,dl\,q(\theta)d\theta |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −(1−α)​∫Θ∫0L¯[1−gI​n​(Fθ​(l))]​𝑑l​𝑑Q​(θ),\displaystyle\qquad-(1-\alpha)\int\_{\Theta}\int\_{0}^{\bar{L}}\left[1-g^{In}(F\_{\theta}(l))\right]\,dldQ(\theta), |  | (27) |

where,

|  |  |  |
| --- | --- | --- |
|  | Jθ,η​(l)=(1−α)​[gI​n​(Fθ​(l))−gθ​(Fθ​(l))]+[∂gθ∂θ​(Fθ​(l))+gθ′​(Fθ​(l))​∂Fθ​(l)∂θ]​[(1−α)​Q¯​(θ)−α​Q¯η​(θ)q​(θ)],J\_{\theta,\eta}(l)=(1-\alpha)\left[g^{In}(F\_{\theta}(l))-g\_{\theta}(F\_{\theta}(l))\right]+\left[\frac{\partial g\_{\theta}}{\partial\theta}(F\_{\theta}(l))+g^{\prime}\_{\theta}(F\_{\theta}(l))\frac{\partial F\_{\theta}(l)}{\partial\theta}\right]\left[\frac{(1-\alpha)\bar{Q}(\theta)-\alpha\bar{Q}\_{\eta}(\theta)}{q(\theta)}\right], |  |

which can be rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jθ,η​(l)=(1−α)​[gI​n​(Fθ​(l))−gθ​(Fθ​(l))]+(Q¯​(θ)q​(θ))​[∂gθ∂θ​(Fθ​(l))+gθ′​(Fθ​(l))​∂Fθ​(l)∂θ]​[(1−α)−α​Q¯η​(θ)Q¯​(θ)].J\_{\theta,\eta}(l)=(1-\alpha)\left[g^{In}(F\_{\theta}(l))-g\_{\theta}(F\_{\theta}(l))\right]+\left(\frac{\bar{Q}(\theta)}{q(\theta)}\right)\left[\frac{\partial g\_{\theta}}{\partial\theta}(F\_{\theta}(l))+g^{\prime}\_{\theta}(F\_{\theta}(l))\frac{\partial F\_{\theta}(l)}{\partial\theta}\right]\left[(1-\alpha)-\alpha\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)}\right]. |  | (28) |

We now consider the following three cases for the values of the social weight α∈(0,1]\alpha\in(0,1].

#### B.8.1. The case where α≤12\alpha\leq\frac{1}{2}

The social welfare function Wη,α​((Rθ,pθ)θ∈Θ)W\_{\eta,\alpha}\left((R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\right) given by ([B.8](https://arxiv.org/html/2602.09967v1#A2.Ex263 "B.8. Proof of Theorem 4.17 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) is non-decreasing with respect to pθ¯p\_{\underline{\theta}}, and then at the optimum, pθ¯∗p^{\*}\_{\underline{\theta}} must take its largest value.
By individual rationality, we conclude from Proposition [4.5](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem5 "Proposition 4.5. ‣ 4.1. Dual Utility Framework ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") that:

|  |  |  |
| --- | --- | --- |
|  | pθ¯∗=∫0L¯[1−gθ¯​(Fθ¯​(l))]​[1−∂Rθ¯​(l)∂l]​𝑑l.p^{\*}\_{\underline{\theta}}=\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}(F\_{\underline{\theta}}(l))\,\right]\left[1-\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}\right]\,dl\,. |  |

Using the premium pθ¯=∫0L¯[1−gθ¯​(Fθ¯​(l))]​[1−∂Rθ¯​(l)∂l]​𝑑lp\_{\underline{\theta}}=\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}(F\_{\underline{\theta}}(l))\,\right]\left[1-\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}\right]\,dl, the social welfare functions simplifies to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wη,α​((Rθ,pθ)θ∈Θ)\displaystyle W\_{\eta,\alpha}\left((R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\right) | =(1−2​α)⋅∫0L¯[1−gθ¯​(Fθ¯​(l))]​𝑑l−∫Θ∫0L¯Jθ,η​(l)​∂Rθ​(l)∂l​𝑑l​q​(θ)​𝑑θ\displaystyle=(1-2\alpha)\cdot\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}(F\_{\underline{\theta}}(l))\right]\,dl-\int\_{\Theta}\int\_{0}^{\bar{L}}J\_{\theta,\eta}(l)\frac{\partial R\_{\theta}(l)}{\partial l}\,dl\,q(\theta)d\theta |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −(1−α)​∫Θ∫0L¯[1−gI​n​(Fθ​(l))]​𝑑l​𝑑Q​(θ).\displaystyle\qquad-(1-\alpha)\int\_{\Theta}\int\_{0}^{\bar{L}}\left[1-g^{In}(F\_{\theta}(l))\right]\,dldQ(\theta). |  |

To find a solution for Problem ([4](https://arxiv.org/html/2602.09967v1#S4.E4 "Equation 4 ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")), we aim to maximize this function pointwise. We first start by analyzing Jθ,η​(l)J\_{\theta,\eta}(l) given by ([28](https://arxiv.org/html/2602.09967v1#A2.E28 "Equation 28 ‣ B.8. Proof of Theorem 4.17 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")). Firstly, since α≤12\alpha\leq\frac{1}{2} and by Assumption [4.4](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem4 "Assumption 4.4. ‣ 4.1. Dual Utility Framework ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), the first term is non-negative:

|  |  |  |
| --- | --- | --- |
|  | (1−α)​[gI​n​(Fθ​(l))−gθ​(Fθ​(l))]≥0.(1-\alpha)\left[g^{In}(F\_{\theta}(l))-g\_{\theta}(F\_{\theta}(l))\right]\geq 0\,. |  |

Moreover, by Assumption [4.7](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem7 "Assumption 4.7. ‣ 4.2. Type Ordering under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection") and Assumptions [4.8](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem8 "Assumption 4.8. ‣ 4.2. Type Ordering under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), we know that

|  |  |  |
| --- | --- | --- |
|  | Q¯​(θ)q​(θ)​[∂gθ∂θ​(Fθ​(l))+gθ′​(Fθ​(l))​∂Fθ​(l)∂θ]≤0.\frac{\bar{Q}(\theta)}{q(\theta)}\left[\frac{\partial g\_{\theta}}{\partial\theta}(F\_{\theta}(l))+g^{\prime}\_{\theta}(F\_{\theta}(l))\frac{\partial F\_{\theta}(l)}{\partial\theta}\right]\leq 0\,. |  |

Using ([6](https://arxiv.org/html/2602.09967v1#S4.E6 "Equation 6 ‣ Remark 4.16. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")), we observe that for θ=θ¯\theta=\underline{\theta},

|  |  |  |
| --- | --- | --- |
|  | [(1−α)−α​Q¯η​(θ)Q¯​(θ)]θ=θ¯=1−2​α.\left[(1-\alpha)-\alpha\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)}\right]\_{\theta=\underline{\theta}}=1-2\alpha. |  |

Using ([7](https://arxiv.org/html/2602.09967v1#S4.E7 "Equation 7 ‣ Remark 4.16. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")), for θ=θ¯\theta=\bar{\theta}, we have

|  |  |  |
| --- | --- | --- |
|  | [(1−α)−α​Q¯η​(θ)Q¯​(θ)]θ=θ¯=1−α−α​qη​(θ¯)q​(θ¯).\left[(1-\alpha)-\alpha\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)}\right]\_{\theta=\bar{\theta}}=1-\alpha-\alpha\frac{q\_{\eta}(\bar{\theta})}{q(\bar{\theta})}. |  |

Moreover, the function θ↦(1−α)−α​Q¯η​(θ)Q¯​(θ)\theta\mapsto(1-\alpha)-\alpha\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)} is non-increasing in θ∈Θ\theta\in\Theta, since Q¯η​(θ)Q¯​(θ)\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)} is non-decreasing in θ\theta.
This means that if 1−α−α​qη​(θ¯)q​(θ¯)>01-\alpha-\alpha\frac{q\_{\eta}(\bar{\theta})}{q(\bar{\theta})}>0, or equivalently α<q​(θ¯)qη​(θ¯)+q​(θ¯)≤12\alpha<\frac{q(\bar{\theta})}{q\_{\eta}(\bar{\theta})+q(\bar{\theta})}\leq\frac{1}{2}, then

|  |  |  |
| --- | --- | --- |
|  | 1−α−α​Q¯η​(θ)Q¯​(θ)>0,∀θ∈Θ.1-\alpha-\alpha\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)}>0,\ \forall\,\theta\in\Theta. |  |

Hence,

|  |  |  |
| --- | --- | --- |
|  | Q¯​(θ)q​(θ)​[(1−α)−α​Q¯η​(θ)Q¯​(θ)]​[∂gθ∂θ​(Fθ​(l))+gθ′​(Fθ​(l))​∂Fθ​(l)∂θ]≤0.\frac{\bar{Q}(\theta)}{q(\theta)}\left[(1-\alpha)-\alpha\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)}\right]\left[\frac{\partial g\_{\theta}}{\partial\theta}(F\_{\theta}(l))+g^{\prime}\_{\theta}(F\_{\theta}(l))\frac{\partial F\_{\theta}(l)}{\partial\theta}\right]\leq 0\,. |  |

For a fixed θ∈Θ\theta\in\Theta, the optimal retention satisfies

|  |  |  |
| --- | --- | --- |
|  | Rθ∗∈arg⁡maxRθ∈ℛ−∫0L¯Jθ,η​(l)​∂Rθ​(l)∂l​𝑑l.R^{\*}\_{\theta}\in\underset{R\_{\theta}\in\mathcal{R}}{\arg\max}\ -\int\_{0}^{\bar{L}}J\_{\theta,\eta}(l)\frac{\partial R\_{\theta}(l)}{\partial l}\,dl\,. |  |

Hence if α∈(0,q​(θ¯)qη​(θ¯)+q​(θ¯))\alpha\in\left(0,\frac{q(\bar{\theta})}{q\_{\eta}(\bar{\theta})+q(\bar{\theta})}\right), then the optimal retention function satisfies the following:

|  |  |  |
| --- | --- | --- |
|  | ∂Rθ∗​(l)∂l={0Jθ,η​(l)>0,∈[0,1]Jθ,η​(l)=0,1Jθ,η​(l)<0.\frac{\partial R^{\*}\_{\theta}(l)}{\partial l}=\begin{cases}0&J\_{\theta,\eta}(l)>0,\\ \in[0,1]&J\_{\theta,\eta}(l)=0,\\ 1&J\_{\theta,\eta}(l)<0.\end{cases} |  |

When η\eta and α\alpha are specified, for any θ<θ′\theta<\theta^{\prime}, and if Jθ,η​(l)J\_{\theta,\eta}(l) is non-decreasing in θ\theta for all ll, then Jη,α,θ​(l)<Jη,α,θ′​(l)J\_{\eta,\alpha,\theta}(l)<J\_{\eta,\alpha,\theta^{\prime}}(l). The pointwise maximization solution satisfies:

|  |  |  |
| --- | --- | --- |
|  | ∂Rη,α,θ′∗​(l)∂l≤∂Rη,α,θ∗​(l)∂l∀l,\frac{\partial R^{\*}\_{\eta,\alpha,\theta^{\prime}}(l)}{\partial l}\leq\frac{\partial R^{\*}\_{\eta,\alpha,\theta}(l)}{\partial l}\ \ \forall\,l\,, |  |

which implies that Rη,α,θ∗R^{\*}\_{\eta,\alpha,\theta} is submodular.

#### B.8.2. The case where α∈[q​(θ¯)qη​(θ¯)+q​(θ¯),12]\alpha\in\left[\frac{q(\bar{\theta})}{q\_{\eta}(\bar{\theta})+q(\bar{\theta})},\frac{1}{2}\right]

There exists θα∈Θ\theta\_{\alpha}\in\Theta, such that 1−α−α​Q¯η​(θα)Q¯​(θα)=01-\alpha-\alpha\frac{\bar{Q}\_{\eta}(\theta\_{\alpha})}{\bar{Q}(\theta\_{\alpha})}=0.
Since the function θ↦(1−α)−α​Q¯η​(θ)Q¯​(θ)\theta\mapsto(1-\alpha)-\alpha\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)} is non-increasing in θ∈Θ\theta\in\Theta, it foll.ows that:

1. (i)

   If θ<θα\theta<\theta\_{\alpha}, then 1−α−α​Q¯η​(θ)Q¯​(θ)≥01-\alpha-\alpha\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)}\geq 0. Therefore, if the function Jθ,η​(l)J\_{\theta,\eta}(l) is non-decreasing in θ\theta, then the optimal retention function Rθ∗R^{\*}\_{\theta} follows the form given in ([9](https://arxiv.org/html/2602.09967v1#S4.E9 "Equation 9 ‣ Item 1 ‣ Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")).
2. (ii)

   If θ≥θα\theta\geq\theta\_{\alpha}, then 1−α−α​Q¯η​(θ)Q¯​(θ)≤01-\alpha-\alpha\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)}\leq 0. Therefore Jθ,η≥0J\_{\theta,\eta}\geq 0 for all ll. It follows that Rθ∗=0R^{\*}\_{\theta}=0 in this case.

#### B.8.3. The case where α>12\alpha>\frac{1}{2}

The social welfare function in ([B.8](https://arxiv.org/html/2602.09967v1#A2.Ex263 "B.8. Proof of Theorem 4.17 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) is non-increasing in pθ¯p\_{\underline{\theta}}. Therefore, at the optimum, pθ¯p\_{\underline{\theta}} must take its smallest value while still satisfying the IR condition. By Proposition [4.5](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem5 "Proposition 4.5. ‣ 4.1. Dual Utility Framework ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), pθ¯∗=0p^{\*}\_{\underline{\theta}}=0. Substituting this into the social welfare function in ([B.8](https://arxiv.org/html/2602.09967v1#A2.Ex263 "B.8. Proof of Theorem 4.17 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")), we obtain the following:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wη,α​((Rθ,pθ)θ∈Θ)\displaystyle W\_{\eta,\alpha}\left((R\_{\theta},p\_{\theta})\_{\theta\in\Theta}\right) | =(1−2​α)​∫0L¯[1−gθ¯​(Fθ¯​(l))]⋅∂Rθ¯​(l)∂l​𝑑l−(1−α)​∫Θ∫0L¯[1−gI​n​(Fθ​(l))]​𝑑l​𝑑Q​(θ)\displaystyle=(1-2\alpha)\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}(F\_{\underline{\theta}}(l))\right]\cdot\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}\,dl-(1-\alpha)\int\_{\Theta}\int\_{0}^{\bar{L}}\left[1-g^{In}(F\_{\theta}(l))\right]\,dldQ(\theta) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫Θ∫0L¯Jθ,η​(l)​∂Rθ​(l)∂l​𝑑l​q​(θ)​𝑑θ\displaystyle\quad-\int\_{\Theta}\int\_{0}^{\bar{L}}J\_{\theta,\eta}(l)\frac{\partial R\_{\theta}(l)}{\partial l}\,dl\,q(\theta)d\theta |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫Θ∫0L¯[(1−2​α)​[1−gθ¯​(Fθ¯​(l))]​∂Rθ¯​(l)∂l−Jθ,η​(l)​∂Rθ​(l)∂l]​𝑑l​q​(θ)​𝑑θ\displaystyle=\int\_{\Theta}\int\_{0}^{\bar{L}}\left[(1-2\alpha)\left[1-g\_{\underline{\theta}}(F\_{\underline{\theta}}(l))\right]\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}-J\_{\theta,\eta}(l)\frac{\partial R\_{\theta}(l)}{\partial l}\right]\,dl\,q(\theta)\,d\theta |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −(1−α)​∫Θ∫0L¯[1−gI​n​(Fθ​(l))]​𝑑l​𝑑Q​(θ).\displaystyle\quad-(1-\alpha)\int\_{\Theta}\int\_{0}^{\bar{L}}\left[1-g^{In}(F\_{\theta}(l))\right]\,dldQ(\theta). |  |

In this case, 1−α−α​Q¯η​(θ)Q¯​(θ)<01-\alpha-\alpha\frac{\bar{Q}\_{\eta}(\theta)}{\bar{Q}(\theta)}<0 for all θ∈Θ\theta\in\Theta. This implies that Jθ,η≥0J\_{\theta,\eta}\geq 0 for all θ∈Θ\theta\in\Theta. In particular, for θ=θ¯\theta=\underline{\theta}, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wη,α​(Rθ¯,pθ¯)\displaystyle W\_{\eta,\alpha}(R\_{\underline{\theta}},p\_{\underline{\theta}}) | =∫Θ∫0L¯((1−2​α)​[1−gθ¯​(Fθ¯​(l))]−Jθ¯,η​(l))​∂Rθ¯​(l)∂l​𝑑l​q​(θ)​𝑑θ\displaystyle=\int\_{\Theta}\int\_{0}^{\bar{L}}\bigg((1-2\alpha)\left[1-g\_{\underline{\theta}}(F\_{\underline{\theta}}(l))\right]-J\_{\underline{\theta},\eta}(l)\bigg)\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}\,dl\,q(\theta)\,d\theta |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −(1−α)​∫Θ∫0L¯[1−gI​n​(Fθ​(l))]​𝑑l​𝑑Q​(θ).\displaystyle\qquad-(1-\alpha)\int\_{\Theta}\int\_{0}^{\bar{L}}\left[1-g^{In}(F\_{\theta}(l))\right]\,dldQ(\theta). |  |

We define J~θ¯,η​(l)\widetilde{J}\_{\underline{\theta},\eta}(l) by
J~θ¯,η​(l):=−(1−2​α)​[1−gθ¯​(Fθ¯​(l))]+Jθ¯,η​(l).\widetilde{J}\_{\underline{\theta},\eta}(l):=-(1-2\alpha)\left[1-g\_{\underline{\theta}}(F\_{\underline{\theta}}(l))\right]+J\_{\underline{\theta},\eta}(l)\,.
For α>12\alpha>\frac{1}{2}, we have the following:

|  |  |  |
| --- | --- | --- |
|  | J~θ¯,η​(l)≥Jθ¯,η​(l)≥0.\displaystyle\widetilde{J}\_{\underline{\theta},\eta}(l)\geq J\_{\underline{\theta},\eta}(l)\geq 0\,. |  |

The optimal retention function for the lowest risk type θ¯\underline{\theta}, satisfies:

|  |  |  |
| --- | --- | --- |
|  | Rθ¯∗∈arg⁡maxRθ¯∈ℛ−∫0L¯J~θ¯,η​(l)​∂Rθ¯​(l)∂l​𝑑l.R\_{\underline{\theta}}^{\*}\in\underset{R\_{\underline{\theta}}\in\mathcal{R}}{\arg\max}-\int\_{0}^{\bar{L}}\widetilde{J}\_{\underline{\theta},\eta}(l)\frac{\partial R\_{\underline{\theta}}(l)}{\partial l}\,dl\,. |  |

For all the other risk types θ\theta, the optimal retention function satisfies:

|  |  |  |
| --- | --- | --- |
|  | Rθ∗∈arg⁡maxRθ∈ℛ−∫0L¯Jθ,η​(l)​∂Rθ​(l)∂l​𝑑l.R\_{\theta}^{\*}\in\underset{R\_{\theta}\in\mathcal{R}}{\arg\max}-\int\_{0}^{\bar{L}}J\_{\theta,\eta}(l)\frac{\partial R\_{\theta}(l)}{\partial l}\,dl\,. |  |

The pointwise maximization implies that ∂Rθ∗​(l)∂l=0\frac{\partial R^{\*}\_{\theta}(l)}{\partial l}=0, for all ll. Thus, Rθ∗=0R^{\*}\_{\theta}=0 for all θ∈Θ\theta\in\Theta. ∎

### B.9. Proof of Lemma [4.18](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem18 "Lemma 4.18. ‣ 4.5. Properties of the Optimal Menu ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")

Consider an optimal incentive efficient menu of contracts (Rθ∗,pθ∗)θ∈Θ(R^{\*}\_{\theta},p^{\*}\_{\theta})\_{\theta\in\Theta}. The insurer’s aggregate utility is given by:

|  |  |  |
| --- | --- | --- |
|  | ∫ΘVθ​(Rθ∗,pθ∗)​𝑑μ=∫Θpθ∗​𝑑μ−∫Θ∫0L¯[1−gI​n​(Fθ​(l))]​(1−∂Rθ∗​(l)∂l)​𝑑l​𝑑μ.\displaystyle\int\_{\Theta}V\_{\theta}(R^{\*}\_{\theta},p^{\*}\_{\theta})\,d\mu=\int\_{\Theta}p^{\*}\_{\theta}\,d\mu-\int\_{\Theta}\int\_{0}^{\bar{L}}\left[1-g^{In}(F\_{\theta}(l))\right]\left(1-\frac{\partial R^{\*}\_{\theta}(l)}{\partial l}\right)\,dl\,d\mu. |  |

Assuming that the optimal premium pθ∗p^{\*}\_{\theta} satisfies ([1](https://arxiv.org/html/2602.09967v1#S4.Ex49 "Item 1 ‣ Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")), the insurer’s aggregate utility becomes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫ΘVθ​(Rθ∗,pθ∗)​𝑑μ\displaystyle\int\_{\Theta}V\_{\theta}(R^{\*}\_{\theta},p^{\*}\_{\theta})\,d\mu | =∫Θ∫0L¯[1−gθ¯​(Fθ¯​(l))]​𝑑l​𝑑μ−∫Θ∫θ¯θ∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​∂Rs∗​(l)∂l​𝑑l​𝑑s\displaystyle=\int\_{\Theta}\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\right]\,dl\,d\mu-\int\_{\Theta}\int\_{\underline{\theta}}^{\theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\frac{\partial R^{\*}\_{s}(l)}{\partial l}\,dl\,ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫Θ∫0L¯[1−gθ​(Fθ​(l))]​∂Rθ∗​(l)∂l​𝑑l−∫Θ∫0L¯[1−gI​n​(Fθ​(l))]​(1−∂Rθ∗​(l)∂l)​𝑑l​𝑑μ.\displaystyle\quad-\int\_{\Theta}\int\_{0}^{\bar{L}}\left[1-g\_{\theta}\big(F\_{\theta}(l)\big)\right]\,\frac{\partial R^{\*}\_{\theta}(l)}{\partial l}\,dl-\int\_{\Theta}\int\_{0}^{\bar{L}}\left[1-g^{In}(F\_{\theta}(l))\right]\left(1-\frac{\partial R^{\*}\_{\theta}(l)}{\partial l}\right)\,dl\,d\mu. |  |

We consider the following three cases for the optimal marginal retention function.

1. (1)

   If ∂Rθ∗∂l≡0\frac{\partial R^{\*}\_{\theta}}{\partial l}\equiv 0, and by the insurer’s participation constraint (P2) of Definition [3.3](https://arxiv.org/html/2602.09967v1#S3.Thmtheorem3 "Definition 3.3. ‣ 3.1. Incentive Pareto Optimality ‣ 3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), we have: ∫ΘVθ​(Rθ∗,pθ∗)​𝑑μ≥0\int\_{\Theta}V\_{\theta}(R^{\*}\_{\theta},p^{\*}\_{\theta})\,d\mu\geq 0. Hence,

   |  |  |  |
   | --- | --- | --- |
   |  | ∫Θ∫0L¯[gI​n​(Fθ​(l))−gθ¯​(Fθ¯​(l))]​𝑑l​𝑑μ≥0,\int\_{\Theta}\int\_{0}^{\bar{L}}\left[g^{In}(F\_{\theta}(l))-g\_{\underline{\theta}}(F\_{\underline{\theta}}(l))\right]\,dl\,d\mu\geq 0, |  |

   or equivalently,

   |  |  |  |
   | --- | --- | --- |
   |  | ∫Θ∫0L¯gI​n​(Fθ​(l))​𝑑l​𝑑μ≥∫0L¯gθ¯​(Fθ¯​(l))​𝑑l.\int\_{\Theta}\int\_{0}^{\bar{L}}g^{In}(F\_{\theta}(l))\,dl\,d\mu\geq\int\_{0}^{\bar{L}}g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\,dl. |  |
2. (2)

   Suppose that ∂Rθ∗∂l≡1\frac{\partial R^{\*}\_{\theta}}{\partial l}\equiv 1. Then using the optimal premium pθ∗p^{\*}\_{\theta} given in ([1](https://arxiv.org/html/2602.09967v1#S4.Ex49 "Item 1 ‣ Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) for θ∈Θ\theta\in\Theta, the insurer’s utility reduces to the following:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Vθ​(Rθ∗,pθ∗)\displaystyle V\_{\theta}(R^{\*}\_{\theta},p^{\*}\_{\theta}) | =∫0L¯[gθ​(Fθ​(l))−gθ¯​(Fθ¯​(l))]​𝑑l−∫θ¯θ∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​𝑑l​𝑑s\displaystyle=\int\_{0}^{\bar{L}}\left[g\_{\theta}(F\_{\theta}(l))-g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\right]\,dl-\int\_{\underline{\theta}}^{\theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\,dl\,ds |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | =∫0L¯∫θ¯θ∂∂s​(gs∘Fs)​(l)​𝑑s​𝑑l−∫θ¯θ∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​𝑑l​𝑑s\displaystyle=\int\_{0}^{\bar{L}}\int\_{\underline{\theta}}^{\theta}\frac{\partial}{\partial s}(g\_{s}\circ F\_{s})(l)ds\,dl-\int\_{\underline{\theta}}^{\theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\,dl\,ds |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | =0.\displaystyle=0. |  |
3. (3)

   If ∂Rθ∗∂l\frac{\partial R^{\*}\_{\theta}}{\partial l} takes values in (0,1)(0,1), then

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∫ΘVθ​(Rθ∗,pθ∗)​𝑑μ\displaystyle\int\_{\Theta}V\_{\theta}(R^{\*}\_{\theta},p^{\*}\_{\theta})\,d\mu | =∫Θ∫0L¯[gI​n​(Fθ​(l))−gθ¯​(Fθ¯​(l))]​𝑑l​𝑑μ+∫Θ∫0L¯[gθ​(Fθ​(l))−gI​n​(Fθ​(l))]​∂Rθ∗​(l)∂l​𝑑l​𝑑μ\displaystyle=\int\_{\Theta}\int\_{0}^{\bar{L}}\left[g^{In}(F\_{\theta}(l))-g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\right]\,dl\,d\mu+\int\_{\Theta}\int\_{0}^{\bar{L}}\left[g\_{\theta}\big(F\_{\theta}(l)\big)-g^{In}(F\_{\theta}(l))\right]\,\frac{\partial R^{\*}\_{\theta}(l)}{\partial l}\,dl\,d\mu |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | −∫Θ∫θ¯θ∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​∂Rs∗​(l)∂l​𝑑l​𝑑s​𝑑μ.\displaystyle\quad-\int\_{\Theta}\int\_{\underline{\theta}}^{\theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\frac{\partial R^{\*}\_{s}(l)}{\partial l}\,dl\,dsd\mu. |  |

   We know that

   |  |  |  |
   | --- | --- | --- |
   |  | ∫Θ∫θ¯θ∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​∂Rs∗​(l)∂l​𝑑l​𝑑s​𝑑μ≤0,\int\_{\Theta}\int\_{\underline{\theta}}^{\theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\frac{\partial R^{\*}\_{s}(l)}{\partial l}\,dl\,dsd\mu\leq 0, |  |

   and

   |  |  |  |
   | --- | --- | --- |
   |  | gθ​(Fθ​(l))−gI​n​(Fθ​(l))≤0.g\_{\theta}\big(F\_{\theta}(l)\big)-g^{In}(F\_{\theta}(l))\leq 0. |  |

   Since ∫ΘVθ​(Rθ∗,pθ∗)​𝑑μ≥0\int\_{\Theta}V\_{\theta}(R^{\*}\_{\theta},p^{\*}\_{\theta})\,d\mu\geq 0, we then must have:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∫Θ∫0L¯gI​n​(Fθ​(l))​𝑑l​𝑑μ\displaystyle\int\_{\Theta}\int\_{0}^{\bar{L}}g^{In}(F\_{\theta}(l))\,dl\,d\mu | ≥∫0L¯gθ¯​(Fθ¯​(l))​𝑑l+∫Θ∫θ¯θ∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​∂Rs∗​(l)∂l​𝑑l​𝑑s​𝑑μ\displaystyle\geq\int\_{0}^{\bar{L}}g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\,dl+\int\_{\Theta}\int\_{\underline{\theta}}^{\theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\frac{\partial R^{\*}\_{s}(l)}{\partial l}\,dl\,dsd\mu |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | −∫Θ∫0L¯[gθ​(Fθ​(l))−gI​n​(Fθ​(l))]​∂Rθ∗​(l)∂l​𝑑l​𝑑μ.\displaystyle\quad-\int\_{\Theta}\int\_{0}^{\bar{L}}\left[g\_{\theta}\big(F\_{\theta}(l)\big)-g^{In}(F\_{\theta}(l))\right]\,\frac{\partial R^{\*}\_{\theta}(l)}{\partial l}\,dl\,d\mu. |  |

   Moreover, it follows from the envelope theorem, that:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∫Θ∫θ¯θ∫0L¯[∂gs∂s​(Fs​(l))+gs′​(Fs​(l))​∂Fs​(l)∂s]​∂Rs∗​(l)∂l​𝑑l​𝑑s​𝑑μ\displaystyle\int\_{\Theta}\int\_{\underline{\theta}}^{\theta}\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{s}}{\partial s}(F\_{s}(l))+g^{\prime}\_{s}(F\_{s}(l))\frac{\partial F\_{s}(l)}{\partial s}\right]\frac{\partial R^{\*}\_{s}(l)}{\partial l}\,dl\,dsd\mu | =∫ΘUθ​(Rθ∗,pθ∗)​𝑑μ−Uθ¯​(Rθ¯∗,pθ¯∗).\displaystyle=\int\_{\Theta}U\_{\theta}(R^{\*}\_{\theta},p^{\*}\_{\theta})\,d\mu-U\_{\underline{\theta}}(R^{\*}\_{\underline{\theta}},p^{\*}\_{\underline{\theta}}). |  |

   Hence, we obtain:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∫Θ∫0L¯gI​n​(Fθ​(l))​𝑑l​𝑑μ\displaystyle\int\_{\Theta}\int\_{0}^{\bar{L}}g^{In}(F\_{\theta}(l))\,dl\,d\mu | ≥∫0L¯gθ¯​(Fθ¯​(l))​𝑑l+∫ΘUθ​(Rθ∗,pθ∗)​𝑑μ−Uθ¯​(Rθ¯∗,pθ¯∗)\displaystyle\geq\int\_{0}^{\bar{L}}g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\,dl+\int\_{\Theta}U\_{\theta}(R^{\*}\_{\theta},p^{\*}\_{\theta})\,d\mu-U\_{\underline{\theta}}(R^{\*}\_{\underline{\theta}},p^{\*}\_{\underline{\theta}}) |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | +∫Θ∫0L¯[gI​n​(Fθ​(l))−gθ​(Fθ​(l))]​∂Rθ∗​(l)∂l​𝑑l​𝑑μ.\displaystyle\quad+\int\_{\Theta}\int\_{0}^{\bar{L}}\left[g^{In}(F\_{\theta}(l))-g\_{\theta}(F\_{\theta}(l))\right]\,\frac{\partial R^{\*}\_{\theta}(l)}{\partial l}\,dl\,d\mu. |  |

We now consider the case where for each θ∈Θ\theta\in\Theta, pθ∗=0p^{\*}\_{\theta}=0, and Rθ∗​(l)=0R^{\*}\_{\theta}(l)=0 for all ll. The insurer’s aggregate utility in this case reduces to

|  |  |  |
| --- | --- | --- |
|  | ∫ΘVθ​(Rθ∗,pθ∗)​𝑑μ=−∫Θ∫0L¯[1−gI​n​(Fθ​(l))]​𝑑l​𝑑μ≤0.\int\_{\Theta}V\_{\theta}(R^{\*}\_{\theta},p^{\*}\_{\theta})\,d\mu=-\int\_{\Theta}\int\_{0}^{\bar{L}}\left[1-g^{In}(F\_{\theta}(l))\right]\,dl\,d\mu\leq 0. |  |

However, since the optimal menu (Rθ∗,pθ∗)θ∈Θ(R^{\*}\_{\theta},p^{\*}\_{\theta})\_{\theta\in\Theta} is individually rational, then we know by (P2) that ∫ΘVθ​(Rθ∗,pθ∗)​𝑑μ≥0\int\_{\Theta}V\_{\theta}(R^{\*}\_{\theta},p^{\*}\_{\theta})\,d\mu\geq 0. Hence, we must have:

|  |  |  |
| --- | --- | --- |
|  | ∫ΘVθ​(Rθ∗,pθ∗)​𝑑μ=0,\int\_{\Theta}V\_{\theta}(R^{\*}\_{\theta},p^{\*}\_{\theta})\,d\mu=0, |  |

which implies that gI​n​(Fθ​(l))=1g^{In}(F\_{\theta}(l))=1, for almost every θ∈Θ\theta\in\Theta and almost every l∈[0,L¯]l\in[0,\bar{L}]. ∎

### B.10. Proof of Proposition [4.19](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem19 "Proposition 4.19. ‣ 4.5. Properties of the Optimal Menu ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")

Consider the optimal menu of contracts (Rθ∗,pθ∗)θ∈Θ(R^{\*}\_{\theta},p^{\*}\_{\theta})\_{\theta\in\Theta}, characterized in Theorem [4.17](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem17 "Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"). Differentiating the insurer’s utility with respect to θ\theta, we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂Vθ​(Rθ∗,pθ∗)∂θ\displaystyle\frac{\partial V\_{\theta}(R^{\*}\_{\theta},p^{\*}\_{\theta})}{\partial\theta} | =∂pθ∗∂θ+∫0L¯gI​n⁣′​(Fθ​(l))​∂Fθ​(l)∂θ​(1−∂Rθ∗​(l)∂l)​𝑑l+∫0L¯[1−gI​n​(Fθ​(l))]​∂2Rθ∗​(l)∂θ​∂l​𝑑l\displaystyle=\frac{\partial p^{\*}\_{\theta}}{\partial\theta}+\int\_{0}^{\bar{L}}g^{In\,\prime}(F\_{\theta}(l))\frac{\partial F\_{\theta}(l)}{\partial\theta}\left(1-\frac{\partial R^{\*}\_{\theta}(l)}{\partial l}\right)\,dl+\int\_{0}^{\bar{L}}\left[1-g^{In}(F\_{\theta}(l))\right]\frac{\partial^{2}R^{\*}\_{\theta}(l)}{\partial\theta\partial l}\,dl |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0L¯[gθ​(Fθ​(l))−gI​n​(Fθ​(l))]​∂2Rθ∗​(l)∂θ​∂l​𝑑l+∫0L¯gI​n⁣′​(Fθ​(l))​∂Fθ​(l)∂θ​(1−∂Rθ∗​(l)∂l)​𝑑l.\displaystyle=\int\_{0}^{\bar{L}}\left[g\_{\theta}\big(F\_{\theta}(l)\big)-g^{In}(F\_{\theta}(l))\right]\,\frac{\partial^{2}R^{\*}\_{\theta}(l)}{\partial\theta\partial l}\,dl+\int\_{0}^{\bar{L}}g^{In\,\prime}(F\_{\theta}(l))\frac{\partial F\_{\theta}(l)}{\partial\theta}\left(1-\frac{\partial R^{\*}\_{\theta}(l)}{\partial l}\right)\,dl. |  |

We consider the following three cases.

1. (1)

   If ∂Rθ∗∂l≡0\frac{\partial R^{\*}\_{\theta}}{\partial l}\equiv 0, then ∂2Rθ∗∂θ​∂l≡0\frac{\partial^{2}R^{\*}\_{\theta}}{\partial\theta\partial l}\equiv 0. The partial derivative of the insurer’s utility reduces to the following:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∂Vθ​(Rθ∗,pθ∗)∂θ\displaystyle\frac{\partial V\_{\theta}(R^{\*}\_{\theta},p^{\*}\_{\theta})}{\partial\theta} | =∫0L¯gI​n⁣′​(Fθ​(l))​∂Fθ​(l)∂θ​𝑑l≤0,\displaystyle=\int\_{0}^{\bar{L}}g^{In\,\prime}(F\_{\theta}(l))\frac{\partial F\_{\theta}(l)}{\partial\theta}\,dl\leq 0, |  |

   since ∂Fθ​(l)∂θ≤0\frac{\partial F\_{\theta}(l)}{\partial\theta}\leq 0.
2. (2)

   If ∂Rθ∗∂l≡1\frac{\partial R^{\*}\_{\theta}}{\partial l}\equiv 1, then ∂2Rθ∗∂θ​∂l≡0\frac{\partial^{2}R^{\*}\_{\theta}}{\partial\theta\partial l}\equiv 0. The partial derivative of the insurer’s utility in this case reduces to the following:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∂Vθ​(Rθ∗,pθ∗)∂θ\displaystyle\frac{\partial V\_{\theta}(R^{\*}\_{\theta},p^{\*}\_{\theta})}{\partial\theta} | =0.\displaystyle=0. |  |
3. (3)

   If ∂Rθ∗∂l\frac{\partial R^{\*}\_{\theta}}{\partial l} takes values in (0,1)(0,1), then by submodularity of the optimal collection of retention functions, ∂2Rθ∗∂θ​∂l≤0\frac{\partial^{2}R^{\*}\_{\theta}}{\partial\theta\partial l}\leq 0. Hence, the partial derivative of the insurer’s utility in this case is given by:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∂Vθ​(Rθ∗,pθ∗)∂θ\displaystyle\frac{\partial V\_{\theta}(R^{\*}\_{\theta},p^{\*}\_{\theta})}{\partial\theta} | =∫0L¯[[gθ​(Fθ​(l))−gI​n​(Fθ​(l))]​∂2Rθ∗​(l)∂θ​∂l+gI​n⁣′​(Fθ​(l))​∂Fθ​(l)∂θ​(1−∂Rθ∗​(l)∂l)]​𝑑l.\displaystyle=\int\_{0}^{\bar{L}}\left[\left[g\_{\theta}\big(F\_{\theta}(l)\big)-g^{In}(F\_{\theta}(l))\right]\,\frac{\partial^{2}R^{\*}\_{\theta}(l)}{\partial\theta\partial l}+g^{In\,\prime}(F\_{\theta}(l))\frac{\partial F\_{\theta}(l)}{\partial\theta}\left(1-\frac{\partial R^{\*}\_{\theta}(l)}{\partial l}\right)\right]\,dl. |  |

   We know that

   |  |  |  |
   | --- | --- | --- |
   |  | [gθ​(Fθ​(l))−gI​n​(Fθ​(l))]​∂2Rθ∗​(l)∂θ​∂l≥0,\left[g\_{\theta}\big(F\_{\theta}(l)\big)-g^{In}(F\_{\theta}(l))\right]\,\frac{\partial^{2}R^{\*}\_{\theta}(l)}{\partial\theta\partial l}\geq 0, |  |

   since gI​n​(Fθ​(l))≥gθ​(Fθ​(l))g^{In}(F\_{\theta}(l))\geq g\_{\theta}\big(F\_{\theta}(l)\big), for each θ∈Θ\theta\in\Theta, and {Rθ∗}θ∈Θ\{R^{\*}\_{\theta}\}\_{\theta\in\Theta} is submodular. Moreover,

   |  |  |  |
   | --- | --- | --- |
   |  | gI​n⁣′​(Fθ​(l))​∂Fθ​(l)∂θ​(1−∂Rθ∗​(l)∂l)≤0,g^{In\,\prime}(F\_{\theta}(l))\frac{\partial F\_{\theta}(l)}{\partial\theta}\left(1-\frac{\partial R^{\*}\_{\theta}(l)}{\partial l}\right)\leq 0, |  |

   since ∂Fθ​(l)∂θ≤0\frac{\partial F\_{\theta}(l)}{\partial\theta}\leq 0 for all ll. Hence, Vθ​(Rθ∗,pθ∗)V\_{\theta}(R^{\*}\_{\theta},p^{\*}\_{\theta}) increases with θ\theta, if

   |  |  |  |
   | --- | --- | --- |
   |  | [gθ​(Fθ​(l))−gI​n​(Fθ​(l))]​∂2Rθ∗​(l)∂θ​∂l≥−gI​n⁣′​(Fθ​(l))​∂Fθ​(l)∂θ​(1−∂Rθ∗​(l)∂l).\left[g\_{\theta}\big(F\_{\theta}(l)\big)-g^{In}(F\_{\theta}(l))\right]\,\frac{\partial^{2}R^{\*}\_{\theta}(l)}{\partial\theta\partial l}\geq-g^{In\,\prime}(F\_{\theta}(l))\frac{\partial F\_{\theta}(l)}{\partial\theta}\left(1-\frac{\partial R^{\*}\_{\theta}(l)}{\partial l}\right). |  |

∎

### B.11. Proof of Proposition [4.20](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem20 "Proposition 4.20. ‣ 4.5. Properties of the Optimal Menu ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")

Consider the optimal menu of contracts (Rθ∗,pθ∗)θ∈Θ(R^{\*}\_{\theta},p^{\*}\_{\theta})\_{\theta\in\Theta}, characterized in Theorem [4.17](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem17 "Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").

(1) Since {Rθ∗}θ∈Θ\{R^{\*}\_{\theta}\}\_{\theta\in\Theta} is submodular, it follows that Rθ∗R^{\*}\_{\theta} decreases with θ\theta. Moreover, the optimal premium is given by ([1](https://arxiv.org/html/2602.09967v1#S4.Ex49 "Item 1 ‣ Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")). Differentiating this expression with respect to θ\theta, we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂pθ∗∂θ\displaystyle\frac{\partial p^{\*}\_{\theta}}{\partial\theta} | =−∫0L¯[∂gθ∂θ​(Fθ​(l))+gθ′​(Fθ​(l))​∂Fθ​(l)∂θ]​∂Rθ∗​(l)∂l​𝑑l​𝑑θ−∫0L¯[1−gθ​(Fθ​(l))]​∂2Rθ∗​(l)∂θ​∂l​𝑑l\displaystyle=-\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{\theta}}{\partial\theta}(F\_{\theta}(l))+g^{\prime}\_{\theta}(F\_{\theta}(l))\frac{\partial F\_{\theta}(l)}{\partial\theta}\right]\frac{\partial R^{\*}\_{\theta}(l)}{\partial l}\,dl\,d\theta-\int\_{0}^{\bar{L}}\left[1-g\_{\theta}\big(F\_{\theta}(l)\big)\right]\,\frac{\partial^{2}R^{\*}\_{\theta}(l)}{\partial\theta\partial l}\,dl |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0L¯[∂gθ∂θ​(Fθ​(l))+gθ′​(Fθ​(l))​∂Fθ​(l)∂θ]​∂Rθ∗​(l)∂l\displaystyle\quad+\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{\theta}}{\partial\theta}(F\_{\theta}(l))+g^{\prime}\_{\theta}(F\_{\theta}(l))\frac{\partial F\_{\theta}(l)}{\partial\theta}\right]\frac{\partial R^{\*}\_{\theta}(l)}{\partial l} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−∫0L¯[1−gθ​(Fθ​(l))]​∂2Rθ∗​(l)∂θ​∂l​𝑑l≥0,\displaystyle=-\int\_{0}^{\bar{L}}\left[1-g\_{\theta}\big(F\_{\theta}(l)\big)\right]\,\frac{\partial^{2}R^{\*}\_{\theta}(l)}{\partial\theta\partial l}\,dl\geq 0, |  |

since ∂2Rθ∗​(l)∂θ​∂l≤0\frac{\partial^{2}R^{\*}\_{\theta}(l)}{\partial\theta\partial l}\leq 0. Hence, the optimal premium pθ∗p^{\*}\_{\theta} increases with θ\theta.

(2) For θ=θ¯\theta=\bar{\theta}, we have:

|  |  |  |
| --- | --- | --- |
|  | Jθ¯,η​(l)=(1−α)​[gI​n​(Fθ¯​(l))−gθ¯​(Fθ¯​(l))]≥0,∀l,J\_{\bar{\theta},\eta}(l)=(1-\alpha)\left[g^{In}(F\_{\bar{\theta}}(l))-g\_{\bar{\theta}}(F\_{\bar{\theta}}(l))\right]\geq 0,\ \forall l, |  |

by Assumption [4.4](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem4 "Assumption 4.4. ‣ 4.1. Dual Utility Framework ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"). Then, ∂Rθ¯∗​(l)∂l=0\frac{\partial R^{\*}\_{\bar{\theta}}(l)}{\partial l}=0 for all ll, and hence Rθ¯∗​(l)=0R^{\*}\_{\bar{\theta}}(l)=0 for all ll.

(3) For θ=θ¯\theta=\underline{\theta}, the optimal premium given in ([1](https://arxiv.org/html/2602.09967v1#S4.Ex49 "Item 1 ‣ Theorem 4.17. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) reduces to

|  |  |  |  |
| --- | --- | --- | --- |
|  | pθ∗\displaystyle p^{\*}\_{\theta} | =∫0L¯[1−gθ¯​(Fθ¯​(l))]​[1−∂Rθ∗​(l)∂l]​𝑑l.\displaystyle=\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\right]\left[1-\frac{\partial R^{\*}\_{\theta}(l)}{\partial l}\right]\,dl. |  |

Hence, the least risk averse agent’s end-of-period utility is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Uθ¯​(Rθ¯∗,pθ¯∗)\displaystyle U\_{\underline{\theta}}(R^{\*}\_{\underline{\theta}},p^{\*}\_{\underline{\theta}}) | =−pθ¯∗−∫0L¯[1−gθ¯​(Fθ¯​(l))]​∂Rθ¯∗​(l)∂l​𝑑l=−∫0L¯[1−gθ¯​(Fθ¯​(l))]​𝑑l=Uθ¯​(Lθ¯,0).\displaystyle=-p^{\*}\_{\underline{\theta}}-\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\right]\,\frac{\partial R^{\*}\_{\underline{\theta}}(l)}{\partial l}\,dl=-\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}\big(F\_{\underline{\theta}}(l)\big)\right]\,dl=U\_{\underline{\theta}}(L\_{\underline{\theta}},0). |  |

(4) It follows from the envelope theorem that the partial derivative of Uθ​(Rθ∗,pθ∗)U\_{\theta}(R^{\*}\_{\theta},p^{\*}\_{\theta}) with respect to θ\theta is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂Uθ​(Rθ∗,pθ∗)∂θ\displaystyle\frac{\partial U\_{\theta}(R^{\*}\_{\theta},p^{\*}\_{\theta})}{\partial\theta} | =∫0L¯[∂gθ∂θ​(Fθ​(l))+gθ′​(Fθ​(l))​∂Fθ​(l)∂θ]​∂Rθ∗​(l)∂l​𝑑l≤0.\displaystyle=\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{\theta}}{\partial\theta}(F\_{\theta}(l))+g^{\prime}\_{\theta}(F\_{\theta}(l))\frac{\partial F\_{\theta}(l)}{\partial\theta}\right]\frac{\partial R^{\*}\_{\theta}(l)}{\partial l}\,dl\leq 0. |  |

Moreover, the second-order derivative with respect to θ\theta is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂2Uθ​(Rθ∗,pθ∗)∂θ2\displaystyle\frac{\partial^{2}U\_{\theta}(R^{\*}\_{\theta},p^{\*}\_{\theta})}{\partial\theta^{2}} | =∫0L¯[∂gθ∂θ​(Fθ​(l))+gθ′​(Fθ​(l))​∂Fθ​(l)∂θ]​∂2Rθ∗​(l)∂θ​∂l​𝑑l\displaystyle=\int\_{0}^{\bar{L}}\left[\frac{\partial g\_{\theta}}{\partial\theta}(F\_{\theta}(l))+g^{\prime}\_{\theta}(F\_{\theta}(l))\frac{\partial F\_{\theta}(l)}{\partial\theta}\right]\frac{\partial^{2}R^{\*}\_{\theta}(l)}{\partial\theta\partial l}\,dl |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0L¯[∂2gθ∂θ2​(Fθ​(l))+∂2gθ∂θ​∂t​(Fθ​(l))​∂Fθ​(l)∂θ+gθ′′​(Fθ​(l))​(∂Fθ​(l)∂θ)2+gθ′​(Fθ​(l))​∂2Fθ​(l)∂θ2]​∂Rθ∗​(l)∂l​𝑑l.\displaystyle\quad+\int\_{0}^{\bar{L}}\left[\frac{\partial^{2}g\_{\theta}}{\partial\theta^{2}}(F\_{\theta}(l))+\frac{\partial^{2}g\_{\theta}}{\partial\theta\partial t}(F\_{\theta}(l))\frac{\partial F\_{\theta}(l)}{\partial\theta}+g^{\prime\prime}\_{\theta}(F\_{\theta}(l))\left(\frac{\partial F\_{\theta}(l)}{\partial\theta}\right)^{2}+g^{\prime}\_{\theta}(F\_{\theta}(l))\frac{\partial^{2}F\_{\theta}(l)}{\partial\theta^{2}}\right]\frac{\partial R^{\*}\_{\theta}(l)}{\partial l}\,dl. |  |

The above expression is non-negative if the following conditions hold:

1. (i)

   The function g:(θ,t)↦gθ​(t)g:(\theta,t)\mapsto g\_{\theta}(t) is submodular. That is,

   |  |  |  |
   | --- | --- | --- |
   |  | ∂2gθ​(t)∂θ​∂t≤0.\frac{\partial^{2}g\_{\theta}(t)}{\partial\theta\partial t}\leq 0. |  |
2. (ii)

   The function θ↦gθ​(t)\theta\mapsto g\_{\theta}(t) is convex in θ\theta, for all tt. That is,

   |  |  |  |
   | --- | --- | --- |
   |  | ∂2gθ​(t)∂θ2≥0,∀t.\frac{\partial^{2}g\_{\theta}(t)}{\partial\theta^{2}}\geq 0,\ \forall t. |  |
3. (iii)

   The function t↦gθ​(t)t\mapsto g\_{\theta}(t) is convex in tt, for all θ∈Θ\theta\in\Theta. That is,

   |  |  |  |
   | --- | --- | --- |
   |  | ∂2gθ​(t)∂t2≥0,∀θ.\frac{\partial^{2}g\_{\theta}(t)}{\partial t^{2}}\geq 0,\ \forall\theta. |  |
4. (iv)

   The function θ↦Fθ​(l)\theta\mapsto F\_{\theta}(l) is convex in θ\theta, for all ll. That is,

   |  |  |  |
   | --- | --- | --- |
   |  | ∂2Fθ​(l)∂θ2≥0,∀l.\frac{\partial^{2}F\_{\theta}(l)}{\partial\theta^{2}}\geq 0,\ \forall l. |  |

∎

### B.12. Proof of Theorem [4.22](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem22 "Theorem 4.22. ‣ 4.6.1. Insurer’s Welfare Maximization ‣ 4.6. Special Cases of Social Weight ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")

First note that the total utility given in ([4.21](https://arxiv.org/html/2602.09967v1#S4.Ex57 "Proposition 4.21. ‣ 4.6.1. Insurer’s Welfare Maximization ‣ 4.6. Special Cases of Social Weight ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) is an increasing function of pθ¯p\_{\underline{\theta}}. Therefore at the optimum, the corresponding pθ¯p\_{\underline{\theta}} must take its largest value provided individual rationality is satisfied. Then by Proposition [4.5](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem5 "Proposition 4.5. ‣ 4.1. Dual Utility Framework ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), the largest value of the premium is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | pθ¯∗=∫0L¯[1−gθ¯​(Fθ¯)]​[1−∂Rθ¯​(l)∂l]​𝑑l.p^{\*}\_{\underline{\theta}}=\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}(F\_{\underline{\theta}})\right]\left[1-\frac{\partial R\_{\underline{\theta}(l)}}{\partial l}\right]\,dl. |  | (29) |

For any θ∈Θ\theta\in\Theta and Rθ∈ℛR\_{\theta}\in\mathcal{R}, we know that Rθ​(0)=0R\_{\theta}(0)=0, and ∂Rθ​(l)∂l∈[0,1]\frac{\partial R\_{\theta}(l)}{\partial l}\in[0,1].
The uniformly bounded set ℛ\mathcal{R} of retention functions consists of 1-Lipschitz continuous functions on [0,1][0,1]. ℛ\mathcal{R} is therefore equicontinuous, and hence compact by the Arzela-Ascoli Theorem.
An optimal solution for ([14](https://arxiv.org/html/2602.09967v1#S4.E14 "Equation 14 ‣ 4.6.1. Insurer’s Welfare Maximization ‣ 4.6. Special Cases of Social Weight ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) exists since the profit functional is continuous and the set of retention functions ℛ\mathcal{R} is compact.
Replacing pθ¯=∫0L¯[1−gθ¯​(Fθ¯)]​[1−∂Rθ¯​(l)∂l]​𝑑lp\_{\underline{\theta}}=\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}(F\_{\underline{\theta}})\right]\left[1-\frac{\partial R\_{\underline{\theta}(l)}}{\partial l}\right]\,dl in ([4.21](https://arxiv.org/html/2602.09967v1#S4.Ex57 "Proposition 4.21. ‣ 4.6.1. Insurer’s Welfare Maximization ‣ 4.6. Special Cases of Social Weight ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")), we obtain the following:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0L¯[1−gθ¯​(Fθ¯​(l))]​𝑑l−∫Θ(∫0L¯Jθ​(l)​∂Rθ​(l)∂l​𝑑l)​q​(θ)​𝑑θ−∫Θ∫0L¯[1−gI​n​(Fθ​(l))]​q​(θ)​𝑑l​𝑑θ.\displaystyle\int\_{0}^{\bar{L}}\left[1-g\_{\underline{\theta}}(F\_{\underline{\theta}}(l))\right]\ dl-\int\_{\Theta}\left(\int\_{0}^{\bar{L}}\ J\_{\theta}(l)\frac{\partial R\_{\theta}(l)}{\partial l}dl\right)q(\theta)d\theta-\int\_{\Theta}\int\_{0}^{\bar{L}}\left[1-g^{In}(F\_{\theta}(l))\right]q(\theta)\ dl\,d\theta. |  | (30) |

We maximize ([30](https://arxiv.org/html/2602.09967v1#A2.E30 "Equation 30 ‣ B.12. Proof of Theorem 4.22 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) pointwise. For a fixed θ∈Θ\theta\in\Theta, we look for

|  |  |  |
| --- | --- | --- |
|  | Rθ∗∈arg⁡maxRθ∈ℛ​{−∫0L¯Jθ​(l)​∂Rθ​(l)∂l​𝑑l}.R^{\*}\_{\theta}\in\underset{R\_{\theta}\in\mathcal{R}}{\arg\max}\left\{-\int\_{0}^{\bar{L}}J\_{\theta}(l)\frac{\partial R\_{\theta}(l)}{\partial l}\,dl\right\}. |  |

The maximum is achieved when

|  |  |  |
| --- | --- | --- |
|  | ∂Rθ∗​(l)∂l={0,Jθ​(l)>0,∈[0,1],Jθ​(l)=0,1,Jθ​(l)<0.\frac{\partial R^{\*}\_{\theta}(l)}{\partial l}=\begin{cases}0,&J\_{\theta}(l)>0,\\ \in[0,1],&J\_{\theta}(l)=0,\\ 1,&J\_{\theta}(l)<0.\end{cases} |  |

by assumption, we know that Jθ​(l)J\_{\theta}(l) is increasing in θ\theta for all ll.
That is, for each θ,θ′∈Θ\theta,\theta^{\prime}\in\Theta;
θ<θ′,Jθ​(l)<Jθ′​(l).\theta<\theta^{\prime},\ J\_{\theta}(l)<J\_{\theta^{\prime}}(l). It follows that the pointwise maximization solution is such that for any θ<θ′\theta<\theta^{\prime},

|  |  |  |
| --- | --- | --- |
|  | ∂Rθ′∗​(l)∂l≤∂Rθ∗​(l)∂l,∀l.\frac{\partial R^{\*}\_{\theta^{\prime}}(l)}{\partial l}\leq\frac{\partial R^{\*}\_{\theta}(l)}{\partial l},\ \forall\ l. |  |

Hence, Rθ∗​(l)R^{\*}\_{\theta}(l) is submodular since we have shown that ∂Rθ∗∂l\frac{\partial R^{\*}\_{\theta}}{\partial l} is non-increasing in θ\theta (Definition [4.11](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem11 "Definition 4.11. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")).
Now, since Rθ∗​(l)R^{\*}\_{\theta}(l) is submodular, and pθ∗p^{\*}\_{\theta} satisfies ([4.10](https://arxiv.org/html/2602.09967v1#S4.Ex41 "Proposition 4.10. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")) with pθ¯∗p\_{\underline{\theta}}^{\*} given by ([29](https://arxiv.org/html/2602.09967v1#A2.E29 "Equation 29 ‣ B.12. Proof of Theorem 4.22 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection")), then by Proposition [4.12](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem12 "Proposition 4.12. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"), (Rθ∗,pθ∗)∈ℐ​𝒞(R^{\*}\_{\theta},p^{\*}\_{\theta})\in\mathcal{I}\mathcal{C}.
In addition, we have that ∫ΘVθ​(Rθ∗,pθ∗)​𝑑μ≥0\int\_{\Theta}V\_{\theta}(R^{\*}\_{\theta},p^{\*}\_{\theta})d\mu\geq 0 ensuring that (Rθ∗,pθ∗)∈ℐ​ℛ(R^{\*}\_{\theta},p^{\*}\_{\theta})\in\mathcal{I}\mathcal{R} by Corollary [4.14](https://arxiv.org/html/2602.09967v1#S4.Thmtheorem14 "Corollary 4.14. ‣ 4.3. Solution Characterization Under Dual Utility ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").

## References

* M. Allais (1953)
  L’éxtension des Théories de l’Équilibre Économique General et du Rendement Social au Cas du Risque.
  Econometrica 21 (2),  pp. 269–290.
  Cited by: [§1](https://arxiv.org/html/2602.09967v1#S1.p1.1 "1. Introduction ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
* A. Bisin and P. Gottardi (2006)
  Efficient competitive equilibria with adverse selection.
  Journal of political Economy 114 (3),  pp. 485–516.
  Cited by: [§1](https://arxiv.org/html/2602.09967v1#S1.p4.1 "1. Introduction ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
* G. Carlier and R. Dana (2003)
  Pareto efficient insurance contracts when the insurer’s cost function is discontinuous.
  Economic Theory 21 (4),  pp. 871–893.
  External Links: ISBN 1432-0479
  Cited by: [§2](https://arxiv.org/html/2602.09967v1#S2.p4.1 "2. The Insurance Market ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
* H. Chade and E. Schlee (2012)
  Optimal insurance with adverse selection.
  Theoretical Economics 7 (3),  pp. 571–607.
  Cited by: [§1](https://arxiv.org/html/2602.09967v1#S1.p3.1 "1. Introduction ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"),
  [§1](https://arxiv.org/html/2602.09967v1#S1.p8.1 "1. Introduction ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"),
  [§4.5](https://arxiv.org/html/2602.09967v1#S4.SS5.p5.4 "4.5. Properties of the Optimal Menu ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"),
  [§4.5](https://arxiv.org/html/2602.09967v1#S4.SS5.p6.3 "4.5. Properties of the Optimal Menu ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
* A. Chateauneuf and M. Cohen (1994)
  Risk seeking with diminishing marginal utility in a non-expected utility model.
  Journal of Risk and Uncertainty 9 (1),  pp. 77–91.
  Cited by: [§4.1](https://arxiv.org/html/2602.09967v1#S4.SS1.p2.3 "4.1. Dual Utility Framework ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
* S.H. Chew, E. Karni, and Z. Safra (1987)
  Risk Aversion in the Theory of Expected Utility with Rank Dependent Pobabilities.
  Journal of Economic Theory 42 (2),  pp. 370–381.
  Cited by: [§4.1](https://arxiv.org/html/2602.09967v1#S4.SS1.p2.3 "4.1. Dual Utility Framework ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
* J. B. Conway (2019)
  A course in functional analysis.
  Vol. 96, Springer.
  Cited by: [§A.2](https://arxiv.org/html/2602.09967v1#A1.SS2.p4.1 "A.2. Functional-Analytic Background ‣ Appendix A Mathematical Background ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
* J. Diestel and J. Uhl (1977)
  Vector measures.
  Mathematical Surveys, Vol. 15, American Mathematical Society, Providence, RI.
  Cited by: [§A.3](https://arxiv.org/html/2602.09967v1#A1.SS3.1.p1.1 "Proof. ‣ A.3. Separation and Duality ‣ Appendix A Mathematical Background ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"),
  [Remark A.15](https://arxiv.org/html/2602.09967v1#A1.Thmtheorem15.p1.2.2 "Remark A.15. ‣ A.3. Separation and Duality ‣ Appendix A Mathematical Background ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"),
  [Remark A.5](https://arxiv.org/html/2602.09967v1#A1.Thmtheorem5.p1.5.5 "Remark A.5. ‣ A.1. Bochner Integrability ‣ Appendix A Mathematical Background ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
* A. Gershkov, B. Moldovanu, P. Strack, and M. Zhang (2023)
  Optimal insurance: dual utility, random losses, and adverse selection.
  American Economic Review 113 (10),  pp. 2581–2614.
  Cited by: [§1](https://arxiv.org/html/2602.09967v1#S1.p3.1 "1. Introduction ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"),
  [§1](https://arxiv.org/html/2602.09967v1#S1.p8.1 "1. Introduction ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"),
  [§4.5](https://arxiv.org/html/2602.09967v1#S4.SS5.p5.4 "4.5. Properties of the Optimal Menu ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"),
  [§4.5](https://arxiv.org/html/2602.09967v1#S4.SS5.p6.3 "4.5. Properties of the Optimal Menu ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
* M. Ghossoub and X. D. He (2021)
  Comparative risk aversion in rdeu with applications to optimal underwriting of securities issuance.
  Insurance: Mathematics and Economics 101,  pp. 6–22.
  Cited by: [§4.1](https://arxiv.org/html/2602.09967v1#S4.SS1.p3.8 "4.1. Dual Utility Framework ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
* M. Ghossoub, B. Li, and B. Shi (2025)
  Optimal insurance in a monopoly: dual utilities with hidden risk attitudes.
  arXiv preprint arXiv:2504.01095.
  Cited by: [§1](https://arxiv.org/html/2602.09967v1#S1.p3.1 "1. Introduction ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"),
  [§1](https://arxiv.org/html/2602.09967v1#S1.p4.1 "1. Introduction ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"),
  [§1](https://arxiv.org/html/2602.09967v1#S1.p5.4 "1. Introduction ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"),
  [§1](https://arxiv.org/html/2602.09967v1#S1.p8.1 "1. Introduction ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"),
  [§3](https://arxiv.org/html/2602.09967v1#S3.p1.1 "3. Efficiency under asymmetric information ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"),
  [§4.5](https://arxiv.org/html/2602.09967v1#S4.SS5.p5.4 "4.5. Properties of the Optimal Menu ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"),
  [§4.5](https://arxiv.org/html/2602.09967v1#S4.SS5.p6.3 "4.5. Properties of the Optimal Menu ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
* B. Holmström (1979)
  Moral hazard and observability.
  The Bell journal of economics,  pp. 74–91.
  Cited by: [§1](https://arxiv.org/html/2602.09967v1#S1.p2.1 "1. Introduction ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
* B. Jerez (2003)
  A dual characterization of incentive efficiency.
  Journal of Economic Theory 112 (1),  pp. 1–34.
  Cited by: [§1](https://arxiv.org/html/2602.09967v1#S1.p4.1 "1. Introduction ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
* V. L. Klee (1951)
  Convex sets in linear spaces.
  Cited by: [§A.3](https://arxiv.org/html/2602.09967v1#A1.SS3.p1.2 "A.3. Separation and Duality ‣ Appendix A Mathematical Background ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
* J. M. Marshall (1976)
  Moral hazard.
  The American Economic Review 66 (5),  pp. 880–890.
  Cited by: [§1](https://arxiv.org/html/2602.09967v1#S1.p2.1 "1. Introduction ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
* P. Milgrom and I. Segal (2002)
  Envelope theorems for arbitrary choice sets.
  Econometrica 70 (2),  pp. 583–601.
  Cited by: [§B.4](https://arxiv.org/html/2602.09967v1#A2.SS4.p5.3 "B.4. Proof of Proposition 4.10 ‣ Appendix B Proofs of Main Results ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
* M. V. Pauly (1978)
  Overinsurance and public provision of insurance: the roles of moral hazard and adverse selection.
  In Uncertainty in economics,
   pp. 307–331.
  Cited by: [§1](https://arxiv.org/html/2602.09967v1#S1.p2.1 "1. Introduction ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
* E. C. Prescott and R. M. Townsend (1984)
  Pareto optima and competitive equilibria with adverse selection and moral hazard.
  Econometrica: journal of the econometric society,  pp. 21–45.
  Cited by: [§1](https://arxiv.org/html/2602.09967v1#S1.p4.1 "1. Introduction ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
* J. Quiggin (1993)
  Generalized expected utility theory: the rank-dependent model.
   Springer Science & Business Media.
  Cited by: [§4.1](https://arxiv.org/html/2602.09967v1#S4.SS1.p2.3 "4.1. Dual Utility Framework ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"),
  [§4.1](https://arxiv.org/html/2602.09967v1#S4.SS1.p3.8 "4.1. Dual Utility Framework ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
* M. Rothschild and J. E. Stiglitz (1976)
  Equilibrium in competitive insurance markets: an essay on the economics of imperfect information.
  Cited by: [§1](https://arxiv.org/html/2602.09967v1#S1.p3.1 "1. Introduction ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
* S. Shavell (1979)
  On moral hazard and insurance.
  The quarterly journal of economics 93 (4),  pp. 541–562.
  Cited by: [§1](https://arxiv.org/html/2602.09967v1#S1.p2.1 "1. Introduction ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
* M. Spence and R. Zeckhauser (1978)
  Insurance, information, and individual action.
  In Uncertainty in economics,
   pp. 333–343.
  Cited by: [§1](https://arxiv.org/html/2602.09967v1#S1.p2.1 "1. Introduction ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
* J. E. Stiglitz (1977)
  Monopoly, non-linear pricing and imperfect information: the insurance market.
  The Review of Economic Studies 44 (3),  pp. 407–430.
  Cited by: [§1](https://arxiv.org/html/2602.09967v1#S1.p3.1 "1. Introduction ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
* R. M. Townsend (1979)
  Optimal contracts and competitive markets with costly state verification.
  Journal of Economic theory 21 (2),  pp. 265–293.
  Cited by: [§1](https://arxiv.org/html/2602.09967v1#S1.p2.1 "1. Introduction ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").
* M. E. Yaari (1987)
  The dual theory of choice under risk.
  Econometrica: Journal of the Econometric Society,  pp. 95–115.
  Cited by: [§1](https://arxiv.org/html/2602.09967v1#S1.p3.1 "1. Introduction ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"),
  [§4.1](https://arxiv.org/html/2602.09967v1#S4.SS1.p1.1 "4.1. Dual Utility Framework ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection"),
  [§4.1](https://arxiv.org/html/2602.09967v1#S4.SS1.p2.3 "4.1. Dual Utility Framework ‣ 4. The Case of Dual Utilities ‣ Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection").