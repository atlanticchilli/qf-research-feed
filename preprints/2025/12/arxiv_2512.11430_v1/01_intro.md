---
authors:
- Tim J. Boonen
- Xia Han
- Peng Liu
- Jiacong Wang
doc_id: arxiv:2512.11430v1
family_id: arxiv:2512.11430
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Pareto-optimal reinsurance under dependence uncertainty
url_abs: http://arxiv.org/abs/2512.11430v1
url_html: https://arxiv.org/html/2512.11430v1
venue: arXiv q-fin
version: 1
year: 2025
---


Tim J. Boonen
Department of Statistics and Actuarial Science, School of Computing and Data Science, The University of Hong Kong, Hong Kong, China. Email: tjboonen@hku.hk
  
Xia Han
School of Mathematical Sciences, LPMC and AAIS, Nankai University, China. Email: xiahan@nankai.edu.cn
  
Peng Liu
School of Mathematics, Statistics and Actuarial Science, University of Essex, UK. Email: peng.liu@essex.ac.uk
  
Jiacong Wang
School of Mathematical Sciences, Nankai University, China. Email: 2120240092@mail.nankai.edu.cn

###### Abstract

This paper studies Pareto-optimal reinsurance design in a monopolistic market with multiple primary insurers and a single reinsurer, all with heterogeneous risk preferences. The risk preferences are characterized by a family of risk measures, called Range Value-at-Risk (RVaR), which includes both Value-at-Risk (VaR) and Expected Shortfall (ES) as special cases. Recognizing the practical difficulty of accurately estimating the dependence structure among the insurers’ losses, we adopt a robust optimization approach that assumes the marginal distributions are known while leaving the dependence structure unspecified. We provide a complete characterization of optimal indemnity schedules under the worst-case scenario, showing that the infinite-dimensional optimization problem can be reduced to a tractable finite-dimensional problem involving only two or three parameters for each indemnity function. Additionally, for independent and identically distributed risks, we exploit the argument of asymptotic normality to derive optimal two-parameter layer contracts. Finally, numerical applications are considered in a two-insurer setting to illustrate the influence of the dependence structures and heterogeneous risk tolerances on optimal strategies and the corresponding risk evaluation.

Keywords: Optimal reinsurance, robust risk management, Range Value-at-Risk, dependence uncertainty, Pareto efficiency

## 1 Introduction

Centralized risk pooling, where a single entity assumes the financial risks of a large and heterogeneous client base, underpins modern insurance markets. This principle naturally extends to reinsurance, in which specialized entities absorb and manage risks ceded by primary insurers, enhancing market capacity and stability.

In this paper, we study risk-transfer mechanisms in a monopolistic reinsurance market with multiple primary insurers (cedants) and a single reinsurer. Each cedant holds a fixed portfolio of risks and seeks to transfer part of these risks through structured premium payments. A reinsurance treaty specifies a coordinated schedule of premiums and corresponding indemnity rules. A tension arises between the participants’ perspectives: cedants evaluate the treaty based on their individual post-transfer risk, whereas the reinsurer considers aggregate liabilities versus total premiums.

