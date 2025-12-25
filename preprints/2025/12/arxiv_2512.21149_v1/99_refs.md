---
authors:
- Luca De Gennaro Aquino
- Sascha Desmettre
- Yevhen Havrylenko
- Mogens Steffensen
doc_id: arxiv:2512.21149v1
family_id: arxiv:2512.21149
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Equilibrium investment under dynamic preference uncertainty
url_abs: http://arxiv.org/abs/2512.21149v1
url_html: https://arxiv.org/html/2512.21149v1
venue: arXiv q-fin
version: 1
year: 2025
---


Luca De Gennaro Aquino111Department of Engineering, Reykjavik University, Iceland. <lucaa@ru.is> Sascha Desmettre222Institute of Financial Mathematics and Applied Number Theory, Johannes Kepler University Linz, Austria. <sascha.desmettre@jku.at>
  
Yevhen Havrylenko333Faculty of Business and Economics, University of Lausanne, Switzerland. [yevhen.havrylenko@unil.ch](yevhen.havrylenko@unil.cg)  Mogens Steffensen444Department of Mathematical Sciences, University of Copenhagen, Denmark. <mogens@math.ku.dk>

###### Abstract

We study a continuous-time portfolio choice problem for an investor whose state-dependent preferences are determined by an exogenous factor that evolves as an Itô diffusion process. Since risk attitudes at the end of the investment horizon are uncertain, terminal wealth is evaluated under a set of utility functions corresponding to all possible future preference states. These utilities are first converted into certainty equivalents at their respective levels of terminal risk aversion and then (nonlinearly) aggregated over the conditional distribution of future states, yielding an inherently time-inconsistent optimization criterion. We approach this problem by developing a general equilibrium framework for such state-dependent preferences and characterizing subgame-perfect equilibrium investment policies through an extended Hamilton–Jacobi–Bellman system. This system gives rise to a coupled nonlinear partial integro-differential equation for the value functions associated with each state. We then specialize the model to a tractable constant relative risk aversion specification in which the preference factor follows an arithmetic Brownian motion. In this setting, the equilibrium policy admits a semi-explicit representation that decomposes into a standard myopic demand and a novel preference-hedging component that captures incentives to hedge against anticipated changes in risk aversion. Numerical experiments illustrate how features of the preference dynamics –most notably the drift of the preference process and the correlation between preference shocks and asset returns– jointly determine the sign and magnitude of the hedging demand and the evolution of the equilibrium risky investment over time.

Keywords: Preference uncertainty, time-inconsistency, equilibrium control theory, certainty equivalents

AMS subject classifications: 91B16, 91B42, 91G10

## 1 Introduction

Optimal dynamic investment problems under uncertainty form a central theme in mathematical finance.
Classical formulations of these problems typically vary along three main dimensions: (i) the nature of the decisions to be made (investment, consumption, insurance, etc.); (ii) the structure of the underlying market (completeness, presence of jumps, stochastic market coefficients, and related features); and (iii) the objective functional (mean-variance trade-offs, expected utility maximization, constraints, or combinations thereof). Within this broad landscape, expected utility maximization remains the dominant paradigm, thanks to its well-established axiomatic foundation and compatibility with dynamic programming.

Most of the existing literature adopts a fixed parametric specification of preferences, typically power utility with a constant relative risk aversion (CRRA). While substantial effort has gone into modeling uncertainty in the financial market (e.g., by replacing deterministic returns and volatilities with stochastic processes), far less attention has been devoted to modeling uncertainty in preferences themselves. The prevailing assumption is that the decision maker knows her utility function and its parameters exactly. As a consequence, comparative statics with respect to the risk aversion coefficient are usually interpreted as comparisons across different agents, rather than as reflecting the uncertainty a single individual may face regarding her own risk attitudes. From a practical perspective, however, the choice of a utility function and its parameters is often the most contentious aspect of the modeling exercise, and skepticism about these inputs can undermine the normative force of the resulting optimization results.

This paper takes a different perspective by treating risk aversion itself as an uncertain and dynamically evolving quantity. Modeling such preference uncertainty introduces a number of conceptual choices. Even in the simple power utility setting, one must specify whether the risk aversion parameter is a random variable or a random process, whether it is observable or latent, what information about it can be learned over time, and whether it should be correlated with the financial market. Each of these modeling choices leads to a distinct dynamic optimization problem. In this paper, we focus on an investor who observes her current level of risk aversion, anticipates that it will evolve randomly over time, and takes this evolution into account when forming long-term investment plans. To capture this, we model risk aversion as a function of an observable diffusion, which may be correlated with the market, and thus can span cases where preferences and returns are independent as well as cases where they are systematically linked.

When formulating a decision problem under random risk aversion, a technical difficulty arises: outcomes evaluated under different utility functions are not directly comparable. Even for power utility, a payoff preferred at one risk aversion level may not be preferred at another, and utilities themselves live on incomparable scales. To resolve this, we map utilities associated with different future risk aversion levels onto a common scale by means of certainty equivalents, and then aggregate them through a flexible second-stage operator. The objective functional resulting from this normalization-aggregation procedure involves an integral of nonlinear transformations of conditional expectations, a structure known to generate time-inconsistency. As a consequence, the usual notion of optimal control is no longer appropriate. Instead, the proper solution concept is that of a time-consistent equilibrium strategy, meaning a strategy that is locally optimal at every point in time.

We develop a continuous-time framework for portfolio choice under evolving, state-dependent preferences and provide both the theoretical foundations and explicit characterizations of an equilibrium investment behavior in this setting.

Our first contribution is to formulate a coherent intertemporal criterion for a decision maker who anticipates that her future risk attitudes will change and that terminal wealth will ultimately be evaluated under the utility corresponding to the realized future state. As mentioned, to compare outcomes evaluated under different utilities, we normalize them through state-specific certainty equivalents and aggregate across future preference realizations using an outer evaluation function. This construction accommodates broad classes of utility functions and preference specifications, and it makes explicit how random, evolving risk aversion generates intrinsic time-inconsistency, even when preferences are fully observable and the market is otherwise standard.

