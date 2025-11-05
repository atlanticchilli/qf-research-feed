---
authors:
- Wilfried Kuissi-Kamdem
doc_id: arxiv:2511.02158v1
family_id: arxiv:2511.02158
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Asset-liability management with Epstein-Zin utility under stochastic interest
  rate and unknown market price of risk
url_abs: http://arxiv.org/abs/2511.02158v1
url_html: https://arxiv.org/html/2511.02158v1
venue: arXiv q-fin
version: 1
year: 2025
---


Wilfried Kuissi-Kamdem
African Institute for Mathematical Sciences, Ghana
Department of Mathematics, University of Rwanda, Rwanda
Department of Mathematical Stochastics, University of Freiburg, Germany
[donatien@aims.edu.gh, wilfried.kuissi.kamdem@stochastik.uni-freiburg.de](mailto:donatien@aims.edu.gh,%20wilfried.kuissi.kamdem@stochastik.uni-freiburg.de)

###### Abstract.

This paper considers a stochastic control problem with Epstein-Zin recursive utility under partial information (unknown market price of risk), in which an investor is constrained to a liability at the end of the investment period. Introducing liabilities is the main novelty of the model and appears for the first time in the literature of recursive utilities. Such constraint leads to a fully coupled forward-backward stochastic differential equation (FBSDE), which well-posedness has not been addressed in the literature. We derive an explicit solution to the FBSDE, contrasting with the existence and uniqueness results with no explicit expression of the solutions typically found in most related literature. Moreover, under minimal additional assumptions, we obtain the Malliavin differentiability of the solution of the FBSDE. We solve the problem completely and find the expression of the controls and the value function. Finally, we determine the utility loss that investors suffer from ignoring the fact that they can learn about the market price of risk.

###### Key words and phrases:

Consumption-portfolio choice; Epstein-Zin utility with liability; Partial information; Forward-backward stochastic differential equations; Malliavin calculus.

###### 2020 Mathematics Subject Classification:

93E11, 93E20, 91G10, 91G20

This work was supported by a grant from the African Institute for Mathematical Sciences, with financial support from the Government of Canada, provided through Global Affairs Canada, and the International Development Research Centre.

## 1. Introduction