We evaluate the efficiency of multilateral reinsurance treaties through the lens of Pareto optimality: a treaty is considered efficient if no participant’s risk can be reduced without increasing that of another. The seminal work of Arrow ([1971](https://arxiv.org/html/2512.11430v1#bib.bib2)) established that for a risk-averse decision maker maximizing expected utility, Pareto-optimal contracts take the form of full coverage above a constant deductible. This foundational result has been substantially generalized to alternative market settings, including those employing distortion-type premium principles and accommodating heterogeneous beliefs; see, e.g., Cai et al. ([2017](https://arxiv.org/html/2512.11430v1#bib.bib11)), Jiang et al. ([2018](https://arxiv.org/html/2512.11430v1#bib.bib30)), Ghossoub ([2019](https://arxiv.org/html/2512.11430v1#bib.bib29)), Boonen and Jiang ([2023](https://arxiv.org/html/2512.11430v1#bib.bib9)), and Coke et al. ([2024](https://arxiv.org/html/2512.11430v1#bib.bib18)). Boonen et al. ([2024](https://arxiv.org/html/2512.11430v1#bib.bib10)) study the case with multiple policyholders transferring risk to a single central authority, achieving Pareto efficiency with distortion risk measures. They provide only an implicit description of the optimal risk-transfer contracts and show the relevance of the setting in examples involving flood risk.

In our framework, where multiple cedants cede risk to a single reinsurer, presents a distinct challenge, as treaty performance depends not only on the marginal distributions of the cedants’ risks but also critically on the dependence structure governing their joint behavior, which directly determines the reinsurer’s aggregate loss. McNeil et al. ([2015](https://arxiv.org/html/2512.11430v1#bib.bib33)) emphasize that accurately estimating this dependence structure is notoriously difficult in practice, and its misspecification can lead to severe risk management consequences. Moreover, data for different but correlated insurance lines are often collected separately, providing little or no empirical basis for inferring dependence; see, e.g., Embrechts et al. ([2013](https://arxiv.org/html/2512.11430v1#bib.bib23)) and Embrechts et al. ([2015](https://arxiv.org/html/2512.11430v1#bib.bib24)).
Motivated by these operational challenges, we adopt a robust optimization framework in which the marginal loss distributions are assumed to be known, whereas the dependence structure among the risks is left completely unspecified.
Robust optimization provides a principled approach to decision-making under model uncertainty, with its theoretical foundations developed in Ben-Tal et al. ([2009](https://arxiv.org/html/2512.11430v1#bib.bib3)), key methodological advances presented in Ben-Tal and Nemirovski ([2008](https://arxiv.org/html/2512.11430v1#bib.bib4)) and Bertsimas et al. ([2011](https://arxiv.org/html/2512.11430v1#bib.bib6)), and an overview provided in Gabrel et al. ([2014](https://arxiv.org/html/2512.11430v1#bib.bib27)). Applications of robust methods to insurance and risk management include the analysis of minimax portfolio strategies in Polak et al. ([2010](https://arxiv.org/html/2512.11430v1#bib.bib34)) and the study of robust and Pareto-efficient insurance contracts in Asimit et al. ([2017](https://arxiv.org/html/2512.11430v1#bib.bib1)). More recent developments addressing model uncertainty in (re)insurance design have appeared in Chi et al. ([2022](https://arxiv.org/html/2512.11430v1#bib.bib17)) and Cai et al. ([2024](https://arxiv.org/html/2512.11430v1#bib.bib12)). Although Fadina et al. ([2025](https://arxiv.org/html/2512.11430v1#bib.bib25)) also study reinsurance problems under dependence ambiguity, their framework does not incorporate the Pareto-optimal multilateral treaty structure that is central to our analysis.

A defining feature of our model is its ability to coherently accommodate heterogeneous risk preferences among all market participants. We assume that both cedants and the reinsurer evaluate risk using the Range Value-at-Risk (RVaR) measure, while allowing each entity to adopt a distinct RVaR threshold, thereby reflecting differing levels of risk tolerance. The RVaR family, introduced by Cont et al. ([2010](https://arxiv.org/html/2512.11430v1#bib.bib19)) as a class of robust risk measures, generalizes two of the most widely adopted risk measures in insurance practice and regulation: Value-at-Risk (VaR) and Expected Shortfall (ES). The extensive use of VaR and ES for risk quantification and capital requirements (see, e.g., Cai et al., [2008](https://arxiv.org/html/2512.11430v1#bib.bib13); Lu et al., [2013](https://arxiv.org/html/2512.11430v1#bib.bib31); Chi and Meng, [2014](https://arxiv.org/html/2512.11430v1#bib.bib15)) has motivated a substantial body of research on optimal reinsurance design based on these measures. More recently, RVaR has been employed as a preference functional in a range of risk-sharing and reinsurance settings, including cooperative and competitive risk allocation (Embrechts et al., [2018](https://arxiv.org/html/2512.11430v1#bib.bib22)) and optimal reinsurance design (Gavagan et al., [2022](https://arxiv.org/html/2512.11430v1#bib.bib28); Fadina et al., [2025](https://arxiv.org/html/2512.11430v1#bib.bib25)). Our paper is organized as follows.

Section [2](https://arxiv.org/html/2512.11430v1#S2 "2 Model description and notation ‣ Pareto-optimal reinsurance under dependence uncertainty") formulates the problem and presents the methodological foundations of our analysis. We show that identifying a Pareto-optimal reinsurance contract is equivalent to solving a system-wide risk minimization problem, where the total risk is represented as a weighted sum of the cedants’ and the reinsurer’s risk exposures (Proposition [1](https://arxiv.org/html/2512.11430v1#Thmproposition1 "Proposition 1. ‣ 2 Model description and notation ‣ Pareto-optimal reinsurance under dependence uncertainty")).

In Section [3](https://arxiv.org/html/2512.11430v1#S3 "3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty"), we investigate the worst-case scenario. We assume that the marginal loss distributions of the cedants are known, while the dependence structure among these risks remains completely unspecified. Because robust aggregation results for VaR\mathrm{VaR} and RVaR\mathrm{RVaR} are limited, we restrict the search to convex or concave indemnity schedules and work on the corresponding reduced domains. The theoretical developments rely on the techniques of Blanchet et al. ([2025](https://arxiv.org/html/2512.11430v1#bib.bib8)) and their extension to the insurer’s problem in Fadina et al. ([2025](https://arxiv.org/html/2512.11430v1#bib.bib25)). Under dependence uncertainty, the problem naturally becomes a minimax optimization in which the objective is to identify indemnity rules that minimize the system’s total risk under the worst possible dependence configuration. Our main analytical contribution in this section is a complete characterization of the Pareto-optimal indemnity schedules. We show that the infinite-dimensional optimization over measurable indemnity functions can be reduced to a finite-dimensional search. Specifically, for each cedant, the optimal indemnity function is either a two- or three-parameter layer contract (Theorem [1](https://arxiv.org/html/2512.11430v1#Thmtheorem1 "Theorem 1. ‣ 3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty")). These tractable parametric representations not only simplify computation but also provide a clear economic interpretation, illustrating how optimal contracts allocate risk between cedants and the reinsurer under heterogeneous preferences and dependence uncertainty. In the special case where the risk measure is reduced to VaR, we derive explicit forms of the optimal reinsurance contracts (Theorem [2](https://arxiv.org/html/2512.11430v1#Thmtheorem2 "Theorem 2. ‣ 4 Optimal solution to the special case of VaR ‣ Pareto-optimal reinsurance under dependence uncertainty")). For the case of two risks, the optimal contracts admit a particularly simple representation based on Makarov-type bounds, allowing explicit evaluation of the worst-case VaR.

Section [5](https://arxiv.org/html/2512.11430v1#S5 "5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty") focuses on the case of independent and identically distributed (i.i.d.) risks, which allows us to leverage the asymptotic normality established in Proposition [5](https://arxiv.org/html/2512.11430v1#Thmproposition5 "Proposition 5. ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty") to obtain approximately optimal reinsurance strategies. In this setting, the optimal indemnity function admits a simple two-parameter layer form (Theorem [3](https://arxiv.org/html/2512.11430v1#Thmtheorem3 "Theorem 3. ‣ 5.1 The results for RVaR ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty")), making the solution more tractable while retaining economic interpretability. In the special case of a single insurer, this formulation coincides with the classical problem of designing an optimal reinsurance contract under a mean-standard deviation framework with RVaR\mathrm{RVaR} as the risk criterion, and naturally recovers the VaR\mathrm{VaR}- and ES\mathrm{ES}-based results of Chi ([2012](https://arxiv.org/html/2512.11430v1#bib.bib14)). We also provide the corresponding asymptotic normality results under VaR\mathrm{VaR} (Theorem [4](https://arxiv.org/html/2512.11430v1#Thmtheorem4 "Theorem 4. ‣ 5.2 The result for VaR ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty")).

In Section [6](https://arxiv.org/html/2512.11430v1#S6 "6 Simulation studies ‣ Pareto-optimal reinsurance under dependence uncertainty"), we provide numerical illustrations of our theoretical findings. In a two-insurer setting, we derive general VaR\mathrm{VaR}-based optimal solutions and compute specific reinsurance contracts for simulated data under three dependence regimes: independence, comonotonicity, and full dependence uncertainty. As expected, worst-case dependence generally produces the largest system risk, although VaR\mathrm{VaR} does not always attain its maximum in the comonotonic case; in some situations, the i.i.d. scenario may yield even larger values than the comonotonic benchmark. Finally, we present comparative examples illustrating how constraints on reinsurance strategies interact with different loss distributions, highlighting the impact of distributional features on the structure of the optimal indemnity schedules. Section [7](https://arxiv.org/html/2512.11430v1#S7 "7 Conclusion ‣ Pareto-optimal reinsurance under dependence uncertainty") concludes the paper. The proofs are delegated to the appendices.

## 2 Model description and notation

For an atomless probability space (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}), let
L1L^{1} be the set of random variables with finite expectation, and L0L^{0} be the set of all measurable random variables. For simplicity, let [n]={1,…,n}[n]=\{1,\dots,n\}. Random variables XX and YY are called comonotonic if there exist non-decreasing functions hh and gg such that X=h​(X+Y)X=h(X+Y) and Y=g​(X+Y)Y=g(X+Y) (Denneberg, [1994](https://arxiv.org/html/2512.11430v1#bib.bib20)).

In a monopolistic reinsurance market with multiple primary insurers and a single reinsurer, we assume that each insurer seeks to purchase an optimal reinsurance contract from the reinsurer. Let fif\_{i} denote the indemnity function that maps losses to indemnities.
To mitigate potential ex post moral hazard, we focus on the class of indemnity functions

|  |  |  |
| --- | --- | --- |
|  | ℐ={f:[0,∞)→[0,∞)|f(0)=0, 0⩽f(x2)−f(x1)⩽x2−x1for all 0⩽x1⩽x2}.\mathcal{I}=\left\{f:[0,\infty)\to[0,\infty)\;\middle|\;f(0)=0,\;0\leqslant f(x\_{2})-f(x\_{1})\leqslant x\_{2}-x\_{1}\ \text{for all }0\leqslant x\_{1}\leqslant x\_{2}\right\}. |  |

This class ℐ\mathcal{I} is sufficiently rich: it includes many commonly used indemnity functions, such as the excess-of-loss function f​(x)=(x−d)+f(x)=(x-d)\_{+} for some d⩾0d\geqslant 0, where z+:=max⁡{z,0}z\_{+}:=\max\{z,0\}, and the quota-share function f​(x)=q​xf(x)=qx for q∈[0,1]q\in[0,1].

Given the reinsurance contract fif\_{i} and the premium πi∈ℝ,\pi\_{i}\in\mathbb{R}, the loss random variable for the ii-th insurer is

|  |  |  |
| --- | --- | --- |
|  | Tfi,πi​(Xi)=Xi−fi​(Xi)+πi,T\_{f\_{i},\pi\_{i}}(X\_{i})=X\_{i}-f\_{i}(X\_{i})+\pi\_{i}, |  |

and the loss random variable for the (centralized) reinsurer is

|  |  |  |
| --- | --- | --- |
|  | R𝐟,𝝅​(𝐗)=∑i=1nfi​(Xi)−∑i=1nπi,R\_{\mathbf{f},\boldsymbol{\pi}}(\mathbf{X})=\sum\_{i=1}^{n}f\_{i}(X\_{i})-\sum\_{i=1}^{n}\pi\_{i}, |  |

with 𝐟=(f1,…,fn),\mathbf{f}=(f\_{1},\dots,f\_{n}), 𝝅=(π1,…,πn)\boldsymbol{\pi}=(\pi\_{1},\dots,\pi\_{n}) and 𝐗=(X1,…,Xn).\mathbf{X}=(X\_{1},\dots,X\_{n}). In this paper, we assume that the marginal distributions of the risks are fixed, but their dependence structure is left unspecified. The corresponding uncertainty set is defined as

|  |  |  |
| --- | --- | --- |
|  | ℰn​(𝐅)={(X1,…,Xn):Xi∼Fi,i∈[n]},\mathcal{E}\_{n}(\mathbf{F})=\left\{\left(X\_{1},\ldots,X\_{n}\right):X\_{i}\sim F\_{i},i\in[n]\right\}, |  |

where 𝐅=(F1,…,Fn).\mathbf{F}=\left(F\_{1},\ldots,F\_{n}\right).

Next, we introduce the risk measures used in this paper to evaluate the risk.
Define the left quantile of a distribution FF and a random variable XX with X∼FX\sim F at α∈(0,1]\alpha\in(0,1] as

|  |  |  |
| --- | --- | --- |
|  | F−1​(α)=VaRα​(X)=inf{x:F​(x)⩾α},F^{-1}(\alpha)=\mathrm{VaR}\_{\alpha}(X)=\inf\{x:F(x)\geqslant\alpha\}, |  |

and for α∈[0,1),\alpha\in[0,1), the right quantile is given by

|  |  |  |
| --- | --- | --- |
|  | F+−1​(α)=VaRα+​(X)=inf{x:F​(x)>α}F^{-1}\_{+}(\alpha)=\mathrm{VaR}^{+}\_{\alpha}(X)=\inf\{x:F(x)>\alpha\} |  |

with the convention that inf∅=∞\inf\emptyset=\infty.

In this paper, we assume that all insurers and the reinsurer evaluate their risks using Range Value-at-Risk (RVaR\mathrm{RVaR}) , possibly at different levels.
For any α,β\alpha,\beta satisfying 0⩽β<β+α⩽1,0\leqslant\beta<\beta+\alpha\leqslant 1, the RVaR\mathrm{RVaR} of a random variable X∈L1X\in L^{1} at levels (α,β)(\alpha,\beta) is defined as

|  |  |  |
| --- | --- | --- |
|  | RVaRβ,α⁡(X)=1α​∫βα+βVaR1−γ​(X)​dγ.\operatorname{RVaR}\_{\beta,\alpha}(X)=\frac{1}{\alpha}\int\_{\beta}^{\alpha+\beta}\mathrm{VaR}\_{1-\gamma}(X)\mathrm{d}\gamma. |  |

Note that RVaR\operatorname{RVaR} falls in the family of distortion risk measures. Hence, it satisfies the properties enjoyed by the general distortion risk measures such as monotonicity, cash invariance, and comonotonic additivity; see Chapter 4 of Föllmer and Schied ([2016](https://arxiv.org/html/2512.11430v1#bib.bib26)).
Moreover, the two regulatory risk measures Value-at-Risk (VaR)(\mathrm{VaR}) and expected shortfall (ES)(\mathrm{ES}) are special cases or limits of RVaR\mathrm{RVaR}. Specifically,
for β∈(0,1)\beta\in(0,1) and X∈L0X\in L^{0},

|  |  |  |
| --- | --- | --- |
|  | VaR1−β​(X)=limα↓0RVaRβ,α​(X),and​VaR1−β+​(X)=limα↓0RVaRβ−α,α​(X),\mathrm{VaR}\_{1-\beta}(X)=\lim\_{\alpha\downarrow 0}\mathrm{RVaR}\_{\beta,\alpha}(X),\penalty 10000\ \text{and}\penalty 10000\ \mathrm{VaR}\_{1-\beta}^{+}(X)=\lim\_{\alpha\downarrow 0}\mathrm{RVaR}\_{\beta-\alpha,\alpha}(X), |  |

and for α∈[0,1)\alpha\in[0,1) and X∈L1X\in L^{1},

|  |  |  |
| --- | --- | --- |
|  | ESα​(X)=RVaR0,1−α​(X)=11−α​∫α1VaRγ​(X)​dγ.\mathrm{ES}\_{\alpha}(X)=\mathrm{RVaR}\_{0,1-\alpha}(X)=\frac{1}{1-\alpha}\int\_{\alpha}^{1}\mathrm{VaR}\_{\gamma}(X)\mathrm{d}\gamma. |  |

In this paper, our aim is to find the optimal reinsurance policies from the perspective of both the insurers and the reinsurer in the worst-case scenario under dependence uncertainty. A contract (𝐟,𝝅)∈ℐn×ℝn(\mathbf{f},\boldsymbol{\pi})\in\mathcal{I}^{n}\times\mathbb{R}^{n} is said to be *robust Pareto-optimal* under dependence uncertainty if there exists no other contract (𝐟^,𝝅^)∈ℐn×ℝn(\hat{\mathbf{f}},\hat{\boldsymbol{\pi}})\in\mathcal{I}^{n}\times\mathbb{R}^{n} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | RVaRβi,αi​(Tfi,πi​(Xi))\displaystyle\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(T\_{f\_{i},\pi\_{i}}(X\_{i})\right) | ⩾RVaRβi,αi​(Tf^i,π^i​(Xi)), for all ​i∈[n],\displaystyle\geqslant\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(T\_{\hat{f}\_{i},\hat{\pi}\_{i}}(X\_{i})\right),\text{ for all }i\in[n], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | sup𝐗∈ℰn​(𝐅)RVaRβ,α​(R𝐟,𝝅​(𝐗))\displaystyle\sup\_{\mathbf{X}\in\mathcal{E}\_{n}(\mathbf{F})}\mathrm{RVaR}\_{\beta,\alpha}\left(R\_{\mathbf{f},\boldsymbol{\pi}}(\mathbf{X})\right) | ⩾sup𝐗∈ℰn​(𝐅)RVaRβ,α​(R𝐟^,𝝅^​(𝐗)),\displaystyle\geqslant\sup\_{\mathbf{X}\in\mathcal{E}\_{n}(\mathbf{F})}\mathrm{RVaR}\_{\beta,\alpha}\left(R\_{\hat{\mathbf{f}},\hat{\boldsymbol{\pi}}}(\mathbf{X})\right), |  |

with at least one of these inequalities being strict. This concept highlights the inherent trade-offs between the insurers’ individual risk assessments and the reinsurer’s evaluation under the worst-case dependence structure.

The following proposition shows that robust Pareto-optimal contracts can be characterized through a single aggregated optimization problem.

###### Proposition 1.

A contract (𝐟,𝛑)∈ℐn×ℝn(\mathbf{f},\boldsymbol{\pi})\in\mathcal{I}^{n}\times\mathbb{R}^{n} is robust Pareto-optimal under dependence uncertainty if and only if 𝐟∈ℐn\mathbf{f}\in\mathcal{I}^{n} solves inf𝐟∈ℐnV​(𝐟),\inf\_{\mathbf{f}\in\mathcal{I}^{n}}V(\mathbf{f}), where

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(𝐟):=∑i=1nRVaRβi,αi​(Tfi,πi​(Xi))+sup𝐗∈ℰn​(𝐅)RVaRβ,α​(R𝐟,𝝅​(𝐗)),𝐟∈ℐ𝐧.V(\mathbf{f}):=\sum\_{i=1}^{n}\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(T\_{f\_{i},\pi\_{i}}(X\_{i})\right)+\sup\_{\mathbf{X}\in\mathcal{E}\_{n}(\mathbf{F})}\mathrm{RVaR}\_{\beta,\alpha}\left(R\_{\mathbf{f},\boldsymbol{\pi}}(\mathbf{X})\right),\penalty 10000\ \penalty 10000\ \penalty 10000\ \bf f\in\mathcal{I}^{n}. |  | (1) |

Note that V​(𝐟)V({\bf f}) is independent of 𝝅\boldsymbol{\pi} and hence we rewrite it as

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(𝐟)=∑i=1nRVaRβi,αi​(Tfi​(Xi))+sup𝐗∈ℰn​(𝐅)RVaRβ,α​(R𝐟​(𝐗)),V(\mathbf{f})=\sum\_{i=1}^{n}\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(T\_{f\_{i}}(X\_{i})\right)+\sup\_{\mathbf{X}\in\mathcal{E}\_{n}(\mathbf{F})}\mathrm{RVaR}\_{\beta,\alpha}\left(R\_{\mathbf{f}}(\mathbf{X})\right), |  | (2) |

where
Tfi​(Xi)=Xi−fi​(Xi)T\_{f\_{i}}(X\_{i})=X\_{i}-f\_{i}(X\_{i}) and
R𝐟​(𝐗)=∑i=1nfi​(Xi).R\_{\mathbf{f}}(\mathbf{X})=\sum\_{i=1}^{n}f\_{i}(X\_{i}).
In the following, we will focus on the optimal reinsurance policies such that V​(𝐟)V({\bf f}) is minimized over 𝐟∈ℐn.{\bf f}\in\mathcal{I}^{n}.

###### Remark 1.

In our framework, the premium πi\pi\_{i} for each insurer is treated as a fixed constant, agreed upon in advance between the insurer and the reinsurer. This reflects practical situations in which framework contracts or long-term agreements specify the premium upfront, leaving only the indemnity structure fif\_{i} adjustable by the insurer to manage retained risk. Under this assumption, the reinsurer’s net loss R𝐟,𝝅R\_{\mathbf{f},\boldsymbol{\pi}} depends on the indemnity functions up to an additive constant determined by the premiums.

A natural concern arises: if the reinsurer strictly seeks to minimize its risk, it could in principle choose fi=0f\_{i}=0, effectively avoiding any risk exposure. While this would indeed minimize the reinsurer’s risk, in practice, the reinsurer may still accept a positive fif\_{i} for several reasons: contractual obligations, regulatory requirements, long-term relationship considerations, or specified risk tolerances. Within this setup, Pareto optimality is meaningful: it identifies indemnity schedules where no participant—whether an insurer or the reinsurer—can reduce their own risk without increasing the risk of another, given the fixed premiums and the risk tolerances of all parties. Thus, with fixed premiums, Pareto-optimal contracts capture the efficient sharing of risk across insurers and the reinsurer, provided the reinsurer’s willingness to bear risk is bounded by these practical considerations.

From a theoretical perspective, treating the premium as fixed allows us to focus on the structure of Pareto-optimal reinsurance contracts under heterogeneous risk preferences and dependence uncertainty, without the additional complexity of a premium that varies with fif\_{i}.

## 3 Optimal insurance with dependence uncertainty

Note that Proposition [1](https://arxiv.org/html/2512.11430v1#Thmproposition1 "Proposition 1. ‣ 2 Model description and notation ‣ Pareto-optimal reinsurance under dependence uncertainty") implies that identifying a robust Pareto-optimal contract is equivalent to minimizing V​(𝐟)V(\mathbf{f}); that is, determining the optimal reinsurance strategies for individual insurers so that the total risk of a system with multiple insurers and a single reinsurer is minimized in the worst-case scenario under dependence uncertainty,
i.e., finding the optimal reinsurance policies 𝐟∈ℐn\mathbf{f}\in\mathcal{I}^{n} that solve:

|  |  |  |  |
| --- | --- | --- | --- |
|  | inf𝐟∈ℐn{∑i=1nRVaRβi,αi​(Tfi​(Xi))+sup𝐗∈ℰn​(𝐅)RVaRβ,α​(R𝐟​(𝐗))}.\inf\_{\mathbf{f}\in\mathcal{I}^{n}}\left\{\sum\_{i=1}^{n}\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(T\_{f\_{i}}(X\_{i})\right)+\sup\_{\mathbf{X}\in\mathcal{E}\_{n}(\mathbf{F})}\mathrm{RVaR}\_{\beta,\alpha}\left(R\_{\mathbf{f}}(\mathbf{X})\right)\right\}. |  | (3) |

Due to the limited availability of robust aggregation results for VaR and RVaR, it is sometimes necessary to impose additional restrictions on the indemnity functions, such as convexity or concavity. Accordingly, we consider the following domains:

|  |  |  |
| --- | --- | --- |
|  | ℐc​xn={𝐟=(f1,…,fn)∈ℐn:fi​ is convex for ​i∈[n]},\mathcal{I}\_{cx}^{n}=\left\{\mathbf{f}=(f\_{1},\ldots,f\_{n})\in\mathcal{I}^{n}:\ f\_{i}\text{ is convex for }i\in[n]\right\}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | ℐc​vn={𝐟=(f1,…,fn)∈ℐn:fi​ is concave for ​i∈[n]}.\mathcal{I}\_{cv}^{n}=\left\{\mathbf{f}=(f\_{1},\ldots,f\_{n})\in\mathcal{I}^{n}:\ f\_{i}\text{ is concave for }i\in[n]\right\}. |  |

For α∈(0,1),\alpha\in(0,1), we say that a distribution FF is concave beyond its α\alpha-quantile if the distribution (F​(x)−α)+/(1−α){(F(x)-\alpha)\_{+}}/{(1-\alpha)} is concave over (F+−1​(α),∞),(F\_{+}^{-1}(\alpha),\infty), and a distribution FF is convex beyond its α\alpha-quantile if the distribution (F​(x)−α)+/(1−α){(F(x)-\alpha)\_{+}}/{(1-\alpha)} is convex on (−∞,F−1​(1))(-\infty,F^{-1}(1)); see, for instance, Figure [1](https://arxiv.org/html/2512.11430v1#S3.F1 "Figure 1 ‣ 3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty"). We denote by ℳc​xα\mathcal{M}\_{cx}^{\alpha} the set of all distributions that are convex beyond their corresponding α\alpha-quantiles, and by ℳc​vα\mathcal{M}\_{cv}^{\alpha} the set of all distributions that are concave beyond their corresponding α\alpha-quantiles.

F+−1​(α)F^{-1}\_{+}(\alpha)01(F​(x)−α)+1−α\frac{(F(x)-\alpha)\_{+}}{1-\alpha}

F+−1​(α)F^{-1}\_{+}(\alpha)F−1​(1)F^{-1}(1)01(F​(x)−α)+1−α\frac{(F(x)-\alpha)\_{+}}{1-\alpha}

Figure 1: Concave beyond the α\alpha-quantile (left panel) and convex beyond the α\alpha-quantile (right panel).

The following representation for robust RVaR\mathrm{RVaR} with dependence uncertainty comes from Proposition 4 of Fadina et al. ([2025](https://arxiv.org/html/2512.11430v1#bib.bib25)), which is crucial for the proof of our Theorem [1](https://arxiv.org/html/2512.11430v1#Thmtheorem1 "Theorem 1. ‣ 3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty").
Define

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δn={𝜸∈(0,1)×[0,1)n:∑i=0nγi=1},with​𝜸=(γ0,γ1,…,γn).\Delta\_{n}=\left\{\boldsymbol{\gamma}\in(0,1)\times[0,1)^{n}:\sum\_{i=0}^{n}\gamma\_{i}=1\right\},\penalty 10000\ \text{with}\penalty 10000\ \boldsymbol{\gamma}=(\gamma\_{0},\gamma\_{1},\dots,\gamma\_{n}). |  | (4) |

Furthermore, for any α∈(0,1),\alpha\in(0,1), we define α​Δn={𝜸∈(0,1)×[0,1)n:∑i=0nγi=α}.\alpha\Delta\_{n}=\left\{\boldsymbol{\gamma}\in(0,1)\times[0,1)^{n}:\sum\_{i=0}^{n}\gamma\_{i}=\alpha\right\}.

###### Lemma 1.

Suppose that F1−1,…,Fn−1F\_{1}^{-1},\dots,F\_{n}^{-1} are continuous on (0,1).(0,1). For any α,β\alpha,\beta satisfying 0⩽β<β+α⩽1,0\leqslant\beta<\beta+\alpha\leqslant 1, if
𝐅∈(ℳc​v1−β−α)n,\mathbf{F}\in(\mathcal{M}\_{cv}^{1-\beta-\alpha})^{n},
then we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup𝐗∈ℰn​(𝐅)RVaRβ,α​(∑i=1nXi)=inf𝜸∈(β+α)​Δn,γ0⩾α∑i=1nRVaRγi,γ0​(Xi).\displaystyle\sup\_{\mathbf{X}\in\mathcal{E}\_{n}(\mathbf{F})}\mathrm{RVaR}\_{\beta,\alpha}\left(\sum\_{i=1}^{n}X\_{i}\right)=\inf\_{\boldsymbol{\gamma}\in(\beta+\alpha)\Delta\_{n},\gamma\_{0}\geqslant\alpha}\sum\_{i=1}^{n}\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(X\_{i}). |  | (5) |

The proof of Lemma [1](https://arxiv.org/html/2512.11430v1#Thmlemma1 "Lemma 1. ‣ 3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty") follows the arguments in Blanchet et al. ([2025](https://arxiv.org/html/2512.11430v1#bib.bib8)), which establish the representation for distributions with decreasing densities in the tail part. The extension to distributions that are concave in the tail region is provided in Fadina et al. ([2025](https://arxiv.org/html/2512.11430v1#bib.bib25)), thereby establishing Lemma [1](https://arxiv.org/html/2512.11430v1#Thmlemma1 "Lemma 1. ‣ 3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty").

Define
ga,b​(x):=(x−a)+−(x−b)+,g\_{a,b}(x):=(x-a)\_{+}-(x-b)\_{+},
where 0⩽a⩽b⩽∞0\leqslant a\leqslant b\leqslant\infty. This function represents a layered coverage, paying losses exceeding a retention level
aa that are capped at
bb. The special case b=∞b=\infty corresponds to the classical stop-loss indemnity, which covers all losses above the retention level. We denote
𝐠𝐚,𝐛=(ga1,b1,…,gan,bn){\bf g}\_{{\bf a},{\bf b}}=(g\_{a\_{1},b\_{1}},\dots,g\_{a\_{n},b\_{n}}) with parameter domain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜1={(𝐚,𝐛):𝐠𝐚,𝐛∈ℐn,0⩽ai⩽bi⩽∞,i∈[n]}.\displaystyle\mathcal{A}\_{1}=\{({\bf a},{\bf b}):{\bf g}\_{{\bf a},{\bf b}}\in\mathcal{I}^{n},0\leqslant a\_{i}\leqslant b\_{i}\leqslant\infty,\penalty 10000\ i\in[n]\}. |  | (6) |

Define ra,b,c​(x):=a​x+c​(x−b)+r\_{a,b,c}(x):=ax+c(x-b)\_{+} with 0⩽a,c⩽a+c⩽10\leqslant a,c\leqslant a+c\leqslant 1 and 0⩽b⩽∞.0\leqslant b\leqslant\infty. This class allows a flexible combination of proportional and excess-of-loss strategies, providing fine-grained control over both the proportion of loss retained and the additional protection above specified thresholds. The special case
b=∞b=\infty is reduced to a pure quota share, in which a fixed proportion of all losses is ceded.
We denote
𝐫𝐚,𝐛,𝐜=(ra1,b1,c1,…,ran,bn,cn){\bf r}\_{{\bf a},{\bf b},{\bf c}}=(r\_{a\_{1},b\_{1},c\_{1}},\dots,r\_{a\_{n},b\_{n},c\_{n}}) with parameter domain

|  |  |  |
| --- | --- | --- |
|  | 𝒜2={(𝐚,𝐛,𝐜):𝐫𝐚,𝐛,𝐜∈ℐn,0⩽ai,ci⩽ai+ci⩽1,bi⩾0,i∈[n]}.\mathcal{A}\_{2}=\{({\bf a},{\bf b},{\bf c}):{\bf r}\_{{\bf a},{\bf b},{\bf c}}\in\mathcal{I}^{n},0\leqslant a\_{i},c\_{i}\leqslant a\_{i}+c\_{i}\leqslant 1,b\_{i}\geqslant 0,\penalty 10000\ i\in[n]\}. |  |

In what follows, we use the convention that 00=0.\frac{0}{0}=0.

Our main result is stated as follows.

###### Theorem 1.

Let V​(𝐟)V(\mathbf{f}) be given by ([2](https://arxiv.org/html/2512.11430v1#S2.E2 "In 2 Model description and notation ‣ Pareto-optimal reinsurance under dependence uncertainty")), and Δn\Delta\_{n} be given by ([4](https://arxiv.org/html/2512.11430v1#S3.E4 "In 3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty")). Suppose F1−1,…,Fn−1F\_{1}^{-1},\dots,F\_{n}^{-1} are continuous on (0,1).(0,1). For any α,β\alpha,\beta satisfying 0⩽β<β+α⩽1,0\leqslant\beta<\beta+\alpha\leqslant 1, we have the following two conclusions.

1. (i)

   If β=0,\beta=0, then
   inff ∈InV(f)= inf(a,b)∈A1G(a,b), where

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | G​(𝐚,𝐛)=∑i=1n{RVaRβi,αi​(Xi)−RVaRβi,αi​(gai,bi​(Xi))+ES1−α​(gai,bi​(Xi))}.G({\bf a},{\bf b})=\sum\_{i=1}^{n}\left\{\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X\_{i})-\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(g\_{a\_{i},b\_{i}}(X\_{i})\right)+\mathrm{ES}\_{1-\alpha}(g\_{a\_{i},b\_{i}}(X\_{i}))\right\}. |  | (7) |
2. (ii)

   If 𝐅∈(ℳc​v1−β−α)n,\mathbf{F}\in(\mathcal{M}\_{cv}^{1-\beta-\alpha})^{n}, then
   inff ∈IcxnV(f)= inf(a,b,c)∈A2infγ∈(β+α)Δn,γ0⩾αR(a,b,c,γ), where

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | R​(𝐚,𝐛,𝐜,𝜸)=∑i=1n{RVaRβi,αi​(Xi)−RVaRβi,αi​(rai,bi,ci​(Xi))+RVaRγi,γ0​(rai,bi,ci​(Xi))}.R({\bf a},{\bf b},{\bf c},\boldsymbol{\gamma})=\sum\_{i=1}^{n}\left\{\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X\_{i})-\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i})\right)+\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i}))\right\}. |  | (8) |

The forms of optimal indemnity functions are given in Theorem [1](https://arxiv.org/html/2512.11430v1#Thmtheorem1 "Theorem 1. ‣ 3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty"). To determine the corresponding optimal reinsurance strategies, it remains to specify the parameters of these functions. This is addressed in the following proposition.

###### Proposition 2.

Let G​(𝐚,𝐛)G({\bf a},{\bf b}) and R​(𝐚,𝐛,𝐜,𝛄)R({\bf a},{\bf b},{\bf c},\boldsymbol{\gamma}) be given by ([7](https://arxiv.org/html/2512.11430v1#S3.E7 "In item (i) ‣ Theorem 1. ‣ 3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty")) and ([8](https://arxiv.org/html/2512.11430v1#S3.E8 "In item (ii) ‣ Theorem 1. ‣ 3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty")), respectively. The parameters of the optimal ceded loss functions 𝐠𝐚,𝐛{\bf g}\_{{\bf a},{\bf b}} and 𝐫𝐚,𝐛,𝐜{\bf r}\_{{\bf a},{\bf b},{\bf c}}, as defined in (i)–(ii) of Theorem [1](https://arxiv.org/html/2512.11430v1#Thmtheorem1 "Theorem 1. ‣ 3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty"), are well defined and are determined as follows

1. (i)

   For 𝐠𝐚,𝐛{\bf g}\_{{\bf a},{\bf b}},
   (a^\*, b^\*)∈arginf\_(a,b)∈A\_1
   G(a, b);
2. (ii)

   For 𝐫𝐚,𝐛,𝐜{\bf r}\_{{\bf a},{\bf b},{\bf c}},
   (a^\*,b^\*,c^\*)=arginf\_(a,b,c)∈A\_2
   {inf\_γ∈(β+α)Δ\_n,γ\_0⩾αR(a, b,c, γ)}.

Theorems [1](https://arxiv.org/html/2512.11430v1#Thmtheorem1 "Theorem 1. ‣ 3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty") and Proposition [2](https://arxiv.org/html/2512.11430v1#Thmproposition2 "Proposition 2. ‣ 3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty") provide a complete characterization of optimal reinsurance designs under the robust framework with multiple insurers and dependence uncertainty. Our analysis establishes that layered stop-loss indemnities g𝐚,𝐛g\_{{\bf a},{\bf b}} are optimal when evaluating risk using ES, while combined proportional-excess-of-loss contracts r𝐚,𝐛,𝐜r\_{{\bf a},{\bf b},{\bf c}} emerge as optimal under RVaR criteria for convex indemnities. This characterization effectively reduces the inherently infinite-dimensional optimization over admissible indemnity functions to tractable finite-dimensional parameter search problems over the domains 𝒜1\mathcal{A}\_{1} and 𝒜2\mathcal{A}\_{2}.
Proposition [2](https://arxiv.org/html/2512.11430v1#Thmproposition2 "Proposition 2. ‣ 3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty") further ensures the existence of optimal parameters and guarantees that these solutions can be obtained numerically. This transforms complex reinsurance contract design problems into computationally manageable optimization tasks, bridging theoretical optimality with practical implementability.

Note that the optimal indemnity functions derived in Theorem 2 of Fadina et al. ([2025](https://arxiv.org/html/2512.11430v1#bib.bib25)) have the form of a​min⁡(x,b)a\min(x,b) with 0⩽a⩽10\leqslant a\leqslant 1 and 0⩽b⩽∞0\leqslant b\leqslant\infty, which is very different from the optimal indemnity functions obtained in Theorem [1](https://arxiv.org/html/2512.11430v1#Thmtheorem1 "Theorem 1. ‣ 3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty") with the form ra,b,c​(x)=a​x+c​(x−b)+r\_{a,b,c}(x)=ax+c(x-b)\_{+} with 0⩽a,c⩽a+c⩽10\leqslant a,c\leqslant a+c\leqslant 1 and 0⩽b⩽∞.0\leqslant b\leqslant\infty. This is due to the qualitatively different setups of the models in the two papers. The objective in Fadina et al. ([2025](https://arxiv.org/html/2512.11430v1#bib.bib25)) is to minimize the total risk from the perspective of the reinsurer under dependence uncertainty, whereas the objective in our paper is to find the robust Pareto-optimal contract for a system consisting of multiple insurers and a single reinsurer. Moreover, the proof of Theorem [1](https://arxiv.org/html/2512.11430v1#Thmtheorem1 "Theorem 1. ‣ 3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty") is more complex as it involves the detailed discussion of six different cases.

## 4 Optimal solution to the special case of VaR

In this section, we examine the VaR-based optimal insurance problem, which represents a special case of RVaR. Recall that the relationship between these measures is given by VaR1−β​(X)=limα↓0RVaRβ,α​(X)\mathrm{VaR}\_{1-\beta}(X)=\lim\_{\alpha\downarrow 0}\mathrm{RVaR}\_{\beta,\alpha}(X). We next aim to minimize the following target:

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(𝐟)=∑i=1nVaRαi​(Tfi​(Xi))+sup𝐗∈ℰn​(𝐅)VaRα​(R𝐟​(𝐗)).V(\mathbf{f})=\sum\_{i=1}^{n}\mathrm{VaR}\_{\alpha\_{i}}\left(T\_{f\_{i}}(X\_{i})\right)+\sup\_{\mathbf{X}\in\mathcal{E}\_{n}(\mathbf{F})}\mathrm{VaR}\_{\alpha}\left(R\_{\mathbf{f}}(\mathbf{X})\right). |  | (9) |

An analogous representation for RVaR\mathrm{RVaR} in Lemma [1](https://arxiv.org/html/2512.11430v1#Thmlemma1 "Lemma 1. ‣ 3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty") can be established for VaR\mathrm{VaR}, which can also be extended to 𝐅∈(ℳc​xα)n\mathbf{F}\in(\mathcal{M}\_{cx}^{\alpha})^{n} in this special case.

###### Lemma 2.

Suppose F1−1,…,Fn−1F\_{1}^{-1},\dots,F\_{n}^{-1} are continuous on (0,1)(0,1) and 𝐅∈(ℳc​xα)n∪(ℳc​vα)n,\mathbf{F}\in\left(\mathcal{M}\_{cx}^{\alpha}\right)^{n}\cup\left(\mathcal{M}\_{cv}^{\alpha}\right)^{n}, then we have

|  |  |  |
| --- | --- | --- |
|  | sup𝐗∈ℰn​(𝐅)VaRα⁡(∑i=1nXi)=infγ∈(1−α)​Δn∑i=1nRVaRγi,γ0​(Xi).\sup\_{\mathbf{X}\in\mathcal{E}\_{n}(\mathbf{F})}\operatorname{VaR}\_{\alpha}\left(\sum\_{i=1}^{n}X\_{i}\right)=\inf\_{\gamma\in(1-\alpha)\Delta\_{n}}\sum\_{i=1}^{n}\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}\left(X\_{i}\right). |  |

###### Proof.

By Lemma 4.5 of Bernard et al. ([2014](https://arxiv.org/html/2512.11430v1#bib.bib5)), the continuity of F1−1,…,Fn−1F\_{1}^{-1},\dots,F\_{n}^{-1} over (0,1)(0,1) implies that for α∈(0,1),\alpha\in(0,1),

|  |  |  |
| --- | --- | --- |
|  | sup𝐗∈ℰn​(𝐅)VaRα+​(∑i=1nXi)=sup𝐗∈ℰn​(𝐅)VaRα​(∑i=1nXi).\sup\_{\mathbf{X}\in\mathcal{E}\_{n}(\mathbf{F})}\mathrm{VaR}\_{\alpha}^{+}\left(\sum\_{i=1}^{n}X\_{i}\right)=\sup\_{\mathbf{X}\in\mathcal{E}\_{n}(\mathbf{F})}\mathrm{VaR}\_{\alpha}\left(\sum\_{i=1}^{n}X\_{i}\right). |  |

Applying Proposition 1 of Fadina et al. ([2025](https://arxiv.org/html/2512.11430v1#bib.bib25)), we obtain the desired result.
∎

We introduce two additional reinsurance policies that will be used in our main results. Define
la,b​(x):=a​min⁡(x,b),l\_{a,b}(x):=a\min(x,b),
where 0⩽a⩽10\leqslant a\leqslant 1 and 0⩽b⩽∞,0\leqslant b\leqslant\infty, including the quota-share function as a special case (when b=∞b=\infty). Let
𝐥𝐚,𝐛=(la1,b1,…,lan,bn){\bf l}\_{{\bf a},{\bf b}}=(l\_{a\_{1},b\_{1}},\dots,l\_{a\_{n},b\_{n}}) with parameter domain

|  |  |  |
| --- | --- | --- |
|  | 𝒜3={(𝐚,𝐛):𝐥𝐚,𝐛∈ℐn,0⩽ai⩽1,0⩽bi⩽∞,i=1,…,n}.\mathcal{A}\_{3}=\{({\bf a},{\bf b}):{\bf l}\_{{\bf a},{\bf b}}\in\mathcal{I}^{n},0\leqslant a\_{i}\leqslant 1,0\leqslant b\_{i}\leqslant\infty,\penalty 10000\ i=1,\dots,n\}. |  |

Moreover, define
ha,b​(x):=a​(x−b)+,h\_{a,b}(x):=a(x-b)\_{+}, with 0⩽a⩽∞0\leqslant a\leqslant\infty and 0⩽b⩽1,0\leqslant b\leqslant 1, including the quota-share (b=0b=0) and stop-loss (a=1a=1) functions as special cases. Let 𝐡𝐚,𝐛=(ha1,b1,…,han,bn){\bf h}\_{{\bf a},{\bf b}}=(h\_{a\_{1},b\_{1}},\dots,h\_{a\_{n},b\_{n}}) with parameter domain

|  |  |  |
| --- | --- | --- |
|  | 𝒜4={(𝐚,𝐛):𝐡𝐚,𝐛∈ℐn,0⩽ai⩽1,0⩽bi⩽∞,i=1,…,n}.\mathcal{A}\_{4}=\{({\bf a},{\bf b}):{\bf h}\_{{\bf a},{\bf b}}\in\mathcal{I}^{n},0\leqslant a\_{i}\leqslant 1,0\leqslant b\_{i}\leqslant\infty,\penalty 10000\ i=1,\dots,n\}. |  |

Note that 𝒜4\mathcal{A}\_{4} constitutes a subset of 𝒜2\mathcal{A}\_{2}, indicating that when the RVaR risk measure degenerates to VaR, the structure of optimal ceded loss functions becomes more specific and constrained.

###### Theorem 2.

Let V​(𝐟)V(\mathbf{f}) be given by ([9](https://arxiv.org/html/2512.11430v1#S4.E9 "In 4 Optimal solution to the special case of VaR ‣ Pareto-optimal reinsurance under dependence uncertainty")). Suppose F1−1,…,Fn−1F\_{1}^{-1},\dots,F\_{n}^{-1} are continuous on (0,1)(0,1) and α∈(0,1).\alpha\in(0,1). We have the following conclusions.

1. (i)

   If n=2n=2 then

   |  |  |  |
   | --- | --- | --- |
   |  | inf𝐟∈ℐnV​(𝐟)=inf(𝐚,𝐛)∈𝒜1inf𝜸∈(1−α)​ΔnG¯​(𝐚,𝐛,𝜸),\displaystyle\inf\_{{\bf f}\in\mathcal{I}^{n}}V(\mathbf{f})=\inf\_{({\bf a},{\bf b})\in\mathcal{A}\_{1}}\inf\_{\boldsymbol{\gamma}\in(1-\alpha)\Delta\_{n}}\overline{G}({\bf a},{\bf b},{\boldsymbol{\gamma}}), |  |

   where

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | G¯​(𝐚,𝐛,𝜸)=∑i=1n{VaRαi​(Xi)−VaRαi​(gai,bi​(Xi))+RVaRγi,γ0​(gai,bi​(Xi))}.\displaystyle\overline{G}({\bf a},{\bf b},{\boldsymbol{\gamma}})=\sum\_{i=1}^{n}\left\{\mathrm{VaR}\_{\alpha\_{i}}(X\_{i})-\mathrm{VaR}\_{\alpha\_{i}}(g\_{a\_{i},b\_{i}}(X\_{i}))+\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(g\_{a\_{i},b\_{i}}(X\_{i}))\right\}. |  | (10) |
2. (ii)

   If 𝐅∈(ℳc​xα)n,\mathbf{F}\in(\mathcal{M}\_{cx}^{\alpha})^{n}, then

   |  |  |  |
   | --- | --- | --- |
   |  | inf𝐟∈ℐc​vnV​(𝐟)=inf(𝐚,𝐛)∈𝒜3inf𝜸∈(1−α)​ΔnL​(𝐚,𝐛,𝜸),\displaystyle\inf\_{{\bf f}\in\mathcal{I}\_{cv}^{n}}V(\mathbf{f})=\inf\_{({\bf a},{\bf b})\in\mathcal{A}\_{3}}\inf\_{\boldsymbol{\gamma}\in(1-\alpha)\Delta\_{n}}L({\bf a},{\bf b},{\boldsymbol{\gamma}}), |  |

   where
   L(a, b, γ)=∑i=1n{VaRαi(Xi)-VaRαi(lai,bi(Xi))+RVaRγi,γ0(lai,bi(Xi))}.
3. (iii)

   If 𝐅∈(ℳc​vα)n,\mathbf{F}\in(\mathcal{M}\_{cv}^{\alpha})^{n}, then

   |  |  |  |
   | --- | --- | --- |
   |  | inf𝐟∈ℐc​xnV​(𝐟)=inf(𝐚,𝐛)∈𝒜4inf𝜸∈(1−α)​ΔnH​(𝐚,𝐛,𝜸),\displaystyle\inf\_{{\bf f}\in\mathcal{I}\_{cx}^{n}}V(\mathbf{f})=\inf\_{({\bf a},{\bf b})\in\mathcal{A}\_{4}}\inf\_{\boldsymbol{\gamma}\in(1-\alpha)\Delta\_{n}}H({\bf a},{\bf b},{\boldsymbol{\gamma}}), |  |

   where
   H(a, b, γ)=∑i=1n{VaRαi(Xi)-VaRαi(hai,bi(Xi))+RVaRγi,γ0(hai,bi(Xi))}.

Further, for the case n=2n=2, we can offer a simpler expression than that of (i) of Theorem [2](https://arxiv.org/html/2512.11430v1#Thmtheorem2 "Theorem 2. ‣ 4 Optimal solution to the special case of VaR ‣ Pareto-optimal reinsurance under dependence uncertainty") by applying the result in Makarov ([1981](https://arxiv.org/html/2512.11430v1#bib.bib32)), which shows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup(X1,X2)∈ℰ2​(𝐅)VaRα+⁡(X1+X2)=inft∈[0,1−α]{VaRα+t​(X1)+VaR1−t​(X2)}.\displaystyle\sup\_{\left(X\_{1},X\_{2}\right)\in\mathcal{E}\_{2}(\mathbf{F})}\operatorname{VaR}^{+}\_{\alpha}\left(X\_{1}+X\_{2}\right)=\inf\_{t\in[0,1-\alpha]}\{\mathrm{VaR}\_{\alpha+t}(X\_{1})+\mathrm{VaR}\_{1-t}(X\_{2})\}. |  | (11) |

###### Proposition 3.

Let V​(𝐟)V(\mathbf{f}) be given by ([9](https://arxiv.org/html/2512.11430v1#S4.E9 "In 4 Optimal solution to the special case of VaR ‣ Pareto-optimal reinsurance under dependence uncertainty")). For n=2n=2, suppose that F1−1F\_{1}^{-1} and F2−1F\_{2}^{-1} are continuous on (0,1)(0,1), then

|  |  |  |
| --- | --- | --- |
|  | inf(f1,f2)∈ℐ2V​(𝐟)=inf(a1,a2,b1,b2)∈𝒜1inft∈[0,1−α]G¯1​(a1,a2,b1,b2,t),\displaystyle\inf\_{(f\_{1},f\_{2})\in\mathcal{I}^{2}}V({\bf f})=\inf\_{(a\_{1},a\_{2},b\_{1},b\_{2})\in\mathcal{A}\_{1}}\inf\_{t\in[0,1-\alpha]}\overline{G}\_{1}(a\_{1},a\_{2},b\_{1},b\_{2},t), |  |

where

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | G¯1​(a1,a2,b1,b2,t)=\displaystyle\overline{G}\_{1}(a\_{1},a\_{2},b\_{1},b\_{2},t)= | VaRα1​(X1)+VaRα2​(X2)+VaRα+t​(ga1,b1​(X1))−VaRα1​(ga1,b1​(X1))\displaystyle\mathrm{VaR}\_{\alpha\_{1}}(X\_{1})+\mathrm{VaR}\_{\alpha\_{2}}(X\_{2})+\mathrm{VaR}\_{\alpha+t}(g\_{a\_{1},b\_{1}}(X\_{1}))-\mathrm{VaR}\_{\alpha\_{1}}(g\_{a\_{1},b\_{1}}(X\_{1})) |  | (12) |
|  |  | +VaR1−t​(ga2,b2​(X2))−VaRα2​(ga2,b2​(X2)).\displaystyle+\mathrm{VaR}\_{1-t}(g\_{a\_{2},b\_{2}}(X\_{2}))-\mathrm{VaR}\_{\alpha\_{2}}(g\_{a\_{2},b\_{2}}(X\_{2})). |  |

Moreover, (ga1,b1,ga2,b2)(g\_{a\_{1},b\_{1}},g\_{a\_{2},b\_{2}}) are the optimal indemnity functions for the worst-case scenario, provided

|  |  |  |
| --- | --- | --- |
|  | (a1,a2,b1,b2)∈arg​inf(a1,a2,b1,b2)∈𝒜1{inft∈[0,1−α]G¯1​(a1,a2,b1,b2,t)}.(a\_{1},a\_{2},b\_{1},b\_{2})\in\arg\inf\_{(a\_{1},a\_{2},b\_{1},b\_{2})\in\mathcal{A}\_{1}}\left\{\inf\_{t\in[0,1-\alpha]}\overline{G}\_{1}(a\_{1},a\_{2},b\_{1},b\_{2},t)\right\}. |  |

###### Remark 2.

We observe from ([12](https://arxiv.org/html/2512.11430v1#S4.E12 "In Proposition 3. ‣ 4 Optimal solution to the special case of VaR ‣ Pareto-optimal reinsurance under dependence uncertainty")) that if either α⩾α1\alpha\geqslant\alpha\_{1} or α⩾α2\alpha\geqslant\alpha\_{2}, then the following inequalities hold for t∈[0,1−α]t\in[0,1-\alpha]:

|  |  |  |
| --- | --- | --- |
|  | VaRα+t​(ga1,b1​(X1))−ga1,b1​(VaRα1​(X1))⩾0orVaR1−t​(ga2,b2​(X2))−ga2,b2​(VaRα2​(X2))⩾0.\mathrm{VaR}\_{\alpha+t}\big(g\_{a\_{1},b\_{1}}(X\_{1})\big)-g\_{a\_{1},b\_{1}}\big(\mathrm{VaR}\_{\alpha\_{1}}(X\_{1})\big)\geqslant 0\quad\text{or}\quad\mathrm{VaR}\_{1-t}\big(g\_{a\_{2},b\_{2}}(X\_{2})\big)-g\_{a\_{2},b\_{2}}\big(\mathrm{VaR}\_{\alpha\_{2}}(X\_{2})\big)\geqslant 0. |  |

Consequently, the optimal value of the objective function coincides with the no-insurance benchmark, i.e.,
VaRαi​(Xi),i=1,2.\mathrm{VaR}\_{\alpha\_{i}}(X\_{i}),\penalty 10000\ i=1,2.
This implies that under these parameter conditions, purchasing insurance does not provide any improvement over the no-reinsurance case using VaR\mathrm{VaR} to quantify the risk.

To obtain the optimal reinsurance strategies, we need to fix the parameters of these functions in Theorem [2](https://arxiv.org/html/2512.11430v1#Thmtheorem2 "Theorem 2. ‣ 4 Optimal solution to the special case of VaR ‣ Pareto-optimal reinsurance under dependence uncertainty"), which will be discussed in the following proposition.
The proof follows along the same lines as that of Proposition [2](https://arxiv.org/html/2512.11430v1#Thmproposition2 "Proposition 2. ‣ 3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty") and is therefore omitted.

###### Proposition 4.

The parameters of the optimal ceded loss functions 𝐠𝐚,𝐛,𝐥𝐚,𝐛,𝐡𝐚,𝐛{\bf g}\_{{\bf a},{\bf b}},{\bf l}\_{{\bf a},{\bf b}},{\bf h}\_{{\bf a},{\bf b}} in (i)-(iii) of Theorem [2](https://arxiv.org/html/2512.11430v1#Thmtheorem2 "Theorem 2. ‣ 4 Optimal solution to the special case of VaR ‣ Pareto-optimal reinsurance under dependence uncertainty") are well defined and are determined as follows.

1. (i)

   For 𝐠𝐚,𝐛{\bf g}\_{{\bf a},{\bf b}},
   (a^\*, b^\*)∈arginf\_(a,b)∈A\_1{
   inf\_γ∈(1-α)Δ\_nG(a, b, γ)};
2. (ii)

   For 𝐥𝐚,𝐛{\bf l}\_{{\bf a},{\bf b}},
    (a^\*, b^\*)=arginf\_(a,b)∈A\_3
   {inf\_γ∈(1-α)Δ\_n L(a, b, γ)};
3. (iii)

   For 𝐡𝐚,𝐛{\bf h}\_{{\bf a},{\bf b}},
   (a^\*,b^\*)=arginf\_(a,b)∈A\_4
   {inf\_γ∈(1-α)Δ\_n H(a, b, γ)}.

In Theorem 1 of Fadina et al. ([2025](https://arxiv.org/html/2512.11430v1#bib.bib25)), the obtained optimal indemnity functions have the form (i) ga,bg\_{a,b} for n=2n=2; (ii) c​(x−a)++d​(x−b)+c(x-a)\_{+}+d(x-b)\_{+} with 0⩽a⩽b⩽∞0\leqslant a\leqslant b\leqslant\infty and 0⩽c,d⩽c+d⩽10\leqslant c,d\leqslant c+d\leqslant 1 for 𝐅∈(ℳc​xα)n\mathbf{F}\in(\mathcal{M}\_{cx}^{\alpha})^{n}; (iii) la,b​(x)=a​min⁡(x,b)l\_{a,b}(x)=a\min(x,b) with 0⩽a⩽10\leqslant a\leqslant 1 and 0⩽b⩽∞0\leqslant b\leqslant\infty for 𝐅∈(ℳc​vα)n\mathbf{F}\in(\mathcal{M}\_{cv}^{\alpha})^{n}. For the cases of 𝐅∈(ℳc​xα)n\mathbf{F}\in(\mathcal{M}\_{cx}^{\alpha})^{n} and 𝐅∈(ℳc​vα)n\mathbf{F}\in(\mathcal{M}\_{cv}^{\alpha})^{n}, the optimal indemnity functions in Fadina et al. ([2025](https://arxiv.org/html/2512.11430v1#bib.bib25)) are completely different from those derived in Theorem [2](https://arxiv.org/html/2512.11430v1#Thmtheorem2 "Theorem 2. ‣ 4 Optimal solution to the special case of VaR ‣ Pareto-optimal reinsurance under dependence uncertainty") due to the different setups of the two models.

## 5 Optimal solutions for i.i.d. risks

In the previous section, we analyzed the optimal reinsurance problem under fully unknown dependence, where the joint distribution of (X1,…,Xn)(X\_{1},\dots,X\_{n}) was unspecified and a worst-case formulation was necessary. In this section, we focus on the case where the risks X1,…,XnX\_{1},\dots,X\_{n} are i.i.d.. In particular, when n→∞n\to\infty, the aggregated risk exhibits asymptotic normality, which allows us to derive explicit and tractable expressions for the optimal indemnity functions. Our target is to minimize

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(𝐟):=∑i=1nRVaRβi,αi​(Tfi​(Xi))+RVaRβ,α​(R𝐟​(𝐗)),𝐟∈ℐ𝐧.V(\mathbf{f}):=\sum\_{i=1}^{n}\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(T\_{f\_{i}}(X\_{i})\right)+\mathrm{RVaR}\_{\beta,\alpha}\left(R\_{\mathbf{f}}(\mathbf{X})\right),\penalty 10000\ \penalty 10000\ \penalty 10000\ \bf f\in\mathcal{I}^{n}. |  | (13) |

The following proposition provides a classical asymptotic normality result for sums of i.i.d. transformed risks.

###### Proposition 5.

Let {Xi}i=1n\{X\_{i}\}\_{i=1}^{n} be a sequence of nonnegative i.i.d. random variables with mean 𝔼​[Xi]=μ<∞\mathbb{E}[X\_{i}]=\mu<\infty and variance Var​(Xi)=σ2<∞\mathrm{Var}(X\_{i})=\sigma^{2}<\infty. Define Sn=∑i=1nfi​(Xi)S\_{n}=\sum\_{i=1}^{n}f\_{i}(X\_{i}) with fi∈ℐf\_{i}\in\mathcal{I}. If Var​(Sn)→∞\mathrm{Var}(S\_{n})\to\infty as n→∞n\to\infty, then

|  |  |  |
| --- | --- | --- |
|  | Sn−𝔼​[Sn]Var​(Sn)→𝑑𝒩​(0,1).\frac{S\_{n}-\mathbb{E}[S\_{n}]}{\sqrt{\mathrm{Var}(S\_{n})}}\xrightarrow{d}\mathcal{N}(0,1). |  |

The condition Var​(Sn)→∞\mathrm{Var}(S\_{n})\to\infty in Proposition [5](https://arxiv.org/html/2512.11430v1#Thmproposition5 "Proposition 5. ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty") captures the natural growth of total accumulated risk as the number of risks increases, assuming that the fif\_{i} are nontrivial (not identically zero).

Because of the conclusion in Proposition [5](https://arxiv.org/html/2512.11430v1#Thmproposition5 "Proposition 5. ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty"), we suppose that R𝐟​(𝐗)∼𝒩​(𝔼​(R𝐟​(𝐗)),Var​(R𝐟​(𝐗)))R\_{\mathbf{f}}(\mathbf{X})\sim\mathcal{N}(\mathbb{E}(R\_{\mathbf{f}}(\mathbf{X})),\mathrm{Var}(R\_{\mathbf{f}}(\mathbf{X}))) in the following two subsections.

### 5.1 The results for RVaR

Recall that
α¯i=1−βi−αi,β¯i=1−βi,α¯=1−β−α,\bar{\alpha}\_{i}=1-\beta\_{i}-\alpha\_{i},\bar{\beta}\_{i}=1-\beta\_{i},\bar{\alpha}=1-\beta-\alpha, and β¯=1−β.\bar{\beta}=1-\beta.
Then the problem in equation ([13](https://arxiv.org/html/2512.11430v1#S5.E13 "In 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty")) asymptotically becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | min𝐟∈ℐn⁡V~​(𝐟):=∑i=1nRVaRβi,αi​(Xi−fi​(Xi))+μ​(𝐟)+σ​(𝐟)​1α​∫α¯β¯Φ−1​(γ)​dγ,\min\_{\mathbf{f}\in\mathcal{I}^{n}}\widetilde{V}(\mathbf{f}):=\sum\_{i=1}^{n}\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X\_{i}-f\_{i}(X\_{i}))+\mu(\mathbf{f})+\sigma(\mathbf{f})\frac{1}{\alpha}\int\_{\bar{\alpha}}^{\bar{\beta}}\Phi^{-1}(\gamma)\mathrm{d}\gamma, |  | (14) |

where Φ\Phi is the cumulative distribution function of a standard normal random variable, and

|  |  |  |
| --- | --- | --- |
|  | μ​(𝐟):=∑i=1n𝔼​[fi​(Xi)],σ2​(𝐟):=∑i=1nVar​(fi​(Xi)).\mu(\mathbf{f}):=\sum\_{i=1}^{n}\mathbb{E}[f\_{i}(X\_{i})],\qquad\sigma^{2}(\mathbf{f}):=\sum\_{i=1}^{n}\mathrm{Var}(f\_{i}(X\_{i})). |  |

###### Remark 3.

The optimization problem in ([14](https://arxiv.org/html/2512.11430v1#S5.E14 "In 5.1 The results for RVaR ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty")) admits an alternative interpretation in the context of collective reinsurance purchasing. Specifically, it can be viewed as minimizing the aggregate risk exposure of nn insurers who jointly purchase reinsurance for their respective business lines, with premiums calculated via a mean-standard deviation principle, where 1α​∫α¯β¯Φ−1​(γ)​dγ\frac{1}{\alpha}\int\_{\bar{\alpha}}^{\bar{\beta}}\Phi^{-1}(\gamma)\mathrm{d}\gamma serves as a loading coefficient.
In the special case when n=1n=1, our framework reduces to the single-insurer problem and generalizes part of the results of Chi ([2012](https://arxiv.org/html/2512.11430v1#bib.bib14)), who considered optimal reinsurance under VaR and ES criteria with mean-standard deviation premium principles.

The following lemma is well known; see, e.g., Property 3.4.19 in Denuit et al. ([2005](https://arxiv.org/html/2512.11430v1#bib.bib21)) and Lemma A.2 in Chi ([2012](https://arxiv.org/html/2512.11430v1#bib.bib14)).

###### Lemma 3.

Provided that the random variables Y1Y\_{1} and Y2Y\_{2} have finite expectations, if they satisfy

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Y1]=𝔼​[Y2],FY1​(t)⩽FY2​(t),t<t0,SY1​(t)⩽SY2​(t),t⩾t0\mathbb{E}\left[Y\_{1}\right]=\mathbb{E}\left[Y\_{2}\right],\quad F\_{Y\_{1}}(t)\leqslant F\_{Y\_{2}}(t),\quad t<t\_{0},\penalty 10000\ \penalty 10000\ S\_{Y\_{1}}(t)\leqslant S\_{Y\_{2}}(t),\quad t\geqslant t\_{0} |  |

for some t0∈ℝt\_{0}\in\mathbb{R}, then Y1⩽c​xY2Y\_{1}\leqslant\_{cx}Y\_{2}, i.e.,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[G​(Y1)]⩽𝔼​[G​(Y2)]\mathbb{E}\left[G\left(Y\_{1}\right)\right]\leqslant\mathbb{E}\left[G\left(Y\_{2}\right)\right] |  |

for any convex function G​(x)G(x) provided that the expectations exist.

Theorem [3](https://arxiv.org/html/2512.11430v1#Thmtheorem3 "Theorem 3. ‣ 5.1 The results for RVaR ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty") characterizes the explicit form of the optimal retention strategies in the asymptotic framework.

###### Theorem 3.

Let V~​(𝐟)\widetilde{V}({\bf f}) be given by ([14](https://arxiv.org/html/2512.11430v1#S5.E14 "In 5.1 The results for RVaR ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty")). We have

|  |  |  |
| --- | --- | --- |
|  | inf𝐟∈ℐnV~​(𝐟)=inf(𝐚,𝐛)∈𝒜1G~​(𝐚,𝐛),\displaystyle\inf\_{\mathbf{f}\in\mathcal{I}^{n}}\widetilde{V}({\bf f})=\inf\_{({\bf a},{\bf b})\in\mathcal{A}\_{1}}\widetilde{G}({\bf a},{\bf b}), |  |

where

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | G~​(𝐚,𝐛)\displaystyle\widetilde{G}({\bf a},{\bf b}) | =∑i=1n{RVaRβi,αi​(Xi)−RVaRβi,αi​(gai,bi​(Xi))+𝔼​[gai,bi​(Xi)]}\displaystyle=\sum\_{i=1}^{n}\left\{\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X\_{i})-\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(g\_{a\_{i},b\_{i}}(X\_{i})\right)+\mathbb{E}[g\_{a\_{i},b\_{i}}(X\_{i})]\right\} |  | (15) |
|  |  | +(∑i=1nVar​(gai,bi​(Xi)))1/2​1α​∫α¯β¯Φ−1​(γ)​dγ.\displaystyle+\left(\sum\_{i=1}^{n}\mathrm{Var}(g\_{a\_{i},b\_{i}}(X\_{i}))\right)^{1/2}\frac{1}{\alpha}\int\_{\bar{\alpha}}^{\bar{\beta}}\Phi^{-1}(\gamma)\mathrm{d}\gamma. |  |

The layered structure of the optimal strategy in Theorem [3](https://arxiv.org/html/2512.11430v1#Thmtheorem3 "Theorem 3. ‣ 5.1 The results for RVaR ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty") under the asymptotic normality framework aligns with the forms identified in worst-case scenarios where RVaR degenerates to ES (when β=0\beta=0) in Theorem [1](https://arxiv.org/html/2512.11430v1#Thmtheorem1 "Theorem 1. ‣ 3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty") or VaR (when n=2n=2) in Theorem [2](https://arxiv.org/html/2512.11430v1#Thmtheorem2 "Theorem 2. ‣ 4 Optimal solution to the special case of VaR ‣ Pareto-optimal reinsurance under dependence uncertainty").
Notably, this common layered form emerges in our asymptotic setting without requiring any distributional assumptions on XiX\_{i} or functional form restrictions on fif\_{i}.

The proof for Proposition [6](https://arxiv.org/html/2512.11430v1#Thmproposition6 "Proposition 6. ‣ 5.1 The results for RVaR ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty") follows along the same lines as that of Proposition [2](https://arxiv.org/html/2512.11430v1#Thmproposition2 "Proposition 2. ‣ 3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty") and is therefore omitted.

###### Proposition 6.

Let G~\widetilde{G} be given by ([15](https://arxiv.org/html/2512.11430v1#S5.E15 "In Theorem 3. ‣ 5.1 The results for RVaR ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty")). The parameters of the optimal ceded loss function 𝐠𝐚,𝐛{\bf g}\_{{\bf a},{\bf b}} of Theorem [3](https://arxiv.org/html/2512.11430v1#Thmtheorem3 "Theorem 3. ‣ 5.1 The results for RVaR ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty") exists and is determined by

|  |  |  |
| --- | --- | --- |
|  | (𝐚∗,𝐛∗)∈arg​inf(𝐚,𝐛)∈𝒜1G​(𝐚,𝐛).({\bf a}^{\*},{\bf b}^{\*})\in\arg\inf\_{({\bf a},{\bf b})\in\mathcal{A}\_{1}}G({\bf a},{\bf b}). |  |

### 5.2 The result for VaR

In this section, we solve for the optimal insurance contract under the VaR-based criterion in the asymptotic framework. Firstly, we show that solving the VaR-based optimal insurance problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(𝐟)=∑i=1nVaRαi​(Tfi​(Xi))+VaRα​(R𝐟​(𝐗))\displaystyle V(\mathbf{f})=\sum\_{i=1}^{n}\mathrm{VaR}\_{\alpha\_{i}}\left(T\_{f\_{i}}(X\_{i})\right)+\mathrm{VaR}\_{\alpha}\left(R\_{\mathbf{f}}(\mathbf{X})\right) |  | (16) |

over 𝐟∈ℐn\mathbf{f}\in\mathcal{I}^{n} is equivalent to solving ([16](https://arxiv.org/html/2512.11430v1#S5.E16 "In 5.2 The result for VaR ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty")) over 𝐠𝐚,𝐛∈ℐn\mathbf{g}\_{{\bf a},{\bf b}}\in\mathcal{I}^{n}, as shown in the proposition below.

###### Proposition 7.

The optimization problem ([16](https://arxiv.org/html/2512.11430v1#S5.E16 "In 5.2 The result for VaR ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty")) over ℐn\mathcal{I}^{n} can be equivalently reformulated as

|  |  |  |
| --- | --- | --- |
|  | inf𝐟∈ℐnV​(𝐟)=inf(𝐚,𝐛)∈𝒜1G0​(𝐚,𝐛),\displaystyle\inf\_{{\bf f}\in\mathcal{I}^{n}}V(\mathbf{f})=\inf\_{({\bf a},{\bf b})\in\mathcal{A}\_{1}}G\_{0}({\bf a},{\bf b}), |  |

where G0​(𝐚,𝐛)G\_{0}({\bf a},{\bf b}) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | G0​(𝐚,𝐛)=∑i=1n{VaRαi​(Xi)−gai,bi​(VaRαi​(Xi))}+VaRα​(∑i=1ngai,bi​(Xi)).\displaystyle G\_{0}({\bf a},{\bf b})=\sum\_{i=1}^{n}\left\{\mathrm{VaR}\_{\alpha\_{i}}(X\_{i})-g\_{a\_{i},b\_{i}}\left(\mathrm{VaR}\_{\alpha\_{i}}(X\_{i})\right)\right\}+\mathrm{VaR}\_{\alpha}\left(\sum\_{i=1}^{n}g\_{a\_{i},b\_{i}}(X\_{i})\right). |  | (17) |

Proposition [7](https://arxiv.org/html/2512.11430v1#Thmproposition7 "Proposition 7. ‣ 5.2 The result for VaR ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty") indicates that, when the multivariate risks
{Xi}i=1n\{X\_{i}\}\_{i=1}^{n} are i.i.d., the Central Limit Theorem can be applied
directly to the aggregate ∑i=1ngai,bi\sum\_{i=1}^{n}g\_{a\_{i},b\_{i}} in the asymptotic
analysis of aggregation risk, which gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | ming𝐚,𝐛∈𝒜1⁡{∑i=1nVaRαi​(X−gai,bi​(X))+μ​(g𝐚,𝐛)+Φ−1​(α)​σ​(g𝐚,𝐛)},\min\_{g\_{{\bf a},{\bf b}}\in\mathcal{A}\_{1}}\left\{\sum\_{i=1}^{n}\mathrm{VaR}\_{\alpha\_{i}}(X-g\_{a\_{i},b\_{i}}(X))+\mu(g\_{{\bf a},{\bf b}})+\Phi^{-1}(\alpha)\,\sigma(g\_{{\bf a},{\bf b}})\right\}, |  | (18) |

where

|  |  |  |
| --- | --- | --- |
|  | μ​(g𝐚,𝐛)=∑i=1n𝔼​[gai,bi​(X)],σ2​(g𝐚,𝐛)=∑i=1nVar​(gai,bi​(X)),\mu(g\_{{\bf a},{\bf b}})=\sum\_{i=1}^{n}\mathbb{E}[g\_{a\_{i},b\_{i}}(X)],\qquad\sigma^{2}(g\_{{\bf a},{\bf b}})=\sum\_{i=1}^{n}\mathrm{Var}(g\_{a\_{i},b\_{i}}(X)), |  |

and the parameters satisfy
0⩽ai⩽VaRαi​(X)0\leqslant a\_{i}\leqslant\mathrm{VaR}\_{\alpha\_{i}}(X)
and
bi=VaRαi​(X)b\_{i}=\mathrm{VaR}\_{\alpha\_{i}}(X).

In the next theorem, we can determine the optimal ceded loss functions g𝐚,𝐛g\_{{\bf a},{\bf b}} explicitly for ([18](https://arxiv.org/html/2512.11430v1#S5.E18 "In 5.2 The result for VaR ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty")). For convenience, define

|  |  |  |
| --- | --- | --- |
|  | wi​(ai)=∫aiVaRαi​(Xi)SX​(x)​dx,andvi​(ai)=2​∫aiVaRαi​(Xi)(x−ai)​SX​(x)​dx.w\_{i}(a\_{i})=\int\_{a\_{i}}^{\mathrm{VaR}\_{\alpha\_{i}}(X\_{i})}S\_{X}(x)\mathrm{d}x,\penalty 10000\ \penalty 10000\ \text{and}\penalty 10000\ \penalty 10000\ v\_{i}(a\_{i})=2\int\_{a\_{i}}^{\mathrm{VaR}\_{\alpha\_{i}}(X\_{i})}(x-a\_{i})S\_{X}(x)\mathrm{d}x. |  |

###### Theorem 4.

The optimal indemnity functions 𝐠𝐚,𝐛∗=(ga1,b1∗,…,gan,bn∗){\mathbf{g}}^{\*}\_{{\bf a},{\bf b}}=(g^{\*}\_{a\_{1},b\_{1}},\dots,g^{\*}\_{a\_{n},b\_{n}}) for Problem ([18](https://arxiv.org/html/2512.11430v1#S5.E18 "In 5.2 The result for VaR ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty")) are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | gai∗,bi∗∗​(x)=(x−ai∗)+−(x−bi∗)+,i=1,…,n,g^{\*}\_{a^{\*}\_{i},b^{\*}\_{i}}(x)=(x-a^{\*}\_{i})\_{+}-(x-b^{\*}\_{i})\_{+},\quad i=1,\dots,n, |  | (19) |

with parameters determined by

|  |  |  |
| --- | --- | --- |
|  | ai∗=inf{0⩽ai⩽VaRαi​(Xi):1−Φ−1​(α)⋅wi​(ai)2∑j=1n(vj​(aj)−wj​(aj)2)⩾0},a\_{i}^{\*}=\inf\left\{0\leqslant a\_{i}\leqslant\mathrm{VaR}\_{\alpha\_{i}}(X\_{i}):1-\Phi^{-1}(\alpha)\cdot\frac{w\_{i}(a\_{i})^{2}}{\sum\_{j=1}^{n}\left(v\_{j}(a\_{j})-w\_{j}(a\_{j})^{2}\right)}\geqslant 0\right\}, |  |

and bi∗=VaRαi​(Xi)b\_{i}^{\*}=\mathrm{VaR}\_{\alpha\_{i}}(X\_{i}).

###### Corollary 1.

For α1=⋯=αn\alpha\_{1}=\dots=\alpha\_{n}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ga1,b1∗​(x)=⋯=gan,bn∗​(x)=(x−a∗)+−(x−VaRα​(X))+{g}^{\*}\_{a\_{1},b\_{1}}(x)=\dots={g}^{\*}\_{a\_{n},b\_{n}}(x)=(x-a^{\*})\_{+}-(x-\mathrm{VaR}\_{\alpha}(X))\_{+} |  | (20) |

with

|  |  |  |
| --- | --- | --- |
|  | a∗=inf{0⩽a⩽VaRα​(X):1−Φ−1​(α)​w​(a)2n​(v​(a)−w​(a)2)⩾0},a^{\*}=\inf\left\{0\leqslant a\leqslant\mathrm{VaR}\_{\alpha}(X):1-\Phi^{-1}(\alpha)\frac{w(a)^{2}}{n(v(a)-w(a)^{2})}\geqslant 0\right\}, |  |

in which

|  |  |  |
| --- | --- | --- |
|  | w​(a)=∫aVaRα​(X)SX​(x)​dx,andv​(a)=2​∫aVaRα​(X)(x−a)​SX​(x)​dx.w(a)=\int\_{a}^{\mathrm{VaR}\_{\alpha}(X)}S\_{X}(x)\mathrm{d}x,\penalty 10000\ \penalty 10000\ \text{and}\penalty 10000\ \penalty 10000\ v(a)=2\int\_{a}^{\mathrm{VaR}\_{\alpha}(X)}(x-a)S\_{X}(x)\mathrm{d}x. |  |

In particular, a∗=0a^{\*}=0 as n→∞.n\to\infty.

Corollary [1](https://arxiv.org/html/2512.11430v1#Thmcorollary1 "Corollary 1. ‣ 5.2 The result for VaR ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty") highlights that when the insurer pools a large number of i.i.d. risks, the aggregate ceded loss
∑i=1nga,b​(Xi)\sum\_{i=1}^{n}g\_{a,b}(X\_{i}) becomes increasingly predictable due to diversification.
As a result, the incentive to introduce a positive attachment point a>0a>0 vanishes.

## 6 Simulation studies

In this section, we present two simulation studies to illustrate our theoretical results. In Section [6.1](https://arxiv.org/html/2512.11430v1#S6.SS1 "6.1 Effects of dependence and confidence levels ‣ 6 Simulation studies ‣ Pareto-optimal reinsurance under dependence uncertainty"), we provide a case study that examines the minimization of ([9](https://arxiv.org/html/2512.11430v1#S4.E9 "In 4 Optimal solution to the special case of VaR ‣ Pareto-optimal reinsurance under dependence uncertainty")) under the special case where RVaR is reduced to VaR. We consider three distinct dependence structures: i.i.d. risks, comonotonic risks, and dependence uncertainty.
Section [6.2](https://arxiv.org/html/2512.11430v1#S6.SS2 "6.2 Effects of distributional assumptions ‣ 6 Simulation studies ‣ Pareto-optimal reinsurance under dependence uncertainty") presents comparative examples that demonstrate the differences in optimal reinsurance design for a general distribution FF versus the case where F∈(ℳc​v)nF\in(\mathcal{M}\_{cv})^{n}, as characterized in Theorem [2](https://arxiv.org/html/2512.11430v1#Thmtheorem2 "Theorem 2. ‣ 4 Optimal solution to the special case of VaR ‣ Pareto-optimal reinsurance under dependence uncertainty").

### 6.1 Effects of dependence and confidence levels

We present an illustrative example that solves the minimization problem ([9](https://arxiv.org/html/2512.11430v1#S4.E9 "In 4 Optimal solution to the special case of VaR ‣ Pareto-optimal reinsurance under dependence uncertainty")) under three different dependence structures—i.i.d., comonotonicity, and dependence uncertainty when n=2n=2. In particular, the optimization problem ([9](https://arxiv.org/html/2512.11430v1#S4.E9 "In 4 Optimal solution to the special case of VaR ‣ Pareto-optimal reinsurance under dependence uncertainty")) can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | K​(𝐚,𝐛)=∑i=12VaRαi​(Xi−gai,bi​(Xi))+VaRα​(∑i=12gai,bi​(Xi)).\displaystyle K({\bf a},{\bf b})=\sum\_{i=1}^{2}\mathrm{VaR}\_{\alpha\_{i}}(X\_{i}-g\_{a\_{i},b\_{i}}(X\_{i}))+\mathrm{VaR}\_{\alpha}\Big(\sum\_{i=1}^{2}g\_{a\_{i},b\_{i}}(X\_{i})\Big). |  | (21) |

Under the different dependence structures, K​(𝐚,𝐛)K({\bf a},{\bf b}) takes the following forms:

1. (i)

   Worst-case: K​(𝐚,𝐛)=inft∈[0,1−α]G¯1​(𝐚,𝐛,t),K({\bf a},{\bf b})=\inf\_{t\in[0,1-\alpha]}\overline{G}\_{1}({\bf a},{\bf b},t),
   where G¯1\overline{G}\_{1} is defined in ([12](https://arxiv.org/html/2512.11430v1#S4.E12 "In Proposition 3. ‣ 4 Optimal solution to the special case of VaR ‣ Pareto-optimal reinsurance under dependence uncertainty"));
2. (ii)

   i.i.d. case:
   K​(𝐚,𝐛)=G0​(𝐚,𝐛),K({\bf a},{\bf b})=G\_{0}({\bf a},{\bf b}),
   where G0G\_{0} is defined in ([17](https://arxiv.org/html/2512.11430v1#S5.E17 "In Proposition 7. ‣ 5.2 The result for VaR ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty"));
3. (iii)

   Comonotonic case:
   K​(𝐚,𝐛)=∑i=12VaRαi​(Xi−gai,bi​(Xi))+∑i=12VaRα​(gai,bi​(Xi)).K({\bf a},{\bf b})=\sum\_{i=1}^{2}\mathrm{VaR}\_{\alpha\_{i}}(X\_{i}-g\_{a\_{i},b\_{i}}(X\_{i}))+\sum\_{i=1}^{2}\mathrm{VaR}\_{\alpha}(g\_{a\_{i},b\_{i}}(X\_{i})).

###### Lemma 4.

Suppose F1−1F\_{1}^{-1} and F2−1F\_{2}^{-1} are identical and continuous on (0,1)(0,1), and let α∈(0,1)\alpha\in(0,1). Then, under the different dependence structures, the following holds:

|  |  |  |
| --- | --- | --- |
|  | inf(𝐚,𝐛)∈𝒜1K​(𝐚,𝐛)=inf𝐮∈𝒜𝟏​(𝐮)K​(𝐮,𝐯),\displaystyle\inf\_{({\bf a},{\bf b})\in\mathcal{A}\_{1}}K({\bf a},{\bf b})=\inf\_{\bf u\in\mathcal{A}\_{1}(\bf u)}K(\bf u,\bf v), |  |

where vi=VaRαi​(Xi)v\_{i}=\mathrm{VaR}\_{\alpha\_{i}}(X\_{i}) for i=1,2i=1,2, and

|  |  |  |
| --- | --- | --- |
|  | 𝒜1​(𝐮)={𝐮:𝐠𝐮,𝐯∈ℐn, 0⩽ui⩽vi⩽∞,i=1,2}.\displaystyle\mathcal{A}\_{1}({\bf u})=\{{\bf u}:\mathbf{g\_{{\bf u},{\bf v}}}\in\mathcal{I}^{n},\penalty 10000\ 0\leqslant u\_{i}\leqslant v\_{i}\leqslant\infty,\penalty 10000\ i=1,2\}. |  |

Obtaining a closed-form solution for the optimal insurance problem ([21](https://arxiv.org/html/2512.11430v1#S6.E21 "In 6.1 Effects of dependence and confidence levels ‣ 6 Simulation studies ‣ Pareto-optimal reinsurance under dependence uncertainty")) remains challenging even under the i.i.d. assumption. Therefore, we employ the asymptotic normality result established in Theorem [4](https://arxiv.org/html/2512.11430v1#Thmtheorem4 "Theorem 4. ‣ 5.2 The result for VaR ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty") to derive numerical solutions.

We generate independent samples of XiX\_{i}, i=1,2i=1,2, from a Pareto distribution with cumulative distribution function

|  |  |  |
| --- | --- | --- |
|  | FX​(x)=1−(1+xλ)−β,F\_{X}(x)=1-\left(1+\frac{x}{\lambda}\right)^{-\beta}, |  |

where we set β=9\beta=9 and λ=8\lambda=8. This parameterization yields 𝔼​[Xi]=1\mathbb{E}[X\_{i}]=1 and Var​(Xi)=97\mathrm{Var}(X\_{i})=\frac{9}{7}.

We consider three scenarios with α1>α2\alpha\_{1}>\alpha\_{2} to examine different configurations of confidence levels:

* •

  Case 1: α1=0.9\alpha\_{1}=0.9, α2=0.85\alpha\_{2}=0.85, α=0.95\alpha=0.95
* •

  Case 2: α1=0.95\alpha\_{1}=0.95, α2=0.85\alpha\_{2}=0.85, α=0.9\alpha=0.9
* •

  Case 3: α1=0.95\alpha\_{1}=0.95, α2=0.9\alpha\_{2}=0.9, α=0.85\alpha=0.85

The corresponding parameter choices and numerical results are summarized in Table [1](https://arxiv.org/html/2512.11430v1#S6.T1 "Table 1 ‣ 6.1 Effects of dependence and confidence levels ‣ 6 Simulation studies ‣ Pareto-optimal reinsurance under dependence uncertainty").

Table 1: Optimal parameters (a1∗,a2∗)(a\_{1}^{\*},a\_{2}^{\*}) and objective values under different dependence structures

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Case | Dependence | Objective Value | a1∗a\_{1}^{\*} | a2∗a\_{2}^{\*} | t∗t^{\*} |
| 1 | Worst-case | 4.2096 | [0,2.3324][0,2.3324] | [0,1.8772][0,1.8772] | 0 |
| Comonotonic | 4.2096 | [0,2.3324][0,2.3324] | [0,1.8772][0,1.8772] | – |
| i.i.d. | 3.2695 | 0.4224 | 0.3372 | – |
| 2 | Worst-case | 4.2096 | [0,2.3324][0,2.3324] | [0,1.8772][0,1.8772] | 0 |
| Comonotonic | 4.2096 | [0,2.3324][0,2.3324] | [0,1.8772][0,1.8772] | – |
| i.i.d. | 3.1258 | 0.0996 | 0.0072 | – |
| 3 | Worst-case | 4.2096 | [0,1.8772][0,1.8772] | [0,2.3324][0,2.3324] | 0 |
| Comonotonic | 3.7545 | [0,1.8772][0,1.8772] | [0,1.8772][0,1.8772] | – |
| i.i.d. | 2.9832 | 0 | 0 | – |

Note: VaR0.85​(X)=1.8772\mathrm{VaR}\_{0.85}(X)=1.8772, VaR0.9​(X)=2.3324\mathrm{VaR}\_{0.9}(X)=2.3324. The notation [0,c][0,c] indicates that any value in the interval achieves the same optimal objective value, and t∗t^{\*} is related to the optimal value of tt in Proposition [3](https://arxiv.org/html/2512.11430v1#Thmproposition3 "Proposition 3. ‣ 4 Optimal solution to the special case of VaR ‣ Pareto-optimal reinsurance under dependence uncertainty"). Dashes (–) indicate that the parameter t∗t^{\*} is not applicable in that setting.

The emergence of interval-valued optimal parameters stems from the specific structure of our objective function K​(𝐚,𝐛)K(\mathbf{a},\mathbf{b}). From Table [1](https://arxiv.org/html/2512.11430v1#S6.T1 "Table 1 ‣ 6.1 Effects of dependence and confidence levels ‣ 6 Simulation studies ‣ Pareto-optimal reinsurance under dependence uncertainty"), we observe the following patterns: Under the worst-case condition, we obtain t∗=0t^{\*}=0 in all three scenarios, although this does not hold in general (see Section [6.2](https://arxiv.org/html/2512.11430v1#S6.SS2 "6.2 Effects of distributional assumptions ‣ 6 Simulation studies ‣ Pareto-optimal reinsurance under dependence uncertainty")). This particular choice of t∗=0t^{\*}=0 implies that the parameter a2∗a^{\*}\_{2} can take any value within the interval [0,VaRα2​(X)][0,\mathrm{VaR}\_{\alpha\_{2}}(X)] without affecting the optimal objective value, since the condition α2+t⩽1\alpha\_{2}+t\leqslant 1 is satisfied throughout this range; see Remark [2](https://arxiv.org/html/2512.11430v1#Thmremark2 "Remark 2. ‣ 4 Optimal solution to the special case of VaR ‣ Pareto-optimal reinsurance under dependence uncertainty") for details.

In Case 1, the optimal objective values under both comonotonic and worst-case dependence coincide, equaling ∑i=12VaRαi​(Xi)\sum\_{i=1}^{2}\mathrm{VaR}\_{\alpha\_{i}}(X\_{i}), which exceeds the value obtained under the i.i.d. condition.
Given that α⩾α1⩾α2\alpha\geqslant\alpha\_{1}\geqslant\alpha\_{2}, the optimal intervals ai∈[0,bi∗]a\_{i}\in[0,b\_{i}^{\*}] indicate that under comonotonic and worst-case dependence, insurers can select any retention level within [0,VaRαi​(Xi)][0,\mathrm{VaR}\_{\alpha\_{i}}(X\_{i})] for losses up to VaRαi​(Xi)\mathrm{VaR}\_{\alpha\_{i}}(X\_{i}), while retaining all losses beyond this threshold. This results in the same aggregate risk measure as having no reinsurance at all.

In Case 2, where α1⩾α⩾α2\alpha\_{1}\geqslant\alpha\geqslant\alpha\_{2}, under both comonotonic and worst-case dependence, only the second insurer possesses flexibility, being able to choose any retention level for a2∗∈[0,VaRα2​(X2)]a\_{2}^{\*}\in[0,\mathrm{VaR}\_{\alpha\_{2}}(X\_{2})] while taking no reinsurance beyond this threshold. This leads to the same outcome as purchasing no reinsurance for the second insurer.
For the first insurer, the optimal strategy involves reinsuring the layer x−a1x-a\_{1} for losses in the interval x∈[VaRα​(X1),VaRα1​(X1)]x\in[\mathrm{VaR}\_{\alpha}(X\_{1}),\mathrm{VaR}\_{\alpha\_{1}}(X\_{1})], while maintaining flexibility in other regions. Furthermore, under the i.i.d. condition, we observe the intuitive result that a1⩾a2a\_{1}\geqslant a\_{2} when α1⩾α2\alpha\_{1}\geqslant\alpha\_{2}, reflecting that higher risk tolerance requires less reinsurance.
Although the comonotonic scenario yields a higher objective value than the i.i.d. case in this particular configuration, we emphasize that this ordering is not universal. As demonstrated in Figure [2](https://arxiv.org/html/2512.11430v1#S6.F2 "Figure 2 ‣ 6.1 Effects of dependence and confidence levels ‣ 6 Simulation studies ‣ Pareto-optimal reinsurance under dependence uncertainty"), the relationship between optimal values under different dependence structures can vary across parameter settings.

In Case 3, the parameter tt remains at 0, and the optimal reinsurance structure under the worst-case condition resembles that observed in Case 2. The worst-case objective value exceeds the comonotonic value, demonstrating that comonotonic dependence does not always constitute the worst-case scenario for VaR-based risk measures. Under comonotonic dependence, any combination of a1,a2∈[0,VaRα​(Xi)]a\_{1},a\_{2}\in[0,\mathrm{VaR}\_{\alpha}(X\_{i})] minimizes the objective function.
In contrast, under the i.i.d. condition, the unique optimal solution is a1=a2=0a\_{1}=a\_{2}=0. This outcome follows directly from Theorem [4](https://arxiv.org/html/2512.11430v1#Thmtheorem4 "Theorem 4. ‣ 5.2 The result for VaR ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty"): when α\alpha is sufficiently small relative to α1\alpha\_{1} and α2\alpha\_{2}, the condition 1−Φ−1​(α)​Gi​(𝐚)1/2⩾01-\Phi^{-1}(\alpha)G\_{i}(\mathbf{a})^{1/2}\geqslant 0 holds for all a1,a2⩾0a\_{1},a\_{2}\geqslant 0, driving the optimal retention levels to their minimum values.

Next, we assume α1=α2\alpha\_{1}=\alpha\_{2} to facilitate a clearer analysis of the relationship between α\alpha, αi\alpha\_{i}, and the value of the objective function under the optimal strategy.

![Refer to caption](x1.png)


Figure 2:  Value of the objective function under the optimal insurance strategy (left panel) and the benefit of purchasing reinsurance (right panel) for α∈(0.5,1)\alpha\in(0.5,1)

![Refer to caption](x2.png)


Figure 3:  Value of the objective function under the optimal insurance strategy (left panel) and the benefit of purchasing reinsurance (right panel) for αi∈(0.5,1)\alpha\_{i}\in(0.5,1)

As shown in the left panel of Figure [2](https://arxiv.org/html/2512.11430v1#S6.F2 "Figure 2 ‣ 6.1 Effects of dependence and confidence levels ‣ 6 Simulation studies ‣ Pareto-optimal reinsurance under dependence uncertainty"), with fixed α1=α2=0.9\alpha\_{1}=\alpha\_{2}=0.9, the optimal objective value increases with α\alpha. The worst-case scenario consistently yields the highest values, dominating other dependence structures. When α⩾αi\alpha\geqslant\alpha\_{i}, the comonotonic and worst-case results coincide with ∑i=12VaRαi​(Xi)\sum\_{i=1}^{2}\mathrm{VaR}\_{\alpha\_{i}}(X\_{i}), as evidenced in both Figures [2](https://arxiv.org/html/2512.11430v1#S6.F2 "Figure 2 ‣ 6.1 Effects of dependence and confidence levels ‣ 6 Simulation studies ‣ Pareto-optimal reinsurance under dependence uncertainty") and [3](https://arxiv.org/html/2512.11430v1#S6.F3 "Figure 3 ‣ 6.1 Effects of dependence and confidence levels ‣ 6 Simulation studies ‣ Pareto-optimal reinsurance under dependence uncertainty"). For sufficiently small α\alpha, the i.i.d. case may outperform the comonotonic scenario, confirming that comonotonic dependence does not always represent the worst-case outcome for VaR-based optimization.

The right panel of Figure [2](https://arxiv.org/html/2512.11430v1#S6.F2 "Figure 2 ‣ 6.1 Effects of dependence and confidence levels ‣ 6 Simulation studies ‣ Pareto-optimal reinsurance under dependence uncertainty") reveals that the benefit of reinsurance — measured as the reduction in the objective value compared to no reinsurance — decreases with α\alpha. This suggests that the advantage of purchasing reinsurance diminishes when reinsurers employ higher confidence levels. Economically, this aligns with intuition: as reinsurers become more conservative in their risk assessment, the value proposition of reinsurance contracts weakens. Furthermore, when α⩾αi\alpha\geqslant\alpha\_{i}, the optimal objective value coincides with the no-reinsurance case, indicating zero benefit from risk transfer under these parameter conditions.

In Figure [3](https://arxiv.org/html/2512.11430v1#S6.F3 "Figure 3 ‣ 6.1 Effects of dependence and confidence levels ‣ 6 Simulation studies ‣ Pareto-optimal reinsurance under dependence uncertainty"), with fixed α=0.9\alpha=0.9, the left panel demonstrates that the optimal objective value increases with αi\alpha\_{i}. While VaRαi​(Xi)\mathrm{VaR}\_{\alpha\_{i}}(X\_{i}) naturally grows with αi\alpha\_{i}, the reinsurance strategy’s indirect dependence on this parameter warrants further examination of the net benefit. We therefore analyze the difference:

|  |  |  |
| --- | --- | --- |
|  | ∑i=12VaRαi​(gai,bi​(Xi))−VaRα​(∑i=12gai,bi​(Xi)),\displaystyle\sum\_{i=1}^{2}\mathrm{VaR}\_{\alpha\_{i}}(g\_{a\_{i},b\_{i}}(X\_{i}))-\mathrm{VaR}\_{\alpha}\!\left(\sum\_{i=1}^{2}g\_{a\_{i},b\_{i}}(X\_{i})\right), |  |

which quantifies the impovement over the no-reinsurance case. As shown in the right panel, this difference increases with αi\alpha\_{i}, indicating that the value of optimal reinsurance becomes more pronounced as insurers adopt higher confidence levels in their risk assessment.

### 6.2 Effects of distributional assumptions

In Subsection [6.1](https://arxiv.org/html/2512.11430v1#S6.SS1 "6.1 Effects of dependence and confidence levels ‣ 6 Simulation studies ‣ Pareto-optimal reinsurance under dependence uncertainty"), we examined specific examples under the worst-case condition for n=2n=2 given by Proposition [3](https://arxiv.org/html/2512.11430v1#Thmproposition3 "Proposition 3. ‣ 4 Optimal solution to the special case of VaR ‣ Pareto-optimal reinsurance under dependence uncertainty"), where the optimal parameter tt consistently took the value 0. We now extend our analysis to investigate the general behavior of tt and its implications for optimal reinsurance design.

###### Proposition 8.

Let n=2n=2 and G¯1\overline{G}\_{1} be defined by ([12](https://arxiv.org/html/2512.11430v1#S4.E12 "In Proposition 3. ‣ 4 Optimal solution to the special case of VaR ‣ Pareto-optimal reinsurance under dependence uncertainty")). Assume that F1−1F\_{1}^{-1} and F2−1F\_{2}^{-1} are continuous on (0,1)(0,1), and that α⩾α1+α2−1\alpha\geqslant\alpha\_{1}+\alpha\_{2}-1. Then, in the optimization problem

|  |  |  |
| --- | --- | --- |
|  | inf(a1,a2,b1,b2)∈𝒜1inft∈[0,1−α]G¯1​(a1,a2,b1,b2,t),\inf\_{(a\_{1},a\_{2},b\_{1},b\_{2})\in\mathcal{A}\_{1}}\inf\_{t\in[0,1-\alpha]}\overline{G}\_{1}(a\_{1},a\_{2},b\_{1},b\_{2},t), |  |

the optimal value of tt is attained at one of the boundary points: either t∗=0t^{\*}=0 or t∗=1−αt^{\*}=1-\alpha.

###### Proposition 9.

Let n=2n=2 and G¯1\overline{G}\_{1} be defined by ([12](https://arxiv.org/html/2512.11430v1#S4.E12 "In Proposition 3. ‣ 4 Optimal solution to the special case of VaR ‣ Pareto-optimal reinsurance under dependence uncertainty")). Assume that F1−1F\_{1}^{-1} and F2−1F\_{2}^{-1} are continuous on (0,1)(0,1), and 𝐅∈(ℳc​xα)2\mathbf{F}\in\left(\mathcal{M}\_{cx}^{\alpha}\right)^{2}. Then, in the optimization problem

|  |  |  |
| --- | --- | --- |
|  | inf(a1,a2,b1,b2)∈𝒜1inft∈[0,1−α]G¯1​(a1,a2,b1,b2,t),\inf\_{(a\_{1},a\_{2},b\_{1},b\_{2})\in\mathcal{A}\_{1}}\inf\_{t\in[0,1-\alpha]}\overline{G}\_{1}(a\_{1},a\_{2},b\_{1},b\_{2},t), |  |

the optimal value of tt is attained at one of the boundary points: either t∗=0t^{\*}=0 or t∗=1−αt^{\*}=1-\alpha.

Our theoretical analysis establishes that for n=2n=2, the optimal solution reduces to boundary points (t∗=0t^{\*}=0 or t∗=1−αt^{\*}=1-\alpha) under two scenarios: when 𝐅∈(ℳcxα)n\mathbf{F}\in(\mathcal{M}\_{\text{cx}}^{\alpha})^{n}, or when α1+α2⩽1+α\alpha\_{1}+\alpha\_{2}\leqslant 1+\alpha. However, more complex behavior emerges in other parameter configurations.
We consider the case where 𝐅∈(ℳcvα)n\mathbf{F}\in(\mathcal{M}\_{\text{cv}}^{\alpha})^{n} and α1+α2>1+α\alpha\_{1}+\alpha\_{2}>1+\alpha. We generate XiX\_{i} from Pareto distributions with cumulative distribution functions

|  |  |  |
| --- | --- | --- |
|  | FXi​(x)=1−(1+xλi)−βi,F\_{X\_{i}}(x)=1-\left(1+\frac{x}{\lambda\_{i}}\right)^{-\beta\_{i}}, |  |

using parameters (β1,β2)=(9,6)(\beta\_{1},\beta\_{2})=(9,6) and (λ1,λ2)=(8,5)(\lambda\_{1},\lambda\_{2})=(8,5). This specification yields heterogeneous risk profiles with different tail behaviors. We set the confidence level α=0.9\alpha=0.9 and report the corresponding optimal parameters (a1∗,a2∗,t∗)(a^{\*}\_{1},a^{\*}\_{2},t^{\*}) obtained through numerical optimization in Table [2](https://arxiv.org/html/2512.11430v1#S6.T2 "Table 2 ‣ 6.2 Effects of distributional assumptions ‣ 6 Simulation studies ‣ Pareto-optimal reinsurance under dependence uncertainty").

Table 2: Optimal reinsurance parameters under worst-case dependence with high confidence levels (α=0.9\alpha=0.9)

| Case | result | a1∗a\_{1}^{\*} | a2∗a\_{2}^{\*} | t∗t^{\*} |
| --- | --- | --- | --- | --- |
| α1=0.97,α2=0.99\alpha\_{1}=0.97,\penalty 10000\ \alpha\_{2}=0.99 | 6.30226.3022 | [0,2.3324][0,2.3324] | [0,3.9698][0,3.9698] | 0 |
| α1=0.98,α2=0.99\alpha\_{1}=0.98,\penalty 10000\ \alpha\_{2}=0.99 | 6.39446.3944 | [0,3.2103][0,3.2103] | [0,3.1841][0,3.1841] | 0.0520.052 |
| α1=0.99,α2=0.99\alpha\_{1}=0.99,\penalty 10000\ \alpha\_{2}=0.99 | 6.39446.3944 | [0,3.2103][0,3.2103] | [0,3.1841][0,3.1841] | 0.0520.052 |
| α1=0.99,α2=0.98\alpha\_{1}=0.99,\penalty 10000\ \alpha\_{2}=0.98 | 6.39446.3944 | [0,3.2103][0,3.2103] | [0,3.1841][0,3.1841] | 0.0520.052 |
| α1=0.99,α2=0.97\alpha\_{1}=0.99,\penalty 10000\ \alpha\_{2}=0.97 | 6.15036.1503 | [0,3.8113][0,3.8113] | [0,2.3390][0,2.3390] | 0.10000.1000 |

Note:
VaR0.9​(X1)=2.3324\mathrm{VaR}\_{0.9}(X\_{1})=2.3324, VaR0.952​(X1)=3.2103\mathrm{VaR}\_{0.952}(X\_{1})=3.2103, VaR0.99​(X1)=3.8113\mathrm{VaR}\_{0.99}(X\_{1})=3.8113;
VaR0.9​(X2)=2.3390\mathrm{VaR}\_{0.9}(X\_{2})=2.3390, VaR0.948​(X2)=3.1841\mathrm{VaR}\_{0.948}(X\_{2})=3.1841, VaR0.99​(X2)=3.9698\mathrm{VaR}\_{0.99}(X\_{2})=3.9698.
The notation [0,c][0,c] indicates that any retention level in this interval achieves the same optimal objective value, and t∗t^{\*} is related to the optimal value of tt in Proposition [3](https://arxiv.org/html/2512.11430v1#Thmproposition3 "Proposition 3. ‣ 4 Optimal solution to the special case of VaR ‣ Pareto-optimal reinsurance under dependence uncertainty").

Table [2](https://arxiv.org/html/2512.11430v1#S6.T2 "Table 2 ‣ 6.2 Effects of distributional assumptions ‣ 6 Simulation studies ‣ Pareto-optimal reinsurance under dependence uncertainty") reveals that boundary solutions persist even when α1+α2>1+α\alpha\_{1}+\alpha\_{2}>1+\alpha: for (α1,α2)=(0.97,0.99)(\alpha\_{1},\alpha\_{2})=(0.97,0.99) we obtain t∗=0t^{\*}=0, while for (0.99,0.97)(0.99,0.97) we have t∗=1−αt^{\*}=1-\alpha. This demonstrates that the reduction to boundary points is not limited to the theoretical condition α1+α2⩽1+α\alpha\_{1}+\alpha\_{2}\leqslant 1+\alpha.

When both α1\alpha\_{1} and α2\alpha\_{2} are sufficiently large, the optimal retention levels exhibit the structure a1∗∈[0,VaRα+t∗​(X1)]a^{\*}\_{1}\in[0,\mathrm{VaR}\_{\alpha+t^{\*}}(X\_{1})] and a2∗∈[0,VaR1−t∗​(X2)]a^{\*}\_{2}\in[0,\mathrm{VaR}\_{1-t^{\*}}(X\_{2})]. Notably, the optimal solutions for (α1,α2)=(0.98,0.99)(\alpha\_{1},\alpha\_{2})=(0.98,0.99), (0.99,0.99)(0.99,0.99), and (0.99,0.98)(0.99,0.98) are identical. Similar to Proposition [9](https://arxiv.org/html/2512.11430v1#Thmproposition9 "Proposition 9. ‣ 6.2 Effects of distributional assumptions ‣ 6 Simulation studies ‣ Pareto-optimal reinsurance under dependence uncertainty"), the optimal value VaRα+t∗​(X1)+VaR1−t∗​(X2)\mathrm{VaR}\_{\alpha+t^{\*}}(X\_{1})+\mathrm{VaR}\_{1-t^{\*}}(X\_{2}) depends only on t∗t^{\*} and not on the specific values of α1\alpha\_{1} and α2\alpha\_{2}. Consequently, both t∗t^{\*} and the optimal objective value remain unchanged across these configurations, as further illustrated in Figure [3](https://arxiv.org/html/2512.11430v1#S6.F3 "Figure 3 ‣ 6.1 Effects of dependence and confidence levels ‣ 6 Simulation studies ‣ Pareto-optimal reinsurance under dependence uncertainty").
These findings have practical relevance for insurance markets. Insurers, being typically more risk averse, often employ higher confidence levels (e.g., α1,α2=0.99\alpha\_{1},\alpha\_{2}=0.99) compared to reinsurers (e.g., α=0.9\alpha=0.9). This makes the case α1+α2>1+α\alpha\_{1}+\alpha\_{2}>1+\alpha particularly relevant in practice, and our results provide guidance for optimal reinsurance design in such realistic settings.

###### Remark 4.

It is important to emphasize that our preceding analysis focuses specifically on the case n=2n=2 and addresses the optimal insurance problem under the VaR\mathrm{VaR} risk measure. When considering the more general RVaR\mathrm{RVaR}-based optimization, the interplay between RVaRβi,αi​(Xi−fi​(Xi))\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X\_{i}-f\_{i}(X\_{i})) and RVaRγi,γ0​(fi​(Xi))\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(f\_{i}(X\_{i})) introduces additional complexity, necessitating more sophisticated technical treatment.
Consider a simplified setting with 𝐟∈ℐn\mathbf{f}\in\mathcal{I}^{n}, β=0\beta=0, and βi=0\beta\_{i}=0 for i=1,2i=1,2. The optimization problem becomes:

|  |  |  |
| --- | --- | --- |
|  | inf(ai,bi)∈𝒜1[ES1−αi​(Xi)−ES1−αi​(gai,bi​(Xi))+ES1−α​(gai,bi​(Xi))].\displaystyle\inf\_{(a\_{i},b\_{i})\in\mathcal{A}\_{1}}\left[\mathrm{ES}\_{1-\alpha\_{i}}(X\_{i})-\mathrm{ES}\_{1-\alpha\_{i}}(g\_{a\_{i},b\_{i}}(X\_{i}))+\mathrm{ES}\_{1-\alpha}(g\_{a\_{i},b\_{i}}(X\_{i}))\right]. |  |

If α⩽αi\alpha\leqslant\alpha\_{i}, then

|  |  |  |
| --- | --- | --- |
|  | ES1−α​(gai,bi​(Xi))−ES1−αi​(gai,bi​(Xi))⩾0.\displaystyle\mathrm{ES}\_{1-\alpha}(g\_{a\_{i},b\_{i}}(X\_{i}))-\mathrm{ES}\_{1-\alpha\_{i}}(g\_{a\_{i},b\_{i}}(X\_{i}))\geqslant 0. |  |

If α>αi\alpha>\alpha\_{i}, we derive:

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ES1−α​(gai,bi​(Xi))−ES1−αi​(gai,bi​(Xi))\displaystyle\mathrm{ES}\_{1-\alpha}(g\_{a\_{i},b\_{i}}(X\_{i}))-\mathrm{ES}\_{1-\alpha\_{i}}(g\_{a\_{i},b\_{i}}(X\_{i})) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 1α​∫1−α1−αigai,bi​(x)​dFX​(x)−(1αi−1α)​∫1−αi1gai,bi​(x)​dFX​(x)\displaystyle\frac{1}{\alpha}\int\_{1-\alpha}^{1-\alpha\_{i}}g\_{a\_{i},b\_{i}}(x)\mathrm{d}F\_{X}(x)-\left(\frac{1}{\alpha\_{i}}-\frac{1}{\alpha}\right)\int\_{1-\alpha\_{i}}^{1}g\_{a\_{i},b\_{i}}(x)\mathrm{d}F\_{X}(x) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 1α​∫1−α1−αi(gai,bi​(x)−gai,bi​(VaR1−αi​(Xi)))​dFX​(x)\displaystyle\frac{1}{\alpha}\int\_{1-\alpha}^{1-\alpha\_{i}}\left(g\_{a\_{i},b\_{i}}(x)-g\_{a\_{i},b\_{i}}(\mathrm{VaR}\_{1-\alpha\_{i}}(X\_{i}))\right)\mathrm{d}F\_{X}(x) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −(1αi−1α)​∫1−αi1(gai,bi​(x)−gai,bi​(VaR1−αi​(Xi)))​dFX​(x).\displaystyle-\left(\frac{1}{\alpha\_{i}}-\frac{1}{\alpha}\right)\int\_{1-\alpha\_{i}}^{1}\left(g\_{a\_{i},b\_{i}}(x)-g\_{a\_{i},b\_{i}}(\mathrm{VaR}\_{1-\alpha\_{i}}(X\_{i}))\right)\mathrm{d}F\_{X}(x). |  |

Note that for x⩽VaR1−αi​(Xi)x\leqslant\mathrm{VaR}\_{1-\alpha\_{i}}(X\_{i}), we have gai,bi​(x)−gai,bi​(VaR1−αi​(Xi))⩾x−VaR1−αi​(Xi)g\_{a\_{i},b\_{i}}(x)-g\_{a\_{i},b\_{i}}(\mathrm{VaR}\_{1-\alpha\_{i}}(X\_{i}))\geqslant x-\mathrm{VaR}\_{1-\alpha\_{i}}(X\_{i}), and for x⩾VaR1−αi​(Xi)x\geqslant\mathrm{VaR}\_{1-\alpha\_{i}}(X\_{i}), we have gai,bi​(x)−gai,bi​(VaR1−αi​(Xi))⩽x−VaR1−αi​(Xi)g\_{a\_{i},b\_{i}}(x)-g\_{a\_{i},b\_{i}}(\mathrm{VaR}\_{1-\alpha\_{i}}(X\_{i}))\leqslant x-\mathrm{VaR}\_{1-\alpha\_{i}}(X\_{i}).
Therefore, the optimal solution for the ES case is achieved with ai∗⩽VaR1−α​(Xi)a^{\*}\_{i}\leqslant\mathrm{VaR}\_{1-\alpha}(X\_{i}) and bi∗=∞b^{\*}\_{i}=\infty,
which differs from the optimal solution in the VaR\mathrm{VaR} case.

## 7 Conclusion

This paper develops a robust framework for designing Pareto-optimal multilateral reinsurance treaties under dependence uncertainty. Through theoretical analysis and numerical studies, we establish several key insights that advance the understanding of optimal risk sharing in complex insurance markets.

Our main theoretical contribution lies in characterizing the precise structure of Pareto-optimal reinsurance contracts when the dependence between the cedants’ risks is completely unknown. Under the robust RVaR framework (Theorem [1](https://arxiv.org/html/2512.11430v1#Thmtheorem1 "Theorem 1. ‣ 3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty")), the originally infinite-dimensional optimization problem can be reduced to a tractable finite-dimensional one. Optimal indemnities take distinctive parametric forms, including layered contracts ga,bg\_{a,b} that cover losses exceeding a retention level aa but are capped at bb, and hybrid contracts ra,b,cr\_{a,b,c} that combine proportional and excess-of-loss coverage. These structures allow explicit control over the retained proportion of losses and additional protection above specified thresholds.

For the special case of VaR objectives (Theorem [2](https://arxiv.org/html/2512.11430v1#Thmtheorem2 "Theorem 2. ‣ 4 Optimal solution to the special case of VaR ‣ Pareto-optimal reinsurance under dependence uncertainty")), optimal indemnity functions exhibit layer structures whose forms depend on the convexity properties of marginal distributions. When distributions belong to ℳc​xα\mathcal{M}\_{cx}^{\alpha} or ℳc​vα\mathcal{M}\_{cv}^{\alpha}, we obtain even more explicit characterizations: the capped proportional contracts la,bl\_{a,b} generalize quota-share arrangements, and the shifted excess-of-loss contracts ha,bh\_{a,b} include stop loss or quota share as special cases. The asymptotic analysis (Theorems [3](https://arxiv.org/html/2512.11430v1#Thmtheorem3 "Theorem 3. ‣ 5.1 The results for RVaR ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty") and [4](https://arxiv.org/html/2512.11430v1#Thmtheorem4 "Theorem 4. ‣ 5.2 The result for VaR ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty")) further demonstrates that as the number of cedants grows, optimal contracts converge to layered structures, represented by ga,bg\_{a,b}.

Our simulation studies highlight several practical patterns. First, the relationship between dependence and optimal outcomes is nuanced: while the worst-case dependence consistently produces conservative outcomes, comonotonicity does not always yield the maximal VaR, and i.i.d. scenarios can sometimes generate larger objective values depending on parameter configurations. Second, the value of reinsurance is highly sensitive to confidence levels: higher α\alpha in the reinsurer’s assessment reduces the marginal benefit of reinsurance, and higher confidence levels among cedants amplify the advantage of optimal contracts.

Finally, while our analysis assumes exogenously set premiums, a natural extension is to study premium-dependent strategies, in which optimal contracts interact with pricing decisions. Exploring this interaction will be critical for understanding the full economic implications of Pareto-optimal reinsurance design in practice.

### Acknowledgments

The authors are grateful to Yiying Zhang for his helpful comments. Xia Han is supported by the National Natural Science Foundation of China (Grant Nos. 12301604, 12371471, and 12471449).

### Declaration of Interest statements

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this article.

## Appendix A Proofs of Section [2](https://arxiv.org/html/2512.11430v1#S2 "2 Model description and notation ‣ Pareto-optimal reinsurance under dependence uncertainty")

###### Proof of Proposition [1](https://arxiv.org/html/2512.11430v1#Thmproposition1 "Proposition 1. ‣ 2 Model description and notation ‣ Pareto-optimal reinsurance under dependence uncertainty").

We first show the “if” part by contradiction. Assume that there exists a contract (𝐟,𝝅)∈ℐn×ℝn(\mathbf{f},\boldsymbol{\pi})\in\mathcal{I}^{n}\times\mathbb{R}^{n} that solves inf𝐟∈ℐnV​(𝐟),\inf\_{\mathbf{f}\in\mathcal{I}^{n}}V(\mathbf{f}), but is not robust Pareto-optimal. This means that there exists (𝐟^,𝝅^)∈ℐn×ℝn(\hat{\mathbf{f}},\hat{\boldsymbol{\pi}})\in\mathcal{I}^{n}\times\mathbb{R}^{n} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | RVaRβi,αi​(Tfi,πi​(Xi))\displaystyle\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(T\_{f\_{i},\pi\_{i}}(X\_{i})\right) | ⩾RVaRβi,αi​(Tf^i,π^i​(Xi)), for all ​i∈[n],\displaystyle\geqslant\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(T\_{\hat{f}\_{i},\hat{\pi}\_{i}}(X\_{i})\right),\text{ for all }i\in[n], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | sup𝐗∈ℰn​(𝐅)RVaRβ,α​(R𝐟,𝝅​(𝐗))\displaystyle\sup\_{\mathbf{X}\in\mathcal{E}\_{n}(\mathbf{F})}\mathrm{RVaR}\_{\beta,\alpha}\left(R\_{\mathbf{f},\boldsymbol{\pi}}(\mathbf{X})\right) | ⩾sup𝐗∈ℰn​(𝐅)RVaRβ,α​(R𝐟^,𝝅^​(𝐗)),\displaystyle\geqslant\sup\_{\mathbf{X}\in\mathcal{E}\_{n}(\mathbf{F})}\mathrm{RVaR}\_{\beta,\alpha}\left(R\_{\hat{\mathbf{f}},\hat{\boldsymbol{\pi}}}(\mathbf{X})\right), |  |

with at least one strict inequality. It follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∑i=1nRVaRβi,αi​(Tfi,πi​(Xi))+sup𝐗∈ℰn​(𝐅)RVaRβ,α​(R𝐟,𝝅​(𝐗))\displaystyle\sum\_{i=1}^{n}\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(T\_{f\_{i},\pi\_{i}}(X\_{i})\right)+\sup\_{\mathbf{X}\in\mathcal{E}\_{n}(\mathbf{F})}\mathrm{RVaR}\_{\beta,\alpha}\left(R\_{\mathbf{f},\boldsymbol{\pi}}(\mathbf{X})\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | >∑i=1nRVaRβi,αi​(Tf^i,π^i​(Xi))+sup𝐗∈ℰn​(𝐅)RVaRβ,α​(R𝐟^,𝝅^​(𝐗)),\displaystyle>\sum\_{i=1}^{n}\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(T\_{\hat{f}\_{i},\hat{\pi}\_{i}}(X\_{i})\right)+\sup\_{\mathbf{X}\in\mathcal{E}\_{n}(\mathbf{F})}\mathrm{RVaR}\_{\beta,\alpha}\left(R\_{\hat{\mathbf{f}},\hat{\boldsymbol{\pi}}}(\mathbf{X})\right), |  |

which contradicts the assumption that 𝐟∈arg​inf𝐟∈ℐnV​(𝐟).\mathbf{f}\in\arg\inf\_{\mathbf{f}\in\mathcal{I}^{n}}V(\mathbf{f}). Hence, the “if” part holds.

To show the “only if” part, assume, by way of contradiction, that there exists a robust Pareto-optimal contract (𝐟∗,𝝅∗)∈ℐn×ℝn(\mathbf{f}^{\*},\boldsymbol{\pi}^{\*})\in\mathcal{I}^{n}\times\mathbb{R}^{n} such that 𝐟∗∉arg​inf𝐟∈ℐnV​(𝐟).\mathbf{f}^{\*}\notin\arg\inf\_{\mathbf{f}\in\mathcal{I}^{n}}V(\mathbf{f}). Then, there exists (𝐟~,𝝅~)∈ℐn×ℝn(\widetilde{\mathbf{f}},\widetilde{\boldsymbol{\pi}})\in\mathcal{I}^{n}\times\mathbb{R}^{n} such that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ∑i=1nRVaRβi,αi​(Tf~i,π~i​(Xi))+sup𝐗∈ℰn​(𝐅)RVaRβ,α​(R𝐟~,𝝅~​(𝐗))\displaystyle\;\sum\_{i=1}^{n}\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(T\_{\widetilde{f}\_{i},\widetilde{\pi}\_{i}}(X\_{i})\right)+\sup\_{\mathbf{X}\in\mathcal{E}\_{n}(\mathbf{F})}\mathrm{RVaR}\_{\beta,\alpha}\left(R\_{\widetilde{\mathbf{f}},\widetilde{\boldsymbol{\pi}}}(\mathbf{X})\right) |  | (22) |
|  |  | <∑i=1nRVaRβi,αi​(Tfi∗,πi∗​(Xi))+sup𝐗∈ℰn​(𝐅)RVaRβ,α​(R𝐟∗,𝝅∗​(𝐗)).\displaystyle<\sum\_{i=1}^{n}\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(T\_{f\_{i}^{\*},\pi\_{i}^{\*}}(X\_{i})\right)+\sup\_{\mathbf{X}\in\mathcal{E}\_{n}(\mathbf{F})}\mathrm{RVaR}\_{\beta,\alpha}\left(R\_{\mathbf{f}^{\*},\boldsymbol{\pi}^{\*}}(\mathbf{X})\right). |  |

Define, for i∈[n],i\in[n],

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | π^i:\displaystyle\hat{\pi}\_{i}: | =π~i+(RVaRβi,αi​(Tfi∗,πi∗​(Xi))−RVaRβi,αi​(Tf~i,π~i​(Xi)))\displaystyle=\;\widetilde{\pi}\_{i}+\left(\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(T\_{f\_{i}^{\*},\pi\_{i}^{\*}}(X\_{i})\right)-\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(T\_{\widetilde{f}\_{i},\widetilde{\pi}\_{i}}(X\_{i})\right)\right) |  | (23) |
|  |  | =RVaRβi,αi​(f~i​(Xi))−RVaRβi,αi​(fi∗​(Xi))+πi∗.\displaystyle=\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(\widetilde{f}\_{i}(X\_{i})\right)-\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(f\_{i}^{\*}(X\_{i})\right)+\pi^{\*}\_{i}. |  |

Note that (𝐟~,𝝅^)∈ℐn×ℝn.(\widetilde{\mathbf{f}},\hat{\boldsymbol{\pi}})\in\mathcal{I}^{n}\times\mathbb{R}^{n}. By ([23](https://arxiv.org/html/2512.11430v1#A1.E23 "In Appendix A Proofs of Section 2 ‣ Pareto-optimal reinsurance under dependence uncertainty")) and cash additivity of RVaRβi,αi\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}},111For c∈ℝc\in\mathbb{R}, RVaRβi,αi​(X+c)=RVaRβi,αi​(X)+c\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X+c)=\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X)+c holds for all X∈L1X\in L^{1}.  we have, for i∈[n],i\in[n],

|  |  |  |
| --- | --- | --- |
|  | RVaRβi,αi​(Tf~i,π^i​(Xi))=RVaRβi,αi​(Tfi∗,πi∗​(Xi)).\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(T\_{\widetilde{f}\_{i},\hat{\pi}\_{i}}(X\_{i})\right)=\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(T\_{f\_{i}^{\*},\pi\_{i}^{\*}}(X\_{i})\right). |  |

Moreover, it follows from ([22](https://arxiv.org/html/2512.11430v1#A1.E22 "In Appendix A Proofs of Section 2 ‣ Pareto-optimal reinsurance under dependence uncertainty")), ([23](https://arxiv.org/html/2512.11430v1#A1.E23 "In Appendix A Proofs of Section 2 ‣ Pareto-optimal reinsurance under dependence uncertainty")), and cash additivity of RVaRβ,α\mathrm{RVaR}\_{\beta,\alpha} that

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup𝐗∈ℰn​(𝐅)RVaRβ,α​(R𝐟~,𝝅^​(𝐗))\displaystyle\sup\_{\mathbf{X}\in\mathcal{E}\_{n}(\mathbf{F})}\mathrm{RVaR}\_{\beta,\alpha}\left(R\_{\widetilde{\mathbf{f}},\hat{\boldsymbol{\pi}}}(\mathbf{X})\right) | =sup𝐗∈ℰn​(𝐅)RVaRβ,α​(R𝐟~,𝝅~​(𝐗))+∑i=1nRVaRβi,αi​(Tf~i,π~i​(Xi))\displaystyle=\sup\_{\mathbf{X}\in\mathcal{E}\_{n}(\mathbf{F})}\mathrm{RVaR}\_{\beta,\alpha}\left(R\_{\widetilde{\mathbf{f}},\widetilde{\boldsymbol{\pi}}}(\mathbf{X})\right)+\sum\_{i=1}^{n}\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(T\_{\widetilde{f}\_{i},\widetilde{\pi}\_{i}}(X\_{i})\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∑i=1nRVaRβi,αi​(Tfi∗,πi∗​(Xi))\displaystyle\qquad-\sum\_{i=1}^{n}\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(T\_{f\_{i}^{\*},\pi\_{i}^{\*}}(X\_{i})\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | <sup𝐗∈ℰn​(𝐅)RVaRβ,α​(R𝐟∗,𝝅∗​(𝐗)).\displaystyle<\sup\_{\mathbf{X}\in\mathcal{E}\_{n}(\mathbf{F})}\mathrm{RVaR}\_{\beta,\alpha}\left(R\_{\mathbf{f}^{\*},\boldsymbol{\pi}^{\*}}(\mathbf{X})\right). |  |

This contradicts the fact that (𝐟∗,𝝅∗)∈ℐn×ℝn(\mathbf{f}^{\*},\boldsymbol{\pi}^{\*})\in\mathcal{I}^{n}\times\mathbb{R}^{n} is Pareto optimal.
Hence, the “only if” part holds. This completes the proof.
∎

## Appendix B Proofs of Section [3](https://arxiv.org/html/2512.11430v1#S3 "3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty")

###### Proof of Theorem [1](https://arxiv.org/html/2512.11430v1#Thmtheorem1 "Theorem 1. ‣ 3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty").

(i)
If β=0,\beta=0, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | sup𝐗∈ℰn​(𝐅)RVaRβ,α​(∑i=1nfi​(Xi))\displaystyle\sup\_{\mathbf{X}\in\mathcal{E}\_{n}(\mathbf{F})}\mathrm{RVaR}\_{\beta,\alpha}\left(\sum\_{i=1}^{n}f\_{i}(X\_{i})\right) | =sup𝐗∈ℰn​(𝐅)ES1−α​(∑i=1nfi​(Xi))\displaystyle=\sup\_{\mathbf{X}\in\mathcal{E}\_{n}(\mathbf{F})}\mathrm{ES}\_{1-\alpha}\left(\sum\_{i=1}^{n}f\_{i}(X\_{i})\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑i=1nES1−α​(fi​(Xi)).\displaystyle=\sum\_{i=1}^{n}\mathrm{ES}\_{1-\alpha}(f\_{i}(X\_{i})). |  |

The second equality holds because ES is subadditive222For α∈(0,1]\alpha\in(0,1], ES1−α​(X+Y)⩽ES1−α​(X)+ES1−α​(Y)\mathrm{ES}\_{1-\alpha}(X+Y)\leqslant\mathrm{ES}\_{1-\alpha}(X)+\mathrm{ES}\_{1-\alpha}(Y) holds for all X,Y∈L1X,Y\in L^{1}.  and is maximized under the comonotonic dependence structure.
Thus, the optimization problem ([3](https://arxiv.org/html/2512.11430v1#S3.E3 "In 3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty")) can be written as

|  |  |  |
| --- | --- | --- |
|  | inf𝐟∈ℐn∑i=1n{RVaRβi,αi​(Xi)−RVaRβi,αi​(fi​(Xi))+ES1−α​(fi​(Xi))}.\displaystyle\inf\_{\mathbf{f}\in\mathcal{I}^{n}}\sum\_{i=1}^{n}\left\{\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X\_{i})-\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(f\_{i}(X\_{i})\right)+\mathrm{ES}\_{1-\alpha}(f\_{i}(X\_{i}))\right\}. |  |

By definition, every strategy 𝐠𝐚,𝐛{\bf g}\_{{\bf a},{\bf b}} with (𝐚,𝐛)∈𝒜1({\bf a},{\bf b})\in\mathcal{A}\_{1} belongs to ℐn\mathcal{I}^{n}. Hence, restricting the infimum over ℐn\mathcal{I}^{n} to this subset yields

|  |  |  |
| --- | --- | --- |
|  | inf𝐟∈ℐnV​(𝐟)⩽inf(𝐚,𝐛)∈𝒜1V​(𝐠𝐚,𝐛)=inf(𝐚,𝐛)∈𝒜1G​(𝐚,𝐛).\inf\_{\mathbf{f}\in\mathcal{I}^{n}}V(\mathbf{f})\leqslant\inf\_{({\bf a},{\bf b})\in\mathcal{A}\_{1}}V({\bf g}\_{{\bf a},{\bf b}})=\inf\_{({\bf a},{\bf b})\in\mathcal{A}\_{1}}G({\bf a},{\bf b}). |  |

For ease of notation, define α¯i=1−βi−αi,\bar{\alpha}\_{i}=1-\beta\_{i}-\alpha\_{i}, β¯i=1−βi\bar{\beta}\_{i}=1-\beta\_{i} and α¯=1−α.\bar{\alpha}=1-\alpha. Next, we explore the optimal indemnity functions under the following three cases (see Figure [4](https://arxiv.org/html/2512.11430v1#A2.F4 "Figure 4 ‣ Appendix B Proofs of Section 3 ‣ Pareto-optimal reinsurance under dependence uncertainty")).

![Refer to caption](x3.png)


Figure 4:  Three parameter orderings and corresponding gai,big\_{a\_{i},b\_{i}}

Let

|  |  |  |
| --- | --- | --- |
|  | ai=VaRα¯i​(Xi)−fi​(VaRα¯i​(Xi)),VaRα¯i​(Xi)⩽bi⩽VaRβ¯i​(Xi)a\_{i}=\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i})-f\_{i}(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i})),\quad\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i})\leqslant b\_{i}\leqslant\mathrm{VaR}\_{\bar{\beta}\_{i}}(X\_{i}) |  |

be such that

|  |  |  |
| --- | --- | --- |
|  | RVaRβi,αi​(gai,bi​(Xi))=RVaRβi,αi​(fi​(Xi)).\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\bigl(g\_{a\_{i},b\_{i}}(X\_{i})\bigr)=\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\bigl(f\_{i}(X\_{i})\bigr). |  |

The existence of such bib\_{i} is ensured by the continuity of the mapping

|  |  |  |
| --- | --- | --- |
|  | t↦RVaRβi,αi​(gai,t​(Xi)),t∈[VaRα¯i​(Xi),VaRβ¯i​(Xi)],t\mapsto\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\bigl(g\_{a\_{i},t}(X\_{i})\bigr),\quad t\in[\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i}),\mathrm{VaR}\_{\bar{\beta}\_{i}}(X\_{i})], |  |

together with the intermediate-value property

|  |  |  |
| --- | --- | --- |
|  | RVaRβi,αi​(gai,VaRα¯i​(Xi)​(Xi))⩽RVaRβi,αi​(fi​(Xi))⩽RVaRβi,αi​(gai,VaRβ¯i​(Xi)​(Xi)).\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\bigl(g\_{a\_{i},\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i})}(X\_{i})\bigr)\leqslant\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\bigl(f\_{i}(X\_{i})\bigr)\leqslant\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\bigl(g\_{a\_{i},\mathrm{VaR}\_{\bar{\beta}\_{i}}(X\_{i})}(X\_{i})\bigr). |  |

Case (1): α¯⩽α¯i<β¯i.\bar{\alpha}\leqslant\bar{\alpha}\_{i}<\bar{\beta}\_{i}.
With the predefined ai,bi,a\_{i},b\_{i}, we have gai,bi​(x)⩽fi​(x)g\_{a\_{i},b\_{i}}(x)\leqslant f\_{i}(x) for x⩽VaRα¯i​(Xi)x\leqslant\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i}) and x⩾VaRβ¯i​(Xi).x\geqslant\mathrm{VaR}\_{\bar{\beta}\_{i}}(X\_{i}). Hence, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESα¯​(gai,bi​(Xi))\displaystyle\mathrm{ES}\_{\bar{\alpha}}(g\_{a\_{i},b\_{i}}(X\_{i})) | =1α​(∫[α¯,α¯i]∪[β¯i,1]gai,bi​(VaRt​(Xi))​dt+αi​RVaRβi,αi​(gai,bi​(Xi)))\displaystyle=\frac{1}{\alpha}\left(\int\_{[\bar{\alpha},\bar{\alpha}\_{i}]\cup[\bar{\beta}\_{i},1]}g\_{a\_{i},b\_{i}}(\mathrm{VaR}\_{t}(X\_{i}))\mathrm{d}t+\alpha\_{i}\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(g\_{a\_{i},b\_{i}}(X\_{i}))\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⩽1α​(∫[α¯,α¯i]∪[β¯i,1]fi​(VaRt​(Xi))​dt+αi​RVaRβi,αi​(fi​(Xi)))\displaystyle\leqslant\frac{1}{\alpha}\left(\int\_{[\bar{\alpha},\bar{\alpha}\_{i}]\cup[\bar{\beta}\_{i},1]}f\_{i}(\mathrm{VaR}\_{t}(X\_{i}))\mathrm{d}t+\alpha\_{i}\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(f\_{i}(X\_{i}))\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ESα¯​(fi​(X)).\displaystyle=\mathrm{ES}\_{\bar{\alpha}}(f\_{i}(X)). |  |

This implies that for any fi∈ℐ,f\_{i}\in\mathcal{I}, we can always find gai,bi∈ℐg\_{a\_{i},b\_{i}}\in\mathcal{I} that is better than fi.f\_{i}.

Case (2): α¯i<α¯<β¯i.\bar{\alpha}\_{i}<\bar{\alpha}<\bar{\beta}\_{i}. By the construction of aia\_{i} and bi,b\_{i}, there exists VaRα¯i​(Xi)⩽x¯i⩽VaRβ¯i​(Xi)\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i})\leqslant\bar{x}\_{i}\leqslant\mathrm{VaR}\_{\bar{\beta}\_{i}}(X\_{i}) such that
gai,bi​(x)⩾fi​(x)g\_{a\_{i},b\_{i}}(x)\geqslant f\_{i}(x) for x∈[VaRα¯i​(Xi),x¯i]x\in[\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i}),\bar{x}\_{i}] and gai,bi​(x)⩽fi​(x)g\_{a\_{i},b\_{i}}(x)\leqslant f\_{i}(x) for x⩾x¯i.x\geqslant\bar{x}\_{i}. Hence, RVaRβi,αi​(gai,bi​(Xi))=RVaRβi,αi​(fi​(Xi))\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(g\_{a\_{i},b\_{i}}(X\_{i}))=\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(f\_{i}(X\_{i})) implies

|  |  |  |
| --- | --- | --- |
|  | ∫[α¯,β¯i]gai,bi​(VaRt​(Xi))​dt⩽∫[α¯,β¯i]fi​(VaRt​(Xi))​dt,\int\_{[\bar{\alpha},\bar{\beta}\_{i}]}g\_{a\_{i},b\_{i}}(\mathrm{VaR}\_{t}(X\_{i}))\mathrm{d}t\leqslant\int\_{[\bar{\alpha},\bar{\beta}\_{i}]}f\_{i}(\mathrm{VaR}\_{t}(X\_{i}))\mathrm{d}t, |  |

which further implies ESα¯​(gai,bi​(Xi))⩽ESα¯​(fi​(X)).\mathrm{ES}\_{\bar{\alpha}}(g\_{a\_{i},b\_{i}}(X\_{i}))\leqslant\mathrm{ES}\_{\bar{\alpha}}(f\_{i}(X)). Therefore, for any fi∈ℐ,f\_{i}\in\mathcal{I}, there always exists gai,bi∈ℐg\_{a\_{i},b\_{i}}\in\mathcal{I} such that it is better than fi.f\_{i}.

Case (3): α¯i<β¯i⩽α¯.\bar{\alpha}\_{i}<\bar{\beta}\_{i}\leqslant\bar{\alpha}. In this case, it is obvious that ESα¯​(gai,bi​(Xi))⩽ESα¯​(fi​(X)).\mathrm{ES}\_{\bar{\alpha}}(g\_{a\_{i},b\_{i}}(X\_{i}))\leqslant\mathrm{ES}\_{\bar{\alpha}}(f\_{i}(X)). Therefore, for any fi∈ℐ,f\_{i}\in\mathcal{I}, there always exists gai,bi∈ℐg\_{a\_{i},b\_{i}}\in\mathcal{I} such that it is better than fi∈ℐ.f\_{i}\in\mathcal{I}.

To summarize the three cases, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | inf𝐟∈ℐnV​(𝐟)\displaystyle\inf\_{{\bf f}\in\mathcal{I}^{n}}V(\mathbf{f}) | ⩾inf(𝐚,𝐛)∈𝒜1G​(𝐚,𝐛).\displaystyle\geqslant\inf\_{({\bf a},{\bf b})\in\mathcal{A}\_{1}}G({\bf a},{\bf b}). |  |

We obtain the desired result for (i).

(ii)
Let fi∈ℐf\_{i}\in\mathcal{I} be convex, and consider XiX\_{i} with FXi∈ℳc​v1−β−αF\_{X\_{i}}\in\mathcal{M}\_{cv}^{1-\beta-\alpha}.
To show Ffi​(Xi)∈ℳc​v1−β−αF\_{f\_{i}(X\_{i})}\in\mathcal{M}\_{cv}^{1-\beta-\alpha}, take any y1,y2⩾fi​(F+−1​(1−β−α))y\_{1},y\_{2}\geqslant f\_{i}(F\_{+}^{-1}(1-\beta-\alpha)) with y1⩽y2y\_{1}\leqslant y\_{2}, and let x1=fi−1​(y1)x\_{1}=f\_{i}^{-1}(y\_{1}), x2=fi−1​(y2)x\_{2}=f\_{i}^{-1}(y\_{2}).
By the monotonicity of fif\_{i}, the preimage of the interval [y1,y2][y\_{1},y\_{2}] lies in [x1,x2][x\_{1},x\_{2}].
Then, for any λ∈(0,1)\lambda\in(0,1), by the convexity of fif\_{i},

|  |  |  |
| --- | --- | --- |
|  | fi​(λ​x1+(1−λ)​x2)⩽λ​fi​(x1)+(1−λ)​fi​(x2)=λ​y1+(1−λ)​y2,f\_{i}(\lambda x\_{1}+(1-\lambda)x\_{2})\leqslant\lambda f\_{i}(x\_{1})+(1-\lambda)f\_{i}(x\_{2})=\lambda y\_{1}+(1-\lambda)y\_{2}, |  |

which implies

|  |  |  |
| --- | --- | --- |
|  | fi−1​(λ​y1+(1−λ)​y2)⩾λ​x1+(1−λ)​x2.f\_{i}^{-1}(\lambda y\_{1}+(1-\lambda)y\_{2})\geqslant\lambda x\_{1}+(1-\lambda)x\_{2}. |  |

Since FXi∈ℳc​v1−β−αF\_{X\_{i}}\in\mathcal{M}\_{cv}^{1-\beta-\alpha}, for x1,x2⩾F+−1​(1−β−α)x\_{1},x\_{2}\geqslant F\_{+}^{-1}(1-\beta-\alpha) we have

|  |  |  |
| --- | --- | --- |
|  | FXi​(λ​x1+(1−λ)​x2)⩾λ​FXi​(x1)+(1−λ)​FXi​(x2).F\_{X\_{i}}(\lambda x\_{1}+(1-\lambda)x\_{2})\geqslant\lambda F\_{X\_{i}}(x\_{1})+(1-\lambda)F\_{X\_{i}}(x\_{2}). |  |

Combining the above inequalities and using monotonicity of fif\_{i}, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ffi​(Xi)​(λ​y1+(1−λ)​y2)\displaystyle F\_{f\_{i}(X\_{i})}(\lambda y\_{1}+(1-\lambda)y\_{2}) | =FXi​(fi−1​(λ​y1+(1−λ)​y2))\displaystyle=F\_{X\_{i}}(f\_{i}^{-1}(\lambda y\_{1}+(1-\lambda)y\_{2})) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⩾FXi​(λ​x1+(1−λ)​x2)\displaystyle\geqslant F\_{X\_{i}}(\lambda x\_{1}+(1-\lambda)x\_{2}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⩾λ​FXi​(x1)+(1−λ)​FXi​(x2)\displaystyle\geqslant\lambda F\_{X\_{i}}(x\_{1})+(1-\lambda)F\_{X\_{i}}(x\_{2}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =λ​Ffi​(Xi)​(y1)+(1−λ)​Ffi​(Xi)​(y2),\displaystyle=\lambda F\_{f\_{i}(X\_{i})}(y\_{1})+(1-\lambda)F\_{f\_{i}(X\_{i})}(y\_{2}), |  |

which proves that Ffi​(Xi)∈ℳc​v1−β−αF\_{f\_{i}(X\_{i})}\in\mathcal{M}\_{cv}^{1-\beta-\alpha}.

Hence, in light of Lemma [1](https://arxiv.org/html/2512.11430v1#Thmlemma1 "Lemma 1. ‣ 3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty"), the optimization problem ([3](https://arxiv.org/html/2512.11430v1#S3.E3 "In 3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty")) becomes

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | inf𝐟∈ℐc​xninf𝜸∈(β+α)​Δn,γ0⩾α{∑i=1nRVaRβi,αi​(Tfi​(Xi))+∑i=1nRVaRγi,γ0​(fi​(Xi))}\displaystyle\inf\_{\mathbf{f}\in\mathcal{I}\_{cx}^{n}}\inf\_{\boldsymbol{\gamma}\in(\beta+\alpha)\Delta\_{n},\gamma\_{0}\geqslant\alpha}\left\{\sum\_{i=1}^{n}\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(T\_{f\_{i}}(X\_{i})\right)+\sum\_{i=1}^{n}\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(f\_{i}(X\_{i}))\right\} |  | (24) |
|  | =\displaystyle= | inf𝜸∈(β+α)​Δn,γ0⩾αinf𝐟∈ℐc​xn∑i=1n{RVaRβi,αi​(Xi)−RVaRβi,αi​(fi​(Xi))+RVaRγi,γ0​(fi​(Xi))}.\displaystyle\inf\_{\boldsymbol{\gamma}\in(\beta+\alpha)\Delta\_{n},\gamma\_{0}\geqslant\alpha}\inf\_{\mathbf{f}\in\mathcal{I}\_{cx}^{n}}\sum\_{i=1}^{n}\left\{\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X\_{i})-\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(f\_{i}(X\_{i})\right)+\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(f\_{i}(X\_{i}))\right\}. |  |

By a proof similar to Theorem [1](https://arxiv.org/html/2512.11430v1#Thmtheorem1 "Theorem 1. ‣ 3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty") (i), we have

|  |  |  |
| --- | --- | --- |
|  | inf𝐟∈ℐc​xnV​(𝐟)⩽inf(𝐚,𝐛,𝐜)∈𝒜2inf𝜸∈(β+α)​Δn,γ0⩾αR​(𝐚,𝐛,𝐜,𝜸).\displaystyle\inf\_{{\bf f}\in\mathcal{I}\_{cx}^{n}}V(\mathbf{f})\leqslant\inf\_{({\bf a},{\bf b},{\bf c})\in\mathcal{A}\_{2}}\inf\_{\boldsymbol{\gamma}\in(\beta+\alpha)\Delta\_{n},\gamma\_{0}\geqslant\alpha}R({\bf a},{\bf b},{\bf c},\boldsymbol{\gamma}). |  |

Let γ¯0=1−γ0−γi\bar{\gamma}\_{0}=1-\gamma\_{0}-\gamma\_{i} and γ¯i=1−γi.\bar{\gamma}\_{i}=1-\gamma\_{i}. We need to show the inverse inequality for ([24](https://arxiv.org/html/2512.11430v1#A2.E24 "In Appendix B Proofs of Section 3 ‣ Pareto-optimal reinsurance under dependence uncertainty")) under the following six cases (see Figure [5](https://arxiv.org/html/2512.11430v1#A2.F5 "Figure 5 ‣ Appendix B Proofs of Section 3 ‣ Pareto-optimal reinsurance under dependence uncertainty")).

![Refer to caption](x4.png)


Figure 5: Six parameter orderings and corresponding rai,bi,cir\_{a\_{i},b\_{i},c\_{i}}, each outperforming convex indemnities.

Case (1): α¯i<β¯i⩽γ¯0<γ¯i\bar{\alpha}\_{i}<\bar{\beta}\_{i}\leqslant\bar{\gamma}\_{0}<\bar{\gamma}\_{i}.
In this case, we have RVaRβi,αi​(fi​(Xi))⩽RVaRγi,γ0​(fi​(Xi))\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(f\_{i}(X\_{i})\right)\leqslant\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(f\_{i}(X\_{i})) for any fi∈ℐc​x.f\_{i}\in\mathcal{I}\_{cx}. Thus we have RVaRγi,γ0​(fi​(Xi))−RVaRβi,αi​(fi​(Xi))⩾0\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(f\_{i}(X\_{i}))-\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(f\_{i}(X\_{i})\right)\geqslant 0, which implies that r0,0,0∈ℐc​xr\_{0,0,0}\in\mathcal{I}\_{cx} always performs better than fi.f\_{i}.

Case (2): γ¯0<γ¯i⩽α¯i<β¯i\bar{\gamma}\_{0}<\bar{\gamma}\_{i}\leqslant\bar{\alpha}\_{i}<\bar{\beta}\_{i}.
Define ai=0a\_{i}=0, bi=x¯ib\_{i}=\bar{x}\_{i} and ci=1,c\_{i}=1, where VaRα¯i​(Xi)−fi​(VaRα¯i​(Xi))⩽x¯i⩽VaRβ¯i​(Xi),\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i})-f\_{i}(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i}))\leqslant\bar{x}\_{i}\leqslant\mathrm{VaR}\_{\bar{\beta}\_{i}}(X\_{i}), such that RVaRβi,αi​(rai,bi,ci​(Xi))=RVaRβi,αi​(fi​(Xi)).\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i}))=\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(f\_{i}(X\_{i})). The existence of such x¯i\bar{x}\_{i} is guaranteed by the continuity of RVaRβi,αi​(rai,t,ci​(Xi))\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(r\_{a\_{i},t,c\_{i}}(X\_{i})) for t∈[VaRα¯i​(Xi)−fi​(VaRα¯i​(Xi)),VaRβ¯i​(Xi)]t\in[\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i})-f\_{i}(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i})),\mathrm{VaR}\_{\bar{\beta}\_{i}}(X\_{i})] and the fact that

|  |  |  |
| --- | --- | --- |
|  | RVaRβi,αi​(rai,VaRβ¯i​(Xi),ci​(Xi))⩽RVaRβi,αi​(fi​(Xi))⩽RVaRβi,αi​(rai,VaRα¯i​(Xi)−fi​(VaRα¯i​(Xi)),ci​(Xi)).\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(r\_{a\_{i},\mathrm{VaR}\_{\bar{\beta}\_{i}}(X\_{i}),c\_{i}}(X\_{i}))\leqslant\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(f\_{i}(X\_{i}))\leqslant\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(r\_{a\_{i},\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i})-f\_{i}(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i})),c\_{i}}(X\_{i})). |  |

The convexity of fif\_{i} implies that rai,bi,ci​(x)⩽fi​(x)r\_{a\_{i},b\_{i},c\_{i}}(x)\leqslant f\_{i}(x) for x⩽x¯.x\leqslant\bar{x}. Hence, we have RVaRγi,γ0​(rai,bi,ci​(Xi))⩽RVaRγi,γ0​(fi​(Xi)),\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i}))\leqslant\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(f\_{i}(X\_{i})), which implies RVaRγi,γ0​(fi​(Xi))−RVaRβi,αi​(fi​(Xi))⩾RVaRγi,γ0​(rai,bi,ci​(Xi))−RVaRβi,αi​(rai,bi,ci​(Xi)).\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(f\_{i}(X\_{i}))-\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(f\_{i}(X\_{i})\right)\geqslant\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i}))-\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i})\right).

Case (3): γ¯0⩽α¯i<β¯i⩽γ¯i\bar{\gamma}\_{0}\leqslant\bar{\alpha}\_{i}<\bar{\beta}\_{i}\leqslant\bar{\gamma}\_{i}.
Let

|  |  |  |
| --- | --- | --- |
|  | k1​i=fi​(VaRβ¯i​(Xi))−fi​(VaRα¯i​(Xi))VaRβ¯i​(Xi)−VaRα¯i​(Xi),k\_{1i}=\frac{f\_{i}(\mathrm{VaR}\_{\bar{\beta}\_{i}}(X\_{i}))-f\_{i}(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i}))}{\mathrm{VaR}\_{\bar{\beta}\_{i}}(X\_{i})-\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i})}, |  |

with the convention that 00=0.\frac{0}{0}=0.
For any f∈ℐc​x,f\in\mathcal{I}\_{cx}, let ai=0a\_{i}=0 , bi=x¯ib\_{i}=\bar{x}\_{i} and ci=k1​i,c\_{i}=k\_{1i}, where

|  |  |  |
| --- | --- | --- |
|  | VaRα¯i(Xi)−1k1​ifi(VaRα¯i(Xi)))⩽x¯i⩽VaRβ¯i(Xi),\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i})-\frac{1}{k\_{1i}}f\_{i}(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i})))\leqslant\bar{x}\_{i}\leqslant\mathrm{VaR}\_{\bar{\beta}\_{i}}(X\_{i}), |  |

such that
RVaRβi,αi(rai,bi,ci(Xi)))=RVaRβi,αi(fi(Xi)).\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i})))=\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(f\_{i}(X\_{i})).
The existence of such x¯i\bar{x}\_{i} is guaranteed by the continuity of RVaRβi,αi​(rai,t,ci​(Xi))\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(r\_{a\_{i},t,c\_{i}}(X\_{i})) for t∈[VaRα¯i(Xi)−1k1​ifi(VaRα¯i(Xi))),VaRβ¯i(Xi)],t\in[\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i})-\frac{1}{k\_{1i}}f\_{i}(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i}))),\mathrm{VaR}\_{\bar{\beta}\_{i}}(X\_{i})],
and the fact that

|  |  |  |
| --- | --- | --- |
|  | RVaRβi,αi​(rai,VaRβ¯i​(Xi),ci​(Xi))⩽RVaRβi,αi​(fi​(Xi))⩽RVaRβi,αi​(rai,VaRα¯i(Xi)−1k1​ifi(VaRα¯i(Xi))),ci​(Xi)).\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(r\_{a\_{i},\mathrm{VaR}\_{\bar{\beta}\_{i}}(X\_{i}),c\_{i}}(X\_{i}))\leqslant\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(f\_{i}(X\_{i}))\leqslant\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(r\_{a\_{i},\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i})-\frac{1}{k\_{1i}}f\_{i}(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i}))),c\_{i}}(X\_{i})). |  |

By the convexity of fi,f\_{i}, we have rai,bi,ci​(x)⩽fi​(x)r\_{a\_{i},b\_{i},c\_{i}}(x)\leqslant f\_{i}(x) for x⩽VaRα¯ix\leqslant\mathrm{VaR}\_{\bar{\alpha}\_{i}} and x⩾VaRβ¯i.x\geqslant\mathrm{VaR}\_{\bar{\beta}\_{i}}. So, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | RVaRγi,γ0​(rai,bi,ci​(Xi))\displaystyle\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i})) | =1γ0​(∫[γ¯0,α¯i]∪[β¯i,γ¯i]rai,bi,ci​(VaRt​(Xi))​dt+αi​RVaRβi,αi​(rai,bi,ci​(Xi)))\displaystyle=\frac{1}{\gamma}\_{0}\left(\int\_{[\bar{\gamma}\_{0},\bar{\alpha}\_{i}]\cup[\bar{\beta}\_{i},\bar{\gamma}\_{i}]}r\_{a\_{i},b\_{i},c\_{i}}(\mathrm{VaR}\_{t}(X\_{i}))\mathrm{d}t+\alpha\_{i}\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i}))\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⩽1γ0​(∫[α¯,α¯i]∪[β¯i,1]fi​(VaRt​(Xi))​dt+αi​RVaRβi,αi​(fi​(Xi)))\displaystyle\leqslant\frac{1}{\gamma}\_{0}\left(\int\_{[\bar{\alpha},\bar{\alpha}\_{i}]\cup[\bar{\beta}\_{i},1]}f\_{i}(\mathrm{VaR}\_{t}(X\_{i}))\mathrm{d}t+\alpha\_{i}\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(f\_{i}(X\_{i}))\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =RVaRγi,γ0​(fi​(X)).\displaystyle=\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(f\_{i}(X)). |  |

This implies that we can always find rai,bi,ci∈ℐc​xr\_{a\_{i},b\_{i},c\_{i}}\in\mathcal{I}\_{cx} that is better than fi.f\_{i}.

Case (4): α¯i⩽γ¯0<γ¯i<β¯i\bar{\alpha}\_{i}\leqslant\bar{\gamma}\_{0}<\bar{\gamma}\_{i}<\bar{\beta}\_{i}.
Let k2​i=(fi)−′​(VaRβ¯i​(Xi)),k\_{2i}=(f\_{i})\_{-}^{\prime}(\mathrm{VaR}\_{\bar{\beta}\_{i}}(X\_{i})), where (fi)−′​(x)(f\_{i})\_{-}^{\prime}(x) is the left derivative of fif\_{i} at xx. Define ai=fi​(VaRγ¯0​(Xi))VaRγ¯0​(Xi),a\_{i}=\frac{f\_{i}(\mathrm{VaR}\_{\bar{\gamma}\_{0}}(X\_{i}))}{\mathrm{VaR}\_{\bar{\gamma}\_{0}}(X\_{i})}, bi=x¯ib\_{i}=\bar{x}\_{i} and
ci=k2​i−ai,c\_{i}=k\_{2i}-a\_{i}, where

|  |  |  |
| --- | --- | --- |
|  | VaRγ¯0​(Xi)⩽x¯i⩽VaRγ¯i​(Xi)\mathrm{VaR}\_{\bar{\gamma}\_{0}}(X\_{i})\leqslant\bar{x}\_{i}\leqslant\mathrm{VaR}\_{\bar{\gamma}\_{i}}(X\_{i}) |  |

such that
RVaRγi,γ0​(rai,bi,ci​(Xi))=RVaRγi,γ0​(fi​(Xi)).\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i}))=\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(f\_{i}(X\_{i})).
The existence of such x¯i\bar{x}\_{i} is guaranteed by the continuity of RVaRγi,γ0​(rai,t,ci​(Xi))\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(r\_{a\_{i},t,c\_{i}}(X\_{i})) for t∈[VaRγ¯0​(Xi),VaRγ¯i​(Xi)]t\in[\mathrm{VaR}\_{\bar{\gamma}\_{0}}(X\_{i}),\mathrm{VaR}\_{\bar{\gamma}\_{i}}(X\_{i})]
and the fact that

|  |  |  |
| --- | --- | --- |
|  | RVaRγi,γ0​(rai,VaRγ¯i​(Xi),ci​(Xi))⩽RVaRγi,γ0​(fi​(Xi))⩽RVaRγi,γ0​(rai,VaRγ¯0​(Xi),ci​(Xi)).\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(r\_{a\_{i},\mathrm{VaR}\_{\bar{\gamma}\_{i}}(X\_{i}),c\_{i}}(X\_{i}))\leqslant\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(f\_{i}(X\_{i}))\leqslant\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(r\_{a\_{i},\mathrm{VaR}\_{\bar{\gamma}\_{0}}(X\_{i}),c\_{i}}(X\_{i})). |  |

The convexity of fif\_{i} implies that rai,bi,ci​(x)⩾fi​(x)r\_{a\_{i},b\_{i},c\_{i}}(x)\geqslant f\_{i}(x) for VaRα¯i​(Xi)⩽x⩽VaRγ¯0​(Xi)\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i})\leqslant x\leqslant\mathrm{VaR}\_{\bar{\gamma}\_{0}}(X\_{i}) and VaRγ¯i​(Xi)⩽x⩽VaRβ¯i​(Xi).\mathrm{VaR}\_{\bar{\gamma}\_{i}}(X\_{i})\leqslant x\leqslant\mathrm{VaR}\_{\bar{\beta}\_{i}}(X\_{i}). Hence, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | RVaRβi,αi​(rai,bi,ci​(Xi))\displaystyle\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i})) | =1αi​(∫[α¯i,γ¯0]∪[γ¯i,β¯i]rai,bi,ci​(VaRt​(Xi))​dt+γ0​RVaRγi,γ0​(rai,bi,ci​(Xi)))\displaystyle=\frac{1}{\alpha\_{i}}\left(\int\_{[\bar{\alpha}\_{i},\bar{\gamma}\_{0}]\cup[\bar{\gamma}\_{i},\bar{\beta}\_{i}]}r\_{a\_{i},b\_{i},c\_{i}}(\mathrm{VaR}\_{t}(X\_{i}))\mathrm{d}t+\gamma\_{0}\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i}))\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⩾1αi​(∫[α¯i,γ¯0]∪[γ¯i,β¯i]fi​(VaRt​(Xi))​dt+γ0​RVaRγi,γ0​(fi​(Xi)))\displaystyle\geqslant\frac{1}{\alpha\_{i}}\left(\int\_{[\bar{\alpha}\_{i},\bar{\gamma}\_{0}]\cup[\bar{\gamma}\_{i},\bar{\beta}\_{i}]}f\_{i}(\mathrm{VaR}\_{t}(X\_{i}))\mathrm{d}t+\gamma\_{0}\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(f\_{i}(X\_{i}))\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =RVaRβi,αi​(fi​(Xi)).\displaystyle=\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(f\_{i}(X\_{i})). |  |

Consequently, RVaRγi,γ0​(fi​(Xi))−RVaRβi,αi​(fi​(Xi))⩾RVaRγi,γ0​(rai,bi,ci​(Xi))−RVaRβi,αi​(rai,bi,ci​(Xi)).\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(f\_{i}(X\_{i}))-\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(f\_{i}(X\_{i})\right)\geqslant\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i}))-\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i})\right).

Case (5): α¯i⩽γ¯0<β¯i<γ¯i\bar{\alpha}\_{i}\leqslant\bar{\gamma}\_{0}<\bar{\beta}\_{i}<\bar{\gamma}\_{i}.
Define ai=fi​(x¯i)x¯ia\_{i}=\frac{f\_{i}(\bar{x}\_{i})}{\bar{x}\_{i}} and bi=ci=0,b\_{i}=c\_{i}=0, where VaRγ¯0​(Xi)⩽x¯i⩽VaRγ¯i​(Xi),\mathrm{VaR}\_{\bar{\gamma}\_{0}}(X\_{i})\leqslant\bar{x}\_{i}\leqslant\mathrm{VaR}\_{\bar{\gamma}\_{i}}(X\_{i}), such that RVaRγi,γ0​(rai,bi,ci​(Xi))=RVaRγi,γ0​(fi​(Xi)).\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i}))=\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(f\_{i}(X\_{i})).
The existence of such x¯i\bar{x}\_{i} is guaranteed by the continuity of RVaRγi,γ0​(rt,bi,ci​(Xi))\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(r\_{t,b\_{i},c\_{i}}(X\_{i})) for t∈[fi​(VaRγ¯0​(Xi))VaRγ¯0​(Xi),fi​(VaRγ¯i​(Xi))VaRγ¯i​(Xi)],t\in[\frac{f\_{i}(\mathrm{VaR}\_{\bar{\gamma}\_{0}}(X\_{i}))}{\mathrm{VaR}\_{\bar{\gamma}\_{0}}(X\_{i})},\frac{f\_{i}(\mathrm{VaR}\_{\bar{\gamma}\_{i}}(X\_{i}))}{\mathrm{VaR}\_{\bar{\gamma}\_{i}}(X\_{i})}],
and the fact that

|  |  |  |
| --- | --- | --- |
|  | RVaRγi,γ0​(rfi​(VaRγ¯0​(Xi))/VaRγ¯0​(Xi),bi,ci​(Xi))⩽RVaRγi,γ0​(fi​(Xi))⩽RVaRγi,γ0​(rfi​(VaRγ¯i​(Xi))/VaRγ¯i​(Xi),bi,ci​(Xi)).\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(r\_{f\_{i}(\mathrm{VaR}\_{\bar{\gamma}\_{0}}(X\_{i}))/\mathrm{VaR}\_{\bar{\gamma}\_{0}}(X\_{i}),b\_{i},c\_{i}}(X\_{i}))\leqslant\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(f\_{i}(X\_{i}))\leqslant\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(r\_{f\_{i}(\mathrm{VaR}\_{\bar{\gamma}\_{i}}(X\_{i}))/\mathrm{VaR}\_{\bar{\gamma}\_{i}}(X\_{i}),b\_{i},c\_{i}}(X\_{i})). |  |

Note that RVaRγi,γ0​(rai,bi,ci​(Xi))=RVaRγi,γ0​(fi​(Xi))\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i}))=\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(f\_{i}(X\_{i})) implies

|  |  |  |
| --- | --- | --- |
|  | ∫[γ¯0,β¯i]rai,bi,ci​(VaRt​(Xi))​dt⩾∫[γ¯0,β¯i]fi​(VaRt​(Xi))​dt.\int\_{[\bar{\gamma}\_{0},\bar{\beta}\_{i}]}r\_{a\_{i},b\_{i},c\_{i}}(\mathrm{VaR}\_{t}(X\_{i}))\mathrm{d}t\geqslant\int\_{[\bar{\gamma}\_{0},\bar{\beta}\_{i}]}f\_{i}(\mathrm{VaR}\_{t}(X\_{i}))\mathrm{d}t. |  |

By the convexity of fi,f\_{i}, we have rai,bi,ci​(x)⩾fi​(x)r\_{a\_{i},b\_{i},c\_{i}}(x)\geqslant f\_{i}(x) for VaRα¯i​(Xi)⩽x⩽VaRγ¯0​(Xi).\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i})\leqslant x\leqslant\mathrm{VaR}\_{\bar{\gamma}\_{0}}(X\_{i}). Hence, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | RVaRβi,αi​(rai,bi,ci​(Xi))\displaystyle\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i})) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1αi​(∫[α¯i,γ¯0]rai,bi,ci​(VaRt​(Xi))​dt+∫[γ¯0,β¯i]rai,bi,ci​(VaRt​(Xi))​dt)\displaystyle=\frac{1}{\alpha\_{i}}\left(\int\_{[\bar{\alpha}\_{i},\bar{\gamma}\_{0}]}r\_{a\_{i},b\_{i},c\_{i}}(\mathrm{VaR}\_{t}(X\_{i}))\mathrm{d}t+\int\_{[\bar{\gamma}\_{0},\bar{\beta}\_{i}]}r\_{a\_{i},b\_{i},c\_{i}}(\mathrm{VaR}\_{t}(X\_{i}))\mathrm{d}t\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⩾1αi​(∫[α¯i,γ¯0]fi​(VaRt​(Xi))​dt+∫[γ¯0,β¯i]fi​(VaRt​(Xi))​dt)\displaystyle\geqslant\frac{1}{\alpha\_{i}}\left(\int\_{[\bar{\alpha}\_{i},\bar{\gamma}\_{0}]}f\_{i}(\mathrm{VaR}\_{t}(X\_{i}))\mathrm{d}t+\int\_{[\bar{\gamma}\_{0},\bar{\beta}\_{i}]}f\_{i}(\mathrm{VaR}\_{t}(X\_{i}))\mathrm{d}t\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =RVaRβi,αi​(fi​(X)),\displaystyle=\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(f\_{i}(X)), |  |

implying that we can always find rai,bi,ci∈ℐc​xr\_{a\_{i},b\_{i},c\_{i}}\in\mathcal{I}\_{cx} that is better than fi.f\_{i}.

Case (6): γ¯0⩽α¯i<γ¯i<β¯i\bar{\gamma}\_{0}\leqslant\bar{\alpha}\_{i}<\bar{\gamma}\_{i}<\bar{\beta}\_{i}.
Define ai=0a\_{i}=0, bi=x¯ib\_{i}=\bar{x}\_{i} and ci=1,c\_{i}=1, where VaRα¯i​(Xi)−fi​(VaRα¯i​(Xi))⩽x¯i⩽VaRβ¯i​(Xi),\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i})-f\_{i}(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i}))\leqslant\bar{x}\_{i}\leqslant\mathrm{VaR}\_{\bar{\beta}\_{i}}(X\_{i}), such that RVaRβi,αi​(rai,bi,ci​(Xi))=RVaRβi,αi​(fi​(Xi)).\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i}))=\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(f\_{i}(X\_{i})). The existence of such x¯i\bar{x}\_{i} is guaranteed by the continuity of RVaRβi,αi​(rai,t,ci​(Xi))\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(r\_{a\_{i},t,c\_{i}}(X\_{i})) for t∈[VaRα¯i​(Xi)−fi​(VaRα¯i​(Xi)),VaRβ¯i​(Xi)]t\in[\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i})-f\_{i}(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i})),\mathrm{VaR}\_{\bar{\beta}\_{i}}(X\_{i})] and the fact that

|  |  |  |
| --- | --- | --- |
|  | RVaRβi,αi​(rai,VaRβ¯i​(Xi),ci​(Xi))⩽RVaRβi,αi​(fi​(Xi))⩽RVaRβi,αi​(rai,VaRα¯i​(Xi)−fi​(VaRα¯i​(Xi)),ci​(Xi)).\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(r\_{a\_{i},\mathrm{VaR}\_{\bar{\beta}\_{i}}(X\_{i}),c\_{i}}(X\_{i}))\leqslant\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(f\_{i}(X\_{i}))\leqslant\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(r\_{a\_{i},\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i})-f\_{i}(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i})),c\_{i}}(X\_{i})). |  |

