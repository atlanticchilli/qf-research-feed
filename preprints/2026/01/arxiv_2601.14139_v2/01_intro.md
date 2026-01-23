---
authors:
- Michail Anthropelos
- Constantinos Kardaras
- Constantinos Stefanakis
doc_id: arxiv:2601.14139v2
family_id: arxiv:2601.14139
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Log-optimality with small liability stream
url_abs: http://arxiv.org/abs/2601.14139v2
url_html: https://arxiv.org/html/2601.14139v2
venue: arXiv q-fin
version: 2
year: 2026
---


Michail Anthropelos
Department of Banking and Financial Management
  
University of Piraeus
[anthropel@unipi.gr](mailto:anthropel@unipi.gr)
, 
Constantinos Kardaras
Department of Statistics
  
London School of Economics
[k.kardaras@lse.ac.uk](mailto:k.kardaras@lse.ac.uk)
 and 
Constantinos Stefanakis
Department of Banking and Financial Management
  
University of Piraeus
[kstefanakis@unipi.gr](mailto:kstefanakis@unipi.gr)

###### Abstract.

In an incomplete financial market with general continuous semimartingale dynamics; we model an investor with log-utility preferences who, in addition to an initial capital, receives units of a non-traded endowment process. Using duality techniques, we derive the fourth-order expansion of the primal value function with respect to the units ϵ\epsilon, held in the non-traded endowment. In turn, this lays the foundation for expanding the optimal wealth process, in this context, up to second order w.r.t. ϵ\epsilon. The key processes underpinning the aforementioned results are given in terms of Kunita-Watanabe projections, mirroring the case of lower order expansions of similar nature. Both the case of finite and infinite horizons are treated in a unified manner.

The research project was supported by the Hellenic Foundation for Research and Innovation (H.F.R.I.) under the “2nd Call for H.F.R.I. Research Projects to support Faculty Members & Researchers” (Project Number: 3444/2022, Project Title: “Valuation and Optimal Investment of Pension Plans”).

We would like to thank Scott Robertson, Mihai Sirbu, Gordan Žitković and Thaleia Zariphopoulou for their valuable comments and suggestions.

October, 2025

## Introduction

### Discussion

