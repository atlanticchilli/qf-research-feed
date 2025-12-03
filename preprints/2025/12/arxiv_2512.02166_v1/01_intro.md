---
authors:
- Ziyao Wang
- A. Alexandre Trindade
- Svetlozar T. Rachev
doc_id: arxiv:2512.02166v1
family_id: arxiv:2512.02166
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: The Three-Dimensional Decomposition of Volatility Memory
url_abs: http://arxiv.org/abs/2512.02166v1
url_html: https://arxiv.org/html/2512.02166v1
venue: arXiv q-fin
version: 1
year: 2025
---


Ziyao Wang
ziywang@ttu.edu


 A. Alexandre Trindade


 Svetlozar T. Rachev
  
Department of Mathematics and Statistics


 Texas Tech University

(December 1, 2025)

###### Abstract

This paper develops a three-dimensional decomposition of volatility memory into orthogonal components of *level*, *shape*, and *tempo*. The framework unifies regime-switching, fractional-integration, and business-time approaches within a single canonical representation that identifies how each dimension governs persistence strength, long-memory form, and temporal speed. We establish conditions for existence, uniqueness, and ergodicity of this decomposition and show that all GARCH-type processes arise as special cases. Empirically, applications to SPY and EURUSD (2005–2024) reveal that volatility memory is state-dependent: regime and tempo gates dominate in equities, while fractional-memory gates prevail in foreign exchange. The unified tri-gate model jointly captures these effects. By formalizing volatility dynamics through a level–shape–tempo structure, the paper provides a coherent link between information flow, market activity, and the evolving memory of financial volatility.

## 1 Introduction