Note that RVaRβi,αi​(rai,bi,ci​(Xi))=RVaRβi,αi​(fi​(Xi))\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i}))=\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(f\_{i}(X\_{i})) implies

|  |  |  |
| --- | --- | --- |
|  | ∫[α¯i,γ¯i]rai,bi,ci​(VaRt​(Xi))​dt⩽∫[α¯i,γ¯i]fi​(VaRt​(Xi))​dt.\int\_{[\bar{\alpha}\_{i},\bar{\gamma}\_{i}]}r\_{a\_{i},b\_{i},c\_{i}}(\mathrm{VaR}\_{t}(X\_{i}))\mathrm{d}t\leqslant\int\_{[\bar{\alpha}\_{i},\bar{\gamma}\_{i}]}f\_{i}(\mathrm{VaR}\_{t}(X\_{i}))\mathrm{d}t. |  |

By the convexity of fif\_{i}, we have rai,bi,ci​(x)⩽fi​(x)r\_{a\_{i},b\_{i},c\_{i}}(x)\leqslant f\_{i}(x) for VaRγ¯0​(Xi)⩽x⩽VaRα¯i​(Xi).\mathrm{VaR}\_{\bar{\gamma}\_{0}}(X\_{i})\leqslant x\leqslant\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X\_{i}). Hence, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | RVaRγi,γ0​(rai,bi,ci​(Xi))\displaystyle\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i})) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1γ0​(∫[γ¯0,α¯i]rai,bi,ci​(VaRt​(Xi))​dt+∫[α¯i,γ¯i]rai,bi,ci​(VaRt​(Xi))​dt)\displaystyle=\frac{1}{\gamma\_{0}}\left(\int\_{[\bar{\gamma}\_{0},\bar{\alpha}\_{i}]}r\_{a\_{i},b\_{i},c\_{i}}(\mathrm{VaR}\_{t}(X\_{i}))\mathrm{d}t+\int\_{[\bar{\alpha}\_{i},\bar{\gamma}\_{i}]}r\_{a\_{i},b\_{i},c\_{i}}(\mathrm{VaR}\_{t}(X\_{i}))\mathrm{d}t\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⩽1γ0​(∫[γ¯0,α¯i]fi​(VaRt​(Xi))​dt+∫[α¯i,γ¯i]fi​(VaRt​(Xi))​dt)\displaystyle\leqslant\frac{1}{\gamma\_{0}}\left(\int\_{[\bar{\gamma}\_{0},\bar{\alpha}\_{i}]}f\_{i}(\mathrm{VaR}\_{t}(X\_{i}))\mathrm{d}t+\int\_{[\bar{\alpha}\_{i},\bar{\gamma}\_{i}]}f\_{i}(\mathrm{VaR}\_{t}(X\_{i}))\mathrm{d}t\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =RVaRγi,γ0​(fi​(X)).\displaystyle=\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(f\_{i}(X)). |  |

Consequently, we have

|  |  |  |
| --- | --- | --- |
|  | RVaRγi,γ0​(fi​(Xi))−RVaRβi,αi​(fi​(Xi))⩾RVaRγi,γ0​(rai,bi,ci​(Xi))−RVaRβi,αi​(rai,bi,ci​(Xi)).\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(f\_{i}(X\_{i}))-\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(f\_{i}(X\_{i})\right)\geqslant\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i}))-\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}\left(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i})\right). |  |