Our second contribution is methodological. The equilibrium Hamilton–Jacobi–Bellman (HJB) formulations available in earlier studies cannot be applied directly to our framework: the objective involves conditioning on future preference states and an uncountable family of nonlinear transformations of conditional expected utilities. We develop an extension of the equilibrium HJB approach that addresses these two difficulties simultaneously. The key steps are: (i) deriving the dynamics of the state variables under conditioning on a future preference state (Section [3.1](https://arxiv.org/html/2512.21149v1#S3.SS1 "3.1 Preliminary definitions and state process dynamics under conditional measures ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")); and (ii) establishing the limiting form –as the number of approximation terms tends to infinity– of the extended HJB system (eHJB) characterizing an equilibrium strategy for a finite-sum approximation of the original reward functional (Section [3.2](https://arxiv.org/html/2512.21149v1#S3.SS2 "3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")). This yields a new system that captures the structure of preference uncertainty and is linked to several existing results on equilibrium investment under random risk aversion.

Our third contribution is a verification theorem showing that any solution to the eHJB indeed generates an equilibrium strategy (Section [3.3](https://arxiv.org/html/2512.21149v1#S3.SS3 "3.3 Verification results ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")). This result provides the conceptual bridge between the abstract equilibrium definition and the PDE characterization.

Finally, we apply our framework to a tractable CRRA specification in which the preference factor follows an arithmetic Brownian motion (Section [4](https://arxiv.org/html/2512.21149v1#S4 "4 Application: state-dependent CRRA utility ‣ Equilibrium investment under dynamic preference uncertainty")). In this setting, the equilibrium conditions reduce to a system that yields the semi-explicit representation of an equilibrium portfolio rule. The resulting policy decomposes into the familiar myopic demand and a new preference-hedging component that reflects the investor’s incentive to adjust her exposure in anticipation of future changes in risk aversion. The structure, sign, and magnitude of this hedging term depend on the drift and volatility of the preference process, its correlation with asset returns, and the shape of the certainty equivalent aggregator.

Even in this simplified CRRA environment, the equilibrium conditions give rise to a coupled nonlinear partial integro-differential equation (PIDE) for the auxiliary value functions associated with each potential preference state. This system cannot be solved analytically and presents significant numerical challenges due to its dimensionality and the continuum of conditioning arguments. To address this, we apply a neural network-based solution method that formulates the PIDE system as a physics-informed learning problem.

Numerical experiments based on this approach illustrate how preference dynamics shape both the hedging demand and the evolution of the equilibrium risky investment over time.

#### Related literature.

Our work relates to and expands several research areas. Optimal investment under state-dependent utility has been studied in BVY18, who adopt the martingale method to obtain explicit solutions and avoid issues of time-inconsistency by not using certainty equivalents for normalization. In their framework, random preferences are fully correlated with the financial market. Optimal consumption, investment, and insurance under state-dependent risk aversion in the health dimension are analyzed in SoS23. As in BVY18, they do not use certainty equivalents, but, in contrast, their random preferences are not correlated with asset returns.

Beyond these contributions, several papers consider time-varying risk attitudes more generally, including Netzer2009:AER, Schildberg2018:JEP, and Bekaert2022:MS, who document how attitudes toward risk may adjust with economic conditions, learning, or endogenous feedback mechanisms. In addition, a substantial body of empirical evidence suggests that preferences themselves are uncertain and subject to latent heterogeneity. Experimental studies, such as WeberMilliman1997:MS, Fischer2000:MS, AndersenEtAl2008:IER, and Brunnermeier2008:AER, show that individuals display significant variation in measured risk aversion across tasks, contexts, and time, supporting the view that preferences may evolve with economic or personal circumstances.

A paper that is particularly close in spirit to ours is DesmettreSteffensen2023:MF, who average over the distribution of certainty equivalents associated with different realizations of an individual’s risk aversion. The primary distinction is that they treat risk aversion as a static random variable, about which the decision maker receives no new information. In contrast, we model risk aversion as an observable stochastic process driven by a stochastic differential equation (SDE), thus offering a greater level of flexibility and dynamic structure.

BS21 also employ certainty equivalents to normalize across a heterogeneous set of agents with varying preferences. More specifically, their objective is formulated as a two-stage utility functional, where an outer utility function is applied to the distribution of the agents’ certainty equivalents. Another related work is ChenGuanLiang2025, in which risk aversion is determined by a finite-state Markov chain that identifies market regimes. Each regime determines both the drift and volatility of returns and the level of risk aversion, and the optimization problem aggregates expected certainty equivalents across regimes, leading to time-inconsistency.

On the methodological side, our approach is rooted in the equilibrium concept for time-inconsistent control problems. The interpretation that dynamically inconsistent preferences can be treated as a non-cooperative game between successive selves goes back to Strotz1956:RES. A precise mathematical formalization in continuous time was provided by EkelandLazrak2010:MFE, EkelandPirvu2008:MFE, and EkelandMbodjiPirvu2012:SIFIN, primarily in the context of non-exponential discounting. The mean-variance optimization problem, initially incorporated in this framework by BasakChabakauri2010:RFS, was subsequently formalized in the general equilibrium approach by BjorkMurgoci2014:FS, BjorkMurgociZhou2014:MF, and BjorkKhapkoMurgoci2017:FS. KrygerNordfangSteffensen2020:MMRO provide a survey-style overview of objectives where time-inconsistency originates from nonlinearities such as the square function. A comprehensive review of time-inconsistent control theory with applications in finance is given in BjoerkKhapkoMurgoci2021:TICT. Problems in which time-inconsistency arises from certainty equivalents have also been approached through equilibrium theory; see, for example, JensenSteffensen2015:IME and FahrenwaldtJensenSteffensen2020:JME, who aggregate certainty equivalents to disentangle time and risk preferences.

The structure of our objective functional also bears a formal resemblance to the smooth ambiguity model of KlibanoffMarinacciMukerji2005:Econometrica; KlibanoffMarinacciMukerji2009:JET, which separates attitudes toward risk from attitudes toward model uncertainty. However, the rationale is fundamentally different, as in our model, the aggregation reflects uncertainty about future preferences rather than ambiguity about probability models; we expand on this parallel in Remark [2.2](https://arxiv.org/html/2512.21149v1#S2.Thmtheorem2 "Remark 2.2. ‣ 2 Problem formulation ‣ Equilibrium investment under dynamic preference uncertainty"). Similar themes of model uncertainty in dynamic equilibrium problems can be found in GuanLiangXia2025:MOR, who combine smooth ambiguity preferences with equilibrium strategies and learning about uncertain asset drift.

Finally, our setting is related to the literature on forward performance processes, as established by MusielaZariphopoulou2007investment; MusielaZariphopoulou2008optimal and Z09. They introduce a new class of dynamic utilities generated forward in time and allow these utilities to be stochastic processes, similar to the exposition in this paper. The key difference is that they do not rely on certainty equivalents, and time-inconsistency does not arise. In that direction, Maggis2025 more recently elaborated on the consistency of optimal portfolio choice for state-dependent exponential utilities, and found that a unique forward prediction of random risk aversion exists, ensuring the consistency of optimal strategies across any time horizon.

#### Structure of the paper

The rest of the paper unfolds as follows. Section [2](https://arxiv.org/html/2512.21149v1#S2 "2 Problem formulation ‣ Equilibrium investment under dynamic preference uncertainty") introduces the economic environment, including the financial market, the preference state process, and the reward functional used to evaluate portfolio strategies. Section [3](https://arxiv.org/html/2512.21149v1#S3 "3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty") develops the extended equilibrium HJB system and contains the verification theorem. Section [4](https://arxiv.org/html/2512.21149v1#S4 "4 Application: state-dependent CRRA utility ‣ Equilibrium investment under dynamic preference uncertainty") specializes the framework to a tractable CRRA setting. Section [5](https://arxiv.org/html/2512.21149v1#S5 "5 Conclusion ‣ Equilibrium investment under dynamic preference uncertainty") concludes. All technical proofs and auxiliary results are collected in the Appendices.

## 2 Problem formulation

Let (Ω,ℱ,(ℱt)0≤t≤T,ℙ)(\Omega,\mathcal{F},(\mathcal{F}\_{t})\_{0\leq t\leq T},\mathbb{P}) be a filtered probability space satisfying the usual conditions, where T>0T>0 is a fixed time horizon, and let B1B^{1} and B2B^{2} be two independent standard Brownian motions on this space. We denote by 𝒯:=[0,T]\mathcal{T}:=[0,T] the investment period.

The investor operates under a classical Black–Scholes financial market with a risk-free asset and one risky asset:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St0\displaystyle dS^{0}\_{t} | =St0​r​d​t,\displaystyle=S^{0}\_{t}rdt\,, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St1\displaystyle dS^{1}\_{t} | =St1​(μS​d​t+σS​(ρ​d​Bt1+1−ρ2​d​Bt2)),\displaystyle=S^{1}\_{t}\left(\mu\_{S}dt+\sigma\_{S}\left(\rho dB^{1}\_{t}+\sqrt{1-\rho^{2}}dB^{2}\_{t}\right)\right)\,, |  |

with r,μS∈ℝ,σS>0r,\mu\_{S}\in\mathbb{R},\sigma\_{S}>0, ρ∈[−1,1]\rho\in[-1,1] constants. Here, we introduced two Brownian motions to keep track of two distinct sources of uncertainty. One of them, B1B^{1}, will also drive the evolution of the preference factor (described below) so that shocks to the risky asset can be correlated with shocks to risk aversion. The second, B2B^{2}, provides an independent source of randomness.

In what follows, we denote by π​(t,x,y)∈ℝ\pi(t,x,y)\in\mathbb{R} the fraction of wealth invested in the stock S1S^{1} at time tt, given current wealth xx and preference state yy. The process π=(π​(t,Xtπ,Yt))t∈𝒯\pi=\left(\pi(t,X^{\pi}\_{t},Y\_{t})\right)\_{t\in\mathcal{T}} is referred to as the portfolio strategy, the investment strategy, or simply the control. For brevity, we will often write π​(t)\pi(t) in place of π​(t,Xtπ,Yt)\pi(t,X^{\pi}\_{t},Y\_{t}). (We adopt the notation π​(t)\pi(t), instead of πt\pi\_{t}, to emphasize that the control depends explicitly on the current time –and state variables–, rather than to suggest a dynamic process indexed by tt.)

The controlled wealth process Xπ=(Xtπ)t∈𝒯X^{\pi}=\left(X^{\pi}\_{t}\right)\_{t\in\mathcal{T}}, under an admissible portfolio strategy π\pi, is given by the solution of the SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xtπ=Xtπ​(r+π​(t)​(μS−r))​d​t+Xtπ​π​(t)​σS​(ρ​d​Bt1+1−ρ2​d​Bt2),X0π=x0>0.\begin{split}dX^{\pi}\_{t}&=X^{\pi}\_{t}(r+\pi(t)(\mu\_{S}-r))dt+X^{\pi}\_{t}\pi(t)\sigma\_{S}\left(\rho dB^{1}\_{t}+\sqrt{1-\rho^{2}}dB^{2}\_{t}\right)\,,\\ X^{\pi}\_{0}&=x\_{0}>0.\end{split} |  | (2.1) |

The drift μX\mu\_{X} and diffusion σX\sigma\_{X} of XπX^{\pi}, in accordance with ([2.1](https://arxiv.org/html/2512.21149v1#S2.E1 "In 2 Problem formulation ‣ Equilibrium investment under dynamic preference uncertainty")), may be written compactly as

|  |  |  |
| --- | --- | --- |
|  | d​Xtπ=μX​(t,Xtπ,π​(t))​d​t+σX​(t,Xtπ,π​(t))​d​Bt,dX^{\pi}\_{t}=\mu\_{X}(t,X^{\pi}\_{t},\pi(t))dt+\sigma\_{X}(t,X^{\pi}\_{t},\pi(t))dB\_{t}, |  |

where B:=(B1,B2)B:=(B^{1},B^{2}). The wealth process takes values in 𝒳:=(0,∞)\mathcal{X}:=(0,\infty).

To model time variation in risk attitudes, we introduce an exogenous factor process YY, taking values in a state space 𝒴\mathcal{Y}, and governed by the diffusion process

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Yt=μY​(t,Yt)​d​t+σY​(t,Yt)​d​Bt1,Y0=y0∈ℝ,dY\_{t}=\mu\_{Y}(t,Y\_{t})dt+\sigma\_{Y}(t,Y\_{t})dB^{1}\_{t},\qquad Y\_{0}=y\_{0}\in\mathbb{R}, |  | (2.2) |

where μY,σY:𝒯×𝒴↦ℝ\mu\_{Y},\sigma\_{Y}:\mathcal{T}\times\mathcal{Y}\mapsto\mathbb{R} are continuous functions ensuring that ([2.2](https://arxiv.org/html/2512.21149v1#S2.E2 "In 2 Problem formulation ‣ Equilibrium investment under dynamic preference uncertainty")) has a unique strong solution and σY​(t,y)≠0\sigma\_{Y}(t,y)\neq 0 for all (t,y)∈𝒯×𝒴(t,y)\in\mathcal{T}\times\mathcal{Y}. Note that while ChenGuanLiang2025 assume the independence between the preference factor and the risky asset, we allow for arbitrary correlation through the common Brownian motion B1B^{1}.

The process YY serves as the sole driver of intertemporal fluctuations in preferences; that is, the investor’s risk attitude at time tt is captured through the mapping γ:𝒴↦ℝ\gamma:\mathcal{Y}\mapsto\mathbb{R}, which parametrizes the curvature of the instantaneous utility function. Therefore, all changes in risk aversion arise from the stochastic evolution of YY.

Intuitively, the factor YY may represent broad economic indicators, such as stock prices or volatility, or more individual circumstances, such as health conditions or habits. For a fixed realization of YT=y¯Y\_{T}=\bar{y}, the value γ​(y¯)\gamma(\bar{y}) is then inserted into a utility specification, where, depending on the chosen utility family, it parametrizes either relative risk aversion or absolute risk aversion. (In the present formulation, only the terminal value YTY\_{T} enters the utility evaluation, so we only require a parameterization of γ\gamma at time TT. Nonetheless, if one were to introduce intermediate consumption, the same mechanism would naturally extend to a time-varying risk aversion index γ​(Yt)\gamma(Y\_{t}), applied at each consumption time.)

The usual notions of constant relative or absolute risk aversion refer primarily to the parameter’s independence on wealth, and this feature is preserved here. What we allow, however, is that risk aversion may shift in response to the evolution of the underlying state variable YY. Thus, along the wealth dimension, the investor behaves like a standard CRRA or CARA agent, while economic or personal conditions summarized by YY can make the investor effectively more or less risk-averse over time.

For each possible future preference state y¯∈𝒴\bar{y}\in\mathcal{Y}, we denote by uγ​(y¯):𝒳→ℝu^{\gamma(\bar{y})}:\mathcal{X}\to\mathbb{R} the von-Neumann-Morgenstern utility function associated with the risk aversion level γ​(y¯)\gamma(\bar{y}). We assume that each uγ​(y¯)u^{\gamma(\bar{y})} is increasing, strictly concave, and twice continuously differentiable, with strictly nonvanishing marginal utility, i.e., (uγ​(y¯))′​(x)≠0,(u^{\gamma(\bar{y})})^{\prime}(x)\neq 0, for all x∈𝒳x\in\mathcal{X}.

###### Remark 2.1.

The pair (Y,γ)(Y,\gamma) is intentionally not uniquely determined. Only the composite quantity γ​(y¯)\gamma(\bar{y}) matters for preferences, and different choices of y¯\bar{y} and γ\gamma can produce the same effective specification. For example, in the numerical section, we formalize the state variable as an arithmetic Brownian motion and take γ​(y¯)=exp⁡(y¯)\gamma(\bar{y})=\exp(\bar{y}), which leads to the risk aversion becoming a geometric Brownian motion.
The very same structure could instead be obtained by choosing YY directly as a geometric Brownian motion and letting γ\gamma be the identity function. More generally, any monotone reparameterization of YY, combined with the corresponding inverse adjustment of γ\gamma, leaves the induced preferences unchanged.

This apparent ambiguity is a feature rather than a limitation: it enables us to place different *types* of risk aversion, such as relative and absolute risk aversion, within a common framework, in the sense that the same underlying factor YY, be that a stock price or a health index, may drive both the CRRA and the CARA. The model, therefore, accommodates situations in which several facets of risk attitudes respond to the same economic or personal conditions.

Before defining the objective functional, we describe the utility structure induced by preference uncertainty. As mentioned, at the investment horizon, terminal wealth is evaluated under the utility function uγ​(y¯)u^{\gamma(\bar{y})}, for each y¯∈𝒴\bar{y}\in\mathcal{Y}. However, utilities arising from different preference states are not directly comparable, hence after computing the conditional expected utility under the scenario YT=y¯,Y\_{T}=\bar{y},
we normalize it via the inverse utility (uγ​(y¯))−1\left(u^{\gamma(\bar{y})}\right)^{-1}, obtaining the certainty equivalent at the preference state y¯\bar{y}:

|  |  |  |
| --- | --- | --- |
|  | (uγ​(YT))−1​(𝔼t,x,y,y¯​[uγ​(YT)​(XTπ)]),\left(u^{\gamma(Y\_{T})}\right)^{-1}\Big(\mathbb{E}\_{t,x,y,\overline{y}}\left[u^{\gamma(Y\_{T})}(X^{\pi}\_{T})\right]\Big), |  |

with the conditional expectation meant as 𝔼t,x,y,y¯[⋅]:=𝔼[⋅|Xtπ=x,Yt=y,YT=y¯].\mathbb{E}\_{t,x,y,\overline{y}}\big[\cdot\big]:=\mathbb{E}\big[\cdot\,|\,X^{\pi}\_{t}=x,Y\_{t}=y,Y\_{T}=\overline{y}\big].
These state-dependent certainty equivalents are then aggregated across all possible future preference states through a function v:𝒳→ℝv:\mathcal{X}\to\mathbb{R}, which is assumed to be increasing and twice continuously differentiable.

This produces the reward functional

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jπ​(t,x,y):=𝔼t,x,y​[v∘(uγ​(YT))−1​(𝔼t,x,y,y¯​[uγ​(YT)​(XTπ)])],J^{\pi}(t,x,y):=\mathbb{E}\_{t,x,y}\left[v\circ\left(u^{\gamma(Y\_{T})}\right)^{-1}\Big(\mathbb{E}\_{t,x,y,\overline{y}}\left[u^{\gamma(Y\_{T})}(X^{\pi}\_{T})\right]\Big)\right]\,,\\ |  | (2.3) |

where v∘(uγ​(YT))−1v\circ\left(u^{\gamma(Y\_{T})}\right)^{-1} denotes the composition of vv and (uγ​(YT))−1\left(u^{\gamma(Y\_{T})}\right)^{-1}.

This two-stage normalization-aggregation structure provides a coherent way to compare utilities generated under different future preference states, but it also introduces nonlinear conditioning on both the present and future preference states, thereby generating time-inconsistency.

###### Remark 2.2.

The outer function vv in ([2.3](https://arxiv.org/html/2512.21149v1#S2.E3 "In 2 Problem formulation ‣ Equilibrium investment under dynamic preference uncertainty")) plays a role reminiscent of the second-order utility (also referred to as the ambiguity index) in the smooth ambiguity model of KlibanoffMarinacciMukerji2005:Econometrica. In their model, Klibanoff, Marinacci, and Mukerji (KMM) aggregate expected first-order utility via a fixed function ϕ\phi, whose concavity (convexity) directly encodes ambiguity aversion (ambiguity loving). In our setting, aggregation occurs through the family of functions v∘(uγ​(y¯))−1v\circ\left(u^{\gamma(\overline{y})}\right)^{-1}, which depend explicitly on the future preference state y¯\overline{y} and are therefore random rather than fixed.

Alternatively, one may regard vv itself as a deterministic aggregator applied to certainty equivalents (instead of expected utilities, as in the KMM model), conditional on YT=y¯Y\_{T}=\overline{y}. The curvature of vv therefore governs the attitude toward ambiguity in certainty equivalents, which is not directly analogous to the curvature of ϕ\phi. Therefore, the economic meaning of concavity differs across the two frameworks: while the concavity of ϕ\phi captures aversion to model uncertainty, the concavity of vv captures aversion to dispersion in normalized payoffs arising from uncertain future preferences.

We next specify the class of admissible investment strategies. Admissibility here requires that the wealth and preference processes remain well-defined under the chosen control, and that the reward functional Jπ​(t,x,y)J^{\pi}(t,x,y) is finite for all initial states.

###### Definition 2.3 (Admissible control law).

An admissible control law is a map π:𝒯×𝒳×𝒴→ℝ\pi:\mathcal{T}\times\mathcal{X}\times\mathcal{Y}\to\mathbb{R} satisfying the following conditions:

1. (a)

   For each initial point (t,x,y)∈𝒯×𝒳×𝒴(t,x,y)\in\mathcal{T}\times\mathcal{X}\times\mathcal{Y}, the SDEs ([2.1](https://arxiv.org/html/2512.21149v1#S2.E1 "In 2 Problem formulation ‣ Equilibrium investment under dynamic preference uncertainty"))-([2.2](https://arxiv.org/html/2512.21149v1#S2.E2 "In 2 Problem formulation ‣ Equilibrium investment under dynamic preference uncertainty"))
   have a unique strong solution denoted by XπX^{\pi}, YY.
2. (b)

   For each point (t,x,y)∈𝒯×𝒳×𝒴(t,x,y)\in\mathcal{T}\times\mathcal{X}\times\mathcal{Y}, we have

   |  |  |  |
   | --- | --- | --- |
   |  | 𝔼t,x,y​[v∘(uγ​(YT))−1​(𝔼t,x,y,y¯​[uγ​(YT)​(XTπ)])]<∞.\mathbb{E}\_{t,x,y}\left[v\circ\left(u^{\gamma(Y\_{T})}\right)^{-1}\left(\mathbb{E}\_{t,x,y,\overline{y}}\left[u^{\gamma(Y\_{T})}(X^{\pi}\_{T})\right]\right)\right]<\infty\,. |  |
3. (c)

   π\pi is continuous in t,x,yt,x,y.

The set of admissible strategies is denoted by 𝓐\bm{\mathcal{A}}.

Because the objective functional ([2.3](https://arxiv.org/html/2512.21149v1#S2.E3 "In 2 Problem formulation ‣ Equilibrium investment under dynamic preference uncertainty")) is time-inconsistent, one cannot rely on the dynamic programming principle to find optimal controls. Therefore, we seek to determine equilibrium control laws in the sense of the following definition.

###### Definition 2.4 (Equilibrium control law; cf. Def. 15.3 in BjoerkKhapkoMurgoci2021:TICT).

Consider an admissible control law π^\widehat{\pi} (informally viewed as a candidate equilibrium law). Choose an arbitrary π∈𝓐\pi\in\bm{\mathcal{A}} and a fixed real number δ>0\delta>0. Fix moreover an arbitrary initial point (t,x,y)(t,x,y) and define the control law πδ\pi\_{\delta} by

|  |  |  |
| --- | --- | --- |
|  | πδ​(s,x,y)={π​(s,x,y)for​(s,x,y)∈[t,t+δ)×𝒳×𝒴,π^​(s,x,y)for​(s,x,y)∈[t+δ,T)×𝒳×𝒴.\displaystyle\pi\_{\delta}(s,x,y)=\begin{cases}\pi(s,x,y)&\mbox{for}\,\,(s,x,y)\in[t,t+\delta)\times\mathcal{X}\times\mathcal{Y}\,,\\ \widehat{\pi}(s,x,y)&\mbox{for}\,\,(s,x,y)\in[t+\delta,T)\times\mathcal{X}\times\mathcal{Y}\,.\end{cases} |  |

If, for all π∈𝓐\pi\in\bm{\mathcal{A}}, the following condition holds,

|  |  |  |
| --- | --- | --- |
|  | liminfδ→0Jπ^​(t,x,y)−Jπδ​(t,x,y)δ≥0,\displaystyle\underset{\delta\to 0}{\lim\inf}\quad\frac{J^{\hat{\pi}}(t,x,y)-J^{\pi\_{\delta}}(t,x,y)}{\delta}\geq 0\,, |  |

then π^\widehat{\pi} is referred to as an equilibrium control law.

For an equilibrium control law π^\widehat{\pi}, we define the equilibrium value function V^\widehat{V} by

|  |  |  |
| --- | --- | --- |
|  | V^​(t,x,y):=Jπ^​(t,x,y).\widehat{V}\left(t,x,y\right):=J^{\widehat{\pi}}\left(t,x,y\right)\,. |  |

## 3 Derivation of equilibrium controls

This section develops the framework needed to characterize equilibrium investment policies. We begin with several preliminary definitions and then describe the dynamics of the state variables under the conditional measure that arises from our preference model. Building on these ingredients, we present a heuristic derivation of the eHJB governing equilibrium behavior, followed by a rigorous verification argument. We conclude the section by situating our eHJB within the broader literature, comparing its structure to existing formulations and highlighting key differences.

### 3.1 Preliminary definitions and state process dynamics under conditional measures

Define, for any y¯∈𝒴\overline{y}\in\mathcal{Y},

|  |  |  |  |
| --- | --- | --- | --- |
|  | φy¯:=v∘(uγ​(y¯))−1,\varphi^{\overline{y}}:=v\circ\left(u^{\gamma(\overline{y})}\right)^{-1}\,, |  | (3.1) |

which is twice continuously differentiable as the composition of two functions that are twice continuously differentiable.

Let fYT​(y¯;t,y)f\_{Y\_{T}}(\overline{y};t,y) and FYT​(y¯;t,y)F\_{Y\_{T}}(\overline{y};t,y) denote, respectively, the conditional probability density function (PDF) and the conditional cumulative distribution function (CDF) of YTY\_{T} given Yt=yY\_{t}=y. Using this notation, we can rewrite the reward functional ([2.3](https://arxiv.org/html/2512.21149v1#S2.E3 "In 2 Problem formulation ‣ Equilibrium investment under dynamic preference uncertainty")) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jπ​(t,x,y)=𝔼t,x,y​[v∘(uγ​(YT))−1​(𝔼t,x,y,y¯​[uγ​(YT)​(XTπ)])]=∫𝒴φy¯​(𝔼t,x,y,y¯​[uγ​(y¯)​(XTπ)])​fYT​(y¯;t,y)​𝑑y¯=∫𝒴φy¯​(𝔼t,x,y,y¯​[uγ​(y¯)​(XTπ)])​𝑑FYT​(y¯;t,y).\begin{split}J^{\pi}(t,x,y)&=\mathbb{E}\_{t,x,y}\left[v\circ\left(u^{\gamma(Y\_{T})}\right)^{-1}\Big(\mathbb{E}\_{t,x,y,\overline{y}}\left[u^{\gamma(Y\_{T})}(X^{\pi}\_{T})\right]\Big)\right]\,\\[5.69046pt] &=\int\_{\mathcal{Y}}\varphi^{\overline{y}}\Big(\mathbb{E}\_{t,x,y,\overline{y}}\left[u^{\gamma(\overline{y})}\left(X^{\pi}\_{T}\right)\right]\Big)f\_{Y\_{T}}(\overline{y};t,y)\,d\overline{y}\\ &=\int\_{\mathcal{Y}}\varphi^{\overline{y}}\Big(\mathbb{E}\_{t,x,y,\overline{y}}\left[u^{\gamma(\overline{y})}\left(X^{\pi}\_{T}\right)\right]\Big)\,dF\_{Y\_{T}}(\overline{y};t,y).\end{split} |  | (3.2) |

The state process (Xπ,Y)\left(X^{\pi},Y\right), conditional on Xtπ=xX^{\pi}\_{t}=x and Yt=yY\_{t}=y, satisfies the same SDEs ([2.1](https://arxiv.org/html/2512.21149v1#S2.E1 "In 2 Problem formulation ‣ Equilibrium investment under dynamic preference uncertainty"))-([2.2](https://arxiv.org/html/2512.21149v1#S2.E2 "In 2 Problem formulation ‣ Equilibrium investment under dynamic preference uncertainty")) with the initial condition (x,y)(x,y). In particular, under ℙt,x,y\mathbb{P}\_{t,x,y}, we have:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Xtπ\displaystyle dX^{\pi}\_{t} | =Xtπ​(r+π​(t)​(μS−r))​d​t+Xtπ​π​(t)​σS​(ρ​d​Bt1+1−ρ2​d​Bt2),\displaystyle=X^{\pi}\_{t}(r+\pi(t)(\mu\_{S}-r))dt+X^{\pi}\_{t}\pi(t)\sigma\_{S}\left(\rho dB^{1}\_{t}+\sqrt{1-\rho^{2}}dB^{2}\_{t}\right), |  | (3.3) |
|  | d​Ys\displaystyle dY\_{s} | =μY​(s,Ys)​d​s+σY​(s,Ys)​d​Bs1,\displaystyle=\mu\_{Y}(s,Y\_{s})ds+\sigma\_{Y}(s,Y\_{s})dB^{1}\_{s}, |  |

with Xt=xX\_{t}=x, Yt=yY\_{t}=y, σS>0\sigma\_{S}>0, σY>0\sigma\_{Y}>0, and d​Bs1​d​Bs2=0dB^{1}\_{s}dB^{2}\_{s}=0 for every s∈[t,T]s\in[t,T], i.e., B1B^{1} and B2B^{2} are still independent Brownian motions under ℙt,x,y\mathbb{P}\_{t,x,y}.

Because the objective ([3.2](https://arxiv.org/html/2512.21149v1#S3.E2 "In 3.1 Preliminary definitions and state process dynamics under conditional measures ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")) involves the conditional expectation 𝔼t,x,y,y¯​[⋅]\mathbb{E}\_{t,x,y,\overline{y}}[\,\cdot\,], we need the dynamics of (Xπ,Y)\left(X^{\pi},Y\right) under the conditional measure ℙt,x,y,y¯\mathbb{P}\_{t,x,y,\overline{y}}. For this, we rely on a change-of-measure argument based on the transition density of YY; see DesmettreLeobacherRogers2021ChangeOfDrift for the one-dimensional diffusion case.

Let pY​(s,y;t,y¯)p\_{Y}(s,y;t,\overline{y}) denote the transition density function of YY, i.e. the density of Yt=y¯Y\_{t}=\overline{y} given Ys=yY\_{s}=y, for 0≤s≤t≤T0\leq s\leq t\leq T. The conditional density fYTf\_{Y\_{T}} is obtained as the special case

|  |  |  |
| --- | --- | --- |
|  | fYT​(y¯;t,y)=pY​(t,y;T,y¯).f\_{Y\_{T}}(\overline{y};t,y)=p\_{Y}(t,y;T,\overline{y}). |  |

It is convenient to keep both notations: we interpret fYT​(y¯;t,y)f\_{Y\_{T}}(\overline{y};t,y) as a function of y¯∈𝒴\overline{y}\in\mathcal{Y} for fixed (t,y)∈𝒯×𝒴(t,y)\in\mathcal{T}\times\mathcal{Y}, whereas pY​(s,y;t,y¯)p\_{Y}(s,y;t,\overline{y}) will be treated as a function of (s,y)∈𝒯×𝒴(s,y)\in\mathcal{T}\times\mathcal{Y} for fixed (t,y¯)∈[s,T]×𝒴(t,\overline{y})\in[s,T]\times\mathcal{Y}. Denote by ∂ypY​(s,y;T,y¯)\partial\_{y}p\_{Y}(s,y;T,\overline{y}) the partial derivative of pY​(s,y;T,y¯)p\_{Y}(s,y;T,\overline{y}) with respect to yy. We then have the following result.

###### Lemma 3.1.

Let B¯1\overline{B}^{1} and B¯2\overline{B}^{2} be two standard
motions under ℙt,x,y,y¯\mathbb{P}\_{t,x,y,\overline{y}}. Then, under ℙt,x,y,y¯\mathbb{P}\_{t,x,y,\overline{y}}, for s∈[t,T)s\in[t,T):

* •

  The wealth process XπX^{\pi} evolves as

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | d​Xsπ\displaystyle dX^{\pi}\_{s} | =Xsπ​(r+π​(s)​(μS−r)+π​(s)​σS​ρ​σY​(s,Ys)​∂yln⁡(pY​(s,Ys;T,y¯)))​d​s\displaystyle=X^{\pi}\_{s}\left(r+\pi(s)(\mu\_{S}-r)+\pi(s)\sigma\_{S}\rho\sigma\_{Y}(s,Y\_{s})\partial\_{y}\ln\big(p\_{Y}(s,Y\_{s};{T},\overline{y})\big)\right)ds |  | (3.4) |
  |  |  | +Xsπ​π​(s)​σS​(ρ​d​B¯s1+1−ρ2​d​B¯s2),\displaystyle\quad+X^{\pi}\_{s}\pi(s)\sigma\_{S}\left(\rho d\overline{B}^{1}\_{s}+\sqrt{1-\rho^{2}}d\overline{B}^{2}\_{s}\right), |  |

  with Xtπ=xX^{\pi}\_{t}=x and XTπ=limt→TXtπX^{\pi}\_{T}=\lim\_{t\to T}X^{\pi}\_{t}.
* •

  The process YY evolves as

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  |  | d​Ys\displaystyle d{Y}\_{s} | =(μY​(s,Ys)+σY2​(s,Ys)​∂yln⁡(pY​(s,Ys;T,y¯)))​d​s+σY​(s,Ys)​d​B¯s1,\displaystyle=\left(\mu\_{Y}(s,Y\_{s})+\sigma\_{Y}^{2}(s,Y\_{s})\partial\_{y}\ln\big(p\_{Y}(s,{Y}\_{s};{T},\overline{y})\right)\big)ds+\sigma\_{Y}\left(s,Y\_{s}\right)d\overline{B}^{1}\_{s}, |  | (3.5) |

  with Yt=yY\_{t}=y and YT=y¯Y\_{T}=\overline{y}.

Proof. See Appendix [A.1](https://arxiv.org/html/2512.21149v1#A1.SS1 "A.1 Proof of Lemma 3.1 ‣ Appendix A Proofs ‣ Equilibrium investment under dynamic preference uncertainty").

For later use, it is convenient to introduce compact notation for the drift and diffusion coefficients under the conditional measure ℙt,x,y,y¯\mathbb{P}\_{t,x,y,\overline{y}}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ¯X​(t,x,π)\displaystyle\overline{\mu}\_{X}(t,x,\pi) | :=x​[r+π​(μS−r)+π​σS​ρ​σY​(t,y)​∂yln⁡pY​(t,y;T,y¯)],\displaystyle:=x\Bigl[r+\pi(\mu\_{S}-r)+\pi\sigma\_{S}\rho\,\sigma\_{Y}(t,y)\,\partial\_{y}\ln p\_{Y}(t,y;T,\overline{y})\Bigr], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | σ¯X​(t,x,π)\displaystyle\overline{\sigma}\_{X}(t,x,\pi) | :=(σ¯X,1​(t,x,π),σ¯X,2​(t,x,π)):=(x​π​σS​ρ,x​π​σS​1−ρ2),\displaystyle:=\left(\overline{\sigma}\_{X,1}(t,x,\pi),\overline{\sigma}\_{X,2}(t,x,\pi)\right):=\Bigl(x\pi\sigma\_{S}\rho,\;x\pi\sigma\_{S}\sqrt{1-\rho^{2}}\Bigr), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | μ¯Y​(t,y)\displaystyle\overline{\mu}\_{Y}(t,y) | :=μY​(t,y)+σY2​(t,y)​∂yln⁡pY​(t,y;T,y¯),\displaystyle:=\mu\_{Y}(t,y)+\sigma\_{Y}^{2}(t,y)\,\partial\_{y}\ln p\_{Y}(t,y;T,\overline{y}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | σ¯Y​(t,y)\displaystyle\overline{\sigma}\_{Y}(t,y) | :=σY​(t,y).\displaystyle:=\sigma\_{Y}(t,y). |  |

To express the eHJB in compact form, we now introduce the controlled differential operators associated with the dynamics under ℙt,x,y\mathbb{P}\_{t,x,y} and ℙt,x,y,y¯\mathbb{P}\_{t,x,y,\overline{y}}.

###### Definition 3.2.

Let XπX^{\pi} and YY be given by ([2.1](https://arxiv.org/html/2512.21149v1#S2.E1 "In 2 Problem formulation ‣ Equilibrium investment under dynamic preference uncertainty")) and ([2.2](https://arxiv.org/html/2512.21149v1#S2.E2 "In 2 Problem formulation ‣ Equilibrium investment under dynamic preference uncertainty")), respectively, and let ξ:𝒯×𝒳×𝒴↦ℝ\xi:\mathcal{T}\times\mathcal{X}\times\mathcal{Y}\mapsto\mathbb{R} be a map such that ξ∈\textgoth​C1,2,2​(𝒯×𝒳×𝒴)\xi\in\textgoth{C}^{1,2,2}\left(\mathcal{T}\times\mathcal{X}\times\mathcal{Y}\right).
(Given positive integers p,q,rp,q,r, we write \textgoth​Cp,q,r​(𝔻)\textgoth{C}^{p,q,r}(\mathbb{D}) for the space of functions on the domain 𝔻\mathbb{D} that are continuously differentiable up to order p,q,p,q, and rr in the respective arguments.)

For any admissible π∈𝓐\pi\in\bm{\mathcal{A}}, the controlled differential operator 𝒟π\mathcal{D}^{\pi} under ℙt,x,y\mathbb{P}\_{t,x,y} is defined as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒟π​ξ​(t,x,y)\displaystyle\mathcal{D}^{\pi}\xi(t,x,y) | =∂tξ​(t,x,y)+μX​(t,x,π​(t,x,y))​∂xξ​(t,x,y)+μY​(t,y)​∂yξ​(t,x,y)\displaystyle=\partial\_{t}\xi(t,x,y)+\mu\_{X}(t,x,\pi(t,x,y))\partial\_{x}\xi(t,x,y)+\mu\_{Y}(t,y)\partial\_{y}\xi(t,x,y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +12​‖σX​(t,x,y)‖2​∂x​xξ​(t,x,y)+12​(σY​(t,y))2​∂y​yξ​(t,x,y)\displaystyle\quad+\dfrac{1}{2}\left\lVert\sigma\_{X}(t,x,y)\right\rVert^{2}\partial\_{xx}\xi(t,x,y)+\dfrac{1}{2}\left(\sigma\_{Y}(t,y)\right)^{2}\partial\_{yy}\xi(t,x,y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +σX,1​(t,x,π​(t,x,y))​σY​(t,y)​∂x​yξ​(t,x,y),\displaystyle\quad+\sigma\_{X,1}(t,x,\pi(t,x,y))\sigma\_{Y}(t,y)\partial\_{xy}\xi(t,x,y), |  |

where ∂x,∂y,∂x​x,∂x​y,∂y​y\partial\_{x},\partial\_{y},\partial\_{xx},\partial\_{xy},\partial\_{yy} denote the corresponding partial derivatives.

Analogously, we define the controlled differential operator 𝒟¯π\overline{\mathcal{D}}^{\pi} under ℙt,x,y,y¯\mathbb{P}\_{t,x,y,\overline{y}} as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒟¯π​ξ​(t,x,y)\displaystyle\overline{\mathcal{D}}^{\pi}\xi(t,x,y) | =∂tξ​(t,x,y)+μ¯X​(t,x,π​(t,x,y))​∂xξ​(t,x,y)+μ¯Y​(t,y)​∂yξ​(t,x,y)\displaystyle=\partial\_{t}\xi(t,x,y)+\overline{\mu}\_{X}(t,x,\pi(t,x,y))\partial\_{x}\xi(t,x,y)+\overline{\mu}\_{Y}(t,y)\partial\_{y}\xi(t,x,y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +12​‖σ¯X​(t,x,y)‖2​∂x​xξ​(t,x,y)+12​(σ¯Y​(t,y))2​∂y​yξ​(t,x,y)\displaystyle\quad+\dfrac{1}{2}\left\lVert\overline{\sigma}\_{X}(t,x,y)\right\rVert^{2}\partial\_{xx}\xi(t,x,y)+\dfrac{1}{2}\left(\overline{\sigma}\_{Y}(t,y)\right)^{2}\partial\_{yy}\xi(t,x,y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +σ¯X,1​(t,x,π​(t,x,y))​σ¯Y​(t,y)​∂x​yξ​(t,x,y).\displaystyle\quad+\overline{\sigma}\_{X,1}(t,x,\pi(t,x,y))\overline{\sigma}\_{Y}(t,y)\partial\_{xy}\xi(t,x,y). |  |

For a constant control π\pi, the operators are defined in the same way.

### 3.2 Heuristic derivation of the eHJB

The reward functional ([3.2](https://arxiv.org/html/2512.21149v1#S3.E2 "In 3.1 Preliminary definitions and state process dynamics under conditional measures ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")) does not fall directly within the general framework of BjoerkKhapkoMurgoci2021:TICT (henceforth, BKM21), Section 15.5, whose most general objective (in our notation) when the dimensionality of the state process is n=2n=2 has the form

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | 𝔼t,x,y​[∫tTH​(t,x,y,s,Xsπ,Ys,π​(s,Xsπ,Ys))​𝑑s]\displaystyle\mathbb{E}\_{t,x,y}\Bigg[\int\_{t}^{T}H(t,x,y,s,X^{\pi}\_{s},Y\_{s},\pi(s,X^{\pi}\_{s},Y\_{s}))\,ds\Bigg] |  | (3.6) |
|  |  | +𝔼t,x,y​[F​(t,x,y,XTπ,YT)]+G​(t,x,y,𝔼t,x,y​[XTπ],𝔼t,x,y​[YT]),\displaystyle+\mathbb{E}\_{t,x,y}\Big[F\big(t,x,y,X^{\pi}\_{T},Y\_{T}\big)\Big]+G\Big(t,x,y,\mathbb{E}\_{t,x,y}[X^{\pi}\_{T}],\mathbb{E}\_{t,x,y}[Y\_{T}]\Big), |  |

for possibly nonlinear functions F,G,HF,G,H; cf. Eq. (15.13) therein. (In Section [3.4](https://arxiv.org/html/2512.21149v1#S3.SS4 "3.4 Relation to existing formulations ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty"), we return to this reward functional and discuss the corresponding eHJB.)

Two structural features of our preferences ([3.2](https://arxiv.org/html/2512.21149v1#S3.E2 "In 3.1 Preliminary definitions and state process dynamics under conditional measures ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")) prevent a direct embedding into (LABEL:eq:reward\_functional\_general\_BKM2021):

1. (a)

   the objective involves expectations conditional on a fixed terminal state, YT=y¯Y\_{T}=\overline{y}, inside a nonlinear function of the expectation of the terminal state;
2. (b)

   the nonlinear function of the expectation of terminal state involves a continuum of terms φy¯​(𝔼t,x,y,y¯​[uγ​(y¯)​(XTπ)])\varphi^{\overline{y}}\left(\mathbb{E}\_{t,x,y,\overline{y}}\left[u^{\gamma(\overline{y})}\left(X^{\pi}\_{T}\right)\right]\right), rather than one expectation of terminal state.

In what follows, we then explain how to generalize (LABEL:eq:reward\_functional\_general\_BKM2021) to a form that includes ([3.2](https://arxiv.org/html/2512.21149v1#S3.E2 "In 3.1 Preliminary definitions and state process dynamics under conditional measures ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")). Feature (a) is addressed by using Lemma [3.1](https://arxiv.org/html/2512.21149v1#S3.Thmtheorem1 "Lemma 3.1. ‣ 3.1 Preliminary definitions and state process dynamics under conditional measures ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty"), which describes the dynamics of (Xπ,Y)(X^{\pi},Y) under ℙt,x,y,y¯\mathbb{P}\_{t,x,y,\overline{y}}. Feature (b), on the other hand, requires more work. Specifically, we need to approximate ([3.2](https://arxiv.org/html/2512.21149v1#S3.E2 "In 3.1 Preliminary definitions and state process dynamics under conditional measures ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")) as a finite sum of different GG-terms in (LABEL:eq:reward\_functional\_general\_BKM2021), where we use the label “GG-term” to refer to any nonlinear function of the expectation(s) of function(s) of the terminal value of the state process.

In the simplest case of a sum consisting of just one element, the approximating reward functional resembles (LABEL:eq:reward\_functional\_general\_BKM2021) with F≡0F\equiv 0, H≡0H\equiv 0 and one suitable G≢0G\not\equiv 0, with a minor difference that under the expectation operator there is a function of the terminal value of the state process (instead of just the terminal value of the state process itself). Therefore, for the heuristic derivation of the eHJB for our reward functional, we use the following reward functional as a starting point:

|  |  |  |  |
| --- | --- | --- | --- |
|  | G​(t,x,y,𝔼t,x,y​[XTπ],𝔼t,x,y​[YT]).G\Big(t,x,y,\mathbb{E}\_{t,x,y}[X^{\pi}\_{T}],\mathbb{E}\_{t,x,y}[Y\_{T}]\Big). |  | (3.7) |

As we explain in detail in Section [3.4](https://arxiv.org/html/2512.21149v1#S3.SS4 "3.4 Relation to existing formulations ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty"), the extended system characterizing an equilibrium control for ([3.7](https://arxiv.org/html/2512.21149v1#S3.E7 "In 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")) involves an auxiliary function g​(t,x,y)=(g1​(t,x,y),g2​(t,x,y))g(t,x,y)=(g\_{1}(t,x,y),g\_{2}(t,x,y)), where g1,g2:𝒯×𝒳×𝒴→ℝg\_{1},g\_{2}:\mathcal{T}\times\mathcal{X}\times\mathcal{Y}\rightarrow\mathbb{R}, and uses the following notation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (G⋄g)​(t,x,y):=G​(t,x,y,g1​(t,x,y),g2​(t,x,y)),ℋπ​g​(t,x,y):=Gx~​(t,x,y,g1​(t,x,y),g2​(t,x,y))​𝒟π​g1​(t,x,y)+Gy~​(t,x,y,g1​(t,x,y),g2​(t,x,y))​𝒟π​g2​(t,x,y),𝒟π^​g​(t,x,y):=(𝒟π^​g1​(t,x,y),𝒟π^​g2​(t,x,y)).\begin{split}(G\diamond g)(t,x,y)&:=G(t,x,y,g\_{1}(t,x,y),g\_{2}(t,x,y)),\\[5.69046pt] \mathcal{H}^{\pi}g(t,x,y)&:=G\_{\tilde{x}}(t,x,y,g\_{1}(t,x,y),g\_{2}(t,x,y))\ \mathcal{D}^{\pi}g\_{1}(t,x,y)\\ &\quad+G\_{\tilde{y}}(t,x,y,g\_{1}(t,x,y),g\_{2}(t,x,y))\,\mathcal{D}^{\pi}g\_{2}(t,x,y),\\ \mathcal{D}^{\widehat{\pi}}g(t,x,y)&:=\left(\mathcal{D}^{\widehat{\pi}}g\_{1}(t,x,y),\mathcal{D}^{\widehat{\pi}}g\_{2}(t,x,y)\right).\end{split} |  | (3.8) |

The eHJB is then given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | =supπ∈𝒜​(t,x,y){𝒟π​V​(t,x,y)−𝒟π​(G⋄g)​(t,x,y)+ℋπ​g​(t,x,y)},\displaystyle=\sup\_{\pi\in\mathcal{A}(t,x,y)}\Big\{\mathcal{D}^{\pi}V(t,x,y)-\mathcal{D}^{\pi}(G\diamond g)(t,x,y)+\mathcal{H}^{\pi}g(t,x,y)\Big\}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (0,0)\displaystyle(0,0) | =𝒟π^​g​(t,x,y),\displaystyle=\mathcal{D}^{\widehat{\pi}}g(t,x,y), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(T,x,y)\displaystyle V(T,x,y) | =G​(T,x,y,x,y),\displaystyle=G(T,x,y,x,y), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(T,x,y)\displaystyle g(T,x,y) | =(x,y),\displaystyle=(x,y), |  |

where π^\widehat{\pi} denotes the control law that realizes the supremum in the first equation of the system; for more details, see Section [3.4](https://arxiv.org/html/2512.21149v1#S3.SS4 "3.4 Relation to existing formulations ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty").

As stated in Section 16.3 of BKM21, it is possible to generalize the above eHJB to the case of

|  |  |  |
| --- | --- | --- |
|  | G1​(t,x,y,𝔼t,x,y​[k11​(XTπ)],𝔼t,x,y​[k12​(YT)]),G\_{1}\Big(t,x,y,\mathbb{E}\_{t,x,y}[k\_{1}^{1}(X^{\pi}\_{T})],\mathbb{E}\_{t,x,y}[k\_{1}^{2}(Y\_{T})]\Big), |  |

for some functions k11:𝒳→ℝk\_{1}^{1}:\mathcal{X}\rightarrow\mathbb{R} and k12:𝒴→ℝk\_{1}^{2}:\mathcal{Y}\rightarrow\mathbb{R}, where the superscript refers to the dimension of the state process (Xπ,Y)(X^{\pi},Y) and the subscript refers to the number of expectations of a function of the terminal state process value.

For a one-dimensional state process XπX^{\pi}, another generalization is studied in KrygerNordfangSteffensen2020:MMRO, where the eHJB is established for the case where the GG-term depends on the conditional expectations of two different functions of the terminal state:

|  |  |  |
| --- | --- | --- |
|  | G2​(t,x,𝔼t,x​[k1​(XTπ)],𝔼t,x​[k2​(XTπ)]),G\_{2}\Big(t,x,\mathbb{E}\_{t,x}[k\_{1}(X^{\pi}\_{T})],\mathbb{E}\_{t,x}[k\_{2}(X^{\pi}\_{T})]\Big), |  |

for k1,k2:𝒳→ℝk\_{1},k\_{2}:\mathcal{X}\rightarrow\mathbb{R}.

In Remark 2 of the same paper, it is stated (yet not shown) that one can similarly obtain the eHJB for the case with n>2n>2 different functions ki:𝒳→ℝk\_{i}:\mathcal{X}\rightarrow\mathbb{R}, i=1,…​ni=1,\dots n:

|  |  |  |
| --- | --- | --- |
|  | Gn​(t,x,𝔼t,x​[k1​(XTπ)],…,𝔼t,x​[kn​(XTπ)]).G\_{n}\Big(t,x,\mathbb{E}\_{t,x}[k\_{1}(X^{\pi}\_{T})],\dots,\mathbb{E}\_{t,x}[k\_{n}(X^{\pi}\_{T})]\Big). |  |

The function GnG\_{n} can be interpreted as an nn-term finite aggregator of conditional expectations. Since finite sums provide natural discrete approximations of integrals, the expression above represents a tractable discretization of the continuum aggregation appearing in ([3.2](https://arxiv.org/html/2512.21149v1#S3.E2 "In 3.1 Preliminary definitions and state process dynamics under conditional measures ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")). In our problem, the integral averages certainty equivalents across the entire distribution of future preference states. By choosing the functions kik\_{i} and the structure of GnG\_{n} appropriately, the sequence of discretized problems (Pn)(P\_{n}) can approximate the original problem with continuous aggregation arbitrarily well. This observation allows us to construct the eHJB for our full objective by first analyzing the finite-dimensional case and then passing to the limit.

We proceed in two steps:

1. 1.

   We construct a sequence of auxiliary problems (Pn)(P\_{n}) that approximate the equilibrium investment problem associated with ([3.2](https://arxiv.org/html/2512.21149v1#S3.E2 "In 3.1 Preliminary definitions and state process dynamics under conditional measures ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")). Each problem (Pn)(P\_{n}) replaces the integral aggregation over future preference states by a finite sum, enabling us to heuristically derive the eHJB in the finite-dimensional case (Pn)(P\_{n}).
2. 2.

   We then let n→∞n\to\infty and interpret the integral in ([3.2](https://arxiv.org/html/2512.21149v1#S3.E2 "In 3.1 Preliminary definitions and state process dynamics under conditional measures ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")) as the limit of these discrete approximations. In doing so, we obtain the eHJB for the original problem as the limiting case of the systems associated with (Pn)(P\_{n}).

Step 1: Sequence of approximating problems (Pn)(P\_{n})

Fix an arbitrary point (t,x,y)∈[0,T)×𝒳×𝒴(t,x,y)\in[0,T)\times\mathcal{X}\times\mathcal{Y}. For any n∈ℕn\in\mathbb{N}, let 𝒫𝒴:={y¯0,y¯1,…,y¯n}\mathcal{P}\_{\mathcal{Y}}:=\left\{\overline{y}\_{0},\overline{y}\_{1},\dots,\overline{y}\_{n}\right\} be an arbitrarily chosen partition of 𝒴\mathcal{Y}, with y¯i∈ℝ¯\overline{y}\_{i}\in\overline{\mathbb{R}}\, for every i∈{0,1,…,n}i\in\left\{0,1,\dots,n\right\}, where ℝ¯:=ℝ∪{−∞,∞}\overline{\mathbb{R}}:=\mathbb{R}\cup\left\{-\infty,\infty\right\}. Define Δ​Fi​(t,y):=FYT​(y¯i+1;t,y)−FYT​(y¯i;t,y)\Delta F\_{i}(t,y):=F\_{Y\_{T}}(\overline{y}\_{i+1};t,y)-F\_{Y\_{T}}(\overline{y}\_{i};t,y).
Then, we can approximate the integral as a finite sum as follows:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Jπ​(t,x,y)\displaystyle J^{\pi}(t,x,y) | ≈∑i=1nφy¯i−1​(𝔼t,x,y,y¯i−1​[uγ​(y¯i−1)​(XTπ)])​Δ​Fi−1​(t,y)\displaystyle\approx\sum\limits\_{i=1}^{n}\varphi^{\overline{y}\_{i-1}}\Big(\mathbb{E}\_{t,x,y,\overline{y}\_{i-1}}\left[u^{\gamma(\overline{y}\_{i-1})}\left(X^{\pi}\_{T}\right)\right]\Big)\Delta F\_{i-1}(t,y) |  | (3.9) |
|  |  | =:Gn(t,y,𝔼t,x,y,y¯0[uγ​(y¯0)(XTπ)],…,𝔼t,x,y,y¯n−1[uγ​(y¯n−1)(XTπ)]),\displaystyle=:G\_{n}\Big(t,y,\mathbb{E}\_{t,x,y,\overline{y}\_{0}}\left[u^{\gamma(\overline{y}\_{0})}\left(X^{\pi}\_{T}\right)\right],\dots,\mathbb{E}\_{t,x,y,\overline{y}\_{n-1}}\left[u^{\gamma(\overline{y}\_{n-1})}\left(X^{\pi}\_{T}\right)\right]\Big), |  |

where GnG\_{n} above does not have xx as its argument, though the derivation below can easily be extended to this case.

We define the nn-th approximating problem (Pn)(P\_{n}) as the one for which the reward functional is given by

|  |  |  |
| --- | --- | --- |
|  | Jnπ​(t,x,y):=Gn​(t,y,𝔼t,x,y,y¯0​[uγ​(y¯0)​(XTπ)],…,𝔼t,x,y,y¯n−1​[uγ​(y¯n−1)​(XTπ)]).J^{\pi}\_{n}(t,x,y):=G\_{n}\Big(t,y,\mathbb{E}\_{t,x,y,\overline{y}\_{0}}\left[u^{\gamma(\overline{y}\_{0})}\left(X^{\pi}\_{T}\right)\right],\dots,\mathbb{E}\_{t,x,y,\overline{y}\_{n-1}}\left[u^{\gamma(\overline{y}\_{n-1})}\left(X^{\pi}\_{T}\right)\right]\Big). |  |

Denote by π^n\widehat{\pi}\_{n} an equilibrium investment strategy for (Pn)(P\_{n}) and by V^n​(t,x,y)\widehat{V}\_{n}(t,x,y) the respective equilibrium value function.

Let us derive the eHJB for the simplest case of (P1)(P\_{1}). Choose an arbitrary partition 𝒫𝒴={y¯0,y¯1}\mathcal{P}\_{\mathcal{Y}}=\left\{\overline{y}\_{0},\overline{y}\_{1}\right\}, i.e., y¯0\overline{y}\_{0} is such that FYT​(y¯0;t,y)=0F\_{Y\_{T}}(\overline{y}\_{0};t,y)=0 and y¯1\overline{y}\_{1} is such that FYT​(y¯1;t,y)=1F\_{Y\_{T}}(\overline{y}\_{1};t,y)=1. Then, Δ​F0​(t,y)=1\Delta F\_{0}(t,y)=1 and (P1)(P\_{1}) has the reward functional

|  |  |  |  |
| --- | --- | --- | --- |
|  | J1π​(t,x,y)=φy¯0​(𝔼t,x,y,y¯0​[uγ​(y¯0)​(XTπ)])​Δ​F0​(t,y)=G1​(t,y,𝔼t,x,y,y¯0​[uγ​(y¯0)​(XTπ)]).\begin{split}J^{\pi}\_{1}(t,x,y)&=\varphi^{\overline{y}\_{0}}\left(\mathbb{E}\_{t,x,y,\overline{y}\_{0}}\left[u^{\gamma(\overline{y}\_{0})}\left(X^{\pi}\_{T}\right)\right]\right)\Delta F\_{0}(t,y)\\ &=G\_{1}\left(t,y,\mathbb{E}\_{t,x,y,\overline{y}\_{0}}\left[u^{\gamma(\overline{y}\_{0})}\left(X^{\pi}\_{T}\right)\right]\right).\end{split} |  | (3.10) |

Comparing ([3.10](https://arxiv.org/html/2512.21149v1#S3.E10 "In 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")) with ([3.7](https://arxiv.org/html/2512.21149v1#S3.E7 "In 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")), we observe that the two formulations are nearly identical, with only two conceptual differences. First, the appearance of the nonlinear function uγ​(y¯0)u^{\gamma(\overline{y}\_{0})} inside the expectation, which poses no structural difficulty; as noted in Section 16.3 of BKM21 and in KrygerNordfangSteffensen2020:MMRO, such a modification can be incorporated simply by adjusting the terminal condition for the auxiliary function in the extended HJB system. Second, because the expectation in ([3.7](https://arxiv.org/html/2512.21149v1#S3.E7 "In 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")) is also conditional on YT=y¯Y\_{T}=\overline{y}, the relevant state dynamics –and hence the differential operator appearing in the HJB– must be taken under the conditional measure ℙt,x,y,y¯\mathbb{P}\_{t,x,y,\overline{y}} rather than ℙt,x,y\mathbb{P}\_{t,x,y}. Apart from this change of measure, the overall structure remains fully aligned with the framework of BKM21. (For completeness, we note that G1G\_{1} in ([3.10](https://arxiv.org/html/2512.21149v1#S3.E10 "In 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")) does not depend on xx and the conditional expectation of YTY\_{T}, in contrast to ([3.7](https://arxiv.org/html/2512.21149v1#S3.E7 "In 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")). If G1G\_{1} were to explicitly depend on these two objects, the arguments of this section could easily be adjusted to account for such dependence.)

Building on these observations, we now derive the eHJB for (P1)(P\_{1}). We begin by introducing the following notation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (G1⋄g1y¯0)​(t,x,y)\displaystyle\left(G\_{1}\diamond g\_{1}^{\overline{y}\_{0}}\right)(t,x,y) | :=G1​(t,y,g1y¯0​(t,x,y))=φy¯0​(g1y¯0​(t,x,y))​Δ​F0​(t,y),\displaystyle:=G\_{1}\big(t,y,g\_{1}^{\overline{y}\_{0}}(t,x,y)\big)=\varphi^{\overline{y}\_{0}}\left(g\_{1}^{\overline{y}\_{0}}(t,x,y)\right)\Delta F\_{0}(t,y), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℋ¯1π​g1y¯0​(t,x,y)\displaystyle\overline{\mathcal{H}}^{\pi}\_{1}g\_{1}^{\overline{y}\_{0}}(t,x,y) | :=∂z1G1​(t,y,g1y¯0​(t,x,y))​𝒟¯π​g1y¯0​(t,x,y),\displaystyle:=\partial\_{z\_{1}}G\_{1}\big(t,y,g\_{1}^{\overline{y}\_{0}}(t,x,y)\big)\,\overline{\mathcal{D}}^{\pi}g\_{1}^{\overline{y}\_{0}}(t,x,y), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(φy¯0)′​(g1y¯0​(t,x,y))​𝒟¯π​g1y¯0​(t,x,y)​Δ​F0​(t,y).\displaystyle=\left(\varphi^{\overline{y}\_{0}}\right)^{\prime}\left(g\_{1}^{\overline{y}\_{0}}(t,x,y)\right)\,\overline{\mathcal{D}}^{\pi}g\_{1}^{\overline{y}\_{0}}(t,x,y)\,\Delta F\_{0}(t,y). |  |

With this notation in place, the eHJB for (P1)(P\_{1}) takes the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=supπ∈𝒜​(t,x,y){𝒟π​V1​(t,x,y)−𝒟π​(G1⋄g1y¯0)​(t,x,y)+ℋ¯1π​g1y¯0​(t,x,y)},0=𝒟¯π^1​g1y¯0​(t,x,y),V1​(T,x,y)=v​(x),g1y¯0​(T,x,y)=uγ​(y¯0)​(x),\begin{split}0&=\sup\_{\pi\in\mathcal{A}(t,x,y)}\Big\{\mathcal{D}^{\pi}V\_{1}(t,x,y)-\mathcal{D}^{\pi}\left(G\_{1}\diamond g\_{1}^{\overline{y}\_{0}}\right)(t,x,y)+\overline{\mathcal{H}}^{\pi}\_{1}g\_{1}^{\overline{y}\_{0}}(t,x,y)\Big\},\\[5.69046pt] 0&=\overline{\mathcal{D}}^{\widehat{\pi}\_{1}}g\_{1}^{\overline{y}\_{0}}(t,x,y),\\[5.69046pt] V\_{1}(T,x,y)&=v(x),\\ g\_{1}^{\overline{y}\_{0}}(T,x,y)&=u^{\gamma(\overline{y}\_{0})}(x),\end{split} |  | (3.11) |

where π^1\widehat{\pi}\_{1} realizes the supremum in the first equation of ([3.11](https://arxiv.org/html/2512.21149v1#S3.E11 "In 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")). A slight modification of Theorem 15.2 in BKM21 verifies that, under certain regularity conditions, π^1\widehat{\pi}\_{1} solving the above extended system is indeed an equilibrium control for (P1)(P\_{1}).

Applying similar heuristic reasoning as in Section 15.3.1 of BKM21 to the problem (Pn)(P\_{n}), whose reward functional is given by ([3.9](https://arxiv.org/html/2512.21149v1#S3.E9 "In 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")), we obtain the natural extension of the system derived for (P1)(P\_{1}). To express this compactly, we introduce the notation

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Gn⋄(g1y¯0,…,gny¯n−1))​(t,x,y)\displaystyle\left(G\_{n}\diamond\left(g\_{1}^{\overline{y}\_{0}},\dots,g\_{n}^{\overline{y}\_{n-1}}\right)\right)\left(t,x,y\right) | :=Gn​(t,y,g1y¯0​(t,x,y),…,gny¯n−1​(t,x,y))\displaystyle:=G\_{n}\left(t,y,g^{\overline{y}\_{0}}\_{1}\left(t,x,y\right),\dots,g^{\overline{y}\_{n-1}}\_{n}\left(t,x,y\right)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑i=1nφy¯i−1(giy¯i−1(t,x,y)))ΔFi−1(t,y),\displaystyle=\sum\limits\_{i=1}^{n}\varphi^{\overline{y}\_{i-1}}\left(g\_{i}^{\overline{y}\_{i-1}}(t,x,y))\right)\Delta F\_{i-1}(t,y), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℋ¯nπ​((giy¯i−1)i=1,…,n)​(t,x,y)\displaystyle\overline{\mathcal{H}}^{\pi}\_{n}\left(\left(g\_{i}^{\overline{y}\_{i-1}}\right)\_{i=1,\dots,n}\right)(t,x,y) | :=∑i=1n(φy¯i−1)′(giy¯i−1(t,x,y)))\displaystyle:=\sum\limits\_{i=1}^{n}\left(\varphi^{\overline{y}\_{i-1}}\right)^{\prime}\left(g\_{i}^{\overline{y}\_{i-1}}(t,x,y))\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×𝒟¯π​giy¯i−1​(t,x,y)​Δ​Fi−1​(t,y).\displaystyle\qquad\times\overline{\mathcal{D}}^{\pi}g\_{i}^{\overline{y}\_{i-1}}(t,x,y)\,\Delta F\_{i-1}(t,y). |  |

These expressions parallel exactly the one-component case, except that each discrete preference scenario contributes its own auxiliary function giy¯i−1g\_{i}^{\overline{y}\_{i-1}} and sensitivity term weighted by the corresponding probability mass Δ​Fi−1​(t,y)\Delta F\_{i-1}(t,y).

With this notation in place, the eHJB for (Pn)(P\_{n}) takes the form

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0\displaystyle 0 | =supπ∈𝒜​(t,x,y){𝒟πVn(t,x,y)−𝒟π(Gn⋄(g1y¯0,…,gny¯n−1))(t,x,y)\displaystyle=\sup\_{\pi\in\mathcal{A}(t,x,y)}\Bigg\{\mathcal{D}^{\pi}V\_{n}(t,x,y)-\mathcal{D}^{\pi}\left(G\_{n}\diamond\left(g\_{1}^{\overline{y}\_{0}},\dots,g\_{n}^{\overline{y}\_{n-1}}\right)\right)\left(t,x,y\right)\Bigg. |  | (3.12) |
|  |  | +ℋ¯nπ((giy¯i−1)i=1,…,n)(t,x,y)},\displaystyle\qquad\qquad\qquad\Bigg.+\overline{\mathcal{H}}^{\pi}\_{n}\left(\left(g\_{i}^{\overline{y}\_{i-1}}\right)\_{i=1,\dots,n}\right)(t,x,y)\Bigg\}, |  |
|  | 0\displaystyle 0 | =𝒟¯π^n​giy¯i−1​(t,x,y),i∈{1,…,n},\displaystyle=\overline{\mathcal{D}}^{\widehat{\pi}\_{n}}g\_{i}^{\overline{y}\_{i-1}}(t,x,y),\qquad i\in\left\{1,\dots,n\right\}, |  |
|  | Vn​(T,x,y)\displaystyle V\_{n}(T,x,y) | =v​(x),\displaystyle=v(x), |  |
|  | giy¯i−1​(T,x,y)\displaystyle g\_{i}^{\overline{y}\_{i-1}}(T,x,y) | =uγ​(y¯i−1)​(x),i∈{1,…,n},\displaystyle=u^{\gamma(\overline{y}\_{i-1})}(x),\,\qquad i\in\left\{1,\dots,n\right\}, |  |

where π^n\widehat{\pi}\_{n} realizes the supremum in the first equation of ([3.12](https://arxiv.org/html/2512.21149v1#S3.E12 "In 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")). Once more, an appropriate adaptation of the verification argument in BKM21 shows that, under suitable smoothness and integrability conditions, the control π^n\widehat{\pi}\_{n} obtained from this system constitutes an equilibrium control for (Pn)(P\_{n}).

Step 2: eHJB for the limiting case

To obtain the eHJB associated with the original objective functional ([3.2](https://arxiv.org/html/2512.21149v1#S3.E2 "In 3.1 Preliminary definitions and state process dynamics under conditional measures ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")), we now pass from the discrete problems (Pn)(P\_{n}) to their continuous counterpart. This motivates introducing the limiting objects

|  |  |  |  |
| --- | --- | --- | --- |
|  | G∞​(t,x,y)\displaystyle G\_{\infty}(t,x,y) | :=limn→∞(Gn⋄(g1y¯0,…,gny¯n−1))​(t,x,y)\displaystyle:=\lim\_{n\to\infty}\left(G\_{n}\diamond\left(g\_{1}^{\overline{y}\_{0}},\dots,g\_{n}^{\overline{y}\_{n-1}}\right)\right)\left(t,x,y\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫𝒴φy¯​(gy¯​(t,x,y))​𝑑FYT​(y¯;t,y),\displaystyle=\int\_{\mathcal{Y}}\varphi^{\overline{y}}\left(g^{\overline{y}}\left(t,x,y\right)\right)dF\_{Y\_{T}}(\overline{y};t,y), |  | (3.13) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℋ¯π​((gy¯)y¯∈𝒴)​(t,x,y)\displaystyle\overline{\mathcal{H}}^{\pi}\left(\left(g^{\overline{y}}\right)\_{\overline{y}\in\mathcal{Y}}\right)(t,x,y) | :=limn→∞ℋ¯nπ​((giy¯i−1)i=1,…,n)​(t,x,y)\displaystyle:=\lim\_{n\to\infty}\overline{\mathcal{H}}^{\pi}\_{n}\left(\left(g\_{i}^{\overline{y}\_{i-1}}\right)\_{i=1,\dots,n}\right)(t,x,y) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫𝒴(φy¯)′​(gy¯​(t,x,y))​𝒟¯π​gy¯​(t,x,y)​𝑑FYT​(y¯;t,y).\displaystyle=\int\_{\mathcal{Y}}\left(\varphi^{\overline{y}}\right)^{\prime}\left(g^{\overline{y}}\left(t,x,y\right)\right)\,\overline{\mathcal{D}}^{\pi}g^{\overline{y}}\left(t,x,y\right)\,dF\_{Y\_{T}}(\overline{y};t,y). |  | (3.14) |

We are now equipped to write down the eHJB characterizing an equilibrium control for the original, infinite-dimensional aggregation problem.

#### The extended HJB system.

The system consists of the following coupled relations:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0\displaystyle 0 | =supπ∈𝒜​(t,x,y){𝒟π​V​(t,x,y)−𝒟π​G∞​(t,x,y)+ℋ¯π​((gy¯)y¯∈𝒴)​(t,x,y)},\displaystyle=\sup\_{\pi\in\mathcal{A}(t,x,y)}\Bigg\{\mathcal{D}^{\pi}V(t,x,y)-\mathcal{D}^{\pi}G\_{\infty}(t,x,y)+\overline{\mathcal{H}}^{\pi}\left(\left(g^{\overline{y}}\right)\_{\overline{y}\in\mathcal{Y}}\right)(t,x,y)\Bigg\}, |  | (S​1S1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0\displaystyle 0 | =𝒟¯π^​gy¯​(t,x,y),y¯∈𝒴,\displaystyle=\overline{\mathcal{D}}^{\widehat{\pi}}g^{\overline{y}}\left(t,x,y\right),\qquad\bar{y}\in\mathcal{Y}, |  | (S​2S2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | v​(x)\displaystyle v(x) | =V​(T,x,y)\displaystyle=V(T,x,y) |  | (S​3S3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | uγ​(y¯)​(x)\displaystyle u^{\gamma(\overline{y})}(x) | =gy¯​(T,x,y),y¯∈𝒴,\displaystyle=g^{\overline{y}}\left(T,x,y\right),\qquad\bar{y}\in\mathcal{Y}, |  | (S​4S4) |

where π^\widehat{\pi} realizes the supremum in ([S​1S1](https://arxiv.org/html/2512.21149v1#S3.Ex25 "In The extended HJB system. ‣ 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")).

The following section provides a verification theorem establishing that a solution of ([S​1S1](https://arxiv.org/html/2512.21149v1#S3.Ex25 "In The extended HJB system. ‣ 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty"))-([S​4S4](https://arxiv.org/html/2512.21149v1#S3.Ex28 "In The extended HJB system. ‣ 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")) indeed yields an equilibrium strategy.

### 3.3 Verification results

For the proof of the main theorem, we will require suitable integrability conditions. These are outlined in the following definition of an ℒ2\mathcal{L}^{2} function space.

###### Definition 3.3.

Fix an arbitrary control π∈𝓐\pi\in\bm{\mathcal{A}}. A function ξ:𝒯×𝒳×𝒴→ℝ\xi:\mathcal{T}\times\mathcal{X}\times\mathcal{Y}\rightarrow\mathbb{R} is said to belong to the space ℒ2​(Xπ,Y)\mathcal{L}^{2}(X^{\pi},Y) if, for any (t,x,y)∈[0,T)×𝒳×𝒴(t,x,y)\in[0,T)\times\mathcal{X}\times\mathcal{Y}, there exists a constant δ¯∈(0,T−t)\bar{\delta}\in(0,T-t) such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼t,x,y[sup0≤δ≤δ¯|∫tt+δ1δ𝒟πξ(s,Xsπ,Ys)ds|\displaystyle\mathbb{E}\_{t,x,y}\Bigg[\sup\_{0\leq\delta\leq\bar{\delta}}\Bigg|\int\_{t}^{t+\delta}\dfrac{1}{\delta}\mathcal{D}^{\pi}\xi(s,X^{\pi}\_{s},Y\_{s})ds\;\Bigg|\Bigg. |  |
|  |  |  |
| --- | --- | --- |
|  | +∫tt+δ¯‖∂xξ​(s,Xsπ,Ys)​σX​(s,Xsπ,π​(s))‖2​𝑑s\displaystyle\hskip 56.9055pt\Bigg.+\int\_{t}^{t+\bar{\delta}}\left\lVert\partial\_{x}\xi(s,X^{\pi}\_{s},Y\_{s})\sigma\_{X}\left(s,X^{\pi}\_{s},\pi(s)\right)\right\rVert^{2}ds\Bigg. |  |
|  |  |  |
| --- | --- | --- |
|  | +∫tt+δ¯(∂yξ(s,Xsπ,Ys)σY(s,Ys))2ds]<∞.\displaystyle\hskip 56.9055pt\Bigg.+\int\_{t}^{t+\bar{\delta}}\Big(\partial\_{y}\xi(s,X^{\pi}\_{s},Y\_{s})\sigma\_{Y}\left(s,Y\_{s}\right)\Big)^{2}ds\Bigg]<\infty. |  |

Analogously, we say that ξ:𝒯×𝒳×𝒴→ℝ\xi:\mathcal{T}\times\mathcal{X}\times\mathcal{Y}\rightarrow\mathbb{R} belongs to the space ℒ¯2​(Xπ,Y)\overline{\mathcal{L}}^{2}(X^{\pi},Y) if, for any (t,x,y)∈[0,T)×𝒳×𝒴(t,x,y)\in[0,T)\times\mathcal{X}\times\mathcal{Y}, there exists a constant δ¯∈(0,T−t)\bar{\delta}\in(0,T-t) such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼t,x,y[sup0≤δ≤δ¯|∫tt+δ1δ𝒟¯πξ(s,Xsπ,Ys)ds|\displaystyle\mathbb{E}\_{t,x,y}\Bigg[\sup\_{0\leq\delta\leq\bar{\delta}}\Bigg|\int\_{t}^{t+\delta}\dfrac{1}{\delta}\overline{\mathcal{D}}^{\pi}\xi(s,X^{\pi}\_{s},Y\_{s})ds\;\Bigg|\Bigg. |  |
|  |  |  |
| --- | --- | --- |
|  | +∫tt+δ¯‖∂xξ​(s,Xsπ,Ys)​σ¯X​(s,Xsπ,π​(s))‖2​𝑑s\displaystyle\hskip 56.9055pt\Bigg.+\int\_{t}^{t+\bar{\delta}}\left\lVert\partial\_{x}\xi(s,X^{\pi}\_{s},Y\_{s})\overline{\sigma}\_{X}\left(s,X^{\pi}\_{s},\pi(s)\right)\right\rVert^{2}ds\Bigg. |  |
|  |  |  |
| --- | --- | --- |
|  | +∫tt+δ¯(∂yξ(s,Xsπ,Ys)σ¯Y(s,Ys))2ds]<∞.\displaystyle\hskip 56.9055pt\Bigg.+\int\_{t}^{t+\bar{\delta}}\Big(\partial\_{y}\xi(s,X^{\pi}\_{s},Y\_{s})\overline{\sigma}\_{Y}\left(s,Y\_{s}\right)\Big)^{2}ds\Bigg]<\infty. |  |

We now introduce a family of auxiliary functions parameterized by y¯∈𝒴\overline{y}\in\mathcal{Y}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | gπ;y¯​(t,x,y)=𝔼t,x,y,y¯​[uγ​(YT)​(XTπ)],\displaystyle g^{\pi;\overline{y}}(t,x,y)=\mathbb{E}\_{t,x,y,\overline{y}}\left[u^{\gamma(Y\_{T})}(X^{\pi}\_{T})\right]\,, |  | (3.15) |

where, by construction, yy and y¯\overline{y} must coincide at t=Tt=T.

In the following lemma, we derive a recursive representation for each function in (gπ;y¯)y¯∈𝒴\left(g^{\pi;\overline{y}}\right)\_{\overline{y}\in\mathcal{Y}} and also characterize it via a PDE. Its proof follows the same steps as Lemma 3.5 in Lindensjoe2019:ORL or Lemma 3.7 in DeGennaroAquino2024equilibrium, with the only difference that we work here under the conditional measure ℙt,x,y,y¯\mathbb{P}\_{t,x,y,\overline{y}} instead of ℙt,x,y\mathbb{P}\_{t,x,y}.

###### Lemma 3.4.

For any admissible control π∈𝓐\pi\in\bm{\mathcal{A}} and y¯∈𝒴\overline{y}\in\mathcal{Y}, for any δ∈(0,T−t]\delta\in(0,T-t], the function gπ;y¯​(t,x,y)g^{\pi;\overline{y}}(t,x,y) satisfies the recursive relation

|  |  |  |
| --- | --- | --- |
|  | gπ;y¯​(t,x,y)=𝔼t,x,y,y¯​[gπ;y¯​(t+δ,Xπ​(t+δ),Y​(t+δ))],g^{\pi;\overline{y}}(t,x,y)=\mathbb{E}\_{t,x,y,\overline{y}}\left[g^{\pi;\overline{y}}\left(t+\delta,X^{\pi}(t+\delta),Y(t+\delta)\right)\right], |  |

and the terminal condition

|  |  |  |
| --- | --- | --- |
|  | gπ;y¯​(T,x,y)=uγ​(y¯)​(x).g^{\pi;\overline{y}}(T,x,y)=u^{\gamma(\overline{y})}(x). |  |

Moreover, if gπ;y¯∈\textgoth​C1,2,1​(𝒯×ℝ×ℝ)∩ℒ¯2​(Xπ,Y)g^{\pi;\overline{y}}\in\textgoth{C}^{1,2,1}\left(\mathcal{T}\times\mathbb{R}\times\mathbb{R}\right)\cap\overline{\mathcal{L}}^{2}\left(X^{\pi},Y\right), then, for t∈[0,T)t\in[0,T), gπ;y¯​(t,x,y)g^{\pi;\overline{y}}(t,x,y) satisfies the PDE

|  |  |  |
| --- | --- | --- |
|  | 𝒟¯π​gπ;y¯​(t,x,y)=0.\overline{\mathcal{D}}^{\pi}g^{\pi;\overline{y}}(t,x,y)=0. |  |

We are now in a position to state our main result.

###### Theorem 3.5 (Verification theorem).

Assume that the functions V​(t,x,y)V(t,x,y), G∞​(t,x,y)G\_{\infty}(t,x,y), and the family (gy¯​(t,x,y))y¯∈𝒴\left(g^{\overline{y}}\left(t,x,y\right)\right)\_{\overline{y}\in\mathcal{Y}} satisfy the following properties:

1. (C1)

   The arg sup in ([S​1S1](https://arxiv.org/html/2512.21149v1#S3.Ex25 "In The extended HJB system. ‣ 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")) exists, is denoted by π^\widehat{\pi}, and it is an admissible control.
2. (C2)

   The triplet (V,G∞,(gy¯)y¯∈𝒴)\left(V,G\_{\infty},\left(g^{\overline{y}}\right)\_{\overline{y}\in\mathcal{Y}}\right) solves the system ([S​1S1](https://arxiv.org/html/2512.21149v1#S3.Ex25 "In The extended HJB system. ‣ 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty"))-([S​4S4](https://arxiv.org/html/2512.21149v1#S3.Ex28 "In The extended HJB system. ‣ 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")).
3. (C3)

   For every y¯∈𝒴\overline{y}\in\mathcal{Y},

   |  |  |  |
   | --- | --- | --- |
   |  | gy¯∈𝒞1,2,2​(𝒯×𝒳×𝒴)g^{\overline{y}}\in\mathcal{C}^{1,2,2}\left(\mathcal{T}\times\mathcal{X}\times\mathcal{Y}\right) |  |

   and

   |  |  |  |
   | --- | --- | --- |
   |  | V∈𝒞1,2,2​(𝒯×𝒳×𝒴),G∞∈𝒞1,2,2​(𝒯×𝒳×𝒴).V\in\mathcal{C}^{1,2,2}\left(\mathcal{T}\times\mathcal{X}\times\mathcal{Y}\right),G\_{\infty}\in\mathcal{C}^{1,2,2}\left(\mathcal{T}\times\mathcal{X}\times\mathcal{Y}\right). |  |
4. (C4)

   For every y¯∈𝒴\overline{y}\in\mathcal{Y} and π∈𝓐\pi\in\bm{\mathcal{A}},

   |  |  |  |
   | --- | --- | --- |
   |  | gy¯∈ℒ¯2​(Xπ,Yπ),g^{\overline{y}}\in\overline{\mathcal{L}}^{2}\left(X^{\pi},Y^{\pi}\right), |  |

   and for every π∈𝓐\pi\in\bm{\mathcal{A}},

   |  |  |  |
   | --- | --- | --- |
   |  | V∈ℒ2​(Xπ,Yπ),G∞∈ℒ2​(Xπ,Yπ).V\in\mathcal{L}^{2}\left(X^{\pi},Y^{\pi}\right),G\_{\infty}\in\mathcal{L}^{2}\left(X^{\pi},Y^{\pi}\right). |  |

Then:

1. (R1)

   gy¯​(t,x,y)=gπ^;y¯​(t,x,y)g^{\overline{y}}(t,x,y)=g^{\widehat{\pi};\overline{y}}(t,x,y), and admits the probabilistic representation

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | gy¯​(t,x,y)\displaystyle g^{\overline{y}}(t,x,y) | =𝔼​[uγ​(YT)​(XTπ^)|Xtπ^=x,Yt=y,YT=y¯]\displaystyle=\mathbb{E}\left[u^{\gamma(Y\_{T})}\left(X^{\widehat{\pi}}\_{T}\right)|\,X^{\widehat{\pi}}\_{t}=x,Y\_{t}=y,Y\_{T}=\overline{y}\right] |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | =𝔼​[uγ​(y¯)​(XTπ^)|Xtπ^=x,Yt=y].\displaystyle=\mathbb{E}\left[u^{\gamma(\overline{y})}\left(X^{\widehat{\pi}}\_{T}\right)|\,X^{\widehat{\pi}}\_{t}=x,Y\_{t}=y\right]. |  |
2. (R2)

   For π^\widehat{\pi} realizing the sup in ([S​1S1](https://arxiv.org/html/2512.21149v1#S3.Ex25 "In The extended HJB system. ‣ 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")), the objective can be written as

   |  |  |  |
   | --- | --- | --- |
   |  | Jπ^​(t,x,y)=∫𝒴φy¯​(gy¯​(t,x,y))​𝑑FYT​(y¯;t,y).J^{\widehat{\pi}}(t,x,y)=\int\_{\mathcal{Y}}\varphi^{\overline{y}}\left(g^{\overline{y}}(t,x,y)\right)\,dF\_{Y\_{T}}(\overline{y};t,y). |  |
3. (R3)

   π^\widehat{\pi} is an equilibrium investment strategy.
4. (R4)

   The equilibrium value function is given by

   |  |  |  |
   | --- | --- | --- |
   |  | V^​(t,x,y)=V​(t,x,y)=∫𝒴φy¯​(gy¯​(t,x,y))​𝑑FYT​(y¯;t,y),\widehat{V}(t,x,y)=V(t,x,y)=\int\_{\mathcal{Y}}\varphi^{\overline{y}}\left(g^{\overline{y}}(t,x,y)\right)\,dF\_{Y\_{T}}(\overline{y};t,y), |  |

   and admits the probabilistic representation ([3.2](https://arxiv.org/html/2512.21149v1#S3.E2 "In 3.1 Preliminary definitions and state process dynamics under conditional measures ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")) for π=π^\pi=\widehat{\pi}.

Proof. See Appendix [A.2](https://arxiv.org/html/2512.21149v1#A1.SS2 "A.2 Proof of Theorem 3.5 ‣ Appendix A Proofs ‣ Equilibrium investment under dynamic preference uncertainty").

The verification theorem allows us to simplify the eHJB ([S​1S1](https://arxiv.org/html/2512.21149v1#S3.Ex25 "In The extended HJB system. ‣ 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty"))-([S​4S4](https://arxiv.org/html/2512.21149v1#S3.Ex28 "In The extended HJB system. ‣ 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")) in a way analogous to what is done in Section 16.1 of BKM21. From (R4) and ([3.13](https://arxiv.org/html/2512.21149v1#S3.E13 "In 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")), we in fact notice that

|  |  |  |
| --- | --- | --- |
|  | V​(t,x,y)=G∞​(t,x,y).V(t,x,y)=G\_{\infty}(t,x,y). |  |

Therefore, the first two terms under the supremum in ([S​1S1](https://arxiv.org/html/2512.21149v1#S3.Ex25 "In The extended HJB system. ‣ 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")) cancel out.

###### Corollary 3.6.

Using ([3.14](https://arxiv.org/html/2512.21149v1#S3.E14 "In 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")), the eHJB ([S​1S1](https://arxiv.org/html/2512.21149v1#S3.Ex25 "In The extended HJB system. ‣ 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty"))-([S​4S4](https://arxiv.org/html/2512.21149v1#S3.Ex28 "In The extended HJB system. ‣ 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")) can be written in the following equivalent form:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0\displaystyle 0 | =supπ∈𝒜​(t,x,y)ℋ¯π​((gy¯)y¯∈𝒴)​(t,x,y),\displaystyle=\sup\limits\_{\pi\in\mathcal{A}(t,x,y)}\overline{\mathcal{H}}^{\pi}\left(\left(g^{\overline{y}}\right)\_{\overline{y}\in\mathcal{Y}}\right)(t,x,y), |  | (S​1¯\overline{S1}) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0\displaystyle 0 | =𝒟¯π^​gy¯​(t,x,y),y¯∈𝒴,\displaystyle=\overline{\mathcal{D}}^{\widehat{\pi}}g^{\overline{y}}\left(t,x,y\right),\qquad\,\overline{y}\in\mathcal{Y}, |  | (S​2¯\overline{S2}) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | uγ​(y¯)​(x)\displaystyle u^{\gamma(\overline{y})}(x) | =gy¯​(T,x,y),y¯∈𝒴,\displaystyle=g^{\overline{y}}\left(T,x,y\right),\qquad\,\overline{y}\in\mathcal{Y}, |  | (S​3¯\overline{S3}) |

where π^\widehat{\pi} realizes the supremum in ([S​1¯\overline{S1}](https://arxiv.org/html/2512.21149v1#S3.Ex47 "In Corollary 3.6. ‣ 3.3 Verification results ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")).

### 3.4 Relation to existing formulations

To place our eHJB in context, we relate it to the general framework of time-inconsistent control developed by BKM21. We begin by recalling the eHJB associated with the objective function (LABEL:eq:reward\_functional\_general\_BKM2021), adapted to the case when the state space is two-dimensional. For clarity, we consistently translate their notation into ours.

For functions g=(g1,g2)g=(g\_{1},g\_{2}) and GG, recall the definitions used by BKM21 introduced in ([3.8](https://arxiv.org/html/2512.21149v1#S3.E8 "In 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")). In addition, for a function ff, they write

|  |  |  |
| --- | --- | --- |
|  | fs​x~​y~​(t,x,y):=f​(t,x,y,s,x~,y~),with ​s,x~,y~​ seen as fixed values.f^{s\tilde{x}\tilde{y}}(t,x,y):=f(t,x,y,s,\tilde{x},\tilde{y}),\quad\mbox{with }s,\tilde{x},\tilde{y}\;\mbox{ seen as fixed values.} |  |

With these definitions, the full characterization of the value function VV, the family of auxiliary value functions fs​x~​y~​(t,x,y)f^{s\tilde{x}\tilde{y}}(t,x,y), and the function gg, takes the form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=supπ∈𝒜​(t,x,y){𝒟πV(t,x,y)+H(t,x,y,t,x,y,π)−𝒟πf(t,x,y,t,x,y),+𝒟πft​x​y(t,x,y)−𝒟π(G⋄g)(t,x,y)+(ℋπg)(t,x,y)},0=𝒟π^​fs​x~​y~​(t,x,y)+H​(s,x~,y~,t,x,y,π^),(s,x~,y~)∈[0,T)×𝒳×𝒴,(0,0)=𝒟π^​g​(t,x,y),V​(T,x,y)=F​(T,x,y,x,y)+G​(T,x,y,x,y),fs​x~​y~​(T,x,y)=F​(s,x~,y~,x,y),(s,x~,y~)∈[0,T)×𝒳×𝒴,g​(T,x,y)=(x,y),\begin{split}0&=\sup\_{\pi\in\mathcal{A}(t,x,y)}\Big\{\mathcal{D}^{\pi}V(t,x,y)+H(t,x,y,t,x,y,\pi)-\mathcal{D}^{\pi}f(t,x,y,t,x,y),\\ &\hskip 42.67912pt+\mathcal{D}^{\pi}f^{txy}(t,x,y)-\mathcal{D}^{\pi}(G\diamond g)(t,x,y)+(\mathcal{H}^{\pi}g)(t,x,y)\Big\},\\ 0&=\mathcal{D}^{\widehat{\pi}}f^{s\tilde{x}\tilde{y}}(t,x,y)+H(s,\tilde{x},\tilde{y},t,x,y,\widehat{\pi}),\quad(s,\tilde{x},\tilde{y})\in[0,T)\times\mathcal{X}\times\mathcal{Y},\\ (0,0)&=\mathcal{D}^{\widehat{\pi}}g(t,x,y),\\ V(T,x,y)&=F(T,x,y,x,y)+G(T,x,y,x,y),\\ f^{s\tilde{x}\tilde{y}}(T,x,y)&=F(s,\tilde{x},\tilde{y},x,y),\quad(s,\tilde{x},\tilde{y})\in[0,T)\times\mathcal{X}\times\mathcal{Y},\\ g(T,x,y)&=(x,y),\end{split} |  | (3.16) |

where π^\widehat{\pi} realizes the supremum in the first equation of ([3.16](https://arxiv.org/html/2512.21149v1#S3.E16 "In 3.4 Relation to existing formulations ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")).

To understand how our system relates to the general framework presented above, we need to examine what happens when the general reward functional (LABEL:eq:reward\_functional\_general\_BKM2021) contains only the nonlinear GG-term corresponding to ([3.7](https://arxiv.org/html/2512.21149v1#S3.E7 "In 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")). This case arises by setting H≡0H\equiv 0 and F≡0F\equiv 0.

Under this restriction, several simplifications occur in the system ([3.16](https://arxiv.org/html/2512.21149v1#S3.E16 "In 3.4 Relation to existing formulations ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")). Firstly, the second and fifth equations are redundant. Secondly, by noticing that V=G⋄gV=G\diamond g, the two terms (𝒟π​V)​(t,x,y)(\mathcal{D}^{\pi}V)(t,x,y) and 𝒟π​(G⋄g)​(t,x,y)\mathcal{D}^{\pi}(G\diamond g)(t,x,y) become identical. This gives the system

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0\displaystyle 0 | =supπ∈𝒜​(t,x,y)(ℋπ​g)​(t,x,y),\displaystyle=\sup\_{\pi\in\mathcal{A}(t,x,y)}(\mathcal{H}^{\pi}g)(t,x,y), |  | (3.17) |
|  | (0,0)\displaystyle(0,0) | =𝒟π^​g​(t,x,y),\displaystyle=\mathcal{D}^{\widehat{\pi}}g(t,x,y), |  |
|  | g​(T,x,y)\displaystyle g(T,x,y) | =(x,y),\displaystyle=(x,y), |  |

which is structurally similar to ([S​1¯\overline{S1}](https://arxiv.org/html/2512.21149v1#S3.Ex47 "In Corollary 3.6. ‣ 3.3 Verification results ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty"))–([S​3¯\overline{S3}](https://arxiv.org/html/2512.21149v1#S3.Ex49 "In Corollary 3.6. ‣ 3.3 Verification results ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")).

As for the extended system in DesmettreSteffensen2023:MF, Theorem 3.5, observe that Ut​(t,x)U\_{t}(t,x) and all the terms in the first two lines under the infimum in their Eq. (10) cancel out as a consequence of their Eq. (20). After these cancellations, their extended system can be rewritten in the following compact form:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 0\displaystyle 0 | =supπ∫ιγ​(Yγ​(t,x))​𝒟π​Yγ​(t,x)​dΓ​(γ),\displaystyle=\sup\_{\pi}\int\iota^{\gamma}(Y^{\gamma}(t,x))\,\mathcal{D}^{\pi}Y^{\gamma}(t,x)\,\mathrm{d}\Gamma(\gamma), |  | (3.18) |
|  | 0\displaystyle 0 | =𝒟π^​Yγ​(t,x),for each realization of ​γ,\displaystyle=\mathcal{D}^{\widehat{\pi}}Y^{\gamma}(t,x),\qquad\text{for each realization of }\gamma, |  |
|  | uγ​(x)\displaystyle u^{\gamma}(x) | =Yγ​(T,x),for each realization of ​γ,\displaystyle=Y^{\gamma}(T,x),\qquad\text{for each realization of }\gamma, |  |

which is identical to our eHJB for v​(x)=xv(x)=x once we translate their notation into ours:

|  |  |  |
| --- | --- | --- |
|  | γ→γ​(y¯),ιγ→(φy¯)′,Yγ​(t,x)→gy¯​(t,x,y),uγ→uγ​(y¯),d​Γ​(γ)→d​FYT​(y¯;t,y).\begin{split}&\gamma\rightarrow\gamma(\overline{y}),\quad\iota^{\gamma}\rightarrow\left(\varphi^{\overline{y}}\right)^{\prime},\quad Y^{\gamma}(t,x)\rightarrow g^{\overline{y}}(t,x,y),\\ &u^{\gamma}\rightarrow u^{\gamma(\overline{y})},\quad d\Gamma(\gamma)\rightarrow dF\_{Y\_{T}}(\overline{y};t,y).\end{split} |  |

Finally, we relate our eHJB to the system in Eq. (9) of ChenGuanLiang2025, reported below:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=supπ∈Π{∑k∈𝒮((uk)−1)′​(fi,k​(t,x))​𝒜π​fi,k​(t,x)​p​(t,i,k)}=0,0=𝒜π​fi,j​(t,x)=0,j∈𝒮,fi,j​(T,x)=uj​(x),j∈𝒮.\begin{split}0&=\sup\_{\pi\in\Pi}\left\{\sum\_{k\in\mathcal{S}}\left((u^{k})^{-1}\right)^{\prime}\left(f^{i,k}(t,x)\right)\;\mathscr{A}^{\pi}f^{i,k}(t,x)\;p(t,i,k)\right\}=0,\\ 0&=\mathscr{A}^{\pi}f^{i,j}(t,x)=0,\qquad j\in\mathcal{S},\\ f^{i,j}(T,x)&=u^{j}(x),\qquad j\in\mathcal{S}.\end{split} |  | (3.19) |

Here 𝒮:={1,…,n}\mathcal{S}:=\left\{1,\dots,n\right\}, with n∈ℕn\in\mathbb{N}, is the state space of the Markov chain ϵ:=(ϵt)t∈𝒯\epsilon:=\left(\epsilon\_{t}\right)\_{t\in\mathcal{T}} driving both risk aversion and market coefficients, p​(t,i,k)=ℙ​(ϵT=k|ϵt=i)p(t,i,k)=\mathbb{P}\left(\epsilon\_{T}=k\,|\ \epsilon\_{t}=i\right), for every t∈𝒯t\in\mathcal{T} and i,k∈𝒮i,k\in\mathcal{S}, Π\Pi is the set of admissible strategies, and 𝒜π\mathscr{A}^{\pi} is the controlled infinitesimal generator of the regime-switching diffusion. Naturally, ([3.19](https://arxiv.org/html/2512.21149v1#S3.E19 "In 3.4 Relation to existing formulations ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")) corresponds to the special case of our ([S​1¯\overline{S1}](https://arxiv.org/html/2512.21149v1#S3.Ex47 "In Corollary 3.6. ‣ 3.3 Verification results ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")) under v​(x)=x,ρ=0v(x)=x,\rho=0, and the dictionary

|  |  |  |
| --- | --- | --- |
|  | Σ→∫,𝒮→𝒴,k→y¯,j→y¯,i→y,(uk)−1→φy¯,p​(t,i,k)→d​FYT​(y¯;t,y),fi,j​(t,x)→gy¯​(t,x,y).\begin{split}&\Sigma\rightarrow\int,\quad\mathcal{S}\rightarrow\mathcal{Y},\quad k\rightarrow\overline{y},\quad j\rightarrow\overline{y},\quad i\rightarrow y,\quad\left(u^{k}\right)^{-1}\rightarrow\varphi^{\overline{y}},\\ &p(t,i,k)\rightarrow dF\_{Y\_{T}}(\overline{y};t,y),\quad f^{i,j}(t,x)\rightarrow g^{\overline{y}}(t,x,y).\end{split} |  |

Due to the assumption of independence between the Markov chain ϵ\epsilon and the Brownian motion driving the wealth process in ChenGuanLiang2025, conditioning on ϵT=k\epsilon\_{T}=k, for some k∈𝒮k\in\mathcal{S}, does not change the law of the wealth process. In contrast, our setting allows for arbitrary correlation between XX and YY via ρ∈[−1,1]\rho\in[-1,1]. Conditioning on YT=y¯Y\_{T}=\overline{y} therefore changes the law of XX, which requires a change of the differential operator from 𝒟\mathcal{D} (under ℙt,x,y\mathbb{P}\_{t,x,y}) to 𝒟¯\overline{\mathcal{D}} (under ℙt,x,y,y¯\mathbb{P}\_{t,x,y,\overline{y}}).

## 4 Application: state-dependent CRRA utility

In this section, we apply the general equilibrium framework developed in Sections [2](https://arxiv.org/html/2512.21149v1#S2 "2 Problem formulation ‣ Equilibrium investment under dynamic preference uncertainty") and [3](https://arxiv.org/html/2512.21149v1#S3 "3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty") to a tractable case in which the investor’s relative risk aversion is driven by an exogenous factor that follows an arithmetic Brownian motion.

First, we describe the preference specification and derive the specialized form of the eHJB. Second, we analyze the resulting equilibrium policy numerically and provide some intuition on the underlying economic mechanisms.

### 4.1 Preference specification and equilibrium investment

We consider preferences that are CRRA with a state-dependent relative risk aversion. The intertemporal variation in risk attitudes is driven by an exogenous factor, denoted by YY, which evolves according to the arithmetic Brownian motion

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Yt=μY​d​t+σY​d​Bt1,dY\_{t}=\mu\_{Y}dt+\sigma\_{Y}dB^{1}\_{t}, |  | (4.1) |

for constants μY∈ℝ\mu\_{Y}\in\mathbb{R} and σY>0\sigma\_{Y}>0, with slight abuse of notation compared to ([2.2](https://arxiv.org/html/2512.21149v1#S2.E2 "In 2 Problem formulation ‣ Equilibrium investment under dynamic preference uncertainty")).

For a fixed realization of YT=y¯Y\_{T}=\overline{y}, we model the risk aversion coefficient by

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ​(y¯):=ey¯,\gamma(\overline{y}):=e^{\overline{y}}, |  | (4.2) |

which induces the CRRA utility

|  |  |  |  |
| --- | --- | --- | --- |
|  | uγ​(y¯)​(x)=x1−γ​(y¯)1−γ​(y¯).u^{\gamma(\overline{y})}(x)=\dfrac{x^{1-\gamma(\overline{y})}}{1-\gamma(\overline{y})}. |  | (4.3) |

Thus, the investor behaves as a standard CRRA agent along the wealth dimension, while changes in YY alter her effective risk aversion over time.

The corresponding evaluation of a portfolio strategy π\pi is recalled here for convenience:

|  |  |  |
| --- | --- | --- |
|  | Jπ​(t,x,y)=∫𝒴φy¯​(𝔼t,x,y,y¯​[uγ​(y¯)​(XTπ)])​fYT​(y¯;t,y)​𝑑y¯.J^{\pi}(t,x,y)=\int\_{\mathcal{Y}}\varphi^{\overline{y}}\!\left(\mathbb{E}\_{t,x,y,\bar{y}}\big[u^{\gamma(\bar{y})}(X^{\pi}\_{T})\big]\right)f\_{Y\_{T}}(\bar{y};t,y)\,d\bar{y}. |  |

In the general framework of Section [3](https://arxiv.org/html/2512.21149v1#S3 "3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty"), vv is an arbitrary increasing, concave, and differentiable function. Here, we adopt the logarithmic form

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(x)=ln⁡(x),v(x)=\ln(x), |  | (4.4) |

which is helpful for tractability reasons as it naturally aligns with the multiplicative structure of CRRA preferences. (This form of aggregator for certainty equivalents is also used in BS21, albeit in a different context.)

In addition, recall that the density fYT​(y¯;t,y)f\_{Y\_{T}}(\bar{y};t,y) is the PDF of YTY\_{T} conditional on Yt=yY\_{t}=y, which is Gaussian, since ([4.1](https://arxiv.org/html/2512.21149v1#S4.E1 "In 4.1 Preference specification and equilibrium investment ‣ 4 Application: state-dependent CRRA utility ‣ Equilibrium investment under dynamic preference uncertainty")) implies

|  |  |  |
| --- | --- | --- |
|  | YT|Yt=y∼𝒩​(y+μY​(T−t),σY2​(T−t)).Y\_{T}\,|\,Y\_{t}=y\sim\mathcal{N}\left(y+\mu\_{Y}(T-t),\sigma\_{Y}^{2}(T-t)\right). |  |

To construct the equilibrium policy, we next adapt the general eHJB from Section [3](https://arxiv.org/html/2512.21149v1#S3 "3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty") to this CRRA setting. The first step is to identify the dynamics of the state process (Xπ,Y)(X^{\pi},Y) under the family of conditional measures appearing in the equilibrium equations. The next result follows from Lemma [3.1](https://arxiv.org/html/2512.21149v1#S3.Thmtheorem1 "Lemma 3.1. ‣ 3.1 Preliminary definitions and state process dynamics under conditional measures ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty") upon inserting the diffusion specification for YY.

###### Corollary 4.1.

Let B¯1\overline{B}^{1} and B¯2\overline{B}^{2} be two standard Brownian motions under the conditional measure ℙt,x,y,y¯\mathbb{P}\_{t,x,y,\overline{y}}. Then, for s∈[t,T)s\in[t,T):

* •

  The preference factor YY satisfies

  |  |  |  |
  | --- | --- | --- |
  |  | d​Ys=y¯−YsT−s​d​s+σY​d​B¯s1,dY\_{s}=\frac{\overline{y}-Y\_{s}}{T-s}ds+\sigma\_{Y}d\overline{B}^{1}\_{s}, |  |

  with Yt=yY\_{t}=y and YT=y¯Y\_{T}=\overline{y}.
* •

  The wealth process XπX^{\pi} satisfies

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | d​Xsπ\displaystyle dX^{\pi}\_{s} | =Xsπ​(r+π​(s)​(μS−r)+π​(s)​ρ​σSσY​y¯−Ys−μY​(T−s)T−s)​d​s\displaystyle=X^{\pi}\_{s}\left(r+\pi(s)(\mu\_{S}-r)+\pi(s)\rho\frac{\sigma\_{S}}{\sigma\_{Y}}\frac{\overline{y}-Y\_{s}-\mu\_{Y}(T-s)}{T-s}\right)ds |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | +Xsπ​π​(s)​σS​(ρ​d​B¯s1+1−ρ2​d​B¯s2),\displaystyle\qquad+X^{\pi}\_{s}\pi(s)\sigma\_{S}\left(\rho d\overline{B}^{1}\_{s}+\sqrt{1-\rho^{2}}d\overline{B}^{2}\_{s}\right), |  |

  with Xtπ=xX^{\pi}\_{t}=x and XTπ=limt→TXtπX^{\pi}\_{T}=\lim\_{t\to T}X^{\pi}\_{t}.

Proof. See Appendix [A.3](https://arxiv.org/html/2512.21149v1#A1.SS3 "A.3 Proof of Corollary 4.1 ‣ Appendix A Proofs ‣ Equilibrium investment under dynamic preference uncertainty").

The process YY thus becomes an arithmetic Brownian bridge under ℙt,x,y,y¯\mathbb{P}\_{t,x,y,\overline{y}}, whereas XπX^{\pi} carries an additional drift adjustment reflecting both the conditioning on YT=y¯Y\_{T}=\bar{y} and the correlation between the underlying shocks.

The following proposition provides the semi-explicit representation of an equilibrium policy. Its expression depends on a family of auxiliary functions hy¯​(t,y)h^{\bar{y}}(t,y) which solve a coupled nonlinear PIDE.

###### Proposition 4.2.

For a reward functional of the form in ([2.3](https://arxiv.org/html/2512.21149v1#S2.E3 "In 2 Problem formulation ‣ Equilibrium investment under dynamic preference uncertainty")), consider a CRRA specification ([4.2](https://arxiv.org/html/2512.21149v1#S4.E2 "In 4.1 Preference specification and equilibrium investment ‣ 4 Application: state-dependent CRRA utility ‣ Equilibrium investment under dynamic preference uncertainty"))-([4.3](https://arxiv.org/html/2512.21149v1#S4.E3 "In 4.1 Preference specification and equilibrium investment ‣ 4 Application: state-dependent CRRA utility ‣ Equilibrium investment under dynamic preference uncertainty")) with logarithmic certainty equivalent aggregator ([4.4](https://arxiv.org/html/2512.21149v1#S4.E4 "In 4.1 Preference specification and equilibrium investment ‣ 4 Application: state-dependent CRRA utility ‣ Equilibrium investment under dynamic preference uncertainty")). In this setting, the equilibrium investment policy depends only on (t,y)(t,y) and is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | π^​(t,y)=μS−r+ρ​σS​σY​∫𝒴∂yhy¯​(t,y)hy¯​(t,y)​fYT​(y¯;t,y)​𝑑y¯σS2​exp⁡(y+μY​(T−t)+12​σY2​(T−t)),\begin{split}\widehat{\pi}(t,y)&=\dfrac{\mu\_{S}-r+\rho\sigma\_{S}\sigma\_{Y}\displaystyle{\int\_{\mathcal{Y}}\dfrac{\partial\_{y}h^{\bar{y}}(t,y)}{h^{\bar{y}}(t,y)}f\_{Y\_{T}}(\bar{y};t,y)d\bar{y}}}{\sigma\_{S}^{2}\exp\left(y+\mu\_{Y}(T-t)+\dfrac{1}{2}\sigma\_{Y}^{2}(T-t)\right)},\end{split} |  | (4.5) |

where, for each y¯∈𝒴\bar{y}\in\mathcal{Y}, the function hy¯h^{\bar{y}} solves

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=∂thy¯​(t,y)+(y¯−yT−t+ρ​π^​σS​σY​(1−ey¯))​∂yhy¯​(t,y)+12​σY2​∂y​yhy¯​(t,y)+(r+π^​(μS−r+ρ​σSσY​(y¯−yT−t−μY))−12​π^2​σS2​ey¯)​(1−ey¯)​hy¯​(t,y),hy¯​(T,y)=1.\begin{split}0&=\partial\_{t}h^{\bar{y}}(t,y)+\left(\dfrac{\bar{y}-y}{T-t}+\rho\widehat{\pi}\sigma\_{S}\sigma\_{Y}\big(1-e^{\bar{y}}\big)\right)\partial\_{y}h^{\bar{y}}(t,y)+\dfrac{1}{2}\sigma\_{Y}^{2}\partial\_{yy}h^{\bar{y}}(t,y)\\ &+\left(r+\widehat{\pi}\left(\mu\_{S}-r+\rho\dfrac{\sigma\_{S}}{\sigma\_{Y}}\left(\dfrac{\bar{y}-y}{T-t}-\mu\_{Y}\right)\right)-\dfrac{1}{2}\widehat{\pi}^{2}\sigma\_{S}^{2}\,e^{\bar{y}}\right)\big(1-e^{\bar{y}}\big)h^{\bar{y}}(t,y),\\ h^{\bar{y}}(T,y)&=1.\end{split} |  | (4.6) |

Proof. See Appendix [A.4](https://arxiv.org/html/2512.21149v1#A1.SS4 "A.4 Proof of Proposition 4.2 ‣ Appendix A Proofs ‣ Equilibrium investment under dynamic preference uncertainty").

The relation defining the equilibrium control in ([4.5](https://arxiv.org/html/2512.21149v1#S4.E5 "In Proposition 4.2. ‣ 4.1 Preference specification and equilibrium investment ‣ 4 Application: state-dependent CRRA utility ‣ Equilibrium investment under dynamic preference uncertainty")) and the PIDE for hy¯h^{\bar{y}} in ([4.6](https://arxiv.org/html/2512.21149v1#S4.E6 "In Proposition 4.2. ‣ 4.1 Preference specification and equilibrium investment ‣ 4 Application: state-dependent CRRA utility ‣ Equilibrium investment under dynamic preference uncertainty")) are jointly nonlinear and fully coupled, except in the special case ρ=0\rho=0. The numerical computations reported below are based on solving this forward-backward system.

### 4.2 Interpretation and numerical analysis

Let us comment on the equilibrium investment policy in ([4.5](https://arxiv.org/html/2512.21149v1#S4.E5 "In Proposition 4.2. ‣ 4.1 Preference specification and equilibrium investment ‣ 4 Application: state-dependent CRRA utility ‣ Equilibrium investment under dynamic preference uncertainty")). Since the exponential factor appearing in the denominator equals the conditional expectation of γ​(YT)\gamma(Y\_{T}) given Yt=yY\_{t}=y, we may rewrite π^​(t,y)\widehat{\pi}(t,y) as

|  |  |  |
| --- | --- | --- |
|  | π^​(t,y)=μS−rσS2​𝔼t,y​[γ​(YT)]+ρ​σYσS​𝔼t,y​[γ​(YT)]​∫𝒴∂yhy¯​(t,y)hy¯​(t,y)​fYT​(y¯;t,y)​𝑑y¯.\widehat{\pi}(t,y)=\dfrac{\mu\_{S}-r}{\sigma\_{S}^{2}\mathbb{E}\_{t,y}\left[\gamma(Y\_{T})\right]}+\dfrac{\rho\sigma\_{Y}}{\sigma\_{S}\mathbb{E}\_{t,y}\left[\gamma(Y\_{T})\right]}\int\_{\mathcal{Y}}\frac{\partial\_{y}h^{\bar{y}}(t,y)}{h^{\bar{y}}(t,y)}f\_{Y\_{T}}(\bar{y};t,y)\,d\bar{y}. |  |

The first term is the familiar myopic (Merton-type) demand, but with the constant risk aversion coefficient replaced by the conditional expectation of its terminal realization. The second term is what we call a preference-hedging demand,
for it captures the agent’s intention to adjust today’s exposure in anticipation of how her future risk aversion may evolve. Crucially, this hedging term depends not only on preference dynamics but also on how these dynamics interact with the market. When ρ≠0\rho\neq 0, preference shocks and asset return shocks are partially correlated, giving the investor a channel to hedge the stochastic evolution of her own future risk attitudes. When ρ=0\rho=0, this channel is absent and the hedging component vanishes entirely, yielding a solution that resembles the one found in Eq. (19) of BS21.

The integral term itself involves the elasticity ∂yhy¯​(t,y)hy¯​(t,y)\frac{\partial\_{y}h^{\bar{y}}(t,y)}{h^{\bar{y}}(t,y)}, where the function hy¯h^{\bar{y}} solves the PIDE in ([4.6](https://arxiv.org/html/2512.21149v1#S4.E6 "In Proposition 4.2. ‣ 4.1 Preference specification and equilibrium investment ‣ 4 Application: state-dependent CRRA utility ‣ Equilibrium investment under dynamic preference uncertainty")). As shown in the proof of Proposition [4.2](https://arxiv.org/html/2512.21149v1#S4.Thmtheorem2 "Proposition 4.2. ‣ 4.1 Preference specification and equilibrium investment ‣ 4 Application: state-dependent CRRA utility ‣ Equilibrium investment under dynamic preference uncertainty") in Appendix [A.4](https://arxiv.org/html/2512.21149v1#A1.SS4 "A.4 Proof of Proposition 4.2 ‣ Appendix A Proofs ‣ Equilibrium investment under dynamic preference uncertainty"), this function is tied to the value function of the problem (specifically, to the continuation value), so the hedging demand reflects the sensitivity of future continuation value to the current preference state.

A notable feature of this representation is that, despite the complexity of the underlying dynamic inconsistency, the equilibrium policy does not depend on wealth. This property, of course, follows from the homothetic structure of CRRA preferences and is preserved here even in the presence of evolving risk attitudes. It is worth contrasting this with the findings of KrausslLucasSiegman2012:FinResearchLetters, who –working with a different model for preferences– show that uncertainty about risk aversion can instead generate a positive relation between wealth and risk taking.

![Refer to caption](eqpolicy_positive_muy_positive_rho.png)


(a)

![Refer to caption](eqpolicy_negative_muy_positive_rho.png)


(b)

![Refer to caption](prefhedging_positive_muy_positive_rho.png)


(c)

![Refer to caption](prefhedging_negative_muy_positive_rho.png)


(d)

Figure 1: Equilibrium policy π^​(t,y)\widehat{\pi}(t,y) and preference hedging demand for μY=0.02\mu\_{Y}=0.02 (left column) and μY=−0.02\mu\_{Y}=-0.02 (right column). Other parameters: (r,μS,σS,σY,ρ,exp⁡(y0))=(0.02, 0.07, 0.2, 0.04, 0.6, 2)(r,\mu\_{S},\sigma\_{S},\sigma\_{Y},\rho,\exp(y\_{0}))=(0.02,\,0.07,\,0.2,\,0.04,\,0.6,\,2).

Figures [1](https://arxiv.org/html/2512.21149v1#S4.F1 "Figure 1 ‣ 4.2 Interpretation and numerical analysis ‣ 4 Application: state-dependent CRRA utility ‣ Equilibrium investment under dynamic preference uncertainty") (a)-(b) show the equilibrium policy for μY={−0.02,0.02}\mu\_{Y}=\{-0.02,0.02\}, while Figures [1](https://arxiv.org/html/2512.21149v1#S4.F1 "Figure 1 ‣ 4.2 Interpretation and numerical analysis ‣ 4 Application: state-dependent CRRA utility ‣ Equilibrium investment under dynamic preference uncertainty") (c)-(d) display the corresponding preference hedging demand. Other parameters in the computations are set as follows: (r,μS,σS,σY,ρ,exp⁡(y0))=(0.02, 0.07, 0.2, 0.04, 0.6, 2)(r,\mu\_{S},\sigma\_{S},\sigma\_{Y},\rho,\exp(y\_{0}))=(0.02,\,0.07,\,0.2,\,0.04,\,0.6,\,2).

A first observation is the asymmetry between positive and negative μY\mu\_{Y}. When μY=0.02\mu\_{Y}=0.02, the expected drift of future risk aversion is positive. For a fixed current state yy, the agent behaves more conservatively at early dates, and the equilibrium policy increases over time. The associated preference-hedging demand is positive but small and decays quickly. Its economic role is to partially counteract the conservative initial attitude, although quantitatively the effect is minor.

When μY=−0.02\mu\_{Y}=-0.02, the expected drift of future risk aversion is negative. The agent initially invests more aggressively, anticipating a less risk-averse future self, and the equilibrium policy decreases over time. Here, the hedging demand reinforces the agent’s initial behavior and is larger in magnitude. A plausible explanation is that the distribution of YTY\_{T} shifts towards regions where hy¯h^{\bar{y}} is more sensitive in yy, leading to a higher weighted elasticity.

It is important to emphasize that, in standard models of time-inconsistent preferences, agents may foresee changes in utility, but equilibrium strategies typically do not feature an explicit hedging motive against such preference shifts. In our setting, however, a hedging component arises endogenously from the sensitivity structure of the continuation value with respect to the preference factor YY.

Additional numerical results, including tables, are provided in Appendix [B](https://arxiv.org/html/2512.21149v1#A2 "Appendix B Additional numerical results ‣ Equilibrium investment under dynamic preference uncertainty"). The pseudocode for the computational procedure is given in Appendix [C](https://arxiv.org/html/2512.21149v1#A3 "Appendix C Pseudocodes ‣ Equilibrium investment under dynamic preference uncertainty").

## 5 Conclusion

We developed a continuous-time investment framework in which risk preferences evolve endogenously with an observable state variable. By evaluating payoffs through conditional certainty equivalents and aggregating them across future preference states, we obtained a reward functional that is inherently time-inconsistent. This required refining existing equilibrium methods for time-inconsistent control problems and deriving a new one suited to our setting.

Specializing to CRRA preferences, we let the underlying preference factor follow an arithmetic Brownian motion and define relative risk aversion as its exponential –yielding de facto a geometric Brownian motion for risk aversion itself. Under this specification, we showed that the equilibrium system reduces to a coupled nonlinear PIDE indexed by terminal preference states. The resulting semi-explicit equilibrium portfolio rule features a novel hedging component that captures incentives to adjust current exposure in the risky asset in anticipation of future changes in risk attitudes.

Possible avenues for future work include expanding the market environment (for instance, by introducing incompleteness), incorporating intermediate evaluation of consumption, and allowing for path dependence in the evolution of preferences over time.

## Acknowledgements

We gratefully thank the institutions at which parts of this work were carried out. Luca De Gennaro Aquino acknowledges the University of Copenhagen, the Johannes Kepler University Linz, and the University of Lausanne for their support and hospitality. Sascha Desmettre is grateful to the University of Copenhagen and to the University of Lausanne for supporting the respective research visits. Yevhen Havrylenko acknowledges the financial support from the PRIME program (<https://www.daad.de/en/studying-in-germany/scholarships/daad-funding-programmes/prime/prime-fellows-202324/>) of the German Academic Exchange Service (DAAD, <https://ror.org/039djdh30>), funded by the German Federal Ministry of Education and Research (BMBF). He further acknowledges the generous support of the University of Copenhagen and Ulm University, where parts of this research were done, and the Johannes Kepler University Linz for its hospitality during his research visit.

## Appendices

## Appendix A Proofs

### A.1 Proof of Lemma [3.1](https://arxiv.org/html/2512.21149v1#S3.Thmtheorem1 "Lemma 3.1. ‣ 3.1 Preliminary definitions and state process dynamics under conditional measures ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")

To derive the dynamics of YY under ℙt,x,y,y¯\mathbb{P}\_{t,x,y,\overline{y}} (i.e., under the condition YT=y¯Y\_{T}=\overline{y}), we can directly use the theory of conditional diffusion processes; see Delyon2006.

To derive the dynamics of XπX^{\pi}, again under ℙt,x,y,y¯\mathbb{P}\_{t,x,y,\overline{y}}, we first note that, by Girsanov’s theorem, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ℙt,x,y,y¯d​ℙt,x,y|ℱT=exp(\displaystyle\left.\frac{d\mathbb{P}\_{t,x,y,\overline{y}}}{d\mathbb{P}\_{t,x,y}}\right|\_{\mathcal{F}\_{T}}=\exp\Biggl( | −∫tTνs1dBs1−∫tTνs2dBs2−12∫tT(νs1)2ds−12∫tT(νs2)2ds),\displaystyle-\int\_{t}^{T}\nu^{1}\_{s}dB^{1}\_{s}-\int\_{t}^{T}\nu^{2}\_{s}dB^{2}\_{s}-\frac{1}{2}\int\_{t}^{T}(\nu^{1}\_{s})^{2}ds-\frac{1}{2}\int\_{t}^{T}(\nu^{2}\_{s})^{2}ds\Biggr), |  |

where ν1\nu^{1} and ν2\nu^{2} are square-integrable processes characterizing the change of measure. Also, the SDEs of standard Brownian motions under ℙt,x,y,y¯\mathbb{P}\_{t,x,y,\overline{y}} are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​B¯s1=d​Bs1+νs1​d​s,d​B¯s2=d​Bs2+νs2​d​s.d\overline{B}^{1}\_{s}=dB^{1}\_{s}+\nu^{1}\_{s}ds,\qquad\,d\overline{B}^{2}\_{s}=dB^{2}\_{s}+\nu^{2}\_{s}ds. |  | (A.1) |

Since conditioning on YT=y¯Y\_{T}=\overline{y} influences only B1B^{1}, and B1⟂B2B^{1}\perp B^{2}, we deduce that the dynamics of B2B^{2} remains unchanged under ℙt,x,y,y¯\mathbb{P}\_{t,x,y,\overline{y}}. Therefore, for a standard Brownian motion B¯2\overline{B}^{2} under ℙt,x,y,y¯\mathbb{P}\_{t,x,y,\overline{y}}, we have d​B¯s2=d​Bs2d\overline{B}^{2}\_{s}=dB^{2}\_{s} and νs2=0\nu^{2}\_{s}=0, for all s∈[t,T]s\in[t,T]. To find the correct ν1\nu\_{1}, we insert ([A.1](https://arxiv.org/html/2512.21149v1#A1.E1 "In A.1 Proof of Lemma 3.1 ‣ Appendix A Proofs ‣ Equilibrium investment under dynamic preference uncertainty")) in ([3.5](https://arxiv.org/html/2512.21149v1#S3.E5 "In 2nd item ‣ Lemma 3.1. ‣ 3.1 Preliminary definitions and state process dynamics under conditional measures ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")) and get

|  |  |  |
| --- | --- | --- |
|  | d​Ys=(μY​(s,Ys)+σY2​(s,Ys)​∂yln⁡(pY​(s,Ys;T,y¯))+σY​(s,Ys)​νs1)​d​s+σY​(s,Ys)​d​Bs1.\displaystyle dY\_{s}=\Big(\mu\_{Y}(s,Y\_{s})+\sigma\_{Y}^{2}(s,Y\_{s})\partial\_{y}\ln\big(p\_{Y}(s,Y\_{s};{T},\overline{y})\big)+\sigma\_{Y}(s,Y\_{s})\nu^{1}\_{s}\Big)ds+\sigma\_{Y}(s,Y\_{s})dB^{1}\_{s}. |  |

As the drift must be equal to μY​(s,Ys)\mu\_{Y}(s,Y\_{s}) under ℙt,x,y\mathbb{P}\_{t,x,y}, and σY​(s,Ys)≠0\sigma\_{Y}(s,Y\_{s})\neq 0 almost surely, for all s∈[t,T]s\in[t,T], we conclude that

|  |  |  |
| --- | --- | --- |
|  | νs1=−σY​(s,Ys)​∂yln⁡(pY​(s,Ys;T,y¯)).\nu^{1}\_{s}=-\sigma\_{Y}(s,Y\_{s})\partial\_{y}\ln\big(p\_{Y}(s,Y\_{s};{T},\overline{y})\big). |  |

Inserting ([A.1](https://arxiv.org/html/2512.21149v1#A1.E1 "In A.1 Proof of Lemma 3.1 ‣ Appendix A Proofs ‣ Equilibrium investment under dynamic preference uncertainty")) in the SDE ([3.4](https://arxiv.org/html/2512.21149v1#S3.E4 "In 1st item ‣ Lemma 3.1. ‣ 3.1 Preliminary definitions and state process dynamics under conditional measures ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")) for XπX^{\pi} under ℙt,x,y\mathbb{P}\_{t,x,y} and using the above form of ν1\nu\_{1} specifying the change of measure, we obtain the SDE of XπX^{\pi} under ℙt,x,y,y¯\mathbb{P}\_{t,x,y,\overline{y}}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xsπ\displaystyle dX^{\pi}\_{s} | =Xsπ​(r+π​(s)​(μS−r))​d​s+Xsπ​π​(s)​σS​(ρ​(d​B¯s1−νs1​d​s)+1−ρ2​d​B¯s2)\displaystyle=X^{\pi}\_{s}(r+\pi(s)(\mu\_{S}-r))ds+X^{\pi}\_{s}\pi(s)\sigma\_{S}\left(\rho\left(d\overline{B}^{1}\_{s}-\nu^{1}\_{s}ds\right)+\sqrt{1-\rho^{2}}d\overline{B}^{2}\_{s}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Xsπ​(r+π​(s)​(μS−r)+π​(s)​σS​ρ​σY​(s,Ys)​∂yln⁡(pY​(s,Ys;T,y¯)))​d​s\displaystyle=X^{\pi}\_{s}\Big(r+\pi(s)(\mu\_{S}-r)+\pi(s)\sigma\_{S}\rho\,\sigma\_{Y}(s,Y\_{s})\,\partial\_{y}\ln\big(p\_{Y}(s,Y\_{s};{T},\overline{y})\big)\Big)ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +Xsπ​π​(s)​σS​(ρ​d​B¯s1+1−ρ2​d​B¯s2).\displaystyle\quad+X^{\pi}\_{s}\pi(s)\sigma\_{S}\left(\rho d\overline{B}^{1}\_{s}+\sqrt{1-\rho^{2}}d\overline{B}^{2}\_{s}\right). |  |

∎

### A.2 Proof of Theorem [3.5](https://arxiv.org/html/2512.21149v1#S3.Thmtheorem5 "Theorem 3.5 (Verification theorem). ‣ 3.3 Verification results ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")

Proof of (R1). Choose an arbitrary but fixed y¯∈𝒴\overline{y}\in\mathcal{Y} and (t,x,y)∈[0,T)×𝒳×𝒴(t,x,y)\in[0,T)\times\mathcal{X}\times\mathcal{Y}. Let π^\widehat{\pi} be the arg​sup\arg\sup in ([3.11](https://arxiv.org/html/2512.21149v1#S3.E11 "In 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")), which exists by assumption (C1). Applying Itô’s lemma to the function gy¯g^{\overline{y}} (which belongs to 𝒞1,2,2​(𝒯×𝒳×𝒴)\mathcal{C}^{1,2,2}\left(\mathcal{T}\times\mathcal{X}\times\mathcal{Y}\right) by assumption (C3)) and the state process (Xπ^,Y)(X^{\widehat{\pi}},Y) under the measure ℙt,x,y,y¯\mathbb{P}\_{t,x,y,\overline{y}}, we get

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | gy¯​(T,XTπ^,YT)\displaystyle g^{\overline{y}}\left(T,X^{\widehat{\pi}}\_{T},Y\_{T}\right) | =gy¯​(t,Xtπ^,Yt)+∫tT𝒟¯π^​gy¯​(s,Xsπ^,Ys)​𝑑s\displaystyle=g^{\overline{y}}\left(t,X^{\widehat{\pi}}\_{t},Y\_{t}\right)+\int\limits\_{t}^{T}\overline{\mathcal{D}}^{\widehat{\pi}}g^{\overline{y}}\left(s,X^{\widehat{\pi}}\_{s},Y\_{s}\right)\,ds |  | (A.2) |
|  |  | +∫tT∂xgy¯​(s,Xsπ^,Ys)​π^​(s)​σS​(ρ​d​B¯s1+1−ρ2​d​B¯s2)\displaystyle\quad+\int\limits\_{t}^{T}\partial\_{x}g^{\overline{y}}\left(s,X^{\widehat{\pi}}\_{s},Y\_{s}\right)\widehat{\pi}(s)\sigma\_{S}\left(\rho d\overline{B}^{1}\_{s}+\sqrt{1-\rho^{2}}d\overline{B}^{2}\_{s}\right) |  |
|  |  | +∫tT∂ygy¯​(s,Xsπ^,Ys)​σY​d​B¯s1.\displaystyle\quad+\int\limits\_{t}^{T}\partial\_{y}g^{\overline{y}}\left(s,X^{\widehat{\pi}}\_{s},Y\_{s}\right)\sigma\_{Y}d\overline{B}^{1}\_{s}. |  |

Taking the expectation on both sides of ([A.2](https://arxiv.org/html/2512.21149v1#A1.E2 "In A.2 Proof of Theorem 3.5 ‣ Appendix A Proofs ‣ Equilibrium investment under dynamic preference uncertainty")), and using the fact that gy¯​(t,x,y)g^{\overline{y}}\left(t,x,y\right) satisfies ([S​2S2](https://arxiv.org/html/2512.21149v1#S3.Ex26 "In The extended HJB system. ‣ 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")) by assumption (C2), as well as gy¯​(t,x,y)∈ℒ2​(Xπ^,Y)g^{\overline{y}}\left(t,x,y\right)\in\mathcal{L}^{2}\left(X^{\widehat{\pi}},Y\right) by assumption (C4), gives

|  |  |  |
| --- | --- | --- |
|  | 𝔼t,x,y,y¯​[gy¯​(T,XTπ^,YT)]=𝔼t,x,y,y¯​[gy¯​(t,Xtπ^,Yt)].\mathbb{E}\_{t,x,y,\overline{y}}\left[g^{\overline{y}}\left(T,X^{\widehat{\pi}}\_{T},Y\_{T}\right)\right]=\mathbb{E}\_{t,x,y,\overline{y}}\left[g^{\overline{y}}\left(t,X^{\widehat{\pi}}\_{t},Y\_{t}\right)\right]. |  |

Thus, since gy¯​(T,x,y)g^{\overline{y}}\left(T,x,y\right) solves ([S​4S4](https://arxiv.org/html/2512.21149v1#S3.Ex28 "In The extended HJB system. ‣ 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")) (again by (C2)), we have

|  |  |  |
| --- | --- | --- |
|  | gy¯​(t,x,y)=𝔼t,x,y,y¯​[gy¯​(T,XTπ^,YT)]=𝔼t,x,y,y¯​[uγ​(YT)​(XTπ^)],g^{\overline{y}}\left(t,x,y\right)=\mathbb{E}\_{t,x,y,\overline{y}}\left[g^{\overline{y}}\left(T,X^{\widehat{\pi}}\_{T},Y\_{T}\right)\right]=\mathbb{E}\_{t,x,y,\overline{y}}\left[u^{\gamma(Y\_{T})}\left(X^{\widehat{\pi}}\_{T}\right)\right], |  |

which proves (R1).

Proof of (R2). Plugging π^\widehat{\pi} in ([S​1S1](https://arxiv.org/html/2512.21149v1#S3.Ex25 "In The extended HJB system. ‣ 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | =𝒟π^​V​(t,x,y)−𝒟π^​∫𝒴φy¯​(gy¯​(t,x,y))​𝑑FYT​(y¯;t,y)\displaystyle=\mathcal{D}^{\widehat{\pi}}V(t,x,y)-\mathcal{D}^{\widehat{\pi}}\int\_{\mathcal{Y}}\varphi^{\overline{y}}\left(g^{\overline{y}}\left(t,x,y\right)\right)dF\_{Y\_{T}}(\overline{y};t,y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫𝒴(φy¯)′​(gy¯​(t,x,y))​𝒟¯π^​gy¯​(t,x,y)​𝑑FYT​(y¯;t,y).\displaystyle\qquad\qquad\qquad+\int\_{\mathcal{Y}}\left(\varphi^{\overline{y}}\right)^{\prime}\left(g^{\overline{y}}\left(t,x,y\right)\right)\,\overline{\mathcal{D}}^{\widehat{\pi}}g^{\overline{y}}\left(t,x,y\right)\,dF\_{Y\_{T}}(\overline{y};t,y). |  |

Since ([S​2S2](https://arxiv.org/html/2512.21149v1#S3.Ex26 "In The extended HJB system. ‣ 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")) holds, the last term in the above PDE is zero. Thus,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒟π^​V​(t,x,y)=𝒟π^​∫𝒴φy¯​(gy¯​(t,x,y))​𝑑FYT​(y¯;t,y).\mathcal{D}^{\widehat{\pi}}V(t,x,y)=\mathcal{D}^{\widehat{\pi}}\int\_{\mathcal{Y}}\varphi^{\overline{y}}\left(g^{\overline{y}}\left(t,x,y\right)\right)dF\_{Y\_{T}}(\overline{y};t,y). |  | (A.3) |

Due to (C3), V∈𝒞1,2,2​(𝒯×𝒳×𝒴)V\in\mathcal{C}^{1,2,2}\left(\mathcal{T}\times\mathcal{X}\times\mathcal{Y}\right). Applying Itô’s lemma to V​(t,Xtπ^,Yt)V(t,X^{\widehat{\pi}}\_{t},Y\_{t}) on [t,T][t,T] under the measure ℙt,x,y\mathbb{P}\_{t,x,y}, and then taking the expectation on both sides of the equality, we derive that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼t,x,y\displaystyle\mathbb{E}\_{t,x,y} | [V​(T,XTπ^,YT)]=V​(t,x,y)+𝔼t,x,y​[∫tT𝒟π^​V​(s,Xsπ^,Ys)​𝑑s]\displaystyle\left[V(T,X^{\widehat{\pi}}\_{T},Y\_{T})\right]=V(t,x,y)+\mathbb{E}\_{t,x,y}\left[\int\limits\_{t}^{T}\mathcal{D}^{\widehat{\pi}}V(s,X^{\widehat{\pi}}\_{s},Y\_{s})\,ds\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝔼t,x,y​[∫tT∂xV​(s,Xsπ^,Ys)​π^​(s)​σS​(ρ​d​Bs1+1−ρ2​d​Bs2)]\displaystyle+\mathbb{E}\_{t,x,y}\left[\int\limits\_{t}^{T}\partial\_{x}V(s,X^{\widehat{\pi}}\_{s},Y\_{s})\widehat{\pi}(s)\sigma\_{S}\left(\rho dB^{1}\_{s}+\sqrt{1-\rho^{2}}dB^{2}\_{s}\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝔼t,x,y​[∫tT∂yV​(s,Xsπ^,Ys)​σY​d​Bs1]\displaystyle+\mathbb{E}\_{t,x,y}\left[\int\limits\_{t}^{T}\partial\_{y}V(s,X^{\widehat{\pi}}\_{s},Y\_{s})\sigma\_{Y}dB^{1}\_{s}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(C​4)V​(t,x,y)+𝔼t,x,y​[∫tT𝒟π^​V​(s,Xsπ^,Ys)​𝑑s]\displaystyle\mathrel{{\mathop{=}\limits^{(C4)}}}V(t,x,y)+\mathbb{E}\_{t,x,y}\left[\int\limits\_{t}^{T}\mathcal{D}^{\widehat{\pi}}V(s,X^{\widehat{\pi}}\_{s},Y\_{s})\,ds\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =([A.3](https://arxiv.org/html/2512.21149v1#A1.E3 "In A.2 Proof of Theorem 3.5 ‣ Appendix A Proofs ‣ Equilibrium investment under dynamic preference uncertainty"))V​(t,x,y)+𝔼t,x,y​[∫tT𝒟π^​(∫𝒴φy¯​(gy¯​(s,Xsπ^,Ys))​𝑑FYT​(y¯;s,Ys))​𝑑s].\displaystyle\mathrel{{\mathop{=}\limits^{\eqref{eq:equal\_terms\_in\_HJB\_PDE}}}}V(t,x,y)+\mathbb{E}\_{t,x,y}\left[\int\limits\_{t}^{T}\mathcal{D}^{\widehat{\pi}}\left(\int\_{\mathcal{Y}}\varphi^{\overline{y}}\left(g^{\overline{y}}\left(s,X^{\widehat{\pi}}\_{s},Y\_{s}\right)\right)dF\_{Y\_{T}}\left(\overline{y};s,Y\_{s}\right)\right)ds\right]. |  |

Using the notation for G∞​(t,x,y)G\_{\infty}(t,x,y) in ([3.13](https://arxiv.org/html/2512.21149v1#S3.E13 "In 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")),
we consider the process

|  |  |  |
| --- | --- | --- |
|  | G∞​(s,Xsπ^,Ys)=∫𝒴φy¯​(gy¯​(s,Xsπ^,Ys))​𝑑FYT​(y¯;s,Ys).G\_{\infty}(s,X^{\widehat{\pi}}\_{s},Y\_{s})=\int\_{\mathcal{Y}}\varphi^{\overline{y}}\left(g^{\overline{y}}\left(s,X^{\widehat{\pi}}\_{s},Y\_{s}\right)\right)dF\_{Y\_{T}}\left(\overline{y};s,Y\_{s}\right). |  |

Due to (C3), G∞∈𝒞1,2,2​(𝒯×𝒳×𝒴)G\_{\infty}\in\mathcal{C}^{1,2,2}\left(\mathcal{T}\times\mathcal{X}\times\mathcal{Y}\right). Applying Itô’s lemma to G∞G\_{\infty} under ℙt,x,y\mathbb{P}\_{t,x,y}, taking the expectation and using that G∞∈ℒ2​(Xπ^,Y)G\_{\infty}\in\mathcal{L}^{2}\left(X^{\widehat{\pi}},Y\right) (again by (C4)), we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼t,x,y\displaystyle\mathbb{E}\_{t,x,y} | [G∞​(T,XTπ^,YT)]−𝔼t,x,y​[G∞​(t,Xtπ^,Yt)]\displaystyle\left[G\_{\infty}(T,X^{\widehat{\pi}}\_{T},Y\_{T})\right]-\mathbb{E}\_{t,x,y}\left[G\_{\infty}(t,X^{\widehat{\pi}}\_{t},Y\_{t})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼t,x,y​[∫tT𝒟π^​(∫𝒴φy¯​(gy¯​(s,Xsπ^,Ys))​𝑑FYT​(y¯;s,Ys))​𝑑s].\displaystyle=\mathbb{E}\_{t,x,y}\left[\int\limits\_{t}^{T}\mathcal{D}^{\widehat{\pi}}\left(\int\_{\mathcal{Y}}\varphi^{\overline{y}}\left(g^{\overline{y}}\left(s,X^{\widehat{\pi}}\_{s},Y\_{s}\right)\right)dF\_{Y\_{T}}\left(\overline{y};s,Y\_{s}\right)\right)ds\right]. |  |

Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼t,x,y​[V​(T,XTπ^,YT)]\displaystyle\mathbb{E}\_{t,x,y}\left[V(T,X^{\widehat{\pi}}\_{T},Y\_{T})\right] | =V​(t,x,y)+𝔼t,x,y​[G∞​(T,XTπ^,YT)]−G∞​(t,Xtπ^,Yt).\displaystyle=V(t,x,y)+\mathbb{E}\_{t,x,y}\left[G\_{\infty}(T,X^{\widehat{\pi}}\_{T},Y\_{T})\right]-G\_{\infty}(t,X^{\widehat{\pi}}\_{t},Y\_{t}). |  |

Due to ([S​3S3](https://arxiv.org/html/2512.21149v1#S3.Ex27 "In The extended HJB system. ‣ 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")) and ([S​4S4](https://arxiv.org/html/2512.21149v1#S3.Ex28 "In The extended HJB system. ‣ 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")),
𝔼t,x,y​[V​(T,XTπ^,YT)]=𝔼t,x,y​[G∞​(T,XTπ^,YT)]\mathbb{E}\_{t,x,y}\left[V(T,X^{\widehat{\pi}}\_{T},Y\_{T})\right]=\mathbb{E}\_{t,x,y}\left[G\_{\infty}(T,X^{\widehat{\pi}}\_{T},Y\_{T})\right]. Thus,

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t,x,y)\displaystyle V(t,x,y) | =G∞​(t,x,y)=∫𝒴φy¯​(gy¯​(t,x,y))​𝑑FYT​(y¯;t,y)\displaystyle=G\_{\infty}(t,x,y)=\int\_{\mathcal{Y}}\varphi^{\overline{y}}\left(g^{\overline{y}}\left(t,x,y\right)\right)dF\_{Y\_{T}}\left(\overline{y};t,y\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(R​1)∫𝒴φy¯​(𝔼t,x,y,y¯​[uγ​(YT)​(XTπ^)])​𝑑FYT​(y¯;t,y)\displaystyle\mathrel{{\mathop{=}\limits^{(R1)}}}\int\_{\mathcal{Y}}\varphi^{\overline{y}}\left(\mathbb{E}\_{t,x,y,\overline{y}}\left[u^{\gamma(Y\_{T})}\left(X^{\widehat{\pi}}\_{T}\right)\right]\right)dF\_{Y\_{T}}\left(\overline{y};t,y\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼t,x,y​[v∘(uγ​(YT))−1​(𝔼t,x,y,y¯​[uγ​(YT)​(XTπ)])]\displaystyle=\mathbb{E}\_{t,x,y}\left[v\circ\left(u^{\gamma(Y\_{T})}\right)^{-1}\left(\mathbb{E}\_{t,x,y,\overline{y}}\left[u^{\gamma(Y\_{T})}(X^{\pi}\_{T})\right]\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =([2.3](https://arxiv.org/html/2512.21149v1#S2.E3 "In 2 Problem formulation ‣ Equilibrium investment under dynamic preference uncertainty"))Jπ​(t,x,y),\displaystyle\mathrel{{\mathop{=}\limits^{\eqref{eq:reward\_functional}}}}J^{\pi}(t,x,y), |  |

which proves (R2).

Proof of (R3). First, we derive a recursive representation of gy¯​(t,x,y)g^{\overline{y}}\left(t,x,y\right) and Jπδ​(t,x,y)J^{\pi\_{\delta}}(t,x,y) for an arbitrary but fixed πδ\pi\_{\delta}. Similarly to ([A.2](https://arxiv.org/html/2512.21149v1#A1.E2 "In A.2 Proof of Theorem 3.5 ‣ Appendix A Proofs ‣ Equilibrium investment under dynamic preference uncertainty")), under the measure ℙt,x,y,y¯\mathbb{P}\_{t,x,y,\overline{y}}, we can apply Itô’s lemma to the process gy¯​(s,Xsπδ,Ys)g^{\overline{y}}\left(s,X^{\pi\_{\delta}}\_{s},Y\_{s}\right) on the time interval [t+δ,T][t+\delta,T]:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | gy¯​(T,XTπδ,YT)\displaystyle g^{\overline{y}}\left(T,X^{\pi\_{\delta}}\_{T},Y\_{T}\right) | =gy¯​(t+δ,Xπδ​(t+δ),Y​(t+δ))+∫t+δTD¯πδ​gy¯​(s,Xsπδ,Ys)​𝑑s\displaystyle=g^{\overline{y}}\left(t+\delta,X^{\pi\_{\delta}}(t+\delta),Y(t+\delta)\right)+\int\limits\_{t+\delta}^{T}\overline{D}^{\pi\_{\delta}}g^{\overline{y}}\left(s,X^{\pi\_{\delta}}\_{s},Y\_{s}\right)\,ds |  | (A.4) |
|  |  | +∫t+δT∂xgy¯​(s,Xsπδ,Ys)​πδ​(s)​σS​(ρ​d​B¯s1+1−ρ2​d​B¯s2)\displaystyle\quad+\int\limits\_{t+\delta}^{T}\partial\_{x}g^{\overline{y}}\left(s,X^{\pi\_{\delta}}\_{s},Y\_{s}\right)\pi\_{\delta}(s)\sigma\_{S}\left(\rho d\overline{B}^{1}\_{s}+\sqrt{1-\rho^{2}}d\overline{B}^{2}\_{s}\right) |  |
|  |  | +∫t+δT∂ygy¯​(s,Xsπδ,Ys)​σY​d​B¯s1.\displaystyle\quad+\int\limits\_{t+\delta}^{T}\partial\_{y}g^{\overline{y}}\left(s,X^{\pi\_{\delta}}\_{s},Y\_{s}\right)\sigma\_{Y}d\overline{B}^{1}\_{s}. |  |

Taking the expectation and using πδ​(s)=π^​(s)\pi\_{\delta}(s)=\widehat{\pi}(s) , for every s∈[t+δ,T]s\in[t+\delta,T], together with assumptions (C2) and (C4), we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼t,x,y,y¯​[gy¯​(t+δ,Xπδ​(t+δ),Y​(t+δ))]=𝔼t,x,y,y¯​[uγ​(y¯)​(XTπδ)].\mathbb{E}\_{t,x,y,\overline{y}}\left[g^{\overline{y}}\left(t+\delta,X^{\pi\_{\delta}}(t+\delta),Y(t+\delta)\right)\right]=\mathbb{E}\_{t,x,y,\overline{y}}\left[u^{\gamma(\overline{y})}\left(X^{\pi\_{\delta}}\_{T}\right)\right]. |  | (A.5) |

Furthermore, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jπδ​(t,x,y)\displaystyle J^{\pi\_{\delta}}(t,x,y) | =([3.2](https://arxiv.org/html/2512.21149v1#S3.E2 "In 3.1 Preliminary definitions and state process dynamics under conditional measures ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty"))∫𝒴φy¯​(𝔼t,x,y,y¯​[uγ​(y¯)​(XTπδ)])​𝑑FYT​(y¯;t,y)\displaystyle\mathrel{{\mathop{=}\limits^{\eqref{eq:reward\_functional\_explicit}}}}\int\_{\mathcal{Y}}\varphi^{\overline{y}}\left(\mathbb{E}\_{t,x,y,\overline{y}}\left[u^{\gamma(\overline{y})}\left(X^{\pi\_{\delta}}\_{T}\right)\right]\right)\,dF\_{Y\_{T}}(\overline{y};t,y) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫𝒴φy¯​(𝔼t,x,y,y¯​[uγ​(y¯)​(XTπδ)])​𝑑FYT​(y¯;t,y)\displaystyle=\int\_{\mathcal{Y}}\varphi^{\overline{y}}\left(\mathbb{E}\_{t,x,y,\overline{y}}\left[u^{\gamma(\overline{y})}\left(X^{\pi\_{\delta}}\_{T}\right)\right]\right)\,dF\_{Y\_{T}}(\overline{y};t,y) |  | (A.6) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +V​(t+δ,Xπδ​(t+δ),Y​(t+δ))−Jπδ​(t+δ,Xπδ​(t+δ),Y​(t+δ)),\displaystyle\quad+V(t+\delta,X^{\pi\_{\delta}}(t+\delta),Y(t+\delta))-J^{\pi\_{\delta}}(t+\delta,X^{\pi\_{\delta}}(t+\delta),Y(t+\delta)), |  |

where the difference between the last two terms is zero due to πδ​(s)=π^​(s),s∈[t+δ,T]\pi\_{\delta}(s)=\widehat{\pi}(s),s\in[t+\delta,T]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jπδ​(t+δ,Xπδ​(t+δ),Y​(t+δ))\displaystyle J^{\pi\_{\delta}}(t+\delta,X^{\pi\_{\delta}}(t+\delta),Y(t+\delta)) | =Jπ^​(t+δ,Xπδ​(t+δ),Y​(t+δ))\displaystyle\;=J^{\widehat{\pi}}(t+\delta,X^{\pi\_{\delta}}(t+\delta),Y(t+\delta)) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(R2)V​(t+δ,Xπδ​(t+δ),Y​(t+δ)).\displaystyle\mathrel{{\mathop{=}\limits^{\textit{(R2)}}}}V(t+\delta,X^{\pi\_{\delta}}(t+\delta),Y(t+\delta)). |  |

Taking the expectation under the measure ℙt,x,y\mathbb{P}\_{t,x,y} in ([A.6](https://arxiv.org/html/2512.21149v1#A1.E6 "In A.2 Proof of Theorem 3.5 ‣ Appendix A Proofs ‣ Equilibrium investment under dynamic preference uncertainty")) yields

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Jπδ​(t,x,y)\displaystyle J^{\pi\_{\delta}}(t,x,y) | =∫𝒴φy¯​(𝔼t,x,y,y¯​[uγ​(y¯)​(XTπδ)])​𝑑FYT​(y¯;t,y)\displaystyle=\int\_{\mathcal{Y}}\varphi^{\overline{y}}\left(\mathbb{E}\_{t,x,y,\overline{y}}\left[u^{\gamma(\overline{y})}\left(X^{\pi\_{\delta}}\_{T}\right)\right]\right)\,dF\_{Y\_{T}}(\overline{y};t,y) |  | (A.7) |
|  |  | +𝔼t,x,y​[V​(t+δ,Xπδ​(t+δ),Y​(t+δ))]\displaystyle\quad+\mathbb{E}\_{t,x,y}\left[V(t+\delta,X^{\pi\_{\delta}}(t+\delta),Y(t+\delta))\right] |  |
|  |  | −𝔼t,x,y​[Jπδ​(t+δ,Xπδ​(t+δ),Y​(t+δ))].\displaystyle\quad-\mathbb{E}\_{t,x,y}\left[J^{\pi\_{\delta}}(t+\delta,X^{\pi\_{\delta}}(t+\delta),Y(t+\delta))\right]. |  |

Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jπ^​(t,x,y)−Jπδ​(t,x,y)\displaystyle J^{\widehat{\pi}}(t,x,y)-J^{\pi\_{\delta}}(t,x,y) | =([A.7](https://arxiv.org/html/2512.21149v1#A1.E7 "In A.2 Proof of Theorem 3.5 ‣ Appendix A Proofs ‣ Equilibrium investment under dynamic preference uncertainty"))+(R2)V​(t,x,y)−𝔼t,x,y​[V​(t+δ,Xπδ​(t+δ),Y​(t+δ))]\displaystyle\mathrel{{\mathop{=}\limits^{\eqref{eq:R3\_proof\_J\_pih\_recursion\_after\_E}+\textit{(R2)}}}}V(t,x,y)-\mathbb{E}\_{t,x,y}\left[V(t+\delta,X^{\pi\_{\delta}}(t+\delta),Y(t+\delta))\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫𝒴φy¯​(𝔼t,x,y,y¯​[uγ​(y¯)​(XTπδ)])​𝑑FYT​(y¯;t,y)\displaystyle\quad-\int\_{\mathcal{Y}}\varphi^{\overline{y}}\left(\mathbb{E}\_{t,x,y,\overline{y}}\left[u^{\gamma(\overline{y})}\left(X^{\pi\_{\delta}}\_{T}\right)\right]\right)\,dF\_{Y\_{T}}(\overline{y};t,y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝔼t,x,y​[Jπδ​(t+δ,Xπδ​(t+δ),Y​(t+δ))]\displaystyle\quad+\mathbb{E}\_{t,x,y}\left[J^{\pi\_{\delta}}(t+\delta,X^{\pi\_{\delta}}(t+\delta),Y(t+\delta))\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−(𝔼t,x,y​[V​(t+δ,Xπδ​(t+δ),Y​(t+δ))]−V​(t,x,y))\displaystyle=-\left(\mathbb{E}\_{t,x,y}\left[V(t+\delta,X^{\pi\_{\delta}}(t+\delta),Y(t+\delta))\right]-V(t,x,y)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −(∫𝒴φy¯(𝔼t,x,y,y¯[gy¯(t+δ,Xπδ(t+δ),Y(t+δ))])dFYT(y¯;t,y)\displaystyle\quad-\Bigl(\int\_{\mathcal{Y}}\varphi^{\overline{y}}\left(\mathbb{E}\_{t,x,y,\overline{y}}\left[g^{\overline{y}}\left(t+\delta,X^{\pi\_{\delta}}(t+\delta),Y(t+\delta)\right)\right]\right)\,dF\_{Y\_{T}}(\overline{y};t,y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫𝒴φy¯(gy¯(t,x,y))dFYT(y¯;t,y))\displaystyle\quad\quad-\int\_{\mathcal{Y}}\varphi^{\overline{y}}\left(g^{\overline{y}}\left(t,x,y\right)\right)\,dF\_{Y\_{T}}(\overline{y};t,y)\Bigr) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(𝔼t,x,y[Jπδ(t+δ,Xπδ(t+δ),Y(t+δ))]\displaystyle\quad+\Bigl(\mathbb{E}\_{t,x,y}\left[J^{\pi\_{\delta}}(t+\delta,X^{\pi\_{\delta}}(t+\delta),Y(t+\delta))\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫𝒴φy¯(gy¯(t,x,y))dFYT(y¯;t,y))\displaystyle\quad\quad-\int\_{\mathcal{Y}}\varphi^{\overline{y}}\left(g^{\overline{y}}\left(t,x,y\right)\right)\,dF\_{Y\_{T}}(\overline{y};t,y)\Bigr) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =:−Δ1(δ)−Δ2(δ)+Δ3(δ),\displaystyle=:-\Delta\_{1}(\delta)-\Delta\_{2}(\delta)+\Delta\_{3}(\delta), |  | (A.8) |

where in the second equality we add and subtract the same term and use ([A.5](https://arxiv.org/html/2512.21149v1#A1.E5 "In A.2 Proof of Theorem 3.5 ‣ Appendix A Proofs ‣ Equilibrium investment under dynamic preference uncertainty")) for 𝔼t,x,y,y¯​[uγ​(y¯)​(XTπδ)]\mathbb{E}\_{t,x,y,\overline{y}}\left[u^{\gamma(\overline{y})}\left(X^{\pi\_{\delta}}\_{T}\right)\right].

To prove that π^\widehat{\pi} is an equilibrium control according to Definition [2.4](https://arxiv.org/html/2512.21149v1#S2.Thmtheorem4 "Definition 2.4 (Equilibrium control law; cf. Def. 15.3 in BjoerkKhapkoMurgoci2021:TICT). ‣ 2 Problem formulation ‣ Equilibrium investment under dynamic preference uncertainty"), we need to compute the following limit:

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim infδ↓0\displaystyle\liminf\_{\delta\downarrow 0} | Jπ^​(t,x,y)−Jπδ​(t,x,y)δ=([A.8](https://arxiv.org/html/2512.21149v1#A1.E8 "In A.2 Proof of Theorem 3.5 ‣ Appendix A Proofs ‣ Equilibrium investment under dynamic preference uncertainty"))lim infδ↓01δ​(−Δ1​(δ)−Δ2​(δ)+Δ3​(δ))\displaystyle\frac{J^{\hat{\pi}}(t,x,y)-J^{\pi\_{\delta}}(t,x,y)}{\delta}\mathrel{{\mathop{=}\limits^{\eqref{eq:R3\_proof\_def\_delta\_terms}}}}\liminf\_{\delta\downarrow 0}\frac{1}{\delta}\left(-\Delta\_{1}(\delta)-\Delta\_{2}(\delta)+\Delta\_{3}(\delta)\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−(lim supδ↓01δ​Δ1​(δ)+lim supδ↓01δ​Δ2​(δ)−lim infδ↓01δ​Δ3​(δ)),\displaystyle=-\left(\limsup\_{\delta\downarrow 0}\frac{1}{\delta}\Delta\_{1}(\delta)+\limsup\_{\delta\downarrow 0}\frac{1}{\delta}\Delta\_{2}(\delta)-\liminf\_{\delta\downarrow 0}\frac{1}{\delta}\Delta\_{3}(\delta)\right), |  | (A.9) |

where we use the linearity of the limit and the relation between lim sup\limsup and lim inf\liminf.

Using standard arguments, we can show that

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim supδ↓01δ​Δ1​(δ)=𝒟π​V​(t,x,y).\limsup\_{\delta\downarrow 0}\frac{1}{\delta}\Delta\_{1}(\delta)=\mathcal{D}^{\pi}V(t,x,y). |  | (A.10) |

Furthermore, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim supδ↓0\displaystyle\limsup\_{\delta\downarrow 0} | 1δΔ2(δ)=lim supδ↓01δ(∫𝒴φy¯(𝔼t,x,y,y¯[gy¯(t+δ,Xπδ(t+δ),Y(t+δ))])dFYT(y¯;t,y)\displaystyle\frac{1}{\delta}\Delta\_{2}(\delta)=\limsup\_{\delta\downarrow 0}\frac{1}{\delta}\Biggl(\int\_{\mathcal{Y}}\varphi^{\overline{y}}\left(\mathbb{E}\_{t,x,y,\overline{y}}\left[g^{\overline{y}}\left(t+\delta,X^{\pi\_{\delta}}(t+\delta),Y(t+\delta)\right)\right]\right)\,dF\_{Y\_{T}}(\overline{y};t,y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫𝒴φy¯(gy¯(t,x,y))dFYT(y¯;t,y))\displaystyle\quad\quad-\int\_{\mathcal{Y}}\varphi^{\overline{y}}\left(g^{\overline{y}}\left(t,x,y\right)\right)\,dF\_{Y\_{T}}(\overline{y};t,y)\Biggr) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫𝒴lim supδ↓01δ(φy¯(𝔼t,x,y,y¯[gy¯(t+δ,Xπδ(t+δ),Y(t+δ))])\displaystyle=\int\_{\mathcal{Y}}\limsup\_{\delta\downarrow 0}\frac{1}{\delta}\Biggl(\varphi^{\overline{y}}\left(\mathbb{E}\_{t,x,y,\overline{y}}\left[g^{\overline{y}}\left(t+\delta,X^{\pi\_{\delta}}(t+\delta),Y(t+\delta)\right)\right]\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −φy¯(gy¯(t,x,y)))dFYT(y¯;t,y)\displaystyle\quad\quad-\varphi^{\overline{y}}\left(g^{\overline{y}}\left(t,x,y\right)\right)\Biggr)\,dF\_{Y\_{T}}(\overline{y};t,y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫𝒴lim supδ↓0(φy¯​(𝔼t,x,y,y¯​[gy¯​(t+δ,Xπδ​(t+δ),Y​(t+δ))])−φy¯​(gy¯​(t,x,y))𝔼t,x,y,y¯​[gy¯​(t+δ,Xπδ​(t+δ),Y​(t+δ))]−gy¯​(t,x,y)\displaystyle=\int\_{\mathcal{Y}}\limsup\_{\delta\downarrow 0}\Biggl(\frac{\varphi^{\overline{y}}\left(\mathbb{E}\_{t,x,y,\overline{y}}\left[g^{\overline{y}}\left(t+\delta,X^{\pi\_{\delta}}(t+\delta),Y(t+\delta)\right)\right]\right)-\varphi^{\overline{y}}\left(g^{\overline{y}}\left(t,x,y\right)\right)}{\mathbb{E}\_{t,x,y,\overline{y}}\left[g^{\overline{y}}\left(t+\delta,X^{\pi\_{\delta}}(t+\delta),Y(t+\delta)\right)\right]-g^{\overline{y}}\left(t,x,y\right)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⋅𝔼t,x,y,y¯​[gy¯​(t+δ,Xπδ​(t+δ),Y​(t+δ))]−gy¯​(t,x,y)δ)dFYT(y¯;t,y)\displaystyle\quad\quad\cdot\frac{\mathbb{E}\_{t,x,y,\overline{y}}\left[g^{\overline{y}}\left(t+\delta,X^{\pi\_{\delta}}(t+\delta),Y(t+\delta)\right)\right]-g^{\overline{y}}\left(t,x,y\right)}{\delta}\Biggr)\,dF\_{Y\_{T}}(\overline{y};t,y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫𝒴(φy¯)′​(gy¯​(t,x,y))​𝒟¯π​gy¯​(t,x,y)​𝑑FYT​(y¯;t,y)\displaystyle=\int\_{\mathcal{Y}}\left(\varphi^{\overline{y}}\right)^{\prime}\left(g^{\overline{y}}\left(t,x,y\right)\right)\,\overline{\mathcal{D}}^{\pi}g^{\overline{y}}\left(t,x,y\right)\,dF\_{Y\_{T}}(\overline{y};t,y) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =([3.14](https://arxiv.org/html/2512.21149v1#S3.E14 "In 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty"))ℋ¯π​((gy¯)y¯∈𝒴)​(t,x,y),\displaystyle\hskip-5.69046pt\mathrel{{\mathop{=}\limits^{\eqref{eq:barH\_pi}}}}\overline{\mathcal{H}}^{\pi}\left(\left(g^{\overline{y}}\right)\_{\overline{y}\in\mathcal{Y}}\right)(t,x,y), |  | (A.11) |

where in the second equality we use regularity conditions (C4) to exchange lim inf\liminf and integral, in the third equality we multiply and divide by the same non-zero term, and in the fourth equality we use the definition of a derivative for the first term, the definition of the differential operator under ℙt,x,y,y¯\mathbb{P}\_{t,x,y,\overline{y}}, the assumption that φy¯\varphi^{\overline{y}} is differentiable, the condition that gy¯∈ℒ¯2​(Xπ,Y)g^{\overline{y}}\in\overline{\mathcal{L}}^{2}(X^{\pi},Y) as per (C4), and the product rule for limits.

Finally, observing that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jπδ\displaystyle J^{\pi\_{\delta}} | (t+δ,Xπδ​(t+δ),Y​(t+δ))\displaystyle(t+\delta,X^{\pi\_{\delta}}(t+\delta),Y(t+\delta)) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =([3.2](https://arxiv.org/html/2512.21149v1#S3.E2 "In 3.1 Preliminary definitions and state process dynamics under conditional measures ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty"))∫𝒴φy¯​(𝔼t+δ,Xπδ​(t+δ),Y​(t+δ),y¯​[uγ​(y¯)​(XTπ)])​𝑑FYT​(y¯;t+δ,Y​(t+δ))\displaystyle\mathrel{{\mathop{=}\limits^{\eqref{eq:reward\_functional\_explicit}}}}\int\_{\mathcal{Y}}\varphi^{\overline{y}}\left(\mathbb{E}\_{t+\delta,X^{\pi\_{\delta}}(t+\delta),Y(t+\delta),\overline{y}}\left[u^{\gamma(\overline{y})}\left(X^{\pi}\_{T}\right)\right]\right)\,dF\_{Y\_{T}}(\overline{y};t+\delta,Y(t+\delta)) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(R​1)∫𝒴φy¯​(gy¯​(t+δ,Xπδ​(t+δ),Y​(t+δ)))​𝑑FYT​(y¯;t+δ,Y​(t+δ))\displaystyle\mathrel{{\mathop{=}\limits^{(R1)}}}\int\_{\mathcal{Y}}\varphi^{\overline{y}}\left(g^{\overline{y}}\left(t+\delta,X^{\pi\_{\delta}}(t+\delta),Y(t+\delta)\right)\right)\,dF\_{Y\_{T}}(\overline{y};t+\delta,Y(t+\delta)) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =([3.13](https://arxiv.org/html/2512.21149v1#S3.E13 "In 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty"))G∞​(t+δ,Xπδ​(t+δ),Y​(t+δ)),\displaystyle\mathrel{{\mathop{=}\limits^{\eqref{eq:G\_infty}}}}G\_{\infty}(t+\delta,X^{\pi\_{\delta}}(t+\delta),Y(t+\delta)), |  |

we compute

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim infδ↓01δ​Δ3​(δ)\displaystyle\liminf\_{\delta\downarrow 0}\frac{1}{\delta}\Delta\_{3}(\delta) | =lim infδ↓01δ(𝔼t,x,y[Jπδ(t+δ,Xπδ(t+δ),Y(t+δ))]\displaystyle=\liminf\_{\delta\downarrow 0}\frac{1}{\delta}\Biggl(\mathbb{E}\_{t,x,y}\left[J^{\pi\_{\delta}}(t+\delta,X^{\pi\_{\delta}}(t+\delta),Y(t+\delta))\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫𝒴φy¯(gy¯(t,x,y))dFYT(y¯;t,y))\displaystyle\quad\quad-\int\_{\mathcal{Y}}\varphi^{\overline{y}}\left(g^{\overline{y}}\left(t,x,y\right)\right)\,dF\_{Y\_{T}}(\overline{y};t,y)\Biggr) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =([3.13](https://arxiv.org/html/2512.21149v1#S3.E13 "In 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty"))lim infδ↓01δ​(𝔼t,x,y​[G∞​(t+δ,Xπδ​(t+δ),Y​(t+δ))]−G∞​(t,x,y))\displaystyle\mathrel{{\mathop{=}\limits^{\eqref{eq:G\_infty}}}}\liminf\_{\delta\downarrow 0}\frac{1}{\delta}\Biggl(\mathbb{E}\_{t,x,y}\left[G\_{\infty}(t+\delta,X^{\pi\_{\delta}}(t+\delta),Y(t+\delta))\right]-G\_{\infty}(t,x,y)\Biggr) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =𝒟π​G∞​(t,x,y).\displaystyle\mathrel{{\mathop{=}\limits}}\mathcal{D}^{\pi}G\_{\infty}(t,x,y). |  | (A.12) |

Using ([A.8](https://arxiv.org/html/2512.21149v1#A1.E8 "In A.2 Proof of Theorem 3.5 ‣ Appendix A Proofs ‣ Equilibrium investment under dynamic preference uncertainty")) and the convergence results in ([A.10](https://arxiv.org/html/2512.21149v1#A1.E10 "In A.2 Proof of Theorem 3.5 ‣ Appendix A Proofs ‣ Equilibrium investment under dynamic preference uncertainty"))-([A.12](https://arxiv.org/html/2512.21149v1#A1.E12 "In A.2 Proof of Theorem 3.5 ‣ Appendix A Proofs ‣ Equilibrium investment under dynamic preference uncertainty")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim infδ↓0\displaystyle\liminf\_{\delta\downarrow 0}\, | Jπ^​(t,x,y)−Jπδ​(t,x,y)δ\displaystyle\frac{J^{\hat{\pi}}(t,x,y)-J^{\pi\_{\delta}}(t,x,y)}{\delta} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−(lim supδ↓01δ​Δ1​(δ)+lim supδ↓01δ​Δ2​(δ)−lim infδ↓01δ​Δ3​(δ))\displaystyle=-\left(\limsup\_{\delta\downarrow 0}\frac{1}{\delta}\Delta\_{1}(\delta)+\limsup\_{\delta\downarrow 0}\frac{1}{\delta}\Delta\_{2}(\delta)-\liminf\_{\delta\downarrow 0}\frac{1}{\delta}\Delta\_{3}(\delta)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−(𝒟π​V​(t,x,y)+ℋ¯π​((gy¯)y¯∈𝒴)​(t,x,y)−𝒟π​G∞​(t,x,y))\displaystyle=-\left(\mathcal{D}^{\pi}V(t,x,y)+\overline{\mathcal{H}}^{\pi}\left(\left(g^{\overline{y}}\right)\_{\overline{y}\in\mathcal{Y}}\right)(t,x,y)-\mathcal{D}^{\pi}G\_{\infty}(t,x,y)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥0,\displaystyle\geq 0, |  |

where the inequality follows from the fact that π^\widehat{\pi} realizes the supremum in ([S​1S1](https://arxiv.org/html/2512.21149v1#S3.Ex25 "In The extended HJB system. ‣ 3.2 Heuristic derivation of the eHJB ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")) as per (C1). Therefore, π^\widehat{\pi} is an equilibrium control, which proves (R3).

Proof of (R4).
We conclude that V​(t,x,y)V(t,x,y) is indeed the equilibrium value function, i.e., V^​(t,x,y)=V​(t,x,y)\widehat{V}(t,x,y)=V(t,x,y), since V​(t,x,y)=Jπ^​(t,x,y)V(t,x,y)=J^{\widehat{\pi}}(t,x,y) by (R2) and π^\widehat{\pi} is an equilibrium control by (R3). This proves (R4) and completes the proof of the verification theorem. ∎

### A.3 Proof of Corollary [4.1](https://arxiv.org/html/2512.21149v1#S4.Thmtheorem1 "Corollary 4.1. ‣ 4.1 Preference specification and equilibrium investment ‣ 4 Application: state-dependent CRRA utility ‣ Equilibrium investment under dynamic preference uncertainty")

First, it is straightforward to verify that

|  |  |  |
| --- | --- | --- |
|  | fYT​(y¯;t,y)=12​π​σY2​(T−t)​exp⁡(−(y¯−y−μY​(T−t))22​σY2​(T−t)).f\_{Y\_{T}}(\overline{y};t,y)=\frac{1}{\sqrt{2\uppi\sigma\_{Y}^{2}(T-t)}}\exp\left(-\frac{\left(\overline{y}-y-\mu\_{Y}(T-t)\right)^{2}}{2\sigma\_{Y}^{2}(T-t)}\right). |  |

(Note that π\uppi in the conditional PDF above denotes the mathematical constant pi, so it should not be confused with the control (investment strategy) denoted by π\pi.)

Thus, for YT|Ys=yY\_{T}|Y\_{s}=y, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂yln⁡(pY​(s,y;T,y¯))=∂yln⁡(12​π​σY2​(T−s)​exp⁡(−(y¯−(y+μY​(T−s)))22​σY2​(T−s)))=−y¯−(y+μY​(T−s))σY2​(T−s).\begin{split}\partial\_{y}\ln\big(p\_{Y}(s,y;T,\overline{y})\big)&=\partial\_{y}\ln\left(\frac{1}{\sqrt{2\uppi\sigma\_{Y}^{2}(T-s)}}\exp\left(-\frac{\left(\overline{y}-(y+\mu\_{Y}(T-s))\right)^{2}}{2\sigma\_{Y}^{2}(T-s)}\right)\right)\\ &=-\frac{\overline{y}-(y+\mu\_{Y}(T-s))}{\sigma\_{Y}^{2}(T-s)}.\end{split} |  | (A.13) |

Plugging this result in ([3.5](https://arxiv.org/html/2512.21149v1#S3.E5 "In 2nd item ‣ Lemma 3.1. ‣ 3.1 Preliminary definitions and state process dynamics under conditional measures ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")), we obtain the SDE for (Ys)s∈[t,T)\left(Y\_{s}\right)\_{s\in[t,T)} under the condition YT=y¯Y\_{T}=\overline{y}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Ys\displaystyle dY\_{s} | =(μY​d​s+σY2​(−y¯−(y+μY​(T−s))σY2​(T−s)))​d​s+σY​d​Bs1\displaystyle=\left(\mu\_{Y}ds+\sigma\_{Y}^{2}\left(-\frac{\overline{y}-(y+\mu\_{Y}(T-s))}{\sigma\_{Y}^{2}(T-s)}\right)\right)ds+\sigma\_{Y}dB^{1}\_{s} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =y¯−YsT−s​d​s+σY​d​B¯s1,\displaystyle=\frac{\overline{y}-Y\_{s}}{T-s}ds+\sigma\_{Y}d\overline{B}^{1}\_{s}, |  |

with Yt=yY\_{t}=y.

Similarly, inserting ([A.13](https://arxiv.org/html/2512.21149v1#A1.E13 "In A.3 Proof of Corollary 4.1 ‣ Appendix A Proofs ‣ Equilibrium investment under dynamic preference uncertainty")) into ([3.4](https://arxiv.org/html/2512.21149v1#S3.E4 "In 1st item ‣ Lemma 3.1. ‣ 3.1 Preliminary definitions and state process dynamics under conditional measures ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")), using that σY​(s,YS)=σY\sigma\_{Y}(s,Y\_{S})=\sigma\_{Y}, and simplifying, we obtain the SDE for (Xπ)s∈[t,T)(X^{\pi})\_{s\in[t,T)}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xsπ\displaystyle dX^{\pi}\_{s} | =Xsπ​(r+π​(s)​(μS−r)+π​(s)​ρ​σSσY​y¯−Ys−μY​(T−s)T−s)​d​s\displaystyle=X^{\pi}\_{s}\left(r+\pi(s)(\mu\_{S}-r)+\pi(s)\rho\frac{\sigma\_{S}}{\sigma\_{Y}}\frac{\overline{y}-Y\_{s}-\mu\_{Y}(T-s)}{T-s}\right)ds |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +Xsπ​π​(s)​σS​(ρ​d​B¯s1+1−ρ2​d​B¯s2),\displaystyle\qquad+X^{\pi}\_{s}\pi(s)\sigma\_{S}\left(\rho d\overline{B}^{1}\_{s}+\sqrt{1-\rho^{2}}d\overline{B}^{2}\_{s}\right), |  |

with Xtπ=xX^{\pi}\_{t}=x and XTπ=limt→TXtπX^{\pi}\_{T}=\lim\_{t\to T}X^{\pi}\_{t}.
∎

### A.4 Proof of Proposition [4.2](https://arxiv.org/html/2512.21149v1#S4.Thmtheorem2 "Proposition 4.2. ‣ 4.1 Preference specification and equilibrium investment ‣ 4 Application: state-dependent CRRA utility ‣ Equilibrium investment under dynamic preference uncertainty")

Recall our choice of the CRRA specification uy¯​(x)=11−γ​(y¯)​x1−γ​(y¯)u^{\overline{y}}(x)=\frac{1}{1-\gamma(\overline{y})}x^{1-\gamma(\overline{y})} and the aggregator v​(x)=ln⁡(x)v(x)=\ln(x). The inverse utility and certainty equivalent transform then satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | (uy¯)−1​(x)\displaystyle\left(u^{\overline{y}}\right)^{-1}(x) | =((1−γ​(y¯))​x)11−γ​(y¯),\displaystyle=\big(\left(1-\gamma(\overline{y})\right)x\big)^{\frac{1}{1-\gamma(\overline{y})}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | φy¯​(x)\displaystyle\varphi^{\overline{y}}(x) | =ln⁡(((1−γ​(y¯))​x)11−γ​(y¯))=11−γ​(y¯)​(ln⁡(1−γ​(y¯))+ln⁡(x)),\displaystyle=\ln\left(\big(\left(1-\gamma(\overline{y})\right)x\big)^{\frac{1}{1-\gamma(\overline{y})}}\right)=\frac{1}{1-\gamma(\overline{y})}\big(\ln\left(1-\gamma(\overline{y})\right)+\ln(x)\big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (φy¯)′​(x)\displaystyle\left(\varphi^{\overline{y}}\right)^{\prime}(x) | =1x​(1−γ​(y¯)).\displaystyle=\frac{1}{x\left(1-\gamma(\overline{y})\right)}. |  |

Using these expressions and the evolution of (Xπ,Y)(X^{\pi},Y), the in ([S​1¯\overline{S1}](https://arxiv.org/html/2512.21149v1#S3.Ex47 "In Corollary 3.6. ‣ 3.3 Verification results ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty"))-([S​3¯\overline{S3}](https://arxiv.org/html/2512.21149v1#S3.Ex49 "In Corollary 3.6. ‣ 3.3 Verification results ‣ 3 Derivation of equilibrium controls ‣ Equilibrium investment under dynamic preference uncertainty")) takes the form

|  |  |  |
| --- | --- | --- |
|  | 0=supπ∫𝒴1gy¯​(t,x,y)​(1−γ​(y¯))(∂tgy¯(t,x,y)+x​(r+π​(μS−r+ρ​σSσY​y¯−y−μY​(T−t)T−t))​∂xgy¯​(t,x,y)+y¯−yT−t​∂ygy¯​(t,x,y)+12​x2​π2​σS2​∂x​xgy¯​(t,x,y)+12​σY2​∂y​ygy¯​(t,x,y)+ρxπσSσY∂x​ygy¯(t,x,y))fYT(y¯;t,y)dy¯,0=∂tgy¯​(t,x,y)+x​(r+π^​(μS−r+ρ​σSσY​y¯−y−μY​(T−t)T−t))​∂xgy¯​(t,x,y)+y¯−yT−t​∂ygy¯​(t,x,y)+12​x2​π^2​σS2​∂x​xgy¯​(t,x,y)+12​σY2​∂y​ygy¯​(t,x,y)+ρ​x​π^​σS​σY​∂x​ygy¯​(t,x,y),uγ​(y¯)​(x)=gy¯​(T,x,y).\begin{split}&0=\sup\_{\pi}\int\_{\mathcal{Y}}\dfrac{1}{g^{\overline{y}}(t,x,y)(1-\gamma(\bar{y}))}\Bigg(\partial\_{t}g^{\overline{y}}(t,x,y)\Bigg.\\ &\hskip 56.9055pt+x\left(r+\pi\left(\mu\_{S}-r+\rho\dfrac{\sigma\_{S}}{\sigma\_{Y}}\dfrac{\bar{y}-y-\mu\_{Y}(T-t)}{T-t}\right)\right)\partial\_{x}g^{\overline{y}}(t,x,y)\\ &\hskip 56.9055pt+\dfrac{\bar{y}-y}{T-t}\partial\_{y}g^{\overline{y}}(t,x,y)+\dfrac{1}{2}x^{2}\pi^{2}\sigma\_{S}^{2}\partial\_{xx}g^{\overline{y}}(t,x,y)+\dfrac{1}{2}\sigma\_{Y}^{2}\partial\_{yy}g^{\overline{y}}(t,x,y)\\ &\hskip 56.9055pt\Bigg.+\rho x\pi\sigma\_{S}\sigma\_{Y}\partial\_{xy}g^{\overline{y}}(t,x,y)\Bigg)f\_{Y\_{T}}(\bar{y};t,y)d\bar{y},\\ &0=\partial\_{t}g^{\overline{y}}(t,x,y)+x\left(r+\widehat{\pi}\left(\mu\_{S}-r+\rho\dfrac{\sigma\_{S}}{\sigma\_{Y}}\dfrac{\bar{y}-y-\mu\_{Y}(T-t)}{T-t}\right)\right)\partial\_{x}g^{\overline{y}}(t,x,y)\\ &\qquad+\dfrac{\bar{y}-y}{T-t}\partial\_{y}g^{\overline{y}}(t,x,y)+\dfrac{1}{2}x^{2}\widehat{\pi}^{2}\sigma\_{S}^{2}\partial\_{xx}g^{\overline{y}}(t,x,y)+\dfrac{1}{2}\sigma\_{Y}^{2}\partial\_{yy}g^{\overline{y}}(t,x,y)\\ &\qquad+\rho x\widehat{\pi}\sigma\_{S}\sigma\_{Y}\partial\_{xy}g^{\overline{y}}(t,x,y),\\ u^{\gamma(\bar{y})}(x)&=g^{\overline{y}}(T,x,y).\end{split} |  |

The first order condition for π\pi gives

|  |  |  |
| --- | --- | --- |
|  | π^(t,x,y)=1σS2​x2∫𝒴1gy¯​(t,x,y)​(1−γ​(y¯))((−μS+r−ρσSσYy¯−y−μY​(T−t)T−t)∂xgy¯(t,x,y)−ρσSσY∂x​ygy¯(t,x,y))fYT(y¯;t,y)dy¯×(∫𝒴1gy¯​(t,x,y)​(1−γ​(y¯))​∂x​xgy¯​(t,x,y)​fYT​(y¯;t,y)​d​y¯)−1.\begin{split}&\widehat{\pi}(t,x,y)=\dfrac{1}{\sigma\_{S}^{2}x^{2}}\int\_{\mathcal{Y}}\dfrac{1}{g^{\overline{y}}(t,x,y)\big(1-\gamma(\bar{y})\big)}\bigg(\left(-\mu\_{S}+r-\rho\dfrac{\sigma\_{S}}{\sigma\_{Y}}\dfrac{\bar{y}-y-\mu\_{Y}(T-t)}{T-t}\right)\partial\_{x}g^{\overline{y}}(t,x,y)\bigg.\Bigg.\\ &\Bigg.\bigg.\hskip 113.81102pt-\rho\sigma\_{S}\sigma\_{Y}\partial\_{xy}g^{\overline{y}}(t,x,y)\bigg)f\_{Y\_{T}}(\bar{y};t,y)d\bar{y}\\ &\hskip 56.9055pt\times\Bigg(\int\_{\mathcal{Y}}\dfrac{1}{g^{\overline{y}}(t,x,y)\big(1-\gamma(\bar{y})\big)}\partial\_{xx}g^{\overline{y}}(t,x,y)f\_{Y\_{T}}(\bar{y};t,y)d\bar{y}\Bigg)^{-1}.\end{split} |  |

We now apply the ansatz

|  |  |  |
| --- | --- | --- |
|  | gy¯​(t,x,y)=11−γ​(y¯)​hy¯​(t,y)​x1−γ​(y¯),g^{\bar{y}}(t,x,y)=\dfrac{1}{1-\gamma(\bar{y})}h^{\bar{y}}(t,y)x^{1-\gamma(\bar{y})}, |  |

which leads to the following PIDE:

|  |  |  |
| --- | --- | --- |
|  | 0=11−γ​(y¯)​x1−γ​(y¯)​∂thy¯​(t,y)+x​(r+π^​(μS−r+ρ​σSσY​y¯−y−μY​(T−t)T−t))​x−γ​(y¯)​hy¯​(t,y)+y¯−yT−t​(11−γ​(y¯)​x1−γ​(y¯))​∂yhy¯​(t,y)−12​x2​π^2​σS2​γ​(y¯)​x−γ​(y¯)−1​hy¯​(t,y)+12​σY2​(11−γ​(y¯)​x1−γ​(y¯))​∂y​yhy¯​(t,y)+ρ​x​π^​σS​σY​x−γ​(y¯)​∂yhy¯​(t,y),\begin{split}0&=\dfrac{1}{1-\gamma(\bar{y})}x^{1-\gamma(\bar{y})}\partial\_{t}h^{\bar{y}}(t,y)\\ &+x\left(r+\widehat{\pi}\left(\mu\_{S}-r+\rho\dfrac{\sigma\_{S}}{\sigma\_{Y}}\dfrac{\bar{y}-y-\mu\_{Y}(T-t)}{T-t}\right)\right)x^{-\gamma(\bar{y})}h^{\bar{y}}(t,y)\\ &\qquad+\dfrac{\bar{y}-y}{T-t}\left(\dfrac{1}{1-\gamma(\bar{y})}x^{1-\gamma(\bar{y})}\right)\partial\_{y}h^{\bar{y}}(t,y)-\dfrac{1}{2}x^{2}\widehat{\pi}^{2}\sigma\_{S}^{2}\,\gamma(\bar{y})x^{-\gamma(\bar{y})-1}h^{\bar{y}}(t,y)\\ &\qquad+\dfrac{1}{2}\sigma\_{Y}^{2}\left(\dfrac{1}{1-\gamma(\bar{y})}x^{1-\gamma(\bar{y})}\right)\partial\_{yy}h^{\bar{y}}(t,y)+\rho x\widehat{\pi}\sigma\_{S}\sigma\_{Y}x^{-\gamma(\bar{y})}\partial\_{y}h^{\bar{y}}(t,y),\end{split} |  |

with terminal condition hy¯​(T,y)=1.h^{\bar{y}}(T,y)=1.

Simplifying with respect to xx (which cancels out entirely), this reduces to

|  |  |  |
| --- | --- | --- |
|  | 0=∂thy¯​(t,y)+(r+π^​(μS−r+ρ​σSσY​y¯−y−μY​(T−t)T−t))​(1−γ​(y¯))​hy¯​(t,y)+y¯−yT−t​∂yhy¯​(t,y)−12​π^2​σS2​γ​(y¯)​(1−γ​(y¯))​hy¯​(t,y)+12​σY2​∂y​yhy¯​(t,y)+ρ​π^​σS​σY​(1−γ​(y¯))​∂yhy¯​(t,y).\begin{split}&0=\partial\_{t}h^{\bar{y}}(t,y)+\left(r+\widehat{\pi}\left(\mu\_{S}-r+\rho\dfrac{\sigma\_{S}}{\sigma\_{Y}}\dfrac{\bar{y}-y-\mu\_{Y}(T-t)}{T-t}\right)\right)\big(1-\gamma(\bar{y})\big)h^{\bar{y}}(t,y)\\ &\qquad+\dfrac{\bar{y}-y}{T-t}\partial\_{y}h^{\bar{y}}(t,y)-\dfrac{1}{2}\widehat{\pi}^{2}\sigma\_{S}^{2}\,\gamma(\bar{y})\big(1-\gamma(\bar{y})\big)h^{\bar{y}}(t,y)+\dfrac{1}{2}\sigma\_{Y}^{2}\partial\_{yy}h^{\bar{y}}(t,y)\\ &\qquad+\rho\widehat{\pi}\sigma\_{S}\sigma\_{Y}\big(1-\gamma(\bar{y})\big)\partial\_{y}h^{\bar{y}}(t,y).\end{split} |  |

Collecting terms near partial derivatives, we then have

|  |  |  |
| --- | --- | --- |
|  | 0=∂thy¯​(t,y)+(y¯−yT−t+ρ​π^​σS​σY​(1−γ​(y¯)))​∂yhy¯​(t,y)+12​σY2​∂y​yhy¯​(t,y)+(r+π^​(μS−r+ρ​σSσY​(y¯−yT−t−μY))−12​π^2​σS2​γ​(y¯))​(1−γ​(y¯))​hy¯​(t,y).\begin{split}&0=\partial\_{t}h^{\bar{y}}(t,y)+\left(\dfrac{\bar{y}-y}{T-t}+\rho\widehat{\pi}\sigma\_{S}\sigma\_{Y}\big(1-\gamma(\bar{y})\big)\right)\partial\_{y}h^{\bar{y}}(t,y)+\dfrac{1}{2}\sigma\_{Y}^{2}\partial\_{yy}h^{\bar{y}}(t,y)\\ &+\left(r+\widehat{\pi}\left(\mu\_{S}-r+\rho\dfrac{\sigma\_{S}}{\sigma\_{Y}}\left(\dfrac{\bar{y}-y}{T-t}-\mu\_{Y}\right)\right)-\dfrac{1}{2}\widehat{\pi}^{2}\sigma\_{S}^{2}\gamma(\bar{y})\right)\big(1-\gamma(\bar{y})\big)h^{\bar{y}}(t,y).\end{split} |  |

Finally, using γ​(y¯)=exp⁡(y¯)\gamma(\bar{y})=\exp(\bar{y}), we obtain the equilibrium policy

|  |  |  |
| --- | --- | --- |
|  | π^​(t,y)=1σS2​𝔼t,y​[γ​(YT)]​(μS−r+ρ​σS​σY​∫𝒴∂yhy¯​(t,y)hy¯​(t,y)​fYT​(y¯;t,y)​𝑑y¯)=μS−r+ρ​σS​σY​∫𝒴∂yhy¯​(t,y)hy¯​(t,y)​fYT​(y¯;t,y)​𝑑y¯σS2​exp⁡(y+μY​(T−t)+12​σY2​(T−t)),\begin{split}\widehat{\pi}(t,y)&=\dfrac{1}{\sigma\_{S}^{2}\mathbb{E}\_{t,y}\left[\gamma(Y\_{T})\right]}\left(\mu\_{S}-r+\rho\sigma\_{S}\sigma\_{Y}\int\_{\mathcal{Y}}\dfrac{\partial\_{y}h^{\bar{y}}(t,y)}{h^{\bar{y}}(t,y)}f\_{Y\_{T}}(\bar{y};t,y)d\bar{y}\right)\\ &=\dfrac{\mu\_{S}-r+\rho\sigma\_{S}\sigma\_{Y}\int\_{\mathcal{Y}}\dfrac{\partial\_{y}h^{\bar{y}}(t,y)}{h^{\bar{y}}(t,y)}f\_{Y\_{T}}(\bar{y};t,y)d\bar{y}}{\sigma\_{S}^{2}\exp\left(y+\mu\_{Y}(T-t)+\dfrac{1}{2}\sigma\_{Y}^{2}(T-t)\right)},\end{split} |  |

which is independent of the current wealth level.
∎

## Appendix B Additional numerical results

In this appendix, we provide supplementary numerics that complement the analysis in Section [4](https://arxiv.org/html/2512.21149v1#S4 "4 Application: state-dependent CRRA utility ‣ Equilibrium investment under dynamic preference uncertainty").

First, Figures [2](https://arxiv.org/html/2512.21149v1#A2.F2 "Figure 2 ‣ Appendix B Additional numerical results ‣ Equilibrium investment under dynamic preference uncertainty") (a)-(b) display the functions hy¯​(t,y)h^{\bar{y}}(t,y) solving the PIDE ([4.6](https://arxiv.org/html/2512.21149v1#S4.E6 "In Proposition 4.2. ‣ 4.1 Preference specification and equilibrium investment ‣ 4 Application: state-dependent CRRA utility ‣ Equilibrium investment under dynamic preference uncertainty")) for a fixed value of y¯=YT=ln⁡(2)\bar{y}=Y\_{T}=\ln(2).

![Refer to caption](hfunction_positive_muy_positive_rho.png)


(a)

![Refer to caption](hfunction_negative_muy_positive_rho.png)


(b)

Figure 2: Intertemporal continuation value hy¯​(t,y)h^{\bar{y}}(t,y) for μY=0.02\mu\_{Y}=0.02 (left) and μY=−0.02\mu\_{Y}=-0.02 (right), fixing yT=ln⁡(2)y\_{T}=\ln(2). Other parameters: (r,μS,σS,σY,ρ,exp⁡(y0))=(0.02,0.07,0.2,0.04,0.6,2)(r,\mu\_{S},\sigma\_{S},\sigma\_{Y},\rho,\exp(y\_{0}))=(0.02,0.07,0.2,0.04,0.6,2).

Second, Figure [3](https://arxiv.org/html/2512.21149v1#A2.F3 "Figure 3 ‣ Appendix B Additional numerical results ‣ Equilibrium investment under dynamic preference uncertainty") shows the equilibrium investment policy in the special case μY=0.5​σY2\mu\_{Y}=0.5\sigma\_{Y}^{2}. Under this specification, the exponential factor in the denominator of ([4.5](https://arxiv.org/html/2512.21149v1#S4.E5 "In Proposition 4.2. ‣ 4.1 Preference specification and equilibrium investment ‣ 4 Application: state-dependent CRRA utility ‣ Equilibrium investment under dynamic preference uncertainty")) becomes time-invariant, leading to an equilibrium policy that is static in tt.

![Refer to caption](eqpolicy_special_muy_positive_rho.png)


Figure 3: Equilibrium policy for μY=0.5​σY2\mu\_{Y}=0.5\sigma\_{Y}^{2}. Other parameters: (r,μS,σS,σY,ρ)=(0.02,0.07,0.2,0.03,0.6)(r,\mu\_{S},\sigma\_{S},\sigma\_{Y},\rho)=(0.02,0.07,0.2,0.03,0.6).

To conclude, Table LABEL:tab:policy\_values reports equilibrium allocations for a range of parameter combinations in μY\mu\_{Y} and ρ\rho. All remaining parameters are as specified above.

Table 1: Equilibrium policy π^​(y,t)\hat{\pi}(y,t) for selected values of (y,t)(y,t).
Other parameters: (r,μS,σS,σY,γ​(y0))=(0.02,0.07,0.2,0.04,2)(r,\mu\_{S},\sigma\_{S},\sigma\_{Y},\gamma(y\_{0}))=(0.02,0.07,0.2,0.04,2).

| μY,ρ\mu\_{Y},\rho | exp⁡(y)\exp(y) | t=0t=0 | t=7t=7 | t=14t=14 | t=21t=21 | t=28t=28 | t=35t=35 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.02,0.60.02,0.6 | 2 | 0.272 | 0.315 | 0.364 | 0.421 | 0.487 | 0.563 |
| 3 | 0.182 | 0.21 | 0.243 | 0.281 | 0.325 | 0.376 |
| 4 | 0.136 | 0.157 | 0.182 | 0.211 | 0.244 | 0.282 |
| 7 | 0.078 | 0.09 | 0.104 | 0.120 | 0.139 | 0.161 |
| 10 | 0.054 | 0.063 | 0.073 | 0.084 | 0.097 | 0.113 |
| 0.02,−0.60.02,-0.6 | 2 | 0.272 | 0.315 | 0.364 | 0.421 | 0.487 | 0.563 |
| 3 | 0.181 | 0.21 | 0.243 | 0.281 | 0.325 | 0.376 |
| 4 | 0.136 | 0.157 | 0.182 | 0.21 | 0.243 | 0.281 |
| 7 | 0.078 | 0.09 | 0.104 | 0.12 | 0.139 | 0.161 |
| 10 | 0.054 | 0.063 | 0.073 | 0.084 | 0.097 | 0.113 |
| −0.02,0.6-0.02,0.6 | 0.8 | 3.48 | 2.946 | 2.574 | 2.251 | 1.967 | 1.72 |
| 1.2 | 2.328 | 1.963 | 1.716 | 1.5 | 1.312 | 1.147 |
| 1.6 | 1.724 | 1.472 | 1.287 | 1.125 | 0.984 | 0.86 |
| 2 | 1.365 | 1.178 | 1.03 | 0.9 | 0.787 | 0.688 |
| 2.4 | 1.13 | 0.981 | 0.858 | 0.75 | 0.656 | 0.573 |
| −0.02,−0.6-0.02,-0.6 | 0.8 | 3.384 | 2.93 | 2.573 | 2.25 | 1.967 | 1.72 |
| 1.2 | 2.257 | 1.948 | 1.716 | 1.5 | 1.312 | 1.147 |
| 1.6 | 1.692 | 1.462 | 1.287 | 1.125 | 0.984 | 0.86 |
| 2 | 1.353 | 1.171 | 1.029 | 0.9 | 0.787 | 0.688 |
| 2.4 | 1.128 | 0.976 | 0.858 | 0.75 | 0.656 | 0.573 |
| 0.5​σY2,0.60.5\sigma\_{Y}^{2},0.6 | 1 | 1.172 | 1.186 | 1.199 | 1.213 | 1.226 | 1.24 |
| 2 | 0.586 | 0.593 | 0.599 | 0.606 | 0.613 | 0.62 |
| 3 | 0.391 | 0.395 | 0.4 | 0.404 | 0.409 | 0.413 |
| 4 | 0.293 | 0.296 | 0.3 | 0.303 | 0.307 | 0.31 |
| 5 | 0.235 | 0.237 | 0.24 | 0.243 | 0.245 | 0.248 |
| 0.5​σY2,−0.60.5\sigma\_{Y}^{2},-0.6 | 1 | 1.171 | 1.186 | 1.199 | 1.213 | 1.227 | 1.24 |
| 2 | 0.586 | 0.593 | 0.599 | 0.606 | 0.613 | 0.62 |
| 3 | 0.391 | 0.395 | 0.4 | 0.404 | 0.409 | 0.413 |
| 4 | 0.293 | 0.296 | 0.3 | 0.303 | 0.307 | 0.31 |
| 5 | 0.234 | 0.237 | 0.24 | 0.243 | 0.245 | 0.248 |
| 0.02,10.02,1 | 2 | 0.272 | 0.315 | 0.364 | 0.421 | 0.487 | 0.563 |
| 3 | 0.181 | 0.21 | 0.243 | 0.281 | 0.325 | 0.376 |
| 4 | 0.136 | 0.157 | 0.182 | 0.21 | 0.243 | 0.282 |
| 7 | 0.078 | 0.09 | 0.104 | 0.12 | 0.139 | 0.161 |
| 10 | 0.054 | 0.063 | 0.073 | 0.084 | 0.097 | 0.113 |
| 0.02,−10.02,-1 | 2 | 0.272 | 0.315 | 0.364 | 0.421 | 0.487 | 0.563 |
| 3 | 0.181 | 0.21 | 0.243 | 0.281 | 0.325 | 0.376 |
| 4 | 0.136 | 0.157 | 0.182 | 0.21 | 0.243 | 0.282 |
| 7 | 0.078 | 0.09 | 0.104 | 0.12 | 0.139 | 0.161 |
| 10 | 0.054 | 0.063 | 0.073 | 0.084 | 0.097 | 0.113 |
| −0.02,1-0.02,1 | 0.8 | 3.446 | 3.027 | 2.578 | 2.251 | 1.967 | 1.72 |
| 1.2 | 2.34 | 2.008 | 1.717 | 1.5 | 1.312 | 1.467 |
| 1.6 | 1.767 | 1.43 | 1.287 | 1.125 | 0.984 | 0.86 |
| 2 | 1.419 | 1.188 | 1.03 | 0.9 | 0.787 | 0.688 |
| 2.4 | 1.185 | 0.986 | 0.858 | 0.75 | 0.656 | 0.573 |
| −0.02,−1-0.02,-1 | 0.8 | 3.49 | 2.942 | 2.574 | 2.251 | 1.968 | 1.72 |
| 1.2 | 2.387 | 1.962 | 1.716 | 1.5 | 1.312 | 1.147 |
| 1.6 | 1.794 | 1.471 | 1.287 | 1.125 | 0.984 | 0.86 |
| 2 | 1.424 | 1.177 | 1.03 | 0.9 | 0.787 | 0.688 |
| 2.4 | 1.174 | 0.981 | 0.858 | 0.75 | 0.656 | 0.573 |
| 0.02,00.02,0 | 2 | 0.272 | 0.315 | 0.3634 | 0.421 | 0.487 | 0.563 |
| 3 | 0.181 | 0.21 | 0.243 | 0.281 | 0.325 | 0.376 |
| 4 | 0.136 | 0.157 | 0.182 | 0.21 | 0.243 | 0.282 |
| 7 | 0.078 | 0.09 | 0.104 | 0.12 | 0.139 | 0.161 |
| 10 | 0.054 | 0.063 | 0.073 | 0.084 | 0.097 | 0.113 |
| −0.02,0-0.02,0 | 0.8 | 3.368 | 2.946 | 2.574 | 2.25 | 1.968 | 1.72 |
| 1.2 | 2.245 | 1.963 | 1.716 | 1.5 | 1.312 | 1.147 |
| 1.6 | 1.684 | 1.472 | 1.287 | 1.125 | 0.984 | 0.86 |
| 2 | 1.347 | 1.178 | 1.03 | 0.9 | 0.787 | 0.688 |
| 2.4 | 1.123 | 0.981 | 0.858 | 0.75 | 0.656 | 0.573 |

## Appendix C Pseudocodes

To compute the equilibrium policy numerically, we solve the coupled system ([4.5](https://arxiv.org/html/2512.21149v1#S4.E5 "In Proposition 4.2. ‣ 4.1 Preference specification and equilibrium investment ‣ 4 Application: state-dependent CRRA utility ‣ Equilibrium investment under dynamic preference uncertainty"))-([4.6](https://arxiv.org/html/2512.21149v1#S4.E6 "In Proposition 4.2. ‣ 4.1 Preference specification and equilibrium investment ‣ 4 Application: state-dependent CRRA utility ‣ Equilibrium investment under dynamic preference uncertainty")) using a neural network-based approach. The key idea is to approximate each function hy¯​(t,y)h^{\bar{y}}(t,y) by a neural network and to enforce the PIDE through a physics-informed loss that penalizes deviations from the differential equation, the boundary condition, and the coupling with π^​(t,y)\widehat{\pi}(t,y). The equilibrium policy is updated iteratively: given an estimate of hy¯h^{\bar{y}}, we compute π^\widehat{\pi}; this updated policy is then fed back into the PIDE, and the networks are trained until a fixed point is reached.

1EvaluatePiHat(*hθh\_{\theta}, current state yy, time tt*)

Input : Trained model hθh\_{\theta}, grid size Ng​r​i​dN\_{grid} for yTy\_{T} integration

Output : Estimated policy π^​(t,y)\widehat{\pi}(t,y)

2

3Construct grid {yT(j)}j=1Ng​r​i​d\{y\_{T}^{(j)}\}\_{j=1}^{N\_{grid}} over support of yTy\_{T};

4
for *j=1j=1 to Ng​r​i​dN\_{grid}* do

5   Compute hj=hθ​(t,y,yT(j))h\_{j}=h\_{\theta}(t,y,y\_{T}^{(j)});

6   
Compute partial derivative ∂yhj​(t,y,yT(j));\partial\_{y}h\_{j}(t,y,y\_{T}^{(j)})\;;

7   Compute ratio:

|  |  |  |
| --- | --- | --- |
|  | rj=∂yhjhj+ε;r\_{j}=\frac{\partial\_{y}h\_{j}}{h\_{j}+\varepsilon}\;; |  |

8   Using the conditional distribution of the arithmetic Brownian motion, YT|Yt=y∼𝒩​(y+μY​(T−t),σY2​(T−t))Y\_{T}\,|\,Y\_{t}=y\sim\mathcal{N}\big(y+\mu\_{Y}(T-t),\sigma\_{Y}^{2}(T-t)\big), compute CDF weights:

|  |  |  |
| --- | --- | --- |
|  | wj=Φ​(yT(j)−y−μY​(T−t)σY​T−t).w\_{j}=\Phi\left(\frac{y\_{T}^{(j)}-y-\mu\_{Y}(T-t)}{\sigma\_{Y}\sqrt{T-t}}\right)\;. |  |

9

10Compute integral using trapezoidal rule:

|  |  |  |
| --- | --- | --- |
|  | I=∑j=1Ng​r​i​drj⋅wj⋅Δ​yT;I=\sum\_{j=1}^{N\_{grid}}r\_{j}\cdot w\_{j}\cdot\Delta y\_{T}\;; |  |

Return:

|  |  |  |
| --- | --- | --- |
|  | π^​(t,y)=μS−r+ρ​σS​σY​IσS2​𝔼t,y​[γ​(yT)]=μS−r+ρ​σS​σY​IσS2​exp⁡(y+μY​(T−t)+12​σY2​(T−t)).\widehat{\pi}(t,y)=\frac{\mu\_{S}-r+\rho\sigma\_{S}\sigma\_{Y}I}{\sigma\_{S}^{2}\,\mathbb{E}\_{t,y}\left[\gamma(y\_{T})\right]}=\frac{\mu\_{S}-r+\rho\sigma\_{S}\sigma\_{Y}I}{\sigma\_{S}^{2}\,\exp\left(y+\mu\_{Y}(T-t)+\frac{1}{2}\sigma\_{Y}^{2}(T-t)\right)}. |  |

Algorithm 1 Evaluate equilibrium policy π^​(t,y)\widehat{\pi}(t,y)



1TrainHModel(*θ\theta (NN parameters), terminal time TT, initial state Y0Y\_{0}*)

Input : Learning rate η\eta, number of iterations NiterN\_{\text{iter}}, batch size Nb​a​t​c​hN\_{batch}, sample size Np​a​t​h​sN\_{paths}, boundary loss weight λb​c\lambda\_{bc}

Output : Trained model hθ​(t,y,yT)h\_{\theta}(t,y,y\_{T})

2

3Initialize neural network hθ:(t,y,yT)↦ℝ+h\_{\theta}\colon(t,y,y\_{T})\mapsto\mathbb{R}\_{+};

4
for *k=1k=1 to Ni​t​e​rN\_{iter}* do

5   
Sample training batch {(ti,yi,yT(i))}i=1Nb​a​t​c​h\{(t\_{i},y\_{i},y\_{T}^{(i)})\}\_{i=1}^{N\_{batch}} from training domain;

6   
for *i=1i=1 to Nb​a​t​c​hN\_{batch}* do

7      
Compute model output hi=hθ​(ti,yi,yT(i))h\_{i}=h\_{\theta}(t\_{i},y\_{i},y\_{T}^{(i)});

8      
Compute partial derivatives ∂thi,∂yhi,∂y​yhi\partial\_{t}h\_{i},\,\partial\_{y}h\_{i},\,\partial\_{yy}h\_{i} with autograd;

9

10      Compute π=π^​(yi,ti)\pi=\widehat{\pi}(y\_{i},t\_{i}) using Algorithm [1](https://arxiv.org/html/2512.21149v1#algorithm1 "In Appendix C Pseudocodes ‣ Equilibrium investment under dynamic preference uncertainty");

11

12      Compute PIDE coefficient functions Pi=P​(ti,yi,yT(i)),Qi=Q​(ti,yi,yT(i)),P\_{i}=P(t\_{i},y\_{i},y\_{T}^{(i)}),Q\_{i}=Q(t\_{i},y\_{i},y\_{T}^{(i)}), Ri=R​(ti,yi,yT(i))R\_{i}=R(t\_{i},y\_{i},y\_{T}^{(i)}):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Pi\displaystyle P\_{i} | =\displaystyle= | (r+π​(μS−r+ρ​σSσY​(yT(i)−yiT−ti−μY))−12​π2​σS2​γ​(yT(i)))​(1−γ​(yT(i))),\displaystyle\left(r+\pi\left(\mu\_{S}-r+\rho\dfrac{\sigma\_{S}}{\sigma\_{Y}}\left(\dfrac{y\_{T}^{(i)}-y\_{i}}{T-t\_{i}}-\mu\_{Y}\right)\right)-\dfrac{1}{2}\pi^{2}\sigma\_{S}^{2}\gamma(y\_{T}^{(i)})\right)(1-\gamma(y\_{T}^{(i)}))\;, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Qi\displaystyle Q\_{i} | =\displaystyle= | yT(i)−yiT−ti+ρ​σS​σY​(1−γ​(yT(i))),Ri=12​σY2;\displaystyle\dfrac{y\_{T}^{(i)}-y\_{i}}{T-t\_{i}}+\rho\sigma\_{S}\sigma\_{Y}(1-\gamma(y\_{T}^{(i)}))\;,\quad R\_{i}=\dfrac{1}{2}\sigma\_{Y}^{2}\;; |  |

13      Evaluate PIDE residual:

|  |  |  |
| --- | --- | --- |
|  | residuali=∂thi+P​(ti,yi,yT(i))​hi+Q​(ti,yi,yT(i))​∂yhi+R​(ti,yi,yT(i))​∂y​yhi;\text{residual}\_{i}=\partial\_{t}h\_{i}+P(t\_{i},y\_{i},y\_{T}^{(i)})h\_{i}+Q(t\_{i},y\_{i},y\_{T}^{(i)})\partial\_{y}h\_{i}+R(t\_{i},y\_{i},y\_{T}^{(i)})\partial\_{yy}h\_{i}\;; |  |

14

15   Compute PIDE loss:

|  |  |  |
| --- | --- | --- |
|  | Lp​i​d​e=1Nb​a​t​c​h​∑i=1Nb​a​t​c​h(residuali)2;L\_{pide}=\frac{1}{N\_{batch}}\sum\_{i=1}^{N\_{batch}}(\text{residual}\_{i})^{2}\;; |  |

16   Sample boundary points {(T,yT(j),yT(j))}j=1Np​a​t​h​s\{(T,y\_{T}^{(j)},y\_{T}^{(j)})\}\_{j=1}^{N\_{paths}};

17   
Compute terminal condition loss:

|  |  |  |
| --- | --- | --- |
|  | Lbc=1Np​a​t​h​s​∑j=1Np​a​t​h​s(hθ​(T,yT(j),yT(j))−1)2;L\_{\text{bc}}=\frac{1}{N\_{paths}}\sum\_{j=1}^{N\_{paths}}\left(h\_{\theta}(T,y\_{T}^{(j)},y\_{T}^{(j)})-1\right)^{2}\;; |  |

18   Compute total loss: L=Lp​i​d​e+λbc​Lbc;\quad L=L\_{pide}+\lambda\_{\text{bc}}L\_{\text{bc}};

19   Update parameters: θ←θ−η​∇θL;\quad\theta\leftarrow\theta-\eta\nabla\_{\theta}L\;;

return hθ.h\_{\theta}\;.

Algorithm 2 Training the NN solution h​(t,y,yT)h(t,y,y\_{T})