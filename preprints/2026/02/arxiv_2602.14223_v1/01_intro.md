---
authors:
- Tim J. Boonen
- Kenneth Tsz Hin Ng
- Tak Wa Ng
- Thai Nguyen
doc_id: arxiv:2602.14223v1
family_id: arxiv:2602.14223
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance
url_abs: http://arxiv.org/abs/2602.14223v1
url_html: https://arxiv.org/html/2602.14223v1
venue: arXiv q-fin
version: 1
year: 2026
---


Tim J. Boonen Kenneth Tsz Hin Ng  Tak Wa Ng  Thai Nguyen
Department of Statistics and Actuarial Science, School of Computing and Data Science, The University of Hong Kong, Hong Kong; Email: tjboonen@hku.hkDepartment of Mathematics, The Ohio State University, Columbus, United States; Email: ng.499@osu.eduÉcole d’Actuariat, Université Laval, Quebec, Canada; Email: tak-wa.ng.1@ulaval.caÉcole d’Actuariat, Université Laval, Quebec, Canada; Email: thai.nguyen@act.ulaval.ca

###### Abstract

We propose a peer-to-peer (P2P) insurance scheme comprising a risk-sharing pool and a reinsurer. A plan manager determines how risks are allocated among members and ceded to the reinsurer, while the reinsurer sets the reinsurance loading. Our work focuses on the strategic interaction between the plan manager and the reinsurer, and this focus leads to two game-theoretic contract designs: a Pareto design and a Bowley design, for which we derive closed-form optimal contracts. In the Pareto design, cooperation between the reinsurer and the plan manager leads to multiple Pareto-optimal contracts, which are further refined by introducing the notion of coalitional stability. In contrast, the Bowley design yields a unique optimal contract through a leader–follower framework, and we provide a rigorous verification of the individual rationality constraints via pointwise comparisons of payoff vectors. Comparing the two designs, we prove that the Bowley-optimal contract is never Pareto optimal and typically yields lower total welfare.
In our numerical examples, the presence of reinsurance improves welfare, especially with Pareto designs and a less risk-averse reinsurer.
We further analyze the impact of the single-loading restriction, which disproportionately favors members with riskier losses.

Keywords:
Risk management,
Peer-to-peer risk sharing,
Optimal reinsurance,
Pareto optimality,
Cooperative game theory.

JEL Classification: C71, C72, G22

## 1 Introduction

