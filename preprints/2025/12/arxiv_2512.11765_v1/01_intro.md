---
authors:
- Marcel Nutz
- Alessandro Prosperi
doc_id: arxiv:2512.11765v1
family_id: arxiv:2512.11765
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: High-Frequency Analysis of a Trading Game with Transient Price Impact
url_abs: http://arxiv.org/abs/2512.11765v1
url_html: https://arxiv.org/html/2512.11765v1
venue: arXiv q-fin
version: 1
year: 2025
---


Marcel Nutz
Departments of Statistics and Mathematics, Columbia University
[mnutz@columbia.edu](mailto:mnutz@columbia.edu)
 and 
Alessandro Prosperi
Department of Statistics, Columbia University
[alessandro.prosperi@columbia.edu](mailto:alessandro.prosperi@columbia.edu)

(Date: December 12, 2025)

###### Abstract.

…

###### Abstract.

We study the high-frequency limit of an nn-trader optimal execution game in discrete time. Traders face transient price impact of Obizhaeva–Wang type in addition to quadratic instantaneous trading costs θ​(Δ​Xt)2\theta(\Delta X\_{t})^{2} on each transaction Δ​Xt\Delta X\_{t}. There is a unique Nash equilibrium in which traders choose liquidation strategies minimizing expected execution costs. In the high-frequency limit where the grid of trading dates converges to the continuous interval [0,T][0,T], the discrete equilibrium inventories converge at rate 1/N1/N to the continuous-time equilibrium of an Obizhaeva–Wang model with additional quadratic costs ϑ0​(Δ​X0)2\vartheta\_{0}(\Delta X\_{0})^{2} and ϑT​(Δ​XT)2\vartheta\_{T}(\Delta X\_{T})^{2} on initial and terminal block trades, where ϑ0=(n−1)/2\vartheta\_{0}=(n-1)/2 and ϑT=1/2\vartheta\_{T}=1/2. The latter model was introduced by Campbell and Nutz as the limit of continuous-time equilibria with vanishing instantaneous costs. Our results extend and refine previous results of Schied, Strehle, and Zhang for the particular case n=2n=2 where ϑ0=ϑT=1/2\vartheta\_{0}=\vartheta\_{T}=1/2. In particular, we show how the coefficients ϑ0=(n−1)/2\vartheta\_{0}=(n-1)/2 and ϑT=1/2\vartheta\_{T}=1/2 arise endogenously in the high-frequency limit: the initial and terminal block costs of the continuous-time model are identified as the limits of the cumulative discrete instantaneous costs incurred over small neighborhoods of 0 and TT, respectively, and these limits are independent of θ>0\theta>0. By contrast, when θ=0\theta=0 the discrete-time equilibrium strategies and costs exhibit persistent oscillations and admit no high-frequency limit, mirroring the non-existence of continuous-time equilibria without boundary block costs. Our results show that two different types of trading frictions—a fine time discretization and small instantaneous costs in continuous time—have similar regularizing effects and, in the limiting regime, select a canonical continuous-time model with transient price impact and endogenous block costs.

###### Key words and phrases:

NN-Player Game; Optimal Execution; Transient Price Impact

###### 2020 Mathematics Subject Classification:

91G10; 91A06; 91A15

MN was supported by NSF Grants DMS-2407074 and DMS-2106056.

## 1. Introduction

Transaction costs are a key consideration for financial institutions. In equity trading, the lion’s share of costs is due to price impact, i.e., the fact that buy (sell) orders tend to push prices up (down). Following [[2](https://arxiv.org/html/2512.11765v1#bib.bib2)], price impact is often modeled in reduced form, positing that each atomic trade mechanically leads to a price change. Later models incorporate price resilience (transient impact), meaning that prices revert over time once the buying or selling pressure ceases. The most tractable formulation is the Obizhaeva–Wang model [[17](https://arxiv.org/html/2512.11765v1#bib.bib17)], which uses an exponential decay kernel. Starting with [[9](https://arxiv.org/html/2512.11765v1#bib.bib9), [11](https://arxiv.org/html/2512.11765v1#bib.bib11)], numerous works have added quadratic instantaneous costs on the trading rate to the Obizhaeva–Wang impact cost. As illustrated in [[11](https://arxiv.org/html/2512.11765v1#bib.bib11)], this “regularizes” the problem and leads to smoother optimal trading strategies; see also [[13](https://arxiv.org/html/2512.11765v1#bib.bib13)]. We refer to [[6](https://arxiv.org/html/2512.11765v1#bib.bib6), [25](https://arxiv.org/html/2512.11765v1#bib.bib25)] for further background and extensive references on price impact. Strategic interactions between several large traders are studied in game-theoretic models. This branch of the literature emerged to study predatory trading, where one trader exploits the price impact of a second trader who needs to unwind a position [[18](https://arxiv.org/html/2512.11765v1#bib.bib18), [5](https://arxiv.org/html/2512.11765v1#bib.bib5)]. For the Obizhaeva–Wang model regularized by quadratic instantaneous costs, [[23](https://arxiv.org/html/2512.11765v1#bib.bib23)] shows that there is a unique Nash equilibrium, whose closed form is provided in [[3](https://arxiv.org/html/2512.11765v1#bib.bib3)]. While these works follow the optimal execution literature in assuming that the unaffected price is a martingale, they have been generalized in several directions, such as incorporating alpha signals [[16](https://arxiv.org/html/2512.11765v1#bib.bib16)], alpha signals and non-exponential decay kernels [[1](https://arxiv.org/html/2512.11765v1#bib.bib1)], or self-exciting order flow [[8](https://arxiv.org/html/2512.11765v1#bib.bib8)].

The goal of the present paper is to shed light on the Nash equilibria of trading games in the Obizhaeva–Wang model without regularization. Surprisingly, a naive formulation in continuous time does not admit an equilibrium, as established by [[19](https://arxiv.org/html/2512.11765v1#bib.bib19)] and [[3](https://arxiv.org/html/2512.11765v1#bib.bib3)]. They further show that existence is restored if very specific costs on block trades are added to the Obizhaeva–Wang impact cost. Namely, in a game with nn traders, a block trade of size Δ​X0\Delta X\_{0} at the initial time t=0t=0 is charged ϑ0​(Δ​X0)2\vartheta\_{0}(\Delta X\_{0})^{2}, where ϑ0:=(n−1)/2\vartheta\_{0}\mathrel{\mathop{\ordinarycolon}}=(n-1)/2, and a block trade Δ​XT\Delta X\_{T} at the terminal time t=Tt=T is charged ϑT​(Δ​XT)2\vartheta\_{T}(\Delta X\_{T})^{2}, where ϑT:=1/2\vartheta\_{T}\mathrel{\mathop{\ordinarycolon}}=1/2 (up to reparametrizing time). On the open interval (0,T)(0,T), no additional costs are charged. For n=2n=2 traders, as studied in [[19](https://arxiv.org/html/2512.11765v1#bib.bib19)], the initial and terminal costs coincide. For general nn, as studied in [[3](https://arxiv.org/html/2512.11765v1#bib.bib3)], the two costs differ, with ϑ0\vartheta\_{0} depending directly on nn, making this adjustment even more surprising. Conversely, these works show that for general initial inventories of the traders, no equilibrium exists unless ϑ0\vartheta\_{0} and ϑT\vartheta\_{T} have exactly the stated values. The two works further motivate their models by asymptotic considerations. On the one hand, [[19](https://arxiv.org/html/2512.11765v1#bib.bib19)] shows that their continuous-time equilibrium strategies are the high-frequency limits of *discrete-time* equilibria. The discrete-time models use Obizhaeva–Wang impact and an additional quadratic instantaneous cost θ​(Δ​Xt)2\theta(\Delta X\_{t})^{2}, where θ>0\theta>0 is arbitrary and fixed. The authors further show that without instantaneous costs, the high-frequency limit does not exist because strategies oscillate. These results build on [[21](https://arxiv.org/html/2512.11765v1#bib.bib21), [22](https://arxiv.org/html/2512.11765v1#bib.bib22), [20](https://arxiv.org/html/2512.11765v1#bib.bib20)], which documented such oscillations in different contexts; see also [[15](https://arxiv.org/html/2512.11765v1#bib.bib15)]. On the other hand, [[3](https://arxiv.org/html/2512.11765v1#bib.bib3)] shows that their equilibrium is the limit of *continuous-time* equilibria with quadratic instantaneous costs ε​(d​Xt/d​t)2\varepsilon(dX\_{t}/dt)^{2} as ε→0\varepsilon\to 0.

The present work refines and extends the analysis of [[19](https://arxiv.org/html/2512.11765v1#bib.bib19)] in several ways. First, we generalize from n=2n=2 to an arbitrary number nn of traders. We show that the high-frequency limits of discrete-time equilibria with instantaneous costs θ​(Δ​Xt)2\theta(\Delta X\_{t})^{2} recover the continuous-time model of [[3](https://arxiv.org/html/2512.11765v1#bib.bib3)] with the block cost coefficients ϑ0\vartheta\_{0} and ϑT\vartheta\_{T}, which are distinct for n>2n>2. Second, refining the results of [[19](https://arxiv.org/html/2512.11765v1#bib.bib19)], we show not only that the total execution costs converge, but also how the different parts of the continuous-time model emerge in the high-frequency limit: The initial block costs are identified as the limits of the instantaneous costs accrued over an initial interval [0,t0][0,t\_{0}] with arbitrary 0<t0<T0<t\_{0}<T; similarly, the terminal block costs are the limits of the instantaneous costs accrued over an interval [t0,T][t\_{0},T]. Moreover, the “regular” Obizhaeva–Wang impact costs of the continuous-time model are the limits of the Obizhaeva–Wang costs of the discrete-time models. Third, we not only show the qualitative convergence of the equilibria, but also establish the convergence rate 1/N1/N for the trading strategies, where NN is the number of trading periods in [0,T][0,T]. Finally, we show that when the discrete-time models are formulated without instantaneous costs (θ=0\theta=0), the equilibrium strategies oscillate in the high-frequency limit. This yields a one-to-one correspondence between non-existence of the high-frequency limits and non-existence of the continuous-time equilibria without block costs. This correspondence is robust and even extends to fine details: For n>2n>2, [[3](https://arxiv.org/html/2512.11765v1#bib.bib3)] shows that an equilibrium can exist for particular initial inventories of the traders even when only one of the two coefficients ϑ0\vartheta\_{0} and ϑT\vartheta\_{T} has the “correct” value—namely, when initial inventories are symmetric or sum to zero, respectively. We further link this to high-frequency limits of discrete-time models where instantaneous costs are charged only on an initial or terminal portion of the time interval.

Our results complement the analysis of [[3](https://arxiv.org/html/2512.11765v1#bib.bib3)] for vanishing instantaneous costs in continuous time. Taken together, a high-level picture emerges: discretizing time has the same regularizing effect as adding a small instantaneous cost in continuous time, and yields the same limit. This leads us to conjecture a universality phenomenon: a broad class of trading frictions can be introduced to obtain existence of equilibria in trading games with Obizhaeva–Wang price impact, and the small-friction limits of such regularizations all yield the same model, namely Obizhaeva–Wang price impact with additional block costs as specified in [[19](https://arxiv.org/html/2512.11765v1#bib.bib19)] and [[3](https://arxiv.org/html/2512.11765v1#bib.bib3)].

The remainder of this paper is organized as follows. Section [2](https://arxiv.org/html/2512.11765v1#S2 "2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") formulates and solves the discrete-time models, while Section [3](https://arxiv.org/html/2512.11765v1#S3 "3. Continuous-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") recalls the corresponding continuous-time results. Section [4](https://arxiv.org/html/2512.11765v1#S4 "4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") states our main results: the high-frequency limits of the discrete-time equilibrium strategies and costs (Theorems [4.1](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem1 "Theorem 4.1 (Convergence of strategies for 𝜃>0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") and [4.2](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem2 "Theorem 4.2 (Convergence of costs for 𝜃>0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")), as well as the corresponding oscillatory asymptotics for θ=0\theta=0 (Theorems [4.3](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem3 "Theorem 4.3 (Divergence of strategies for 𝜃=0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") and [4.4](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem4 "Theorem 4.4 (Divergence of costs for 𝜃=0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")). Appendix [A](https://arxiv.org/html/2512.11765v1#A1 "Appendix A Closed Form of the Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") provides a closed-form expression for the discrete-time equilibrium strategies that is used in the high-frequency proofs. Appendix [B](https://arxiv.org/html/2512.11765v1#A2 "Appendix B Proofs for Section 2 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") contains the proofs for the discrete-time results in Section [2](https://arxiv.org/html/2512.11765v1#S2 "2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"), while Appendix [C](https://arxiv.org/html/2512.11765v1#A3 "Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") collects the proofs for the main results in Section [4](https://arxiv.org/html/2512.11765v1#S4 "4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"). Finally, Appendix [D](https://arxiv.org/html/2512.11765v1#A4 "Appendix D Time-Varying Instantaneous Costs ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") analyzes the high-frequency asymptotics when instantaneous costs are charged only on an initial or terminal portion of the time interval.

## 2. Discrete-Time Equilibrium

### 2.1. Model Specifications

We consider n≥2n\geq 2 agents trading a single risky asset on the discrete time grid 0=t0<t1<⋯<tN=T0=t\_{0}<t\_{1}<\dots<t\_{N}=T, and a filtered probability space (Ω,ℱ,(ℱt)t≥0,ℙ)(\Omega,\mathscr{F},(\mathscr{F}\_{t})\_{t\geq 0},\mathbb{P}) where ℱ0\mathscr{F}\_{0} is ℙ\mathbb{P}-trivial. The *unaffected* price S0=(St0)t≥0S^{0}=(S^{0}\_{t})\_{t\geq 0} is a square-integrable, right-continuous martingale. The definitions below detail how trading generates transient price impact governed by the exponential *decay kernel* G:ℝ+→ℝ+G\mathrel{\mathop{\ordinarycolon}}\mathbb{R}\_{+}\to\mathbb{R}\_{+},

|  |  |  |
| --- | --- | --- |
|  | G​(t)=e−ρ​t,\displaystyle G(t)=e^{-\rho t}, |  |

where ρ>0\rho>0. (A more general form is G​(t)=λ​e−ρ​tG(t)=\lambda e^{-\rho t}, but we set λ=1\lambda=1 without loss of generality as all other quantities can be rescaled accordingly.)

###### Definition 2.1 (Admissible trading strategy).

Given a grid 𝕋={t0,…,tN}\mathbb{T}=\{t\_{0},\dots,t\_{N}\} and an initial inventory x∈ℝx\in\mathbb{R}, an *admissible trading strategy* is a vector 𝝃=(ξ0,…,ξN)⊤\bm{\xi}=(\xi\_{0},\dots,\xi\_{N})^{\top} of random variables such that

1. (a)

   each ξi\xi\_{i} is ℱti\mathscr{F}\_{t\_{i}}-measurable and bounded;
2. (b)

   x=ξ0+⋯+ξNx=\xi\_{0}+\dots+\xi\_{N} ℙ\mathbb{P}-a.s.

We write 𝒳​(x,𝕋)\mathscr{X}(x,\mathbb{T}) for the set of admissible strategies.

Intuitively, agent ii chooses 𝝃i=(ξi,0,…,ξi,N)⊤∈𝒳​(xi,𝕋)\bm{\xi}\_{i}=(\xi\_{i,0},\dots,\xi\_{i,N})^{\top}\in\mathscr{X}(x\_{i},\mathbb{T}), where xix\_{i} denotes the agent’s initial inventory and ξi,k\xi\_{i,k} is the number of shares traded at time tkt\_{k}, with the sign convention that ξi,k>0\xi\_{i,k}>0 is a sell and ξi,k<0\xi\_{i,k}<0 is a buy. Condition [(b)](https://arxiv.org/html/2512.11765v1#S2.I1.i2 "item (b) ‣ Definition 2.1 (Admissible trading strategy). ‣ 2.1. Model Specifications ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") enforces liquidation by tN=Tt\_{N}=T.
Collecting agents’ strategies in the matrix Ξ=[𝝃1,…,𝝃n]\Xi=[\bm{\xi}\_{1},\dots,\bm{\xi}\_{n}], the (affected) price process is

|  |  |  |
| --- | --- | --- |
|  | StΞ=St0−∑tk<tG​(t−tk)​∑i=1nξi,k.\displaystyle S\_{t}^{\Xi}=S\_{t}^{0}-\sum\_{t\_{k}<t}G(t-t\_{k})\sum\_{i=1}^{n}\xi\_{i,k}. |  |

We fix an *instantaneous cost* parameter θ≥0\theta\geq 0 and define the execution cost of agent ii as follows.

###### Definition 2.2 (Execution cost).

Given a grid 𝕋\mathbb{T} and inventories (x1,…,xn)(x\_{1},\dots,x\_{n}), the execution cost of 𝝃i\bm{\xi}\_{i} given opponents’ strategies 𝝃−i=[𝝃1,…,𝝃i−1,𝝃i+1,…,𝝃n]\bm{\xi}\_{-i}=[\bm{\xi}\_{1},\dots,\bm{\xi}\_{i-1},\bm{\xi}\_{i+1},\dots,\bm{\xi}\_{n}] is

|  |  |  |  |
| --- | --- | --- | --- |
| (2.1) |  | 𝒞𝕋​(𝝃i∣𝝃−i)=xi​S00+∑k=0N(G​(0)2​ξi,k2−StkΞ​ξi,k+G​(0)2​∑j≠iξi,k​ξj,k+θ​ξi,k2).\mathscr{C}\_{\mathbb{T}}(\bm{\xi}\_{i}\mid\bm{\xi}\_{-i})=x\_{i}S^{0}\_{0}+\sum\_{k=0}^{N}\Big(\frac{G(0)}{2}\xi\_{i,k}^{2}-S\_{t\_{k}}^{\Xi}\xi\_{i,k}+\frac{G(0)}{2}\sum\_{j\neq i}\xi\_{i,k}\xi\_{j,k}+\theta\xi\_{i,k}^{2}\Big). |  |

In ([2.1](https://arxiv.org/html/2512.11765v1#S2.E1 "In Definition 2.2 (Execution cost). ‣ 2.1. Model Specifications ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")), the cross-term describes the standard (symmetric) tie-breaking rule that applies when agents place orders at the same instant; see [[20](https://arxiv.org/html/2512.11765v1#bib.bib20), [15](https://arxiv.org/html/2512.11765v1#bib.bib15)]. In addition to the cost of transient impact, each trade incurs quadratic instantaneous (or “temporary impact”) costs θ​ξi,k2\theta\xi\_{i,k}^{2}; see [[10](https://arxiv.org/html/2512.11765v1#bib.bib10)] for a related discussion.

### 2.2. Nash Equilibrium

Fix a grid 𝕋\mathbb{T} and initial inventories (x1,…,xn)(x\_{1},\dots,x\_{n}). Each agent ii is risk-neutral and chooses an admissible strategy to minimize the expected execution cost ([2.1](https://arxiv.org/html/2512.11765v1#S2.E1 "In Definition 2.2 (Execution cost). ‣ 2.1. Model Specifications ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")), where we may assume St0≡0S^{0}\_{t}\equiv 0 without loss of generality.
This leads to the standard notion of Nash equilibrium.

###### Definition 2.3 (Nash equilibrium).

A *Nash equilibrium* is a profile (𝝃1∗,…,𝝃n∗)∈∏i𝒳​(xi,𝕋)(\bm{\xi}^{\*}\_{1},\dots,\bm{\xi}^{\*}\_{n})\in\prod\_{i}\mathscr{X}(x\_{i},\mathbb{T}) such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝒞𝕋​(𝝃i∗∣𝝃−i∗)]=min𝝃∈𝒳​(xi,𝕋)​𝔼​[𝒞𝕋​(𝝃∣𝝃−i∗)],for every ​i=1,…,n.\mathbb{E}[\mathscr{C}\_{\mathbb{T}}(\bm{\xi}^{\*}\_{i}\mid\bm{\xi}^{\*}\_{-i})]=\underset{\bm{\xi}\in\mathscr{X}(x\_{i},\mathbb{T})}{\min}\mathbb{E}[\mathscr{C}\_{\mathbb{T}}(\bm{\xi}\mid\bm{\xi}^{\*}\_{-i})],\qquad\text{for every }i=1,\dots,n. |  |

To state a more explicit expression for the objective functional, let δi​j\delta\_{ij} denote the Kronecker delta and define, for i,j=0,…,Ni,j=0,\dots,N,

|  |  |  |  |
| --- | --- | --- | --- |
| (2.2) |  | Γi​jθ:=G(|ti−tj|)+2θδi​j,Γ~i​j:={0,i<j,12​G​(0),i=j,Γi​j0,i>j.\displaystyle\Gamma\_{ij}^{\theta}\mathrel{\mathop{\ordinarycolon}}=G(|t\_{i}-t\_{j}|)+2\theta\delta\_{ij},\qquad\widetilde{\Gamma}\_{ij}\mathrel{\mathop{\ordinarycolon}}=\begin{cases}0,&i<j,\\ \frac{1}{2}G(0),&i=j,\\ \Gamma\_{ij}^{0},&i>j.\end{cases} |  |

Moreover, we introduce the vectors

|  |  |  |  |
| --- | --- | --- | --- |
| (2.3) |  | 𝒗:=(Γθ+(n−1)​Γ~)−1​𝟏𝟏⊤​(Γθ+(n−1)​Γ~)−1​𝟏,𝒘:=(Γθ−Γ~)−1​𝟏𝟏⊤​(Γθ−Γ~)−1​𝟏.\bm{v}\mathrel{\mathop{\ordinarycolon}}=\frac{(\Gamma^{\theta}+(n-1)\widetilde{\Gamma})^{-1}\bm{1}}{\bm{1}^{\top}(\Gamma^{\theta}+(n-1)\widetilde{\Gamma})^{-1}\bm{1}},\qquad\bm{w}\mathrel{\mathop{\ordinarycolon}}=\frac{(\Gamma^{\theta}-\widetilde{\Gamma})^{-1}\bm{1}}{\bm{1}^{\top}(\Gamma^{\theta}-\widetilde{\Gamma})^{-1}\bm{1}}. |  |

###### Remark 2.4.

We observe that 𝒘\bm{w} does *not depend on nn*, whereas 𝒗\bm{v} depends on nn through Γθ+(n−1)​Γ~\Gamma^{\theta}+(n-1)\widetilde{\Gamma}. An interpretation for 𝒗\bm{v} and 𝒘\bm{w} will be given in Remark [2.8](https://arxiv.org/html/2512.11765v1#S2.Thmtheorem8 "Remark 2.8. ‣ 2.2. Nash Equilibrium ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact").

The next lemma ensures that ([2.3](https://arxiv.org/html/2512.11765v1#S2.E3 "In 2.2. Nash Equilibrium ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) is well-defined. We call a (possibly non-symmetric) square matrix AA *positive* if 𝒙⊤​A​𝒙>0\bm{x}^{\top}A\bm{x}>0 for all nonzero 𝒙\bm{x}. Then, AA is invertible, and A−1A^{-1} is positive as well.

###### Lemma 2.5.

For all θ≥0\theta\geq 0, the matrices Γθ\Gamma^{\theta} and Γθ+(n−1)​Γ~\Gamma^{\theta}+(n-1)\widetilde{\Gamma} and Γθ−Γ~\Gamma^{\theta}-\widetilde{\Gamma} are positive. In particular, the denominators in ([2.3](https://arxiv.org/html/2512.11765v1#S2.E3 "In 2.2. Nash Equilibrium ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) are strictly positive.

The proof is analogous to [[20](https://arxiv.org/html/2512.11765v1#bib.bib20), Lemma 3.2] and omitted. The next result gives an explicit expression for agent ii’s objective functional.

###### Lemma 2.6 (Explicit objective).

For 𝛏i∈𝒳​(xi,𝕋)\bm{\xi}\_{i}\in\mathscr{X}(x\_{i},\mathbb{T}) and competitors’ strategies 𝛏j∈𝒳​(xj,𝕋)\bm{\xi}\_{j}\in\mathscr{X}(x\_{j},\mathbb{T}),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[𝒞𝕋​(𝝃i∣𝝃−i)]\displaystyle\mathbb{E}[\mathscr{C}\_{\mathbb{T}}(\bm{\xi}\_{i}\mid\bm{\xi}\_{-i})] | =𝔼​[12​𝝃i⊤​Γθ​𝝃i+𝝃i⊤​Γ~​(∑j≠i𝝃j)].\displaystyle=\mathbb{E}\Bigl[\frac{1}{2}\bm{\xi}\_{i}^{\top}\Gamma^{\theta}\bm{\xi}\_{i}+\bm{\xi}\_{i}^{\top}\widetilde{\Gamma}\Bigl(\sum\_{j\neq i}\bm{\xi}\_{j}\Bigr)\Bigr]. |  |

The proof follows [[15](https://arxiv.org/html/2512.11765v1#bib.bib15), Lemma 3.1] and is omitted. The final result of this section establishes existence and uniqueness of a Nash equilibrium; it is deterministic and described by 𝒗\bm{v} and 𝒘\bm{w} of ([2.3](https://arxiv.org/html/2512.11765v1#S2.E3 "In 2.2. Nash Equilibrium ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")).

###### Theorem 2.7 (Discrete equilibrium).

For any grid 𝕋\mathbb{T}, θ≥0\theta\geq 0, and initial inventories (x1,…,xn)∈ℝn(x\_{1},\dots,x\_{n})\in\mathbb{R}^{n}, there exists a unique Nash equilibrium
(𝛏1∗,…,𝛏n∗)∈∏i𝒳​(xi,𝕋)(\bm{\xi}^{\*}\_{1},\dots,\bm{\xi}^{\*}\_{n})\in\prod\_{i}\mathscr{X}(x\_{i},\mathbb{T}).
The equilibrium strategies are deterministic and given by

|  |  |  |  |
| --- | --- | --- | --- |
| (2.4) |  | 𝝃i∗=x¯​𝒗+(xi−x¯)​𝒘,wherex¯=1n​∑j=1nxj.\displaystyle\bm{\xi}^{\*}\_{i}=\bar{x}\bm{v}+(x\_{i}-\bar{x})\bm{w},\qquad\text{where}\quad\bar{x}=\frac{1}{n}\sum\_{j=1}^{n}x\_{j}. |  |

(Theorem [A.4](https://arxiv.org/html/2512.11765v1#A1.Thmtheorem4 "Theorem A.4 (Explicit form of 𝝎 and 𝝂). ‣ Appendix A Closed Form of the Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") in Appendix [A](https://arxiv.org/html/2512.11765v1#A1 "Appendix A Closed Form of the Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") provides fully explicit expressions for 𝐯\bm{v} and 𝐰\bm{w}, for equidistant grids 𝕋\mathbb{T}.)

The proof is detailed in Appendix [B](https://arxiv.org/html/2512.11765v1#A2 "Appendix B Proofs for Section 2 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact").

###### Remark 2.8.

We observe the following special cases of Theorem [2.7](https://arxiv.org/html/2512.11765v1#S2.Thmtheorem7 "Theorem 2.7 (Discrete equilibrium). ‣ 2.2. Nash Equilibrium ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"). In the symmetric case x1=⋯=xnx\_{1}=\dots=x\_{n}, we have 𝝃i∗=x1​𝒗\bm{\xi}^{\*}\_{i}=x\_{1}\bm{v} for all ii, whereas in the case x1+⋯+xn=0x\_{1}+\dots+x\_{n}=0 of zero net supply, 𝝃i∗=xi​𝒘\bm{\xi}^{\*}\_{i}=x\_{i}\bm{w} for all ii. Thus, 𝒗\bm{v} and 𝒘\bm{w} can be interpreted as the strategies for an agent with unit initial inventory in each of those cases.

## 3. Continuous-Time Equilibrium

This section recalls the continuous-time setting with *boundary block costs*. We refer to [[3](https://arxiv.org/html/2512.11765v1#bib.bib3), Section 2] for further details and proofs.

### 3.1. Model Specifications

There are nn traders with inventory processes Xi=(Xti)t∈[0,T]X^{i}=(X^{i}\_{t})\_{t\in[0,T]}. An *admissible inventory* XiX^{i} is càdlàg, predictable, has (essentially) bounded total variation, and satisfies X0−i=xi∈ℝX^{i}\_{0-}=x\_{i}\in\mathbb{R} and XTi=0X^{i}\_{T}=0.
The *unaffected price* S=(St)t≥0S=(S\_{t})\_{t\geq 0} is a càdlàg local martingale with 𝔼​[[S,S]T]<∞\mathbb{E}[[S,S]\_{T}]<\infty. By risk-neutrality (see [[3](https://arxiv.org/html/2512.11765v1#bib.bib3), Proposition 2.2] for a detailed proof), we may assume S≡0S\equiv 0. As in the discrete-time model, trading generates transient impact I=(It)t≥0I=(I\_{t})\_{t\geq 0} with the Obizhaeva–Wang dynamics

|  |  |  |
| --- | --- | --- |
|  | d​It=−ρ​It​d​t+λ​∑i=1nd​Xti,I0−=0.\displaystyle dI\_{t}=-\rho I\_{t}\,dt+\lambda\sum\_{i=1}^{n}dX^{i}\_{t},\qquad I\_{0-}=0. |  |

Collecting agents’ inventories in the vector 𝑿=(X1,…,Xn)\bm{X}=(X^{1},\dots,X^{n}) and setting λ=1\lambda=1 without loss of generality, the (affected) price process is

|  |  |  |
| --- | --- | --- |
|  | St𝑿=∫0te−ρ​(t−s)​∑i=1nd​Xsi.\displaystyle S\_{t}^{\bm{X}}=\int\_{0}^{t}e^{-\rho(t-s)}\sum\_{i=1}^{n}dX^{i}\_{s}. |  |

In addition to the cost of transient impact, we charge quadratic *boundary block costs* at t=0t=0 and t=Tt=T with coefficients ϑ0,ϑT≥0\vartheta\_{0},\vartheta\_{T}\geq 0. Given opponents’ strategies 𝑿−i\bm{X}^{-i}, the execution cost of XiX^{i} is then defined as

|  |  |  |  |
| --- | --- | --- | --- |
| (3.1) |  | 𝒞​(Xi∣𝑿−i)=𝔼​[∫0TSt−𝑿​𝑑Xti+12​∑t∈[0,T]Δ​St​Δ​Xti+12​(ϑ0​(Δ​X0i)2+ϑT​(Δ​XTi)2)].\mathscr{C}(X^{i}\mid\bm{X}^{-i})=\mathbb{E}\left[\int\_{0}^{T}S^{\bm{X}}\_{t-}\,dX^{i}\_{t}+\frac{1}{2}\sum\_{t\in[0,T]}\Delta S\_{t}\,\Delta X^{i}\_{t}+\frac{1}{2}\big(\vartheta\_{0}(\Delta X^{i}\_{0})^{2}+\vartheta\_{T}(\Delta X^{i}\_{T})^{2}\big)\right]. |  |

Thus, block trades at the initial and terminal times incur an additional quadratic cost governed by ϑ0\vartheta\_{0} and ϑT\vartheta\_{T}, respectively. The cross-term has the same interpretation as the discrete-time model.

### 3.2. Nash Equilibrium

A profile 𝑿∗=(X∗,1,…,X∗,n)\bm{X}^{\*}=(X^{\*,1},\dots,X^{\*,n}) is a Nash equilibrium if each X∗,iX^{\*,i} is admissible and

|  |  |  |
| --- | --- | --- |
|  | 𝒞​(Z∣𝑿∗,−i)≥𝒞​(X∗,i∣𝑿∗,−i)for all admissible ​Z.\displaystyle\mathscr{C}(Z\mid\bm{X}^{\*,-i})\geq\mathscr{C}(X^{\*,i}\mid\bm{X}^{\*,-i})\qquad\text{for all admissible }Z. |  |

Existence of an equilibrium depends crucially on the initial and terminal block cost coefficients ϑ0\vartheta\_{0} and ϑT\vartheta\_{T}—there is a single choice yielding existence for general initial inventories.

###### Theorem 3.1 (Continuous equilibrium, [[3](https://arxiv.org/html/2512.11765v1#bib.bib3), Theorem 4.4, Corollary 4.6]).

Let ϑ0=(n−1)/2\vartheta\_{0}=({n-1})/{2} and ϑT=1/2\vartheta\_{T}={1}/{2}. Then the unique Nash equilibrium is given by

|  |  |  |  |
| --- | --- | --- | --- |
| (3.2) |  | Xt∗,i=𝕗​(t)​(xi−x¯)+𝕘​(t)​x¯,t∈[0,T],i=1,…,n,where ​x¯=1n​∑j=1nxj\displaystyle X^{\*,i}\_{t}=\mathbbm{f}(t)(x\_{i}-\bar{x})+\mathbbm{g}(t)\bar{x},\qquad t\in[0,T],\ i=1,\dots,n,\qquad\text{where }\bar{x}=\frac{1}{n}\sum\_{j=1}^{n}x\_{j} |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
| (3.3) |  | 𝕗(t):=ρ​(T−t)+1ρ​T+1,t∈[0,T),𝕗0−=1,𝕗T=0,\displaystyle\mathbbm{f}(t)\mathrel{\mathop{\ordinarycolon}}=\frac{\rho(T-t)+1}{\rho T+1},\quad t\in[0,T),\qquad\mathbbm{f}\_{0-}=1,\qquad\mathbbm{f}\_{T}=0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
| (3.4) |  | 𝕘(t):=1−n​(ρ​t+1)​(n+1)​eρ​n+1n−1​T+2​n​eρ​n+1n−1​t−(n−1)n​((ρ​T+1)​(n+1)+2)​eρ​n+1n−1​T−(n−1),t∈[0,T],𝕘0−=1.\displaystyle\mathbbm{g}(t)\mathrel{\mathop{\ordinarycolon}}=1-\frac{n(\rho t+1)(n+1)e^{\rho\frac{n+1}{n-1}T}+2ne^{\rho\frac{n+1}{n-1}t}-(n-1)}{n((\rho T+1)(n+1)+2)e^{\rho\frac{n+1}{n-1}T}-(n-1)},\quad t\in[0,T],\qquad\mathbbm{g}\_{0-}=1. |  |

Moreover, the equilibrium execution cost is given by

|  |  |  |  |
| --- | --- | --- | --- |
| (3.5) |  | 𝒞​(X∗,i∣𝑿∗,−i)=ℐ+ℬ0+ℬT,\displaystyle\mathscr{C}(X^{\*,i}\mid\bm{X}^{\*,-i})=\mathscr{I}+\mathscr{B}\_{0}+\mathscr{B}\_{T}, |  |

where ℐ\mathscr{I} is *impact cost*

|  |  |  |  |
| --- | --- | --- | --- |
| (3.6) |  | ℐ:=nρ​T+1x¯(xi−x¯)+x¯2​n3​(n+1)​(((ρ​T+12)​(n+1)+3)​e2​(n+1)​ρ​Tn−1−2​(n−1)n2​(n​e(n+1)​ρ​Tn−1+14))[n​((ρ​T+1)​(n+1)+2)​e(n+1)​ρ​Tn−1−(n−1)]2\displaystyle\mathscr{I}\mathrel{\mathop{\ordinarycolon}}=\frac{n}{\rho T+1}\bar{x}(x\_{i}-\bar{x})+\frac{\bar{x}^{2}n^{3}(n+1)\left(\left((\rho T+\frac{1}{2})(n+1)+3\right)e^{\frac{2(n+1)\rho T}{n-1}}-\frac{2(n-1)}{n^{2}}\left(ne^{\frac{(n+1)\rho T}{n-1}}+\frac{1}{4}\right)\right)}{[n((\rho T+1)(n+1)+2)e^{\frac{(n+1)\rho T}{n-1}}-(n-1)]^{2}} |  |

and ℬ0,ℬT\mathscr{B}\_{0},\mathscr{B}\_{T} are the *initial and terminal block costs*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (3.7) |  | ℬ0\displaystyle\mathscr{B}\_{0} | :=(n−1)​(n+1)2​(1+n​eρ​n+1n−1​T)2​x¯24​[n​((ρ​T+1)​(n+1)+2)​eρ​n+1n−1​T−(n−1)]2,\displaystyle\mathrel{\mathop{\ordinarycolon}}=\frac{(n-1)(n+1)^{2}(1+ne^{\rho\frac{n+1}{n-1}T})^{2}\bar{x}^{2}}{4[n((\rho T+1)(n+1)+2)e^{\rho\frac{n+1}{n-1}T}-(n-1)]^{2}}, |  |
|  | ℬT\displaystyle\mathscr{B}\_{T} | :=(xi−x¯)24​(ρ​T+1)2.\displaystyle\mathrel{\mathop{\ordinarycolon}}=\frac{(x\_{i}-\bar{x})^{2}}{4(\rho T+1)^{2}}. |  |

###### Remark 3.2.

The stated values for the block cost coefficients ϑ0,ϑT\vartheta\_{0},\vartheta\_{T} are the unique “correct” choice for this model. Indeed, for different values of ϑ0,ϑT\vartheta\_{0},\vartheta\_{T}, equilibrium does not exist, except for particular initial inventories. Specifically, [[3](https://arxiv.org/html/2512.11765v1#bib.bib3), Theorem 4.4] shows that if ϑT=1/2\vartheta\_{T}={1}/{2} but ϑ0≠(n−1)/2\vartheta\_{0}\neq({n-1})/{2}, an equilibrium exists if and only if x¯=0\bar{x}=0, and if ϑ0=(n−1)/2\vartheta\_{0}=({n-1})/{2} but ϑT≠1/2\vartheta\_{T}\neq{1}/{2}, an equilibrium exists if and only if x1=⋯=xnx\_{1}=\cdots=x\_{n}. Thus, if both ϑ0≠(n−1)/2\vartheta\_{0}\neq({n-1})/{2} and ϑT≠1/2\vartheta\_{T}\neq{1}/{2}, then the only case with equilibrium is xi≡0x\_{i}\equiv 0, which yields the trivial no-trade solution X∗,i≡0X^{\*,i}\equiv 0. In the cases with existence, the equilibrium is given by ([3.2](https://arxiv.org/html/2512.11765v1#S3.E2 "In Theorem 3.1 (Continuous equilibrium, [3, Theorem 4.4, Corollary 4.6]). ‣ 3.2. Nash Equilibrium ‣ 3. Continuous-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")).

## 4. High-Frequency Limits

We can now present our main results on the high-frequency limits of the discrete equilibrium strategies and costs. In the case θ>0\theta>0 of non-zero instantaneous costs, we show that the discrete equilibria converge to the continuous-time equilibrium of Theorem [3.1](https://arxiv.org/html/2512.11765v1#S3.Thmtheorem1 "Theorem 3.1 (Continuous equilibrium, [3, Theorem 4.4, Corollary 4.6]). ‣ 3.2. Nash Equilibrium ‣ 3. Continuous-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") including the particular boundary block costs. Whereas for θ=0\theta=0, the limit does not exist, and this will be linked to the non-existence of a continuous-time equilibrium when there are no boundary block costs (Remark [3.2](https://arxiv.org/html/2512.11765v1#S3.Thmtheorem2 "Remark 3.2. ‣ 3.2. Nash Equilibrium ‣ 3. Continuous-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")).
We fix initial inventories (x1,…,xn)∈ℝn({x\_{1},\dots,x\_{n}})\in\mathbb{R}^{n} and consider equidistant grids

|  |  |  |  |
| --- | --- | --- | --- |
| (4.1) |  | 𝕋N:={kT/N∣k=0,1,…,N},N=2,3,…\displaystyle\mathbb{T}\_{N}\mathrel{\mathop{\ordinarycolon}}=\{kT/N\mid k=0,1,\dots,N\},\quad N=2,3,\dots |  |

For t∈[0,T]t\in[0,T], define

|  |  |  |  |
| --- | --- | --- | --- |
| (4.2) |  | nt=⌈N​t/T⌉,Vt(N)=1−∑k=1ntvk,Wt(N)=1−∑k=1ntwk,Xt(N),i=x¯​Vt(N)+(xi−x¯)​Wt(N),n\_{t}=\lceil Nt/T\rceil,\qquad V\_{t}^{(N)}=1-\sum\_{k=1}^{n\_{t}}v\_{k},\qquad W\_{t}^{(N)}=1-\sum\_{k=1}^{n\_{t}}w\_{k},\qquad X^{(N),i}\_{t}=\bar{x}V^{(N)}\_{t}+(x\_{i}-\bar{x})W^{(N)}\_{t}, |  |

where 𝒗\bm{v} and 𝒘\bm{w} are the vectors from ([2.3](https://arxiv.org/html/2512.11765v1#S2.E3 "In 2.2. Nash Equilibrium ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")).
Note that time tt corresponds to the ntn\_{t}-th trading date in 𝕋N\mathbb{T}\_{N}. In view of Remark [2.8](https://arxiv.org/html/2512.11765v1#S2.Thmtheorem8 "Remark 2.8. ‣ 2.2. Nash Equilibrium ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"), Vt(N)V\_{t}^{(N)} is the time-tt inventory of an agent with unit initial inventory in the symmetric case x1=⋯=xnx\_{1}=\dots=x\_{n}. Similarly, Wt(N)W\_{t}^{(N)} is the time-tt inventory of an agent with unit initial inventory in the case of zero net supply. Finally, Xt(N),iX^{(N),i}\_{t} is the time-tt inventory of agent ii with initial inventory xix\_{i}.

We first focus on the case θ>0\theta>0. The first result states the convergence of the strategies. More precisely, the time-tt inventory Xt(N),iX^{(N),i}\_{t} converges pointwise to the continuous-time inventory Xt∗,iX^{\*,i}\_{t} of Theorem [3.1](https://arxiv.org/html/2512.11765v1#S3.Thmtheorem1 "Theorem 3.1 (Continuous equilibrium, [3, Theorem 4.4, Corollary 4.6]). ‣ 3.2. Nash Equilibrium ‣ 3. Continuous-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") for t∈(0,T)t\in(0,T), and we establish the rate 1/N1/N. Given the form of the strategies, convergence boils down to Vt(N)→𝕘​(t)V^{(N)}\_{t}\to\mathbbm{g}(t) and Wt(N)→𝕗​(t)W^{(N)}\_{t}\to\mathbbm{f}(t), where 𝕗\mathbbm{f} and 𝕘\mathbbm{g} are defined in ([3.3](https://arxiv.org/html/2512.11765v1#S3.E3 "In Theorem 3.1 (Continuous equilibrium, [3, Theorem 4.4, Corollary 4.6]). ‣ 3.2. Nash Equilibrium ‣ 3. Continuous-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) and ([3.4](https://arxiv.org/html/2512.11765v1#S3.E4 "In Theorem 3.1 (Continuous equilibrium, [3, Theorem 4.4, Corollary 4.6]). ‣ 3.2. Nash Equilibrium ‣ 3. Continuous-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")). At each of the boundaries (t=0t=0 and t=Tt=T), one of these limits fails, whence the convergence of the strategies only on the open interval (0,T)(0,T).

###### Theorem 4.1 (Convergence of strategies for θ>0\theta>0).

If θ>0\theta>0, we have

|  |  |  |
| --- | --- | --- |
|  | Xt(N),i⟶Xt∗,i,for any ​t∈(0,T).\displaystyle X^{(N),i}\_{t}\longrightarrow X^{\*,i}\_{t},\qquad\text{for any }t\in(0,T). |  |

More precisely:

1. (a)

   For any t∈(0,T]t\in(0,T], the sequence N​|Vt(N)−𝕘​(t)|N|V^{(N)}\_{t}-\mathbbm{g}(t)| is bounded, and V0(N)=1V\_{0}^{(N)}=1 for all NN.
2. (b)

   For any t∈[0,T)t\in[0,T), the sequence N​|Wt(N)−𝕗​(t)|N|W^{(N)}\_{t}-\mathbbm{f}(t)| is bounded, and N​|WT(N)−1(2​θ+12)​(ρ​T+1)|=𝒪​(1)N|W\_{T}^{(N)}-\frac{1}{(2\theta+\frac{1}{2})(\rho T+1)}|=\mathcal{O}(1).

We emphasize that the limits are *independent* of the specific value of θ>0\theta>0.

![Refer to caption](x1.png)


Figure 1. Convergence of Vt(N)V^{(N)}\_{t} for θ=0.1\theta=0.1, n=10n=10, and ρ=1\rho=1.

![Refer to caption](x2.png)


Figure 2. Convergence of Wt(N)W^{(N)}\_{t} for θ=0.1\theta=0.1, n=10n=10, and ρ=1\rho=1.

A similar conclusion holds for the costs. We show not only the convergence of the total cost, but also that the specific boundary block costs ℬ0\mathscr{B}\_{0} and ℬT\mathscr{B}\_{T} arise as the limits of the instantaneous costs incurred near the boundaries t=0t=0 and t=Tt=T, respectively. Hence, the coefficients ϑ0\vartheta\_{0} and ϑT\vartheta\_{T} in Theorem [3.1](https://arxiv.org/html/2512.11765v1#S3.Thmtheorem1 "Theorem 3.1 (Continuous equilibrium, [3, Theorem 4.4, Corollary 4.6]). ‣ 3.2. Nash Equilibrium ‣ 3. Continuous-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") arise naturally from the high-frequency limit, and they are canonical in that the limit does not depend on the value of θ\theta as long as θ>0\theta>0.

###### Theorem 4.2 (Convergence of costs for θ>0\theta>0).

Let θ>0\theta>0 and let (𝛏∗1(N),…,𝛏∗n(N))∈∏i=1n𝒳​(xi,𝕋N)({{\bm{\xi}}^{\*}}^{({N})}\_{1},\dots,{\bm{\xi}^{\*}}^{(N)}\_{n})\in\prod\_{i=1}^{n}\mathscr{X}(x\_{i},\mathbb{T}\_{N}) be the equilibrium strategies.
The discrete execution cost converges to its continuous counterpart,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (4.3) |  | limN↑∞𝔼​[𝒞𝕋N​(𝝃∗i(N)∣𝝃∗−i(N))]\displaystyle\lim\_{N\uparrow\infty}\mathbb{E}\bigl[\mathscr{C}\_{\mathbb{T}\_{N}}({\bm{\xi}^{\*}}^{(N)}\_{i}\mid{\bm{\xi}^{\*}}^{(N)}\_{-i})\bigr] | =𝒞​(X∗,i∣𝑿∗,−i)=ℐ+ℬ0+ℬT.\displaystyle=\mathscr{C}(X^{\*,i}\mid\bm{X}^{\*,-i})=\mathscr{I}+\mathscr{B}\_{0}+\mathscr{B}\_{T}. |  |

More precisely, for any split mN:=⌈cN⌉m\_{N}\mathrel{\mathop{\ordinarycolon}}=\lceil cN\rceil with c∈(0,1)c\in({0,1}), the cumulative initial/terminal instantaneous costs converge to the initial/terminal block costs of the continuous equilibrium,

|  |  |  |  |
| --- | --- | --- | --- |
| (4.4) |  | θ​∑k=0mN−1(ξi,k∗(N))2⟶ℬ0,θ​∑k=mNN(ξi,k∗(N))2⟶ℬT,\displaystyle\theta\sum\_{k=0}^{m\_{N}-1}\bigl({\xi^{\*\,(N)}\_{i,k}}\bigr)^{2}\longrightarrow\mathscr{B}\_{0},\qquad\theta\sum\_{k=m\_{N}}^{N}\bigl({\xi^{\*\,(N)}\_{i,k}}\bigr)^{2}\longrightarrow\mathscr{B}\_{T}, |  |

and the discrete impact cost

|  |  |  |
| --- | --- | --- |
|  | ℐN(𝝃∗i(N)∣𝝃∗−i(N)):=𝔼[𝒞𝕋N(𝝃∗i(N)∣𝝃∗−i(N))−θ∑k=0N(ξi,k∗(N))2]\displaystyle\mathscr{I}\_{N}({\bm{\xi}^{\*}}\_{i}^{(N)}\mid{\bm{\xi}^{\*}}\_{-i}^{(N)})\mathrel{\mathop{\ordinarycolon}}=\mathbb{E}\bigl[\mathscr{C}\_{\mathbb{T}\_{N}}({\bm{\xi}^{\*}}\_{i}^{(N)}\mid{\bm{\xi}^{\*}}\_{-i}^{(N)})-\theta\sum\_{k=0}^{N}\bigl(\xi^{\*\,(N)}\_{i,k}\bigr)^{2}\bigr] |  |

converges to its continuous counterpart,

|  |  |  |  |
| --- | --- | --- | --- |
| (4.5) |  | ℐN​(𝝃∗i(N)∣𝝃∗−i(N))→ℐ.\displaystyle\mathscr{I}\_{N}({\bm{\xi}^{\*}}^{(N)}\_{i}\mid{\bm{\xi}^{\*}}^{(N)}\_{-i})\to\mathscr{I}. |  |

Figures [1](https://arxiv.org/html/2512.11765v1#S4.F1 "Figure 1 ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") and [2](https://arxiv.org/html/2512.11765v1#S4.F2 "Figure 2 ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") illustrate the persistent oscillations of the inventories V(N)V^{(N)} and W(N)W^{(N)} near the boundaries t=0t=0 and t=Tt=T, whereas in the interior (0,T)({0,T}) the jumps of the inventories are 𝒪​(1/N)\mathcal{O}({1/N}); see Theorem [4.1](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem1 "Theorem 4.1 (Convergence of strategies for 𝜃>0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"). The cumulative instantaneous costs of the oscillations near the boundaries tend to ℬ0\mathscr{B}\_{0} and ℬT\mathscr{B}\_{T}; see ([4.4](https://arxiv.org/html/2512.11765v1#S4.E4 "In Theorem 4.2 (Convergence of costs for 𝜃>0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")).

Theorems [4.1](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem1 "Theorem 4.1 (Convergence of strategies for 𝜃>0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") and [4.2](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem2 "Theorem 4.2 (Convergence of costs for 𝜃>0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") show convergence to a limit (independent of θ\theta) whenever θ>0\theta>0. By contrast, without instantaneous costs (θ=0\theta=0), the optimal strategies and the costs both oscillate and do not converge. The following theorems make this precise; for brevity, we use the constants 𝔡1,𝔡2,𝔞±​(t),𝔟​(t),𝔠​(t)\mathfrak{d}\_{1},\mathfrak{d}\_{2},\mathfrak{a}\_{\pm}(t),\mathfrak{b}(t),\mathfrak{c}(t) detailed in
Table [1](https://arxiv.org/html/2512.11765v1#S4.T1 "Table 1 ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact").

| Constant | Definition |
| --- | --- |
| 𝔡1\mathfrak{d}\_{1} | n​e2​n+1n−1​ρ​T​((n+1)​ρ​T+n+3)+(n−1)2​en+1n−1​ρ​T+(n+1)​ρ​T+3​n+1\displaystyle ne^{2\frac{n+1}{n-1}\rho T}((n+1)\rho T+n+3)+(n-1)^{2}e^{\frac{n+1}{n-1}\rho T}+(n+1)\rho T+3n+1 |
| 𝔡2\mathfrak{d}\_{2} | n​e2​n+1n−1​ρ​T​((n+1)​ρ​T+n+3)+(1−n2)​en+1n−1​ρ​T−(n+1)​ρ​T−3​n−1\displaystyle ne^{2\frac{n+1}{n-1}\rho T}((n+1)\rho T+n+3)+(1-n^{2})e^{\frac{n+1}{n-1}\rho T}-(n+1)\rho T-3n-1 |
| 𝔞±​(t)\mathfrak{a}\_{\pm}(t) | ±(n+1)​en+1n−1​ρ​(T−t)±n​(n+1)​en+1n−1​ρ​(2​T−t)\displaystyle\pm(n+1)e^{\frac{n+1}{n-1}\rho(T-t)}\pm n(n+1)e^{\frac{n+1}{n-1}\rho(2T-t)} |
| 𝔟​(t)\mathfrak{b}(t) | e2​n+1n−1​ρ​T​(n​(n+1)​ρ​(T−t)+2​n)−2​n​en+1n−1​ρ​(T+t)\displaystyle e^{2\frac{n+1}{n-1}\rho T}(n(n+1)\rho(T-t)+2n)-2ne^{\frac{n+1}{n-1}\rho(T+t)} |
| 𝔠​(t)\mathfrak{c}(t) | (n+1)​ρ​(T−t)+n​(n−1)​en+1n−1​ρ​T+2​n​eρ​n+1n−1​t+n+1\displaystyle(n+1)\rho(T-t)+n(n-1)e^{\frac{n+1}{n-1}\rho T}+2ne^{\rho\frac{n+1}{n-1}t}+n+1 |

Table 1. Constants for oscillatory limits.

###### Theorem 4.3 (Divergence of strategies for θ=0\theta=0).

Assume θ=0\theta=0.

1. (a)

   Define the functions β±,γ±:[0,T]→ℝ\beta\_{\pm},\gamma\_{\pm}\mathrel{\mathop{\ordinarycolon}}[0,T]\to\mathbb{R} by

   |  |  |  |
   | --- | --- | --- |
   |  | β±(t):=𝔞±​(t)+𝔟​(t)+𝔠​(t)𝔡1,γ±(t):=𝔞±​(t)+𝔟​(t)−𝔠​(t)𝔡2.\beta\_{\pm}(t)\mathrel{\mathop{\ordinarycolon}}=\frac{\mathfrak{a}\_{\pm}(t)+\mathfrak{b}(t)+\mathfrak{c}(t)}{\mathfrak{d}\_{1}},\qquad\gamma\_{\pm}(t)\mathrel{\mathop{\ordinarycolon}}=\frac{\mathfrak{a}\_{\pm}(t)+\mathfrak{b}(t)-\mathfrak{c}(t)}{\mathfrak{d}\_{2}}. |  |

   Then V0(N)=1V\_{0}^{(N)}=1, and for 0<t≤T0<t\leq T the subsequence (Vt(2​N))N∈ℕ(V\_{t}^{(2N)})\_{N\in\mathbb{N}} has exactly the two cluster points β+​(t)\beta\_{+}(t) and β−​(t)\beta\_{-}(t), while (Vt(2​N+1))N∈ℕ(V\_{t}^{(2N+1)})\_{N\in\mathbb{N}} has exactly the two cluster points γ+​(t)\gamma\_{+}(t) and γ−​(t)\gamma\_{-}(t).
2. (b)

   Define the functions φ±,ψ±:[0,T]→ℝ\varphi\_{\pm},\psi\_{\pm}\mathrel{\mathop{\ordinarycolon}}[0,T]\to\mathbb{R} by

   |  |  |  |
   | --- | --- | --- |
   |  | φ±(t):=1+ρ​(T−t)±e−ρ​(T−t)1+ρ​T+e−ρ​T,ψ±(t):=1+ρ​(T−t)±e−ρ​(T−t)1+ρ​T−e−ρ​T.\varphi\_{\pm}(t)\mathrel{\mathop{\ordinarycolon}}=\frac{1+\rho(T-t)\pm e^{-\rho(T-t)}}{1+\rho T+e^{-\rho T}},\qquad\psi\_{\pm}(t)\mathrel{\mathop{\ordinarycolon}}=\frac{1+\rho(T-t)\pm e^{-\rho(T-t)}}{1+\rho T-e^{-\rho T}}. |  |

   Then W0(N)=1W\_{0}^{(N)}=1, and for 0<t<T0<t<T the sequence (Wt(2​N))N∈ℕ(W\_{t}^{(2N)})\_{N\in\mathbb{N}} has exactly the two cluster points φ+​(t)\varphi\_{+}(t) and φ−​(t)\varphi\_{-}(t), while (Wt(2​N+1))N∈ℕ(W\_{t}^{(2N+1)})\_{N\in\mathbb{N}} has exactly the two cluster points ψ+​(t)\psi\_{+}(t) and ψ−​(t)\psi\_{-}(t). For t=Tt=T we have WT(2​N)→φ+​(T)W\_{T}^{(2N)}\to\varphi\_{+}(T) and WT(2​N+1)→ψ+​(T)W\_{T}^{(2N+1)}\to\psi\_{+}(T).

\begin{overpic}[width=216.81pt]{plots/convergence\_V\_zero\_theta\_N\_100\_n\_10.pdf}
\end{overpic}\begin{overpic}[width=216.81pt]{plots/convergence\_V\_zero\_theta\_N\_101\_n\_10.pdf}
\end{overpic}

Figure 3. Vt(100)V\_{t}^{(100)} (left) and Vt(101)V\_{t}^{(101)} (right) for n=10n=10, θ=0\theta=0, and ρ=1\rho=1, together with the corresponding cluster points from Theorem [4.3](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem3 "Theorem 4.3 (Divergence of strategies for 𝜃=0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") [(a)](https://arxiv.org/html/2512.11765v1#S4.I2.i1 "item (a) ‣ Theorem 4.3 (Divergence of strategies for 𝜃=0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact").

Likewise, the equilibrium costs oscillate when θ=0\theta=0, approaching different limits along subsequences of time grids with an even or odd number of steps.

###### Theorem 4.4 (Divergence of costs for θ=0\theta=0).

Using the same notation as in Theorem [4.2](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem2 "Theorem 4.2 (Convergence of costs for 𝜃>0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"), the equilibrium costs satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | limN↑∞𝔼​[𝒞𝕋2​N​(𝝃∗i(2​N)∣𝝃∗−i(2​N))]\displaystyle\lim\_{N\uparrow\infty}\mathbb{E}[\mathscr{C}\_{\mathbb{T}\_{2N}}({\bm{\xi}^{\*}}\_{i}^{(2N)}\mid{\bm{\xi}^{\*}}\_{-i}^{(2N)})] | =n​x¯2​((n+1)​n​e2​ρ​n+1n−1​T+n+1)𝔡1+n​x¯​(xi−x¯)e−ρ​T+ρ​T+1\displaystyle=\frac{n\bar{x}^{2}((n+1)ne^{2\rho\frac{n+1}{n-1}T}+n+1)}{\mathfrak{d}\_{1}}+\frac{n\bar{x}(x\_{i}-\bar{x})}{e^{-\rho T}+\rho T+1} |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | limN↑∞𝔼​[𝒞𝕋2​N+1​(𝝃∗i(2​N+1)∣𝝃∗−i(2​N+1))]\displaystyle\lim\_{N\uparrow\infty}\mathbb{E}[\mathscr{C}\_{\mathbb{T}\_{2N+1}}({\bm{\xi}^{\*}}\_{i}^{(2N+1)}\mid{\bm{\xi}^{\*}}\_{-i}^{(2N+1)})] | =n​x¯2​((n+1)​n​e2​ρ​n+1n−1​T−n−1)𝔡2+n​x¯​(xi−x¯)ρ​T+1−e−ρ​T.\displaystyle=\frac{n\bar{x}^{2}((n+1)ne^{2\rho\frac{n+1}{n-1}T}-n-1)}{\mathfrak{d}\_{2}}+\frac{n\bar{x}(x\_{i}-\bar{x})}{\rho T+1-e^{-\rho T}}. |  |

Recall that Remark [3.2](https://arxiv.org/html/2512.11765v1#S3.Thmtheorem2 "Remark 3.2. ‣ 3.2. Nash Equilibrium ‣ 3. Continuous-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") identified two special configurations of the initial inventories where continuous-time equilibrium exists even though one of the two boundary block costs ϑ0,ϑT\vartheta\_{0},\vartheta\_{T} does not have the “correct” value. That phenomenon has no analogue in Theorems [4.3](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem3 "Theorem 4.3 (Divergence of strategies for 𝜃=0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") and [4.4](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem4 "Theorem 4.4 (Divergence of costs for 𝜃=0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"), which feature a single parameter θ\theta for the entire time interval. Appendix [D](https://arxiv.org/html/2512.11765v1#A4 "Appendix D Time-Varying Instantaneous Costs ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") analyzes the behavior of the equilibrium inventories in a richer discrete-time model where the cost functional is modified by charging instantaneous costs only on either the first or the second half of the time interval; this amounts to a time-dependent θ\theta. When the cost is charged only on the second half (and there is no cost on the first half), the discrete-time inventories converge to the continuous-time equilibrium in the zero-net-supply case, whereas when the cost is charged only on the first half, convergence holds in the symmetric case. Thus, for those special configurations of the initial inventories, convergence of the discrete-time models with costs on the first/second half is in one-to-one correspondence with the existence of a continuous-time equilibrium when the initial/terminal block cost is specified correctly.

This completes the overall picture that emerges from the preceding theorems: any positive instantaneous costs give rise to the “correct” boundary block costs in the limit, whereas absence of instantaneous costs leads to failure of convergence, corresponding to non-existence of equilibrium in the continuous-time setting.

## Appendix A Closed Form of the Discrete-Time Equilibrium

The goal of this section is to obtain an explicit formula for the discrete-time equilibrium of Theorem [2.7](https://arxiv.org/html/2512.11765v1#S2.Thmtheorem7 "Theorem 2.7 (Discrete equilibrium). ‣ 2.2. Nash Equilibrium ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"). For that, we only need to derive a formula for 𝒗\bm{v}. The formula for 𝒘\bm{w} is the same as in [[19](https://arxiv.org/html/2512.11765v1#bib.bib19)] which treats the case of n=2n=2 traders; indeed, by Remark [2.4](https://arxiv.org/html/2512.11765v1#S2.Thmtheorem4 "Remark 2.4. ‣ 2.2. Nash Equilibrium ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"), 𝒘\bm{w} does not depend on nn. Recall the time grid 𝕋N\mathbb{T}\_{N} in ([4.1](https://arxiv.org/html/2512.11765v1#S4.E1 "In 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) and the matrices Γθ\Gamma^{\theta}, Γ~\widetilde{\Gamma} in ([2.2](https://arxiv.org/html/2512.11765v1#S2.E2 "In 2.2. Nash Equilibrium ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")).
Define the following column vectors of length N+1N+1,

|  |  |  |  |
| --- | --- | --- | --- |
| (A.1) |  | 𝝂:=(Γθ+(n−1)Γ~)−1𝟏,𝝎:=(Γθ−Γ~)−1𝟏.\displaystyle\bm{\nu}\mathrel{\mathop{\ordinarycolon}}=(\Gamma^{\theta}+(n-1)\widetilde{\Gamma})^{-1}\bm{1},\qquad\bm{\omega}\mathrel{\mathop{\ordinarycolon}}=(\Gamma^{\theta}-\widetilde{\Gamma})^{-1}\bm{1}. |  |

Then, by ([2.3](https://arxiv.org/html/2512.11765v1#S2.E3 "In 2.2. Nash Equilibrium ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")),

|  |  |  |  |
| --- | --- | --- | --- |
| (A.2) |  | 𝒗=1𝟏⊤​𝝂​𝝂,𝒘=1𝟏⊤​𝝎​𝝎.\displaystyle\bm{v}=\frac{1}{\bm{1}^{\top}\bm{\nu}}\bm{\nu},\qquad\bm{w}=\frac{1}{\bm{1}^{\top}\bm{\omega}}\bm{\omega}. |  |

Generalizing [[19](https://arxiv.org/html/2512.11765v1#bib.bib19)], we set

|  |  |  |
| --- | --- | --- |
|  | α:=e−ρ​T/N,κ:=2θ+(n−1)/2,Γ:=Γ0,\alpha\mathrel{\mathop{\ordinarycolon}}=e^{-\rho T/N},\qquad\kappa\mathrel{\mathop{\ordinarycolon}}=2\theta+({n-1})/{2},\qquad\Gamma\mathrel{\mathop{\ordinarycolon}}=\Gamma^{0}, |  |

and introduce the matrix

|  |  |  |
| --- | --- | --- |
|  | B:=(1−α2)(Id+Γ−1((n−1)Γ~+2θId)).B\mathrel{\mathop{\ordinarycolon}}=(1-\alpha^{2})(\operatorname{Id}+\Gamma^{-1}((n-1)\widetilde{\Gamma}+2\theta\operatorname{Id})). |  |

From ([A.1](https://arxiv.org/html/2512.11765v1#A1.E1 "In Appendix A Closed Form of the Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) we then have

|  |  |  |  |
| --- | --- | --- | --- |
| (A.3) |  | 𝝂=(Γθ+(n−1)​Γ~)−1​𝟏=(1−α2)​B−1​Γ−1​𝟏.\displaystyle\bm{\nu}=(\Gamma^{\theta}+(n-1)\widetilde{\Gamma})^{-1}\bm{1}=(1-\alpha^{2})B^{-1}\Gamma^{-1}\bm{1}. |  |

Moreover, the inverse of the Kac–Murdock–Szegő matrix Γ\Gamma is the tridiagonal matrix

|  |  |  |
| --- | --- | --- |
|  | Γ−1=11−α2​(1−α0⋯⋯0−α1+α2−α0⋯00⋱⋱⋱⋱⋮⋮⋱⋱⋱⋱⋮⋮⋱⋱−α1+α2−α0⋯⋯0−α1);\Gamma^{-1}=\frac{1}{1-\alpha^{2}}\begin{pmatrix}1&-\alpha&0&\cdots&\cdots&0\\ -\alpha&1+\alpha^{2}&-\alpha&0&\cdots&0\\ 0&\ddots&\ddots&\ddots&\ddots&\vdots\\ \vdots&\ddots&\ddots&\ddots&\ddots&\vdots\\ \vdots&\ddots&\ddots&-\alpha&1+\alpha^{2}&-\alpha\\ 0&\cdots&\cdots&0&-\alpha&1\end{pmatrix}; |  |

see, e.g., [[12](https://arxiv.org/html/2512.11765v1#bib.bib12), Section 7.2, Problems 12–13]. From this expression, we find that

|  |  |  |  |
| --- | --- | --- | --- |
| (A.4) |  | (1−α2)​Γ−1​𝟏=(1−α,(1−α)2,…,(1−α)2,1−α)⊤.\displaystyle(1-\alpha^{2})\Gamma^{-1}\bm{1}=(1-\alpha,(1-\alpha)^{2},\dots,(1-\alpha)^{2},1-\alpha)^{\top}. |  |

In view of ([A.3](https://arxiv.org/html/2512.11765v1#A1.E3 "In Appendix A Closed Form of the Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")), our main task is then to determine B−1B^{-1}. To that end, we first compute that

|  |  |  |  |
| --- | --- | --- | --- |
|  | B\displaystyle B | =(1−α2)​Id\displaystyle=(1-\alpha^{2})\operatorname{Id} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−α0⋯⋯0−α1+α2−α0⋯00⋱⋱⋱⋱⋮⋮⋱⋱⋱⋱⋮⋮⋱⋱−α1+α2−α0⋯⋯0−α1)​(κ0⋯⋯⋯0(n−1)​ακ0⋯⋯0(n−1)​α2(n−1)​α⋱⋱⋱⋮⋮⋮0⋮(n−1)​αN−1(n−1)​αN−2⋱⋱κ0(n−1)​αN(n−1)​αN−1⋯⋯(n−1)​ακ)\displaystyle+\begin{pmatrix}1&-\alpha&0&\cdots&\cdots&0\\ -\alpha&1+\alpha^{2}&-\alpha&0&\cdots&0\\ 0&\ddots&\ddots&\ddots&\ddots&\vdots\\ \vdots&\ddots&\ddots&\ddots&\ddots&\vdots\\ \vdots&\ddots&\ddots&-\alpha&1+\alpha^{2}&-\alpha\\ 0&\cdots&\cdots&0&-\alpha&1\end{pmatrix}\begin{pmatrix}\kappa&0&\cdots&\cdots&\cdots&0\\ (n-1)\alpha&\kappa&0&\cdots&\cdots&0\\ (n-1)\alpha^{2}&(n-1)\alpha&\ddots&\ddots&\ddots&\vdots\\ \vdots&\vdots&&&0&\vdots\\ (n-1)\alpha^{N-1}&(n-1)\alpha^{N-2}&\ddots&\ddots&\kappa&0\\ (n-1)\alpha^{N}&(n-1)\alpha^{N-1}&\cdots&\cdots&(n-1)\alpha&\kappa\end{pmatrix} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(1−n​α2+κ−α​κ0⋯⋯0−α​(κ+1−n)1+α2​(κ−n)+κ−α​κ0⋯00⋱⋱⋱⋱⋮⋮⋱⋱⋱⋱⋮⋮⋱0−α​(κ+1−n)1+α2​(κ−n)+κ−α​κ0⋯⋯0−α​(κ+1−n)1−α2+κ).\displaystyle=\begin{pmatrix}1-n\alpha^{2}+\kappa&-\alpha\kappa&0&\cdots&\cdots&0\\ -\alpha(\kappa+1-n)&1+\alpha^{2}(\kappa-n)+\kappa&-\alpha\kappa&0&\cdots&0\\ 0&\ddots&\ddots&\ddots&\ddots&\vdots\\ \vdots&\ddots&\ddots&\ddots&\ddots&\vdots\\ \vdots&\ddots&0&-\alpha(\kappa+1-n)&1+\alpha^{2}(\kappa-n)+\kappa&-\alpha\kappa\\ 0&\cdots&\cdots&0&-\alpha(\kappa+1-n)&1-\alpha^{2}+\kappa\end{pmatrix}. |  |

###### Lemma A.1.

For k≤Nk\leq N, the kk*th* leading principal minor δk\delta\_{k} of BB is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | δk\displaystyle\delta\_{k} | =c+​m+k+c−​m−k,\displaystyle=c\_{+}m\_{+}^{k}+c\_{-}m\_{-}^{k}, |  |

where, defining the real number

|  |  |  |
| --- | --- | --- |
|  | R:=α4​(κ−n)2−2​α2​(κ​(κ+1)+n​(1−κ))+(κ+1)2,\displaystyle R\mathrel{\mathop{\ordinarycolon}}=\sqrt{\alpha^{4}(\kappa-n)^{2}-2\alpha^{2}(\kappa(\kappa+1)+n(1-\kappa))+(\kappa+1)^{2}}, |  |

the real numbers c±c\_{\pm} and m±m\_{\pm} are given by

|  |  |  |
| --- | --- | --- |
|  | c±=±(1−α2​(κ+n)+κ)+R2​R,m±=1+α2​(κ−n)+κ±R2.\displaystyle c\_{\pm}=\frac{\pm(1-\alpha^{2}(\kappa+n)+\kappa)+R}{2R},\qquad m\_{\pm}=\frac{1+\alpha^{2}(\kappa-n)+\kappa\pm R}{2}. |  |

###### Proof.

We have

|  |  |  |  |
| --- | --- | --- | --- |
| (A.5) |  | δ1=1−n​α2+κ\delta\_{1}=1-n\alpha^{2}+\kappa |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
| (A.6) |  | δ2=−n​α4​(κ−n)−n​α2​(κ+2)+(κ+1)2.\delta\_{2}=-n\alpha^{4}(\kappa-n)-n\alpha^{2}(\kappa+2)+(\kappa+1)^{2}. |  |

For k∈{3,…,N}k\in\{3,\dots,N\}, the kkth principal minor δk\delta\_{k} satisfies the recursion

|  |  |  |
| --- | --- | --- |
|  | δk=(1+α2​(κ−n)+κ)​δk−1−α2​κ​(κ+1−n)​δk−2.\displaystyle\delta\_{k}=(1+\alpha^{2}(\kappa-n)+\kappa)\delta\_{k-1}-\alpha^{2}\kappa(\kappa+1-n)\delta\_{k-2}. |  |

This is a homogeneous linear difference equation of second-order. Its characteristic equation is

|  |  |  |  |
| --- | --- | --- | --- |
| (A.7) |  | m2−(1+α2​(κ−n)+κ)​m+α2​κ​(κ+1−n)=0.\displaystyle m^{2}-(1+\alpha^{2}(\kappa-n)+\kappa)m+\alpha^{2}\kappa(\kappa+1-n)=0. |  |

The roots of ([A.7](https://arxiv.org/html/2512.11765v1#A1.E7 "In Appendix A Closed Form of the Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) are

|  |  |  |
| --- | --- | --- |
|  | m±=1+α2​(κ−n)+κ±R2.m\_{\pm}=\frac{1+\alpha^{2}(\kappa-n)+\kappa\pm R}{2}. |  |

We first claim that m+m\_{+} and m−m\_{-} are real for α∈[0,1]\alpha\in[0,1] and κ≥n−12\kappa\geq\frac{n-1}{2}. This is equivalent to the nonnegativity of the radicand in RR, which in turn is equivalent to

|  |  |  |
| --- | --- | --- |
|  | f(t):=t2(κ−n)2−2t(κ(κ+1)+n(1−κ))+(κ+1)2≥0,0≤t≤1,f(t)\mathrel{\mathop{\ordinarycolon}}=t^{2}(\kappa-n)^{2}-2t(\kappa(\kappa+1)+n(1-\kappa))+(\kappa+1)^{2}\geq 0,\quad 0\leq t\leq 1, |  |

after setting t=α2t=\alpha^{2}. The claim is clear for κ=n\kappa=n since

|  |  |  |
| --- | --- | --- |
|  | −2​t​(n2+2​n−n2)+n2+2​n+1=n2+1+2​n​(1−2​t)≥(n−1)2≥0.-2t(n^{2}+2n-n^{2})+n^{2}+2n+1=n^{2}+1+2n(1-2t)\geq(n-1)^{2}\geq 0. |  |

Otherwise, ff is minimized at

|  |  |  |
| --- | --- | --- |
|  | t0:=κ​(κ+1)+n​(1−κ)(κ−n)2.t\_{0}\mathrel{\mathop{\ordinarycolon}}=\frac{\kappa(\kappa+1)+n(1-\kappa)}{(\kappa-n)^{2}}. |  |

We have t0<1t\_{0}<1 iff κ<n2−2n+1\kappa<\frac{n^{2}-2}{n+1}. In this case, f​(t)≥f​(t0)=−(κ​(κ+1)+n​(1−κ))2+(κ−n)2​(κ+1)2(κ−n)2>0f(t)\geq f(t\_{0})=\frac{-(\kappa(\kappa+1)+n(1-\kappa))^{2}+(\kappa-n)^{2}(\kappa+1)^{2}}{(\kappa-n)^{2}}>0 for all tt. For κ≥n2−2n+1\kappa\geq\frac{n^{2}-2}{n+1}, we have t0≥1t\_{0}\geq 1 and, in turn, f′​(t)≤0f^{\prime}(t)\leq 0 for 0≤t≤10\leq t\leq 1, so f​(t)≥f​(1)=(n−1)2>0f(t)\geq f(1)=(n-1)^{2}>0. This proves that m±m\_{\pm} are real.

By the theory of second-order linear difference equations, every solution of ([A.7](https://arxiv.org/html/2512.11765v1#A1.E7 "In Appendix A Closed Form of the Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) has the form
c1​m+k+c2​m−kc\_{1}m\_{+}^{k}+c\_{2}m\_{-}^{k}
with real constants c1,c2c\_{1},c\_{2}; see [[14](https://arxiv.org/html/2512.11765v1#bib.bib14), Theorem 3.7].
Imposing the initial conditions ([A.5](https://arxiv.org/html/2512.11765v1#A1.E5 "In Appendix A Closed Form of the Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"))–([A.6](https://arxiv.org/html/2512.11765v1#A1.E6 "In Appendix A Closed Form of the Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) yields c1=c+c\_{1}=c\_{+} and c2=c−c\_{2}=c\_{-}, as stated.
∎

###### Lemma A.2.

Define the sequence ϕk\phi\_{k} recursively by

|  |  |  |
| --- | --- | --- |
|  | ϕN+2=1,ϕN+1=1−α2+κ,\phi\_{N+2}=1,\qquad\phi\_{N+1}=1-\alpha^{2}+\kappa, |  |

and, for k=N,N−1,…,2k=N,N-1,\dots,2,

|  |  |  |
| --- | --- | --- |
|  | ϕk=(1+α2​(κ−n)+κ)​ϕk+1−α2​κ​(κ+1−n)​ϕk+2.\phi\_{k}=(1+\alpha^{2}(\kappa-n)+\kappa)\phi\_{k+1}-\alpha^{2}\kappa(\kappa+1-n)\phi\_{k+2}. |  |

Then, for k∈{2,…,N+2}k\in\{2,\dots,N+2\},

|  |  |  |
| --- | --- | --- |
|  | ϕk=d+​m+N+2−k+d−​m−N+2−k,\phi\_{k}=d\_{+}m\_{+}^{N+2-k}+d\_{-}m\_{-}^{N+2-k}, |  |

where m±m\_{\pm} are as in Lemma [A.1](https://arxiv.org/html/2512.11765v1#A1.Thmtheorem1 "Lemma A.1. ‣ Appendix A Closed Form of the Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") and

|  |  |  |
| --- | --- | --- |
|  | d±:=±(1+(1−α2)​κ−α2​(2−n))+R2​R.d\_{\pm}\mathrel{\mathop{\ordinarycolon}}=\frac{\pm(1+(1-\alpha^{2})\kappa-\alpha^{2}(2-n))+R}{2R}. |  |

###### Proof.

Let

|  |  |  |  |
| --- | --- | --- | --- |
| (A.8) |  | ψ0=1,ψ1=1−α2+κ,\displaystyle\psi\_{0}=1,\qquad\psi\_{1}=1-\alpha^{2}+\kappa, |  |

and, for l∈{2,…,N}l\in\{2,\dots,N\}, set

|  |  |  |  |
| --- | --- | --- | --- |
| (A.9) |  | ψl=(1+α2​(κ−n)+κ)​ψl−1−α2​κ​(κ+1−n)​ψl−2.\displaystyle\psi\_{l}=(1+\alpha^{2}(\kappa-n)+\kappa)\psi\_{l-1}-\alpha^{2}\kappa(\kappa+1-n)\psi\_{l-2}. |  |

Then ψk=ϕN+2−k\psi\_{k}=\phi\_{N+2-k}. As in the proof of Lemma [A.1](https://arxiv.org/html/2512.11765v1#A1.Thmtheorem1 "Lemma A.1. ‣ Appendix A Closed Form of the Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"), the general solution to ([A.9](https://arxiv.org/html/2512.11765v1#A1.E9 "In Appendix A Closed Form of the Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) is d1​m+l+d2​m−ld\_{1}m\_{+}^{l}+d\_{2}m\_{-}^{l} with m±m\_{\pm} as above. Choosing d1=d+d\_{1}=d\_{+} and d2=d−d\_{2}=d\_{-} satisfies the initial conditions ([A.8](https://arxiv.org/html/2512.11765v1#A1.E8 "In Appendix A Closed Form of the Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) and completes the proof.
∎

###### Lemma A.3.

The matrix BB is nonsingular and its inverse is

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (A.10) |  | (B−1)i​j\displaystyle(B^{-1})\_{ij} | ={(α​κ)j−i​δi−1​ϕj+1​δN+1−1,if ​i≤j,(α​(κ+1−n))i−j​δj−1​ϕi+1​δN+1−1,if ​i≥j,\displaystyle=\begin{cases}(\alpha\kappa)^{j-i}\delta\_{i-1}\phi\_{j+1}\delta\_{N+1}^{-1},&\text{if }i\leq j,\\ (\alpha(\kappa+1-n))^{i-j}\delta\_{j-1}\phi\_{i+1}\delta\_{N+1}^{-1},&\text{if }i\geq j,\end{cases} |  |

where δ0=1\delta\_{0}=1 and δN+1=detB\delta\_{N+1}=\det B.

###### Proof.

We have shown in Lemma [2.5](https://arxiv.org/html/2512.11765v1#S2.Thmtheorem5 "Lemma 2.5. ‣ 2.2. Nash Equilibrium ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") that both Γ\Gamma and Γθ+(n−1)​Γ~\Gamma^{\theta}+(n-1)\widetilde{\Gamma} are invertible. Thus

|  |  |  |
| --- | --- | --- |
|  | B=(1−α2)​Γ−1​(Γθ+(n−1)​Γ~)B=(1-\alpha^{2})\Gamma^{-1}(\Gamma^{\theta}+(n-1)\widetilde{\Gamma}) |  |

is also invertible. Hence δN+1≠0\delta\_{N+1}\neq 0, so the right–hand side of ([A.10](https://arxiv.org/html/2512.11765v1#A1.E10 "In Lemma A.3. ‣ Appendix A Closed Form of the Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) is well defined.
In view of Lemmas [A.1](https://arxiv.org/html/2512.11765v1#A1.Thmtheorem1 "Lemma A.1. ‣ Appendix A Closed Form of the Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") and [A.2](https://arxiv.org/html/2512.11765v1#A1.Thmtheorem2 "Lemma A.2. ‣ Appendix A Closed Form of the Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"), the explicit form follows from Usmani’s formula for the inverse of a tridiagonal Jacobi matrix [[24](https://arxiv.org/html/2512.11765v1#bib.bib24)].
∎

###### Theorem A.4 (Explicit form of 𝝎\bm{\omega} and 𝝂\bm{\nu}).

Recall that the vectors 𝐯\bm{v} and 𝐰\bm{w} of the discrete-time equilibrium in Theorem [2.7](https://arxiv.org/html/2512.11765v1#S2.Thmtheorem7 "Theorem 2.7 (Discrete equilibrium). ‣ 2.2. Nash Equilibrium ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") have been written as

|  |  |  |
| --- | --- | --- |
|  | 𝒗=1𝟏⊤​𝝂​𝝂,𝒘=1𝟏⊤​𝝎​𝝎.\displaystyle\bm{v}=\frac{1}{\bm{1}^{\top}\bm{\nu}}\bm{\nu},\qquad\bm{w}=\frac{1}{\bm{1}^{\top}\bm{\omega}}\bm{\omega}. |  |

Let κ~=2​θ+12\tilde{\kappa}=2\theta+\frac{1}{2}. Then the components of 𝛚\bm{\omega} are

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (A.11) |  | ωi\displaystyle\omega\_{i} | =(1−α)​κ~+α​(α​(κ~−1)κ~)N+1−iκ~​(κ~−α​(κ~−1)),i∈{1,…,N+1},\displaystyle=\frac{(1-\alpha)\tilde{\kappa}+\alpha\left(\frac{\alpha(\tilde{\kappa}-1)}{\tilde{\kappa}}\right)^{N+1-i}}{\tilde{\kappa}(\tilde{\kappa}-\alpha(\tilde{\kappa}-1))},\qquad i\in\{1,\dots,N+1\}, |  |

and in particular ωN+1=1/κ~\omega\_{N+1}=1/\tilde{\kappa}.
The components of 𝛎\bm{\nu} are

|  |  |  |  |
| --- | --- | --- | --- |
|  | ν1\displaystyle\nu\_{1} | =1−αδN+1​(ϕ2+(1−α)​∑j=2N(α​κ)j−1​ϕj+1+(α​κ)N),\displaystyle=\frac{1-\alpha}{\delta\_{N+1}}\Bigg(\phi\_{2}+(1-\alpha)\sum\_{j=2}^{N}(\alpha\kappa)^{j-1}\phi\_{j+1}+(\alpha\kappa)^{N}\Bigg), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | νN+1\displaystyle\nu\_{N+1} | =1−αδN+1​((α​(κ+1−n))N+(1−α)​∑j=2N(α​(κ+1−n))N+1−j​δj−1+δN),\displaystyle=\frac{1-\alpha}{\delta\_{N+1}}\Bigg((\alpha(\kappa+1-n))^{N}+(1-\alpha)\sum\_{j=2}^{N}(\alpha(\kappa+1-n))^{N+1-j}\delta\_{j-1}+\delta\_{N}\Bigg), |  |

and, for i=2,…,Ni=2,\dots,N,

|  |  |  |
| --- | --- | --- |
|  | νi=1−αδN+1((α(κ+1−n))i−1ϕi+1+(1−α)∑j=2i−1(α(κ+1−n))i−jδj−1ϕi+1+(1−α)∑j=iN(ακ)j−iδi−1ϕj+1+(ακ)N+1−iδi−1).\begin{split}\nu\_{i}&=\frac{1-\alpha}{\delta\_{N+1}}\Bigg((\alpha(\kappa+1-n))^{i-1}\phi\_{i+1}+(1-\alpha)\sum\_{j=2}^{i-1}(\alpha(\kappa+1-n))^{i-j}\delta\_{j-1}\phi\_{i+1}\\ &\qquad\qquad\qquad\qquad\qquad\quad+(1-\alpha)\sum\_{j=i}^{N}(\alpha\kappa)^{j-i}\delta\_{i-1}\phi\_{j+1}+(\alpha\kappa)^{N+1-i}\delta\_{i-1}\Bigg).\end{split} |  |

###### Proof.

The representation ([A.11](https://arxiv.org/html/2512.11765v1#A1.E11 "In Theorem A.4 (Explicit form of 𝝎 and 𝝂). ‣ Appendix A Closed Form of the Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) for the components of 𝝎\bm{\omega} was proved in [[20](https://arxiv.org/html/2512.11765v1#bib.bib20), Equation (16)] in the case n=2n=2. (Note that our vector 𝝎\bm{\omega} is denoted by 𝒖\bm{u} in [[20](https://arxiv.org/html/2512.11765v1#bib.bib20)], our α\alpha corresponds to a1/Na^{1/N} there, and we have λ=1\lambda=1 here.) By Remark [2.4](https://arxiv.org/html/2512.11765v1#S2.Thmtheorem4 "Remark 2.4. ‣ 2.2. Nash Equilibrium ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"), 𝝎\bm{\omega} does not depend on nn, so the same formula holds for any nn. For 𝝂\bm{\nu}, recall from ([A.3](https://arxiv.org/html/2512.11765v1#A1.E3 "In Appendix A Closed Form of the Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) that

|  |  |  |
| --- | --- | --- |
|  | 𝝂=(Γθ+(n−1)​Γ~)−1​𝟏=(1−α2)​B−1​Γ−1​𝟏.\bm{\nu}=(\Gamma^{\theta}+(n-1)\widetilde{\Gamma})^{-1}\bm{1}=(1-\alpha^{2})B^{-1}\Gamma^{-1}\bm{1}. |  |

Using the explicit expression for (1−α2)​Γ−1​𝟏(1-\alpha^{2})\Gamma^{-1}\bm{1} from ([A.4](https://arxiv.org/html/2512.11765v1#A1.E4 "In Appendix A Closed Form of the Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) and the formula for B−1B^{-1} in Lemma [A.3](https://arxiv.org/html/2512.11765v1#A1.Thmtheorem3 "Lemma A.3. ‣ Appendix A Closed Form of the Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"), we obtain the stated formulas for the components of 𝝂\bm{\nu}.
∎

## Appendix B Proofs for Section [2](https://arxiv.org/html/2512.11765v1#S2 "2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")

We first show uniqueness.

###### Lemma B.1.

For a given time grid 𝕋\mathbb{T} and initial inventories (x1,…,xn)(x\_{1},\dots,x\_{n}), there exists at most one Nash equilibrium in the class ∏i𝒳​(xi,𝕋)\prod\_{i}\mathscr{X}(x\_{i},\mathbb{T}).

###### Proof.

This is a special case of the uniqueness result stated in [[4](https://arxiv.org/html/2512.11765v1#bib.bib4), Theorem 5.1] for a general class of models. To embed the present discrete-time model in that continuous-time setting, we specify an infinite cost for strategies acting outside the grid 𝕋\mathbb{T}; cf. [[4](https://arxiv.org/html/2512.11765v1#bib.bib4), Section 2.3].
∎

Next, we reduce the existence proof to the class

|  |  |  |
| --- | --- | --- |
|  | 𝒳d​e​t(x,𝕋):={𝝃∈𝒳(x,𝕋)∣𝝃 is deterministic}\displaystyle\mathscr{X}\_{det}(x,\mathbb{T})\mathrel{\mathop{\ordinarycolon}}=\{\bm{\xi}\in\mathscr{X}(x,\mathbb{T})\mid\bm{\xi}\text{ is deterministic}\} |  |

of deterministic strategies. A Nash equilibrium in the class 𝒳det​(x1,𝕋)×⋯×𝒳det​(xn,𝕋)\mathscr{X}\_{\rm det}(x\_{1},\mathbb{T})\times\dots\times\mathscr{X}\_{\rm det}(x\_{n},\mathbb{T}) is defined in the same way as in Definition [2.3](https://arxiv.org/html/2512.11765v1#S2.Thmtheorem3 "Definition 2.3 (Nash equilibrium). ‣ 2.2. Nash Equilibrium ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") and called a deterministic Nash equilibrium.

###### Lemma B.2.

A Nash equilibrium in the class 𝒳det​(x1,𝕋)×⋯×𝒳det​(xn,𝕋)\mathscr{X}\_{\rm det}(x\_{1},\mathbb{T})\times\dots\times\mathscr{X}\_{\rm det}(x\_{n},\mathbb{T}) of deterministic strategies is also a Nash equilibrium in the class 𝒳​(x1,𝕋)×⋯×𝒳​(xn,𝕋)\mathscr{X}(x\_{1},\mathbb{T})\times\dots\times\mathscr{X}(x\_{n},\mathbb{T}) of adapted strategies.

###### Proof.

We follow [[20](https://arxiv.org/html/2512.11765v1#bib.bib20), Lemma 3.4]. Assume that (𝝃1∗,…,𝝃n∗)(\bm{\xi}\_{1}^{\*},\dots,\bm{\xi}\_{n}^{\*}) is a Nash equilibrium in the class 𝒳det​(x1,𝕋)×⋯×𝒳det​(xn,𝕋)\mathscr{X}\_{\rm det}(x\_{1},\mathbb{T})\times\dots\times\mathscr{X}\_{\rm det}(x\_{n},\mathbb{T}) of deterministic strategies. We need to show that 𝝃i∗\bm{\xi}\_{i}^{\*} minimizes 𝔼[𝒞𝕋(𝝃|𝝃−i∗)]\mathbb{E}[\mathscr{C}\_{\mathbb{T}}(\bm{\xi}\lvert\bm{\xi}^{\*}\_{-i})] over 𝒳​(xi,𝕋)\mathscr{X}(x\_{i},\mathbb{T}), for any ii. To this end, fix 𝝃∈𝒳​(xi,𝕋)\bm{\xi}\in\mathscr{X}(x\_{i},\mathbb{T}) and define 𝝃¯∈𝒳det​(xi,𝕋)\overline{\bm{\xi}}\in\mathscr{X}\_{\rm det}(x\_{i},\mathbb{T}) by ξ¯k=𝔼​[ξk]\overline{\xi}\_{k}=\mathbb{E}[\xi\_{k}] for k=0,1,…,Nk=0,1,\dots,N.
Applying Jensen’s inequality to the convex map ℝN+1∋𝒙↦𝒙⊤​Γθ​𝒙\mathbb{R}^{N+1}\ni\bm{x}\mapsto\bm{x}^{\top}\Gamma^{\theta}\bm{x} gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[𝒞𝕋​(𝝃∣𝝃−i∗)]\displaystyle\mathbb{E}[\mathscr{C}\_{\mathbb{T}}(\bm{\xi}\mid\bm{\xi}^{\*}\_{-i})] | =𝔼​[12​𝝃⊤​Γθ​𝝃+𝝃⊤​Γ~​∑j≠i𝝃j∗]=𝔼​[12​𝝃⊤​Γθ​𝝃]+𝝃¯⊤​Γ~​∑j≠i𝝃j∗\displaystyle=\mathbb{E}\Big[\frac{1}{2}\bm{\xi}^{\top}\Gamma^{\theta}\bm{\xi}+\bm{\xi}^{\top}\widetilde{\Gamma}\sum\_{j\neq i}\bm{\xi}^{\*}\_{j}\Big]=\mathbb{E}\Big[\frac{1}{2}\bm{\xi}^{\top}\Gamma^{\theta}\bm{\xi}\Big]+\overline{\bm{\xi}}^{\top}\widetilde{\Gamma}\sum\_{j\neq i}\bm{\xi}^{\*}\_{j} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥12​𝝃¯⊤​Γθ​𝝃¯+𝝃¯⊤​Γ~​∑j≠i𝝃j∗=𝔼​[𝒞𝕋​(𝝃¯∣𝝃−i∗)]\displaystyle\geq\frac{1}{2}\overline{\bm{\xi}}^{\top}\Gamma^{\theta}\overline{\bm{\xi}}+\overline{\bm{\xi}}^{\top}\widetilde{\Gamma}\sum\_{j\neq i}\bm{\xi}^{\*}\_{j}=\mathbb{E}[\mathscr{C}\_{\mathbb{T}}(\overline{\bm{\xi}}\mid\bm{\xi}^{\*}\_{-i})] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥𝔼​[𝒞𝕋​(𝝃i∗∣𝝃−i∗)],\displaystyle\geq\mathbb{E}[\mathscr{C}\_{\mathbb{T}}(\bm{\xi}\_{i}^{\*}\mid\bm{\xi}^{\*}\_{-i})], |  |

showing that 𝝃i∗\bm{\xi}\_{i}^{\*} minimizes 𝔼​[𝒞𝕋​(𝝃∣𝝃−i∗)]\mathbb{E}[\mathscr{C}\_{\mathbb{T}}(\bm{\xi}\mid\bm{\xi}^{\*}\_{-i})] over 𝝃∈𝒳​(xi,𝕋)\bm{\xi}\in\mathscr{X}(x\_{i},\mathbb{T}). ∎

We can now establish the main theorem on the discrete-time equilibrium.

###### Proof of Theorem [2.7](https://arxiv.org/html/2512.11765v1#S2.Thmtheorem7 "Theorem 2.7 (Discrete equilibrium). ‣ 2.2. Nash Equilibrium ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact").

We adapt [[15](https://arxiv.org/html/2512.11765v1#bib.bib15), Theorem 2.4]. Recall that uniqueness was shown in Lemma [B.1](https://arxiv.org/html/2512.11765v1#A2.Thmtheorem1 "Lemma B.1. ‣ Appendix B Proofs for Section 2 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"). By Lemma [B.2](https://arxiv.org/html/2512.11765v1#A2.Thmtheorem2 "Lemma B.2. ‣ Appendix B Proofs for Section 2 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"), it then suffices to show that the strategies stated in Theorem [2.7](https://arxiv.org/html/2512.11765v1#S2.Thmtheorem7 "Theorem 2.7 (Discrete equilibrium). ‣ 2.2. Nash Equilibrium ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") form a deterministic Nash equilibrium. In view of Lemma [2.6](https://arxiv.org/html/2512.11765v1#S2.Thmtheorem6 "Lemma 2.6 (Explicit objective). ‣ 2.2. Nash Equilibrium ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"), we thus need to show that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[𝒞𝕋​(𝝃i∗∣𝝃−i∗)]=min𝝃i∈𝒳det​(xi,𝕋)⁡(12​𝝃i⊤​Γθ​𝝃i+𝝃i⊤​Γ~​∑j≠i𝝃j∗).\mathbb{E}[\mathscr{C}\_{\mathbb{T}}(\bm{\xi}^{\*}\_{i}\mid\bm{\xi}^{\*}\_{-i})]=\min\_{\bm{\xi}\_{i}\in\mathscr{X}\_{\mathrm{det}}(x\_{i},\mathbb{T})}\Big(\frac{1}{2}\bm{\xi}\_{i}^{\top}\Gamma^{\theta}\bm{\xi}\_{i}+\bm{\xi}\_{i}^{\top}\widetilde{\Gamma}\sum\_{j\neq i}\bm{\xi}^{\*}\_{j}\Big). |  |

The constraint 𝝃i∈𝒳det​(xi,𝕋)\bm{\xi}\_{i}\in\mathscr{X}\_{\mathrm{det}}(x\_{i},\mathbb{T}) is the linear equality 𝟏⊤​𝝃i=xi\bm{1}^{\top}\bm{\xi}\_{i}=x\_{i}. By Lagrange multiplier theory, a necessary condition for (𝝃1∗,…,𝝃n∗)(\bm{\xi}^{\*}\_{1},\dots,\bm{\xi}^{\*}\_{n}) to be a deterministic Nash equilibrium is the existence of αi∈ℝ\alpha\_{i}\in\mathbb{R}, i=1,…,ni=1,\dots,n, such that

|  |  |  |  |
| --- | --- | --- | --- |
| (B.1) |  | {Γθ​𝝃i∗+Γ~​∑j≠i𝝃j∗=αi​𝟏,𝟏⊤​𝝃i∗=xi.\left\{\begin{array}[]{l}\Gamma^{\theta}\bm{\xi}\_{i}^{\*}+\widetilde{\Gamma}\displaystyle\sum\_{j\neq i}\bm{\xi}\_{j}^{\*}=\alpha\_{i}\bm{1},\\ \bm{1}^{\top}\bm{\xi}\_{i}^{\*}=x\_{i}.\end{array}\right. |  |

We will show below that these equations are also sufficient for our optimization problem. Summing the first line of ([B.1](https://arxiv.org/html/2512.11765v1#A2.E1 "In Appendix B Proofs for Section 2 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) over ii yields

|  |  |  |
| --- | --- | --- |
|  | (Γθ+(n−1)​Γ~)​∑j=1n𝝃j∗=(∑j=1nαj)​𝟏.(\Gamma^{\theta}+(n-1)\widetilde{\Gamma})\sum\_{j=1}^{n}\bm{\xi}\_{j}^{\*}=\Big(\sum\_{j=1}^{n}\alpha\_{j}\Big)\bm{1}. |  |

By Lemma [2.5](https://arxiv.org/html/2512.11765v1#S2.Thmtheorem5 "Lemma 2.5. ‣ 2.2. Nash Equilibrium ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"), Γθ+(n−1)​Γ~\Gamma^{\theta}+(n-1)\widetilde{\Gamma} is invertible. Hence

|  |  |  |  |
| --- | --- | --- | --- |
| (B.2) |  | ∑j=1n𝝃j∗=∑j=1nαj​(Γθ+(n−1)​Γ~)−1​𝟏=𝟏⊤​∑j=1nαj​(Γθ+(n−1)​Γ~)−1​𝟏𝟏⊤​(Γθ+(n−1)​Γ~)−1​𝟏​(Γθ+(n−1)​Γ~)−1​𝟏=∑j=1n𝟏⊤​𝝃j∗𝟏⊤​(Γθ+(n−1)​Γ~)−1​𝟏​(Γθ+(n−1)​Γ~)−1​𝟏=∑j=1nxj​𝒗,\begin{split}\sum^{n}\_{j=1}\bm{\xi}\_{j}^{\*}&=\sum^{n}\_{j=1}\alpha\_{j}(\Gamma^{\theta}+(n-1)\widetilde{\Gamma})^{-1}\bm{1}\\ &=\frac{\bm{1}^{\top}\sum^{n}\_{j=1}\alpha\_{j}(\Gamma^{\theta}+(n-1)\widetilde{\Gamma})^{-1}\bm{1}}{\bm{1}^{\top}(\Gamma^{\theta}+(n-1)\widetilde{\Gamma})^{-1}\bm{1}}(\Gamma^{\theta}+(n-1)\widetilde{\Gamma})^{-1}\bm{1}\\ &=\sum^{n}\_{j=1}\frac{\bm{1}^{\top}\bm{\xi}\_{j}^{\*}}{\bm{1}^{\top}(\Gamma^{\theta}+(n-1)\widetilde{\Gamma})^{-1}\bm{1}}(\Gamma^{\theta}+(n-1)\widetilde{\Gamma})^{-1}\bm{1}\\ &=\sum^{n}\_{j=1}x\_{j}\bm{v},\end{split} |  |

using the second line of ([B.1](https://arxiv.org/html/2512.11765v1#A2.E1 "In Appendix B Proofs for Section 2 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) in the last step. Next, take the iith equation in ([B.1](https://arxiv.org/html/2512.11765v1#A2.E1 "In Appendix B Proofs for Section 2 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")), multiply by n−1n-1, and subtract the sum of the remaining n−1n-1 equations. This gives

|  |  |  |
| --- | --- | --- |
|  | Γθ​((n−1)​𝝃i∗−∑j≠i𝝃j∗)−Γ~​((n−1)​𝝃i∗−∑j≠i𝝃j∗)=((n−1)​αi−∑j≠iαj)​𝟏.\Gamma^{\theta}\Big((n-1)\bm{\xi}\_{i}^{\*}-\sum\_{j\neq i}\bm{\xi}\_{j}^{\*}\Big)-\widetilde{\Gamma}\Big((n-1)\bm{\xi}\_{i}^{\*}-\sum\_{j\neq i}\bm{\xi}\_{j}^{\*}\Big)=\Big((n-1)\alpha\_{i}-\sum\_{j\neq i}\alpha\_{j}\Big)\bm{1}. |  |

Further simplifications show that

|  |  |  |
| --- | --- | --- |
|  | (Γθ−Γ~)​(n​𝝃i∗−∑j=1n𝝃j∗)=(n​αi−∑j=1nαj)​𝟏.(\Gamma^{\theta}-\widetilde{\Gamma})\Big(n\bm{\xi}\_{i}^{\*}-\sum^{n}\_{j=1}\bm{\xi}\_{j}^{\*}\Big)=\Big(n\alpha\_{i}-\sum^{n}\_{j=1}\alpha\_{j}\Big)\bm{1}. |  |

Since Γθ−Γ~\Gamma^{\theta}-\widetilde{\Gamma} is invertible (Lemma [2.5](https://arxiv.org/html/2512.11765v1#S2.Thmtheorem5 "Lemma 2.5. ‣ 2.2. Nash Equilibrium ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
| (B.3) |  | n​𝝃i∗−∑j=1n𝝃j∗=(n​xi−∑j=1nxj)​𝒘.n\bm{\xi}\_{i}^{\*}-\sum\_{j=1}^{n}\bm{\xi}\_{j}^{\*}=\Big(nx\_{i}-\sum\_{j=1}^{n}x\_{j}\Big)\bm{w}. |  |

Combining ([B.2](https://arxiv.org/html/2512.11765v1#A2.E2 "In Appendix B Proofs for Section 2 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) and ([B.3](https://arxiv.org/html/2512.11765v1#A2.E3 "In Appendix B Proofs for Section 2 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) yields

|  |  |  |
| --- | --- | --- |
|  | 𝝃i∗=x¯​𝒗+(xi−x¯)​𝒘.\bm{\xi}\_{i}^{\*}=\bar{x}\bm{v}+(x\_{i}-\bar{x})\bm{w}. |  |

It remains to show that ([B.1](https://arxiv.org/html/2512.11765v1#A2.E1 "In Appendix B Proofs for Section 2 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) is sufficient. Write

|  |  |  |
| --- | --- | --- |
|  | 12𝝃i∗⊤Γθ𝝃i+𝝃i∗⊤Γ~∑j≠i𝝃j∗=12𝝃i∗⊤Γθ𝝃i∗+𝒈i⊤𝝃i∗,𝒈i:=Γ~∑j≠i𝝃j∗.\frac{1}{2}{\bm{\xi}\_{i}^{\*}}^{\top}\Gamma^{\theta}\bm{\xi}\_{i}+{\bm{\xi}\_{i}^{\*}}^{\top}\widetilde{\Gamma}\sum\_{j\neq i}\bm{\xi}^{\*}\_{j}=\frac{1}{2}{\bm{\xi}\_{i}^{\*}}^{\top}\Gamma^{\theta}\bm{\xi}\_{i}^{\*}+\bm{g}\_{i}^{\top}\bm{\xi}^{\*}\_{i},\qquad\bm{g}\_{i}\mathrel{\mathop{\ordinarycolon}}=\widetilde{\Gamma}\sum\_{j\neq i}\bm{\xi}^{\*}\_{j}. |  |

For any 𝜼i∈𝒳det​(xi,𝕋)\bm{\eta}\_{i}\in\mathscr{X}\_{\mathrm{det}}(x\_{i},\mathbb{T}), using ([B.1](https://arxiv.org/html/2512.11765v1#A2.E1 "In Appendix B Proofs for Section 2 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) and the symmetry of Γθ\Gamma^{\theta},

|  |  |  |  |
| --- | --- | --- | --- |
| (B.4) |  | 12​𝜼𝒊⊤​Γθ​𝜼𝒊+𝒈𝒊⊤​𝜼𝒊−12​𝝃i∗⊤​Γθ​𝝃i∗−𝒈𝒊⊤​𝝃i∗=12​(𝜼𝒊+𝝃i∗)⊤​Γθ​(𝜼𝒊−𝝃i∗)+𝒈𝒊⊤​(𝜼𝒊−𝝃i∗)=(12​(Γθ)⊤​(𝜼𝒊+𝝃i∗)+𝒈𝒊)⊤​(𝜼𝒊−𝝃i∗)=((Γθ​𝝃i∗+𝒈𝒊)+12​(Γθ)⊤​(𝜼𝒊−𝝃i∗))⊤​(𝜼𝒊−𝝃i∗)=(αi​𝟏+12​(Γθ)⊤​(𝜼𝒊−𝝃i∗))⊤​(𝜼𝒊−𝝃i∗)=αi​𝟏⊤​(𝜼𝒊−𝝃i∗)+12​(𝜼𝒊−𝝃i∗)⊤​Γθ​(𝜼𝒊−𝝃i∗)≥0,\begin{split}\frac{1}{2}\bm{\eta\_{i}}^{\top}\Gamma^{\theta}\bm{\eta\_{i}}+\bm{g\_{i}}^{\top}\bm{\eta\_{i}}-\frac{1}{2}{\bm{\xi}\_{i}^{\*}}^{\top}\Gamma^{\theta}{\bm{\xi}\_{i}^{\*}}-\bm{g\_{i}}^{\top}{\bm{\xi}\_{i}^{\*}}&=\frac{1}{2}(\bm{\eta\_{i}}+{\bm{\xi}\_{i}^{\*}})^{\top}\Gamma^{\theta}(\bm{\eta\_{i}}-{\bm{\xi}\_{i}^{\*}})+\bm{g\_{i}}^{\top}(\bm{\eta\_{i}}-{\bm{\xi}\_{i}^{\*}})\\ &=\Big(\frac{1}{2}(\Gamma^{\theta})^{\top}(\bm{\eta\_{i}}+{\bm{\xi}\_{i}^{\*}})+\bm{g\_{i}}\Big)^{\top}(\bm{\eta\_{i}}-{\bm{\xi}\_{i}^{\*}})\\ &=\Big((\Gamma^{\theta}{\bm{\xi}\_{i}^{\*}}+\bm{g\_{i}})+\frac{1}{2}(\Gamma^{\theta})^{\top}(\bm{\eta\_{i}}-{\bm{\xi}\_{i}^{\*}})\Big)^{\top}(\bm{\eta\_{i}}-{\bm{\xi}\_{i}^{\*}})\\ &=\Big(\alpha\_{i}\bm{1}+\frac{1}{2}(\Gamma^{\theta})^{\top}(\bm{\eta\_{i}}-{\bm{\xi}\_{i}^{\*}})\Big)^{\top}(\bm{\eta\_{i}}-{\bm{\xi}\_{i}^{\*}})\\ &=\alpha\_{i}\bm{1}^{\top}(\bm{\eta\_{i}}-{\bm{\xi}\_{i}^{\*}})+\frac{1}{2}(\bm{\eta\_{i}}-{\bm{\xi}\_{i}^{\*}})^{\top}\Gamma^{\theta}(\bm{\eta\_{i}}-{\bm{\xi}\_{i}^{\*}})\\ &\geq 0,\end{split} |  |

with equality if and only if 𝜼𝒊=𝝃i∗\bm{\eta\_{i}}={\bm{\xi}\_{i}^{\*}}. Therefore, the strategy profile defined by ([2.4](https://arxiv.org/html/2512.11765v1#S2.E4 "In Theorem 2.7 (Discrete equilibrium). ‣ 2.2. Nash Equilibrium ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) is a deterministic Nash equilibrium and the proof is complete.
∎

We mention that the proofs in this section remain valid if the exponential kernel GG is generalized to an arbitrary positive definite kernel (in the sense of Bochner).

## Appendix C Proofs for Section [4](https://arxiv.org/html/2512.11765v1#S4 "4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")

The proofs for the high-frequency asymptotics of Section [4](https://arxiv.org/html/2512.11765v1#S4 "4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") involve rather lengthy expressions. We start with some abstract remarks and notation intended to make the exposition more concise. While the quantities introduced in Appendix [A](https://arxiv.org/html/2512.11765v1#A1 "Appendix A Closed Form of the Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") (e.g., α\alpha, 𝝂\bm{\nu}, 𝝎\bm{\omega}) depend on the trading frequency NN, we usually suppress this dependence for brevity. Throughout, we let N↑∞N\uparrow\infty, so, for example, we write

|  |  |  |
| --- | --- | --- |
|  | limN↑∞α=limN↑∞e−ρ​T/N=1.\lim\_{N\uparrow\infty}\alpha=\lim\_{N\uparrow\infty}e^{-\rho T/N}=1. |  |

For t∈[0,T]t\in[0,T] we recall the discrete trading index nt=⌈N​t/T⌉n\_{t}=\lceil Nt/T\rceil and denote the distance between N​t/TNt/T and the subsequent grid point by

|  |  |  |
| --- | --- | --- |
|  | ηtN:=nt−N​tT∈[0,1).\eta\_{t}^{N}\mathrel{\mathop{\ordinarycolon}}=n\_{t}-\frac{Nt}{T}\in[0,1). |  |

This will appear, for example, when first-order terms depend on ntn\_{t}.

Rather than expanding every expression directly in powers of N−1N^{-1}, it will be often convenient to introduce the small parameter
Δ:=1−α=1−e−ρ​T/N.\Delta\mathrel{\mathop{\ordinarycolon}}=1-\alpha=1-e^{-\rho T/N}.
A Taylor expansion at 0 yields

|  |  |  |
| --- | --- | --- |
|  | Δ=ρ​TN−(ρ​T)22​N2+𝒪​(N−3),1N=Δρ​T+Δ22​ρ​T+𝒪​(Δ3).\Delta=\frac{\rho T}{N}-\frac{(\rho T)^{2}}{2N^{2}}+\mathcal{O}(N^{-3}),\qquad\frac{1}{N}=\frac{\Delta}{\rho T}+\frac{\Delta^{2}}{2\rho T}+\mathcal{O}(\Delta^{3}). |  |

Hence o​(N−p)o(N^{-p}) and o​(Δp)o(\Delta^{p}) are interchangeable; we switch between these two symbols as convenient.

All the functions we manipulate are real-analytic in the neighborhoods we consider. Two consequences, often used without further comment, are the following.

1. (a)

   *Stability under algebraic operations.* If AN=a0+o​(N−p)A\_{N}=a\_{0}+o(N^{-p}) and BN=b0+o​(N−p)B\_{N}=b\_{0}+o(N^{-p}), then

   |  |  |  |
   | --- | --- | --- |
   |  | AN±BN=(a0±b0)+o​(N−p),AN​BN=a0​b0+o​(N−p),A\_{N}\pm B\_{N}=(a\_{0}\pm b\_{0})+o(N^{-p}),\qquad A\_{N}B\_{N}=a\_{0}b\_{0}+o(N^{-p}), |  |

   and, provided b0≠0b\_{0}\neq 0,

   |  |  |  |
   | --- | --- | --- |
   |  | ANBN=a0b0+o​(N−p).\frac{A\_{N}}{B\_{N}}=\frac{a\_{0}}{b\_{0}}+o(N^{-p}). |  |

   Thus sums, products, and quotients preserve the error order.
2. (b)

   *Stability under composition.* If XN=x0+rNX\_{N}=x\_{0}+r\_{N} with rN=o​(N−p)r\_{N}=o(N^{-p}) and hh is real-analytic on a neighborhood UU of x0x\_{0}, then by Taylor’s formula with Lagrange remainder, for any fixed q∈ℕq\in\mathbb{N} and all sufficiently large NN,

   |  |  |  |
   | --- | --- | --- |
   |  | h​(XN)=∑k=0qh(k)​(x0)k!​rNk+h(q+1)​(x0+ζN​rN)(q+1)!​rNq+1,ζN∈(0,1).h(X\_{N})=\sum\_{k=0}^{q}\frac{h^{(k)}(x\_{0})}{k!}r\_{N}^{k}+\frac{h^{(q+1)}(x\_{0}+\zeta\_{N}r\_{N})}{(q+1)!}r\_{N}^{q+1},\qquad\zeta\_{N}\in(0,1). |  |

   Hence, if rN=𝒪​(N−m)r\_{N}=\mathcal{O}(N^{-m}) and (q+1)​m>p(q+1)m>p, the remainder is o​(N−p)o(N^{-p}). In particular, in our setting, compositions of finitely many analytic maps preserve o​(N−p)o(N^{-p}) remainders (equivalently o​(Δp)o(\Delta^{p})). Typical uses below include h​(x)=1/xh(x)=1/x (with x0≠0x\_{0}\neq 0), h​(x)=xh(x)=\sqrt{x} (with x0>0x\_{0}>0), log⁡x\log x (with x0>0x\_{0}>0), and their compositions.

Whenever a quotient of two analytic expansions is required, we identify the coefficients via the standard series-division rule below; see also [[7](https://arxiv.org/html/2512.11765v1#bib.bib7), § 67]. This will be used repeatedly when taking quotients of closed forms and extracting leading constants.

###### Lemma C.1 (Quotient of analytic Taylor series).

Let I⊂ℝI\subset\mathbb{R} be an open interval containing aa, and let f,gf,g be real-analytic on II with

|  |  |  |
| --- | --- | --- |
|  | f​(x)=∑k≥0ak​(x−a)k,g​(x)=∑k≥0bk​(x−a)k,f(x)=\sum\_{k\geq 0}a\_{k}(x-a)^{k},\qquad g(x)=\sum\_{k\geq 0}b\_{k}(x-a)^{k}, |  |

both converging on some interval (a−R,a+R)⊂I(a-R,a+R)\subset I. If b0=g​(a)≠0b\_{0}=g(a)\neq 0, then f/gf/g is real-analytic on (a−r,a+r)(a-r,a+r) for some r∈(0,R)r\in(0,R) with

|  |  |  |
| --- | --- | --- |
|  | f​(x)g​(x)=∑k≥0ck​(x−a)k,\frac{f(x)}{g(x)}=\sum\_{k\geq 0}c\_{k}(x-a)^{k}, |  |

and the coefficients {ck}k≥0\{c\_{k}\}\_{k\geq 0} are uniquely determined by

|  |  |  |
| --- | --- | --- |
|  | b0​c0=a0,∑j=0mbj​cm−j=am(m≥1).b\_{0}c\_{0}=a\_{0},\qquad\sum\_{j=0}^{m}b\_{j}c\_{m-j}=a\_{m}\quad(m\geq 1). |  |

###### Remark C.2.

In particular, at first order one has

|  |  |  |  |
| --- | --- | --- | --- |
| (C.1) |  | f​(x)g​(x)=a0b0+a1​b0−a0​b1b02​(x−a)+higher-order terms.\displaystyle\frac{f(x)}{g(x)}=\frac{a\_{0}}{b\_{0}}+\frac{a\_{1}b\_{0}-a\_{0}b\_{1}}{b\_{0}^{2}}(x-a)+\text{higher-order terms}. |  |

The subsequent proofs proceed by expanding all discrete objects using the conventions above, together with ([C.1](https://arxiv.org/html/2512.11765v1#A3.E1 "In Remark C.2. ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")), to organize remainders into o​(N−p)o(N^{-p}) at the target order.

### C.1. Proof of Theorem [4.1](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem1 "Theorem 4.1 (Convergence of strategies for 𝜃>0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") [(b)](https://arxiv.org/html/2512.11765v1#S4.I1.i2 "item (b) ‣ Theorem 4.1 (Convergence of strategies for 𝜃>0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")

We remark that the convergence of Wt(N)W^{(N)}\_{t} to 𝕗​(t)\mathbbm{f}(t) for t∈[0,T)t\in[0,T), without a rate, already follows from [[19](https://arxiv.org/html/2512.11765v1#bib.bib19), Theorem 3.1(c)] as W(N)W^{(N)} is independent of nn by Remark [2.4](https://arxiv.org/html/2512.11765v1#S2.Thmtheorem4 "Remark 2.4. ‣ 2.2. Nash Equilibrium ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"). Next, we establish the 1/N1/N rate and recover their result as a by-product. We observe that (in contrast to the statement in [[19](https://arxiv.org/html/2512.11765v1#bib.bib19), Theorem 3.1(c)], which seems to have a glitch) the sequence WT(N)W\_{T}^{(N)} does not converge to 𝕗​(T)\mathbbm{f}(T).

###### Proof of Theorem [4.1](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem1 "Theorem 4.1 (Convergence of strategies for 𝜃>0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") [(b)](https://arxiv.org/html/2512.11765v1#S4.I1.i2 "item (b) ‣ Theorem 4.1 (Convergence of strategies for 𝜃>0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact").

Using the closed-form expression in Theorem [A.4](https://arxiv.org/html/2512.11765v1#A1.Thmtheorem4 "Theorem A.4 (Explicit form of 𝝎 and 𝝂). ‣ Appendix A Closed Form of the Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"),

|  |  |  |  |
| --- | --- | --- | --- |
| (C.2) |  | Wt(N)=1𝟏⊤​𝝎​∑k=nt+1N+1ωk=(N+1−nt)​(1−α)κ~−α​(κ~−1)+ακ~​(κ~−α​(κ~−1))​1−(α​(κ~−1)κ~)N+1−nt1−α​(κ~−1)κ~(N+1)​(1−α)κ~−α​(κ~−1)+ακ~​(κ~−α​(κ~−1))​1−(α​(κ~−1)κ~)N+11−α​(κ~−1)κ~.\displaystyle W^{(N)}\_{t}=\frac{1}{\mathbf{1}^{\top}\bm{\omega}}\sum\_{k=n\_{t}+1}^{N+1}\omega\_{k}=\frac{(N+1-n\_{t})\frac{(1-\alpha)}{\tilde{\kappa}-\alpha(\tilde{\kappa}-1)}+\frac{\alpha}{\tilde{\kappa}(\tilde{\kappa}-\alpha(\tilde{\kappa}-1))}\frac{1-\left(\frac{\alpha(\tilde{\kappa}-1)}{\tilde{\kappa}}\right)^{N+1-n\_{t}}}{1-\frac{\alpha(\tilde{\kappa}-1)}{\tilde{\kappa}}}}{(N+1)\frac{(1-\alpha)}{\tilde{\kappa}-\alpha(\tilde{\kappa}-1)}+\frac{\alpha}{\tilde{\kappa}(\tilde{\kappa}-\alpha(\tilde{\kappa}-1))}\frac{1-\left(\frac{\alpha(\tilde{\kappa}-1)}{\tilde{\kappa}}\right)^{N+1}}{1-\frac{\alpha(\tilde{\kappa}-1)}{\tilde{\kappa}}}}. |  |

We first treat t=Tt=T. With κ~=2​θ+12\tilde{\kappa}=2\theta+\frac{1}{2} and using ([C.1](https://arxiv.org/html/2512.11765v1#A3.E1 "In Remark C.2. ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")),

|  |  |  |
| --- | --- | --- |
|  | WT(N)=ωN+1𝟏⊤​𝝎=1κ~​𝟏⊤​𝝎=1κ~​(ρ​T+1)−1N​(κ~−32)​ρ2​T2−2​ρ​T​(κ~−1)​(ρ​T+1)κ~​(ρ​T+1)2+o​(1N),W^{(N)}\_{T}=\frac{\omega\_{N+1}}{\mathbf{1}^{\top}\bm{\omega}}=\frac{1}{\tilde{\kappa}\mathbf{1}^{\top}\bm{\omega}}=\frac{1}{\tilde{\kappa}(\rho T+1)}-\frac{1}{N}\frac{(\tilde{\kappa}-\frac{3}{2})\rho^{2}T^{2}-2\rho T(\tilde{\kappa}-1)(\rho T+1)}{\tilde{\kappa}(\rho T+1)^{2}}+o\left(\frac{1}{N}\right), |  |

which yields the stated claim at t=Tt=T.

Now fix t∈[0,T)t\in[0,T) and apply ([C.1](https://arxiv.org/html/2512.11765v1#A3.E1 "In Remark C.2. ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"))–([C.2](https://arxiv.org/html/2512.11765v1#A3.E2 "In C.1. Proof of Theorem 4.1 (b) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")). A direct calculation (whose details we omit for the sake of brevity) yields

|  |  |  |
| --- | --- | --- |
|  | N​|Wt(N)−𝕗​(t)|=ρ​Tρ​T+1​|ηtN+ρ​t​(2​θ−1)ρ​T+1|+o​(1),N→∞.N|W^{(N)}\_{t}-\mathbbm{f}(t)|=\frac{\rho T}{\rho T+1}\bigg|\eta\_{t}^{N}+\frac{\rho t(2\theta-1)}{\rho T+1}\bigg|+o(1),\qquad N\to\infty. |  |

This proves the claimed 𝒪​(N−1)\mathcal{O}(N^{-1}) rate of convergence to 𝕗​(t)\mathbbm{f}(t) for every fixed t∈[0,T)t\in[0,T).
∎

### C.2. Proof of Theorem [4.1](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem1 "Theorem 4.1 (Convergence of strategies for 𝜃>0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") [(a)](https://arxiv.org/html/2512.11765v1#S4.I1.i1 "item (a) ‣ Theorem 4.1 (Convergence of strategies for 𝜃>0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")

We state separately the proofs for κ=n−1\kappa=n-1 and κ≠n−1\kappa\neq n-1. The details are different because the general representation for the sum of the components of 𝝂\bm{\nu} in ([C.7](https://arxiv.org/html/2512.11765v1#A3.E7 "In Lemma C.4. ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) involves denominators that vanish exactly at κ=n−1\kappa=n-1, and therefore is not well defined at this value.

#### C.2.1. Proof for κ=n−1\kappa=n-1

Adapting arguments from [[19](https://arxiv.org/html/2512.11765v1#bib.bib19)], we first consider the case κ=n−1\kappa=n-1, which corresponds to θ=n−14\theta=\frac{n-1}{4}. The proof of Theorem [4.1](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem1 "Theorem 4.1 (Convergence of strategies for 𝜃>0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")[(a)](https://arxiv.org/html/2512.11765v1#S4.I1.i1 "item (a) ‣ Theorem 4.1 (Convergence of strategies for 𝜃>0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") for this particular value of κ\kappa will be given after the following lemma.

###### Lemma C.3.

Let κ=n−1\kappa=n-1. Then, for m∈{1,…,N+1}m\in\{1,\dots,N+1\},

|  |  |  |  |
| --- | --- | --- | --- |
| (C.3) |  | ∑i=1mνi=1n+α​((1−α)​m+α+α​(α2−n)n​(n+α)​(α​(n−1)n−α2)N+1+α​(1+α)n+α​(α​(n−1)n−α2)N+1−m).\displaystyle\sum\_{i=1}^{m}\nu\_{i}=\frac{1}{n+\alpha}\left((1-\alpha)m+\alpha+\frac{\alpha(\alpha^{2}-n)}{n(n+\alpha)}\left(\frac{\alpha(n-1)}{n-\alpha^{2}}\right)^{N+1}+\frac{\alpha(1+\alpha)}{n+\alpha}\left(\frac{\alpha(n-1)}{n-\alpha^{2}}\right)^{N+1-m}\right). |  |

###### Proof.

Plugging in κ=n−1\kappa=n-1 yields R=n−α2R=n-\alpha^{2}, δk=n​(1−α2)​(n−α2)k−1\delta\_{k}=n(1-\alpha^{2})(n-\alpha^{2})^{k-1} for k∈{1,…,N+1}k\in\{1,\dots,N+1\}, and ϕk=(n−α2)N+2−k\phi\_{k}=(n-\alpha^{2})^{N+2-k} for k∈{2,…,N+2}k\in\{2,\dots,N+2\}. Therefore,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (C.4) |  | ν1\displaystyle\nu\_{1} | =1n+α​(1+(n−α2n​(n−1))​(α​(n−1)n−α2)N+1),\displaystyle=\frac{1}{n+\alpha}\left(1+\left(\frac{n-\alpha^{2}}{n(n-1)}\right)\left(\frac{\alpha(n-1)}{n-\alpha^{2}}\right)^{N+1}\right), |  |
|  | νi\displaystyle\nu\_{i} | =1n+α​(1−α+(α​(n−1)n−α2)N+2−i​(1−α2n−1)),i∈{2,…,N+1}.\displaystyle=\frac{1}{n+\alpha}\left(1-\alpha+\left(\frac{\alpha(n-1)}{n-\alpha^{2}}\right)^{N+2-i}\left(\frac{1-\alpha^{2}}{n-1}\right)\right),\qquad i\in\{2,\dots,N+1\}. |  |

Summing ([C.4](https://arxiv.org/html/2512.11765v1#A3.E4 "In C.2.1. Proof for 𝜅=𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) over i=1,…,mi=1,\dots,m yields ([C.3](https://arxiv.org/html/2512.11765v1#A3.E3 "In Lemma C.3. ‣ C.2.1. Proof for 𝜅=𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")).
∎

###### Proof of Theorem [4.1](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem1 "Theorem 4.1 (Convergence of strategies for 𝜃>0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") [(a)](https://arxiv.org/html/2512.11765v1#S4.I1.i1 "item (a) ‣ Theorem 4.1 (Convergence of strategies for 𝜃>0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") for κ=n−1\kappa=n-1.

Recall that α=e−ρ​T/N\alpha=e^{-\rho T/N}. Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1−α)​nt\displaystyle(1-\alpha)n\_{t} | =ρ​t+1N​(ηtN​ρ​T−ρ2​T​t2)+o​(1N),\displaystyle=\rho t+\frac{1}{N}\big(\eta\_{t}^{N}\rho T-\tfrac{\rho^{2}Tt}{2}\big)+o\!\left(\frac{1}{N}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (α​(n−1)n−α2)N+1\displaystyle\left(\frac{\alpha(n-1)}{n-\alpha^{2}}\right)^{N+1} | =e−ρ​T​n+1n−1​(1+1N​(−ρ​T​n+1n−1+2​n​ρ2​T2(n−1)2))+o​(1N),\displaystyle=e^{-\rho T\frac{n+1}{n-1}}\bigg(1+\frac{1}{N}\Big(-\rho T\frac{n+1}{n-1}+\frac{2n\rho^{2}T^{2}}{(n-1)^{2}}\Big)\bigg)+o\!\left(\frac{1}{N}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (α​(n−1)n−α2)N+1−nt\displaystyle\left(\frac{\alpha(n-1)}{n-\alpha^{2}}\right)^{N+1-n\_{t}} | =e−ρ​n+1n−1​(T−t)​(1+1N​(2​n​ρ2​T​(T−t)(n−1)2−(1−ηtN)​ρ​T​n+1n−1))+o​(1N),\displaystyle=e^{-\rho\frac{n+1}{n-1}(T-t)}\bigg(1+\frac{1}{N}\Big(\frac{2n\rho^{2}T(T-t)}{(n-1)^{2}}-(1-\eta\_{t}^{N})\rho T\frac{n+1}{n-1}\Big)\bigg)+o\!\left(\frac{1}{N}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 1n+α\displaystyle\frac{1}{n+\alpha} | =1n+1+ρ​TN​(n+1)2+o​(1N),\displaystyle=\frac{1}{n+1}+\frac{\rho T}{N(n+1)^{2}}+o\!\left(\frac{1}{N}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | α\displaystyle\alpha | =1−ρ​TN+o​(1N),\displaystyle=1-\frac{\rho T}{N}+o\!\left(\frac{1}{N}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | α​(α2−n)n​(n+α)\displaystyle\frac{\alpha(\alpha^{2}-n)}{n(n+\alpha)} | =1−nn​(n+1)+1N​ρ​T​(n2−3​n−2)n​(n+1)2+o​(1N),\displaystyle=\frac{1-n}{n(n+1)}+\frac{1}{N}\frac{\rho T(n^{2}-3n-2)}{n(n+1)^{2}}+o\!\left(\frac{1}{N}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | α​(1+α)n+α\displaystyle\frac{\alpha(1+\alpha)}{n+\alpha} | =2n+1−1N​ρ​T​(3​n+1)(n+1)2+o​(1N)\displaystyle=\frac{2}{n+1}-\frac{1}{N}\frac{\rho T(3n+1)}{(n+1)^{2}}+o\!\left(\frac{1}{N}\right) |  |

for all t∈(0,T]t\in(0,T]. Moreover,

|  |  |  |
| --- | --- | --- |
|  | (1−α)​(N+1)=ρ​T+ρ​T−ρ2​T22N+o​(1N).({1-\alpha})(N+1)=\rho T+\frac{\rho T-\frac{\rho^{2}T^{2}}{2}}{N}+o\left({\frac{1}{N}}\right). |  |

Putting everything together in ([C.3](https://arxiv.org/html/2512.11765v1#A3.E3 "In Lemma C.3. ‣ C.2.1. Proof for 𝜅=𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) yields

|  |  |  |  |
| --- | --- | --- | --- |
| (C.5) |  | ∑i=1N+1νi=e−ρ​n+1n−1​T(n+1)2​n​(n​((ρ​T+1)​(n+1)+2)​eρ​n+1n−1​T−(n−1))+𝒬​1N+o​(1N),\displaystyle\sum\_{i=1}^{N+1}\nu\_{i}=\frac{e^{-\rho\frac{n+1}{n-1}T}}{(n+1)^{2}n}\Big(n\big((\rho T+1)(n+1)+2\big)e^{\rho\frac{n+1}{n-1}T}-(n-1)\Big)+\mathscr{Q}\frac{1}{N}+o\left({\frac{1}{N}}\right), |  |

where

|  |  |  |
| --- | --- | --- |
|  | 𝒬=ρ​T2​(n+1)3​((ρ​T)​(1−n2)−4​(n−1))+e−ρ​T​n+1n−1​(2​ρ​T​(n−1)(n+1)3−2​ρ2​T2(n+1)2​(n−1))\displaystyle\mathscr{Q}=\frac{\rho T}{2({n+1})^{3}}\left({(\rho T)({1-n^{2}})-4(n-1)}\right)+e^{-\rho T\frac{n+1}{n-1}}\left(\frac{2\rho T(n-1)}{(n+1)^{3}}-\frac{2\rho^{2}T^{2}}{(n+1)^{2}(n-1)}\right) |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
| (C.6) |  | ∑i=1ntνi=e−ρ​n+1n−1​T(n+1)2​n​(n​(ρ​t+1)​(n+1)​eρ​n+1n−1​T−(n−1)+2​n​eρ​n+1n−1​t)+ℛN​(t)​1N+o​(1N),\displaystyle\sum\_{i=1}^{n\_{t}}\nu\_{i}=\frac{e^{-\rho\frac{n+1}{n-1}T}}{(n+1)^{2}n}\Big(n(\rho t+1)(n+1)e^{\rho\frac{n+1}{n-1}T}-(n-1)+2ne^{\rho\frac{n+1}{n-1}t}\Big)+\mathscr{R}\_{N}(t)\frac{1}{N}+o\left({\frac{1}{N}}\right), |  |

where

|  |  |  |
| --- | --- | --- |
|  | ℛN​(t)=1n+1​b1​(t,ηtN)+ρ​T(n+1)2​b0​(t)\mathscr{R}\_{N}(t)=\frac{1}{n+1}b\_{1}({t,\eta\_{t}^{N}})+\frac{\rho T}{({n+1})^{2}}b\_{0}({t}) |  |

with

|  |  |  |
| --- | --- | --- |
|  | b0​(t)=ρ​t+1+1−nn​(n+1)​e−ρ​n+1n−1​T+2n+1​e−ρ​n+1n−1​(T−t)b\_{0}({t})=\rho t+1+\frac{1-n}{n({n+1})}e^{-\rho\frac{n+1}{n-1}T}+\frac{2}{n+1}e^{-\rho\frac{n+1}{n-1}({T-t})} |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | b1​(t,η)\displaystyle b\_{1}({t,\eta}) | =η​ρ​T−ρ2​T​t2−ρ​T+e−ρ​n+1n−1​T​1−nn​(n+1)​(−ρ​T​(n+1)n−1+2​n​ρ2​T2(n−1)2)\displaystyle=\eta\rho T-\frac{\rho^{2}Tt}{2}-\rho T+e^{-\rho\frac{n+1}{n-1}T}\frac{1-n}{n({n+1})}\left({-\frac{\rho T({n+1})}{n-1}+\frac{2n\rho^{2}T^{2}}{({n-1})^{2}}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +e−ρ​n+1n−1​T​ρ​T​(n2−3​n−2)n​(n+1)2+2n+1​e−ρ​n+1n−1​(T−t)​(2​n​ρ2​T​(T−t)(n−1)2−(1−η)​ρ​T​n+1n−1)\displaystyle\quad+e^{-\rho\frac{n+1}{n-1}T}\frac{\rho T({n^{2}-3n-2})}{n({n+1})^{2}}+\frac{2}{n+1}e^{-\rho\frac{n+1}{n-1}({T-t})}\left({\frac{2n\rho^{2}T({T-t})}{({n-1})^{2}}-({1-\eta})\rho T\frac{n+1}{n-1}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −ρ​T​(3​n+1)(n+1)2​e−ρ​n+1n−1​(T−t).\displaystyle\quad-\frac{\rho T({3n+1})}{({n+1})^{2}}e^{-\rho\frac{n+1}{n-1}({T-t})}. |  |

Because ηtN∈[0,1)\eta\_{t}^{N}\in[0,1) for all N∈ℕN\in\mathbb{N} and b1b\_{1} depends linearly on ηtN\eta\_{t}^{N}, the sequence ℛN​(t)\mathscr{R}\_{N}(t) is bounded for fixed parameters θ,T,ρ,n\theta,T,\rho,n.

Finally, plugging ([C.5](https://arxiv.org/html/2512.11765v1#A3.E5 "In C.2.1. Proof for 𝜅=𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) and ([C.6](https://arxiv.org/html/2512.11765v1#A3.E6 "In C.2.1. Proof for 𝜅=𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) into the definition of Vt(N)V^{(N)}\_{t} and applying ([C.1](https://arxiv.org/html/2512.11765v1#A3.E1 "In Remark C.2. ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) once more yields the claim.
∎

#### C.2.2. Proof for κ≠n−1\kappa\neq n-1

We now prepare for the proof of Theorem [4.1](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem1 "Theorem 4.1 (Convergence of strategies for 𝜃>0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") [(a)](https://arxiv.org/html/2512.11765v1#S4.I1.i1 "item (a) ‣ Theorem 4.1 (Convergence of strategies for 𝜃>0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") for the case κ≠n−1\kappa\neq n-1. We introduce the shorthand

|  |  |  |
| --- | --- | --- |
|  | [x]m:=1−αδN+1xm[x]^{m}\mathrel{\mathop{\ordinarycolon}}=\frac{1-\alpha}{\delta\_{N+1}}x^{m} |  |

for x∈ℝx\in\mathbb{R} and m∈ℕm\in\mathbb{N}, which is convenient when taking limits of terms such as [x]N\left[x\right]^{N}.

###### Lemma C.4.

Let κ≥n−12\kappa\geq\frac{n-1}{2} and κ≠n−1\kappa\neq n-1. Define κ^:=n−1\hat{\kappa}\mathrel{\mathop{\ordinarycolon}}=n-1 and C1:=α​(α+1)κ+1−α​(κ−κ^−1)C\_{1}\mathrel{\mathop{\ordinarycolon}}=\frac{\alpha(\alpha+1)}{\kappa+1-\alpha\big(\kappa-\hat{\kappa}-1\big)}.
Then, for m∈{1,…,N}m\in\{1,\dots,N\},

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (C.7) |  | ∑i=1mνi\displaystyle\sum\_{i=1}^{m}\nu\_{i} | =∑σ∈{+,−}dσ​(mσ−α2​κ)mσ−α​κ​[mσ]N\displaystyle=\sum\_{\sigma\in\{+,-\}}\frac{d\_{\sigma}\big(m\_{\sigma}-\alpha^{2}\kappa\big)}{m\_{\sigma}-\alpha\kappa}\big[m\_{\sigma}\big]^{N} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−α)​(m−1)​∑σ∈{+,−}cσ​dσ​(α​(κ−κ^)mσ−α​(κ−κ^)+mσmσ−α​κ)​[mσ]N\displaystyle\quad+(1-\alpha)(m-1)\sum\_{\sigma\in\{+,-\}}c\_{\sigma}d\_{\sigma}\left(\frac{\alpha\big(\kappa-\hat{\kappa}\big)}{m\_{\sigma}-\alpha\big(\kappa-\hat{\kappa}\big)}+\frac{m\_{\sigma}}{m\_{\sigma}-\alpha\kappa}\right)\big[m\_{\sigma}\big]^{N} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +C1​(1+∑σ∈{+,−}cσ​mσ​((mσα​κ)m−1−1)mσ−α​κ)​αN​[κ]N\displaystyle\quad+C\_{1}\left(1+\sum\_{\sigma\in\{+,-\}}\frac{c\_{\sigma}m\_{\sigma}\Big(\big(\frac{m\_{\sigma}}{\alpha\kappa}\big)^{m-1}-1\Big)}{m\_{\sigma}-\alpha\kappa}\right)\alpha^{N}[\kappa]^{N} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +n​C1​∑σ∈{+,−}dσ​mσ​(α​(κ−κ^)mσ−(α​(κ−κ^)mσ)m)mσ−α​(κ−κ^)​[mσ]N,\displaystyle\quad+nC\_{1}\sum\_{\sigma\in\{+,-\}}\frac{d\_{\sigma}m\_{\sigma}\left(\frac{\alpha(\kappa-\hat{\kappa})}{m\_{\sigma}}-\big(\tfrac{\alpha(\kappa-\hat{\kappa})}{m\_{\sigma}}\big)^{m}\right)}{m\_{\sigma}-\alpha(\kappa-\hat{\kappa})}\big[m\_{\sigma}\big]^{N}, |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
| (C.8) |  | νN+1=∑σ∈{+,−}cσ​(mσ−α2​(κ−κ^))mσ−α​(κ−κ^)​[mσ]N+n​C1​αN​[κ−κ^]N.\nu\_{N+1}=\sum\_{\sigma\in\{+,-\}}\frac{c\_{\sigma}\big(m\_{\sigma}-\alpha^{2}(\kappa-\hat{\kappa})\big)}{m\_{\sigma}-\alpha(\kappa-\hat{\kappa})}\big[m\_{\sigma}\big]^{N}+nC\_{1}\alpha^{N}[\kappa-\hat{\kappa}]^{N}. |  |

###### Proof.

For i∈{3,…,N}i\in\{3,\dots,N\} we have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (C.9) |  | ∑j=2i−1(α​(κ−κ^))i−j​δj−1​ϕi+1\displaystyle\sum\_{j=2}^{i-1}(\alpha(\kappa-\hat{\kappa}))^{i-j}\delta\_{j-1}\phi\_{i+1} | =α(κ−κ^)(∑σ∈{+,−}cσ​dσmσ−α​(κ−κ^)mσN\displaystyle=\alpha(\kappa-\hat{\kappa})\Bigg(\sum\_{\sigma\in\{+,-\}}\frac{c\_{\sigma}d\_{\sigma}}{m\_{\sigma}-\alpha(\kappa-\hat{\kappa})}m\_{\sigma}^{N} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +c+​d−​m−N+1m+​(m+−α​(κ−κ^))​(m+m−)i+c−​d+​m+N+1m−​(m−−α​(κ−κ^))​(m−m+)i\displaystyle\hskip 59.75095pt+\frac{c\_{+}d\_{-}m\_{-}^{N+1}}{m\_{+}(m\_{+}-\alpha(\kappa-\hat{\kappa}))}\left(\frac{m\_{+}}{m\_{-}}\right)^{i}+\frac{c\_{-}d\_{+}m\_{+}^{N+1}}{m\_{-}(m\_{-}-\alpha(\kappa-\hat{\kappa}))}\left(\frac{m\_{-}}{m\_{+}}\right)^{i} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∑σ∈{+,−}cσ​mσmσ−α​(κ−κ^)∑τ∈{+,−}dτ​mτN+1(α​(κ−κ^))2(α​(κ−κ^)mτ)i)\displaystyle\hskip 59.75095pt-\sum\_{\sigma\in\{+,-\}}\frac{c\_{\sigma}m\_{\sigma}}{m\_{\sigma}-\alpha(\kappa-\hat{\kappa})}\sum\_{\tau\in\{+,-\}}\frac{d\_{\tau}m\_{\tau}^{N+1}}{(\alpha(\kappa-\hat{\kappa}))^{2}}\left(\frac{\alpha(\kappa-\hat{\kappa})}{m\_{\tau}}\right)^{i}\Bigg) |  |

and

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (C.10) |  | ∑j=iN(α​κ)j−i​δi−1​ϕj+1\displaystyle\sum\_{j=i}^{N}(\alpha\kappa)^{j-i}\delta\_{i-1}\phi\_{j+1} | =∑σ∈{+,−}cσ​dσmσ−α​κ​mσN+1+c+​d−​m−N+2m+​(m−−α​κ)​(m+m−)i+c−​d+​m+N+2m−​(m+−α​κ)​(m−m+)i\displaystyle=\sum\_{\sigma\in\{+,-\}}\frac{c\_{\sigma}d\_{\sigma}}{m\_{\sigma}-\alpha\kappa}m\_{\sigma}^{N+1}+\frac{c\_{+}d\_{-}m\_{-}^{N+2}}{m\_{+}\big(m\_{-}-\alpha\kappa\big)}\left(\frac{m\_{+}}{m\_{-}}\right)^{i}+\frac{c\_{-}d\_{+}m\_{+}^{N+2}}{m\_{-}\big(m\_{+}-\alpha\kappa\big)}\left(\frac{m\_{-}}{m\_{+}}\right)^{i} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∑σ∈{+,−}dσ​mσmσ−α​κ​∑τ∈{+,−}cτ​(α​κ)N+1mτ​(mτα​κ)i.\displaystyle\quad-\sum\_{\sigma\in\{+,-\}}\frac{d\_{\sigma}m\_{\sigma}}{m\_{\sigma}-\alpha\kappa}\sum\_{\tau\in\{+,-\}}\frac{c\_{\tau}(\alpha\kappa)^{N+1}}{m\_{\tau}}\left(\frac{m\_{\tau}}{\alpha\kappa}\right)^{i}. |  |

Using

|  |  |  |
| --- | --- | --- |
|  | α​(κ−κ^)​(m−−α​κ)+m−​(m+−α​(κ−κ^))=α​(κ−κ^)​(m+−α​κ)+m+​(m−−α​(κ−κ^))=m+​m−−α2​κ​(κ−κ^)=0,\alpha(\kappa-\hat{\kappa})(m\_{-}-\alpha\kappa)+m\_{-}\big(m\_{+}-\alpha(\kappa-\hat{\kappa})\big)=\alpha(\kappa-\hat{\kappa})(m\_{+}-\alpha\kappa)+m\_{+}\big(m\_{-}-\alpha(\kappa-\hat{\kappa})\big)=m\_{+}m\_{-}-\alpha^{2}\kappa(\kappa-\hat{\kappa})=0, |  |

the second and third terms in ([C.9](https://arxiv.org/html/2512.11765v1#A3.E9 "In C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) and ([C.10](https://arxiv.org/html/2512.11765v1#A3.E10 "In C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) cancel. After simplification we obtain, for i∈{2,…,N}i\in\{2,\dots,N\},

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (C.11) |  | νi\displaystyle\nu\_{i} | =(1−α)​∑σ∈{+,−}cσ​dσ​(α​(κ−κ^)mσ−α​(κ−κ^)+mσmσ−α​κ)​[mσ]N\displaystyle=(1-\alpha)\sum\_{\sigma\in\{+,-\}}c\_{\sigma}d\_{\sigma}\left(\frac{\alpha(\kappa-\hat{\kappa})}{m\_{\sigma}-\alpha(\kappa-\hat{\kappa})}+\frac{m\_{\sigma}}{m\_{\sigma}-\alpha\kappa}\right)[m\_{\sigma}]^{N} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +n​C1​∑σ∈{+,−}dσ​mσα​(κ−κ^)​[mσ]N​(α​(κ−κ^)mσ)i+C1​∑σ∈{+,−}cσ​αN+1​κmσ​[κ]N​(mσα​κ)i.\displaystyle\quad+nC\_{1}\sum\_{\sigma\in\{+,-\}}\frac{d\_{\sigma}m\_{\sigma}}{\alpha(\kappa-\hat{\kappa})}[m\_{\sigma}]^{N}\left(\frac{\alpha(\kappa-\hat{\kappa})}{m\_{\sigma}}\right)^{i}+C\_{1}\sum\_{\sigma\in\{+,-\}}\frac{c\_{\sigma}\alpha^{N+1}\kappa}{m\_{\sigma}}[\kappa]^{N}\left(\frac{m\_{\sigma}}{\alpha\kappa}\right)^{i}. |  |

Similar computations give

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (C.12) |  | ν1\displaystyle\nu\_{1} | =∑σ∈{+,−}dσ​(mσ−α2​κ)mσ−α​κ​[mσ]N+C1​αN​[κ]N,\displaystyle=\sum\_{\sigma\in\{+,-\}}\frac{d\_{\sigma}(m\_{\sigma}-\alpha^{2}\kappa)}{m\_{\sigma}-\alpha\kappa}[m\_{\sigma}]^{N}+C\_{1}\alpha^{N}[\kappa]^{N}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (C.13) |  | νN+1\displaystyle\nu\_{N+1} | =∑σ∈{+,−}cσ​(mσ−α2​(κ−κ^))mσ−α​(κ−κ^)​[mσ]N+n​C1​αN​[κ−κ^]N.\displaystyle=\sum\_{\sigma\in\{+,-\}}\frac{c\_{\sigma}(m\_{\sigma}-\alpha^{2}(\kappa-\hat{\kappa}))}{m\_{\sigma}-\alpha(\kappa-\hat{\kappa})}[m\_{\sigma}]^{N}+nC\_{1}\alpha^{N}[\kappa-\hat{\kappa}]^{N}. |  |

Finally, for m∈{2,…,N}m\in\{2,\dots,N\},

|  |  |  |
| --- | --- | --- |
|  | ∑i=2m∑σ∈{+,−}dσ​mσα​(κ−κ^)​[mσ]N​(α​(κ−κ^)mσ)i=∑σ∈{+,−}dσ​mσ​((mσα​(κ−κ^))N−1−(mσα​(κ−κ^))N−m)mσ−α​(κ−κ^)​αN​[κ−κ^]N,\sum\_{i=2}^{m}\sum\_{\sigma\in\{+,-\}}\frac{d\_{\sigma}m\_{\sigma}}{\alpha(\kappa-\hat{\kappa})}[m\_{\sigma}]^{N}\left(\frac{\alpha(\kappa-\hat{\kappa})}{m\_{\sigma}}\right)^{i}=\sum\_{\sigma\in\{+,-\}}\frac{d\_{\sigma}m\_{\sigma}\Big(\big(\frac{m\_{\sigma}}{\alpha(\kappa-\hat{\kappa})}\big)^{N-1}-\big(\frac{m\_{\sigma}}{\alpha(\kappa-\hat{\kappa})}\big)^{N-m}\Big)}{m\_{\sigma}-\alpha(\kappa-\hat{\kappa})}\alpha^{N}[\kappa-\hat{\kappa}]^{N}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | ∑i=2m∑σ∈{+,−}cσ​αN+1​κmσ​[κ]N​(mσα​κ)i=∑σ∈{+,−}cσ​mσ​((mσα​κ)m−1−1)mσ−α​κ​αN​[κ]N,\sum\_{i=2}^{m}\sum\_{\sigma\in\{+,-\}}\frac{c\_{\sigma}\alpha^{N+1}\kappa}{m\_{\sigma}}[\kappa]^{N}\left(\frac{m\_{\sigma}}{\alpha\kappa}\right)^{i}=\sum\_{\sigma\in\{+,-\}}\frac{c\_{\sigma}m\_{\sigma}\Big(\big(\frac{m\_{\sigma}}{\alpha\kappa}\big)^{m-1}-1\Big)}{m\_{\sigma}-\alpha\kappa}\alpha^{N}[\kappa]^{N}, |  |

which, together with ([C.11](https://arxiv.org/html/2512.11765v1#A3.E11 "In C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")), ([C.12](https://arxiv.org/html/2512.11765v1#A3.E12 "In C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")), and ([C.13](https://arxiv.org/html/2512.11765v1#A3.E13 "In C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")), proves the claim.
∎

The next lemma collects the limiting behavior of all quantities that appear in the derivation of the limiting strategy and, subsequently, the limiting costs. In addition, for the case θ>0\theta>0 (equivalently, κ>κ^/2\kappa>\hat{\kappa}/2) we record first or second-order Taylor expansions used to compute the pointwise convergence rate of the strategies.

For a sequence (aN)N∈ℕ\left({a\_{N}}\right)\_{N\in\mathbb{N}} and a real number aa, we use the shorthand

|  |  |  |
| --- | --- | --- |
|  | (aN)nt→±a:⟺(aN)nt=(−1)nt|aN|nt and limN→∞|aN|nt=a.({a\_{N}})^{n\_{t}}\to\pm a\quad\mathrel{\mathop{\ordinarycolon}}\Longleftrightarrow\quad({a\_{N}})^{n\_{t}}=({-1})^{n\_{t}}\lvert a\_{N}\rvert^{n\_{t}}\ \text{ and }\ \lim\_{N\to\infty}\lvert a\_{N}\rvert^{n\_{t}}=a. |  |

Recall that Δ=(1−α)\Delta=({1-\alpha}) and note that Δ→0\Delta\to 0 as N→∞N\to\infty. When convenient, we express expansions in the variable Δ\Delta; see also the discussion at the beginning of Appendix [C](https://arxiv.org/html/2512.11765v1#A3 "Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact").

###### Lemma C.5.

For κ>κ^2\kappa>\frac{\hat{\kappa}}{2} and κ≠κ^\kappa\neq\hat{\kappa}, we have the following Taylor expansions as N↑∞N\uparrow\infty.

1. (a)\mathrm{(a)}

   |  |  |  |
   | --- | --- | --- |
   |  | α=1−ρ​TN+ρ2​T22​N2+o​(1N2),αnt=e−ρ​TN​(N​tT+ηtN)=e−ρ​t​(1−ρ​T​ηtNN+(ρ​T​ηtN)22​N2)+o​(1N2).\displaystyle\hskip 34.99677pt\begin{aligned} &\alpha&&=1-\frac{\rho T}{N}+\frac{\rho^{2}T^{2}}{2N^{2}}+o\left(\frac{1}{N^{2}}\right),\\ &\alpha^{n\_{t}}&&=e^{-\frac{\rho T}{N}\left(\frac{Nt}{T}+\eta^{N}\_{t}\right)}=e^{-\rho t}\left(1-\frac{\rho T\eta^{N}\_{t}}{N}+\frac{(\rho T\eta^{N}\_{t})^{2}}{2N^{2}}\right)+o\left(\frac{1}{N^{2}}\right).\end{aligned} |  |
2. (b)\mathrm{(b)}

   |  |  |  |
   | --- | --- | --- |
   |  | R=κ^+Δ​2​(κ​n+1κ^−n)+Δ2​2​κ2+3​n2−5​κ​n−κ−n−2​(κ​n+1κ^−n)2κ^+o​(Δ2),c+=Δ​2​κ​nκ^2−Δ2​κ​n​4​κ​n+8​κ−3​n2−2​n+5κ^4+o​(Δ2),c−=1−Δ​2​κ​nκ^2+Δ2​κ​n​4​κ​n+8​κ−3​n2−2​n+5κ^4+o​(Δ2),d+=1−Δ​2κ^2​(κ−κ^)+Δ2​3​κ^3−11​κ^2​κ+4​κ^2+8​κ^​κ2−16​κ^​κ+12​κ2κ^4+o​(Δ2),d−=Δ​2κ^2​(κ−κ^)+Δ2​−3​κ^3+11​κ^2​κ−4​κ^2−8​κ^​κ2+16​κ^​κ−12​κ2κ^4+o​(Δ2),m+=κ+Δ​2​κκ^+Δ2​κ​3​κ^2−4​κ^​κ+4​κ^−4​κκ^3+o​(Δ2),m−=κ−κ^+Δ​2​n​(κ^−κ)κ^+Δ2​n​−κ^3+4​κ2+κ​n2−6​κ​n+5​κκ^3+o​(Δ2).\displaystyle\hskip 34.99677pt\begin{aligned} &R&&=\hat{\kappa}+\Delta 2\left({\kappa\frac{n+1}{\hat{\kappa}}-n}\right)+\Delta^{2}\frac{2\kappa^{2}+3n^{2}-5\kappa n-\kappa-n-2({\kappa\frac{n+1}{\hat{\kappa}}-n})^{2}}{\hat{\kappa}}+o({\Delta^{2}}),\\ &c\_{+}&&=\Delta\frac{2\kappa n}{\hat{\kappa}^{2}}-\Delta^{2}\kappa n\frac{4\kappa n+8\kappa-3n^{2}-2n+5}{\hat{\kappa}^{4}}+o({\Delta^{2}}),\\ &c\_{-}&&=1-\Delta\frac{2\kappa n}{\hat{\kappa}^{2}}+\Delta^{2}\kappa n\frac{4\kappa n+8\kappa-3n^{2}-2n+5}{\hat{\kappa}^{4}}+o({\Delta^{2}}),\\ &d\_{+}&&=1-\Delta\frac{2}{\hat{\kappa}^{2}}({\kappa-\hat{\kappa}})+\Delta^{2}\frac{3\hat{\kappa}^{3}-11\hat{\kappa}^{2}\kappa+4\hat{\kappa}^{2}+8\hat{\kappa}\kappa^{2}-16\hat{\kappa}\kappa+12\kappa^{2}}{\hat{\kappa}^{4}}+o({\Delta^{2}}),\\ &d\_{-}&&=\Delta\frac{2}{\hat{\kappa}^{2}}({\kappa-\hat{\kappa}})+\Delta^{2}\frac{-3\hat{\kappa}^{3}+11\hat{\kappa}^{2}\kappa-4\hat{\kappa}^{2}-8\hat{\kappa}\kappa^{2}+16\hat{\kappa}\kappa-12\kappa^{2}}{\hat{\kappa}^{4}}+o({\Delta^{2}}),\\ &m\_{+}&&=\kappa+\Delta\frac{2\kappa}{\hat{\kappa}}+\Delta^{2}\kappa\frac{3\hat{\kappa}^{2}-4\hat{\kappa}\kappa+4\hat{\kappa}-4\kappa}{\hat{\kappa}^{3}}+o({\Delta^{2}}),\\ &m\_{-}&&=\kappa-\hat{\kappa}+\Delta\frac{2n({\hat{\kappa}-\kappa})}{\hat{\kappa}}+\Delta^{2}n\frac{-\hat{\kappa}^{3}+4\kappa^{2}+\kappa n^{2}-6\kappa n+5\kappa}{\hat{\kappa}^{3}}+o({\Delta^{2}}).\end{aligned} |  |
3. (c)\mathrm{(c)}

   |  |  |  |
   | --- | --- | --- |
   |  | c+m+−κ=nκ^+Δ​2​n​(κ^−2​κ)κ^3+o​(Δ),c+m+−α​κ=2​nκ^​(n+1)+Δ​n​−4​κ​n2−4​κ​n−8​κ+3​n3−n2+n−3(n+1)2​κ^3+o​(Δ),c+m+−α2​κ=1n−1+Δ​−2​κ−n​(2​κ−κ^)+n+κ^2−1κ^3+o​(Δ),c+1−α2=κ​nκ^2−Δ​2​κ​n​κ​n+2​κ−n2+1κ^4+o​(Δ).\displaystyle\hskip 34.99677pt\begin{aligned} &\frac{c\_{+}}{m\_{+}-\kappa}&&=\frac{n}{\hat{\kappa}}+\Delta\frac{2n({\hat{\kappa}-2\kappa})}{\hat{\kappa}^{3}}+o({\Delta}),\\ &\frac{c\_{+}}{m\_{+}-\alpha\kappa}&&=\frac{2n}{\hat{\kappa}({n+1})}+\Delta n\frac{-4\kappa n^{2}-4\kappa n-8\kappa+3n^{3}-n^{2}+n-3}{({n+1})^{2}\hat{\kappa}^{3}}+o({\Delta}),\\ &\frac{c\_{+}}{m\_{+}-\alpha^{2}\kappa}&&=\frac{1}{n-1}+\Delta\frac{-2\kappa-n(2\kappa-\hat{\kappa})+n+\hat{\kappa}^{2}-1}{\hat{\kappa}^{3}}+o({\Delta}),\\ &\frac{c\_{+}}{1-\alpha^{2}}&&=\frac{\kappa n}{\hat{\kappa}^{2}}-\Delta 2\kappa n\frac{\kappa n+2\kappa-n^{2}+1}{\hat{\kappa}^{4}}+o({\Delta}).\end{aligned} |  |
4. (d)\mathrm{(d)}

   |  |  |  |
   | --- | --- | --- |
   |  | d−m−−(κ−κ^)=−1n​κ^+Δ​8​θ(n−1)3+o​(Δ),d−m−−α​(κ−κ^)=−2(n+1)​κ^+Δ​8​κ​n2+4​κ​n+4​κ−5​n3+3​n2+n+1κ^3​(n+1)2+o​(Δ),d−m−−α2​(κ−κ^)=−1κ^+Δ​2​κ+n​(2​κ−κ^)−n−κ^2+1κ^3+o​(Δ),d−1−α2=κ−κ^κ^2+Δ​2​−κ^3+3​κ^2​κ−κ^2−2​κ^​κ2+4​κ^​κ−3​κ2κ^4+o​(Δ).\displaystyle\hskip 34.99677pt\begin{aligned} &\frac{d\_{-}}{m\_{-}-({\kappa-\hat{\kappa}})}&&=-\frac{1}{n\hat{\kappa}}+\Delta\frac{8\theta}{({n-1})^{3}}+o({\Delta}),\\ &\frac{d\_{-}}{m\_{-}-\alpha({\kappa-\hat{\kappa}})}&&=-\frac{2}{(n+1)\hat{\kappa}}+\Delta\frac{8\kappa n^{2}+4\kappa n+4\kappa-5n^{3}+3n^{2}+n+1}{\hat{\kappa}^{3}(n+1)^{2}}+o({\Delta}),\\ &\frac{d\_{-}}{m\_{-}-\alpha^{2}(\kappa-\hat{\kappa})}&&=-\frac{1}{\hat{\kappa}}+\Delta\frac{2\kappa+n(2\kappa-\hat{\kappa})-n-\hat{\kappa}^{2}+1}{\hat{\kappa}^{3}}+o({\Delta}),\\ &\frac{d\_{-}}{1-\alpha^{2}}&&=\frac{\kappa-\hat{\kappa}}{\hat{\kappa}^{2}}+\Delta 2\frac{-\hat{\kappa}^{3}+3\hat{\kappa}^{2}\kappa-\hat{\kappa}^{2}-2\hat{\kappa}\kappa^{2}+4\hat{\kappa}\kappa-3\kappa^{2}}{\hat{\kappa}^{4}}+o({\Delta}).\end{aligned} |  |

Fix t∈(0,T]t\in(0,T] and recall ηTN=0\eta\_{T}^{N}=0 for all N∈ℕN\in\mathbb{N}. If κ>κ^/2\kappa>\hat{\kappa}/2, the following expansions hold.

1. (e)\mathrm{(e)}

   |  |  |  |
   | --- | --- | --- |
   |  | (1−α)​nt=ρ​t+ρ​TN​(ηtN−ρ​t2)+o​(1N).\displaystyle\hskip 34.99677pt\begin{aligned} (1-\alpha)n\_{t}=\rho t+\frac{\rho T}{N}\left({\eta^{N}\_{t}-\frac{\rho t}{2}}\right)+o\left({\frac{1}{N}}\right).\end{aligned} |  |
2. (f)\mathrm{(f)}

   |  |  |  |
   | --- | --- | --- |
   |  | (κ−κ^κ)nt=o​(1N)and more generally(κ−κ^κ)nt=o​(1Np),∀p∈ℕ,(m+κ)nt=exp⁡(2​ρ​tn−1)​(1+ρ​TN​(−ρ​t​8​n​θ(n−1)3+2n−1​ηtN))+o​(1N),(κ−κ^m+)nt=o​(1N)and more generally(κ−κ^m+)nt=o​(1Np),∀p∈ℕ,(m−κ)nt=o​(1N)and more generally(m−κ)nt=o​(1Np),∀p∈ℕ,(κ−κ^m−)nt=exp⁡(2​n​ρ​tn−1)​(1+ρ​T​nN​(−ρ​t​8​θ(n−1)3+2n−1​ηtN))+o​(1N).\displaystyle\hskip 34.99677pt\begin{aligned} &\left({\frac{\kappa-\hat{\kappa}}{\kappa}}\right)^{n\_{t}}&&=o\left({\frac{1}{N}}\right)\quad\text{and more generally}\quad\left({\frac{\kappa-\hat{\kappa}}{\kappa}}\right)^{n\_{t}}=o\left({\frac{1}{N^{p}}}\right),\ \forall p\in\mathbb{N},\\ &\left({\frac{m\_{+}}{\kappa}}\right)^{n\_{t}}&&=\exp\left({\frac{2\rho t}{n-1}}\right)\left({1+\frac{\rho T}{N}\left({-\rho t\frac{8n\theta}{(n-1)^{3}}+\frac{2}{n-1}\eta^{N}\_{t}}\right)}\right)+o\left({\frac{1}{N}}\right),\\ &\left({\frac{\kappa-\hat{\kappa}}{m\_{+}}}\right)^{n\_{t}}&&=o\left({\frac{1}{N}}\right)\quad\text{and more generally}\quad\left({\frac{\kappa-\hat{\kappa}}{m\_{+}}}\right)^{n\_{t}}=o\left({\frac{1}{N^{p}}}\right),\ \forall p\in\mathbb{N},\\ &\left({\frac{m\_{-}}{\kappa}}\right)^{n\_{t}}&&=o\left({\frac{1}{N}}\right)\quad\text{and more generally}\quad\left({\frac{m\_{-}}{\kappa}}\right)^{n\_{t}}=o\left({\frac{1}{N^{p}}}\right),\ \forall p\in\mathbb{N},\\ &\left({\frac{\kappa-\hat{\kappa}}{m\_{-}}}\right)^{n\_{t}}&&=\exp\left({\frac{2n\rho t}{n-1}}\right)\left({1+\frac{\rho Tn}{N}\left({-\rho t\frac{8\theta}{(n-1)^{3}}+\frac{2}{n-1}\eta^{N}\_{t}}\right)}\right)+o\left({\frac{1}{N}}\right).\end{aligned} |  |
3. (g)\mathrm{(g)}

   |  |  |  |
   | --- | --- | --- |
   |  | [m+]N=κ^2​κ​n​(1+Δ​κ^2−8​κ^+8​κ2​κ^2)+o​(Δ),[m−]N=o​(1N)and more generally[m−]N=o​(1Np),∀p∈ℕ,[κ]N=exp⁡(−2​ρ​Tκ^)​κ^2​κ​n​(1+ρ​TN​(ρ​T​8​n​θκ^3+κ^2−8​κ^+8​κ2​κ^2))+o​(1N),[κ−κ^]N=o​(1N)and more generally[κ−κ^]N=o​(1Np),∀p∈ℕ.\displaystyle\hskip 34.99677pt\begin{aligned} &\left[{m\_{+}}\right]^{N}&&=\frac{\hat{\kappa}}{2\kappa n}\left(1+\Delta\frac{\hat{\kappa}^{2}-8\hat{\kappa}+8\kappa}{2\hat{\kappa}^{2}}\right)+o\left({\Delta}\right),\\ &[m\_{-}]^{N}&&=o\left({\frac{1}{N}}\right)\quad\text{and more generally}\quad[m\_{-}]^{N}=o\left({\frac{1}{N^{p}}}\right),\ \forall p\in\mathbb{N},\\ &\left[{\kappa}\right]^{N}&&=\exp\left({\frac{-2\rho T}{\hat{\kappa}}}\right)\frac{\hat{\kappa}}{2\kappa n}\left(1+\frac{\rho T}{N}\left({\rho T\frac{8n\theta}{\hat{\kappa}^{3}}+\frac{\hat{\kappa}^{2}-8\hat{\kappa}+8\kappa}{2\hat{\kappa}^{2}}}\right)\right)+o\left({\frac{1}{N}}\right),\\ &[\kappa-\hat{\kappa}]^{N}&&=o\left({\frac{1}{N}}\right)\quad\text{and more generally}\quad[\kappa-\hat{\kappa}]^{N}=o\left({\frac{1}{N^{p}}}\right),\ \forall p\in\mathbb{N}.\end{aligned} |  |
4. (h)\mathrm{(h)}

   |  |  |  |
   | --- | --- | --- |
   |  | (κ−κ^κ)N1−α2=o​(1N)and more generally(κ−κ^κ)N1−α2=o​(1Np),∀p∈ℕ,[m−]N1−α2=o​(1N)and more generally[m−]N1−α2=o​(1Np),∀p∈ℕ,[κ−κ^]N1−α2=o​(1N)and more generally[κ−κ^]N1−α2=o​(1Np),∀p∈ℕ.\displaystyle\hskip 34.99677pt\begin{aligned} &\frac{\left({\frac{\kappa-\hat{\kappa}}{\kappa}}\right)^{N}}{1-\alpha^{2}}&&=o\left({\frac{1}{N}}\right)\quad\text{and more generally}\quad\frac{\left({\frac{\kappa-\hat{\kappa}}{\kappa}}\right)^{N}}{1-\alpha^{2}}=o\left({\frac{1}{N^{p}}}\right),\ \forall p\in\mathbb{N},\\ &\frac{[m\_{-}]^{N}}{1-\alpha^{2}}&&=o\left({\frac{1}{N}}\right)\quad\text{and more generally}\quad\frac{[m\_{-}]^{N}}{1-\alpha^{2}}=o\left({\frac{1}{N^{p}}}\right),\ \forall p\in\mathbb{N},\\ &\frac{[\kappa-\hat{\kappa}]^{N}}{1-\alpha^{2}}&&=o\left({\frac{1}{N}}\right)\quad\text{and more generally}\quad\frac{[\kappa-\hat{\kappa}]^{N}}{1-\alpha^{2}}=o\left({\frac{1}{N^{p}}}\right),\ \forall p\in\mathbb{N}.\end{aligned} |  |

If, on the other hand, κ=κ^/2\kappa=\hat{\kappa}/2, then the preceding limits no longer hold. Instead, we have:

1. (f’)

   (κ−κ^κ)nt→±1,(m+κ)nt→e2​ρ​tn−1,(κ−κ^m+)nt→±e−2​ρ​tn−1,(m−κ)nt→±e−2​n​ρ​tn−1\left(\frac{\kappa-\hat{\kappa}}{\kappa}\right)^{n\_{t}}\to{\pm 1},\quad\left(\frac{m\_{+}}{\kappa}\right)^{n\_{t}}\to e^{\frac{2\rho t}{n-1}},\quad\left(\frac{\kappa-\hat{\kappa}}{m\_{+}}\right)^{n\_{t}}\to{\pm e^{-\frac{2\rho t}{n-1}}},\quad\left(\frac{m\_{-}}{\kappa}\right)^{n\_{t}}\to{\pm e^{-\frac{2n\rho t}{n-1}}},
     
   and (κ−κ^m−)nt→e2​n​ρ​tn−1\left(\frac{\kappa-\hat{\kappa}}{m\_{-}}\right)^{n\_{t}}\to e^{\frac{2n\rho t}{n-1}};
2. (g’)

   [m+]2​N→1e−2​n+1n−1​ρ​T+n,[m−]2​N→1n​e2​n+1n−1​ρ​T+1,[κ]2​N→e2​n​ρ​Tn−1n​e2​n+1n−1​ρ​T+1,[κ−κ^]2​N→e2​n​ρ​Tn−1n​e2​n+1n−1​ρ​T+1[m\_{+}]^{2N}\to\frac{1}{e^{-2\frac{n+1}{n-1}\rho T}+n},\quad[m\_{-}]^{2N}\to\frac{1}{ne^{2\frac{n+1}{n-1}\rho T}+1},\quad[\kappa]^{2N}\to\frac{e^{\frac{2n\rho T}{n-1}}}{ne^{2\frac{n+1}{n-1}\rho T}+1},\quad[\kappa-\hat{\kappa}]^{2N}\to\frac{e^{\frac{2n\rho T}{n-1}}}{ne^{2\frac{n+1}{n-1}\rho T}+1},
     
   [m+]2​N+1→1−e−2​n+1n−1​ρ​T+n,[m−]2​N+1→1−n​e2​n+1n−1​ρ​T+1,[κ]2​N+1→e2​n​ρ​Tn−1n​e2​n+1n−1​ρ​T−1[m\_{+}]^{2N+1}\to\frac{1}{-e^{-2\frac{n+1}{n-1}\rho T}+n},\quad[m\_{-}]^{2N+1}\to\frac{1}{-ne^{2\frac{n+1}{n-1}\rho T}+1},\quad[\kappa]^{2N+1}\to\frac{e^{\frac{2n\rho T}{n-1}}}{ne^{2\frac{n+1}{n-1}\rho T}-1},
     
   and [κ−κ^]2​N+1→e2​n​ρ​Tn−1−n​e2​n+1n−1​ρ​T+1[\kappa-\hat{\kappa}]^{2N+1}\to\frac{e^{\frac{2n\rho T}{n-1}}}{-ne^{2\frac{n+1}{n-1}\rho T}+1};
3. (h’)

   m++κ−κ^m++α​(κ−κ^)→2n+1,m−+α2​κm−+α​κ→2n+1\frac{m\_{+}+\kappa-\hat{\kappa}}{m\_{+}+\alpha(\kappa-\hat{\kappa})}\to{\frac{2}{n+1}},\quad\frac{m\_{-}+\alpha^{2}\kappa}{m\_{-}+\alpha\kappa}\to{\frac{2}{n+1}}, and κ+α​(κ−κ^)1−α2→n−14\frac{\kappa+\alpha(\kappa-\hat{\kappa})}{1-\alpha^{2}}\to{\frac{n-1}{4}}.

###### Proof.

We start with [(b)\mathrm{(b)}](https://arxiv.org/html/2512.11765v1#A3.I2.i2 "item (b) ‣ Lemma C.5. ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"). Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | R\displaystyle R | =α4​(κ−n)2−2​α2​(κ​(κ+1)+n​(1−κ))+(κ+1)2\displaystyle=\sqrt{\alpha^{4}(\kappa-n)^{2}-2\alpha^{2}\big(\kappa(\kappa+1)+n(1-\kappa)\big)+(\kappa+1)^{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =κ^+Δ​2​(κ​n+1κ^−n)+Δ2​2​κ2+3​n2−5​κ​n−κ−n−2​(κ​n+1κ^−n)2κ^+o​(Δ2),\displaystyle=\hat{\kappa}+\Delta 2\left({\kappa\frac{n+1}{\hat{\kappa}}-n}\right)+\Delta^{2}\frac{2\kappa^{2}+3n^{2}-5\kappa n-\kappa-n-2({\kappa\frac{n+1}{\hat{\kappa}}-n})^{2}}{\hat{\kappa}}+o({\Delta^{2}}), |  |

for c+c\_{+}, set R=κ^+Δ​LR+Δ2​BR+o​(Δ2)R=\hat{\kappa}+\Delta L\_{R}+\Delta^{2}B\_{R}+o(\Delta^{2}) and compute

|  |  |  |  |
| --- | --- | --- | --- |
|  | c+\displaystyle c\_{+} | =1−(1−Δ)2​(κ+n)+κ+R2​R\displaystyle=\frac{1-(1-\Delta)^{2}(\kappa+n)+\kappa+R}{2R} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Δ​(2​(κ+n)+LR)+Δ2​(BR−(κ+n))+o​(Δ2)2​κ^​(1+Δ​LR/κ^+Δ2​BR/κ^+o​(Δ2))\displaystyle=\frac{\Delta(2(\kappa+n)+L\_{R})+\Delta^{2}(B\_{R}-(\kappa+n))+o(\Delta^{2})}{2\hat{\kappa}(1+\Delta L\_{R}/\hat{\kappa}+\Delta^{2}B\_{R}/\hat{\kappa}+o(\Delta^{2}))} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Δ​2​κ​nκ^2−Δ2​κ​n​4​κ​n+8​κ−3​n2−2​n+5κ^4+o​(Δ2).\displaystyle=\Delta\,\frac{2\kappa n}{\hat{\kappa}^{2}}-\Delta^{2}\,\kappa n\frac{4\kappa n+8\kappa-3n^{2}-2n+5}{\hat{\kappa}^{4}}+o(\Delta^{2}). |  |

Analogous expansions yield d±d\_{\pm} and m±m\_{\pm}.
For [(c)\mathrm{(c)}](https://arxiv.org/html/2512.11765v1#A3.I2.i3 "item (c) ‣ Lemma C.5. ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"), write

|  |  |  |
| --- | --- | --- |
|  | c+=Δ​Lc++Δ2​Bc++o​(Δ2),m+−κ=Δ​Lm++Δ2​Bm++o​(Δ2),c\_{+}=\Delta L\_{c\_{+}}+\Delta^{2}B\_{c\_{+}}+o(\Delta^{2}),\qquad m\_{+}-\kappa=\Delta L\_{m\_{+}}+\Delta^{2}B\_{m\_{+}}+o(\Delta^{2}), |  |

and compute

|  |  |  |  |
| --- | --- | --- | --- |
|  | c+m+−κ\displaystyle\frac{c\_{+}}{m\_{+}-\kappa} | =Lc++Δ​Bc++o​(Δ)Lm+​(1+Δ​Bm+/Lm++o​(Δ))=(nκ^+Δ​κ^2​κ​Bc++o​(Δ))​(1−Δ​κ^2​κ​Bm++o​(Δ))\displaystyle=\frac{L\_{c\_{+}}+\Delta B\_{c\_{+}}+o(\Delta)}{L\_{m\_{+}}(1+\Delta B\_{m\_{+}}/L\_{m\_{+}}+o(\Delta))}=\left(\frac{n}{\hat{\kappa}}+\Delta\frac{\hat{\kappa}}{2\kappa}B\_{c\_{+}}+o(\Delta)\right)\left(1-\Delta\frac{\hat{\kappa}}{2\kappa}B\_{m\_{+}}+o(\Delta)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =nκ^+Δ​(−n2​κ​Bm++κ^2​κ​Bc+)+o​(Δ)=nκ^+Δ​2​n​(κ^−2​κ)κ^3+o​(Δ).\displaystyle=\frac{n}{\hat{\kappa}}+\Delta\left(-\frac{n}{2\kappa}B\_{m\_{+}}+\frac{\hat{\kappa}}{2\kappa}B\_{c\_{+}}\right)+o(\Delta)=\frac{n}{\hat{\kappa}}+\Delta\frac{2n(\hat{\kappa}-2\kappa)}{\hat{\kappa}^{3}}+o(\Delta). |  |

The remaining ratios in
[(c)\mathrm{(c)}](https://arxiv.org/html/2512.11765v1#A3.I2.i3 "item (c) ‣ Lemma C.5. ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")–[(d)\mathrm{(d)}](https://arxiv.org/html/2512.11765v1#A3.I2.i4 "item (d) ‣ Lemma C.5. ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")
follow similarly. Item [(e)\mathrm{(e)}](https://arxiv.org/html/2512.11765v1#A3.I3.i5 "item (e) ‣ Lemma C.5. ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") and the limits in
[(f)\mathrm{(f)}](https://arxiv.org/html/2512.11765v1#A3.I3.i6 "item (f) ‣ Lemma C.5. ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") are obtained by the same ideas used in the proof of Theorem [4.1](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem1 "Theorem 4.1 (Convergence of strategies for 𝜃>0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")[(b)](https://arxiv.org/html/2512.11765v1#S4.I1.i2 "item (b) ‣ Theorem 4.1 (Convergence of strategies for 𝜃>0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact").
For [(g)\mathrm{(g)}](https://arxiv.org/html/2512.11765v1#A3.I3.i7 "item (g) ‣ Lemma C.5. ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"), note that

|  |  |  |
| --- | --- | --- |
|  | [m+]N=ΔδN+1​m+N=Δc+​(1−α2+κ−α2​κ​(κ−κ^)m+)+c−​(1−α2+κ−α2​κ​(κ−κ^)m−)​(m−m+)N.[m\_{+}]^{N}=\frac{\Delta}{\delta\_{N+1}}m\_{+}^{N}=\frac{\Delta}{c\_{+}\left(1-\alpha^{2}+\kappa-\frac{\alpha^{2}\kappa(\kappa-\hat{\kappa})}{m\_{+}}\right)+c\_{-}\left(1-\alpha^{2}+\kappa-\frac{\alpha^{2}\kappa(\kappa-\hat{\kappa})}{m\_{-}}\right)\left(\frac{m\_{-}}{m\_{+}}\right)^{N}}. |  |

Expanding the denominator in Δ\Delta and observing that the second term decays faster than any power of 1/N1/N, we only need the expansion of c+​(1−α2+κ−α2​κ​(κ−κ^)m+)c\_{+}\Big(1-\alpha^{2}+\kappa-\frac{\alpha^{2}\kappa({\kappa-\hat{\kappa}})}{m\_{+}}\Big).
Writing

|  |  |  |
| --- | --- | --- |
|  | c+=Δ​a1+Δ2​a2+o​(Δ2),m+=κ+Δ​b1+Δ2​b2+o​(Δ2),c\_{+}=\Delta a\_{1}+\Delta^{2}a\_{2}+o(\Delta^{2}),\qquad m\_{+}=\kappa+\Delta b\_{1}+\Delta^{2}b\_{2}+o(\Delta^{2}), |  |

we compute

|  |  |  |
| --- | --- | --- |
|  | c+​(1−α2+κ−α2​κ​(κ−κ^)m+)=Δ​(a1+Δ​a2+o​(Δ))​(κ^+Δ​((κ−κ^)​(b^+2)+2)+o​(Δ)),\displaystyle c\_{+}\left(1-\alpha^{2}+\kappa-\frac{\alpha^{2}\kappa(\kappa-\hat{\kappa})}{m\_{+}}\right)=\Delta(a\_{1}+\Delta a\_{2}+o(\Delta))\left(\hat{\kappa}+\Delta\big((\kappa-\hat{\kappa})(\hat{b}+2)+2\big)+o(\Delta)\right), |  |

where b^=b1/κ\hat{b}=b\_{1}/\kappa.
After some algebra, we arrive at

|  |  |  |
| --- | --- | --- |
|  | c+​(1−α2+κ−α2​κ​(κ−κ^)m+)=Δ​(2​κ​nκ^+Δ​κ​n​10​κ^−8​κ−n2+1κ^3+o​(Δ)),c\_{+}\left(1-\alpha^{2}+\kappa-\frac{\alpha^{2}\kappa(\kappa-\hat{\kappa})}{m\_{+}}\right)=\Delta\left(\frac{2\kappa n}{\hat{\kappa}}+\Delta\,\kappa n\,\frac{10\hat{\kappa}-8\kappa-n^{2}+1}{\hat{\kappa}^{3}}+o(\Delta)\right), |  |

thus

|  |  |  |  |
| --- | --- | --- | --- |
|  | [m+]N\displaystyle[m\_{+}]^{N} | =ΔΔ​(2​κ​nκ^+Δ​κ​n​10​κ^−8​κ−n2+1κ^3+o​(Δ))=κ^2​κ​n​(1+Δ​κ^2−8​κ^+8​κ2​κ^2+o​(Δ)).\displaystyle=\frac{\Delta}{\Delta\left(\frac{2\kappa n}{\hat{\kappa}}+\Delta\kappa n\,\frac{10\hat{\kappa}-8\kappa-n^{2}+1}{\hat{\kappa}^{3}}+o(\Delta)\right)}=\frac{\hat{\kappa}}{2\kappa n}\left(1+\Delta\,\frac{\hat{\kappa}^{2}-8\hat{\kappa}+8\kappa}{2\hat{\kappa}^{2}}+o(\Delta)\right). |  |

The remaining expansions in
[(g)\mathrm{(g)}](https://arxiv.org/html/2512.11765v1#A3.I3.i7 "item (g) ‣ Lemma C.5. ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")–[(h)\mathrm{(h)}](https://arxiv.org/html/2512.11765v1#A3.I3.i8 "item (h) ‣ Lemma C.5. ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") follow analogously.
Items [(f’)](https://arxiv.org/html/2512.11765v1#A3.I4.i6 "item (f’) ‣ Lemma C.5. ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")–[(h’)](https://arxiv.org/html/2512.11765v1#A3.I4.i8 "item (h’) ‣ Lemma C.5. ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") follow by L’Hôpital’s rule and straightforward algebra. ∎

###### Proof of Theorem [4.1](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem1 "Theorem 4.1 (Convergence of strategies for 𝜃>0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") [(a)](https://arxiv.org/html/2512.11765v1#S4.I1.i1 "item (a) ‣ Theorem 4.1 (Convergence of strategies for 𝜃>0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") for κ≠n−1\kappa\neq n-1.

Let κ>n−12\kappa>\frac{n-1}{2} with κ≠n−1\kappa\neq n-1. Starting from ([C.7](https://arxiv.org/html/2512.11765v1#A3.E7 "In Lemma C.4. ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"))–([C.8](https://arxiv.org/html/2512.11765v1#A3.E8 "In Lemma C.4. ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")), we expand each term using the asymptotics in Lemma [C.5](https://arxiv.org/html/2512.11765v1#A3.Thmtheorem5 "Lemma C.5. ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact").

*Step 1: Expansion of ∑i=1ntνi\sum\_{i=1}^{n\_{t}}\nu\_{i}.*

Let t∈(0,T]t\in(0,T] and consider ([C.7](https://arxiv.org/html/2512.11765v1#A3.E7 "In Lemma C.4. ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) with m=ntm=n\_{t}; we expand each of the four terms in ([C.7](https://arxiv.org/html/2512.11765v1#A3.E7 "In Lemma C.4. ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) as N↑∞N\uparrow\infty.

1. 1)

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | ∑σ∈{+,−}dσ​(mσ−α2​κ)mσ−α​κ​[mσ]N\displaystyle\sum\_{\sigma\in\{+,-\}}\frac{d\_{\sigma}(m\_{\sigma}-\alpha^{2}\kappa)}{m\_{\sigma}-\alpha\kappa}[m\_{\sigma}]^{N} | =n−1κ​(n+1)+1N​2​ρ​T​(−n2+8​n​θ+1)(n−1)​(n+1)2​(n−1+4​θ)⏟=⁣:𝒴(1)+o​(1N).\displaystyle=\frac{n-1}{\kappa(n+1)}+\frac{1}{N}\underbrace{\frac{2\rho T(-n^{2}+8n\theta+1)}{(n-1)(n+1)^{2}(n-1+4\theta)}}\_{=\mathrel{\mathop{\ordinarycolon}}\penalty 10000\ \mathscr{Y}^{(1)}}+o\left(\frac{1}{N}\right). |  |
2. 2)

   |  |  |  |
   | --- | --- | --- |
   |  | (1−α)​(nt−1)​∑σ∈{+,−}cσ​dσ​(α​(κ−κ^)mσ−α​(κ−κ^)+mσmσ−α​κ)​[mσ]N=ρ​tn+1+1N​ρ​Tn+1​(ηtN−1−ρ​t2+ρ​t​(n−4​θ+1)2​(n+1))⏟=⁣:𝒴N(2)​(t)+o​(1N).(1-\alpha)(n\_{t}-1)\sum\_{\sigma\in\{+,-\}}c\_{\sigma}d\_{\sigma}\left(\frac{\alpha(\kappa-\hat{\kappa})}{m\_{\sigma}-\alpha(\kappa-\hat{\kappa})}+\frac{m\_{\sigma}}{m\_{\sigma}-\alpha\kappa}\right)[m\_{\sigma}]^{N}\\ =\frac{\rho t}{n+1}+\frac{1}{N}\underbrace{\frac{\rho T}{n+1}\left(\eta\_{t}^{N}-1-\frac{\rho t}{2}+\frac{\rho t(n-4\theta+1)}{2(n+1)}\right)}\_{=\mathrel{\mathop{\ordinarycolon}}\penalty 10000\ \mathscr{Y}\_{N}^{(2)}(t)}+o\left(\frac{1}{N}\right). |  |
3. 3)

   |  |  |  |
   | --- | --- | --- |
   |  | C1​(1+∑σ∈{+,−}cσ​mσ​((mσ/(α​κ))nt−1−1)mσ−α​κ)​αN​[κ]N=e−ρ​n+1n−1​Tn​(n+1)2​(−(n−1)+2​n​eρ​n+1n−1​t)+𝒴N(3)​(t)N+o​(1N),C\_{1}\left(1+\sum\_{\sigma\in\{+,-\}}\frac{c\_{\sigma}m\_{\sigma}((m\_{\sigma}/(\alpha\kappa))^{n\_{t}-1}-1)}{m\_{\sigma}-\alpha\kappa}\right)\alpha^{N}[\kappa]^{N}\\ =\frac{e^{-\rho\frac{n+1}{n-1}T}}{n(n+1)^{2}}(-(n-1)+2ne^{\rho\frac{n+1}{n-1}t})+\frac{\mathscr{Y}\_{N}^{(3)}(t)}{N}+o\left(\frac{1}{N}\right), |  |

   where

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | 𝒴N(3)​(t)\displaystyle\mathscr{Y}\_{N}^{(3)}(t) | =e−ρ​T​n+1n−1​(c(0)+cN(1)​(t)​eρ​t​n+1n−1),\displaystyle=e^{-\rho T\frac{n+1}{n-1}}(c^{(0)}+c\_{N}^{(1)}(t)e^{\rho t\frac{n+1}{n-1}}), |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | c(0)\displaystyle c^{(0)} | =ρ​Tn​(n−1)2​(n+1)3​(−8​T​n2​ρ​θ−8​T​n​ρ​θ+n4+4​n3​θ−20​n2​θ−2​n2+12​n​θ+4​θ+1),\displaystyle=\frac{\rho T}{n(n-1)^{2}(n+1)^{3}}(-8Tn^{2}\rho\theta-8Tn\rho\theta+n^{4}+4n^{3}\theta-20n^{2}\theta-2n^{2}+12n\theta+4\theta+1), |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | cN(1)​(t)\displaystyle c\_{N}^{(1)}(t) | =2​ρ​T(n−1)3​(n+1)3(ηtN(n4−2n2+1)−8ρt(n2θ+nθ)+8Tρn2θ+8Tρnθ−n4−6n3θ\displaystyle=\frac{2\rho T}{(n-1)^{3}(n+1)^{3}}(\eta\_{t}^{N}(n^{4}-2n^{2}+1)-8\rho t(n^{2}\theta+n\theta)+8T\rho n^{2}\theta+8T\rho n\theta-n^{4}-6n^{3}\theta |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | +14n2θ+2n2−10nθ+2θ−1).\displaystyle\hskip 110.00017pt+14n^{2}\theta+2n^{2}-10n\theta+2\theta-1). |  |
4. 4)

   |  |  |  |
   | --- | --- | --- |
   |  | n​C1​∑σ∈{+,−}dσ​mσ​(α​(κ−κ^)mσ−(α​(κ−κ^)mσ)nt)mσ−α​(κ−κ^)​[mσ]N=κ−κ^κ​(n+1)+1N​ρ​T​(n−4​θ−1)​(n2+4​n​θ+2​n+1)(n−1)​(n+1)2​(n+4​θ−1)⏟=⁣:𝒴(4)+o​(1N).nC\_{1}\sum\_{\sigma\in\{+,-\}}\frac{d\_{\sigma}m\_{\sigma}\left(\frac{\alpha(\kappa-\hat{\kappa})}{m\_{\sigma}}-\bigl(\frac{\alpha(\kappa-\hat{\kappa})}{m\_{\sigma}}\bigr)^{n\_{t}}\right)}{m\_{\sigma}-\alpha(\kappa-\hat{\kappa})}[m\_{\sigma}]^{N}\\ =\frac{\kappa-\hat{\kappa}}{\kappa(n+1)}+\frac{1}{N}\underbrace{\frac{\rho T(n-4\theta-1)(n^{2}+4n\theta+2n+1)}{(n-1)(n+1)^{2}(n+4\theta-1)}}\_{=\mathrel{\mathop{\ordinarycolon}}\penalty 10000\ \mathscr{Y}^{(4)}}+o\left(\frac{1}{N}\right). |  |

Collecting the first-order coefficients of [1)](https://arxiv.org/html/2512.11765v1#A3.I5.i1 "item 1) ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"), [2)](https://arxiv.org/html/2512.11765v1#A3.I5.i2 "item 2) ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"), and [4)](https://arxiv.org/html/2512.11765v1#A3.I5.i4 "item 4) ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"), set

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒴N​(t)\displaystyle\mathscr{Y}\_{N}(t) | :=𝒴(1)+𝒴N(2)(t)+𝒴(4)\displaystyle\mathrel{\mathop{\ordinarycolon}}=\mathscr{Y}^{(1)}+\mathscr{Y}\_{N}^{(2)}(t)+\mathscr{Y}^{(4)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =2​ρ​T​(−n2+8​n​θ+1)(n−1)​(n+1)2​(n−1+4​θ)+ρ​Tn+1​(ηtN−1−ρ​t2+ρ​t​(n−4​θ+1)2​(n+1))\displaystyle=\frac{2\rho T(-n^{2}+8n\theta+1)}{(n-1)(n+1)^{2}(n-1+4\theta)}+\frac{\rho T}{n+1}\left(\eta\_{t}^{N}-1-\frac{\rho t}{2}+\frac{\rho t(n-4\theta+1)}{2(n+1)}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +ρ​T​(n−4​θ−1)​(n2+4​n​θ+2​n+1)(n−1)​(n+1)2​(n+4​θ−1).\displaystyle\qquad+\frac{\rho T(n-4\theta-1)(n^{2}+4n\theta+2n+1)}{(n-1)(n+1)^{2}(n+4\theta-1)}. |  |

Hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1ntνi\displaystyle\sum\_{i=1}^{n\_{t}}\nu\_{i} | =e−ρ​n+1n−1​T(n+1)2​n​(n​(ρ​t+1)​(n+1)​eρ​n+1n−1​T−(n−1)+2​n​eρ​n+1n−1​t)\displaystyle=\frac{e^{-\rho\frac{n+1}{n-1}T}}{(n+1)^{2}n}(n(\rho t+1)(n+1)e^{\rho\frac{n+1}{n-1}T}-(n-1)+2ne^{\rho\frac{n+1}{n-1}t}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (C.14) |  |  | +𝒴N​(t)+𝒴N(3)​(t)N+o​(1N),\displaystyle\quad+\frac{\mathscr{Y}\_{N}(t)+\mathscr{Y}\_{N}^{(3)}(t)}{N}+o\left(\frac{1}{N}\right), |  |

and 𝒴N​(t)+𝒴N(3)​(t)\mathscr{Y}\_{N}(t)+\mathscr{Y}\_{N}^{(3)}(t) is bounded once θ,T,ρ,n\theta,T,\rho,n are fixed.

*Step 2: Expansion of νN+1\nu\_{N+1}.*

From ([C.8](https://arxiv.org/html/2512.11765v1#A3.E8 "In Lemma C.4. ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) and Lemma [C.5](https://arxiv.org/html/2512.11765v1#A3.Thmtheorem5 "Lemma C.5. ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"),

|  |  |  |
| --- | --- | --- |
|  | νN+1=𝒯N+o(1N),𝒯:=ρ​Tκ^.\nu\_{N+1}=\frac{\mathscr{T}}{N}+o\left(\frac{1}{N}\right),\qquad\mathscr{T}\mathrel{\mathop{\ordinarycolon}}=\frac{\rho T}{\hat{\kappa}}. |  |

*Step 3: Expansion of ∑i=1N+1νi\sum\_{i=1}^{N+1}\nu\_{i}.*

Since nT=Nn\_{T}=N, ([C.14](https://arxiv.org/html/2512.11765v1#A3.E14 "In C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) at t=Tt=T gives ∑i=1Nνi\sum\_{i=1}^{N}\nu\_{i}; adding νN+1\nu\_{N+1} yields

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (C.15) |  | ∑i=1N+1νi\displaystyle\sum\_{i=1}^{N+1}\nu\_{i} | =e−ρ​n+1n−1​T(n+1)2​n​(n​((ρ​T+1)​(n+1)+2)​eρ​n+1n−1​T−(n−1))+ℳN+o​(1N),\displaystyle=\frac{e^{-\rho\frac{n+1}{n-1}T}}{(n+1)^{2}n}(n((\rho T+1)(n+1)+2)e^{\rho\frac{n+1}{n-1}T}-(n-1))+\frac{\mathscr{M}}{N}+o\left(\frac{1}{N}\right), |  |

with ℳ:=𝒴N(T)+𝒴N(3)(T)+𝒯\mathscr{M}\mathrel{\mathop{\ordinarycolon}}=\mathscr{Y}\_{N}(T)+\mathscr{Y}\_{N}^{(3)}(T)+\mathscr{T} (note that ηTN=0\eta\_{T}^{N}=0, so ℳ\mathscr{M} is independent of NN).

*Step 4: Expansion of Vt(N)V\_{t}^{(N)}.*

The limit in ([C.15](https://arxiv.org/html/2512.11765v1#A3.E15 "In C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) matches the right-hand side of ([C.14](https://arxiv.org/html/2512.11765v1#A3.E14 "In C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) at t=Tt=T, and ([C.14](https://arxiv.org/html/2512.11765v1#A3.E14 "In C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) matches the limit from ([C.6](https://arxiv.org/html/2512.11765v1#A3.E6 "In C.2.1. Proof for 𝜅=𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) (obtained when κ=n−1\kappa=n-1). Although the leading coefficient of the 1/N1/N term depends on θ\theta, the convergence order remains 1/N1/N for every θ>0\theta>0. Plugging these into the definition of V(N)V^{(N)} and applying ([C.1](https://arxiv.org/html/2512.11765v1#A3.E1 "In Remark C.2. ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) once more yields the claim.
∎

### C.3. Proof of Theorem [4.2](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem2 "Theorem 4.2 (Convergence of costs for 𝜃>0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")

Let (𝝃1,…,𝝃n)(\bm{\xi}\_{1},\dots,\bm{\xi}\_{n}) be the equilibrium profile; we drop the star superscript and suppress the NN-dependence of 𝝃i\bm{\xi}\_{i} and related quantities to keep notation light. We start with a simple lemma (valid for all κ≥κ^/2\kappa\geq\hat{\kappa}/2).

###### Lemma C.6.

For all i=1,…,ni=1,\dots,n,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| (C.16) |  | 𝔼​[𝒞𝕋​(𝝃i∣𝝃−i)]\displaystyle\mathbb{E}\left[\mathscr{C}\_{\mathbb{T}}\left(\bm{\xi}\_{i}\mid\bm{\xi}\_{-i}\right)\right] | =12(x¯2𝟏⊤​𝝂+x¯​(xi−x¯)​(𝟏⊤​𝝂+𝟏⊤​𝝎)(𝟏⊤​𝝂)​(𝟏⊤​𝝎)+(xi−x¯)2𝟏⊤​𝝎\displaystyle=\frac{1}{2}\Bigg(\frac{\bar{x}^{2}}{\bm{1}^{\top}\bm{\nu}}+\frac{\bar{x}(x\_{i}-\bar{x})(\bm{1}^{\top}\bm{\nu}+\bm{1}^{\top}\bm{\omega})}{(\bm{1}^{\top}\bm{\nu})(\bm{1}^{\top}\bm{\omega})}+\frac{(x\_{i}-\bar{x})^{2}}{\bm{1}^{\top}\bm{\omega}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +κ^(x¯𝟏⊤​𝝂)2𝝂⊤Γ~𝝂+x¯​(xi−x¯)(𝟏⊤​𝝂)​(𝟏⊤​𝝎)𝝎⊤(κ^Γ~−Γ~⊤)𝝂−(xi−x¯𝟏⊤​𝝎)2𝝎⊤Γ~𝝎),\displaystyle\hskip 30.00005pt+\hat{\kappa}\left(\frac{\bar{x}}{\bm{1}^{\top}\bm{\nu}}\right)^{2}\bm{\nu}^{\top}\tilde{\Gamma}\bm{\nu}+\frac{\bar{x}(x\_{i}-\bar{x})}{(\bm{1}^{\top}\bm{\nu})(\bm{1}^{\top}\bm{\omega})}\bm{\omega}^{\top}(\hat{\kappa}\tilde{\Gamma}-\tilde{\Gamma}^{\top})\bm{\nu}-\left(\frac{x\_{i}-\bar{x}}{\bm{1}^{\top}\bm{\omega}}\right)^{2}\bm{\omega}^{\top}\tilde{\Gamma}\bm{\omega}\Bigg), |  |

where x¯=1n​∑i=1nxi\bar{x}=\frac{1}{n}\sum\_{i=1}^{n}x\_{i}.

###### Proof.

By Lemma [2.6](https://arxiv.org/html/2512.11765v1#S2.Thmtheorem6 "Lemma 2.6 (Explicit objective). ‣ 2.2. Nash Equilibrium ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"),

|  |  |  |  |
| --- | --- | --- | --- |
| (C.17) |  | 𝔼[𝒞𝕋(𝝃i∣𝝃−i)]=12𝝃i⊤Γθ𝝃i+𝝃i⊤Γ~∑j≠i𝝃j=:A+B.\displaystyle\mathbb{E}[\mathscr{C}\_{\mathbb{T}}(\bm{\xi}\_{i}\mid\bm{\xi}\_{-i})]=\frac{1}{2}\bm{\xi}\_{i}^{\top}\Gamma^{\theta}\bm{\xi}\_{i}+\bm{\xi}\_{i}^{\top}\tilde{\Gamma}\sum\_{j\neq i}\bm{\xi}\_{j}=\mathrel{\mathop{\ordinarycolon}}A+B. |  |

By Theorem [2.7](https://arxiv.org/html/2512.11765v1#S2.Thmtheorem7 "Theorem 2.7 (Discrete equilibrium). ‣ 2.2. Nash Equilibrium ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"), 𝝃i=x¯​𝒗+(xi−x¯)​𝒘\bm{\xi}\_{i}=\bar{x}\bm{v}+(x\_{i}-\bar{x})\bm{w}, hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | A\displaystyle A | =12​(x¯2​𝒗⊤​Γθ​𝒗+x¯​(xi−x¯)​𝒗⊤​Γθ​𝒘+x¯​(xi−x¯)​𝒘⊤​Γθ​𝒗+(xi−x¯)2​𝒘⊤​Γθ​𝒘).\displaystyle=\frac{1}{2}\Big(\bar{x}^{2}\bm{v}^{\top}\Gamma^{\theta}\bm{v}+\bar{x}(x\_{i}-\bar{x})\bm{v}^{\top}\Gamma^{\theta}\bm{w}+\bar{x}(x\_{i}-\bar{x})\bm{w}^{\top}\Gamma^{\theta}\bm{v}+(x\_{i}-\bar{x})^{2}\bm{w}^{\top}\Gamma^{\theta}\bm{w}\Big). |  |

Moreover, since ∑j≠i𝝃j=κ^​x¯​𝒗+(x¯−xi)​𝒘\sum\_{j\neq i}\bm{\xi}\_{j}=\hat{\kappa}\bar{x}\bm{v}+(\bar{x}-x\_{i})\bm{w},

|  |  |  |  |
| --- | --- | --- | --- |
|  | B\displaystyle B | =(x¯​𝒗+(xi−x¯)​𝒘)⊤​Γ~​(κ^​x¯​𝒗+(x¯−xi)​𝒘)\displaystyle=\left(\bar{x}\bm{v}+\left(x\_{i}-\bar{x}\right)\bm{w}\right)^{\top}\tilde{\Gamma}\left(\hat{\kappa}\bar{x}\bm{v}+(\bar{x}-x\_{i})\bm{w}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =κ^​x¯2​𝒗⊤​Γ~​𝒗+κ^​x¯​(xi−x¯)​𝒘⊤​Γ~​𝒗−x¯​(xi−x¯)​𝒗⊤​Γ~​𝒘−(xi−x¯)2​𝒘⊤​Γ~​𝒘.\displaystyle=\hat{\kappa}\bar{x}^{2}\bm{v}^{\top}\tilde{\Gamma}\bm{v}+\hat{\kappa}\bar{x}\left(x\_{i}-\bar{x}\right)\bm{w}^{\top}\tilde{\Gamma}\bm{v}-\bar{x}\left(x\_{i}-\bar{x}\right)\bm{v}^{\top}\tilde{\Gamma}\bm{w}-\left(x\_{i}-\bar{x}\right)^{2}\bm{w}^{\top}\tilde{\Gamma}\bm{w}. |  |

Substituting into ([C.17](https://arxiv.org/html/2512.11765v1#A3.E17 "In C.3. Proof of Theorem 4.2 ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) and using

|  |  |  |
| --- | --- | --- |
|  | (Γθ+κ^​Γ~)​𝝂=𝟏,(Γθ−Γ~)​𝝎=𝟏,(\Gamma^{\theta}+\hat{\kappa}\tilde{\Gamma})\bm{\nu}=\bm{1},\qquad(\Gamma^{\theta}-\tilde{\Gamma})\bm{\omega}=\bm{1}, |  |

together with 𝝂⊤​𝟏=𝟏⊤​𝝂\bm{\nu}^{\top}\bm{1}=\bm{1}^{\top}\bm{\nu},
𝝎⊤​𝟏=𝟏⊤​𝝎\bm{\omega}^{\top}\bm{1}=\bm{1}^{\top}\bm{\omega}, and
𝝂⊤​Γ~​𝝎=𝝎⊤​Γ~⊤​𝝂\bm{\nu}^{\top}\tilde{\Gamma}\bm{\omega}=\bm{\omega}^{\top}\tilde{\Gamma}^{\top}\bm{\nu},
and writing 𝒗=𝝂/(𝟏⊤​𝝂)\bm{v}=\bm{\nu}/(\bm{1}^{\top}\bm{\nu}) and
𝒘=𝝎/(𝟏⊤​𝝎)\bm{w}=\bm{\omega}/(\bm{1}^{\top}\bm{\omega}), we obtain ([C.16](https://arxiv.org/html/2512.11765v1#A3.E16 "In Lemma C.6. ‣ C.3. Proof of Theorem 4.2 ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")).
∎

###### Lemma C.7.

For κ>κ^/2\kappa>\hat{\kappa}/2, as N↑∞N\uparrow\infty,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝂⊤​Γ~​𝝂\displaystyle{\bm{\nu}}^{\top}\tilde{\Gamma}{\bm{\nu}} | ⟶n−12​n2​(n+1)3​(−e−2​ρ​n+1n−1​T−4​n​e−ρ​n+1n−1​T+2​n2​(n+1)n−1​ρ​T+n2​(n+7)n−1),\displaystyle\longrightarrow\frac{n-1}{2n^{2}(n+1)^{3}}\Biggl(-e^{-2\rho\frac{n+1}{n-1}T}-4ne^{-\rho\frac{n+1}{n-1}T}+\frac{2n^{2}(n+1)}{n-1}\rho T+\frac{n^{2}(n+7)}{n-1}\Biggr), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝎⊤​(κ^​Γ~−Γ~⊤)​𝝂\displaystyle{\bm{\omega}}^{\top}\bigl(\hat{\kappa}\tilde{\Gamma}-\tilde{\Gamma}^{\top}\bigr){\bm{\nu}} | ⟶−(n−1)​(2​n−1)​e−ρ​n+1n−1​T+n​(n+4)​(n−1)+n​(n+1)​(n−2)​ρ​Tn​(n+1)2,\displaystyle\longrightarrow\frac{-(n-1)(2n-1)e^{-\rho\frac{n+1}{n-1}T}+n(n+4)(n-1)+n(n+1)(n-2)\rho T}{n(n+1)^{2}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝎⊤​Γ~​𝝎\displaystyle{\bm{\omega}}^{\top}\tilde{\Gamma}{\bm{\omega}} | ⟶2​ρ​T+12.\displaystyle\longrightarrow\frac{2\rho T+1}{2}. |  |

###### Proof.

The third limit follows from [[19](https://arxiv.org/html/2512.11765v1#bib.bib19), Lemma A.5]; we prove the first two.

*Step 1: Case κ=κ^\kappa=\hat{\kappa} (so κ~=n/2\tilde{\kappa}=n/2).* We have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝂⊤​Γ~​𝝂\displaystyle{\bm{\nu}}^{\top}\tilde{\Gamma}{\bm{\nu}} | =ν122+12​∑i=2N+1νi2+ν1​∑i=2N+1νi​αi−1+∑i=3N+1∑j=2i−1νi​νj​αi−j\displaystyle=\frac{\nu\_{1}^{2}}{2}+\frac{1}{2}\sum\_{i=2}^{N+1}\nu\_{i}^{2}+\nu\_{1}\sum\_{i=2}^{N+1}\nu\_{i}\alpha^{i-1}+\sum\_{i=3}^{N+1}\sum\_{j=2}^{i-1}\nu\_{i}\nu\_{j}\alpha^{i-j} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1(n+α)2[(1−α2)​N2+−α4+2​α3​(n−2)+α2​(2​n−2)+2​n​α+n22​(n2−α2)\displaystyle=\frac{1}{(n+\alpha)^{2}}\Biggl[\frac{(1-\alpha^{2})N}{2}+\frac{-\alpha^{4}+2\alpha^{3}(n-2)+\alpha^{2}(2n-2)+2n\alpha+n^{2}}{2\left(n^{2}-\alpha^{2}\right)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −θN(n−1)​α2​(α+1)n​(n+α)−θ2​Nα4​κ^22​n2​(n2−α2)],\displaystyle\hskip 42.00003pt-\theta^{N}\frac{(n-1)\alpha^{2}(\alpha+1)}{n(n+\alpha)}-\theta^{2N}\frac{\alpha^{4}\hat{\kappa}^{2}}{2n^{2}\left(n^{2}-\alpha^{2}\right)}\Biggr], |  |

and therefore, as N↑∞N\uparrow\infty,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝂⊤​Γ~​𝝂\displaystyle{\bm{\nu}}^{\top}\tilde{\Gamma}{\bm{\nu}} | ⟶1(n+1)2​(ρ​T+n+72​(n+1)−2​(n−1)n​(n+1)​e−ρ​n+1n−1​T−n−12​n2​(n+1)​e−2​ρ​n+1n−1​T)\displaystyle\longrightarrow\frac{1}{(n+1)^{2}}\Biggl(\rho T+\frac{n+7}{2(n+1)}-\frac{2(n-1)}{n(n+1)}e^{-\rho\frac{n+1}{n-1}T}-\frac{n-1}{2n^{2}(n+1)}e^{-2\rho\frac{n+1}{n-1}T}\Biggr) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =n−12​n2​(n+1)3​(−e−2​ρ​n+1n−1​T−4​n​e−ρ​n+1n−1​T+2​n2​(n+1)n−1​ρ​T+n2​(n+7)n−1)\displaystyle=\frac{n-1}{2n^{2}(n+1)^{3}}\Biggl(-e^{-2\rho\frac{n+1}{n-1}T}-4ne^{-\rho\frac{n+1}{n-1}T}+\frac{2n^{2}(n+1)}{n-1}\rho T+\frac{n^{2}(n+7)}{n-1}\Biggr) |  |

as well as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝎⊤​(κ^​Γ~−Γ~⊤)​𝝂\displaystyle{\bm{\omega}}^{\top}\left(\hat{\kappa}\tilde{\Gamma}-\tilde{\Gamma}^{\top}\right){\bm{\nu}} | =n−22​(ν1​ω1+∑i=2N+1νi​ωi)+κ^​ν1​∑i=2N+1ωi​αi−1+κ^​ωN+1​∑i=2Nνi​αN+1−i\displaystyle=\frac{n-2}{2}\left(\nu\_{1}\omega\_{1}+\sum\_{i=2}^{N+1}\nu\_{i}\omega\_{i}\right)+\hat{\kappa}\nu\_{1}\sum\_{i=2}^{N+1}\omega\_{i}\alpha^{i-1}+\hat{\kappa}\omega\_{N+1}\sum\_{i=2}^{N}\nu\_{i}\alpha^{N+1-i} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑i=1Nωi​(κ^​∑j=2i−1νj​αi−j−∑j=i+1N+1νj​αj−i)\displaystyle\quad+\sum\_{i=1}^{N}\omega\_{i}\left(\hat{\kappa}\sum\_{j=2}^{i-1}\nu\_{j}\alpha^{i-j}-\sum\_{j=i+1}^{N+1}\nu\_{j}\alpha^{j-i}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | →−(n−1)​(2​n−1)​e−ρ​n+1n−1​T+n​(n+4)​(n−1)+n​(n+1)​(n−2)​ρ​Tn​(n+1)2.\displaystyle\to\frac{-(n-1)(2n-1)e^{-\rho\frac{n+1}{n-1}T}+n(n+4)(n-1)+n(n+1)(n-2)\rho T}{n(n+1)^{2}}. |  |

*Step 2: General case κ≥n−12\kappa\geq\frac{n-1}{2} with κ≠n−1\kappa\neq n-1.*
We include the boundary value κ=n−12\kappa=\frac{n-1}{2} because intermediary limits below will also be used for that case. We first compute Γ~​𝝂\tilde{\Gamma}\bm{\nu}. Define C1=α​(α+1)κ+1−α​(κ−κ^−1)C\_{1}=\frac{\alpha\left(\alpha+1\right)}{\kappa+1-\alpha\left(\kappa-\hat{\kappa}-1\right)} as above and

|  |  |  |  |
| --- | --- | --- | --- |
|  | C2\displaystyle C\_{2} | :=∑σ∈{+,−}cσdσ(α​(κ−κ^)mσ−α​(κ−κ^)+mσmσ−α​κ)[mσ]N,\displaystyle\mathrel{\mathop{\ordinarycolon}}=\sum\_{\sigma\in\{+,-\}}c\_{\sigma}d\_{\sigma}\left(\frac{\alpha(\kappa-\hat{\kappa})}{m\_{\sigma}-\alpha(\kappa-\hat{\kappa})}+\frac{m\_{\sigma}}{m\_{\sigma}-\alpha\kappa}\right)[m\_{\sigma}]^{N}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | C3\displaystyle C\_{3} | :=−C2+∑σ∈{+,−}dσ(mσ−α2​κmσ−α​κ+n​C1​(κ−κ^)mσ−(κ−κ^))[mσ]N.\displaystyle\mathrel{\mathop{\ordinarycolon}}=-C\_{2}+\sum\_{\sigma\in\{+,-\}}d\_{\sigma}\left(\frac{m\_{\sigma}-\alpha^{2}\kappa}{m\_{\sigma}-\alpha\kappa}+\frac{nC\_{1}(\kappa-\hat{\kappa})}{m\_{\sigma}-(\kappa-\hat{\kappa})}\right)[m\_{\sigma}]^{N}. |  |

For σ∈{+,−}\sigma\in\{+,-\}, write σ¯=−\bar{\sigma}=- if σ=+\sigma=+ and σ¯=+\bar{\sigma}=+ if σ=−\sigma=-. Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Γ~​𝝂)1\displaystyle(\tilde{\Gamma}{\bm{\nu}})\_{1} | =12​∑σ∈{+,−}dσ​(mσ−α2​κ)mσ−α​κ​[mσ]N+C1​αN2​[κ]N,\displaystyle=\frac{1}{2}\sum\_{\sigma\in\{+,-\}}\frac{d\_{\sigma}(m\_{\sigma}-\alpha^{2}\kappa)}{m\_{\sigma}-\alpha\kappa}[m\_{\sigma}]^{N}+\frac{C\_{1}\alpha^{N}}{2}[\kappa]^{N}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (Γ~​𝝂)2\displaystyle(\tilde{\Gamma}{\bm{\nu}})\_{2} | =∑σ∈{+,−}dσ​(α​(mσ−α2​κ)mσ−α​κ+n​C1​α​(κ−κ^)2​mσ)​[mσ]N\displaystyle=\sum\_{\sigma\in\{+,-\}}d\_{\sigma}\left(\frac{\alpha(m\_{\sigma}-\alpha^{2}\kappa)}{m\_{\sigma}-\alpha\kappa}+\frac{nC\_{1}\alpha(\kappa-\hat{\kappa})}{2m\_{\sigma}}\right)[m\_{\sigma}]^{N} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +C2​(1−α)2+C1​(1+α2​(2​κ−n)+κ)​αN2​α​κ​[κ]N,\displaystyle\hskip 28.45274pt{}+\frac{C\_{2}(1-\alpha)}{2}+\frac{C\_{1}(1+\alpha^{2}\left(2\kappa-n\right)+\kappa)\alpha^{N}}{2\alpha\kappa}[\kappa]^{N}, |  |

and, for i∈{3,…,N}i\in\{3,\dots,N\},

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Γ~​𝝂)i\displaystyle(\tilde{\Gamma}{\bm{\nu}})\_{i} | =C2​(1+α)2+n​C12​α​(κ−κ^)​∑σ∈{+,−}dσ​mσ​(κ^−κ−mσ)​[mσ]Nκ^−κ+mσ​((κ−κ^)​αmσ)i\displaystyle=\frac{C\_{2}\left(1+\alpha\right)}{2}+\frac{nC\_{1}}{2\alpha(\kappa-\hat{\kappa})}\sum\_{\sigma\in\{+,-\}}\frac{d\_{\sigma}m\_{\sigma}\left(\hat{\kappa}-\kappa-m\_{\sigma}\right)[m\_{\sigma}]^{N}}{\hat{\kappa}-\kappa+m\_{\sigma}}\left(\frac{(\kappa-\hat{\kappa})\alpha}{m\_{\sigma}}\right)^{i} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +C1​αN+1​κ​[κ]N2​∑σ∈{+,−}cσ​(mσ+α2​κ)mσ​(mσ−α2​κ)​(mσα​κ)i+C3​αi−1.\displaystyle\hskip 28.45274pt{}+\frac{C\_{1}\alpha^{N+1}\kappa[\kappa]^{N}}{2}\sum\_{\sigma\in\{+,-\}}\frac{c\_{\sigma}\left(m\_{\sigma}+\alpha^{2}\kappa\right)}{m\_{\sigma}\left(m\_{\sigma}-\alpha^{2}\kappa\right)}\left(\frac{m\_{\sigma}}{\alpha\kappa}\right)^{i}+C\_{3}\alpha^{i-1}. |  |

Moreover,

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Γ~​𝝂)N+1\displaystyle(\tilde{\Gamma}{\bm{\nu}})\_{N+1} | =∑σ∈{+,−}cσ​(dσ​mσ​αmσ−α​κ+mσ+(2​dσ−1)​α2​(κ−κ^)2​(mσ−α​(κ−κ^))+C1​α2​κmσ−α2​κ)​[mσ]N\displaystyle=\sum\_{\sigma\in\{+,-\}}c\_{\sigma}\left(\frac{d\_{\sigma}m\_{\sigma}\alpha}{m\_{\sigma}-\alpha\kappa}+\frac{m\_{\sigma}+(2d\_{\sigma}-1)\alpha^{2}(\kappa-\hat{\kappa})}{2(m\_{\sigma}-\alpha(\kappa-\hat{\kappa}))}+\frac{C\_{1}\alpha^{2}\kappa}{m\_{\sigma}-\alpha^{2}\kappa}\right)[m\_{\sigma}]^{N} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +C3​αN−C1​αN​κ~​[κ−κ^]N,\displaystyle\hskip 14.22636pt{}+C\_{3}\alpha^{N}-C\_{1}\alpha^{N}\tilde{\kappa}\left[\kappa-\hat{\kappa}\right]^{N}, |  |

whose last term can also be written as −C1​αN2​(2​κ−κ^+1)​[κ−κ^]N-\frac{C\_{1}\alpha^{N}}{2}(2\kappa-\hat{\kappa}+1)[\kappa-\hat{\kappa}]^{N}.

Next, for i∈{3,…,N}i\in\{3,\dots,N\},

|  |  |  |
| --- | --- | --- |
|  | νi​(Γ~​𝝂)i=D1i+D2i+D3i+D4i,\nu\_{i}(\tilde{\Gamma}{\bm{\nu}})\_{i}=D\_{1}^{i}+D\_{2}^{i}+D\_{3}^{i}+D\_{4}^{i}, |  |

with D1i:=C2​(1+α)2νiD\_{1}^{i}\mathrel{\mathop{\ordinarycolon}}=\dfrac{C\_{2}\left(1+\alpha\right)}{2}\nu\_{i} and

|  |  |  |  |
| --- | --- | --- | --- |
|  | D2i:=C2(1−α)(\displaystyle D\_{2}^{i}\mathrel{\mathop{\ordinarycolon}}=C\_{2}(1-\alpha)\Bigg( | C3​αi−1+n​C12​α​(κ−κ^)​∑σ∈{+,−}dσ​mσ​(κ^−κ−mσ)​[mσ]Nκ^−κ+mσ​((κ−κ^)​αmσ)i\displaystyle C\_{3}\alpha^{i-1}+\frac{nC\_{1}}{2\alpha(\kappa-\hat{\kappa})}\sum\_{\sigma\in\{+,-\}}\frac{d\_{\sigma}m\_{\sigma}(\hat{\kappa}-\kappa-m\_{\sigma})[m\_{\sigma}]^{N}}{\hat{\kappa}-\kappa+m\_{\sigma}}\left(\frac{(\kappa-\hat{\kappa})\alpha}{m\_{\sigma}}\right)^{i} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +C1​αN+1​κ​[κ]N2∑σ∈{+,−}cσ​(mσ+α2​κ)mσ​(mσ−α2​κ)(mσα​κ)i),\displaystyle\hskip 99.58464pt{}+\frac{C\_{1}\alpha^{N+1}\kappa[\kappa]^{N}}{2}\sum\_{\sigma\in\{+,-\}}\frac{c\_{\sigma}(m\_{\sigma}+\alpha^{2}\kappa)}{m\_{\sigma}(m\_{\sigma}-\alpha^{2}\kappa)}\left(\frac{m\_{\sigma}}{\alpha\kappa}\right)^{i}\Bigg), |  |

|  |  |  |
| --- | --- | --- |
|  | D3i:=C1​C3α(n∑σ∈{+,−}dσ​mσ​[mσ]Nα​(κ−κ^)(α2​(κ−κ^)mσ)i+∑σ∈{+,−}cσ​αN+1​κ​[κ]Nmσ(mσκ)i),\displaystyle D\_{3}^{i}\mathrel{\mathop{\ordinarycolon}}=\frac{C\_{1}C\_{3}}{\alpha}\left(n\sum\_{\sigma\in\{+,-\}}\frac{d\_{\sigma}m\_{\sigma}[m\_{\sigma}]^{N}}{\alpha(\kappa-\hat{\kappa})}\left(\frac{\alpha^{2}(\kappa-\hat{\kappa})}{m\_{\sigma}}\right)^{i}+\sum\_{\sigma\in\{+,-\}}\frac{c\_{\sigma}\alpha^{N+1}\kappa[\kappa]^{N}}{m\_{\sigma}}\left(\frac{m\_{\sigma}}{\kappa}\right)^{i}\right), |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | D4i\displaystyle D\_{4}^{i} | :=(C1)2(n22​(α​(κ−κ^))2(∑σ∈{+,−}(dσmσ[mσ]N)2κ^−κ−mσκ^−κ+mσ(α​(κ−κ^)mσ)2​i\displaystyle\mathrel{\mathop{\ordinarycolon}}=\left(C\_{1}\right)^{2}\Bigg(\frac{n^{2}}{2(\alpha(\kappa-\hat{\kappa}))^{2}}\Bigg(\sum\_{\sigma\in\{+,-\}}\left(d\_{\sigma}m\_{\sigma}[m\_{\sigma}]^{N}\right)^{2}\frac{\hat{\kappa}-\kappa-m\_{\sigma}}{\hat{\kappa}-\kappa+m\_{\sigma}}\left(\frac{\alpha(\kappa-\hat{\kappa})}{m\_{\sigma}}\right)^{2i} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +d+d−m+m−[m+]N[m−]N(2​((κ^−κ)2−m+​m−)n​(1−α2)​(κ^−κ))((α​(κ−κ^))2m+​m−)i)\displaystyle\hskip 128.0374pt+d\_{+}d\_{-}m\_{+}m\_{-}\left[m\_{+}\right]^{N}\left[m\_{-}\right]^{N}\left(\frac{2\left((\hat{\kappa}-\kappa)^{2}-m\_{+}m\_{-}\right)}{n(1-\alpha^{2})(\hat{\kappa}-\kappa)}\right)\left(\frac{\left(\alpha(\kappa-\hat{\kappa})\right)^{2}}{m\_{+}m\_{-}}\right)^{i}\Bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +α2​(N+1)​κ2​([κ]N)22(∑σ∈{+,−}(cσ)2​(mσ+α2​κ)(mσ)2​(mσ−α2​κ)(mσα​κ)2​i\displaystyle\hskip 56.9055pt+\frac{\alpha^{2(N+1)}\kappa^{2}\left([\kappa]^{N}\right)^{2}}{2}\Bigg(\sum\_{\sigma\in\{+,-\}}\frac{(c\_{\sigma})^{2}(m\_{\sigma}+\alpha^{2}\kappa)}{(m\_{\sigma})^{2}(m\_{\sigma}-\alpha^{2}\kappa)}\left(\frac{m\_{\sigma}}{\alpha\kappa}\right)^{2i} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +c+​c−​2​((α2​κ)2−m+​m−)n​m+​m−​α2​(1−α2)​κ(m+​m−(α​κ)2)i)\displaystyle\hskip 170.71652pt+\frac{c\_{+}c\_{-}2\left((\alpha^{2}\kappa)^{2}-m\_{+}m\_{-}\right)}{nm\_{+}m\_{-}\alpha^{2}(1-\alpha^{2})\kappa}\left(\frac{m\_{+}m\_{-}}{(\alpha\kappa)^{2}}\right)^{i}\Bigg) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +αN​κ​[κ]N​n2​(κ−κ^)(2​(κ^−(1−α2)​κ)n​(1−α2)∑σ∈{+,−}dσcσ[mσ]N(κ−κ^κ)i\displaystyle\hskip 56.9055pt+\frac{\alpha^{N}\kappa\left[\kappa\right]^{N}n}{2(\kappa-\hat{\kappa})}\Bigg(\frac{2(\hat{\kappa}-(1-\alpha^{2})\kappa)}{n(1-\alpha^{2})}\sum\_{\sigma\in\{+,-\}}d\_{\sigma}c\_{\sigma}\left[m\_{\sigma}\right]^{N}\left(\frac{\kappa-\hat{\kappa}}{\kappa}\right)^{i} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑σ∈{+,−}cσ¯​dσ​mσ​[mσ]Nmσ¯(κ^−κ−mσκ^−κ+mσ+mσ¯+α2​κmσ¯−α2​κ)(mσ¯​(κ−κ^)mσ​κ)i)).\displaystyle\hskip 133.72786pt+\sum\_{\sigma\in\{+,-\}}\frac{c\_{\bar{\sigma}}d\_{\sigma}m\_{\sigma}[m\_{\sigma}]^{N}}{m\_{\bar{\sigma}}}\left(\frac{\hat{\kappa}-\kappa-m\_{\sigma}}{\hat{\kappa}-\kappa+m\_{\sigma}}+\frac{m\_{\bar{\sigma}}+\alpha^{2}\kappa}{m\_{\bar{\sigma}}-\alpha^{2}\kappa}\right)\left(\frac{m\_{\bar{\sigma}}(\kappa-\hat{\kappa})}{m\_{\sigma}\kappa}\right)^{i}\Bigg)\Bigg). |  |

Summing over ii, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=3ND1i\displaystyle\sum\_{i=3}^{N}D^{i}\_{1} | =C2​(1+α)2(C2(1−α)(N−2)+C1∑σ∈{+,−}mσ​cσ​(α​κmσ​[mσ]N−mσα​κ​αN​[κ]N)mσ−α​κ\displaystyle=\frac{C\_{2}(1+\alpha)}{2}\Bigg(C\_{2}(1-\alpha)(N-2)+C\_{1}\sum\_{\sigma\in\{+,-\}}\frac{m\_{\sigma}c\_{\sigma}\left(\frac{\alpha\kappa}{m\_{\sigma}}[m\_{\sigma}]^{N}-\frac{m\_{\sigma}}{\alpha\kappa}\alpha^{N}[\kappa]^{N}\right)}{m\_{\sigma}-\alpha\kappa} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +nC1∑σ∈{+,−}dσ​mσ​((α​(κ−κ^)mσ)2​[mσ]N−αN​[κ−κ^]N)mσ−α​(κ−κ^)),\displaystyle\hskip 75.39963pt+nC\_{1}\sum\_{\sigma\in\{+,-\}}\frac{d\_{\sigma}m\_{\sigma}\left(\left(\frac{\alpha(\kappa-\hat{\kappa})}{m\_{\sigma}}\right)^{2}[m\_{\sigma}]^{N}-\alpha^{N}\left[\kappa-\hat{\kappa}\right]^{N}\right)}{m\_{\sigma}-\alpha(\kappa-\hat{\kappa})}\Bigg), |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=3ND2i\displaystyle\sum\_{i=3}^{N}D\_{2}^{i} | =C2​C3​(α2−αN)\displaystyle=C\_{2}C\_{3}(\alpha^{2}-\alpha^{N}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +C2​C1​(1−α2)​n2​(1+α)​∑σ∈{+,−}(dσ)2​(κ^−κ−mσ)​((mσ)2​αN​[κ−κ^]N−(α​(κ−κ^))2​[mσ]N)dσ​mσ​(mσ−(κ−κ^))​((κ−κ^)​α−mσ)\displaystyle\quad+\frac{C\_{2}C\_{1}(1-\alpha^{2})n}{2(1+\alpha)}\sum\_{\sigma\in\{+,-\}}\frac{(d\_{\sigma})^{2}(\hat{\kappa}-\kappa-m\_{\sigma})\left((m\_{\sigma})^{2}\alpha^{N}\left[\kappa-\hat{\kappa}\right]^{N}-(\alpha(\kappa-\hat{\kappa}))^{2}\left[m\_{\sigma}\right]^{N}\right)}{d\_{\sigma}m\_{\sigma}(m\_{\sigma}-(\kappa-\hat{\kappa}))((\kappa-\hat{\kappa})\alpha-m\_{\sigma})} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +C2​C1​(1−α2)2​(1+α)​∑σ∈{+,−}(cσ)2​(mσ+α2​κ)​((α​κ)2​[mσ]N−(mσ)2​αN​[κ]N)cσ​α​κ​(mσ−α​κ)​(mσ−α2​κ),\displaystyle\quad+\frac{C\_{2}C\_{1}(1-\alpha^{2})}{2(1+\alpha)}\sum\_{\sigma\in\{+,-\}}\frac{(c\_{\sigma})^{2}(m\_{\sigma}+\alpha^{2}\kappa)((\alpha\kappa)^{2}\left[m\_{\sigma}\right]^{N}-(m\_{\sigma})^{2}\alpha^{N}\left[\kappa\right]^{N})}{c\_{\sigma}\alpha\kappa(m\_{\sigma}-\alpha\kappa)(m\_{\sigma}-\alpha^{2}\kappa)}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=3ND3i\displaystyle\sum\_{i=3}^{N}D\_{3}^{i} | =C1C3(∑σ∈{+,−}n​dσ​((mσ​αN)2​[κ−κ^]N−(α2​(κ−κ^))2​[mσ]N)mσ​(α2​(κ−κ^)−mσ)\displaystyle=C\_{1}C\_{3}\Bigg(\sum\_{\sigma\in\{+,-\}}\frac{nd\_{\sigma}\left((m\_{\sigma}\alpha^{N})^{2}\left[\kappa-\hat{\kappa}\right]^{N}-\left({\alpha^{2}}(\kappa-\hat{\kappa})\right)^{2}[m\_{\sigma}]^{N}\right)}{m\_{\sigma}(\alpha^{2}(\kappa-\hat{\kappa})-m\_{\sigma})} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑σ∈{+,−}cσ​(κ2​αN​[mσ]N−(mσ)2​αN​[κ]N)κ​(mσ−κ)),\displaystyle\hskip 75.39963pt+\sum\_{\sigma\in\{+,-\}}\frac{c\_{\sigma}\left(\kappa^{2}\alpha^{N}\left[m\_{\sigma}\right]^{N}-(m\_{\sigma})^{2}\alpha^{N}[\kappa]^{N}\right)}{\kappa(m\_{\sigma}-\kappa)}\Bigg), |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=3ND4i\displaystyle\sum\_{i=3}^{N}D\_{4}^{i} |  | |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(C1)2(n22∑σ∈{+,−}(dσ​mσ)2​(κ^−κ−mσ)(mσ−(κ−κ^))​(α​(κ−κ^)−mσ)​(mσ+α​(κ−κ^))(αN[κ−κ^]N)2\displaystyle=(C\_{1})^{2}\Bigg(\frac{n^{2}}{2}\sum\_{\sigma\in\{+,-\}}\frac{({d\_{\sigma}m\_{\sigma}})^{2}({\hat{\kappa}-\kappa-m\_{\sigma}})}{({m\_{\sigma}-(\kappa-\hat{\kappa})})({\alpha(\kappa-\hat{\kappa})-m\_{\sigma}})({m\_{\sigma}+\alpha(\kappa-\hat{\kappa})})}({\alpha^{N}[{\kappa-\hat{\kappa}}]^{N}})^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −12​(α​κ)2​∑σ∈{+,−}(cσ)2​(mσ)4​(mσ+α2​κ)(mσ−α​κ)​(mσ−α2​κ)​(mσ+α​κ)​(αN​[κ]N)2\displaystyle\hskip 14.22636pt-\frac{1}{2(\alpha\kappa)^{2}}\sum\_{\sigma\in\{+,-\}}\frac{(c\_{\sigma})^{2}(m\_{\sigma})^{4}(m\_{\sigma}+\alpha^{2}\kappa)}{(m\_{\sigma}-\alpha\kappa)(m\_{\sigma}-\alpha^{2}\kappa)\left({m\_{\sigma}+\alpha\kappa}\right)}\left({\alpha^{N}\left[{\kappa}\right]^{N}}\right)^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑σ∈{+,−}((cσ)2​(mσ+α2​κ)​(α​κ)22​(mσ−α​κ)​(mσ−α2​κ)​(mσ+α​κ)\displaystyle\hskip 14.22636pt+\sum\_{\sigma\in\{+,-\}}\Bigg(\frac{(c\_{\sigma})^{2}\left({m\_{\sigma}+\alpha^{2}\kappa}\right)(\alpha\kappa)^{2}}{2(m\_{\sigma}-\alpha\kappa)\left({m\_{\sigma}-\alpha^{2}\kappa}\right)\left({m\_{\sigma}+\alpha\kappa}\right)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −n2​(dσ)2​(α​(κ−κ^))4​(κ^−κ−mσ)2​(mσ)2​(mσ−(κ−κ^))​(α​(κ−κ^)−mσ)​(mσ+α​(κ−κ^)))([mσ]N)2\displaystyle\hskip 85.35826pt-\frac{n^{2}\left({d\_{\sigma}}\right)^{2}\left({\alpha(\kappa-\hat{\kappa})}\right)^{4}\left({\hat{\kappa}-\kappa-m\_{\sigma}}\right)}{2(m\_{\sigma})^{2}\left({m\_{\sigma}-(\kappa-\hat{\kappa})}\right)\left({\alpha(\kappa-\hat{\kappa})-m\_{\sigma}}\right)\left({m\_{\sigma}+\alpha(\kappa-\hat{\kappa})}\right)}\Bigg)\left({\left[{m\_{\sigma}}\right]^{N}}\right)^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑σ∈{+,−}αN​κ​(n​cσ​dσ¯​mσ¯​(κ^−κ−mσ¯κ^−κ+mσ¯+mσ+α2​κmσ−α2​κ)2​(mσ​(κ−κ^)−mσ¯​κ)−cσ​dσ​(κ^−(1−α2)​κ)(1−α2)​κ^)​[mσ]N​[κ−κ^]N\displaystyle\hskip 14.22636pt+\sum\_{\sigma\in\{+,-\}}\alpha^{N}\kappa\left({\frac{nc\_{\sigma}d\_{\bar{\sigma}}m\_{\bar{\sigma}}\left({\frac{\hat{\kappa}-\kappa-m\_{\bar{\sigma}}}{\hat{\kappa}-\kappa+m\_{\bar{\sigma}}}+\frac{m\_{\sigma}+\alpha^{2}\kappa}{m\_{\sigma}-\alpha^{2}\kappa}}\right)}{2\left({m\_{\sigma}(\kappa-\hat{\kappa})-m\_{\bar{\sigma}}\kappa}\right)}-\frac{c\_{\sigma}d\_{\sigma}\left({\hat{\kappa}-\left({1-\alpha^{2}}\right)\kappa}\right)}{\left({1-\alpha^{2}}\right)\hat{\kappa}}}\right)\left[{m\_{\sigma}}\right]^{N}\left[{\kappa-\hat{\kappa}}\right]^{N} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑σ∈{+,−}αN​(κ−κ^)2κ​(cσ​dσ​(κ^−(1−α2)​κ)κ^​(1−α2)−n​cσ¯​dσ​(mσ¯)2​(κ^−κ−mσκ^−κ+mσ+mσ¯+α2​κmσ¯−α2​κ)2​mσ​(mσ¯​(κ−κ^)−mσ​κ))​[mσ]N​[κ]N\displaystyle\hskip 14.22636pt+\sum\_{\sigma\in\{+,-\}}\frac{\alpha^{N}(\kappa-\hat{\kappa})^{2}}{\kappa}\left({\frac{c\_{\sigma}d\_{\sigma}\left({\hat{\kappa}-\left({1-\alpha^{2}}\right)\kappa}\right)}{\hat{\kappa}\left({1-\alpha^{2}}\right)}-\frac{nc\_{\bar{\sigma}}d\_{\sigma}\left({m\_{\bar{\sigma}}}\right)^{2}\left({\frac{\hat{\kappa}-\kappa-m\_{\sigma}}{\hat{\kappa}-\kappa+m\_{\sigma}}+\frac{m\_{\bar{\sigma}}+\alpha^{2}\kappa}{m\_{\bar{\sigma}}-\alpha^{2}\kappa}}\right)}{2m\_{\sigma}\left({m\_{\bar{\sigma}}(\kappa-\hat{\kappa})-m\_{\sigma}\kappa}\right)}}\right)\left[{m\_{\sigma}}\right]^{N}\left[{\kappa}\right]^{N} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +κ​((α2−1)​κ+κ^)​(αN)2​(c+​c−​(α​(κ−κ^))2n​(α​κ)2​(1−α2)​κ^​([κ]N)2−n​d+​d−κ^​(1−α2)​([κ−κ^]N)2)\displaystyle\hskip 14.22636pt+\kappa\left({\left({\alpha^{2}-1}\right)\kappa+\hat{\kappa}}\right)\left({\alpha^{N}}\right)^{2}\left({\frac{c\_{+}c\_{-}\left({\alpha(\kappa-\hat{\kappa})}\right)^{2}}{n(\alpha\kappa)^{2}\left({1-\alpha^{2}}\right)\hat{\kappa}}\left({\left[{\kappa}\right]^{N}}\right)^{2}-\frac{nd\_{+}d\_{-}}{\hat{\kappa}\left({1-\alpha^{2}}\right)}\left({\left[{\kappa-\hat{\kappa}}\right]^{N}}\right)^{2}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−α2)​κ−κ^n​κ(c+​c−​κ2κ^​(1−α2)−n2​d+​d−​(κ−κ^)2κ^​(1−α2))[m+]N[m−]N).\displaystyle\hskip 14.22636pt+\frac{\left({1-\alpha^{2}}\right)\kappa-\hat{\kappa}}{n\kappa}\left({\frac{c\_{+}c\_{-}\kappa^{2}}{\hat{\kappa}\left({1-\alpha^{2}}\right)}-\frac{n^{2}d\_{+}d\_{-}(\kappa-\hat{\kappa})^{2}}{\hat{\kappa}\left({1-\alpha^{2}}\right)}}\right)\left[{m\_{+}}\right]^{N}[m\_{-}]^{N}\Bigg). |  |

Note that

|  |  |  |
| --- | --- | --- |
|  | c+m+​(κ−κ^)−m−​κ=(R​(d−1−α2​1−α2c+​κ+(κ−κ^)))−1.\frac{c\_{+}}{m\_{+}(\kappa-\hat{\kappa})-m\_{-}\kappa}=\left(R\left(\frac{d\_{-}}{1-\alpha^{2}}\frac{1-\alpha^{2}}{c\_{+}}\kappa+(\kappa-\hat{\kappa})\right)\right)^{-1}. |  |

Using Lemma [C.5](https://arxiv.org/html/2512.11765v1#A3.Thmtheorem5 "Lemma C.5. ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"), the limits of the preceding sums combine to give

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝂⊤​Γ~​𝝂\displaystyle{\bm{\nu}}^{\top}\tilde{\Gamma}{\bm{\nu}} | =ν1​(Γ~​𝝂)1+ν2​(Γ~​𝝂)2+∑k=14∑i=3NDki+νN+1​(Γ~​𝝂)N+1\displaystyle=\nu\_{1}(\tilde{\Gamma}{\bm{\nu}})\_{1}+\nu\_{2}(\tilde{\Gamma}{\bm{\nu}})\_{2}+\sum\_{k=1}^{4}\sum\_{i=3}^{N}D\_{k}^{i}+\nu\_{N+1}(\tilde{\Gamma}{\bm{\nu}})\_{N+1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | →(n−1)2​n2​(n+1)3​(−e−2​ρ​n+1n−1​T−4​n​e−ρ​n+1n−1​T+2​n2​(n+1)(n−1)​ρ​T+n2​(n+7)(n−1)).\displaystyle\to\frac{(n-1)}{2n^{2}(n+1)^{3}}\left(-e^{-2\rho\frac{n+1}{n-1}T}-4ne^{-\rho\frac{n+1}{n-1}T}+\frac{2n^{2}(n+1)}{(n-1)}\rho T+\frac{n^{2}(n+7)}{(n-1)}\right). |  |

We now turn to 𝝎⊤​(κ^​Γ~−Γ~⊤)​𝝂{\bm{\omega}}^{\top}\left(\hat{\kappa}\tilde{\Gamma}-\tilde{\Gamma}^{\top}\right){\bm{\nu}}. Set

|  |  |  |  |
| --- | --- | --- | --- |
|  | C4\displaystyle C\_{4} | :=(α2​(κ~−1)−κ~)−α​(α​(κ~−1)κ~)N+1(κ~−α​(κ~−1))​(α2​(κ~−1)−κ~),\displaystyle\mathrel{\mathop{\ordinarycolon}}=\frac{\left(\alpha^{2}\left(\tilde{\kappa}-1\right)-\tilde{\kappa}\right)-\alpha\left(\frac{\alpha\left(\tilde{\kappa}-1\right)}{\tilde{\kappa}}\right)^{N+1}}{\left(\tilde{\kappa}-\alpha\left(\tilde{\kappa}-1\right)\right)\left(\alpha^{2}\left(\tilde{\kappa}-1\right)-\tilde{\kappa}\right)}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | C5\displaystyle C\_{5} | :=(κ~+α(κ~−1)−(n−2)​κ~​(α2​(κ~−1)−κ~)κ~−α​(κ~−1))α2​(κ~−1)κ~2​(α2​(κ~−1)−κ~),\displaystyle\mathrel{\mathop{\ordinarycolon}}=\left(\tilde{\kappa}+\alpha\left(\tilde{\kappa}-1\right)-\frac{(n-2)\tilde{\kappa}\left(\alpha^{2}(\tilde{\kappa}-1)-\tilde{\kappa}\right)}{\tilde{\kappa}-\alpha(\tilde{\kappa}-1)}\right)\frac{\alpha^{2}(\tilde{\kappa}-1)}{\tilde{\kappa}^{2}\left(\alpha^{2}\left(\tilde{\kappa}-1\right)-\tilde{\kappa}\right)}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | C6\displaystyle C\_{6} | :=n−22​κ~​(κ~−α​(κ~−1)).\displaystyle\mathrel{\mathop{\ordinarycolon}}=\frac{n-2}{2\tilde{\kappa}\left(\tilde{\kappa}-\alpha(\tilde{\kappa}-1)\right)}. |  |

Then, for i∈{2,…,N}i\in\{2,\dots,N\},

|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝝎⊤​(κ^​Γ~−Γ~⊤))1\displaystyle\bigl({\bm{\omega}}^{\top}(\hat{\kappa}\tilde{\Gamma}-\tilde{\Gamma}^{\top})\bigr)\_{1} | =n−22​ω1+(n−1)​ακ~−α​(κ~−1)​(1−(α​(κ~−1)κ~)N),\displaystyle=\frac{n-2}{2}\omega\_{1}+\frac{(n-1)\alpha}{\tilde{\kappa}-\alpha\bigl(\tilde{\kappa}-1\bigr)}\left(1-\left(\frac{\alpha(\tilde{\kappa}-1)}{\tilde{\kappa}}\right)^{N}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝝎⊤​(κ^​Γ~−Γ~⊤))i\displaystyle\bigl({\bm{\omega}}^{\top}(\hat{\kappa}\tilde{\Gamma}-\tilde{\Gamma}^{\top})\bigr)\_{i} | =n−22​ωi+C4​αi+C5​(α​(κ~−1)κ~)N−i+(n−2)​ακ~−α​(κ~−1),\displaystyle=\frac{n-2}{2}\omega\_{i}+C\_{4}\alpha^{i}+C\_{5}\left(\frac{\alpha(\tilde{\kappa}-1)}{\tilde{\kappa}}\right)^{N-i}+\frac{(n-2)\alpha}{\tilde{\kappa}-\alpha\bigl(\tilde{\kappa}-1\bigr)}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | (𝝎⊤​(κ^​Γ~−Γ~⊤))N+1=α​(αN​(κ~−α2​(κ~−1))​κ~+α2​(κ~−1)​(κ~−1+(α2​(κ~−1)κ~)N)−κ~2)κ~​(κ~−α​(κ~−1))​(κ~−α2​(κ~−1))+n−22​1κ~.\displaystyle\bigl({\bm{\omega}}^{\top}(\hat{\kappa}\tilde{\Gamma}-\tilde{\Gamma}^{\top})\bigr)\_{N+1}=\frac{\alpha\Big(\alpha^{N}\left(\tilde{\kappa}-\alpha^{2}\left(\tilde{\kappa}-1\right)\right)\tilde{\kappa}+\alpha^{2}\left(\tilde{\kappa}-1\right)\left(\tilde{\kappa}-1+\left(\frac{\alpha^{2}\left(\tilde{\kappa}-1\right)}{\tilde{\kappa}}\right)^{N}\right)-\tilde{\kappa}^{2}\Big)}{\tilde{\kappa}\left(\tilde{\kappa}-\alpha\left(\tilde{\kappa}-1\right)\right)\left(\tilde{\kappa}-\alpha^{2}\left(\tilde{\kappa}-1\right)\right)}+\frac{n-2}{2}\frac{1}{\tilde{\kappa}}. |  |

For i∈{2,…,N}i\in\{2,\dots,N\}, write

|  |  |  |
| --- | --- | --- |
|  | (𝝎⊤​(κ^​Γ~−Γ~⊤))i​νi=G1i+G2i+G3i,\bigl({\bm{\omega}}^{\top}(\hat{\kappa}\tilde{\Gamma}-\tilde{\Gamma}^{\top})\bigr)\_{i}{\nu}\_{i}=G^{i}\_{1}+G^{i}\_{2}+G^{i}\_{3}, |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | G1i\displaystyle G^{i}\_{1} | =C2​(1−α)​(n−22​ωi+C4​αi+C5​(α​(κ~−1)κ~)N​(κ~α​(κ~−1))i+(n−2)​ακ~−α​(κ~−1)),\displaystyle=C\_{2}(1-\alpha)\left(\frac{n-2}{2}\omega\_{i}+C\_{4}\alpha^{i}+C\_{5}\left(\frac{\alpha(\tilde{\kappa}-1)}{\tilde{\kappa}}\right)^{N}\left(\frac{\tilde{\kappa}}{\alpha(\tilde{\kappa}-1)}\right)^{i}+\frac{(n-2)\alpha}{\tilde{\kappa}-\alpha(\tilde{\kappa}-1)}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | G2i\displaystyle G^{i}\_{2} | =nC1∑σ∈{+,−}dσ​mσα​(κ−κ^)(n−22ωi(α​(κ−κ^)mσ)i+C4(α2​(κ−κ^)mσ)i\displaystyle=nC\_{1}\sum\_{\sigma\in\{+,-\}}\frac{d\_{\sigma}m\_{\sigma}}{\alpha(\kappa-\hat{\kappa})}\Bigg(\frac{n-2}{2}\omega\_{i}\left(\frac{\alpha(\kappa-\hat{\kappa})}{m\_{\sigma}}\right)^{i}+C\_{4}\left(\frac{\alpha^{2}(\kappa-\hat{\kappa})}{m\_{\sigma}}\right)^{i} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +C5(α​(κ~−1)κ~)N(κ~​(κ−κ^)mσ​(κ~−1))i+(n−2)​ακ~−α​(κ~−1)(α​(κ−κ^)mσ)i)[mσ]N,\displaystyle\qquad\qquad+C\_{5}\left(\frac{\alpha(\tilde{\kappa}-1)}{\tilde{\kappa}}\right)^{N}\left(\frac{\tilde{\kappa}(\kappa-\hat{\kappa})}{m\_{\sigma}(\tilde{\kappa}-1)}\right)^{i}+\frac{(n-2)\alpha}{\tilde{\kappa}-\alpha(\tilde{\kappa}-1)}\left(\frac{\alpha(\kappa-\hat{\kappa})}{m\_{\sigma}}\right)^{i}\Bigg)[m\_{\sigma}]^{N}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | G3i\displaystyle G^{i}\_{3} | =C1∑σ∈{+,−}cσ​αN+1​κmσ(n−22ωi(mσα​κ)i+C4(mσκ)i+C5(α​(κ~−1)κ~)N(κ~​mσκ​α2​(κ~−1))i\displaystyle=C\_{1}\sum\_{\sigma\in\{+,-\}}\frac{c\_{\sigma}\alpha^{N+1}\kappa}{m\_{\sigma}}\Bigg(\frac{n-2}{2}\omega\_{i}\left(\frac{m\_{\sigma}}{\alpha\kappa}\right)^{i}+C\_{4}\left(\frac{m\_{\sigma}}{\kappa}\right)^{i}+C\_{5}\left(\frac{\alpha(\tilde{\kappa}-1)}{\tilde{\kappa}}\right)^{N}\left(\frac{\tilde{\kappa}m\_{\sigma}}{{\kappa}\alpha^{2}(\tilde{\kappa}-1)}\right)^{i} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(n−2)​ακ~−α​(κ~−1)(mσα​κ)i)[κ]N.\displaystyle\qquad\qquad+\frac{(n-2)\alpha}{\tilde{\kappa}-\alpha(\tilde{\kappa}-1)}\left(\frac{m\_{\sigma}}{\alpha\kappa}\right)^{i}\Bigg)[\kappa]^{N}. |  |

Summing over ii,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=2NG1i\displaystyle\sum\_{i=2}^{N}G\_{1}^{i} | =C2(1−α)\bBigg@3.3[C6((1−α)(N−1)κ~+α2​(κ~−1)κ~−α​(κ~−1)(1−(α​(κ~−1)κ~)N−1))\displaystyle=C\_{2}\left(1-\alpha\right)\bBigg@{3.3}[C\_{6}\left(\left(1-\alpha\right)\left(N-1\right)\tilde{\kappa}+\frac{\alpha^{2}\left(\tilde{\kappa}-1\right)}{\tilde{\kappa}-\alpha\left(\tilde{\kappa}-1\right)}\left(1-\left(\frac{\alpha\left(\tilde{\kappa}-1\right)}{\tilde{\kappa}}\right)^{N-1}\right)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +C4αN+1−α2α−1+C5​κ~κ~−α​(κ~−1)(1−(α​(κ~−1)κ~)N−1)+(n−2)​ακ~−α​(κ~−1)(N−1)\bBigg@3.3].\displaystyle\hskip 46.00012pt+C\_{4}\frac{\alpha^{N+1}-\alpha^{2}}{\alpha-1}+\frac{C\_{5}\tilde{\kappa}}{\tilde{\kappa}-\alpha\left(\tilde{\kappa}-1\right)}\left(1-\left(\frac{\alpha\left(\tilde{\kappa}-1\right)}{\tilde{\kappa}}\right)^{N-1}\right)+\frac{\left(n-2\right)\alpha}{\tilde{\kappa}-\alpha\left(\tilde{\kappa}-1\right)}\left(N-1\right)\bBigg@{3.3}]. |  |

Moreover,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=2NG2i\displaystyle{\sum\_{i=2}^{N}G^{i}\_{2}} |  |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑σ∈{+,−}n​C1​dσ​mσα​(κ−κ^)\bBigg@3.3[C6\bBigg@3(α​(1−α)​κ~​(κ−κ^)α​(κ−κ^)−mσ(αN[κ−κ^]N−α​(κ−κ^)mσ[mσ]N)\displaystyle\hskip-28.45274pt=\sum\_{\sigma\in\{+,-\}}\frac{nC\_{1}d\_{\sigma}m\_{\sigma}}{\alpha(\kappa-\hat{\kappa})}\bBigg@{3.3}[C\_{6}\bBigg@{3}(\frac{\alpha\left({1-\alpha}\right)\tilde{\kappa}(\kappa-\hat{\kappa})}{\alpha(\kappa-\hat{\kappa})-m\_{\sigma}}\left({\alpha^{N}\left[\kappa-\hat{\kappa}\right]^{N}-\frac{\alpha\left({\kappa-\hat{\kappa}}\right)}{m\_{\sigma}}\left[m\_{\sigma}\right]^{N}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +α​κ~​(κ−κ^)κ~​(κ−κ^)−mσ​(κ~−1)(κ~−1κ~αN+1[κ−κ^]N−κ−κ^mσαN+1(κ~−1κ~)N[mσ]N)\bBigg@3)\displaystyle\hskip 79.6678pt+\frac{\alpha\tilde{\kappa}(\kappa-\hat{\kappa})}{\tilde{\kappa}(\kappa-\hat{\kappa})-m\_{\sigma}\left({\tilde{\kappa}-1}\right)}\left({\frac{\tilde{\kappa}-1}{\tilde{\kappa}}\alpha^{N+1}\left[\kappa-\hat{\kappa}\right]^{N}-\frac{\kappa-\hat{\kappa}}{m\_{\sigma}}\alpha^{N+1}\left({\frac{\tilde{\kappa}-1}{\tilde{\kappa}}}\right)^{N}\left[m\_{\sigma}\right]^{N}}\right)\bBigg@{3}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +C4​α2​(κ−κ^)α2​(κ−κ^)−mσ​(α2​N​[κ−κ^]N−α2​(κ−κ^)mσ​[mσ]N)\displaystyle\hskip 82.51282pt+\frac{C\_{4}\alpha^{2}(\kappa-\hat{\kappa})}{\alpha^{2}(\kappa-\hat{\kappa})-m\_{\sigma}}\left({\alpha^{2N}\left[\kappa-\hat{\kappa}\right]^{N}-\frac{\alpha^{2}(\kappa-\hat{\kappa})}{m\_{\sigma}}\left[m\_{\sigma}\right]^{N}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +C5​κ~​(κ−κ^)κ~​(κ−κ^)−mσ​(κ~−1)​(αN​[κ−κ^]N−κ−κ^mσ​αN​(κ~−1κ~)N−1​[mσ]N)\displaystyle\hskip 82.51282pt+\frac{C\_{5}\tilde{\kappa}(\kappa-\hat{\kappa})}{\tilde{\kappa}(\kappa-\hat{\kappa})-m\_{\sigma}\left({\tilde{\kappa}-1}\right)}\left({\alpha^{N}\left[\kappa-\hat{\kappa}\right]^{N}-\frac{\kappa-\hat{\kappa}}{m\_{\sigma}}\alpha^{N}\left({\frac{\tilde{\kappa}-1}{\tilde{\kappa}}}\right)^{N-1}\left[m\_{\sigma}\right]^{N}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(n−2)​α2​(κ−κ^)(κ~−α​(κ~−1))​(α​(κ−κ^)−mσ)(αN[κ−κ^]N−α​(κ−κ^)mσ[mσ]N)\bBigg@3.3].\displaystyle\hskip 82.51282pt+\frac{\left({n-2}\right)\alpha^{2}(\kappa-\hat{\kappa})}{\left({\tilde{\kappa}-\alpha\left({\tilde{\kappa}-1}\right)}\right)\left({\alpha(\kappa-\hat{\kappa})-m\_{\sigma}}\right)}\left({\alpha^{N}\left[\kappa-\hat{\kappa}\right]^{N}-\frac{\alpha(\kappa-\hat{\kappa})}{m\_{\sigma}}\left[m\_{\sigma}\right]^{N}}\right)\bBigg@{3.3}]. |  |

Finally,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=2NG3i\displaystyle{\sum\_{i=2}^{N}G^{i}\_{3}} | =C1∑σ∈{+,−}cσ​κmσ\bBigg@3.3[C6\bBigg@3((1−α)​κ~​mσmσ−α​κ(α[mσ]N−αN​mσκ[κ]N)\displaystyle=C\_{1}\sum\_{\sigma\in\{+,-\}}\frac{c\_{\sigma}\kappa}{m\_{\sigma}}\bBigg@{3.3}[C\_{6}\bBigg@{3}(\frac{\left({1-\alpha}\right)\tilde{\kappa}m\_{\sigma}}{m\_{\sigma}-\alpha\kappa}\left({\alpha\left[m\_{\sigma}\right]^{N}-\frac{\alpha^{N}m\_{\sigma}}{\kappa}[\kappa]^{N}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +α​mσ​κ~mσ​κ~−κ​α2​(κ~−1)(α2​(κ~−1)κ~[mσ]N−(α2​(κ~−1)κ~)Nmσκ[κ]N)\bBigg@3)\displaystyle\hskip 91.04872pt+\frac{\alpha m\_{\sigma}\tilde{\kappa}}{m\_{\sigma}\tilde{\kappa}-\kappa\alpha^{2}\left({\tilde{\kappa}-1}\right)}\left({\frac{\alpha^{2}\left({\tilde{\kappa}-1}\right)}{\tilde{\kappa}}\left[m\_{\sigma}\right]^{N}-\left({\frac{\alpha^{2}\left({\tilde{\kappa}-1}\right)}{\tilde{\kappa}}}\right)^{N}\frac{m\_{\sigma}}{\kappa}[\kappa]^{N}}\right)\bBigg@{3}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +C4​mσmσ−κ​(αN+1​[mσ]N−mσκ​αN+1​[κ]N)\displaystyle\hskip 71.13188pt+\frac{C\_{4}m\_{\sigma}}{m\_{\sigma}-\kappa}\left({\alpha^{N+1}\left[m\_{\sigma}\right]^{N}-\frac{m\_{\sigma}}{\kappa}\alpha^{N+1}[\kappa]^{N}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +C5​α​κ~​mσκ~​mσ−κ​α2​(κ~−1)​([mσ]N−(α2​(κ~−1)κ~)N−1​mσκ​[κ]N)\displaystyle\hskip 71.13188pt+C\_{5}\frac{\alpha\tilde{\kappa}m\_{\sigma}}{\tilde{\kappa}m\_{\sigma}-\kappa\alpha^{2}\left({\tilde{\kappa}-1}\right)}\left({\left[m\_{\sigma}\right]^{N}-\left({\frac{\alpha^{2}\left({\tilde{\kappa}-1}\right)}{\tilde{\kappa}}}\right)^{N-1}\frac{m\_{\sigma}}{\kappa}[\kappa]^{N}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(n−2)​ακ~−α​(κ~−1)mσmσ−α​κ(α[mσ]N−mσκαN[κ]N)\bBigg@3.3].\displaystyle\hskip 71.13188pt+\frac{\left({n-2}\right)\alpha}{\tilde{\kappa}-\alpha\left({\tilde{\kappa}-1}\right)}\frac{m\_{\sigma}}{m\_{\sigma}-\alpha\kappa}\left({\alpha\left[m\_{\sigma}\right]^{N}-\frac{m\_{\sigma}}{\kappa}\alpha^{N}[\kappa]^{N}}\right)\bBigg@{3.3}]. |  |

Again, Lemma [C.5](https://arxiv.org/html/2512.11765v1#A3.Thmtheorem5 "Lemma C.5. ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") and [[19](https://arxiv.org/html/2512.11765v1#bib.bib19), Lemma A.3] yield all necessary limits, and therefore

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝎⊤​(κ^​Γ~−Γ~⊤)​𝝂\displaystyle{\bm{\omega}}^{\top}(\left.\hat{\kappa}\tilde{\Gamma}-\tilde{\Gamma}^{\top}\right.){\bm{\nu}} | =(𝝎⊤​(κ^​Γ~−Γ~⊤))1​ν1+∑k=13∑i=2NGki+(𝝎⊤​(κ^​Γ~−Γ~⊤))N+1​νN+1\displaystyle=({\bm{\omega}}^{\top}(\left.\hat{\kappa}\tilde{\Gamma}-\tilde{\Gamma}^{\top}\right.))\_{1}{\nu\_{1}}+\sum\_{k=1}^{3}\sum\_{i=2}^{N}G^{i}\_{k}+({\bm{\omega}}^{\top}(\left.\hat{\kappa}\tilde{\Gamma}-\tilde{\Gamma}^{\top}\right.))\_{N+1}{\nu\_{N+1}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | →(n−1)2​(n+e−ρ​n+1n−1​T)n​κ​(n+1)+\bBigg@3.3((n+1)​n​κ​(1+(n−2)​ρ​T−e−ρ​n+1n−1​T)(n+1)2​n​κ\displaystyle\to\frac{\left({n-1}\right)^{2}\left({n+e^{-\rho\frac{n+1}{n-1}T}}\right)}{n\kappa(n+1)}+\bBigg@{3.3}(\frac{(n+1)n\kappa\left({1+(n-2)\rho T-e^{-\rho\frac{n+1}{n-1}T}}\right)}{(n+1)^{2}n\kappa} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(n+1)​(κ−κ^)​(n​(n−1)+(n−1)​e−ρ​n+1n−1​T)+2​(n−2)​n​κ​(1−e−ρ​n+1n−1​T)(n+1)2​n​κ\bBigg@3.3)+0\displaystyle+\frac{(n+1)(\kappa-\hat{\kappa})\left({n(n-1)+(n-1)e^{-\rho\frac{n+1}{n-1}T}}\right)+2(n-2)n\kappa\left({1-e^{-\rho\frac{n+1}{n-1}T}}\right)}{(n+1)^{2}n\kappa}\bBigg@{3.3})+0 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−(n−1)​(2​n−1)​e−ρ​n+1n−1​T+n​(n+4)​(n−1)+n​(n+1)​(n−2)​ρ​Tn​(n+1)2.\displaystyle=\frac{-(n-1)(2n-1)e^{-\rho\frac{n+1}{n-1}T}+n(n+4)(n-1)+n(n+1)(n-2)\rho T}{n(n+1)^{2}}. |  |

∎

Before proving Theorem [4.2](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem2 "Theorem 4.2 (Convergence of costs for 𝜃>0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"), we recall that vkv\_{k} corresponds to the kk-th element of the vector 𝒗=(v1,…,vN+1)∈ℝN+1\bm{v}=(v\_{1},\dots,v\_{N+1})\in\mathbb{R}^{N+1}, whereas ξk\xi\_{k} corresponds to the (k+1)(k+1)-th element of the vector 𝝃=(ξ0,…,ξN)∈ℝN+1\bm{\xi}=(\xi\_{0},\dots,\xi\_{N})\in\mathbb{R}^{N+1}.

###### Proof of Theorem [4.2](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem2 "Theorem 4.2 (Convergence of costs for 𝜃>0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact").

By [[19](https://arxiv.org/html/2512.11765v1#bib.bib19), (23)] we have

|  |  |  |  |
| --- | --- | --- | --- |
| (C.18) |  | 𝟏⊤​𝝎=∑i=1N+1ωi⟶ρ​T+1as ​N↑∞.\mathbf{1}^{\top}{\bm{\omega}}=\sum\_{i=1}^{N+1}\omega\_{i}\longrightarrow\rho T+1\quad\text{as }N\uparrow\infty. |  |

Moreover, the limit of 𝟏⊤​𝝂=∑i=1N+1νi\mathbf{1}^{\top}{\bm{\nu}}=\sum\_{i=1}^{N+1}\nu\_{i} is given by ([C.5](https://arxiv.org/html/2512.11765v1#A3.E5 "In C.2.1. Proof for 𝜅=𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) when κ=n−1\kappa=n-1, and by ([C.15](https://arxiv.org/html/2512.11765v1#A3.E15 "In C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) when κ≠n−1\kappa\neq n-1 with κ>n−12\kappa>\frac{n-1}{2}. The limits of 𝝂⊤​Γ~​𝝂{\bm{\nu}}^{\top}\tilde{\Gamma}{\bm{\nu}}, 𝝎⊤​(κ^​Γ~−Γ~⊤)​𝝂{\bm{\omega}}^{\top}(\hat{\kappa}{\tilde{\Gamma}-\tilde{\Gamma}^{\top}}){\bm{\nu}}, and 𝝎⊤​Γ~​𝝎{\bm{\omega}}^{\top}\tilde{\Gamma}{\bm{\omega}} are collected in Lemma [C.7](https://arxiv.org/html/2512.11765v1#A3.Thmtheorem7 "Lemma C.7. ‣ C.3. Proof of Theorem 4.2 ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"). Substituting these into ([C.16](https://arxiv.org/html/2512.11765v1#A3.E16 "In Lemma C.6. ‣ C.3. Proof of Theorem 4.2 ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) yields the claim.
Finally, we only need to prove ([4.4](https://arxiv.org/html/2512.11765v1#S4.E4 "In Theorem 4.2 (Convergence of costs for 𝜃>0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")), then ([4.5](https://arxiv.org/html/2512.11765v1#S4.E5 "In Theorem 4.2 (Convergence of costs for 𝜃>0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) will follow automatically; recall

|  |  |  |
| --- | --- | --- |
|  | ξi,k=x¯​vk+(xi−x¯)​wk,\xi\_{i,k}=\bar{x}v\_{k}+(x\_{i}-\bar{x})w\_{k}, |  |

where 𝒘\bm{w} and 𝒗\bm{v} are defined in ([A.2](https://arxiv.org/html/2512.11765v1#A1.E2 "In Appendix A Closed Form of the Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")). Without loss of generality, and to simplify explicit computations, we can fix c=1/2c=1/2; the same argument remains valid replacing 1/21/2 with any c∈(0,1)c\in(0,1).

*Step 1: Back window [⌈N/2⌉,…,N][\lceil{N}/{2}\rceil,\dots,N], recovery of ℬT\mathscr{B}\_{T}.*

Near t=Tt=T the 𝒘\bm{w}-contribution dominates, hence (recall the indexing convention for 𝝃\bm{\xi} is {0,…,N}\{0,\dots,N\} and for 𝒗\bm{v} and 𝒘\bm{w} is {1,…,N+1}\{1,\dots,N+1\})

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ​∑k=⌈N/2⌉N(ξi,k)2\displaystyle\theta\sum\_{k=\lceil N/2\rceil}^{N}\bigl(\xi\_{i,k}\bigr)^{2} | =θ​x¯2​∑k=⌈N/2⌉+1N+1vk2+2​θ​x¯​(xi−x¯)​∑k=⌈N/2⌉+1N+1vk​wk+θ​(xi−x¯)2​∑k=⌈N/2⌉+1N+1wk2\displaystyle=\theta\bar{x}^{2}\sum\_{k=\lceil N/2\rceil+1}^{N+1}v\_{k}^{2}+2\theta\bar{x}\bigl(x\_{i}-\bar{x}\bigr)\sum\_{k=\lceil N/2\rceil+1}^{N+1}v\_{k}w\_{k}+\theta\bigl(x\_{i}-\bar{x}\bigr)^{2}\sum\_{k=\lceil N/2\rceil+1}^{N+1}w\_{k}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =θ​(xi−x¯)2​∑k=⌈N/2⌉+1N+1wk2+o​(1)⟶ℬT(N→∞).\displaystyle=\theta\bigl(x\_{i}-\bar{x}\bigr)^{2}\sum\_{k=\lceil N/2\rceil+1}^{N+1}w\_{k}^{2}+o(1)\longrightarrow\mathscr{B}\_{T}\qquad(N\to\infty). |  |

Using the explicit formula in ([A.11](https://arxiv.org/html/2512.11765v1#A1.E11 "In Theorem A.4 (Explicit form of 𝝎 and 𝝂). ‣ Appendix A Closed Form of the Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")),

|  |  |  |
| --- | --- | --- |
|  | ∑k=⌈N/2⌉+1N+1ωk2⟶12​κ~−1=14​θ,\sum\_{k=\lceil N/2\rceil+1}^{N+1}\omega\_{k}^{2}\ \longrightarrow\ \frac{1}{2\tilde{\kappa}-1}=\frac{1}{4\theta}, |  |

and, combining this with ([C.18](https://arxiv.org/html/2512.11765v1#A3.E18 "In C.3. Proof of Theorem 4.2 ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")),

|  |  |  |
| --- | --- | --- |
|  | ∑k=⌈N/2⌉+1N+1wk2⟶14​θ​(ρ​T+1)2.\sum\_{k=\lceil N/2\rceil+1}^{N+1}w\_{k}^{2}\ \longrightarrow\ \frac{1}{4\theta(\rho T+1)^{2}}. |  |

To see that the 𝒗\bm{v}-part and the cross term vanish as N→∞N\to\infty, first consider κ=n−1\kappa=n-1: by ([C.4](https://arxiv.org/html/2512.11765v1#A3.E4 "In C.2.1. Proof for 𝜅=𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")),

|  |  |  |
| --- | --- | --- |
|  | νi2≤ρ2​T2(n−1)2​1N2+o​(1N2),i∈{⌈N2⌉+1,…,N+1}.\nu\_{i}^{2}\leq\frac{\rho^{2}T^{2}}{(n-1)^{2}}\frac{1}{N^{2}}+o\left(\frac{1}{N^{2}}\right),\qquad i\in\Bigl\{\bigl\lceil\tfrac{N}{2}\bigr\rceil+1,\dots,N+1\Bigr\}. |  |

For κ≠n−1\kappa\neq n-1, ([C.11](https://arxiv.org/html/2512.11765v1#A3.E11 "In C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) and ([C.13](https://arxiv.org/html/2512.11765v1#A3.E13 "In C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) yield, for i∈{⌈N/2⌉+1,…,N}i\in\{\lceil N/2\rceil+1,\dots,N\},

|  |  |  |
| --- | --- | --- |
|  | νi2≤ρ2​T2​(2(n+1)​(n−1)​eρ​T​n+1n−1+1n+1)2​1N2+o​(1N2),νN+12≤ρ2​T2(n−1)2​1N2+o​(1N2).\nu\_{i}^{2}\leq\rho^{2}T^{2}\Bigl(\frac{2}{(n+1)(n-1)}e^{\rho T\frac{n+1}{n-1}}+\frac{1}{n+1}\Bigr)^{2}\frac{1}{N^{2}}+o\left(\frac{1}{N^{2}}\right),\qquad\nu\_{N+1}^{2}\leq\frac{\rho^{2}T^{2}}{(n-1)^{2}}\frac{1}{N^{2}}+o\left(\frac{1}{N^{2}}\right). |  |

Together with the limit of 𝟏⊤​𝝂\mathbf{1}^{\top}\bm{\nu} (from ([C.5](https://arxiv.org/html/2512.11765v1#A3.E5 "In C.2.1. Proof for 𝜅=𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) or ([C.15](https://arxiv.org/html/2512.11765v1#A3.E15 "In C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"))), this implies

|  |  |  |
| --- | --- | --- |
|  | ∑k=⌈N/2⌉+1N+1vk2=𝒪​(1N),for any ​κ>n−12.\sum\_{k=\lceil N/2\rceil+1}^{N+1}v\_{k}^{2}=\mathcal{O}\left(\frac{1}{N}\right),\qquad\text{for any }\kappa>\frac{n-1}{2}. |  |

By Cauchy–Schwarz,

|  |  |  |
| --- | --- | --- |
|  | |∑k=⌈N/2⌉+1N+1vk​wk|≤(∑k=⌈N/2⌉+1N+1vk2)1/2​(∑k=⌈N/2⌉+1N+1wk2)1/2→N→∞0.\Bigl|\sum\_{k=\lceil N/2\rceil+1}^{N+1}v\_{k}w\_{k}\Bigr|\leq\Bigl(\sum\_{k=\lceil N/2\rceil+1}^{N+1}v\_{k}^{2}\Bigr)^{1/2}\Bigl(\sum\_{k=\lceil N/2\rceil+1}^{N+1}w\_{k}^{2}\Bigr)^{1/2}\xrightarrow[N\to\infty]{}0. |  |

Hence the limit over the back half equals ℬT\mathscr{B}\_{T}.

*Step 2: Front window [0,…,⌈N/2⌉−1][0,\dots,\lceil{N}/{2}\rceil-1], recovery of ℬ0\mathscr{B}\_{0}.*

Near t=0t=0 the 𝒗\bm{v}-contribution dominates, so

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ​∑k=0⌈N/2⌉−1(ξi,k)2\displaystyle\theta\sum\_{k=0}^{\lceil N/2\rceil-1}\bigl(\xi\_{i,k}\bigr)^{2} | =θ​x¯2​∑k=1⌈N/2⌉vk2+2​θ​x¯​(xi−x¯)​∑k=1⌈N/2⌉vk​wk+θ​(xi−x¯)2​∑k=1⌈N/2⌉wk2\displaystyle=\theta\bar{x}^{2}\sum\_{k=1}^{\lceil N/2\rceil}v\_{k}^{2}+2\theta\bar{x}\bigl(x\_{i}-\bar{x}\bigr)\sum\_{k=1}^{\lceil N/2\rceil}v\_{k}w\_{k}+\theta\bigl(x\_{i}-\bar{x}\bigr)^{2}\sum\_{k=1}^{\lceil N/2\rceil}w\_{k}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =θ​x¯2​∑k=1⌈N/2⌉vk2+o​(1).\displaystyle=\theta\bar{x}^{2}\sum\_{k=1}^{\lceil N/2\rceil}v\_{k}^{2}+o(1). |  |

Using ([C.12](https://arxiv.org/html/2512.11765v1#A3.E12 "In C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"))-([C.11](https://arxiv.org/html/2512.11765v1#A3.E11 "In C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) for κ≠n−1\kappa\neq n-1 and ([C.4](https://arxiv.org/html/2512.11765v1#A3.E4 "In C.2.1. Proof for 𝜅=𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) for κ=n−1\kappa=n-1 (in the latter case θ=n−14\theta=\tfrac{n-1}{4} and only the first trade contributes, meaning ∑k=2⌈N/2⌉νk2→0\sum\_{k=2}^{\lceil N/2\rceil}\nu\_{k}^{2}\to 0),

|  |  |  |
| --- | --- | --- |
|  | ∑k=1⌈N/2⌉νk2⟶(n−1)​e−2​ρ​T​n+1n−1​(n​eρ​T​n+1n−1+1)2(n+1)2​n2​4​θ.\sum\_{k=1}^{\lceil N/2\rceil}\nu\_{k}^{2}\ \longrightarrow\ \frac{(n-1)e^{-2\rho T\frac{n+1}{n-1}}\Bigl(ne^{\rho T\frac{n+1}{n-1}}+1\Bigr)^{2}}{(n+1)^{2}n^{2}4\theta}. |  |

Therefore, combining with the limit in ([C.15](https://arxiv.org/html/2512.11765v1#A3.E15 "In C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) (that does not depend on θ\theta), we get, for any θ>0\theta>0,

|  |  |  |
| --- | --- | --- |
|  | ∑k=1⌈N/2⌉vk2⟶(n−1)​(n+1)2​(1+n​eρ​n+1n−1​T)24​θ​(n​((ρ​T+1)​(n+1)+2)​eρ​n+1n−1​T−(n−1))2.\sum\_{k=1}^{\lceil N/2\rceil}v\_{k}^{2}\ \longrightarrow\ \frac{(n-1)(n+1)^{2}\Bigl(1+ne^{\rho\frac{n+1}{n-1}T}\Bigr)^{2}}{4\theta\Bigl(n\bigl((\rho T+1)(n+1)+2\bigr)e^{\rho\frac{n+1}{n-1}T}-(n-1)\Bigr)^{2}}. |  |

To show that the 𝒘\bm{w}-part and the cross term vanish, note from ([A.11](https://arxiv.org/html/2512.11765v1#A1.E11 "In Theorem A.4 (Explicit form of 𝝎 and 𝝂). ‣ Appendix A Closed Form of the Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) that, for i∈{1,…,⌈N/2⌉}i\in\{1,\dots,\lceil N/2\rceil\},

|  |  |  |
| --- | --- | --- |
|  | ωi2≤4​ρ2​T2​1N2+o​(1N2).\omega\_{i}^{2}\leq 4\rho^{2}T^{2}\frac{1}{N^{2}}+o\left(\frac{1}{N^{2}}\right). |  |

By ([C.18](https://arxiv.org/html/2512.11765v1#A3.E18 "In C.3. Proof of Theorem 4.2 ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")), we conclude as in Step 1.
∎

### C.4. Proof of Theorem [4.3](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem3 "Theorem 4.3 (Divergence of strategies for 𝜃=0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") [(a)](https://arxiv.org/html/2512.11765v1#S4.I2.i1 "item (a) ‣ Theorem 4.3 (Divergence of strategies for 𝜃=0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")

###### Proof of Theorem [4.3](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem3 "Theorem 4.3 (Divergence of strategies for 𝜃=0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") [(a)](https://arxiv.org/html/2512.11765v1#S4.I2.i1 "item (a) ‣ Theorem 4.3 (Divergence of strategies for 𝜃=0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact").

For κ=n−12\kappa=\frac{n-1}{2}, the limits in ([C.7](https://arxiv.org/html/2512.11765v1#A3.E7 "In Lemma C.4. ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) and ([C.8](https://arxiv.org/html/2512.11765v1#A3.E8 "In Lemma C.4. ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) follow from Lemma [C.5](https://arxiv.org/html/2512.11765v1#A3.Thmtheorem5 "Lemma C.5. ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact").
We evaluate ([C.7](https://arxiv.org/html/2512.11765v1#A3.E7 "In Lemma C.4. ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) with m=ntm=n\_{t} term-by-term as N↑∞N\uparrow\infty.

1. 1.

   |  |  |  |
   | --- | --- | --- |
   |  | ∑σ∈{+,−}dσ​(mσ−α2​κ)mσ−α​κ​[mσ]N⟶{2​n(e−2​n+1n−1​ρ​T+n)​(n+1),N=2​k,2​n(−e−2​n+1n−1​ρ​T+n)​(n+1),N=2​k+1.\sum\_{\sigma\in\{+,-\}}\frac{d\_{\sigma}\left(m\_{\sigma}-\alpha^{2}\kappa\right)}{m\_{\sigma}-\alpha\kappa}[m\_{\sigma}]^{N}\longrightarrow\begin{cases}\displaystyle\frac{2n}{\left(e^{-2\frac{n+1}{n-1}\rho T}+n\right)(n+1)},&N=2k,\\[6.0pt] \displaystyle\frac{2n}{\left(-e^{-2\frac{n+1}{n-1}\rho T}+n\right)(n+1)},&N=2k+1.\end{cases} |  |
2. 2.

   |  |  |  |
   | --- | --- | --- |
   |  | (1−α)​(nt−1)​∑σ∈{+,−}cσ​dσ​(α​(κ−κ^)mσ−α​(κ−κ^)+mσmσ−α​κ)​[mσ]N⟶{ρ​tn+1,N=2​k,ρ​tn+1,N=2​k+1.\left(1-\alpha\right)\left(n\_{t}-1\right)\sum\_{\sigma\in\{+,-\}}c\_{\sigma}d\_{\sigma}\left(\frac{\alpha(\kappa-\hat{\kappa})}{m\_{\sigma}-\alpha(\kappa-\hat{\kappa})}+\frac{m\_{\sigma}}{m\_{\sigma}-\alpha\kappa}\right)[m\_{\sigma}]^{N}\longrightarrow\begin{cases}\displaystyle\frac{\rho t}{n+1},&N=2k,\\[6.0pt] \displaystyle\frac{\rho t}{n+1},&N=2k+1.\end{cases} |  |
3. 3.

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | C1​(1+∑σ∈{+,−}cσ​mσ​((mσα​κ)nt−1−1)mσ−α​κ)​αN​[κ]N\displaystyle C\_{1}\left(1+\sum\_{\sigma\in\{+,-\}}\frac{c\_{\sigma}m\_{\sigma}\Big(\big(\frac{m\_{\sigma}}{\alpha\kappa}\big)^{n\_{t}-1}-1\Big)}{m\_{\sigma}-\alpha\kappa}\right)\alpha^{N}[\kappa]^{N} |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | ⟶{e−ρ​n+1n−1​T(e−2​n+1n−1​ρ​T+n)​(n+1)2​(2​n​eρ​n+1n−1​t−(n+1)​(±e−ρ​n+1n−1​t)−(n−1)),N=2​k,e−ρ​n+1n−1​T(−e−2​n+1n−1​ρ​T+n)​(n+1)2​(2​n​eρ​n+1n−1​t−(n+1)​(±e−ρ​n+1n−1​t)−(n−1)),N=2​k+1.\displaystyle\qquad\longrightarrow |  |
4. 4.

   Define

   |  |  |  |
   | --- | --- | --- |
   |  | D+:=(ne2​n+1n−1​ρ​T+1)(n+1)2,D−:=(ne2​n+1n−1​ρ​T−1)(n+1)2.D\_{+}\mathrel{\mathop{\ordinarycolon}}=\left(ne^{2\frac{n+1}{n-1}\rho T}+1\right)(n+1)^{2},\qquad D\_{-}\mathrel{\mathop{\ordinarycolon}}=\left(ne^{2\frac{n+1}{n-1}\rho T}-1\right)(n+1)^{2}. |  |

   Then

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | n​C1​∑σ∈{+,−}dσ​mσ​(α​(κ−κ^)mσ−(α​(κ−κ^)mσ)nt)mσ−α​(κ−κ^)​[mσ]N\displaystyle nC\_{1}\sum\_{\sigma\in\{+,-\}}\frac{d\_{\sigma}m\_{\sigma}\left(\frac{\alpha(\kappa-\hat{\kappa})}{m\_{\sigma}}-\left(\frac{\alpha(\kappa-\hat{\kappa})}{m\_{\sigma}}\right)^{n\_{t}}\right)}{m\_{\sigma}-\alpha(\kappa-\hat{\kappa})}[m\_{\sigma}]^{N} |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | ⟶{2​n−2​n​eρ​n+1n−1​t−n​(n+1)​e2​n+1n−1​ρ​T​(1±e−ρ​n+1n−1​t)D+,N=2​k,−2​n+2​n​eρ​n+1n−1​t−n​(n+1)​e2​n+1n−1​ρ​T​(1±e−ρ​n+1n−1​t)D−,N=2​k+1.\displaystyle\qquad\longrightarrow |  |

Summing the four contributions yields the limit

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∑i=1ntνi\displaystyle\sum\_{i=1}^{n\_{t}}\nu\_{i} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⟶{2​n+(n+1)​ρ​t−2​n​eρ​n+1n−1​t+e2​n+1n−1​ρ​T​(n​(n+1)+n​(n+1)​ρ​t)−en+1n−1​ρ​(2​T−t)​(±n​(n+1))D++2​n​en+1n−1​ρ​(T+t)−en+1n−1​ρ​(T−t)​(±(n+1))−(n−1)​en+1n−1​ρ​TD+,N=2​k,−2​n−(n+1)​ρ​t+2​n​eρ​n+1n−1​t+e2​n+1n−1​ρ​T​(n​(n+1)+n​(n+1)​ρ​t)−en+1n−1​ρ​(2​T−t)​(±n​(n+1))D−+2​n​en+1n−1​ρ​(T+t)−en+1n−1​ρ​(T−t)​(±(n+1))−(n−1)​en+1n−1​ρ​TD−,N=2​k+1.\displaystyle\qquad\longrightarrow |  |

Setting t=Tt=T in the preceding display gives the limit

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∑i=1Nνi\displaystyle\sum\_{i=1}^{N}\nu\_{i} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ⟶{n​e2​n+1n−1​ρ​T​((n+3)+(n+1)​ρ​T)+en+1n−1​ρ​T​(1−4​n−n2)+(n+1)​ρ​T+(n−1)D+,N=2​k,n​e2​n+1n−1​ρ​T​((n+3)+(n+1)​ρ​T)+en+1n−1​ρ​T​(1+2​n+n2)−(n+1)​ρ​T−(n−1)D−,N=2​k+1.\displaystyle\qquad\longrightarrow |  |

Turning to νN+1\nu\_{N+1}, ([C.8](https://arxiv.org/html/2512.11765v1#A3.E8 "In Lemma C.4. ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) yields

|  |  |  |
| --- | --- | --- |
|  | νN+1⟶{2​(n+1)+2​n​(n+1)​en+1n−1​ρ​TD+,N=2​k,−2​(n+1)−2​n​(n+1)​en+1n−1​ρ​TD−,N=2​k+1.\nu\_{N+1}\longrightarrow\begin{cases}\displaystyle\frac{2(n+1)+2n(n+1)e^{\frac{n+1}{n-1}\rho T}}{D\_{+}},&N=2k,\\[8.0pt] \displaystyle\frac{-2(n+1)-2n(n+1)e^{\frac{n+1}{n-1}\rho T}}{D\_{-}},&N=2k+1.\end{cases} |  |

Combining the preceding two displays yields the limits of 𝟏⊤​𝝂\mathbf{1}^{\top}{\bm{\nu}}:

|  |  |  |  |
| --- | --- | --- | --- |
| (C.19) |  | limN↑∞N​even𝟏⊤​𝝂=n​e2​n+1n−1​ρ​T​((n+1)​ρ​T+(n+3))+(n−1)2​en+1n−1​ρ​T+(n+1)​ρ​T+(3​n+1)D+,limN↑∞N​odd𝟏⊤​𝝂=n​e2​n+1n−1​ρ​T​((n+1)​ρ​T+(n+3))+(1−n2)​en+1n−1​ρ​T−(n+1)​ρ​T−(3​n+1)D−.\begin{split}\lim\_{\begin{subarray}{c}N\uparrow\infty\\ N\mathrm{even}\end{subarray}}\mathbf{1}^{\top}{\bm{\nu}}&=\frac{ne^{2\frac{n+1}{n-1}\rho T}\left((n+1)\rho T+(n+3)\right)+(n-1)^{2}e^{\frac{n+1}{n-1}\rho T}+(n+1)\rho T+(3n+1)}{D\_{+}},\\ \lim\_{\begin{subarray}{c}N\uparrow\infty\\ N\mathrm{odd}\end{subarray}}\mathbf{1}^{\top}{\bm{\nu}}&=\frac{ne^{2\frac{n+1}{n-1}\rho T}\left((n+1)\rho T+(n+3)\right)+(1-n^{2})e^{\frac{n+1}{n-1}\rho T}-(n+1)\rho T-(3n+1)}{D\_{-}}.\end{split} |  |

Finally, substituting these limits into the definition of Vt(N)V\_{t}^{(N)} completes the proof of the oscillation statement in part [(a)](https://arxiv.org/html/2512.11765v1#S4.I2.i1 "item (a) ‣ Theorem 4.3 (Divergence of strategies for 𝜃=0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact").
∎

### C.5. Proof of Theorem [4.3](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem3 "Theorem 4.3 (Divergence of strategies for 𝜃=0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") [(b)](https://arxiv.org/html/2512.11765v1#S4.I2.i2 "item (b) ‣ Theorem 4.3 (Divergence of strategies for 𝜃=0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")

###### Proof of Theorem [4.3](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem3 "Theorem 4.3 (Divergence of strategies for 𝜃=0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") [(b)](https://arxiv.org/html/2512.11765v1#S4.I2.i2 "item (b) ‣ Theorem 4.3 (Divergence of strategies for 𝜃=0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact").

By Remark [2.4](https://arxiv.org/html/2512.11765v1#S2.Thmtheorem4 "Remark 2.4. ‣ 2.2. Nash Equilibrium ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"), W(N)W^{\left({N}\right)} is independent of nn. Hence the argument of [[19](https://arxiv.org/html/2512.11765v1#bib.bib19), Theorem 3.1(d)], established for n=2n=2, applies analogously in our setting for any t∈(0,T)t\in(0,T). For t=0t=0 and t=Tt=T a straightforward limit computation yields the result.
∎

### C.6. Proof of Theorem [4.4](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem4 "Theorem 4.4 (Divergence of costs for 𝜃=0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")

###### Lemma C.8.

Let κ=n−12\kappa=\frac{n-1}{2}. Then, as N↑∞N\uparrow\infty,

|  |  |  |  |
| --- | --- | --- | --- |
|  | limN↑∞N​even𝝂⊤​Γ~​𝝂\displaystyle\lim\_{\begin{subarray}{c}N\uparrow\infty\\ N\mathrm{even}\end{subarray}}{\bm{\nu}}^{\top}\tilde{\Gamma}{\bm{\nu}} | =n​e2​ρ​n+1n−1​T​((n+1)​ρ​T+n+3)+(n−1)2​eρ​n+1n−1​T+(n+1)​ρ​T+3​n+1(n+1)​D+,\displaystyle=\frac{ne^{2\rho\frac{n+1}{n-1}T}\left({(n+1)\rho T+n+3}\right)+(n-1)^{2}e^{\rho\frac{n+1}{n-1}T}+(n+1)\rho T+3n+1}{(n+1)D\_{+}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | limN↑∞N​even𝝎⊤​(κ^​Γ~−Γ~⊤)​𝝂\displaystyle\lim\_{\begin{subarray}{c}N\uparrow\infty\\ N\mathrm{even}\end{subarray}}{\bm{\omega}}^{\top}\left({\hat{\kappa}\tilde{\Gamma}-\tilde{\Gamma}^{\top}}\right){\bm{\nu}} | =n2​e2​ρ​n+1n−1​T−n​(n+1)​eρ​n+3n−1​T+(2​n2−3​n−1)​eρ​n+1n−1​T−(n+1)​e−ρ​T+3​n−2𝒟+\displaystyle=\frac{n^{2}e^{2\rho\frac{n+1}{n-1}T}-n(n+1)e^{\rho\frac{n+3}{n-1}T}+(2n^{2}-3n-1)e^{\rho\frac{n+1}{n-1}T}-(n+1)e^{-\rho T}+3n-2}{\mathscr{D}\_{+}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +ρ​T​(n−2)​(n​e2​ρ​n+1n−1​T+1)𝒟++2​n​(n−2)​(eρ​n+1n−1​T−1)2D+,\displaystyle\quad+\frac{\rho T\left({n-2}\right)\left({ne^{2\rho\frac{n+1}{n-1}T}+1}\right)}{\mathscr{D}\_{+}}+\frac{2n(n-2)\left({e^{\rho\frac{n+1}{n-1}T}-1}\right)^{2}}{D\_{+}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | limN↑∞N​even𝝎⊤​Γ~​𝝎\displaystyle\lim\_{\begin{subarray}{c}N\uparrow\infty\\ N\mathrm{even}\end{subarray}}{\bm{\omega}}^{\top}\tilde{\Gamma}{\bm{\omega}} | =e−ρ​T+ρ​T+1.\displaystyle=e^{-\rho T}+\rho T+1. |  |

Moreover,

|  |  |  |  |
| --- | --- | --- | --- |
|  | limN↑∞N​odd𝝂⊤​Γ~​𝝂\displaystyle\lim\_{\begin{subarray}{c}N\uparrow\infty\\ N\mathrm{odd}\end{subarray}}{\bm{\nu}}^{\top}\tilde{\Gamma}{\bm{\nu}} | =n​e2​ρ​n+1n−1​T​((n+1)​ρ​T+n+3)−(n2−1)​eρ​n+1n−1​T−(n+1)​ρ​T−(3​n+1)(n+1)​D−,\displaystyle=\frac{ne^{2\rho\frac{n+1}{n-1}T}\left({(n+1)\rho T+n+3}\right)-(n^{2}-1)e^{\rho\frac{n+1}{n-1}T}-(n+1)\rho T-(3n+1)}{(n+1)D\_{-}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | limN↑∞N​odd𝝎⊤​(κ^​Γ~−Γ~⊤)​𝝂\displaystyle\lim\_{\begin{subarray}{c}N\uparrow\infty\\ N\mathrm{odd}\end{subarray}}{\bm{\omega}}^{\top}\left({\hat{\kappa}\tilde{\Gamma}-\tilde{\Gamma}^{\top}}\right){\bm{\nu}} | =n2​e2​ρ​n+1n−1​T+n​(n+1)​eρ​n+3n−1​T−(2​n2−3​n+1)​eρ​n+1n−1​T−(n+1)​e−ρ​T−3​n+2𝒟−\displaystyle=\frac{n^{2}e^{2\rho\frac{n+1}{n-1}T}+n(n+1)e^{\rho\frac{n+3}{n-1}T}-(2n^{2}-3n+1)e^{\rho\frac{n+1}{n-1}T}-(n+1)e^{-\rho T}-3n+2}{\mathscr{D}\_{-}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +ρ​T​(n−2)​(n​e2​ρ​n+1n−1​T−1)𝒟−+2​n​(n−2)​(e2​ρ​n+1n−1​T−1)D−,\displaystyle\quad+\frac{\rho T\left({n-2}\right)\left({ne^{2\rho\frac{n+1}{n-1}T}-1}\right)}{\mathscr{D}\_{-}}+\frac{2n(n-2)\left({e^{2\rho\frac{n+1}{n-1}T}-1}\right)}{D\_{-}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | limN↑∞N​odd𝝎⊤​Γ~​𝝎\displaystyle\lim\_{\begin{subarray}{c}N\uparrow\infty\\ N\mathrm{odd}\end{subarray}}{\bm{\omega}}^{\top}\tilde{\Gamma}{\bm{\omega}} | =−e−ρ​T+ρ​T+1.\displaystyle=-e^{-\rho T}+\rho T+1. |  |

Here

|  |  |  |
| --- | --- | --- |
|  | D±:=(ne2​n+1n−1​ρ​T±1)(n+1)2,𝒟±:=D±(n+1).D\_{\pm}\mathrel{\mathop{\ordinarycolon}}=\left({ne^{2\frac{n+1}{n-1}\rho T}\pm 1}\right)(n+1)^{2},\qquad\mathscr{D}\_{\pm}\mathrel{\mathop{\ordinarycolon}}=\frac{D\_{\pm}}{(n+1)}. |  |

###### Proof.

Since 𝝎{\bm{\omega}} is independent of nn, the third limits coincide with the 22–player case and are given by [[19](https://arxiv.org/html/2512.11765v1#bib.bib19), Lemma A.6]. Hence it suffices to establish, for κ=n−12\kappa=\frac{n-1}{2}, the first two limits for NN even and odd. Moreover, as explained in the proof of Lemma [C.7](https://arxiv.org/html/2512.11765v1#A3.Thmtheorem7 "Lemma C.7. ‣ C.3. Proof of Theorem 4.2 ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"), the representations of

|  |  |  |
| --- | --- | --- |
|  | 𝝂⊤​Γ~​𝝂and𝝎⊤​(κ^​Γ~−Γ~⊤)​𝝂{\bm{\nu}}^{\top}\tilde{\Gamma}{\bm{\nu}}\quad\text{and}\quad{\bm{\omega}}^{\top}\left({\hat{\kappa}\tilde{\Gamma}-\tilde{\Gamma}^{\top}}\right){\bm{\nu}} |  |

obtained there for κ≠n−1\kappa\neq n-1 also hold for κ=n−12\kappa=\frac{n-1}{2}. Plugging in the limits from Lemma [C.5](https://arxiv.org/html/2512.11765v1#A3.Thmtheorem5 "Lemma C.5. ‣ C.2.2. Proof for 𝜅≠𝑛-1 ‣ C.2. Proof of Theorem 4.1 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") yields the claim. For completeness, we record the decomposition and limiting contributions used in the argument.

*Quadratic form in 𝛎{\bm{\nu}}*:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝂⊤​Γ~​𝝂\displaystyle{\bm{\nu}}^{\top}\tilde{\Gamma}{\bm{\nu}} | =ν1​(Γ~​𝝂)1+ν2​(Γ~​𝝂)2+∑k=14∑i=3NDki+νN+1​(Γ~​𝝂)N+1.\displaystyle=\nu\_{1}\bigl(\tilde{\Gamma}{\bm{\nu}}\bigr)\_{1}+\nu\_{2}\bigl(\tilde{\Gamma}{\bm{\nu}}\bigr)\_{2}+\sum\_{k=1}^{4}\sum\_{i=3}^{N}D\_{k}^{i}+\nu\_{N+1}\bigl(\tilde{\Gamma}{\bm{\nu}}\bigr)\_{N+1}. |  |

The boundary terms cancel asymptotically,

|  |  |  |
| --- | --- | --- |
|  | ν1​(Γ~​𝝂)1+ν2​(Γ~​𝝂)2⟶0.\nu\_{1}\bigl(\tilde{\Gamma}{\bm{\nu}}\bigr)\_{1}+\nu\_{2}\bigl(\tilde{\Gamma}{\bm{\nu}}\bigr)\_{2}\longrightarrow 0. |  |

For the interior contributions,

|  |  |  |
| --- | --- | --- |
|  | ∑k=13∑i=3NDki⟶{1(n+1)​D+[(ne2​ρ​n+1n−1​T+1)(n+1)ρT+((n2+4n−1)e2​ρ​n+1n−1​T−(n2+6n−3)eρ​n+1n−1​T+2(n−1))],N=2​k,1(n+1)​D−[(ne2​ρ​n+1n−1​T−1)(n+1)ρT+((n2+4n−1)e2​ρ​n+1n−1​T+(n+1)2eρ​n+1n−1​T−2(n−1))],N=2​k+1,\displaystyle\sum\_{k=1}^{3}\sum\_{i=3}^{N}D\_{k}^{i}\longrightarrow\begin{cases}\displaystyle\frac{1}{(n+1)D\_{+}}\Bigl[\left({ne^{2\rho\frac{n+1}{n-1}T}+1}\right)(n+1)\rho T\\[-2.0pt] \displaystyle\qquad\qquad\quad+\left({(n^{2}+4n-1)e^{2\rho\frac{n+1}{n-1}T}-(n^{2}+6n-3)e^{\rho\frac{n+1}{n-1}T}+2(n-1)}\right)\Bigr],&N=2k,\\[10.0pt] \displaystyle\frac{1}{(n+1)D\_{-}}\Bigl[\left({ne^{2\rho\frac{n+1}{n-1}T}-1}\right)(n+1)\rho T\\[-2.0pt] \displaystyle\qquad\qquad\quad+\left({(n^{2}+4n-1)e^{2\rho\frac{n+1}{n-1}T}+(n+1)^{2}e^{\rho\frac{n+1}{n-1}T}-2(n-1)}\right)\Bigr],&N=2k+1,\end{cases} |  |

and

|  |  |  |
| --- | --- | --- |
|  | ∑i=3ND4i+νN+1​(Γ~​𝝂)N+1⟶{1(n+1)​D+[2(n2−1+2n)eρ​n+1n−1​T−(n−1)e2​ρ​n+1n−1​T+n+3],N=2​k,1(n+1)​D−[−2n(n+1)eρ​n+1n−1​T−(n−1)e2​ρ​n+1n−1​T−(n+3)],N=2​k+1.\displaystyle\sum\_{i=3}^{N}D\_{4}^{i}+\nu\_{N+1}\bigl(\tilde{\Gamma}{\bm{\nu}}\bigr)\_{N+1}\longrightarrow\begin{cases}\displaystyle\frac{1}{(n+1)D\_{+}}\Bigl[2(n^{2}-1+2n)e^{\rho\frac{n+1}{n-1}T}\\[-2.0pt] \displaystyle\qquad\qquad\quad\ -(n-1)e^{2\rho\frac{n+1}{n-1}T}+n+3\Bigr],&N=2k,\\[10.0pt] \displaystyle\frac{1}{(n+1)D\_{-}}\Bigl[-2n(n+1)e^{\rho\frac{n+1}{n-1}T}\\[-2.0pt] \displaystyle\qquad\qquad\quad\ -(n-1)e^{2\rho\frac{n+1}{n-1}T}-(n+3)\Bigr],&N=2k+1.\end{cases} |  |

Adding these two displays gives the limit for 𝝂⊤​Γ~​𝝂{\bm{\nu}}^{\top}\tilde{\Gamma}{\bm{\nu}}.

*Mixed form 𝛚⊤​(κ^​Γ~−Γ~⊤)​𝛎{\bm{\omega}}^{\top}\left({\hat{\kappa}\tilde{\Gamma}-\tilde{\Gamma}^{\top}}\right){\bm{\nu}}*:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝝎⊤​(κ^​Γ~−Γ~⊤)​𝝂\displaystyle{\bm{\omega}}^{\top}\left({\hat{\kappa}\tilde{\Gamma}-\tilde{\Gamma}^{\top}}\right){\bm{\nu}} | =(𝝎⊤​(κ^​Γ~−Γ~⊤))1​ν1+∑k=13∑i=2NGki+(𝝎⊤​(κ^​Γ~−Γ~⊤))N+1​νN+1.\displaystyle=\bigl({\bm{\omega}}^{\top}\left({\hat{\kappa}\tilde{\Gamma}-\tilde{\Gamma}^{\top}}\right)\bigr)\_{1}\nu\_{1}+\sum\_{k=1}^{3}\sum\_{i=2}^{N}G\_{k}^{i}+\bigl({\bm{\omega}}^{\top}\left({\hat{\kappa}\tilde{\Gamma}-\tilde{\Gamma}^{\top}}\right)\bigr)\_{N+1}\nu\_{N+1}. |  |

The boundary terms satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝝎⊤​(κ^​Γ~−Γ~⊤))1​ν1\displaystyle\bigl({\bm{\omega}}^{\top}\left({\hat{\kappa}\tilde{\Gamma}-\tilde{\Gamma}^{\top}}\right)\bigr)\_{1}\nu\_{1} | ⟶{2​(−e−ρ​T+n−1)​(n​e2​ρ​n+1n−1​T+eρ​n+1n−1​T)𝒟+,N=2​k,2​(e−ρ​T+n−1)​(n​e2​ρ​n+1n−1​T+eρ​n+1n−1​T)𝒟−,N=2​k+1,\displaystyle\longrightarrow\begin{cases}\displaystyle\frac{2\left({-e^{-\rho T}+n-1}\right)\left({ne^{2\rho\frac{n+1}{n-1}T}+e^{\rho\frac{n+1}{n-1}T}}\right)}{\mathscr{D}\_{+}},&N=2k,\\[8.0pt] \displaystyle\frac{2\left({e^{-\rho T}+n-1}\right)\left({ne^{2\rho\frac{n+1}{n-1}T}+e^{\rho\frac{n+1}{n-1}T}}\right)}{\mathscr{D}\_{-}},&N=2k+1,\end{cases} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝝎⊤​(κ^​Γ~−Γ~⊤))N+1​νN+1\displaystyle\bigl({\bm{\omega}}^{\top}\left({\hat{\kappa}\tilde{\Gamma}-\tilde{\Gamma}^{\top}}\right)\bigr)\_{N+1}\nu\_{N+1} | ⟶{2​(e−ρ​T−e−2​ρ​T+n−2)​(1+n​eρ​n+1n−1​T)𝒟+,N=2​k,−2​(e−ρ​T+e−2​ρ​T+n−2)​(1+n​eρ​n+1n−1​T)𝒟−,N=2​k+1.\displaystyle\longrightarrow\begin{cases}\displaystyle\frac{2\left({e^{-\rho T}-e^{-2\rho T}+n-2}\right)\left({1+ne^{\rho\frac{n+1}{n-1}T}}\right)}{\mathscr{D}\_{+}},&N=2k,\\[8.0pt] \displaystyle\frac{-2\left({e^{-\rho T}+e^{-2\rho T}+n-2}\right)\left({1+ne^{\rho\frac{n+1}{n-1}T}}\right)}{\mathscr{D}\_{-}},&N=2k+1.\end{cases} |  |

For the sums, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=2NG1i\displaystyle\sum\_{i=2}^{N}G\_{1}^{i} | ⟶{(1−e−ρ​T)2+(n−2)​ρ​Tn+1,N=2​k,1−e−2​ρ​T+(n−2)​ρ​Tn+1,N=2​k+1,\displaystyle\longrightarrow\begin{cases}\displaystyle\frac{\left({1-e^{-\rho T}}\right)^{2}+(n-2)\rho T}{n+1},&N=2k,\\[6.0pt] \displaystyle\frac{1-e^{-2\rho T}+(n-2)\rho T}{n+1},&N=2k+1,\end{cases} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=2NG2i\displaystyle\sum\_{i=2}^{N}G\_{2}^{i} | ⟶{n​(−2​e−ρ​T+2​e−2​ρ​T+1)​eρ​n+1n−1​T+n​(1−n+(2−n)​e−ρ​T)​e2​ρ​n+1n−1​T−n​(e−ρ​T−1)𝒟+−2​n​(n−2)D+​(eρ​n+1n−1​T−1),N=2​k,n​(2​e−ρ​T+2​e−2​ρ​T−1)​eρ​n+1n−1​T+n​(1−n+(n−2)​e−ρ​T)​e2​ρ​n+1n−1​T−n​(1+e−ρ​T)𝒟−+2​n​(n−2)D−​(eρ​n+1n−1​T−1),N=2​k+1,\displaystyle\longrightarrow\begin{cases}\displaystyle\frac{n\left({-2e^{-\rho T}+2e^{-2\rho T}+1}\right)e^{\rho\frac{n+1}{n-1}T}+n\left({1-n+(2-n)e^{-\rho T}}\right)e^{2\rho\frac{n+1}{n-1}T}-n\left({e^{-\rho T}-1}\right)}{\mathscr{D}\_{+}}\\[-2.0pt] \displaystyle\qquad-\frac{2n(n-2)}{D\_{+}}\left({e^{\rho\frac{n+1}{n-1}T}-1}\right),&\hskip-85.35826ptN=2k,\\[10.0pt] \displaystyle\frac{n\left({2e^{-\rho T}+2e^{-2\rho T}-1}\right)e^{\rho\frac{n+1}{n-1}T}+n\left({1-n+(n-2)e^{-\rho T}}\right)e^{2\rho\frac{n+1}{n-1}T}-n\left({1+e^{-\rho T}}\right)}{\mathscr{D}\_{-}}\\[-2.0pt] \displaystyle\qquad+\frac{2n(n-2)}{D\_{-}}\left({e^{\rho\frac{n+1}{n-1}T}-1}\right),&\hskip-85.35826ptN=2k+1,\end{cases} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=2NG3i\displaystyle\sum\_{i=2}^{N}G\_{3}^{i} | ⟶{(e−ρ​T−e−2​ρ​T)​n​e2​ρ​n+1n−1​T−(e−ρ​T−e−2​ρ​T−1)+2​e−ρ​T​eρ​n+1n−1​T−(2​n−1)​eρ​n+1n−1​T𝒟++2​n​(n−2)D+​eρ​n+1n−1​T​(eρ​n+1n−1​T−1),N=2​k,(e−ρ​T+e−2​ρ​T)​n​e2​ρ​n+1n−1​T+(e−ρ​T+e−2​ρ​T−1)−(2​n−1)​eρ​n+1n−1​T−2​e−ρ​T​eρ​n+1n−1​T𝒟−+2​n​(n−2)D−​eρ​n+1n−1​T​(eρ​n+1n−1​T−1),N=2​k+1.\displaystyle\longrightarrow\begin{cases}\displaystyle\frac{\left({e^{-\rho T}-e^{-2\rho T}}\right)ne^{2\rho\frac{n+1}{n-1}T}-\left({e^{-\rho T}-e^{-2\rho T}-1}\right)+2e^{-\rho T}e^{\rho\frac{n+1}{n-1}T}-(2n-1)e^{\rho\frac{n+1}{n-1}T}}{\mathscr{D}\_{+}}\\[-2.0pt] \displaystyle\qquad+\frac{2n(n-2)}{D\_{+}}e^{\rho\frac{n+1}{n-1}T}\left({e^{\rho\frac{n+1}{n-1}T}-1}\right),&\hskip-56.9055ptN=2k,\\[10.0pt] \displaystyle\frac{\left({e^{-\rho T}+e^{-2\rho T}}\right)ne^{2\rho\frac{n+1}{n-1}T}+\left({e^{-\rho T}+e^{-2\rho T}-1}\right)-(2n-1)e^{\rho\frac{n+1}{n-1}T}-2e^{-\rho T}e^{\rho\frac{n+1}{n-1}T}}{\mathscr{D}\_{-}}\\[-2.0pt] \displaystyle\qquad+\frac{2n(n-2)}{D\_{-}}e^{\rho\frac{n+1}{n-1}T}\left({e^{\rho\frac{n+1}{n-1}T}-1}\right),&\hskip-56.9055ptN=2k+1.\end{cases} |  |

Summing the boundary contributions with ∑i=2NGki\sum\_{i=2}^{N}G\_{k}^{i} for k=1,2,3k=1,2,3 yields the claimed limits for

|  |  |  |
| --- | --- | --- |
|  | 𝝎⊤​(κ^​Γ~−Γ~⊤)​𝝂.∎{\bm{\omega}}^{\top}\left({\hat{\kappa}\tilde{\Gamma}-\tilde{\Gamma}^{\top}}\right)\bm{\nu}.\qed |  |

###### Proof of Theorem [4.4](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem4 "Theorem 4.4 (Divergence of costs for 𝜃=0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact").

We proceed as in the proof of Theorem [4.2](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem2 "Theorem 4.2 (Convergence of costs for 𝜃>0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"), now using the limits

|  |  |  |  |
| --- | --- | --- | --- |
| (C.20) |  | limN↑∞N​even𝝎⊤​𝟏=e−ρ​T+ρ​T+1,limN↑∞N​odd𝝎⊤​𝟏=−e−ρ​T+ρ​T+1.\lim\_{\begin{subarray}{c}N\uparrow\infty\\ N\mathrm{even}\end{subarray}}\bm{\omega}^{\top}\bm{1}=e^{-\rho T}+\rho T+1,\qquad\lim\_{\begin{subarray}{c}N\uparrow\infty\\ N\mathrm{odd}\end{subarray}}\bm{\omega}^{\top}\bm{1}=-e^{-\rho T}+\rho T+1. |  |

These limits are taken from [[19](https://arxiv.org/html/2512.11765v1#bib.bib19), eq. (25), Proof of Theorem 3.1(d)], derived for the 22-player case; since 𝝎\bm{\omega} is independent of nn (Remark [2.4](https://arxiv.org/html/2512.11765v1#S2.Thmtheorem4 "Remark 2.4. ‣ 2.2. Nash Equilibrium ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")), the same limits apply here. In addition, we invoke ([C.19](https://arxiv.org/html/2512.11765v1#A3.E19 "In C.4. Proof of Theorem 4.3 (a) ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) together with Lemma [C.8](https://arxiv.org/html/2512.11765v1#A3.Thmtheorem8 "Lemma C.8. ‣ C.6. Proof of Theorem 4.4 ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"). Substituting these limits into the cost representation ([C.16](https://arxiv.org/html/2512.11765v1#A3.E16 "In Lemma C.6. ‣ C.3. Proof of Theorem 4.2 ‣ Appendix C Proofs for Section 4 ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) yields the claim.
∎

## Appendix D Time-Varying Instantaneous Costs

In this appendix we present a numerical analysis of how the equilibrium strategies and their asymptotics change when we charge instantaneous costs only on the first or second half of the time interval. This construction is motivated by the continuous-time game, where we can specify the “correct” block cost at 0 but the “wrong” one at TT (or vice versa), and then an equilibrium exists only in the case of zero-net supply (or symmetric initial inventories, respectively); see Remark [3.2](https://arxiv.org/html/2512.11765v1#S3.Thmtheorem2 "Remark 3.2. ‣ 3.2. Nash Equilibrium ‣ 3. Continuous-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact").
In the discrete-time model, a unique equilibrium still exists in these half-grid instantaneous-cost configurations. However, the qualitative behavior of the time-tt inventories changes substantially: when there is no instantaneous cost on one half of the grid, exactly one of the two processes V(N)V^{(N)} and W(N)W^{(N)} develops oscillations on that half of the interval, and the cluster points of the oscillating inventory are no longer the four cluster points from Theorem [4.3](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem3 "Theorem 4.3 (Divergence of strategies for 𝜃=0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"). In both of the configurations described below, the inventories X(N),iX^{(N),i} converge to the corresponding continuous-time equilibrium in precisely the cases singled out in
Remark [3.2](https://arxiv.org/html/2512.11765v1#S3.Thmtheorem2 "Remark 3.2. ‣ 3.2. Nash Equilibrium ‣ 3. Continuous-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact").

### Set-up

We modify the matrix Γθ\Gamma^{\theta} by turning the instantaneous-cost term on
or off separately on the first and second halves of the grid. Define

|  |  |  |
| --- | --- | --- |
|  | Hθ:=Γ0+2θI~,Jθ:=Γ0+2θI¯,\displaystyle H^{\theta}\mathrel{\mathop{\ordinarycolon}}=\Gamma^{0}+2\theta\widetilde{I},\qquad J^{\theta}\mathrel{\mathop{\ordinarycolon}}=\Gamma^{0}+2\theta\overline{I}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | I¯:=I−I~,I~i​j:={0,i≠j,0,i=j,i∈{1,…,⌈(N+1)/2⌉},1,i=j,i∈{⌈(N+1)/2⌉+1,…,N+1}.\displaystyle\overline{I}\mathrel{\mathop{\ordinarycolon}}=I-\widetilde{I},\qquad\widetilde{I}\_{ij}\mathrel{\mathop{\ordinarycolon}}=\begin{cases}0,&i\neq j,\\[1.99997pt] 0,&i=j,\ i\in\{1,\dots,\lceil(N+1)/2\rceil\},\\[1.99997pt] 1,&i=j,\ i\in\{\lceil(N+1)/2\rceil+1,\dots,N+1\}.\end{cases} |  |

Thus HθH^{\theta} corresponds to charging instantaneous costs only on the second
half of the time grid, while JθJ^{\theta} corresponds to charging instantaneous
costs only on the first half.

It can be shown that, if we replace Γθ\Gamma^{\theta} by HθH^{\theta} or JθJ^{\theta},
the proof of Theorem [2.7](https://arxiv.org/html/2512.11765v1#S2.Thmtheorem7 "Theorem 2.7 (Discrete equilibrium). ‣ 2.2. Nash Equilibrium ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") carries over. Hence
the equilibrium strategies are still of the form ([2.4](https://arxiv.org/html/2512.11765v1#S2.E4 "In Theorem 2.7 (Discrete equilibrium). ‣ 2.2. Nash Equilibrium ‣ 2. Discrete-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")) with

|  |  |  |  |
| --- | --- | --- | --- |
| (D.1) |  | 𝒗:=(Hθ+(n−1)​Γ~)−1​𝟏𝟏⊤​(Hθ+(n−1)​Γ~)−1​𝟏,𝒘:=(Hθ−Γ~)−1​𝟏𝟏⊤​(Hθ−Γ~)−1​𝟏,\bm{v}\mathrel{\mathop{\ordinarycolon}}=\frac{(H^{\theta}+(n-1)\widetilde{\Gamma})^{-1}\bm{1}}{\bm{1}^{\top}(H^{\theta}+(n-1)\widetilde{\Gamma})^{-1}\bm{1}},\qquad\bm{w}\mathrel{\mathop{\ordinarycolon}}=\frac{(H^{\theta}-\widetilde{\Gamma})^{-1}\bm{1}}{\bm{1}^{\top}(H^{\theta}-\widetilde{\Gamma})^{-1}\bm{1}}, |  |

and analogously with HθH^{\theta} replaced by JθJ^{\theta}.
We then define the time-tt inventories V(N)V^{(N)} and W(N)W^{(N)} from 𝒗\bm{v} and 𝒘\bm{w} in each case, as in ([4.2](https://arxiv.org/html/2512.11765v1#S4.E2 "In 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")).

### Second-half instantaneous cost

We first charge instantaneous costs only on
the second half of the grid, that is, we use the objective with HθH^{\theta}
replacing Γθ\Gamma^{\theta}. Numerically we observe that

|  |  |  |
| --- | --- | --- |
|  | |Wt(N)−𝕗​(t)|⟶0.\displaystyle\left\lvert{W^{(N)}\_{t}-\mathbbm{f}(t)}\right\rvert\longrightarrow 0. |  |

By contrast, Vt(N)V^{(N)}\_{t} does not converge to 𝕘​(t)\mathbbm{g}(t) on the whole
interval [0,T][0,T], but it does converge to 𝕘​(t)\mathbbm{g}(t) on [T/2,T][T/2,T]. On
[0,T/2][0,T/2], the process V(N)V^{(N)} exhibits oscillations and does not have a
limit; see Figure [4](https://arxiv.org/html/2512.11765v1#A4.F4 "Figure 4 ‣ Second-half instantaneous cost ‣ Appendix D Time-Varying Instantaneous Costs ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"). In light of
Remark [3.2](https://arxiv.org/html/2512.11765v1#S3.Thmtheorem2 "Remark 3.2. ‣ 3.2. Nash Equilibrium ‣ 3. Continuous-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"), this reflects the
continuous-time situation with ϑ0≠(n−1)/2\vartheta\_{0}\neq(n-1)/2 and
ϑT=1/2\vartheta\_{T}=1/2, where an equilibrium exists only in the zero-net-supply case
x¯=0\bar{x}=0 and is given by xi​𝕗​(t)x\_{i}\mathbbm{f}(t). If we assume
x¯=0\bar{x}=0, we recover the convergence of the
discrete-time inventories Xt(N),iX^{(N),i}\_{t} to the continuous-time equilibrium xi​𝕗​(t)x\_{i}\mathbbm{f}(t).

![Refer to caption](x3.png)


Figure 4. Convergence of inventories for even/odd values of NN
in the modified game with cost functional H1H^{1} (instantaneous cost charged in second half). We also plot the cluster points β±\beta\_{\pm} and γ±\gamma\_{\pm} from Theorem [4.3](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem3 "Theorem 4.3 (Divergence of strategies for 𝜃=0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") and note how they differ from the envelope of Vt(N)V^{(N)}\_{t}.

### First-half instantaneous cost

Next, we charge instantaneous costs only on
the first half of the grid, that is, we use the objective with JθJ^{\theta}
replacing Γθ\Gamma^{\theta}. In this case we observe numerically that

|  |  |  |
| --- | --- | --- |
|  | |Vt(N)−𝕘​(t)|⟶0.\displaystyle\left\lvert{V^{(N)}\_{t}-\mathbbm{g}(t)}\right\rvert\longrightarrow 0. |  |

By contrast, Wt(N)W^{(N)}\_{t} converges 𝕗​(t)\mathbbm{f}(t) only on [0,T/2][0,T/2]. On [T/2,T][T/2,T], the process
W(N)W^{(N)} oscillates and fails to converge; see Figure [5](https://arxiv.org/html/2512.11765v1#A4.F5 "Figure 5 ‣ First-half instantaneous cost ‣ Appendix D Time-Varying Instantaneous Costs ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact").
This behavior is consistent with
Remark [3.2](https://arxiv.org/html/2512.11765v1#S3.Thmtheorem2 "Remark 3.2. ‣ 3.2. Nash Equilibrium ‣ 3. Continuous-Time Equilibrium ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"), which states that in the
continuous-time game with ϑ0=(n−1)/2\vartheta\_{0}=(n-1)/2 and ϑT≠1/2\vartheta\_{T}\neq 1/2, an
equilibrium exists only in the symmetric case x1=⋯=xnx\_{1}=\cdots=x\_{n} and is given by
xi​𝕘​(t)x\_{i}\mathbbm{g}(t). If we assume x1=⋯=xnx\_{1}=\cdots=x\_{n}, we recover the convergence of the discrete-time inventories Xt(N),iX^{(N),i}\_{t} to the continuous-time equilibrium xi​𝕘​(t)x\_{i}\mathbbm{g}(t).

![Refer to caption](x4.png)


Figure 5. Convergence of inventories for even/odd values of NN
in the modified game with cost functional J1J^{1} (instantaneous cost charged in first half). We also plot the cluster points φ±\varphi\_{\pm} and ψ±\psi\_{\pm} from Theorem [4.3](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem3 "Theorem 4.3 (Divergence of strategies for 𝜃=0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact").

### Comparison with the cluster points from Theorem [4.3](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem3 "Theorem 4.3 (Divergence of strategies for 𝜃=0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact")

Finally, we note that the oscillatory envelopes observed in
Figures [4](https://arxiv.org/html/2512.11765v1#A4.F4 "Figure 4 ‣ Second-half instantaneous cost ‣ Appendix D Time-Varying Instantaneous Costs ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") and [5](https://arxiv.org/html/2512.11765v1#A4.F5 "Figure 5 ‣ First-half instantaneous cost ‣ Appendix D Time-Varying Instantaneous Costs ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact") differ from the cluster points from Theorem [4.3](https://arxiv.org/html/2512.11765v1#S4.Thmtheorem3 "Theorem 4.3 (Divergence of strategies for 𝜃=0). ‣ 4. High-Frequency Limits ‣ High-Frequency Analysis of a Trading Game with Transient Price Impact"), which are driven by NN being even or odd. In the
half-grid instantaneous-cost setting, the oscillations are localized to the
half of the grid where cost is absent, and the associated cluster points are no
longer determined by the even/odd parity of NN seen in the specification with no instantaneous costs.

## References

* [1]

  E. Abi Jaber, E. Neuman, and M. Voß.
  Equilibrium in functional stochastic games with mean-field interaction.
  Preprint arXiv:2306.05433v1, 2024.
* [2]

  R. Almgren and N. Chriss.
  Optimal execution of portfolio transactions.
  J. Risk, 3(2):5–39, 2001.
* [3]

  S. Campbell and M. Nutz.
  Optimal execution among NN traders with transient price impact.
  Preprint arXiv:2501.09638, 2024.
* [4]

  S. Campbell and M. Nutz.
  Randomization in optimal execution games.
  Preprint arXiv:2503.08833, 2025.
* [5]

  B. I. Carlin, M. S. Lobo, and S. Viswanathan.
  Episodic liquidity crises: Cooperative and predatory trading.
  J. Finance, 62(5):2235–2274, 2007.
* [6]

  Á. Cartea, S. Jaimungal, and J. Penalva.
  Algorithmic and High-Frequency Trading.
  Cambridge University Press, 2015.
* [7]

  R. Churchill and J. Brown.
  Complex Variables and Applications.
  International student edition. McGraw-Hill, 1984.
* [8]

  G. Fu, U. Horst, and X. Xia.
  Portfolio liquidation games with self-exciting order flow.
  Math. Finance, 32(4):1020–1065, 2022.
* [9]

  N. Garleanu and L. H. Pedersen.
  Dynamic portfolio choice with frictions.
  J. Econ. Theory, 165:487–516, 2016.
* [10]

  J. Gatheral.
  No-dynamic-arbitrage and market impact.
  Quant. Finance, 10(7):749–759, 2010.
* [11]

  P. Graewe and U. Horst.
  Optimal trade execution with instantaneous price impact and stochastic resilience.
  SIAM J. Control Optim., 55(6):3707–3725, 2017.
* [12]

  R. A. Horn and C. R. Johnson.
  Matrix Analysis.
  Cambridge University Press, 1985.
* [13]

  U. Horst and E. Kivman.
  Optimal trade execution under small market impact and portfolio liquidation with semimartingale strategies.
  Finance Stoch., 28(3):759–812, 2024.
* [14]

  W. Kelley and A. Peterson.
  Difference Equations: An Introduction with Applications.
  Elsevier Science, 2001.
* [15]

  X. Luo and A. Schied.
  Nash equilibrium for risk-averse investors in a market impact game with transient price impact.
  Market Microstructure and Liquidity, 05(01n04):2050001, 2019.
* [16]

  E. Neuman and M. Voß.
  Trading with the crowd.
  Math. Finance, 33(3):548–617, 2023.
* [17]

  A. A. Obizhaeva and J. Wang.
  Optimal trading strategy and supply/demand dynamics.
  J. Financial Mark., 16(1):1–32, 2013.
* [18]

  L. H. Pedersen and M. K. Brunnermeier.
  Predatory trading.
  J. Finance, 60(4):1825–1863, 2005.
* [19]

  A. Schied, E. Strehle, and T. Zhang.
  High-frequency limit of Nash equilibria in a market impact game with transient price impact.
  SIAM J. Financial Math., 8(1):589–634, 2017.
* [20]

  A. Schied and T. Zhang.
  A market impact game under transient price impact.
  Math. Oper. Res., 44(1):102–121, 2019.
* [21]

  T. Schöneborn.
  Trade execution in illiquid markets.
  PhD thesis, TU Berlin, 2008.
* [22]

  T. Schöneborn and A. Schied.
  Liquidation in the face of adversity: Stealth vs. sunshine trading.
  Preprint SSRN:1007014, 2009.
* [23]

  E. Strehle.
  Optimal execution in a multiplayer model of transient price impact.
  Market Microstructure and Liquidity, 03(03n04):1850007, 2017.
* [24]

  R. A. Usmani.
  Inversion of a tridiagonal Jacobi matrix.
  Linear Algebra and its Applications, 212-213:413–414, 1994.
* [25]

  K. Webster.
  Handbook of Price Impact Modeling.
  CRC Press, Boca Raton, FL, 2023.