To summarize the six cases, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | inf𝐟∈ℐc​xnV​(𝐟)\displaystyle\inf\_{{\bf f}\in\mathcal{I}\_{cx}^{n}}V(\mathbf{f}) | ⩾inf𝜸∈(β+α)​Δn,γ0⩾αinf(𝐚,𝐛,𝐜)∈𝒜2R​(𝐚,𝐛,𝐜,𝜸)\displaystyle\geqslant\inf\_{\boldsymbol{\gamma}\in(\beta+\alpha)\Delta\_{n},\gamma\_{0}\geqslant\alpha}\inf\_{({\bf a},{\bf b},{\bf c})\in\mathcal{A}\_{2}}R({\bf a},{\bf b},{\bf c},\boldsymbol{\gamma}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =inf(𝐚,𝐛,𝐜)∈𝒜2inf𝜸∈(β+α)​Δn,γ0⩾αR​(𝐚,𝐛,𝐜,𝜸).\displaystyle=\inf\_{({\bf a},{\bf b},{\bf c})\in\mathcal{A}\_{2}}\inf\_{\boldsymbol{\gamma}\in(\beta+\alpha)\Delta\_{n},\gamma\_{0}\geqslant\alpha}R({\bf a},{\bf b},{\bf c},\boldsymbol{\gamma}). |  |

We obtain the desired result.
∎

###### Proof of Proposition [2](https://arxiv.org/html/2512.11430v1#Thmproposition2 "Proposition 2. ‣ 3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty").

It is evident that 𝐠𝐚∗,𝐛∗{\bf g}\_{{\bf a}^{\*},{\bf b}^{\*}} and 𝐫𝐚∗,𝐛∗,𝐜∗{\bf r}\_{{\bf a}^{\*},{\bf b}^{\*},{\bf c}^{\*}} are the optimal ceded loss functions for cases (i)-(ii), respectively. The existence of (𝐚∗,𝐛∗)∈𝒜1({\bf a}^{\*},{\bf b}^{\*})\in\mathcal{A}\_{1} and (𝐚∗,𝐛∗,𝐜∗)∈𝒜2({\bf a}^{\*},{\bf b}^{\*},{\bf c}^{\*})\in\mathcal{A}\_{2} follows from the continuity of the functions GG and RR. Specifically, the existence of (𝐚∗,𝐛∗)({\bf a}^{\*},{\bf b}^{\*}) is guaranteed by the continuity of RVaR\mathrm{RVaR} and ES\mathrm{ES}, while the existence of (𝐚∗,𝐛∗,𝐜∗)({\bf a}^{\*},{\bf b}^{\*},{\bf c}^{\*}) needs an additional argument because RVaRγi,γ0​(Xi)\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(X\_{i}) may lose continuity as γ0↓0\gamma\_{0}\downarrow 0.

To be specific, for 0⩽ε⩽T⩽1,0\leqslant\varepsilon\leqslant T\leqslant 1, define

|  |  |  |
| --- | --- | --- |
|  | Δ¯nε,T={(γ0,γ1,…,γn)∈[ε,T]×[0,T]n:∑i=0nγi=T}.\bar{\Delta}\_{n}^{\varepsilon,T}=\left\{(\gamma\_{0},\gamma\_{1},\ldots,\gamma\_{n})\in[\varepsilon,T]\times[0,T]^{n}:\sum^{n}\_{i=0}\gamma\_{i}=T\right\}. |  |

Clearly, for 0<ε<β+α0<\varepsilon<\beta+\alpha, RVaRγi,γ0​(Xi)\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(X\_{i}) is continuous with respect to 𝜸\boldsymbol{\gamma} over Δ¯nε,β+α\bar{\Delta}\_{n}^{\varepsilon,\beta+\alpha}, and

|  |  |  |
| --- | --- | --- |
|  | RVaRγi,γ0​(rai,bi,ci​(Xi))=1γ0​∫γiγi+γ0rai,bi,ci​(Fi−1​(t))​dt,\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i}))=\frac{1}{\gamma\_{0}}\int^{\gamma\_{i}+\gamma\_{0}}\_{\gamma\_{i}}r\_{a\_{i},b\_{i},c\_{i}}(F^{-1}\_{i}(t))\mathrm{d}t, |  |

