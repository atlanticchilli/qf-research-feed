---
authors:
- Jeonggyu Huh
- Hyeng Keun Koo
doc_id: arxiv:2601.03175v1
family_id: arxiv:2601.03175
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter
  Uncertainty via Pontryagin Projection'
url_abs: http://arxiv.org/abs/2601.03175v1
url_html: https://arxiv.org/html/2601.03175v1
venue: arXiv q-fin
version: 1
year: 2026
---


Jeonggyu Huh
Department of Mathematics, Sungkyunkwan University, Suwon, Republic of Korea

Hyeng Keun Koo
Department of Financial Engineering, Ajou University, Suwon, Republic of Korea

###### Abstract

We study continuous-time portfolio choice in diffusion markets with parameter θ∈Θ\theta\in\Theta and uncertainty law q​(d​θ)q(d\theta).
Nature draws latent θ∼q\theta\sim q at time 0; the investor cannot observe it and must deploy a single θ\theta-blind feedback policy maximizing an *ex–ante* CRRA objective averaged over diffusion noise and θ\theta.
Our methods access qq only by sampling and assume no parametric form.
We extend Pontryagin–Guided Direct Policy Optimization (PG–DPO) by sampling θ\theta inside the simulator and computing discrete-time gradients via backpropagation through time (BPTT), and we propose projected PG–DPO (P–PGDPO) that projects costate estimates to satisfy the qq-aggregated Pontryagin first-order condition, yielding a deployable rule.
We prove a BPTT–PMP correspondence uniform on compacts and a residual-based θ\theta-blind policy-gap bound under local stability with explicit discretization/Monte Carlo errors; experiments show projection-driven stability and accurate decision-time benchmark recovery in high dimensions.

## 1 Introduction

A central problem in quantitative finance is to allocate wealth dynamically across many risky assets in continuous time.
In the classical Merton model, investment opportunities are described by a low-dimensional diffusion with *known* drift and volatility, and the investor solves a Hamilton–Jacobi–Bellman (HJB) equation to obtain closed-form optimal portfolios and value functions; see, for example, merton1969lifetime; merton1971optimum and the subsequent literature.
In realistic markets, however, neither expected returns nor volatilities are known: they must be estimated from finite samples, often using many assets and predictors and under nontrivial model selection and regularization.
Empirically, expected-return forecasting is fragile and return predictability is unstable across samples and over time, with many proposed predictors delivering limited out-of-sample gains (e.g., goyalwelch2008; campbellthompson2008; rapach2010forecast; danglhalling2012tvp; lettauvanNieuwerburgh2008shifts; pettenuzzo2014constraints).
In such settings it is crucial to distinguish diffusion risk (Brownian noise conditional on parameters) from statistical parameter uncertainty (error in estimated coefficients).
A long line of portfolio-choice work shows that return predictability, learning, and parameter uncertainty can induce substantial intertemporal hedging effects and more conservative allocations (e.g., kandelstambaugh1996predictability; barberis2000investor; campbell2002strategic; brandt2005portfolio; brennan1998investor; xia2001learning; maenhout2004robust).

We study continuous-time portfolio choice when market dynamics are known only up to an *estimated* parameter θ∈Θ\theta\in\Theta, where the estimation pipeline produces a nondegenerate uncertainty law q​(d​θ)q(d\theta) over Θ\Theta.
We treat qq as an *input* object that encapsulates all statistical information available at time 0:
it may be derived from resampling approximations (e.g. bootstrap) (e.g., efron1979bootstrap; efron1994bootstrap),
model averaging or Bayesian model uncertainty pipelines (e.g., pastor2000portfolio; avramov2002stock; cremers2002stock),
approximate posteriors, or other procedures.
Our goal is not to revisit inference, but to optimize decisions *given* this uncertainty description.
Algorithmically, we interact with qq only through sampling θ∼q\theta\sim q inside the simulator; we do not assume closed-form densities, conjugate updates, or any particular parametric form.
Concretely, we seek portfolio policies that maximize terminal CRRA utility *ex–ante*, averaging over both diffusion noise and parameter draws θ∼q\theta\sim q.
This formulation also supports offline diagnostics that quantify how recommended allocations vary across the statistically plausible models encoded in qq.

A key modeling choice is that θ\theta is *latent*: Nature draws a fixed but unobserved θ∼q\theta\sim q at time 0 (independent of the Brownian drivers) and keeps it fixed on [0,T][0,T].
While the investor knows qq, she does not observe the realized θ\theta and must therefore deploy a single *θ\theta-blind* policy.
We restrict attention to Markov feedback policies of the form πt=π¯​(t,Xt,Yt)\pi\_{t}=\bar{\pi}(t,X\_{t},Y\_{t}) that depend only on observable wealth XtX\_{t} and market factors YtY\_{t}, and we do not augment the state by a belief/posterior process.
This fixed-qq commitment is intended as a *decision-time* benchmark: it targets a single deployable rule given an exogenous uncertainty law, cleanly decoupling *how* uncertainty is produced (any pipeline yielding qq) from *how* decisions are optimized (our solver given qq).
We do not claim that belief-state control is conceptually inappropriate; rather, it defines a different (and typically far more demanding) problem than computing a single θ\theta-blind deployable feedback rule from a fixed uncertainty description (e.g., bensoussan1985optimal; pham2017dynamic).
At the same time, fixed-qq optimization couples heterogeneous market models: gradient signals can vary substantially across θ\theta draws and may partially cancel when learning a single global policy end-to-end.

The θ\theta-blind constraint also changes what a first-order optimality condition means.
If θ\theta were observable, Pontryagin’s Maximum Principle (PMP) yields a θ\theta-conditional criticality condition and an associated θ\theta-conditional full-information feedback map (infeasible under latent θ\theta).
Under θ\theta-blind deployability, admissible perturbations are also θ\theta-blind.
Taking the first variation of the ex–ante objective and using Fubini’s theorem shows that the correct necessary condition is *qq-aggregated*: the expectation over θ∼q\theta\sim q of the Hamiltonian gradient ∂πHθctrl\partial\_{\pi}H^{\mathrm{ctrl}}\_{\theta} must vanish along the state process, in the standard stochastic maximum principle framework (e.g., yong1999stochastic; fleming2006controlled; pham2009continuous).
Because ∂πHθctrl\partial\_{\pi}H^{\mathrm{ctrl}}\_{\theta} is affine in π\pi for our portfolio Hamiltonian, this aggregation yields a statewise linear system whose solution defines a deployable θ\theta-blind projected portfolio rule.
Notably, the condition and resulting projection are agnostic to the internal construction of qq and depend only on its role as the ex–ante mixing law.

These features place the problem outside the practical reach of classical dynamic programming in the *high-dimensional* regime we target.
In low-dimensional deterministic-parameter Markov models, DP/HJB is canonical; however, even with several factors it requires solving an HJB equation in the state (t,Xt,Yt)(t,X\_{t},Y\_{t}), where grid-based PDE methods are quickly defeated by the curse of dimensionality (e.g., bellman1961adaptive; kushner2001numerical).
Deep PDE surrogates such as PINNs (e.g., raissi2019physics; sirignano2018dgm) and deep BSDE methods (e.g., han2018solving; beck2019machine) alleviate the need for grids, but fully nonlinear portfolio HJBs with many assets and factors remain numerically delicate, especially when accurate mixed derivatives are required.
If one further models parameter uncertainty via belief-state augmentation, the state becomes a posterior measure and the control problem becomes infinite-dimensional (e.g., bensoussan1985optimal; pham2017dynamic).

Our approach is simulation-based and builds on *Pontryagin–Guided Direct Policy Optimization* (PG–DPO) (huh2025breaking; huh2025constraint).
PG–DPO parameterizes a θ\theta-blind feedback policy via a neural network, simulates trajectories of the controlled SDE, and employs backpropagation through time (BPTT) to compute exact gradients of terminal utility.
Crucially, intermediate pathwise sensitivities computed by BPTT coincide with the stochastic costates (adjoints) in PMP, mirroring the classical duality between backpropagation and adjoint methods (see lecun1988optimal; yong1999stochastic).
In the latent-parameter setting, we approximate the ex–ante objective by sampling θ∼q\theta\sim q inside the simulator and fixing it along each trajectory, while the policy depends only on observable states.
To stabilize learning under heterogeneous θ\theta draws, we extend the projected variant, *P–PGDPO*, to latent θ\theta: after a warm-up phase that stabilizes costate estimates, we project Monte Carlo Pontryagin objects onto the qq-aggregated Pontryagin first-order condition.
This reconstruction yields a robust deployable θ\theta-blind rule obtained from the qq-aggregated criticality, and can be amortized into a fast-to-evaluate policy.

In high-dimensional scaling experiments under static Gaussian drift uncertainty, the two-stage projected pipeline substantially improves decision-time accuracy relative to end-to-end learning, with clear stabilization effects in aligned regimes.
In misaligned regimes, projection gains diminish with dimension; diagnostics indicate that deterioration is driven primarily by growth of aggregated first-order residuals and curvature mismatch rather than by catastrophic numerical inversion.
In factor-driven markets with mean-reverting investment opportunities where return–factor correlation induces intertemporal hedging demand, the projected pipeline recovers the analytic decision-time benchmark under the same θ\theta-blind deployability restriction, while a model-free PPO baseline remains far from the reference in the regimes we test.

Our main theoretical guarantee is a residual-based ex–ante θ\theta-blind policy-gap bound for the deployable fixed-qq commitment problem:
under mild slab-wise local stability conditions for the qq-aggregated projection map, a small warm-up aggregated first-order residual implies that the projected policy is close (in L2​(μ)L^{2}(\mu)) to a locally optimal interior deployable θ\theta-blind policy, up to discretization and Monte Carlo error.

Our contributions are threefold.
(i) We formulate a latent-parameter, fixed-qq ex–ante CRRA portfolio problem under a deployable θ\theta-blind Markov feedback restriction and derive the corresponding qq-aggregated Pontryagin first-order condition, emphasizing an inference-agnostic interface where uncertainty enters only through an exogenous mixing law q​(d​θ)q(d\theta).
(ii) We extend PG–DPO to this setting by sampling θ\theta only inside the simulator and using BPTT to compute exact discrete-time gradients and pathwise sensitivities, and we establish a conditional BPTT–PMP correspondence uniform over θ\theta on compact subsets of Θ\Theta.
(iii) We develop uncertainty-aware P–PGDPO that projects Monte Carlo costate estimates to produce a deployable qq-aggregated θ\theta-blind rule, together with a residual-based ex–ante θ\theta-blind policy-gap bound and empirical evidence of two-time-scale stabilization and stability gains from projection.

