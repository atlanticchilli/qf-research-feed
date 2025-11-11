---
authors:
- Yue Cao
- Zongxia Liang
- Sheng Wang
- Xiang Yu
doc_id: arxiv:2511.05861v1
family_id: arxiv:2511.05861
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns
  in Incomplete Markets
url_abs: http://arxiv.org/abs/2511.05861v1
url_html: https://arxiv.org/html/2511.05861v1
venue: arXiv q-fin
version: 1
year: 2025
---


Yue Cao
Department of Mathematical Sciences, Tsinghua University, Beijing, China. <caoyue24@mails.tsinghua.edu.cn>
  
Zongxia Liang
Department of Mathematical Sciences, Tsinghua University, Beijing, China. <liangzongxia@tsinghua.edu.cn>
  
Sheng Wang
Department of Statistics and Actuarial Science, The University of Hong Kong, Pokfulam Road, Hong Kong. <sheng-wa15@tsinghua.org.cn>
  
Xiang Yu
Department of Applied Mathematics, The Hong Kong Polytechnic University, Kowloon, Hong Kong. <xiang.yu@polyu.edu.hk>

###### Abstract

This paper investigates a time-inconsistent portfolio selection problem in the incomplete market model, integrating expected utility maximization with risk control. The objective functional balances the expected utility and variance on log returns, giving rise to time inconsistency and motivating the search of a time-consistent equilibrium strategy. We characterize the equilibrium via a coupled quadratic backward stochastic differential equation (BSDE) system and establish the existence theory in two special cases: (i) two Brownian motions driven the price dynamics and the factor process are independent with ρ=0\rho=0; (ii) the trading strategy is constrained to be bounded. For the general case with correlation coefficient ρ≠0\rho\neq 0, we introduce the notion of an approximate time-consistent equilibrium. By employing the solution structure from the equilibrium in the case ρ=0\rho=0, we can construct an approximate time-consistent equilibrium in the general case with an error of order O​(ρ2)O(\rho^{2}). Numerical examples and financial insights based on deep learning algorithms are also presented.

Keywords: Time inconsistent control, time-consistent equilibrium, quadratic BSDE system, approximate time-consistent equilibrium

## 1 Introduction

The optimal portfolio management problem has always been a core research topic in quantitative finance, traditionally approached via the mean-variance (MV) criterion proposed by Markowitz\_1952 and the expected utility (EU) theory developed in merton\_1969; MERTON1971373. The classical mean–variance criterion captures the trade-off between the expected return and the risk (variance). In contrary, the utility maximization framework incorporates the investor’s risk aversion level into decision making without concerning the risk level of terminal wealth.

One natural extension is to integrate the risk management into the utility maximization problem, dictating the optimal trading strategy at a reasonable risk level. The research in this direction has gained an upsurge of attention recently. As a pioneer attempt, Bsask\_2001 study the utility maximization on portfolio and consumption plans by imposing the Value-at-Risk (VaR) constraints on the terminal wealth to encode the agent’s concern on the risk level. Wong\_2017 examine a utility–deviation–risk portfolio selection problem by reformulating it as an equivalent nonlinear moment system, where the objective combines expected utility with a deviation-based risk measure, and derives the optimal strategy in a Black-Scholes model. Bensouusan\_2022 recently combine the utility maximization problem with the variance minimization of terminal wealth, and recasts the problem as a mean field-type control (MFC) problem using a coupled system of Hamilton–Jacobi–Bellman and Fokker–Planck equation, and characterizes the optimal consumption and trading strategies in the mean-field context.

Our paper adopts an integrated formulation that aims to optimize the trade-off between the expected utility and the variance of portfolio in incomplete market models. Unlike the setting that focuses on the capital amount (see, e.g., Wong\_2017 and Bensouusan\_2022), we target at the log returns of the portfolio. This choice follows a growing line of research on portfolio selection (see dai\_dynamic\_2021, Peng\_2023, Guan2025, and references therein). Specifically, the objective functional in our paper at time tt is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(t,π)=𝔼t​[U​(log⁡(WTπWtπ))]−γt2​Vart​[log⁡(WTπWtπ)].\displaystyle J(t,\pi)=\mathbb{E}\_{t}\left[U\left(\log\left(\frac{W^{\pi}\_{T}}{W^{\pi}\_{t}}\right)\right)\right]-\frac{\gamma\_{t}}{2}\textup{Var}\_{t}\left[\log\left(\frac{W^{\pi}\_{T}}{W^{\pi}\_{t}}\right)\right]. |  | (1.1) |

Nevertheless, the log returns and the variance term in the objective functional render the problem time-inconsistent. That is, a strategy being optimal today may no longer remain optimal at future dates. Strotz1955 classifies agents facing time-inconsistency into three types.
The naive agent always re-optimizes the current objective, ignoring time-inconsistency and thus constantly changing strategies. The precommitted agent fixes an initial optimal plan, knowing it will later become suboptimal; the plan remains time-inconsistent since it is only optimal at the initial time. A sophisticated agent cannot precommit but anticipates future deviations, viewing her future selves as strategic counterparts and seeking a time-consistent equilibrium strategy that each self optimally follows—namely, the intrapersonal equilibrium.