which implies that RVaRγi,γ0​(rai,bi,ci​(Xi))\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i})) is continuous with respect to (𝐚,𝐛,𝐜,𝜸)({\bf a},{\bf b},{\bf c},\boldsymbol{\gamma}) over 𝒜2×Δ¯nε,β+α\mathcal{A}\_{2}\times\bar{\Delta}\_{n}^{\varepsilon,\beta+\alpha} for ε>0.\varepsilon>0. So, by the continuity of RVaR,\mathrm{RVaR}, R​(𝐚,𝐛,𝐜,𝜸)R({\bf a},{\bf b},{\bf c},\boldsymbol{\gamma}) is a continuous function of (𝐚,𝐛,𝐜,𝜸)({\bf a},{\bf b},{\bf c},\boldsymbol{\gamma}) over 𝒜2×Δ¯nε,β+α\mathcal{A}\_{2}\times\bar{\Delta}\_{n}^{\varepsilon,\beta+\alpha} for ε>0\varepsilon>0 and 𝒜2\mathcal{A}\_{2} is a closed set. Therefore, there exists (𝐚ε∗,𝐛ε∗,𝐜ε∗,𝜸ε∗)∈𝒜2×Δ¯nε,β+α({\bf a}^{\*}\_{\varepsilon},{\bf b}^{\*}\_{\varepsilon},{\bf c}^{\*}\_{\varepsilon},\boldsymbol{\gamma}^{\*}\_{\varepsilon})\in\mathcal{A}\_{2}\times\bar{\Delta}\_{n}^{\varepsilon,\beta+\alpha} such that

|  |  |  |
| --- | --- | --- |
|  | (𝐚ε∗,𝐛ε∗,𝐜ε∗,𝜸ε∗)∈arg​inf(𝐚,𝐛,𝐜,𝜸)∈𝒜2×Δ¯nε,β+αR​(𝐚,𝐛,𝐜,𝜸).({\bf a}^{\*}\_{\varepsilon},{\bf b}^{\*}\_{\varepsilon},{\bf c}^{\*}\_{\varepsilon},\boldsymbol{\gamma}^{\*}\_{\varepsilon})\in\arg\inf\_{({\bf a},{\bf b},{\bf c},\boldsymbol{\gamma})\in\mathcal{A}\_{2}\times\bar{\Delta}\_{n}^{\varepsilon,\beta+\alpha}}R({\bf a},{\bf b},{\bf c},\boldsymbol{\gamma}). |  |

Note that

|  |  |  |  |
| --- | --- | --- | --- |
|  | limγ0↓0RVaRγi,γ0​(rai,bi,ci​(Xi))\displaystyle\lim\limits\_{\gamma\_{0}\downarrow 0}\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i})) | =limγ0↓01γ0​∫γiγi+γ0VaR1−t​(rai,bi,ci​(Xi))​dt\displaystyle=\lim\limits\_{\gamma\_{0}\downarrow 0}\frac{1}{\gamma\_{0}}\int^{\gamma\_{i}+\gamma\_{0}}\_{\gamma\_{i}}\mathrm{VaR}\_{1-t}(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i}))\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =VaR1−γi​(rai,bi,ci​(Xi)).\displaystyle=\mathrm{VaR}\_{1-\gamma\_{i}}(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i})). |  |

We define RVaRγi,0​(rai,bi,ci​(Xi))=VaR1−γi​(rai,bi,ci​(Xi)).\mathrm{RVaR}\_{\gamma\_{i},0}(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i}))=\mathrm{VaR}\_{1-\gamma\_{i}}(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i})). Also, RVaR0,0​(rai,bi,ci​(Xi))=∞\mathrm{RVaR}\_{0,0}(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i}))=\infty for ai+ci>0a\_{i}+c\_{i}>0 and ess​sup⁡Xi=∞.\operatorname{ess\,sup}X\_{i}=\infty. With this situation, RVaRγi,γ0​(rai,bi,ci​(Xi))\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}(r\_{a\_{i},b\_{i},c\_{i}}(X\_{i})) is continuous with respect to (𝐚,𝐛,𝐜,𝜸)({\bf a},{\bf b},{\bf c},\boldsymbol{\gamma}) over 𝒜2×Δ¯n0,β+α.\mathcal{A}\_{2}\times\bar{\Delta}\_{n}^{0,\beta+\alpha}. Then R​(𝐚,𝐛,𝐜,𝜸)R({\bf a},{\bf b},{\bf c},\boldsymbol{\gamma}) is a continuous function of (𝐚,𝐛,𝐜,𝜸)({\bf a},{\bf b},{\bf c},\boldsymbol{\gamma}) over 𝒜2×Δ¯n0,β+α.\mathcal{A}\_{2}\times\bar{\Delta}\_{n}^{0,\beta+\alpha}. According to the fact that 𝒜2×Δ¯n0,β+α\mathcal{A}\_{2}\times\bar{\Delta}\_{n}^{0,\beta+\alpha} is a closed set, there exists

|  |  |  |
| --- | --- | --- |
|  | (𝐚∗,𝐛∗,𝐜∗)=arg​inf(𝐚,𝐛,𝐜)∈𝒜2{inf𝜸∈(β+α)​Δn,γ0⩾αR​(𝐚,𝐛,𝐜,𝜸)}.({\bf a}^{\*},{\bf b}^{\*},{\bf c}^{\*})=\arg\inf\_{({\bf a},{\bf b},{\bf c})\in\mathcal{A}\_{2}}\left\{\inf\_{\boldsymbol{\gamma}\in(\beta+\alpha)\Delta\_{n},\gamma\_{0}\geqslant\alpha}R({\bf a},{\bf b},{\bf c},\boldsymbol{\gamma})\right\}. |  |

