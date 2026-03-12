---
authors:
- Charlie Che
- Hanxuan Lin
- Yudong Yang
- Guofan Hu
- Lei Fang
doc_id: arxiv:2603.10857v1
family_id: arxiv:2603.10857
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: SPX–VIX Risk Computations Via Perturbed Optimal Transport
url_abs: http://arxiv.org/abs/2603.10857v1
url_html: https://arxiv.org/html/2603.10857v1
venue: arXiv q-fin
version: 1
year: 2026
---


Charlie Che∗
charlie.che@jpmchase.com
Quantitative Trading & Research, JPMorganChase, New York, NY 10017, USA

Hanxuan Lin∗
hanxuan.lin@jpmchase.com
Quantitative Research China, JPMorganChase, Beijing, 100033, China

Yudong Yang∗
yudong.yang@jpmchase.com
Quantitative Trading & Research, JPMorganChase, New York, NY 10017, USA

Guofan Hu∗
guofan.hu@jpmchase.com
Quantitative Trading & Research, JPMorganChase, New York, NY 10017, USA

Lei Fang∗
lei.x.fang@jpmchase.com
Quantitative Trading & Research, JPMorganChase, New York, NY 10017, USA

## 1 Introduction

Joint modeling of SPX and VIX derivatives has become a central problem in equity volatility markets.
While SPX options encode the distribution of future equity prices, VIX options are derivative contracts written on VIX, the square root of forward variance.
Consistency between these two markets is therefore essential for both pricing and risk management of the SPX/VIX derivative family.