The recent decades have seen the prevalence of asset-liability management (ALM) problems in the financial sector (especially with banks, insurance companies and pension funds). This framework enables institutions to mitigate the risk of failing to meet their financial obligations, particularly under adverse market conditions. Similarly, individual investors aim to determine optimal asset allocation strategies that ensure consistency between assets and liabilities while pursuing their profitability objectives. To this end, they continuously adjust their investment portfolios in response to evolving market dynamics and regulatory requirements (see [[14](https://arxiv.org/html/2511.02158v1#bib.bib14)]). However, the literature on ALM problems has so far focused exclusively on either mean-variance criterion or time-additive utilities under full information structure.

The key drawback on the use of time-additive utilities is the fact they restrict the coefficient of risk aversion (which measures the desire to smooth consumption across states of nature) and the coefficient of intertemporal substitutability, EIS, (which measures the desire to smooth consumption over time) to be the inverse of each other, leading to a vast literature on asset pricing paradoxes (see [[21](https://arxiv.org/html/2511.02158v1#bib.bib21), on pp.227-228]). To resolve these paradoxes, Epstein and Zin [[7](https://arxiv.org/html/2511.02158v1#bib.bib7)] introduced the recursive utility. Since then the Epstein-Zin utility has been widely used in a variety of different contexts. However, despite the established and rapid growing literature on consumption and portfolio choice problems with recursive utilities, to the best of our knowledge no research has ever solved such problems in presence of liabilities. The present paper starts to bridge this gap by using an extension of a well-known technique proposed by [[12](https://arxiv.org/html/2511.02158v1#bib.bib12)] (for time-additive utility) and [[21](https://arxiv.org/html/2511.02158v1#bib.bib21)] (for Epstein-Zin utility) to analyse asset-liability management problems with Epstein-Zin preferences under partial information.

There is by now ample evidence in the literature that stock returns are predictable; see [[2](https://arxiv.org/html/2511.02158v1#bib.bib2)] for a review. In [[20](https://arxiv.org/html/2511.02158v1#bib.bib20)] unobservability of the predictive variables was assumed. Since then this assumption has been widely considered in the literature. However, in contrast to the situation for classical time-additive utility preferences (see [[8](https://arxiv.org/html/2511.02158v1#bib.bib8)] for a review), there appears to be only few articles on recursive utility maximisation under partial information. Notable rare exceptions are [[4](https://arxiv.org/html/2511.02158v1#bib.bib4), [15](https://arxiv.org/html/2511.02158v1#bib.bib15)] who study an Epstein-Zin utility maximisation under partial information in different settings with infinite time horizon. Hence, without taking any liability into account.

The main contributions of this paper can summarised to the following:

* 1.1.

  We solve, for the first time, an Epstein-Zin utility maximisation problem with liability at terminal time; see ([2.10](https://arxiv.org/html/2511.02158v1#S2.E10 "In 2.3. The Epstein-Zin utility maximisation problem with partial information ‣ 2. Model and problem formulation ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")). We would like to highlight that the liability may depend on the entire paths of the risky assets. Typical examples of such liabilities are (European option-style) equity-linked securities, convertible bonds, to mention only few. Moreover, we emphasise that even without liability our model is still new in the literature of Epstein-Zin utilities under partial information because it incorporates stochastic volatility.
* 2.2.

  We derive explicit solutions for the optimal consumption, portfolio allocations and value function in a framework featuring recursive utility, stochastic interest rates, stochastic volatility, and return predictability driven by an unobserved factor; see Theorem [3.6](https://arxiv.org/html/2511.02158v1#S3.Thmdefi6 "Theorem 3.6. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk"). Explicit results under partial information with stochastic volatility are rare in general, as they typically require restrictive assumptions on the underlying filtering structure.
* 3.3.

  We determine the utility loss that investors suffer from ignoring the fact that they can learn about the market price of risk; see Section [4](https://arxiv.org/html/2511.02158v1#S4 "4. Utility loss ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk"). Following [[8](https://arxiv.org/html/2511.02158v1#bib.bib8)], we measure the utility loss in terms of the percentage of the initial wealth (the so-called welfare loss). The numerical results show that the welfare loss is an increasing function of the initial wealth of the investors when liabilities are considered, and is independent (meaning, a constant function) of their initial wealth when liabilities are not taken into account. Moreover, the risk aversion coefficient has a negative impact on the welfare loss, whereas the EIS coefficient has a positive impact on the welfare loss.

The remainder of the present paper is structured as follows. We introduce the model and formulate the problem in Section [2](https://arxiv.org/html/2511.02158v1#S2 "2. Model and problem formulation ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk"). In Section [3](https://arxiv.org/html/2511.02158v1#S3 "3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk") we give the main results of this paper. Finally, in Section [4](https://arxiv.org/html/2511.02158v1#S4 "4. Utility loss ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk") we determine the utility loss and perform some numerical analysis.

## 2. Model and problem formulation

We consider a filtered probability space (Ω,𝔽,(ℱt)0≤t≤T,ℙ)(\Omega,\mathbb{F},(\mathcal{F}\_{t})\_{0\leq t\leq T},\mathbb{P}) generated by a standard three dimensional Wiener process W:=(W1,W2,W3)W:=(W^{1},W^{2},W^{3}). The filtration (ℱt)0≤t≤T(\mathcal{F}\_{t})\_{0\leq t\leq T} is assumed to satisfy the usual conditions of completeness and right-continuity.

### 2.1. The financial market

We consider a dynamic financial environment with three traded assets and one non-traded financial index. The traded assets consist of one money market account S0S^{0}, one stock SS and one zero-coupon bond BB maturing at time TT. The money market account follows

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​St0\displaystyle\mathrm{d}S\_{t}^{0} | =rt​St0​d​t,S00>0,\displaystyle=r\_{t}S\_{t}^{0}\mathrm{d}t,~S\_{0}^{0}>0, |  | (2.1) |

with (rt)t∈[0,T](r\_{t})\_{t\in[0,T]} being the stochastic short-term interest rate given by an Ornstein-Uhlenbeck process; that is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​rt\displaystyle\mathrm{d}r\_{t} | =κr​(μr−rt)​d​t+σr​(ρr​S​d​Wt1+1−ρr​S2​d​Wt2),\displaystyle=\kappa\_{r}\big(\mu\_{r}-r\_{t}\big)\mathrm{d}t+\sigma\_{r}\Big(\rho\_{rS}\mathrm{d}W\_{t}^{1}+\sqrt{1-\rho\_{rS}^{2}}\mathrm{d}W\_{t}^{2}\Big), |  | (2.2) |

with correlation coefficient ρr​S∈(−1,1)\rho\_{rS}\in(-1,1), speed of mean reversion κr\kappa\_{r}, long run mean μr\mu\_{r} and volatility σr>0\sigma\_{r}>0.

The zero-coupon bond evolves according to the stochastic differential equation (see [[19](https://arxiv.org/html/2511.02158v1#bib.bib19)])

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Bt=Bt​((rt+μB​(t))​d​t+σB​(t)​(ρr​S​d​Wt1+1−ρr​S2​d​Wt2)),\displaystyle\mathrm{d}B\_{t}=B\_{t}\Big(\big(r\_{t}+\mu\_{B}(t)\big)\mathrm{d}t+\sigma\_{B}(t)\Big(\rho\_{rS}\mathrm{d}W\_{t}^{1}+\sqrt{1-\rho\_{rS}^{2}}\mathrm{d}W\_{t}^{2}\Big)\Big), |  | (2.3) |

with correlation coefficient ρr​S∈(−1,1)\rho\_{rS}\in(-1,1), excess rerun of the bond μB​(t):=ϕB​σB​(t)\mu\_{B}(t):=\phi\_{B}\sigma\_{B}(t) and volatility σB​(t):=σr​1−exp⁡(−κr​(T−t))κr\sigma\_{B}(t):=\sigma\_{r}\frac{1-\exp(-\kappa\_{r}(T-t))}{\kappa\_{r}}. We assume that the investor follows a roll-over strategy for the bond investment and keeps the maturity of the bond in his portfolio constant. This is a common assumption in the literature on portfolio choice with stochastic interest rates; see [[8](https://arxiv.org/html/2511.02158v1#bib.bib8)] and reference therein.

The stock price has dynamics given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​St=St​((rt+β​σ​(t,rt)​Rt)​d​t+σ​(t,rt)​d​Wt1),S0>0,\displaystyle\mathrm{d}S\_{t}=S\_{t}\Big(\big(r\_{t}+\beta\sigma(t,r\_{t})R\_{t}\big)\mathrm{d}t+\sigma(t,r\_{t})\mathrm{d}W\_{t}^{1}\Big),~S\_{0}>0, |  | (2.4) |

with σ\sigma a uniformly positive function and β≠0\beta\neq 0. (Compare with the setup in [[5](https://arxiv.org/html/2511.02158v1#bib.bib5), [8](https://arxiv.org/html/2511.02158v1#bib.bib8)]).

In ([2.4](https://arxiv.org/html/2511.02158v1#S2.E4 "In 2.1. The financial market ‣ 2. Model and problem formulation ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")), RR is an ℝ\mathbb{R}-valued non-traded financial index which follows a linear mean-reverting dynamics given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Rt\displaystyle\mathrm{d}R\_{t} | =κR​(μR−Rt)​d​t+σR​(ρR​S​d​Wt1+ρR​r​d​Wt2+1−ρR​S2−ρR​r2​d​Wt3),\displaystyle=\kappa\_{R}\big(\mu\_{R}-R\_{t}\big)\mathrm{d}t+\sigma\_{R}\Big(\rho\_{RS}\mathrm{d}W\_{t}^{1}+\rho\_{Rr}\mathrm{d}W\_{t}^{2}+\sqrt{1-\rho\_{RS}^{2}-\rho\_{Rr}^{2}}\mathrm{d}W\_{t}^{3}\Big), |  | (2.5) |

with correlation coefficients ρR​S,ρR​r∈[−1,1]\rho\_{RS},\rho\_{Rr}\in[-1,1], speed of mean reversion κR\kappa\_{R}, long run mean μR\mu\_{R} and volatility σR>0\sigma\_{R}>0. In the sequel, following [[8](https://arxiv.org/html/2511.02158v1#bib.bib8)], we assume that ρR​r:=ρ0−ρr​S​ρR​S1−ρr​S2\rho\_{Rr}:=\frac{\rho\_{0}-\rho\_{rS}\rho\_{RS}}{\sqrt{1-\rho\_{rS}^{2}}} for ρ0∈ℝ\rho\_{0}\in\mathbb{R} such that ρR​S2+ρR​r2∈[−1,1]\rho\_{RS}^{2}+\rho\_{Rr}^{2}\in[-1,1]. Hence, the process (Rt)t∈[0,T](R\_{t})\_{t\in[0,T]} plays the role of the market price of risk.

Hence, investors choose the consumption rate ct,t∈[0,T]c\_{t},~t\in[0,T], (according to 𝒞a\mathcal{C}\_{a}) and the amounts πtS\pi\_{t}^{S} and πtB\pi\_{t}^{B} to be invested in the stock and in the bond, respectively. For such (c,πS,πB)(c,\pi^{S},\pi^{B}), the wealth process XX of the investors with initial endowment xx at time 0 evolves according to the stochastic differential equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt\displaystyle\mathrm{d}X\_{t} | =(rt​Xt+πtS​β​σ​(t,rt)​Rt+πtB​ϕB​σB​(t))​d​t+(πtS​σ​(t,rt)+πtB​σB​(t)​ρr​S)​d​Wt1\displaystyle=\Big(r\_{t}X\_{t}+\pi\_{t}^{S}\beta\sigma(t,r\_{t})R\_{t}+\pi\_{t}^{B}\phi\_{B}\sigma\_{B}(t)\Big)\mathrm{d}t+\Big(\pi\_{t}^{S}\sigma(t,r\_{t})+\pi\_{t}^{B}\sigma\_{B}(t)\rho\_{rS}\Big)\mathrm{d}W\_{t}^{1} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +πtB​σB​(t)​1−ρr​S2​d​Wt2−ct​d​t.\displaystyle\phantom{X}+\pi\_{t}^{B}\sigma\_{B}(t)\sqrt{1-\rho\_{rS}^{2}}\mathrm{d}W\_{t}^{2}-c\_{t}\mathrm{d}t. |  | (2.6) |

Note that the market is incomplete (the number of traded assets being less than the number of Wiener processes).

### 2.2. The partial information framework

We assume that the risk premium Rt,t∈[0,T]R\_{t},~t\in[0,T], is not directly observable by the investors. Hence, the investors have no direct information on the return of the stock. The available information flow comes from past realisations/observation of two processes: the stochastic interest rate rr and the stock SS. We
introduce the observation filtration as 𝔽r,S:=𝔽r∨𝔽S\mathbb{F}^{r,S}:=\mathbb{F}^{r}\vee\mathbb{F}^{S}, with 𝔽r:=(ℱtr)0≤t≤T\mathbb{F}^{r}:=(\mathcal{F}\_{t}^{r})\_{0\leq t\leq T} and 𝔽S:=(ℱtS)0≤t≤T\mathbb{F}^{S}:=(\mathcal{F}\_{t}^{S})\_{0\leq t\leq T} being the natural filtration of rr and SS, respectively. We assume that 𝔽r,S\mathbb{F}^{r,S} is completed with ℙ\mathbb{P}-null sets and right-continuous.

We end this section with the definition of some spaces that are used throughout. Let 𝒞\mathcal{C} be the set of 𝔽r,S\mathbb{F}^{r,S}-non-negative progressively measurable processes on [0,T]×Ω[0,T]\times\Omega. For c∈𝒞c\in\mathcal{C} and t<Tt<T, ctc\_{t} denotes the consumption rate at time tt and cTc\_{T} represents a lumpsum consumption at the finite time horizon TT. Let ℒℙq,q≥1\mathcal{L}\_{\mathbb{P}}^{q},~q\geq 1, denotes the space of ℱTr,S\mathcal{F}\_{T}^{r,S}-measurable ℝ\mathbb{R}-valued random variables XX such that 𝔼​[|X|q]<∞\mathbb{E}[|X|^{q}]<\infty. Let ℋℙq,q≥1\mathcal{H}\_{\mathbb{P}}^{q},~q\geq 1, denotes the space of 𝔽r,S\mathbb{F}^{r,S}-predictable ℝ\mathbb{R}-valued processes (Yt)0≤t≤T(Y\_{t})\_{0\leq t\leq T} such that 𝔼​[∫0T|Yt|q​dt]<∞\mathbb{E}[\int\_{0}^{T}|Y\_{t}|^{q}\mathrm{d}t]<\infty. Let ℍℙq,q≥1\mathbb{H}\_{\mathbb{P}}^{q},~q\geq 1, denotes the space of 𝔽r,S\mathbb{F}^{r,S}-predictable ℝ2\mathbb{R}^{2}-valued processes (Zt)0≤t≤T(Z\_{t})\_{0\leq t\leq T} such that 𝔼​[(∫0T|Zt|2​dt)q2]<∞\mathbb{E}[(\int\_{0}^{T}|Z\_{t}|^{2}\mathrm{d}t)^{\frac{q}{2}}]<\infty. Note that similar spaces can and will be defined under another probability measure ℚ\mathbb{Q}, by replacing ℙ\mathbb{P} with ℚ\mathbb{Q} in the subscripts of the corresponding spaces, and taking expectations with respect to ℚ\mathbb{Q}.

### 2.3. The Epstein-Zin utility maximisation problem with partial information

An agent’s preference over 𝒞\mathcal{C}-valued consumption is given by the Epstein-Zin recursive preference. To describe this preference, let δ>0\delta>0 represent the discounting rate, 0<γ≠10<\gamma\neq 1 be the relative risk aversion, and 0<ψ≠10<\psi\neq 1 be the elasticity of intertemporal substitution coefficient (EIS). Then, the Epstein–Zin aggregator is defined by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | f​(c,v)\displaystyle f(c,v) | :=δ​e−δ​t​c1−1ψ1−1ψ​((1−γ)​v)1−1θ, with ​θ:=1−γ1−1ψ,\displaystyle:=\delta e^{-\delta t}\frac{c^{1-\frac{1}{\psi}}}{1-\frac{1}{\psi}}((1-\gamma)v)^{1-\frac{1}{\theta}},\text{ with }~\theta:=\frac{1-\gamma}{1-\frac{1}{\psi}}, |  | (2.7) |

and the bequest utility function by h​(c):=e−δ​θ​T​c1−γ1−γh(c):=e^{-\delta\theta T}\frac{c^{1-\gamma}}{1-\gamma}. Hence, the Epstein-Zin utility over the consumption stream c∈𝒞c\in\mathcal{C} on a finite time horizon TT is a process VcV^{c} which satisfies

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vtc\displaystyle V\_{t}^{c} | =𝔼​[h​(cT)+∫tTf​(cs,Vsc)​ds|ℱt]​ for ​t∈[0,T].\displaystyle=\mathbb{E}\Big[h(c\_{T})+\int\_{t}^{T}f(c\_{s},V\_{s}^{c})\mathrm{d}s~\big|\mathcal{F}\_{t}\Big]~\text{ for }t\in[0,T]. |  | (2.8) |

We consider the following parameter configuration:

|  |  |  |  |
| --- | --- | --- | --- |
|  | either ​γ>1,ψ>1​ or ​γ​ψ=1,γ>1.\displaystyle\text{either }~\gamma>1,\psi>1~\text{ or }~\gamma\psi=1,\gamma>1. |  | (2.9) |

Note that the special case of time-additive Merton CRRA utility corresponds to the condition γ​ψ=1\gamma\psi=1.

###### Definition 2.1.

A consumption stream c∈𝒞c\in\mathcal{C} is said to be admissible if Equation ([2.8](https://arxiv.org/html/2511.02158v1#S2.E8 "In 2.3. The Epstein-Zin utility maximisation problem with partial information ‣ 2. Model and problem formulation ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) admits a unique solution VcV^{c} within the class of processes of class (D)(D) satisfying (1−γ)​Vc>0(1-\gamma)V^{c}>0. The set of all admissible consumption streams is denoted by 𝒞a\mathcal{C}\_{a}.

The set 𝒞a\mathcal{C}\_{a} defined in Definition [2.1](https://arxiv.org/html/2511.02158v1#S2.Thmdefi1 "Definition 2.1. ‣ 2.3. The Epstein-Zin utility maximisation problem with partial information ‣ 2. Model and problem formulation ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk") aligns with those considered in [[16](https://arxiv.org/html/2511.02158v1#bib.bib16), [11](https://arxiv.org/html/2511.02158v1#bib.bib11)]. All known sufficient conditions for the existence of Epstein–Zin utility over a finite time horizon are summarised in [[16](https://arxiv.org/html/2511.02158v1#bib.bib16), Prop. 2.1], which, in particular, ensures that 𝒞a≠∅\mathcal{C}\_{a}\neq\emptyset.

In the present paper, we are interested in the optimal consumption and portfolio choice problem of investors with random liabilities KK at terminal time TT and recursive preferences of Epstein-Zin type. (Note that KK is not necessarily positive). Specifically, we consider liabilties at maturity TT which may depend on the entire paths of the bond BB and the stock SS (such as equity-linked securities, convertible bonds, to mention only few). We assume that the investors only observe the stock with the market price of risk remaining unknown. Therefore, we want to find the best strategy (c∗,πS,∗,πB,∗)(c^{\*},\pi^{S,\*},\pi^{B,\*}) solution to the optimisation problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒱:=sup(c,πS,πB)∈𝒜𝔼​[h​(XT−K)+∫0Tf​(ct,Vtc)​dt],\displaystyle\mathcal{V}:=\sup\_{(c,\pi^{S},\pi^{B})\in\mathcal{A}}~\mathbb{E}\Big[h(X\_{T}-K)+\int\_{0}^{T}f(c\_{t},V\_{t}^{c})\mathrm{d}t\Big], |  | (2.10) |

where 𝒜\mathcal{A} is a subset of the set of ℝ3\mathbb{R}^{3}-valued 𝔽r,S\mathbb{F}^{r,S}-adapted processes. A precise definition of the set 𝒜\mathcal{A} is postponed in Definition [3.2](https://arxiv.org/html/2511.02158v1#S3.Thmdefi2 "Definition 3.2. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk").

A key feature of the stochastic optimisation problem ([2.10](https://arxiv.org/html/2511.02158v1#S2.E10 "In 2.3. The Epstein-Zin utility maximisation problem with partial information ‣ 2. Model and problem formulation ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) is that the supremum is taken over strategies adapted to the observation filtration 𝔽r,S\mathbb{F}^{r,S}, rather than the global filtration 𝔽\mathbb{F}. This places us in the setting of stochastic optimisation under partial information. To address this challenge, we follow the approach of [[10](https://arxiv.org/html/2511.02158v1#bib.bib10)] and introduce an auxiliary separated problem. In the separated formulation, all state variables are adapted to 𝔽r,S\mathbb{F}^{r,S}. Establishing this requires tools from stochastic filtering theory, which will be presented in Section [3.1](https://arxiv.org/html/2511.02158v1#S3.SS1 "3.1. Reduction to the observable filtration ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk"). See [[13](https://arxiv.org/html/2511.02158v1#bib.bib13)] for more details on the subject.

## 3. Main results

### 3.1. Reduction to the observable filtration

Mathematically the financial market is described in terms of a partially observable triple of processes (R,r,S)(R,r,S), where RR is called the unobservable signal, and rr and SS the observation processes. The conditional distribution of RR, given the observation filtration, is defined by 𝔼​[Rt|ℱtr,S]\mathbb{E}\big[R\_{t}~|\mathcal{F}\_{t}^{r,S}\big] for each t∈[0,T]t\in[0,T]. Because the conditional distribution of RR is Gaussian, it is identified by its conditional expectation (mt)t∈[0,T](m\_{t})\_{t\in[0,T]} and conditional variance (vt)t∈[0,T](v\_{t})\_{t\in[0,T]}; that is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | mt\displaystyle m\_{t} | :=𝔼​[Rt|ℱtr,S]​ and ​vt:=𝔼​[(Rt−mt)2|ℱtr,S]​ for ​t∈[0,T].\displaystyle:=\mathbb{E}\big[R\_{t}~|\mathcal{F}\_{t}^{r,S}\big]~\text{ and }~v\_{t}:=\mathbb{E}\big[\big(R\_{t}-m\_{t}\big)^{2}~|\mathcal{F}\_{t}^{r,S}\big]~\text{ for }~t\in[0,T]. |  | (3.1) |

Following [[8](https://arxiv.org/html/2511.02158v1#bib.bib8), Appendix AA], we obtain the following results.

###### Proposition 3.1.

Let the conditional mean-variance pair (mt,vt)t∈[0,T](m\_{t},v\_{t})\_{t\in[0,T]} be defined as in ([3.1](https://arxiv.org/html/2511.02158v1#S3.E1 "In 3.1. Reduction to the observable filtration ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")). Then, (mt,vt),t∈[0,T](m\_{t},v\_{t}),~t\in[0,T], solves the system

|  |  |  |
| --- | --- | --- |
|  | {d​mt=κR​(μR−mt)​d​t+(σR​ρR​S+β​vt)​d​It1+(σR​ρR​r−ρr​S​β​(1−ρr​S2)−12​vt)​d​It2d​vt=(σR2−2​κR​vt−(σR​ρR​S+β​vt)2−(σR​ρR​r−ρr​S​β​(1−ρr​S2)−12​vt)2)​d​t,\displaystyle\begin{cases}\mathrm{d}m\_{t}&=\kappa\_{R}\big(\mu\_{R}-m\_{t}\big)\mathrm{d}t+\big(\sigma\_{R}\rho\_{RS}+\beta v\_{t}\big)\mathrm{d}I\_{t}^{1}+\big(\sigma\_{R}\rho\_{Rr}-\rho\_{rS}\beta(1-\rho\_{rS}^{2})^{-\frac{1}{2}}v\_{t}\big)\mathrm{d}I\_{t}^{2}\\ \mathrm{d}v\_{t}&=\Big(\sigma\_{R}^{2}-2\kappa\_{R}v\_{t}-\big(\sigma\_{R}\rho\_{RS}+\beta v\_{t}\big)^{2}-\big(\sigma\_{R}\rho\_{Rr}-\rho\_{rS}\beta(1-\rho\_{rS}^{2})^{-\frac{1}{2}}v\_{t}\big)^{2}\Big)\mathrm{d}t,\end{cases} |  |

where m0=𝔼​[R0],v0=𝔼​[(R0−m0)2]m\_{0}=\mathbb{E}\big[R\_{0}\big],v\_{0}=\mathbb{E}\big[\big(R\_{0}-m\_{0}\big)^{2}\big] and the ℝ2\mathbb{R}^{2}-valued process I=(It1,It2)t∈[0,T]I=(I\_{t}^{1},I\_{t}^{2})\_{t\in[0,T]}, called the innovation process, given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | It1\displaystyle I\_{t}^{1} | :=Wt1+β​∫0t(Rs−ms)​ds,It2:=Wt2−ρr​S(1−ρr​S2)1/2​β​∫0t(Rs−ms)​ds\displaystyle:=W\_{t}^{1}+\beta\int\_{0}^{t}\big(R\_{s}-m\_{s}\big)\mathrm{d}s,~~I\_{t}^{2}:=W\_{t}^{2}-\frac{\rho\_{rS}}{(1-\rho\_{rS}^{2})^{1/2}}\beta\int\_{0}^{t}\big(R\_{s}-m\_{s}\big)\mathrm{d}s |  | (3.2) |

is a two dimensional Brownian motion under the filtration 𝔽\mathbb{F} and the probability ℙ\mathbb{P}.

###### Proof.

The proof follows similar arguments as in the proof of proposition 11 in [[8](https://arxiv.org/html/2511.02158v1#bib.bib8)] for σλ,κλ,ρS​λ,ρ^λ,ρ^λ​P\sigma\_{\lambda},\kappa\_{\lambda},\rho\_{S\lambda},\hat{\rho}\_{\lambda},\hat{\rho}\_{\lambda P} and ρ^λ​β\hat{\rho}\_{\lambda\beta} therein substituted by 0,0,0,1,00,0,0,1,0 and 0, respectively.
∎

Using the definition of the innovation process, given by ([3.2](https://arxiv.org/html/2511.02158v1#S3.E2 "In Proposition 3.1. ‣ 3.1. Reduction to the observable filtration ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")), we can equivalently write the dynamics of the wealth process (Xt)t∈[0,T](X\_{t})\_{t\in[0,T]} as follows:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Xt\displaystyle\mathrm{d}X\_{t} | =(rt​Xt+πt⊺​ηt)​d​t+πt⊺​d​It−ct​d​t,X0=x,\displaystyle=\Big(r\_{t}X\_{t}+\pi\_{t}^{\intercal}\eta\_{t}\Big)\mathrm{d}t+\pi\_{t}^{\intercal}\mathrm{d}I\_{t}-c\_{t}\mathrm{d}t,~X\_{0}=x, |  | (3.3) |

where Σt:=(σ​(t,rt)0σB​(t)​ρr​SσB​(t)​1−ρr​S2)\Sigma\_{t}:=\begin{pmatrix}\sigma(t,r\_{t})&0\\
\sigma\_{B}(t)\rho\_{rS}&\sigma\_{B}(t)\sqrt{1-\rho\_{rS}^{2}}\end{pmatrix}, μt:=(β​σ​(t,rt)​mtϕB​σB​(t))\mu\_{t}:=\begin{pmatrix}\beta\sigma(t,r\_{t})m\_{t}\\
\phi\_{B}\sigma\_{B}(t)\end{pmatrix}, πt⊺:=(πtS,πtB)​Σt\pi\_{t}^{\intercal}:=(\pi\_{t}^{S},\pi\_{t}^{B})\Sigma\_{t} and ηt:=Σt−1​μt=(β​mt,(1−ρr​S2)−12​(−β​ρr​S​mt+ϕB))⊺\eta\_{t}:=\Sigma\_{t}^{-1}\mu\_{t}=\big(\beta m\_{t},~\big(1-\rho\_{rS}^{2}\big)^{-\frac{1}{2}}\big(-\beta\rho\_{rS}m\_{t}+\phi\_{B}\big)\big)^{\intercal} for t∈[0,T]t\in[0,T].

Note that in ([3.3](https://arxiv.org/html/2511.02158v1#S3.E3 "In 3.1. Reduction to the observable filtration ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) the unobservable market price of risk process (Rt)t∈[0,T](R\_{t})\_{t\in[0,T]} does not appear anymore, and all coefficients are adapted to the observation filtration 𝔽r,S\mathbb{F}^{r,S}.

### 3.2. Solution to the optimisation problem

We start this section by defining the set of admissible consumption-portfolio strategies (c,π)(c,\pi). We introduce the BSDE.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Yt\displaystyle\mathrm{d}Y\_{t} | =−ℋ​(t,Xt,Yt,Zt)​d​t+Zt​d​It,YT=−K​e−∫0Trs​ds,\displaystyle=-\mathcal{H}(t,X\_{t},Y\_{t},Z\_{t})\mathrm{d}t+Z\_{t}\mathrm{d}I\_{t},\quad Y\_{T}=-Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}, |  | (3.4) |

where the generator ℋ\mathcal{H} is to be defined. We define the set of admissible consumption-portfolio strategies as follows.

###### Definition 3.2.

A pair (c,π=(πS,πB))(c,\pi=(\pi^{S},\pi^{B})) of 𝔽r,S\mathbb{F}^{r,S}-adapted consumption-portfolio strategy is admissible if

* (i)(i)

  c∈𝒞ac\in\mathcal{C}\_{a} with cT=XT+e∫0Trs​ds​YTc\_{T}=X\_{T}+e^{\int\_{0}^{T}r\_{s}\mathrm{d}s}Y\_{T};
* (i​i​i)(iii)

  Xt+e∫0trs​ds​Yt>0X\_{t}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t}>0 for all t∈[0,T]t\in[0,T];
* (i​v)(iv)

  (X⋅+e∫0⋅rs​ds​Y⋅)1−γ(X\_{\cdot}+e^{\int\_{0}^{\cdot}r\_{s}\mathrm{d}s}Y\_{\cdot})^{1-\gamma} is of class (D) on [0,T][0,T].

We denote by 𝒜\mathcal{A} the set of admissible consumption-portfolio strategies (compare with the definition of the permissible set in [[21](https://arxiv.org/html/2511.02158v1#bib.bib21), on p.236]).

We speculate that the investor’s optimal utility process takes the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Xt+e∫0trs​ds​Yt)1−γ1−γ​ for ​t∈[0,T].\displaystyle\frac{(X\_{t}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t})^{1-\gamma}}{1-\gamma}~\text{ for }~t\in[0,T]. |  | (3.5) |

Hence we must choose the function ℋ\mathcal{H} in ([3.4](https://arxiv.org/html/2511.02158v1#S3.E4 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) such that the process

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mtc,π:=e−δ​θ​t​(Xt+e∫0trs​ds​Yt)1−γ1−γ+∫0tf​(cs,e−δ​θ​s​(Xs+e∫0sru​du​Ys)1−γ1−γ)​ds\displaystyle M\_{t}^{c,\pi}:={e^{-\delta\theta t}}\frac{(X\_{t}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t})^{1-\gamma}}{1-\gamma}+\int\_{0}^{t}f\big(c\_{s},{e^{-\delta\theta s}}\frac{(X\_{s}+e^{\int\_{0}^{s}r\_{u}\mathrm{d}u}Y\_{s})^{1-\gamma}}{1-\gamma}\big)\mathrm{d}s |  | (3.6) |

for t∈[0,T]t\in[0,T], is a local supermartingale for all (c,π)∈𝒜(c,\pi)\in\mathcal{A} and there exists (c∗,π∗)∈𝒜(c^{\*},\pi^{\*})\in\mathcal{A} such that Mc∗,π∗M^{c^{\*},\pi^{\*}} is a local martingale. Itô’s formula applied to Mc,πM^{c,\pi} gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Mtc,π\displaystyle\mathrm{d}M\_{t}^{c,\pi} | =e−δ​θ​t(Xt+e∫0trs​dsYt)−γ(−ct+δct1−1ψ1−1ψ(Xt+e∫0trs​dsYt)1ψ−e∫0trs​dsZt⊺ηt\displaystyle=e^{-\delta\theta t}(X\_{t}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t})^{-\gamma}\Big(-c\_{t}+\delta\frac{c\_{t}^{1-\frac{1}{\psi}}}{1-\frac{1}{\psi}}(X\_{t}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t})^{\frac{1}{\psi}}-e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Z\_{t}^{\intercal}\eta\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +12​γ​(Xt+e∫0trs​ds​Yt)​‖ηt‖2+rt​(Xt+e∫0trs​ds​Yt)−δ​θ1−γ​(Xt+e∫0trs​ds​Y)\displaystyle+\frac{1}{2\gamma}(X\_{t}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t})\|\eta\_{t}\|^{2}+r\_{t}(X\_{t}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t})-\frac{\delta\theta}{1-\gamma}(X\_{t}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −e∫0trs​dsℋ(t,Xt,Yt,Zt))dt\displaystyle-e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}\mathcal{H}(t,X\_{t},Y\_{t},Z\_{t})\Big)\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −γ2​e−δ​θ​t​(Xt+e∫0trs​ds​Yt)−γ−1​‖πt+(e∫0trs​ds​Zt−1γ​(Xt+e∫0trs​ds​Yt)​ηt)‖2​d​t\displaystyle-\frac{\gamma}{2}e^{-\delta\theta t}(X\_{t}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t})^{-\gamma-1}\Big\|\pi\_{t}+\Big(e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Z\_{t}-\frac{1}{\gamma}(X\_{t}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t})\eta\_{t}\Big)\Big\|^{2}\mathrm{d}t |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +e−δ​θ​t​(Xt+e∫0trs​ds​Yt)−γ​(πt⊺+e∫0trs​ds​Zt⊺)​d​Wt.\displaystyle+e^{-\delta\theta t}(X\_{t}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t})^{-\gamma}\big(\pi\_{t}^{\intercal}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Z\_{t}^{\intercal}\big)\mathrm{d}W\_{t}. |  | (3.7) |

Expecting the drift to be non-positive for any (c,π)∈𝒜(c,\pi)\in\mathcal{A} and zero at an optimal strategy (c∗,π∗)∈𝒜(c^{\*},\pi^{\*})\in\mathcal{A}, we deduce that the candidate optimal portfolio π∗\pi^{\*} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | πt∗=−e∫0trs​ds​Zt+1γ​(Xt+e∫0trs​ds​Yt)​ηt,0≤t<T,\displaystyle\pi\_{t}^{\*}=-e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Z\_{t}+\frac{1}{\gamma}(X\_{t}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t})\eta\_{t},~0\leq t<T, |  | (3.8) |

and the generator ℋ\mathcal{H} in ([3.4](https://arxiv.org/html/2511.02158v1#S3.E4 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℋ​(t,Xt,Yt,Zt)\displaystyle\mathcal{H}(t,X\_{t},Y\_{t},Z\_{t}) | =e−∫0trs​ds​(rt+12​γ​‖ηt‖2−δ​θ1−γ)​(Xt+e∫0trs​ds​Yt)−Zt⊺​ηt\displaystyle=e^{-\int\_{0}^{t}r\_{s}\mathrm{d}s}\Big(r\_{t}+\frac{1}{2\gamma}\|\eta\_{t}\|^{2}{-\frac{\delta\theta}{1-\gamma}}\Big)(X\_{t}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t})-Z\_{t}^{\intercal}\eta\_{t} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +e−∫0trs​ds​maxc>0⁡{−ct+δ​ct1−1ψ1−1ψ​(Xt+e∫0trs​ds​Yt)1ψ}.\displaystyle\phantom{X}+e^{-\int\_{0}^{t}r\_{s}\mathrm{d}s}\max\_{c>0}\Big\{-c\_{t}+\delta\frac{c\_{t}^{1-\frac{1}{\psi}}}{1-\frac{1}{\psi}}(X\_{t}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t})^{\frac{1}{\psi}}\Big\}. |  | (3.9) |

The maximisation in ([3.2](https://arxiv.org/html/2511.02158v1#S3.Ex6 "3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) leads to the candidate optimal consumption c∗c^{\*} given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ct∗=δψ​(Xt+e∫0trs​ds​Yt),0≤t<T.\displaystyle c\_{t}^{\*}=\delta^{\psi}(X\_{t}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t}),~0\leq t<T. |  | (3.10) |

Substituting ([3.10](https://arxiv.org/html/2511.02158v1#S3.E10 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) and ([3.8](https://arxiv.org/html/2511.02158v1#S3.E8 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) into ([3.3](https://arxiv.org/html/2511.02158v1#S3.E3 "In 3.1. Reduction to the observable filtration ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) and ([3.2](https://arxiv.org/html/2511.02158v1#S3.Ex6 "3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")), the generator ℋ\mathcal{H} and the wealth process X=:X∗X=:X^{\*} are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℋ​(t,Xt∗,Yt,Zt)=e−∫0trs​ds​(δψψ−1+rt+12​γ​‖ηt‖2−δ​θ1−γ)​(Xt∗+e∫0trs​ds​Yt)−Zt⊺​ηt\displaystyle\mathcal{H}(t,X\_{t}^{\*},Y\_{t},Z\_{t})=e^{-\int\_{0}^{t}r\_{s}\mathrm{d}s}\Big(\frac{\delta^{\psi}}{\psi-1}+r\_{t}+\frac{1}{2\gamma}\|\eta\_{t}\|^{2}{-\frac{\delta\theta}{1-\gamma}}\Big)(X\_{t}^{\*}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t})-Z\_{t}^{\intercal}\eta\_{t} |  | (3.11) |
|  |  |  |
| --- | --- | --- |
|  | and ​d​Xt∗=(rt​Xt∗+(−δψ+1γ​‖ηt‖2)​(Xt∗+e∫0trs​ds​Yt)−e∫0trs​ds​Zt⊺​ηt)​d​t\displaystyle\text{and }~\mathrm{d}X\_{t}^{\*}=\Big(r\_{t}X\_{t}^{\*}+\big(-\delta^{\psi}+\frac{1}{\gamma}\|\eta\_{t}\|^{2}\big)(X\_{t}^{\*}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t})-e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Z\_{t}^{\intercal}\eta\_{t}\Big)\mathrm{d}t |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | +(1γ​(Xt∗+e∫0trs​ds​Yt)​ηt⊺−e∫0trs​ds​Zt⊺)​d​It,X0∗=x>0.\displaystyle\phantom{XXXXXXx}+\Big(\frac{1}{\gamma}(X\_{t}^{\*}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t})\eta\_{t}^{\intercal}-e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Z\_{t}^{\intercal}\Big)\mathrm{d}I\_{t},\quad X\_{0}^{\*}=x>0. |  | (3.12) |

Therefore, the candidate solution to problem ([2.10](https://arxiv.org/html/2511.02158v1#S2.E10 "In 2.3. The Epstein-Zin utility maximisation problem with partial information ‣ 2. Model and problem formulation ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) is given by ([3.8](https://arxiv.org/html/2511.02158v1#S3.E8 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) and ([3.10](https://arxiv.org/html/2511.02158v1#S3.E10 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")), provided that the coupled FBSDE ([3.4](https://arxiv.org/html/2511.02158v1#S3.E4 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")), ([3.11](https://arxiv.org/html/2511.02158v1#S3.E11 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) and ([3.12](https://arxiv.org/html/2511.02158v1#S3.E12 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) with random coefficients is well-defined in an appropriate function space. To show the well-definedness of the latter FBSDE we consider the following conditions.

###### Assumption 3.3.

* (i)(i)

  𝔼​[exp⁡(4​(2​q+1)2​∫0T‖ηs‖2​ds)]<∞,q≥1\mathbb{E}\Big[\exp\Big(4(2q+1)^{2}\int\_{0}^{T}\|\eta\_{s}\|^{2}\mathrm{d}s\Big)\Big]<\infty,~q\geq 1.
* (i​i)(ii)

  K​exp⁡(−∫0Trs​ds)∈ℒℚ(−1)2​q,q≥1K\exp\Big(-\int\_{0}^{T}r\_{s}\mathrm{d}s\Big)\in\mathcal{L}\_{\mathbb{Q}^{(-1)}}^{2q},~q\geq 1, where ℚ(−1)\mathbb{Q}^{(-1)} is the probability measure equivalent to ℙ\mathbb{P} and defined by d​ℚ(−1)d​ℙ|ℱTr,S:=ℰ​(∫−η⊺​d​I)T:=exp⁡(−12​∫0T‖ηs‖2​ds−∫0Tηs⊺​dIs)\frac{\mathrm{d}\mathbb{Q}^{(-1)}}{\mathrm{d}\mathbb{P}}\big|\_{\mathcal{F}\_{T}^{r,S}}:=\mathcal{E}\big(\int-\eta^{\intercal}\mathrm{d}I\big)\_{T}:=\exp\left(-\frac{1}{2}\int\_{0}^{T}\|\eta\_{s}\|^{2}\mathrm{d}s-\int\_{0}^{T}\eta\_{s}^{\intercal}\mathrm{d}I\_{s}\right).

We define the processes (Ht)t∈[0,T](H\_{t})\_{t\in[0,T]}, (αt)t∈[0,T](\alpha\_{t})\_{t\in[0,T]} and (φt)t∈[0,T](\varphi\_{t})\_{t\in[0,T]} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | {Ht:=ℰ​(∫−η⊺​d​I)t,αt:=e−∫0trs​ds​(δψψ−1+rt+12​γ​‖ηt‖2−δ​θ1−γ)and ​φt:=exp⁡(∫0t(−δψ​ψψ−1+γ−12​γ2​‖ηs‖2+δ​θ1−γ)​ds+1γ​∫0tηs⊺​dIs).\displaystyle\begin{cases}&H\_{t}:=\mathcal{E}\big(\int-\eta^{\intercal}\mathrm{d}I\big)\_{t},\quad\alpha\_{t}:=e^{-\int\_{0}^{t}r\_{s}\mathrm{d}s}\Big(\frac{\delta^{\psi}}{\psi-1}+r\_{t}+\frac{1}{2\gamma}\|\eta\_{t}\|^{2}-\frac{\delta\theta}{1-\gamma}\Big)\\ &\text{and }\varphi\_{t}:=\exp\Big(\int\_{0}^{t}\Big(-\frac{\delta^{\psi}\psi}{\psi-1}+\frac{\gamma-1}{2\gamma^{2}}\|\eta\_{s}\|^{2}+\frac{\delta\theta}{1-\gamma}\Big)\mathrm{d}s+\frac{1}{\gamma}\int\_{0}^{t}\eta\_{s}^{\intercal}\mathrm{d}I\_{s}\Big).\end{cases} |  | (3.13) |

###### Remark 3.4.

Assumption [3.3](https://arxiv.org/html/2511.02158v1#S3.Thmdefi3 "Assumption 3.3. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk") yields α​φ∈ℋℚ(−1)2​q,q≥1\alpha\varphi\in\mathcal{H}\_{\mathbb{Q}^{(-1)}}^{2q},~q\geq 1, (see Appendix [A](https://arxiv.org/html/2511.02158v1#A1 "Appendix A Integrability of 𝛼⁢𝜑 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")). This is used in the existence result of the FBSDE ([3.4](https://arxiv.org/html/2511.02158v1#S3.E4 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")), ([3.11](https://arxiv.org/html/2511.02158v1#S3.E11 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) and ([3.12](https://arxiv.org/html/2511.02158v1#S3.E12 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")); see Proposition [3.5](https://arxiv.org/html/2511.02158v1#S3.Thmdefi5 "Proposition 3.5. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk").

###### Proposition 3.5.

Let x~\widetilde{x} denotes the constant defined by x~:=x−𝔼​[HT​K​e−∫0Trs​ds]1−𝔼​[∫0THs​αs​φs​ds]\widetilde{x}:=\frac{x-\mathbb{E}\big[H\_{T}Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}\big]}{1-\mathbb{E}\big[\int\_{0}^{T}H\_{s}\alpha\_{s}\varphi\_{s}\mathrm{d}s\big]}. Then the FBSDE ([3.4](https://arxiv.org/html/2511.02158v1#S3.E4 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")), ([3.11](https://arxiv.org/html/2511.02158v1#S3.E11 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) and ([3.12](https://arxiv.org/html/2511.02158v1#S3.E12 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) admits a solution (X∗,Y,Z)∈ℋℙq×ℋℙq×ℍℙq,q≥1(X^{\*},Y,Z)\in\mathcal{H}\_{\mathbb{P}}^{q}\times\mathcal{H}\_{\mathbb{P}}^{q}\times\mathbb{H}\_{\mathbb{P}}^{q},~q\geq 1, satisfying

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt∗=x~​φt−e∫0trs​ds​Yt,0≤t≤T,\displaystyle X\_{t}^{\*}=\widetilde{x}\varphi\_{t}-e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t},~0\leq t\leq T, |  | (3.14) |

with (Y,Z)∈ℋℙq×ℍℙq,q≥1(Y,Z)\in\mathcal{H}\_{\mathbb{P}}^{q}\times\mathbb{H}\_{\mathbb{P}}^{q},~q\geq 1, the unique solution to the BSDE

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Yt\displaystyle\mathrm{d}Y\_{t} | =−(x~​αt​φt−Zt​ηt)​d​t+Zt⊺​d​It,YT=−K​e−∫0Trs​ds,\displaystyle=-\Big(\widetilde{x}\alpha\_{t}\varphi\_{t}-Z\_{t}\eta\_{t}\Big)\mathrm{d}t+Z\_{t}^{\intercal}\mathrm{d}I\_{t},~~Y\_{T}=-Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}, |  | (3.15) |

Besides, the expectation representation of the first component YY is given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Yt\displaystyle Y\_{t} | =Ht−1​𝔼​[−HT​K​e−∫0Trs​ds+x~​∫tTHs​αs​φs​ds|ℱtr,S],  0≤t≤T.\displaystyle=H\_{t}^{-1}\mathbb{E}\Big[-H\_{T}Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}+\widetilde{x}\int\_{t}^{T}H\_{s}\alpha\_{s}\varphi\_{s}\mathrm{d}s~|\mathcal{F}\_{t}^{r,S}\Big],\,\,0\leq t\leq T. |  | (3.16) |

###### Proof.

First, we prove that the BSDE ([3.15](https://arxiv.org/html/2511.02158v1#S3.E15 "In Proposition 3.5. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) admits a unique solution (Y,Z)(Y,Z) with YY given by ([3.16](https://arxiv.org/html/2511.02158v1#S3.E16 "In Proposition 3.5. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")). Under ℚ(−1)\mathbb{Q}^{(-1)}, we consider a pair (Y~,Z~)(\tilde{Y},\tilde{Z}) satisfying the BSDE

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Y~t\displaystyle\mathrm{d}\tilde{Y}\_{t} | =−x~​αt​φt​d​t+Z~t⊺​d​Itℚ(−1)=−(x~​αt​φt−Z~t⊺​ηt)​d​t+Z~t⊺​d​It,\displaystyle=-\widetilde{x}\alpha\_{t}\varphi\_{t}\mathrm{d}t+\tilde{Z}\_{t}^{\intercal}\mathrm{d}I\_{t}^{\mathbb{Q}^{(-1)}}=-\Big(\widetilde{x}\alpha\_{t}\varphi\_{t}-\tilde{Z}\_{t}^{\intercal}\eta\_{t}\Big)\mathrm{d}t+\tilde{Z}\_{t}^{\intercal}\mathrm{d}I\_{t}, |  | (3.17) |

with Y~T=−K​e−∫0Trs​ds\tilde{Y}\_{T}=-Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}. Using Remark [3.4](https://arxiv.org/html/2511.02158v1#S3.Thmdefi4 "Remark 3.4. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk") and [[6](https://arxiv.org/html/2511.02158v1#bib.bib6), Thm. 5.1], the BSDE ([3.17](https://arxiv.org/html/2511.02158v1#S3.E17 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) admits a unique solution (Y~,Z~)∈ℋℚ(−1)2​q×ℍℚ(−1)2​q,q≥1(\tilde{Y},\tilde{Z})\in\mathcal{H}\_{\mathbb{Q}^{(-1)}}^{2q}\times\mathbb{H}\_{\mathbb{Q}^{(-1)}}^{2q},~q\geq 1, with the expectation representation of the first component Y~\tilde{Y} being given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y~t\displaystyle\tilde{Y}\_{t} | =𝔼ℚ(−1)​[−K​e−∫0Trs​ds+x~​∫tTαs​φs​ds|ℱtr,S]\displaystyle=\mathbb{E}^{\mathbb{Q}^{(-1)}}\Big[-Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}+\widetilde{x}\int\_{t}^{T}\alpha\_{s}\varphi\_{s}\mathrm{d}s~|\mathcal{F}\_{t}^{r,S}\Big] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =Ht−1​𝔼​[−HT​K​e−∫0Trs​ds+x~​∫tTHs​αs​φs​ds|ℱtr,S],0≤t≤T.\displaystyle=H\_{t}^{-1}\mathbb{E}\Big[-H\_{T}Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}+\widetilde{x}\int\_{t}^{T}H\_{s}\alpha\_{s}\varphi\_{s}\mathrm{d}s~|\mathcal{F}\_{t}^{r,S}\Big],~0\leq t\leq T. |  | (3.18) |

From ([3.17](https://arxiv.org/html/2511.02158v1#S3.E17 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) we deduce that the BSDE ([3.15](https://arxiv.org/html/2511.02158v1#S3.E15 "In Proposition 3.5. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) also admits a unique solution with the expectation representation for the first component of the solution also given by ([3.2](https://arxiv.org/html/2511.02158v1#S3.Ex8 "3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")). Moreover, using repeatedly Cauchy-Schwarz inequality we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0T|Y~t|q​dt]\displaystyle\mathbb{E}\Big[\int\_{0}^{T}|\tilde{Y}\_{t}|^{q}\mathrm{d}t\Big] | ≤(𝔼ℚ(−1)​[HT−2])12​(𝔼ℚ(−1)​[∫0T|Y~t|2​q​dt])12\displaystyle\leq\Big(\mathbb{E}^{\mathbb{Q}^{(-1)}}\Big[H\_{T}^{-2}\Big]\Big)^{\frac{1}{2}}\Big(\mathbb{E}^{\mathbb{Q}^{(-1)}}\Big[\int\_{0}^{T}|\tilde{Y}\_{t}|^{2q}\mathrm{d}t\Big]\Big)^{\frac{1}{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤(𝔼​[exp⁡(3​∫0T‖ηs‖2​ds)])14​(𝔼ℚ(−1)​[∫0T|Y~t|2​q​dt])12<∞,\displaystyle\leq\Big(\mathbb{E}\Big[\exp\Big(3\int\_{0}^{T}\|\eta\_{s}\|^{2}\mathrm{d}s\Big)\Big]\Big)^{\frac{1}{4}}\Big(\mathbb{E}^{\mathbb{Q}^{(-1)}}\Big[\int\_{0}^{T}|\tilde{Y}\_{t}|^{2q}\mathrm{d}t\Big]\Big)^{\frac{1}{2}}<\infty, |  |

where the last inequality holds due to Assumption [3.3](https://arxiv.org/html/2511.02158v1#S3.Thmdefi3 "Assumption 3.3. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk").(i).(i) and the fact that Y~∈ℋℚ(−1)2​q\tilde{Y}\in\mathcal{H}\_{\mathbb{Q}^{(-1)}}^{2q}. Using similar arguments and the fact that Z~∈ℍℚ(−1)2​q\tilde{Z}\in\mathbb{H}\_{\mathbb{Q}^{(-1)}}^{2q}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[(∫0T|Z~s|2​ds)q2]\displaystyle\mathbb{E}\Big[\Big(\int\_{0}^{T}|\tilde{Z}\_{s}|^{2}\mathrm{d}s\Big)^{\frac{q}{2}}\Big] | ≤(𝔼​[exp⁡(3​∫0T‖ηs‖2​ds)])14​(𝔼ℚ(−1)​[(∫0T|Z~s|2​ds)q])12<∞.\displaystyle\leq\Big(\mathbb{E}\Big[\exp\Big(3\int\_{0}^{T}\|\eta\_{s}\|^{2}\mathrm{d}s\Big)\Big]\Big)^{\frac{1}{4}}\Big(\mathbb{E}^{\mathbb{Q}^{(-1)}}\Big[\Big(\int\_{0}^{T}|\tilde{Z}\_{s}|^{2}\mathrm{d}s\Big)^{q}\Big]\Big)^{\frac{1}{2}}<\infty. |  |

Second, we show that the triple (X∗,Y,Z)(X^{\*},Y,Z) satisfying the representation ([3.14](https://arxiv.org/html/2511.02158v1#S3.E14 "In Proposition 3.5. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) is a solution to the FBSDE ([3.4](https://arxiv.org/html/2511.02158v1#S3.E4 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")), ([3.11](https://arxiv.org/html/2511.02158v1#S3.E11 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) and ([3.12](https://arxiv.org/html/2511.02158v1#S3.E12 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")). Clearly, substituting ([3.14](https://arxiv.org/html/2511.02158v1#S3.E14 "In Proposition 3.5. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) into ([3.15](https://arxiv.org/html/2511.02158v1#S3.E15 "In Proposition 3.5. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) gives the BSDE part of the FBSDE. To obtain the SDE part, it suffices to apply Itô’s formula on X∗X^{\*} given by ([3.14](https://arxiv.org/html/2511.02158v1#S3.E14 "In Proposition 3.5. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")).

Finally, we prove that the constant x~\widetilde{x} is finite. By Assumption [3.3](https://arxiv.org/html/2511.02158v1#S3.Thmdefi3 "Assumption 3.3. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk").(i).(i), it suffices to show that 1−𝔼​[∫0THs​αs​φs​ds]≠01-\mathbb{E}\big[\int\_{0}^{T}H\_{s}\alpha\_{s}\varphi\_{s}\mathrm{d}s\big]\neq 0. Indeed, recalling the expressions of α\alpha and φ\varphi from ([3.13](https://arxiv.org/html/2511.02158v1#S3.E13 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) , we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 1−𝔼​[∫0THs​αs​φs​ds]\displaystyle 1-\mathbb{E}\Big[\int\_{0}^{T}H\_{s}\alpha\_{s}\varphi\_{s}\mathrm{d}s\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℚ(1−γγ)​[∫0Tδψ​exp⁡(∫0s(−δψ​ψψ−1−ru−12​γ​‖ηu‖2+δ​θ1−γ)​du)​ds]\displaystyle=\mathbb{E}^{\mathbb{Q}^{(\frac{1-\gamma}{\gamma})}}\Big[\int\_{0}^{T}\delta^{\psi}\exp\Big(\int\_{0}^{s}\big(-\frac{\delta^{\psi}\psi}{\psi-1}-r\_{u}-\frac{1}{2\gamma}\|\eta\_{u}\|^{2}{+\frac{\delta\theta}{1-\gamma}}\big)\mathrm{d}u\Big)\mathrm{d}s\Big] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +𝔼ℚ(1−γγ)​[exp⁡(∫0T(−δψ​ψψ−1−ru−12​γ​‖ηu‖2+δ​θ1−γ)​du)]>0.\displaystyle\phantom{xx}+\mathbb{E}^{\mathbb{Q}^{(\frac{1-\gamma}{\gamma})}}\Big[\exp\Big(\int\_{0}^{T}\big(-\frac{\delta^{\psi}\psi}{\psi-1}-r\_{u}-\frac{1}{2\gamma}\|\eta\_{u}\|^{2}{+\frac{\delta\theta}{1-\gamma}}\big)\mathrm{d}u\Big)\Big]>0. |  | (3.19) |

∎

We are now ready to give the main result of this paper

###### Theorem 3.6.

Assume x>𝔼​[HT​K​e−∫0Trs​ds]x>\mathbb{E}\big[H\_{T}Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}\big] and Assumption [3.3](https://arxiv.org/html/2511.02158v1#S3.Thmdefi3 "Assumption 3.3. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk") holds. Let x~\widetilde{x} be defined as in Proposition [3.5](https://arxiv.org/html/2511.02158v1#S3.Thmdefi5 "Proposition 3.5. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk"). Then the optimal consumption and portfolio strategy for the stochastic optimisation problem ([2.10](https://arxiv.org/html/2511.02158v1#S2.E10 "In 2.3. The Epstein-Zin utility maximisation problem with partial information ‣ 2. Model and problem formulation ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ct∗=δψ​(Xt∗+e∫0trs​ds​Yt)​ and ​πt∗=−e∫0trs​ds​Zt+1γ​(Xt+e∫0trs​ds​Yt)​mt.\displaystyle c\_{t}^{\*}=\delta^{\psi}\big(X\_{t}^{\*}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t}\big)~\text{ and }~\pi\_{t}^{\*}=-e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Z\_{t}+\frac{1}{\gamma}\big(X\_{t}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t}\big)m\_{t}. |  | (3.20) |

In particular, the optimal amount πS,∗\pi^{S,\*} invested in the stock and the optimal amount πB,∗\pi^{B,\*} invested in the bond are given by (πtS,πtB)=πt∗,⊺​Σt−1(\pi\_{t}^{S},\pi\_{t}^{B})=\pi\_{t}^{\*,\intercal}\Sigma\_{t}^{-1} for t∈[0,T]t\in[0,T] (see the definition of Σ\Sigma just below ([2.1](https://arxiv.org/html/2511.02158v1#S2.Ex1 "2.1. The financial market ‣ 2. Model and problem formulation ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk"))).

Besides, the optimal value function of problem ([2.10](https://arxiv.org/html/2511.02158v1#S2.E10 "In 2.3. The Epstein-Zin utility maximisation problem with partial information ‣ 2. Model and problem formulation ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) is given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒱\displaystyle\mathcal{V} | =11−γ​(x−𝔼​[HT​K​e−∫0Trs​ds]1−𝔼​[∫0THs​αs​φs​ds])1−γ.\displaystyle=\frac{1}{1-\gamma}\left(\frac{x-\mathbb{E}\big[H\_{T}Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}\big]}{1-\mathbb{E}\big[\int\_{0}^{T}H\_{s}\alpha\_{s}\varphi\_{s}\mathrm{d}s\big]}\right)^{1-\gamma}. |  | (3.21) |

###### Proof.

First, we prove that (c∗,π∗)∈𝒜(c^{\*},\pi^{\*})\in\mathcal{A}. (Recall 𝒜\mathcal{A} from Definition [3.2](https://arxiv.org/html/2511.02158v1#S3.Thmdefi2 "Definition 3.2. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")). Clearly, Xt∗+e∫0trs​ds​Yt=x~​φt>0,t∈[0,T]X\_{t}^{\*}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t}=\widetilde{x}\varphi\_{t}>0,~t\in[0,T]; due to x>𝔼​[HT​K​e−∫0Trs​ds]x>\mathbb{E}\big[H\_{T}Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}\big] and ([3.2](https://arxiv.org/html/2511.02158v1#S3.Ex12 "3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")). Besides,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (Xt∗+e∫0trs​ds​Yt)1−γ\displaystyle\big(X\_{t}^{\*}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t}\big)^{1-\gamma} | =x~1−γ​exp⁡(∫0t(−δψ​θ​e−δ​θ​ψ​s+δ​θ)​ds)​ℰ​(∫1−γγ​η⊺​dI)t.\displaystyle=\widetilde{x}^{1-\gamma}\exp\Big(\int\_{0}^{t}\big(-\delta^{\psi}\theta e^{-\delta\theta\psi s}{+\delta\theta}\big)\mathrm{d}s\Big)\mathcal{E}\big(\int\frac{1-\gamma}{\gamma}\eta^{\intercal}\mathrm{d}I\big)\_{t}. |  | (3.22) |

Using Assumption [3.3](https://arxiv.org/html/2511.02158v1#S3.Thmdefi3 "Assumption 3.3. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk").(i).(i) with (1−γγ)2<1<4​(2​q+1)2,q≥1\big(\frac{1-\gamma}{\gamma}\big)^{2}<1<4(2q+1)^{2},~q\geq 1, we deduce that ℰ​(∫1−γγ​η⊺​dI)\mathcal{E}\big(\int\frac{1-\gamma}{\gamma}\eta^{\intercal}\mathrm{d}I\big) is a ℙ\mathbb{P}-martingale (hence of class (D)). Thus the right-side of ([3.22](https://arxiv.org/html/2511.02158v1#S3.E22 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) is of class (D) as a product of a bounded deterministic function and a process of class (D). Therefore, (X∗+e∫0rs​ds​Y)1−γ(X^{\*}+e^{\int\_{0}r\_{s}\mathrm{d}s}Y)^{1-\gamma} is of class (D) on [0,T][0,T]. Finally, using [[21](https://arxiv.org/html/2511.02158v1#bib.bib21), Prop. 2.2] and the latter class (D) property, to show that c∈𝒞ac\in\mathcal{C}\_{a} it suffices to prove that 𝔼​[∫0T(Xt∗+e∫0trs​ds​Yt)1−1ψ​dt]<∞\mathbb{E}\big[\int\_{0}^{T}(X\_{t}^{\*}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t})^{1-\frac{1}{\psi}}\mathrm{d}t\big]<\infty. If γ​ψ=1,γ>1\gamma\psi=1,\gamma>1, then the latter inequality follows from ([3.22](https://arxiv.org/html/2511.02158v1#S3.E22 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")). If γ>1,ψ>1\gamma>1,\psi>1, then using successively Cauchy-Schwarz inequality, the inequality exp⁡(∫0t(−δψ+δ1−γ)​ds)≤exp⁡(|δ1−γ|​T)\exp\big(\int\_{0}^{t}\big(-\delta^{\psi}+\frac{\delta}{1-\gamma}\big)\mathrm{d}s\big)\leq\exp\big(\big|\frac{\delta}{1-\gamma}\big|T\big) for t∈[0,T]t\in[0,T], and Assumption [3.3](https://arxiv.org/html/2511.02158v1#S3.Thmdefi3 "Assumption 3.3. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk").(i).(i) with 0<(1−1ψ)​(γ+1γ−2γ​ψ2)<2<4​(2​q+1)20<\big(1-\frac{1}{\psi}\big)\big(\frac{\gamma+1}{\gamma}-\frac{2}{\gamma\psi^{2}}\big)<2<4(2q+1)^{2} and (1−1ψ)2​4γ2<4<4​(2​q+1)2,q≥1\big(1-\frac{1}{\psi}\big)^{2}\frac{4}{\gamma^{2}}<4<4(2q+1)^{2},~q\geq 1, we obtain

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∫0T(Xt∗+e∫0trs​ds​Yt)1−1ψ​dt]\displaystyle\mathbb{E}\Big[\int\_{0}^{T}\big(X\_{t}^{\*}+e^{\int\_{0}^{t}r\_{s}\mathrm{d}s}Y\_{t}\big)^{1-\frac{1}{\psi}}\mathrm{d}t\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤(𝔼​[∫0Texp⁡((1−1ψ)​(γ+1γ−2γ​ψ2)​∫0t‖ηs‖2​ds)​dt])12\displaystyle\leq\Big(\mathbb{E}\Big[\int\_{0}^{T}\exp\Big(\big(1-\frac{1}{\psi}\big)\big(\frac{\gamma+1}{\gamma}-\frac{2}{\gamma\psi^{2}}\big)\int\_{0}^{t}\|\eta\_{s}\|^{2}\mathrm{d}s\Big)\mathrm{d}t\Big]\Big)^{\frac{1}{2}} |  |
|  |  |  |
| --- | --- | --- |
|  | ×(𝔼[∫0Tℰ(∫(1−1ψ)2γη⊺dI)tdt])12exp(|δ1−γ|T)x~1−1ψ<∞.\displaystyle\phantom{xx}\times\Big(\mathbb{E}\Big[\int\_{0}^{T}\mathcal{E}\big(\int\big(1-\frac{1}{\psi}\big)\frac{2}{\gamma}\eta^{\intercal}\mathrm{d}I\big)\_{t}\mathrm{d}t\Big]\Big)^{\frac{1}{2}}\exp\big(\big|\frac{\delta}{1-\gamma}\big|T\big)\widetilde{x}^{1-\frac{1}{\psi}}<\infty. |  |

Second, we show that (c∗,π∗)(c^{\*},\pi^{\*}) is optimal. The proof follows similar arguments as in the proof of proposition 3.23.2 in [[9](https://arxiv.org/html/2511.02158v1#bib.bib9)].
∎

Our next objective is to establish the Malliavin differentiability of the solution to the BSDE ([3.15](https://arxiv.org/html/2511.02158v1#S3.E15 "In Proposition 3.5. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")). We refer the reader to [[17](https://arxiv.org/html/2511.02158v1#bib.bib17)] for clear exposition on the subject. We assume the following conditions.

###### Assumption 3.7.

Let x~,α\widetilde{x},\alpha and φ\varphi be given as in Proposition [3.5](https://arxiv.org/html/2511.02158v1#S3.Thmdefi5 "Proposition 3.5. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk") and Equation ([3.13](https://arxiv.org/html/2511.02158v1#S3.E13 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")).

* (i)(i)

  𝔼​[exp⁡(324​∫0T‖ηs‖2​ds)]<∞\mathbb{E}\Big[\exp\Big(324\int\_{0}^{T}\|\eta\_{s}\|^{2}\mathrm{d}s\Big)\Big]<\infty.
* (i​i)(ii)

  K​e−∫0Trs​ds+x~​∫0Tαs​φs​ds∈𝔻1,2Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}+\widetilde{x}\int\_{0}^{T}\alpha\_{s}\varphi\_{s}\mathrm{d}s\in\mathbb{D}^{1,2}, HT​(K​e−∫0Trs​ds+x~​∫0Tαs​φs​ds)∈𝔻1,2H\_{T}\Big(Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}+\widetilde{x}\int\_{0}^{T}\alpha\_{s}\varphi\_{s}\mathrm{d}s\Big)\in\mathbb{D}^{1,2}.
* (i​i​i)(iii)

  ηt∈𝔻1,2\eta\_{t}\in\mathbb{D}^{1,2} for almost all t∈[0,T]t\in[0,T].
* (i​v)(iv)

  𝔼ℚ(−1)​[|K​e−∫0Trs​ds+x~​∫0Tαs​φs​ds|]<∞\mathbb{E}^{\mathbb{Q}^{(-1)}}\Big[\big|Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}+\widetilde{x}\int\_{0}^{T}\alpha\_{s}\varphi\_{s}\mathrm{d}s\big|\Big]<\infty.
* (v)(v)

  𝔼ℚ(−1)​[∫0T(‖Dt​(−K​e−∫0Trs​ds)‖2+‖x~​Dt​(∫0Tαs​φs​ds)‖2)​dt]<∞\mathbb{E}^{\mathbb{Q}^{(-1)}}\Big[\int\_{0}^{T}\Big(\big\|D\_{t}\big(-Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}\big)\big\|^{2}+\big\|\widetilde{x}D\_{t}\big(\int\_{0}^{T}\alpha\_{s}\varphi\_{s}\mathrm{d}s\big)\big\|^{2}\Big)\mathrm{d}t\Big]<\infty.
* (v​i)(vi)

  (Dt​(αt​φt)−Zt⊺​Dt​(ηt))t∈[0,T]∈ℍℚ(−1)2\big(D\_{t}(\alpha\_{t}\varphi\_{t})-Z\_{t}^{\intercal}D\_{t}(\eta\_{t})\big)\_{t\in[0,T]}\in\mathbb{H}\_{\mathbb{Q}^{(-1)}}^{2}.

Assumptions [3.7](https://arxiv.org/html/2511.02158v1#S3.Thmdefi7 "Assumption 3.7. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk").(ii).(ii)-(i​v)(iv) are required to apply the Clark-Ocone formula to the ℱTr,S\mathcal{F}\_{T}^{r,S}-random variable K​e−∫0Trs​ds+x~​∫0Tαs​φs​dsKe^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}+\widetilde{x}\int\_{0}^{T}\alpha\_{s}\varphi\_{s}\mathrm{d}s under the new measure ℚ(−1)\mathbb{Q}^{(-1)} (compare with [[18](https://arxiv.org/html/2511.02158v1#bib.bib18), Thm. 4.5, Rmk. 4.6]).

###### Proposition 3.8.

Let Assumptions [3.3](https://arxiv.org/html/2511.02158v1#S3.Thmdefi3 "Assumption 3.3. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk") and [3.7](https://arxiv.org/html/2511.02158v1#S3.Thmdefi7 "Assumption 3.7. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk") hold. Then the unique solution (Y,Z)∈ℋℙq×ℍℙq,q≥1(Y,Z)\in\mathcal{H}\_{\mathbb{P}}^{q}\times\mathbb{H}\_{\mathbb{P}}^{q},~q\geq 1, to the BSDE ([3.15](https://arxiv.org/html/2511.02158v1#S3.E15 "In Proposition 3.5. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) is Malliavin differentiable and we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Zt\displaystyle Z\_{t} | =Dt​(Yt),where Dt​(⋅) denote the Malliavin operator for all t∈[0,T].\displaystyle=D\_{t}(Y\_{t}),~\text{where $D\_{t}(\cdot)$ denote the Malliavin operator for all $t\in[0,T]$.} |  | (3.23) |

###### Proof.

We define the processes Y~t:=Yt+x~​∫0tαs​φs​ds\tilde{Y}\_{t}:=Y\_{t}+\widetilde{x}\int\_{0}^{t}\alpha\_{s}\varphi\_{s}\mathrm{d}s and Z~t:=Zt\tilde{Z}\_{t}:=Z\_{t} for t∈[0,T]t\in[0,T]. Hence, (Y~,Z~)(\tilde{Y},\tilde{Z}) is the unique solution to the BSDE

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Y~t\displaystyle\mathrm{d}\tilde{Y}\_{t} | =Z~t⊺​ηt​d​t+Z~t⊺​d​It=Z~t⊺​d​Itℚ(−1),Y~T=−K​e−∫0Trs​ds+x~​∫0Tαs​φs​ds,\displaystyle=\tilde{Z}\_{t}^{\intercal}\eta\_{t}\mathrm{d}t+\tilde{Z}\_{t}^{\intercal}\mathrm{d}I\_{t}=\tilde{Z}\_{t}^{\intercal}\mathrm{d}I\_{t}^{\mathbb{Q}^{(-1)}},~~\tilde{Y}\_{T}=-Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}+\widetilde{x}\int\_{0}^{T}\alpha\_{s}\varphi\_{s}\mathrm{d}s, |  | (3.24) |

where I⋅ℚ(−1):=I⋅+∫0⋅ηs​dsI\_{\cdot}^{\mathbb{Q}^{(-1)}}:=I\_{\cdot}+\int\_{0}^{\cdot}\eta\_{s}\mathrm{d}s is a Brownian motion under ℚ(−1)\mathbb{Q}^{(-1)}. Then

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | −K​e−∫0Trs​ds+x~​∫0Tαs​φs​ds\displaystyle-Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}+\widetilde{x}\int\_{0}^{T}\alpha\_{s}\varphi\_{s}\mathrm{d}s | =Y0+∫0TZ~s⊺​dIsℚ(−1).\displaystyle=Y\_{0}+\int\_{0}^{T}\tilde{Z}\_{s}^{\intercal}\mathrm{d}I\_{s}^{\mathbb{Q}^{(-1)}}. |  | (3.25) |

Using Assumption [3.7](https://arxiv.org/html/2511.02158v1#S3.Thmdefi7 "Assumption 3.7. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk") and applying the Clark-Ocone formula under change of measure as in [[18](https://arxiv.org/html/2511.02158v1#bib.bib18), Thm. 4.5] to Y~T=−K​e−∫0Trs​ds+x~​∫0Tαs​φs​ds∈𝔻1,2\tilde{Y}\_{T}=-Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}+\widetilde{x}\int\_{0}^{T}\alpha\_{s}\varphi\_{s}\mathrm{d}s\in\mathbb{D}^{1,2}, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −K​e−∫0Trs​ds+x~​∫0Tαs​φs​ds\displaystyle-Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}+\widetilde{x}\int\_{0}^{T}\alpha\_{s}\varphi\_{s}\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼ℚ(−1)​[−K​e−∫0Trs​ds+x~​∫0Tαs​φs​ds]\displaystyle=\mathbb{E}^{\mathbb{Q}^{(-1)}}\Big[-Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}+\widetilde{x}\int\_{0}^{T}\alpha\_{s}\varphi\_{s}\mathrm{d}s\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0T𝔼ℚ(−1)[Dt(−Ke−∫0Trs​ds+x~∫0Tαsφsds)\displaystyle\phantom{xx}+\int\_{0}^{T}\mathbb{E}^{\mathbb{Q}^{(-1)}}\Big[D\_{t}\big(-Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}+\widetilde{x}\int\_{0}^{T}\alpha\_{s}\varphi\_{s}\mathrm{d}s\big) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −(−Ke−∫0Trs​ds+x~∫0Tαsφsds)∫tTDt(ηs)dIsℚ(−1)|ℱtr,S]⊺dItℚ(−1).\displaystyle\phantom{xx}-\big(-Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}+\widetilde{x}\int\_{0}^{T}\alpha\_{s}\varphi\_{s}\mathrm{d}s\big)\int\_{t}^{T}D\_{t}(\eta\_{s})\mathrm{d}I\_{s}^{\mathbb{Q}^{(-1)}}~|\mathcal{F}\_{t}^{r,S}\Big]^{\intercal}\mathrm{d}I\_{t}^{\mathbb{Q}^{(-1)}}. |  | (3.26) |

By uniqueness of the solution to the BSDE ([3.24](https://arxiv.org/html/2511.02158v1#S3.E24 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")), we deduce from ([3.25](https://arxiv.org/html/2511.02158v1#S3.E25 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk"))-([3.2](https://arxiv.org/html/2511.02158v1#S3.Ex17 "3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Y0\displaystyle Y\_{0} | =𝔼​[−HT​K​e−∫0Trs​ds+x~​∫0THs​αs​φs​ds]\displaystyle=\mathbb{E}\Big[-H\_{T}Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}+\widetilde{x}\int\_{0}^{T}H\_{s}\alpha\_{s}\varphi\_{s}\mathrm{d}s\Big] |  | (3.27) |

as we already obtained in Proposition [3.5](https://arxiv.org/html/2511.02158v1#S3.Thmdefi5 "Proposition 3.5. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk"), and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zt=Z~t\displaystyle Z\_{t}=\tilde{Z}\_{t} | =𝔼ℚ(−1)[Dt(−Ke−∫0Trs​ds+x~∫0Tαsφsds)\displaystyle=\mathbb{E}^{\mathbb{Q}^{(-1)}}\Big[D\_{t}\big(-Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}+\widetilde{x}\int\_{0}^{T}\alpha\_{s}\varphi\_{s}\mathrm{d}s\big) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −(−Ke−∫0Trs​ds+x~∫0Tαsφsds)∫tTDt(ηs)dIsℚ(−1)|ℱtr,S].\displaystyle\phantom{XXXXx}-\big(-Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}+\widetilde{x}\int\_{0}^{T}\alpha\_{s}\varphi\_{s}\mathrm{d}s\big)\int\_{t}^{T}D\_{t}(\eta\_{s})\mathrm{d}I\_{s}^{\mathbb{Q}^{(-1)}}~|\mathcal{F}\_{t}^{r,S}\Big]. |  | (3.28) |

Besides, we consider the BSDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​Dt​(Yt)=−(x~​Dt​(αt​φt)−Dt​(Zt⊺)​ηt−Zt⊺​Dt​(ηt))​d​t+Dt​(Zt⊺)​d​ItDt​(YT)=Dt​(−K​e−∫0Trs​ds).\displaystyle\begin{cases}\mathrm{d}D\_{t}(Y\_{t})&=-\big(\widetilde{x}D\_{t}(\alpha\_{t}\varphi\_{t})-D\_{t}(Z\_{t}^{\intercal})\eta\_{t}-Z\_{t}^{\intercal}D\_{t}(\eta\_{t})\big)\mathrm{d}t+D\_{t}(Z\_{t}^{\intercal})\mathrm{d}I\_{t}\\ D\_{t}(Y\_{T})&=D\_{t}(-Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}).\end{cases} |  | (3.29) |

Using similar arguments as in the proof of Proposition [3.5](https://arxiv.org/html/2511.02158v1#S3.Thmdefi5 "Proposition 3.5. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk"), we obtain that the BSDE ([3.29](https://arxiv.org/html/2511.02158v1#S3.E29 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) admits a unique solution (Dt​(Yt),Dt​(Zt))t∈[0,T]∈ℋℚ(−1)2×ℍℚ(−1)2(D\_{t}(Y\_{t}),D\_{t}(Z\_{t}))\_{t\in[0,T]}\in\mathcal{H}\_{\mathbb{Q}^{(-1)}}^{2}\times\mathbb{H}\_{\mathbb{Q}^{(-1)}}^{2}, with the expectation representation of the first component (Dt​(Yt))t∈[0,T](D\_{t}(Y\_{t}))\_{t\in[0,T]} being given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Dt​(Yt)\displaystyle D\_{t}(Y\_{t}) | =𝔼ℚ(−1)​[Dt​(−K​e−∫0Trs​ds)+∫tT(x~​Dt​(αs​φs)​d​s−Zs⊺​Dt​(ηs))​ds|ℱtr,S].\displaystyle=\mathbb{E}^{\mathbb{Q}^{(-1)}}\Big[D\_{t}(-Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s})+\int\_{t}^{T}\Big(\widetilde{x}D\_{t}(\alpha\_{s}\varphi\_{s})\mathrm{d}s-Z\_{s}^{\intercal}D\_{t}(\eta\_{s})\Big)\mathrm{d}s~|\mathcal{F}\_{t}^{r,S}\Big]. |  | (3.30) |

Using successively ([3.25](https://arxiv.org/html/2511.02158v1#S3.E25 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")), the fact that Z~t=Zt,t∈[0,T]\tilde{Z}\_{t}=Z\_{t},~t\in[0,T], and Itô isometry we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼ℚ(−1)​[(−K​e−∫0Trs​ds+x~​∫0Tαs​φs​ds)​∫tTDt​(ηs)​dIsℚ(−1)|ℱtr,S]\displaystyle\mathbb{E}^{\mathbb{Q}^{(-1)}}\Big[\big(-Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}+\widetilde{x}\int\_{0}^{T}\alpha\_{s}\varphi\_{s}\mathrm{d}s\big)\int\_{t}^{T}D\_{t}(\eta\_{s})\mathrm{d}I\_{s}^{\mathbb{Q}^{(-1)}}~|\mathcal{F}\_{t}^{r,S}\Big] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =𝔼ℚ(−1)​[∫tTZs⊺​Dt​(ηs)​ds|ℱtr,S].\displaystyle=\mathbb{E}^{\mathbb{Q}^{(-1)}}\Big[\int\_{t}^{T}Z\_{s}^{\intercal}D\_{t}(\eta\_{s})\mathrm{d}s~|\mathcal{F}\_{t}^{r,S}\Big]. |  | (3.31) |

Substituting ([3.2](https://arxiv.org/html/2511.02158v1#S3.Ex21 "3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) into ([3.30](https://arxiv.org/html/2511.02158v1#S3.E30 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) and using the linearity of the operator Dt​(⋅)D\_{t}(\cdot) we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dt​(Yt)\displaystyle D\_{t}(Y\_{t}) | =𝔼ℚ(−1)[Dt(−Ke−∫0Trs​ds+x~∫0Tαsφsds)\displaystyle=\mathbb{E}^{\mathbb{Q}^{(-1)}}\Big[D\_{t}\big(-Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}+\widetilde{x}\int\_{0}^{T}\alpha\_{s}\varphi\_{s}\mathrm{d}s\big) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −(−Ke−∫0Trs​ds+x~∫0Tαsφsds)∫tTDt(ηs)dIsℚ(−1)|ℱtr,S].\displaystyle\phantom{XXXXx}-\big(-Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}+\widetilde{x}\int\_{0}^{T}\alpha\_{s}\varphi\_{s}\mathrm{d}s\big)\int\_{t}^{T}D\_{t}(\eta\_{s})\mathrm{d}I\_{s}^{\mathbb{Q}^{(-1)}}~|\mathcal{F}\_{t}^{r,S}\Big]. |  | (3.32) |

Hence, comparing ([3.2](https://arxiv.org/html/2511.02158v1#S3.Ex20 "3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) and ([3.2](https://arxiv.org/html/2511.02158v1#S3.Ex22 "3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")), we deduce that Zt=Dt​(Yt)Z\_{t}=D\_{t}(Y\_{t}) for t∈[0,T]t\in[0,T].
∎

## 4. Utility loss

In this section, we determine the utility loss that investors suffer from ignoring the fact that they can learn about the market price of risk RR: Instead of learning about RR and using the estimate mm in their optimisation problem, investors use its long-rum mean μR\mu\_{R}. Following [[8](https://arxiv.org/html/2511.02158v1#bib.bib8)], we measure the utility loss in terms of the percentage of the initial wealth. That is, we solve for L∈(0,1)L\in(0,1) the equation 𝒱​(x​(1−L))=𝒱0​(x)\mathcal{V}(x(1-L))=\mathcal{V}^{0}(x), where 𝒱​(x​(1−L))\mathcal{V}(x(1-L)) represents the value function of problem ([2.10](https://arxiv.org/html/2511.02158v1#S2.E10 "In 2.3. The Epstein-Zin utility maximisation problem with partial information ‣ 2. Model and problem formulation ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) for X0=x​(1−L)X\_{0}=x(1-L), and 𝒱0​(x)\mathcal{V}^{0}(x) the value function of problem ([2.10](https://arxiv.org/html/2511.02158v1#S2.E10 "In 2.3. The Epstein-Zin utility maximisation problem with partial information ‣ 2. Model and problem formulation ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) for mt=μR,m\_{t}=\mu\_{R}, t∈[0,T]t\in[0,T]. From Theorem [3.6](https://arxiv.org/html/2511.02158v1#S3.Thmdefi6 "Theorem 3.6. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk"), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | L\displaystyle L | =1−1x​(1−𝔼​[∫0THs​αs​φs​ds]1−𝔼​[∫0THs0​αs0​φs0​ds]​(x−𝔼​[HT0​K​e−∫0Trs​ds])+𝔼​[HT​K​e−∫0Trs​ds]),\displaystyle=1-\frac{1}{x}\left(\frac{1-\mathbb{E}\big[\int\_{0}^{T}H\_{s}\alpha\_{s}\varphi\_{s}\mathrm{d}s\big]}{1-\mathbb{E}\big[\int\_{0}^{T}H\_{s}^{0}\alpha\_{s}^{0}\varphi\_{s}^{0}\mathrm{d}s\big]}\left(x-\mathbb{E}\big[H\_{T}^{0}Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}\big]\right)+\mathbb{E}\big[H\_{T}Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}\big]\right), |  |

where H0,α0H^{0},\alpha^{0}, and φ0\varphi^{0} are given by ([3.13](https://arxiv.org/html/2511.02158v1#S3.E13 "In 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) for mt=μR,t∈[0,T]m\_{t}=\mu\_{R},~t\in[0,T].

In the sequel, for simplicity, we assume a non-negative constant liability KK. Before we provide parameter conditions such that Assumptions [3.3](https://arxiv.org/html/2511.02158v1#S3.Thmdefi3 "Assumption 3.3. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk") and [3.7](https://arxiv.org/html/2511.02158v1#S3.Thmdefi7 "Assumption 3.7. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk") hold, we introduce σm2​(t):=(σR​ρR​S+β​vt)2+(σR​ρR​r−ρr​S​β​(1−ρr​S2)−12​vt)2,Δ​(t):=2​σm2​(t)​ζ−κR2\sigma\_{m}^{2}(t):=\big(\sigma\_{R}\rho\_{RS}+\beta v\_{t}\big)^{2}+\big(\sigma\_{R}\rho\_{Rr}-\rho\_{rS}\beta(1-\rho\_{rS}^{2})^{-\frac{1}{2}}v\_{t}\big)^{2},~\Delta(t):=2\sigma\_{m}^{2}(t)\zeta-\kappa\_{R}^{2}, bm​a​x:=maxt∈[0,T]⁡σm2​(t)b\_{max}:=\max\_{t\in[0,T]}\sigma\_{m}^{2}(t) and Δm​a​x:=2​bm​a​x​ζ−κR2\Delta\_{max}:=2b\_{max}\zeta-\kappa\_{R}^{2}, with ζ:=100​β2​(1−ρr​S2)−1\zeta:=100\beta^{2}(1-\rho\_{rS}^{2})^{-1}.

###### Proposition 4.1.

Suppose that γ,ψ>1\gamma,\psi>1 or γ​ψ=1,γ>1\gamma\psi=1,\gamma>1. Assume that Δm​a​x≤0\Delta\_{max}\leq 0 or Δm​a​x>0,T<(pi−arctan⁡(Δm​a​x/κR))/Δm​a​x\Delta\_{max}>0,~T<\left(\textsl{pi}-\arctan(\sqrt{\Delta\_{max}}/\kappa\_{R})\right)/\sqrt{\Delta\_{max}} hold. Then Assumptions [3.3](https://arxiv.org/html/2511.02158v1#S3.Thmdefi3 "Assumption 3.3. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk") and [3.7](https://arxiv.org/html/2511.02158v1#S3.Thmdefi7 "Assumption 3.7. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk") are satisfied for q=2q=2. Moreover, Assumption [3.7](https://arxiv.org/html/2511.02158v1#S3.Thmdefi7 "Assumption 3.7. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk") also holds if ζ:=324​β2​(1−ρr​S2)−1\zeta:=324\beta^{2}(1-\rho\_{rS}^{2})^{-1}.

###### Proof.

See Appendix [B](https://arxiv.org/html/2511.02158v1#A2 "Appendix B Proof of Proposition 4.1 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk").
∎

In the numerical illustrations, except otherwise stated, the market parameter values are given by
κr=0.5,κR=1.5,μr=0.02,μR=ϕB=ρr​S=0,σr=−0.03,σR=0.2,β=4,ρR​S=−0.95,ρR​r=0.1\kappa\_{r}=0.5,\kappa\_{R}=1.5,\mu\_{r}=0.02,\mu\_{R}=\phi\_{B}=\rho\_{rS}=0,\sigma\_{r}=-0.03,\sigma\_{R}=0.2,\beta=4,\rho\_{RS}=-0.95,\rho\_{Rr}=0.1 and T=1T=1. (All comparative statistics are produced using a Monte Carlo simulation of 10000001000000 paths and averaging them).

![Refer to caption](psi_welfare_loss_initial_wealth.png)

![Refer to caption](gamma_welfare_loss_initial_wealth.png)

Figure 1. Welfare loss LL. Both figures use K=500K=500 and δ=0.08\delta=0.08. The left panel uses γ=5\gamma=5, and the right panel takes ψ=1.5\psi=1.5. The solid lines represent the cases where the estimate, mm, of the risk premium is used and the dashed lines the cases where its long-rum mean, μR\mu\_{R}, is used.

## Acknowledgments

I would like to acknowledge fruitful discussions with Prof. Olivier Menoukeu Pamen.

## Funding

This work was supported by a grant from the African Institute for Mathematical Sciences, with financial support from the Government of Canada, provided through Global Affairs Canada, and the International Development Research Centre.

## Appendix A Integrability of α​φ\alpha\varphi

First, we recall that (see the expression of η\eta just below ([3.3](https://arxiv.org/html/2511.02158v1#S3.E3 "In 3.1. Reduction to the observable filtration ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")))

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖ηt‖2=β21−ρr​S2​mt2−2​β​ρr​S​ϕB1−ρr​S2​mt+ϕB21−ρr​S2​ for ​t∈[0,T].\displaystyle\|\eta\_{t}\|^{2}=\frac{\beta^{2}}{1-\rho\_{rS}^{2}}m\_{t}^{2}-2\frac{\beta\rho\_{rS}\phi\_{B}}{\sqrt{1-\rho\_{rS}^{2}}}m\_{t}+\frac{\phi\_{B}^{2}}{1-\rho\_{rS}^{2}}~\text{ for }~t\in[0,T]. |  | (A.1) |

Hence, using the fact that (mt)t∈[0,T](m\_{t})\_{t\in[0,T]} is an OU process (see Proposition [3.1](https://arxiv.org/html/2511.02158v1#S3.Thmdefi1 "Proposition 3.1. ‣ 3.1. Reduction to the observable filtration ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) and the inequality (∑i=1ℓai)p≤ℓp−1​∑i=1ℓaip\big(\sum\_{i=1}^{\ell}a\_{i}\big)^{p}\leq\ell^{p-1}\sum\_{i=1}^{\ell}a\_{i}^{p} for p≥1,ai>0,i∈{1,⋯,ℓ}p\geq 1,a\_{i}>0,~i\in\{1,\cdots,\ell\}, we deduce that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0T‖ηs‖2​p​ds]+𝔼​[∫0Tmsp​ds]+𝔼​[exp⁡(−p​∫0Tms​ds)]<∞​ for all ​p≥1.\displaystyle\mathbb{E}\Big[\int\_{0}^{T}\|\eta\_{s}\|^{2p}\mathrm{d}s\Big]+\mathbb{E}\Big[\int\_{0}^{T}m\_{s}^{p}\mathrm{d}s\Big]+\mathbb{E}\Big[\exp\Big(-p\int\_{0}^{T}m\_{s}\mathrm{d}s\Big)\Big]<\infty~\text{ for all }~p\geq 1. |  | (A.2) |

Moreover, using the innovation process, given by ([3.2](https://arxiv.org/html/2511.02158v1#S3.E2 "In Proposition 3.1. ‣ 3.1. Reduction to the observable filtration ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")), we obtain that (rt)t∈[0,T](r\_{t})\_{t\in[0,T]}, given by ([2.2](https://arxiv.org/html/2511.02158v1#S2.E2 "In 2.1. The financial market ‣ 2. Model and problem formulation ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")), is again an OU process. Hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0Trsp​ds]+𝔼​[exp⁡(−p​∫0Trs​ds)]<∞​ for all ​p≥1.\displaystyle\mathbb{E}\Big[\int\_{0}^{T}r\_{s}^{p}\mathrm{d}s\Big]+\mathbb{E}\Big[\exp\Big(-p\int\_{0}^{T}r\_{s}\mathrm{d}s\Big)\Big]<\infty~\text{ for all }~p\geq 1. |  | (A.3) |

Next, we compute 𝔼​[HTp]\mathbb{E}\big[H\_{T}^{p}\big], 𝔼​[∫0Tαsp​ds]\mathbb{E}\big[\int\_{0}^{T}\alpha\_{s}^{p}\mathrm{d}s\big] and 𝔼​[∫0Tφsp​ds]\mathbb{E}\big[\int\_{0}^{T}\varphi\_{s}^{p}\mathrm{d}s\big] for p>1p>1. Using Cauchy-Schwarz inequality we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[HTp]\displaystyle\mathbb{E}\big[H\_{T}^{p}\big] | =𝔼​[exp⁡(−p2​∫0T‖ηs‖2​ds−p​∫0Tηs⊺​dIs)]\displaystyle=\mathbb{E}\Big[\exp\Big(-\frac{p}{2}\int\_{0}^{T}\|\eta\_{s}\|^{2}\mathrm{d}s-p\int\_{0}^{T}\eta\_{s}^{\intercal}\mathrm{d}I\_{s}\Big)\Big] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤𝔼​[exp⁡((2​p2−p)​∫0T‖ηs‖2​ds)]+𝔼​[ℰ​(∫−2​p​η⊺​d​I)s].\displaystyle\leq\mathbb{E}\Big[\exp\Big((2p^{2}-p)\int\_{0}^{T}\|\eta\_{s}\|^{2}\mathrm{d}s\Big)\Big]+\mathbb{E}\Big[\mathcal{E}\Big(\int-2p\eta^{\intercal}\mathrm{d}I\Big)\_{s}\Big]. |  | (A.4) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0Tφsp​ds]\displaystyle\mathbb{E}\Big[\int\_{0}^{T}\varphi\_{s}^{p}\mathrm{d}s\Big] | =𝔼[∫0Texp(∫0s(−pδ​ψψ−1+pδ​θ1−γ)ds)\displaystyle=\mathbb{E}\Big[\int\_{0}^{T}\exp\Big(\int\_{0}^{s}\Big(-p\frac{\delta\psi}{\psi-1}+p\frac{\delta\theta}{1-\gamma}\Big)\mathrm{d}s\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×exp(pγ−12​γ2∫0T∥ηs∥2ds+pγ∫0Tηs⊺dIs)]\displaystyle\phantom{XXXX}\times\exp\Big(p\frac{\gamma-1}{2\gamma^{2}}\int\_{0}^{T}\|\eta\_{s}\|^{2}\mathrm{d}s+\frac{p}{\gamma}\int\_{0}^{T}\eta\_{s}^{\intercal}\mathrm{d}I\_{s}\Big)\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤max⁡(1,exp⁡(∫0T(−p​δ​ψψ−1+p​δ​θ1−γ)​ds))\displaystyle\leq\max\Big(1,\exp\Big(\int\_{0}^{T}\Big(-p\frac{\delta\psi}{\psi-1}+p\frac{\delta\theta}{1-\gamma}\Big)\mathrm{d}s\Big)\Big) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ×(𝔼​[∫0Texp⁡(p​γ+2​p2−pγ2​∫0s‖ηu‖2​du)​ds]+𝔼​[∫0Tℰ​(∫2​pγ​η⊺​dI)s​ds]).\displaystyle\times\Big(\mathbb{E}\Big[\int\_{0}^{T}\exp\Big(\frac{p\gamma+2p^{2}-p}{\gamma^{2}}\int\_{0}^{s}\|\eta\_{u}\|^{2}\mathrm{d}u\Big)\mathrm{d}s\Big]+\mathbb{E}\Big[\int\_{0}^{T}\mathcal{E}\Big(\int\frac{2p}{\gamma}\eta^{\intercal}\mathrm{d}I\Big)\_{s}\mathrm{d}s\Big]\Big). |  | (A.5) |

Again, using Cauchy-Schwarz inequality, the convex inequality used for the proof of ([A.2](https://arxiv.org/html/2511.02158v1#A1.E2 "In Appendix A Integrability of 𝛼⁢𝜑 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")), ([A.3](https://arxiv.org/html/2511.02158v1#A1.E3 "In Appendix A Integrability of 𝛼⁢𝜑 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) and ([A.2](https://arxiv.org/html/2511.02158v1#A1.E2 "In Appendix A Integrability of 𝛼⁢𝜑 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0Tαsp​ds]\displaystyle\mathbb{E}\Big[\int\_{0}^{T}\alpha\_{s}^{p}\mathrm{d}s\Big] | ≤𝔼​[exp⁡(−2​p​∫0Trs​ds)]\displaystyle\leq\mathbb{E}\Big[\exp\Big(-2p\int\_{0}^{T}r\_{s}\mathrm{d}s\Big)\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +32​p−1​(T​(δψψ−1−δ​θ1−γ)2​p+𝔼​[∫0Trs2​p​ds]+12​γ​𝔼​[∫0T‖ηs‖4​p​ds])\displaystyle+3^{2p-1}\Big(T\Big(\frac{\delta^{\psi}}{\psi-1}-\frac{\delta\theta}{1-\gamma}\Big)^{2p}+\mathbb{E}\Big[\int\_{0}^{T}r\_{s}^{2p}\mathrm{d}s\Big]+\frac{1}{2\gamma}\mathbb{E}\Big[\int\_{0}^{T}\|\eta\_{s}\|^{4p}\mathrm{d}s\Big]\Big) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | <∞.\displaystyle<\infty. |  | (A.6) |

Note that to show α​φ∈ℋℚ(−1)2​q\alpha\varphi\in\mathcal{H}\_{\mathbb{Q}^{(-1)}}^{2q} for q>1q>1, it suffices to show it for all integer q≥2q\geq 2. Hence, for γ>1\gamma>1 and q≥2q\geq 2 we have (using Jensen inequality, Hölder inequality and Young inequality)

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℚ(−1)​[(∫0T|αs​φs|2​ds)2​q2]≤Tq−1​𝔼ℚ(−1)​[∫0T|αs​φs|2​q​ds]=Tq−1​𝔼​[HT​∫0T|αs​φs|2​q​ds]\displaystyle\mathbb{E}^{\mathbb{Q}^{(-1)}}\Big[\Big(\int\_{0}^{T}|\alpha\_{s}\varphi\_{s}|^{2}\mathrm{d}s\Big)^{\frac{2q}{2}}\Big]\leq T^{q-1}\mathbb{E}^{\mathbb{Q}^{(-1)}}\Big[\int\_{0}^{T}|\alpha\_{s}\varphi\_{s}|^{2q}\mathrm{d}s\Big]=T^{q-1}\mathbb{E}\Big[H\_{T}\int\_{0}^{T}|\alpha\_{s}\varphi\_{s}|^{2q}\mathrm{d}s\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤Tq−1​(𝔼​[HT2​q+1]+T12​q​(𝔼​[∫0Tαs(2​q+1)​(2​q+2)​ds]+𝔼​[∫0Tφs2​q+2​ds])).\displaystyle\leq T^{q-1}\Big(\mathbb{E}\big[H\_{T}^{2q+1}\big]+T^{\frac{1}{2q}}\Big(\mathbb{E}\Big[\int\_{0}^{T}\alpha\_{s}^{(2q+1)(2q+2)}\mathrm{d}s\Big]+\mathbb{E}\Big[\int\_{0}^{T}\varphi\_{s}^{2q+2}\mathrm{d}s\Big]\Big)\Big). |  |

When p=2​q+1p=2q+1, we have 2​p2−p=8​q2+6​q+1<(2​p)2=4​(2​q+1)22p^{2}-p=8q^{2}+6q+1<(2p)^{2}=4(2q+1)^{2} for q≥1q\geq 1. Then using ([A](https://arxiv.org/html/2511.02158v1#A1.Ex1 "Appendix A Integrability of 𝛼⁢𝜑 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) and Assumption [3.3](https://arxiv.org/html/2511.02158v1#S3.Thmdefi3 "Assumption 3.3. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk").(i).(i) we obtain 𝔼​[HT2​q+1]<∞\mathbb{E}\big[H\_{T}^{2q+1}\big]<\infty. When p=2​q+2p=2q+2, we have p​γ+2​p2−pγ2<8​q2+18​q+10<4​(2​q+1)2\frac{p\gamma+2p^{2}-p}{\gamma^{2}}<8q^{2}+18q+10<4(2q+1)^{2} for q≥1q\geq 1. Then using ([A](https://arxiv.org/html/2511.02158v1#A1.Ex2 "Appendix A Integrability of 𝛼⁢𝜑 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) and Assumption [3.3](https://arxiv.org/html/2511.02158v1#S3.Thmdefi3 "Assumption 3.3. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk").(i).(i) we obtain 𝔼​[∫0Tφs2​q+2​ds]<∞\mathbb{E}\big[\int\_{0}^{T}\varphi\_{s}^{2q+2}\mathrm{d}s\big]<\infty. Hence 𝔼ℚ(−1)​[(∫0T|αs​φs|2​ds)2​q2]<∞\mathbb{E}^{\mathbb{Q}^{(-1)}}\Big[\Big(\int\_{0}^{T}|\alpha\_{s}\varphi\_{s}|^{2}\mathrm{d}s\Big)^{\frac{2q}{2}}\Big]<\infty for q≥1q\geq 1.

## Appendix B Proof of Proposition [4.1](https://arxiv.org/html/2511.02158v1#S4.Thmdefi1 "Proposition 4.1. ‣ 4. Utility loss ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")

First, we state and prove three intermediate results (Lemmas [B.1](https://arxiv.org/html/2511.02158v1#A2.Thmdefi1 "Lemma B.1. ‣ Appendix B Proof of Proposition 4.1 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk"), [B.2](https://arxiv.org/html/2511.02158v1#A2.Thmdefi2 "Lemma B.2. ‣ Appendix B Proof of Proposition 4.1 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk") and [B.3](https://arxiv.org/html/2511.02158v1#A2.Thmdefi3 "Lemma B.3. ‣ Appendix B Proof of Proposition 4.1 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) on which the proof of Lemma [4.1](https://arxiv.org/html/2511.02158v1#S4.Thmdefi1 "Proposition 4.1. ‣ 4. Utility loss ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk") will rely on. Lemmas [B.1](https://arxiv.org/html/2511.02158v1#A2.Thmdefi1 "Lemma B.1. ‣ Appendix B Proof of Proposition 4.1 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk") gives the expression of the solution of the Riccati equation given in Proposition [3.1](https://arxiv.org/html/2511.02158v1#S3.Thmdefi1 "Proposition 3.1. ‣ 3.1. Reduction to the observable filtration ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk") and presents the bounds of such solution, Lemma [B.2](https://arxiv.org/html/2511.02158v1#A2.Thmdefi2 "Lemma B.2. ‣ Appendix B Proof of Proposition 4.1 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk") gives a comparison result for some Riccati equations, and Lemma [B.3](https://arxiv.org/html/2511.02158v1#A2.Thmdefi3 "Lemma B.3. ‣ Appendix B Proof of Proposition 4.1 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk") gives sufficient conditions for the non-explosion of the exponential moments of the square of an OU process with constant coefficients.

###### Lemma B.1.

For β≠0\beta\neq 0, the solution vv to the Riccati equation

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | vt′\displaystyle v\_{t}^{\prime} | =σR2−2​κR​vt−(σR​ρR​S+β​vt)2−(σR​ρR​r−ρr​S​β​(1−ρr​S2)−12​vt)2,v0=0\displaystyle=\sigma\_{R}^{2}-2\kappa\_{R}v\_{t}-\big(\sigma\_{R}\rho\_{RS}+\beta v\_{t}\big)^{2}-\big(\sigma\_{R}\rho\_{Rr}-\rho\_{rS}\beta(1-\rho\_{rS}^{2})^{-\frac{1}{2}}v\_{t}\big)^{2},~v\_{0}=0 |  | (B.1) |

is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | vt=(−1a​b24−a​c)​1−k0​exp⁡(−2​t​b24−a​c)1+k0​exp⁡(−2​t​b24−a​c)−b2​a​ for ​t∈[0,T],\displaystyle v\_{t}=\left(-\frac{1}{a}\sqrt{\frac{b^{2}}{4}-ac}\right)\frac{1-k\_{0}\exp\left(-2t\sqrt{\frac{b^{2}}{4}-ac}\right)}{1+k\_{0}\exp\left(-2t\sqrt{\frac{b^{2}}{4}-ac}\right)}-\frac{b}{2a}~\text{ for }~t\in[0,T], |  | (B.2) |

with a:=−β2​(1+ρr​S2​(1−ρr​S2)−1),b:=−2​κR−2​β​σR​ρR​S+2​σR​ρR​r​β​ρr​S​(1−ρr​S2)−1/2a:=-\beta^{2}\big(1+\rho\_{rS}^{2}\big(1-\rho\_{rS}^{2}\big)^{-1}\big),~b:=-2\kappa\_{R}-2\beta\sigma\_{R}\rho\_{RS}+2\sigma\_{R}\rho\_{Rr}\beta\rho\_{rS}\big(1-\rho\_{rS}^{2}\big)^{-1/2}, c:=σR2​(1−ρR​S2−ρR​r2)c:=\sigma\_{R}^{2}\big(1-\rho\_{RS}^{2}-\rho\_{Rr}^{2}\big) and k0:=(1+b2​(b24−a​c)−1/2)​(1−b2​(b24−a​c)−1/2)−1k\_{0}:=\big(1+\frac{b}{2}\big(\frac{b^{2}}{4}-ac\big)^{-1/2}\big)\big(1-\frac{b}{2}\big(\frac{b^{2}}{4}-ac\big)^{-1/2}\big)^{-1}.

Moreover, 0≤vt≤−1a​b24−a​c0\leq v\_{t}\leq-\frac{1}{a}\sqrt{\frac{b^{2}}{4}-ac} for all t∈[0,T]t\in[0,T].

###### Proof.

To check that vv given by ([B.2](https://arxiv.org/html/2511.02158v1#A2.E2 "In Lemma B.1. ‣ Appendix B Proof of Proposition 4.1 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) solves ([B.1](https://arxiv.org/html/2511.02158v1#A2.E1 "In Lemma B.1. ‣ Appendix B Proof of Proposition 4.1 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")), it suffices to differentiate vv and to compare the obtained expression with the right side of ([B.1](https://arxiv.org/html/2511.02158v1#A2.E1 "In Lemma B.1. ‣ Appendix B Proof of Proposition 4.1 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) for vv as in ([B.2](https://arxiv.org/html/2511.02158v1#A2.E2 "In Lemma B.1. ‣ Appendix B Proof of Proposition 4.1 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")). Uniqueness follows from the uniqueness of a solution to a Riccati equation. Observe that a<0a<0. Then b2<b24−a​c\frac{b}{2}<\sqrt{\frac{b^{2}}{4}-ac} and k0>0k\_{0}>0. Having obtained the derivative of vv, we directly have v′​(t)<0v^{\prime}(t)<0 for all t∈[0,T]t\in[0,T] (because k0>0k\_{0}>0). Hence v0=0≤vtv\_{0}=0\leq v\_{t}. Moreover, b2<b24−a​c\frac{b}{2}<\sqrt{\frac{b^{2}}{4}-ac} and k0>0k\_{0}>0 yield vt≤−1a​b24−a​cv\_{t}\leq-\frac{1}{a}\sqrt{\frac{b^{2}}{4}-ac} for all t∈[0,T]t\in[0,T].
∎

###### Lemma B.2.

For v​(t)v(t) defined as in Proposition [3.1](https://arxiv.org/html/2511.02158v1#S3.Thmdefi1 "Proposition 3.1. ‣ 3.1. Reduction to the observable filtration ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk"), let σm2​(t):=(σR​ρR​S+β​vt)2+(σR​ρR​r−ρr​S​β​(1−ρr​S2)−12​vt)2,t∈[0,T]\sigma\_{m}^{2}(t):=\big(\sigma\_{R}\rho\_{RS}+\beta v\_{t}\big)^{2}+\big(\sigma\_{R}\rho\_{Rr}-\rho\_{rS}\beta(1-\rho\_{rS}^{2})^{-\frac{1}{2}}v\_{t}\big)^{2},~t\in[0,T], and bm​a​x2:=maxt∈[0,T]⁡σm2​(t)b\_{max}^{2}:=\max\_{t\in[0,T]}\sigma\_{m}^{2}(t). If g1,g2g\_{1},g\_{2} and g3g\_{3} are solutions on [0,T][0,T] of the ordinary equations

|  |  |  |
| --- | --- | --- |
|  | g1′​(t)=−2​σm2​(t)​g12​(t)+2​κR​g1​(t)−ζ,g2′​(t)=−2​bm​a​x2​g22​(t)+2​κR​g2​(t)−ζ\displaystyle g\_{1}^{\prime}(t)=-2\sigma\_{m}^{2}(t)g\_{1}^{2}(t)+2\kappa\_{R}g\_{1}(t)-\zeta,\quad g\_{2}^{\prime}(t)=-2b\_{max}^{2}g\_{2}^{2}(t)+2\kappa\_{R}g\_{2}(t)-\zeta |  |
|  |  |  |
| --- | --- | --- |
|  | and ​g3′​(t)=2​κR​g3​(t)−ζ\displaystyle\text{and }~g\_{3}^{\prime}(t)=2\kappa\_{R}g\_{3}(t)-\zeta |  |

with g1​(T)=g2​(T)=g3​(T)g\_{1}(T)=g\_{2}(T)=g\_{3}(T), then g3​(t)≤g1​(t)≤g2​(t)g\_{3}(t)\leq g\_{1}(t)\leq g\_{2}(t) for all t∈[0,T]t\in[0,T].

###### Proof.

The proof follows from theorem 4.1.44.1.4 (on p.185185) in [[1](https://arxiv.org/html/2511.02158v1#bib.bib1)].
∎

###### Lemma B.3.

For ζ=512​β2​(1−ρr​S2)−1>0\zeta=512\beta^{2}(1-\rho\_{rS}^{2})^{-1}>0, let Δm​a​x:=2​bm​a​x​ζ−κR2\Delta\_{max}:=2b\_{max}\zeta-\kappa\_{R}^{2}. If Δm​a​x≤0\Delta\_{max}\leq 0 or Δm​a​x>0,T<(pi−arctan⁡(Δm​a​x/κR))/Δm​a​x\Delta\_{max}>0,~T<\left(\textsl{pi}-\arctan(\sqrt{\Delta\_{max}}/\kappa\_{R})\right)/\sqrt{\Delta\_{max}} hold, then 𝔼​[exp⁡(ζ​∫0Tmt2​dt)]<∞\mathbb{E}\left[\exp\left(\zeta\int\_{0}^{T}m\_{t}^{2}\mathrm{d}t\right)\right]<\infty.

###### Proof.

Define u​(t,x):=𝔼​[exp⁡(ζ​∫tTms2​ds)|mt=x]u(t,x):=\mathbb{E}\left[\exp\left(\zeta\int\_{t}^{T}m\_{s}^{2}\mathrm{d}s\right)\big|m\_{t}=x\right]. Then uu satisfies the backward Feynman–Kǎc partial differential equation (PDE):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂u∂t−κR​x​∂u∂x+12​σm2​(t)​∂2u∂x2+ζ​x2​u=0, with ​u​(T,x)=1.\displaystyle\frac{\partial u}{\partial t}-\kappa\_{R}x\frac{\partial u}{\partial x}+\frac{1}{2}\sigma\_{m}^{2}(t)\frac{\partial^{2}u}{\partial x^{2}}+\zeta x^{2}u=0,~\text{ with }~u(T,x)=1. |  | (B.3) |

We make the exponential–quadratic ansatz u​(t,x)=exp⁡(g​(t)​x2+B​(t))u(t,x)=\exp\big(g(t)x^{2}+B(t)\big), with g​(t)=0,B​(T)=0g(t)=0,B(T)=0. Hence, ut=(g′​(t)​x2+B′​(t))​u,ux=2​g​(t)​x​u,ux​x=(2​g​(t)+4​g2​(t)​x2)​uu\_{t}=\big(g^{\prime}(t)x^{2}+B^{\prime}(t)\big)u,u\_{x}=2g(t)xu,~u\_{xx}=(2g(t)+4g^{2}(t)x^{2})u and we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | (g′​(t)−2​κR​g​(t)+2​σm2​(t)​g2​(t)+ζ)​x2+B′​(t)+σm2​(t)​g​(t)=0​ for all ​x∈ℝ.\displaystyle\big(g^{\prime}(t)-2\kappa\_{R}g(t)+2\sigma\_{m}^{2}(t)g^{2}(t)+\zeta\big)x^{2}+B^{\prime}(t)+\sigma\_{m}^{2}(t)g(t)=0~\text{ for all }~x\in\mathbb{R}. |  | (B.4) |

Hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | g′​(t)=−2​σm2​(t)​g2​(t)+2​κR​g​(t)−ζ​ and ​B′​(t)=−σm2​(t)​g​(t).\displaystyle g^{\prime}(t)=-2\sigma\_{m}^{2}(t)g^{2}(t)+2\kappa\_{R}g(t)-\zeta~\text{ and }~B^{\prime}(t)=-\sigma\_{m}^{2}(t)g(t). |  | (B.5) |

Using Lemma [B.3](https://arxiv.org/html/2511.02158v1#A2.Thmdefi3 "Lemma B.3. ‣ Appendix B Proof of Proposition 4.1 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk") we have 0≤ζ2​κR​(exp⁡(2​κR​(T−t))−1)≤g​(t)≤g2​(t)0\leq\frac{\zeta}{2\kappa\_{R}}\left(\exp\big(2\kappa\_{R}(T-t)\big)-1\right)\leq g(t)\leq g\_{2}(t) and B​(t)≤0B(t)\leq 0, with ζ2​κR​(exp⁡(2​κR​(T−t))−1)=g3​(t)\frac{\zeta}{2\kappa\_{R}}\big(\exp\big(2\kappa\_{R}(T-t)\big)-1\big)=g\_{3}(t) for all t∈[0,T]t\in[0,T].

Therefore, from the exponential-quadratic ansatz we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[exp⁡(ζ​∫0Tmt2​dt)]≤exp⁡(g2​(0)​x2).\displaystyle\mathbb{E}\left[\exp\left(\zeta\int\_{0}^{T}m\_{t}^{2}\mathrm{d}t\right)\right]\leq\exp\big(g\_{2}(0)x^{2}\big). |  | (B.6) |

Now, we solve the Riccati equation satisfied by g2g\_{2}. We consider the transformation g2​(t)=12​bm​a​x2​g4′​(t)g4​(t)g\_{2}(t)=\frac{1}{2b\_{max}^{2}}\frac{g\_{4}^{\prime}(t)}{g\_{4}(t)}. Then g2′​(t)=g4′′​(t)​g4​(t)−(g4′​(t))22​bm​a​x2​g42​(t)g\_{2}^{\prime}(t)=\frac{g\_{4}^{\prime\prime}(t)g\_{4}(t)-(g\_{4}^{\prime}(t))^{2}}{2b\_{max}^{2}g\_{4}^{2}(t)}. Hence g4g\_{4} satisfies the linear ODE g4′′=2​κR​g4′−2​bm​a​x2​ζ​g4g\_{4}^{\prime\prime}=2\kappa\_{R}g\_{4}^{\prime}-2b\_{max}^{2}\zeta g\_{4}. Thus,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | g4​(t)\displaystyle g\_{4}(t) | =k1​e(κR+−Δm​a​x)​t+k2​e(κR−−Δm​a​x)​t,with ​Δm​a​x=2​bm​a​x2​ζ−κR2.\displaystyle=k\_{1}e^{(\kappa\_{R}+\sqrt{-\Delta\_{max}})t}+k\_{2}e^{(\kappa\_{R}-\sqrt{-\Delta\_{max}})t},~\text{with }\Delta\_{max}=2b\_{max}^{2}\zeta-\kappa\_{R}^{2}. |  | (B.7) |

Hence

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | g2​(t)\displaystyle g\_{2}(t) | =κR​(k1​e(κR+−Δm​a​x)​t+k2​e(κR−−Δm​a​x)​t)+−Δm​a​x​(k1​e(κR+−Δm​a​x)​t−k2​e(κR−−Δm​a​x)​t)2​bm​a​x2​(k1​e(κR+−Δm​a​x)​t+k2​e(κR−−Δm​a​x)​t).\displaystyle=\frac{\kappa\_{R}\big(k\_{1}e^{(\kappa\_{R}+\sqrt{-\Delta\_{max}})t}+k\_{2}e^{(\kappa\_{R}-\sqrt{-\Delta\_{max}})t}\big)+\sqrt{-\Delta\_{max}}\big(k\_{1}e^{(\kappa\_{R}+\sqrt{-\Delta\_{max}})t}-k\_{2}e^{(\kappa\_{R}-\sqrt{-\Delta\_{max}})t}\big)}{2b\_{max}^{2}\big(k\_{1}e^{(\kappa\_{R}+\sqrt{-\Delta\_{max}})t}+k\_{2}e^{(\kappa\_{R}-\sqrt{-\Delta\_{max}})t}\big)}. |  | (B.8) |

Applying the boundary condition g2​(T)=0g\_{2}(T)=0 to fix the constants k1,k2k\_{1},k\_{2} we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | g2​(0)\displaystyle g\_{2}(0) | =ζ​sinh⁡(T​−Δm​a​x)2​(−Δm​a​x​cosh⁡(T​−Δm​a​x)+κR​sinh⁡(T​−Δm​a​x)).\displaystyle=\frac{\zeta\sinh(T\sqrt{-\Delta\_{max}})}{2\left(\sqrt{-\Delta\_{max}}\cosh(T\sqrt{-\Delta\_{max}})+\kappa\_{R}\sinh(T\sqrt{-\Delta\_{max}})\right)}. |  | (B.9) |

Next, we discuss the finiteness of g2​(0)g\_{2}(0). We obtain the following situations.
  
Case 11: For Δm​a​x<0\Delta\_{max}<0, the denominator of the fraction on the right side of ([B.8](https://arxiv.org/html/2511.02158v1#A2.E8 "In Appendix B Proof of Proposition 4.1 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) does not vanish. Then g2​(0)<∞g\_{2}(0)<\infty.
  
Case 22: For Δm​a​x=0\Delta\_{max}=0, the denominator as well as the numerator of the fraction on the right side of ([B.8](https://arxiv.org/html/2511.02158v1#A2.E8 "In Appendix B Proof of Proposition 4.1 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) vanishes. However, g2​(0)=12​ζ​T​(1+κR​T)−1<∞g\_{2}(0)=\frac{1}{2}\zeta T\big(1+\kappa\_{R}T\big)^{-1}<\infty.
  
Case 33: For Δm​a​x>0\Delta\_{max}>0, the denominator of the fraction on the right side of ([B.8](https://arxiv.org/html/2511.02158v1#A2.E8 "In Appendix B Proof of Proposition 4.1 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) does not vanish for all TT smaller than a critical value TcT\_{c}. Indeed, using the facts that −Δm​a​x=i​Δm​a​x\sqrt{-\Delta\_{max}}=i\sqrt{\Delta\_{max}}, sinh⁡(i​T​Δm​a​x)=i​sin⁡(T​Δm​a​x)\sinh(iT\sqrt{\Delta\_{max}})=i\sin(T\sqrt{\Delta\_{max}}) and cosh⁡(i​T​Δm​a​x)=cos⁡(T​Δm​a​x)\cosh(iT\sqrt{\Delta\_{max}})=\cos(T\sqrt{\Delta\_{max}}) we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | g2​(0)\displaystyle g\_{2}(0) | =ζ​sin⁡(T​Δm​a​x)2​(Δm​a​x​cos⁡(T​Δm​a​x)+κR​sin⁡(T​Δm​a​x)).\displaystyle=\frac{\zeta\sin(T\sqrt{\Delta\_{max}})}{2\left(\sqrt{\Delta\_{max}}\cos(T\sqrt{\Delta\_{max}})+\kappa\_{R}\sin(T\sqrt{\Delta\_{max}})\right)}. |  | (B.10) |

Finding the first positive TT such that Δm​a​x​cos⁡(T​−Δm​a​x)+κR​sin⁡(T​Δm​a​x)=0\sqrt{\Delta\_{max}}\cos(T\sqrt{-\Delta\_{max}})+\kappa\_{R}\sin(T\sqrt{\Delta\_{max}})=0 is equivalent to find the smallest T>0T>0 satisfying tan⁡(T​−Δm​a​x)=Δm​a​xκR\tan(T\sqrt{-\Delta\_{max}})=\frac{\sqrt{\Delta\_{max}}}{\kappa\_{R}}. If we denote by TcT\_{c} such value, then Tc=1Δm​a​x​(pi−arctan⁡(Δm​a​xκR))T\_{c}=\frac{1}{\sqrt{\Delta\_{max}}}\left(\textsl{pi}-\arctan\left(\frac{\sqrt{\Delta\_{max}}}{\kappa\_{R}}\right)\right). Hence, g2​(0)<∞g\_{2}(0)<\infty for all T<TcT<T\_{c}.

Finally, using ([B.6](https://arxiv.org/html/2511.02158v1#A2.E6 "In Appendix B Proof of Proposition 4.1 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) and the results in Cases 11-33 we conclude the proof.
∎

We can now confirm Proposition [4.1](https://arxiv.org/html/2511.02158v1#S4.Thmdefi1 "Proposition 4.1. ‣ 4. Utility loss ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk").

###### Proof of Proposition [4.1](https://arxiv.org/html/2511.02158v1#S4.Thmdefi1 "Proposition 4.1. ‣ 4. Utility loss ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk").

Let us check that Assumptions [3.3](https://arxiv.org/html/2511.02158v1#S3.Thmdefi3 "Assumption 3.3. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk") and [3.7](https://arxiv.org/html/2511.02158v1#S3.Thmdefi7 "Assumption 3.7. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk") are verified for q=2q=2.
  
Assumption [3.3](https://arxiv.org/html/2511.02158v1#S3.Thmdefi3 "Assumption 3.3. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk"): Recall that ζ:=100​β2​(1−ρr​S2)−1\zeta:=100\beta^{2}(1-\rho\_{rS}^{2})^{-1}.

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​[exp⁡(4​(2​q+1)2​∫0T‖ηs‖2​ds)]\displaystyle\mathbb{E}\Big[\exp\Big(4(2q+1)^{2}\int\_{0}^{T}\|\eta\_{s}\|^{2}\mathrm{d}s\Big)\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[exp⁡(100​∫0T(β21−ρr​S2​ms2−2​β​ρr​S​ϕB1−ρr​S2​ms+ϕB21−ρr​S2)​ds)]\displaystyle=\mathbb{E}\Big[\exp\Big(100\int\_{0}^{T}\Big(\frac{\beta^{2}}{1-\rho\_{rS}^{2}}m\_{s}^{2}-2\frac{\beta\rho\_{rS}\phi\_{B}}{\sqrt{1-\rho\_{rS}^{2}}}m\_{s}+\frac{\phi\_{B}^{2}}{1-\rho\_{rS}^{2}}\Big)\mathrm{d}s\Big)\Big] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤e72​ϕB2​(1−ρr​S2)−1​T​(𝔼​[e−200​β​ρr​S​ϕB​(1−ρr​S2)−1/2​∫0Tms​ds])12​(𝔼​[e100​β2​(1−ρr​S2)−1​∫0Tms2​ds])12<∞,\displaystyle\leq e^{72\phi\_{B}^{2}(1-\rho\_{rS}^{2})^{-1}T}\Big(\mathbb{E}\Big[e^{-200\beta\rho\_{rS}\phi\_{B}(1-\rho\_{rS}^{2})^{-1/2}\int\_{0}^{T}m\_{s}\mathrm{d}s}\Big]\Big)^{\frac{1}{2}}\Big(\mathbb{E}\Big[e^{100\beta^{2}(1-\rho\_{rS}^{2})^{-1}\int\_{0}^{T}m\_{s}^{2}\mathrm{d}s}\Big]\Big)^{\frac{1}{2}}<\infty, |  | (B.11) |

where the first inequality holds due to Cauchy-Schwarz inequality and the last inequality comes from ([A.2](https://arxiv.org/html/2511.02158v1#A1.E2 "In Appendix A Integrability of 𝛼⁢𝜑 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")), ([B.6](https://arxiv.org/html/2511.02158v1#A2.E6 "In Appendix B Proof of Proposition 4.1 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")), Lemma [B.3](https://arxiv.org/html/2511.02158v1#A2.Thmdefi3 "Lemma B.3. ‣ Appendix B Proof of Proposition 4.1 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk") and the fact that 100​β2​(1−ρr​S2)−1=ζ100\beta^{2}(1-\rho\_{rS}^{2})^{-1}=\zeta.
  
For Assumption [3.3](https://arxiv.org/html/2511.02158v1#S3.Thmdefi3 "Assumption 3.3. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk").(ii).(ii), with KK constant and d​ℚ(−1)d​ℙ|ℱTr,S=HT\frac{\mathrm{d}\mathbb{Q}^{(-1)}}{\mathrm{d}\mathbb{P}}\big|\_{\mathcal{F}\_{T}^{r,S}}=H\_{T}, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℚ(−1)​[K2​q​exp⁡(−2​q​∫0Trs​ds)]=𝔼​[K​HT​exp⁡(−2​q​∫0Trs​ds)]\displaystyle\mathbb{E}^{\mathbb{Q}^{(-1)}}\Big[K^{2q}\exp\Big(-2q\int\_{0}^{T}r\_{s}\mathrm{d}s\Big)\Big]=\mathbb{E}\Big[KH\_{T}\exp\Big(-2q\int\_{0}^{T}r\_{s}\mathrm{d}s\Big)\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤K​(𝔼​[HT2])1/2​(𝔼​[exp⁡(−4​q​∫0Trs​ds)])1/2\displaystyle\leq K\big(\mathbb{E}\big[H\_{T}^{2}\big]\big)^{1/2}\Big(\mathbb{E}\Big[\exp\Big(-4q\int\_{0}^{T}r\_{s}\mathrm{d}s\Big)\Big]\Big)^{1/2} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤K​(𝔼​[exp⁡(9​∫0T‖ηs‖2​ds)]+𝔼​[ℰ​(∫−4​η⊺​d​I)s])1/2\displaystyle\leq K\Big(\mathbb{E}\Big[\exp\Big(9\int\_{0}^{T}\|\eta\_{s}\|^{2}\mathrm{d}s\Big)\Big]+\mathbb{E}\Big[\mathcal{E}\Big(\int-4\eta^{\intercal}\mathrm{d}I\Big)\_{s}\Big]\Big)^{1/2} |  |
|  |  |  |
| --- | --- | --- |
|  | ×(𝔼​[exp⁡(−8​∫0Trs​ds)])1/2\displaystyle\phantom{Xxx}\times\Big(\mathbb{E}\Big[\exp\Big(-8\int\_{0}^{T}r\_{s}\mathrm{d}s\Big)\Big]\Big)^{1/2} |  |
|  |  |  |
| --- | --- | --- |
|  | <∞,\displaystyle<\infty, |  |

where the first inequality follows from Cauchy-Schwarz inequality, the second inequality comes from ([A](https://arxiv.org/html/2511.02158v1#A1.Ex1 "Appendix A Integrability of 𝛼⁢𝜑 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) and the last inequality holds due to ([A.3](https://arxiv.org/html/2511.02158v1#A1.E3 "In Appendix A Integrability of 𝛼⁢𝜑 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")), ([B](https://arxiv.org/html/2511.02158v1#A2.Ex3 "Appendix B Proof of Proposition 4.1 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) and the fact that 9<16<4​(2​q+1)2=1009<16<4(2q+1)^{2}=100.
  
Assumption [3.7](https://arxiv.org/html/2511.02158v1#S3.Thmdefi7 "Assumption 3.7. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk"): In the sequel, ζ:=324​β2​(1−ρr​S2)−1\zeta:=324\beta^{2}(1-\rho\_{rS}^{2})^{-1}. The proof of Assumption [3.7](https://arxiv.org/html/2511.02158v1#S3.Thmdefi7 "Assumption 3.7. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk").(i).(i) follows similar arguments as in the proof of ([B](https://arxiv.org/html/2511.02158v1#A2.Ex3 "Appendix B Proof of Proposition 4.1 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")). So for brevity it is omitted.

Using [[3](https://arxiv.org/html/2511.02158v1#bib.bib3), Sect. 3.2.2.1 on p.64] we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dt​(ms)\displaystyle D\_{t}\big(m\_{s}\big) | =−1κR(eκR​(s−t)−1)(σR​ρR​S+β​vtσR​ρR​r−ρr​S​β​(1−ρr​S2)−12​vt)𝟙{t<s}=:(Dt(1)​(ms)Dt(2)​(ms))\displaystyle=-\frac{1}{\kappa\_{R}}\big(e^{\kappa\_{R}(s-t)}-1\big)\begin{pmatrix}\sigma\_{R}\rho\_{RS}+\beta v\_{t}\\ \sigma\_{R}\rho\_{Rr}-\rho\_{rS}\beta(1-\rho\_{rS}^{2})^{-\frac{1}{2}}v\_{t}\end{pmatrix}\mathds{1}\_{\{t<s\}}=:\begin{pmatrix}D\_{t}^{(1)}\big(m\_{s}\big)\\ D\_{t}^{(2)}\big(m\_{s}\big)\end{pmatrix} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Dt​(rs)\displaystyle D\_{t}\big(r\_{s}\big) | =−σrκr​(eκr​(s−t)−1)​(ρr​S1−ρr​S2)​𝟙{t<s}\displaystyle=-\frac{\sigma\_{r}}{\kappa\_{r}}\big(e^{\kappa\_{r}(s-t)}-1\big)\begin{pmatrix}\rho\_{rS}\\ \sqrt{1-\rho\_{rS}^{2}}\end{pmatrix}\mathds{1}\_{\{t<s\}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Dt​(e−∫0Trs​ds)\displaystyle D\_{t}\big(e^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}\big) | =−e−∫0Trs​ds​∫tTDt​(rs)​ds\displaystyle=-e^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}\int\_{t}^{T}D\_{t}(r\_{s})\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Dt​(αs)\displaystyle D\_{t}\big(\alpha\_{s}\big) | =Dt​(e−∫0sru​du​(δψψ−1+rs+12​γ​‖ηs‖2−δ​θ1−γ))\displaystyle=D\_{t}\Big(e^{-\int\_{0}^{s}r\_{u}\mathrm{d}u}\Big(\frac{\delta^{\psi}}{\psi-1}+r\_{s}+\frac{1}{2\gamma}\|\eta\_{s}\|^{2}-\frac{\delta\theta}{1-\gamma}\Big)\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(δψψ−1+rs+12​γ​‖ηs‖2−δ​θ1−γ)​Dt​(e−∫0sru​du)\displaystyle=\Big(\frac{\delta^{\psi}}{\psi-1}+r\_{s}+\frac{1}{2\gamma}\|\eta\_{s}\|^{2}-\frac{\delta\theta}{1-\gamma}\Big)D\_{t}\Big(e^{-\int\_{0}^{s}r\_{u}\mathrm{d}u}\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +e−∫0sru​du​Dt​((δψψ−1+rs+12​γ​‖ηs‖2−δ​θ1−γ))\displaystyle\phantom{x}+e^{-\int\_{0}^{s}r\_{u}\mathrm{d}u}D\_{t}\Big(\Big(\frac{\delta^{\psi}}{\psi-1}+r\_{s}+\frac{1}{2\gamma}\|\eta\_{s}\|^{2}-\frac{\delta\theta}{1-\gamma}\Big)\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(δψψ−1+rs+12​γ​‖ηs‖2−δ​θ1−γ)​Dt​(e−∫0Trs​ds)\displaystyle=\Big(\frac{\delta^{\psi}}{\psi-1}+r\_{s}+\frac{1}{2\gamma}\|\eta\_{s}\|^{2}-\frac{\delta\theta}{1-\gamma}\Big)D\_{t}\Big(e^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +e−∫0sru​du​(Dt​(rs)+β2γ​(1−ρr​S2)​ms​Dt​(ms)−β​ρr​S​ϕBγ​1−ρr​S2​Dt​(ms))\displaystyle\phantom{x}+e^{-\int\_{0}^{s}r\_{u}\mathrm{d}u}\Big(D\_{t}\big(r\_{s}\big)+\frac{\beta^{2}}{\gamma(1-\rho\_{rS}^{2})}m\_{s}D\_{t}\big(m\_{s}\big)-\frac{\beta\rho\_{rS}\phi\_{B}}{\gamma\sqrt{1-\rho\_{rS}^{2}}}D\_{t}\big(m\_{s}\big)\Big) |  |

Using Young inequality, ([A.2](https://arxiv.org/html/2511.02158v1#A1.E2 "In Appendix A Integrability of 𝛼⁢𝜑 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")), ([A.3](https://arxiv.org/html/2511.02158v1#A1.E3 "In Appendix A Integrability of 𝛼⁢𝜑 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) and ([A](https://arxiv.org/html/2511.02158v1#A1.Ex5 "Appendix A Integrability of 𝛼⁢𝜑 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∫0T‖Dt​(e−∫0Trs​ds)‖p​dt]+𝔼​[∫0T(∫tT‖Dt​(αs)‖p​ds)​dt]<∞​ for all ​p≥1.\displaystyle\mathbb{E}\Big[\int\_{0}^{T}\big\|D\_{t}\big(e^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}\big)\big\|^{p}\mathrm{d}t\Big]+\mathbb{E}\Big[\int\_{0}^{T}\Big(\int\_{t}^{T}\|D\_{t}\big(\alpha\_{s}\big)\|^{p}\mathrm{d}s\Big)\mathrm{d}t\Big]<\infty\text{ for all }p\geq 1. |  | (B.12) |

Besides,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dt​(φs)\displaystyle D\_{t}\big(\varphi\_{s}\big) | =φs​(∫ts((γ−1)​β2γ2​(1−ρr​S2)​ms​Dt​(mu)−(γ−1)​β​ρr​S​ϕBγ2​1−ρr​S2​Dt​(mu))​du)\displaystyle=\varphi\_{s}\Big(\int\_{t}^{s}\Big(\frac{(\gamma-1)\beta^{2}}{\gamma^{2}(1-\rho\_{rS}^{2})}m\_{s}D\_{t}\big(m\_{u}\big)-\frac{(\gamma-1)\beta\rho\_{rS}\phi\_{B}}{\gamma^{2}\sqrt{1-\rho\_{rS}^{2}}}D\_{t}\big(m\_{u}\big)\Big)\mathrm{d}u\Big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +φs​(1γ​ηt+∫ts(βγ​Dt(1)​(mu)00−β​ρr​Sγ​1−ρr​S2​Dt(2)​(mu))​dIu).\displaystyle\phantom{x}+\varphi\_{s}\left(\frac{1}{\gamma}\eta\_{t}+\int\_{t}^{s}\begin{pmatrix}\frac{\beta}{\gamma}D\_{t}^{(1)}\big(m\_{u}\big)&0\\ 0&-\frac{\beta\rho\_{rS}}{\gamma\sqrt{1-\rho\_{rS}^{2}}}D\_{t}^{(2)}\big(m\_{u}\big)\end{pmatrix}\mathrm{d}I\_{u}\right). |  |

Using successively Young inequality, Jensen inequality and Burkholder–Davis–Gundy (BDG) inequality we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​[∫0T(∫tT‖Dt​(φs)‖p​ds)​dt]\displaystyle\mathbb{E}\Big[\int\_{0}^{T}\Big(\int\_{t}^{T}\|D\_{t}\big(\varphi\_{s}\big)\|^{p}\mathrm{d}s\Big)\mathrm{d}t\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼​[∫0T(∫tTφsp+1​ds)​dt]\displaystyle\leq\mathbb{E}\Big[\int\_{0}^{T}\Big(\int\_{t}^{T}\varphi\_{s}^{p+1}\mathrm{d}s\Big)\mathrm{d}t\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +((γ−1)​β2γ2​(1−ρr​S2))p​(p+1)​𝔼​[∫0T(s−t)p​(p+1)−1​msp​(p+1)​(∫ts‖Dt​(mu)‖p​(p+1)​du)​dt]\displaystyle+\Big(\frac{(\gamma-1)\beta^{2}}{\gamma^{2}(1-\rho\_{rS}^{2})}\Big)^{p(p+1)}\mathbb{E}\Big[\int\_{0}^{T}(s-t)^{p(p+1)-1}m\_{s}^{p(p+1)}\Big(\int\_{t}^{s}\|D\_{t}\big(m\_{u}\big)\|^{p(p+1)}\mathrm{d}u\Big)\mathrm{d}t\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +((γ−1)​β​ρr​S​ϕBγ2​1−ρr​S2)p​(p+1)​𝔼​[∫0T(s−t)p​(p+1)−1​(∫ts‖Dt​(mu)‖p​(p+1)​du)​dt]\displaystyle+\Big(\frac{(\gamma-1)\beta\rho\_{rS}\phi\_{B}}{\gamma^{2}\sqrt{1-\rho\_{rS}^{2}}}\Big)^{p(p+1)}\mathbb{E}\Big[\int\_{0}^{T}(s-t)^{p(p+1)-1}\Big(\int\_{t}^{s}\|D\_{t}\big(m\_{u}\big)\|^{p(p+1)}\mathrm{d}u\Big)\mathrm{d}t\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝔼​[∫0T(∫tTφsp+1​ds)​dt]+1γp​(p+1)​𝔼​[∫0T(T−t)​‖ηt‖p​(p+1)​dt]\displaystyle+\mathbb{E}\Big[\int\_{0}^{T}\Big(\int\_{t}^{T}\varphi\_{s}^{p+1}\mathrm{d}s\Big)\mathrm{d}t\Big]+\frac{1}{\gamma^{p(p+1)}}\mathbb{E}\Big[\int\_{0}^{T}(T-t)\|\eta\_{t}\|^{p(p+1)}\mathrm{d}t\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫0T(∫tT(s−t)p−1(∫tsβp​(p+1)γp​(p+1)(Dt(1)(mu))p​(p+1)du\displaystyle+\int\_{0}^{T}\Big(\int\_{t}^{T}(s-t)^{p-1}\Big(\int\_{t}^{s}\frac{\beta^{p(p+1)}}{\gamma^{p(p+1)}}\big(D\_{t}^{(1)}\big(m\_{u}\big)\big)^{p(p+1)}\mathrm{d}u |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∫ts(β​ρr​Sγ​1−ρr​S2)p​(p+1)(Dt(2)(mu))p​(p+1)du)ds)dt.\displaystyle\phantom{XXXXXXXXXXX}+\int\_{t}^{s}\Big(\frac{\beta\rho\_{rS}}{\gamma\sqrt{1-\rho\_{rS}^{2}}}\Big)^{p(p+1)}\big(D\_{t}^{(2)}\big(m\_{u}\big)\big)^{p(p+1)}\mathrm{d}u\Big)\mathrm{d}s\Big)\mathrm{d}t. |  | (B.13) |

For Assumption [3.7](https://arxiv.org/html/2511.02158v1#S3.Thmdefi7 "Assumption 3.7. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk").(ii).(ii),

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​[(K​e−∫0Trs​ds+x~​∫0Tαs​φs​ds)2]\displaystyle\mathbb{E}\Big[\Big(Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}+\widetilde{x}\int\_{0}^{T}\alpha\_{s}\varphi\_{s}\mathrm{d}s\Big)^{2}\Big] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤2​K2​𝔼​[e−2​∫0Trs​ds]+2​x~2​T​(𝔼​[∫0Tαs4​ds]+𝔼​[∫0Tφs4​ds])<∞,\displaystyle\leq 2K^{2}\mathbb{E}\big[e^{-2\int\_{0}^{T}r\_{s}\mathrm{d}s}\big]+2\widetilde{x}^{2}T\Big(\mathbb{E}\Big[\int\_{0}^{T}\alpha\_{s}^{4}\mathrm{d}s\Big]+\mathbb{E}\Big[\int\_{0}^{T}\varphi\_{s}^{4}\mathrm{d}s\Big]\Big)<\infty, |  | (B.14) |

where the first inequality comes from the convex inequality (a+b)2≤2​(a2+b2)(a+b)^{2}\leq 2(a^{2}+b^{2}), Jensen inequality and Young inequality, and the last inequality follows from ([A](https://arxiv.org/html/2511.02158v1#A1.Ex5 "Appendix A Integrability of 𝛼⁢𝜑 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")), ([A](https://arxiv.org/html/2511.02158v1#A1.Ex2 "Appendix A Integrability of 𝛼⁢𝜑 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) and the facts that 2​γ+6γ2<8<324\frac{2\gamma+6}{\gamma^{2}}<8<324 and (4γ)2<16<324\Big(\frac{4}{\gamma}\Big)^{2}<16<324.

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​[∫0T‖Dt​(K​e−∫0Trs​ds+x~​∫0Tαs​φs​ds)‖2​dt]\displaystyle\mathbb{E}\Big[\int\_{0}^{T}\big\|D\_{t}\Big(Ke^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}+\widetilde{x}\int\_{0}^{T}\alpha\_{s}\varphi\_{s}\mathrm{d}s\Big)\big\|^{2}\mathrm{d}t\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤K2​𝔼​[∫0T‖Dt​(e−∫0Trs​ds)‖2​dt]+x~2​𝔼​[∫0T‖Dt​(∫0Tαs​φs​ds)‖2​dt]\displaystyle\leq K^{2}\mathbb{E}\Big[\int\_{0}^{T}\big\|D\_{t}\Big(e^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}\Big)\big\|^{2}\mathrm{d}t\Big]+\widetilde{x}^{2}\mathbb{E}\Big[\int\_{0}^{T}\big\|D\_{t}\Big(\int\_{0}^{T}\alpha\_{s}\varphi\_{s}\mathrm{d}s\Big)\big\|^{2}\mathrm{d}t\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =K2​𝔼​[∫0T‖Dt​(e−∫0Trs​ds)‖2​dt]+x~2​T​𝔼​[∫0T(∫tT‖αs​Dt​(φs)+φs​Dt​(αs)‖2​ds)​dt]\displaystyle=K^{2}\mathbb{E}\Big[\int\_{0}^{T}\big\|D\_{t}\Big(e^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}\Big)\big\|^{2}\mathrm{d}t\Big]+\widetilde{x}^{2}T\mathbb{E}\Big[\int\_{0}^{T}\Big(\int\_{t}^{T}\big\|\alpha\_{s}D\_{t}\big(\varphi\_{s}\big)+\varphi\_{s}D\_{t}\big(\alpha\_{s}\big)\big\|^{2}\mathrm{d}s\Big)\mathrm{d}t\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤K2​𝔼​[∫0T‖Dt​(e−∫0Trs​ds)‖2​dt]+x~2​T​𝔼​[∫0T(∫tT(αs4+‖Dt​(φs)‖4+φs4+‖Dt​(αs)‖4)​ds)​dt]\displaystyle\leq K^{2}\mathbb{E}\Big[\int\_{0}^{T}\big\|D\_{t}\Big(e^{-\int\_{0}^{T}r\_{s}\mathrm{d}s}\Big)\big\|^{2}\mathrm{d}t\Big]+\widetilde{x}^{2}T\mathbb{E}\Big[\int\_{0}^{T}\Big(\int\_{t}^{T}\big(\alpha\_{s}^{4}+\|D\_{t}\big(\varphi\_{s}\big)\|^{4}+\varphi\_{s}^{4}+\|D\_{t}\big(\alpha\_{s}\big)\|^{4}\big)\mathrm{d}s\Big)\mathrm{d}t\Big] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | <∞,\displaystyle<\infty, |  | (B.15) |

where the first and second inequalities come from the convex inequality (a+b)2≤2​(a2+b2)(a+b)^{2}\leq 2(a^{2}+b^{2}), the triangular inequality and Cauchy-Schwarz inequality, and the last inequality follows from ([A](https://arxiv.org/html/2511.02158v1#A1.Ex2 "Appendix A Integrability of 𝛼⁢𝜑 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")), ([A](https://arxiv.org/html/2511.02158v1#A1.Ex5 "Appendix A Integrability of 𝛼⁢𝜑 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")), ([B.12](https://arxiv.org/html/2511.02158v1#A2.E12 "In Appendix B Proof of Proposition 4.1 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")), ([B](https://arxiv.org/html/2511.02158v1#A2.Ex20 "Appendix B Proof of Proposition 4.1 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) and the facts that 8​γ+120γ2<136<324\frac{8\gamma+120}{\gamma^{2}}<136<324 and (16γ)2<324\big(\frac{16}{\gamma}\big)^{2}<324.

The proofs of Assumptions [3.7](https://arxiv.org/html/2511.02158v1#S3.Thmdefi7 "Assumption 3.7. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk").(ii).(ii), (i​i​i)(iii) and (i​v)(iv) follow similar arguments as in the proof of Assumptions [3.7](https://arxiv.org/html/2511.02158v1#S3.Thmdefi7 "Assumption 3.7. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk").(i).(i). So for brevity they are omitted.

To prove Assumption [3.7](https://arxiv.org/html/2511.02158v1#S3.Thmdefi7 "Assumption 3.7. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk").(v).(v) for q=2q=2, it suffices to show

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℚ(−1)​[∫0T‖Dt​(αt​φt)‖2​dt]<∞​ and ​𝔼ℚ(−1)​[∫0T‖ZtF,⊺​Dt​(ηt)‖2​dt]<∞.\displaystyle\mathbb{E}^{\mathbb{Q}^{(-1)}}\Big[\int\_{0}^{T}\|D\_{t}(\alpha\_{t}\varphi\_{t})\|^{2}\mathrm{d}t\Big]<\infty~\text{ and }~\mathbb{E}^{\mathbb{Q}^{(-1)}}\Big[\int\_{0}^{T}\|Z\_{t}^{F,\intercal}D\_{t}(\eta\_{t})\|^{2}\mathrm{d}t\Big]<\infty. |  | (B.16) |

Again, because the proof of the first inequality in ([B.16](https://arxiv.org/html/2511.02158v1#A2.E16 "In Appendix B Proof of Proposition 4.1 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) is on similar lines with the proof of Assumption [3.7](https://arxiv.org/html/2511.02158v1#S3.Thmdefi7 "Assumption 3.7. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk").(i).(i), it is also omitted for brevity. It remains to show the second inequality in ([B.16](https://arxiv.org/html/2511.02158v1#A2.E16 "In Appendix B Proof of Proposition 4.1 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")). Using successively Young’s inequality, Jensen inequality, ([A](https://arxiv.org/html/2511.02158v1#A1.Ex1 "Appendix A Integrability of 𝛼⁢𝜑 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")), ([B.12](https://arxiv.org/html/2511.02158v1#A2.E12 "In Appendix B Proof of Proposition 4.1 ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) and the fact that Z=:Z~∈ℍℚ(−1)4Z=:\tilde{Z}\in\mathbb{H}\_{\mathbb{Q}^{(-1)}}^{4} (see the proof of Proposition [3.5](https://arxiv.org/html/2511.02158v1#S3.Thmdefi5 "Proposition 3.5. ‣ 3.2. Solution to the optimisation problem ‣ 3. Main results ‣ Asset-liability management with Epstein-Zin utility under stochastic interest rate and unknown market price of risk")) we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℚ(−1)​[∫0T‖ZtF,⊺​Dt​(ηt)‖2​dt]\displaystyle\mathbb{E}^{\mathbb{Q}^{(-1)}}\Big[\int\_{0}^{T}\|Z\_{t}^{F,\intercal}D\_{t}(\eta\_{t})\|^{2}\mathrm{d}t\Big] |  |
|  |  |  |
| --- | --- | --- |
|  | ≤𝔼ℚ(−1)​[∫0T‖ZtF‖4​dt]+𝔼​[HT2]+T​𝔼​[∫0T‖Dt​(ηt)‖8​dt]<∞.\displaystyle\leq\mathbb{E}^{\mathbb{Q}^{(-1)}}\Big[\int\_{0}^{T}\|Z\_{t}^{F}\|^{4}\mathrm{d}t\Big]+\mathbb{E}\big[H\_{T}^{2}\big]+T\mathbb{E}\Big[\int\_{0}^{T}\|D\_{t}(\eta\_{t})\|^{8}\mathrm{d}t\Big]<\infty. |  |

∎

## Acknowledgments

I would like to acknowledge fruitful discussions with Prof. Olivier Menoukeu Pamen.

## References

* [1]
   Abou-Kandil, H., Freiling, G., Ionescu, V., and Jank, G. (2003): Matrix Riccati Equations in Control and Systems Theory. Birkhäuser, Basel.
* [2]
   Aït-Sahali, Y., Brandt, M. (2001): Variable selection for portfolio choice. Journal of Finance, 56: 1297–1351.
* [3]
   Alós, E., Ewald, C.-O. (2008): Malliavin differentiability of the Heston volatility and applications to option pricing. Advances in Applied Probability, 40: 144–162.
* [4]
   Chen, X., Ruan, X., and Zhang, W. (2021): Dynamic portfolio choice and information trading with recursive utility. Economic Modelling, 98: 154–167.
* [5]
   Detemple, J., Garcia, R., and Rindisbacher, M. (2003): A Monte Carlo method for optimal portfolios. Journal of Finance, 58: 401–446.
* [6]
   El Karoui, N., Peng, S., and Quenez, M.-C. (1997): Backward stochastic differential equations in finance. Mathematical Finance, 7: 1–71.
* [7]
   Epstein, L.G., Zin, S.E. (1989):
  Substitution, risk aversion, and the temporal behavior of consumption and asset returns: A theoretical framework. Econometrica, 57: 937–969.
* [8]
   Escobar, M., Ferrando, S., and Rubtsov, A. (2016): Portfolio choice with stochastic interest rates and learning about stock return predictability. International Review of Economics & Finance, 41: 347–370.
* [9]
   Feng, Z., Tian, D., and Zheng, H. (2024): Consumption-investment optimization with Epstein-Zin utility in unbounded non-Markovian markets. arXiv preprint arXiv:2407.19995.
* [10]
   Fleming, W., Pardoux, É. (1982): Optimal control for partially observed diffusions. SIAM Journal on Control and Optimization, 20: 261–285.
* [11]
   Herdegen, M., Hobson, D., and Jerome, J. (2023): The infinite-horizon investment–consumption problem for Epstein–Zin stochastic differential utility. I: Foundations. Finance and Stochastics, 27: 127–158.
* [12]
   Hu, Y., Imkeller, P., and Müller, M. (2005): Utility maximization in incomplete markets. Annals of Applied Probability, 15: 1691–1712.
* [13]
   Liptser, R., Shiryaev, A. (2013):
  Statistics of Random Processes I: General Theory. 2nd ed., Springer Science & Business Media, Berlin.
* [14]
   Luckner, W., Abbott, M., Backus, J., et al. (2003): Professional Actuarial Specialty Guide: Asset-Liability Management. Society of Actuaries.
* [15]
   Ma, Y., Zhang, X. (2023): Consumption and asset allocation with information learning and capital gains tax. Journal of Industrial Management and Optimization, 19.
* [16]
   Matoussi, A., Xing, H. (2018): Convex duality for Epstein–Zin stochastic differential utility. Mathematical Finance, 28: 991–1019.
* [17]
   Nualart, D. (2006): The Malliavin Calculus and Related Topics. Springer-Verlag, Heidelberg.
* [18]
   Di Nunno, G., Øksendal, B., and Proske, F. (2008): Malliavin Calculus for Lévy Processes with Applications to Finance. 2nd ed., Springer-Verlag, Heidelberg.
* [19]
   Vasicek, O. (1977): An equilibrium characterization of the term structure. Journal of Financial Economics, 21: 177–188.
* [20]
   Xia, Y. (2001): Learning about predictability: The effects of parameter uncertainty on dynamic asset allocation. Journal of Finance, 56: 205–246.
* [21]
   Xing, H. (2017): Consumption–investment optimization with Epstein–Zin utility in incomplete markets. Finance and Stochastics, 21: 227–262.