Contrary to Wong\_2017 and Bensouusan\_2022, who focus on the precommitted strategy, the present paper aims to characterize a time-consistent equilibrium strategy by a sophisticated agent under game theoretical thinking with future selves, whose precise definition in continuous time was first proposed in Ekeland2006noncommitmentsubgameperfectequilibrium111Since then, a strand of literature on time-inconsistent control problems in continuous-time setting has emerged, see e.g. Basak\_dynamic\_2010, hu\_time-inconsistent\_2012, hu\_time-inconsistent\_2017, Bjork\_2014, dai\_dynamic\_2021 for MV problems, Ekeland2006noncommitmentsubgameperfectequilibrium, Ekeland\_2007, Hamaguchi\_2021 for non-exponential discounting problems.. Moreover, we consider the incomplete market model, where the financial market consists of a risk-free asset and a single risky asset222For simplicity, we focus on one risky asset, as the analysis can be extended directly to multiple risky assets.. The wealth process is driven by a standard Brownian motion BB, while the asset prices are influenced by an exogenous factor process driven by another Brownian motion B¯\bar{B}. The correlation coefficient of these two Brownian motions is denoted by ρ\rho.
Similar to Hamaguchi\_2021 and dai\_dynamic\_2021, we can employ the perturbation and maximum principle to establish a necessary condition to characterize an open-loop time-consistent equilibrium strategy in Theorem [3.1](https://arxiv.org/html/2511.05861v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") for our utility maximization problem with variance minization via a two-dimensional system of coupled BSDEs ([3.1](https://arxiv.org/html/2511.05861v1#S3.E1 "In item 2 ‣ Theorem 3.1. ‣ 3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) (see also ([4.2](https://arxiv.org/html/2511.05861v1#S4.E2 "In 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) for a simplified yet still coupled system), which has not been addressed before in the existing literature.

In general, the system ([4.2](https://arxiv.org/html/2511.05861v1#S4.E2 "In 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) consists of two quadratic BSDEs coupled by the derived optimal strategy in
quadratic form. Classical existence results for the multidimensional BSDE mainly fall into two categories: the fixed-point approach based on contraction mappings, which ensures uniqueness of solutions (see HU20161066, Luo\_2017 and FAN2023105), and the construction of uniformly convergent approximations via coefficient regularization (see xing\_class\_2018, Jackson\_2022 and JACKSON2023). However, neither of these methods applies to our problem (see Appendix [C](https://arxiv.org/html/2511.05861v1#A3 "Appendix C The Challenge of our BSDE System when 𝜌≠0 ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") for the detailed explanation).

In response to the challenge of the unconventional BSDE system, we first study two special cases where the existence of solution can be obtained and the verification theorem can be exercised: (i) the case with zero correlation coefficient (ρ=0\rho=0) for two Brownian motions BB and B¯\bar{B}; (ii) the case with trading constraint in a bounded set.

For the general case with ρ≠0\rho\neq 0 and without trading constraint,
we can no longer establish the existence of solution to the more complicated BSDE system. However, as a new contribution to the existing literature, we can show that by employing the solution structure from the time-consistent equilibrium strategy in the special case with ρ=0\rho=0 we can successfully construct an approximate time-consistent equilibrium (see Definition [5.1](https://arxiv.org/html/2511.05861v1#S5.Thmtheorem1 "Definition 5.1. ‣ 5 Approximate Time-Consistent Equilibrium for Small 𝜌≠0 ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) in the general case with ρ≠0\rho\neq 0 when the correlation coefficient ρ\rho is sufficiently small. More importantly, under some additional regularity conditions, we can rigorously show that the approximation error using the equilibrium solution in the case ρ=0\rho=0 is of order O​(ρ2)O(\rho^{2}), see Theorem [5.5](https://arxiv.org/html/2511.05861v1#S5.Thmtheorem5 "Theorem 5.5. ‣ 5 Approximate Time-Consistent Equilibrium for Small 𝜌≠0 ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets"). This approximation result using the explicit equilibrium structure in the special case with ρ=0\rho=0 significantly simplifies the decision making in some general incomplete market models with small ρ\rho such that it is sufficient to implement the more tractable control process while the time-consistency can be retained in an approximate sense.

We also highlight the main differences between the present paper and some related studies in Gu\_2020 and Bensoussan\_2025. Gu\_2020 studies a time-consistent Hamilton–Jacobi–Bellman (HJB) equation to characterize the equilibrium strategy for a utility–deviation risk control problem. They obtain the explicit equilibrium value function and the corresponding equilibrium strategy in a homogeneous utility–deviation risk problem with CRRA utility based on a specific choice of risk-aversion function. In contrast, we focus on the optimization of the trade-off between the exponential utility and variance over
log returns and characterize the open-loop time-consistent equilibrium via a system of coupled quadratic BSDEs, for which we establish existence results in some cases and provide an approximate equilibrium in the general case. Bensoussan\_2025 study a stochastic control problem incorporating higher-order moments in the complete market model and provide the characterization of the time-consistent equilibrium strategy. On the contrary, we consider an incomplete stochastic factor model that significantly increases the mathematical complexity to establish the existence of time-consistent equilibrium.

To illustrate our theoretical results, we further employ a deep learning–based numerical scheme, originally proposed by e\_deep\_2017 and Han\_2018, to solve the BSDE systems arising in the three cases—namely, the case with ρ=0\rho=0, the case with trading constraints, and the case of the approximate equilibrium for ρ≠0\rho\neq 0. We find that when the correlation coefficient ρ=0\rho=0, the equilibrium investment ratio exhibits a slight upward trend as time approaches the terminal horizon, differing from the observation in dai\_dynamic\_2021 such that the investment strategy remains constant. When ρ<0\rho<0, however, our results are consistent with dai\_dynamic\_2021, showing a downward trend in the investment ratio when time approaches the terminal horizon. In addition, we perform sensitivity analysis with respect to the risk-aversion parameter ζ\zeta in the utility function and the weighting coefficient γ\gamma between the expected utility and the variance. The numerical results illustrate that the equilibrium strategy exhibits a reasonable monotonic pattern with respect to both ζ\zeta and γ\gamma. Moreover, the numerical results also shows that the approximate Nash equilibrium strategy and its resulting value function are relatively close to those under the true constrained equilibrium when the trading constraint bound is large.

The remainder of the paper is organized as follows. Section [2](https://arxiv.org/html/2511.05861v1#S2 "2 Problem Formulation ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") formulates the time inconsistent control problem as the trade-off between the utility maximization and the variance minimization over logarithmic portfolio returns, for which a time-consistent equilibrium is introduced. Section [3](https://arxiv.org/html/2511.05861v1#S3 "3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") provides the characterization of the time-consistent equilibrium by a quadratic BSDE system. Section [4](https://arxiv.org/html/2511.05861v1#S4 "4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") investigates the existence of solution to the BSDE system in the stochastic factor model in two special cases: (i) when two Brownian motions in the price dynamics and in the factor model are independent; (2) when the trading strategy is constrained in a compact set. Section [5](https://arxiv.org/html/2511.05861v1#S5 "5 Approximate Time-Consistent Equilibrium for Small 𝜌≠0 ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") establishes the approximate time-consistent equilibrium in the general case when two Brownian motions are correlated with ρ≠0\rho\neq 0 using the same solution structure from time-consistent equilibrium solution in the model with ρ=0\rho=0 with the error of order O​(ρ2)O(\rho^{2}). Some numerical illustrations and financial implications are presented in Section [6](https://arxiv.org/html/2511.05861v1#S6 "6 Numerical Examples ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets"). Finally, Appendix [A](https://arxiv.org/html/2511.05861v1#A1 "Appendix A The Energy Inequality and the John-Nirenberg Inequality ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") and [B](https://arxiv.org/html/2511.05861v1#A2 "Appendix B Sufficient Conditions for the Existence of Solution to BSDEs ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") collect some inequalities and sufficient conditions for the existence theory of BSDE system that are used in previous sections, and Appendix [C](https://arxiv.org/html/2511.05861v1#A3 "Appendix C The Challenge of our BSDE System when 𝜌≠0 ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") elaborates some challenges of the BSDE system in the general case when ρ≠0\rho\neq 0.

Notations: For t∈[0,T]t\in[0,T], p,q≥1p,q\geq 1, we list below some notations that will be used frequently throughout the paper:

* •

  HBMOH\_{\textup{BMO}} denotes the set of ℝ\mathbb{R}-valued 𝔽\mathbb{F}-progressively measurable processes such that ‖π‖BMO<∞\|\pi\|\_{\textup{BMO}}<\infty, where

  |  |  |  |
  | --- | --- | --- |
  |  | ‖π‖BMO2:=supτ∈𝒯[0,T]‖𝔼τ​[∫τT|πs|2​𝑑s]‖∞,\|\pi\|\_{\textup{BMO}}^{2}:=\sup\_{\tau\in\mathcal{T}\_{[0,T]}}\left\|\mathbb{E}\_{\tau}\left[\int\_{\tau}^{T}|\pi\_{s}|^{2}ds\right]\right\|\_{\infty}, |  |

  𝒯[0,T]\mathcal{T}\_{[0,T]} denotes all stopping times on [0,T][0,T].
* •

  Lℱt∞​(Ω;ℝ)L^{\infty}\_{\mathcal{F}\_{t}}(\Omega;\mathbb{R}) denotes the set of all ℝ\mathbb{R}-valued ℱt\mathcal{F}\_{t}-measurable bounded random variables.
* •

  L𝔽p​(Ω;Lq​(t,T;ℝ))L^{p}\_{\mathbb{F}}(\Omega;L^{q}(t,T;\mathbb{R})) denotes the set of all ℝ\mathbb{R}-valued progressively measurable processes XX with

  |  |  |  |
  | --- | --- | --- |
  |  | 𝔼​[(∫tT|Xs|q​𝑑s)p/q]<∞.\mathbb{E}\left[\left(\int\_{t}^{T}|X\_{s}|^{q}ds\right)^{p/q}\right]<\infty. |  |

  When p=qp=q, we write L𝔽p​(t,T;ℝ):=L𝔽p​(Ω;Lp​(t,T;ℝ))L^{p}\_{\mathbb{F}}(t,T;\mathbb{R}):=L^{p}\_{\mathbb{F}}(\Omega;L^{p}(t,T;\mathbb{R}))
* •

  L𝔽p​(Ω;C​([t,T];ℝ))L^{p}\_{\mathbb{F}}(\Omega;C([t,T];\mathbb{R})) denotes the set of all ℝ\mathbb{R}-valued adapted and continuous processes XX with

  |  |  |  |
  | --- | --- | --- |
  |  | 𝔼​[sups∈[t,T]|Xs|p]<∞.\mathbb{E}\left[\sup\_{s\in[t,T]}|X\_{s}|^{p}\right]<\infty. |  |
* •

  𝒮∞\mathcal{S}^{\infty} denotes the set of all ℝ\mathbb{R}-valued 𝔽\mathbb{F}-progressively measurable and bounded processes.

## 2 Problem Formulation

Let T>0T>0 be a finite time horizon and (Ω,ℱ,𝔽,ℙ)(\Omega,\mathcal{F},\mathbb{F},\mathbb{P}) be a filtered complete probability space, where 𝔽={ℱt,0≤t≤T}\mathbb{F}=\{\mathcal{F}\_{t},0\leq t\leq T\} is the augmented natural filtration generated by two standard Brownian motions {B​(t),0≤t≤T}\{B(t),0\leq t\leq T\} and {B¯​(t),0≤t≤T}\{\bar{B}(t),0\leq t\leq T\}.
Their correlation coefficient ρ\rho is such that
𝔼​[B​(t)​B¯​(t)]=ρ​t\mathbb{E}[B(t)\bar{B}(t)]=\rho t. The market model consists of one risk-free bond with interest rate r={rt:t∈[0,T]}r=\{r\_{t}:t\in[0,T]\} and one stockwith price dynamics governed by

|  |  |  |
| --- | --- | --- |
|  | d​St=St​(μt​d​t+σt​d​Bt),S0=s0∈(0,∞),\mathrm{d}S\_{t}=S\_{t}\left(\mu\_{t}\mathrm{d}t+\sigma\_{t}\mathrm{d}B\_{t}\right),\quad S\_{0}=s\_{0}\in(0,\infty), |  |

where the drift μ:[0,T]×Ω→ℝ\mu:[0,T]\times\Omega\to\mathbb{R}, the volatility σ>0:[0,T]×Ω→ℝ\mathbf{\sigma}>0:[0,T]\times\Omega\to\mathbb{R}, and the interest rate r:[0,T]×Ω→ℝr:[0,T]\times\Omega\to\mathbb{R}, are all 𝔽\mathbb{F}-progressively measurable processes.

###### Assumption 2.1.

rt,μt,σt>0r\_{t},\mu\_{t},\sigma\_{t}>0 and θt:=σt−1​(μt−rt)\theta\_{t}:=\sigma\_{t}^{-1}(\mu\_{t}-r\_{t}) are bounded 𝔽\mathbb{F}-progressively measurable processes.

A trading strategy is a 𝔽\mathbb{F}-progressively measurable processes π\pi such that ∫0T|πt​(μ​(t)−r​(t))|​dt+∫0T|σ​(t)​πt|2​dt<∞\int\_{0}^{T}|\pi\_{t}(\mu(t)-r(t))|\mathrm{d}t+\int\_{0}^{T}|\sigma(t)\pi\_{t}|^{2}\mathrm{d}t<\infty a.s., where πt\pi\_{t} stands for the fraction of wealth allocated in the stock at time tt.
The self-financing wealth process WπW^{\pi} evolves according to

|  |  |  |
| --- | --- | --- |
|  | d​Wtπ=Wtπ​(rt+πt​(μt−rt)​d​t+πt​σt​d​Bt),W0π=w0>0.\mathrm{d}W^{\pi}\_{t}=W^{\pi}\_{t}\left(r\_{t}+\pi\_{t}(\mu\_{t}-r\_{t})\mathrm{d}t+\pi\_{t}\sigma\_{t}\mathrm{d}B\_{t}\right),\quad W^{\pi}\_{0}=w\_{0}>0. |  |

In this paper, we consider a utility maximization framework with variance adjustment on log return of the
portfolio. That is, with given r0∈ℝ,π0r\_{0}\in\mathbb{R},\pi\_{0} and t∈[0,T)t\in[0,T), the objective functional of the investor given the trading strategy π\pi at time tt is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(t,π)=𝔼t​[U​(log⁡(WTπWtπ))]−γt2​Vart​[log⁡(WTπWtπ)],J(t,\pi)=\mathbb{E}\_{t}\left[U\left(\log\left(\frac{W^{\pi}\_{T}}{W^{\pi}\_{t}}\right)\right)\right]-\frac{\gamma\_{t}}{2}\textup{Var}\_{t}\left[\log\left(\frac{W^{\pi}\_{T}}{W^{\pi}\_{t}}\right)\right], |  | (2.1) |

where 𝔼t\mathbb{E}\_{t} and Vart\textup{Var}\_{t} represent the conditional expectation and the conditional variance at time tt, respectively, and γt>0\gamma\_{t}>0 can be regarded as the weighting parameter measuring the trade-off between the expected utility and the risk (variance) at time tt.
In particular, we shall work with the CARA utility U​(x)=−1ζ​e−ζ​xU(x)=-\frac{1}{\zeta}e^{-\zeta x} with the risk aversion parameter ζ>0\zeta>0.

To simplify the notation, let us denote Rtπ=log⁡WtπR^{\pi}\_{t}=\log W^{\pi}\_{t}, which satisfies

|  |  |  |
| --- | --- | --- |
|  | d​Rtπ=[rt+πt​(μt−rt)−12​|σt​πt|2]​d​t+πt​σt​d​Bt,R0π=r0=log⁡w0∈ℝ.\mathrm{d}R^{\pi}\_{t}=\left[r\_{t}+\pi\_{t}(\mu\_{t}-r\_{t})-\frac{1}{2}|\sigma\_{t}\pi\_{t}|^{2}\right]\mathrm{d}t+\pi\_{t}\sigma\_{t}\mathrm{d}B\_{t},\quad R^{\pi}\_{0}=r\_{0}=\log w\_{0}\in\mathbb{R}. |  |

Then the objective functional in ([2.1](https://arxiv.org/html/2511.05861v1#S2.E1 "In 2 Problem Formulation ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) at time tt can be written as

|  |  |  |
| --- | --- | --- |
|  | 𝔼t​[U​(RTπ−Rtπ)]−γt2​Vart​[RTπ−Rtπ]=−1ζ​𝔼t​[exp⁡(−ζ​(RTπ−Rtπ))]−γt2​Vart​[RTπ].\mathbb{E}\_{t}\left[U(R^{\pi}\_{T}-R^{\pi}\_{t})\right]-\frac{\gamma\_{t}}{2}\textup{Var}\_{t}[R^{\pi}\_{T}-R^{\pi}\_{t}]=-\frac{1}{\zeta}\mathbb{E}\_{t}\left[\exp\left(-\zeta(R^{\pi}\_{T}-R^{\pi}\_{t})\right)\right]-\frac{\gamma\_{t}}{2}\textup{Var}\_{t}[R^{\pi}\_{T}]. |  |

To ensure the objective functional under π\pi is well defined, we impose the following condition on trading strategies:

###### Definition 2.2.

(Admissible trading strategy)
A trading strategy π\pi is admissible if π∈HBMO\pi\in H\_{\textup{BMO}} and, for some p>1p>1, it satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼t​[exp⁡(−p​ζ​(RTπ−Rtπ))]<∞,a.s.\displaystyle\mathbb{E}\_{t}\left[\exp\left(-p\zeta(R^{\pi}\_{T}-R^{\pi}\_{t})\right)\right]<\infty,\quad a.s. |  | (2.2) |

for any t∈[0,T)t\in[0,T).
We denote by Π0\Pi\_{0} the set of all admissible trading strategies.

###### Remark 2.3.

Note that we have to require 𝔼t​[exp⁡(−ζ​(RTπ−Rtπ))]<∞,a.s.\mathbb{E}\_{t}\left[\exp\left(-\zeta(R^{\pi}\_{T}-R^{\pi}\_{t})\right)\right]<\infty,a.s. to ensure that the objetive functional at time tt is well-defined. In ([2.2](https://arxiv.org/html/2511.05861v1#S2.E2 "In Definition 2.2. ‣ 2 Problem Formulation ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")), we impose a slightly stronger integrability condition (with p>1p>1). As will be shown in the subsequent discussion, this condition guarantees that the admissible set remains open under perturbations (see Lemma [2.7](https://arxiv.org/html/2511.05861v1#S2.Thmtheorem7 "Lemma 2.7. ‣ 2 Problem Formulation ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") and Corollary [2.9](https://arxiv.org/html/2511.05861v1#S2.Thmtheorem9 "Corollary 2.9. ‣ 2 Problem Formulation ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")), which is essential for the rigorous definition of the equilibrium. Moreover, it also implies that 𝔼t​[(U′​(RTπ−Rtπ))p]<∞,a.s.\mathbb{E}\_{t}\left[\left(U^{\prime}(R^{\pi}\_{T}-R^{\pi}\_{t})\right)^{p}\right]<\infty,a.s., a fact that will play a crucial role in the proof of Theorem [3.1](https://arxiv.org/html/2511.05861v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets"); see Hamaguchi\_2021 for similar conditions.

The following lemma shows that J​(t,π)<∞J(t,\pi)<\infty for any π∈Π0\pi\in\Pi\_{0}.

###### Lemma 2.4.

For π∈Π0\pi\in\Pi\_{0} and t∈[0,T)t\in[0,T), J​(t,π)J(t,\pi) is finite almost surely. Moreover, Rπ∈L𝔽2​(Ω;C​([0,T];ℝ))R^{\pi}\in L^{2}\_{\mathbb{F}}(\Omega;C([0,T];\mathbb{R})).

###### Proof.

First, by Hölder’s inequality, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼t​[exp⁡(−ζ​(RTπ−Rtπ))]≤(𝔼t​[exp⁡(−p​ζ​(RTπ−Rtπ))])1p<∞,a.s..\mathbb{E}\_{t}\left[\exp\left(-\zeta(R^{\pi}\_{T}-R^{\pi}\_{t})\right)\right]\leq\left(\mathbb{E}\_{t}\left[\exp\left(-p\zeta(R^{\pi}\_{T}-R^{\pi}\_{t})\right)\right]\right)^{\frac{1}{p}}<\infty,\quad a.s.. |  |

By the definition of the admissible strategy π\pi, it holds that

|  |  |  |
| --- | --- | --- |
|  | RTπ−Rtπ=∫tT[rs+πs​(μs−rs)−12​|σs​πs|2]​ds+πs​σs​d​Bs.R^{\pi}\_{T}-R^{\pi}\_{t}=\int\_{t}^{T}\left[r\_{s}+\pi\_{s}(\mu\_{s}-r\_{s})-\frac{1}{2}|\sigma\_{s}\pi\_{s}|^{2}\right]\mathrm{d}s+\pi\_{s}\sigma\_{s}\mathrm{d}B\_{s}. |  |

Using the standard estimate for SDE (see Theorem 3.4.3 in zhang\_backward\_2017), we obtain that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[sups∈[t,T]|Rsπ−Rtπ|2​𝟙A]=\displaystyle\mathbb{E}\left[\sup\limits\_{s\in[t,T]}\left|R^{\pi}\_{s}-R^{\pi}\_{t}\right|^{2}\mathds{1}\_{A}\right]= | C​(T)​𝔼​[(∫tT[rs+πs​(μs−rs)−12​|σs​πs|2]​𝟙A​ds)2+∫tT|πs​σs|2​𝟙A​ds]\displaystyle C(T)\mathbb{E}\left[\left(\int\_{t}^{T}\left[r\_{s}+\pi\_{s}(\mu\_{s}-r\_{s})-\frac{1}{2}|\sigma\_{s}\pi\_{s}|^{2}\right]\mathds{1}\_{A}\mathrm{d}s\right)^{2}+\int\_{t}^{T}|\pi\_{s}\sigma\_{s}|^{2}\mathds{1}\_{A}\mathrm{d}s\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | C​(‖r‖∞,‖μ‖∞,‖σ‖∞,T)​𝔼​[((∫tT|πs|2​ds)2+1)​𝟙A].\displaystyle C(\|r\|\_{\infty},\|\mu\|\_{\infty},\|\sigma\|\_{\infty},T)\mathbb{E}\left[\left(\left(\int\_{t}^{T}|\pi\_{s}|^{2}\mathrm{d}s\right)^{2}+1\right)\mathds{1}\_{A}\right]. |  |

Note that A∈ℱtA\in\mathcal{F}\_{t} is arbitrary and π∈HBMO\pi\in H\_{\textup{BMO}}, by the definition of conditional expectation and Lemma [A.1](https://arxiv.org/html/2511.05861v1#A1.Thmtheorem1 "Lemma A.1. ‣ Appendix A The Energy Inequality and the John-Nirenberg Inequality ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets"), we deduce that

|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝔼t​[|RTπ−Rtπ|])2≤𝔼t​[|RTπ−Rtπ|2]\displaystyle\left(\mathbb{E}\_{t}\left[\left|R^{\pi}\_{T}-R^{\pi}\_{t}\right|\right]\right)^{2}\leq\mathbb{E}\_{t}\left[\left|R^{\pi}\_{T}-R^{\pi}\_{t}\right|^{2}\right] | ≤𝔼t​[sups∈[t,T]|Rsπ−Rtπ|2]\displaystyle\leq\mathbb{E}\_{t}\left[\sup\limits\_{s\in[t,T]}\left|R^{\pi}\_{s}-R^{\pi}\_{t}\right|^{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C​(‖r‖∞,‖μ‖∞,‖σ‖∞,T)​(𝔼t​[(∫tT|πs|2​ds)2]+1)\displaystyle\leq C(\|r\|\_{\infty},\|\mu\|\_{\infty},\|\sigma\|\_{\infty},T)\left(\mathbb{E}\_{t}\left[\left(\int\_{t}^{T}|\pi\_{s}|^{2}\mathrm{d}s\right)^{2}\right]+1\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C​(‖r‖∞,‖μ‖∞,‖σ‖∞,T)​(‖π‖BMO4+1)<∞.\displaystyle\leq C(\|r\|\_{\infty},\|\mu\|\_{\infty},\|\sigma\|\_{\infty},T)\left(\|\pi\|\_{\textup{BMO}}^{4}+1\right)<\infty. |  |

Thus Vart​[RTπ−Rtπ]\textup{Var}\_{t}[R^{\pi}\_{T}-R^{\pi}\_{t}] is bounded, and consequently, J​(t,π)J(t,\pi) is finite for any t∈[0,T)t\in[0,T). The proof also verifies that Rπ∈L𝔽2​(Ω;C​([0,T];ℝ))R^{\pi}\in L^{2}\_{\mathbb{F}}(\Omega;C([0,T];\mathbb{R})).
∎

###### Remark 2.5.

Note that for a given admissible trading strategy π\pi, RTπ−RtπR^{\pi}\_{T}-R^{\pi}\_{t} is independent of the initial value r0r\_{0}. Hence, the definition of the admissible set Π0\Pi\_{0} is independent of the initial value r0r\_{0}.

The issue of time inconsistency arises due to the initial dependence of RtR\_{t} and the variance term, as a result, the optimal solution make no longer sense as the optimal decision today might be turned over at future dates. Instead, we seek the equilibrium solution using the game theoretic thinking with future selves. To define the equilibrium strategy, we first introduce the perturbation strategy of an admissible strategy.

###### Definition 2.6.

Assume that π\pi is an admissible strategy, for any fixed t∈[0,T)t\in[0,T), ε∈(0,T−t)\varepsilon\in(0,T-t) and η∈Lℱt∞​(Ω,ℝ)\eta\in L\_{\mathcal{F}\_{t}}^{\infty}(\Omega,\mathbb{R}), define an admissible perturbation strategy πt,ε,η\pi^{t,\varepsilon,\eta} (see Corollary [2.9](https://arxiv.org/html/2511.05861v1#S2.Thmtheorem9 "Corollary 2.9. ‣ 2 Problem Formulation ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) as follows:

|  |  |  |
| --- | --- | --- |
|  | πst,ε,η=πs+η​𝟙s∈[t,t+ε),s∈[0,T],\pi\_{s}^{t,\varepsilon,\eta}={\pi}\_{s}+\eta\mathds{1}\_{s\in[t,t+\varepsilon)},\quad s\in[0,T], |  |

where 𝟙\mathds{1} denotes the indicator function.

Let
ξt,ε,η,π:=Rπt.ε,η−Rπ\xi^{t,\varepsilon,\eta,\pi}:=R^{\pi^{t.\varepsilon,\eta}}-R^{\pi} be the difference of log return processes between πt,ε,η\pi^{t,\varepsilon,\eta} and π\pi. Then for any t∈[0,T)t\in[0,T), η∈Lℱt∞​(Ω,ℝd)\eta\in L\_{\mathcal{F}\_{t}}^{\infty}(\Omega,\mathbb{R}^{d}), ε∈(0,T−t)\varepsilon\in(0,T-t) and an admissible strategy π\pi, ξt,ε,π:=ξt,ε,η,π\xi^{t,\varepsilon,\pi}:=\xi^{t,\varepsilon,\eta,\pi}333For notation simplicity, we drop the superscript η\eta. is the unique solution of the SDE444Formally, both Rπt.ε,ηR^{\pi^{t.\varepsilon,\eta}} and ξt,ε,π\xi^{t,\varepsilon,\pi} can be defined on the entire interval [0,T][0,T]. Nevertheless, in view of the definition of equilibrium, it suffices to consider them only on [t,T][t,T].  that

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​ξst,ε,π=(a​(s,πst,ε,η)−a​(s,πs))​d​s+σs​η​1s∈[t,t+ε)​d​Bs,ξtt,ε,π=0.\left\{\begin{aligned} &\mathrm{d}\xi\_{s}^{t,\varepsilon,\pi}=\left(a(s,\pi^{t,\varepsilon,\eta}\_{s})-a(s,\pi\_{s})\right)\mathrm{d}s+\sigma\_{s}\eta 1\_{s\in[t,t+\varepsilon)}\mathrm{d}B\_{s},\\ &\xi\_{t}^{t,\varepsilon,\pi}=0.\end{aligned}\right. |  | (2.3) |

Here, a​(s,π):=rs+(μs−rs)​π−12​|σs​π|2a(s,\pi):=r\_{s}+(\mu\_{s}-r\_{s})\pi-\frac{1}{2}|\sigma\_{s}\pi|^{2} . In the following lemma, we will first establish some fundamental properties of ξt,ε,π\xi^{t,\varepsilon,\pi}.

###### Lemma 2.7.

Let t∈[0,T)t\in[0,T) and η∈Lℱt∞​(Ω,ℝ)\eta\in L\_{\mathcal{F}\_{t}}^{\infty}(\Omega,\mathbb{R}) be fixed.

1. 1.

   For any ε∈(0,T−t)\varepsilon\in(0,T-t), ξt,ε,π∈L𝔽k​(Ω;C​([t,T];ℝ))\xi^{t,\varepsilon,\pi}\in L\_{\mathbb{F}}^{k}(\Omega;C([t,T];\mathbb{R})) for any k≥1k\geq 1.
2. 2.

   For any k≥1k\geq 1, there exists a constant C​(‖r‖∞,‖μ‖∞,‖σ‖∞,T,k,‖π‖BMO)C(\|r\|\_{\infty},\|\mu\|\_{\infty},\|\sigma\|\_{\infty},T,k,\|\pi\|\_{\textup{BMO}}) such that
   E\_t[sup\_s∈[t,T]—ξ\_s^t,ε,π—^2k]≤C(∥r∥\_∞,∥μ∥\_∞,∥σ∥\_∞,T,k,∥π∥\_BMO)(ε—η—^2)^k, a.s.
   for ε∈(0,T−t)\varepsilon\in(0,T-t) sufficiently small.
3. 3.

   For any c>0,π∈Π0,ε∈(0,T−t)c>0,\pi\in\Pi\_{0},\varepsilon\in(0,T-t), it holds that supε∈(0,T−t)𝔼t​[exp⁡(c​|ξTt,ε,π|)]<C​(c,π,‖η‖∞)<∞,ℙ−a.s.\sup\limits\_{\varepsilon\in(0,T-t)}\mathbb{E}\_{t}\left[\exp(c|\xi^{t,\varepsilon,\pi}\_{T}|)\right]<C(c,\pi,\|\eta\|\_{\infty})<\infty,\mathbb{P}-a.s., where C​(c,π,‖η‖∞)C(c,\pi,\|\eta\|\_{\infty}) denotes a constant depending only on c,π,‖η‖∞c,\pi,\|\eta\|\_{\infty}, but independent of ϵ\epsilon, and is increasing with respect to ‖η‖∞\|\eta\|\_{\infty}.

###### Proof.

The first assertion is standard, see Theorem 3.4.3 in zhang\_backward\_2017. The proof of the second assertion is similar to the ones of Lemma [2.4](https://arxiv.org/html/2511.05861v1#S2.Thmtheorem4 "Lemma 2.4. ‣ 2 Problem Formulation ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") and Lemma 2.5 in Hamaguchi\_2021. Indeed, for any set A∈ℱtA\in\mathcal{F}\_{t}, it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[sups∈[t,T]|ξst,ε,π|2​k​𝟙A]≤\displaystyle\mathbb{E}\left[\sup\limits\_{s\in[t,T]}|\xi\_{s}^{t,\varepsilon,\pi}|^{2k}\mathds{1}\_{A}\right]\leq | C​𝔼​[(∫tt+ε|(μs−rs)​η−12​σs2​η2−σs2​πs​η|​𝟙A​ds)2​k+(∫tt+ε|σs​η|2​𝟙A​ds)k]\displaystyle C\mathbb{E}\left[\left(\int\_{t}^{t+\varepsilon}\left|(\mu\_{s}-r\_{s})\eta-\frac{1}{2}\sigma\_{s}^{2}\eta^{2}-\sigma\_{s}^{2}\pi\_{s}\eta\right|\mathds{1}\_{A}\mathrm{d}s\right)^{2k}+\left(\int\_{t}^{t+\varepsilon}|\sigma\_{s}\eta|^{2}\mathds{1}\_{A}\mathrm{d}s\right)^{k}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | C​𝔼​[{(ε+ε​η+ε12​(∫tt+ε|π|2​ds)12)2​k​|η|2​k+εk​|η|2​k}​𝟙A]\displaystyle C\mathbb{E}\left[\left\{\left(\varepsilon+\varepsilon\eta+\varepsilon^{\frac{1}{2}}\left(\int\_{t}^{t+\varepsilon}|\pi|^{2}\mathrm{d}s\right)^{\frac{1}{2}}\right)^{2k}|\eta|^{2k}+\varepsilon^{k}|\eta|^{2k}\right\}\mathds{1}\_{A}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | C​𝔼​[((ε​|η|2)k​[(∫tt+ε|πs|2​ds)k+1]+o​(εk))​𝟙A].\displaystyle C\mathbb{E}\left[\left((\varepsilon|\eta|^{2})^{k}\left[\left(\int\_{t}^{t+\varepsilon}|\pi\_{s}|^{2}\mathrm{d}s\right)^{k}+1\right]+o(\varepsilon^{k})\right)\mathds{1}\_{A}\right]. |  |

Here, we have omitted the dependence of CC for simplicity. Then, it follows that

|  |  |  |
| --- | --- | --- |
|  | 𝔼t​[sups∈[t,T]|ξst,ε,π|2​k]≤C​(ε​|η|2)k​(1+𝔼t​[(∫tT|πs|2​ds)k])≤C​(ε​|η|2)k,\mathbb{E}\_{t}\left[\sup\limits\_{s\in[t,T]}|\xi\_{s}^{t,\varepsilon,\pi}|^{2k}\right]\leq C(\varepsilon|\eta|^{2})^{k}\left(1+\mathbb{E}\_{t}\left[\left(\int\_{t}^{T}|\pi\_{s}|^{2}\mathrm{d}s\right)^{k}\right]\right)\leq C(\varepsilon|\eta|^{2})^{k}, |  |

where we have used the fact that π∈HBMO\pi\in H\_{\textup{BMO}} and the conditional version of the energy inequality (see Lemma [A.1](https://arxiv.org/html/2511.05861v1#A1.Thmtheorem1 "Lemma A.1. ‣ Appendix A The Energy Inequality and the John-Nirenberg Inequality ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")).

For the third assertion, note that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼t​[exp⁡(c​|ξTt,ε,π|)]\displaystyle\mathbb{E}\_{t}\left[\exp(c|\xi^{t,\varepsilon,\pi}\_{T}|)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼t​[exp⁡(c​∫tt+ε((μs−rs)​η−12​σs2​η2−σs2​πs​η)​ds+c​∫tt+εσs​η​dBs)]\displaystyle\mathbb{E}\_{t}\left[\exp\left(c\int\_{t}^{t+\varepsilon}\left((\mu\_{s}-r\_{s})\eta-\frac{1}{2}\sigma\_{s}^{2}\eta^{2}-\sigma\_{s}^{2}\pi\_{s}\eta\right)\mathrm{d}s+c\int\_{t}^{t+\varepsilon}\sigma\_{s}\eta\mathrm{d}B\_{s}\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | C​(c,η)​(𝔼t​[exp⁡(2​c​‖σ‖∞2​|η|​∫tT|πs|​ds)])12​(𝔼t​[exp⁡(2​c​∫tt+εσs​η​dBs−2​c2​∫tt+ε|σs​η|2)])12\displaystyle C(c,\eta)\left(\mathbb{E}\_{t}\left[\exp\left(2c\|\sigma\|^{2}\_{\infty}|\eta|\int\_{t}^{T}|\pi\_{s}|\mathrm{d}s\right)\right]\right)^{\frac{1}{2}}\left(\mathbb{E}\_{t}\left[\exp\left(2c\int\_{t}^{t+\varepsilon}\sigma\_{s}\eta\mathrm{d}B\_{s}-2c^{2}\int\_{t}^{t+\varepsilon}|\sigma\_{s}\eta|^{2}\right)\right]\right)^{\frac{1}{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | C​(c,δ,‖η‖∞)​(𝔼t​[exp⁡(δ​∫tT|πs|2​ds)])12​(𝔼t​[exp⁡(2​c​∫tt+εσs​η​dBs−2​c2​∫tt+ε|σs​η|2​ds)])12.\displaystyle C(c,\delta,\|\eta\|\_{\infty})\left(\mathbb{E}\_{t}\left[\exp\left(\delta\int\_{t}^{T}|\pi\_{s}|^{2}\mathrm{d}s\right)\right]\right)^{\frac{1}{2}}\left(\mathbb{E}\_{t}\left[\exp\left(2c\int\_{t}^{t+\varepsilon}\sigma\_{s}\eta\mathrm{d}B\_{s}-2c^{2}\int\_{t}^{t+\varepsilon}|\sigma\_{s}\eta|^{2}\mathrm{d}s\right)\right]\right)^{\frac{1}{2}}. |  |

In view that σ\sigma and η\eta are bounded, the Novikov condition is satisfied such that the second term equals 11 a.s.. We also note that C​(c,δ)C(c,\delta) can be chosen independent of ε\varepsilon. In fact, we can choose

|  |  |  |
| --- | --- | --- |
|  | C​(c,δ,‖η‖∞)=exp⁡(c​(T−t)​(‖μ−r‖∞⋅‖η‖∞+12​‖σ‖∞2​‖η‖∞2)+c2​(T−t)​‖σ‖∞2​‖η‖∞2+Tδ​(2​c​‖σ‖∞2​‖η‖∞)2).C(c,\delta,\|\eta\|\_{\infty})=\exp\left(c(T-t)\left(\|\mu-r\|\_{\infty}\cdot\|\eta\|\_{\infty}+\frac{1}{2}\|\sigma\|\_{\infty}^{2}\|\eta\|\_{\infty}^{2}\right)+c^{2}(T-t)\|\sigma\|\_{\infty}^{2}\|\eta\|\_{\infty}^{2}+\frac{T}{\delta}\left(2c\|\sigma\|^{2}\_{\infty}\|\eta\|\_{\infty}\right)^{2}\right). |  |

By the John–Nirenberg inequality (see Lemma [A.2](https://arxiv.org/html/2511.05861v1#A1.Thmtheorem2 "Lemma A.2. ‣ Appendix A The Energy Inequality and the John-Nirenberg Inequality ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")), for δ>0\delta>0 such that δ​‖π‖BMO2<1\delta\|\pi\|\_{\textup{BMO}}^{2}<1, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼t​[exp⁡(δ​∫tT|πs|2​ds)]<11−δ​‖π‖BMO2<∞a.s..\mathbb{E}\_{t}\left[\exp\left(\delta\int\_{t}^{T}|\pi\_{s}|^{2}\mathrm{d}s\right)\right]<\frac{1}{1-\delta\|\pi\|\_{\textup{BMO}}^{2}}<\infty\quad a.s.. |  |

As a result,

|  |  |  |
| --- | --- | --- |
|  | supε∈(0,T−t)𝔼t​[exp⁡(c​|ξTt,ε,π|)]≤C​(c,δ,‖η‖∞)​(11−δ​‖π‖BMO2)12<∞a.s..\sup\limits\_{\varepsilon\in(0,T-t)}\mathbb{E}\_{t}\left[\exp(c|\xi^{t,\varepsilon,\pi}\_{T}|)\right]\leq C(c,\delta,\|\eta\|\_{\infty})\left(\frac{1}{1-\delta\|\pi\|\_{\textup{BMO}}^{2}}\right)^{\frac{1}{2}}<\infty\quad a.s.. |  |

∎

###### Remark 2.8.

The above result is similar to Lemma 2.5 in Hamaguchi\_2021. However, as the control process appears in the SDE governing the difference process, ξt,ε,π\xi^{t,\varepsilon,\pi} cannot satisfy the properties in Hamaguchi\_2021 under arbitrary trading strategies. This motivates us to consider the BMO condition into the definition of our admissible strategies. Consequently, the proof differs from that of Lemma 2.5 in Hamaguchi\_2021.

###### Corollary 2.9.

Assume that π\pi is an admissible trading strategy, for any t∈[0,T)t\in[0,T) and η∈Lℱt∞​(Ω,ℝ)\eta\in L\_{\mathcal{F}\_{t}}^{\infty}(\Omega,\mathbb{R}),
πt,ε,η\pi^{t,\varepsilon,\eta} is an admissible strategy.

###### Proof.

We can choose 1<p′<p1<p^{\prime}<p and q>1q>1 such that 1p+1q=1p′\frac{1}{p}+\frac{1}{q}=\frac{1}{p^{\prime}}. By Lemma [2.7](https://arxiv.org/html/2511.05861v1#S2.Thmtheorem7 "Lemma 2.7. ‣ 2 Problem Formulation ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets"), it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | (𝔼t​[exp⁡(−p′​ζ​(RTπt,ε,η−Rtπt,ε,η))])1p′\displaystyle\left(\mathbb{E}\_{t}\left[\exp\left(-p^{\prime}\zeta(R^{\pi^{t,\varepsilon,\eta}}\_{T}-R^{\pi^{t,\varepsilon,\eta}}\_{t})\right)\right]\right)^{\frac{1}{p^{\prime}}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | (𝔼t​[exp⁡(−p′​ζ​[(RTπ−Rtπ)+ξTt,ε,π])])1p′\displaystyle\left(\mathbb{E}\_{t}\left[\exp\left(-p^{\prime}\zeta\left[(R^{\pi}\_{T}-R^{\pi}\_{t})+\xi\_{T}^{t,\varepsilon,\pi}\right]\right)\right]\right)^{\frac{1}{p^{\prime}}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | (𝔼t​[exp⁡(−p​ζ​(RTπ−Rtπ))])1p​(𝔼t​[exp⁡(q​ζ​|ξTt,ε,π|)])1q<∞​a.s..\displaystyle\left(\mathbb{E}\_{t}\left[\exp\left(-p\zeta(R^{\pi}\_{T}-R^{\pi}\_{t})\right)\right]\right)^{\frac{1}{p}}\left(\mathbb{E}\_{t}\left[\exp\left(q\zeta\left|\xi\_{T}^{t,\varepsilon,\pi}\right|\right)\right]\right)^{\frac{1}{q}}<\infty\;a.s.. |  |

Moreover, it is obvious that under a bounded perturbation η\eta,

|  |  |  |
| --- | --- | --- |
|  | ‖πt,ε,η‖BMO2≤2​supτ∈𝒯[0,T]‖𝔼τ​[∫τT|πs|2​𝑑s]‖∞+2​ε​‖η‖∞2<∞.\|\pi^{t,\varepsilon,\eta}\|\_{\textup{BMO}}^{2}\leq 2\sup\_{\tau\in\mathcal{T}\_{[0,T]}}\left\|\mathbb{E}\_{\tau}\left[\int\_{\tau}^{T}|\pi\_{s}|^{2}ds\right]\right\|\_{\infty}+2\varepsilon\|\eta\|\_{\infty}^{2}<\infty. |  |

Thus, πt,ε,η\pi^{t,\varepsilon,\eta} is an admissible strategy.
∎

Next we give the definition of our (open-loop) time-consistent equilibrium strategy using the intra-personal game theoretic thinking by perturbation, which is inspired by hu\_time-inconsistent\_2012; hu\_time-inconsistent\_2017.

###### Definition 2.10.

For π^∈Π0\hat{\pi}\in\Pi\_{0}, π^\hat{\pi} is called a time-consistent equilibrium strategy if

|  |  |  |
| --- | --- | --- |
|  | lim supε→0J​(t,π^t,ε,η)−J​(t,π^)ε≤0a.s.,\limsup\limits\_{\varepsilon\rightarrow 0}\frac{J(t,\hat{\pi}^{t,\varepsilon,\eta})-J(t,\hat{\pi})}{\varepsilon}\leq 0\quad a.s., |  |

for any t∈[0,T)t\in[0,T) and any η∈Lℱt∞​(Ω,ℝ)\eta\in L\_{\mathcal{F}\_{t}}^{\infty}(\Omega,\mathbb{R}).

###### Remark 2.11.

In the following sections, we often fix a candidate equilibrium strategy π^\hat{\pi} or an arbitrary admissible strategy π\pi for analysis. In proving the necessary conditions or verifying equilibrium, we will work with the perturbed log return process under a fixed perturbation η\eta. To ease presentation, we denote by π^t,ϵ,πt,ϵ\hat{\pi}^{t,\epsilon},\pi^{t,\epsilon} the perturbation strategy π^t,ϵ,η,πt,ϵ,η\hat{\pi}^{t,\epsilon,\eta},\pi^{t,\epsilon,\eta}, and denote by R^,R\hat{R},R the log return process Rπ^,Rπ{R}^{\hat{\pi}},R^{\pi}, and denote by R^t,ε,Rt,ε\hat{R}^{t,\varepsilon},R^{t,\varepsilon} the perturbed log return process Rπ^t,ϵ,η,Rπt,ϵ,η{R}^{\hat{\pi}^{t,\epsilon,\eta}},{R}^{\pi^{t,\epsilon,\eta}}, and denote by ξt,ε\xi^{t,\varepsilon} the difference process ξt,ε,π\xi^{t,\varepsilon,\pi} under the perturbation. For simplicity, we also use the notations u^:=σ​π^\hat{u}:=\sigma\hat{\pi} and u:=σ​πu:=\sigma\pi in the following sections.

## 3 A Necessary Condition of Time-Consistent Equilibria

In this section, we establish several properties of admissible strategies and characterize the necessary conditions of a time-consistent equilibrium by a BSDE system. Without loss of generality, we consider a fixed pp such that any admissible strategy satisfies

|  |  |  |
| --- | --- | --- |
|  | 𝔼t​[exp⁡(−p​ζ​(RTπ−Rtπ))]<∞,a.s..\mathbb{E}\_{t}\left[\exp\left(-p\zeta(R^{\pi}\_{T}-R^{\pi}\_{t})\right)\right]<\infty,\quad a.s.. |  |

###### Theorem 3.1.

If π^∈Π0\hat{\pi}\in\Pi\_{0} is a time-consistent equilibrium strategy, there exist (Y,Y~)(Y,\tilde{Y}) and (Z1,Z,Z~1,Z~)(Z^{1},Z,\tilde{Z}^{1},\tilde{Z}) such that

1. 1.

   YY and Y~\tilde{Y} are continuous and adapted processes such that exp⁡(−ζ​(R^+Y))∈L𝔽p​(Ω;C​([0,T];ℝ))\exp\left(-\zeta(\hat{R}+Y)\right)\in L^{p}\_{\mathbb{F}}(\Omega;C([0,T];\mathbb{R})) and Y~∈L𝔽2​(Ω;C​([0,T];ℝ))\tilde{Y}\in L^{2}\_{\mathbb{F}}(\Omega;C([0,T];\mathbb{R})). Moreover, (Z1,Z~1,Z,Z~)(Z^{1},\tilde{Z}^{1},Z,\tilde{Z}) are ℝ\mathbb{R}-valued progressively measurable processes such that
   ∫\_0^T (—Z\_s^1—^2+—Z\_s—^2+—~Z\_s^1—^2+—~Z\_s—^2)ds¡∞, P-a.s..
2. 2.

   (Y,Y~)(Y,\tilde{Y}) and (Z1,Z,Z~1,Z~)(Z^{1},Z,\tilde{Z}^{1},\tilde{Z}) satisfy the following coupled BSDE system:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | {d​Ys=(ζ2​|Zs1+σs​π^s+ρ​Zs|2+ζ​(1−ρ2)2​|Zs|2−a​(s,π^s))​d​s+Zs1​d​Bs+Zs​d​B¯s,d​Y~s=−a​(s,π^s)​d​s+Z~s1​d​Bs+Z~s​d​B¯s,YT=0,YT~=0.\left\{\begin{aligned} &\mathrm{d}Y\_{s}=\left(\frac{\zeta}{2}|Z\_{s}^{1}+\sigma\_{s}\hat{\pi}\_{s}+\rho Z\_{s}|^{2}+\frac{\zeta(1-\rho^{2})}{2}|Z\_{s}|^{2}-a(s,\hat{\pi}\_{s})\right)\mathrm{d}s+Z\_{s}^{1}\mathrm{d}B\_{s}+Z\_{s}\mathrm{d}\bar{B}\_{s},\\ &\mathrm{d}\tilde{Y}\_{s}=-a(s,\hat{\pi}\_{s})\mathrm{d}s+\tilde{Z}^{1}\_{s}\mathrm{d}B\_{s}+\tilde{Z}\_{s}\mathrm{d}\bar{B}\_{s},\\ &Y\_{T}=0,\\ &\tilde{Y\_{T}}=0.\end{aligned}\right. |  | (3.1) |

Furthermore, the equilibrium strategy is characterized by

|  |  |  |
| --- | --- | --- |
|  | π^=σ−1​e−ζ​Y​θ−ζ​e−ζ​Y​(Z1+ρ​Z)−γ​(Z~1+ρ​Z~)(ζ+1)​e−ζ​Y+γ.\hat{\pi}=\sigma^{-1}\frac{e^{-\zeta Y}\theta-\zeta e^{-\zeta Y}(Z^{1}+\rho Z)-\gamma(\tilde{Z}^{1}+\rho\tilde{Z})}{(\zeta+1)e^{-\zeta Y}+\gamma}. |  |

###### Remark 3.2.

When the market model becomes complete, i.e., the second Brownian motion B¯\bar{B} is absent, the BSDE system ([3.1](https://arxiv.org/html/2511.05861v1#S3.E1 "In item 2 ‣ Theorem 3.1. ‣ 3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) degenerates to

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​Ys=(ζ2​|Zs+u^s|2−a​(s,π^s))​d​s+Zs​d​Bs,d​Y~s=−a​(s,π^s)​d​s+Z~​d​Bs,YT=0,YT~=0.\left\{\begin{aligned} &\mathrm{d}Y\_{s}=\left(\frac{\zeta}{2}|Z\_{s}+\hat{u}\_{s}|^{2}-a(s,\hat{\pi}\_{s})\right)\mathrm{d}s+Z\_{s}\mathrm{d}B\_{s},\\ &\mathrm{d}\tilde{Y}\_{s}=-a(s,\hat{\pi}\_{s})\mathrm{d}s+\tilde{Z}\mathrm{d}B\_{s},\\ &Y\_{T}=0,\\ &\tilde{Y\_{T}}=0.\end{aligned}\right. |  | (3.2) |

The equilibrium strategy takes the form π^=σ−1​e−ζ​Y​θ−ζ​e−ζ​Y​Z−γ​Z~(ζ+1)​e−ζ​Y+γ\hat{\pi}=\sigma^{-1}\frac{e^{-\zeta Y}\theta-\zeta e^{-\zeta Y}Z-\gamma\tilde{Z}}{(\zeta+1)e^{-\zeta Y}+\gamma}.
We observe that the BSDE system admits a solution when Z=0Z=0 and Z~=0\tilde{Z}=0, thus an equilibrium is given by

|  |  |  |
| --- | --- | --- |
|  | π^=σ−1​e−ζ​Y​θ(ζ+1)​e−ζ​Y+γ,\hat{\pi}=\sigma^{-1}\frac{e^{-\zeta Y}\theta}{(\zeta+1)e^{-\zeta Y}+\gamma}, |  |

where YY is the solution of the ODE with terminal condition:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​Ys=(ζ2​|u^s|2−a​(s,π^s))​d​s,YT=0.\displaystyle\left\{\begin{aligned} &\mathrm{d}Y\_{s}=\left(\frac{\zeta}{2}|\hat{u}\_{s}|^{2}-a(s,\hat{\pi}\_{s})\right)\mathrm{d}s,\\ &Y\_{T}=0.\end{aligned}\right. |  | (3.3) |

Let A=e−ζ​YA=e^{-\zeta Y}, then AA satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | At=A​(f​(A)):=−ζ​(ζ+1)​A3​θ22​((ζ+1)​A+γ)2+ζ​A2​θ2(ζ+1)​A+γ+r​ζ​A,\displaystyle A\_{t}=A(f(A)):=-\frac{\zeta(\zeta+1)A^{3}\theta^{2}}{2((\zeta+1)A+\gamma)^{2}}+\frac{\zeta A^{2}\theta^{2}}{(\zeta+1)A+\gamma}+r\zeta A, |  | (3.4) |

with the terminal condition A​(T)=1A(T)=1.
It is clear that AA has a lower bound 0. Combining A′=A​(f​(A))A^{\prime}=A(f(A)) and the fact that f​(A)f(A) is bounded, we deduce that AA is bounded from above and thus there exists a unique solution and AA is positive.

###### Remark 3.3.

Hamaguchi\_2021 derives a one-dimensional FBSDE as a necessary condition for an equilibrium in a general non-exponential time-inconsistent problem. In our setting, however, the introduced variance must to be represented by another BSDE of Y~\tilde{Y}, which leads to strong coupling in our equation. Although dai\_dynamic\_2021 study a mean-variance framework including a variance term in their objective function, it is straightforward to see that the mean term can be represented by the BSDE of Y~\tilde{Y}. In fact, Y~:=𝔼t​[RT−Rt]\tilde{Y}:=\mathbb{E}\_{t}[R\_{T}-R\_{t}] (see in Lemma [3.4](https://arxiv.org/html/2511.05861v1#S3.Thmtheorem4 "Lemma 3.4. ‣ 3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") later) corresponds precisely to the mean term at time tt. Hence, their analysis also focus on a one-dimensional BSDE. Unlike Hamaguchi\_2021 and dai\_dynamic\_2021, we focus on a two-dimensional fully coupled quadratic BSDE system.

To prove Theorem [3.1](https://arxiv.org/html/2511.05861v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets"), we need some auxiliary preparations.

###### Lemma 3.4.

For any admissible strategy π∈Π0\pi\in\Pi\_{0}, there exists (Y,Y~)(Y,\tilde{Y}) and (Z1,Z,Z~1,Z~)(Z^{1},Z,\tilde{Z}^{1},\tilde{Z}) satisfying the BSDEs ([3.1](https://arxiv.org/html/2511.05861v1#S3.E1 "In item 2 ‣ Theorem 3.1. ‣ 3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) (with π^\hat{\pi} replaced by π\pi) such that, for any t∈[0,T)t\in[0,T), η∈Lℱt∞​(Ω,ℝd)\eta\in L\_{\mathcal{F}\_{t}}^{\infty}(\Omega,\mathbb{R}^{d}) and ε∈(0,T−t)\varepsilon\in(0,T-t), it holds that, a.s.,

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | J​(t,Rt,πt,ε)−J​(t,Rt,π)\displaystyle J(t,R\_{t},\pi^{t,\varepsilon})-J(t,R\_{t},\pi) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼t​[∫tt+εe−ζ​(Rs+Ys−Rt)​(a​(s,πst,ε)−a​(s,πs)−ζ​(Zs1+σs​πs+ρ​Z)⋅σs​η)​ds]\displaystyle\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}e^{-\zeta(R\_{s}+Y\_{s}-R\_{t})}(a(s,\pi^{t,\varepsilon}\_{s})-a(s,\pi\_{s})-\zeta(Z\_{s}^{1}+\sigma\_{s}\pi\_{s}+\rho Z)\cdot\sigma\_{s}\eta)\mathrm{d}s\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −ζ​𝔼t​[∫01e−ζ​(RT+λ​ξTt,ε−Rt)​(1−λ)​𝑑λ​|ξTt,ε|2]\displaystyle-\zeta\mathbb{E}\_{t}\left[\int\_{0}^{1}e^{-\zeta(R\_{T}+\lambda\xi\_{T}^{t,\varepsilon}-R\_{t})}(1-\lambda)d\lambda|\xi\_{T}^{t,\varepsilon}|^{2}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +γ2​𝔼t​[∫tt+ε((σs​πs+Z~s1+ρ​Z~s)2−(σs​πst,ε+Z~s1+ρ​Z~s)2)​ds].\displaystyle+\frac{\gamma}{2}\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}((\sigma\_{s}\pi\_{s}+\tilde{Z}\_{s}^{1}+\rho\tilde{Z}\_{s})^{2}-(\sigma\_{s}\pi\_{s}^{t,\varepsilon}+\tilde{Z}\_{s}^{1}+\rho\tilde{Z}\_{s})^{2})\mathrm{d}s\right]. |  |

###### Proof.

Fix the strategy π\pi, t∈[0,T)t\in[0,T), η∈Lℱt∞​(Ω,ℝd)\eta\in L\_{\mathcal{F}\_{t}}^{\infty}(\Omega,\mathbb{R}^{d}) and ε∈(0,T−t)\varepsilon\in(0,T-t). By the definition of JJ, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | J​(t,Rt,πt,ε)−J​(t,Rt,π)=𝔼t​[U​(RTt,ε−Rt)−U​(RT−Rt)]−γ2​(Vart​[RTt,ε]−Vart​[RT])\displaystyle J(t,R\_{t},\pi^{t,\varepsilon})-J(t,R\_{t},\pi)=\mathbb{E}\_{t}\left[U(R\_{T}^{t,\varepsilon}-R\_{t})-U(R\_{T}-R\_{t})\right]-\frac{\gamma}{2}\left(\textup{Var}\_{t}[R\_{T}^{t,\varepsilon}]-\textup{Var}\_{t}[R\_{T}]\right) |  |

For the first term, we have that

|  |  |  |
| --- | --- | --- |
|  | 𝔼t​[U​(RTt,ε−Rt)−U​(RT−Rt)]=eζ​Rt​𝔼t​[U′​(RT)​ξTt,ε+∫01U′′​(RT+λ​ξTt,ε)​(1−λ)​𝑑λ​|ξTt,ε|2].\displaystyle\mathbb{E}\_{t}\left[U(R\_{T}^{t,\varepsilon}-R\_{t})-U(R\_{T}-R\_{t})\right]=e^{\zeta R\_{t}}\mathbb{E}\_{t}\left[U^{{}^{\prime}}(R\_{T})\xi\_{T}^{t,\varepsilon}+\int\_{0}^{1}U^{{}^{\prime\prime}}(R\_{T}+\lambda\xi\_{T}^{t,\varepsilon})(1-\lambda)d\lambda|\xi\_{T}^{t,\varepsilon}|^{2}\right]. |  |

Next we analyze the conditional expectation 𝔼t​[U′​(RT)​ξTt,ε]\mathbb{E}\_{t}\left[U^{{}^{\prime}}(R\_{T})\xi\_{T}^{t,\varepsilon}\right] and let (α,β)(\alpha,\beta) be the unique adapted solution of the BSDE

|  |  |  |
| --- | --- | --- |
|  | {d​αs=βs1​d​Bs+βs​d​B¯s,αT=e−ζ​RT.\left\{\begin{aligned} &\mathrm{d}\alpha\_{s}=\beta\_{s}^{1}\mathrm{d}B\_{s}+\beta\_{s}\mathrm{d}\bar{B}\_{s},\\ &\alpha\_{T}=e^{-\zeta R\_{T}}.\end{aligned}\right. |  |

The martingale representation theorem impllies that αs=𝔼s​[U′​(RT)]\alpha\_{s}=\mathbb{E}\_{s}\left[U^{{}^{\prime}}(R\_{T})\right]. By the definition of the admissible strategy, it holds that αT∈LℱTp​(Ω;ℝ)\alpha\_{T}\in L^{p}\_{\mathcal{F}\_{T}}(\Omega;\mathbb{R}) for some p>1p>1. Let Y=−1ζ​log⁡α−RY=-\frac{1}{\zeta}\log\alpha-R and hence U′​(Rs+Ys)=αs=𝔼s​[U′​(RT)]U^{{}^{\prime}}(R\_{s}+Y\_{s})=\alpha\_{s}=\mathbb{E}\_{s}\left[U^{{}^{\prime}}(R\_{T})\right]. In particular, α\alpha is positive and YY is well defined for any t∈[0,T]t\in[0,T] a.s.. Moreover, α∈L𝔽p​(Ω;C​([0,T];ℝ))\alpha\in L^{p}\_{\mathbb{F}}(\Omega;C([0,T];\mathbb{R})) and β1,β∈L𝔽p​(Ω;L2​(0,T;ℝ))\beta^{1},\beta\in L^{p}\_{\mathbb{F}}\left(\Omega;L^{2}(0,T;\mathbb{R})\right). Then YY is an adapted process satisfying the following BSDE that

|  |  |  |
| --- | --- | --- |
|  | {d​Ys=(12​ζ​αs2​(|βs1|2+|βs|2+2​ρ​βs1​βs)−a​(s,πs))​d​s−(βs1ζ​αs+σ​πs)​d​Bs−βsζ​αs​d​B¯s,YT=0.\left\{\begin{aligned} &\mathrm{d}Y\_{s}=\left(\frac{1}{2\zeta\alpha\_{s}^{2}}\left(|\beta\_{s}^{1}|^{2}+|\beta\_{s}|^{2}+2\rho\beta\_{s}^{1}\beta\_{s}\right)-a(s,\pi\_{s})\right)\mathrm{d}s-\left(\frac{\beta\_{s}^{1}}{\zeta\alpha\_{s}}+\sigma\pi\_{s}\right)\mathrm{d}B\_{s}-\frac{\beta\_{s}}{\zeta\alpha\_{s}}\mathrm{d}\bar{B}\_{s},\\ &Y\_{T}=0.\end{aligned}\right. |  |

Let Z1=−β1ζ​α−σ​πZ^{1}=-\frac{\beta^{1}}{\zeta\alpha}-\sigma\pi and Z=−βζ​αZ=-\frac{\beta}{\zeta\alpha}, it then holds that

|  |  |  |
| --- | --- | --- |
|  | d​Ys=(ζ2​|Zs1+σs​π+ρ​Zs|2+ζ​(1−ρ2)2​|Zs|2−a​(s,πs))​d​s+Zs1​d​Bs+Z1​d​B¯s.\mathrm{d}Y\_{s}=\left(\frac{\zeta}{2}|Z\_{s}^{1}+\sigma\_{s}\pi+\rho Z\_{s}|^{2}+\frac{\zeta(1-\rho^{2})}{2}|Z\_{s}|^{2}-a(s,\pi\_{s})\right)\mathrm{d}s+Z\_{s}^{1}\mathrm{d}B\_{s}+Z^{1}\mathrm{d}\bar{B}\_{s}. |  |

Moreover, by taking the conditional expectations, we see that

|  |  |  |
| --- | --- | --- |
|  | 𝔼t​[U′​(RT)​ξTt,ε]=𝔼t​[αT​ξt+εt,ε]=𝔼t​[𝔼​[αT|ℱt+ε]​ξt+εt,ε]=𝔼t​[αt+ε​ξt+εt,ε]=𝔼t​[U′​(Rt+ε+Yt+ε)​ξt+εt,ε].\mathbb{E}\_{t}\left[U^{{}^{\prime}}(R\_{T})\xi\_{T}^{t,\varepsilon}\right]=\mathbb{E}\_{t}[\alpha\_{T}\xi\_{t+\varepsilon}^{t,\varepsilon}]=\mathbb{E}\_{t}\left[\mathbb{E}[\alpha\_{T}|\mathcal{F}\_{t+\varepsilon}]\xi\_{t+\varepsilon}^{t,\varepsilon}\right]=\mathbb{E}\_{t}[\alpha\_{t+\varepsilon}\xi\_{t+\varepsilon}^{t,\varepsilon}]=\mathbb{E}\_{t}\left[U^{{}^{\prime}}(R\_{t+\varepsilon}+Y\_{t+\varepsilon})\xi\_{t+\varepsilon}^{t,\varepsilon}\right]. |  |

Ito^\hat{\text{o}}’s formula gives that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼t​[U′​(Rt+ε+Yt+ε)​ξt+εt,ε]\displaystyle\mathbb{E}\_{t}\left[U^{{}^{\prime}}(R\_{t+\varepsilon}+Y\_{t+\varepsilon})\xi\_{t+\varepsilon}^{t,\varepsilon}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼t[∫tt+εU′(Rs+Ys)((a(s,πst,ε)−a(s,πs))ds+σsηdBs)\displaystyle\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}U^{{}^{\prime}}(R\_{s}+Y\_{s})\left(\left(a(s,\pi^{t,\varepsilon}\_{s})-a(s,\pi\_{s})\right)\mathrm{d}s+\sigma\_{s}\eta\mathrm{d}B\_{s}\right)\right. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫tt+εξst,ε​U′′​(Rs+Ys)​((Zs1+σs​πs)​d​Bs+Zs​d​B¯s+(ζ2​|Zs1+σs​πs+ρ​Zs|2+ζ​(1−ρ2)2​|Zs|2)​d​s)\displaystyle+\int\_{t}^{t+\varepsilon}\xi\_{s}^{t,\varepsilon}U^{{}^{\prime\prime}}(R\_{s}+Y\_{s})\left((Z\_{s}^{1}+\sigma\_{s}\pi\_{s})\mathrm{d}B\_{s}+Z\_{s}\mathrm{d}\bar{B}\_{s}+\left(\frac{\zeta}{2}|Z\_{s}^{1}+\sigma\_{s}\pi\_{s}+\rho Z\_{s}|^{2}+\frac{\zeta(1-\rho^{2})}{2}|Z\_{s}|^{2}\right)\mathrm{d}s\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +12​∫tt+εξst,ε​U′′′​(Rs+Ys)​(|Zs1+σs​πs|2+|Zs|2+2​ρ​(Zs1+σs​πs)​Zs)​ds\displaystyle+\frac{1}{2}\int\_{t}^{t+\varepsilon}\xi\_{s}^{t,\varepsilon}U^{{}^{\prime\prime\prime}}(R\_{s}+Y\_{s})\left(|Z\_{s}^{1}+\sigma\_{s}\pi\_{s}|^{2}+|Z\_{s}|^{2}+2\rho(Z\_{s}^{1}+\sigma\_{s}\pi\_{s})Z\_{s}\right)\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫tt+εU′′(Rs+Ys)(Zs1+σsπs+ρZs)⋅σsηds]\displaystyle\left.+\int\_{t}^{t+\varepsilon}U^{{}^{\prime\prime}}(R\_{s}+Y\_{s})(Z\_{s}^{1}+\sigma\_{s}\pi\_{s}+\rho Z\_{s})\cdot\sigma\_{s}\eta\mathrm{d}s\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼t​[∫tt+εe−ζ​(Rs+Ys)​(a​(s,πst,ε)−a​(s,πs)−ζ​(Zs1+σs​πs+ρ​Zs)⋅σs​η)​ds]\displaystyle\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}e^{-\zeta(R\_{s}+Y\_{s})}\left(a(s,\pi^{t,\varepsilon}\_{s})-a(s,\pi\_{s})-\zeta(Z\_{s}^{1}+\sigma\_{s}\pi\_{s}+\rho Z\_{s})\cdot\sigma\_{s}\eta\right)\mathrm{d}s\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +𝔼t​[∫tt+εe−ζ​(Rs+Ys)​[(σs​η−ζ​ξst,ε​(Zs1+σs​πs))​d​Bs−ζ​ξst,ε​Zs​d​B¯s]].\displaystyle+\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}e^{-\zeta(R\_{s}+Y\_{s})}\left[(\sigma\_{s}\eta-\zeta\xi\_{s}^{t,\varepsilon}(Z\_{s}^{1}+\sigma\_{s}\pi\_{s}))\mathrm{d}B\_{s}-\zeta\xi\_{s}^{t,\varepsilon}Z\_{s}\mathrm{d}\bar{B}\_{s}\right]\right]. |  | (3.5) |

Under Assumption [2.1](https://arxiv.org/html/2511.05861v1#S2.Thmtheorem1 "Assumption 2.1. ‣ 2 Problem Formulation ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets"), we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼t​[(∫tt+ε(αs​σs​η)2​ds)12]≤(𝔼t​[(sups∈[t,t+ε]αs)p])1p​(𝔼t​[(sups∈[t,t+ε]σs​η)q])1q<∞,\mathbb{E}\_{t}\left[\left(\int\_{t}^{t+\varepsilon}(\alpha\_{s}\sigma\_{s}\eta)^{2}\mathrm{d}s\right)^{\frac{1}{2}}\right]\leq\left(\mathbb{E}\_{t}\left[\left(\sup\limits\_{s\in[t,t+\varepsilon]}\alpha\_{s}\right)^{p}\right]\right)^{\frac{1}{p}}\left(\mathbb{E}\_{t}\left[\left(\sup\limits\_{s\in[t,t+\varepsilon]}\sigma\_{s}\eta\right)^{q}\right]\right)^{\frac{1}{q}}<\infty, |  |

|  |  |  |
| --- | --- | --- |
|  | 𝔼t​[(∫tt+ε(βs​ξst,ε)2​ds)12]≤(𝔼t​[(∫tt+ε(βs)2​ds)p2])1p​(𝔼t​[(sups∈[t,t+ε]ξst,ε)q])1q<∞,\mathbb{E}\_{t}\left[\left(\int\_{t}^{t+\varepsilon}(\beta\_{s}\xi\_{s}^{t,\varepsilon})^{2}\mathrm{d}s\right)^{\frac{1}{2}}\right]\leq\left(\mathbb{E}\_{t}\left[\left(\int\_{t}^{t+\varepsilon}(\beta\_{s})^{2}\mathrm{d}s\right)^{\frac{p}{2}}\right]\right)^{\frac{1}{p}}\left(\mathbb{E}\_{t}\left[\left(\sup\limits\_{s\in[t,t+\varepsilon]}\xi\_{s}^{t,\varepsilon}\right)^{q}\right]\right)^{\frac{1}{q}}<\infty, |  |

|  |  |  |
| --- | --- | --- |
|  | 𝔼t​[(∫tt+ε(βs1​ξst,ε)2​ds)12]≤(𝔼t​[(∫tt+ε(βs1)2​ds)p2])1p​(𝔼t​[(sups∈[t,t+ε]ξst,ε)q])1q<∞.\mathbb{E}\_{t}\left[\left(\int\_{t}^{t+\varepsilon}(\beta\_{s}^{1}\xi\_{s}^{t,\varepsilon})^{2}\mathrm{d}s\right)^{\frac{1}{2}}\right]\leq\left(\mathbb{E}\_{t}\left[\left(\int\_{t}^{t+\varepsilon}(\beta\_{s}^{1})^{2}\mathrm{d}s\right)^{\frac{p}{2}}\right]\right)^{\frac{1}{p}}\left(\mathbb{E}\_{t}\left[\left(\sup\limits\_{s\in[t,t+\varepsilon]}\xi\_{s}^{t,\varepsilon}\right)^{q}\right]\right)^{\frac{1}{q}}<\infty. |  |

The Burkholder-Davis-Gundy inequality yields that

|  |  |  |
| --- | --- | --- |
|  | 𝔼t​[∫tt+εe−ζ​(Rs+Ys)​[(σ​η−ζ​ξst,ε​(Zs1+σ​π))​d​Bs−ζ​ξst,ε​Zs​d​B¯s]]=0.\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}e^{-\zeta(R\_{s}+Y\_{s})}\left[(\sigma\eta-\zeta\xi\_{s}^{t,\varepsilon}(Z\_{s}^{1}+\sigma\pi))\mathrm{d}B\_{s}-\zeta\xi\_{s}^{t,\varepsilon}Z\_{s}\mathrm{d}\bar{B}\_{s}\right]\right]=0. |  |

For the second part, let α~t=𝔼t​[RT]\tilde{\alpha}\_{t}=\mathbb{E}\_{t}[R\_{T}] and Yt~=α~t−Rt\tilde{Y\_{t}}=\tilde{\alpha}\_{t}-R\_{t}. Then, α~\tilde{\alpha} and Y~\tilde{Y} satisfy that

|  |  |  |
| --- | --- | --- |
|  | d​α~=β~1​d​Bs+β~​d​B¯s,\displaystyle\mathrm{d}\tilde{\alpha}=\tilde{\beta}^{1}\mathrm{d}B\_{s}+\tilde{\beta}\mathrm{d}\bar{B}\_{s}, |  |
|  |  |  |
| --- | --- | --- |
|  | d​Y~s=−a​(s,πs)​d​s+Z~s1​d​Bs+Z~s​d​B¯s,\displaystyle\mathrm{d}\tilde{Y}\_{s}=-a(s,\pi\_{s})\mathrm{d}s+\tilde{Z}^{1}\_{s}\mathrm{d}B\_{s}+\tilde{Z}\_{s}\mathrm{d}\bar{B}\_{s}, |  |

and α~∈L𝔽2​(Ω;C​([0,T];ℝ)),β~1=Z~1+σ​π,β~=Z~∈L𝔽2​(Ω;L2​(0,T;ℝ))\tilde{\alpha}\in L^{2}\_{\mathbb{F}}(\Omega;C([0,T];\mathbb{R})),\tilde{\beta}^{1}=\tilde{Z}^{1}+\sigma\pi,\tilde{\beta}=\tilde{Z}\in L^{2}\_{\mathbb{F}}\left(\Omega;L^{2}(0,T;\mathbb{R})\right). From Lemma [2.4](https://arxiv.org/html/2511.05861v1#S2.Thmtheorem4 "Lemma 2.4. ‣ 2 Problem Formulation ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets"), it follows that Rπ∈L𝔽2​(Ω;C​([0,T];ℝ))R^{\pi}\in L^{2}\_{\mathbb{F}}(\Omega;C([0,T];\mathbb{R})) and hence Y~∈L𝔽2​(Ω;C​([0,T];ℝ))\tilde{Y}\in L^{2}\_{\mathbb{F}}(\Omega;C([0,T];\mathbb{R})). We thus get that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | Vart​[RT]−Vart​[RTt,ε]\displaystyle\textup{Var}\_{t}[R\_{T}]-\textup{Var}\_{t}[R\_{T}^{t,\varepsilon}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | Vart​[𝔼t+ε​[RT]]+𝔼t​[Vart+ε​[RT]]−Vart​[𝔼t+ε​[RTt,ε]]−𝔼t​[Vart+ε​[RTt,ε]]\displaystyle\textup{Var}\_{t}\left[\mathbb{E}\_{t+\varepsilon}[R\_{T}]\right]+\mathbb{E}\_{t}\left[\textup{Var}\_{t+\varepsilon}[R\_{T}]\right]-\textup{Var}\_{t}\left[\mathbb{E}\_{t+\varepsilon}[R\_{T}^{t,\varepsilon}]\right]-\mathbb{E}\_{t}\left[\textup{Var}\_{t+\varepsilon}[R\_{T}^{t,\varepsilon}]\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | Vart​[Rt+ε+Y~t+ε]−Vart​[Rt+εt,ε+Y~t+ε]\displaystyle\textup{Var}\_{t}[R\_{t+\varepsilon}+\tilde{Y}\_{t+\varepsilon}]-\textup{Var}\_{t}[R\_{t+\varepsilon}^{t,\varepsilon}+\tilde{Y}\_{t+\varepsilon}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | Vart​[∫tt+ε(σ​πs+Z~s1)​dBs+Z~s​d​B¯s]−Vart​[∫tt+ε(σ​πst,ε+Z~s1)​dBs+Z~s​d​B¯s]\displaystyle\textup{Var}\_{t}\left[\int\_{t}^{t+\varepsilon}(\sigma\pi\_{s}+\tilde{Z}^{1}\_{s})\mathrm{d}B\_{s}+\tilde{Z}\_{s}\mathrm{d}\bar{B}\_{s}\right]-\textup{Var}\_{t}\left[\int\_{t}^{t+\varepsilon}(\sigma\pi\_{s}^{t,\varepsilon}+\tilde{Z}\_{s}^{1})\mathrm{d}B\_{s}+\tilde{Z}\_{s}\mathrm{d}\bar{B}\_{s}\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼t​[∫tt+ε((σ​πs+Z~s1+ρ​Z~s)2−(σ​πst,ε+Z~s1+ρ​Z~s)2)​ds],\displaystyle\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}((\sigma\pi\_{s}+\tilde{Z}^{1}\_{s}+\rho\tilde{Z}\_{s})^{2}-(\sigma\pi\_{s}^{t,\varepsilon}+\tilde{Z}^{1}\_{s}+\rho\tilde{Z}\_{s})^{2})\mathrm{d}s\right], |  | (3.6) |

where we have used the fact that RT−Rt+ε=RTt,ε−Rt+εt,εR\_{T}-R\_{t+\varepsilon}=R\_{T}^{t,\varepsilon}-R\_{t+\varepsilon}^{t,\varepsilon} in the second and third equalities . The conclusion then follows by combining ([3](https://arxiv.org/html/2511.05861v1#S3.Ex11 "3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) and ([3](https://arxiv.org/html/2511.05861v1#S3.Ex23 "3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")).
∎

###### Lemma 3.5.

Let π∈Π0\pi\in\Pi\_{0} fixed. For any t∈[0,T)t\in[0,T) and η∈Lℱt∞​(Ω,ℝ)\eta\in L\_{\mathcal{F}\_{t}}^{\infty}(\Omega,\mathbb{R}) fixed and for ε\varepsilon sufficiently small, it holds that a.s.

|  |  |  |
| --- | --- | --- |
|  | lim supε→01ε​𝔼t​[∫01e−ζ​(RT+λ​ξTt,ε−Rt)​(1−λ)​𝑑λ​|ξTt,ε|2]≤C​(‖η‖∞)​|η|2,a.s.\limsup\limits\_{\varepsilon\rightarrow 0}\frac{1}{\varepsilon}\mathbb{E}\_{t}\left[\int\_{0}^{1}e^{-\zeta(R\_{T}+\lambda\xi\_{T}^{t,\varepsilon}-R\_{t})}(1-\lambda)d\lambda|\xi\_{T}^{t,\varepsilon}|^{2}\right]\leq C(\|\eta\|\_{\infty})|\eta|^{2},\quad a.s. |  |

with CC denoting a constant independent of ε\varepsilon and increasing with respect to ‖η‖∞\|\eta\|\_{\infty}.

###### Proof.

Hölder’s inequality and Lemma [2.7](https://arxiv.org/html/2511.05861v1#S2.Thmtheorem7 "Lemma 2.7. ‣ 2 Problem Formulation ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") imply that 𝔼t​[e−ζ​RT​|ξTt,ε|2]<∞\mathbb{E}\_{t}\left[e^{-\zeta R\_{T}}|\xi\_{T}^{t,\varepsilon}|^{2}\right]<\infty and 𝔼t​[e−ζ​(RT+ξTt,ε)​|ξTt,ε|2]<∞\mathbb{E}\_{t}\left[e^{-\zeta(R\_{T}+\xi\_{T}^{t,\varepsilon})}|\xi\_{T}^{t,\varepsilon}|^{2}\right]<\infty a.s.. Noting that e−(RT+λ​ξTt,ε)​|ξTt,ε|2e^{-(R\_{T}+\lambda\xi\_{T}^{t,\varepsilon})}|\xi\_{T}^{t,\varepsilon}|^{2} is nonnegative and convex almost sure with respect to λ\lambda, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 1ε​𝔼t​[∫01(e−ζ​(RT+λ​ξTt,ε−Rt)​(1−λ))​𝑑λ⋅|ξTt,ε|2]=1ε​∫01(𝔼t​[e−ζ​(RT+λ​ξTt,ε−Rt)​|ξTt,ε|2]​(1−λ))​dλ\displaystyle\frac{1}{\varepsilon}\mathbb{E}\_{t}\left[\int\_{0}^{1}\left(e^{-\zeta(R\_{T}+\lambda\xi\_{T}^{t,\varepsilon}-R\_{t})}(1-\lambda)\right)d\lambda\cdot|\xi\_{T}^{t,\varepsilon}|^{2}\right]=\frac{1}{\varepsilon}\int\_{0}^{1}\left(\mathbb{E}\_{t}\left[e^{-\zeta(R\_{T}+\lambda\xi\_{T}^{t,\varepsilon}-R\_{t})}|\xi\_{T}^{t,\varepsilon}|^{2}\right](1-\lambda)\right)\mathrm{d}\lambda |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 1ε​eζ​Rt​(𝔼t​[e−ζ​RT​|ξTt,ε|2]​∫01(1−λ)2​dλ+𝔼t​[e−ζ​(RT+ξTt,ε)​|ξTt,ε|2]​∫01λ​(1−λ)​dλ).\displaystyle\frac{1}{\varepsilon}e^{\zeta R\_{t}}\left(\mathbb{E}\_{t}\left[e^{-\zeta R\_{T}}|\xi\_{T}^{t,\varepsilon}|^{2}\right]\int\_{0}^{1}(1-\lambda)^{2}\mathrm{d}\lambda+\mathbb{E}\_{t}\left[e^{-\zeta(R\_{T}+\xi\_{T}^{t,\varepsilon})}|\xi\_{T}^{t,\varepsilon}|^{2}\right]\int\_{0}^{1}\lambda(1-\lambda)\mathrm{d}\lambda\right). |  |

Therefore, we only need to show that 1ε​𝔼t​[e−(RT+λ​ξTt,ε−Rt)​|ξTt,ε|2]≤C​|η|2\frac{1}{\varepsilon}\mathbb{E}\_{t}\left[e^{-(R\_{T}+\lambda\xi\_{T}^{t,\varepsilon}-R\_{t})}|\xi\_{T}^{t,\varepsilon}|^{2}\right]\leq C|\eta|^{2} a.s. for λ=0,1\lambda=0,1, and for any t∈[0,T)t\in[0,T) and η∈Lℱt∞​(Ω,ℝ)\eta\in L\_{\mathcal{F}\_{t}}^{\infty}(\Omega,\mathbb{R}). By Lemma [2.7](https://arxiv.org/html/2511.05861v1#S2.Thmtheorem7 "Lemma 2.7. ‣ 2 Problem Formulation ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") and the Hölder’s inequality, there exists a constant CC only depending on q,‖r‖∞,‖μ‖∞,‖σ‖∞,T,k,‖π‖BMOq,\|r\|\_{\infty},\|\mu\|\_{\infty},\|\sigma\|\_{\infty},T,k,\|\pi\|\_{\textup{BMO}} such that,
for ε\varepsilon sufficiently small,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1ε​𝔼t​[e−ζ​(RT+λ​ξTt,ε−Rt)​|ξTt,ε|2]\displaystyle\frac{1}{\varepsilon}\mathbb{E}\_{t}\left[e^{-\zeta(R\_{T}+\lambda\xi\_{T}^{t,\varepsilon}-R\_{t})}|\xi\_{T}^{t,\varepsilon}|^{2}\right] | ≤1ε(𝔼t[e−p​ζ​(RT−Rt)|])1p(𝔼t[|ξTt,ε|2​q])1q(𝔼t[e−r​ζ​λ​ξTt,ε])1r\displaystyle\leq\frac{1}{\varepsilon}\left(\mathbb{E}\_{t}\left[e^{-p\zeta(R\_{T}-R\_{t})}|\right]\right)^{\frac{1}{p}}\left(\mathbb{E}\_{t}\left[|\xi\_{T}^{t,\varepsilon}|^{2q}\right]\right)^{\frac{1}{q}}\left(\mathbb{E}\_{t}\left[e^{-r\zeta\lambda\xi\_{T}^{t,\varepsilon}}\right]\right)^{\frac{1}{r}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C(𝔼t[e−p​ζ​(RT−Rt)|])1p(𝔼t[e−r​ζ​λ​ξTt,ε])1r|η|2\displaystyle\leq C\left(\mathbb{E}\_{t}\left[e^{-p\zeta(R\_{T}-R\_{t})}|\right]\right)^{\frac{1}{p}}\left(\mathbb{E}\_{t}\left[e^{-r\zeta\lambda\xi\_{T}^{t,\varepsilon}}\right]\right)^{\frac{1}{r}}|\eta|^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C​(‖η‖∞)​|η|2,λ=0,1.\displaystyle\leq C(\|\eta\|\_{\infty})|\eta|^{2},\quad\lambda=0,1. |  |

Here, we choose q,rq,r such that 1p+1q+1r=1\frac{1}{p}+\frac{1}{q}+\frac{1}{r}=1.
Then, it holds that

|  |  |  |
| --- | --- | --- |
|  | lim supε→01ε​𝔼t​[∫01e−ζ​(RT+λ​ξTt,ε−Rt)​(1−λ)​𝑑λ​|ξTt,ε|2]≤C​(‖η‖∞)​|η|2a.s..\limsup\limits\_{\varepsilon\rightarrow 0}\frac{1}{\varepsilon}\mathbb{E}\_{t}\left[\int\_{0}^{1}e^{-\zeta(R\_{T}+\lambda\xi\_{T}^{t,\varepsilon}-R\_{t})}(1-\lambda)d\lambda|\xi\_{T}^{t,\varepsilon}|^{2}\right]\leq C(\|\eta\|\_{\infty})|\eta|^{2}\quad a.s.. |  |

∎

###### Lemma 3.6.

For any admissible strategy π∈Π0\pi\in\Pi\_{0}, consider the pair (Y,Y~)(Y,\tilde{Y}) and (Z,Z~)(Z,\tilde{Z}) in Lemma [3.4](https://arxiv.org/html/2511.05861v1#S3.Thmtheorem4 "Lemma 3.4. ‣ 3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets"). We deduce the existence of a measurable set E1⊂[0,T)E\_{1}\subset[0,T) with Leb⁡([0,T]∖E1)=0\operatorname{Leb}([0,T]\setminus E\_{1})=0 such that,
for any t∈E1t\in E\_{1}, there exists a sequence {εn}n∈ℕ⊂(0,T−t)\{\varepsilon\_{n}\}\_{n\in\mathbb{N}}\subset(0,T-t) satisfying limn→∞εnt=0\lim\_{n\to\infty}\varepsilon\_{n}^{t}=0
and for any perturbation η∈Lℱt∞​(Ω;ℝ)\eta\in L\_{\mathcal{F}\_{t}}^{\infty}(\Omega;\mathbb{R}), it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | limn→∞1εnt​𝔼t​[∫tt+εnte−ζ​(Rs+Ys−Rt)​(a​(s,πst,εnt)−a​(s,πs)−ζ​(Zs1+σs​πs+ρ​Zs)⋅σs​η)​ds]\displaystyle\lim\limits\_{n\rightarrow\infty}\frac{1}{\varepsilon\_{n}^{t}}\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon\_{n}^{t}}e^{-\zeta(R\_{s}+Y\_{s}-R\_{t})}\left(a(s,\pi^{t,\varepsilon\_{n}^{t}}\_{s})-a(s,\pi\_{s})-\zeta(Z\_{s}^{1}+\sigma\_{s}\pi\_{s}+\rho Z\_{s})\cdot\sigma\_{s}\eta\right)\mathrm{d}s\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | e−ζ​Yt​((μt−rt)​η−12​σt2​η2−σt2​η​πt−ζ​(Zt1+σt​πt+ρ​Zt)⋅σt​η),a.s.\displaystyle e^{-\zeta Y\_{t}}\left((\mu\_{t}-r\_{t})\eta-\frac{1}{2}\sigma^{2}\_{t}\eta^{2}-\sigma^{2}\_{t}\eta\pi\_{t}-\zeta(Z\_{t}^{1}+\sigma\_{t}\pi\_{t}+\rho Z\_{t})\cdot\sigma\_{t}\eta\right),\quad a.s. |  | (3.7) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | limn→∞1εnt​𝔼t​[∫tt+εnt((σs​πs+Z~s1+ρ​Z~s)2−(σs​πst,ε+Z~s1+ρ​Z~s)2)​ds]\displaystyle\lim\limits\_{n\rightarrow\infty}\frac{1}{\varepsilon\_{n}^{t}}\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon\_{n}^{t}}\left((\sigma\_{s}\pi\_{s}+\tilde{Z}^{1}\_{s}+\rho\tilde{Z}\_{s})^{2}-(\sigma\_{s}\pi\_{s}^{t,\varepsilon}+\tilde{Z}^{1}\_{s}+\rho\tilde{Z}\_{s})^{2}\right)\mathrm{d}s\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | −2​σt​η​(σt​πt+Z~t1+ρ​Z~t−σt2​η2),a.s..\displaystyle-2\sigma\_{t}\eta(\sigma\_{t}\pi\_{t}+\tilde{Z}^{1}\_{t}+\rho\tilde{Z}\_{t}-\sigma\_{t}^{2}\eta^{2}),\quad a.s.. |  | (3.8) |

###### Proof.

Noting that a​(s,πst,εnt)−a​(s,πs)=(μs−rs)​η−12​σs2​η2−σt2​η​πsa(s,\pi^{t,\varepsilon\_{n}^{t}}\_{s})-a(s,\pi\_{s})=(\mu\_{s}-r\_{s})\eta-\frac{1}{2}\sigma^{2}\_{s}\eta^{2}-\sigma^{2}\_{t}\eta\pi\_{s} and (σs​πs+Z~s1+ρ​Z~s)2−(σs​πst,ε+Z~s1+ρ​Z~s)2=−2​σs​η​(σs​πs+Z~s1+ρ​Z~s−σs2​η2)(\sigma\_{s}\pi\_{s}+\tilde{Z}^{1}\_{s}+\rho\tilde{Z}\_{s})^{2}-(\sigma\_{s}\pi\_{s}^{t,\varepsilon}+\tilde{Z}^{1}\_{s}+\rho\tilde{Z}\_{s})^{2}=-2\sigma\_{s}\eta(\sigma\_{s}\pi\_{s}+\tilde{Z}^{1}\_{s}+\rho\tilde{Z}\_{s}-\sigma\_{s}^{2}\eta^{2}), we only need to prove that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | limn→∞1εnt​𝔼t​[∫tt+εntαs​((μs−rs)​η−12​σs2​η2−σt2​η​πs−ζ​(Zs1+σs​πs+ρ​Zs)⋅σs​η)​ds]\displaystyle\lim\limits\_{n\rightarrow\infty}\frac{1}{\varepsilon\_{n}^{t}}\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon\_{n}^{t}}\alpha\_{s}\left((\mu\_{s}-r\_{s})\eta-\frac{1}{2}\sigma^{2}\_{s}\eta^{2}-\sigma^{2}\_{t}\eta\pi\_{s}-\zeta(Z\_{s}^{1}+\sigma\_{s}\pi\_{s}+\rho Z\_{s})\cdot\sigma\_{s}\eta\right)\mathrm{d}s\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | αt​((μt−rt)​η−12​σt2​η2−σt2​η​πt−ζ​(Zt1+σt​πt+ρ​Zt)⋅σt​η),a.s.\displaystyle\alpha\_{t}\left((\mu\_{t}-r\_{t})\eta-\frac{1}{2}\sigma^{2}\_{t}\eta^{2}-\sigma^{2}\_{t}\eta\pi\_{t}-\zeta(Z\_{t}^{1}+\sigma\_{t}\pi\_{t}+\rho Z\_{t})\cdot\sigma\_{t}\eta\right),\quad a.s. |  |

and

|  |  |  |
| --- | --- | --- |
|  | limn→∞1εnt​𝔼t​[∫tt+εnt2​σs​(σs​πs+Z~s1+ρ​Z~s−σs2​η2)​ds]=2​σt​(σt​πt+Z~t1+ρ​Z~t−σt2​η2),a.s..\lim\limits\_{n\rightarrow\infty}\frac{1}{\varepsilon\_{n}^{t}}\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon\_{n}^{t}}2\sigma\_{s}(\sigma\_{s}\pi\_{s}+\tilde{Z}^{1}\_{s}+\rho\tilde{Z}\_{s}-\sigma\_{s}^{2}\eta^{2})\mathrm{d}s\right]=2\sigma\_{t}(\sigma\_{t}\pi\_{t}+\tilde{Z}^{1}\_{t}+\rho\tilde{Z}\_{t}-\sigma\_{t}^{2}\eta^{2}),\quad a.s.. |  |

In view of e−ζ​(Rs+Ys)=αs∈L𝔽p​(Ω;C​([0,T];ℝ))e^{-\zeta(R\_{s}+Y\_{s})}=\alpha\_{s}\in L^{p}\_{\mathbb{F}}(\Omega;C([0,T];\mathbb{R})) and the fact that μ−r\mu-r and σ\sigma are bounded, we have α​(μ−r),α​σ2∈Lp​(0,T;ℝ)\alpha(\mu-r),\alpha\sigma^{2}\in L^{p}(0,T;\mathbb{R}) with p>1p>1. It also holds that, for any 1<γ<p1<\gamma<p and 1γ=1p+1q′\frac{1}{\gamma}=\frac{1}{p}+\frac{1}{q^{\prime}},

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0T|αs​πs|γ​ds]≤(𝔼​[sups∈[0,T]|αs|p])γp​(𝔼​[(∫0T|πs|γ​ds)q′γ])γq′<∞,\mathbb{E}\left[\int\_{0}^{T}|\alpha\_{s}\pi\_{s}|^{\gamma}\mathrm{d}s\right]\leq\left(\mathbb{E}\left[\sup\limits\_{s\in[0,T]}|\alpha\_{s}|^{p}\right]\right)^{\frac{\gamma}{p}}\left(\mathbb{E}\left[\left(\int\_{0}^{T}|\pi\_{s}|^{\gamma}\mathrm{d}s\right)^{\frac{q^{\prime}}{\gamma}}\right]\right)^{\frac{\gamma}{q^{\prime}}}<\infty, |  |

which implies that α​σ2​π∈Lγ​(0,T;ℝ)\alpha\sigma^{2}\pi\in L^{\gamma}(0,T;\mathbb{R}). In addition, α​(Z1+σ​π)=β1,α​Z=β∈L𝔽p​(Ω;L2​(0,T;ℝ))⊂Lp∧2​(0,T;ℝ)\alpha(Z^{1}+\sigma\pi)=\beta^{1},\;\alpha Z=\beta\in L^{p}\_{\mathbb{F}}\left(\Omega;L^{2}(0,T;\mathbb{R})\right)\subset L^{p\wedge 2}(0,T;\mathbb{R}) and β~1=Z~1+σ​π,β~=Z~∈L𝔽2​(Ω;L2​(0,T;ℝ))⊂L2​(0,T;ℝ)\tilde{\beta}^{1}=\tilde{Z}^{1}+\sigma\pi,\tilde{\beta}=\tilde{Z}\in L^{2}\_{\mathbb{F}}\left(\Omega;L^{2}(0,T;\mathbb{R})\right)\subset L^{2}(0,T;\mathbb{R}).

Therefore, by Lemma 3.3 in Hamaguchi\_2021 , there exists a measurable set E1E\_{1} with Leb⁡([0,T]∖E1)=0\operatorname{Leb}([0,T]\setminus E\_{1})=0 such that for any t∈E1t\in E\_{1}, we can choose a subsequence by recursively extracting subsequences and applying the diagonal selection argument that

|  |  |  |
| --- | --- | --- |
|  | limn→∞𝔼t​[1εnt​∫tεntPs]=Pt.\lim\limits\_{n\rightarrow\infty}\mathbb{E}\_{t}\left[\frac{1}{\varepsilon\_{n}^{t}}\int\_{t}^{\varepsilon\_{n}^{t}}P\_{s}\right]=P\_{t}. |  |

Here PP can be chosen to be α​(μ−r),α​σ2,α​σ2​π,α​(Z1+σ​π+ρ​Z)\alpha(\mu-r),\alpha\sigma^{2},\alpha\sigma^{2}\pi,\alpha(Z^{1}+\sigma\pi+\rho Z) and σ​(σ​π+Z~1+ρ​Z~),σ3​η2\sigma(\sigma\pi+\tilde{Z}^{1}+\rho\tilde{Z}),\sigma^{3}\eta^{2}. Then we obtain ([3.6](https://arxiv.org/html/2511.05861v1#S3.Ex31 "Lemma 3.6. ‣ 3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) and ([3.6](https://arxiv.org/html/2511.05861v1#S3.Ex32 "Lemma 3.6. ‣ 3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) with E1E\_{1} and the corresponding εnt\varepsilon\_{n}^{t} for any t∈E1t\in E\_{1}, independent of η\eta.

∎

###### Remark 3.7.

Note that a​(s,πst,εnt)−a​(s,πs)a(s,\pi^{t,\varepsilon\_{n}^{t}}\_{s})-a(s,\pi\_{s}) depends on the perturbation strategy πt,εnt\pi^{t,\varepsilon\_{n}^{t}} only on [t,t+εnt][t,t+\varepsilon\_{n}^{t}] and will be affected by η\eta, we cannot directly apply Lemma 3.3 in Hamaguchi\_2021. However, because the effect of η\eta can be separated, we can apply Lemma 3.3 to each element in two expressions and then use the diagonal selection argument to complete the proof.

Now we are ready to give the proof of Theorem [3.1](https://arxiv.org/html/2511.05861v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets").

###### Proof of Theorem [3.1](https://arxiv.org/html/2511.05861v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets").

Assume that π^∈Π0\hat{\pi}\in\Pi\_{0} is an equilibrium strategy. Fix an arbitrary δ>0\delta>0 and take an arbitrary tt from the set E1E\_{1} in Lemma [3.6](https://arxiv.org/html/2511.05861v1#S3.Thmtheorem6 "Lemma 3.6. ‣ 3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") . Let {δm}m∈ℕ\{\delta\_{m}\}\_{m\in\mathbb{N}} be a sequence such that 0<δm≤δ,m∈ℕ,0<\delta\_{m}\leq\delta,\;m\in\mathbb{N}, and limm→∞δm=0\lim\_{m\rightarrow\infty}\delta\_{m}=0. For each m∈ℕm\in\mathbb{N}, define ηm\eta\_{m} by

|  |  |  |
| --- | --- | --- |
|  | ηm={δme−ζ​Yt​θ−e−ζ​Yt​σt​π^t−ζ​e−ζ​Yt​(σt​π^t+Zt1+ρ​Zt)−γ​(Z~t1+σt​π^t+ρ​Z~t)≥0,−δme−ζ​Yt​θ−e−ζ​Yt​σt​π^t−ζ​e−ζ​Yt​(σt​π^t+Zt1+ρ​Zt)−γ​(Z~t1+σt​π^t+ρ​Z~t)<0.\eta\_{m}=\begin{cases}\delta\_{m}&e^{-\zeta Y\_{t}}\theta-e^{-\zeta Y\_{t}}\sigma\_{t}\hat{\pi}\_{t}-\zeta e^{-\zeta Y\_{t}}(\sigma\_{t}\hat{\pi}\_{t}+Z\_{t}^{1}+\rho Z\_{t})-\gamma(\tilde{Z}^{1}\_{t}+\sigma\_{t}\hat{\pi}\_{t}+\rho\tilde{Z}\_{t})\geq 0,\\ -\delta\_{m}&e^{-\zeta Y\_{t}}\theta-e^{-\zeta Y\_{t}}\sigma\_{t}\hat{\pi}\_{t}-\zeta e^{-\zeta Y\_{t}}(\sigma\_{t}\hat{\pi}\_{t}+Z\_{t}^{1}+\rho Z\_{t})-\gamma(\tilde{Z}^{1}\_{t}+\sigma\_{t}\hat{\pi}\_{t}+\rho\tilde{Z}\_{t})<0.\end{cases} |  |

By the definition of the equilibrium, Lemma [3.6](https://arxiv.org/html/2511.05861v1#S3.Thmtheorem6 "Lemma 3.6. ‣ 3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets"), Lemma [3.4](https://arxiv.org/html/2511.05861v1#S3.Thmtheorem4 "Lemma 3.4. ‣ 3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") as well as Lemma [3.5](https://arxiv.org/html/2511.05861v1#S3.Thmtheorem5 "Lemma 3.5. ‣ 3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets"), we obtain that there exists a sequence {εnt}n∈ℕ⊂(0,T−t)\{\varepsilon\_{n}^{t}\}\_{n\in\mathbb{N}}\subset(0,T-t) satisfying limn→∞εnt=0\lim\_{n\to\infty}\varepsilon\_{n}^{t}=0
such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≥\displaystyle 0\geq | lim supn→∞1εnt​(J​(t,Rt^,π^t,εnt,ηm)−J​(t,Rt^,π^))\displaystyle\limsup\limits\_{n\rightarrow\infty}\frac{1}{\varepsilon\_{n}^{t}}\left(J(t,\hat{R\_{t}},\hat{\pi}^{t,\varepsilon\_{n}^{t},\eta\_{m}})-J(t,\hat{R\_{t}},\hat{\pi})\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | e−ζ​Yt​((μt−rt)​ηm−12​σt2​ηm2−σt2​π^t​ηm−ζ​(Zt1+σt​π^t+ρ​Zt)⋅σt​ηm)\displaystyle e^{-\zeta Y\_{t}}\left((\mu\_{t}-r\_{t})\eta\_{m}-\frac{1}{2}\sigma\_{t}^{2}\eta\_{m}^{2}-\sigma\_{t}^{2}\hat{\pi}\_{t}\eta\_{m}-\zeta(Z\_{t}^{1}+\sigma\_{t}\hat{\pi}\_{t}+\rho Z\_{t})\cdot\sigma\_{t}\eta\_{m}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −γ2​σt​ηm​(2​σt​π^+2​Z~t1+2​ρ​Z~t+σt​ηm)−C​(|δ|)​(|ηm|2),a.s..\displaystyle\quad\quad-\frac{\gamma}{2}\sigma\_{t}\eta\_{m}\left(2\sigma\_{t}\hat{\pi}+2\tilde{Z}^{1}\_{t}+2\rho\tilde{Z}\_{t}+\sigma\_{t}\eta\_{m}\right)-C(|\delta|)(|\eta\_{m}|^{2}),\quad a.s.. |  |

Dividing both sides of the above inequality by δm\delta\_{m}, sending m→∞m\rightarrow\infty and noting that the coefficient of σt​ηm\sigma\_{t}\eta\_{m} tends to zero, we deduce that

|  |  |  |
| --- | --- | --- |
|  | e−ζ​Yt​θ−e−ζ​Yt​σt​π^t−ζ​e−ζ​Yt​(σt​π^t+Zt1+ρ​Zt)−γ​(Z~t1+σt​π^t+ρ​Z~t)=0.e^{-\zeta Y\_{t}}\theta-e^{-\zeta Y\_{t}}\sigma\_{t}\hat{\pi}\_{t}-\zeta e^{-\zeta Y\_{t}}(\sigma\_{t}\hat{\pi}\_{t}+Z\_{t}^{1}+\rho Z\_{t})-\gamma(\tilde{Z}^{1}\_{t}+\sigma\_{t}\hat{\pi}\_{t}+\rho\tilde{Z}\_{t})=0. |  |

Consequently, the desired result holds that

|  |  |  |
| --- | --- | --- |
|  | σ​π^=e−ζ​Y​θ−ζ​e−ζ​Y​(Z1+ρ​Z)−γ​(Z~1+ρ​Z~)(ζ+1)​e−ζ​Y+γ.\sigma\hat{\pi}=\frac{e^{-\zeta Y}\theta-\zeta e^{-\zeta Y}(Z^{1}+\rho Z)-\gamma(\tilde{Z}^{1}+\rho\tilde{Z})}{(\zeta+1)e^{-\zeta Y}+\gamma}. |  |

∎

## 4 Study of BSDE System in the Incomplete Factor Model

In this section, we focus on the factor model and the asssociated BSDEs ([3.1](https://arxiv.org/html/2511.05861v1#S3.E1 "In item 2 ‣ Theorem 3.1. ‣ 3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")). The factor model provides an incomplete market setting with stochastic parameters in which the risk-free rate, the stock return rate, and the volatility rate can be expressed by a deterministic function of time tt and the factor XtX\_{t}. It is assumed that the stochastic factor XX is governed by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=m​(t,Xt)​d​t+ν​(t,Xt)​d​Bt¯,X0=x0.\displaystyle\mathrm{d}X\_{t}=m(t,X\_{t})\mathrm{d}t+\nu(t,X\_{t})\mathrm{d}\bar{B\_{t}},\quad X\_{0}=x\_{0}. |  | (4.1) |

It is assumed that rt=r​(t,Xt),μt=μ​(t,Xt),σt=σ​(t,Xt)r\_{t}=r(t,X\_{t}),\mu\_{t}=\mu(t,X\_{t}),\sigma\_{t}=\sigma(t,X\_{t}) for some functions r,μ,σ:[0,T]×ℝ→ℝr,\mu,\sigma:[0,T]\times\mathbb{R}\to\mathbb{R} respectively. Moreover, we impose the following assumptions:

###### Assumption 4.1.

μ​(t,x),r​(t,x),σ​(t,x)>0\mu(t,x),r(t,x),\sigma(t,x)>0 and θ​(t,x)=σ−1​(μ−r)​(t,x)\theta(t,x)=\sigma^{-1}(\mu-r)(t,x) are bounded measurable (w.r.t. ℬ​([0,T]×ℝ)\mathcal{B}([0,T]\times\mathbb{R})) deterministic functions with respect to (t,x)(t,x). Here, θ\theta represents the market price of risk, which is assumed to be positive and bounded.

###### Assumption 4.2.

The coefficients of the factor model satisfy that

1. The drift vector mm is uniformly bounded.

2. There exists a constant λ>0\lambda>0 such that λ​|z|2≥|z​ν​(t,x)|2≥1λ​|z|2\lambda|z|^{2}\geq|z\nu(t,x)|^{2}\geq\frac{1}{\lambda}|z|^{2} for any (t,x,z)∈[0,T]×ℝ×ℝ(t,x,z)\in[0,T]\times\mathbb{R}\times\mathbb{R}.

3. There exists a constant LL such that

|  |  |  |
| --- | --- | --- |
|  | |m​(t,x)−m​(t,x′)|+|ν​(t,x)−ν​(t,x′)|≤L​|x−x′|.|m(t,x)-m(t,x^{\prime})|+|\nu(t,x)-\nu(t,x^{\prime})|\leq L|x-x^{\prime}|. |  |

Under Assumption [4.2](https://arxiv.org/html/2511.05861v1#S4.Thmtheorem2 "Assumption 4.2. ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets"), SDE ([4.1](https://arxiv.org/html/2511.05861v1#S4.E1 "In 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) admits a unique strong solution.
It is noted that the log-return process RR does not appear in the BSDE system ([3.1](https://arxiv.org/html/2511.05861v1#S3.E1 "In item 2 ‣ Theorem 3.1. ‣ 3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")), which motivates us to consider the solution adapted to the filtration 𝔽B¯\mathbb{F}\_{\bar{B}}. We can therefore conjecture that Z1=Z~1=0Z^{1}=\tilde{Z}^{1}=0 and aim to find the solution to the following Markovian BSDE system.

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​Xs=m​(s,Xs)​d​t+ν​(s,Xs)​d​B¯s,d​Ys=(ζ2​|ρ​Zs+u^s|2+ζ​(1−ρ2)2​|Zs|2−a​(s,π^s))​d​s+Zs​d​B¯s,d​Y~s=−a​(s,π^s)​d​s+Z~s​d​B¯s,YT=0,Y~T=0,u^=e−ζ​Y​θ−ζ​e−ζ​Y​ρ​Z−γ​ρ​Z~(ζ+1)​e−ζ​Y+γ,π^=σ−1​u^,a​(⋅,π):=r+(μ−r)​π−12​|σ​π|2.\left\{\begin{aligned} &\mathrm{d}X\_{s}=m(s,X\_{s})\mathrm{d}t+\nu(s,X\_{s})\mathrm{d}\bar{B}\_{s},\\ &\mathrm{d}Y\_{s}=\left(\frac{\zeta}{2}|\rho Z\_{s}+\hat{u}\_{s}|^{2}+\frac{\zeta(1-\rho^{2})}{2}|Z\_{s}|^{2}-a(s,\hat{\pi}\_{s})\right)\mathrm{d}s+Z\_{s}\mathrm{d}\bar{B}\_{s},\\ &\mathrm{d}\tilde{Y}\_{s}=-a(s,\hat{\pi}\_{s})\mathrm{d}s+\tilde{Z}\_{s}\mathrm{d}\bar{B}\_{s},\\ &Y\_{T}=0,\quad\tilde{Y}\_{T}=0,\\ &\hat{u}=\frac{e^{-\zeta Y}\theta-\zeta e^{-\zeta Y}\rho Z-\gamma\rho\tilde{Z}}{(\zeta+1)e^{-\zeta Y}+\gamma},\hat{\pi}=\sigma^{-1}\hat{u},a(\cdot,\pi):=r+(\mu-r)\pi-\frac{1}{2}|\sigma\pi|^{2}.\end{aligned}\right. |  | (4.2) |

### 4.1 Existence of time-consistent equilibrium when ρ=0\rho=0

In this subsection, we consider the case ρ=0\rho=0. Then it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | π^t=σt−1​u^t=σt−1​e−ζ​Yt​θ​(t,Xt)(ζ+1)​e−ζ​Yt+γ,\displaystyle\hat{\pi}\_{t}=\sigma\_{t}^{-1}\hat{u}\_{t}=\sigma\_{t}^{-1}\frac{e^{-\zeta Y\_{t}}\theta(t,X\_{t})}{(\zeta+1)e^{-\zeta Y\_{t}}+\gamma}, |  | (4.3) |

and the BSDE system ([3.1](https://arxiv.org/html/2511.05861v1#S3.E1 "In item 2 ‣ Theorem 3.1. ‣ 3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) can be decoupled as

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​Xs=m​(s,Xs)​d​t+ν​(s,Xs)​d​B¯s,d​Ys=(ζ+12​u^s2+ζ2​|Zs|2−r​(s,Xs)−θ​(s,Xs)​u^s)​d​s+Zs​d​B¯s,X0=x,YT=0.\left\{\begin{aligned} &\mathrm{d}X\_{s}=m(s,X\_{s})\mathrm{d}t+\nu(s,X\_{s})\mathrm{d}\bar{B}\_{s},\\ &\mathrm{d}Y\_{s}=\left(\frac{\zeta+1}{2}\hat{u}\_{s}^{2}+\frac{\zeta}{2}|Z\_{s}|^{2}-r(s,X\_{s})-\theta(s,X\_{s})\hat{u}\_{s}\right)\mathrm{d}s+Z\_{s}\mathrm{d}\bar{B}\_{s},\\ &X\_{0}=x,\quad Y\_{T}=0.\end{aligned}\right. |  | (4.4) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​Y~s=−r​(s,Xs)−θ​(s,Xs)​u^s+12​|u^t|2​d​s+Z~s​d​B¯s,Y~T=0.\left\{\begin{aligned} &\mathrm{d}\tilde{Y}\_{s}=-r(s,X\_{s})-\theta(s,X\_{s})\hat{u}\_{s}+\frac{1}{2}|\hat{u}\_{t}|^{2}\mathrm{d}s+\tilde{Z}\_{s}\mathrm{d}\bar{B}\_{s},\\ &\tilde{Y}\_{T}=0.\end{aligned}\right. |  | (4.5) |

It is straightforward to see that one can first solve equation ([4.4](https://arxiv.org/html/2511.05861v1#S4.E4 "In 4.1 Existence of time-consistent equilibrium when 𝜌=0 ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) and then substitute this solution into equation ([4.5](https://arxiv.org/html/2511.05861v1#S4.E5 "In 4.1 Existence of time-consistent equilibrium when 𝜌=0 ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) to obtain the solution for the entire system.
Regarding the existence of the solution to BSDE ([4.4](https://arxiv.org/html/2511.05861v1#S4.E4 "In 4.1 Existence of time-consistent equilibrium when 𝜌=0 ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")), we verify conditions (2A3), (3A2), (2A1), and (4A2) and apply Theorem 4.3 in FAN20161511, which leads to the following existence and uniqueness result.

###### Proposition 4.3.

If Assumptions [4.1](https://arxiv.org/html/2511.05861v1#S4.Thmtheorem1 "Assumption 4.1. ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") and [4.2](https://arxiv.org/html/2511.05861v1#S4.Thmtheorem2 "Assumption 4.2. ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") hold, the BSDE ([4.4](https://arxiv.org/html/2511.05861v1#S4.E4 "In 4.1 Existence of time-consistent equilibrium when 𝜌=0 ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) has a unique solution (Y,Z)∈𝒮∞×L𝔽2​(0,T;ℝ)(Y,Z)\in\mathcal{S}^{\infty}\times L^{2}\_{\mathbb{F}}(0,T;\mathbb{R}).

By Proposition [4.3](https://arxiv.org/html/2511.05861v1#S4.Thmtheorem3 "Proposition 4.3. ‣ 4.1 Existence of time-consistent equilibrium when 𝜌=0 ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets"), the candidate equilibrium strategy defined in ([4.3](https://arxiv.org/html/2511.05861v1#S4.E3 "In 4.1 Existence of time-consistent equilibrium when 𝜌=0 ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) satisfies
π^∈𝒮∞\hat{\pi}\in\mathcal{S}^{\infty}. Therefore, BSDE ([4.5](https://arxiv.org/html/2511.05861v1#S4.E5 "In 4.1 Existence of time-consistent equilibrium when 𝜌=0 ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) admits a unique solution (Y~,Z~)∈𝒮∞×L𝔽2​(0,T;ℝ)(\tilde{Y},\tilde{Z})\in\mathcal{S}^{\infty}\times L^{2}\_{\mathbb{F}}(0,T;\mathbb{R}) and Y~\tilde{Y} is given by

|  |  |  |
| --- | --- | --- |
|  | Y~t=𝔼t​[∫tT(r​(s,Xs)+θ​(s,Xs)​u^s−12​|u^s|2)​ds].\tilde{Y}\_{t}=\mathbb{E}\_{t}\left[\int\_{t}^{T}\left(r(s,X\_{s})+\theta(s,X\_{s})\hat{u}\_{s}-\frac{1}{2}|\hat{u}\_{s}|^{2}\right)\mathrm{d}s\right]. |  |

In the following, we establish that π^\hat{\pi} is an equilibrium strategy by means of BSDEs ([4.5](https://arxiv.org/html/2511.05861v1#S4.E5 "In 4.1 Existence of time-consistent equilibrium when 𝜌=0 ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) and ([4.3](https://arxiv.org/html/2511.05861v1#S4.Thmtheorem3 "Proposition 4.3. ‣ 4.1 Existence of time-consistent equilibrium when 𝜌=0 ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")), along with Lemma [3.4](https://arxiv.org/html/2511.05861v1#S3.Thmtheorem4 "Lemma 3.4. ‣ 3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets").
This result is stated in the theorem below.

###### Theorem 4.4.

When ρ=0\rho=0, suppose that Assumptions [4.1](https://arxiv.org/html/2511.05861v1#S4.Thmtheorem1 "Assumption 4.1. ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") and [4.2](https://arxiv.org/html/2511.05861v1#S4.Thmtheorem2 "Assumption 4.2. ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") hold, and let YY denote the bounded solution to BSDE ([4.4](https://arxiv.org/html/2511.05861v1#S4.E4 "In 4.1 Existence of time-consistent equilibrium when 𝜌=0 ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")).
Then the strategy defined in ([4.3](https://arxiv.org/html/2511.05861v1#S4.E3 "In 4.1 Existence of time-consistent equilibrium when 𝜌=0 ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) is an equilibrium strategy.

###### Proof.

For notational simplicity, let R^=Rπ^\hat{R}=R^{\hat{\pi}} denote the log-return process associated with π^\hat{\pi}. Moreover, we use πt,ε\pi^{t,\varepsilon} and ξt,ε\xi^{t,\varepsilon} to represent the perturbation strategy π^t,ε,η\hat{\pi}^{t,\varepsilon,\eta} and the corresponding difference process for any fixed t∈[0,T)t\in[0,T), η∈Lℱt∞​(Ω,ℝd)\eta\in L\_{\mathcal{F}\_{t}}^{\infty}(\Omega,\mathbb{R}^{d}) and ε∈(0,T−t)\varepsilon\in(0,T-t).

We first verify that π^\hat{\pi} is an admissible strategy. Since π^\hat{\pi} is bounded, it follows that π^∈HBMO\hat{\pi}\in H\_{\textup{BMO}}.
It is straightforward to show that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[exp⁡(c​|∫tT|​σs​π^s​|d​Bs|)]≤2​exp⁡(c22​‖σ​π^‖∞2​(T−t)),∀c>0.\mathbb{E}\left[\exp\left(c\left|\int\_{t}^{T}|\sigma\_{s}\hat{\pi}\_{s}|\mathrm{d}B\_{s}\right|\right)\right]\leq 2\exp\left(\frac{c^{2}}{2}\|\sigma\hat{\pi}\|\_{\infty}^{2}(T-t)\right),\quad\forall c>0. |  |

Combining this with R^T−R^t=∫tT(rs+(μs−rs)​π^s−12​|σs​π^s|2)​ds+σs​π^s​d​Bs\hat{R}\_{T}-\hat{R}\_{t}=\int\_{t}^{T}\left(r\_{s}+(\mu\_{s}-r\_{s})\hat{\pi}\_{s}-\frac{1}{2}|\sigma\_{s}\hat{\pi}\_{s}|^{2}\right)\mathrm{d}s+\sigma\_{s}\hat{\pi}\_{s}\mathrm{d}B\_{s},
we conclude that 𝔼t​[exp⁡(−p​ζ​(RTπ^−Rtπ^))]<∞,a.s.\mathbb{E}\_{t}\left[\exp\left(-p\zeta(R^{\hat{\pi}}\_{T}-R^{\hat{\pi}}\_{t})\right)\right]<\infty,\,a.s. for any p>1p>1. Thus, π^\hat{\pi} is an admissible strategy.

Next, we show that π^\hat{\pi} is indeed an equilibrium strategy. By Lemma [3.4](https://arxiv.org/html/2511.05861v1#S3.Thmtheorem4 "Lemma 3.4. ‣ 3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") and Z1=Z~1=0Z^{1}=\tilde{Z}^{1}=0, it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(t,R^t,πt,ε)−J​(t,Rt,π^)≤\displaystyle J(t,\hat{R}\_{t},\pi^{t,\varepsilon})-J(t,R\_{t},\hat{\pi})\leq | 𝔼t​[∫tt+εe−ζ​(R^s+Ys−R^t)​(a​(s,πst,ε)−a​(s,π^s)−ζ​σs​π^s⋅σs​η)​ds]\displaystyle\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}e^{-\zeta(\hat{R}\_{s}+Y\_{s}-\hat{R}\_{t})}(a(s,\pi^{t,\varepsilon}\_{s})-a(s,\hat{\pi}\_{s})-\zeta\sigma\_{s}\hat{\pi}\_{s}\cdot\sigma\_{s}\eta)\mathrm{d}s\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +γ2​𝔼t​[∫tt+ε((σs​π^s)2−(σs​πst,ε)2)​ds]\displaystyle+\frac{\gamma}{2}\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}((\sigma\_{s}\hat{\pi}\_{s})^{2}-(\sigma\_{s}\pi\_{s}^{t,\varepsilon})^{2})\mathrm{d}s\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼t​[∫tt+εe−ζ​(R^s+Ys−R^t)​((μs−rs)​η−12​σs2​η2−(ζ+1)​σs2​π^s​η)​ds]\displaystyle\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}e^{-\zeta(\hat{R}\_{s}+Y\_{s}-\hat{R}\_{t})}\left((\mu\_{s}-r\_{s})\eta-\frac{1}{2}\sigma\_{s}^{2}\eta^{2}-(\zeta+1)\sigma\_{s}^{2}\hat{\pi}\_{s}\eta\right)\mathrm{d}s\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −γ2​𝔼t​[∫tt+εσs​η​(2​σs​π^s+σs​η)​ds].\displaystyle-\frac{\gamma}{2}\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}\sigma\_{s}\eta\left(2\sigma\_{s}\hat{\pi}\_{s}+\sigma\_{s}\eta\right)\mathrm{d}s\right]. |  |

We first prove that

|  |  |  |
| --- | --- | --- |
|  | limε→01ε​𝔼t​[∫tt+ε|(e−ζ​(Ys+R^s−R^t)−e−ζ​Ys)​((μs−rs)​η−12​σs2​η2−(ζ+1)​σs2​π^s​η)|​ds]=0,a.s..\lim\limits\_{\varepsilon\rightarrow 0}\frac{1}{\varepsilon}\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}\left|\left(e^{-\zeta\left(Y\_{s}+\hat{R}\_{s}-\hat{R}\_{t}\right)}-e^{-\zeta Y\_{s}}\right)\left((\mu\_{s}-r\_{s})\eta-\frac{1}{2}\sigma\_{s}^{2}\eta^{2}-(\zeta+1)\sigma\_{s}^{2}\hat{\pi}\_{s}\eta\right)\right|\mathrm{d}s\right]=0,\quad a.s.. |  |

Since rr, μ\mu, σ\sigma, π^\hat{\pi}, and YY are all bounded, it suffices to show that

|  |  |  |
| --- | --- | --- |
|  | limε→01ε​𝔼t​[∫tt+ε|(e−ζ​(R^s−R^t)−1)|​ds]=0,a.s.,\lim\limits\_{\varepsilon\rightarrow 0}\frac{1}{\varepsilon}\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}\left|\left(e^{-\zeta\left(\hat{R}\_{s}-\hat{R}\_{t}\right)}-1\right)\right|\mathrm{d}s\right]=0,\quad a.s., |  |

which follows immediately from the fact that {e−ζ​(R^s−R^t)}s∈[t,T]∈L𝔽p​(Ω;(C​[t,T];ℝ))\{e^{-\zeta\left(\hat{R}\_{s}-\hat{R}\_{t}\right)}\}\_{s\in[t,T]}\in L\_{\mathbb{F}}^{p}\left(\Omega;\left(C[t,T];\mathbb{R}\right)\right).
Therefore

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | lim supε→01ε​(J​(t,R^t,πt,ε)−J​(t,R^t,π^))\displaystyle\limsup\limits\_{\varepsilon\rightarrow 0}\frac{1}{\varepsilon}\left(J(t,\hat{R}\_{t},\pi^{t,\varepsilon})-J(t,\hat{R}\_{t},\hat{\pi})\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | lim supε→01ε𝔼t[∫tt+ε(e−ζ​Ys((μs−rs)η−12σs2η2−(ζ+1)σsηu^s))−γ2σs2η2−γσsηu^s)ds]\displaystyle\limsup\limits\_{\varepsilon\rightarrow 0}\frac{1}{\varepsilon}\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}\bigg(e^{-\zeta Y\_{s}}\Big((\mu\_{s}-r\_{s})\eta-\frac{1}{2}\sigma\_{s}^{2}\eta^{2}-(\zeta+1)\sigma\_{s}\eta\hat{u}\_{s})\Big)-\frac{\gamma}{2}\sigma\_{s}^{2}\eta^{2}-\gamma\sigma\_{s}\eta\hat{u}\_{s}\bigg)\mathrm{d}s\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | lim supε→01ε​𝔼t​[∫tt+ε(−12​(e−ζ​Ys+γ)​(σs​η)2+σs​η​[e−ζ​Ys​(θs−(ζ+1)​u^s)−γ​u^s])​ds].\displaystyle\limsup\limits\_{\varepsilon\rightarrow 0}\frac{1}{\varepsilon}\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}\left(-\frac{1}{2}\left(e^{-\zeta Y\_{s}}+\gamma\right)(\sigma\_{s}\eta)^{2}+\sigma\_{s}\eta\left[e^{-\zeta Y\_{s}}\left(\theta\_{s}-(\zeta+1)\hat{u}\_{s}\right)-\gamma\hat{u}\_{s}\right]\right)\mathrm{d}s\right]. |  |

Substituting u^=e−ζ​Y​θ(ζ+1)​e−ζ​Y+γ\hat{u}=\frac{e^{-\zeta Y}\theta}{(\zeta+1)e^{-\zeta Y}+\gamma} into the above expression yields that

|  |  |  |
| --- | --- | --- |
|  | lim supε→01ε​(J​(t,R^t,πt,ε)−J​(t,R^t,π^))≤lim supε→01ε​𝔼t​[∫tt+ε(−12​(e−ζ​Ys+γ)​(σs​η)2)​ds]≤0.\limsup\limits\_{\varepsilon\rightarrow 0}\frac{1}{\varepsilon}\left(J(t,\hat{R}\_{t},\pi^{t,\varepsilon})-J(t,\hat{R}\_{t},\hat{\pi})\right)\leq\limsup\limits\_{\varepsilon\rightarrow 0}\frac{1}{\varepsilon}\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}\left(-\frac{1}{2}\left(e^{-\zeta Y\_{s}}+\gamma\right)(\sigma\_{s}\eta)^{2}\right)\mathrm{d}s\right]\leq 0. |  |

Therefore, π^\hat{\pi} is a time-consistent equilibrium strategy.
∎

### 4.2 Existence of time-consistent equilibrium under trading constraint

In this subsection, we assume that the trading strategy πt\pi\_{t} takes values in a bounded convex Borel set AA. Consequently, ut=σt​πtu\_{t}=\sigma\_{t}\pi\_{t} is also bounded. To be precise, we introduce the following definition.

###### Definition 4.5 ((Admissible trading strategy with constraint AA)).

A trading strategy π\pi is said to be admissible with constraint AA if πt∈A\pi\_{t}\in A a.s. for any t∈[0,T]t\in[0,T]. We denote by ΠA\Pi\_{A} the set of all admissible trading strategies with constraint AA.

As in the proof of Theorem [4.4](https://arxiv.org/html/2511.05861v1#S4.Thmtheorem4 "Theorem 4.4. ‣ 4.1 Existence of time-consistent equilibrium when 𝜌=0 ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets"), it is straightforward that ΠA⊆Π0\Pi\_{A}\subseteq\Pi\_{0}.
Following yan2019time and liang2025integral, we next introduce the modified definitions of the perturbation strategy and the equilibrium strategy.

###### Definition 4.6.

A strategy π^∈ΠA\hat{\pi}\in\Pi\_{A} is called an equilibrium strategy if

|  |  |  |
| --- | --- | --- |
|  | lim supε→0J​(t,π^t,ε,a)−J​(t,π^)ε≤0a.s.,\limsup\limits\_{\varepsilon\rightarrow 0}\frac{J(t,\hat{\pi}^{t,\varepsilon,a})-J(t,\hat{\pi})}{\varepsilon}\leq 0\quad a.s., |  |

for any t∈[0,T)t\in[0,T) and any a∈Lℱt∞​(Ω,A)a\in L\_{\mathcal{F}\_{t}}^{\infty}(\Omega,A) . Here

|  |  |  |
| --- | --- | --- |
|  | π^t,ε,a={a,t∈[t,t+ε),π^,t∈[t+ε,T],\hat{\pi}^{t,\varepsilon,a}=\left\{\begin{aligned} &a,\quad t\in[t,t+\varepsilon),\\ &\hat{\pi},\quad t\in[t+\varepsilon,T],\end{aligned}\right. |  |

denotes the modified perturbation strategy.

###### Remark 4.7.

In this modified definition, instead of adding an ℱt\mathcal{F}\_{t}-measurable random variable η\eta to the original strategy π^\hat{\pi}, we perturb the strategy by directly replacing it with an ℱt\mathcal{F}\_{t}-measurable random variable aa taking values in AA. This modification is made because requiring the perturbed strategy to remain admissible, i.e., πs+η∈A\pi\_{s}+\eta\in A for s∈[t,t+ε)s\in[t,t+\varepsilon), would impose a strong restriction on η\eta, possibly making it impossible to perturb many strategies.

We first introduce a lemma for the projection onto a convex closed set.

###### Lemma 4.8.

Let U⊂ℝnU\subset\mathbb{R}^{n} be a convex and closed set. Fix
w∈ℝnw\in\mathbb{R}^{n}, then we have the following two assertions: (i) if u=PU​(w)u=P\_{U}(w) is the orthogonal
projection of ww onto UU. Let
h∈ℝnh\in\mathbb{R}^{n} satisfy u+h∈Uu+h\in U. Then for any
α>0\alpha>0

|  |  |  |  |
| --- | --- | --- | --- |
|  | |α​(w−u)−h|≥α​|w−u|,\displaystyle\bigl|\alpha(w-u)-h\bigr|\geq\alpha|w-u|, |  | (4.6) |

and equality can occur only in the trivial case
h=0h=0; (ii) if U∋u≠PU​(w)U\ni u\neq P\_{U}(w), then for any α>0\alpha>0, there exists an hh such that u+h∈Uu+h\in U and

|  |  |  |
| --- | --- | --- |
|  | |α​(w−u)−h|<α​|w−u|.\bigl|\alpha(w-u)-h\bigr|<\alpha|w-u|. |  |

Moreover, hh can be chosen to be λ​(PU​(w)−u)\lambda\left(P\_{U}(w)-u\right) for any λ∈(0,2​α)\lambda\in(0,2\alpha).

###### Proof.

We first prove assertion (i). By the characterization of the orthogonal projection onto a convex set,
for every z∈Uz\in U, we have

|  |  |  |
| --- | --- | --- |
|  | ⟨w−u,z−u⟩≤0.\langle w-u,\,z-u\rangle\leq 0. |  |

Choosing z=u+h∈Uz=u+h\in U yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨w−u,h⟩≤0.\langle w-u,\,h\rangle\leq 0. |  | (4.7) |

It then follows that

|  |  |  |
| --- | --- | --- |
|  | |α​(w−u)−h|2=α2​|w−u|2+|h|2−2​α​⟨w−u,h⟩≥α2​|w−u|2.\displaystyle\bigl|\alpha(w-u)-h\bigr|^{2}=\alpha^{2}|w-u|^{2}+|h|^{2}-2\alpha\langle w-u,\,h\rangle\geq\alpha^{2}|w-u|^{2}. |  |

Taking the square root yields the desired inequality ([4.6](https://arxiv.org/html/2511.05861v1#S4.E6 "In Lemma 4.8. ‣ 4.2 Existence of time-consistent equilibrium under trading constraint ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")). Moreover, the equality requires both ⟨w−u,h⟩=0\langle w-u,h\rangle=0 and |h|2=0|h|^{2}=0, which implies that
h=0h=0.

Next we verify assertion (ii). As uu is not the projection, the vector v=PU​(w)v=P\_{U}(w) satisfies that

|  |  |  |
| --- | --- | --- |
|  | ⟨w−u,v−u⟩≥|v−u|2>0.\langle w-u,\,v-u\rangle\geq|v-u|^{2}>0. |  |

Let h=λ​(v−u),λ∈(0,1]h=\lambda(v-u),\;\lambda\in(0,1] ,then

|  |  |  |
| --- | --- | --- |
|  | |α​(w−u)−h|<α​|w−u|⇔2​α​⟨w−u,h⟩>|h|2⟸0<λ<2​α.\bigl|\alpha(w-u)-h\bigr|<\alpha|w-u|\iff 2\alpha\langle w-u,h\rangle>|h|^{2}\Longleftarrow 0<\lambda<2\alpha. |  |

Since α>0\alpha>0, the above inequality holds for sufficiently small λ>0\lambda>0. By the convexity of UU, u+h∈Uu+h\in U, which completes the proof.
∎

###### Remark 4.9.

In this lemma, we consider a convex and closed set in ℝn\mathbb{R}^{n} for any positive integer nn, rather than in ℝ\mathbb{R}, thereby showing that our subsequent proof remains valid in the presence of multiple risky assets.

By an analogous argument in section [3](https://arxiv.org/html/2511.05861v1#S3 "3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets"), we have the following necessary condition for an equilibrium strategy.

###### Theorem 4.10 (Necessary condition).

If π^\hat{\pi} is an equilibrium strategy, then then there exist (Y,Y~)(Y,\tilde{Y}) and (Z1,Z,Z~1,Z~)(Z^{1},Z,\tilde{Z}^{1},\tilde{Z}) satisfy the same condition in Theorem [3.1](https://arxiv.org/html/2511.05861v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") and the BSDE system ([3.1](https://arxiv.org/html/2511.05861v1#S3.E1 "In item 2 ‣ Theorem 3.1. ‣ 3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) and π^\hat{\pi} satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | π^=σ−1​𝒫σ​A​(e−ζ​Y​θ−ζ​e−ζ​Y​(Z1+ρ​Z)−γ​(Z~1+ρ​Z~)(ζ+1)​e−ζ​Y+γ),t∈[0,T).\displaystyle\hat{\pi}=\sigma^{-1}\mathcal{P}\_{\sigma A}\left(\frac{e^{-\zeta Y}\theta-\zeta e^{-\zeta Y}(Z^{1}+\rho Z)-\gamma(\tilde{Z}^{1}+\rho\tilde{Z})}{(\zeta+1)e^{-\zeta Y}+\gamma}\right),\quad t\in[0,T). |  | (4.8) |

###### Proof.

The derivation here is similar to that in Theorem [3.1](https://arxiv.org/html/2511.05861v1#S3.Thmtheorem1 "Theorem 3.1. ‣ 3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets"), we only give a sketch. Let Δ=σ​(a−π^)\Delta=\sigma(a-\hat{\pi}), by the same argument in Lemma [3.4](https://arxiv.org/html/2511.05861v1#S3.Thmtheorem4 "Lemma 3.4. ‣ 3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets"), we can obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | J​(t,R^t,πt,ε,a)−J​(t,Rt,π^)\displaystyle J(t,\hat{R}\_{t},\pi^{t,\varepsilon,a})-J(t,R\_{t},\hat{\pi}) |  | (4.9) |
|  | =\displaystyle= | 𝔼t​[∫tt+εe−ζ​(R^s+Ys−R^t)​(a​(s,a)−a​(s,π^s)−ζ​σs​π^s⋅Δs−ζ​Δs​(Z~s1+ρ​Zs))​ds]\displaystyle\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}e^{-\zeta(\hat{R}\_{s}+Y\_{s}-\hat{R}\_{t})}(a(s,a)-a(s,\hat{\pi}\_{s})-\zeta\sigma\_{s}\hat{\pi}\_{s}\cdot\Delta\_{s}-\zeta\Delta\_{s}\left(\tilde{Z}^{1}\_{s}+\rho Z\_{s}\right))\mathrm{d}s\right] |  |
|  |  | −ζ​𝔼t​[∫01e−ζ​(R^T+λ​ξTt,ε,a−R^t)​(1−λ)​𝑑λ​|ξTt,ε,a|2]\displaystyle-\zeta\mathbb{E}\_{t}\left[\int\_{0}^{1}e^{-\zeta(\hat{R}\_{T}+\lambda\xi\_{T}^{t,\varepsilon,a}-\hat{R}\_{t})}(1-\lambda)d\lambda|\xi\_{T}^{t,\varepsilon,a}|^{2}\right] |  |
|  |  | +γ2​𝔼t​[∫tt+ε((σs​π^s+Z~s1+ρ​Z~s)2−(σs​a+Z~s1+ρ​Z~s)2)​ds].\displaystyle+\frac{\gamma}{2}\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}\left((\sigma\_{s}\hat{\pi}\_{s}+\tilde{Z}^{1}\_{s}+\rho\tilde{Z}\_{s})^{2}-(\sigma\_{s}a+\tilde{Z}^{1}\_{s}+\rho\tilde{Z}\_{s})^{2}\right)\mathrm{d}s\right]. |  |

Moreover, by the same argument in Lemma [3.5](https://arxiv.org/html/2511.05861v1#S3.Thmtheorem5 "Lemma 3.5. ‣ 3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") and Lemma [3.6](https://arxiv.org/html/2511.05861v1#S3.Thmtheorem6 "Lemma 3.6. ‣ 3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets"), there exists a sequence {εnt}\{\varepsilon\_{n}^{t}\} and a fixed constant CC independent of aa such that for a.e.a.e. t∈[0,T)t\in[0,T),

|  |  |  |  |
| --- | --- | --- | --- |
|  | limn→∞1εnt​𝔼t\displaystyle\lim\limits\_{n\rightarrow\infty}\frac{1}{\varepsilon\_{n}^{t}}\mathbb{E}\_{t} | [∫tt+εnte−ζ​(R^s+Ys−R^t)​(a​(s,a)−a​(s,π^s)−ζ​(Zs1+σs​π^s+ρ​Zs)⋅Δs)​ds]\displaystyle\left[\int\_{t}^{t+\varepsilon\_{n}^{t}}e^{-\zeta(\hat{R}\_{s}+Y\_{s}-\hat{R}\_{t})}\left(a(s,a)-a(s,\hat{\pi}\_{s})-\zeta(Z\_{s}^{1}+\sigma\_{s}\hat{\pi}\_{s}+\rho Z\_{s})\cdot\Delta\_{s}\right)\mathrm{d}s\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | e−ζ​Yt​(θt​Δt−12​Δt2−σt​πt​Δt−ζ​(Zt1+σt​π^t+ρ​Zt)⋅Δt),a.s.,\displaystyle e^{-\zeta Y\_{t}}\left(\theta\_{t}\Delta\_{t}-\frac{1}{2}\Delta\_{t}^{2}-\sigma\_{t}\pi\_{t}\Delta\_{t}-\zeta(Z\_{t}^{1}+\sigma\_{t}\hat{\pi}\_{t}+\rho Z\_{t})\cdot\Delta\_{t}\right),\quad a.s., |  |

|  |  |  |
| --- | --- | --- |
|  | limn→∞1εnt​𝔼t​[∫01e−ζ​(R^T+λ​ξTt,ε,a−R^t)​(1−λ)​𝑑λ​|ξTt,ε,a|2]≤C​Δt2,a.s.,\lim\limits\_{n\rightarrow\infty}\frac{1}{\varepsilon\_{n}^{t}}\mathbb{E}\_{t}\left[\int\_{0}^{1}e^{-\zeta(\hat{R}\_{T}+\lambda\xi\_{T}^{t,\varepsilon,a}-\hat{R}\_{t})}(1-\lambda)d\lambda|\xi\_{T}^{t,\varepsilon,a}|^{2}\right]\leq C\Delta\_{t}^{2},\quad a.s., |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | limn→∞1εnt​𝔼t\displaystyle\lim\limits\_{n\rightarrow\infty}\frac{1}{\varepsilon\_{n}^{t}}\mathbb{E}\_{t} | [∫tt+εnt((σs​π^s+Z~s1+ρ​Z~s)2−(σs​a+Z~s1+ρ​Z~s)2)​ds]\displaystyle\left[\int\_{t}^{t+\varepsilon\_{n}^{t}}\left((\sigma\_{s}\hat{\pi}\_{s}+\tilde{Z}^{1}\_{s}+\rho\tilde{Z}\_{s})^{2}-(\sigma\_{s}a+\tilde{Z}^{1}\_{s}+\rho\tilde{Z}\_{s})^{2}\right)\mathrm{d}s\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | (σt​π^t+Z~t1+ρ​Z~t)2−(σt​a+Z~t1+ρ​Z~t)2,a.s..\displaystyle(\sigma\_{t}\hat{\pi}\_{t}+\tilde{Z}^{1}\_{t}+\rho\tilde{Z}\_{t})^{2}-(\sigma\_{t}a+\tilde{Z}^{1}\_{t}+\rho\tilde{Z}\_{t})^{2},\quad a.s.. |  |

Then the equilibrium strategy π^\hat{\pi} should satisfy that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −e−ζ​Yt+γ2​(σt​a)2+(e−ζ​Yt​(θt−ζ​(σt​π^t+Zt1+ρ​Zt))−γ​(Z~t1+ρ​Z~t))​σt​a\displaystyle-\frac{e^{-\zeta Y\_{t}}+\gamma}{2}(\sigma\_{t}a)^{2}+\left(e^{-\zeta Y\_{t}}\left(\theta\_{t}-\zeta\left(\sigma\_{t}\hat{\pi}\_{t}+Z^{1}\_{t}+\rho Z\_{t}\right)\right)-\gamma\left(\tilde{Z}^{1}\_{t}+\rho\tilde{Z}\_{t}\right)\right)\sigma\_{t}a |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ≤\displaystyle\leq | −e−ζ​Yt+γ2​(σt​π^t)2+(e−ζ​Yt​(θt−ζ​(σt​π^t+Zt1+ρ​Zt))−γ​(Z~t1+ρ​Z~t))​σt​π^t+C​Δt2,a.s..\displaystyle-\frac{e^{-\zeta Y\_{t}}+\gamma}{2}(\sigma\_{t}\hat{\pi}\_{t})^{2}+\left(e^{-\zeta Y\_{t}}\left(\theta\_{t}-\zeta\left(\sigma\_{t}\hat{\pi}\_{t}+Z^{1}\_{t}+\rho Z\_{t}\right)\right)-\gamma\left(\tilde{Z}^{1}\_{t}+\rho\tilde{Z}\_{t}\right)\right)\sigma\_{t}\hat{\pi}\_{t}+C\Delta\_{t}^{2},\quad a.s.. |  | (4.10) |

It follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | −e−ζ​Yt+γ2​Δt2+(e−ζ​Yt​(θt−(ζ+1)​σt​π^t−ζ​(Zt1+ρ​Zt))−γ​(Z~t1+ρ​Z~)−γ​σt​π^t)​Δt≤0,a.s..-\frac{e^{-\zeta Y\_{t}}+\gamma}{2}\Delta\_{t}^{2}+\left(e^{-\zeta Y\_{t}}\left(\theta\_{t}-(\zeta+1)\sigma\_{t}\hat{\pi}\_{t}-\zeta\left(Z\_{t}^{1}+\rho Z\_{t}\right)\right)-\gamma\left(\tilde{Z}\_{t}^{1}+\rho\tilde{Z}\right)-\gamma\sigma\_{t}\hat{\pi}\_{t}\right)\Delta\_{t}\leq 0,\quad a.s.. |  | (4.11) |

Suppose, to the contrary, that there exists some a∈Lℱt​(Ω,A)a\in L\_{\mathcal{F}\_{t}}(\Omega,A) such that ([4.11](https://arxiv.org/html/2511.05861v1#S4.E11 "In 4.2 Existence of time-consistent equilibrium under trading constraint ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) fails to hold. Define a new admissible strategy aλ=π^t+λ​σt−1​Δ∈Aa\_{\lambda}=\hat{\pi}\_{t}+\lambda\sigma\_{t}^{-1}\Delta\in A with sufficiently small constant λ∈(0,γγ+2​C)\lambda\in(0,\frac{\gamma}{\gamma+2C}). On one hand, by ([4.2](https://arxiv.org/html/2511.05861v1#S4.Ex19 "4.2 Existence of time-consistent equilibrium under trading constraint ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0≥\displaystyle 0\geq | −e−ζ​Yt+γ2​(σt​aλ)2+(e−ζ​Yt​(θt−ζ​(σt​π^t+Zt1+ρ​Zt))−γ​(Z~t1+ρ​Z~t))​σt​aλ−C​|aλ−π^t|2\displaystyle-\frac{e^{-\zeta Y\_{t}}+\gamma}{2}(\sigma\_{t}a\_{\lambda})^{2}+\left(e^{-\zeta Y\_{t}}\left(\theta\_{t}-\zeta\left(\sigma\_{t}\hat{\pi}\_{t}+Z^{1}\_{t}+\rho Z\_{t}\right)\right)-\gamma\left(\tilde{Z}^{1}\_{t}+\rho\tilde{Z}\_{t}\right)\right)\sigma\_{t}a\_{\lambda}-C|a\_{\lambda}-\hat{\pi}\_{t}|^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +e−ζ​Yt+γ2​(σt​π^t)2−(e−ζ​Yt​(θt−ζ​(σt​π^t+Zt1+ρ​Zt))−γ​(Z~t1+ρ​Z~t))​σt​π^t\displaystyle+\frac{e^{-\zeta Y\_{t}}+\gamma}{2}(\sigma\_{t}\hat{\pi}\_{t})^{2}-\left(e^{-\zeta Y\_{t}}\left(\theta\_{t}-\zeta\left(\sigma\_{t}\hat{\pi}\_{t}+Z^{1}\_{t}+\rho Z\_{t}\right)\right)-\gamma\left(\tilde{Z}^{1}\_{t}+\rho\tilde{Z}\_{t}\right)\right)\sigma\_{t}\hat{\pi}\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | λ​(−e−ζ​Yt+γ2​λ​Δt2+(e−ζ​Yt​(θt−(ζ+1)​σt​π^t−ζ​ρ​Zt)−γ​ρ​Z~−γ​σt​π^t)​Δt−C​λ​Δt2),a.s..\displaystyle\lambda\left(-\frac{e^{-\zeta Y\_{t}}+\gamma}{2}\lambda\Delta\_{t}^{2}+\left(e^{-\zeta Y\_{t}}\left(\theta\_{t}-(\zeta+1)\sigma\_{t}\hat{\pi}\_{t}-\zeta\rho Z\_{t}\right)-\gamma\rho\tilde{Z}-\gamma\sigma\_{t}\hat{\pi}\_{t}\right)\Delta\_{t}-C\lambda\Delta\_{t}^{2}\right),\quad a.s.. |  |

On the other hand, as λ∈(0,γγ+2​C)\lambda\in(0,\frac{\gamma}{\gamma+2C}) and ([4.11](https://arxiv.org/html/2511.05861v1#S4.E11 "In 4.2 Existence of time-consistent equilibrium under trading constraint ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) does not hold for aa, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | λ​(−e−ζ​Yt+γ2​λ​Δt2+(e−ζ​Yt​(θt−(ζ+1)​σt​π^t−ζ​ρ​Zt)−γ​ρ​Z~−γ​σt​π^t)​Δt−C​λ​Δt2)\displaystyle\lambda\left(-\frac{e^{-\zeta Y\_{t}}+\gamma}{2}\lambda\Delta\_{t}^{2}+\left(e^{-\zeta Y\_{t}}\left(\theta\_{t}-(\zeta+1)\sigma\_{t}\hat{\pi}\_{t}-\zeta\rho Z\_{t}\right)-\gamma\rho\tilde{Z}-\gamma\sigma\_{t}\hat{\pi}\_{t}\right)\Delta\_{t}-C\lambda\Delta\_{t}^{2}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≥\displaystyle\geq | λ​(−e−ζ​Yt+γ2​Δt2+(e−ζ​Yt​(θt−(ζ+1)​σt​π^t−ζ​ρ​Zt)−γ​ρ​Z~−γ​σt​π^t)​Δt)>0,\displaystyle\lambda\left(-\frac{e^{-\zeta Y\_{t}}+\gamma}{2}\Delta\_{t}^{2}+\left(e^{-\zeta Y\_{t}}\left(\theta\_{t}-(\zeta+1)\sigma\_{t}\hat{\pi}\_{t}-\zeta\rho Z\_{t}\right)-\gamma\rho\tilde{Z}-\gamma\sigma\_{t}\hat{\pi}\_{t}\right)\Delta\_{t}\right)>0, |  |

on a set of positive measure, which leads to a contradiction. Therefore, ([4.11](https://arxiv.org/html/2511.05861v1#S4.E11 "In 4.2 Existence of time-consistent equilibrium under trading constraint ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) must hold for all a∈Lℱt∞​(Ω,A)a\in L\_{\mathcal{F}\_{t}}^{\infty}(\Omega,A). Consequently, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |Δt−e−ζ​Yt​(θt−(ζ+1)​σt​π^t−ζ​(Zt1+ρ​Zt))−γ​(Z~t1+ρ​Z~)−γ​σt​π^te−ζ​Yt+γ|\displaystyle\left|\Delta\_{t}-\frac{e^{-\zeta Y\_{t}}\left(\theta\_{t}-(\zeta+1)\sigma\_{t}\hat{\pi}\_{t}-\zeta\left(Z\_{t}^{1}+\rho Z\_{t}\right)\right)-\gamma\left(\tilde{Z}\_{t}^{1}+\rho\tilde{Z}\right)-\gamma\sigma\_{t}\hat{\pi}\_{t}}{e^{-\zeta Y\_{t}}+\gamma}\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≥\displaystyle\geq | |e−ζ​Yt​(θt−(ζ+1)​σt​π^t−ζ​(Zt1+ρ​Zt))−γ​(Z~t1+ρ​Z~)−γ​σt​π^te−ζ​Yt+γ|,a.s..\displaystyle\left|\frac{e^{-\zeta Y\_{t}}\left(\theta\_{t}-(\zeta+1)\sigma\_{t}\hat{\pi}\_{t}-\zeta\left(Z\_{t}^{1}+\rho Z\_{t}\right)\right)-\gamma\left(\tilde{Z}\_{t}^{1}+\rho\tilde{Z}\right)-\gamma\sigma\_{t}\hat{\pi}\_{t}}{e^{-\zeta Y\_{t}}+\gamma}\right|,\quad a.s.. |  |

Take α=(ζ+1)​e−ζ​Yt+γe−ζ​Yt+γ\alpha=\frac{(\zeta+1)e^{-\zeta Y\_{t}}+\gamma}{e^{-\zeta Y\_{t}}+\gamma} and w=e−ζ​Y​θ−ζ​e−ζ​Y​(Z1+ρ​Z)−γ​(Z~1+ρ​Z~)(ζ+1)​e−ζ​Y+γw=\frac{e^{-\zeta Y}\theta-\zeta e^{-\zeta Y}(Z^{1}+\rho Z)-\gamma(\tilde{Z}^{1}+\rho\tilde{Z})}{(\zeta+1)e^{-\zeta Y}+\gamma}, the above inequality can be converted to

|  |  |  |
| --- | --- | --- |
|  | |σt​a−u^t−αt​(wt−u^t)|≥|αt​(wt−u^t)|,a.s..\left|\sigma\_{t}a-\hat{u}\_{t}-\alpha\_{t}\left(w\_{t}-\hat{u}\_{t}\right)\right|\geq\left|\alpha\_{t}\left(w\_{t}-\hat{u}\_{t}\right)\right|,\quad a.s.. |  |

By Lemma [4.8](https://arxiv.org/html/2511.05861v1#S4.Thmtheorem8 "Lemma 4.8. ‣ 4.2 Existence of time-consistent equilibrium under trading constraint ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")(ii), if u^t≠𝒫σt​A​(wt)\hat{u}\_{t}\neq\mathcal{P}\_{\sigma\_{t}A}\left(w\_{t}\right), as αt>1\alpha\_{t}>1, we can take λ=1\lambda=1 and then

|  |  |  |
| --- | --- | --- |
|  | |𝒫σt​A​(wt)−u^t−αt​(wt−u^t)|<|αt​(wt−u^t)|.\left|\mathcal{P}\_{\sigma\_{t}A}\left(w\_{t}\right)-\hat{u}\_{t}-\alpha\_{t}(w\_{t}-\hat{u}\_{t})\right|<\left|\alpha\_{t}(w\_{t}-\hat{u}\_{t})\right|. |  |

Thus we know that u^≠𝒫σt​A​(wt)\hat{u}\neq\mathcal{P}\_{\sigma\_{t}A}\left(w\_{t}\right) can not be an equilibrium strategy by letting σt​a=𝒫σt​A​(wt)\sigma\_{t}a=\mathcal{P}\_{\sigma\_{t}A}\left(w\_{t}\right).
Therefore, ([4.8](https://arxiv.org/html/2511.05861v1#S4.E8 "In Theorem 4.10 (Necessary condition). ‣ 4.2 Existence of time-consistent equilibrium under trading constraint ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) holds.
∎

As RR does not appear in the BSDE system, we also assume that Z1=Z~1=0Z^{1}=\tilde{Z}^{1}=0

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​Xs=m​(s,Xs)​d​t+v​(s,Xs)​d​B¯s,d​Ys=(ζ2​|ρ​Zs+u^s|2+ζ​(1−ρ2)2​|Zs|2−a​(s,π^s))​d​s+Zs​d​B¯s,d​Y~s=−a​(s,π^s)​d​s+Z~s​d​B¯s,YT=0,Y~T=0,u^=σ​π^=𝒫σt​A​(e−ζ​Y​θ−ζ​e−ζ​Y​ρ​Z−γ​ρ​Z~(ζ+1)​e−ζ​Y+γ).\left\{\begin{aligned} &\mathrm{d}X\_{s}=m(s,X\_{s})\mathrm{d}t+v(s,X\_{s})\mathrm{d}\bar{B}\_{s},\\ &\mathrm{d}Y\_{s}=\left(\frac{\zeta}{2}|\rho Z\_{s}+\hat{u}\_{s}|^{2}+\frac{\zeta(1-\rho^{2})}{2}|Z\_{s}|^{2}-a(s,\hat{\pi}\_{s})\right)\mathrm{d}s+Z\_{s}\mathrm{d}\bar{B}\_{s},\\ &\mathrm{d}\tilde{Y}\_{s}=-a(s,\hat{\pi}\_{s})\mathrm{d}s+\tilde{Z}\_{s}\mathrm{d}\bar{B}\_{s},\\ &Y\_{T}=0,\quad\tilde{Y}\_{T}=0,\quad\hat{u}=\sigma\hat{\pi}=\mathcal{P}\_{\sigma\_{t}A}\left(\frac{e^{-\zeta Y}\theta-\zeta e^{-\zeta Y}\rho Z-\gamma\rho\tilde{Z}}{(\zeta+1)e^{-\zeta Y}+\gamma}\right).\end{aligned}\right. |  | (4.12) |

To establish the existence of the BSDE system, we only need to verify the AB condition and the BF condition (see their definitions in Appendix [B](https://arxiv.org/html/2511.05861v1#A2 "Appendix B Sufficient Conditions for the Existence of Solution to BSDEs ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")).

AB condition:
:   The generator of YY satisfy that
:   |  |  |  |
    | --- | --- | --- |
    |  | −r−θ​u^≤ζ2​Z2+ζ​ρ​Z​u^−r−θ​u^+ζ+12​u^2≤ζ​(1+ρ2)2​Z2+2​ζ+12​u^2−r+θ​|u^|-r-\theta\hat{u}\leq\frac{\zeta}{2}Z^{2}+\zeta\rho Z\hat{u}-r-\theta\hat{u}+\frac{\zeta+1}{2}\hat{u}^{2}\leq\frac{\zeta(1+\rho^{2})}{2}Z^{2}+\frac{2\zeta+1}{2}\hat{u}^{2}-r+\theta|\hat{u}| |  |

    The generator of Y~\tilde{Y} satisfy that

    |  |  |  |
    | --- | --- | --- |
    |  | −r−θ2≤−r−θ​u^+12​u^2≤12​(u^−θ)2-r-\theta^{2}\leq-r-\theta\hat{u}+\frac{1}{2}\hat{u}^{2}\leq\frac{1}{2}(\hat{u}-\theta)^{2} |  |

    Let ai,i=1,2,3,4a\_{i},i=1,2,3,4 be (1,0),(−1,0),(0,1)​(0,−1)(1,0),(-1,0),(0,1)(0,-1). Then ai,i=1,2,3,4a\_{i},i=1,2,3,4 can positively span ℝ2\mathbb{R}^{2} and the generator satisfy the AB condition.

BF condition
:   The generator of YY satisfy that

    |  |  |  |
    | --- | --- | --- |
    |  | |ζ2​Z2+ζ​ρ​Z​u^−r−θ​u^+ζ+12​u^2|≤ζ​(1+ρ2)2​Z2+k​(t),\left|\frac{\zeta}{2}Z^{2}+\zeta\rho Z\hat{u}-r-\theta\hat{u}+\frac{\zeta+1}{2}\hat{u}^{2}\right|\leq\frac{\zeta(1+\rho^{2})}{2}Z^{2}+k(t), |  |

    with k​(t)=r​(t,Xt)+θ​(t,Xt)​supu^∈σt​A|u^|+2​ζ+12​supu^∈σt​A|u^|2k(t)=r(t,X\_{t})+\theta(t,X\_{t})\sup\limits\_{\hat{u}\in\sigma\_{t}A}|\hat{u}|+\frac{2\zeta+1}{2}\sup\limits\_{\hat{u}\in\sigma\_{t}A}|\hat{u}|^{2}.

    Let Cn=supt∈[0,T]{|θ​(t,Xt)|+k​(t)}C\_{n}=\sup\limits\_{t\in[0,T]}\left\{|\theta(t,X\_{t})|+k(t)\right\} and
    the generator of Y~\tilde{Y} satisfy that

    |  |  |  |
    | --- | --- | --- |
    |  | |−r−θ​u^+12​u^2|≤k​(t)|-r-\theta\hat{u}+\frac{1}{2}\hat{u}^{2}|\leq k(t) |  |

Then the BSDE system under the bounded equilibrium strategy admits a locally Holder and BMO solution (see Theorem 2.14 in xing\_class\_2018). Moreover, YY and Y~\tilde{Y} are bounded due to the terminal condition YT=0Y\_{T}=0.

###### Theorem 4.11.

Under the trading constraint ut=σt​πt∈σt​Au\_{t}=\sigma\_{t}\pi\_{t}\in\sigma\_{t}A, where A⊂ℝA\subset\mathbb{R} is a bounded closed convex Borel set, assume that (Y,Y~,Z,Z~)(Y,\tilde{Y},Z,\tilde{Z}) is a bounded BMO solution to the BSDE ([4.12](https://arxiv.org/html/2511.05861v1#S4.E12 "In 4.2 Existence of time-consistent equilibrium under trading constraint ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")), then

|  |  |  |  |
| --- | --- | --- | --- |
|  | u^t=σt​π^t=𝒫σt​A​(e−ζ​Y​θ−ζ​e−ζ​Y​ρ​Z−γ​ρ​Z~(ζ+1)​e−ζ​Y+γ)\displaystyle\hat{u}\_{t}=\sigma\_{t}\hat{\pi}\_{t}=\mathcal{P}\_{\sigma\_{t}A}\left(\frac{e^{-\zeta Y}\theta-\zeta e^{-\zeta Y}\rho Z-\gamma\rho\tilde{Z}}{(\zeta+1)e^{-\zeta Y}+\gamma}\right) |  | (4.13) |

is an equilibrium strategy.

###### Proof.

It is clear that π^∈ΠA\hat{\pi}\in\Pi\_{A}. We now prove that π^\hat{\pi} is an equilibrium strategy. Fix t∈[0,T)t\in[0,T) and let a∈Lℱt∞​(Ω;A)a\in L\_{\mathcal{F}\_{t}}^{\infty}(\Omega;A); denote the corresponding perturbed strategy by πt,ε\pi^{t,\varepsilon}. Put Δs=σs​(a−π^s)\Delta\_{s}=\sigma\_{s}(a-\hat{\pi}\_{s}).
Then, by ([4.9](https://arxiv.org/html/2511.05861v1#S4.E9 "In 4.2 Existence of time-consistent equilibrium under trading constraint ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")), it holds almost surely that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | J​(t,R^t,πt,ε,a)−J​(t,Rt,π^)\displaystyle J(t,\hat{R}\_{t},\pi^{t,\varepsilon},a)-J(t,R\_{t},\hat{\pi}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 𝔼t​[∫tt+εe−ζ​(R^s+Ys−R^t)​(a​(s,a)−a​(s,π^s)−ζ​σs​π^s⋅Δs−ζ​ρ​Δs​Zs)​ds]\displaystyle\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}e^{-\zeta(\hat{R}\_{s}+Y\_{s}-\hat{R}\_{t})}(a(s,a)-a(s,\hat{\pi}\_{s})-\zeta\sigma\_{s}\hat{\pi}\_{s}\cdot\Delta\_{s}-\zeta\rho\Delta\_{s}Z\_{s})\mathrm{d}s\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +γ2​𝔼t​[∫tt+ε((σs​π^s+ρ​Z~s)2−(σs​a+ρ​Z~s)2)​ds]\displaystyle+\frac{\gamma}{2}\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}((\sigma\_{s}\hat{\pi}\_{s}+\rho\tilde{Z}\_{s})^{2}-(\sigma\_{s}a+\rho\tilde{Z}\_{s})^{2})\mathrm{d}s\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼t​[∫tt+εe−ζ​(R^s+Ys−R^t)​(θs​Δs−12​Δs2−(ζ+1)​σs​π^s​Δs−ζ​ρ​Δs​Zs)​ds]\displaystyle\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}e^{-\zeta(\hat{R}\_{s}+Y\_{s}-\hat{R}\_{t})}\left(\theta\_{s}\Delta\_{s}-\frac{1}{2}\Delta\_{s}^{2}-(\zeta+1)\sigma\_{s}\hat{\pi}\_{s}\Delta\_{s}-\zeta\rho\Delta\_{s}Z\_{s}\right)\mathrm{d}s\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −γ2​𝔼t​[∫tt+εΔs​(2​σs​π^s+2​ρ​Z~s+Δs)​ds].\displaystyle-\frac{\gamma}{2}\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}\Delta\_{s}\left(2\sigma\_{s}\hat{\pi}\_{s}+2\rho\tilde{Z}\_{s}+\Delta\_{s}\right)\mathrm{d}s\right]. |  |

To verify that the candidate strategy is a time-consistent equilibrium, we need to show that

|  |  |  |
| --- | --- | --- |
|  | limε→01ε​𝔼t​[∫tt+ε|(e−ζ​(Ys+R^s−R^t)−e−ζ​Ys)​(θs​Δs−12​Δs2−(ζ+1)​σs​π^s​Δs−ζ​ρ​Δs​Zs)|​ds]=0.\lim\limits\_{\varepsilon\rightarrow 0}\frac{1}{\varepsilon}\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}\left|\left(e^{-\zeta\left(Y\_{s}+\hat{R}\_{s}-\hat{R}\_{t}\right)}-e^{-\zeta Y\_{s}}\right)\left(\theta\_{s}\Delta\_{s}-\frac{1}{2}\Delta\_{s}^{2}-(\zeta+1)\sigma\_{s}\hat{\pi}\_{s}\Delta\_{s}-\zeta\rho\Delta\_{s}Z\_{s}\right)\right|\mathrm{d}s\right]=0. |  |

It suffices to prove that

|  |  |  |
| --- | --- | --- |
|  | limε→01ε​𝔼t​[∫tt+ε|(e−ζ​(R^s−R^t)−1)​Zs|​ds]=0,a.s.,\lim\limits\_{\varepsilon\rightarrow 0}\frac{1}{\varepsilon}\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}\left|\left(e^{-\zeta\left(\hat{R}\_{s}-\hat{R}\_{t}\right)}-1\right)Z\_{s}\right|\mathrm{d}s\right]=0,\quad a.s., |  |

Note that {e−ζ​(R^s−R^t)}s∈[t,T]\left\{e^{-\zeta(\hat{R}\_{s}-\hat{R}\_{t})}\right\}\_{s\in[t,T]} satisfies

|  |  |  |
| --- | --- | --- |
|  | d​(e−ζ​(R^s−R^t))=−ζ​e−ζ​(R^s−R^t)​((a​(s,π^s)−ζ2​σs2​π^s2)​d​s+σs​π^s​d​Bs).\mathrm{d}\left(e^{-\zeta(\hat{R}\_{s}-\hat{R}\_{t})}\right)=-\zeta e^{-\zeta(\hat{R}\_{s}-\hat{R}\_{t})}\left(\left(a(s,\hat{\pi}\_{s})-\frac{\zeta}{2}\sigma\_{s}^{2}\hat{\pi}\_{s}^{2}\right)\mathrm{d}s+\sigma\_{s}\hat{\pi}\_{s}\mathrm{d}B\_{s}\right). |  |

Because π^\hat{\pi} is bounded, by Theorem 3.4.3 in zhang\_backward\_2017 and the same argument of Lemma [2.7](https://arxiv.org/html/2511.05861v1#S2.Thmtheorem7 "Lemma 2.7. ‣ 2 Problem Formulation ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets"), we deduce that

|  |  |  |
| --- | --- | --- |
|  | 𝔼t​[sups∈[t,t+ε]|e−ζ​(R^s−R^t)−1|2]≤C​𝔼​[(∫tt+ε|a​(s,π^s)−ζ2​σs2​π^s2|​ds)2+∫tt+εσs2​π^s2​ds]≤C​ε.\mathbb{E}\_{t}\left[\sup\_{s\in[t,t+\varepsilon]}\left|e^{-\zeta(\hat{R}\_{s}-\hat{R}\_{t})}-1\right|^{2}\right]\leq C\mathbb{E}\left[\left(\int\_{t}^{t+\varepsilon}\left|a(s,\hat{\pi}\_{s})-\frac{\zeta}{2}\sigma\_{s}^{2}\hat{\pi}\_{s}^{2}\right|\mathrm{d}s\right)^{2}+\int\_{t}^{t+\varepsilon}\sigma\_{s}^{2}\hat{\pi}\_{s}^{2}\mathrm{d}s\right]\leq C\varepsilon. |  |

Moreover, since Z∈HBMOZ\in H\_{\textup{BMO}}, ∫tT|Zs|2​ds<∞,a.s.\int\_{t}^{T}|Z\_{s}|^{2}\mathrm{d}s<\infty,\quad a.s. and for fixed tt ∫tt+ε|Zs|2​ds→ 0a.s..\int\_{t}^{t+\varepsilon}|Z\_{s}|^{2}\mathrm{d}s\;\rightarrow\;0\quad a.s.. By the Conditional Dominated Convergence Theorem

|  |  |  |
| --- | --- | --- |
|  | 𝔼t​[∫tt+ε|Zs|2​ds]⟶ 0a.s..\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}|Z\_{s}|^{2}\mathrm{d}s\right]\;\longrightarrow\;0\quad a.s.. |  |

Then

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 1ε​𝔼t​[∫tt+ε|(e−ζ​(R^s−R^t)−1)​Zs​d​s|]\displaystyle\frac{1}{\varepsilon}\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}\left|\left(e^{-\zeta\left(\hat{R}\_{s}-\hat{R}\_{t}\right)}-1\right)Z\_{s}\mathrm{d}s\right|\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 1ε​𝔼t​[∫tt+ε|e−ζ​(R^s−R^t)−1|2​ds]12​𝔼t​[∫tt+εZs2​ds]12\displaystyle\frac{1}{\varepsilon}\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}\left|e^{-\zeta\left(\hat{R}\_{s}-\hat{R}\_{t}\right)}-1\right|^{2}\mathrm{d}s\right]^{\frac{1}{2}}\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}Z\_{s}^{2}\mathrm{d}s\right]^{\frac{1}{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 1ε​𝔼t​[sups∈[t,t+ε]|e−ζ​(R^s−R^t)−1|2]12​𝔼t​[∫tt+εZs2​ds]12\displaystyle\frac{1}{\sqrt{\varepsilon}}\mathbb{E}\_{t}\left[\sup\_{s\in[t,t+\varepsilon]}\left|e^{-\zeta(\hat{R}\_{s}-\hat{R}\_{t})}-1\right|^{2}\right]^{\frac{1}{2}}\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}Z\_{s}^{2}\mathrm{d}s\right]^{\frac{1}{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | C​𝔼t​[∫tt+εZs2​ds]12⟶ 0,a.s..\displaystyle C\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}Z\_{s}^{2}\mathrm{d}s\right]^{\frac{1}{2}}\;\longrightarrow 0,\quad a.s.. |  |

Similar to Theorem [4.4](https://arxiv.org/html/2511.05861v1#S4.Thmtheorem4 "Theorem 4.4. ‣ 4.1 Existence of time-consistent equilibrium when 𝜌=0 ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets"), one can derive that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | lim supε→01ε​(J​(t,R^t,πt,ε)−J​(t,R^t,π^))\displaystyle\limsup\limits\_{\varepsilon\rightarrow 0}\frac{1}{\varepsilon}\left(J(t,\hat{R}\_{t},\pi^{t,\varepsilon})-J(t,\hat{R}\_{t},\hat{\pi})\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | lim supε→01ε𝔼t[∫tt+εe−ζ​Ys(θsΔs−12Δs2−(ζ+1)σsηu^s−ζρΔsZs)\displaystyle\limsup\limits\_{\varepsilon\rightarrow 0}\frac{1}{\varepsilon}\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}e^{-\zeta Y\_{s}}\left(\theta\_{s}\Delta\_{s}-\frac{1}{2}\Delta\_{s}^{2}-(\zeta+1)\sigma\_{s}\eta\hat{u}\_{s}-\zeta\rho\Delta\_{s}Z\_{s}\right)\right. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −γ2Δs2−γΔs(u^s+ρZ~s)ds]\displaystyle\left.-\frac{\gamma}{2}\Delta\_{s}^{2}-\gamma\Delta\_{s}(\hat{u}\_{s}+\rho\tilde{Z}\_{s})\mathrm{d}s\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | lim supε→01ε𝔼t[∫tt+ε(−12(e−ζ​Ys+γ)(Δs)2\displaystyle\limsup\limits\_{\varepsilon\rightarrow 0}\frac{1}{\varepsilon}\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}\left(-\frac{1}{2}\left(e^{-\zeta Y\_{s}}+\gamma\right)(\Delta\_{s})^{2}\right.\right. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +Δs[e−ζ​Ys(θs−(ζ+1)u^s−ζρZs)−γ(u^s+ρZ~s)])ds].\displaystyle\left.\left.+\Delta\_{s}\left[e^{-\zeta Y\_{s}}\left(\theta\_{s}-(\zeta+1)\hat{u}\_{s}-\zeta\rho Z\_{s}\right)-\gamma(\hat{u}\_{s}+\rho\tilde{Z}\_{s})\right]\right)\mathrm{d}s\right]. |  |

As σ>0\sigma>0 and σs​A\sigma\_{s}A is a closed and convex set, by Lemma [4.8](https://arxiv.org/html/2511.05861v1#S4.Thmtheorem8 "Lemma 4.8. ‣ 4.2 Existence of time-consistent equilibrium under trading constraint ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")(i), for any Δs\Delta\_{s} such that u^s+Δs∈σs​A\hat{u}\_{s}+\Delta\_{s}\in\sigma\_{s}A, it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |(ζ+1)​e−Ys+γe−Ys+γ​(e−ζ​Ys​θs−ζ​e−ζ​Ys​ρ​Zs−γ​ρ​Z~s(ζ+1)​e−Ys+γ−u^s)−Δs|\displaystyle\left|\frac{(\zeta+1)e^{-Y\_{s}}+\gamma}{e^{-Y\_{s}}+\gamma}\left(\frac{e^{-\zeta Y\_{s}}\theta\_{s}-\zeta e^{-\zeta Y\_{s}}\rho Z\_{s}-\gamma\rho\tilde{Z}\_{s}}{(\zeta+1)e^{-Y\_{s}}+\gamma}-\hat{u}\_{s}\right)-\Delta\_{s}\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≥\displaystyle\geq | |(ζ+1)​e−Ys+γe−Ys+γ​(e−ζ​Ys​θs−ζ​e−ζ​Ys​ρ​Zs−γ​ρ​Z~s(ζ+1)​e−Ys+γ−u^s)|.\displaystyle\left|\frac{(\zeta+1)e^{-Y\_{s}}+\gamma}{e^{-Y\_{s}}+\gamma}\left(\frac{e^{-\zeta Y\_{s}}\theta\_{s}-\zeta e^{-\zeta Y\_{s}}\rho Z\_{s}-\gamma\rho\tilde{Z}\_{s}}{(\zeta+1)e^{-Y\_{s}}+\gamma}-\hat{u}\_{s}\right)\right|. |  |

Thus lim supε→01ε​(J​(t,R^t,πt,ε,a)−J​(t,R^t,π^))≤0\limsup\limits\_{\varepsilon\rightarrow 0}\frac{1}{\varepsilon}\left(J(t,\hat{R}\_{t},\pi^{t,\varepsilon,a})-J(t,\hat{R}\_{t},\hat{\pi})\right)\leq 0 , a.s., which completes the proof.
∎

## 5 Approximate Time-Consistent Equilibrium for Small ρ≠0\rho\neq 0

The goal of this section is to construct and verify an approximate time-consistent equilibrium in the general case with small ρ≠0\rho\neq 0, where the approximation error can be shown to be the order O​(ρ2)O(\rho^{2}). Let us first introduce the definition of an approximate time-consistent equilibrium strategy.

###### Definition 5.1.

For π^∈Π0\hat{\pi}\in\Pi\_{0}, π^\hat{\pi} is called an approximate time-consistent equilibrium strategy with an approximation error MM if

|  |  |  |
| --- | --- | --- |
|  | lim supε→0J​(t,π^t,ε,η)−J​(t,π^)ε≤Ma.s.,\limsup\limits\_{\varepsilon\rightarrow 0}\frac{J(t,\hat{\pi}^{t,\varepsilon,\eta})-J(t,\hat{\pi})}{\varepsilon}\leq M\quad a.s., |  |

for any t∈[0,T)t\in[0,T) and any η∈Lℱt∞​(Ω,ℝ)\eta\in L\_{\mathcal{F}\_{t}}^{\infty}(\Omega,\mathbb{R}). Moreover, if M=O​(|ρ|α)M=O(|\rho|^{\alpha}), we say that the approximation error555The order of the approximation error effectively characterizes the convergence rate of the equilibrium approximation as ρ\rho tends to 0. is of the order O​(|ρ|α)O(|\rho|^{\alpha}).

Recall that for ρ=0\rho=0, the equilibrium strategy follows the form of u^=e−ζ​Y​θ(ζ+1)​e−ζ​Y+γ\hat{u}=\frac{e^{-\zeta Y}\theta}{(\zeta+1)e^{-\zeta Y}+\gamma}, where YY is the solution to the BSDE ([4.4](https://arxiv.org/html/2511.05861v1#S4.E4 "In 4.1 Existence of time-consistent equilibrium when 𝜌=0 ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")). For the case ρ≠0\rho\neq 0, we consider a trading strategy of the same structure, except that the process YY is replaced by the solution YρY^{\rho} to the following BSDE, Specifically, let YρY^{\rho} and Y~ρ\tilde{Y}^{\rho} satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​Xs=m​(s,Xs)​d​t+v​(s,Xs)​d​B¯s,d​Ysρ=(ζ2​|ρ​Zsρ+usρ|2+ζ​(1−ρ2)2​|Zsρ|2−a​(s,πsρ))​d​s+Zsρ​d​B¯s,d​Y~sρ=−a​(s,πsρ)​d​s+Z~sρ​d​B¯s,uρ=σ​πρ=e−ζ​Yρ​θ(ζ+1)​e−ζ​Yρ+γ,YT=0,Y~T=0.\left\{\begin{aligned} &\mathrm{d}X\_{s}=m(s,X\_{s})\mathrm{d}t+v(s,X\_{s})\mathrm{d}\bar{B}\_{s},\\ &\mathrm{d}Y^{\rho}\_{s}=\left(\frac{\zeta}{2}|\rho Z^{\rho}\_{s}+u^{\rho}\_{s}|^{2}+\frac{\zeta(1-\rho^{2})}{2}|Z^{\rho}\_{s}|^{2}-a(s,\pi^{\rho}\_{s})\right)\mathrm{d}s+Z^{\rho}\_{s}\mathrm{d}\bar{B}\_{s},\\ &\mathrm{d}\tilde{Y}^{\rho}\_{s}=-a(s,\pi^{\rho}\_{s})\mathrm{d}s+\tilde{Z}^{\rho}\_{s}\mathrm{d}\bar{B}\_{s},\\ &u^{\rho}=\sigma\pi^{\rho}=\frac{e^{-\zeta Y^{\rho}}\theta}{(\zeta+1)e^{-\zeta Y^{\rho}}+\gamma},\quad Y\_{T}=0,\quad\tilde{Y}\_{T}=0.\end{aligned}\right. |  | (5.1) |

Next, we will rigorously verify that the constructed strategy uρu^{\rho} is an approximate time-consistent equilibrium satisfying Definition [5.1](https://arxiv.org/html/2511.05861v1#S5.Thmtheorem1 "Definition 5.1. ‣ 5 Approximate Time-Consistent Equilibrium for Small 𝜌≠0 ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets").

Let RtρR\_{t}^{\rho} denote the log return at tt under strategy uρu^{\rho}. We first show that the Markovian BSDE system ([5.1](https://arxiv.org/html/2511.05861v1#S5.E1 "In 5 Approximate Time-Consistent Equilibrium for Small 𝜌≠0 ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) admits a solution such that YρY^{\rho} and ZρZ^{\rho} are uniformly bounded with bounds independent of ρ∈[−1,1]\rho\in[-1,1] To this end, we need to impose an additional assumption as below.

###### Assumption 5.2.

We assume that

1. 1.

   vv is differentiable w.r.t. t,xt,x and vxv\_{x} is uniformly bounded.
2. 2.

   There exists a positive constant β>0\beta>0 such that v,vx,m,r,θv,v\_{x},m,r,\theta are Hölder continuous w. r. t x,tx,t with exponents β,β/2\beta,\beta/2 respectively for any bounded cylinder QTQ\_{T} of the layer RTR\_{T}.

By the nonlinear Feynman-Kac formula, if the PDE

|  |  |  |
| --- | --- | --- |
|  | ℒ​f=ζ​ρ​fx​v​uρ+ζ2​fx2​v2−r−θ​uρ+ζ+12​(uρ)2\mathcal{L}f=\zeta\rho f\_{x}vu^{\rho}+\frac{\zeta}{2}f\_{x}^{2}v^{2}-r-\theta u^{\rho}+\frac{\zeta+1}{2}(u^{\rho})^{2} |  |

admits a classical solution with the terminal conditionf​(T,x)=1f(T,x)=1. Let Yt:=f​(t,Xt)Y\_{t}:=f(t,X\_{t}) and Zt:=fx​(t,Xt)​v​(t,Xt)Z\_{t}:=f\_{x}(t,X\_{t})v(t,X\_{t}). Then (Y,Z)(Y,Z) is the solution to our BSDE. This is a cauchy problem and we introduce the following classical result for the quasi-linear equations with the principal part in divergence form,

|  |  |  |
| --- | --- | --- |
|  | ut−dd​xi​ai​(t,x,u,ux)+a​(t,x,u,ux)=0,u\_{t}-\frac{d}{dx\_{i}}a\_{i}(t,x,u,u\_{x})+a(t,x,u,u\_{x})=0, |  |

with u​(0,x)=ψ0​(x)u(0,x)=\psi\_{0}(x) in RT=[0,T]×ℝnR\_{T}=[0,T]\times\mathbb{R}^{n} and

|  |  |  |
| --- | --- | --- |
|  | ai​j​(x,t,u,p)≡∂ai​(x,t,u,p)∂pj,A​(x,t,u,p)≡a​(x,t,u,p)−∂ai∂u​pi−∂ai∂xi.a\_{ij}(x,t,u,p)\equiv\frac{\partial a\_{i}(x,t,u,p)}{\partial p\_{j}},\quad A(x,t,u,p)\equiv a(x,t,u,p)-\frac{\partial a\_{i}}{\partial u}p\_{i}-\frac{\partial a\_{i}}{\partial x\_{i}}. |  |

###### Remark 5.3.

The existence of solution to the BSDE system ([5.1](https://arxiv.org/html/2511.05861v1#S5.E1 "In 5 Approximate Time-Consistent Equilibrium for Small 𝜌≠0 ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) can be investigated in xing\_class\_2018 and FAN20161511, in which a BMO solution can be established. However, we require the boundedness of ZZ and Z~\tilde{Z} in our verification theorem (Theorem [5.5](https://arxiv.org/html/2511.05861v1#S5.Thmtheorem5 "Theorem 5.5. ‣ 5 Approximate Time-Consistent Equilibrium for Small 𝜌≠0 ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")). Therefore, we employ the Feynman–Kac representation and resort to a PDE-based analysis. Specifically, we utilize Theorem [5.4](https://arxiv.org/html/2511.05861v1#S5.Thmtheorem4 "Theorem 5.4. ‣ 5 Approximate Time-Consistent Equilibrium for Small 𝜌≠0 ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") as a technical tool to derive the desired boundedness.

###### Theorem 5.4.

Suppose that the following conditions hold.

1. a)\mathrm{a)}

   ψ0​(x)∈H2+β​(Ω)\psi\_{0}(x)\in H^{2+\beta}(\Omega) in any Ω⊂ℝn\Omega\subset\mathbb{R}^{n} and maxℝn⁡|ψ0​(x)|<∞.\max\_{\mathbb{R}^{n}}|\psi\_{0}(x)|<\infty.
2. b)\mathrm{b)}

   For t∈(0,T]t\in(0,T] and arbitrary x,u,px,u,p, we have

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | μ1​ξ2≤ai​j​(t,x,u,p)​ξ2≤μ2​ξ2,\mu\_{1}\xi^{2}\leq a\_{ij}(t,x,u,p)\xi^{2}\leq\mu\_{2}\xi^{2}, |  | (5.2) |

   with positive constants μ1>0\mu\_{1}>0 and μ>0\mu>0 and

   |  |  |  |
   | --- | --- | --- |
   |  | A​(x,t,u,0)​u≥−b1​u2−b2,with constants​b1,b2≥0.A(x,t,u,0)u\geq-b\_{1}u^{2}-b\_{2},\quad\text{with constants}\ b\_{1},\,b\_{2}\geq 0. |  |
3. c)\mathrm{c)}

   For any bounded cylinder QTQ\_{T} of the layer RTR\_{T} and |u|≤M|u|\leq M, where MM is a constant depending only on b1,b2b\_{1},b\_{2} and ψ0\psi\_{0}, it holds that
   ∑\_i=1^n ( — a\_i — + — ∂ai∂u — ) (1 + —p—) + ∑\_i, j=1^n — ∂ai∂xj — + —a— ≤μ(1 + —p—)^2.
   Moreover, the functions ai​(x,t,u,p)a\_{i}(x,t,u,p) and a​(x,t,u,p)a(x,t,u,p) are continuous, and ai​(t,x,u,p)a\_{i}(t,x,u,p) is differentiable w.r.t. variables x,u,px,u,p for each ii.
4. d)\mathrm{d)}

   For any bounded cylinder QTQ\_{T} of the layer RTR\_{T} and |u|≤M|u|\leq M, |p|≤M1|p|\leq M\_{1}, where M1M\_{1} is a constant depending only on M,μ,μ1,μ2M,\mu,\mu\_{1},\mu\_{2} and ψ\psi, the function ai,a,∂ai∂pj,∂ai∂ua\_{i},a,\frac{\partial a\_{i}}{\partial p\_{j}},\frac{\partial a\_{i}}{\partial u}, and ∂ai∂xi\frac{\partial a\_{i}}{\partial x\_{i}} are continuous functions satisfying a Hölder condition in x,t,ux,t,u and pp with exponents β,β/2,β\beta,\beta/2,\beta and β\beta respectively.

Then there exists at least one solution u​(x,t)u(x,t) of the Cauchy problem([5.2](https://arxiv.org/html/2511.05861v1#S5.E2 "In item b) ‣ Theorem 5.4. ‣ 5 Approximate Time-Consistent Equilibrium for Small 𝜌≠0 ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) in the strip RTR\_{T} that |u|≤M|u|\leq M, |ux|≤M1|u\_{x}|\leq M\_{1} and belongs to H2+β,1+β/2​(QT¯)H^{2+\beta,1+\beta/2}(\overline{Q\_{T}}) for any bounded cylinder QT⊂RTQ\_{T}\subset R\_{T}. It will be an element of H2+β,1+β/2​(RT)H^{2+\beta,1+\beta/2}(R\_{T}) if it is further assumed that the constants in conditions c)-d) do not depend on QTQ\_{T}.

###### Proof.

The result follows directly from Theorem 6.1 and Theorem 8.1 in ladyzhenskaia1968linear. The dependence of MM and M1M\_{1} can be found in Theorem 2.9 and (6.10) in ladyzhenskaia1968linear.
∎

Next, we verify that our equations satisfy these conditions under Assumptions [4.1](https://arxiv.org/html/2511.05861v1#S4.Thmtheorem1 "Assumption 4.1. ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets"), [4.2](https://arxiv.org/html/2511.05861v1#S4.Thmtheorem2 "Assumption 4.2. ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") and [5.2](https://arxiv.org/html/2511.05861v1#S5.Thmtheorem2 "Assumption 5.2. ‣ 5 Approximate Time-Consistent Equilibrium for Small 𝜌≠0 ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets"). We reverse the time and still denote f​(T−t,x)f(T-t,x) by f​(t,x)f(t,x) and rewrite the PDE in the divergence form

|  |  |  |  |
| --- | --- | --- | --- |
|  | ft−dd​x​(12​v2​(t,x)​fx)+a​(t,x,f,fx)=0,f\_{t}-\frac{\mathrm{d}}{\mathrm{d}x}\left(\frac{1}{2}v^{2}(t,x)f\_{x}\right)+a(t,x,f,f\_{x})=0, |  | (5.3) |

with f​(0,x)=1f(0,x)=1. Here we suppress the dependence of the functions on (t,x)(t,x) for notational simplicity and also denote that

|  |  |  |
| --- | --- | --- |
|  | a​(t,x,f,p)=−m​p+ζ​ρ​p​v​e−ζ​f​θ(ζ+1)​e−ζ​f+γ+ζ2​p2​v2−r−θ​e−ζ​f​θ(ζ+1)​e−ζ​f+γ+(e−ζ​f​θ(ζ+1)​e−ζ​f+γ)2+v​vx​p,a(t,x,f,p)=-mp+\zeta\rho pv\frac{e^{-\zeta f}\theta}{(\zeta+1)e^{-\zeta f}+\gamma}+\frac{\zeta}{2}p^{2}v^{2}-r-\theta\frac{e^{-\zeta f}\theta}{(\zeta+1)e^{-\zeta f}+\gamma}+\left(\frac{e^{-\zeta f}\theta}{(\zeta+1)e^{-\zeta f}+\gamma}\right)^{2}+vv\_{x}p, |  |

|  |  |  |
| --- | --- | --- |
|  | A​(t,x,f,p)=−m​p+ζ​ρ​p​v​e−ζ​f​θ(ζ+1)​e−ζ​f+γ+ζ2​p2​v2−r−θ​e−ζ​f​θ(ζ+1)​e−ζ​f+γ+(e−ζ​f​θ(ζ+1)​e−ζ​f+γ)2.A(t,x,f,p)=-mp+\zeta\rho pv\frac{e^{-\zeta f}\theta}{(\zeta+1)e^{-\zeta f}+\gamma}+\frac{\zeta}{2}p^{2}v^{2}-r-\theta\frac{e^{-\zeta f}\theta}{(\zeta+1)e^{-\zeta f}+\gamma}+\left(\frac{e^{-\zeta f}\theta}{(\zeta+1)e^{-\zeta f}+\gamma}\right)^{2}. |  |

In our case, ψ0=0\psi\_{0}=0 and ai​j=12​v2a\_{ij}=\frac{1}{2}v^{2} where vv has positive upper and lower bounds. Let b1=b2=12​(‖r‖∞+14​‖θ‖∞2)b\_{1}=b\_{2}=\frac{1}{2}\left(||r||\_{\infty}+\frac{1}{4}||\theta||\_{\infty}^{2}\right), we have

|  |  |  |
| --- | --- | --- |
|  | A​(t,x,f,0)​f=(−r−θ​e−ζ​f​θ(ζ+1)​e−ζ​f+γ+(e−ζ​f​θ(ζ+1)​e−ζ​f+γ)2)​f≥−12​(‖r‖∞+14​‖θ‖∞2)​(f2+1),A(t,x,f,0)f=\left(-r-\theta\frac{e^{-\zeta f}\theta}{(\zeta+1)e^{-\zeta f}+\gamma}+\left(\frac{e^{-\zeta f}\theta}{(\zeta+1)e^{-\zeta f}+\gamma}\right)^{2}\right)f\geq-\frac{1}{2}\left(||r||\_{\infty}+\frac{1}{4}||\theta||\_{\infty}^{2}\right)(f^{2}+1), |  |

and the first two conditions are verified given the differentiability of vv. For condition c), we have

|  |  |  |
| --- | --- | --- |
|  | (|ai|+|∂ai∂f|)​(1+|p|)+|∂ai∂xj|+|a|=12​v2​|p|​(1+|p|)+|v​vx​p|+|a​(t,x,f,p)|≤C​(1+|p|2),\displaystyle\left(\left|a\_{i}\right|+\left|\frac{\partial a\_{i}}{\partial f}\right|\right)(1+|p|)+\left|\frac{\partial a\_{i}}{\partial x\_{j}}\right|+|a|=\frac{1}{2}v^{2}|p|(1+|p|)+|vv\_{x}p|+|a(t,x,f,p)|\leq C(1+|p|^{2}), |  |

as θ,v,vx,m,uρ\theta,v,v\_{x},m,u^{\rho} are bounded independent of ρ\rho and 0≤ρ≤10\leq\rho\leq 1. We emphasize that CC can be chosen independently of ρ\rho. To verify the final condition in the theorem, we employ a minor result concerning Hölder continuous functions. That is, if h1h\_{1} and h2h\_{2} are two bounded Hölder continuous functions with α1\alpha\_{1} and α2\alpha\_{2} being their Hölder coefficients respectively, then h1​h2h\_{1}h\_{2} is a Hölder continuous function with Hölder coefficient min⁡(α1,α2)\min(\alpha\_{1},\alpha\_{2}). Then condition d) can be easily verified and there exists a solution f∈C2+β,1+β/2​(QT)f\in C^{2+\beta,1+\beta/2}(Q\_{T}) for any bounded cylinder QTQ\_{T} of the layer RTR\_{T}. Moreover, as b1,b2,μ,μ1,μ2b\_{1},b\_{2},\mu,\mu\_{1},\mu\_{2} are independent of ρ\rho, the constant MM and M1M\_{1} also do not depend on ρ\rho. Then Zρ=m​fxZ^{\rho}=mf\_{x} is bounded independently of ρ\rho.

For the same reason, we seek the solution to

|  |  |  |
| --- | --- | --- |
|  | ℒ​g=−r−θ​e−ζ​f​θ(ζ+1)​e−ζ​f+γ+12​(e−ζ​f​θ(ζ+1)​e−ζ​f+γ)2,\mathcal{L}g=-r-\theta\frac{e^{-\zeta f}\theta}{(\zeta+1)e^{-\zeta f}+\gamma}+\frac{1}{2}\left(\frac{e^{-\zeta f}\theta}{(\zeta+1)e^{-\zeta f}+\gamma}\right)^{2}, |  |

with the terminal condition g​(T,x)=0g(T,x)=0. Here ff is the solution to equation ([5.3](https://arxiv.org/html/2511.05861v1#S5.E3 "In 5 Approximate Time-Consistent Equilibrium for Small 𝜌≠0 ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")). By the same argument, Z~ρ\tilde{Z}^{\rho} is also bounded independently of ρ\rho.

Next, we turn to show that πρ\pi^{\rho} is an approximate time-consistent equilibrium. Thanks to the concavity of the utility function, it holds that

|  |  |  |
| --- | --- | --- |
|  | J​(t,Rtρ,πt,ε)−J​(t,Rtρ,πρ)≤eRtρ​𝔼t​[U′​(RTρ)​ξTt,ε]+γ2​(Var​(RTρ)−Var​(RTt,ε))\displaystyle J(t,R\_{t}^{\rho},\pi^{t,\varepsilon})-J(t,R\_{t}^{\rho},\pi^{\rho})\leq e^{R\_{t}^{\rho}}\mathbb{E}\_{t}\left[U^{\prime}(R\_{T}^{\rho})\xi\_{T}^{t,\varepsilon}\right]+\frac{\gamma}{2}\left(\textup{Var}(R\_{T}^{\rho})-\textup{Var}(R\_{T}^{t,\varepsilon})\right) |  |

Here, we use πt,ε=πρ+η​𝟙s∈[t,t+ε)\pi^{t,\varepsilon}=\pi^{\rho}+\eta\mathds{1}\_{s\in[t,t+\varepsilon)} to denote the perturbation strategy and let ξt,ε\xi^{t,\varepsilon} be the resulting difference process for any η∈Lℱt∞​(Ω;ℝ)\eta\in L^{\infty}\_{\mathcal{F}\_{t}}(\Omega;\mathbb{R}) and we shall omit the dependence on ρ\rho and η\eta for simplicity.

###### Theorem 5.5.

Under Assumptions [4.1](https://arxiv.org/html/2511.05861v1#S4.Thmtheorem1 "Assumption 4.1. ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets"), [4.2](https://arxiv.org/html/2511.05861v1#S4.Thmtheorem2 "Assumption 4.2. ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets"), [5.2](https://arxiv.org/html/2511.05861v1#S5.Thmtheorem2 "Assumption 5.2. ‣ 5 Approximate Time-Consistent Equilibrium for Small 𝜌≠0 ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets"), the strategy πρ\pi^{\rho} is admissible for any fixed ρ∈[0,1]\rho\in[0,1]. Moreover, πρ\pi^{\rho} is an approximate time-consistent equilibrium with the approximate error of the order O​(ρ2)O(\rho^{2}) such that for any t∈[0,T]t\in[0,T] and any fixed η∈Lℱt∞​(Ω;ℝ)\eta\in L\_{\mathcal{F}\_{t}}^{\infty}(\Omega;\mathbb{R}),

|  |  |  |
| --- | --- | --- |
|  | lim supε→01ε​(J​(t,Rtρ,πt,ε)−J​(t,Rtρ,πρ))≤C​ρ2.\displaystyle\limsup\limits\_{\varepsilon\rightarrow 0}\frac{1}{\varepsilon}\left(J(t,R\_{t}^{\rho},\pi^{t,\varepsilon})-J(t,R\_{t}^{\rho},\pi^{\rho})\right)\leq C\rho^{2}. |  |

Here CC is a positive constant independent of tt, η\eta and ρ\rho.

###### Proof.

As πρ\pi^{\rho} is a bounded strategy, it follows from the same arguments for Theorem [4.4](https://arxiv.org/html/2511.05861v1#S4.Thmtheorem4 "Theorem 4.4. ‣ 4.1 Existence of time-consistent equilibrium when 𝜌=0 ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") that πρ\pi^{\rho} is an admissible strategy.
We next show that πρ\pi^{\rho} is an approximate Nash equilibrium strategy. Fix t∈[0,T)t\in[0,T) and η∈Lℱt∞​(Ω;ℝ)\eta\in L\_{\mathcal{F}\_{t}}^{\infty}(\Omega;\mathbb{R}) and use πt,ε\pi^{t,\varepsilon} to denote the perturbed strategy. By Lemma [3.4](https://arxiv.org/html/2511.05861v1#S3.Thmtheorem4 "Lemma 3.4. ‣ 3 A Necessary Condition of Time-Consistent Equilibria ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") and the same argument in Theorem [4.11](https://arxiv.org/html/2511.05861v1#S4.Thmtheorem11 "Theorem 4.11. ‣ 4.2 Existence of time-consistent equilibrium under trading constraint ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets"), it holds that, a.s.,

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | J​(t,Rtρ,πt,ε)−J​(t,Rtρ,πρ)\displaystyle J(t,R\_{t}^{\rho},\pi^{t,\varepsilon})-J(t,R\_{t}^{\rho},\pi^{\rho}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | 𝔼t​[∫tt+εe−ζ​Ysρ​((μs−rs)​η−12​σs2​η2−(ζ+1)​σs​η​usρ−ζ​ρ​σs​η​Zsρ)​ds]−γ2​𝔼​[σs​η​(2​usρ+2​ρ​Z~sρ+σs​η)​d​s]\displaystyle\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}e^{-\zeta Y^{\rho}\_{s}}\left((\mu\_{s}-r\_{s})\eta-\frac{1}{2}\sigma\_{s}^{2}\eta^{2}-(\zeta+1)\sigma\_{s}\eta u^{\rho}\_{s}-\zeta\rho\sigma\_{s}\eta Z^{\rho}\_{s}\right)\mathrm{d}s\right]-\frac{\gamma}{2}\mathbb{E}\left[\sigma\_{s}\eta(2u^{\rho}\_{s}+2\rho\tilde{Z}^{\rho}\_{s}+\sigma\_{s}\eta)\mathrm{d}s\right] |  |

By the same arguments for Theorem [4.4](https://arxiv.org/html/2511.05861v1#S4.Thmtheorem4 "Theorem 4.4. ‣ 4.1 Existence of time-consistent equilibrium when 𝜌=0 ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") and Theorem [4.11](https://arxiv.org/html/2511.05861v1#S4.Thmtheorem11 "Theorem 4.11. ‣ 4.2 Existence of time-consistent equilibrium under trading constraint ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets"), we deduce that

|  |  |  |
| --- | --- | --- |
|  | limε→01ε​𝔼t​[∫tt+ε|(e−ζ​(Ysρ+Rsρ−Rtρ)−e−ζ​Ysρ)​((μs−rs)​η−12​σs2​η2−(ζ+1)​σs2​πsρ​η−ζ​ρ​σs​η​Zsρ)|​ds]=0,a.s..\lim\limits\_{\varepsilon\rightarrow 0}\frac{1}{\varepsilon}\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}\left|\left(e^{-\zeta\left(Y^{\rho}\_{s}+R^{\rho}\_{s}-R^{\rho}\_{t}\right)}-e^{-\zeta Y^{\rho}\_{s}}\right)\left((\mu\_{s}-r\_{s})\eta-\frac{1}{2}\sigma\_{s}^{2}\eta^{2}-(\zeta+1)\sigma\_{s}^{2}\pi^{\rho}\_{s}\eta-\zeta\rho\sigma\_{s}\eta Z^{\rho}\_{s}\right)\right|\mathrm{d}s\right]=0,\quad a.s.. |  |

Consequently, it holds that

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | lim supε→01ε​(J​(t,Rtρ,πt,ε)−J​(t,Rtρ,πρ))\displaystyle\limsup\limits\_{\varepsilon\rightarrow 0}\frac{1}{\varepsilon}\left(J(t,R\_{t}^{\rho},\pi^{t,\varepsilon})-J(t,R\_{t}^{\rho},\pi^{\rho})\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | lim supε→01ε𝔼t[∫tt+ε{e−ζ​Ysρ((μs−rs)η−12σs2η2−(ζ+1)σsηusρ−ζρσsηZsρ)\displaystyle\limsup\limits\_{\varepsilon\rightarrow 0}\frac{1}{\varepsilon}\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}\bigg\{e^{-\zeta Y^{\rho}\_{s}}\left((\mu\_{s}-r\_{s})\eta-\frac{1}{2}\sigma\_{s}^{2}\eta^{2}-(\zeta+1)\sigma\_{s}\eta u^{\rho}\_{s}-\zeta\rho\sigma\_{s}\eta Z^{\rho}\_{s}\right)\right. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −γ2σs2η2−γσsη(usρ+ρZ~sρ)}ds]\displaystyle\left.-\frac{\gamma}{2}\sigma\_{s}^{2}\eta^{2}-\gamma\sigma\_{s}\eta(u^{\rho}\_{s}+\rho\tilde{Z}^{\rho}\_{s})\bigg\}\mathrm{d}s\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | lim supε→01ε​𝔼t​[∫tt+ε(−12​(e−ζ​Ysρ+γ)​(σs​η)2−σs​η​[ζ​e−ζ​Ysρ​ρ​Zsρ+γ​ρ​Z~sρ])​ds]\displaystyle\limsup\limits\_{\varepsilon\rightarrow 0}\frac{1}{\varepsilon}\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}\left(-\frac{1}{2}\left(e^{-\zeta Y^{\rho}\_{s}}+\gamma\right)(\sigma\_{s}\eta)^{2}-\sigma\_{s}\eta\left[\zeta e^{-\zeta Y^{\rho}\_{s}}\rho Z^{\rho}\_{s}+\gamma\rho\tilde{Z}^{\rho}\_{s}\right]\right)\mathrm{d}s\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ≤\displaystyle\leq | lim supε→01ε​𝔼t​[∫tt+ε(ζ​e−ζ​Ysρ​Zsρ+γ​Z~sρ)22​(e−ζ​Ysρ+γ)​ds]​ρ2≤C​ρ2.\displaystyle\limsup\limits\_{\varepsilon\rightarrow 0}\frac{1}{\varepsilon}\mathbb{E}\_{t}\left[\int\_{t}^{t+\varepsilon}\frac{(\zeta e^{-\zeta Y^{\rho}\_{s}}Z^{\rho}\_{s}+\gamma\tilde{Z}^{\rho}\_{s})^{2}}{2(e^{-\zeta Y^{\rho}\_{s}}+\gamma)}\mathrm{d}s\right]\rho^{2}\leq C\rho^{2}. |  |

Here CC is a constant independent of ρ\rho and tt.
Thus πρ=σ−1​e−ζ​Yρ​θ(ζ+1)​e−ζ​Yρ+γ\pi^{\rho}=\sigma^{-1}\frac{e^{-\zeta Y^{\rho}}\theta}{(\zeta+1)e^{-\zeta Y^{\rho}}+\gamma} is an approximate time-consistent equilibrium with the desired approximation error C​ρ2C\rho^{2}.
∎

## 6 Numerical Examples

In this section, we present some numerical studies on the equilibrium strategy in the incomplete factor market model by employing some deep learning algorithms developed in e\_deep\_2017 and Han\_2018 to our BSDE systems ([4.4](https://arxiv.org/html/2511.05861v1#S4.E4 "In 4.1 Existence of time-consistent equilibrium when 𝜌=0 ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")), ([4.12](https://arxiv.org/html/2511.05861v1#S4.E12 "In 4.2 Existence of time-consistent equilibrium under trading constraint ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")), and ([5.1](https://arxiv.org/html/2511.05861v1#S5.E1 "In 5 Approximate Time-Consistent Equilibrium for Small 𝜌≠0 ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")).
In particular, to fulfill our model assumptions, we consider a truncated time-varying Gaussian mean-return model
in which the stock price process StS\_{t} and the market factor process XtX\_{t} evolve as

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​StSt\displaystyle\frac{\mathrm{d}S\_{t}}{S\_{t}} | =(r+σ⋅θ​(Xt))​d​t+σ​d​Bt,\displaystyle=(r+\sigma\cdot\theta(X\_{t}))\mathrm{d}t+\sigma\mathrm{d}B\_{t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt\displaystyle\mathrm{d}X\_{t} | =λ​(−10000∨(X¯−Xt)∧10000)​d​t+ν​d​B¯t.\displaystyle=\lambda(-0000\vee(\bar{X}-X\_{t})\wedge 0000)\mathrm{d}t+\nu\mathrm{d}\bar{B}\_{t}. |  |

Here, we choose θ​(X):=X+∧10000\theta(X):=X^{+}\wedge 10000 to ensure that Assumptions [4.1](https://arxiv.org/html/2511.05861v1#S4.Thmtheorem1 "Assumption 4.1. ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets"), [4.2](https://arxiv.org/html/2511.05861v1#S4.Thmtheorem2 "Assumption 4.2. ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets"), and [5.2](https://arxiv.org/html/2511.05861v1#S5.Thmtheorem2 "Assumption 5.2. ‣ 5 Approximate Time-Consistent Equilibrium for Small 𝜌≠0 ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") are satisfied. Similar to dai\_dynamic\_2021, we fix the parameter values: r=0.017r=0.017, σ=0.15\sigma=0.15, X0=X¯=0.273X\_{0}=\bar{X}=0.273, λ=0.27\lambda=0.27 and ν=0.065\nu=0.065. Moreover, we set ζ=1\zeta=1, γ=0.1\gamma=0.1 and T=2T=2 for the base model.
We discretize the horizon [0,T][0,T] into time grid 0=t0<t1<⋯<tN=T0=t\_{0}<t\_{1}<\cdots<t\_{N}=T, where ti=i​Δ​tt\_{i}=i\Delta t for i=0,1,…,Ni=0,1,\dots,N and Δ​t=T/N\Delta t=T/N. Henceforth, for notational simplicity, we use the subscript nn to denote the processes evaluated at time tnt\_{n}. The truncated Ornstein–Uhlenbeck process XX is approximated by the Euler scheme:

|  |  |  |
| --- | --- | --- |
|  | Xn+1=Xn+λ​(−10000∨(X¯−Xn)∧10000)​Δ​t+ν​(B¯n+1−B¯n)X\_{n+1}=X\_{n}+\lambda(-10000\vee(\bar{X}-X\_{n})\wedge 10000)\Delta t+\nu(\bar{B}\_{n+1}-\bar{B}\_{n}) |  |

for n=1,⋯,N−1n=1,\cdots,N-1, with X0=0.273X\_{0}=0.273.
To numerically illustrate our theoreticla results, we trained three models. For the decoupled BSDE systems ([4.4](https://arxiv.org/html/2511.05861v1#S4.E4 "In 4.1 Existence of time-consistent equilibrium when 𝜌=0 ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) and ([5.1](https://arxiv.org/html/2511.05861v1#S5.E1 "In 5 Approximate Time-Consistent Equilibrium for Small 𝜌≠0 ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")), because the equilibrium strategy π^\hat{\pi} (for ρ=0\rho=0) and the approximate Nash equilibrium strategy πρ\pi^{\rho} both only depend on the process YY, we consider the discretized form of YY in each case, respectively:

|  |  |  |
| --- | --- | --- |
|  | Yn+1=Yn+(ζ2​|u^s|2+ζ2​|Zn|2−a​(tn,π^n))​Δ​t+Zn​(B¯n+1−B¯n),Y\_{n+1}=Y\_{n}+\left(\frac{\zeta}{2}|\hat{u}\_{s}|^{2}+\frac{\zeta}{2}|Z\_{n}|^{2}-a(t\_{n},\hat{\pi}\_{n})\right)\Delta t+Z\_{n}(\bar{B}\_{n+1}-\bar{B}\_{n}), |  |

and

|  |  |  |
| --- | --- | --- |
|  | Yn+1ρ=Ynρ+(ζ2​|ρ​Znρ+unρ|2+ζ​(1−ρ2)2​|Zn|2−a​(tn,πnρ))​Δ​t+Zn​(B¯n+1−B¯n).Y\_{n+1}^{\rho}=Y\_{n}^{\rho}+\left(\frac{\zeta}{2}|\rho Z\_{n}^{\rho}+u^{\rho}\_{n}|^{2}+\frac{\zeta(1-\rho^{2})}{2}|Z\_{n}|^{2}-a(t\_{n},\pi^{\rho}\_{n})\right)\Delta t+Z\_{n}(\bar{B}\_{n+1}-\bar{B}\_{n}). |  |

We then employ a deep learning approximation for the initial conditions (Y0,Z0)(Y\_{0},Z\_{0}) and the sequence {Zn}n=1N−1\{Z\_{n}\}\_{n=1}^{N-1}, using {Xn}n=0N−1\{X\_{n}\}\_{n=0}^{N-1} as inputs. Particularly, we use N−1N-1 fully connected feedforward neural networks with bias terms to represent {Zn}n=1N−1\{Z\_{n}\}\_{n=1}^{N-1} and two trainable parameters (Y0,Z0)(Y\_{0},Z\_{0}) to represent the initial values of YY and ZZ at time t0t\_{0}. Motivated by the terminal condition YT=0Y\_{T}=0, we define the mean squared loss function as

|  |  |  |
| --- | --- | --- |
|  | L​o​s​s=𝔼​[|YN|2].Loss=\mathbb{E}\big[|Y\_{N}|^{2}\big]. |  |

For the coupled BSDE system ([4.12](https://arxiv.org/html/2511.05861v1#S4.E12 "In 4.2 Existence of time-consistent equilibrium under trading constraint ‣ 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")), we consider the following discretized counterparts:

|  |  |  |
| --- | --- | --- |
|  | {Yn+1=Yn+(ζ2​|ρ​Zn+u^n|2+ζ​(1−ρ2)2​|Zn|2−a​(tn,π^n))​Δ​t+Zn​(B¯n+1−B¯n),Y~n+1=Y~n−a​(tn,π^n)​Δ​t+Z~n​(B¯n+1−B¯n).\left\{\begin{aligned} &Y\_{n+1}=Y\_{n}+\left(\frac{\zeta}{2}|\rho Z\_{n}+\hat{u}\_{n}|^{2}+\frac{\zeta(1-\rho^{2})}{2}|Z\_{n}|^{2}-a(t\_{n},\hat{\pi}\_{n})\right)\Delta t+Z\_{n}(\bar{B}\_{n+1}-\bar{B}\_{n}),\\ &\tilde{Y}\_{n+1}=\tilde{Y}\_{n}-a(t\_{n},\hat{\pi}\_{n})\Delta t+\tilde{Z}\_{n}(\bar{B}\_{n+1}-\bar{B}\_{n}).\end{aligned}\right. |  |

We adopt a similar neural network structure as above, introducing two additional parameters (Y~0,Z~0)(\tilde{Y}\_{0},\tilde{Z}\_{0}) to represent the initial values of the second BSDE. Moreover, the loss function is modified to 𝔼​[YT2+Y~T2]\mathbb{E}\left[Y\_{T}^{2}+\tilde{Y}\_{T}^{2}\right].

![Refer to caption](images/loss_curve.png)


Figure 1: The training loss function of an experiment with ρ=0\rho=0.

Note that each neural network has the same structure: one input layer, two hidden layers, and one output layer. Both the input and output layers are 1 dimensional, while each hidden layer has 11 dimensions. We adopt batch normalization immediately after each matrix multiplication and before applying the ReLU activation function. At each epoch, we use the Adam optimizer to update the parameters with mini-batches of 512512 samples.
Figure [1](https://arxiv.org/html/2511.05861v1#S6.F1 "Figure 1 ‣ 6 Numerical Examples ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") plots the mean of the loss function for the model with ρ=0\rho=0 in the experiment. It is observed that the average loss decreases to approximately 3×10−53\times 10^{-5} after 5,000 epochs.666Given the small variation range of the learned YtY\_{t} (see Figure [2](https://arxiv.org/html/2511.05861v1#S6.F2 "Figure 2 ‣ 6 Numerical Examples ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")), a sufficiently low loss is required for good relative accuracy. We employ a four-stage linear decay learning rate schedule to balance exploration and convergence:
(1) exploration: 8×10−4→5×10−48\times 10^{-4}\to 5\times 10^{-4};
(2) convergence: 5×10−4→2×10−45\times 10^{-4}\to 2\times 10^{-4};
(3) fine-tuning: 2×10−4→5×10−52\times 10^{-4}\to 5\times 10^{-5};
(4) terminal reinforcement: 5×10−5→1×10−55\times 10^{-5}\to 1\times 10^{-5}.

![Refer to caption](images/Y_strategy_X_trajectories.png)


Figure 2: A sample trajectory of YY, π^t\hat{\pi}\_{t} and XtX\_{t} with ρ=0\rho=0

Figure [2](https://arxiv.org/html/2511.05861v1#S6.F2 "Figure 2 ‣ 6 Numerical Examples ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") presents a sample trajectory of the learned solution YtY\_{t}, the associated equilibrium strategy π^t\hat{\pi}\_{t} and the factor process XtX\_{t}. It is observed that the sample path of YY exhibit an overall downward trend over time.
In our framework, the process YY satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ys\displaystyle Y\_{s} | =−1ζ​log⁡(e−ζ​Ys)=−1ζ​log⁡(𝔼s​[e−ζ​(RT−Rs)])\displaystyle=-\frac{1}{\zeta}\log(e^{-\zeta Y\_{s}})=-\frac{1}{\zeta}\log\left(\mathbb{E}\_{s}\left[e^{-\zeta(R\_{T}-R\_{s})}\right]\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−1ζ​log⁡(−𝔼s​[U​(RT−Rs)])=−1ζ​log⁡(𝔼s​[1ζ​U′​(RT−Rs)]).\displaystyle=-\frac{1}{\zeta}\log\left(-\mathbb{E}\_{s}\left[U(R\_{T}-R\_{s})\right]\right)=-\frac{1}{\zeta}\log\left(\mathbb{E}\_{s}\left[\frac{1}{\zeta}U^{\prime}(R\_{T}-R\_{s})\right]\right). |  |

Intuitively, 𝔼s​[U​(RT−Rs)]\mathbb{E}\_{s}\left[U(R\_{T}-R\_{s})\right] decreases as time evolves, leading to a decrease in YsY\_{s}. Therefore, 𝔼s​[U′​(RT−Rs)]\mathbb{E}\_{s}\left[U^{\prime}(R\_{T}-R\_{s})\right] increases as YsY\_{s} declines. As the investment horizon approaches, the expected marginal utility rises; consequently, the investor becomes more inclined to invest.
This also explains why the equilibrium strategy π^\hat{\pi} in the mean–variance problem in dai\_dynamic\_2021 remains constant when ρ=0\rho=0, regardless of the volatility of the factor XtX\_{t}, since the expected marginal utility is constant in that case.

![Refer to caption](images/compare_gamma_zeta.png)


Figure 3: Plots of the mean of the equilibrium strategy π^\hat{\pi} of 10001000 trajectories under different γ\gamma (left panel) and different ζ\zeta (right panel) with ρ=0\rho=0.

Figure [3](https://arxiv.org/html/2511.05861v1#S6.F3 "Figure 3 ‣ 6 Numerical Examples ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") plots the mean of the strategy π^\hat{\pi} using 10001000 trajectories under different values of γ\gamma and ζ\zeta. As illustrated, a higher γ\gamma corresponds to a smaller investment proportion π^\hat{\pi}, which is intuitively reasonable. This behavior reflects that a larger γ\gamma indicates the agent places a higher weight on the variance term, leading the investor to favor stability over high returns. Moreover, a higher ζ\zeta also leads to a smaller investment proportion π^\hat{\pi}, which is also intuitively reasonable as γ\gamma represents the constant risk aversion in the CARA utility function.

![Refer to caption](images/compare_variance_utility1000.png)


Figure 4: Comparison of conditional variance and conditional expected utility: our model with different γ\gamma vs. model without variance term

Figure [4](https://arxiv.org/html/2511.05861v1#S6.F4 "Figure 4 ‣ 6 Numerical Examples ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") compares the conditional variance and expected utility under the equilibrium strategy π^\hat{\pi} in our model with ρ=0\rho=0 and the corresponding strategy in the same market setting where the agent ignores the variance term. The optimal strategy in this case can be obtained by setting γ=0\gamma=0:

|  |  |  |
| --- | --- | --- |
|  | π=σ−1⋅θ​(Xt)2.\pi=\sigma^{-1}\cdot\frac{\theta(X\_{t})}{2}. |  |

We then simulate 1,000 trajectories of the log-return process under each strategy and compute the sample mean and variance of RT−RtR\_{T}-R\_{t} at any time t=n​Δ​tt=n\Delta t, n=0,1,2,…,Nn=0,1,2,\dots,N. It can be observed that, by incorporating the variance term in the tt-functional, our equilibrium strategy reduces the conditional variance at the cost of a very small decrease in conditional expected utility.

![Refer to caption](images/Conexpected_strategy_and_X_try.png)


Figure 5: The mean of π^t\hat{\pi}\_{t} and YtY\_{t} under trading constraint with different ρ\rho.

Figure [5](https://arxiv.org/html/2511.05861v1#S6.F5 "Figure 5 ‣ 6 Numerical Examples ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") illustrates the equilibrium strategies with trading constraints A=[−10000,10000]A=[-10000,10000] and negative correlations (ρ=−0.31,−0.62,−0.93\rho=-0.31,-0.62,-0.93) alongside the equilibrium strategy with ρ=0\rho=0. Although the differences in YtY\_{t} are small, there is a clear gap between the strategies. The constrained cases with negative ρ\rho exhibit higher investment levels. Furthermore, the investment decreases as the terminal time approaches, which is consistent with the results in dai\_dynamic\_2021.

| Time | Approximation (π^ρ\hat{\pi}^{\rho}) | Constraint (π^\hat{\pi}) | Relative Error (‰) |
| --- | --- | --- | --- |
| 0.0 | -0.959920 | -0.960158 | 0.248‰ |
| 0.5 | -0.968967 | -0.969083 | 0.121‰ |
| 1.0 | -0.977834 | -0.977824 | -0.010‰ |
| 1.5 | -0.990868 | -0.990840 | -0.028‰ |
| 2.0 | -1.000000 | -1.000000 | -0.000‰ |

Table 1: Comparison of Approximation and Constrained Equilibrium Strategies

Table [1](https://arxiv.org/html/2511.05861v1#S6.T1 "Table 1 ‣ 6 Numerical Examples ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets") compares the approximate Nash equilibrium strategy π^ρ\hat{\pi}^{\rho} with the equilibrium strategy π^\hat{\pi} under a trading constraint at five discrete time point (t=0.0, 0.5, 1.0, 1.5, 2.0)(t=0.0,\;0.5,\;1.0,\;1.5,\;2.0) with ρ=−0.31\rho=-0.31 and γ=1\gamma=1 fixed777In this case, since the loss from the variance term is relatively small, we use γ=1\gamma=1 instead of 0.10.1 to make the numerical results more intuitive. . The last column reports the relative errors in per mille (‰). The results show that the discrepancies between the two strategies are negligible, and the relative errors remain extremely small across all time points. Furthermore, as t→Tt\rightarrow T, the relative error exhibits a slightly decreasing trend. This indicates that the expected payoff generated by the approximate Nash equilibrium strategy closely matches that of the true constrained equilibrium.

Acknowledgements: Zongxia Liang is supported by the National Natural Science Foundation of China under grant no. 12271290. Sheng Wang acknowledges Professor Ka Chun Cheung and the financial supports as a postdoctoral fellow from Department of Statistics and Actuarial Science, School of Computing and Data Science, The University of
Hong Kong. Part of this work was completed in 2024, when Sheng Wang was a visiting student (research assistant) under the supervision of Professor Xiang Yu. He acknowledges the financial support under the Hong Kong Polytechnic University research grant under no. P0045654. Xiang Yu is supported by the Hong Kong RGC General Research Fund (GRF) under grant no. 15211524, the Hong Kong Polytechnic University research grant under no. P0045654 and the Research Centre for Quantitative Finance at the Hong Kong Polytechnic University under grant no. P0042708.

## Appendix A The Energy Inequality and the John-Nirenberg Inequality

For the reader’s convenience, we collect below the energy inequality and the John-Nirenberg inequality (see kazamaki\_continuous\_1994 and zhang\_backward\_2017).

###### Lemma A.1.

Assume that Z∈HBMOZ\in H\_{\textup{BMO}}. For each integer n≥1n\geq 1, it holds that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[(∫0TZs2​ds)n]≤n!​‖Z‖BMO2​n.\mathbb{E}\left[\left(\int\_{0}^{T}Z^{2}\_{s}\mathrm{d}s\right)^{n}\right]\leq n!\|Z\|\_{\textup{BMO}}^{2n}. |  |

Moreover, the conditional version of the energy inequality also holds that, for any stopping time τ\tau,

|  |  |  |
| --- | --- | --- |
|  | 𝔼τ​[(∫τTZs2​ds)n]≤n!​‖Z‖BMO2​n,a.s..\mathbb{E}\_{\tau}\left[\left(\int\_{\tau}^{T}Z^{2}\_{s}\mathrm{d}s\right)^{n}\right]\leq n!\|Z\|\_{\textup{BMO}}^{2n},\quad a.s.. |  |

If further ‖Z‖BMO<1\|Z\|\_{\textup{BMO}}<1, we have the John-Nirenberg inequality.

###### Lemma A.2.

If ‖Z‖BMO<1\|Z\|\_{\textup{BMO}}<1, for every stopping time τ\tau

|  |  |  |
| --- | --- | --- |
|  | 𝔼τ​[exp⁡(∫τTZs2​ds)]≤11−‖Z‖BMO2,a.s..\mathbb{E}\_{\tau}\left[\exp\left(\int\_{\tau}^{T}Z\_{s}^{2}\mathrm{d}s\right)\right]\leq\frac{1}{1-\|Z\|\_{\textup{BMO}}^{2}},\quad a.s.. |  |

## Appendix B Sufficient Conditions for the Existence of Solution to BSDEs

For the reader’s convenience, we present a sufficient condition in xing\_class\_2018 for the existence of a solution to the following BSDE system.

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Yt=−f​(t,Xt,Yt,Zt)​d​t+Zt​σ​(t,Xt)​d​Wt,YT=g​(XT),dY\_{t}=-f(t,X\_{t},Y\_{t},Z\_{t})\,dt+Z\_{t}\sigma(t,X\_{t})\,dW\_{t},\qquad Y\_{T}=g(X\_{T}), |  | (B.1) |

where f:[0,T]×ℝd×ℝN×ℝN×d→ℝN,g:ℝd→ℝNf:[0,T]\times\mathbb{R}^{d}\times\mathbb{R}^{N}\times\mathbb{R}^{N\times d}\to\mathbb{R}^{N},\;g:\mathbb{R}^{d}\to\mathbb{R}^{N} are Borel functions.
We first introduce two structural conditions on the generator ff that appear in the theorem.

###### Definition B.1 (A priori boundedness (AB) condition).

We say that a function

|  |  |  |
| --- | --- | --- |
|  | f:[0,T]×ℝd×ℝ×ℝN×d→ℝNf:[0,T]\times\mathbb{R}^{d}\times\mathbb{R}\times\mathbb{R}^{N\times d}\to\mathbb{R}^{N} |  |

satisfies the *condition AB* if there exist a deterministic function
l∈L1​([0,T])l\in L^{1}([0,T]) and a set of vectors a1,…,aK∈ℝNa\_{1},\dots,a\_{K}\in\mathbb{R}^{N}
positively spanning ℝN\mathbb{R}^{N}, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ak⊤​f​(t,x,y,z)≤l​(t)+12​|ak⊤​z|2,for all ​(t,x,y,z)​ and ​k=1,…,K.a\_{k}^{\top}f(t,x,y,z)\leq l(t)+\frac{1}{2}\lvert a\_{k}^{\top}z\rvert^{2},\qquad\text{for all }(t,x,y,z)\text{ and }k=1,\dots,K. |  | (B.2) |

We say that ff satisfies the *weak AB condition* (short as (w​A​B)(wAB)) if
there exist Borel functions

|  |  |  |
| --- | --- | --- |
|  | Lk:[0,T]×ℝd×ℝN×d→ℝd,k=1,…,K,L\_{k}:[0,T]\times\mathbb{R}^{d}\times\mathbb{R}^{N\times d}\to\mathbb{R}^{d},\quad k=1,\dots,K, |  |

such that |Lk​(t,x,z)|≤C​(1+|z|)\lvert L\_{k}(t,x,z)\rvert\leq C(1+\lvert z\rvert) for some constant CC, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ak⊤​f​(t,x,y,z)≤l​(t)+12​|ak⊤​z|2+ak⊤​z​Lk​(t,x,z),for all ​(t,x,y,z)​ and ​k=1,…,K.a\_{k}^{\top}f(t,x,y,z)\leq l(t)+\frac{1}{2}\lvert a\_{k}^{\top}z\rvert^{2}+a\_{k}^{\top}z\,L\_{k}(t,x,z),\qquad\text{for all }(t,x,y,z)\text{ and }k=1,\dots,K. |  | (B.3) |

###### Remark B.2.

A set of nonzero vectors
a1,…,aKa\_{1},\dots,a\_{K} in ℝN\mathbb{R}^{N} (with K>NK>N) is said to positively span
ℝN\mathbb{R}^{N} if, for each a∈ℝNa\in\mathbb{R}^{N}, there exist nonnegative constants
λ1,…,λK\lambda\_{1},\dots,\lambda\_{K} such that

|  |  |  |
| --- | --- | --- |
|  | λ1​a1+⋯+λK​aK=a.\lambda\_{1}a\_{1}+\cdots+\lambda\_{K}a\_{K}=a. |  |

###### Definition B.3 (The Bensoussan–Frehse (BF) condition).

We say that a continuous function

|  |  |  |
| --- | --- | --- |
|  | f:[0,T]×ℝd×ℝN×ℝN×d→ℝNf:[0,T]\times\mathbb{R}^{d}\times\mathbb{R}^{N}\times\mathbb{R}^{N\times d}\to\mathbb{R}^{N} |  |

satisfies the *BF* condition if it admits a decomposition of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(t,x,y,z)=diag​(z​l​(t,x,y,z))+q​(t,x,y,z)+s​(t,x,y,z)+k​(t,x),f(t,x,y,z)=\mathrm{diag}(z\,l(t,x,y,z))+q(t,x,y,z)+s(t,x,y,z)+k(t,x), |  | (B.4) |

such that the functions

|  |  |  |
| --- | --- | --- |
|  | l:[0,T]×ℝd×ℝN×ℝN×d→ℝd×Nandq,s,k:[0,T]×ℝd×ℝN×ℝN×d→ℝNl:[0,T]\times\mathbb{R}^{d}\times\mathbb{R}^{N}\times\mathbb{R}^{N\times d}\to\mathbb{R}^{d\times N}\quad\text{and}\quad q,s,k:[0,T]\times\mathbb{R}^{d}\times\mathbb{R}^{N}\times\mathbb{R}^{N\times d}\to\mathbb{R}^{N} |  |

fulfill the following conditions: there exist b0∈ℝdb\_{0}\in\mathbb{R}^{d} and two sequences {Cn}\{C\_{n}\} and {qn}\{q\_{n}\} of positive constants with qn>1+d/2q\_{n}>1+d/2, and a sequence {κn}\{\kappa\_{n}\} of functions

|  |  |  |
| --- | --- | --- |
|  | κn:[0,∞)→[0,∞),limw→∞κn​(w)w2=0,\kappa\_{n}:[0,\infty)\to[0,\infty),\qquad\lim\_{w\to\infty}\frac{\kappa\_{n}(w)}{w^{2}}=0, |  |

such that for each n∈ℕn\in\mathbb{N} and any (t,x,y,z)∈[0,T]×Bn​(b0)×ℝN×ℝN×d(t,x,y,z)\in[0,T]\times B\_{n}(b\_{0})\times\mathbb{R}^{N}\times\mathbb{R}^{N\times d}, we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |l​(t,x,y,z)|\displaystyle|l(t,x,y,z)| | ≤Cn​(1+|z|),\displaystyle\leq C\_{n}(1+|z|), | (quadratic-linear) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |qi​(t,x,y,z)|\displaystyle|q^{i}(t,x,y,z)| | ≤Cn​(1+∑j=1i|zj|2),\displaystyle\leq C\_{n}\left(1+\sum\_{j=1}^{i}|z^{j}|^{2}\right), | i=1,…,N,(quadratic-triangular)\displaystyle i=1,\dots,N,\qquad\textnormal{(quadratic-triangular)} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |s​(t,x,y,z)|\displaystyle|s(t,x,y,z)| | ≤κn​(|z|),\displaystyle\leq\kappa\_{n}(|z|), | (subquadratic) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | k\displaystyle k | ∈Lqn​([0,T]×Bn),\displaystyle\in L^{q\_{n}}([0,T]\times B\_{n}), | (z-independent).\displaystyle\textnormal{(z-independent)}. |  |

In this case, we write f∈BF​({Cn},{κn},{qn})f\in\mathrm{BF}(\{C\_{n}\},\{\kappa\_{n}\},\{q\_{n}\}).

###### Theorem B.4 (Existence under BF + AB conditions).

Suppose that ff satisfies BF and AB conditions,
and that g∈Cloc,b0{αn}g\in C^{\{\alpha\_{n}\}}\_{\mathrm{loc},b\_{0}} for some b0b\_{0} and it satisfies lim|x|→∞|g​(x)||x|2=0\lim\_{|x|\to\infty}\frac{|g(x)|}{|x|^{2}}=0. Then the system ([B.1](https://arxiv.org/html/2511.05861v1#A2.E1 "In Appendix B Sufficient Conditions for the Existence of Solution to BSDEs ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) admits a locally Hölderian solution (v,w)(v,w),
that is, v∈Cloc,b0{αn′}v\in C^{\{\alpha\_{n}^{\prime}\}}\_{\mathrm{loc},b\_{0}} for some sequence
{αn′}\{\alpha\_{n}^{\prime}\} in (0,1](0,1]. When gg is bounded, the AB condition
can be replaced by wAB condition and (v,w)(v,w) is a bounded
bmo-solution.

## Appendix C The Challenge of our BSDE System when ρ≠0\rho\neq 0

For the general case ρ≠0\rho\neq 0, we encounter a system of coupled two-dimensional quadratic BSDEs. Existing results for the existence of solution to the multidimensional BSDEs bifurcate into two paradigms: fixed-point arguments via contraction mappings (yielding the unique solution) (see FAN2023105, Luo\_2017 and HU20161066) and construction of uniformly convergent approximants through coefficient regularization (see xing\_class\_2018, Jackson\_2022 and JACKSON2023). In this section, we explain that these two methods are not applicable in our setting.

For our coupled BSDE system in ([4.2](https://arxiv.org/html/2511.05861v1#S4.E2 "In 4 Study of BSDE System in the Incomplete Factor Model ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")), we can compute the quadratic term of the drift −f1=(ζ2​|ρ​Z+u^|2+ζ​(1−ρ2)2​|Z|2−a​(t,π^))-f\_{1}=\left(\frac{\zeta}{2}|\rho Z+\hat{u}|^{2}+\frac{\zeta(1-\rho^{2})}{2}|Z|^{2}-a(t,\hat{\pi})\right) w.r.t zz and z~\tilde{z} as

|  |  |  |
| --- | --- | --- |
|  | ζ2​z2−ρ​ζ​z⋅ζ​e−ζ​y​ρ​z+γ​ρ​z~(ζ+1)​e−ζ​y+γ+ζ+12​(ζ​e−ζ​y​ρ​z+γ​ρ​z~(ζ+1)​e−ζ​y+γ)2\displaystyle\frac{\zeta}{2}z^{2}-\rho\zeta z\cdot\frac{\zeta e^{-\zeta y}\rho z+\gamma\rho\tilde{z}}{(\zeta+1)e^{-\zeta y}+\gamma}+\frac{\zeta+1}{2}\left(\frac{\zeta e^{-\zeta y}\rho z+\gamma\rho\tilde{z}}{(\zeta+1)e^{-\zeta y}+\gamma}\right)^{2} |  |

and the quadratic term of −f2=−a​(t,π^)-f\_{2}=-a(t,\hat{\pi}) w.r.t. zz and z~\tilde{z} as

|  |  |  |
| --- | --- | --- |
|  | 12​(ζ​e−ζ​y​ρ​z+γ​ρ​z~(ζ+1)​e−ζ​y+γ)2.\displaystyle\frac{1}{2}\left(\frac{\zeta e^{-\zeta y}\rho z+\gamma\rho\tilde{z}}{(\zeta+1)e^{-\zeta y}+\gamma}\right)^{2}. |  |

The first approach typically requires a continuity condition on yy to guarantee a contraction mapping that

|  |  |  |
| --- | --- | --- |
|  | |fi​(t,x,y1,z,z~)−fi​(t,x,y2,z,z~)|≤C​ϕ​(y1∨y2)​(1+‖(z,z~)‖)​|y1−y2|,i=1,2.|f\_{i}(t,x,y\_{1},z,\tilde{z})-f\_{i}(t,x,y\_{2},z,\tilde{z})|\leq C\phi\left(y\_{1}\vee y\_{2}\right)\left(1+||(z,\tilde{z})||\right)|y\_{1}-y\_{2}|,\quad i=1,2. |  |

which is not satisfied in our case as yy is coupled with the quadratic term of z,z~z,\tilde{z}.

The second approach relies on the AB condition or the wAB condition (see Appendix [B](https://arxiv.org/html/2511.05861v1#A2 "Appendix B Sufficient Conditions for the Existence of Solution to BSDEs ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) for the convergence of a subsequence of approximated solutions to the approximated BSDE system. Specifically, there exist a deterministic function l∈L1​[0,T]l\in L^{1}[0,T] and a1​⋯​aka\_{1}\cdots a\_{k} that positively span ℝN\mathbb{R}^{N} such that

|  |  |  |
| --- | --- | --- |
|  | ak⊤​f​(t,x,y,z)≤l​(t)+12​|ak⊤​z|2+ak⊤​z​Lk​(t,x,z).a\_{k}^{\top}f(t,x,y,z)\leq l(t)+\frac{1}{2}|a\_{k}^{\top}z|^{2}+a\_{k}^{\top}z\,L\_{k}(t,x,z). |  |

In our case, there exists two vectors (−a,b),(c,−d)(-a,b),\;(c,-d) with a>0,d>0a>0,\;d>0 and deterministic functions l1,l2∈L1​[0,T]l\_{1},l\_{2}\in L^{1}[0,T] such that, for any (t,x,y,z,z~)(t,x,y,z,\tilde{z}),

|  |  |  |
| --- | --- | --- |
|  | −a​f1+b​f2≤l1​(t)+12​|−a​z+b​z~|2+(−a​z+b​z~)​L2​(t,x,z,z~),-af\_{1}+bf\_{2}\leq l\_{1}(t)+\frac{1}{2}|-az+b\tilde{z}|^{2}+(-az+b\tilde{z})L\_{2}(t,x,z,\tilde{z}), |  |

|  |  |  |
| --- | --- | --- |
|  | c​f1−d​f2≤l2​(t)+12​|−a​z+b​z~|2+(−a​z+b​z~)​L2​(t,x,z,z~).cf\_{1}-df\_{2}\leq l\_{2}(t)+\frac{1}{2}|-az+b\tilde{z}|^{2}+(-az+b\tilde{z})L\_{2}(t,x,z,\tilde{z}). |  |

Here, Li​(t,x,z,z~)≤C​(1+|z|+|z~|),i=1,2L\_{i}(t,x,z,\tilde{z})\leq C(1+|z|+|\tilde{z}|),\;i=1,2 for a constant CC.

If b=0​(c=0)b=0\;(c=0), the inequality fails to hold as z~​(z)→∞\tilde{z}\;(z)\rightarrow\infty and z​(z~)=0z\;(\tilde{z})=0.
Now we assume that b≠0,d≠0b\neq 0,\;d\neq 0 and select zz and z~\tilde{z} such that a​z=b​z~​(c​z=d​z~)az=b\tilde{z}\;(cz=d\tilde{z}). We focus on the quadratic terms in zz and z~\tilde{z}, because if there exist zz and z~\tilde{z} such that the quadratic term is positive, then by scaling zz and z~\tilde{z} proportionally, the inequality is violated. Moreover, we assume that a=d=1a=d=1 without loss of generality. Let y→∞y\rightarrow\infty and y→−∞y\rightarrow-\infty, it holds that

|  |  |  |
| --- | --- | --- |
|  | ζ​e−ζ​y​ρ​z+γ​ρ​z~(ζ+1)​e−ζ​y+γ⟶ρ​z~,ζ​e−ζ​y​ρ​z+γ​ρ​z~(ζ+1)​e−ζ​y+γ⟶ζ​ρ​zζ+1.\frac{\zeta e^{-\zeta y}\rho z+\gamma\rho\tilde{z}}{(\zeta+1)e^{-\zeta y}+\gamma}\longrightarrow\rho\tilde{z},\quad\frac{\zeta e^{-\zeta y}\rho z+\gamma\rho\tilde{z}}{(\zeta+1)e^{-\zeta y}+\gamma}\longrightarrow\frac{\zeta\rho z}{\zeta+1}. |  |

Substituting it into wAB condition, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ζ2b2+−(ρ2ζ+ρ22)b+ζ+12ρ2≤0,(ζ2−ζ2​ρ22​(ζ+1))b2−ρ2​ζ22​(ζ+1)2b3≤0.\displaystyle\frac{\zeta}{2}b^{2}+-\left(\rho^{2}\zeta+\frac{\rho^{2}}{2}\right)b+\frac{\zeta+1}{2}\rho^{2}\leq 0,\quad\left(\frac{\zeta}{2}-\frac{\zeta^{2}\rho^{2}}{2(\zeta+1)}\right)b^{2}-\frac{\rho^{2}\zeta^{2}}{2(\zeta+1)^{2}}b^{3}\leq 0. |  | (C.1) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | 12​ρ2​c2−c​(ζ2−ρ2​ζ​c+ζ+12​ρ2​c2)≤0,ζ2​ρ22​(ζ+1)2−c​(ζ2−ζ2​ρ22​(ζ+1))≤0.\displaystyle\frac{1}{2}\rho^{2}c^{2}-c\left(\frac{\zeta}{2}-\rho^{2}\zeta c+\frac{\zeta+1}{2}\rho^{2}c^{2}\right)\leq 0,\quad\frac{\zeta^{2}\rho^{2}}{2(\zeta+1)^{2}}-c\left(\frac{\zeta}{2}-\frac{\zeta^{2}\rho^{2}}{2(\zeta+1)}\right)\leq 0. |  | (C.2) |

It then follows from ([C.1](https://arxiv.org/html/2511.05861v1#A3.E1 "In Appendix C The Challenge of our BSDE System when 𝜌≠0 ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")) that

|  |  |  |
| --- | --- | --- |
|  | ρ4​(ζ+12)2−ζ​(ζ+1)≥0,ζ+1ζ≤(ζ+1)2ρ​ζ−(ζ+1)≤b≤ρ2​ζ+ρ22+ρ4​(ζ+12)2−ζ​(ζ+1)ζ≤ζ+1ζ,\rho^{4}(\zeta+\frac{1}{2})^{2}-\zeta(\zeta+1)\geq 0,\quad\frac{\zeta+1}{\zeta}\leq\frac{(\zeta+1)^{2}}{\rho\zeta}-(\zeta+1)\leq b\leq\frac{\rho^{2}\zeta+\frac{\rho^{2}}{2}+\sqrt{\rho^{4}(\zeta+\frac{1}{2})^{2}-\zeta(\zeta+1)}}{\zeta}\leq\frac{\zeta+1}{\zeta}, |  |

which result in ρ=1\rho=1 and b=ζ+1ζ>0b=\frac{\zeta+1}{\zeta}>0. Substituting ρ=1\rho=1 into ([C.2](https://arxiv.org/html/2511.05861v1#A3.E2 "In Appendix C The Challenge of our BSDE System when 𝜌≠0 ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")), we get that c>0c>0 by ([C.1](https://arxiv.org/html/2511.05861v1#A3.E1 "In Appendix C The Challenge of our BSDE System when 𝜌≠0 ‣ Equilibrium Portfolio Selection under Utility-Variance Analysis of Log Returns in Incomplete Markets")). Consequently, we have

|  |  |  |
| --- | --- | --- |
|  | ζ+12​c2−(ζ+12)​c+ζ2≥0,c≥ζζ+1,\frac{\zeta+1}{2}c^{2}-\left(\zeta+\frac{1}{2}\right)c+\frac{\zeta}{2}\geq 0,\quad c\geq\frac{\zeta}{\zeta+1}, |  |

which then imply c≥1c\geq 1.

As we have shown that, for any ai=(m,n)∈{a1,⋯,ak}a\_{i}=(m,n)\in\{a\_{1},\cdots,a\_{k}\} chosen in wAB condition, mm and nn must satisfy one of the three conditions

1. 1.

   m≥0m\geq 0, n≥0n\geq 0.
2. 2.

   m<0m<0, n=−ζ+1ζ​mn=-\frac{\zeta+1}{\zeta}m.
3. 3.

   n<0n<0, m≥nm\geq n.

Each of the three cases implies that (m,n)⋅(−1,−1)≤0(m,n)\cdot(-1,-1)\leq 0, as a consequence, {a1,⋯,ak}\{a\_{1},\cdots,a\_{k}\} cannot positively span ℝ2\mathbb{R}^{2}. Then neither AB condition nor wAB condition holds in our problem.