Traditional approaches to the joint SPX–VIX modeling problem rely on parametric stochastic volatility models such as the Heston model, stochastic volatility with jumps, Bergomi model, or rough volatility frameworks Heston ([1993](#bib.bib22 "A closed-form solution for options with stochastic volatility with applications to bond and currency options")); Gatheral ([2006](#bib.bib23 "The volatility surface: a practitioner’s guide")); Bergomi ([2016](#bib.bib21 "Stochastic volatility modeling")); Bayer and Friz ([2022](#bib.bib6 "Regularity of stochastic volatility models: rough and beyond")).
Although these models provide tractable simulation dynamics, they impose structural assumptions on volatility dynamics that are not directly implied by the observed option surfaces.

An alternative model-free approach was proposed by Guyon in Guyon ([2020](#bib.bib35 "The joint S&P 500/VIX smile calibration puzzle solved"), [2021](#bib.bib4 "Dispersion-constrained martingale schrödinger problems and the exact joint S&P 500/VIX smile calibration puzzle")), who formulated the joint SPX–VIX calibration problem as a martingale optimal transport (MOT) problem.
In this framework the calibrated coupling between equity levels and forward variance is obtained by solving a discrete entropic optimal transport problem using Sinkhorn iterations Cuturi ([2013](#bib.bib1 "Sinkhorn distances: lightspeed computation of optimal transport")); Benamou et al. ([2015](#bib.bib8 "Iterative bregman projections for regularized transportation problems")).
The resulting Gibbs distribution exactly reproduces the observed SPX and VIX option prices while remaining free of parametric volatility assumptions.

While entropic martingale optimal transport provides an exact joint
calibration of SPX and VIX smiles, calibration alone does not yield a
practical risk framework. In existing implementations, sensitivities
are typically obtained by re-running the full calibration after each
market perturbation. This bump-and-recalibrate approach is both
computationally expensive and obscures the structural relationship
between market shocks and model-implied risk.

The central observation of this paper is that entropic martingale optimal transport naturally defines a statistical manifold whose local geometry determines how the calibrated coupling reacts to marginal perturbations.
Because the optimal coupling belongs to an exponential family, its response to marginal shocks can be characterized by the Fisher information matrix of the calibrated Gibbs distribution.

This perspective leads to a new framework, which we term *Perturbed Optimal Transport(POT)*, for risk generation without recalibration. Within this POT framework, we propose two distinct yet complementary methodologies: one leveraging the local geometry of the calibrated coupling via a Linear Response (LR) system derived from the Fisher information matrix, and another utilizing Dimensional Reduction (DR) to efficiently re-solve a simpler transport problem under specific conditional invariance assumptions.

Beyond providing analytic risk formulas, the POT framework also enables incorporating empirical volatility dynamics into the optimal transport formulation.
In particular, we embed Skew Stickiness Ratio (SSR) dynamics for the VIX volatility surface as linear constraints in the entropic projection problem.
This allows the transport framework to incorporate empirically observed volatility smile dynamics without introducing parametric stochastic volatility models.

Taken together, these results establish Perturbed Optimal Transport (POT) not only as a powerful calibration tool but as a unified framework for joint calibration and risk propagation in SPX–VIX markets, offering efficient risk generation through both Linear Response and Dimensional Reduction techniques.

### 1.1 Related Literature

This work relates to three strands of literature.

SPX–VIX joint modeling.

Joint modeling of SPX and VIX derivatives has traditionally relied on stochastic volatility frameworks such as the Heston model and its extensions Heston ([1993](#bib.bib22 "A closed-form solution for options with stochastic volatility with applications to bond and currency options")); Gatheral ([2006](#bib.bib23 "The volatility surface: a practitioner’s guide")); Bergomi ([2016](#bib.bib21 "Stochastic volatility modeling")).
These models impose specific assumptions on volatility dynamics and require calibration of multiple parameters to match the observed option surfaces.

Optimal transport in finance.

Martingale optimal transport has emerged as a powerful model-free approach to derivative pricing and calibration Beiglböck et al. ([2013](#bib.bib17 "Model-independent bounds for option prices: a mass transport approach")); Henry-Labordère ([2017](#bib.bib15 "Model-free hedging: a martingale optimal transport viewpoint")).
Guyon ([2020](#bib.bib35 "The joint S&P 500/VIX smile calibration puzzle solved"), [2021](#bib.bib4 "Dispersion-constrained martingale schrödinger problems and the exact joint S&P 500/VIX smile calibration puzzle")) introduced an entropic optimal transport formulation for the joint calibration of SPX and VIX smiles, which can be solved efficiently using Sinkhorn iterations.

Computational optimal transport and entropy regularization.

Entropy-regularized transport problems have become widely used in machine learning and computational optimal transport due to their favorable numerical properties Cuturi ([2013](#bib.bib1 "Sinkhorn distances: lightspeed computation of optimal transport")); Benamou et al. ([2015](#bib.bib8 "Iterative bregman projections for regularized transportation problems")); Peyré and Cuturi ([2019](#bib.bib52 "Computational optimal transport")).
These formulations lead to Gibbs distributions whose structure enables efficient iterative algorithms.

Our contribution extends this literature by showing that entropic MOT calibration naturally induces a perturbation theory that can be used to generate risk sensitivities without recomputing the transport solution.

### 1.2 Main Contributions

The contributions of this paper are fivefold.

1. 1.

   The Linear Response (LR) System For Perturbed Optimal Transport In SPX–VIX Markets.

   We develop a perturbation framework for discrete entropic optimal transport
   under both marginal and financial constraints.
   Using the implicit function theorem applied to the dual formulation,
   we show that the calibrated Gibbs coupling depends smoothly on admissible
   market perturbations.
   This yields explicit linear-response formulas for sensitivities of arbitrary
   payoffs, governed by the Fisher information matrix of the calibrated
   exponential family.
2. 2.

   Linearized Skew Stickiness Ratio dynamics for VIX options.

   We introduce a linearization of Skew Stickiness Ratio (SSR) dynamics for
   VIX implied volatility surfaces and incorporate it as linear constraints
   within the optimal transport perturbation framework.
   This formulation provides a model-independent mechanism for propagating
   SPX perturbations to the VIX volatility smile while preserving convexity
   and tractability of the entropic projection problem.
   The SSR linearization is compatible with both the perturbation-based
   linear-response risk engine and the dimension-reduced transport framework
   developed later in the paper.
3. 3.

   Dimensional reduction (DR) Within The Perturbed Optimal Transport Framework.

   We identify a conditional coupling invariance structure under which
   the perturbed three-dimensional transport problem on
   (S1,V,S2)(S\_{1},V,S\_{2}) reduces to a two-dimensional entropic projection
   on (S1,V)(S\_{1},V).
   Under this structure the conditional kernel of S2S\_{2} given (S1,V)(S\_{1},V)
   remains fixed, so martingality and variance-consistency constraints
   are automatically preserved.
   This reduction dramatically lowers the computational complexity of
   risk generation while maintaining financial consistency of the model.
4. 4.

   Numerical validation of perturbation risk against full recalibration.

   We perform numerical experiments comparing risk sensitivities computed
   using the perturbation-based linear response system(LR) with those obtained
   from full recalibration of the SPX–VIX martingale optimal transport model.
   Across VIX futures and VIX option cross-greeks, the perturbation-based
   sensitivities closely match those obtained from recalibration while
   requiring substantially less computation.
   These results validate the perturbation framework as an accurate and
   efficient risk-generation method.
5. 5.

   Hedging backtests demonstrating practical effectiveness.

   We further evaluate the framework in a hedging backtest on randomized
   VIX option portfolios.
   Using SPX sensitivities generated by the dimension-reduced optimal
   transport method(DR), we construct dynamic hedges and compare their
   performance with hedges produced by a benchmark stochastic volatility
   model.
   The transport-based hedges consistently achieve lower hedged P&L
   variance, particularly during volatile market regimes, demonstrating
   the practical value of the proposed risk-generation framework.

These contributions show that Perturbed Optimal Transport(POT)
serves as a powerful, unified framework for SPX–VIX joint calibration, risk generation (via LR and DR), and hedging.

### 1.3 Market Consistency And Risk Propagation

In equity volatility markets the SPX and VIX option surfaces are linked through
the forward variance identity

|  |  |  |
| --- | --- | --- |
|  | ForwardVar=V​I​XF2+2​∫0V​I​XF(K−V​I​X)+​𝑑K+2​∫V​I​XF∞(V​I​X−K)+​𝑑K.\mathrm{ForwardVar}=VIX\_{F}^{2}+2\int\_{0}^{VIX\_{F}}(K-VIX)^{+}dK+2\int\_{VIX\_{F}}^{\infty}(VIX-K)^{+}dK. |  |

This relation implies that changes in SPX option prices propagate to the VIX
future level through the forward variance term structure. Differentiating the forward variance identity with respect to SPX
implied volatility parameters (for example, a parallel shift of a
volatility slice) yields

|  |  |  |
| --- | --- | --- |
|  | d​V​I​XFd​σS​P​X=d​(ForwardVar)/d​σS​P​X2​V​I​XF+2​∫B​SΔ​(K−V​I​X)+​𝑑K+2​∫B​SΔ​(V​I​X−K)+​𝑑K.\frac{dVIX\_{F}}{d\sigma\_{SPX}}=\frac{d(\mathrm{ForwardVar})/d\sigma\_{SPX}}{2VIX\_{F}+2\int BS\_{\Delta}(K-VIX)^{+}dK+2\int BS\_{\Delta}(VIX-K)^{+}dK}. |  |

In traditional stochastic volatility models the sensitivities of exotic
derivatives are obtained by applying the chain rule

|  |  |  |
| --- | --- | --- |
|  | d​payoffd​σS​P​X=∂payoff∂V​I​XF​d​V​I​XFd​σS​P​X+∂payoff∂σV​I​X​d​σV​I​Xd​σS​P​X.\frac{d\,\mathrm{payoff}}{d\sigma\_{SPX}}=\frac{\partial\mathrm{payoff}}{\partial VIX\_{F}}\frac{dVIX\_{F}}{d\sigma\_{SPX}}+\frac{\partial\mathrm{payoff}}{\partial\sigma\_{VIX}}\frac{d\sigma\_{VIX}}{d\sigma\_{SPX}}. |  |

Capturing these cross-asset sensitivities consistently is one of the central motivations for building a joint SPX–VIX model. In parametric models these sensitivities depend heavily on the assumed volatility dynamics.
More fundamentally, parametric stochastic volatility and stochastic
local volatility models cannot simultaneously recover both the SPX and
VIX marginals observed in the market. As a result, practitioners often
decouple the modeling of SPX vanillas, forward variance, and VIX
futures from the modeling of VIX options. In practice the latter is
frequently handled using Black’s formula applied directly to VIX
futures, reflecting the high liquidity of the VIX option market. But such decoupling results in the d​σV​I​Xd​σS​P​X\frac{d\sigma\_{V}IX}{d\sigma\_{S}PX} not being captured at all.

In contrast, the optimal transport approach provides a model-free calibration of
the joint distribution.
The perturbation framework developed in this paper shows that the same transport
structure can be used to generate the corresponding risk sensitivities directly
from the calibrated coupling. Guyon’s celebrated work in Guyon ([2020](#bib.bib35 "The joint S&P 500/VIX smile calibration puzzle solved"), [2021](#bib.bib4 "Dispersion-constrained martingale schrödinger problems and the exact joint S&P 500/VIX smile calibration puzzle")) has demonstrated that the OT approach gives perfect statics in that the joint calibration between SPX and VIX is perfect by construction. Our work can be seen as a decisive step forward to demonstrate even the SPX–VIX volatility dynamics can be captured accurately at no additional computational cost.

### 1.4 Martingality And Consistency Conditions

In the joint SPX–VIX calibration framework, two structural conditions must hold for the calibrated coupling to be financially meaningful.
These conditions were emphasized in the joint calibration framework of Guyon ([2020](#bib.bib35 "The joint S&P 500/VIX smile calibration puzzle solved"), [2021](#bib.bib4 "Dispersion-constrained martingale schrödinger problems and the exact joint S&P 500/VIX smile calibration puzzle")).

##### Martingality condition

Let S1S\_{1} denote the SPX level at time T1T\_{1} and S2S\_{2} the SPX level at a later maturity T2T\_{2}.

Under the risk-neutral measure, the discounted asset price must be a martingale.
Ignoring discounting for notational simplicity, the martingale condition reads

|  |  |  |
| --- | --- | --- |
|  | E​[S2∣S1,V]=S1.E[S\_{2}\mid S\_{1},V]=S\_{1}. |  |

Equivalently, for the calibrated coupling μ\mu on (S1,V,S2)(S\_{1},V,S\_{2}),

|  |  |  |
| --- | --- | --- |
|  | ∑s2s2​μ​(s1,v,s2)=s1​∑s2μ​(s1,v,s2).\sum\_{s\_{2}}s\_{2}\,\mu(s\_{1},v,s\_{2})=s\_{1}\sum\_{s\_{2}}\mu(s\_{1},v,s\_{2}). |  |

This condition ensures that the SPX dynamics implied by the calibrated distribution are arbitrage-free.

##### SPX–VIX consistency condition

The VIX index represents the square root of the risk‑neutral expectation of
future variance. In the discrete MOT framework this implies the conditional
identity

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼[L(S2/S1)|S1,V]=V2.\mathbb{E}\!\left[\,L(S\_{2}/S\_{1})\,\middle|\,S\_{1},V\right]=V^{2}. |  | (1) |

where L:=−2τ​ln⁡(x), ​τ=T2−T1=30L:=-\frac{2}{\tau}\ln(x),\text{ }\tau=T\_{2}-T\_{1}=30. This is the form used in Guyon ([2020](#bib.bib35 "The joint S&P 500/VIX smile calibration puzzle solved"), [2021](#bib.bib4 "Dispersion-constrained martingale schrödinger problems and the exact joint S&P 500/VIX smile calibration puzzle")). It enforces the forward‑variance
relation pointwise on the (S1,V)(S\_{1},V) grid and ensures structural consistency between
the SPX smile and the VIX future level. The scalar identity

|  |  |  |
| --- | --- | --- |
|  | Eμ​[V]=FV,E\_{\mu}[V]=F\_{V}, |  |

follows from this conditional relation but is strictly weaker and is not sufficient
to define a consistent SPX–VIX joint distribution.

##### Practical considerations

In real market data the SPX and VIX option surfaces are not perfectly consistent with this theoretical identity.
As observed in Guyon ([2020](#bib.bib35 "The joint S&P 500/VIX smile calibration puzzle solved"), [2021](#bib.bib4 "Dispersion-constrained martingale schrödinger problems and the exact joint S&P 500/VIX smile calibration puzzle")), calibration frameworks typically relax the consistency condition by allowing a basis between the SPX implied forward variance and the traded VIX future.

In the experiments reported in Section 9.2, we therefore compute diagnostic plots for both the martingality condition and the SPX–VIX consistency condition in order to assess the quality of the calibrated coupling.

## 2 Mathematical Framework For Entropic Projections

### 2.1 Finite Discrete Setup

Let

|  |  |  |
| --- | --- | --- |
|  | 𝒮1={s11,…,s1N1},𝒮2={s21,…,s2N2},𝒱={v1,…,vNV}\mathcal{S}\_{1}=\{s\_{1}^{1},\dots,s\_{1}^{N\_{1}}\},\quad\mathcal{S}\_{2}=\{s\_{2}^{1},\dots,s\_{2}^{N\_{2}}\},\quad\mathcal{V}=\{v^{1},\dots,v^{N\_{V}}\} |  |

be finite state spaces.

Denote

|  |  |  |
| --- | --- | --- |
|  | 𝒳:=𝒮1×𝒱×𝒮2.\mathcal{X}:=\mathcal{S}\_{1}\times\mathcal{V}\times\mathcal{S}\_{2}. |  |

Let μ¯\bar{\mu} be a strictly positive prior probability on 𝒳\mathcal{X}:

|  |  |  |
| --- | --- | --- |
|  | μ¯​(x)>0∀x∈𝒳.\bar{\mu}(x)>0\quad\forall x\in\mathcal{X}. |  |

Let prescribed marginals:

|  |  |  |
| --- | --- | --- |
|  | μ1∈Δ​(𝒮1),μV∈Δ​(𝒱),μ2∈Δ​(𝒮2),\mu\_{1}\in\Delta(\mathcal{S}\_{1}),\quad\mu\_{V}\in\Delta(\mathcal{V}),\quad\mu\_{2}\in\Delta(\mathcal{S}\_{2}), |  |

where Δ​(⋅)\Delta(\cdot) denotes the probability simplex.

Define admissible set:

|  |  |  |
| --- | --- | --- |
|  | 𝒫​(μ1,μV,μ2)={μ∈Δ​(𝒳):μ​ has marginals ​μ1,μV,μ2}.\mathcal{P}(\mu\_{1},\mu\_{V},\mu\_{2})=\left\{\mu\in\Delta(\mathcal{X}):\mu\text{ has marginals }\mu\_{1},\mu\_{V},\mu\_{2}\right\}. |  |

### 2.2 Entropic Optimal Transport

We consider the entropic projection problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | infμ∈𝒫​(μ1,μV,μ2)D​(μ∥μ¯),\inf\_{\mu\in\mathcal{P}(\mu\_{1},\mu\_{V},\mu\_{2})}D(\mu\|\bar{\mu}), |  | (2) |

where relative entropy is

|  |  |  |
| --- | --- | --- |
|  | D​(μ∥μ¯)=∑x∈𝒳μ​(x)​ln⁡μ​(x)μ¯​(x).D(\mu\|\bar{\mu})=\sum\_{x\in\mathcal{X}}\mu(x)\ln\frac{\mu(x)}{\bar{\mu}(x)}. |  |

###### Theorem 2.1 (Existence and Uniqueness).

Assume μ¯​(x)>0\bar{\mu}(x)>0 for all xx.
If 𝒫​(μ1,μV,μ2)\mathcal{P}(\mu\_{1},\mu\_{V},\mu\_{2}) is nonempty, then problem ([2](#S2.E2 "Equation 2 ‣ 2.2 Entropic Optimal Transport ‣ 2 Mathematical Framework For Entropic Projections ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport")) admits a unique minimizer μ⋆\mu^{\star}.

###### Proof.

Since 𝒳\mathcal{X} is finite, Δ​(𝒳)\Delta(\mathcal{X}) is compact and convex.

Relative entropy is strictly convex in μ\mu on the interior of the simplex because the function
x↦x​log⁡xx\mapsto x\log x
is strictly convex.

The feasible set 𝒫​(μ1,μV,μ2)\mathcal{P}(\mu\_{1},\mu\_{V},\mu\_{2}) is an affine slice of the simplex, hence convex and compact.

Strict convexity of D(⋅∥μ¯)D(\cdot\|\bar{\mu}) on a convex compact set implies existence and uniqueness of the minimizer.
∎

###### Theorem 2.2 (Primal–Dual Equivalence).

The optimal value of ([2](#S2.E2 "Equation 2 ‣ 2.2 Entropic Optimal Transport ‣ 2 Mathematical Framework For Entropic Projections ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport")) equals

|  |  |  |
| --- | --- | --- |
|  | supu1,uV,u2{Eμ1​[u1]+EμV​[uV]+Eμ2​[u2]−ln​∑x∈𝒳μ¯​(x)​eU​(x)}.\sup\_{u\_{1},u\_{V},u\_{2}}\left\{E\_{\mu\_{1}}[u\_{1}]+E\_{\mu\_{V}}[u\_{V}]+E\_{\mu\_{2}}[u\_{2}]-\ln\sum\_{x\in\mathcal{X}}\bar{\mu}(x)e^{U(x)}\right\}. |  |

Moreover, the supremum is attained.

###### Proof.

For fixed uu, consider

|  |  |  |
| --- | --- | --- |
|  | infμ∈Δ​(𝒳){D​(μ∥μ¯)−∑xμ​(x)​U​(x)}.\inf\_{\mu\in\Delta(\mathcal{X})}\left\{D(\mu\|\bar{\mu})-\sum\_{x}\mu(x)U(x)\right\}. |  |

The first-order condition gives

|  |  |  |
| --- | --- | --- |
|  | μ​(x)=μ¯​(x)​eU​(x)/Z,\mu(x)=\bar{\mu}(x)e^{U(x)}/Z, |  |

where

|  |  |  |
| --- | --- | --- |
|  | Z=∑xμ¯​(x)​eU​(x).Z=\sum\_{x}\bar{\mu}(x)e^{U(x)}. |  |

Substitution yields value −ln⁡Z-\ln Z.

Strong duality holds because the feasible set has nonempty interior.
∎

### 2.3 Gauge Fixing And Numerical Stability

The dual potentials (u1,uV,u2)(u\_{1},u\_{V},u\_{2}) are not uniquely determined.
Indeed, the Gibbs representation

|  |  |  |
| --- | --- | --- |
|  | μ​(s1,v,s2)∝μ¯​(s1,v,s2)​exp⁡(u1​(s1)+uV​(v)+u2​(s2))\mu(s\_{1},v,s\_{2})\propto\bar{\mu}(s\_{1},v,s\_{2})\exp\!\big(u\_{1}(s\_{1})+u\_{V}(v)+u\_{2}(s\_{2})\big) |  |

is invariant under the transformation

|  |  |  |
| --- | --- | --- |
|  | (u1,uV,u2)↦(u1+c1,uV+cV,u2+c2)(u\_{1},u\_{V},u\_{2})\;\mapsto\;(u\_{1}+c\_{1},\;u\_{V}+c\_{V},\;u\_{2}+c\_{2}) |  |

provided

|  |  |  |
| --- | --- | --- |
|  | c1+cV+c2=0.c\_{1}+c\_{V}+c\_{2}=0. |  |

This transformation leaves the Gibbs weights unchanged because the additive
constant cancels with the normalization factor. Consequently, the dual parameterization possesses a two–dimensional gauge
freedom. The Hessian of the dual objective therefore has a corresponding
two–dimensional null space.

To obtain a unique representation of the dual variables we fix the gauge by
imposing two independent normalization conditions. A convenient choice is

|  |  |  |
| --- | --- | --- |
|  | ∑s1∈S1μ1​(s1)​u1​(s1)=0,∑v∈VμV​(v)​uV​(v)=0.\sum\_{s\_{1}\in S\_{1}}\mu\_{1}(s\_{1})\,u\_{1}(s\_{1})=0,\qquad\sum\_{v\in V}\mu\_{V}(v)\,u\_{V}(v)=0. |  |

Under these constraints the potentials are uniquely determined up to the
remaining normalization constant absorbed by the partition function.

##### Log-partition function.

For dual potentials (u1,uV,u2)(u\_{1},u\_{V},u\_{2}) define the log-partition function

|  |  |  |
| --- | --- | --- |
|  | Λ​(u)=log​∑x∈𝒳μ¯​(x)​exp⁡(u1​(s1)+uV​(v)+u2​(s2)).\Lambda(u)=\log\sum\_{x\in\mathcal{X}}\bar{\mu}(x)\exp\!\big(u\_{1}(s\_{1})+u\_{V}(v)+u\_{2}(s\_{2})\big). |  |

This function is the cumulant generating function of the exponential family
defined by the Gibbs coupling.

Under the gauge fixing above, the potentials can be parameterized by the
reduced vector ω\omega, and we write Λ​(ω)\Lambda(\omega) for the same
log-partition function expressed in these reduced coordinates.
Let

|  |  |  |
| --- | --- | --- |
|  | ω∈ℝN1+NV+N2−2\omega\in\mathbb{R}^{N\_{1}+N\_{V}+N\_{2}-2} |  |

denote the vector of gauge–fixed dual parameters obtained by removing the
two redundant degrees of freedom. On this reduced parameter space the Hessian of the dual objective

|  |  |  |
| --- | --- | --- |
|  | H=∇ω2Λ​(ω)H=\nabla^{2}\_{\omega}\Lambda(\omega) |  |

coincides with the Fisher information matrix of the calibrated exponential
family. The gauge fixing ensures that HH is strictly positive
definite on the reduced parameter space.

This property guarantees the invertibility of the Fisher system used later
for risk computation.

## 3 Perturbation Theory: General Marginal Shocks

### 3.1 Admissible Perturbations

Let the base marginals be (μ1,μV,μ2)(\mu\_{1},\mu\_{V},\mu\_{2}) and denote the unique entropic MOT optimizer by μ⋆\mu^{\star}.

A *directional perturbation* of the marginals is a triple

|  |  |  |
| --- | --- | --- |
|  | h:=(h1,hV,h2),h1:𝒮1→ℝ,hV:𝒱→ℝ,h2:𝒮2→ℝ,h:=(h\_{1},h\_{V},h\_{2}),\qquad h\_{1}:\mathcal{S}\_{1}\to\mathbb{R},\ h\_{V}:\mathcal{V}\to\mathbb{R},\ h\_{2}:\mathcal{S}\_{2}\to\mathbb{R}, |  |

satisfying the mass-preserving constraints

|  |  |  |
| --- | --- | --- |
|  | ∑s1∈𝒮1h1​(s1)=0,∑v∈𝒱hV​(v)=0,∑s2∈𝒮2h2​(s2)=0.\sum\_{s\_{1}\in\mathcal{S}\_{1}}h\_{1}(s\_{1})=0,\quad\sum\_{v\in\mathcal{V}}h\_{V}(v)=0,\quad\sum\_{s\_{2}\in\mathcal{S}\_{2}}h\_{2}(s\_{2})=0. |  |

For ε\varepsilon sufficiently small, define perturbed marginals

|  |  |  |
| --- | --- | --- |
|  | μ1ε=μ1+ε​h1,μVε=μV+ε​hV,μ2ε=μ2+ε​h2.\mu\_{1}^{\varepsilon}=\mu\_{1}+\varepsilon h\_{1},\quad\mu\_{V}^{\varepsilon}=\mu\_{V}+\varepsilon h\_{V},\quad\mu\_{2}^{\varepsilon}=\mu\_{2}+\varepsilon h\_{2}. |  |

We assume ε\varepsilon is chosen so that μ1ε,μVε,μ2ε\mu\_{1}^{\varepsilon},\mu\_{V}^{\varepsilon},\mu\_{2}^{\varepsilon} remain strictly positive on their supports
(to stay in the interior of the simplices).

Define the perturbed feasible set

|  |  |  |
| --- | --- | --- |
|  | 𝒫ε:=𝒫​(μ1ε,μVε,μ2ε)\mathcal{P}^{\varepsilon}:=\mathcal{P}(\mu\_{1}^{\varepsilon},\mu\_{V}^{\varepsilon},\mu\_{2}^{\varepsilon}) |  |

and the perturbed entropic MOT problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | infμ∈𝒫εD​(μ∥μ¯).\inf\_{\mu\in\mathcal{P}^{\varepsilon}}D(\mu\|\bar{\mu}). |  | (3) |

Denote its unique optimizer by με\mu^{\varepsilon}.

###### Theorem 3.1 (Well-posedness of Entropic Projections).

Let 𝒜\mathcal{A} be a linear operator representing a set of KK independent linear constraints. Let 𝒫={μ∈ℝ+n:𝒜​μ=b}\mathcal{P}=\{\mu\in\mathbb{R}\_{+}^{n}:\mathcal{A}\mu=b\}. Suppose the base problem (2.2) is feasible with a strictly positive solution μ⋆\mu^{\star}. Then for any perturbation δ​b\delta b in the image of 𝒜\mathcal{A}, there exists ϵ0>0\epsilon\_{0}>0 such that for all |ϵ|<ϵ0|\epsilon|<\epsilon\_{0}, the perturbed problem with constraints b+ϵ​δ​bb+\epsilon\delta b has a unique minimizer μϵ\mu^{\epsilon}.

###### Proof.

Since μ⋆>0\mu^{\star}>0, it lies in the relative interior of the simplex. The map F:μ↦𝒜​μF:\mu\mapsto\mathcal{A}\mu is a linear surjection onto its image. By the Open Mapping Theorem, for a sufficiently small neighborhood UU of μ⋆\mu^{\star}, F​(U)F(U) contains a neighborhood of bb. Thus, for small ϵ\epsilon, the feasible set is non-empty. The strict convexity of the relative entropy ensures uniqueness.
∎

### 3.2 Dual variables And Sinkhorn Scaling Form

The dual representation (Theorem [2.2](#S2.Thmtheorem2 "Theorem 2.2 (Primal–Dual Equivalence). ‣ 2.2 Entropic Optimal Transport ‣ 2 Mathematical Framework For Entropic Projections ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport")) implies there exist optimal potentials

|  |  |  |
| --- | --- | --- |
|  | u1ε:𝒮1→ℝ,uVε:𝒱→ℝ,u2ε:𝒮2→ℝu\_{1}^{\varepsilon}:\mathcal{S}\_{1}\to\mathbb{R},\quad u\_{V}^{\varepsilon}:\mathcal{V}\to\mathbb{R},\quad u\_{2}^{\varepsilon}:\mathcal{S}\_{2}\to\mathbb{R} |  |

such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | με​(s1,v,s2)=1Zε​μ¯​(s1,v,s2)​exp⁡(u1ε​(s1)+uVε​(v)+u2ε​(s2)),\mu^{\varepsilon}(s\_{1},v,s\_{2})=\frac{1}{Z^{\varepsilon}}\,\bar{\mu}(s\_{1},v,s\_{2})\,\exp\!\Big(u\_{1}^{\varepsilon}(s\_{1})+u\_{V}^{\varepsilon}(v)+u\_{2}^{\varepsilon}(s\_{2})\Big), |  | (4) |

with Zε=∑xμ¯​(x)​eUε​(x)Z^{\varepsilon}=\sum\_{x}\bar{\mu}(x)e^{U^{\varepsilon}(x)}, Uε​(x)=u1ε​(s1)+uVε​(v)+u2ε​(s2)U^{\varepsilon}(x)=u\_{1}^{\varepsilon}(s\_{1})+u\_{V}^{\varepsilon}(v)+u\_{2}^{\varepsilon}(s\_{2}).

It is convenient to work with *scaling variables*

|  |  |  |
| --- | --- | --- |
|  | aε​(s1):=eu1ε​(s1),bε​(v):=euVε​(v),cε​(s2):=eu2ε​(s2),a^{\varepsilon}(s\_{1}):=e^{u\_{1}^{\varepsilon}(s\_{1})},\quad b^{\varepsilon}(v):=e^{u\_{V}^{\varepsilon}(v)},\quad c^{\varepsilon}(s\_{2}):=e^{u\_{2}^{\varepsilon}(s\_{2})}, |  |

so that (absorbing ZεZ^{\varepsilon} into one of the scalings if desired)

|  |  |  |  |
| --- | --- | --- | --- |
|  | με​(s1,v,s2)∝μ¯​(s1,v,s2)​aε​(s1)​bε​(v)​cε​(s2).\mu^{\varepsilon}(s\_{1},v,s\_{2})\propto\bar{\mu}(s\_{1},v,s\_{2})\,a^{\varepsilon}(s\_{1})b^{\varepsilon}(v)c^{\varepsilon}(s\_{2}). |  | (5) |

##### Gauge invariance.

Potentials are not unique: adding constants κ1,κV,κ2\kappa\_{1},\kappa\_{V},\kappa\_{2} with κ1+κV+κ2=0\kappa\_{1}+\kappa\_{V}+\kappa\_{2}=0
leaves με\mu^{\varepsilon} unchanged. We fix a gauge, e.g.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑s1μ1​(s1)​u1ε​(s1)=0,∑vμV​(v)​uVε​(v)=0,\sum\_{s\_{1}}\mu\_{1}(s\_{1})u\_{1}^{\varepsilon}(s\_{1})=0,\quad\sum\_{v}\mu\_{V}(v)u\_{V}^{\varepsilon}(v)=0, |  | (6) |

which pins down uniqueness of (u1ε,uVε,u2ε)(u\_{1}^{\varepsilon},u\_{V}^{\varepsilon},u\_{2}^{\varepsilon}) locally.

### 3.3 Differentiability Of The Entropic Projection

We now prove that the optimizer (με,uε)(\mu^{\varepsilon},u^{\varepsilon}) depends smoothly on ε\varepsilon,
and derive explicit first-order formulas.

Define the constraint maps (marginals) for any μ∈Δ​(𝒳)\mu\in\Delta(\mathcal{X}):

|  |  |  |
| --- | --- | --- |
|  | (ℳ1​μ)​(s1)=∑v,s2μ​(s1,v,s2),(ℳV​μ)​(v)=∑s1,s2μ​(s1,v,s2),(ℳ2​μ)​(s2)=∑s1,vμ​(s1,v,s2).(\mathcal{M}\_{1}\mu)(s\_{1})=\sum\_{v,s\_{2}}\mu(s\_{1},v,s\_{2}),\quad(\mathcal{M}\_{V}\mu)(v)=\sum\_{s\_{1},s\_{2}}\mu(s\_{1},v,s\_{2}),\quad(\mathcal{M}\_{2}\mu)(s\_{2})=\sum\_{s\_{1},v}\mu(s\_{1},v,s\_{2}). |  |

Stack them as ℳ​μ=(ℳ1​μ,ℳV​μ,ℳ2​μ)\mathcal{M}\mu=(\mathcal{M}\_{1}\mu,\mathcal{M}\_{V}\mu,\mathcal{M}\_{2}\mu).

Let u=(u1,uV,u2)u=(u\_{1},u\_{V},u\_{2}) and define the log-partition function

|  |  |  |
| --- | --- | --- |
|  | Λ​(u):=ln​∑x∈𝒳μ¯​(x)​eU​(x).\Lambda(u):=\ln\sum\_{x\in\mathcal{X}}\bar{\mu}(x)e^{U(x)}. |  |

Then the dual objective for marginals (ν1,νV,ν2)(\nu\_{1},\nu\_{V},\nu\_{2}) is

|  |  |  |
| --- | --- | --- |
|  | 𝒟​(u;ν):=⟨ν1,u1⟩+⟨νV,uV⟩+⟨ν2,u2⟩−Λ​(u).\mathcal{D}(u;\nu):=\langle\nu\_{1},u\_{1}\rangle+\langle\nu\_{V},u\_{V}\rangle+\langle\nu\_{2},u\_{2}\rangle-\Lambda(u). |  |

###### Lemma 3.2 (Strict concavity and smoothness of the dual).

Λ​(u)\Lambda(u) is C∞C^{\infty} and strictly convex on ℝN1+NV+N2\mathbb{R}^{N\_{1}+N\_{V}+N\_{2}} (modulo gauge).
Hence 𝒟​(u;ν)\mathcal{D}(u;\nu) is strictly concave (modulo gauge), and admits a unique maximizer under gauge fixing.

###### Proof.

Since μ¯​(x)>0\bar{\mu}(x)>0 and 𝒳\mathcal{X} is finite, Λ\Lambda is the log-sum-exp of affine functions, hence C∞C^{\infty}.
Its Hessian is the covariance matrix of the sufficient statistics under the Gibbs measure proportional to μ¯​eU\bar{\mu}e^{U},
which is positive semidefinite and positive definite on the quotient space after fixing gauge (standard exponential family theory).
∎

###### Theorem 3.3 (Differentiability of optimal potentials and coupling).

Fix a gauge as in ([6](#S3.E6 "Equation 6 ‣ Gauge invariance. ‣ 3.2 Dual variables And Sinkhorn Scaling Form ‣ 3 Perturbation Theory: General Marginal Shocks ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport")) and assume base marginals are strictly positive.
Then there exists ε0>0\varepsilon\_{0}>0 such that on (−ε0,ε0)(-\varepsilon\_{0},\varepsilon\_{0}):

1. 1.

   ε↦uε\varepsilon\mapsto u^{\varepsilon} is C1C^{1},
2. 2.

   ε↦με\varepsilon\mapsto\mu^{\varepsilon} is C1C^{1} entrywise,
3. 3.

   derivatives solve a linear system explicitly characterized by the Fisher information matrix (dual Hessian).

###### Proof.

The first-order optimality condition for the dual reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇uΛ​(uε)=νε,\nabla\_{u}\Lambda(u^{\varepsilon})=\nu^{\varepsilon}, |  | (7) |

where νε\nu^{\varepsilon} denotes the stacked perturbed marginals (μ1ε,μVε,μ2ε)(\mu\_{1}^{\varepsilon},\mu\_{V}^{\varepsilon},\mu\_{2}^{\varepsilon})
embedded in ℝN1+NV+N2\mathbb{R}^{N\_{1}+N\_{V}+N\_{2}}.

Under gauge fixing, Lemma [3.2](#S3.Thmtheorem2 "Lemma 3.2 (Strict concavity and smoothness of the dual). ‣ 3.3 Differentiability Of The Entropic Projection ‣ 3 Perturbation Theory: General Marginal Shocks ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport") implies ∇uΛ\nabla\_{u}\Lambda is C∞C^{\infty} with Jacobian
Hε:=∇u2Λ​(uε)H^{\varepsilon}:=\nabla\_{u}^{2}\Lambda(u^{\varepsilon}) invertible on the gauge-fixed subspace.
Thus, by the implicit function theorem applied to

|  |  |  |
| --- | --- | --- |
|  | F​(u,ε):=∇uΛ​(u)−νε,F(u,\varepsilon):=\nabla\_{u}\Lambda(u)-\nu^{\varepsilon}, |  |

there exists a unique C1C^{1} map ε↦uε\varepsilon\mapsto u^{\varepsilon} locally satisfying ([7](#S3.E7 "Equation 7 ‣ Proof. ‣ 3.3 Differentiability Of The Entropic Projection ‣ 3 Perturbation Theory: General Marginal Shocks ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport")).

Differentiating ([7](#S3.E7 "Equation 7 ‣ Proof. ‣ 3.3 Differentiability Of The Entropic Projection ‣ 3 Perturbation Theory: General Marginal Shocks ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport")) gives

|  |  |  |
| --- | --- | --- |
|  | Hε​u˙ε=ν˙ε,H^{\varepsilon}\,\dot{u}^{\varepsilon}=\dot{\nu}^{\varepsilon}, |  |

where dots denote d/d​εd/d\varepsilon and ν˙ε=(h1,hV,h2)\dot{\nu}^{\varepsilon}=(h\_{1},h\_{V},h\_{2}) is constant.
Hence u˙ε=(Hε)−1​ν˙ε\dot{u}^{\varepsilon}=(H^{\varepsilon})^{-1}\dot{\nu}^{\varepsilon} on the gauge-fixed subspace.

Finally, με\mu^{\varepsilon} is given by the smooth Gibbs map ([4](#S3.E4 "Equation 4 ‣ 3.2 Dual variables And Sinkhorn Scaling Form ‣ 3 Perturbation Theory: General Marginal Shocks ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport")), so entrywise differentiability follows by chain rule.
∎

### 3.4 Risk Representation: Gateaux Derivative Of Expectations

Let G:𝒳→ℝG:\mathcal{X}\to\mathbb{R} be any payoff (bounded is automatic since 𝒳\mathcal{X} finite).
Define the model price under calibration με\mu^{\varepsilon} by

|  |  |  |
| --- | --- | --- |
|  | Π​(ε):=𝔼με​[G]=∑x∈𝒳G​(x)​με​(x).\Pi(\varepsilon):=\mathbb{E}\_{\mu^{\varepsilon}}[G]=\sum\_{x\in\mathcal{X}}G(x)\mu^{\varepsilon}(x). |  |

###### Theorem 3.4 (General risk representation).

Let G:𝒳→ℝG:\mathcal{X}\to\mathbb{R} be any payoff and let

|  |  |  |
| --- | --- | --- |
|  | Π​(ε)=𝔼με​[G]\Pi(\varepsilon)=\mathbb{E}\_{\mu^{\varepsilon}}[G] |  |

denote its price under the perturbed entropic projection.
Under the assumptions of Theorem 3.3, the map ε↦Π​(ε)\varepsilon\mapsto\Pi(\varepsilon)
is C1C^{1} and its first–order variation is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Π′​(0)=⟨h1,ψ1⟩+⟨hV,ψV⟩+⟨h2,ψ2⟩.\Pi^{\prime}(0)=\langle h\_{1},\psi\_{1}\rangle+\langle h\_{V},\psi\_{V}\rangle+\langle h\_{2},\psi\_{2}\rangle. |  | (8) |

The vector ψ=(ψ1,ψV,ψ2)\psi=(\psi\_{1},\psi\_{V},\psi\_{2}) is the *influence function*
of the payoff GG and is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ=(H0)−1​gG,\psi=(H^{0})^{-1}g\_{G}, |  | (9) |

where H0=∇u2Λ​(u0)H^{0}=\nabla^{2}\_{u}\Lambda(u^{0}) is the Fisher information matrix of the
calibrated exponential family, and gGg\_{G} is the covariance vector

|  |  |  |
| --- | --- | --- |
|  | (gG)i=Covμ∗⁡(G,Ti),(g\_{G})\_{i}=\operatorname{Cov}\_{\mu^{\*}}(G,\,T\_{i}), |  |

with {Ti}\{T\_{i}\} denoting the sufficient statistics associated with the dual
potentials u=(u1,uV,u2)u=(u\_{1},u\_{V},u\_{2}). Thus, to first order,
perturbations of the marginals propagate through the inverse Fisher information
and the covariance of GG with the sufficient statistics.

###### Proof.

Since με\mu^{\varepsilon} is C1C^{1} in ε\varepsilon by Theorem 3.3 and
𝒳\mathcal{X} is finite, the price

|  |  |  |
| --- | --- | --- |
|  | Π​(ε)=∑x∈𝒳G​(x)​με​(x)\Pi(\varepsilon)=\sum\_{x\in\mathcal{X}}G(x)\,\mu^{\varepsilon}(x) |  |

is C1C^{1} and

|  |  |  |
| --- | --- | --- |
|  | Π′​(0)=∑xG​(x)​μ˙0​(x),\Pi^{\prime}(0)=\sum\_{x}G(x)\,\dot{\mu}^{0}(x), |  |

where μ˙0\dot{\mu}^{0} denotes dd​ε​με|ε=0\frac{d}{d\varepsilon}\mu^{\varepsilon}\big|\_{\varepsilon=0}.

From the Gibbs representation,

|  |  |  |
| --- | --- | --- |
|  | με​(x)=exp⁡(log⁡μ¯​(x)+Uε​(x)−Λ​(uε)),\mu^{\varepsilon}(x)=\exp\!\big(\log\bar{\mu}(x)+U^{\varepsilon}(x)-\Lambda(u^{\varepsilon})\big), |  |

with

|  |  |  |
| --- | --- | --- |
|  | Uε​(x)=u1ε​(s1)+uVε​(v)+u2ε​(s2),Λ​(u)=log​∑xμ¯​(x)​eU​(x),U^{\varepsilon}(x)=u\_{1}^{\varepsilon}(s\_{1})+u\_{V}^{\varepsilon}(v)+u\_{2}^{\varepsilon}(s\_{2}),\qquad\Lambda(u)=\log\!\sum\_{x}\bar{\mu}(x)e^{U(x)}, |  |

we obtain the standard exponential-family derivative

|  |  |  |
| --- | --- | --- |
|  | μ˙0​(x)μ∗​(x)=U˙0​(x)−𝔼μ∗​[U˙0],\frac{\dot{\mu}^{0}(x)}{\mu^{\*}(x)}=\dot{U}^{0}(x)-\mathbb{E}\_{\mu^{\*}}[\dot{U}^{0}], |  |

where μ∗=μ0\mu^{\*}=\mu^{0}.

Since UεU^{\varepsilon} is linear in the potentials,

|  |  |  |
| --- | --- | --- |
|  | U˙0​(s1,v,s2)=u˙10​(s1)+u˙V0​(v)+u˙20​(s2)=⟨u˙0,T​(x)⟩,\dot{U}^{0}(s\_{1},v,s\_{2})=\dot{u}\_{1}^{0}(s\_{1})+\dot{u}\_{V}^{0}(v)+\dot{u}\_{2}^{0}(s\_{2})=\langle\dot{u}^{0},\,T(x)\rangle, |  |

where T​(x)T(x) is the vector of sufficient statistics (indicator functions
of s1s\_{1}, vv, s2s\_{2}). Substituting ([3.4](#S3.Ex42 "Proof. ‣ 3.4 Risk Representation: Gateaux Derivative Of Expectations ‣ 3 Perturbation Theory: General Marginal Shocks ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport")) into Π′​(0)\Pi^{\prime}(0) gives

|  |  |  |
| --- | --- | --- |
|  | Π′​(0)=⟨u˙0,Covμ∗⁡(G,T)⟩=⟨u˙0,gG⟩,\Pi^{\prime}(0)=\left\langle\dot{u}^{0},\operatorname{Cov}\_{\mu^{\*}}(G,\,T)\right\rangle=\langle\dot{u}^{0},\,g\_{G}\rangle, |  |

where gGg\_{G} is the covariance vector

|  |  |  |
| --- | --- | --- |
|  | (gG)i=Covμ∗⁡(G,Ti).(g\_{G})\_{i}=\operatorname{Cov}\_{\mu^{\*}}(G,\,T\_{i}). |  |

To identify u˙0\dot{u}^{0}, differentiate the dual KKT condition

|  |  |  |
| --- | --- | --- |
|  | ∇uΛ​(uε)=νε\nabla\_{u}\Lambda(u^{\varepsilon})=\nu^{\varepsilon} |  |

at ε=0\varepsilon=0. Since
∇u2Λ​(u0)=H0\nabla\_{u}^{2}\Lambda(u^{0})=H^{0} is the Fisher information matrix,
we obtain the linear system

|  |  |  |
| --- | --- | --- |
|  | H0​u˙0=ν˙,H^{0}\,\dot{u}^{0}=\dot{\nu}, |  |

where ν˙\dot{\nu} is the perturbation of the marginal constraints,
i.e. ν˙=(h1,hV,h2)\dot{\nu}=(h\_{1},h\_{V},h\_{2}) in the gauge-fixed coordinates.
Solving ([3.4](#S3.Ex49 "Proof. ‣ 3.4 Risk Representation: Gateaux Derivative Of Expectations ‣ 3 Perturbation Theory: General Marginal Shocks ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport")) yields

|  |  |  |
| --- | --- | --- |
|  | u˙0=(H0)−1​ν˙.\dot{u}^{0}=(H^{0})^{-1}\dot{\nu}. |  |

Finally, substituting this expression for u˙0\dot{u}^{0} into
([3.4](#S3.Ex45 "Proof. ‣ 3.4 Risk Representation: Gateaux Derivative Of Expectations ‣ 3 Perturbation Theory: General Marginal Shocks ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport")) gives

|  |  |  |
| --- | --- | --- |
|  | Π′​(0)=⟨(H0)−1​ν˙,gG⟩=⟨ν˙,(H0)−1​gG⟩.\Pi^{\prime}(0)=\langle(H^{0})^{-1}\dot{\nu},\,g\_{G}\rangle=\langle\dot{\nu},\,(H^{0})^{-1}g\_{G}\rangle. |  |

Define the influence function

|  |  |  |
| --- | --- | --- |
|  | ψ:=(H0)−1​gG,\psi:=(H^{0})^{-1}g\_{G}, |  |

so that

|  |  |  |
| --- | --- | --- |
|  | Π′​(0)=⟨h1,ψ1⟩+⟨hV,ψV⟩+⟨h2,ψ2⟩.\Pi^{\prime}(0)=\langle h\_{1},\psi\_{1}\rangle+\langle h\_{V},\psi\_{V}\rangle+\langle h\_{2},\psi\_{2}\rangle. |  |

This completes the proof.
∎

###### Remark (Practitioner interpretation).

Equation ([8](#S3.E8 "Equation 8 ‣ Theorem 3.4 (General risk representation). ‣ 3.4 Risk Representation: Gateaux Derivative Of Expectations ‣ 3 Perturbation Theory: General Marginal Shocks ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport")) states: to first order, the price sensitivity of any payoff GG under marginal shocks
is obtained by pairing the marginal shock directions with a set of influence functions computed from the calibrated Gibbs coupling.
This converts “bump-and-revalue” into a mathematically controlled linear response.

### 3.5 Second-Order Sensitivity Expansion

The linear response formula derived in Theorem 3.4 characterizes the first-order
sensitivity of model prices under marginal perturbations. We now establish a
second-order expansion that quantifies the approximation error of the linear
risk formula.

###### Theorem 3.5 (Second-Order Risk Expansion).

Assume the conditions of Theorem 3.3. Let G:X→ℝG:X\to\mathbb{R} be any payoff and
consider perturbed marginals νϵ=ν+ϵ​h\nu\_{\epsilon}=\nu+\epsilon h.

Then the price function

|  |  |  |
| --- | --- | --- |
|  | Π​(ϵ)=𝔼μϵ​[G]\Pi(\epsilon)=\mathbb{E}\_{\mu\_{\epsilon}}[G] |  |

admits the expansion

|  |  |  |
| --- | --- | --- |
|  | Π​(ϵ)=Π​(0)+ϵ​⟨h,ψ⟩+ϵ22​h⊤​KG​h+o​(ϵ2),\Pi(\epsilon)=\Pi(0)+\epsilon\langle h,\psi\rangle+\frac{\epsilon^{2}}{2}h^{\top}K\_{G}h+o(\epsilon^{2}), |  |

where KGK\_{G} is a symmetric matrix depending on the third-order derivatives of
the log-partition function Λ​(u)\Lambda(u).

Moreover, there exists a constant CC such that

|  |  |  |
| --- | --- | --- |
|  | |Π​(ϵ)−Π​(0)−ϵ​⟨h,ψ⟩|≤C​ϵ2​‖h‖2.|\Pi(\epsilon)-\Pi(0)-\epsilon\langle h,\psi\rangle|\leq C\epsilon^{2}\|h\|^{2}. |  |

###### Proof.

Since the dual potentials uϵu\_{\epsilon} are C2C^{2} functions of ϵ\epsilon by the
implicit function theorem and smoothness of Λ​(u)\Lambda(u), the coupling
μϵ\mu\_{\epsilon} is twice differentiable in ϵ\epsilon.

Applying a second-order Taylor expansion to

|  |  |  |
| --- | --- | --- |
|  | Π​(ϵ)=∑xG​(x)​μϵ​(x)\Pi(\epsilon)=\sum\_{x}G(x)\mu\_{\epsilon}(x) |  |

yields the stated expansion. The quadratic term arises from the second
derivative of the dual potentials and the third-order cumulants of the
exponential family distribution defined by the Gibbs coupling.

Boundedness follows from smoothness of Λ\Lambda and compactness of the simplex.
∎

### 3.6 Stability Bounds

###### Proposition 3.6 (Lipschitz stability of potentials and couplings).

Under the assumptions of Theorem [3.3](#S3.Thmtheorem3 "Theorem 3.3 (Differentiability of optimal potentials and coupling). ‣ 3.3 Differentiability Of The Entropic Projection ‣ 3 Perturbation Theory: General Marginal Shocks ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport"),
there exists C>0C>0 such that for all sufficiently small ε\varepsilon:

|  |  |  |
| --- | --- | --- |
|  | ‖uε−u0‖≤C​|ε|​‖(h1,hV,h2)‖,‖με−μ⋆‖1≤C​|ε|​‖(h1,hV,h2)‖.\|u^{\varepsilon}-u^{0}\|\leq C|\varepsilon|\|(h\_{1},h\_{V},h\_{2})\|,\qquad\|\mu^{\varepsilon}-\mu^{\star}\|\_{1}\leq C|\varepsilon|\|(h\_{1},h\_{V},h\_{2})\|. |  |

###### Proof.

From the implicit function theorem, u˙ε=(Hε)−1​ν˙\dot{u}^{\varepsilon}=(H^{\varepsilon})^{-1}\dot{\nu} and HεH^{\varepsilon} varies continuously in ε\varepsilon.
On a compact neighborhood, the operator norm of (Hε)−1(H^{\varepsilon})^{-1} is bounded by some CC.
Integrate u˙ε\dot{u}^{\varepsilon} over ε\varepsilon to get the first bound.
The second bound follows from smoothness of the Gibbs map με=𝒢​(uε)\mu^{\varepsilon}=\mathcal{G}(u^{\varepsilon})
and bounded Jacobian on the same neighborhood.
∎

### 3.7 Information-Geometric Interpretation

The perturbation theory derived above admits a natural interpretation in terms
of information geometry.

The calibrated coupling

|  |  |  |
| --- | --- | --- |
|  | μ⋆​(x)=μ¯​(x)​exp⁡(U∗​(x))/Z∗\mu^{\star}(x)=\bar{\mu}(x)\exp(U^{\*}(x))/Z^{\*} |  |

defines an exponential family distribution with sufficient statistics given by
the marginal indicator functions.

The Hessian of the log-partition function

|  |  |  |
| --- | --- | --- |
|  | H=∇2Λ​(u)H=\nabla^{2}\Lambda(u) |  |

coincides with the Fisher information matrix of this exponential family.

Consequently, the linear response system

|  |  |  |
| --- | --- | --- |
|  | H​u˙=hH\dot{u}=h |  |

can be interpreted geometrically as projecting marginal perturbations onto the
tangent space of the exponential family manifold.

The risk representation

|  |  |  |
| --- | --- | --- |
|  | Π′​(0)=g⊤​H−1​h\Pi^{\prime}(0)=g^{\top}H^{-1}h |  |

therefore corresponds to a natural Riemannian metric induced by the Fisher
information. In this view, sensitivities arise from the dual affine
connections of the exponential family manifold
Amari ([2016](#bib.bib9 "Information geometry and its applications")); Peyré and Cuturi ([2019](#bib.bib52 "Computational optimal transport")).

This geometric interpretation highlights that the entropic MOT calibration
defines not only a transport plan but also an intrinsic statistical manifold
whose local curvature governs the propagation of market shocks.

##### Economic interpretation.

The perturbation framework can be interpreted as solving a nearby optimal
transport problem whose prior is the calibrated coupling μ⋆\mu^{\star}.
A marginal perturbation corresponds to a change in market forwards or option prices.
The entropic projection identifies the closest joint distribution consistent
with the new market information.

This perspective shows that the risk sensitivities derived in this paper are
not tied to any specific stochastic volatility model.
Instead they arise from the geometry of the calibrated transport plan.
In this sense the risk generation mechanism is largely model independent.

## 4 Martingality And Variance Consistency As Linear Constraints

Sections 2 and 3 developed the perturbation theory for the general entropic
projection problem with marginal constraints only. In the SPX–VIX joint
calibration problem, however, the admissible set must also satisfy the
fundamental no–arbitrage relations linking the SPX dynamics and the VIX
definition.

Accordingly, the feasible set of couplings is obtained by intersecting the
marginal constraint set with additional linear constraints enforcing
martingality of the SPX process and consistency between the VIX level and the
forward variance implied by the SPX distribution.

Let AmargA\_{\mathrm{marg}} denote the operator imposing the marginal constraints
and let AfinA\_{\mathrm{fin}} denote the operator encoding the financial
constraints described below. The admissible set therefore takes the form

|  |  |  |
| --- | --- | --- |
|  | 𝒫={μ∈Δ​(X):Amarg​μ=ν,Afin​μ=0}.\mathcal{P}=\{\,\mu\in\Delta(X):A\_{\mathrm{marg}}\mu=\nu,\;A\_{\mathrm{fin}}\mu=0\}. |  |

This formulation preserves the convex structure of the entropic projection
problem because both sets of constraints remain linear in μ\mu. The
perturbation analysis of Section 3 therefore continues to apply once the
perturbations are restricted to the tangent subspace compatible with these
financial constraints.

### 4.1 Definition Of Financial Constraints

The financial constraints appearing in the admissible set above are now
specified explicitly. They enforce the martingale property of the SPX process
and the consistency relation linking the VIX level to the forward variance
implied by the SPX distribution. Both constraints are linear in the coupling
μ\mu and therefore define components of the operator AfinA\_{\mathrm{fin}}.

We define the Martingale and Variance Consistency constraints as follows:

* •

  Martingale Constraint: For every grid point (s1,i,vj)(s\_{1,i},v\_{j}), the conditional expectation of the terminal spot must equal the forward:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ∑kμ​(s1,i,vj,s2,k)​s2,k=s1,i⋅μ​(s1,i,vj,⋅)\sum\_{k}\mu(s\_{1,i},v\_{j},s\_{2,k})s\_{2,k}=s\_{1,i}\cdot\mu(s\_{1,i},v\_{j},\cdot) |  | (9) |
* •

  Variance Consistency: The VIX index must represent the fair strike of a log-contract on S2S\_{2}:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ∑kμ​(s1,i,vj,s2,k)​ℒ​(s2,k/s1,i)=vj2⋅μ​(s1,i,vj,⋅)\sum\_{k}\mu(s\_{1,i},v\_{j},s\_{2,k})\mathcal{L}(s\_{2,k}/s\_{1,i})=v\_{j}^{2}\cdot\mu(s\_{1,i},v\_{j},\cdot) |  | (10) |

### 4.2 The Tangent Subspace Of Risk

Under this framework, the total constraint operator 𝒜\mathcal{A} is the concatenation of the marginal constraints 𝒜m​a​r​g\mathcal{A}\_{marg} and the financial constraints 𝒜fin\mathcal{A}\_{\mathrm{fin}}, i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜=(𝒜marg,𝒜fin)\mathcal{A}=(\mathcal{A}\_{\mathrm{marg}},\mathcal{A}\_{\mathrm{fin}}) |  | (11) |

When we compute risk (Greeks), we are interested in perturbations δ​b\delta b of the marginals. However, to maintain market consistency, the resulting shift in the measure δ​μ\delta\mu must satisfy the linearized system:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝒜m​a​r​g𝒜fin)​δ​μ=(δ​ν0)\begin{pmatrix}\mathcal{A}\_{marg}\\ \mathcal{A}\_{\mathrm{fin}}\end{pmatrix}\delta\mu=\begin{pmatrix}\delta\nu\\ 0\end{pmatrix} |  | (12) |

This implies that the risk sensitivities are gradients of the Dual Objective restricted to the tangent subspace defined by the kernel of 𝒜fin\mathcal{A}\_{\mathrm{fin}}.

###### Remark.

The well-posedness argued in Section 3 ensures that as long as the market data ν\nu allows for the existence of any martingale measure (a standard assumption in no-arbitrage theory), our entropic projection will smoothly track the market changes.

## 5 Financial Perturbations: Spot And Volatility Bumps

### 5.1 SPX Spot Perturbation

Let the SPX grid at time T1T\_{1} be 𝒮1={s1i}\mathcal{S}\_{1}=\{s\_{1}^{i}\}.
A spot bump corresponds to shifting the forward level:

|  |  |  |
| --- | --- | --- |
|  | S0↦S0+δ.S\_{0}\mapsto S\_{0}+\delta. |  |

In a discrete marginal representation, this induces a redistribution of mass
via interpolation on the grid. Formally, define the perturbed marginal

|  |  |  |
| --- | --- | --- |
|  | μ1δ​(s1i)=μ1​(s1i−δ)\mu\_{1}^{\delta}(s\_{1}^{i})=\mu\_{1}(s\_{1}^{i}-\delta) |  |

interpreted via linear interpolation.

###### Proposition 5.1 (Admissibility of small spot perturbations).

For sufficiently small δ\delta, the perturbed marginal μ1δ\mu\_{1}^{\delta}
is strictly positive and satisfies

|  |  |  |
| --- | --- | --- |
|  | ∑iμ1δ​(s1i)=1.\sum\_{i}\mu\_{1}^{\delta}(s\_{1}^{i})=1. |  |

Moreover, the directional derivative

|  |  |  |
| --- | --- | --- |
|  | h1​(s1i)=dd​δ​μ1δ​(s1i)|δ=0h\_{1}(s\_{1}^{i})=\left.\frac{d}{d\delta}\mu\_{1}^{\delta}(s\_{1}^{i})\right|\_{\delta=0} |  |

satisfies ∑ih1​(s1i)=0\sum\_{i}h\_{1}(s\_{1}^{i})=0.

###### Proof.

Mass preservation follows from change-of-variable invariance.
Differentiating under interpolation preserves zero total mass.
∎

Hence spot bump induces admissible perturbation in the sense of Section 4.

### 5.2 SPX Implied Volatility Surface Perturbation

Consider a parallel implied volatility bump:

|  |  |  |
| --- | --- | --- |
|  | σ​(K,T)↦σ​(K,T)+δ.\sigma(K,T)\mapsto\sigma(K,T)+\delta. |  |

Through option pricing, this modifies call prices C​(K)C(K).
Using Breeden-Litzenberger inversion, the marginal density changes:

|  |  |  |
| --- | --- | --- |
|  | μ1δ​(s)=∂2Cδ​(K)∂K2|K=s.\mu\_{1}^{\delta}(s)=\frac{\partial^{2}C^{\delta}(K)}{\partial K^{2}}\Big|\_{K=s}. |  |

###### Proposition 5.2 (Admissibility of small volatility perturbations).

For sufficiently small δ\delta, the perturbed marginal
μ1δ\mu\_{1}^{\delta} remains strictly positive and defines a valid
probability distribution.

###### Proof.

Black-Scholes prices are smooth in σ\sigma.
For sufficiently small perturbations,
convexity in strike is preserved,
ensuring nonnegative density.
Mass preservation follows from boundary behavior.
∎

Thus volatility bumps define admissible h1h\_{1} directions.

## 6 SSR Dynamics For VIX And Its Linearization

### 6.1 Skew Stickiness Ratio: Bergomi’s Definition And Extension To VIX

We now give a formal definition of the Skew Stickiness Ratio (SSR) following
 Bergomi ([2016](#bib.bib21 "Stochastic volatility modeling"), [2009](#bib.bib31 "Smile dynamics II")).
Let σ​(K,F)\sigma(K,F) denote the implied volatility of an option with strike KK
and forward level FF of the underlying asset.
Bergomi models smile dynamics by expressing first–order reactions of the
volatility surface to changes in the forward.

#### 6.1.1 Bergomi’s Definition of Skew Stickiness Ratio

Consider the ATM implied volatility

|  |  |  |
| --- | --- | --- |
|  | σATM​(F):=σ​(F,F),\sigma\_{\mathrm{ATM}}(F):=\sigma(F,F), |  |

and the ATM skew

|  |  |  |
| --- | --- | --- |
|  | Skew​(F):=∂σ​(K,F)∂K|K=F.\mathrm{Skew}(F):=\left.\frac{\partial\sigma(K,F)}{\partial K}\right|\_{K=F}. |  |

Bergomi introduces a dimensionless parameter SSR\mathrm{SSR} through the
decomposition

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂σ​(K,F)∂F=−SSR⋅Skew​(F)(Bergomi).\frac{\partial\sigma(K,F)}{\partial F}=-\,\mathrm{SSR}\cdot\mathrm{Skew}(F)\qquad\text{(Bergomi)}. |  | (13) |

Thus a perturbation δ​F\delta F in the forward produces the leading–order smile
shift

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​σ​(K)=−SSR⋅Skew​(F)​δ​F(K​ fixed).\delta\sigma(K)=-\,\mathrm{SSR}\cdot\mathrm{Skew}(F)\,\delta F\qquad(K\text{ fixed}). |  | (14) |

The limiting cases correspond to standard practitioner regimes:

* •

  SSR=1\mathrm{SSR}=1: Sticky strike (vol surface fixed in strike space),
* •

  SSR=0\mathrm{SSR}=0: Sticky delta,
* •

  SSR>1\mathrm{SSR}>1: Super skew.

#### 6.1.2 Extension to VIX Futures And VIX Options

Let FVF\_{V} denote the VIX future level and let σV​(K,FV)\sigma\_{V}(K,F\_{V}) denote the VIX
option implied volatility.
Define the VIX skew

|  |  |  |
| --- | --- | --- |
|  | SkewV​(FV):=∂σV​(K,FV)∂K|K=FV.\mathrm{Skew}\_{V}(F\_{V}):=\left.\frac{\partial\sigma\_{V}(K,F\_{V})}{\partial K}\right|\_{K=F\_{V}}. |  |

By analogy with Bergomi’s equity SSR, we define the VIX Skew Stickiness Ratio
SSRV\mathrm{SSR}\_{V} via

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂σV​(K,FV)∂FV=−SSRV⋅SkewV​(FV).\frac{\partial\sigma\_{V}(K,F\_{V})}{\partial F\_{V}}=-\,\mathrm{SSR}\_{V}\cdot\mathrm{Skew}\_{V}(F\_{V}). |  | (15) |

Thus the volatility shift induced by a perturbation δ​FV\delta F\_{V} in the VIX
future is

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​σV​(K)=−SSRV⋅SkewV​(FV)​δ​FV.\delta\sigma\_{V}(K)=-\,\mathrm{SSR}\_{V}\cdot\mathrm{Skew}\_{V}(F\_{V})\,\delta F\_{V}. |  | (16) |

### 6.2 Linear SSR Approximation And Second–Order Accuracy

We now derive the linear Skew Stickiness Ratio (SSR) approximation used in the
perturbed optimal transport framework, and quantify its accuracy in a single,
self–contained result.

Let FVF\_{V} denote the VIX future and σV​(K,FV)\sigma\_{V}(K,F\_{V}) the VIX implied
volatility.
Following Bergomi Bergomi ([2009](#bib.bib31 "Smile dynamics II")), the VIX Skew Stickiness Ratio is defined
by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂σV​(K,FV)∂FV=−SSRV⋅SkewV​(FV),\frac{\partial\sigma\_{V}(K,F\_{V})}{\partial F\_{V}}=-\,\mathrm{SSR}\_{V}\cdot\mathrm{Skew}\_{V}(F\_{V}), |  | (17) |

where

|  |  |  |
| --- | --- | --- |
|  | SkewV​(FV)=∂σV​(K,FV)∂K|K=FV,SSRV>0.\mathrm{Skew}\_{V}(F\_{V})=\left.\frac{\partial\sigma\_{V}(K,F\_{V})}{\partial K}\right|\_{K=F\_{V}},\qquad\mathrm{SSR}\_{V}>0. |  |

We now formalize the linearization implicit in
([17](#S6.E17 "Equation 17 ‣ 6.2 Linear SSR Approximation And Second–Order Accuracy ‣ 6 SSR Dynamics For VIX And Its Linearization ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport")), and simultaneously provide a quantitative
error bound.

###### Theorem 6.1 (Unified linear SSR expansion with second–order error).

Assume σV​(K,FV)\sigma\_{V}(K,F\_{V}) is C2C^{2} in the forward variable FVF\_{V} in a
neighborhood of the base level FVF\_{V}.
Let FV′=FV+δF\_{V}^{\prime}=F\_{V}+\delta.
Then the implied volatility satisfies the expansion

|  |  |  |  |
| --- | --- | --- | --- |
|  | σV​(K,FV′)=σV​(K,FV)−SSRV⋅SkewV​(FV)​δ+RK​(δ),\sigma\_{V}(K,F\_{V}^{\prime})=\sigma\_{V}(K,F\_{V})-\mathrm{SSR}\_{V}\cdot\mathrm{Skew}\_{V}(F\_{V})\,\delta+R\_{K}(\delta), |  | (18) |

where the remainder satisfies the deterministic bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | |RK​(δ)|≤12​sup|u−FV|≤|δ||∂2σV​(K,u)∂FV2|​δ2.\bigl|R\_{K}(\delta)\bigr|\leq\frac{1}{2}\sup\_{\lvert u-F\_{V}\rvert\leq\lvert\delta\rvert}\left|\frac{\partial^{2}\sigma\_{V}(K,u)}{\partial F\_{V}^{2}}\right|\,\delta^{2}. |  | (19) |

In particular, the linear SSR approximation

|  |  |  |  |
| --- | --- | --- | --- |
|  | σV​(K,FV′)≈σV​(K,FV)−SSRV⋅SkewV​(FV)​(FV′−FV)\sigma\_{V}(K,F\_{V}^{\prime})\approx\sigma\_{V}(K,F\_{V})-\mathrm{SSR}\_{V}\cdot\mathrm{Skew}\_{V}(F\_{V})\,(F\_{V}^{\prime}-F\_{V}) |  | (20) |

is accurate to first order, with an O​(δ2)O(\delta^{2}) error uniformly controlled by
([19](#S6.E19 "Equation 19 ‣ Theorem 6.1 (Unified linear SSR expansion with second–order error). ‣ 6.2 Linear SSR Approximation And Second–Order Accuracy ‣ 6 SSR Dynamics For VIX And Its Linearization ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport")).

###### Proof.

Apply Taylor’s theorem to σV​(K,FV′)\sigma\_{V}(K,F\_{V}^{\prime}) in the variable FVF\_{V}:

|  |  |  |
| --- | --- | --- |
|  | σV​(K,FV+δ)=σV​(K,FV)+∂σV∂FV​(K,FV)​δ+12​∂2σV∂FV2​(K,ξ)​δ2,\sigma\_{V}(K,F\_{V}+\delta)=\sigma\_{V}(K,F\_{V})+\frac{\partial\sigma\_{V}}{\partial F\_{V}}(K,F\_{V})\,\delta+\frac{1}{2}\,\frac{\partial^{2}\sigma\_{V}}{\partial F\_{V}^{2}}(K,\xi)\,\delta^{2}, |  |

for some ξ\xi between FVF\_{V} and FV+δF\_{V}+\delta.
Using the SSR identity

|  |  |  |
| --- | --- | --- |
|  | ∂σV∂FV​(K,FV)=−SSRV​SkewV​(FV)\frac{\partial\sigma\_{V}}{\partial F\_{V}}(K,F\_{V})=-\,\mathrm{SSR}\_{V}\,\mathrm{Skew}\_{V}(F\_{V}) |  |

yields the expression ([18](#S6.E18 "Equation 18 ‣ Theorem 6.1 (Unified linear SSR expansion with second–order error). ‣ 6.2 Linear SSR Approximation And Second–Order Accuracy ‣ 6 SSR Dynamics For VIX And Its Linearization ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport")), and the bound
([19](#S6.E19 "Equation 19 ‣ Theorem 6.1 (Unified linear SSR expansion with second–order error). ‣ 6.2 Linear SSR Approximation And Second–Order Accuracy ‣ 6 SSR Dynamics For VIX And Its Linearization ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport")) follows by taking the supremum of the second
derivative over the interval. ∎

##### Interpretation.

The first–order term in ([18](#S6.E18 "Equation 18 ‣ Theorem 6.1 (Unified linear SSR expansion with second–order error). ‣ 6.2 Linear SSR Approximation And Second–Order Accuracy ‣ 6 SSR Dynamics For VIX And Its Linearization ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport")) gives the SSR–based
linear smile reaction used in the perturbed optimal transport constraints.
The explicit O​(δ2)O(\delta^{2}) bound in ([19](#S6.E19 "Equation 19 ‣ Theorem 6.1 (Unified linear SSR expansion with second–order error). ‣ 6.2 Linear SSR Approximation And Second–Order Accuracy ‣ 6 SSR Dynamics For VIX And Its Linearization ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport")) quantifies the
approximation error and shows that the SSR mapping is highly accurate for the
small forward perturbations relevant for risk generation.

### 6.3 Why VIX Dynamics Must Be Introduced

The entropic martingale optimal transport calibration determines a joint
distribution of (S1,V,S2)(S\_{1},V,S\_{2}) that is fully consistent with observed SPX and
VIX option prices. However, the resulting calibrated coupling is inherently a
*static object*. In particular, the transport formulation itself does not
impose any dynamic rule governing how the VIX smile evolves under perturbations
of the SPX surface.

In contrast, risk management in volatility markets requires a specification of
how both the VIX future level and the VIX implied volatility smile react to
changes in the SPX surface. In traditional stochastic volatility models this
dynamic behavior is encoded through the joint dynamics of the spot and variance
processes. For example, perturbations of the SPX volatility surface affect both
the forward variance level and the volatility-of-volatility parameters, which
in turn determine the evolution of VIX option prices.

Within the optimal transport framework, however, the calibration produces only
a joint distribution consistent with option prices and martingale constraints.
As a consequence, the response of the VIX smile to SPX perturbations is not
determined by the model itself. To generate realistic risk sensitivities it is
therefore necessary to introduce an empirical rule describing how VIX implied
volatility moves when the underlying market changes.

In equity volatility markets an analogous phenomenon occurs for SPX options,
where practitioners often model the movement of the implied volatility smile
using the Skew Stickiness Ratio (SSR). The SSR describes how the skew of the
volatility smile shifts relative to movements of the underlying spot. Empirical
studies suggest that similar behavior is present in VIX options: changes in the
VIX future level are typically accompanied by systematic changes in the slope
and level of the VIX volatility smile.

Motivated by this empirical observation, we incorporate VIX Skew Stickiness Ratio
dynamics into the perturbed optimal transport problem. The idea is to treat the
SSR relation as an exogenous constraint that governs how the VIX smile adjusts
when the SPX surface is perturbed. In practice, a perturbation of the SPX
surface modifies the SPX marginal distributions, which induces a change in the
VIX forward level through the forward variance relationship. The SSR rule then
determines how the VIX implied volatility levels adjust in response to this
shift.

By embedding these SSR constraints into the entropic projection, the perturbed
optimal transport problem simultaneously enforces consistency with the SPX
surface, the VIX future level, and the empirically observed VIX smile dynamics.
This provides a natural mechanism for generating realistic SPX–VIX risk
sensitivities within the optimal transport framework.

### 6.4 Empirical Evidence For VIX Skew Stickiness Ratio

Skew Stickiness Ratio (SSR) is widely used by practitioners to describe how the VIX
volatility smile responds to changes in the underlying SPX level.

To estimate SSR empirically we regress daily changes in VIX implied volatility
against changes in the VIX future level across different maturities.
Figures [1](#S6.F1 "Figure 1 ‣ 6.4 Empirical Evidence For VIX Skew Stickiness Ratio ‣ 6 SSR Dynamics For VIX And Its Linearization ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport") illustrate the estimated SSR term
structure using historical windows of six months and one year.

![Refer to caption](2603.10857v1/x1.png)


(a) 6m window

![Refer to caption](2603.10857v1/x2.png)


(b) 1y window

![Refer to caption](2603.10857v1/x3.png)


(c) 2y window

![Refer to caption](2603.10857v1/x4.png)


(d) 3y window

Figure 1: Estimated VIX SSR term structure across four historical windows.

These empirical observations motivate incorporating SSR dynamics into the
optimal transport framework as exogenous constraints.

### 6.5 Compatibility With The Optimal Transport Linear Response System

We now show that the SSR perturbation rule integrates naturally into the
linear-response framework derived for entropic martingale optimal transport.

Let FVF\_{V} denote the VIX future level implied by the calibrated coupling
μ⋆\mu^{\star} and let δ​FV\delta F\_{V} denote the change induced by a perturbation
of the SPX marginal distribution.

Under the SSR dynamics derived above, the corresponding change in VIX
implied volatility is

|  |  |  |
| --- | --- | --- |
|  | δ​σV​(K)=−SSRV⋅SkewV​(FV)​δ​FV.\delta\sigma\_{V}(K)=-\text{SSR}\_{V}\cdot\text{Skew}\_{V}(F\_{V})\,\delta F\_{V}. |  |

Using the first-order Taylor expansion of VIX option prices,

|  |  |  |
| --- | --- | --- |
|  | δ​CVK=ΔVK​δ​FV+VegaVK​δ​σV​(K),\delta C\_{V}^{K}=\Delta\_{V}^{K}\delta F\_{V}+\text{Vega}\_{V}^{K}\delta\sigma\_{V}(K), |  |

we obtain

|  |  |  |
| --- | --- | --- |
|  | δ​CVK=(ΔVK−VegaVK​SSRV​SkewV​(FV))​δ​FV.\delta C\_{V}^{K}=\left(\Delta\_{V}^{K}-\text{Vega}\_{V}^{K}\text{SSR}\_{V}\text{Skew}\_{V}(F\_{V})\right)\delta F\_{V}. |  |

Therefore the SSR dynamics define a linear mapping between the SPX perturbation and the VIX option constraints.

In the optimal transport perturbation framework this mapping corresponds to an additional linear constraint of the form

|  |  |  |
| --- | --- | --- |
|  | ΦK​(μ)=bK+b˙K\Phi\_{K}(\mu)=b\_{K}+\dot{b}\_{K} |  |

where the perturbation term b˙K\dot{b}\_{K} is determined by the SSR relation above.

Consequently the SSR dynamics enter the linear response system derived in
Section 3 through an augmented perturbation vector

|  |  |  |
| --- | --- | --- |
|  | h=(h1,h2,b˙K).h=(h\_{1},h\_{2},\dot{b}\_{K}). |  |

The resulting sensitivity formula

|  |  |  |
| --- | --- | --- |
|  | Π′​(0)=g⊤​H−1​h\Pi^{\prime}(0)=g^{\top}H^{-1}h |  |

remains valid with the augmented constraint vector.

## 7 Algorithm For SPX–VIX Risk Without Recalibration

### 7.1 Base Calibration

We first compute a base joint coupling between the SPX state S1S\_{1}, the VIX variable VV, and the future SPX state S2S\_{2}.
The goal of this calibration step is to construct a probability measure

|  |  |  |
| --- | --- | --- |
|  | μ​(s1,v,s2)\mu(s\_{1},v,s\_{2}) |  |

that matches the prescribed SPX and VIX marginals while simultaneously enforcing the key financial consistency conditions linking SPX and VIX dynamics.

Specifically, the calibrated coupling must satisfy:

* •

  the marginal constraints

  |  |  |  |
  | --- | --- | --- |
  |  | M1​μ=μ1,MV​μ=μV,M2​μ=μ2,M\_{1}\mu=\mu\_{1},\qquad M\_{V}\mu=\mu\_{V},\qquad M\_{2}\mu=\mu\_{2}, |  |

  corresponding to the SPX spot, VIX, and future SPX marginals implied by market prices;
* •

  the martingale condition

  |  |  |  |
  | --- | --- | --- |
  |  | 𝔼​[S2∣S1,V]=S1,\mathbb{E}[S\_{2}\mid S\_{1},V]=S\_{1}, |  |
* •

  the SPX–VIX variance consistency condition

  |  |  |  |
  | --- | --- | --- |
  |  | 𝔼​[L​(S2/S1)∣S1,V]=V2,\mathbb{E}[L(S\_{2}/S\_{1})\mid S\_{1},V]=V^{2}, |  |

  which links the VIX level to the expected forward variance of the SPX.

Numerically, we solve this constrained calibration problem using a nested scheme.
An outer Sinkhorn iteration enforces the marginal constraints via multiplicative scaling factors, while an inner Newton (or damped Newton) correction enforces the conditional martingale and variance-consistency conditions at each (S1,V)(S\_{1},V) node.

This structure closely follows the constrained calibration framework introduced in the SPX–VIX joint calibration methodology of  Guyon ([2020](#bib.bib35 "The joint S&P 500/VIX smile calibration puzzle solved")), where optimal transport techniques are combined with financial consistency constraints to produce arbitrage-consistent joint distributions.

The resulting calibrated coupling μ⋆\mu^{\star} serves as the base distribution for the subsequent perturbation and risk-generation procedures described in the following sections.

Algorithm 1: Base Calibration Via Sinkhorn With Newton/LM Enforcement

1. 1.

   Inputs. Discrete grids 𝒮1,𝒱,𝒮2\mathcal{S}\_{1},\mathcal{V},\mathcal{S}\_{2}; target marginals μ1,μV,μ2\mu\_{1},\mu\_{V},\mu\_{2};
   prior μ¯​(s1,v,s2)\bar{\mu}(s\_{1},v,s\_{2}); log-return functional L​(⋅)L(\cdot); marginal tolerance εmarg\varepsilon\_{\mathrm{marg}};
   financial tolerance εfin\varepsilon\_{\mathrm{fin}}; Newton damping λ≥0\lambda\geq 0.
2. 2.

   Outputs. Calibrated coupling μ⋆​(s1,v,s2)\mu^{\star}(s\_{1},v,s\_{2}) and Fisher information matrix HH.
3. 3.

   Initialize.

   |  |  |  |
   | --- | --- | --- |
   |  | a​(s1)←1,b​(v)←1,c​(s2)←1,ΔM​(s1,v)←0,ΔC​(s1,v)←0.a(s\_{1})\leftarrow 1,\quad b(v)\leftarrow 1,\quad c(s\_{2})\leftarrow 1,\qquad\Delta\_{M}(s\_{1},v)\leftarrow 0,\quad\Delta\_{C}(s\_{1},v)\leftarrow 0. |  |

   Form initial Gibbs coupling

   |  |  |  |
   | --- | --- | --- |
   |  | μ​(s1,v,s2)∝μ¯​(s1,v,s2)​a​(s1)​b​(v)​c​(s2)​exp⁡{ΔM​(s1,v)​(s2−s1)+ΔC​(s1,v)​(L​(s2/s1)−v2)}.\mu(s\_{1},v,s\_{2})\propto\bar{\mu}(s\_{1},v,s\_{2})\,a(s\_{1})b(v)c(s\_{2})\exp\{\Delta\_{M}(s\_{1},v)(s\_{2}-s\_{1})+\Delta\_{C}(s\_{1},v)(L(s\_{2}/s\_{1})-v^{2})\}. |  |
4. 4.

   Outer loop: repeat until marginal errors ≤εmarg\leq\varepsilon\_{\mathrm{marg}} and financial residuals ≤εfin\leq\varepsilon\_{\mathrm{fin}}:

   1. (a)

      Sinkhorn marginal updates: for all grid points update

      |  |  |  |
      | --- | --- | --- |
      |  | a​(s1)←μ1​(s1)∑v,s2μ¯​(s1,v,s2)​b​(v)​c​(s2)​eΔM​(s1,v)​(s2−s1)+ΔC​(s1,v)​(L​(s2/s1)−v2),a(s\_{1})\leftarrow\frac{\mu\_{1}(s\_{1})}{\sum\_{v,s\_{2}}\bar{\mu}(s\_{1},v,s\_{2})\,b(v)c(s\_{2})\,e^{\Delta\_{M}(s\_{1},v)(s\_{2}-s\_{1})+\Delta\_{C}(s\_{1},v)(L(s\_{2}/s\_{1})-v^{2})}}, |  |

      |  |  |  |
      | --- | --- | --- |
      |  | b​(v)←μV​(v)∑s1,s2μ¯​(s1,v,s2)​a​(s1)​c​(s2)​eΔM​(s1,v)​(s2−s1)+ΔC​(s1,v)​(L​(s2/s1)−v2),b(v)\leftarrow\frac{\mu\_{V}(v)}{\sum\_{s\_{1},s\_{2}}\bar{\mu}(s\_{1},v,s\_{2})\,a(s\_{1})c(s\_{2})\,e^{\Delta\_{M}(s\_{1},v)(s\_{2}-s\_{1})+\Delta\_{C}(s\_{1},v)(L(s\_{2}/s\_{1})-v^{2})}}, |  |

      |  |  |  |
      | --- | --- | --- |
      |  | c​(s2)←μ2​(s2)∑s1,vμ¯​(s1,v,s2)​a​(s1)​b​(v)​eΔM​(s1,v)​(s2−s1)+ΔC​(s1,v)​(L​(s2/s1)−v2).c(s\_{2})\leftarrow\frac{\mu\_{2}(s\_{2})}{\sum\_{s\_{1},v}\bar{\mu}(s\_{1},v,s\_{2})\,a(s\_{1})b(v)\,e^{\Delta\_{M}(s\_{1},v)(s\_{2}-s\_{1})+\Delta\_{C}(s\_{1},v)(L(s\_{2}/s\_{1})-v^{2})}}. |  |

      Refresh μ​(s1,v,s2)\mu(s\_{1},v,s\_{2}) using the Gibbs map above.
   2. (b)

      Conditional Newton/LM enforcement: for each (s1,v)∈𝒮1×𝒱(s\_{1},v)\in\mathcal{S}\_{1}\times\mathcal{V} do

      1. i.

         repeat up to inner iterations:

         |  |  |  |
         | --- | --- | --- |
         |  | ws1,v​(s2)=μ​(s1,v,s2)∑u∈𝒮2μ​(s1,v,u)w\_{s\_{1},v}(s\_{2})\;=\;\frac{\mu(s\_{1},v,s\_{2})}{\sum\_{u\in\mathcal{S}\_{2}}\mu(s\_{1},v,u)} |  |

         (conditional law over s2s\_{2}),
         residuals

         |  |  |  |
         | --- | --- | --- |
         |  | rM​(s1,v)=∑s2ws1,v​(s2)​(s2−s1),rC​(s1,v)=∑s2ws1,v​(s2)​(L​(s2/s1)−v2),r\_{M}(s\_{1},v)=\sum\_{s\_{2}}w\_{s\_{1},v}(s\_{2})(s\_{2}-s\_{1}),\qquad r\_{C}(s\_{1},v)=\sum\_{s\_{2}}w\_{s\_{1},v}(s\_{2})\bigl(L(s\_{2}/s\_{1})-v^{2}\bigr), |  |

         Jacobian entries

         |  |  |  |
         | --- | --- | --- |
         |  | J11=Varw⁡(s2−s1),J22=Varw⁡(L​(s2/s1)−v2),J\_{11}=\operatorname{Var}\_{w}(s\_{2}-s\_{1}),\quad J\_{22}=\operatorname{Var}\_{w}\bigl(L(s\_{2}/s\_{1})-v^{2}\bigr), |  |

         |  |  |  |
         | --- | --- | --- |
         |  | J12=J21=Covw⁡(s2−s1,L​(s2/s1)−v2),J\_{12}=J\_{21}=\operatorname{Cov}\_{w}\bigl(s\_{2}-s\_{1},\;L(s\_{2}/s\_{1})-v^{2}\bigr), |  |

         solve damped Newton system

         |  |  |  |
         | --- | --- | --- |
         |  | (J11+λJ12J21J22+λ)​(δMδC)=−(rMrC),\begin{pmatrix}J\_{11}+\lambda&J\_{12}\\[4.0pt] J\_{21}&J\_{22}+\lambda\end{pmatrix}\begin{pmatrix}\delta\_{M}\\[2.0pt] \delta\_{C}\end{pmatrix}=-\begin{pmatrix}r\_{M}\\[2.0pt] r\_{C}\end{pmatrix}, |  |

         update multipliers

         |  |  |  |
         | --- | --- | --- |
         |  | ΔM​(s1,v)←ΔM​(s1,v)+δM,ΔC​(s1,v)←ΔC​(s1,v)+δC,\Delta\_{M}(s\_{1},v)\leftarrow\Delta\_{M}(s\_{1},v)+\delta\_{M},\qquad\Delta\_{C}(s\_{1},v)\leftarrow\Delta\_{C}(s\_{1},v)+\delta\_{C}, |  |

         refresh μ​(s1,v,s2)\mu(s\_{1},v,s\_{2}).
      2. ii.

         until rM​(s1,v)2+rC​(s1,v)2≤εfin\sqrt{r\_{M}(s\_{1},v)^{2}+r\_{C}(s\_{1},v)^{2}}\leq\varepsilon\_{\mathrm{fin}} or inner cap reached.
5. 5.

   On convergence set μ⋆←μ\mu^{\star}\leftarrow\mu.
6. 6.

   Fisher information. With sufficient statistics Ti​(x)T\_{i}(x) compute

   |  |  |  |
   | --- | --- | --- |
   |  | Hi​j=∑xμ⋆​(x)​(Ti​(x)−𝔼μ⋆​[Ti])​(Tj​(x)−𝔼μ⋆​[Tj]),x=(s1,v,s2).H\_{ij}=\sum\_{x}\mu^{\star}(x)\bigl(T\_{i}(x)-\mathbb{E}\_{\mu^{\star}}[T\_{i}]\bigr)\bigl(T\_{j}(x)-\mathbb{E}\_{\mu^{\star}}[T\_{j}]\bigr),\quad x=(s\_{1},v,s\_{2}). |  |
7. 7.

   Return: μ⋆,H\mu^{\star},H.

### 7.2 POT Risk Computation: The Linear Response(LR) Approach

We compute first–order (Gateaux) price sensitivities under small marginal or constraint perturbations using the Fisher information matrix from the calibrated exponential family. Let μ⋆\mu^{\star} denote the calibrated coupling and HH the Fisher matrix; let hh be the stacked perturbation vector of marginal and constraint shocks. The perturbation vector hh introduced above represents the first-order change in the calibration constraints.
As discussed in Section 6.5, the constraint system is augmented to incorporate the SSR dynamics as additional linear relations linking SPX and VIX perturbations.
Consequently, the perturbation vector hh is not arbitrary but belongs to the augmented constraint space defined in Section 6.5.

In addition, the calibrated coupling μ⋆\mu^{\star} satisfies the financial consistency constraints

|  |  |  |
| --- | --- | --- |
|  | Afin​μ⋆=0.A\_{\mathrm{fin}}\mu^{\star}=0. |  |

To preserve these constraints to first order under a perturbation

|  |  |  |
| --- | --- | --- |
|  | με=μ⋆+ε​δ​μ+o​(ε),\mu^{\varepsilon}=\mu^{\star}+\varepsilon\,\delta\mu+o(\varepsilon), |  |

the admissible perturbation directions must satisfy

|  |  |  |
| --- | --- | --- |
|  | Afin​δ​μ=0.A\_{\mathrm{fin}}\delta\mu=0. |  |

Equivalently, the perturbation vector hh must lie in the tangent space

|  |  |  |
| --- | --- | --- |
|  | h∈ker⁡(Afin).h\in\ker(A\_{\mathrm{fin}}). |  |

In practice, the perturbation vector constructed from the augmented SSR constraint system of Section 6.5 is projected onto this admissible subspace before the Fisher-information risk formula is applied.
Thus the Fisher-based sensitivities are computed along perturbation directions that preserve the martingale and SPX–VIX consistency conditions to first order.

Let the payoff be G:X→ℝG:X\to\mathbb{R} with price Π​(ε)=𝔼με​[G]\Pi(\varepsilon)=\mathbb{E}\_{\mu\_{\varepsilon}}[G] and baseline Π​(0)=𝔼μ⋆​[G]\Pi(0)=\mathbb{E}\_{\mu^{\star}}[G]. The first–order risk is

|  |  |  |
| --- | --- | --- |
|  | Π′​(0)=g⊤​θ˙,\Pi^{\prime}(0)\;=\;g^{\top}\dot{\theta}, |  |

where θ˙\dot{\theta} solves the linear response system H​θ˙=hH\,\dot{\theta}=h, and gg is the covariance vector of GG with the sufficient statistics.

##### Inputs.

Calibrated coupling μ⋆\mu^{\star}; Fisher matrix HH; perturbation vector hh (stacked in the same coordinate system as HH); payoff G​(x)G(x); optional damping λ≥0\lambda\geq 0 and solver tolerances.

##### Outputs.

First–order risk Π′​(0)\Pi^{\prime}(0); optionally the dual variation θ˙\dot{\theta} (for greeks mapping).

Algorithm 2: Linear Response(LR) Risk Computation.

1. 1.

   Solve the linear response system.
   Compute the dual variation by solving

   |  |  |  |
   | --- | --- | --- |
   |  | (H+λ​I)​θ˙=h,(H+\lambda I)\,\dot{\theta}\;=\;h, |  |

   with λ=0\lambda=0 for pure Newton or small λ>0\lambda>0 for Levenberg–Marquardt damping if HH is ill–conditioned. Use the same gauge as in calibration (e.g., fix one potential or project to the gauge–fixed subspace).
2. 2.

   Compute the covariance vector gg.
   Let {Ti}\{T\_{i}\} be the sufficient statistics (coordinates of the dual potentials). Compute

   |  |  |  |
   | --- | --- | --- |
   |  | gi=∑x∈Xμ⋆​(x)​(G​(x)−𝔼μ⋆​[G])​(Ti​(x)−𝔼μ⋆​[Ti]),i=1,…,dim(θ).g\_{i}\;=\;\sum\_{x\in X}\mu^{\star}(x)\,\Big(G(x)-\mathbb{E}\_{\mu^{\star}}[G]\Big)\,\Big(T\_{i}(x)-\mathbb{E}\_{\mu^{\star}}[T\_{i}]\Big),\qquad i=1,\dots,\dim(\theta). |  |
3. 3.

   Evaluate first–order risk.

   |  |  |  |
   | --- | --- | --- |
   |  | Π′​(0)=g⊤​θ˙.\Pi^{\prime}(0)\;=\;g^{\top}\dot{\theta}. |  |

   Return Π′​(0)\Pi^{\prime}(0) (and θ˙\dot{\theta} if needed for greeks attribution).

##### Notes.

* •

  For augmented constraint sets (e.g., SSR–adjusted VIX constraints), HH and hh are augmented accordingly; the same steps apply with the enlarged system.
* •

  The covariance step can be reused across multiple payoffs once μ⋆\mu^{\star} and {Ti}\{T\_{i}\} are fixed; only gg changes with GG.

## 8 Dimensional Reduction(DR) For POT

An alternative to computing first-order sensitivities via the Fisher information is to exploit the conditional
coupling invariance directly and re-solve a reduced entropic projection on (S1,V)(S\_{1},V). Under a conditional kernel invariance assumption, the perturbed three-dimensional problem is equivalent to a two-dimensional entropic projection for
γ\gamma on (S1,V)(S\_{1},V), so one may obtain the exact perturbed coupling in the reduced class by solving a
Sinkhorn-type projection that matches the perturbed VIX marginal implied by the SSR propagation of the SPX shock, while remaining close in entropy to the base reduced coupling.
This reduced-OT approach retains convexity and numerical stability and unlike the Fisher linearization—
captures nonlinear effects for finite (non-infinitesimal) shocks insofar as the dimension reduction assumption remains numerically accurate. Surprisingly, even though the reduced OT recipe involves a mini-recalibration, the algorithm takes only 5-6 steps to converge, hence is computationally efficient.

### 8.1 Base Conditional Structure

Let μ⋆∈Δ​(𝒳)\mu^{\star}\in\Delta(\mathcal{X}) denote the calibrated optimal coupling,
where

|  |  |  |
| --- | --- | --- |
|  | 𝒳=𝒮1×𝒱×𝒮2.\mathcal{X}=\mathcal{S}\_{1}\times\mathcal{V}\times\mathcal{S}\_{2}. |  |

Define the marginal of μ⋆\mu^{\star} over (S1,V)(S\_{1},V):

|  |  |  |
| --- | --- | --- |
|  | μ1,V⋆​(s1,v)=∑s2∈𝒮2μ⋆​(s1,v,s2).\mu^{\star}\_{1,V}(s\_{1},v)=\sum\_{s\_{2}\in\mathcal{S}\_{2}}\mu^{\star}(s\_{1},v,s\_{2}). |  |

Define the conditional kernel of S2S\_{2} given (S1,V)(S\_{1},V):

|  |  |  |
| --- | --- | --- |
|  | κ∗​(s2∣s1,v)=μ⋆​(s1,v,s2)μ1,V⋆​(s1,v).\kappa^{\*}(s\_{2}\mid s\_{1},v)=\frac{\mu^{\star}(s\_{1},v,s\_{2})}{\mu^{\star}\_{1,V}(s\_{1},v)}. |  |

Then the coupling admits the disintegration:

|  |  |  |
| --- | --- | --- |
|  | μ⋆​(s1,v,s2)=κ∗​(s2∣s1,v)​μ1,V⋆​(s1,v).\mu^{\star}(s\_{1},v,s\_{2})=\kappa^{\*}(s\_{2}\mid s\_{1},v)\,\mu^{\star}\_{1,V}(s\_{1},v). |  |

### 8.2 Conditional Coupling Invariance Assumption

###### Assumption 8.1 (Conditional Coupling Invariance).

Under sufficiently small perturbations of the SPX marginals,
the conditional distribution of S2S\_{2} given (S1,V)(S\_{1},V) remains unchanged, i.e.,

|  |  |  |
| --- | --- | --- |
|  | κε​(s2∣s1,v)=κ∗​(s2∣s1,v)for all ​(s1,v,s2).\kappa^{\varepsilon}(s\_{2}\mid s\_{1},v)=\kappa^{\*}(s\_{2}\mid s\_{1},v)\quad\text{for all }(s\_{1},v,s\_{2}). |  |

This assumption reflects that the structural dependence
between S2S\_{2} and (S1,V)(S\_{1},V) is stable under small marginal shocks.

### 8.3 Exact Dimensional Reduction

###### Theorem 8.2 (Exact Reduction to Two-Dimensional Entropic Projection).

Assume μ⋆\mu^{\star} is strictly positive on 𝒳\mathcal{X}
and Assumption [8.1](#S8.Thmtheorem1 "Assumption 8.1 (Conditional Coupling Invariance). ‣ 8.2 Conditional Coupling Invariance Assumption ‣ 8 Dimensional Reduction(DR) For POT ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport") holds.

Then the perturbed entropic projection problem

|  |  |  |
| --- | --- | --- |
|  | infμ∈𝒫εD​(μ∥μ⋆)\inf\_{\mu\in\mathcal{P}^{\varepsilon}}D(\mu\,\|\,\mu^{\star}) |  |

reduces exactly to the two-dimensional problem

|  |  |  |
| --- | --- | --- |
|  | infν∈𝒬εD​(ν∥μ1,V⋆),\inf\_{\nu\in\mathcal{Q}^{\varepsilon}}D(\nu\,\|\,\mu^{\star}\_{1,V}), |  |

where ν\nu is a probability measure on
𝒮1×𝒱\mathcal{S}\_{1}\times\mathcal{V} satisfying the perturbed marginal constraints,
and the full three-dimensional coupling is reconstructed by

|  |  |  |
| --- | --- | --- |
|  | με​(s1,v,s2)=κ∗​(s2∣s1,v)​νε​(s1,v).\mu^{\varepsilon}(s\_{1},v,s\_{2})=\kappa^{\*}(s\_{2}\mid s\_{1},v)\,\nu^{\varepsilon}(s\_{1},v). |  |

###### Proof.

Under Assumption [8.1](#S8.Thmtheorem1 "Assumption 8.1 (Conditional Coupling Invariance). ‣ 8.2 Conditional Coupling Invariance Assumption ‣ 8 Dimensional Reduction(DR) For POT ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport"),
any admissible perturbed coupling με\mu^{\varepsilon} must satisfy

|  |  |  |
| --- | --- | --- |
|  | με​(s1,v,s2)=κ∗​(s2∣s1,v)​ν​(s1,v)\mu^{\varepsilon}(s\_{1},v,s\_{2})=\kappa^{\*}(s\_{2}\mid s\_{1},v)\,\nu(s\_{1},v) |  |

for some probability measure ν\nu on 𝒮1×𝒱\mathcal{S}\_{1}\times\mathcal{V}.

Substitute this representation into the relative entropy:

|  |  |  |
| --- | --- | --- |
|  | D​(με∥μ⋆)=∑s1,v,s2με​(s1,v,s2)​ln⁡με​(s1,v,s2)μ⋆​(s1,v,s2).D(\mu^{\varepsilon}\,\|\,\mu^{\star})=\sum\_{s\_{1},v,s\_{2}}\mu^{\varepsilon}(s\_{1},v,s\_{2})\ln\frac{\mu^{\varepsilon}(s\_{1},v,s\_{2})}{\mu^{\star}(s\_{1},v,s\_{2})}. |  |

Using the disintegration formulas for με\mu^{\varepsilon} and μ⋆\mu^{\star}:

|  |  |  |
| --- | --- | --- |
|  | =∑s1,v,s2κ∗​(s2∣s1,v)​ν​(s1,v)​ln⁡κ∗​(s2∣s1,v)​ν​(s1,v)κ∗​(s2∣s1,v)​μ1,V⋆​(s1,v).=\sum\_{s\_{1},v,s\_{2}}\kappa^{\*}(s\_{2}\mid s\_{1},v)\,\nu(s\_{1},v)\ln\frac{\kappa^{\*}(s\_{2}\mid s\_{1},v)\,\nu(s\_{1},v)}{\kappa^{\*}(s\_{2}\mid s\_{1},v)\,\mu^{\star}\_{1,V}(s\_{1},v)}. |  |

Canceling κ∗​(s2∣s1,v)\kappa^{\*}(s\_{2}\mid s\_{1},v) inside the logarithm yields

|  |  |  |
| --- | --- | --- |
|  | =∑s1,v,s2κ∗​(s2∣s1,v)​ν​(s1,v)​ln⁡ν​(s1,v)μ1,V⋆​(s1,v).=\sum\_{s\_{1},v,s\_{2}}\kappa^{\*}(s\_{2}\mid s\_{1},v)\,\nu(s\_{1},v)\ln\frac{\nu(s\_{1},v)}{\mu^{\star}\_{1,V}(s\_{1},v)}. |  |

Since for each (s1,v)(s\_{1},v),

|  |  |  |
| --- | --- | --- |
|  | ∑s2κ∗​(s2∣s1,v)=1,\sum\_{s\_{2}}\kappa^{\*}(s\_{2}\mid s\_{1},v)=1, |  |

we obtain

|  |  |  |
| --- | --- | --- |
|  | D​(με∥μ⋆)=∑s1,vν​(s1,v)​ln⁡ν​(s1,v)μ1,V⋆​(s1,v)=D​(ν∥μ1,V⋆).D(\mu^{\varepsilon}\,\|\,\mu^{\star})=\sum\_{s\_{1},v}\nu(s\_{1},v)\ln\frac{\nu(s\_{1},v)}{\mu^{\star}\_{1,V}(s\_{1},v)}=D(\nu\,\|\,\mu^{\star}\_{1,V}). |  |

Thus the three-dimensional projection problem
is equivalent to the two-dimensional entropic projection.

The perturbed marginal constraints
reduce correspondingly to constraints on ν\nu,
and the reconstructed coupling satisfies the reduced constraints and preserves the conditional martingale and variance-consistency relations inherited from the base calibration.
∎

The reduction follows from the disintegration of the base coupling

|  |  |  |
| --- | --- | --- |
|  | μ⋆​(s1,v,s2)=μ⋆​(s2|s1,v)​μ⋆​(s1,v).\mu^{\star}(s\_{1},v,s\_{2})=\mu^{\star}(s\_{2}|s\_{1},v)\mu^{\star}(s\_{1},v). |  |

Fixing the conditional kernel and perturbing only the marginal
distribution on (S1,V)(S\_{1},V) preserves both the martingale and variance
consistency constraints, which depend only on conditional expectations
of S2S\_{2} given (S1,V)(S\_{1},V).

##### Computational implication.

The dimensional reduction has an important algorithmic consequence for risk
generation.

In the base calibration, the entropic martingale optimal transport problem
must enforce the martingale constraint

|  |  |  |
| --- | --- | --- |
|  | E​[S2|S1,V]=S1,E[S\_{2}|S\_{1},V]=S\_{1}, |  |

which couples the (S1,V,S2)(S\_{1},V,S\_{2}) variables and requires solving the full
three–dimensional Sinkhorn calibration.

In contrast, under the conditional coupling invariance assumption the
perturbed distribution takes the form

|  |  |  |
| --- | --- | --- |
|  | με​(s1,v,s2)=κ∗​(s2|s1,v)​νε​(s1,v),\mu\_{\varepsilon}(s\_{1},v,s\_{2})=\kappa^{\*}(s\_{2}|s\_{1},v)\,\nu\_{\varepsilon}(s\_{1},v), |  |

so that the martingale and variance constraints remain automatically
satisfied by the fixed conditional kernel κ∗\kappa^{\*}.

As a result the perturbed optimal transport problem reduces to a
two–dimensional entropic projection for νε​(s1,v)\nu\_{\varepsilon}(s\_{1},v).
Operationally this amounts to running a Sinkhorn-type projection
*without re-imposing the martingale constraint*.

This is the key reason why the proposed risk generation method is
computationally efficient: the perturbed problem no longer requires
recalibration of the full martingale optimal transport model.
In practice the perturbed projection typically converges in only a few
Sinkhorn iterations because the solution is close to the base coupling.

### 8.4 SPX–VIX Family Risk Generation: The Dimensional Reduction(DR) Approach

We now describe the practical algorithm used to compute SPX–VIX risk
sensitivities under SSR while preserving the structure of the calibrated
joint coupling.

Let

|  |  |  |
| --- | --- | --- |
|  | μ⋆​(s1,v,s2)\mu^{\star}(s\_{1},v,s\_{2}) |  |

denote the base calibrated joint coupling obtained from the SPX–VIX
martingale optimal transport problem in
Section [7.1](#S7.SS1 "7.1 Base Calibration ‣ 7 Algorithm For SPX–VIX Risk Without Recalibration ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport"). By construction, μ⋆\mu^{\star}
satisfies the SPX market constraints, the VIX market constraints,
the martingale condition, and the SPX–VIX consistency condition.

The key point is that, in the risk calculation considered here,
the perturbation is not generated by directly changing the SPX marginal
inside the transport problem. Rather, one starts from an exogenous SPX
market perturbation (for example, a spot bump or an SPX volatility bump),
propagates this perturbation through the SSR dynamics, and obtains the
corresponding change in VIX option prices. These perturbed VIX option
prices determine a new admissible VIX marginal constraint, and hence a
new perturbed optimal transport problem.

A full recalibration of the joint coupling would be computationally
expensive. Instead, we exploit the dimension reduction result of
Section [8](#S8 "8 Dimensional Reduction(DR) For POT ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport"), according to which the perturbation
can be carried out at the level of the lower-dimensional coupling in
(S1,V)(S\_{1},V) while leaving the conditional kernel of S2S\_{2} given (S1,V)(S\_{1},V)
unchanged.

More precisely, write the base calibrated coupling in disintegrated form as

|  |  |  |
| --- | --- | --- |
|  | μ⋆​(s1,v,s2)=γ⋆​(s1,v)​κ⋆​(d​s2∣s1,v),\mu^{\star}(s\_{1},v,s\_{2})=\gamma^{\star}(s\_{1},v)\,\kappa^{\star}(ds\_{2}\mid s\_{1},v), |  |

where

|  |  |  |
| --- | --- | --- |
|  | γ⋆​(s1,v)\gamma^{\star}(s\_{1},v) |  |

is the marginal coupling of (S1,V)(S\_{1},V) and

|  |  |  |
| --- | --- | --- |
|  | κ⋆​(d​s2∣s1,v)\kappa^{\star}(ds\_{2}\mid s\_{1},v) |  |

is the conditional kernel of S2S\_{2} given (S1,V)(S\_{1},V).
The dimension reduction theorem implies that the perturbed coupling may be
constructed as

|  |  |  |
| --- | --- | --- |
|  | με​(s1,v,s2)=γε​(s1,v)​κ⋆​(d​s2∣s1,v),\mu\_{\varepsilon}(s\_{1},v,s\_{2})=\gamma\_{\varepsilon}(s\_{1},v)\,\kappa^{\star}(ds\_{2}\mid s\_{1},v), |  |

that is, only γε\gamma\_{\varepsilon} is updated from the base reduced coupling γ⋆\gamma^{\star}, while the
conditional kernel κ⋆\kappa^{\star} is kept fixed.

The VIX marginal is therefore free to adjust through the perturbation of
γ⋆​(s1,v)\gamma^{\star}(s\_{1},v), whereas the conditional dependence structure of
S2S\_{2} given (S1,V)(S\_{1},V) remains inherited from the base calibration.

Algorithm 3: SSR-Enhanced Dimensional Reduction(DR) For POT Risk Generation

1. 1.

   Inputs.

   * •

     Base joint coupling μ⋆​(s1,v,s2)\mu^{\star}(s\_{1},v,s\_{2}) and relevant marginals from Algorithm 1
   * •

     Exogenous SPX perturbation (e.g., spot bump or volatility surface shift)
   * •

     SSR (Skew Stickiness Ratio) parameters for VIX volatility dynamics
   * •

     Observed SPX and VIX market data
2. 2.

   Outputs.

   * •

     Updated perturbed coupling με​(s1,v,s2)\mu\_{\varepsilon}(s\_{1},v,s\_{2})
   * •

     Risk sensitivities under με\mu\_{\varepsilon}
3. 3.

   Base Calibration.

   1. (a)

      Disintegrate μ⋆\mu^{\star} as

      |  |  |  |
      | --- | --- | --- |
      |  | μ⋆​(s1,v,s2)=γ⋆​(s1,v)​κ⋆​(s2∣s1,v),\mu^{\star}(s\_{1},v,s\_{2})=\gamma^{\star}(s\_{1},v)\,\kappa^{\star}(s\_{2}\mid s\_{1},v), |  |

      where γ⋆\gamma^{\star} is the (S1,V)(S\_{1},V) marginal and κ⋆\kappa^{\star} is the conditional kernel.
4. 4.

   Generate exogenous SPX perturbation.

   1. (a)

      Apply the prescribed SPX perturbation (e.g., spot or implied volatility shift) to obtain the new SPX marginal and updated SPX implied forward variance FV′F\_{V}^{\prime}.
5. 5.

   Propagate VIX smile using SSR.

   1. (a)

      Use the SSR rule as in Theorem [6.1](#S6.Thmtheorem1 "Theorem 6.1 (Unified linear SSR expansion with second–order error). ‣ 6.2 Linear SSR Approximation And Second–Order Accuracy ‣ 6 SSR Dynamics For VIX And Its Linearization ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport") to compute a synthetic perturbed VIX implied volatility surface:

      |  |  |  |
      | --- | --- | --- |
      |  | σVIX′​(K)=σVIX​(K)−S​S​R⋅∂σVIX∂K|K=FV⋅Δ​FV.\sigma^{\prime}\_{\mathrm{VIX}}(K)=\sigma\_{\mathrm{VIX}}(K)-SSR\cdot\left.\frac{\partial\sigma\_{\mathrm{VIX}}}{\partial K}\right|\_{K=F\_{V}}\cdot\Delta F\_{V}. |  |
   2. (b)

      Compute the corresponding perturbed VIX option prices from the shifted surface.
6. 6.

   Construct perturbed VIX marginal.

   1. (a)

      Infer the new VIX marginal distribution so that, under the VIX variable, the model reproduces the SSR-propagated VIX option prices.
7. 7.

   Dimension-reduced entropic transport update.

   1. (a)

      Holding κ⋆​(s2∣s1,v)\kappa^{\star}(s\_{2}\mid s\_{1},v) fixed, solve for the updated (S1,V)(S\_{1},V) coupling γε​(s1,v)\gamma\_{\varepsilon}(s\_{1},v) that matches the perturbed VIX marginals implied by the SSR propagation of the SPX shock and remains closest in relative entropy to the base reduced coupling γ⋆​(s1,v)\gamma^{\star}(s\_{1},v).
   2. (b)

      Reconstruct the full perturbed joint coupling as

      |  |  |  |
      | --- | --- | --- |
      |  | με​(s1,v,s2)=γε​(s1,v)​κ⋆​(s2∣s1,v).\mu\_{\varepsilon}(s\_{1},v,s\_{2})=\gamma\_{\varepsilon}(s\_{1},v)\,\kappa^{\star}(s\_{2}\mid s\_{1},v). |  |
8. 8.

   Risk extraction.

   1. (a)

      For any payoff function GG, compute model prices under μ⋆\mu^{\star} and με\mu\_{\varepsilon}, and report the sensitivity as

      |  |  |  |
      | --- | --- | --- |
      |  | Greek≈P​(με)−P​(μ⋆)ε,\text{Greek}\approx\frac{P(\mu\_{\varepsilon})-P(\mu^{\star})}{\varepsilon}, |  |

      where P​(μ)P(\mu) denotes the portfolio valuation under μ\mu.

This procedure avoids a full recalibration of the original SPX–VIX
martingale optimal transport problem. The perturbation is carried only
by the reduced coupling in (S1,V)(S\_{1},V), while the conditional kernel of
S2S\_{2} given (S1,V)(S\_{1},V) remains unchanged. In this way, the endogenous
adjustment of the VIX marginal is captured through the perturbed reduced
coupling, yielding a fast and structurally consistent risk-generation
algorithm.

## 9 Experiments: SPX-VIX Risk Generation And Hedging Backtest

### 9.1 SPX–VIX Basis In Market Data

In theory the VIX future level should be consistent with the forward variance
implied by the SPX option surface through the well-known replication formula. This is precisely the consistency condition in ([1](#S1.E1 "Equation 1 ‣ SPX–VIX consistency condition ‣ 1.4 Martingality And Consistency Conditions ‣ 1 Introduction ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport")). However, empirical market data shows that this relation does not hold exactly.
In practice a persistent basis exists between the SPX implied forward variance
and the traded VIX futures.

Figure [2](#S9.F2 "Figure 2 ‣ 9.1 SPX–VIX Basis In Market Data ‣ 9 Experiments: SPX-VIX Risk Generation And Hedging Backtest ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport") shows the time series of the SPX–VIX basis for
the 1-month tenor over a two-year window. The presence of this basis is well
documented in practice and is typically attributed to market segmentation,
liquidity effects, and supply–demand imbalances in the VIX futures market.

In our calibration framework we therefore allow a basis adjustment when
linking SPX forward variance and the VIX future level.

![Refer to caption](2603.10857v1/x5.png)


Figure 2: SPX–VIX basis time series for the 1-month tenor over a two-year window.

Despite the presence of this basis, the calibrated optimal transport model
still satisfies the martingality condition and approximate consistency
constraints, which we verify in Section 9.2.

### 9.2 Base Calibration And Fit Quality

We first assess the quality of the base calibration used throughout the experiments. The joint SPX–VIX coupling μ⋆\mu^{\star} is obtained via entropic projection with Sinkhorn scaling on the discrete grids. After calibration, we compute the sufficient statistics and the Fisher information matrix HH for subsequent risk analysis. Existence, uniqueness, and the Gibbs form of the optimizer ensure a consistent fit to the prescribed marginals and targets on the grids.

To visualize fit quality, we plot observed market smiles against model-implied values from the calibrated coupling for a representative maturity (e.g., March 18, 2026, two weeks to expiry), consistent with our option risk comparisons. Additionally, we generate the martingality plot and consistency plot. It is worth pointing out, that the consistency condition which should hold in theory, does not in reality. To this end, in order to make use of the SPX–VIX joint calibration, we must relax the consistency condition and incorporate the basis in both the base calibration and the perturbed calibration.

![Refer to caption](2603.10857v1/x6.png)


(a) SPX T1T\_{1} smile fit

![Refer to caption](2603.10857v1/x7.png)


(b) SPX T2T\_{2} smile fit

Figure 3: SPX smile fit quality (two expiries)

![Refer to caption](2603.10857v1/x8.png)


Figure 4: VIX smile fit: observed vs model-implied



![Refer to caption](2603.10857v1/x9.png)


(a) Martingality check

![Refer to caption](2603.10857v1/x10.png)


(b) Consistency condition

Figure 5: SPX–VIX calibration theoretical conditions

### 9.3 Risk Computation Benchmark: Recalibration vs Perturbation

This section evaluates the accuracy and computational efficiency of the
perturbation framework developed in Sections 3–7. The objective of this experiment is to evaluate the Linear Response (LR) approach within our Perturbed Optimal Transport (POT) framework. We compare risk sensitivities obtained from the LR system (Fisher-information perturbation method) with those obtained from a full recalibration of the SPX–VIX optimal transport model.

The experiment therefore compares two approaches for computing
risk sensitivities under SPX market perturbations.

1. 1.

   Full recalibration (benchmark).
   After applying a perturbation to the SPX market, the entire
   SPX–VIX martingale optimal transport calibration problem
   is recomputed using Algorithm 1.
   The resulting joint distribution
   μrecalε\mu^{\varepsilon}\_{\mathrm{recal}}
   serves as the benchmark distribution for computing option prices
   and sensitivities.
2. 2.

   Perturbation (LR).
   Starting from the calibrated base coupling μ⋆\mu^{\star},
   we compute the perturbed distribution using the
   linear response system derived in Sections 3.4–3.5.
   This method uses the Fisher information matrix of the calibrated
   exponential family to approximate the perturbed coupling
   μpertε\mu^{\varepsilon}\_{\mathrm{pert}}
   without solving the full calibration problem again.

The goal of the experiment is twofold.
First, we verify that the perturbation-based sensitivities closely
match those obtained from full recalibration.
Second, we demonstrate that the perturbation method achieves a
substantial computational speedup compared to repeatedly solving the
full optimal transport calibration.

##### SPX perturbations.

In all experiments the perturbation is applied on the SPX side,
either as a spot shift or as a parallel shift of the SPX implied
volatility surface. These perturbations are mapped to corresponding
changes in the forward variance, which acts as the key control
variable in the SPX–VIX coupling.

The perturbations are chosen to remain within a regime where the
linear-response approximation is expected to be accurate while still
representing realistic market shocks.

##### Implementation details.

Several groups of parameters control the perturbation experiments:

* •

  Base OT object.
  The initial martingale optimal transport calibration provides the
  reference coupling μ⋆\mu^{\star} and the Fisher information matrix
  used in the perturbation calculations.
* •

  Bumped SPX information.
  The perturbed SPX marginal distributions include the shifted spot
  and the modified implied volatility surface at the relevant maturities.
  Throughout the experiments we assume a sticky-strike behavior for the
  SPX volatility surface under spot perturbations.
* •

  Perturbation controls.
  Parameters defining the magnitude and structure of the volatility
  perturbations, including lower and upper cutoffs for invariant
  volatility regions.
* •

  VIX volatility shape controls.
  Parameters governing the Skew Stickiness Ratio (SSR), skewness,
  convexity, and the treatment of at-the-money and out-of-the-money
  VIX option strikes.
* •

  Basis and numerical controls.
  Optional parameters allowing forward basis adjustments,
  regularization parameters, and marking conventions for volatility,
  skew, SSR, convexity, and VIX marginal constraints.

In the following section we use these perturbation scenarios to compare
SPX risk sensitivities of VIX derivatives computed using the two
methods described above.

### 9.4 VIX Option Risk And Cross-Greeks

Using the experimental setup described in Section 9.3, we now compare
SPX risk sensitivities of VIX derivatives computed using the two
methods:

* •

  Full recalibration, where the SPX–VIX martingale optimal
  transport model is recalibrated after each SPX perturbation.
* •

  Perturbation (linear response), where the sensitivities
  are obtained using the Fisher-information linear response system
  derived in Sections 3.4–3.5 without recomputing the full calibration.

For each SPX perturbation we compute the corresponding change in the
joint SPX–VIX distribution under both approaches and evaluate the
resulting price sensitivities of VIX derivatives.

##### VIX future cross-greeks.

We begin by comparing the SPX cross-greeks of the VIX future contract.
The sensitivities are computed with respect to SPX spot and SPX implied
volatility perturbations. Table 1 reports the SPX delta and SPX vega
of the VIX future obtained from the recalibration benchmark and from
the perturbation method.

Table 1: VIX Future ’s SPX Greeks LR-POT vs Recalibration

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | LR-POT. SPX Delta | Recalib. SPX Delta | LR-POT. SPX Vega | Recalib. SPX Vega |
| VIX Future | -8.88339 | -8.99380 | 1043.42832 | 1071.35419 |

The results show that the perturbation-based sensitivities closely
match those obtained from the full recalibration procedure. The
differences remain small relative to the magnitude of the sensitivities,
confirming that the linear response(LR) system provides an accurate local
approximation of the recalibrated optimal transport model.

##### VIX option SPX delta.

We next compare SPX delta sensitivities for a strip of VIX call options
spanning a wide range of strikes. The options correspond to the same
expiry used in the calibration experiment and cover both out-of-the-money
and near-the-money regions of the VIX smile.

Table 2: VIX Options SPX Delta Comparison (LR-POT vs Recalibration). March 18, 2026, 2w to expiry.

| Strike | Pert. Delta | Recalib. Delta |
| --- | --- | --- |
| 16.916.9 | 0.1020.102 | 0.0890.089 |
| 17.617.6 | 0.1370.137 | 0.1350.135 |
| 18.218.2 | 0.1730.173 | 0.1790.179 |
| 18.718.7 | 0.2070.207 | 0.2240.224 |
| 19.219.2 | 0.2450.245 | 0.2680.268 |
| 19.719.7 | 0.2860.286 | 0.3130.313 |
| 20.320.3 | 0.3280.328 | 0.3580.358 |
| 20.920.9 | 0.3710.371 | 0.4030.403 |
| 21.621.6 | 0.4690.469 | 0.4500.450 |
| 22.522.5 | 0.4200.420 | 0.4050.405 |
| 23.523.5 | 0.3690.369 | 0.3600.360 |
| 24.724.7 | 0.3160.316 | 0.3150.315 |
| 26.326.3 | 0.2660.266 | 0.2700.270 |
| 28.528.5 | 0.2220.222 | 0.2250.225 |
| 31.431.4 | 0.1780.178 | 0.1790.179 |
| 35.835.8 | 0.1330.133 | 0.1350.135 |
| 44.044.0 | 0.0890.089 | 0.0900.090 |

![Refer to caption](2603.10857v1/x11.png)


Figure 6: SPX Delta

Figure 6 visualizes the same comparison across strikes.

The perturbation-based deltas closely track the sensitivities obtained
from the full recalibration. Small discrepancies appear primarily in
the wings of the VIX smile, where nonlinear effects become more
pronounced. However, even in these regions the overall shape and
magnitude of the sensitivities remain consistent with the recalibration
benchmark.

##### VIX option SPX vega.

We perform the same comparison for SPX vega sensitivities of the VIX
options. Table 3 reports the SPX vega obtained from both approaches.

Table 3: VIX Options SPX Vega Comparison (LR-POT vs Recalibration). March 18, 2026, 2w to expiry.

| Strike | Pert. Vega | Rcalib. Vega |
| --- | --- | --- |
| 16.916.9 | 9.6889.688 | 10.26510.265 |
| 17.617.6 | 14.00414.004 | 15.64815.648 |
| 18.218.2 | 18.65618.656 | 20.89220.892 |
| 18.718.7 | 22.92122.921 | 26.23126.231 |
| 19.219.2 | 27.80727.807 | 31.48331.483 |
| 19.719.7 | 32.99032.990 | 36.83636.836 |
| 20.320.3 | 38.20538.205 | 42.20542.205 |
| 20.920.9 | 43.39743.397 | 47.57547.575 |
| 21.621.6 | 55.29955.299 | 53.98553.985 |
| 22.522.5 | 50.34450.344 | 48.60148.601 |
| 23.523.5 | 45.13945.139 | 43.21343.213 |
| 24.724.7 | 39.68639.686 | 37.82137.821 |
| 26.326.3 | 34.06734.067 | 32.41932.419 |
| 28.528.5 | 28.13128.131 | 27.01427.014 |
| 31.431.4 | 21.82021.820 | 21.56821.568 |
| 35.835.8 | 15.67315.673 | 16.20616.206 |
| 44.044.0 | 10.43210.432 | 10.80010.800 |

![Refer to caption](2603.10857v1/x12.png)


Figure 7: SPX Vega

As with the delta comparison, the perturbation method reproduces the
recalibrated sensitivities with high accuracy. The agreement confirms
that the Fisher-information linear response captures the dominant
first-order effects of SPX volatility perturbations on VIX option
prices.

##### Performance comparison.

While the recalibration method provides the benchmark sensitivities,
it requires solving the full SPX–VIX optimal transport calibration
problem after each perturbation. This involves repeated Sinkhorn
iterations together with enforcement of the martingale and
variance-consistency constraints, making the computation relatively
expensive.

Table 4: Risk Performance Comparison

|  |  |  |  |
| --- | --- | --- | --- |
| Base calibration | Recalib based risk calculation | DR-POT method | LR-POT method |
| 348.26 secs | 370.13 secs | 18.45 secs | 5.73 secs |

Table [4](#S9.T4 "Table 4 ‣ Performance comparison. ‣ 9.4 VIX Option Risk And Cross-Greeks ‣ 9 Experiments: SPX-VIX Risk Generation And Hedging Backtest ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport") compares the runtime required to compute sensitivities under
the three approaches. The results
show that the LR method and the DR method both achieve a substantial computational speedup while maintaining accuracy comparable to the recalibration benchmark.

This efficiency gain is the key practical advantage of the perturbation
framework: risk sensitivities can be generated quickly without
re-running the full martingale optimal transport calibration.

Lastly, we note here that the risk numbers generated by the DR method in [8](#S8 "8 Dimensional Reduction(DR) For POT ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport") are extremely close to those produced by the LR method.

### 9.5 Backtest: Hedging Efficiency Of Optimal Transport Method

We now evaluate whether the SPX sensitivities produced by our model independent risk generation methods lead to more effective hedging
than those generated by a benchmark industry standard model, in this case a stochastic local volatility model. In the backtest we perform below, we choose the dimensional reduction(DR) method in [8.4](#S8.SS4 "8.4 SPX–VIX Family Risk Generation: The Dimensional Reduction(DR) Approach ‣ 8 Dimensional Reduction(DR) For POT ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport").

The experiment consists of two parts: first hedging backtest in which portfolios of
VIX options are hedged using VIX futures; second hedging backtest in which the same option portfolio is hedged using SPX futures and SPX vanillas. The sizing of the VIX futures
is determined by matching SPX Vega computed under
either the optimal transport method or the stochastic local vol benchmark. The sizing of the SPX futures and SPX vanillas is similarly determined by matching SPX delta and SPX vega between the hedging instruments and the VIX option portfolio for each of the methods. Given that the comparison is between two risk hedging methodologies, and they trade comparable sizes, we have therefore omitted transaction cost.

##### Backtest period

The backtest runs daily from January 2024 to February 2026.
VIX smile dynamics follow the Skew Stickiness Ratio (SSR) rule

|  |  |  |
| --- | --- | --- |
|  | Δ​σV​(K)=−S​S​R⋅S​k​e​wV​(FV)​Δ​FV,\Delta\sigma\_{V}(K)=-SSR\cdot Skew\_{V}(F\_{V})\Delta F\_{V}, |  |

with S​S​R=1.2SSR=1.2.

##### Synthetic portfolio generation

To test the robustness of the hedging performance we generate
5050 randomized VIX option portfolios.

For each trading day tt the portfolios are constructed as follows:

1. 1.

   All listed VIX expiries available on day tt are included.
2. 2.

   For each expiry we construct a strike grid using call option deltas

   |  |  |  |
   | --- | --- | --- |
   |  | Δ∈{10,15,…,90},\Delta\in\{10,15,\ldots,90\}, |  |

   resulting in 1717 strikes per maturity.
3. 3.

   Options with Δ<50\Delta<50 are taken as puts while options
   with Δ≥50\Delta\geq 50 are taken as calls.
4. 4.

   Each option ii is assigned a random portfolio weight

   |  |  |  |
   | --- | --- | --- |
   |  | wi,t∼Uniform​(−1,1).w\_{i,t}\sim\text{Uniform}(-1,1). |  |

The resulting portfolio value is

|  |  |  |
| --- | --- | --- |
|  | Pt=∑iwi,t​Vi,t.P\_{t}=\sum\_{i}w\_{i,t}V\_{i,t}. |  |

This procedure produces diversified portfolios spanning a wide range
of smile exposures.

##### Hedging methodology

The portfolios are hedged using VIX futures whose expiries match those
of the VIX options. The hedge sizes are determined by matching SPX
Vega per expiry.

For a given model M∈{SV,POT}M\in\{\text{SV},\text{POT}\} we compute

|  |  |  |
| --- | --- | --- |
|  | GtM=∂Pt∂σS​P​X,G\_{t}^{M}=\frac{\partial P\_{t}}{\partial\sigma\_{SPX}}, |  |

the SPX sensitivity of the option portfolio, and

|  |  |  |
| --- | --- | --- |
|  | gj,tM=∂Fj,t∂σS​P​X,g\_{j,t}^{M}=\frac{\partial F\_{j,t}}{\partial\sigma\_{SPX}}, |  |

the SPX sensitivity of each VIX future Fj,tF\_{j,t}.

The hedge sizes αj,tM\alpha\_{j,t}^{M} are chosen so that

|  |  |  |
| --- | --- | --- |
|  | GtM+∑jαj,tM​gj,tM=0.G\_{t}^{M}+\sum\_{j}\alpha\_{j,t}^{M}g\_{j,t}^{M}=0. |  |

##### Hedged P&L

The daily hedged P&L for model MM is

|  |  |  |
| --- | --- | --- |
|  | P&LtM=Δ​Pt+∑jαj,tM​Δ​Fj,t.P\&L\_{t}^{M}=\Delta P\_{t}+\sum\_{j}\alpha\_{j,t}^{M}\Delta F\_{j,t}. |  |

The effectiveness of the hedge is evaluated using the standard
deviation of the hedged P&L.

##### Cross-sectional comparison across portfolios

For each of the 5050 randomly generated portfolios we compute the
standard deviation of the hedged P&L under both hedging strategies.

Figure [8](#S9.F8 "Figure 8 ‣ Cross-sectional comparison across portfolios ‣ 9.5 Backtest: Hedging Efficiency Of Optimal Transport Method ‣ 9 Experiments: SPX-VIX Risk Generation And Hedging Backtest ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport") plots the difference

|  |  |  |
| --- | --- | --- |
|  | σP​O​T−σS​V\sigma\_{POT}-\sigma\_{SV} |  |

for each portfolio, where σP​O​T\sigma\_{POT} and σS​V\sigma\_{SV} denote the
standard deviation of hedged P&L under the POT and SV hedges,
respectively.

![Refer to caption](2603.10857v1/Figures/backest1.png)


Figure 8: Difference in hedged P&L standard deviation between the
POT hedge and the SV hedge across 5050 randomized VIX option portfolios using VIX futures.
Each bar corresponds to one portfolio.
Negative values indicate that the POT hedge achieves lower hedging
variance than the SV hedge.

##### Time-series hedge stability

To illustrate the time-series behavior of the hedging error,
we select one representative portfolio from the set of
5050 portfolios and compute the rolling 2020-day standard
deviation of hedged P&L.

|  |  |  |
| --- | --- | --- |
|  | RollStdevtM​(20)=119​∑u=t−19t(P&LuM−P&L¯t,20M)2.\text{RollStdev}\_{t}^{M}(20)=\sqrt{\frac{1}{19}\sum\_{u=t-19}^{t}\left(P\&L\_{u}^{M}-\overline{P\&L}\_{t,20}^{M}\right)^{2}}. |  |

![Refer to caption](2603.10857v1/Figures/backest2.png)


Figure 9: 20-day rolling standard deviation of VIX future hedged P&L for a
representative portfolio. The POT hedge produces lower hedging
variance during volatile periods while remaining comparable to
the SV hedge during calm market regimes.

![Refer to caption](2603.10857v1/x13.png)


Figure 10: Difference in hedged P&L standard deviation between the
POT hedge and the SV hedge across 5050 randomized VIX option portfolios using SPX futures and SPX vanillas.
Each bar corresponds to one portfolio.
Negative values indicate that the POT hedge achieves lower hedging
variance than the SV hedge.

![Refer to caption](2603.10857v1/x14.png)


Figure 11: 20-day rolling standard deviation of SPX future and SPX vanillas hedged P&L for a
representative portfolio. The POT hedge produces lower hedging
variance during volatile periods while remaining comparable to
the SV hedge during calm market regimes.

##### Summary

The cross-sectional experiment in Figure [8](#S9.F8 "Figure 8 ‣ Cross-sectional comparison across portfolios ‣ 9.5 Backtest: Hedging Efficiency Of Optimal Transport Method ‣ 9 Experiments: SPX-VIX Risk Generation And Hedging Backtest ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport")
shows that the POT VIX future hedge reduces PnL variance for all tested
portfolios. In Figure [10](#S9.F10 "Figure 10 ‣ Time-series hedge stability ‣ 9.5 Backtest: Hedging Efficiency Of Optimal Transport Method ‣ 9 Experiments: SPX-VIX Risk Generation And Hedging Backtest ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport"), all but 1 of the 50 VIX option portfolios have smaller PnL variance for the POT method when hedged to SPX futures and SPX vanillas. The time-series analysis in both Figure [9](#S9.F9 "Figure 9 ‣ Time-series hedge stability ‣ 9.5 Backtest: Hedging Efficiency Of Optimal Transport Method ‣ 9 Experiments: SPX-VIX Risk Generation And Hedging Backtest ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport") and Figure [11](#S9.F11 "Figure 11 ‣ Time-series hedge stability ‣ 9.5 Backtest: Hedging Efficiency Of Optimal Transport Method ‣ 9 Experiments: SPX-VIX Risk Generation And Hedging Backtest ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport")
further demonstrates that the improvement is most pronounced
during periods of elevated market volatility.

Together these results provide empirical evidence that the
perturbed optimal transport framework produces more accurate
SPX–VIX risk sensitivities than a benchmark stochastic local volatility model.

## 10 Conclusion

This paper develops a model-independent framework for SPX–VIX risk
generation based on entropic martingale optimal transport.
Starting from the joint calibration methodology of Guyon,
we show that the calibrated Gibbs coupling admits a natural perturbation
theory: admissible market shocks propagate through the Fisher information
matrix of the calibrated exponential family, yielding explicit
linear-response formulas for risk sensitivities.

To incorporate realistic VIX smile dynamics, we introduce a linearized
Skew Stickiness Ratio formulation and embed it as linear constraints in the
transport perturbation system.
This approach allows SPX perturbations to propagate consistently to
VIX implied volatility while maintaining the convex structure of the
entropic projection problem.

We further show that the perturbed transport problem admits a structural
dimensional reduction under a conditional coupling invariance assumption.
In this regime the three-dimensional transport problem collapses to a
two-dimensional projection on (S1,V)(S\_{1},V) while preserving the conditional
dependence structure inherited from the base calibration.
This explains why risk sensitivities can be generated efficiently without
re-solving the full martingale optimal transport calibration.

Two sets of numerical experiments support the theoretical framework.
First, we compare perturbation-based risk sensitivities with those
obtained from full recalibration of the SPX–VIX transport model.
Across VIX futures and VIX option cross-greeks, the perturbation
method produces sensitivities that are very close to the recalibration
benchmark while achieving significant computational speedups.
Second, we conduct hedging backtests on randomized VIX option portfolios.
Using SPX sensitivities generated by the dimension-reduced transport
method, the resulting hedges consistently outperform those based on
a stochastic volatility benchmark in terms of hedged P&L variance.

Overall, the results show that entropic martingale optimal transport
provides more than a calibration tool.
Combined with perturbation theory and dimensional reduction,
it yields a practical framework for SPX–VIX risk generation that is
financially consistent, computationally efficient, and effective in
hedging applications.

## Disclaimer

This paper was prepared for informational purposes in part by the Quantitative Trading & Research Group of JPMorganChase & Co. This paper is not a product of the Research Department of JPMorganChase & Co. or its affiliates. Neither JPMorganChase & Co. nor any of its affiliates makes any explicit or implied representation or warranty and none of them accept any liability in connection with this paper, including, without limitation, with respect to the completeness, accuracy, or reliability of the information contained herein and the potential legal, compliance, tax, or accounting effects thereof. This document is not intended as investment research or investment advice, or as a recommendation, offer, or solicitation for the purchase or sale of any security, financial instrument, financial product or service, or to be used in any way for evaluating the merits of participating in any transaction.

## References

* S. Amari (2016)
  Information geometry and its applications.
   Springer.
  Cited by: [§3.7](#S3.SS7.p13.1 "3.7 Information-Geometric Interpretation ‣ 3 Perturbation Theory: General Marginal Shocks ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport").
* C. Bayer and P. K. Friz (2022)
  Regularity of stochastic volatility models: rough and beyond.
  MOS-SIAM Series on Optimization, Society for Industrial and Applied Mathematics.
  External Links: [Document](https://dx.doi.org/10.1137/1.9781611977783),
  [Link](https://epubs.siam.org/doi/book/10.1137/1.9781611977783)
  Cited by: [§1](#S1.p2.1 "1 Introduction ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport").
* M. Beiglböck, P. Henry-Labordère, and F. Penkner (2013)
  Model-independent bounds for option prices: a mass transport approach.
  Finance and Stochastics 17 (3),  pp. 477–501.
  External Links: [Document](https://dx.doi.org/10.1007/s00780-013-0205-8)
  Cited by: [§1.1](#S1.SS1.p5.1 "1.1 Related Literature ‣ 1 Introduction ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport").
* J. Benamou, G. Carlier, M. Cuturi, L. Nenna, and G. Peyré (2015)
  Iterative bregman projections for regularized transportation problems.
  SIAM Journal on Scientific Computing 37 (2).
  Cited by: [§1.1](#S1.SS1.p7.1 "1.1 Related Literature ‣ 1 Introduction ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport"),
  [§1](#S1.p3.1 "1 Introduction ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport").
* L. Bergomi (2009)
  Smile dynamics II.
   Fields Institute.
  Note: Fields Institute Seminar, Toronto<https://www.fields.utoronto.ca/programs/scientific/09-10/finance/derivatives/bergomi.pdf>
  Cited by: [§6.1](#S6.SS1.p1.3 "6.1 Skew Stickiness Ratio: Bergomi’s Definition And Extension To VIX ‣ 6 SSR Dynamics For VIX And Its Linearization ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport"),
  [§6.2](#S6.SS2.p2.2 "6.2 Linear SSR Approximation And Second–Order Accuracy ‣ 6 SSR Dynamics For VIX And Its Linearization ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport").
* L. Bergomi (2016)
  Stochastic volatility modeling.
   CRC Press, Boca Raton.
  Cited by: [§1.1](#S1.SS1.p3.1 "1.1 Related Literature ‣ 1 Introduction ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport"),
  [§1](#S1.p2.1 "1 Introduction ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport"),
  [§6.1](#S6.SS1.p1.3 "6.1 Skew Stickiness Ratio: Bergomi’s Definition And Extension To VIX ‣ 6 SSR Dynamics For VIX And Its Linearization ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport").
* M. Cuturi (2013)
  Sinkhorn distances: lightspeed computation of optimal transport.
  Advances in Neural Information Processing Systems.
  Cited by: [§1.1](#S1.SS1.p7.1 "1.1 Related Literature ‣ 1 Introduction ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport"),
  [§1](#S1.p3.1 "1 Introduction ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport").
* J. Gatheral (2006)
  The volatility surface: a practitioner’s guide.
   John Wiley & Sons, Hoboken, NJ.
  Cited by: [§1.1](#S1.SS1.p3.1 "1.1 Related Literature ‣ 1 Introduction ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport"),
  [§1](#S1.p2.1 "1 Introduction ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport").
* J. Guyon (2020)
  The joint S&P 500/VIX smile calibration puzzle solved.
  Risk.
  Cited by: [§1.1](#S1.SS1.p5.1 "1.1 Related Literature ‣ 1 Introduction ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport"),
  [§1.3](#S1.SS3.p8.1 "1.3 Market Consistency And Risk Propagation ‣ 1 Introduction ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport"),
  [§1.4](#S1.SS4.SSS0.Px2.p1.2 "SPX–VIX consistency condition ‣ 1.4 Martingality And Consistency Conditions ‣ 1 Introduction ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport"),
  [§1.4](#S1.SS4.SSS0.Px3.p1.1 "Practical considerations ‣ 1.4 Martingality And Consistency Conditions ‣ 1 Introduction ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport"),
  [§1.4](#S1.SS4.p1.1 "1.4 Martingality And Consistency Conditions ‣ 1 Introduction ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport"),
  [§1](#S1.p3.1 "1 Introduction ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport"),
  [§7.1](#S7.SS1.p5.1 "7.1 Base Calibration ‣ 7 Algorithm For SPX–VIX Risk Without Recalibration ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport").
* J. Guyon (2021)
  Dispersion-constrained martingale schrödinger problems and the exact joint S&P 500/VIX smile calibration puzzle.
   Bloomberg L.P.; CERMICS, École des Ponts ParisTech.
  Note: SSRN preprint
  Cited by: [§1.1](#S1.SS1.p5.1 "1.1 Related Literature ‣ 1 Introduction ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport"),
  [§1.3](#S1.SS3.p8.1 "1.3 Market Consistency And Risk Propagation ‣ 1 Introduction ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport"),
  [§1.4](#S1.SS4.SSS0.Px2.p1.2 "SPX–VIX consistency condition ‣ 1.4 Martingality And Consistency Conditions ‣ 1 Introduction ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport"),
  [§1.4](#S1.SS4.SSS0.Px3.p1.1 "Practical considerations ‣ 1.4 Martingality And Consistency Conditions ‣ 1 Introduction ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport"),
  [§1.4](#S1.SS4.p1.1 "1.4 Martingality And Consistency Conditions ‣ 1 Introduction ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport"),
  [§1](#S1.p3.1 "1 Introduction ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport").
* P. Henry-Labordère (2017)
  Model-free hedging: a martingale optimal transport viewpoint.
  Chapman and Hall/CRC Financial Mathematics Series, CRC Press, Boca Raton.
  Cited by: [§1.1](#S1.SS1.p5.1 "1.1 Related Literature ‣ 1 Introduction ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport").
* S. L. Heston (1993)
  A closed-form solution for options with stochastic volatility with applications to bond and currency options.
  The Review of Financial Studies 6 (2),  pp. 327–343.
  External Links: [Document](https://dx.doi.org/10.1093/rfs/6.2.327)
  Cited by: [§1.1](#S1.SS1.p3.1 "1.1 Related Literature ‣ 1 Introduction ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport"),
  [§1](#S1.p2.1 "1 Introduction ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport").
* G. Peyré and M. Cuturi (2019)
  Computational optimal transport.
  Foundations and Trends in Machine Learning 11 (5–6),  pp. 355–607.
  Cited by: [§1.1](#S1.SS1.p7.1 "1.1 Related Literature ‣ 1 Introduction ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport"),
  [§3.7](#S3.SS7.p13.1 "3.7 Information-Geometric Interpretation ‣ 3 Perturbation Theory: General Marginal Shocks ‣ SPX–VIX Risk Computations Via Perturbed Optimal Transport").

BETA