Decentralized insurance arrangements, such as peer-to-peer (P2P) insurance (Denuit, [2020](https://arxiv.org/html/2602.14223v1#bib.bib15 "Investing in your own and peers’ risks: the simple analytics of P2P insurance"); Feng, [2023](https://arxiv.org/html/2602.14223v1#bib.bib4 "Decentralized insurance")), mutual insurance (Laux and Muermann, [2010](https://arxiv.org/html/2602.14223v1#bib.bib3 "Financing risk transfer under governance problems: mutual versus stock insurers"); Li et al., [2025](https://arxiv.org/html/2602.14223v1#bib.bib49 "Mean field analysis of mutual insurance market")), and tontines (Milevsky and Salisbury, [2015](https://arxiv.org/html/2602.14223v1#bib.bib5 "Optimal retirement income tontines"); Ng and Nguyen, [2025a](https://arxiv.org/html/2602.14223v1#bib.bib98 "Individual survivor fund account: the impact of bequest motives on tontine participation")), have attracted increasing attention as alternatives to traditional centralized insurance models (e.g., Boonen et al., [2024](https://arxiv.org/html/2602.14223v1#bib.bib41 "Pareto-efficient risk sharing in centralized insurance markets with application to flood risk")). By allowing members to share risks within a community directly, these schemes promise improved transparency, reduced administrative costs, and better alignment of incentives. In particular, many P2P insurance schemes incorporate an external reinsurance layer to enhance risk coverage and ensure solvency, leading to hybrid designs that combine internal risk sharing with external risk transfer.
For example, Denuit and Robert ([2021b](https://arxiv.org/html/2602.14223v1#bib.bib64 "Stop-loss protection for a large P2P insurance pool"))
study
the stop-loss treaty in P2P insurance in which the retained part is shared by the conditional mean risk-sharing rule (Denuit and Dhaene, [2012](https://arxiv.org/html/2602.14223v1#bib.bib82 "Convex order and comonotonic conditional mean risk sharing")). Anthropelos et al. ([2026](https://arxiv.org/html/2602.14223v1#bib.bib99 "On the expansion of risk pooling")) consider the expansion of risk-sharing pools and examine the impact of exogenous reinsurance.
However, to our knowledge, the literature on the strategic interaction between a reinsurer and a decentralized P2P pool remains largely unexplored.

Understanding this interaction is important because, in practice, reinsurers are not passive risk absorbers but strategic market participants who price coverage and influence the feasibility of P2P schemes. Whether the reinsurer acts as a price-setting leader or engages in coordinated contract design directly affects equilibrium risk allocation, premium levels, and the long-run sustainability of decentralized insurance pools. Accordingly, the present paper focuses on this strategic interaction and its implications for all stakeholders in the P2P insurance scheme.

### 1.1 Contributions

This paper considers a novel mean-variance P2P insurance-reinsurance scheme comprising a risk-sharing pool managed by a plan manager and a reinsurer that provides external insurance protection to the pool.
In this scheme, the P2P plan manager decides the internal risk mutualization among members and external risk transfer to the reinsurer, while the reinsurer sets the price of the reinsurance contract under the expected value premium principle. Depending on the interaction between the reinsurer and the plan manager, we consider two institutional designs: the Pareto and the Bowley models.

In the Pareto design, the reinsurer and the P2P plan manager optimize their joint interests, which we term a joint-Pareto-optimal (JP-optimal) contract. Following the two-step approach described in Asimit et al. ([2021](https://arxiv.org/html/2602.14223v1#bib.bib8 "Risk sharing with multiple indemnity environments"), Section 2), we determine the risk mutualization between members and the reinsurer via a
social-objective optimization. Since the price of the reinsurance contract cancels out when aggregating the members’ and the reinsurer’s disutility, the optimal risk-mutualization and reinsurance strategy is independent of the price of the reinsurance contract,
which gives rise to multiple JP-optimal contracts due to the flexibility to choose the reinsurance premium. This freedom permits additional selection criteria within the JP-optimal set based on coalitional stability considerations.
Specifically, we study the premium decision via a coalition game that assigns to each agent111In this paper, we refer to “members” as participants in the risk-sharing pool, and to “agents” as all individuals, including both members and the reinsurer. the welfare gain from joining the P2P contract. We prove that the core is non-empty and that its elements correspond to coalitionally stable and JP-optimal contracts. Furthermore, we derive sufficient conditions for contracts with nonnegative safety loadings, and in particular for contracts with a single common safety loading.

The Bowley design is formulated as a leader–follower game, in which the reinsurer acts as the leader and sets the reinsurance premium, while the plan manager responds by determining the reinsurance and internal risk-sharing strategies for the members. By backward induction and solving the two subproblems sequentially, we derive the unique Bowley-optimal contract in closed form, both with and without the single-loading restriction. Unlike the Pareto design, the reinsurance premium in the Bowley framework is uniquely determined,
but the individual rationality (IR) constraints are not immediately satisfied. We therefore provide explicit closed-form conditions on the market parameters that ensure the IR constraints are satisfied.
Finally, by comparing the two game-theoretic designs, we show that the Bowley contract is never JP-optimal and always results in lower total welfare for all agents.

Through a comprehensive numerical analysis, we compare
various contracts
and investigate their impacts on welfare. Owing to the multiplicity of admissible safety loadings under the Pareto design, we select JP-optimal contracts that
Pareto-dominate the Bowley counterparts.
The numerical comparison of all contracts yields four key insights.
First, Pareto and Bowley contracts dominate the no-reinsurance case in terms of each agent’s welfare improvement. This underscores the value of the reinsurance layer, aligning with the finding in Anthropelos et al. ([2026](https://arxiv.org/html/2602.14223v1#bib.bib99 "On the expansion of risk pooling")) despite different settings and research questions.

Second, the Pareto design generally leads to
lower safety loadings and higher risk transfers for all members, and the combined effect leads to a higher premium payment.
From the reinsurer’s perspective, the additional risk borne under the Pareto contracts is well-compensated by the increased premium income,
resulting in higher welfare for all agents in the community.

Third,
we find that the single-loading restriction primarily benefits members with riskier losses, as they are typically charged lower safety loadings than in the unrestricted case. As a result,
the high-risk member may receive a disproportionately large welfare gain
at the expense of other members and the reinsurer. Nonetheless, this does not necessarily reduce total welfare relative to contracts without the restriction: with a less risk-averse reinsurer, Bowley contracts with the single-loading restriction achieve a larger total welfare improvement.

Finally, through
comparative statics analysis of the reinsurer’s risk aversion, we find that without the single-loading restriction, Bowley-optimal contracts exhibit underinsurance compared to JP-optimal cases, echoing the results in Jiang et al. ([2025](https://arxiv.org/html/2602.14223v1#bib.bib12 "Bowley solution of a variance game in insurance")). In addition, the welfare improvement depends on the reinsurer’s risk tolerance: when she
is less risk averse and thus more risk is transferred from the pool, a greater increase in total welfare results.

### 1.2 Related Literature

Our work contributes to the literature on decentralized insurance.
This strand of research has followed several representative directions, such as the construction of risk-sharing architectures through, among others, axiomatic characterizations (Denuit et al., [2022](https://arxiv.org/html/2602.14223v1#bib.bib79 "Risk-sharing rules and their properties, with applications to peer-to-peer insurance")) and optimization-based approaches (Abdikerimova and Feng, [2022](https://arxiv.org/html/2602.14223v1#bib.bib73 "Peer-to-peer multi-risk insurance and mutual aid")). Other contributions from insurance economics examine issues such as adverse selection (Chen et al., [2024](https://arxiv.org/html/2602.14223v1#bib.bib40 "Cost-effectiveness, fairness and adverse selection in mutual aid")) and moral hazard (Boonen et al., [2025](https://arxiv.org/html/2602.14223v1#bib.bib21 "Contractibility, peer-to-peer insurance, and moral hazard")), as well as institutional design aspects. For example, Denuit and Robert ([2021a](https://arxiv.org/html/2602.14223v1#bib.bib14 "Risk sharing under the dominant peer-to-peer property and casualty insurance business models")) propose three business models with different governance, and Clemente et al. ([2023](https://arxiv.org/html/2602.14223v1#bib.bib34 "Optimal cashback in a cooperative framework for peer-to-peer insurance coverages")) design a novel cashback mechanism based on the Shapley value. In particular, our paper devises a new P2P insurance scheme featuring a proportional risk mutualization similar to that in Feng et al. ([2023](https://arxiv.org/html/2602.14223v1#bib.bib91 "Peer-to-peer risk sharing with an application to flood risk pooling")) and an additional proportional reinsurance treaty.
Unlike Denuit and Robert ([2021b](https://arxiv.org/html/2602.14223v1#bib.bib64 "Stop-loss protection for a large P2P insurance pool")) and Anthropelos et al. ([2026](https://arxiv.org/html/2602.14223v1#bib.bib99 "On the expansion of risk pooling")), who assume that the reinsurance layer is exogenously offered, the novelty of this paper lies in incorporating the reinsurer’s perspective and modeling her strategic interaction with the P2P insurance manager in setting the reinsurance premium, which fundamentally shapes equilibrium risk sharing
and welfare outcomes.

Besides, our Pareto and Bowley reinsurance games connect the literature on decentralized insurance to game-theoretic (re)insurance contracting.222The literature review focuses on (re)insurance contracting under Pareto and Bowley games. For a more comprehensive review of reinsurance contracting, we refer to Cai and Chi ([2020](https://arxiv.org/html/2602.14223v1#bib.bib42 "Optimal reinsurance designs based on risk measures: a review")). In Pareto-optimal (re)insurance arrangements, there are mainly two categories related to premium setting. In the first category, the contract is composed via a weighted-sum optimization with a given premium function. For instance, Cai et al. ([2017](https://arxiv.org/html/2602.14223v1#bib.bib23 "Pareto-optimal reinsurance arrangements under general model settings")) develop a mutually acceptable Pareto-optimal reinsurance contract that accommodates both the reinsurer and the insurer’s goals. Lo and Tang ([2019](https://arxiv.org/html/2602.14223v1#bib.bib33 "Pareto-optimal reinsurance policies in the presence of individual risk constraints")) further extend their work to incorporate risk constraints.

Another category endogenizes the premium decision in the bargaining process among agents, which is in line with the seminal contribution of Raviv ([1979](https://arxiv.org/html/2602.14223v1#bib.bib6 "The design of an optimal insurance policy")).
Methodologically, this approach first optimizes the total welfare to determine the optimal indemnity, and then redistributes the resulting welfare gain among agents via a cooperative game to set the premium. Our Pareto design features a cooperative game study on premium decision, further advancing this line of research in the P2P insurance setting.
To name a few contributions in this spirit, Asimit and Boonen ([2018](https://arxiv.org/html/2602.14223v1#bib.bib7 "Insurance with multiple insurers: a game-theoretic approach")) study Pareto-efficient insurance contracts with one policyholder and multiple insurers, which is further examined in Boonen and Jiang ([2025](https://arxiv.org/html/2602.14223v1#bib.bib36 "Pareto-optimal insurance under robust distortion risk measures")) with distributional uncertainty of the insurable loss. Boonen et al. ([2024](https://arxiv.org/html/2602.14223v1#bib.bib41 "Pareto-efficient risk sharing in centralized insurance markets with application to flood risk")) explore the risk sharing between one monopolistic insurer and multiple policyholders with applications in flood risk management. Our Pareto design adds a risk-mutualization layer to the setting of Boonen et al. ([2024](https://arxiv.org/html/2602.14223v1#bib.bib41 "Pareto-efficient risk sharing in centralized insurance markets with application to flood risk")). Therein, the core of the insurance game exists trivially since the insurer serves as the veto player who establishes the risk-sharing scheme. In contrast, in our model, the risk-sharing scheme can operate even without the reinsurer’s involvement. Therefore, our work contributes by
providing a nontrivial proof of the non-emptiness of the resulting core (Gillies, [1953](https://arxiv.org/html/2602.14223v1#bib.bib25 "Some theorems on n-person games")).

The leader–follower framework is another key model in (re)insurance contracting. In the continuous-time setting, Chen and Shen ([2018](https://arxiv.org/html/2602.14223v1#bib.bib16 "On a new paradigm of optimal reinsurance: a stochastic Stackelberg differential game between an insurer and a reinsurer")) study such a reinsurance game under the expected utility maximization criterion, which is further extended to the settings of ambiguous claim arrival (Hu et al., [2018](https://arxiv.org/html/2602.14223v1#bib.bib35 "Robust reinsurance contracts with uncertainty about jump risk")), multiple competitive followers with relative performance concern (Bai et al., [2022](https://arxiv.org/html/2602.14223v1#bib.bib31 "A hybrid stochastic differential reinsurance and investment game with bounded memory")), and multiple leaders with different premium principles (Cao et al., [2023](https://arxiv.org/html/2602.14223v1#bib.bib43 "Reinsurance games with two reinsurers: tree versus chain")).

The Bowley reinsurance game considered herein belongs to the same leader-follower framework, featuring a monopolistic reinsurer in a discrete-time setting. The seminal work of this stream dates back to the study in Chan and Gerber ([1985](https://arxiv.org/html/2602.14223v1#bib.bib9 "The reinsurer’s monopoly and the Bowley solution")) under the expected utility setting. Cheung et al. ([2019](https://arxiv.org/html/2602.14223v1#bib.bib10 "Risk-adjusted Bowley reinsurance under distorted probabilities")) revisit the problem under a general premium principle for the reinsurer and use a distortion risk measure for the insurer. In addition, Boonen and Ghossoub ([2023](https://arxiv.org/html/2602.14223v1#bib.bib11 "Bowley vs. Pareto optima in reinsurance contracting")) compare Pareto and Bowley-optimal reinsurance designs. They find that the Bowley optimum can be Pareto efficient but leaves the insurer’s welfare indifferent to the status quo. However, the Bowley optimum is not necessarily Pareto optimal:
Jiang et al. ([2025](https://arxiv.org/html/2602.14223v1#bib.bib12 "Bowley solution of a variance game in insurance")) also make such a comparison under the generalized mean-variance preference setting and prove the inefficiency
of Bowley-optimal contracts. Our result echoes this finding in the literature on P2P insurance design and suggests caution regarding the adoption of the Bowley reinsurance scheme.

The remainder of the paper is organized as follows. Section [2](https://arxiv.org/html/2602.14223v1#S2 "2 Model Formulations ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") formulates the general model setting. Pareto and Bowley designs are introduced in Section [3](https://arxiv.org/html/2602.14223v1#S3 "3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") and Section [4](https://arxiv.org/html/2602.14223v1#S4 "4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"), respectively. Section [5](https://arxiv.org/html/2602.14223v1#S5 "5 Numerical Illustration and Welfare Analysis ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") numerically illustrates two designs and performs a welfare analysis. We conclude the paper in Section [6](https://arxiv.org/html/2602.14223v1#S6 "6 Conclusion ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") with future research directions. Most proofs and additional exposition are relegated to the Appendix.

## 2 Model Formulations

### 2.1 Basic setting and risk sharing

We consider a pool of n≥2n\geq 2 members who share individual-specific losses 𝑿=(X1,…,Xn)\bm{X}=(X\_{1},\dots,X\_{n}), where XiX\_{i} represents the loss random variable of the Member ii. Denote the mean and the positive definite covariance matrix of 𝑿\bm{X} by 𝝁=(μ1,…,μn)\bm{\mu}=(\mu\_{1},\dots,\mu\_{n}) and 𝚺=(σi​j)i,j=1,…,n\bm{\Sigma}=(\sigma\_{ij})\_{i,j=1,\dots,n}, respectively, where μi,σi​i>0{\mu\_{i}},\sigma\_{ii}>0 for any i=1,…,ni=1,\dots,n.
In the sequel, unless otherwise specified, we use bold symbols to denote vectors or matrices; and unbolded symbols to denote scalars.

A plan manager oversees the risk management strategies of the pool, which consist of two main components:

1. 1.

   Reinsurance. The plan manager decides the proportional reinsurance strategy 𝒑=(p1,…,pn)\bm{p}=(p\_{1},\dots,p\_{n}), which transfers the risk 𝑿\bm{X} partially to a reinsurer.333We use the term “reinsurer” to distinguish it from the P2P plan manager. Such contracts can also be offered by insurers.  In return, each member ii pays a premium πi\pi\_{i} for the reinsurance policy. We assume that the expected value premium principle is adopted:

   |  |  |  |
   | --- | --- | --- |
   |  | πi​(ηi,pi):=(1+ηi)​𝔼​(pi​Xi)=(1+ηi)​pi​μi,\pi\_{i}(\eta\_{i},p\_{i}):=(1+\eta\_{i})\mathbb{E}(p\_{i}X\_{i})=(1+\eta\_{i})p\_{i}\mu\_{i}, |  |

   where ηi≥0\eta\_{i}\geq 0 is the safety loading.
2. 2.

   Risk mutualization. The plan manager also determines the risk mutualization rule 𝑨=(ai​j)i,j∈{1,…,n}\bm{A}=(a\_{ij})\_{i,j\in\{1,\dots,n\}} on how losses are shared among members of the pool, where ai​ja\_{ij} represents the portion of member jj’s loss, ai​j​Xja\_{ij}X\_{j}, which is borne by Member ii ex post.

Summarizing the above, Member ii has to pay πi​(ηi,pi)\pi\_{i}(\eta\_{i},p\_{i}) to cede pi​Xip\_{i}X\_{i} to the reinsurer, and has to bear ∑j=1nai​j​Xj\sum\_{j=1}^{n}a\_{ij}X\_{j} from other members and herself.
The mechanism is graphically illustrated in Fig. [1](https://arxiv.org/html/2602.14223v1#S2.F1 "Figure 1 ‣ 2.1 Basic setting and risk sharing ‣ 2 Model Formulations ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").

Member iiMember jj⋯\cdotsReinsureraj​i​Xia\_{ji}X\_{i}ai​j​Xja\_{ij}X\_{j}ai​i​Xia\_{ii}X\_{i}\,aj​j​Xj\,a\_{jj}X\_{j}pi​Xip\_{i}X\_{i}\,pj​Xj\,p\_{j}X\_{j}


Figure 1: Illustration of the risk management mechanism.

The risk-sharing scheme herein adds an additional reinsurance layer to the P2P risk mutualization introduced in Feng et al. ([2023](https://arxiv.org/html/2602.14223v1#bib.bib91 "Peer-to-peer risk sharing with an application to flood risk pooling")). Motivated by their work, we formulate the zero-conserving condition and actuarial fairness for our mechanism as follows.

###### Definition 2.1 (Zero conserving).

The risk-mutualization-reinsurance rule (𝐀,𝐩)(\bm{A},\bm{p}) is said to be zero conserving if all losses are shared completely among members and the reinsurer. Mathematically, pi+∑j=1naj​i=1p\_{i}+\sum\_{j=1}^{n}a\_{ji}=1 for all i=1,…,ni=1,\dots,n.
The condition can be equivalently expressed as 𝟏⊤​𝐀+𝐩⊤=𝟏⊤\mathbf{1}^{\top}\bm{A}+\bm{p}^{\top}=\bm{1}^{\top}, where 𝟏∈ℝn\bm{1}\in\mathbb{R}^{n} is the vector with all entries being 1.

###### Definition 2.2 (Actuarial fairness).

The risk-mutualization-reinsurance rule (𝐀,𝐩)(\bm{A},\bm{p}) is said to be actuarially fair if the post-reinsurance expected loss is preserved before and after risk mutualization for all members in the pool. Mathematically, ∑j=1nai​j​μj=(1−pi)​μi\sum\_{j=1}^{n}a\_{ij}\mu\_{j}=(1-p\_{i})\mu\_{i} for all i=1,…,ni=1,\dots,n.
Equivalently, the condition can be expressed as 𝐀​𝛍+𝐃​(𝛍)​𝐩=𝛍\bm{A}\bm{\mu}+\bm{D}(\bm{\mu})\bm{p}=\bm{\mu}, where 𝐃\bm{D} is the operator that transforms an nn-dimensional vector to an n×nn\times n diagonal matrix.

On the other hand, the reinsurer (indexed by RR in the sequel) shall determine the safety loadings 𝜼=(η1,…,ηn)\bm{\eta}=(\eta\_{1},\dots,\eta\_{n}) charged to the members based on the collective risk exposure. The total premium collected by the reinsurer is thus ∑i=1nπi​(ηi,pi)=(𝑫​(𝝁)​(𝟏+𝜼))⊤​𝒑\sum\_{i=1}^{n}\pi\_{i}(\eta\_{i},p\_{i})=(\bm{D}(\bm{\mu})(\bm{1}+\bm{\eta}))^{\top}\bm{p}.
Here, we assume that the reinsurer can charge members differently based on their individual risks. We collect the notions of risk sharing among members, reinsurance, and safety loading to define the P2P insurance contract below.

###### Definition 2.3 (P2P insurance contract).

A triplet (𝐀,𝐩,𝛈)(\bm{A},\bm{p},\bm{\eta}) is called a P2P insurance contract, where 𝐀\bm{A} is the risk mutualization among members, 𝐩\bm{p} is the proportional reinsurance strategy, and 𝛈\bm{\eta} is the safety loading factor.

### 2.2 Agents’ preferences

We introduce the preferences of each individual member, the plan manager, and the reinsurer as follows. The risk borne by each member is measured by a mean-variance disutility based on the risk mutualization arrangement:

|  |  |  |
| --- | --- | --- |
|  | ρi​(𝑨):=∑j=1n𝔼​(ai​j​Xj)+γi2​V​a​r​(∑j=1nai​j​Xj)=𝑨i​𝝁+γi2​𝑨i​𝚺​𝑨i⊤,for all ​i=1,⋯,n,\rho\_{i}(\bm{A}):=\sum\_{j=1}^{n}\mathbb{E}(a\_{ij}X\_{j})+\frac{\gamma\_{i}}{2}Var\left(\sum\_{j=1}^{n}a\_{ij}X\_{j}\right)=\bm{A}\_{i}\bm{\mu}+\frac{\gamma\_{i}}{2}\bm{A}\_{i}\bm{\Sigma}\bm{A}\_{i}^{\top},\quad\text{for all }i=1,\cdots,n, |  |

where 𝑨i\bm{A}\_{i} is the ii-th row of 𝑨\bm{A}
and γi>0\gamma\_{i}>0 captures the heterogeneous risk aversion of Member ii. Together with the premium paid to the reinsurer for the reinsurance policy, πi​(ηi,pi)\pi\_{i}(\eta\_{i},p\_{i}), the preference for the ii-th member is given by ui​(𝑨,𝒑,𝜼):=ρi​(𝑨)+πi​(ηi,pi)u\_{i}(\bm{A},\bm{p},\bm{\eta}):=\rho\_{i}(\bm{A})+\pi\_{i}(\eta\_{i},p\_{i}).
The plan manager’s preference is then given by the sum of the members’ preferences:

|  |  |  |
| --- | --- | --- |
|  | u​(𝑨,𝒑,𝜼):=∑i=1nui​(𝑨,𝒑,𝜼)=𝟏⊤​𝑨​𝝁+12​t​r​(𝑫​(𝜸)​𝑨​𝚺​𝑨⊤)+(𝑫​(𝝁)​(𝟏+𝜼))⊤​𝒑,u(\bm{A},\bm{p},\bm{\eta}):=\sum\_{i=1}^{n}u\_{i}(\bm{A},\bm{p},\bm{\eta})=\bm{1}^{\top}\bm{A}\bm{\mu}+\frac{1}{2}tr(\bm{D}(\bm{\gamma})\bm{A}\bm{\Sigma}\bm{A}^{\top})+(\bm{D}(\bm{\mu})(\bm{1}+\bm{\eta}))^{\top}\bm{p}, |  |

where t​r​(⋅)tr(\cdot) is the trace operator.

The reinsurer aims to maximize the profit while controlling the risk taken. The former is given by ∑i=1nπi​(ηi,pi)\sum\_{i=1}^{n}\pi\_{i}(\eta\_{i},p\_{i}), while the latter is measured by the mean-variance disutility:

|  |  |  |
| --- | --- | --- |
|  | ρR​(𝒑):=𝔼​(∑i=1npi​Xi)+γR2​V​a​r​(∑i=1npi​Xi)=𝝁⊤​𝒑+γR2​𝒑⊤​𝚺​𝒑,\rho\_{R}(\bm{p}):=\mathbb{E}\left(\sum\_{i=1}^{n}p\_{i}X\_{i}\right)+\frac{\gamma\_{R}}{2}Var\left(\sum\_{i=1}^{n}p\_{i}X\_{i}\right)=\bm{\mu}^{\top}\bm{p}+\frac{\gamma\_{R}}{2}\bm{p}^{\top}\bm{\Sigma}\bm{p}, |  |

where γR≥0\gamma\_{R}\geq 0 captures the reinsurer’s risk aversion, with a larger γR\gamma\_{R} signifying that the reinsurer is more risk averse. The reinsurer’s preference is thus given by the sum of the two components:

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(𝜼,𝒑):=ρR​(𝒑)−∑i=1nπi​(ηi,pi)=γR2​𝒑⊤​𝚺​𝒑−(𝑫​(𝝁)​𝜼)⊤​𝒑.v(\bm{\eta},\bm{p}):=\rho\_{R}(\bm{p})-\sum\_{i=1}^{n}\pi\_{i}(\eta\_{i},p\_{i})=\frac{\gamma\_{R}}{2}\bm{p}^{\top}\bm{\Sigma}\bm{p}-(\bm{D}(\bm{\mu})\bm{\eta})^{\top}\bm{p}. |  | (1) |

### 2.3 Individual rationality

The individual rationality (IR) constraint is a set of conditions that must be satisfied so that all agents (members and the reinsurer) are better off than under the status quo, thereby incentivizing them to join the risk-sharing scheme. For members in the pool, we define the welfare gain ωi\omega\_{i} for Member ii by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ωi​(𝑨,𝒑,𝜼):=μi+γi2​σi2−ui​(𝑨,𝒑,𝜼)=γi2​(σi2−𝑨i​𝚺​𝑨i⊤)−ηi​pi​μi,i=1,…,n,\omega\_{i}(\bm{A},\bm{p},\bm{\eta}):=\mu\_{i}+\frac{\gamma\_{i}}{2}\sigma\_{i}^{2}-u\_{i}(\bm{A},\bm{p},\bm{\eta})=\frac{\gamma\_{i}}{2}(\sigma\_{i}^{2}-\bm{A}\_{i}\bm{\Sigma}\bm{A}\_{i}^{\top})-\eta\_{i}p\_{i}\mu\_{i},\quad i=1,\dots,n, |  | (2) |

where the second equality follows from the actuarial fairness condition.
This represents the reduction in the member’s disutility after joining the pool. The IR constraints for the members are then given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ωi​(𝑨,𝒑,𝜼)≥0⇔ηi​pi​μi≤γi2​(σi2−𝑨i​𝚺​𝑨i⊤),for all ​i=1,…,n.\omega\_{i}(\bm{A},\bm{p},\bm{\eta})\geq 0\iff\eta\_{i}p\_{i}\mu\_{i}\leq\frac{\gamma\_{i}}{2}(\sigma\_{i}^{2}-\bm{A}\_{i}\bm{\Sigma}\bm{A}\_{i}^{\top}),\quad\text{for all }i=1,\dots,n. |  | (3) |

The reinsurer’s welfare gain can be formulated similarly as

|  |  |  |
| --- | --- | --- |
|  | ωR​(𝑨,𝒑,𝜼):=−v​(𝒑,𝜼)=(𝑫​(𝝁)​𝜼)⊤​𝒑−γR2​𝒑⊤​𝚺​𝒑,\omega\_{R}(\bm{A},\bm{p},\bm{\eta}):=-v(\bm{p},\bm{\eta})=(\bm{D}(\bm{\mu})\bm{\eta})^{\top}\bm{p}-\frac{\gamma\_{R}}{2}\bm{p}^{\top}\bm{\Sigma}\bm{p}, |  |

which again measures the reduction in disutility upon forming the risk-sharing scheme. The IR constraint for the reinsurer is thus

|  |  |  |  |
| --- | --- | --- | --- |
|  | ωR​(𝑨,𝒑,𝜼)≥0⇔γR2​𝒑⊤​𝚺​𝒑≤(𝑫​(𝝁)​𝜼)⊤​𝒑.\omega\_{R}(\bm{A},\bm{p},\bm{\eta})\geq 0\iff\frac{\gamma\_{R}}{2}\bm{p}^{\top}\bm{\Sigma}\bm{p}\leq(\bm{D}(\bm{\mu})\bm{\eta})^{\top}\bm{p}. |  | (4) |

In the sequel, we denote by ℐ​ℛ\mathcal{IR} the set of all contracts (𝑨,𝒑,𝜼)(\bm{A},\bm{p},\bm{\eta}) that satisfy constraints ([3](https://arxiv.org/html/2602.14223v1#S2.E3 "In 2.3 Individual rationality ‣ 2 Model Formulations ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) and ([4](https://arxiv.org/html/2602.14223v1#S2.E4 "In 2.3 Individual rationality ‣ 2 Model Formulations ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")).

## 3 Pareto Design

In this section, we consider the situation in which the reinsurer and the plan manager cooperate on the risk-sharing scheme, thereby leading to a Pareto game. We use the term Joint-Pareto (JP) optimality to distinguish it from Pareto optimality in Definition [4.1](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem1 "Definition 4.1 (Pareto-optimal risk allocation). ‣ 4.1.1 Plan manager’s follower problem ‣ 4.1 Problem formulation ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") below.

###### Definition 3.1.

[Joint-Pareto-optimal P2P insurance contract]
A contract (𝐀,𝐩,𝛈)(\bm{A},\bm{p},\bm{\eta}) is called Joint-Pareto optimal if (𝐀,𝐩,𝛈)∈ℐ​ℛ(\bm{A},\bm{p},\bm{\eta})\in\mathcal{IR}, and no (𝐀~,𝐩~,𝛈~)∈ℐ​ℛ(\bm{\tilde{A}},\bm{\tilde{p}},\bm{\tilde{\eta}}){\in\mathcal{IR}} satisfies v​(𝛈~,𝐩~)≤v​(𝛈,𝐩)v(\bm{\tilde{\eta}},\bm{\tilde{p}})\leq v(\bm{\eta},\bm{p}) and ui​(𝐀~,𝐩~,𝛈~)≤ui​(𝐀,𝐩,𝛈)u\_{i}(\bm{\tilde{A}},\bm{\tilde{p}},\bm{\tilde{\eta}})\leq u\_{i}(\bm{A},\bm{p},\bm{\eta})
for all i=1,…,ni=1,\dots,n, with at least one of these inequalities being strict.

### 3.1 Characterization of Joint-Pareto optimality

To characterize the JP-optimal contracts in Definition [3.1](https://arxiv.org/html/2602.14223v1#S3.Thmtheorem1 "Definition 3.1. ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"), we adopt the 2-step approach delineated in Asimit et al. ([2021](https://arxiv.org/html/2602.14223v1#bib.bib8 "Risk sharing with multiple indemnity environments"), Section 2). First, we solve

|  |  |  |  |
| --- | --- | --- | --- |
|  | min𝑨,𝒑⁡{ρR​(𝒑)+∑i=1nρi​(𝑨)}s.t. ​𝑨​𝝁+𝑫​(𝝁)​𝒑=𝝁,𝟏⊤​𝑨+𝒑⊤=𝟏⊤.\min\_{\bm{A},\bm{p}}\left\{\rho\_{R}(\bm{p})+\sum\_{i=1}^{n}\rho\_{i}(\bm{A})\right\}\quad\text{s.t. }\bm{A}\bm{\mu}+\bm{D}(\bm{\mu})\bm{p}=\bm{\mu},\quad\mathbf{1}^{\top}\bm{A}+\bm{p}^{\top}=\bm{1}^{\top}. |  | (5) |

Note that the objective of Problem ([5](https://arxiv.org/html/2602.14223v1#S3.E5 "In 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) is given by the sum of members’ and the reinsurer’s preferences, which is independent of 𝜼\bm{\eta} as the relevant terms are canceled in the summation. Based on the solution to Problem ([5](https://arxiv.org/html/2602.14223v1#S3.E5 "In 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), we then determine the loading 𝜼\bm{\eta} in a way that the resulting triplet is JP-optimal.

We now provide the solution to Problem ([5](https://arxiv.org/html/2602.14223v1#S3.E5 "In 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")). To this end, we define the matrix

|  |  |  |
| --- | --- | --- |
|  | 𝑴¯:=(γR+1∑j=1nγj−1)​𝚺+k​𝑫​(𝝁2)​𝑫​(𝜸)−k​𝝁​𝝁⊤∑j=1nγj−1,\overline{\bm{M}}:=\left(\gamma\_{R}+\frac{1}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\right)\bm{\Sigma}+k\bm{D}(\bm{\mu}^{2})\bm{D}(\bm{\gamma})-\frac{k\bm{\mu}\bm{\mu}^{\top}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}, |  |

where 𝝁2\bm{\mu}^{2} is the componentwise square 𝝁\bm{\mu}, and k:=(𝝁⊤​𝚺−1​𝝁)−1k:=(\bm{\mu}^{\top}\bm{\Sigma}^{-1}\bm{\mu})^{-1}, which is positive since 𝝁≠𝟎\bm{\mu}\neq\bm{0} and 𝚺\bm{\Sigma} is positive definite. The following lemma addresses the invertibility of 𝑴¯\overline{\bm{M}}.

###### Lemma 3.2.

The matrix 𝐌¯\overline{\bm{M}} is positive definite and thus invertible.

Proof. 
See Appendix [A](https://arxiv.org/html/2602.14223v1#A1 "Appendix A Proof of Lemma 3.2 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
 ∎

The following proposition solves Problem ([5](https://arxiv.org/html/2602.14223v1#S3.E5 "In 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")).

###### Proposition 3.3.

The unique minimizer of Problem ([5](https://arxiv.org/html/2602.14223v1#S3.E5 "In 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝑨∗=𝑫​(𝜸)−1​𝟏𝟏⊤∑j=1nγj−1​𝑫​(𝟏−𝒑∗)+k​(𝑰n−𝑫​(𝜸)−1​𝟏𝟏⊤∑j=1nγj−1)​𝑫​(𝟏−𝒑∗)​𝝁​𝝁⊤​𝚺−1,𝒑∗= 1−γR​𝑴¯−1​𝚺​𝟏.\displaystyle\begin{split}\bm{A}\_{\*}=&\ \frac{\bm{D}(\bm{\gamma})^{-1}\bm{1}\bm{1}^{\top}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\bm{D}(\bm{1}-\bm{p}\_{\*})+k\left(\bm{I}\_{n}-\frac{\bm{D}(\bm{\gamma})^{-1}\bm{1}\bm{1}^{\top}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\right)\bm{D}(\bm{1}-\bm{p}\_{\*})\bm{\mu}\bm{\mu}^{\top}\bm{\Sigma}^{-1},\\ \bm{p}\_{\*}=&\ \bm{1}-\gamma\_{R}\overline{\bm{M}}^{-1}\bm{\Sigma}\bm{1}.\end{split} | |  | (6) |

In addition, if

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −γR​σi2+∑m≠i(k​μi​μm∑j=1nγj−1−(γR+1∑j=1nγj−1)​σi​m)+\displaystyle-\gamma\_{R}\sigma\_{i}^{2}+\sum\_{m\neq i}\left(\frac{k\mu\_{i}\mu\_{m}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}-\left(\gamma\_{R}+\frac{1}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\right)\sigma\_{im}\right)\_{+} |  | (7) |
|  |  | <∑m≠i(k​μi​μm−σi​m)∑j=1nγj−1<k​μi2​γi+σi2−k​μi2∑j=1nγj−1−∑m≠i((γR+1∑j=1nγj−1)​σi​m−k​μi​μm∑j=1nγj−1)+\displaystyle<\frac{\sum\_{{m\neq i}}(k\mu\_{i}\mu\_{m}-\sigma\_{im})}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}<k\mu\_{i}^{2}\gamma\_{i}{+\frac{\sigma\_{i}^{2}-k\mu\_{i}^{2}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}}-\sum\_{m\neq i}\left(\left(\gamma\_{R}+\frac{1}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\right)\sigma\_{im}-\frac{k\mu\_{i}\mu\_{m}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\right)\_{+} |  |

for any i∈{1,…,n}i\in\{1,\dots,n\}, then 𝐩∗∈(0,1)n\bm{p}\_{\*}\in(0,1)^{n}.

Proof. 
See Appendix [B](https://arxiv.org/html/2602.14223v1#A2 "Appendix B Proof of Proposition 3.3 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
 ∎

Note that the risk allocation in Proposition [3.3](https://arxiv.org/html/2602.14223v1#S3.Thmtheorem3 "Proposition 3.3. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") differs from the one depicted in Feng et al. ([2023](https://arxiv.org/html/2602.14223v1#bib.bib91 "Peer-to-peer risk sharing with an application to flood risk pooling"), Remark 3) due to the extra reinsurance layer.
One can immediately infer from the form of 𝑨∗\bm{A}\_{\*} that if there is no risk transfer to the reinsurer, both risk mutualizations in the current paper and that in Feng et al. ([2023](https://arxiv.org/html/2602.14223v1#bib.bib91 "Peer-to-peer risk sharing with an application to flood risk pooling")) coincide.

From the form of 𝒑∗\bm{p}\_{\*}, one can deduce that γR\gamma\_{R} should be positive and sufficiently small to circumvent full and zero reinsurance. In particular, γR=0\gamma\_{R}=0 leads to 𝒑∗=𝟏\bm{p}\_{\*}=\bm{1}, i.e., it is in the best interest of all agents for the risk-neutral reinsurer to absorb all risks in the Pareto design.
This entails that the reinsurer’s risk tolerance should be within an appropriate range to avoid both full reinsurance and no reinsurance. Moreover, ([7](https://arxiv.org/html/2602.14223v1#S3.E7 "In Proposition 3.3. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) is easier to satisfy when the σi​m\sigma\_{im} have small magnitudes compared to σi2\sigma\_{i}^{2}, i.e., 𝚺\bm{\Sigma} exhibits a weak dependence, which enables the diversification among agents.

The following statement characterizes the Joint-Pareto optimality.

###### Theorem 3.4.

[Characterization of Joint-Pareto optimality]
Suppose that Condition ([7](https://arxiv.org/html/2602.14223v1#S3.E7 "In Proposition 3.3. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) holds.
Let 𝒥​𝒫​𝒪\mathcal{JPO} be the set of JP-optimal contracts and 𝒵:={(𝐀,𝐩,𝛈)∈ℐ​ℛ:(𝐀,𝐩)​ solves Problem ([5](https://arxiv.org/html/2602.14223v1#S3.E5 "In 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"))}\mathcal{Z}:=\{(\bm{A},\bm{p},\bm{\eta})\in\mathcal{IR}:(\bm{A},\bm{p})\text{ solves Problem \eqref{Prob:RS}}\}.
Then, 𝒥​𝒫​𝒪=𝒵≠∅\mathcal{JPO}=\mathcal{Z}\neq\emptyset. Furthermore, let (𝐀∗,𝐩∗)(\bm{A}\_{\*},\bm{p}\_{\*}) be given in ([6](https://arxiv.org/html/2602.14223v1#S3.E6 "In Proposition 3.3. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), and 𝛈∗\bm{\eta}\_{\*} be a vector of safety loadings. Then, the following statements are equivalent:

1. (i)

   (𝑨∗,𝒑∗,𝜼∗)∈𝒥​𝒫​𝒪(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*})\in\mathcal{JPO}.
2. (ii)

   There exists (c1,c2,…,cn)∈ℝn(c\_{1},c\_{2},\dots,c\_{n})\in\mathbb{R}^{n} such that (𝑨∗,𝒑∗,𝜼∗)(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*}) solves

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  |  | min(𝑨,𝒑,𝜼)∈ℐ​ℛ,𝒑>0⁡v​(𝜼,𝒑)\displaystyle\min\_{(\bm{A},\bm{p},\bm{\eta})\in\mathcal{IR},{\bm{p}>0}}v(\bm{\eta},\bm{p}) |  | (8) |
   |  | s.t. | ui​(𝑨,𝒑,𝜼)=ci,for all ​i=1,…,n,𝑨​𝝁+𝑫​(𝝁)​𝒑=𝝁, 1⊤​𝑨+𝒑⊤=𝟏⊤.\displaystyle u\_{i}(\bm{A},\bm{p},\bm{\eta})=c\_{i},\ \text{for all }i=1,\dots,n,\ \bm{A}\bm{\mu}+\bm{D}(\bm{\mu})\bm{p}=\bm{\mu},\mathbf{1}^{\top}\bm{A}+\bm{p}^{\top}=\bm{1}^{\top}. |  |
3. (iii)

   There exists cR∈ℝc\_{R}\in\mathbb{R} such that (𝑨∗,𝒑∗,𝜼∗)(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*}) solves

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | min(𝑨,𝒑,𝜼)∈ℐ​ℛ,𝒑>0⁡u​(𝑨,𝒑,𝜼)​ s.t. ​v​(𝜼,𝒑)=cR,𝑨​𝝁+𝑫​(𝝁)​𝒑=𝝁, 1⊤​𝑨+𝒑⊤=𝟏⊤.\min\_{(\bm{A},\bm{p},\bm{\eta})\in\mathcal{IR},{\bm{p}>0}}u(\bm{A},\bm{p},\bm{\eta})\text{ s.t. }v(\bm{\eta},\bm{p})=c\_{R},\ \bm{A}\bm{\mu}+\bm{D}(\bm{\mu})\bm{p}=\bm{\mu},\ \mathbf{1}^{\top}\bm{A}+\bm{p}^{\top}=\bm{1}^{\top}. |  | (9) |

Proof. 
See Appendix [C](https://arxiv.org/html/2602.14223v1#A3 "Appendix C Proof of Theorem 3.4 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
 ∎

Theorem [3.4](https://arxiv.org/html/2602.14223v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") shows that one can always select a loading 𝜼∗\bm{\eta}\_{\*} such that, along with the solution (𝑨∗,𝒑∗)(\bm{A}\_{\*},\bm{p}\_{\*}) to Problem ([5](https://arxiv.org/html/2602.14223v1#S3.E5 "In 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), the resulting contract (𝑨∗,𝒑∗,𝜼∗)(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*}) satisfies all agents’ IRs ([3](https://arxiv.org/html/2602.14223v1#S2.E3 "In 2.3 Individual rationality ‣ 2 Model Formulations ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) and ([4](https://arxiv.org/html/2602.14223v1#S2.E4 "In 2.3 Individual rationality ‣ 2 Model Formulations ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), which is also a JP-optimal contract. In addition, Theorem [3.4](https://arxiv.org/html/2602.14223v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") offers two equivalent optimizations. By varying parameter cic\_{i}, i=1,…,ni=1,\ldots,n, (resp. cRc\_{R}) in (ii) (resp. (iii)), the entire Pareto frontier can be traced.

### 3.2 Cooperative game study on premium decision

Theorem [3.4](https://arxiv.org/html/2602.14223v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") shows that there may exist many safety loadings 𝜼∗\bm{\eta}\_{\*} such that the triple (𝑨∗,𝒑∗,𝜼∗)(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*}) is JP-optimal. This flexibility arises because all terms involving the safety loading cancel out in Problem ([5](https://arxiv.org/html/2602.14223v1#S3.E5 "In 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")). As revealed in Theorem [3.4](https://arxiv.org/html/2602.14223v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") and its proof, the selection of safety loadings can be considered as an allocation problem that apportions welfare gains from forming the P2P risk-sharing scheme. To study such a distribution problem and the corresponding premium decisions systematically, we formulate a cooperative transferable utility (TU) game (𝒩,ℬ)(\mathcal{N},\mathcal{B}), where 𝒩:={1,…,n,R}\mathcal{N}:=\{1,\dots,n,R\} is a finite set including all members and the reinsurer and ℬ:2𝒩↦[0,+∞)\mathcal{B}:2^{\mathcal{N}}\mapsto[0,+\infty) represents the worth of coalitions by mapping every subgroup to the corresponding maximal coalitional welfare gain, which is defined in detail below.

For the subgroup of members 𝒮⊆𝒯:={1,…,n}\mathcal{S}\subseteq\mathcal{T}:=\{1,\dots,n\}, we let 𝝁𝒮:=(μi)i∈𝒮\bm{\mu}^{\mathcal{S}}:=(\mu\_{i})\_{i\in\mathcal{S}}, 𝚺𝒮:=(σi​j)i,j∈𝒮\bm{\Sigma}^{\mathcal{S}}:=(\sigma\_{ij})\_{i,j\in\mathcal{S}}, and 𝜸𝒮:=(γi)i∈𝒮\bm{\gamma}^{\mathcal{S}}:=(\gamma\_{i})\_{i\in\mathcal{S}}. For any 𝑨𝒮=(ai​j)i,j∈𝒮∈ℝ|𝒮|×|𝒮|\bm{A}^{\mathcal{S}}=(a\_{ij})\_{i,j\in\mathcal{S}}\in\mathbb{R}^{|\mathcal{S}|\times|\mathcal{S}|}, 𝒑𝒮=(pi)i∈𝒮∈ℝ|𝒮|\bm{p}^{\mathcal{S}}=(p\_{i})\_{i\in\mathcal{S}}\in\mathbb{R}^{|\mathcal{S}|}, 𝜼𝒮=(ηi)i∈𝒮∈ℝ|𝒮|\bm{\eta}^{\mathcal{S}}=(\eta\_{i})\_{i\in\mathcal{S}}\in\mathbb{R}^{|\mathcal{S}|}, we (re)define, for any i∈𝒮i\in\mathcal{S},

|  |  |  |
| --- | --- | --- |
|  | ρi​(𝑨𝒮;𝒮):=∑j∈𝒮ai​j​μj+γi2​V​a​r​(∑j∈𝒮ai​j​Xj),ui​(𝑨𝒮,𝒑𝒮,𝜼𝒮;𝒮∪ℛ):=ρi​(𝑨𝒮;𝒮)+πi​(ηi,pi),\displaystyle\rho\_{i}(\bm{A}^{\mathcal{S}};\mathcal{S}):=\sum\_{j\in\mathcal{S}}a\_{ij}\mu\_{j}+\frac{\gamma\_{i}}{2}Var\left(\sum\_{j\in\mathcal{S}}a\_{ij}X\_{j}\right),\ u\_{i}(\bm{A}^{\mathcal{S}},\bm{p}^{\mathcal{S}},\bm{\eta}^{\mathcal{S}};\mathcal{S}\cup\mathcal{R}):=\rho\_{i}(\bm{A}^{\mathcal{S}};\mathcal{S})+\pi\_{i}(\eta\_{i},p\_{i}), |  |
|  |  |  |
| --- | --- | --- |
|  | u​(𝑨𝒮,𝒑𝒮,𝜼𝒮;𝒮∪ℛ):=∑i∈𝒮ui​(𝑨𝒮,𝒑𝒮,𝜼𝒮;𝒮∪ℛ),ρR​(𝒑𝒮;𝒮∪ℛ):=∑i∈𝒮pi​μi+γR2​V​a​r​(∑i∈𝒮pi​Xi),\displaystyle u(\bm{A}^{\mathcal{S}},\bm{p}^{\mathcal{S}},\bm{\eta}^{\mathcal{S}};\mathcal{S}\cup\mathcal{R}):=\sum\_{i\in\mathcal{S}}u\_{i}(\bm{A}^{\mathcal{S}},\bm{p}^{\mathcal{S}},\bm{\eta}^{\mathcal{S}};\mathcal{S}\cup\mathcal{R}),\ \rho\_{R}(\bm{p}^{\mathcal{S}};\mathcal{S}\cup\mathcal{R}):=\sum\_{i\in\mathcal{S}}p\_{i}\mu\_{i}+\frac{\gamma\_{R}}{2}Var\left(\sum\_{i\in\mathcal{S}}p\_{i}X\_{i}\right), |  |
|  |  |  |
| --- | --- | --- |
|  | v​(𝜼𝒮,𝒑𝒮;𝒮∪ℛ):=ρR​(𝒑𝒮;𝒮∪ℛ)−∑i∈𝒮πi​(ηi,pi).\displaystyle v(\bm{\eta}^{\mathcal{S}},\bm{p}^{\mathcal{S}};\mathcal{S}\cup\mathcal{R}):=\rho\_{R}(\bm{p}^{\mathcal{S}};\mathcal{S}\cup\mathcal{R})-\sum\_{i\in\mathcal{S}}\pi\_{i}(\eta\_{i},p\_{i}). |  |

Also, we define the set of all contracts that meet the individual rationality constraints, actuarial fairness, and zero-conserving condition for the subgroup 𝒮∪ℛ\mathcal{S}\cup\mathcal{R}, where ℛ:={R}\mathcal{R}:=\{R\}, by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℱ𝒮∪ℛ:={(𝑨𝒮∪ℛ\displaystyle{\mathcal{F}^{\mathcal{S}\cup\mathcal{R}}}=\bigg\{(\bm{A}^{\mathcal{S}\cup\mathcal{R}} | ,𝒑𝒮∪ℛ,𝜼𝒮∪ℛ):ωi(𝑨𝒮∪ℛ,𝒑𝒮∪ℛ,𝜼𝒮∪ℛ;𝒮∪ℛ)≥0,i∈𝒮∪ℛ,\displaystyle,\bm{p}^{\mathcal{S}\cup\mathcal{R}},\bm{\eta}^{\mathcal{S}\cup\mathcal{R}}):\omega\_{i}(\bm{A}^{\mathcal{S}\cup\mathcal{R}},\bm{p}^{\mathcal{S}\cup\mathcal{R}},\bm{\eta}^{\mathcal{S}\cup\mathcal{R}};\mathcal{S}\cup\mathcal{R})\geq 0,\ i\in\mathcal{S}\cup\mathcal{R}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝑨𝒮∪ℛ𝝁𝒮+𝑫(𝝁𝒮)𝒑𝒮∪ℛ=𝝁𝒮,(𝟏𝒮)⊤𝑨𝒮∪ℛ+(𝒑𝒮∪ℛ)⊤=(𝟏𝒮)⊤}.\displaystyle\bm{A}^{\mathcal{S}\cup\mathcal{R}}\bm{\mu}^{\mathcal{S}}+\bm{D}(\bm{\mu}^{\mathcal{S}})\bm{p}^{\mathcal{S}\cup\mathcal{R}}=\bm{\mu}^{\mathcal{S}},\ (\bm{1}^{\mathcal{S}})^{\top}\bm{A}^{\mathcal{S}\cup\mathcal{R}}+(\bm{p}^{\mathcal{S}\cup\mathcal{R}})^{\top}=(\bm{1}^{\mathcal{S}})^{\top}\bigg\}. |  |

Note that with a slight abuse of notation, here we assume that (𝑨𝒮∪ℛ,𝒑𝒮∪ℛ,𝜼𝒮∪ℛ)∈ℝ|𝒮|×|𝒮|×ℝ|𝒮|×ℝ|𝒮|(\bm{A}^{\mathcal{S}\cup\mathcal{R}},\bm{p}^{\mathcal{S}\cup\mathcal{R}},\bm{\eta}^{\mathcal{S}\cup\mathcal{R}})\in\mathbb{R}^{|\mathcal{S}|\times|\mathcal{S}|}\times\mathbb{R}^{|\mathcal{S}|}\times\mathbb{R}^{|\mathcal{S}|} for 𝒮⊆𝒯\mathcal{S}\subseteq\mathcal{T}. For the coalition 𝒮⊆𝒯\mathcal{S}\subseteq\mathcal{T} without the reinsurer, ℱ𝒮\mathcal{F}^{\mathcal{S}} can be defined by forcing 𝒑𝒮=𝜼𝒮=𝟎𝒮\bm{p}^{\mathcal{S}}=\bm{\eta}^{\mathcal{S}}=\bm{0}^{\mathcal{S}}, where 𝟎𝒮\bm{0}^{\mathcal{S}} denotes the zero vector in ℝ|𝒮|\mathbb{R}^{|\mathcal{S}|},
i.e.,

|  |  |  |
| --- | --- | --- |
|  | ℱ𝒮:={(𝑨𝒮,𝟎𝒮,𝟎𝒮):ωi​(𝑨𝒮,𝟎𝒮,𝟎𝒮;𝒮)≥0,i∈𝒮,𝑨𝒮​𝝁𝒮=𝝁𝒮,(𝟏𝒮)⊤​𝑨𝒮=(𝟏𝒮)⊤}.\mathcal{F}^{\mathcal{S}}:=\{(\bm{A}^{\mathcal{S}},\bm{0}^{\mathcal{S}},\bm{0}^{\mathcal{S}}):\omega\_{i}(\bm{A}^{\mathcal{S}},{\bm{0}^{\mathcal{S}},\bm{0}^{\mathcal{S}}};\mathcal{S})\geq 0,\ i\in\mathcal{S},\ \bm{A}^{\mathcal{S}}\bm{\mu}^{\mathcal{S}}=\bm{\mu}^{\mathcal{S}},\ (\bm{1}^{\mathcal{S}})^{\top}\bm{A}^{\mathcal{S}}=(\bm{1}^{\mathcal{S}})^{\top}\}. |  |

Next, we define the mapping ℬ\mathcal{B} for coalitions with and without the reinsurer as follows. For coalitions 𝒞\mathcal{C} with the reinsurer included, i.e.,
𝒞=𝒮∪ℛ\mathcal{C}=\mathcal{S}\cup\mathcal{R},
𝒮⊆𝒯\mathcal{S}\subseteq\mathcal{T}, we define

|  |  |  |
| --- | --- | --- |
|  | ℬ​(𝒞):=ℬ​(𝒮∪ℛ)=∑i∈𝒮(μi+γi​σi22)−∑i∈𝒮ρi​(𝑨∗𝒮∪ℛ;𝒮)−ρR​(𝒑∗𝒮∪ℛ;𝒮∪ℛ),\mathcal{B}(\mathcal{C}):=\mathcal{B}(\mathcal{S}\cup\mathcal{R})=\sum\_{i\in\mathcal{S}}\left(\mu\_{i}+\frac{\gamma\_{i}\sigma\_{i}^{2}}{2}\right)-\sum\_{i\in\mathcal{S}}\rho\_{i}(\bm{A}^{\mathcal{S}\cup\mathcal{R}}\_{\*};\mathcal{S})-\rho\_{R}(\bm{p}^{\mathcal{S}\cup\mathcal{R}}\_{\*};\mathcal{S}\cup\mathcal{R}), |  |

where (𝑨∗𝒮∪ℛ,𝒑∗𝒮∪ℛ)∈ℝ|𝒮|×|𝒮|×ℝ|𝒮|(\bm{A}^{\mathcal{S}\cup\mathcal{R}}\_{\*},\bm{p}^{\mathcal{S}\cup\mathcal{R}}\_{\*})\in\mathbb{R}^{|\mathcal{S}|\times|\mathcal{S}|}\times\mathbb{R}^{|\mathcal{S}|} is the solution to the following minimization problem, which is the version of Problem ([5](https://arxiv.org/html/2602.14223v1#S3.E5 "In 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) under the coalition 𝒞=𝒮∪ℛ\mathcal{C}=\mathcal{S}\cup\mathcal{R},

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | min𝑨𝒮∪ℛ,𝒑𝒮∪ℛ⁡{ρR​(𝒑𝒮∪ℛ;𝒮∪ℛ)+∑i∈𝒮ρi​(𝑨𝒮∪ℛ;𝒮)}\displaystyle\min\_{\bm{A}^{\mathcal{S}\cup\mathcal{R}},\bm{p}^{\mathcal{S}\cup\mathcal{R}}}\left\{\rho\_{R}(\bm{p}^{\mathcal{S}\cup\mathcal{R}};\mathcal{S}\cup\mathcal{R})+\sum\_{i\in\mathcal{S}}\rho\_{i}(\bm{A}^{\mathcal{S}\cup\mathcal{R}};\mathcal{S})\right\} |  | (10) |
|  |  | s.t. ​𝑨𝒮∪ℛ​𝝁𝒮+𝑫​(𝝁𝒮)​𝒑𝒮∪ℛ=𝝁𝒮,(𝟏𝒮)⊤​𝑨𝒮∪ℛ+(𝒑𝒮∪ℛ)⊤=(𝟏𝒮)⊤.\displaystyle\text{s.t. }\bm{A}^{\mathcal{S}\cup\mathcal{R}}\bm{\mu}^{\mathcal{S}}+\bm{D}(\bm{\mu}^{\mathcal{S}})\bm{p}^{\mathcal{S}\cup\mathcal{R}}=\bm{\mu}^{\mathcal{S}},\quad(\mathbf{1}^{\mathcal{S}})^{\top}\bm{A}^{\mathcal{S}\cup\mathcal{R}}+(\bm{p}^{\mathcal{S}\cup\mathcal{R}})^{\top}=(\bm{1}^{\mathcal{S}})^{\top}. |  |

In particular,

|  |  |  |
| --- | --- | --- |
|  | ℬ​(𝒩)=∑i=1n(μi+γi​σi22)−∑i=1nρi​(𝑨∗;𝒯)−ρR​(𝒑∗;𝒩),\mathcal{B}(\mathcal{N})=\sum\_{i=1}^{n}\left(\mu\_{i}+\frac{\gamma\_{i}\sigma\_{i}^{2}}{2}\right)-\sum\_{i=1}^{n}\rho\_{i}(\bm{A}\_{\*};\mathcal{T})-\rho\_{R}(\bm{p}\_{\*};\mathcal{N}), |  |

where (𝑨∗,𝒑∗)(\bm{A}\_{\*},\bm{p}\_{\*}) is the solution of Problem ([5](https://arxiv.org/html/2602.14223v1#S3.E5 "In 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")).

On the other hand, for coalitions 𝒞\mathcal{C} without the reinsurer, i.e., R∉𝒞R\notin\mathcal{C},
we define ℬ​(𝒞)\mathcal{B}(\mathcal{C}) by considering the following version of Problem ([5](https://arxiv.org/html/2602.14223v1#S3.E5 "In 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) under 𝒞\mathcal{C}, i.e.,

|  |  |  |  |
| --- | --- | --- | --- |
|  | min𝑨𝒞​∑i∈𝒞ρi​(𝑨𝒞;𝒞)s.t. ​𝑨𝒞​𝝁𝒞=𝝁𝒞,(𝟏𝒞)⊤​𝑨𝒞=(𝟏𝒞)⊤.\min\_{\bm{A}^{\mathcal{C}}}\sum\_{i\in\mathcal{C}}\rho\_{i}(\bm{A}^{\mathcal{C}};\mathcal{C})\quad\text{s.t. }\bm{A}^{\mathcal{C}}\bm{\mu}^{\mathcal{C}}=\bm{\mu}^{\mathcal{C}},\quad(\mathbf{1}^{\mathcal{C}})^{\top}\bm{A}^{\mathcal{C}}=(\bm{1}^{\mathcal{C}})^{\top}. |  | (11) |

The solution to Problem ([11](https://arxiv.org/html/2602.14223v1#S3.E11 "In 3.2 Cooperative game study on premium decision ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) is given in Feng et al. ([2023](https://arxiv.org/html/2602.14223v1#bib.bib91 "Peer-to-peer risk sharing with an application to flood risk pooling"), Remark 3), depicted as follows:

|  |  |  |
| --- | --- | --- |
|  | 𝑨∗𝒞=𝑫​(𝜸𝒞)−1​𝟏𝒞​(𝟏𝒞)⊤∑i∈𝒞γi−1+k𝒞​(𝑰𝒞−𝑫​(𝜸𝒞)−1​𝟏𝒞​(𝟏𝒞)⊤|𝒞|)​𝝁𝒞​(𝝁𝒞)⊤​(𝚺𝒞)−1,\bm{A}^{\mathcal{C}}\_{\*}=\frac{\bm{D}(\bm{\gamma}^{\mathcal{C}})^{-1}\bm{1}^{\mathcal{C}}(\bm{1}^{\mathcal{C}})^{\top}}{\sum\_{i\in\mathcal{C}}\gamma\_{i}^{-1}}+k\_{\mathcal{C}}\left(\bm{I}\_{\mathcal{C}}-\frac{\bm{D}(\bm{\gamma}^{\mathcal{C}})^{-1}\bm{1}^{\mathcal{C}}(\bm{1}^{\mathcal{C}})^{\top}}{|{\mathcal{C}}|}\right)\bm{\mu}^{\mathcal{C}}(\bm{\mu}^{\mathcal{C}})^{\top}(\bm{\Sigma}^{\mathcal{C}})^{-1}, |  |

where k𝒞:=((𝝁𝒞)⊤​(𝚺𝒞)−1​𝝁𝒞)−1k\_{\mathcal{C}}:=((\bm{\mu}^{\mathcal{C}})^{\top}(\bm{\Sigma}^{\mathcal{C}})^{-1}\bm{\mu}^{\mathcal{C}})^{-1}. Using this, we define

|  |  |  |
| --- | --- | --- |
|  | ℬ​(𝒞):=∑i∈𝒞(μi+γi​σi22)−∑i∈𝒞ρi​(𝑨∗𝒞;𝒞)≥0,\displaystyle\mathcal{B}(\mathcal{C}):=\sum\_{i\in\mathcal{C}}\left(\mu\_{i}+\frac{\gamma\_{i}\sigma\_{i}^{2}}{2}\right)-\sum\_{i\in\mathcal{C}}\rho\_{i}(\bm{A}^{\mathcal{C}}\_{\*};\mathcal{C})\geq 0, |  |

where the inequality follows from the fact that 𝑰𝓒∈ℝ|𝒞|×|𝒞|\bm{I\_{\mathcal{C}}}\in\mathbb{R}^{|\mathcal{C}|\times|\mathcal{C}|} is also admissible in Problem ([11](https://arxiv.org/html/2602.14223v1#S3.E11 "In 3.2 Cooperative game study on premium decision ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")).

#### 3.2.1 Coalitional stability and the core

The core (Gillies, [1953](https://arxiv.org/html/2602.14223v1#bib.bib25 "Some theorems on n-person games")) of the game (𝒩,ℬ)(\mathcal{N},\mathcal{B}) collects the set of allocations such that no subgroup of agents has a joint incentive to deviate from the grand coalition 𝒩\mathcal{N}, which is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | c​o​r​e​(𝒩,ℬ):={𝒄∈ℝ+n+1:∑i∈𝒞ci≥ℬ​(𝒞),∑i∈𝒩ci=ℬ​(𝒩),for all ​∅≠𝒞⊆𝒩}.core(\mathcal{N},\mathcal{B}):=\left\{\bm{c}\in\mathbb{R}\_{+}^{n+1}:\sum\_{i\in\mathcal{C}}c\_{i}\geq\mathcal{B}(\mathcal{C}),\ \sum\_{i\in\mathcal{N}}c\_{i}=\mathcal{B}(\mathcal{N}),\ \text{for all }\emptyset\neq\mathcal{C}\subseteq\mathcal{N}\right\}. |  | (12) |

In other words, if the allocation lies in the core, no subgroup of agents has an incentive to break away from the grand coalition 𝒩\mathcal{N}. The following theorem proves the non-emptiness of the core.

###### Theorem 3.5.

The core of the coalition game (𝒩,ℬ)(\mathcal{N},\mathcal{B}) is non-empty.

Proof. 
See Appendix [D](https://arxiv.org/html/2602.14223v1#A4 "Appendix D Proof of Theorem 3.5 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")
 ∎

The next proposition shows how to construct a JP-optimal contract from the core.

###### Proposition 3.6.

Let 𝐜∈c​o​r​e​(𝒩,ℬ)\bm{c}\in core(\mathcal{N},\mathcal{B}), and suppose that (𝐀∗,𝐩∗)(\bm{A}\_{\*},\bm{p}\_{\*}) solves Problem ([5](https://arxiv.org/html/2602.14223v1#S3.E5 "In 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")). Then, we can uniquely define 𝛈∗\bm{\eta}\_{\*} such that ωi​(𝐀∗,𝐩∗,𝛈∗)=ci\omega\_{i}(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*})=c\_{i} for all i∈𝒩i\in\mathcal{N}, and (𝐀∗,𝐩∗,𝛈∗)∈𝒥​𝒫​𝒪(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*})\in\mathcal{JPO}.

Proof. 
See Appendix [E](https://arxiv.org/html/2602.14223v1#A5 "Appendix E Proof of Proposition 3.6 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
 ∎

The elements in the core lead to stable allocations, which are formally defined as follows.

###### Definition 3.7 (Coalitional stability).

A contract (𝐀,𝐩,𝛈)∈ℐ​ℛ(\bm{A},\bm{p},\bm{\eta})\in\mathcal{IR} is called coalitionally stable if there does not exist a subset 𝒞⊆𝒩\mathcal{C}\subseteq\mathcal{N} and (𝐀𝒞,𝐩𝒞,𝛈𝒞)∈ℱ𝒞(\bm{A}^{\mathcal{C}},\bm{p}^{\mathcal{C}},\bm{\eta}^{\mathcal{C}})\in\mathcal{F}^{\mathcal{C}} such that for all i∈𝒞i\in\mathcal{C}, ui​(𝐀𝒞,𝐩𝒞,𝛈𝒞;𝒞)≤ui​(𝐀,𝐩,𝛈;𝒩)u\_{i}(\bm{A}^{\mathcal{C}},\bm{p}^{\mathcal{C}},\bm{\eta}^{\mathcal{C}};{\mathcal{C}})\leq u\_{i}(\bm{A},\bm{p},\bm{\eta};{\mathcal{N}}), and if R∈𝒞R\in\mathcal{C}, v​(𝛈𝒞,𝐩𝒞;𝒞)≤v​(𝛈,𝐩;𝒩)v(\bm{\eta}^{\mathcal{C}},\bm{p}^{\mathcal{C}};{\mathcal{C}})\leq v(\bm{\eta},\bm{p};{\mathcal{N}}),
with at least one strict inequality.

It is clear that a coalitionally stable contract is JP-optimal.
The following proposition asserts that JP-optimal contracts with welfare gains allocation lying in the core are coalitionally stable.

###### Proposition 3.8.

A contract (𝐀,𝐩,𝛈)(\bm{A},\bm{p},\bm{\eta}) is coalitionally stable if (𝐀,𝐩,𝛈)∈𝒥​𝒫​𝒪(\bm{A},\bm{p},\bm{\eta})\in\mathcal{JPO} and

|  |  |  |
| --- | --- | --- |
|  | (ω1​(𝑨,𝒑,𝜼),…,ωn​(𝑨,𝒑,𝜼),ℬ​(𝒩)−∑i=1nωi​(𝑨,𝒑,𝜼))∈c​o​r​e​(𝒩,b).\left(\omega\_{1}(\bm{A},\bm{p},\bm{\eta}),\dots,\omega\_{n}(\bm{A},\bm{p},\bm{\eta}),\mathcal{B}(\mathcal{N})-\sum\_{i=1}^{n}\omega\_{i}(\bm{A},\bm{p},\bm{\eta})\right)\in core(\mathcal{N},b). |  |

Proof. 
See Appendix [F](https://arxiv.org/html/2602.14223v1#A6 "Appendix F Proof of Proposition 3.8 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")
 ∎

#### 3.2.2 Practical premium suggestions

In practice, the loading under the expected value premium principle is positive and is used to build up risk capital and compensate for administrative costs. Hereafter, we impose a non-negativity condition ηi≥0\eta\_{i}\geq 0, i=1,…,ni=1,\dots,n, to maintain the closure of feasible contract sets.

To ensure the reinsurer’s IR constraint is met, consider the following price of the reinsurance contracts:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜼min​(𝒑):=γR2​𝑫​(𝝁)−1​𝚺​𝒑.\bm{\eta}\_{\min}(\bm{p}):=\frac{\gamma\_{R}}{2}\bm{D}(\bm{\mu})^{-1}\bm{\Sigma}\bm{p}. |  | (13) |

It is clear that ([4](https://arxiv.org/html/2602.14223v1#S2.E4 "In 2.3 Individual rationality ‣ 2 Model Formulations ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) is met for any 𝜼≥𝜼min​(𝒑)\bm{\eta}\geq\bm{\eta}\_{\min}(\bm{p}) provided that 𝒑≥𝟎\bm{p}\geq\bm{0}. Combining with the non-negativity requirement, we impose the following minimal safety loadings given by max⁡{𝟎,𝜼min​(𝒑)}\max\{\bm{0},\bm{\eta}\_{\min}(\bm{p})\}.444For 𝒂,𝒃∈ℝn\bm{a},\bm{b}\in\mathbb{R}^{n}, max⁡{𝒂,𝒃}=(max⁡(ai,bi))i=1,…,n\max\{\bm{a},\bm{b}\}=(\max(a\_{i},b\_{i}))\_{i=1,\ldots,n}.

The following statement provides sufficient conditions for the construction of JP-optimal contracts that satisfy the minimal charge requirement, and establishes a correspondence between core elements and such contracts. The proof of the latter statement relies on the fact that no member can obtain a welfare gain exceeding their marginal contribution, which ensures stability.

###### Proposition 3.9 (Nonnegative loading in the core).

Let (𝐀∗,𝐩∗)(\bm{A}\_{\*},\bm{p}\_{\*}) be the solution to Problem ([5](https://arxiv.org/html/2602.14223v1#S3.E5 "In 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")),
and assume that Condition ([7](https://arxiv.org/html/2602.14223v1#S3.E7 "In Proposition 3.3. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) and the following hold for all i=1,…,ni=1,\dots,n:

|  |  |  |  |
| --- | --- | --- | --- |
|  | γi​[σi2−(γi−1∑j=1nγj−1)2​∑j,l=1n(σj​l)+−k​μi2]≥γR​∑m=1n(σi​m)+.\gamma\_{i}\left[\sigma\_{i}^{2}-\left(\frac{\gamma\_{i}^{-1}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\right)^{2}\sum\_{j,l=1}^{n}(\sigma\_{jl})\_{+}-k\mu\_{i}^{2}\right]\geq\gamma\_{R}\sum\_{m=1}^{n}(\sigma\_{im})\_{+}. |  | (14) |

Then, there exists 𝛈≥max⁡{𝟎,𝛈min​(𝐩∗)}\bm{\eta}\geq\max\{\bm{0},\bm{\eta}\_{\min}(\bm{p}\_{\*})\} such that (𝐀∗,𝐩∗,𝛈)∈𝒥​𝒫​𝒪(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta})\in\mathcal{JPO}.

Furthermore, suppose that for any i=1,…,n,i=1,\dots,n,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℬ​(𝒩)−ℬ​(𝒩\{i})≤ωi​(𝑨∗,𝒑∗,max⁡{𝟎,𝜼min​(𝒑∗)}).\mathcal{B}(\mathcal{N})-\mathcal{B}(\mathcal{N}\backslash\{i\})\leq{\omega\_{i}(\bm{A}\_{\*},\bm{p}\_{\*},\max\{\bm{0},\bm{\eta}\_{\min}(\bm{p}\_{\*})\}).} |  | (15) |

Then, for any 𝐜∈c​o​r​e​(𝒩,ℬ)\bm{c}\in core(\mathcal{N},\mathcal{B}), there exists 𝛈𝐜≥max⁡{𝟎,𝛈min​(𝐩∗)}\bm{\eta}\_{\bm{c}}\geq\max\{\bm{0},\bm{\eta}\_{\min}(\bm{p}\_{\*})\} such that ωi​(𝐀∗,𝐩∗,𝛈𝐜)=ci\omega\_{i}(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\bm{c}})=c\_{i} for all i∈𝒩i\in\mathcal{N} and (𝐀∗,𝐩∗,𝛈𝐜)∈𝒥​𝒫​𝒪(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\bm{c}})\in\mathcal{JPO}.

Proof. 
See Appendix [G](https://arxiv.org/html/2602.14223v1#A7 "Appendix G Proof of Proposition 3.9 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
 ∎

Condition ([14](https://arxiv.org/html/2602.14223v1#S3.E14 "In Proposition 3.9 (Nonnegative loading in the core). ‣ 3.2.2 Practical premium suggestions ‣ 3.2 Cooperative game study on premium decision ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) holds when the risk aversion of the reinsurer is sufficiently small, and risks are mildly correlated. In particular, for a given 𝒑\bm{p}, the minimum safety loading 𝜼min​(𝒑)\bm{\eta}\_{\min}(\bm{p}) required to satisfy the reinsurer’s IR constraint decreases as γR\gamma\_{R} decreases, which in turn raises the members’ welfare gains (see ([2](https://arxiv.org/html/2602.14223v1#S2.E2 "In 2.3 Individual rationality ‣ 2 Model Formulations ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"))) and makes it easier to satisfy their IR constraints.
Moreover, Condition ([15](https://arxiv.org/html/2602.14223v1#S3.E15 "In Proposition 3.9 (Nonnegative loading in the core). ‣ 3.2.2 Practical premium suggestions ‣ 3.2 Cooperative game study on premium decision ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) further indicates that all members shall receive welfare gains that exceed their marginal contributions to the pool so that stability is ensured.

The following corollary describes a condition under which the reinsurer can set a single nonnegative loading without violating the stability requirement when she is not allowed to charge differently across members in the pool, i.e., she must set 𝜼=t​𝟏\bm{\eta}=t\bm{1} for some t≥0t\geq 0.

###### Corollary 3.10 (Single loading in the core).

Assume that c​o​r​e​(𝒩,ℬ)core(\mathcal{N},\mathcal{B}) is not a singleton and that Conditions ([7](https://arxiv.org/html/2602.14223v1#S3.E7 "In Proposition 3.3. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), ([14](https://arxiv.org/html/2602.14223v1#S3.E14 "In Proposition 3.9 (Nonnegative loading in the core). ‣ 3.2.2 Practical premium suggestions ‣ 3.2 Cooperative game study on premium decision ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) and ([15](https://arxiv.org/html/2602.14223v1#S3.E15 "In Proposition 3.9 (Nonnegative loading in the core). ‣ 3.2.2 Practical premium suggestions ‣ 3.2 Cooperative game study on premium decision ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) hold.
Let 𝐜(𝟏),𝐜(𝟐)∈c​o​r​e​(𝒩,ℬ)\bm{c^{(1)}},\bm{c^{(2)}}\in core(\mathcal{N},\mathcal{B}),
and 𝛈(𝟏)\bm{\eta^{(1)}} and 𝛈(𝟐)\bm{\eta^{(2)}} the corresponding loadings (see Proposition [3.6](https://arxiv.org/html/2602.14223v1#S3.Thmtheorem6 "Proposition 3.6. ‣ 3.2.1 Coalitional stability and the core ‣ 3.2 Cooperative game study on premium decision ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")). If mini⁡ηi(1)≥maxi⁡ηi(2)\min\_{i}\eta^{(1)}\_{i}\geq\max\_{i}\eta^{(2)}\_{i}, then
for any t∈[maxi⁡ηi(1),mini⁡ηi(2)]t\in[\max\_{i}\eta^{(1)}\_{i},\min\_{i}\eta^{(2)}\_{i}], (𝐀∗,𝐩∗,t​𝟏)∈𝒥​𝒫​𝒪(\bm{A}\_{\*},\bm{p}\_{\*},t\bm{1})\in\mathcal{JPO}, and

|  |  |  |
| --- | --- | --- |
|  | (ω1​(𝑨∗,𝒑∗,t​𝟏),…,ωn​(𝑨∗,𝒑∗,t​𝟏),ℬ​(𝒩)−∑i=1nωi​(𝑨,𝒑,t​𝟏))∈c​o​r​e​(𝒩,b).\left(\omega\_{1}(\bm{A}\_{\*},\bm{p}\_{\*},t\bm{1}),\dots,\omega\_{n}(\bm{A}\_{\*},\bm{p}\_{\*},t\bm{1}),\mathcal{B}(\mathcal{N})-\sum\_{i=1}^{n}\omega\_{i}(\bm{A},\bm{p},t\bm{1})\right)\in core(\mathcal{N},b). |  |

Proof. 
See Appendix [H](https://arxiv.org/html/2602.14223v1#A8 "Appendix H Proof of Corollary 3.10 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
 ∎

## 4 Bowley Design

In this section, we examine the risk-sharing scheme of the Bowley design. Under this setting, the reinsurer acts as the leader and has the first-mover advantage of choosing the safety loading 𝜼\bm{\eta} while anticipating the plan manager’s response. The plan manager, in turn, acts as the follower and determines the risk-mutualization–reinsurance strategy (𝑨​(𝜼),𝒑​(𝜼))(\bm{A}(\bm{\eta}),\bm{p}(\bm{\eta})) based on the quoted loading 𝜼\bm{\eta}. This leads to two sequentially linked sub-problems, as illustrated in Fig. [2](https://arxiv.org/html/2602.14223v1#S4.F2 "Figure 2 ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").

P2P Plan Manager (𝑨​(𝜼),𝒑​(𝜼)\bm{A}(\bm{\eta}),\bm{p}(\bm{\eta}))Reinsurer (𝜼\bm{\eta})Risk-aware profit optimizationPareto allocation and reinsurance game𝜼\bm{\eta}𝒑​(𝜼)\bm{p}(\bm{\eta})Stage 1Stage 2


Figure 2: Summary of the sequential game between the reinsurer and the P2P insurance plan manager. The reinsurer selects the risk loading η\eta, and the insurer the proportional reinsurance strategy 𝒑​(𝜼)\bm{p}(\bm{\eta}).

### 4.1 Problem formulation

We formulate sub-problems in the sequential game and thereby define the Bowley-optimal contract.

#### 4.1.1 Plan manager’s follower problem

We first consider the plan manager’s problem. To this end, we assume that the safety loading 𝜼\bm{\eta} is exogenous and define the manager’s optimization problem in Definition [4.1](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem1 "Definition 4.1 (Pareto-optimal risk allocation). ‣ 4.1.1 Plan manager’s follower problem ‣ 4.1 Problem formulation ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"). To maintain mathematical tractability and obtain closed-form solutions, we initially omit the IR constraints from the follower’s and leader’s problems, and defer the analysis of the IR constraints to Lemma [4.7](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem7 "Lemma 4.7. ‣ 4.4 Bowley optimum ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") and Section [L](https://arxiv.org/html/2602.14223v1#A12 "Appendix L A Discussion on Condition (19) ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").

###### Definition 4.1 (Pareto-optimal risk allocation).

Given a safety loading 𝛈\bm{\eta}, a risk allocation (𝐀(𝛈)(\bm{A}(\bm{\eta}),𝐩(𝛈))\bm{p}(\bm{\eta})) is called Pareto optimal if there exists no other risk allocation (𝐀~​(𝛈),𝐩~​(𝛈))(\bm{\tilde{A}}(\bm{\eta}),\bm{\tilde{p}}(\bm{\eta})) such that ui​(𝐀~​(𝛈),𝐩~​(𝛈),𝛈)≤ui​(𝐀,𝐩,𝛈)u\_{i}(\bm{\tilde{A}}(\bm{\eta}),\bm{\tilde{p}}(\bm{\eta}),\bm{\eta})\leq u\_{i}(\bm{A},\bm{p},\bm{\eta})
for all i=1,…,ni=1,\dots,n, with at least one strict inequality.

By the standard argument (e.g., Aubin, [2002](https://arxiv.org/html/2602.14223v1#bib.bib26 "Optima and equilibria: an introduction to nonlinear analysis"), Chapter 12), a Pareto-optimal risk allocation is characterized by the following convex minimization problem with the actuarial fairness and zero-conserving constraints:

|  |  |  |  |
| --- | --- | --- | --- |
|  | min𝑨​(𝜼),𝒑​(𝜼)⁡u​(𝑨​(𝜼),𝒑​(𝜼),𝜼)s.t. ​𝑨​(𝜼)​𝝁+𝑫​(𝝁)​𝒑​(𝜼)=𝝁,𝟏⊤​𝑨​(𝜼)+𝒑⊤​(𝜼)=𝟏⊤.\min\_{\bm{A}(\bm{\eta}),\bm{p}(\bm{\eta})}u(\bm{A}(\bm{\eta}),\bm{p}(\bm{\eta}),\bm{\eta})\quad\text{s.t. }\bm{A}(\bm{\eta})\bm{\mu}+\bm{D}(\bm{\mu})\bm{p}(\bm{\eta})=\bm{\mu},\quad\mathbf{1}^{\top}\bm{A}(\bm{\eta})+\bm{p}^{\top}(\bm{\eta})=\bm{1}^{\top}. |  | (16) |

#### 4.1.2 Reinsurer’s leader problem

Next, we consider the reinsurer’s optimization problem.
Exploiting her first-mover advantage and taking into account the induced follower response (𝑨∗​(𝜼),𝒑∗​(𝜼))(\bm{A}^{\*}(\bm{\eta}),\bm{p}^{\*}(\bm{\eta})) in Proposition [4.4](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem4 "Proposition 4.4. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"), the reinsurer chooses the loading to optimize her objective, which is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | min𝜼⁡v​(𝜼,𝒑∗​(𝜼))s.t. ​𝒑∗​(𝜼)​ is the optimal indemnity of Problem ([16](https://arxiv.org/html/2602.14223v1#S4.E16 "In 4.1.1 Plan manager’s follower problem ‣ 4.1 Problem formulation ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")).\min\_{\bm{\eta}}v(\bm{\eta},\bm{p}^{\*}(\bm{\eta}))\quad\text{s.t. }\bm{p}^{\*}(\bm{\eta})\text{ is the optimal indemnity of Problem \eqref{Prob:follower}}. |  | (17) |

Based on the two sub-problems, we define the Bowley-optimal contract as follows.

###### Definition 4.2.

A contract (𝐀∗​(𝛈∗),𝐩∗​(𝛈∗),𝛈∗)(\bm{A}^{\*}(\bm{\eta}^{\*}),\bm{p}^{\*}(\bm{\eta}^{\*}),\bm{\eta}^{\*}) is called Bowley-optimal if it satisfies the following conditions:

1. 1.

   (𝑨∗​(𝜼∗),𝒑∗​(𝜼∗))(\bm{A}^{\*}(\bm{\eta}^{\*}),\bm{p}^{\*}(\bm{\eta}^{\*})) is a Pareto-optimal risk allocation (see Definition [4.1](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem1 "Definition 4.1 (Pareto-optimal risk allocation). ‣ 4.1.1 Plan manager’s follower problem ‣ 4.1 Problem formulation ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"));
2. 2.

   𝜼∗\bm{\eta}^{\*} solves Problem ([17](https://arxiv.org/html/2602.14223v1#S4.E17 "In 4.1.2 Reinsurer’s leader problem ‣ 4.1 Problem formulation ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"));
3. 3.

   (𝑨∗​(𝜼∗),𝒑∗​(𝜼∗),𝜼∗)∈ℐ​ℛ(\bm{A}^{\*}(\bm{\eta}^{\*}),\bm{p}^{\*}(\bm{\eta}^{\*}),\bm{\eta}^{\*})\in\mathcal{IR}.

### 4.2 Solution to the plan manager’s follower problem

Following the backward induction, we first tackle the follower’s problem.
Similar to Lemma [3.2](https://arxiv.org/html/2602.14223v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"), the solution of Problem ([16](https://arxiv.org/html/2602.14223v1#S4.E16 "In 4.1.1 Plan manager’s follower problem ‣ 4.1 Problem formulation ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) is characterized by a matrix 𝑴\bm{M} defined below, whose properties can be proven in the same manner as Lemma [3.2](https://arxiv.org/html/2602.14223v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").

###### Lemma 4.3.

The matrix 𝐌:=𝐌¯−γR​𝚺\bm{M}:=\overline{\bm{M}}-\gamma\_{R}\bm{\Sigma}
is invertible and positive definite.

The following proposition solves Problem ([16](https://arxiv.org/html/2602.14223v1#S4.E16 "In 4.1.1 Plan manager’s follower problem ‣ 4.1 Problem formulation ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) by the Lagrangian method.

###### Proposition 4.4.

The solution to Problem ([16](https://arxiv.org/html/2602.14223v1#S4.E16 "In 4.1.1 Plan manager’s follower problem ‣ 4.1 Problem formulation ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) is given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝑨∗​(𝜼)=𝑫​(𝜸)−1​𝟏𝟏⊤∑j=1nγj−1​𝑫​(𝟏−𝒑∗​(𝜼))+k​(𝑰n−𝑫​(𝜸)−1​𝟏𝟏⊤∑j=1nγj−1)​𝑫​(𝟏−𝒑∗​(𝜼))​𝝁​𝝁⊤​𝚺−1,𝒑∗​(𝜼)= 1−𝑴−1​𝑫​(𝝁)​𝜼.\displaystyle\begin{split}\bm{A}^{\*}(\bm{\eta})=&\frac{\bm{D}(\bm{\gamma})^{-1}\bm{1}\bm{1}^{\top}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\bm{D}(\bm{1}-\bm{p}^{\*}(\bm{\eta}))+k\left(\bm{I}\_{n}-\frac{\bm{D}(\bm{\gamma})^{-1}\bm{1}\bm{1}^{\top}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\right)\bm{D}(\bm{1}-\bm{p}^{\*}(\bm{\eta}))\bm{\mu}\bm{\mu}^{\top}\bm{\Sigma}^{-1},\\ \bm{p}^{\*}(\bm{\eta})=&\ \bm{1}-\bm{M}^{-1}\bm{D}(\bm{\mu})\bm{\eta}.\end{split} | |  | (18) |

In addition, if

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑m≠i(σi​m−k​μi​μm)+∑j=1nγj−1<μi​ηi<−∑m≠i(k​μi​μm−σi​m)+∑j=1nγj−1+k​μi2​γi+σi2−k​μi2∑j=1nγj−1,\displaystyle{\frac{\sum\_{m\neq i}(\sigma\_{im}-k\mu\_{i}\mu\_{m})\_{+}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}<\mu\_{i}\eta\_{i}<-\frac{\sum\_{m\neq i}(k\mu\_{i}\mu\_{m}-\sigma\_{im})\_{+}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}+k\mu\_{i}^{2}\gamma\_{i}+\frac{\sigma\_{i}^{2}-k\mu\_{i}^{2}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}},} |  | (19) |

then we have 𝐩∗​(𝛈)∈(0,1)n\bm{p}^{\*}(\bm{\eta})\in(0,1)^{n}.

Proof. 
It follows from an argument similar to the proof of Proposition [3.3](https://arxiv.org/html/2602.14223v1#S3.Thmtheorem3 "Proposition 3.3. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") in Appendix [B](https://arxiv.org/html/2602.14223v1#A2 "Appendix B Proof of Proposition 3.3 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
 ∎

Examining the form of 𝒑∗​(𝜼)\bm{p}^{\*}(\bm{\eta}) and Condition ([19](https://arxiv.org/html/2602.14223v1#S4.E19 "In Proposition 4.4. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) entails a bound on the loading factor 𝜼\bm{\eta}. Economically, this implies that reinsurance contracts must be priced within a moderate range: excessively high loadings lead to zero reinsurance, while overly low loadings induce full risk transfer.

### 4.3 Solution to the reinsurer’s leader problem

We then solve the leader’s problem.
Using Proposition [4.4](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem4 "Proposition 4.4. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"), Problem ([17](https://arxiv.org/html/2602.14223v1#S4.E17 "In 4.1.2 Reinsurer’s leader problem ‣ 4.1 Problem formulation ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) can be transformed into:

|  |  |  |  |
| --- | --- | --- | --- |
|  | min𝜼⁡γR2​𝒑⊤​𝚺​𝒑−(𝑫​(𝝁)​𝜼)⊤​𝒑s.t. ​𝒑=𝟏−𝑴−1​𝑫​(𝝁)​𝜼.\min\_{\bm{\eta}}\frac{\gamma\_{R}}{2}\bm{p}^{\top}\bm{\Sigma}\bm{p}-(\bm{D}(\bm{\mu})\bm{\eta})^{\top}\bm{p}\quad\text{s.t. }\bm{p}=\bm{1}-\bm{M}^{-1}\bm{D}(\bm{\mu})\bm{\eta}. |  | (20) |

The following proposition gives the optimal loading factor to Problem ([20](https://arxiv.org/html/2602.14223v1#S4.E20 "In 4.3 Solution to the reinsurer’s leader problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")).

###### Proposition 4.5.

The optimal safety loading of Problem ([20](https://arxiv.org/html/2602.14223v1#S4.E20 "In 4.3 Solution to the reinsurer’s leader problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜼∗:=𝑫​(𝝁)−1​𝑴​(γR​𝚺+2​𝑴)−1​(γR​𝚺+𝑴)​𝟏.\bm{\eta}^{\*}:=\bm{D}(\bm{\mu})^{-1}\bm{M}(\gamma\_{R}\bm{\Sigma}+2\bm{M})^{-1}(\gamma\_{R}\bm{\Sigma}+\bm{M})\bm{1}. |  | (21) |

Moreover, suppose that 𝐌\bm{M} and 𝚺\bm{\Sigma} are strictly diagonally dominant, i.e., δ𝐌:=mini∈{1,…,n}⁡(Mi​i−∑j≠i|Mi​j|)>0\delta\_{\bm{M}}:=\min\_{i\in\{1,\ldots,n\}}(M\_{ii}-\sum\_{j\neq i}|M\_{ij}|)>0, δ𝚺:=mini∈{1,…,n}⁡(σi​i−∑j≠i|σi​j|)>0\delta\_{\bm{\Sigma}}:=\min\_{i\in\{1,\ldots,n\}}(\sigma\_{ii}-\sum\_{j\neq i}|\sigma\_{ij}|)>0, where Mi​jM\_{ij} denotes the (i,j)(i,j)-th entry of 𝐌\bm{M}, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ𝑴+γR2​δ𝚺≥γR2​‖𝚺‖∞22​(2​δ𝑴+γR​δ𝚺),\delta\_{\bm{M}}+\frac{\gamma\_{R}}{2}\delta\_{\bm{\Sigma}}\geq\frac{\gamma\_{R}^{2}\|\bm{\Sigma}\|\_{\infty}^{2}}{2(2\delta\_{\bm{M}}+\gamma\_{R}\delta\_{\bm{\Sigma}})}, |  | (22) |

∥⋅∥∞\|\cdot\|\_{\infty} denotes the infinity-norm of a square matrix. Then, 𝛈∗≥𝟎\bm{\eta}^{\*}\geq\bm{0}.

Proof. 
See Appendix [I](https://arxiv.org/html/2602.14223v1#A9 "Appendix I Proof of Proposition 4.5 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
 ∎

###### Remark 4.6.

The condition ([22](https://arxiv.org/html/2602.14223v1#S4.E22 "In Proposition 4.5. ‣ 4.3 Solution to the reinsurer’s leader problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) implies an entry-wise lower bound on the optimal safety loading 𝛈∗\bm{\eta}^{\*}. In Appendix [L](https://arxiv.org/html/2602.14223v1#A12 "Appendix L A Discussion on Condition (19) ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"), we invoke the idea of the proof of the non-negativity of 𝛈∗\bm{\eta}^{\*} and establish an upper bound on 𝛈∗\bm{\eta}^{\*}. This also provides a way to verify ([19](https://arxiv.org/html/2602.14223v1#S4.E19 "In Proposition 4.4. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) under the reinsurer’s optimal strategy, which requires substituting 𝛈∗\bm{\eta}^{\*} into the constraints. In particular, when γR=0\gamma\_{R}=0, ([19](https://arxiv.org/html/2602.14223v1#S4.E19 "In Proposition 4.4. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) is equivalent to, for i=1,…,ni=1,\dots,n,

|  |  |  |  |
| --- | --- | --- | --- |
|  | k​μi2​γi+σi2−k​μi2∑j=1nγj−1>∑j≠i|σi​j−k​μi​μj|∑j=1nγj−1.k\mu\_{i}^{2}\gamma\_{i}+\frac{\sigma\_{i}^{2}-k\mu\_{i}^{2}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}>\frac{\sum\_{j\neq i}|\sigma\_{ij}-k\mu\_{i}\mu\_{j}|}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}. |  | (23) |

### 4.4 Bowley optimum

With the optimal risk allocation in Proposition [4.4](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem4 "Proposition 4.4. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") and the optimal loading in Proposition [4.5](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem5 "Proposition 4.5. ‣ 4.3 Solution to the reinsurer’s leader problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"), we have a candidate for the desired Bowley optimum.
Following Definition [4.2](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem2 "Definition 4.2. ‣ 4.1.2 Reinsurer’s leader problem ‣ 4.1 Problem formulation ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"), the next step is to check the individual rationality of all agents, shown in the following statement.

###### Lemma 4.7.

Under the contract (𝐀∗​(𝛈∗),𝐩∗​(𝛈∗),𝛈∗)(\bm{A}^{\*}(\bm{\eta}^{\*}),\bm{p}^{\*}(\bm{\eta}^{\*}),\bm{\eta}^{\*}) given by Propositions [4.4](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem4 "Proposition 4.4. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") and [4.5](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem5 "Proposition 4.5. ‣ 4.3 Solution to the reinsurer’s leader problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"), the reinsurer’s welfare gain is given by

|  |  |  |
| --- | --- | --- |
|  | ωR​(𝑨∗​(𝜼∗),𝒑∗​(𝜼∗),𝜼∗)=12​𝟏⊤​(γR​𝑴−1​𝚺​𝑴−1+2​𝑴−1)−1​𝟏>0.\omega\_{R}(\bm{A}^{\*}(\bm{\eta}^{\*}),\bm{p}^{\*}(\bm{\eta}^{\*}),\bm{\eta}^{\*})=\frac{1}{2}\bm{1}^{\top}\left(\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}\bm{M}^{-1}+2\bm{M}^{-1}\right)^{-1}\bm{1}>0. |  |

In addition, the members’ IRs are fulfilled provided that 𝛈∗\bm{\eta}^{\*} satisfies ([19](https://arxiv.org/html/2602.14223v1#S4.E19 "In Proposition 4.4. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), and the following holds for i=1,…,ni=1,\dots,n:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | γi2​(σi2−(γi−1∑j=1nγj−1)2​∑j,l=1n(σj​l)+−3​k​μi2)+∑m≠i(k​μi​μm−σi​m)++k​μi2−σi2∑j=1nγj−1≥0.\displaystyle\ \ \ \ \frac{\gamma\_{i}}{2}\left(\sigma\_{i}^{2}-\left(\frac{\gamma\_{i}^{-1}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\right)^{2}\sum\_{j,l=1}^{n}(\sigma\_{jl})\_{+}-3k\mu\_{i}^{2}\right)+\frac{\sum\_{m\neq i}(k\mu\_{i}\mu\_{m}-\sigma\_{im})\_{+}+k\mu\_{i}^{2}-\sigma\_{i}^{2}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\geq 0. |  | (24) |

Proof. 
See Appendix [J](https://arxiv.org/html/2602.14223v1#A10 "Appendix J Proof of Lemma 4.7 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
 ∎

Synthesizing the solutions to two sequentially-linked sub-problems and the IR analysis, we characterize the Bowley optimum as follows.

###### Theorem 4.8.

Suppose that Conditions ([19](https://arxiv.org/html/2602.14223v1#S4.E19 "In Proposition 4.4. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) and ([24](https://arxiv.org/html/2602.14223v1#S4.E24 "In Lemma 4.7. ‣ 4.4 Bowley optimum ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) are fulfilled. Let (𝐀∗​(𝛈∗),𝐩∗​(𝛈∗),𝛈∗)(\bm{A}^{\*}(\bm{\eta}^{\*}),\bm{p}^{\*}(\bm{\eta}^{\*}),\bm{\eta}^{\*}) be given in ([18](https://arxiv.org/html/2602.14223v1#S4.E18 "In Proposition 4.4. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) and ([21](https://arxiv.org/html/2602.14223v1#S4.E21 "In Proposition 4.5. ‣ 4.3 Solution to the reinsurer’s leader problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")). Then, (𝐀∗​(𝛈∗),𝐩∗​(𝛈∗),𝛈∗)(\bm{A}^{\*}(\bm{\eta}^{\*}),\bm{p}^{\*}(\bm{\eta}^{\*}),\bm{\eta}^{\*}) is Bowley-optimal.

Proof. 
It follows directly from Proposition [4.4](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem4 "Proposition 4.4. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"), Proposition [4.5](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem5 "Proposition 4.5. ‣ 4.3 Solution to the reinsurer’s leader problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"), and Lemma [4.7](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem7 "Lemma 4.7. ‣ 4.4 Bowley optimum ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
 ∎

The following corollary characterizes the optimal loading when the reinsurer is not allowed to set different prices for members in the pool.

###### Corollary 4.9.

With the single-loading restriction, i.e., 𝛈=η​𝟏\bm{\eta}=\eta\bm{1}, the optimal safety loading of Problem ([20](https://arxiv.org/html/2602.14223v1#S4.E20 "In 4.3 Solution to the reinsurer’s leader problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | η∗=𝝁⊤​(𝑰n+γR​𝑴−1​𝚺)​𝟏𝝁⊤​(2​𝑴−1+γR​𝑴−1​𝚺​𝑴−1)​𝝁.\eta^{\*}=\frac{\bm{\mu}^{\top}(\bm{I}\_{n}+\gamma\_{R}\bm{M}^{-1}\bm{\Sigma})\bm{1}}{\bm{\mu}^{\top}(2\bm{M}^{-1}+\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}\bm{M}^{-1})\bm{\mu}}. |  | (25) |

Assume further that Conditions ([19](https://arxiv.org/html/2602.14223v1#S4.E19 "In Proposition 4.4. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) and ([24](https://arxiv.org/html/2602.14223v1#S4.E24 "In Lemma 4.7. ‣ 4.4 Bowley optimum ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) are fulfilled; then (𝐀∗​(η∗​𝟏),𝐩∗​(η∗​𝟏),η∗​𝟏)(\bm{A}^{\*}(\eta^{\*}\bm{1}),\bm{p}^{\*}(\eta^{\*}\bm{1}),\eta^{\*}\bm{1}) is the Bowley-optimal contract. In addition, if 𝐌\bm{M} is strictly diagonally dominant and γR≤δ𝐌/‖𝚺‖∞\gamma\_{R}\leq\delta\_{\bm{M}}/\|\bm{\Sigma}\|\_{\infty},
then η∗≥0\eta^{\*}\geq 0.

Proof. 
See Appendix [K](https://arxiv.org/html/2602.14223v1#A11 "Appendix K Proof of Corollary 4.9 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
 ∎

###### Remark 4.10 (On including individual rationality constraints in optimizations).

For mathematical tractability, we do not directly include two IR constraints ([3](https://arxiv.org/html/2602.14223v1#S2.E3 "In 2.3 Individual rationality ‣ 2 Model Formulations ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) and ([4](https://arxiv.org/html/2602.14223v1#S2.E4 "In 2.3 Individual rationality ‣ 2 Model Formulations ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) in the optimization problems ([16](https://arxiv.org/html/2602.14223v1#S4.E16 "In 4.1.1 Plan manager’s follower problem ‣ 4.1 Problem formulation ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) and ([17](https://arxiv.org/html/2602.14223v1#S4.E17 "In 4.1.2 Reinsurer’s leader problem ‣ 4.1 Problem formulation ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), respectively. We nonetheless note that both conditions can be added to the leader’s problem ([17](https://arxiv.org/html/2602.14223v1#S4.E17 "In 4.1.2 Reinsurer’s leader problem ‣ 4.1 Problem formulation ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), yielding a convex minimization problem that is solvable. However, a closed-form solution is not available in this case, and one must rely on numerical optimization solvers.

### 4.5 Comparison of Bowley and Pareto optima

We provide a brief comparison between the Bowley-optimal contract (𝑨∗​(𝜼∗),𝒑∗​(𝜼∗),𝜼∗)(\bm{A}^{\*}(\bm{\eta}^{\*}),\bm{p}^{\*}(\bm{\eta}^{\*}),\bm{\eta}^{\*}) and a JP-optimal contract (𝑨∗,𝒑∗,𝜼∗)(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*}). Despite the flexibility of setting 𝜼∗\bm{\eta}\_{\*} in the JP-optimal contracts (see the discussion in Section [3.1](https://arxiv.org/html/2602.14223v1#S3.SS1 "3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")),
we shall show that a Bowley-optimal contract is never JP-optimal.

###### Proposition 4.11.

The Bowley-optimal contract (𝐀∗​(𝛈∗),𝐩∗​(𝛈∗),𝛈∗)(\bm{A}^{\*}(\bm{\eta}^{\*}),\bm{p}^{\*}(\bm{\eta}^{\*}),\bm{\eta}^{\*}) in Theorem [4.8](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem8 "Theorem 4.8. ‣ 4.4 Bowley optimum ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") is not JP-optimal.

Proof. 
By direct calculation, 𝒑∗​(𝜼∗)=(γR​𝚺+2​𝑴)−1​𝑴​𝟏≠(γR​𝚺+𝑴)−1​𝑴​𝟏=𝒑∗\bm{p}^{\*}(\bm{\eta}^{\*})=(\gamma\_{R}\bm{\Sigma}+2\bm{M})^{-1}\bm{M}\bm{1}\neq(\gamma\_{R}\bm{\Sigma}+\bm{M})^{-1}\bm{M}\bm{1}=\bm{p}\_{\*},
as 𝑴\bm{M} is not a zero matrix according to Lemma [4.3](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem3 "Lemma 4.3. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"). As 𝒑∗​(𝜼∗)≠𝒑∗\bm{p}^{\*}(\bm{\eta}^{\*}){\neq}\bm{p}\_{\*}, the Bowley-optimal contract does not solve Problem ([5](https://arxiv.org/html/2602.14223v1#S3.E5 "In 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) and thus not JP-optimal according to Theorem [3.4](https://arxiv.org/html/2602.14223v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"),
 ∎

Proposition [4.11](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem11 "Proposition 4.11. ‣ 4.5 Comparison of Bowley and Pareto optima ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") asserts that the Bowley optimum is inefficient in terms of JP optimality.
This stands in contrast to Boonen and Ghossoub ([2023](https://arxiv.org/html/2602.14223v1#bib.bib11 "Bowley vs. Pareto optima in reinsurance contracting")), who study a two-agent Bowley optimum under convex and comonotonic additive risk measures. In contrast, our focus is on a multi-agent problem with mean-variance-premium objectives for the followers, which are non-convex in the contract variables and not comonotonic-additive. Our result echoes a similar finding in Jiang et al. ([2025](https://arxiv.org/html/2602.14223v1#bib.bib12 "Bowley solution of a variance game in insurance")) that the two-agent Bowley optimum is not Pareto efficient under the generalized mean-variance setting.

In addition, due to the inefficiency of the Bowley optimum, we can also assert that it achieves smaller total welfare gains for all agents compared to the JP-optimal counterpart, summarized in the following corollary.

###### Corollary 4.12.

Let (A∗​(𝛈∗),𝐩∗​(𝛈∗),𝛈∗)(A^{\*}(\bm{\eta}^{\*}),\bm{p}^{\*}(\bm{\eta}^{\*}),\bm{\eta}^{\*}) be the Bowley-optimal contract given by ([18](https://arxiv.org/html/2602.14223v1#S4.E18 "In Proposition 4.4. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) and ([31](https://arxiv.org/html/2602.14223v1#A3.E31 "In Appendix C Proof of Theorem 3.4 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), and let (𝐀∗,𝐩∗,𝛈∗)(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*}) be a JP-optimal contract. Then, ∑i∈𝒩ωi​(𝐀∗​(𝛈∗),𝐩∗​(𝛈∗),𝛈∗)<∑i∈𝒩ωi​(𝐀∗,𝐩∗,𝛈∗)\sum\_{i\in\mathcal{N}}\omega\_{i}(\bm{A}^{\*}(\bm{\eta}^{\*}),\bm{p}^{\*}(\bm{\eta}^{\*}),\bm{\eta}^{\*})<\sum\_{i\in\mathcal{N}}\omega\_{i}(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*}).

Proof. 
It follows directly from the observation that (𝑨∗,𝒑∗)(\bm{A}^{\*},\bm{p}^{\*}) is admissible and suboptimal (see Proposition [4.11](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem11 "Proposition 4.11. ‣ 4.5 Comparison of Bowley and Pareto optima ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) in Problem ([5](https://arxiv.org/html/2602.14223v1#S3.E5 "In 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")).
 ∎

Overall, the issues of inefficiency and welfare loss, respectively revealed in Proposition [4.11](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem11 "Proposition 4.11. ‣ 4.5 Comparison of Bowley and Pareto optima ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") and Corollary [4.12](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem12 "Corollary 4.12. ‣ 4.5 Comparison of Bowley and Pareto optima ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"), raise concerns about adopting the Bowley design with the monopolistic reinsurer. Importantly,
the implication from Corollary [4.12](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem12 "Corollary 4.12. ‣ 4.5 Comparison of Bowley and Pareto optima ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")
should not be interpreted as a blanket rejection of Bowley-type contracting as it is more realistic in the practical business models. In our setting, the Pareto design corresponds to full cooperation and thus serves as an upper benchmark, whereas the Bowley design represents the opposite extreme of unilateral pricing power. This motivates further study of intermediate market structures—for example, Nash-bargaining-based contract composition (Boonen, [2016](https://arxiv.org/html/2602.14223v1#bib.bib39 "Nash equilibria of over-the-counter bargaining for insurance risk redistributions: the role of a regulator")) and structures with multiple reinsurers (Cao et al., [2023](https://arxiv.org/html/2602.14223v1#bib.bib43 "Reinsurance games with two reinsurers: tree versus chain")).

## 5 Numerical Illustration and Welfare Analysis

In this section, we present numerical results to demonstrate our findings and conduct a welfare comparison across different contracts. In addition, we carry out a comparative statics analysis on the reinsurer’s risk aversion γR\gamma\_{R}.
Baseline parameters are shown as follows: we consider a three-member case, where

|  |  |  |
| --- | --- | --- |
|  | 𝒩={1,2,3,R},γR=0.01,𝝁=(10012585),𝚺=(10000−1200720−1200144006487206488100),𝜸=(0.0150.0250.02).\mathcal{N}=\{1,2,3,R\},\quad\gamma\_{R}=0.01,\quad\bm{\mu}=\begin{pmatrix}100\\ 125\\ 85\end{pmatrix},\quad\bm{\Sigma}=\begin{pmatrix}10000&-1200&720\\ -1200&14400&648\\ 720&648&8100\end{pmatrix},\quad\bm{\gamma}=\begin{pmatrix}0.015\\ 0.025\\ 0.02\end{pmatrix}. |  |

In this profile, Member 2 faces the riskiest loss, with the highest expected loss and variance, whereas Member 3 faces the least risky loss. Among the three members, Member 1 is the least risk averse, followed by Member 3.

### 5.1 Baseline contracts

From the baseline setting, we compose the following five contracts:

* •

  No-reinsurer case 𝑨0\bm{A}\_{0}
* •

  JPO1 (𝑨∗,𝒑∗,𝜼∗)(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*}): JP-optimal contract
* •

  JPO2 (𝑨∗,𝒑∗,η∗​𝟏)(\bm{A}\_{\*},\bm{p}\_{\*},\eta\_{\*}\bm{1}): JP-optimal contract with the single-loading restriction
* •

  BO1 (𝑨∗​(𝜼∗),𝒑∗​(𝜼∗),𝜼∗)(\bm{A}^{\*}(\bm{\eta}^{\*}),\bm{p}^{\*}(\bm{\eta}^{\*}),\bm{\eta}^{\*}): Bowley-optimal contract
* •

  BO2 (𝑨∗​(η∗​𝟏),𝒑∗​(η∗​𝟏),η∗​𝟏)(\bm{A}^{\*}(\eta^{\*}\bm{1}),\bm{p}^{\*}(\eta^{\*}\bm{1}),\eta^{\*}\bm{1}): Bowley-optimal contract with the single-loading restriction

Below, we discuss each component in the contract triplet and related figures.

#### 5.1.1 Construction of JP-optimal contracts and safety loadings

Safety loadings of the Bowley-optimal contracts can be calculated explicitly; see ([21](https://arxiv.org/html/2602.14223v1#S4.E21 "In Proposition 4.5. ‣ 4.3 Solution to the reinsurer’s leader problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) and ([25](https://arxiv.org/html/2602.14223v1#S4.E25 "In Corollary 4.9. ‣ 4.4 Bowley optimum ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) for the closed-form formulae. However, this is not the case for Pareto designs, which allow the plan manager and reinsurer to jointly devise the safety loadings. As such, we select the premiums for the JPO1 and JPO2 contracts so that they respectively Pareto-dominate the BO1 and BO2 contracts, as follows.

According to Corollary [4.12](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem12 "Corollary 4.12. ‣ 4.5 Comparison of Bowley and Pareto optima ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"), JP-optimal contracts always result in greater total welfare gains for the community. Utilizing the freedom of distributing the total welfare among members and the reinsurer in the Pareto design, we equally redistribute these extra welfare gains among them and derive 𝜼∗\bm{\eta}\_{\*} in the JPO1 contract. Mathematically, whenever 𝒑∗≥𝟎\bm{p}\_{\*}\geq\bm{0}, we determine 𝜼∗\bm{\eta}\_{\*} by solving

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ωi​(𝑨∗,𝒑∗,𝜼∗)=ωi​(𝑨∗​(𝜼∗),𝒑∗​(𝜼∗),𝜼∗)+ρR​(𝒑∗)−ρR​(𝒑∗​(𝜼∗))+∑i=1n(ρi​(𝑨∗)−ρi​(𝑨∗​(𝜼∗)))|𝒩|,\displaystyle\omega\_{i}(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*})=\omega\_{i}(\bm{A}^{\*}(\bm{\eta}^{\*}),\bm{p}^{\*}(\bm{\eta}^{\*}),\bm{\eta}^{\*})+\frac{\rho\_{R}(\bm{p}\_{\*})-\rho\_{R}(\bm{p}^{\*}(\bm{\eta}^{\*}))+\sum\_{i=1}^{n}(\rho\_{i}(\bm{A}\_{\*})-\rho\_{i}(\bm{A}^{\*}(\bm{\eta}^{\*})))}{|\mathcal{N}|}, |  | (26) |

for all i∈𝒩i\in\mathcal{N}.
We also verify that the resulting vector of welfare gains lies in the core; see Equation ([12](https://arxiv.org/html/2602.14223v1#S3.E12 "In 3.2.1 Coalitional stability and the core ‣ 3.2 Cooperative game study on premium decision ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")). Therefore, the JPO contracts are also coalitionally stable.

For η∗\eta\_{\*} in the JPO2 contract, we follow a similar scheme by redistributing the welfare gains. However, due to the single-loading restriction, we cannot, in general, equally split the extra welfare gains among agents while satisfying the coalitional stability criteria. Instead, we search for welfare gains induced by the single loading η∗\eta\_{\*} of the JP-optimal contract in the core that Pareto-dominates the BO2 contract. Mathematically, we look for η∗≥0\eta\_{\*}\geq 0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ωi​(𝑨∗,𝒑∗,η∗​𝟏))i∈𝒩∈\displaystyle\left(\omega\_{i}(\bm{A}\_{\*},\bm{p}\_{\*},\eta\_{\*}\bm{1})\right)\_{i\in\mathcal{N}}\in | {𝒄:𝒄∈c​o​r​e​(𝒩,ℬ),ci≥ωi​(𝑨∗​(η∗​𝟏),𝒑∗​(η∗​𝟏),η∗​𝟏)​ for all ​i∈𝒩}.\displaystyle\{\bm{c}:\bm{c}\in core(\mathcal{N},\mathcal{B}),\ c\_{i}\geq\omega\_{i}(\bm{A}^{\*}(\eta^{\*}\bm{1}),\bm{p}^{\*}(\eta^{\*}\bm{1}),\eta^{\*}\bm{1})\text{ for all }i\in\mathcal{N}\}. |  |

Note that in general, there is no unique solution for this search, and we thus select one particular choice to construct the JPO2 contract.

| Contracts\Safety loading | η1\eta\_{1} | η2\eta\_{2} | η3\eta\_{3} |
| --- | --- | --- | --- |
| JPO1 | 0.313589 | 0.678401 | 0.404502 |
| JPO2 | 0.4395 | | |
| BO1 | 0.345775 | 0.725918 | 0.460025 |
| BO2 | 0.495050 | | |

Table 1: Safety loadings under the baseline contracts.

The computed safety loadings of all contracts are summarized in Table [1](https://arxiv.org/html/2602.14223v1#S5.T1 "Table 1 ‣ 5.1.1 Construction of JP-optimal contracts and safety loadings ‣ 5.1 Baseline contracts ‣ 5 Numerical Illustration and Welfare Analysis ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"). All loadings are positive, and the loadings of the two contracts (JPO2/BO2) with the single-loading restriction are located around the average of safety loadings in the corresponding unrestricted contracts (JPO1/BO1). In line with general intuition, members with larger expected losses and higher loss variances are charged higher loadings in both the JPO1 and BO1 contracts, with Member 2 facing the highest loading. In addition, the loading for Member 2 is reduced under the single-loading restriction, which is balanced by higher loadings for Members 1 and 3. Comparing the corresponding contracts across the two designs, we observe that the higher loadings are set under the Bowley design, as the reinsurer, acting as the leader, can leverage its first-mover advantage when determining the premium.

#### 5.1.2 Reinsurance strategies

| Contracts \Reinsurance | p1p\_{1} | p2p\_{2} | p3p\_{3} |
| --- | --- | --- | --- |
| JPO1 and JPO2 | 0.357528 | 0.473022 | 0.364981 |
| BO1 | 0.265399 | 0.378127 | 0.269785 |
| BO2 | 0.148915 | 0.445595 | 0.244199 |

Table 2: Comparison of reinsurance strategies among contracts.

Table [2](https://arxiv.org/html/2602.14223v1#S5.T2 "Table 2 ‣ 5.1.2 Reinsurance strategies ‣ 5.1 Baseline contracts ‣ 5 Numerical Illustration and Welfare Analysis ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") depicts all members’ reinsurance strategies in different contracts. The reinsurance strategies are the same for JPO1 and JPO2, since under the Pareto design, the risk transfer is independent of the safety loadings. In general, the Pareto design leads to higher reinsurance levels for all members compared to the Bowley design. This is because the reinsurer cooperates with the manager and internalizes members’ risk-sharing benefits, thereby allowing more effective risk management. For all but Member 2, the next highest levels occur under the BO1 contract, since her safety loading decreases substantially when moving from BO1 to BO2, while the other members’ loadings increase (see Table [1](https://arxiv.org/html/2602.14223v1#S5.T1 "Table 1 ‣ 5.1.1 Construction of JP-optimal contracts and safety loadings ‣ 5.1 Baseline contracts ‣ 5 Numerical Illustration and Welfare Analysis ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")).

#### 5.1.3 Risk allocation matrices

| i\ji\backslash j | 1 | 2 | 3 |
| --- | --- | --- | --- |
| 1 | 0.223266 | 0.180385 | 0.227910 |
| 2 | 0.231155 | 0.193278 | 0.218787 |
| 3 | 0.188050 | 0.153314 | 0.188321 |

(a) JPO1 and JPO2 𝑨∗\bm{A}\_{\*}

| i\ji\backslash j | 1 | 2 | 3 |
| --- | --- | --- | --- |
| 1 | 0.312006 | 0.326195 | 0.329707 |
| 2 | 0.418419 | 0.298033 | 0.392988 |
| 3 | 0.269576 | 0.275772 | 0.277305 |

(b) No-reinsurer case 𝑨0\bm{A}\_{0}

| i\ji\backslash j | 1 | 2 | 3 |
| --- | --- | --- | --- |
| 1 | 0.239741 | 0.226409 | 0.249234 |
| 2 | 0.290250 | 0.263952 | 0.273118 |
| 3 | 0.204610 | 0.191511 | 0.207863 |

(c) BO1 𝑨∗​(𝜼∗)\bm{A}^{\*}(\bm{\eta}^{\*})

| i\ji\backslash j | 1 | 2 | 3 |
| --- | --- | --- | --- |
| 1 | 0.333939 | 0.211219 | 0.297793 |
| 2 | 0.265230 | 0.183491 | 0.233428 |
| 3 | 0.251918 | 0.159696 | 0.224580 |

(d) BO2 𝑨∗​(η∗​𝟏)\bm{A}^{\*}(\eta^{\*}\bm{1})

Table 3: Risk allocations (ai​j)i,j∈{1,2,3}(a\_{ij})\_{i,j\in\{1,2,3\}} of members in different contracts.

Table [3](https://arxiv.org/html/2602.14223v1#S5.T3 "Table 3 ‣ 5.1.3 Risk allocation matrices ‣ 5.1 Baseline contracts ‣ 5 Numerical Illustration and Welfare Analysis ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") presents the risk mutualization of members in all contracts.
Driven by the introduction of the reinsurance option, we observe two key effects. First, the allocation matrix 𝑨0\bm{A}\_{0} has the highest values in all entries, followed by 𝑨∗​(𝜼∗)\bm{A}^{\*}(\bm{\eta}^{\*}) and then 𝑨∗\bm{A}\_{\*}.
This follows from the ordering of the corresponding reinsurance strategies, i.e., 𝟎<𝒑∗​(𝜼∗)<𝒑∗\bm{0}<\bm{p}^{\*}(\bm{\eta}^{\*})<\bm{p}\_{\*}
(cf. Table [2](https://arxiv.org/html/2602.14223v1#S5.T2 "Table 2 ‣ 5.1.2 Reinsurance strategies ‣ 5.1 Baseline contracts ‣ 5 Numerical Illustration and Welfare Analysis ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")). This is consistent with the intuition that members need to carry more risk from each other with fewer risk transfers.

For the BO2 contract where the single-loading restriction is imposed, the entries of 𝑨​(η∗​𝟏)\bm{A}(\eta^{\*}\bm{1}) exhibit greater dispersion compared to other allocation matrices. In particular, a11a\_{11} in 𝑨​(η∗​𝟏)\bm{A}(\eta^{\*}\bm{1}) is the highest among all contracts, whereas a22a\_{22} is the smallest.
The reasons are twofold. First, the lower premium payment incentivizes Member 2 to transfer a large portion of risk to the reinsurer. Consequently, she bears a smaller proportion of losses for others due to the actuarial fairness condition. As such, Member 1 must retain more risk in her own house. Second, for Member 1, the premium is substantially higher in the BO2
contract than in the other designs, making the reinsurance option less appealing and thereby increasing her retained loss.

#### 5.1.4 Welfare analysis

In this subsection, we compare the induced welfare of all agents and analyze the attribution of welfare improvements with respect to the premium and mean-variance disutility components.

| Contracts \Premium | π1​(η1,p1)\pi\_{1}(\eta\_{1},p\_{1}) | π2​(η2,p2)\pi\_{2}(\eta\_{2},p\_{2}) | π3​(η3,p3)\pi\_{3}(\eta\_{3},p\_{3}) | Total premium payment |
| --- | --- | --- | --- | --- |
| JPO1 | 46.9654 | 99.2401 | 43.5725 | 189.777 |
| JPO2 | 51.4662 | 85.1144 | 44.6582 | 181.239 |
| BO1 | 35.7167 | 68.6327 | 33.4809 | 137.830 |
| BO2 | 22.2633 | 83.2733 | 31.0327 | 136.569 |

Table 4: Comparison of premium payment among contracts.

Table [4](https://arxiv.org/html/2602.14223v1#S5.T4 "Table 4 ‣ 5.1.4 Welfare analysis ‣ 5.1 Baseline contracts ‣ 5 Numerical Illustration and Welfare Analysis ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") reports the members’ premium payments under different contracts, showing that members pay higher premiums under the JP-optimal contracts. With lower safety loadings in the JPO contracts (see Table [1](https://arxiv.org/html/2602.14223v1#S5.T1 "Table 1 ‣ 5.1.1 Construction of JP-optimal contracts and safety loadings ‣ 5.1 Baseline contracts ‣ 5 Numerical Illustration and Welfare Analysis ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), members are incentivized to increase their reinsurance purchases (see Table [2](https://arxiv.org/html/2602.14223v1#S5.T2 "Table 2 ‣ 5.1.2 Reinsurance strategies ‣ 5.1 Baseline contracts ‣ 5 Numerical Illustration and Welfare Analysis ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")). Overall, the higher reinsurance volumes offset the lower unit premiums, resulting in higher total premium payments.
Consequently, the reinsurer receives higher premium income when engaging in the JP-optimal contracts.

| Contracts \Mean-variance disutility | ρ1​(𝑨,𝒑)\rho\_{1}(\bm{A},\bm{p}) | ρ2​(𝑨,𝒑)\rho\_{2}(\bm{A},\bm{p}) | ρ3​(𝑨,𝒑)\rho\_{3}(\bm{A},\bm{p}) | ρR​(𝒑)\rho\_{R}(\bm{p}) |
| --- | --- | --- | --- | --- |
| Status quo | 175 | 305 | 166 | 0 |
| No-reinsurer case | 125.721 | 191.536 | 109.730 | N/A |
| JPO1 and JPO2 | 74.9797 | 84.3771 | 63.9625 | 153.829 |
| BO1 | 87.2974 | 116.154 | 75.2239 | 103.052 |
| BO2 | 104.094 | 90.0197 | 78.6610 | 109.338 |

Table 5: Mean-variance disutilities among agents in different contracts.

Table [5](https://arxiv.org/html/2602.14223v1#S5.T5 "Table 5 ‣ 5.1.4 Welfare analysis ‣ 5.1 Baseline contracts ‣ 5 Numerical Illustration and Welfare Analysis ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") reports the mean-variance disutilities for all agents, which indicate the level of risk borne by each agent.
We note that
including the reinsurance layer
yields a substantially greater risk reduction for all members than in the case without reinsurance. As the mean-variance disutilities attain their minimum in JP-optimal contracts, this indicates better risk sharing among agents in the full-cooperation framework.
Juxtaposing the two Bowley-optimal contracts in Table [5](https://arxiv.org/html/2602.14223v1#S5.T5 "Table 5 ‣ 5.1.4 Welfare analysis ‣ 5.1 Baseline contracts ‣ 5 Numerical Illustration and Welfare Analysis ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") reflects the impact of the single-loading restriction. As Member 2 cedes more risk in the BO2 contract (see Table [2](https://arxiv.org/html/2602.14223v1#S5.T2 "Table 2 ‣ 5.1.2 Reinsurance strategies ‣ 5.1 Baseline contracts ‣ 5 Numerical Illustration and Welfare Analysis ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), she faces a lower mean-variance disutility. Note that similar arguments can be made to explain why Members 1 and 3 instead bear more risk in the BO2 contract.

|  | ω1​(𝑨,𝒑,𝜼)\omega\_{1}(\bm{A},\bm{p},\bm{\eta}) | ω2​(𝑨,𝒑,𝜼)\omega\_{2}(\bm{A},\bm{p},\bm{\eta}) | ω3​(𝑨,𝒑,𝜼)\omega\_{3}(\bm{A},\bm{p},\bm{\eta}) | ωR​(𝑨,𝒑,𝜼)\omega\_{R}(\bm{A},\bm{p},\bm{\eta}) | Total welfare gains |
| --- | --- | --- | --- | --- | --- |
| No-reinsurer case | 49.2790 | 113.464 | 56.2696 | N/A | 219.012 |
| JPO1 | 53.1558 | 121.383 | 58.4651 | 35.9478 | 268.951 |
| JPO2 | 48.6541 | 135.508 | 57.3793 | 27.4096 |
| BO1 | 51.9859 | 120.213 | 57.2952 | 34.7780 | 264.272 |
| BO2 | 48.6430 | 131.707 | 56.3063 | 27.2311 | 263.888 |

Table 6: Welfare gains among contracts.

Table [6](https://arxiv.org/html/2602.14223v1#S5.T6 "Table 6 ‣ 5.1.4 Welfare analysis ‣ 5.1 Baseline contracts ‣ 5 Numerical Illustration and Welfare Analysis ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") reports the overall welfare gains of agents. Scrutinizing the effect of reinsurance, we note that all figures are much lower in the design without the reinsurer than in those with the reinsurer, highlighting the value of the reinsurance option and thus echoing the finding in Anthropelos et al. ([2026](https://arxiv.org/html/2602.14223v1#bib.bib99 "On the expansion of risk pooling"), Theorem 4) despite a different research focus.

Concerning the effect of the single-loading restriction, under the Bowley design, the total welfare gain of the BO2 contract is smaller than that of the BO1 contract. Indeed, except for Member 2 who benefits substantially from the reduced loading (see Table [1](https://arxiv.org/html/2602.14223v1#S5.T1 "Table 1 ‣ 5.1.1 Construction of JP-optimal contracts and safety loadings ‣ 5.1 Baseline contracts ‣ 5 Numerical Illustration and Welfare Analysis ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), all other agents experience a decline in individual welfare. This suggests that the single-loading restriction primarily benefits members with riskier losses, while failing to improve overall welfare and potentially harming it. In particular, Table [4](https://arxiv.org/html/2602.14223v1#S5.T4 "Table 4 ‣ 5.1.4 Welfare analysis ‣ 5.1 Baseline contracts ‣ 5 Numerical Illustration and Welfare Analysis ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") indicates that the reinsurer’s welfare loss is due to a lower premium income.
A similar effect on the individual welfare is observed when comparing JPO1 and JPO2 contracts, except that the total welfare gain is preserved due to the Pareto design.

Between the two designs, all members and the reinsurer prefer the Pareto design to the Bowley design, with all individual welfare gains being higher under the JPO1 (resp. JPO2) contract than under the BO1 (resp. BO2) contract. The intuition is straightforward: the Pareto design generates a higher total welfare gain by default and, owing to the flexibility in setting the reinsurance premium, the resulting surplus is redistributed among all agents according to ([26](https://arxiv.org/html/2602.14223v1#S5.E26 "In 5.1.1 Construction of JP-optimal contracts and safety loadings ‣ 5.1 Baseline contracts ‣ 5 Numerical Illustration and Welfare Analysis ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")). It is also noteworthy that the reinsurer attains a higher welfare gain under the JP-optimal contracts owing to the fact that the higher premium income more than compensates for the additional risk (see Tables [4](https://arxiv.org/html/2602.14223v1#S5.T4 "Table 4 ‣ 5.1.4 Welfare analysis ‣ 5.1 Baseline contracts ‣ 5 Numerical Illustration and Welfare Analysis ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") and [5](https://arxiv.org/html/2602.14223v1#S5.T5 "Table 5 ‣ 5.1.4 Welfare analysis ‣ 5.1 Baseline contracts ‣ 5 Numerical Illustration and Welfare Analysis ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")).
From the members’ perspective, although they need to pay more under JP-optimal contracts, they are well-compensated with better risk sharing and thus enjoy greater welfare gains.

Consequently, for all agents except Member 2, individual welfare gains are maximized under the JPO1 contract.
By contrast, benefiting from the reduced loading, Member 2 attains the highest welfare gain under the JPO2 contract. Moreover, the asymmetric allocation of welfare toward Member 2 in the JPO2 contract results in lower individual welfare gains for all other agents compared to the JPO1 contract, even though their total welfare is the same. This observation further reinforces the conclusion that the single-loading restriction disproportionately favors high-risk members.

### 5.2 Impact of the reinsurer’s risk aversion

In this subsection, we examine the effect of the reinsurer’s risk aversion γR\gamma\_{R} on members’ reinsurance policies and the total welfare gains across various contracts. Given this focus, we do not consider the construction of coalitionally stable JP-optimal contracts.

#### 5.2.1 Members’ reinsurance policies

![Refer to caption](Graphics/p1vsGammaR.png)


(a) Member 1

![Refer to caption](Graphics/p2vsGammaR.png)


(b) Member 2

![Refer to caption](Graphics/p3vsGammaR.png)


(c) Member 3

Figure 3: Members’ reinsurance strategies of the four contracts with different γR\gamma\_{R}.

Fig. [3](https://arxiv.org/html/2602.14223v1#S5.F3 "Figure 3 ‣ 5.2.1 Members’ reinsurance policies ‣ 5.2 Impact of the reinsurer’s risk aversion ‣ 5 Numerical Illustration and Welfare Analysis ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") displays the members’ reinsurance strategies pip\_{i} against γR\gamma\_{R}.
In general, every pip\_{i} is decreasing in γR\gamma\_{R}. This is consistent with the general intuition that the more risk averse the reinsurer, the less risk she is willing to take. In addition, when γR=0\gamma\_{R}=0, i.e., the reinsurer is risk-neutral, all members adopt full reinsurance in the JP-optimal contracts. This can also be deduced from the form of 𝒑∗\bm{p}\_{\*} given in ([6](https://arxiv.org/html/2602.14223v1#S3.E6 "In Proposition 3.3. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")). Moreover, members cede only a portion of their risks when the reinsurer is risk-neutral. In particular, under the BO1 contract, the reinsurance proportion is always 50%50\% for all members when γR=0\gamma\_{R}=0, which follows directly from ([18](https://arxiv.org/html/2602.14223v1#S4.E18 "In Proposition 4.4. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) and ([21](https://arxiv.org/html/2602.14223v1#S4.E21 "In Proposition 4.5. ‣ 4.3 Solution to the reinsurer’s leader problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")).

Concerning the impact of the single-loading restriction, we note that Member 1’s reinsurance is near zero in the BO2 contract when γR=0.029\gamma\_{R}=0.029.555This also explains the choice of the plotting range.
This indicates that the single-loading restriction can discourage the least risk-averse member from participating in reinsurance protection as the reinsurer becomes more risk averse. Indeed, as noted earlier, this restriction tends to favor members with riskier losses. When γR>0.013\gamma\_{R}>0.013, Member 2 adopts the highest reinsurance level under the BO2 contract, highlighting the extent to which the single-loading restriction enhances her welfare with a more risk-averse reinsurer.

Comparing the three contract designs, we find that the ordering of reinsurance proportions in Fig. [3](https://arxiv.org/html/2602.14223v1#S5.F3 "Figure 3 ‣ 5.2.1 Members’ reinsurance policies ‣ 5.2 Impact of the reinsurer’s risk aversion ‣ 5 Numerical Illustration and Welfare Analysis ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") largely aligns with that reported in Table [2](https://arxiv.org/html/2602.14223v1#S5.T2 "Table 2 ‣ 5.1.2 Reinsurance strategies ‣ 5.1 Baseline contracts ‣ 5 Numerical Illustration and Welfare Analysis ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"), with reinsurance levels typically being highest for all members under the JP-optimal contracts. Focusing on the BO1 and JP-optimal contracts, this finding echoes the results of Jiang et al. ([2025](https://arxiv.org/html/2602.14223v1#bib.bib12 "Bowley solution of a variance game in insurance"), Theorem 4.3), despite the different modeling framework. The only exception to the above pattern occurs for Member 2, for whom the reinsurance level under the BO2 contract exceeds that under the JP-optimal contracts when γR\gamma\_{R} becomes sufficiently large for the aforementioned reason. In addition, the reinsurance strategies of all members tend to converge under the JP-optimal and BO1 contracts as γR\gamma\_{R} becomes sufficiently large. This occurs because the reinsurer’s risk-bearing capacity decreases as she becomes more risk averse, reducing the advantage of the JP-optimal contracts over the BO1 contracts. Consequently, the distinction between the two designs becomes less significant, leading to the alignment of the reinsurance strategies.

#### 5.2.2 Total welfare gains

![Refer to caption](Graphics/TWGvsGammaR.png)


Figure 4: Comparison of total welfare gains among contracts with different γR\gamma\_{R}.

Fig. [4](https://arxiv.org/html/2602.14223v1#S5.F4 "Figure 4 ‣ 5.2.2 Total welfare gains ‣ 5.2 Impact of the reinsurer’s risk aversion ‣ 5 Numerical Illustration and Welfare Analysis ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") shows the total welfare gains of all contracts as γR\gamma\_{R} varies, where JP-optimal contracts attain the largest total welfare levels and thus corroborate the result in Corollary [4.12](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem12 "Corollary 4.12. ‣ 4.5 Comparison of Bowley and Pareto optima ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
We highlight three key observations below.

First, the welfare levels of both Pareto and Bowley contracts decline with γR\gamma\_{R}.
As reflected in the decline of members’ reinsurance strategies with γR\gamma\_{R} depicted in Fig. [3](https://arxiv.org/html/2602.14223v1#S5.F3 "Figure 3 ‣ 5.2.1 Members’ reinsurance policies ‣ 5.2 Impact of the reinsurer’s risk aversion ‣ 5 Numerical Illustration and Welfare Analysis ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"), the effectiveness of the risk-transfer mechanism weakens as the risk-bearing capacity of the reinsurer decreases.
Such dampening of risk sharing
leads to a decline in the welfare improvement.

Second, concerning the impact of the single-loading restriction, we observe that when γR\gamma\_{R} is small, the total welfare gain under the BO2 contract mildly exceeds that under the BO1 contract. As the reinsurer has a higher risk-bearing capacity, Member 2, who bears the riskiest loss, can take advantage of the loading design in the BO2 contract to transfer her risk to the reinsurer. This disproportionately increases her welfare gain, which dominates the welfare improvement of the community, thereby leading to a lower total welfare gain (cf. Table [6](https://arxiv.org/html/2602.14223v1#S5.T6 "Table 6 ‣ 5.1.4 Welfare analysis ‣ 5.1 Baseline contracts ‣ 5 Numerical Illustration and Welfare Analysis ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")). As γR\gamma\_{R} increases, the risk-bearing capacity is weakened, which calls for a more balanced distribution of risks in the community. In that case, benefiting from the better risk-premium alignment, the BO1 contract outperforms the BO2 contract and delivers a higher total welfare gain.

Third, the total welfare gains of the JP-optimal and the BO1 contracts converge as γR\gamma\_{R} increases. This is consistent with the findings in Fig. [3](https://arxiv.org/html/2602.14223v1#S5.F3 "Figure 3 ‣ 5.2.1 Members’ reinsurance policies ‣ 5.2 Impact of the reinsurer’s risk aversion ‣ 5 Numerical Illustration and Welfare Analysis ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"), which reveal the diminishing advantage of the Pareto design as the reinsurer’s risk-bearing capacity declines, ultimately aligning both the reinsurance strategies and the total welfare outcomes of the two designs.

## 6 Conclusion

This paper introduces a new design of P2P insurance schemes with an endogenous
reinsurance treaty.
We compare two canonical designs depending on the interaction between the plan manager and the reinsurer: Pareto and Bowley.

In the Pareto design, full cooperation induces pricing freedom, corresponding to the allocation of welfare gains among agents. By formulating a transferable-utility cooperative game, we show that this allocation problem admits a non-empty core, and any core allocation induces a coalitionally stable JP-optimal contract.
In contrast, the Bowley design leads to strategic pricing distortions.
We show that it is never JP-optimal and yields strictly lower total welfare than its cooperative counterpart. This arises from the reinsurer’s first-mover advantage, which leads to higher reinsurance prices and alters reinsurance demand and mutualization patterns.

Our numerical analysis showcases the welfare improvement of the reinsurance option and illustrates how single-loading restrictions further affect welfare distribution, particularly disadvantaging low-risk members.
Also, the comparative static analysis highlights
that a less risk-averse reinsurer accepts more risk from members, leading to a greater increase in total welfare.

Having opened up a new avenue of game-theoretic study on reinsurance contracting in P2P insurance, our framework can be generalized to other settings:
(i) A continuous-time risk-exchange environment (Tao et al., [2025](https://arxiv.org/html/2602.14223v1#bib.bib58 "Pareto-optimal risk exchange in a continuous-time economy: application to target benefit pension")), which can also incorporate correlated investment risk, thereby enabling designs with collective investment (Balter and Schweizer, [2024](https://arxiv.org/html/2602.14223v1#bib.bib38 "Robust decisions for heterogeneous agents via certainty equivalents"); Ng and Nguyen, [2025b](https://arxiv.org/html/2602.14223v1#bib.bib62 "Pareto efficiency and financial fairness under limited expected loss constraint"));
(ii) Multiple reinsurers: this enables different strategic interaction between reinsurers such as cooperation, co-opetition and competition; see, e.g., Cao et al. ([2025](https://arxiv.org/html/2602.14223v1#bib.bib32 "Co-opetition in reinsurance markets: when Pareto meets Stackelberg and Nash")) and Chu et al. ([2025](https://arxiv.org/html/2602.14223v1#bib.bib29 "Mean field analysis of two-party governance: competition versus cooperation among leaders"));
(iii) The Nash bargaining model (Boonen, [2016](https://arxiv.org/html/2602.14223v1#bib.bib39 "Nash equilibria of over-the-counter bargaining for insurance risk redistributions: the role of a regulator"); Nguyen and Zou, [2025](https://arxiv.org/html/2602.14223v1#bib.bib57 "Optimal design of registered index-linked annuities under asymmetric Nash bargaining")): it is of both theoretical and practical interest to study differences in bargaining power between the reinsurer and the P2P plan manager.
We leave these for future research.

## Acknowledgments

Tak Wa Ng and Thai Nguyen acknowledge the support from the Natural Sciences and Engineering Research Council of Canada (Grant No. RGPIN-2021-02594) and the Chair of Actuary, Laval University. Tak Wa Ng also acknowledges the hospitality of the Department of Mathematics at The Ohio State University during the drafting of this paper. Kenneth Ng acknowledges support from the start-up fund at The Ohio State University and the CKER research fund of the Society of Actuaries (Project title: Pricing and Staking of Decentralized Insurance).

## References

* S. Abdikerimova and R. Feng (2022)
  Peer-to-peer multi-risk insurance and mutual aid.
  European Journal of Operational Research 299 (2),  pp. 735–749.
  Cited by: [§1.2](https://arxiv.org/html/2602.14223v1#S1.SS2.p1.1 "1.2 Related Literature ‣ 1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* M. Anthropelos, R. Feng, and S. Kim (2026)
  On the expansion of risk pooling.
  Management Science.
  Cited by: [§1.1](https://arxiv.org/html/2602.14223v1#S1.SS1.p4.1 "1.1 Contributions ‣ 1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"),
  [§1.2](https://arxiv.org/html/2602.14223v1#S1.SS2.p1.1 "1.2 Related Literature ‣ 1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"),
  [§1](https://arxiv.org/html/2602.14223v1#S1.p1.1 "1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"),
  [§5.1.4](https://arxiv.org/html/2602.14223v1#S5.SS1.SSS4.p4.1 "5.1.4 Welfare analysis ‣ 5.1 Baseline contracts ‣ 5 Numerical Illustration and Welfare Analysis ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* A. V. Asimit, T. J. Boonen, Y. Chi, and W. F. Chong (2021)
  Risk sharing with multiple indemnity environments.
  European Journal of Operational Research 295 (2),  pp. 587–603.
  Cited by: [§1.1](https://arxiv.org/html/2602.14223v1#S1.SS1.p2.1 "1.1 Contributions ‣ 1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"),
  [§3.1](https://arxiv.org/html/2602.14223v1#S3.SS1.p1.3 "3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* V. Asimit and T. J. Boonen (2018)
  Insurance with multiple insurers: a game-theoretic approach.
  European Journal of Operational Research 267 (2),  pp. 778–790.
  Cited by: [§1.2](https://arxiv.org/html/2602.14223v1#S1.SS2.p3.1 "1.2 Related Literature ‣ 1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* J. Aubin (2002)
  Optima and equilibria: an introduction to nonlinear analysis.
  Vol. 140, Springer Science & Business Media.
  Cited by: [§4.1.1](https://arxiv.org/html/2602.14223v1#S4.SS1.SSS1.p2.1 "4.1.1 Plan manager’s follower problem ‣ 4.1 Problem formulation ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* Y. Bai, Z. Zhou, H. Xiao, R. Gao, and F. Zhong (2022)
  A hybrid stochastic differential reinsurance and investment game with bounded memory.
  European Journal of Operational Research 296 (2),  pp. 717–737.
  Cited by: [§1.2](https://arxiv.org/html/2602.14223v1#S1.SS2.p4.1 "1.2 Related Literature ‣ 1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* A. G. Balter and N. Schweizer (2024)
  Robust decisions for heterogeneous agents via certainty equivalents.
  European Journal of Operational Research 317 (1),  pp. 171–184.
  Cited by: [§6](https://arxiv.org/html/2602.14223v1#S6.p4.1 "6 Conclusion ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* T. J. Boonen, W. F. Chong, and M. Ghossoub (2024)
  Pareto-efficient risk sharing in centralized insurance markets with application to flood risk.
  Journal of Risk and Insurance 91 (2),  pp. 449–488.
  Cited by: [§1.2](https://arxiv.org/html/2602.14223v1#S1.SS2.p3.1 "1.2 Related Literature ‣ 1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"),
  [§1](https://arxiv.org/html/2602.14223v1#S1.p1.1 "1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* T. J. Boonen and M. Ghossoub (2023)
  Bowley vs. Pareto optima in reinsurance contracting.
  European Journal of Operational Research 307 (1),  pp. 382–391.
  Cited by: [§1.2](https://arxiv.org/html/2602.14223v1#S1.SS2.p5.1 "1.2 Related Literature ‣ 1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"),
  [§4.5](https://arxiv.org/html/2602.14223v1#S4.SS5.p3.1 "4.5 Comparison of Bowley and Pareto optima ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* T. J. Boonen and W. Jiang (2025)
  Pareto-optimal insurance under robust distortion risk measures.
  European Journal of Operational Research 324 (2),  pp. 690–705.
  Cited by: [§1.2](https://arxiv.org/html/2602.14223v1#S1.SS2.p3.1 "1.2 Related Literature ‣ 1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* T. J. Boonen, T. W. Ng, and T. Nguyen (2025)
  Contractibility, peer-to-peer insurance, and moral hazard.
  Available at SSRN 5647630.
  Cited by: [§1.2](https://arxiv.org/html/2602.14223v1#S1.SS2.p1.1 "1.2 Related Literature ‣ 1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* T. J. Boonen (2016)
  Nash equilibria of over-the-counter bargaining for insurance risk redistributions: the role of a regulator.
  European Journal of Operational Research 250 (3),  pp. 955–965.
  Cited by: [§4.5](https://arxiv.org/html/2602.14223v1#S4.SS5.p6.1 "4.5 Comparison of Bowley and Pareto optima ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"),
  [§6](https://arxiv.org/html/2602.14223v1#S6.p4.1 "6 Conclusion ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* J. Cai and Y. Chi (2020)
  Optimal reinsurance designs based on risk measures: a review.
  Statistical Theory and Related Fields 4 (1),  pp. 1–13.
  Cited by: [footnote 2](https://arxiv.org/html/2602.14223v1#footnote2 "In 1.2 Related Literature ‣ 1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* J. Cai, H. Liu, and R. Wang (2017)
  Pareto-optimal reinsurance arrangements under general model settings.
  Insurance: Mathematics and Economics 77,  pp. 24–37.
  Cited by: [§1.2](https://arxiv.org/html/2602.14223v1#S1.SS2.p2.1 "1.2 Related Literature ‣ 1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* J. Cao, D. Li, V. R. Young, and B. Zou (2023)
  Reinsurance games with two reinsurers: tree versus chain.
  European Journal of Operational Research 310 (2),  pp. 928–941.
  Cited by: [§1.2](https://arxiv.org/html/2602.14223v1#S1.SS2.p4.1 "1.2 Related Literature ‣ 1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"),
  [§4.5](https://arxiv.org/html/2602.14223v1#S4.SS5.p6.1 "4.5 Comparison of Bowley and Pareto optima ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* J. Cao, D. Li, V. R. Young, and B. Zou (2025)
  Co-opetition in reinsurance markets: when Pareto meets Stackelberg and Nash.
  Insurance: Mathematics and Economics 125,  pp. 103133.
  Cited by: [§6](https://arxiv.org/html/2602.14223v1#S6.p4.1 "6 Conclusion ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* F. Chan and H. U. Gerber (1985)
  The reinsurer’s monopoly and the Bowley solution.
  ASTIN Bulletin: The Journal of the IAA 15 (2),  pp. 141–148.
  Cited by: [§1.2](https://arxiv.org/html/2602.14223v1#S1.SS2.p5.1 "1.2 Related Literature ‣ 1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* L. Chen and Y. Shen (2018)
  On a new paradigm of optimal reinsurance: a stochastic Stackelberg differential game between an insurer and a reinsurer.
  ASTIN Bulletin: The Journal of the IAA 48 (2),  pp. 905–960.
  Cited by: [§1.2](https://arxiv.org/html/2602.14223v1#S1.SS2.p4.1 "1.2 Related Literature ‣ 1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* Z. Chen, R. Feng, L. Wei, and J. Zhao (2024)
  Cost-effectiveness, fairness and adverse selection in mutual aid.
  European Financial Management 30 (3),  pp. 1510–1544.
  Cited by: [§1.2](https://arxiv.org/html/2602.14223v1#S1.SS2.p1.1 "1.2 Related Literature ‣ 1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* K. C. Cheung, S. C. P. Yam, and Y. Zhang (2019)
  Risk-adjusted Bowley reinsurance under distorted probabilities.
  Insurance: Mathematics and Economics 86,  pp. 64–72.
  Cited by: [§1.2](https://arxiv.org/html/2602.14223v1#S1.SS2.p5.1 "1.2 Related Literature ‣ 1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* D. Chu, K. T. H. Ng, S. C. P. Yam, and H. Zheng (2025)
  Mean field analysis of two-party governance: competition versus cooperation among leaders.
  Automatica 173,  pp. 112028.
  Cited by: [§6](https://arxiv.org/html/2602.14223v1#S6.p4.1 "6 Conclusion ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* G. P. Clemente, S. Levantesi, and G. Piscopo (2023)
  Optimal cashback in a cooperative framework for peer-to-peer insurance coverages.
  Annals of Operations Research,  pp. 1–13.
  Cited by: [§1.2](https://arxiv.org/html/2602.14223v1#S1.SS2.p1.1 "1.2 Related Literature ‣ 1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* M. Denuit, J. Dhaene, and C. Y. Robert (2022)
  Risk-sharing rules and their properties, with applications to peer-to-peer insurance.
  Journal of Risk and Insurance 89 (3),  pp. 615–667.
  Cited by: [§1.2](https://arxiv.org/html/2602.14223v1#S1.SS2.p1.1 "1.2 Related Literature ‣ 1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* M. Denuit and J. Dhaene (2012)
  Convex order and comonotonic conditional mean risk sharing.
  Insurance: Mathematics and Economics 51 (2),  pp. 265–270.
  Cited by: [§1](https://arxiv.org/html/2602.14223v1#S1.p1.1 "1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* M. Denuit and C. Y. Robert (2021a)
  Risk sharing under the dominant peer-to-peer property and casualty insurance business models.
  Risk Management and Insurance Review 24 (2),  pp. 181–205.
  Cited by: [§1.2](https://arxiv.org/html/2602.14223v1#S1.SS2.p1.1 "1.2 Related Literature ‣ 1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* M. Denuit and C. Y. Robert (2021b)
  Stop-loss protection for a large P2P insurance pool.
  Insurance: Mathematics and Economics 100,  pp. 210–233.
  Cited by: [§1.2](https://arxiv.org/html/2602.14223v1#S1.SS2.p1.1 "1.2 Related Literature ‣ 1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"),
  [§1](https://arxiv.org/html/2602.14223v1#S1.p1.1 "1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* M. Denuit (2020)
  Investing in your own and peers’ risks: the simple analytics of P2P insurance.
  European Actuarial Journal 10 (2),  pp. 335–359.
  Cited by: [§1](https://arxiv.org/html/2602.14223v1#S1.p1.1 "1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* R. Feng, C. Liu, and S. Taylor (2023)
  Peer-to-peer risk sharing with an application to flood risk pooling.
  Annals of Operations Research 321 (1-2),  pp. 813–842.
  Cited by: [§1.2](https://arxiv.org/html/2602.14223v1#S1.SS2.p1.1 "1.2 Related Literature ‣ 1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"),
  [§2.1](https://arxiv.org/html/2602.14223v1#S2.SS1.p3.1 "2.1 Basic setting and risk sharing ‣ 2 Model Formulations ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"),
  [§3.1](https://arxiv.org/html/2602.14223v1#S3.SS1.p6.1 "3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"),
  [§3.2](https://arxiv.org/html/2602.14223v1#S3.SS2.p5.7 "3.2 Cooperative game study on premium decision ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* R. Feng (2023)
  Decentralized insurance.
  In Decentralized insurance: Technical foundation of business models,
   pp. 119–139.
  Cited by: [§1](https://arxiv.org/html/2602.14223v1#S1.p1.1 "1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* D. B. Gillies (1953)
  Some theorems on n-person games.
   Princeton University.
  Cited by: [§1.2](https://arxiv.org/html/2602.14223v1#S1.SS2.p3.1 "1.2 Related Literature ‣ 1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"),
  [§3.2.1](https://arxiv.org/html/2602.14223v1#S3.SS2.SSS1.p1.2 "3.2.1 Coalitional stability and the core ‣ 3.2 Cooperative game study on premium decision ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* D. Hu, S. Chen, and H. Wang (2018)
  Robust reinsurance contracts with uncertainty about jump risk.
  European Journal of Operational Research 266 (3),  pp. 1175–1188.
  Cited by: [§1.2](https://arxiv.org/html/2602.14223v1#S1.SS2.p4.1 "1.2 Related Literature ‣ 1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* W. Jiang, X. Liang, and V. R. Young (2025)
  Bowley solution of a variance game in insurance.
  Scandinavian Actuarial Journal 2025 (6),  pp. 617–634.
  Cited by: [§1.1](https://arxiv.org/html/2602.14223v1#S1.SS1.p7.1 "1.1 Contributions ‣ 1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"),
  [§1.2](https://arxiv.org/html/2602.14223v1#S1.SS2.p5.1 "1.2 Related Literature ‣ 1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"),
  [§4.5](https://arxiv.org/html/2602.14223v1#S4.SS5.p3.1 "4.5 Comparison of Bowley and Pareto optima ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"),
  [§5.2.1](https://arxiv.org/html/2602.14223v1#S5.SS2.SSS1.p3.2 "5.2.1 Members’ reinsurance policies ‣ 5.2 Impact of the reinsurer’s risk aversion ‣ 5 Numerical Illustration and Welfare Analysis ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* C. Laux and A. Muermann (2010)
  Financing risk transfer under governance problems: mutual versus stock insurers.
  Journal of Financial Intermediation 19 (3),  pp. 333–354.
  Cited by: [§1](https://arxiv.org/html/2602.14223v1#S1.p1.1 "1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* B. Li, W. Li, K. T. H. Ng, and S. C. P. Yam (2025)
  Mean field analysis of mutual insurance market.
  arXiv preprint arXiv:2511.12292.
  Cited by: [§1](https://arxiv.org/html/2602.14223v1#S1.p1.1 "1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* A. Lo and Z. Tang (2019)
  Pareto-optimal reinsurance policies in the presence of individual risk constraints.
  Annals of Operations Research 274 (1),  pp. 395–423.
  Cited by: [§1.2](https://arxiv.org/html/2602.14223v1#S1.SS2.p2.1 "1.2 Related Literature ‣ 1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* M. A. Milevsky and T. S. Salisbury (2015)
  Optimal retirement income tontines.
  Insurance: Mathematics and economics 64,  pp. 91–105.
  Cited by: [§1](https://arxiv.org/html/2602.14223v1#S1.p1.1 "1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* T. W. Ng and T. Nguyen (2025a)
  Individual survivor fund account: the impact of bequest motives on tontine participation.
  Insurance: Mathematics and Economics 125,  pp. 103161.
  Cited by: [§1](https://arxiv.org/html/2602.14223v1#S1.p1.1 "1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* T. W. Ng and T. Nguyen (2025b)
  Pareto efficiency and financial fairness under limited expected loss constraint.
  Journal of Mathematical Economics 117 (C),  pp. 103096.
  Cited by: [§6](https://arxiv.org/html/2602.14223v1#S6.p4.1 "6 Conclusion ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* T. Nguyen and B. Zou (2025)
  Optimal design of registered index-linked annuities under asymmetric Nash bargaining.
  Available at SSRN 5864823.
  Cited by: [§6](https://arxiv.org/html/2602.14223v1#S6.p4.1 "6 Conclusion ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* M. J. Osborne and A. Rubinstein (1994)
  A course in game theory.
   MIT press.
  Cited by: [Appendix D](https://arxiv.org/html/2602.14223v1#A4.p2.11 "Appendix D Proof of Theorem 3.5 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* K. B. Petersen and M. S. Pedersen (2008)
  The matrix cookbook.
  Technical University of Denmark 7 (15),  pp. 510.
  Cited by: [Appendix B](https://arxiv.org/html/2602.14223v1#A2.p1.4 "Appendix B Proof of Proposition 3.3 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* A. Raviv (1979)
  The design of an optimal insurance policy.
  American Economic Review 69 (1),  pp. 84–96.
  Cited by: [§1.2](https://arxiv.org/html/2602.14223v1#S1.SS2.p3.1 "1.2 Related Literature ‣ 1 Introduction ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").
* C. Tao, Y. Shen, and T. K. Siu (2025)
  Pareto-optimal risk exchange in a continuous-time economy: application to target benefit pension.
  ASTIN Bulletin: The Journal of the IAA 55 (3),  pp. 615–643.
  Cited by: [§6](https://arxiv.org/html/2602.14223v1#S6.p4.1 "6 Conclusion ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").

## Appendix A Proof of Lemma [3.2](https://arxiv.org/html/2602.14223v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")

To show that 𝑴¯\overline{\bm{M}} is positive definite, consider for any 𝒗∈ℝn\bm{v}\in\mathbb{R}^{n},

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒗⊤​𝑴¯​𝒗\displaystyle\bm{v}^{\top}\overline{\bm{M}}\bm{v} | =γR​𝒗⊤​𝚺​𝒗+k​𝒗⊤​𝑫​(𝝁2)​𝑫​(𝜸)​𝒗+1∑j=1nγj−1​(𝒗⊤​𝚺​𝒗−k​(𝝁⊤​𝒗)2).\displaystyle=\gamma\_{R}\bm{v}^{\top}\bm{\Sigma}\bm{v}+k\bm{v}^{\top}\bm{D}(\bm{\mu}^{2})\bm{D}(\bm{\gamma})\bm{v}+\frac{1}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\left(\bm{v}^{\top}\bm{\Sigma}\bm{v}-k(\bm{\mu}^{\top}\bm{v})^{2}\right). |  |

Using the Cauchy–Schwarz inequality and the positive-definiteness of 𝚺\bm{\Sigma},

|  |  |  |
| --- | --- | --- |
|  | (𝝁⊤​𝒗)2=((𝚺1/2​𝒗)⊤​(𝚺−1/2​𝝁))2≤(𝒗⊤​𝚺​𝒗)​(𝝁⊤​𝚺−1​𝝁)=1k​(𝒗⊤​𝚺​𝒗).(\bm{\mu}^{\top}\bm{v})^{2}=\big((\bm{\Sigma}^{1/2}\bm{v})^{\top}(\bm{\Sigma}^{-1/2}\bm{\mu})\big)^{2}\leq(\bm{v}^{\top}\bm{\Sigma}\bm{v})(\bm{\mu}^{\top}\bm{\Sigma}^{-1}\bm{\mu})=\frac{1}{k}(\bm{v}^{\top}\bm{\Sigma}\bm{v}). |  |

Therefore, for 𝒗≠0\bm{v}\neq 0, we have 𝒗⊤​𝑴¯​𝒗≥γR​𝒗⊤​𝚺​𝒗+k​𝒗⊤​𝑫​(𝝁2)​𝑫​(𝜸)​𝒗>0\bm{v}^{\top}\overline{\bm{M}}\bm{v}\geq\gamma\_{R}\bm{v}^{\top}\bm{\Sigma}\bm{v}+k\bm{v}^{\top}\bm{D}(\bm{\mu}^{2})\bm{D}(\bm{\gamma})\bm{v}>0.

## Appendix B Proof of Proposition [3.3](https://arxiv.org/html/2602.14223v1#S3.Thmtheorem3 "Proposition 3.3. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")

Due to the actuarial fairness condition, the objective can be transformed to 12​t​r​(𝑫​(𝜸)​𝑨​𝚺​𝑨⊤)+γR2​𝒑⊤​𝚺​𝒑.\frac{1}{2}tr(\bm{D}(\bm{\gamma})\bm{A}\bm{\Sigma}\bm{A}^{\top})+\frac{\gamma\_{R}}{2}\bm{p}^{\top}\bm{\Sigma}\bm{p}.
Consider the corresponding Lagrangian:

|  |  |  |
| --- | --- | --- |
|  | ℒ​(𝑨,𝒑,ϕ,𝝍)=12​t​r​(𝑫​(𝜸)​𝑨​𝚺​𝑨⊤)+γR2​𝒑⊤​𝚺​𝒑+(𝟏⊤−𝟏⊤​𝑨−𝒑⊤)​ϕ+𝝍⊤​(𝝁−𝑫​(𝝁)​𝒑−𝑨​𝝁),\displaystyle\mathcal{L}(\bm{A},\bm{p},\bm{\phi},\bm{\psi})=\frac{1}{2}tr({\bm{D}(\bm{\gamma})}\bm{A}\bm{\Sigma}\bm{A}^{\top})+\frac{\gamma\_{R}}{2}\bm{p}^{\top}\bm{\Sigma}\bm{p}+(\bm{1}^{\top}-\bm{1}^{\top}\bm{A}-\bm{p}^{\top})\bm{\phi}+\bm{\psi}^{\top}(\bm{\mu}-\bm{D}(\bm{\mu})\bm{p}-\bm{A}\bm{\mu}), |  |

where ϕ\bm{\phi} and 𝝍\bm{\psi} are Lagrangian multipliers capturing two constraints in Problem ([5](https://arxiv.org/html/2602.14223v1#S3.E5 "In 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")).
The first order condition (FOC) then yields

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂ℒ∂𝑨=𝑫​(𝜸)​𝑨​𝚺−𝟏​ϕ⊤−𝝍​𝝁⊤=𝟎n×n,∂ℒ∂𝒑=γR​𝚺​𝒑−𝑫​(𝝁)​𝝍−ϕ=𝟎,∂ℒ∂ϕ=𝟏⊤−𝟏⊤​𝑨−𝒑⊤=𝟎,∂ℒ∂𝝍=𝝁−𝑫​(𝝁)​𝒑−𝑨​𝝁=𝟎,\displaystyle\begin{split}&\frac{\partial\mathcal{L}}{\partial\bm{A}}=\bm{D}(\bm{\gamma})\bm{A}\bm{\Sigma}-\bm{1}\bm{\phi}^{\top}-\bm{\psi}\bm{\mu}^{\top}=\bm{0}\_{n\times n},\qquad\frac{\partial\mathcal{L}}{\partial\bm{p}}=\gamma\_{R}\bm{\Sigma}\bm{p}-\bm{D}(\bm{\mu})\bm{\psi}-\bm{\phi}=\bm{0},\\ &\frac{\partial\mathcal{L}}{\partial\bm{\phi}}=\bm{1}^{\top}-\bm{1}^{\top}\bm{A}-\bm{p}^{\top}=\bm{0},\qquad\frac{\partial\mathcal{L}}{\partial\bm{\psi}}=\bm{\mu}-\bm{D}(\bm{\mu})\bm{p}-\bm{A}\bm{\mu}=\bm{0},\end{split} | |  | (27) |

where the first equation follows from Petersen and Pedersen ([2008](https://arxiv.org/html/2602.14223v1#bib.bib50 "The matrix cookbook"), Equation (114)) and the cyclic property of the trace operator.

From the first equation in ([27](https://arxiv.org/html/2602.14223v1#A2.E27 "In Appendix B Proof of Proposition 3.3 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), we have 𝑨=𝑫​(𝜸)−1​(𝟏​ϕ⊤+𝝍​𝝁⊤)​𝚺−1\bm{A}=\bm{D}(\bm{\gamma})^{-1}(\bm{1}\bm{\phi}^{\top}+\bm{\psi}\bm{\mu}^{\top})\bm{\Sigma}^{-1}.
Plugging this into 𝟏⊤​𝑨=𝟏⊤−𝒑⊤\bm{1}^{\top}\bm{A}=\bm{1}^{\top}-\bm{p}^{\top}, we have 𝟏⊤​𝑫​(𝜸)−1​(𝟏​ϕ⊤+𝝍​𝝁⊤)​𝚺−1=𝟏⊤−𝒑⊤\bm{1}^{\top}\bm{D}(\bm{\gamma})^{-1}(\bm{1}\bm{\phi}^{\top}+\bm{\psi}\bm{\mu}^{\top})\bm{\Sigma}^{-1}=\bm{1}^{\top}-\bm{p}^{\top},
which leads to

|  |  |  |
| --- | --- | --- |
|  | ϕ⊤=𝟏⊤∑j=1nγj−1​(𝑫​(𝟏−𝒑)​𝚺−𝑫​(𝜸)−1​𝝍​𝝁⊤).\bm{\phi}^{\top}=\frac{\bm{1}^{\top}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}(\bm{D}(\bm{1}-\bm{p})\bm{\Sigma}-\bm{D}(\bm{\gamma})^{-1}\bm{\psi}\bm{\mu}^{\top}). |  |

Substituting 𝑨=𝑫​(𝜸)−1​(𝟏​ϕ⊤+𝝍​𝝁⊤)​𝚺−1\bm{A}=\bm{D}(\bm{\gamma})^{-1}(\bm{1}\bm{\phi}^{\top}+\bm{\psi}\bm{\mu}^{\top})\bm{\Sigma}^{-1} and ϕ⊤\bm{\phi}^{\top} to 𝑨​𝝁=𝑫​(𝟏−𝒑)​𝝁\bm{A}\bm{\mu}=\bm{D}(\bm{1}-\bm{p})\bm{\mu}, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝑫​(𝟏−𝒑)​𝝁=𝑫​(𝜸)−1​(𝟏𝟏⊤∑j=1nγj−1​(𝑫​(𝟏−𝒑)​𝚺−𝑫​(𝜸)−1​𝝍​𝝁⊤)+𝝍​𝝁⊤)​𝚺−1​𝝁\displaystyle\bm{D}(\bm{1}-\bm{p})\bm{\mu}=\bm{D}(\bm{\gamma})^{-1}\left(\frac{\bm{1}\bm{1}^{\top}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}(\bm{D}(\bm{1}-\bm{p})\bm{\Sigma}-\bm{D}(\bm{\gamma})^{-1}\bm{\psi}\bm{\mu}^{\top})+\bm{\psi}\bm{\mu}^{\top}\right)\bm{\Sigma}^{-1}\bm{\mu} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⇔\displaystyle\iff | (𝑫​(𝜸)−𝟏𝟏⊤∑j=1nγj−1)​𝑫​(𝟏−𝒑)​𝝁=k−1​(𝑰n−𝟏𝟏⊤​𝑫​(𝜸)−1∑j=1nγj−1)​𝝍.\displaystyle\left(\bm{D}(\bm{\gamma})-\frac{\bm{1}\bm{1}^{\top}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\right)\bm{D}(\bm{1}-\bm{p})\bm{\mu}=k^{-1}\left(\bm{I}\_{n}-\frac{\bm{1}\bm{1}^{\top}\bm{D}(\bm{\gamma})^{-1}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\right)\bm{\psi}. |  |

Solving the equation yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝍=k​𝑫​(𝜸)​𝑫​(𝟏−𝒑)​𝝁​and​ϕ⊤=𝟏⊤∑j=1nγj−1​(𝑫​(𝟏−𝒑)​𝚺−k​𝑫​(𝟏−𝒑)​𝝁​𝝁⊤).\bm{\psi}=k\bm{D}(\bm{\gamma})\bm{D}(\bm{1}-\bm{p})\bm{\mu}\quad\text{and}\quad\bm{\phi}^{\top}=\frac{\bm{1}^{\top}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}(\bm{D}(\bm{1}-\bm{p})\bm{\Sigma}-k\bm{D}(\bm{1}-\bm{p})\bm{\mu}\bm{\mu}^{\top}). |  | (28) |

Substituting ([28](https://arxiv.org/html/2602.14223v1#A2.E28 "In Appendix B Proof of Proposition 3.3 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) into 𝑨=𝑫​(𝜸)−1​(𝟏​ϕ⊤+𝝍​𝝁⊤)​𝚺−1\bm{A}=\bm{D}(\bm{\gamma})^{-1}(\bm{1}\bm{\phi}^{\top}+\bm{\psi}\bm{\mu}^{\top})\bm{\Sigma}^{-1}, we deduce that 𝑨∗\bm{A}\_{\*} is given by ([6](https://arxiv.org/html/2602.14223v1#S3.E6 "In Proposition 3.3. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")).

To obtain 𝒑∗\bm{p}\_{\*}, we substitute ([28](https://arxiv.org/html/2602.14223v1#A2.E28 "In Appendix B Proof of Proposition 3.3 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) into the second equation of ([27](https://arxiv.org/html/2602.14223v1#A2.E27 "In Appendix B Proof of Proposition 3.3 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), which leads to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | γR​𝚺​𝒑=k​𝑫​(𝝁)​𝑫​(𝜸)​𝑫​(𝟏−𝒑)​𝝁+1∑j=1nγj−1​(𝚺​(𝟏−𝒑)−k​𝝁​𝝁⊤​(𝟏−𝒑)).\displaystyle\begin{split}&\gamma\_{R}\bm{\Sigma}\bm{p}=k\bm{D}(\bm{\mu})\bm{D}(\bm{\gamma})\bm{D}(\bm{1}-\bm{p})\bm{\mu}+\frac{1}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}(\bm{\Sigma}(\bm{1}-\bm{p})-k\bm{\mu}\bm{\mu}^{\top}(\bm{1}-\bm{p})).\end{split} | |  | (29) |

Solving the equation yields ([6](https://arxiv.org/html/2602.14223v1#S3.E6 "In Proposition 3.3. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")).

Finally, we prove that the unique solution of the linear system ([29](https://arxiv.org/html/2602.14223v1#A2.E29 "In Appendix B Proof of Proposition 3.3 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) lies in (0,1)n(0,1)^{n} given the condition ([7](https://arxiv.org/html/2602.14223v1#S3.E7 "In Proposition 3.3. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")). Note that the system can be re-expressed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Li​(𝒑):=∑m=1nσi​m​(1−pm∑j=1nγj−1−γR​pm)+k​μi2​γi​(1−pi)−k​μi∑j=1nγj−1​∑m=1nμm​(1−pm)=0,L\_{i}(\bm{p}):=\sum\_{m=1}^{n}\sigma\_{im}\left(\frac{1-p\_{m}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}-\gamma\_{R}p\_{m}\right)+k\mu\_{i}^{2}\gamma\_{i}(1-p\_{i})-\frac{k\mu\_{i}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\sum\_{m=1}^{n}\mu\_{m}(1-p\_{m})=0, |  | (30) |

for all i=1,…,ni=1,\ldots,n. The claim can be established using the Poincaré–Miranda theorem. To this end, we need to check that for 𝒑∈[0,1]n\bm{p}\in[0,1]^{n}, the sign of left-hand side in ([30](https://arxiv.org/html/2602.14223v1#A2.E30 "In Appendix B Proof of Proposition 3.3 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) is nonnegative (resp. nonpositive) if pi=1p\_{i}=1 (resp. pi=0p\_{i}=0) for all i=1,…,ni=1,\ldots,n. For pi=1p\_{i}=1, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Li​(p1,…,pi−1,1,pi+1,…,pn)\displaystyle\ L\_{i}(p\_{1},\dots,p\_{i-1},1,p\_{i+1},\dots,p\_{n}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | −γR​σi2+∑m≠iσi​m∑j=1nγj−1−k​μi∑j=1nγj−1​∑m≠iμm+∑m≠ipm​(k​μi​μm∑j=1nγj−1−(γR+1∑j=1nγj−1)​σi​m)\displaystyle\ -\gamma\_{R}\sigma\_{i}^{2}+\frac{\sum\_{m\neq i}\sigma\_{im}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}-\frac{k\mu\_{i}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\sum\_{m\neq i}\mu\_{m}+\sum\_{m\neq i}p\_{m}\left(\frac{k\mu\_{i}\mu\_{m}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}-\left(\gamma\_{R}+\frac{1}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\right)\sigma\_{im}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | −γR​σi2+∑m≠iσi​m∑j=1nγj−1−k​μi​∑m≠iμm∑j=1nγj−1+∑m≠i(k​μi​μm∑j=1nγj−1−(γR+1∑j=1nγj−1)​σi​m)+<0.\displaystyle\ -\gamma\_{R}\sigma\_{i}^{2}+\frac{\sum\_{m\neq i}\sigma\_{im}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}-\frac{k\mu\_{i}\sum\_{m\neq i}\mu\_{m}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}+\sum\_{m\neq i}\left(\frac{k\mu\_{i}\mu\_{m}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}-\left(\gamma\_{R}+\frac{1}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\right)\sigma\_{im}\right)\_{+}<0. |  |

On the other hand, for pi=0p\_{i}=0, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Li​(p1,…,pi−1,0,pi+1,…,pn)\displaystyle\ L\_{i}(p\_{1},\dots,p\_{i-1},0,p\_{i+1},\dots,p\_{n}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∑m=1nσi​m∑j=1nγj−1+k​μi2​γi−k​μi​∑m=1nμm∑j=1nγj−1+∑m≠ipm​(k​μi​μm∑j=1nγj−1−(γR+1∑j=1nγj−1)​σi​m)\displaystyle\ \frac{\sum\_{m=1}^{n}\sigma\_{im}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}+k\mu\_{i}^{2}\gamma\_{i}-\frac{k\mu\_{i}\sum\_{m=1}^{n}\mu\_{m}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}+\sum\_{m\neq i}p\_{m}\left(\frac{k\mu\_{i}\mu\_{m}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}-\left(\gamma\_{R}+\frac{1}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\right)\sigma\_{im}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≥\displaystyle\geq | ∑m=1nσi​m∑j=1nγj−1+k​μi2​γi−k​μi​∑m=1nμm∑j=1nγj−1−∑m≠i((γR+1∑j=1nγj−1)​σi​m−k​μi​μm∑j=1nγj−1)+>0.\displaystyle\ \frac{\sum\_{m=1}^{n}\sigma\_{im}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}+k\mu\_{i}^{2}\gamma\_{i}-\frac{k\mu\_{i}\sum\_{m=1}^{n}\mu\_{m}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}-\sum\_{m\neq i}\left(\left(\gamma\_{R}+\frac{1}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\right)\sigma\_{im}-\frac{k\mu\_{i}\mu\_{m}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\right)\_{+}>0. |  |

Note that the above two inequalities follow from the condition ([7](https://arxiv.org/html/2602.14223v1#S3.E7 "In Proposition 3.3. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")). In addition, as the inequalities in ([7](https://arxiv.org/html/2602.14223v1#S3.E7 "In Proposition 3.3. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) are strict, pi≠0p\_{i}\neq 0 (resp. pi≠1p\_{i}\neq 1) for all i=1,…,ni=1,\dots,n. Finally, the uniqueness follows from the invertibility of 𝑴¯\overline{\bm{M}} as asserted in Lemma [3.2](https://arxiv.org/html/2602.14223v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").

## Appendix C Proof of Theorem [3.4](https://arxiv.org/html/2602.14223v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")

We first prove 𝒵⊆𝒥​𝒫​𝒪\mathcal{Z}\subseteq\mathcal{JPO} by contradiction. Assume that there exists a contract (𝑨^,𝒑^,𝜼^)∈𝒵(\bm{\hat{A}},\bm{\hat{p}},\bm{\hat{\eta}})\in\mathcal{Z} that is not JP-optimal, then there exists (𝑨~,𝒑~,𝜼~)∈ℐ​ℛ(\bm{\tilde{A}},\bm{\tilde{p}},\bm{\tilde{\eta}})\in\mathcal{IR} such that v​(𝜼~,𝒑~)≤v​(𝜼^,𝒑^)v(\bm{\tilde{\eta}},\bm{\tilde{p}})\leq v(\bm{\hat{\eta}},\bm{\hat{p}}) and ui​(𝑨~,𝒑~,𝜼~)≤ui​(𝑨^,𝒑^,𝜼^)u\_{i}(\bm{\tilde{A}},\bm{\tilde{p}},\bm{\tilde{\eta}})\leq u\_{i}(\bm{\hat{A}},\bm{\hat{p}},\bm{\hat{\eta}})
for all i=1,…,ni=1,\dots,n, with at least one strict inequality. This implies
u​(𝑨~,𝒑~,𝜼~)+v​(𝜼~,𝒑~)<u​(𝑨^,𝒑^,𝜼^)+v​(𝜼^,𝒑^)u(\bm{\tilde{A}},\bm{\tilde{p}},\bm{\tilde{\eta}})+v(\bm{\tilde{\eta}},\bm{\tilde{p}})<u(\bm{\hat{A}},\bm{\hat{p}},\bm{\hat{\eta}})+v(\bm{\hat{\eta}},\bm{\hat{p}}), which violates the optimality of (𝑨^,𝒑^,𝜼^)(\bm{\hat{A}},\bm{\hat{p}},\bm{\hat{\eta}}).

Next, we prove that 𝒥​𝒫​𝒪⊆𝒵\mathcal{JPO}\subseteq\mathcal{Z}, again by contradiction. Assume that there exists (𝑨¯,𝒑¯,𝜼¯)∈𝒥​𝒫​𝒪(\bm{\underline{A}},\bm{\underline{p}},\bm{\underline{\eta}})\in\mathcal{JPO} that does not belong to 𝒵\mathcal{Z}. Then, there exists (𝑨ˇ,𝒑ˇ,𝜼ˇ)∈𝒵(\bm{\check{A}},\bm{\check{p}},\bm{\check{\eta}})\in\mathcal{Z} such that u​(𝑨ˇ,𝒑ˇ,𝜼ˇ)+v​(𝜼ˇ,𝒑ˇ)<u​(𝑨¯,𝒑¯,𝜼¯)+v​(𝜼¯,𝒑¯)u(\bm{\check{A}},\bm{\check{p}},\bm{\check{\eta}})+v(\bm{\check{\eta}},\bm{\check{p}})<u(\bm{\underline{A}},\bm{\underline{p}},\bm{\underline{\eta}})+v(\bm{\underline{\eta}},\bm{\underline{p}}).
Define ηi⋆\eta\_{i}^{\star}, i=1,…,ni=1,\dots,n, by the solution of

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1+ηi⋆)​pˇi​μi=(1+ηˇi)​pˇi​μi+ui​(𝑨¯,𝒑¯,𝜼¯)−ui​(𝑨ˇ,𝒑ˇ,𝜼ˇ)=(1+η¯i)​p¯i​μi+ρi​(𝑨¯)−ρi​(𝑨ˇ).(1+\eta\_{i}^{\star})\check{p}\_{i}\mu\_{i}=(1+\check{\eta}\_{i})\check{p}\_{i}\mu\_{i}+u\_{i}(\bm{\underline{A}},\bm{\underline{p}},\bm{\underline{\eta}})-u\_{i}(\bm{\check{A}},\bm{\check{p}},\bm{\check{\eta}})=(1+\underline{\eta}\_{i})\underline{p}\_{i}\mu\_{i}+\rho\_{i}(\bm{\underline{A}})-\rho\_{i}(\bm{\check{A}}). |  | (31) |

Note that this needs pˇi>0\check{p}\_{i}>0 for all i=1,…,ni=1,\dots,n, which is ensured by Condition ([7](https://arxiv.org/html/2602.14223v1#S3.E7 "In Proposition 3.3. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")).
We then have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ui​(𝑨ˇ,𝒑ˇ,𝜼⋆)=\displaystyle u\_{i}(\bm{\check{A}},\bm{\check{p}},\bm{\eta}^{\star})= | ρi​(𝑨ˇ)+(1+ηi⋆)​pˇi​μi=(1+η¯i)​p¯i​μi+ρi​(𝑨¯)=ui​(𝑨¯,𝒑¯,𝜼¯)\displaystyle\rho\_{i}(\bm{\check{A}})+(1+\eta\_{i}^{\star})\check{p}\_{i}\mu\_{i}=(1+\underline{\eta}\_{i})\underline{p}\_{i}\mu\_{i}+\rho\_{i}(\bm{\underline{A}})=u\_{i}(\bm{\underline{A}},\bm{\underline{p}},\bm{\underline{\eta}}) |  |

for all i=1,…,ni=1,\dots,n, where the second last equality follows from ([31](https://arxiv.org/html/2602.14223v1#A3.E31 "In Appendix C Proof of Theorem 3.4 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")).

On the other hand, summing ([31](https://arxiv.org/html/2602.14223v1#A3.E31 "In Appendix C Proof of Theorem 3.4 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) over i=1,…,ni=1,\dots,n yields (𝑫​(𝝁)​𝜼⋆)⊤​𝒑ˇ=(𝑫​(𝝁)​𝜼ˇ)⊤​𝒑ˇ+u​(𝑨¯,𝒑¯,𝜼¯)−u​(𝑨ˇ,𝒑ˇ,𝜼ˇ)(\bm{D}(\bm{\mu})\bm{\eta}^{\star})^{\top}\bm{\check{p}}=(\bm{D}(\bm{\mu})\bm{\check{\eta}})^{\top}\bm{\check{p}}+u(\bm{\underline{A}},\bm{\underline{p}},\bm{\underline{\eta}})-u(\bm{\check{A}},\bm{\check{p}},\bm{\check{\eta}}).
Using this and u​(𝑨ˇ,𝒑ˇ,𝜼ˇ)+v​(𝜼ˇ,𝒑ˇ)<u​(𝑨¯,𝒑¯,𝜼¯)+v​(𝜼¯,𝒑¯)u(\bm{\check{A}},\bm{\check{p}},\bm{\check{\eta}})+v(\bm{\check{\eta}},\bm{\check{p}})<u(\bm{\underline{A}},\bm{\underline{p}},\bm{\underline{\eta}})+v(\bm{\underline{\eta}},\bm{\underline{p}}),

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(𝜼⋆,𝒑ˇ)=\displaystyle v(\bm{\eta^{\star}},\bm{\check{p}})= | γR2​𝒑ˇ⊤​𝚺​𝒑ˇ−(𝑫​(𝝁)​𝜼⋆)⊤​𝒑ˇ=v​(𝜼ˇ,𝒑ˇ)+u​(𝑨ˇ,𝒑ˇ,𝜼ˇ)−u​(𝑨¯,𝒑¯,𝜼¯)<v​(𝜼¯,𝒑¯),\displaystyle\frac{\gamma\_{R}}{2}\bm{\check{p}}^{\top}\bm{\Sigma}\bm{\check{p}}-(\bm{D}(\bm{\mu})\bm{\eta}^{\star})^{\top}\bm{\check{p}}=v(\bm{\check{\eta}},\bm{\check{p}})+u(\bm{\check{A}},\bm{\check{p}},\bm{\check{\eta}})-u(\bm{\underline{A}},\bm{\underline{p}},\bm{\underline{\eta}})<v(\bm{\underline{\eta}},\bm{\underline{p}}), |  |

These imply (𝑨ˇ,𝒑ˇ,𝜼⋆)∈ℐ​ℛ(\bm{\check{A}},\bm{\check{p}},\bm{\eta}^{\star})\in\mathcal{IR} and Pareto-dominates (𝑨¯,𝒑¯,𝜼¯)(\bm{\underline{A}},\bm{\underline{p}},\bm{\underline{\eta}}), leading to the desired contradiction.

Next, we show that 𝒵\mathcal{Z} is non-empty. To this end, for (𝑨∗,𝒑∗)(\bm{A}\_{\*},\bm{p}\_{\*}) solving ([5](https://arxiv.org/html/2602.14223v1#S3.E5 "In 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), we construct 𝜼∗\bm{\eta}\_{\*} such that (𝑨∗,𝒑∗,𝜼∗)∈ℐ​ℛ(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*})\in\mathcal{IR}. For any 𝜼\bm{\eta}, let ε:=u​(𝑰,0,𝜼)+v​(𝜼,𝟎)−u​(𝑨∗,𝒑∗,𝜼)−v​(𝜼,𝒑∗)\varepsilon:=u(\bm{I},0,\bm{\eta})+v(\bm{\eta},\bm{0})-u(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta})-v(\bm{\eta},\bm{p}\_{\*}). Note that ε>0\varepsilon>0 and is independent of 𝜼\bm{\eta}, since (𝑨∗,𝒑∗)(\bm{A}\_{\*},\bm{p}\_{\*}) is the unique minimizer of ([5](https://arxiv.org/html/2602.14223v1#S3.E5 "In 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")). Define 𝜼∗=(η∗1,…,η∗n)\bm{\eta}\_{\*}=(\eta\_{\*1},\dots,\eta\_{\*n}) by,

|  |  |  |  |
| --- | --- | --- | --- |
|  | η∗i​pi⁣∗​μi=γi2​(σi2−𝑨∗i​𝚺​𝑨∗i⊤)−ε2​n,i=1,…,n,\eta\_{\*i}p\_{i\*}\mu\_{i}=\frac{\gamma\_{i}}{2}\left(\sigma\_{i}^{2}-\bm{A}\_{\*i}\bm{\Sigma}\bm{A}\_{\*i}^{\top}\right)-\frac{\varepsilon}{2n},\quad i=1,\dots,n, |  | (32) |

It is clear that the members’ IR constraints ([3](https://arxiv.org/html/2602.14223v1#S2.E3 "In 2.3 Individual rationality ‣ 2 Model Formulations ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) are satisfied by the definition of η∗i\eta\_{\*i} with welfare gain

|  |  |  |
| --- | --- | --- |
|  | ωi​(𝑨∗,𝒑∗,𝜼∗)=μi+γi​σi22−ui​(𝑨∗,𝒑∗,𝜼∗)=γi2​(σi2−𝑨∗i​𝚺​𝑨∗i⊤)−η∗i​pi⁣∗​μi=ε2​n>0.\omega\_{i}(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*})=\mu\_{i}+\frac{\gamma\_{i}\sigma\_{i}^{2}}{2}-u\_{i}(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*})=\frac{\gamma\_{i}}{2}\left(\sigma\_{i}^{2}-\bm{A}\_{\*i}\bm{\Sigma}\bm{A}\_{\*i}^{\top}\right)-\eta\_{\*i}p\_{i\*}\mu\_{i}=\frac{\varepsilon}{2n}>0. |  |

Summing ([32](https://arxiv.org/html/2602.14223v1#A3.E32 "In Appendix C Proof of Theorem 3.4 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) over i=1,…,ni=1,\dots,n, we have

|  |  |  |
| --- | --- | --- |
|  | (𝑫​(𝝁)​𝜼∗)⊤​𝒑∗=12​(t​r​(𝑫​(𝜸)​𝚺)−t​r​(𝑫​(𝜸)​𝑨∗​𝚺​𝑨∗⊤))−ε2.(\bm{D}(\bm{\mu})\bm{\eta}\_{\*})^{\top}\bm{p}\_{\*}=\frac{1}{2}\left(tr(\bm{D}(\bm{\gamma})\bm{\Sigma})-tr(\bm{D}(\bm{\gamma})\bm{A}\_{\*}\bm{\Sigma}\bm{A}\_{\*}^{\top})\right)-\frac{\varepsilon}{2}. |  |

Using this and the actuarial fairness condition, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ωR​(𝑨∗,𝒑∗,𝜼∗)\displaystyle\omega\_{R}(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*}) | =(𝑫​(𝝁)​𝜼∗)⊤​𝒑∗−γR2​𝒑∗⊤​𝚺​𝒑∗\displaystyle=(\bm{D}(\bm{\mu})\bm{\eta}\_{\*})^{\top}\bm{p}\_{\*}-\frac{\gamma\_{R}}{2}\bm{p}\_{\*}^{\top}\bm{\Sigma}\bm{p}\_{\*} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =12​(t​r​(𝑫​(𝜸)​𝚺)−t​r​(𝑫​(𝜸)​𝑨∗​𝚺​𝑨∗⊤))−γR2​𝒑∗⊤​𝚺​𝒑∗−ε2\displaystyle=\frac{1}{2}\left(tr(\bm{D}(\bm{\gamma})\bm{\Sigma})-tr(\bm{D}(\bm{\gamma})\bm{A}\_{\*}\bm{\Sigma}\bm{A}\_{\*}^{\top})\right)-\frac{\gamma\_{R}}{2}\bm{p}\_{\*}^{\top}\bm{\Sigma}\bm{p}\_{\*}-\frac{\varepsilon}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =12​t​r​(𝑫​(𝜸)​𝚺)+𝟏⊤​𝑨∗​𝝁+𝝁⊤​𝒑∗\displaystyle=\frac{1}{2}tr(\bm{D}(\bm{\gamma})\bm{\Sigma})+\bm{1}^{\top}\bm{A}\_{\*}\bm{\mu}+\bm{\mu}^{\top}\bm{p}\_{\*} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −(γR2​𝒑∗⊤​𝚺​𝒑∗+12​t​r​(𝑫​(𝜸)​𝑨∗​𝚺​𝑨∗⊤)+𝟏⊤​𝑨∗​𝝁+𝝁⊤​𝒑∗)−ε2\displaystyle\qquad-\left(\frac{\gamma\_{R}}{2}\bm{p}\_{\*}^{\top}\bm{\Sigma}\bm{p}\_{\*}+\frac{1}{2}tr(\bm{D}(\bm{\gamma})\bm{A}\_{\*}\bm{\Sigma}\bm{A}\_{\*}^{\top})+\bm{1}^{\top}\bm{A}\_{\*}\bm{\mu}+\bm{\mu}^{\top}\bm{p}\_{\*}\right)-\frac{\varepsilon}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =12​t​r​(𝑫​(𝜸)​𝚺)+𝟏⊤​𝝁−(u​(𝑨∗,𝒑∗,𝜼∗)+v​(𝜼∗,𝒑∗))−ε2\displaystyle=\frac{1}{2}tr(\bm{D}(\bm{\gamma})\bm{\Sigma})+\bm{1}^{\top}\bm{\mu}-\left(u(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*})+v(\bm{\eta}\_{\*},\bm{p}\_{\*})\right)-\frac{\varepsilon}{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =u​(𝑰,𝟎,𝜼∗)+v​(𝜼∗,𝟎)−(u​(𝑨∗,𝒑∗,𝜼∗)+v​(𝜼∗,𝒑∗))−ε2=ε2>0,\displaystyle=u(\bm{I},\bm{0},\bm{\eta}\_{\*})+v(\bm{\eta}\_{\*},\bm{0})-\left(u(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*})+v(\bm{\eta}\_{\*},\bm{p}\_{\*})\right)-\frac{\varepsilon}{2}=\frac{\varepsilon}{2}>0, |  |

Therefore, the reinsurer’s IR constraint is also satisfied.

To study the equivalence between (i) and (ii), we define the following auxiliary problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | min(𝑨,𝒑,𝜼)∈ℐ​ℛ⁡v​(𝜼,𝒑)s.t. ​ui​(𝑨,𝒑,𝜼)≤ci​ for all ​i=1,…,n,𝑨​𝝁+𝑫​(𝝁)​𝒑=𝝁, 1⊤​𝑨+𝒑⊤=𝟏⊤.\min\_{(\bm{A},\bm{p},\bm{\eta})\in\mathcal{IR}}v(\bm{\eta},\bm{p})\quad\text{s.t. }u\_{i}(\bm{A},\bm{p},\bm{\eta})\leq c\_{i}\text{ for all }i=1,\dots,n,\ \bm{A}\bm{\mu}+\bm{D}(\bm{\mu})\bm{p}=\bm{\mu},\ \mathbf{1}^{\top}\bm{A}+\bm{p}^{\top}=\bm{1}^{\top}. |  | (33) |

We show that (𝑨∗,𝒑∗,𝜼∗)∈𝒥​𝒫​𝒪(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*})\in\mathcal{JPO} if and only if there exists (ci)i=1n(c\_{i})\_{i=1}^{n} such that (𝑨∗,𝒑∗,𝜼∗)(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*}) solves ([33](https://arxiv.org/html/2602.14223v1#A3.E33 "In Appendix C Proof of Theorem 3.4 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")).

Suppose that (𝑨∗,𝒑∗,𝜼∗)∈𝒥​𝒫​𝒪(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*})\in\mathcal{JPO} and let ci=ui​(𝑨∗,𝒑∗,𝜼∗)c\_{i}=u\_{i}(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*}), i=1,…,ni=1,\dots,n. We need to show that (𝑨∗,𝒑∗,𝜼∗)(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*}) is the minimizer of Problem ([33](https://arxiv.org/html/2602.14223v1#A3.E33 "In Appendix C Proof of Theorem 3.4 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) with parameters c1,…,cnc\_{1},\dots,c\_{n}.
Assume the contrary, so that there exists (𝑨′,𝒑′,𝜼′)∈ℐ​ℛ(\bm{A}^{\prime},\bm{p}^{\prime},\bm{\eta}^{\prime})\in\mathcal{IR} with ui​(𝑨′,𝒑′,𝜼′)≤ci=ui​(𝑨∗,𝒑∗,𝜼∗)u\_{i}(\bm{A}^{\prime},\bm{p}^{\prime},\bm{\eta}^{\prime})\leq c\_{i}=u\_{i}(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*}) for all i=1,…,ni=1,\dots,n, and v​(𝜼′,𝒑′)<v​(𝜼∗,𝒑∗)v(\bm{\eta}^{\prime},\bm{p}^{\prime})<v(\bm{\eta}\_{\*},\bm{p}\_{\*}).
This contradicts with the JP optimality of (𝑨∗,𝒑∗,𝜼∗)(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*}).

Conversely, assume that there exists c1,…,cnc\_{1},\dots,c\_{n} such that (𝑨∗,𝒑∗,𝜼∗)∉𝒥​𝒫​𝒪(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*})\notin\mathcal{JPO} is optimal for Problem ([33](https://arxiv.org/html/2602.14223v1#A3.E33 "In Appendix C Proof of Theorem 3.4 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")). Then, there exists (𝑨′,𝒑′,𝜼′)∈ℐ​ℛ(\bm{A}\_{{}^{\prime}},\bm{p}\_{{}^{\prime}},\bm{\eta}\_{{}^{\prime}})\in\mathcal{IR} such that ui​(𝑨′,𝒑′,𝜼′)≤ci=ui​(𝑨∗,𝒑∗,𝜼∗)u\_{i}(\bm{A}\_{{}^{\prime}},\bm{p}\_{{}^{\prime}},\bm{\eta}\_{{}^{\prime}})\leq c\_{i}=u\_{i}(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*}) for all i=1,…,ni=1,\dots,n, and v​(𝜼′,𝒑′)≤v​(𝜼∗,𝒑∗)v(\bm{\eta}\_{{}^{\prime}},\bm{p}\_{{}^{\prime}})\leq v(\bm{\eta}\_{\*},\bm{p}\_{\*}),
with at least one strict inequality. If v​(𝜼′,𝒑′)<v​(𝜼∗,𝒑∗)v(\bm{\eta}\_{{}^{\prime}},\bm{p}\_{{}^{\prime}})<v(\bm{\eta}\_{\*},\bm{p}\_{\*}), then it contradicts the optimality of (𝑨∗,𝒑∗,𝜼∗)(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*}). Thus, we have v​(𝜼′,𝒑′)=v​(𝜼∗,𝒑∗)v(\bm{\eta}\_{{}^{\prime}},\bm{p}\_{{}^{\prime}})=v(\bm{\eta}\_{\*},\bm{p}\_{\*}),
and there exists j∈{1,…,n}j\in\{1,\dots,n\} such that uj​(𝑨′,𝒑′,𝜼′)<uj​(𝑨∗,𝒑∗,𝜼∗)≤cju\_{j}(\bm{A}\_{{}^{\prime}},\bm{p}\_{{}^{\prime}},\bm{\eta}\_{{}^{\prime}})<u\_{j}(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*})\leq c\_{j}.
Define ϵj:=uj​(𝑨∗,𝒑∗,𝜼∗)−uj​(𝑨′,𝒑′,𝜼′)\epsilon\_{j}:=u\_{j}(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*})-u\_{j}(\bm{A}\_{{}^{\prime}},\bm{p}\_{{}^{\prime}},\bm{\eta}\_{{}^{\prime}}) and consider a new contract (𝑨′,𝒑′,𝜼>)(\bm{A}\_{{}^{\prime}},\bm{p}\_{{}^{\prime}},\bm{\eta}\_{>}), where
𝜼>=(η>1,…,η>n)\bm{\eta}\_{>}=(\eta\_{>1},\dots,\eta\_{>n}) is given by η>i:=ηi′\eta\_{>i}:=\eta\_{{}^{\prime}i} for i≠ji\neq j, and η>j:=ηj′+εj/(pj′​μj)\eta\_{>j}:=\eta\_{{}^{\prime}j}+\varepsilon\_{j}/(p\_{{}^{\prime}j}\mu\_{j}). Then, ui​(𝑨′,𝒑′,𝜼>)=ui​(𝑨′,𝒑′,𝜼′)≤ciu\_{i}(\bm{A}\_{{}^{\prime}},\bm{p}\_{{}^{\prime}},\bm{\eta}\_{>})=u\_{i}(\bm{A}\_{{}^{\prime}},\bm{p}\_{{}^{\prime}},\bm{\eta}\_{{}^{\prime}})\leq c\_{i} for i≠ji\neq j, and uj​(𝑨′,𝒑′,𝜼>)=uj​(𝑨′,𝒑′,𝜼′)+εj=uj​(𝑨∗,𝒑∗,𝜼∗)≤cju\_{j}(\bm{A}\_{{}^{\prime}},\bm{p}\_{{}^{\prime}},\bm{\eta}\_{>})=u\_{j}(\bm{A}\_{{}^{\prime}},\bm{p}\_{{}^{\prime}},\bm{\eta}\_{{}^{\prime}})+\varepsilon\_{j}=u\_{j}(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*})\leq c\_{j}.
In addition, by the fact that v​(𝜼′,𝒑′)=v​(𝜼∗,𝒑∗)v(\bm{\eta}\_{{}^{\prime}},\bm{p}\_{{}^{\prime}})=v(\bm{\eta}\_{\*},\bm{p}\_{\*}), we have v​(𝜼>,𝒑′)=v​(𝜼′,𝒑′)−ϵj=v​(𝜼∗,𝒑∗)−ϵj<v​(𝜼∗,𝒑∗)v(\bm{\eta}\_{>},\bm{p}\_{{}^{\prime}})=v(\bm{\eta}\_{{}^{\prime}},\bm{p}\_{{}^{\prime}})-\epsilon\_{j}=v(\bm{\eta}\_{\*},\bm{p}\_{\*})-\epsilon\_{j}<v(\bm{\eta}\_{\*},\bm{p}\_{\*}),
contradicting the optimality of (𝑨∗,𝒑∗,𝜼∗)(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*}).

Finally, we need to show the equivalence of Problems ([33](https://arxiv.org/html/2602.14223v1#A3.E33 "In Appendix C Proof of Theorem 3.4 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) and ([8](https://arxiv.org/html/2602.14223v1#S3.E8 "In item (ii) ‣ Theorem 3.4. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), which follows from the fact that optimality of Problem ([33](https://arxiv.org/html/2602.14223v1#A3.E33 "In Appendix C Proof of Theorem 3.4 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) only occurs when constraints are binding; otherwise, one can repeat the above proof with a new contract that surcharges the member without a binding constraint to improve the objective value.

To show the equivalence between (i) and (iii), we introduce the following auxiliary problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | min(𝑨,𝒑,𝜼)∈ℐ​ℛ,𝒑>0⁡u​(𝑨,𝒑,𝜼)s.t. ​v​(𝜼,𝒑)≤cR,𝑨​𝝁+𝑫​(𝝁)​𝒑=𝝁, 1⊤​𝑨+𝒑⊤=𝟏⊤.\min\_{(\bm{A},\bm{p},\bm{\eta})\in\mathcal{IR},{\bm{p}>0}}u(\bm{A},\bm{p},\bm{\eta})\quad\text{s.t. }v(\bm{\eta},\bm{p})\leq c\_{R},\ \bm{A}\bm{\mu}+\bm{D}(\bm{\mu})\bm{p}=\bm{\mu},\ \mathbf{1}^{\top}\bm{A}+\bm{p}^{\top}=\bm{1}^{\top}. |  | (34) |

Suppose that (𝑨∗,𝒑∗,𝜼∗)∈𝒥​𝒫​𝒪(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*})\in\mathcal{JPO} and let cR=v​(𝜼∗,𝒑∗)c\_{R}=v(\bm{\eta}\_{\*},\bm{p}\_{\*}). Assume the contrary that (𝑨∗,𝒑∗,𝜼∗)(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*}) does not solve Problem ([34](https://arxiv.org/html/2602.14223v1#A3.E34 "In Appendix C Proof of Theorem 3.4 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")). Then, there exists (𝑨”,𝒑”,𝜼”)∈ℐ​ℛ(\bm{A}^{"},\bm{p}^{"},\bm{\eta}^{"})\in\mathcal{IR} that solves Problem ([34](https://arxiv.org/html/2602.14223v1#A3.E34 "In Appendix C Proof of Theorem 3.4 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), with u​(𝑨”,𝒑”,𝜼”)<u​(𝑨∗,𝒑∗,𝜼∗)u(\bm{A}^{"},\bm{p}^{"},\bm{\eta}^{"})<u(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*}) and v​(𝜼”,𝒑”)≤cRv(\bm{\eta}^{"},\bm{p}^{"})\leq c\_{R}.
Fix i∈{1,…,n}i\in\{1,\ldots,n\}, and for j≠ij\neq i, define ϵ¯j:=uj​(𝑨∗,𝒑∗,𝜼∗)−uj​(𝑨”,𝒑”,𝜼”)\overline{\epsilon}\_{j}:=u\_{j}(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*})-u\_{j}(\bm{A}^{"},\bm{p}^{"},\bm{\eta}^{"}), ηj>=ηj”+ϵ¯jpj”​μj\eta\_{j}^{>}=\eta\_{j}^{"}+\frac{\overline{\epsilon}\_{j}}{p\_{j}^{"}\mu\_{j}}, and ηi>=ηi”−∑j≠iϵ¯jpi”​μi\eta\_{i}^{>}=\eta\_{i}^{"}-\frac{\sum\_{j\neq i}\overline{\epsilon}\_{j}}{p\_{i}^{"}\mu\_{i}}.
Then, we have uj​(𝑨”,𝒑”,𝜼>)=uj​(𝑨”,𝒑”,𝜼”)+ϵ¯j=uj​(𝑨∗,𝒑∗,𝜼∗)u\_{j}(\bm{A}^{"},\bm{p}^{"},\bm{\eta}^{>})=u\_{j}(\bm{A}^{"},\bm{p}^{"},\bm{\eta}^{"})+\overline{\epsilon}\_{j}=u\_{j}(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*}), v​(𝜼>,𝒑”)=v​(𝜼”,𝒑”)v(\bm{\eta}^{>},\bm{p}^{"})=v(\bm{\eta}^{"},\bm{p}^{"}), and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ui​(𝑨”,𝒑”,𝜼>)=\displaystyle u\_{i}(\bm{A}^{"},\bm{p}^{"},\bm{\eta}^{>})= | ui​(𝑨”,𝒑”,𝜼”)−∑j≠iϵ¯j\displaystyle u\_{i}(\bm{A}^{"},\bm{p}^{"},\bm{\eta}^{"})-\sum\_{j\neq i}{\bar{\epsilon}\_{j}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ui​(𝑨”,𝒑”,𝜼”)−∑j≠i(uj​(𝑨∗,𝒑∗,𝜼∗)−uj​(𝑨”,𝒑”,𝜼”))\displaystyle u\_{i}(\bm{A}^{"},\bm{p}^{"},\bm{\eta}^{"})-\sum\_{j\neq i}(u\_{j}(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*})-u\_{j}(\bm{A}^{"},\bm{p}^{"},\bm{\eta}^{"})) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | u​(𝑨”,𝒑”,𝜼”)−∑j≠iuj​(𝑨∗,𝒑∗,𝜼∗)\displaystyle u(\bm{A}^{"},\bm{p}^{"},\bm{\eta}^{"})-\sum\_{j\neq i}u\_{j}(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | u​(𝑨”,𝒑”,𝜼”)−u​(𝑨∗,𝒑∗,𝜼∗)+ui​(𝑨∗,𝒑∗,𝜼∗)<ui​(𝑨∗,𝒑∗,𝜼∗),\displaystyle u(\bm{A}^{"},\bm{p}^{"},\bm{\eta}^{"})-u(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*})+u\_{i}(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*})<u\_{i}(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*}), |  |

contradicting the JP-optimality of (𝑨∗,𝒑∗,𝜼∗)(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*}).

Conversely, suppose that (𝑨∗,𝒑∗,𝜼∗)(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*}) solves Problem ([34](https://arxiv.org/html/2602.14223v1#A3.E34 "In Appendix C Proof of Theorem 3.4 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")). Assume the contrary that (𝑨∗,𝒑∗,𝜼∗)(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*}) is not JP-optimal and there exists (𝑨@,𝒑@,𝜼@)∈ℐ​ℛ(\bm{A}^{@},\bm{p}^{@},\bm{\eta}^{@})\in\mathcal{IR} such that ui​(𝑨@,𝒑@,𝜼@)≤ui​(𝑨∗,𝒑∗,𝜼∗)u\_{i}(\bm{A}^{@},\bm{p}^{@},\bm{\eta}^{@})\leq u\_{i}(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*}) for all i=1,…,ni=1,\ldots,n, and v​(𝜼@,𝒑@)≤v​(𝜼∗,𝒑∗)v(\bm{\eta}^{@},\bm{p}^{@})\leq v(\bm{\eta}\_{\*},\bm{p}\_{\*}),
with at least one of these inequalities being strict. The first nn inequalities must be equalities; otherwise, it violates the optimality of (𝑨∗,𝒑∗,𝜼∗)(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*}). Then, we have v​(𝜼@,𝒑@)<v​(𝜼∗,𝒑∗)v(\bm{\eta}^{@},\bm{p}^{@})<v(\bm{\eta}\_{\*},\bm{p}\_{\*}).
Define ϵ¯=v​(𝜼∗,𝒑∗)−v​(𝜼@,𝒑@)>0\underline{\epsilon}=v(\bm{\eta}\_{\*},\bm{p}\_{\*})-v(\bm{\eta}^{@},\bm{p}^{@})>0 and
ηi<=ηi@−ϵ¯/n​pi@​μi\eta\_{i}^{<}=\eta\_{i}^{@}-\underline{\epsilon}/np\_{i}^{@}\mu\_{i}. Then, ui​(𝑨@,𝒑@,𝜼<)=ui​(𝑨@,𝒑@,𝜼@)−ϵ¯n<ui​(𝑨@,𝒑@,𝜼@)u\_{i}(\bm{A}^{@},\bm{p}^{@},\bm{\eta}^{<})=u\_{i}(\bm{A}^{@},\bm{p}^{@},\bm{\eta}^{@})-\frac{\underline{\epsilon}}{n}<u\_{i}(\bm{A}^{@},\bm{p}^{@},\bm{\eta}^{@}).
This implies u​(𝑨@,𝒑@,𝜼<)<u​(𝑨@,𝒑@,𝜼@)=u​(𝑨∗,𝒑∗,𝜼∗)u(\bm{A}^{@},\bm{p}^{@},\bm{\eta}^{<})<u(\bm{A}^{@},\bm{p}^{@},\bm{\eta}^{@})=u(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*}) and v​(𝜼∗,𝒑∗)=v​(𝜼@,𝒑@)+ϵ¯=v​(𝜼<,𝒑@)v(\bm{\eta}\_{\*},\bm{p}\_{\*})=v(\bm{\eta}^{@},\bm{p}^{@})+\underline{\epsilon}=v(\bm{\eta}^{<},\bm{p}^{@}), contradicting the optimality of (𝑨∗,𝒑∗,𝜼∗)(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*}).

Finally, we observe that Problem ([34](https://arxiv.org/html/2602.14223v1#A3.E34 "In Appendix C Proof of Theorem 3.4 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) reaches optimality when the inequality constraint becomes an equality, i.e., Problem ([9](https://arxiv.org/html/2602.14223v1#S3.E9 "In item (iii) ‣ Theorem 3.4. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")); otherwise, the loadings can be adjusted to improve the objective value.

## Appendix D Proof of Theorem [3.5](https://arxiv.org/html/2602.14223v1#S3.Thmtheorem5 "Theorem 3.5. ‣ 3.2.1 Coalitional stability and the core ‣ 3.2 Cooperative game study on premium decision ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")

We first define an auxiliary game (𝒯,b)(\mathcal{T},b) that includes only coalitions with the reinsurer, where 𝒯:={1,…,n}\mathcal{T}:=\{1,\dots,n\} and b:2𝒯↦ℝb:2^{\mathcal{T}}\mapsto\mathbb{R} such that b​(𝒮∪ℛ):=ℬ​(𝒮∪ℛ)b(\mathcal{S}\cup\mathcal{R}):=\mathcal{B}(\mathcal{S}\cup\mathcal{R}).
The corresponding core is defined as

|  |  |  |
| --- | --- | --- |
|  | c​o​r​e​(𝒯,b):={𝒄∈ℝ+n+1:∑i∈𝒮∪ℛci≥b​(𝒮∪ℛ),∑i∈𝒯∪ℛci=b​(𝒯∪ℛ), for all ​∅≠𝒮⊆𝒯}.core(\mathcal{T},b):=\left\{\bm{c}\in\mathbb{R}^{n+1}\_{+}:\sum\_{i\in\mathcal{S}\cup\mathcal{R}}c\_{i}\geq b(\mathcal{S}\cup\mathcal{R}),\ \sum\_{i\in\mathcal{T}\cup\mathcal{R}}{c\_{i}}=b(\mathcal{T}\cup\mathcal{R}),\ \text{ for all }\emptyset\neq\mathcal{S}\subseteq\mathcal{T}\right\}. |  |

Note that c​o​r​e​(𝒯,b)core(\mathcal{T},b) is not empty since (0,…,0,b​(𝒯∪ℛ))∈c​o​r​e​(𝒯,b)(0,\dots,0,b(\mathcal{T}\cup\mathcal{R}))\in core(\mathcal{T},b). By the Bondareva-Shapley theorem (see, e.g., Osborne and Rubinstein, [1994](https://arxiv.org/html/2602.14223v1#bib.bib52 "A course in game theory"), Proposition 262.1), (𝒯,b)(\mathcal{T},b) is balanced, i.e., ∑𝒮⊆𝒯λ𝒮​b​(𝒮∪ℛ)≤b​(𝒯∪ℛ)\sum\_{\mathcal{S}\subseteq\mathcal{T}}\lambda\_{\mathcal{S}}b(\mathcal{S}\cup\mathcal{R})\leq b(\mathcal{T}\cup\mathcal{R})
for all
λ𝒮∈[0,1]\lambda\_{\mathcal{S}}\in[0,1] such that ∑𝒮⊆𝒯λ𝒮​𝒆𝒮=𝒆𝒯\sum\_{\mathcal{S}\subseteq\mathcal{T}}\lambda\_{\mathcal{S}}\bm{e}\_{\mathcal{S}}=\bm{e}\_{\mathcal{T}}, where 𝒆𝒮∈ℝn\bm{e}\_{\mathcal{S}}\in\mathbb{R}^{n} is the characteristic vector of the subset 𝒮\mathcal{S} such that (𝒆𝒮)i=1(\bm{e}\_{\mathcal{S}})\_{i}=1 if i∈𝒮i\in\mathcal{S}, and (𝒆𝒮)i=0(\bm{e}\_{\mathcal{S}})\_{i}=0 otherwise.

Next,
for any 𝒞⊊𝒩\mathcal{C}\subsetneq\mathcal{N} with R∉𝒞R\notin\mathcal{C}, let (𝑨∗𝒞∪ℛ,𝒑∗𝒞∪ℛ)(\bm{A}\_{\*}^{\mathcal{C}\cup\mathcal{R}},\bm{p}\_{\*}^{\mathcal{C}\cup\mathcal{R}}) and 𝑨∗𝒞\bm{A}\_{\*}^{\mathcal{C}} be the optimal solution to Problem ([10](https://arxiv.org/html/2602.14223v1#S3.E10 "In 3.2 Cooperative game study on premium decision ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) and Problem ([11](https://arxiv.org/html/2602.14223v1#S3.E11 "In 3.2 Cooperative game study on premium decision ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), respectively.
Since Problem ([11](https://arxiv.org/html/2602.14223v1#S3.E11 "In 3.2 Cooperative game study on premium decision ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) can be considered as Problem ([10](https://arxiv.org/html/2602.14223v1#S3.E10 "In 3.2 Cooperative game study on premium decision ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) with an additional constraint 𝒑𝒞=𝟎𝒞\bm{p}^{\mathcal{C}}=\bm{0}^{\mathcal{C}}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i∈𝒞ρi​(𝑨∗𝒞∪ℛ;𝒞)+ρR​(𝒑∗𝒞∪ℛ;𝒞∪ℛ)≤∑i∈𝒞ρi​(𝑨∗𝒞;𝒞).\sum\_{i\in\mathcal{C}}\rho\_{i}(\bm{A}\_{\*}^{\mathcal{C}\cup\mathcal{R}};\mathcal{C})+\rho\_{R}(\bm{p}\_{\*}^{\mathcal{C}\cup\mathcal{R}};\mathcal{C}\cup\mathcal{R})\leq\sum\_{i\in\mathcal{C}}\rho\_{i}(\bm{A}\_{\*}^{\mathcal{C}};\mathcal{C}). |  | (35) |

To prove c​o​r​e​(𝒩,ℬ)≠∅core(\mathcal{N},\mathcal{B})\neq\emptyset, we again invoke the Bondareva-Shapley theorem and show that (𝒩,ℬ)(\mathcal{N},\mathcal{B}) is balanced.
Let 𝒆¯𝒞∈ℝn+1\bm{\overline{e}}\_{\mathcal{C}}\in\mathbb{R}^{n+1} be the characteristic vector of the subset 𝒞⊆𝒩\mathcal{C}\subseteq\mathcal{N} such that (𝒆¯𝒞)i=1(\bm{\overline{e}}\_{\mathcal{C}})\_{i}=1 if i∈𝒞i\in\mathcal{C}, and (𝒆¯𝒞)i=0(\bm{\overline{e}}\_{\mathcal{C}})\_{i}=0 otherwise.
For any 𝒞⊆𝒩\mathcal{C}\subseteq\mathcal{N} and λ¯𝒞∈[0,1]\overline{\lambda}\_{\mathcal{C}}\in[0,1] such that ∑𝒞⊆𝒩λ¯𝒞​𝒆¯𝒞=𝒆¯𝒩\sum\_{\mathcal{C}\subseteq\mathcal{N}}\overline{\lambda}\_{\mathcal{C}}\bm{\overline{e}}\_{\mathcal{C}}=\bm{\overline{e}}\_{\mathcal{N}},
we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑𝒞⊆𝒩λ¯𝒞​ℬ​(𝒞)=\displaystyle\sum\_{\mathcal{C}\subseteq\mathcal{N}}\overline{\lambda}\_{\mathcal{C}}\mathcal{B}(\mathcal{C})= | ∑𝒞⊆𝒩λ¯𝒞[1R∈𝒞(∑i∈𝒞\ℛ(μi+γi​σi22)−∑i∈𝒞\ℛρi(𝑨∗𝒞;𝒞\ℛ)−ρR(𝒑∗𝒞;𝒞))\displaystyle\sum\_{\mathcal{C}\subseteq\mathcal{N}}\overline{\lambda}\_{\mathcal{C}}\left[1\_{R\in\mathcal{C}}\left(\sum\_{i\in\mathcal{C}\backslash\mathcal{R}}\left(\mu\_{i}+\frac{\gamma\_{i}\sigma\_{i}^{2}}{2}\right)-\sum\_{i\in\mathcal{C}\backslash\mathcal{R}}\rho\_{i}(\bm{A}\_{\*}^{\mathcal{C}};\mathcal{C}\backslash\mathcal{R})-\rho\_{R}(\bm{p}\_{\*}^{\mathcal{C}};{\mathcal{C}})\right)\right. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +1R∉𝒞(∑i∈𝒞(μi+γi​σi22)−∑i∈𝒞ρi(𝑨∗𝒞;𝒞))]\displaystyle+\left.1\_{R\notin\mathcal{C}}\left(\sum\_{i\in\mathcal{C}}\left(\mu\_{i}+\frac{\gamma\_{i}\sigma\_{i}^{2}}{2}\right)-\sum\_{i\in\mathcal{C}}\rho\_{i}(\bm{A}\_{\*}^{\mathcal{C}};\mathcal{C})\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | ∑𝒞⊆𝒩λ¯𝒞[1R∈𝒞(∑i∈𝒞\ℛ(μi+γi​σi22)−(∑i∈𝒞\ℛρi(𝑨∗𝒞;𝒞\ℛ)+ρR(𝒑∗𝒞;𝒞)))\displaystyle\sum\_{\mathcal{C}\subseteq\mathcal{N}}\overline{\lambda}\_{\mathcal{C}}\left[1\_{R\in\mathcal{C}}\left(\sum\_{i\in\mathcal{C}\backslash\mathcal{R}}\left(\mu\_{i}+\frac{\gamma\_{i}\sigma\_{i}^{2}}{2}\right)-\left(\sum\_{i\in\mathcal{C}\backslash\mathcal{R}}\rho\_{i}(\bm{A}\_{\*}^{\mathcal{C}};\mathcal{C}\backslash\mathcal{R})+\rho\_{R}(\bm{p}\_{\*}^{\mathcal{C}};\mathcal{C})\right)\right)\right. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +1R∉𝒞(∑i∈𝒞(μi+γi​σi22)−(∑i∈𝒞ρi(𝑨∗𝒞∪ℛ;𝒞)+ρR(𝒑∗𝒞;𝒞∪ℛ)))]\displaystyle\left.+1\_{R\notin\mathcal{C}}\left(\sum\_{i\in\mathcal{C}}\left(\mu\_{i}+\frac{\gamma\_{i}\sigma\_{i}^{2}}{2}\right)-\left(\sum\_{i\in\mathcal{C}}\rho\_{i}(\bm{A}\_{\*}^{\mathcal{C}\cup\mathcal{R}};\mathcal{C})+\rho\_{R}(\bm{p}\_{\*}^{\mathcal{C}};\mathcal{C}\cup\mathcal{R})\right)\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∑𝒞⊊𝒩,𝒞∋Rλ¯𝒞​b​(𝒞)+∑𝒞⊊𝒩,𝒞∌Rλ¯𝒞​b​(𝒞∪ℛ)\displaystyle\ \sum\_{\mathcal{C}\subsetneq\mathcal{N},\mathcal{C}\ni R}\overline{\lambda}\_{\mathcal{C}}b(\mathcal{C})+\sum\_{\mathcal{C}\subsetneq\mathcal{N},\mathcal{C}\not\ni R}\overline{\lambda}\_{\mathcal{C}}b(\mathcal{C}\cup\mathcal{R}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∑𝒮⊆𝒯λ¯𝒮∪ℛ​b​(𝒮∪ℛ)+∑𝒮⊆𝒯λ¯𝒮​b​(𝒮∪ℛ)≤b​(𝒯∪ℛ)=ℬ​(𝒩),\displaystyle\ {\sum\_{\mathcal{S}\subseteq\mathcal{T}}\overline{\lambda}\_{\mathcal{S}\cup\mathcal{R}}b(\mathcal{S}\cup\mathcal{R})+\sum\_{\mathcal{S}\subseteq\mathcal{T}}\overline{\lambda}\_{\mathcal{S}}b(\mathcal{S}\cup\mathcal{R})}\leq b(\mathcal{T}\cup\mathcal{R})=\mathcal{B}(\mathcal{N}), |  |

where the first inequality follows from ([35](https://arxiv.org/html/2602.14223v1#A4.E35 "In Appendix D Proof of Theorem 3.5 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"))
, and
the second inequality follows from the fact that (𝒯,b)(\mathcal{T},b) is balanced and ∑𝒮⊆𝒯(λ¯𝒮∪ℛ+λ¯𝒮)​𝒆𝒮=𝒆𝒯\sum\_{\mathcal{S}\subseteq\mathcal{T}}(\overline{\lambda}\_{\mathcal{S}\cup\mathcal{R}}+\overline{\lambda}\_{\mathcal{S}})\bm{e}\_{\mathcal{S}}=\bm{e}\_{\mathcal{T}}. To see the last relation, note that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒆¯N=∑𝒞⊆𝒩λ¯𝒞​𝒆¯𝒞=∑𝒮⊆𝒯λ¯𝒮​𝒆¯𝒮+∑𝒮⊆𝒯λ¯𝒮∪ℛ​𝒆¯𝒮∪ℛ\displaystyle\bm{\overline{e}}\_{N}=\sum\_{\mathcal{C}\subseteq\mathcal{N}}\overline{\lambda}\_{\mathcal{C}}\bm{\overline{e}}\_{\mathcal{C}}=\sum\_{\mathcal{S}\subseteq\mathcal{T}}\overline{\lambda}\_{\mathcal{S}}\bm{\overline{e}}\_{\mathcal{S}}+\sum\_{\mathcal{S}\subseteq\mathcal{T}}\overline{\lambda}\_{\mathcal{S}\cup\mathcal{R}}\bm{\overline{e}}\_{\mathcal{S}\cup\mathcal{R}} | =∑𝒮⊆𝒯(λ¯𝒮+λ¯𝒮∪ℛ)​𝒆¯𝒮+∑𝒮⊆𝒯λ¯𝒮∪ℛ​(𝒆¯𝒮∪ℛ−𝒆¯𝒮)\displaystyle=\sum\_{\mathcal{S}\subseteq\mathcal{T}}\left(\overline{\lambda}\_{\mathcal{S}}+\overline{\lambda}\_{\mathcal{S}\cup\mathcal{R}}\right)\bm{\overline{e}}\_{\mathcal{S}}+\sum\_{\mathcal{S}\subseteq\mathcal{T}}\overline{\lambda}\_{\mathcal{S}\cup\mathcal{R}}(\bm{\overline{e}}\_{\mathcal{S}\cup\mathcal{R}}-\bm{\overline{e}}\_{\mathcal{S}}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑𝒮⊆𝒯(λ¯𝒮+λ¯𝒮∪ℛ)​𝒆¯𝒮+∑𝒮⊆𝒯λ¯𝒮∪ℛ​𝒆¯ℛ.\displaystyle=\sum\_{\mathcal{S}\subseteq\mathcal{T}}\left(\overline{\lambda}\_{\mathcal{S}}+\overline{\lambda}\_{\mathcal{S}\cup\mathcal{R}}\right)\bm{\overline{e}}\_{\mathcal{S}}+\sum\_{\mathcal{S}\subseteq\mathcal{T}}\overline{\lambda}\_{\mathcal{S}\cup\mathcal{R}}\bm{\overline{e}}\_{\mathcal{R}}. |  |

The claim thus follows from the linear independence of 𝒆¯𝒮\bm{\overline{e}}\_{\mathcal{S}}, 𝒮⊆𝒯\mathcal{S}\subseteq\mathcal{T}, and 𝒆¯ℛ\bm{\overline{e}}\_{\mathcal{R}}, and the proof is complete.

## Appendix E Proof of Proposition [3.6](https://arxiv.org/html/2602.14223v1#S3.Thmtheorem6 "Proposition 3.6. ‣ 3.2.1 Coalitional stability and the core ‣ 3.2 Cooperative game study on premium decision ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")

Let (c1,…,cn,cR)∈c​o​r​e​(𝒩,ℬ)(c\_{1},\dots,c\_{n},c\_{R})\in core(\mathcal{N},\mathcal{B}) and choose 𝜼∗=(η∗,1,…,η∗,n)\bm{\eta}\_{\*}=(\eta\_{\*,1},\dots,\eta\_{\*,n}) such that ωi=ωi​(𝑨∗,𝒑∗,𝜼∗)=ci\omega\_{i}=\omega\_{i}(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*})=c\_{i}, for i=1,…,ni=1,\dots,n. Note that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≤cR=ℬ​(𝒩)−∑i=1nωi\displaystyle 0\leq c\_{R}=\mathcal{B}(\mathcal{N})-\sum\_{i=1}^{n}\omega\_{i} | =∑i=1n(μi+γi​σi22−ρi​(𝑨∗))−ρR​(𝒑∗)−∑i=1n(μi+γi​σi22−ρi​(𝑨∗)−πi​(η∗,i,p∗,i))\displaystyle=\sum\_{i=1}^{n}\left(\mu\_{i}+\frac{\gamma\_{i}\sigma\_{i}^{2}}{2}-\rho\_{i}(\bm{A}\_{\*})\right)-\rho\_{R}(\bm{p}\_{\*})-\sum\_{i=1}^{n}\left(\mu\_{i}+\frac{\gamma\_{i}\sigma\_{i}^{2}}{2}-\rho\_{i}(\bm{A}\_{\*})-\pi\_{i}(\eta\_{\*,i},p\_{\*,i})\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑i=1nπi​(η∗,i,p∗,i)−ρR​(𝒑∗),\displaystyle=\sum\_{i=1}^{n}\pi\_{i}(\eta\_{\*,i},p\_{\*,i})-\rho\_{R}(\bm{p}\_{\*}), |  |

which implies ρR​(𝒑∗)≤∑i=1nπi​(η∗,i,p∗,i)\rho\_{R}(\bm{p}\_{\*})\leq\sum\_{i=1}^{n}\pi\_{i}(\eta\_{\*,i},p\_{\*,i}), i.e., the reinsurer’s IR ([4](https://arxiv.org/html/2602.14223v1#S2.E4 "In 2.3 Individual rationality ‣ 2 Model Formulations ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) is satisfied. In addition, for each i=1,…,ni=1,\dots,n, it holds that 0≤ci=ωi=μi+γi​σi22−ρi​(𝑨∗)−πi​(η∗,i,p∗,i),0\leq c\_{i}=\omega\_{i}=\mu\_{i}+\frac{\gamma\_{i}\sigma\_{i}^{2}}{2}-\rho\_{i}(\bm{A}\_{\*})-\pi\_{i}(\eta\_{\*,i},p\_{\*,i}),
which implies members’ IRs ([3](https://arxiv.org/html/2602.14223v1#S2.E3 "In 2.3 Individual rationality ‣ 2 Model Formulations ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) are also satisfied. As (𝑨∗,𝒑∗,𝜼∗)∈ℐ​ℛ(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\*})\in\mathcal{IR}, its JP-optimality follows from Theorem [3.4](https://arxiv.org/html/2602.14223v1#S3.Thmtheorem4 "Theorem 3.4. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").

## Appendix F Proof of Proposition [3.8](https://arxiv.org/html/2602.14223v1#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.2.1 Coalitional stability and the core ‣ 3.2 Cooperative game study on premium decision ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")

Assume that (𝑨,𝒑,𝜼)(\bm{A},\bm{p},\bm{\eta}) is not coalitional stable.
This induces two cases.

(i): There exists ∅≠𝒞⊊𝒩\emptyset\neq\mathcal{C}\subsetneq\mathcal{N}, R∈𝒞R\in\mathcal{C} and (𝑨ˇ𝒞,𝒑ˇ𝒞,𝜼ˇ𝒞)∈ℱ𝒞(\check{\bm{A}}^{\mathcal{C}},\check{\bm{p}}^{\mathcal{C}},\check{\bm{\eta}}^{\mathcal{C}})\in\mathcal{F}^{\mathcal{C}} such that ui​(𝑨ˇ𝒞,𝒑ˇ𝒞,𝜼ˇ𝒞;𝒞)≤ui​(𝑨,𝒑,𝜼;𝒩)u\_{i}(\check{\bm{A}}^{\mathcal{C}},\check{\bm{p}}^{\mathcal{C}},\check{\bm{\eta}}^{\mathcal{C}};\mathcal{C})\leq u\_{i}(\bm{A},\bm{p},\bm{\eta};\mathcal{N}) for all i∈𝒞i\in\mathcal{C}, and v​(𝜼ˇ𝒞,𝒑ˇ𝒞;𝒞)≤v​(𝜼,𝒑;𝒩)v(\check{\bm{\eta}}^{\mathcal{C}},\check{\bm{p}}^{\mathcal{C}};\mathcal{C})\leq v(\bm{\eta},\bm{p};\mathcal{N}),
with at least one strict inequality.
Note that 𝒞≠𝒩\mathcal{C}\neq\mathcal{N} since (𝑨,𝒑,𝜼)∈𝒥​𝒫​𝒪(\bm{A},\bm{p},\bm{\eta})\in\mathcal{JPO}. Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i∈𝒞ωi​(𝑨,𝒑,𝜼)=\displaystyle\sum\_{i\in\mathcal{C}}\omega\_{i}({\bm{A},\bm{p},\bm{\eta}})= | ∑i∈𝒞,i≠R(μi+γi​σi22−ui​(𝑨,𝒑,𝜼;𝒩))−v​(𝜼,𝒑;𝒩)\displaystyle\sum\_{i\in\mathcal{C},i\neq R}\left(\mu\_{i}+\frac{\gamma\_{i}\sigma\_{i}^{2}}{2}-{u\_{i}(\bm{A},\bm{p},\bm{\eta};\mathcal{N})}\right)-v(\bm{\eta},\bm{p};{\mathcal{N}}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | <\displaystyle< | ∑i∈𝒞,i≠R(μi+γi​σi22−ui​(𝑨ˇ𝒞,𝒑ˇ𝒞,𝜼ˇ𝒞;𝒞))−v​(𝜼ˇ𝒞,𝒑ˇ𝒞;𝒞)\displaystyle\sum\_{i\in\mathcal{C},i\neq R}\left(\mu\_{i}+\frac{\gamma\_{i}\sigma\_{i}^{2}}{2}{-u\_{i}(\check{\bm{A}}^{\mathcal{C}},\check{\bm{p}}^{\mathcal{C}},\check{\bm{\eta}}^{\mathcal{C}};\mathcal{C})}\right)-v(\check{\bm{\eta}}^{\mathcal{C}},\check{\bm{p}}^{\mathcal{C}};\mathcal{C}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | ∑i∈𝒞,i≠R(μi+γi​σi22)−min(𝑨𝒞,𝒑𝒞,𝜼𝒞)∈ℱ𝒞​∑i∈𝒞(ρi​(𝑨𝒞;𝒞)+ρR​(𝒑𝒞;𝒞))=ℬ​(𝒞).\displaystyle\sum\_{i\in\mathcal{C},i\neq R}\left(\mu\_{i}+\frac{\gamma\_{i}\sigma\_{i}^{2}}{2}\right)-\min\_{(\bm{A}^{\mathcal{C}},\bm{p}^{\mathcal{C}},\bm{\eta}^{\mathcal{C}})\in\mathcal{F}^{\mathcal{C}}}{\sum\_{i\in\mathcal{C}}}\left(\rho\_{i}(\bm{A}^{\mathcal{C}};\mathcal{C})+\rho\_{R}(\bm{p}^{\mathcal{C}};\mathcal{C})\right)=\mathcal{B}(\mathcal{C}). |  |

(ii): There exists ∅≠𝒞⊊𝒩\emptyset\neq\mathcal{C}\subsetneq\mathcal{N}, R∉𝒞R\notin\mathcal{C} and 𝑨ˇ𝒞∈ℱ𝒞\check{\bm{A}}^{\mathcal{C}}\in\mathcal{F}^{\mathcal{C}} such that ui​(𝑨ˇ𝒞,𝟎𝒞,𝟎𝒞;𝒞)≤ui​(𝑨,𝒑,𝜼;𝒩)u\_{i}(\check{\bm{A}}^{\mathcal{C}},\bm{0}^{\mathcal{C}},\bm{0}^{\mathcal{C}};\mathcal{C})\leq u\_{i}(\bm{A},\bm{p},\bm{\eta};\mathcal{N}) for all i∈𝒞i\in\mathcal{C},
with at least one strict inequality. Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i∈𝒞ωi​(𝑨,𝒑,𝜼)=∑i∈𝒞(μi+γi​σi22−ui​(𝑨,𝒑,𝜼;𝒩))\displaystyle\sum\_{i\in\mathcal{C}}\omega\_{i}({\bm{A},\bm{p},\bm{\eta}})=\sum\_{i\in\mathcal{C}}\left(\mu\_{i}+\frac{\gamma\_{i}\sigma\_{i}^{2}}{2}-{u\_{i}(\bm{A},\bm{p},\bm{\eta};\mathcal{N})}\right) | <∑i∈𝒞(μi+γi​σi22−ui​(𝑨ˇ𝒞,𝟎𝒞,𝟎𝒞;𝒞))\displaystyle<\sum\_{i\in\mathcal{C}}\left(\mu\_{i}+\frac{\gamma\_{i}\sigma\_{i}^{2}}{2}{-u\_{i}(\check{\bm{A}}^{\mathcal{C}},\bm{0}^{\mathcal{C}},\bm{0}^{\mathcal{C}};\mathcal{C})}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∑i∈𝒞(μi+γi​σi22)−min𝑨𝒞∈ℱ𝒞​∑i∈𝒞ρi​(𝑨𝒞;𝒞)=ℬ​(𝒞),\displaystyle\leq\sum\_{i\in\mathcal{C}}\left(\mu\_{i}+\frac{\gamma\_{i}\sigma\_{i}^{2}}{2}\right)-\min\_{\bm{A}^{\mathcal{C}}\in\mathcal{F}^{\mathcal{C}}}{\sum\_{i\in\mathcal{C}}}\rho\_{i}(\bm{A}^{\mathcal{C}};\mathcal{C})=\mathcal{B}(\mathcal{C}), |  |

As the above two cases indicate
(ω1(𝑨,𝒑,𝜼),…,ωn(𝑨,𝒑,𝜼),ℬ(𝒩)−∑i=1nωi(𝑨,𝒑,𝜼)))∉core(𝒩,ℬ)(\omega\_{1}({\bm{A},\bm{p},\bm{\eta}}),\dots,\omega\_{n}({\bm{A},\bm{p},\bm{\eta}}),\mathcal{B}(\mathcal{N})-\sum\_{i=1}^{n}\omega\_{i}({\bm{A},\bm{p},\bm{\eta}})))\not\in core(\mathcal{N},\mathcal{B}) and contradiction arises, the proof is complete.

## Appendix G Proof of Proposition [3.9](https://arxiv.org/html/2602.14223v1#S3.Thmtheorem9 "Proposition 3.9 (Nonnegative loading in the core). ‣ 3.2.2 Practical premium suggestions ‣ 3.2 Cooperative game study on premium decision ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")

To prove the first statement, it suffices to show that ωi​(𝑨∗,𝒑∗,max⁡{𝟎,𝜼min​(𝒑∗)})≥0\omega\_{i}(\bm{A}\_{\*},\bm{p}\_{\*},\max\{\bm{0},\bm{\eta}\_{\min}(\bm{p}\_{\*})\})\geq 0 for all i∈𝒩i\in\mathcal{N}.
Using ([6](https://arxiv.org/html/2602.14223v1#S3.E6 "In Proposition 3.3. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), the ii-th row of 𝑨∗\bm{A}\_{\*} is given by

|  |  |  |
| --- | --- | --- |
|  | 𝑨∗,i=γi−1∑j=1nγj−1​𝟏⊤​𝑫​(𝟏−𝒑∗)+k​(α∗,i−α¯∗,i)​𝝁⊤​𝚺−1,\bm{A}\_{\*,i}=\frac{\gamma\_{i}^{-1}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\bm{1}^{\top}\bm{D}(\bm{1}-\bm{p}\_{\*})+k(\alpha\_{\*,i}-\bar{\alpha}\_{\*,i})\bm{\mu}^{\top}\bm{\Sigma}^{-1}, |  |

where α∗,i:=(1−p∗,i)​μi\alpha\_{\*,i}:=(1-p\_{\*,i})\mu\_{i} and α¯∗,i=γi−1​∑j=1n(1−p∗,j)​μj/∑j=1nγj−1\bar{\alpha}\_{\*,i}=\gamma\_{i}^{-1}\sum\_{j=1}^{n}(1-p\_{\*,j})\mu\_{j}/\sum\_{j=1}^{n}\gamma\_{j}^{-1}. Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑨∗,i​𝚺​𝑨∗,i⊤\displaystyle\bm{A}\_{\*,i}\bm{\Sigma}\bm{A}\_{\*,i}^{\top} | =(γi−1∑j=1nγj−1)2​𝟏⊤​𝑫​(𝟏−𝒑∗)​𝚺​𝑫​(𝟏−𝒑∗)​𝟏+2​k​γi−1​(α∗,i−α¯∗,i)∑j=1nγj−1​𝝁⊤​𝑫​(𝟏−𝒑∗)​𝟏\displaystyle=\left(\frac{\gamma\_{i}^{-1}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\right)^{2}\bm{1}^{\top}\bm{D}(\bm{1}-\bm{p}\_{\*})\bm{\Sigma}\bm{D}(\bm{1}-\bm{p}\_{\*})\bm{1}+\frac{2k\gamma\_{i}^{-1}(\alpha\_{\*,i}-\bar{\alpha}\_{\*,i})}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\bm{\mu}^{\top}\bm{D}(\bm{1}-\bm{p}\_{\*})\bm{1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +k2​(α∗,i−α¯∗,i)2​𝝁⊤​𝚺−1​𝝁\displaystyle+k^{2}(\alpha\_{\*,i}-\bar{\alpha}\_{\*,i})^{2}\bm{\mu}^{\top}\bm{\Sigma}^{-1}\bm{\mu} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(γi−1∑j=1nγj−1)2​𝟏⊤​𝑫​(𝟏−𝒑∗)​𝚺​𝑫​(𝟏−𝒑∗)​𝟏+2​k​α¯∗,i​(α∗,i−α¯∗,i)+k​(α∗,i−α¯∗,i)2\displaystyle=\left(\frac{\gamma\_{i}^{-1}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\right)^{2}\bm{1}^{\top}\bm{D}(\bm{1}-\bm{p}\_{\*})\bm{\Sigma}\bm{D}(\bm{1}-\bm{p}\_{\*})\bm{1}+2k\bar{\alpha}\_{\*,i}(\alpha\_{\*,i}-\bar{\alpha}\_{\*,i})+k(\alpha\_{\*,i}-\bar{\alpha}\_{\*,i})^{2} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =(γi−1∑j=1nγj−1)2​∑j,l=1n(1−p∗,j)​(1−p∗,l)​σj​l+k​((α∗,i)2−(α¯∗,i)2).\displaystyle=\left(\frac{\gamma\_{i}^{-1}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\right)^{2}\sum\_{j,l=1}^{n}(1-p\_{\*,j})(1-p\_{\*,l})\sigma\_{jl}+k((\alpha\_{\*,i})^{2}-(\bar{\alpha}\_{\*,i})^{2}). |  | (36) |

Using this, we have, for i=1,…,ni=1,\dots,n,

|  |  |  |
| --- | --- | --- |
|  | ωi​(𝑨∗,𝒑∗,𝜼min​(𝒑∗))\displaystyle\qquad\omega\_{i}(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\min}(\bm{p}\_{\*})) |  |
|  |  |  |
| --- | --- | --- |
|  | =γi2​(σi2−𝑨∗,i​𝚺​𝑨∗,i⊤)−ηmin,i​p∗,i​μi\displaystyle=\frac{\gamma\_{i}}{2}\left(\sigma\_{i}^{2}-\bm{A}\_{\*,i}\bm{\Sigma}\bm{A}\_{\*,i}^{\top}\right)-\eta\_{\min,i}p\_{\*,i}\mu\_{i} |  |
|  |  |  |
| --- | --- | --- |
|  | =γi2​(σi2−(γi−1∑j=1nγj−1)2​∑j,l=1n(1−p∗,j)​(1−p∗,l)​σj​l−k​((α∗,i)2−(α¯∗,i)2))−γR2​p∗,i​∑m=1nσi​m​p∗,m\displaystyle=\frac{\gamma\_{i}}{2}\left(\sigma\_{i}^{2}-\left(\frac{\gamma\_{i}^{-1}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\right)^{2}\sum\_{j,l=1}^{n}(1-p\_{\*,j})(1-p\_{\*,l})\sigma\_{jl}-k((\alpha\_{\*,i})^{2}-(\bar{\alpha}\_{\*,i})^{2})\right)-\frac{\gamma\_{R}}{2}p\_{\*,i}\sum\_{m=1}^{n}\sigma\_{im}p\_{\*,m} |  |
|  |  |  |
| --- | --- | --- |
|  | ≥γi2​(σi2−(γi−1∑j=1nγj−1)2​∑j,l=1n(σj​l)+−k​(α∗,i)2)−γR2​∑m=1n(σi​m)+\displaystyle\geq\frac{\gamma\_{i}}{2}\left(\sigma\_{i}^{2}-\left(\frac{\gamma\_{i}^{-1}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\right)^{2}\sum\_{j,l=1}^{n}(\sigma\_{jl})\_{+}-k(\alpha\_{\*,i})^{2}\right)-\frac{\gamma\_{R}}{2}\sum\_{m=1}^{n}(\sigma\_{im})\_{+} |  |
|  |  |  |
| --- | --- | --- |
|  | ≥γi2​(σi2−(γi−1∑j=1nγj−1)2​∑j,l=1n(σj​l)+−k​μi2)−γR2​∑m=1n(σi​m)+≥0,\displaystyle\geq\frac{\gamma\_{i}}{2}\left(\sigma\_{i}^{2}-\left(\frac{\gamma\_{i}^{-1}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\right)^{2}\sum\_{j,l=1}^{n}(\sigma\_{jl})\_{+}-k\mu\_{i}^{2}\right)-\frac{\gamma\_{R}}{2}\sum\_{m=1}^{n}(\sigma\_{im})\_{+}\geq 0, |  |

where the second equality results from ([13](https://arxiv.org/html/2602.14223v1#S3.E13 "In 3.2.2 Practical premium suggestions ‣ 3.2 Cooperative game study on premium decision ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")),
the first inequality follows from the fact that p∗,i∈[0,1]p\_{\*,i}\in[0,1] under ([7](https://arxiv.org/html/2602.14223v1#S3.E7 "In Proposition 3.3. ‣ 3.1 Characterization of Joint-Pareto optimality ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), and the second inequality follows from ([14](https://arxiv.org/html/2602.14223v1#S3.E14 "In Proposition 3.9 (Nonnegative loading in the core). ‣ 3.2.2 Practical premium suggestions ‣ 3.2 Cooperative game study on premium decision ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")). Following a similar argument, one can also obtain ωi​(𝑨∗,𝒑∗,𝟎)≥0\omega\_{i}(\bm{A}\_{\*},\bm{p}\_{\*},\bm{0})\geq 0.

To verify the reinsurer’s welfare gain is non-negative if 𝜼≥max⁡{𝟎,𝜼min​(𝒑∗)}\bm{\eta}\geq\max\{\bm{0},\bm{\eta}\_{\min}(\bm{p}\_{\*})\}, it suffices to show that ωR​(𝑨∗,𝒑∗,𝜼min​(𝒑∗))≥0\omega\_{R}(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\min}(\bm{p}\_{\*}))\geq 0, since ωR​(𝑨∗,𝒑∗,𝜼min​(𝒑∗))≤ωR​(𝑨∗,𝒑∗,𝜼)\omega\_{R}(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}\_{\min}(\bm{p}\_{\*}))\leq\omega\_{R}(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}). Indeed, γR2​𝒑∗⊤​𝚺​𝒑∗=𝒑∗⊤​𝑫​(𝝁)​𝜼min​(𝒑∗)≤(𝑫​(𝝁)​𝜼)⊤​𝒑∗.\frac{\gamma\_{R}}{2}\bm{p}\_{\*}^{\top}\bm{\Sigma}\bm{p}\_{\*}={\bm{p}\_{\*}^{\top}\bm{D}(\bm{\mu})\bm{\eta}\_{\min}(\bm{p}\_{\*})}\leq(\bm{D}(\bm{\mu})\bm{\eta})^{\top}\bm{p}\_{\*}. Therefore, the proof of the first statement is complete.

For the second statement, note that for any 𝒄∈c​o​r​e​(𝒩,ℬ)\bm{c}\in core(\mathcal{N},\mathcal{B}), we have ℬ​(𝒩)−ci=∑j≠ici≥ℬ​(𝒩\{i})\mathcal{B}(\mathcal{N})-c\_{i}=\sum\_{j\neq i}c\_{i}\geq\mathcal{B}(\mathcal{N}\backslash\{i\}) for all i=1,…,ni=1,\dots,n.
This leads to ci≤ℬ​(𝒩)−ℬ​(𝒩\{i})c\_{i}\leq\mathcal{B}(\mathcal{N})-\mathcal{B}(\mathcal{N}\backslash\{i\}). Then, imposing ([15](https://arxiv.org/html/2602.14223v1#S3.E15 "In Proposition 3.9 (Nonnegative loading in the core). ‣ 3.2.2 Practical premium suggestions ‣ 3.2 Cooperative game study on premium decision ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"))
means each member has an excess welfare gain to pay max⁡{𝟎,𝜼min​(𝒑∗)}\max\{\bm{0},\bm{\eta}\_{\min}(\bm{p}\_{\*})\} after joining the program.
Then, by invoking Proposition [3.6](https://arxiv.org/html/2602.14223v1#S3.Thmtheorem6 "Proposition 3.6. ‣ 3.2.1 Coalitional stability and the core ‣ 3.2 Cooperative game study on premium decision ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"), we can construct a JP-optimal contract with nonnegative loading.

## Appendix H Proof of Corollary [3.10](https://arxiv.org/html/2602.14223v1#S3.Thmtheorem10 "Corollary 3.10 (Single loading in the core). ‣ 3.2.2 Practical premium suggestions ‣ 3.2 Cooperative game study on premium decision ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")

Let 𝜼(1)\bm{\eta}^{(1)} and 𝜼(2)\bm{\eta}^{(2)} be the safety loadings given in the statement. Define n¯:=maxi⁡ηi(2)\underline{n}:=\max\_{i}\eta\_{i}^{(2)} and n¯:=mini⁡ηi(1)\overline{n}:=\min\_{i}\eta\_{i}^{(1)}. For any scalar t∈[n¯,n¯]t\in[\underline{n},\overline{n}], set a uniform loading t​𝟏t\bm{1}, and define the associated welfare gains by 𝝎​(t)\bm{\omega}(t), i.e., ωi​(t):=ωi​(𝑨∗,𝒑∗,t​𝟏)=ωi​(𝑨∗,𝒑∗,𝟎)−t​p∗,i​μi\omega\_{i}(t):=\omega\_{i}(\bm{A}\_{\*},\bm{p}\_{\*},t\bm{1})=\omega\_{i}(\bm{A}\_{\*},\bm{p}\_{\*},\bm{0})-tp\_{\*,i}\mu\_{i} for all i=1,…,ni=1,\dots,n, and ωR​(t):=ωR​(𝑨∗,𝒑∗,t​𝟏)=ℬ​(𝒩)−∑i=1nωi​(t)\omega\_{R}(t):=\omega\_{R}(\bm{A}\_{\*},\bm{p}\_{\*},t\bm{1})=\mathcal{B}(\mathcal{N})-\sum\_{i=1}^{n}\omega\_{i}(t).
Note that the efficiency constraint is satisfied as ∑i∈𝒩ωi​(t)=ℬ​(𝒩)\sum\_{i\in\mathcal{N}}\omega\_{i}(t)=\mathcal{B}(\mathcal{N}).

Next, we show that ωi​(t)≥0\omega\_{i}(t)\geq 0 for all i∈𝒩i\in\mathcal{N}. As t≤n¯≤ηi(1)t\leq\overline{n}\leq\eta\_{i}^{(1)} for all i=1,…,ni=1,\ldots,n, we have

|  |  |  |
| --- | --- | --- |
|  | ωi​(t)=ωi​(0)−t​p∗,i​μi≥ωi​(0)−ηi(1)​p∗,i​μi=ci(1):=ωi​(𝑨∗,𝒑∗,𝜼(1)).\omega\_{i}(t)=\omega\_{i}(0)-tp\_{\*,i}\mu\_{i}\geq\omega\_{i}(0)-\eta\_{i}^{(1)}p\_{\*,i}\mu\_{i}=c\_{i}^{(1)}:=\omega\_{i}(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}^{(1)}). |  |

Similarly, since t≤n¯≤ηi(2)t\leq\underline{n}\leq\eta\_{i}^{(2)} for all i=1,…,ni=1,\ldots,n, we obtain ωi​(t)≤ωi​(0)−ηi(2)​p∗,i​μi=ci(2):=ωi​(𝑨∗,𝒑∗,𝜼(2))\omega\_{i}(t)\leq\omega\_{i}(0)-\eta\_{i}^{(2)}p\_{\*,i}\mu\_{i}=c\_{i}^{(2)}:=\omega\_{i}(\bm{A}\_{\*},\bm{p}\_{\*},\bm{\eta}^{(2)}).
These two inequalities lead to ωi​(t)≥ci(1)≥0\omega\_{i}(t)\geq c\_{i}^{(1)}\geq 0 and ωR​(t)=ℬ​(𝒩)−∑i=1nωi​(t)≥ℬ​(𝒩)−∑i=1nci(2)=ωR(2)≥0.\omega\_{R}(t)=\mathcal{B}(\mathcal{N})-\sum\_{i=1}^{n}\omega\_{i}(t)\geq\mathcal{B}(\mathcal{N})-\sum\_{i=1}^{n}c\_{i}^{(2)}=\omega\_{R}^{(2)}\geq 0.
Therefore, 𝝎​(t)∈ℝ+n+1\bm{\omega}(t)\in\mathbb{R}\_{+}^{n+1}.

The last step is to verify all inequality constraints in the definition of c​o​r​e​(𝒩,ℬ)core(\mathcal{N},\mathcal{B}) (see ([12](https://arxiv.org/html/2602.14223v1#S3.E12 "In 3.2.1 Coalitional stability and the core ‣ 3.2 Cooperative game study on premium decision ‣ 3 Pareto Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"))). For any 𝒞⊊𝒩\mathcal{C}\subsetneq\mathcal{N} such that R∉𝒞R\notin\mathcal{C}, we have ∑i∈𝒞ωi​(t)≥∑i∈𝒞ci(1)≥ℬ​(𝒞)\sum\_{i\in\mathcal{C}}\omega\_{i}(t)\geq\sum\_{i\in\mathcal{C}}c\_{i}^{(1)}\geq\mathcal{B}(\mathcal{C}),
since 𝝎(1)∈c​o​r​e​(𝒩,ℬ)\bm{\omega}^{(1)}\in core(\mathcal{N},\mathcal{B}). Similarly, for any 𝒞⊊𝒩\mathcal{C}\subsetneq\mathcal{N} such that R∈𝒞R\in\mathcal{C}, we have ∑i∈𝒞ωi​(t)=ℬ​(𝒩)−∑i∉𝒞ωi​(t)≥ℬ​(𝒩)−∑i∉𝒞ci(2)=∑i∈𝒞ci(2)≥ℬ​(𝒞),\sum\_{i\in\mathcal{C}}\omega\_{i}(t)=\mathcal{B}(\mathcal{N})-\sum\_{i\notin\mathcal{C}}\omega\_{i}(t)\geq\mathcal{B}(\mathcal{N})-\sum\_{i\notin\mathcal{C}}c\_{i}^{(2)}=\sum\_{i\in\mathcal{C}}c\_{i}^{(2)}\geq\mathcal{B}(\mathcal{C}),
since 𝒄(𝟐)∈c​o​r​e​(𝒩,ℬ)\bm{c^{(2)}}\in core(\mathcal{N},\mathcal{B}).
Therefore, 𝝎​(t)∈c​o​r​e​(𝒩,ℬ)\bm{\omega}(t)\in core(\mathcal{N},\mathcal{B}).

## Appendix I Proof of Proposition [4.5](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem5 "Proposition 4.5. ‣ 4.3 Solution to the reinsurer’s leader problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")

Using 𝒑∗\bm{p}^{\*} in ([18](https://arxiv.org/html/2602.14223v1#S4.E18 "In Proposition 4.4. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), we have

|  |  |  |
| --- | --- | --- |
|  | 𝜼⊤​𝑫​(𝝁)​𝒑∗=𝝁⊤​𝜼−𝜼⊤​𝑫​(𝝁)​𝑴−1​𝑫​(𝝁)​𝜼,(𝒑∗)⊤​𝚺​𝒑∗=(𝟏−𝑴−1​𝑫​(𝝁)​𝜼)⊤​𝚺​(𝟏−𝑴−1​𝑫​(𝝁)​𝜼).\displaystyle\bm{\eta}^{\top}\bm{D}(\bm{\mu})\bm{p}^{\*}=\bm{\mu}^{\top}\bm{\eta}-\bm{\eta}^{\top}\bm{D}(\bm{\mu})\bm{M}^{-1}\bm{D}(\bm{\mu})\bm{\eta},\qquad(\bm{p}^{\*})^{\top}\bm{\Sigma}\bm{p}^{\*}=(\bm{1}-\bm{M}^{-1}\bm{D}(\bm{\mu})\bm{\eta})^{\top}\bm{\Sigma}(\bm{1}-\bm{M}^{-1}\bm{D}(\bm{\mu})\bm{\eta}). |  |

As the terms independent of 𝜼\bm{\eta} play no role in the optimization, Problem ([20](https://arxiv.org/html/2602.14223v1#S4.E20 "In 4.3 Solution to the reinsurer’s leader problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) is equivalent to minimizing

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | γR2​(−2⋅𝟏⊤​𝚺​𝑴−1​𝑫​(𝝁)​𝜼+𝜼⊤​𝑫​(𝝁)​𝑴−1​𝚺​𝑴−1​𝑫​(𝝁)​𝜼)−𝝁⊤​𝜼+𝜼⊤​𝑫​(𝝁)​𝑴−1​𝑫​(𝝁)​𝜼\displaystyle\frac{\gamma\_{R}}{2}(-2\cdot\bm{1}^{\top}\bm{\Sigma}\bm{M}^{-1}\bm{D}(\bm{\mu})\bm{\eta}+\bm{\eta}^{\top}\bm{D}(\bm{\mu})\bm{M}^{-1}\bm{\Sigma}\bm{M}^{-1}\bm{D}(\bm{\mu})\bm{\eta})-\bm{\mu}^{\top}\bm{\eta}+\bm{\eta}^{\top}\bm{D}(\bm{\mu})\bm{M}^{-1}\bm{D}(\bm{\mu})\bm{\eta} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝜼⊤​(𝑫​(𝝁)​𝑴−1​𝑫​(𝝁)+γR2​𝑫​(𝝁)​𝑴−1​𝚺​𝑴−1​𝑫​(𝝁))​𝜼−(𝝁⊤+γR​𝟏⊤​𝚺​𝑴−1​𝑫​(𝝁))​𝜼\displaystyle\ \bm{\eta}^{\top}\left(\bm{D}(\bm{\mu})\bm{M}^{-1}\bm{D}(\bm{\mu})+\frac{\gamma\_{R}}{2}\bm{D}(\bm{\mu})\bm{M}^{-1}\bm{\Sigma}\bm{M}^{-1}\bm{D}(\bm{\mu})\right)\bm{\eta}-(\bm{\mu}^{\top}+\gamma\_{R}\bm{1}^{\top}\bm{\Sigma}\bm{M}^{-1}\bm{D}(\bm{\mu}))\bm{\eta} |  |

Then, the FOC yields

|  |  |  |
| --- | --- | --- |
|  | 𝑫​(𝝁)​(γR​𝑴−1​𝚺+2​𝑰)​𝑴−1​𝑫​(𝝁)​𝜼=γR​𝑫​(𝝁)​𝑴−1​𝚺​𝟏+𝝁⇔(γR​𝚺+2​𝑴)​𝑴−1​𝑫​(𝝁)​𝜼=(γR​𝚺+𝑴)​𝟏.\displaystyle\bm{D}(\bm{\mu})(\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}+2\bm{I})\bm{M}^{-1}\bm{D}(\bm{\mu})\bm{\eta}=\gamma\_{R}\bm{D}(\bm{\mu})\bm{M}^{-1}\bm{\Sigma}\bm{1}+\bm{\mu}\iff{(\gamma\_{R}\bm{\Sigma}+2\bm{M})\bm{M}^{-1}\bm{D}(\bm{\mu})\bm{\eta}=(\gamma\_{R}\bm{\Sigma}+\bm{M})\bm{1}}. |  |

Since 𝚺\bm{\Sigma} and 𝑴\bm{M} are positive definite (see Lemma [4.3](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem3 "Lemma 4.3. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), γR​𝚺+2​𝑴\gamma\_{R}\bm{\Sigma}+2\bm{M} is invertible. The result thus follows.

Finally, we prove the non-negativity of 𝜼∗\bm{\eta}^{\*} under Condition ([22](https://arxiv.org/html/2602.14223v1#S4.E22 "In Proposition 4.5. ‣ 4.3 Solution to the reinsurer’s leader problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")). Consider

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑫​(𝝁)​𝜼∗\displaystyle\bm{D}(\bm{\mu})\bm{\eta}^{\*} | =𝑴​𝟏−𝑴​(γR​𝚺+2​𝑴)−1​𝑴​𝟏\displaystyle=\bm{M}\bm{1}-\bm{M}(\gamma\_{R}\bm{\Sigma}+2\bm{M})^{-1}\bm{M}\bm{1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝑴​𝟏−12​(γR​𝚺+2​𝑴−γR​𝚺)​(γR​𝚺+2​𝑴)−1​𝑴​𝟏\displaystyle=\bm{M}\bm{1}-\frac{1}{2}\left(\gamma\_{R}\bm{\Sigma}+2\bm{M}-\gamma\_{R}\bm{\Sigma}\right)(\gamma\_{R}\bm{\Sigma}+2\bm{M})^{-1}\bm{M}\bm{1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =12​𝑴​𝟏+γR2​𝚺​(γR​𝚺+2​𝑴)−1​𝑴​𝟏\displaystyle=\frac{1}{2}\bm{M}\bm{1}+\frac{\gamma\_{R}}{2}\bm{\Sigma}(\gamma\_{R}\bm{\Sigma}+2\bm{M})^{-1}\bm{M}\bm{1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =12​𝑴​𝟏+γR4​𝚺​(γR​𝚺+2​𝑴)−1​(γR​𝚺+2​𝑴−γR​𝚺)​𝟏\displaystyle=\frac{1}{2}\bm{M}\bm{1}+\frac{\gamma\_{R}}{4}\bm{\Sigma}(\gamma\_{R}\bm{\Sigma}+2\bm{M})^{-1}\left(\gamma\_{R}\bm{\Sigma}+2\bm{M}-\gamma\_{R}\bm{\Sigma}\right)\bm{1} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =12𝑴𝟏+γR4𝚺𝟏−γR24𝚺(γR𝚺+2𝑴)−1𝚺𝟏:=12𝑩𝟏.\displaystyle=\frac{1}{2}\bm{M}\bm{1}+\frac{\gamma\_{R}}{4}\bm{\Sigma}\bm{1}-\frac{\gamma\_{R}^{2}}{4}\bm{\Sigma}(\gamma\_{R}\bm{\Sigma}+2\bm{M})^{-1}\bm{\Sigma}\bm{1}:=\frac{1}{2}\bm{B}\bm{1}. |  | (37) |

Thus, we only need to show 𝑩​𝟏≥𝟎\bm{B}\bm{1}\geq\bm{0}, implied by Bi​i≥∑j≠i|Bi​j|B\_{ii}\geq\sum\_{j\neq i}|B\_{ij}| for all i=1,…,ni=1,\ldots,n, where Bi​jB\_{ij} represents the (i,j)(i,j)-th entry of 𝑩\bm{B}.

Define 𝑩0:=𝑴+γR2​𝚺\bm{B}^{0}:=\bm{M}+\frac{\gamma\_{R}}{2}\bm{\Sigma} and 𝑩1:=𝚺​(γR​𝚺+2​𝑴)−1​𝚺\bm{B}^{1}:=\bm{\Sigma}(\gamma\_{R}\bm{\Sigma}+2\bm{M})^{-1}\bm{\Sigma}, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bi​i−∑j≠i|Bi​j|=\displaystyle B\_{ii}-\sum\_{j\neq i}|B\_{ij}|= | Bi​i0−γR22​Bi​i1−∑j≠i|Bi​j0−γR22​Bi​j1|≥Bi​i0−∑j≠i|Bi​j0|−γR22​(Bi​i1+∑j≠i|Bi​j1|),\displaystyle B\_{ii}^{0}-\frac{\gamma\_{R}^{2}}{2}B\_{ii}^{1}-\sum\_{j\neq i}\left|B\_{ij}^{0}-\frac{\gamma\_{R}^{2}}{2}B\_{ij}^{1}\right|\geq B\_{ii}^{0}-\sum\_{j\neq i}|B\_{ij}^{0}|-\frac{\gamma\_{R}^{2}}{2}\left(B\_{ii}^{1}+\sum\_{j\neq i}|B\_{ij}^{1}|\right), |  |

which is non-negative if

|  |  |  |  |
| --- | --- | --- | --- |
|  | mini∈{1,…,n}⁡(Bi​i0−∑j≠i|Bi​j0|)≥γR22​‖𝑩1‖∞.\min\_{i\in\{1,\ldots,n\}}\left(B\_{ii}^{0}-\sum\_{j\neq i}|B\_{ij}^{0}|\right)\geq\frac{\gamma\_{R}^{2}}{2}\|\bm{B}^{1}\|\_{\infty}. |  | (38) |

We complete the proof by showing that ([22](https://arxiv.org/html/2602.14223v1#S4.E22 "In Proposition 4.5. ‣ 4.3 Solution to the reinsurer’s leader problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) leads to ([38](https://arxiv.org/html/2602.14223v1#A9.E38 "In Appendix I Proof of Proposition 4.5 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")). For the left-hand side of ([38](https://arxiv.org/html/2602.14223v1#A9.E38 "In Appendix I Proof of Proposition 4.5 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), we have

|  |  |  |
| --- | --- | --- |
|  | mini∈{1,…,n}⁡(Bi​i0−∑j≠i|Bi​j0|)=mini∈{1,…,n}⁡(Mi​i+γR2​σi​i−∑j≠i|Mi​j+γR2​σi​j|)≥δ𝑴+γR2​δ𝚺.\min\_{i\in\{1,\ldots,n\}}\left(B\_{ii}^{0}-\sum\_{j\neq i}|B\_{ij}^{0}|\right)=\min\_{i\in\{1,\ldots,n\}}\left(M\_{ii}+\frac{\gamma\_{R}}{2}\sigma\_{ii}-\sum\_{j\neq i}\left|M\_{ij}+\frac{\gamma\_{R}}{2}\sigma\_{ij}\right|\right)\geq\delta\_{\bm{M}}+\frac{\gamma\_{R}}{2}\delta\_{\bm{\Sigma}}. |  |

For the right-hand side of ([38](https://arxiv.org/html/2602.14223v1#A9.E38 "In Appendix I Proof of Proposition 4.5 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), we observe that

|  |  |  |
| --- | --- | --- |
|  | ‖𝑩1‖∞=‖𝚺​(γR​𝚺+2​𝑴)−1​𝚺‖∞≤‖𝚺‖∞2​‖(γR​𝚺+2​𝑴)−1‖∞≤‖𝚺‖∞2κmin≤‖𝚺‖∞22​δ𝑴+γR​δ𝚺,\displaystyle\|\bm{B}^{1}\|\_{\infty}=\|\bm{\Sigma}(\gamma\_{R}\bm{\Sigma}+2\bm{M})^{-1}\bm{\Sigma}\|\_{\infty}\leq\|\bm{\Sigma}\|\_{\infty}^{2}\|(\gamma\_{R}\bm{\Sigma}+2\bm{M})^{-1}\|\_{\infty}\leq\frac{\|\bm{\Sigma}\|\_{\infty}^{2}}{\kappa\_{\min}}\leq\frac{\|\bm{\Sigma}\|\_{\infty}^{2}}{2\delta\_{\bm{M}}+\gamma\_{R}\delta\_{\bm{\Sigma}}}, |  |

where κmin:=mini∈{1,…,n}⁡(γR​σi​i+2​Mi​i−∑j≠i|γR​σi​j+2​Mi​j|)\kappa\_{\min}:=\min\_{i\in\{1,\ldots,n\}}(\gamma\_{R}\sigma\_{ii}+2M\_{ii}-\sum\_{j\neq i}|\gamma\_{R}\sigma\_{ij}+2M\_{ij}|) and the last inequality follows from the triangle inequality. The proof is complete.

## Appendix J Proof of Lemma [4.7](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem7 "Lemma 4.7. ‣ 4.4 Bowley optimum ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")

Using the expression 𝒑∗​(𝜼∗)=𝟏−𝑴−1​𝑫​(𝝁)​𝜼∗\bm{p}^{\*}(\bm{\eta}^{\*})=\bm{1}-\bm{M}^{-1}\bm{D}(\bm{\mu})\bm{\eta}^{\*}, we have ωR∗:=ωR​(𝑨∗​(𝜼∗),𝒑∗​(𝜼∗),𝜼∗)\omega\_{R}^{\*}:=\omega\_{R}(\bm{A}^{\*}(\bm{\eta}^{\*}),\bm{p}^{\*}(\bm{\eta}^{\*}),\bm{\eta}^{\*}) satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | ωR∗\displaystyle\omega\_{R}^{\*} | =(𝜼∗)⊤​𝑫​(𝝁)​𝒑∗−γR2​(𝒑∗)⊤​𝚺​𝒑∗\displaystyle=(\bm{\eta}^{\*})^{\top}\bm{D}(\bm{\mu})\bm{p}^{\*}-\frac{\gamma\_{R}}{2}(\bm{p}^{\*})^{\top}\bm{\Sigma}\bm{p}^{\*} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(𝜼∗)⊤​𝑫​(𝝁)​[𝟏−𝑴−1​𝑫​(𝝁)​𝜼∗]−γR2​[𝟏−𝑴−1​𝑫​(𝝁)​𝜼∗]⊤​𝚺​[𝟏−𝑴−1​𝑫​(𝝁)​𝜼∗]\displaystyle=(\bm{\eta}^{\*})^{\top}\bm{D}(\bm{\mu})\left[\bm{1}-\bm{M}^{-1}\bm{D}(\bm{\mu})\bm{\eta}^{\*}\right]-\frac{\gamma\_{R}}{2}[\bm{1}-\bm{M}^{-1}\bm{D}(\bm{\mu})\bm{\eta}^{\*}]^{\top}\bm{\Sigma}[\bm{1}-\bm{M}^{-1}\bm{D}(\bm{\mu})\bm{\eta}^{\*}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−(𝑫​(𝝁)​𝜼∗)⊤​𝑴−1​𝑫​(𝝁)​𝜼∗−γR2​(𝑫​(𝝁)​𝜼∗)⊤​𝑴−1​𝚺​𝑴−1​𝑫​(𝝁)​𝜼∗\displaystyle=-(\bm{D}(\bm{\mu})\bm{\eta}^{\*})^{\top}\bm{M}^{-1}\bm{D}(\bm{\mu})\bm{\eta}^{\*}-\frac{\gamma\_{R}}{2}(\bm{D}(\bm{\mu})\bm{\eta}^{\*})^{\top}\bm{M}^{-1}\bm{\Sigma}\bm{M}^{-1}\bm{D}(\bm{\mu})\bm{\eta}^{\*} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝟏⊤​𝑫​(𝝁)​𝜼∗+γR​𝟏⊤​𝚺​𝑴−1​𝑫​(𝝁)​𝜼∗−γR2​𝟏⊤​𝚺​𝟏\displaystyle\qquad+\bm{1}^{\top}\bm{D}(\bm{\mu})\bm{\eta}^{\*}+\gamma\_{R}\bm{1}^{\top}\bm{\Sigma}\bm{M}^{-1}\bm{D}(\bm{\mu})\bm{\eta}^{\*}-\frac{\gamma\_{R}}{2}\bm{1}^{\top}\bm{\Sigma}\bm{1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−12​(𝑫​(𝝁)​𝜼∗)⊤​[γR​𝑴−1​𝚺+2​𝑰n]​𝑴−1​𝑫​(𝝁)​𝜼∗+[(γR​𝑴−1​𝚺+𝑰n)​𝟏]⊤​𝑫​(𝝁)​𝜼∗−γR2​𝟏⊤​𝚺​𝟏.\displaystyle=-\frac{1}{2}(\bm{D}(\bm{\mu})\bm{\eta}^{\*})^{\top}\left[\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}+2\bm{I}\_{n}\right]\bm{M}^{-1}\bm{D}(\bm{\mu})\bm{\eta}^{\*}+\left[\left(\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}+\bm{I}\_{n}\right)\bm{1}\right]^{\top}\bm{D}(\bm{\mu})\bm{\eta}^{\*}-\frac{\gamma\_{R}}{2}\bm{1}^{\top}\bm{\Sigma}\bm{1}. |  |

Using ([21](https://arxiv.org/html/2602.14223v1#S4.E21 "In Proposition 4.5. ‣ 4.3 Solution to the reinsurer’s leader problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), we have 𝑫​(𝝁)​𝜼∗=𝑴​(γR​𝑴−1​𝚺+2​𝑰n)−1​(γR​𝑴−1​𝚺+𝑰n)​𝟏\bm{D}(\bm{\mu})\bm{\eta}^{\*}=\bm{M}(\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}+2\bm{I}\_{n})^{-1}(\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}+\bm{I}\_{n})\bm{1}, whence

|  |  |  |  |
| --- | --- | --- | --- |
|  | ωR∗\displaystyle\omega\_{R}^{\*} | =−12​𝟏⊤​(γR​𝑴−1​𝚺+𝑰n)⊤​[(γR​𝑴−1​𝚺+2​𝑰n)−1]⊤​𝑴​(γR​𝑴−1​𝚺+𝑰n)​𝟏\displaystyle=-\frac{1}{2}\bm{1}^{\top}(\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}+\bm{I}\_{n})^{\top}[(\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}+2\bm{I}\_{n})^{-1}]^{\top}\bm{M}(\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}+\bm{I}\_{n})\bm{1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝟏⊤​(γR​𝑴−1​𝚺+𝑰n)⊤​𝑴​(γR​𝑴−1​𝚺+2​𝑰n)−1​(γR​𝑴−1​𝚺+𝑰n)​𝟏−γR2​𝟏⊤​𝚺​𝟏\displaystyle\qquad+\bm{1}^{\top}(\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}+\bm{I}\_{n})^{\top}\bm{M}(\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}+2\bm{I}\_{n})^{-1}(\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}+\bm{I}\_{n})\bm{1}-\frac{\gamma\_{R}}{2}\bm{1}^{\top}\bm{\Sigma}\bm{1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =12​𝟏⊤​[(γR​𝑴−1​𝚺+𝑰n)⊤​𝑴​(γR​𝑴−1​𝚺+2​𝑰n)−1​(γR​𝑴−1​𝚺+𝑰n)−γR​𝚺]​𝟏.\displaystyle=\frac{1}{2}\bm{1}^{\top}\left[(\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}+\bm{I}\_{n})^{\top}\bm{M}(\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}+2\bm{I}\_{n})^{-1}(\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}+\bm{I}\_{n})-\gamma\_{R}\bm{\Sigma}\right]\bm{1}. |  |

Using γR​𝚺=−𝑴+(γR​𝑴−1​𝚺+𝑰n)⊤​𝑴​(γR​𝑴−1​𝚺+𝑰n)−1​(γR​𝑴−1​𝚺+𝑰n),\gamma\_{R}\bm{\Sigma}=-\bm{M}+(\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}+\bm{I}\_{n})^{\top}\bm{M}(\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}+\bm{I}\_{n})^{-1}(\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}+\bm{I}\_{n}),
we have

|  |  |  |
| --- | --- | --- |
|  | (γR​𝑴−1​𝚺+𝑰n)⊤​𝑴​(γR​𝑴−1​𝚺+2​𝑰n)−1​(γR​𝑴−1​𝚺+𝑰n)−γR​𝚺\displaystyle\ \ \ \ (\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}+\bm{I}\_{n})^{\top}\bm{M}(\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}+2\bm{I}\_{n})^{-1}(\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}+\bm{I}\_{n})-\gamma\_{R}\bm{\Sigma} |  |
|  |  |  |
| --- | --- | --- |
|  | =𝑴+(γR​𝑴−1​𝚺+𝑰n)⊤​𝑴​[(γR​𝑴−1​𝚺+2​𝑰n)−1−(γR​𝑴−1​𝚺+𝑰n)−1]​(γR​𝑴−1​𝚺+𝑰n)\displaystyle=\bm{M}+(\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}+\bm{I}\_{n})^{\top}\bm{M}\left[(\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}+2\bm{I}\_{n})^{-1}-(\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}+\bm{I}\_{n})^{-1}\right](\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}+\bm{I}\_{n}) |  |
|  |  |  |
| --- | --- | --- |
|  | =𝑴−(γR​𝑴−1​𝚺+𝑰n)⊤​𝑴​(γR​𝑴−1​𝚺+2​𝑰n)−1\displaystyle=\bm{M}-(\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}+\bm{I}\_{n})^{\top}\bm{M}(\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}+2\bm{I}\_{n})^{-1} |  |
|  |  |  |
| --- | --- | --- |
|  | =[𝑴​(γR​𝑴−1​𝚺+2​𝑰n)−(γR​𝑴−1​𝚺+𝑰n)⊤​𝑴]​(γR​𝑴−1​𝚺+2​𝑰n)−1\displaystyle=\left[\bm{M}(\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}+2\bm{I}\_{n})-(\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}+\bm{I}\_{n})^{\top}\bm{M}\right](\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}+2\bm{I}\_{n})^{-1} |  |
|  |  |  |
| --- | --- | --- |
|  | =(γR​𝑴−1​𝚺​𝑴−1+2​𝑴−1)−1.\displaystyle=\left(\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}\bm{M}^{-1}+2\bm{M}^{-1}\right)^{-1}. |  |

Therefore, ωR∗=12​𝟏⊤​(γR​𝑴−1​𝚺​𝑴−1+2​𝑴−1)−1​𝟏\omega\_{R}^{\*}=\frac{1}{2}\bm{1}^{\top}\left(\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}\bm{M}^{-1}+2\bm{M}^{-1}\right)^{-1}\bm{1}.
Since γR​𝑴−1​𝚺​𝑴−1+2​𝑴−1\gamma\_{R}\bm{M}^{-1}\bm{\Sigma}\bm{M}^{-1}+2\bm{M}^{-1} is positive definite, we conclude that ωR∗=ωR​(𝑨∗​(𝜼∗),𝒑∗​(𝜼∗),𝜼∗)>0\omega\_{R}^{\*}=\omega\_{R}(\bm{A}^{\*}(\bm{\eta}^{\*}),\bm{p}^{\*}(\bm{\eta}^{\*}),\bm{\eta}^{\*})>0.

Next, we verify the members’ IR constraints given ([19](https://arxiv.org/html/2602.14223v1#S4.E19 "In Proposition 4.4. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) and ([24](https://arxiv.org/html/2602.14223v1#S4.E24 "In Lemma 4.7. ‣ 4.4 Bowley optimum ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")). Using ([18](https://arxiv.org/html/2602.14223v1#S4.E18 "In Proposition 4.4. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), the fact that under ([19](https://arxiv.org/html/2602.14223v1#S4.E19 "In Proposition 4.4. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), pi∗∈[0,1]p^{\*}\_{i}\in[0,1], i=1,…,ni=1,\dots,n, and following the derivation of ([G](https://arxiv.org/html/2602.14223v1#A7.Ex64 "Appendix G Proof of Proposition 3.9 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), ωi∗:=ωi​(𝑨∗​(𝜼∗),𝒑∗​(𝜼∗),𝜼∗)\omega\_{i}^{\*}:=\omega\_{i}(\bm{A}^{\*}(\bm{\eta}^{\*}),\bm{p}^{\*}(\bm{\eta}^{\*}),\bm{\eta}^{\*}) satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | ωi∗\displaystyle\omega\_{i}^{\*} | =γi2​(σi2−(γi−1∑j=1nγj−1)2​∑j,l=1n(1−pj∗)​(1−pl∗)​σj​l−k​((αi∗)2−(α¯i∗)2))−ηi∗​pi∗​μi\displaystyle=\frac{\gamma\_{i}}{2}\left(\sigma\_{i}^{2}-\left(\frac{\gamma\_{i}^{-1}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\right)^{2}\sum\_{j,l=1}^{n}(1-p^{\*}\_{j})(1-p^{\*}\_{l})\sigma\_{jl}-k((\alpha^{\*}\_{i})^{2}-(\bar{\alpha}^{\*}\_{i})^{2})\right)-\eta^{\*}\_{i}p^{\*}\_{i}\mu\_{i} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥γi2​(σi2−(γi−1∑j=1nγj−1)2​∑j,l=1n(σj​l)+−k​μi2)−ηi∗​pi∗​μi,\displaystyle\geq\frac{\gamma\_{i}}{2}\left(\sigma\_{i}^{2}-\left(\frac{\gamma\_{i}^{-1}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\right)^{2}\sum\_{j,l=1}^{n}(\sigma\_{jl})\_{+}-k\mu\_{i}^{2}\right)-\eta^{\*}\_{i}p^{\*}\_{i}\mu\_{i}, |  |

where αi∗:=(1−pi∗)​μi\alpha^{\*}\_{i}:=(1-p^{\*}\_{i})\mu\_{i} and α¯i∗=γi−1​∑j=1n(1−pj∗)​μj/∑j=1nγj−1\bar{\alpha}^{\*}\_{i}=\gamma\_{i}^{-1}\sum\_{j=1}^{n}(1-p^{\*}\_{j})\mu\_{j}/\sum\_{j=1}^{n}\gamma\_{j}^{-1}.
Using the upper bound of μi​ηi∗\mu\_{i}\eta^{\*}\_{i} in ([19](https://arxiv.org/html/2602.14223v1#S4.E19 "In Proposition 4.4. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), pi∗∈[0,1]p^{\*}\_{i}\in[0,1], and ([24](https://arxiv.org/html/2602.14223v1#S4.E24 "In Lemma 4.7. ‣ 4.4 Bowley optimum ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), we further have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ωi∗\displaystyle\omega\_{i}^{\*} | ≥γi2​(σi2−(γi−1∑j=1nγj−1)2​∑j,l=1n(σj​l)+−k​μi2)−k​μi2​γi+∑m≠i(k​μi​μm−σi​m)++k​μi2−σi2∑j=1nγj−1≥0.\displaystyle\geq\frac{\gamma\_{i}}{2}\left(\sigma\_{i}^{2}-\left(\frac{\gamma\_{i}^{-1}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\right)^{2}\sum\_{j,l=1}^{n}(\sigma\_{jl})\_{+}-k\mu\_{i}^{2}\right)-k\mu\_{i}^{2}\gamma\_{i}+\frac{\sum\_{m\neq i}(k\mu\_{i}\mu\_{m}-\sigma\_{im})\_{+}+k\mu\_{i}^{2}-\sigma\_{i}^{2}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\geq 0. |  |

Therefore, the members’ IR constraints are fulfilled, and the proof is complete.

## Appendix K Proof of Corollary [4.9](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem9 "Corollary 4.9. ‣ 4.4 Bowley optimum ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")

When 𝜼=η​𝟏\bm{\eta}=\eta\bm{1}, the optimal reinsurance strategy in Proposition [4.4](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem4 "Proposition 4.4. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") becomes
𝒑=𝟏−η​𝑴−1​𝝁.\bm{p}=\bm{1}-\eta\bm{M}^{-1}\bm{\mu}.
We shall repeat the proof of Proposition [4.5](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem5 "Proposition 4.5. ‣ 4.3 Solution to the reinsurer’s leader problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance") with this new setting.

By direct substitutions, we have 𝒑⊤​𝚺​𝒑=𝟏⊤​𝚺​𝟏−2​η​𝟏⊤​𝚺​𝑴−1​𝝁+η2​𝝁⊤​𝑴−1​𝚺​𝑴−1​𝝁\bm{p}^{\top}\bm{\Sigma}\bm{p}=\bm{1}^{\top}\bm{\Sigma}\bm{1}-2\eta\bm{1}^{\top}\bm{\Sigma}\bm{M}^{-1}\bm{\mu}+\eta^{2}\bm{\mu}^{\top}\bm{M}^{-1}\bm{\Sigma}\bm{M}^{-1}\bm{\mu} and η​𝝁⊤​𝒑=η​𝝁⊤​𝟏−η2​𝝁⊤​𝑴−1​𝝁\eta\bm{\mu}^{\top}\bm{p}=\eta\bm{\mu}^{\top}\bm{1}-\eta^{2}\bm{\mu}^{\top}\bm{M}^{-1}\bm{\mu}.
Removing terms that are independent of η\eta, we see that Problem ([20](https://arxiv.org/html/2602.14223v1#S4.E20 "In 4.3 Solution to the reinsurer’s leader problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) is equivalent to minimizing

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | γR2​(−2​η​𝟏⊤​𝚺​𝑴−1​𝝁+η2​𝝁⊤​𝑴−1​𝚺​𝑴−1​𝝁)−η​𝝁⊤​𝟏+η2​𝝁⊤​𝑴−1​𝝁\displaystyle\frac{\gamma\_{R}}{2}(-2\eta\bm{1}^{\top}\bm{\Sigma}\bm{M}^{-1}\bm{\mu}+\eta^{2}\bm{\mu}^{\top}\bm{M}^{-1}\bm{\Sigma}\bm{M}^{-1}\bm{\mu})-\eta\bm{\mu}^{\top}\bm{1}+\eta^{2}\bm{\mu}^{\top}\bm{M}^{-1}\bm{\mu} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | (𝝁⊤​𝑴−1​𝝁+γR2​𝝁⊤​𝑴−1​𝚺​𝑴−1​𝝁)​η2−(𝝁⊤​𝟏+γR​𝟏⊤​𝚺​𝑴−1​𝝁)​η\displaystyle\left(\bm{\mu}^{\top}\bm{M}^{-1}\bm{\mu}+\frac{\gamma\_{R}}{2}\bm{\mu}^{\top}\bm{M}^{-1}\bm{\Sigma}\bm{M}^{-1}\bm{\mu}\right)\eta^{2}-(\bm{\mu}^{\top}\bm{1}+\gamma\_{R}\bm{1}^{\top}\bm{\Sigma}\bm{M}^{-1}\bm{\mu})\eta |  |

The FOC then yields the solution ([21](https://arxiv.org/html/2602.14223v1#S4.E21 "In Proposition 4.5. ‣ 4.3 Solution to the reinsurer’s leader problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) by noting the positive definiteness of 𝑴\bm{M} and 𝚺\bm{\Sigma}. The second statement follows from Theorem [4.8](https://arxiv.org/html/2602.14223v1#S4.Thmtheorem8 "Theorem 4.8. ‣ 4.4 Bowley optimum ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance").

For the last statement, note that the non-negativity of η∗\eta^{\*} follows from the diagonal dominance of 𝑰n+γR​𝑴−1​𝚺\bm{I}\_{n}+\gamma\_{R}\bm{M}^{-1}\bm{\Sigma} and its diagonal elements are positive. To prove the latter, we need γR​‖𝑴−1​𝚺‖∞≤1\gamma\_{R}\|\bm{M}^{-1}\bm{\Sigma}\|\_{\infty}\leq 1. As 𝑴\bm{M} is strictly diagonally dominant, using the Varah bound, we have ‖𝑴−1‖∞≤1/δ𝑴\|\bm{M}^{-1}\|\_{\infty}\leq 1/\delta\_{\bm{M}}. Together with γR≤δ𝑴/‖𝚺‖∞\gamma\_{R}\leq\delta\_{\bm{M}}/\|\bm{\Sigma}\|\_{\infty}, the result follows.

## Appendix L A Discussion on Condition ([19](https://arxiv.org/html/2602.14223v1#S4.E19 "In Proposition 4.4. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance"))

This note provides a discussion on obtaining bounds on the optimal safety loading 𝜼∗\bm{\eta}^{\*}, and consequently, a way to verify the condition ([19](https://arxiv.org/html/2602.14223v1#S4.E19 "In Proposition 4.4. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) under the Bowley optimum by deriving an explicit representation that depends on the underlying model parameters.

We first consider the benchmark case γR=0\gamma\_{R}=0 where 𝜼∗\bm{\eta}^{\*} admits a closed-form, entry-wise expression, allowing ([19](https://arxiv.org/html/2602.14223v1#S4.E19 "In Proposition 4.4. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) to be written explicitly in terms of the model parameters. When γR>0\gamma\_{R}>0, 𝜼∗\bm{\eta}^{\*} contains additional terms involving matrix inverses, and its entries are no longer available in closed form. We therefore discuss ways to bound these terms and substitute the resulting bounds back into ([19](https://arxiv.org/html/2602.14223v1#S4.E19 "In Proposition 4.4. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) to obtain tractable sufficient conditions. To this end, we utilize the formula derived in ([I](https://arxiv.org/html/2602.14223v1#A9.Ex77 "Appendix I Proof of Proposition 4.5 ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝑫​(𝝁)​𝜼∗=12​𝑴​𝟏+γR4​𝚺​𝟏−γR24​𝚺​(γR​𝚺+2​𝑴)−1​𝚺​𝟏.\bm{D}(\bm{\mu})\bm{\eta}^{\*}=\frac{1}{2}\bm{M}\bm{1}+\frac{\gamma\_{R}}{4}\bm{\Sigma}\bm{1}-\frac{\gamma\_{R}^{2}}{4}\bm{\Sigma}(\gamma\_{R}\bm{\Sigma}+2\bm{M})^{-1}\bm{\Sigma}\bm{1}. |  | (39) |

When the reinsurer is risk-neutral, i.e., γR=0\gamma\_{R}=0, we have 𝑫​(𝝁)​𝜼∗=12​𝑴​𝟏\bm{D}(\bm{\mu})\bm{\eta}^{\*}=\frac{1}{2}\bm{M}\bm{1}. Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | μi​ηi∗=12​[∑j=1n(σi​j−k​μi​μj)∑j=1nγj−1+k​μi2​γi].\mu\_{i}\eta^{\*}\_{i}=\frac{1}{2}\left[\frac{\sum\_{j=1}^{n}(\sigma\_{ij}-k\mu\_{i}\mu\_{j})}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}+k\mu\_{i}^{2}\gamma\_{i}\right]. |  | (40) |

Substituting this into ([19](https://arxiv.org/html/2602.14223v1#S4.E19 "In Proposition 4.4. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), the condition is equivalent to, for any i=1,…,ni=1,\dots,n,

|  |  |  |
| --- | --- | --- |
|  | k​μi2​γi+σi2−k​μi2∑j=1nγj−1>∑j≠i|σi​j−k​μi​μj|∑j=1nγj−1​and​k​μi2​γi+σi2−k​μi2∑j=1nγj−1>∑j≠i(σi​j−k​μi​μj)+∑j≠iγj−1.k\mu\_{i}^{2}\gamma\_{i}+\frac{\sigma\_{i}^{2}-k\mu\_{i}^{2}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}>\frac{\sum\_{j\neq i}|\sigma\_{ij}-k\mu\_{i}\mu\_{j}|}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\quad\text{and}\quad k\mu\_{i}^{2}\gamma\_{i}+\frac{\sigma\_{i}^{2}-k\mu\_{i}^{2}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}>\frac{\sum\_{j\neq i}(\sigma\_{ij}-k\mu\_{i}\mu\_{j})\_{+}}{\sum\_{j\neq i}\gamma\_{j}^{-1}}. |  |

Combining the two inequalities, we see that ([19](https://arxiv.org/html/2602.14223v1#S4.E19 "In Proposition 4.4. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) is equivalent to ([23](https://arxiv.org/html/2602.14223v1#S4.E23 "In Remark 4.6. ‣ 4.3 Solution to the reinsurer’s leader problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")).

When γR>0\gamma\_{R}>0,
one has to handle the term (γR​𝚺+2​𝑴)−1(\gamma\_{R}\bm{\Sigma}+2\bm{M})^{-1}. In that case, using ([39](https://arxiv.org/html/2602.14223v1#A12.E39 "In Appendix L A Discussion on Condition (19) ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | μi​ηi∗\displaystyle\mu\_{i}\eta^{\*}\_{i} | =12​[∑j=1n(σi​j−k​μi​μj)∑j=1nγj−1+k​μi2​γi]+γR4​∑j=1nσi​j−γR24​[𝚺​(γR​𝚺+2​𝑴)−1​𝚺​𝟏]i,\displaystyle=\frac{1}{2}\left[\frac{\sum\_{j=1}^{n}(\sigma\_{ij}-k\mu\_{i}\mu\_{j})}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}+k\mu\_{i}^{2}\gamma\_{i}\right]+\frac{\gamma\_{R}}{4}\sum\_{j=1}^{n}\sigma\_{ij}-\frac{\gamma\_{R}^{2}}{4}\left[\bm{\Sigma}(\gamma\_{R}\bm{\Sigma}+2\bm{M})^{-1}\bm{\Sigma}\bm{1}\right]\_{i}, |  | (41) |

where [𝒙]i[\bm{x}]\_{i} denotes the ii-th entry of 𝒙\bm{x}. The formula shows that the non-explicit term appears only at second order in γR\gamma\_{R}. Substituting this into ([19](https://arxiv.org/html/2602.14223v1#S4.E19 "In Proposition 4.4. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), we see that the condition is equivalent to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | k​μi2​γi+σi2−k​μi2∑j=1nγj−1\displaystyle k\mu\_{i}^{2}\gamma\_{i}+\frac{\sigma\_{i}^{2}-k\mu\_{i}^{2}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}} | >max{∑j≠i|σi​j−k​μi​μj|∑j=1nγj−1−γR2∑j=1nσi​j+γR22[𝚺(γR𝚺+2𝑴)−1𝚺𝟏]i,\displaystyle>\max\bigg\{\frac{\sum\_{j\neq i}|\sigma\_{ij}-k\mu\_{i}\mu\_{j}|}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}-\frac{\gamma\_{R}}{2}\sum\_{j=1}^{n}\sigma\_{ij}+\frac{\gamma\_{R}^{2}}{2}\left[\bm{\Sigma}(\gamma\_{R}\bm{\Sigma}+2\bm{M})^{-1}\bm{\Sigma}\bm{1}\right]\_{i}, |  | (42) |
|  |  | ∑j=1n(σi​j−k​μi​μj)∑j=1nγj−1+γR2∑j=1nσi​j−γR22[𝚺(γR𝚺+2𝑴)−1𝚺𝟏]i}.\displaystyle\hskip 18.49988pt\frac{\sum\_{j=1}^{n}(\sigma\_{ij}-k\mu\_{i}\mu\_{j})}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}+\frac{\gamma\_{R}}{2}\sum\_{j=1}^{n}\sigma\_{ij}-\frac{\gamma\_{R}^{2}}{2}\left[\bm{\Sigma}(\gamma\_{R}\bm{\Sigma}+2\bm{M})^{-1}\bm{\Sigma}\bm{1}\right]\_{i}\bigg\}. |  |

Herein, we provide two possible entry-wise bounds. For the first bound, we impose the following condition: for i=1,…,ni=1,\dots,n,

|  |  |  |  |
| --- | --- | --- | --- |
|  | κi:=(γR+2∑j=1nγj−1)​(σi2−∑j≠i|σi​j|)+2​k​μi2​(γi−1∑j=1nγj−1)+2​k​μi∑j=1nγj−1​∑j≠iμj>0,\kappa\_{i}:=\left(\gamma\_{R}+\frac{2}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\right)\left(\sigma\_{i}^{2}-\sum\_{j\neq i}|\sigma\_{ij}|\right)+2k\mu\_{i}^{2}\left(\gamma\_{i}-\frac{1}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\right)+\frac{2k\mu\_{i}}{\sum\_{j=1}^{n}\gamma\_{j}^{-1}}\sum\_{j\neq i}\mu\_{j}>0, |  | (43) |

i.e., the matrix γR​𝚺+2​𝑴\gamma\_{R}\bm{\Sigma}+2\bm{M} is strictly diagonally dominant. Let also κmin:=mini=1,…,n⁡κi\kappa\_{\min}:=\min\_{i=1,\dots,n}\kappa\_{i}. By the Varah bound for strictly diagonally dominant matrices, ‖(γR​𝚺+2​𝑴)−1‖∞≤1κmin\|(\gamma\_{R}\bm{\Sigma}+2\bm{M})^{-1}\|\_{\infty}\leq\frac{1}{\kappa\_{\min}}.
Therefore,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | |γR2​[𝚺​(γR​𝚺+2​𝑴)−1​𝚺​𝟏]i|≤γR2​‖𝚺‖∞κmin​maxj=1,…,n⁡|∑k=1nσj​k|.\displaystyle\ \ \ \ \left|\gamma\_{R}^{2}\left[\bm{\Sigma}(\gamma\_{R}\bm{\Sigma}+2\bm{M})^{-1}\bm{\Sigma}\bm{1}\right]\_{i}\right|\leq\frac{\gamma\_{R}^{2}\|\bm{\Sigma}\|\_{\infty}}{\kappa\_{\min}}\max\_{j=1,\dots,n}\left|\sum\_{k=1}^{n}\sigma\_{jk}\right|. |  | (44) |

We can thus substitute ([44](https://arxiv.org/html/2602.14223v1#A12.E44 "In Appendix L A Discussion on Condition (19) ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) into ([42](https://arxiv.org/html/2602.14223v1#A12.E42 "In Appendix L A Discussion on Condition (19) ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) to obtain an expression for the condition ([19](https://arxiv.org/html/2602.14223v1#S4.E19 "In Proposition 4.4. ‣ 4.2 Solution to the plan manager’s follower problem ‣ 4 Bowley Design ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")).

In the second bound, by considering 𝚺​(γR​𝚺+2​𝑴)−1=𝚺12​(γR​𝑰n+2​𝚺−12​𝑴​𝚺−12)−1​𝚺−12\bm{\Sigma}(\gamma\_{R}\bm{\Sigma}+2\bm{M})^{-1}=\bm{\Sigma}^{\frac{1}{2}}(\gamma\_{R}\bm{I}\_{n}+2\bm{\Sigma}^{-\frac{1}{2}}\bm{M}\bm{\Sigma}^{-\frac{1}{2}})^{-1}\bm{\Sigma}^{-\frac{1}{2}},
we have

|  |  |  |
| --- | --- | --- |
|  | ‖𝚺​(γR​𝚺+2​𝑴)−1‖2≤1γR+2λmin(𝚺−12𝑴𝚺−12)−1𝚺−12).\|\bm{\Sigma}(\gamma\_{R}\bm{\Sigma}+2\bm{M})^{-1}\|\_{2}\leq\frac{1}{\gamma\_{R}+2\lambda\_{\min}(\bm{\Sigma}^{-\frac{1}{2}}\bm{M}\bm{\Sigma}^{-\frac{1}{2}})^{-1}\bm{\Sigma}^{-\frac{1}{2}})}. |  |

Hence,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | |γR2​[𝚺​(γR​𝚺+2​𝑴)−1​𝚺​𝟏]i|≤γR2γR+2λmin(𝚺−12𝑴𝚺−12)−1𝚺−12)​‖𝚺​𝟏‖2.\displaystyle\ \ \ \ \left|\gamma\_{R}^{2}\left[\bm{\Sigma}(\gamma\_{R}\bm{\Sigma}+2\bm{M})^{-1}\bm{\Sigma}\bm{1}\right]\_{i}\right|\leq\frac{\gamma\_{R}^{2}}{\gamma\_{R}+2\lambda\_{\min}(\bm{\Sigma}^{-\frac{1}{2}}\bm{M}\bm{\Sigma}^{-\frac{1}{2}})^{-1}\bm{\Sigma}^{-\frac{1}{2}})}\left\|\bm{\Sigma}\bm{1}\right\|\_{2}. |  | (45) |

Compared with ([44](https://arxiv.org/html/2602.14223v1#A12.E44 "In Appendix L A Discussion on Condition (19) ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")), the bound ([45](https://arxiv.org/html/2602.14223v1#A12.E45 "In Appendix L A Discussion on Condition (19) ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")) does not require additional conditions as introduced in ([43](https://arxiv.org/html/2602.14223v1#A12.E43 "In Appendix L A Discussion on Condition (19) ‣ Pareto and Bowley Reinsurance Games in Peer-to-Peer Insurance")). However, it could suffer from the curse of dimensionality as the l2l\_{2}-norm of 𝚺​𝟏\bm{\Sigma}\bm{1} would, in general, introduce a factor of n\sqrt{n}.