The remainder of the paper is organized as follows.
Section [2](https://arxiv.org/html/2601.03175v1#S2 "2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection") formulates the fixed-qq ex–ante portfolio problem under a latent parameter and a deployable θ\theta-blind Markov feedback restriction, and derives the θ\theta-conditional versus qq-aggregated Pontryagin first-order conditions together with Gaussian decision-time reference models.
Section [3](https://arxiv.org/html/2601.03175v1#S3 "3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection") develops PG–DPO and uncertainty-aware P–PGDPO for the latent-θ\theta setting, establishes the conditional BPTT–PMP correspondence, and proves a residual-based ex–ante θ\theta-blind policy-gap bound under local stability of the aggregated projection map.
Section [4](https://arxiv.org/html/2601.03175v1#S4 "4 Breaking the Dimensional Barrier under Drift Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection") reports high-dimensional scaling experiments under static Gaussian drift uncertainty, and Section [5](https://arxiv.org/html/2601.03175v1#S5 "5 Recovering Intertemporal Hedging Demand in Factor-Driven Markets ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection") studies hedging-demand recovery in factor-driven markets with mean-reverting investment opportunities.
Technical proofs and implementation details are collected in the appendix.

## 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty

In this section we formulate a continuous-time dynamic portfolio choice problem with CRRA preferences in a diffusion market whose coefficients are estimated from data and are therefore statistically uncertain. Rather than committing to a particular estimation architecture, we treat the market as belonging to a (possibly high-dimensional) parameterized family indexed by θ∈Θ\theta\in\Theta, and we represent the uncertainty in the estimated parameter by an exogenously given probability law q​(d​θ)q(d\theta) over Θ\Theta.

* •

  Nature draws a fixed but unobserved θ∼q\theta\sim q at time 0 and keeps it constant on [0,T][0,T].
* •

  The investor knows qq but does not observe the realized θ\theta and must deploy a single θ\theta-blind portfolio policy.
* •

  Performance is evaluated *ex–ante* by averaging terminal utility over both diffusion noise and θ∼q\theta\sim q.
* •

  We restrict to θ\theta-blind Markov feedback rules πt=π¯​(t,Xt,Yt)\pi\_{t}=\bar{\pi}(t,X\_{t},Y\_{t}) and do not augment the state by a belief/posterior process.

This fixed-qq, θ\theta-blind formulation is intentionally *algorithm-facing*: we view the estimation procedure that produced q​(d​θ)q(d\theta) as exogenous, and our goal is to compute stable, scalable portfolio rules *given* this uncertainty description. It is also a *commitment* model: the investor commits at time 0 to a single feedback map and does not update qq during trading. As a result, one must distinguish between (i) θ\theta-conditional (full-information) optimality conditions and objects that would be available if θ\theta were observable (infeasible under latent θ\theta), and (ii) qq-aggregated conditions that characterize optimality *within the θ\theta-blind admissible class*. Throughout, θ\theta-conditional objects are used only for offline diagnostics (e.g., heterogeneity inspection and infeasible upper bounds), whereas our algorithms target a single deployable θ\theta-blind rule; see Section [2.2](https://arxiv.org/html/2601.03175v1#S2.SS2 "2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection").

### 2.1 Model and ex–ante objective in estimated diffusion markets

We work on a filtered probability space
(Ω,ℱ,(ℱt)t∈[0,T],ℙ)(\Omega,\mathcal{F},(\mathcal{F}\_{t})\_{t\in[0,T]},\mathbb{P})
supporting Brownian motions of appropriate dimension. Time is continuous and runs over a fixed finite horizon [0,T][0,T].

##### Deterministic-parameter reference (classical CRRA Merton).

There is one risk-free asset (money market account) with price process BB satisfying

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​BtBt=r​d​t,B0=1,\frac{dB\_{t}}{B\_{t}}=r\,dt,\hskip 18.49988ptB\_{0}=1, |  | (1) |

where r∈ℝr\in\mathbb{R} is a constant short rate. In the classical Merton model, the dd risky assets have prices
St=(St1,…,Std)⊤S\_{t}=(S\_{t}^{1},\dots,S\_{t}^{d})^{\top} solving

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​StSt:=(d​St1St1,…,d​StdStd)⊤=r​ 1​d​t+μ​d​t+Σ1/2​d​Wt,S0∈(0,∞)d,\frac{dS\_{t}}{S\_{t}}:=\bigg(\frac{dS\_{t}^{1}}{S\_{t}^{1}},\dots,\frac{dS\_{t}^{d}}{S\_{t}^{d}}\bigg)^{\top}=r\,\mathbf{1}\,dt+\mu\,dt+\Sigma^{1/2}dW\_{t},\hskip 18.49988ptS\_{0}\in(0,\infty)^{d}, |  | (2) |

with constant excess returns μ∈ℝd\mu\in\mathbb{R}^{d}, volatility matrix Σ1/2∈ℝd×d\Sigma^{1/2}\in\mathbb{R}^{d\times d}, and a dd-dimensional Brownian motion WW.
An investor with CRRA utility U​(x)=x1−γ/(1−γ)U(x)=x^{1-\gamma}/(1-\gamma), γ>0,γ≠1\gamma>0,\gamma\neq 1, chooses a progressively measurable portfolio fraction πt∈ℝd\pi\_{t}\in\mathbb{R}^{d}; the wealth process satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​XtπXtπ=(r+πt⊤​λ)​d​t+πt⊤​Σ1/2​d​Wt,X0π=x>0,\frac{dX\_{t}^{\pi}}{X\_{t}^{\pi}}=\big(r+\pi\_{t}^{\top}\lambda\big)dt+\pi\_{t}^{\top}\Sigma^{1/2}dW\_{t},\hskip 18.49988ptX\_{0}^{\pi}=x>0, |  | (3) |

where λ:=μ\lambda:=\mu is the vector of risk premia. In this benchmark setting the optimal policy is constant:

|  |  |  |  |
| --- | --- | --- | --- |
|  | π⋆=1γ​Σ−1​λ,\pi^{\star}=\frac{1}{\gamma}\,\Sigma^{-1}\lambda, |  | (4) |

and the corresponding value function is given explicitly by

|  |  |  |  |
| --- | --- | --- | --- |
|  | VMerton​(t,x;λ)=x1−γ1−γ​exp⁡{(1−γ)​(r+12​γ​λ⊤​Σ−1​λ)​(T−t)},V^{\mathrm{Merton}}(t,x;\lambda)=\frac{x^{1-\gamma}}{1-\gamma}\,\exp\Big\{(1-\gamma)\Big(r+\tfrac{1}{2\gamma}\lambda^{\top}\Sigma^{-1}\lambda\Big)(T-t)\Big\}, |  | (5) |

see, for example, merton1969lifetime; merton1971optimum. We use this constant-coefficient model only as a deterministic-parameter reference.

##### Estimated diffusion market family (conditional on a latent parameter).

In our main formulation, drift and volatility are not assumed known. Instead, we consider a general multi-asset, multi-factor diffusion family indexed by θ∈Θ⊂ℝk\theta\in\Theta\subset\mathbb{R}^{k}, where θ\theta represents the (possibly high-dimensional) parameter produced by an estimation procedure. Conditional on θ\theta, the dd risky assets and an mm-dimensional factor process YtY\_{t} evolve as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​StSt\displaystyle\frac{dS\_{t}}{S\_{t}} | =r​ 1​d​t+b​(Yt,θ)​d​t+σ​(Yt,θ)​d​Wt,S0∈(0,∞)d,\displaystyle=r\,\mathbf{1}\,dt+b\big(Y\_{t},\theta\big)\,dt+\sigma\big(Y\_{t},\theta\big)\,dW\_{t},\hskip 18.49988ptS\_{0}\in(0,\infty)^{d}, |  | (6) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Yt\displaystyle dY\_{t} | =a​(Yt,θ)​d​t+β​(Yt,θ)​d​WtY,Y0=y∈ℝm,\displaystyle=a\big(Y\_{t},\theta\big)\,dt+\beta\big(Y\_{t},\theta\big)\,dW\_{t}^{Y},\hskip 18.49988ptY\_{0}=y\in\mathbb{R}^{m}, |  | (7) |

where WW and WYW^{Y} are Brownian motions (possibly of different dimension) that may be instantaneously correlated. We write the instantaneous covariance and return–factor cross-covariance as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ​(y,θ):=σ​(y,θ)​σ​(y,θ)⊤,ΣS​Y​(y,θ):=σ​(y,θ)​ρ​β​(y,θ)⊤,\Sigma(y,\theta):=\sigma(y,\theta)\sigma(y,\theta)^{\top},\hskip 18.49988pt\Sigma\_{SY}(y,\theta):=\sigma(y,\theta)\,\rho\,\beta(y,\theta)^{\top}, |  | (8) |

where ρ\rho is defined by d​⟨W,WY⟩t=ρ​d​td\langle W,W^{Y}\rangle\_{t}=\rho\,dt. Thus Σ​(y,θ)∈ℝd×d\Sigma(y,\theta)\in\mathbb{R}^{d\times d} and ΣS​Y​(y,θ)∈ℝd×m\Sigma\_{SY}(y,\theta)\in\mathbb{R}^{d\times m}.

##### Uncertainty law q​(d​θ)q(d\theta) and information structure.

The parameter θ\theta is estimated from finite samples and is uncertain. We summarize this uncertainty by a probability distribution

|  |  |  |  |
| --- | --- | --- | --- |
|  | q​(d​θ).q(d\theta). |  | (9) |

We deliberately do not tie qq to any specific inference paradigm. Concretely, qq may represent an empirical/sampling distribution produced by resampling procedures such as the bootstrap (efron1979bootstrap; efron1994bootstrap), a distribution induced by model averaging or sub-sample aggregation procedures such as bagging (breiman1996bagging), an approximate Bayesian posterior (when a prior and likelihood/criterion are specified), or an asymptotic normal (or sandwich) approximation in parametric or semiparametric estimation. For our purposes, qq is an *input* object describing statistically plausible market parameters.

###### Remark 1 (Latent parameter, observability, and admissible controls).

We interpret θ\theta as a latent (unobserved) market parameter: Nature draws an ℱ0\mathcal{F}\_{0}-measurable random variable θ∼q\theta\sim q at time 0 (independent of the Brownian drivers) and keeps it fixed over [0,T][0,T]. The investor knows qq but does not observe the realized θ\theta, so deployable portfolio rules cannot take θ\theta as an input.

We consider the observable market filtration

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℱtobs:=σ​{(Ss,Ys):0≤s≤t},0≤t≤T,\mathcal{F}\_{t}^{\mathrm{obs}}:=\sigma\{(S\_{s},Y\_{s}):0\leq s\leq t\},\hskip 18.49988pt0\leq t\leq T, |  | (10) |

where σ​{⋅}\sigma\{\cdot\} denotes the σ\sigma-field generated by the observed asset and factor paths (with the usual augmentation). Admissible portfolio processes are required to be progressively measurable with respect to (ℱtobs)(\mathcal{F}\_{t}^{\mathrm{obs}}).

Throughout the paper we *restrict* attention to the Markov feedback subclass

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜fb:={π∈𝒜obs:∃π¯:[0,T]×(0,∞)×ℝm→ℝd​s.t.​πt=π¯​(t,Xt,Yt)},\mathcal{A}^{\mathrm{fb}}:=\Big\{\pi\in\mathcal{A}^{\mathrm{obs}}:\ \exists\,\bar{\pi}:[0,T]\times(0,\infty)\times\mathbb{R}^{m}\to\mathbb{R}^{d}\ \text{s.t.}\ \pi\_{t}=\bar{\pi}(t,X\_{t},Y\_{t})\Big\}, |  | (11) |

where 𝒜obs\mathcal{A}^{\mathrm{obs}} is defined below. This restriction reflects a fixed-qq commitment model: the investor uses historical data to form qq prior to trading and does not perform online filtering/belief-state updates during [0,T][0,T].

Whenever we display θ\theta-conditional (full-information) controls or sensitivity objects, they are computed under frozen-θ\theta simulations and are used only for offline diagnostics; the deployed policy class and the learned policy remain θ\theta-blind.

##### Wealth dynamics and admissibility (given θ\theta).

For any fixed θ\theta, the corresponding wealth dynamics under a portfolio process πt​(ω)∈ℝd\pi\_{t}(\omega)\in\mathbb{R}^{d} adapted to ℱtobs\mathcal{F}\_{t}^{\mathrm{obs}} are

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​XtπXtπ=(r+πt⊤​b​(Yt,θ))​d​t+πt⊤​σ​(Yt,θ)​d​Wt,\frac{dX\_{t}^{\pi}}{X\_{t}^{\pi}}=\Big(r+\pi\_{t}^{\top}b(Y\_{t},\theta)\Big)dt+\pi\_{t}^{\top}\sigma(Y\_{t},\theta)\,dW\_{t}, |  | (12) |

and we denote by 𝒜obs\mathcal{A}^{\mathrm{obs}} the set of progressively measurable portfolio processes adapted to (ℱtobs)(\mathcal{F}\_{t}^{\mathrm{obs}}) for which ([12](https://arxiv.org/html/2601.03175v1#S2.E12 "Equation 12 ‣ Wealth dynamics and admissibility (given 𝜃). ‣ 2.1 Model and ex–ante objective in estimated diffusion markets ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) admits a (strictly) positive wealth solution. In the Markovian feedback case π∈𝒜fb\pi\in\mathcal{A}^{\mathrm{fb}} one may think of πt=π¯​(t,Xt,Yt)\pi\_{t}=\bar{\pi}(t,X\_{t},Y\_{t}).

##### Ex–ante objective under latent θ\theta (and simulator viewpoint).

The investor evaluates policies under an *ex–ante* objective that averages over both diffusion noise for fixed θ\theta and the parametric uncertainty encoded by ([9](https://arxiv.org/html/2601.03175v1#S2.E9 "Equation 9 ‣ Uncertainty law 𝑞⁢(𝑑⁢𝜃) and information structure. ‣ 2.1 Model and ex–ante objective in estimated diffusion markets ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(π):=𝔼θ∼q​[𝔼​[U​(XTπ)|θ]]=∫Θ𝔼​[U​(XTπ)|θ]​q​(d​θ).J(\pi):=\mathbb{E}\_{\theta\sim q}\bigg[\mathbb{E}\big[U(X\_{T}^{\pi})\,\big|\,\theta\big]\bigg]=\int\_{\Theta}\mathbb{E}\big[U(X\_{T}^{\pi})\,\big|\,\theta\big]\,q(d\theta). |  | (13) |

The corresponding optimization problem (under our feedback restriction) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | supπ∈𝒜fbJ​(π).\sup\_{\pi\in\mathcal{A}^{\mathrm{fb}}}J(\pi). |  | (14) |

Whenever it exists, we denote by

|  |  |  |
| --- | --- | --- |
|  | π⋆,blind∈arg⁡maxπ∈𝒜fb⁡J​(π)\pi^{\star,\mathrm{blind}}\in\arg\max\_{\pi\in\mathcal{A}^{\mathrm{fb}}}J(\pi) |  |

an optimal θ\theta-blind feedback for the fixed-qq commitment problem ([14](https://arxiv.org/html/2601.03175v1#S2.E14 "Equation 14 ‣ Ex–ante objective under latent 𝜃 (and simulator viewpoint). ‣ 2.1 Model and ex–ante objective in estimated diffusion markets ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")). For each fixed θ\theta, we also write π⋆,θ\pi^{\star,\theta} for the (infeasible) θ\theta-conditional *full-information* optimal control that would be available if θ\theta were observed.

The θ\theta-blind constraint makes ([14](https://arxiv.org/html/2601.03175v1#S2.E14 "Equation 14 ‣ Ex–ante objective under latent 𝜃 (and simulator viewpoint). ‣ 2.1 Model and ex–ante objective in estimated diffusion markets ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) strictly harder than solving a separate control problem for each fixed θ\theta, since the latter yields a θ\theta-indexed full-information family. Ex–ante averaging in ([13](https://arxiv.org/html/2601.03175v1#S2.E13 "Equation 13 ‣ Ex–ante objective under latent 𝜃 (and simulator viewpoint). ‣ 2.1 Model and ex–ante objective in estimated diffusion markets ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) can also create gradient cancellation across heterogeneous parameter draws when one attempts to learn a single global policy end-to-end. While an ℱtobs\mathcal{F}\_{t}^{\mathrm{obs}}-adapted policy could, in principle, filter θ\theta online and solve a belief-state control problem (see, e.g., bensoussan1985optimal; pham2017dynamic), we do *not* pursue that formulation here.

Approximating the outer expectation in ([13](https://arxiv.org/html/2601.03175v1#S2.E13 "Equation 13 ‣ Ex–ante objective under latent 𝜃 (and simulator viewpoint). ‣ 2.1 Model and ex–ante objective in estimated diffusion markets ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) amounts to sampling θ∼q\theta\sim q *inside the simulator* (once per trajectory or once per update), running ([6](https://arxiv.org/html/2601.03175v1#S2.E6 "Equation 6 ‣ Estimated diffusion market family (conditional on a latent parameter). ‣ 2.1 Model and ex–ante objective in estimated diffusion markets ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"))–([7](https://arxiv.org/html/2601.03175v1#S2.E7 "Equation 7 ‣ Estimated diffusion market family (conditional on a latent parameter). ‣ 2.1 Model and ex–ante objective in estimated diffusion markets ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) under that frozen draw, and updating a θ\theta-blind feedback policy to perform well *on average* over such draws. This is the setting targeted by the simulation-based PG–DPO and P–PGDPO methods developed in Section [3](https://arxiv.org/html/2601.03175v1#S3 "3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection").

### 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions

This subsection records the Hamiltonian structure underlying our projection step and clarifies what “Pontryagin first-order conditions”
mean when the market parameter θ\theta is latent and admissible controls are θ\theta-blind. In particular, we distinguish between
(i) *θ\theta-conditional* (full-information) criticality conditions that would apply if θ\theta were observable (and are therefore infeasible
under latent θ\theta), and (ii) *qq-aggregated* criticality conditions that characterize stationarity *within the θ\theta-blind admissible
class* for the fixed-qq ex–ante objective. Our discussion follows standard stochastic control/PMP arguments for diffusion control
(e.g. yong1999stochastic; fleming2006controlled; pham2009continuous). We also comment on the relationship to partial-information (belief-state)
PMP, but we do not develop that formulation here.

##### A θ\theta-conditional (full-information) Hamiltonian and first-order condition (infeasible under latent θ\theta).

Fix θ∈Θ\theta\in\Theta and suppose, for the moment, that θ\theta were observable to the controller. In Markovian settings with sufficient
smoothness, the θ\theta-conditional value function V⋆,θ​(t,x,y)V^{\star,\theta}(t,x,y) satisfies an HJB equation whose *control Hamiltonian*
(the part depending on π\pi) can be written explicitly using ([8](https://arxiv.org/html/2601.03175v1#S2.E8 "Equation 8 ‣ Estimated diffusion market family (conditional on a latent parameter). ‣ 2.1 Model and ex–ante objective in estimated diffusion markets ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℋθctrl​(t,x,y,π;Vx,Vx​x,Vx​y):=x​π⊤​b​(y,θ)​Vx+12​x2​π⊤​Σ​(y,θ)​π​Vx​x+x​π⊤​ΣS​Y​(y,θ)​Vx​y,\mathcal{H}\_{\theta}^{\mathrm{ctrl}}(t,x,y,\pi;\,V\_{x},V\_{xx},V\_{xy}):=x\,\pi^{\top}b(y,\theta)\,V\_{x}+\frac{1}{2}x^{2}\,\pi^{\top}\Sigma(y,\theta)\,\pi\,V\_{xx}+x\,\pi^{\top}\Sigma\_{SY}(y,\theta)\,V\_{xy}, |  | (15) |

where Vx,Vx​xV\_{x},V\_{xx} are evaluated at (t,x,y)(t,x,y) and Vx​y​(t,x,y)∈ℝmV\_{xy}(t,x,y)\in\mathbb{R}^{m}. The last term in ([15](https://arxiv.org/html/2601.03175v1#S2.E15 "Equation 15 ‣ A 𝜃-conditional (full-information) Hamiltonian and first-order condition (infeasible under latent 𝜃). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) is the
return–factor hedging term induced by d​⟨W,WY⟩≠0d\langle W,W^{Y}\rangle\neq 0.

The pointwise first-order condition for an interior optimizer is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂πℋθctrl=x​Vx⋆,θ​b​(y,θ)+x2​Vx​x⋆,θ​Σ​(y,θ)​π+x​ΣS​Y​(y,θ)​Vx​y⋆,θ= 0.\partial\_{\pi}\mathcal{H}\_{\theta}^{\mathrm{ctrl}}=x\,V\_{x}^{\star,\theta}\,b(y,\theta)+x^{2}\,V\_{xx}^{\star,\theta}\,\Sigma(y,\theta)\,\pi+x\,\Sigma\_{SY}(y,\theta)\,V\_{xy}^{\star,\theta}\;=\;0. |  | (16) |

Assuming Σ​(y,θ)\Sigma(y,\theta) is invertible and Vx​x⋆,θ<0V\_{xx}^{\star,\theta}<0, this yields the closed-form θ\theta-conditional full-information portfolio rule

|  |  |  |  |
| --- | --- | --- | --- |
|  | π⋆,θ​(t,x,y)=−1x​Vx​x⋆,θ​(t,x,y)​Σ​(y,θ)−1​(Vx⋆,θ​(t,x,y)​b​(y,θ)+ΣS​Y​(y,θ)​Vx​y⋆,θ​(t,x,y)).\pi^{\star,\theta}(t,x,y)=-\,\frac{1}{x\,V\_{xx}^{\star,\theta}(t,x,y)}\,\Sigma(y,\theta)^{-1}\Big(V\_{x}^{\star,\theta}(t,x,y)\,b(y,\theta)+\Sigma\_{SY}(y,\theta)\,V\_{xy}^{\star,\theta}(t,x,y)\Big). |  | (17) |

This θ\theta-indexed rule is *not deployable* under latent parameters; we record it only as a full-information benchmark and diagnostic reference.
In our setting, deployable policies never take the realized θ\theta as an input; θ\theta is accessed only through sampling inside the simulator when
approximating qq-expectations.

##### qq-aggregated Pontryagin condition for the θ\theta-blind ex–ante problem (Markov feedback).

We now return to the actual setting: θ\theta is latent, policies are θ\theta-blind, and we restrict attention to the Markov feedback class
𝒜fb\mathcal{A}^{\mathrm{fb}} (Remark [1](https://arxiv.org/html/2601.03175v1#Thmremark1 "Remark 1 (Latent parameter, observability, and admissible controls). ‣ Uncertainty law 𝑞⁢(𝑑⁢𝜃) and information structure. ‣ 2.1 Model and ex–ante objective in estimated diffusion markets ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")). Under this restriction we neither perform online filtering of θ\theta nor replace
qq by a time-varying posterior distribution. Accordingly, the relevant Pontryagin condition is not the θ\theta-conditional criticality
([16](https://arxiv.org/html/2601.03175v1#S2.E16 "Equation 16 ‣ A 𝜃-conditional (full-information) Hamiltonian and first-order condition (infeasible under latent 𝜃). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) enforced pointwise in θ\theta, but rather a necessary condition for optimality *within the θ\theta-blind
admissible class* for the fixed-qq objective ([13](https://arxiv.org/html/2601.03175v1#S2.E13 "Equation 13 ‣ Ex–ante objective under latent 𝜃 (and simulator viewpoint). ‣ 2.1 Model and ex–ante objective in estimated diffusion markets ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).

To see why ex–ante aggregation enters the first-order condition, take any θ\theta-blind admissible perturbation h={ht}t∈[0,T]h=\{h\_{t}\}\_{t\in[0,T]}
that is progressively measurable with respect to the observation filtration (ℱtobs)(\mathcal{F}\_{t}^{\mathrm{obs}}) and square-integrable, and define
πε:=π+ε​h\pi^{\varepsilon}:=\pi+\varepsilon h for small ε\varepsilon. For each fixed θ\theta, the stochastic maximum principle yields the first-variation
identity

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​ε​Jθ​(πε)|ε=0=𝔼​[∫0T∂πℋθctrl​(t,Xt,Yt,πt;ptθ,px,tθ,py,tθ)⊤​ht​d​t|θ],\left.\frac{d}{d\varepsilon}J^{\theta}(\pi^{\varepsilon})\right|\_{\varepsilon=0}=\mathbb{E}\!\left[\int\_{0}^{T}\partial\_{\pi}\mathcal{H}^{\mathrm{ctrl}}\_{\theta}\big(t,X\_{t},Y\_{t},\pi\_{t};\,p\_{t}^{\theta},p\_{x,t}^{\theta},p\_{y,t}^{\theta}\big)^{\top}h\_{t}\,dt\,\Big|\,\theta\right], |  | (18) |

where (ptθ,px,tθ,py,tθ)\big(p\_{t}^{\theta},p\_{x,t}^{\theta},p\_{y,t}^{\theta}\big) denotes the θ\theta-conditional Pontryagin sensitivity objects associated with the
*fixed* policy π\pi in the frozen-θ\theta market. Because both π\pi and hh are θ\theta-blind, taking the outer expectation over
θ∼q\theta\sim q and using Fubini’s theorem gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​ε​J​(πε)|ε=0=𝔼​[∫0T𝔼θ∼q​[∂πℋθctrl​(t,Xt,Yt,πt;ptθ,px,tθ,py,tθ)]⊤​ht​𝑑t].\left.\frac{d}{d\varepsilon}J(\pi^{\varepsilon})\right|\_{\varepsilon=0}=\mathbb{E}\!\left[\int\_{0}^{T}\mathbb{E}\_{\theta\sim q}\!\Big[\partial\_{\pi}\mathcal{H}^{\mathrm{ctrl}}\_{\theta}\big(t,X\_{t},Y\_{t},\pi\_{t};\,p\_{t}^{\theta},p\_{x,t}^{\theta},p\_{y,t}^{\theta}\big)\Big]^{\top}h\_{t}\,dt\right]. |  | (19) |

Hence, for an interior θ\theta-blind optimum π⋆,blind\pi^{\star,\mathrm{blind}}, the first variation must vanish for all such perturbations hh,
which implies the aggregated first-order condition

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼θ∼q​[∂πℋθctrl​(t,Xt,Yt,πt;ptθ,px,tθ,py,tθ)]=0,a.s. for a.e. ​t∈[0,T].\mathbb{E}\_{\theta\sim q}\!\Big[\partial\_{\pi}\mathcal{H}^{\mathrm{ctrl}}\_{\theta}\big(t,X\_{t},Y\_{t},\pi\_{t};\,p\_{t}^{\theta},p\_{x,t}^{\theta},p\_{y,t}^{\theta}\big)\Big]=0,\hskip 18.49988pt\text{a.s.\ for a.e.\ }t\in[0,T]. |  | (20) |

Equation ([20](https://arxiv.org/html/2601.03175v1#S2.E20 "Equation 20 ‣ 𝑞-aggregated Pontryagin condition for the 𝜃-blind ex–ante problem (Markov feedback). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) is the correct necessary condition for the ex–ante problem under the θ\theta-blind constraint. In
particular, it is generally distinct from imposing ([16](https://arxiv.org/html/2601.03175v1#S2.E16 "Equation 16 ‣ A 𝜃-conditional (full-information) Hamiltonian and first-order condition (infeasible under latent 𝜃). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) for each θ\theta separately, because θ\theta-conditional
criticality cannot be enforced by a single deployable θ\theta-blind policy.

To operationalize ([20](https://arxiv.org/html/2601.03175v1#S2.E20 "Equation 20 ‣ 𝑞-aggregated Pontryagin condition for the 𝜃-blind ex–ante problem (Markov feedback). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) in the Markov feedback class, fix a feedback policy π∈𝒜fb\pi\in\mathcal{A}^{\mathrm{fb}} and,
for each frozen θ\theta, consider the corresponding θ\theta-conditional Pontryagin sensitivity objects
(ptθ,px,tθ,py,tθ)\big(p\_{t}^{\theta},p\_{x,t}^{\theta},p\_{y,t}^{\theta}\big) along the induced state process. In smooth Markov regimes these coincide with spatial
derivatives of a decoupling field and, in particular, reduce to (Vx,Vx​x,Vx​y)(V\_{x},V\_{xx},V\_{xy}) in the full-information setting; in our algorithms we estimate
them pathwise by automatic differentiation (see Section [3](https://arxiv.org/html/2601.03175v1#S3 "3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).

For the portfolio Hamiltonian ([15](https://arxiv.org/html/2601.03175v1#S2.E15 "Equation 15 ‣ A 𝜃-conditional (full-information) Hamiltonian and first-order condition (infeasible under latent 𝜃). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")), ∂πℋθctrl\partial\_{\pi}\mathcal{H}\_{\theta}^{\mathrm{ctrl}} is affine in π\pi. This motivates
defining the θ\theta-conditional “projection inputs”

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Atθ​(t,x,y)\displaystyle A\_{t}^{\theta}(t,x,y) | :=x​px,tθ​(t,x,y)​Σ​(y,θ)∈ℝd×d,\displaystyle:=x\,p\_{x,t}^{\theta}(t,x,y)\,\Sigma(y,\theta)\in\mathbb{R}^{d\times d}, |  | (21) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Gtθ​(t,x,y)\displaystyle G\_{t}^{\theta}(t,x,y) | :=ptθ​(t,x,y)​b​(y,θ)+ΣS​Y​(y,θ)​py,tθ​(t,x,y)∈ℝd,\displaystyle:=p\_{t}^{\theta}(t,x,y)\,b(y,\theta)+\Sigma\_{SY}(y,\theta)\,p\_{y,t}^{\theta}(t,x,y)\in\mathbb{R}^{d}, |  | (22) |

and their qq-aggregated counterparts

|  |  |  |  |
| --- | --- | --- | --- |
|  | At​(t,x,y):=𝔼θ∼q​[Atθ​(t,x,y)],Gt​(t,x,y):=𝔼θ∼q​[Gtθ​(t,x,y)].A\_{t}(t,x,y):=\mathbb{E}\_{\theta\sim q}\!\big[A\_{t}^{\theta}(t,x,y)\big],\hskip 18.49988ptG\_{t}(t,x,y):=\mathbb{E}\_{\theta\sim q}\!\big[G\_{t}^{\theta}(t,x,y)\big]. |  | (23) |

These objects summarize how the latent parameter affects the first-order stationarity condition through the
θ\theta-conditional sensitivities.

###### Theorem 1 (qq-aggregated first-order condition under latent θ\theta (deployable θ\theta-blind stationarity)).

Consider the fixed-qq ex–ante objective ([13](https://arxiv.org/html/2601.03175v1#S2.E13 "Equation 13 ‣ Ex–ante objective under latent 𝜃 (and simulator viewpoint). ‣ 2.1 Model and ex–ante objective in estimated diffusion markets ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) over the θ\theta-blind Markov feedback class 𝒜fb\mathcal{A}^{\mathrm{fb}}.
Assume standard smoothness/integrability conditions ensuring validity of first variations within 𝒜fb\mathcal{A}^{\mathrm{fb}} and existence of the
associated θ\theta-conditional Pontryagin objects.
If π⋆,blind\pi^{\star,\mathrm{blind}} is a locally optimal interior policy in 𝒜fb\mathcal{A}^{\mathrm{fb}}, then ([20](https://arxiv.org/html/2601.03175v1#S2.E20 "Equation 20 ‣ 𝑞-aggregated Pontryagin condition for the 𝜃-blind ex–ante problem (Markov feedback). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) holds.
Moreover, in the portfolio setting ([15](https://arxiv.org/html/2601.03175v1#S2.E15 "Equation 15 ‣ A 𝜃-conditional (full-information) Hamiltonian and first-order condition (infeasible under latent 𝜃). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")), the aggregated stationarity is equivalent to the statewise linear system

|  |  |  |  |
| --- | --- | --- | --- |
|  | At​(t,x,y)​π⋆,blind​(t,x,y)=−Gt​(t,x,y),(t,x,y)∈[0,T]×(0,∞)×ℝm,A\_{t}(t,x,y)\,\pi^{\star,\mathrm{blind}}(t,x,y)=-\,G\_{t}(t,x,y),\hskip 18.49988pt(t,x,y)\in[0,T]\times(0,\infty)\times\mathbb{R}^{m}, |  | (24) |

(where At,GtA\_{t},G\_{t} are defined by ([23](https://arxiv.org/html/2601.03175v1#S2.E23 "Equation 23 ‣ 𝑞-aggregated Pontryagin condition for the 𝜃-blind ex–ante problem (Markov feedback). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) using the θ\theta-conditional Pontryagin objects generated by π⋆,blind\pi^{\star,\mathrm{blind}}).
Whenever At​(t,x,y)A\_{t}(t,x,y) is invertible on the working domain, ([24](https://arxiv.org/html/2601.03175v1#S2.E24 "Equation 24 ‣ Theorem 1 (𝑞-aggregated first-order condition under latent 𝜃 (deployable 𝜃-blind stationarity)). ‣ 𝑞-aggregated Pontryagin condition for the 𝜃-blind ex–ante problem (Markov feedback). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) is equivalently expressed as the projected feedback rule

|  |  |  |  |
| --- | --- | --- | --- |
|  | πagg​(t,x,y)=−At​(t,x,y)−1​Gt​(t,x,y).\pi^{\mathrm{agg}}(t,x,y)=-\,A\_{t}(t,x,y)^{-1}\,G\_{t}(t,x,y). |  | (25) |

###### Proof sketch.

The conditional first-variation identity ([18](https://arxiv.org/html/2601.03175v1#S2.E18 "Equation 18 ‣ 𝑞-aggregated Pontryagin condition for the 𝜃-blind ex–ante problem (Markov feedback). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) is standard for diffusion control under a fixed parameter θ\theta
(e.g. yong1999stochastic; fleming2006controlled; pham2009continuous). Taking the outer expectation over θ∼q\theta\sim q yields
([19](https://arxiv.org/html/2601.03175v1#S2.E19 "Equation 19 ‣ 𝑞-aggregated Pontryagin condition for the 𝜃-blind ex–ante problem (Markov feedback). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")). Since hh is an arbitrary θ\theta-blind admissible perturbation, vanishing of the first variation at an interior
optimum implies ([20](https://arxiv.org/html/2601.03175v1#S2.E20 "Equation 20 ‣ 𝑞-aggregated Pontryagin condition for the 𝜃-blind ex–ante problem (Markov feedback). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")). For the quadratic portfolio Hamiltonian ([15](https://arxiv.org/html/2601.03175v1#S2.E15 "Equation 15 ‣ A 𝜃-conditional (full-information) Hamiltonian and first-order condition (infeasible under latent 𝜃). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")), substituting the explicit expression
for ∂πℋθctrl\partial\_{\pi}\mathcal{H}^{\mathrm{ctrl}}\_{\theta} and introducing ([21](https://arxiv.org/html/2601.03175v1#S2.E21 "Equation 21 ‣ 𝑞-aggregated Pontryagin condition for the 𝜃-blind ex–ante problem (Markov feedback). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"))–([23](https://arxiv.org/html/2601.03175v1#S2.E23 "Equation 23 ‣ 𝑞-aggregated Pontryagin condition for the 𝜃-blind ex–ante problem (Markov feedback). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) yields the linear
system ([24](https://arxiv.org/html/2601.03175v1#S2.E24 "Equation 24 ‣ Theorem 1 (𝑞-aggregated first-order condition under latent 𝜃 (deployable 𝜃-blind stationarity)). ‣ 𝑞-aggregated Pontryagin condition for the 𝜃-blind ex–ante problem (Markov feedback). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) and the projected form ([25](https://arxiv.org/html/2601.03175v1#S2.E25 "Equation 25 ‣ Theorem 1 (𝑞-aggregated first-order condition under latent 𝜃 (deployable 𝜃-blind stationarity)). ‣ 𝑞-aggregated Pontryagin condition for the 𝜃-blind ex–ante problem (Markov feedback). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) whenever AtA\_{t} is invertible.
∎

Note that πagg\pi^{\mathrm{agg}} is generally *not* equal to the naive average 𝔼θ∼q​[π⋆,θ​(t,x,y)]\mathbb{E}\_{\theta\sim q}[\pi^{\star,\theta}(t,x,y)] of θ\theta-conditional full-information controls, reflecting the noncommutativity between averaging over θ\theta and solving a first-order condition. In particular, even if one could compute π⋆,θ\pi^{\star,\theta} for each θ\theta, averaging these infeasible oracles does not, in general, enforce the deployable qq-aggregated stationarity ([20](https://arxiv.org/html/2601.03175v1#S2.E20 "Equation 20 ‣ 𝑞-aggregated Pontryagin condition for the 𝜃-blind ex–ante problem (Markov feedback). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).

###### Remark 2 (Relation to belief-state/learning formulations).

If one allows history-dependent policies that explicitly infer θ\theta from observed returns, a principled partial-information formulation introduces
a time-varying posterior/belief state qt(⋅)=ℙ(θ∈⋅∣ℱtobs)q\_{t}(\cdot)=\mathbb{P}(\theta\in\cdot\mid\mathcal{F}\_{t}^{\mathrm{obs}}). In such belief-state problems, the
corresponding PMP/Hamiltonian criticality condition is expressed in terms of conditional expectations under qtq\_{t} (or, equivalently, conditional on
ℱtobs\mathcal{F}\_{t}^{\mathrm{obs}}); see, e.g., haussmann1987maximum; li1995general; baghery2007maximum. We do not pursue that learning/belief-state
route here. Our algorithms and theory target the fixed-qq, qq-aggregated projection ([25](https://arxiv.org/html/2601.03175v1#S2.E25 "Equation 25 ‣ Theorem 1 (𝑞-aggregated first-order condition under latent 𝜃 (deployable 𝜃-blind stationarity)). ‣ 𝑞-aggregated Pontryagin condition for the 𝜃-blind ex–ante problem (Markov feedback). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) under the θ\theta-blind Markov feedback
restriction ([52](https://arxiv.org/html/2601.03175v1#S3.E52 "Equation 52 ‣ Setup and objectives (frozen 𝜃, deployable 𝜃-blind feedback). ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).

### 2.3 Gaussian references at a fixed decision time

This subsection collects Gaussian benchmarks that isolate *decision-time statistical uncertainty* and yield closed-form reference allocations.
We fix a calendar decision time t0t\_{0} at which an external estimation pipeline outputs an uncertainty law qt0​(d​θ)q\_{t\_{0}}(d\theta) for a risk-premium parameter,
and we treat this law as an ℱt0\mathcal{F}\_{t\_{0}}-measurable *input* for portfolio choice over the remaining horizon.
This interface accommodates both Bayesian posterior/prior-like uncertainty descriptions (e.g., barberis2000investor; pastor2000portfolio)
and frequentist sampling/resampling laws conditional on ℱt0\mathcal{F}\_{t\_{0}} (e.g., bootstrap or bagging) (e.g., efron1979bootstrap; efron1994bootstrap; breiman1996bagging).
Throughout this subsection we work conditionally on ℱt0\mathcal{F}\_{t\_{0}}, suppress conditioning by writing q​(d​θ)q(d\theta), and shift the trading clock so that
the decision time becomes 0 and the remaining horizon is TT.
These references are used as analytic targets and sanity checks for our numerical sections (Sections [4](https://arxiv.org/html/2601.03175v1#S4 "4 Breaking the Dimensional Barrier under Drift Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection") and [5](https://arxiv.org/html/2601.03175v1#S5 "5 Recovering Intertemporal Hedging Demand in Factor-Driven Markets ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")),
rather than as characterizations of the unrestricted optimum of ([14](https://arxiv.org/html/2601.03175v1#S2.E14 "Equation 14 ‣ Ex–ante objective under latent 𝜃 (and simulator viewpoint). ‣ 2.1 Model and ex–ante objective in estimated diffusion markets ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) over the full feedback class.

We present two decision-time references.
Section [2.3.1](https://arxiv.org/html/2601.03175v1#S2.SS3.SSS1 "2.3.1 Static Gaussian drift uncertainty ‣ 2.3 Gaussian references at a fixed decision time ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection") considers *static* drift uncertainty: a latent premium is drawn from qq once at time 0 and kept fixed on [0,T][0,T],
providing the controlled benchmark used in the high-dimensional scaling/geometry experiments of Section [4](https://arxiv.org/html/2601.03175v1#S4 "4 Breaking the Dimensional Barrier under Drift Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection").
Section [2.3.2](https://arxiv.org/html/2601.03175v1#S2.SS3.SSS2 "2.3.2 Mean-reverting Gaussian premium and an induced horizon-dependent reference ‣ 2.3 Gaussian references at a fixed decision time ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection") considers a mean-reverting (OU) premium with Gaussian initial uncertainty, which induces a horizon-dependent Gaussian law
for the *time-averaged* premium and yields a tractable closed-form reference used in the hedging-demand recovery study of Section [5](https://arxiv.org/html/2601.03175v1#S5 "5 Recovering Intertemporal Hedging Demand in Factor-Driven Markets ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection").
For completeness, an online linear–Gaussian illustration that produces a time-varying uncertainty law qtq\_{t} via Kalman–Bucy filtering is deferred to
Appendix [A](https://arxiv.org/html/2601.03175v1#A1 "Appendix A Online uncertainty updates: Kalman–Bucy filtering and a plug-in decision-time benchmark ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"); it is included only to motivate a *plug-in* (receding-horizon) decision-time workflow in which qtq\_{t} is treated as an
externally updated input at each decision time, rather than solving the fully optimal belief-state control problem (e.g., bensoussan1985optimal; pham2017dynamic).

#### 2.3.1 Static Gaussian drift uncertainty

We start from a time-homogeneous Gaussian benchmark in which the (vector) risk premium is an
unobserved *static* parameter drawn at the decision time. The agent commits to a single
θ\theta-blind policy, and all ex–ante uncertainty is summarized by the decision-time law qq.

##### Market model (static latent drift).

Let dd risky assets satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​StSt=r​ 1​d​t+θ​d​t+Σ1/2​d​Wt,S0∈(0,∞)d,\frac{dS\_{t}}{S\_{t}}=r\,\mathbf{1}\,dt+\theta\,dt+\Sigma^{1/2}dW\_{t},\hskip 18.49988ptS\_{0}\in(0,\infty)^{d}, |  | (26) |

where Σ∈ℝd×d\Sigma\in\mathbb{R}^{d\times d} is symmetric positive definite and the latent excess-return
vector is drawn at time 0 as

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ∼q​(d​θ).\theta\sim q(d\theta). |  | (27) |

A θ\theta-blind portfolio fraction process πt∈ℝd\pi\_{t}\in\mathbb{R}^{d} generates wealth

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​XtπXtπ=(r+πt⊤​θ)​d​t+πt⊤​Σ1/2​d​Wt,X0π=x>0,\frac{dX\_{t}^{\pi}}{X\_{t}^{\pi}}=\big(r+\pi\_{t}^{\top}\theta\big)\,dt+\pi\_{t}^{\top}\Sigma^{1/2}\,dW\_{t},\hskip 18.49988ptX\_{0}^{\pi}=x>0, |  | (28) |

and we evaluate the ex–ante objective

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(π):=𝔼θ∼q​[𝔼​[U​(XTπ)∣θ]].J(\pi):=\mathbb{E}\_{\theta\sim q}\Big[\mathbb{E}\big[U(X\_{T}^{\pi})\mid\theta\big]\Big]. |  | (29) |

For reference, under full information and CRRA utility U​(x)=x1−γ/(1−γ)U(x)=x^{1-\gamma}/(1-\gamma)
(γ>0,γ≠1\gamma>0,\gamma\neq 1), the oracle Merton rule is
π⋆​(θ)=1γ​Σ−1​θ\pi^{\star}(\theta)=\frac{1}{\gamma}\Sigma^{-1}\theta
(merton1969lifetime; merton1971optimum), which is infeasible here because θ\theta is latent.

Analytic qq-references via constant portfolios.
To obtain a transparent closed-form benchmark that depends *only* on the decision-time law qq,
we temporarily restrict attention to constant portfolio fractions

|  |  |  |  |
| --- | --- | --- | --- |
|  | πt≡π∈ℝd.\pi\_{t}\equiv\pi\in\mathbb{R}^{d}. |  | (30) |

This restriction is used solely to define an analytic qq-reference; it is *not* imposed on the
learning problem.

##### Log utility (γ=1\gamma=1).

Let mθ:=𝔼θ∼q​[θ]m\_{\theta}:=\mathbb{E}\_{\theta\sim q}[\theta]. For constant π\pi, the objective depends on qq
only through mθm\_{\theta}, and the optimal constant portfolio is

|  |  |  |  |
| --- | --- | --- | --- |
|  | πq,logconst​(T)=Σ−1​mθ,\pi\_{q,\log}^{\mathrm{const}}(T)=\Sigma^{-1}m\_{\theta}, |  | (31) |

which is independent of TT in this static benchmark. In the one-asset case (d=1d=1,
Σ=σ2\Sigma=\sigma^{2}),

|  |  |  |  |
| --- | --- | --- | --- |
|  | πq,logconst​(T)=mθσ2.\pi\_{q,\log}^{\mathrm{const}}(T)=\frac{m\_{\theta}}{\sigma^{2}}. |  | (32) |

##### CRRA (γ≠1\gamma\neq 1): tilted optimality and Gaussian shrinkage.

For γ≠1\gamma\neq 1 and constant π\pi, conditional on θ\theta the terminal wealth is lognormal, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(π)=x1−γ1−γ​exp⁡{(1−γ)​r​T−12​γ​(1−γ)​T​π⊤​Σ​π}​Mq​((1−γ)​T​π),J(\pi)=\frac{x^{1-\gamma}}{1-\gamma}\,\exp\Big\{(1-\gamma)rT-\tfrac{1}{2}\gamma(1-\gamma)T\,\pi^{\top}\Sigma\pi\Big\}\,M\_{q}\big((1-\gamma)T\pi\big), |  | (33) |

where Mq​(u):=𝔼θ∼q​[exp⁡(u⊤​θ)]M\_{q}(u):=\mathbb{E}\_{\theta\sim q}[\exp(u^{\top}\theta)] is the moment generating function of qq.
Any interior optimizer πq,γconst​(T)\pi\_{q,\gamma}^{\mathrm{const}}(T) satisfies the tilted first-order condition

|  |  |  |  |
| --- | --- | --- | --- |
|  | γ​Σ​πq,γconst​(T)=∇ulog⁡Mq​(u)|u=(1−γ)​T​πq,γconst​(T).\gamma\,\Sigma\,\pi\_{q,\gamma}^{\mathrm{const}}(T)=\nabla\_{u}\log M\_{q}(u)\Big|\_{u=(1-\gamma)T\,\pi\_{q,\gamma}^{\mathrm{const}}(T)}. |  | (34) |

If qq is Gaussian,

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ∼𝒩​(mθ,P),P⪰0,\theta\sim\mathcal{N}(m\_{\theta},P),\hskip 18.49988ptP\succeq 0, |  | (35) |

then ∇ulog⁡Mq​(u)=mθ+P​u\nabla\_{u}\log M\_{q}(u)=m\_{\theta}+Pu and the reference reduces to the linear system

|  |  |  |  |
| --- | --- | --- | --- |
|  | (γ​Σ−(1−γ)​T​P)​πq,γconst​(T)=mθ,\big(\gamma\Sigma-(1-\gamma)T\,P\big)\,\pi\_{q,\gamma}^{\mathrm{const}}(T)=m\_{\theta}, |  | (36) |

hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | πq,γconst​(T)=(γ​Σ−(1−γ)​T​P)−1​mθ.\pi\_{q,\gamma}^{\mathrm{const}}(T)=\big(\gamma\Sigma-(1-\gamma)T\,P\big)^{-1}m\_{\theta}. |  | (37) |

For γ>1\gamma>1, this takes the familiar shrinkage form

|  |  |  |  |
| --- | --- | --- | --- |
|  | πq,γconst​(T)=(γ​Σ+(γ−1)​T​P)−1​mθ,(γ>1),\pi\_{q,\gamma}^{\mathrm{const}}(T)=\big(\gamma\Sigma+(\gamma-1)T\,P\big)^{-1}m\_{\theta},\hskip 18.49988pt(\gamma>1), |  | (38) |

and in one dimension (d=1d=1, Σ=σ2\Sigma=\sigma^{2}, P=pP=p),

|  |  |  |  |
| --- | --- | --- | --- |
|  | πq,γconst​(T)=mθγ​σ2+(γ−1)​T​p,(γ>1).\pi\_{q,\gamma}^{\mathrm{const}}(T)=\frac{m\_{\theta}}{\gamma\sigma^{2}+(\gamma-1)T\,p},\hskip 18.49988pt(\gamma>1). |  | (39) |

#### 2.3.2 Mean-reverting Gaussian premium and an induced horizon-dependent reference

We next replace the static premium by a mean-reverting Gaussian premium process, a standard reduced-form
device for return predictability and intertemporal hedging (campbell2002strategic; xia2001learning).
Our goal here is *not* to introduce additional information structure, but to obtain a closed-form,
decision-time Gaussian reference for the *time-averaged* premium over the remaining horizon. This
induces a horizon-dependent effective premium law that can be used as a controlled analytic input in
numerical experiments.

##### OU premium dynamics and decision-time uncertainty.

Let the uncertain initial state be ϑ\vartheta and set Y0=ϑ∼𝒩​(m0,P0)Y\_{0}=\vartheta\sim\mathcal{N}(m\_{0},P\_{0}), so the
decision-time law is q=𝒩​(m0,P0)q=\mathcal{N}(m\_{0},P\_{0}). The premium factor follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Yt=K​(y¯−Yt)​d​t+Ξ​d​WtY,Y0=ϑ∼𝒩​(m0,P0),dY\_{t}=K(\bar{y}-Y\_{t})\,dt+\Xi\,dW\_{t}^{Y},\hskip 18.49988ptY\_{0}=\vartheta\sim\mathcal{N}(m\_{0},P\_{0}), |  | (40) |

and risky excess returns satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Rt:=d​StSt−r​𝟏​d​t=B​Yt​d​t+Σ1/2​d​Wt,dR\_{t}:=\frac{dS\_{t}}{S\_{t}}-r\mathbf{1}\,dt=BY\_{t}\,dt+\Sigma^{1/2}\,dW\_{t}, |  | (41) |

allowing instantaneous correlation

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​⟨W,WY⟩t=ρ​d​t,ρ∈ℝd×m.d\langle W,W^{Y}\rangle\_{t}=\rho\,dt,\hskip 18.49988pt\rho\in\mathbb{R}^{d\times m}. |  | (42) |

##### Integrated premium and induced Gaussian law.

Define the integrated premium

|  |  |  |  |
| --- | --- | --- | --- |
|  | IT:=∫0TYs​𝑑s∈ℝm.I\_{T}:=\int\_{0}^{T}Y\_{s}\,ds\in\mathbb{R}^{m}. |  | (43) |

Since ([40](https://arxiv.org/html/2601.03175v1#S2.E40 "Equation 40 ‣ OU premium dynamics and decision-time uncertainty. ‣ 2.3.2 Mean-reverting Gaussian premium and an induced horizon-dependent reference ‣ 2.3 Gaussian references at a fixed decision time ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) is linear-Gaussian with Gaussian initial condition, ITI\_{T} is Gaussian.
Its mean and covariance are

|  |  |  |  |
| --- | --- | --- | --- |
|  | mI​(T)=𝔼​[IT]=T​y¯+K−1​(I−e−K​T)​(m0−y¯),m\_{I}(T)=\mathbb{E}[I\_{T}]=T\bar{y}+K^{-1}\big(I-e^{-KT}\big)\,(m\_{0}-\bar{y}), |  | (44) |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | CI​(T):=Cov​(IT)\displaystyle C\_{I}(T)=\mathrm{Cov}(I\_{T}) | =K−1​(I−e−K​T)​P0​(I−e−K​T)⊤​K−⊤\displaystyle=K^{-1}\big(I-e^{-KT}\big)\,P\_{0}\,\big(I-e^{-KT}\big)^{\top}K^{-\top} |  | (45) |
|  |  | +∫0TK−1​(I−e−K​(T−s))​Ξ​Ξ⊤​(I−e−K​(T−s))⊤​K−⊤​𝑑s.\displaystyle\qquad+\int\_{0}^{T}K^{-1}\big(I-e^{-K(T-s)}\big)\,\Xi\Xi^{\top}\,\big(I-e^{-K(T-s)}\big)^{\top}K^{-\top}\,ds. |  |

Notably, ([44](https://arxiv.org/html/2601.03175v1#S2.E44 "Equation 44 ‣ Integrated premium and induced Gaussian law. ‣ 2.3.2 Mean-reverting Gaussian premium and an induced horizon-dependent reference ‣ 2.3 Gaussian references at a fixed decision time ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"))–([45](https://arxiv.org/html/2601.03175v1#S2.E45 "Equation 45 ‣ Integrated premium and induced Gaussian law. ‣ 2.3.2 Mean-reverting Gaussian premium and an induced horizon-dependent reference ‣ 2.3 Gaussian references at a fixed decision time ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) depend only on the OU
dynamics and the decision-time uncertainty (m0,P0)(m\_{0},P\_{0}); they do not depend on the return–factor
correlation ρ\rho.

##### Horizon-averaged premium and effective Gaussian law.

Define the horizon-averaged effective premium

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ¯T:=1T​B​IT∈ℝd.\bar{\theta}\_{T}:=\frac{1}{T}\,B\,I\_{T}\in\mathbb{R}^{d}. |  | (46) |

Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ¯T∼𝒩​(mθ¯​(T),Pθ¯​(T)),mθ¯​(T)=1T​B​mI​(T),Pθ¯​(T)=1T2​B​CI​(T)​B⊤.\bar{\theta}\_{T}\sim\mathcal{N}(m\_{\bar{\theta}}(T),P\_{\bar{\theta}}(T)),\hskip 18.49988ptm\_{\bar{\theta}}(T)=\frac{1}{T}B\,m\_{I}(T),\hskip 18.49988ptP\_{\bar{\theta}}(T)=\frac{1}{T^{2}}B\,C\_{I}(T)\,B^{\top}. |  | (47) |

When ρ=0\rho=0, this induced law can be plugged directly into the static Gaussian reference of
Section [2.3.1](https://arxiv.org/html/2601.03175v1#S2.SS3.SSS1 "2.3.1 Static Gaussian drift uncertainty ‣ 2.3 Gaussian references at a fixed decision time ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"). When ρ≠0\rho\neq 0, the marginal law
([47](https://arxiv.org/html/2601.03175v1#S2.E47 "Equation 47 ‣ Horizon-averaged premium and effective Gaussian law. ‣ 2.3.2 Mean-reverting Gaussian premium and an induced horizon-dependent reference ‣ 2.3 Gaussian references at a fixed decision time ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) remains valid, but constant-portfolio expected utility involves an additional
cross-covariance term capturing the return–state shock linkage that generates hedging demand
(campbell2002strategic; xia2001learning).

##### Closed-form references under constant portfolios.

Restricting to constant fractions πt≡π\pi\_{t}\equiv\pi turns the problem into a transparent decision-time benchmark:
only the *integrated premium* IT=∫0TYs​𝑑sI\_{T}=\int\_{0}^{T}Y\_{s}\,ds enters the drift of log⁡XTπ\log X\_{T}^{\pi}, while the risk term remains
time-homogeneous. This yields a closed-form target that depends on the decision-time law q=𝒩​(m0,P0)q=\mathcal{N}(m\_{0},P\_{0}) only through
the induced mean mI​(T)=𝔼​[IT]m\_{I}(T)=\mathbb{E}[I\_{T}] (and, for CRRA, through covariances as well).

##### Log utility (γ=1\gamma=1).

With πt≡π\pi\_{t}\equiv\pi, the log-utility criterion reduces to a strictly concave quadratic in π\pi whose drift term depends on the OU factor only through the mean integrated premium mI​(T)=𝔼​[∫0TYs​𝑑s]m\_{I}(T)=\mathbb{E}\!\left[\int\_{0}^{T}Y\_{s}\,ds\right]. Hence the decision-time reference depends on q=𝒩​(m0,P0)q=\mathcal{N}(m\_{0},P\_{0}) only through mθ¯​(T)=(1/T)​B​mI​(T)m\_{\bar{\theta}}(T)=(1/T)B\,m\_{I}(T) (and, in particular, does not involve return–factor correlation), giving

|  |  |  |  |
| --- | --- | --- | --- |
|  | πq,logconst​(T)=Σ−1​mθ¯​(T)=1T​Σ−1​B​mI​(T).\pi\_{q,\log}^{\mathrm{const}}(T)=\Sigma^{-1}m\_{\bar{\theta}}(T)=\frac{1}{T}\,\Sigma^{-1}B\,m\_{I}(T). |  | (48) |

##### CRRA (γ>1\gamma>1).

Define

|  |  |  |  |
| --- | --- | --- | --- |
|  | CI​W​(T):=Cov​(IT,WT)=∫0TK−1​(I−e−K​(T−s))​Ξ​ρ⊤​𝑑s∈ℝm×d,C\_{IW}(T):=\mathrm{Cov}(I\_{T},W\_{T})=\int\_{0}^{T}K^{-1}\big(I-e^{-K(T-s)}\big)\,\Xi\,\rho^{\top}\,ds\;\in\;\mathbb{R}^{m\times d}, |  | (49) |

and the induced symmetric cross term

|  |  |  |  |
| --- | --- | --- | --- |
|  | Mcross​(T):=B​CI​W​(T)​(Σ1/2)⊤+Σ1/2​CI​W​(T)⊤​B⊤∈ℝd×d.M\_{\mathrm{cross}}(T):=B\,C\_{IW}(T)\,\big(\Sigma^{1/2}\big)^{\top}+\Sigma^{1/2}\,C\_{IW}(T)^{\top}\,B^{\top}\;\in\;\mathbb{R}^{d\times d}. |  | (50) |

Then the Gaussian-qq decision-time reference under constant portfolios is characterized by

|  |  |  |  |
| --- | --- | --- | --- |
|  | (γ​T​Σ+(γ−1)​(B​CI​(T)​B⊤+Mcross​(T)))​πq,γconst​(T)=B​mI​(T),(γ>1),\Big(\gamma T\Sigma+(\gamma-1)\big(B\,C\_{I}(T)\,B^{\top}+M\_{\mathrm{cross}}(T)\big)\Big)\,\pi\_{q,\gamma}^{\mathrm{const}}(T)=B\,m\_{I}(T),\hskip 18.49988pt(\gamma>1), |  | (51) |

equivalently

|  |  |  |
| --- | --- | --- |
|  | πq,γconst​(T)=(γ​T​Σ+(γ−1)​(B​CI​(T)​B⊤+Mcross​(T)))−1​B​mI​(T).\pi\_{q,\gamma}^{\mathrm{const}}(T)=\Big(\gamma T\Sigma+(\gamma-1)\big(B\,C\_{I}(T)\,B^{\top}+M\_{\mathrm{cross}}(T)\big)\Big)^{-1}B\,m\_{I}(T). |  |

When ρ=0\rho=0, we have CI​W​(T)=0C\_{IW}(T)=0 and Mcross​(T)=0M\_{\mathrm{cross}}(T)=0, recovering the independence-case
shrinkage reference.

### 2.4 Why dynamic programming and deep PDE surrogates break down in high-dimensional uncertain markets

This subsection explains why we do *not* treat classical dynamic programming (DP/HJB) or
value-function-based deep PDE surrogates (PINNs / deep BSDE methods) as practical baselines in the
high-dimensional uncertain markets targeted here. DP is conceptually sound in low-dimensional
Markovian settings (fleming2006controlled; pham2009continuous), but two issues dominate in our regime:
*(i)* numerically learning the value-function derivatives required for optimal policies becomes
prohibitive as dimension and nonlinearity grow, and *(ii)* principled parameter uncertainty
magnifies these difficulties.

Classical HJB: curse of dimensionality and full nonlinearity.
With deterministic parameters, DP leads to an HJB for V​(t,x,y)V(t,x,y) (fleming2006controlled).
Grid-based solvers scale exponentially in the state dimension (bellman1961adaptive; kushner2001numerical).
In portfolio problems with dd assets and mm factors, the natural state already has dimension m+2m+2,
so even modest discretizations require Nm+2N^{m+2} grid points. Moreover, constraints, transaction
costs, and non-affine dynamics typically yield *fully nonlinear* HJBs, where stable monotone
schemes are delicate even in moderate dimension and become impractical in the regime we target
(kushner2001numerical).

Deep PDE surrogates: fewer grids, same derivative bottleneck.
PINNs and deep BSDE methods replace grids with neural approximators trained on sampled points/paths
(raissi2019physics; sirignano2018dgm; han2018solving; beck2019machine), but for fully nonlinear
portfolio HJBs they remain value-function-based: they must implicitly learn high-dimensional
gradients/Hessians and, crucially, mixed sensitivities (e.g. Vx​yV\_{xy}) that drive intertemporal
hedging. In practice this induces nonconvex, ill-conditioned objectives (due to control
suprema and nonlinear derivative dependence) and training signals that do not reliably control the
specific derivative components needed for stable hedging demands in high dimension.

Latent parameter uncertainty: belief-state blowup and θ\theta-blind aggregation.
A principled DP treatment augments the state with a posterior/belief over parameters, leading to a
value function V​(t,x,y,Π)V(t,x,y,\Pi) on a space of measures in general (bensoussan1985optimal; pham2017dynamic).
Even when finite-dimensional conjugate summaries exist, the enlarged HJB is substantially harder.
For deep surrogates, uncertainty either requires solving many θ\theta-conditional problems (expensive)
or treating θ\theta as an extra input (higher effective dimension, worse conditioning). In our
deployable *θ\theta-blind* setting, a single policy must perform well under θ∼q\theta\sim q,
coupling heterogeneous models and potentially causing high-variance gradients and cancellation across
parameter draws.

We therefore avoid value-function PDE/BSDE baselines in this regime and instead work with a
qq-aggregated Pontryagin stationarity condition and projection map, estimating expectations over
θ∼q\theta\sim q via Monte Carlo *inside the simulator*. While θ\theta-conditional PMP objects can
still be computed under frozen-θ\theta simulations for inspection, our deployable target and
guarantees are expressed in terms of qq-aggregated stationarity, motivating the simulation-based
methods in Section [3](https://arxiv.org/html/2601.03175v1#S3 "3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection").

## 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty

We study the fixed-qq ex–ante portfolio choice problem of Section [2](https://arxiv.org/html/2601.03175v1#S2 "2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection") under latent parameter uncertainty
θ∼q\theta\sim q. The investor must deploy a *θ\theta-blind* policy (Remark [1](https://arxiv.org/html/2601.03175v1#Thmremark1 "Remark 1 (Latent parameter, observability, and admissible controls). ‣ Uncertainty law 𝑞⁢(𝑑⁢𝜃) and information structure. ‣ 2.1 Model and ex–ante objective in estimated diffusion markets ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")), so the control can depend on
observable states (t,Xt,Yt)(t,X\_{t},Y\_{t}) but cannot take θ\theta as an input. We restrict attention to Markov feedback policies parameterized
by a neural network πφ​(t,x,y)\pi\_{\varphi}(t,x,y).

Our solution approach follows a two-stage pipeline:

* •

  Stage 1 (PG–DPO). We perform stochastic gradient ascent on the ex–ante objective
  J​(φ)=𝔼​[U​(XTπφ,θ)]J(\varphi)=\mathbb{E}[U(X\_{T}^{\pi\_{\varphi},\theta})], sampling θ\theta only inside the simulator while keeping πφ\pi\_{\varphi} deployable and θ\theta-blind.
* •

  Stage 2 (Pontryagin projection). Under a warm-up policy, we estimate Pontryagin sensitivity objects by BPTT
  (conditionally on frozen θ\theta), aggregate them across θ∼q\theta\sim q, and construct a single deployable portfolio by projecting onto the
  aggregated first-order condition ([20](https://arxiv.org/html/2601.03175v1#S2.E20 "Equation 20 ‣ 𝑞-aggregated Pontryagin condition for the 𝜃-blind ex–ante problem (Markov feedback). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).

A practical subtlety is that the qq-aggregated Pontryagin condition involves mixed moments across θ\theta
(products of θ\theta-dependent costates and θ\theta-dependent coefficients). In moderate to high dimensions, these quantities can be
statistically noisy under finite Monte Carlo budgets. In our implementation, the main stabilization mechanisms are
(i) estimating stage 2 objects under a warm-up policy (two-time-scale stabilization), (ii) computing the same projection in a residual/control-variate
form (Section [3.3.1](https://arxiv.org/html/2601.03175v1#S3.SS3.SSS1 "3.3.1 Control-variate (residual) form of the projected rule ‣ 3.3 Coupling stage 1 and stage 2: residual projection and interactive distillation ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")), and (iii) amortizing projection via interactive distillation (Section [3.3.2](https://arxiv.org/html/2601.03175v1#S3.SS3.SSS2 "3.3.2 Interactive distillation: projection-guided training and amortized deployment ‣ 3.3 Coupling stage 1 and stage 2: residual projection and interactive distillation ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).

Section [3.1](https://arxiv.org/html/2601.03175v1#S3.SS1 "3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection") reviews baseline PG–DPO and the conditional BPTT–PMP correspondence.
Section [3.2](https://arxiv.org/html/2601.03175v1#S3.SS2 "3.2 Projected PG–DPO under latent 𝜃: 𝑞-aggregated projection and a residual-based policy-gap bound ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection") develops the stage 2 qq-aggregated projection under latent θ\theta, together with a residual-based
policy-gap guarantee.
Section [3.3](https://arxiv.org/html/2601.03175v1#S3.SS3 "3.3 Coupling stage 1 and stage 2: residual projection and interactive distillation ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection") records two practical couplings between stage 1 and stage 2 (residual form and interactive distillation).

### 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence

##### Setup and objectives (frozen θ\theta, deployable θ\theta-blind feedback).

A latent parameter θ∈Θ\theta\in\Theta is sampled from a fixed law q​(d​θ)q(d\theta) inside the simulator and kept frozen along each simulated trajectory.
A deployable portfolio policy is a θ\theta-blind Markov feedback rule represented by a neural network

|  |  |  |  |
| --- | --- | --- | --- |
|  | πφ:[0,T]×(0,∞)×ℝm→ℝd,(t,x,y)↦πφ​(t,x,y),φ∈ℝp,\pi\_{\varphi}:\ [0,T]\times(0,\infty)\times\mathbb{R}^{m}\to\mathbb{R}^{d},\hskip 18.49988pt(t,x,y)\mapsto\pi\_{\varphi}(t,x,y),\hskip 18.49988pt\varphi\in\mathbb{R}^{p}, |  | (52) |

which does *not* take θ\theta as an input.
For a fixed frozen θ\theta, the θ\theta-conditional state is (Xtπ,θ,Ytθ)t∈[0,T](X\_{t}^{\pi,\theta},Y\_{t}^{\theta})\_{t\in[0,T]} and evolves as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Xtπ,θXtπ,θ\displaystyle\frac{dX\_{t}^{\pi,\theta}}{X\_{t}^{\pi,\theta}} | =(r+πt⊤​b​(Ytθ,θ))​d​t+πt⊤​σ​(Ytθ,θ)​d​Wt,X0=x>0,\displaystyle=\Big(r+\pi\_{t}^{\top}b\big(Y\_{t}^{\theta},\theta\big)\Big)\,dt+\pi\_{t}^{\top}\sigma\big(Y\_{t}^{\theta},\theta\big)\,dW\_{t},\hskip 18.49988ptX\_{0}=x>0, |  | (53) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Ytθ\displaystyle dY\_{t}^{\theta} | =a​(Ytθ,θ)​d​t+β​(Ytθ,θ)​d​WtY,Y0=y∈ℝm.\displaystyle=a\big(Y\_{t}^{\theta},\theta\big)\,dt+\beta\big(Y\_{t}^{\theta},\theta\big)\,dW\_{t}^{Y},\hskip 18.49988ptY\_{0}=y\in\mathbb{R}^{m}. |  | (54) |

For each fixed θ\theta we evaluate πφ\pi\_{\varphi} by the conditional objective

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jθ​(φ):=𝔼​[U​(XTπφ,θ)|θ],J^{\theta}(\varphi):=\mathbb{E}\big[U\big(X\_{T}^{\pi\_{\varphi},\theta}\big)\,\big|\,\theta\big], |  | (55) |

where the expectation is over Brownian paths in ([53](https://arxiv.org/html/2601.03175v1#S3.E53 "Equation 53 ‣ Setup and objectives (frozen 𝜃, deployable 𝜃-blind feedback). ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"))–([54](https://arxiv.org/html/2601.03175v1#S3.E54 "Equation 54 ‣ Setup and objectives (frozen 𝜃, deployable 𝜃-blind feedback). ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).
The fixed-qq ex–ante objective is

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(φ):=𝔼θ∼q​[Jθ​(φ)]=𝔼​[U​(XTπφ,θ)],J(\varphi):=\mathbb{E}\_{\theta\sim q}\big[J^{\theta}(\varphi)\big]=\mathbb{E}\Big[U\big(X\_{T}^{\pi\_{\varphi},\theta}\big)\Big], |  | (56) |

where the last expectation is joint over θ∼q\theta\sim q and (W,WY)(W,W^{Y}).
Thus supφJ​(φ)\sup\_{\varphi}J(\varphi) is a standard stochastic optimization problem: θ\theta is sampled inside the simulator while the policy remains θ\theta-blind.

##### Discretization, sampling over θ\theta, and baseline PG–DPO update.

We discretize [0,T][0,T] into NN steps of length Δ​t\Delta t and approximate
([53](https://arxiv.org/html/2601.03175v1#S3.E53 "Equation 53 ‣ Setup and objectives (frozen 𝜃, deployable 𝜃-blind feedback). ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"))–([54](https://arxiv.org/html/2601.03175v1#S3.E54 "Equation 54 ‣ Setup and objectives (frozen 𝜃, deployable 𝜃-blind feedback). ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) by an Euler scheme.
For episode ii we denote the discrete state by (Xk(i),Yk(i))k=0,…,N(X\_{k}^{(i)},Y\_{k}^{(i)})\_{k=0,\dots,N} and write
θ(i)\theta^{(i)} for the frozen parameter used to generate that simulated environment.
Given πφ\pi\_{\varphi} and Brownian increments, the mapping

|  |  |  |
| --- | --- | --- |
|  | (x(i),y(i),θ(i),{Δ​Wk(i),Δ​WkY,(i)}k=0N−1,φ)⟼U​(XN(i))\big(x^{(i)},y^{(i)},\theta^{(i)},\{\Delta W\_{k}^{(i)},\Delta W\_{k}^{Y,(i)}\}\_{k=0}^{N-1},\varphi\big)\longmapsto U\big(X\_{N}^{(i)}\big) |  |

is a finite computational graph, so automatic differentiation computes exact discrete gradients
∇φU​(XN(i))\nabla\_{\varphi}U(X\_{N}^{(i)}).

A typical PG–DPO update samples a mini-batch of initial states
{(t0(i),x0(i),y0(i))}i=1M\{(t\_{0}^{(i)},x\_{0}^{(i)},y\_{0}^{(i)})\}\_{i=1}^{M} from a user-chosen training distribution ν\nu on [0,T)×(0,∞)×ℝm[0,T)\times(0,\infty)\times\mathbb{R}^{m},
samples θ∼q\theta\sim q inside the simulator (unseen by the policy) and holds it frozen for the update, and simulates forward:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yk+1(i)\displaystyle Y\_{k+1}^{(i)} | =Yk(i)+a​(Yk(i),θ)​Δ​t(i)+β​(Yk(i),θ)​Δ​WkY,(i),\displaystyle=Y\_{k}^{(i)}+a\big(Y\_{k}^{(i)},\theta\big)\Delta t^{(i)}+\beta\big(Y\_{k}^{(i)},\theta\big)\Delta W\_{k}^{Y,(i)}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Xk+1(i)\displaystyle X\_{k+1}^{(i)} | =Xk(i)+Xk(i)​(r+πφ​(tk(i),Xk(i),Yk(i))⊤​b​(Yk(i),θ))​Δ​t(i)\displaystyle=X\_{k}^{(i)}+X\_{k}^{(i)}\Big(r+\pi\_{\varphi}\big(t\_{k}^{(i)},X\_{k}^{(i)},Y\_{k}^{(i)}\big)^{\top}b\big(Y\_{k}^{(i)},\theta\big)\Big)\Delta t^{(i)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +Xk(i)​πφ​(tk(i),Xk(i),Yk(i))⊤​σ​(Yk(i),θ)​Δ​Wk(i),\displaystyle\hphantom{={}}{}+X\_{k}^{(i)}\,\pi\_{\varphi}\big(t\_{k}^{(i)},X\_{k}^{(i)},Y\_{k}^{(i)}\big)^{\top}\sigma\big(Y\_{k}^{(i)},\theta\big)\Delta W\_{k}^{(i)}, |  |

starting from X0(i)=x0(i)X\_{0}^{(i)}=x\_{0}^{(i)}, Y0(i)=y0(i)Y\_{0}^{(i)}=y\_{0}^{(i)}.
The episode reward is

|  |  |  |  |
| --- | --- | --- | --- |
|  | J(i)​(φ):=U​(XN(i)),J^{(i)}(\varphi):=U\big(X\_{N}^{(i)}\big), |  | (57) |

and BPTT computes ∇φJ(i)​(φ)\nabla\_{\varphi}J^{(i)}(\varphi).
The policy parameters are then updated (e.g. by Adam) as

|  |  |  |  |
| --- | --- | --- | --- |
|  | φ←φ+α​1M​∑i=1M∇φJ(i)​(φ).\varphi\leftarrow\varphi+\alpha\,\frac{1}{M}\sum\_{i=1}^{M}\nabla\_{\varphi}J^{(i)}(\varphi). |  | (58) |

Sampling θ\theta independently per episode (i.e. θ(i)∼q\theta^{(i)}\sim q) or sampling one θ∼q\theta\sim q per update and reusing it across the batch
both yield unbiased stochastic gradients for J​(φ)J(\varphi).

##### Pathwise costates from BPTT and the (conditional) BPTT–PMP correspondence.

BPTT returns not only ∇φJ(i)​(φ)\nabla\_{\varphi}J^{(i)}(\varphi) but also pathwise sensitivities with respect to intermediate state variables,
which coincide with discrete-time adjoint variables (costates) in the sense of Pontryagin.
For a single episode (suppressing ii and θ\theta in notation), define the pathwise wealth costate

|  |  |  |  |
| --- | --- | --- | --- |
|  | pk:=∂U​(XN)∂Xk,k=0,…,N,p\_{k}:=\frac{\partial U(X\_{N})}{\partial X\_{k}},\hskip 18.49988ptk=0,\dots,N, |  | (59) |

and the additional pathwise sensitivity objects used in projected controls:

|  |  |  |  |
| --- | --- | --- | --- |
|  | px,k:=∂pk∂Xk,py,k:=∂pk∂Yk,k=0,…,N.p\_{x,k}:=\frac{\partial p\_{k}}{\partial X\_{k}},\hskip 18.49988ptp\_{y,k}:=\frac{\partial p\_{k}}{\partial Y\_{k}},\hskip 18.49988ptk=0,\dots,N. |  | (60) |

###### Theorem 2 (BPTT–PMP correspondence (conditional on θ\theta, uniform on compacts)).

Fix θ∈Θ\theta\in\Theta and assume standard regularity conditions ensuring (i) well-posedness of the θ\theta-conditional forward SDE
([53](https://arxiv.org/html/2601.03175v1#S3.E53 "Equation 53 ‣ Setup and objectives (frozen 𝜃, deployable 𝜃-blind feedback). ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"))–([54](https://arxiv.org/html/2601.03175v1#S3.E54 "Equation 54 ‣ Setup and objectives (frozen 𝜃, deployable 𝜃-blind feedback). ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) under the θ\theta-blind policy πφ\pi\_{\varphi} and
(ii) well-posedness of the associated θ\theta-conditional stochastic maximum principle (adjoint) system.
Let (ptθ,px,tθ,py,tθ)(p\_{t}^{\theta},p\_{x,t}^{\theta},p\_{y,t}^{\theta}) denote the resulting continuous-time Pontryagin objects under πφ\pi\_{\varphi}
(and, in smooth Markov regimes, the corresponding spatial derivatives of the decoupling field).
Let (pk,px,k,py,k)(p\_{k},p\_{x,k},p\_{y,k}) be the discrete pathwise quantities computed by BPTT for the Euler discretization
with step Δ​t\Delta t, as defined in ([59](https://arxiv.org/html/2601.03175v1#S3.E59 "Equation 59 ‣ Pathwise costates from BPTT and the (conditional) BPTT–PMP correspondence. ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"))–([60](https://arxiv.org/html/2601.03175v1#S3.E60 "Equation 60 ‣ Pathwise costates from BPTT and the (conditional) BPTT–PMP correspondence. ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).

Then, as Δ​t→0\Delta t\to 0, the BPTT-induced discrete adjoints converge to their continuous-time counterparts in an appropriate mean-square sense
(along trajectories). Moreover, for any compact set K⊂ΘK\subset\Theta, the constants in the convergence bounds can be chosen uniformly for all
θ∈K\theta\in K.

###### Proof.

See Appendix [B](https://arxiv.org/html/2601.03175v1#A2 "Appendix B Proof of Theorem 2 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection").
∎

Across θ∼q\theta\sim q, these Pontryagin objects form a θ\theta-indexed family.
Baseline PG–DPO trains against the ex–ante objective ([56](https://arxiv.org/html/2601.03175v1#S3.E56 "Equation 56 ‣ Setup and objectives (frozen 𝜃, deployable 𝜃-blind feedback). ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) by repeatedly sampling θ∼q\theta\sim q inside the simulator,
while the deployable policy remains θ\theta-blind.

### 3.2 Projected PG–DPO under latent θ\theta: qq-aggregated projection and a residual-based policy-gap bound

Stage 2 is a *projection step*: given a warm-up deployable θ\theta-blind feedback policy
πwarm=πφwarm\pi^{\mathrm{warm}}=\pi\_{\varphi^{\mathrm{warm}}} (from stage 1), we estimate θ\theta-conditional Pontryagin sensitivity objects
by BPTT/Monte Carlo under frozen θ∼q\theta\sim q, aggregate them across θ\theta, and construct a deployable θ\theta-blind policy by
projecting onto the qq-aggregated Pontryagin stationarity condition derived in Section [2.2](https://arxiv.org/html/2601.03175v1#S2.SS2 "2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection").
The main point is that the aggregated first-order condition is *affine* in the portfolio control; hence it induces a statewise
linear system and, on a suitable working domain, a concrete projection map from estimated Pontryagin objects to a portfolio rule.

Working domain and norms.
Fix a measurable working state domain D⊂[0,T]×(0,∞)×ℝmD\subset[0,T]\times(0,\infty)\times\mathbb{R}^{m} (e.g. a training/evaluation band) and a reference
measure μ\mu on DD (e.g. an empirical state distribution induced by rollouts).
For h:D→ℝnh:D\to\mathbb{R}^{n} we write

|  |  |  |
| --- | --- | --- |
|  | ‖h‖L2​(μ):=(∫D‖h​(z)‖2​μ​(d​z))1/2,z=(t,x,y),\|h\|\_{L^{2}(\mu)}:=\Big(\int\_{D}\|h(z)\|^{2}\,\mu(dz)\Big)^{1/2},\hskip 18.49988ptz=(t,x,y), |  |

and for θ\theta-indexed families (used when tracking frozen-θ\theta quantities in analysis/inspection),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖f‖L2​(q⊗μ):=(∫Θ∫D‖fθ​(z)‖2​μ​(d​z)​q​(d​θ))1/2.\|f\|\_{L^{2}(q\otimes\mu)}:=\bigg(\int\_{\Theta}\int\_{D}\|f^{\theta}(z)\|^{2}\,\mu(dz)\,q(d\theta)\bigg)^{1/2}. |  | (61) |

##### Mixed-moment qq-aggregation under a warm-up policy.

By Theorem [1](https://arxiv.org/html/2601.03175v1#Thmtheorem1 "Theorem 1 (𝑞-aggregated first-order condition under latent 𝜃 (deployable 𝜃-blind stationarity)). ‣ 𝑞-aggregated Pontryagin condition for the 𝜃-blind ex–ante problem (Markov feedback). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"), any locally optimal interior *deployable* θ\theta-blind policy
π⋆,blind\pi^{\star,\mathrm{blind}} for the fixed-qq ex–ante problem satisfies the qq-aggregated stationarity condition
([20](https://arxiv.org/html/2601.03175v1#S2.E20 "Equation 20 ‣ 𝑞-aggregated Pontryagin condition for the 𝜃-blind ex–ante problem (Markov feedback). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")). In the portfolio Hamiltonian ([15](https://arxiv.org/html/2601.03175v1#S2.E15 "Equation 15 ‣ A 𝜃-conditional (full-information) Hamiltonian and first-order condition (infeasible under latent 𝜃). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")), this stationarity is equivalent to a statewise linear
system and hence to the projected form ([25](https://arxiv.org/html/2601.03175v1#S2.E25 "Equation 25 ‣ Theorem 1 (𝑞-aggregated first-order condition under latent 𝜃 (deployable 𝜃-blind stationarity)). ‣ 𝑞-aggregated Pontryagin condition for the 𝜃-blind ex–ante problem (Markov feedback). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) on the working domain (under invertibility of the aggregated curvature term).
P–PGDPO constructs a practical approximation of this projection by estimating the relevant aggregated Pontryagin objects under a fixed warm-up
policy πwarm=πφwarm\pi^{\mathrm{warm}}=\pi\_{\varphi^{\mathrm{warm}}}.

Fix a query state z=(t,x,y)∈Dz=(t,x,y)\in D and a frozen parameter θ\theta.
We simulate trajectories under πwarm\pi^{\mathrm{warm}} and compute pathwise Pontryagin sensitivity objects by autodiff/BPTT; averaging over
MMCM\_{\mathrm{MC}} trajectories yields Monte Carlo estimates

|  |  |  |  |
| --- | --- | --- | --- |
|  | p^tθ​(z),p^x,tθ​(z),p^y,tθ​(z).\widehat{p}\_{t}^{\theta}(z),\hskip 18.49988pt\widehat{p}\_{x,t}^{\theta}(z),\hskip 18.49988pt\widehat{p}\_{y,t}^{\theta}(z). |  | (62) |

Using these, define the θ\theta-conditional estimated projection inputs

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | A^tθ​(t,x,y)\displaystyle\widehat{A}\_{t}^{\theta}(t,x,y) | :=x​p^x,tθ​(t,x,y)​Σ​(y,θ)∈ℝd×d,\displaystyle:=x\,\widehat{p}\_{x,t}^{\theta}(t,x,y)\,\Sigma(y,\theta)\in\mathbb{R}^{d\times d}, |  | (63) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | G^tθ​(t,x,y)\displaystyle\widehat{G}\_{t}^{\theta}(t,x,y) | :=p^tθ​(t,x,y)​b​(y,θ)+ΣS​Y​(y,θ)​p^y,tθ​(t,x,y)∈ℝd.\displaystyle:=\widehat{p}\_{t}^{\theta}(t,x,y)\,b(y,\theta)+\Sigma\_{SY}(y,\theta)\,\widehat{p}\_{y,t}^{\theta}(t,x,y)\in\mathbb{R}^{d}. |  | (64) |

Aggregating across θ∼q\theta\sim q (approximated in practice by sampling MθM\_{\theta} frozen parameters) gives

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | A^t​(t,x,y)\displaystyle\widehat{A}\_{t}(t,x,y) | :=𝔼θ∼q​[A^tθ​(t,x,y)],\displaystyle:=\mathbb{E}\_{\theta\sim q}\Big[\widehat{A}\_{t}^{\theta}(t,x,y)\Big], |  | (65) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | G^tmix​(t,x,y)\displaystyle\widehat{G}\_{t}^{\mathrm{mix}}(t,x,y) | :=𝔼θ∼q​[G^tθ​(t,x,y)].\displaystyle:=\mathbb{E}\_{\theta\sim q}\Big[\widehat{G}\_{t}^{\theta}(t,x,y)\Big]. |  | (66) |

Whenever A^t​(t,x,y)\widehat{A}\_{t}(t,x,y) is invertible on DD, we obtain the mixed-moment projected policy

|  |  |  |  |
| --- | --- | --- | --- |
|  | π^agg,mix​(t,x,y):=−A^t​(t,x,y)−1​G^tmix​(t,x,y).\widehat{\pi}^{\mathrm{agg,mix}}(t,x,y):=-\,\widehat{A}\_{t}(t,x,y)^{-1}\,\widehat{G}\_{t}^{\mathrm{mix}}(t,x,y). |  | (67) |

##### Residual diagnostic and a slab-wise small-gain policy-gap bound.

To connect the projected policy ([67](https://arxiv.org/html/2601.03175v1#S3.E67 "Equation 67 ‣ Mixed-moment 𝑞-aggregation under a warm-up policy. ‣ 3.2 Projected PG–DPO under latent 𝜃: 𝑞-aggregated projection and a residual-based policy-gap bound ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) to a locally optimal deployable θ\theta-blind policy, we measure how well the warm-up
policy satisfies the *population* mixed-moment aggregated stationarity.
Let (Aπ,Gπmix)(A\_{\pi},G\_{\pi}^{\mathrm{mix}}) denote the mixed-moment qq-aggregated projection inputs induced by a policy π\pi
(i.e. the objects in ([23](https://arxiv.org/html/2601.03175v1#S2.E23 "Equation 23 ‣ 𝑞-aggregated Pontryagin condition for the 𝜃-blind ex–ante problem (Markov feedback). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) evaluated using the θ\theta-conditional Pontryagin objects generated by π\pi).
Define the warm-up aggregated stationarity residual on DD by

|  |  |  |  |
| --- | --- | --- | --- |
|  | rFOC,mixwarm​(t,x,y):=Aπwarm​(t,x,y)​πwarm​(t,x,y)+Gπwarmmix​(t,x,y),εwarmmix:=‖rFOC,mixwarm‖L2​(μ).r^{\mathrm{warm}}\_{\mathrm{FOC,mix}}(t,x,y):=A\_{\pi^{\mathrm{warm}}}(t,x,y)\,\pi^{\mathrm{warm}}(t,x,y)+G\_{\pi^{\mathrm{warm}}}^{\mathrm{mix}}(t,x,y),\hskip 18.49988pt\varepsilon\_{\mathrm{warm}}^{\mathrm{mix}}:=\big\|r^{\mathrm{warm}}\_{\mathrm{FOC,mix}}\big\|\_{L^{2}(\mu)}. |  | (68) |

In practice we monitor the estimator
r^FOC,mixwarm:=A^t​πwarm+G^tmix\widehat{r}^{\mathrm{warm}}\_{\mathrm{FOC,mix}}:=\widehat{A}\_{t}\,\pi^{\mathrm{warm}}+\widehat{G}\_{t}^{\mathrm{mix}}
computed from the same BPTT/Monte Carlo pipeline.

A technical point is that a *global* small-gain condition of the form C1<1C\_{1}<1 can be overly restrictive.
Following the slab-wise philosophy in our prior PGDPO analysis (e.g. huh2025breaking),
we default to a *time-slab* decomposition of the working domain and close the warm-up gap on each short slab.
Concretely, assume DD carries a time coordinate and fix a partition 0=t0<t1<⋯<tK=T0=t\_{0}<t\_{1}<\cdots<t\_{K}=T with slab lengths
τk:=tk−tk−1\tau\_{k}:=t\_{k}-t\_{k-1}. Let

|  |  |  |
| --- | --- | --- |
|  | Dk:=D∩([tk−1,tk]×𝒮),μk:=μ|Dk,‖f‖k:=‖f‖L2​(μk).D\_{k}:=D\cap([t\_{k-1},t\_{k}]\times\mathcal{S}),\hskip 18.49988pt\mu\_{k}:=\mu|\_{D\_{k}},\hskip 18.49988pt\|f\|\_{k}:=\|f\|\_{L^{2}(\mu\_{k})}. |  |

We write T​(π):=−Aπ−1​GπmixT(\pi):=-A\_{\pi}^{-1}G\_{\pi}^{\mathrm{mix}} for the (population) qq-aggregated projection map.
Theorem [3](https://arxiv.org/html/2601.03175v1#Thmtheorem3 "Theorem 3 (Residual-based ex–ante 𝜃-blind policy-gap bound for P–PGDPO (mixed-moment, deployable, slab-wise local)). ‣ Residual diagnostic and a slab-wise small-gain policy-gap bound. ‣ 3.2 Projected PG–DPO under latent 𝜃: 𝑞-aggregated projection and a residual-based policy-gap bound ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection") below shows that, under a mild *slab-wise* local stability regime
(i.e. a short-time contraction of TT on each DkD\_{k}), small residual implies that the projected policy is close
(in L2​(μ)L^{2}(\mu)) to a locally optimal deployable θ\theta-blind policy, up to discretization/Monte Carlo error.
The proof combines a projection-map stability bound (Appendix [C.1](https://arxiv.org/html/2601.03175v1#A3.SS1 "C.1 Stability of the projection map (𝐴,𝐺)↦-𝐴⁻¹⁢𝐺 ‣ Appendix C Auxiliary results for Theorem 3 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) with a slab-wise closure
(Appendix [C.2](https://arxiv.org/html/2601.03175v1#A3.SS2 "C.2 Slab-wise small-gain for the 𝑞-aggregated projection inputs ‣ Appendix C Auxiliary results for Theorem 3 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")), in the same spirit as the slab analyses used in huh2025breaking.

###### Theorem 3 (Residual-based ex–ante θ\theta-blind policy-gap bound for P–PGDPO (mixed-moment, deployable, slab-wise local)).

Assume the uniform invertibility/stability conditions of Proposition [1](https://arxiv.org/html/2601.03175v1#Thmproposition1 "Proposition 1 (Stability of the projection map (𝐴,𝐺)↦-𝐴⁻¹⁢𝐺). ‣ C.1 Stability of the projection map (𝐴,𝐺)↦-𝐴⁻¹⁢𝐺 ‣ Appendix C Auxiliary results for Theorem 3 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")
(Appendix [C.1](https://arxiv.org/html/2601.03175v1#A3.SS1 "C.1 Stability of the projection map (𝐴,𝐺)↦-𝐴⁻¹⁢𝐺 ‣ Appendix C Auxiliary results for Theorem 3 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) hold on DD for the relevant aggregated curvature terms
and for the estimator perturbations constructed under πwarm\pi^{\mathrm{warm}}.

Let π⋆,blind\pi^{\star,\mathrm{blind}} be a locally optimal interior deployable θ\theta-blind policy for the fixed-qq ex–ante problem.
Assume there exists a neighborhood 𝒰\mathcal{U} of π⋆,blind\pi^{\star,\mathrm{blind}} in L2​(μ)L^{2}(\mu) such that for all π∈𝒰\pi\in\mathcal{U},

|  |  |  |
| --- | --- | --- |
|  | ‖Aπ−1‖L∞​(D)≤κ,‖Gπmix‖L∞​(D)≤MG,\|A\_{\pi}^{-1}\|\_{L^{\infty}(D)}\leq\kappa,\hskip 18.49988pt\|G\_{\pi}^{\mathrm{mix}}\|\_{L^{\infty}(D)}\leq M\_{G}, |  |

and assume the *slab-wise Lipschitz gain* of Appendix [C.2](https://arxiv.org/html/2601.03175v1#A3.SS2 "C.2 Slab-wise small-gain for the 𝑞-aggregated projection inputs ‣ Appendix C Auxiliary results for Theorem 3 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection") holds:
there exist constants L¯A,L¯G>0\bar{L}\_{A},\bar{L}\_{G}>0 such that for every slab DkD\_{k} and all π1,π2∈𝒰\pi\_{1},\pi\_{2}\in\mathcal{U},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Aπ1−Aπ2‖k≤L¯A​τk1/2​‖π1−π2‖k,‖Gπ1mix−Gπ2mix‖k≤L¯G​τk1/2​‖π1−π2‖k.\|A\_{\pi\_{1}}-A\_{\pi\_{2}}\|\_{k}\leq\bar{L}\_{A}\,\tau\_{k}^{1/2}\,\|\pi\_{1}-\pi\_{2}\|\_{k},\hskip 18.49988pt\|G\_{\pi\_{1}}^{\mathrm{mix}}-G\_{\pi\_{2}}^{\mathrm{mix}}\|\_{k}\leq\bar{L}\_{G}\,\tau\_{k}^{1/2}\,\|\pi\_{1}-\pi\_{2}\|\_{k}. |  | (69) |

Define

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ​(τ):=(κ​L¯G+κ2​MG​L¯A)​τ1/2,ρ∗:=max1≤k≤K⁡ρ​(τk).\rho(\tau):=\big(\kappa\bar{L}\_{G}+\kappa^{2}M\_{G}\bar{L}\_{A}\big)\tau^{1/2},\hskip 18.49988pt\rho\_{\*}:=\max\_{1\leq k\leq K}\rho(\tau\_{k}). |  | (70) |

Assume the slab partition is chosen so that ρ∗<1\rho\_{\*}<1.

Let π^agg,mix\widehat{\pi}^{\mathrm{agg,mix}} be the mixed-moment projected policy ([67](https://arxiv.org/html/2601.03175v1#S3.E67 "Equation 67 ‣ Mixed-moment 𝑞-aggregation under a warm-up policy. ‣ 3.2 Projected PG–DPO under latent 𝜃: 𝑞-aggregated projection and a residual-based policy-gap bound ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) computed from BPTT/Monte Carlo estimates under
πwarm\pi^{\mathrm{warm}}, and let εwarmmix\varepsilon\_{\mathrm{warm}}^{\mathrm{mix}} be the population residual
([68](https://arxiv.org/html/2601.03175v1#S3.E68 "Equation 68 ‣ Residual diagnostic and a slab-wise small-gain policy-gap bound. ‣ 3.2 Projected PG–DPO under latent 𝜃: 𝑞-aggregated projection and a residual-based policy-gap bound ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")). Then there exists C2>0C\_{2}>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖π^agg,mix−π⋆,blind‖L2​(μ)≤ρ∗​κ1−ρ∗​εwarmmix+C2​δBPTT​(Δ​t,MMC,Mθ).\big\|\widehat{\pi}^{\mathrm{agg,mix}}-\pi^{\star,\mathrm{blind}}\big\|\_{L^{2}(\mu)}\;\leq\;\frac{\rho\_{\*}\kappa}{1-\rho\_{\*}}\,\varepsilon\_{\mathrm{warm}}^{\mathrm{mix}}\;+\;C\_{2}\,\delta\_{\mathrm{BPTT}}(\Delta t,M\_{\mathrm{MC}},M\_{\theta}). |  | (71) |

Moreover, under the perturbative regime of Proposition [1](https://arxiv.org/html/2601.03175v1#Thmproposition1 "Proposition 1 (Stability of the projection map (𝐴,𝐺)↦-𝐴⁻¹⁢𝐺). ‣ C.1 Stability of the projection map (𝐴,𝐺)↦-𝐴⁻¹⁢𝐺 ‣ Appendix C Auxiliary results for Theorem 3 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"), one may take for example
C2:=2​κ+4​κ2​MGC\_{2}:=2\kappa+4\kappa^{2}M\_{G}.

###### Proof.

See Appendix [C.3](https://arxiv.org/html/2601.03175v1#A3.SS3 "C.3 Proof of Theorem 3 ‣ Appendix C Auxiliary results for Theorem 3 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection").
∎

### 3.3 Coupling stage 1 and stage 2: residual projection and interactive distillation

We keep the ex–ante objective ([56](https://arxiv.org/html/2601.03175v1#S3.E56 "Equation 56 ‣ Setup and objectives (frozen 𝜃, deployable 𝜃-blind feedback). ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) and the θ\theta-blind deployability constraint throughout.
Stage 2 is *not* a separate optimization problem: it reuses the current stage 1 policy as a warm-up control under which the
(costate-based) projection ingredients are estimated, and then applies a qq-aggregated Pontryagin projection as a post-processing map.

This subsection records two couplings between the two stages, each with a distinct role.
First, we implement the projected rule in a residual (control-variate) form, which is algebraically equivalent to the direct projection
but typically reduces Monte Carlo variance and improves numerical stability in high dimensions.
Second, we use the projected output as a teacher signal via interactive distillation.
Beyond acting as an optimization aid, distillation serves an *amortization* purpose: stage 2 projection can be accurate but Monte-Carlo
intensive, whereas a distilled student policy can approximate the projected rule with a single forward pass at stage 1 inference cost.

#### 3.3.1 Control-variate (residual) form of the projected rule

Recall the mixed-moment projected rule ([67](https://arxiv.org/html/2601.03175v1#S3.E67 "Equation 67 ‣ Mixed-moment 𝑞-aggregation under a warm-up policy. ‣ 3.2 Projected PG–DPO under latent 𝜃: 𝑞-aggregated projection and a residual-based policy-gap bound ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")). In high dimensions, Monte Carlo noise in the projection inputs can be
non-negligible, and solving a linear system with A^t\widehat{A}\_{t} can amplify this noise. A convenient stabilization is to compute the
*same* projected rule in a residual form around the warm-up policy πφwarm\pi\_{\varphi^{\mathrm{warm}}}.

Define the θ\theta-conditional residual (under frozen-θ\theta simulations)

|  |  |  |  |
| --- | --- | --- | --- |
|  | r^FOCθ(t,x,y):=A^tθ(t,x,y)πφwarm(t,x,y)+G^tθ(t,x,y),\widehat{r}\_{\mathrm{FOC}}^{\theta}(t,x,y):=\widehat{A}\_{t}^{\theta}(t,x,y)\,\pi\_{\varphi^{\mathrm{warm}}}(t,x,y)+\widehat{G}\_{t}^{\theta}(t,x,y), |  | (72) |

and the aggregated residual (the quantity we actually solve against)

|  |  |  |  |
| --- | --- | --- | --- |
|  | r^FOC​(t,x,y):=A^t​(t,x,y)​πφwarm​(t,x,y)+G^tmix​(t,x,y).\widehat{r}\_{\mathrm{FOC}}(t,x,y):=\widehat{A}\_{t}(t,x,y)\,\pi\_{\varphi^{\mathrm{warm}}}(t,x,y)+\widehat{G}\_{t}^{\mathrm{mix}}(t,x,y). |  | (73) |

Whenever A^t​(t,x,y)\widehat{A}\_{t}(t,x,y) is invertible, the projected rule admits the identity

|  |  |  |  |
| --- | --- | --- | --- |
|  | π^agg,mix​(t,x,y)=πφwarm​(t,x,y)−A^t​(t,x,y)−1​r^FOC​(t,x,y),\widehat{\pi}^{\mathrm{agg,mix}}(t,x,y)=\pi\_{\varphi^{\mathrm{warm}}}(t,x,y)-\widehat{A}\_{t}(t,x,y)^{-1}\,\widehat{r}\_{\mathrm{FOC}}(t,x,y), |  | (74) |

which is an algebraic rewriting of ([67](https://arxiv.org/html/2601.03175v1#S3.E67 "Equation 67 ‣ Mixed-moment 𝑞-aggregation under a warm-up policy. ‣ 3.2 Projected PG–DPO under latent 𝜃: 𝑞-aggregated projection and a residual-based policy-gap bound ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) (hence it does not change the target). Its practical value is variance
reduction: when the warm-up policy is already close to a projected fixed point on the working domain, the residual
r^FOC\widehat{r}\_{\mathrm{FOC}} tends to be small, and it often concentrates faster because the ingredients entering
A^t​πφwarm\widehat{A}\_{t}\pi\_{\varphi^{\mathrm{warm}}} and G^tmix\widehat{G}\_{t}^{\mathrm{mix}} are computed from the same Monte Carlo pool and partially cancel.

#### 3.3.2 Interactive distillation: projection-guided training and amortized deployment

Let πφ\pi\_{\varphi} be the trainable stage 1 policy network. At intermittent refresh times, we freeze a lagged copy πφ−\pi\_{\varphi^{-}} and
run stage 2 under πφ−\pi\_{\varphi^{-}} to construct a qq-aggregated projected teacher. This coupling serves two purposes.
During training it provides projection-guided targets that can stabilize and accelerate stage 1 optimization; after training it amortizes
the expensive projection by distilling it into a fast deployable policy network.

In residual form ([74](https://arxiv.org/html/2601.03175v1#S3.E74 "Equation 74 ‣ 3.3.1 Control-variate (residual) form of the projected rule ‣ 3.3 Coupling stage 1 and stage 2: residual projection and interactive distillation ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")), the teacher is the θ\theta-blind map

|  |  |  |  |
| --- | --- | --- | --- |
|  | π^φ−agg,mix​(t,x,y):=πφ−​(t,x,y)−(A^tφ−​(t,x,y))−1​r^FOCφ−​(t,x,y),\widehat{\pi}^{\mathrm{agg,mix}}\_{\varphi^{-}}(t,x,y):=\pi\_{\varphi^{-}}(t,x,y)-\big(\widehat{A}\_{t}^{\varphi^{-}}(t,x,y)\big)^{-1}\,\widehat{r}\_{\mathrm{FOC}}^{\varphi^{-}}(t,x,y), |  | (75) |

where r^FOCφ−:=A^tφ−​πφ−+G^tmix,φ−\widehat{r}\_{\mathrm{FOC}}^{\varphi^{-}}:=\widehat{A}\_{t}^{\varphi^{-}}\pi\_{\varphi^{-}}+\widehat{G}\_{t}^{\mathrm{mix},\varphi^{-}} is computed
using the mixed-moment qq-aggregation under the lagged policy. We then train πφ\pi\_{\varphi} by combining the original ex–ante objective with a
proximity term to this teacher on the working domain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxφ⁡J​(φ)−λ​𝔼(t,x,y)∼μ​[‖πφ​(t,x,y)−stopgrad​(π^φ−agg,mix​(t,x,y))‖2],\max\_{\varphi}\;J(\varphi)\;-\;\lambda\,\mathbb{E}\_{(t,x,y)\sim\mu}\Big[\big\|\pi\_{\varphi}(t,x,y)-\mathrm{stopgrad}\big(\widehat{\pi}^{\mathrm{agg,mix}}\_{\varphi^{-}}(t,x,y)\big)\big\|^{2}\Big], |  | (76) |

where μ\mu is the working-domain sampling measure and λ≥0\lambda\geq 0 controls the strength of projection guidance. The operator
stopgrad​(⋅)\mathrm{stopgrad}(\cdot) indicates that gradients are not propagated through stage 2; once computed from πφ−\pi\_{\varphi^{-}}, the teacher
is treated as fixed.

In practice, φ−\varphi^{-} and π^φ−agg,mix\widehat{\pi}^{\mathrm{agg,mix}}\_{\varphi^{-}} are refreshed on a slower timescale than the stage 1 gradient steps:
we hold φ−\varphi^{-} fixed for several updates of φ\varphi under ([76](https://arxiv.org/html/2601.03175v1#S3.E76 "Equation 76 ‣ 3.3.2 Interactive distillation: projection-guided training and amortized deployment ‣ 3.3 Coupling stage 1 and stage 2: residual projection and interactive distillation ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")), then set φ−←φ\varphi^{-}\leftarrow\varphi
and recompute the teacher. A practical schedule is to start with λ=0\lambda=0 (pure PG–DPO) and increase λ\lambda only after basic projection
checks on the working domain (e.g., residual magnitudes and curvature/denominator stability) indicate that the stage 2 map has become reliable.
Moreover, to avoid injecting noisy teacher targets early in training or on pathological regions of the domain, we may apply projection guidance only
on states where the projection checks certify reliability (an “adaptive teacher selection”); implementation details are deferred to the appendix
(Appendix [D](https://arxiv.org/html/2601.03175v1#A4 "Appendix D Implementation details for Section 3 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).

## 4 Breaking the Dimensional Barrier under Drift Uncertainty

This section instantiates the decision-time *static* Gaussian drift-uncertainty benchmark in
Section [2.3.1](https://arxiv.org/html/2601.03175v1#S2.SS3.SSS1 "2.3.1 Static Gaussian drift uncertainty ‣ 2.3 Gaussian references at a fixed decision time ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection") and uses its closed-form constant-portfolio
qq-reference as an analytic target.
Nature draws a fixed latent drift θ∼q\theta\sim q at t=0t=0 and keeps it constant over [0,T][0,T], while the investor
cannot observe θ\theta and must deploy a single θ\theta-blind policy under an ex–ante CRRA objective.
Because the benchmark admits a transparent decision-time reference, we can measure accuracy directly via decision-time RMSE,
rather than relying only on realized utility.

Our goal is to test whether Pontryagin-guided learning and projection remain stable as the number of assets grows.
We generate APT-style covariance structures and sweep dimensions d∈{5,10,50,100}d\in\{5,10,50,100\} under both
*aligned* uncertainty (P=s​ΣP=s\Sigma) and a *misaligned* geometry that rotates uncertainty away from market risk directions.
We compare Stage 1 (PG–DPO) to Stage 2 (Pontryagin projection) (and, when applicable, amortized variants via interactive distillation)
under matched simulation budgets that scale linearly with dd.

### 4.1 Benchmark market and evaluation protocol

This subsection fixes the benchmark and evaluation protocol used in Section [4](https://arxiv.org/html/2601.03175v1#S4 "4 Breaking the Dimensional Barrier under Drift Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection").
Our goal is to provide controlled evidence that the proposed two-stage pipeline remains
*computationally stable and accurate* as the number of assets dd grows under *decision-time*
parameter uncertainty.
The aligned vs. misaligned uncertainty geometries serve as two representative stress-test regimes;
the main message is scalability under uncertainty rather than any specific choice of PP.

θ\theta-blind deployability (and what uses θ\theta).
Throughout Section [4](https://arxiv.org/html/2601.03175v1#S4 "4 Breaking the Dimensional Barrier under Drift Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"), *all reported policies are deployable and θ\theta-blind*:
the control is a function of observable state only (here, decision-time evaluation uses t=0t=0 and X0X\_{0}),
and *never takes the realized latent premium θ\theta as an input*.
The latent θ∼q\theta\sim q is sampled *only inside the simulator* to generate trajectories and to form
Monte Carlo averages that approximate qq-expectations (notably in Stage 2 projection).
Any θ\theta-indexed objects (when referenced elsewhere) are used only for *offline diagnostics* and are
not part of the deployable decision rule.

Static decision-time uncertainty benchmark.
We adopt the static Gaussian drift-uncertainty market of Section [2.3.1](https://arxiv.org/html/2601.03175v1#S2.SS3.SSS1 "2.3.1 Static Gaussian drift uncertainty ‣ 2.3 Gaussian references at a fixed decision time ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"),
i.e., ([26](https://arxiv.org/html/2601.03175v1#S2.E26 "Equation 26 ‣ Market model (static latent drift). ‣ 2.3.1 Static Gaussian drift uncertainty ‣ 2.3 Gaussian references at a fixed decision time ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) with ([35](https://arxiv.org/html/2601.03175v1#S2.E35 "Equation 35 ‣ CRRA (𝛾≠1): tilted optimality and Gaussian shrinkage. ‣ 2.3.1 Static Gaussian drift uncertainty ‣ 2.3 Gaussian references at a fixed decision time ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")). Equivalently, we simulate

|  |  |  |
| --- | --- | --- |
|  | d​StSt=r​ 1​d​t+θ​d​t+Σ1/2​d​Wt,θ∼𝒩​(m,P),\frac{dS\_{t}}{S\_{t}}=r\,\mathbf{1}\,dt+\theta\,dt+\Sigma^{1/2}dW\_{t},\hskip 18.49988pt\theta\sim\mathcal{N}(m,P), |  |

where the latent premium θ\theta is drawn once at time 0 and kept fixed over [0,T][0,T].
The deployable policy is θ\theta-blind and interacts with qq only through sampling θ\theta inside the simulator.

APT-style factor construction of (m,Σ)(m,\Sigma).
We construct the mean premium and covariance via a low-dimensional factor representation.
Let WfW^{f} be a kΣk\_{\Sigma}-dimensional Brownian motion (factor shocks) and WεW^{\varepsilon} a dd-dimensional
Brownian motion (idiosyncratic shocks), independent of WfW^{f}.
We write excess returns as

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Rt:=d​StSt−r​𝟏​d​t=θ​d​t+B​Σf1/2​d​Wtf+diag​(D)​d​Wtε,dR\_{t}:=\frac{dS\_{t}}{S\_{t}}-r\mathbf{1}\,dt=\theta\,dt+B\,\Sigma\_{f}^{1/2}\,dW\_{t}^{f}+\mathrm{diag}(\sqrt{D})\,dW\_{t}^{\varepsilon}, |  | (77) |

with B∈ℝd×kΣB\in\mathbb{R}^{d\times k\_{\Sigma}}, Σf≻0\Sigma\_{f}\succ 0, and D∈(0,∞)dD\in(0,\infty)^{d}.
This implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ=B​Σf​B⊤+diag​(D)=F​F⊤+diag​(D),\Sigma=B\,\Sigma\_{f}\,B^{\top}+\mathrm{diag}(D)\;=\;FF^{\top}+\mathrm{diag}(D), |  | (78) |

where F:=B​chol​(Σf)F:=B\,\mathrm{chol}(\Sigma\_{f}).
We generate the mean premium in an APT-like form by drawing a factor price vector
λm∈ℝkΣ\lambda\_{m}\in\mathbb{R}^{k\_{\Sigma}} and setting

|  |  |  |  |
| --- | --- | --- | --- |
|  | m:=B​λm.m:=B\,\lambda\_{m}. |  | (79) |

One-shot generation and fairness across methods.
For each dimension dd, we generate a single market instance (B,Σf,D,λm)(B,\Sigma\_{f},D,\lambda\_{m}) once (using a fixed random seed)
and *hold it fixed across all algorithmic comparisons and MC-budget variants*.
Within a fixed dd, we change only the uncertainty covariance PP (aligned vs. misaligned and the scale ss below).
This isolates algorithmic effects from instance-to-instance randomness and makes the scaling comparisons controlled.

Uncertainty regimes (aligned vs. misaligned).
We consider two geometries for the drift-uncertainty covariance PP, controlled by a scalar magnitude s>0s>0.

*Aligned:* uncertainty shares market risk directions,

|  |  |  |  |
| --- | --- | --- | --- |
|  | P=s​Σ,s>0.P=s\,\Sigma,\hskip 18.49988pts>0. |  | (80) |

*Misaligned:* uncertainty factors are rotated away from the market factor space,

|  |  |  |  |
| --- | --- | --- | --- |
|  | P=B~​Σ~f​B~⊤+s​diag​(D),P=\widetilde{B}\,\widetilde{\Sigma}\_{f}\,\widetilde{B}^{\top}+s\,\mathrm{diag}(D), |  | (81) |

where B~\widetilde{B} is generated independently of BB (or explicitly orthogonalized against the span of BB to enforce
large principal angles). The factor term is rescaled so that its overall magnitude matches the aligned case under the same ss
(e.g., by matching tr​(P)\mathrm{tr}(P) or ‖P‖F\|P\|\_{F} up to the shared diagonal component).
This geometry increases heterogeneity across θ∼q\theta\sim q and makes mixed-moment estimation and subsequent linear-algebra
steps more fragile, providing a stringent scalability test.

Experiment grid and simulation budgets.
We vary the number of assets over d∈{5,10,50,100}d\in\{5,10,50,100\} and sweep three uncertainty magnitudes s∈{10−3,10−2,10−1}s\in\{10^{-3},10^{-2},10^{-1}\},
for both aligned and misaligned geometries.
To keep Monte Carlo noise comparable across dimensions, we use linear-in-dd sampling budgets:
a *base* regime with NMC=100⋅dN\_{\mathrm{MC}}=100\cdot d paths and a *high* regime with NMC=400⋅dN\_{\mathrm{MC}}=400\cdot d
(where NMCN\_{\mathrm{MC}} denotes the per-update or per-estimator path budget, depending on the stage).
All methods share the same discretization scheme (Euler) and action constraints; implementation details (network architecture,
optimizer settings, and exact sampling conventions for Stage 1 vs. Stage 2) are reported in the implementation appendix and code release.

Analytic reference and decision-time evaluation.
In the static Gaussian benchmark, the analytic decision-time reference under constant portfolios is available in closed form.
We use this closed-form rule only as an external decision-time target for evaluation; training does not impose the constant-portfolio restriction, and all methods learn from simulated trajectories over [0,T][0,T] under the same θ\theta-blind constraint.
For γ>1\gamma>1 we use the CRRA reference ([38](https://arxiv.org/html/2601.03175v1#S2.E38 "Equation 38 ‣ CRRA (𝛾≠1): tilted optimality and Gaussian shrinkage. ‣ 2.3.1 Static Gaussian drift uncertainty ‣ 2.3 Gaussian references at a fixed decision time ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) and, for γ=1\gamma=1, the log-utility reference
([31](https://arxiv.org/html/2601.03175v1#S2.E31 "Equation 31 ‣ Log utility (𝛾=1). ‣ 2.3.1 Static Gaussian drift uncertainty ‣ 2.3 Gaussian references at a fixed decision time ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).
We evaluate each method at t=0t=0 on a fixed grid {(X0(i),T(i))}i=1Neval\{(X\_{0}^{(i)},T^{(i)})\}\_{i=1}^{N\_{\mathrm{eval}}} and report RMSE to the analytic reference:

|  |  |  |  |
| --- | --- | --- | --- |
|  | RMSE​(u0,πq,γconst):=(1Neval​∑i=1Neval‖u0​(X0(i),T(i))−πq,γconst​(T(i))‖2)1/2,\mathrm{RMSE}(u\_{0},\pi\_{q,\gamma}^{\mathrm{const}}):=\bigg(\frac{1}{N\_{\mathrm{eval}}}\sum\_{i=1}^{N\_{\mathrm{eval}}}\big\|u\_{0}(X\_{0}^{(i)},T^{(i)})-\pi\_{q,\gamma}^{\mathrm{const}}(T^{(i)})\big\|^{2}\bigg)^{1/2}, |  | (82) |

where u0​(⋅)u\_{0}(\cdot) denotes the decision-time action prescribed by the method (deployable θ\theta-blind output).
With the benchmark fixed and with (m,Σ,P)(m,\Sigma,P) constructed as in ([79](https://arxiv.org/html/2601.03175v1#S4.E79 "Equation 79 ‣ 4.1 Benchmark market and evaluation protocol ‣ 4 Breaking the Dimensional Barrier under Drift Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"))–([81](https://arxiv.org/html/2601.03175v1#S4.E81 "Equation 81 ‣ 4.1 Benchmark market and evaluation protocol ‣ 4 Breaking the Dimensional Barrier under Drift Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")),
the remaining subsections compare baseline Stage 1 PG–DPO, post-hoc Stage 2 P–PGDPO projection, and interactive distillation
under matched simulation budgets.

### 4.2 High-dimensional CRRA benchmark: projection and amortization

Mixed-moment estimation and a decoupling approximation.
A practical issue throughout our experiments (both aligned and misaligned) is the estimation of *mixed moments* across the latent parameter, such as
𝔼θ∼q​[ptθ​(z)​θ]\mathbb{E}\_{\theta\sim q}[p\_{t}^{\theta}(z)\,\theta] (and analogous products entering G^tmix\widehat{G}\_{t}^{\mathrm{mix}}), because the costate ptθ​(z)p\_{t}^{\theta}(z) is
θ\theta-dependent and high-dimensional, and finite-sample covariance between ptθp\_{t}^{\theta} and θ\theta can lead to large Monte-Carlo variance once the
subsequent linear solve is applied. For numerical stability and a uniform protocol across geometries, we therefore use a simple *decoupling*
(independence) approximation for these mixed moments,

|  |  |  |
| --- | --- | --- |
|  | 𝔼θ∼q​[ptθ​(z)​θ]≈𝔼θ∼q​[ptθ​(z)]​𝔼θ∼q​[θ],\mathbb{E}\_{\theta\sim q}[p\_{t}^{\theta}(z)\,\theta]\;\approx\;\mathbb{E}\_{\theta\sim q}[p\_{t}^{\theta}(z)]\,\mathbb{E}\_{\theta\sim q}[\theta], |  |

(and similarly for other mixed products), which is exact when the relevant Pontryagin objects are effectively θ\theta-invariant and is accurate whenever
Covq​(ptθ​(z),θ)\mathrm{Cov}\_{q}(p\_{t}^{\theta}(z),\theta) is small relative to marginal scales. While this approximation is most valuable under misalignment—where direction
mixing can amplify mixed-moment noise—it also performs well in aligned regimes (where mixed moments are typically easier to estimate), and in the CRRA
benchmark below it does not alter the qualitative scaling conclusions: projection remains stable, and the observed misaligned degradation is consistent
with residual growth and curvature mismatch rather than catastrophic mixed-moment blow-ups. 111We note, however, that in extreme uncertainty/misalignment—where
θ\theta–costate dependence becomes pronounced—the decoupling can break down, in which case one should revert to full mixed-moment estimation (possibly with
larger budgets and/or regularized/certified projection).

![Refer to caption](x1.png)


Figure 1: Decision-time RMSE at t=0t=0 versus dimension dd (log scale), summarized by a *tail median* over the late-training window
(computed from the last evaluation snapshots). Rows: uncertainty magnitude s∈{10−3,10−2,10−1}s\in\{10^{-3},10^{-2},10^{-1}\}.
Columns: aligned vs. misaligned geometry. Curves compare Stage 1 (deployable) and Stage 2 (post-hoc projection), with and without interactive distillation.
Solid vs. dashed lines correspond to MC base (100⋅d100\cdot d) vs. high (400⋅d400\cdot d) budgets.

Protocol and summary statistic.
We consider the CRRA benchmark with γ=2\gamma=2 under Gaussian drift uncertainty qq and evaluate against the analytic constant qq-reference
([38](https://arxiv.org/html/2601.03175v1#S2.E38 "Equation 38 ‣ CRRA (𝛾≠1): tilted optimality and Gaussian shrinkage. ‣ 2.3.1 Static Gaussian drift uncertainty ‣ 2.3 Gaussian references at a fixed decision time ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).
We track (i) the Monte-Carlo objective estimate J^\widehat{J} during training and (ii) the decision-time error at t=0t=0 via RMSE ([82](https://arxiv.org/html/2601.03175v1#S4.E82 "Equation 82 ‣ 4.1 Benchmark market and evaluation protocol ‣ 4 Breaking the Dimensional Barrier under Drift Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).
Because stochastic optimization produces non-monotone and noisy RMSE curves, we summarize each condition by a robust *tail median*:
the median RMSE over the final evaluation snapshots in the late-training window.
Unless stated otherwise, the projection/teacher direction uses the mixed-moment (pθp\_{\theta}) aggregation.

What is compared in Figure [1](https://arxiv.org/html/2601.03175v1#S4.F1 "Figure 1 ‣ 4.2 High-dimensional CRRA benchmark: projection and amortization ‣ 4 Breaking the Dimensional Barrier under Drift Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection").
Stage 1 (PG–DPO; Section [3.1](https://arxiv.org/html/2601.03175v1#S3.SS1 "3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) trains a deployable θ\theta-blind policy πφ\pi\_{\varphi} by maximizing J^\widehat{J} via pathwise
gradients.
Stage 2 (P–PGDPO; Section [3.2](https://arxiv.org/html/2601.03175v1#S3.SS2 "3.2 Projected PG–DPO under latent 𝜃: 𝑞-aggregated projection and a residual-based policy-gap bound ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) applies a qq-aggregated Pontryagin projection to a Stage 1 checkpoint; we use the residual
form of Section [3.3.1](https://arxiv.org/html/2601.03175v1#S3.SS3.SSS1 "3.3.1 Control-variate (residual) form of the projected rule ‣ 3.3 Coupling stage 1 and stage 2: residual projection and interactive distillation ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection").
Interactive distillation (Section [3.3.2](https://arxiv.org/html/2601.03175v1#S3.SS3.SSS2 "3.3.2 Interactive distillation: projection-guided training and amortized deployment ‣ 3.3 Coupling stage 1 and stage 2: residual projection and interactive distillation ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) treats the Stage 2 projected control as a teacher signal and amortizes it
back into a deployable Stage 1 policy network.

Thus Figure [1](https://arxiv.org/html/2601.03175v1#S4.F1 "Figure 1 ‣ 4.2 High-dimensional CRRA benchmark: projection and amortization ‣ 4 Breaking the Dimensional Barrier under Drift Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection") separates *projection quality* (Stage 2: post-hoc projected, still θ\theta-blind)
from *amortized deployable quality* (Stage 1 distilled: single forward pass).

Stage 2 projection versus amortization: scaling with dimension.
*Aligned geometry.*
For small and moderate uncertainty (s=10−3,10−2s=10^{-3},10^{-2}), Stage 2 delivers a sharp reduction in decision-time error across all tested dimensions,
bringing RMSE down to the 10−510^{-5}–10−410^{-4} range, while Stage 1 policies remain around 10−310^{-3}.
Interactive distillation consistently improves the deployable policy (Stage 1 (distill.) below Stage 1) while leaving Stage 2 essentially unchanged,
confirming the intended division of labor: Stage 2 supplies a structured stationarity-correction signal, and distillation reduces the policy-class
approximation/optimization gap by injecting that signal into πφ\pi\_{\varphi}.

*Misaligned geometry.*
The picture becomes more heterogeneous. For small to moderate uncertainty (s=10−3,10−2s=10^{-3},10^{-2}), Stage 2 still improves decision-time RMSE at small dd,
but its advantage shrinks with dimension and can approach the 10−310^{-3} level by d=100d=100.
For the largest uncertainty scale (s=10−1s=10^{-1}), Stage 1 becomes markedly less reliable, whereas Stage 2 remains substantially better, indicating that
projection can act as a stabilizing correction even when end-to-end learning is stressed.
Across settings, the base and high MC budgets tend to yield similar tail-median RMSE curves, suggesting that linear-in-dd scaling of simulation budgets
is sufficient for stable comparisons in this benchmark.

Mechanism: why misalignment can reduce projection gains.
To explain when and why the projection gains shrink, we analyze Stage 2 diagnostic statistics reported in Appendix [E](https://arxiv.org/html/2601.03175v1#A5 "Appendix E Stage 2 projection diagnostics ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"); see
Figures [3](https://arxiv.org/html/2601.03175v1#A5.F3 "Figure 3 ‣ Appendix E Stage 2 projection diagnostics ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")–[6](https://arxiv.org/html/2601.03175v1#A5.F6 "Figure 6 ‣ Appendix E Stage 2 projection diagnostics ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection").
The diagnostics indicate that the degradation under misalignment is driven primarily by increased stationarity residuals and curvature mismatch, rather
than by catastrophic denominator sign failures:
(i) the Stage 2 residual norm grows with dimension and becomes especially large in the hardest misaligned regime,
(ii) the projection denominator magnitude stays away from zero at typical quantiles, and
(iii) the bad-sign fraction remains negligible, while
(iv) the effective curvature statistic κ\kappa stays near the nominal 1/γ1/\gamma reference in easy regimes but can deviate substantially in the hardest
misaligned/high-uncertainty setting.
These patterns are consistent with the geometric explanation: when PP and Σ\Sigma do not commute, the inverse operations implicit in projection mix
directions and can amplify Monte-Carlo errors in mixed-moment quantities (e.g., 𝔼​[p1​θ]\mathbb{E}[p\_{1}\theta]), especially as dd increases.

![Refer to caption](x2.png)

![Refer to caption](x3.png)

Figure 2: Pathwise sanity check at d=100d=100 under *common random numbers* (same sampled θ\theta and Brownian increments).
Top: aligned geometry. Bottom: misaligned geometry.
Each panel shows log⁡Xt\log X\_{t} trajectories induced by the warm Stage 1 policy (PGDPO), the online Stage 2 P–PGDPO teacher (residual form),
and the analytic qq-reference.

Pathwise sanity check.
Figure [2](https://arxiv.org/html/2601.03175v1#S4.F2 "Figure 2 ‣ 4.2 High-dimensional CRRA benchmark: projection and amortization ‣ 4 Breaking the Dimensional Barrier under Drift Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection") complements the decision-time RMSE with a trajectory-level view under common random numbers.
In the aligned case, the online Stage 2 teacher tracks the analytic qq-reference closely along a realized path and reduces the deviation
Δ​log⁡Xt\Delta\log X\_{t} relative to the warm Stage 1 policy.
In the misaligned case, the teacher can deviate more noticeably under the same common-noise protocol, mirroring the reduced projection advantage in the
hardest regimes of Figure [1](https://arxiv.org/html/2601.03175v1#S4.F1 "Figure 1 ‣ 4.2 High-dimensional CRRA benchmark: projection and amortization ‣ 4 Breaking the Dimensional Barrier under Drift Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection") and motivating amortization/reliability mechanisms in interactive distillation.

Overall, the benchmark highlights a separation of roles.
Stage 2 projection supplies a structured stationarity-correction signal that is particularly effective under aligned uncertainty, and interactive
distillation amortizes this signal into a fast deployable Stage 1 policy.
Under misalignment, projection can become more sensitive as dd and ss grow, consistent with diagnostic evidence of increased residuals and curvature
mismatch; nevertheless, amortization remains a robust route to improving deployable policies under fixed simulation budgets.

### 4.3 A strong RL baseline: PPO, and why it falls short in our benchmark

Why include PPO, and how we match the setting.
Proximal Policy Optimization (PPO) is a widely used and robust model-free policy-gradient baseline for continuous control (schulman2017proximal).
We include PPO to answer a concrete question: can a generic, well-tuned model-free RL method recover the decision-time qq-optimal θ\theta-blind allocation
in our high-dimensional drift-uncertainty benchmark under comparable simulation budgets?
This comparison is especially informative in our static Gaussian benchmark because the target decision-time rule is structurally simple (constant and available
in closed form), so performance gaps primarily reflect optimization difficulty and credit assignment rather than policy-class expressiveness.

Since classical HJB solvers and value-function-based deep PDE surrogates are not practical baselines in the high-dimensional uncertain regime targeted here
(Section [2.4](https://arxiv.org/html/2601.03175v1#S2.SS4 "2.4 Why dynamic programming and deep PDE surrogates break down in high-dimensional uncertain markets ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")), PPO serves as a strong *simulation-only* comparator that operates on the same sampled trajectories without exploiting
value-function PDE structure. For a fair comparison, PPO is trained on the same Euler simulator and time discretization as our PG–DPO pipeline, under the same
deployability restriction (the policy never observes the latent θ\theta), and under the same terminal-utility objective. We also use the same action cap
umaxu\_{\max} (with the same dimension-scaling convention) so that exploration ranges are comparable across dd. Implementation details are deferred to the appendix
and code release.

Empirical outcome.
Table LABEL:tab:crra\_stage12\_distill\_ppo\_landscape shows that PPO remains far from the analytic decision-time qq-reference across essentially all
conditions, with RMSE typically on the order of 10−110^{-1}. In contrast, the Pontryagin-based pipeline attains substantially smaller errors:
in aligned regimes Stage 2 projection reaches the 10−510^{-5}–10−410^{-4} range for small and moderate uncertainty, while in misaligned regimes the
projection advantage narrows but remains systematic. Distillation improves the *deployable* Stage 1 policy relative to basic PG–DPO, but does not
eliminate the remaining gap to the post-hoc projection, consistent with the amortization interpretation in Section [4.2](https://arxiv.org/html/2601.03175v1#S4.SS2 "4.2 High-dimensional CRRA benchmark: projection and amortization ‣ 4 Breaking the Dimensional Barrier under Drift Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection").

Why PPO underperforms in this benchmark.
The gap is not evidence that PPO is intrinsically weak; rather, it reflects that our benchmark stresses regimes where a generic likelihood-ratio
policy gradient is statistically disadvantaged compared to pathwise/adjoint-based updates. With terminal utility as the only reward, PPO faces a
long-horizon credit-assignment problem whose gradient variance grows with both horizon and action dimension. Sampling θ∼q\theta\sim q further creates
episode-wise heterogeneity under a single θ\theta-blind policy, inducing additional variance and potential cancellation across parameter draws.
In contrast, Stage 1 exploits backpropagation through the differentiable simulator (pathwise gradients), and Stage 2 leverages the affine-in-control
Pontryagin structure through a qq-aggregated projection, replacing a noisy high-dimensional policy-gradient update by a structured stationarity
correction that is tailored to the θ\theta-blind ex–ante objective.

Under matched simulation budgets in our latent-θ\theta, θ\theta-blind benchmark, a generic model-free PPO baseline does not reliably recover the
decision-time qq-optimal allocation (Table LABEL:tab:crra\_stage12\_distill\_ppo\_landscape), motivating structure-exploiting alternatives—pathwise
gradients, costates, and the qq-aggregated Pontryagin projection—as in PG–DPO and P–PGDPO.

## 5 Recovering Intertemporal Hedging Demand in Factor-Driven Markets

Sections [4](https://arxiv.org/html/2601.03175v1#S4 "4 Breaking the Dimensional Barrier under Drift Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection") stressed *scaling* under static drift uncertainty, where the target
qq-reference is time-homogeneous and largely myopic. Here we shift the focus to an *economic*
target: recovering the *intertemporal hedging demand* induced by factor-driven investment
opportunities when return shocks are correlated with factor shocks (campbell2002strategic; xia2001learning).

We use the mean-reverting Gaussian premium benchmark of
Section [2.3.2](https://arxiv.org/html/2601.03175v1#S2.SS3.SSS2 "2.3.2 Mean-reverting Gaussian premium and an induced horizon-dependent reference ‣ 2.3 Gaussian references at a fixed decision time ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"). Decision-time statistical uncertainty enters through
the (uncertain) initial premium state Y0∼𝒩​(m0,P0)Y\_{0}\sim\mathcal{N}(m\_{0},P\_{0}), while a nonzero return–factor
correlation ρ\rho generates hedging demand through the cross term Mcross​(T)M\_{\mathrm{cross}}(T) in
([51](https://arxiv.org/html/2601.03175v1#S2.E51 "Equation 51 ‣ CRRA (𝛾>1). ‣ 2.3.2 Mean-reverting Gaussian premium and an induced horizon-dependent reference ‣ 2.3 Gaussian references at a fixed decision time ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")). Crucially, we enforce a *deployable* restriction aligned with
Section [3](https://arxiv.org/html/2601.03175v1#S3 "3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"): the policy is *YY-blind* and does not observe the realized
Y0Y\_{0} nor the path (Yt)(Y\_{t}).

We compare:
(i) Stage 1 PG–DPO (deployable end-to-end learning; Section [3.1](https://arxiv.org/html/2601.03175v1#S3.SS1 "3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")),
(ii) Stage 2 qq-aggregated Pontryagin projection (post-hoc correction in residual form; Sections [3.2](https://arxiv.org/html/2601.03175v1#S3.SS2 "3.2 Projected PG–DPO under latent 𝜃: 𝑞-aggregated projection and a residual-based policy-gap bound ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection") and [3.3.1](https://arxiv.org/html/2601.03175v1#S3.SS3.SSS1 "3.3.1 Control-variate (residual) form of the projected rule ‣ 3.3 Coupling stage 1 and stage 2: residual projection and interactive distillation ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")),
(iii) interactive distillation (amortized projection guidance; Section [3.3.2](https://arxiv.org/html/2601.03175v1#S3.SS3.SSS2 "3.3.2 Interactive distillation: projection-guided training and amortized deployment ‣ 3.3 Coupling stage 1 and stage 2: residual projection and interactive distillation ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")), and
(iv) a model-free PPO baseline trained under the same deployable YY-blind observation restriction.
Performance is measured by decision-time RMSE against the analytic constant-portfolio OU reference
([51](https://arxiv.org/html/2601.03175v1#S2.E51 "Equation 51 ‣ CRRA (𝛾>1). ‣ 2.3.2 Mean-reverting Gaussian premium and an induced horizon-dependent reference ‣ 2.3 Gaussian references at a fixed decision time ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) (which reduces to the independence-case benchmark when ρ=0\rho=0).

In addition to the full allocation error, this benchmark provides a natural *myopic + hedging*
decomposition (driven by return–factor correlation). We therefore report (a) the RMSE of the full
decision-time allocation for all methods (including PPO), and (b) component-wise diagnostics for the
projected (Stage 2) rules: RMSE of the hedging component (Table [1](https://arxiv.org/html/2601.03175v1#S5.T1 "Table 1 ‣ 5.2 Results: hedging-demand recovery, amortization, and robustness to decision-time uncertainty ‣ 5 Recovering Intertemporal Hedging Demand in Factor-Driven Markets ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"))
and, in the appendix, the RMSE of the myopic component (Table [2](https://arxiv.org/html/2601.03175v1#A6.T2 "Table 2 ‣ Appendix F Supplementary decomposition diagnostics for Section 5 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) and
the cosine similarity of the hedging direction (Table [3](https://arxiv.org/html/2601.03175v1#A6.T3 "Table 3 ‣ Appendix F Supplementary decomposition diagnostics for Section 5 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).
Since PPO does not expose a compatible myopic/hedging decomposition for these diagnostics, we include it
only in the full RMSE table.

To keep the main text focused, we include the full RMSE table (Table LABEL:tab:ou\_rmse\_s0\_sweep\_landscape)
and the hedging-RMSE table (Table [1](https://arxiv.org/html/2601.03175v1#S5.T1 "Table 1 ‣ 5.2 Results: hedging-demand recovery, amortization, and robustness to decision-time uncertainty ‣ 5 Recovering Intertemporal Hedging Demand in Factor-Driven Markets ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) in
Section [5.2](https://arxiv.org/html/2601.03175v1#S5.SS2 "5.2 Results: hedging-demand recovery, amortization, and robustness to decision-time uncertainty ‣ 5 Recovering Intertemporal Hedging Demand in Factor-Driven Markets ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"); the remaining two diagnostic tables are deferred to the appendix
(Section [F](https://arxiv.org/html/2601.03175v1#A6 "Appendix F Supplementary decomposition diagnostics for Section 5 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).

### 5.1 Experimental setting

YY-blind deployability (and what uses YY).
Throughout this section, all reported policies are *deployable and YY-blind*: the control is a
function of observable wealth and time-to-go only, and never takes the realized initial premium Y0Y\_{0}
nor the factor path (Yt)(Y\_{t}) as an input (including the PPO baseline). The latent premium factor is
sampled and propagated *only inside the simulator* to generate trajectories and to form Monte Carlo
averages used by the stage 2 projection (and by the teacher in distillation). Any YY-indexed quantities
are used only for offline evaluation and diagnostics.

OU premium market with a hedging channel.
We adopt the OU premium benchmark of Section [2.3.2](https://arxiv.org/html/2601.03175v1#S2.SS3.SSS2 "2.3.2 Mean-reverting Gaussian premium and an induced horizon-dependent reference ‣ 2.3 Gaussian references at a fixed decision time ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"). Let Yt∈ℝmY\_{t}\in\mathbb{R}^{m} be a mean-reverting premium factor and Rt∈ℝdR\_{t}\in\mathbb{R}^{d} the risky excess returns:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Yt\displaystyle dY\_{t} | =κ​(y¯−Yt)​d​t+Ξ​d​WtY,Y0∼𝒩​(m0,P0),\displaystyle=\kappa(\bar{y}-Y\_{t})\,dt+\Xi\,dW\_{t}^{Y},\hskip 18.49988ptY\_{0}\sim\mathcal{N}(m\_{0},P\_{0}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Rt\displaystyle dR\_{t} | :=d​StSt−r​𝟏​d​t=B​Yt​d​t+Σ1/2​d​Wt,\displaystyle:=\frac{dS\_{t}}{S\_{t}}-r\mathbf{1}\,dt=BY\_{t}\,dt+\Sigma^{1/2}\,dW\_{t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​⟨W,WY⟩t\displaystyle d\langle W,W^{Y}\rangle\_{t} | =ρ​d​t.\displaystyle=\rho\,dt. |  |

A nonzero ρ\rho induces intertemporal hedging demand and enters the CRRA decision-time reference through the cross-covariance term Mcross​(T)M\_{\mathrm{cross}}(T) in ([51](https://arxiv.org/html/2601.03175v1#S2.E51 "Equation 51 ‣ CRRA (𝛾>1). ‣ 2.3.2 Mean-reverting Gaussian premium and an induced horizon-dependent reference ‣ 2.3 Gaussian references at a fixed decision time ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")). When ρ=0\rho=0 (independent return and factor shocks), the hedging channel vanishes (Mcross​(T)=0M\_{\mathrm{cross}}(T)=0) and the reference reduces to the independence-case benchmark.

Decision-time uncertainty geometry for Y0∼𝒩​(m0,P0)Y\_{0}\sim\mathcal{N}(m\_{0},P\_{0}).
We control the magnitude of decision-time statistical uncertainty by a scalar s0>0s\_{0}>0 and construct P0P\_{0} from an identification-motivated baseline

|  |  |  |
| --- | --- | --- |
|  | P~0:=(B⊤​Σ−1​B)−1∈ℝm×m.\widetilde{P}\_{0}:=(B^{\top}\Sigma^{-1}B)^{-1}\in\mathbb{R}^{m\times m}. |  |

We consider two geometries. In the *aligned* case, we keep the principal directions of P~0\widetilde{P}\_{0} and rescale it so that the average marginal variance equals s0s\_{0}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P0aligned​(s0):=s0​mtr​(P~0)​P~0,P\_{0}^{\mathrm{aligned}}(s\_{0}):=\frac{s\_{0}\,m}{\mathrm{tr}(\widetilde{P}\_{0})}\,\widetilde{P}\_{0}, |  | (83) |

so that tr​(P0aligned)/m=s0\mathrm{tr}(P\_{0}^{\mathrm{aligned}})/m=s\_{0}. In the *misaligned* case, we preserve the eigenvalue spectrum of P~0\widetilde{P}\_{0} but randomize its eigenvectors via an orthogonal rotation: letting P~0=U​diag​(λ)​U⊤\widetilde{P}\_{0}=U\mathrm{diag}(\lambda)U^{\top} be an eigen-decomposition and drawing an orthogonal matrix RR (e.g., Haar), we define

|  |  |  |  |
| --- | --- | --- | --- |
|  | P0misaligned​(s0):=s0​mtr​(P~0)​U​R​diag​(λ)​R⊤​U⊤,P\_{0}^{\mathrm{misaligned}}(s\_{0}):=\frac{s\_{0}\,m}{\mathrm{tr}(\widetilde{P}\_{0})}\,UR\,\mathrm{diag}(\lambda)\,R^{\top}U^{\top}, |  | (84) |

which matches the same trace normalization while rotating the uncertainty directions away from those of P~0\widetilde{P}\_{0}. We sweep s0∈{10−3,10−2,10−1}s\_{0}\in\{10^{-3},10^{-2},10^{-1}\} under both aligned and misaligned P0P\_{0}.

Two-stage solver, amortization, and evaluation protocol.
We use the two-stage pipeline of Section [3](https://arxiv.org/html/2601.03175v1#S3 "3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"). Stage 1 trains a deployable policy by stochastic gradient ascent using pathwise/BPTT gradients (Section [3.1](https://arxiv.org/html/2601.03175v1#S3.SS1 "3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")). Stage 2 applies the qq-aggregated Pontryagin projection computed under a warm-up policy (Section [3.2](https://arxiv.org/html/2601.03175v1#S3.SS2 "3.2 Projected PG–DPO under latent 𝜃: 𝑞-aggregated projection and a residual-based policy-gap bound ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")), implemented in the residual/control-variate form (Section [3.3.1](https://arxiv.org/html/2601.03175v1#S3.SS3.SSS1 "3.3.1 Control-variate (residual) form of the projected rule ‣ 3.3 Coupling stage 1 and stage 2: residual projection and interactive distillation ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")). Interactive distillation amortizes the projected teacher into a fast deployable policy network (Section [3.3.2](https://arxiv.org/html/2601.03175v1#S3.SS3.SSS2 "3.3.2 Interactive distillation: projection-guided training and amortized deployment ‣ 3.3 Coupling stage 1 and stage 2: residual projection and interactive distillation ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")). As a model-free baseline, we also train a PPO policy under the same YY-blind observation restriction and report its decision-time full RMSE in Table LABEL:tab:ou\_rmse\_s0\_sweep\_landscape.

We sweep d∈{5,10,50,100}d\in\{5,10,50,100\} (one fixed market instance per dd), train for 50005000 epochs, and evaluate every 100100 epochs. Unless stated otherwise we set γ=2\gamma=2, r=0.03r=0.03, κ=1.0\kappa=1.0, ξscale=0.25\xi\_{\mathrm{scale}}=0.25, and ρ=0.5\rho=0.5. We evaluate the decision-time action at t=0t=0 and report RMSE to the analytic constant-portfolio OU reference ([51](https://arxiv.org/html/2601.03175v1#S2.E51 "Equation 51 ‣ CRRA (𝛾>1). ‣ 2.3.2 Mean-reverting Gaussian premium and an induced horizon-dependent reference ‣ 2.3 Gaussian references at a fixed decision time ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).

In addition to the full allocation error, we use the natural *myopic + hedging* decomposition induced by the OU factor structure. We report the RMSE of the full decision-time allocation for all methods, and component-wise diagnostics for the projected (Stage 2) rules, including the RMSE of the hedging component and (in the appendix) the RMSE of the myopic component and cosine similarity of the hedging direction. To reduce noise from stochastic optimization, for each condition we summarize each metric by a *tail median* over the last six evaluation checkpoints.

### 5.2 Results: hedging-demand recovery, amortization, and robustness to decision-time uncertainty

We report decision-time RMSE at t=0t=0 against the analytic OU reference ([51](https://arxiv.org/html/2601.03175v1#S2.E51 "Equation 51 ‣ CRRA (𝛾>1). ‣ 2.3.2 Mean-reverting Gaussian premium and an induced horizon-dependent reference ‣ 2.3 Gaussian references at a fixed decision time ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")). To reduce noise from stochastic optimization, we summarize each condition by a *tail median* over the last six evaluation checkpoints. Table LABEL:tab:ou\_rmse\_s0\_sweep\_landscape reports the full decision-time RMSE for all deployable objects (Stage 1 and Stage 1+Stage 2, with and without distillation), and also includes a model-free PPO baseline trained under the same YY-blind deployability restriction. To isolate the economic channel of interest, Table [1](https://arxiv.org/html/2601.03175v1#S5.T1 "Table 1 ‣ 5.2 Results: hedging-demand recovery, amortization, and robustness to decision-time uncertainty ‣ 5 Recovering Intertemporal Hedging Demand in Factor-Driven Markets ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection") reports the RMSE of the *hedging* component for the post-hoc projected (Stage 2) rules. Two additional diagnostics—the myopic-component RMSE and the hedging-direction cosine similarity—are deferred to the appendix (Tables [2](https://arxiv.org/html/2601.03175v1#A6.T2 "Table 2 ‣ Appendix F Supplementary decomposition diagnostics for Section 5 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection") and [3](https://arxiv.org/html/2601.03175v1#A6.T3 "Table 3 ‣ Appendix F Supplementary decomposition diagnostics for Section 5 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")). Since PPO does not expose a compatible myopic/hedging decomposition in our diagnostic protocol, we report it only in the full-RMSE table.

Projection and economic hedging-demand recovery.
Across all dd and s0s\_{0}, the post-hoc Pontryagin projection (Stage 1+Stage 2) substantially reduces decision-time RMSE relative to the deployable Stage 1 policy (Table LABEL:tab:ou\_rmse\_s0\_sweep\_landscape). For example, under aligned P0P\_{0} with s0=10−3s\_{0}=10^{-3} and d=100d=100, Stage 1 attains 3.54×10−033.54\text{\times}{10}^{-03} whereas Stage 1+Stage 2 achieves 1.56×10−041.56\text{\times}{10}^{-04}. The component-wise diagnostics indicate that the remaining discrepancy is largely driven by the hedging channel: in the same setting, the hedging RMSE is 1.55×10−041.55\text{\times}{10}^{-04} (Basic) and 1.42×10−041.42\text{\times}{10}^{-04} (Distill.) (Table [1](https://arxiv.org/html/2601.03175v1#S5.T1 "Table 1 ‣ 5.2 Results: hedging-demand recovery, amortization, and robustness to decision-time uncertainty ‣ 5 Recovering Intertemporal Hedging Demand in Factor-Driven Markets ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")), while the myopic RMSE is an order of magnitude smaller (Appendix Table [2](https://arxiv.org/html/2601.03175v1#A6.T2 "Table 2 ‣ Appendix F Supplementary decomposition diagnostics for Section 5 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")). This pattern is consistent with the economic mechanism in this benchmark: once the (mostly) myopic component is captured, the dominant remaining challenge is to recover the intertemporal hedge induced by correlated return–factor shocks.

Amortization, robustness, and the PPO baseline.
Interactive distillation improves the *deployable* Stage 1 policy relative to the basic PG–DPO run, while the most accurate object remains the post-hoc projected policy (Table LABEL:tab:ou\_rmse\_s0\_sweep\_landscape). This matches the intended division of labor in Section [3.3](https://arxiv.org/html/2601.03175v1#S3.SS3 "3.3 Coupling stage 1 and stage 2: residual projection and interactive distillation ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"): Stage 2 provides a structured stationarity-correction signal through the aggregated Pontryagin projection, and distillation amortizes that correction into a single forward pass, up to policy-class approximation limits.

As the decision-time uncertainty scale s0s\_{0} increases, both the full RMSE and the hedging-component RMSE increase, with the most visible degradation at s0=10−1s\_{0}=10^{-1}, especially at larger dimensions (Tables LABEL:tab:ou\_rmse\_s0\_sweep\_landscape–[1](https://arxiv.org/html/2601.03175v1#S5.T1 "Table 1 ‣ 5.2 Results: hedging-demand recovery, amortization, and robustness to decision-time uncertainty ‣ 5 Recovering Intertemporal Hedging Demand in Factor-Driven Markets ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")). Misalignment has a limited effect for small and moderate uncertainty scales, but can induce noticeable deterioration in the hardest settings, where the direction-of-hedge diagnostic can also weaken (Appendix Table [3](https://arxiv.org/html/2601.03175v1#A6.T3 "Table 3 ‣ Appendix F Supplementary decomposition diagnostics for Section 5 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).

Finally, the PPO baseline remains far from the analytic OU reference under the same YY-blind deployability restriction, with degradation that becomes especially pronounced at larger dd (Table LABEL:tab:ou\_rmse\_s0\_sweep\_landscape). This is consistent with PPO facing a terminal-only credit-assignment problem under latent-factor heterogeneity, in contrast to the pathwise-sensitivity and affine-in-control correction exploited by our two-stage pipeline. Since PPO does not provide a compatible myopic/hedging decomposition under our evaluation protocol, we include it only in the full-RMSE table.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| s0s\_{0} | Method | d=5d=5 | 1010 | 5050 | 100100 |
| Aligned P0P\_{0} | | | | | |
| 10−310^{-3} | Stage 1+Stage 2 (Basic) | 4.59×10−054.59\text{\times}{10}^{-05} | 4.87×10−054.87\text{\times}{10}^{-05} | 1.37×10−041.37\text{\times}{10}^{-04} | 1.55×10−041.55\text{\times}{10}^{-04} |
| Stage 1+Stage 2 (Distill.) | 4.39×10−054.39\text{\times}{10}^{-05} | 5.25×10−055.25\text{\times}{10}^{-05} | 1.37×10−041.37\text{\times}{10}^{-04} | 1.42×10−041.42\text{\times}{10}^{-04} |
| 10−210^{-2} | Stage 1+Stage 2 (Basic) | 4.98×10−054.98\text{\times}{10}^{-05} | 4.47×10−054.47\text{\times}{10}^{-05} | 1.44×10−041.44\text{\times}{10}^{-04} | 1.74×10−041.74\text{\times}{10}^{-04} |
| Stage 1+Stage 2 (Distill.) | 4.43×10−054.43\text{\times}{10}^{-05} | 4.95×10−054.95\text{\times}{10}^{-05} | 1.47×10−041.47\text{\times}{10}^{-04} | 1.55×10−041.55\text{\times}{10}^{-04} |
| 10−110^{-1} | Stage 1+Stage 2 (Basic) | 5.27×10−055.27\text{\times}{10}^{-05} | 3.99×10−053.99\text{\times}{10}^{-05} | 2.60×10−042.60\text{\times}{10}^{-04} | 2.95×10−042.95\text{\times}{10}^{-04} |
| Stage 1+Stage 2 (Distill.) | 4.72×10−054.72\text{\times}{10}^{-05} | 5.36×10−055.36\text{\times}{10}^{-05} | 2.58×10−042.58\text{\times}{10}^{-04} | 2.86×10−042.86\text{\times}{10}^{-04} |
| Misaligned P0P\_{0} | | | | | |
| 10−310^{-3} | Stage 1+Stage 2 (Basic) | 5.00×10−055.00\text{\times}{10}^{-05} | 4.87×10−054.87\text{\times}{10}^{-05} | 1.34×10−041.34\text{\times}{10}^{-04} | 1.57×10−041.57\text{\times}{10}^{-04} |
| Stage 1+Stage 2 (Distill.) | 4.30×10−054.30\text{\times}{10}^{-05} | 5.33×10−055.33\text{\times}{10}^{-05} | 1.40×10−041.40\text{\times}{10}^{-04} | 1.43×10−041.43\text{\times}{10}^{-04} |
| 10−210^{-2} | Stage 1+Stage 2 (Basic) | 4.93×10−054.93\text{\times}{10}^{-05} | 5.65×10−055.65\text{\times}{10}^{-05} | 1.53×10−041.53\text{\times}{10}^{-04} | 1.75×10−041.75\text{\times}{10}^{-04} |
| Stage 1+Stage 2 (Distill.) | 4.56×10−054.56\text{\times}{10}^{-05} | 6.09×10−056.09\text{\times}{10}^{-05} | 1.53×10−041.53\text{\times}{10}^{-04} | 1.56×10−041.56\text{\times}{10}^{-04} |
| 10−110^{-1} | Stage 1+Stage 2 (Basic) | 5.45×10−055.45\text{\times}{10}^{-05} | 1.55×10−041.55\text{\times}{10}^{-04} | 3.19×10−043.19\text{\times}{10}^{-04} | 3.28×10−043.28\text{\times}{10}^{-04} |
| Stage 1+Stage 2 (Distill.) | 5.20×10−055.20\text{\times}{10}^{-05} | 1.57×10−041.57\text{\times}{10}^{-04} | 3.13×10−043.13\text{\times}{10}^{-04} | 3.20×10−043.20\text{\times}{10}^{-04} |

Table 1: Decision-time RMSE at t=0t=0 for the *hedging component* of the OU decision-time reference, evaluated on the post-hoc projected (Stage 2) policies (tail median over the last six evaluation checkpoints). Component-wise diagnostics are reported for Stage 2 since Stage 1 does not explicitly output a myopic/hedging decomposition.

In a factor-driven market where return–factor correlation induces intertemporal hedging demand, the proposed two-stage pipeline recovers the analytic OU decision-time reference with high accuracy: projection provides the dominant gains, and distillation improves deployable policies by amortizing projection guidance. In contrast, a model-free PPO baseline does not reliably match the analytic reference in this YY-blind setting.

## 6 Conclusion

We studied continuous-time portfolio choice in diffusion markets whose coefficients are estimated and therefore subject to statistical uncertainty (Section [2.1](https://arxiv.org/html/2601.03175v1#S2.SS1 "2.1 Model and ex–ante objective in estimated diffusion markets ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")). We model this uncertainty by an exogenous law q​(d​θ)q(d\theta) over a latent parameter θ\theta that is drawn once at time 0 and remains fixed over the investment horizon, while the investor must deploy a single θ\theta-blind Markov feedback policy evaluated under an ex–ante CRRA objective (Remark [1](https://arxiv.org/html/2601.03175v1#Thmremark1 "Remark 1 (Latent parameter, observability, and admissible controls). ‣ Uncertainty law 𝑞⁢(𝑑⁢𝜃) and information structure. ‣ 2.1 Model and ex–ante objective in estimated diffusion markets ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"), Section [2.1](https://arxiv.org/html/2601.03175v1#S2.SS1 "2.1 Model and ex–ante objective in estimated diffusion markets ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")). This information structure shifts the relevant optimality notion from θ\theta-conditional (full-information) criticality to a qq-aggregated Pontryagin first-order condition that is enforceable within the deployable θ\theta-blind policy class (Section [2.2](https://arxiv.org/html/2601.03175v1#S2.SS2 "2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"), Theorem [1](https://arxiv.org/html/2601.03175v1#Thmtheorem1 "Theorem 1 (𝑞-aggregated first-order condition under latent 𝜃 (deployable 𝜃-blind stationarity)). ‣ 𝑞-aggregated Pontryagin condition for the 𝜃-blind ex–ante problem (Markov feedback). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).

Methodologically, we extended Pontryagin–Guided Direct Policy Optimization (PG–DPO) to the latent-parameter setting by sampling θ\theta only inside the simulator and computing exact discrete-time gradients via BPTT (Section [3.1](https://arxiv.org/html/2601.03175v1#S3.SS1 "3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")), and we leveraged the BPTT–PMP correspondence to extract the costate objects needed for structured control updates (Theorem [2](https://arxiv.org/html/2601.03175v1#Thmtheorem2 "Theorem 2 (BPTT–PMP correspondence (conditional on 𝜃, uniform on compacts)). ‣ Pathwise costates from BPTT and the (conditional) BPTT–PMP correspondence. ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")). Building on the qq-aggregated stationarity, we proposed uncertainty-aware projected PG–DPO (P–PGDPO), which aggregates Monte Carlo Pontryagin quantities across θ∼q\theta\sim q and projects them onto the deployable first-order condition to obtain a single θ\theta-blind rule (Section [3.2](https://arxiv.org/html/2601.03175v1#S3.SS2 "3.2 Projected PG–DPO under latent 𝜃: 𝑞-aggregated projection and a residual-based policy-gap bound ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")). We established a residual-based ex–ante policy-gap bound under local stability of the aggregated projection map, with discretization and Monte Carlo errors made explicit (Theorem [3](https://arxiv.org/html/2601.03175v1#Thmtheorem3 "Theorem 3 (Residual-based ex–ante 𝜃-blind policy-gap bound for P–PGDPO (mixed-moment, deployable, slab-wise local)). ‣ Residual diagnostic and a slab-wise small-gain policy-gap bound. ‣ 3.2 Projected PG–DPO under latent 𝜃: 𝑞-aggregated projection and a residual-based policy-gap bound ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")). In experiments with finite-sample uncertainty, projection improves stability and accuracy in high dimensions and exhibits a two-time-scale stabilization effect (costates versus policies), while interactive distillation amortizes the projection into a fast deployable network (Sections [4](https://arxiv.org/html/2601.03175v1#S4 "4 Breaking the Dimensional Barrier under Drift Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection") and [5](https://arxiv.org/html/2601.03175v1#S5 "5 Recovering Intertemporal Hedging Demand in Factor-Driven Markets ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"); Section [3.3](https://arxiv.org/html/2601.03175v1#S3.SS3 "3.3 Coupling stage 1 and stage 2: residual projection and interactive distillation ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).

Several extensions are natural. A first direction is to allow time-varying uncertainty descriptions qtq\_{t} (e.g., produced by an external filter) and connect the present fixed-qq projection to belief-aware decision rules (Remark [2](https://arxiv.org/html/2601.03175v1#Thmremark2 "Remark 2 (Relation to belief-state/learning formulations). ‣ 𝑞-aggregated Pontryagin condition for the 𝜃-blind ex–ante problem (Markov feedback). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"), Appendix [A](https://arxiv.org/html/2601.03175v1#A1 "Appendix A Online uncertainty updates: Kalman–Bucy filtering and a plug-in decision-time benchmark ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")). A second direction is to incorporate realistic frictions and constraints (transaction costs, leverage and short-sale limits) and develop certified or regularized projection steps when mixed-moment estimation becomes fragile (Section [2.4](https://arxiv.org/html/2601.03175v1#S2.SS4 "2.4 Why dynamic programming and deep PDE surrogates break down in high-dimensional uncertain markets ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"); Section [4.2](https://arxiv.org/html/2601.03175v1#S4.SS2 "4.2 High-dimensional CRRA benchmark: projection and amortization ‣ 4 Breaking the Dimensional Barrier under Drift Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"); Appendix [D.5](https://arxiv.org/html/2601.03175v1#A4.SS5 "D.5 Engineering notes and stabilizers ‣ Appendix D Implementation details for Section 3 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")). Finally, applying the framework to large cross-sectional datasets with modern estimation pipelines would further clarify the practical benefits of inference-agnostic, simulation-only optimization under parameter uncertainty (Section [1](https://arxiv.org/html/2601.03175v1#S1 "1 Introduction ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).

## Acknowledgments

This work was supported by the National Research Foundation of Korea (NRF) grant
funded by the Korea government (MSIT) (RS-2025-00562904).

## Appendix A Online uncertainty updates: Kalman–Bucy filtering and a plug-in decision-time benchmark

Purpose and scope.
Sections [2.3.1](https://arxiv.org/html/2601.03175v1#S2.SS3.SSS1 "2.3.1 Static Gaussian drift uncertainty ‣ 2.3 Gaussian references at a fixed decision time ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection") and [2.3.2](https://arxiv.org/html/2601.03175v1#S2.SS3.SSS2 "2.3.2 Mean-reverting Gaussian premium and an induced horizon-dependent reference ‣ 2.3 Gaussian references at a fixed decision time ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection") focus on *decision-time* benchmarks in which an
uncertainty description qq is treated as given and the investor optimizes under the corresponding θ\theta-blind deployability constraint.
In practice, however, new data arrive and the uncertainty description is updated over time by an external estimation/filtering engine, a viewpoint
that aligns with learning/estimation-risk portfolio choice and Bayesian decision-time formulations (barberis2000investor; pastor2000portfolio; xia2001learning).
This subsection records a simple linear–Gaussian example in which such an updated description qtq\_{t} arises endogenously via a Kalman–Bucy filter
(a canonical partially observed diffusion setting; see, e.g., bensoussan1985optimal; pham2017dynamic),
and then formalizes a *plug-in* workflow: at each decision time, treat the current uncertainty description qtq\_{t} as given and compute a decision-time
optimal control under that qtq\_{t}.
We emphasize that solving the fully optimal partial-observation (belief-state) control problem is *not* the goal of this paper; rather, we view the
resulting qtq\_{t} as an external input to decision-time optimization.
In particular, our simulation-based Pontryagin-guided solvers developed later (Section [3](https://arxiv.org/html/2601.03175v1#S3 "3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) can be used as inner-loop engines that
are refreshed whenever a new uncertainty description qtq\_{t} becomes available.

A linear–Gaussian hidden-premium model (OU state, observed returns).
We use a stylized linear–Gaussian counterpart of the mean-reverting premium setting, but now assume the premium factor is not directly observed.
Let Yt∈ℝmY\_{t}\in\mathbb{R}^{m} be a latent premium factor following an OU dynamics

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Yt=K​(y¯−Yt)​d​t+Ξ​d​WtY,Y0∼𝒩​(y^0,P0),dY\_{t}=K(\bar{y}-Y\_{t})\,dt+\Xi\,dW\_{t}^{Y},\hskip 18.49988ptY\_{0}\sim\mathcal{N}(\hat{y}\_{0},P\_{0}), |  | (85) |

where K∈ℝm×mK\in\mathbb{R}^{m\times m} is stable, y¯∈ℝm\bar{y}\in\mathbb{R}^{m}, and Ξ∈ℝm×m\Xi\in\mathbb{R}^{m\times m}.
Risky assets satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​StSt=r​𝟏​d​t+B​Yt​d​t+Σ1/2​d​Wt,Σ∈ℝd×d​s.p.d.,\frac{dS\_{t}}{S\_{t}}=r\mathbf{1}\,dt+BY\_{t}\,dt+\Sigma^{1/2}\,dW\_{t},\hskip 18.49988pt\Sigma\in\mathbb{R}^{d\times d}\ \text{s.p.d.}, |  | (86) |

with B∈ℝd×mB\in\mathbb{R}^{d\times m}.
Equivalently, the investor observes the excess-return signal

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Zt:=d​StSt−r​𝟏​d​t=B​Yt​d​t+Σ1/2​d​Wt.dZ\_{t}:=\frac{dS\_{t}}{S\_{t}}-r\mathbf{1}\,dt=BY\_{t}\,dt+\Sigma^{1/2}\,dW\_{t}. |  | (87) |

We write 𝔽Z=(ℱtZ)t∈[0,T]\mathbb{F}^{Z}=(\mathcal{F}\_{t}^{Z})\_{t\in[0,T]} for the filtration generated by (Zs)s≤t(Z\_{s})\_{s\leq t}.
For clarity, we present the independent-noise case W⟂WYW\perp W^{Y}; the correlated-noise extension remains linear–Gaussian but leads to more cumbersome gain
formulas.

Kalman–Bucy posterior qt=ℒ​(Yt∣ℱtZ)q\_{t}=\mathcal{L}(Y\_{t}\mid\mathcal{F}\_{t}^{Z}).
Under ([85](https://arxiv.org/html/2601.03175v1#A1.E85 "Equation 85 ‣ Appendix A Online uncertainty updates: Kalman–Bucy filtering and a plug-in decision-time benchmark ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"))–([87](https://arxiv.org/html/2601.03175v1#A1.E87 "Equation 87 ‣ Appendix A Online uncertainty updates: Kalman–Bucy filtering and a plug-in decision-time benchmark ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")), the conditional law of the latent factor remains Gaussian:

|  |  |  |  |
| --- | --- | --- | --- |
|  | qt​(d​y):=ℒ​(Yt∣ℱtZ)=𝒩​(Y^t,Pt),q\_{t}(dy):=\mathcal{L}(Y\_{t}\mid\mathcal{F}\_{t}^{Z})=\mathcal{N}(\hat{Y}\_{t},P\_{t}), |  | (88) |

where (Y^t,Pt)(\hat{Y}\_{t},P\_{t}) satisfy the Kalman–Bucy equations

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Y^t\displaystyle d\hat{Y}\_{t} | =K​(y¯−Y^t)​d​t+Pt​B⊤​Σ−1​(d​Zt−B​Y^t​d​t),\displaystyle=K(\bar{y}-\hat{Y}\_{t})\,dt+P\_{t}B^{\top}\Sigma^{-1}\Big(dZ\_{t}-B\hat{Y}\_{t}\,dt\Big), |  | (89) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | P˙t\displaystyle\dot{P}\_{t} | =K​Pt+Pt​K⊤+Ξ​Ξ⊤−Pt​B⊤​Σ−1​B​Pt,P0​given.\displaystyle=KP\_{t}+P\_{t}K^{\top}+\Xi\Xi^{\top}-P\_{t}B^{\top}\Sigma^{-1}BP\_{t},\hskip 18.49988ptP\_{0}\ \text{given}. |  | (90) |

Thus, even though the posterior qtq\_{t} is a distribution-valued object, in this affine/Gaussian regime it is fully characterized by the finite-dimensional
sufficient statistics (Y^t,Pt)(\hat{Y}\_{t},P\_{t}), with PtP\_{t} evolving deterministically via ([90](https://arxiv.org/html/2601.03175v1#A1.E90 "Equation 90 ‣ Appendix A Online uncertainty updates: Kalman–Bucy filtering and a plug-in decision-time benchmark ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")); this is the prototypical setting in
which belief-state control reduces to finite-dimensional sufficient statistics (bensoussan1985optimal; pham2017dynamic).

From a posterior on YtY\_{t} to a Gaussian uncertainty description for decision-time optimization.
To mirror the decision-time perspective of the OU benchmark, we consider the remaining-horizon time-averaged premium

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ¯t,T:=1T−t​∫tTB​Ys​𝑑s∈ℝd,τ:=T−t.\bar{\theta}\_{t,T}:=\frac{1}{T-t}\int\_{t}^{T}BY\_{s}\,ds\in\mathbb{R}^{d},\hskip 18.49988pt\tau:=T-t. |  | (91) |

For the OU dynamics ([85](https://arxiv.org/html/2601.03175v1#A1.E85 "Equation 85 ‣ Appendix A Online uncertainty updates: Kalman–Bucy filtering and a plug-in decision-time benchmark ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")), one has the decomposition

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫tTYs​𝑑s=τ​y¯+K−1​(I−e−K​τ)​(Yt−y¯)+∫tTK−1​(I−e−K​(T−u))​Ξ​𝑑WuY.\int\_{t}^{T}Y\_{s}\,ds=\tau\bar{y}+K^{-1}\big(I-e^{-K\tau}\big)(Y\_{t}-\bar{y})+\int\_{t}^{T}K^{-1}\big(I-e^{-K(T-u)}\big)\Xi\,dW\_{u}^{Y}. |  | (92) |

Conditioning on ℱtZ\mathcal{F}\_{t}^{Z}, the random variable YtY\_{t} is distributed as 𝒩​(Y^t,Pt)\mathcal{N}(\hat{Y}\_{t},P\_{t}) by ([88](https://arxiv.org/html/2601.03175v1#A1.E88 "Equation 88 ‣ Appendix A Online uncertainty updates: Kalman–Bucy filtering and a plug-in decision-time benchmark ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")), while
the future increments (WuY−WtY)u≥t(W\_{u}^{Y}-W\_{t}^{Y})\_{u\geq t} are independent of ℱtZ\mathcal{F}\_{t}^{Z} in the independent-noise case. Hence θ¯t,T∣ℱtZ\bar{\theta}\_{t,T}\mid\mathcal{F}\_{t}^{Z}
is Gaussian:

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ¯t,T∣ℱtZ∼𝒩​(mt,T,Pt,T),mt,T:=B​mI​(t,T)τ,Pt,T:=1τ2​B​CI​(t,T)​B⊤,\bar{\theta}\_{t,T}\mid\mathcal{F}\_{t}^{Z}\sim\mathcal{N}\!\big(m\_{t,T},\,P\_{t,T}\big),\hskip 18.49988ptm\_{t,T}:=\frac{B\,m\_{I}(t,T)}{\tau},\hskip 18.49988ptP\_{t,T}:=\frac{1}{\tau^{2}}\,B\,C\_{I}(t,T)\,B^{\top}, |  | (93) |

where

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | mI​(t,T)\displaystyle m\_{I}(t,T) | :=τ​y¯+K−1​(I−e−K​τ)​(Y^t−y¯),\displaystyle:=\tau\bar{y}+K^{-1}\big(I-e^{-K\tau}\big)(\hat{Y}\_{t}-\bar{y}), |  | (94) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | CI​(t,T)\displaystyle C\_{I}(t,T) | :=K−1​(I−e−K​τ)​Pt​(I−e−K​τ)⊤​K−⊤+∫0τK−1​(I−e−K​s)​Ξ​Ξ⊤​(I−e−K​s)⊤​K−⊤​𝑑s.\displaystyle:=K^{-1}\big(I-e^{-K\tau}\big)P\_{t}\big(I-e^{-K\tau}\big)^{\top}K^{-\top}+\int\_{0}^{\tau}K^{-1}\big(I-e^{-Ks}\big)\Xi\Xi^{\top}\big(I-e^{-Ks}\big)^{\top}K^{-\top}\,ds. |  | (95) |

Equation ([93](https://arxiv.org/html/2601.03175v1#A1.E93 "Equation 93 ‣ Appendix A Online uncertainty updates: Kalman–Bucy filtering and a plug-in decision-time benchmark ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) provides a concrete example of an *online-updated* Gaussian uncertainty description
qt,T:=ℒ​(θ¯t,T∣ℱtZ)=𝒩​(mt,T,Pt,T).q\_{t,T}:=\mathcal{L}(\bar{\theta}\_{t,T}\mid\mathcal{F}\_{t}^{Z})=\mathcal{N}(m\_{t,T},P\_{t,T}).

A plug-in decision-time benchmark (receding-horizon fixed-qt,Tq\_{t,T}).
Given (mt,T,Pt,T)(m\_{t,T},P\_{t,T}) from ([93](https://arxiv.org/html/2601.03175v1#A1.E93 "Equation 93 ‣ Appendix A Online uncertainty updates: Kalman–Bucy filtering and a plug-in decision-time benchmark ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")), a simple decision-time rule is obtained by treating qt,Tq\_{t,T} as
fixed over the remaining horizon and applying the Gaussian constant-allocation benchmark of Section [2.3.1](https://arxiv.org/html/2601.03175v1#S2.SS3.SSS1 "2.3.1 Static Gaussian drift uncertainty ‣ 2.3 Gaussian references at a fixed decision time ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection") with horizon τ\tau:

|  |  |  |  |
| --- | --- | --- | --- |
|  | πtplug:=(γ​Σ+(γ−1)​τ​Pt,T)−1​mt,T.\pi\_{t}^{\mathrm{plug}}:=\Big(\gamma\,\Sigma+(\gamma-1)\tau\,P\_{t,T}\Big)^{-1}m\_{t,T}. |  | (96) |

One may interpret ([96](https://arxiv.org/html/2601.03175v1#A1.E96 "Equation 96 ‣ Appendix A Online uncertainty updates: Kalman–Bucy filtering and a plug-in decision-time benchmark ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) as a *receding-horizon* decision-time policy driven by an externally updated uncertainty
description, consistent with the general “update beliefs, then optimize” workflow used in Bayesian/learning-based portfolio choice (barberis2000investor; pastor2000portfolio; xia2001learning).

Remarks (relation to belief-aware control).
The plug-in rule ([96](https://arxiv.org/html/2601.03175v1#A1.E96 "Equation 96 ‣ Appendix A Online uncertainty updates: Kalman–Bucy filtering and a plug-in decision-time benchmark ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) is intentionally decision-time: it conditions on the current uncertainty description and does
not attempt to optimize over how the posterior will evolve. In the present paper, we therefore treat the uncertainty law as fixed at a decision time
(either as a fixed qq over a horizon, or as an externally updated sequence of inputs qtq\_{t} that is *not* controlled by the agent), mirroring the
decision-time perspective common in Bayesian/learning portfolio-choice studies (barberis2000investor; pastor2000portfolio; xia2001learning).
Even in linear–Gaussian regimes where the belief state is finite-dimensional, the *fully optimal* partial-observation portfolio problem would treat
the belief state (here, (Y^t,Pt)(\hat{Y}\_{t},P\_{t})) as part of the controlled state and optimize the policy in that enlarged state space (bensoussan1985optimal; pham2017dynamic).
Related necessary conditions under partial information can also be expressed via partial-observation maximum principles (haussmann1987maximum; li1995general; baghery2007maximum).
Developing a belief-aware Pontryagin-guided policy optimizer that operates directly in (x,y,Y^,P)(x,y,\hat{Y},P)-space (or its sufficient-statistic analogues) is an important direction that
we defer to future work.

## Appendix B Proof of Theorem [2](https://arxiv.org/html/2601.03175v1#Thmtheorem2 "Theorem 2 (BPTT–PMP correspondence (conditional on 𝜃, uniform on compacts)). ‣ Pathwise costates from BPTT and the (conditional) BPTT–PMP correspondence. ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")

Theorem [2](https://arxiv.org/html/2601.03175v1#Thmtheorem2 "Theorem 2 (BPTT–PMP correspondence (conditional on 𝜃, uniform on compacts)). ‣ Pathwise costates from BPTT and the (conditional) BPTT–PMP correspondence. ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection") extends the BPTT–PMP (equivalently, BPTT–BSDE)
correspondence established for deterministic-parameter models in our prior work on PG–DPO
(see the main BPTT–BSDE correspondence result and proof in huh2025breaking).
Here the only substantive change is that the market coefficients are indexed by a random but
*frozen* parameter θ∼q\theta\sim q, and we need convergence statements that hold
*conditionally on θ\theta* and uniformly over θ\theta in compact subsets of Θ\Theta.

Important remark (what this proof does *not* use).
This proof concerns the *θ\theta-conditional* Pontryagin adjoint/costate for the fixed-θ\theta
control problem induced by ([53](https://arxiv.org/html/2601.03175v1#S3.E53 "Equation 53 ‣ Setup and objectives (frozen 𝜃, deployable 𝜃-blind feedback). ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"))–([54](https://arxiv.org/html/2601.03175v1#S3.E54 "Equation 54 ‣ Setup and objectives (frozen 𝜃, deployable 𝜃-blind feedback). ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).
It does *not* use the θ\theta-blind qq-aggregated stationarity condition
(Theorem [1](https://arxiv.org/html/2601.03175v1#Thmtheorem1 "Theorem 1 (𝑞-aggregated first-order condition under latent 𝜃 (deployable 𝜃-blind stationarity)). ‣ 𝑞-aggregated Pontryagin condition for the 𝜃-blind ex–ante problem (Markov feedback). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection") in Section [3.2](https://arxiv.org/html/2601.03175v1#S3.SS2 "3.2 Projected PG–DPO under latent 𝜃: 𝑞-aggregated projection and a residual-based policy-gap bound ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).
Those constructions affect only the deployable aggregation/projection target in stage 2 and are irrelevant
to the BPTT–PMP convergence itself.

Notation and filtration.
Fix θ∈Θ\theta\in\Theta. We work conditionally on this θ\theta and consider the augmented
(simulator) filtration

|  |  |  |
| --- | --- | --- |
|  | 𝔾θ:=(𝒢tθ)t∈[0,T],𝒢tθ:=σ​(θ,{Ws,WsY:0≤s≤t})​(with the usual augmentation).\mathbb{G}^{\theta}:=(\mathcal{G}\_{t}^{\theta})\_{t\in[0,T]},\hskip 18.49988pt\mathcal{G}\_{t}^{\theta}:=\sigma\!\big(\theta,\{W\_{s},W\_{s}^{Y}:0\leq s\leq t\}\big)\ \text{(with the usual augmentation)}. |  |

All conditional expectations and L2L^{2} projections below are taken with respect to
𝒢tkθ\mathcal{G}\_{t\_{k}}^{\theta}. This choice matches the information set used by the simulator
and by automatic differentiation/BPTT (which differentiates through the full forward recursion).

Let Δ​t>0\Delta t>0, tk:=k​Δ​tt\_{k}:=k\Delta t, k=0,…,Nk=0,\dots,N, N​Δ​t=TN\Delta t=T.
For readability we suppress the policy parameters φ\varphi and write
πk:=πφ​(tk,Xkθ,Ykθ)\pi\_{k}:=\pi\_{\varphi}(t\_{k},X\_{k}^{\theta},Y\_{k}^{\theta}), where πφ\pi\_{\varphi} is θ\theta-blind in the sense of
([52](https://arxiv.org/html/2601.03175v1#S3.E52 "Equation 52 ‣ Setup and objectives (frozen 𝜃, deployable 𝜃-blind feedback). ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) but evaluated along the θ\theta-conditional trajectory.

Step 1: Conditioning on θ\theta and uniformity of bounds.
Fix a compact set K⊂ΘK\subset\Theta. Assume the coefficients in
([53](https://arxiv.org/html/2601.03175v1#S3.E53 "Equation 53 ‣ Setup and objectives (frozen 𝜃, deployable 𝜃-blind feedback). ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"))–([54](https://arxiv.org/html/2601.03175v1#S3.E54 "Equation 54 ‣ Setup and objectives (frozen 𝜃, deployable 𝜃-blind feedback). ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) satisfy the usual Lipschitz and
linear-growth conditions *uniformly over θ∈K\theta\in K*, and that the block covariance structure
of (W,WY)(W,W^{Y}) (including instantaneous correlation) is uniformly nondegenerate on KK.
Then, for each fixed θ∈K\theta\in K, the controlled SDE system
([53](https://arxiv.org/html/2601.03175v1#S3.E53 "Equation 53 ‣ Setup and objectives (frozen 𝜃, deployable 𝜃-blind feedback). ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"))–([54](https://arxiv.org/html/2601.03175v1#S3.E54 "Equation 54 ‣ Setup and objectives (frozen 𝜃, deployable 𝜃-blind feedback). ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) is well posed and admits uniform-in-time
L2L^{2} moment bounds. Moreover, the Euler–Maruyama scheme enjoys the standard strong error bound

|  |  |  |
| --- | --- | --- |
|  | supt∈[0,T]𝔼​[‖(Xtπ,θ,Ytθ)−(XtΔ​t,θ,YtΔ​t,θ)‖2]1/2≤CK​Δ​t1/2,\sup\_{t\in[0,T]}\mathbb{E}\big[\|(X\_{t}^{\pi,\theta},Y\_{t}^{\theta})-(X\_{t}^{\Delta t,\theta},Y\_{t}^{\Delta t,\theta})\|^{2}\big]^{1/2}\;\leq\;C\_{K}\,\Delta t^{1/2}, |  |

with a constant CKC\_{K} that can be chosen independently of θ∈K\theta\in K.
These are the deterministic assumptions used in huh2025breaking, now stated uniformly on KK.

Step 2: Discrete forward scheme and BPTT pathwise adjoints (fixed θ\theta).
Under fixed θ\theta, consider the Euler scheme for
([53](https://arxiv.org/html/2601.03175v1#S3.E53 "Equation 53 ‣ Setup and objectives (frozen 𝜃, deployable 𝜃-blind feedback). ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"))–([54](https://arxiv.org/html/2601.03175v1#S3.E54 "Equation 54 ‣ Setup and objectives (frozen 𝜃, deployable 𝜃-blind feedback). ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) on the grid (tk)(t\_{k}):

|  |  |  |
| --- | --- | --- |
|  | Yk+1θ=Ykθ+a​(Ykθ,θ)​Δ​t+β​(Ykθ,θ)​Δ​WkY,Y\_{k+1}^{\theta}=Y\_{k}^{\theta}+a(Y\_{k}^{\theta},\theta)\Delta t+\beta(Y\_{k}^{\theta},\theta)\Delta W\_{k}^{Y}, |  |

|  |  |  |
| --- | --- | --- |
|  | Xk+1θ=Xkθ+Xkθ​(r+πk⊤​b​(Ykθ,θ))​Δ​t+Xkθ​πk⊤​σ​(Ykθ,θ)​Δ​Wk,X\_{k+1}^{\theta}=X\_{k}^{\theta}+X\_{k}^{\theta}\Big(r+\pi\_{k}^{\top}b(Y\_{k}^{\theta},\theta)\Big)\Delta t+X\_{k}^{\theta}\,\pi\_{k}^{\top}\sigma(Y\_{k}^{\theta},\theta)\Delta W\_{k}, |  |

with terminal reward U​(XNθ)U(X\_{N}^{\theta}).
Define the discrete (pathwise) wealth costate

|  |  |  |
| --- | --- | --- |
|  | pkpw,θ:=∂∂Xkθ​U​(XNθ),k=0,…,N,p\_{k}^{\mathrm{pw},\theta}:=\frac{\partial}{\partial X\_{k}^{\theta}}\,U(X\_{N}^{\theta}),\hskip 18.49988ptk=0,\dots,N, |  |

which is the same object as ([59](https://arxiv.org/html/2601.03175v1#S3.E59 "Equation 59 ‣ Pathwise costates from BPTT and the (conditional) BPTT–PMP correspondence. ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) (episode indices suppressed and
dependence on θ\theta made explicit).
For the projected-control constructions we also consider the additional pathwise objects

|  |  |  |
| --- | --- | --- |
|  | px,kpw,θ:=∂pkpw,θ∂Xkθ,py,kpw,θ:=∂pkpw,θ∂Ykθ,p\_{x,k}^{\mathrm{pw},\theta}:=\frac{\partial p\_{k}^{\mathrm{pw},\theta}}{\partial X\_{k}^{\theta}},\hskip 18.49988ptp\_{y,k}^{\mathrm{pw},\theta}:=\frac{\partial p\_{k}^{\mathrm{pw},\theta}}{\partial Y\_{k}^{\theta}}, |  |

which correspond to ([60](https://arxiv.org/html/2601.03175v1#S3.E60 "Equation 60 ‣ Pathwise costates from BPTT and the (conditional) BPTT–PMP correspondence. ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).
Automatic differentiation/BPTT computes
{(pkpw,θ,px,kpw,θ,py,kpw,θ)}k=0N\{(p\_{k}^{\mathrm{pw},\theta},p\_{x,k}^{\mathrm{pw},\theta},p\_{y,k}^{\mathrm{pw},\theta})\}\_{k=0}^{N}
via the backward chain rule along the discrete forward graph.

The algebraic form of the one-step backward recursion coincides with the deterministic-parameter analysis
in huh2025breaking, with the replacements

|  |  |  |
| --- | --- | --- |
|  | μ↦b​(⋅,θ),σ↦σ​(⋅,θ),\mu\mapsto b(\cdot,\theta),\hskip 18.49988pt\sigma\mapsto\sigma(\cdot,\theta), |  |

and with the factor block (Yθ,Δ​WY)(Y^{\theta},\Delta W^{Y}) handled exactly as in the wealth–factor extension therein.
All one-step remainder terms are controlled by standard Taylor/Euler estimates with constants uniform in θ∈K\theta\in K.

Step 3: One-step L2L^{2} projection and discrete BSDE form (fixed θ\theta).
Fix θ∈K\theta\in K. As in huh2025breaking, take the conditional L2L^{2}-projection of
pk+1pw,θp\_{k+1}^{\mathrm{pw},\theta} onto span​{1,Δ​Wk,Δ​WkY}\mathrm{span}\{1,\Delta W\_{k},\Delta W\_{k}^{Y}\} given
𝒢tkθ\mathcal{G}\_{t\_{k}}^{\theta}:

|  |  |  |
| --- | --- | --- |
|  | pk+1pw,θ=𝔼​[pk+1pw,θ∣𝒢tkθ]+zkθ​Δ​Wk+z~kθ​Δ​WkY+εk+1θ,p\_{k+1}^{\mathrm{pw},\theta}=\mathbb{E}\!\left[p\_{k+1}^{\mathrm{pw},\theta}\mid\mathcal{G}\_{t\_{k}}^{\theta}\right]+z\_{k}^{\theta}\Delta W\_{k}+\tilde{z}\_{k}^{\theta}\Delta W\_{k}^{Y}+\varepsilon\_{k+1}^{\theta}, |  |

where εk+1θ\varepsilon\_{k+1}^{\theta} is orthogonal (in L2L^{2}) to
span​{1,Δ​Wk,Δ​WkY}\mathrm{span}\{1,\Delta W\_{k},\Delta W\_{k}^{Y}\} conditionally on 𝒢tkθ\mathcal{G}\_{t\_{k}}^{\theta}.
Uniform nondegeneracy of the block covariance of (Δ​Wk,Δ​WkY)(\Delta W\_{k},\Delta W\_{k}^{Y}) yields unique projection
coefficients (zkθ,z~kθ)(z\_{k}^{\theta},\tilde{z}\_{k}^{\theta}).

Substituting this projection into the BPTT backward recursion from Step 2 yields a canonical discrete BSDE
representation for (pkpw,θ,zkθ,z~kθ)(p\_{k}^{\mathrm{pw},\theta},z\_{k}^{\theta},\tilde{z}\_{k}^{\theta}) whose drift matches the Euler
discretization of the θ\theta-conditional Pontryagin adjoint BSDE associated with
([53](https://arxiv.org/html/2601.03175v1#S3.E53 "Equation 53 ‣ Setup and objectives (frozen 𝜃, deployable 𝜃-blind feedback). ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"))–([54](https://arxiv.org/html/2601.03175v1#S3.E54 "Equation 54 ‣ Setup and objectives (frozen 𝜃, deployable 𝜃-blind feedback). ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).
The same argument applies to the derivatives (px,kpw,θ,py,kpw,θ)(p\_{x,k}^{\mathrm{pw},\theta},p\_{y,k}^{\mathrm{pw},\theta}):
they satisfy linearized discrete backward recursions obtained by differentiating the discrete adjoint equations,
hence admit analogous discrete-BSDE representations with coefficients uniformly controlled on KK.

Step 4: Passage to continuous time and identification with the PMP costate.
For each fixed θ∈K\theta\in K, the forward SDE and the θ\theta-conditional adjoint BSDE form a standard
FBSDE with coefficients parametrized by θ\theta.
Let (ptθ,px,tθ,py,tθ)(p\_{t}^{\theta},p\_{x,t}^{\theta},p\_{y,t}^{\theta}) denote the continuous-time θ\theta-conditional Pontryagin objects
under policy πφ\pi\_{\varphi}, so pTθ=U′​(XTπ,θ)p\_{T}^{\theta}=U^{\prime}(X\_{T}^{\pi,\theta}).

Define the piecewise-constant interpolations

|  |  |  |
| --- | --- | --- |
|  | ptΔ​t,θ:=pkpw,θ,px,tΔ​t,θ:=px,kpw,θ,py,tΔ​t,θ:=py,kpw,θ,t∈[tk,tk+1).p\_{t}^{\Delta t,\theta}:=p\_{k}^{\mathrm{pw},\theta},\qquad p\_{x,t}^{\Delta t,\theta}:=p\_{x,k}^{\mathrm{pw},\theta},\qquad p\_{y,t}^{\Delta t,\theta}:=p\_{y,k}^{\mathrm{pw},\theta},\hskip 18.49988ptt\in[t\_{k},t\_{k+1}). |  |

By the same stability and convergence arguments as in huh2025breaking
(Euler convergence for the forward equation plus discrete-BSDE convergence for the backward equation),
we obtain, for each fixed θ∈K\theta\in K,

|  |  |  |
| --- | --- | --- |
|  | supt∈[0,T]𝔼​[|ptΔ​t,θ−ptθ|2]→0,supt∈[0,T]𝔼​[‖px,tΔ​t,θ−px,tθ‖2]→0,supt∈[0,T]𝔼​[‖py,tΔ​t,θ−py,tθ‖2]→0,\sup\_{t\in[0,T]}\mathbb{E}\big[\,|p\_{t}^{\Delta t,\theta}-p\_{t}^{\theta}|^{2}\,\big]\to 0,\hskip 18.49988pt\sup\_{t\in[0,T]}\mathbb{E}\big[\,\|p\_{x,t}^{\Delta t,\theta}-p\_{x,t}^{\theta}\|^{2}\,\big]\to 0,\hskip 18.49988pt\sup\_{t\in[0,T]}\mathbb{E}\big[\,\|p\_{y,t}^{\Delta t,\theta}-p\_{y,t}^{\theta}\|^{2}\,\big]\to 0, |  |

as Δ​t→0\Delta t\to 0.
Because all Lipschitz, growth, ellipticity, and covariance constants were assumed uniform on KK,
the convergence constants can be chosen independently of θ∈K\theta\in K.
This yields the claimed BPTT–PMP correspondence conditionally on θ\theta and uniformly over θ\theta
in compact subsets of Θ\Theta, completing the proof.
∎

## Appendix C Auxiliary results for Theorem [3](https://arxiv.org/html/2601.03175v1#Thmtheorem3 "Theorem 3 (Residual-based ex–ante 𝜃-blind policy-gap bound for P–PGDPO (mixed-moment, deployable, slab-wise local)). ‣ Residual diagnostic and a slab-wise small-gain policy-gap bound. ‣ 3.2 Projected PG–DPO under latent 𝜃: 𝑞-aggregated projection and a residual-based policy-gap bound ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")

### C.1 Stability of the projection map (A,G)↦−A−1​G(A,G)\mapsto-A^{-1}G

###### Proposition 1 (Stability of the projection map (A,G)↦−A−1​G(A,G)\mapsto-A^{-1}G).

Let DD be a measurable domain and let μ\mu be a reference measure on DD.
Let A,A~:D→ℝd×dA,\widetilde{A}:D\to\mathbb{R}^{d\times d} and G,G~:D→ℝdG,\widetilde{G}:D\to\mathbb{R}^{d} be measurable.
Assume:

1. (i)

   A​(z)A(z) is invertible for μ\mu-a.e. z∈Dz\in D and ‖A−1‖L∞​(D)≤κ\|A^{-1}\|\_{L^{\infty}(D)}\leq\kappa for some κ>0\kappa>0;
2. (ii)

   ‖G‖L∞​(D)≤M\|G\|\_{L^{\infty}(D)}\leq M for some M>0M>0;
3. (iii)

   ‖A~−A‖L∞​(D)≤(2​κ)−1\|\widetilde{A}-A\|\_{L^{\infty}(D)}\leq(2\kappa)^{-1}.

Define π:=−A−1​G\pi:=-A^{-1}G and π~:=−A~−1​G~\widetilde{\pi}:=-\widetilde{A}^{-1}\widetilde{G}.
Then A~​(z)\widetilde{A}(z) is invertible for μ\mu-a.e. z∈Dz\in D with ‖A~−1‖L∞​(D)≤2​κ\|\widetilde{A}^{-1}\|\_{L^{\infty}(D)}\leq 2\kappa, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖π~−π‖L2​(μ)≤ 2​κ​‖G~−G‖L2​(μ)+ 2​κ2​(M+‖G~‖L∞​(D))​‖A~−A‖L2​(μ).\|\widetilde{\pi}-\pi\|\_{L^{2}(\mu)}\;\leq\;2\kappa\,\|\widetilde{G}-G\|\_{L^{2}(\mu)}\;+\;2\kappa^{2}\,\big(M+\|\widetilde{G}\|\_{L^{\infty}(D)}\big)\,\|\widetilde{A}-A\|\_{L^{2}(\mu)}. |  | (97) |

###### Proof.

Throughout, ∥⋅∥\|\cdot\| denotes the operator norm induced by the Euclidean norm.
For a matrix-valued function M:D→ℝd×dM:D\to\mathbb{R}^{d\times d}, write

|  |  |  |
| --- | --- | --- |
|  | ‖M‖L∞​(D):=ess​supz∈D⁡‖M​(z)‖,‖M‖L2​(μ):=(∫D‖M​(z)‖2​μ​(d​z))1/2,\|M\|\_{L^{\infty}(D)}:=\operatorname\*{ess\,sup}\_{z\in D}\|M(z)\|,\hskip 18.49988pt\|M\|\_{L^{2}(\mu)}:=\Big(\int\_{D}\|M(z)\|^{2}\,\mu(dz)\Big)^{1/2}, |  |

and similarly for vector-valued functions.

Step 1: Invertibility and inverse bound for A~\widetilde{A}.
Fix z∈Dz\in D such that A​(z)A(z) is invertible (this holds for μ\mu-a.e. zz).
Let E​(z):=A~​(z)−A​(z)E(z):=\widetilde{A}(z)-A(z). By (i) and (iii),

|  |  |  |
| --- | --- | --- |
|  | ‖A​(z)−1​E​(z)‖≤‖A​(z)−1‖​‖E​(z)‖≤‖A−1‖L∞​(D)​‖A~−A‖L∞​(D)≤κ⋅12​κ=12.\|A(z)^{-1}E(z)\|\leq\|A(z)^{-1}\|\,\|E(z)\|\leq\|A^{-1}\|\_{L^{\infty}(D)}\,\|\widetilde{A}-A\|\_{L^{\infty}(D)}\leq\kappa\cdot\frac{1}{2\kappa}=\frac{1}{2}. |  |

Hence I+A​(z)−1​E​(z)I+A(z)^{-1}E(z) is invertible and admits the Neumann-series inverse. Therefore,

|  |  |  |
| --- | --- | --- |
|  | A~​(z)−1=(A​(z)+E​(z))−1=(I+A​(z)−1​E​(z))−1​A​(z)−1,\widetilde{A}(z)^{-1}=(A(z)+E(z))^{-1}=(I+A(z)^{-1}E(z))^{-1}A(z)^{-1}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | ‖A~​(z)−1‖≤11−‖A​(z)−1​E​(z)‖​‖A​(z)−1‖≤11−1/2​κ=2​κ.\|\widetilde{A}(z)^{-1}\|\leq\frac{1}{1-\|A(z)^{-1}E(z)\|}\,\|A(z)^{-1}\|\leq\frac{1}{1-1/2}\,\kappa=2\kappa. |  |

Taking the essential supremum over z∈Dz\in D yields

|  |  |  |
| --- | --- | --- |
|  | ‖A~−1‖L∞​(D)≤2​κ.\|\widetilde{A}^{-1}\|\_{L^{\infty}(D)}\leq 2\kappa. |  |

Step 2: A pointwise bound for A~−1−A−1\widetilde{A}^{-1}-A^{-1}.
For μ\mu-a.e. z∈Dz\in D where both inverses exist,

|  |  |  |
| --- | --- | --- |
|  | A~​(z)−1−A​(z)−1=A~​(z)−1​(A​(z)−A~​(z))​A​(z)−1.\widetilde{A}(z)^{-1}-A(z)^{-1}=\widetilde{A}(z)^{-1}\big(A(z)-\widetilde{A}(z)\big)A(z)^{-1}. |  |

Thus,

|  |  |  |
| --- | --- | --- |
|  | ‖A~​(z)−1−A​(z)−1‖≤‖A~​(z)−1‖​‖A~​(z)−A​(z)‖​‖A​(z)−1‖≤(2​κ)​‖A~​(z)−A​(z)‖​κ=2​κ2​‖A~​(z)−A​(z)‖.\|\widetilde{A}(z)^{-1}-A(z)^{-1}\|\leq\|\widetilde{A}(z)^{-1}\|\,\|\widetilde{A}(z)-A(z)\|\,\|A(z)^{-1}\|\leq(2\kappa)\,\|\widetilde{A}(z)-A(z)\|\,\kappa=2\kappa^{2}\|\widetilde{A}(z)-A(z)\|. |  |

Consequently,

|  |  |  |
| --- | --- | --- |
|  | ‖A~−1−A−1‖L2​(μ)≤2​κ2​‖A~−A‖L2​(μ).\|\widetilde{A}^{-1}-A^{-1}\|\_{L^{2}(\mu)}\leq 2\kappa^{2}\,\|\widetilde{A}-A\|\_{L^{2}(\mu)}. |  |

Step 3: Control error bound.
Recall π=−A−1​G\pi=-A^{-1}G and π~=−A~−1​G~\widetilde{\pi}=-\widetilde{A}^{-1}\widetilde{G}. Then

|  |  |  |
| --- | --- | --- |
|  | π~−π=−A~−1​(G~−G)−(A~−1−A−1)​G.\widetilde{\pi}-\pi=-\widetilde{A}^{-1}(\widetilde{G}-G)-(\widetilde{A}^{-1}-A^{-1})G. |  |

Taking L2​(μ)L^{2}(\mu) norms and using Hölder (L∞×L2→L2L^{\infty}\times L^{2}\to L^{2}) gives

|  |  |  |
| --- | --- | --- |
|  | ‖π~−π‖L2​(μ)≤‖A~−1‖L∞​(D)​‖G~−G‖L2​(μ)+‖A~−1−A−1‖L2​(μ)​‖G‖L∞​(D).\|\widetilde{\pi}-\pi\|\_{L^{2}(\mu)}\leq\|\widetilde{A}^{-1}\|\_{L^{\infty}(D)}\,\|\widetilde{G}-G\|\_{L^{2}(\mu)}+\|\widetilde{A}^{-1}-A^{-1}\|\_{L^{2}(\mu)}\,\|G\|\_{L^{\infty}(D)}. |  |

Using ‖A~−1‖L∞​(D)≤2​κ\|\widetilde{A}^{-1}\|\_{L^{\infty}(D)}\leq 2\kappa (Step 1),
‖G‖L∞​(D)≤M\|G\|\_{L^{\infty}(D)}\leq M (assumption (ii)), and Step 2, we obtain

|  |  |  |
| --- | --- | --- |
|  | ‖π~−π‖L2​(μ)≤2​κ​‖G~−G‖L2​(μ)+2​κ2​M​‖A~−A‖L2​(μ).\|\widetilde{\pi}-\pi\|\_{L^{2}(\mu)}\leq 2\kappa\,\|\widetilde{G}-G\|\_{L^{2}(\mu)}+2\kappa^{2}\,M\,\|\widetilde{A}-A\|\_{L^{2}(\mu)}. |  |

Finally, since M≤M+‖G~‖L∞​(D)M\leq M+\|\widetilde{G}\|\_{L^{\infty}(D)}, this implies ([97](https://arxiv.org/html/2601.03175v1#A3.E97 "Equation 97 ‣ Proposition 1 (Stability of the projection map (𝐴,𝐺)↦-𝐴⁻¹⁢𝐺). ‣ C.1 Stability of the projection map (𝐴,𝐺)↦-𝐴⁻¹⁢𝐺 ‣ Appendix C Auxiliary results for Theorem 3 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).
∎

### C.2 Slab-wise small-gain for the qq-aggregated projection inputs

##### Time-slab decomposition.

In the portfolio problem the working domain DD carries a time coordinate; for concreteness, assume

|  |  |  |
| --- | --- | --- |
|  | D⊂[0,T]×𝒮,μ​(d​t,d​ξ)=d​t⊗ν​(d​ξ),D\subset[0,T]\times\mathcal{S},\hskip 18.49988pt\mu(dt,d\xi)=dt\otimes\nu(d\xi), |  |

for some reference measure ν\nu on 𝒮\mathcal{S}.
Fix a partition 0=t0<t1<⋯<tK=T0=t\_{0}<t\_{1}<\cdots<t\_{K}=T with slab lengths τk:=tk−tk−1\tau\_{k}:=t\_{k}-t\_{k-1} and define

|  |  |  |
| --- | --- | --- |
|  | Dk:=D∩([tk−1,tk]×𝒮),μk:=μ|Dk,‖f‖k:=‖f‖L2​(μk).D\_{k}:=D\cap\big([t\_{k-1},t\_{k}]\times\mathcal{S}\big),\hskip 18.49988pt\mu\_{k}:=\mu|\_{D\_{k}},\hskip 18.49988pt\|f\|\_{k}:=\|f\|\_{L^{2}(\mu\_{k})}. |  |

Then ‖f‖L2​(μ)2=∑k=1K‖f‖k2\|f\|\_{L^{2}(\mu)}^{2}=\sum\_{k=1}^{K}\|f\|\_{k}^{2}.

###### Proposition 2 (Short-time (slab) Lipschitz gain).

Let 𝒰\mathcal{U} be a neighborhood of π⋆\pi^{\star} in the deployable θ\theta-blind policy class
such that for all π∈𝒰\pi\in\mathcal{U},

|  |  |  |
| --- | --- | --- |
|  | ‖Aπ−1‖L∞​(D)≤κ,‖Gπmix‖L∞​(D)≤MG.\|A\_{\pi}^{-1}\|\_{L^{\infty}(D)}\leq\kappa,\hskip 18.49988pt\|G\_{\pi}^{\mathrm{mix}}\|\_{L^{\infty}(D)}\leq M\_{G}. |  |

Assume that on each slab DkD\_{k} the qq-aggregated projection inputs satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Aπ1−Aπ2‖k≤L¯A​τk1/2​‖π1−π2‖k,‖Gπ1mix−Gπ2mix‖k≤L¯G​τk1/2​‖π1−π2‖k,\|A\_{\pi\_{1}}-A\_{\pi\_{2}}\|\_{k}\leq\bar{L}\_{A}\,\tau\_{k}^{1/2}\,\|\pi\_{1}-\pi\_{2}\|\_{k},\hskip 18.49988pt\|G\_{\pi\_{1}}^{\mathrm{mix}}-G\_{\pi\_{2}}^{\mathrm{mix}}\|\_{k}\leq\bar{L}\_{G}\,\tau\_{k}^{1/2}\,\|\pi\_{1}-\pi\_{2}\|\_{k}, |  | (98) |

for all π1,π2∈𝒰\pi\_{1},\pi\_{2}\in\mathcal{U} and constants L¯A,L¯G>0\bar{L}\_{A},\bar{L}\_{G}>0 that depend only on band data.
Define

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ​(τ):=(κ​L¯G+κ2​MG​L¯A)​τ1/2.\rho(\tau):=\Big(\kappa\bar{L}\_{G}+\kappa^{2}M\_{G}\bar{L}\_{A}\Big)\tau^{1/2}. |  | (99) |

Then for each slab DkD\_{k} and all π1,π2∈𝒰\pi\_{1},\pi\_{2}\in\mathcal{U},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖T​(π1)−T​(π2)‖k≤ρ​(τk)​‖π1−π2‖k,T​(π):=−Aπ−1​Gπmix.\|T(\pi\_{1})-T(\pi\_{2})\|\_{k}\;\leq\;\rho(\tau\_{k})\,\|\pi\_{1}-\pi\_{2}\|\_{k},\hskip 18.49988ptT(\pi):=-A\_{\pi}^{-1}G\_{\pi}^{\mathrm{mix}}. |  | (100) |

In particular, if the partition is chosen with maxk⁡τk≤τ⋆\max\_{k}\tau\_{k}\leq\tau^{\star} for some τ⋆>0\tau^{\star}>0
such that ρ​(τ⋆)<1\rho(\tau^{\star})<1, then

|  |  |  |
| --- | --- | --- |
|  | ρ∗:=max1≤k≤K⁡ρ​(τk)<1\rho\_{\*}:=\max\_{1\leq k\leq K}\rho(\tau\_{k})<1 |  |

and TT is a contraction on every slab with constant at most ρ∗\rho\_{\*}.

###### Proof.

Fix kk and π1,π2∈𝒰\pi\_{1},\pi\_{2}\in\mathcal{U}. Write Ai:=AπiA\_{i}:=A\_{\pi\_{i}} and Gi:=GπimixG\_{i}:=G\_{\pi\_{i}}^{\mathrm{mix}}.
Then

|  |  |  |
| --- | --- | --- |
|  | T​(π1)−T​(π2)=−A1−1​(G1−G2)−(A1−1−A2−1)​G2,T(\pi\_{1})-T(\pi\_{2})=-A\_{1}^{-1}(G\_{1}-G\_{2})-(A\_{1}^{-1}-A\_{2}^{-1})G\_{2}, |  |

and

|  |  |  |
| --- | --- | --- |
|  | A1−1−A2−1=A1−1​(A2−A1)​A2−1.A\_{1}^{-1}-A\_{2}^{-1}=A\_{1}^{-1}(A\_{2}-A\_{1})A\_{2}^{-1}. |  |

Using Hölder (L∞×L2→L2L^{\infty}\times L^{2}\to L^{2}) on DkD\_{k} together with
‖Ai−1‖L∞​(D)≤κ\|A\_{i}^{-1}\|\_{L^{\infty}(D)}\leq\kappa and ‖G2‖L∞​(D)≤MG\|G\_{2}\|\_{L^{\infty}(D)}\leq M\_{G}, we obtain

|  |  |  |
| --- | --- | --- |
|  | ‖T​(π1)−T​(π2)‖k≤κ​‖G1−G2‖k+κ2​MG​‖A1−A2‖k.\|T(\pi\_{1})-T(\pi\_{2})\|\_{k}\leq\kappa\,\|G\_{1}-G\_{2}\|\_{k}+\kappa^{2}M\_{G}\,\|A\_{1}-A\_{2}\|\_{k}. |  |

Applying ([98](https://arxiv.org/html/2601.03175v1#A3.E98 "Equation 98 ‣ Proposition 2 (Short-time (slab) Lipschitz gain). ‣ Time-slab decomposition. ‣ C.2 Slab-wise small-gain for the 𝑞-aggregated projection inputs ‣ Appendix C Auxiliary results for Theorem 3 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) yields ([100](https://arxiv.org/html/2601.03175v1#A3.E100 "Equation 100 ‣ Proposition 2 (Short-time (slab) Lipschitz gain). ‣ Time-slab decomposition. ‣ C.2 Slab-wise small-gain for the 𝑞-aggregated projection inputs ‣ Appendix C Auxiliary results for Theorem 3 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) with ρ​(τk)\rho(\tau\_{k}) as in ([99](https://arxiv.org/html/2601.03175v1#A3.E99 "Equation 99 ‣ Proposition 2 (Short-time (slab) Lipschitz gain). ‣ Time-slab decomposition. ‣ C.2 Slab-wise small-gain for the 𝑞-aggregated projection inputs ‣ Appendix C Auxiliary results for Theorem 3 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).
∎

###### Remark 3 (Verification of the τ1/2\tau^{1/2} gain and relation to prior slab analyses).

The τ1/2\tau^{1/2}-gain in ([98](https://arxiv.org/html/2601.03175v1#A3.E98 "Equation 98 ‣ Proposition 2 (Short-time (slab) Lipschitz gain). ‣ Time-slab decomposition. ‣ C.2 Slab-wise small-gain for the 𝑞-aggregated projection inputs ‣ Appendix C Auxiliary results for Theorem 3 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) is the same short-time parabolic smoothing
effect used in our prior PGDPO analysis (see, e.g., huh2025breaking):
one combines a Duhamel/semigroup representation of the relevant adjoint/costate objects with Young-type
convolution bounds to obtain a factor τ1/2\tau^{1/2} on each short slab.
In the present paper, the only additional bookkeeping is that (Aπ,Gπmix)(A\_{\pi},G\_{\pi}^{\mathrm{mix}}) are qq-aggregated
(in particular, linear expectations over θ\theta), which does not alter the semigroup estimates;
it only changes constants through coefficient bounds uniform in θ\theta on the compact parameter set.

### C.3 Proof of Theorem [3](https://arxiv.org/html/2601.03175v1#Thmtheorem3 "Theorem 3 (Residual-based ex–ante 𝜃-blind policy-gap bound for P–PGDPO (mixed-moment, deployable, slab-wise local)). ‣ Residual diagnostic and a slab-wise small-gain policy-gap bound. ‣ 3.2 Projected PG–DPO under latent 𝜃: 𝑞-aggregated projection and a residual-based policy-gap bound ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")

##### Setup.

Let DD be the working domain with reference measure μ\mu and slab decomposition
{Dk,μk,∥⋅∥k}k=1K\{D\_{k},\mu\_{k},\|\cdot\|\_{k}\}\_{k=1}^{K} as in Appendix [C.2](https://arxiv.org/html/2601.03175v1#A3.SS2 "C.2 Slab-wise small-gain for the 𝑞-aggregated projection inputs ‣ Appendix C Auxiliary results for Theorem 3 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection").
For a deployable θ\theta-blind policy π\pi, write (Aπ,Gπmix)(A\_{\pi},G\_{\pi}^{\mathrm{mix}}) for the
qq-aggregated projection inputs corresponding to the *mixed-moment* aggregation in
([65](https://arxiv.org/html/2601.03175v1#S3.E65 "Equation 65 ‣ Mixed-moment 𝑞-aggregation under a warm-up policy. ‣ 3.2 Projected PG–DPO under latent 𝜃: 𝑞-aggregated projection and a residual-based policy-gap bound ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"))–([66](https://arxiv.org/html/2601.03175v1#S3.E66 "Equation 66 ‣ Mixed-moment 𝑞-aggregation under a warm-up policy. ‣ 3.2 Projected PG–DPO under latent 𝜃: 𝑞-aggregated projection and a residual-based policy-gap bound ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")). Define the projection map

|  |  |  |
| --- | --- | --- |
|  | T​(π)​(z):=−Aπ​(z)−1​Gπmix​(z),z∈D,T(\pi)(z):=-A\_{\pi}(z)^{-1}G\_{\pi}^{\mathrm{mix}}(z),\hskip 18.49988ptz\in D, |  |

whenever Aπ​(z)A\_{\pi}(z) is invertible.

Let πwarm\pi^{\mathrm{warm}} be the warm-up policy and set

|  |  |  |
| --- | --- | --- |
|  | Awarm:=Aπwarm,Gwarm:=Gπwarmmix,πproj:=T​(πwarm)=−Awarm−1​Gwarm.A\_{\mathrm{warm}}:=A\_{\pi^{\mathrm{warm}}},\hskip 18.49988ptG\_{\mathrm{warm}}:=G\_{\pi^{\mathrm{warm}}}^{\mathrm{mix}},\hskip 18.49988pt\pi\_{\mathrm{proj}}:=T(\pi^{\mathrm{warm}})=-A\_{\mathrm{warm}}^{-1}G\_{\mathrm{warm}}. |  |

Let A^t\widehat{A}\_{t} and G^tmix\widehat{G}\_{t}^{\mathrm{mix}} be the BPTT/Monte Carlo estimators constructed under πwarm\pi^{\mathrm{warm}},
and denote

|  |  |  |
| --- | --- | --- |
|  | π^agg,mix:=−A^t−1​G^tmixon ​D.\widehat{\pi}^{\mathrm{agg,mix}}:=-\widehat{A}\_{t}^{-1}\widehat{G}\_{t}^{\mathrm{mix}}\hskip 18.49988pt\text{on }D. |  |

###### Proof.

Step 0 (Fixed-point form of the deployable optimum).
Let π⋆:=π⋆,blind\pi^{\star}:=\pi^{\star,\mathrm{blind}} be a locally optimal interior deployable θ\theta-blind policy
for the fixed-qq ex–ante problem.
By the qq-aggregated stationarity (Theorem [1](https://arxiv.org/html/2601.03175v1#Thmtheorem1 "Theorem 1 (𝑞-aggregated first-order condition under latent 𝜃 (deployable 𝜃-blind stationarity)). ‣ 𝑞-aggregated Pontryagin condition for the 𝜃-blind ex–ante problem (Markov feedback). ‣ 2.2 Pontryagin optimality under latent parameters: full-information vs. aggregated conditions ‣ 2 Dynamic Portfolio Choice in Estimated Diffusion Markets with Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")), π⋆\pi^{\star} satisfies

|  |  |  |
| --- | --- | --- |
|  | Aπ⋆​(z)​π⋆​(z)=−Gπ⋆mix​(z)​for ​μ​-a.e. ​z∈D,A\_{\pi^{\star}}(z)\,\pi^{\star}(z)=-G\_{\pi^{\star}}^{\mathrm{mix}}(z)\qquad\text{for }\mu\text{-a.e.\ }z\in D, |  |

hence (under invertibility on DD) it is a fixed point of TT:

|  |  |  |
| --- | --- | --- |
|  | π⋆​(z)=T​(π⋆)​(z)=−Aπ⋆​(z)−1​Gπ⋆mix​(z),μ​-a.e. ​z∈D.\pi^{\star}(z)=T(\pi^{\star})(z)=-A\_{\pi^{\star}}(z)^{-1}G\_{\pi^{\star}}^{\mathrm{mix}}(z),\hskip 18.49988pt\mu\text{-a.e.\ }z\in D. |  |

Step 1 (Triangle decomposition).
Add and subtract πproj\pi\_{\mathrm{proj}}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖π^agg,mix−π⋆‖L2​(μ)≤‖π^agg,mix−πproj‖L2​(μ)+‖πproj−π⋆‖L2​(μ).\|\widehat{\pi}^{\mathrm{agg,mix}}-\pi^{\star}\|\_{L^{2}(\mu)}\leq\|\widehat{\pi}^{\mathrm{agg,mix}}-\pi\_{\mathrm{proj}}\|\_{L^{2}(\mu)}+\|\pi\_{\mathrm{proj}}-\pi^{\star}\|\_{L^{2}(\mu)}. |  | (101) |

Step 2 (Estimation error via Proposition [1](https://arxiv.org/html/2601.03175v1#Thmproposition1 "Proposition 1 (Stability of the projection map (𝐴,𝐺)↦-𝐴⁻¹⁢𝐺). ‣ C.1 Stability of the projection map (𝐴,𝐺)↦-𝐴⁻¹⁢𝐺 ‣ Appendix C Auxiliary results for Theorem 3 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).
Apply Proposition [1](https://arxiv.org/html/2601.03175v1#Thmproposition1 "Proposition 1 (Stability of the projection map (𝐴,𝐺)↦-𝐴⁻¹⁢𝐺). ‣ C.1 Stability of the projection map (𝐴,𝐺)↦-𝐴⁻¹⁢𝐺 ‣ Appendix C Auxiliary results for Theorem 3 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection") with

|  |  |  |
| --- | --- | --- |
|  | (A,G)=(Awarm,Gwarm),(A~,G~)=(A^t,G^tmix).(A,G)=(A\_{\mathrm{warm}},G\_{\mathrm{warm}}),\hskip 18.49988pt(\widetilde{A},\widetilde{G})=(\widehat{A}\_{t},\widehat{G}\_{t}^{\mathrm{mix}}). |  |

Assume the perturbative regime on DD:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Awarm−1‖L∞​(D)≤κ,‖Gwarm‖L∞​(D)≤MG,‖A^t−Awarm‖L∞​(D)≤(2​κ)−1,‖G^tmix‖L∞​(D)≤MG.\|A\_{\mathrm{warm}}^{-1}\|\_{L^{\infty}(D)}\leq\kappa,\qquad\|G\_{\mathrm{warm}}\|\_{L^{\infty}(D)}\leq M\_{G},\qquad\|\widehat{A}\_{t}-A\_{\mathrm{warm}}\|\_{L^{\infty}(D)}\leq(2\kappa)^{-1},\qquad\|\widehat{G}\_{t}^{\mathrm{mix}}\|\_{L^{\infty}(D)}\leq M\_{G}. |  | (102) |

Then ([97](https://arxiv.org/html/2601.03175v1#A3.E97 "Equation 97 ‣ Proposition 1 (Stability of the projection map (𝐴,𝐺)↦-𝐴⁻¹⁢𝐺). ‣ C.1 Stability of the projection map (𝐴,𝐺)↦-𝐴⁻¹⁢𝐺 ‣ Appendix C Auxiliary results for Theorem 3 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) yields

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ‖π^agg,mix−πproj‖L2​(μ)\displaystyle\|\widehat{\pi}^{\mathrm{agg,mix}}-\pi\_{\mathrm{proj}}\|\_{L^{2}(\mu)} | ≤2​κ​‖G^tmix−Gwarm‖L2​(μ)+4​κ2​MG​‖A^t−Awarm‖L2​(μ).\displaystyle\leq 2\kappa\,\|\widehat{G}\_{t}^{\mathrm{mix}}-G\_{\mathrm{warm}}\|\_{L^{2}(\mu)}+4\kappa^{2}M\_{G}\,\|\widehat{A}\_{t}-A\_{\mathrm{warm}}\|\_{L^{2}(\mu)}. |  | (103) |

By the definition of δBPTT​(Δ​t,MMC,Mθ)\delta\_{\mathrm{BPTT}}(\Delta t,M\_{\mathrm{MC}},M\_{\theta}) in Theorem [3](https://arxiv.org/html/2601.03175v1#Thmtheorem3 "Theorem 3 (Residual-based ex–ante 𝜃-blind policy-gap bound for P–PGDPO (mixed-moment, deployable, slab-wise local)). ‣ Residual diagnostic and a slab-wise small-gain policy-gap bound. ‣ 3.2 Projected PG–DPO under latent 𝜃: 𝑞-aggregated projection and a residual-based policy-gap bound ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"),

|  |  |  |
| --- | --- | --- |
|  | ‖A^t−Awarm‖L2​(μ)+‖G^tmix−Gwarm‖L2​(μ)≤δBPTT​(Δ​t,MMC,Mθ),\|\widehat{A}\_{t}-A\_{\mathrm{warm}}\|\_{L^{2}(\mu)}+\|\widehat{G}\_{t}^{\mathrm{mix}}-G\_{\mathrm{warm}}\|\_{L^{2}(\mu)}\leq\delta\_{\mathrm{BPTT}}(\Delta t,M\_{\mathrm{MC}},M\_{\theta}), |  |

hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖π^agg,mix−πproj‖L2​(μ)≤C2​δBPTT​(Δ​t,MMC,Mθ),C2:=2​κ+4​κ2​MG.\|\widehat{\pi}^{\mathrm{agg,mix}}-\pi\_{\mathrm{proj}}\|\_{L^{2}(\mu)}\leq C\_{2}\,\delta\_{\mathrm{BPTT}}(\Delta t,M\_{\mathrm{MC}},M\_{\theta}),\hskip 18.49988ptC\_{2}:=2\kappa+4\kappa^{2}M\_{G}. |  | (104) |

Step 3 (Slab-wise warm-up bias bound).
Assume πwarm,π⋆∈𝒰\pi^{\mathrm{warm}},\pi^{\star}\in\mathcal{U} and the slab-wise contraction
‖T​(π1)−T​(π2)‖k≤ρ​(τk)​‖π1−π2‖k\|T(\pi\_{1})-T(\pi\_{2})\|\_{k}\leq\rho(\tau\_{k})\|\pi\_{1}-\pi\_{2}\|\_{k} from Proposition [2](https://arxiv.org/html/2601.03175v1#Thmproposition2 "Proposition 2 (Short-time (slab) Lipschitz gain). ‣ Time-slab decomposition. ‣ C.2 Slab-wise small-gain for the 𝑞-aggregated projection inputs ‣ Appendix C Auxiliary results for Theorem 3 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection").
Let ρ∗:=maxk⁡ρ​(τk)<1\rho\_{\*}:=\max\_{k}\rho(\tau\_{k})<1.
Since πproj=T​(πwarm)\pi\_{\mathrm{proj}}=T(\pi^{\mathrm{warm}}) and π⋆=T​(π⋆)\pi^{\star}=T(\pi^{\star}),
for each slab DkD\_{k} we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖πproj−π⋆‖k=‖T​(πwarm)−T​(π⋆)‖k≤ρ​(τk)​‖πwarm−π⋆‖k≤ρ∗​‖πwarm−π⋆‖k.\|\pi\_{\mathrm{proj}}-\pi^{\star}\|\_{k}=\|T(\pi^{\mathrm{warm}})-T(\pi^{\star})\|\_{k}\leq\rho(\tau\_{k})\,\|\pi^{\mathrm{warm}}-\pi^{\star}\|\_{k}\leq\rho\_{\*}\,\|\pi^{\mathrm{warm}}-\pi^{\star}\|\_{k}. |  | (105) |

Step 4 (Residual identity and slab-wise closure).
Define the warm-up aggregated stationarity residual (mixed-moment) on DD by

|  |  |  |
| --- | --- | --- |
|  | rFOC,mixwarm​(z):=Awarm​(z)​πwarm​(z)+Gwarm​(z),εwarmmix:=‖rFOC,mixwarm‖L2​(μ).r\_{\mathrm{FOC,mix}}^{\mathrm{warm}}(z):=A\_{\mathrm{warm}}(z)\,\pi^{\mathrm{warm}}(z)+G\_{\mathrm{warm}}(z),\hskip 18.49988pt\varepsilon\_{\mathrm{warm}}^{\mathrm{mix}}:=\|r\_{\mathrm{FOC,mix}}^{\mathrm{warm}}\|\_{L^{2}(\mu)}. |  |

Also define the slab-wise residual sizes

|  |  |  |
| --- | --- | --- |
|  | εwarm,kmix:=‖rFOC,mixwarm‖k,so that ​(εwarmmix)2=∑k=1K(εwarm,kmix)2.\varepsilon\_{\mathrm{warm},k}^{\mathrm{mix}}:=\|r\_{\mathrm{FOC,mix}}^{\mathrm{warm}}\|\_{k},\hskip 18.49988pt\text{so that }\ (\varepsilon\_{\mathrm{warm}}^{\mathrm{mix}})^{2}=\sum\_{k=1}^{K}(\varepsilon\_{\mathrm{warm},k}^{\mathrm{mix}})^{2}. |  |

By construction of πproj\pi\_{\mathrm{proj}},

|  |  |  |
| --- | --- | --- |
|  | πwarm−πproj=Awarm−1​rFOC,mixwarm,\pi^{\mathrm{warm}}-\pi\_{\mathrm{proj}}=A\_{\mathrm{warm}}^{-1}r\_{\mathrm{FOC,mix}}^{\mathrm{warm}}, |  |

hence on each slab

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖πwarm−πproj‖k≤κ​εwarm,kmix.\|\pi^{\mathrm{warm}}-\pi\_{\mathrm{proj}}\|\_{k}\leq\kappa\,\varepsilon\_{\mathrm{warm},k}^{\mathrm{mix}}. |  | (106) |

Now combine the triangle inequality on each slab with ([105](https://arxiv.org/html/2601.03175v1#A3.E105 "Equation 105 ‣ Proof. ‣ Setup. ‣ C.3 Proof of Theorem 3 ‣ Appendix C Auxiliary results for Theorem 3 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")):

|  |  |  |
| --- | --- | --- |
|  | ‖πwarm−π⋆‖k≤‖πwarm−πproj‖k+‖πproj−π⋆‖k≤κ​εwarm,kmix+ρ∗​‖πwarm−π⋆‖k.\|\pi^{\mathrm{warm}}-\pi^{\star}\|\_{k}\leq\|\pi^{\mathrm{warm}}-\pi\_{\mathrm{proj}}\|\_{k}+\|\pi\_{\mathrm{proj}}-\pi^{\star}\|\_{k}\leq\kappa\,\varepsilon\_{\mathrm{warm},k}^{\mathrm{mix}}+\rho\_{\*}\,\|\pi^{\mathrm{warm}}-\pi^{\star}\|\_{k}. |  |

Since ρ∗<1\rho\_{\*}<1, we close slab-wise:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖πwarm−π⋆‖k≤κ1−ρ∗​εwarm,kmix.\|\pi^{\mathrm{warm}}-\pi^{\star}\|\_{k}\leq\frac{\kappa}{1-\rho\_{\*}}\,\varepsilon\_{\mathrm{warm},k}^{\mathrm{mix}}. |  | (107) |

Plugging into ([105](https://arxiv.org/html/2601.03175v1#A3.E105 "Equation 105 ‣ Proof. ‣ Setup. ‣ C.3 Proof of Theorem 3 ‣ Appendix C Auxiliary results for Theorem 3 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖πproj−π⋆‖k≤ρ∗​κ1−ρ∗​εwarm,kmix.\|\pi\_{\mathrm{proj}}-\pi^{\star}\|\_{k}\leq\frac{\rho\_{\*}\kappa}{1-\rho\_{\*}}\,\varepsilon\_{\mathrm{warm},k}^{\mathrm{mix}}. |  | (108) |

Summing over slabs yields the global bias bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖πproj−π⋆‖L2​(μ)≤ρ∗​κ1−ρ∗​εwarmmix.\|\pi\_{\mathrm{proj}}-\pi^{\star}\|\_{L^{2}(\mu)}\leq\frac{\rho\_{\*}\kappa}{1-\rho\_{\*}}\,\varepsilon\_{\mathrm{warm}}^{\mathrm{mix}}. |  | (109) |

Step 5 (Finish).
Combine ([101](https://arxiv.org/html/2601.03175v1#A3.E101 "Equation 101 ‣ Proof. ‣ Setup. ‣ C.3 Proof of Theorem 3 ‣ Appendix C Auxiliary results for Theorem 3 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")), ([104](https://arxiv.org/html/2601.03175v1#A3.E104 "Equation 104 ‣ Proof. ‣ Setup. ‣ C.3 Proof of Theorem 3 ‣ Appendix C Auxiliary results for Theorem 3 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")), and ([109](https://arxiv.org/html/2601.03175v1#A3.E109 "Equation 109 ‣ Proof. ‣ Setup. ‣ C.3 Proof of Theorem 3 ‣ Appendix C Auxiliary results for Theorem 3 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) to obtain

|  |  |  |
| --- | --- | --- |
|  | ‖π^agg,mix−π⋆‖L2​(μ)≤ρ∗​κ1−ρ∗​εwarmmix+C2​δBPTT​(Δ​t,MMC,Mθ),\|\widehat{\pi}^{\mathrm{agg,mix}}-\pi^{\star}\|\_{L^{2}(\mu)}\leq\frac{\rho\_{\*}\kappa}{1-\rho\_{\*}}\,\varepsilon\_{\mathrm{warm}}^{\mathrm{mix}}+C\_{2}\,\delta\_{\mathrm{BPTT}}(\Delta t,M\_{\mathrm{MC}},M\_{\theta}), |  |

which is the slab-wise version of ([71](https://arxiv.org/html/2601.03175v1#S3.E71 "Equation 71 ‣ Theorem 3 (Residual-based ex–ante 𝜃-blind policy-gap bound for P–PGDPO (mixed-moment, deployable, slab-wise local)). ‣ Residual diagnostic and a slab-wise small-gain policy-gap bound. ‣ 3.2 Projected PG–DPO under latent 𝜃: 𝑞-aggregated projection and a residual-based policy-gap bound ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) (with ρ∗\rho\_{\*} in place of a global C1C\_{1}).
∎

###### Remark 4 (Relation to prior PGDPO slab analyses).

The closure step above uses the same *slab-wise* small-gain philosophy as in huh2025breaking:
short-time parabolic smoothing yields a contraction on each time slab, and the global bound follows by concatenation.
The key difference here is that the contraction is applied to the *qq-aggregated projection map*
T​(π)=−Aπ−1​GπmixT(\pi)=-A\_{\pi}^{-1}G\_{\pi}^{\mathrm{mix}}, hence the additional use of the algebraic projection stability
(Proposition [1](https://arxiv.org/html/2601.03175v1#Thmproposition1 "Proposition 1 (Stability of the projection map (𝐴,𝐺)↦-𝐴⁻¹⁢𝐺). ‣ C.1 Stability of the projection map (𝐴,𝐺)↦-𝐴⁻¹⁢𝐺 ‣ Appendix C Auxiliary results for Theorem 3 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) for the estimator π^agg,mix\widehat{\pi}^{\mathrm{agg,mix}}.

## Appendix D Implementation details for Section [3](https://arxiv.org/html/2601.03175v1#S3 "3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")

This appendix provides reproducible step-by-step templates for the methods in
Section [3](https://arxiv.org/html/2601.03175v1#S3 "3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"). The high-level pipeline is summarized in
Figure LABEL:fig:sec3-pipeline-sideways. For compactness we present one template per
subsection of Section [3](https://arxiv.org/html/2601.03175v1#S3 "3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection").

### D.1 Stage 1 (PG–DPO) template for Section [3.1](https://arxiv.org/html/2601.03175v1#S3.SS1 "3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")

Stage 1 performs stochastic gradient ascent on the fixed-qq ex–ante objective
([56](https://arxiv.org/html/2601.03175v1#S3.E56 "Equation 56 ‣ Setup and objectives (frozen 𝜃, deployable 𝜃-blind feedback). ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")), with latent θ∼q\theta\sim q sampled inside the simulator
while the policy remains θ\theta-blind.

##### Inputs.

Policy parameters φ\varphi; sampler ν\nu over initial states;
prior qq; time grid (N,Δ​t)(N,\Delta t); batch size MM; optimizer and step size α\alpha.

##### Template (one training iteration).

1. 1.

   Sample initial states.
   Draw a mini-batch {z0(i)=(t0(i),x0(i),y0(i))}i=1M∼ν\{z\_{0}^{(i)}=(t\_{0}^{(i)},x\_{0}^{(i)},y\_{0}^{(i)})\}\_{i=1}^{M}\sim\nu.
2. 2.

   Sample latent environment parameter.
   Sample θ∼q\theta\sim q *inside the simulator* (unseen by πφ\pi\_{\varphi}).
   (Variant: sample θ(i)∼q\theta^{(i)}\sim q independently per episode; both are unbiased for ∇φJ​(φ)\nabla\_{\varphi}J(\varphi).)
3. 3.

   Simulate Euler rollouts.
   For each episode ii, simulate the Euler scheme in
   ([53](https://arxiv.org/html/2601.03175v1#S3.E53 "Equation 53 ‣ Setup and objectives (frozen 𝜃, deployable 𝜃-blind feedback). ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"))–([54](https://arxiv.org/html/2601.03175v1#S3.E54 "Equation 54 ‣ Setup and objectives (frozen 𝜃, deployable 𝜃-blind feedback). ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) under the θ\theta-blind policy
   πφ\pi\_{\varphi} and collect terminal utilities {U​(XT(i))}i=1M\{U(X\_{T}^{(i)})\}\_{i=1}^{M}.
4. 4.

   Backpropagation through time (BPTT).
   Compute the Monte Carlo gradient estimator

   |  |  |  |
   | --- | --- | --- |
   |  | g^←1M​∑i=1M∇φU​(XT(i)).\widehat{g}\;\leftarrow\;\frac{1}{M}\sum\_{i=1}^{M}\nabla\_{\varphi}U(X\_{T}^{(i)}). |  |
5. 5.

   Parameter update.
   Update φ←φ+α⋅OptimizerStep​(g^)\varphi\leftarrow\varphi+\alpha\cdot\texttt{OptimizerStep}(\widehat{g}),
   consistent with ([58](https://arxiv.org/html/2601.03175v1#S3.E58 "Equation 58 ‣ Discretization, sampling over 𝜃, and baseline PG–DPO update. ‣ 3.1 PG–DPO as stochastic gradient ascent and BPTT–PMP correspondence ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).
6. 6.

   Checkpoint.
   Periodically save a warm-up checkpoint φwarm\varphi^{\mathrm{warm}} for stage 2 projection.

### D.2 Stage 2 (P–PGDPO projection; mixed-moment qq-aggregation) template for Section [3.2](https://arxiv.org/html/2601.03175v1#S3.SS2 "3.2 Projected PG–DPO under latent 𝜃: 𝑞-aggregated projection and a residual-based policy-gap bound ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")

Stage 2 is a post-processing map: given a warm-up θ\theta-blind policy πφwarm\pi\_{\varphi^{\mathrm{warm}}},
it estimates Pontryagin sensitivity objects by Monte Carlo and constructs a *deployable* projected
control on a working-domain sample z∼μz\sim\mu.

The aggregation used here matches the mixed-moment qq-aggregation in
([65](https://arxiv.org/html/2601.03175v1#S3.E65 "Equation 65 ‣ Mixed-moment 𝑞-aggregation under a warm-up policy. ‣ 3.2 Projected PG–DPO under latent 𝜃: 𝑞-aggregated projection and a residual-based policy-gap bound ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"))–([66](https://arxiv.org/html/2601.03175v1#S3.E66 "Equation 66 ‣ Mixed-moment 𝑞-aggregation under a warm-up policy. ‣ 3.2 Projected PG–DPO under latent 𝜃: 𝑞-aggregated projection and a residual-based policy-gap bound ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")), yielding the projected control ([67](https://arxiv.org/html/2601.03175v1#S3.E67 "Equation 67 ‣ Mixed-moment 𝑞-aggregation under a warm-up policy. ‣ 3.2 Projected PG–DPO under latent 𝜃: 𝑞-aggregated projection and a residual-based policy-gap bound ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).

##### Inputs.

Warm-up policy πφwarm\pi\_{\varphi^{\mathrm{warm}}}; working-domain sampler μ\mu on DD;
budgets (Mz,Mθ,MMC)(M\_{z},M\_{\theta},M\_{\mathrm{MC}}).

##### Template (constructing projection targets on a batch of query states).

1. 1.

   Sample working-domain query states.
   Draw {zj=(tj,xj,yj)}j=1Mz∼μ\{z\_{j}=(t\_{j},x\_{j},y\_{j})\}\_{j=1}^{M\_{z}}\sim\mu.
2. 2.

   For each query state zjz\_{j}, sample latent parameters.
   Sample {θℓ}ℓ=1Mθ∼q\{\theta\_{\ell}\}\_{\ell=1}^{M\_{\theta}}\sim q.
3. 3.

   For each frozen θℓ\theta\_{\ell}, estimate costates at zjz\_{j}.
   For each ℓ=1,…,Mθ\ell=1,\dots,M\_{\theta}:

   1. (a)

      Simulate MMCM\_{\mathrm{MC}} trajectories from zjz\_{j} under πφwarm\pi\_{\varphi^{\mathrm{warm}}} with frozen θℓ\theta\_{\ell}.
   2. (b)

      Compute pathwise sensitivities by autodiff/BPTT and average as in ([62](https://arxiv.org/html/2601.03175v1#S3.E62 "Equation 62 ‣ Mixed-moment 𝑞-aggregation under a warm-up policy. ‣ 3.2 Projected PG–DPO under latent 𝜃: 𝑞-aggregated projection and a residual-based policy-gap bound ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) to obtain
      p^tθℓ​(zj)\widehat{p}\_{t}^{\theta\_{\ell}}(z\_{j}), p^x,tθℓ​(zj)\widehat{p}\_{x,t}^{\theta\_{\ell}}(z\_{j}), p^y,tθℓ​(zj)\widehat{p}\_{y,t}^{\theta\_{\ell}}(z\_{j}).
   3. (c)

      Form the θ\theta-conditional inputs (cf. ([63](https://arxiv.org/html/2601.03175v1#S3.E63 "Equation 63 ‣ Mixed-moment 𝑞-aggregation under a warm-up policy. ‣ 3.2 Projected PG–DPO under latent 𝜃: 𝑞-aggregated projection and a residual-based policy-gap bound ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"))–([64](https://arxiv.org/html/2601.03175v1#S3.E64 "Equation 64 ‣ Mixed-moment 𝑞-aggregation under a warm-up policy. ‣ 3.2 Projected PG–DPO under latent 𝜃: 𝑞-aggregated projection and a residual-based policy-gap bound ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"))):

      |  |  |  |
      | --- | --- | --- |
      |  | A^tθℓ​(zj)←xj​p^x,tθℓ​(zj)​Σ​(yj,θℓ),G^tθℓ​(zj)←p^tθℓ​(zj)​b​(yj,θℓ)+ΣS​Y​(yj,θℓ)​p^y,tθℓ​(zj).\widehat{A}\_{t}^{\theta\_{\ell}}(z\_{j})\leftarrow x\_{j}\,\widehat{p}\_{x,t}^{\theta\_{\ell}}(z\_{j})\,\Sigma(y\_{j},\theta\_{\ell}),\hskip 18.49988pt\widehat{G}\_{t}^{\theta\_{\ell}}(z\_{j})\leftarrow\widehat{p}\_{t}^{\theta\_{\ell}}(z\_{j})\,b(y\_{j},\theta\_{\ell})+\Sigma\_{SY}(y\_{j},\theta\_{\ell})\,\widehat{p}\_{y,t}^{\theta\_{\ell}}(z\_{j}). |  |
4. 4.

   Aggregate across θ∼q\theta\sim q (mixed-moment).
   Compute

   |  |  |  |
   | --- | --- | --- |
   |  | A^t​(zj)←1Mθ​∑ℓ=1MθA^tθℓ​(zj),G^tmix​(zj)←1Mθ​∑ℓ=1MθG^tθℓ​(zj),\widehat{A}\_{t}(z\_{j})\;\leftarrow\;\frac{1}{M\_{\theta}}\sum\_{\ell=1}^{M\_{\theta}}\widehat{A}\_{t}^{\theta\_{\ell}}(z\_{j}),\hskip 18.49988pt\widehat{G}\_{t}^{\mathrm{mix}}(z\_{j})\;\leftarrow\;\frac{1}{M\_{\theta}}\sum\_{\ell=1}^{M\_{\theta}}\widehat{G}\_{t}^{\theta\_{\ell}}(z\_{j}), |  |

   consistent with ([65](https://arxiv.org/html/2601.03175v1#S3.E65 "Equation 65 ‣ Mixed-moment 𝑞-aggregation under a warm-up policy. ‣ 3.2 Projected PG–DPO under latent 𝜃: 𝑞-aggregated projection and a residual-based policy-gap bound ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"))–([66](https://arxiv.org/html/2601.03175v1#S3.E66 "Equation 66 ‣ Mixed-moment 𝑞-aggregation under a warm-up policy. ‣ 3.2 Projected PG–DPO under latent 𝜃: 𝑞-aggregated projection and a residual-based policy-gap bound ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).
5. 5.

   Solve the projection (mixed-moment aggregation).
   Whenever A^t​(zj)\widehat{A}\_{t}(z\_{j}) is invertible and the solve is numerically stable,
   compute the deployable projected control

   |  |  |  |
   | --- | --- | --- |
   |  | π^agg,mix​(zj)←−(A^t​(zj))−1​G^tmix​(zj),\widehat{\pi}^{\mathrm{agg,mix}}(z\_{j})\;\leftarrow\;-\big(\widehat{A}\_{t}(z\_{j})\big)^{-1}\widehat{G}\_{t}^{\mathrm{mix}}(z\_{j}), |  |

   which matches ([67](https://arxiv.org/html/2601.03175v1#S3.E67 "Equation 67 ‣ Mixed-moment 𝑞-aggregation under a warm-up policy. ‣ 3.2 Projected PG–DPO under latent 𝜃: 𝑞-aggregated projection and a residual-based policy-gap bound ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).

### D.3 Coupling I: residual/control-variate projection (Section [3.3.1](https://arxiv.org/html/2601.03175v1#S3.SS3.SSS1 "3.3.1 Control-variate (residual) form of the projected rule ‣ 3.3 Coupling stage 1 and stage 2: residual projection and interactive distillation ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"))

This subsection records a variance-reduced implementation of the stage 2 map using the residual identity
([74](https://arxiv.org/html/2601.03175v1#S3.E74 "Equation 74 ‣ 3.3.1 Control-variate (residual) form of the projected rule ‣ 3.3 Coupling stage 1 and stage 2: residual projection and interactive distillation ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")). The residual form is applied around the warm-up policy
and uses the mixed-moment aggregated inputs (A^t,G^tmix)(\widehat{A}\_{t},\widehat{G}\_{t}^{\mathrm{mix}}).

##### Inputs.

Warm-up policy πφwarm\pi\_{\varphi^{\mathrm{warm}}}; query state(s) z=(t,x,y)∼μz=(t,x,y)\sim\mu; and
stage 2 projection ingredients (A^t​(z),G^tmix​(z))(\widehat{A}\_{t}(z),\widehat{G}\_{t}^{\mathrm{mix}}(z)) constructed as in
Section [D.2](https://arxiv.org/html/2601.03175v1#A4.SS2 "D.2 Stage 2 (P–PGDPO projection; mixed-moment 𝑞-aggregation) template for Section 3.2 ‣ Appendix D Implementation details for Section 3 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection").

##### Template (statewise residual projection; mixed-moment aggregation).

1. 1.

   Evaluate warm-up control.
   Compute πφwarm​(z)\pi\_{\varphi^{\mathrm{warm}}}(z).
2. 2.

   Form the aggregated residual.
   Compute

   |  |  |  |
   | --- | --- | --- |
   |  | r^FOC​(z)←A^t​(z)​πφwarm​(z)+G^tmix​(z).\widehat{r}\_{\mathrm{FOC}}(z)\;\leftarrow\;\widehat{A}\_{t}(z)\,\pi\_{\varphi^{\mathrm{warm}}}(z)+\widehat{G}\_{t}^{\mathrm{mix}}(z). |  |
3. 3.

   Apply the residual correction.
   Compute

   |  |  |  |
   | --- | --- | --- |
   |  | π^agg,mix​(z)←πφwarm​(z)−(A^t​(z))−1​r^FOC​(z).\widehat{\pi}^{\mathrm{agg,mix}}(z)\;\leftarrow\;\pi\_{\varphi^{\mathrm{warm}}}(z)-\big(\widehat{A}\_{t}(z)\big)^{-1}\widehat{r}\_{\mathrm{FOC}}(z). |  |

### D.4 Coupling II: interactive distillation (Section [3.3.2](https://arxiv.org/html/2601.03175v1#S3.SS3.SSS2 "3.3.2 Interactive distillation: projection-guided training and amortized deployment ‣ 3.3 Coupling stage 1 and stage 2: residual projection and interactive distillation ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"))

This subsection records an implementation template for interactive distillation: the projected output
from stage 2 is used as a teacher signal during stage 1 training via the mixed objective
([76](https://arxiv.org/html/2601.03175v1#S3.E76 "Equation 76 ‣ 3.3.2 Interactive distillation: projection-guided training and amortized deployment ‣ 3.3 Coupling stage 1 and stage 2: residual projection and interactive distillation ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")). The teacher is built from the mixed-moment projected rule
(possibly evaluated in residual form for variance reduction).

##### Inputs.

Student parameters φ\varphi; teacher refresh interval KK; distillation schedule λ​(n)\lambda(n);
working-domain sampler μ\mu.

##### Template (training loop with intermittent teacher refresh).

1. 1.

   Initialize.
   Set φ−←φ\varphi^{-}\leftarrow\varphi and initialize an empty teacher buffer ℬ←∅\mathcal{B}\leftarrow\emptyset.
2. 2.

   Repeat for iterations n=1,2,…n=1,2,\dots:

   1. (a)

      Stage 1 update (PG–DPO step).
      Perform one PG–DPO update step on J​(φ)J(\varphi) as in Section [D.1](https://arxiv.org/html/2601.03175v1#A4.SS1 "D.1 Stage 1 (PG–DPO) template for Section 3.1 ‣ Appendix D Implementation details for Section 3 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection").
   2. (b)

      Teacher refresh (every KK steps).
      If nmodK=0n\bmod K=0:

      1. i.

         Set φ−←φ\varphi^{-}\leftarrow\varphi (lagged copy).
      2. ii.

         Sample working-domain states {zj}j=1Mz∼μ\{z\_{j}\}\_{j=1}^{M\_{z}}\sim\mu.
      3. iii.

         For each zjz\_{j}, run stage 2 under πφ−\pi\_{\varphi^{-}} (mixed-moment aggregation) to compute a projected teacher
         π^φ−agg,mix​(zj)\widehat{\pi}^{\mathrm{agg,mix}}\_{\varphi^{-}}(z\_{j}).
         (In practice we compute it in residual form around πφ−\pi\_{\varphi^{-}} as in ([75](https://arxiv.org/html/2601.03175v1#S3.E75 "Equation 75 ‣ 3.3.2 Interactive distillation: projection-guided training and amortized deployment ‣ 3.3 Coupling stage 1 and stage 2: residual projection and interactive distillation ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).)
      4. iv.

         Optionally filter states using diagnostics (Section [D.5](https://arxiv.org/html/2601.03175v1#A4.SS5 "D.5 Engineering notes and stabilizers ‣ Appendix D Implementation details for Section 3 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) and update the buffer:

         |  |  |  |
         | --- | --- | --- |
         |  | ℬ←{(zj,π^φ−agg,mix​(zj))}j=1Mz​(after filtering).\mathcal{B}\ \leftarrow\ \{(z\_{j},\widehat{\pi}^{\mathrm{agg,mix}}\_{\varphi^{-}}(z\_{j}))\}\_{j=1}^{M\_{z}}\ \ \text{(after filtering)}. |  |
   3. (c)

      Distillation step (when enabled).
      If λ​(n)>0\lambda(n)>0 and ℬ≠∅\mathcal{B}\neq\emptyset:

      1. i.

         Sample (z,πteach)(z,\pi^{\mathrm{teach}}) from ℬ\mathcal{B}.
      2. ii.

         Apply a gradient step to minimize the proximity term
         ‖πφ​(z)−stopgrad​(πteach)‖2\|\pi\_{\varphi}(z)-\mathrm{stopgrad}(\pi^{\mathrm{teach}})\|^{2}
         with coefficient λ​(n)\lambda(n), consistent with ([76](https://arxiv.org/html/2601.03175v1#S3.E76 "Equation 76 ‣ 3.3.2 Interactive distillation: projection-guided training and amortized deployment ‣ 3.3 Coupling stage 1 and stage 2: residual projection and interactive distillation ‣ 3 Pontryagin–Guided Policy Optimization under Latent Parameter Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")).

### D.5 Engineering notes and stabilizers

This subsection collects practical stabilizers that we found helpful for reliable training and projection in high dimensions.

* •

  Antithetic sampling for θ\theta.
  When qq is symmetric (e.g. Gaussian in a latent normal parameterization), sample θ\theta in antithetic pairs by drawing
  z∼𝒩​(0,I)z\sim\mathcal{N}(0,I) and using (z,−z)(z,-z) to construct (θ+,θ−)(\theta^{+},\theta^{-}). This reduces the variance of qq-averaged quantities
  and typically improves the stability of stage 2 diagnostics on the working domain.
* •

  Blockwise Monte Carlo and robust aggregation.
  To control rare-tail domination, split Monte Carlo replications into BB blocks and compute blockwise averages of costate-driven
  ingredients (e.g. A^tθ​(z)\widehat{A}\_{t}^{\theta}(z) and G^tθ​(z)\widehat{G}\_{t}^{\theta}(z)). Aggregate across blocks using a robust statistic
  such as the median or median-of-means, which makes the projection less sensitive to outlier trajectories.
* •

  Curvature/denominator stability checks.
  Because the projection map (A,G)↦−A−1​G(A,G)\mapsto-A^{-1}G can be sensitive to near-singularity of AA, monitor the conditioning of
  A^t\widehat{A}\_{t} (or failure rates of the linear solve). When diagnostics indicate ill-conditioning, skip projection-guided updates at that
  state or increase Monte Carlo budgets locally.
* •

  Residual magnitude as a reliability diagnostic.
  For the residual form, compute r^FOC​(z)=A^t​(z)​πφwarm​(z)+G^tmix​(z)\widehat{r}\_{\mathrm{FOC}}(z)=\widehat{A}\_{t}(z)\pi\_{\varphi^{\mathrm{warm}}}(z)+\widehat{G}\_{t}^{\mathrm{mix}}(z).
  Small ‖r^FOC​(z)‖\|\widehat{r}\_{\mathrm{FOC}}(z)\| indicates approximate satisfaction of the mixed-moment aggregated first-order condition at zz and
  empirically correlates with more reliable teacher targets.
* •

  Diagnostics-based teacher selection on the working domain.
  Rather than applying distillation on all sampled {zj}∼μ\{z\_{j}\}\sim\mu, keep only states that pass a reliability predicate.
  In practice, filter using residual-magnitude thresholds together with stable linear-solve diagnostics to prevent a small subset
  of pathological states from contaminating the teacher buffer.
* •

  λ\lambda schedule and safeguards.
  Use a warm-up period with λ=0\lambda=0 (pure PG–DPO) and increase λ\lambda only after stage 2 diagnostics on the working domain are stable.
  To prevent the teacher term from dominating the ex–ante objective, cap the effective coefficient via

  |  |  |  |
  | --- | --- | --- |
  |  | λeff:=min⁡{λ,c​|Lmain|Ldistill+ε},\lambda\_{\mathrm{eff}}:=\min\Big\{\lambda,\;c\,\frac{|L\_{\mathrm{main}}|}{L\_{\mathrm{distill}}+\varepsilon}\Big\}, |  |

  with c∈(0,1)c\in(0,1) and ε>0\varepsilon>0.
* •

  Initialization and scale control in high dimensions.
  To avoid early-time numerical blow-ups (often through quadratic variation terms of the form π⊤​Σ​π\pi^{\top}\Sigma\pi), initialize the policy
  output near zero and/or scale the output by d−1/2d^{-1/2}. As a last-resort safety net, a mild log-wealth clamp can prevent overflow, but it
  should be used conservatively and monitored, since frequent clamping may distort higher-order sensitivities.

## Appendix E Stage 2 projection diagnostics

We report Stage 2 diagnostic statistics as a visual supplement to
Section [4.2](https://arxiv.org/html/2601.03175v1#S4.SS2 "4.2 High-dimensional CRRA benchmark: projection and amortization ‣ 4 Breaking the Dimensional Barrier under Drift Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"). Each figure summarizes the same
tail-median protocol and layout; see captions for definitions and interpretation.

![Refer to caption](x4.png)


Figure 3: Stage 2 stationarity residual (q50). All panels report tail medians over epochs 9500–10000 (final six evaluation snapshots).
Layout matches Figure [1](https://arxiv.org/html/2601.03175v1#S4.F1 "Figure 1 ‣ 4.2 High-dimensional CRRA benchmark: projection and amortization ‣ 4 Breaking the Dimensional Barrier under Drift Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"): rows correspond to s∈{10−3,10−2,10−1}s\in\{10^{-3},10^{-2},10^{-1}\} and
columns correspond to aligned vs. misaligned uncertainty. Solid vs. dashed lines are MC base (100⋅d100\cdot d)
vs. high (400⋅d400\cdot d). We plot the median (q50) of the estimated Hamiltonian first-order condition residual norm at the query states.
Larger residual indicates the warm policy is farther from stationarity, implying a larger correction is required in
the residual-form projection. Growth of this residual with dd (especially under misalignment) supports the mechanism
that projection becomes more sensitive in high dimension due to larger correction magnitudes and amplified mixed-moment noise.

![Refer to caption](x5.png)


Figure 4: Stage 2 denominator magnitude (q50). All panels report tail medians over epochs 9500–10000 (final six evaluation snapshots).
Layout matches Figure [1](https://arxiv.org/html/2601.03175v1#S4.F1 "Figure 1 ‣ 4.2 High-dimensional CRRA benchmark: projection and amortization ‣ 4 Breaking the Dimensional Barrier under Drift Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"): rows correspond to s∈{10−3,10−2,10−1}s\in\{10^{-3},10^{-2},10^{-1}\} and
columns correspond to aligned vs. misaligned uncertainty. Solid vs. dashed lines are MC base (100⋅d100\cdot d)
vs. high (400⋅d400\cdot d). We plot a typical (q50) magnitude of the projection denominator/curvature term used in the residual-form update.
Values bounded away from zero indicate that projection is not operating in a near-singular regime at typical quantiles.
This helps rule out “catastrophic inversion” as the primary driver of degradation; instead, residual growth and
curvature mismatch (Fig. [5](https://arxiv.org/html/2601.03175v1#A5.F5 "Figure 5 ‣ Appendix E Stage 2 projection diagnostics ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")) provide a more consistent explanation in misaligned/high-dd regimes.

![Refer to caption](x6.png)


Figure 5: Stage 2 curvature-consistency statistic κ\kappa. All panels report tail medians over epochs 9500–10000 (final six evaluation snapshots).
Layout matches Figure [1](https://arxiv.org/html/2601.03175v1#S4.F1 "Figure 1 ‣ 4.2 High-dimensional CRRA benchmark: projection and amortization ‣ 4 Breaking the Dimensional Barrier under Drift Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"): rows correspond to s∈{10−3,10−2,10−1}s\in\{10^{-3},10^{-2},10^{-1}\} and
columns correspond to aligned vs. misaligned uncertainty. Solid vs. dashed lines are MC base (100⋅d100\cdot d)
vs. high (400⋅d400\cdot d). We report the stabilized median-after-floor statistic κ\kappa and compare it to the nominal reference 1/γ1/\gamma
(horizontal dotted line). For CRRA, costate ratios imply a characteristic curvature scale; sustained deviations of
κ\kappa from 1/γ1/\gamma indicate costate inconsistency and/or bias in mixed-moment estimation, and are most visible
in the hardest misaligned/high-uncertainty regime.

![Refer to caption](x7.png)


Figure 6: Stage 2 bad-sign fraction. All panels report tail medians over epochs 9500–10000 (final six evaluation snapshots).
Layout matches Figure [1](https://arxiv.org/html/2601.03175v1#S4.F1 "Figure 1 ‣ 4.2 High-dimensional CRRA benchmark: projection and amortization ‣ 4 Breaking the Dimensional Barrier under Drift Uncertainty ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection"): rows correspond to s∈{10−3,10−2,10−1}s\in\{10^{-3},10^{-2},10^{-1}\} and
columns correspond to aligned vs. misaligned uncertainty. Solid vs. dashed lines are MC base (100⋅d100\cdot d)
vs. high (400⋅d400\cdot d). We plot the fraction of samples in which the estimated curvature/denominator violates the expected sign condition
(loss of local concavity on the sampled batch). Near-zero bad-sign fractions across most regimes suggest that the
projection typically operates in a locally well-behaved region and that failures are not dominated by sign flips,
supporting the main-text conclusion that misalignment primarily increases residual/costate mismatch rather than inducing
widespread concavity violations.

## Appendix F Supplementary decomposition diagnostics for Section [5](https://arxiv.org/html/2601.03175v1#S5 "5 Recovering Intertemporal Hedging Demand in Factor-Driven Markets ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")

Tables [2](https://arxiv.org/html/2601.03175v1#A6.T2 "Table 2 ‣ Appendix F Supplementary decomposition diagnostics for Section 5 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection")–[3](https://arxiv.org/html/2601.03175v1#A6.T3 "Table 3 ‣ Appendix F Supplementary decomposition diagnostics for Section 5 ‣ Breaking the Dimensional Barrier: Dynamic Portfolio Choice with Parameter Uncertainty via Pontryagin Projection") report Stage 2 decomposition diagnostics at t=0t=0.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| s0s\_{0} | Method | d=5d=5 | 1010 | 5050 | 100100 |
| Aligned P0P\_{0} | | | | | |
| 10−310^{-3} | Stage 1+Stage 2 (Basic) | 7.17×10−067.17\text{\times}{10}^{-06} | 1.51×10−051.51\text{\times}{10}^{-05} | 1.60×10−051.60\text{\times}{10}^{-05} | 1.23×10−051.23\text{\times}{10}^{-05} |
| Stage 1+Stage 2 (Distill.) | 5.20×10−065.20\text{\times}{10}^{-06} | 9.81×10−069.81\text{\times}{10}^{-06} | 1.64×10−051.64\text{\times}{10}^{-05} | 1.62×10−051.62\text{\times}{10}^{-05} |
| 10−210^{-2} | Stage 1+Stage 2 (Basic) | 6.21×10−066.21\text{\times}{10}^{-06} | 1.38×10−051.38\text{\times}{10}^{-05} | 1.63×10−051.63\text{\times}{10}^{-05} | 1.42×10−051.42\text{\times}{10}^{-05} |
| Stage 1+Stage 2 (Distill.) | 7.13×10−067.13\text{\times}{10}^{-06} | 7.13×10−067.13\text{\times}{10}^{-06} | 1.62×10−051.62\text{\times}{10}^{-05} | 1.76×10−051.76\text{\times}{10}^{-05} |
| 10−110^{-1} | Stage 1+Stage 2 (Basic) | 8.18×10−068.18\text{\times}{10}^{-06} | 1.41×10−051.41\text{\times}{10}^{-05} | 3.82×10−053.82\text{\times}{10}^{-05} | 2.42×10−052.42\text{\times}{10}^{-05} |
| Stage 1+Stage 2 (Distill.) | 6.72×10−066.72\text{\times}{10}^{-06} | 9.21×10−069.21\text{\times}{10}^{-06} | 3.67×10−053.67\text{\times}{10}^{-05} | 3.16×10−053.16\text{\times}{10}^{-05} |
| Misaligned P0P\_{0} | | | | | |
| 10−310^{-3} | Stage 1+Stage 2 (Basic) | 1.10×10−051.10\text{\times}{10}^{-05} | 1.41×10−051.41\text{\times}{10}^{-05} | 1.70×10−051.70\text{\times}{10}^{-05} | 1.18×10−051.18\text{\times}{10}^{-05} |
| Stage 1+Stage 2 (Distill.) | 7.71×10−067.71\text{\times}{10}^{-06} | 5.94×10−065.94\text{\times}{10}^{-06} | 1.84×10−051.84\text{\times}{10}^{-05} | 1.62×10−051.62\text{\times}{10}^{-05} |
| 10−210^{-2} | Stage 1+Stage 2 (Basic) | 7.90×10−067.90\text{\times}{10}^{-06} | 2.02×10−052.02\text{\times}{10}^{-05} | 1.46×10−051.46\text{\times}{10}^{-05} | 1.20×10−051.20\text{\times}{10}^{-05} |
| Stage 1+Stage 2 (Distill.) | 6.00×10−066.00\text{\times}{10}^{-06} | 1.71×10−051.71\text{\times}{10}^{-05} | 2.21×10−052.21\text{\times}{10}^{-05} | 1.43×10−051.43\text{\times}{10}^{-05} |
| 10−110^{-1} | Stage 1+Stage 2 (Basic) | 1.24×10−051.24\text{\times}{10}^{-05} | 1.93×10−041.93\text{\times}{10}^{-04} | 5.77×10−055.77\text{\times}{10}^{-05} | 3.14×10−053.14\text{\times}{10}^{-05} |
| Stage 1+Stage 2 (Distill.) | 1.20×10−051.20\text{\times}{10}^{-05} | 1.90×10−041.90\text{\times}{10}^{-04} | 7.40×10−057.40\text{\times}{10}^{-05} | 2.47×10−052.47\text{\times}{10}^{-05} |

Table 2: Myopic-component RMSE at t=0t=0 (tail medians).



|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| s0s\_{0} | Method | d=5d=5 | 1010 | 5050 | 100100 |
| Aligned P0P\_{0} | | | | | |
| 10−310^{-3} | Stage 1+Stage 2 (Basic) | 0.9940.994 | 0.9880.988 | 0.9910.991 | 0.9900.990 |
| Stage 1+Stage 2 (Distill.) | 0.9950.995 | 0.9860.986 | 0.9900.990 | 0.9870.987 |
| 10−210^{-2} | Stage 1+Stage 2 (Basic) | 0.9930.993 | 0.9890.989 | 0.9920.992 | 0.9880.988 |
| Stage 1+Stage 2 (Distill.) | 0.9920.992 | 0.9940.994 | 0.9900.990 | 0.9870.987 |
| 10−110^{-1} | Stage 1+Stage 2 (Basic) | 0.9880.988 | 0.9900.990 | 0.9360.936 | 0.9320.932 |
| Stage 1+Stage 2 (Distill.) | 0.9960.996 | 0.9900.990 | 0.9490.949 | 0.9220.922 |
| Misaligned P0P\_{0} | | | | | |
| 10−310^{-3} | Stage 1+Stage 2 (Basic) | 0.9880.988 | 0.9880.988 | 0.9930.993 | 0.9900.990 |
| Stage 1+Stage 2 (Distill.) | 0.9940.994 | 0.9950.995 | 0.9900.990 | 0.9870.987 |
| 10−210^{-2} | Stage 1+Stage 2 (Basic) | 0.9940.994 | 0.9760.976 | 0.9920.992 | 0.9880.988 |
| Stage 1+Stage 2 (Distill.) | 0.9940.994 | 0.9800.980 | 0.9880.988 | 0.9890.989 |
| 10−110^{-1} | Stage 1+Stage 2 (Basic) | 0.9900.990 | 0.0050.005 | 0.6680.668 | 0.8510.851 |
| Stage 1+Stage 2 (Distill.) | 0.9920.992 | −0.009-0.009 | 0.6420.642 | 0.8710.871 |

Table 3: Hedging-direction cosine similarity at t=0t=0 (tail medians). Higher is better; negative indicates direction reversal.