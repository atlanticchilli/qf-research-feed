---
authors:
- Criscent Birungi
- Cody Hyndman
doc_id: arxiv:2510.10371v1
family_id: arxiv:2510.10371
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Optimal annuitization with labor income under age-dependent force of mortality
url_abs: http://arxiv.org/abs/2510.10371v1
url_html: https://arxiv.org/html/2510.10371v1
venue: arXiv q-fin
version: 1
year: 2025
---


Criscent Birungi
Department of Mathematics and Statistics
  
Concordia University
  
Montréal, QC, Canada

Cody Hyndman
Corresponding author. Emails:
[criscent.birungi@concordia.ca](mailto:criscent.birungi@concordia.ca),
[cody.hyndman@concordia.ca](mailto:cody.hyndman@concordia.ca)
Department of Mathematics and Statistics
  
Concordia University
  
Montréal, QC, Canada

(October 10, 2025)

###### Abstract

We consider the problem of optimal annuitization with labour income, where an agent aims to maximize utility from consumption and labour income under age-dependent force of mortality. Using a dynamic programming approach, we derive closed-form solutions for the value function and the optimal consumption, portfolio, and labor supply strategies. Our results show that before retirement, investment behavior increases with wealth until a threshold set by labor supply. After retirement, agents tend to consume a larger portion of their wealth. Two main factors influence optimal annuitization decisions as people get older. First, the agent’s perspective (demand side); the agent’s personal discount rate rises with age, reducing their desire to annuitize. Second, the insurer’s perspective (supply side); insurers offer higher payout rates (mortality credits). Our model demonstrates that beyond a certain age, sharply declining survival probabilities make annuitization substantially optimal, as the powerful incentive of mortality credits outweighs the agent’s high personal discount rate. Finally, post-retirement labor income serves as a direct substitute for annuitization by providing an alternative stable income source. It enhances the financial security of retirees.

Keywords: Stochastic control; Optimal annuitization; Labor income; Optimal stopping; Force of mortality; Dynamic programming

## 1 Introduction