We complete the proof.
∎

## Appendix C Proofs of Section [4](https://arxiv.org/html/2512.11430v1#S4 "4 Optimal solution to the special case of VaR ‣ Pareto-optimal reinsurance under dependence uncertainty")

###### Proof of Theorem [2](https://arxiv.org/html/2512.11430v1#Thmtheorem2 "Theorem 2. ‣ 4 Optimal solution to the special case of VaR ‣ Pareto-optimal reinsurance under dependence uncertainty").

(i) In light of Lemma [2](https://arxiv.org/html/2512.11430v1#Thmlemma2 "Lemma 2. ‣ 4 Optimal solution to the special case of VaR ‣ Pareto-optimal reinsurance under dependence uncertainty"), we have for n=2n=2,

|  |  |  |
| --- | --- | --- |
|  | inf𝐟∈ℐnV​(𝐟)\displaystyle\inf\_{{\bf f}\in\mathcal{I}^{n}}V(\mathbf{f}) |  |
|  |  |  |
| --- | --- | --- |
|  | =inf𝐟∈ℐninf𝜸∈(1−α)​Δn∑i=1n(VaRαi​(Xi)−fi​(VaRαi​(Xi))+RVaRγi,γ0​(fi​(Xi)))\displaystyle=\inf\_{{\bf f}\in\mathcal{I}^{n}}\inf\_{\boldsymbol{\gamma}\in(1-\alpha)\Delta\_{n}}\sum\_{i=1}^{n}\left(\mathrm{VaR}\_{\alpha\_{i}}\left(X\_{i}\right)-f\_{i}(\mathrm{VaR}\_{\alpha\_{i}}\left(X\_{i}\right))+\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}\left(f\_{i}(X\_{i})\right)\right) |  |
|  |  |  |
| --- | --- | --- |
|  | =inf𝜸∈(1−α)​Δninf𝐟∈ℐn∑i=1n(VaRαi​(Xi)−fi​(VaRαi​(Xi))+RVaRγi,γ0​(fi​(Xi))).\displaystyle=\inf\_{\boldsymbol{\gamma}\in(1-\alpha)\Delta\_{n}}\inf\_{{\bf f}\in\mathcal{I}^{n}}\sum\_{i=1}^{n}\left(\mathrm{VaR}\_{\alpha\_{i}}\left(X\_{i}\right)-f\_{i}(\mathrm{VaR}\_{\alpha\_{i}}\left(X\_{i}\right))+\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}\left(f\_{i}(X\_{i})\right)\right). |  |

Let ai=VaRαi​(Xi)−fi​(VaRαi​(Xi))a\_{i}=\mathrm{VaR}\_{\alpha\_{i}}(X\_{i})-f\_{i}(\mathrm{VaR}\_{\alpha\_{i}}(X\_{i})) and bi=VaRαi​(Xi).b\_{i}=\mathrm{VaR}\_{\alpha\_{i}}(X\_{i}). Then it follows that fi​(VaRαi​(Xi))=gai,bi​(VaRαi​(Xi))f\_{i}(\mathrm{VaR}\_{\alpha\_{i}}\left(X\_{i}\right))=g\_{a\_{i},b\_{i}}(\mathrm{VaR}\_{\alpha\_{i}}\left(X\_{i}\right)) and fi​(Xi)⩾gai,bi​(Xi),f\_{i}(X\_{i})\geqslant g\_{a\_{i},b\_{i}}(X\_{i}), which implies

|  |  |  |
| --- | --- | --- |
|  | RVaRγi,γ0​(fi​(Xi))−fi​(VaRαi​(Xi))⩾RVaRγi,γ0​(gai,bi​(Xi))−gai,bi​(VaRαi​(Xi));\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}\left(f\_{i}(X\_{i})\right)-f\_{i}(\mathrm{VaR}\_{\alpha\_{i}}\left(X\_{i}\right))\geqslant\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}\left(g\_{a\_{i},b\_{i}}(X\_{i})\right)-g\_{a\_{i},b\_{i}}(\mathrm{VaR}\_{\alpha\_{i}}\left(X\_{i}\right)); |  |

see Figure [6](https://arxiv.org/html/2512.11430v1#A3.F6 "Figure 6 ‣ Appendix C Proofs of Section 4 ‣ Pareto-optimal reinsurance under dependence uncertainty") (i).
Hence, we have

|  |  |  |
| --- | --- | --- |
|  | inf𝐟∈ℐnV​(𝐟)⩾inf𝜸∈(1−α)​Δninf(𝐚,𝐛)∈𝒜1G¯​(𝐚,𝐛,𝜸)=inf(𝐚,𝐛)∈𝒜1inf𝜸∈(1−α)​ΔnG¯​(𝐚,𝐛,𝜸).\inf\_{{\bf f}\in\mathcal{I}^{n}}V(\mathbf{f})\geqslant\inf\_{\boldsymbol{\gamma}\in(1-\alpha)\Delta\_{n}}\inf\_{({\bf a},{\bf b})\in\mathcal{A}\_{1}}\overline{G}({\bf a},{\bf b},{\boldsymbol{\gamma}})=\inf\_{({\bf a},{\bf b})\in\mathcal{A}\_{1}}\inf\_{\boldsymbol{\gamma}\in(1-\alpha)\Delta\_{n}}\overline{G}({\bf a},{\bf b},{\boldsymbol{\gamma}}). |  |

The inverse inequality is trivial, similar to the proof of Theorem [1](https://arxiv.org/html/2512.11430v1#Thmtheorem1 "Theorem 1. ‣ 3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty") (i). We obtain the desired result.

(ii) Let fi∈ℐc​vnf\_{i}\in\mathcal{I}\_{cv}^{n} and consider XiX\_{i} with FXi∈ℳc​x1−β−αF\_{X\_{i}}\in\mathcal{M}\_{cx}^{1-\beta-\alpha}.
To show that Ffi​(Xi)∈ℳc​x1−β−αF\_{f\_{i}(X\_{i})}\in\mathcal{M}\_{cx}^{1-\beta-\alpha}, we can follow the same method as in Theorem [1](https://arxiv.org/html/2512.11430v1#Thmtheorem1 "Theorem 1. ‣ 3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty"), which establishes that applying a convex ceded loss function to a variable with a concave-tail distribution preserves the concavity in the tail. By Lemma [2](https://arxiv.org/html/2512.11430v1#Thmlemma2 "Lemma 2. ‣ 4 Optimal solution to the special case of VaR ‣ Pareto-optimal reinsurance under dependence uncertainty"), we have

|  |  |  |
| --- | --- | --- |
|  | inf𝐟∈ℐc​vnV​(𝐟)\displaystyle\inf\_{{\bf f}\in\mathcal{I}\_{cv}^{n}}V(\mathbf{f}) |  |
|  |  |  |
| --- | --- | --- |
|  | =inf𝐟∈ℐc​vninf𝜸∈(1−α)​Δn∑i=1n(VaRαi​(Xi)−fi​(VaRαi​(Xi))+RVaRγi,γ0​(fi​(Xi)))\displaystyle=\inf\_{{\bf f}\in\mathcal{I}\_{cv}^{n}}\inf\_{\boldsymbol{\gamma}\in(1-\alpha)\Delta\_{n}}\sum\_{i=1}^{n}\left(\mathrm{VaR}\_{\alpha\_{i}}\left(X\_{i}\right)-f\_{i}(\mathrm{VaR}\_{\alpha\_{i}}\left(X\_{i}\right))+\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}\left(f\_{i}(X\_{i})\right)\right) |  |
|  |  |  |
| --- | --- | --- |
|  | =inf𝜸∈(1−α)​Δninf𝐟∈ℐc​vn∑i=1n(VaRαi​(Xi)−fi​(VaRαi​(Xi))+RVaRγi,γ0​(fi​(Xi))).\displaystyle=\inf\_{\boldsymbol{\gamma}\in(1-\alpha)\Delta\_{n}}\inf\_{{\bf f}\in\mathcal{I}\_{cv}^{n}}\sum\_{i=1}^{n}\left(\mathrm{VaR}\_{\alpha\_{i}}\left(X\_{i}\right)-f\_{i}(\mathrm{VaR}\_{\alpha\_{i}}\left(X\_{i}\right))+\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}\left(f\_{i}(X\_{i})\right)\right). |  |

Let ai=fi​(VaRαi​(Xi))VaRαi​(Xi)a\_{i}=\frac{f\_{i}(\mathrm{VaR}\_{\alpha\_{i}}(X\_{i}))}{\mathrm{VaR}\_{\alpha\_{i}}(X\_{i})} and bi=VaRαi​(Xi).b\_{i}=\mathrm{VaR}\_{\alpha\_{i}}(X\_{i}). Then we have

|  |  |  |
| --- | --- | --- |
|  | RVaRγi,γ0​(fi​(Xi))−fi​(VaRαi​(Xi))⩾RVaRγi,γ0​(lai,bi​(Xi))−lai,bi​(VaRαi​(Xi));\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}\left(f\_{i}(X\_{i})\right)-f\_{i}(\mathrm{VaR}\_{\alpha\_{i}}\left(X\_{i}\right))\geqslant\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}\left(l\_{a\_{i},b\_{i}}(X\_{i})\right)-l\_{a\_{i},b\_{i}}(\mathrm{VaR}\_{\alpha\_{i}}\left(X\_{i}\right)); |  |

see Figure [6](https://arxiv.org/html/2512.11430v1#A3.F6 "Figure 6 ‣ Appendix C Proofs of Section 4 ‣ Pareto-optimal reinsurance under dependence uncertainty") (ii).
The rest of the proof is the same as that of (i). Hence, it is omitted.

(iii) As already verified in Theorem [1](https://arxiv.org/html/2512.11430v1#Thmtheorem1 "Theorem 1. ‣ 3 Optimal insurance with dependence uncertainty ‣ Pareto-optimal reinsurance under dependence uncertainty"), one can check that if Xi∼Fi∈ℳc​vαX\_{i}\sim F\_{i}\in\mathcal{M}\_{cv}^{\alpha} and fi∈ℐc​xf\_{i}\in\mathcal{I}\_{cx}, then the cumulative distribution function of fi​(Xi)f\_{i}(X\_{i}) is concave beyond its α\alpha-quantile.
Hence, by Lemma [2](https://arxiv.org/html/2512.11430v1#Thmlemma2 "Lemma 2. ‣ 4 Optimal solution to the special case of VaR ‣ Pareto-optimal reinsurance under dependence uncertainty"), we have

|  |  |  |
| --- | --- | --- |
|  | inf𝐟∈ℐc​xnV​(𝐟)\displaystyle\inf\_{{\bf f}\in\mathcal{I}\_{cx}^{n}}V(\mathbf{f}) |  |
|  |  |  |
| --- | --- | --- |
|  | =inf𝐟∈ℐc​xninf𝜸∈(1−β)​Δn∑i=1n(VaRαi​(Xi)−fi​(VaRαi​(Xi))+RVaRγi,γ0​(fi​(Xi)))\displaystyle=\inf\_{{\bf f}\in\mathcal{I}\_{cx}^{n}}\inf\_{\boldsymbol{\gamma}\in(1-\beta)\Delta\_{n}}\sum\_{i=1}^{n}\left(\mathrm{VaR}\_{\alpha\_{i}}\left(X\_{i}\right)-f\_{i}(\mathrm{VaR}\_{\alpha\_{i}}\left(X\_{i}\right))+\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}\left(f\_{i}(X\_{i})\right)\right) |  |
|  |  |  |
| --- | --- | --- |
|  | =inf𝜸∈(1−β)​Δninf𝐟∈ℐc​xn∑i=1n(VaRαi​(Xi)−fi​(VaRαi​(Xi))+RVaRγi,γ0​(fi​(Xi))).\displaystyle=\inf\_{\boldsymbol{\gamma}\in(1-\beta)\Delta\_{n}}\inf\_{{\bf f}\in\mathcal{I}\_{cx}^{n}}\sum\_{i=1}^{n}\left(\mathrm{VaR}\_{\alpha\_{i}}\left(X\_{i}\right)-f\_{i}(\mathrm{VaR}\_{\alpha\_{i}}\left(X\_{i}\right))+\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}\left(f\_{i}(X\_{i})\right)\right). |  |

Let ai=(fi)+′​(VaRαi​(Xi))a\_{i}=(f\_{i})\_{+}^{\prime}(\mathrm{VaR}\_{\alpha\_{i}}(X\_{i})) and bi=VaRαi​(Xi)−fi​(VaRαi​(Xi))ai,b\_{i}=\mathrm{VaR}\_{\alpha\_{i}}(X\_{i})-\frac{f\_{i}(\mathrm{VaR}\_{\alpha\_{i}}(X\_{i}))}{a\_{i}}, where (fi)+′​(x)(f\_{i})\_{+}^{\prime}(x) is the right derivative of fif\_{i} at xx. Then it follows that fi​(VaRαi​(Xi))=hai,bi​(VaRαi​(Xi))f\_{i}(\mathrm{VaR}\_{\alpha\_{i}}\left(X\_{i}\right))=h\_{a\_{i},b\_{i}}(\mathrm{VaR}\_{\alpha\_{i}}\left(X\_{i}\right)) and fi​(Xi)⩾hai,bi​(Xi),f\_{i}(X\_{i})\geqslant h\_{a\_{i},b\_{i}}(X\_{i}), which implies

|  |  |  |
| --- | --- | --- |
|  | RVaRγi,γ0​(fi​(Xi))−fi​(VaRαi​(Xi))⩾RVaRγi,γ0​(hai,bi​(Xi))−hai,bi​(VaRαi​(Xi));\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}\left(f\_{i}(X\_{i})\right)-f\_{i}(\mathrm{VaR}\_{\alpha\_{i}}\left(X\_{i}\right))\geqslant\mathrm{RVaR}\_{\gamma\_{i},\gamma\_{0}}\left(h\_{a\_{i},b\_{i}}(X\_{i})\right)-h\_{a\_{i},b\_{i}}(\mathrm{VaR}\_{\alpha\_{i}}\left(X\_{i}\right)); |  |

see Figure [6](https://arxiv.org/html/2512.11430v1#A3.F6 "Figure 6 ‣ Appendix C Proofs of Section 4 ‣ Pareto-optimal reinsurance under dependence uncertainty") (iii).
The rest of the proof is exactly the same as that of (i). The details are omitted.
∎

![Refer to caption](x5.png)


Figure 6:  (i) gai,big\_{a\_{i},b\_{i}} for the general case with n=2n=2;
(ii) lai,bil\_{a\_{i},b\_{i}} for 𝐅∈(ℳc​xα)n\mathbf{F}\in(\mathcal{M}\_{cx}^{\alpha})^{n};
(iii) hai,bih\_{a\_{i},b\_{i}} for 𝐅∈(ℳc​vα)n\mathbf{F}\in(\mathcal{M}\_{cv}^{\alpha})^{n}.

###### Proof of Proposition [3](https://arxiv.org/html/2512.11430v1#Thmproposition3 "Proposition 3. ‣ 4 Optimal solution to the special case of VaR ‣ Pareto-optimal reinsurance under dependence uncertainty").

By the result in Makarov ([1981](https://arxiv.org/html/2512.11430v1#bib.bib32)) and the continuity of F1−1F\_{1}^{-1} and F2−1F\_{2}^{-1}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(𝐟)=\displaystyle V(\mathbf{f})= | VaRα1​(X1)+VaRα2​(X2)−f​(VaRα1​(X1))−f2​(VaRα2​(X2))\displaystyle\mathrm{VaR}\_{\alpha\_{1}}(X\_{1})+\mathrm{VaR}\_{\alpha\_{2}}(X\_{2})-f(\mathrm{VaR}\_{\alpha\_{1}}(X\_{1}))-f\_{2}(\mathrm{VaR}\_{\alpha\_{2}}(X\_{2})) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +inft∈[0,1−α]{f1​(VaRα+t​(X1))+f2​(VaR1−t​(X2))}.\displaystyle+\inf\_{t\in[0,1-\alpha]}\left\{f\_{1}(\mathrm{VaR}\_{\alpha+t}(X\_{1}))+f\_{2}(\mathrm{VaR}\_{1-t}(X\_{2}))\right\}. |  |

Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | inf(f1,f2)∈ℐ2V​(𝐟)\displaystyle\inf\_{(f\_{1},f\_{2})\in\mathcal{I}^{2}}V(\mathbf{f}) | =VaRα1(X1)+VaRα2(X2)+inft∈[0,1−α]inf(f1,f2)∈ℐ2{f1(VaRα+t(X1))\displaystyle=\mathrm{VaR}\_{\alpha\_{1}}(X\_{1})+\mathrm{VaR}\_{\alpha\_{2}}(X\_{2})+\inf\_{t\in[0,1-\alpha]}\inf\_{(f\_{1},f\_{2})\in\mathcal{I}^{2}}\left\{f\_{1}(\mathrm{VaR}\_{\alpha+t}(X\_{1}))\right. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +f2(VaR1−t(X2))−f1(VaRα1(X1))−f2(VaRα2(X2))}.\displaystyle\left.+f\_{2}(\mathrm{VaR}\_{1-t}(X\_{2}))-f\_{1}(\mathrm{VaR}\_{\alpha\_{1}}(X\_{1}))-f\_{2}(\mathrm{VaR}\_{\alpha\_{2}}(X\_{2}))\right\}. |  |

Let ai=VaRαi​(Xi)−fi​(VaRαi​(Xi))a\_{i}=\mathrm{VaR}\_{\alpha\_{i}}(X\_{i})-f\_{i}(\mathrm{VaR}\_{\alpha\_{i}}(X\_{i})) and bi=VaRαi​(Xi),i=1,2.b\_{i}=\mathrm{VaR}\_{\alpha\_{i}}(X\_{i}),\penalty 10000\ i=1,2.
Using the above ai,bia\_{i},b\_{i}, we have fi​(VaRαi​(Xi))=lai,bi​(VaRαi​(Xi))f\_{i}(\mathrm{VaR}\_{\alpha\_{i}}(X\_{i}))=l\_{a\_{i},b\_{i}}(\mathrm{VaR}\_{\alpha\_{i}}(X\_{i})) and fi​(x)⩾gai,bi​(x)f\_{i}(x)\geqslant g\_{a\_{i},b\_{i}}(x) for all x⩾0.x\geqslant 0. Hence, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | f1​(VaRα+t​(X1))−f1​(VaRα1​(X1))+f2​(VaR1−t​(X2))−f2​(VaRα2​(X2))\displaystyle f\_{1}(\mathrm{VaR}\_{\alpha+t}(X\_{1}))-f\_{1}(\mathrm{VaR}\_{\alpha\_{1}}(X\_{1}))+f\_{2}(\mathrm{VaR}\_{1-t}(X\_{2}))-f\_{2}(\mathrm{VaR}\_{\alpha\_{2}}(X\_{2})) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⩾\displaystyle\geqslant | ga1,b1​(VaRα+t​(X1))−ga1,b1​(VaRα1​(X1))+ga2,b2​(VaR1−t​(X2))−ga2,b2​(VaRα2​(X2)),\displaystyle g\_{a\_{1},b\_{1}}(\mathrm{VaR}\_{\alpha+t}(X\_{1}))-g\_{a\_{1},b\_{1}}(\mathrm{VaR}\_{\alpha\_{1}}(X\_{1}))+g\_{a\_{2},b\_{2}}(\mathrm{VaR}\_{1-t}(X\_{2}))-g\_{a\_{2},b\_{2}}(\mathrm{VaR}\_{\alpha\_{2}}(X\_{2})), |  |

which implies

|  |  |  |
| --- | --- | --- |
|  | inf(f1,f2)∈ℐ2V​(𝐟)⩾inf(a1,a2,b1,b2)∈𝒜inft∈[0,1−α]G¯1​(a1,a2,b1,b2,t).\inf\_{(f\_{1},f\_{2})\in\mathcal{I}^{2}}V(\mathbf{f})\geqslant\inf\_{(a\_{1},a\_{2},b\_{1},b\_{2})\in\mathcal{A}}\inf\_{t\in[0,1-\alpha]}\overline{G}\_{1}(a\_{1},a\_{2},b\_{1},b\_{2},t). |  |

The inverse inequality holds trivially. We complete the proof.
∎

## Appendix D Proofs of Section [5](https://arxiv.org/html/2512.11430v1#S5 "5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty")

###### Proof of Proposition [5](https://arxiv.org/html/2512.11430v1#Thmproposition5 "Proposition 5. ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty").

Since {Xi}i=1n\{X\_{i}\}\_{i=1}^{n} are independent random variables, and fi​(Xi)f\_{i}(X\_{i}) depends only on XiX\_{i}, the sequence {fi​(Xi)}i=1n\{f\_{i}(X\_{i})\}\_{i=1}^{n} is also a sequence of independent random variables.
Since each fif\_{i} is 1-Lipschitz continuous, and 𝔼​[Xi2]<∞\mathbb{E}[X\_{i}^{2}]<\infty, we have 𝔼​[fi​(Xi)2]⩽𝔼​[Xi2]<∞.\mathbb{E}[f\_{i}(X\_{i})^{2}]\leqslant\mathbb{E}[X\_{i}^{2}]<\infty.
Hence, Var​(fi​(Xi))=𝔼​[fi​(Xi)2]−(𝔼​[fi​(Xi)])2\mathrm{Var}(f\_{i}(X\_{i}))=\mathbb{E}[f\_{i}(X\_{i})^{2}]-(\mathbb{E}[f\_{i}(X\_{i})])^{2} exists and is finite.
Define

|  |  |  |
| --- | --- | --- |
|  | Zn=Sn−𝔼​[Sn]Var​(Sn).Z\_{n}=\frac{S\_{n}-\mathbb{E}[S\_{n}]}{\sqrt{\mathrm{Var}(S\_{n})}}. |  |

We aim to show that Zn→𝑑𝒩​(0,1).Z\_{n}\xrightarrow{d}\mathcal{N}(0,1). Note that
𝔼​[Sn]=∑i=1n𝔼​[fi​(Xi)],\mathbb{E}[S\_{n}]=\sum\_{i=1}^{n}\mathbb{E}[f\_{i}(X\_{i})], and
Var​(Sn)=∑i=1nVar​(fi​(Xi)).\mathrm{Var}(S\_{n})=\sum\_{i=1}^{n}\mathrm{Var}(f\_{i}(X\_{i})).

To verify the Lindeberg condition (see, e.g., Billingsley, [1995](https://arxiv.org/html/2512.11430v1#bib.bib7), Theorem 27.3), recall that for any ε>0\varepsilon>0,

|  |  |  |
| --- | --- | --- |
|  | 1Var​(Sn)​∑i=1n𝔼​[(fi​(Xi)−𝔼​[fi​(Xi)])2​𝕀{|fi​(Xi)−𝔼​[fi​(Xi)]|>ε​Var​(Sn)}]→0,n→∞.\frac{1}{\mathrm{Var}(S\_{n})}\sum\_{i=1}^{n}\mathbb{E}\Big[(f\_{i}(X\_{i})-\mathbb{E}[f\_{i}(X\_{i})])^{2}\,\mathbb{I}\_{\{|f\_{i}(X\_{i})-\mathbb{E}[f\_{i}(X\_{i})]|>\varepsilon\sqrt{\mathrm{Var}(S\_{n})}\}}\Big]\to 0,\quad n\to\infty. |  |

Using the 1-Lipschitz property of fif\_{i}, we have
|fi​(Xi)−fi​(μ)|⩽|Xi−μ|,|f\_{i}(X\_{i})-f\_{i}(\mu)|\leqslant|X\_{i}-\mu|,
which implies

|  |  |  |
| --- | --- | --- |
|  | |fi​(Xi)−𝔼​[fi​(Xi)]|=|fi​(Xi)−fi​(μ)+fi​(μ)−𝔼​[fi​(Xi)]|⩽|Xi−μ|+𝔼​[|Xi−μ|].|f\_{i}(X\_{i})-\mathbb{E}[f\_{i}(X\_{i})]|=|f\_{i}(X\_{i})-f\_{i}(\mu)+f\_{i}(\mu)-\mathbb{E}[f\_{i}(X\_{i})]|\leqslant|X\_{i}-\mu|+\mathbb{E}[|X\_{i}-\mu|]. |  |

Define

|  |  |  |
| --- | --- | --- |
|  | Ai:={|fi​(Xi)−𝔼​[fi​(Xi)]|>ε​Var​(Sn)},Bi:={|Xi−μ|+𝔼​[|Xi−μ|]>ε​Var​(Sn)}.A\_{i}:=\{|f\_{i}(X\_{i})-\mathbb{E}[f\_{i}(X\_{i})]|>\varepsilon\sqrt{\mathrm{Var}(S\_{n})}\},\quad B\_{i}:=\{|X\_{i}-\mu|+\mathbb{E}[|X\_{i}-\mu|]>\varepsilon\sqrt{\mathrm{Var}(S\_{n})}\}. |  |

Then it is clear that Ai⊆BiA\_{i}\subseteq B\_{i}. Note that

|  |  |  |
| --- | --- | --- |
|  | Var​(Sn)=∑i=1n𝔼​[(fi​(Xi)−𝔼​[fi​(Xi)])2].\mathrm{Var}(S\_{n})=\sum\_{i=1}^{n}\mathbb{E}[(f\_{i}(X\_{i})-\mathbb{E}[f\_{i}(X\_{i})])^{2}]. |  |

Hence, we can bound the Lindeberg term as

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 1Var​(Sn)​∑i=1n𝔼​[(fi​(Xi)−𝔼​[fi​(Xi)])2​𝕀Ai]\displaystyle\frac{1}{\mathrm{Var}(S\_{n})}\sum\_{i=1}^{n}\mathbb{E}\big[(f\_{i}(X\_{i})-\mathbb{E}[f\_{i}(X\_{i})])^{2}\,\mathbb{I}\_{A\_{i}}\big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑i=1n𝔼​[(fi​(Xi)−𝔼​[fi​(Xi)])2]Var​(Sn)⋅𝔼​[(fi​(Xi)−𝔼​[fi​(Xi)])2​𝕀Ai]𝔼​[(fi​(Xi)−𝔼​[fi​(Xi)])2]\displaystyle=\sum\_{i=1}^{n}\frac{\mathbb{E}[(f\_{i}(X\_{i})-\mathbb{E}[f\_{i}(X\_{i})])^{2}]}{\mathrm{Var}(S\_{n})}\cdot\frac{\mathbb{E}[(f\_{i}(X\_{i})-\mathbb{E}[f\_{i}(X\_{i})])^{2}\,\mathbb{I}\_{A\_{i}}]}{\mathbb{E}[(f\_{i}(X\_{i})-\mathbb{E}[f\_{i}(X\_{i})])^{2}]} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⩽maxi∈[n]⁡𝔼​[(fi​(Xi)−𝔼​[fi​(Xi)])2​𝕀Ai]𝔼​[(fi​(Xi)−𝔼​[fi​(Xi)])2].\displaystyle\leqslant\max\_{i\in[n]}\frac{\mathbb{E}[(f\_{i}(X\_{i})-\mathbb{E}[f\_{i}(X\_{i})])^{2}\,\mathbb{I}\_{A\_{i}}]}{\mathbb{E}[(f\_{i}(X\_{i})-\mathbb{E}[f\_{i}(X\_{i})])^{2}]}. |  |

It is easy to verify that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|Xi−μ|]⩽2​𝔼​[Xi]<∞,𝔼​[|Xi−μ|2]⩽4​𝔼​[Xi2]<∞.\mathbb{E}[|X\_{i}-\mu|]\leqslant 2\mathbb{E}[X\_{i}]<\infty,\quad\mathbb{E}[|X\_{i}-\mu|^{2}]\leqslant 4\mathbb{E}[X\_{i}^{2}]<\infty. |  |

Hence,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[(fi​(Xi)−𝔼​[fi​(Xi)])2]⩽𝔼​[(|Xi−μ|+𝔼​[|Xi−μ|])2]<∞.\mathbb{E}\big[(f\_{i}(X\_{i})-\mathbb{E}[f\_{i}(X\_{i})])^{2}\big]\leqslant\mathbb{E}\big[(|X\_{i}-\mu|+\mathbb{E}[|X\_{i}-\mu|])^{2}\big]<\infty. |  |

If fif\_{i} is a constant function, then fi​(Xi)−𝔼​[fi​(Xi)]≡0f\_{i}(X\_{i})-\mathbb{E}[f\_{i}(X\_{i})]\equiv 0.
The convention 0/0=00/0=0 ensures that this case does not cause any issues. Clearly,

|  |  |  |
| --- | --- | --- |
|  | 0⩽𝔼​[(fi​(Xi)−𝔼​[fi​(Xi)])2​𝕀Ai]𝔼​[(fi​(Xi)−𝔼​[fi​(Xi)])2]⩽1.0\leqslant\frac{\mathbb{E}[(f\_{i}(X\_{i})-\mathbb{E}[f\_{i}(X\_{i})])^{2}\,\mathbb{I}\_{A\_{i}}]}{\mathbb{E}[(f\_{i}(X\_{i})-\mathbb{E}[f\_{i}(X\_{i})])^{2}]}\leqslant 1. |  |

Since Var​(Sn)→∞\mathrm{Var}(S\_{n})\to\infty as n→∞n\to\infty,
using Markov’s inequality, we have

|  |  |  |
| --- | --- | --- |
|  | ℙ​(|Xi−μ|+𝔼​[|Xi−μ|]>ε​Var​(Sn))⩽2​𝔼​[|Xi−μ|]ε​Var​(Sn)→0,n→∞.\mathbb{P}\big(|X\_{i}-\mu|+\mathbb{E}[|X\_{i}-\mu|]>\varepsilon\sqrt{\mathrm{Var}(S\_{n})}\big)\leqslant\frac{2\mathbb{E}[|X\_{i}-\mu|]}{\varepsilon\sqrt{\mathrm{Var}(S\_{n})}}\to 0,\quad n\to\infty. |  |

Since Ai⊆BiA\_{i}\subseteq B\_{i}, it follows that ℙ​(Ai)⩽ℙ​(Bi)→0\mathbb{P}(A\_{i})\leqslant\mathbb{P}(B\_{i})\to 0.
By the Monotone Convergence Theorem,

|  |  |  |
| --- | --- | --- |
|  | limn→∞𝔼​[(fi​(Xi)−𝔼​[fi​(Xi)])2​𝕀Ai]𝔼​[(fi​(Xi)−𝔼​[fi​(Xi)])2]=𝔼​[limn→∞(fi​(Xi)−𝔼​[fi​(Xi)])2​𝕀Ai]𝔼​[(fi​(Xi)−𝔼​[fi​(Xi)])2]=0.\lim\_{n\to\infty}\frac{\mathbb{E}[(f\_{i}(X\_{i})-\mathbb{E}[f\_{i}(X\_{i})])^{2}\,\mathbb{I}\_{A\_{i}}]}{\mathbb{E}[(f\_{i}(X\_{i})-\mathbb{E}[f\_{i}(X\_{i})])^{2}]}=\frac{\mathbb{E}[\lim\_{n\to\infty}(f\_{i}(X\_{i})-\mathbb{E}[f\_{i}(X\_{i})])^{2}\,\mathbb{I}\_{A\_{i}}]}{\mathbb{E}[(f\_{i}(X\_{i})-\mathbb{E}[f\_{i}(X\_{i})])^{2}]}=0. |  |

Thus, the Lindeberg condition holds for each i∈[n]i\in[n].
Since {fi​(Xi)}i=1n\{f\_{i}(X\_{i})\}\_{i=1}^{n} are independent with finite variances, the Central Limit Theorem implies

|  |  |  |
| --- | --- | --- |
|  | Zn=Sn−𝔼​[Sn]Var​(Sn)→𝑑𝒩​(0,1).Z\_{n}=\frac{S\_{n}-\mathbb{E}[S\_{n}]}{\sqrt{\mathrm{Var}(S\_{n})}}\xrightarrow{d}\mathcal{N}(0,1). |  |

We complete the proof.
∎

###### Proof of Theorem [3](https://arxiv.org/html/2512.11430v1#Thmtheorem3 "Theorem 3. ‣ 5.1 The results for RVaR ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty").

Let M=1α​∫α¯β¯Φ−1​(γ)​dγ.M=\frac{1}{\alpha}\int\_{\bar{\alpha}}^{\bar{\beta}}\Phi^{-1}(\gamma)\mathrm{d}\gamma.
We prove the result in the following three steps:

Step 1: For any fi∈ℐ,f\_{i}\in\mathcal{I}, let

|  |  |  |
| --- | --- | --- |
|  | kfi​(x)≜{fi​(x),0⩽x⩽VaRα¯i​(X),min⁡{x+fi​(VaRα¯i​(X))−VaRα¯i​(X),bi},x>VaRα¯i​(X),k\_{f\_{i}}(x)\triangleq\begin{cases}f\_{i}(x),&0\leqslant x\leqslant\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X),\\ \min\left\{x+f\_{i}\left(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X)\right)-\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X),b\_{i}\right\},&x>\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X),\end{cases} |  |

where bi⩾fi​(VaRα¯i​(X))b\_{i}\geqslant f\_{i}\left(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X)\right) is determined by ESα¯i​(fi​(X))=ESα¯i​(kfi​(X)).\mathrm{ES}\_{\bar{\alpha}\_{i}}(f\_{i}(X))=\mathrm{ES}\_{\bar{\alpha}\_{i}}\left(k\_{f\_{i}}(X)\right). Note that

|  |  |  |
| --- | --- | --- |
|  | fi​(x)⩽x−VaRα¯i​(X)+fi​(VaRα​(X)),∀x⩾VaRα¯i⁡(X).f\_{i}(x)\leqslant x-\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X)+f\_{i}\left(\mathrm{VaR}\_{\alpha}(X)\right),\quad\forall x\geqslant\operatorname{VaR}\_{\bar{\alpha}\_{i}}(X). |  |

Then,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESα¯i​(fi​(X))\displaystyle\mathrm{ES}\_{\bar{\alpha}\_{i}}(f\_{i}(X)) | =1αi+βi​∫α¯i1VaRs⁡(fi​(X))​ds=1αi+βi​∫α¯i1fi​(VaRs​(X))​ds\displaystyle=\frac{1}{\alpha\_{i}+\beta\_{i}}\int\_{\bar{\alpha}\_{i}}^{1}\operatorname{VaR}\_{s}(f\_{i}(X))\mathrm{d}s=\frac{1}{\alpha\_{i}+\beta\_{i}}\int\_{\bar{\alpha}\_{i}}^{1}f\_{i}\left(\mathrm{VaR}\_{s}(X)\right)\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⩽1αi+βi​∫α¯i1(VaRs⁡(X)−VaRα¯i⁡(X)+f​(VaRα¯i​(X)))​ds.\displaystyle\leqslant\frac{1}{\alpha\_{i}+\beta\_{i}}\int\_{\bar{\alpha}\_{i}}^{1}\left(\operatorname{VaR}\_{s}(X)-\operatorname{VaR}\_{\bar{\alpha}\_{i}}(X)+f\left(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X)\right)\right)\mathrm{d}s. |  |

Thus, there exists bi⩾fi​(VaRα​(X))b\_{i}\geqslant f\_{i}\left(\mathrm{VaR}\_{\alpha}(X)\right) such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESα¯i​(fi​(X))\displaystyle\mathrm{ES}\_{\bar{\alpha}\_{i}}(f\_{i}(X)) | =1αi+βi​∫α¯i1min⁡{VaRs⁡(X)−VaRα¯i⁡(X)+fi​(VaRα¯i​(X)),bi}​ds\displaystyle=\frac{1}{\alpha\_{i}+\beta\_{i}}\int\_{\bar{\alpha}\_{i}}^{1}\min\{\operatorname{VaR}\_{s}(X)-\operatorname{VaR}\_{\bar{\alpha}\_{i}}(X)+f\_{i}\left(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X)\right),b\_{i}\}\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ESα¯i​(kfi​(X)).\displaystyle=\mathrm{ES}\_{\bar{\alpha}\_{i}}\left(k\_{f\_{i}}(X)\right). |  |