A central problem in financial economics involves an investor allocating initial wealth across an array of assets, with the goal of maximizing the expected utility of terminal wealth. This optimal investment problem in continuous-time settings was initially studied by Merton in [[32](https://arxiv.org/html/2601.14139v2#bib.bib46 "Lifetime portfolio selection under uncertainty: the continuous-time case"), [33](https://arxiv.org/html/2601.14139v2#bib.bib47 "Optimum consumption and prtfolio rules in a continuous-time model")], who used dynamic programming techniques to derive a non-linear partial differential equation characterizing the value function.

A major conceptual advancement came with the development of the theory of equivalent martingale measures by Ross [[46](https://arxiv.org/html/2601.14139v2#bib.bib50 "The arbitrage theory of capital asset pricing")], Harrison and Kreps [[10](https://arxiv.org/html/2601.14139v2#bib.bib48 "Martingales and arbitrage in multiperiod security markets")] and Harrison and Pliska [[11](https://arxiv.org/html/2601.14139v2#bib.bib49 "Martingales and stochastic integrals in the theory of continuous trading")], which enabled the application of martingale and duality methods to such optimization problems. Under the assumption of market completeness, this duality approach was further developed by Pliska [[45](https://arxiv.org/html/2601.14139v2#bib.bib51 "A stochastic calculus model of continuous trading: optimal portfolio")]; Karatzas, Lehoczky, and Shreve [[24](https://arxiv.org/html/2601.14139v2#bib.bib52 "Optimal portfolio and consumption decisions for a “small investor” on a finite horizon")]; and Cox and Huang [[2](https://arxiv.org/html/2601.14139v2#bib.bib53 "Optimal consumption and portfolio policies when asset prices follow a diffusion process"), [3](https://arxiv.org/html/2601.14139v2#bib.bib54 "A variational problem arising in financial economics")]. The more intricate case of incomplete markets was addressed in foundational works by He and Pearson [[12](https://arxiv.org/html/2601.14139v2#bib.bib55 "Consumption and portfolio policies with incomplete markets and short-sale constraints: the finite-dimensional case"), [13](https://arxiv.org/html/2601.14139v2#bib.bib56 "Consumption and portfolio policies with incomplete markets and short-sale constraints: the infinite-dimensional case")] and by Karatzas, Lehoczky, Shreve, and Xu [[23](https://arxiv.org/html/2601.14139v2#bib.bib57 "Martingale and duality methods for utility maximization in an incomplete market")]. Building on these contributions, Kramkov and Schachermayer [[26](https://arxiv.org/html/2601.14139v2#bib.bib3 "The asymptotic elasticity of utility functions and optimal investment in incomplete markets"), [27](https://arxiv.org/html/2601.14139v2#bib.bib58 "Necessary and sufficient conditions in the problem of optimal investment in incomplete markets")] established minimal conditions on both the utility function and the financial market under which the core results of the theory remain valid.

In the context of incomplete markets, a natural extension of the problem involves maximizing expected utility when the investor receives an additional exogenous random endowment. Typical examples of this being pension funds. In complete markets, endowments can be perfectly replicated using traded assets, effectively reducing the problem to one with augmented initial wealth and no random endowment. However, as noted among others in [[14](https://arxiv.org/html/2601.14139v2#bib.bib34 "Utility indifference pricing: an overview")], real-world markets are typically incomplete, with perfect replication impeded by frictions such as transaction costs, non-traded assets, and portfolio constraints. In such settings, assets are associated with a range of arbitrage-free prices, and the risk of holding them cannot be fully hedged through market trading alone.

Consequently, analyzing the value function and its solution in an incomplete market setting is undeniably more challenging. Notable contributions addressing this challenge include Cvitanić, Schachermayer, and Wang [[4](https://arxiv.org/html/2601.14139v2#bib.bib59 "Utility maximization in incomplete markets with random endowment")], who characterized the optimal terminal wealth in a general semimartingale model via a dual formulation. [[25](https://arxiv.org/html/2601.14139v2#bib.bib60 "Optimal consumption from investment and random endowment in incomplete semimartingale markets")] extends this framework to account for intertemporal consumption. Hugonnier and Kramkov [[18](https://arxiv.org/html/2601.14139v2#bib.bib4 "Optimal investment with random endowments in incomplete markets")] treated both the initial capital and the units held in the endowment as optimization variables, hence not requiring the use of finitely additive measures. [[44](https://arxiv.org/html/2601.14139v2#bib.bib61 "Optimal investment with an unbounded random endowment and utility-based pricing")] studies the case of unbounded random endowments and utility functions defined over the entire real line, providing necessary and sufficient conditions for the existence of a solution to the primal problem. [[40](https://arxiv.org/html/2601.14139v2#bib.bib67 "Necessary and sufficient conditions in the problem of optimal investment with intermediate consumption")] obtains necessary and sufficient conditions in the general framework of an incomplete financial model with a stochastic field utility and intermediate consumption, occurring according to some stochastic clock, while [[41](https://arxiv.org/html/2601.14139v2#bib.bib68 "Optimal investment with intermediate consumption and random endowment")] generalizes the former by also incorporating a random endowment process into the model. Staying within the context of intermediate consumption, [[1](https://arxiv.org/html/2601.14139v2#bib.bib69 "Optimal investment with intermediate consumption under no unbounded profit with bounded risk")] show that the key conclusions of the utility maximization theory hold under the assumptions of No Unbounded Profit with Bounded Risk (NUPBR) and of the finiteness of both primal and dual functions.

### Contributions

In an incomplete financial market with general continuous semimartingale dynamics, we model an investor with log-utility preferences who, in addition to an initial capital, receives units of a non-traded endowment process. As explicit solutions to the associated utility maximization problem are generally unavailable, even for simple model specifications; to address this, we assume that the payoff from the non-traded endowment is small relative to the investor’s total wealth. Within this framework, our contributions to the literature are as follows:

1. (1)

   Fourth-order expansion and nearly optimal strategies:
   Using duality techniques, we derive the fourth-order expansion of the primal value function with respect to the number of units ϵ\epsilon, held in the non-traded endowment. In turn, this lays the foundation for expanding the optimal wealth process, in this context, up to second order w.r.t. ϵ\epsilon. To the best of our knowledge this is the first result in this direction, extending the work of [[28](https://arxiv.org/html/2601.14139v2#bib.bib18 "Sensitivity analysis of utility-based prices and risk-tolerance wealth processes")], [[29](https://arxiv.org/html/2601.14139v2#bib.bib19 "Asymptotic analysis of utility-based hedging strategies for small number of contingent claims")] for the case of log-utility. Interestingly enough, the key processes underpinning the aforementioned results are given in terms of Kunita-Watanabe projections, mirroring the case of lower order expansions of similar nature.
2. (2)

   Long-horizon asymptotics:
   Our model also accommodates the case of “infinite time horizons”. This is a non-trivial addition which allows for the original problem to be understood in “myopic terms” for investors with distant maturities. The upshot being that one can obtain explicit results in a larger array of models, as the dependence on the horizon is eliminated.

These results have two key implications. First they allow for a better understanding of log-optimal behavior in the incomplete setting, under the presence of a non-traded endowment. This stems from the fact that the first order approximation of the optimal wealth process with non-traded endowment, w.r.t. ϵ\epsilon, is actually optimal; assuming market completeness. This provides unique insight on how market incompleteness affects asset allocation. Second, considering the case of arbitrarily large time horizons, i.e. the infinite horizon setting, comes with its own merits. Namely it enables analyzing assets which do not have a certain pre-specified maturity. A prominent example of such a situation arises, for example, in the context of a pension fund’s liabilities.

### Related literature

The existing literature on optimal investment is too vast in order to give a complete overview. Instead, we focus on the specific area of utility-based hedging and pricing, which is closely aligned to our work.

An appealing choice of utility in this context is the exponential one, as it allows for closed-form results in various settings. This is due to its property of separating the value function into components associated with wealth and trading; simplifying the analysis considerably. Prominent works in this context include [[17](https://arxiv.org/html/2601.14139v2#bib.bib16 "Valuation of claims on nontraded assets using utility maximization")], [[43](https://arxiv.org/html/2601.14139v2#bib.bib21 "An example of indifference prices under exponential preferences")], [[9](https://arxiv.org/html/2601.14139v2#bib.bib31 "Indifference pricing and hedging for volatility derivatives")], and [[30](https://arxiv.org/html/2601.14139v2#bib.bib24 "Accounting for risk aversion in derivatives purchase timing")]. These studies leverage a linearization technique—commonly referred to as the Cole-Hopf transformation or distortion power—first introduced in claim valuation by [[48](https://arxiv.org/html/2601.14139v2#bib.bib25 "A solution approach to valuation with unhedgeable risks")], which reduces the resulting nonlinear HJB PDE to a linear form, solvable via standard methods. Further generalizations by [[7](https://arxiv.org/html/2601.14139v2#bib.bib29 "Exponential utility indifference valuation in two brownian settings with stochastic correlation")] and [[8](https://arxiv.org/html/2601.14139v2#bib.bib28 "Exponential utility indifference valuation in a general semimartingale model")] showed that, even in models with general asset dynamics, the exponential utility-based price admits an explicit expression; although these formulas are often less interpretable. Complementary to these results, [[5](https://arxiv.org/html/2601.14139v2#bib.bib13 "Optimal hedging with basis risk")] used duality techniques to derive an explicit form for the optimal hedging strategy; with related developments also appearing in [[37](https://arxiv.org/html/2601.14139v2#bib.bib33 "Malliavin calculus method for asymptotic expansion of dual control problems")].

Even within the relatively tractable exponential utility framework, explicit expressions are not always obtainable. For example, in models where the claim depends on the traded asset Sircar and Zariphopoulou [[47](https://arxiv.org/html/2601.14139v2#bib.bib36 "Bounds and asymptotic approximations for utility prices when volatility is random")] derive asymptotic expansions for the utility-indifference price in the context of fast mean-reverting volatility. Henderson and Liang [[16](https://arxiv.org/html/2601.14139v2#bib.bib37 "A multidimensional exponential utility indifference pricing model with applications to counterparty risk")] consider a multidimensional non-traded asset model subject to intertemporal default risk, and develop a semigroup approximation using splitting techniques.

Given the scarcity of explicit results, various asymptotic approaches have been proposed for pricing and hedging in incomplete markets. Monoyios [[34](https://arxiv.org/html/2601.14139v2#bib.bib14 "Performance of utility-based strategies for hedging basis risk"), [35](https://arxiv.org/html/2601.14139v2#bib.bib15 "Optimal hedging and parameter uncertainty")], for example, works within a Black-Scholes framework with basis risk and approximates the hedging strategy in powers of 1−ρ21-\rho^{2}, where ρ\rho denotes the correlation between traded and non-traded assets. In [[17](https://arxiv.org/html/2601.14139v2#bib.bib16 "Valuation of claims on nontraded assets using utility maximization")] and [[15](https://arxiv.org/html/2601.14139v2#bib.bib17 "Real options with constant relative risk aversion")] the authors consider the case of power utility and derive the second-order expansions of the investor’s value function with respect to a small position in the contingent claim, thereby approximating both the hedging strategy and reservation price.

These early results of Henderson and Hobson were significantly extended in [[28](https://arxiv.org/html/2601.14139v2#bib.bib18 "Sensitivity analysis of utility-based prices and risk-tolerance wealth processes"), [29](https://arxiv.org/html/2601.14139v2#bib.bib19 "Asymptotic analysis of utility-based hedging strategies for small number of contingent claims")], where the authors study a general semimartingale framework; under a broad class of utility functions defined on the positive real line. Particularly in [[28](https://arxiv.org/html/2601.14139v2#bib.bib18 "Sensitivity analysis of utility-based prices and risk-tolerance wealth processes")] they derive the second-order expansion of the value function which in turn is used to get a first order approximation for marginal (utility-based) indifference prices and study their qualitative features. A related analysis by Kallsen [[21](https://arxiv.org/html/2601.14139v2#bib.bib20 "Derivative pricing based on local utility maximization")] studies first order marginal price approximations under local utility maximization.

In [[29](https://arxiv.org/html/2601.14139v2#bib.bib19 "Asymptotic analysis of utility-based hedging strategies for small number of contingent claims")], using techniques developed in their earlier work, the authors also provide a first-order approximation of the utility-based hedging strategy w.r.t. the units held in the non-traded endowment and demonstrate its relation to quadratic hedging. Similar asymptotic results are found in [[36](https://arxiv.org/html/2601.14139v2#bib.bib40 "Utility-based valuation and hedging of basis risk with partial information")], which considers valuation and hedging in the presence of parameter uncertainty under exponential utility and partial information. Therein, the indifference price is approximated up to linear order in the risk aversion parameter via PDE methods.

In the same spirit, [[20](https://arxiv.org/html/2601.14139v2#bib.bib41 "Asymptotic utility-based pricing and hedging for exponential utility")] analyzes utility-based pricing and hedging under exponential utility for a vanishing risk aversion. [[19](https://arxiv.org/html/2601.14139v2#bib.bib44 "Asymptotic power utility-based pricing and hedging")], focusing on exponential Lévy models, presents alternative representations of the results in [[28](https://arxiv.org/html/2601.14139v2#bib.bib18 "Sensitivity analysis of utility-based prices and risk-tolerance wealth processes"), [29](https://arxiv.org/html/2601.14139v2#bib.bib19 "Asymptotic analysis of utility-based hedging strategies for small number of contingent claims")] for power utility functions, that avoid the need for a change of numeraire.

Within the setting of exponential Lévy processes, [[31](https://arxiv.org/html/2601.14139v2#bib.bib45 "Asymptotic indifference pricing in exponential lévy models")] derives a non-asymptotic approximation for the exponential utility-based indifference price. The approach therein extends the earlier small risk-aversion asymptotics and yields a closed-form approximation by treating the Lévy model as a perturbation of the classical Black-Scholes framework.

There is also an associated strand of literature which conducts sensitivity analysis of the utility maximization problem w.r.t. other model perturbations. For example [[38](https://arxiv.org/html/2601.14139v2#bib.bib70 "Sensitivity analysis of the utility maximization problem with respect to model perturbations")] studies the sensitivity of the expected utility maximization problem in a continuous semimartingale market w.r.t. small changes in the market price of risk. [[42](https://arxiv.org/html/2601.14139v2#bib.bib71 "Asymptotic analysis of the expected utility maximization problem with respect to perturbations of the numeraire")] investigates the behavior of the expected utility maximization problem under small perturbations of the numeraire, while [[39](https://arxiv.org/html/2601.14139v2#bib.bib72 "Quadratic expansions in optimal investment with respect to perturbations of the semimartingale model")] study the response of the optimal investment problem to small changes of the stock price dynamics.

### Structure of the paper

This paper is organized as follows: in §2 the setup of the model is given; therein dynamics for the financial market, investment opportunities and illiquid asset are explained. In §3 we perform the fourth order expansion for the value function u​(ϵ)u(\epsilon) of the problem of optimal investment with a random endowment. This section lays the foundation for subsequent results. In §4 we derive the second order expansion for the optimal wealth XϵX^{\epsilon}, i.e. the unique solution of u​(ϵ)u(\epsilon). Both in §3 and in §4, the cases of finite and infinite horizon are treated simultaneously. We conclude with a discussion of derived results as well as a concrete example, presented in §5.

## 1. Setup

### 1.1. The financial market

Fix a probability space (Ω,ℱ,ℙ)(\Omega,\mathscr{F},\mathbb{P}) equipped with a filtration ℱ​(⋅)\mathscr{F}(\cdot) satisfying the usual conditions, s.t. ℱ​(0)\mathscr{F}(0) is trivial a.s. We set:

|  |  |  |
| --- | --- | --- |
|  | ℱ​(∞):=σ​(⋃t∈ℝ≥0ℱ​(t))⊆ℱ,\mathscr{F}(\infty):=\sigma\bigg(\bigcup\_{t\in\mathbb{R}\_{\geq 0}}\mathscr{F}(t)\bigg)\subseteq\mathscr{F}, |  |

and work within the infinite horizon setting, i.e. ℝ≥0=[0,∞)\mathbb{R}\_{\geq 0}=[0,\infty), since any finite time horizon can be naturally embedded in it. Unless otherwise explicitly stated, identities or inequalities involving random variables are interpreted as being valid almost everywhere under ℙ\mathbb{P}. Similarly, comparisons between processes will be understood up to indistinguishability. Moreover for f:Ω→ℝf:\Omega\rightarrow\mathbb{R}, let f+:=max⁡(f,0)f^{+}:=\max(f,0), f−:=max⁡(−f,0)f^{-}:=\max(-f,0) and for p≥1p\geq 1, denote the class of Lebesgue pp-integrable functions in (Ω,ℱ,ℙ)(\Omega,\mathscr{F},\mathbb{P}) by ℒp\mathscr{L}\_{p}. In cases where it is important to underline that the sigma algebra is different than ℱ\mathscr{F}, it will be stated explicitly.

Consider an agent that trades in 1+d∈ℕ>01+d\in\mathbb{N}\_{>0} assets; a baseline with stochastic exponential price S~0\widetilde{S}\_{0}, driven by a continuous finite variation process R0R\_{0} s.t. R0​(0)=0R\_{0}(0)=0 and dd risky assets. Discounting by S~0\widetilde{S}\_{0} we denote the cumulative returns of the risky assets, relative to the baseline, by R=(Ri;1≤i≤d)R=(R\_{i};1\leq i\leq d) and assume they satisfy the following continuous semimartingale dynamics:

|  |  |  |
| --- | --- | --- |
|  | Ri=Ai+Mi,1≤i≤d.R\_{i}=A\_{i}+M\_{i},\qquad 1\leq i\leq d. |  |

Here, each real-valued component AiA\_{i} of the vector-valued A=(Ai;1≤i≤d)A=(A\_{i};1\leq i\leq d) is a continuous finite variation process with Ai​(0)=0A\_{i}(0)=0, whereas each MiM\_{i} in M=(Mi;1≤i≤d)M=(M\_{i};1\leq i\leq d) is a continuous local martingale with Mi​(0)=0M\_{i}(0)=0. In turn, the prices of the risky assets S~=(S~i;1≤i≤d)\widetilde{S}=(\widetilde{S}\_{i};1\leq i\leq d), discounted by S~0\widetilde{S}\_{0}, satisfy:

|  |  |  |
| --- | --- | --- |
|  | S~i=S~i​(0)​ℰ​(Ri),S~i​(0)>0,1≤i≤d,\widetilde{S}\_{i}=\widetilde{S}\_{i}(0)\mathscr{E}(R\_{i}),\qquad\widetilde{S}\_{i}(0)>0,\qquad 1\leq i\leq d, |  |

where ℰ​(⋅)\mathscr{E}(\cdot) denotes the stochastic exponential.

We introduce the continuous, nondecreasing scalar process:

|  |  |  |
| --- | --- | --- |
|  | O:=∑i=1d(∫0⋅|d​Ai​(t)|+[Mi]),O:=\sum\_{i=1}^{d}\left(\int\_{0}^{\cdot}|dA\_{i}(t)|+[M\_{i}]\right), |  |

with ∫0S|d​Ai​(t)|\int\_{0}^{S}|dA\_{i}(t)| denoting the total variation of AiA\_{i} on the interval [0,S][0,S], for S>0S>0. This scalar process OO plays the role of an “operational clock” for the vector semimartingale RR: all processes AiA\_{i} and [Mi,Mj][M\_{i},M\_{j}] for 1≤i≤d1\leq i\leq d and 1≤j≤d1\leq j\leq d are absolutely continuous w.r.t. this clock (i.e. the respective induced measures). Hence, there exist predictable processes a=(ai;1≤i≤d)a=(a\_{i};1\leq i\leq d) and c=(ci​j;1≤i,j≤d)c=(c\_{ij};1\leq i,j\leq d), s.t.:

|  |  |  |
| --- | --- | --- |
|  | A=∫0⋅a​(t)​𝑑O​(t),[M]=∫0⋅c​(t)​𝑑O​(t).A=\int\_{0}^{\cdot}a(t)dO(t),\qquad[M]=\int\_{0}^{\cdot}c(t)dO(t). |  |

By altering it on a (ℙ⊗O)(\mathbb{P}\otimes O)-null set if necessary, we shall assume throughout that the process cc takes values in the space of symmetric, nonnegative-definite, d×dd\times d matrices.

### 1.2. Investment opportunities

In the market (1,S~)(1,\widetilde{S}), an initial capital x∈ℝx\in\mathbb{R} and a choice of a (self-financing) strategy θ=(θi;1≤i≤d)\theta=(\theta\_{i};1\leq i\leq d) (assumed to be predictable and S~\widetilde{S}-vector integrable) result in a wealth process:

|  |  |  |  |
| --- | --- | --- | --- |
| (1.1) |  | X~​(⋅;x,θ):=x+∫0⋅θ​(t)​𝑑S~​(t),\widetilde{X}(\cdot;x,\theta):=x+\int\_{0}^{\cdot}\theta(t)d\widetilde{S}(t)\ , |  |

where the above is understood as a vector stochastic integral. To avoid the so-called doubling strategies, we restrict the above class as follows: a wealth process X~\widetilde{X} with initial capital X~​(0)=x\widetilde{X}(0)=x is called admissible if:

X~>0\widetilde{X}>0.

We denote this subset of wealth processes by 𝒳~​(x)\widetilde{\mathscr{X}}(x). The union ∪x>0𝒳~​(x)\cup\_{x>0}\widetilde{\mathscr{X}}(x) is denoted by 𝒳~\widetilde{\mathscr{X}}.

The market’s viability is intimately connected to the following condition, as shown in [[22](https://arxiv.org/html/2601.14139v2#bib.bib6 "Portfolio theory and arbitrage: a course in mathematical finance"), Theorem 2.31]:

|  |  |  |  |
| --- | --- | --- | --- |
| (A1) |  | cc is non-singular, (ℙ⊗O)(\mathbb{P}\otimes O)-a.e. and ∫0K(a​(t))′​(c​(t))−1​a​(t)​𝑑O​(t)<∞\int\_{0}^{K}(a(t))^{{}^{\prime}}(c(t))^{-1}a(t)dO(t)<\infty, ∀K>0\forall K>0. |  |

In particular, the above condition implies the existence of the supermartingale numeraire; denote it by Xπ⋆:=ℰ​(Rπ⋆)X\_{\pi^{\star}}:=\mathscr{E}(R^{\pi^{\star}}), where Rπ⋆:=∫0⋅(π⋆​(t))′​𝑑R​(t)R^{\pi^{\star}}:=\int\_{0}^{\cdot}(\pi^{\star}(t))^{{}^{\prime}}dR(t) and π⋆:=c−1​a\pi^{\star}:=c^{-1}a (refer to §2 in [[22](https://arxiv.org/html/2601.14139v2#bib.bib6 "Portfolio theory and arbitrage: a course in mathematical finance")] for further details on this concept). Note that Xπ⋆X\_{\pi^{\star}} can be used as a new numeraire, under which each X~∈𝒳~\widetilde{X}\in\widetilde{\mathscr{X}} becomes a local martingale. In fact, by considering the auxiliary market:

|  |  |  |
| --- | --- | --- |
|  | S:=(S0:=1Xπ⋆,S:=S~Xπ⋆),S:=\left(S\_{0}:=\frac{1}{X\_{\pi^{\star}}},S:=\frac{\widetilde{S}}{X\_{\pi^{\star}}}\right), |  |

we have for each wealth process X~\widetilde{X} in (1,S~)(1,\widetilde{S}):

|  |  |  |  |
| --- | --- | --- | --- |
| (1.2) |  | X~/Xπ⋆=x+∫0⋅∑i=1dθi​(t)​d​Si​(t)+∫0⋅(X~​(t)/Xπ⋆​(t)−∑i=1dθi​(t)​Si​(t))​d​S0​(t)S0​(t),\widetilde{X}/X\_{\pi^{\star}}=x+\int\_{0}^{\cdot}\sum\_{i=1}^{d}\theta\_{i}(t)dS\_{i}(t)+\int\_{0}^{\cdot}\left(\widetilde{X}(t)/X\_{\pi^{\star}}(t)-\sum\_{i=1}^{d}\theta\_{i}(t)S\_{i}(t)\right)\frac{dS\_{0}(t)}{S\_{0}(t)}, |  |

where SS is a ℝ1+d\mathbb{R}^{1+d}-valued local martingale.

### 1.3. Illiquid asset

Besides trading in the financial market, the agent holds ϵ∈ℝ≥0\epsilon\in\mathbb{R}\_{\geq 0} units of an exogenous, non-traded cumulative stream Λ\Lambda that is absolutely continuous on ℝ≥0\mathbb{R}\_{\geq 0}, given in discounted terms (w.r.t. S~0\widetilde{S}\_{0}) by:

|  |  |  |
| --- | --- | --- |
|  | Λ=∫0⋅λ​(t)/S~0​(t)​𝑑t,\Lambda=\int\_{0}^{\cdot}\lambda(t)/\widetilde{S}\_{0}(t)dt, |  |

for a predictable process λ\lambda. The only regularity assumption on the illiquid asset is that it can be super and subreplicated using the traded asset S~\widetilde{S}. In other words, we use the following standing assumption:

|  |  |  |  |
| --- | --- | --- | --- |
| (A2) |  | {X~∈𝒳~:|Λ​(T)|≤X~​(T)}≠∅\{\widetilde{X}\in\widetilde{\mathscr{X}}:|\Lambda(T)|\leq\widetilde{X}(T)\}\neq\emptyset, |  |

where TT is any a.s. finite stopping time.

###### Remark 1.1.

Note that the non-traded asset Λ\Lambda, expressed under the numeraire Xπ⋆X\_{\pi^{\star}}, is given by L:=Λ/Xπ⋆L:=\Lambda/X\_{\pi^{\star}}. Now, integration by parts yields:

|  |  |  |  |
| --- | --- | --- | --- |
| (1.3) |  | L=∫0⋅Λ​(t)​𝑑S0​(t)+F,L=\int\_{0}^{\cdot}\Lambda(t)dS\_{0}(t)+F, |  |

F:=∫0⋅S0​(t)​𝑑Λ​(t)F:=\int\_{0}^{\cdot}S\_{0}(t)d\Lambda(t). In turn, we have for a wealth process X~\widetilde{X}, with initial capital xx, that:

|  |  |  |
| --- | --- | --- |
|  | X~/Xπ⋆−∫0⋅Λ​(t)​𝑑S0​(t),\widetilde{X}/X\_{\pi^{\star}}-\int\_{0}^{\cdot}\Lambda(t)dS\_{0}(t), |  |

is simply ([1.2](https://arxiv.org/html/2601.14139v2#S1.E2 "In 1.2. Investment opportunities ‣ 1. Setup ‣ Log-optimality with small liability stream")) with a shifted position in S0S\_{0}. In other words, when considering the illiquid asset discounted by the supermartingale numeraire, the non-replicable part of LL comes solely from FF.

### 1.4. Utility maximization problem

Fix any stopping time TT s.t. either T<∞T<\infty or T=∞T=\infty, that will serve as the maturity of the agent. We focus on the model (S,F)(S,F) in the sequel. Therein an initial capital x∈ℝx\in\mathbb{R} and a choice of θ=(θi;1≤i≤d)\theta=(\theta\_{i};1\leq i\leq d) (assumed to be predictable and SS-integrable) result in a wealth process in SS:

|  |  |  |  |
| --- | --- | --- | --- |
| (1.4) |  | X​(⋅;x,θ):=x+∫0⋅θ​(t)​𝑑S​(t).X(\cdot;x,\theta):=x+\int\_{0}^{\cdot}\theta(t)dS(t). |  |

Hence, all processes of the form shown in ([1.2](https://arxiv.org/html/2601.14139v2#S1.E2 "In 1.2. Investment opportunities ‣ 1. Setup ‣ Log-optimality with small liability stream")) are in fact wealth processes in SS. The subset of admissible processes will be characterized by:

|  |  |  |
| --- | --- | --- |
|  | X>0X>0 on ⟦0,T⟧:={(ω,t)∈Ω×ℝ≥0:t≤T​(ω)}\llbracket 0,T\rrbracket:=\{(\omega,t)\in\Omega\times\mathbb{R}\_{\geq 0}:t\leq T(\omega)\}, |  |

which shall be denoted by 𝒳​(x)\mathscr{X}(x) and its union ∪x>0𝒳​(x)\cup\_{x>0}\mathscr{X}(x) by 𝒳\mathscr{X}. In this context, following [[6](https://arxiv.org/html/2601.14139v2#bib.bib1 "The banach space of workable contingent claims in arbitrage theory")], a process X∈𝒳X\in\mathscr{X} is called maximal if for each X′∈𝒳X^{{}^{\prime}}\in\mathscr{X} s.t. X′​(T)≥X​(T)X^{{}^{\prime}}(T)\geq X(T) and X′​(0)=X​(0)X^{{}^{\prime}}(0)=X(0), we necessarily have X′=XX^{{}^{\prime}}=X. Lastly, a wealth process in SS, XX is called acceptable if there exists a maximal process X′∈𝒳X^{{}^{\prime}}\in\mathscr{X} s.t. X+X′∈𝒳X+X^{{}^{\prime}}\in\mathscr{X}. Note that when the horizon is infinite, for each X∈𝒳X\in\mathscr{X} we have X​(∞):=limt→∞X​(t)X(\infty):=\lim\_{t\rightarrow\infty}X(t) a.s., by the fact that XX is a continuous positive local martingale. Hence for any acceptable process XX, limt→∞X​(t)\lim\_{t\rightarrow\infty}X(t) exists a.s. in that case since X=X′−X′′X=X^{{}^{\prime}}-X^{{}^{\prime\prime}}, where X′∈𝒳X^{{}^{\prime}}\in\mathscr{X} and X′′X^{{}^{\prime\prime}} is maximal.

Assuming:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (A3) |  |  | limt→∞F​(t)\lim\_{t\rightarrow\infty}F(t) exists a.s., and |  |
|  |  | {X∈𝒳:|F​(T)|≤X​(T)}≠∅\{X\in\mathscr{X}:|F(T)|\leq X(T)\}\neq\emptyset, |  |

we define the following class:

|  |  |  |
| --- | --- | --- |
|  | 𝒳​(x,ϵ):={X a wealth process in S:X is acceptable, X​(0)=x and X​(T)−ϵ​F​(T)>0}.\mathscr{X}(x,\epsilon):=\{\text{$X$ a wealth process in $S$}:\text{$X$ is acceptable, $X(0)=x$ and $X(T)-\epsilon F(T)>0$}\}. |  |

From the definition of acceptable processes, we also deduce that:

|  |  |  |
| --- | --- | --- |
|  | 𝒳​(x,0)=𝒳​(x),x>0.\mathscr{X}(x,0)=\mathscr{X}(x),\qquad x>0. |  |

The set of points (x,ϵ)(x,\epsilon) where 𝒳​(x,ϵ)\mathscr{X}(x,\epsilon) is not empty is a closed convex cone in ℝ2\mathbb{R}^{2}. Denote its interior by 𝒦:={(x,ϵ):𝒳​(x,ϵ)≠∅}o\mathscr{K}:=\{(x,\epsilon):\mathscr{X}(x,\epsilon)\neq\emptyset\}^{\mathrm{o}} and note, as shown in [[18](https://arxiv.org/html/2601.14139v2#bib.bib4 "Optimal investment with random endowments in incomplete markets")], that ([A3](https://arxiv.org/html/2601.14139v2#S1.Ex12 "In 1.4. Utility maximization problem ‣ 1. Setup ‣ Log-optimality with small liability stream")) implies (x,0)∈𝒦(x,0)\in\mathscr{K}, x>0x>0.
In turn consider:

|  |  |  |
| --- | --- | --- |
|  | u​(x,ϵ):=supX∈𝒳​(x,ϵ)𝔼​[ln⁡(X​(T)−ϵ​F​(T))],u(x,\epsilon):=\sup\_{X\in\mathscr{X}(x,\epsilon)}\mathbb{E}[\ln(X(T)-\epsilon F(T))], |  |

i.e. the log-optimization problem in (S,F)(S,F). To avoid the trivial case we need:

|  |  |  |
| --- | --- | --- |
|  | We have u​(x,ϵ)<∞u(x,\epsilon)<\infty, for some (x,ϵ)∈𝒦(x,\epsilon)\in\mathscr{K}, |  |

In fact the above should always hold for the case of log-utility in this context. To see that note (x,0)∈𝒦(x,0)\in\mathscr{K} for any x>0x>0 under ([A3](https://arxiv.org/html/2601.14139v2#S1.Ex12 "In 1.4. Utility maximization problem ‣ 1. Setup ‣ Log-optimality with small liability stream")), as shown in [[18](https://arxiv.org/html/2601.14139v2#bib.bib4 "Optimal investment with random endowments in incomplete markets")]. In particular for any such point we have 𝒳​(x,0)=𝒳​(x)\mathscr{X}(x,0)=\mathscr{X}(x). Using the inequality ln⁡(x)≤x−1,x>0\ln(x)\leq x-1,\ x>0 and the fact that 𝔼​[X​(T)]≤x\mathbb{E}[X(T)]\leq x for X∈𝒳​(x)X\in\mathscr{X}(x) shows the claim. The concavity of u​(x,ϵ)u(x,\epsilon) on the open set 𝒦\mathscr{K} finally gives that u​(x,ϵ)<∞u(x,\epsilon)<\infty for all (x,ϵ)∈𝒦(x,\epsilon)\in\mathscr{K}.

In turn, following [[18](https://arxiv.org/html/2601.14139v2#bib.bib4 "Optimal investment with random endowments in incomplete markets")], since the log-utility satisfies the asymptotic elasticity condition, i.e. for U​(x):=ln⁡(x)U(x):=\ln(x) we have lim¯x→∞⁡x​U′​(x)/U​(x)<1\operatorname\*{\overline{lim}}\_{x\rightarrow\infty}xU^{{}^{\prime}}(x)/U(x)<1, SS trivially satisfies the condition of NFLVR and we also have ([A3](https://arxiv.org/html/2601.14139v2#S1.Ex12 "In 1.4. Utility maximization problem ‣ 1. Setup ‣ Log-optimality with small liability stream")); the solution to u​(x,ϵ)u(x,\epsilon) exists and is unique. We focus on:

|  |  |  |  |
| --- | --- | --- | --- |
| (1.5) |  | u​(ϵ):=u​(1,ϵ)=𝔼​[ln⁡(1+Xϵ​(T)−ϵ​F​(T))],u(\epsilon):=u(1,\epsilon)=\mathbb{E}[\ln(1+X^{\epsilon}(T)-\epsilon F(T))], |  |

where Xϵ​(T)X^{\epsilon}(T) denotes the shifted counterpart of the solution of u​(1,ϵ)u(1,\epsilon) s.t. it starts from zero.

###### Remark 1.2.

Note that working with the optimization problem in (S,F)(S,F) doesn’t come with any loss of generality in this context, since by using the numeraire invariance of log-utility, along with (ln⁡(Xπ⋆​(T)))−∈ℒ1(\ln(X\_{\pi^{\star}}(T)))^{-}\in\mathscr{L}\_{1} as well as ([A2](https://arxiv.org/html/2601.14139v2#S1.Ex9 "In 1.3. Illiquid asset ‣ 1. Setup ‣ Log-optimality with small liability stream")) and ([A3](https://arxiv.org/html/2601.14139v2#S1.Ex12 "In 1.4. Utility maximization problem ‣ 1. Setup ‣ Log-optimality with small liability stream")) yields that the unique solution to the respective optimization problem of u​(ϵ)u(\epsilon) in (1,S~,Λ)(1,\widetilde{S},\Lambda), denoted by X~ϵ\widetilde{X}^{\epsilon}, is given as:

|  |  |  |
| --- | --- | --- |
|  | X~ϵ​(T)=Xπ⋆​(T)​(1+Xϵ​(T)+ϵ​∫0TΛ​(t)​𝑑S0​(t)),\widetilde{X}^{\epsilon}(T)=X\_{\pi^{\star}}(T)\left(1+X^{\epsilon}(T)+\epsilon\int\_{0}^{T}\Lambda(t)dS\_{0}(t)\right), |  |

for any a.s. finite stopping time TT. Even if the ”original” utility maximization problem in (1,S~,Λ)(1,\widetilde{S},\Lambda) is not well-defined for potentially infinite TT, due to it taking infinite value, it is still well-defined for the numeraire-discounted market. Hence it is preferable to work with the latter for long time horizon settings.

## 2. Fourth order expansion of value function w.r.t. ϵ\epsilon

For p≥1p\geq 1 denote the class of (local) martingales s.t. for each MM we have 𝔼​[(M¯​(T))p]<∞\mathbb{E}[(\overline{M}(T))^{p}]<\infty by ℋp\mathscr{H}\_{p}; where M¯:=supt∈[0,⋅]|M​(t)|\overline{M}:=\sup\_{t\in[0,\cdot]}|M(t)|. Using the above, define:

|  |  |  |
| --- | --- | --- |
|  | ℳp:={M∈ℋp:M​(0)=0 and M=∫0⋅θ​(t)​𝑑S​(t)}.\displaystyle\mathscr{M}\_{p}:=\left\{M\in\mathscr{H}\_{p}:\text{$M(0)=0$ and $M=\int\_{0}^{\cdot}\theta(t)dS(t)$}\right\}. |  |

As it is discussed in [[28](https://arxiv.org/html/2601.14139v2#bib.bib18 "Sensitivity analysis of utility-based prices and risk-tolerance wealth processes")] the following assumption is crucial in order to derive the second order expansion of the value function (with a non-traded endowment), and particularly its lower bound:

|  |  |  |
| --- | --- | --- |
|  | ∃x>0\exists x>0 and M∈ℳ2M\in\mathscr{M}\_{2} s.t. |L​(T)|≤x+M​(T)|L(T)|\leq x+M(T). |  |

In our context, where we go up to fourth order on the value function, the aforementioned is naturally extended to the following stronger version:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (A3II) |  |  | limt→∞F​(t)\lim\_{t\rightarrow\infty}F(t) exists a.s., and |  |
|  |  | ∃x>0\exists x>0 and M∈ℳ4M\in\mathscr{M}\_{4} s.t. |F​(T)|≤x+M​(T).|F(T)|\leq x+M(T). |  |

Moving forward, the key tools for the fourth order expansion of u​(ϵ)u(\epsilon) are two Kunita-Watanabe (K-W) projections. Denote by ℱ​(T)\mathscr{F}(T) the “stopped” sigma-algebra at TT, i.e.:

|  |  |  |
| --- | --- | --- |
|  | ℱ​(T)={A∈ℱ​(∞):A∩{T≤t}∈ℱ​(t)​for all t≥0},\mathscr{F}(T)=\left\{A\in\mathscr{F}(\infty):A\cap\{T\leq t\}\in\mathscr{F}(t)\ \text{for all $t\geq 0$}\right\}, |  |

where the restriction to sets in ℱ​(∞)\mathscr{F}(\infty) is to take into account the possibility of the stopping time being infinite. Now, as FF is progressive (in ℝ≥0\mathbb{R}\_{\geq 0}) and F​(∞)F(\infty) is ℱ​(∞)\mathscr{F}(\infty)-measurable we have that F​(T)F(T) is ℱ​(T)\mathscr{F}(T)-measurable. In fact, when we have an a.s. infinite horizon it holds that ℱ​(T)=ℱ​(∞)\mathscr{F}(T)=\mathscr{F}(\infty). In particular, as F​(T)∈ℒ2​(ℱ​(T))F(T)\in\mathscr{L}\_{2}(\mathscr{F}(T)) it admits an orthogonal projection on the space of stochastic integrals w.r.t. SS that start at zero. In turn, this gives rise to the following K-W decomposition:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[F​(T)|ℱ​(⋅)]=Δ+N,\mathbb{E}[F(T)|\mathscr{F}(\cdot)]=\Delta+N, |  |

where NN is strongly orthogonal to Δ\Delta and N​(0)=𝔼​[F​(T)]N(0)=\mathbb{E}[F(T)]. Assuming:

|  |  |  |  |
| --- | --- | --- | --- |
| (A4) |  | 𝔼​[(N​(T))4]<∞,\mathbb{E}[(N(T))^{4}]<\infty, |  |

and applying similar reasoning to the above, we have:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[(N​(T))2|ℱ​(⋅)]=Γ+P,\mathbb{E}[(N(T))^{2}|\mathscr{F}(\cdot)]=\Gamma+P, |  |

where PP is strongly orthogonal to Γ\Gamma, which is a stochastic integral w.r.t. SS, and P​(0)=𝔼​[(N​(T))2]P(0)=\mathbb{E}[(N(T))^{2}]. In fact, by ([A3II](https://arxiv.org/html/2601.14139v2#S2.Ex3 "In 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")) and ([A4](https://arxiv.org/html/2601.14139v2#S2.Ex6 "In 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")) we have Δ,N∈ℋ4\Delta,N\in\mathscr{H}\_{4} and Γ,P∈ℋ2\Gamma,P\in\mathscr{H}\_{2}.

###### Theorem 2.1.

Assume ([A1](https://arxiv.org/html/2601.14139v2#S1.Ex6 "In 1.2. Investment opportunities ‣ 1. Setup ‣ Log-optimality with small liability stream")), ([A3II](https://arxiv.org/html/2601.14139v2#S2.Ex3 "In 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")) and ([A4](https://arxiv.org/html/2601.14139v2#S2.Ex6 "In 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")); then we have:

|  |  |  |  |
| --- | --- | --- | --- |
| (2.1) |  | u​(ϵ)+ϵ​𝔼​[F​(T)]+ϵ22​𝔼​[(N​(T))2]+ϵ33​𝔼​[(N​(T))3]+ϵ44​𝔼​[(N​(T))4]+ϵ4​𝔼​[(Γ​(T))2/2−(N​(T))2​Γ​(T)]=o​(ϵ4),u(\epsilon)+\epsilon\mathbb{E}[F(T)]+\frac{\epsilon^{2}}{2}\mathbb{E}[(N(T))^{2}]+\frac{\epsilon^{3}}{3}\mathbb{E}[(N(T))^{3}]+\frac{\epsilon^{4}}{4}\mathbb{E}[(N(T))^{4}]+\epsilon^{4}\mathbb{E}[(\Gamma(T))^{2}/2-(N(T))^{2}\Gamma(T)]=o(\epsilon^{4}), |  |

as ϵ→0+\epsilon\rightarrow 0+.

###### Proof.

We do some general setup that will be useful in deriving both bounds for the value function u​(ϵ)u(\epsilon).

Let x+Mx+M be the martingale implied by ([A3II](https://arxiv.org/html/2601.14139v2#S2.Ex3 "In 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")). Define:

|  |  |  |
| --- | --- | --- |
|  | ϵL:=1∧16​x∧14​|𝔼​[F​(T)]|∧12​(P​(0))1/2.\epsilon^{L}:=1\land\frac{1}{6x}\land\frac{1}{4|\mathbb{E}[F(T)]|}\land\frac{1}{2(P(0))^{1/2}}. |  |

For ϵ∈(0,ϵL)\epsilon\in(0,\epsilon^{L}), consider the stopping times:

|  |  |  |
| --- | --- | --- |
|  | τϵΔ:=inf{t:|Δ​(t)|≥1/6​ϵ},τϵΓ:=inf{t:|Γ​(t)|≥1/6​ϵ2},\displaystyle\tau\_{\epsilon}^{\Delta}:=\inf\{t:|\Delta(t)|\geq 1/6\epsilon\},\qquad\tau\_{\epsilon}^{\Gamma}:=\inf\{t:|\Gamma(t)|\geq 1/6\epsilon^{2}\}, |  |
|  |  |  |
| --- | --- | --- |
|  | τϵN:=inf{t:|N​(t)|≥1/4​ϵ},τϵM:=inf{t:x+M​(t)≥1/6​ϵ},\displaystyle\tau\_{\epsilon}^{N}:=\inf\{t:|N(t)|\geq 1/4\epsilon\},\qquad\tau\_{\epsilon}^{M}:=\inf\{t:x+M(t)\geq 1/6\epsilon\}, |  |
|  |  |  |
| --- | --- | --- |
|  | τϵP:=inf{t:|P​(t)|≥1/4​ϵ2},\displaystyle\tau\_{\epsilon}^{P}:=\inf\{t:|P(t)|\geq 1/4\epsilon^{2}\}, |  |

and τϵ:=τϵΔ∧τϵΓ∧τϵN∧τϵM∧τϵP\tau\_{\epsilon}:=\tau\_{\epsilon}^{\Delta}\land\tau\_{\epsilon}^{\Gamma}\land\tau\_{\epsilon}^{N}\land\tau\_{\epsilon}^{M}\land\tau\_{\epsilon}^{P}. Now noting that for a non-negative random variable ζ\zeta with 𝔼​[ζp]<∞\mathbb{E}[\zeta^{p}]<\infty and p>0p>0 implies:

|  |  |  |
| --- | --- | --- |
|  | limz→∞zp​ℙ​(ζ>z)=0,\lim\_{z\rightarrow\infty}z^{p}\mathbb{P}(\zeta>z)=0, |  |

we have:

|  |  |  |
| --- | --- | --- |
|  | limϵ→0+1ϵ4​ℙ​(τϵΔ≤T)=0,limϵ→0+1ϵ4​ℙ​(τϵΓ≤T)=0,\displaystyle\lim\_{\epsilon\rightarrow 0+}\frac{1}{\epsilon^{4}}\mathbb{P}(\tau\_{\epsilon}^{\Delta}\leq T)=0,\qquad\lim\_{\epsilon\rightarrow 0+}\frac{1}{\epsilon^{4}}\mathbb{P}(\tau\_{\epsilon}^{\Gamma}\leq T)=0, |  |
|  |  |  |
| --- | --- | --- |
|  | limϵ→0+1ϵ4​ℙ​(τϵN≤T)=0,limϵ→0+1ϵ4​ℙ​(τϵM≤T)=0,\displaystyle\lim\_{\epsilon\rightarrow 0+}\frac{1}{\epsilon^{4}}\mathbb{P}(\tau\_{\epsilon}^{N}\leq T)=0,\qquad\lim\_{\epsilon\rightarrow 0+}\frac{1}{\epsilon^{4}}\mathbb{P}(\tau\_{\epsilon}^{M}\leq T)=0, |  |
|  |  |  |
| --- | --- | --- |
|  | limϵ→0+1ϵ4​ℙ​(τϵP≤T)=0,\displaystyle\lim\_{\epsilon\rightarrow 0+}\frac{1}{\epsilon^{4}}\mathbb{P}(\tau\_{\epsilon}^{P}\leq T)=0, |  |

since Δ,N,M∈ℋ4\Delta,N,M\in\mathscr{H}\_{4} and Γ,P∈ℋ2\Gamma,P\in\mathscr{H}\_{2}. In particular the above also give:

|  |  |  |  |
| --- | --- | --- | --- |
| (2.2) |  | limϵ→0+1ϵ4​ℙ​(τϵ≤T)=0.\lim\_{\epsilon\rightarrow 0+}\frac{1}{\epsilon^{4}}\mathbb{P}(\tau\_{\epsilon}\leq T)=0. |  |

The lower bound

Now note that:

|  |  |  |
| --- | --- | --- |
|  | 1+ϵ​(Δτϵ+M−Mτϵ)+ϵ2​Γτϵ∈𝒳​(1,ϵ).1+\epsilon(\Delta^{\tau\_{\epsilon}}+M-M^{\tau\_{\epsilon}})+\epsilon^{2}\Gamma^{\tau\_{\epsilon}}\in\mathscr{X}(1,\epsilon). |  |

In turn, Taylor expansion and the above give:

|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(ϵ)\displaystyle u(\epsilon) | ≥𝔼​[ln⁡(1+ϵ​(Δτϵ​(T)+M​(T)−Mτϵ​(T)−F​(T))+ϵ2​Γτϵ​(T))]\displaystyle\geq\mathbb{E}\left[\ln\left(1+\epsilon\left(\Delta^{\tau\_{\epsilon}}(T)+M(T)-M^{\tau\_{\epsilon}}(T)-F(T)\right)+\epsilon^{2}\Gamma^{\tau\_{\epsilon}}(T)\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−ϵ​𝔼​[F​(T)]−12​𝔼​[(ϵ​(Δτϵ​(T)+M​(T)−Mτϵ​(T)−F​(T))+ϵ2​Γτϵ​(T))2]\displaystyle=-\epsilon\mathbb{E}[F(T)]-\frac{1}{2}\mathbb{E}\left[\left(\epsilon\left(\Delta^{\tau\_{\epsilon}}(T)+M(T)-M^{\tau\_{\epsilon}}(T)-F(T)\right)+\epsilon^{2}\Gamma^{\tau\_{\epsilon}}(T)\right)^{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +13​𝔼​[(ϵ​(Δτϵ​(T)+M​(T)−Mτϵ​(T)−F​(T))+ϵ2​Γτϵ​(T))3]\displaystyle+\frac{1}{3}\mathbb{E}\left[\left(\epsilon\left(\Delta^{\tau\_{\epsilon}}(T)+M(T)-M^{\tau\_{\epsilon}}(T)-F(T)\right)+\epsilon^{2}\Gamma^{\tau\_{\epsilon}}(T)\right)^{3}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −14​𝔼​[(ϵ​(Δτϵ​(T)+M​(T)−Mτϵ​(T)−F​(T))+ϵ2​Γτϵ​(T))4​ξϵL],\displaystyle-\frac{1}{4}\mathbb{E}\left[\left(\epsilon\left(\Delta^{\tau\_{\epsilon}}(T)+M(T)-M^{\tau\_{\epsilon}}(T)-F(T)\right)+\epsilon^{2}\Gamma^{\tau\_{\epsilon}}(T)\right)^{4}\xi\_{\epsilon}^{L}\right], |  |

where ξϵL\xi\_{\epsilon}^{L} is a r.v., s.t. limϵ→0+ξϵL=1\lim\_{\epsilon\rightarrow 0+}\xi\_{\epsilon}^{L}=1 a.s. and 0<ξϵL≤240<\xi\_{\epsilon}^{L}\leq 2^{4}, ∀ϵ∈(0,ϵL)\forall\epsilon\in(0,\epsilon^{L}). Hence, as it is bounded above, we can disregard it in the following estimates since it does not affect limits being zero as ϵ→0+\epsilon\rightarrow 0+.

Now define Qϵ:=Δτϵ+M−Mτϵ∈ℳ4Q^{\epsilon}:=\Delta^{\tau\_{\epsilon}}+M-M^{\tau\_{\epsilon}}\in\mathscr{M}\_{4}, where Qϵ​(T)→Δ​(T)Q^{\epsilon}(T)\rightarrow\Delta(T) almost surely as ϵ→0+\epsilon\rightarrow 0+ (similarly Γτϵ​(T)→Γ​(T)\Gamma^{\tau\_{\epsilon}}(T)\rightarrow\Gamma(T) a.s.). Collecting terms, we get:

|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(ϵ)\displaystyle u(\epsilon) | ≥−ϵ​𝔼​[F​(T)]−ϵ2​𝔼​[(Qϵ​(T)−F​(T))2/2]+ϵ3​𝔼​[(Qϵ​(T)−F​(T))3/3−Γτϵ​(T)​(Qϵ​(T)−F​(T))]\displaystyle\geq-\epsilon\mathbb{E}[F(T)]-\epsilon^{2}\mathbb{E}[(Q^{\epsilon}(T)-F(T))^{2}/2]+\epsilon^{3}\mathbb{E}[(Q^{\epsilon}(T)-F(T))^{3}/3-\Gamma^{\tau\_{\epsilon}}(T)(Q^{\epsilon}(T)-F(T))] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −ϵ4​𝔼​[(Qϵ​(T)−F​(T))4​ξϵL/4−(Qϵ​(T)−F​(T))2​Γτϵ​(T)+(Γτϵ​(T))2/2]\displaystyle-\epsilon^{4}\mathbb{E}[(Q^{\epsilon}(T)-F(T))^{4}\xi\_{\epsilon}^{L}/4-(Q^{\epsilon}(T)-F(T))^{2}\Gamma^{\tau\_{\epsilon}}(T)+(\Gamma^{\tau\_{\epsilon}}(T))^{2}/2] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +ϵ5​𝔼​[(Qϵ​(T)−F​(T))​(Γτϵ​(T))2−(Qϵ​(T)−F​(T))3​Γτϵ​(T)​ξϵL]\displaystyle+\epsilon^{5}\mathbb{E}[(Q^{\epsilon}(T)-F(T))(\Gamma^{\tau\_{\epsilon}}(T))^{2}-(Q^{\epsilon}(T)-F(T))^{3}\Gamma^{\tau\_{\epsilon}}(T)\xi\_{\epsilon}^{L}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +ϵ6​𝔼​[(Γτϵ​(T))3/3−(3/2)​(Qϵ​(T)−F​(T))2​(Γτϵ)2​ξϵL]−ϵ7​𝔼​[(Qϵ​(T)−F​(T))​(Γτϵ​(T))3​ξϵL]\displaystyle+\epsilon^{6}\mathbb{E}[(\Gamma^{\tau\_{\epsilon}}(T))^{3}/3-(3/2)(Q^{\epsilon}(T)-F(T))^{2}(\Gamma^{\tau\_{\epsilon}})^{2}\xi\_{\epsilon}^{L}]-\epsilon^{7}\mathbb{E}[(Q^{\epsilon}(T)-F(T))(\Gamma^{\tau\_{\epsilon}}(T))^{3}\xi\_{\epsilon}^{L}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −ϵ8​𝔼​[(Γτϵ​(T))4​ξϵL/4].\displaystyle-\epsilon^{8}\mathbb{E}[(\Gamma^{\tau\_{\epsilon}}(T))^{4}\xi\_{\epsilon}^{L}/4]. |  |

At this point we use the following result: let ζ\zeta be a non-negative r.v. and assume that 𝔼​[ζp1]<∞\mathbb{E}[\zeta^{p\_{1}}]<\infty holds for some p1>0p\_{1}>0. The, for all p2>0p\_{2}>0:

|  |  |  |  |
| --- | --- | --- | --- |
| (2.3) |  | limz→∞1zp2​𝔼​[ζp1+p2​𝟏ζ≤z]=0.\lim\_{z\rightarrow\infty}\frac{1}{z^{p\_{2}}}\mathbb{E}[\zeta^{p\_{1}+p\_{2}}\mathbf{1}\_{\zeta\leq z}]=0. |  |

We examine the above terms (w.r.t. to ϵ\epsilon) one by one, beginning with the highest order.

Eighth order term

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϵ4​(Γτϵ​(T))4\displaystyle\epsilon^{4}(\Gamma^{\tau\_{\epsilon}}(T))^{4} | =ϵ4​(Γτϵ​(T))4​𝟏τϵ≤T+ϵ4​(Γτϵ​(T))4​𝟏τϵ=∞\displaystyle=\epsilon^{4}(\Gamma^{\tau\_{\epsilon}}(T))^{4}\mathbf{1}\_{\tau\_{\epsilon}\leq T}+\epsilon^{4}(\Gamma^{\tau\_{\epsilon}}(T))^{4}\mathbf{1}\_{\tau\_{\epsilon}=\infty} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤1(6​ϵ)4​𝟏τϵ≤T+ϵ4​(Γ¯​(T))4​𝟏Γ¯​(T)≤1/6​ϵ2.\displaystyle\leq\frac{1}{(6\epsilon)^{4}}\mathbf{1}\_{\tau\_{\epsilon}\leq T}+\epsilon^{4}(\overline{\Gamma}(T))^{4}\mathbf{1}\_{\overline{\Gamma}(T)\leq 1/6\epsilon^{2}}. |  |

Hence:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϵ4​𝔼​[(Γτϵ​(T))4]\displaystyle\epsilon^{4}\mathbb{E}[(\Gamma^{\tau\_{\epsilon}}(T))^{4}] | ≤1(6​ϵ4)​ℙ​(τϵ≤T)+ϵ4​𝔼​[(Γ¯​(T))4​𝟏Γ¯​(T)≤1/6​ϵ2].\displaystyle\leq\frac{1}{(6\epsilon^{4})}\mathbb{P}(\tau\_{\epsilon}\leq T)+\epsilon^{4}\mathbb{E}\left[(\overline{\Gamma}(T))^{4}\mathbf{1}\_{\overline{\Gamma}(T)\leq 1/6\epsilon^{2}}\right]. |  |

In turn, limϵ→0+ϵ4​𝔼​[(Γτϵ​(T))4]=0\lim\_{\epsilon\rightarrow 0+}\epsilon^{4}\mathbb{E}[(\Gamma^{\tau\_{\epsilon}}(T))^{4}]=0 follows by ([2.2](https://arxiv.org/html/2601.14139v2#S2.E2 "In Proof. ‣ 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")), Γ∈ℳ2\Gamma\in\mathscr{M}\_{2} and ([2.3](https://arxiv.org/html/2601.14139v2#S2.E3 "In Proof. ‣ 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")) after a simple change of variables.

Seventh order term

Holder’s inequality gives:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϵ3​𝔼​[|Qϵ​(T)−F​(T)|​|Γτϵ​(T)|3]\displaystyle\epsilon^{3}\mathbb{E}[|Q^{\epsilon}(T)-F(T)||\Gamma^{\tau\_{\epsilon}}(T)|^{3}] | ≤(𝔼​[(|M​(T)−F​(T)|+supt∈[0,T]|Δ​(t)−M​(t)|)4])14​(𝔼​[(ϵ​Γτϵ​(T))4])34,\displaystyle\leq\bigg(\mathbb{E}\bigg[\bigg(\bigg|M(T)-F(T)\bigg|+\sup\_{t\in[0,T]}\bigg|\Delta(t)-M(t)\bigg|\bigg)^{4}\bigg]\bigg)^{\frac{1}{4}}\left(\mathbb{E}\left[(\epsilon\Gamma^{\tau\_{\epsilon}}(T))^{4}\right]\right)^{\frac{3}{4}}, |  |

where the first expectation is finite by ([A3II](https://arxiv.org/html/2601.14139v2#S2.Ex3 "In 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")), ([A4](https://arxiv.org/html/2601.14139v2#S2.Ex6 "In 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")) and:

|  |  |  |
| --- | --- | --- |
|  | limϵ→0+ϵ4​𝔼​[(Γτϵ​(T))4]=0,\lim\_{\epsilon\rightarrow 0+}\epsilon^{4}\mathbb{E}[(\Gamma^{\tau\_{\epsilon}}(T))^{4}]=0, |  |

by the previous result on the eight order term.

Sixth order terms

The first part follows similarly to the eight order term, since:

|  |  |  |
| --- | --- | --- |
|  | ϵ2​|Γτϵ​(T)|3≤163​ϵ4​𝟏τϵ≤T+ϵ2​(Γ¯​(T))3​𝟏Γ¯​(T)≤1/6​ϵ2.\epsilon^{2}|\Gamma^{\tau\_{\epsilon}}(T)|^{3}\leq\frac{1}{6^{3}\epsilon^{4}}\mathbf{1}\_{\tau\_{\epsilon}\leq T}+\epsilon^{2}(\overline{\Gamma}(T))^{3}\mathbf{1}\_{\overline{\Gamma}(T)\leq 1/6\epsilon^{2}}. |  |

Hence, as before, limϵ→0+ϵ2​𝔼​[|Γτϵ​(T)|3]=0\lim\_{\epsilon\rightarrow 0+}\epsilon^{2}\mathbb{E}[|\Gamma^{\tau\_{\epsilon}}(T)|^{3}]=0 follows by ([2.2](https://arxiv.org/html/2601.14139v2#S2.E2 "In Proof. ‣ 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")), Γ∈ℳ2\Gamma\in\mathscr{M}\_{2} and ([2.3](https://arxiv.org/html/2601.14139v2#S2.E3 "In Proof. ‣ 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")).

For the second part note that by Holder’s inequality we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϵ2​𝔼​[(Qϵ​(T)−F​(T))2​(Γτϵ​(T))2]\displaystyle\epsilon^{2}\mathbb{E}[(Q^{\epsilon}(T)-F(T))^{2}(\Gamma^{\tau\_{\epsilon}}(T))^{2}] | ≤(𝔼[(|M(T)−F(T)|\displaystyle\leq\bigg(\mathbb{E}\bigg[\bigg(\bigg|M(T)-F(T)\bigg| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +supt∈[0,T]|Δ(t)−M(t)|)4])12(𝔼[(ϵΓτϵ(T))4])12,\displaystyle+\sup\_{t\in[0,T]}\bigg|\Delta(t)-M(t)\bigg|\bigg)^{4}\bigg]\bigg)^{\frac{1}{2}}\left(\mathbb{E}\left[(\epsilon\Gamma^{\tau\_{\epsilon}}(T))^{4}\right]\right)^{\frac{1}{2}}, |  |

where the first expectation is finite by ([A3II](https://arxiv.org/html/2601.14139v2#S2.Ex3 "In 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")), ([A4](https://arxiv.org/html/2601.14139v2#S2.Ex6 "In 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")) and:

|  |  |  |
| --- | --- | --- |
|  | limϵ→0+ϵ4​𝔼​[(Γτϵ​(T))4]=0,\lim\_{\epsilon\rightarrow 0+}\epsilon^{4}\mathbb{E}[(\Gamma^{\tau\_{\epsilon}}(T))^{4}]=0, |  |

by the previous result on the eight order term.

Fifth order terms

For the first part we have that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϵ​𝔼​[(Qϵ​(T)−F​(T))​(Γτϵ​(T))2]\displaystyle\epsilon\mathbb{E}[(Q^{\epsilon}(T)-F(T))(\Gamma^{\tau\_{\epsilon}}(T))^{2}] | =𝔼​[𝔼​[(Qϵ​(T)−F​(T))​(Γτϵ​(T))2|ℱ​(T∧τϵ)]]\displaystyle=\mathbb{E}\left[\mathbb{E}\left[(Q^{\epsilon}(T)-F(T))(\Gamma^{\tau\_{\epsilon}}(T))^{2}\Big|\mathscr{F}(T\land\tau\_{\epsilon})\right]\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−𝔼​[ϵ​Nτϵ​(T)​(Γτϵ​(T))2].\displaystyle=-\mathbb{E}[\epsilon N^{\tau\_{\epsilon}}(T)(\Gamma^{\tau\_{\epsilon}}(T))^{2}]. |  |

Now note that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[|ϵ​Nτϵ​(T)|​(Γτϵ​(T))2]\displaystyle\mathbb{E}[|\epsilon N^{\tau\_{\epsilon}}(T)|(\Gamma^{\tau\_{\epsilon}}(T))^{2}] | ≤𝔼​[|ϵ​Nτϵ​(T)|​(Γ¯​(T))2],\displaystyle\leq\mathbb{E}[|\epsilon N^{\tau\_{\epsilon}}(T)|(\overline{\Gamma}(T))^{2}], |  |

where 4​|ϵ​Nτϵ​(T)|≤14|\epsilon N^{\tau\_{\epsilon}}(T)|\leq 1. In turn, since limϵ→0+|ϵ​Nτϵ​(T)|=0\lim\_{\epsilon\rightarrow 0+}|\epsilon N^{\tau\_{\epsilon}}(T)|=0 a.s., we have:

|  |  |  |
| --- | --- | --- |
|  | limϵ→0+ϵ​𝔼​[(Qϵ​(T)−F​(T))​(Γτϵ​(T))2]=0.\lim\_{\epsilon\rightarrow 0+}\epsilon\mathbb{E}[(Q^{\epsilon}(T)-F(T))(\Gamma^{\tau\_{\epsilon}}(T))^{2}]=0. |  |

For the second part,

|  |  |  |
| --- | --- | --- |
|  | limϵ→0+ϵ​𝔼​[|Qϵ​(T)−F​(T)|3​|Γτϵ​(T)|]=0,\lim\_{\epsilon\rightarrow 0+}\epsilon\mathbb{E}[|Q^{\epsilon}(T)-F(T)|^{3}|\Gamma^{\tau\_{\epsilon}}(T)|]=0, |  |

follows from Holder’s inequality and limϵ→0+ϵ4​𝔼​[(Γτϵ​(T))4]=0\lim\_{\epsilon\rightarrow 0+}\epsilon^{4}\mathbb{E}[(\Gamma^{\tau\_{\epsilon}}(T))^{4}]=0, similarly to the sixth and seventh order terms.

Fourth order terms

We have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limϵ→0+𝔼​[(Γτϵ​(T))2]\displaystyle\lim\_{\epsilon\rightarrow 0+}\mathbb{E}[(\Gamma^{\tau\_{\epsilon}}(T))^{2}] | =𝔼​[(Γ​(T))2],\displaystyle=\mathbb{E}[(\Gamma(T))^{2}], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | limϵ→0+𝔼​[(Qϵ​(T)−F​(T))2​Γτϵ​(T)]\displaystyle\lim\_{\epsilon\rightarrow 0+}\mathbb{E}[(Q^{\epsilon}(T)-F(T))^{2}\Gamma^{\tau\_{\epsilon}}(T)] | =𝔼​[(N​(T))2​Γ​(T)],\displaystyle=\mathbb{E}[(N(T))^{2}\Gamma(T)], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | limϵ→0+𝔼​[(Qϵ​(T)−F​(T))4​ξϵL]\displaystyle\lim\_{\epsilon\rightarrow 0+}\mathbb{E}[(Q^{\epsilon}(T)-F(T))^{4}\xi\_{\epsilon}^{L}] | =𝔼​[(N​(T))4],\displaystyle=\mathbb{E}[(N(T))^{4}], |  |

which all hold by dominated convergence, ([A3II](https://arxiv.org/html/2601.14139v2#S2.Ex3 "In 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")), ([A4](https://arxiv.org/html/2601.14139v2#S2.Ex6 "In 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")), 0<ξϵL≤240<\xi\_{\epsilon}^{L}\leq 2^{4} and limϵ→0+ξϵL=1\lim\_{\epsilon\rightarrow 0+}\xi\_{\epsilon}^{L}=1 a.s.

Third order terms

Initially note that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Γτϵ​(T)​(Qϵ​(T)−F​(T))]\displaystyle\mathbb{E}[\Gamma^{\tau\_{\epsilon}}(T)(Q^{\epsilon}(T)-F(T))] | =𝔼​[𝔼​[Γτϵ​(T)​(Qϵ​(T)−F​(T))|ℱ​(T∧τϵ)]]=0.\displaystyle=\mathbb{E}\left[\mathbb{E}\left[\Gamma^{\tau\_{\epsilon}}(T)(Q^{\epsilon}(T)-F(T))\Big|\mathscr{F}(T\land\tau\_{\epsilon})\right]\right]=0. |  |

For the second part we have by Holder’s inequality:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1ϵ​𝔼​[|(Qϵ​(T)−F​(T))3+(N​(T))3|]\displaystyle\frac{1}{\epsilon}\mathbb{E}[|(Q^{\epsilon}(T)-F(T))^{3}+(N(T))^{3}|] | =1ϵ​𝔼​[|(Qϵ​(T)−F​(T))3+(N​(T))3|​𝟏τϵ≤T]\displaystyle=\frac{1}{\epsilon}\mathbb{E}[|(Q^{\epsilon}(T)-F(T))^{3}+(N(T))^{3}|\mathbf{1}\_{\tau\_{\epsilon}\leq T}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤214(𝔼[(|M(T)−F(T)|\displaystyle\leq 2^{\frac{1}{4}}\bigg(\mathbb{E}\bigg[\bigg(\bigg|M(T)-F(T)\bigg| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +supt∈[0,T]|Δ(t)−M(t)|)4+(N(T))4])34\displaystyle+\sup\_{t\in[0,T]}\bigg|\Delta(t)-M(t)\bigg|\bigg)^{4}+(N(T))^{4}\bigg]\bigg)^{\frac{3}{4}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⋅(1ϵ4​ℙ​(τϵ≤T))14,\displaystyle\cdot\left(\frac{1}{\epsilon^{4}}\mathbb{P}(\tau\_{\epsilon}\leq T)\right)^{\frac{1}{4}}, |  |

where the expectation on the last inequality is finite by ([A3II](https://arxiv.org/html/2601.14139v2#S2.Ex3 "In 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")), ([A4](https://arxiv.org/html/2601.14139v2#S2.Ex6 "In 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")) and limϵ→0+(ϵ4)−1​ℙ​(τϵ≤T)=0\lim\_{\epsilon\rightarrow 0+}(\epsilon^{4})^{-1}\mathbb{P}(\tau\_{\epsilon}\leq T)=0 by ([2.2](https://arxiv.org/html/2601.14139v2#S2.E2 "In Proof. ‣ 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")). Hence the second part also tends to zero.

Second order term

We have:

|  |  |  |
| --- | --- | --- |
|  | limϵ→0+1ϵ2​𝔼​[|(Qϵ​(T)−F​(T))2−(N​(T))2|]=0,\lim\_{\epsilon\rightarrow 0+}\frac{1}{\epsilon^{2}}\mathbb{E}[|(Q^{\epsilon}(T)-F(T))^{2}-(N(T))^{2}|]=0, |  |

following the same process as for the third order term.

Lastly, combining all the above we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (2.4) |  |  | lim¯ϵ→0+1ϵ4(u(ϵ)+ϵ𝔼[F(T)]+ϵ22𝔼[(N(T))2]+ϵ33𝔼[(N(T))3]+ϵ44𝔼[(N(T))4]\displaystyle\operatorname\*{\overline{lim}}\_{\epsilon\rightarrow 0+}\frac{1}{\epsilon^{4}}\Big(u(\epsilon)+\epsilon\mathbb{E}[F(T)]+\frac{\epsilon^{2}}{2}\mathbb{E}[(N(T))^{2}]+\frac{\epsilon^{3}}{3}\mathbb{E}[(N(T))^{3}]+\frac{\epsilon^{4}}{4}\mathbb{E}[(N(T))^{4}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +ϵ4𝔼[(Γ(T))2/2−(N(T))2Γ(T)])≥0.\displaystyle+\epsilon^{4}\mathbb{E}[(\Gamma(T))^{2}/2-(N(T))^{2}\Gamma(T)]\Big)\geq 0. |  |

The upper bound

Note that by Legendre-Fenchel duality we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ln⁡(1+Xϵ​(T)−ϵ​F​(T))\displaystyle\ln(1+X^{\epsilon}(T)-\epsilon F(T)) | ≤−1−ln⁡(1+ϵ​Nτϵ​(T)+ϵ2​Pτϵ​(T))\displaystyle\leq-1-\ln(1+\epsilon N^{\tau\_{\epsilon}}(T)+\epsilon^{2}P^{\tau\_{\epsilon}}(T)) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1+ϵ​Nτϵ​(T)+ϵ2​Pτϵ​(T))​(1+Xϵ​(T)−ϵ​F​(T)).\displaystyle+(1+\epsilon N^{\tau\_{\epsilon}}(T)+\epsilon^{2}P^{\tau\_{\epsilon}}(T))(1+X^{\epsilon}(T)-\epsilon F(T)). |  |

Now, denoting the probability measure induced by (1+ϵ​Nτϵ​(T)+ϵ2​Pτϵ​(T))/𝔼​[1+ϵ​Nτϵ​(T)+ϵ2​Pτϵ​(T)](1+\epsilon N^{\tau\_{\epsilon}}(T)+\epsilon^{2}P^{\tau\_{\epsilon}}(T))/\mathbb{E}[1+\epsilon N^{\tau\_{\epsilon}}(T)+\epsilon^{2}P^{\tau\_{\epsilon}}(T)] as ℚϵ\mathbb{Q}^{\epsilon} we claim that 1+Xϵ1+X^{\epsilon} is a supermartingale under ℚϵ\mathbb{Q}^{\epsilon} and therefore:

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℚϵ​[1+Xϵ​(T)]≤1.\mathbb{E}^{\mathbb{Q}^{\epsilon}}[1+X^{\epsilon}(T)]\leq 1. |  |

Indeed, we have 1+Xϵ​(T)−ϵ​F​(T)>01+X^{\epsilon}(T)-\epsilon F(T)>0 and in particular from ([A3II](https://arxiv.org/html/2601.14139v2#S2.Ex3 "In 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")) we get ϵ​|F​(T)|≤ϵ​(x+M​(T))\epsilon|F(T)|\leq\epsilon(x+M(T)). It follows that 1+Xϵ+ϵ​(x+M)1+X^{\epsilon}+\epsilon(x+M) is a positive stochastic integral w.r.t. SS. This, along with the fact that NN, PP are strongly orthogonal to SS yields that 1+Xϵ+ϵ​(x+M)1+X^{\epsilon}+\epsilon(x+M) is a supermartingale under ℚϵ\mathbb{Q}^{\epsilon}. The claim now follows from the fact that ϵ​(x+M)\epsilon(x+M) is a martingale under ℚϵ\mathbb{Q}^{\epsilon}. Hence we get:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[(1+ϵ​Nτϵ​(T)+ϵ2​Pτϵ​(T))​(1+Xϵ​(T))]\displaystyle\mathbb{E}[(1+\epsilon N^{\tau\_{\epsilon}}(T)+\epsilon^{2}P^{\tau\_{\epsilon}}(T))(1+X^{\epsilon}(T))] | =𝔼​[1+ϵ​Nτϵ​(T)+ϵ2​Pτϵ​(T)]​𝔼ℚϵ​[1+Xϵ​(T)]\displaystyle=\mathbb{E}[1+\epsilon N^{\tau\_{\epsilon}}(T)+\epsilon^{2}P^{\tau\_{\epsilon}}(T)]\mathbb{E}^{\mathbb{Q}^{\epsilon}}[1+X^{\epsilon}(T)] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼​[1+ϵ​Nτϵ​(T)+ϵ2​Pτϵ​(T)].\displaystyle\leq\mathbb{E}[1+\epsilon N^{\tau\_{\epsilon}}(T)+\epsilon^{2}P^{\tau\_{\epsilon}}(T)]. |  |

Furthermore we have:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Nτϵ​(T)​F​(T)]=𝔼​[Nτϵ​(T)​N​(T)]=𝔼​[(Nτϵ​(T))2],\displaystyle\mathbb{E}[N^{\tau\_{\epsilon}}(T)F(T)]=\mathbb{E}[N^{\tau\_{\epsilon}}(T)N(T)]=\mathbb{E}[(N^{\tau\_{\epsilon}}(T))^{2}], |  |
|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Pτϵ​(T)​F​(T)]=𝔼​[Pτϵ​(T)​N​(T)]=𝔼​[Pτϵ​(T)​Nτϵ​(T)],\displaystyle\mathbb{E}[P^{\tau\_{\epsilon}}(T)F(T)]=\mathbb{E}[P^{\tau\_{\epsilon}}(T)N(T)]=\mathbb{E}[P^{\tau\_{\epsilon}}(T)N^{\tau\_{\epsilon}}(T)], |  |

given the definitions and properties of NN, PP. It follows that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(ϵ)\displaystyle u(\epsilon) | ≤−ϵ​𝔼​[F​(T)]−ϵ2​𝔼​[(Nτϵ​(T))2]−ϵ3​𝔼​[Pτϵ​(T)​Nτϵ​(T)]\displaystyle\leq-\epsilon\mathbb{E}[F(T)]-\epsilon^{2}\mathbb{E}[(N^{\tau\_{\epsilon}}(T))^{2}]-\epsilon^{3}\mathbb{E}[P^{\tau\_{\epsilon}}(T)N^{\tau\_{\epsilon}}(T)] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝔼​[−ln⁡(1+ϵ​Nτϵ​(T)+ϵ2​Pτϵ​(T))+ϵ​Nτϵ​(T)+ϵ2​Pτϵ​(T)].\displaystyle+\mathbb{E}[-\ln(1+\epsilon N^{\tau\_{\epsilon}}(T)+\epsilon^{2}P^{\tau\_{\epsilon}}(T))+\epsilon N^{\tau\_{\epsilon}}(T)+\epsilon^{2}P^{\tau\_{\epsilon}}(T)]. |  |

In turn, Taylor expansion yields:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[−ln⁡(1+ϵ​Nτϵ​(T)+ϵ2​Pτϵ​(T))+ϵ​Nτϵ​(T)+ϵ2​Pτϵ​(T)]\displaystyle\mathbb{E}[-\ln(1+\epsilon N^{\tau\_{\epsilon}}(T)+\epsilon^{2}P^{\tau\_{\epsilon}}(T))+\epsilon N^{\tau\_{\epsilon}}(T)+\epsilon^{2}P^{\tau\_{\epsilon}}(T)] | =12​ϵ2​𝔼​[(Nτϵ​(T)+ϵ​Pτϵ​(T))2]\displaystyle=\frac{1}{2}\epsilon^{2}\mathbb{E}[(N^{\tau\_{\epsilon}}(T)+\epsilon P^{\tau\_{\epsilon}}(T))^{2}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −13​ϵ3​𝔼​[(Nτϵ​(T)+ϵ​Pτϵ​(T))3]\displaystyle-\frac{1}{3}\epsilon^{3}\mathbb{E}[(N^{\tau\_{\epsilon}}(T)+\epsilon P^{\tau\_{\epsilon}}(T))^{3}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +14​ϵ4​𝔼​[(Nτϵ​(T)+ϵ​Pτϵ​(T))4​ξϵU],\displaystyle+\frac{1}{4}\epsilon^{4}\mathbb{E}[(N^{\tau\_{\epsilon}}(T)+\epsilon P^{\tau\_{\epsilon}}(T))^{4}\xi\_{\epsilon}^{U}], |  |

where the random variables ξϵU\xi\_{\epsilon}^{U} satisfy:

|  |  |  |
| --- | --- | --- |
|  | 0<ξϵU≤24,∀ϵ∈(0,ϵL);limϵ→0+ξϵU=1 a.s.0<\xi\_{\epsilon}^{U}\leq 2^{4},\ \forall\epsilon\in(0,\epsilon^{L});\qquad\text{$\lim\_{\epsilon\rightarrow 0+}\xi\_{\epsilon}^{U}=1$ a.s.} |  |

Note that we can once more disregard ξϵU\xi\_{\epsilon}^{U} from the estimates, similarly to ξϵL\xi\_{\epsilon}^{L}, since it is bounded above by 242^{4}. Collecting terms of same order, we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[−ln⁡(1+ϵ​Nτϵ​(T)+ϵ2​Pτϵ​(T))+ϵ​Nτϵ​(T)+ϵ2​Pτϵ​(T)]\displaystyle\mathbb{E}[-\ln(1+\epsilon N^{\tau\_{\epsilon}}(T)+\epsilon^{2}P^{\tau\_{\epsilon}}(T))+\epsilon N^{\tau\_{\epsilon}}(T)+\epsilon^{2}P^{\tau\_{\epsilon}}(T)] | =ϵ2​𝔼​[(Nτϵ​(T))22]\displaystyle=\epsilon^{2}\mathbb{E}\left[\frac{(N^{\tau\_{\epsilon}}(T))^{2}}{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +ϵ3​𝔼​[Nτϵ​(T)​Pτϵ​(T)−(Nτϵ​(T))33]\displaystyle+\epsilon^{3}\mathbb{E}\left[N^{\tau\_{\epsilon}}(T)P^{\tau\_{\epsilon}}(T)-\frac{(N^{\tau\_{\epsilon}}(T))^{3}}{3}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +ϵ4𝔼[(Pτϵ​(T))22−(Nτϵ(T))2Pτϵ(T)\displaystyle+\epsilon^{4}\mathbb{E}\bigg[\frac{(P^{\tau\_{\epsilon}}(T))^{2}}{2}-(N^{\tau\_{\epsilon}}(T))^{2}P^{\tau\_{\epsilon}}(T) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(Nτϵ​(T))44ξϵU]\displaystyle+\frac{(N^{\tau\_{\epsilon}}(T))^{4}}{4}\xi\_{\epsilon}^{U}\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +ϵ5𝔼[−Nτϵ(T)(Pτϵ(T))2\displaystyle+\epsilon^{5}\mathbb{E}[-N^{\tau\_{\epsilon}}(T)(P^{\tau\_{\epsilon}}(T))^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(Nτϵ(T))3Pτϵ(T)ξϵU]\displaystyle+(N^{\tau\_{\epsilon}}(T))^{3}P^{\tau\_{\epsilon}}(T)\xi\_{\epsilon}^{U}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ϵ6​𝔼​[−(Pτϵ​(T))33+32​(Pτϵ​(T))2​(Nτϵ​(T))2​ξϵU]\displaystyle\epsilon^{6}\mathbb{E}\left[-\frac{(P^{\tau\_{\epsilon}}(T))^{3}}{3}+\frac{3}{2}(P^{\tau\_{\epsilon}}(T))^{2}(N^{\tau\_{\epsilon}}(T))^{2}\xi\_{\epsilon}^{U}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +ϵ7​𝔼​[Nτϵ​(T)​(Pτϵ​(T))3​ξϵU]\displaystyle+\epsilon^{7}\mathbb{E}[N^{\tau\_{\epsilon}}(T)(P^{\tau\_{\epsilon}}(T))^{3}\xi\_{\epsilon}^{U}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +ϵ8​𝔼​[(Pτϵ​(T))44​ξϵU]\displaystyle+\epsilon^{8}\mathbb{E}\left[\frac{(P^{\tau\_{\epsilon}}(T))^{4}}{4}\xi\_{\epsilon}^{U}\right] |  |

We examine the above terms (w.r.t. to ϵ\epsilon) one by one, beginning with the highest order.

Eighth order term

We claim that:

|  |  |  |
| --- | --- | --- |
|  | lim→0+ϵ4​𝔼​[(Pτϵ​(T))4]=0.\lim\_{\rightarrow 0+}\epsilon^{4}\mathbb{E}[(P^{\tau\_{\epsilon}}(T))^{4}]=0. |  |

To see this note that since 4​ϵ2​|Pτϵ​(T)|≤14\epsilon^{2}|P^{\tau\_{\epsilon}}(T)|\leq 1:

|  |  |  |
| --- | --- | --- |
|  | ϵ4​(Pτϵ​(T))4≤1(4​ϵ)4​𝟏τϵ≤T+ϵ4​(P¯​(T))4​𝟏P¯​(T)≤(4​ϵ2)−1.\epsilon^{4}(P^{\tau\_{\epsilon}}(T))^{4}\leq\frac{1}{(4\epsilon)^{4}}\mathbf{1}\_{\tau\_{\epsilon}\leq T}+\epsilon^{4}(\overline{P}(T))^{4}\mathbf{1}\_{\overline{P}(T)\leq(4\epsilon^{2})^{-1}}. |  |

Since limϵ→0+ϵ−4​ℙ​(τϵ<∞)=0\lim\_{\epsilon\rightarrow 0+}\epsilon^{-4}\mathbb{P}(\tau\_{\epsilon}<\infty)=0 by ([2.2](https://arxiv.org/html/2601.14139v2#S2.E2 "In Proof. ‣ 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")), we only have to show:

|  |  |  |
| --- | --- | --- |
|  | limz→∞1z2​𝔼​[(P¯​(T))4​𝟏P¯​(T)≤z]=0,\lim\_{z\rightarrow\infty}\frac{1}{z^{2}}\mathbb{E}[(\overline{P}(T))^{4}\mathbf{1}\_{\overline{P}(T)\leq z}]=0, |  |

which follows from ([2.3](https://arxiv.org/html/2601.14139v2#S2.E3 "In Proof. ‣ 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")), similarly to the way we handled the eighth order term in the lower bound of the value function.

Seventh order term

We show that:

|  |  |  |
| --- | --- | --- |
|  | limϵ→0+ϵ3​𝔼​[|Nτϵ​(T)|​|Pτϵ​(T)|3]=0.\lim\_{\epsilon\rightarrow 0+}\epsilon^{3}\mathbb{E}[|N^{\tau\_{\epsilon}}(T)||P^{\tau\_{\epsilon}}(T)|^{3}]=0. |  |

This follows from Holder’s inequality as:

|  |  |  |
| --- | --- | --- |
|  | ϵ3𝔼[|Nτϵ(T)||Pτϵ(T)|3]≤(𝔼[(N¯(T))4]14(𝔼[ϵ4(Pτϵ(T))4])34,\epsilon^{3}\mathbb{E}[|N^{\tau\_{\epsilon}}(T)||P^{\tau\_{\epsilon}}(T)|^{3}]\leq(\mathbb{E}[(\overline{N}(T))^{4}]^{\frac{1}{4}}(\mathbb{E}[\epsilon^{4}(P^{\tau\_{\epsilon}}(T))^{4}])^{\frac{3}{4}}, |  |

and using ([A4](https://arxiv.org/html/2601.14139v2#S2.Ex6 "In 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")) as well as limϵ→0+ϵ−4​ℙ​(τϵ<∞)=0\lim\_{\epsilon\rightarrow 0+}\epsilon^{-4}\mathbb{P}(\tau\_{\epsilon}<\infty)=0.

Sixth order terms

For the first part we have:

|  |  |  |
| --- | --- | --- |
|  | limϵ→0+ϵ2​𝔼​[|Pτϵ​(T)|3]=0,\lim\_{\epsilon\rightarrow 0+}\epsilon^{2}\mathbb{E}[|P^{\tau\_{\epsilon}}(T)|^{3}]=0, |  |

which follows similarly to the eighth order term of the upper bound since:

|  |  |  |
| --- | --- | --- |
|  | ϵ2​|Pτϵ​(T)|3≤143​ϵ4​𝟏τϵ≤T+ϵ2​(P¯​(T))3​𝟏P¯​(T)≤(4​ϵ2)−1.\epsilon^{2}|P^{\tau\_{\epsilon}}(T)|^{3}\leq\frac{1}{4^{3}\epsilon^{4}}\mathbf{1}\_{\tau\_{\epsilon\leq T}}+\epsilon^{2}(\overline{P}(T))^{3}\mathbf{1}\_{\overline{P}(T)\leq(4\epsilon^{2})^{-1}}. |  |

We also have that:

|  |  |  |
| --- | --- | --- |
|  | limϵ→0+ϵ2​𝔼​[(Nτϵ​(T))2​(Pτϵ​(T))2]=0.\lim\_{\epsilon\rightarrow 0+}\epsilon^{2}\mathbb{E}[(N^{\tau\_{\epsilon}}(T))^{2}(P^{\tau\_{\epsilon}}(T))^{2}]=0. |  |

Indeed, this follows from dominated convergence, as:

|  |  |  |
| --- | --- | --- |
|  | ϵ2𝔼[(Nτϵ(T))2(Pτϵ(T))2]≤𝔼[(ϵNτϵ(T))2(P¯(T))2,\epsilon^{2}\mathbb{E}[(N^{\tau\_{\epsilon}}(T))^{2}(P^{\tau\_{\epsilon}}(T))^{2}]\leq\mathbb{E}[(\epsilon N^{\tau\_{\epsilon}}(T))^{2}(\overline{P}(T))^{2}, |  |

and 4​|ϵ​Nτϵ​(T)|≤14|\epsilon N^{\tau\_{\epsilon}}(T)|\leq 1, N∈ℋ4N\in\mathscr{H}\_{4} (implying P∈ℋ2P\in\mathscr{H}\_{2}) as well as limϵ→0+|ϵ​Nτϵ​(T)|=0\lim\_{\epsilon\rightarrow 0+}|\epsilon N^{\tau\_{\epsilon}}(T)|=0.

Fifth order terms

For the first part we have that:

|  |  |  |
| --- | --- | --- |
|  | limϵ→0+ϵ​𝔼​[|Nτϵ​(T)|​(Pτϵ​(T))2]=0,\lim\_{\epsilon\rightarrow 0+}\epsilon\mathbb{E}[|N^{\tau\_{\epsilon}}(T)|(P^{\tau\_{\epsilon}}(T))^{2}]=0, |  |

follows similarly to the sixth order terms of the upper bound, while:

|  |  |  |
| --- | --- | --- |
|  | limϵ→0+ϵ​𝔼​[|Nτϵ​(T)|3​|Pτϵ​(T)|]=0,\lim\_{\epsilon\rightarrow 0+}\epsilon\mathbb{E}[|N^{\tau\_{\epsilon}}(T)|^{3}|P^{\tau\_{\epsilon}}(T)|]=0, |  |

follows from Holder’s inequality since:

|  |  |  |
| --- | --- | --- |
|  | ϵ​𝔼​[|Nτϵ​(T)|3​|Pτϵ​(T)|]≤𝔼​[(N¯​(T))4]34​(ϵ4​𝔼​[(Pτϵ​(T))4])14,\epsilon\mathbb{E}[|N^{\tau\_{\epsilon}}(T)|^{3}|P^{\tau\_{\epsilon}}(T)|]\leq\mathbb{E}[(\overline{N}(T))^{4}]^{\frac{3}{4}}\left(\epsilon^{4}\mathbb{E}[(P^{\tau\_{\epsilon}}(T))^{4}]\right)^{\frac{1}{4}}, |  |

and using the fact that lim→0+ϵ4​𝔼​[(Pτϵ​(T))4]=0\lim\_{\rightarrow 0+}\epsilon^{4}\mathbb{E}[(P^{\tau\_{\epsilon}}(T))^{4}]=0.

Fourth order terms

We have that:

|  |  |  |
| --- | --- | --- |
|  | limϵ→0+𝔼​[(Pτϵ​(T))2]=𝔼​[(P​(T))2],\displaystyle\lim\_{\epsilon\rightarrow 0+}\mathbb{E}[(P^{\tau\_{\epsilon}}(T))^{2}]=\mathbb{E}[(P(T))^{2}], |  |
|  |  |  |
| --- | --- | --- |
|  | limϵ→0+𝔼​[ξϵU​(Nτϵ​(T))4]=𝔼​[(N​(T))4],\displaystyle\lim\_{\epsilon\rightarrow 0+}\mathbb{E}[\xi\_{\epsilon}^{U}(N^{\tau\_{\epsilon}}(T))^{4}]=\mathbb{E}[(N(T))^{4}], |  |
|  |  |  |
| --- | --- | --- |
|  | limϵ→0+𝔼​[(Nτϵ​(T))2​Pτϵ​(T)]=𝔼​[(N​(T))2​P​(T)],\displaystyle\lim\_{\epsilon\rightarrow 0+}\mathbb{E}[(N^{\tau\_{\epsilon}}(T))^{2}P^{\tau\_{\epsilon}}(T)]=\mathbb{E}[(N(T))^{2}P(T)], |  |

which all hold by dominated convergence, ([A3II](https://arxiv.org/html/2601.14139v2#S2.Ex3 "In 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")), ([A4](https://arxiv.org/html/2601.14139v2#S2.Ex6 "In 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")), 0<ξϵU≤240<\xi\_{\epsilon}^{U}\leq 2^{4} and limϵ→0+ξϵU=1\lim\_{\epsilon\rightarrow 0+}\xi\_{\epsilon}^{U}=1 a.s.

Third order term

Holder’s inequality gives:

|  |  |  |
| --- | --- | --- |
|  | 1ϵ​𝔼​[|(Nτϵ​(T))3−(N​(T))3|]≤2​(𝔼​[(N¯​(T))4])34​(1ϵ4​ℙ​(τϵ≤T))14,\frac{1}{\epsilon}\mathbb{E}[|(N^{\tau\_{\epsilon}}(T))^{3}-(N(T))^{3}|]\leq 2(\mathbb{E}[(\overline{N}(T))^{4}])^{\frac{3}{4}}\left(\frac{1}{\epsilon^{4}}\mathbb{P}(\tau\_{\epsilon}\leq T)\right)^{\frac{1}{4}}, |  |

which goes to zero by ([2.2](https://arxiv.org/html/2601.14139v2#S2.E2 "In Proof. ‣ 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")).

Second order term

We have:

|  |  |  |
| --- | --- | --- |
|  | 1ϵ2​𝔼​[|(Nτϵ​(T))2−(N​(T))2|]≤2​(𝔼​[(N¯​(T))4])12​(1ϵ4​ℙ​(τϵ≤T))12,\frac{1}{\epsilon^{2}}\mathbb{E}[|(N^{\tau\_{\epsilon}}(T))^{2}-(N(T))^{2}|]\leq 2(\mathbb{E}[(\overline{N}(T))^{4}])^{\frac{1}{2}}\left(\frac{1}{\epsilon^{4}}\mathbb{P}(\tau\_{\epsilon}\leq T)\right)^{\frac{1}{2}}, |  |

which goes to zero, similarly to the third order case for the upper bound.

Combining all the above and after some algebra we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (2.5) |  |  | lim¯ϵ→0+1ϵ4(u(ϵ)+ϵ𝔼[F(T)]+ϵ22𝔼[(N(T))2]+ϵ33𝔼[(N(T))3]+ϵ44𝔼[(N(T))4]\displaystyle\operatorname\*{\overline{lim}}\_{\epsilon\rightarrow 0+}\frac{1}{\epsilon^{4}}\Big(u(\epsilon)+\epsilon\mathbb{E}[F(T)]+\frac{\epsilon^{2}}{2}\mathbb{E}[(N(T))^{2}]+\frac{\epsilon^{3}}{3}\mathbb{E}[(N(T))^{3}]+\frac{\epsilon^{4}}{4}\mathbb{E}[(N(T))^{4}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +ϵ4𝔼[(Γ(T))2/2−(N(T))2Γ(T)])≤0.\displaystyle+\epsilon^{4}\mathbb{E}[(\Gamma(T))^{2}/2-(N(T))^{2}\Gamma(T)]\Big)\leq 0. |  |

Lastly, noting that ([2.4](https://arxiv.org/html/2601.14139v2#S2.E4 "In Proof. ‣ 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")) and ([2.5](https://arxiv.org/html/2601.14139v2#S2.E5 "In Proof. ‣ 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")) also hold for limit inferior as ϵ→0+\epsilon\rightarrow 0+ concludes the proof.
∎

## 3. Second order expansion of optimal wealth w.r.t. ϵ\epsilon

###### Theorem 3.1.

Assume the same conditions as in Theorem [2.1](https://arxiv.org/html/2601.14139v2#S2.Thmtheorem1 "Theorem 2.1. ‣ 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream"); then:

|  |  |  |  |
| --- | --- | --- | --- |
| (3.1) |  | Xϵ​(T)−ϵ​Δ​(T)−ϵ2​Γ​(T)=oℙ​(ϵ2),X^{\epsilon}(T)-\epsilon\Delta(T)-\epsilon^{2}\Gamma(T)=o\_{\mathbb{P}}(\epsilon^{2})\ , |  |

as ϵ→0+\epsilon\rightarrow 0+.

###### Proof.

Take any sequence ϵn∈(0,ϵL)\epsilon\_{n}\in(0,\epsilon^{L}) s.t. limn→∞ϵn=0\lim\_{n\rightarrow\infty}\epsilon\_{n}=0 333This should come without loss of generality for our purposes since any positive sequence ϵn\epsilon\_{n}, that tends to zero, eventually lies in (0,ϵL)(0,\epsilon^{L}).. In turn, recalling the process we were considering for the fourth order lower bound of the value function, i.e. QϵnQ^{\epsilon\_{n}} and Taylor expanding U​(1+ϵn​Qϵn​(T)+ϵn2​Γτϵn​(T)−ϵn​F​(T))U(1+\epsilon\_{n}Q^{\epsilon\_{n}}(T)+\epsilon\_{n}^{2}\Gamma^{\tau\_{\epsilon\_{n}}}(T)-\epsilon\_{n}F(T)) around Xϵn​(T)−ϵn​F​(T)X^{\epsilon\_{n}}(T)-\epsilon\_{n}F(T) we get:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.2) |  |  | ln⁡(1+ϵn​Qϵn​(T)+ϵn2​Γτϵn​(T)−ϵn​F​(T))−ln⁡(1+Xϵn​(T)−ϵn​F​(T))=\displaystyle\ln(1+\epsilon\_{n}Q^{\epsilon\_{n}}(T)+\epsilon\_{n}^{2}\Gamma^{\tau\_{\epsilon\_{n}}}(T)-\epsilon\_{n}F(T))-\ln(1+X^{\epsilon\_{n}}(T)-\epsilon\_{n}F(T))= |  |
|  |  | 11+Xϵn​(T)−ϵn​F​(T)​((1+ϵn​Qϵn​(T)+ϵn2​Γτϵn​(T)−ϵn​F​(T))−(1+XT,ϵn​(T)−ϵn​F​(T)))\displaystyle\frac{1}{1+X^{\epsilon\_{n}}(T)-\epsilon\_{n}F(T)}\left(\left(1+\epsilon\_{n}Q^{\epsilon\_{n}}(T)+\epsilon\_{n}^{2}\Gamma^{\tau\_{\epsilon\_{n}}}(T)-\epsilon\_{n}F(T)\right)-\left(1+X^{T,\epsilon\_{n}}(T)-\epsilon\_{n}F(T)\right)\right) |  |
|  |  | −12​(1+ξn)2​(Xϵn​(T)−ϵn​Qϵn​(T)−ϵn2​Γτϵn​(T))2,\displaystyle-\frac{1}{2(1+\xi\_{n})^{2}}\left(X^{\epsilon\_{n}}(T)-\epsilon\_{n}Q^{\epsilon\_{n}}(T)-\epsilon\_{n}^{2}\Gamma^{\tau\_{\epsilon\_{n}}}(T)\right)^{2}, |  |

where ξn\xi\_{n} is a r.v. between Xϵn​(T)−ϵn​F​(T)X^{\epsilon\_{n}}(T)-\epsilon\_{n}F(T) and ϵn​Qϵn​(T)+ϵn2​Γτϵn​(T)−ϵn​F​(T)\epsilon\_{n}Q^{\epsilon\_{n}}(T)+\epsilon\_{n}^{2}\Gamma^{\tau\_{\epsilon\_{n}}}(T)-\epsilon\_{n}F(T) s.t. limn→∞ξn=0\lim\_{n\rightarrow\infty}\xi\_{n}=0 in probability. This holds by the fact that limn→∞Xϵn​(T)=0\lim\_{n\rightarrow\infty}X^{\epsilon\_{n}}(T)=0 in probability (see [[26](https://arxiv.org/html/2601.14139v2#bib.bib3 "The asymptotic elasticity of utility functions and optimal investment in incomplete markets"), Lemma 3.6], [[28](https://arxiv.org/html/2601.14139v2#bib.bib18 "Sensitivity analysis of utility-based prices and risk-tolerance wealth processes"), Theorem 1] for similar results that cover the case of log-utility). Passing to any subsequence of ϵn\epsilon\_{n} we can always find a further subsequence, denoted by ϵm\epsilon\_{m}, s.t. limm→∞Xϵm​(T)=0\lim\_{m\rightarrow\infty}X^{\epsilon\_{m}}(T)=0 a.s., which in turn implies that the r.v. supmXϵm​(T)\sup\_{m}X^{\epsilon\_{m}}(T) is well-defined a.s. 444In fact note that if ([3.1](https://arxiv.org/html/2601.14139v2#S3.E1 "In Theorem 3.1. ‣ 3. Second order expansion of optimal wealth w.r.t. ϵ ‣ Log-optimality with small liability stream")) holds for the subsequence ϵm\epsilon\_{m}, then it also holds for the original (arbitrary) sequence ϵn\epsilon\_{n} by the double subsequence trick..

Now note that:

|  |  |  |
| --- | --- | --- |
|  | 0<1+ξm≤(2+supmXϵm(T)+|F(T)|)∨(2+Q¯ϵ(T)+Γ¯(T)+|F(T)|)=:B,0<1+\xi\_{m}\leq\left(2+\sup\_{m}X^{\epsilon\_{m}}(T)+|F(T)|\right)\lor\left(2+\overline{Q}^{\epsilon}(T)+\overline{\Gamma}(T)+|F(T)|\right)=:B, |  |

which implies that −1/2​(1+ξm)2≤−1/2​B2-1/2(1+\xi\_{m})^{2}\leq-1/2B^{2} and in particular we have 1/B≤11/B\leq 1. Hence ([3.2](https://arxiv.org/html/2601.14139v2#S3.E2 "In Proof. ‣ 3. Second order expansion of optimal wealth w.r.t. ϵ ‣ Log-optimality with small liability stream")) becomes:

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ln⁡(1+ϵm​Qϵm​(T)+ϵm2​Γτϵm​(T)−ϵm​F​(T))−ln⁡(1+Xϵm​(T)−ϵm​F​(T))≤\displaystyle\ln(1+\epsilon\_{m}Q^{\epsilon\_{m}}(T)+\epsilon\_{m}^{2}\Gamma^{\tau\_{\epsilon\_{m}}}(T)-\epsilon\_{m}F(T))-\ln(1+X^{\epsilon\_{m}}(T)-\epsilon\_{m}F(T))\leq |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 11+Xϵm​(T)−ϵm​F​(T)​((1+ϵm​Qϵm​(T)+ϵm2​Γτϵm​(T)−ϵm​F​(T))−(1+Xϵm​(T)−ϵm​F​(T)))\displaystyle\frac{1}{1+X^{\epsilon\_{m}}(T)-\epsilon\_{m}F(T)}\left(\left(1+\epsilon\_{m}Q^{\epsilon\_{m}}(T)+\epsilon\_{m}^{2}\Gamma^{\tau\_{\epsilon\_{m}}}(T)-\epsilon\_{m}F(T)\right)-\left(1+X^{\epsilon\_{m}}(T)-\epsilon\_{m}F(T)\right)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −12​B2​(Xϵm​(T)−ϵm​Qϵm​(T)−ϵm2​Γτϵm​(T))2.\displaystyle-\frac{1}{2B^{2}}\left(X^{\epsilon\_{m}}(T)-\epsilon\_{m}Q^{\epsilon\_{m}}(T)-\epsilon\_{m}^{2}\Gamma^{\tau\_{\epsilon\_{m}}}(T)\right)^{2}. |  |

Now we claim that:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[1+ϵm​Qϵm​(T)+ϵm2​Γτϵm​(T)−ϵm​F​(T)1+Xϵm​(T)−ϵm​F​(T)]≤1.\mathbb{E}\left[\frac{1+\epsilon\_{m}Q^{\epsilon\_{m}}(T)+\epsilon\_{m}^{2}\Gamma^{\tau\_{\epsilon\_{m}}}(T)-\epsilon\_{m}F(T)}{1+X^{\epsilon\_{m}}(T)-\epsilon\_{m}F(T)}\right]\leq 1. |  |

This holds since 1+ϵm​Qϵm+ϵm2​Γτϵm∈𝒳​(1,ϵ)1+\epsilon\_{m}Q^{\epsilon\_{m}}+\epsilon\_{m}^{2}\Gamma^{\tau\_{\epsilon\_{m}}}\in\mathscr{X}(1,\epsilon). Hence:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[ln⁡(1+ϵm​Qϵm​(T)+ϵm2​Γτϵm​(T)−ϵm​F​(T)1+Xϵm​(T)−ϵm​F​(T))]≤0.\mathbb{E}\left[\ln\left(\frac{1+\epsilon\_{m}Q^{\epsilon\_{m}}(T)+\epsilon\_{m}^{2}\Gamma^{\tau\_{\epsilon\_{m}}}(T)-\epsilon\_{m}F(T)}{1+X^{\epsilon\_{m}}(T)-\epsilon\_{m}F(T)}\right)\right]\leq 0. |  |

Using Jensen’s inequality, the claim follows. In turn we have:

|  |  |  |  |
| --- | --- | --- | --- |
| (3.3) |  | u​(ϵm)−𝔼​[ln⁡(1+ϵm​Qϵm​(T)+ϵm2​Γτϵm​(T)−ϵm​F​(T))]ϵm4≥𝔼​[(Xϵm​(T)−ϵm​Qϵm​(T)−ϵm2​Γτϵm​(T))2/2​B2]ϵm4,\frac{u(\epsilon\_{m})-\mathbb{E}[\ln(1+\epsilon\_{m}Q^{\epsilon\_{m}}(T)+\epsilon\_{m}^{2}\Gamma^{\tau\_{\epsilon\_{m}}}(T)-\epsilon\_{m}F(T))]}{\epsilon\_{m}^{4}}\geq\frac{\mathbb{E}[(X^{\epsilon\_{m}}(T)-\epsilon\_{m}Q^{\epsilon\_{m}}(T)-\epsilon\_{m}^{2}\Gamma^{\tau\_{\epsilon\_{m}}}(T))^{2}/2B^{2}]}{\epsilon\_{m}^{4}}, |  |

where by the fourth order expansion of the value function we have that the left-hand side of ([3.3](https://arxiv.org/html/2601.14139v2#S3.E3 "In Proof. ‣ 3. Second order expansion of optimal wealth w.r.t. ϵ ‣ Log-optimality with small liability stream")) tends to zero as m→∞m\rightarrow\infty. Furthermore, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[(Xϵm​(T)−ϵm​Δ​(T)−ϵm2​Γ​(T))2/2​B2]ϵm4\displaystyle\frac{\mathbb{E}[(X^{\epsilon\_{m}}(T)-\epsilon\_{m}\Delta(T)-\epsilon\_{m}^{2}\Gamma(T))^{2}/2B^{2}]}{\epsilon\_{m}^{4}} | ≤2​𝔼​[(Xϵm​(T)−ϵm​Qϵm​(T)−ϵm2​Γτϵm​(T))2/2​B2]ϵm4\displaystyle\leq\frac{2\mathbb{E}[(X^{\epsilon\_{m}}(T)-\epsilon\_{m}Q^{\epsilon\_{m}}(T)-\epsilon\_{m}^{2}\Gamma^{\tau\_{\epsilon\_{m}}}(T))^{2}/2B^{2}]}{\epsilon\_{m}^{4}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +2​𝔼​[(ϵm​Qϵm​(T)+ϵm2​Γτϵm​(T)−ϵm​Δ​(T)−ϵm2​Γ​(T))2]ϵm4\displaystyle+\frac{2\mathbb{E}[(\epsilon\_{m}Q^{\epsilon\_{m}}(T)+\epsilon\_{m}^{2}\Gamma^{\tau\_{\epsilon\_{m}}}(T)-\epsilon\_{m}\Delta(T)-\epsilon\_{m}^{2}\Gamma(T))^{2}]}{\epsilon\_{m}^{4}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2​𝔼​[(Xϵm​(T)−ϵm​Qϵm​(T)−ϵm2​Γτϵm​(T))2/2​B2]ϵm4\displaystyle\leq\frac{2\mathbb{E}[(X^{\epsilon\_{m}}(T)-\epsilon\_{m}Q^{\epsilon\_{m}}(T)-\epsilon\_{m}^{2}\Gamma^{\tau\_{\epsilon\_{m}}}(T))^{2}/2B^{2}]}{\epsilon\_{m}^{4}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +4​𝔼​[(Γτϵm​(T)−Γ​(T))4]\displaystyle+4\mathbb{E}[(\Gamma^{\tau\_{\epsilon\_{m}}}(T)-\Gamma(T))^{4}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +C​(ℙ​(τϵm≤T)ϵm4)12,\displaystyle+C\left(\frac{\mathbb{P}(\tau\_{\epsilon\_{m}}\leq T)}{\epsilon\_{m}^{4}}\right)^{\frac{1}{2}}, |  |

for C>0C>0. Now the above tends to zero as m→∞m\rightarrow\infty by ([3.3](https://arxiv.org/html/2601.14139v2#S3.E3 "In Proof. ‣ 3. Second order expansion of optimal wealth w.r.t. ϵ ‣ Log-optimality with small liability stream")), dominated convergence, ([A3II](https://arxiv.org/html/2601.14139v2#S2.Ex3 "In 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")), ([A4](https://arxiv.org/html/2601.14139v2#S2.Ex6 "In 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")) and ([2.2](https://arxiv.org/html/2601.14139v2#S2.E2 "In Proof. ‣ 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")). Lastly, Markov’s inequality applied on the increasing, positive non-negative function x↦x2/2​B2x\mapsto x^{2}/2B^{2} gives the desired result.
∎

## 4. Discussion and an example

Before considering a concrete example, let us comment on the usefulness of the results derived in the previous sections. In particular, besides the obvious increase of accuracy in Xϵ​(T)X^{\epsilon}(T)’s approximation by also considering Γ​(T)\Gamma(T); there is another arguably more important upside. One that provides some added intuition on the way the investor behaves optimally in an incomplete v.s. complete market setting. In order to underline this we claim that Xϵ​(T)=ϵ​Δ​(T)X^{\epsilon}(T)=\epsilon\Delta(T) in a complete market setting, i.e. the first order approximation discussed in §2-3 is actually optimal. Indeed, in this case we have that Δ​(T)=F​(T)−𝔼​[F​(T)]\Delta(T)=F(T)-\mathbb{E}[F(T)], since N=𝔼​[F​(T)]N=\mathbb{E}[F(T)]. This implies that 1+ϵ​Δ​(T)−ϵ​F​(T)=1−ϵ​𝔼​[F​(T)]1+\epsilon\Delta(T)-\epsilon F(T)=1-\epsilon\mathbb{E}[F(T)]. But then, we get for sufficiently small ϵ\epsilon s.t. 1−ϵ​𝔼​[F​(T)]>01-\epsilon\mathbb{E}[F(T)]>0 and ∀X∈𝒳​(1,ϵ)\forall X\in\mathscr{X}(1,\epsilon):

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[X​(T)−1−Xϵ​(T)1+Xϵ​(T)−ϵ​F​(T)]=𝔼​[X​(T)−1−ϵ​Δ​(T)1−ϵ​𝔼​[F​(T)]]=𝔼​[X​(T)]−11−ϵ​𝔼​[F​(T)]≤0,\mathbb{E}\left[\frac{X(T)-1-X^{\epsilon}(T)}{1+X^{\epsilon}(T)-\epsilon F(T)}\right]=\mathbb{E}\left[\frac{X(T)-1-\epsilon\Delta(T)}{1-\epsilon\mathbb{E}[F(T)]}\right]=\frac{\mathbb{E}[X(T)]-1}{1-\epsilon\mathbb{E}[F(T)]}\leq 0, |  |

which shows that Xϵ​(T)=ϵ​Δ​(T)X^{\epsilon}(T)=\epsilon\Delta(T) in view of the first order conditions. Hence, the term ϵ2​Γ​(T)\epsilon^{2}\Gamma(T) in the approximation of Xϵ​(T)X^{\epsilon}(T) allows us to get a sense of how market incompleteness directly affects optimal behavior in a context where a non-traded endowment is present.

Secondly, the fact that the model accommodates infinite horizon markets is a non-trivial addition. In order to better grasp the added benefit of such a result note that while we have a characterization of Δ\Delta, Γ\Gamma; their dependence of the maturity makes explicit results not possible in many cases. On the other hand the “myopic case” of T=∞T=\infty provides a more tractable tool to approximate optimal behavior. Informally, the message being that in the case of distant horizons asset allocation can be further approximated by the projections of 𝔼​[F​(∞)|ℱ​(⋅)]\mathbb{E}[F(\infty)|\mathscr{F}(\cdot)] and 𝔼​[(N​(∞))2|ℱ​(⋅)]\mathbb{E}[(N(\infty))^{2}|\mathscr{F}(\cdot)] on the space of SS-integrals. Concretely, let us consider a space that supports a two dimensional standard Brownian motion (W1,W2)(W^{1},W^{2}), where the risky asset is driven by ∫0⋅σ​(t)​𝑑W1​(t)\int\_{0}^{\cdot}\sigma(t)dW^{1}(t), and factor process ZZ:

|  |  |  |
| --- | --- | --- |
|  | Z=Z​(0)+∫0⋅μ​(Z​(t))​𝑑t+∫0⋅κ​(Z​(t))​𝑑B​(t),Z=Z(0)+\int\_{0}^{\cdot}\mu(Z(t))dt+\int\_{0}^{\cdot}\kappa(Z(t))dB(t), |  |

where β:=κ2\beta:=\kappa^{2} and B:=ρ​W1+1−ρ2​W2,ρ∈(−1,1)B:=\rho W^{1}+\sqrt{1-\rho^{2}}W^{2},\ \rho\in(-1,1). With a slight abuse of notation, we assume that all R0R\_{0}, aa, σ\sigma, λ\lambda are functions of the factor (c:=σ2c:=\sigma^{2}). Explicit calculations regarding Δ∞\Delta^{\infty} require us to have a sense of the following form:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0∞S0π⋆​(s)​λ​(s)/S0​(s)​𝑑s|ℱ​(t)]=∫0tS0π⋆​(s)​λ​(s)/S0​(s)​𝑑s+S0π⋆​(t)​ψ​(Z​(t))/S0​(t),\mathbb{E}\left[\int\_{0}^{\infty}S\_{0}^{\pi^{\star}}(s)\lambda(s)/S\_{0}(s)ds\bigg|\mathscr{F}(t)\right]=\int\_{0}^{t}S\_{0}^{\pi^{\star}}(s)\lambda(s)/S\_{0}(s)ds+S\_{0}^{\pi^{\star}}(t)\psi(Z(t))/S\_{0}(t), |  |

where ψ\psi satisfies the following second order ODE:

|  |  |  |
| --- | --- | --- |
|  | λ−R0​ψ+(μ−π⋆​σ​κ​ρ)​∂zψ+12​β​∂z​zψ=0.\lambda-R\_{0}\psi+(\mu-\pi^{\star}\sigma\kappa\rho)\partial\_{z}\psi+\frac{1}{2}\beta\partial\_{zz}\psi=0. |  |

On the contrary, similar calculations for finite horizons would require us to solve a PDE, since a time variable would also be present.

###### Example 4.1 (Linear payoff on a factor model and an infinite horizon).

In a market with one riskless and one risky asset as well as T=∞T=\infty, we consider a standard two dimensional Brownian motion (W1,W2)(W^{1},W^{2}) generating the augmented filtration ℱ​(⋅)\mathscr{F}(\cdot), and formulate the following problem for B:=ρ​W1+1−ρ2​W2,ρ∈(−1,1)B:=\rho W^{1}+\sqrt{1-\rho^{2}}W^{2},\ \rho\in(-1,1):

|  |  |  |
| --- | --- | --- |
|  | Λ=∫0⋅e−r​t​Z​(t)​𝑑t,r>0,\displaystyle\Lambda=\int\_{0}^{\cdot}e^{-rt}Z(t)dt,\qquad r>0, |  |
|  |  |  |
| --- | --- | --- |
|  | d​Z​(t)=k​(θ−Z​(t))​d​t+b​d​B​(t),k,b>0;Z​(0),θ∈ℝ,\displaystyle dZ(t)=k(\theta-Z(t))dt+bdB(t),\qquad k,b>0;\ Z(0),\theta\in\mathbb{R}, |  |
|  |  |  |
| --- | --- | --- |
|  | d​R​(t)=a​d​t+σ​d​W1​(t),a∈ℝ;σ>0,\displaystyle dR(t)=adt+\sigma dW^{1}(t),\qquad a\in\mathbb{R};\ \sigma>0, |  |
|  |  |  |
| --- | --- | --- |
|  | d​S~​(t)=S~​(t)​d​R​(t).\displaystyle d\widetilde{S}(t)=\widetilde{S}(t)dR(t). |  |

In turn, in the above model, the portfolio that gives rise to the supermartingale numeraire is constant and in particular we have:

|  |  |  |
| --- | --- | --- |
|  | d​S0​(t)S0​(t)=−π⋆​σ​d​W1​(t)⏞d​R0π⋆​(t),\displaystyle\frac{dS\_{0}(t)}{S\_{0}(t)}=\overbrace{-\pi^{\star}\sigma dW^{1}(t)}^{dR\_{0}^{\pi^{\star}}(t)}, |  |
|  |  |  |
| --- | --- | --- |
|  | F=∫0⋅e−r​t​S0​(t)​Z​(t)​𝑑t.\displaystyle F=\int\_{0}^{\cdot}e^{-rt}S\_{0}(t)Z(t)dt. |  |

Note that even if a non-traded (local) endowment λ\lambda given as a linear contract on the factor ZZ isn’t sub/super replicable, the continuity (and adaptedness) of the factor process give that ZZ is locally bounded. Hence the above are still relevant. In fact define τn:=inf{t:|Z​(t)|≥n}\tau\_{n}:=\inf\{t:|Z(t)|\geq n\} (for big enough nn s.t. it dominates Z​(0)Z(0)). Then Fn:=∫0⋅e−r​t​S0​(t)​Zτn​(t)​𝑑tF\_{n}:=\int\_{0}^{\cdot}e^{-rt}S\_{0}(t)Z^{\tau\_{n}}(t)dt satisfies the sub/super replicability conditions for all nn, since ZτnZ^{\tau\_{n}} is (uniformly) bounded. Denote the martingales closed by F​(∞)F(\infty), Fn​(∞)F\_{n}(\infty) as MM and MnM\_{n} respectively and recall that we have the following Kunita-Watanabe decompositions, as in §2:

|  |  |  |  |
| --- | --- | --- | --- |
|  | M\displaystyle M | =Δ+N,\displaystyle=\Delta+N, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Q\displaystyle Q | :=𝔼​[(N​(∞))2|ℱ​(⋅)]=Γ+P,\displaystyle:=\mathbb{E}[(N(\infty))^{2}|\mathscr{F}(\cdot)]=\Gamma+P, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Mn\displaystyle M\_{n} | =Δn+Nn,\displaystyle=\Delta\_{n}+N\_{n}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Qn\displaystyle Q\_{n} | :=𝔼​[(Nn​(∞))2|ℱ​(⋅)]=Γn+Pn,\displaystyle:=\mathbb{E}[(N\_{n}(\infty))^{2}|\mathscr{F}(\cdot)]=\Gamma\_{n}+P\_{n}, |  |

where Δ​(0)=Γ​(0)=Δn​(0)=Γn​(0)=0\Delta(0)=\Gamma(0)=\Delta\_{n}(0)=\Gamma\_{n}(0)=0. For sufficiently big rr, we get:

|  |  |  |
| --- | --- | --- |
|  | ‖[Mn−M]​(∞)‖ℒ1→0,\|[M\_{n}-M](\infty)\|\_{\mathscr{L}\_{1}}\rightarrow 0, |  |

as n→∞n\rightarrow\infty.

Markov’s inequality gives that the above convergence also holds in probability. Now, using [Mn−M]=[Δn−Δ]+[Nn−N][M\_{n}-M]=[\Delta\_{n}-\Delta]+[N\_{n}-N] implies that [Δn−Δ]​(∞)→0[\Delta\_{n}-\Delta](\infty)\rightarrow 0 in probability as n→∞n\rightarrow\infty. In turn, we get:

|  |  |  |
| --- | --- | --- |
|  | supt≥0|Δn​(t)−Δ​(t)|→0,\sup\_{t\geq 0}|\Delta\_{n}(t)-\Delta(t)|\rightarrow 0, |  |

in probability as n→∞n\rightarrow\infty. For the case of Γn\Gamma\_{n}, Γ\Gamma note that we have for any a>0a>0:

|  |  |  |
| --- | --- | --- |
|  | ℙ​(supt≥0|Qn​(t)−Q​(t)|>a)≤1a​‖(Nn​(∞))2−(N​(∞))2‖ℒ1​(ℙ),\mathbb{P}\left(\sup\_{t\geq 0}|Q\_{n}(t)-Q(t)|>a\right)\leq\frac{1}{a}\|(N\_{n}(\infty))^{2}-(N(\infty))^{2}\|\_{\mathscr{L}\_{1}(\mathbb{P})}, |  |

which holds by Doob’s maximal inequality, the fact that |𝔼[(Nn(∞))2−(N(∞))2|ℱ(⋅)]|≤𝔼[|(Nn(∞))2−(N(∞))2||ℱ(⋅)]|\mathbb{E}[(N\_{n}(\infty))^{2}-(N(\infty))^{2}|\mathscr{F}(\cdot)]|\leq\mathbb{E}[|(N\_{n}(\infty))^{2}-(N(\infty))^{2}||\mathscr{F}(\cdot)] and ∪K>0{ω:sup0≤t≤K|Qn​(t)−Q​(t)|>a}={ω:supt≥0|Qn​(t)−Q​(t)|>a}\cup\_{K>0}\{\omega:\sup\_{0\leq t\leq K}|Q\_{n}(t)-Q(t)|>a\}=\{\omega:\sup\_{t\geq 0}|Q\_{n}(t)-Q(t)|>a\}. In turn, we get:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℙ​(supt≥0|Qn​(t)−Q​(t)|>a)\displaystyle\mathbb{P}\left(\sup\_{t\geq 0}|Q\_{n}(t)-Q(t)|>a\right) | ≤1a​(‖Nn​(∞)−N​(∞)‖ℒ2​(ℙ)2+2​‖N​(∞)​(Nn​(∞)−N​(∞))‖ℒ1​(ℙ))\displaystyle\leq\frac{1}{a}\left(\|N\_{n}(\infty)-N(\infty)\|\_{\mathscr{L}\_{2}(\mathbb{P})}^{2}+2\|N(\infty)(N\_{n}(\infty)-N(\infty))\|\_{\mathscr{L}\_{1}(\mathbb{P})}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤4a​(‖Fn​(∞)−F​(∞)‖ℒ2​(ℙ)2+2​‖F​(∞)‖ℒ2​(ℙ)​‖Fn​(∞)−F​(∞)‖ℒ2​(ℙ))\displaystyle\leq\frac{4}{a}\left(\|F\_{n}(\infty)-F(\infty)\|\_{\mathscr{L}\_{2}(\mathbb{P})}^{2}+2\|F(\infty)\|\_{\mathscr{L}\_{2}(\mathbb{P})}\|F\_{n}(\infty)-F(\infty)\|\_{\mathscr{L}\_{2}(\mathbb{P})}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤4a​(‖Fn​(∞)−F​(∞)‖ℒ2​(ℙ)2+2​‖F​(∞)‖ℒ2​(ℙ)​‖Fn​(∞)−F​(∞)‖ℒ2​(ℙ)),\displaystyle\leq\frac{4}{a}\left(\|F\_{n}(\infty)-F(\infty)\|\_{\mathscr{L}\_{2}(\mathbb{P})}^{2}+2\|F(\infty)\|\_{\mathscr{L}\_{2}(\mathbb{P})}\|F\_{n}(\infty)-F(\infty)\|\_{\mathscr{L}\_{2}(\mathbb{P})}\right), |  |

where we’ve also used that ‖F​(∞)‖ℒ2​(ℙ)\|F(\infty)\|\_{\mathscr{L}\_{2}(\mathbb{P})} is bounded by 𝔼​[(∫0∞e−r​t​S0​(t)​|Z​(t)|​𝑑t)2]1/2<∞\mathbb{E}[(\int\_{0}^{\infty}e^{-rt}S\_{0}(t)|Z(t)|dt)^{2}]^{1/2}<\infty (for sufficiently big rr). The above converges to zero as n→∞n\rightarrow\infty, as for sufficiently big rr we have ‖Fn​(∞)−F​(∞)‖ℒ2​(ℙ)→0\|F\_{n}(\infty)-F(\infty)\|\_{\mathscr{L}\_{2}(\mathbb{P})}\rightarrow 0. In fact for Q~:=Q−Q​(0)\widetilde{Q}:=Q-Q(0), Q~n:=Qn−Qn​(0)\widetilde{Q}\_{n}:=Q\_{n}-Q\_{n}(0) we have by the above that supt≥0|Q~n​(t)−Q~​(t)|→0\sup\_{t\geq 0}|\widetilde{Q}\_{n}(t)-\widetilde{Q}(t)|\rightarrow 0 in probability. This yields [Q~n−Q~]​(∞)→0[\widetilde{Q}\_{n}-\widetilde{Q}](\infty)\rightarrow 0 in probability, implying [Γn−Γ]​(∞)→0[\Gamma\_{n}-\Gamma](\infty)\rightarrow 0 in probability; which lastly gives:

|  |  |  |
| --- | --- | --- |
|  | supt≥0|Γn​(t)−Γ​(t)|→0,\sup\_{t\geq 0}|\Gamma\_{n}(t)-\Gamma(t)|\rightarrow 0, |  |

in probability as n→∞n\rightarrow\infty.

Having established a concrete connection between (Δn,Δ)(\Delta\_{n},\Delta) and (Γn,Γ)(\Gamma\_{n},\Gamma), we move forward with explicit calculations of Δ\Delta, Γ\Gamma. Beginning with the former denote the measure induced by S0S\_{0} as ℚπ⋆\mathbb{Q}^{\pi^{\star}} (which is locally equivalent to ℙ\mathbb{P}) and note that:

|  |  |  |
| --- | --- | --- |
|  | M​(t)=∫0te−r​s​S0​(s)​Z​(s)​𝑑s+e−r​t​S0​(t)​∫0∞e−r​s​𝔼zℚπ⋆​[Z​(s)]​𝑑s.M(t)=\int\_{0}^{t}e^{-rs}S\_{0}(s)Z(s)ds+e^{-rt}S\_{0}(t)\int\_{0}^{\infty}e^{-rs}\mathbb{E}\_{z}^{\mathbb{Q}^{\pi^{\star}}}[Z(s)]ds. |  |

Now, under ℚπ⋆\mathbb{Q}^{\pi^{\star}} we have:

|  |  |  |
| --- | --- | --- |
|  | d​Z​(t)=(η−k​Z​(t))​d​t+b​d​Bℚπ⋆​(t),η:=k​θ−b​σ​π⋆​ρ.dZ(t)=(\eta-kZ(t))dt+bdB^{\mathbb{Q}^{\pi^{\star}}}(t),\qquad\eta:=k\theta-b\sigma\pi^{\star}\rho. |  |

Hence, we get:

|  |  |  |
| --- | --- | --- |
|  | M​(t)=∫0te−r​s​S0​(s)​Z​(s)​𝑑s+e−r​t​S0​(t)​(Z​(t)+η/rr+k).M(t)=\int\_{0}^{t}e^{-rs}S\_{0}(s)Z(s)ds+e^{-rt}S\_{0}(t)\left(\frac{Z(t)+\eta/r}{r+k}\right). |  |

Applying the Kunita-Watanabe decomposition on MM w.r.t. W1W^{1} (which drives both S0S\_{0} and S1S\_{1}), we get:

|  |  |  |
| --- | --- | --- |
|  | Δ=∫0⋅θΔ​(t)​𝑑W1​(t),θΔ​(t):=(b​ρ−π⋆​σ​η/r)r+k​e−r​t​S0​(t)−π⋆​σr+k​e−r​t​S0​(t)​Z​(t).\Delta=\int\_{0}^{\cdot}\theta^{\Delta}(t)dW^{1}(t),\qquad\theta^{\Delta}(t):=\frac{(b\rho-\pi^{\star}\sigma\eta/r)}{r+k}e^{-rt}S\_{0}(t)-\frac{\pi^{\star}\sigma}{r+k}e^{-rt}S\_{0}(t)Z(t). |  |

Continuing with Γ\Gamma, denote the martingale closed by [N]​(∞)[N](\infty) as KK, then:

|  |  |  |  |
| --- | --- | --- | --- |
|  | K​(t)\displaystyle K(t) | =𝔼​[∫0∞b2​(1−ρ2)(r+k)2​e−2​r​s​(S0​(s))2​𝑑s|ℱ​(t)]=∫0tb2​(1−ρ2)(r+k)2​e−2​r​s​(S0​(s))2​𝑑s\displaystyle=\mathbb{E}\left[\int\_{0}^{\infty}\frac{b^{2}(1-\rho^{2})}{(r+k)^{2}}e^{-2rs}(S\_{0}(s))^{2}ds\bigg|\mathscr{F}(t)\right]=\int\_{0}^{t}\frac{b^{2}(1-\rho^{2})}{(r+k)^{2}}e^{-2rs}(S\_{0}(s))^{2}ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝔼​[∫t∞b2​(1−ρ2)(r+k)2​e−(2​r−(π⋆​σ)2)​s​ℰ​(2​R0π⋆)​(s)​𝑑s|ℱ​(t)]\displaystyle+\mathbb{E}\bigg[\int\_{t}^{\infty}\frac{b^{2}(1-\rho^{2})}{(r+k)^{2}}e^{-(2r-(\pi^{\star}\sigma)^{2})s}\mathscr{E}(2R\_{0}^{\pi^{\star}})(s)ds\bigg|\mathscr{F}(t)\bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0tb2​(1−ρ2)(r+k)2​e−2​r​s​(S0​(s))2​𝑑s+b2​(1−ρ2)(r+k)2​(2​r−(π⋆​σ)2)​e−(2​r−(π⋆​σ)2)​t​ℰ​(2​R0π⋆)​(t),\displaystyle=\int\_{0}^{t}\frac{b^{2}(1-\rho^{2})}{(r+k)^{2}}e^{-2rs}(S\_{0}(s))^{2}ds+\frac{b^{2}(1-\rho^{2})}{(r+k)^{2}(2r-(\pi^{\star}\sigma)^{2})}e^{-(2r-(\pi^{\star}\sigma)^{2})t}\mathscr{E}(2R\_{0}^{\pi^{\star}})(t), |  |

for sufficiently big rr. Hence:

|  |  |  |
| --- | --- | --- |
|  | Γ=∫0⋅θΓ​(t)​𝑑W1​(t),θΓ​(t):=−2​b2​(1−ρ2)​π⋆​σ(r+k)2​(2​r−(π⋆​σ)2)​e−(2​r−(π⋆​σ)2)​t​ℰ​(2​R0π⋆)​(t),\Gamma=\int\_{0}^{\cdot}\theta^{\Gamma}(t)dW^{1}(t),\qquad\theta^{\Gamma}(t):=-\frac{2b^{2}(1-\rho^{2})\pi^{\star}\sigma}{(r+k)^{2}(2r-(\pi^{\star}\sigma)^{2})}e^{-(2r-(\pi^{\star}\sigma)^{2})t}\mathscr{E}(2R\_{0}^{\pi^{\star}})(t), |  |

where it is direct to note that if ρ\rho tends to either 11 or −1-1, Γ\Gamma vanishes.

## 5. Utility-based pricing

The utility-based approach can also be used for the sake of pricing non-traded streams. To fix ideas we focus, for now, on the case of a finite horizon (i.e. a finite stopping time). Recalling §1.2, we define:

|  |  |  |
| --- | --- | --- |
|  | v​(x):=supX~∈𝒳~​(x)𝔼​[ln⁡(X~​(T))],v(x):=\sup\_{\widetilde{X}\in\widetilde{\mathscr{X}}(x)}\mathbb{E}[\ln(\widetilde{X}(T))], |  |

and assume:

|  |  |  |  |
| --- | --- | --- | --- |
| (A5) |  | v​(x)<∞v(x)<\infty, for some x>0x>0, |  |

which in turn implies that v​(x)<∞v(x)<\infty, for all x>0x>0 by the concavity of the logarithm. In particular, the finiteness of v​(x)v(x) yields (ln⁡(X~​(T)))+∈ℒ1(\ln(\widetilde{X}(T)))^{+}\in\mathscr{L}\_{1}, for all X~∈𝒳~​(x)\widetilde{X}\in\widetilde{\mathscr{X}}(x). To see this, note that for δ∈(0,1)\delta\in(0,1), 𝒳~​(x)∋X~δ:=δ+(1−δ)​X~\widetilde{\mathscr{X}}(x)\ni\widetilde{X}\_{\delta}:=\delta+(1-\delta)\widetilde{X} is bounded away from zero. Hence 𝔼​[ln⁡(X~​(T))]\mathbb{E}[\ln(\widetilde{X}(T))] is well-defined with values in ℝ∪{−∞}\mathbb{R}\cup\{-\infty\}, since 𝔼​[(ln⁡(X~δ​(T)))+]≥(1−δ)​𝔼​[(ln⁡(X~​(T)))+]\mathbb{E}[(\ln(\widetilde{X}\_{\delta}(T)))^{+}]\geq(1-\delta)\mathbb{E}[(\ln(\widetilde{X}(T)))^{+}].

In fact, (ln⁡(Xπ⋆​(T)))−∈ℒ1(\ln(X\_{\pi^{\star}}(T)))^{-}\in\mathscr{L}\_{1} along with (ln⁡(X~​(T)))+∈ℒ1(\ln(\widetilde{X}(T)))^{+}\in\mathscr{L}\_{1}, and [[22](https://arxiv.org/html/2601.14139v2#bib.bib6 "Portfolio theory and arbitrage: a course in mathematical finance"), Proposition 2.46] imply that the wealth process in (1,S~)(1,\widetilde{S}) with initial value x>0x>0, generated by θi⋆:=x​Xπ⋆​πi⋆/S~i\theta\_{i}^{\star}:=xX\_{\pi^{\star}}\pi^{\star}\_{i}/\widetilde{S}\_{i} for 1≤i≤d1\leq i\leq d, is the solution to to v​(x)v(x). Particularly, we get:

|  |  |  |
| --- | --- | --- |
|  | v​(x)=𝔼​[ln⁡(x+∫0T(θ⋆​(t))′​𝑑S~​(t))]=𝔼​[ln⁡(x​Xπ⋆​(T))].v(x)=\mathbb{E}\left[\ln\left(x+\int\_{0}^{T}(\theta^{\star}(t))^{{}^{\prime}}d\widetilde{S}(t)\right)\right]=\mathbb{E}\left[\ln\left(xX\_{\pi^{\star}}(T)\right)\right]. |  |

By the above, and after recalling the discussion in Remark in [1.2](https://arxiv.org/html/2601.14139v2#S1.Thmthm2 "Remark 1.2. ‣ 1.4. Utility maximization problem ‣ 1. Setup ‣ Log-optimality with small liability stream"), we derive the log-based certainty equivalent c​(ϵ)c(\epsilon) of the position (1,ϵ)(1,\epsilon) as the solution to the following equation:

|  |  |  |  |
| --- | --- | --- | --- |
| (CE) |  | 𝔼​[ln⁡(1+c​(ϵ)+∫0T(θ⋆​(t))′​𝑑S~​(t))]=𝔼​[ln⁡(X~ϵ​(T)−ϵ​Λ​(T))].\mathbb{E}\left[\ln\left(1+c(\epsilon)+\int\_{0}^{T}(\theta^{\star}(t))^{{}^{\prime}}d\widetilde{S}(t)\right)\right]=\mathbb{E}\left[\ln\left(\widetilde{X}^{\epsilon}(T)-\epsilon\Lambda(T)\right)\right]. |  |

Rearranging and using the fact that the logarithm turns multiplication into addition, we have:

|  |  |  |  |
| --- | --- | --- | --- |
| (CEII) |  | c​(ϵ)=eu​(ϵ)−1,c(\epsilon)=e^{u(\epsilon)}-1, |  |

where u​(ϵ)u(\epsilon) is given in ([1.5](https://arxiv.org/html/2601.14139v2#S1.E5 "In 1.4. Utility maximization problem ‣ 1. Setup ‣ Log-optimality with small liability stream")). In fact, we may take ([CEII](https://arxiv.org/html/2601.14139v2#S5.Ex5 "In 5. Utility-based pricing ‣ Log-optimality with small liability stream")) as an alternative characterization of the log-based certainty equivalent, and we shall do so henceforth. The advantage is that ([CEII](https://arxiv.org/html/2601.14139v2#S5.Ex5 "In 5. Utility-based pricing ‣ Log-optimality with small liability stream")) remains valid on an infinite horizon setting, does not require ([A5](https://arxiv.org/html/2601.14139v2#S5.Ex2 "In 5. Utility-based pricing ‣ Log-optimality with small liability stream")), and reduces to ([CE](https://arxiv.org/html/2601.14139v2#S5.Ex4 "In 5. Utility-based pricing ‣ Log-optimality with small liability stream")) whenever the more restrictive assumptions underlying it are in force.

Putting all these together we get the following result.

###### Corollary 5.1.

Assume the same conditions as in Theorem [2.1](https://arxiv.org/html/2601.14139v2#S2.Thmtheorem1 "Theorem 2.1. ‣ 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream"); then:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (5.1) |  | c​(ϵ)\displaystyle c(\epsilon) | +A1​ϵ+A2−A122​ϵ2+(A33−A1​A22+A136)​ϵ3+(A44+G−A1​A33−A228+A12​A24−A1424)​ϵ4=o​(ϵ4),\displaystyle+A\_{1}\epsilon+\frac{A\_{2}-A\_{1}^{2}}{2}\epsilon^{2}+\left(\frac{A\_{3}}{3}-\frac{A\_{1}A\_{2}}{2}+\frac{A\_{1}^{3}}{6}\right)\epsilon^{3}+\left(\frac{A\_{4}}{4}+G-\frac{A\_{1}A\_{3}}{3}-\frac{A\_{2}^{2}}{8}+\frac{A\_{1}^{2}A\_{2}}{4}-\frac{A\_{1}^{4}}{24}\right)\epsilon^{4}=o(\epsilon^{4}), |  |

as ϵ→0+\epsilon\rightarrow 0+; where:

|  |  |  |  |
| --- | --- | --- | --- |
|  | A1\displaystyle A\_{1} | :=𝔼​[F​(T)],A2:=𝔼​[(N​(T))2],A3:=𝔼​[(N​(T))3],A4:=𝔼​[(N​(T))4],\displaystyle=\mathbb{E}[F(T)],\ \ A\_{2}=\mathbb{E}[(N(T))^{2}],\ \ A\_{3}=\mathbb{E}[(N(T))^{3}],\ \ A\_{4}=\mathbb{E}[(N(T))^{4}], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | G\displaystyle G | :=𝔼​[(Γ​(T))2/2−(N​(T))2​Γ​(T)].\displaystyle=\mathbb{E}[(\Gamma(T))^{2}/2-(N(T))^{2}\Gamma(T)]. |  |

###### Proof.

Using ([2.1](https://arxiv.org/html/2601.14139v2#S2.E1 "In Theorem 2.1. ‣ 2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream")) write 555In §1 we’ve shown that u​(ϵ)<∞u(\epsilon)<\infty. In fact, recalling ([A3](https://arxiv.org/html/2601.14139v2#S1.Ex12 "In 1.4. Utility maximization problem ‣ 1. Setup ‣ Log-optimality with small liability stream")) it also holds that u​(ϵ)>−∞u(\epsilon)>-\infty, by potentially restricting ϵ\epsilon to a sub-interval of (0,ϵL)(0,\epsilon^{L}) s.t. ϵ​x<1\epsilon x<1. One way to see this is to take the positive wealth process in SS: Xx:=(1−ϵ​x)+ϵ​XX^{x}:=(1-\epsilon x)+\epsilon X with Xx​(0)=1X^{x}(0)=1, where XX is the process implied by ([A3](https://arxiv.org/html/2601.14139v2#S1.Ex12 "In 1.4. Utility maximization problem ‣ 1. Setup ‣ Log-optimality with small liability stream")), starting at xx. In particular, at maturity Xx​(T)−ϵ​F​(T)X^{x}(T)-\epsilon F(T) is bounded below by 1−ϵ​x>01-\epsilon x>0.:

|  |  |  |
| --- | --- | --- |
|  | u​(ϵ)=u1​ϵ+u2​ϵ2+u3​ϵ3+u4​ϵ4+o​(ϵ4),u(\epsilon)=u\_{1}\epsilon+u\_{2}\epsilon^{2}+u\_{3}\epsilon^{3}+u\_{4}\epsilon^{4}+o(\epsilon^{4}), |  |

where:

|  |  |  |
| --- | --- | --- |
|  | u1:=−A1,u2:=−A22,u3:=−A33,u4:=−(A44+G).u\_{1}:=-A\_{1},\ \ u\_{2}:=-\frac{A\_{2}}{2},\ \ u\_{3}:=-\frac{A\_{3}}{3},\ \ u\_{4}:=-\left(\frac{A\_{4}}{4}+G\right). |  |

Using ([CEII](https://arxiv.org/html/2601.14139v2#S5.Ex5 "In 5. Utility-based pricing ‣ Log-optimality with small liability stream")) and expanding:

|  |  |  |
| --- | --- | --- |
|  | c​(ϵ)=u​(ϵ)+(u​(ϵ))22+(u​(ϵ))36+(u​(ϵ))424+o​(ϵ4).c(\epsilon)=u(\epsilon)+\frac{(u(\epsilon))^{2}}{2}+\frac{(u(\epsilon))^{3}}{6}+\frac{(u(\epsilon))^{4}}{24}+o(\epsilon^{4}). |  |

Collecting terms, for order ϵ\epsilon we only have a contribution from u1u\_{1}; for order ϵ2\epsilon^{2} we have contributions from u2u\_{2}, and u12/2u\_{1}^{2}/2; for order ϵ3\epsilon^{3} we have contributions from u3u\_{3}, u1​u2u\_{1}u\_{2}, and u13/6u\_{1}^{3}/6; finally for order ϵ4\epsilon^{4} we have contributions from u4u\_{4}, u1​u3u\_{1}u\_{3}, u22/2u\_{2}^{2}/2, u12​u2/2u\_{1}^{2}u\_{2}/2, and u14/24u\_{1}^{4}/24. Bringing all these together, we get the desired result.
∎

###### Remark 5.1.

Note that in a complete market setting we have:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[F​(T)|ℱ​(⋅)]=𝔼​[F​(T)]+Δ,\mathbb{E}[F(T)|\mathscr{F}(\cdot)]=\mathbb{E}[F(T)]+\Delta, |  |

i.e. the quadratic variation of NN as well as Γ\Gamma vanish. In turn, in this context we get:

|  |  |  |
| --- | --- | --- |
|  | A2=A12,A3=A13,A4=A14,G=0.A\_{2}=A\_{1}^{2},\ \ A\_{3}=A\_{1}^{3},\ \ A\_{4}=A\_{1}^{4},\ \ G=0. |  |

Applying the above to ([5.1](https://arxiv.org/html/2601.14139v2#S5.E1 "In Corollary 5.1. ‣ 5. Utility-based pricing ‣ Log-optimality with small liability stream")) we have that its second, third, and fourth order terms vanish, and the log-based certainty equivalent reduces to −ϵ​𝔼​[F​(T)]-\epsilon\mathbb{E}[F(T)].

## References

* [1]
  H. Chau, A. Cosso, C. Fontana, and O. Mostovyi (2017)
  Optimal investment with intermediate consumption under no unbounded profit with bounded risk.
  Journal of Applied Probability (54),  pp. 710–719.
  Cited by: [Discussion](https://arxiv.org/html/2601.14139v2#Sx1.SSx1.p4.1 "Discussion ‣ Introduction ‣ Log-optimality with small liability stream").
* [2]
  J.C. Cox and C.F. Huang (1989)
  Optimal consumption and portfolio policies when asset prices follow a diffusion process.
  Journal of Mathematical Economics 49,  pp. 33–83.
  Cited by: [Discussion](https://arxiv.org/html/2601.14139v2#Sx1.SSx1.p2.1 "Discussion ‣ Introduction ‣ Log-optimality with small liability stream").
* [3]
  J.C. Cox and C.F. Huang (1991)
  A variational problem arising in financial economics.
  Journal of Mathematical Economics 20,  pp. 465–487.
  Cited by: [Discussion](https://arxiv.org/html/2601.14139v2#Sx1.SSx1.p2.1 "Discussion ‣ Introduction ‣ Log-optimality with small liability stream").
* [4]
  J. Cvitanic̀, W. Schachermayer, and H. Wang (2001)
  Utility maximization in incomplete markets with random endowment.
  Finance and Stochastics 5,  pp. 259–272.
  Cited by: [Discussion](https://arxiv.org/html/2601.14139v2#Sx1.SSx1.p4.1 "Discussion ‣ Introduction ‣ Log-optimality with small liability stream").
* [5]
  M.H.A. Davis (2006)
  Optimal hedging with basis risk.
  In From Stochastic Calculus to Mathematical Finance: The Shiryaev Festschrift,
   pp. 169–187.
  Cited by: [Related literature](https://arxiv.org/html/2601.14139v2#Sx1.SSx3.p2.1 "Related literature ‣ Introduction ‣ Log-optimality with small liability stream").
* [6]
  F. Delbaen and W. Schachermayer (1997)
  The banach space of workable contingent claims in arbitrage theory.
  Annales de l’Institut Henri Poincare (B) Probability and Statistics 33,  pp. 113–144.
  Cited by: [§1.4](https://arxiv.org/html/2601.14139v2#S1.SS4.p1.29 "1.4. Utility maximization problem ‣ 1. Setup ‣ Log-optimality with small liability stream").
* [7]
  C. Frei and M. Schweizer (2008)
  Exponential utility indifference valuation in two brownian settings with stochastic correlation.
  Advances in Applied Probability 40,  pp. 401–423.
  Cited by: [Related literature](https://arxiv.org/html/2601.14139v2#Sx1.SSx3.p2.1 "Related literature ‣ Introduction ‣ Log-optimality with small liability stream").
* [8]
  C. Frei and M. Schweizer (2010)
  Exponential utility indifference valuation in a general semimartingale model.
  In Optimality and Risk - Modern Trends in Mathematical Finance: The Kabanov Festschrift,
   pp. 49–86.
  Cited by: [Related literature](https://arxiv.org/html/2601.14139v2#Sx1.SSx3.p2.1 "Related literature ‣ Introduction ‣ Log-optimality with small liability stream").
* [9]
  M. Grasselli and T.R. Hurd (2007)
  Indifference pricing and hedging for volatility derivatives.
  Applied Mathematical Finance 14,  pp. 303–317.
  Cited by: [Related literature](https://arxiv.org/html/2601.14139v2#Sx1.SSx3.p2.1 "Related literature ‣ Introduction ‣ Log-optimality with small liability stream").
* [10]
  J.M. Harrison and D. Kreps (1979)
  Martingales and arbitrage in multiperiod security markets.
  Journal of Economic Theory 20,  pp. 381–408.
  Cited by: [Discussion](https://arxiv.org/html/2601.14139v2#Sx1.SSx1.p2.1 "Discussion ‣ Introduction ‣ Log-optimality with small liability stream").
* [11]
  J.M. Harrison and S.R. Pliska (1981)
  Martingales and stochastic integrals in the theory of continuous trading.
  Stochastic Processes and their Applications 11,  pp. 215–260.
  Cited by: [Discussion](https://arxiv.org/html/2601.14139v2#Sx1.SSx1.p2.1 "Discussion ‣ Introduction ‣ Log-optimality with small liability stream").
* [12]
  H. He and N.D. Pearson (1991)
  Consumption and portfolio policies with incomplete markets and short-sale constraints: the finite-dimensional case.
  Mathematical Finance 1,  pp. 1–10.
  Cited by: [Discussion](https://arxiv.org/html/2601.14139v2#Sx1.SSx1.p2.1 "Discussion ‣ Introduction ‣ Log-optimality with small liability stream").
* [13]
  H. He and N.D. Pearson (1991)
  Consumption and portfolio policies with incomplete markets and short-sale constraints: the infinite-dimensional case.
  Journal of Economic Theory 54,  pp. 259–304.
  Cited by: [Discussion](https://arxiv.org/html/2601.14139v2#Sx1.SSx1.p2.1 "Discussion ‣ Introduction ‣ Log-optimality with small liability stream").
* [14]
  V. Henderson and D. Hobson (2007)
  Utility indifference pricing: an overview.
  In R. Carmona (Ed.) Volume on Indifference Pricing,
  Cited by: [Discussion](https://arxiv.org/html/2601.14139v2#Sx1.SSx1.p3.1 "Discussion ‣ Introduction ‣ Log-optimality with small liability stream").
* [15]
  V. Henderson and D.G. Hobson (2002)
  Real options with constant relative risk aversion.
  Journal of Economic Dynamics & Control 27,  pp. 329–355.
  Cited by: [Related literature](https://arxiv.org/html/2601.14139v2#Sx1.SSx3.p4.2 "Related literature ‣ Introduction ‣ Log-optimality with small liability stream").
* [16]
  V. Henderson and G. Liang (2016)
  A multidimensional exponential utility indifference pricing model with applications to counterparty risk.
  SIAM Journal on Control and Optimization 54,  pp. 690–717.
  Cited by: [Related literature](https://arxiv.org/html/2601.14139v2#Sx1.SSx3.p3.1 "Related literature ‣ Introduction ‣ Log-optimality with small liability stream").
* [17]
  V. Henderson (2002)
  Valuation of claims on nontraded assets using utility maximization.
  Mathematical Finance 12,  pp. 351–373.
  Cited by: [Related literature](https://arxiv.org/html/2601.14139v2#Sx1.SSx3.p2.1 "Related literature ‣ Introduction ‣ Log-optimality with small liability stream"),
  [Related literature](https://arxiv.org/html/2601.14139v2#Sx1.SSx3.p4.2 "Related literature ‣ Introduction ‣ Log-optimality with small liability stream").
* [18]
  J. Hugonnier and D. Kramkov (2004)
  Optimal investment with random endowments in incomplete markets.
  The Annals of Applied Probability 14,  pp. 845–864.
  Cited by: [§1.4](https://arxiv.org/html/2601.14139v2#S1.SS4.p2.17 "1.4. Utility maximization problem ‣ 1. Setup ‣ Log-optimality with small liability stream"),
  [§1.4](https://arxiv.org/html/2601.14139v2#S1.SS4.p2.6 "1.4. Utility maximization problem ‣ 1. Setup ‣ Log-optimality with small liability stream"),
  [§1.4](https://arxiv.org/html/2601.14139v2#S1.SS4.p3.4 "1.4. Utility maximization problem ‣ 1. Setup ‣ Log-optimality with small liability stream"),
  [Discussion](https://arxiv.org/html/2601.14139v2#Sx1.SSx1.p4.1 "Discussion ‣ Introduction ‣ Log-optimality with small liability stream").
* [19]
  J. Kallsen, J. Muhle-Karbe, and R. Vierthauer (2014)
  Asymptotic power utility-based pricing and hedging.
  Mathematics and Financial Economics 8,  pp. 1–28.
  Cited by: [Related literature](https://arxiv.org/html/2601.14139v2#Sx1.SSx3.p7.1 "Related literature ‣ Introduction ‣ Log-optimality with small liability stream").
* [20]
  J. Kallsen and T. Rheinländer (2011)
  Asymptotic utility-based pricing and hedging for exponential utility.
  Statistics & Decisions 28,  pp. 17–36.
  Cited by: [Related literature](https://arxiv.org/html/2601.14139v2#Sx1.SSx3.p7.1 "Related literature ‣ Introduction ‣ Log-optimality with small liability stream").
* [21]
  J. Kallsen (2002)
  Derivative pricing based on local utility maximization.
  Finance and Stochastics 6,  pp. 115–140.
  Cited by: [Related literature](https://arxiv.org/html/2601.14139v2#Sx1.SSx3.p5.1 "Related literature ‣ Introduction ‣ Log-optimality with small liability stream").
* [22]
  I. Karatzas and C. Kardaras (2021)
  Portfolio theory and arbitrage: a course in mathematical finance.
  Graduate Studies in Mathematics, American Mathematical Society.
  External Links: ISBN 9781470465988
  Cited by: [§1.2](https://arxiv.org/html/2601.14139v2#S1.SS2.p2.10 "1.2. Investment opportunities ‣ 1. Setup ‣ Log-optimality with small liability stream"),
  [§1.2](https://arxiv.org/html/2601.14139v2#S1.SS2.p2.5 "1.2. Investment opportunities ‣ 1. Setup ‣ Log-optimality with small liability stream"),
  [§5](https://arxiv.org/html/2601.14139v2#S5.p2.7 "5. Utility-based pricing ‣ Log-optimality with small liability stream").
* [23]
  I. Karatzas, J.P. Lehoczky, S.E. Shreve, and G.L. Xu (1991)
  Martingale and duality methods for utility maximization in an incomplete market.
  SIAM Journal of Control and Optimization 29,  pp. 702–730.
  Cited by: [Discussion](https://arxiv.org/html/2601.14139v2#Sx1.SSx1.p2.1 "Discussion ‣ Introduction ‣ Log-optimality with small liability stream").
* [24]
  I. Karatzas, J.P. Lehoczky, and S.E. Shreve (1987)
  Optimal portfolio and consumption decisions for a “small investor” on a finite horizon.
  SIAM Journal of Control and Optimization 25,  pp. 1557–1586.
  Cited by: [Discussion](https://arxiv.org/html/2601.14139v2#Sx1.SSx1.p2.1 "Discussion ‣ Introduction ‣ Log-optimality with small liability stream").
* [25]
  I. Karatzas and G. Žitković (2003)
  Optimal consumption from investment and random endowment in incomplete semimartingale markets.
  The Annals of Applied Probability 31,  pp. 1821–1858.
  Cited by: [Discussion](https://arxiv.org/html/2601.14139v2#Sx1.SSx1.p4.1 "Discussion ‣ Introduction ‣ Log-optimality with small liability stream").
* [26]
  D. Kramkov and W. Schachermayer (1999)
  The asymptotic elasticity of utility functions and optimal investment in incomplete markets.
  The Annals of Applied Probability 9,  pp. 904–950.
  Cited by: [§3](https://arxiv.org/html/2601.14139v2#S3.3.p1.14 "Proof. ‣ 3. Second order expansion of optimal wealth w.r.t. ϵ ‣ Log-optimality with small liability stream"),
  [Discussion](https://arxiv.org/html/2601.14139v2#Sx1.SSx1.p2.1 "Discussion ‣ Introduction ‣ Log-optimality with small liability stream").
* [27]
  D. Kramkov and W. Schachermayer (2003)
  Necessary and sufficient conditions in the problem of optimal investment in incomplete markets.
  The Annals of Applied Probability 13,  pp. 1504–1516.
  Cited by: [Discussion](https://arxiv.org/html/2601.14139v2#Sx1.SSx1.p2.1 "Discussion ‣ Introduction ‣ Log-optimality with small liability stream").
* [28]
  D. Kramkov and M. Sîrbu (2006)
  Sensitivity analysis of utility-based prices and risk-tolerance wealth processes.
  Annals of Applied Probability 16,  pp. 2140–2194.
  Cited by: [§2](https://arxiv.org/html/2601.14139v2#S2.p1.28 "2. Fourth order expansion of value function w.r.t. ϵ ‣ Log-optimality with small liability stream"),
  [§3](https://arxiv.org/html/2601.14139v2#S3.3.p1.14 "Proof. ‣ 3. Second order expansion of optimal wealth w.r.t. ϵ ‣ Log-optimality with small liability stream"),
  [item 1](https://arxiv.org/html/2601.14139v2#Sx1.I1.i1.p1.2 "In Contributions ‣ Introduction ‣ Log-optimality with small liability stream"),
  [Related literature](https://arxiv.org/html/2601.14139v2#Sx1.SSx3.p5.1 "Related literature ‣ Introduction ‣ Log-optimality with small liability stream"),
  [Related literature](https://arxiv.org/html/2601.14139v2#Sx1.SSx3.p7.1 "Related literature ‣ Introduction ‣ Log-optimality with small liability stream").
* [29]
  D. Kramkov and M. Sîrbu (2007)
  Asymptotic analysis of utility-based hedging strategies for small number of contingent claims.
  Stochastic Processes and their Applications 117,  pp. 1606–1620.
  Cited by: [item 1](https://arxiv.org/html/2601.14139v2#Sx1.I1.i1.p1.2 "In Contributions ‣ Introduction ‣ Log-optimality with small liability stream"),
  [Related literature](https://arxiv.org/html/2601.14139v2#Sx1.SSx3.p5.1 "Related literature ‣ Introduction ‣ Log-optimality with small liability stream"),
  [Related literature](https://arxiv.org/html/2601.14139v2#Sx1.SSx3.p6.1 "Related literature ‣ Introduction ‣ Log-optimality with small liability stream"),
  [Related literature](https://arxiv.org/html/2601.14139v2#Sx1.SSx3.p7.1 "Related literature ‣ Introduction ‣ Log-optimality with small liability stream").
* [30]
  T. Leung and M. Ludkovski (2012)
  Accounting for risk aversion in derivatives purchase timing.
  Mathematics and Financial Economics 6,  pp. 363–386.
  Cited by: [Related literature](https://arxiv.org/html/2601.14139v2#Sx1.SSx3.p2.1 "Related literature ‣ Introduction ‣ Log-optimality with small liability stream").
* [31]
  C. Ménassé and P. Tankov (2016)
  Asymptotic indifference pricing in exponential lévy models.
  Applied Mathematical Finance 23,  pp. 197–235.
  Cited by: [Related literature](https://arxiv.org/html/2601.14139v2#Sx1.SSx3.p8.1 "Related literature ‣ Introduction ‣ Log-optimality with small liability stream").
* [32]
  R.C. Merton (1969)
  Lifetime portfolio selection under uncertainty: the continuous-time case.
  Rev. Econom. Statist. 51,  pp. 247–257.
  Cited by: [Discussion](https://arxiv.org/html/2601.14139v2#Sx1.SSx1.p1.1 "Discussion ‣ Introduction ‣ Log-optimality with small liability stream").
* [33]
  R.C. Merton (1971)
  Optimum consumption and prtfolio rules in a continuous-time model.
  Journal of Economic Theory 3,  pp. 373–413.
  Cited by: [Discussion](https://arxiv.org/html/2601.14139v2#Sx1.SSx1.p1.1 "Discussion ‣ Introduction ‣ Log-optimality with small liability stream").
* [34]
  M. Monoyios (2004)
  Performance of utility-based strategies for hedging basis risk.
  Quantitative Finance 4,  pp. 245–255.
  Cited by: [Related literature](https://arxiv.org/html/2601.14139v2#Sx1.SSx3.p4.2 "Related literature ‣ Introduction ‣ Log-optimality with small liability stream").
* [35]
  M. Monoyios (2007)
  Optimal hedging and parameter uncertainty.
  IMA Journal of Management Mathematics 18,  pp. 331–351.
  Cited by: [Related literature](https://arxiv.org/html/2601.14139v2#Sx1.SSx3.p4.2 "Related literature ‣ Introduction ‣ Log-optimality with small liability stream").
* [36]
  M. Monoyios (2010)
  Utility-based valuation and hedging of basis risk with partial information.
  Applied Mathematical Finance 17,  pp. 519–551.
  Cited by: [Related literature](https://arxiv.org/html/2601.14139v2#Sx1.SSx3.p6.1 "Related literature ‣ Introduction ‣ Log-optimality with small liability stream").
* [37]
  M. Monoyios (2013)
  Malliavin calculus method for asymptotic expansion of dual control problems.
  SIAM Journal of Financial Mathematics 4,  pp. 884–915.
  Cited by: [Related literature](https://arxiv.org/html/2601.14139v2#Sx1.SSx3.p2.1 "Related literature ‣ Introduction ‣ Log-optimality with small liability stream").
* [38]
  O. Mostovyi and M. Sirbu (2019)
  Sensitivity analysis of the utility maximization problem with respect to model perturbations.
  Finance and Stochastics (23),  pp. 595–640.
  Cited by: [Related literature](https://arxiv.org/html/2601.14139v2#Sx1.SSx3.p9.1 "Related literature ‣ Introduction ‣ Log-optimality with small liability stream").
* [39]
  O. Mostovyi and M. Sirbu (2024)
  Quadratic expansions in optimal investment with respect to perturbations of the semimartingale model.
  Finance and Stochastics (28),  pp. 553–613.
  Cited by: [Related literature](https://arxiv.org/html/2601.14139v2#Sx1.SSx3.p9.1 "Related literature ‣ Introduction ‣ Log-optimality with small liability stream").
* [40]
  O. Mostovyi (2015)
  Necessary and sufficient conditions in the problem of optimal investment with intermediate consumption.
  Finance and Stochastics (19),  pp. 135–159.
  Cited by: [Discussion](https://arxiv.org/html/2601.14139v2#Sx1.SSx1.p4.1 "Discussion ‣ Introduction ‣ Log-optimality with small liability stream").
* [41]
  O. Mostovyi (2017)
  Optimal investment with intermediate consumption and random endowment.
  Mathematical Finance (27),  pp. 96–114.
  Cited by: [Discussion](https://arxiv.org/html/2601.14139v2#Sx1.SSx1.p4.1 "Discussion ‣ Introduction ‣ Log-optimality with small liability stream").
* [42]
  O. Mostovyi (2020)
  Asymptotic analysis of the expected utility maximization problem with respect to perturbations of the numeraire.
  Stochastic Processes and their Applications (130),  pp. 4444–4469.
  Cited by: [Related literature](https://arxiv.org/html/2601.14139v2#Sx1.SSx3.p9.1 "Related literature ‣ Introduction ‣ Log-optimality with small liability stream").
* [43]
  M. Musiela and T. Zariphopoulou (2004)
  An example of indifference prices under exponential preferences.
  Finance and Stochastics 8,  pp. 229–239.
  Cited by: [Related literature](https://arxiv.org/html/2601.14139v2#Sx1.SSx3.p2.1 "Related literature ‣ Introduction ‣ Log-optimality with small liability stream").
* [44]
  M. Owen and G. Žitković (2009)
  Optimal investment with an unbounded random endowment and utility-based pricing.
  Mathematical Finance 19,  pp. 129–159.
  Cited by: [Discussion](https://arxiv.org/html/2601.14139v2#Sx1.SSx1.p4.1 "Discussion ‣ Introduction ‣ Log-optimality with small liability stream").
* [45]
  S.R. Pliska (1986)
  A stochastic calculus model of continuous trading: optimal portfolio.
  Mathematics of Operational Research 11,  pp. 371–382.
  Cited by: [Discussion](https://arxiv.org/html/2601.14139v2#Sx1.SSx1.p2.1 "Discussion ‣ Introduction ‣ Log-optimality with small liability stream").
* [46]
  S.A. Ross (1976)
  The arbitrage theory of capital asset pricing.
  Journal of Economic Theory 13,  pp. 341–360.
  Cited by: [Discussion](https://arxiv.org/html/2601.14139v2#Sx1.SSx1.p2.1 "Discussion ‣ Introduction ‣ Log-optimality with small liability stream").
* [47]
  R. Sircar and T. Zariphopoulou (2005)
  Bounds and asymptotic approximations for utility prices when volatility is random.
  SIAM Journal on Control and Optimization 43,  pp. 1328–1353.
  Cited by: [Related literature](https://arxiv.org/html/2601.14139v2#Sx1.SSx3.p3.1 "Related literature ‣ Introduction ‣ Log-optimality with small liability stream").
* [48]
  T. Zariphopoulou (2001)
  A solution approach to valuation with unhedgeable risks.
  Finance and Stochastics 5,  pp. 61–82.
  Cited by: [Related literature](https://arxiv.org/html/2601.14139v2#Sx1.SSx3.p2.1 "Related literature ‣ Introduction ‣ Log-optimality with small liability stream").