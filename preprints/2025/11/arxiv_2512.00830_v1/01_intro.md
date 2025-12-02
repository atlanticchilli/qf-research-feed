---
authors:
- Cheng Weilun
- Liang Zongxia
- Wang Sheng
- Xia Jianming
doc_id: arxiv:2512.00830v1
family_id: arxiv:2512.00830
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality,
  and Comparative Statics'
url_abs: http://arxiv.org/abs/2512.00830v1
url_html: https://arxiv.org/html/2512.00830v1
venue: arXiv q-fin
version: 1
year: 2025
---


Weilun Cheng
Department of Mathematical Sciences, Tsinghua University, Beijing, China. <chengwl25@mails.tsinghua.edu.cn>


 Zongxia Liang
Department of Mathematical Sciences, Tsinghua University, Beijing, China. <liangzongxia@tsinghua.edu.cn>


 Sheng Wang
Department of Statistics and Actuarial Science, The University of Hong Kong, Pokfulam Road, Hong Kong. <sheng-wa15@tsinghua.org.cn>


 Jianming Xia
State Key Laboratory of Mathematical Sciences, Academy of Mathematics and Systems Science, Chinese
Academy of Sciences, Beijing, China. <xia@amss.ac.cn>

###### Abstract

This paper investigates infinite-dimensional portfolio selection problem under a general distribution of the risk aversion parameter. We provide a complete characterization of all deterministic equilibrium investment strategies. Our results reveal that the solution structure depends critically on the distribution of risk aversion: the equilibrium is unique whenever it exists in the case of finite expected risk aversion, whereas an infinite expectation can lead to infinitely many equilibria or to a unique trivial one (π¯≡𝟎\bar{\pi}\equiv\mathbf{0}). To address this multiplicity, we introduce three optimality criteria—optimal, uniformly optimal, and uniformly strictly optimal—and explicitly characterize the existence and uniqueness of the corresponding equilibria. Under the same necessary and sufficient condition, the optimal and uniformly optimal equilibria exist uniquely and coincide. Furthermore, by additionally assuming that the market price of risk is non-zero near the terminal time, we show that the optimal (and hence uniformly optimal) equilibrium is also uniformly strictly optimal. Finally, we perform comparative statics to demonstrate that a risk aversion distribution dominating another in the reverse hazard rate order leads to a less aggressive equilibrium strategy.

Keywords: Random Risk Aversion; Time-Inconsistency; Portfolio Selection; Intra-Personal Equilibrium; Multiple Equilibria; Comparative Statics

## 1 Introduction

The classical framework for portfolio selection, pioneered by merton1969lifetime; merton1975optimum and samuelson1969lifetime, is based on the assumption that an investor’s risk aversion can be captured by a single known constant. In practice, however, this coefficient is very difficult for an agent to specify with certainty, and a growing body of empirical evidence suggests that it varies dynamically with market conditions, often increasing during financial crises and bear markets, as shown in studies by gordon2000preference; chetty2006new and guiso2018time. These challenges have motivated a move towards models that incorporate random risk aversion. Within this paradigm, a more economically coherent approach, as advanced by Desmettre2023, is to aggregate certainty equivalents over the distribution of the risk aversion parameter.
While the random risk aversion in Desmettre2023 provides a consistent performance measure in monetary units, it introduces a nonlinearity in expectation that naturally leads to the time inconsistency of the preference.

The first systematic treatment of time inconsistency was given by Strotz1955, who proposed the notion of consistent planning, laying the foundation for the intra-personal game-theoretic equilibrium framework. Building on this idea, ekeland2006being later developed a rigorous continuous-time formalization, which in turn inspired extensive research on continuous-time control with time-inconsistent preferences. For example, bjork2010general (published version Bjork2017) established a general theoretical framework by deriving an extended HJB equation and hu2012time; Hu2017 investigated a time-inconsistent stochastic linear–quadratic control problem. For further discussions and related developments, see yan2019time, he2021equilibrium, Hernandez2023, and the references therein.