In conjunction with
ESβ¯i​(fi​(X))⩾ESβ¯i​(kfi​(X)),\mathrm{ES}\_{\bar{\beta}\_{i}}(f\_{i}(X))\geqslant\mathrm{ES}\_{\bar{\beta}\_{i}}(k\_{f\_{i}}(X)),
this yields
RVaRβi,αi​(fi​(X))⩽RVaRβi,αi​(kfi​(X)).\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(f\_{i}(X))\leqslant\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(k\_{f\_{i}}(X)).
Next, we demonstrate 𝔼​[kfi​(X)]=𝔼​[fi​(X)].\mathbb{E}\left[k\_{f\_{i}}(X)\right]=\mathbb{E}[f\_{i}(X)]. Let UU be uniformly distributed on [0,1],[0,1], then

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[fi​(X)]\displaystyle\mathbb{E}[f\_{i}(X)] | =𝔼​[VaRU​(fi​(X))]=𝔼​[fi​(VaRU​(X))]\displaystyle=\mathbb{E}\left[\mathrm{VaR}\_{U}(f\_{i}(X))\right]=\mathbb{E}\left[f\_{i}\left(\mathrm{VaR}\_{U}(X)\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0α¯ifi​(VaRs​(X))​ds+∫α¯i1fi​(VaRs​(X))​ds\displaystyle=\int\_{0}^{\bar{\alpha}\_{i}}f\_{i}\left(\mathrm{VaR}\_{s}(X)\right)\mathrm{d}s+\int\_{\bar{\alpha}\_{i}}^{1}f\_{i}\left(\mathrm{VaR}\_{s}(X)\right)\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0α¯ikfi​(VaRs​(X))​ds+(αi+βi)​ESα¯i​(fi​(X))\displaystyle=\int\_{0}^{\bar{\alpha}\_{i}}k\_{f\_{i}}\left(\mathrm{VaR}\_{s}(X)\right)\mathrm{d}s+(\alpha\_{i}+\beta\_{i})\mathrm{ES}\_{\bar{\alpha}\_{i}}(f\_{i}(X)) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0α¯ikfi​(VaRs​(X))​ds+(αi+βi)​ESα¯i​(kfi​(X))=𝔼​[kfi​(X)].\displaystyle=\int\_{0}^{\bar{\alpha}\_{i}}k\_{f\_{i}}\left(\mathrm{VaR}\_{s}(X)\right)\mathrm{d}s+(\alpha\_{i}+\beta\_{i})\mathrm{ES}\_{\bar{\alpha}\_{i}}(k\_{f\_{i}}(X))=\mathbb{E}\left[k\_{f\_{i}}(X)\right]. |  |

Finally, by setting t0=bit\_{0}=b\_{i} in Lemma [3](https://arxiv.org/html/2512.11430v1#Thmlemma3 "Lemma 3. ‣ 5.1 The results for RVaR ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty"), let G​(x)=(x−𝔼​[fi​(Xi)])2,G(x)=(x-\mathbb{E}\big[f\_{i}(X\_{i})\big])^{2}, we have
ℙ​(kfi​(X)⩽t)⩽ℙ​(fi​(X)⩽t),\mathbb{P}(k\_{f\_{i}}(X)\leqslant t)\leqslant\mathbb{P}(f\_{i}(X)\leqslant t), for t<bit<b\_{i} and ℙ​(kfi​(X)>t)⩽ℙ​(fi​(X)>t)\mathbb{P}(k\_{f\_{i}}(X)>t)\leqslant\mathbb{P}(f\_{i}(X)>t) for t⩾bit\geqslant b\_{i}, then kfi​(X)⩽c​xfi​(X).k\_{f\_{i}}(X)\leqslant\_{cx}f\_{i}(X). Then by Lemma [3](https://arxiv.org/html/2512.11430v1#Thmlemma3 "Lemma 3. ‣ 5.1 The results for RVaR ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty"), we know that Var​(kfi​(X))⩽Var​(fi​(X)).\mathrm{Var}(k\_{f\_{i}}(X))\leqslant\mathrm{Var}(f\_{i}(X)).

Step 2: Let 0⩽ci⩽fi​(VaRα¯i​(X))0\leqslant c\_{i}\leqslant f\_{i}(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X)) and di=VaRα¯i​(X)−fi​(VaRα¯i​(X))+ci.d\_{i}=\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X)-f\_{i}(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X))+c\_{i}. Define

|  |  |  |
| --- | --- | --- |
|  | k~fi(x,ci)={kfi​(x),x>VaRα¯i​(X),x∧ci+(x−di)+,x⩽VaRα¯i​(X).\widetilde{k}\_{f\_{i}}(x,c\_{i})=\left\{\begin{aligned} &k\_{f\_{i}}(x),&x>\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X),\\ &x\wedge c\_{i}+(x-d\_{i})\_{+},&x\leqslant\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X).\end{aligned}\right. |  |

It is straightforward to verify that 0=k~fi​(x,0)⩽kfi​(x)0=\widetilde{k}\_{f\_{i}}(x,0)\leqslant k\_{f\_{i}}(x) and k~fi​(x,fi​(VaRα¯i​(X)))⩾kfi​(x).\widetilde{k}\_{f\_{i}}(x,f\_{i}(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X)))\geqslant k\_{f\_{i}}(x). Further, since k~fi​(x,ci)\widetilde{k}\_{f\_{i}}(x,c\_{i}) is increasing and continuous with respect to ci,c\_{i}, then there exists a ci∗∈[0,fi​(VaRα¯i​(X))]c\_{i}^{\*}\in[0,f\_{i}(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X))] such that 𝔼​[k~fi​(X,ci∗)]=𝔼​[kfi​(X)].\mathbb{E}[\widetilde{k}\_{f\_{i}}(X,c^{\*}\_{i})]=\mathbb{E}[k\_{f\_{i}}(X)].

Moreover, for y<ci∗,y<c\_{i}^{\*}, we have ℙ​(k~fi​(X,ci∗)⩽y)⩽ℙ​(kfi​(X)⩽y).\mathbb{P}(\widetilde{k}\_{f\_{i}}(X,c^{\*}\_{i})\leqslant y)\leqslant\mathbb{P}(k\_{f\_{i}}(X)\leqslant y). Let di∗=VaRα¯i​(X)−fi​(VaRα¯i​(X))+ci∗,d\_{i}^{\*}=\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X)-f\_{i}(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X))+c^{\*}\_{i}, then for y⩾ci∗,y\geqslant c^{\*}\_{i},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(k~fi​(X,ci∗)>y)=\displaystyle\mathbb{P}(\widetilde{k}\_{f\_{i}}(X,c^{\*}\_{i})>y)= | ℙ​(X⩾ci∗,k~fi​(X,ci∗)>y)\displaystyle\mathbb{P}(X\geqslant c^{\*}\_{i},\widetilde{k}\_{f\_{i}}(X,c^{\*}\_{i})>y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ℙ(X>VaRα¯i(X),kfi(X)>y)+ℙ(ci∗⩽X⩽VaRα¯i(X),X−di∗+ci∗>y)\displaystyle\mathbb{P}(X>\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X),k\_{f\_{i}}(X)>y)+\mathbb{P}(c\_{i}^{\*}\leqslant X\leqslant\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X),X-d^{\*}\_{i}+c^{\*}\_{i}>y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⩽\displaystyle\leqslant | ℙ(X>VaRα¯i(X),kfi(X)>y)+ℙ(ci∗⩽X⩽VaRα¯i(X),kfi(X)>y)\displaystyle\mathbb{P}(X>\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X),k\_{f\_{i}}(X)>y)+\mathbb{P}\left(c\_{i}^{\*}\leqslant X\leqslant\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X),k\_{f\_{i}}(X)>y\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ℙ​(kfi​(X)>y).\displaystyle\mathbb{P}(k\_{f\_{i}}(X)>y). |  |

Then by Lemma [3](https://arxiv.org/html/2512.11430v1#Thmlemma3 "Lemma 3. ‣ 5.1 The results for RVaR ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty"), we know that Var​(k~fi​(X,ci∗))⩽Var​(kfi​(X)).\mathrm{Var}(\widetilde{k}\_{f\_{i}}(X,c^{\*}\_{i}))\leqslant\mathrm{Var}(k\_{f\_{i}}(X)).

Step 3: Define

|  |  |  |
| --- | --- | --- |
|  | kfi∗​(x,ai)=(x−ai)+∧(VaRα¯i​(X)−fi​(VaRα¯i​(X))+bi−ai)k^{\*}\_{f\_{i}}(x,a\_{i})=(x-a\_{i})\_{+}\wedge(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X)-f\_{i}(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X))+b\_{i}-a\_{i}) |  |

with 0⩽ai⩽VaRα¯i​(X).0\leqslant a\_{i}\leqslant\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X).
Let θi∈[0,1],\theta\_{i}\in[0,1], θ¯i=1−θi\bar{\theta}\_{i}=1-\theta\_{i} and γi∈[0,1],\gamma\_{i}\in[0,1], such that

|  |  |  |
| --- | --- | --- |
|  | VaRθi(X)=(VaRα¯i(X)−fi(VaRα¯i(X))+bi,\mathrm{VaR}\_{\theta\_{i}}(X)=(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X)-f\_{i}(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X))+b\_{i}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | VaRγi(X)=(VaRα¯i(X)−fi(VaRα¯i(X)).\mathrm{VaR}\_{\gamma\_{i}}(X)=(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X)-f\_{i}(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X)). |  |

Then we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​[kfi∗​(RVaRβi,αi​(X),ai)−kfi∗​(X,ai)]\displaystyle\mathbb{E}[k^{\*}\_{f\_{i}}(\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X),a\_{i})-k^{\*}\_{f\_{i}}(X,a\_{i})] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle=\penalty 10000 | RVaRβi,αi​(X)−ai−𝔼​[(X−ai)+∧(VaRγi​(X)+bi−ai)]\displaystyle\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X)-a\_{i}-\mathbb{E}[(X-a\_{i})\_{+}\wedge(\mathrm{VaR}\_{\gamma\_{i}}(X)+b\_{i}-a\_{i})] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle=\penalty 10000 | 𝔼​[(RVaRβi,αi​(X)−ai)∧max⁡(RVaRβi,αi​(X)−X,RVaRβi,αi​(X)−VaRθi​(X))]\displaystyle\mathbb{E}[(\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X)-a\_{i})\wedge\max(\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X)-X,\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X)-\mathrm{VaR}\_{\theta\_{i}}(X))] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | :=\displaystyle=\penalty 10000 | g​(ai).\displaystyle g(a\_{i}). |  |

It is clear that

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(VaRγi​(X))=\displaystyle g(\mathrm{VaR}\_{\gamma\_{i}}(X))= | RVaRβi,αi(X)−𝔼[X𝟙{VaRγi​(X)⩽X⩽VaRθi​(X)}]−γi(VaRγi(X)−θ¯iVaRθi(X),\displaystyle\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X)-\mathbb{E}[X\mathds{1}\_{\{\mathrm{VaR}\_{\gamma\_{i}}(X)\leqslant X\leqslant\mathrm{VaR}\_{\theta\_{i}}(X)\}}]-\gamma\_{i}(\mathrm{VaR}\_{\gamma\_{i}}(X)-\bar{\theta}\_{i}\mathrm{VaR}\_{\theta\_{i}}(X), |  |

and

|  |  |  |
| --- | --- | --- |
|  | g​(VaRα¯i​(X))=RVaRβi,αi​(X)−α¯i​VaRα¯i​(X)−𝔼​[X​𝟙{VaRα¯i​(X)⩽X⩽VaRθi​(X)}]−θ¯i​VaRθi​(X).g(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X))=\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X)-\bar{\alpha}\_{i}\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X)-\mathbb{E}[X\mathds{1}\_{\{\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X)\leqslant X\leqslant\mathrm{VaR}\_{\theta\_{i}}(X)\}}]-\bar{\theta}\_{i}\mathrm{VaR}\_{\theta\_{i}}(X). |  |

Also, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​[k~fi​(RVaRβi,αi​(X),ci∗)−k~fi​(X,ci∗)]\displaystyle\mathbb{E}[\widetilde{k}\_{f\_{i}}(\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X),c^{\*}\_{i})-\widetilde{k}\_{f\_{i}}(X,c^{\*}\_{i})] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle=\penalty 10000 | RVaRβi,αi​(X)−VaRα¯i​(X)+fi​(VaRα¯i​(X))−𝔼​[k~fi​(X,ci∗)]\displaystyle\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X)-\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X)+f\_{i}(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X))-\mathbb{E}[\widetilde{k}\_{f\_{i}}(X,c^{\*}\_{i})] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle=\penalty 10000 | RVaRβi,αi​(X)−𝔼​[X+VaRα¯i​(X)−fi​(VaRα¯i​(X))​𝟙{X∈[0,ci∗]}]\displaystyle\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X)-\mathbb{E}[X+\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X)-f\_{i}(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X))\mathds{1}\_{\{X\in[0,c^{\*}\_{i}]\}}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −𝔼​[X​𝟙{X∈[di∗,VaRθi​(X)]}]−di∗​(FX​(di∗)−FX​(ci∗))−θ¯i​VaRθi​(X).\displaystyle-\mathbb{E}[X\mathds{1}\_{\{X\in[d\_{i}^{\*},\mathrm{VaR}\_{\theta\_{i}}(X)]\}}]-d\_{i}^{\*}(F\_{X}(d\_{i}^{\*})-F\_{X}(c\_{i}^{\*}))-\bar{\theta}\_{i}\mathrm{VaR}\_{\theta\_{i}}(X). |  |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | g(VaRα¯i(X)−fi(VaRα¯i(X))⩾𝔼[k~fi(RVaRβi,αi(X),ci∗)−k~fi(X,ci∗)]⩾g(VaRα¯i(X)).\displaystyle g(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X)-f\_{i}(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X))\geqslant\mathbb{E}[\widetilde{k}\_{f\_{i}}(\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X),c^{\*}\_{i})-\widetilde{k}\_{f\_{i}}(X,c^{\*}\_{i})]\geqslant g(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X)). |  |

Together with the fact that g​(ai)g(a\_{i}) is decreasing and continuous with respect to ai,a\_{i}, then there exist VaRα¯i​(X)−fi​(VaRα¯i​(X))⩽ai∗⩽VaRα¯i​(X)\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X)-f\_{i}(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X))\leqslant a^{\*}\_{i}\leqslant\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X) such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[kfi∗​(RVaRβi,αi​(X),ai∗)−kfi∗​(X,ai∗)]=𝔼​[k~fi​(RVaRβi,αi​(X),ci∗)−k~fi​(X,ci∗)].\mathbb{E}[k^{\*}\_{f\_{i}}(\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X),a^{\*}\_{i})-k^{\*}\_{f\_{i}}(X,a^{\*}\_{i})]=\mathbb{E}[\widetilde{k}\_{f\_{i}}(\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X),c^{\*}\_{i})-\widetilde{k}\_{f\_{i}}(X,c^{\*}\_{i})]. |  |

For y<RVaRβi,αi​(X)−ai∗,y<\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X)-a\_{i}^{\*}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ℙ​(kfi∗​(RVaRβi,αi​(X),ai∗)−kfi∗​(X,ai∗)⩽y)\displaystyle\mathbb{P}(k^{\*}\_{f\_{i}}(\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X),a^{\*}\_{i})-k^{\*}\_{f\_{i}}(X,a^{\*}\_{i})\leqslant y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ℙ​(X⩾ai∗,kfi∗​(RVaRβi,αi​(X),ai∗)−kfi∗​(X,ai∗)⩽y)\displaystyle\penalty 10000\ \mathbb{P}(X\geqslant a\_{i}^{\*},k^{\*}\_{f\_{i}}(\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X),a^{\*}\_{i})-k^{\*}\_{f\_{i}}(X,a^{\*}\_{i})\leqslant y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ℙ​(X>VaRα¯i​(X),k~fi​(RVaRβi,αi​(X),ci∗)−k~fi​(X,ci∗)⩽y)\displaystyle\penalty 10000\ \mathbb{P}(X>\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X),\widetilde{k}\_{f\_{i}}(\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X),c^{\*}\_{i})-\widetilde{k}\_{f\_{i}}(X,c^{\*}\_{i})\leqslant y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +ℙ(ai∗⩽X⩽VaRα¯i(X),RVaRβi,αi(X)−X⩽y)\displaystyle+\mathbb{P}(a\_{i}^{\*}\leqslant X\leqslant\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X),\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X)-X\leqslant y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⩽\displaystyle\leqslant | ℙ​(X>VaRα¯i​(X),k~fi​(RVaRβi,αi​(X),ci∗)−k~fi​(X,ci∗)⩽y)\displaystyle\penalty 10000\ \mathbb{P}(X>\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X),\widetilde{k}\_{f\_{i}}(\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X),c^{\*}\_{i})-\widetilde{k}\_{f\_{i}}(X,c^{\*}\_{i})\leqslant y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +ℙ(ai∗⩽X⩽VaRα¯i(X),k~fi(RVaRβi,αi(X),ci∗)−k~fi(X,ci∗)⩽y)\displaystyle+\mathbb{P}(a\_{i}^{\*}\leqslant X\leqslant\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X),\widetilde{k}\_{f\_{i}}(\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X),c^{\*}\_{i})-\widetilde{k}\_{f\_{i}}(X,c^{\*}\_{i})\leqslant y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ℙ​(k~fi​(RVaRβi,αi​(X),ci∗)−k~fi​(X,ci∗)⩽y).\displaystyle\penalty 10000\ \mathbb{P}(\widetilde{k}\_{f\_{i}}(\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X),c^{\*}\_{i})-\widetilde{k}\_{f\_{i}}(X,c^{\*}\_{i})\leqslant y). |  |

On the other hand, for y⩾RVaRβi,αi​(X)−ai∗,y\geqslant\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X)-a\_{i}^{\*}, we have

|  |  |  |
| --- | --- | --- |
|  | 0=ℙ​(kfi∗​(VaRα¯i​(X),ai∗)−kfi∗​(X,ai∗)>y)⩽ℙ​(k~fi​(VaRα¯i​(X),ci∗)−k~fi​(X,ci∗)>y).0=\mathbb{P}(k^{\*}\_{f\_{i}}(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X),a^{\*}\_{i})-k^{\*}\_{f\_{i}}(X,a^{\*}\_{i})>y)\leqslant\mathbb{P}(\widetilde{k}\_{f\_{i}}(\mathrm{VaR}\_{\bar{\alpha}\_{i}}(X),c^{\*}\_{i})-\widetilde{k}\_{f\_{i}}(X,c^{\*}\_{i})>y). |  |

Thus, we have

|  |  |  |
| --- | --- | --- |
|  | Var​(kfi∗​(RVaRβi,αi​(X),ai∗)−kfi∗​(X,ai∗))⩽Var​(k~fi​(RVaRβi,αi​(X),ci∗)−k~fi​(X,ci∗)).\mathrm{Var}\left(k^{\*}\_{f\_{i}}(\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X),a^{\*}\_{i})-k^{\*}\_{f\_{i}}(X,a^{\*}\_{i})\right)\leqslant\mathrm{Var}(\widetilde{k}\_{f\_{i}}\left(\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X),c^{\*}\_{i})-\widetilde{k}\_{f\_{i}}(X,c^{\*}\_{i})\right). |  |