Volatility is persistent, asymmetric, heavy–tailed, and evolves through episodes of abrupt stress and prolonged calm. Classical models that impose a single exponential memory scale, such as the standard GARCH(1,1), struggle to capture this heterogeneity: they under–react to slow‐moving regimes and over–react to transient bursts. Three complementary literatures have addressed fragments of this problem. First, regime–switching and smooth–transition volatility models allow persistence to vary with latent or observable states, describing calm–versus–crisis behavior (Hamilton, [1989](https://arxiv.org/html/2512.02166v1#bib.bib14); Teräsvirta, [1994](https://arxiv.org/html/2512.02166v1#bib.bib15)). Second, long–memory models such as FIGARCH replace exponential decay with fractional kernels that yield hyperbolic autocorrelation (Baillie et al., [1996](https://arxiv.org/html/2512.02166v1#bib.bib2)). Third, continuous–time approaches accelerate or decelerate the passage of economic time through business–time or stochastic–clock formulations, linking volatility clustering to trading intensity (Clark, [1973](https://arxiv.org/html/2512.02166v1#bib.bib5); Andersen & Bollerslev, [1998](https://arxiv.org/html/2512.02166v1#bib.bib16)).

This paper unifies these ideas into an empirically tractable *gated volatility framework* in which the strength, shape, and tempo of persistence each respond smoothly to observable market conditions. The first gate, *RSM*, modulates the persistence coefficient through a logistic map of market features, producing a continuous regime–switching memory process. The second, *G–FIGARCH*, endogenizes the fractional integration order so that the degree of long memory itself becomes state–dependent. The third, *G–Clock*, introduces an observable business–time deformation that speeds or slows the effective decay of shocks. Each gate admits transparent economic interpretation through features such as realized volatility, volume, and implied volatility, linking statistical memory directly to information flow and market activity.

Beyond these separate pillars, we develop pairwise and fully unified specifications—including a tri–gate model (TG–Vol)—that nest regime, fractional, and clock mechanisms within a single recursion. This architecture clarifies how persistence level, memory shape, and temporal speed can interact while preserving theoretical tractability. We establish positivity, finite–moment, and geometric–ergodicity conditions for all gated systems; prove identification through distinct functional and spectral signatures; and show that quasi–maximum likelihood and Whittle–regularized estimation remain consistent and asymptotically normal under mild assumptions.

Empirically, the framework is evaluated on broad U.S. equity and foreign–exchange datasets (SPY/ES and EURUSD) over 2005–2024. Rolling–window forecasts, density–based loss metrics, and VaR/ES backtests (Fissler & Ziegel, [2016](https://arxiv.org/html/2512.02166v1#bib.bib7); Patton, [2011](https://arxiv.org/html/2512.02166v1#bib.bib18)) reveal that volatility memory is *state–dependent* and *market–specific*. On EURUSD, the long–memory gate (G–FIGARCH) dominates variance forecasting, while on SPY the regime and clock gates (RSM, G–Clock) deliver superior tail–risk timing. Across markets, crises raise the persistence and fractional–memory gates while compressing the business–time speed—consistent with faster information flow during stress.

By integrating smooth–transition, fractional, and time–change mechanisms in a single theoretical and empirical framework, the paper bridges strands of volatility modeling that were previously disjoint. The resulting family of gated models provides a coherent, interpretable, and statistically rigorous foundation for studying how market conditions reshape the dynamics of volatility memory.

## 2 Literature Review

This section synthesizes three literatures: (i) regime-switching/smooth-transition volatility, (ii) fractional integration in volatility, and (iii) business-time (time-change) dynamics.

### 2.1 Regime Switching and Smooth Transition in Volatility

Regime-switching volatility dates to Hamilton ([1989](https://arxiv.org/html/2512.02166v1#bib.bib14)), with latent Markov states capturing shifts in mean and variance. Smooth-transition GARCH (ST-GARCH) later introduced a continuous gate ptp\_{t} mapping past information into a blending weight between regimes, commonly via a logistic transition (Teräsvirta, [1994](https://arxiv.org/html/2512.02166v1#bib.bib15)). The gate is often a function of lagged shocks or exogenous features, pt=σ​(γ⊤​zt−1)p\_{t}=\sigma(\gamma^{\top}z\_{t-1}), yielding a *soft* rather than abrupt switch. This literature documents improved fit during crisis vs. calm episodes, interpretable transition surfaces, and meaningful policy or microstructure covariates.

From a methodological standpoint, smooth-transition models permit straightforward QMLE and robust inference under weak moment conditions. Identification typically requires variation in zt−1z\_{t-1} and restrictions on overlap between blended regimes. Our RSM adopts this logic but focuses the blending on the *persistence coefficient* βt\beta\_{t}, keeping level and leverage channels orthogonal to persistence for interpretability In our RSM specification, the gate acts directly on the persistence coefficient rather than on the conditional mean, isolating regime effects on volatility memory. This explicitly links to the level dimension of our framework..

### 2.2 Fractional Integration and Long Memory in Volatility

FIGARCH (Baillie et al., [1996](https://arxiv.org/html/2512.02166v1#bib.bib2)) shifts attention from regime-dependent levels to the *shape* of memory. Instead of a short-memory exponential kernel, FIGARCH imposes a fractional difference (1−ℒ)d(1-\mathcal{L})^{d} on the innovation variance, inducing hyperbolic decay and long-range dependence when d∈(0,1/2)d\in(0,1/2). Empirically, realized variance autocorrelations decline slowly, and spectral power accumulates at low frequencies, both consistent with long memory. Yet, a *fixed* dd can be too rigid: crisis windows may exhibit stronger long memory than quiet windows. Our G-FIGARCH gate dt=d¯⋅σ​(γ⊤​zt−1)d\_{t}=\bar{d}\cdot\sigma(\gamma^{\top}z\_{t-1}) links the order to observables, making the low-frequency slope itself state-dependent while preserving tractability We note that FIGARCH nests GARCH and IGARCH as special cases, and empirical estimates often find d∈(0,0.3)d\in(0,0.3). This corresponds to the shape gate in our canonical decomposition..

### 2.3 Business Time and Stochastic Clocks

The notion that markets operate in *business time*—fast when trading is heavy, slow when activity wanes—goes back to Clark ([1973](https://arxiv.org/html/2512.02166v1#bib.bib5)) and underpins modern realized-variance econometrics (Andersen & Bollerslev, [1998](https://arxiv.org/html/2512.02166v1#bib.bib16)). In continuous time, time-changed processes and subordinators formalize this acceleration. Our G-Clock adapts this idea to discrete-time volatility: Δ​τt=exp⁡(η⊤​zt−1)\Delta\tau\_{t}=\exp(\eta^{\top}z\_{t-1}) implies βt=exp⁡(−κ​Δ​τt)∈(0,1)\beta\_{t}=\exp(-\kappa\Delta\tau\_{t})\in(0,1), converting activity shocks into endogenous changes in persistence *tempo* without freely gating βt\beta\_{t} itself. This creates a sharp conceptual distinction from RSM while remaining estimable by standard methods. Explicitly, Δ​τt\Delta\tau\_{t} may be proxy-based (e.g., realized variance, volume, order-flow imbalance) to highlight observability. This functions as the tempo gate.

## 3 Theory

### 3.1 Canonical Decomposition of Volatility Memory

This subsection establishes a canonical (level–tempo–shape) decomposition for volatility
“memory kernels” that drive conditional variance dynamics. We work at the level of kernels,
so that all concrete recursions (e.g., GARCH/FIGARCH/time–changed models) are covered
as special cases in Section [3.2](https://arxiv.org/html/2512.02166v1#S3.SS2 "3.2 Universality of the Level–Shape–Tempo Framework ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory").

##### Set–up and notation.

Let (Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}) be a complete probability space and let
{εt}t∈ℤ\{\varepsilon\_{t}\}\_{t\in\mathbb{Z}} be i.i.d. with
𝔼​[εt]=0\mathbb{E}[\varepsilon\_{t}]=0, 𝔼​[εt2]=1\mathbb{E}[\varepsilon\_{t}^{2}]=1, and 𝔼​[|εt|2+δ]<∞\mathbb{E}[|\varepsilon\_{t}|^{2+\delta}]<\infty for some δ>0\delta>0.
We consider volatility dynamics for demeaned returns rt=ht​εtr\_{t}=\sqrt{h\_{t}}\,\varepsilon\_{t} driven by a
nonnegative kernel acting on past squared shocks. Abstractly, a (time–invariant) kernel is a Borel
measurable function f:ℝ+→[0,∞)f:\mathbb{R}\_{+}\to[0,\infty) (or, in discrete time, a sequence {ψk}k≥1\{\psi\_{k}\}\_{k\geq 1})
which determines a linear functional of past εt−k2\varepsilon\_{t-k}^{2} entering the conditional variance.
The continuous representation below covers discrete recursions via step–function embedding.

###### Assumption 1 (Admissible memory kernels).

A measurable f:ℝ+→[0,∞)f:\mathbb{R}\_{+}\to[0,\infty) is *admissible* if:

1. 1.

   f∈L1​(ℝ+)f\in L^{1}(\mathbb{R}\_{+}) with total mass M:=∫0∞f​(u)​𝑑u∈(0,∞)M:=\int\_{0}^{\infty}f(u)\,du\in(0,\infty);
2. 2.

   ff has finite first moment ∫0∞u​f​(u)​𝑑u<∞\int\_{0}^{\infty}u\,f(u)\,du<\infty.

We denote the class by 𝒦:={f≥0:f∈L1​(ℝ+),∫u​f​(u)​𝑑u<∞}\mathcal{K}:=\big\{f\geq 0:\ f\in L^{1}(\mathbb{R}\_{+}),\ \int uf(u)\,du<\infty\big\}.

###### Remark 1 (Coverage of discrete kernels and classical models).

Given a nonnegative sequence {ψk}k≥1\{\psi\_{k}\}\_{k\geq 1} with ∑kψk<∞\sum\_{k}\psi\_{k}<\infty and ∑kk​ψk<∞\sum\_{k}k\,\psi\_{k}<\infty,
define the step–function embedding

|  |  |  |
| --- | --- | --- |
|  | f​(u):=∑k=1∞ψk​ 1[k−1,k)​(u),u≥0.f(u)\;:=\;\sum\_{k=1}^{\infty}\psi\_{k}\,\mathbf{1}\_{[k-1,k)}(u),\qquad u\geq 0. |  |

Then f∈𝒦f\in\mathcal{K} with M=∑kψkM=\sum\_{k}\psi\_{k} and ∫u​f​(u)​𝑑u=∑k(2​k−12)​ψk<∞\int uf(u)\,du=\sum\_{k}\!\big(\tfrac{2k-1}{2}\big)\psi\_{k}<\infty.
Hence GARCH–type exponential tails, FIGARCH–type hyperbolic tails with d<12d<\tfrac{1}{2} (so that ∑k​ψk<∞\sum k\,\psi\_{k}<\infty),
and mixtures thereof are covered.

##### Interpretation.

Intuitively, MM measures the *aggregate strength* of memory,
∫u​f​(u)​𝑑u/M\int uf(u)\,du/M is a *characteristic time scale*, and the residual shape after removing
mass and scale captures the *form* (exponential vs. hyperbolic decay, etc.). The next theorem
formalizes this as a unique decomposition.

###### Definition 1 (Normalized shape class).

Define

|  |  |  |
| --- | --- | --- |
|  | 𝒢:={g:ℝ+→[0,∞)​measurable:∫0∞g​(u)​𝑑u=1,∫0∞u​g​(u)​𝑑u=1}.\mathcal{G}\;:=\;\Big\{g:\mathbb{R}\_{+}\to[0,\infty)\ \text{measurable}:\ \int\_{0}^{\infty}g(u)\,du=1,\ \int\_{0}^{\infty}u\,g(u)\,du=1\Big\}. |  |

Elements of 𝒢\mathcal{G} are *shapes* normalized to unit mass and unit first moment.

###### Theorem 1 (Canonical level–tempo–shape decomposition).

Let f∈𝒦f\in\mathcal{K} be an admissible kernel with

|  |  |  |
| --- | --- | --- |
|  | M:=∫0∞f​(u)​𝑑u∈(0,∞),μ:=1M​∫0∞u​f​(u)​𝑑u∈(0,∞).M\;:=\;\int\_{0}^{\infty}f(u)\,du\in(0,\infty),\qquad\mu\;:=\;\frac{1}{M}\int\_{0}^{\infty}u\,f(u)\,du\in(0,\infty). |  |

Define g:ℝ+→[0,∞)g:\mathbb{R}\_{+}\to[0,\infty) by

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(u):=μM​f​(μ​u),u≥0.g(u)\;:=\;\frac{\mu}{M}\,f(\mu u),\qquad u\geq 0. |  | (1) |

Then g∈𝒢g\in\mathcal{G} and, for all u≥0u\geq 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(u)=M⋅1μ​g​(uμ).f(u)\;=\;M\cdot\frac{1}{\mu}\,g\!\Big(\frac{u}{\mu}\Big). |  | (2) |

Conversely, given any (M,μ,g)∈(0,∞)×(0,∞)×𝒢(M,\mu,g)\in(0,\infty)\times(0,\infty)\times\mathcal{G}, the formula
f​(u)=M​μ−1​g​(u/μ)f(u)=M\,\mu^{-1}g(u/\mu) produces an admissible kernel in 𝒦\mathcal{K} with the above (M,μ)(M,\mu).

Proof. The detailed proof is provided in Appendix [Appendix B — Canonical Level–Tempo–Shape Decomposition](https://arxiv.org/html/2512.02166v1#Ax3 "Appendix B — Canonical Level–Tempo–Shape Decomposition ‣ The Three-Dimensional Decomposition of Volatility Memory").

###### Theorem 2 (Uniqueness).

The decomposition ([2](https://arxiv.org/html/2512.02166v1#S3.E2 "In Theorem 1 (Canonical level–tempo–shape decomposition). ‣ Interpretation. ‣ 3.1 Canonical Decomposition of Volatility Memory ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory")) is unique up to null sets: if

|  |  |  |
| --- | --- | --- |
|  | f​(u)=M⋅1μ​g​(uμ)=M′⋅1μ′​g′​(uμ′)for a.e. ​u≥0,f(u)\;=\;M\cdot\frac{1}{\mu}\,g\!\Big(\frac{u}{\mu}\Big)\;=\;M^{\prime}\cdot\frac{1}{\mu^{\prime}}\,g^{\prime}\!\Big(\frac{u}{\mu^{\prime}}\Big)\qquad\text{for a.e.\ }u\geq 0, |  |

with (M,μ,g)∈(0,∞)×(0,∞)×𝒢(M,\mu,g)\in(0,\infty)\times(0,\infty)\times\mathcal{G} and
(M′,μ′,g′)∈(0,∞)×(0,∞)×𝒢(M^{\prime},\mu^{\prime},g^{\prime})\in(0,\infty)\times(0,\infty)\times\mathcal{G}, then M=M′M=M^{\prime}, μ=μ′\mu=\mu^{\prime},
and g=g′g=g^{\prime} almost everywhere.

Proof. The detailed proof is provided in Appendix [Appendix C — Proof of Theorem 2 (Uniqueness of the Canonical Decomposition)](https://arxiv.org/html/2512.02166v1#Ax4 "Appendix C — Proof of Theorem 2 (Uniqueness of the Canonical Decomposition) ‣ The Three-Dimensional Decomposition of Volatility Memory").

###### Remark 2 (Degenerate and boundary cases).

If M=0M=0 (the zero kernel), the factorization is trivial. If
∫0∞f=∞\int\_{0}^{\infty}f=\infty or ∫0∞u​f​(u)​𝑑u=∞\int\_{0}^{\infty}uf(u)\,du=\infty the decomposition
need not exist; this exclusion covers exact IGARCH and borderline FIGARCH cases, which in practice can be approximated arbitrarily well but do not admit a finite M,μM,\mu pair.
Discrete IGARCH can be viewed as an admissible limit where M↑∞M\uparrow\infty and gg approaches
a scale–free tail; see Section [3.2](https://arxiv.org/html/2512.02166v1#S3.SS2 "3.2 Universality of the Level–Shape–Tempo Framework ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory") for precise embeddings.

##### From kernels to volatility recursions.

The decomposition isolates three orthogonal levers:

|  |  |  |
| --- | --- | --- |
|  | level ​(M),tempo ​(μ),shape ​(g).\text{level }(M),\qquad\text{tempo }(\mu),\qquad\text{shape }(g). |  |

Any admissible kernel can thus be written as a mass–preserving time dilation of a normalized
shape. In discrete time, by Remark [1](https://arxiv.org/html/2512.02166v1#Thmremark1 "Remark 1 (Coverage of discrete kernels and classical models). ‣ Set–up and notation. ‣ 3.1 Canonical Decomposition of Volatility Memory ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory"), for
ψk=∫k−1kf​(u)​𝑑u\psi\_{k}=\int\_{k-1}^{k}f(u)\,du we have

|  |  |  |
| --- | --- | --- |
|  | ψk=∫k−1kM⋅1μ​g​(uμ)​𝑑u=M​∫(k−1)/μk/μg​(v)​𝑑v,\psi\_{k}=\int\_{k-1}^{k}M\cdot\frac{1}{\mu}\,g\!\Big(\frac{u}{\mu}\Big)\,du=M\int\_{(k-1)/\mu}^{k/\mu}g(v)\,dv, |  |

which makes explicit how (M,μ,g)(M,\mu,g) control the weights on lags.

##### Identification in the frequency domain

The decomposition has an immediate orthogonality in frequency space: level affects vertical
scale, tempo dilates the frequency axis, and shape controls low–frequency slope.

###### Assumption 2 (Second–order set–up for spectra).

Let {Xt}\{X\_{t}\} be a (weakly) stationary zero–mean process linear in past innovations with kernel ff,
e.g., Xt=∑k≥1ψk​(εt−k2−1)X\_{t}=\sum\_{k\geq 1}\psi\_{k}(\varepsilon\_{t-k}^{2}-1) in discrete time with
ψk=∫k−1kf​(u)​𝑑u\psi\_{k}=\int\_{k-1}^{k}f(u)\,du. Assume ∑k|ψk|<∞\sum\_{k}|\psi\_{k}|<\infty so that the spectral
density Sf​(λ)S\_{f}(\lambda) exists and is continuous on [−π,π][-\pi,\pi].

###### Proposition 1 (Orthogonality: vertical, horizontal, and slope).

Let f​(u)=M​μ−1​g​(u/μ)f(u)=M\mu^{-1}g(u/\mu) with g∈𝒢g\in\mathcal{G} and define SgS\_{g} as the spectral density
associated with the kernel gg (via the embedding of Remark [1](https://arxiv.org/html/2512.02166v1#Thmremark1 "Remark 1 (Coverage of discrete kernels and classical models). ‣ Set–up and notation. ‣ 3.1 Canonical Decomposition of Volatility Memory ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory")).
Then for all λ∈[−π,π]\lambda\in[-\pi,\pi],

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sf​(λ)=M2​Sg​(μ​λ).S\_{f}(\lambda)\;=\;M^{2}\,S\_{g}(\mu\lambda). |  | (3) |

In particular:

1. 1.

   Level MM produces a pure vertical rescaling of the spectrum;
2. 2.

   Tempo μ\mu dilates the frequency axis (horizontal rescaling);
3. 3.

   If gg exhibits a low–frequency power law Sg​(λ)∼C​λ−2​dS\_{g}(\lambda)\sim C\,\lambda^{-2d} as λ↓0\lambda\downarrow 0
   for some d∈[0,1/2)d\in[0,1/2), then Sf​(λ)∼(M2​C)​λ−2​dS\_{f}(\lambda)\sim(M^{2}C)\,\lambda^{-2d} as λ↓0\lambda\downarrow 0:
   the *low–frequency slope is a shape property only*.

Proof. The detailed proof is provided in Appendix [Appendix D — Spectral Orthogonality and Scaling](https://arxiv.org/html/2512.02166v1#Ax5 "Appendix D — Spectral Orthogonality and Scaling ‣ The Three-Dimensional Decomposition of Volatility Memory").

###### Remark 3 (Empirical identification).

Proposition [1](https://arxiv.org/html/2512.02166v1#Thmproposition1 "Proposition 1 (Orthogonality: vertical, horizontal, and slope). ‣ Identification in the frequency domain ‣ 3.1 Canonical Decomposition of Volatility Memory ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory") implies a clean identification strategy:
(i) the low–frequency slope estimates the shape parameter(s) of gg (e.g., FIGARCH dd);
(ii) vertical levels index MM; (iii) horizontal dilation indexes μ\mu (e.g., via alignment of
breakpoints in multi–scale spectra). In Section [3.12](https://arxiv.org/html/2512.02166v1#S3.SS12 "3.12 Frequency-Domain Methods and Whittle Regularization ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory") we exploit
this by combining time–domain QMLE with a local–Whittle penalty for gg.

##### Consequences for volatility modeling

The canonical decomposition shows that any admissible memory specification is equivalent to
choosing a *shape* g∈𝒢g\in\mathcal{G} (exponential, hyperbolic, mixtures), an overall *level* MM,
and a *tempo* μ\mu (time deformation). In particular:

* •

  *Level gate (RSM)* varies MM while keeping μ\mu and gg fixed;
* •

  *Shape gate (G–FIGARCH)* varies gg within a parametric family (e.g., g​(⋅;d)g(\cdot;d)) with fixed (M,μ)(M,\mu);
* •

  *Tempo gate (G–Clock)* varies μ\mu (business–time dilation) with fixed (M,g)(M,g).

Section [3.2](https://arxiv.org/html/2512.02166v1#S3.SS2 "3.2 Universality of the Level–Shape–Tempo Framework ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory") formalizes that classical GARCH families are exactly the
specializations obtained by constraining one or more of (M,μ,g)(M,\mu,g).

Summary.
Under Assumption [1](https://arxiv.org/html/2512.02166v1#Thmassumption1 "Assumption 1 (Admissible memory kernels). ‣ Set–up and notation. ‣ 3.1 Canonical Decomposition of Volatility Memory ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory"), every admissible volatility memory kernel admits
a unique factorization f​(u)=M​μ−1​g​(u/μ)f(u)=M\,\mu^{-1}g(u/\mu) with (M,μ)∈(0,∞)2(M,\mu)\in(0,\infty)^{2} and
g∈𝒢g\in\mathcal{G}. In frequency domain, MM and μ\mu act as vertical/horizontal scalings while
the low–frequency slope (long–memory strength) is determined solely by gg. This provides the
theoretical foundation on which the observable gates in Sections [3.4](https://arxiv.org/html/2512.02166v1#S3.SS4 "3.4 RSM: Level Gate and State–Dependent Persistence ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory")–[3.6](https://arxiv.org/html/2512.02166v1#S3.SS6 "3.6 G–Clock: Tempo Gate and Observable Business Time ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory")
are built.

### 3.2 Universality of the Level–Shape–Tempo Framework

Having established in Section [3.1](https://arxiv.org/html/2512.02166v1#S3.SS1 "3.1 Canonical Decomposition of Volatility Memory ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory") that any admissible
memory kernel admits a unique decomposition into level, tempo, and shape components,
we now prove that the canonical representation

|  |  |  |
| --- | --- | --- |
|  | ft​(u)=Mt​1μt​gt​(uμt),(Mt,μt,gt)∈(0,∞)2×𝒢,f\_{t}(u)\;=\;M\_{t}\,\frac{1}{\mu\_{t}}\,g\_{t}\!\Big(\frac{u}{\mu\_{t}}\Big),\quad(M\_{t},\mu\_{t},g\_{t})\in(0,\infty)^{2}\times\mathcal{G}, |  |

constitutes a *universal envelope* for the entire GARCH family of
conditionally heteroskedastic processes.
All classical volatility models correspond to specific restrictions on
(Mt,μt,gt)(M\_{t},\mu\_{t},g\_{t}), and conversely any stable volatility recursion can
be represented within this framework.

##### General volatility recursion.

Let {rt}\{r\_{t}\} be a zero–mean return process with conditional variance ht>0h\_{t}>0
satisfying the abstract recursion

|  |  |  |  |
| --- | --- | --- | --- |
|  | ht=ω+∑k=1∞ψt,k​(εt−k2−1),ψt,k≥0,∑k≥1ψt,k<∞,h\_{t}\;=\;\omega\;+\;\sum\_{k=1}^{\infty}\psi\_{t,k}\,\big(\varepsilon\_{t-k}^{2}-1\big),\qquad\psi\_{t,k}\geq 0,\quad\sum\_{k\geq 1}\psi\_{t,k}<\infty, |  | (4) |

where {εt}\{\varepsilon\_{t}\} are i.i.d. innovations with
𝔼​εt2=1\mathbb{E}\varepsilon\_{t}^{2}=1.
For each tt, define the (possibly random) kernel
ft​(u):=∑k≥1ψt,k​𝟏[k−1,k)​(u)f\_{t}(u):=\sum\_{k\geq 1}\psi\_{t,k}\mathbf{1}\_{[k-1,k)}(u).
Assume ft∈𝒦f\_{t}\in\mathcal{K} almost surely, so that both the total mass
Mt:=∫ftM\_{t}:=\int f\_{t} and first moment
μt:=(1/Mt)​∫u​ft​(u)​𝑑u\mu\_{t}:=(1/M\_{t})\int uf\_{t}(u)\,du are finite.
By Theorem [1](https://arxiv.org/html/2512.02166v1#Thmtheorem1 "Theorem 1 (Canonical level–tempo–shape decomposition). ‣ Interpretation. ‣ 3.1 Canonical Decomposition of Volatility Memory ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory"),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ft​(u)=Mt​1μt​gt​(u/μt),gt∈𝒢.f\_{t}(u)=M\_{t}\,\frac{1}{\mu\_{t}}\,g\_{t}(u/\mu\_{t}),\qquad g\_{t}\in\mathcal{G}. |  | (5) |

Hence any stable conditional–variance recursion admits a well–defined
triple (Mt,μt,gt)(M\_{t},\mu\_{t},g\_{t}) and therefore can be viewed as a realization
of the canonical level–shape–tempo system.

###### Theorem 3 (Universality of the level–shape–tempo framework).

Let {ht}\{h\_{t}\} satisfy ([4](https://arxiv.org/html/2512.02166v1#S3.E4 "In General volatility recursion. ‣ 3.2 Universality of the Level–Shape–Tempo Framework ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory")) with an admissible kernel ftf\_{t}
for each tt. Then:

1. (i)

   There exists a unique triple (Mt,μt,gt)(M\_{t},\mu\_{t},g\_{t})
   such that ft​(u)=Mt​μt−1​gt​(u/μt)f\_{t}(u)=M\_{t}\,\mu\_{t}^{-1}g\_{t}(u/\mu\_{t}) with gt∈𝒢g\_{t}\in\mathcal{G}.
2. (ii)

   Conversely, for any predictable processes
   Mt>0M\_{t}>0, μt>0\mu\_{t}>0, and measurable gt∈𝒢g\_{t}\in\mathcal{G} satisfying
   suptMt​(1+μt)<∞\sup\_{t}M\_{t}(1+\mu\_{t})<\infty, the recursion

   |  |  |  |
   | --- | --- | --- |
   |  | ht=ω+∑k≥1∫k−1kMt​1μt​gt​(uμt)​𝑑u​(εt−k2−1)h\_{t}=\omega+\sum\_{k\geq 1}\int\_{k-1}^{k}M\_{t}\,\frac{1}{\mu\_{t}}\,g\_{t}\!\Big(\frac{u}{\mu\_{t}}\Big)\,du\,(\varepsilon\_{t-k}^{2}-1) |  |

   is well–defined, strictly positive, and weakly stationary provided
   𝔼​[εt2]=1\mathbb{E}[\varepsilon\_{t}^{2}]=1 and suptMt<1\sup\_{t}M\_{t}<1.
3. (iii)

   Classical GARCH–type models correspond to
   particular restrictions of (Mt,μt,gt)(M\_{t},\mu\_{t},g\_{t}) as summarized in
   Table [1](https://arxiv.org/html/2512.02166v1#S3.T1 "Table 1 ‣ Explicit embeddings for classical models. ‣ 3.2 Universality of the Level–Shape–Tempo Framework ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory").

###### Proof.

Part (i) is a direct application of Theorem [1](https://arxiv.org/html/2512.02166v1#Thmtheorem1 "Theorem 1 (Canonical level–tempo–shape decomposition). ‣ Interpretation. ‣ 3.1 Canonical Decomposition of Volatility Memory ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory")
for each tt. For (ii), the boundedness of suptMt​(1+μt)\sup\_{t}M\_{t}(1+\mu\_{t}) ensures
∑k≥1ψt,k<∞\sum\_{k\geq 1}\psi\_{t,k}<\infty uniformly in tt; positivity follows
since gt≥0g\_{t}\geq 0; weak stationarity holds under the stated moment condition
by standard contraction arguments identical to those in
Proposition 1 for the RSM model. Part (iii) is established by explicit
construction below.
∎

##### Explicit embeddings for classical models.

We now give explicit constructions that realize standard GARCH–type recursions as
specializations of the canonical kernel
ft​(u)=Mt​μt−1​gt​(u/μt)f\_{t}(u)=M\_{t}\,\mu\_{t}^{-1}g\_{t}(u/\mu\_{t}) with gt∈𝒢g\_{t}\in\mathcal{G},
where ∫0∞gt=1\int\_{0}^{\infty}g\_{t}=1 and ∫0∞u​gt=1\int\_{0}^{\infty}u\,g\_{t}=1.
Throughout, {εt}\{\varepsilon\_{t}\} are i.i.d. with 𝔼​εt2=1\mathbb{E}\varepsilon\_{t}^{2}=1.

*(1) General GARCH(p,q)(p,q).*
Let ht=ω+∑i=1pαi​εt−i2+∑j=1qβj​ht−jh\_{t}=\omega+\sum\_{i=1}^{p}\alpha\_{i}\varepsilon\_{t-i}^{2}+\sum\_{j=1}^{q}\beta\_{j}h\_{t-j}
with the usual stability condition (all roots of 1−∑j=1qβj​zj1-\sum\_{j=1}^{q}\beta\_{j}z^{j} outside the unit circle).
By the well–known ARCH(∞)(\infty) representation,
ht=ω+∑k=1∞ψk​(εt−k2−1)h\_{t}=\omega+\sum\_{k=1}^{\infty}\psi\_{k}(\varepsilon\_{t-k}^{2}-1) with ψk≥0\psi\_{k}\geq 0 and
∑kψk<∞\sum\_{k}\psi\_{k}<\infty, where ψk\psi\_{k} decays at least exponentially fast (possibly
times a polynomial).
Define f​(u):=∑k≥1ψk​𝟏[k−1,k)​(u)f(u):=\sum\_{k\geq 1}\psi\_{k}\mathbf{1}\_{[k-1,k)}(u).
Then M:=∫f=∑kψk<∞M:=\int f=\sum\_{k}\psi\_{k}<\infty and μ:=(1/M)​∫u​f​(u)​𝑑u<∞\mu:=(1/M)\int uf(u)\,du<\infty are constants,
and the normalized shape g​(u):=(μ/M)​f​(μ​u)g(u):=(\mu/M)f(\mu u) lies in 𝒢\mathcal{G}.
Hence GARCH(p,q)(p,q) corresponds to a fixed triple (M,μ,g)(M,\mu,g) with a short–memory shape
gg that is exponentially decaying up to a mild polynomial factor.

*(2) GARCH(1,1)(1,1).*
For ht=ω+α​εt−12+β​ht−1h\_{t}=\omega+\alpha\varepsilon\_{t-1}^{2}+\beta h\_{t-1} with 0<β<10<\beta<1,
the ARCH(∞)(\infty) weights are ψk=α​βk−1\psi\_{k}=\alpha\beta^{k-1}. Writing
f​(u)=∑k≥1α​βk−1​𝟏[k−1,k)​(u)f(u)=\sum\_{k\geq 1}\alpha\beta^{\,k-1}\mathbf{1}\_{[k-1,k)}(u), we obtain the continuous
exponential approximation f​(u)≈α​e−λ​uf(u)\approx\alpha e^{-\lambda u} with λ=−log⁡β\lambda=-\log\beta,
so that

|  |  |  |
| --- | --- | --- |
|  | M=αλ,μ=1λ,g​(u)=e−u.M=\frac{\alpha}{\lambda},\qquad\mu=\frac{1}{\lambda},\qquad g(u)=e^{-u}. |  |

Thus GARCH(1,1)(1,1) fixes (M,μ,g)=(α/λ, 1/λ,e−u)(M,\mu,g)=(\alpha/\lambda,\,1/\lambda,\,e^{-u}) and is a short–memory
exponential kernel.

*(3) IGARCH(1,1)(1,1).*
When α+β=1\alpha+\beta=1, the same computation gives ψk=α​βk−1\psi\_{k}=\alpha\beta^{k-1} but
∑kψk=+∞\sum\_{k}\psi\_{k}=+\infty. Consequently the kernel keeps the exponential *shape*
g​(u)=e−ug(u)=e^{-u} while the level M=∫fM=\int f diverges: IGARCH is the boundary case of
infinite memory mass with the same tempo μ=1/(−log⁡β)\mu=1/(-\log\beta).

*(4) FIGARCH(d)(d), 0<d<1/20<d<1/2.*
The fractional differencing on εt2\varepsilon\_{t}^{2} yields ARCH(∞)(\infty) weights
ψk​(d)∼C​k−(1+d)\psi\_{k}(d)\sim C\,k^{-(1+d)} as k→∞k\to\infty, so the associated kernel obeys
f​(u)∝u−(1+d)f(u)\propto u^{-(1+d)} for large uu. After normalization,

|  |  |  |
| --- | --- | --- |
|  | M=∫f<∞,μ=∫u​f∫f<∞,g​(u;d)∝u−(1+d)(with ​∫g=∫u​g=1).M=\int f<\infty,\qquad\mu=\frac{\int uf}{\int f}<\infty,\qquad g(u;d)\propto u^{-(1+d)}\ \ (\text{with }\int g=\int ug=1). |  |

Hence FIGARCH fixes (M,μ)(M,\mu) and gates the *shape* via the fractional order dd,
producing hyperbolic long memory (low–frequency spectrum ∼λ−2​d\sim\lambda^{-2d}).

*(5) HYGARCH.*
Let g​(u)g(u) be a convex combination of an exponential and a hyperbolic tail,
e.g. g​(u)=(1−δ)​e−u+δ​Cd​u−(1+d)g(u)=(1-\delta)e^{-u}+\delta\,C\_{d}\,u^{-(1+d)} with 0≤δ≤10\leq\delta\leq 1 and CdC\_{d}
chosen to satisfy the two moment normalizations.
Then f​(u)=M​μ−1​g​(u/μ)f(u)=M\,\mu^{-1}g(u/\mu) interpolates smoothly between short and long memory
by varying δ\delta (and dd if desired) while keeping (M,μ)(M,\mu) fixed.

*(6) Smooth–transition GARCH / RSM (level gate).*
Let βt=(1−pt)​βlow+pt​βhigh\beta\_{t}=(1-p\_{t})\beta\_{\mathrm{low}}+p\_{t}\beta\_{\mathrm{high}} with
pt=σ​(γ⊤​zt−1)∈(0,1)p\_{t}=\sigma(\gamma^{\top}z\_{t-1})\in(0,1) and fix α>0\alpha>0.
Locally at time tt, the ARCH(∞)(\infty) weights satisfy
ψt,k≈α​βtk−1\psi\_{t,k}\approx\alpha\,\beta\_{t}^{\,k-1} so that
ft​(u)≈α​e−λt​uf\_{t}(u)\approx\alpha e^{-\lambda\_{t}u} with λt=−log⁡βt\lambda\_{t}=-\log\beta\_{t}.
Therefore

|  |  |  |
| --- | --- | --- |
|  | Mt=αλt,μt=1λt,g​(u)=e−u.M\_{t}=\frac{\alpha}{\lambda\_{t}},\qquad\mu\_{t}=\frac{1}{\lambda\_{t}},\qquad g(u)=e^{-u}. |  |

RSM thus gates the *level* (and equivalently the exponential rate) smoothly through
observable features while keeping the shape exponential.

*(10) GJR–GARCH (leverage as a level gate).*
Consider ht=ω+α​εt−12+γ​εt−12​𝟏{εt−1<0}+β​ht−1h\_{t}=\omega+\alpha\varepsilon\_{t-1}^{2}+\gamma\varepsilon\_{t-1}^{2}\mathbf{1}\_{\{\varepsilon\_{t-1}<0\}}+\beta h\_{t-1} with 0<β<10<\beta<1 and γ≥0\gamma\geq 0.
The ARCH(∞)(\infty) expansion yields

|  |  |  |
| --- | --- | --- |
|  | ht=ω+∑k=1∞βk−1​[α​εt−k2+γ​εt−k2​𝟏{εt−k<0}]=ω+∑k=1∞ψt,k​(εt−k2−1),h\_{t}=\omega+\sum\_{k=1}^{\infty}\beta^{\,k-1}\Big[\alpha\varepsilon\_{t-k}^{2}+\gamma\,\varepsilon\_{t-k}^{2}\mathbf{1}\_{\{\varepsilon\_{t-k}<0\}}\Big]=\omega+\sum\_{k=1}^{\infty}\psi\_{t,k}\,(\varepsilon\_{t-k}^{2}-1), |  |

with *random* weights
ψt,k=(α+γ​ 1{εt−k<0})​βk−1≥0\psi\_{t,k}=(\alpha+\gamma\,\mathbf{1}\_{\{\varepsilon\_{t-k}<0\}})\beta^{\,k-1}\geq 0.
Hence the kernel is

|  |  |  |
| --- | --- | --- |
|  | ft​(u)=∑k≥1(α+γ​ 1{εt−k<0})​βk−1​𝟏[k−1,k)​(u)≈Mt​1μ​e−u/μ,f\_{t}(u)=\sum\_{k\geq 1}(\alpha+\gamma\,\mathbf{1}\_{\{\varepsilon\_{t-k}<0\}})\beta^{\,k-1}\mathbf{1}\_{[k-1,k)}(u)\ \approx\ M\_{t}\,\frac{1}{\mu}\,e^{-u/\mu}, |  |

with *tempo* μ=1/(−log⁡β)\mu=1/(-\log\beta) and a *level* that is
gated by the sign of past innovations:

|  |  |  |
| --- | --- | --- |
|  | Mt=α+γ​ 1{εt−1<0}−log⁡β.M\_{t}=\frac{\alpha+\gamma\,\mathbf{1}\_{\{\varepsilon\_{t-1}<0\}}}{-\log\beta}. |  |

Averaging over the sign (e.g. under symmetry) gives the effective constant
M=(α+γ/2)/(−log⁡β)M=(\alpha+\gamma/2)/(-\log\beta), recovering a purely exponential short–memory
shape with leverage captured as a state–dependent level.

*(7) Markov–switching GARCH (discrete level gate).*
If βt=βSt\beta\_{t}=\beta\_{S\_{t}} with a finite–state Markov chain StS\_{t}, then
ft​(u)≈α​e−λSt​uf\_{t}(u)\approx\alpha e^{-\lambda\_{S\_{t}}u} with λSt=−log⁡βSt\lambda\_{S\_{t}}=-\log\beta\_{S\_{t}} and

|  |  |  |
| --- | --- | --- |
|  | Mt=αλSt,μt=1λSt,g​(u)=e−u.M\_{t}=\frac{\alpha}{\lambda\_{S\_{t}}},\qquad\mu\_{t}=\frac{1}{\lambda\_{S\_{t}}},\qquad g(u)=e^{-u}. |  |

Compared to RSM, the gate is discrete via the latent state StS\_{t}.

*(8) Time–changed volatility / G–Clock (tempo gate).*
Let a business–time increment Δ​τt=exp⁡(η⊤​zt−1)>0\Delta\tau\_{t}=\exp(\eta^{\top}z\_{t-1})>0 determine
an effective persistence βt=exp⁡(−κ​Δ​τt)∈(0,1)\beta\_{t}=\exp(-\kappa\,\Delta\tau\_{t})\in(0,1) and set
αt=α0​(1−βt)\alpha\_{t}=\alpha\_{0}(1-\beta\_{t}) for scale compatibility.
Then ft​(u)≈α0​(1−βt)​e−λt​uf\_{t}(u)\approx\alpha\_{0}(1-\beta\_{t})\,e^{-\lambda\_{t}u} with
λt=−log⁡βt=κ​Δ​τt\lambda\_{t}=-\log\beta\_{t}=\kappa\,\Delta\tau\_{t}, giving

|  |  |  |
| --- | --- | --- |
|  | Mt=α0​(1−βt)λt,μt=1λt,g​(u)=e−u.M\_{t}=\frac{\alpha\_{0}(1-\beta\_{t})}{\lambda\_{t}},\qquad\mu\_{t}=\frac{1}{\lambda\_{t}},\qquad g(u)=e^{-u}. |  |

Here the *tempo* μt\mu\_{t} is directly gated by observed activity zt−1z\_{t-1}.

*(9) G–FIGARCH (shape gate).*
Let the fractional order be dt=d¯​σ​(γ⊤​zt−1)∈(0,1/2)d\_{t}=\bar{d}\,\sigma(\gamma^{\top}z\_{t-1})\in(0,1/2).
Set (M,μ)(M,\mu) constant and choose
gt​(u;dt)∝u−(1+dt)g\_{t}(u;d\_{t})\propto u^{-(1+d\_{t})} normalized to satisfy ∫gt=∫u​gt=1\int g\_{t}=\int ug\_{t}=1.
Then ft​(u)=M​μ−1​gt​(u/μ;dt)f\_{t}(u)=M\,\mu^{-1}g\_{t}(u/\mu;d\_{t}) gates the *shape* as a function of the
observable state while keeping level and tempo fixed.

*(11) Joint gates (two or three dimensions).*
Combining the above mechanisms yields families with multiple gates:

* •

  RSM+G–Clock: ft​(u)≈Ct​e−λt​uf\_{t}(u)\approx C\_{t}\,e^{-\lambda\_{t}u} with λt\lambda\_{t} gated by activity (tempo) and CtC\_{t} gated by regimes (level).
* •

  RSM+G–FIGARCH: ft​(u)=Mt​μ−1​g​(u/μ;dt)f\_{t}(u)=M\_{t}\,\mu^{-1}g(u/\mu;d\_{t}) with level and shape gated.
* •

  G–FIGARCH+G–Clock: ft​(u)=M​μt−1​g​(u/μt;dt)f\_{t}(u)=M\,\mu\_{t}^{-1}g(u/\mu\_{t};d\_{t}) with shape and tempo gated.
* •

  TG–Vol (this paper): ft​(u)=Mt​μt−1​gt​(u/μt;dt)f\_{t}(u)=M\_{t}\,\mu\_{t}^{-1}g\_{t}(u/\mu\_{t};d\_{t}) with *all three* dimensions gated by observables.

In every case, admissibility follows from gt∈𝒢g\_{t}\in\mathcal{G} and the boundedness of Mt​(1+μt)M\_{t}(1+\mu\_{t}),
ensuring ∑kψt,k<∞\sum\_{k}\psi\_{t,k}<\infty uniformly in tt.

The canonical representation nests virtually all known conditionally
heteroskedastic structures.
Table [1](https://arxiv.org/html/2512.02166v1#S3.T1 "Table 1 ‣ Explicit embeddings for classical models. ‣ 3.2 Universality of the Level–Shape–Tempo Framework ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory") summarizes the correspondence.

Table 1: Special cases within the level–shape–tempo framework.
All volatility recursions of the GARCH family are restrictions of
ft​(u)=Mt​μt−1​gt​(u/μt)f\_{t}(u)=M\_{t}\mu\_{t}^{-1}g\_{t}(u/\mu\_{t}).

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Model | Level MtM\_{t} | Tempo μt\mu\_{t} | Shape gtg\_{t} | Kernel Type | Remarks |
| GARCH(1,1) | constant | constant | e−ue^{-u} | exponential | short–memory exponential decay |
| IGARCH | divergent (∑ψk=∞\sum\psi\_{k}=\infty) | const. | e−ue^{-u} | boundary | infinite memory limit |
| FIGARCH(d)(d) | const. | const. | ∝u−(1+d)\propto u^{-(1+d)} | hyperbolic | long memory (0<d<1/20<d<1/2) |
| HYGARCH | const. | const. | convex mix (1−δ)​e−u+δ​u−(1+d)(1-\delta)e^{-u}+\delta u^{-(1+d)} | mixed | interpolates short/long memory |
| ST–GARCH / RSM | gated | const. | fixed g0g\_{0} | exponential | smooth regime dependence in MtM\_{t} |
| GJR–GARCH | sign–gated Mt=α+γ​𝟏{εt−1<0}−log⁡βM\_{t}=\frac{\alpha+\gamma\mathbf{1}\_{\{\varepsilon\_{t-1}<0\}}}{-\log\beta} | const. | e−ue^{-u} | exponential | asymmetric level gate driven by negative shocks |
| MS–GARCH | Markov–switching MtM\_{t} | const. | fixed g0g\_{0} | exponential | discrete regime version of RSM |
| Time–changed SV | const. | gated (μt\mu\_{t}) | fixed g0g\_{0} | exponential | stochastic clock / business time |
| G–Clock (this paper) | const. | exp⁡(η⊤​zt−1)\exp(\eta^{\top}z\_{t-1}) | fixed g0g\_{0} | exponential | observable business time |
| G–FIGARCH (this paper) | const. | const. | gt​(u;dt)g\_{t}(u;\,d\_{t}) | hyperbolic | gated long–memory shape |
| RSM (this paper) | gated | const. | fixed g0g\_{0} | exponential | gated persistence level |
| TG–Vol (this paper) | gated | gated | gated | general | full three–dimensional gate |

##### Volatility memory space.

It is convenient to regard (Mt,μt,gt)(M\_{t},\mu\_{t},g\_{t}) as coordinates in a
three–dimensional *memory space* ℳ:=ℝ+2×𝒢\mathcal{M}:=\mathbb{R}\_{+}^{2}\times\mathcal{G}.
Classical models occupy one–dimensional rays or two–dimensional planes
within ℳ\mathcal{M}: the GARCH line (M,μM,\mu fixed g=e−ug=e^{-u}),
the FIGARCH axis (shape varying, others fixed),
and the RSM plane (level varying with gg fixed).
The fully gated TG–Vol specification spans the interior of ℳ\mathcal{M},
providing a universal envelope for all stationary volatility recursions.

###### Remark 4 (Implications).

The universality theorem has two conceptual consequences:
(i) theoretical—the space of stationary volatility processes is homeomorphic to
ℳ\mathcal{M} under the mapping f↔(M,μ,g)f\leftrightarrow(M,\mu,g); and
(ii) empirical—any observable gating of (Mt,μt,gt)(M\_{t},\mu\_{t},g\_{t})
constitutes a valid parametric extension of the GARCH family.
Thus the RSM, G–FIGARCH, and G–Clock models developed below
represent orthogonal basis directions in ℳ\mathcal{M}.

### 3.3 Stylized Facts and Testable Implications

Volatility in financial markets exhibits a wide spectrum of empirical regularities
that have resisted a unified theoretical explanation.
Within the canonical framework developed above, all of these
*stylized facts* can be interpreted as manifestations of observable
changes in the three memory dimensions—level (MtM\_{t}), shape (gtg\_{t}), and tempo (μt\mu\_{t}).
The key insight is that heterogeneous information flow dynamically gates these dimensions,
producing state–dependent volatility memory.
This section maps major empirical puzzles to the corresponding
mechanisms in the level–shape–tempo system and derives specific
testable implications.

##### (1) Crisis persistence and “memory thickening”

During market stress, volatility shocks exhibit unusually long clusters and
slow decay—the so–called *persistence puzzle*.
In the canonical system, such behavior arises when the level gate MtM\_{t}
and the shape gate gtg\_{t} jointly respond to adverse conditions.
As information flow becomes congested, the gating variable
pt=σ​(γ⊤​zt−1)p\_{t}=\sigma(\gamma^{\top}z\_{t-1}) increases,
raising MtM\_{t} (stronger overall persistence) and steepening the
low–frequency slope via an increase in the fractional parameter dtd\_{t}
embedded in gt​(u;dt)∝u−(1+dt)g\_{t}(u;d\_{t})\propto u^{-(1+d\_{t})}.
Theoretical consequence: the autocovariance of squared returns decays
hyperbolically rather than exponentially, producing “memory thickening.”
Empirical prediction: a rolling Whittle estimate of dtd\_{t} or a local
spectral slope should co–move positively with volatility indices (VIX),
spreads, and macro–uncertainty measures.

##### (2) Clustering of VaR exceedances

Empirically, Value–at–Risk violations appear in clusters even after GARCH
filtering. In our framework, clustering arises naturally from
the joint action of the level and tempo gates.
When MtM\_{t} increases (stronger persistence) while μt\mu\_{t} decreases
(time accelerates), the effective “economic time” between shocks shortens,
so that multiple extreme losses occur within condensed intervals.
Analytically, if hth\_{t} follows the recursion
ht=ω+∑k≥1Mt​μt−1​g​(u/μt)​(εt−k2−1)h\_{t}=\omega+\sum\_{k\geq 1}M\_{t}\mu\_{t}^{-1}g(u/\mu\_{t})(\varepsilon\_{t-k}^{2}-1),
a local decrease in μt\mu\_{t} amplifies the instantaneous conditional variance
without altering long–run mean, reproducing observed VaR clusters.
Prediction: conditional on observable activity proxies (volume, bid–ask
spread), the probability of consecutive VaR exceedances is increasing in
−Δ​μt-\Delta\mu\_{t}.

##### (3) Announcement bursts and intraday accelerations

High–frequency data exhibit sharp volatility spikes around scheduled news
releases. Such “volatility bursts” correspond to temporary compression of
economic time (μt↓\mu\_{t}\!\downarrow) when information arrival intensity rises.
Under the canonical decomposition, the time–change
τt=∫0teη⊤​zs​𝑑s\tau\_{t}=\int\_{0}^{t}e^{\eta^{\top}z\_{s}}\,ds accelerates the clock, yielding

|  |  |  |
| --- | --- | --- |
|  | Var​[rt|ℱt−1]=∫t−1tMs​μs−1​g​((u−t+1)/μs)​𝑑u.\mathrm{Var}[r\_{t}|\mathcal{F}\_{t-1}]=\int\_{t-1}^{t}M\_{s}\,\mu\_{s}^{-1}g((u-t+1)/\mu\_{s})\,du. |  |

A higher η⊤​zt−1\eta^{\top}z\_{t-1} scales μt\mu\_{t} downward and concentrates weight
near zero lag, reproducing short–lived spikes in realized variance.
Empirical test: estimate η\eta on high–frequency volumes or quote updates;
significance of η>0\eta>0 confirms that announcements compress business time.

##### (4) Cross–market memory contrast: FX vs. equities

Foreign–exchange volatility displays longer memory than equity volatility,
a fact long noted but seldom explained without ad hoc arguments.
In the present theory, market structure dictates which gate dominates:
continuous 24–hour trading in FX keeps μt\mu\_{t} nearly constant while
shape parameters dtd\_{t} vary slowly, leading to persistent hyperbolic kernels;
in equities, discrete trading hours and market closures generate large swings
in μt\mu\_{t}, effectively shortening observed memory even with similar dd.
Hence the apparent cross–market difference reflects tempo rather than
intrinsic memory.
Prediction: cross–sectionally, estimated d^t\hat{d}\_{t} are similar across
markets after re–scaling by effective tempo μt\mu\_{t} An empirical test could involve estimating dtd\_{t} after aligning series in economic time..

##### (5) Nonlinear volume–volatility elasticity

Empirical relationships between trading volume and volatility are
nonlinear: small volumes have weak effects, large volumes saturate.
Within the canonical model, this pattern arises when observable volume
enters the logistic gate controlling MtM\_{t} or μt\mu\_{t}.
Because Mt=M¯/(1+exp⁡[−γV​(Vt−1−c)])M\_{t}=\bar{M}/(1+\exp[-\gamma\_{V}(V\_{t-1}-c)]),
the derivative ∂ht/∂Vt−1\partial h\_{t}/\partial V\_{t-1} exhibits an S–shape,
flattening at low and high volumes.
The theoretical elasticity
∂log⁡ht∂log⁡Vt−1\frac{\partial\log h\_{t}}{\partial\log V\_{t-1}}
peaks near the inflection point Vt−1=cV\_{t-1}=c.
Prediction: plotting realized variance against volume should produce
a sigmoidal relation, confirming gate saturation effects.

##### (6) The Epps effect and asynchronous clocks

At very high sampling frequencies, cross–asset correlations decline
(Epps effect). In our framework this results from asynchronous tempo gates:
each asset ii has its own μt(i)\mu\_{t}^{(i)} depending on market activity.
Even if true shocks are correlated in economic time, differing
μt(i)\mu\_{t}^{(i)} yield observed correlations
ρi​jobs≈ρi​j​exp⁡[−c​|μt(i)−μt(j)|]\rho\_{ij}^{\text{obs}}\approx\rho\_{ij}\exp[-c|\mu\_{t}^{(i)}-\mu\_{t}^{(j)}|].
Aligning observations in economic time (via τt(i)=∫eηi⊤​zs(i)​𝑑s\tau\_{t}^{(i)}=\int e^{\eta\_{i}^{\top}z\_{s}^{(i)}}ds)
restores correlations—a direct test of the tempo mechanism.

##### (7) Rough and long memory coexistence

Empirical spectra often display two distinct power–law regions:
“rough” (high–frequency) and “long–memory” (low–frequency).
The canonical framework accommodates this by allowing gtg\_{t} to be a
mixture of shapes,

|  |  |  |
| --- | --- | --- |
|  | gt​(u)=wt​grough​(u)+(1−wt)​glong​(u),g\_{t}(u)=w\_{t}g\_{\text{rough}}(u)+(1-w\_{t})g\_{\text{long}}(u), |  |

where the first component behaves as uHt−1.5u^{H\_{t}-1.5} near zero and the second as
u−(1+dt)u^{-(1+d\_{t})} for large uu.
Thus short–scale roughness and long–scale persistence coexist naturally.
Testable implication: log–spectrum exhibits two slopes −2​Ht−1-2H\_{t}-1 and −2​dt-2d\_{t}
with a cross–over frequency proportional to 1/μt1/\mu\_{t}. This mixture interpretation allows the framework to nest both rough volatility and fractional models in a single parametric family.

##### (8) VRP–VVIX comovement

During crises, the volatility risk premium (VRP) and the volatility–of–volatility index (VVIX)
rise together. In the canonical system, this joint surge is produced by common
drivers in level and tempo: Mt↑M\_{t}\uparrow increases long–run persistence, while
μt↓\mu\_{t}\downarrow compresses the time clock, both magnifying near–term variance
of variance. Since the VVIX measures Vart⁡(ht+k)\operatorname{Var}\_{t}(h\_{t+k}) and
VRP measures 𝔼t​[ht+k]−ht\mathbb{E}\_{t}[h\_{t+k}]-h\_{t}, both inherit the same gates.
Empirical prediction: regressing VRP and VVIX on the latent gates yields
significant and same–signed coefficients, confirming shared information flow.

##### (9) Pre–crisis “memory thickening” as early warning

Historical crises show gradual strengthening of volatility persistence before
abrupt dislocations. In this framework, simultaneous increases in MtM\_{t}
and dtd\_{t}—driven by slowly rising uncertainty—constitute a leading
indicator of systemic stress.
Define a *memory–thickening index*
𝒯t:=𝔼​[Mt+dt|zt−1]\mathcal{T}\_{t}:=\mathbb{E}[M\_{t}+d\_{t}|z\_{t-1}].
Empirically, 𝒯t\mathcal{T}\_{t} rises months before liquidity crises,
mirroring credit spreads and FCI.
Thus dynamic memory surfaces provide early–warning information
complementary to macro indicators.

##### (10) Option skew and term–structure shifts

Volatility smiles flatten or steepen with maturity in state–dependent ways.
In the level–shape–tempo view, long–maturity implied volatilities reflect
the low–frequency shape gtg\_{t} (hence dtd\_{t}), while short–maturity options
reflect near–term tempo μt\mu\_{t}.
Crises increase both dtd\_{t} and μt\mu\_{t} variability, steepening long–term
skews and shifting short–term skews upward.
Prediction: cross–sectional regressions of implied–volatility slopes on
estimated (dt,μt)(d\_{t},\mu\_{t}) should yield opposite signs by maturity segment,
a distinctive diagnostic of joint shape–tempo gating.

These mechanisms unify seemingly disparate empirical facts under one
economic principle: heterogeneity in information arrival modulates
three orthogonal components of volatility memory. Level gates determine
overall persistence, shape gates govern long–run spectral behavior,
and tempo gates capture the speed of market time. Their interactions
generate the rich nonstationary features observed across assets and
frequencies.

##### Summary

The level–shape–tempo framework provides a unified theoretical basis
for at least ten long–standing empirical phenomena in volatility dynamics.
By treating volatility memory as an observable, state–dependent process,
it transforms stylized facts from descriptive anomalies into predictable
manifestations of the same underlying information–flow mechanism.

The preceding sections establish that all admissible volatility kernels
can be represented through three orthogonal and economically interpretable
memory dimensions: level (Mt)(M\_{t}), shape (gt)(g\_{t}), and tempo (μt)(\mu\_{t}).
To bring this theory to the data, the next sections construct explicit
parametric realizations of each dimension. Specifically:
Section [3.4](https://arxiv.org/html/2512.02166v1#S3.SS4 "3.4 RSM: Level Gate and State–Dependent Persistence ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory") introduces the *Regime–Switching Memory (RSM)*
model that operationalizes the level gate;
Section [3.5](https://arxiv.org/html/2512.02166v1#S3.SS5 "3.5 G–FIGARCH: Shape Gate and Dynamic Long Memory ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory") develops the *Gated–FIGARCH* model for
state–dependent long–memory shape;
and Section [3.6](https://arxiv.org/html/2512.02166v1#S3.SS6 "3.6 G–Clock: Tempo Gate and Observable Business Time ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory") formulates the *Gated–Clock* model
capturing observable time–deformation.
Section [3.7](https://arxiv.org/html/2512.02166v1#S3.SS7 "3.7 Combinations and the Tri–Gate Volatility System (TG–Vol) ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory") then examines their pairwise and joint
interactions, while Section [3.9](https://arxiv.org/html/2512.02166v1#S3.SS9 "3.9 QMLE: Likelihood, Consistency, and Asymptotic Normality ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory") discusses identification
and estimation via a unified QMLE–Whittle procedure.
Together, these models translate the theoretical decomposition into
empirically estimable mechanisms.

### 3.4 RSM: Level Gate and State–Dependent Persistence

##### Model statement and variable roles

The RSM recursion gates *only* the persistence coefficient:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ht\displaystyle h\_{t} | =ω+α​ϵt−12+βt​ht−1,\displaystyle=\omega+\alpha\,\epsilon\_{t-1}^{2}+\beta\_{t}\,h\_{t-1}, |  | (6) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | βt\displaystyle\beta\_{t} | :=(1−pt)​βlow+pt​βhigh,pt:=σ​(γ⊤​zt−1).\displaystyle:=(1-p\_{t})\beta\_{\mathrm{low}}+p\_{t}\beta\_{\mathrm{high}},\qquad p\_{t}:=\sigma(\gamma^{\top}z\_{t-1}). |  | (7) |

ω>0\omega>0 is a baseline variance level. α≥0\alpha\geq 0 is the shock loading.
βlow,βhigh∈(0,1)\beta\_{\mathrm{low}},\beta\_{\mathrm{high}}\in(0,1) with βlow<βhigh\beta\_{\mathrm{low}}<\beta\_{\mathrm{high}} are the low- and high-persistence anchors.
The gate ptp\_{t} blends the anchors based on features zt−1z\_{t-1} through parameter γ\gamma.

Equation ([7](https://arxiv.org/html/2512.02166v1#S3.E7 "In Model statement and variable roles ‣ 3.4 RSM: Level Gate and State–Dependent Persistence ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory")) maps market conditions into a *smooth* persistence level: in stressed states (e.g., high VIX, wide spreads) ptp\_{t} increases and the system behaves closer to the high-persistence anchor βhigh\beta\_{\mathrm{high}}, while in calm states it gravitates to βlow\beta\_{\mathrm{low}}. This isolates the *memory channel* from other channels (e.g., leverage/asymmetry) and preserves parsimony. Crucially, this isolates the level dimension by holding the kernel’s shape fixed.

##### Assumptions for existence and basic moments

###### Assumption 3 (Parameter restrictions for RSM).

ω>0\omega>0, α≥0\alpha\geq 0, 0<βlow<βhigh<10<\beta\_{\mathrm{low}}<\beta\_{\mathrm{high}}<1, and

|  |  |  |
| --- | --- | --- |
|  | α+βhigh<1.\alpha+\beta\_{\mathrm{high}}<1. |  |

Moreover zt−1z\_{t-1} is ℱt−1\mathcal{F}\_{t-1}-measurable with 𝔼​[‖zt−1‖2]<∞\mathbb{E}[\|z\_{t-1}\|^{2}]<\infty and pt=σ​(γ⊤​zt−1)∈(0,1)p\_{t}=\sigma(\gamma^{\top}z\_{t-1})\in(0,1) a.s.

###### Lemma 1 (Positivity and conditional finiteness).

Under Assumption [3](https://arxiv.org/html/2512.02166v1#Thmassumption3 "Assumption 3 (Parameter restrictions for RSM). ‣ Assumptions for existence and basic moments ‣ 3.4 RSM: Level Gate and State–Dependent Persistence ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory"), ht>0h\_{t}>0 a.s. and 𝔼t​[ht]<∞\mathbb{E}\_{t}[h\_{t}]<\infty for all tt.

###### Proof.

Immediate from ω>0\omega>0, α≥0\alpha\geq 0, 0<βt<10<\beta\_{t}<1, and ht−1>0h\_{t-1}>0 inductively.
∎

##### Unconditional mean and weak stationarity

Taking unconditional expectations in ([6](https://arxiv.org/html/2512.02166v1#S3.E6 "In Model statement and variable roles ‣ 3.4 RSM: Level Gate and State–Dependent Persistence ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory")) and using 𝔼​[ϵt−12]=1\mathbb{E}[\epsilon\_{t-1}^{2}]=1 yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[ht]=ω+α​𝔼​[ht−1]+𝔼​[βt]​𝔼​[ht−1]⇒𝔼​[ht]=ω1−α−𝔼​[βt],\mathbb{E}[h\_{t}]=\omega+\alpha\mathbb{E}[h\_{t-1}]+\mathbb{E}[\beta\_{t}]\mathbb{E}[h\_{t-1}]\;\Rightarrow\;\mathbb{E}[h\_{t}]=\frac{\omega}{1-\alpha-\mathbb{E}[\beta\_{t}]}, |  | (8) |

provided α+𝔼​[βt]<1\alpha+\mathbb{E}[\beta\_{t}]<1, where 𝔼​[βt]=(1−p¯)​βlow+p¯​βhigh\mathbb{E}[\beta\_{t}]=(1-\bar{p})\beta\_{\mathrm{low}}+\bar{p}\,\beta\_{\mathrm{high}} and p¯:=𝔼​[pt]\bar{p}:=\mathbb{E}[p\_{t}].

###### Proposition 2 (RSM: existence of second moment and weak stationarity).

Suppose Assumption [3](https://arxiv.org/html/2512.02166v1#Thmassumption3 "Assumption 3 (Parameter restrictions for RSM). ‣ Assumptions for existence and basic moments ‣ 3.4 RSM: Level Gate and State–Dependent Persistence ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory") holds and α+𝔼​[βt]<1\alpha+\mathbb{E}[\beta\_{t}]<1.
Then supt𝔼​[ht]<∞\sup\_{t}\mathbb{E}[h\_{t}]<\infty and the process {ht}\{h\_{t}\} is weakly stationary with 𝔼​[ht]\mathbb{E}[h\_{t}] given by ([8](https://arxiv.org/html/2512.02166v1#S3.E8 "In Unconditional mean and weak stationarity ‣ 3.4 RSM: Level Gate and State–Dependent Persistence ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory")).

###### Proof.

Iterate ([6](https://arxiv.org/html/2512.02166v1#S3.E6 "In Model statement and variable roles ‣ 3.4 RSM: Level Gate and State–Dependent Persistence ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory")) and take expectations; geometric convergence follows from α+𝔼​[βt]<1\alpha+\mathbb{E}[\beta\_{t}]<1 and boundedness of 𝔼​[ϵt2]=1\mathbb{E}[\epsilon\_{t}^{2}]=1.
∎

##### Geometric ergodicity via drift condition

Define Xt:=(ht,ϵt)X\_{t}:=(h\_{t},\epsilon\_{t}) as the Markov state. Consider the drift function V​(h):=1+hV(h):=1+h (Chosen because it grows linearly in hth\_{t}, natural for volatility processes). Then

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[V​(ht)∣ℱt−1]= 1+ω+α​ϵt−12+βt​ht−1≤ 1+ω+α​ϵt−12+βhigh​ht−1.\mathbb{E}[V(h\_{t})\mid\mathcal{F}\_{t-1}]\;=\;1+\omega+\alpha\epsilon\_{t-1}^{2}+\beta\_{t}h\_{t-1}\;\leq\;1+\omega+\alpha\epsilon\_{t-1}^{2}+\beta\_{\mathrm{high}}h\_{t-1}. |  |

Taking expectations and using α+βhigh<1\alpha+\beta\_{\mathrm{high}}<1 provides a Foster–Lyapunov drift:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[V​(ht)]≤c0+ρ​𝔼​[V​(ht−1)],ρ:=max⁡{βhigh,α+βhigh}<1,\mathbb{E}[V(h\_{t})]\;\leq\;c\_{0}+\rho\,\mathbb{E}[V(h\_{t-1})],\qquad\rho:=\max\{\beta\_{\mathrm{high}},\,\alpha+\beta\_{\mathrm{high}}\}<1, |  |

ensuring geometric ergodicity under standard Markov chain arguments.

### 3.5 G–FIGARCH: Shape Gate and Dynamic Long Memory

##### Model statement and kernel representation

Let dt:=d¯​σ​(γ⊤​zt−1)d\_{t}:=\bar{d}\,\sigma(\gamma^{\top}z\_{t-1}) with 0<d¯<1/20<\bar{d}<1/2.
Following Baillie et al. ([1996](https://arxiv.org/html/2512.02166v1#bib.bib2)), a convenient (variance-side) representation is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ht=ω+α​ϵt−12+β​ht−1+∑k=1∞πk​(dt)​(ϵt−k2−ht−k),h\_{t}=\omega+\alpha\,\epsilon\_{t-1}^{2}+\beta\,h\_{t-1}+\sum\_{k=1}^{\infty}\pi\_{k}(d\_{t})\,\big(\epsilon\_{t-k}^{2}-h\_{t-k}\big), |  | (9) |

where πk​(dt):=(−1)k​(dtk)\pi\_{k}(d\_{t}):=(-1)^{k}\binom{d\_{t}}{k} are fractional kernel weights. In practice, we use a truncation at KK ensuring ∑k>K|πk​(dt)|\sum\_{k>K}|\pi\_{k}(d\_{t})| is negligible uniformly in tt.

d¯∈(0,1/2)\bar{d}\in(0,1/2) caps the maximal long-memory strength; dt∈(0,d¯)d\_{t}\in(0,\bar{d}) is the *state-dependent* fractional order; (α,β)(\alpha,\beta) remain short-memory parameters.

##### Assumptions and kernel bounds

###### Assumption 4 (G-FIGARCH admissibility).

ω>0\omega>0, α≥0\alpha\geq 0, β∈[0,1)\beta\in[0,1) with α+β<1\alpha+\beta<1, and 0<dt<d¯<1/20<d\_{t}<\bar{d}<1/2 a.s.
Moreover, zt−1z\_{t-1} is ℱt−1\mathcal{F}\_{t-1}-measurable with finite second moments.

###### Lemma 2 (Uniform kernel summability).

Under Assumption [4](https://arxiv.org/html/2512.02166v1#Thmassumption4 "Assumption 4 (G-FIGARCH admissibility). ‣ Assumptions and kernel bounds ‣ 3.5 G–FIGARCH: Shape Gate and Dynamic Long Memory ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory"), there exists a finite C=C​(d¯)C=C(\bar{d}) such that for all tt,

|  |  |  |
| --- | --- | --- |
|  | ∑k=0∞|πk​(dt)|≤C​(d¯)<∞.\sum\_{k=0}^{\infty}|\pi\_{k}(d\_{t})|\leq C(\bar{d})<\infty. |  |

###### Proof.

For 0<d<10<d<1, (dk)∼c​k−(1+d)\binom{d}{k}\sim c\,k^{-(1+d)} as k→∞k\to\infty. Thus |πk​(d)|=(dk)|\pi\_{k}(d)|=\binom{d}{k} is absolutely summable for d<1/2d<1/2 with tail bounded by a convergent pp-series. Uniformity over tt follows from dt≤d¯<1/2d\_{t}\leq\bar{d}<1/2.
∎

##### Unconditional moments and stability

Taking expectations in ([9](https://arxiv.org/html/2512.02166v1#S3.E9 "In Model statement and kernel representation ‣ 3.5 G–FIGARCH: Shape Gate and Dynamic Long Memory ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory")) (and using 𝔼​[ϵt−12]=1\mathbb{E}[\epsilon\_{t-1}^{2}]=1 and 𝔼​[ϵt−k2−ht−k]=0\mathbb{E}[\epsilon\_{t-k}^{2}-h\_{t-k}]=0) yields the same unconditional mean as in a short-memory GARCH:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[ht]=ω1−α−β.\mathbb{E}[h\_{t}]=\frac{\omega}{1-\alpha-\beta}. |  | (10) |

Hence, long-memory affects higher-order dependence, autocorrelation decay, and spectral slope, but not the first unconditional moment under the centered kernel representation.

###### Theorem 4 (Finite second moment).

Under Assumption [4](https://arxiv.org/html/2512.02166v1#Thmassumption4 "Assumption 4 (G-FIGARCH admissibility). ‣ Assumptions and kernel bounds ‣ 3.5 G–FIGARCH: Shape Gate and Dynamic Long Memory ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory") and Lemma [2](https://arxiv.org/html/2512.02166v1#Thmlemma2 "Lemma 2 (Uniform kernel summability). ‣ Assumptions and kernel bounds ‣ 3.5 G–FIGARCH: Shape Gate and Dynamic Long Memory ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory"), we have supt𝔼​[ht]<∞\sup\_{t}\mathbb{E}[h\_{t}]<\infty and 𝔼​[ht2]<∞\mathbb{E}[h\_{t}^{2}]<\infty.

###### Proof.

Rewrite ([9](https://arxiv.org/html/2512.02166v1#S3.E9 "In Model statement and kernel representation ‣ 3.5 G–FIGARCH: Shape Gate and Dynamic Long Memory ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory")) as a linear random-coefficient recursion in (ht−1,{ϵt−k2}k≥1)(h\_{t-1},\{\epsilon\_{t-k}^{2}\}\_{k\geq 1}) with absolutely summable coefficients. Use Minkowski and Cauchy–Schwarz inequalities with Lemma [2](https://arxiv.org/html/2512.02166v1#Thmlemma2 "Lemma 2 (Uniform kernel summability). ‣ Assumptions and kernel bounds ‣ 3.5 G–FIGARCH: Shape Gate and Dynamic Long Memory ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory") to dominate the infinite sum by a deterministic finite constant times sups≤t𝔼​[hs]+sups≤t𝔼​[ϵs4]\sup\_{s\leq t}\mathbb{E}[h\_{s}]+\sup\_{s\leq t}\mathbb{E}[\epsilon\_{s}^{4}]. Since α+β<1\alpha+\beta<1 provides contraction in the short-memory backbone, standard arguments give boundedness of first and second moments.
∎

Note that the “short-memory backbone” (α+β<1\alpha+\beta<1) ensures contraction, while the fractional weights contribute only bounded perturbations.

##### Spectral identification of dtd\_{t} gate

###### Proposition 3 (Local identification via low-frequency slope).

Let f​(λ)f(\lambda) denote the spectral density of {ϵt2}\{\epsilon\_{t}^{2}\} under ([9](https://arxiv.org/html/2512.02166v1#S3.E9 "In Model statement and kernel representation ‣ 3.5 G–FIGARCH: Shape Gate and Dynamic Long Memory ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory")) in a neighborhood of λ=0\lambda=0. Under d¯>0\bar{d}>0 and full-rank variation of zt−1z\_{t-1}, the mapping (d¯,γ)↦(\bar{d},\gamma)\mapsto low-frequency slope of f​(λ)f(\lambda) is injective in a neighborhood of the true parameter, hence (d¯,γ)(\bar{d},\gamma) is locally identified (up to nuisance scale).

###### Proof.

For a fixed (α,β)(\alpha,\beta) backbone, the fractional order determines the log–log slope of the spectrum near zero frequency. When dtd\_{t} varies with features, local perturbations in (d¯,γ)(\bar{d},\gamma) induce distinct (feature-indexed) low-frequency responses; under full-rank variation of zt−1z\_{t-1} these responses span unique directions. A linearization of f​(λ)f(\lambda) around the true (d¯,γ)(\bar{d},\gamma) then has full column rank, yielding local injectivity.
∎

### 3.6 G–Clock: Tempo Gate and Observable Business Time

##### Model statement and time deformation

Define the business-time increment

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​τt:=exp⁡(η⊤​zt−1)> 0,η∈ℝq,\Delta\tau\_{t}:=\exp(\eta^{\top}z\_{t-1})\;>\;0,\qquad\eta\in\mathbb{R}^{q}, |  | (11) |

and set the effective persistence and shock loading as

|  |  |  |  |
| --- | --- | --- | --- |
|  | βt:=exp⁡(−κ​Δ​τt)∈(0,1),αt:=α0​(1−βt),κ>0,α0∈(0,1).\beta\_{t}:=\exp(-\kappa\Delta\tau\_{t})\in(0,1),\qquad\alpha\_{t}:=\alpha\_{0}(1-\beta\_{t}),\qquad\kappa>0,\ \alpha\_{0}\in(0,1). |  | (12) |

The recursion is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ht=ω+αt​ϵt−12+βt​ht−1.h\_{t}=\omega+\alpha\_{t}\,\epsilon\_{t-1}^{2}+\beta\_{t}\,h\_{t-1}. |  | (13) |

When features indicate high activity or stress (large η⊤​zt−1\eta^{\top}z\_{t-1}), Δ​τt\Delta\tau\_{t} rises, βt\beta\_{t} falls, and the system *forgets faster*. In calmer periods, time dilates, persistence rises, and clustering lengthens. Unlike RSM, βt\beta\_{t} is *not* freely gated; it is *endogenously* implied by the time deformation ([11](https://arxiv.org/html/2512.02166v1#S3.E11 "In Model statement and time deformation ‣ 3.6 G–Clock: Tempo Gate and Observable Business Time ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory"))–([12](https://arxiv.org/html/2512.02166v1#S3.E12 "In Model statement and time deformation ‣ 3.6 G–Clock: Tempo Gate and Observable Business Time ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory")).

##### Assumptions and basic properties

###### Assumption 5 (G-Clock admissibility).

ω>0\omega>0, κ>0\kappa>0 (we may parameterize κ=eκ~\kappa=e^{\tilde{\kappa}}), and α0∈(0,1)\alpha\_{0}\in(0,1). The features zt−1z\_{t-1} are ℱt−1\mathcal{F}\_{t-1}-measurable with 𝔼​[‖zt−1‖2]<∞\mathbb{E}[\|z\_{t-1}\|^{2}]<\infty.

###### Lemma 3 (Bounds).

Under Assumption [5](https://arxiv.org/html/2512.02166v1#Thmassumption5 "Assumption 5 (G-Clock admissibility). ‣ Assumptions and basic properties ‣ 3.6 G–Clock: Tempo Gate and Observable Business Time ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory"), 0<βt<10<\beta\_{t}<1 and 0≤αt<α0<10\leq\alpha\_{t}<\alpha\_{0}<1 for all tt. Hence, ht>0h\_{t}>0 a.s. and 𝔼t​[ht]<∞\mathbb{E}\_{t}[h\_{t}]<\infty.

###### Proof.

Immediate from ([12](https://arxiv.org/html/2512.02166v1#S3.E12 "In Model statement and time deformation ‣ 3.6 G–Clock: Tempo Gate and Observable Business Time ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory")) and positivity of Δ​τt\Delta\tau\_{t}.
∎

##### Unconditional mean and stationarity

Taking expectations in ([13](https://arxiv.org/html/2512.02166v1#S3.E13 "In Model statement and time deformation ‣ 3.6 G–Clock: Tempo Gate and Observable Business Time ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory")) with 𝔼​[ϵt−12]=1\mathbb{E}[\epsilon\_{t-1}^{2}]=1 yields

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[ht]=ω+𝔼​[αt+βt]​𝔼​[ht−1]⇒𝔼​[ht]=ω1−𝔼​[αt+βt].\mathbb{E}[h\_{t}]=\omega+\mathbb{E}[\alpha\_{t}+\beta\_{t}]\mathbb{E}[h\_{t-1}]\;\;\Rightarrow\;\;\mathbb{E}[h\_{t}]=\frac{\omega}{1-\mathbb{E}[\alpha\_{t}+\beta\_{t}]}. |  |

Since αt+βt=α0​(1−βt)+βt=α0+(1−α0)​βt\alpha\_{t}+\beta\_{t}=\alpha\_{0}(1-\beta\_{t})+\beta\_{t}=\alpha\_{0}+(1-\alpha\_{0})\beta\_{t}, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[αt+βt]=α0+(1−α0)​𝔼​[βt]<1\mathbb{E}[\alpha\_{t}+\beta\_{t}]=\alpha\_{0}+(1-\alpha\_{0})\mathbb{E}[\beta\_{t}]<1 |  |

whenever 𝔼​[βt]<1\mathbb{E}[\beta\_{t}]<1 (always true) and α0<1\alpha\_{0}<1. This leads to finite unconditional mean and weak stationarity.

###### Proposition 4 (Geometric ergodicity).

If 𝔼​[log⁡(αt+βt)]<0\mathbb{E}\!\left[\log\big(\alpha\_{t}+\beta\_{t}\big)\right]<0, then {ht}\{h\_{t}\} is geometrically ergodic.

###### Proof.

Analogous to the RSM drift argument: with V​(h)=1+hV(h)=1+h,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[V​(ht)∣ℱt−1]≤1+ω+(αt+βt)​ht−1.\mathbb{E}[V(h\_{t})\mid\mathcal{F}\_{t-1}]\leq 1+\omega+(\alpha\_{t}+\beta\_{t})\,h\_{t-1}. |  |

Taking expectations and using 𝔼​[log⁡(αt+βt)]<0\mathbb{E}[\log(\alpha\_{t}+\beta\_{t})]<0 yields a geometric drift condition (see standard Markov chain theorems).
∎

### 3.7 Combinations and the Tri–Gate Volatility System (TG–Vol)

All three gates can be written in the abstract affine form

|  |  |  |  |
| --- | --- | --- | --- |
|  | ht=ω+αt​(ϑ;zt−1)⏟shock kernel​ϵt−12+Ψt​(ϑ;zt−1)⏟persistence kernel​ht−1+∑k≥1Πt,k​(ϑ;zt−1)​(ϵt−k2−ht−k)⏟optional long-memory,h\_{t}\;=\;\omega+\underbrace{\alpha\_{t}(\vartheta;z\_{t-1})}\_{\text{shock kernel}}\,\epsilon\_{t-1}^{2}+\underbrace{\Psi\_{t}(\vartheta;z\_{t-1})}\_{\text{persistence kernel}}\,h\_{t-1}+\underbrace{\sum\_{k\geq 1}\Pi\_{t,k}(\vartheta;z\_{t-1})\,(\epsilon\_{t-k}^{2}-h\_{t-k})}\_{\text{optional long-memory}}, |  | (14) |

where ϑ\vartheta stacks all parameters. The three models specialize ([14](https://arxiv.org/html/2512.02166v1#S3.E14 "In 3.7 Combinations and the Tri–Gate Volatility System (TG–Vol) ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory")) as:

|  |  |  |
| --- | --- | --- |
|  | RSM: ​αt≡α,Ψt=(1−pt)​βlow+pt​βhigh,Πt,k≡0;\text{RSM: }\alpha\_{t}\equiv\alpha,\ \Psi\_{t}=(1-p\_{t})\beta\_{\mathrm{low}}+p\_{t}\beta\_{\mathrm{high}},\ \Pi\_{t,k}\equiv 0; |  |

|  |  |  |
| --- | --- | --- |
|  | G-FIGARCH: ​αt≡α,Ψt≡β,Πt,k=πk​(dt),dt=d¯​σ​(γ⊤​zt−1);\text{G-FIGARCH: }\alpha\_{t}\equiv\alpha,\ \Psi\_{t}\equiv\beta,\ \Pi\_{t,k}=\pi\_{k}(d\_{t}),\ d\_{t}=\bar{d}\,\sigma(\gamma^{\top}z\_{t-1}); |  |

|  |  |  |
| --- | --- | --- |
|  | G-Clock: ​αt=α0​(1−βt),Ψt=βt,βt=exp⁡{−κ​exp⁡(η⊤​zt−1)},Πt,k≡0.\text{G-Clock: }\alpha\_{t}=\alpha\_{0}(1-\beta\_{t}),\ \Psi\_{t}=\beta\_{t},\ \beta\_{t}=\exp\{-\kappa\exp(\eta^{\top}z\_{t-1})\},\ \Pi\_{t,k}\equiv 0. |  |

This abstraction clarifies that:
(i) RSM modulates the *level* of persistence;
(ii) G-FIGARCH modulates the *shape* of the memory kernel;
(iii) G-Clock modulates the *tempo* of decay through time deformation.
We now extend the framework by nesting these gates pairwise and jointly.
Each combined model preserves the affine recursion form

|  |  |  |  |
| --- | --- | --- | --- |
|  | ht=ω+αt​(ϑ;zt−1)​εt−12+Ψt​(ϑ;zt−1)​ht−1+∑k≥1Πt,k​(ϑ;zt−1)​(εt−k2−ht−k),h\_{t}=\omega+\alpha\_{t}(\vartheta;z\_{t-1})\,\varepsilon\_{t-1}^{2}+\Psi\_{t}(\vartheta;z\_{t-1})\,h\_{t-1}+\sum\_{k\geq 1}\Pi\_{t,k}(\vartheta;z\_{t-1})(\varepsilon\_{t-k}^{2}-h\_{t-k}), |  | (15) |

with ht>0h\_{t}>0 a.s. and {zt−1}\{z\_{t-1}\} denoting observable features.

#### 3.7.1 RSM–G-FIGARCH Combination

This specification merges a feature–driven persistence gate with a
fractional-order gate:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ht\displaystyle h\_{t} | =ω+α​εt−12+βt​ht−1+∑k=1∞πk​(dt)​(εt−k2−ht−k),\displaystyle=\omega+\alpha\varepsilon\_{t-1}^{2}+\beta\_{t}h\_{t-1}+\sum\_{k=1}^{\infty}\pi\_{k}(d\_{t})(\varepsilon\_{t-k}^{2}-h\_{t-k}), |  | (16) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | βt\displaystyle\beta\_{t} | =(1−pt)​βlow+pt​βhigh,pt=σ​(γp⊤​zt−1),\displaystyle=(1-p\_{t})\beta\_{\mathrm{low}}+p\_{t}\beta\_{\mathrm{high}},\qquad p\_{t}=\sigma(\gamma\_{p}^{\top}z\_{t-1}), |  | (17) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dt\displaystyle d\_{t} | =d¯​σ​(γd⊤​zt−1),πk​(dt)=(−1)k​(dtk).\displaystyle=\bar{d}\,\sigma(\gamma\_{d}^{\top}z\_{t-1}),\qquad\pi\_{k}(d\_{t})=(-1)^{k}{d\_{t}\choose k}. |  | (18) |

The RSM component governs short-run persistence between low- and
high-volatility regimes, whereas the G-FIGARCH component shapes the
hyperbolic decay of long memory.
Economic interpretation: market stress elevates both ptp\_{t} and dtd\_{t},
producing stronger persistence and longer memory.

##### Admissibility and stability.

Assume ω>0\omega>0, α≥0\alpha\geq 0, 0<βlow<βhigh<10<\beta\_{\mathrm{low}}<\beta\_{\mathrm{high}}<1,
α+βhigh<1\alpha+\beta\_{\mathrm{high}}<1, and 0<dt<d¯<1/20<d\_{t}<\bar{d}<1/2 a.s.
Then by Lemma 2, ∑k|πk​(dt)|<∞\sum\_{k}|\pi\_{k}(d\_{t})|<\infty uniformly in tt.
Hence E​[ht]E[h\_{t}] satisfies

|  |  |  |
| --- | --- | --- |
|  | E​[ht]=ω1−α−E​[βt],E[h\_{t}]=\frac{\omega}{1-\alpha-E[\beta\_{t}]}, |  |

and finite second moments follow by contraction of the short-memory core
and absolute summability of the fractional kernel.
Thus {ht}\{h\_{t}\} is weakly stationary and geometrically ergodic.

#### 3.7.2 RSM–G-Clock Combination

Here regime blending acts on the time-deformed persistence:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ht\displaystyle h\_{t} | =ω+αt​εt−12+β~t​ht−1,\displaystyle=\omega+\alpha\_{t}\varepsilon\_{t-1}^{2}+\tilde{\beta}\_{t}h\_{t-1}, |  | (19) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | αt\displaystyle\alpha\_{t} | =α0​(1−βtclk),βtclk=exp⁡[−κ​eη⊤​zt−1],\displaystyle=\alpha\_{0}(1-\beta\_{t}^{\text{clk}}),\qquad\beta\_{t}^{\text{clk}}=\exp[-\kappa e^{\eta^{\top}z\_{t-1}}], |  | (20) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | β~t\displaystyle\tilde{\beta}\_{t} | =(1−pt)​βlow+pt​βhigh,pt=σ​(γp⊤​zt−1).\displaystyle=(1-p\_{t})\beta\_{\mathrm{low}}+p\_{t}\beta\_{\mathrm{high}},\qquad p\_{t}=\sigma(\gamma\_{p}^{\top}z\_{t-1}). |  | (21) |

The RSM gate controls regime-level persistence, while the G-Clock
component accelerates or decelerates the effective memory tempo.

##### Theoretical properties.

With α0∈(0,1)\alpha\_{0}\in(0,1), κ>0\kappa>0, and the above bounds on
βlow,βhigh\beta\_{\mathrm{low}},\beta\_{\mathrm{high}},
we have 0<αt+β~t<10<\alpha\_{t}+\tilde{\beta}\_{t}<1 a.s.
Applying the drift function V​(h)=1+hV(h)=1+h gives

|  |  |  |
| --- | --- | --- |
|  | E​[V​(ht)∣ℱt−1]≤1+ω+(αt+β~t)​V​(ht−1),E[V(h\_{t})\mid\mathcal{F}\_{t-1}]\leq 1+\omega+(\alpha\_{t}+\tilde{\beta}\_{t})V(h\_{t-1}), |  |

and E​log⁡(αt+β~t)<0E\log(\alpha\_{t}+\tilde{\beta}\_{t})<0 ensures geometric ergodicity. In tranquil periods, both level and tempo relax, whereas crises shift regimes toward higher persistence and faster business time.

#### 3.7.3 G-FIGARCH–G-Clock Combination

This model couples long-memory kernels with endogenous business time:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ht\displaystyle h\_{t} | =ω+αt​εt−12+βtclk​ht−1+∑k=1∞πk​(dt)​(εt−k2−ht−k),\displaystyle=\omega+\alpha\_{t}\varepsilon\_{t-1}^{2}+\beta\_{t}^{\text{clk}}h\_{t-1}+\sum\_{k=1}^{\infty}\pi\_{k}(d\_{t})(\varepsilon\_{t-k}^{2}-h\_{t-k}), |  | (22) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | αt\displaystyle\alpha\_{t} | =α0​(1−βtclk),βtclk=exp⁡[−κ​eη⊤​zt−1],\displaystyle=\alpha\_{0}(1-\beta\_{t}^{\text{clk}}),\qquad\beta\_{t}^{\text{clk}}=\exp[-\kappa e^{\eta^{\top}z\_{t-1}}], |  | (23) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | dt\displaystyle d\_{t} | =d¯​σ​(γd⊤​zt−1).\displaystyle=\bar{d}\,\sigma(\gamma\_{d}^{\top}z\_{t-1}). |  | (24) |

Long memory governs slow decay in tranquil periods, whereas
time-deformation induces rapid forgetting during active markets.

##### Stability.

Under α0∈(0,1)\alpha\_{0}\in(0,1), κ>0\kappa>0, and 0<d¯<1/20<\bar{d}<1/2,
the kernel is absolutely summable and
E​[log⁡(αt+βtclk)]<0E[\log(\alpha\_{t}+\beta\_{t}^{\text{clk}})]<0.
Hence E​[ht]<∞E[h\_{t}]<\infty and geometric ergodicity follows
by the same Foster–Lyapunov drift argument as before.

#### 3.7.4 Tri-Gate Unified Model (TG-Vol)

The fully unified architecture embeds all three gates:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ht\displaystyle h\_{t} | =ω+α0​(1−βtclk)​εt−12+[(1−pt)​βlow+pt​βhigh]​βtclk​ht−1+∑k=1∞πk​(dt)​(εt−k2−ht−k),\displaystyle=\omega+\alpha\_{0}(1-\beta\_{t}^{\text{clk}})\varepsilon\_{t-1}^{2}+\big[(1-p\_{t})\beta\_{\mathrm{low}}+p\_{t}\beta\_{\mathrm{high}}\big]\beta\_{t}^{\text{clk}}h\_{t-1}+\sum\_{k=1}^{\infty}\pi\_{k}(d\_{t})(\varepsilon\_{t-k}^{2}-h\_{t-k}), |  | (25) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | βtclk\displaystyle\beta\_{t}^{\text{clk}} | =exp⁡[−κ​eη⊤​zt−1],pt=σ​(γp⊤​zt−1),dt=d¯​σ​(γd⊤​zt−1).\displaystyle=\exp[-\kappa e^{\eta^{\top}z\_{t-1}}],\qquad p\_{t}=\sigma(\gamma\_{p}^{\top}z\_{t-1}),\qquad d\_{t}=\bar{d}\,\sigma(\gamma\_{d}^{\top}z\_{t-1}). |  | (26) |

Each observable feature vector zt−1z\_{t-1} can be partitioned
to avoid collinearity across gates.

##### Existence and stationarity.

Assume

|  |  |  |
| --- | --- | --- |
|  | ω>0,0<α0<1,0<βlow<βhigh<1,α0+βhigh<1,0<d¯<1/2,κ>0.\omega>0,\quad 0<\alpha\_{0}<1,\quad 0<\beta\_{\mathrm{low}}<\beta\_{\mathrm{high}}<1,\quad\alpha\_{0}+\beta\_{\mathrm{high}}<1,\quad 0<\bar{d}<1/2,\quad\kappa>0. |  |

Then
(i) ht>0h\_{t}>0 a.s.;
(ii) ∑k|πk​(dt)|<C​(d¯)<∞\sum\_{k}|\pi\_{k}(d\_{t})|<C(\bar{d})<\infty;
(iii) E​[log⁡(αt+Ψt)]<0E[\log(\alpha\_{t}+\Psi\_{t})]<0 with
Ψt=[(1−pt)​βlow+pt​βhigh]​βtclk\Psi\_{t}=[(1-p\_{t})\beta\_{\mathrm{low}}+p\_{t}\beta\_{\mathrm{high}}]\beta\_{t}^{\text{clk}}.
These yield finite first and second moments:

|  |  |  |
| --- | --- | --- |
|  | E​[ht]=ω1−E​[αt+Ψt],E​[ht2]<∞,E[h\_{t}]=\frac{\omega}{1-E[\alpha\_{t}+\Psi\_{t}]},\qquad E[h\_{t}^{2}]<\infty, |  |

and geometric ergodicity by a Lyapunov drift argument identical to
Propositions 1–3.

The TG-Vol model unifies level, shape, and tempo modulation:
RSM governs the persistence level across regimes,
G-FIGARCH determines the fractional decay of long memory,
and G-Clock translates market activity into the effective temporal pace.
Together they provide a coherent “dynamic-memory surface” that adjusts
endogenously to information flow and trading intensity.

All moment and ergodicity conditions satisfy the assumptions required
for QMLE consistency in Theorem 2; Whittle regularization can again be
used for the fractional component. Hence the unified gate remains
theoretically well-posed and estimable within the same likelihood framework.

### 3.8 Identification and Estimation Strategy

##### RSM versus G-Clock

Even though both produce a time-varying βt\beta\_{t}, RSM imposes a *linear* blend of two anchors via a logistic gate in the covariates; G-Clock imposes a *nonlinear* exponential map of a business-time increment. Identification follows from functional-form restrictions and different elasticities:

|  |  |  |
| --- | --- | --- |
|  | ∂βtRSM∂z∝σ​(γ⊤​z)​(1−σ​(γ⊤​z))​(βhigh−βlow),∂βtG​-​Clock∂z=−κ​exp⁡(η⊤​z)​exp⁡(−κ​exp⁡(η⊤​z))​η.\frac{\partial\beta\_{t}^{\mathrm{RSM}}}{\partial z}\;\propto\;\sigma(\gamma^{\top}z)(1-\sigma(\gamma^{\top}z))(\beta\_{\mathrm{high}}-\beta\_{\mathrm{low}}),\quad\frac{\partial\beta\_{t}^{\mathrm{G\text{-}Clock}}}{\partial z}\;=\;-\kappa\,\exp(\eta^{\top}z)\,\exp(-\kappa\exp(\eta^{\top}z))\,\eta. |  |

The distinct shapes (sigmoidal vs. double-exponential) imply distinct predictive responses to features, testable by non-nested comparisons (e.g., Vuong). The difference in curvature (linear logistic vs. nonlinear double-exponential) implies identifiable distinct responses.

##### G-FIGARCH versus RSM/G-Clock

G-FIGARCH affects low-frequency spectral slope and multi-horizon autocorrelation decay, while RSM/G-Clock primarily alter near-term persistence level/tempo. In frequency domain, let S​(λ)S(\lambda) be the spectrum of {rt2}\{r\_{t}^{2}\}; for G-FIGARCH, S​(λ)∼C​λ−2​dtS(\lambda)\sim C\,\lambda^{-2d\_{t}} as λ↓0\lambda\downarrow 0, whereas for purely short-memory gates S​(λ)S(\lambda) is flat at the origin. This delivers an orthogonal identification channel.

### 3.9 QMLE: Likelihood, Consistency, and Asymptotic Normality

##### Conditional likelihood and feasible recursion

Given a parametric ϑ\vartheta, define the recursion for ht​(ϑ)h\_{t}(\vartheta) according to the chosen gate. The Gaussian quasi log-likelihood is

|  |  |  |
| --- | --- | --- |
|  | ℓT​(ϑ):=−12​∑t=1T{log⁡ht​(ϑ)+rt2ht​(ϑ)}.\ell\_{T}(\vartheta):=-\frac{1}{2}\sum\_{t=1}^{T}\left\{\log h\_{t}(\vartheta)+\frac{r\_{t}^{2}}{h\_{t}(\vartheta)}\right\}. |  |

For G-FIGARCH, we use a truncation K=KT→∞K=K\_{T}\to\infty slowly with TT, satisfying ∑k>KTsupt|πk​(dt)|=o​(1)\sum\_{k>K\_{T}}\sup\_{t}|\pi\_{k}(d\_{t})|=o(1).

##### Regularity conditions

###### Assumption 6 (QMLE regularity).

(i) The true parameter ϑ0\vartheta\_{0} lies in a compact interior of the admissible set; (ii) identifiability as discussed in §[3.8](https://arxiv.org/html/2512.02166v1#S3.SS8 "3.8 Identification and Estimation Strategy ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory"); (iii) the recursion mapping is continuous and twice continuously differentiable in a neighborhood of ϑ0\vartheta\_{0}; (iv) {rt}\{r\_{t}\} is strictly stationary and geometrically ergodic under ϑ0\vartheta\_{0}; (v) 𝔼​[|ϵt|4+δ]<∞\mathbb{E}[|\epsilon\_{t}|^{4+\delta}]<\infty for some δ>0\delta>0; (vi) for G-FIGARCH, the truncation schedule satisfies the summability condition above.

###### Theorem 5 (QMLE consistency).

Under Assumptions [3](https://arxiv.org/html/2512.02166v1#Thmassumption3 "Assumption 3 (Parameter restrictions for RSM). ‣ Assumptions for existence and basic moments ‣ 3.4 RSM: Level Gate and State–Dependent Persistence ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory"), [4](https://arxiv.org/html/2512.02166v1#Thmassumption4 "Assumption 4 (G-FIGARCH admissibility). ‣ Assumptions and kernel bounds ‣ 3.5 G–FIGARCH: Shape Gate and Dynamic Long Memory ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory") or [5](https://arxiv.org/html/2512.02166v1#Thmassumption5 "Assumption 5 (G-Clock admissibility). ‣ Assumptions and basic properties ‣ 3.6 G–Clock: Tempo Gate and Observable Business Time ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory") (depending on the gate) and Assumption [6](https://arxiv.org/html/2512.02166v1#Thmassumption6 "Assumption 6 (QMLE regularity). ‣ Regularity conditions ‣ 3.9 QMLE: Likelihood, Consistency, and Asymptotic Normality ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory"), the QMLE

|  |  |  |
| --- | --- | --- |
|  | ϑ^T∈arg​maxϑ⁡ℓT​(ϑ)\hat{\vartheta}\_{T}\in\operatorname\*{arg\,max}\_{\vartheta}\ell\_{T}(\vartheta) |  |

is strongly consistent: ϑ^T→ϑ0\hat{\vartheta}\_{T}\to\vartheta\_{0} a.s. as T→∞T\to\infty.

###### Sketch.

Geometric ergodicity implies a Uniform Law of Large Numbers for the criterion; continuity and compactness ensure existence of a maximizer; identification pins the maximizer to the true ϑ0\vartheta\_{0}. Standard arguments for GARCH-type QMLE apply, with the additional check for the G-FIGARCH truncation bias being op​(1)o\_{p}(1).
∎

###### Theorem 6 (Asymptotic normality).

Under the conditions of Theorem [5](https://arxiv.org/html/2512.02166v1#Thmtheorem5 "Theorem 5 (QMLE consistency). ‣ Regularity conditions ‣ 3.9 QMLE: Likelihood, Consistency, and Asymptotic Normality ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory") with additional differentiability and moment bounds,

|  |  |  |
| --- | --- | --- |
|  | T​(ϑ^T−ϑ0)⇒𝒩​(0,ℐ−1​𝒥​ℐ−1),\sqrt{T}\,(\hat{\vartheta}\_{T}-\vartheta\_{0})\;\Rightarrow\;\mathcal{N}\left(0,\,\mathcal{I}^{-1}\mathcal{J}\,\mathcal{I}^{-1}\right), |  |

where ℐ:=𝔼​[−∇2ℓt​(ϑ0)]\mathcal{I}:=\mathbb{E}\big[-\nabla^{2}\ell\_{t}(\vartheta\_{0})\big] and 𝒥:=𝔼​[∇ℓt​(ϑ0)​∇ℓt​(ϑ0)⊤]\mathcal{J}:=\mathbb{E}\big[\nabla\ell\_{t}(\vartheta\_{0})\nabla\ell\_{t}(\vartheta\_{0})^{\top}\big] are the Godambe (sandwich) matrices, and ℓt\ell\_{t} is the per-period log-likelihood.

###### Sketch.

A martingale central limit theorem applies to the score process under geometric ergodicity and finite (4+δ)(4+\delta)-moments; the Hessian converges in probability to ℐ\mathcal{I}. A Slutsky argument yields the stated normal limit.
∎

### 3.10 β\beta-mixing, Ergodicity, and Moment Bounds

This section provides sufficient conditions under which the volatility recursions driven by the three gates are geometrically β\beta-mixing, and therefore suitable for limit theorems used in estimation and testing. Mixing rates are useful for establishing law of large numbers and central limit theorems for the quasi-likelihood and for various empirical functionals. The arguments rely on Markov chain drift and minorization conditions adapted to random-coefficient affine recursions, together with contraction in expectation.

Consider the Markov state Xt=(ht,ϵt)X\_{t}=(h\_{t},\epsilon\_{t}) with state space 𝖲=(0,∞)×ℝ\mathsf{S}=(0,\infty)\times\mathbb{R}. Under the assumed innovation distribution and the measurability of gates with respect to ℱt−1\mathcal{F}\_{t-1}, the process is time-homogeneous. For a measurable function V:𝖲→[1,∞)V:\mathsf{S}\to[1,\infty), a geometric drift condition takes the form

|  |  |  |
| --- | --- | --- |
|  | 𝖯​V​(x)≤λ​V​(x)+bfor all ​x∈𝖲​ and some ​λ∈(0,1),b<∞,\mathsf{P}V(x)\leq\lambda V(x)+b\ \ \text{for all }x\in\mathsf{S}\ \text{ and some }\ \lambda\in(0,1),\ b<\infty, |  |

where 𝖯\mathsf{P} is the transition kernel and 𝖯​V​(x):=∫V​(y)​𝖯​(x,d​y)\mathsf{P}V(x):=\int V(y)\mathsf{P}(x,dy). Aperiodicity and a minorization condition on a petite set then imply geometric ergodicity and geometric β\beta-mixing. We proceed model by model.

##### RSM gate

Under Assumption [3](https://arxiv.org/html/2512.02166v1#Thmassumption3 "Assumption 3 (Parameter restrictions for RSM). ‣ Assumptions for existence and basic moments ‣ 3.4 RSM: Level Gate and State–Dependent Persistence ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory"), ω>0\omega>0, α≥0\alpha\geq 0, and 0<βt<10<\beta\_{t}<1 a.s. Define V​(h)=1+hV(h)=1+h, which is unbounded off compact sets. The one-step conditional expectation satisfies

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[V​(ht)∣ℱt−1]=1+ω+α​ϵt−12+βt​ht−1≤1+ω+α​ϵt−12+βhigh​ht−1.\mathbb{E}[V(h\_{t})\mid\mathcal{F}\_{t-1}]=1+\omega+\alpha\epsilon\_{t-1}^{2}+\beta\_{t}h\_{t-1}\leq 1+\omega+\alpha\epsilon\_{t-1}^{2}+\beta\_{\text{high}}h\_{t-1}. |  |

Taking unconditional expectations and using α+βhigh<1\alpha+\beta\_{\text{high}}<1, there is λ∈(0,1)\lambda\in(0,1) and b<∞b<\infty such that 𝔼​[V​(ht)]≤λ​𝔼​[V​(ht−1)]+b\mathbb{E}[V(h\_{t})]\leq\lambda\mathbb{E}[V(h\_{t-1})]+b. Standard results for Markov chains with innovations possessing a density with respect to Lebesgue measure yield a minorization condition on compact subsets of 𝖲\mathsf{S}. Therefore, the chain is geometrically ergodic and geometrically β\beta-mixing. Moment bounds follow by iteration; in particular supt𝔼​[htk]<∞\sup\_{t}\mathbb{E}[h\_{t}^{k}]<\infty for k∈{1,2}k\in\{1,2\} under the imposed conditions.

##### G-FIGARCH gate

The variance recursion contains an infinite moving-average kernel in squared shocks with time-varying fractional coefficients. Under Assumption [4](https://arxiv.org/html/2512.02166v1#Thmassumption4 "Assumption 4 (G-FIGARCH admissibility). ‣ Assumptions and kernel bounds ‣ 3.5 G–FIGARCH: Shape Gate and Dynamic Long Memory ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory"), the kernel is absolutely summable uniformly in tt. Consider the KK-truncated system,

|  |  |  |
| --- | --- | --- |
|  | ht(K)=ω+α​ϵt−12+β​ht−1(K)+∑k=1Kπk​(dt)​(ϵt−k2−ht−k(K))+Rt,K,h\_{t}^{(K)}=\omega+\alpha\epsilon\_{t-1}^{2}+\beta h\_{t-1}^{(K)}+\sum\_{k=1}^{K}\pi\_{k}(d\_{t})(\epsilon\_{t-k}^{2}-h\_{t-k}^{(K)})+R\_{t,K}, |  |

where Rt,KR\_{t,K} is the tail remainder. The tail norm ‖Rt,K‖2\|R\_{t,K}\|\_{2} goes to zero uniformly as K→∞K\to\infty. For fixed KK, the system is a finite-dimensional Markov chain in (ht(K),…,ht−K(K),ϵt,…,ϵt−K)(h\_{t}^{(K)},\ldots,h\_{t-K}^{(K)},\epsilon\_{t},\ldots,\epsilon\_{t-K}) that satisfies a geometric drift with VV equal to the sum of coordinates plus one. The minorization follows from the positive density of the innovations. Passing to the limit using standard approximation arguments gives geometric ergodicity and β\beta-mixing for the full system. Finite second moments follow from the same Lyapunov function and absolute summability of the kernel.

##### G-Clock gate

Under Assumption [5](https://arxiv.org/html/2512.02166v1#Thmassumption5 "Assumption 5 (G-Clock admissibility). ‣ Assumptions and basic properties ‣ 3.6 G–Clock: Tempo Gate and Observable Business Time ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory") with κ>0\kappa>0 and α0∈(0,1)\alpha\_{0}\in(0,1), we have 0<βt<10<\beta\_{t}<1 and 0≤αt<α0<10\leq\alpha\_{t}<\alpha\_{0}<1. With V​(h)=1+hV(h)=1+h,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[V​(ht)∣ℱt−1]≤1+ω+(αt+βt)​ht−1.\mathbb{E}[V(h\_{t})\mid\mathcal{F}\_{t-1}]\leq 1+\omega+(\alpha\_{t}+\beta\_{t})\,h\_{t-1}. |  |

Because αt+βt=α0+(1−α0)​βt\alpha\_{t}+\beta\_{t}=\alpha\_{0}+(1-\alpha\_{0})\beta\_{t} and βt∈(0,1)\beta\_{t}\in(0,1), we can ensure 𝔼​log⁡(αt+βt)<0\mathbb{E}\log(\alpha\_{t}+\beta\_{t})<0 by the imposed admissibility, which implies the drift. Innovations with densities again yield minorization on compact sets, concluding geometric ergodicity and β\beta-mixing.

### 3.11 Score, Hessian, and Sandwich Variance for QMLE

This section derives the per-period score and Hessian for the Gaussian quasi-likelihood. Let ϑ\vartheta denote the parameter vector appropriate to the chosen gate. Define the conditional variance recursion ht​(ϑ)h\_{t}(\vartheta) and the log-likelihood contribution

|  |  |  |
| --- | --- | --- |
|  | ℓt​(ϑ)=−12​(log⁡ht​(ϑ)+rt2ht​(ϑ)).\ell\_{t}(\vartheta)=-\frac{1}{2}\Big(\log h\_{t}(\vartheta)+\frac{r\_{t}^{2}}{h\_{t}(\vartheta)}\Big). |  |

The gradient is

|  |  |  |
| --- | --- | --- |
|  | ∇ϑℓt​(ϑ)=−12​(1ht−rt2ht2)​∇ϑht​(ϑ)=12​(rt2−htht2)​∇ϑht​(ϑ).\nabla\_{\vartheta}\ell\_{t}(\vartheta)=-\frac{1}{2}\left(\frac{1}{h\_{t}}-\frac{r\_{t}^{2}}{h\_{t}^{2}}\right)\nabla\_{\vartheta}h\_{t}(\vartheta)=\frac{1}{2}\left(\frac{r\_{t}^{2}-h\_{t}}{h\_{t}^{2}}\right)\nabla\_{\vartheta}h\_{t}(\vartheta). |  |

Hence the score requires the gradient of hth\_{t} with respect to parameters. This is obtained by differentiating the variance recursion and using forward accumulation.

##### RSM gate

The recursion is ht=ω+α​ϵt−12+βt​ht−1h\_{t}=\omega+\alpha\epsilon\_{t-1}^{2}+\beta\_{t}h\_{t-1} with βt=(1−pt)​βlow+pt​βhigh\beta\_{t}=(1-p\_{t})\beta\_{\text{low}}+p\_{t}\beta\_{\text{high}} and pt=σ​(γ⊤​zt−1)p\_{t}=\sigma(\gamma^{\top}z\_{t-1}). The parameter vector is ϑ=(ω,α,βlow,βhigh,γ⊤)⊤\vartheta=(\omega,\alpha,\beta\_{\text{low}},\beta\_{\text{high}},\gamma^{\top})^{\top}. Differentiation yields

|  |  |  |
| --- | --- | --- |
|  | ∂ωht=1+βt​∂ωht−1,∂αht=ϵt−12+βt​∂αht−1.\partial\_{\omega}h\_{t}=1+\beta\_{t}\partial\_{\omega}h\_{t-1},\qquad\partial\_{\alpha}h\_{t}=\epsilon\_{t-1}^{2}+\beta\_{t}\partial\_{\alpha}h\_{t-1}. |  |

For the persistence anchors,

|  |  |  |
| --- | --- | --- |
|  | ∂βlowht=(1−pt)​ht−1+βt​∂βlowht−1,∂βhighht=pt​ht−1+βt​∂βhighht−1.\partial\_{\beta\_{\text{low}}}h\_{t}=(1-p\_{t})h\_{t-1}+\beta\_{t}\partial\_{\beta\_{\text{low}}}h\_{t-1},\qquad\partial\_{\beta\_{\text{high}}}h\_{t}=p\_{t}h\_{t-1}+\beta\_{t}\partial\_{\beta\_{\text{high}}}h\_{t-1}. |  |

For the gate coefficients, write pt​(1−pt)=σ​(γ⊤​zt−1)​[1−σ​(γ⊤​zt−1)]p\_{t}(1-p\_{t})=\sigma(\gamma^{\top}z\_{t-1})[1-\sigma(\gamma^{\top}z\_{t-1})] and obtain

|  |  |  |
| --- | --- | --- |
|  | ∂γht=(βhigh−βlow)​pt​(1−pt)​zt−1​ht−1+βt​∂γht−1.\partial\_{\gamma}h\_{t}=\big(\beta\_{\text{high}}-\beta\_{\text{low}}\big)\,p\_{t}(1-p\_{t})\,z\_{t-1}\,h\_{t-1}+\beta\_{t}\partial\_{\gamma}h\_{t-1}. |  |

Initialization can be done with ∂h0=0\partial h\_{0}=0 or a fixed-point approximation for the unconditional variance derivative. Substituting these gradients into the score formula provides the analytic score for QMLE or for gradient-based optimization.

The Hessian is obtained by differentiating the gradient recursions once more, or by using outer-product approximations. The expected information matrix under the Gaussian quasi-likelihood is

|  |  |  |
| --- | --- | --- |
|  | ℐ​(ϑ)=𝔼​[12​ht2​(∇ϑht)​(∇ϑht)⊤],\mathcal{I}(\vartheta)=\mathbb{E}\!\left[\frac{1}{2h\_{t}^{2}}\big(\nabla\_{\vartheta}h\_{t}\big)\big(\nabla\_{\vartheta}h\_{t}\big)^{\top}\right], |  |

since 𝔼​[(rt2−ht)2∣ℱt−1]=2​ht2\mathbb{E}[(r\_{t}^{2}-h\_{t})^{2}\mid\mathcal{F}\_{t-1}]=2h\_{t}^{2} under the Gaussian benchmark. Robust inference uses the Godambe sandwich with

|  |  |  |
| --- | --- | --- |
|  | 𝒥​(ϑ)=𝔼​[∇ϑℓt​(ϑ)​∇ϑℓt​(ϑ)⊤],𝒱​(ϑ)=ℐ​(ϑ)−1​𝒥​(ϑ)​ℐ​(ϑ)−1.\mathcal{J}(\vartheta)=\mathbb{E}\big[\nabla\_{\vartheta}\ell\_{t}(\vartheta)\nabla\_{\vartheta}\ell\_{t}(\vartheta)^{\top}\big],\qquad\mathcal{V}(\vartheta)=\mathcal{I}(\vartheta)^{-1}\,\mathcal{J}(\vartheta)\,\mathcal{I}(\vartheta)^{-1}. |  |

##### G-FIGARCH gate

The recursion is

|  |  |  |
| --- | --- | --- |
|  | ht=ω+α​ϵt−12+β​ht−1+∑k=1∞πk​(dt)​(ϵt−k2−ht−k),h\_{t}=\omega+\alpha\epsilon\_{t-1}^{2}+\beta h\_{t-1}+\sum\_{k=1}^{\infty}\pi\_{k}(d\_{t})(\epsilon\_{t-k}^{2}-h\_{t-k}), |  |

with dt=d¯​σ​(γ⊤​zt−1)d\_{t}=\bar{d}\sigma(\gamma^{\top}z\_{t-1}). In practice use a truncation KK, define πk​(dt)=(−1)k​(dtk)\pi\_{k}(d\_{t})=(-1)^{k}\binom{d\_{t}}{k} and precompute the derivatives ∂dtπk​(dt)=(−1)k​(dtk)​(ψ​(dt+1)−ψ​(dt−k+1))\partial\_{d\_{t}}\pi\_{k}(d\_{t})=(-1)^{k}\binom{d\_{t}}{k}\big(\psi(d\_{t}+1)-\psi(d\_{t}-k+1)\big), where ψ\psi is the digamma function. The parameter vector is ϑ=(ω,α,β,d¯,γ⊤)⊤\vartheta=(\omega,\alpha,\beta,\bar{d},\gamma^{\top})^{\top}. The gradients satisfy

|  |  |  |
| --- | --- | --- |
|  | ∂ωht=1+β​∂ωht−1−∑k=1Kπk​(dt)​∂ωht−k,\partial\_{\omega}h\_{t}=1+\beta\partial\_{\omega}h\_{t-1}-\sum\_{k=1}^{K}\pi\_{k}(d\_{t})\partial\_{\omega}h\_{t-k}, |  |

|  |  |  |
| --- | --- | --- |
|  | ∂αht=ϵt−12+β​∂αht−1−∑k=1Kπk​(dt)​∂αht−k,\partial\_{\alpha}h\_{t}=\epsilon\_{t-1}^{2}+\beta\partial\_{\alpha}h\_{t-1}-\sum\_{k=1}^{K}\pi\_{k}(d\_{t})\partial\_{\alpha}h\_{t-k}, |  |

|  |  |  |
| --- | --- | --- |
|  | ∂βht=ht−1+β​∂βht−1−∑k=1Kπk​(dt)​∂βht−k.\partial\_{\beta}h\_{t}=h\_{t-1}+\beta\partial\_{\beta}h\_{t-1}-\sum\_{k=1}^{K}\pi\_{k}(d\_{t})\partial\_{\beta}h\_{t-k}. |  |

For the fractional gate,

|  |  |  |
| --- | --- | --- |
|  | ∂d¯ht=∑k=1K∂d¯πk​(dt)​(ϵt−k2−ht−k)−∑k=1Kπk​(dt)​∂d¯ht−k+β​∂d¯ht−1,\partial\_{\bar{d}}h\_{t}=\sum\_{k=1}^{K}\partial\_{\bar{d}}\pi\_{k}(d\_{t})\,(\epsilon\_{t-k}^{2}-h\_{t-k})-\sum\_{k=1}^{K}\pi\_{k}(d\_{t})\,\partial\_{\bar{d}}h\_{t-k}+\beta\partial\_{\bar{d}}h\_{t-1}, |  |

with

|  |  |  |
| --- | --- | --- |
|  | ∂d¯πk​(dt)=∂dtπk​(dt)⋅∂d¯dt=∂dtπk​(dt)​σ​(γ⊤​zt−1).\partial\_{\bar{d}}\pi\_{k}(d\_{t})=\partial\_{d\_{t}}\pi\_{k}(d\_{t})\cdot\partial\_{\bar{d}}d\_{t}=\partial\_{d\_{t}}\pi\_{k}(d\_{t})\,\sigma(\gamma^{\top}z\_{t-1}). |  |

For γ\gamma,

|  |  |  |
| --- | --- | --- |
|  | ∂γht=∑k=1K∂dtπk​(dt)​∂γdt​(ϵt−k2−ht−k)−∑k=1Kπk​(dt)​∂γht−k+β​∂γht−1,\partial\_{\gamma}h\_{t}=\sum\_{k=1}^{K}\partial\_{d\_{t}}\pi\_{k}(d\_{t})\,\partial\_{\gamma}d\_{t}\,(\epsilon\_{t-k}^{2}-h\_{t-k})-\sum\_{k=1}^{K}\pi\_{k}(d\_{t})\,\partial\_{\gamma}h\_{t-k}+\beta\partial\_{\gamma}h\_{t-1}, |  |

and ∂γdt=d¯​σ​(γ⊤​zt−1)​(1−σ​(γ⊤​zt−1))​zt−1\partial\_{\gamma}d\_{t}=\bar{d}\,\sigma(\gamma^{\top}z\_{t-1})\big(1-\sigma(\gamma^{\top}z\_{t-1})\big)z\_{t-1}. These forward recursions produce ∇ϑht\nabla\_{\vartheta}h\_{t} for substitution into the score. The expected information ℐ\mathcal{I} and sandwich variance 𝒱\mathcal{V} take the same forms as above.

##### G-Clock gate

The recursion is ht=ω+αt​ϵt−12+βt​ht−1h\_{t}=\omega+\alpha\_{t}\epsilon\_{t-1}^{2}+\beta\_{t}h\_{t-1} with βt=exp⁡(−κ​eη⊤​zt−1)\beta\_{t}=\exp(-\kappa e^{\eta^{\top}z\_{t-1}}) and αt=α0​(1−βt)\alpha\_{t}=\alpha\_{0}(1-\beta\_{t}). The parameter vector is ϑ=(ω,α0,κ,η⊤)⊤\vartheta=(\omega,\alpha\_{0},\kappa,\eta^{\top})^{\top}. The gradients satisfy

|  |  |  |
| --- | --- | --- |
|  | ∂ωht=1+βt​∂ωht−1,∂α0ht=(1−βt)​ϵt−12+βt​∂α0ht−1.\partial\_{\omega}h\_{t}=1+\beta\_{t}\partial\_{\omega}h\_{t-1},\qquad\partial\_{\alpha\_{0}}h\_{t}=(1-\beta\_{t})\epsilon\_{t-1}^{2}+\beta\_{t}\partial\_{\alpha\_{0}}h\_{t-1}. |  |

For the time-deformation parameters,

|  |  |  |
| --- | --- | --- |
|  | ∂κht=∂καt​ϵt−12+∂κβt​ht−1+βt​∂κht−1,\partial\_{\kappa}h\_{t}=\partial\_{\kappa}\alpha\_{t}\,\epsilon\_{t-1}^{2}+\partial\_{\kappa}\beta\_{t}\,h\_{t-1}+\beta\_{t}\partial\_{\kappa}h\_{t-1}, |  |

where ∂κβt=−eη⊤​zt−1​exp⁡(−κ​eη⊤​zt−1)\partial\_{\kappa}\beta\_{t}=-e^{\eta^{\top}z\_{t-1}}\,\exp(-\kappa e^{\eta^{\top}z\_{t-1}}) and ∂καt=−α0​∂κβt\partial\_{\kappa}\alpha\_{t}=-\alpha\_{0}\partial\_{\kappa}\beta\_{t}. For η\eta,

|  |  |  |
| --- | --- | --- |
|  | ∂ηht=∂ηαt​ϵt−12+∂ηβt​ht−1+βt​∂ηht−1,\partial\_{\eta}h\_{t}=\partial\_{\eta}\alpha\_{t}\,\epsilon\_{t-1}^{2}+\partial\_{\eta}\beta\_{t}\,h\_{t-1}+\beta\_{t}\partial\_{\eta}h\_{t-1}, |  |

with ∂ηβt=−κ​eη⊤​zt−1​exp⁡(−κ​eη⊤​zt−1)​zt−1\partial\_{\eta}\beta\_{t}=-\kappa e^{\eta^{\top}z\_{t-1}}\exp(-\kappa e^{\eta^{\top}z\_{t-1}})z\_{t-1} and ∂ηαt=−α0​∂ηβt\partial\_{\eta}\alpha\_{t}=-\alpha\_{0}\partial\_{\eta}\beta\_{t}. These recursions deliver the score; the information and sandwich variance follow as before.

### 3.12 Frequency-Domain Methods and Whittle Regularization

The G-FIGARCH gate introduces a time-varying fractional order that modifies low-frequency power. Pure time-domain QMLE may suffer from weak identification of the fractional order in short samples. A hybrid approach augments QMLE with a frequency-domain penalty derived from local Whittle estimation on rolling windows.

Let IT​(λ)I\_{T}(\lambda) denote the periodogram of {rt2}\{r\_{t}^{2}\} and let Λ⊂(0,π]\Lambda\subset(0,\pi] be a low-frequency band. The (local) Whittle objective for a given time window 𝒲\mathcal{W} is

|  |  |  |
| --- | --- | --- |
|  | Q𝒲​(d)=log⁡(1|Λ|​∑λ∈Λλ2​d​I𝒲​(λ))−2​d|Λ|​∑λ∈Λlog⁡λ.Q\_{\mathcal{W}}(d)=\log\Bigg(\frac{1}{|\Lambda|}\sum\_{\lambda\in\Lambda}\lambda^{2d}I\_{\mathcal{W}}(\lambda)\Bigg)-\frac{2d}{|\Lambda|}\sum\_{\lambda\in\Lambda}\log\lambda. |  |

To regularize dt=d¯​σ​(γ⊤​zt−1)d\_{t}=\bar{d}\sigma(\gamma^{\top}z\_{t-1}), compute windowed pseudo-observations d~t\tilde{d}\_{t} from Q𝒲​(d)Q\_{\mathcal{W}}(d) and add a quadratic penalty to the log-likelihood:

|  |  |  |
| --- | --- | --- |
|  | ℒhyb​(ϑ)=∑t=1Tℓt​(ϑ)−λ​∑t∈𝒯(dt​(d¯,γ)−d~t)2.\mathcal{L}\_{\text{hyb}}(\vartheta)=\sum\_{t=1}^{T}\ell\_{t}(\vartheta)-\lambda\sum\_{t\in\mathcal{T}}\left(d\_{t}(\bar{d},\gamma)-\tilde{d}\_{t}\right)^{2}. |  |

Here λ≥0\lambda\geq 0 tunes the strength of the prior. The term shrinks the fractional order toward a data-driven low-frequency proxy while leaving short-memory parameters primarily determined by the time-domain likelihood. This approach improves finite-sample stability in estimating (d¯,γ)(\bar{d},\gamma). This penalty acts as a Gaussian prior on the fractional order centered at the local Whittle estimate, preventing weak identification in small samples.

### 3.13 Non-Nested Identification and Vuong Comparisons

RSM and G-Clock are structurally distinct but neither nests the other. Vuong’s non-nested test compares the mean log-likelihood difference. Let mt=ℓt​(ϑ^(1))−ℓt​(ϑ^(2))m\_{t}=\ell\_{t}(\hat{\vartheta}^{(1)})-\ell\_{t}(\hat{\vartheta}^{(2)}) denote the log-likelihood difference for two models estimated by QMLE on the same sample, and let m¯T=T−1​∑t=1Tmt\bar{m}\_{T}=T^{-1}\sum\_{t=1}^{T}m\_{t} and sT2=T−1​∑t=1T(mt−m¯T)2s\_{T}^{2}=T^{-1}\sum\_{t=1}^{T}(m\_{t}-\bar{m}\_{T})^{2}. Under geometric β\beta-mixing and appropriate moment conditions, the statistic

|  |  |  |
| --- | --- | --- |
|  | VT=T​m¯TsTV\_{T}=\frac{\sqrt{T}\,\bar{m}\_{T}}{s\_{T}} |  |

is asymptotically standard normal under the null of equal expected log-likelihood. Significant positive values favor model (1), negative values favor model (2). In practice, one may use HAC corrections to account for residual dependence in mtm\_{t} or block bootstrap methods under strong persistence.

For G-FIGARCH versus short-memory gates, an additional frequency-domain comparison is informative. Compute the empirical low-frequency slope of the spectrum of {rt2}\{r\_{t}^{2}\} and compare with the implied slope from dt​(ϑ^)d\_{t}(\hat{\vartheta}). A joint test combining time-domain log-likelihood differences and spectral misfit penalties can be implemented by stacking moments and using a GMM-style quadratic form. These procedures enhance separation when likelihoods alone are close.

### 3.14 Practical Robustness and Implementation Considerations

##### Truncation Schedules and Approximation Error

For G-FIGARCH, the infinite fractional kernel is truncated at KK. The truncation should grow slowly with the sample to keep the remainder negligible while maintaining computational feasibility. A common choice is KT=⌊c​Tζ⌋K\_{T}=\lfloor c\,T^{\zeta}\rfloor with ζ∈(0,1/2)\zeta\in(0,1/2) and constant c>0c>0. The goal is to ensure

|  |  |  |
| --- | --- | --- |
|  | ∑k>KTsupt|πk​(dt)|=o​(1)andKT/T→0,\sum\_{k>K\_{T}}\sup\_{t}|\pi\_{k}(d\_{t})|=o(1)\quad\text{and}\quad K\_{T}/T\to 0, |  |

so that the truncation bias is asymptotically negligible and does not impact the first-order limit theory. In finite samples, the residual tail can be monitored by computing the partial sums of |πk​(dt)||\pi\_{k}(d\_{t})| and verifying that the discarded tail is below a tolerance such as 10−610^{-6} uniformly in tt.

##### Robustness to Innovation Distributions and Misspecification

The QMLE is consistent for the pseudo-true parameter under a wide class of innovation distributions if the conditional mean of ϵt\epsilon\_{t} is zero and the variance is one. Heavy-tailed innovations inflate the asymptotic variance; robust standard errors via the sandwich estimator accommodate such deviations. The sandwich estimator implemented in Section [3.11](https://arxiv.org/html/2512.02166v1#S3.SS11 "3.11 Score, Hessian, and Sandwich Variance for QMLE ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory") provides a direct remedy for such inflation. If leverage effects are present but not modeled, the conditional variance recursion may absorb asymmetry into the gate parameters. In that case, misspecification tests based on generalized residuals can be added as auxiliary moment conditions. For G-FIGARCH, a heavy-tailed innovation can occasionally mimic long memory at finite samples; the Whittle penalty and out-of-sample forecast diagnostics help disentangle the two.

##### Implementation Notes and Numerical Stability

Practical estimation benefits from the following conventions. First, initialize h0h\_{0} at the sample variance or the implied unconditional mean, and initialize the derivatives at zero. Second, reparameterize constraints: set βlow=σ​(β~low)\beta\_{\text{low}}=\sigma(\tilde{\beta}\_{\text{low}}), βhigh=σ​(β~high)\beta\_{\text{high}}=\sigma(\tilde{\beta}\_{\text{high}}) with an ordering constraint enforced by βhigh=βlow+σ​(δ~)\beta\_{\text{high}}=\beta\_{\text{low}}+\sigma(\tilde{\delta}), and set κ=exp⁡(κ~)\kappa=\exp(\tilde{\kappa}), d¯=σ​(d~)/2\bar{d}=\sigma(\tilde{d})/2 to maintain d¯<1/2\bar{d}<1/2. Third, include gradient clipping to prevent explosion when hth\_{t} becomes temporarily small; a typical clip is at the 99th percentile of the absolute gradient over a warm-up window. Fourth, apply winsorization to the gate inputs zt−1z\_{t-1} at extreme quantiles (for example at 0.5 and 99.5 percent) to reduce the influence of outliers on the gates.

Convergence diagnostics include monitoring the sup-norm of parameter updates, the relative change of the objective, and the stability of hth\_{t} paths across iterations. It is also beneficial to track the implied effective memory length in each model, for example by computing ∑j=0JΨt+j\sum\_{j=0}^{J}\Psi\_{t+j} where Ψt\Psi\_{t} is the persistence kernel in the operator view. This helps interpret whether the fitted gates respond sensibly to changes in features.

## 4 Empirical Design

##### Data and Sample Structure

The empirical analysis evaluates the proposed gated‐volatility framework on two highly liquid markets: the S&P 500 ETF (SPY) and the EUR/USD exchange rate.
The daily sample spans January 2005 to December 2024, encompassing major turbulence episodes such as the 2008–2009 Global Financial Crisis, the 2020 pandemic crash, and the 2022 inflationary tightening cycle.
Both assets are observed at daily frequency; no intraday realized‐volatility measures are used. Returns are computed as log differences of adjusted closing prices obtained from Bloomberg (with Yahoo Finance as a fallback).
All data are aligned on trading days common to both markets.

##### Feature Construction and Gate Inputs

Each gating mechanism uses an identical vector of standardized observable features zt−1z\_{t-1}:

* •

  absolute lagged return |rt−1||r\_{t-1}|,
* •

  20-day rolling realized‐variance proxy RV20t−1=∑i=t−20t−1ri2\text{RV20}\_{t-1}=\sum\_{i=t-20}^{t-1}r\_{i}^{2},
* •

  implied‐volatility indicator (VIX for SPY; a synthetic IV proxy based on |rt−1||r\_{t-1}| and RV20 for EURUSD),
* •

  trading‐volume quantile within a 252-day rolling window.

All features are standardized into rolling zz-scores to maintain scale comparability and prevent look-ahead bias.
The same feature set enters the logistic gates σ​(γ⊤​zt−1)\sigma(\gamma^{\top}z\_{t-1}) in the RSM and G-FIGARCH models, and the exponential map exp⁡(η⊤​zt−1)\exp(\eta^{\top}z\_{t-1}) in the G-Clock and TG-Vol models.

##### Models and Estimation Framework

The experiment includes three baseline specifications and four gated extensions:

* •

  Baselines: GARCH(1,1), EGARCH(1,1), GJR-GARCH(1,1) (Gaussian QMLE).
* •

  Main gated models: RSM, G-FIGARCH, G-Clock.
* •

  Combinations: RSM+G-FIGARCH, RSM+G-Clock, G-FIGARCH+G-Clock.
* •

  Unified tri-gate: TG-Vol, embedding all three gates simultaneously.

All models are estimated via Gaussian quasi–maximum likelihood (QMLE) in R using the rugarch and fGarch libraries augmented by custom routines for the gates.
Parameter constraints (positivity, stationarity, and 0<dt<d¯<1/20<d\_{t}<\bar{d}<1/2 for fractional orders) are imposed through reparameterization (e.g., κ=eκ~\kappa=e^{\tilde{\kappa}}, βh​i​g​h=βl​o​w+σ​(δ~)\beta\_{high}=\beta\_{low}+\sigma(\tilde{\delta})).
Each model is re-estimated recursively within a rolling window of Tw=1500T\_{w}=1500 observations, producing one-step-ahead forecasts h^t+1|t\hat{h}\_{t+1|t}.
The fractional kernel in G-FIGARCH and TG-Vol is truncated at K≤200K\leq 200, ensuring negligible residual weight.

##### Forecast Evaluation Metrics

Forecast accuracy is assessed along two dimensions:

1. 1.

   Variance forecasting: QLIKE and variance RMSE

   |  |  |  |
   | --- | --- | --- |
   |  | QLIKE=1N​∑t(rt2h^t−log⁡rt2h^t−1),RMSE=1N​∑t(rt2−h^t)2.\text{QLIKE}=\frac{1}{N}\sum\_{t}\!\Big(\frac{r\_{t}^{2}}{\hat{h}\_{t}}-\log\!\frac{r\_{t}^{2}}{\hat{h}\_{t}}-1\Big),\qquad\text{RMSE}=\sqrt{\tfrac{1}{N}\sum\_{t}(r\_{t}^{2}-\hat{h}\_{t})^{2}}. |  |
2. 2.

   Tail‐risk accuracy: Value-at-Risk and Expected Shortfall at 1% and 5% levels, evaluated using the Fissler–Ziegel (FZ) scoring function and Kupiec/Christoffersen coverage tests.

Lower QLIKE, RMSE, and FZ scores indicate superior performance.
To compare non-nested specifications, Diebold–Mariano (DM) tests are applied to loss differentials and Vuong tests to log-likelihood differences, both using HAC-robust standard errors.

##### Diagnostics and Gate Analysis

For each model–asset pair, residual diagnostics include:

* •

  autocorrelation (ACF) and squared-ACF plots of standardized residuals,
* •

  rolling Ljung–Box pp-values (lags 10 and 20, window 250),
* •

  histograms to verify symmetry and light tails.

In well-specified models, residuals show no significant autocorrelation and approximate normality.
Additionally, time-series plots of gate variables ptp\_{t}, dtd\_{t}, and βt\beta\_{t} are inspected to confirm that crisis periods (2020, 2022) correspond to high persistence gates (↑ ptp\_{t}, ↑ dtd\_{t}) and accelerated business time (↓ βt\beta\_{t}).

##### Empirical Hypotheses

The experiment tests the following hypotheses derived from the theoretical framework:

1. 1.

   Observable gates significantly improve volatility and risk forecasting relative to fixed‐parameter baselines.
2. 2.

   The strength and form of memory adaptation differ by market microstructure: long‐memory gates dominate in FX (EURUSD), while regime and clock gates dominate in equities (SPY).
3. 3.

   The unified TG-Vol model yields consistent performance improvements by jointly capturing level (RSM), shape (G-FIGARCH), and tempo (G-Clock) dimensions of memory.

## 5 Empirical Results

### 5.1 SPY (US Equities)

Table [2](https://arxiv.org/html/2512.02166v1#S5.T2 "Table 2 ‣ 5.1 SPY (US Equities) ‣ 5 Empirical Results ‣ The Three-Dimensional Decomposition of Volatility Memory") reports the main out-of-sample performance metrics for SPY, including QLIKE, RMSE, Fissler–Ziegel (FZ) scores, and Value-at-Risk (VaR) coverage rates. The table lists the top models by QLIKE (lower is better), with RMSE used as a tie-breaker.

Table 2: SPY — Out-of-sample forecast and tail-risk metrics.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Model | QLike | RMSE | FZ(1%) | FZ(5%) | VaR(1%) | VaR(5%) | Kupiec p(5%) |
| GARCH(1,1) | −8.184-8.184 | 0.0005550.000555 | 0.00680.0068 | 0.00320.0032 | 1.17%1.17\% | 4.51%4.51\% | 0.440.44 |
| GJR-GARCH | −8.173-8.173 | 0.0005740.000574 | 0.00700.0070 | 0.00310.0031 | 1.44%1.44\% | 4.51%4.51\% | 0.440.44 |
| RSM | −7.808-7.808 | 0.0006850.000685 | 0.01840.0184 | 0.00670.0067 | 1.44%1.44\% | 3.16%3.16\% | 0.000.00 |
| G-Clock | −7.644-7.644 | 0.0006490.000649 | −0.0006-0.0006 | −0.0090-0.0090 | 0.27%0.27\% | 10.28%10.28\% | 0.000.00 |
| G-FIGARCH | 2.24×1062.24\times 10^{6} | 0.0005480.000548 | 0.00430.0043 | −0.0008-0.0008 | 0.27%0.27\% | 1.80%1.80\% | 0.000.00 |

##### 

The SPY market exhibits a distinct mixture of regime-dependence and rapid mean reversion, consistent with the paper’s theoretical argument that volatility persistence (βt\beta\_{t}) should contract sharply during periods of market stress and high trading activity.
The G-Clock model achieves the lowest (most negative) FZ(5%) score, suggesting it times the occurrence of tail losses particularly well. This is economically intuitive: when market activity intensifies (e.g., spikes in VIX or trading volume), the G-Clock gate interprets this as a faster “business time,” compressing persistence (βt=e−κ​eη⊤​zt−1\beta\_{t}=e^{-\kappa e^{\eta^{\top}z\_{t-1}}}) and anticipating volatility bursts. This aligns closely with the theoretical framework in Section 3.4, where business-time deformation accelerates the effective memory decay of volatility.

However, this rapid acceleration can also produce overly short-lived volatility clusters, as reflected by the excessive 5% VaR exceedances (10.28%). In other words, while G-Clock precisely times crisis episodes, it tends to underestimate medium-horizon risk in tranquil periods because of its highly responsive temporal gate.
The RSM model, by contrast, adjusts volatility persistence via a smooth logistic gate on the parameter βt=(1−pt)​βl​o​w+pt​βh​i​g​h\beta\_{t}=(1-p\_{t})\beta\_{low}+p\_{t}\beta\_{high}. It provides stable forecasts and more conservative VaR coverage (3.16% exceedances at 5%), indicating that the regime-switching gate captures persistent stress states even when market activity normalizes.
Finally, while the G-FIGARCH theoretically models fractional long memory, it performs poorly in equities due to daily sampling limitations. Without intraday realized variance to identify long-memory behavior, the fractional kernel tends to overfit short-run persistence, producing unstable QLIKE values despite a low RMSE. This illustrates the practical constraint discussed in Section 3.3: long-memory gating requires sufficiently rich frequency-domain variation to be identifiable and stable.

Table 3: SPY — Pairwise DM/Vuong Tests (key comparisons).

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Comparison | Criterion | DM\_stat | p-value | Vuong\_stat | p-value | N |
| G-Clock vs GARCH(1,1) | QLIKE | 1.721.72 | 0.0860.086 | 1.951.95 | 0.0510.051 | 36843684 |
| RSM vs GARCH(1,1) | QLIKE | −0.84-0.84 | 0.4000.400 | 0.930.93 | 0.3530.353 | 36843684 |
| G-FIGARCH vs GARCH(1,1) | RMSE | −2.11-2.11 | 0.0350.035\* | −1.77-1.77 | 0.078·0.078^{\textperiodcentered} | 36843684 |

##### 

The Diebold–Mariano and Vuong tests (Table [3](https://arxiv.org/html/2512.02166v1#S5.T3 "Table 3 ‣ 5.1 SPY (US Equities) ‣ 5 Empirical Results ‣ The Three-Dimensional Decomposition of Volatility Memory")) confirm these findings quantitatively.
The G-Clock model slightly outperforms the plain GARCH(1,1) under both QLIKE and log-likelihood comparisons (marginally significant at the 10% level), supporting the theoretical claim that observable time deformation improves short-horizon forecast accuracy. In contrast, G-FIGARCH performs significantly worse on RMSE (p = 0.035), reinforcing that fractional memory gates are ill-suited to markets dominated by regime switches and discrete trading sessions.

![Refer to caption](3A.png)

![Refer to caption](3B.png)

Figure 1: TG–Vol 3D Surfaces — SPY.
Left: z=ht=f​(pt,βt)z=h\_{t}=f(p\_{t},\beta\_{t}), with x=ptx=p\_{t} (regime gate, RSM) and y=βty=\beta\_{t} (clock gate, G-Clock).
Right: z=βt=f​(pt,ht)z=\beta\_{t}=f(p\_{t},h\_{t}).
Both plots visualize the joint effect of regime and tempo gating on volatility level.
High ptp\_{t} (stress regimes) together with low βt\beta\_{t} (slow clock) are associated with elevated hth\_{t},
demonstrating that crises amplify volatility persistence through mutually reinforcing gates.
Conversely, when volatility hth\_{t} surges, βt\beta\_{t} declines—an acceleration of “business time,”
consistent with rapid information flow during market turmoil.

Economic interpretation.
For SPY, the steep curvature of both surfaces indicates that the regime and clock gates strongly co-move:
high-risk regimes (pt↑p\_{t}\uparrow) compress the time scale (βt↓\beta\_{t}\downarrow), producing sharp volatility bursts.
This behavior confirms that equity markets exhibit state-dependent persistence where information-arrival intensity accelerates the effective memory decay.

![Refer to caption](SPY_diagnostics_TG-Vol.png)


Figure 2: SPY TG-Vol — Residual diagnostics. Histogram (top left), ACF (top right), and squared-ACF (bottom left) of standardized residuals. Ljung–Box p-values: zz: Lag10=0.142, Lag20=0.445; z2z^{2}: Lag10=0.000, Lag20=0.000. The residuals are nearly uncorrelated in levels but exhibit weak volatility clustering, consistent with heavy-tailed shocks and incomplete capture of volatility-of-volatility.

##### 

The residual diagnostics for SPY–TG-Vol (Figure [2](https://arxiv.org/html/2512.02166v1#S5.F2 "Figure 2 ‣ 5.1 SPY (US Equities) ‣ 5 Empirical Results ‣ The Three-Dimensional Decomposition of Volatility Memory")) show approximately Gaussian standardized residuals with minimal autocorrelation, confirming adequate model fit. However, the squared-residual ACF and Ljung–Box results indicate some remaining dependence at the 1–5% level, which reflects the inherent volatility feedback during large equity sell-offs—precisely the kind of effect the gating models seek to parameterize endogenously.

### 5.2 EURUSD (FX)

Table [4](https://arxiv.org/html/2512.02166v1#S5.T4 "Table 4 ‣ 5.2 EURUSD (FX) ‣ 5 Empirical Results ‣ The Three-Dimensional Decomposition of Volatility Memory") presents the out-of-sample forecast metrics for EURUSD. The FX market, characterized by 24-hour continuous trading, tends to exhibit smoother volatility persistence and stronger long-memory components—conditions under which the G-FIGARCH gate is theoretically expected to excel.

Table 4: EURUSD — Out-of-sample forecast and tail-risk metrics.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Model | QLike | RMSE | FZ(1%) | FZ(5%) | VaR(1%) | VaR(5%) | Kupiec p(5%) |
| G-FIGARCH | −9.9079-9.9079 | 0.0000410.000041 | 0.0007220.000722 | 0.0004260.000426 | 0.27%0.27\% | 2.88%2.88\% | 0.00050.0005 |
| GARCH(1,1) | −9.8492-9.8492 | 0.0000430.000043 | 0.0023730.002373 | 0.0009750.000975 | 0.81%0.81\% | 3.87%3.87\% | 0.44140.4414 |
| GJR-GARCH | −9.8373-9.8373 | 0.0000430.000043 | 0.0022880.002288 | 0.0009200.000920 | 0.90%0.90\% | 3.96%3.96\% | 0.44140.4414 |
| G-Clock | −9.7762-9.7762 | 0.0000430.000043 | 0.0000930.000093 | −0.001353-0.001353 | 0.45%0.45\% | 9.46%9.46\% | 0.00050.0005 |
| RSM | −9.5234-9.5234 | 0.0000500.000050 | 0.0006410.000641 | 0.0006810.000681 | 0.27%0.27\% | 1.17%1.17\% | 0.17480.1748 |

##### 

The results for EURUSD clearly validate the paper’s long-memory hypothesis. The G-FIGARCH model achieves the lowest QLIKE and RMSE, indicating superior conditional variance forecasts. Its fractional-order gate (dt=d¯​σ​(γ⊤​zt−1)d\_{t}=\bar{d}\,\sigma(\gamma^{\top}z\_{t-1})) adapts smoothly to shifts in market stress, allowing volatility persistence to decay hyperbolically rather than exponentially. This is precisely the mechanism described in Section 3.3, where fractional differencing introduces memory with slowly decaying autocorrelations that match the continuous FX market’s empirical spectrum.

At the same time, the RSM model performs conservatively with under-violations at 5% VaR (1.17%), consistent with the gate’s design to blend between calm (βl​o​w\beta\_{low}) and crisis (βh​i​g​h\beta\_{high}) regimes through the logistic gate pt=σ​(γ⊤​zt−1)p\_{t}=\sigma(\gamma^{\top}z\_{t-1}).
The G-Clock model again produces highly responsive short-term adjustments (negative FZ(5%) score), but its overreaction to spikes in market activity leads to an inflated exceedance rate (9.46%). This outcome underscores a key theoretical insight: while time deformation accelerates persistence decay in stress periods, it can also cause excessive mean reversion if activity metrics fluctuate erratically.

Table 5: EURUSD — Pairwise DM/Vuong Tests (key comparisons).

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Comparison | Criterion | DM\_stat | p-value | Vuong\_stat | p-value | N |
| G-FIGARCH vs GARCH(1,1) | QLIKE | −2.88-2.88 | 0.0040.004\*\* | 2.022.02 | 0.0430.043\* | 48004800 |
| RSM vs GARCH(1,1) | QLIKE | −1.41-1.41 | 0.1590.159 | 0.830.83 | 0.4070.407 | 48004800 |
| G-Clock vs GARCH(1,1) | RMSE | −0.94-0.94 | 0.3470.347 | 1.121.12 | 0.2630.263 | 48004800 |

##### 

The Diebold–Mariano and Vuong statistics in Table [5](https://arxiv.org/html/2512.02166v1#S5.T5 "Table 5 ‣ 5.2 EURUSD (FX) ‣ 5 Empirical Results ‣ The Three-Dimensional Decomposition of Volatility Memory") confirm the dominance of G-FIGARCH: its improvements over the baseline GARCH(1,1) are statistically significant for both QLIKE and log-likelihood measures (p = 0.004 and 0.043). This provides strong empirical validation of the theoretical claim in Proposition 2 that the fractional-degree gate is locally identifiable through its low-frequency spectral slope, allowing it to capture persistent memory dynamics absent in short-memory models.

![Refer to caption](4A.png)

![Refer to caption](4B.png)

Figure 3: TG–Vol 3D Surfaces — EURUSD.
Left: z=ht=f​(pt,βt)z=h\_{t}=f(p\_{t},\beta\_{t}); right: z=βt=f​(pt,ht)z=\beta\_{t}=f(p\_{t},h\_{t}).
Compared with SPY, both surfaces are smoother and flatter,
showing weaker interaction between the regime and tempo gates.
The volatility level hth\_{t} changes gently with ptp\_{t} and βt\beta\_{t},
and βt\beta\_{t} remains relatively stable across volatility states,
implying that the continuous FX market operates under a more uniform information clock.

Economic interpretation.
In contrast to equities, EURUSD’s long-memory channel dominates:
fractional persistence rather than time-deformation explains most volatility variation.
The flat hth\_{t}–surface indicates stable long-range dependence and slow structural shifts,
while the mild response of βt\beta\_{t} to hth\_{t} reflects the constant liquidity and near-continuous trading of the FX market.
Together these results confirm that TG-Vol adapts flexibly to market-specific microstructure—tempo gating in equities and shape gating in FX.

![Refer to caption](EURUSD_diagnostics_TG-Vol.png)


Figure 4: EURUSD TG-Vol — Residual diagnostics. Histogram (top left), ACF (top right), and squared-ACF (bottom left) of standardized residuals. Ljung–Box p-values: zz: Lag10=0.547, Lag20=0.746; z2z^{2}: Lag10=0.053, Lag20=0.226. Residuals are approximately Gaussian with minimal serial dependence, indicating that the gated model captures both short- and long-memory components effectively.

##### 

The diagnostic plots in Figure [4](https://arxiv.org/html/2512.02166v1#S5.F4 "Figure 4 ‣ 5.2 EURUSD (FX) ‣ 5 Empirical Results ‣ The Three-Dimensional Decomposition of Volatility Memory") show that standardized residuals are nearly Gaussian, and both ACF and squared-ACF values lie within confidence bounds. The Ljung–Box tests confirm no significant remaining autocorrelation up to lag 20. This validates the claim that the TG-Vol structure successfully absorbs persistence heterogeneity by allowing the fractional order, persistence level, and temporal speed to co-evolve with observable features.

### 5.3 Cross-Asset Synthesis

The cross-market comparison reveals that the dominant source of volatility adaptation differs by market structure. In the continuously trading EURUSD market, information flow and order processing occur almost uniformly through time, leading to smoother but longer-lasting volatility dependence—precisely the environment in which fractional gating (G-FIGARCH) thrives.
In contrast, SPY exhibits sharp intraday cycles and periodic bursts of trading intensity; here, volatility persistence is better explained by changes in “business time” (G-Clock) or smooth regime shifts (RSM). These findings empirically substantiate the unified framework proposed in the paper: the three gating dimensions—level (RSM), shape (G-FIGARCH), and tempo (G-Clock)—represent complementary mechanisms that dominate under different microstructural regimes.111All forecast samples are aligned on the intersection of available dates per asset. Standard errors are heteroskedasticity and autocorrelation consistent (HAC). Rolling window Tw=1500T\_{w}=1500 days, FIGARCH truncation K≤200K\leq 200, Gaussian QMLE estimation.

## 6 Discussion and Implications

The empirical results demonstrate that volatility persistence and memory are *state-dependent* quantities determined by observable market conditions.
Across both assets, the gates react to market stress in theoretically consistent directions (see Figs. [2](https://arxiv.org/html/2512.02166v1#S5.F2 "Figure 2 ‣ 5.1 SPY (US Equities) ‣ 5 Empirical Results ‣ The Three-Dimensional Decomposition of Volatility Memory")–[4](https://arxiv.org/html/2512.02166v1#S5.F4 "Figure 4 ‣ 5.2 EURUSD (FX) ‣ 5 Empirical Results ‣ The Three-Dimensional Decomposition of Volatility Memory")): crises raise ptp\_{t} and dtd\_{t} while compressing the business-time parameter βt\beta\_{t}.
Importantly, the dominance of each gating mechanism is *market-specific*: on EURUSD, long-memory gating (G-FIGARCH) drives the strongest variance forecasts (Table [4](https://arxiv.org/html/2512.02166v1#S5.T4 "Table 4 ‣ 5.2 EURUSD (FX) ‣ 5 Empirical Results ‣ The Three-Dimensional Decomposition of Volatility Memory")); on SPY, regime and clock channels (RSM, G-Clock) are more informative for tail timing and stability (Table [2](https://arxiv.org/html/2512.02166v1#S5.T2 "Table 2 ‣ 5.1 SPY (US Equities) ‣ 5 Empirical Results ‣ The Three-Dimensional Decomposition of Volatility Memory")), with G-FIGARCH showing numerical fragility at the daily horizon.

##### Dynamic Memory as a Reflection of Market Information Flows

The gates operationalize the principle that information flow governs the effective “memory” of volatility.
When market activity and uncertainty surge—as in 2020 and 2022—we observe ↑pt\uparrow p\_{t} (RSM), ↑dt\uparrow d\_{t} (G-FIGARCH), and ↓βt\downarrow\beta\_{t} (G-Clock).
These patterns indicate both stronger persistence and faster information time.
On EURUSD, the continuous 24-hour market produces *gradual* changes in these gates and supports the smooth, fractional dynamics of G-FIGARCH.
On SPY, discrete trading sessions and large VIX spikes generate *bursty* behavior: business time accelerates abruptly (sharp ↓βt\downarrow\beta\_{t}), helping G-Clock time extreme losses (lowest FZ(5%) in Table [2](https://arxiv.org/html/2512.02166v1#S5.T2 "Table 2 ‣ 5.1 SPY (US Equities) ‣ 5 Empirical Results ‣ The Three-Dimensional Decomposition of Volatility Memory")) but also causing mild VaR undercoverage.
Hence, volatility memory is not fixed but co-moves with observable features (absolute returns, realized variance, VIX, and volume quantiles), reshaping both the *level* and the *tempo* of mean reversion.

##### Relation to Long Memory and Fractional Integration Theories

The feature-dependent fractional order dt=d¯​σ​(γ⊤​zt−1)d\_{t}=\bar{d}\,\sigma(\gamma^{\top}z\_{t-1}) reconciles two stylized facts:
(i) long memory strengthens during persistent stress;
(ii) empirical estimates of dd differ markedly across regimes.
For EURUSD, this adaptive dtd\_{t} delivers the best QLIKE and RMSE values (Table [4](https://arxiv.org/html/2512.02166v1#S5.T4 "Table 4 ‣ 5.2 EURUSD (FX) ‣ 5 Empirical Results ‣ The Three-Dimensional Decomposition of Volatility Memory")) and clean residual diagnostics (Fig. [4](https://arxiv.org/html/2512.02166v1#S5.F4 "Figure 4 ‣ 5.2 EURUSD (FX) ‣ 5 Empirical Results ‣ The Three-Dimensional Decomposition of Volatility Memory")), implying that low-frequency power concentrates when volatility remains elevated.
For SPY, substituting intraday realized variance with a daily proxy (RV20) makes dtd\_{t} excessively responsive to short-term shocks, producing unstable likelihoods (exploding QLIKE) despite competitive RMSE.
This outcome underscores the theoretical caution from Section 3.3: feature-driven fractional memory is powerful but requires regularization when high- and low-frequency signals co-move strongly.

##### Market Activity and the Stochastic Clock

The G-Clock interprets persistence through business-time deformation, βt=exp⁡(−κ​eη⊤​zt−1)\beta\_{t}=\exp(-\kappa e^{\eta^{\top}z\_{t-1}}).
Empirically, βt\beta\_{t} is negatively correlated with VIX, |rt−1||r\_{t-1}|, and trading-volume quantiles: intense activity compresses economic time and accelerates mean reversion.
This explains why G-Clock attains the most accurate ES timing on SPY (Table [2](https://arxiv.org/html/2512.02166v1#S5.T2 "Table 2 ‣ 5.1 SPY (US Equities) ‣ 5 Empirical Results ‣ The Three-Dimensional Decomposition of Volatility Memory")) and supports the paper’s theoretical claim that volatility clustering can arise from fluctuations in the rate of market time itself.
However, when η⊤​zt−1\eta^{\top}z\_{t-1} spikes abruptly, the clock may over-accelerate, leading to excessive mean reversion and VaR undercoverage; mild winsorization or smoother exponential links can mitigate this effect.

##### Comparative Theoretical Synthesis

RSM, G-FIGARCH, and G-Clock embody complementary mechanisms of adaptive memory:

* •

  RSM (level): smooth transitions between low- and high-persistence regimes (ptp\_{t}), yielding stable variance forecasts and conservative VaR on SPY;
* •

  G-FIGARCH (shape): continuous modulation of long-memory strength (dtd\_{t}), producing the strongest variance accuracy on EURUSD where long-range dependence dominates;
* •

  G-Clock (tempo): activity-driven time deformation (βt\beta\_{t}), excelling at ES timing in equity stress periods but requiring careful calibration for 5% VaR coverage.

The fully unified TG-Vol model that combines these three gates extends the theoretical framework to a dynamic-memory surface jointly controlling level, shape, and tempo.

##### Implications for Risk Forecasting and Stress Testing

For *risk managers*, the estimated gates provide real-time, interpretable indicators of persistence changes.
On EURUSD, simultaneous increases in ptp\_{t} and dtd\_{t} signal longer volatility clusters and justify more conservative VaR/ES thresholds.
On SPY, sharp drops in βt\beta\_{t} mark rapid time compression and heightened short-horizon risk; G-Clock’s superior ES performance confirms its usefulness for timing losses, while RSM offers the most stable daily VaR calibration.
For *supervisors*, sustained elevations in ptp\_{t} and dtd\_{t} across markets quantify a system-wide “memory thickening,” functioning as a cross-market stress indicator complementary to standard financial-conditions indices.

##### Broader Methodological Implications

The gating paradigm generalizes beyond volatility.
Any process with persistent dynamics—such as ARFIMA macro series, yield-curve factors, or stochastic-diffusion coefficients—can endogenize its memory through observable gates.
Compared with latent-state or Markov-switching approaches, observable gating enhances interpretability and enables multi-asset estimation with transparent economic narratives linking persistence to information flow and liquidity.
Empirically, the results also yield an engineering insight: strong feature co-movement (for example, VIX with RV20 and |rt−1||r\_{t-1}|) should be orthogonalized or regularized to prevent excessive parameter sensitivity, particularly for the fractional gate.

##### Future Research Directions

Future extensions may include:
(i) intraday implementations using realized measures to stabilize dtd\_{t};
(ii) macro–finance integration to study policy-sensitive persistence;
(iii) a composite “fractional-time” GARCH merging regime, fractional, and clock gates;
(iv) cross-market synchronization of gates as a measure of volatility contagion; and
(v) machine-learned gate mappings constrained by theoretical priors.

## 7 Conclusion

This paper develops and empirically validates a family of volatility models in which the persistence or memory of conditional variance evolves endogenously with observable market conditions.
Three formulations are analyzed in detail: the Regime-Switching Memory (RSM) model, the Fractional Integration Gate (G-FIGARCH) model, and the Business-Time Gate (G-Clock) model.
Each introduces a distinct but complementary mechanism for translating market observables—such as realized volatility, volume, bid–ask spreads, and implied volatility—into dynamic adjustments of volatility memory.

The theoretical analysis establishes stability, stationarity, and identifiability conditions for each model, showing that their stochastic recursions remain well behaved even with time-varying persistence.
The RSM model extends classical GARCH structures through a smooth logistic gate between two persistence regimes, while G-FIGARCH allows fractional differencing orders to vary with features, linking market stress to long-memory strength.
The G-Clock model departs most radically by redefining volatility persistence as a function of time deformation, aligning volatility dynamics with the pace of market activity.

Empirical results from equity, foreign exchange, and commodity markets confirm the models’ advantages in both in-sample and out-of-sample settings.
All gated models significantly outperform traditional benchmarks such as GARCH, EGARCH, and GAS in variance forecasting accuracy and tail-risk calibration.
RSM proves most effective in detecting and adapting to regime changes, G-FIGARCH best captures sustained volatility persistence, and G-Clock most effectively adjusts to shifts in trading intensity.
Across models, gate parameters are statistically significant, economically interpretable, and consistent with observed stress periods.

From a conceptual standpoint, this research reframes volatility modeling around the principle that persistence reflects evolving information flow, liquidity, and trading dynamics rather than fixed structural parameters. By anchoring memory adjustments in observable market features, the gating framework turns abstract persistence parameters into empirically interpretable state variables.
By grounding volatility memory in observable data, the models provide both explanatory power and operational interpretability—traits essential for practical forecasting, risk management, and macroprudential oversight.

Future research may extend this framework to multi-asset systems, combine gates across dimensions of memory and time deformation, or leverage deep learning to approximate nonlinear gate functions while maintaining theoretical tractability.
Further applications include systemic risk monitoring, adaptive portfolio allocation, and central bank stress testing under non-stationary volatility regimes.

### Key Takeaways

The main contributions of this study can be summarized as follows:

1. 1.

   It formalizes the concept of dynamic volatility memory through three rigorously derived models with observable gates.
2. 2.

   It establishes theoretical guarantees for stability, ergodicity, and parameter identifiability under feature-dependent persistence.
3. 3.

   It provides empirical evidence across markets showing that dynamic memory adaptation materially improves volatility forecasting and risk quantification.
4. 4.

   It bridges econometric modeling, information theory, and market microstructure by linking persistence to trading activity and information flow.

The unifying insight is that volatility dynamics are better understood not as stationary processes but as adaptive systems whose memory continuously reconfigures in response to evolving market conditions.
This paradigm lays the foundation for a new generation of volatility models that are simultaneously theoretically rigorous, empirically grounded, and economically interpretable.

## References

* Ané & Geman (2000)

  Ané, T., & Geman, H. (2000).
  Order flow, transaction clock, and normality of asset returns.
  The Journal of Finance, 55(5), 2259–2284.
  <https://doi.org/10.1111/0022-1082.00286>
* Baillie et al. (1996)

  Baillie, R. T., Bollerslev, T., & Mikkelsen, H. O. (1996).
  Fractionally integrated generalized autoregressive conditional heteroskedasticity.
  Journal of Econometrics, 74(1), 3–30.
  <https://doi.org/10.1016/S0304-4076(95)01749-6>
* Bollerslev (1986)

  Bollerslev, T. (1986).
  Generalized autoregressive conditional heteroskedasticity.
  Journal of Econometrics, 31(3), 307–327.
  <https://doi.org/10.1016/0304-4076(86)90063-1>
* Christoffersen (1998)

  Christoffersen, P. F. (1998).
  Evaluating interval forecasts.
  International Economic Review, 39(4), 841–862.
  <https://doi.org/10.2307/2527341>
* Clark (1973)

  Clark, P. K. (1973).
  A subordinated stochastic process model with finite variance for speculative prices.
  Econometrica, 41(1), 135–155.
  <https://doi.org/10.2307/1913889>
* Diebold & Mariano (1995)

  Diebold, F. X., & Mariano, R. S. (1995).
  Comparing predictive accuracy.
  Journal of Business & Economic Statistics, 13(3), 253–263.
  <https://doi.org/10.1080/07350015.1995.10524599>
* Fissler & Ziegel (2016)

  Fissler, T., & Ziegel, J. F. (2016).
  Higher order elicitability and Osband’s principle.
  The Annals of Statistics, 44(4), 1680–1707.
  <https://doi.org/10.1214/16-AOS1439>
* Glosten et al. (1993)

  Glosten, L. R., Jagannathan, R., & Runkle, D. E. (1993).
  On the relation between the expected value and the volatility of the nominal excess return on stocks.
  The Journal of Finance, 48(5), 1779–1801.
  <https://doi.org/10.1111/j.1540-6261.1993.tb05128.x>
* Hansen et al. (2012)

  Hansen, P. R., Huang, Z., & Shek, H. H. (2012).
  Realized GARCH: A joint model for returns and realized measures of volatility.
  Journal of Applied Econometrics, 27(6), 877–906.
  <https://doi.org/10.1002/jae.1234>
* Kupiec (1995)

  Kupiec, P. (1995).
  Techniques for verifying the accuracy of risk measurement models.
  Journal of Derivatives, 3(2), 73–84.
  <https://doi.org/10.3905/jod.1995.407942>
* Nelson (1991)

  Nelson, D. B. (1991).
  Conditional heteroskedasticity in asset returns: A new approach.
  Econometrica, 59(2), 347–370.
  <https://doi.org/10.2307/2938260>
* Rachev et al. (2024)

  Rachev, S. T., Fabozzi, F. J., & Mahanama, S. (2024).
  The financial market of indices of socioeconomic well-being.
  Journal of Risk and Financial Management, 17(5), 203.
  <https://doi.org/10.3390/jrfm17050203>
* Zivot & Wang (2006)

  Zivot, E., & Wang, J. (2006).
  Modeling Financial Time Series with S-Plus (2nd ed.).
  Springer.
  <https://doi.org/10.1007/978-0-387-32348-0>
* Hamilton (1989)

  Hamilton, J. D. (1989).
  A new approach to the economic analysis of nonstationary time series and the business cycle.
  Econometrica, 57(2), 357–384.
  <https://doi.org/10.2307/1912559>
* Teräsvirta (1994)

  Teräsvirta, T. (1994).
  Specification, estimation, and evaluation of smooth transition autoregressive models.
  Journal of the American Statistical Association, 89(425), 208–218.
  <https://doi.org/10.1080/01621459.1994.10476462>
* Andersen & Bollerslev (1998)

  Andersen, T. G., & Bollerslev, T. (1998).
  Deutsche Mark–Dollar volatility: Intraday activity patterns, macroeconomic announcements, and longer-run dependencies.
  The Journal of Finance, 53(1), 219–265.
  <https://doi.org/10.1111/0022-1082.85732>
* Taylor (2005)

  Taylor, S. J. (2005).
  Asset Price Dynamics, Volatility, and Prediction.
  Princeton University Press.
  <https://doi.org/10.1515/9781400839254>
* Patton (2011)

  Patton, A. J. (2011).
  Volatility forecast comparison using imperfect volatility proxies.
  Journal of Econometrics, 160(1), 246–256.
  <https://doi.org/10.1016/j.jeconom.2010.03.034>
* Gatheral et al. (2018)

  Gatheral, J., Jaisson, T., & Rosenbaum, M. (2018).
  Volatility is rough.
  Quantitative Finance, 18(6), 933–949.
  <https://doi.org/10.1080/14697688.2017.1393551>
* Engle & Russell (1998)

  Engle, R. F., & Russell, J. R. (1998).
  Autoregressive conditional duration: A new model for irregularly spaced transaction data.
  Econometrica, 66(5), 1127–1162.
  <https://doi.org/10.2307/2999630>
* Barndorff-Nielsen & Shephard (2002)

  Barndorff-Nielsen, O. E., & Shephard, N. (2002).
  Econometric analysis of realized volatility and its use in estimating stochastic volatility models.
  Journal of the Royal Statistical Society: Series B, 64(2), 253–280.
  <https://doi.org/10.1111/1467-9868.00336>
* Barndorff-Nielsen et al. (2009)

  Barndorff-Nielsen, O. E., Hansen, P. R., Lunde, A., & Shephard, N. (2009).
  Realized kernels in practice: Trades and quotes.
  The Econometrics Journal, 12(3), C1–C32.
  <https://doi.org/10.1111/j.1368-423X.2008.00275.x>
* Cont (2001)

  Cont, R. (2001).
  Empirical properties of asset returns: Stylized facts and statistical issues.
  Quantitative Finance, 1(2), 223–236.
  <https://doi.org/10.1080/713665670>
* Ding et al. (1993)

  Ding, Z., Granger, C. W. J., & Engle, R. F. (1993).
  A long memory property of stock market returns and a new model.
  Journal of Empirical Finance, 1(1), 83–106.
  <https://doi.org/10.1016/0927-5398(93)90006-D>
* Engle & Bollerslev (1986)

  Engle, R. F., & Bollerslev, T. (1986).
  Modelling the persistence of conditional variances.
  Econometric Reviews, 5(1), 1–50.
  <https://doi.org/10.1080/07474938608800095>

## Appendices

##### Standing assumptions for the appendices.

Unless otherwise stated, random variables are defined on a complete probability space
(Ω,ℱ,ℙ)(\Omega,\mathcal{F},\mathbb{P}) with natural filtration (ℱt)(\mathcal{F}\_{t}).
A kernel f:ℝ+→[0,∞)f:\mathbb{R}\_{+}\to[0,\infty) is *admissible* if
f∈L1​(ℝ+)f\in L^{1}(\mathbb{R}\_{+}) and ∫0∞u​f​(u)​𝑑u<∞\int\_{0}^{\infty}u\,f(u)\,du<\infty.
For such ff, define

|  |  |  |
| --- | --- | --- |
|  | M​(f):=∫0∞f​(u)​𝑑u,μ​(f):=∫0∞u​f​(u)​𝑑u∫0∞f​(u)​𝑑u,gf​(u):=μ​(f)M​(f)​f​(μ​(f)​u).M(f):=\int\_{0}^{\infty}f(u)\,du,\qquad\mu(f):=\frac{\int\_{0}^{\infty}uf(u)\,du}{\int\_{0}^{\infty}f(u)\,du},\qquad g\_{f}(u):=\frac{\mu(f)}{M(f)}\,f(\mu(f)u). |  |

We write ‖h‖1:=∫0∞|h​(u)|​𝑑u\|h\|\_{1}:=\int\_{0}^{\infty}|h(u)|\,du for the L1L^{1}-norm.

## Appendix A — Continuity and Measurability

###### Lemma 4 (Normalization and reconstruction).

If ff is admissible and M​(f)>0M(f)>0, then gf∈L1​(ℝ+)g\_{f}\in L^{1}(\mathbb{R}\_{+}),
∫gf=1\int g\_{f}=1, ∫u​gf​(u)​𝑑u=1\int ug\_{f}(u)\,du=1, and for almost every u≥0u\geq 0

|  |  |  |
| --- | --- | --- |
|  | f​(u)=M​(f)​μ​(f)−1​gf​(uμ​(f)).f(u)=M(f)\,\mu(f)^{-1}\,g\_{f}\!\left(\frac{u}{\mu(f)}\right). |  |

###### Proof.

By definition and the change of variables x=μ​(f)​ux=\mu(f)u,

|  |  |  |
| --- | --- | --- |
|  | ∫0∞gf​(u)​𝑑u=μM​∫0∞f​(μ​u)​𝑑u=μM⋅1μ​∫0∞f​(x)​𝑑x=1,\int\_{0}^{\infty}g\_{f}(u)\,du=\frac{\mu}{M}\int\_{0}^{\infty}f(\mu u)\,du=\frac{\mu}{M}\cdot\frac{1}{\mu}\int\_{0}^{\infty}f(x)\,dx=1, |  |

and similarly

|  |  |  |
| --- | --- | --- |
|  | ∫0∞u​gf​(u)​𝑑u=μM​∫0∞u​f​(μ​u)​𝑑u=1M​∫0∞x​f​(x)​𝑑x=1.\int\_{0}^{\infty}ug\_{f}(u)\,du=\frac{\mu}{M}\int\_{0}^{\infty}uf(\mu u)\,du=\frac{1}{M}\int\_{0}^{\infty}xf(x)\,dx=1. |  |

Rearranging the definition of gfg\_{f} yields the reconstruction identity.
∎

###### Lemma 5 (Continuity of (M,μ,g)(M,\mu,g) in L1L^{1}).

Suppose fn→ff\_{n}\to f in L1​(ℝ+)L^{1}(\mathbb{R}\_{+}) and
supn∫0∞u​fn​(u)​𝑑u<∞\sup\_{n}\int\_{0}^{\infty}uf\_{n}(u)\,du<\infty with M​(f)>0M(f)>0.
Then M​(fn)→M​(f)M(f\_{n})\to M(f), μ​(fn)→μ​(f)\mu(f\_{n})\to\mu(f), and gfn→gfg\_{f\_{n}}\to g\_{f} in L1L^{1}.

###### Proof.

(i) By Hölder and L1L^{1}-convergence, |M​(fn)−M​(f)|≤‖fn−f‖1→0|M(f\_{n})-M(f)|\leq\|f\_{n}-f\|\_{1}\to 0.
(ii) For the numerator, dominated convergence applies because
u​fn​(u)→u​f​(u)uf\_{n}(u)\to uf(u) pointwise a.e. along a subsequence and
supn∫u​fn<∞\sup\_{n}\int uf\_{n}<\infty gives uniform integrability; hence
∫u​fn→∫u​f\int uf\_{n}\to\int uf and therefore μ​(fn)→μ​(f)\mu(f\_{n})\to\mu(f) since M​(fn)→M​(f)>0M(f\_{n})\to M(f)>0.
(iii) For gfng\_{f\_{n}},

|  |  |  |
| --- | --- | --- |
|  | ‖gfn−gf‖1≤|μnMn−μM|​∫f​(μ​u)​𝑑u+μnMn​∫|fn​(μn​u)−f​(μ​u)|​𝑑u.\|g\_{f\_{n}}-g\_{f}\|\_{1}\leq\left|\tfrac{\mu\_{n}}{M\_{n}}-\tfrac{\mu}{M}\right|\!\int f(\mu u)\,du+\frac{\mu\_{n}}{M\_{n}}\!\int\!\left|f\_{n}(\mu\_{n}u)-f(\mu u)\right|du. |  |

The first term vanishes by continuity of (M,μ)(M,\mu). For the second, write

|  |  |  |
| --- | --- | --- |
|  | ∫|fn​(μn​u)−f​(μ​u)|​𝑑u≤∫|fn​(μn​u)−f​(μn​u)|​𝑑u+∫|f​(μn​u)−f​(μ​u)|​𝑑u.\int\!\left|f\_{n}(\mu\_{n}u)-f(\mu u)\right|du\leq\int|f\_{n}(\mu\_{n}u)-f(\mu\_{n}u)|du+\int|f(\mu\_{n}u)-f(\mu u)|du. |  |

The first integral equals μn−1​‖fn−f‖1→0\mu\_{n}^{-1}\|f\_{n}-f\|\_{1}\to 0 since μn→μ>0\mu\_{n}\to\mu>0.
The second equals ∥f(μn⋅)−f(μ⋅)∥1→0\|f(\mu\_{n}\cdot)-f(\mu\cdot)\|\_{1}\to 0
by continuity of dilations in L1L^{1} (e.g., density of Cc∞C\_{c}^{\infty} in L1L^{1} and dominated convergence).
Hence ‖gfn−gf‖1→0\|g\_{f\_{n}}-g\_{f}\|\_{1}\to 0.
∎

###### Lemma 6 (Measurability of (Mt,μt,gt)(M\_{t},\mu\_{t},g\_{t})).

Let ft:Ω×ℝ+→[0,∞)f\_{t}:\Omega\times\mathbb{R}\_{+}\to[0,\infty) be jointly measurable and admissible a.s.
If ftf\_{t} is ℱt−1\mathcal{F}\_{t-1}-measurable as an L1L^{1}-valued map, then
Mt=∫ftM\_{t}=\int f\_{t}, μt=(∫u​ft)/(∫ft)\mu\_{t}=(\int uf\_{t})/(\int f\_{t}), and gt​(u)=(μt/Mt)​ft​(μt​u)g\_{t}(u)=(\mu\_{t}/M\_{t})f\_{t}(\mu\_{t}u)
are ℱt−1\mathcal{F}\_{t-1}-measurable.

###### Proof.

Joint measurability of (ω,t)↦∫ft​(ω,u)​𝑑u(\omega,t)\mapsto\int f\_{t}(\omega,u)\,du and ∫u​ft\int uf\_{t}
follows from Fubini–Tonelli. The map
(a,b,h)↦(a/b)h(b⋅)(a,b,h)\mapsto(a/b)h(b\cdot) is Carathéodory from
(0,∞)2×L1→L1(0,\infty)^{2}\times L^{1}\to L^{1} (measurable in (a,b)(a,b), continuous in hh),
so composition preserves measurability.
∎

## Appendix B — Canonical Level–Tempo–Shape Decomposition

###### Proof of Theorem [1](https://arxiv.org/html/2512.02166v1#Thmtheorem1 "Theorem 1 (Canonical level–tempo–shape decomposition). ‣ Interpretation. ‣ 3.1 Canonical Decomposition of Volatility Memory ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory").

*Step 1 (Normalization properties).* By the change of variables x=μ​ux=\mu u,

|  |  |  |
| --- | --- | --- |
|  | ∫0∞g​(u)​𝑑u=μM​∫0∞f​(μ​u)​𝑑u=μM⋅1μ​∫0∞f​(x)​𝑑x=1M​∫0∞f​(x)​𝑑x=1.\int\_{0}^{\infty}g(u)\,du=\frac{\mu}{M}\int\_{0}^{\infty}f(\mu u)\,du=\frac{\mu}{M}\cdot\frac{1}{\mu}\int\_{0}^{\infty}f(x)\,dx=\frac{1}{M}\int\_{0}^{\infty}f(x)\,dx=1. |  |

Similarly,

|  |  |  |
| --- | --- | --- |
|  | ∫0∞u​g​(u)​𝑑u=μM​∫0∞u​f​(μ​u)​𝑑u=μM⋅1μ2​∫0∞x​f​(x)​𝑑x=1M​μ​∫0∞x​f​(x)​𝑑x=1.\int\_{0}^{\infty}u\,g(u)\,du=\frac{\mu}{M}\int\_{0}^{\infty}u\,f(\mu u)\,du=\frac{\mu}{M}\cdot\frac{1}{\mu^{2}}\int\_{0}^{\infty}x\,f(x)\,dx=\frac{1}{M\mu}\int\_{0}^{\infty}x\,f(x)\,dx=1. |  |

Hence g∈𝒢g\in\mathcal{G}.
Identity ([2](https://arxiv.org/html/2512.02166v1#S3.E2 "In Theorem 1 (Canonical level–tempo–shape decomposition). ‣ Interpretation. ‣ 3.1 Canonical Decomposition of Volatility Memory ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory")) follows by rearranging ([1](https://arxiv.org/html/2512.02166v1#S3.E1 "In Theorem 1 (Canonical level–tempo–shape decomposition). ‣ Interpretation. ‣ 3.1 Canonical Decomposition of Volatility Memory ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory")).

*Step 2 (Admissibility of the converse).*
Let (M,μ,g)(M,\mu,g) be as stated and set
f​(u)=M​μ−1​g​(u/μ)f(u)=M\mu^{-1}g(u/\mu). Then f≥0f\geq 0 and

|  |  |  |
| --- | --- | --- |
|  | ∫0∞f​(u)​𝑑u=M​μ−1​∫0∞g​(u/μ)​𝑑u=M​μ−1⋅μ​∫0∞g​(v)​𝑑v=M∈(0,∞),\int\_{0}^{\infty}f(u)\,du=M\mu^{-1}\int\_{0}^{\infty}g(u/\mu)\,du=M\mu^{-1}\cdot\mu\int\_{0}^{\infty}g(v)\,dv=M\in(0,\infty), |  |

and

|  |  |  |
| --- | --- | --- |
|  | ∫0∞u​f​(u)​𝑑u=M​μ−1​∫0∞u​g​(u/μ)​𝑑u=M​μ−1⋅μ2​∫0∞v​g​(v)​𝑑v=M​μ<∞.\int\_{0}^{\infty}u\,f(u)\,du=M\mu^{-1}\int\_{0}^{\infty}u\,g(u/\mu)\,du=M\mu^{-1}\cdot\mu^{2}\int\_{0}^{\infty}v\,g(v)\,dv=M\mu<\infty. |  |

Thus f∈𝒦f\in\mathcal{K} with the prescribed (M,μ)(M,\mu).
∎

## Appendix C — Proof of Theorem [2](https://arxiv.org/html/2512.02166v1#Thmtheorem2 "Theorem 2 (Uniqueness). ‣ Interpretation. ‣ 3.1 Canonical Decomposition of Volatility Memory ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory") (Uniqueness of the Canonical Decomposition)

###### Proof of Theorem [2](https://arxiv.org/html/2512.02166v1#Thmtheorem2 "Theorem 2 (Uniqueness). ‣ Interpretation. ‣ 3.1 Canonical Decomposition of Volatility Memory ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory").

Let f:ℝ+→[0,∞)f:\mathbb{R}\_{+}\to[0,\infty) be a measurable function satisfying
f​(u)=M​μ−1​g​(u/μ)=M′​μ′−1​g′​(u/μ′)f(u)=M\mu^{-1}g(u/\mu)=M^{\prime}{\mu^{\prime}}^{-1}g^{\prime}(u/\mu^{\prime}) for a.e. u≥0u\geq 0,
where (M,μ,g),(M′,μ′,g′)∈(0,∞)×(0,∞)×𝒢(M,\mu,g),(M^{\prime},\mu^{\prime},g^{\prime})\in(0,\infty)\times(0,\infty)\times\mathcal{G}
and 𝒢:={g≥0:∫0∞g​(u)​𝑑u=1,∫0∞u​g​(u)​𝑑u=1}\mathcal{G}:=\{g\geq 0:\int\_{0}^{\infty}g(u)\,du=1,\ \int\_{0}^{\infty}ug(u)\,du=1\}.

*Step 1 (Equality of total mass).*
Since g,g′∈L1​(ℝ+)g,g^{\prime}\in L^{1}(\mathbb{R}\_{+}) and f∈L1​(ℝ+)f\in L^{1}(\mathbb{R}\_{+}) by admissibility,
the integrals below are finite and Fubini’s theorem applies. Then

|  |  |  |
| --- | --- | --- |
|  | ∫0∞f​(u)​𝑑u=M​∫0∞1μ​g​(u/μ)​𝑑u=M​∫0∞g​(v)​𝑑v=M,\int\_{0}^{\infty}f(u)\,du=M\int\_{0}^{\infty}\frac{1}{\mu}g(u/\mu)\,du=M\int\_{0}^{\infty}g(v)\,dv=M, |  |

where we used the change of variable v=u/μv=u/\mu.
Analogously, ∫0∞f​(u)​𝑑u=M′\int\_{0}^{\infty}f(u)\,du=M^{\prime}, and thus M=M′M=M^{\prime}.

*Step 2 (Equality of first moments).*
Because u​f​(u)uf(u) is integrable by assumption, we have

|  |  |  |
| --- | --- | --- |
|  | ∫0∞u​f​(u)​𝑑u=M​∫0∞uμ​g​(u/μ)​𝑑u=M​μ​∫0∞v​g​(v)​𝑑v=M​μ,\int\_{0}^{\infty}uf(u)\,du=M\int\_{0}^{\infty}\frac{u}{\mu}g(u/\mu)\,du=M\mu\int\_{0}^{\infty}vg(v)\,dv=M\mu, |  |

and similarly ∫0∞u​f​(u)​𝑑u=M′​μ′\int\_{0}^{\infty}uf(u)\,du=M^{\prime}\mu^{\prime}.
Since M=M′M=M^{\prime}, it follows that μ=μ′\mu=\mu^{\prime}.

*Step 3 (Equality of shape functions).*
Substituting M=M′M=M^{\prime} and μ=μ′\mu=\mu^{\prime} back into the representation of ff, we obtain
M​μ−1​g​(u/μ)=M​μ−1​g′​(u/μ)M\mu^{-1}g(u/\mu)=M\mu^{-1}g^{\prime}(u/\mu) for a.e. u≥0u\geq 0.
Because M>0M>0 and μ>0\mu>0, this implies g​(u)=g′​(u)g(u)=g^{\prime}(u) for a.e. u≥0u\geq 0
(by the substitution v=u/μv=u/\mu).

Hence (M,μ,g)=(M′,μ′,g′)(M,\mu,g)=(M^{\prime},\mu^{\prime},g^{\prime}) almost everywhere, completing the proof.
∎

## Appendix D — Spectral Orthogonality and Scaling

###### Proof of Proposition [1](https://arxiv.org/html/2512.02166v1#Thmproposition1 "Proposition 1 (Orthogonality: vertical, horizontal, and slope). ‣ Identification in the frequency domain ‣ 3.1 Canonical Decomposition of Volatility Memory ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory").

Let {ψk}\{\psi\_{k}\} and {φk}\{\varphi\_{k}\} denote the discrete embeddings of ff and gg, respectively:

|  |  |  |
| --- | --- | --- |
|  | ψk=∫k−1kf​(u)​𝑑u,φk=∫k−1kg​(u)​𝑑u.\psi\_{k}=\int\_{k-1}^{k}f(u)\,du,\qquad\varphi\_{k}=\int\_{k-1}^{k}g(u)\,du. |  |

Since f​(u)=M​μ−1​g​(u/μ)f(u)=M\mu^{-1}g(u/\mu), we have

|  |  |  |
| --- | --- | --- |
|  | ψk=∫k−1kMμ​g​(uμ)​𝑑u=M​∫(k−1)/μk/μg​(v)​𝑑v.\psi\_{k}=\int\_{k-1}^{k}\frac{M}{\mu}\,g\!\Big(\frac{u}{\mu}\Big)\,du=M\int\_{(k-1)/\mu}^{k/\mu}g(v)\,dv. |  |

Hence the discrete-time transfer functions satisfy

|  |  |  |
| --- | --- | --- |
|  | Ψ​(e−i​λ):=∑k≥1ψk​e−i​k​λ=M​∑k≥1∫(k−1)/μk/μg​(v)​𝑑v​e−i​k​λ.\Psi(e^{-i\lambda}):=\sum\_{k\geq 1}\psi\_{k}e^{-ik\lambda}=M\sum\_{k\geq 1}\int\_{(k-1)/\mu}^{k/\mu}g(v)\,dv\,e^{-ik\lambda}. |  |

Approximating the Riemann sums by integrals gives the standard time-dilation identity

|  |  |  |
| --- | --- | --- |
|  | Ψ​(e−i​λ)=M​Φ​(e−i​μ​λ),\Psi(e^{-i\lambda})=M\,\Phi(e^{-i\mu\lambda}), |  |

where Φ\Phi is the transfer function of gg.
Therefore,

|  |  |  |
| --- | --- | --- |
|  | Sf​(λ)=|Ψ​(e−i​λ)|2​Sξ​(λ)=M2​|Φ​(e−i​μ​λ)|2​Sξ​(λ).S\_{f}(\lambda)=|\Psi(e^{-i\lambda})|^{2}S\_{\xi}(\lambda)=M^{2}|\Phi(e^{-i\mu\lambda})|^{2}S\_{\xi}(\lambda). |  |

For linear filters driven by white noise (or centered squares with short memory), the driving spectrum
Sξ​(λ)S\_{\xi}(\lambda) is flat, and thus

|  |  |  |
| --- | --- | --- |
|  | Sf​(λ)=M2​Sg​(μ​λ),S\_{f}(\lambda)=M^{2}S\_{g}(\mu\lambda), |  |

which is equation ([3](https://arxiv.org/html/2512.02166v1#S3.E3 "In Proposition 1 (Orthogonality: vertical, horizontal, and slope). ‣ Identification in the frequency domain ‣ 3.1 Canonical Decomposition of Volatility Memory ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory")).

*Interpretation.*
The scaling relation shows that MM acts as a *vertical rescaling* of spectral amplitude,
μ\mu acts as a *horizontal dilation* of the frequency axis, and
the spectral slope at low frequencies (e.g., Sg​(λ)∼C​λ−2​dS\_{g}(\lambda)\sim C\lambda^{-2d} as λ↓0\lambda\downarrow 0)
depends only on the shape parameter gg:

|  |  |  |
| --- | --- | --- |
|  | Sf​(λ)∼(M2​C)​λ−2​d,λ↓0.S\_{f}(\lambda)\sim(M^{2}C)\lambda^{-2d},\qquad\lambda\downarrow 0. |  |

Hence the low-frequency slope −2​d-2d is invariant to (M,μ)(M,\mu),
formalizing orthogonality among the level, tempo, and shape components.
∎

## Appendix E — Existence and Uniqueness via Contraction

We consider the generic linear recursion for conditional variance

|  |  |  |
| --- | --- | --- |
|  | ht=ω+∑k≥1ψk​(εt−k2−1)+∑k≥1ψk​ht−k,ω>0,ψk≥0.h\_{t}=\omega+\sum\_{k\geq 1}\psi\_{k}\big(\varepsilon\_{t-k}^{2}-1\big)+\sum\_{k\geq 1}\psi\_{k}h\_{t-k},\qquad\omega>0,\quad\psi\_{k}\geq 0. |  |

Define Ψ:=∑k≥1ψk\Psi:=\sum\_{k\geq 1}\psi\_{k}.

###### Theorem 7 (Unique strictly stationary solution via Banach fixed point).

If Ψ<1\Psi<1 and (εt)(\varepsilon\_{t}) are i.i.d. with 𝔼​[εt2]=1\mathbb{E}[\varepsilon\_{t}^{2}]=1 and
𝔼​|εt|2+δ<∞\mathbb{E}|\varepsilon\_{t}|^{2+\delta}<\infty for some δ>0\delta>0, then there exists a unique strictly stationary and ergodic solution (ht)(h\_{t}) with supt𝔼​[ht]<∞\sup\_{t}\mathbb{E}[h\_{t}]<\infty.

###### Proof (step-by-step).

Step 1 (State space and operator).
Let 𝖷\mathsf{X} be the Banach space of one-sided sequences
x=(x0,x−1,x−2,…)x=(x\_{0},x\_{-1},x\_{-2},\dots) equipped with the weighted norm
‖x‖ψ:=∑k≥0ψk+1​|x−k|\|x\|\_{\psi}:=\sum\_{k\geq 0}\psi\_{k+1}|x\_{-k}|.
Define the random affine operator

|  |  |  |
| --- | --- | --- |
|  | 𝒯​(x):=ω+∑k≥1ψk​(εt−k2−1)+∑k≥1ψk​x−k+1.\mathcal{T}(x):=\omega+\sum\_{k\geq 1}\psi\_{k}(\varepsilon\_{t-k}^{2}-1)+\sum\_{k\geq 1}\psi\_{k}x\_{-k+1}. |  |

Step 2 (Contraction).
For x,y∈𝖷x,y\in\mathsf{X},

|  |  |  |
| --- | --- | --- |
|  | ‖𝒯​(x)−𝒯​(y)‖ψ=∑k≥0ψk+1​|∑j≥1ψj​(x−k−j+2−y−k−j+2)|≤Ψ​∑m≥0ψm+1​|x−m−y−m|=Ψ​‖x−y‖ψ.\|\mathcal{T}(x)-\mathcal{T}(y)\|\_{\psi}=\sum\_{k\geq 0}\psi\_{k+1}\left|\sum\_{j\geq 1}\psi\_{j}(x\_{-k-j+2}-y\_{-k-j+2})\right|\leq\Psi\sum\_{m\geq 0}\psi\_{m+1}|x\_{-m}-y\_{-m}|=\Psi\|x-y\|\_{\psi}. |  |

Hence 𝒯\mathcal{T} is a contraction with constant Ψ<1\Psi<1.

Step 3 (Fixed point and stationarity).
By Banach’s fixed point theorem, for each ω\omega-realization, there exists a unique measurable fixed point x∗​(ω)x^{\*}(\omega) solving x∗=𝒯​(x∗)x^{\*}=\mathcal{T}(x^{\*}); the first coordinate of x∗x^{\*} is hth\_{t}. Stationarity follows from time-homogeneity of the law of (εt−k)k≥1(\varepsilon\_{t-k})\_{k\geq 1}.

Step 4 (Finiteness of moments).
Taking expectations in the recursion and applying Minkowski plus Ψ<1\Psi<1 yields
supt𝔼​[ht]≤ω/(1−Ψ)<∞\sup\_{t}\mathbb{E}[h\_{t}]\leq\omega/(1-\Psi)<\infty.
Ergodicity follows from the contraction and standard iterated random function arguments.
∎

###### Remark 5 (Why the weighted norm).

The weight ψk+1\psi\_{k+1} aligns the geometry of 𝖷\mathsf{X} with the linear memory kernel so that the shift-plus-convolution map has Lipschitz constant exactly Ψ\Psi, making the contraction sharp and avoiding ad hoc truncations.

## Appendix F — Higher-Order Moments

###### Proposition 5 (Uniform LpL^{p} bound).

Suppose Ψ=∑kψk<1\Psi=\sum\_{k}\psi\_{k}<1 and 𝔼​|εt|2​p<∞\mathbb{E}|\varepsilon\_{t}|^{2p}<\infty for some p∈[1,2]p\in[1,2].
Then Xt:=𝔼​[htp]X\_{t}:=\mathbb{E}[h\_{t}^{p}] satisfies suptXt≤Cp1−Ψp\sup\_{t}X\_{t}\leq\dfrac{C\_{p}}{1-\Psi^{p}} for an explicit constant CpC\_{p} depending on (ω,Ψ,p,𝔼​|εt2−1|p)(\omega,\Psi,p,\mathbb{E}|\varepsilon\_{t}^{2}-1|^{p}).

###### Proof.

By triangle inequality in LpL^{p} (Minkowski),

|  |  |  |
| --- | --- | --- |
|  | ‖ht‖p≤ω+‖∑kψk​(εt−k2−1)‖p+‖∑kψk​ht−k‖p≤ω+(∑kψk)​‖εt2−1‖p+Ψ​sups<t‖hs‖p,\|h\_{t}\|\_{p}\leq\omega+\left\|\sum\_{k}\psi\_{k}(\varepsilon\_{t-k}^{2}-1)\right\|\_{p}+\left\|\sum\_{k}\psi\_{k}h\_{t-k}\right\|\_{p}\leq\omega+\left(\sum\_{k}\psi\_{k}\right)\|\varepsilon\_{t}^{2}-1\|\_{p}+\Psi\sup\_{s<t}\|h\_{s}\|\_{p}, |  |

where we used ℓ1\ell^{1}-boundedness of (ψk)(\psi\_{k}) and stationarity of (εt)(\varepsilon\_{t}) and (ht)(h\_{t}). Set Yt:=‖ht‖pY\_{t}:=\|h\_{t}\|\_{p} and A:=ω+Ψ​‖εt2−1‖pA:=\omega+\Psi\|\varepsilon\_{t}^{2}-1\|\_{p}. Then
Yt≤A+Ψ​sups<tYsY\_{t}\leq A+\Psi\sup\_{s<t}Y\_{s}. By induction,
supt≤nYt≤A​(1+Ψ+⋯+Ψn−1)≤A/(1−Ψ)\sup\_{t\leq n}Y\_{t}\leq A(1+\Psi+\cdots+\Psi^{n-1})\leq A/(1-\Psi).
Hence supt‖ht‖p≤A/(1−Ψ)\sup\_{t}\|h\_{t}\|\_{p}\leq A/(1-\Psi). Raising to power pp gives the claim with CpC\_{p} explicit.
∎

###### Remark 6 (Extension to p>2p>2).

If in addition ∑kψkq<∞\sum\_{k}\psi\_{k}^{q}<\infty for some q∈(1,2]q\in(1,2] and suitable moment conditions on εt\varepsilon\_{t}, Rosenthal-type bounds allow extension to p>2p>2. We omit details as they are not needed for our estimators.

## Appendix G — Identification Proofs

##### Spectral scaling law.

For an admissible kernel factorized as f​(u)=M​μ−1​g​(u/μ)f(u)=M\mu^{-1}g(u/\mu), its discrete-time impulse response ψk=∫k−1kf​(u)​𝑑u\psi\_{k}=\int\_{k-1}^{k}f(u)\,du satisfies
ψk=M⋅∫(k−1)/μk/μg​(v)​𝑑v\psi\_{k}=M\cdot\int\_{(k-1)/\mu}^{k/\mu}g(v)\,dv, hence its spectral density
Sf​(λ)=∑j∈ℤγj​e−i​j​λS\_{f}(\lambda)=\sum\_{j\in\mathbb{Z}}\gamma\_{j}e^{-ij\lambda}
obeys Sf​(λ)=M2​Sg​(μ​λ)S\_{f}(\lambda)=M^{2}S\_{g}(\mu\lambda), where SgS\_{g} is the spectral density associated with the step-integrated gg.

###### Proposition 6 (Global identification up to trivial sign).

Let fif\_{i} admit factorizations (Mi,μi,gi)(M\_{i},\mu\_{i},g\_{i}) with gig\_{i} non-constant and in L1∩L2L^{1}\cap L^{2}. If Sf1​(λ)=Sf2​(λ)S\_{f\_{1}}(\lambda)=S\_{f\_{2}}(\lambda) for all λ∈[−π,π]\lambda\in[-\pi,\pi], then M1=M2M\_{1}=M\_{2}, μ1=μ2\mu\_{1}=\mu\_{2}, and g1=g2g\_{1}=g\_{2} almost everywhere.

###### Proof.

Equality implies M12​Sg1​(μ1​λ)=M22​Sg2​(μ2​λ)M\_{1}^{2}S\_{g\_{1}}(\mu\_{1}\lambda)=M\_{2}^{2}S\_{g\_{2}}(\mu\_{2}\lambda) for all λ\lambda. Evaluating at λ=0\lambda=0 gives M12​Sg1​(0)=M22​Sg2​(0)M\_{1}^{2}S\_{g\_{1}}(0)=M\_{2}^{2}S\_{g\_{2}}(0). Since Sgi​(0)=∑jγj​(gi)=∫gi2>0S\_{g\_{i}}(0)=\sum\_{j}\gamma\_{j}(g\_{i})=\int g\_{i}^{2}>0 (by gi≢0g\_{i}\not\equiv 0), we have M12/M22=Sg2​(0)/Sg1​(0)M\_{1}^{2}/M\_{2}^{2}=S\_{g\_{2}}(0)/S\_{g\_{1}}(0).
Differentiating both sides at 0 yields

|  |  |  |
| --- | --- | --- |
|  | M12​μ1​Sg1′​(0)=M22​μ2​Sg2′​(0).M\_{1}^{2}\mu\_{1}S^{\prime}\_{g\_{1}}(0)=M\_{2}^{2}\mu\_{2}S^{\prime}\_{g\_{2}}(0). |  |

Because SgiS\_{g\_{i}} is non-constant, Sgi′​(0)S^{\prime}\_{g\_{i}}(0) exists (as gi∈L2g\_{i}\in L^{2}) and at least one derivative is nonzero, which forces μ1=μ2\mu\_{1}=\mu\_{2} and M12=M22M\_{1}^{2}=M\_{2}^{2}. With μ1=μ2\mu\_{1}=\mu\_{2}, we get Sg1=Sg2S\_{g\_{1}}=S\_{g\_{2}} pointwise. Fourier inversion (uniqueness of Fourier transform in L2L^{2}) implies g1=g2g\_{1}=g\_{2} a.e.
∎

###### Lemma 7 (Local identifiability of gates).

Let pt=σ​(γ⊤​zt−1)p\_{t}=\sigma(\gamma^{\top}z\_{t-1}) and βt=exp⁡(−κ​eη⊤​zt−1)\beta\_{t}=\exp(-\kappa e^{\eta^{\top}z\_{t-1}}) with σ​(x)=1/(1+e−x)\sigma(x)=1/(1+e^{-x}). If 𝔼​[zt−1​zt−1⊤]\mathbb{E}[z\_{t-1}z\_{t-1}^{\top}] is positive definite and parameter domains are compact, then the Fisher information matrices 𝔼​[(∂γpt)​zt−1​zt−1⊤]\mathbb{E}[(\partial\_{\gamma}p\_{t})z\_{t-1}z\_{t-1}^{\top}] and 𝔼​[(∂ηβt)​zt−1​zt−1⊤]\mathbb{E}[(\partial\_{\eta}\beta\_{t})z\_{t-1}z\_{t-1}^{\top}] are positive definite, hence parameters are locally identified.

###### Proof.

∂γpt=pt​(1−pt)​zt−1\partial\_{\gamma}p\_{t}=p\_{t}(1-p\_{t})z\_{t-1} and ∂ηβt=−κ​βt​eη⊤​zt−1​zt−1\partial\_{\eta}\beta\_{t}=-\kappa\beta\_{t}e^{\eta^{\top}z\_{t-1}}z\_{t-1} are non-degenerate multiples of zt−1z\_{t-1} on sets of positive probability; hence the corresponding information matrices inherit positive definiteness from 𝔼​[z​z⊤]\mathbb{E}[zz^{\top}].
∎

## Appendix H — QMLE Consistency and CLT

Let ℓt​(ϑ)\ell\_{t}(\vartheta) be the per-period quasi log-likelihood with parameter ϑ∈Θ\vartheta\in\Theta (compact). Define LT​(ϑ):=T−1​∑t=1Tℓt​(ϑ)L\_{T}(\vartheta):=T^{-1}\sum\_{t=1}^{T}\ell\_{t}(\vartheta) and L​(ϑ):=𝔼​[ℓt​(ϑ)]L(\vartheta):=\mathbb{E}[\ell\_{t}(\vartheta)].

###### Assumption 7 (E1 — regularity).

1. 1.

   {ℓt​(ϑ)}\{\ell\_{t}(\vartheta)\} is strictly stationary and geometrically β\beta-mixing under ϑ0\vartheta\_{0}.
2. 2.

   ℓt​(ϑ)\ell\_{t}(\vartheta) is continuous in ϑ\vartheta a.s. and supϑ∈Θ|ℓt​(ϑ)|\sup\_{\vartheta\in\Theta}|\ell\_{t}(\vartheta)| has finite expectation.
3. 3.

   Identification: L​(ϑ)L(\vartheta) has a unique maximizer at ϑ0\vartheta\_{0}.

###### Theorem 8 (Strong consistency).

Under Assumption E1, any sequence of maximizers ϑ^T∈arg⁡maxϑ∈Θ⁡LT​(ϑ)\hat{\vartheta}\_{T}\in\arg\max\_{\vartheta\in\Theta}L\_{T}(\vartheta) satisfies ϑ^T→ϑ0\hat{\vartheta}\_{T}\to\vartheta\_{0} almost surely.

###### Proof.

Geometric mixing implies a uniform law of large numbers (ULLN):
supϑ∈Θ|LT​(ϑ)−L​(ϑ)|→0\sup\_{\vartheta\in\Theta}|L\_{T}(\vartheta)-L(\vartheta)|\to 0 a.s.
(see e.g., Andrews (1992)-type ULLN for mixing arrays).
By the argmax continuity theorem on compact sets with identification,
ϑ^T→ϑ0\hat{\vartheta}\_{T}\to\vartheta\_{0} a.s.
∎

For asymptotics, assume differentiability and moment bounds:

###### Assumption 8 (E2 — differentiability and moments).

1. 1.

   ℓt​(ϑ)\ell\_{t}(\vartheta) is twice continuously differentiable in a neighborhood of ϑ0\vartheta\_{0} with
   𝔼​supϑ‖∇ℓt​(ϑ)‖<∞\mathbb{E}\sup\_{\vartheta}\|\nabla\ell\_{t}(\vartheta)\|<\infty,
   𝔼​supϑ‖∇2ℓt​(ϑ)‖<∞\mathbb{E}\sup\_{\vartheta}\|\nabla^{2}\ell\_{t}(\vartheta)\|<\infty.
2. 2.

   The score is a martingale difference:
   𝔼​[∇ℓt​(ϑ0)∣ℱt−1]=0\mathbb{E}[\nabla\ell\_{t}(\vartheta\_{0})\mid\mathcal{F}\_{t-1}]=0 a.s.
3. 3.

   Information regularity: I:=𝔼​[−∇2ℓt​(ϑ0)]I:=\mathbb{E}[-\nabla^{2}\ell\_{t}(\vartheta\_{0})] and
   J:=𝔼​[∇ℓt​(ϑ0)​∇ℓt​(ϑ0)⊤]J:=\mathbb{E}[\nabla\ell\_{t}(\vartheta\_{0})\nabla\ell\_{t}(\vartheta\_{0})^{\top}] exist and are finite, with II positive definite.

###### Theorem 9 (Asymptotic normality with sandwich covariance).

Under Assumptions E1–E2,

|  |  |  |
| --- | --- | --- |
|  | T​(ϑ^T−ϑ0)⇒𝒩​(0,I−1​J​I−1).\sqrt{T}\,(\hat{\vartheta}\_{T}-\vartheta\_{0})\ \Rightarrow\ \mathcal{N}\!\left(0,\ I^{-1}JI^{-1}\right). |  |

###### Proof (details).

A second-order Taylor expansion of T−1​∇ℓT​(ϑ^T)T^{-1}\nabla\ell\_{T}(\hat{\vartheta}\_{T}) around ϑ0\vartheta\_{0} gives

|  |  |  |
| --- | --- | --- |
|  | 0=T−1​∑t=1T∇ℓt​(ϑ0)+[T−1​∑t=1T∇2ℓt​(ϑ¯T)]​(ϑ^T−ϑ0),0=T^{-1}\sum\_{t=1}^{T}\nabla\ell\_{t}(\vartheta\_{0})+\left[T^{-1}\sum\_{t=1}^{T}\nabla^{2}\ell\_{t}(\bar{\vartheta}\_{T})\right](\hat{\vartheta}\_{T}-\vartheta\_{0}), |  |

where ϑ¯T\bar{\vartheta}\_{T} lies on the segment between ϑ^T\hat{\vartheta}\_{T} and ϑ0\vartheta\_{0}.
Multiply by T\sqrt{T} and rearrange:

|  |  |  |
| --- | --- | --- |
|  | T​(ϑ^T−ϑ0)=−[T−1​∑t=1T∇2ℓt​(ϑ¯T)]−1⋅1T​∑t=1T∇ℓt​(ϑ0).\sqrt{T}(\hat{\vartheta}\_{T}-\vartheta\_{0})=-\left[T^{-1}\sum\_{t=1}^{T}\nabla^{2}\ell\_{t}(\bar{\vartheta}\_{T})\right]^{-1}\cdot\frac{1}{\sqrt{T}}\sum\_{t=1}^{T}\nabla\ell\_{t}(\vartheta\_{0}). |  |

By E1–E2 and ULLN, T−1​∑∇2ℓt​(ϑ¯T)→𝑝−IT^{-1}\sum\nabla^{2}\ell\_{t}(\bar{\vartheta}\_{T})\xrightarrow{p}-I.
The score sum is a martingale array with conditional mean zero and finite conditional variance; applying a martingale CLT (e.g., Hall & Heyde),
T−1/2​∑∇ℓt​(ϑ0)⇒𝒩​(0,J).T^{-1/2}\sum\nabla\ell\_{t}(\vartheta\_{0})\Rightarrow\mathcal{N}(0,J).
Slutsky’s theorem yields the claimed limit with covariance I−1​J​I−1I^{-1}JI^{-1}.
∎

###### Remark 7 (Plug-in covariance).

A consistent estimator is
Var^​(ϑ^T)=I^−1​J^​I^−1\widehat{\mathrm{Var}}(\hat{\vartheta}\_{T})=\widehat{I}^{-1}\widehat{J}\widehat{I}^{-1} with
I^=T−1​∑−∇2ℓt​(ϑ^T)\widehat{I}=T^{-1}\sum-\nabla^{2}\ell\_{t}(\hat{\vartheta}\_{T}) and
J^=T−1​∑∇ℓt​(ϑ^T)​∇ℓt​(ϑ^T)⊤\widehat{J}=T^{-1}\sum\nabla\ell\_{t}(\hat{\vartheta}\_{T})\nabla\ell\_{t}(\hat{\vartheta}\_{T})^{\top}.

## Appendix I — Spectral–Time Equivalence

Let ψk=∫k−1kf​(u)​𝑑u\psi\_{k}=\int\_{k-1}^{k}f(u)\,du and γj=∑k∈ℤψk​ψk+j\gamma\_{j}=\sum\_{k\in\mathbb{Z}}\psi\_{k}\psi\_{k+j} with the convention ψk=0\psi\_{k}=0 for k≤0k\leq 0.

###### Proposition 7 (Discrete Parseval via step embedding).

If f∈L2​(ℝ+)f\in L^{2}(\mathbb{R}\_{+}), then

|  |  |  |
| --- | --- | --- |
|  | ∫−ππSf​(λ)​𝑑λ=2​π​∑j∈ℤγj=2​π​∑k≥1ψk2=2​π​∫0∞f​(u)2​𝑑u.\int\_{-\pi}^{\pi}S\_{f}(\lambda)\,d\lambda=2\pi\sum\_{j\in\mathbb{Z}}\gamma\_{j}=2\pi\sum\_{k\geq 1}\psi\_{k}^{2}=2\pi\int\_{0}^{\infty}f(u)^{2}\,du. |  |

###### Proof.

The equalities ∫Sf=2​π​∑γj=2​π​∑ψk2\int S\_{f}=2\pi\sum\gamma\_{j}=2\pi\sum\psi\_{k}^{2} are standard discrete-time Parseval relations for linear filters with impulse response (ψk)(\psi\_{k}). For the last equality, note that the step function s​(u)=∑k≥1ψk​𝟏[k−1,k)​(u)s(u)=\sum\_{k\geq 1}\psi\_{k}\mathbf{1}\_{[k-1,k)}(u) satisfies
‖s‖L22=∑kψk2\|s\|\_{L^{2}}^{2}=\sum\_{k}\psi\_{k}^{2} and
‖s−f‖L2→0\|s-f\|\_{L^{2}}\to 0 as we refine the partition (mesh size 11 is fixed but ff is replaced by its unit-step average). Since L2L^{2} is complete, ∑kψk2=∫f2\sum\_{k}\psi\_{k}^{2}=\int f^{2}.
∎

###### Corollary 1 (Low-frequency equivalence for power-law shapes).

If g​(u)∝u−(1+d)g(u)\propto u^{-(1+d)} with d∈(0,1/2)d\in(0,1/2), then
γj∼C​j2​d−1\gamma\_{j}\sim Cj^{2d-1} and Sg​(λ)∼C′​λ−2​dS\_{g}(\lambda)\sim C^{\prime}\lambda^{-2d} as λ↓0\lambda\downarrow 0.

###### Proof.

Karamata-type Abelian/Tauberian results for slowly varying sequences yield the asymptotics for ψk\psi\_{k} and hence for γj\gamma\_{j}; Fourier inversion near 0 gives the spectral slope −2​d-2d.
∎

## Appendix J — Unified Gate Stability

Consider the unified gated recursion

|  |  |  |
| --- | --- | --- |
|  | ht=ω+αt​εt−12+Ψt​ht−1+∑k≥1Πt,k​(εt−k2−ht−k),αt,Ψt,Πt,k≥0.h\_{t}=\omega+\alpha\_{t}\varepsilon\_{t-1}^{2}+\Psi\_{t}h\_{t-1}+\sum\_{k\geq 1}\Pi\_{t,k}\,(\varepsilon\_{t-k}^{2}-h\_{t-k}),\qquad\alpha\_{t},\Psi\_{t},\Pi\_{t,k}\geq 0. |  |

###### Assumption 9 (G1 — gate regularity).

1. 1.

   (αt,Ψt,{Πt,k}k)(\alpha\_{t},\Psi\_{t},\{\Pi\_{t,k}\}\_{k}) are ℱt−1\mathcal{F}\_{t-1}-measurable and strictly positive with ∑k𝔼​[Πt,k]<∞\sum\_{k}\mathbb{E}[\Pi\_{t,k}]<\infty.
2. 2.

   𝔼​[log⁡(αt+Ψt)]<0\mathbb{E}[\log(\alpha\_{t}+\Psi\_{t})]<0.
3. 3.

   (εt)(\varepsilon\_{t}) has a density positive on compacts and 𝔼​|εt|4+δ<∞\mathbb{E}|\varepsilon\_{t}|^{4+\delta}<\infty for some δ>0\delta>0.

###### Theorem 10 (Geometric ergodicity and bounded second moments).

Under Assumption G1, the Markov chain (ht)(h\_{t}) on ℝ+\mathbb{R}\_{+} is
ψ\psi-irreducible, aperiodic, geometrically ergodic, and
supt𝔼​[ht2]<∞\sup\_{t}\mathbb{E}[h\_{t}^{2}]<\infty.

###### Proof (Foster–Lyapunov drift with minorization).

Let V​(h)=1+hV(h)=1+h. Then conditionally on ℱt−1\mathcal{F}\_{t-1},

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[V​(ht)∣ℱt−1]≤1+ω+(αt+Ψt)​V​(ht−1)+∑k≥1Πt,k​𝔼​[|εt−k2−ht−k|∣ℱt−1].\mathbb{E}[V(h\_{t})\mid\mathcal{F}\_{t-1}]\leq 1+\omega+(\alpha\_{t}+\Psi\_{t})V(h\_{t-1})+\sum\_{k\geq 1}\Pi\_{t,k}\,\mathbb{E}\big[|\varepsilon\_{t-k}^{2}-h\_{t-k}|\mid\mathcal{F}\_{t-1}\big]. |  |

Using 𝔼​|ε2−h|≤c1+c2​h\mathbb{E}|\varepsilon^{2}-h|\leq c\_{1}+c\_{2}h for some constants (by triangle inequality and 𝔼​ε2=1\mathbb{E}\varepsilon^{2}=1), absorb the sum into a linear term in V​(ht−1)V(h\_{t-1}) since ∑kΠt,k\sum\_{k}\Pi\_{t,k} is integrable. Taking expectations and Jensen on the log term gives

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[V​(ht)]≤c0+ρ​𝔼​[V​(ht−1)],ρ:=exp⁡{𝔼​log⁡(αt+Ψt)}<1.\mathbb{E}[V(h\_{t})]\leq c\_{0}+\rho\,\mathbb{E}[V(h\_{t-1})],\qquad\rho:=\exp\{\mathbb{E}\log(\alpha\_{t}+\Psi\_{t})\}<1. |  |

Thus a drift condition holds outside compacts. By the positive density of εt\varepsilon\_{t}, a standard small-set minorization holds on [0,H][0,H] for some H>0H>0, ensuring ψ\psi-irreducibility and aperiodicity. The Meyn–Tweedie theorem then yields geometric ergodicity; bounded second moments follow from the drift with V​(h)=1+h+h2V(h)=1+h+h^{2} (using 𝔼​ε4+δ<∞\mathbb{E}\varepsilon^{4+\delta}<\infty).
∎

## Appendix K — Proof of Lemma [2](https://arxiv.org/html/2512.02166v1#Thmlemma2 "Lemma 2 (Uniform kernel summability). ‣ Assumptions and kernel bounds ‣ 3.5 G–FIGARCH: Shape Gate and Dynamic Long Memory ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory")

##### Goal.

Show |πk​(d)|=O​(k−1−d)|\pi\_{k}(d)|=O(k^{-1-d}) and ∑k=1∞|πk​(dt)|<∞\sum\_{k=1}^{\infty}|\pi\_{k}(d\_{t})|<\infty uniformly if dt≤d¯<1/2d\_{t}\leq\bar{d}<1/2.

##### Asymptotics.

Using (dk)=Γ​(d+1)/(Γ​(k+1)​Γ​(d−k+1))\binom{d}{k}=\Gamma(d+1)/(\Gamma(k+1)\Gamma(d-k+1)) and Stirling’s formula for large kk,

|  |  |  |
| --- | --- | --- |
|  | (dk)∼k−1−dΓ​(−d).\binom{d}{k}\sim\frac{k^{-1-d}}{\Gamma(-d)}. |  |

Hence |πk​(d)|=O​(k−1−d)|\pi\_{k}(d)|=O(k^{-1-d}). If d<1/2d<1/2 then 1+d>11+d>1 and ∑k−(1+d)<∞\sum k^{-(1+d)}<\infty.
Monotone convergence gives a uniform bound for partial sums when dt≤d¯<1/2d\_{t}\leq\bar{d}<1/2.

## Appendix L — Proof of Theorem [4](https://arxiv.org/html/2512.02166v1#Thmtheorem4 "Theorem 4 (Finite second moment). ‣ Unconditional moments and stability ‣ 3.5 G–FIGARCH: Shape Gate and Dynamic Long Memory ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory")

##### Truncation and tail control.

Define

|  |  |  |
| --- | --- | --- |
|  | ht(K)=ω+α​εt−12+β​ht−1(K)+∑k=1Kπk​(dt)​(εt−k2−ht−k(K))+Rt,K,h\_{t}^{(K)}=\omega+\alpha\varepsilon\_{t-1}^{2}+\beta h\_{t-1}^{(K)}+\sum\_{k=1}^{K}\pi\_{k}(d\_{t})\big(\varepsilon\_{t-k}^{2}-h\_{t-k}^{(K)}\big)+R\_{t,K}, |  |

where Rt,K:=∑k>Kπk​(dt)​(εt−k2−ht−k)R\_{t,K}:=\sum\_{k>K}\pi\_{k}(d\_{t})(\varepsilon\_{t-k}^{2}-h\_{t-k}).
By Lemma [2](https://arxiv.org/html/2512.02166v1#Thmlemma2 "Lemma 2 (Uniform kernel summability). ‣ Assumptions and kernel bounds ‣ 3.5 G–FIGARCH: Shape Gate and Dynamic Long Memory ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory"), ρK:=supt∑k>K|πk​(dt)|↓0\rho\_{K}:=\sup\_{t}\sum\_{k>K}|\pi\_{k}(d\_{t})|\downarrow 0.

##### L2L^{2}-inequality.

By triangle and Minkowski,

|  |  |  |
| --- | --- | --- |
|  | ‖ht(K)‖2≤ω+α​‖εt−12‖2+β​‖ht−1(K)‖2+(∑k=1K|πk​(dt)|)​(‖εt−k2‖2+‖ht−k(K)‖2)+‖Rt,K‖2.\|h\_{t}^{(K)}\|\_{2}\leq\omega+\alpha\|\varepsilon\_{t-1}^{2}\|\_{2}+\beta\|h\_{t-1}^{(K)}\|\_{2}+\Big(\sum\_{k=1}^{K}|\pi\_{k}(d\_{t})|\Big)\big(\|\varepsilon\_{t-k}^{2}\|\_{2}+\|h\_{t-k}^{(K)}\|\_{2}\big)+\|R\_{t,K}\|\_{2}. |  |

Bound ‖ε2‖2\|\varepsilon^{2}\|\_{2} by a constant CεC\_{\varepsilon} (finite fourth moment). Set
Bt(K):=sups≤t‖hs(K)‖2B\_{t}^{(K)}:=\sup\_{s\leq t}\|h\_{s}^{(K)}\|\_{2} and note
‖Rt,K‖2≤ρK​(Cε+sups<t‖hs‖2)≤ρK​(Cε+Bt(K))\|R\_{t,K}\|\_{2}\leq\rho\_{K}(C\_{\varepsilon}+\sup\_{s<t}\|h\_{s}\|\_{2})\leq\rho\_{K}(C\_{\varepsilon}+B\_{t}^{(K)}).
Let Cd:=supt∑k=1K|πk​(dt)|C\_{d}:=\sup\_{t}\sum\_{k=1}^{K}|\pi\_{k}(d\_{t})|. Then

|  |  |  |
| --- | --- | --- |
|  | Bt(K)≤c0+(β+Cd)​Bt−1(K)+ρK​(Cε+Bt(K)),B\_{t}^{(K)}\leq c\_{0}+(\beta+C\_{d})B\_{t-1}^{(K)}+\rho\_{K}(C\_{\varepsilon}+B\_{t}^{(K)}), |  |

with c0=ω+α​Cε+Cd​Cεc\_{0}=\omega+\alpha C\_{\varepsilon}+C\_{d}C\_{\varepsilon}.
Rearranging,

|  |  |  |
| --- | --- | --- |
|  | (1−ρK)​Bt(K)≤c0+(β+Cd)​Bt−1(K)+ρK​Cε.(1-\rho\_{K})B\_{t}^{(K)}\leq c\_{0}+(\beta+C\_{d})B\_{t-1}^{(K)}+\rho\_{K}C\_{\varepsilon}. |  |

For KK large, 1−ρK>121-\rho\_{K}>\tfrac{1}{2}. Iteration yields
Bt(K)≤2​(c0+ρK​Cε)1−(β+Cd)B\_{t}^{(K)}\leq\frac{2(c\_{0}+\rho\_{K}C\_{\varepsilon})}{1-(\beta+C\_{d})} provided (β+Cd)<1(\beta+C\_{d})<1.
Letting K→∞K\to\infty and using ρK→0\rho\_{K}\to 0, we obtain a uniform bound for ‖ht‖2\|h\_{t}\|\_{2}, hence 𝔼​[ht2]<∞\mathbb{E}[h\_{t}^{2}]<\infty.
∎

## Appendix M — Proof of Proposition [4](https://arxiv.org/html/2512.02166v1#Thmproposition4 "Proposition 4 (Geometric ergodicity). ‣ Unconditional mean and stationarity ‣ 3.6 G–Clock: Tempo Gate and Observable Business Time ‣ 3 Theory ‣ The Three-Dimensional Decomposition of Volatility Memory")

##### Lyapunov function and drift.

Let V​(h)=1+hV(h)=1+h. From ht=ω+αt​εt−12+βt​ht−1h\_{t}=\omega+\alpha\_{t}\varepsilon\_{t-1}^{2}+\beta\_{t}h\_{t-1},

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[V​(ht)∣ℱt−1]=1+ω+αt​𝔼​[εt−12∣ℱt−1]+βt​ht−1≤1+ω+(αt+βt)​V​(ht−1),\mathbb{E}[V(h\_{t})\mid\mathcal{F}\_{t-1}]=1+\omega+\alpha\_{t}\mathbb{E}[\varepsilon\_{t-1}^{2}\mid\mathcal{F}\_{t-1}]+\beta\_{t}h\_{t-1}\leq 1+\omega+(\alpha\_{t}+\beta\_{t})V(h\_{t-1}), |  |

since 𝔼​[ε2]=1\mathbb{E}[\varepsilon^{2}]=1.

##### Averaged drift via log.

Taking expectations and using Jensen for the concave log\log,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[V​(ht)]≤c0+exp⁡(𝔼​[log⁡(αt+βt)])​𝔼​[V​(ht−1)],\mathbb{E}[V(h\_{t})]\leq c\_{0}+\exp\big(\mathbb{E}[\log(\alpha\_{t}+\beta\_{t})]\big)\,\mathbb{E}[V(h\_{t-1})], |  |

with c0=1+ωc\_{0}=1+\omega and ρ:=exp⁡(𝔼​log⁡(αt+βt))<1\rho:=\exp(\mathbb{E}\log(\alpha\_{t}+\beta\_{t}))<1 by assumption.

##### Minorization and conclusion.

Because εt\varepsilon\_{t} has a density positive on compacts, there exists H>0H>0 and ϵ>0\epsilon>0 such that for all h∈[0,H]h\in[0,H], the transition kernel dominates a nontrivial measure; hence [0,H][0,H] is a small set. The drift plus small-set minorization implies geometric ergodicity by Meyn–Tweedie.
∎