Within the Black-Scholes market model, Desmettre2023 provide a verification theorem on the intra-personal equilibrium strategies for a CRRA utility function with a general random risk aversion and, in the case of a binomial random risk aversion, characterize the equilibrium by a three-dimensional ODE system without establishing the existence and uniqueness of the solution.111This work has spurred further research extending the model to more complex settings. For example, chen2025equilibrium incorporate a regime-switching framework in which market dynamics and preferences co-evolve; WANG2025103140 study the management of the DC pension plan, providing semi-explicit solutions for a CRRA utility with a binomial random risk aversion; he2025dynamic establish the existence and uniqueness of the solution to an infinite-dimensional Ricatti equation which characterizes the equilibrium strategies under Heston’s SV model for a CRRA or CARA utility function with a general bounded
random risk aversion. For an investigation on the corresponding pre-commitment problem, see xia2024optimal.
This technical gap is fulfilled by liang2025short. For a general random risk aversion, liang2025short characterize
the intra-personal equilibrium strategies by an integral equation. They establish the existence and uniqueness of the solution to the integral equation under the assumptions that the variance of the random risk aversion is finite and that the function hh defined in ([2.6](https://arxiv.org/html/2512.00830v1#S2.E6 "In Theorem 2.4. ‣ 2 Time-inconsistent portfolio selection with random risk aversion ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")) below is bounded.

This paper aims to offer more insight into the portfolio selection problem with random risk aversion within the simplest model, in line with Desmettre2023 and liang2025short. Our main contributions are summarized as follows:

* •

  Complete characterization under general random risk aversion.
  We relax the assumptions in the existing literature and derive a full characterization of all deterministic equilibrium strategies. An important finding is that equilibria may be multiple when the expectation of the random risk aversion is infinite.
* •

  Resolution of equilibrium multiplicity via three optimality criteria.
  To address the non-uniqueness issue, we introduce three optimality notions—optimal, uniformly optimal, and uniformly strictly optimal. We give the necessary and sufficient condition for the existence of optimal equilibria and observe that the optimal equilibrium, if exists, is unique and is also uniformly optimal. Moreover, if the market price of risk remains non-zero near the terminal time, the optimal equilibrium is also uniformly strictly optimal.222wei2024time also observed the non-uniqueness of the equilibrium strategies for rank dependent utilities and discussed the optimal and the uniform optimal equilibria.
* •

  Comparative statics on equilibrium strategies.
  We examine how the distribution of the random risk aversion influences the equilibrium strategies. In analogy with the comparative statics under the standard expected utility maximization (see xia2011risk for example), we show that a “larger” random risk aversion—in the sense of reverse hazard rate dominance—leads to a strictly less aggressive equilibrium allocation to the risky assets.

The paper is organized as follows. Section [2](https://arxiv.org/html/2512.00830v1#S2 "2 Time-inconsistent portfolio selection with random risk aversion ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics") presents the model and derives the integral equation characterizing the equilibrium. Section [3](https://arxiv.org/html/2512.00830v1#S3 "3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics") analyzes both the finite and infinite expectation cases， providing a complete characterization of all equilibria. Section [4](https://arxiv.org/html/2512.00830v1#S4 "4 Optimal Equilibrium Selection ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics") introduces three optimality criteria for equilibrium selection and establishes the necessary and sufficient conditions for their existence and uniqueness. Section [5](https://arxiv.org/html/2512.00830v1#S5 "5 Comparative Statics of Equilibrium Strategies ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics") performs comparative statics to investigate the impact of risk aversion distributions on equilibrium strategies, establishing monotonicity under the reverse hazard rate order, and provides numerical illustrations that verify the theoretical results and present a counterexample under first-order stochastic dominance.

## 2 Time-inconsistent portfolio selection with random risk aversion

Let T>0T>0 be a finite time horizon and (Ω,ℱ,𝔽,ℙ)(\Omega,\mathcal{F},\mathbb{F},\mathbb{P}) be a complete filtered probability space, where 𝔽={ℱt,0≤t≤T}\mathbb{F}=\{\mathcal{F}\_{t},0\leq t\leq T\} is the augmented natural filtration generated by a standard dd-dimensional Brownian motion {B​(t),0≤t≤T}\{B(t),0\leq t\leq T\} and ℱ=ℱT\mathcal{F}=\mathcal{F}\_{T}. The market consists of one risk-free asset (bond) and dd risky assets (stocks). For simplicity, we assume that the interest rate of the bond is zero. The dynamics of the stock price processes SiS\_{i}, i=1,…,di=1,\dots,d, are given by

|  |  |  |
| --- | --- | --- |
|  | d​Si​(t)=Si​(t)​[μi​(t)​d​t+σi​(t)​d​B​(t)],t∈[0,T],dS\_{i}(t)=S\_{i}(t)[\mu\_{i}(t)dt+\sigma\_{i}(t)dB(t)],\quad t\in[0,T], |  |

where the market coefficients μ:[0,T]→ℝd\mu:[0,T]\rightarrow\mathbb{R}^{d} and σ:[0,T]→ℝd×d\sigma:[0,T]\rightarrow\mathbb{R}^{d\times d} are right-continuous and deterministic (each σi\sigma\_{i} denotes the ii-th row of σ\sigma). We always assume that

|  |  |  |
| --- | --- | --- |
|  | ∫0T|μ​(t)|​𝑑t+∑i=1d∫0T|σi​(t)|2​𝑑t<∞\int\_{0}^{T}|\mu(t)|dt+\sum\_{i=1}^{d}\int\_{0}^{T}|\sigma\_{i}(t)|^{2}dt<\infty |  |

and σ​(t)\sigma(t) is invertible for every t∈[0,T]t\in[0,T]. Let λ​(t)≜(σ​(t))−1​μ​(t)\lambda(t)\triangleq(\sigma(t))^{-1}\mu(t) be the market price of risk. We also assume that λ∈L2​((0,T),ℝd)\lambda\in L^{2}((0,T),\mathbb{R}^{d}).

For any m≥1m\geq 1 and 𝕊⊂ℝm\mathbb{S}\subset\mathbb{R}^{m}, L0​(𝔽,𝕊)L^{0}(\mathbb{F},\mathbb{S}) is the space of 𝕊\mathbb{S}-valued, 𝔽\mathbb{F}-progressively measurable processes. For each t∈[0,T]t\in[0,T], p∈[1,∞]p\in[1,\infty], Lp​(ℱt,𝕊)L^{p}(\mathcal{F}\_{t},\mathbb{S}) is the set of all LpL^{p}-integrable, 𝕊\mathbb{S}-valued, and ℱt\mathcal{F}\_{t}-measurable random variables.

A trading strategy is a process π={πt,t∈[0,T)}∈L0​(𝔽,ℝd)\pi=\{\pi\_{t},t\in[0,T)\}\in L^{0}(\mathbb{F},\mathbb{R}^{d}) such that

|  |  |  |
| --- | --- | --- |
|  | ∫0T|πt⊤​μ​(t)|​dt+∫0T|σ⊤​(t)​πt|2​dt<∞​ a.s.,\int\_{0}^{T}|\pi^{\top}\_{t}\mu(t)|\mathrm{d}t+\int\_{0}^{T}|\sigma^{\top}(t)\pi\_{t}|^{2}\mathrm{d}t<\infty\text{ a.s.,} |  |

where πt\pi\_{t} represents the vector of portfolio weights determining the investment of wealth into the stocks at time tt. The self-financing wealth process {Wtπ,0≤t≤T}\{W^{\pi}\_{t},0\leq t\leq T\} associated with a trading strategy π\pi satisfies the following stochastic differential equation (SDE):

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​Wtπ=Wtπ​πt⊤​μ​(t)​d​t+Wtπ​πt⊤​σ​(t)​d​B​(t),W0π=w0>0.\left\{\begin{aligned} &\mathrm{d}W^{\pi}\_{t}=W^{\pi}\_{t}\pi^{\top}\_{t}\mu(t)\mathrm{d}t+W^{\pi}\_{t}\pi^{\top}\_{t}\sigma(t)\mathrm{d}B(t),\\ &W^{\pi}\_{0}=w\_{0}>0.\end{aligned}\right. |  | (2.1) |

The performance of a trading strategy π\pi at time tt is evaluated by the functional J​(t,π)J(t,\pi), defined as the expectation of certainty equivalents

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(t,π)=∫(0,∞)(uγ)−1​(𝔼t​[uγ​(WTπWtπ)])​dΓ​(γ),J(t,\pi)=\int\_{(0,\infty)}\left(u^{\gamma}\right)^{-1}\left(\mathbb{E}\_{t}\left[u^{\gamma}\left({W^{\pi}\_{T}\over W^{\pi}\_{t}}\right)\right]\right)\mathrm{d}\Gamma(\gamma), |  | (2.2) |

where uγu^{\gamma} are the constant relative risk aversion (CRRA) utility functions given by

|  |  |  |
| --- | --- | --- |
|  | uγ​(x)={x1−γ1−γ,γ>0,γ≠1,x>0,log⁡x,γ=1,x>0,\displaystyle u^{\gamma}(x)=\begin{cases}\frac{x^{1-\gamma}}{1-\gamma},&\gamma>0,\gamma\neq 1,x>0,\\ \log x,&\gamma=1,x>0,\end{cases} |  |

and Γ\Gamma is a distribution function on (0,∞)(0,\infty) corresponding to a random variable 𝑹\bm{R} defined on another independent probability space (Ω~,ℱ~,ℙ~)(\tilde{\Omega},\tilde{\mathcal{F}},\tilde{\mathbb{P}}). For notational convenience, expectations with respect to 𝑹\bm{R} will also be denoted by 𝔼\mathbb{E} instead of 𝔼~\tilde{\mathbb{E}}.

A trading strategy π\pi is called *admissible* if

|  |  |  |
| --- | --- | --- |
|  | {𝔼t[|uγ(WTπWtπ)|]<∞a.s.,∀t∈[0,T)and∀γ∈(0,∞),∫(0,∞)|(uγ)−1(𝔼t[uγ(WTπWtπ)])|dΓ(γ)<∞a.s.,∀t∈[0,T).\displaystyle\begin{cases}\mathbb{E}\_{t}\left[\left|u^{\gamma}\left({W^{\pi}\_{T}\over W^{\pi}\_{t}}\right)\right|\right]<\infty\,\ a.s.,\quad\forall t\in[0,T)\,\,\text{and}\,\,\forall\gamma\in(0,\infty),\\ \int\_{(0,\infty)}\left|\left(u^{\gamma}\right)^{-1}\left(\mathbb{E}\_{t}\left[u^{\gamma}\left({W^{\pi}\_{T}\over W^{\pi}\_{t}}\right)\right]\right)\right|\mathrm{d}\Gamma(\gamma)<\infty\,\ \ a.s.,\quad\forall t\in[0,T).\end{cases} |  |

Let Π\Pi denote the set of all admissible strategies.

Hereafter, we consider a fixed π¯∈Π\bar{\pi}\in\Pi, which is a candidate equilibrium strategy.
For any t∈[0,T)t\in[0,T), ε∈(0,T−t)\varepsilon\in(0,T-t) and k∈L∞​(ℱt,ℝd)k\in L^{\infty}(\mathcal{F}\_{t},\mathbb{R}^{d}), define πt,ε,k\pi^{t,\varepsilon,k} by

|  |  |  |
| --- | --- | --- |
|  | πst,ε,k≜{π¯s+k,s∈[t,t+ε),π¯s,s∉[t,t+ε).\pi^{t,\varepsilon,k}\_{s}\triangleq\left\{\begin{aligned} &{\bar{\pi}\_{s}+k},&s\in[t,t+\varepsilon),\\ &\bar{\pi}\_{s},&s\notin[t,t+\varepsilon).\end{aligned}\right. |  |

The strategy πt,ε,k\pi^{t,\varepsilon,k} serves as a perturbation of π¯\bar{\pi}.
Following hu2012time; Hu2017 and
yan2019time, we introduce the definition of equilibrium strategies as follows.

###### Definition 2.1.

A strategy π¯\bar{\pi} is called an equilibrium strategy if for any t∈[0,T)t\in[0,T) and k∈L∞​(ℱt,ℝd)k\in L^{\infty}(\mathcal{F}\_{t},\mathbb{R}^{d}), whenever πt,ε,k∈Π\pi^{t,\varepsilon,k}\in\Pi for all sufficiently small ε>0\varepsilon>0, we have for any positive sequence {εn,n≥1}\{\varepsilon\_{n},n\geq 1\} satisfying limn→∞εn=0\lim\limits\_{n\to\infty}\varepsilon\_{n}=0 that

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim supn→∞J​(t,πt,εn,k)−J​(t,π¯)εn≤0,a.s.\displaystyle\limsup\_{n\to\infty}\frac{J(t,\pi^{t,\varepsilon\_{n},k})-J(t,\bar{\pi})}{\varepsilon\_{n}}\leq 0,\quad\text{a.s.} |  | (2.3) |

###### Remark 2.2.

In the literature, the inequality is usually

|  |  |  |
| --- | --- | --- |
|  | lim supε↓0J​(t,πt,ε,k)−J​(t,π¯)ε≤0,a.s.\displaystyle\limsup\_{\varepsilon\downarrow 0}\frac{J(t,\pi^{t,\varepsilon,k})-J(t,\bar{\pi})}{\varepsilon}\leq 0,\quad\text{a.s.} |  |

However, the left-hand side of the inequality might not be measurable. To ensure measurability, we have modified the definition of equilibrium accordingly.

In our analysis, we follow the approach of liang2025short and focus on the equilibrium strategies given by π¯=(σ⊤)−1​a\bar{\pi}=(\sigma^{\top})^{-1}a, where aa is deterministic, right-continuous, and belongs to the L2L^{2} space. Let Πd⊂Π\Pi\_{d}\subset\Pi denote the set of all such strategies.
For any π¯=(σ⊤)−1​a∈Πd\bar{\pi}=(\sigma^{\top})^{-1}a\in\Pi\_{d}, we introduce the following notations for ease of analysis:

|  |  |  |
| --- | --- | --- |
|  | va​(t)≜∫tT|a​(s)|2​𝑑s,ya​(t)≜∫tTa⊤​(s)​λ​(s)​𝑑s.v\_{a}(t)\triangleq\int\_{t}^{T}|a(s)|^{2}ds,\quad y\_{a}(t)\triangleq\int\_{t}^{T}a^{\top}(s)\lambda(s)ds. |  |

Since the strategy is deterministic, the conditional distribution of the wealth ratio depends only on the deterministic quantities va​(t)v\_{a}(t) and ya​(t)y\_{a}(t) and we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(t,π¯)=𝔼​[e−12​(𝑹​va​(t)−2​ya​(t))].\displaystyle J(t,\bar{\pi})=\mathbb{E}\left[\mathrm{e}^{-\frac{1}{2}\left(\bm{R}v\_{a}(t)-2y\_{a}(t)\right)}\right]. |  | (2.4) |

Before stating the necessary and sufficient condition for the strategy π¯=(σ⊤)−1​a∈Πd\bar{\pi}=(\sigma^{\top})^{-1}a\in\Pi\_{d} to be an equilibrium, we first show that π≡𝟎\pi\equiv\mathbf{0} is an equilibrium if 𝔼​[𝑹]=∞\mathbb{E}[\bm{R}]=\infty.

###### Theorem 2.3.

If 𝔼​[𝐑]=∞\mathbb{E}[\bm{R}]=\infty, then π¯≡𝟎\bar{\pi}\equiv\mathbf{0} is an equilibrium.

###### Proof.

Let π¯=𝟎\bar{\pi}=\mathbf{0}. For any t∈[0,T)t\in[0,T), ε∈(0,T−t)\varepsilon\in(0,T-t), and k∈L∞​(ℱt,ℝd)k\in L^{\infty}(\mathcal{F}\_{t},\mathbb{R}^{d}), we have J​(t,π¯)=1J(t,\bar{\pi})=1 and

|  |  |  |
| --- | --- | --- |
|  | J​(t,πt,ε,k)=e∫tt+εμ⊤​(s)​k​ds​∫(0,∞)e−γ2​∫tt+ε|σ⊤​(s)​k|2​ds​dΓ​(γ)≜ϕ​(ε)×ψ​(ε).\displaystyle J(t,\pi^{t,\varepsilon,k})=\mathrm{e}^{\int\_{t}^{t+\varepsilon}\mu^{\top}(s)k\mathrm{d}s}\int\_{(0,\infty)}\mathrm{e}^{-\frac{\gamma}{2}\int\_{t}^{t+\varepsilon}|\sigma^{\top}(s)k|^{2}\mathrm{d}s}\mathrm{d}\Gamma(\gamma)\triangleq\phi(\varepsilon)\times\psi(\varepsilon). |  |

Noting that

|  |  |  |  |
| --- | --- | --- | --- |
|  | limε→0ψ​(ε)−1ε\displaystyle\lim\_{\varepsilon\to 0}\frac{\psi(\varepsilon)-1}{\varepsilon} | =−12​|σ⊤​(t)​k|2​limε→0∫(0,∞)γ​e−γ2​∫tt+ε|σ⊤​(s)​k|2​ds​dΓ​(γ)\displaystyle=-\frac{1}{2}|\sigma^{\top}(t)k|^{2}\lim\_{\varepsilon\to 0}\int\_{(0,\infty)}\gamma\mathrm{e}^{-\frac{\gamma}{2}\int\_{t}^{t+\varepsilon}|\sigma^{\top}(s)k|^{2}\mathrm{d}s}\mathrm{d}\Gamma(\gamma) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−12​|σ⊤​(t)​k|2​∫(0,∞)γ​dΓ​(γ),\displaystyle=-\frac{1}{2}|\sigma^{\top}(t)k|^{2}\int\_{(0,\infty)}\gamma\mathrm{d}\Gamma(\gamma), |  |

where the first equality uses the mean value theorem
and the second the monotone convergence theorem. Thus, for any positive sequence {εn,n≥1}\{\varepsilon\_{n},n\geq 1\} satisfying limn→∞εn=0\lim\limits\_{n\to\infty}\varepsilon\_{n}=0, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | limn→∞J​(t,πt,εn,k)−J​(t,π¯)εn\displaystyle\lim\_{n\to\infty}\frac{J(t,\pi^{t,\varepsilon\_{n},k})-J(t,\bar{\pi})}{\varepsilon\_{n}} | =limn→∞ϕ​(εn)​ψ​(εn)−1εn=limn→∞(ϕ​(εn)−1)​ψ​(εn)+ψ​(εn)−1εn\displaystyle=\lim\_{n\to\infty}\frac{\phi(\varepsilon\_{n})\psi(\varepsilon\_{n})-1}{\varepsilon\_{n}}=\lim\_{n\to\infty}\frac{(\phi(\varepsilon\_{n})-1)\psi(\varepsilon\_{n})+\psi(\varepsilon\_{n})-1}{\varepsilon\_{n}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =μ⊤​(t)​k−12​|σ⊤​(t)​k|2​∫(0,∞)γ​dΓ​(γ).\displaystyle=\mu^{\top}(t)k-\frac{1}{2}|\sigma^{\top}(t)k|^{2}\int\_{(0,\infty)}\gamma\mathrm{d}\Gamma(\gamma). |  |

Therefore, 𝟎\mathbf{0} is an equilibrium if 𝔼​[𝑹]=∞\mathbb{E}[\bm{R}]=\infty.
∎

We now present the theorem that provides the necessary and sufficient condition for

|  |  |  |
| --- | --- | --- |
|  | π¯=(σ⊤)−1​a∈Πd\displaystyle\bar{\pi}=(\sigma^{\top})^{-1}a\in\Pi\_{d} |  |

to be an equilibrium.

###### Theorem 2.4.

π¯=(σ⊤)−1​a∈Πd\bar{\pi}=(\sigma^{\top})^{-1}a\in\Pi\_{d} is an equilibrium if and only if

|  |  |  |  |
| --- | --- | --- | --- |
|  | a​(t)=h​(va​(t))​λ​(t)\displaystyle a(t)=h(v\_{a}(t))\lambda(t) |  | (2.5) |

for any t∈[0,T)t\in[0,T), where333For the convenience of the analysis that follows, we introduce a slightly different definition from liang2025short, where the function hh corresponds to h​(x2)h(x^{2}) in our setting. Nevertheless, the relevant functional properties—such as boundedness—remain equivalent under the two formulations.

|  |  |  |  |
| --- | --- | --- | --- |
|  | h​(x)≜𝔼​[e−12​𝑹​x]𝔼​[𝑹​e−12​𝑹​x],x∈(0,∞).\displaystyle h(x)\triangleq\frac{\mathbb{E}\left[\mathrm{e}^{-\frac{1}{2}\bm{R}x}\right]}{\mathbb{E}\left[\bm{R}\mathrm{e}^{-\frac{1}{2}\bm{R}x}\right]},\quad x\in(0,\infty). |  | (2.6) |

###### Proof.

It suffices to show that for any t∈[0,T)t\in[0,T), ([2.3](https://arxiv.org/html/2512.00830v1#S2.E3 "In Definition 2.1. ‣ 2 Time-inconsistent portfolio selection with random risk aversion ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")) holds if and only if ([2.5](https://arxiv.org/html/2512.00830v1#S2.E5 "In Theorem 2.4. ‣ 2 Time-inconsistent portfolio selection with random risk aversion ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")) holds.

When 𝔼​[𝑹]<∞\mathbb{E}[\bm{R}]<\infty, we have h​(0)=1𝔼​[𝑹]∈(0,∞)h(0)=\frac{1}{\mathbb{E}[\bm{R}]}\in(0,\infty) and h∈C​([0,∞))h\in C([0,\infty)). In this case, similar to the proof of (liang2025short, Theorem 3.4 ), we know that for any t∈[0,T)t\in[0,T), ([2.3](https://arxiv.org/html/2512.00830v1#S2.E3 "In Definition 2.1. ‣ 2 Time-inconsistent portfolio selection with random risk aversion ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")) holds if and only if ([2.5](https://arxiv.org/html/2512.00830v1#S2.E5 "In Theorem 2.4. ‣ 2 Time-inconsistent portfolio selection with random risk aversion ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")) holds.

When 𝔼​[𝑹]=∞\mathbb{E}[\bm{R}]=\infty, we have h​(0)=0h(0)=0. In this case, ([2.3](https://arxiv.org/html/2512.00830v1#S2.E3 "In Definition 2.1. ‣ 2 Time-inconsistent portfolio selection with random risk aversion ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")) and ([2.5](https://arxiv.org/html/2512.00830v1#S2.E5 "In Theorem 2.4. ‣ 2 Time-inconsistent portfolio selection with random risk aversion ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")) are equivalent for t∈[0,T0)t\in[0,T\_{0}), where

|  |  |  |  |
| --- | --- | --- | --- |
|  | T0≜inf{t∈[0,T]:va​(t)=0}.\displaystyle T\_{0}\triangleq\inf\{t\in[0,T]:v\_{a}(t)=0\}. |  | (2.7) |

Moreover, they are satisfied automatically for t∈[T0,T)t\in[T\_{0},T), by Theorem [2.3](https://arxiv.org/html/2512.00830v1#S2.Thmtheorem3 "Theorem 2.3. ‣ 2 Time-inconsistent portfolio selection with random risk aversion ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics") and h​(0)=0h(0)=0.
∎

The function h​(⋅)h(\cdot) defined in ([2.6](https://arxiv.org/html/2512.00830v1#S2.E6 "In Theorem 2.4. ‣ 2 Time-inconsistent portfolio selection with random risk aversion ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")) plays a central role in our analysis. Here, we simply present two examples in which h​(⋅)h(\cdot) can be computed explicitly.

###### Example 2.5.

Let l:[0,∞)→(0,∞)l:[0,\infty)\to(0,\infty) be defined as l​(y)≜𝔼​[e−𝐑​y]l(y)\triangleq\mathbb{E}[e^{-\bm{R}y}]. Consider the following two distributions for the risk aversion parameter 𝐑\bm{R}.

1. (1)

   Suppose 𝑹\bm{R} follows a Poisson distribution with parameter θ>0\theta>0. Then l​(y)=𝔼​[e−𝑹​y]=eθ​(e−y−1)l(y)=\mathbb{E}[e^{-\bm{R}y}]=e^{\theta(e^{-y}-1)}. According to ([2.6](https://arxiv.org/html/2512.00830v1#S2.E6 "In Theorem 2.4. ‣ 2 Time-inconsistent portfolio selection with random risk aversion ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")), we obtain

   |  |  |  |
   | --- | --- | --- |
   |  | h​(x)=l​(x2)−l′​(x2)=1θ​ex2.\displaystyle h(x)=\frac{l(\frac{x}{2})}{-l^{\prime}(\frac{x}{2})}=\frac{1}{\theta}e^{\frac{x}{2}}. |  |
2. (2)

   Suppose 𝑹\bm{R} follows a Gamma distribution with shape parameter α>0\alpha>0 and scale parameter β>0\beta>0, i.e., with density

   |  |  |  |
   | --- | --- | --- |
   |  | f𝑹​(r)=rα−1​e−rβΓ​(α)​βα,r>0.\displaystyle f\_{\bm{R}}(r)=\frac{r^{\alpha-1}e^{-\frac{r}{\beta}}}{\Gamma(\alpha)\beta^{\alpha}},\quad r>0. |  |

   In this case, l​(y)=𝔼​[e−𝑹​y]=(1+β​y)−αl(y)=\mathbb{E}[e^{-\bm{R}y}]=(1+\beta y)^{-\alpha}, which gives

   |  |  |  |
   | --- | --- | --- |
   |  | h​(x)=l​(x2)−l′​(x2)=1α​β​(1+β2​x).\displaystyle h(x)=\frac{l(\frac{x}{2})}{-l^{\prime}(\frac{x}{2})}=\frac{1}{\alpha\beta}\left(1+\frac{\beta}{2}x\right). |  |

Based on Example [3.4](https://arxiv.org/html/2512.00830v1#S3.Thmtheorem4 "Example 3.4. ‣ 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics") in Section [3](https://arxiv.org/html/2512.00830v1#S3 "3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics"), explicit equilibrium strategies can be obtained in both cases under certain conditions. Moreover, since h​(x)→∞h(x)\to\infty as x→∞x\to\infty in these two examples, some assumptions in prior literature—Desmettre2023, which is restricted to a two-point distribution, and liang2025short, which assumes hh is bounded—may be overly restrictive for standard distributions. This motivates our consideration of general distributions in the subsequent analysis.

According to Theorem [2.4](https://arxiv.org/html/2512.00830v1#S2.Thmtheorem4 "Theorem 2.4. ‣ 2 Time-inconsistent portfolio selection with random risk aversion ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics"), the equilibrium strategies in Πd\Pi\_{d} are given by the solutions to the integral equation ([2.5](https://arxiv.org/html/2512.00830v1#S2.E5 "In Theorem 2.4. ‣ 2 Time-inconsistent portfolio selection with random risk aversion ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")) on [0,T)[0,T), which will be explored in the next section.

## 3 Equilibrium Analysis and Characterization of Solutions

To analyze the existence and uniqueness of the solution to ([2.5](https://arxiv.org/html/2512.00830v1#S2.E5 "In Theorem 2.4. ‣ 2 Time-inconsistent portfolio selection with random risk aversion ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")), we transform it into an ordinary differential equation (ODE) for va​(t)v\_{a}(t). Specifically, by differentiating va​(t)=∫tT|a​(s)|2​𝑑sv\_{a}(t)=\int\_{t}^{T}|a(s)|^{2}ds with respect to tt and substituting a​(t)a(t) from ([2.5](https://arxiv.org/html/2512.00830v1#S2.E5 "In Theorem 2.4. ‣ 2 Time-inconsistent portfolio selection with random risk aversion ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | {va′​(t)=−h2​(va​(t))​|λ​(t)|2,t∈[0,T),va​(T)=0.\displaystyle\begin{cases}v\_{a}^{\prime}(t)=-h^{2}(v\_{a}(t))|\lambda(t)|^{2},&t\in\left[0,T\right),\\ v\_{a}(T)=0.\end{cases} |  | (3.1) |

Note that the ODE ([3.1](https://arxiv.org/html/2512.00830v1#S3.E1 "In 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")) is an equation for vav\_{a} that no longer depends on aa. For simplicity, we will therefore omit the subscript in the discussion below.

We then transform the ODE ([3.1](https://arxiv.org/html/2512.00830v1#S3.E1 "In 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")) into an autonomous equation. To this end, we first define

|  |  |  |
| --- | --- | --- |
|  | Ψ​(t)≜∫tT|λ​(s)|2​ds,t∈[0,T].\displaystyle\Psi(t)\triangleq\int\_{t}^{T}|\lambda(s)|^{2}\mathrm{d}s,\quad t\in[0,T]. |  |

In the sequel, we assume Ψ​(0)>0\Psi(0)>0. Indeed, the condition Ψ​(0)=0\Psi(0)=0 would imply λ​(t)≡0\lambda(t)\equiv 0 on [0,T)[0,T) and, in view of ([2.5](https://arxiv.org/html/2512.00830v1#S2.E5 "In Theorem 2.4. ‣ 2 Time-inconsistent portfolio selection with random risk aversion ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")), lead to a unique equilibrium π≡𝟎\pi\equiv\mathbf{0}. This is a trivial case and will therefore be excluded. For t¯∈[0,Ψ​(0)]\bar{t}\in\left[0,\Psi(0)\right], we also define the following two mappings:

|  |  |  |
| --- | --- | --- |
|  | Φ​(t¯)≜max⁡{ζ∈[0,T]∣Ψ​(ζ)=t¯},φ​(t¯)≜min⁡{ζ∈[0,T]∣Ψ​(ζ)=t¯}.\displaystyle\Phi(\bar{t})\triangleq\max\{\zeta\in[0,T]\mid\Psi(\zeta)=\bar{t}\},\quad\varphi(\bar{t})\triangleq\min\{\zeta\in[0,T]\mid\Psi(\zeta)=\bar{t}\}. |  |

By continuity of Ψ\Psi, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ψ​(Φ​(t¯))=Ψ​(φ​(t¯))=t¯,∀t¯∈[0,Ψ​(0)].\displaystyle\Psi(\Phi(\bar{t}))=\Psi(\varphi(\bar{t}))=\bar{t},\quad\forall\,\bar{t}\in\left[0,\Psi(0)\right]. |  | (3.2) |

Now define, for such t¯\bar{t},

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y¯​(t¯)≜v​(Φ​(t¯)).\displaystyle\bar{Y}(\bar{t})\triangleq v(\Phi(\bar{t})). |  | (3.3) |

For the same t¯\bar{t}, it holds that

|  |  |  |
| --- | --- | --- |
|  | ∫φ​(t¯)Φ​(t¯)|λ​(s)|2​ds=Ψ​(φ​(t¯))−Ψ​(Φ​(t¯))=t¯−t¯=0.\displaystyle\int\_{\varphi(\bar{t})}^{\Phi(\bar{t})}|\lambda(s)|^{2}\mathrm{d}s=\Psi(\varphi(\bar{t}))-\Psi(\Phi(\bar{t}))=\bar{t}-\bar{t}=0. |  |

Since |λ​(s)|2≥0|\lambda(s)|^{2}\geq 0 and λ​(t)\lambda(t) is right-continuous, we deduce that |λ​(s)|2=0|\lambda(s)|^{2}=0 on [φ​(t¯),Φ​(t¯))[\varphi(\bar{t}),\Phi(\bar{t})).
Define f​(⋅)≜h2​(⋅)f(\cdot)\triangleq h^{2}(\cdot). It then follows that

|  |  |  |
| --- | --- | --- |
|  | v′​(t)=−f​(v​(t))​|λ​(t)|2=0 on ​[φ​(t¯),Φ​(t¯)).\displaystyle v^{\prime}(t)=-f(v(t))|\lambda(t)|^{2}=0\quad\text{ on }[\varphi(\bar{t}),\Phi(\bar{t})). |  |

Since v​(t)v(t) is absolutely continuous and v′​(t)=0v^{\prime}(t)=0 on [φ​(t¯),Φ​(t¯))[\varphi(\bar{t}),\Phi(\bar{t})), v​(t)v(t) must be constant on [φ​(t¯),Φ​(t¯)][\varphi(\bar{t}),\Phi(\bar{t})].
Therefore, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(φ​(t¯))=v​(Φ​(t¯)).\displaystyle v(\varphi(\bar{t}))=v(\Phi(\bar{t})). |  | (3.4) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(t)=Y¯​(Ψ​(t)),t∈[0,T].\displaystyle v(t)=\bar{Y}(\Psi(t)),\quad t\in[0,T]. |  | (3.5) |

We now characterize the differentiability of Y¯​(⋅)\bar{Y}(\cdot), we have the following result.

###### Lemma 3.1.

For any t¯∈[0,Ψ​(0)]\bar{t}\in\left[0,\Psi(0)\right], the derivative Y¯′​(t¯)\bar{Y}^{\prime}(\bar{t}) exists and satisfies

|  |  |  |
| --- | --- | --- |
|  | Y¯′​(t¯)=f​(Y¯​(t¯)),\displaystyle\bar{Y}^{\prime}(\bar{t})=f(\bar{Y}(\bar{t})), |  |

where endpoint derivatives are understood in the one-sided sense.

###### Proof.

First, we substitute ([2.5](https://arxiv.org/html/2512.00830v1#S2.E5 "In Theorem 2.4. ‣ 2 Time-inconsistent portfolio selection with random risk aversion ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")) into v​(t)=∫tT|a​(s)|2​dsv(t)=\int\_{t}^{T}|a(s)|^{2}\mathrm{d}s. Noting that d​Ψ​(s)=−|λ​(s)|2​d​s\mathrm{d}\Psi(s)=-|\lambda(s)|^{2}\mathrm{d}s, we can rewrite v​(t)v(t) as

|  |  |  |
| --- | --- | --- |
|  | v​(t)=−∫tTh2​(v​(s))​dΨ​(s).\displaystyle v(t)=-\int\_{t}^{T}h^{2}(v(s))\mathrm{d}\Psi(s). |  |

Using ([3.5](https://arxiv.org/html/2512.00830v1#S3.E5 "In 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")) and applying the change of variables formula444See Proposition 0.4.10 in revuz2013continuous., we transform the integral variable from ss to s¯=Ψ​(s)\bar{s}=\Psi(s):

|  |  |  |
| --- | --- | --- |
|  | Y¯​(Ψ​(t))=∫0Ψ​(t)h2​(Y¯​(s¯))​ds¯.\displaystyle\bar{Y}(\Psi(t))=\int\_{0}^{\Psi(t)}h^{2}(\bar{Y}(\bar{s}))\mathrm{d}\bar{s}. |  |

Letting t¯=Ψ​(t)\bar{t}=\Psi(t) and recalling f​(⋅)=h2​(⋅)f(\cdot)=h^{2}(\cdot), this equation becomes Y¯​(t¯)=∫0t¯f​(Y¯​(s¯))​ds¯\bar{Y}(\bar{t})=\int\_{0}^{\bar{t}}f(\bar{Y}(\bar{s}))\mathrm{d}\bar{s}. Since ff is continuous, differentiating with respect to t¯\bar{t} yields Y¯′​(t¯)=f​(Y¯​(t¯))\bar{Y}^{\prime}(\bar{t})=f(\bar{Y}(\bar{t})).
∎

Lemma [3.1](https://arxiv.org/html/2512.00830v1#S3.Thmtheorem1 "Lemma 3.1. ‣ 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics") shows that any solution v​(t)v(t) to ([3.1](https://arxiv.org/html/2512.00830v1#S3.E1 "In 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")) generates a solution Y¯​(t¯)\bar{Y}(\bar{t}) to

|  |  |  |  |
| --- | --- | --- | --- |
|  | {Y¯′​(t¯)=f​(Y​(t¯)),t¯∈[0,Ψ​(0)],Y¯​(0)=0.\displaystyle\begin{cases}\bar{Y}^{\prime}(\bar{t})=f(Y(\bar{t})),&\bar{t}\in\left[0,\Psi(0)\right],\\ \bar{Y}(0)=0.\end{cases} |  | (3.6) |

Conversely, assume Y¯​(t¯)\bar{Y}(\bar{t}) is a solution to ([3.6](https://arxiv.org/html/2512.00830v1#S3.E6 "In 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")).
Differentiating ([3.5](https://arxiv.org/html/2512.00830v1#S3.E5 "In 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")) yields

|  |  |  |
| --- | --- | --- |
|  | v′​(t)=Y¯′​(Ψ​(t))​Ψ′​(t)=−f​(v​(t))​|λ​(t)|2.\displaystyle v^{\prime}(t)=\bar{Y}^{\prime}(\Psi(t))\Psi^{\prime}(t)=-f(v(t))|\lambda(t)|^{2}. |  |

Hence, v​(t)v(t) satisfies ([3.1](https://arxiv.org/html/2512.00830v1#S3.E1 "In 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")). Therefore, ODE ([3.1](https://arxiv.org/html/2512.00830v1#S3.E1 "In 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")) and ODE ([3.6](https://arxiv.org/html/2512.00830v1#S3.E6 "In 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")) are equivalent in the sense that their solution sets are in one-to-one correspondence: each v​(t)v(t) uniquely determines a corresponding Y¯​(t¯)\bar{Y}(\bar{t}), and vice versa. Consequently, it suffices to analyze the solutions of ([3.6](https://arxiv.org/html/2512.00830v1#S3.E6 "In 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")), for which we obtain the following theorem.

###### Theorem 3.2.

Define F​(⋅)≜∫0⋅1f​(s)​dsF(\cdot)\triangleq\int\_{0}^{\cdot}\frac{1}{f(s)}\mathrm{d}s. Then the following assertions hold.

1. (1)

   If 𝔼​[𝑹]<∞\mathbb{E}[\bm{R}]<\infty, then the ODE ([3.6](https://arxiv.org/html/2512.00830v1#S3.E6 "In 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics"))(\ref{eq:secondode}) has a unique solution if and only if F​(∞)>Ψ​(0)F(\infty)>\Psi(0);
2. (2)

   If 𝔼​[𝑹]=∞\mathbb{E}[\bm{R}]=\infty and F​(ε)<∞F(\varepsilon)<\infty for all ε>0\varepsilon>0, then the ODE ([3.6](https://arxiv.org/html/2512.00830v1#S3.E6 "In 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics"))(\ref{eq:secondode}) has infinitely many solutions defined by

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Y¯(η)​(t¯)={00≤t¯≤η,F−1​(t¯−η)η<t¯≤Ψ​(0),\displaystyle\bar{Y}^{(\eta)}(\bar{t})=\begin{cases}0&0\leq\bar{t}\leq\eta,\\ F^{-1}\left(\bar{t}-\eta\right)&\eta<\bar{t}\leq\Psi(0),\end{cases} |  | (3.7) |

   where η∈𝒜≜[0,Ψ​(0)]∩(Ψ​(0)−F​(∞),Ψ​(0)]\eta\in\mathcal{A}\triangleq[0,\Psi(0)]\cap(\Psi(0)-F(\infty),\Psi(0)].
3. (3)

   If 𝔼​[𝑹]=∞\mathbb{E}[\bm{R}]=\infty and there exists an ε>0\varepsilon>0 such that F​(ε)=∞F(\varepsilon)=\infty, then the ODE ([3.6](https://arxiv.org/html/2512.00830v1#S3.E6 "In 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics"))(\ref{eq:secondode}) has a unique solution y≡0y\equiv 0.

###### Proof.

(1) Assume that 𝔼​[𝑹]<∞\mathbb{E}[\bm{R}]<\infty. As f​(0)=(1𝔼​[𝑹])2>0f(0)=\left(\frac{1}{\mathbb{E}[\bm{R}]}\right)^{2}>0, it follows that F​(0)=0F(0)=0 and F​(⋅)∈C1​([0,+∞))F(\cdot)\in{C}^{1}\left([0,+\infty)\right) is strictly increasing. Thus, the inverse function F−1F^{-1} is well-defined, continuous, and strictly increasing on [0,Ψ​(τ))\left[0,\Psi(\tau)\right), where

|  |  |  |
| --- | --- | --- |
|  | τ≜inf{t∈[0,T):F​(∞)>Ψ​(t)}.\displaystyle\tau\triangleq\inf\left\{t\in\left[0,T\right):F(\infty)>\Psi(t)\right\}. |  |

Consider the function F​(Y¯​(t¯))F(\bar{Y}(\bar{t})) on t¯∈[0,Ψ​(τ))\bar{t}\in\left[0,\Psi(\tau)\right),

|  |  |  |
| --- | --- | --- |
|  | (F​(Y¯​(t¯)))′=F′​(Y¯​(t¯))​Y¯′​(t¯)=1f​(Y¯​(t¯))​f​(Y¯​(t¯))=1,\displaystyle(F(\bar{Y}(\bar{t})))^{\prime}=F^{\prime}(\bar{Y}(\bar{t}))\bar{Y}^{\prime}(\bar{t})=\frac{1}{f(\bar{Y}(\bar{t}))}f(\bar{Y}(\bar{t}))=1, |  |

hence F​(Y¯​(t¯))=t¯+CF(\bar{Y}(\bar{t}))=\bar{t}+C, where CC is a constant.
Using Y¯​(0)=0\bar{Y}(0)=0 and F​(0)=0F(0)=0, we have C=0C=0,
thus F​(Y¯​(t¯))=t¯F(\bar{Y}(\bar{t}))=\bar{t}, and Y¯​(t¯)=F−1​(t¯)\bar{Y}(\bar{t})=F^{-1}(\bar{t}).
Therefore, the equation ([3.6](https://arxiv.org/html/2512.00830v1#S3.E6 "In 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")) has a unique solution Y​(t¯)=F−1​(t¯)Y(\bar{t})=F^{-1}(\bar{t}) on t¯∈[0,Ψ​(τ))\bar{t}\in\left[0,\Psi(\tau)\right).

A global solution on [0,Ψ​(0)]\left[0,\Psi(0)\right] exists only if the domain of F−1F^{-1}, which is [0,F​(∞))\left[0,F(\infty)\right), is sufficiently large. If F​(∞)≤Ψ​(0)F(\infty)\leq\Psi(0), the solution Y¯​(⋅)\bar{Y}(\cdot) diverges to infinity at Ψ​(τ)≥0\Psi(\tau)\geq 0. As a result, the interval [0,Ψ​(τ))\left[0,\Psi(\tau)\right) is the maximal interval of existence for the solution Y¯​(t¯)\bar{Y}(\bar{t}), because the solution blows up at Ψ​(τ)\Psi(\tau).

(2) Assume that 𝔼​[𝑹]=∞\mathbb{E}[\bm{R}]=\infty and F​(ε)<∞F(\varepsilon)<\infty for all ε>0\varepsilon>0. This condition ensures that the function F​(y)F(y) is well-defined for all y≥0y\geq 0. As in the analysis of assertion (1), we have F​(0)=0F(0)=0 and F​(⋅)∈C0​([0,+∞])∩C1​((0,+∞))F(\cdot)\in C^{0}([0,+\infty])\cap C^{1}((0,+\infty)), and FF is strictly increasing. Therefore, a continuous and strictly increasing inverse function F−1F^{-1} exists, satisfying F−1​(0)=0F^{-1}(0)=0.

Assume that Y¯​(⋅)\bar{Y}(\cdot) is a solution to ([3.6](https://arxiv.org/html/2512.00830v1#S3.E6 "In 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")). Define η≜sup{t¯∈[0,Ψ​(0)]:Y¯​(t¯)=0}\eta\triangleq\sup\{\bar{t}\in[0,\Psi(0)]:\bar{Y}(\bar{t})=0\}. For s>ηs>\eta, we must have Y¯​(s)>0\bar{Y}(s)>0 and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y¯′​(s)=f​(Y¯​(s))​Y¯​(s)⇒Y¯′​(s)f​(Y¯​(s))=1.\displaystyle\bar{Y}^{\prime}(s)=f(\bar{Y}(s))\bar{Y}(s)\Rightarrow\frac{\bar{Y}^{\prime}(s)}{f(\bar{Y}(s))}=1. |  | (3.8) |

Integrating ([3.8](https://arxiv.org/html/2512.00830v1#S3.E8 "In Theorem 3.2. ‣ 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")) from η\eta to t¯\bar{t} and using F​(0)=0F(0)=0, we obtain F​(Y¯​(t¯))=t¯−ηF(\bar{Y}(\bar{t}))=\bar{t}-\eta. Thus, for t¯>η\bar{t}>\eta, the solution must satisfy Y¯​(t¯)=F−1​(t¯−η)\bar{Y}(\bar{t})=F^{-1}(\bar{t}-\eta), which shows that any solution necessarily takes the form of ([3.7](https://arxiv.org/html/2512.00830v1#S3.E7 "In item (2) ‣ Theorem 3.2. ‣ 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")).
For F−1(⋅−η)F^{-1}(\cdot-\eta) to be well defined on [η,Ψ​(0)][\eta,\Psi(0)], it is required that Ψ​(0)−η<F​(∞)\Psi(0)-\eta<F(\infty). Together with the constraints inherent in the definition of η\eta, we conclude that η∈𝒜\eta\in\mathcal{A}.
By an argument analogous to the verification in assertion (1), one sees that any function of the form ([3.7](https://arxiv.org/html/2512.00830v1#S3.E7 "In item (2) ‣ Theorem 3.2. ‣ 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")) indeed solves the equation. Consequently, every solution must take the form ([3.7](https://arxiv.org/html/2512.00830v1#S3.E7 "In item (2) ‣ Theorem 3.2. ‣ 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")), uniquely determined by the parameter η\eta.

(3) Assume that 𝔼​[𝑹]=∞\mathbb{E}[\bm{R}]=\infty and F​(ε)=∞F(\varepsilon)=\infty for some ε>0\varepsilon>0.
Clearly, Y¯≡0\bar{Y}\equiv 0 is a solution.
Suppose, to the contrary, that there exists another solution Y¯​(t¯)\bar{Y}(\bar{t}) and some t¯1>0\bar{t}\_{1}>0 such that Y¯​(t¯1)>0\bar{Y}(\bar{t}\_{1})>0. By continuity, there exists t¯2∈[0,t¯1)\bar{t}\_{2}\in[0,\bar{t}\_{1}) such that Y¯​(t¯2)=0\bar{Y}(\bar{t}\_{2})=0 and Y¯​(t¯)>0\bar{Y}(\bar{t})>0 for all t¯∈(t¯2,t¯1]\bar{t}\in(\bar{t}\_{2},\bar{t}\_{1}].
On [t¯2,t¯1][\bar{t}\_{2},\bar{t}\_{1}], we have Y¯′​(t¯)=f​(Y¯​(t¯))\bar{Y}^{\prime}(\bar{t})=f(\bar{Y}(\bar{t})). As such

|  |  |  |
| --- | --- | --- |
|  | ∫t¯2t¯1dt¯=∫t¯2t¯1Y¯′​(t¯)f​(Y¯​(t¯))​dt¯=∫Y¯​(t¯2)Y¯​(t¯1)1f​(s)​ds=F​(Y¯​(t¯1)).\displaystyle\int\_{\bar{t}\_{2}}^{\bar{t}\_{1}}\mathrm{d}\bar{t}=\int\_{\bar{t}\_{2}}^{\bar{t}\_{1}}\frac{\bar{Y}^{\prime}(\bar{t})}{f(\bar{Y}(\bar{t}))}\mathrm{d}\bar{t}=\int\_{\bar{Y}(\bar{t}\_{2})}^{\bar{Y}(\bar{t}\_{1})}\frac{1}{f(s)}\mathrm{d}s=F\left(\bar{Y}(\bar{t}\_{1})\right). |  |

However, by assumption, F​(Y¯​(t¯1))=∞F\left(\bar{Y}(\bar{t}\_{1})\right)=\infty, while ∫t¯2t¯1dt¯=t¯1−t¯2<∞\int\_{\bar{t}\_{2}}^{\bar{t}\_{1}}\mathrm{d}\bar{t}=\bar{t}\_{1}-\bar{t}\_{2}<\infty, a contradiction. Therefore, the equation admits the unique solution Y¯≡0\bar{Y}\equiv 0.
∎

Below, we use Theorem [3.2](https://arxiv.org/html/2512.00830v1#S3.Thmtheorem2 "Theorem 3.2. ‣ 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics") to characterize all solutions to the ODE ([3.1](https://arxiv.org/html/2512.00830v1#S3.E1 "In 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")), and thereby identify all equilibrium strategies in Πd\Pi\_{d}.

###### Theorem 3.3.

The following assertions hold:

1. (1)

   If 𝔼​[𝑹]<∞\mathbb{E}[\bm{R}]<\infty, the ODE ([3.1](https://arxiv.org/html/2512.00830v1#S3.E1 "In 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics"))(\ref{eq:firstode}) admits a unique solution if and only if F​(∞)>Ψ​(0)F(\infty)>\Psi(0). Under this condition, the unique solution of ([3.1](https://arxiv.org/html/2512.00830v1#S3.E1 "In 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")) is given by v​(t)=F−1​(Ψ​(t))v(t)=F^{-1}(\Psi(t)) and the corresponding unique equilibrium in Πd\Pi\_{d} is (σ⊤​(⋅))−1​h​(v​(⋅))​λ​(⋅)(\sigma^{\top}(\cdot))^{-1}h(v(\cdot))\lambda(\cdot).
2. (2)

   If 𝔼​[𝑹]=∞\mathbb{E}[\bm{R}]=\infty and F​(ε)<∞F(\varepsilon)<\infty for all ε>0\varepsilon>0, the ODE ([3.1](https://arxiv.org/html/2512.00830v1#S3.E1 "In 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")) admits infinitely many solutions of the form

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | v(T0)​(t)={F−1​(∫tT0|λ​(s)|2​ds),0≤t<T0,0,T0≤t≤T,\displaystyle v^{(T\_{0})}(t)=\begin{cases}F^{-1}\left(\int\_{t}^{T\_{0}}|\lambda(s)|^{2}\mathrm{d}s\right),&0\leq t<T\_{0},\\ 0,&T\_{0}\leq t\leq T,\end{cases} |  | (3.9) |

   where T0∈ℬ={φ​(η)∣η∈𝒜}T\_{0}\in\mathcal{B}=\{\varphi(\eta)\mid\eta\in\mathcal{A}\}. The set of all equilibrium strategies in Πd\Pi\_{d} is therefore

   |  |  |  |
   | --- | --- | --- |
   |  | 𝒥={π(T0)​(⋅)=(σ⊤​(⋅))−1​h​(v(T0)​(⋅))​λ​(⋅):T0∈ℬ}.\displaystyle\mathcal{J}=\left\{\pi^{(T\_{0})}(\cdot)=(\sigma^{\top}(\cdot))^{-1}h(v^{(T\_{0})}(\cdot))\lambda(\cdot):T\_{0}\in\mathcal{B}\right\}. |  |
3. (3)

   If 𝔼​[𝑹]=∞\mathbb{E}[\bm{R}]=\infty and there exists an ε>0\varepsilon>0 such that F​(ε)=∞F(\varepsilon)=\infty, the ODE ([3.1](https://arxiv.org/html/2512.00830v1#S3.E1 "In 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics"))(\ref{eq:firstode}) admits a unique solution v≡0v\equiv 0, and π≡𝟎\pi\equiv\mathbf{0} is the unique equilibrium in Πd\Pi\_{d}.

###### Proof.

We focus on assertion (2), as the other two assertions are straightforward. Recalling the relationship in ([3.5](https://arxiv.org/html/2512.00830v1#S3.E5 "In 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")), for each η∈𝒜\eta\in\mathcal{A}, define

|  |  |  |  |
| --- | --- | --- | --- |
|  | v(η)​(t)=Y¯(η)​(Ψ​(t)),t∈[0,T].\displaystyle v^{(\eta)}(t)=\bar{Y}^{(\eta)}(\Psi(t)),\quad t\in[0,T]. |  | (3.10) |

From ([3.7](https://arxiv.org/html/2512.00830v1#S3.E7 "In item (2) ‣ Theorem 3.2. ‣ 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")), we know that

|  |  |  |
| --- | --- | --- |
|  | η=sup{t¯∈[0,Ψ​(0)]:Y¯(η)​(t¯)=0}.\displaystyle\eta=\sup\left\{\bar{t}\in[0,\Psi(0)]:\bar{Y}^{(\eta)}(\bar{t})=0\right\}. |  |

Using the definition of T0T\_{0} in ([2.7](https://arxiv.org/html/2512.00830v1#S2.E7 "In 2 Time-inconsistent portfolio selection with random risk aversion ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | T0=inf{t∈[0,T]:v​(t)=0}\displaystyle T\_{0}=\inf\{t\in[0,T]:v(t)=0\} | =inf{t∈[0,T]:Y¯​(Ψ​(t))=0}\displaystyle=\inf\{t\in[0,T]:\bar{Y}(\Psi(t))=0\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =inf{t∈[0,T]:Ψ​(t)=η}\displaystyle=\inf\{t\in[0,T]:\Psi(t)=\eta\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =φ​(η).\displaystyle=\varphi(\eta). |  |

Since φ\varphi is strictly decreasing on 𝒜\mathcal{A}, it induces a bijection between η∈𝒜\eta\in\mathcal{A} and T0∈ℬ≜φ​(𝒜)T\_{0}\in\mathcal{B}\triangleq\varphi(\mathcal{A}). Hence we may relabel the solution v(η)v^{(\eta)} as v(T0)v^{(T\_{0})}, which allows the equilibrium strategies to be characterized directly in terms of the parameter T0∈ℬT\_{0}\in\mathcal{B}.

Furthermore, by the definition of Ψ\Psi, we have η=Ψ​(T0)\eta=\Psi(T\_{0}). Substituting this equality into ([3.7](https://arxiv.org/html/2512.00830v1#S3.E7 "In item (2) ‣ Theorem 3.2. ‣ 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")) yields v(T0)​(t)v^{(T\_{0})}(t) in the form given in ([3.9](https://arxiv.org/html/2512.00830v1#S3.E9 "In item (2) ‣ Theorem 3.3. ‣ 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")). Finally, the conclusion regarding the equilibrium strategies follows directly, since we have ([2.5](https://arxiv.org/html/2512.00830v1#S2.E5 "In Theorem 2.4. ‣ 2 Time-inconsistent portfolio selection with random risk aversion ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")).
∎

It is worth noting that previous studies, such as Desmettre2023 and liang2025short, primarily focus on the specific cases covered by Theorem [3.3](https://arxiv.org/html/2512.00830v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics") (1), under the additional assumptions that h​(⋅)h(\cdot) is bounded and 𝑹\bm{R} is square-integrable. To illustrate the broader applicability of our results, we present three examples below. These examples consider distributions for which: (i) 𝔼​[𝑹2]<∞\mathbb{E}[\bm{R}^{2}]<\infty with unbounded h​(⋅)h(\cdot), (ii) 𝔼​[𝑹2]=∞\mathbb{E}[\bm{R}^{2}]=\infty, and (iii) 𝔼​[𝑹]=∞\mathbb{E}[\bm{R}]=\infty with unbounded h​(⋅)h(\cdot). They serve to examine the properties of the corresponding equilibria and verify the conclusions of Theorem [3.3](https://arxiv.org/html/2512.00830v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics").

###### Example 3.4.

This example derives the explicit equilibrium strategies for the two distributions discussed in Example [2.5](https://arxiv.org/html/2512.00830v1#S2.Thmtheorem5 "Example 2.5. ‣ 2 Time-inconsistent portfolio selection with random risk aversion ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics").

1. (1)

   Poisson distribution: Recall that h​(x)=1θ​ex2h(x)=\dfrac{1}{\theta}e^{\frac{x}{2}}. Computing F​(y)F(y) yields

   |  |  |  |
   | --- | --- | --- |
   |  | F​(y)=∫0y1h2​(s)​𝑑s=θ2​(1−e−y),F(y)=\int\_{0}^{y}\frac{1}{h^{2}(s)}ds=\theta^{2}(1-e^{-y}), |  |

   with F​(∞)=θ2F(\infty)=\theta^{2}. If the condition Ψ​(0)<θ2\Psi(0)<\theta^{2} holds, solving v​(t)=F−1​(Ψ​(t))v(t)=F^{-1}(\Psi(t)) gives v​(t)=−ln⁡(1−Ψ​(t)θ2)v(t)=-\ln(1-\dfrac{\Psi(t)}{\theta^{2}}). Substituting this back, the equilibrium strategy is explicitly given by

   |  |  |  |
   | --- | --- | --- |
   |  | π¯​(t)=(σ⊤)​(t)−1​a​(t)=(σ⊤​(t))−1​h​(v​(t))​λ​(t)=(σ⊤​(t))−1​λ​(t)θ2−Ψ​(t),t∈[0,T)\bar{\pi}(t)=(\sigma^{\top})(t)^{-1}a(t)=(\sigma^{\top}(t))^{-1}h(v(t))\lambda(t)=\dfrac{(\sigma^{\top}(t))^{-1}\lambda(t)}{\sqrt{\theta^{2}-\Psi(t)}},\quad t\in[0,T) |  |
2. (2)

   Gamma distribution: Recall that h​(x)=1α​β​(1+β2​x)h(x)=\dfrac{1}{\alpha\beta}(1+\dfrac{\beta}{2}x). Then, F​(y)F(y) is derived as

   |  |  |  |
   | --- | --- | --- |
   |  | F​(y)=∫0yα2​β2(1+β2​s)2​𝑑s=2​α2​β​(1−11+β2​y),F(y)=\int\_{0}^{y}\frac{\alpha^{2}\beta^{2}}{(1+\frac{\beta}{2}s)^{2}}ds=2\alpha^{2}\beta\left(1-\dfrac{1}{1+\frac{\beta}{2}y}\right), |  |

   with F​(∞)=2​α2​βF(\infty)=2\alpha^{2}\beta. Provided that Ψ​(0)<2​α2​β\Psi(0)<2\alpha^{2}\beta, we obtain v​(t)=2β​[(1−Ψ​(t)2​α2​β)−1−1]v(t)=\dfrac{2}{\beta}\left[\left(1-\dfrac{\Psi(t)}{2\alpha^{2}\beta}\right)^{-1}-1\right]. Therefore, the equilibrium strategy is

   |  |  |  |
   | --- | --- | --- |
   |  | π¯​(t)=(σ⊤​(t))−1​a​(t)=(σ⊤​(t))−1​λ​(t)α​β−Ψ​(t)2​α,t∈[0,T)\bar{\pi}(t)=(\sigma^{\top}(t))^{-1}a(t)=\dfrac{(\sigma^{\top}(t))^{-1}\lambda(t)}{\alpha\beta-\frac{\Psi(t)}{2\alpha}},\quad t\in[0,T) |  |

###### Example 3.5.

This example shows that in Theorem [3.3](https://arxiv.org/html/2512.00830v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics") (1), when 𝔼​[𝐑]<∞\mathbb{E}[\bm{R}]<\infty, F​(∞)F(\infty) may be finite. Consider a random variable 𝐑∼F​(m,n)\bm{R}\sim F(m,n) with parameters m>0m>0 and 2<n≤42<n\leq 4. Its probability density function is given by

|  |  |  |
| --- | --- | --- |
|  | f𝑹​(r)=1B​(m2,n2)​(mn)m2​rm2−1​(1+mn​r)−m+n2,r>0.\displaystyle f\_{\bm{R}}(r)=\dfrac{1}{B(\frac{m}{2},\frac{n}{2})}\left(\dfrac{m}{n}\right)^{\frac{m}{2}}r^{\frac{m}{2}-1}{\left(1+\frac{m}{n}r\right)}^{-\frac{m+n}{2}},\quad r>0. |  |

In this case, the expectation of 𝐑\bm{R} is finite, given by 𝔼​[𝐑]=nn−2<∞\mathbb{E}[\bm{R}]=\frac{n}{n-2}<\infty.

We are interested in the convergence of F​(∞)F(\infty), where

|  |  |  |
| --- | --- | --- |
|  | F​(y)=∫0y1h2​(s)​ds=2​∫0y2(l′​(s)l​(s))2​ds.\displaystyle F(y)=\int\_{0}^{y}\dfrac{1}{h^{2}(s)}\mathrm{d}s=2\int\_{0}^{\frac{y}{2}}\left(\frac{l^{\prime}(s)}{l(s)}\right)^{2}\mathrm{d}s. |  |

Since limy→0+l′​(y)l​(y)=−𝔼​[𝐑]\lim\_{y\to 0^{+}}\frac{l^{\prime}(y)}{l(y)}=-\mathbb{E}[\bm{R}] is finite, y=0y=0 is not a singular point. Next, we analyze the behavior of l′​(y)l​(y)\frac{l^{\prime}(y)}{l(y)} as y→∞y\to\infty.
It is straightforward to see that f𝐑​(r)∼C​rm2−1f\_{\bm{R}}(r)\sim Cr^{\frac{m}{2}-1} as r→0+.r\to 0^{+}.
According to Watson’s Lemma watson1918harmonic555Watson’s Lemma states that for a Laplace integral of the form I​(y)=∫0∞e−y​r​ϕ​(r)​𝑑rI(y)=\int\_{0}^{\infty}e^{-yr}\phi(r)\,dr, if ϕ​(r)∼A​rα\phi(r)\sim Ar^{\alpha} as r→0+r\to 0^{+} with α>−1\alpha>-1, then the asymptotic behavior is given by I​(y)∼A​Γ​(α+1)​y−(α+1)I(y)\sim A\Gamma(\alpha+1)y^{-(\alpha+1)} as y→∞y\to\infty., the asymptotic behavior of l​(y)l(y) is determined by the behavior of f𝐑​(r)f\_{\bm{R}}(r) near the origin. Applying the lemma, we obtain

|  |  |  |
| --- | --- | --- |
|  | l​(y)=∫0∞e−r​y​f𝑹​(r)​dr∼y−m2as ​y→∞.\displaystyle l(y)=\int\_{0}^{\infty}e^{-ry}f\_{\bm{R}}(r)\,\mathrm{d}r\sim y^{-\frac{m}{2}}\quad\text{as }y\to\infty. |  |

Similarly, for l′​(y)=−∫0∞e−r​y​r​f𝐑​(r)​drl^{\prime}(y)=-\int\_{0}^{\infty}e^{-ry}rf\_{\bm{R}}(r)\,\mathrm{d}r, the integrand behaves as r​f𝐑​(r)∼C​rm2rf\_{\bm{R}}(r)\sim Cr^{\frac{m}{2}} as r→0+r\to 0^{+}. Applying Watson’s Lemma again yields

|  |  |  |
| --- | --- | --- |
|  | l′​(y)∼−y−(m2+1)as ​y→∞.\displaystyle l^{\prime}(y)\sim-y^{-\left(\frac{m}{2}+1\right)}\quad\text{as }y\to\infty. |  |

Consequently, (l′​(y)l​(y))2∼y−2\left(\frac{l^{\prime}(y)}{l(y)}\right)^{2}\sim y^{-2} as y→∞y\to\infty. Since ∫1∞y−2​dy\int\_{1}^{\infty}y^{-2}\mathrm{d}y converges, we conclude that F​(∞)<∞F(\infty)<\infty.

###### Example 3.6.

This example is provided to verify the conclusion in Theorem [3.3](https://arxiv.org/html/2512.00830v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics") (2) and (3). For α∈(0,1)\alpha\in(0,1), let 𝐑α∼Gα\bm{R}\_{\alpha}\sim G\_{\alpha}, where GαG\_{\alpha} denote the distribution function whose Laplace transform satisfies 666See Pollard1946 and (Feller1971, Section XIII.6).

|  |  |  |
| --- | --- | --- |
|  | ∫0∞e−v​x​dGα​(x)=e−vα,v≥0.\int\_{0}^{\infty}\mathrm{e}^{-vx}\mathrm{d}G\_{\alpha}(x)=\mathrm{e}^{-v^{\alpha}},\quad v\geq 0. |  |

Note that 𝔼​[𝐑α]=∞\mathbb{E}[\bm{R}\_{\alpha}]=\infty for α∈(0,1)\alpha\in(0,1). Moreover, hh is given by h​(x)=1α​(x2)1−αh(x)=\frac{1}{\alpha}\left(\frac{x}{2}\right)^{1-\alpha}. For simplicity, we assume that λ≠0\lambda\neq 0 is a constant in ℝ\mathbb{R}. By direct calculation, the solution to the ODE ([3.1](https://arxiv.org/html/2512.00830v1#S3.E1 "In 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")) for α∈(0.5,1)\alpha\in(0.5,1) takes the form

|  |  |  |
| --- | --- | --- |
|  | v(T0)​(t)={(22​α−2​1α2​(2​α−1)​λ2​(T0−t))12​α−1,t∈[0,T0),0t∈[T0,T],\displaystyle v^{(T\_{0})}(t)=\begin{cases}\left(2^{2\alpha-2}\dfrac{1}{\alpha^{2}}(2\alpha-1)\lambda^{2}(T\_{0}-t)\right)^{\frac{1}{2\alpha-1}},&t\in[0,T\_{0}),\\ 0&t\in[T\_{0},T],\end{cases} |  |

where T0∈[0,T]T\_{0}\in[0,T]. For α∈(0,0.5]\alpha\in(0,0.5], direct calculation shows that the ODE admits only the trivial solution v≡0v\equiv 0.

Below, we recover the above result using Theorem [3.3](https://arxiv.org/html/2512.00830v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics"). Specifically, for any α∈(0.5,1)\alpha\in(0.5,1), we have
F​(ε)<∞F(\varepsilon)<\infty for all ε>0\varepsilon>0.
As a result, the ODE ([3.1](https://arxiv.org/html/2512.00830v1#S3.E1 "In 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics"))(\ref{eq:firstode}) admits infinitely many solutions. Furthermore, because F​(∞)=∫0∞α2​(12​s)2​α−2​ds=∞F(\infty)=\int\_{0}^{\infty}\alpha^{2}\left(\dfrac{1}{2}s\right)^{2\alpha-2}\,\mathrm{d}s=\infty, the parameter η\eta in Theorem [3.2](https://arxiv.org/html/2512.00830v1#S3.Thmtheorem2 "Theorem 3.2. ‣ 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics") (2) can take any value in [0,λ2​T][0,\lambda^{2}T], and T0T\_{0} in Theorem [3.3](https://arxiv.org/html/2512.00830v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics") (2) can take any value in [0,T][0,T]. Moreover, since F​(y)=α2​22−2​α2​α−1​y2​α−1F(y)=\frac{\alpha^{2}2^{2-2\alpha}}{2\alpha-1}y^{2\alpha-1}, we obtain its inverse F−1​(z)=(22​α−2​(2​α−1)α2​z)12​α−1F^{-1}(z)=\left(\frac{2^{2\alpha-2}(2\alpha-1)}{\alpha^{2}}z\right)^{\frac{1}{2\alpha-1}}. Using ([3.9](https://arxiv.org/html/2512.00830v1#S3.E9 "In item (2) ‣ Theorem 3.3. ‣ 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics"))(\ref{solutions}), we then precisely recover the form of v(T0)​(t)v^{(T\_{0})}(t). For α∈(0,0.5]\alpha\in(0,0.5], we have F​(ε)=∞F(\varepsilon)=\infty for every ε>0\varepsilon>0, and therefore the ODE ([3.1](https://arxiv.org/html/2512.00830v1#S3.E1 "In 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics"))(\ref{eq:firstode}) admits the unique solution v≡0v\equiv 0. These results are fully consistent with those obtained by direct calculation.

## 4 Optimal Equilibrium Selection

According to the discussion in Theorem [3.3](https://arxiv.org/html/2512.00830v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics") (2), if 𝔼​[𝑹]=∞\mathbb{E}[\bm{R}]=\infty and F​(ε)<∞F(\varepsilon)<\infty for all ε>0\varepsilon>0, then the set Πd\Pi\_{d} contains infinitely many equilibria, whose collection is denoted by 𝒥\mathcal{J}.
This multiplicity of equilibria naturally raises the question: which equilibrium should the agent choose?
In this section, we introduce several criteria for selecting an optimal equilibrium. These criteria compare the functional J​(t,π)J(t,\pi), either at the initial time t=0t=0 or at any arbitrary time t∈[0,T]t\in[0,T]. We begin by presenting three definitions of optimal equilibrium.

###### Definition 4.1.

1. (1)

   π^∈𝒥\hat{\pi}\in\mathcal{J} is called optimal if

   |  |  |  |
   | --- | --- | --- |
   |  | J​(0,π^)≥J​(0,π(T0)),∀π(T0)∈𝒥.\displaystyle J(0,\hat{\pi})\geq J(0,\pi^{(T\_{0})}),\quad\forall\pi^{(T\_{0})}\in\mathcal{J}. |  |
2. (2)

   π^∈𝒥\hat{\pi}\in\mathcal{J} is called uniformly optimal if

   |  |  |  |
   | --- | --- | --- |
   |  | J​(t,π^)≥J​(t,π(T0)),∀π(T0)∈𝒥​and​t∈[0,T].\displaystyle J(t,\hat{\pi})\geq J(t,\pi^{(T\_{0})}),\quad\forall\pi^{(T\_{0})}\in\mathcal{J}\,\,\text{and}\,\,t\in[0,T]. |  |
3. (3)

   π^∈𝒥\hat{\pi}\in\mathcal{J} is called uniformly strictly optimal if

   |  |  |  |
   | --- | --- | --- |
   |  | J​(t,π^)>J​(t,π(T0)),∀π^≠π(T0)∈𝒥​and​t∈[0,T).\displaystyle J(t,\hat{\pi})>J(t,\pi^{(T\_{0})}),\quad\forall\hat{\pi}\neq\pi^{(T\_{0})}\in\mathcal{J}\,\,\text{and}\,\,t\in[0,T). |  |

###### Theorem 4.2.

The optimal strategy exists if and only if F​(∞)>Ψ​(0)F(\infty)>\Psi(0). When it exists, it is unique and given by π(φ​(0))​(⋅)=(σ⊤​(⋅))−1​h​(v(φ​(0))​(⋅))​λ​(⋅)\pi^{(\varphi(0))}(\cdot)=(\sigma^{\top}(\cdot))^{-1}h(v^{(\varphi(0))}(\cdot))\lambda(\cdot).
Furthermore, π(φ​(0))\pi^{(\varphi(0))} is also uniformly optimal. It is uniformly strictly optimal if and only if both F​(∞)>Ψ​(0)F(\infty)>\Psi(0) and Ψ​(t)>0\Psi(t)>0 for all t∈[0,T)t\in[0,T) hold, in which case φ​(0)=T\varphi(0)=T.

###### Proof.

We first establish a lemma to compare the magnitude relations between different solutions to ODE ([3.6](https://arxiv.org/html/2512.00830v1#S3.E6 "In 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics"))(\ref{eq:secondode}).

###### Lemma 4.3.

In the setting of Theorem [3.2](https://arxiv.org/html/2512.00830v1#S3.Thmtheorem2 "Theorem 3.2. ‣ 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics") (2), where ODE ([3.6](https://arxiv.org/html/2512.00830v1#S3.E6 "In 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics"))(\ref{eq:secondode}) admits infinitely many solutions, Y¯(η)​(t)\bar{Y}^{(\eta)}(t) is non-increasing in η∈𝒜\eta\in\mathcal{A} for any t∈[0,Ψ​(0)]t\in[0,\Psi(0)]. Furthermore, if F​(∞)>Ψ​(0)F(\infty)>\Psi(0) and Ψ​(t)>0\Psi(t)>0 for all t∈[0,T)t\in[0,T) hold, then the strict inequality Y¯(0)​(Ψ​(t))>Y¯(η)​(Ψ​(t))\bar{Y}^{(0)}(\Psi(t))>\bar{Y}^{(\eta)}(\Psi(t)) holds for any η∈𝒜∖{0}\eta\in\mathcal{A}\setminus\{0\} and any t∈[0,T)t\in[0,T).

###### Proof.

Let η1,η2∈𝒜\eta\_{1},\eta\_{2}\in\mathcal{A} with η1<η2\eta\_{1}<\eta\_{2}, we compare Y¯(η1)​(t¯)\bar{Y}^{(\eta\_{1})}(\bar{t}) and Y¯(η2)​(t¯)\bar{Y}^{(\eta\_{2})}(\bar{t}).

For 0≤t¯≤η10\leq\bar{t}\leq\eta\_{1}, Y¯(η1)​(t¯)=Y¯(η2)​(t¯)=0\bar{Y}^{(\eta\_{1})}(\bar{t})=\bar{Y}^{(\eta\_{2})}(\bar{t})=0. For η1<t¯≤η2\eta\_{1}<\bar{t}\leq\eta\_{2}, Y¯(η2)​(t¯)=0<Y¯(η1)​(t¯)\bar{Y}^{(\eta\_{2})}(\bar{t})=0<\bar{Y}^{(\eta\_{1})}(\bar{t}). For η2<t¯≤Ψ​(0)\eta\_{2}<\bar{t}\leq\Psi(0), Y¯(ηi)​(t¯)=F−1​(t¯−ηi)\bar{Y}^{(\eta\_{i})}(\bar{t})=F^{-1}\left(\bar{t}-\eta\_{i}\right) , i=1,2i=1,2. Since η1<η2\eta\_{1}<\eta\_{2}, we have t¯−η1>t¯−η2\bar{t}-\eta\_{1}>\bar{t}-\eta\_{2}, and because F−1F^{-1} is strictly increasing, F−1​(t¯−η1)>F−1​(t¯−η2)F^{-1}\left(\bar{t}-\eta\_{1}\right)>F^{-1}\left(\bar{t}-\eta\_{2}\right), hence Y¯(η1)​(t¯)>Y¯(η2)​(t¯)\bar{Y}^{(\eta\_{1})}(\bar{t})>\bar{Y}^{(\eta\_{2})}(\bar{t}).

Finally, assume F​(∞)>Ψ​(0)F(\infty)>\Psi(0) and Ψ​(t)>0\Psi(t)>0 for all t∈[0,T)t\in[0,T) hold. For any η∈𝒜∖{0}\eta\in\mathcal{A}\setminus\{0\} and t∈[0,T)t\in[0,T), we have

|  |  |  |
| --- | --- | --- |
|  | Y¯(0)​(Ψ​(t))=F−1​(Ψ​(t))>F−1​(max⁡(0,Ψ​(t)−η))=Y¯(η)​(Ψ​(t)),\displaystyle\bar{Y}^{(0)}(\Psi(t))=F^{-1}(\Psi(t))>F^{-1}(\max(0,\Psi(t)-\eta))=\bar{Y}^{(\eta)}(\Psi(t)), |  |

where the inequality follows from the strict monotonicity of F−1F^{-1}.
∎

From the above lemma, we see that for any t∈[0,T]t\in[0,T], v(T0)​(t)v^{(T\_{0})}(t) in ([3.9](https://arxiv.org/html/2512.00830v1#S3.E9 "In item (2) ‣ Theorem 3.3. ‣ 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")) is non-decreasing with respect to T0∈ℬT\_{0}\in\mathcal{B}. We now proceed to prove the main result. For all π(T0)∈𝒥\pi^{(T\_{0})}\in\mathcal{J}, we have

|  |  |  |
| --- | --- | --- |
|  | y(T0)​(0)=∫0T(as(T0))⊤​λ​(s)​ds=∫0Th​(v(T0)​(s))​|λ​(s)|2​ds,\displaystyle y^{(T\_{0})}(0)=\int\_{0}^{T}(a\_{s}^{(T\_{0})})^{\top}\lambda(s)\mathrm{d}s=\int\_{0}^{T}h(v^{(T\_{0})}(s))|\lambda(s)|^{2}\mathrm{d}s, |  |

therefore

|  |  |  |  |
| --- | --- | --- | --- |
|  | −(𝑹​v(T0)​(0)−2​y(T0)​(0))\displaystyle-(\bm{R}v^{(T\_{0})}(0)-2y^{(T\_{0})}(0)) | =−𝑹​v(T0)​(0)+2​∫0Th​(v(T0)​(s))​|λ​(s)|2​ds\displaystyle=-\bm{R}v^{(T\_{0})}(0)+2\int\_{0}^{T}h(v^{(T\_{0})}(s))|\lambda(s)|^{2}\mathrm{d}s |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−𝑹​v(T0)​(0)+2​∫0v(T0)​(0)1h​(y)​dy,\displaystyle=-\bm{R}v^{(T\_{0})}(0)+2\int\_{0}^{v^{(T\_{0})}(0)}\frac{1}{h(y)}\mathrm{d}y, |  |

where the second equality arises from y=v(T0)​(s)y=v^{(T\_{0})}(s), d​y=−h2​(v(T0)​(s))​|λ​(s)|2​d​s\mathrm{d}y=-h^{2}(v^{(T\_{0})}(s))|\lambda(s)|^{2}\mathrm{d}s.

Furthermore, since F​(t)=∫0t1h2​(s)​ds<∞F(t)=\int\_{0}^{t}\frac{1}{h^{2}(s)}\mathrm{d}s<\infty for any t>0t>0, and by the Cauchy-Schwarz inequality, ∫0t1h​(s)​ds\int\_{0}^{t}\frac{1}{h(s)}\mathrm{d}s is well-defined for any t>0t>0.
Thus, we have

|  |  |  |
| --- | --- | --- |
|  | J​(0,π(T0))=e∫0v(T0)​(0)1h​(y)​dy​l​(v(T0)​(0)2),\displaystyle J(0,\pi^{(T\_{0})})=e^{\int\_{0}^{v^{(T\_{0})}(0)}\frac{1}{h(y)}\mathrm{d}y}l\left(\frac{v^{(T\_{0})}(0)}{2}\right), |  |

where l:[0,∞)→(0,∞)l:[0,\infty)\to(0,\infty) is defined by l​(x)≜𝔼​[e−𝑹​x]l(x)\triangleq\mathbb{E}[e^{-\bm{R}x}].
Let ℒ​(z):[0,∞)→[0,∞)\mathcal{L}(z):[0,\infty)\to[0,\infty) be defined by
ℒ​(z)=∫0z1h​(y)​dy+ln⁡l​(z2).\mathcal{L}(z)=\int\_{0}^{z}\frac{1}{h(y)}\mathrm{d}y+\ln l\left(\frac{z}{2}\right).
Then

|  |  |  |
| --- | --- | --- |
|  | d​ℒd​z=1h​(z)−12​𝔼​[𝑹​e−12​𝑹​z]𝔼​[e−12​𝑹​y]=12​h​(z)>0,∀z>0.\displaystyle\frac{d\mathcal{L}}{dz}=\frac{1}{h(z)}-\frac{1}{2}\frac{\mathbb{E}\left[\bm{R}e^{-\frac{1}{2}\bm{R}z}\right]}{\mathbb{E}\left[e^{-\frac{1}{2}\bm{R}y}\right]}=\frac{1}{2h(z)}>0,\quad\forall\,z>0. |  |

Hence, ℒ\mathcal{L} is strictly increasing in zz, and J​(0,π(T0))J(0,\pi^{(T\_{0})}) attains its maximum where v(T0)​(0)v^{(T\_{0})}(0) is maximal. Noting that v(T0)​(0)v^{(T\_{0})}(0) is non-decreasing in T0T\_{0}, it suffices to find a maximal parameter T0T\_{0} within ℬ\mathcal{B}. Since φ\varphi is strictly decreasing, the existence of a maximal element in ℬ\mathcal{B} is equivalent to the existence of a minimal element in 𝒜\mathcal{A}.

If F​(∞)>Ψ​(0)F(\infty)>\Psi(0), then 𝒜=[0,Ψ​(0)]\mathcal{A}=[0,\Psi(0)] includes its minimum at 0, so a maximal strategy exists. Conversely, if F​(∞)≤Ψ​(0)F(\infty)\leq\Psi(0), then 𝒜=(Ψ​(0)−F​(∞),Ψ​(0)]\mathcal{A}=(\Psi(0)-F(\infty),\Psi(0)] is left-open and admits no minimum. Thus, ℬ\mathcal{B} has a maximal element if and only if F​(∞)>Ψ​(0)F(\infty)>\Psi(0).
This establishes that the optimal strategy exists if and only if F​(∞)>Ψ​(0)F(\infty)>\Psi(0), and when it exists, it is given by π(φ​(0))\pi^{(\varphi(0))}.

Next, we turn to the uniformly optimal equilibrium. In light of the preceding proof, we restrict attention to the case F​(∞)>Ψ​(0)F(\infty)>\Psi(0). Analogous to the derivation at t=0t=0, for any fixed t∈[0,T]t\in[0,T], we have J​(t,π(T0))=exp⁡(ℒ​(v(T0)​(t)))J(t,\pi^{(T\_{0})})=\exp\left(\mathcal{L}(v^{(T\_{0})}(t))\right). Since ℒ​(z)\mathcal{L}(z) is strictly increasing in zz and v(T0)​(t)v^{(T\_{0})}(t) is non-decreasing in T0T\_{0}, we conclude that J​(t,π(T0))J(t,\pi^{(T\_{0})}) is non-decreasing with respect to T0T\_{0}. Consequently, it also suffices to find a maximal parameter T0T\_{0} within ℬ\mathcal{B}.
Since ℬ\mathcal{B} admits a unique maximal element φ​(0)\varphi(0), we immediately obtain that the optimal equilibrium π(φ​(0))\pi^{(\varphi(0))} is also uniformly optimal.

Finally, we consider the uniformly strictly optimal equilibrium. If Ψ​(t)=0\Psi(t)=0 for some t∈[0,T)t\in[0,T), then v(T0)​(t)≡0v^{(T\_{0})}(t)\equiv 0 for any T0∈ℬT\_{0}\in\mathcal{B}, which implies J​(t,π(T0))≡exp⁡(ℒ​(0))=1J(t,\pi^{(T\_{0})})\equiv\exp(\mathcal{L}(0))=1 for all π(T0)∈𝒥\pi^{(T\_{0})}\in\mathcal{J}. Hence, no uniformly strictly optimal equilibrium exists in this case. Conversely, assume Ψ​(t)>0\Psi(t)>0 for all t∈[0,T)t\in[0,T) and F​(∞)>Ψ​(0)F(\infty)>\Psi(0). Recalling the definition φ​(0)=min⁡{t∈[0,T]:Ψ​(t)=0}\varphi(0)=\min\{t\in[0,T]:\Psi(t)=0\}, the condition that Ψ​(t)>0\Psi(t)>0 for all t<Tt<T implies that φ​(0)=T\varphi(0)=T. Let T0∈ℬ∖{T}T\_{0}\in\mathcal{B}\setminus\{T\}, then we have η:=Ψ​(T0)>0=Ψ​(T)\eta:=\Psi(T\_{0})>0=\Psi(T). By Lemma [4.3](https://arxiv.org/html/2512.00830v1#S4.Thmtheorem3 "Lemma 4.3. ‣ Theorem 4.2. ‣ 4 Optimal Equilibrium Selection ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics"), for any t∈[0,T)t\in[0,T), it holds that

|  |  |  |
| --- | --- | --- |
|  | v(T)​(t)=Y¯(0)​(Ψ​(t))>Y¯(η)​(Ψ​(t))=v(T0)​(t).\displaystyle v^{(T)}(t)=\bar{Y}^{(0)}(\Psi(t))>\bar{Y}^{(\eta)}(\Psi(t))=v^{(T\_{0})}(t). |  |

Since ℒ​(z)\mathcal{L}(z) is strictly increasing in zz, we obtain J​(t,π(T))>J​(t,π(T0))J(t,\pi^{(T)})>J(t,\pi^{(T\_{0})}). Therefore, π(φ​(0))=π(T)\pi^{(\varphi(0))}=\pi^{(T)} is the unique uniformly strictly optimal equilibrium.
∎

## 5 Comparative Statics of Equilibrium Strategies

In the previous sections, we fully characterized the equilibrium strategies associated with a given distribution of risk aversion 𝑹\bm{R} and discussed how to select the optimal equilibrium. We now turn to comparative statics and ask a natural economic question: How does a shift in the distribution of risk aversion affect the resulting equilibrium investment behavior?

To formalize such comparisons, we begin by recalling the notion of first-order stochastic dominance, which provides a standard criterion for ranking risk aversion distributions.

###### Definition 5.1.

Let 𝐑𝟏\bm{R\_{1}} and 𝐑𝟐\bm{R\_{2}} be two random variables. We say that 𝐑𝟏\bm{R\_{1}} dominates 𝐑𝟐\bm{R\_{2}} in the sense of first-order stochastic dominance, denoted as 𝐑𝟏⪰1𝐑𝟐\bm{R\_{1}}\succeq\_{1}\bm{R\_{2}}, if

|  |  |  |
| --- | --- | --- |
|  | P​(𝑹𝟏≥x)≥P​(𝑹𝟐≥x),∀x∈ℝ.\displaystyle P(\bm{R\_{1}}\geq x)\geq P(\bm{R\_{2}}\geq x),\quad\forall x\in\mathbb{R}. |  |

Intuitively, one might expect that if Investor 1 is “more risk-averse” than Investor 2 in the sense of first-order stochastic dominance, then Investor 1 should take a smaller position in the risky asset at every point in time. Surprisingly, this intuition turns out to be false.

![Refer to caption](counterexample_plot.png)


Figure 1: Comparative evolution of ai​(t)a\_{i}(t) under first-order stochastic dominance. The red solid line corresponds to the more risk-averse Investor 1 with distribution P​(𝑹1=1)=0.5P(\bm{R}\_{1}=1)=0.5, P​(𝑹1=5)=0.5P(\bm{R}\_{1}=5)=0.5, and the blue dashed line to the less risk-averse Investor 2 with P​(𝑹2=1)=0.5P(\bm{R}\_{2}=1)=0.5, P​(𝑹2=2)=0.5P(\bm{R}\_{2}=2)=0.5. The orange shaded region indicates where |a1​(t)|>|a2​(t)||a\_{1}(t)|>|a\_{2}(t)|. Parameters: λ=0.4\lambda=0.4, horizon T=40T=40.

Figure [1](https://arxiv.org/html/2512.00830v1#S5.F1 "Figure 1 ‣ 5 Comparative Statics of Equilibrium Strategies ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics") illustrates the comparative evolution of |ai||a\_{i}|, i=1,2i=1,2777Since π¯=(σ⊤)−1​a\bar{\pi}=(\sigma^{\top})^{-1}a, in the one-dimensional case the comparison of |ai​(t)||a\_{i}(t)| is equivalent to that of |π|i|\pi|\_{i}. for two investors whose risk aversion distributions are given by
P​(𝑹1=1)=0.5P(\bm{R}\_{1}=1)=0.5, P​(𝑹1=5)=0.5P(\bm{R}\_{1}=5)=0.5 and
P​(𝑹2=1)=0.5P(\bm{R}\_{2}=1)=0.5, P​(𝑹2=2)=0.5P(\bm{R}\_{2}=2)=0.5. It is straightforward to verify that 𝑹1⪰1𝑹2\bm{R}\_{1}\succeq\_{1}\bm{R}\_{2}.
The orange-shaded Reversal Region highlights that the more risk-averse Investor 1 adopts a strictly more aggressive position than Investor 2 when the time to maturity is sufficiently long. This counterexample shows that even under first-order stochastic dominance, the magnitudes of equilibrium investment strategies need not exhibit monotonicity.

The appearance of this counterexample (Figure [1](https://arxiv.org/html/2512.00830v1#S5.F1 "Figure 1 ‣ 5 Comparative Statics of Equilibrium Strategies ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")) may suggest that the search for a general comparative result under first-order stochastic dominance is fundamentally obstructed. In fact, the observed reversal is not an artifact of a particular parameter choice. We show below that such a reversal in investment magnitudes is unavoidable when the investment horizon TT is sufficiently large, provided that the risk-aversion distributions satisfy the conditions stated in the following proposition.

In the following proposition, for convenience, we extend the market to an infinite horizon and assume that the market price of risk λ\lambda is defined on [0,∞)[0,\infty). For every fixed T>0T>0, we require Ψ​(0,T)≜∫0T|λ​(s)|2​ds<∞\Psi(0,T)\triangleq\int\_{0}^{T}|\lambda(s)|^{2}\mathrm{d}s<\infty. In addition, we assume that limT→∞Ψ​(0,T)=∞\lim\_{T\to\infty}\Psi(0,T)=\infty and λ​(0)≠0\lambda(0)\neq 0. As discussed in the preceding sections, for each fixed TT we can define the equilibrium strategy {πi​(t,T):t∈[0,T)}\{\pi\_{i}(t,T):t\in[0,T)\} associated with the distribution RiR\_{i} (as used in the proposition below). The proposition shows that, as long as the distributions RiR\_{i} satisfy certain conditions, the magnitudes |πi​(0,T)||\pi\_{i}(0,T)| must exhibit a strict and deterministic ordering when the horizon TT is sufficiently large.

###### Proposition 5.2.

Let 𝐑1\bm{R}\_{1} and 𝐑2\bm{R}\_{2} be two non-negative random variables with finite expectations (i.e., 𝔼​[𝐑i]<∞\mathbb{E}[\bm{R}\_{i}]<\infty). Assume the following conditions are satisfied:

1. (1)

   Let r0=essinf⁡𝑹1=essinf⁡𝑹2>0r\_{0}=\operatorname{essinf}\bm{R}\_{1}=\operatorname{essinf}\bm{R}\_{2}>0. There exists a positive probability mass at r0r\_{0}, meaning that pi=P​(𝑹i=r0)∈(0,1)p\_{i}=P(\bm{R}\_{i}=r\_{0})\in(0,1) for i=1,2i=1,2.
2. (2)

   Define the infimum of the first support point of 𝑹i\bm{R}\_{i} strictly greater than r0r\_{0} as r~i=inf{r∈s​u​p​p​(𝑹i):r>r0}\tilde{r}\_{i}=\inf\{r\in supp(\bm{R}\_{i}):r>r\_{0}\} and let δi=r~i−r0\delta\_{i}=\tilde{r}\_{i}-r\_{0} satisfies δ1>δ2>0\delta\_{1}>\delta\_{2}>0.

Under these conditions, for a sufficiently large TT, we have

|  |  |  |
| --- | --- | --- |
|  | |π1​(0,T)|>|π2​(0,T)|.\displaystyle|\pi\_{1}(0,T)|>|\pi\_{2}(0,T)|. |  |

###### Proof.

See Appendix [A](https://arxiv.org/html/2512.00830v1#A1 "Appendix A Proof of Proposition 5.2 ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics").
∎

It is important to note that the conditions in Proposition [5.2](https://arxiv.org/html/2512.00830v1#S5.Thmtheorem2 "Proposition 5.2. ‣ 5 Comparative Statics of Equilibrium Strategies ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics") are compatible with first-order stochastic dominance. One can construct risk aversion distributions such that 𝑹1⪰1𝑹2\bm{R}\_{1}\succeq\_{1}\bm{R}\_{2} holds while the conditions in Proposition [5.2](https://arxiv.org/html/2512.00830v1#S5.Thmtheorem2 "Proposition 5.2. ‣ 5 Comparative Statics of Equilibrium Strategies ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics") are simultaneously satisfied. For instance, the parameters in Figure [1](https://arxiv.org/html/2512.00830v1#S5.F1 "Figure 1 ‣ 5 Comparative Statics of Equilibrium Strategies ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics") satisfy these conditions with r0=1r\_{0}=1, δ1=4\delta\_{1}=4 and δ2=1\delta\_{2}=1. Consequently, first-order stochastic dominance fails to rule out the reversal of investment magnitudes characterized by |π1​(0,T)|>|π2​(0,T)||\pi\_{1}(0,T)|>|\pi\_{2}(0,T)| for a sufficiently large TT.

However, we demonstrate that the desired monotonicity can be restored under a stronger stochastic order. Specifically, we introduce the concept of reverse hazard rate order and show that if 𝑹𝟏\bm{R\_{1}} dominates 𝑹𝟐\bm{R\_{2}} in this order, the intuition holds, i.e., |π1​(t)|≤|π2​(t)||\pi\_{1}(t)|\leq|\pi\_{2}(t)|.

###### Definition 5.3.

Let 𝐑𝟏\bm{R\_{1}} and 𝐑𝟐\bm{R\_{2}} be two random variables with cumulative distribution functions F𝐑𝟏F\_{\bm{R\_{1}}} and F𝐑𝟐F\_{\bm{R\_{2}}}, respectively. We say that 𝐑𝟏\bm{R\_{1}} dominates 𝐑𝟐\bm{R\_{2}} in the reverse hazard rate order, denoted as 𝐑𝟏⪰r​h𝐑𝟐\bm{R\_{1}}\succeq\_{rh}\bm{R\_{2}}, if the ratio

|  |  |  |
| --- | --- | --- |
|  | F𝑹𝟐​(x)F𝑹𝟏​(x)\displaystyle\frac{F\_{\bm{R\_{2}}}(x)}{F\_{\bm{R\_{1}}}(x)} |  |

is non-increasing in xx for all xx in the union of the supports of 𝐑𝟏\bm{R\_{1}} and 𝐑𝟐\bm{R\_{2}} where F𝐑𝟏​(x)>0F\_{\bm{R\_{1}}}(x)>0.

The next two lemmas, adapted from caperaa1988tail and wang2024weighted, characterize the reverse hazard rate order via expectation ratios and establish its connection to first-order stochastic dominance under weighted measures..

###### Lemma 5.4.

Let 𝐑𝟏\bm{R\_{1}} and 𝐑𝟐\bm{R\_{2}} be two random variables. Then R1⪰r​hR2R\_{1}\succeq\_{rh}R\_{2} if and only if

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[u​(𝑹𝟏)​w​(𝑹𝟏)]𝔼​[w​(𝑹𝟏)]≥𝔼​[u​(𝑹𝟐)​w​(𝑹𝟐)]𝔼​[w​(𝑹𝟐)],\displaystyle\frac{\mathbb{E}\left[u(\bm{R\_{1}})w(\bm{R\_{1}})\right]}{\mathbb{E}[w(\bm{R\_{1}})]}\geq\frac{\mathbb{E}[u(\bm{R\_{2}})w(\bm{R\_{2}})]}{\mathbb{E}[w(\bm{R\_{2}})]}, |  |

for all functions uu and ww for which the expectations exist, such that ww is positive, continuous, and decreasing, and uu is continuous and strictly increasing.

###### Lemma 5.5.

Let 𝐑𝟏\bm{R\_{1}} and 𝐑𝟐\bm{R\_{2}} be two random variables with cumulative distribution functions F𝐑𝟏F\_{\bm{R\_{1}}} and F𝐑𝟐F\_{\bm{R\_{2}}}, respectively. Assume that 𝐑𝟏⪰r​h𝐑𝟐\bm{R\_{1}}\succeq\_{rh}\bm{R\_{2}}. Let w​(⋅)w(\cdot) be a positive, continuous, and strictly decreasing function. Define the weighted probability measures F~i\tilde{F}\_{i} associated with 𝐑i\bm{R}\_{i} for i=1,2i=1,2 by

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​F~i​(x)=w​(x)​d​F~𝑹𝒊𝔼​[w​(𝑹𝒊)].\displaystyle\mathrm{d}\tilde{F}\_{i}(x)=\frac{w(x)\mathrm{d}\tilde{F}\_{\bm{R\_{i}}}}{\mathbb{E}\left[w(\bm{R\_{i}})\right]}. |  | (5.1) |

Then, 𝐑1\bm{R}\_{1} dominates 𝐑2\bm{R}\_{2} under the weighted measures in the sense of first-order stochastic dominance, i.e.,

|  |  |  |
| --- | --- | --- |
|  | F~1⪰1F~2.\displaystyle\tilde{F}\_{1}\succeq\_{1}\tilde{F}\_{2}. |  |

Equipped with this characterization, we are now ready to establish the monotonicity of the function hh defined in ([2.6](https://arxiv.org/html/2512.00830v1#S2.E6 "In Theorem 2.4. ‣ 2 Time-inconsistent portfolio selection with random risk aversion ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")) with respect to the risk aversion distribution in the sense of the reverse hazard rate order.

###### Proposition 5.6.

Given the function hh defined in ([2.6](https://arxiv.org/html/2512.00830v1#S2.E6 "In Theorem 2.4. ‣ 2 Time-inconsistent portfolio selection with random risk aversion ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")). We know that h​(x)h(x) is strictly increasing in xx. Moreover, fixing xx, h​(x)h(x) is strictly decreasing with respect to 𝐑\bm{R} in the sense of the reverse hazard rate order and distinct distributions. For notational simplicity, in the sequel, let hi​(⋅)h\_{i}(\cdot) and Fi​(⋅)F\_{i}(\cdot) denote the function h​(⋅)h(\cdot) and the function defined in Theorem [3.2](https://arxiv.org/html/2512.00830v1#S3.Thmtheorem2 "Theorem 3.2. ‣ 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics") corresponding to the random variable 𝐑i\bm{R}\_{i} for i=1,2i=1,2, respectively.

###### Proof.

Fix x>0x>0. Let 𝑹𝟏\bm{R\_{1}} and 𝑹𝟐{\bm{R\_{2}}} be two non-negative random variables such that 𝑹𝟏⪰r​h𝑹𝟐\bm{R\_{1}}\succeq\_{rh}\bm{R\_{2}} and their distributions are distinct. According to Lemma [5.4](https://arxiv.org/html/2512.00830v1#S5.Thmtheorem4 "Lemma 5.4. ‣ 5 Comparative Statics of Equilibrium Strategies ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics"), let u​(r)=ru(r)=r and w​(r)=exp⁡(−12​r​x)w(r)=\exp(-\frac{1}{2}rx).
Note that u​(r)u(r) is a strictly increasing function, and for v>0v>0, w​(r)w(r) is a positive, continuous, and strictly decreasing function of rr. Substituting them into this inequality, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝑹𝟏​exp⁡(−12​𝑹𝟏​x)]𝔼​[exp⁡(−12​𝑹𝟏​x)]≥𝔼​[𝑹𝟐​exp⁡(−12​𝑹𝟐​x)]𝔼​[exp⁡(−12​𝑹𝟐​x)].\displaystyle\frac{\mathbb{E}[\bm{R\_{1}}\exp(-\frac{1}{2}\bm{R\_{1}}x)]}{\mathbb{E}[\exp(-\frac{1}{2}\bm{R\_{1}}x)]}\geq\frac{\mathbb{E}[\bm{R\_{2}}\exp(-\frac{1}{2}\bm{R\_{2}}x)]}{\mathbb{E}[\exp(-\frac{1}{2}\bm{R\_{2}}x)]}. |  |

Moreover, assume that the equality holds. Define the weighted probability measures F~i\tilde{F}\_{i} for i=1,2i=1,2 by ([5.1](https://arxiv.org/html/2512.00830v1#S5.E1 "In Lemma 5.5. ‣ 5 Comparative Statics of Equilibrium Strategies ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")). The given condition is equivalent to 𝔼F~1​[𝑹𝟏]=𝔼F~2​[𝑹𝟏]\mathbb{E}\_{\tilde{F}\_{1}}[\bm{R\_{1}}]=\mathbb{E}\_{\tilde{F}\_{2}}[\bm{R\_{1}}]. From Lemma [5.5](https://arxiv.org/html/2512.00830v1#S5.Thmtheorem5 "Lemma 5.5. ‣ 5 Comparative Statics of Equilibrium Strategies ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics"), we have F~1⪰1F~2\tilde{F}\_{1}\succeq\_{1}\tilde{F}\_{2} and consequently, d​F~1​(r)=d​F~2​(r)\mathrm{d}\tilde{F}\_{1}(r)=\mathrm{d}\tilde{F}\_{2}(r). Given that w​(r)w(r) is positive, this implies d​F~1𝔼​[w​(𝑹𝟏)]=d​F~2𝔼​[w​(𝑹𝟐)]\frac{\mathrm{d}\tilde{F}\_{1}}{\mathbb{E}\left[w(\bm{R\_{1}})\right]}=\frac{\mathrm{d}\tilde{F}\_{2}}{\mathbb{E}\left[w(\bm{R\_{2}})\right]}. Integrating both sides over the entire support and using the property ∫dF~i​(x)=1\int\mathrm{d}\tilde{F}\_{i}(x)=1, we obtain 1=𝔼​[w​(𝑹𝟏)]𝔼​[w​(𝑹𝟐)]1=\frac{\mathbb{E}\left[w(\bm{R\_{1}})\right]}{\mathbb{E}\left[w(\bm{R\_{2}})\right]}, which implies 𝔼​[w​(𝑹𝟏)]=𝔼​[w​(𝑹𝟐)]\mathbb{E}\left[w(\bm{R\_{1}})\right]=\mathbb{E}\left[w(\bm{R\_{2}})\right]. Substituting this back yields d​F𝑹𝟏​(r)=d​F𝑹𝟐​(r)\mathrm{d}F\_{\bm{R\_{1}}}(r)=\mathrm{d}F\_{\bm{R\_{2}}}(r), confirming that F𝑹𝟏​(r)=F𝑹𝟐​(r)F\_{\bm{R\_{1}}}(r)=F\_{\bm{R\_{2}}}(r). This contradicts the different distributions of 𝑹𝟏\bm{R\_{1}} and 𝑹𝟐\bm{R\_{2}}. Thus, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝑹𝟏​exp⁡(−12​𝑹𝟏​x)]𝔼​[exp⁡(−12​𝑹𝟏​x)]>𝔼​[𝑹𝟐​exp⁡(−12​𝑹𝟐​x)]𝔼​[exp⁡(−12​𝑹𝟐​x)],\displaystyle\frac{\mathbb{E}[\bm{R\_{1}}\exp(-\frac{1}{2}\bm{R\_{1}}x)]}{\mathbb{E}[\exp(-\frac{1}{2}\bm{R\_{1}}x)]}>\frac{\mathbb{E}[\bm{R\_{2}}\exp(-\frac{1}{2}\bm{R\_{2}}x)]}{\mathbb{E}[\exp(-\frac{1}{2}\bm{R\_{2}}x)]}, |  |

and equivalently,

|  |  |  |
| --- | --- | --- |
|  | h1​(x)<h2​(x).\displaystyle h\_{1}(x)<h\_{2}(x). |  |

∎

The following proposition compares the equilibrium strategies of two investors ranked by the reverse hazard rate order.

###### Proposition 5.7.

Let 𝐑𝟏\bm{R\_{1}} and 𝐑𝟐{\bm{R\_{2}}} be two non-negative random variables with 𝔼​[𝐑𝐢]<+∞\mathbb{E}\left[\bm{R\_{i}}\right]<+\infty (i=1,2i=1,2), such that 𝐑𝟏⪰r​h𝐑𝟐\bm{R\_{1}}\succeq\_{rh}\bm{R\_{2}} and their distributions are distinct. Let πi​(t)=(σ⊤)−1​ai​(t)\pi\_{i}(t)=(\sigma^{\top})^{-1}a\_{i}(t) be the corresponding deterministic equilibrium strategies. For any t∈[0,T)t\in[0,T), the magnitude of ai​(t)a\_{i}(t) satisfies

|  |  |  |
| --- | --- | --- |
|  | |a1​(t)|≤|a2​(t)|.\displaystyle|a\_{1}(t)|\leq|a\_{2}(t)|. |  |

Moreover, if λ​(t)≠0\lambda(t)\neq 0, the inequality is strict. As a result, the investor with higher risk aversion adopts a less aggressive equilibrium strategy. i.e., |π1​(t)|≤|π2​(t)||\pi\_{1}(t)|\leq|\pi\_{2}(t)|.

###### Proof.

Since h1​(x)<h2​(x)h\_{1}(x)<h\_{2}(x) for all positive ss, it follows that F1​(y)>F2​(y)F\_{1}(y)>F\_{2}(y) for all y>0y>0. This implies that the inverse functions satisfy F1−1​(z)<F2−1​(z)F\_{1}^{-1}(z)<F\_{2}^{-1}(z) for all z>0z>0. From Theorem [3.2](https://arxiv.org/html/2512.00830v1#S3.Thmtheorem2 "Theorem 3.2. ‣ 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics") (1), we have vi​(t)=Fi−1​(Ψ​(t))v\_{i}(t)=F\_{i}^{-1}(\Psi(t)), where Ψ​(t)=∫tT|λ​(s)|2​𝑑s\Psi(t)=\int\_{t}^{T}|\lambda(s)|^{2}ds and vi​(t)=∫tT|ai​(s)|2​dsv\_{i}(t)=\int\_{t}^{T}|a\_{i}(s)|^{2}\mathrm{d}s. Consequently, monotonicity of the inverse functions implies v1​(t)≤v2​(t)v\_{1}(t)\leq v\_{2}(t). By ([2.5](https://arxiv.org/html/2512.00830v1#S2.E5 "In Theorem 2.4. ‣ 2 Time-inconsistent portfolio selection with random risk aversion ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")), we have |ai​(t)|=h​(vi​(t),𝑹𝒊)​|λ​(t)||a\_{i}(t)|=h(v\_{i}(t),\bm{R\_{i}})|\lambda(t)|. From Proposition [5.6](https://arxiv.org/html/2512.00830v1#S5.Thmtheorem6 "Proposition 5.6. ‣ 5 Comparative Statics of Equilibrium Strategies ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics"), we know that h1​(v1​(t))<h2​(v1​(t))h\_{1}(v\_{1}(t))<h\_{2}(v\_{1}(t)). Since v1​(t)≤v2​(t)v\_{1}(t)\leq v\_{2}(t), it holds that h2​(v1​(t))≤h2​(v2​(t))h\_{2}(v\_{1}(t))\leq h\_{2}(v\_{2}(t)). Combining these relations yields h1​(v1​(t))<h2​(v2​(t))h\_{1}(v\_{1}(t))<h\_{2}(v\_{2}(t)). Multiplying by |λ​(t)||\lambda(t)|, we obtain |a1​(t)|≤|a2​(t)||a\_{1}(t)|\leq|a\_{2}(t)|. If λ​(t)≠0\lambda(t)\neq 0, the strict inequality |a1​(t)|<|a2​(t)||a\_{1}(t)|<|a\_{2}(t)| is preserved.
∎

For the case where the expected risk aversion is infinite, assume that the optimal equilibria exist for both 𝑹1\bm{R}\_{1} and 𝑹2\bm{R}\_{2}. Let ai​(t)a\_{i}(t) denote the deterministic coefficient corresponding to the optimal equilibrium strategy for 𝑹i\bm{R}\_{i} (i=1,2i=1,2). Note that φ​(0)=min⁡{t∈[0,T]∣Ψ​(t)=0}\varphi(0)=\min\{t\in[0,T]\mid\Psi(t)=0\} is determined solely by the market parameters and is therefore identical for both investors. Consequently, we can establish the comparative result by examining the magnitudes of ai​(t)a\_{i}(t) on the intervals [0,φ​(0))[0,\varphi(0)) and [φ​(0),T][\varphi(0),T] separately.
Specifically, on the interval [0,φ​(0))[0,\varphi(0)), the analysis parallels the finite expectation case derived in Proposition [5.7](https://arxiv.org/html/2512.00830v1#S5.Thmtheorem7 "Proposition 5.7. ‣ 5 Comparative Statics of Equilibrium Strategies ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics"), and thus the monotonicity of the equilibrium strategies is preserved.
On the interval [φ​(0),T][\varphi(0),T], the definition of φ​(0)\varphi(0) implies that λ​(t)=0\lambda(t)=0 almost everywhere. Consequently, the equilibrium strategies for both investors vanish, trivially satisfying the comparison inequality. Based on this decomposition, we have the following corollary.

###### Corollary 5.8.

Let 𝐑1\bm{R}\_{1} and 𝐑2\bm{R}\_{2} be two non-negative random variables with 𝔼​[𝐑i]=∞\mathbb{E}[\bm{R}\_{i}]=\infty (i=1,2i=1,2), such that 𝐑1⪰r​h𝐑2\bm{R}\_{1}\succeq\_{rh}\bm{R}\_{2} and their distributions are distinct. Assume that the optimal equilibria exist for both investors (i.e., Fi​(∞)>Ψ​(0)F\_{i}(\infty)>\Psi(0), i=1,2i=1,2). Let πi​(t)\pi\_{i}(t) be the corresponding deterministic optimal equilibrium strategies. Then, for any t∈[0,T)t\in[0,T), the magnitude of πi​(t)\pi\_{i}(t) satisfies

|  |  |  |
| --- | --- | --- |
|  | |π1​(t)|≤|π2​(t)|.\displaystyle|\pi\_{1}(t)|\leq|\pi\_{2}(t)|. |  |

Moreover, if λ​(t)≠0\lambda(t)\neq 0, the inequality is strict.

## Appendix A Proof of Proposition [5.2](https://arxiv.org/html/2512.00830v1#S5.Thmtheorem2 "Proposition 5.2. ‣ 5 Comparative Statics of Equilibrium Strategies ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")

We first establish a technical lemma.

###### Lemma A.1.

Let 𝐑1\bm{R}\_{1} and 𝐑2\bm{R}\_{2} be two non-negative random variables satisfying the conditions in Proposition [5.2](https://arxiv.org/html/2512.00830v1#S5.Thmtheorem2 "Proposition 5.2. ‣ 5 Comparative Statics of Equilibrium Strategies ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics"). Let Xi=𝐑i−r0X\_{i}=\bm{R}\_{i}-r\_{0} and define Qi​(s)=𝔼​[Xi​e−12​Xi​s]𝔼​[e−12​Xi​s]Q\_{i}(s)=\frac{\mathbb{E}[X\_{i}e^{-\frac{1}{2}X\_{i}s}]}{\mathbb{E}[e^{-\frac{1}{2}X\_{i}s}]}. Then, the following properties hold:

1. (1)

   As s→∞s\to\infty, Qi​(s)→0Q\_{i}(s)\to 0. Specifically, for sufficiently large ss, Qi​(s)≤Mi​e−12​δi​sQ\_{i}(s)\leq M\_{i}e^{-\frac{1}{2}\delta\_{i}s} for some constant MiM\_{i}.
2. (2)

   The integral ∫0∞(hi−2​(s)−r02)​𝑑s\int\_{0}^{\infty}(h\_{i}^{-2}(s)-r\_{0}^{2})ds converges to a finite constant KiK\_{i}.
3. (3)

   For any s1s\_{1}, s2s\_{2} and ε>0\varepsilon>0, the ratio Qi​(si)Q\_{i}(s\_{i}) satisfies Q1​(s1)Q2​(s2)≤C1​e−12​δ1​s1C2​e−12​(δ2+ε)​s2\dfrac{Q\_{1}(s\_{1})}{Q\_{2}(s\_{2})}\leq\dfrac{C\_{1}e^{-\frac{1}{2}\delta\_{1}s\_{1}}}{C\_{2}e^{-\frac{1}{2}(\delta\_{2}+\varepsilon)s\_{2}}}, where C1C\_{1} and C2C\_{2} are constants.

###### Proof.

We first analyze the asymptotic bounds of Qi​(s)Q\_{i}(s). According to (2) in Proposition [5.2](https://arxiv.org/html/2512.00830v1#S5.Thmtheorem2 "Proposition 5.2. ‣ 5 Comparative Statics of Equilibrium Strategies ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics"), XiX\_{i} has a probability mass pip\_{i} at 0. Using the Dominated Convergence Theorem, the denominator satisfies lims→∞𝔼​[e−12​Xi​s]=pi\lim\_{s\to\infty}\mathbb{E}[e^{-\frac{1}{2}X\_{i}s}]=p\_{i}. Thus, there exists an S>0S>0 such that for all s>Ss>S, the denominator is bounded below by pi2\frac{p\_{i}}{2}.
For the numerator, by (3) in Proposition [5.2](https://arxiv.org/html/2512.00830v1#S5.Thmtheorem2 "Proposition 5.2. ‣ 5 Comparative Statics of Equilibrium Strategies ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics"), the support of XiX\_{i} on (0,∞)(0,\infty) is contained in [δi,∞)[\delta\_{i},\infty). Thus, we derive the upper bound

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Xi​e−12​Xi​s]=∫δi∞x​e−12​x​s​dFXi​(x)≤e−12​δi​s​∫δi∞x​dFXi​(x)=Ci′​e−12​δi​s,\displaystyle\mathbb{E}[X\_{i}e^{-\frac{1}{2}X\_{i}s}]=\int\_{\delta\_{i}}^{\infty}xe^{-\frac{1}{2}xs}\mathrm{d}F\_{X\_{i}}(x)\leq e^{-\frac{1}{2}\delta\_{i}s}\int\_{\delta\_{i}}^{\infty}x\mathrm{d}F\_{X\_{i}}(x)=C\_{i}^{\prime}e^{-\frac{1}{2}\delta\_{i}s}, |  |

where Ci′=𝔼​[Xi​𝕀{Xi≥δi}]<∞C\_{i}^{\prime}=\mathbb{E}[X\_{i}\mathbb{I}\_{\{X\_{i}\geq\delta\_{i}\}}]<\infty under the assumption of finite expectation. Combining these, for s>Ss>S, we have Qi​(s)≤Ci′​e−12​δi​spi2≜Mi​e−12​δi​sQ\_{i}(s)\leq\dfrac{C\_{i}^{\prime}e^{-\frac{1}{2}\delta\_{i}s}}{\frac{p\_{i}}{2}}\triangleq M\_{i}e^{-\frac{1}{2}\delta\_{i}s}. This proves the first property.

Next, we verify the convergence of the integral. We know hi−2​(s)−r02=2​r0​Qi​(s)+Qi2​(s)h\_{i}^{-2}(s)-r\_{0}^{2}=2r\_{0}Q\_{i}(s)+Q\_{i}^{2}(s). Using the bound derived above, we have

|  |  |  |
| --- | --- | --- |
|  | 2​r0​Qi​(s)+Qi2​(s)≤2​r0​Mi​e−12​δi​s+Mi2​e−δi​s.\displaystyle 2r\_{0}Q\_{i}(s)+Q\_{i}^{2}(s)\leq 2r\_{0}M\_{i}e^{-\frac{1}{2}\delta\_{i}s}+M\_{i}^{2}e^{-\delta\_{i}s}. |  |

Since δi>0\delta\_{i}>0, the exponential functions are integrable on [S,∞)[S,\infty). Furthermore, since Qi​(s)Q\_{i}(s) is continuous on the finite interval [0,S][0,S], the total integral over [0,∞)[0,\infty) converges. We denote this finite integral by KiK\_{i}.

Finally, to compare the ratio Q1​(s1)Q2​(s2)\frac{Q\_{1}(s\_{1})}{Q\_{2}(s\_{2})}, we need a lower bound for the numerator of Q2Q\_{2}. For an arbitrary small ε>0\varepsilon>0, by definition of the support, pε,2≜P​(δ2≤X2<δ2+ε)>0p\_{\varepsilon,2}\triangleq P(\delta\_{2}\leq X\_{2}<\delta\_{2}+\varepsilon)>0. Restricting the integration to this interval yields

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[X2​e−12​X2​s]≥∫δ2δ2+εx​e−12​x​s​dFX2​(x)≥δ2​e−12​(δ2+ε)​s​pε,2.\displaystyle\mathbb{E}[X\_{2}e^{-\frac{1}{2}X\_{2}s}]\geq\int\_{\delta\_{2}}^{\delta\_{2}+\varepsilon}xe^{-\frac{1}{2}xs}\mathrm{d}F\_{X\_{2}}(x)\geq\delta\_{2}e^{-\frac{1}{2}(\delta\_{2}+\varepsilon)s}p\_{\varepsilon,2}. |  |

Using the upper bound for Q1Q\_{1} and this lower bound for Q2Q\_{2}, we have

|  |  |  |
| --- | --- | --- |
|  | Q1​(s1)Q2​(s2)≤C1​e−12​δ1​s1C2​e−12​(δ2+ε)​s2,\displaystyle\dfrac{Q\_{1}(s\_{1})}{Q\_{2}(s\_{2})}\leq\dfrac{C\_{1}e^{-\frac{1}{2}\delta\_{1}s\_{1}}}{C\_{2}e^{-\frac{1}{2}(\delta\_{2}+\varepsilon)s\_{2}}}, |  |

where C1C\_{1} and C2C\_{2} are constants.
∎

Now we return to prove Proposition [5.2](https://arxiv.org/html/2512.00830v1#S5.Thmtheorem2 "Proposition 5.2. ‣ 5 Comparative Statics of Equilibrium Strategies ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics").

Initially, by noting that hi​(s)=(r0+Qi​(s))−1h\_{i}(s)=(r\_{0}+Q\_{i}(s))^{-1} and applying the limit from Lemma [A.1](https://arxiv.org/html/2512.00830v1#A1.Thmtheorem1 "Lemma A.1. ‣ Appendix A Proof of Proposition 5.2 ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics") (1), we establish the asymptotic behavior lims→∞hi​(s)=1r0\lim\_{s\to\infty}h\_{i}(s)=\frac{1}{r\_{0}}. Since r0>0r\_{0}>0, this implies that the integrand hi−2​(s)h\_{i}^{-2}(s) converges to a positive constant r02r\_{0}^{2}. Therefore, the integral ∫0∞hi−2​(s)​𝑑s\int\_{0}^{\infty}h\_{i}^{-2}(s)ds diverges, confirming Fi​(∞)=∞F\_{i}(\infty)=\infty. Consequently, Theorem [3.3](https://arxiv.org/html/2512.00830v1#S3.Thmtheorem3 "Theorem 3.3. ‣ 3 Equilibrium Analysis and Characterization of Solutions ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics") (1) guarantees the existence of a unique equilibrium πi\pi\_{i} for 𝑹i\bm{R}\_{i}.

Based on πi=(σ⊤)−1​ai{\pi}\_{i}=(\sigma^{\top})^{-1}a\_{i}, we only need to compare aia\_{i}. According to ([2.5](https://arxiv.org/html/2512.00830v1#S2.E5 "In Theorem 2.4. ‣ 2 Time-inconsistent portfolio selection with random risk aversion ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")), we have |ai​(0,T)|=hi​(vi​(0,T))​|λ​(0)||a\_{i}(0,T)|=h\_{i}(v\_{i}(0,T))|\lambda(0)|. To prove |a1​(0,T)|>|a2​(0,T)||a\_{1}(0,T)|>|a\_{2}(0,T)|, we must establish the asymptotic behavior of vi​(0,T)v\_{i}(0,T) and then compare the values of hi​(vi​(0,T))h\_{i}(v\_{i}(0,T)) based on the distribution properties of 𝑹i\bm{R}\_{i}. Based on Lemma [A.1](https://arxiv.org/html/2512.00830v1#A1.Thmtheorem1 "Lemma A.1. ‣ Appendix A Proof of Proposition 5.2 ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics"), we proceed in two steps.

First, we establish the asymptotic relationship between the state variables v1​(0,T)v\_{1}(0,T) and v2​(0,T)v\_{2}(0,T). We have the integral equation ∫0vi​(0,T)hi−2​(s)​𝑑s=Ψ​(0)\int\_{0}^{v\_{i}(0,T)}h\_{i}^{-2}(s)ds=\Psi(0). Rewrite this as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫0vi​(0,T)(r02+(hi−2​(s)−r02))​ds=r02​vi​(0,T)+∫0vi​(0,T)(hi−2​(s)−r02)​ds=Ψ​(0,T),\displaystyle\int\_{0}^{v\_{i}(0,T)}(r\_{0}^{2}+(h\_{i}^{-2}(s)-r\_{0}^{2}))\mathrm{d}s=r\_{0}^{2}v\_{i}(0,T)+\int\_{0}^{v\_{i}(0,T)}(h\_{i}^{-2}(s)-r\_{0}^{2})\mathrm{d}s=\Psi(0,T), |  | (A.1) |

and using Lemma [A.1](https://arxiv.org/html/2512.00830v1#A1.Thmtheorem1 "Lemma A.1. ‣ Appendix A Proof of Proposition 5.2 ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics") (2), we note that the integral ∫0∞(hi−2​(s)−r02)​ds=Ki\int\_{0}^{\infty}(h\_{i}^{-2}(s)-r\_{0}^{2})\mathrm{d}s=K\_{i} converges. We define the tail integral Ri​(y)≜∫y∞(hi−2​(s)−r02)​dsR\_{i}(y)\triangleq\int\_{y}^{\infty}(h\_{i}^{-2}(s)-r\_{0}^{2})\mathrm{d}s, which satisfies limy→∞Ri​(y)=0\lim\_{y\to\infty}R\_{i}(y)=0. ([A.1](https://arxiv.org/html/2512.00830v1#A1.E1 "In Appendix A Proof of Proposition 5.2 ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ψ​(0,T)=r02​vi​(0,T)+Ki−Ri​(vi​(0,T)).\displaystyle\Psi(0,T)=r\_{0}^{2}v\_{i}(0,T)+K\_{i}-R\_{i}(v\_{i}(0,T)). |  | (A.2) |

Moreover, since vi​(0,T)=Fi−1​(Ψ​(0,T))v\_{i}(0,T)=F\_{i}^{-1}(\Psi(0,T)), Fi​(∞)=∞F\_{i}(\infty)=\infty and limT→∞Ψ​(0,T)=∞\lim\_{T\to\infty}\Psi(0,T)=\infty, it follows that limT→∞vi​(0,T)=∞\lim\_{T\to\infty}v\_{i}(0,T)=\infty.
Equating ([A.2](https://arxiv.org/html/2512.00830v1#A1.E2 "In Appendix A Proof of Proposition 5.2 ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics")) for i=1i=1 and i=2i=2, we obtain

|  |  |  |
| --- | --- | --- |
|  | v1​(0,T)=v2​(0,T)+K2−K1r02+R2​(v2​(0,T))−R1​(v1​(0,T))r02.\displaystyle v\_{1}(0,T)=v\_{2}(0,T)+\dfrac{K\_{2}-K\_{1}}{r\_{0}^{2}}+\dfrac{R\_{2}(v\_{2}(0,T))-R\_{1}(v\_{1}(0,T))}{r\_{0}^{2}}. |  |

Let Δ​K=K2−K1r02\Delta K=\dfrac{K\_{2}-K\_{1}}{r\_{0}^{2}} and ξ​(T)=R2​(v2​(0,T))−R1​(v1​(0,T))r02\xi(T)=\dfrac{R\_{2}(v\_{2}(0,T))-R\_{1}(v\_{1}(0,T))}{r\_{0}^{2}}. Since vi​(0,T)→∞v\_{i}(0,T)\to\infty as T→∞T\to\infty, the tail difference term ξ​(T)\xi(T) tends to 0. Thus, we have the exact relationship v1​(0,T)=v2​(0,T)+Δ​K+ξ​(T)v\_{1}(0,T)=v\_{2}(0,T)+\Delta K+\xi(T).

Second, we compare h1​(v1​(0,T))h\_{1}(v\_{1}(0,T)) and h2​(v2​(0,T))h\_{2}(v\_{2}(0,T)). Since hi​(s)=(r0+Qi​(s))−1h\_{i}(s)=(r\_{0}+Q\_{i}(s))^{-1}, this reduces to comparing Q1​(v1​(0,T))Q\_{1}(v\_{1}(0,T)) and Q2​(v2​(0,T))Q\_{2}(v\_{2}(0,T)).
Using the bounds established in Lemma [A.1](https://arxiv.org/html/2512.00830v1#A1.Thmtheorem1 "Lemma A.1. ‣ Appendix A Proof of Proposition 5.2 ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics") (3), we have

|  |  |  |
| --- | --- | --- |
|  | Q1​(v1​(0,T))Q2​(v2​(0,T))≤C1​e−12​δ1​v1​(0,T)C2​e−12​(δ2+ε)​v2​(0,T).\displaystyle\dfrac{Q\_{1}(v\_{1}(0,T))}{Q\_{2}(v\_{2}(0,T))}\leq\dfrac{C\_{1}e^{-\frac{1}{2}\delta\_{1}v\_{1}(0,T)}}{C\_{2}e^{-\frac{1}{2}(\delta\_{2}+\varepsilon)v\_{2}(0,T)}}. |  |

Substituting v1​(0,T)=v2​(0,T)+Δ​K+ξ​(T)v\_{1}(0,T)=v\_{2}(0,T)+\Delta K+\xi(T) into the exponent, we have

|  |  |  |
| --- | --- | --- |
|  | Q1​(v1​(0,T))Q2​(v2​(0,T))≤C1C2​e−12​δ1​(Δ​K+ξ​(T))⋅e−12​(δ1−δ2−ε)​v2​(0,T).\displaystyle\dfrac{Q\_{1}(v\_{1}(0,T))}{Q\_{2}(v\_{2}(0,T))}\leq\dfrac{C\_{1}}{C\_{2}}e^{-\frac{1}{2}\delta\_{1}(\Delta K+\xi(T))}\cdot e^{-\frac{1}{2}(\delta\_{1}-\delta\_{2}-\varepsilon)v\_{2}(0,T)}. |  |

Since limT→∞ξ​(T)=0\lim\_{T\to\infty}\xi(T)=0, the first exponential term converges to a finite positive constant. As shown in the Lemma [A.1](https://arxiv.org/html/2512.00830v1#A1.Thmtheorem1 "Lemma A.1. ‣ Appendix A Proof of Proposition 5.2 ‣ Equilibrium Investment with Random Risk Aversion: (Non-)uniqueness, Optimality, and Comparative Statics"), we can strictly choose ε\varepsilon such that δ1−δ2−ε>0\delta\_{1}-\delta\_{2}-\varepsilon>0. Consequently, as v2​(0,T)→∞v\_{2}(0,T)\to\infty, the second term tends to 0 and we have Q1​(v1​(0,T))Q2​(v2​(0,T))→0\frac{Q\_{1}(v\_{1}(0,T))}{Q\_{2}(v\_{2}(0,T))}\to 0.

This implies for sufficiently large TT, Q1​(v1​(0,T))<Q2​(v2​(0,T))Q\_{1}(v\_{1}(0,T))<Q\_{2}(v\_{2}(0,T)). Since hi​(x)=(r0+Qi​(x))−1h\_{i}(x)=(r\_{0}+Q\_{i}(x))^{-1} is strictly decreasing in QiQ\_{i}, we have h1​(v1​(0,T))>h2​(v2​(0,T))h\_{1}(v\_{1}(0,T))>h\_{2}(v\_{2}(0,T)). Consequently, |a1​(0,T)|>|a2​(0,T)||a\_{1}(0,T)|>|a\_{2}(0,T)| since λ​(0)≠0\lambda(0)\neq 0, and equivalently, |π1​(0,T)|>|π2​(0,T)||\pi\_{1}(0,T)|>|\pi\_{2}(0,T)|.