To summarize,

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∑i=1n(RVaRβi,αi​(Xi)−RVaRβi,αi​(fi​(Xi))+𝔼​[fi​(Xi)])+M​(∑i=1nVar​(fi​(Xi)))1/2\displaystyle\sum\_{i=1}^{n}\left(\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X\_{i})-\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(f\_{i}(X\_{i}))+\mathbb{E}[f\_{i}(X\_{i})]\right)+M\left(\sum\_{i=1}^{n}\mathrm{Var}(f\_{i}(X\_{i}))\right)^{1/2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⩾\displaystyle\geqslant | ∑i=1n(RVaRβi,αi​(Xi)−RVaRβi,αi​(kfi​(Xi))+𝔼​[kfi​(Xi)])+M​(∑i=1nVar​(kfi​(Xi)))1/2\displaystyle\sum\_{i=1}^{n}\left(\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X\_{i})-\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(k\_{f\_{i}}(X\_{i}))+\mathbb{E}[k\_{f\_{i}}(X\_{i})]\right)+M\left(\sum\_{i=1}^{n}\mathrm{Var}(k\_{f\_{i}}(X\_{i}))\right)^{1/2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⩾\displaystyle\geqslant | ∑i=1n(RVaRβi,αi​(Xi)−RVaRβi,αi​(k~fi​(Xi,ci∗))+𝔼​[k~fi​(Xi,ci∗)])+M​(∑i=1nVar​(k~fi​(Xi,ci∗)))1/2\displaystyle\sum\_{i=1}^{n}\left(\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X\_{i})-\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(\widetilde{k}\_{f\_{i}}(X\_{i},c\_{i}^{\*}))+\mathbb{E}[\widetilde{k}\_{f\_{i}}(X\_{i},c\_{i}^{\*})]\right)+M\left(\sum\_{i=1}^{n}\mathrm{Var}(\widetilde{k}\_{f\_{i}}(X\_{i},c^{\*}\_{i}))\right)^{1/2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∑i=1n(RVaRβi,αi​(Xi)−(RVaRβi,αi​(k~fi​(Xi,ci∗))−𝔼​[k~fi​(Xi,ci∗)]))+M​(∑i=1nVar​(k~fi​(Xi,ci∗)))1/2\displaystyle\sum\_{i=1}^{n}\left(\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X\_{i})-\big(\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(\widetilde{k}\_{f\_{i}}(X\_{i},c\_{i}^{\*}))-\mathbb{E}[\widetilde{k}\_{f\_{i}}(X\_{i},c\_{i}^{\*})]\big)\right)+M\left(\sum\_{i=1}^{n}\mathrm{Var}(\widetilde{k}\_{f\_{i}}(X\_{i},c^{\*}\_{i}))\right)^{1/2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ⩾\displaystyle\geqslant | ∑i=1n(RVaRβi,αi​(Xi)−(RVaRβi,αi​(kfi∗​(Xi,ai∗))−𝔼​[kfi∗​(Xi,ai∗)]))+M​(∑i=1nVar​(kfi∗​(Xi,ai∗)))1/2\displaystyle\sum\_{i=1}^{n}\left(\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X\_{i})-\big(\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(k^{\*}\_{f\_{i}}(X\_{i},a^{\*}\_{i}))-\mathbb{E}[k^{\*}\_{f\_{i}}(X\_{i},a\_{i}^{\*})])\right)+M\left(\sum\_{i=1}^{n}\mathrm{Var}(k^{\*}\_{f\_{i}}(X\_{i},a^{\*}\_{i}))\right)^{1/2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∑i=1n(RVaRβi,αi​(Xi)−RVaRβi,αi​(kfi∗​(Xi,ai∗))+𝔼​[kfi∗​(Xi,ai∗)])+M​(∑i=1nVar​(kfi∗​(Xi,ai∗)))1/2,\displaystyle\sum\_{i=1}^{n}\left(\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(X\_{i})-\mathrm{RVaR}\_{\beta\_{i},\alpha\_{i}}(k^{\*}\_{f\_{i}}(X\_{i},a^{\*}\_{i}))+\mathbb{E}[k^{\*}\_{f\_{i}}(X\_{i},a\_{i}^{\*})]\right)+M\left(\sum\_{i=1}^{n}\mathrm{Var}(k^{\*}\_{f\_{i}}(X\_{i},a^{\*}\_{i}))\right)^{1/2}, |  |

which completes the proof.
∎

###### Proof of Proposition [7](https://arxiv.org/html/2512.11430v1#Thmproposition7 "Proposition 7. ‣ 5.2 The result for VaR ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty").

For any 𝐟=(f1,…,fn)∈ℐn\mathbf{f}=(f\_{1},\dots,f\_{n})\in\mathcal{I}^{n},
it is clear that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∑i=1nVaRαi​(Tfi,πi​(Xi))+VaRα​(R​(𝐟,π))\displaystyle\sum\_{i=1}^{n}\mathrm{VaR}\_{\alpha\_{i}}\left(T\_{f\_{i},\pi\_{i}}(X\_{i})\right)+\mathrm{VaR}\_{\alpha}\left(R(\mathbf{f},\pi)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑i=1nVaRαi​(Xi)−∑i=1nfi​(VaRαi​(Xi))+VaRα​(∑i=1nfi​(Xi)).\displaystyle=\sum\_{i=1}^{n}\mathrm{VaR}\_{\alpha\_{i}}(X\_{i})-\sum\_{i=1}^{n}f\_{i}\left(\mathrm{VaR}\_{\alpha\_{i}}(X\_{i})\right)+\mathrm{VaR}\_{\alpha}\left(\sum\_{i=1}^{n}f\_{i}(X\_{i})\right). |  |

Let ai=VaRαi​(Xi)−fi​(VaRαi​(Xi))a\_{i}=\mathrm{VaR}\_{\alpha\_{i}}(X\_{i})-f\_{i}(\mathrm{VaR}\_{\alpha\_{i}}(X\_{i})) and bi=VaRαi​(Xi).b\_{i}=\mathrm{VaR}\_{\alpha\_{i}}(X\_{i}). Then it follows that fi​(VaRαi​(Xi))=gai,bi​(VaRαi​(Xi))f\_{i}(\mathrm{VaR}\_{\alpha\_{i}}\left(X\_{i}\right))=g\_{a\_{i},b\_{i}}(\mathrm{VaR}\_{\alpha\_{i}}\left(X\_{i}\right)) and fi​(Xi)⩾gai,bi​(Xi),f\_{i}(X\_{i})\geqslant g\_{a\_{i},b\_{i}}(X\_{i}), which implies

|  |  |  |
| --- | --- | --- |
|  | −∑i=1ngai,bi​(VaRαi​(Xi))+VaRα​(∑i=1ngai,bi​(Xi))⩽−∑i=1nfi​(VaRαi​(Xi))+VaRα​(∑i=1nfi​(Xi)).-\sum\_{i=1}^{n}g\_{a\_{i},b\_{i}}\left(\mathrm{VaR}\_{\alpha\_{i}}(X\_{i})\right)+\mathrm{VaR}\_{\alpha}\left(\sum\_{i=1}^{n}g\_{a\_{i},b\_{i}}(X\_{i})\right)\leqslant-\sum\_{i=1}^{n}f\_{i}\left(\mathrm{VaR}\_{\alpha\_{i}}(X\_{i})\right)+\mathrm{VaR}\_{\alpha}\left(\sum\_{i=1}^{n}f\_{i}(X\_{i})\right). |  |

Then we get the desired result.
∎

###### Proof of Theorem [4](https://arxiv.org/html/2512.11430v1#Thmtheorem4 "Theorem 4. ‣ 5.2 The result for VaR ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty").

From Proposition [7](https://arxiv.org/html/2512.11430v1#Thmproposition7 "Proposition 7. ‣ 5.2 The result for VaR ‣ 5 Optimal solutions for i.i.d. risks ‣ Pareto-optimal reinsurance under dependence uncertainty"), we immediately obtain bi∗=VaRαi​(Xi)b^{\*}\_{i}=\mathrm{VaR}\_{\alpha\_{i}}(X\_{i}). Next, we establish the monotonicity properties of the auxiliary functions. Direct computation yields:

|  |  |  |
| --- | --- | --- |
|  | wi′​(ai)=−SXi​(ai)⩽0,and​vi′​(ai)=−2​wi​(ai)⩽0,w^{\prime}\_{i}(a\_{i})=-S\_{X\_{i}}(a\_{i})\leqslant 0,\quad\text{and}\quad v^{\prime}\_{i}(a\_{i})=-2w\_{i}(a\_{i})\leqslant 0, |  |

where SXi​(x)=1−FXi​(x)S\_{X\_{i}}(x)=1-F\_{X\_{i}}(x) is the survival function.
For any indemnity function fi=gai,bif\_{i}=g\_{a\_{i},b\_{i}}, the objective function becomes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(𝐚)\displaystyle F({\bf a}) | :=∑i=1nVaRαi​(Xi)−∑i=1nfi​(VaRαi​(Xi))+∑i=1n𝔼​[fi​(Xi)]+Φ−1​(α)​(∑i=1nvar​(fi​(Xi)))1/2\displaystyle=\sum\_{i=1}^{n}\mathrm{VaR}\_{\alpha\_{i}}(X\_{i})-\sum\_{i=1}^{n}f\_{i}(\mathrm{VaR}\_{\alpha\_{i}}(X\_{i}))+\sum\_{i=1}^{n}\mathbb{E}[f\_{i}(X\_{i})]+\Phi^{-1}(\alpha)\left(\sum\_{i=1}^{n}\mathrm{var}(f\_{i}(X\_{i}))\right)^{1/2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑i=1n(ai+wi​(ai))+Φ−1​(α)​(∑i=1n(vi​(ai)−wi​(ai)2))1/2.\displaystyle=\sum\_{i=1}^{n}(a\_{i}+w\_{i}(a\_{i}))+\Phi^{-1}(\alpha)\left(\sum\_{i=1}^{n}(v\_{i}(a\_{i})-w\_{i}(a\_{i})^{2})\right)^{1/2}. |  |

Applying the first-order condition, we compute:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂F​(𝐚)∂ai\displaystyle\frac{\partial F({\bf a})}{\partial a\_{i}} | =FXi​(ai)​(1−Φ−1​(α)​(∑j=1n(vj​(aj)−wj​(aj)2))−1/2​wi​(ai))\displaystyle=F\_{X\_{i}}(a\_{i})\left(1-\Phi^{-1}(\alpha)\left(\sum\_{j=1}^{n}\left(v\_{j}(a\_{j})-w\_{j}(a\_{j})^{2}\right)\right)^{-1/2}w\_{i}(a\_{i})\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =FXi​(ai)​(1−Φ−1​(α)​Gi​(𝐚)1/2),\displaystyle=F\_{X\_{i}}(a\_{i})\left(1-\Phi^{-1}(\alpha)G\_{i}({\bf a})^{1/2}\right), |  |

where

|  |  |  |
| --- | --- | --- |
|  | Gi​(𝐚)=wi​(ai)2∑j=1n(vj​(aj)−wj​(aj)2).G\_{i}({\bf a})=\frac{w\_{i}(a\_{i})^{2}}{\sum\_{j=1}^{n}\left(v\_{j}(a\_{j})-w\_{j}(a\_{j})^{2}\right)}. |  |

This implies

|  |  |  |
| --- | --- | --- |
|  | ∂F​(𝐚)∂ai⩾0⟺1−Φ−1​(α)​Gi​(𝐚)1/2⩾0.\frac{\partial F({\bf a})}{\partial a\_{i}}\geqslant 0\quad\Longleftrightarrow\quad 1-\Phi^{-1}(\alpha)G\_{i}({\bf a})^{1/2}\geqslant 0. |  |

To establish the monotonicity of Gi​(𝐚)G\_{i}({\bf a}), consider the function

|  |  |  |  |
| --- | --- | --- | --- |
|  | gi​(ai)\displaystyle g\_{i}(a\_{i}) | :=wi​(ai)2−SXi​(ai)​vi​(ai)\displaystyle=w\_{i}(a\_{i})^{2}-S\_{X\_{i}}(a\_{i})v\_{i}(a\_{i}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(∫aiVaRαi​(Xi)SXi​(x)​dx)2−2​SXi​(ai)​∫aiVaRαi​(Xi)(x−ai)​SXi​(x)​dx.\displaystyle=\left(\int\_{a\_{i}}^{\mathrm{VaR}\_{\alpha\_{i}}(X\_{i})}S\_{X\_{i}}(x)\mathrm{d}x\right)^{2}-2S\_{X\_{i}}(a\_{i})\int\_{a\_{i}}^{\mathrm{VaR}\_{\alpha\_{i}}(X\_{i})}(x-a\_{i})S\_{X\_{i}}(x)\mathrm{d}x. |  |

We observe that gi​(VaRαi​(Xi))=0g\_{i}(\mathrm{VaR}\_{\alpha\_{i}}(X\_{i}))=0 and

|  |  |  |
| --- | --- | --- |
|  | ∂gi​(ai)∂ai=∂FXi​(ai)∂ai​vi​(ai)⩾0,\frac{\partial g\_{i}(a\_{i})}{\partial a\_{i}}=\frac{\partial F\_{X\_{i}}(a\_{i})}{\partial a\_{i}}v\_{i}(a\_{i})\geqslant 0, |  |

which implies gi​(ai)⩽0g\_{i}(a\_{i})\leqslant 0 for 0⩽ai⩽VaRαi​(Xi)0\leqslant a\_{i}\leqslant\mathrm{VaR}\_{\alpha\_{i}}(X\_{i}).

Now, differentiating Gi​(𝐚)G\_{i}({\bf a}) with respect to aia\_{i}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂Gi​(𝐚)∂ai\displaystyle\frac{\partial G\_{i}({\bf a})}{\partial a\_{i}} | =−2​wi​(ai)​SXi​(ai)​(∑j=1n(vj​(aj)−wj​(aj)2))+2​wi​(ai)3​(1−SXi​(ai))(∑j=1n(vj​(aj)−wj​(aj)2))2\displaystyle=\frac{-2w\_{i}(a\_{i})S\_{X\_{i}}(a\_{i})\left(\sum\_{j=1}^{n}(v\_{j}(a\_{j})-w\_{j}(a\_{j})^{2})\right)+2w\_{i}(a\_{i})^{3}(1-S\_{X\_{i}}(a\_{i}))}{\left(\sum\_{j=1}^{n}(v\_{j}(a\_{j})-w\_{j}(a\_{j})^{2})\right)^{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−2​wi​(ai)​SXi​(ai)​(∑j≠i(vj​(aj)−wj​(aj)2))+2​wi​(ai)3−2​wi​(ai)​SXi​(ai)​vi​(ai)(∑j=1n(vj​(aj)−wj​(aj)2))2⩽0.\displaystyle=\frac{-2w\_{i}(a\_{i})S\_{X\_{i}}(a\_{i})\left(\sum\_{j\neq i}(v\_{j}(a\_{j})-w\_{j}(a\_{j})^{2})\right)+2w\_{i}(a\_{i})^{3}-2w\_{i}(a\_{i})S\_{X\_{i}}(a\_{i})v\_{i}(a\_{i})}{\left(\sum\_{j=1}^{n}(v\_{j}(a\_{j})-w\_{j}(a\_{j})^{2})\right)^{2}}\leqslant 0. |  |

Hence, Gi​(𝐚)G\_{i}({\bf a}) is decreasing in aia\_{i}, and consequently ∂F​(𝐚)∂ai⩾0\frac{\partial F({\bf a})}{\partial a\_{i}}\geqslant 0. Therefore, the minimum of F​(𝐚)F({\bf a}) is attained at

|  |  |  |
| --- | --- | --- |
|  | 𝐚∗=(a1∗,…,an∗)\mathbf{a}^{\*}=(a\_{1}^{\*},\dots,a\_{n}^{\*}) |  |

with

|  |  |  |
| --- | --- | --- |
|  | ai∗=inf{0⩽ai⩽VaRαi​(Xi):1−Φ−1​(α)⋅wi​(ai)2∑j=1n(vj​(aj)−wj​(aj)2)⩾0},a\_{i}^{\*}=\inf\left\{0\leqslant a\_{i}\leqslant\mathrm{VaR}\_{\alpha\_{i}}(X\_{i}):1-\Phi^{-1}(\alpha)\cdot\frac{w\_{i}(a\_{i})^{2}}{\sum\_{j=1}^{n}\left(v\_{j}(a\_{j})-w\_{j}(a\_{j})^{2}\right)}\geqslant 0\right\}, |  |

which completes the proof.
∎

## Appendix E Proofs of Section [6](https://arxiv.org/html/2512.11430v1#S6 "6 Simulation studies ‣ Pareto-optimal reinsurance under dependence uncertainty")

###### Proof of Lemma [4](https://arxiv.org/html/2512.11430v1#Thmlemma4 "Lemma 4. ‣ 6.1 Effects of dependence and confidence levels ‣ 6 Simulation studies ‣ Pareto-optimal reinsurance under dependence uncertainty").

The proofs of (ii) and (iii) are similar to those of (i), so we focus on (i).

Step 1.
We first show that

|  |  |  |
| --- | --- | --- |
|  | G¯1​(𝐮,𝐯,t)⩽G¯1​(𝐚,𝐛,t),∀t∈[0,1−α],\overline{G}\_{1}({\bf u},{\bf v},t)\leqslant\overline{G}\_{1}({\bf a},{\bf b},t),\quad\forall t\in[0,1-\alpha], |  |

where vi=VaRαi​(Xi)v\_{i}=\mathrm{VaR}\_{\alpha\_{i}}(X\_{i}) is fixed, and ui=vi−gai,bi​(vi)u\_{i}=v\_{i}-g\_{a\_{i},b\_{i}}(v\_{i}) for i=1,2i=1,2. By Theorem 3.1 in Chi and Tan ([2013](https://arxiv.org/html/2512.11430v1#bib.bib16)), we have

|  |  |  |
| --- | --- | --- |
|  | gui,vi​(x)⩽gai,bi​(x),∀x⩾0,and​gui,vi​(VaRαi​(Xi))=gai,bi​(VaRαi​(Xi)),i=1,2.g\_{u\_{i},v\_{i}}(x)\leqslant g\_{a\_{i},b\_{i}}(x),\quad\forall x\geqslant 0,\quad\text{and}\quad g\_{u\_{i},v\_{i}}(\mathrm{VaR}\_{\alpha\_{i}}(X\_{i}))=g\_{a\_{i},b\_{i}}(\mathrm{VaR}\_{\alpha\_{i}}(X\_{i})),\penalty 10000\ i=1,2. |  |

Let θ1=α+t\theta\_{1}=\alpha+t and θ2=1−t.\theta\_{2}=1-t. Hence,

|  |  |  |
| --- | --- | --- |
|  | VaRθi​(gui,vi​(Xi))⩽VaRθi​(gai,bi​(Xi)),\mathrm{VaR}\_{\theta\_{i}}(g\_{u\_{i},v\_{i}}(X\_{i}))\leqslant\mathrm{VaR}\_{\theta\_{i}}(g\_{a\_{i},b\_{i}}(X\_{i})), |  |

and therefore

|  |  |  |  |
| --- | --- | --- | --- |
|  | G¯1​(𝐮,𝐯,t)\displaystyle\overline{G}\_{1}(\mathbf{u},\mathbf{v},t) | =∑i=12{VaRαi​(Xi)−VaRαi​(gui,vi​(Xi))+VaRθi​(gui,vi​(Xi))}\displaystyle=\sum\_{i=1}^{2}\big\{\mathrm{VaR}\_{\alpha\_{i}}(X\_{i})-\mathrm{VaR}\_{\alpha\_{i}}(g\_{u\_{i},v\_{i}}(X\_{i}))+\mathrm{VaR}\_{\theta\_{i}}(g\_{u\_{i},v\_{i}}(X\_{i}))\big\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⩽∑i=12{VaRαi​(Xi)−VaRαi​(gai,bi​(Xi))+VaRθi​(gai,bi​(Xi))}\displaystyle\leqslant\sum\_{i=1}^{2}\big\{\mathrm{VaR}\_{\alpha\_{i}}(X\_{i})-\mathrm{VaR}\_{\alpha\_{i}}(g\_{a\_{i},b\_{i}}(X\_{i}))+\mathrm{VaR}\_{\theta\_{i}}(g\_{a\_{i},b\_{i}}(X\_{i}))\big\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =G¯1​(𝐚,𝐛,t).\displaystyle=\overline{G}\_{1}({\bf a},{\bf b},t). |  |

Step 2.
We now prove

|  |  |  |
| --- | --- | --- |
|  | inf(𝐚,𝐛)∈𝒜1inft∈[0,1−α]G¯1​(𝐚,𝐛,t)=inf𝐮∈𝒜𝟏​(𝐯)inft∈[0,1−α]G¯1​(𝐮,𝐯,t),\inf\_{({\bf a},{\bf b})\in\mathcal{A}\_{1}}\inf\_{t\in[0,1-\alpha]}\overline{G}\_{1}({\bf a},{\bf b},t)=\inf\_{\bf u\in\mathcal{A}\_{1}(\bf v)}\inf\_{t\in[0,1-\alpha]}\overline{G}\_{1}(\mathbf{u},\mathbf{v},t), |  |

based on Step 1.

Let

|  |  |  |
| --- | --- | --- |
|  | Sa​b∗=arg​inf(𝐚,𝐛)∈𝒜1inft∈[0,1−α]G¯1​(𝐚,𝐛,t),Su​v∗=arg​inf𝐮∈𝒜𝟏​(𝐮)inft∈[0,1−α]G¯1​(𝐮,𝐯,t).S\_{ab}^{\*}=\arg\inf\_{({\bf a},{\bf b})\in\mathcal{A}\_{1}}\inf\_{t\in[0,1-\alpha]}\overline{G}\_{1}({\bf a},{\bf b},t),\quad S\_{uv}^{\*}=\arg\inf\_{\bf u\in\mathcal{A}\_{1}(\bf u)}\inf\_{t\in[0,1-\alpha]}\overline{G}\_{1}(\mathbf{u},\mathbf{v},t). |  |

Assume (u1∗,u2∗,t∗)∈Su​v∗(u\_{1}^{\*},u\_{2}^{\*},t^{\*})\in S\_{uv}^{\*} but (u1∗,u2∗,v1,v2,t∗)∉Sa​b∗(u\_{1}^{\*},u\_{2}^{\*},v\_{1},v\_{2},t^{\*})\notin S\_{ab}^{\*}.
Then there exists (𝐚^,𝐛^,t^)∈Sa​b∗(\hat{{\bf a}},\hat{{\bf b}},\hat{t})\in S\_{ab}^{\*} such that

|  |  |  |
| --- | --- | --- |
|  | G¯1​(𝐚^,𝐛^,t^)<G¯1​(𝐮∗,𝐯,t∗).\overline{G}\_{1}(\hat{{\bf a}},\hat{{\bf b}},\hat{t})<\overline{G}\_{1}(\mathbf{u^{\*}},\mathbf{v},t^{\*}). |  |

If t^=t∗\hat{t}=t^{\*}, this is a contradiction. Otherwise, by Step 1, there exists (𝐮^,t^)∈Su​v∗(\hat{\bf u},\hat{t})\in S\_{uv}^{\*} such that

|  |  |  |
| --- | --- | --- |
|  | G¯1​(𝐮^,𝐯,t^)⩽G¯1​(𝐚^,𝐛^,t^)<G¯1​(𝐮∗,𝐯,t∗),\overline{G}\_{1}(\hat{\mathbf{u}},\mathbf{v},\hat{t})\leqslant\overline{G}\_{1}(\hat{{\bf a}},\hat{{\bf b}},\hat{t})<\overline{G}\_{1}(\mathbf{u^{\*}},\mathbf{v},t^{\*}), |  |

which is also a contradiction. Hence, (u1∗,u2∗,t∗)∈Su​v∗(u\_{1}^{\*},u\_{2}^{\*},t^{\*})\in S\_{uv}^{\*} implies (u1∗,u2∗,v1,v2,t∗)∈Sa​b∗(u\_{1}^{\*},u\_{2}^{\*},v\_{1},v\_{2},t^{\*})\in S\_{ab}^{\*}.

Conversely, if (a1∗,a2∗,v1,v2,t∗)∈Sa​b∗(a\_{1}^{\*},a\_{2}^{\*},v\_{1},v\_{2},t^{\*})\in S\_{ab}^{\*} but (a1∗,a2∗,t∗)∉Su​v∗(a\_{1}^{\*},a\_{2}^{\*},t^{\*})\notin S\_{uv}^{\*}, then there exists (𝐮~,t∗)∈Su​v∗(\widetilde{\mathbf{u}},t^{\*})\in S\_{uv}^{\*} such that

|  |  |  |
| --- | --- | --- |
|  | G¯1​(𝐮~,𝐯,t∗)<G¯1​(𝐚∗,𝐯,t∗),\overline{G}\_{1}(\widetilde{\mathbf{u}},\mathbf{v},t^{\*})<\overline{G}\_{1}({\bf a}^{\*},\mathbf{v},t^{\*}), |  |

again a contradiction.

Finally, by Step 1, for any (a1∗,a2∗,b1∗,b2∗,t∗)∈Sa​b∗(a\_{1}^{\*},a\_{2}^{\*},b\_{1}^{\*},b\_{2}^{\*},t^{\*})\in S\_{ab}^{\*} with b1∗≠v1b\_{1}^{\*}\neq v\_{1} or b2∗≠v2b\_{2}^{\*}\neq v\_{2}, there exists (u1′,u2′,v1,v2,t∗)∈Sa​b∗(u\_{1}^{\prime},u\_{2}^{\prime},v\_{1},v\_{2},t^{\*})\in S\_{ab}^{\*} such that

|  |  |  |
| --- | --- | --- |
|  | G¯1​(𝐚∗,𝐛∗,t∗)=G¯1​(𝐮′,𝐯,t∗),\overline{G}\_{1}({\bf a}^{\*},{\bf b}^{\*},t^{\*})=\overline{G}\_{1}(\mathbf{u^{\prime}},\mathbf{v},t^{\*}), |  |

and hence (u1′,u2′,t∗)∈Su​v∗(u\_{1}^{\prime},u\_{2}^{\prime},t^{\*})\in S\_{uv}^{\*}.

Therefore,

|  |  |  |
| --- | --- | --- |
|  | inf(𝐚,𝐛)∈𝒜1inft∈[0,1−α]G¯1​(𝐚,𝐛,t)=inf𝐮∈𝒜𝟏​(𝐯)inft∈[0,1−α]G¯1​(𝐮,𝐯,t),\inf\_{({\bf a},{\bf b})\in\mathcal{A}\_{1}}\inf\_{t\in[0,1-\alpha]}\overline{G}\_{1}({\bf a},{\bf b},t)=\inf\_{\bf u\in\mathcal{A}\_{1}(\bf v)}\inf\_{t\in[0,1-\alpha]}\overline{G}\_{1}(\mathbf{u},\mathbf{v},t), |  |

which yields the desired result.
∎

###### Proof of Proposition [8](https://arxiv.org/html/2512.11430v1#Thmproposition8 "Proposition 8. ‣ 6.2 Effects of distributional assumptions ‣ 6 Simulation studies ‣ Pareto-optimal reinsurance under dependence uncertainty").

Let θ1=α+t\theta\_{1}=\alpha+t and θ2=1−t\theta\_{2}=1-t. Consider the case where there exists i∈{1,2}i\in\{1,2\} such that α⩾αi\alpha\geqslant\alpha\_{i}, and assume without loss of generality that α⩾α2\alpha\geqslant\alpha\_{2}.
If α⩾α1\alpha\geqslant\alpha\_{1}, then

|  |  |  |
| --- | --- | --- |
|  | VaRθi​(gai,bi​(Xi))−VaRαi​(gai,bi​(Xi))⩾0,i=1,2.\displaystyle\mathrm{VaR}\_{\theta\_{i}}\big(g\_{a\_{i},b\_{i}}(X\_{i})\big)-\mathrm{VaR}\_{\alpha\_{i}}\big(g\_{a\_{i},b\_{i}}(X\_{i})\big)\geqslant 0,\qquad i=1,2. |  |

In this case, ai∈[0,bi∗]a\_{i}\in[0,b\_{i}^{\*}] for i=1,2i=1,2, and t∗=0t^{\*}=0.

If α<α1\alpha<\alpha\_{1} and α+t⩽α1\alpha+t\leqslant\alpha\_{1}, then a2a\_{2} still belongs to [0,b2∗][0,b\_{2}^{\*}]. By the 1-Lipschitz property of ga1,b1g\_{a\_{1},b\_{1}},

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaRα+t​(ga1,b1​(X1))−VaRα1​(ga1,b1​(X1))\displaystyle\mathrm{VaR}\_{\alpha+t}\big(g\_{a\_{1},b\_{1}}(X\_{1})\big)-\mathrm{VaR}\_{\alpha\_{1}}\big(g\_{a\_{1},b\_{1}}(X\_{1})\big) | ⩾VaRα+t​(X1)−VaRα1​(X1)\displaystyle\geqslant\mathrm{VaR}\_{\alpha+t}(X\_{1})-\mathrm{VaR}\_{\alpha\_{1}}(X\_{1}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⩾VaRα​(X1)−VaRα1​(X1),\displaystyle\geqslant\mathrm{VaR}\_{\alpha}(X\_{1})-\mathrm{VaR}\_{\alpha\_{1}}(X\_{1}), |  |

and the infimum is achieved at t∗=0t^{\*}=0 with a1∈[0,VaRα​(X1)]a\_{1}\in[0,\mathrm{VaR}\_{\alpha}(X\_{1})]. By symmetry, one can also obtain t∗=1−αt^{\*}=1-\alpha for the case α⩾α1\alpha\geqslant\alpha\_{1}.

Next, consider the case where αi>α\alpha\_{i}>\alpha for i=1,2i=1,2, and examine the corresponding admissible ranges of tt and the associated minimum values.

Case (1): t∈[0,α1−α)t\in[0,\alpha\_{1}-\alpha).
In this case, we have α+t<α1\alpha+t<\alpha\_{1} and 1−t>α21-t>\alpha\_{2}. Since 1−t>α21-t>\alpha\_{2},

|  |  |  |
| --- | --- | --- |
|  | VaR1−t​(ga2,b2​(X2))−VaRα2​(ga2,b2​(X2))⩾0,\mathrm{VaR}\_{1-t}\big(g\_{a\_{2},b\_{2}}(X\_{2})\big)-\mathrm{VaR}\_{\alpha\_{2}}\big(g\_{a\_{2},b\_{2}}(X\_{2})\big)\geqslant 0, |  |

and the infimum is attained for a2∈[0,VaRα2​(X2)]a\_{2}\in[0,\mathrm{VaR}\_{\alpha\_{2}}(X\_{2})].
Because α+t<α1\alpha+t<\alpha\_{1}, by the 1-Lipschitz condition,

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaRα+t​(ga1,b1​(X1))−VaRα1​(ga1,b1​(X1))\displaystyle\mathrm{VaR}\_{\alpha+t}\big(g\_{a\_{1},b\_{1}}(X\_{1})\big)-\mathrm{VaR}\_{\alpha\_{1}}\big(g\_{a\_{1},b\_{1}}(X\_{1})\big) | ⩾VaRα+t​(X1)−VaRα1​(X1)\displaystyle\geqslant\mathrm{VaR}\_{\alpha+t}(X\_{1})-\mathrm{VaR}\_{\alpha\_{1}}(X\_{1}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⩾VaRα​(X1)−VaRα1​(X1),\displaystyle\geqslant\mathrm{VaR}\_{\alpha}(X\_{1})-\mathrm{VaR}\_{\alpha\_{1}}(X\_{1}), |  |

and the minimum is achieved at t∗=0t^{\*}=0 and a1∈[0,VaRα​(X1)]a\_{1}\in[0,\mathrm{VaR}\_{\alpha}(X\_{1})].
Thus, the minimum value in this case is
VaRα​(X1)+VaRα2​(X2).\mathrm{VaR}\_{\alpha}(X\_{1})+\mathrm{VaR}\_{\alpha\_{2}}(X\_{2}).

Case (2): t∈[α1−α, 1−α2]t\in[\alpha\_{1}-\alpha,\,1-\alpha\_{2}].
In this case, α+t⩾α1\alpha+t\geqslant\alpha\_{1} and 1−t⩾α21-t\geqslant\alpha\_{2}. Recall that θ1=α+t\theta\_{1}=\alpha+t and θ2=1−t\theta\_{2}=1-t. Then

|  |  |  |
| --- | --- | --- |
|  | VaRθi​(gai,bi​(Xi))−VaRαi​(gai,bi​(Xi))⩾0,i=1,2,\mathrm{VaR}\_{\theta\_{i}}\big(g\_{a\_{i},b\_{i}}(X\_{i})\big)-\mathrm{VaR}\_{\alpha\_{i}}\big(g\_{a\_{i},b\_{i}}(X\_{i})\big)\geqslant 0,\quad i=1,2, |  |

and the minimum value is
VaRα1​(X1)+VaRα2​(X2).\mathrm{VaR}\_{\alpha\_{1}}(X\_{1})+\mathrm{VaR}\_{\alpha\_{2}}(X\_{2}).
which is greater than that in Case 1.

Case (3): t∈(1−α2,1]t\in(1-\alpha\_{2},1].
In this case, α+t>α1, 1−t<α2.\alpha+t>\alpha\_{1},\penalty 10000\ 1-t<\alpha\_{2}. Since α+t>α1,\alpha+t>\alpha\_{1},

|  |  |  |
| --- | --- | --- |
|  | VaRα+t​(ga1,b1​(X1))−VaRα1​(ga1,b1​(X1))⩾0,\displaystyle\mathrm{VaR}\_{\alpha+t}(g\_{a\_{1},b\_{1}}(X\_{1}))-\mathrm{VaR}\_{\alpha\_{1}}(g\_{a\_{1},b\_{1}}(X\_{1}))\geqslant 0, |  |

which is obtained for a1∈[0,VaRα1​(X1)].a\_{1}\in[0,\mathrm{VaR}\_{\alpha\_{1}}(X\_{1})]. Since 1−t<α2,1-t<\alpha\_{2}, by the 1-Lipschitz,

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaR1−t​(ga2,b2​(X2))−VaRα2​(ga2,b2​(X2))\displaystyle\mathrm{VaR}\_{1-t}(g\_{a\_{2},b\_{2}}(X\_{2}))-\mathrm{VaR}\_{\alpha\_{2}}(g\_{a\_{2},b\_{2}}(X\_{2})) | ⩾VaR1−t​(X2)−VaRα2​(X2)\displaystyle\geqslant\mathrm{VaR}\_{1-t}(X\_{2})-\mathrm{VaR}\_{\alpha\_{2}}(X\_{2}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⩾VaRα​(X2)−VaRα2​(X2),\displaystyle\geqslant\mathrm{VaR}\_{\alpha}(X\_{2})-\mathrm{VaR}\_{\alpha\_{2}}(X\_{2}), |  |

which is obtained for t∗=1−αt^{\*}=1-\alpha and a2∈[0,VaRα​(X1)].a\_{2}\in[0,\mathrm{VaR}\_{\alpha}(X\_{1})]. The minimum value is VaRα1​(X1)+VaRα​(X2).\mathrm{VaR}\_{\alpha\_{1}}(X\_{1})+\mathrm{VaR}\_{\alpha}(X\_{2}).
  
To sum up, the minimum value is either VaRα​(X1)+VaRα2​(X2)\mathrm{VaR}\_{\alpha}(X\_{1})+\mathrm{VaR}\_{\alpha\_{2}}(X\_{2}) or VaRα1​(X1)+VaRα​(X2)\mathrm{VaR}\_{\alpha\_{1}}(X\_{1})+\mathrm{VaR}\_{\alpha}(X\_{2}), attained at t=0t=0 or t=1−αt=1-\alpha, respectively. Consequently, the problem reduces to the case of one reinsurer and one insurer.
The proof is complete.
∎

###### Proof of Proposition [9](https://arxiv.org/html/2512.11430v1#Thmproposition9 "Proposition 9. ‣ 6.2 Effects of distributional assumptions ‣ 6 Simulation studies ‣ Pareto-optimal reinsurance under dependence uncertainty").

If α⩾α1+α2−1\alpha\geqslant\alpha\_{1}+\alpha\_{2}-1, the conclusion follows directly from Proposition [8](https://arxiv.org/html/2512.11430v1#Thmproposition8 "Proposition 8. ‣ 6.2 Effects of distributional assumptions ‣ 6 Simulation studies ‣ Pareto-optimal reinsurance under dependence uncertainty"). We therefore assume α<α1+α2−1\alpha<\alpha\_{1}+\alpha\_{2}-1 in the remainder of the proof.

We analyze the behavior of the objective function over different intervals of tt:

Case 1: t∈[0,1−α2]t\in[0,1-\alpha\_{2}].
In this regime, we have α+t<α1\alpha+t<\alpha\_{1} and 1−t⩾α21-t\geqslant\alpha\_{2}.
Following an argument analogous to Case (1) in the proof of Proposition [8](https://arxiv.org/html/2512.11430v1#Thmproposition8 "Proposition 8. ‣ 6.2 Effects of distributional assumptions ‣ 6 Simulation studies ‣ Pareto-optimal reinsurance under dependence uncertainty"),
the minimum is attained at t∗=0t^{\*}=0, with optimal value VaRα​(X1)+VaRα2​(X2)\mathrm{VaR}\_{\alpha}(X\_{1})+\mathrm{VaR}\_{\alpha\_{2}}(X\_{2}).

Case 2: t∈[α1−α,1−α]t\in[\alpha\_{1}-\alpha,1-\alpha].
In this parameter regime, the conditions α+t⩾α1\alpha+t\geqslant\alpha\_{1} and 1−t<α21-t<\alpha\_{2} are satisfied.
Following an argument parallel to Case (3) in the proof of Proposition [8](https://arxiv.org/html/2512.11430v1#Thmproposition8 "Proposition 8. ‣ 6.2 Effects of distributional assumptions ‣ 6 Simulation studies ‣ Pareto-optimal reinsurance under dependence uncertainty"),
we find that the minimum is attained at the right endpoint t∗=1−αt^{\*}=1-\alpha.
This yields the optimal value VaRα1​(X1)+VaRα​(X2)\mathrm{VaR}\_{\alpha\_{1}}(X\_{1})+\mathrm{VaR}\_{\alpha}(X\_{2}).

Case (3): t∈(1−α2,α1−α)t\in(1-\alpha\_{2},\alpha\_{1}-\alpha).
In this case, α+t<α1\alpha+t<\alpha\_{1} and 1−t<α21-t<\alpha\_{2}. For any t∈(1−α2,α1−α)t\in(1-\alpha\_{2},\alpha\_{1}-\alpha),

|  |  |  |
| --- | --- | --- |
|  | VaR1−t​(ga2,b2​(X2))−VaRα2​(ga2,b2​(X2))⩾VaR1−t​(X2)−VaRα2​(X2),\mathrm{VaR}\_{1-t}(g\_{a\_{2},b\_{2}}(X\_{2}))-\mathrm{VaR}\_{\alpha\_{2}}(g\_{a\_{2},b\_{2}}(X\_{2}))\geqslant\mathrm{VaR}\_{1-t}(X\_{2})-\mathrm{VaR}\_{\alpha\_{2}}(X\_{2}), |  |

and

|  |  |  |
| --- | --- | --- |
|  | VaRα+t​(ga1,b1​(X1))−VaRα1​(ga1,b1​(X1))⩾VaRα+t​(X1)−VaRα1​(X1),\mathrm{VaR}\_{\alpha+t}(g\_{a\_{1},b\_{1}}(X\_{1}))-\mathrm{VaR}\_{\alpha\_{1}}(g\_{a\_{1},b\_{1}}(X\_{1}))\geqslant\mathrm{VaR}\_{\alpha+t}(X\_{1})-\mathrm{VaR}\_{\alpha\_{1}}(X\_{1}), |  |

with the bounds attained by a1∈[0,VaRα+t​(X1)]a\_{1}\in[0,\mathrm{VaR}\_{\alpha+t}(X\_{1})] and a2∈[0,VaR1−t​(X2)]a\_{2}\in[0,\mathrm{VaR}\_{1-t}(X\_{2})].
Hence, the minimum value for fixed t∈(1−α2,α1−α)t\in(1-\alpha\_{2},\alpha\_{1}-\alpha) is VaRα+t​(X1)+VaR1−t​(X2)\mathrm{VaR}\_{\alpha+t}(X\_{1})+\mathrm{VaR}\_{1-t}(X\_{2}).

The difference between this value and the minimum in Case (1) is

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | VaRα+t​(X1)−VaRα​(X1)+VaR1−t​(X2)−VaRα2​(X2)\displaystyle\mathrm{VaR}\_{\alpha+t}(X\_{1})-\mathrm{VaR}\_{\alpha}(X\_{1})+\mathrm{VaR}\_{1-t}(X\_{2})-\mathrm{VaR}\_{\alpha\_{2}}(X\_{2}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | VaRα+t​(X1)−VaRα+1−α2​(X1)+VaRα+1−α2​(X1)−VaRα​(X1)\displaystyle\mathrm{VaR}\_{\alpha+t}(X\_{1})-\mathrm{VaR}\_{\alpha+1-\alpha\_{2}}(X\_{1})+\mathrm{VaR}\_{\alpha+1-\alpha\_{2}}(X\_{1})-\mathrm{VaR}\_{\alpha}(X\_{1}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +VaR1−t​(X2)−VaRα2​(X2).\displaystyle+\mathrm{VaR}\_{1-t}(X\_{2})-\mathrm{VaR}\_{\alpha\_{2}}(X\_{2}). |  |

If VaRα+t​(X1)−VaRα+1−α2​(X1)⩾VaRα2​(X2)−VaR1−t​(X2)\mathrm{VaR}\_{\alpha+t}(X\_{1})-\mathrm{VaR}\_{\alpha+1-\alpha\_{2}}(X\_{1})\geqslant\mathrm{VaR}\_{\alpha\_{2}}(X\_{2})-\mathrm{VaR}\_{1-t}(X\_{2}),
then since VaRα+1−α2​(X1)−VaRα​(X1)>0\mathrm{VaR}\_{\alpha+1-\alpha\_{2}}(X\_{1})-\mathrm{VaR}\_{\alpha}(X\_{1})>0, the above expression is positive. Otherwise, consider the difference between this value and the minimum in Case (2):

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | VaRα+t​(X1)−VaRα1​(X1)+VaR1−t​(X2)−VaRα​(X2)\displaystyle\mathrm{VaR}\_{\alpha+t}(X\_{1})-\mathrm{VaR}\_{\alpha\_{1}}(X\_{1})+\mathrm{VaR}\_{1-t}(X\_{2})-\mathrm{VaR}\_{\alpha}(X\_{2}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | VaRα+t​(X1)−VaRα1​(X1)+VaR1−t​(X2)−VaRα+1−α1​(X2)\displaystyle\mathrm{VaR}\_{\alpha+t}(X\_{1})-\mathrm{VaR}\_{\alpha\_{1}}(X\_{1})+\mathrm{VaR}\_{1-t}(X\_{2})-\mathrm{VaR}\_{\alpha+1-\alpha\_{1}}(X\_{2}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +VaRα+1−α1​(X2)−VaRα​(X2).\displaystyle+\mathrm{VaR}\_{\alpha+1-\alpha\_{1}}(X\_{2})-\mathrm{VaR}\_{\alpha}(X\_{2}). |  |

Since 𝐅∈(ℳc​xα)2\mathbf{F}\in\left(\mathcal{M}\_{cx}^{\alpha}\right)^{2}, we have

|  |  |  |
| --- | --- | --- |
|  | 1α2+t−1​(VaRα+t​(X1)−VaRα+1−α2​(X1))⩾1α1−α−t​(VaRα1​(X1)−VaRα+t​(X1)),\frac{1}{\alpha\_{2}+t-1}\left(\mathrm{VaR}\_{\alpha+t}(X\_{1})-\mathrm{VaR}\_{\alpha+1-\alpha\_{2}}(X\_{1})\right)\geqslant\frac{1}{\alpha\_{1}-\alpha-t}\left(\mathrm{VaR}\_{\alpha\_{1}}(X\_{1})-\mathrm{VaR}\_{\alpha+t}(X\_{1})\right), |  |

and

|  |  |  |
| --- | --- | --- |
|  | 1α1−α−t​(VaR1−t​(X2)−VaRα+1−α1​(X2))⩾1α2+t−1​(VaRα2​(X2)−VaR1−t​(X2)).\frac{1}{\alpha\_{1}-\alpha-t}\left(\mathrm{VaR}\_{1-t}(X\_{2})-\mathrm{VaR}\_{\alpha+1-\alpha\_{1}}(X\_{2})\right)\geqslant\frac{1}{\alpha\_{2}+t-1}\left(\mathrm{VaR}\_{\alpha\_{2}}(X\_{2})-\mathrm{VaR}\_{1-t}(X\_{2})\right). |  |

From the earlier assumption that VaRα+t​(X1)−VaRα+1−α2​(X1)<VaRα2​(X2)−VaR1−t​(X2)\mathrm{VaR}\_{\alpha+t}(X\_{1})-\mathrm{VaR}\_{\alpha+1-\alpha\_{2}}(X\_{1})<\mathrm{VaR}\_{\alpha\_{2}}(X\_{2})-\mathrm{VaR}\_{1-t}(X\_{2}),
it follows that VaR1−t​(X2)−VaRα+1−α1​(X2)>VaRα1​(X1)−VaRα+t​(X1)\mathrm{VaR}\_{1-t}(X\_{2})-\mathrm{VaR}\_{\alpha+1-\alpha\_{1}}(X\_{2})>\mathrm{VaR}\_{\alpha\_{1}}(X\_{1})-\mathrm{VaR}\_{\alpha+t}(X\_{1}).
Therefore, the above expression is positive.
Thus, the minimum value in Case (3) is greater than the minima in both Cases (1) and (2).
In summary, the global minimum is either VaRα​(X1)+VaRα2​(X2)\mathrm{VaR}\_{\alpha}(X\_{1})+\mathrm{VaR}\_{\alpha\_{2}}(X\_{2}) or VaRα1​(X1)+VaRα​(X2)\mathrm{VaR}\_{\alpha\_{1}}(X\_{1})+\mathrm{VaR}\_{\alpha}(X\_{2}),
attained at t=0t=0 or t=1−αt=1-\alpha, respectively. Consequently, the problem reduces to the case of one reinsurer and one insurer.
∎

## References

* Asimit et al. (2017)

  Asimit, A. V., Bignozzi, V., Cheung, K. C., Hu, J., and Kim, E.-S. (2017).
  Robust and Pareto optimality of insurance contracts.
  *European Journal of Operational Research*, 262, 720–732.
* Arrow (1971)
   Arrow K. J. (1971). *Essays in the theory of risk-bearing.* Chicago: Markham Publishing Company
* Ben-Tal et al. (2009)

  Ben-Tal, A., El Ghaoui, L., and Nemirovski, A. (2009).
  *Robust Optimisation*.
  Princeton University Press, New Jersey, USA.
* Ben-Tal and Nemirovski (2008)

  Ben-Tal, A. and Nemirovski, A. (2008).
  Selected topics in robust convex optimization.
  *Mathematical Programming*, 112(1), 125–158.
* Bernard et al. (2014)

  Bernard, C., Jiang, X., and Wang, R. (2014). Risk aggregation with dependence uncertainty. *Insurance: Mathematics and Economics*, 54, 93–108.
* Bertsimas et al. (2011)

  Bertsimas, D., Brown, D. B., and Caramanis, C. (2011).
  Theory and applications of robust optimization.
  *SIAM Review*, 53(3), 464–501.
* Billingsley (1995)
   Billingsley, P. (1995). *Probability and Measure*, 3rd edition, Wiley.
* Blanchet et al. (2025)
   Blanchet, J., Lam, H.,
  Liu, Y., and Wang, R. (2025). Convolution bounds on quantile aggregation. *Operations Research*, 73(5), 2761–2781.
* Boonen and Jiang (2023)

  Boonen, T. J. and Jiang, W. (2023). Pareto-optimal reinsurance with default risk and solvency regulation. *Probability in the Engineering and Informational Sciences*, 37(2), 518–545.
* Boonen et al. (2024)
   Boonen, T. J., Chong, W. F. and Ghossoub, M. (2024). Pareto‐efficient risk sharing in centralized insurance markets with application to flood risk. *Journal of Risk and Insurance*, 91(2), 449–488.
* Cai et al. (2017)

  Cai, J., Liu, H., and Wang, R. (2017). Pareto-optimal reinsurance arrangements under general model settings. *Insurance: Mathematics and Economics*, 77, 24–37.
* Cai et al. (2024)

  Cai, J., Liu, F., and Yin, M. (2024).
  Worst-case risk measures of stop-loss and limited loss random variables under distribution uncertainty with applications to robust reinsurance.
  *European Journal of Operational Research*, 318(1), 310–326.
* Cai et al. (2008)

  Cai, J., Tan, K. S., Weng, C., and Zhang, Y. (2008). Optimal reinsurance under VaR and CTE risk measures. *Insurance: Mathematics and Economics*, 43(1), 185–196.
* Chi (2012)

  Chi, Y. (2012). Optimal reinsurance under variance related premium principles. *Insurance: Mathematics and Economics*, 51(2), 310–321.
* Chi and Meng (2014)

  Chi, Y. and Meng, H. (2014). Optimal reinsurance arrangements in the presence of two reinsurers. *Scandinavian Actuarial Journal,* 2014(5), 424-438.
* Chi and Tan (2013)

  Chi, Y. and Tan, K. S. (2013). Optimal reinsurance with general premium principles. *Insurance: Mathematics and Economics*, 52(2), 180–189.
* Chi et al. (2022)

  Chi, Y., Xu, Z. Q., and Zhuang, S. C. (2022).
  Distributionally robust goal-reaching optimization in the presence of background risk.
  *North American Actuarial Journal*, 26(3), 351–382.
* Coke et al. (2024)

  Coke, O., Ghossoub, M., and Zhu, M. B. (2024). Pareto-optimal insurance with an upper limit on the insurer’s exposure. Scandinavian Actuarial Journal, 2024(3), 227–251.
* Cont et al. (2010)

  Cont, R., Deguest, R., and Scandolo, G. (2010). Robustness and sensitivity analysis of risk measurement procedures. *Quantitative Finance*, 10(6), 593–606.
* Denneberg (1994)

  Denneberg, D. (1994). *Non-additive measure and integral*, Volumr 27. Springer Science & Business Media.
* Denuit et al. (2005)

  Denuit, M., Dhaene, J., Goovaerts, M., and Kaas, R. (2005). *Actuarial Theory for Dependent Risks: Measures, Orders and Models*. John Wiley & Sons, West Sussex, UK.
* Embrechts et al. (2018)

  Embrechts, P., Liu, H., and Wang, R. (2018). Quantile-based risk sharing. *Operations Research*, 66(4), 936–949.
* Embrechts et al. (2013)
   Embrechts, P., Puccetti, G., and Rüschendorf, L. (2013). Model uncertainty and VaR aggregation. Journal of Banking and Finance, 37(8), 2750–2764.
* Embrechts et al. (2015)
   Embrechts, P., Wang, B., and Wang, R. (2015). Aggregation-robustness and model uncertainty of regulatory risk measures. Finance and Stochastics, 19(4), 763–790.
* Fadina et al. (2025)

  Fadina, T., Hu, J., Liu, P., and Xia, Y. (2025). Optimal reinsurance with multivariate risks and dependence uncertainty. European Journal of Operational Research, 321(1), 231–242.
* Föllmer and Schied (2016)

  Föllmer, H. and Schied, A. (2016). *Stochastic Finance. An Introduction in Discrete Time*. Walter de Gruyter, Berlin, Fourth Edition.
* Gabrel et al. (2014)

  Gabrel, V., Murat, C., and Thiele, A. (2014).
  Recent advances in robust optimization: An overview.
  *European Journal of Operational Research*, 235(3), 471–483.
* Gavagan et al. (2022)

  Gavagan, J., Hu, L., Lee, G. Y., Liu, H., and Weixel, A. (2022). Optimal reinsurance with model uncertainty and Stackelberg game. *Scandinavian Actuarial Journal*, 2022(1), 29–48.
* Ghossoub (2019)

  Ghossoub, M. (2019). Budget-constrained optimal insurance with belief heterogeneity. *Insurance: Mathematics and Economics*, 89, 79–91.
* Jiang et al. (2018)

  Jiang, W., Hong, H., and Ren, J. (2018). On Pareto-optimal reinsurance with constraints under distortion risk measures. European Actuarial Journal, 8(1), 215–243.
* Lu et al. (2013)

  Lu, Z., Liu, L., and Meng, S. (2013). Optimal reinsurance with concave ceded loss functions under VaR and CTE risk measures. Insurance: Mathematics and Economics, 52(1), 46-51.
* Makarov (1981)

  Makarov, G. (1981). Estimates for the distribution function of a sum of two random variables when the marginal distributions are fixed. *Theory of Probability and Its Applications*, 26, 803–806.
* McNeil et al. (2015)

  McNeil, A. J., Frey, R., and Embrechts, P. (2015). *Quantitative
  Risk Management: Concepts, Techniques and Tools*. Revised Edition. Princeton, NJ:
  Princeton University Press.
* Polak et al. (2010)

  Polak, G. G., Rogers, D. F., and Sweeney, D. J. (2010).
  Risk management strategies via minimax portfolio optimization.
  *European Journal of Operational Research*, 207(1), 409–419.