An annuity is a contract that gives buyers a guaranteed, regular income. Annuitization converts a lump sum into regular income and is a critical financial decision, particularly for retirees. As Buttarazzi et al. ([2025](https://arxiv.org/html/2510.10371v1#bib.bib5)) notes, this is a retirement decision where individuals trade investment growth for long-term stability and guaranteed income for life. This decision is increasingly complex due to rising longevity risk, a demographic shift evidenced by growing labor force participation among older age groups Gao et al. ([2022](https://arxiv.org/html/2510.10371v1#bib.bib12)). For instance, the Bureau of Labor Statistics projects that by 2033, the labor participation rate will exceed 10%10\% for those aged 75 and older and surpass 30%30\% for those aged 65. Many factors, such as labor income, contribute to post-retirement welfare, or bridge employment, which transforms conventional retirement planning (see Klotz et al., [2021](https://arxiv.org/html/2510.10371v1#bib.bib19); Lorenz and Zwick, [2021](https://arxiv.org/html/2510.10371v1#bib.bib24); Buttarazzi et al., [2025](https://arxiv.org/html/2510.10371v1#bib.bib5)). The primary challenge is to determine how an agent can maximize lifetime utility from consumption and labor income, given age-dependent mortality risk, while managing wealth optimally.

This study addresses the agent’s optimization problem within the framework of stochastic optimal control. The evolution of the agent’s wealth is described by a stochastic differential equation (SDE) influenced by their strategic choices in investment (π\pi), consumption (cc), and labor (bb). We employ the dynamic programming approach, specifically the Hamilton-Jacobi-Bellman (HJB) methodology, to solve this problem.
This approach, developed in the seminal works of Merton ([1969](https://arxiv.org/html/2510.10371v1#bib.bib25), [1975](https://arxiv.org/html/2510.10371v1#bib.bib26)) and Karatzas et al. ([1986](https://arxiv.org/html/2510.10371v1#bib.bib18)), constitutes a central methodology for addressing such problems, complementing alternative frameworks such as the duality and martingale methods. Foundational contributions to the theory of duality were made by Bismut ([1973](https://arxiv.org/html/2510.10371v1#bib.bib4)), while the comprehensive monograph by Rockafellar and Wets ([1998](https://arxiv.org/html/2510.10371v1#bib.bib29)) provides the authoritative modern treatment of optimization and duality theory. This work substantially extends the classical duality framework introduced in Rockafellar ([1970](https://arxiv.org/html/2510.10371v1#bib.bib28)), generalizing it to encompass nonconvex and nonsmooth settings. Subsequent applications of these ideas include, among others, Karatzas and Wang ([2000](https://arxiv.org/html/2510.10371v1#bib.bib17)), Gerrard et al. ([2012](https://arxiv.org/html/2510.10371v1#bib.bib13)), and Gao et al. ([2022](https://arxiv.org/html/2510.10371v1#bib.bib12)).

Our work builds on a rich literature exploring optimal consumption, leisure, and investment choices under various utility functions and constraints (see Cvitanić and Karatzas, [1992](https://arxiv.org/html/2510.10371v1#bib.bib10); Choi and Shim, [2006](https://arxiv.org/html/2510.10371v1#bib.bib7); Labbé and Heunis, [2007](https://arxiv.org/html/2510.10371v1#bib.bib21); Choi et al., [2008](https://arxiv.org/html/2510.10371v1#bib.bib8); Barucci and Marazzina, [2012](https://arxiv.org/html/2510.10371v1#bib.bib2); Koo et al., [2013](https://arxiv.org/html/2510.10371v1#bib.bib20); Lee and Shin, [2015](https://arxiv.org/html/2510.10371v1#bib.bib22); Heunis, [2015a](https://arxiv.org/html/2510.10371v1#bib.bib14), [b](https://arxiv.org/html/2510.10371v1#bib.bib15); Peng and Li, [2023](https://arxiv.org/html/2510.10371v1#bib.bib27); Ferrari and Zhu, [2023](https://arxiv.org/html/2510.10371v1#bib.bib11)). A significant portion of the existing literature on optimal annuitization, including the works of Lim et al. ([2008](https://arxiv.org/html/2510.10371v1#bib.bib23)), Gerrard et al. ([2012](https://arxiv.org/html/2510.10371v1#bib.bib13)), and Gao et al. ([2022](https://arxiv.org/html/2510.10371v1#bib.bib12)), simplifies the problem by assuming a constant mortality rate. This assumption implies that the agent’s lifetime follows an exponential distribution with a constant mortality rate, which is far from realistic. By relaxing the constant mortality assumption, we extend the model of Gao et al. ([2022](https://arxiv.org/html/2510.10371v1#bib.bib12)). Our objective is to incorporate a more realistic age-dependent force of mortality into the agent’s utility maximization problem. Consequently, we proceed with a different objective function and approach to solve the problem. We adapt the dynamic programming framework from Koo et al. ([2013](https://arxiv.org/html/2510.10371v1#bib.bib20)), providing rigorous proofs to derive closed-form solutions for the value function and the corresponding optimal consumption, labor, and portfolio allocation strategies. This approach avoids the guesswork often associated with developing auxiliary market models. Ultimately, we provide and implement results that have direct practical applications for retirement planning in an era of increasing longevity.

The rest of this paper is structured as follows. Section [2](https://arxiv.org/html/2510.10371v1#S2 "2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality") discusses the market model, including the economic background, mathematical formulations, and the stochastic optimal control problems. We propose methods for determining optimality and provide rigorous proofs to derive closed-form solutions for the value function associated with the optimal annuitization problem with labor income under an age-dependent force of mortality. Additionally, we present the main theoretical results for the optimal consumption, labor, and portfolio allocation strategies. Section [3](https://arxiv.org/html/2510.10371v1#S3 "3 Results and Discussion ‣ Optimal annuitization with labor income under age-dependent force of mortality") presents numerical implementation results and key findings of our study. Finally, Section [4](https://arxiv.org/html/2510.10371v1#S4 "4 Conclusion ‣ Optimal annuitization with labor income under age-dependent force of mortality") presents conclusions and recommendations for future research, and potential directions for further work.

## 2 The Market Model

Consider a financial market consisting of two assets: a risk-free asset St0S\_{t}^{0}, evolving as

|  |  |  |
| --- | --- | --- |
|  | d​St0=r​St0​d​t,dS\_{t}^{0}=rS\_{t}^{0}\,dt, |  |

where rr is the constant risk-free rate, and a risky asset St1S\_{t}^{1}, following

|  |  |  |
| --- | --- | --- |
|  | d​St1=μ​St1​d​t+σ​St1​d​Wt,dS\_{t}^{1}=\mu S\_{t}^{1}\,dt+\sigma S\_{t}^{1}\,dW\_{t}, |  |

where μ\mu is the expected return, σ\sigma is the volatility, and WtW\_{t} is a standard Brownian motion. The agent’s wealth XtX\_{t} is allocated between these two assets. Let
ϕt0\phi\_{t}^{0} be the units held in the risk-free asset,
and ϕt1\phi\_{t}^{1} and units held of the risky asset.
Then, the portfolio value, or total wealth, is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt=ϕt0​St0+ϕt1​St1.X\_{t}=\phi\_{t}^{0}S\_{t}^{0}+\phi\_{t}^{1}S\_{t}^{1}. |  | (2.1) |

We assume the portfolio is self-financing, that is

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=ϕt0​d​St0+ϕt1​d​St1.dX\_{t}=\phi\_{t}^{0}dS\_{t}^{0}+\phi\_{t}^{1}dS\_{t}^{1}. |  | (2.2) |

Substituting the dynamics of St0S\_{t}^{0} and St1S\_{t}^{1} into ([2.2](https://arxiv.org/html/2510.10371v1#S2.E2 "Equation 2.2 ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=r​ϕt0​St0​d​t+μ​ϕt1​St1​d​t+σ​ϕt1​St1​d​Wt.dX\_{t}=r\phi\_{t}^{0}S\_{t}^{0}\,dt+\mu\phi\_{t}^{1}S\_{t}^{1}\,dt+\sigma\phi\_{t}^{1}S\_{t}^{1}\,dW\_{t}. |  | (2.3) |

Let πt=ϕt1​St1\pi\_{t}=\phi\_{t}^{1}S\_{t}^{1} denote the amount invested in the risky asset. From ([2.1](https://arxiv.org/html/2510.10371v1#S2.E1 "Equation 2.1 ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")), we have ϕt0​St0=Xt−πt\phi\_{t}^{0}S\_{t}^{0}=X\_{t}-\pi\_{t}. Substituting these into ([2.3](https://arxiv.org/html/2510.10371v1#S2.E3 "Equation 2.3 ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt\displaystyle dX\_{t} | =r​(Xt−πt)​d​t+μ​πt​d​t+σ​πt​d​Wt\displaystyle=r(X\_{t}-\pi\_{t})\,dt+\mu\pi\_{t}\,dt+\sigma\pi\_{t}\,dW\_{t} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =[r​Xt+πt​(μ−r)]​d​t+σ​πt​d​Wt.\displaystyle=\left[rX\_{t}+\pi\_{t}(\mu-r)\right]dt+\sigma\pi\_{t}\,dW\_{t}. |  | (2.4) |

The agent’s strategic decisions are represented by the control processes for consumption, ctc\_{t}, portfolio allocation, πt\pi\_{t}, and labor, btb\_{t}. The agent is endowed with a total time L¯\overline{L}, which is allocated between labor btb\_{t} and leisure ltl\_{t}, such that bt=L¯−ltb\_{t}=\overline{L}-l\_{t}. We define τ\tau as the voluntary retirement time, which is treated as an optimal stopping time. The agent’s choice of leisure is therefore constrained as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | lt={lt∈[0,L]for ​0≤t<τ(pre-retirement)L¯for ​t≥τ(post-retirement)l\_{t}=\begin{cases}l\_{t}\in[0,L]&\text{for }0\leq t<\tau\quad\text{(pre-retirement)}\\ \overline{L}&\text{for }t\geq\tau\quad\text{(post-retirement)}\end{cases} |  | (2.5) |

where 0≤L<L¯0\leq L<\overline{L} are constants, following the framework of Choi et al. ([2008](https://arxiv.org/html/2510.10371v1#bib.bib8)) and Koo et al. ([2013](https://arxiv.org/html/2510.10371v1#bib.bib20)). This specification implies that labor btb\_{t} can be positive only before retirement (t<τt<\tau), and labor income ceases thereafter.

Incorporating these extensions into the wealth equation ([2](https://arxiv.org/html/2510.10371v1#S2.Ex3 "2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")), then the agent’s wealth, XtX\_{t}, evolves according to the following stochastic differential equation (SDE)

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=[r​Xt+πt​(μ−r)−ct+w​bt]​d​t+σ​πt​d​Wt,dX\_{t}=\left[rX\_{t}+\pi\_{t}(\mu-r)-c\_{t}+wb\_{t}\right]dt+\sigma\pi\_{t}\,dW\_{t}, |  | (2.6) |

subject to the standard non-negativity constraint on consumption, ct≥0c\_{t}\geq 0. The model parameters are defined as: ww: the constant wage rate. The market price of risk is denoted by θ:=μ−rσ\theta:=\frac{\mu-r}{\sigma}.

Given the probability space (Ω,ℱ,P)(\Omega,\mathcal{F},P), as in Lee and Shin ([2015](https://arxiv.org/html/2510.10371v1#bib.bib22)), we assume the processes πt\pi\_{t}, ctc\_{t}, and btb\_{t} are all ℱt\mathcal{F}\_{t}-progressively measurable and satisfy the following technical conditions

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0tπs2​𝑑s<∞,∫0tcs​𝑑s<∞,and∫0tbs​𝑑s<∞for all ​t≥0​ a.s.\int\_{0}^{t}\pi\_{s}^{2}\,ds<\infty,\quad\int\_{0}^{t}c\_{s}\,ds<\infty,\quad\text{and}\quad\int\_{0}^{t}b\_{s}\,ds<\infty\quad\text{for all }t\geq 0\text{ a.s.} |  | (2.7) |

Accordingly, admissible control input πt\pi\_{t} to the dynamical system ([2.6](https://arxiv.org/html/2510.10371v1#S2.E6 "Equation 2.6 ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")) are always restricted to the real vector space

|  |  |  |  |
| --- | --- | --- | --- |
|  | Π:={π:[0,T]×Ω→ℝN|π is ℱt-prog. meas. and ∫0T∥πt∥2dt<∞, a.s.}.\Pi:=\left\{\pi:[0,T]\times\Omega\to\mathbb{R}^{N}\,\middle|\,\pi\text{ is }\mathcal{F}\_{t}\text{-prog. meas. and }\int\_{0}^{T}\|\pi\_{t}\|^{2}\,dt<\infty,\text{ a.s.}\right\}. |  | (2.8) |

The wealth process X(π,c,b)X^{(\pi,c,b)} can be regarded as a stochastic dynamical system with the control input (π,c,b)(\pi,c,b), where π∈Π\pi\in\Pi. To ensure that X(π,c,b)X^{(\pi,c,b)} is well-defined, the consumption process cc must belong to the set

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞:={c:[0,T]×Ω→[0,∞)|c is ℱt-prog. meas. and ∫0Tctdt<∞ a.s.}.\mathcal{C}:=\left\{c:[0,T]\times\Omega\to[0,\infty)\;\middle|\;c\text{ is }\mathcal{F}\_{t}\text{-prog. meas. and }\int\_{0}^{T}c\_{t}\,dt<\infty\text{ a.s.}\right\}. |  | (2.9) |

Define ℬ\mathcal{B}, the set of admissible l​a​b​o​rlabor-processes defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℬ:={b:[0,T]×Ω→[0,∞)|b is ℱt-prog. meas. and ∫0Tbtdt<∞ a.s.}.\mathcal{B}:=\left\{b:[0,T]\times\Omega\to[0,\infty)\;\middle|\;b\text{ is }\mathcal{F}\_{t}\text{-prog. meas. and }\int\_{0}^{T}b\_{t}\,dt<\infty\text{ a.s.}\right\}. |  | (2.10) |

Additionally, the wealth process X(π,c,b)X^{(\pi,c,b)} must not take negative values during the control interval [0,T][0,T]. This ensures that the retiree cannot consume excessively, thereby avoiding negative wealth. A useful way to model these constraints is through a stipulated closed convex set K⊂ℝNK\subset\mathbb{R}^{N}. The set of admissible control strategies is defined by the conditions detailed in the following remark.

###### Remark 2.1 (Admissibility Conditions).

For the optimization problem to be well-posed, we impose the following conditions on the control variables and the resulting wealth process.

1. 1.

   Control Set Constraints:
   The control variables π​(t,ω)\pi(t,\omega) and b​(t,ω)b(t,\omega) must belong to their respective admissible sets KK and KbK\_{b} for almost every (t,ω)∈[0,T]×Ω(t,\omega)\in[0,T]\times\Omega. The set Kb⊂ℝNK\_{b}\subset\mathbb{R}^{N} is a closed convex set that constrains the labor choice btb\_{t}.
2. 2.

   Stopping Time:
   The retirement time τ\tau must be an {ℱt}\{\mathcal{F}\_{t}\}-stopping time. This ensures that the decision to retire at time τ\tau depends only on information available up to that point, preventing any reliance on future knowledge.
3. 3.

   Finite Horizon:
   The stopping time τ\tau must occur on or before the terminal time TT almost surely. That is, τ≤T,ℙ−a.s.\tau\leq T,\quad\mathbb{P}-\text{a.s.}. This assumption imposes a finite time horizon on the control process.
4. 4.

   Wealth Admissibility:
   A control tuple (π,c,b,τ)(\pi,c,b,\tau) is admissible if, for an initial wealth X0>−w​b¯rX\_{0}>-\frac{w\overline{b}}{r}, where w​b¯r\frac{w\overline{b}}{r} represents the present value of the agent’s future labor income and the corresponding wealth process Xt(π,c,b)X\_{t}^{(\pi,c,b)} remains strictly greater than this lower bound for all t∈[0,τ]t\in[0,\tau]. This is the minimum wealth or solvency threshold from which the agent’s first behavior regime starts. It represents the amount that can be made up with labor income only and prevents the agent’s wealth from falling below this threshold. The agent may consume and invest as long as initial wealth X0>−w​b¯rX\_{0}>-\frac{w\overline{b}}{r}.

The set of admissible strategies, denoted by 𝒜\mathcal{A}, consists of all control tuples (π,c,b,τ)(\pi,c,b,\tau) that satisfy the conditions outlined in Remark ([2.1](https://arxiv.org/html/2510.10371v1#S2.Thmremark1 "Remark 2.1 (Admissibility Conditions). ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")). We can formally define this set as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜:={(π,c,b,τ)∈Π×𝒞×ℬ×𝒯∣Conditions ([1](https://arxiv.org/html/2510.10371v1#S2.I1.i1 "Item 1 ‣ Remark 2.1 (Admissibility Conditions). ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality"))-([4](https://arxiv.org/html/2510.10371v1#S2.I1.i4 "Item 4 ‣ Remark 2.1 (Admissibility Conditions). ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")) are satisfied}\mathcal{A}:=\left\{(\pi,c,b,\tau)\in\Pi\times\mathcal{C}\times\mathcal{B}\times\mathcal{T}\mid\text{Conditions \eqref{item:control\_constraints}-\eqref{item:wealth\_admissibility} are satisfied}\right\} |  | (2.11) |

Here, Π\Pi, 𝒞\mathcal{C}, and ℬ\mathcal{B} represent the sets of admissible investment, consumption, and labor processes, respectively. The set 𝒯\mathcal{T} contains all {ℱt}\{\mathcal{F}\_{t}\}-stopping times τ\tau such that τ≤T\tau\leq T ℙ\mathbb{P}-almost surely.

###### Definition 2.1.

An investment-consumption-labor strategy (c,b,π,τ)(c,b,\pi,\tau) is said to be admissible if equation ([2.7](https://arxiv.org/html/2510.10371v1#S2.E7 "Equation 2.7 ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")) holds, almost surely.

We now formally define the agent’s utility maximization problem. The agent’s preferences are governed by two concave utility functions: u1u\_{1}, which captures the utility from consumption and labor before annuitization, and u2u\_{2}, which represents the utility from wealth at the moment of annuitization. Following the framework of Gerrard et al. ([2012](https://arxiv.org/html/2510.10371v1#bib.bib13)), the agent controls the consumption rate, the portfolio allocation, and the timing of the annuitization itself. A fund of size xx is converted into an annuity of k​xkx, where the annuity factor k>rk>r and this decision is irreversible. If the fund is exhausted before this point, all economic activity, including further investment or withdrawal, ceases.

The agent derives utility u1​(c,b)u\_{1}(c,b) from a payment of size cc and bb before annuitization and u2(kx)u\_{2}(kx\_{)} from the annuity payment after annuitization. The agent seeks to maximize the sum of these expected discounted utilities over all (c,b,π,τ)∈𝒜(c,b,\pi,\tau)\in\mathcal{A}. That is, we aim to determine (π∗,c∗,b∗,τ∗)∈𝒜(\pi^{\*},c^{\*},b^{\*},\tau^{\*})\in\mathcal{A} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | V(x)=sup(c,b,π,τ)∈𝒜𝔼[∫0TD∧τe−β​tu1(ct,bt))dt+𝟏{τ<TD}∫TD∧τTDe−β​tu2(kXτc,b,π,τ)dt],V(x)=\sup\_{(c,b,\pi,\tau)\in\mathcal{A}}\mathbb{E}\left[\int\_{0}^{T\_{D}\wedge\tau}e^{-\beta t}u\_{1}(c\_{t},b\_{t}))\,dt+\mathbf{1}\_{\{\tau<T\_{D}\}}\int\_{T\_{D}\wedge\tau}^{T\_{D}}e^{-\beta t}u\_{2}(kX^{c,b,\pi,\tau}\_{\tau})\,dt\right], |  | (2.12) |

where,
TDT\_{D} is the retiree’s time of death, β>0\beta>0 is a subjective discount rate that reflects the retiree’s time preference for money, k​Xτc,b,π,τkX^{c,b,\pi,\tau}\_{\tau} is the annuity payment, and 𝒜\mathcal{A} is the set of admissible control inputs.

Let nn denote the retiree’s current age, and let TnT\_{n} represent the retiree’s uncertain remaining lifetime. In Gao et al. ([2022](https://arxiv.org/html/2510.10371v1#bib.bib12)) and Gerrard et al. ([2012](https://arxiv.org/html/2510.10371v1#bib.bib13)), it is assumed that TnT\_{n} follows a distribution with a constant force of mortality δ>0\delta>0. Under this assumption, the probability of surviving tt years is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(Tn>t)=e​x​p​(−δ​t).P(T\_{n}>t)=exp\left(-\delta t\right). |  | (2.13) |

However, a more realistic model would incorporate an age-dependent force of mortality, particularly one that increases with age. Following the argument in Ashraf ([2023](https://arxiv.org/html/2510.10371v1#bib.bib1)), we introduce an age-dependent force of mortality and assume the Gompertz deterministic mortality law. That is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | δt=1λ​e​x​p​(nt−mλ).\delta\_{t}=\frac{1}{\lambda}exp\left(\frac{n\_{t}-m}{\lambda}\right). |  | (2.14) |

where ntn\_{t} is the age at time tt, mm is the modal value of life (in years), and λ\lambda is the dispersion parameter (in years). In this case, the probability of surviving tt years is expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | \@mathmeasure​\@mathmeasure​Θ​t​\@mathmeasure​4​\@mathmeasure​6​n​\@mathmeasure​8​(δ)​​p=P​(Tn>t)=e​x​p​(−∫0tδy​𝑑y),\@mathmeasure\displaystyle{}\@mathmeasure\tw@\scriptstyle{t}\@mathmeasure 4\scriptstyle{}\@mathmeasure 6\scriptstyle{n}\@mathmeasure 8\scriptstyle{(\delta)}\mathord{}\mathopen{\vphantom{\textstyle p}}p=P(T\_{n}>t)=exp\left(-\int\_{0}^{t}\delta\_{y}\,dy\right), |  | (2.15) |

where δy\delta\_{y} represents the force of mortality at age yy.
The deterministic age-dependent force of mortality is independent of the fund’s level of evolution. With this assumption, the objective function in ([2.12](https://arxiv.org/html/2510.10371v1#S2.E12 "Equation 2.12 ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")) can now be expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(x)=sup(c,b,π,τ)∈𝒜𝔼​[∫0τe−∫0s(β+δu)​𝑑u​u1​(bs,cs)​𝑑s+e−β​τβ+δτ​\@mathmeasure​\@mathmeasure​Θ​τ​\@mathmeasure​4​\@mathmeasure​6​n​\@mathmeasure​8​(δ)​​p​u2​(k​Xτ)],V(x)=\sup\_{(c,b,\pi,\tau)\in\mathcal{A}}\mathbb{E}\left[\int\_{0}^{\tau}e^{-\int\_{0}^{s}(\beta+\delta\_{u})du}u\_{1}(b\_{s},c\_{s})ds+\frac{e^{-\beta\tau}\,}{\beta+\delta\_{\tau}}\@mathmeasure\displaystyle{}\@mathmeasure\tw@\scriptstyle{\tau}\@mathmeasure 4\scriptstyle{}\@mathmeasure 6\scriptstyle{n}\@mathmeasure 8\scriptstyle{(\delta)}\mathord{}\mathopen{\vphantom{\textstyle p}}pu\_{2}(kX\_{\tau})\right], |  | (2.16) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | =sup(c,b,π,τ)∈𝒜𝔼​[∫0τe−(ρs)​s​u1​(bs,cs)​𝑑s+e−(ρτ)​τρτ​u2​(k​Xτ)].=\sup\_{(c,b,\pi,\tau)\in\mathcal{A}}\mathbb{E}\left[\int\_{0}^{\tau}e^{-(\rho\_{s})s}u\_{1}(b\_{s},c\_{s})ds+\frac{e^{-(\rho\_{\tau})\tau}}{\rho\_{\tau}}u\_{2}(kX\_{\tau})\right]. |  | (2.17) |

where, Xτ=Xτx,c,b,πX\_{\tau}=X\_{\tau}^{x,c,b,\pi} is the wealth at the time of annuitization τ\tau, ρt\rho\_{t} is the effective discount rate given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρt=∫0t(β+δy)​𝑑y.\rho\_{t}=\int\_{0}^{t}(\beta+\delta\_{y})\,dy. |  | (2.18) |

In the remainder of the paper, we focus on equation ([2.17](https://arxiv.org/html/2510.10371v1#S2.E17 "Equation 2.17 ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")).
Our analysis initially considers a constant effective discount rate
ρ\rho in equation ([2.17](https://arxiv.org/html/2510.10371v1#S2.E17 "Equation 2.17 ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")). The more general scenario where ρt\rho\_{t} varies with the mortality rate δt\delta\_{t}, is considered when we derive the closed-form solutions for the value function in Theorem [2.2](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem2 "Theorem 2.2 (Value function). ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality") and the optimal joint strategy (πt∗,ct∗,bt∗)(\pi\_{t}^{\*},c\_{t}^{\*},b\_{t}^{\*}) in Theorem [2.5](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem5 "Theorem 2.5 (Optimal policies in the continuation region). ‣ 2.1.1 Hamilton-Jacobi-Bellman Variational Equality ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality"). Under the constant discount rate assumption,
the objective function in ([2.17](https://arxiv.org/html/2510.10371v1#S2.E17 "Equation 2.17 ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")) can be expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(x)=sup(c,b,π,τ)∈𝒜𝔼​[∫0τe−ρ​t​u1​(ct,bt)​𝑑t+e−ρ​τρ​u2​(k​Xτ)].V(x)=\sup\_{(c,b,\pi,\tau)\in\mathcal{A}}\mathbb{E}\left[\int\_{0}^{\tau}e^{-\rho t}u\_{1}(c\_{t},b\_{t})\,dt+\frac{e^{-\rho\tau}}{\rho}u\_{2}(kX\_{\tau})\right]. |  | (2.19) |

The operation of such a scheme may be subject to local regulation, as discussed in Gerrard et al. ([2012](https://arxiv.org/html/2510.10371v1#bib.bib13)) as
ctc\_{t} and btb\_{t} may be restricted to lie in a given range (cmin,cmax)(c\_{\text{min}},c\_{\text{max}})
and (bmin,bmax)(b\_{\text{min}},b\_{\text{max}})
respectively, with both minimum and maximum values dependent on X0X\_{0}.
There may also be an upper limit on the annuitization time, for example, if retirees are required to purchase an annuity by a given age, the investment strategy πt\pi\_{t} may be constrained to be non-negative and/or to be no greater than unity, depending on rules regarding the possibility of borrowing to fund additional equity purchases or regarding the short selling of risky assets.
However, in this paper, we treat only the situation of unconstrained controls c,b,π,a​n​d​τc,b,\pi,and\penalty 10000\ \tau.

The admissible control inputs in equation ([2.11](https://arxiv.org/html/2510.10371v1#S2.E11 "Equation 2.11 ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")) are ℱt\mathcal{F}\_{t}-progressively measurable processes
such that the expectation in ([2.19](https://arxiv.org/html/2510.10371v1#S2.E19 "Equation 2.19 ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")) is well-defined, i.e.,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0τe−ρ​t​u1−​(ct,bt)​𝑑t+e−ρ​τρ​u2−​(k​Xτ)]<∞,\mathbb{E}\left[\int\_{0}^{\tau}e^{-\rho t}u\_{1}^{-}(c\_{t},b\_{t})\,dt+\frac{e^{-\rho\tau}}{\rho}u\_{2}^{-}(kX\_{\tau})\right]<\infty, |  | (2.20) |

where u−u^{-} denotes the negative part of uu, that is, u−=max⁡(−u,0)u^{-}=\max(-u,0). We say that the value V​(x)V(x) is *attainable* if there exists a quadruple (π∗,c∗,b∗,τ∗)∈𝒜(\pi^{\*},c^{\*},b^{\*},\tau^{\*})\in\mathcal{A} that achieves the supremum in ([2.19](https://arxiv.org/html/2510.10371v1#S2.E19 "Equation 2.19 ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")). If we let

|  |  |  |
| --- | --- | --- |
|  | J​(x;c,π,b,τ)≜𝔼​[∫0τe−ρ​t​u1​(ct,bt)​𝑑t+e−ρ​τρ​u2​(k​Xτ)],J(x;c,\pi,b,\tau)\triangleq\mathbb{E}\left[\int\_{0}^{\tau}e^{-\rho t}u\_{1}(c\_{t},b\_{t})\,dt+\frac{e^{-\rho\tau}}{\rho}u\_{2}(kX\_{\tau})\right], |  |

Then, the agent’s optimization problem is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(x)≜max(c,π,b,τ)∈𝒜⁡J​(x;c,π,b,τ).V(x)\triangleq\max\_{(c,\pi,b,\tau)\in\mathcal{A}}J(x;c,\pi,b,\tau). |  | (2.21) |

We assume that V​(x)<∞V(x)<\infty for all x∈(0,∞)x\in(0,\infty). Without loss of generality, the function V​(⋅)V(\cdot) is increasing on (0,∞)(0,\infty). For the concavity properties of V​(⋅)V(\cdot), see Section 8 of Karatzas and Wang ([2000](https://arxiv.org/html/2510.10371v1#bib.bib17)).

###### Remark 2.2.

A sufficient condition for the assumption that V​(x)<∞V(x)<\infty in Equation ([2.21](https://arxiv.org/html/2510.10371v1#S2.E21 "Equation 2.21 ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")) is that

|  |  |  |  |
| --- | --- | --- | --- |
|  | max⁡{u1​(x),u2​(x)}≤κ1+κ2​xη∀x∈(0,∞),\max\{u\_{1}(x),u\_{2}(x)\}\leq\kappa\_{1}+\kappa\_{2}x^{\eta}\quad\forall x\in(0,\infty),\quad\quad\quad\quad\quad\quad\quad |  | (2.22) |

for some κ1>0,κ2>0,η∈(0,1)\kappa\_{1}>0,\quad\kappa\_{2}>0,\quad\eta\in(0,1), (see Remark 3.6.8 in Karatzas and Shreve ([1998](https://arxiv.org/html/2510.10371v1#bib.bib16))).

Next, we specify the utility functions considered in equation ([2.17](https://arxiv.org/html/2510.10371v1#S2.E17 "Equation 2.17 ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")).
The utility function with two elasticity parameters α\alpha and β\beta represents the preferences for consumption and labor, respectively.
Following Koo et al. ([2013](https://arxiv.org/html/2510.10371v1#bib.bib20)), the Cobb–Douglas utility function is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(c,l)=u​(c,b)=1α⋅(cα​b1−α)1−γ1−γ,0<α<1,γ>0​ and ​γ≠1,u(c,l)=u(c,b)=\frac{1}{\alpha}\cdot\frac{\left(c^{\alpha}b^{1-\alpha}\right)^{1-\gamma}}{1-\gamma},\quad 0<\alpha<1,\gamma>0\text{ and }\gamma\neq 1, |  | (2.23) |

where γ\gamma is the retiree’s coefficient of relative risk aversion for two different goods cc and bb, and α\alpha is a constant parameter that measures the contribution of consumption to the agent’s utility when they aren’t retired. If we define γ1:=1−α​(1−γ)\gamma\_{1}:=1-\alpha(1-\gamma), the Cobb–Douglas utility function ([2.23](https://arxiv.org/html/2510.10371v1#S2.E23 "Equation 2.23 ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")) can be rewritten as

|  |  |  |
| --- | --- | --- |
|  | u​(c,b)=c1−γ1​bγ1−γ1−γ1.u(c,b)=\frac{c^{1-\gamma\_{1}}b^{\gamma\_{1}-\gamma}}{1-\gamma\_{1}}. |  |

Then, the utility function u1​(c,b)u\_{1}(c,b) in ([2.19](https://arxiv.org/html/2510.10371v1#S2.E19 "Equation 2.19 ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | u1​(c,b)=c1−γ1​bγ1−γ1−γ1,u\_{1}(c,b)=\frac{c^{1-\gamma\_{1}}b^{\gamma\_{1}-\gamma}}{1-\gamma\_{1}}, |  | (2.24) |

where cc is the consumption rate, bb is the labor income rate, and γ1\gamma\_{1} is the risk aversion coefficient for consumption. If the labor rate b=1b=1, the utility function u1u\_{1} becomes a power utility

|  |  |  |
| --- | --- | --- |
|  | u1​(x)=x1−γ11−γ1.u\_{1}(x)=\frac{x^{1-\gamma\_{1}}}{1-\gamma\_{1}}. |  |

### 2.1 Dynamic Programming Principle

We next present the Dynamic Programming Principle (DPP) for the value function. Let 𝒯t,T\mathcal{T}\_{t,T} denote the set of stopping times taking values in [t,T][t,T]. For a control process α^=(c,b,π,τ)\hat{\alpha}=(c,b,\pi,\tau) and a process XsX\_{s}, define Xst,xX\_{s}^{t,x} as the value of the state at time s≥ts\geq t starting from Xt=xX\_{t}=x under the control α^\hat{\alpha} (so Xtt,x=xX\_{t}^{t,x}=x). Let 𝒜​(t,x)\mathcal{A}(t,x) be the set of admissible control processes α^=(c,b,π,τ)\hat{\alpha}=(c,b,\pi,\tau) on the time interval [t,T][t,T], then the value function V​(t,x)V(t,x) for the problem in ([2.19](https://arxiv.org/html/2510.10371v1#S2.E19 "Equation 2.19 ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")) can now be expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t,x)=supα^∈𝒜​(t,x)𝔼​[∫tτf​(s,Xst,x,α^s)​𝑑s+g​(τ,Xτt,x)],\displaystyle V(t,x)=\sup\_{\hat{\alpha}\in\mathcal{A}(t,x)}\mathbb{E}\left[\int\_{t}^{\tau}f(s,X\_{s}^{t,x},\hat{\alpha}\_{s})ds+g(\tau,X\_{\tau}^{t,x})\right], |  | (2.25) |

where f​(s,Xst,x,α^s)=e−ρ​s​u1​(c​(s),b​(s))f(s,X^{t,x}\_{s},\hat{\alpha}\_{s})=e^{-\rho s}u\_{1}(c(s),b(s)) is the running cost/utility rate, g​(τ,Xτt,x)=e−ρ​τρ​u2​(k​Xτt,x)g(\tau,X\_{\tau}^{t,x})=\frac{e^{-\rho\tau}}{\rho}u\_{2}(kX\_{\tau}^{t,x}) is the terminal utility or cost at time τ\tau.

###### Theorem 2.1 (Dynamic Programming Principle).

Let (t,x)∈[0,T]×ℝN(t,x)\in[0,T]\times\mathbb{R}^{N}, for any stopping time τ∈𝒯t,T\tau\in\mathcal{T}\_{t,T}, then we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | V​(t,x)\displaystyle V(t,x) | =supα^∈𝒜​(t,x)supτ∈𝒯t,T𝔼​[∫tτf​(s,Xst,x,α^s)​𝑑s+g​(τ,Xτt,x)]\displaystyle=\sup\_{\hat{\alpha}\in\mathcal{A}(t,x)}\sup\_{\tau\in\mathcal{T}\_{t,T}}\mathbb{E}\left[\int\_{t}^{\tau}f(s,X\_{s}^{t,x},\hat{\alpha}\_{s})ds+g(\tau,X\_{\tau}^{t,x})\right] |  | (2.26) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =supα^∈𝒜​(t,x)infτ∈𝒯t,T𝔼​[∫tτf​(s,Xst,x,α^s)​𝑑s+g​(τ,Xτt,x)],\displaystyle=\sup\_{\hat{\alpha}\in\mathcal{A}(t,x)}\inf\_{\tau\in\mathcal{T}\_{t,T}}\mathbb{E}\left[\int\_{t}^{\tau}f(s,X\_{s}^{t,x},\hat{\alpha}\_{s})ds+g(\tau,X\_{\tau}^{t,x})\right], |  | (2.27) |

with the convention that e−ρ​τ​(ω)=0e^{-\rho\tau(\omega)}=0 when τ​(ω)=∞\tau(\omega)=\infty.

###### Remark 2.3.

In Theorem [2.1](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem1 "Theorem 2.1 (Dynamic Programming Principle). ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality"), we shall often use the following equivalent formulation of the Dynamic Programming Principle

1. (i)

   For all α^∈𝒜​(t,x)\hat{\alpha}\in\mathcal{A}(t,x) and τ∈𝒯t,T\tau\in\mathcal{T}\_{t,T}:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | V​(t,x)≥𝔼​[∫tτf​(s,Xst,x,α^s)​𝑑s+g​(τ,Xτt,x)].V(t,x)\geq\mathbb{E}\left[\int\_{t}^{\tau}f(s,X\_{s}^{t,x},\hat{\alpha}\_{s})ds+g(\tau,X\_{\tau}^{t,x})\right]. |  | (2.28) |
2. (ii)

   For all ε>0\varepsilon>0, there exists α^∈𝒜​(t,x)\hat{\alpha}\in\mathcal{A}(t,x) such that for all τ∈𝒯t,T\tau\in\mathcal{T}\_{t,T}

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | V​(t,x)−ε≤𝔼​[∫tτf​(s,Xst,x,α^s)​𝑑s+g​(τ,Xτt,x)].V(t,x)-\varepsilon\leq\mathbb{E}\left[\int\_{t}^{\tau}f(s,X\_{s}^{t,x},\hat{\alpha}\_{s})ds+g(\tau,X\_{\tau}^{t,x})\right]. |  | (2.29) |

Then, a stronger version of the DPP for the finite horizon case in Remark [2.3](https://arxiv.org/html/2510.10371v1#S2.Thmremark3 "Remark 2.3. ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality") can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t,x)=supα^∈𝒜​(t,x)𝔼​[∫tτf​(s,Xst,x,α^s)​𝑑s+g​(τ,Xτt,x)],V(t,x)=\sup\_{\hat{\alpha}\in\mathcal{A}(t,x)}\mathbb{E}\left[\int\_{t}^{\tau}f(s,X\_{s}^{t,x},\hat{\alpha}\_{s})ds+g(\tau,X\_{\tau}^{t,x})\right], |  | (2.30) |

for any stopping time τ∈𝒯t,T\tau\in\mathcal{T}\_{t,T}.

###### Proof of Theorem [2.1](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem1 "Theorem 2.1 (Dynamic Programming Principle). ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality"): Dynamic Programming Principle (DPP).

We consider the finite horizon case. To prove the DPP in Theorem [2.1](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem1 "Theorem 2.1 (Dynamic Programming Principle). ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality"), we proceed as follows.
  
1. Given an admissible control process α^∈𝒜t,T\hat{\alpha}\in\mathcal{A}\_{t,T},
for any stopping time τ\tau valued in [t,T][t,T], then by the law of iterated conditional expectation, we then get

|  |  |  |
| --- | --- | --- |
|  | J​(t,x,α^)=𝔼​[∫tτf​(s,Xst,x,α^s)​𝑑s+J​(τ,Xτt,x,α^)],J(t,x,\hat{\alpha})=\mathbb{E}\left[\int\_{t}^{\tau}f(s,X\_{s}^{t,x},\hat{\alpha}\_{s})ds+J(\tau,X\_{\tau}^{t,x},\hat{\alpha})\right], |  |

and since J​(⋅,⋅,α^)≤VJ(\cdot,\cdot,\hat{\alpha})\leq V, and τ\tau is arbitrary in Tt,T,T\_{t,T}, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(t,x,α^)\displaystyle J(t,x,\hat{\alpha}) | ≤infτ∈𝒯t,T𝔼​[∫tτf​(s,Xst,x,α^s)​𝑑s+g​(τ,Xτt,x)]\displaystyle\leq\inf\_{\tau\in\mathcal{T}\_{t,T}}\mathbb{E}\left[\int\_{t}^{\tau}f(s,X\_{s}^{t,x},\hat{\alpha}\_{s})ds+g(\tau,X\_{\tau}^{t,x})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤supα^∈𝒜​(t,x)infτ∈𝒯t,TE​[∫tτf​(s,Xst,x,α^s)​𝑑s+g​(τ,Xτt,x)].\displaystyle\leq\sup\_{\hat{\alpha}\in\mathcal{A}(t,x)}\inf\_{\tau\in\mathcal{T}\_{t,T}}E\left[\int\_{t}^{\tau}f(s,X\_{s}^{t,x},\hat{\alpha}\_{s})ds+g(\tau,X\_{\tau}^{t,x})\right]. |  |

By taking the supremum over α^\hat{\alpha} in the left-hand side term, we obtain the inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t,x)≤supα^∈𝒜​(t,x)infτ∈𝒯t,T𝔼​[∫tτf​(s,Xst,x,α^s)​𝑑s+g​(τ,Xτt,x)].V(t,x)\leq\sup\_{\hat{\alpha}\in\mathcal{A}(t,x)}\inf\_{\tau\in\mathcal{T}\_{t,T}}\mathbb{E}\left[\int\_{t}^{\tau}f(s,X^{t,x}\_{s},\hat{\alpha}\_{s})\,ds+g(\tau,X^{t,x}\_{\tau})\right]. |  | (2.31) |

2. Fix some arbitrary control α^∈𝒜t,T\hat{\alpha}\in\mathcal{A}\_{t,T} and τ∈𝒯t,T\tau\in\mathcal{T}\_{t,T}. By definition of the value functions in equation ([2.30](https://arxiv.org/html/2510.10371v1#S2.E30 "Equation 2.30 ‣ Remark 2.3. ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")), for any ε>0\varepsilon>0 and ω∈Ω\omega\in\Omega, there exists α^ε,ω∈𝒜​(τ​(ω),Xτ​(ω)t,x​(ω))\hat{\alpha}^{\varepsilon,\omega}\in\mathcal{A}(\tau(\omega),X\_{\tau(\omega)}^{t,x}(\omega)), which is an ε\varepsilon-optimal control for V​(τ​(ω),Xτ​(ω)t,x​(ω))V(\tau(\omega),X\_{\tau(\omega)}^{t,x}(\omega)), i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(τ​(ω),Xτ​(ω)t,x​(ω))−ε≤J​(τ​(ω),Xτ​(ω)t,x​(ω),α^ε,ω).V(\tau(\omega),X\_{\tau(\omega)}^{t,x}(\omega))-\varepsilon\leq J(\tau(\omega),X\_{\tau(\omega)}^{t,x}(\omega),\hat{\alpha}^{\varepsilon,\omega}). |  | (2.32) |

Define the process

|  |  |  |
| --- | --- | --- |
|  | αs∗​(ω)={α^s​(ω),if ​s∈[0,τ​(ω)]α^sε,ω​(ω),if ​s∈(τ​(ω),T].\alpha^{\*}\_{s}(\omega)=\begin{cases}\hat{\alpha}\_{s}(\omega),&\text{if }s\in[0,\tau(\omega)]\\ \hat{\alpha}\_{s}^{\varepsilon,\omega}(\omega),&\text{if }s\in(\tau(\omega),T].\end{cases} |  |

The process α∗\alpha^{\*} is progressively measurable and so lies in 𝒜​(t,x)\mathcal{A}(t,x) (see e.g., Chapter 7 in Bertsekas and Shreve ([1996](https://arxiv.org/html/2510.10371v1#bib.bib3))). Applying the law of iterated conditional expectation, and from equation ([2.32](https://arxiv.org/html/2510.10371v1#S2.E32 "Equation 2.32 ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t,x)\displaystyle V(t,x) | ≥J​(t,x,α∗)=𝔼​[∫tτf​(s,Xst,x,α^s)​𝑑s+J​(τ,Xτt,x,α^ε)]\displaystyle\geq J(t,x,\alpha^{\*})=\mathbb{E}\left[\int\_{t}^{\tau}f(s,X\_{s}^{t,x},\hat{\alpha}\_{s})ds+J(\tau,X\_{\tau}^{t,x},\hat{\alpha}^{\varepsilon})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥𝔼​[∫tτf​(s,Xst,x,α^s)​𝑑s+g​(τ,Xτt,x)]−ε.\displaystyle\geq\mathbb{E}\left[\int\_{t}^{\tau}f(s,X\_{s}^{t,x},\hat{\alpha}\_{s})ds+g(\tau,X\_{\tau}^{t,x})\right]-\varepsilon. |  |

Since α^∈𝒜​(t,x)\hat{\alpha}\in\mathcal{A}(t,x), τ∈𝒯t,T\tau\in\mathcal{T}\_{t,T} and ε>0\varepsilon>0, are arbitrary, we obtain the inequality

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t,x)≥supα^∈𝒜​(t,x)supτ∈𝒯t,T𝔼​[∫tτf​(s,Xst,x,α^s)​𝑑s+g​(τ,Xτt,x)].V(t,x)\geq\sup\_{\hat{\alpha}\in\mathcal{A}(t,x)}\sup\_{\tau\in\mathcal{T}\_{t,T}}\mathbb{E}\left[\int\_{t}^{\tau}f(s,X^{t,x}\_{s},\hat{\alpha}\_{s})\,ds+g(\tau,X^{t,x}\_{\tau})\right]. |  | (2.33) |

By combining the two inequalities ([2.31](https://arxiv.org/html/2510.10371v1#S2.E31 "Equation 2.31 ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")) and ([2.33](https://arxiv.org/html/2510.10371v1#S2.E33 "Equation 2.33 ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")), we obtain the required equality in equation ([2.30](https://arxiv.org/html/2510.10371v1#S2.E30 "Equation 2.30 ‣ Remark 2.3. ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")) for an arbitrary stopping time τ∈𝒯t,T\tau\in\mathcal{T}\_{t,T}.
Thus, the proof of the Dynamic Programming Principle is completed.
∎

###### Remark 2.4.

For the optimization problem in ([2.19](https://arxiv.org/html/2510.10371v1#S2.E19 "Equation 2.19 ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")) to be well-defined, several technical conditions must hold. First, we require positive annuity conversion factors, which emerge from the model parameters

|  |  |  |  |
| --- | --- | --- | --- |
|  | k:=r+ρ−rγ+γ−12​γ2​θ2>0andk1:=r+ρ−rγ1+γ1−12​γ12​θ2>0.k:=r+\frac{\rho-r}{\gamma}+\frac{\gamma-1}{2\gamma^{2}}\theta^{2}>0\quad\text{and}\quad k\_{1}:=r+\frac{\rho-r}{\gamma\_{1}}+\frac{\gamma\_{1}-1}{2\gamma\_{1}^{2}}\theta^{2}>0. |  | (2.34) |

These conditions ensure the existence of optimal solutions and appear naturally when solving the Hamilton-Jacobi-Bellman equation in ([2.44](https://arxiv.org/html/2510.10371v1#S2.E44 "Equation 2.44 ‣ 2.1.1 Hamilton-Jacobi-Bellman Variational Equality ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")). This specific form reflects the trade-off between market parameters (rr, θ\theta) and preference parameters (ρ\rho, γ\gamma).

###### Remark 2.5.

For the annuitization phase, we assume the value function u2​(x)u\_{2}(x) in ([2.12](https://arxiv.org/html/2510.10371v1#S2.E12 "Equation 2.12 ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")), which represents the agent’s utility from an annuity purchased with wealth xx, is analogous to the value function from the classical Merton problem Koo et al. ([2013](https://arxiv.org/html/2510.10371v1#bib.bib20)) and is obtained as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | G​(x)=e−ρ​τρ​u2​(k​Xτ)=e−ρ​τ​k1−γ1ρ​(1−γ1)​x1−γ1,G(x)=\frac{e^{-\rho\tau}}{\rho}u\_{2}(kX\_{\tau})=e^{-\rho\tau}\frac{k^{1-\gamma\_{1}}}{\rho(1-\gamma\_{1})}x^{1-\gamma\_{1}}, |  | (2.35) |

which serves as our terminal condition. This formulation preserves the homothetic property of CRRA utility while incorporating the annuity conversion mechanism.

###### Remark 2.6.

Define the quadratic function f​(m)f(m) for later consideration

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(m):=12​θ2​m2+(ρ−r+12​θ2)​m−ρ=0.f(m):=\frac{1}{2}\theta^{2}m^{2}+\left(\rho-r+\frac{1}{2}\theta^{2}\right)m-\rho=0. |  | (2.36) |

whose distinct roots m+>0m\_{+}>0 and m−<−1m\_{-}<-1 play crucial roles in determining the optimal strategies. The transformed quantities p1=m1+1p\_{1}=m\_{1}+1 and p2=m2+1p\_{2}=m\_{2}+1 are free boundary parameters associated with optimal retirement timing.

###### Definition 2.2.

The optimal retirement wealth threshold, denoted by x∗x^{\*}, is the critical level of wealth at which an agent chooses to retire to maximize their lifetime utility.

###### Definition 2.3.

The subsistence consumption wealth threshold, denoted by x~\tilde{x}, is the level of wealth required to meet the minimum consumption boundary c~\tilde{c} when the labor income component bb reaches its upper limit b¯\overline{b}.

###### Theorem 2.2 (Value function).

Given that Xt=xX\_{t}=x, assume the regularity conditions of Definition [2.1](https://arxiv.org/html/2510.10371v1#S2.Thmdefinition1 "Definition 2.1. ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality") hold, then the value function V​(x)V(x) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(x)={Vi​n​t​(x),if ​x<x~,Vb¯​(x),if ​x~≤x<x∗,G​(x),if ​x≥x∗,V(x)=\begin{cases}V\_{int}(x),&\text{if }x<\tilde{x},\\ V\_{\bar{b}}(x),&\text{if }\tilde{x}\leq x<x^{\*},\\ G(x),&\text{if }x\geq x^{\*},\end{cases} |  | (2.37) |

where G​(x)G(x) is terminal condition defined in ([2.35](https://arxiv.org/html/2510.10371v1#S2.E35 "Equation 2.35 ‣ Remark 2.5. ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")), with ρt\rho\_{t}, the effective discount rate given in equation ([2.18](https://arxiv.org/html/2510.10371v1#S2.E18 "Equation 2.18 ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")), which depends on the age-dependent force of mortality δy\delta\_{y} defined in equation ([2.14](https://arxiv.org/html/2510.10371v1#S2.E14 "Equation 2.14 ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")). The functions Vint​(⋅)V\_{\text{int}}(\cdot) and Vb¯​(⋅)V\_{\overline{b}}(\cdot) are the interior value functions for x<x~x<\tilde{x} and x~≤x<x∗\tilde{x}\leq x<x^{\*}, respectively.

###### Proof of Theorem [2.2](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem2 "Theorem 2.2 (Value function). ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality").

See Appendix [A.1](https://arxiv.org/html/2510.10371v1#A1.SS1 "A.1 Proof of Theorem 2.2 (Value Function): ‣ Appendix A Appendix: Proofs of Theorems ‣ Optimal annuitization with labor income under age-dependent force of mortality").
∎

###### Proposition 2.3 (Optimal retirement threshold).

Let Vb¯​(x)V\_{\bar{b}}(x) and G​(x)G(x) be the value functions for an agent in the final working phase and the retired state, respectively, as defined in Theorem [2.2](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem2 "Theorem 2.2 (Value function). ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality"). The optimal retirement wealth threshold, x∗x^{\*}, is determined by the smooth-pasting condition at the boundary, which ensures that the marginal value of wealth is continuous, that is (d​Vb¯d​x​(x∗)=d​Gd​x​(x∗))\left(\frac{dV\_{\bar{b}}}{dx}(x^{\*})=\frac{dG}{dx}(x^{\*})\right). Then, the threshold x∗x^{\*} is the unique solution to the following non-linear algebraic equation

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 12​θ2​(m+−m−)β+δt​B1​k−γ1​m+​(bb¯)m+​(γ1−γ)​(x∗)−γ1​m+\displaystyle\frac{\frac{1}{2}\theta^{2}(m\_{+}-m\_{-})}{\beta+\delta\_{t}}B\_{1}k^{-\gamma\_{1}m\_{+}}\left(\frac{b}{\bar{b}}\right)^{m\_{+}(\gamma\_{1}-\gamma)}(x^{\*})^{-\gamma\_{1}m\_{+}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =[r−12​θ2​m−β+δt−11−γ1​(1−(bb¯)−γ1−γγ1)]​x∗+r−12​θ2​m−β+δt​w​(b¯−b)r\displaystyle=\left[\frac{r-\frac{1}{2}\theta^{2}m\_{-}}{\beta+\delta\_{t}}-\frac{1}{1-\gamma\_{1}}\left(1-\left(\frac{b}{\bar{b}}\right)^{-\frac{\gamma\_{1}-\gamma}{\gamma\_{1}}}\right)\right]x^{\*}+\frac{r-\frac{1}{2}\theta^{2}m\_{-}}{\beta+\delta\_{t}}\frac{w(\bar{b}-b)}{r} |  | (2.38) |

###### Proof of Proposition [2.3](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem3 "Proposition 2.3 (Optimal retirement threshold). ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality").

See Appendix [A.5](https://arxiv.org/html/2510.10371v1#A1.SS5 "A.5 Proof of the Equation for the Retirement Threshold 𝑥^∗ ‣ Appendix A Appendix: Proofs of Theorems ‣ Optimal annuitization with labor income under age-dependent force of mortality").
∎

###### Definition 2.4.

Let Vint​(x)V\_{\text{int}}(x) and Vb¯​(x)V\_{\bar{b}}(x) be the value functions for an agent in the final working phase and the retired state, respectively, as defined in Theorem [2.2](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem2 "Theorem 2.2 (Value function). ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality"). The boundary between these states is a unique wealth threshold, x~\tilde{x}, determined by the value-matching condition. This condition requires the two functions to be equal at the boundary

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vint​(x~)=Vb¯​(x~)V\_{\text{int}}(\tilde{x})=V\_{\bar{b}}(\tilde{x}) |  | (2.39) |

###### Proposition 2.4 (Wealth threshold for the labor constraint).

Applying the value-matching condition from Definition [2.4](https://arxiv.org/html/2510.10371v1#S2.Thmdefinition4 "Definition 2.4. ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality") yields the following system of equations, which implicitly defines the wealth threshold x~\tilde{x} and the corresponding consumption level c~\tilde{c}:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | x~\displaystyle\tilde{x} | =A2​c~−γ​m−+1α​k​c~−w​b¯r=B1​c~−γ1​m++B2​c~−γ1​m−+1k1​c~−w​(b¯−b)r\displaystyle=A\_{2}\tilde{c}^{-\gamma m\_{-}}+\frac{1}{\alpha k}\tilde{c}-\frac{w\bar{b}}{r}=B\_{1}\tilde{c}^{-\gamma\_{1}m\_{+}}+B\_{2}\tilde{c}^{-\gamma\_{1}m\_{-}}+\frac{1}{k\_{1}}\tilde{c}-\frac{w(\bar{b}-b)}{r} |  | (2.40) |

###### Proof of Proposition [2.4](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem4 "Proposition 2.4 (Wealth threshold for the labor constraint). ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality").

See Appendix [A.6](https://arxiv.org/html/2510.10371v1#A1.SS6 "A.6 Proof of the Equation for the Labor Constraint Threshold ‣ Appendix A Appendix: Proofs of Theorems ‣ Optimal annuitization with labor income under age-dependent force of mortality").
∎

#### 2.1.1 Hamilton-Jacobi-Bellman Variational Equality

We now employ a dynamic programming approach within the Hamilton-Jacobi-Bellman (HJB) framework to determine an optimal (π∗,c∗,b∗,τ∗)∈𝒜(\pi^{\*},c^{\*},b^{\*},\tau^{\*})\in\mathcal{A} that satisfies ([2.21](https://arxiv.org/html/2510.10371v1#S2.E21 "Equation 2.21 ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")). Consider the value function at time tt with wealth xx,

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(t,x)=sup(c,b,π,τ)∈𝒜𝔼​[∫tτe−ρ​t​u1​(ct,bt)​𝑑t+e−ρ​τρ​u2​(k​Xτ)].J(t,x)=\sup\_{(c,b,\pi,\tau)\in\mathcal{A}}\mathbb{E}\left[\int\_{t}^{\tau}e^{-\rho t}u\_{1}(c\_{t},b\_{t})\,dt+\frac{e^{-\rho\tau}}{\rho}u\_{2}(kX\_{\tau})\right]. |  | (2.41) |

such that,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt\displaystyle dX\_{t} | =[r​Xt+πt​(μ−r)−ct+w​bt]​d​t+σ​πt​d​Wt,\displaystyle=\left[rX\_{t}+\pi\_{t}(\mu-r)-c\_{t}+wb\_{t}\right]dt+\sigma\pi\_{t}\,dW\_{t}, |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | lt={0≤lt≤Lif ​0≤t<τL¯if ​t≥τl\_{t}=\begin{cases}0\leq l\_{t}\leq L&\text{if }0\leq t<\tau\quad\\ \overline{L}&\text{if }t\geq\tau\quad\end{cases} |  | (2.42) |

where

|  |  |  |
| --- | --- | --- |
|  | J​(τ,x)=e−ρ​τρ​u2​(k​Xτ),J(\tau,x)=\frac{e^{-\rho\tau}}{\rho}u\_{2}(kX\_{\tau}), |  |

is the terminal condition at time τ\tau. Let V​(x)V(x) be the value function, V​(x)=J​(x)V(x)=J(x). Let
G​(x)=e−ρ​τρ​u2​(k​Xτ)G(x)=\frac{e^{-\rho\tau}}{\rho}u\_{2}(kX\_{\tau}) represent the value obtained upon fully retiring at wealth xx that Xt=xX\_{t}=x. Then the value function V​(x)V(x) satisfies the HJB variational equality

|  |  |  |  |
| --- | --- | --- | --- |
|  | max⁡{supc≥0,0≤b≤b¯,π[u1​(c,b)+ℒc,b,π,τ​V​(x)]−ρt​V​(x),G​(x)−V​(x)}=0,\max\left\{\sup\_{c\geq 0,0\leq b\leq\bar{b},\pi}\left[u\_{1}(c,b)+\mathcal{L}^{c,b,\pi,\tau}V(x)\right]-\rho\_{t}\,V(x),\quad G(x)-V(x)\right\}=0, |  | (2.43) |

where the generator ℒc,b,π,τ​V​(x)\mathcal{L}^{c,b,\pi,\tau}V(x) is

|  |  |  |
| --- | --- | --- |
|  | ℒc,b,π,τ​V​(x)=(r​x+π​(μ−r)−c+w​b)​V′​(x)+12​σ2​π2​V′′​(x).\mathcal{L}^{c,b,\pi,\tau}V(x)=\left(rx+\pi(\mu-r)-c+wb\right)V^{\prime}(x)+\frac{1}{2}\sigma^{2}\pi^{2}V^{\prime\prime}(x). |  |

The state space is divided into a continuation (working) region (x<x∗x<{x^{\*}}), where V​(x)>G​(x)V(x)>G(x), and the HJB equation holds

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρt​V​(x)=supc≥0,0≤b≤b¯,π[u1​(c,b)+(r​x+π​(μ−r)−c+w​b)​V′​(x)+12​σ2​π2​V′′​(x)],\rho\_{t}V(x)=\sup\_{c\geq 0,0\leq b\leq\bar{b},\pi}\left[u\_{1}(c,b)+\left(rx+\pi(\mu-r)-c+wb\right)V^{\prime}(x)+\frac{1}{2}\sigma^{2}\pi^{2}V^{\prime\prime}(x)\right], |  | (2.44) |

and
a stopping (retirement) region (x≥x∗x\geq x^{\*}, where V​(x)=G​(x)V(x)=G(x). The value x∗{x^{\*}} is the optimal retirement wealth threshold.

###### Remark 2.7 (Structure of the optimal strategy).

The HJB variational inequality in ([2.43](https://arxiv.org/html/2510.10371v1#S2.E43 "Equation 2.43 ‣ 2.1.1 Hamilton-Jacobi-Bellman Variational Equality ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")) partitions the state space into two distinct regions, separated by the optimal retirement wealth threshold x∗x^{\*}.

1. 1.

   Continuation Region (x<x∗x<x^{\*}): For wealth levels below the threshold, it is optimal for the agent to continue working. In this region, the value function V​(x)V(x) satisfies the HJB equation, as detailed in Proposition [2.3](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem3 "Proposition 2.3 (Optimal retirement threshold). ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality"):

   |  |  |  |
   | --- | --- | --- |
   |  | ρt​V​(x)=supc,b,π[u1​(c,b)+ℒc,b,π​V​(x)]\rho\_{t}V(x)=\sup\_{c,b,\pi}\left[u\_{1}(c,b)+\mathcal{L}^{c,b,\pi}V(x)\right] |  |
2. 2.

   Stopping (Retirement) Region (x≥x∗x\geq x^{\*}): Once the agent’s wealth reaches or exceeds the threshold, it is optimal to stop working and retire. The value function is then equal to the retirement value function, G​(x)G(x):

   |  |  |  |
   | --- | --- | --- |
   |  | V​(x)=G​(x)V(x)=G(x) |  |

   where G​(x)=e−ρ​τρ​u2​(k​Xτ)G(x)=\frac{e^{-\rho\tau}}{\rho}u\_{2}(kX\_{\tau}) represents the total utility derived from retiring with wealth xx.

###### Theorem 2.5 (Optimal policies in the continuation region).

Let V​(x)V(x) be a twice-continuously differentiable solution to the Hamilton-Jacobi-Bellman (HJB) equation ([2.43](https://arxiv.org/html/2510.10371v1#S2.E43 "Equation 2.43 ‣ 2.1.1 Hamilton-Jacobi-Bellman Variational Equality ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")) in the continuation region, where x<x∗x<x^{\*}. Then the admissible optimal policies for portfolio allocation, π∗​(x)\pi^{\*}(x), consumption, c∗​(x)c^{\*}(x), and labor, b∗​(x)b^{\*}(x), are given by the following first-order conditions

1. 1.

   Optimal portfolio: The optimal fraction of wealth invested in the risky asset follows the Merton rule

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | π∗​(x)=−θσ​V′​(x)V′′​(x).\pi^{\*}(x)=-\frac{\theta}{\sigma}\frac{V^{\prime}(x)}{V^{\prime\prime}(x)}. |  | (2.45) |
2. 2.

   Optimal consumption: The optimal consumption rate c∗c^{\*} is determined by the condition that the marginal utility of consumption equals the marginal value of wealth

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∂u1​(c∗,b∗)∂c=V′​(x).\frac{\partial u\_{1}(c^{\*},b^{\*})}{\partial c}=V^{\prime}(x). |  | (2.46) |
3. 3.

   Optimal labor: For an interior solution where 0<b∗<b¯0<b^{\*}<\bar{b}, the optimal labor supply b∗b^{\*} satisfies the condition that the marginal disutility of labor equals its marginal contribution to the value of wealth

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∂u1​(c∗,b∗)∂b=−w​V′​(x).\frac{\partial u\_{1}(c^{\*},b^{\*})}{\partial b}=-wV^{\prime}(x). |  | (2.47) |

   If condition ([3](https://arxiv.org/html/2510.10371v1#S2.I4.i3 "Item 3 ‣ Theorem 2.5 (Optimal policies in the continuation region). ‣ 2.1.1 Hamilton-Jacobi-Bellman Variational Equality ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")) is not met for any b∈(0,b¯)b\in(0,\bar{b}), the optimum is a corner solution at the boundary, b∗=b¯b^{\*}=\bar{b}.
4. 4.

   Marginal rate of substitution: Combining the conditions for Optimal consumption and labor in ([2](https://arxiv.org/html/2510.10371v1#S2.I4.i2 "Item 2 ‣ Theorem 2.5 (Optimal policies in the continuation region). ‣ 2.1.1 Hamilton-Jacobi-Bellman Variational Equality ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")) and ([3](https://arxiv.org/html/2510.10371v1#S2.I4.i3 "Item 3 ‣ Theorem 2.5 (Optimal policies in the continuation region). ‣ 2.1.1 Hamilton-Jacobi-Bellman Variational Equality ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")), respectively, for an interior solution yields the classic static optimality condition, where the marginal rate of substitution between consumption and leisure equals the wage rate

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∂u1​(c∗,b∗)/∂b∂u1​(c∗,b∗)/∂c=−w.\frac{\partial u\_{1}(c^{\*},b^{\*})/\partial b}{\partial u\_{1}(c^{\*},b^{\*})/\partial c}=-w. |  | (2.48) |

###### Proof of Theorem [2.5](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem5 "Theorem 2.5 (Optimal policies in the continuation region). ‣ 2.1.1 Hamilton-Jacobi-Bellman Variational Equality ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality").

See Appendix [A.2](https://arxiv.org/html/2510.10371v1#A1.SS2 "A.2 Proof of Theorem 2.5 (Optimal Policies) ‣ Appendix A Appendix: Proofs of Theorems ‣ Optimal annuitization with labor income under age-dependent force of mortality").
∎

###### Corollary 2.6 (Actuarially fair annuity rate).

The market-consistent annuity rate, denoted ka​n​n​u​i​t​y∗k\_{annuity}^{\*} can be given in an actuarially fair framework by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ka​n​n​u​i​t​y∗=ya¨​(β,δy),k\_{annuity}^{\*}=\frac{y}{\ddot{a}(\beta,\delta\_{y})}, |  | (2.49) |

where,

|  |  |  |  |
| --- | --- | --- | --- |
|  | a¨​(β,δy)=∫0∞e−β​s​\@mathmeasure​\@mathmeasure​Θ​s​\@mathmeasure​4​\@mathmeasure​6​y​\@mathmeasure​8​(δ)​​p​𝑑s,\ddot{a}(\beta,\delta\_{y})=\int\_{0}^{\infty}e^{-\beta s}\,{\@mathmeasure\displaystyle{}\@mathmeasure\tw@\scriptstyle{s}\@mathmeasure 4\scriptstyle{}\@mathmeasure 6\scriptstyle{y}\@mathmeasure 8\scriptstyle{(\delta)}\mathord{}\mathopen{\vphantom{\textstyle p}}p}\,ds, |  | (2.50) |

and β>0\beta>0 is a subjective discount rate that reflects the retiree’s time preference for money, \@mathmeasure​\@mathmeasure​Θ​t​\@mathmeasure​4​\@mathmeasure​6​y​\@mathmeasure​8​(δ)​​p\@mathmeasure\displaystyle{}\@mathmeasure\tw@\scriptstyle{t}\@mathmeasure 4\scriptstyle{}\@mathmeasure 6\scriptstyle{y}\@mathmeasure 8\scriptstyle{(\delta)}\mathord{}\mathopen{\vphantom{\textstyle p}}p is the survival probability defined in equation ([2.15](https://arxiv.org/html/2510.10371v1#S2.E15 "Equation 2.15 ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")) for an individual currently aged yy to survive ss more years, and δy\delta\_{y} represents the age-dependent force of mortality for that individual, as defined in equation ([2.14](https://arxiv.org/html/2510.10371v1#S2.E14 "Equation 2.14 ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")).

###### Theorem 2.7 (Optimal policies).

Assume the value function V​(x)V(x) from Theorem [2.2](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem2 "Theorem 2.2 (Value function). ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality") exists and satisfies the regularity conditions of Definition ([2.1](https://arxiv.org/html/2510.10371v1#S2.Thmdefinition1 "Definition 2.1. ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")), then the optimal strategies are given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ct∗\displaystyle c\_{t}^{\*} | ={(Vint′​(x)(−1−αw​α)(1−α)​(1−γ))−1/γ,if ​x<x~,(Vb¯′​(x)(b¯1−α)1−γ)−1/γ1,if ​x~≤x<x∗,ρt1/γ1​k(γ1−1)/γ1​x,if ​x≥x∗,\displaystyle=\begin{cases}\left(\dfrac{V^{\prime}\_{\mathrm{int}}(x)}{\left(-\dfrac{1-\alpha}{w\alpha}\right)^{(1-\alpha)(1-\gamma)}}\right)^{-1/\gamma},&\text{if }x<\tilde{x},\\[4.30554pt] \left(\dfrac{V^{\prime}\_{\bar{b}}(x)}{(\bar{b}^{1-\alpha})^{1-\gamma}}\right)^{-1/\gamma\_{1}},&\text{if }\tilde{x}\leq x<x^{\*},\\[4.30554pt] \rho\_{t}^{1/\gamma\_{1}}k^{(\gamma\_{1}-1)/\gamma\_{1}}x,&\text{if }x\geq x^{\*},\end{cases} |  | (2.51) |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | bt∗\displaystyle b\_{t}^{\*} | ={(1−αw​α)​(k1−γ1β+δt)−1/γ1​x,if ​x<x~,b¯,if ​x~≤x<x∗,0,if ​x≥x∗,\displaystyle=\begin{cases}\left(\dfrac{1-\alpha}{w\alpha}\right)\left(\dfrac{k^{1-\gamma\_{1}}}{\beta+\delta\_{t}}\right)^{-1/\gamma\_{1}}x,&\text{if }x<\tilde{x},\\[4.30554pt] \bar{b},&\text{if }\tilde{x}\leq x<x^{\*},\\[4.30554pt] 0,&\text{if }x\geq x^{\*},\end{cases} |  | (2.52) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | πt∗\displaystyle\pi\_{t}^{\*} | ={−θσ​Vint′​(x)Vint′′​(x),if ​x<x~,−θσ​Vb¯′​(x)Vb¯′′​(x),if ​x~≤x<x∗,θσ​γ1​x,if ​x≥x∗,\displaystyle=\begin{cases}-\dfrac{\theta}{\sigma}\dfrac{V^{\prime}\_{\mathrm{int}}(x)}{V^{\prime\prime}\_{\mathrm{int}}(x)},&\text{if }x<\tilde{x},\\[4.30554pt] -\dfrac{\theta}{\sigma}\dfrac{V^{\prime}\_{\bar{b}}(x)}{V^{\prime\prime}\_{\bar{b}}(x)},&\text{if }\tilde{x}\leq x<x^{\*},\\[4.30554pt] \dfrac{\theta}{\sigma\gamma\_{1}}x,&\text{if }x\geq x^{\*},\end{cases} |  | (2.53) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | τ∗\displaystyle\tau^{\*} | =inf{t≥0:x≥x∗}.\displaystyle=\inf\{t\geq 0:x\geq x^{\*}\}. |  | (2.54) |

where δt\delta\_{t} represents the age-dependent force of mortality at age tt defined in equation ([2.14](https://arxiv.org/html/2510.10371v1#S2.E14 "Equation 2.14 ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")), the functions Vi​n​t′​(x)V^{\prime}\_{int}(x), Vb¯′​(x)V^{\prime}\_{\bar{b}}(x), Vi​n​t′′​(x)V^{\prime\prime}\_{int}(x) and Vb¯′′​(x)V^{\prime\prime}\_{\bar{b}}(x) represent the first and second derivatives of the value function in the respective regions in Theorem [2.2](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem2 "Theorem 2.2 (Value function). ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality").

###### Corollary 2.8 (Optimal Annuity Payment Rate).

Given optimal policies as in Theorem [2.5](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem5 "Theorem 2.5 (Optimal policies in the continuation region). ‣ 2.1.1 Hamilton-Jacobi-Bellman Variational Equality ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality"), with the optimal retirement wealth threshold x∗x^{\*}, the optimal annuity payment rate kt∗k\_{t}^{\*} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | kt∗={0,if −w​b¯r<x<x∗(working period),ϕ​x,if ​x≥x∗(full retirement period),k\_{t}^{\*}=\begin{cases}0,&\text{if }-\frac{w\bar{b}}{r}<x<x^{\*}\quad\text{(working period)},\\[6.0pt] \phi x,&\text{if }x\geq x^{\*}\quad\text{(full retirement period)},\end{cases} |  | (2.55) |

where ϕ\phi is the endogenous withdrawal rate and satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕ=(ct∗ρ1γ1​x)γ1γ1−1|x≥x∗=k,\phi=\left(\frac{c\_{t}^{\*}}{\rho^{\frac{1}{\gamma\_{1}}}x}\right)^{\frac{\gamma\_{1}}{\gamma\_{1}-1}}\bigg|\_{x\geq x^{\*}}=k, |  | (2.56) |

with ct∗c\_{t}^{\*} given by the optimal consumption policy in ([2.51](https://arxiv.org/html/2510.10371v1#S2.E51 "Equation 2.51 ‣ Theorem 2.7 (Optimal policies). ‣ 2.1.1 Hamilton-Jacobi-Bellman Variational Equality ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")).

## 3 Results and Discussion

We focus on the continuation (working period) region (x<x∗x<{x^{\*}}), where V​(x)>G​(x)V(x)>G(x), and the stopping (full retirement) region (x≥x∗x\geq{x^{\*}}), where V​(x)=G​(x)V(x)=G(x). The value x∗{x^{\*}} is the optimal retirement wealth threshold. We implement the optimal results outlined in Theorem
[2.2](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem2 "Theorem 2.2 (Value function). ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality") and Theorem [2.5](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem5 "Theorem 2.5 (Optimal policies in the continuation region). ‣ 2.1.1 Hamilton-Jacobi-Bellman Variational Equality ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality") and discuss their practical applications in retirement planning.

### 3.1 Numerical Implementation and Results

We set the model parameters following the common setting of Gerrard et al. ([2012](https://arxiv.org/html/2510.10371v1#bib.bib13)), Chen et al. ([2021](https://arxiv.org/html/2510.10371v1#bib.bib6)), and Gao et al. ([2022](https://arxiv.org/html/2510.10371v1#bib.bib12)), for a male retiree at age 6060 with a varying force of mortality δt\delta\_{t}. Unless otherwise specified, the parameters are: w=10w=10 (wage rate), α=0.2\alpha=0.2 (weight for consumption in the period utility function), r=0.02r=0.02 (interest rate), γ=2\gamma=2 (risk aversion coefficient), γ1=1.2\gamma\_{1}=1.2 (risk aversion coefficient for the second part of consumption), θ=0.07\theta=0.07 (market price of risk factor),  subjective discount factor β∈(0.01,0.055)\beta\in(0.01,0.055),
and b¯=1\bar{b}=1 
(upper bound for labor income).

![Refer to caption](Figures/rho_age.png)


Figure 1: Evolution of the effective discount rate (ρt\rho\_{t}) for an agent starting at age 60, shown for different mortality dispersion parameters (λ\lambda). Age-dependent mortality causes ρt\rho\_{t} to rise sharply, reflecting higher mortality risk at advanced ages.

[Figure 1](https://arxiv.org/html/2510.10371v1#S3.F1 "Figure 1 ‣ 3.1 Numerical Implementation and Results ‣ 3 Results and Discussion ‣ Optimal annuitization with labor income under age-dependent force of mortality") examines the impact of the effective discount rate ρt\rho\_{t}, which reflects the age-dependent force of mortality. Compared to existing research on optimal annuitization, including studies by Gerrard et al. ([2012](https://arxiv.org/html/2510.10371v1#bib.bib13)) and Gao et al. ([2022](https://arxiv.org/html/2510.10371v1#bib.bib12)), which assume a constant mortality rate, our findings demonstrate that ρt\rho\_{t} increases with age, indicating higher mortality risk. This results in greater discounting of future annuity payments, as the probability of survival decreases. At older ages, higher ρt\rho\_{t} values lower the present value of annuities, making them less appealing. Consequently, retirees may choose to keep more liquid assets or rely on alternative income sources, such as employment income. Conversely, younger retirees encounter lower ρt\rho\_{t} values, leading to higher present values for annuities and more substantial incentives to annuitize.

Labor income acts as a partial hedge against longevity risk, as individuals with stable earnings might delay annuitization. Nonetheless, the influence of age-dependent mortality remains significant because even with labor income, ρt\rho\_{t} continues to be a key factor in annuity valuation. As shown in
[Figure 1](https://arxiv.org/html/2510.10371v1#S3.F1 "Figure 1 ‣ 3.1 Numerical Implementation and Results ‣ 3 Results and Discussion ‣ Optimal annuitization with labor income under age-dependent force of mortality"), while older individuals qualify for higher annuity payouts due to shorter life expectancy, these benefits are offset by the increased discount rate ρt\rho\_{t}. Therefore, the optimal level of annuitization hinges on the interaction between mortality risk (via ρt\rho\_{t}), the retiree’s age, the availability of other income sources, and liquidity needs. In summary, the effective discount rate ρt\rho\_{t}, which incorporates age-dependent mortality effects, plays a vital role in shaping optimal annuitization decisions.

There are two competing effects for an older individual. First, the agent’s perspective (demand side): the agent’s personal discount rate ρt\rho\_{t} increases with age (see [Figure 1](https://arxiv.org/html/2510.10371v1#S3.F1 "Figure 1 ‣ 3.1 Numerical Implementation and Results ‣ 3 Results and Discussion ‣ Optimal annuitization with labor income under age-dependent force of mortality")). They value a dollar less next year, which reduces their desire to annuitize. Second, the insurer’s perspective (supply side): insurers offer better payout rates to older people. Since an 85-year-old has a shorter life expectancy than a 65-year-old, the insurer can offer a much higher annual payment for the same lump sum. This is often referred to as mortality credits and increases the incentive to annuitize.

![Refer to caption](Figures/surv_age.png)


Figure 2: Agent survival probability from age 60 (\@mathmeasure​\@mathmeasure​Θ​t​\@mathmeasure​4​\@mathmeasure​660​\@mathmeasure​8​​p\@mathmeasure\displaystyle{}\@mathmeasure\tw@\scriptstyle{t}\@mathmeasure 4\scriptstyle{}\@mathmeasure 6\scriptstyle{60}\@mathmeasure 8\scriptstyle{}\mathord{}\mathopen{\vphantom{\textstyle p}}p) under different mortality scenarios, defined by the modal age of death (mm) and the dispersion parameter (λ\lambda).

In [Figure 2](https://arxiv.org/html/2510.10371v1#S3.F2 "Figure 2 ‣ 3.1 Numerical Implementation and Results ‣ 3 Results and Discussion ‣ Optimal annuitization with labor income under age-dependent force of mortality"), we observe that survival probabilities decline sharply after age 70, causing the effective discount rate, ρt\rho\_{t}, to increase. This rising discount rate reveals a critical trade-off in the decision to annuitize. While conventional wisdom suggests that rising mortality risk should increase the demand for annuities as a form of longevity insurance, our model highlights a powerful counteracting force: a high personal discount rate diminishes the subjective value of future annuity payments.

![Refer to caption](Figures/Wealth_Alpha1.png)


Figure 3: Wealth level and the contribution of consumption to the retiree’s period utility.

At younger retirement ages (e.g., 60–70), the survival probability is high and ρt\rho\_{t} is relatively low. However, the perceived need for longevity insurance is distant, so individuals may prefer to maintain liquidity and rely on other income sources. As they age into their 70s and 80s, the sharp increase in ρt\rho\_{t} means they discount future income so heavily that even favorably priced annuities become unappealing. Essentially, the individual becomes increasingly unwilling to sacrifice present wealth for a future income stream they feel progressively less likely to receive. Therefore, our model suggests that the timing and extent of annuitization are governed by the tension between the need for longevity insurance and the declining subjective value of future income at advanced ages.

In [Figure 3](https://arxiv.org/html/2510.10371v1#S3.F3 "Figure 3 ‣ 3.1 Numerical Implementation and Results ‣ 3 Results and Discussion ‣ Optimal annuitization with labor income under age-dependent force of mortality"), we observe that the wealth level at annuitization is a decreasing function of α\alpha, which is the weight for consumption in the period utility function. With a lower α\alpha, consumption contributes more to the agent’s utility. The agent tends to annuitize and fully retire at a lower level of wealth.

[Figure 4](https://arxiv.org/html/2510.10371v1#S3.F4 "Figure 4 ‣ 3.1 Numerical Implementation and Results ‣ 3 Results and Discussion ‣ Optimal annuitization with labor income under age-dependent force of mortality") illustrates the optimal consumption policy across two distinct regions: the continuation region (x<x∗x<x^{\*}), where it is optimal for the agent to continue working because wealth is below the retirement threshold, and the stopping (full retirement) region (x≥x∗x\geq x^{\*}), where the agent’s wealth has reached or exceeded the retirement threshold. Different behaviors in these wealth regions characterize the policy.

![Refer to caption](Figures/Optimal_Consumption_Wealth_oct_2025_new.png)


Figure 4: Optimal consumption and wealth level. The solid blue line represents the pre-retirement optimal consumption path. The dashed lines show post-retirement consumption paths at different time horizons (t=5,10,15t=5,10,15 years post-retirement, corresponding to ages 65, 70, and 75). The vertical dotted lines indicate key thresholds: the subsistence wealth level (x~\tilde{x}) and the retirement wealth level (x∗x^{\*}). Notably, at the point of retirement (x∗x^{\*}), there is a discrete upward jump in consumption, reflecting a regime shift in the retirees’ spending behavior.

Before retirement, in pre-retirement, as shown in [Figure 4](https://arxiv.org/html/2510.10371v1#S3.F4 "Figure 4 ‣ 3.1 Numerical Implementation and Results ‣ 3 Results and Discussion ‣ Optimal annuitization with labor income under age-dependent force of mortality"), the agent’s optimal consumption behavior increases with wealth before reaching the retirement wealth target. This holds for wealth levels below the subsistence wealth level x~\tilde{x}, which drops after the subsistence wealth level x~\tilde{x}. The agent prioritizes wealth accumulation to achieve their retirement goal, resulting in a relatively flat consumption curve. Upon reaching the wealth level x∗x^{\*}, the agent fully retires. This triggers an immediate and discrete upward jump in consumption. The blue linear optimal consumption function (see [Figure 4](https://arxiv.org/html/2510.10371v1#S3.F4 "Figure 4 ‣ 3.1 Numerical Implementation and Results ‣ 3 Results and Discussion ‣ Optimal annuitization with labor income under age-dependent force of mortality")) represents the consumption level just before retirement, while the linear optimal consumption function at age 6565 represents the higher consumption level immediately after retiring.

In post-retirement (x≥x∗x\geq x^{\*}), or full retirement, consumption is represented by the family of linear optimal consumption functions at different ages (see [Figure 4](https://arxiv.org/html/2510.10371v1#S3.F4 "Figure 4 ‣ 3.1 Numerical Implementation and Results ‣ 3 Results and Discussion ‣ Optimal annuitization with labor income under age-dependent force of mortality")). In this phase, the agent’s optimal consumption behavior is significantly more sensitive to wealth, exhibiting a steeper, linear relationship. Furthermore, the consumption path shifts upward over time (from age 65 to 75), indicating that for a given level of wealth, the older agent consumes more, potentially due to a shorter remaining time horizon.

The optimal consumption function is therefore piecewise linear, with a notable discontinuity at the retirement threshold x∗x^{\*}. Contrary to a model where retirement might necessitate a drop in spending, this specification shows that achieving the threshold wealth, the agent unlocks a higher level of consumption. This is driven by the fact that the agent no longer needs to suppress consumption to save for a future goal and can begin to decumulate or spend the returns from their accumulated wealth and annuity payments.

![Refer to caption](Figures/Optimal_labor_Wealth_oct_2025_new.png)


Figure 5: Optimal labor income and wealth level. The red dashed line represents the threshold wealth level corresponding to the labor supplied. The green dashed line represents the threshold wealth level corresponding to the optimal retirement time τ\tau. The discontinuities at x~\tilde{x} and x∗{x^{\*}} represent sudden shifts in the retiree’s optimal labor supply as their wealth crosses critical thresholds. These shifts are linked to retiree decisions about annuitization (in the broader sense of securing future income streams) and the transition into a phase of reduced or no labor (retirement).

In [Figure 5](https://arxiv.org/html/2510.10371v1#S3.F5 "Figure 5 ‣ 3.1 Numerical Implementation and Results ‣ 3 Results and Discussion ‣ Optimal annuitization with labor income under age-dependent force of mortality"), we observe that before retirement, the agent receives an increasing income from labor until the threshold wealth level x~\tilde{x} is reached. In the low-wealth region (x<x~x<\tilde{x}), the agent is actively engaged in labor or borrowing to supplement their resources and maintain a basic consumption level. This is a phase of significant reliance on labor income or debt.

As wealth reaches x~\tilde{x}, there is a discrete jump upwards in the optimal labor income rate to b¯\bar{b}. This marks a change in strategy. At this wealth level, the agent is more secure and aims for a higher consumption level associated with a full retirement lifestyle. The jump reflects a temporary increase in labor supply to reach a desired savings level and align income with pre-retirement spending habits. Reaching x~\tilde{x} triggers a shift toward accumulating wealth for future annuitization, either formally through financial products or informally through savings drawdown. In the intermediate wealth range, the agent maintains a constant labor income rate of b¯\bar{b}.

Once an agent’s wealth reaches the retirement threshold, x∗x^{\*}, they exit the labor force. This stage marks the transition to full retirement, characterized by the complete cessation of labor income. From this point forward, the agent relies solely on their accumulated assets to support their desired consumption through accumulated wealth and annuity payments.

![Refer to caption](Figures/Optimal_Invest_Wealth_oct_2025_new.png)


Figure 6: Optimal investment and wealth level. The red dashed line represents the threshold wealth level corresponding to the labor supply. The green dashed line represents the threshold wealth level corresponding to the optimal retirement time τ\tau. The discontinuity (a jump) in the optimal investment strategy at x=x~x=\tilde{x} signifies a sudden change in the proportion of wealth allocated to the risky asset as the retiree’s wealth crosses the threshold x~\tilde{x}. The discontinuity at x=x∗x={x^{\*}} represents a shift from a constant investment amount (as a proportion of some base consumption level) to an investment amount that is linearly increasing with wealth.

In analyzing the optimal investment strategy shown in [Figure 6](https://arxiv.org/html/2510.10371v1#S3.F6 "Figure 6 ‣ 3.1 Numerical Implementation and Results ‣ 3 Results and Discussion ‣ Optimal annuitization with labor income under age-dependent force of mortality"), a key feature is the discontinuity at the retirement wealth threshold, x∗x^{\*}. The jump is the fundamental and instantaneous change in the agent’s investment strategy, driven by the economics of labour income. Before full retirement, an agent’s total wealth consists of both financial wealth and labour income, with the latter representing the present value of all future labor income. This labor income acts as a large, stable, bond-like asset. To achieve an optimal risk balance across their total portfolio, the agent can aggressively invest their financial wealth in risky assets and safe portion represented by their future income. This explains the high level of investment just before the retirement threshold.

At the moment of full retirement, when wealth reaches x∗x^{\*}, labour income vanishes. The agent’s total wealth is now composed entirely of their financial portfolio. To avoid being over-exposed to market risk, the agent must immediately rebalance by drastically reducing their allocation to risky assets. The sharp downward jump in the optimal investment, πt∗\pi\_{t}^{\*}, represents this strategic de-risking. The optimal policy we derived from our model (see ([2.53](https://arxiv.org/html/2510.10371v1#S2.E53 "Equation 2.53 ‣ Theorem 2.7 (Optimal policies). ‣ 2.1.1 Hamilton-Jacobi-Bellman Variational Equality ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality"))) captures this by switching from a complex value function that accounts for labor income to the classic Merton portfolio rule for a fully retired agent with no human capital.

[Figure 6](https://arxiv.org/html/2510.10371v1#S3.F6 "Figure 6 ‣ 3.1 Numerical Implementation and Results ‣ 3 Results and Discussion ‣ Optimal annuitization with labor income under age-dependent force of mortality") shows the optimal proportion of risky investment. We observe a substantial decline in investment by the agent after full retirement. As reported in Ferrari and Zhu ([2023](https://arxiv.org/html/2510.10371v1#bib.bib11)), this result implies that agents start saving for retirement as a de-risking strategy as people tend to withdraw their investment in risky assets upon retirement to hedge the risk of unemployment. [Figure 6](https://arxiv.org/html/2510.10371v1#S3.F6 "Figure 6 ‣ 3.1 Numerical Implementation and Results ‣ 3 Results and Discussion ‣ Optimal annuitization with labor income under age-dependent force of mortality") also shows the optimal proportion of risky investment. We observe a significant decline in investment by the agent after full retirement. As reported in Ferrari and Zhu ([2023](https://arxiv.org/html/2510.10371v1#bib.bib11)), this result suggests that agents begin saving for retirement as a de-risking strategy, since people tend to withdraw their investments in risky assets upon retirement to hedge against unemployment risk.

The numerical results presented in Figures [4](https://arxiv.org/html/2510.10371v1#S3.F4 "Figure 4 ‣ 3.1 Numerical Implementation and Results ‣ 3 Results and Discussion ‣ Optimal annuitization with labor income under age-dependent force of mortality") and [6](https://arxiv.org/html/2510.10371v1#S3.F6 "Figure 6 ‣ 3.1 Numerical Implementation and Results ‣ 3 Results and Discussion ‣ Optimal annuitization with labor income under age-dependent force of mortality") are consistent with existing research on optimal annuitization (see, e.g., Coile and Milligan ([2009](https://arxiv.org/html/2510.10371v1#bib.bib9)); Ferrari and Zhu ([2023](https://arxiv.org/html/2510.10371v1#bib.bib11))). A key finding of our model is that the effective discount rate, ρt\rho\_{t}, increases with age, directly reflecting a higher mortality risk. Consequently, at older ages, these higher ρt\rho\_{t} values lower the subjective present value of annuities, making them a less appealing financial instrument for wealth management.

![Refer to caption](Figures/wealt_sub.png)


Figure 7: Retirement wealth level and elasticity of substitution.

In [Figure 7](https://arxiv.org/html/2510.10371v1#S3.F7 "Figure 7 ‣ 3.1 Numerical Implementation and Results ‣ 3 Results and Discussion ‣ Optimal annuitization with labor income under age-dependent force of mortality"), we observe that the critical wealth level x∗{x^{\*}} increases with the elasticity of substitution between consumption and leisure. An agent with a higher elasticity of substitution between consumption and leisure can consume more and achieve greater utility than an agent with a lower elasticity of substitution. Consequently, the former has a stronger incentive to continue working, leading to a higher threshold retirement wealth level and a tendency to delay full retirement.

![Refer to caption](Figures/an_intrest.png)


Figure 8: Sensitivity analysis of threshold wealth for annuitization for changes in the risk-free interest rate.

[Figure 8](https://arxiv.org/html/2510.10371v1#S3.F8 "Figure 8 ‣ 3.1 Numerical Implementation and Results ‣ 3 Results and Discussion ‣ Optimal annuitization with labor income under age-dependent force of mortality") illustrates the relationship between the risk-free interest rate and the wealth required for annuitization in retirement planning. We observe that in a low-interest-rate environment, retirees may need to allocate a larger portion of their retirement savings to an annuity to achieve their desired income level compared to a high-interest-rate environment. This relationship highlights the importance of considering broader economic conditions, particularly interest rate trends, when making annuitization decisions as part of retirement planning. [Figure 8](https://arxiv.org/html/2510.10371v1#S3.F8 "Figure 8 ‣ 3.1 Numerical Implementation and Results ‣ 3 Results and Discussion ‣ Optimal annuitization with labor income under age-dependent force of mortality") also shows that the cost of securing a guaranteed income stream through an annuity is inversely related to the prevailing risk-free interest rate, as high interest rates reduce the initial investment required for annuitization.

[Figure 9](https://arxiv.org/html/2510.10371v1#S3.F9 "Figure 9 ‣ 3.2 Optimal Policies Analysis ‣ 3 Results and Discussion ‣ Optimal annuitization with labor income under age-dependent force of mortality") illustrates an agent’s optimal annuity payment rate, kt∗k\_{t}^{\*}, which characterizes the individual’s annuitization strategy conditional on their wealth, xx. During the working period (x<x∗x<x^{\*}), the optimal annuity rate is zero, as the individual derives income from labor and postpones annuitization. This reflects the strategy of preserving liquid wealth for when labor income ceases. Upon reaching the retirement wealth threshold (x≥x∗x\geq x^{\*}), the optimal strategy is not to withdraw a constant percentage but to engage in a dynamic, phased annuitization. The process begins with a relatively small annuity rate at the onset of retirement. As the agent ages, the optimal rate, kt∗k\_{t}^{\*}, steadily increases. This indicates that the agent should progressively allocate more wealth towards securing a guaranteed lifetime income, allowing them to balance the need for portfolio growth in early retirement with the increasing importance of mitigating longevity risk in later life.

### 3.2 Optimal Policies Analysis

Retirement planning represents a critical phase in an individual’s life, demanding careful management of accumulated wealth to ensure a desired level of consumption and financial security over a potentially extended period, typically spanning from age 60 to 90. This section focuses on the analysis of theoretically derived optimal policies in Theorem [2.5](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem5 "Theorem 2.5 (Optimal policies in the continuation region). ‣ 2.1.1 Hamilton-Jacobi-Bellman Variational Equality ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality") for three key decision variables faced by agents: consumption, labor income rate, and investment. The mathematical expressions for these optimal policies define how a agent should ideally behave to these variables to maximize their well-being. We provide a detailed economic interpretation of the various policy regimes and the underlying economic parameters that shape them.

![Refer to caption](Figures/Annuity_payment_rate.png)


Figure 9: Optimal annuity payment rate with age.

Within the dynamic optimization framework of our model, the agent’s total wealth at any given time tt, denoted by xx, functions as the key state variable. This variable captures the agent’s current financial standing and determines the regime for each optimal policy. The agent’s decisions, or control variables, include the optimal consumption rate (ct∗c\_{t}^{\*}), which is the amount of wealth they choose to spend on goods and services at time tt. The optimal labor income rate (bt∗b\_{t}^{\*}) indicates the rate at which the agent earns income from work, if they opt to do so at time tt. The optimal investment strategy (πt∗\pi\_{t}^{\*}) specifically refers to the proportion of wealth allocated to a risky asset at time tt. The agent selects these control variables at each moment to maximize their overall utility, as outlined by the economic model in Section
[2](https://arxiv.org/html/2510.10371v1#S2 "2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality").

A key feature of the derived optimal policies is their piecewise nature. Each policy (ct∗,bt∗,πt∗)(c\_{t}^{\*},b\_{t}^{\*},\pi\_{t}^{\*}) adopts different functional forms depending on the current wealth level xx. Changes in these policies are triggered by specific wealth thresholds: w​b¯/rw\overline{b}/r, x~,\tilde{x}, and x∗{x^{\*}}. These thresholds represent critical points at which the agent’s optimal behavior undergoes a qualitative shift. The lower threshold, w​b¯/rw\overline{b}/r, represents the present value of the agent’s future labor income and a boundary linked to borrowing constraints or a minimum wealth needed to sustain a certain level of consumption. The other two thresholds x~\tilde{x} and x∗{x^{\*}}, are described in Propositions [2.4](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem4 "Proposition 2.4 (Wealth threshold for the labor constraint). ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality") and [2.3](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem3 "Proposition 2.3 (Optimal retirement threshold). ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality") represent the agent’s optimal behavior shift linked to labour supply and full retirement wealth threshold, respectively. They are significant milestones in the agent’s financial journey. These milestones may signal the point at which they can transition to a higher standard of living or cease relying entirely on labor income. The presence of these distinct wealth regimes highlights the adaptive nature of the optimal retirement strategy, where decisions depend on the agent’s evolving financial situation.

Figures [4](https://arxiv.org/html/2510.10371v1#S3.F4 "Figure 4 ‣ 3.1 Numerical Implementation and Results ‣ 3 Results and Discussion ‣ Optimal annuitization with labor income under age-dependent force of mortality"), [5](https://arxiv.org/html/2510.10371v1#S3.F5 "Figure 5 ‣ 3.1 Numerical Implementation and Results ‣ 3 Results and Discussion ‣ Optimal annuitization with labor income under age-dependent force of mortality"), and [6](https://arxiv.org/html/2510.10371v1#S3.F6 "Figure 6 ‣ 3.1 Numerical Implementation and Results ‣ 3 Results and Discussion ‣ Optimal annuitization with labor income under age-dependent force of mortality") illustrate that the optimal policies are piecewise functions of wealth. The first behavioral regime begins at the solvency threshold, which, given the parameters w=10w=10, b¯=1\bar{b}=1, and r=0.02r=0.02, is calculated as −w​b¯/r=−500-w\bar{b}/r=-500. The figures show how the functional form for consumption, labor, and investment changes as wealth crosses this and other critical thresholds.

#### 3.2.1 Analysis of Optimal Consumption Policy

The optimal consumption policy is structured across three distinct wealth regimes, each dictating how spending responds to changes in accumulated wealth (xx). In the low-wealth regime, where −w​b¯r<x<x~-\frac{w\bar{b}}{r}<x<\tilde{x}, consumption is not fixed but varies with current wealth. This variation is determined by the marginal value of additional wealth, Vint′​(x)V^{\prime}\_{\mathrm{int}}(x), ensuring that expenditures, including those for essential needs, are precisely aligned with the agent’s financial position. In the intermediate regime, defined by x~≤x<x∗\tilde{x}\leq x<x^{\*}, optimal consumption remains flexible and continues to adjust as assets increase. Here, the marginal value of wealth, Vb¯′​(x)V^{\prime}\_{\bar{b}}(x), governs spending, allowing the standard of living to improve progressively with financial growth. In the high-wealth regime, where x≥x∗x\geq x^{\*}, consumption becomes directly proportional to wealth. At this stage, the agent consumes a fixed proportion of assets annually, indicating that basic consumption needs are met and spending scales with asset size. This transition from wealth-sensitive consumption in lower regimes to a proportional rule at high wealth reflects a systematic approach to retirement financial management, where spending strategies shift from detailed adjustments to efficient resource utilization as financial security increases.

#### 3.2.2 Analysis of Optimal Labor Income Rate

The optimal labor income rate, bt∗b\_{t}^{\*}, demonstrates piecewise behavior as a function of wealth, xx. In the low wealth regime, defined by x<x~x<\tilde{x}, bt∗b\_{t}^{\*} is positive and increases linearly with wealth, as described by bt∗=(1−αw​α)​kγ1−1γ1​ρt1γ1​xb\_{t}^{\*}=\left(\frac{1-\alpha}{w\alpha}\right)k^{\frac{\gamma\_{1}-1}{\gamma\_{1}}}\rho\_{t}^{\frac{1}{\gamma\_{1}}}x. Under limited wealth, the agent is required to engage in labor to supplement income, and the labor supply adjusts in direct proportion to the wealth level within this regime.

In the intermediate wealth range, where x~≤x<x∗\tilde{x}\leq x<x^{\*}, the optimal labor income rate remains constant at its maximum value, b¯\bar{b}. This regime is characterized by continued labor participation to facilitate further wealth accumulation or to sustain elevated consumption levels. When wealth enters the high regime, defined by x≥x∗x\geq x^{\*}, the optimal labor income rate reduces to zero. At this stage, the agent no longer requires labor income and allocates all available time to leisure. This structure establishes a non-monotonic relationship: labor supply increases with wealth in the low regime, remains at its maximum in the intermediate regime, and ceases entirely in the high wealth regime.

#### 3.2.3 Analysis of Optimal Investment Strategy

The optimal investment strategy, πt∗\pi\_{t}^{\*}, is a piecewise function of the agent’s wealth, xx, with the policy shifting at critical wealth thresholds. The complete policy is defined as in equation ([2.53](https://arxiv.org/html/2510.10371v1#S2.E53 "Equation 2.53 ‣ Theorem 2.7 (Optimal policies). ‣ 2.1.1 Hamilton-Jacobi-Bellman Variational Equality ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")). In the continuation (working period) regimes (x<x∗x<x^{\*}), the amount invested in the risky asset is determined by the agent’s absolute risk tolerance (the term −V′/V′′-V^{\prime}/V^{\prime\prime}) and the market price of risk (θ/σ\theta/\sigma). This reflects a dynamic strategy where the agent’s willingness to accept risk evolves with their wealth.

Upon entering retirement (x≥x∗x\geq x^{\*}), the strategy simplifies to the classical Merton’s problem (see Koo et al. ([2013](https://arxiv.org/html/2510.10371v1#bib.bib20))) where the agent invests a constant proportion of their wealth, θ/σ​γ1\theta/\sigma\gamma\_{1}, in the risky asset. This shift represents a transition from the complex risk adjustments required during the wealth accumulation phase to a more stable asset allocation, focusing on wealth preservation and long-term growth in full retirement.

#### 3.2.4 Role of Parameters

The model parameters quantitatively determine the locations of wealth thresholds and the magnitudes of optimal policies. The optimal investment strategy exhibits significant sensitivity to the agent’s risk preferences and current market conditions. An increase in the risk aversion coefficient, γ1\gamma\_{1}, decreases the proportion of wealth allocated to the risky asset, as reflected in the term θ/(σ​γ1)\theta/(\sigma\gamma\_{1}). Investment is directly related to the market price of risk, represented by the Sharpe ratio, θ/σ\theta/\sigma. Additional parameters characterize the agent’s constraints and available opportunities. An increase in the risk-free interest rate, rr, shifts the solvency boundary, −w​b¯/r-w\bar{b}/r, thereby affecting policy regimes. Moreover, a higher wage rate, ww, amplifies the effect of employment, since labor income, w⋅bt∗w\cdot b\_{t}^{\*}, is directly proportional to the wage.

To summarize the numerical results, Section [3.2](https://arxiv.org/html/2510.10371v1#S3.SS2 "3.2 Optimal Policies Analysis ‣ 3 Results and Discussion ‣ Optimal annuitization with labor income under age-dependent force of mortality") analyzes the optimal policies for an agent’s consumption, labor, and investment. The results reveal a sophisticated framework where decisions are piecewise functions of the agent’s current wealth, defining distinct behavioral phases separated by critical thresholds. As illustrated in Figures [4](https://arxiv.org/html/2510.10371v1#S3.F4 "Figure 4 ‣ 3.1 Numerical Implementation and Results ‣ 3 Results and Discussion ‣ Optimal annuitization with labor income under age-dependent force of mortality"), [5](https://arxiv.org/html/2510.10371v1#S3.F5 "Figure 5 ‣ 3.1 Numerical Implementation and Results ‣ 3 Results and Discussion ‣ Optimal annuitization with labor income under age-dependent force of mortality"), and [6](https://arxiv.org/html/2510.10371v1#S3.F6 "Figure 6 ‣ 3.1 Numerical Implementation and Results ‣ 3 Results and Discussion ‣ Optimal annuitization with labor income under age-dependent force of mortality"), these strategies are consistent with findings in the existing literature (see, e.g., Section 6.2 of Ferrari and Zhu ([2023](https://arxiv.org/html/2510.10371v1#bib.bib11))). The analysis also demonstrates that the model’s underlying economic parameters, such as risk aversion and interest rates, are critical in shaping these thresholds and policy values. While this theoretical framework provides valuable insights, real-world retirement decisions often involve additional factors that necessitate more comprehensive planning tools.

## 4 Conclusion

In this paper, we address an optimal annuitization problem with labor income, considering an age-dependent force of mortality. We derive closed-form solutions for the value function and the optimal joint strategy for investment, consumption, and labor supply. This work highlights practical applications of our findings in retirement planning, offering valuable insights for individuals and policymakers. Key results show that an agent’s strategies change as their wealth surpasses certain thresholds, with the availability of labor income strongly motivating wealth accumulation. Our results also indicate that in low-interest environments, a larger share of savings must be allocated to an annuity to meet income goals.

Furthermore, our findings demonstrate that the effective discount rate increases with age, reflecting a higher mortality risk. This creates two competing effects for an older agent. First, as our model shows, the agent’s personal discount rate, ρt\rho\_{t}, increases with age (see [Figure 1](https://arxiv.org/html/2510.10371v1#S3.F1 "Figure 1 ‣ 3.1 Numerical Implementation and Results ‣ 3 Results and Discussion ‣ Optimal annuitization with labor income under age-dependent force of mortality")). They value a dollar less next year, which reduces their desire to annuitize. Second, from the insurer’s perspective, older agents are offered better payout rates for the same lump sum. This effect, often referred to as mortality credits, increases the incentive to annuitize. Our model’s key finding is that the disincentive from the high personal discount rate can outweigh the incentive from these favorable mortality credits. Therefore, the optimal level of annuitization depends critically on the interplay of mortality risk, the agent’s age, alternative income sources, and liquidity requirements.

This research has certain limitations. The model abstracts from several institutional and behavioral features that may influence annuitization decisions, such as age-dependent labor income, fixed retirement ages, and the presence of employer or public pension benefits. Extending the analysis to incorporate these elements, or to allow for partial and sequential annuitization as mortality risk evolves, would be a natural avenue for future research. Nonetheless, even within this stylized framework, introducing an age-dependent force of mortality reveals nuanced and sometimes counterintuitive interactions between longevity risk, consumption smoothing, and annuity demand. These insights underscore the theoretical importance of age-varying mortality in shaping optimal retirement and annuitization strategies and provide a foundation for future empirical and policy-oriented studies.

Acknowledgements: We acknowledge the support of the Natural Sciences and Engineering Research Council of Canada (NSERC), funding reference number RGPIN-2021-04112. Nous remercions le Conseil de recherches en sciences naturelles et en génie du Canada (CRSNG) de son soutien, numéro de référence RGPIN-2021-04112.

## References

* Ashraf [2023]

  Bushra Shehnam Ashraf.
  *Voluntary Retirement and Optimal Consumption in a Stochastic
  Mortality Environment*.
  PhD thesis, York University, Toronto, Canada, 2023.
* Barucci and Marazzina [2012]

  Emilio Barucci and Daniele Marazzina.
  Optimal investment, stochastic labor income and retirement.
  *Applied Mathematics and Computation*, 218(9):5588–5604, 2012.
* Bertsekas and Shreve [1996]

  Dimitri Bertsekas and Steven E Shreve.
  *Stochastic optimal control: the discrete-time case*, volume 5.
  Athena Scientific, Belmont, Massachusetts, 1996.
* Bismut [1973]

  Jean-Michel Bismut.
  Conjugate convex functions in optimal stochastic control.
  *Journal of Mathematical Analysis and Applications*, 44(2):384–404, 1973.
* Buttarazzi et al. [2025]

  Matteo Buttarazzi, Tiziano De Angelis, and Gabriele Stabile.
  Optimal annuitization with stochastic mortality: Piecewise
  deterministic mortality force.
  *arXiv preprint arXiv:2509.13091*, 2025.
* Chen et al. [2021]

  An Chen, Peter Hieber, and Manuel Rach.
  Optimal retirement products under subjective mortality beliefs.
  *Insurance: Mathematics and Economics*, 101:55–69,
  2021.
* Choi and Shim [2006]

  Kyoung Jin Choi and Gyoocheol Shim.
  Disutility, optimal retirement, and portfolio selection.
  *Mathematical Finance*, 16(2):443–467,
  2006.
* Choi et al. [2008]

  Kyoung Jin Choi, Gyoocheol Shim, and Yong Hyun Shin.
  Optimal portfolio, consumption-leisure and retirement choice problem
  with ces utility.
  *Mathematical Finance*, 18(3):445–472,
  2008.
* Coile and Milligan [2009]

  Courtney Coile and Kevin Milligan.
  How household portfolios evolve after retirement: The effect of aging
  and health shocks.
  *Review of Income and Wealth*, 55(2):226–248, 2009.
* Cvitanić and Karatzas [1992]

  Jakša Cvitanić and Ioannis Karatzas.
  Convex duality in constrained portfolio optimization.
  *The Annals of Applied Probability*, pages 767–818, 1992.
* Ferrari and Zhu [2023]

  Giorgio Ferrari and Shihao Zhu.
  Optimal retirement choice under age-dependent force of mortality.
  *arXiv preprint arXiv:2311.12169*, 2023.
* Gao et al. [2022]

  Xiang Gao, Cody Hyndman, Traian A Pirvu, and Petar Jevtić.
  Optimal annuitization post-retirement with labor income.
  *arXiv preprint arXiv:2202.04220*, 2022.
* Gerrard et al. [2012]

  Russell Gerrard, Bjarne Højgaard, and Elena Vigna.
  Choosing the optimal annuitization time post-retirement.
  *Quantitative Finance*, 12(7):1143–1159,
  2012.
* Heunis [2015a]

  Andrew J Heunis.
  Quadratic minimization with portfolio and terminal wealth
  constraints.
  *Annals of Finance*, 11(2):243–282,
  2015a.
* Heunis [2015b]

  Andrew J Heunis.
  Utility maximization in a regime switching model with convex
  portfolio constraints and margin requirements: optimality relations and
  explicit solutions.
  *SIAM Journal on Control and Optimization*, 53(4):2608–2656, 2015b.
* Karatzas and Shreve [1998]

  Ioannis Karatzas and Steven E Shreve.
  *Methods of Mathematical Finance*.
  Springer-Verlag, New York, 1998.
* Karatzas and Wang [2000]

  Ioannis Karatzas and Hui Wang.
  Utility maximization with discretionary stopping.
  *SIAM Journal on Control and Optimization*, 39(1):306–329, 2000.
* Karatzas et al. [1986]

  Ioannis Karatzas, John P Lehoczky, Suresh P Sethi, and Steven E Shreve.
  Explicit solution of a general consumption/investment problem.
  *Mathematics of Operations Research*, 11(2):261–294, 1986.
* Klotz et al. [2021]

  Anthony C. Klotz, Brian W. Swider, Yiduo Shao, and Melanie K. Prengler.
  The paths from insider to outsider: A review of employee exit
  transitions.
  *Human Resource Management*, 60(1):119–144,
  2021.
* Koo et al. [2013]

  Jung Lim Koo, Byung Lim Koo, and Yong Hyun Shin.
  An optimal investment, consumption, leisure, and voluntary retirement
  problem with Cobb–Douglas utility: dynamic programming approaches.
  *Applied Mathematics Letters*, 26(4):481–486, 2013.
* Labbé and Heunis [2007]

  Chantal Labbé and Andrew J Heunis.
  Convex duality in constrained mean-variance portfolio optimization.
  *Advances in Applied Probability*, 39(1):77–104, 2007.
* Lee and Shin [2015]

  Ho-Seok Lee and Yong Hyun Shin.
  An optimal portfolio, consumption-leisure and retirement choice
  problem with ces utility: a dynamic programming approach.
  *Journal of Inequalities and Applications*, 2015:1–13, 2015.
* Lim et al. [2008]

  Byung Hwa Lim, Yong Hyun Shin, and U Jin Choi.
  Optimal investment, consumption and retirement choice problem with
  disutility and subsistence consumption constraints.
  *Journal of Mathematical Analysis and Applications*,
  345(1):109–122, 2008.
* Lorenz and Zwick [2021]

  Svenja Lorenz and Thomas Zwick.
  Money also is sunny in a retiree’s world: financial incentives and
  work after retirement.
  *Journal for Labour Market Research*, 55(21), 2021.
* Merton [1969]

  Robert C Merton.
  Lifetime portfolio selection under uncertainty: The continuous-time
  case.
  *The Review of Economics and Statistics*, 51(3):247–257, 1969.
* Merton [1975]

  Robert C Merton.
  Optimum consumption and portfolio rules in a continuous-time model.
  In W.T. Ziemba and R.G. Vickson, editors, *Stochastic
  Optimization Models in Finance*, pages 621–661. Academic Press, 1975.
* Peng and Li [2023]

  Xingchun Peng and Baihui Li.
  Optimal investment, consumption and life insurance purchase with
  learning about return predictability.
  *Insurance: Mathematics and Economics*, 113:70–95,
  2023.
* Rockafellar [1970]

  R. Tyrrell Rockafellar.
  *Convex Analysis*.
  Princeton University Press, Princeton, NJ, 1970.
* Rockafellar and Wets [1998]

  R. Tyrrell Rockafellar and Roger J-B Wets.
  *Variational Analysis*, volume 317 of *Grundlehren der
  mathematischen Wissenschaften*.
  Springer-Verlag, Berlin, 1998.

## Appendix A Appendix: Proofs of Theorems

This appendix contains the proofs of theorems that would disrupt the flow of the paper.

### A.1 Proof of Theorem [2.2](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem2 "Theorem 2.2 (Value function). ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality") (Value Function):

We consider the pre-retirement problem (t<τt<\tau). The value function V​(x)V(x) satisfies the HJB equation ([2.44](https://arxiv.org/html/2510.10371v1#S2.E44 "Equation 2.44 ‣ 2.1.1 Hamilton-Jacobi-Bellman Variational Equality ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")) in the continuation region x<x∗x<x^{\*}, where V​(x)>G​(x)=k1−γ1ρt​(1−γ1)​x1−γ1V(x)>G(x)=\frac{k^{1-\gamma\_{1}}}{\rho\_{t}(1-\gamma\_{1})}x^{1-\gamma\_{1}}. We analyze the problem by dividing the continuation region based on the optimal labor supply control btb\_{t}.

Let V​(x)V(x) be the stationary value function satisfying the HJB equation in equation ([2.44](https://arxiv.org/html/2510.10371v1#S2.E44 "Equation 2.44 ‣ 2.1.1 Hamilton-Jacobi-Bellman Variational Equality ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρt​V​(x)=supc≥0,0≤b≤b¯,π[u1​(c,b)+(r​x+π​(μ−r)−c+w​b)​V′​(x)+12​σ2​π2​V′′​(x)].\rho\_{t}V(x)=\sup\_{c\geq 0,0\leq b\leq\bar{b},\pi}\left[u\_{1}(c,b)+\left(rx+\pi(\mu-r)-c+wb\right)V^{\prime}(x)+\frac{1}{2}\sigma^{2}\pi^{2}V^{\prime\prime}(x)\right]. |  | (A.1.1) |

where ρt\rho\_{t} is the effective discount rate ρt\rho\_{t} in equation ([2.18](https://arxiv.org/html/2510.10371v1#S2.E18 "Equation 2.18 ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")), which incorporates age-dependent force of mortality at age tt defined in equation ([2.14](https://arxiv.org/html/2510.10371v1#S2.E14 "Equation 2.14 ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")).

Case I: −r​w​b¯<x<x~-rw\bar{b}<x<\tilde{x} (Interior Labor Supply 0≤b∗<b¯0\leq b^{\*}<\bar{b}).

In this region, the optimal controls are determined by the first-order conditions (FOCs) derived in [Theorem 2.5](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem5 "Theorem 2.5 (Optimal policies in the continuation region). ‣ 2.1.1 Hamilton-Jacobi-Bellman Variational Equality ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | π∗​(x)\displaystyle\pi^{\*}(x) | =−θσ​V′​(x)V′′​(x),\displaystyle=-\frac{\theta}{\sigma}\frac{V^{\prime}(x)}{V^{\prime\prime}(x)}, |  | (A.1.2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | V′​(x)\displaystyle V^{\prime}(x) | =∂u1​(c∗,b∗)∂c,\displaystyle=\frac{\partial u\_{1}(c^{\*},b^{\*})}{\partial c}, |  | (A.1.3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂u1​(c∗,b∗)∂b\displaystyle\frac{\partial u\_{1}(c^{\*},b^{\*})}{\partial b} | =−w​V′​(x).\displaystyle=-wV^{\prime}(x). |  | (A.1.4) |

Using the Cobb-Douglas utility u1​(c,b)=11−γ​(cα​b1−α)1−γu\_{1}(c,b)=\frac{1}{1-\gamma}(c^{\alpha}b^{1-\alpha})^{1-\gamma}, conditions ([A.1.3](https://arxiv.org/html/2510.10371v1#A1.SS1.E3 "Equation A.1.3 ‣ A.1 Proof of Theorem 2.2 (Value Function): ‣ Appendix A Appendix: Proofs of Theorems ‣ Optimal annuitization with labor income under age-dependent force of mortality")) and ([A.1.4](https://arxiv.org/html/2510.10371v1#A1.SS1.E4 "Equation A.1.4 ‣ A.1 Proof of Theorem 2.2 (Value Function): ‣ Appendix A Appendix: Proofs of Theorems ‣ Optimal annuitization with labor income under age-dependent force of mortality")) imply the relationship c∗=−w​α1−α​b∗c^{\*}=-\frac{w\alpha}{1-\alpha}b^{\*}, or equivalently b∗=−1−αw​α​c∗b^{\*}=-\frac{1-\alpha}{w\alpha}c^{\*}.
Substituting these optimal controls into the HJB equation ([A.1.1](https://arxiv.org/html/2510.10371v1#A1.SS1.E1 "Equation A.1.1 ‣ A.1 Proof of Theorem 2.2 (Value Function): ‣ Appendix A Appendix: Proofs of Theorems ‣ Optimal annuitization with labor income under age-dependent force of mortality")), we obtain the maximized HJB equation for V​(x)=Vint​(x)V(x)=V\_{\text{int}}(x). We express the utility and drift terms using c∗c^{\*}:
b∗=−w​α1−α​c∗b^{\*}=-\frac{w\alpha}{1-\alpha}c^{\*},
u1​(c∗,b∗)=h1−γ​(c∗)1−γu\_{1}(c^{\*},b^{\*})=\frac{h}{1-\gamma}(c^{\*})^{1-\gamma}, where h=αα​(1−γ)​(−w​α1−α)(1−α)​(1−γ)h=\alpha^{\alpha(1-\gamma)}(-\frac{w\alpha}{1-\alpha})^{(1-\alpha)(1-\gamma)}.
−c∗+w​b∗=−c∗+w​(−1−αw​α​c∗)=−1α​c∗-c^{\*}+wb^{\*}=-c^{\*}+w(-\frac{1-\alpha}{w\alpha}c^{\*})=-\frac{1}{\alpha}c^{\*}.

Substituting π∗\pi^{\*} using ([A.1.2](https://arxiv.org/html/2510.10371v1#A1.SS1.E2 "Equation A.1.2 ‣ A.1 Proof of Theorem 2.2 (Value Function): ‣ Appendix A Appendix: Proofs of Theorems ‣ Optimal annuitization with labor income under age-dependent force of mortality")), the maximized HJB becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρt​Vint​(x)=h1−γ​(c∗)1−γ+(r​x−1α​c∗)​Vint′​(x)−12​θ2​(Vint′​(x))2Vint′′​(x).\rho\_{t}V\_{\text{int}}(x)=\frac{h}{1-\gamma}(c^{\*})^{1-\gamma}+\left(rx-\frac{1}{\alpha}c^{\*}\right)V\_{\text{int}}^{\prime}(x)-\frac{1}{2}\theta^{2}\frac{(V\_{\text{int}}^{\prime}(x))^{2}}{V\_{\text{int}}^{\prime\prime}(x)}. |  | (A.1.5) |

Now, assume optimal consumption c∗=Cint​(x)c^{\*}=C\_{\text{int}}(x) is invertible with inverse x=Xint​(c)x=X\_{\text{int}}(c). We need to express Vint′​(x)V\_{\text{int}}^{\prime}(x) and Vint′′​(x)V\_{\text{int}}^{\prime\prime}(x) in terms of c=c∗c=c^{\*}. From FOC ([A.1.3](https://arxiv.org/html/2510.10371v1#A1.SS1.E3 "Equation A.1.3 ‣ A.1 Proof of Theorem 2.2 (Value Function): ‣ Appendix A Appendix: Proofs of Theorems ‣ Optimal annuitization with labor income under age-dependent force of mortality")), we have

|  |  |  |
| --- | --- | --- |
|  | Vint′​(x)=∂u1​(c,b∗​(c))∂c=Kv​c−γ,where ​Kv=(−w​α1−α)(1−α)​(1−γ).V\_{\text{int}}^{\prime}(x)=\frac{\partial u\_{1}(c,b^{\*}(c))}{\partial c}=K\_{v}c^{-\gamma},\quad\text{where }K\_{v}=\left(-\frac{w\alpha}{1-\alpha}\right)^{(1-\alpha)(1-\gamma)}. |  |

(Note: KvK\_{v} involves potentially non-standard terms if w>0w>0).
The second derivative is

|  |  |  |
| --- | --- | --- |
|  | Vint′′​(x)=d​(Kv​c−γ)d​x=d​(Kv​c−γ)d​c​d​cd​x=(−γ​Kv​c−γ−1)​1Xint′​(c).V\_{\text{int}}^{\prime\prime}(x)=\frac{d(K\_{v}c^{-\gamma})}{dx}=\frac{d(K\_{v}c^{-\gamma})}{dc}\frac{dc}{dx}=(-\gamma K\_{v}c^{-\gamma-1})\frac{1}{X\_{\text{int}}^{\prime}(c)}. |  |

Substituting Vint′V\_{\text{int}}^{\prime} and Vint′′V\_{\text{int}}^{\prime\prime} into the maximized HJB ([A.1.5](https://arxiv.org/html/2510.10371v1#A1.SS1.E5 "Equation A.1.5 ‣ A.1 Proof of Theorem 2.2 (Value Function): ‣ Appendix A Appendix: Proofs of Theorems ‣ Optimal annuitization with labor income under age-dependent force of mortality")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρt​Vint​(Xint​(c))\displaystyle\rho\_{t}V\_{\text{int}}(X\_{\text{int}}(c)) | =h1−γ​c1−γ+(r​Xint​(c)−1α​c)​Kv​c−γ−12​θ2​(Kv​c−γ)2−γ​Kv​c−γ−1/Xint′​(c)\displaystyle=\frac{h}{1-\gamma}c^{1-\gamma}+\left(rX\_{\text{int}}(c)-\frac{1}{\alpha}c\right)K\_{v}c^{-\gamma}-\frac{1}{2}\theta^{2}\frac{(K\_{v}c^{-\gamma})^{2}}{-\gamma K\_{v}c^{-\gamma-1}/X\_{\text{int}}^{\prime}(c)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ρt​Vint​(Xint​(c))\displaystyle\rho\_{t}V\_{\text{int}}(X\_{\text{int}}(c)) | =h1−γ​c1−γ+Kv​r​Xint​(c)​c−γ−Kvα​c1−γ+12​γ​θ2​Kv​c1−γ​Xint′​(c).\displaystyle=\frac{h}{1-\gamma}c^{1-\gamma}+K\_{v}rX\_{\text{int}}(c)c^{-\gamma}-\frac{K\_{v}}{\alpha}c^{1-\gamma}+\frac{1}{2\gamma}\theta^{2}K\_{v}c^{1-\gamma}X\_{\text{int}}^{\prime}(c). |  |

To obtain the ODE for Xint​(c)X\_{\text{int}}(c), we differentiate this equation with respect to cc. We use the relation dd​c​Vint​(Xint​(c))=Vint′​(Xint​(c))⋅Xint′​(c)=(Kv​c−γ)​Xint′​(c)\frac{d}{dc}V\_{\text{int}}(X\_{\text{int}}(c))=V\_{\text{int}}^{\prime}(X\_{\text{int}}(c))\cdot X\_{\text{int}}^{\prime}(c)=(K\_{v}c^{-\gamma})X\_{\text{int}}^{\prime}(c).

|  |  |  |
| --- | --- | --- |
|  | ρt​Kv​c−γ​Xint′​(c)=h​c−γ+Kv​r​Xint′​(c)​c−γ−Kv​r​γ​Xint​(c)​c−γ−1−Kv​(1−γ)α​c−γ+θ2​Kv​(1−γ)2​γ​c−γ​Xint′​(c)+θ2​Kv​c1−γ2​γ​Xint′′​(c)\begin{split}\rho\_{t}K\_{v}c^{-\gamma}X\_{\text{int}}^{\prime}(c)={}&hc^{-\gamma}+K\_{v}rX\_{\text{int}}^{\prime}(c)c^{-\gamma}-K\_{v}r\gamma X\_{\text{int}}(c)c^{-\gamma-1}-\frac{K\_{v}(1-\gamma)}{\alpha}c^{-\gamma}\\ &+\frac{\theta^{2}K\_{v}(1-\gamma)}{2\gamma}c^{-\gamma}X\_{\text{int}}^{\prime}(c)+\frac{\theta^{2}K\_{v}c^{1-\gamma}}{2\gamma}X\_{\text{int}}^{\prime\prime}(c)\end{split} |  |

Multiplying by cγ+1/Kvc^{\gamma+1}/K\_{v} and rearranging terms yields a second-order linear ODE for Xint​(c)X\_{\text{int}}(c):

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜int​c2​Xint′′​(c)+ℬint​c​Xint′​(c)+𝒞int​Xint​(c)=𝒟int​c+ℰint,\mathcal{A}\_{\text{int}}c^{2}X^{\prime\prime}\_{\text{int}}(c)+\mathcal{B}\_{\text{int}}cX^{\prime}\_{\text{int}}(c)+\mathcal{C}\_{\text{int}}X\_{\text{int}}(c)=\mathcal{D}\_{\text{int}}c+\mathcal{E}\_{\text{int}}, |  | (A.1.6) |

where 𝒜int,ℬint,𝒞int,𝒟int,ℰint\mathcal{A}\_{\text{int}},\mathcal{B}\_{\text{int}},\mathcal{C}\_{\text{int}},\mathcal{D}\_{\text{int}},\mathcal{E}\_{\text{int}} are constants depending on the model parameters (ρ,r,θ,γ,α,h,Kv)(\rho,r,\theta,\gamma,\alpha,h,K\_{v}). Specifically:
𝒜int=12​γ​θ2\mathcal{A}\_{\text{int}}=\frac{1}{2\gamma}\theta^{2},
ℬint=ρt−r−12​γ​θ2​(1−γ)\mathcal{B}\_{\text{int}}=\rho\_{t}-r-\frac{1}{2\gamma}\theta^{2}(1-\gamma),
𝒞int=r​γ\mathcal{C}\_{\text{int}}=r\gamma,
𝒟int=1−γα+hKv\mathcal{D}\_{\text{int}}=\frac{1-\gamma}{\alpha}+\frac{h}{K\_{v}},
ℰint=0\mathcal{E}\_{\text{int}}=0.
The general solution to ([A.1.6](https://arxiv.org/html/2510.10371v1#A1.SS1.E6 "Equation A.1.6 ‣ A.1 Proof of Theorem 2.2 (Value Function): ‣ Appendix A Appendix: Proofs of Theorems ‣ Optimal annuitization with labor income under age-dependent force of mortality")) is Xint​(c)=Xh​(c)+Xp​(c)X\_{\text{int}}(c)=X\_{h}(c)+X\_{p}(c). The homogeneous solution is Xh​(c)=A1​cm1′+A2​cm2′X\_{h}(c)=A\_{1}c^{m^{\prime}\_{1}}+A\_{2}c^{m^{\prime}\_{2}} where m1′,m2′m^{\prime}\_{1},m^{\prime}\_{2} are roots of the characteristic equation 𝒜int​m​(m−1)+ℬint​m+𝒞int=0\mathcal{A}\_{\text{int}}m(m-1)+\mathcal{B}\_{\text{int}}m+\mathcal{C}\_{\text{int}}=0. The particular solution Xp​(c)X\_{p}(c) is typically found to be proportional to cc. Assuming m1′>0m^{\prime}\_{1}>0 and m2′<0m^{\prime}\_{2}<0, boundary conditions usually imply A1=0A\_{1}=0. Thus, the solution takes the form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xint​(c,A2)=A2​cm2′+const⋅c.X\_{\text{int}}(c,A\_{2})=A\_{2}c^{m^{\prime}\_{2}}+\text{const}\cdot c. |  | (A.1.7) |

Substituting this solution structure back into the expression for ρt​Vint​(Xint​(c))\rho\_{t}V\_{\text{int}}(X\_{\text{int}}(c)) gives the functional form of Vint​(x)V\_{\text{int}}(x) which depends on A2A\_{2} and involves terms related to c=Cint​(x)c=C\_{\text{int}}(x). This corresponds to the first case in Theorem ([2.2](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem2 "Theorem 2.2 (Value function). ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")).

Case II: x~≤x<x∗\tilde{x}\leq x<x^{\*} (Corner Labor Supply b=b¯b=\bar{b})

Here b∗=b¯b^{\*}=\bar{b}. The HJB equation is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρt​Vb¯​(x)=max(π,c)⁡[u1​(c,b¯)+(r​x+π​(μ−r)−c+w​b¯)​Vb¯′​(x)+12​σ2​π2​Vb¯′′​(x)].\rho\_{t}V\_{\bar{b}}(x)=\max\_{(\pi,c)}\left[u\_{1}(c,\bar{b})+\left(rx+\pi(\mu-r)-c+w\bar{b}\right)V\_{\bar{b}}^{\prime}(x)+\frac{1}{2}\sigma^{2}\pi^{2}V\_{\bar{b}}^{\prime\prime}(x)\right]. |  | (A.1.8) |

The FOCs are

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | π∗​(x)\displaystyle\pi^{\*}(x) | =−θσ​Vb¯′​(x)Vb¯′′​(x),\displaystyle=-\frac{\theta}{\sigma}\frac{V\_{\bar{b}}^{\prime}(x)}{V\_{\bar{b}}^{\prime\prime}(x)}, |  | (A.1.9) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vb¯′​(x)\displaystyle V\_{\bar{b}}^{\prime}(x) | =∂u1​(c∗,b¯)∂c.\displaystyle=\frac{\partial u\_{1}(c^{\*},\bar{b})}{\partial c}. |  | (A.1.10) |

Substituting π∗\pi^{\*} into ([A.1.8](https://arxiv.org/html/2510.10371v1#A1.SS1.E8 "Equation A.1.8 ‣ A.1 Proof of Theorem 2.2 (Value Function): ‣ Appendix A Appendix: Proofs of Theorems ‣ Optimal annuitization with labor income under age-dependent force of mortality")) yields the maximized HJB:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρt​Vb¯​(x)=u1​(c∗,b¯)+(r​x−c∗+w​b¯)​Vb¯′​(x)−12​θ2​(Vb¯′​(x))2Vb¯′′​(x).\rho\_{t}V\_{\bar{b}}(x)=u\_{1}(c^{\*},\bar{b})+\left(rx-c^{\*}+w\bar{b}\right)V\_{\bar{b}}^{\prime}(x)-\frac{1}{2}\theta^{2}\frac{(V\_{\bar{b}}^{\prime}(x))^{2}}{V\_{\bar{b}}^{\prime\prime}(x)}. |  | (A.1.11) |

Assume c∗=Cb¯​(x)c^{\*}=C\_{\bar{b}}(x) and x=Xb¯​(c)x=X\_{\bar{b}}(c). From FOC ([A.1.10](https://arxiv.org/html/2510.10371v1#A1.SS1.E10 "Equation A.1.10 ‣ A.1 Proof of Theorem 2.2 (Value Function): ‣ Appendix A Appendix: Proofs of Theorems ‣ Optimal annuitization with labor income under age-dependent force of mortality"))

|  |  |  |
| --- | --- | --- |
|  | Vb¯′​(x)=∂u1​(c,b¯)∂c=Kb¯′​c−γ1,where ​Kb¯′=(b¯1−α)1−γ​ and ​γ1=1−α​(1−γ).V\_{\bar{b}}^{\prime}(x)=\frac{\partial u\_{1}(c,\bar{b})}{\partial c}=K^{\prime}\_{\bar{b}}c^{-\gamma\_{1}},\quad\text{where }K^{\prime}\_{\bar{b}}=(\bar{b}^{1-\alpha})^{1-\gamma}\text{ and }\gamma\_{1}=1-\alpha(1-\gamma). |  |

Then Vb¯′′​(x)=−γ1​Kb¯′​c−γ1−1/Xb¯′​(c)V\_{\bar{b}}^{\prime\prime}(x)=-\gamma\_{1}K^{\prime}\_{\bar{b}}c^{-\gamma\_{1}-1}/X\_{\bar{b}}^{\prime}(c).
Substituting Vb¯′V\_{\bar{b}}^{\prime} and Vb¯′′V\_{\bar{b}}^{\prime\prime} into ([A.1.11](https://arxiv.org/html/2510.10371v1#A1.SS1.E11 "Equation A.1.11 ‣ A.1 Proof of Theorem 2.2 (Value Function): ‣ Appendix A Appendix: Proofs of Theorems ‣ Optimal annuitization with labor income under age-dependent force of mortality"))

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρt​Vb¯​(Xb¯​(c))\displaystyle\rho\_{t}V\_{\bar{b}}(X\_{\bar{b}}(c)) | =u1​(c,b¯)+(r​Xb¯​(c)−c+w​b¯)​Kb¯′​c−γ1−12​θ2​(Kb¯′​c−γ1)2−γ1​Kb¯′​c−γ1−1/Xb¯′​(c).\displaystyle=u\_{1}(c,\bar{b})+(rX\_{\bar{b}}(c)-c+w\bar{b})K^{\prime}\_{\bar{b}}c^{-\gamma\_{1}}-\frac{1}{2}\theta^{2}\frac{(K^{\prime}\_{\bar{b}}c^{-\gamma\_{1}})^{2}}{-\gamma\_{1}K^{\prime}\_{\bar{b}}c^{-\gamma\_{1}-1}/X\_{\bar{b}}^{\prime}(c)}. |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ρt​Vb¯​(Xb¯​(c))\displaystyle\rho\_{t}V\_{\bar{b}}(X\_{\bar{b}}(c)) | =u1​(c,b¯)+Kb¯′​r​Xb¯​(c)​c−γ1−Kb¯′​c1−γ1+Kb¯′​w​b¯​c−γ1+12​γ1​θ2​Kb¯′​c1−γ1​Xb¯′​(c).\displaystyle=u\_{1}(c,\bar{b})+K^{\prime}\_{\bar{b}}rX\_{\bar{b}}(c)c^{-\gamma\_{1}}-K^{\prime}\_{\bar{b}}c^{1-\gamma\_{1}}+K^{\prime}\_{\bar{b}}w\bar{b}c^{-\gamma\_{1}}+\frac{1}{2\gamma\_{1}}\theta^{2}K^{\prime}\_{\bar{b}}c^{1-\gamma\_{1}}X\_{\bar{b}}^{\prime}(c). |  |

Differentiating with respect to cc (using dd​c​Vb¯​(Xb¯​(c))=Vb¯′​(Xb¯​(c))​Xb¯′​(c)=Kb¯′​c−γ1​Xb¯′​(c)\frac{d}{dc}V\_{\bar{b}}(X\_{\bar{b}}(c))=V\_{\bar{b}}^{\prime}(X\_{\bar{b}}(c))X\_{\bar{b}}^{\prime}(c)=K^{\prime}\_{\bar{b}}c^{-\gamma\_{1}}X\_{\bar{b}}^{\prime}(c)) leads to a second-order linear ODE for Xb¯​(c)X\_{\bar{b}}(c)

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜b¯​c2​Xb¯′′​(c)+ℬb¯​c​Xb¯′​(c)+𝒞b¯​Xb¯​(c)=𝒟b¯​c+ℰb¯,\mathcal{A}\_{\bar{b}}c^{2}X^{\prime\prime}\_{\bar{b}}(c)+\mathcal{B}\_{\bar{b}}cX^{\prime}\_{\bar{b}}(c)+\mathcal{C}\_{\bar{b}}X\_{\bar{b}}(c)=\mathcal{D}\_{\bar{b}}c+\mathcal{E}\_{\bar{b}}, |  | (A.1.12) |

where 𝒜b¯,ℬb¯,𝒞b¯,𝒟b¯,ℰb¯\mathcal{A}\_{\bar{b}},\mathcal{B}\_{\bar{b}},\mathcal{C}\_{\bar{b}},\mathcal{D}\_{\bar{b}},\mathcal{E}\_{\bar{b}} are constants depending on model parameters and b¯\bar{b}.
The general solution is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xb¯​(c,B1,B2)=B1​cm1′′+B2​cm2′′+Xp,b¯​(c),X\_{\bar{b}}(c,B\_{1},B\_{2})=B\_{1}c^{m^{\prime\prime}\_{1}}+B\_{2}c^{m^{\prime\prime}\_{2}}+X\_{p,\bar{b}}(c), |  | (A.1.13) |

where m1′′,m2′′m^{\prime\prime}\_{1},m^{\prime\prime}\_{2} are roots of the characteristic equation for ([A.1.12](https://arxiv.org/html/2510.10371v1#A1.SS1.E12 "Equation A.1.12 ‣ A.1 Proof of Theorem 2.2 (Value Function): ‣ Appendix A Appendix: Proofs of Theorems ‣ Optimal annuitization with labor income under age-dependent force of mortality")) and Xp,b¯​(c)X\_{p,\bar{b}}(c) is a particular solution. Substituting back yields Vb¯​(x)V\_{\bar{b}}(x) involving B1,B2B\_{1},B\_{2}, corresponding to the second case in Theorem ([2.2](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem2 "Theorem 2.2 (Value function). ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")).

Retirement Region: x≥x∗x\geq x^{\*}

Here V​(x)=G​(x)=k1−γ1ρt​(1−γ1)​x1−γ1V(x)=G(x)=\frac{k^{1-\gamma\_{1}}}{\rho\_{t}(1-\gamma\_{1})}x^{1-\gamma\_{1}}.

Boundary Conditions and Constants A2,B1,B2A\_{2},B\_{1},B\_{2} and thresholds x~,x∗\tilde{x},x^{\*} are determined by imposing C2C^{2} continuity conditions at x=x~x=\tilde{x} and x=x∗x=x^{\*}, as detailed in Appendix ([A.4](https://arxiv.org/html/2510.10371v1#A1.SS4 "A.4 Proof of Boundary Conditions and Constants ‣ Appendix A Appendix: Proofs of Theorems ‣ Optimal annuitization with labor income under age-dependent force of mortality")). Solving the system derived from these conditions uniquely determines the constants and thresholds. For details on the constants c~\tilde{c}, B1B\_{1}, x∗x^{\*}, B2B\_{2}, A2A\_{2}, and x~\tilde{x}, see Appendicies [A.6](https://arxiv.org/html/2510.10371v1#A1.SS6 "A.6 Proof of the Equation for the Labor Constraint Threshold ‣ Appendix A Appendix: Proofs of Theorems ‣ Optimal annuitization with labor income under age-dependent force of mortality"),
[A.4.1](https://arxiv.org/html/2510.10371v1#A1.SS4.SSS1 "A.4.1 Derivation of 𝐵₁ ‣ A.4 Proof of Boundary Conditions and Constants ‣ Appendix A Appendix: Proofs of Theorems ‣ Optimal annuitization with labor income under age-dependent force of mortality"), [A.4.2](https://arxiv.org/html/2510.10371v1#A1.SS4.SSS2 "A.4.2 Derivation of 𝐵₂ ‣ A.4 Proof of Boundary Conditions and Constants ‣ Appendix A Appendix: Proofs of Theorems ‣ Optimal annuitization with labor income under age-dependent force of mortality"), [A.4.3](https://arxiv.org/html/2510.10371v1#A1.SS4.SSS3 "A.4.3 Derivation of the Constant 𝐴₂ ‣ A.4 Proof of Boundary Conditions and Constants ‣ Appendix A Appendix: Proofs of Theorems ‣ Optimal annuitization with labor income under age-dependent force of mortality") and [A.6](https://arxiv.org/html/2510.10371v1#A1.SS6 "A.6 Proof of the Equation for the Labor Constraint Threshold ‣ Appendix A Appendix: Proofs of Theorems ‣ Optimal annuitization with labor income under age-dependent force of mortality").
Thus, the proof is completed.

### A.2 Proof of Theorem [2.5](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem5 "Theorem 2.5 (Optimal policies in the continuation region). ‣ 2.1.1 Hamilton-Jacobi-Bellman Variational Equality ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality") (Optimal Policies)

The optimal policies (π∗,c∗,b∗,τ∗)(\pi^{\*},c^{\*},b^{\*},\tau^{\*}) stated in Theorem [2.5](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem5 "Theorem 2.5 (Optimal policies in the continuation region). ‣ 2.1.1 Hamilton-Jacobi-Bellman Variational Equality ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality") are obtained by applying the First-Order Conditions (FOCs) to the value function V​(x)V(x) determined in Theorem [2.2](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem2 "Theorem 2.2 (Value function). ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality"), considering the different regions defined by the thresholds x~\tilde{x} and x∗x^{\*}.

1. 1.

   Optimal Investment π∗\pi^{\*}:
   The FOC for the optimal investment in the risky asset, given by equation ([2.45](https://arxiv.org/html/2510.10371v1#S2.E45 "Equation 2.45 ‣ Item 1 ‣ Theorem 2.5 (Optimal policies in the continuation region). ‣ 2.1.1 Hamilton-Jacobi-Bellman Variational Equality ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")), is

   |  |  |  |
   | --- | --- | --- |
   |  | π∗​(x)=−θσ​V′​(x)V′′​(x).\pi^{\*}(x)=-\frac{\theta}{\sigma}\frac{V^{\prime}(x)}{V^{\prime\prime}(x)}. |  |

   Applying this to the three regions of the value function V​(x)V(x):

   * •

     For x<x~x<\tilde{x}:

     |  |  |  |
     | --- | --- | --- |
     |  | πt∗=−θσ​Vint′​(x)Vint′′​(x).\pi\_{t}^{\*}=-\frac{\theta}{\sigma}\frac{V^{\prime}\_{\text{int}}(x)}{V^{\prime\prime}\_{\text{int}}(x)}. |  |
   * •

     For x~≤x<x∗\tilde{x}\leq x<x^{\*}:

     |  |  |  |
     | --- | --- | --- |
     |  | πt∗=−θσ​Vb¯′​(x)Vb¯′′​(x).\pi\_{t}^{\*}=-\frac{\theta}{\sigma}\frac{V^{\prime}\_{\bar{b}}(x)}{V^{\prime\prime}\_{\bar{b}}(x)}. |  |
   * •

     For x≥x∗x\geq x^{\*}:
     Here V​(x)=G​(x)=k1−γ1ρt​(1−γ1)​x1−γ1V(x)=G(x)=\frac{k^{1-\gamma\_{1}}}{\rho\_{t}(1-\gamma\_{1})}x^{1-\gamma\_{1}}. Then

     |  |  |  |
     | --- | --- | --- |
     |  | G′​(x)=k1−γ1ρt​x−γ1,G′′​(x)=−γ1​k1−γ1ρt​x−γ1−1.G^{\prime}(x)=\frac{k^{1-\gamma\_{1}}}{\rho\_{t}}x^{-\gamma\_{1}},\qquad G^{\prime\prime}(x)=-\frac{\gamma\_{1}k^{1-\gamma\_{1}}}{\rho\_{t}}x^{-\gamma\_{1}-1}. |  |

     Substituting into the FOC formula,

     |  |  |  |
     | --- | --- | --- |
     |  | π∗​(x)=−θσ​G′​(x)G′′​(x)=−θσ​k1−γ1ρt​x−γ1−γ1​k1−γ1ρt​x−γ1−1=θσ​γ1​x.\pi^{\*}(x)=-\frac{\theta}{\sigma}\frac{G^{\prime}(x)}{G^{\prime\prime}(x)}=-\frac{\theta}{\sigma}\frac{\frac{k^{1-\gamma\_{1}}}{\rho\_{t}}x^{-\gamma\_{1}}}{-\frac{\gamma\_{1}k^{1-\gamma\_{1}}}{\rho\_{t}}x^{-\gamma\_{1}-1}}=\frac{\theta}{\sigma\gamma\_{1}}x. |  |

   This confirms the expression for πt∗\pi\_{t}^{\*} in Theorem [2.5](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem5 "Theorem 2.5 (Optimal policies in the continuation region). ‣ 2.1.1 Hamilton-Jacobi-Bellman Variational Equality ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality"). Explicit formulas for the first two regions would require the explicit forms of VintV\_{\text{int}} and Vb¯V\_{\bar{b}}.
2. 2.

   Optimal Consumption c∗c^{\*}:
   The derivation for the optimal consumption policy c∗c^{\*} proceeds as follows.

   * •

     The FOC for optimal consumption, equation ([2.46](https://arxiv.org/html/2510.10371v1#S2.E46 "Equation 2.46 ‣ Item 2 ‣ Theorem 2.5 (Optimal policies in the continuation region). ‣ 2.1.1 Hamilton-Jacobi-Bellman Variational Equality ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")), is

     |  |  |  |
     | --- | --- | --- |
     |  | V′​(x)=∂u1​(c∗,b∗)∂c,x<x∗.V^{\prime}(x)=\frac{\partial u\_{1}(c^{\*},b^{\*})}{\partial c},\quad x<x^{\*}. |  |

     For x≥x∗x\geq x^{\*}, the policy is derived from the retirement value function G​(x)G(x).
   * •

     For x<x~x<\tilde{x}:
     The value function is Vint​(x;A2)V\_{\text{int}}(x;A\_{2}) and optimal labor b∗b^{\*} is interior. The FOC is

     |  |  |  |
     | --- | --- | --- |
     |  | Vint′​(x)=∂u1​(c∗,bint)∂c.V^{\prime}\_{\text{int}}(x)=\frac{\partial u\_{1}(c^{\*},b^{\text{int}})}{\partial c}. |  |

     From the utility function ([2.24](https://arxiv.org/html/2510.10371v1#S2.E24 "Equation 2.24 ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")) and the relation between c∗c^{\*} and bint∗b\_{\text{int}}^{\*} (see [Theorem 2.5](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem5 "Theorem 2.5 (Optimal policies in the continuation region). ‣ 2.1.1 Hamilton-Jacobi-Bellman Variational Equality ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")),

     |  |  |  |
     | --- | --- | --- |
     |  | ∂u1​(c∗,b∗​(c∗))∂c=Kv​(c∗)−γ,Kv=(−1−αw​α)(1−α)​(1−γ).\frac{\partial u\_{1}(c^{\*},b^{\*}(c^{\*}))}{\partial c}=K\_{v}(c^{\*})^{-\gamma},\qquad K\_{v}=\left(-\frac{1-\alpha}{w\alpha}\right)^{(1-\alpha)(1-\gamma)}. |  |

     Thus,

     |  |  |  |
     | --- | --- | --- |
     |  | Vint′​(x)=Kv​(c∗)−γ⟹c∗​(x)=(Vint′​(x)Kv)−1/γ.V^{\prime}\_{\text{int}}(x)=K\_{v}(c^{\*})^{-\gamma}\quad\implies\quad c^{\*}(x)=\left(\frac{V^{\prime}\_{\text{int}}(x)}{K\_{v}}\right)^{-1/\gamma}. |  |

     This implicitly defines c∗​(x)=Cint​(x)c^{\*}(x)=C\_{\text{int}}(x).
   * •

     For x~≤x<x∗\tilde{x}\leq x<x^{\*}:
     The value function is Vb¯​(x;B1,B2)V\_{\bar{b}}(x;B\_{1},B\_{2}) and optimal labor is fixed at b∗=b¯b^{\*}=\bar{b}. The FOC is

     |  |  |  |
     | --- | --- | --- |
     |  | Vb¯′​(x)=∂u1​(c∗,b¯)∂c.V^{\prime}\_{\bar{b}}(x)=\frac{\partial u\_{1}(c^{\*},\bar{b})}{\partial c}. |  |

     For Cobb–Douglas utility,

     |  |  |  |
     | --- | --- | --- |
     |  | ∂u1​(c,b¯)∂c=Kb¯′​c−γ1,Kb¯′=(b¯1−α)1−γ,γ1=1−α​(1−γ).\frac{\partial u\_{1}(c,\bar{b})}{\partial c}=K^{\prime}\_{\bar{b}}c^{-\gamma\_{1}},\quad K^{\prime}\_{\bar{b}}=(\bar{b}^{1-\alpha})^{1-\gamma},\quad\gamma\_{1}=1-\alpha(1-\gamma). |  |

     Thus,

     |  |  |  |
     | --- | --- | --- |
     |  | Vb¯′​(x)=Kb¯′​(c∗)−γ1⟹c∗​(x)=(Vb¯′​(x)Kb¯′)−1/γ1.V^{\prime}\_{\bar{b}}(x)=K^{\prime}\_{\bar{b}}(c^{\*})^{-\gamma\_{1}}\quad\implies\quad c^{\*}(x)=\left(\frac{V^{\prime}\_{\bar{b}}(x)}{K^{\prime}\_{\bar{b}}}\right)^{-1/\gamma\_{1}}. |  |

     This defines c∗​(x)=Cb¯​(x)c^{\*}(x)=C\_{\bar{b}}(x).
   * •

     For x≥x∗x\geq x^{\*}:
     The agent is retired (b∗=0b^{\*}=0) and V​(x)=G​(x)=k1−γ1ρt​(1−γ1)​x1−γ1V(x)=G(x)=\frac{k^{1-\gamma\_{1}}}{\rho\_{t}(1-\gamma\_{1})}x^{1-\gamma\_{1}}.
     The FOC is

     |  |  |  |
     | --- | --- | --- |
     |  | G′​(x)=u2′​(c∗),u2′​(c)=c−γ1.G^{\prime}(x)=u\_{2}^{\prime}(c^{\*}),\quad u\_{2}^{\prime}(c)=c^{-\gamma\_{1}}. |  |

     Since

     |  |  |  |
     | --- | --- | --- |
     |  | G′​(x)=k1−γ1ρt​x−γ1,G^{\prime}(x)=\frac{k^{1-\gamma\_{1}}}{\rho\_{t}}x^{-\gamma\_{1}}, |  |

     we get

     |  |  |  |
     | --- | --- | --- |
     |  | k1−γ1ρt​x−γ1=(c∗)−γ1⟹c∗​(x)=(k1−γ1ρt)−1/γ1​x=ρt1/γ1​k(γ1−1)/γ1​x.\frac{k^{1-\gamma\_{1}}}{\rho\_{t}}x^{-\gamma\_{1}}=(c^{\*})^{-\gamma\_{1}}\quad\implies\quad c^{\*}(x)=\left(\frac{k^{1-\gamma\_{1}}}{\rho\_{t}}\right)^{-1/\gamma\_{1}}x=\rho\_{t}^{1/\gamma\_{1}}k^{(\gamma\_{1}-1)/\gamma\_{1}}x. |  |

     Thus, c∗​(x)=k′′​xc^{\*}(x)=k^{\prime\prime}x, with k′′=ρt1/γ1​k(γ1−1)/γ1k^{\prime\prime}=\rho\_{t}^{1/\gamma\_{1}}k^{(\gamma\_{1}-1)/\gamma\_{1}}.

   Explicit closed-form expressions for Cint​(x)C\_{\text{int}}(x) and Cb¯​(x)C\_{\bar{b}}(x) are generally unobtainable.
3. 3.

   Optimal Labor Supply b∗b^{\*}:

   * •

     For x<x~x<\tilde{x}: Optimal labor is interior and proportional to optimal consumption, given by the marginal rate of substitution condition:

     |  |  |  |
     | --- | --- | --- |
     |  | b∗​(x)=(1−αw​α)​c∗​(x)=(1−αw​α)​Cint​(x)b^{\*}(x)=\left(\frac{1-\alpha}{w\alpha}\right)c^{\*}(x)=\left(\frac{1-\alpha}{w\alpha}\right)C\_{\text{int}}(x) |  |
   * •

     For x~≤x<x∗\tilde{x}\leq x<x^{\*}: The labor supply constraint is binding, so b∗=b¯b^{\*}=\bar{b}.
   * •

     For x≥x∗x\geq x^{\*}: The agent is retired, so labor supply is b∗=0b^{\*}=0.
4. 4.

   Optimal Retirement Time τ∗\tau^{\*}:
   The problem is an optimal stopping problem where the agent chooses to retire when their wealth process XtX\_{t} first reaches the optimal threshold x∗x^{\*}. This threshold is determined by the value-matching and smooth-pasting conditions, V​(x∗)=G​(x∗)V(x^{\*})=G(x^{\*}) and V′​(x∗)=G′​(x∗)V^{\prime}(x^{\*})=G^{\prime}(x^{\*}). Therefore, the optimal retirement time is:

   |  |  |  |
   | --- | --- | --- |
   |  | τ∗=inf{t≥0:Xt≥x∗}\tau^{\*}=\inf\{t\geq 0:X\_{t}\geq x^{\*}\} |  |

This completes the derivation of the optimal policies.

### A.3 System of Equations for Constants and Thresholds

The constants A2,B1,B2A\_{2},B\_{1},B\_{2} and the wealth thresholds x~,x∗\tilde{x},x^{\*} are determined by ensuring the value function is twice continuously differentiable (C2C^{2}) across the boundaries. This requires enforcing value-matching, smooth-pasting, and super-contact conditions.

#### A.3.1 Derivation of Consumption Threshold c~\tilde{c}

The consumption threshold c~\tilde{c} corresponds to the point where the unconstrained optimal labor supply reaches its upper bound b¯\bar{b}. From the FOC relating optimal labor and consumption, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | b∗​(c∗)=(1−αw​α)​c∗b^{\*}(c^{\*})=\left(\frac{1-\alpha}{w\alpha}\right)c^{\*} |  | (A.3.1) |

Setting b∗=b¯b^{\*}=\bar{b} and c∗=c~c^{\*}=\tilde{c}, we solve for c~\tilde{c}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | c~=(w​α1−α)​b¯\tilde{c}=\left(\frac{w\alpha}{1-\alpha}\right)\bar{b} |  | (A.3.2) |

#### A.3.2 Boundary Conditions and The System of Equations

The five unknowns (A2,B1,B2,x~,x∗A\_{2},B\_{1},B\_{2},\tilde{x},x^{\*}) are solved from the following system of five non-linear equations derived from the boundary conditions.

1. 1.

   Continuity at x~\tilde{x} (C2C^{2} Conditions):

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | Vint​(x~;A2)\displaystyle V\_{\text{int}}(\tilde{x};A\_{2}) | =Vb¯​(x~;B1,B2)\displaystyle=V\_{\bar{b}}(\tilde{x};B\_{1},B\_{2}) |  | (A.3.3) |
   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | Vint′​(x~;A2)\displaystyle V^{\prime}\_{\text{int}}(\tilde{x};A\_{2}) | =Vb¯′​(x~;B1,B2)\displaystyle=V^{\prime}\_{\bar{b}}(\tilde{x};B\_{1},B\_{2}) |  | (A.3.4) |
   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | Vint′′​(x~;A2)\displaystyle V^{\prime\prime}\_{\text{int}}(\tilde{x};A\_{2}) | =Vb¯′′​(x~;B1,B2)\displaystyle=V^{\prime\prime}\_{\bar{b}}(\tilde{x};B\_{1},B\_{2}) |  | (A.3.5) |
2. 2.

   Continuity at x∗x^{\*} (C1C^{1} Conditions):

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | Vb¯​(x∗;B1,B2)\displaystyle V\_{\bar{b}}(x^{\*};B\_{1},B\_{2}) | =G​(x∗)\displaystyle=G(x^{\*}) |  | (A.3.6) |
   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | Vb¯′​(x∗;B1,B2)\displaystyle V^{\prime}\_{\bar{b}}(x^{\*};B\_{1},B\_{2}) | =G′​(x∗)\displaystyle=G^{\prime}(x^{\*}) |  | (A.3.7) |

The wealth thresholds x~\tilde{x} and x∗x^{\*} are themselves functions of the constants. This system is typically solved numerically. Below are the explicit forms of the equations for the constants and thresholds derived from these conditions.

### A.4 Proof of Boundary Conditions and Constants

#### A.4.1 Derivation of B1B\_{1}

The constant B1B\_{1} is found by imposing the boundary conditions at x~\tilde{x}. Its solution is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | B1=(β+δt)​c~γ1​m+12​θ2​(m+−m−)​[r−12​θ2​m−β+δt​(1α​k−1k1)​c~−w​b¯r]+11−γ1​(1k1−1α​k)​c~B\_{1}=\frac{(\beta+\delta\_{t})\tilde{c}^{\gamma\_{1}m\_{+}}}{\frac{1}{2}\theta^{2}(m\_{+}-m\_{-})}\left[\frac{r-\frac{1}{2}\theta^{2}m\_{-}}{\beta+\delta\_{t}}\left(\frac{1}{\alpha k}-\frac{1}{k\_{1}}\right)\tilde{c}-\frac{w\bar{b}}{r}\right]+\frac{1}{1-\gamma\_{1}}\left(\frac{1}{k\_{1}}-\frac{1}{\alpha k}\right)\tilde{c} |  | (A.4.1) |

#### A.4.2 Derivation of B2B\_{2}

Similarly, B2B\_{2} is determined from the conditions at x=x∗x=x^{\*}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | B2=\displaystyle B\_{2}= | (β+δt)​k1γ1​m−​(b¯b)−m−​(γ1−γ)12​θ2​(m+−m−)​(x∗)γ1​m−\displaystyle\frac{(\beta+\delta\_{t})k\_{1}^{\gamma\_{1}m\_{-}}\left(\frac{\bar{b}}{b}\right)^{-m\_{-}(\gamma\_{1}-\gamma)}}{\frac{1}{2}\theta^{2}(m\_{+}-m\_{-})}(x^{\*})^{\gamma\_{1}m\_{-}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ×[−r−12​θ2​m+β+δt​{(1−(b¯b)−γ1−γγ1)​x∗+w​(b¯−b)r}+11−γ1​(1−(b¯b)−γ1−γγ1)​x∗]\displaystyle\times\left[-\frac{r-\frac{1}{2}\theta^{2}m\_{+}}{\beta+\delta\_{t}}\left\{\left(1-\left(\frac{\bar{b}}{b}\right)^{-\frac{\gamma\_{1}-\gamma}{\gamma\_{1}}}\right)x^{\*}+\frac{w(\bar{b}-b)}{r}\right\}+\frac{1}{1-\gamma\_{1}}\left(1-\left(\frac{\bar{b}}{b}\right)^{-\frac{\gamma\_{1}-\gamma}{\gamma\_{1}}}\right)x^{\*}\right] |  | (A.4.2) |

#### A.4.3 Derivation of the Constant A2A\_{2}

The constant A2A\_{2} is determined by applying the value-matching and smooth-pasting conditions at the boundary where the consumption-habit ratio is binding, i.e., at wealth x=x~x=\tilde{x}. This yields the following expression for A2A\_{2}:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | A2=\displaystyle A\_{2}= | B2​c~−m−​(γ1−γ)−(β+δt)​c~γ​m−12​θ2​(m+−m−)​[r−12​θ2​m+β+δt​(1k1−1α​k)​c~+w​b¯r]+11−γ1​(1α​k−1k1)​c~\displaystyle B\_{2}\tilde{c}^{-m\_{-}(\gamma\_{1}-\gamma)}-\frac{(\beta+\delta\_{t})\tilde{c}^{\gamma m\_{-}}}{\frac{1}{2}\theta^{2}(m\_{+}-m\_{-})}\left[\frac{r-\frac{1}{2}\theta^{2}m\_{+}}{\beta+\delta\_{t}}\left(\frac{1}{k\_{1}}-\frac{1}{\alpha k}\right)\tilde{c}+\frac{w\bar{b}}{r}\right]+\frac{1}{1-\gamma\_{1}}\left(\frac{1}{\alpha k}-\frac{1}{k\_{1}}\right)\tilde{c} |  | (A.4.3) |

### A.5 Proof of the Equation for the Retirement Threshold x∗x^{\*}

The optimal retirement threshold x∗x^{\*} is determined by ensuring a smooth and optimal transition from the working phase to the retired phase. This involves the value function for the final working state, Vb¯​(x)V\_{\bar{b}}(x), and the retirement value function, G​(x)G(x), both defined in [Theorem 2.2](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem2 "Theorem 2.2 (Value function). ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality").

##### Boundary Conditions.

For the transition to be optimal, the value function must be C1C^{1} (continuously differentiable) across the boundary x∗x^{\*}. This imposes two conditions

1. 1.

   Value Matching: Vb¯​(x∗)=G​(x∗)V\_{\bar{b}}(x^{\*})=G(x^{\*})
2. 2.

   Smooth Pasting: dd​x​Vb¯​(x∗)=dd​x​G​(x∗)\frac{d}{dx}V\_{\bar{b}}(x^{\*})=\frac{d}{dx}G(x^{\*})

##### The Maximized HJB Equation at the Boundary.

As derived in the proof of [Theorem 2.2](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem2 "Theorem 2.2 (Value function). ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality") (Case II), the maximized HJB equation for the region x~≤x<x∗\tilde{x}\leq x<x^{\*} is given by Equation ([A.1.11](https://arxiv.org/html/2510.10371v1#A1.SS1.E11 "Equation A.1.11 ‣ A.1 Proof of Theorem 2.2 (Value Function): ‣ Appendix A Appendix: Proofs of Theorems ‣ Optimal annuitization with labor income under age-dependent force of mortality"))

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρt​Vb¯​(x)=u1​(c∗,b¯)+(r​x−c∗+w​b¯)​Vb¯′​(x)−12​θ2​(Vb¯′​(x))2Vb¯′′​(x)\rho\_{t}V\_{\bar{b}}(x)=u\_{1}(c^{\*},\bar{b})+\left(rx-c^{\*}+w\bar{b}\right)V\_{\bar{b}}^{\prime}(x)-\frac{1}{2}\theta^{2}\frac{(V\_{\bar{b}}^{\prime}(x))^{2}}{V\_{\bar{b}}^{\prime\prime}(x)} |  | (A.5.1) |

This equation must hold for all xx in the interval, including the limit as x→x∗−x\to x^{\*-}. Substituting the boundary conditions into the HJB equation, the core of the proof is to evaluate equation ([A.5.1](https://arxiv.org/html/2510.10371v1#A1.SS5.E1 "Equation A.5.1 ‣ The Maximized HJB Equation at the Boundary. ‣ A.5 Proof of the Equation for the Retirement Threshold 𝑥^∗ ‣ Appendix A Appendix: Proofs of Theorems ‣ Optimal annuitization with labor income under age-dependent force of mortality")) at x=x∗x=x^{\*} and substitute the known properties of the retirement value function G​(x)G(x) using the boundary conditions. The function G​(x)G(x) and its derivatives are given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | G​(x)\displaystyle G(x) | =k1−γ1ρt​(1−γ1)​x1−γ1\displaystyle=\frac{k^{1-\gamma\_{1}}}{\rho\_{t}(1-\gamma\_{1})}x^{1-\gamma\_{1}} |  | (A.5.2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | G′​(x)\displaystyle G^{\prime}(x) | =k1−γ1ρt​x−γ1\displaystyle=\frac{k^{1-\gamma\_{1}}}{\rho\_{t}}x^{-\gamma\_{1}} |  | (A.5.3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | G′′​(x)\displaystyle G^{\prime\prime}(x) | =−γ1​k1−γ1ρt​x−γ1−1\displaystyle=-\gamma\_{1}\frac{k^{1-\gamma\_{1}}}{\rho\_{t}}x^{-\gamma\_{1}-1} |  | (A.5.4) |

By applying the boundary conditions, we substitute Vb¯​(x∗)=G​(x∗)V\_{\bar{b}}(x^{\*})=G(x^{\*}), Vb¯′​(x∗)=G′​(x∗)V^{\prime}\_{\bar{b}}(x^{\*})=G^{\prime}(x^{\*}), and Vb¯′′​(x∗)=G′′​(x∗)V^{\prime\prime}\_{\bar{b}}(x^{\*})=G^{\prime\prime}(x^{\*}) into the HJB equation. The term involving the second derivative simplifies to

|  |  |  |
| --- | --- | --- |
|  | −12​θ2​(Vb¯′​(x∗))2Vb¯′′​(x∗)=−12​θ2​(G′​(x∗))2G′′​(x∗)=θ22​γ1​ρtk1−γ1​x∗-\frac{1}{2}\theta^{2}\frac{(V^{\prime}\_{\bar{b}}(x^{\*}))^{2}}{V^{\prime\prime}\_{\bar{b}}(x^{\*})}=-\frac{1}{2}\theta^{2}\frac{(G^{\prime}(x^{\*}))^{2}}{G^{\prime\prime}(x^{\*})}=\frac{\theta^{2}}{2\gamma\_{1}}\frac{\rho\_{t}}{k^{1-\gamma\_{1}}}x^{\*} |  |

Substituting the full expressions for G​(x∗)G(x^{\*}) and its derivatives into the HJB equation creates a single algebraic equation that depends only on x∗x^{\*}. After significant algebraic simplification and collection of terms (which involve the specific forms of the constants B1,k,m±B\_{1},k,m\_{\pm} derived from the full ODE solution), we arrive at the required non-linear equation for the threshold x∗x^{\*}

|  |  |  |
| --- | --- | --- |
|  | 12​θ2​(m+−m−)β+δt​B1​k−γ1​m+​(bb¯)m+​(γ1−γ)​(x∗)−γ1​m+\displaystyle\frac{\frac{1}{2}\theta^{2}(m\_{+}-m\_{-})}{\beta+\delta\_{t}}B\_{1}k^{-\gamma\_{1}m\_{+}}\left(\frac{b}{\bar{b}}\right)^{m\_{+}(\gamma\_{1}-\gamma)}(x^{\*})^{-\gamma\_{1}m\_{+}} |  |
|  |  |  |
| --- | --- | --- |
|  | =[r−12​θ2​m−β+δt−11−γ1​(1−(bb¯)−γ1−γγ1)]​x∗+r−12​θ2​m−β+δt​w​(b¯−b)r\displaystyle=\left[\frac{r-\frac{1}{2}\theta^{2}m\_{-}}{\beta+\delta\_{t}}-\frac{1}{1-\gamma\_{1}}\left(1-\left(\frac{b}{\bar{b}}\right)^{-\frac{\gamma\_{1}-\gamma}{\gamma\_{1}}}\right)\right]x^{\*}+\frac{r-\frac{1}{2}\theta^{2}m\_{-}}{\beta+\delta\_{t}}\frac{w(\bar{b}-b)}{r} |  |

This completes the derivation.

### A.6 Proof of the Equation for the Labor Constraint Threshold

The threshold x~\tilde{x} marks the boundary between two pre-retirement regions, each with a distinct value function as defined in [Theorem 2.2](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem2 "Theorem 2.2 (Value function). ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality")

* (a)

  Region 1 (x<x~x<\tilde{x}): Interior labor supply, governed by Vint​(x)V\_{\text{int}}(x).
* (b)

  Region 2 (x~≤x<x∗\tilde{x}\leq x<x^{\*}): Corner labor supply (b=b¯b=\bar{b}), governed by Vb¯​(x)V\_{\bar{b}}(x).

To ensure the overall value function is twice continuously differentiable (C2C^{2}), we impose continuity conditions at the boundary x~\tilde{x}.

##### Boundary Conditions.

Let c~\tilde{c} be the consumption level at the boundary x~\tilde{x}. The conditions are:

1. 1.

   Value Matching (C0C^{0}): Vint​(x~)=Vb¯​(x~)V\_{\text{int}}(\tilde{x})=V\_{\bar{b}}(\tilde{x})
2. 2.

   Smooth Pasting (C1C^{1}): dd​x​Vint​(x~)=dd​x​Vb¯​(x~)\frac{d}{dx}V\_{\text{int}}(\tilde{x})=\frac{d}{dx}V\_{\bar{b}}(\tilde{x})
3. 3.

   Second-Order Continuity (C2C^{2}): d2d​x2​Vint​(x~)=d2d​x2​Vb¯​(x~)\frac{d^{2}}{dx^{2}}V\_{\text{int}}(\tilde{x})=\frac{d^{2}}{dx^{2}}V\_{\bar{b}}(\tilde{x})

##### Derivation from the Inverse Value Functions.

In the Proof of Theorem [2.2](https://arxiv.org/html/2510.10371v1#S2.Thmtheorem2 "Theorem 2.2 (Value function). ‣ 2.1 Dynamic Programming Principle ‣ 2 The Market Model ‣ Optimal annuitization with labor income under age-dependent force of mortality"), the HJB equations for each region are solved by transforming them into ODEs for the inverse value functions, x=X​(c)x=X(c). The general solutions are given by equations ([A.1.7](https://arxiv.org/html/2510.10371v1#A1.SS1.E7 "Equation A.1.7 ‣ A.1 Proof of Theorem 2.2 (Value Function): ‣ Appendix A Appendix: Proofs of Theorems ‣ Optimal annuitization with labor income under age-dependent force of mortality")) and ([A.1.13](https://arxiv.org/html/2510.10371v1#A1.SS1.E13 "Equation A.1.13 ‣ A.1 Proof of Theorem 2.2 (Value Function): ‣ Appendix A Appendix: Proofs of Theorems ‣ Optimal annuitization with labor income under age-dependent force of mortality")).
The value-matching condition, Vint​(x~)=Vb¯​(x~)V\_{\text{int}}(\tilde{x})=V\_{\bar{b}}(\tilde{x}), is the key to this proof. It implies that the boundary point (x~,c~)(\tilde{x},\tilde{c}) must lie on the solution curves for both regions. Therefore, the wealth level x~\tilde{x} can be expressed using either inverse function evaluated at the boundary consumption c~\tilde{c}

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | x~\displaystyle\tilde{x} | =Xint​(c~)\displaystyle=X\_{\text{int}}(\tilde{c}) |  | (A.6.1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | x~\displaystyle\tilde{x} | =Xb¯​(c~)\displaystyle=X\_{\bar{b}}(\tilde{c}) |  | (A.6.2) |

Substituting the explicit forms of these solutions, as derived in the proof of the theorem, yields the system of equations presented in the proposition

|  |  |  |  |
| --- | --- | --- | --- |
|  | x~\displaystyle\tilde{x} | =A2​c~−γ​m−+1α​k​c~−w​b¯r=B1​c~−γ1​m++B2​c~−γ1​m−+1k1​c~−w​(b¯−b)r\displaystyle=A\_{2}\tilde{c}^{-\gamma m\_{-}}+\frac{1}{\alpha k}\tilde{c}-\frac{w\bar{b}}{r}=B\_{1}\tilde{c}^{-\gamma\_{1}m\_{+}}+B\_{2}\tilde{c}^{-\gamma\_{1}m\_{-}}+\frac{1}{k\_{1}}\tilde{c}-\frac{w(\bar{b}-b)}{r} |  |

The remaining two conditions (smooth pasting and second-order continuity) provide the necessary equations to solve for the unknown integration constants (A2,B1,B2A\_{2},B\_{1},B\_{2}) in terms of model parameters, closing the system. This completes the proof of how the system for (x~,c~)(\tilde{x},\tilde{c}) is formed.