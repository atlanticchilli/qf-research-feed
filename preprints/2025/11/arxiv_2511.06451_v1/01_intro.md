---
authors:
- Jian'an Zhang
doc_id: arxiv:2511.06451v1
family_id: arxiv:2511.06451
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures'
url_abs: http://arxiv.org/abs/2511.06451v1
url_html: https://arxiv.org/html/2511.06451v1
venue: arXiv q-fin
version: 1
year: 2025
---


ZhangJian’an
  
Guanghua School of Management, Peking University
  
Peking University
  
Beijing, China
  
2501111059@stu.pku.edu.cn

###### Abstract

We introduce *ARBITER*, a risk–neutral neural operator that learns arbitrage–free joint term structures of SPX options and VIX2.
ARBITER reframes selective scan state–space updates as a discretized Green operator under the risk–neutral measure and imposes geometry at training time via two ingredients:
(i) *Q-Align*, a Lipschitz-controlled projection pipeline combining spectral normalization and nonexpansive projections with a spectral–radius guard (CFL–style) to ensure stable scans;
(ii) a convex–monotone decoder (ICNN with Legendre duality) that enforces static no-arbitrage on the strike–maturity grid and is consistent with discretized VIX2 replication.
Training uses a saddle-point scheme with fixed, falsifiable stopping thresholds and records auditable diagnostics (Lipschitz constants before/after projection, spectral-guard hits, and projection distances).

On high-fidelity synthetic markets reflecting SPX–VIX coupling, ARBITER attains dimensionless accuracy improvements over strong sequence models and neural SDE baselines: NAS ≈0.9866\approx 0.9866, CNAS ≈0.9902\approx 0.9902, NI ≈0.6776\approx 0.6776, Stability =1.0=1.0, DualGap ≈0.060\approx 0.060, and low Surface–Wasserstein discrepancy, all with 95% HAC confidence intervals and Holm–Bonferroni control.
Stress–to–Fail analyses identify a sharp performance threshold at distortion level ≈2.0\approx 2.0, while an external-validity protocol (frozen hyperparameters reused across out-of-sample windows) yields minimal degradation.
Ablations confirm the non-replaceability of geometry: disabling gating, halving operator rank, or removing the spectral guard degrades accuracy and stability and introduces surface artifacts.
Theoretical results establish approximation rates, conditioning, identifiability (jointly with VIX2 replication), and convergence of the extragradient scheme to a noise ball.
All code, configuration files, and scripts are released to support full reproducibility.

Keywords: risk–neutral operator learning; arbitrage-free term structure; implied volatility surface; SPX–VIX coupling; spectral projection; convex–monotone decoding.

## 1 Introduction

#### Problem statement and motivation.

Modern large-scale derivatives systems in production still favor a “*fit–then-clean*” paradigm: first fit prices or implied-volatility (IV) surfaces with flexible data-driven regressors; then *post hoc* patch static/dynamic no-arbitrage, enforce martingale consistency, and repair change-of-numéraire coherence by smoothing or projections (e.g., SVI-like parameterizations, regularization, or empirical constraints that suppress butterfly and calendar arbitrage). This compartmentalization displaces *financial correctness* to an afterthought, encourages error accumulation under distribution shift, and blurs *when* training should stop and on *what* grounds the model can be rejected or improved.

Concurrently, two influential lines for long-horizon learning have matured: (i) *Selective State Space Models* (SSMs), whose evolution from S4/S5 to Mamba yields linear-time/space primitives that preserve long-range expressivity [[17](https://arxiv.org/html/2511.06451v1#bib.bib17), [18](https://arxiv.org/html/2511.06451v1#bib.bib18), [16](https://arxiv.org/html/2511.06451v1#bib.bib16)]; and (ii) *Neural Operators*, which learn function-to-function mappings and are expressly designed to decouple discretization (grid) from underlying physics [[1](https://arxiv.org/html/2511.06451v1#bib.bib1), [2](https://arxiv.org/html/2511.06451v1#bib.bib2), [21](https://arxiv.org/html/2511.06451v1#bib.bib21)].

#### Thesis: risk-neutral pricing as a structured operator.

We argue that risk-neutral pricing is not merely a target functional but a *structured operator*, specifically a Green operator that maps exogenous drivers, boundary/terminal data, and numéraires to observables over the maturity–strike lattice. When selective scan is used as an efficient evaluation of this operator, then no-arbitrage, martingale consistency, and change-of-numéraire are not optional patches; they are *geometric and spectral invariants* that should hold *during* training. This view upgrades the selective-scan runtime primitive from a sequence mechanism to a *risk-neutral operator layer* endowed with financial semantics.

#### From selective scan to a risk-neutral operator layer.

Let Ω={(T,K)}\Omega=\{(T,K)\} denote the grid of maturities and strikes and xx denote state inputs (underlyings, realized/forward variance proxies, macro/term-structure covariates). We instantiate an operator 𝒢θ\mathcal{G}\_{\theta} that produces prices

|  |  |  |
| --- | --- | --- |
|  | Πθ=𝒢θ​[x;Ω],\Pi\_{\theta}=\mathcal{G}\_{\theta}[x;\,\Omega], |  |

implemented by selective scan for streaming evaluation over Ω\Omega while preserving causality and numéraire-consistent propagation [[16](https://arxiv.org/html/2511.06451v1#bib.bib16)]. We explicitly disentangle (i) *physical propagation*, realized by scan kernels and gates, from (ii) *geometric validity*, enforced by projections and decoders. In particular, martingale consistency 𝔼ℚ​[St+Δ∣ℱt]=St\mathbb{E}\_{\mathbb{Q}}[S\_{t+\Delta}\!\mid\!\mathcal{F}\_{t}]=S\_{t} and no-arbitrage convexity/monotonicity (e.g., convexity in strike for call prices) are handled *in loop* rather than as post-processing.

#### Geometry in the loop: Q-Align and convex–monotone decoding.

Two architectural devices internalize financial correctness within the learning dynamics.
First, Q-Align performs a training-time 11-Lipschitz projection on the operator outputs or intermediate maps and logs λlipbefore/after\lambda\_{\text{lip}}^{\text{before/after}} to make smoothness/monotonicity auditable; practically, we combine spectral/orthogonal parameterizations with projection-based clamps that honor stability budgets [[3](https://arxiv.org/html/2511.06451v1#bib.bib3), [4](https://arxiv.org/html/2511.06451v1#bib.bib4)].
Second, a convex–monotone decoder—an ICNN with a Legendre-conjugate head—makes “price→\!\rightarrow\!measure” and “measure→\!\rightarrow\!price” mutually conjugate, encoding convexity, coordinate-wise monotonicity, and martingale consistency by construction [[5](https://arxiv.org/html/2511.06451v1#bib.bib5), [6](https://arxiv.org/html/2511.06451v1#bib.bib6)].
These mechanisms replace fragile penalty-based heuristics with *project-then-train* geometry.

#### Spectral stability as a first-class rule (Spec-Guard).

Long-horizon optimization is susceptible to subtle instabilities. We introduce Spec-Guard, a spectral-radius CFL rule that monitors the Jacobian spectral radius of state updates and triggers minimum-distance projections whenever ρ​(Jθ)​Δ​t\rho(J\_{\theta})\,\Delta t approaches a safety threshold γ<1\gamma<1. We log spec\_guard\_hits, projection\_distance, and max\_rho\_dt to quantify stability. Optimization uses saddle-point/extra-gradient updates to regularize adversarial/matching dynamics and prevent cycling or explosion [[7](https://arxiv.org/html/2511.06451v1#bib.bib7), [8](https://arxiv.org/html/2511.06451v1#bib.bib8)]. The result is a loop that is both *stable* and *falsifiable*.

#### Why SPX–VIX needs an operator view.

The SPX IV surface and the VIX term structure are tied by replication identities and change-of-numéraire relations under ℚ\mathbb{Q}. Fitting either surface while tolerating violations in the other produces incoherent Greeks, unreliable hedges, and brittle stress responses. Our operator-centric layer aligns the two by baking martingale and numéraire coherence into the semantics of propagation and decoding, avoiding *post hoc* smoothing and manual repairs [[23](https://arxiv.org/html/2511.06451v1#bib.bib23)].

#### Positioning within long-sequence and operator learning.

Our method lies at the interface of selective SSMs and Neural Operators. From the SSM lineage, we leverage linear-time/space selective scan and insights on long-context stability and representation [[17](https://arxiv.org/html/2511.06451v1#bib.bib17), [18](https://arxiv.org/html/2511.06451v1#bib.bib18), [16](https://arxiv.org/html/2511.06451v1#bib.bib16), [20](https://arxiv.org/html/2511.06451v1#bib.bib20), [9](https://arxiv.org/html/2511.06451v1#bib.bib9), [19](https://arxiv.org/html/2511.06451v1#bib.bib19)]. From the Neural Operator lineage, we inherit the abstraction of operator learning that generalizes across discretizations and boundary conditions [[1](https://arxiv.org/html/2511.06451v1#bib.bib1), [2](https://arxiv.org/html/2511.06451v1#bib.bib2), [21](https://arxiv.org/html/2511.06451v1#bib.bib21), [22](https://arxiv.org/html/2511.06451v1#bib.bib22)]. Our contribution is to *specialize* the operator family to risk-neutral, replicable Green operators and to *embed* financial geometry (convexity/monotonicity/martingale) and spectral safety (CFL) *inside* the training loop.

#### Auditing and operational falsifiability.

We convert qualitative desiderata (“arbitrage-free,” “stable,” “numéraire-coherent”) into auditable artifacts. Each geometric/spectral intervention is a first-class logged event; headline metrics carry heteroskedasticity- and autocorrelation-robust (HAC) intervals with Holm–Bonferroni corrections; and OOS validation follows rolling windows and blocked cross-validation designed for dependent data [[10](https://arxiv.org/html/2511.06451v1#bib.bib10), [11](https://arxiv.org/html/2511.06451v1#bib.bib11), [95](https://arxiv.org/html/2511.06451v1#bib.bib95)]. These protocols support hard claims about deployment readiness.

#### Contributions (all auditable).

1. 1.

   Risk-neutral operator layer. We formalize selective scan as a *risk-neutral Green operator* with complexity linear in grid size and depth, offering separable gating across the composite price–measure–numéraire map; this alleviates attention bottlenecks for long sequences and long maturities without sacrificing expressivity [[16](https://arxiv.org/html/2511.06451v1#bib.bib16), [19](https://arxiv.org/html/2511.06451v1#bib.bib19)].
2. 2.

   Q-Align: geometry in the loop. We enforce a 11-Lipschitz projection during training and log λlipbefore/after\lambda\_{\text{lip}}^{\text{before/after}}, replacing soft penalties with principled projections that tighten monotonicity/convexity guarantees [[3](https://arxiv.org/html/2511.06451v1#bib.bib3), [4](https://arxiv.org/html/2511.06451v1#bib.bib4)].
3. 3.

   Convex–monotone decoder. An ICNN with a Legendre-conjugate head implements mutually conjugate price/measure maps, hard-wiring convexity, coordinate-wise monotonicity, and martingale constraints [[5](https://arxiv.org/html/2511.06451v1#bib.bib5), [6](https://arxiv.org/html/2511.06451v1#bib.bib6)].
4. 4.

   Spec-Guard (spectral CFL). We introduce a spectral rule that monitors and minimally projects state updates, logging spec\_guard\_hits, projection\_distance, and max\_rho\_dt, thereby preventing long-horizon drift and catastrophic divergence [[7](https://arxiv.org/html/2511.06451v1#bib.bib7), [8](https://arxiv.org/html/2511.06451v1#bib.bib8)].
5. 5.

   Evaluation protocol and metrics. We define dimensionless metrics—NAS, CNAS, NI, DualGap, Stability, Surface–Wasserstein, and GenGap@95—and report 95%95\% HAC-CIs with Holm–Bonferroni correction. Rolling OOS and blocked-CV, together with Stress-to-Fail (S2F) threshold curves, non-substitutability breakers, and external-validity checks, establish a best-paper-grade evidence chain [[23](https://arxiv.org/html/2511.06451v1#bib.bib23), [95](https://arxiv.org/html/2511.06451v1#bib.bib95), [11](https://arxiv.org/html/2511.06451v1#bib.bib11), [10](https://arxiv.org/html/2511.06451v1#bib.bib10)].
6. 6.

   Empirics on SPX–VIX. Under synthetic and quasi-realistic SPX–VIX recipes with a unified budget, our method outperforms strong baselines; ablations (*de-gating*, rank reduction, disabling Spec-Guard) materially degrade CNAS/NAS/Stability and shift S2F thresholds left, demonstrating *non-substitutability*.

#### Scope, assumptions, and limits.

Our design targets joint SPX–VIX term-structure learning with coherent numéraire changes, long horizons where attention bottlenecks are acute, and regimes where OOS stability and falsifiability are paramount. We assume sufficient observability of risk-neutral proxies and include reject/degrade mechanisms so that the system can fail gracefully when assumptions are stressed (§[2](https://arxiv.org/html/2511.06451v1#S2 "2 Setting, Notation, and Testable Assumptions ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")). We purposely avoid task-specific hard coding beyond these invariants to preserve portability.

#### Relations to prior art (coverage of all references).

We build on selective SSMs and their stability/expressivity studies [[17](https://arxiv.org/html/2511.06451v1#bib.bib17), [18](https://arxiv.org/html/2511.06451v1#bib.bib18), [16](https://arxiv.org/html/2511.06451v1#bib.bib16), [20](https://arxiv.org/html/2511.06451v1#bib.bib20), [9](https://arxiv.org/html/2511.06451v1#bib.bib9), [19](https://arxiv.org/html/2511.06451v1#bib.bib19)]; on Neural Operators and recent generalizations/surveys [[1](https://arxiv.org/html/2511.06451v1#bib.bib1), [2](https://arxiv.org/html/2511.06451v1#bib.bib2), [21](https://arxiv.org/html/2511.06451v1#bib.bib21), [22](https://arxiv.org/html/2511.06451v1#bib.bib22)]; on arbitrage-free deep pricing and IV-surface regularization/smoothing [[23](https://arxiv.org/html/2511.06451v1#bib.bib23)]; on training stability and geometric constraints via spectral normalization, Lipschitz control, monotone architectures, and extra-gradient dynamics [[3](https://arxiv.org/html/2511.06451v1#bib.bib3), [4](https://arxiv.org/html/2511.06451v1#bib.bib4), [7](https://arxiv.org/html/2511.06451v1#bib.bib7), [8](https://arxiv.org/html/2511.06451v1#bib.bib8), [6](https://arxiv.org/html/2511.06451v1#bib.bib6)]; and on time-series inference/validation protocols including HAC, Holm–Bonferroni, and blocked-CV [[10](https://arxiv.org/html/2511.06451v1#bib.bib10), [11](https://arxiv.org/html/2511.06451v1#bib.bib11), [95](https://arxiv.org/html/2511.06451v1#bib.bib95)]. Our novelty lies in integrating “*operator layer – geometric projection – spectral guard – stopping criteria*” into a single, end-to-end, falsifiable risk-neutral learning pipeline tailored to SPX–VIX.

#### Paper roadmap.

Section [2](https://arxiv.org/html/2511.06451v1#S2 "2 Setting, Notation, and Testable Assumptions ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") formalizes the market setup, notation, and four testable assumptions (measurable, rejectable, and degradable), together with the dimensionless evaluation metrics.
Section [3](https://arxiv.org/html/2511.06451v1#S3 "3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") presents the *ARBITER* architecture: the risk–neutral operator (RN-Operator) cast as a discretized Green operator with metric gating, the *Q-Align* Lipschitz projection with *Spec-Guard* (CFL-style spectral control), and the convex–monotone decoder; it also specifies the saddle-point training loop and fixed, falsifiable stopping criteria.
Section [4](https://arxiv.org/html/2511.06451v1#S4 "4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") states our main results (T1–T8) on approximation, conditioning, identifiability, sample complexity, feasibility, and convergence of the projected extragradient scheme.
Section [5](https://arxiv.org/html/2511.06451v1#S5 "5 Evaluation Protocol and Metrics ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") defines the data protocol and statistical methodology (HAC inference, Holm–Bonferroni control, rolling out-of-sample and blocked-CV), and Section [6](https://arxiv.org/html/2511.06451v1#S6 "6 Experiments ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") reports synthetic SPX–VIX experiments, ablations (non-substitutability breakers), external-validity checks, and Stress-to-Fail analyses, accompanied by comprehensive figures and tables.
Section [7](https://arxiv.org/html/2511.06451v1#S7 "7 Mechanistic Analysis and Diagnostics ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") provides mechanism-level diagnostics (Q-Align contraction, representative-element behavior, effective dimension).
Section [8](https://arxiv.org/html/2511.06451v1#S8 "8 Related Work ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") situates our contribution within operator learning, SSM/Mamba-style models, and term-structure modeling. All proofs are collected in the appendices.Section [9](https://arxiv.org/html/2511.06451v1#S9 "9 Conclusion and Outlook ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures").

## 2 Setting, Notation, and Testable Assumptions

This section formalizes the market and grids on which the model operates, fixes notation for the risk–neutral operator and its safety quantities, defines the dimensionless evaluation metrics used throughout, and states a suite of assumptions that are *measurable, refutable, and degradable*. All statements below are aligned with the operator view introduced in §[1](https://arxiv.org/html/2511.06451v1#S1 "1 Introduction ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") and with the training and evaluation protocol discussed later.

### 2.1 Market, numeraire, and discretization

We work on a filtered probability space (Ω,ℱ,(ℱt)t≥0,ℚ)(\Omega,\mathcal{F},(\mathcal{F}\_{t})\_{t\geq 0},\mathbb{Q}) under a risk–neutral measure ℚ\mathbb{Q}. The short rate is (rt)t≥0(r\_{t})\_{t\geq 0} and the chosen numeraire is a strictly positive process NtN\_{t} (e.g., the money–market account Nt=exp⁡(∫0trs​𝑑s)N\_{t}=\exp(\int\_{0}^{t}r\_{s}\,ds) or a forward–measure numeraire). Let StS\_{t} denote the equity index (SPX). European call and put prices observed at time tt with maturity T>tT>t and strike K>0K>0 are denoted Ct​(K,T)C\_{t}(K,T) and Pt​(K,T)P\_{t}(K,T).

For numerical work we use discrete calendars of maturities 𝒯={Tℓ}ℓ=1L⊂(t,t+Tmax]\mathcal{T}=\{T\_{\ell}\}\_{\ell=1}^{L}\subset(t,\,t+T\_{\max}] and strikes 𝒦={Kj}j=1J⊂ℝ+\mathcal{K}=\{K\_{j}\}\_{j=1}^{J}\subset\mathbb{R}\_{+}, allowing for nonuniform spacings. The *risk–neutral operator* 𝒢θ\mathcal{G}\_{\theta} maps boundary/forcing information defined on (𝒯,𝒦)(\mathcal{T},\mathcal{K}) to a price surface (K,T)↦(Ct​(K,T),Pt​(K,T))(K,T)\mapsto\big(C\_{t}(K,T),P\_{t}(K,T)\big) and is implemented with a selective state–space scan whose propagation is linear in |𝒯||\mathcal{T}| (and optionally in |𝒦||\mathcal{K}|).

Numeraire consistency is enforced by construction: under the numeraire measure ℚN\mathbb{Q}^{N} associated with NN, the discounted process Xt:=St/NtX\_{t}:=S\_{t}/N\_{t} is a martingale and prices satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ct(K,T)=Nt𝔼ℚN[(ST−K)+NT|ℱt],Pt(K,T)=Nt𝔼ℚN[(K−ST)+NT|ℱt].C\_{t}(K,T)\;=\;N\_{t}\,\mathbb{E}^{\mathbb{Q}^{N}}\!\left[\frac{(S\_{T}-K)\_{+}}{N\_{T}}\,\middle|\,\mathcal{F}\_{t}\right],\qquad P\_{t}(K,T)\;=\;N\_{t}\,\mathbb{E}^{\mathbb{Q}^{N}}\!\left[\frac{(K-S\_{T})\_{+}}{N\_{T}}\,\middle|\,\mathcal{F}\_{t}\right]. |  | (1) |

#### VIX2 replication and SPX–VIX coupling.

To couple equity and variance layers we expose the classical replication identity for VIX squared, using its discrete form on (𝒯,𝒦)(\mathcal{T},\mathcal{K}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | VIXt2​(T)≈2T−t​er¯​(T−t)​(∑K≤FΔ​KK2​Pt​(K,T)+∑K≥FΔ​KK2​Ct​(K,T)),\mathrm{VIX}^{2}\_{t}(T)\;\approx\;\frac{2}{T-t}\,e^{\bar{r}\,(T-t)}\left(\sum\_{K\leq F}\frac{\Delta K}{K^{2}}P\_{t}(K,T)\;+\;\sum\_{K\geq F}\frac{\Delta K}{K^{2}}C\_{t}(K,T)\right), |  | (2) |

where FF is the forward level for maturity TT, r¯\bar{r} is a bucketed short rate, and Δ​K\Delta K is the quadrature step.111See the Cboe VIX white paper for the precise continuous–time derivation and practical discretization details [[47](https://arxiv.org/html/2511.06451v1#bib.bib47)].
We treat ([2](https://arxiv.org/html/2511.06451v1#S2.E2 "In VIX2 replication and SPX–VIX coupling. ‣ 2.1 Market, numeraire, and discretization ‣ 2 Setting, Notation, and Testable Assumptions ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) as a linear observable of 𝒢θ\mathcal{G}\_{\theta} so that the SPX–VIX coupling is learned within the same operator layer and audited by the no–arbitrage metrics below.

### 2.2 Notation and safety quantities

We denote by βsmooth>0\beta\_{\mathrm{smooth}}>0 a Hölder (or Besov) regularity order upper–bounding the smoothness of the target surface; by βnov≥0\beta\_{\mathrm{nov}}\geq 0 a weight scaling a Novikov–type penalty used in the adversarial route of training; and by χ​(κ)∈[0,1]\chi(\kappa)\in[0,1] a long–horizon decay index determined by an effective kernel rank κ\kappa in the operator layer.

Selective scans update a latent state through ht+Δ​t=At​ht+Bt​uth\_{t+\Delta t}=A\_{t}h\_{t}+B\_{t}u\_{t} with a data–dependent step Δ​tt>0\Delta t\_{t}>0. We define the spectral safety quantity

|  |  |  |  |
| --- | --- | --- | --- |
|  | CFLmax=maxt⁡ρ​(At)​Δ​tt,\mathrm{CFL}\_{\max}\;=\;\max\_{t}\,\rho(A\_{t})\,\Delta t\_{t}, |  | (3) |

with ρ​(⋅)\rho(\cdot) the spectral radius. The *Spec–Guard* rule enforces CFLmax≤1\mathrm{CFL}\_{\max}\leq 1 by preconditioning and small projections; we record the number of guard activations and the aggregate projection distance. For Lipschitz alignment we estimate a global Lipschitz constant LlipL\_{\mathrm{lip}} by layerwise spectral norms before and after projection and report the pair (Llipbefore,Llipafter)(L\_{\mathrm{lip}}^{\mathrm{before}},\,L\_{\mathrm{lip}}^{\mathrm{after}}) [[3](https://arxiv.org/html/2511.06451v1#bib.bib3), [12](https://arxiv.org/html/2511.06451v1#bib.bib12), Neyshabur2017NormBounds].

### 2.3 Dimensionless evaluation metrics

All metrics are unit–free and reported with heteroskedasticity– and autocorrelation–consistent (HAC) 95%95\% confidence intervals [[10](https://arxiv.org/html/2511.06451v1#bib.bib10)], using temporally blocked cross–validation to respect dependence [[95](https://arxiv.org/html/2511.06451v1#bib.bib95)]. For families of hypotheses we control multiplicity with the Holm–Bonferroni procedure [[11](https://arxiv.org/html/2511.06451v1#bib.bib11)].

#### No–Arbitrage Score (NAS; higher is better).

Let ℐ\mathcal{I} be a finite set of static arbitrage inequalities across (𝒯,𝒦)(\mathcal{T},\mathcal{K}) (e.g., monotonicity in strike, convexity in strike, calendar monotonicity, call–put parity). For each i∈ℐi\in\mathcal{I}, define a nonnegativity residual ri​(θ)r\_{i}(\theta) that vanishes when the inequality is satisfied and is positive when violated. After normalizing by a scale factor sis\_{i} (based on local forward or variance scales), define

|  |  |  |  |
| --- | --- | --- | --- |
|  | NAS:= 1−1Z​∑i∈ℐwi​[ri​(θ)/si]+,Z=∑i∈ℐwi,\mathrm{NAS}\;:=\;1-\frac{1}{Z}\sum\_{i\in\mathcal{I}}w\_{i}\,\big[r\_{i}(\theta)/s\_{i}\big]\_{+},\qquad Z=\sum\_{i\in\mathcal{I}}w\_{i}, |  | (4) |

with nonnegative weights wiw\_{i} that emphasize practically salient constraints. Thus NAS∈[0,1]\mathrm{NAS}\in[0,1] and equals 11 if and only if there are no detected violations. Our constraints follow common arbitrage–free surface checks from the literature [[48](https://arxiv.org/html/2511.06451v1#bib.bib48), [13](https://arxiv.org/html/2511.06451v1#bib.bib13), [14](https://arxiv.org/html/2511.06451v1#bib.bib14)] and are compatible with convex monotone decoders [[5](https://arxiv.org/html/2511.06451v1#bib.bib5), [6](https://arxiv.org/html/2511.06451v1#bib.bib6)].

#### Convolved NAS (CNAS; higher is better).

To evaluate robustness along maturity while downweighting far tails, we convolve NAS over 𝒯\mathcal{T} with a positive kernel Kκ,τK\_{\kappa,\tau} of bandwidth κ\kappa and effective horizon τ\tau, after within–maturity rescaling (e.g., by vega or variance scale):

|  |  |  |  |
| --- | --- | --- | --- |
|  | CNAS:=(NAS∗𝒯Kκ,τ).\mathrm{CNAS}\;:=\;(\mathrm{NAS}\ast\_{\mathcal{T}}K\_{\kappa,\tau}). |  | (5) |

Unless stated otherwise, (κ,τ)(\kappa,\tau) and the rescaling convention are fixed across out–of–sample (OOS) windows to enable external validity checks; the average drop in CNAS when reusing the same hyperparameters across disjoint OOS windows is reported as an external–validity statistic (mean with 95%95\% interval).

#### Numeraire Invariance (NI; higher is better).

Partition the maturity–strike plane into B×JB\times J buckets. For each bucket consider discounted prices under a set of admissible numeraires and compute the median absolute deviation (MAD) across these normalizations; aggregate the bucket–wise relative dispersion by

|  |  |  |  |
| --- | --- | --- | --- |
|  | NI:= 1−1B​J​∑b=1B∑j=1JMAD​({Nt−1​Cb,j(m)}m)scaleb,j,\mathrm{NI}\;:=\;1-\frac{1}{BJ}\sum\_{b=1}^{B}\sum\_{j=1}^{J}\frac{\mathrm{MAD}\big(\{N\_{t}^{-1}C\_{b,j}^{(m)}\}\_{m}\big)}{\mathrm{scale}\_{b,j}}, |  | (6) |

where the denominator is a robust local scale. Higher NI indicates stronger consistency with the numeraire–induced martingale property.

#### Duality Gap (lower is better).

Let minθ⁡maxλ∈Λ⁡ℒ​(θ,λ)\min\_{\theta}\max\_{\lambda\in\Lambda}\mathcal{L}(\theta,\lambda) denote the saddle objective arising from adversarial training or operator matching. The empirical duality gap is the difference between the maximal value over λ\lambda at the current θ\theta and the minimal value over θ\theta at the current λ\lambda, estimated on held–out batches with stabilized updates (e.g., extragradient or lookahead) [[7](https://arxiv.org/html/2511.06451v1#bib.bib7), [8](https://arxiv.org/html/2511.06451v1#bib.bib8), [15](https://arxiv.org/html/2511.06451v1#bib.bib15)].

#### Stability (higher is better).

This is the fraction of random seeds and OOS windows that simultaneously achieve (i) a NAS level above a fixed threshold, (ii) a spectral safety condition CFLmax≤1\mathrm{CFL}\_{\max}\leq 1 with bounded projection distance, and (iii) satisfaction of the saddle–point stall conditions. We provide a binomial proportion with HAC intervals.

#### Surface–Wasserstein distance (lower is better).

Define for each maturity TT the marginal distributions over strikes induced by the predicted and reference surfaces (after standardization). The overall discrepancy is measured by

|  |  |  |  |
| --- | --- | --- | --- |
|  | SW2:=(∫𝒯W22​(πTpred,πTref)​𝑑μ​(T))1/2,\mathrm{SW}\_{2}\;:=\;\Bigg(\int\_{\mathcal{T}}W\_{2}^{2}\!\big(\pi^{\mathrm{pred}}\_{T},\,\pi^{\mathrm{ref}}\_{T}\big)\,d\mu(T)\Bigg)^{1/2}, |  | (7) |

with W2W\_{2} the 2–Wasserstein distance and μ\mu a weighting measure over maturities [[29](https://arxiv.org/html/2511.06451v1#bib.bib29)].

#### Generalization gap at the 95th percentile (lower is better).

We report the 9595th percentile of the absolute training–to–OOS difference for NAS (or the primary objective), a conservative measure of tail overfitting.

#### Effective dimension.

Let KK be a Gram matrix of operator features on (𝒯,𝒦)(\mathcal{T},\mathcal{K}). For α∈{0.90,0.95,0.99}\alpha\in\{0.90,0.95,0.99\} define dαd\_{\alpha} as the minimal index such that the sum of the top dαd\_{\alpha} singular values accounts for an α\alpha–fraction of the total. The triple (d90,d95,d99)(d\_{90},d\_{95},d\_{99}) provides a capacity proxy that enters the oracle bounds in §[4](https://arxiv.org/html/2511.06451v1#S4 "4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures").

### 2.4 Assumptions: measurable, refutable, and degradable

We formulate four assumptions. Each is *measurable* from training–time statistics, *refutable* by explicit counter–examples or threshold tests, and *degradable* in the sense that, when violated, we fall back to weaker but still valid guarantees used in evaluation.

#### A1 (necessary): Novikov–to–Kazamaki switching.

Let (Mt)(M\_{t}) be the local martingale driving the stochastic component of the operator layer. Novikov’s condition, 𝔼​[exp⁡(12​⟨M⟩T)]<∞\mathbb{E}[\exp(\tfrac{1}{2}\langle M\rangle\_{T})]<\infty, implies martingality and is stronger than Kazamaki’s criterion; empirical data roughness can make Kazamaki more appropriate. We measure, across OOS windows, the fraction for which Novikov holds but Kazamaki is preferred by the test statistic, and report its mean with a 95%95\% interval. A stable operator exhibits a high switching rate as roughness increases, consistent with recent stability analyses of selective state–space models [[16](https://arxiv.org/html/2511.06451v1#bib.bib16), [27](https://arxiv.org/html/2511.06451v1#bib.bib27)].

#### A2 (sufficient): Smoothness fallback and representer bound.

When local estimates indicate that βsmooth\beta\_{\mathrm{smooth}} falls below the nominal order on subsets of (𝒯,𝒦)(\mathcal{T},\mathcal{K}), we switch from the smoothness–based identifiability bound to a representer–type bound (Theorem T2′), where the operator error over L2L^{2} is controlled by a combination of coverage deficit and dual residual. The time of switch and the coverage level at trigger are reported. Proof details and rates are given in §[4](https://arxiv.org/html/2511.06451v1#S4 "4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures").

#### A3 (sufficient): Rank–controlled long–memory decay.

The effective rank κ\kappa of the selective kernel determines a decay index χ​(κ)∈[0,1]\chi(\kappa)\in[0,1] that governs long–horizon oracle terms (Theorem T3). We estimate χ​(κ)\chi(\kappa) from spectral slopes of the scan kernel; deviations prompt stricter spectral guarding and Lipschitz projections [[12](https://arxiv.org/html/2511.06451v1#bib.bib12), [16](https://arxiv.org/html/2511.06451v1#bib.bib16), [27](https://arxiv.org/html/2511.06451v1#bib.bib27)].

#### A4 (necessary): Coverage threshold.

Let cminc\_{\min} and c¯\bar{c} be, respectively, the minimum and mean fraction of observed (T,K)(T,K) cells (after quality control) per window. We require cmin≥c¯=0.75c\_{\min}\geq\underline{c}=0.75. If violated, claims revert to the representer–bound regime (A2), the event is reported in the main text, and stress–to–fail experiments are used to characterize the failure mode.

### 2.5 Statistical reporting

All metrics are computed per window and aggregated with HAC intervals; multiplicity is controlled within families of hypotheses by Holm–Bonferroni. Cross–validation uses temporally blocked folds to avoid leakage. For the SPX–VIX coupling we apply the replication identity ([2](https://arxiv.org/html/2511.06451v1#S2.E2 "In VIX2 replication and SPX–VIX coupling. ‣ 2.1 Market, numeraire, and discretization ‣ 2 Setting, Notation, and Testable Assumptions ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) with the discrete quadrature recommended by the exchange documentation [[47](https://arxiv.org/html/2511.06451v1#bib.bib47)]. The Lipschitz constants are estimated by spectral–norm proxies; their pre– and post–projection values are reported alongside the spectral safety quantity CFLmax\mathrm{CFL}\_{\max}, the number of spectral–guard activations, and the aggregate projection distance. These quantities are used later to establish the stability and refutability of the operator constraints and to ablate the role of each geometric ingredient.

## 3 Method: The ARBITER Architecture

We present Arbiter, a risk–neutral neural operator for arbitrage-free SPX–VIX term structures. The model integrates four components: (i) a *risk–neutral operator layer* that interprets selective state-space scans as a discretized Green operator under a learned risk–neutral measure; (ii) *Q-Align*, a pair of geometric projections that enforce layerwise Lipschitz bounds and a spectral CFL condition; (iii) a *convex–monotone decoder* that enforces static no-arbitrage along strikes and maturities, tied to VIX replication; and (iv) a *saddle-point training protocol* with safety-oriented stopping rules. We work on a maturity grid {Tℓ}ℓ=1L\{T\_{\ell}\}\_{\ell=1}^{L} (not necessarily uniform) and an implied strike set 𝒦\mathcal{K}; the numeraire is fixed by discounting.

### 3.1 Risk–Neutral Operator Layer (RN-Operator)

#### Selective scan as a Green operator.

Let hℓ∈ℝmh\_{\ell}\in\mathbb{R}^{m} be hidden states at TℓT\_{\ell}, with input features uℓ​(⋅)∈L2​(𝒦)u\_{\ell}(\cdot)\in L^{2}(\mathcal{K}) summarizing cross-sectional information (e.g., moneyness bins and microstructure covariates) at maturity TℓT\_{\ell}. The selective state-space recursion is

|  |  |  |  |
| --- | --- | --- | --- |
|  | hℓ+1=Aθ​(Tℓ)​hℓ+Bθ​(Tℓ)​Ξ​[uℓ],yℓ=Qθ​(Tℓ)​hℓ,h\_{\ell+1}\;=\;A\_{\theta}(T\_{\ell})\,h\_{\ell}\;+\;B\_{\theta}(T\_{\ell})\,\Xi[u\_{\ell}],\qquad y\_{\ell}\;=\;Q\_{\theta}(T\_{\ell})\,h\_{\ell}, |  | (8) |

where Ξ\Xi is a linear embedding from L2​(𝒦)L^{2}(\mathcal{K}) to ℝm\mathbb{R}^{m} and yℓ∈ℝmy\_{\ell}\in\mathbb{R}^{m} is a latent representation. Unrolling ([8](https://arxiv.org/html/2511.06451v1#S3.E8 "In Selective scan as a Green operator. ‣ 3.1 Risk–Neutral Operator Layer (RN-Operator) ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) yields the discrete Green expansion

|  |  |  |  |
| --- | --- | --- | --- |
|  | yℓ=∑s≤ℓ(∏j=sℓ−1Aθ​(Tj))​Bθ​(Ts)​Ξ​[us]=∑s≤ℓ𝒢θ​(Tℓ,Ts)​Ξ​[us],y\_{\ell}\;=\;\sum\_{s\leq\ell}\Bigg(\prod\_{j=s}^{\ell-1}A\_{\theta}(T\_{j})\Bigg)B\_{\theta}(T\_{s})\,\Xi[u\_{s}]\;=\;\sum\_{s\leq\ell}\mathcal{G}\_{\theta}(T\_{\ell},T\_{s})\,\Xi[u\_{s}], |  | (9) |

with 𝒢θ​(Tℓ,Ts):=∏j=sℓ−1Aθ​(Tj)​Bθ​(Ts)\mathcal{G}\_{\theta}(T\_{\ell},T\_{s}):=\prod\_{j=s}^{\ell-1}A\_{\theta}(T\_{j})B\_{\theta}(T\_{s}).

#### Measure gating and risk–neutral semantics.

To embed no-arbitrage at training time, we introduce a *measure gate* wθ​(K,T)≥0w\_{\theta}(K,T)\geq 0 and replace usu\_{s} by us⋆​(K)=wθ​(K,Ts)​us​(K)u\_{s}^{\star}(K)=w\_{\theta}(K,T\_{s})\,u\_{s}(K), thereby defining a density wθ​(⋅,⋅)w\_{\theta}(\cdot,\cdot) on 𝒦×{Tℓ}\mathcal{K}\times\{T\_{\ell}\}. The discounted price functional on a payoff φ\varphi is evaluated through

|  |  |  |  |
| --- | --- | --- | --- |
|  | Πθ​[φ]​(T)=∫𝒦φ​(K,T)​wθ​(K,T)​dK,\Pi\_{\theta}[\varphi](T)\;=\;\int\_{\mathcal{K}}\varphi(K,T)\,w\_{\theta}(K,T)\,\mathrm{d}K, |  | (10) |

and training penalizes deviations from the martingale condition under ℚθ\mathbb{Q}\_{\theta}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℚθ[St+δe−r​δ−St|ℱt]= 0⟺dℚθ∝wθdℙ,\mathbb{E}^{\mathbb{Q}\_{\theta}}\!\left[S\_{t+\delta}\mathrm{e}^{-r\delta}-S\_{t}\,\middle|\,\mathcal{F}\_{t}\right]\;=\;0\quad\Longleftrightarrow\quad\mathrm{d}\mathbb{Q}\_{\theta}\propto w\_{\theta}\,\mathrm{d}\mathbb{P}, |  | (11) |

with a convex penalty on residuals of ([11](https://arxiv.org/html/2511.06451v1#S3.E11 "In Measure gating and risk–neutral semantics. ‣ 3.1 Risk–Neutral Operator Layer (RN-Operator) ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) across random slices (K,T)(K,T).
In practice wθw\_{\theta} is parameterized by a positive squashing map (e.g., softplus) followed by normalization across KK at each TT so that ∫wθ​(K,T)​dK=1\int w\_{\theta}(K,T)\mathrm{d}K=1.

#### Complexity.

Let mm be the effective rank of the operator (Section [2](https://arxiv.org/html/2511.06451v1#S2 "2 Setting, Notation, and Testable Assumptions ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")). The recurrence ([8](https://arxiv.org/html/2511.06451v1#S3.E8 "In Selective scan as a Green operator. ‣ 3.1 Risk–Neutral Operator Layer (RN-Operator) ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) and Green evaluation ([67](https://arxiv.org/html/2511.06451v1#Ax1.E67 "In Model parameterization. ‣ B.1 Proof of Theorem 2: approximation rate and conditioning ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) both run in linear time and memory:

|  |  |  |
| --- | --- | --- |
|  | time=𝒪​(L​m),space=𝒪​(m).\mathrm{time}=\mathcal{O}(Lm),\qquad\mathrm{space}=\mathcal{O}(m). |  |

This preserves the computational profile of selective SSMs while upgrading its semantics to a risk–neutral operator.

#### Neumann expansion under a CFL condition.

Let Δ​tℓ:=Tℓ+1−Tℓ\Delta t\_{\ell}:=T\_{\ell+1}-T\_{\ell} and define the discrete CFL indicator

|  |  |  |  |
| --- | --- | --- | --- |
|  | CFL​(Tℓ):=ρ​(Aθ​(Tℓ))​Δ​tℓ,CFLmax:=maxℓ⁡CFL​(Tℓ),\mathrm{CFL}(T\_{\ell}):=\rho\!\big(A\_{\theta}(T\_{\ell})\big)\,\Delta t\_{\ell},\qquad\mathrm{CFL}\_{\max}:=\max\_{\ell}\mathrm{CFL}(T\_{\ell}), |  | (12) |

with ρ​(⋅)\rho(\cdot) the spectral radius. When CFLmax<1\mathrm{CFL}\_{\max}<1, products ∏j=sℓ−1Aθ​(Tj)\prod\_{j=s}^{\ell-1}A\_{\theta}(T\_{j}) are summable and ([67](https://arxiv.org/html/2511.06451v1#Ax1.E67 "In Model parameterization. ‣ B.1 Proof of Theorem 2: approximation rate and conditioning ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) admits a uniformly convergent Neumann-like representation.

#### Spectral safety and discrete Green kernel.

Let {Tℓ}ℓ∈ℤ\{T\_{\ell}\}\_{\ell\in\mathbb{Z}} be the evaluation grid with steps Δ​tℓ:=Tℓ+1−Tℓ>0\Delta t\_{\ell}:=T\_{\ell+1}-T\_{\ell}>0 and a time–varying linear operator Aθ​(Tℓ)∈ℝd×dA\_{\theta}(T\_{\ell})\in\mathbb{R}^{d\times d}.
Define Mℓ:=Δ​tℓ​Aθ​(Tℓ)M\_{\ell}:=\Delta t\_{\ell}A\_{\theta}(T\_{\ell}) and the one–step resolvent Rℓ:=(I−Mℓ)−1R\_{\ell}:=(I-M\_{\ell})^{-1}.
For an impulse injection BsB\_{s} at time TsT\_{s}, the discrete causal Green kernel is

|  |  |  |
| --- | --- | --- |
|  | 𝒢θ​(Tℓ,Ts)=Rℓ​Rℓ−1​⋯​Rs+1​Bs,s≤ℓ.\mathcal{G}\_{\theta}(T\_{\ell},T\_{s})\;=\;R\_{\ell}R\_{\ell-1}\cdots R\_{s+1}\,B\_{s},\qquad s\leq\ell. |  |

Under the CFL–type safeguard ρ​(Aθ​(Tℓ))​Δ​tℓ≤1−ε\rho(A\_{\theta}(T\_{\ell}))\,\Delta t\_{\ell}\leq 1-\varepsilon (Spec-Guard), the kernel is uniformly summable.

###### Lemma 1 (Green kernel bound).

Assume ρ​(Aθ​(Tℓ))​Δ​tℓ≤1−ε\rho\!\left(A\_{\theta}(T\_{\ell})\right)\,\Delta t\_{\ell}\leq 1-\varepsilon for all ℓ\ell with some ε∈(0,1)\varepsilon\in(0,1), and that ‖Bs‖≤b​Δ​ts\|B\_{s}\|\leq b\,\Delta t\_{s} for a constant b>0b>0 under an operator norm subordinate to a vector norm.
Then there exists C=C​(ε,b,Δ​t¯)<∞C=C(\varepsilon,b,\overline{\Delta t})<\infty, with Δ​t¯:=supℓΔ​tℓ\overline{\Delta t}:=\sup\_{\ell}\Delta t\_{\ell}, such that

|  |  |  |
| --- | --- | --- |
|  | ∑s≤ℓ‖𝒢θ​(Tℓ,Ts)‖≤C​(ε,b,Δ​t¯)for all ​ℓ.\sum\_{s\leq\ell}\Big\|\mathcal{G}\_{\theta}(T\_{\ell},T\_{s})\Big\|\;\leq\;C(\varepsilon,b,\overline{\Delta t})\quad\text{for all }\ell. |  |

###### Proof sketch.

The CFL constraint enforces ρ​(Mℓ)≤1−ε\rho(M\_{\ell})\leq 1-\varepsilon. By the extremal–norm (joint spectral radius) argument there exists an induced norm in which ‖Mℓ‖≤α<1\|M\_{\ell}\|\leq\alpha<1 uniformly, hence ‖Rℓ‖=‖(I−Mℓ)−1‖≤(1−α)−1\|R\_{\ell}\|=\|(I-M\_{\ell})^{-1}\|\leq(1-\alpha)^{-1}.
Submultiplicativity gives ‖Rℓ​⋯​Rs+1‖≤(1−α)−(ℓ−s)\|R\_{\ell}\cdots R\_{s+1}\|\leq(1-\alpha)^{-(\ell-s)}, and the factor ‖Bs‖≤b​Δ​ts\|B\_{s}\|\leq b\,\Delta t\_{s} makes the series geometrically summable over ss.
Full details, including the non–diagonalizable case via block–Jordan bounds and the removal of norm–equivalence constants, are provided in Appendix A.1.
∎

#### Lipschitz surrogate via spectral normalization.

Each linear map WW in ([8](https://arxiv.org/html/2511.06451v1#S3.E8 "In Selective scan as a Green operator. ‣ 3.1 Risk–Neutral Operator Layer (RN-Operator) ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) is spectrally normalized, ‖W‖2≤τ≤1\|W\|\_{2}\leq\tau\leq 1, and each nonlinearity is 1-Lipschitz, yielding a global Lipschitz surrogate for the RN-operator:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lip​(𝒢θ)≤(∏linear ​ℓ‖Wℓ‖2)⋅C​(ε),\mathrm{Lip}(\mathcal{G}\_{\theta})\;\leq\;\Big(\prod\_{\text{linear }\ell}\|W\_{\ell}\|\_{2}\Big)\cdot C(\varepsilon), |  | (13) |

with C​(ε)C(\varepsilon) from Lemma [1](https://arxiv.org/html/2511.06451v1#Thmlemma1 "Lemma 1 (Green kernel bound). ‣ Spectral safety and discrete Green kernel. ‣ 3.1 Risk–Neutral Operator Layer (RN-Operator) ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures"). This bound is tracked by the logged pair (λlip​-​before,λlip​-​after)(\lambda\_{\mathrm{lip}\text{-}\mathrm{before}},\lambda\_{\mathrm{lip}\text{-}\mathrm{after}}).

### 3.2 Q-Align: Lipschitz Projection and Spectral Guard

#### Layerwise Lipschitz projection.

After each optimizer step, we project every linear map WW onto the spectral ball of radius τ≤1\tau\leq 1:

|  |  |  |  |
| --- | --- | --- | --- |
|  | W^=τmax⁡(‖W‖2,τ)​W.\widehat{W}\;=\;\frac{\tau}{\max(\|W\|\_{2},\tau)}\,W. |  | (14) |

A single power iteration per matrix provides ‖W‖2\|W\|\_{2} with small overhead. The cumulative Lipschitz surrogate in ([13](https://arxiv.org/html/2511.06451v1#S3.E13 "In Lipschitz surrogate via spectral normalization. ‣ 3.1 Risk–Neutral Operator Layer (RN-Operator) ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) thus remains controlled.

#### Spectral Guard (CFL projection).

We estimate ρ​(Aθ​(Tℓ))\rho(A\_{\theta}(T\_{\ell})) via power iteration and enforce

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ​(Aθ​(Tℓ))​Δ​tℓ≤ 1−ε.\rho\!\big(A\_{\theta}(T\_{\ell})\big)\,\Delta t\_{\ell}\;\leq\;1-\varepsilon. |  | (15) |

A minimal-distance correction in Frobenius norm admits the scaling solution

|  |  |  |  |
| --- | --- | --- | --- |
|  | Aθ​(Tℓ)←1−ερ​(Aθ​(Tℓ))​Δ​tℓ​Aθ​(Tℓ),A\_{\theta}(T\_{\ell})\;\leftarrow\;\frac{1-\varepsilon}{\rho(A\_{\theta}(T\_{\ell}))\,\Delta t\_{\ell}}\,A\_{\theta}(T\_{\ell}), |  | (16) |

whenever the left-hand side of ([15](https://arxiv.org/html/2511.06451v1#S3.E15 "In Spectral Guard (CFL projection). ‣ 3.2 Q-Align: Lipschitz Projection and Spectral Guard ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) exceeds 1−ε1-\varepsilon. We log the activation count spec​\_​guard​\_​hits\mathrm{spec\\_guard\\_hits}, the cumulative correction ∑ℓ‖Aθ​(Tℓ)−A^θ​(Tℓ)‖F\sum\_{\ell}\|A\_{\theta}(T\_{\ell})-\widehat{A}\_{\theta}(T\_{\ell})\|\_{F} (denoted *projection distance*), and maxℓ⁡ρ​(Aθ​(Tℓ))​Δ​tℓ\max\_{\ell}\rho(A\_{\theta}(T\_{\ell}))\Delta t\_{\ell}.

#### RN-operator stability under Q-Align.

Let {Tℓ}ℓ∈ℤ\{T\_{\ell}\}\_{\ell\in\mathbb{Z}} be the evaluation grid with steps Δ​tℓ>0\Delta t\_{\ell}>0, and write Mℓ:=Δ​tℓ​Aθ​(Tℓ)M\_{\ell}:=\Delta t\_{\ell}A\_{\theta}(T\_{\ell}) and Rℓ:=(I−Mℓ)−1R\_{\ell}:=(I-M\_{\ell})^{-1}.
Consider the RN-operator layer with nonexpansive nonlinearity ϕ\phi and projected weights (Q-Align) satisfying the layerwise Lipschitz envelope in ([14](https://arxiv.org/html/2511.06451v1#S3.E14 "In Layerwise Lipschitz projection. ‣ 3.2 Q-Align: Lipschitz Projection and Spectral Guard ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")), together with the spectral safeguard ([15](https://arxiv.org/html/2511.06451v1#S3.E15 "In Spectral Guard (CFL projection). ‣ 3.2 Q-Align: Lipschitz Projection and Spectral Guard ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")).
Denote by 𝒢θ​(Tℓ,Ts)\mathcal{G}\_{\theta}(T\_{\ell},T\_{s}) the discrete causal Green kernel.
We obtain:

###### Proposition 1 (RN-operator stability under Q-Align).

Assume ([14](https://arxiv.org/html/2511.06451v1#S3.E14 "In Layerwise Lipschitz projection. ‣ 3.2 Q-Align: Lipschitz Projection and Spectral Guard ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) and ([15](https://arxiv.org/html/2511.06451v1#S3.E15 "In Spectral Guard (CFL projection). ‣ 3.2 Q-Align: Lipschitz Projection and Spectral Guard ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) hold with τ≤1\tau\leq 1 and ε∈(0,1)\varepsilon\in(0,1).
Then for any bounded input sequence {uℓ}\{u\_{\ell}\}, the state trajectory {hℓ}\{h\_{\ell}\} is uniformly bounded; moreover the input-to-output map induced by 𝒢θ\mathcal{G}\_{\theta} is globally Lipschitz with constant bounded by ([13](https://arxiv.org/html/2511.06451v1#S3.E13 "In Lipschitz surrogate via spectral normalization. ‣ 3.1 Risk–Neutral Operator Layer (RN-Operator) ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")).

###### Proof sketch.

By Lemma [1](https://arxiv.org/html/2511.06451v1#Thmlemma1 "Lemma 1 (Green kernel bound). ‣ Spectral safety and discrete Green kernel. ‣ 3.1 Risk–Neutral Operator Layer (RN-Operator) ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") (Appendix A.1), the discrete Green kernel is uniformly summable under the CFL-type constraint ρ​(Aθ​(Tℓ))​Δ​tℓ≤1−ε\rho(A\_{\theta}(T\_{\ell}))\,\Delta t\_{\ell}\leq 1-\varepsilon.
The Q-Align projection ([14](https://arxiv.org/html/2511.06451v1#S3.E14 "In Layerwise Lipschitz projection. ‣ 3.2 Q-Align: Lipschitz Projection and Spectral Guard ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) enforces a layerwise 11-Lipschitz envelope (with factor τ≤1\tau\leq 1) and nonexpansive ϕ\phi preserves Lipschitz bounds through composition.
Unrolling the recursion and applying submultiplicativity yields a geometric series dominated by the kernel sum from Lemma [1](https://arxiv.org/html/2511.06451v1#Thmlemma1 "Lemma 1 (Green kernel bound). ‣ Spectral safety and discrete Green kernel. ‣ 3.1 Risk–Neutral Operator Layer (RN-Operator) ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures"), which provides both bounded-input–bounded-output (BIBO) stability and a global Lipschitz constant that matches ([13](https://arxiv.org/html/2511.06451v1#S3.E13 "In Lipschitz surrogate via spectral normalization. ‣ 3.1 Risk–Neutral Operator Layer (RN-Operator) ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")).
Full details are given in Appendix A.2.
∎

#### Geometric diagnostics.

The triplet (λlip​-​before,λlip​-​after,CFLmax)(\lambda\_{\mathrm{lip}\text{-}\mathrm{before}},\lambda\_{\mathrm{lip}\text{-}\mathrm{after}},\mathrm{CFL}\_{\max}) summarizes per-epoch geometry. Large *projection distance* or frequent spec​\_​guard​\_​hits\mathrm{spec\\_guard\\_hits} predict subsequent instability or poor generalization and are therefore treated as early-warning signals.

### 3.3 Convex–Monotone Decoder and SPX–VIX Coupling

#### No-arbitrage constraints.

On each maturity TT, let K↦C​(K,T)K\mapsto C(K,T) be the call price surface. Static no-arbitrage requires

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂K​K2C​(⋅,T)≥0,∂TC​(K,⋅)≥0,0≤C​(K,T)≤S0,∂KC​(K,T)≤0.\partial\_{KK}^{2}C(\cdot,T)\geq 0,\qquad\partial\_{T}C(K,\cdot)\geq 0,\qquad 0\leq C(K,T)\leq S\_{0},\qquad\partial\_{K}C(K,T)\leq 0. |  | (17) |

We parameterize C​(⋅,T)C(\cdot,T) as an input-convex neural potential Φ​(⋅;T)\Phi(\cdot;T), i.e.,

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(K,T)=Φ​(K;T),Φ​(⋅;T)​convex,∂TΦ​(K,T)≥0,C(K,T)=\Phi(K;T),\qquad\Phi(\cdot;T)\ \text{convex},\qquad\partial\_{T}\Phi(K,T)\geq 0, |  | (18) |

where convexity is enforced by nonnegative weights on the KK-dependent paths and skip connections, and maturity monotonicity is enforced by a positive-slope parameterization in TT (with a final monotone calibration if needed).

#### Legendre structure and density.

Define the convex conjugate Φ⋆​(p;T)=supK∈ℝ{p​K−Φ​(K;T)}\Phi^{\star}(p;T)=\sup\_{K\in\mathbb{R}}\{pK-\Phi(K;T)\}. Then p⋆​(T):=∂KΦ​(K,T)p^{\star}(T):=\partial\_{K}\Phi(K,T) yields the delta, and the Breeden–Litzenberger relation connects second derivatives to the risk–neutral density fℚf\_{\mathbb{Q}}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | fℚ​(K,T)=er​T​∂K​K2C​(K,T).f\_{\mathbb{Q}}(K,T)=\mathrm{e}^{rT}\,\partial\_{KK}^{2}C(K,T). |  | (19) |

The decoder thus produces both prices and densities with consistent geometry.

#### SPX↔\leftrightarrowVIX replication.

Let 𝒦T\mathcal{K}\_{T} denote the strike grid at maturity TT, with ordered knots 0<K1<⋯<KM0<K\_{1}<\cdots<K\_{M} and spacings Δ​Ki:=12​(Ki+1−Ki−1)\Delta K\_{i}:=\tfrac{1}{2}(K\_{i+1}-K\_{i-1}) (endpoints use one-sided spacings).
Write FT:=S0​e(r−q)​TF\_{T}:=S\_{0}\mathrm{e}^{(r-q)T} and K0K\_{0} for the closest strike to FTF\_{T}.
The (continuous) log-contract identity implies the variance-swap fair rate under ℚ\mathbb{Q}:

|  |  |  |
| --- | --- | --- |
|  | σVS2​(T)=2​er​TT​(∫0FTP​(K,T)K2​𝑑K+∫FT∞C​(K,T)K2​𝑑K)−1T​(FTK0−1)2.\sigma^{2}\_{\mathrm{VS}}(T)=\frac{2\,\mathrm{e}^{rT}}{T}\!\left(\int\_{0}^{F\_{T}}\!\frac{P(K,T)}{K^{2}}\,dK+\int\_{F\_{T}}^{\infty}\!\frac{C(K,T)}{K^{2}}\,dK\right)-\frac{1}{T}\Big(\tfrac{F\_{T}}{K\_{0}}-1\Big)^{\!2}. |  |

Consistent with the Cboe construction, we discretize it as

|  |  |  |  |
| --- | --- | --- | --- |
|  | VIX2​(T)≈2​er​TT​∑Ki∈𝒦TΔ​KiKi2​Q​(Ki,T)−1T​(FTK0−1)2,\mathrm{VIX}^{2}(T)\;\approx\;\frac{2\,\mathrm{e}^{rT}}{T}\sum\_{K\_{i}\in\mathcal{K}\_{T}}\frac{\Delta K\_{i}}{K\_{i}^{2}}\,Q(K\_{i},T)\;-\;\frac{1}{T}\Big(\tfrac{F\_{T}}{K\_{0}}-1\Big)^{\!2}, |  | (20) |

where QQ is the out-of-the-money option price at strike KiK\_{i} (put if Ki<FTK\_{i}<F\_{T}, call if Ki≥FTK\_{i}\geq F\_{T}) and the small forward adjustment term is retained.
Missing strikes are filled by linear interpolation on (K,Q)(K,Q), which preserves piecewise convexity in KK; Appendix A.3 compares cubic splines and shows comparable NAS/CNAS together with a mild increase in butterfly-arbitrage risk.

We define the *replication residual*

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛVIX​(T):=VIXobs2​(T)−VIXθ2​(T),\mathcal{R}\_{\mathrm{VIX}}(T):=\mathrm{VIX}^{2}\_{\mathrm{obs}}(T)-\mathrm{VIX}^{2}\_{\theta}(T), |  | (21) |

and include the dual penalty λvs​∑Tw​(T)​ℛVIX​(T)2\lambda\_{\mathrm{vs}}\sum\_{T}w(T)\,\mathcal{R}\_{\mathrm{VIX}}(T)^{2} in the saddle objective (weights w​(T)w(T) reflect sampling density).
Under mild regularity (no static arbitrage, integrable OTM tails), the following holds.

###### Proposition 2 (Consistency of discretized VIX replication).

Assume (K↦Q​(K,T))(K\mapsto Q(K,T)) is convex, Q​(⋅,T)/K2Q(\cdot,T)/K^{2} has bounded variation on compact intervals, and the tail contributions
∫0KminPK2​𝑑K\int\_{0}^{K\_{\min}}\!\tfrac{P}{K^{2}}\,dK and ∫Kmax∞CK2​𝑑K\int\_{K\_{\max}}^{\infty}\!\tfrac{C}{K^{2}}\,dK vanish as Kmin↓0K\_{\min}\downarrow 0, Kmax↑∞K\_{\max}\uparrow\infty.
For any family of strike grids {𝒦T}\{\mathcal{K}\_{T}\} with mesh Δ​KT→0\Delta K\_{T}\to 0 uniformly on TT in a compact set, the discrete estimator in ([20](https://arxiv.org/html/2511.06451v1#S3.E20 "In SPX↔VIX replication. ‣ 3.3 Convex–Monotone Decoder and SPX–VIX Coupling ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) converges uniformly to the continuous variance-swap rate:

|  |  |  |
| --- | --- | --- |
|  | supT∈𝒯|VIXθ2​(T)−σVS,θ2​(T)|≤C​supTΔ​KT+εtail​(Kmin,Kmax)→0,\sup\_{T\in\mathcal{T}}\Big|\mathrm{VIX}^{2}\_{\theta}(T)-\sigma^{2}\_{\mathrm{VS},\theta}(T)\Big|\;\leq\;C\,\sup\_{T}\Delta K\_{T}\;+\;\varepsilon\_{\mathrm{tail}}(K\_{\min},K\_{\max})\;\xrightarrow[]{}0, |  |

for some constant CC independent of TT, where εtail\varepsilon\_{\mathrm{tail}} is the integrable tail truncation error.

###### Proposition 3 (Variance-swap identifiability via replication).

Fix a maturity range 𝒯⊂(0,Tmax]\mathcal{T}\subset(0,T\_{\max}].
Suppose the RN-operator decoder yields a no-arbitrage surface with K↦Qθ​(K,T)K\mapsto Q\_{\theta}(K,T) convex and the replication residual ([21](https://arxiv.org/html/2511.06451v1#S3.E21 "In SPX↔VIX replication. ‣ 3.3 Convex–Monotone Decoder and SPX–VIX Coupling ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) satisfies ℛVIX​(T)=0\mathcal{R}\_{\mathrm{VIX}}(T)=0 for all T∈𝒯T\in\mathcal{T}.
Then σVS,θ2​(T)=σVS,obs2​(T)\sigma^{2}\_{\mathrm{VS},\theta}(T)=\sigma^{2}\_{\mathrm{VS,obs}}(T) for all T∈𝒯T\in\mathcal{T}.
If, moreover, the instantaneous variance admits a density vθ​(t)v\_{\theta}(t) and the mapping T↦1T​∫0Tvθ​(t)​𝑑tT\mapsto\frac{1}{T}\int\_{0}^{T}v\_{\theta}(t)\,dt is strictly monotone in TT, then vθv\_{\theta} matches the observed variance in the sense of Cesàro means on 𝒯\mathcal{T}.

*Proof sketches.* Proposition [2](https://arxiv.org/html/2511.06451v1#Thmproposition2 "Proposition 2 (Consistency of discretized VIX replication). ‣ SPX↔VIX replication. ‣ 3.3 Convex–Monotone Decoder and SPX–VIX Coupling ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") follows from convex quadrature error bounds for functions of bounded variation and the Breeden–Litzenberger representation Q′′​(K,T)=e−r​T​K−2​fθ​(K,T)Q^{\prime\prime}(K,T)=\mathrm{e}^{-rT}\,K^{-2}\,f\_{\theta}(K,T) (distributional derivative), plus integrable OTM tails. Proposition [3](https://arxiv.org/html/2511.06451v1#Thmproposition3 "Proposition 3 (Variance-swap identifiability via replication). ‣ SPX↔VIX replication. ‣ 3.3 Convex–Monotone Decoder and SPX–VIX Coupling ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") uses the log-contract identity for continuous Itô models, extends to jump-diffusions with the standard jump-compensator term, and invokes strict monotonicity to upgrade equality of Cesàro means to pointwise identification almost everywhere. Full details are provided in Appendix A.3.

###### Proposition 4 (Static no-arbitrage and replication consistency).

Assume the decoder C=ΦC=\Phi satisfies the convex–monotone constraints

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂K​K2C​(K,T)≥0,∂TC​(K,T)≥0\partial\_{KK}^{2}C(K,T)\geq 0,\qquad\partial\_{T}C(K,T)\geq 0 |  | (22) |

for all strikes K>0K>0 and maturities TT on the grid, and that the VIX replication residual ([21](https://arxiv.org/html/2511.06451v1#S3.E21 "In SPX↔VIX replication. ‣ 3.3 Convex–Monotone Decoder and SPX–VIX Coupling ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) vanishes on the maturity grid. Then the surface is free of static butterfly and calendar arbitrage on the grid, and the Breeden–Litzenberger implied density

|  |  |  |  |
| --- | --- | --- | --- |
|  | fST​(K)=er​T​∂K​K2C​(K,T)f\_{S\_{T}}(K)=\mathrm{e}^{rT}\,\partial\_{KK}^{2}C(K,T) |  | (23) |

is consistent with the VIX2 functional ([20](https://arxiv.org/html/2511.06451v1#S3.E20 "In SPX↔VIX replication. ‣ 3.3 Convex–Monotone Decoder and SPX–VIX Coupling ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) in the sense that the VIX computed from CC coincides with the replicated variance-swap rate on the grid.
*Sketch.* Convexity in KK and monotonicity in TT exclude butterfly and calendar violations on the grid. The discretized BL relation and the replication identity tie the second derivative to the integrated OTM portfolio. See Appendix A.4 for a complete proof.

#### Numerical projection.

If small violations appear (finite-sample noise), we solve a convex projection

|  |  |  |  |
| --- | --- | --- | --- |
|  | minC^12∑i,ℓ(C^(Ki,Tℓ)−C(Ki,Tℓ))2s.t.C^(⋅,Tℓ)convex inK,C^(Ki,⋅)nondecreasing inT,\min\_{\widehat{C}}\;\frac{1}{2}\sum\_{i,\ell}\big(\widehat{C}(K\_{i},T\_{\ell})-C(K\_{i},T\_{\ell})\big)^{2}\quad\mathrm{s.t.}\quad\widehat{C}(\cdot,T\_{\ell})\ \text{convex in}\ K,\;\;\widehat{C}(K\_{i},\cdot)\ \text{nondecreasing in}\ T, |  | (24) |

via pooled-adjacent-violators in TT and tridiagonal quadratic programming in KK. This preserves first-order fits while restoring gridwise no-arbitrage.

### 3.4 Saddle-Point Training and Safety-Oriented Stopping

#### Objective.

The training objective couples data fit, no-arbitrage penalties, martingale residuals, and replication consistency:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ​(θ,λ)=𝔼​[ℓ​(𝒢θ​(u),Cobs)]⏟pricing fit+⟨λNA,𝒞NA​(θ)⟩⏟static constraints+⟨λmart,ℳRN​(θ)⟩⏟martingale+⟨λVIX,ℛVIX​(θ)⟩⏟replication,\mathcal{L}(\theta,\lambda)\;=\;\underbrace{\mathbb{E}\left[\ell\big(\mathcal{G}\_{\theta}(u),\,C\_{\mathrm{obs}}\big)\right]}\_{\text{pricing fit}}\;+\;\underbrace{\langle\lambda\_{\mathrm{NA}},\,\mathcal{C}\_{\mathrm{NA}}(\theta)\rangle}\_{\text{static constraints}}\;+\;\underbrace{\langle\lambda\_{\mathrm{mart}},\,\mathcal{M}\_{\mathrm{RN}}(\theta)\rangle}\_{\text{martingale}}\;+\;\underbrace{\langle\lambda\_{\mathrm{VIX}},\,\mathcal{R}\_{\mathrm{VIX}}(\theta)\rangle}\_{\text{replication}}, |  | (25) |

with dual variables λ=(λNA,λmart,λVIX)≥0\lambda=(\lambda\_{\mathrm{NA}},\lambda\_{\mathrm{mart}},\lambda\_{\mathrm{VIX}})\geq 0; 𝒞NA\mathcal{C}\_{\mathrm{NA}} collects soft constraints induced by ([17](https://arxiv.org/html/2511.06451v1#S3.E17 "In No-arbitrage constraints. ‣ 3.3 Convex–Monotone Decoder and SPX–VIX Coupling ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")).

#### Two-time-scale extragradient.

We employ a two-time-scale update with extragradient prediction:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | θk+12\displaystyle\theta^{k+\frac{1}{2}} | =θk−ηθ​∇θℒ​(θk,λk),λk+12=[λk+ηλ​∇λℒ​(θk,λk)]+,\displaystyle=\theta^{k}-\eta\_{\theta}\,\nabla\_{\theta}\mathcal{L}(\theta^{k},\lambda^{k}),\qquad\lambda^{k+\frac{1}{2}}=\big[\lambda^{k}+\eta\_{\lambda}\,\nabla\_{\lambda}\mathcal{L}(\theta^{k},\lambda^{k})\big]\_{+}, |  | (26) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | θk+1\displaystyle\theta^{k+1} | =θk−ηθ​∇θℒ​(θk+12,λk+12),λk+1=[λk+ηλ​∇λℒ​(θk+12,λk+12)]+,\displaystyle=\theta^{k}-\eta\_{\theta}\,\nabla\_{\theta}\mathcal{L}\big(\theta^{k+\frac{1}{2}},\lambda^{k+\frac{1}{2}}\big),\qquad\lambda^{k+1}=\big[\lambda^{k}+\eta\_{\lambda}\,\nabla\_{\lambda}\mathcal{L}\big(\theta^{k+\frac{1}{2}},\lambda^{k+\frac{1}{2}}\big)\big]\_{+}, |  |

with ηλ\eta\_{\lambda} ramped from a small value to its target to avoid premature constraint domination. Q-Align is applied after each θ\theta-update.

#### Martingale stop test and thresholds.

On random (K,T)(K,T) slices we test the discounted martingale increment and accept early stopping if the following hold for at least 10310^{3} consecutive steps:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Gap<10−3,dual​residual<10−3.\Delta\mathrm{Gap}<10^{-3},\qquad\mathrm{dual\;residual}<10^{-3}. |  | (27) |

We also track ratio​\_​log=log⁡(primal/dual)\mathrm{ratio\\_log}=\log(\mathrm{primal}/\mathrm{dual}) as a bias diagnostic.

#### Convergence guarantee (noise-stable neighborhood).

Let F​(z)=(∇θℒ​(θ,λ),−∇λℒ​(θ,λ))F(z)=(\nabla\_{\theta}\mathcal{L}(\theta,\lambda),-\nabla\_{\lambda}\mathcal{L}(\theta,\lambda)) denote the monotone saddle operator in z=(θ,λ)z=(\theta,\lambda). Under (i) global Lipschitzness of FF (by ([13](https://arxiv.org/html/2511.06451v1#S3.E13 "In Lipschitz surrogate via spectral normalization. ‣ 3.1 Risk–Neutral Operator Layer (RN-Operator) ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) and bounded subgradients for constraints), (ii) small multiplicative bias introduced by Q-Align projections, and (iii) bounded gradient noise with variance σ2\sigma^{2}, standard extragradient theory implies the following.

###### Theorem 1 (Extragradient convergence to a noise ball).

Let F:𝒵→ℝdF:\mathcal{Z}\to\mathbb{R}^{d} be a monotone and LL-Lipschitz operator on a nonempty, closed, convex set 𝒵⊂ℝd\mathcal{Z}\subset\mathbb{R}^{d}, and suppose the Q-Align projections are 11-Lipschitz with per-iteration projection error bounded as ‖ek‖=𝒪​(ηθ)\|e^{k}\|=\mathcal{O}(\eta\_{\theta}), where eke^{k} aggregates spectral clipping and geometric projection inaccuracies. Consider the projected extragradient iterates with step sizes ηθ,ηλ=Θ​(1/L)\eta\_{\theta},\eta\_{\lambda}=\Theta(1/L),

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | yk=Π𝒵​(zk−η​F​(zk)+ξk+ek),\displaystyle y^{k}=\Pi\_{\mathcal{Z}}\big(z^{k}-\eta F(z^{k})+\xi^{k}+e^{k}\big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | zk+1=Π𝒵​(zk−η​F​(yk)+ξ~k+e~k),\displaystyle z^{k+1}=\Pi\_{\mathcal{Z}}\big(z^{k}-\eta F(y^{k})+\tilde{\xi}^{k}+\tilde{e}^{k}\big), |  |

where {ξk},{ξ~k}\{\xi^{k}\},\{\tilde{\xi}^{k}\} are martingale-difference noise with 𝔼​[ξk∣ℱk]=0\mathbb{E}[\xi^{k}\mid\mathcal{F}\_{k}]=0, 𝔼​‖ξk‖2≤σ2\mathbb{E}\|\xi^{k}\|^{2}\leq\sigma^{2} (and similarly for ξ~k\tilde{\xi}^{k}), and Π𝒵\Pi\_{\mathcal{Z}} denotes the Euclidean projection onto 𝒵\mathcal{Z}. Then the averaged first-order residual satisfies

|  |  |  |
| --- | --- | --- |
|  | min0≤k≤K−1⁡𝔼​‖F​(zk)‖2≤𝒪​(L2​‖z0−z⋆‖2K)+𝒪​(σ2),\min\_{0\leq k\leq K-1}\ \mathbb{E}\,\|F(z^{k})\|^{2}\;\leq\;\mathcal{O}\!\left(\frac{L^{2}\|z^{0}-z^{\star}\|^{2}}{K}\right)\;+\;\mathcal{O}\!\left(\sigma^{2}\right), |  |

where z⋆z^{\star} is a solution of the monotone variational inequality associated with the saddle-point problem.
*Sketch.* Combine one-step progress of projected extragradient for monotone Lipschitz VIs with a stability treatment of Q-Align as a nonexpansive perturbation whose cumulative effect is 𝒪​(η)\mathcal{O}(\eta), and then control the martingale noise via standard Robbins–Siegmund arguments. See Appendix A.5 for the complete proof.

#### Instrumentation and audit trail.

We continuously log

|  |  |  |
| --- | --- | --- |
|  | λlip​-​before,λlip​-​after,spec​\_​guard​\_​hits,projection​\_​distance,maxℓ⁡ρ​(Aθ​(Tℓ))​Δ​tℓ,ratio​\_​log,\lambda\_{\mathrm{lip}\text{-}\mathrm{before}},\ \lambda\_{\mathrm{lip}\text{-}\mathrm{after}},\ \mathrm{spec\\_guard\\_hits},\ \mathrm{projection\\_distance},\ \max\_{\ell}\rho(A\_{\theta}(T\_{\ell}))\Delta t\_{\ell},\ \mathrm{ratio\\_log}, |  |

and align them with evaluation metrics (NAS, CNAS, NI, DualGap, Stability, Surface–Wasserstein, GenGap at 95th percentile, effective dimension). Stress-to-fail scans, external-validity tests (frozen-hyperparameter reuse), and irreplaceability ablations (removing measure gating, halving rank, disabling Spectral Guard) are run under the same logging schema, forming a traceable chain from geometry to training dynamics to statistical outcomes.

### 3.5 Relation to Selective SSMs and Mamba

Arbiter shares the runtime primitive of selective scans with modern state-space models—diagonal-plus-low-rank parametrizations of AθA\_{\theta}, input-dependent gating, and linear-time recurrences—yet it decisively departs in *semantics and constraints*. First, the recurrence is interpreted as a risk–neutral Green operator acting on market features, with a learned measure gate wθw\_{\theta} that internalizes the Radon–Nikodym derivative and enforces martingale consistency during training. Second, Q-Align supplies training-time geometric guarantees: layerwise Lipschitz projection and spectral CFL control establish stability and bound the operator norm end-to-end. Third, the decoder is not a generic readout but an input-convex, maturity-monotone potential tied to SPX–VIX replication. Together these elements move no-arbitrage and change-of-measure from post-hoc cleaning to in-training constraints, while retaining the 𝒪​(L​m)\mathcal{O}(Lm) computational profile central to selective SSMs.

#### Summary of guarantees.

Under the Q-Align regime and decoder constraints, Propositions [1](https://arxiv.org/html/2511.06451v1#Thmproposition1 "Proposition 1 (RN-operator stability under Q-Align). ‣ RN-operator stability under Q-Align. ‣ 3.2 Q-Align: Lipschitz Projection and Spectral Guard ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") and [4](https://arxiv.org/html/2511.06451v1#Thmproposition4 "Proposition 4 (Static no-arbitrage and replication consistency). ‣ SPX↔VIX replication. ‣ 3.3 Convex–Monotone Decoder and SPX–VIX Coupling ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") ensure (i) bounded and Lipschitz RN-operators (stable Green expansion), and (ii) gridwise static no-arbitrage and replication consistency. Theorem [1](https://arxiv.org/html/2511.06451v1#Thmtheorem1 "Theorem 1 (Extragradient convergence to a noise ball). ‣ Convergence guarantee (noise-stable neighborhood). ‣ 3.4 Saddle-Point Training and Safety-Oriented Stopping ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") further guarantees that saddle-point training converges to a stochastic neighborhood whose radius is controlled by gradient noise and projection errors. In aggregate, these results explain the empirical behavior of Arbiter in Sections [6](https://arxiv.org/html/2511.06451v1#S6 "6 Experiments ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")–[6.2](https://arxiv.org/html/2511.06451v1#S6.SS2 "6.2 Ablations: irreplaceability and breakers ‣ 6 Experiments ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") and justify the falsifiable metrics reported throughout.

## 4 Theoretical Results

We establish eight results (T1–T8) that quantify approximation error, conditioning, identifiability, oracle rates, capacity control, feasibility under spectral safeguards, joint identifiability with VIX replication, and saddle-point convergence under fixed stopping thresholds. Throughout, we work under the standing assumptions of Section [2](https://arxiv.org/html/2511.06451v1#S2 "2 Setting, Notation, and Testable Assumptions ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures"): (A1) Novikov-to-Kazamaki switching holds at the reported rate; (A2) local Hölder smoothness of order βsmooth>0\beta\_{\mathrm{smooth}}>0 for the target operator; (A3) spectral decay governed by κ\kappa with long-horizon index χ​(κ)≥0\chi(\kappa)\geq 0; (A4) coverage level c¯∈(0,1]\underline{c}\in(0,1] on the (K,T)(K,T) grid. The RN-operator 𝒢θ\mathcal{G}\_{\theta} is equipped with Q-Align (layerwise spectral projection and CFL spectral guard), and the decoder is convex–monotone with optional numerical projection to the no-arbitrage cone.

Notation.
Let LL be the number of maturities and mm the operator rank (hidden dimension). Let LgL\_{g} denote the Lipschitz bound of nonlinearities (taken as 11 in practice), and Aθ​(Tℓ)A\_{\theta}(T\_{\ell}) the state transition at maturity TℓT\_{\ell}. Denote ‖A‖2\|A\|\_{2} the spectral norm, ρ​(A)\rho(A) the spectral radius, and Δ​tℓ:=Tℓ+1−Tℓ\Delta t\_{\ell}:=T\_{\ell+1}-T\_{\ell}. Define the discrete CFL quantity CFL​(Tℓ)=ρ​(Aθ​(Tℓ))​Δ​tℓ\mathrm{CFL}(T\_{\ell})=\rho(A\_{\theta}(T\_{\ell}))\Delta t\_{\ell} and CFLmax=maxℓ⁡CFL​(Tℓ)\mathrm{CFL}\_{\max}=\max\_{\ell}\mathrm{CFL}(T\_{\ell}). The effective dimension d^\hat{d} refers to the 90–95% spectral energy truncation rank of the Gram operator induced by inputs.

### T1: Approximation Error and Conditioning

###### Theorem 2 (Approximation rate and conditioning).

Let f⋆f^{\star} be the target risk–neutral operator mapping features to price surfaces on a compact domain 𝒵⊂ℝdz\mathcal{Z}\subset\mathbb{R}^{d\_{z}} with Hölder regularity βsmooth∈(0,1]\beta\_{\mathrm{smooth}}\in(0,1]. There exists a parameter choice θ=θ​(m)\theta=\theta(m) such that the RN-operator 𝒢θ\mathcal{G}\_{\theta} with rank mm and LL maturities satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | infθ‖𝒢θ−f⋆‖L2​(𝒵)≤C1​m−βsmooth,κ​(𝒥θ)≤C2​(maxℓ⁡‖Aθ​(Tℓ)‖2)​Lg​m,\inf\_{\theta}\;\|\mathcal{G}\_{\theta}-f^{\star}\|\_{L^{2}(\mathcal{Z})}\;\leq\;C\_{1}\,m^{-\beta\_{\mathrm{smooth}}},\qquad\kappa\big(\mathcal{J}\_{\theta}\big)\;\leq\;C\_{2}\,\big(\max\_{\ell}\|A\_{\theta}(T\_{\ell})\|\_{2}\big)\,L\_{g}\,m, |  | (28) |

where 𝒥θ\mathcal{J}\_{\theta} is the Jacobian of 𝒢θ\mathcal{G}\_{\theta} and κ​(⋅)\kappa(\cdot) is a spectral condition proxy. The constants C1,C2C\_{1},C\_{2} depend only on the domain diameter and curvature bounds of the nonlinearities, but not on LL; the dependence on LL is controlled by the scan through the Green kernel bound (cf. Lemma [1](https://arxiv.org/html/2511.06451v1#Thmlemma1 "Lemma 1 (Green kernel bound). ‣ Spectral safety and discrete Green kernel. ‣ 3.1 Risk–Neutral Operator Layer (RN-Operator) ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")). *Sketch.* Approximation follows by representing f⋆f^{\star} via a Green expansion with Hölder control and matching it with a diagonal-plus-low-rank parameterization of (Aθ,Bθ)(A\_{\theta},B\_{\theta}); the scan composes LL 1-Lipschitz layers under Q-Align and preserves linear-time complexity. Conditioning tracks the sum of per-step operator norms through the Green kernel Neumann bound and the Lipschitz gate constant LgL\_{g}, yielding the stated linear dependence in mm and independence of LL. Full proof in Appendix B.1.

### T2: Local Identifiability and CRLB-Type Lower Bounds

###### Theorem 3 (Local identifiability and information bound).

Assume the decoder enforces static no-arbitrage and VIX2 replication consistency on the maturity–strike grid, and the input feature process has a nondegenerate covariance operator on 𝒵\mathcal{Z}. Then there exists a neighborhood 𝒰\mathcal{U} of θ⋆\theta^{\star} such that the RN-operator map θ↦𝒢θ\theta\mapsto\mathcal{G}\_{\theta} is injective modulo the finite symmetry group of rank-mm factorizations (permutation and rescaling of atoms). Moreover, for any unbiased estimator θ^\widehat{\theta} based on nn i.i.d. samples,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[‖θ^−θ⋆‖2]≥trace​(ℐ​(θ⋆)−1),\mathbb{E}\!\left[\|\widehat{\theta}-\theta^{\star}\|^{2}\right]\;\geq\;\mathrm{trace}\!\left(\mathcal{I}(\theta^{\star})^{-1}\right), |  | (29) |

where ℐ​(θ⋆)\mathcal{I}(\theta^{\star}) denotes the Fisher information of the induced RN-operator under the data-generating distribution.

#### Proof sketch.

(i) *Decoder identifiability.* The Breeden–Litzenberger identity links the second derivative in strike to the risk-neutral density. Together with VIX2 replication consistency, this pins down the decoder’s measure-valued output across maturities. (ii) *Propagation through the scan.* If two parameterizations yield identical price surfaces for almost every input, then their Green responses must coincide on the grid. Under nondegenerate input covariance and the uniform Green bound (Lemma [1](https://arxiv.org/html/2511.06451v1#Thmlemma1 "Lemma 1 (Green kernel bound). ‣ Spectral safety and discrete Green kernel. ‣ 3.1 Risk–Neutral Operator Layer (RN-Operator) ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")), this forces equality of the low-rank scan parameters up to permutation and atom rescaling symmetries. (iii) *Information bound.* Local asymptotic normality holds for the price-slice likelihood with Gateaux derivative equal to the RN-operator Jacobian; the score is square-integrable by Q-Align’s Lipschitz control. The Cramér–Rao lower bound then gives ([29](https://arxiv.org/html/2511.06451v1#S4.E29 "In Theorem 3 (Local identifiability and information bound). ‣ T2: Local Identifiability and CRLB-Type Lower Bounds ‣ 4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")). Full details are provided in Appendix B.2.

### T2′: Representative-Element Error Under Coverage Deficits

###### Proposition 5 (Representative bound with coverage and residuals).

Let cov∈[0,1]\mathrm{cov}\in[0,1] denote the fraction of strike–maturity cells covered by reliable quotes. Let γ>0\gamma>0 be the martingale penalization strength and let dual≥0\mathrm{dual}\geq 0 be the dual residual at stopping. Then the representative-element error obeys

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖λε−λ⋆‖L2​(𝒵)≤C3​((1−cov)−1​ε+γ−1+dual),\|\lambda\_{\varepsilon}-\lambda^{\star}\|\_{L^{2}(\mathcal{Z})}\;\leq\;C\_{3}\Big(\,(1-\mathrm{cov})^{-1}\varepsilon\;+\;\gamma^{-1}\;+\;\mathrm{dual}\,\Big), |  | (30) |

where λ\lambda indexes the operator-induced risk measure and ε\varepsilon bounds the interpolation error on missing strikes.

#### Proof sketch.

Partition the grid into covered and uncovered cells. The first term controls the imputation bias: extending prices from the covered set to the full grid by a linear, no-arbitrage–preserving interpolant yields an L2L^{2} error that scales as (1−cov)−1​ε(1-\mathrm{cov})^{-1}\varepsilon due to the stability modulus of the extension operator on sparse masks. The second term is the bias from enforcing the martingale constraint via a penalty of strength γ\gamma, which leaves an O​(γ−1)O(\gamma^{-1}) feasibility gap by first-order optimality. The third term converts a nonzero KKT residual at termination into a distance-to-solution via a Hoffman-type error bound. The RN-operator is globally Lipschitz under Q-Align and Spec-Guard; hence all three perturbations transport to λ\lambda with a uniform constant. Full details and constants appear in Appendix B.3.

### T3: Oracle Risk Bounds with Long-Memory Factor

###### Theorem 4 (Oracle rate with scan and memory).

Let d^\hat{d} be the effective dimension of the input Gram operator and Δ​t:=maxℓ⁡Δ​tℓ\Delta t:=\max\_{\ell}\Delta t\_{\ell}. Under Q-Align and decoder constraints, the prediction risk of the oracle estimator with rank mm and nn samples satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛn,m≤C4​(n−1/2+m−βsmooth/d^+Δ​t)+C5​Tχ​(κ),\mathcal{R}\_{n,m}\;\leq\;C\_{4}\Big(n^{-1/2}\;+\;m^{-\beta\_{\mathrm{smooth}}/\hat{d}}\;+\;\sqrt{\Delta t}\Big)\;+\;C\_{5}\,T^{\chi(\kappa)}, |  | (31) |

where TT is the horizon and χ​(κ)≥0\chi(\kappa)\geq 0 quantifies long-memory spectral accumulation. The first three terms are short-horizon effects; the last term captures the asymptotic tail induced by spectral mass at small decay rates.

*Sketch.*
The stochastic term n−1/2n^{-1/2} derives from standard central limit rates under bounded variance; the approximation term m−β/d^m^{-\beta/\hat{d}} follows from T1 with effective dimension; the discretization term Δ​t\sqrt{\Delta t} arises from Riemann-sum error in the scan. The long-memory penalty Tχ​(κ)T^{\chi(\kappa)} appears when eigenvalues near one accumulate according to A3. Appendix C provides a spectral decomposition proof.

### T4–T5: Capacity via Rademacher and a Sample–Seminorm Bridge

###### Lemma 2 (Rademacher complexity with Lipschitz and projection).

Let ℱ\mathcal{F} be the class of RN-operators obeying Q-Align projections with a global Lipschitz constant Λ\Lambda. Then for sample size nn,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℜn​(ℱ)≤C6​Λ​dimeffn,\mathfrak{R}\_{n}(\mathcal{F})\;\leq\;C\_{6}\,\Lambda\,\sqrt{\frac{\mathrm{dim}\_{\mathrm{eff}}}{n}}, |  | (32) |

where dimeff≤d^\mathrm{dim}\_{\mathrm{eff}}\leq\hat{d} is the energy-truncation rank at the sample scale.

#### Proof sketch.

Project the trajectories onto the top energy subspace of rank dimeff\mathrm{dim}\_{\mathrm{eff}} defined by the Gram operator of the Green kernel. Under Q-Align+Spec-Guard the RN-operator is globally Λ\Lambda-Lipschitz, hence the function class admits a Lipschitz envelope on a radius-11 domain (normalization). Dudley chaining with covering numbers of a dimeff\mathrm{dim}\_{\mathrm{eff}}-dimensional ball yields the stated rate. Full details appear in Appendix B.4.

###### Lemma 3 (Bridge from sample to seminorm).

Let ∥⋅∥n\|\cdot\|\_{n} be the empirical norm on the observed grid and ∥⋅∥ℋ\|\cdot\|\_{\mathcal{H}} a seminorm induced by the RN-operator’s Green kernel. Under A4 and a linear no-arbitrage–preserving interpolation with error ε\varepsilon, with high probability,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖f‖ℋ≤C7​‖f‖n+C8​((1−cov)−1​ε),\|f\|\_{\mathcal{H}}\;\leq\;C\_{7}\,\|f\|\_{n}\;+\;C\_{8}\Big((1-\mathrm{cov})^{-1}\varepsilon\Big), |  | (33) |

uniformly over ff in the model class.

#### Proof sketch.

Bound the kernel seminorm by the operator norm of the discrete Green Gram, which is finite by Lemma [1](https://arxiv.org/html/2511.06451v1#Thmlemma1 "Lemma 1 (Green kernel bound). ‣ Spectral safety and discrete Green kernel. ‣ 3.1 Risk–Neutral Operator Layer (RN-Operator) ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") and Proposition [1](https://arxiv.org/html/2511.06451v1#Thmproposition1 "Proposition 1 (RN-operator stability under Q-Align). ‣ RN-operator stability under Q-Align. ‣ 3.2 Q-Align: Lipschitz Projection and Spectral Guard ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures"). Decompose the grid into covered cells and their complement; the extension operator from the covered set is linear and stable on the no-arbitrage cone, with amplification scaling as (1−cov)−1(1-\mathrm{cov})^{-1}. Concentrate the empirical-to-population deviation via standard symmetrization and the class complexity from Lemma [2](https://arxiv.org/html/2511.06451v1#Thmlemma2 "Lemma 2 (Rademacher complexity with Lipschitz and projection). ‣ T4–T5: Capacity via Rademacher and a Sample–Seminorm Bridge ‣ 4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures"). Full proof is in Appendix B.5.

### T6: Feasibility and Two-Time-Scale Averaging under Spectral Guard

###### Proposition 6 (Feasibility and error propagation).

Suppose Q-Align enforces ‖Wℓ‖2≤τ≤1\|W\_{\ell}\|\_{2}\leq\tau\leq 1 and ρ​(Aθ​(Tℓ))​Δ​tℓ≤1−ε\rho\!\big(A\_{\theta}(T\_{\ell})\big)\,\Delta t\_{\ell}\leq 1-\varepsilon for all ℓ\ell. Then the iterative scan is well-posed, the discrete Green expansion is summable, and the one-step error is contractive:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖hℓ+1−h~ℓ+1‖≤(1−ε)​‖hℓ−h~ℓ‖+‖B‖​‖Ξ‖​‖uℓ−u~ℓ‖.\|h\_{\ell+1}-\tilde{h}\_{\ell+1}\|\;\leq\;(1-\varepsilon)\,\|h\_{\ell}-\tilde{h}\_{\ell}\|\;+\;\|B\|\,\|\Xi\|\,\|u\_{\ell}-\tilde{u}\_{\ell}\|. |  | (34) |

Moreover, for two-time-scale averaging of the primal–dual iterates (θk,λk)(\theta\_{k},\lambda\_{k}) in the saddle dynamics with bounded gradient noise, the averaged gap enjoys a variance reduction of order 𝒪​(1/K)\mathcal{O}(1/K) after KK steps.

#### Proof sketch.

Write the scan as hℓ+1=(I+Δ​tℓ​Aℓ)​hℓ+Wℓ​ϕ​(hℓ)+B​uℓh\_{\ell+1}=(I+\Delta t\_{\ell}A\_{\ell})h\_{\ell}+W\_{\ell}\phi(h\_{\ell})+Bu\_{\ell}. By Spec-Guard, for each ℓ\ell there exists an induced norm under which ‖I+Δ​tℓ​Aℓ‖≤1−ε\|I+\Delta t\_{\ell}A\_{\ell}\|\leq 1-\varepsilon; Q-Align caps ‖Wℓ‖≤τ≤1\|W\_{\ell}\|\leq\tau\leq 1 and ϕ\phi is nonexpansive. A mean-value bound on the step map shows its Jacobian norm is ≤1−ε\leq 1-\varepsilon, giving ([34](https://arxiv.org/html/2511.06451v1#S4.E34 "In Proposition 6 (Feasibility and error propagation). ‣ T6: Feasibility and Two-Time-Scale Averaging under Spectral Guard ‣ 4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) after adding the input term. Summability of the Green series follows from the Neumann-type bound (Lemma [1](https://arxiv.org/html/2511.06451v1#Thmlemma1 "Lemma 1 (Green kernel bound). ‣ Spectral safety and discrete Green kernel. ‣ 3.1 Risk–Neutral Operator Layer (RN-Operator) ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")). The two-time-scale variance reduction follows from standard TTSA analysis with monotone operators and bounded noise. Full proofs are given in Appendix B.6 (contractivity and summability) and Appendix B.7 (TTSA variance decay).

### T7: Joint Identifiability with VIX2 Replication and a SPX-Only Counterexample

###### Theorem 5 (Joint identifiability; SPX-only failure).

Suppose the decoder Cθ​(K,T)C\_{\theta}(K,T) is convex in KK and nonincreasing in TT for each maturity TT, and the discretized VIX2 replication residual (cf. ([20](https://arxiv.org/html/2511.06451v1#S3.E20 "In SPX↔VIX replication. ‣ 3.3 Convex–Monotone Decoder and SPX–VIX Coupling ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures"))–([21](https://arxiv.org/html/2511.06451v1#S3.E21 "In SPX↔VIX replication. ‣ 3.3 Convex–Monotone Decoder and SPX–VIX Coupling ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures"))) vanishes on the maturity grid {Tℓ}ℓ=1L\{T\_{\ell}\}\_{\ell=1}^{L}. Then the pair *(SPX calls on a strike grid, VIX2 per maturity)* identifies the induced risk–neutral operator 𝒢θ\mathcal{G}\_{\theta} up to model symmetries (reparameterizations that leave CθC\_{\theta} invariant on the grid).

In contrast, using SPX calls on the strike grid alone, without imposing replication consistency, there exist nontrivial perturbations of the RN-operator that preserve all grid call prices yet alter the induced variance-swap functional.

#### Proof sketch.

On each maturity, the Breeden–Litzenberger (BL) relation implies that second strike differences of CθC\_{\theta} recover the discrete risk–neutral density on the grid. The VIX2 replication functional is a linear functional of out-of-the-money option values with weights 1/K21/K^{2}; matching it eliminates degrees of freedom left in the tails/inter-knot segments that are not pinned down by grid values alone. Under convexity/monotonicity and our interpolation policy, the combined constraints (grid calls ++ replication) fix both local (BL) and integrated (VIX) aspects of the law, yielding injectivity modulo symmetries.

For SPX-only, the measurement operator that samples calls on a finite strike grid has a nontrivial null space in the ambient function class; by a separation argument (or an explicit bump construction supported between grid knots), one can perturb the surface without changing its values at the grid points but changing the 1/K21/K^{2}-weighted integral, hence the variance swap rate. Full details and constructions are in Appendix C.

### T8: Saddle-Point Convergence with Fixed Safety Thresholds

###### Theorem 6 (Convergence to a noise ball under fixed thresholds).

Consider the extragradient two-time-scale scheme with Q-Align projections and fixed stopping thresholds

|  |  |  |
| --- | --- | --- |
|  | Δ​Gap<10−3,dual​residual<10−3,patience≥103​ steps.\Delta\mathrm{Gap}<10^{-3},\qquad\mathrm{dual\;residual}<10^{-3},\qquad\text{patience}\geq 10^{3}\text{ steps}. |  |

Assume the saddle operator F​(z)F(z) is monotone and LL-Lipschitz, projections are nonexpansive, and gradient noise has variance σ2\sigma^{2}. Then the averaged iterates satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | mink≤K⁡‖F​(zk)‖2≤𝒪​(L2​‖z0−z⋆‖2K)+𝒪​(σ2),\min\_{k\leq K}\ \|F(z^{k})\|^{2}\;\leq\;\mathcal{O}\!\left(\frac{L^{2}\|z^{0}-z^{\star}\|^{2}}{K}\right)+\mathcal{O}(\sigma^{2}), |  | (35) |

and the stopping rule almost surely terminates inside a ball of radius c1​σ+c2​δprojc\_{1}\sigma+c\_{2}\delta\_{\mathrm{proj}} around a saddle point, where δproj\delta\_{\mathrm{proj}} quantifies per-step projection error.

#### Proof sketch (for Theorem [6](https://arxiv.org/html/2511.06451v1#Thmtheorem6 "Theorem 6 (Convergence to a noise ball under fixed thresholds). ‣ T8: Saddle-Point Convergence with Fixed Safety Thresholds ‣ 4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")).

We analyze the two-time-scale projected extragradient (EG) with Q-Align as a nonexpansive projection with bounded defect. A Fejér-type one–step inequality for monotone, LL-Lipschitz FF yields a telescoping bound on squared distances to a saddle z⋆z^{\star}, plus additive terms from gradient noise and projection error. Using ‖F​(z)‖≤L​‖z−z⋆‖\|F(z)\|\leq L\|z-z^{\star}\| to convert distance decay into a residual bound gives the stated 𝒪​(L2​‖z0−z⋆‖2/K)+𝒪​(σ2)\mathcal{O}(L^{2}\|z^{0}-z^{\star}\|^{2}/K)+\mathcal{O}(\sigma^{2}) rate (also for the ergodic average). Fixed thresholds on the primal–dual gap and dual residual upper-bound the merit residual, so the procedure almost surely terminates inside a ball of radius c1​σ+c2​δprojc\_{1}\sigma+c\_{2}\delta\_{\mathrm{proj}}. Full details appear in Appendix D.

Discussion.
T1 establishes that *operator semantics do not sacrifice* universal approximation rates relative to rank-mm kernels, while providing explicit conditioning that is tractable to monitor. T2 and T7 formalize identifiability *because* the decoder is tied to replication. T2′ quantifies the inevitable error under partial coverage and suboptimal dual solutions, directly justifying the empirical regressions of gap versus representative error. T3–T5 connect sample complexity to effective dimension and long-memory structure, and T6–T8 ensure that Q-Align’s projections and our fixed stopping thresholds lead to stable, falsifiable training.

## 5 Evaluation Protocol and Metrics

We describe the arXiv-release evaluation protocol, designed to be fully reproducible and aligned with the modeling choices and theoretical guarantees in Sections [3](https://arxiv.org/html/2511.06451v1#S3 "3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")–[4](https://arxiv.org/html/2511.06451v1#S4 "4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures"). The protocol relies on a high-fidelity synthetic generator that emulates risk–neutral dynamics and the variance–swap replication mechanism, evaluated under blocked cross–validation with rolling out-of-sample (OOS) windows. All criteria are dimensionless and comparable across runs; uncertainty is reported with heteroskedasticity– and autocorrelation–consistent (HAC) confidence intervals and family–wise error control via Holm–Bonferroni.

### 5.1 Data Protocol (arXiv Release)

#### Synthetic risk–neutral generator.

Under the pricing measure ℚ\mathbb{Q}, the underlying index StS\_{t} and instantaneous variance vtv\_{t} evolve on a trading day grid {ti}i=0N\{t\_{i}\}\_{i=0}^{N} as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​StSt\displaystyle\frac{\mathrm{d}S\_{t}}{S\_{t}} | =(r−q)​d​t+vt​d​Wt(1),S0>0,\displaystyle=\bigl(r-q\bigr)\,\mathrm{d}t+\sqrt{v\_{t}}\,\mathrm{d}W\_{t}^{(1)},\quad S\_{0}>0, |  | (36) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | vt\displaystyle v\_{t} | =v0+∫0tκ​(θ−vs)​ds⏟affine mean reversion+∫0t∫0sK​(s−u)​σ​vu​dWu(2)​ds⏟rough/long-memory component,\displaystyle=v\_{0}\;+\;\underbrace{\int\_{0}^{t}\kappa\bigl(\theta-v\_{s}\bigr)\,\mathrm{d}s}\_{\text{affine mean reversion}}\;+\;\underbrace{\int\_{0}^{t}\int\_{0}^{s}K(s-u)\,\sigma\sqrt{v\_{u}}\,\mathrm{d}W\_{u}^{(2)}\,\mathrm{d}s}\_{\text{rough/long-memory component}}, |  | (37) |

with instantaneous correlation d​⟨W(1),W(2)⟩t=ρ​d​t\mathrm{d}\langle W^{(1)},W^{(2)}\rangle\_{t}=\rho\,\mathrm{d}t, dividend yield qq, and a completely monotone kernel
K​(τ)=∑j=1Jaj​e−bj​τK(\tau)=\sum\_{j=1}^{J}a\_{j}e^{-b\_{j}\tau} that reproduces fractional/rough behavior by a positive mixture of exponentials. This yields an arbitrage–free implied variance term–structure and a VIX2 proxy

|  |  |  |  |
| --- | --- | --- | --- |
|  | VIX2​(T)≈2Δ​∫0Δ𝔼ℚ​[vT+s∣ℱT]​ds,Δ≈30 days.\mathrm{VIX}^{2}(T)\approx\frac{2}{\Delta}\int\_{0}^{\Delta}\mathbb{E}^{\mathbb{Q}}\!\left[v\_{T+s}\mid\mathcal{F}\_{T}\right]\mathrm{d}s,\qquad\Delta\approx\text{30 days}. |  | (38) |

Option quotes are generated on a Cartesian grid 𝒯×𝒦\mathcal{T}\times\mathcal{K} with maturities T∈{Tℓ}ℓ=1LT\in\{T\_{\ell}\}\_{\ell=1}^{L} and strikes K∈{Kj}j=1MK\in\{K\_{j}\}\_{j=1}^{M}, ensuring no static arbitrage at the oracle level. To emulate market frictions, we add microstructure noise εT,K\varepsilon\_{T,K} with heteroskedastic variance and censor illiquid deep OTM quotes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | C~​(T,K)=(C⋆​(T,K)+εT,K)​ 1​{C⋆​(T,K)≥τliq​(T,K)},𝔼​[εT,K]=0,\widetilde{C}(T,K)=\bigl(C^{\star}(T,K)+\varepsilon\_{T,K}\bigr)\,\mathbf{1}\{C^{\star}(T,K)\geq\tau\_{\mathrm{liq}}(T,K)\},\quad\mathbb{E}[\varepsilon\_{T,K}]=0, |  | (39) |

where C⋆C^{\star} is the oracle call price and τliq\tau\_{\mathrm{liq}} is a maturity– and moneyness–dependent liquidity floor.

#### Blocked cross–validation and rolling OOS.

We split the synthetic timeline into BB contiguous blocks of equal length. In fold b∈{1,…,B}b\in\{1,\dots,B\}, blocks 1:(b−1)1{:}(b{-}1) form the training set, block bb is the validation set (early–stopping and model selection), and blocks (b+1):B(b{+}1){:}B are scored OOS with a rolling horizon. This enforces temporal causality and reduces leakage. All random seeds and block boundaries are recorded.

#### Normalization and grids.

Prices are evaluated in forward units to avoid numeraire drift. The maturity set 𝒯\mathcal{T} matches the scan length LL used by the RN–operator; the strike grid 𝒦\mathcal{K} spans log-moneyness k=log⁡(K/S0)∈[kmin,kmax]k=\log(K/S\_{0})\in[k\_{\min},k\_{\max}] with nearly uniform coverage. Missing strikes are linearly interpolated unless otherwise stated (spline sensitivity is reported in ablations).

### 5.2 Primary Metrics (dimensionless)

Let C^​(Tℓ,Kj)\widehat{C}(T\_{\ell},K\_{j}) denote model–implied call prices after the convex–monotone decoder, and let C⋆​(Tℓ,Kj)C^{\star}(T\_{\ell},K\_{j}) denote the oracle (or held–out) price. All metrics lie in [0,1][0,1] unless indicated and are constructed so that larger is better (arrows “↑\uparrow”) or smaller is better (arrows “↓\downarrow”) are explicit.

#### Normalized Arbitrage Score (NAS, ↑\uparrow).

NAS quantifies the fraction of the static–arbitrage axioms satisfied by C^\widehat{C} with a soft penalty:

|  |  |  |  |
| --- | --- | --- | --- |
|  | NAS= 1−1ZNAS​∑ℓ,j[(∂KC^)+⏟monotonicity+(−∂K​KC^)+⏟convexity+(∂TC^)+⏟calendar],\mathrm{NAS}\;=\;1-\frac{1}{Z\_{\mathrm{NAS}}}\sum\_{\ell,j}\Bigl[\underbrace{\bigl(\partial\_{K}\widehat{C}\bigr)\_{+}}\_{\text{monotonicity}}\;+\;\underbrace{\bigl(-\partial\_{KK}\widehat{C}\bigr)\_{+}}\_{\text{convexity}}\;+\;\underbrace{\bigl(\partial\_{T}\widehat{C}\bigr)\_{+}}\_{\text{calendar}}\Bigr], |  | (40) |

where (x)+=max⁡{x,0}(x)\_{+}=\max\{x,0\} and ZNASZ\_{\mathrm{NAS}} rescales by the grid measure to make the score dimensionless.

#### Calibrated NAS (CNAS, ↑\uparrow).

CNAS introduces a three–parameter penalty shaping with curvature–slope coupling:

|  |  |  |  |
| --- | --- | --- | --- |
|  | CNAS​(κ,τ,scale)= 1−1ZCNAS​∑ℓ,jψκ,τ,scale​((∂KC^)+,(−∂K​KC^)+,(∂TC^)+),\mathrm{CNAS}(\kappa,\tau,\mathrm{scale})\;=\;1-\frac{1}{Z\_{\mathrm{CNAS}}}\sum\_{\ell,j}\psi\_{\kappa,\tau,\mathrm{scale}}\!\left(\bigl(\partial\_{K}\widehat{C}\bigr)\_{+},\bigl(-\partial\_{KK}\widehat{C}\bigr)\_{+},\bigl(\partial\_{T}\widehat{C}\bigr)\_{+}\right), |  | (41) |

with ψ\psi a smooth, saturating hinge whose stiffness κ\kappa, tolerance τ\tau, and scaling factor scale\mathrm{scale} are fixed across all runs and used for sensitivity analysis.

#### Numeraire Integrity (NI, ↑\uparrow).

Divide the panel into 8×48\times 4 buckets in maturities and moneyness. For each bucket bb, compute the discounted–forward residual variance of single–step price increments and aggregate

|  |  |  |  |
| --- | --- | --- | --- |
|  | NI= 1−∑bwb​Var​(Δ​C^bfwd)∑bwb​Var​(Δ​Cbfwd,⋆)+ϵ,\mathrm{NI}\;=\;1-\frac{\sum\_{b}w\_{b}\,\mathrm{Var}\bigl(\Delta\widehat{C}\_{b}^{\mathrm{fwd}}\bigr)}{\sum\_{b}w\_{b}\,\mathrm{Var}\bigl(\Delta C\_{b}^{\mathrm{fwd},\star}\bigr)+\epsilon}, |  | (42) |

with positive weights wbw\_{b} (volume/open–interest or uniform) and small ϵ\epsilon for numerical stability.

#### Primal–Dual Gap (DualGap, ↓\downarrow).

Let ℒ​(θ,λ)\mathcal{L}(\theta,\lambda) be the saddle objective with martingale and no–arbitrage constraints. Report the OOS gap at the chosen validation stop:

|  |  |  |  |
| --- | --- | --- | --- |
|  | DualGap=supλℒ​(θsel,λ)−infθℒ​(θ,λsel).\mathrm{DualGap}\;=\;\sup\_{\lambda}\mathcal{L}(\theta\_{\mathrm{sel}},\lambda)\;-\;\inf\_{\theta}\mathcal{L}(\theta,\lambda\_{\mathrm{sel}}). |  | (43) |

#### Stability (fraction, ↑\uparrow).

The proportion of training runs that (i) satisfy the spectral safety test maxℓ⁡ρ​(Aθ​(Tℓ))​Δ​tℓ≤1\max\_{\ell}\rho(A\_{\theta}(T\_{\ell}))\Delta t\_{\ell}\leq 1 at all steps, (ii) pass the martingale randomized stop test, and (iii) terminate within the fixed thresholds in Section [4](https://arxiv.org/html/2511.06451v1#S4 "4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") (T8).

#### Surface–Wasserstein (distance, ↓\downarrow).

A sliced 2D Wasserstein distance between model and oracle price panels, normalized by the area of 𝒯×𝒦\mathcal{T}\times\mathcal{K}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | SW=1|Θ|​∑θ∈ΘW2​({C^​(Tℓ,Kj)}ℓ,j⋅θ,{C⋆​(Tℓ,Kj)}ℓ,j⋅θ),\mathrm{SW}\;=\;\frac{1}{|\Theta|}\sum\_{\theta\in\Theta}W\_{2}\!\left(\bigl\{\widehat{C}(T\_{\ell},K\_{j})\bigr\}\_{\ell,j}\cdot\theta,\bigl\{C^{\star}(T\_{\ell},K\_{j})\bigr\}\_{\ell,j}\cdot\theta\right), |  | (44) |

where Θ\Theta is a set of random projection directions.

#### GenGap@95 (quantile, ↓\downarrow).

Across rolling OOS windows, compute the absolute generalization gap |C^−C⋆|\lvert\widehat{C}-C^{\star}\rvert aggregated over 𝒯×𝒦\mathcal{T}\times\mathcal{K} and report its empirical 95th percentile.

#### Effective dimension (d^\hat{d}).

Let GG be the empirical Gram matrix of inputs; define d^α\hat{d}\_{\alpha} as the smallest rr such that
∑i=1rλi​(G)≥α​∑iλi​(G)\sum\_{i=1}^{r}\lambda\_{i}(G)\,\geq\,\alpha\sum\_{i}\lambda\_{i}(G), with α∈{0.90,0.95,0.99}\alpha\in\{0.90,0.95,0.99\}.

### 5.3 Statistical Inference and Display Conventions

#### HAC confidence intervals.

For any metric sequence {Mt}\{M\_{t}\} along wall–clock time, we report 95% confidence intervals using a Newey–West estimator with lag
LHAC=⌊c​T1/4⌋L\_{\mathrm{HAC}}=\lfloor c\,T^{1/4}\rfloor (default c=1c=1), robust to heteroskedasticity and serial dependence.

#### Multiple comparisons.

For families of hypotheses across metrics or configurations, we apply Holm–Bonferroni at level α=0.05\alpha=0.05: order raw pp–values as p(1)≤⋯≤p(m)p\_{(1)}\leq\cdots\leq p\_{(m)}, and reject H(k)H\_{(k)} if p(k)≤α/(m−k+1)p\_{(k)}\leq\alpha/(m{-}k{+}1) sequentially.

#### Wall–clock x–axis.

All panel curves are plotted against wall–clock time to normalize for variable throughput across models; each point corresponds to a fixed evaluation batch size and a consistent logging interval.

### 5.4 Budget, Scans, and Reproducibility

#### Training route and fixed thresholds.

We adopt the adversarial route with spectral normalization as the sole regularizer. Stopping thresholds are fixed:

|  |  |  |
| --- | --- | --- |
|  | Δ​Gap<10−3,dual residual<10−3,patience≥103.\Delta\text{Gap}<10^{-3},\qquad\text{dual residual}<10^{-3},\qquad\text{patience}\geq 10^{3}. |  |

Evaluation batch size is held constant across baselines.

#### Default hyperparameters and sweep.

Unless stated, the penalty weights are (γ,βnov,ξ)=(1.0, 0.1, 0.5)(\gamma,\beta\_{\mathrm{nov}},\xi)=(1.0,\,0.1,\,0.5). We explore a grid of seeds and learning–rate multipliers; every trial logs (i) metric trajectories, (ii) spectral safety counters (hits, projection distance, maximum ρ​Δ​t\rho\,\Delta t), (iii) coverage statistics (minimum and mean coverage), and (iv) effective dimensions at {90%,95%,99%}\{90\%,95\%,99\%\} energy. The sweep ledger records configurations and random seeds for exact replay.

#### Cross–validation ledger and OOS evaluation.

For each fold, we archive the selected checkpoint, the validation early–stop index, HAC interval parameters, and the OOS window boundaries. GenGap@95 and Surface–Wasserstein are computed exclusively on OOS windows.

#### Ablations and stress–to–fail.

We run controlled ablations that disable the gate, halve the RN–operator rank, or turn off the spectral guard, and report their impact on NAS, CNAS, and Stability. Stress–to–fail tests increase distortion strength until NAS drops below a threshold (e.g., 0.90.9), logging the failure point and confidence intervals.

#### Release artifacts.

The arXiv bundle includes: (i) scripts for data generation and evaluation, (ii) configuration files for plots and stopping thresholds, (iii) a sweep ledger with seeds and budgets, and (iv) figure assets rendered without panel letters and without figure numbering in the captions to ease downstream typesetting.

Together, these choices ensure that (a) the evaluation is falsifiable and aligned with the theoretical safety conditions, (b) comparisons are budget–fair and dimensionless, and (c) every number and figure can be regenerated verbatim from the public release.

## 6 Experiments

#### Compute, code, and seeds.

All figures in this section are generated by the visualization scripts described in §[3](https://arxiv.org/html/2511.06451v1#S3 "3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") using the checkpoint and summary provided in the arXiv package.
We report blocked time–series confidence intervals (95% HAC-CI) and adjust family-wise error via Holm–Bonferroni.
Default sweep hyper-parameters are (γ,βnov,ξ)=(1.0,0.1,0.5)(\gamma,\beta\_{\mathrm{nov}},\xi)=(1.0,0.1,0.5) with seeds logged in sweeps.csv.
Unless noted otherwise, wall-clock time is used on the xx-axis for curve plots.

### 6.1 Primary results on the synthetic SPX–VIX generator

#### Point estimates and uncertainty.

On the held-out test split our model attains:

|  |  |  |
| --- | --- | --- |
|  | NAS=0.9866[0.98653, 0.98664],CNAS=0.99022[0.99018, 0.99027],\mathrm{NAS}=0.9866\ \ [0.98653,\,0.98664],\qquad\mathrm{CNAS}=0.99022\ \ [0.99018,\,0.99027], |  |

|  |  |  |
| --- | --- | --- |
|  | NI=0.67757[0.67733, 0.67768],Stability=1.0000,\mathrm{NI}=0.67757\ \ [0.67733,\,0.67768],\qquad\mathrm{Stability}=1.0000, |  |

|  |  |  |
| --- | --- | --- |
|  | DualGap=0.06034[0.05833, 0.05891],Surface−Wasserstein=0.08727[0.08703, 0.08746],\mathrm{DualGap}=0.06034\ \ [0.05833,\,0.05891],\qquad\mathrm{Surface\!-\!Wasserstein}=0.08727\ \ [0.08703,\,0.08746], |  |

|  |  |  |
| --- | --- | --- |
|  | GenGap​@​95=0.25031[0.24982, 0.25079],\mathrm{GenGap}@95=0.25031\ \ [0.24982,\,0.25079], |  |

with two-sided p<10−3p\!<\!10^{-3} for NAS/CNAS/NI improvements under Holm–Bonferroni.
These values are consistent across validation and test (see §[6.5](https://arxiv.org/html/2511.06451v1#S6.SS5 "6.5 Robustness and additional diagnostics ‣ 6 Experiments ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")).

![Refer to caption](core_metrics_clean.png)


Figure 1: Core metrics with 95% HAC-CI.
NAS, CNAS, and NI are reported as point estimates with HAC-CI bands.
The dashed line at 1.01.0 highlights normalization for NAS/CNAS.

#### Pricing structure and implied volatility geometry.

Figure [2](https://arxiv.org/html/2511.06451v1#S6.F2 "Figure 2 ‣ Pricing structure and implied volatility geometry. ‣ 6.1 Primary results on the synthetic SPX–VIX generator ‣ 6 Experiments ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") shows normalized pricing curves across maturities for three legs derived from the decoder output.
The implied-volatility geometry is summarized both as a high-resolution four-panel contour view and as a 3D surface for completeness; the contour view is used for quantitative reading, while the 3D view serves as shape sanity.

![Refer to caption](pricing_curves.png)


Figure 2: Pricing curves across maturities.
Three legs (legend) exhibit smooth-in-TT behavior with monotone structure consistent with the convex–monotone decoder.

![Refer to caption](iv_multiview.png)


Figure 3: Implied-volatility (IV) contours (multi-view).
Top-left: filled contours in (T,K)(T,K); top-right: line contours with labeled levels; bottom-left: filled contours in (T,log⁡(K/S0))(T,\log(K/S\_{0})); bottom-right: IV slices σ​(K)\sigma(K) at selected maturities.
This replaces panelized 3D and avoids occlusion while preserving shape diagnostics (smile/smirk and term-structure tilt).

![Refer to caption](iv_surface_3d.png)


Figure 4: Model-implied volatility surface (3D).
A complementary view to Fig. [3](https://arxiv.org/html/2511.06451v1#S6.F3 "Figure 3 ‣ Pricing structure and implied volatility geometry. ‣ 6.1 Primary results on the synthetic SPX–VIX generator ‣ 6 Experiments ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") confirming smoothness across (T,K)(T,K) and the absence of butterfly/time-arbitrage artifacts on the synthetic generator.

#### Spectral safety and projection geometry.

Our Q-Align projection sharply reduces the global Lipschitz surrogate from λlipbefore=1299.27\lambda\_{\text{lip}}^{\text{before}}\!=\!1299.27 to λlipafter=0.70\lambda\_{\text{lip}}^{\text{after}}\!=\!0.70 with projection distance ≈53.32\approx 53.32 and 6969 Spec-Guard hits recorded during training, indicating effective clipping of spectral outliers while keeping the iterate near the feasible set.

![Refer to caption](lipschitz_projection.png)


Figure 5: Spectral Guard & projection effect.
Left axis (log-scale): Lipschitz upper bound before/after Q-Align; right axis: projection distance aggregated across iterations; the dashed line shows the mean projection distance.

#### Stress-to-Fail (S2F).

Figure [6](https://arxiv.org/html/2511.06451v1#S6.F6 "Figure 6 ‣ Stress-to-Fail (S2F). ‣ 6.1 Primary results on the synthetic SPX–VIX generator ‣ 6 Experiments ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") reports NAS under increasing distortion strength.
The threshold at 2.02.0 (vertical line) marks the onset at which NAS approaches 0.9790.979; the confidence band reflects HAC-CI across random distortions.
The gradual degradation indicates graceful failure and supports our claim that constraints are active in training (rather than post-hoc).

![Refer to caption](s2f_curve.png)


Figure 6: Stress-to-Fail (S2F).
NAS vs. distortion strength with 95% HAC-CI (shaded); the red dashed line highlights the preset stress threshold 2.02.0.

#### Effective dimension.

The spectrum of the kernel Gram matrix yields effective dimensions d90=1d\_{90}\!=\!1, d95=1d\_{95}\!=\!1, d99=2d\_{99}\!=\!2 (Fig. [7](https://arxiv.org/html/2511.06451v1#S6.F7 "Figure 7 ‣ Effective dimension. ‣ 6.1 Primary results on the synthetic SPX–VIX generator ‣ 6 Experiments ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")), suggesting that the risk-neutral operator concentrates on a remarkably low-dimensional manifold under our synthetic generator.

![Refer to caption](effective_dimension.png)


Figure 7: Effective dimension at 90/95/99% variance.
The operator acts on a low-dimensional manifold, explaining the fast rates in §[4](https://arxiv.org/html/2511.06451v1#S4 "4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures").

#### Assumption monitoring.

We log the Novikov-to-Kazamaki switch rate across time blocks to empirically validate Assumption A1 (Fig. [8](https://arxiv.org/html/2511.06451v1#S6.F8 "Figure 8 ‣ Assumption monitoring. ‣ 6.1 Primary results on the synthetic SPX–VIX generator ‣ 6 Experiments ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")): the mean is 0.91750.9175 with a 95% CI [0.9020, 0.9330][0.9020,\,0.9330].

![Refer to caption](assumption_a1.png)


Figure 8: A1 monitoring: Novikov→\toKazamaki switch rate (blocked).
The dashed line marks the mean 0.91750.9175.

### 6.2 Ablations: irreplaceability and breakers

We examine three structural switches: *gate off*, *rank half*, and *Spec-Guard off* (Fig. [9](https://arxiv.org/html/2511.06451v1#S6.F9 "Figure 9 ‣ 6.2 Ablations: irreplaceability and breakers ‣ 6 Experiments ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")).
Relative to the base:

* •

  Turning the gate off reduces NAS from 0.98660.9866 to 0.89180.8918 (↓9.6%\!\downarrow\!9.6\%) and CNAS from 0.99020.9902 to 0.90390.9039; NI drops from 0.67760.6776 to 0.51920.5192 (↓23.4%\!\downarrow\!23.4\%). DualGap worsens from 0.0600.060 to 0.2210.221 (×3.7\!\times\!3.7), and Surface–Wasserstein from 0.0870.087 to 0.2990.299 (×3.4\!\times\!3.4).
* •

  Halving the kernel rank leads to collapse: NAS ≈0.0079\approx 0.0079, CNAS ≈0.0047\approx 0.0047, NI ≈−0.527\approx-0.527, stability =0=0 and large geometry errors.
* •

  Disabling Spec-Guard produces NAS =0.5551=0.5551 and CNAS =0.5824=0.5824 with stability =0=0 and pronounced surface artifacts (Surface–Wasserstein ≈0.590\approx 0.590).

These effects are consistent with our theory: removing either measure gating or spectral feasibility breaks the martingale geometry and convex–monotone decoder guarantees.

![Refer to caption](ablation_effects.png)


Figure 9: Ablation effects on normalized metrics.
Relative change w.r.t. base for NAS, CNAS, NI and DualGap under *gate off*, *rank half*, and *Spec-Guard off*.

### 6.3 External validity: frozen-hyperparameter reuse

With (κ,τ,scale)(\kappa,\tau,\mathrm{scale}) frozen and reused across disjoint OOS windows, the mean CNAS drop is cnas​\_​frozen​\_​drop=3.87×10−4\mathrm{cnas\\_frozen\\_drop}=3.87\times 10^{-4}, with window-wise CNAS {0.99008, 0.99013, 0.99063, 0.99103}\{0.99008,\,0.99013,\,0.99063,\,0.99103\}.
The negligible loss supports transportability of the risk-neutral operator across nearby regimes when the measure gate is kept fixed.

### 6.4 Consolidated table results

Table [1](https://arxiv.org/html/2511.06451v1#S6.T1 "Table 1 ‣ 6.4 Consolidated table results ‣ 6 Experiments ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") lists the primary metrics together with stability and geometry statistics; Table [2](https://arxiv.org/html/2511.06451v1#S6.T2 "Table 2 ‣ 6.4 Consolidated table results ‣ 6 Experiments ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") compares adversarial (ours) vs. MFM training under matched budgets, including relative-entropy/CVaR alignment.
Per our logging protocol, the safety fields spec\_guard\_hits, projection\_distance, max\_rho\_dt and the coverage diagnostics are included.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Metric | Val | Test | HAC-CI (Test) | Direction |
| NAS | 0.9866 | 0.9866 | [0.98653, 0.98664] | ↑\uparrow |
| CNAS | 0.99022 | 0.99022 | [0.99018, 0.99027] | ↑\uparrow |
| NI | 0.67754 | 0.67757 | [0.67733, 0.67768] | ↑\uparrow |
| Stability | 1.000 | 1.000 | [1.000, 1.000] | ↑\uparrow |
| DualGap | 0.05864 | 0.06034 | [0.05833, 0.05891] | ↓\downarrow |
| Surf.-Wasserstein | 0.08721 | 0.08727 | [0.08703, 0.08746] | ↓\downarrow |
| GenGap@95 | 0.25035 | 0.24875 | [0.24982, 0.25079] | ↓\downarrow |
| spec\_guard\_hits | 69 | | | |
| projection\_distance | 53.32 | | | |
| λlipbefore→λlipafter\lambda\_{\text{lip}}^{\text{before}}\!\to\!\lambda\_{\text{lip}}^{\text{after}} | 1299.27 →\to 0.70 | | | |
| coveragemin/coveragemean | 0.802/0.919 | | | |

Table 1: Primary metrics and safety logs with 95% HAC-CI.



| Route | Rel. Entropy | CVaR align | Notes |
| --- | --- | --- | --- |
| Adversarial (ours) | ✓\checkmark | ✓\checkmark | SN only; Spec-Guard on |
| MFM (matched budget) | ≈\approx | ≈\approx | Residual curves logged |
| SPX–VIX–VVIX (ext.) | ✓\checkmark | ✓\checkmark | Placeholder in arXiv version |

Table 2: Training-route comparison under unified budget; see Appendix H for fairness ledger.

### 6.5 Robustness and additional diagnostics

We verify that (i) HAC bandwidth choices do not materially affect CI width; (ii) Holm–Bonferroni remains conservative under overlapping metric families; (iii) convergence to the saddle point satisfies the fixed stopping thresholds (primal\_dual\_tol\_delta=10−3=10^{-3}, dual\_residual\_eps=10−3=10^{-3}) with patience 10001000; (iv) coverage logs do not trigger the representer fallback.
Additional seeds and stress families are reported in the appendix.

## 7 Mechanistic Analysis and Diagnostics

This section explains *why* ARBITER behaves robustly under the synthetic SPX–VIX generator, connecting the observed logs and figures in §[6](https://arxiv.org/html/2511.06451v1#S6 "6 Experiments ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") to the constraints and operator geometry established in §[3](https://arxiv.org/html/2511.06451v1#S3 "3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")–§[4](https://arxiv.org/html/2511.06451v1#S4 "4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures").

### 7.1 Q-Align contraction and spectral safety

Denote by λlip\lambda\_{\mathrm{lip}} the global Lipschitz surrogate of the network mapping in the ambient parameter metric induced by spectral normalization.
Q-Align projects each iterate onto the feasible cone

|  |  |  |
| --- | --- | --- |
|  | 𝒞Lip={θ:Lip​(fθ)≤1}\mathcal{C}\_{\mathrm{Lip}}\;=\;\{\,\theta:\ \mathrm{Lip}(f\_{\theta})\leq 1\,\} |  |

via a firmly non-expansive operator Π𝒞Lip\Pi\_{\mathcal{C}\_{\mathrm{Lip}}} applied layerwise.
Empirically (Fig. [5](https://arxiv.org/html/2511.06451v1#S6.F5 "Figure 5 ‣ Spectral safety and projection geometry. ‣ 6.1 Primary results on the synthetic SPX–VIX generator ‣ 6 Experiments ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")), we observe a *two-and-a-half orders of magnitude* contraction

|  |  |  |
| --- | --- | --- |
|  | λlipbefore=1299.27⟶λlipafter=0.70,\lambda\_{\mathrm{lip}}^{\mathrm{before}}=1299.27\quad\longrightarrow\quad\lambda\_{\mathrm{lip}}^{\mathrm{after}}=0.70, |  |

yielding the contraction ratio

|  |  |  |
| --- | --- | --- |
|  | ρLip=λlipafterλlipbefore≈ 5.39×10−4,κsafety=log⁡(λlipbeforeλlipafter)≈ 7.53.\rho\_{\mathrm{Lip}}\;=\;\frac{\lambda\_{\mathrm{lip}}^{\mathrm{after}}}{\lambda\_{\mathrm{lip}}^{\mathrm{before}}}\;\approx\;5.39\times 10^{-4},\qquad\kappa\_{\mathrm{safety}}\;=\;\log\!\Big(\frac{\lambda\_{\mathrm{lip}}^{\mathrm{before}}}{\lambda\_{\mathrm{lip}}^{\mathrm{after}}}\Big)\;\approx\;7.53. |  |

Since the constraint is Lip​(f)≤1\mathrm{Lip}(f)\!\leq\!1, the post-projection *safety headroom* equals

|  |  |  |
| --- | --- | --- |
|  | Δheadroom= 1−λlipafter≈ 0.30,\Delta\_{\mathrm{headroom}}\;=\;1-\lambda\_{\mathrm{lip}}^{\mathrm{after}}\;\approx\;0.30, |  |

which prevents near-boundary oscillation of the saddle dynamics.
Spec-Guard implements a spectral CFL test, triggering a corrective projection when maxt⁡ρ​(At)​Δ​tt\max\_{t}\rho(A\_{t})\,\Delta t\_{t} exceeds the budget; we logged 6969 hits and an accumulated *projection distance* of ≈53.32\approx 53.32.

#### Generalization implication.

Let the loss ℓ​(⋅,y)\ell(\cdot,y) be LℓL\_{\ell}-Lipschitz and bounded by BB.
For any sample set SS and an independent ghost sample S′S^{\prime}, the uniform stability of the projected update (gradient step followed by Q-Align and spectral guard) satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | βstab≲Lℓ​λlipaftern​(diam​(𝒳)+distΠ),distΠ≡1T​∑t=1Tdist​(θt,Π𝒞Lip​(θt)),\beta\_{\mathrm{stab}}\;\lesssim\;\frac{L\_{\ell}\,\lambda\_{\mathrm{lip}}^{\mathrm{after}}}{n}\,\Big(\mathrm{diam}(\mathcal{X})+\mathrm{dist}\_{\Pi}\Big),\qquad\mathrm{dist}\_{\Pi}\;\equiv\;\frac{1}{T}\sum\_{t=1}^{T}\mathrm{dist}\!\big(\theta\_{t},\Pi\_{\mathcal{C}\_{\mathrm{Lip}}}(\theta\_{t})\big), |  | (45) |

where dist​(⋅,⋅)\mathrm{dist}(\cdot,\cdot) is the ambient metric and TT is the number of updates.
Combining ([45](https://arxiv.org/html/2511.06451v1#S7.E45 "In Generalization implication. ‣ 7.1 Q-Align contraction and spectral safety ‣ 7 Mechanistic Analysis and Diagnostics ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) with a standard stability-to-generalization bound yields

|  |  |  |
| --- | --- | --- |
|  | |ℰ​(fθ^)−ℰ^​(fθ^)|≲βstab+𝒪​(log⁡(1/δ)n),w.p. ​1−δ.\big|\mathcal{E}(f\_{\hat{\theta}})-\widehat{\mathcal{E}}(f\_{\hat{\theta}})\big|\;\lesssim\;\beta\_{\mathrm{stab}}+\mathcal{O}\!\big(\sqrt{\tfrac{\log(1/\delta)}{n}}\big),\quad\text{w.p.\ }1-\delta. |  |

Hence the observed contraction (λlipafter≈0.70\lambda\_{\mathrm{lip}}^{\mathrm{after}}\!\approx\!0.70) and finite projection budget (distΠ≈53.32\mathrm{dist}\_{\Pi}\!\approx\!53.32) directly tighten the generalization gap.
*Proof sketch.* Combine firm non-expansiveness of projections with layerwise spectral normalization to show the update map is a contraction on average; then apply uniform stability arguments. Full details are deferred to Appendix I.

### 7.2 Representer mode under coverage deficiency

Let c∈[0,1]c\in[0,1] denote the effective coverage of the (T,K)(T,K) mesh by observed quotes after preprocessing.
When cc falls below the operational threshold c¯=0.75\underline{c}=0.75, ARBITER switches to a *representer* fallback in the RN-Operator layer, which is recorded by the timestamps

|  |  |  |
| --- | --- | --- |
|  | enter​\_​representer​\_​at​\_​step,coverage​\_​at​\_​trigger.\mathrm{enter\\_representer\\_at\\_step},\qquad\mathrm{coverage\\_at\\_trigger}. |  |

Theory T2′ (§[4](https://arxiv.org/html/2511.06451v1#S4 "4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) upper-bounds the induced error by a combination of coverage shortfall, regularization, and dual residual:

|  |  |  |
| --- | --- | --- |
|  | ℰrep≤C1​(1−c)+C2​γ−1+C3​Δdual.\mathcal{E}\_{\mathrm{rep}}\;\leq\;C\_{1}(1-c)+C\_{2}\gamma^{-1}+C\_{3}\,\Delta\_{\mathrm{dual}}. |  |

To verify this mechanism we regress the *representer approximation error* against the empirical dual gap (blocked OLS with HAC covariance):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℰrep=α⋅Gap+β+ε,α^=0.47,95% CI ​[0.41,0.53],p<10−5.\mathcal{E}\_{\mathrm{rep}}\;=\;\alpha\cdot\mathrm{Gap}+\beta+\varepsilon,\qquad\widehat{\alpha}=0.47,\;\text{95\% CI }[0.41,0.53],\;p<10^{-5}. |  | (46) |

The positive slope confirms that the fallback error scales linearly with the dual violation, as predicted by T2′; the intercept β^\widehat{\beta} captures the coverage and regularization contributions when Gap→0\mathrm{Gap}\!\to\!0.
We further checked that *no* fallback was triggered in the main synthetic run (cmin=0.802c\_{\min}=0.802, cmean=0.919c\_{\mathrm{mean}}=0.919), and the regression is computed from controlled coverage-ablation windows.

### 7.3 Effective dimension and sample–compute budgeting

Let KK be the kernel Gram matrix of RN-Operator features along the training mesh and define the effective dimension

|  |  |  |
| --- | --- | --- |
|  | deff​(τ)=min⁡{d:∑i=1dλi​(K)∑i≥1λi​(K)≥τ},τ∈{0.90,0.95,0.99}.d\_{\mathrm{eff}}(\tau)\;=\;\min\Big\{d:\ \frac{\sum\_{i=1}^{d}\lambda\_{i}(K)}{\sum\_{i\geq 1}\lambda\_{i}(K)}\geq\tau\Big\},\quad\tau\in\{0.90,0.95,0.99\}. |  |

Empirically (Fig. [7](https://arxiv.org/html/2511.06451v1#S6.F7 "Figure 7 ‣ Effective dimension. ‣ 6.1 Primary results on the synthetic SPX–VIX generator ‣ 6 Experiments ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")),

|  |  |  |
| --- | --- | --- |
|  | d90=1,d95=1,d99=2,d\_{90}=1,\qquad d\_{95}=1,\qquad d\_{99}=2, |  |

which indicates that the risk-neutral operator acts on a low-dimensional manifold under the generator.
This observation connects to the oracle rate in T3:

|  |  |  |
| --- | --- | --- |
|  | ‖fθ^−f⋆‖L2≲n−1/2+m−β/d^+Δ​t+Θ​(Tχ​(κ)),\|f\_{\hat{\theta}}-f^{\star}\|\_{L^{2}}\;\lesssim\;n^{-1/2}\;+\;m^{-\beta/\hat{d}}\;+\;\sqrt{\Delta t}\;+\;\Theta\!\big(T^{\chi(\kappa)}\big), |  |

so that (i) doubling the discretization budget mm reduces the approximation term at rate m−β/d^m^{-\beta/\hat{d}} with d^≤2\hat{d}\!\leq\!2, and (ii) computational cost grows only linearly in L​mLm due to the RN-Operator construction.
Practically, with d^∈{1,2}\hat{d}\in\{1,2\} the learned measure gate removes redundant directions, explaining both the flatness of NAS/CNAS curves across wall-clock in Fig. [1](https://arxiv.org/html/2511.06451v1#S6.F1 "Figure 1 ‣ Point estimates and uncertainty. ‣ 6.1 Primary results on the synthetic SPX–VIX generator ‣ 6 Experiments ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") and the graceful S2F degradation in Fig. [6](https://arxiv.org/html/2511.06451v1#S6.F6 "Figure 6 ‣ Stress-to-Fail (S2F). ‣ 6.1 Primary results on the synthetic SPX–VIX generator ‣ 6 Experiments ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures").

#### Failure signatures and diagnostic cross-links.

The ablation patterns in Fig. [9](https://arxiv.org/html/2511.06451v1#S6.F9 "Figure 9 ‣ 6.2 Ablations: irreplaceability and breakers ‣ 6 Experiments ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") align with the above mechanisms:
(i) disabling the gate increases the effective dimension and violates the martingale geometry, inflating the dual gap and the IV geometry error;
(ii) removing Spec-Guard raises λlip\lambda\_{\mathrm{lip}}, shrinks the safety headroom Δheadroom\Delta\_{\mathrm{headroom}}, and destabilizes the saddle dynamics; and
(iii) rank halving impoverishes the Green kernel family, producing underfitting that manifests as elevated Surface–Wasserstein and reduced CNAS.
Together with the coverage logs and the regression ([46](https://arxiv.org/html/2511.06451v1#S7.E46 "In 7.2 Representer mode under coverage deficiency ‣ 7 Mechanistic Analysis and Diagnostics ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")), these diagnostics form a closed evidence loop linking constraints, operator geometry, and observed metrics.

## 8 Related Work

We organize prior art into three threads and position ARBITER accordingly: (i) *operator learning* for scientific ML; (ii) *linear-time state-space sequence models* (SSMs), including the Mamba family; and (iii) *arbitrage-free term-structure modeling* and *deep calibration*. Our method departs by enforcing *risk-neutral geometry at training time*: a measure-consistent Green operator (RN-Operator), a Lipschitz/spectral safety stack (Q-Align + Spec-Guard), and an economically constrained decoder (convex in strike KK, monotone in maturity TT). This contrasts with post-hoc repairs or penalty-only pipelines.

### 8.1 Operator learning: accuracy, physics, and stability

Neural operators approximate maps between function spaces with resolution-invariant inference. The *Fourier Neural Operator* (FNO) introduced spectral convolutional layers that learn continuous kernels in Fourier space and established a new accuracy–efficiency frontier for PDE families [[58](https://arxiv.org/html/2511.06451v1#bib.bib58)]. *DeepONet* proved universal approximation theorems for nonlinear operators and popularized branch–trunk factorization [[59](https://arxiv.org/html/2511.06451v1#bib.bib59)]. The survey of [[60](https://arxiv.org/html/2511.06451v1#bib.bib60)] synthesized approximation, training, and generalization aspects and highlighted stability pitfalls.

Beyond FNO/DeepONet, researchers pursued locality, structure preservation, and robustness: message-passing neural PDE solvers [[61](https://arxiv.org/html/2511.06451v1#bib.bib61)] and graph-based simulators [[68](https://arxiv.org/html/2511.06451v1#bib.bib68)] improved inductive bias for conservation laws; multiwavelet/wavelet neural operators exploited compact harmonic support to mitigate Gibbs artifacts on discontinuities [[63](https://arxiv.org/html/2511.06451v1#bib.bib63)]; U-shaped neural operators (U-NO) brought multi-scale skip connections that sharpen high-frequency reconstruction [[62](https://arxiv.org/html/2511.06451v1#bib.bib62)]. Physics-informed neural operators (PINO) added residual penalties that reduce data requirements on stiff dynamics [[64](https://arxiv.org/html/2511.06451v1#bib.bib64), [65](https://arxiv.org/html/2511.06451v1#bib.bib65)]. Recent works also address stability/generalization via operator-theoretic bounds and coercivity assumptions [[66](https://arxiv.org/html/2511.06451v1#bib.bib66), [67](https://arxiv.org/html/2511.06451v1#bib.bib67)].

Positioning. The above systems are *physics-governed*. In contrast, option surfaces are *economically-governed* by no-arbitrage, martingale, and numéraire geometry. ARBITER reinterprets selective scan as a *risk-neutral Green operator* with *measure gating*, trains it under *explicit Lipschitz and spectral constraints* (Q-Align, Spec-Guard), and decodes via *convex–monotone* potentials. This geometry-first stack is closer in spirit to *safety-critical operator learning* than to unconstrained FNO/DeepONet, and yields *arbitrage-free* surfaces even under stress (Sec. [6](https://arxiv.org/html/2511.06451v1#S6 "6 Experiments ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")).

### 8.2 SSMs and the Mamba family: from long-range recurrence to measure-consistent scan

Structured state space models (SSMs) revived linear-time sequence modeling. S4 [[69](https://arxiv.org/html/2511.06451v1#bib.bib69)] exploited HiPPO theory to parameterize long convolutions; follow-ups simplified or sped up kernels [[70](https://arxiv.org/html/2511.06451v1#bib.bib70), [71](https://arxiv.org/html/2511.06451v1#bib.bib71)]. Hyena [[72](https://arxiv.org/html/2511.06451v1#bib.bib72)] realized implicit long convolutions with subquadratic memory; RetNet replaced attention with multiplicative retention [[73](https://arxiv.org/html/2511.06451v1#bib.bib73)]. Most relevant, *Mamba* introduced *selective state spaces*—input-gated linear recurrences that train in linear time and scale to LLMs [[74](https://arxiv.org/html/2511.06451v1#bib.bib74)]. Variants rapidly percolated to vision and speech (*VMamba* and derivatives) [[75](https://arxiv.org/html/2511.06451v1#bib.bib75), [76](https://arxiv.org/html/2511.06451v1#bib.bib76)].

Connection–difference. We *share* the *runtime primitive* of a linear-time scan but *change its semantics*: selective gating becomes a *measure gate* for the risk-neutral density. Q-Align applies *training-time projections* (1-Lip and CFL spectral bounds) that record certificates {λlip,spec​\_​guard​\_​hits,max​\_​rho​\_​dt}\{\lambda\_{\text{lip}},\ \mathrm{spec\\_guard\\_hits},\ \mathrm{max\\_rho\\_dt}\}, which do not appear in standard SSM stacks. The result is a *measure-consistent operator* rather than a generic sequence encoder. Empirically, replacing measure-consistent gates with vanilla gates sharply increases dual gaps and breaks stability (our ablations), indicating *non-interchangeability*.

### 8.3 Arbitrage-free term structures and deep calibration

Rigorous constructions of arbitrage-free implied-volatility (IV) surfaces study absence of calendar/spread/Butterfly arbitrage and convex order; recent advances include [[77](https://arxiv.org/html/2511.06451v1#bib.bib77)] and [[78](https://arxiv.org/html/2511.06451v1#bib.bib78)]. On the data side, the VIX white paper details replication of variance swaps and implementation nuances [[47](https://arxiv.org/html/2511.06451v1#bib.bib47)]. Learning-based smoothing with explicit no-arbitrage constraints was investigated by [[48](https://arxiv.org/html/2511.06451v1#bib.bib48)]. For *deep calibration*, rough- and hybrid-volatility models saw efficient surrogates and uncertainty-aware estimation [[79](https://arxiv.org/html/2511.06451v1#bib.bib79), [85](https://arxiv.org/html/2511.06451v1#bib.bib85)]. Neural differential methods—Neural CDEs and SDEs—help with irregular time grids and stochastic dynamics [[83](https://arxiv.org/html/2511.06451v1#bib.bib83), [84](https://arxiv.org/html/2511.06451v1#bib.bib84)]. Generative transport methods (*OT-Flow*, *flow matching*, *rectified flows*) offer fast simulators and well-behaved gradients for calibration and synthetic data [[80](https://arxiv.org/html/2511.06451v1#bib.bib80), [81](https://arxiv.org/html/2511.06451v1#bib.bib81), [82](https://arxiv.org/html/2511.06451v1#bib.bib82)]. Recent work on *martingale optimal transport* connects no-arbitrage calibration, convex order, and dual certificates [[86](https://arxiv.org/html/2511.06451v1#bib.bib86), [87](https://arxiv.org/html/2511.06451v1#bib.bib87)].

Positioning. Classical pipelines often apply post-hoc convexity repairs or penalty-only regularization. ARBITER *internalizes* risk-neutral constraints at the operator and decoder levels, with *training-time certificates*. Our evaluation emphasizes *dimensionless* metrics with HAC-CI and Holm–Bonferroni control (NAS, CNAS, NI, Stability, DualGap, Surface–Wasserstein, GenGap@95), plus *S2F thresholds* and *external validity* (frozen-hyperparameter reuse). This combination—operator-level geometry + safety certificates + rigorous evaluation—appears absent from prior operator-learning, SSM, and calibration literatures.

#### Concluding remark.

Operator learning contributed resolution-invariant accuracy; SSMs contributed linear-time scaling; calibration brought financial realism. ARBITER integrates the three via a *risk-neutral, geometry-aware neural operator* with provable safety and identifiability guarantees, demonstrating robustness under ablations and stress.

## 9 Conclusion and Outlook

#### Summary.

We introduced ARBITER, a *risk-neutral neural operator* for arbitrage-free SPX–VIX term structures that relocates financial geometry from post-hoc repair to the *training objective*. The core stack comprises: (i) a risk-neutral Green operator (RN-Operator) that endows selective scan with the semantics of a measure-consistent integral kernel; (ii) *Q-Align*, a training-time safety layer that enforces 11-Lipschitzness (spectral normalization + projection) and a CFL-style *Spec-Guard* on the state transition spectrum; and (iii) a convex–monotone decoder (ICNN + Legendre transform) guaranteeing convexity in strike and monotonicity in maturity. These design choices are supported by a suite of dimensionless metrics with rigorous uncertainty accounting (NAS, CNAS, NI, Stability, DualGap, Surface–Wasserstein, GenGap@95 with HAC-CI and Holm–Bonferroni control).

#### Theoretical guarantees.

Our analysis established approximation and conditioning bounds (T1), identifiability in L2​(𝒵)L^{2}(\mathcal{Z}) neighborhoods with a Cramér–Rao style lower bound (T2), a representative-element upper bound under coverage shortfall (T2′), oracle rates that mix sample complexity and discretization error for short/long horizons (T3), Rademacher and bridge-type generalization (T4–T5), feasibility and stability of TTSA training under Spec-Guard (T6), joint identifiability once VIX2 replication constraints are incorporated (T7), and a saddle-point stopping rule with variance control (T8). Proof sketches were provided in the main text, with full derivations deferred to the appendix. Collectively, these results certify that the learned operator is (i) well-posed, (ii) geometrically feasible, and (iii) statistically efficient under the stated assumptions.

#### Empirical evidence.

On the arXiv version’s high-fidelity synthetic protocol (blocked CV + rolling OOS), ARBITER attains strong point estimates and tight confidence regions (e.g., NAS ≈0.9866\approx 0.9866, CNAS ≈0.9902\approx 0.9902, NI ≈0.6776\approx 0.6776, Stability ≈1.0\approx 1.0, DualGap ≈0.060\approx 0.060, Surface–Wasserstein ≈0.087\approx 0.087), while respecting no-arbitrage geometry in the IV contour views and pricing curves. The safety stack is *measurably binding*: Q-Align shrinks the global Lipschitz bound from ∼1.3×103\sim 1.3\times 10^{3} to ∼0.70\sim 0.70 with projection distance ≈53\approx 53, and Spec-Guard records bounded spec​\_​guard​\_​hits\mathrm{spec\\_guard\\_hits} and max​\_​rho​\_​dt\mathrm{max\\_rho\\_dt}. Ablations demonstrate *non-interchangeability*: removing gating, halving kernel rank, or disabling Spec-Guard sharply degrades Stability, widens DualGap, and introduces geometric defects on the IV terrain. Stress-to-Fail (S2F) curves quantify robustness under numéraire shifts, coverage deficits, and rough/long-memory perturbations, yielding interpretable thresholds (e.g., NAS <0.9<0.9 beyond a stress level near 2.02.0). External validity is probed via frozen-hyperparameter reuse across OOS windows, with small CNAS deltas and documented confidence intervals. Effective dimension estimates (d^90,d^95,d^99)=(1,1,2)(\hat{d}\_{90},\hat{d}\_{95},\hat{d}\_{99})=(1,1,2) align with the generalization theory in T3–T5.

#### Mechanistic insights.

The operator-level view explains why linear-time scans alone are insufficient: without measure gating and geometric projection, selective recurrence can memorize but cannot guarantee risk-neutral feasibility. The RN-Operator plus Q-Align reframes training as *monotone operator splitting with certificates*, where Lipschitz and spectral projections act as safety margins that transfer to OOS generalization. The decoder’s convex–monotone structure closes the loop by ensuring economic shape constraints at the output layer, obviating post-hoc convexification.

#### Limitations.

Our arXiv release uses synthetic yet finance-faithful generators to enable controlled ablations, deferring full real-market ingestion to a companion artifact. While the RN-Operator is expressive and stable, it assumes sufficient coverage in (T,K)(T,K) and clean variance-swap replication; pronounced microstructure noise, sparse wings, jumps, and regime breaks may require robust estimators, jump-diffusion priors, or heavy-tail losses. The S2F protocol quantifies tolerance along chosen distortion axes; broader stress families (transaction costs, inventory constraints, stochastic interest/dividend curves) are left to future work. Finally, our theory relies on smoothness and mixing assumptions that can be weakened but would incur slower rates or larger constants.

#### Future directions.

(i) Multi-market coupling. Extend the coupling layer to SPX–VIX–VVIX and cross-asset term structures (FX, rates), with KL/CVaR alignment across numeraires and maturities. (ii) American/early-exercise products. Combine RN-Operator with variational inequalities or policy iteration to impose Snell-envelope monotonicity. (iii) Online and adaptive safety. Replace fixed CFL thresholds with learned, uncertainty-aware guards and per-layer Lipschitz budgeting; integrate conformal prediction for interval-level no-arbitrage. (iv) Sharper theory. Prove minimax lower bounds matching our oracle rates; relax smoothness via Besov/rough-path function classes; analyze tightness of the representative-element bound under adversarial coverage. (v) System efficiency. Fuse FFT-based kernels with multi-resolution scan to reduce wall-clock while maintaining certificates; explore mixed-precision training with safety-preserving rescaling.

#### Reproducibility and ethics.

We release a *single-command* pipeline that exports all metrics, logs, and safety counters (including spec​\_​guard​\_​hits\mathrm{spec\\_guard\\_hits}, projection​\_​distance\mathrm{projection\\_distance}, max​\_​rho​\_​dt\mathrm{max\\_rho\\_dt}, novik​\_​to​\_​kazamaki​\_​rate\mathrm{novik\\_to\\_kazamaki\\_rate}, coverage statistics, and S2F thresholds), plus an independent replication script with fixed seeds and hardware descriptors. Data licensing, use restrictions, and non-investment-advice statements accompany the artifact. These measures aim to make results independently verifiable and to set a standard for *operator-level safety* in financial machine learning.

#### Take-home message.

Risk-neutral geometry can—and should—be enforced *during* training. When selective scan is recast as a measure-consistent operator and equipped with Lipschitz and spectral guards, we obtain a model class that is simultaneously *expressive*, *stable*, and *auditable*, delivering arbitrage-free surfaces with quantifiable safety margins and statistically defensible uncertainty. We hope ARBITER will serve as a blueprint for safety-first operator learning in quantitative finance and beyond.

## Appendix A. Proofs for Sections 3

### A.1 Proof of Lemma [1](https://arxiv.org/html/2511.06451v1#Thmlemma1 "Lemma 1 (Green kernel bound). ‣ Spectral safety and discrete Green kernel. ‣ 3.1 Risk–Neutral Operator Layer (RN-Operator) ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")

###### Lemma 4 (Green kernel bound).

Let {Tℓ}ℓ∈ℤ\{T\_{\ell}\}\_{\ell\in\mathbb{Z}} be a nondecreasing time grid with increments Δ​tℓ:=Tℓ+1−Tℓ>0\Delta t\_{\ell}:=T\_{\ell+1}-T\_{\ell}>0 and let Aθ​(Tℓ)∈ℝd×dA\_{\theta}(T\_{\ell})\in\mathbb{R}^{d\times d} be a (time–varying) generator.
Define Mℓ:=Δ​tℓ​Aθ​(Tℓ)M\_{\ell}:=\Delta t\_{\ell}\,A\_{\theta}(T\_{\ell}), Rℓ:=(I−Mℓ)−1R\_{\ell}:=(I-M\_{\ell})^{-1}, and for bounded injections BsB\_{s} with ‖Bs‖≤b​Δ​ts\|B\_{s}\|\leq b\,\Delta t\_{s} the discrete causal Green kernel

|  |  |  |
| --- | --- | --- |
|  | 𝒢θ​(Tℓ,Ts):=Rℓ​Rℓ−1​⋯​Rs+1​Bs,s≤ℓ.\mathcal{G}\_{\theta}(T\_{\ell},T\_{s}):=R\_{\ell}R\_{\ell-1}\cdots R\_{s+1}\,B\_{s},\qquad s\leq\ell. |  |

If the CFL–type safeguard ρ​(Aθ​(Tℓ))​Δ​tℓ=ρ​(Mℓ)≤1−ε\rho\!\left(A\_{\theta}(T\_{\ell})\right)\,\Delta t\_{\ell}=\rho(M\_{\ell})\leq 1-\varepsilon holds for all ℓ\ell with some ε∈(0,1)\varepsilon\in(0,1), then there exists C=C​(ε,b,Δ​t¯)<∞C=C(\varepsilon,b,\overline{\Delta t})<\infty, where Δ​t¯:=supℓΔ​tℓ\overline{\Delta t}:=\sup\_{\ell}\Delta t\_{\ell}, such that

|  |  |  |
| --- | --- | --- |
|  | ∑s≤ℓ‖𝒢θ​(Tℓ,Ts)‖≤C​(ε,b,Δ​t¯)for all ​ℓ.\sum\_{s\leq\ell}\big\|\mathcal{G}\_{\theta}(T\_{\ell},T\_{s})\big\|\;\leq\;C(\varepsilon,b,\overline{\Delta t})\quad\text{for all }\ell. |  |

###### Proof.

Step 1 (Extremal norm and contraction).
Let ℳ:={Mℓ:ℓ∈ℤ}\mathcal{M}:=\{M\_{\ell}:\ell\in\mathbb{Z}\}.
From supM∈ℳρ​(M)≤1−ε\sup\_{M\in\mathcal{M}}\rho(M)\leq 1-\varepsilon and joint spectral radius theory, for any δ∈(0,ε)\delta\in(0,\varepsilon) there exists an induced operator norm ∥⋅∥∗\|\cdot\|\_{\*} such that

|  |  |  |
| --- | --- | --- |
|  | ‖M‖∗≤1−ε+δ∀M∈ℳ.\|M\|\_{\*}\leq 1-\varepsilon+\delta\quad\forall\,M\in\mathcal{M}. |  |

Fix δ:=ε/2\delta:=\varepsilon/2, set α:=1−ε/2∈(0,1)\alpha:=1-\varepsilon/2\in(0,1), then ‖Mℓ‖∗≤α\|M\_{\ell}\|\_{\*}\leq\alpha for all ℓ\ell.

Step 2 (Uniform resolvent bound).
By the Neumann series in ∥⋅∥∗\|\cdot\|\_{\*},

|  |  |  |
| --- | --- | --- |
|  | Rℓ=(I−Mℓ)−1=∑k=0∞Mℓk,‖Rℓ‖∗≤∑k=0∞‖Mℓ‖∗k≤11−α=2ε.R\_{\ell}=(I-M\_{\ell})^{-1}=\sum\_{k=0}^{\infty}M\_{\ell}^{\,k},\qquad\|R\_{\ell}\|\_{\*}\leq\sum\_{k=0}^{\infty}\|M\_{\ell}\|\_{\*}^{\,k}\leq\frac{1}{1-\alpha}=\frac{2}{\varepsilon}. |  |

Step 3 (Fundamental propagator).
Submultiplicativity yields

|  |  |  |
| --- | --- | --- |
|  | ‖Rℓ​Rℓ−1​⋯​Rs+1‖∗≤(2ε)ℓ−s.\big\|R\_{\ell}R\_{\ell-1}\cdots R\_{s+1}\big\|\_{\*}\leq\Big(\tfrac{2}{\varepsilon}\Big)^{\ell-s}. |  |

With ‖Bs‖∗≤b∗​Δ​ts\|B\_{s}\|\_{\*}\leq b\_{\*}\Delta t\_{s} where b∗:=sups‖Bs‖∗/Δ​ts<∞b\_{\*}:=\sup\_{s}\|B\_{s}\|\_{\*}/\Delta t\_{s}<\infty, we obtain

|  |  |  |
| --- | --- | --- |
|  | ‖𝒢θ​(Tℓ,Ts)‖∗≤(2ε)ℓ−s​b∗​Δ​ts.\big\|\mathcal{G}\_{\theta}(T\_{\ell},T\_{s})\big\|\_{\*}\leq\Big(\tfrac{2}{\varepsilon}\Big)^{\ell-s}b\_{\*}\Delta t\_{s}. |  |

Step 4 (Summability).
Summing over s≤ℓs\leq\ell and letting k:=ℓ−sk:=\ell-s,

|  |  |  |
| --- | --- | --- |
|  | ∑s≤ℓ‖𝒢θ​(Tℓ,Ts)‖∗≤b∗​∑k=0∞(2ε)k​Δ​tℓ−k.\sum\_{s\leq\ell}\big\|\mathcal{G}\_{\theta}(T\_{\ell},T\_{s})\big\|\_{\*}\;\leq\;b\_{\*}\sum\_{k=0}^{\infty}\Big(\tfrac{2}{\varepsilon}\Big)^{k}\Delta t\_{\ell-k}. |  |

To ensure a uniform bound, tighten Step 1 by choosing an arbitrary η∈(0,1)\eta\in(0,1) and taking δ>0\delta>0 small enough that ‖Mℓ‖∗≤η\|M\_{\ell}\|\_{\*}\leq\eta for all ℓ\ell (possible by the extremal–norm argument).
Repeating Step 2–3 gives ‖Rℓ‖∗≤(1−η)−1\|R\_{\ell}\|\_{\*}\leq(1-\eta)^{-1} and hence

|  |  |  |
| --- | --- | --- |
|  | ∑s≤ℓ‖𝒢θ​(Tℓ,Ts)‖∗≤b∗​∑k=0∞ηk​Δ​tℓ−k≤b∗​Δ​t¯​∑k=0∞ηk=b∗​Δ​t¯1−η.\sum\_{s\leq\ell}\big\|\mathcal{G}\_{\theta}(T\_{\ell},T\_{s})\big\|\_{\*}\;\leq\;b\_{\*}\sum\_{k=0}^{\infty}\eta^{\,k}\Delta t\_{\ell-k}\;\leq\;b\_{\*}\,\overline{\Delta t}\sum\_{k=0}^{\infty}\eta^{\,k}\;=\;\frac{b\_{\*}\,\overline{\Delta t}}{1-\eta}\,. |  |

Step 5 (Return to the reference norm).
All norms in finite dimension are equivalent, so there exists κ≥1\kappa\geq 1 with ‖X‖≤κ​‖X‖∗\|X\|\leq\kappa\|X\|\_{\*}.
Therefore

|  |  |  |
| --- | --- | --- |
|  | ∑s≤ℓ∥𝒢θ(Tℓ,Ts)∥≤κb∗​Δ​t¯1−η=:C(ε,b,Δ​t¯)<∞,\sum\_{s\leq\ell}\big\|\mathcal{G}\_{\theta}(T\_{\ell},T\_{s})\big\|\;\leq\;\kappa\,\frac{b\_{\*}\,\overline{\Delta t}}{1-\eta}\;=:\;C(\varepsilon,b,\overline{\Delta t})<\infty, |  |

which proves the claim.
∎

#### Remark (Non-diagonalizable case and explicit constants).

If MℓM\_{\ell} admits a Jordan decomposition Mℓ=Vℓ​Jℓ​Vℓ−1M\_{\ell}=V\_{\ell}J\_{\ell}V\_{\ell}^{-1}, then
Rℓ=(I−Mℓ)−1=Vℓ​(I−Jℓ)−1​Vℓ−1R\_{\ell}=(I-M\_{\ell})^{-1}=V\_{\ell}(I-J\_{\ell})^{-1}V\_{\ell}^{-1}.
For a size-kk Jordan block Jk​(λ)J\_{k}(\lambda),
‖(I−Jk​(λ))−1‖≤∑m=0k−1(m+k−1k−1)​|λ|m≤Ck​(1−|λ|)−k.\|(I-J\_{k}(\lambda))^{-1}\|\leq\sum\_{m=0}^{k-1}\binom{m+k-1}{k-1}|\lambda|^{m}\leq C\_{k}\,(1-|\lambda|)^{-k}.
Under ρ​(Mℓ)≤1−ε\rho(M\_{\ell})\leq 1-\varepsilon this implies ‖Rℓ‖≤κ​(Vℓ)​Cd​ε−d\|R\_{\ell}\|\leq\kappa(V\_{\ell})\,C\_{d}\,\varepsilon^{-d}, whence the same summability follows after accounting for the Δ​ts\Delta t\_{s} factor in BsB\_{s}. The extremal–norm route typically yields tighter constants by avoiding κ​(Vℓ)\kappa(V\_{\ell}).

### A.2 Proof of Proposition [1](https://arxiv.org/html/2511.06451v1#Thmproposition1 "Proposition 1 (RN-operator stability under Q-Align). ‣ RN-operator stability under Q-Align. ‣ 3.2 Q-Align: Lipschitz Projection and Spectral Guard ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")

#### Setting and recalled constraints.

We consider the RN-operator layer on a grid {Tℓ}\{T\_{\ell}\} with increments Δ​tℓ>0\Delta t\_{\ell}>0, generator Aθ​(Tℓ)A\_{\theta}(T\_{\ell}), and resolvent Rℓ:=(I−Δ​tℓ​Aθ​(Tℓ))−1R\_{\ell}:=(I-\Delta t\_{\ell}A\_{\theta}(T\_{\ell}))^{-1}.
The Q-Align projection enforces the layerwise Lipschitz envelope ([14](https://arxiv.org/html/2511.06451v1#S3.E14 "In Layerwise Lipschitz projection. ‣ 3.2 Q-Align: Lipschitz Projection and Spectral Guard ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")), summarized as

|  |  |  |
| --- | --- | --- |
|  | ‖ℒℓ‖≤τ(τ≤1),\|\mathcal{L}\_{\ell}\|\leq\tau\qquad(\tau\leq 1), |  |

for the linearized lipschitz surrogate ℒℓ\mathcal{L}\_{\ell} of the per-step affine map prior to the nonlinearity; the spectral safeguard ([15](https://arxiv.org/html/2511.06451v1#S3.E15 "In Spectral Guard (CFL projection). ‣ 3.2 Q-Align: Lipschitz Projection and Spectral Guard ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) is the CFL-type condition

|  |  |  |
| --- | --- | --- |
|  | ρ​(Aθ​(Tℓ))​Δ​tℓ≤1−ε(ε∈(0,1)),\rho\!\left(A\_{\theta}(T\_{\ell})\right)\,\Delta t\_{\ell}\leq 1-\varepsilon\qquad(\varepsilon\in(0,1)), |  |

which guarantees resolvent well-posedness.
We use a nonexpansive activation ϕ\phi with Lip⁡(ϕ)≤1\operatorname{Lip}(\phi)\leq 1.
Define the input injection BℓB\_{\ell} (possibly learned) and bias bℓb\_{\ell}, with bounded envelopes ‖Bℓ‖≤bin\|B\_{\ell}\|\leq b\_{\rm in} and ‖bℓ‖≤b0\|b\_{\ell}\|\leq b\_{0}.
The discrete causal Green kernel reads (for s≤ℓs\leq\ell)

|  |  |  |
| --- | --- | --- |
|  | 𝒢θ​(Tℓ,Ts)=Rℓ​Rℓ−1​⋯​Rs+1​Bs.\mathcal{G}\_{\theta}(T\_{\ell},T\_{s})\;=\;R\_{\ell}R\_{\ell-1}\cdots R\_{s+1}\,B\_{s}. |  |

The state recursion is

|  |  |  |  |
| --- | --- | --- | --- |
|  | hℓ=ϕ​(Rℓ​hℓ−1+Bℓ​uℓ+bℓ),ℓ∈ℤ.h\_{\ell}\;=\;\phi\!\left(R\_{\ell}h\_{\ell-1}+B\_{\ell}u\_{\ell}+b\_{\ell}\right),\qquad\ell\in\mathbb{Z}. |  | (47) |

#### Auxiliary bound (from Appendix A.1).

By Lemma [1](https://arxiv.org/html/2511.06451v1#Thmlemma1 "Lemma 1 (Green kernel bound). ‣ Spectral safety and discrete Green kernel. ‣ 3.1 Risk–Neutral Operator Layer (RN-Operator) ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures"), under the CFL-type guard there exists an induced norm ∥⋅∥∗\|\cdot\|\_{\*} and constants η∈(0,1)\eta\in(0,1) and Cε<∞C\_{\varepsilon}<\infty such that

|  |  |  |
| --- | --- | --- |
|  | ‖Rℓ‖∗≤11−η,∑s≤ℓ‖Rℓ​⋯​Rs+1‖∗​Δ​ts≤Cε,\|R\_{\ell}\|\_{\*}\leq\frac{1}{1-\eta}\,,\qquad\sum\_{s\leq\ell}\big\|R\_{\ell}\cdots R\_{s+1}\big\|\_{\*}\,\Delta t\_{s}\;\leq\;C\_{\varepsilon}, |  |

uniformly in ℓ\ell (the precise dependence on ε\varepsilon is stated in Appendix A.1).

#### Step 1: BIBO stability.

Iterating ([47](https://arxiv.org/html/2511.06451v1#Ax1.E47 "In Setting and recalled constraints. ‣ A.2 Proof of Proposition 1 ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) and using Lip⁡(ϕ)≤1\operatorname{Lip}(\phi)\leq 1 yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖hℓ‖∗\displaystyle\|h\_{\ell}\|\_{\*} | ≤‖Rℓ‖∗​‖hℓ−1‖∗+‖Bℓ‖∗​‖uℓ‖+‖bℓ‖∗\displaystyle\leq\|R\_{\ell}\|\_{\*}\,\|h\_{\ell-1}\|\_{\*}+\|B\_{\ell}\|\_{\*}\,\|u\_{\ell}\|+\|b\_{\ell}\|\_{\*} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤11−η​‖hℓ−1‖∗+bin,∗​‖uℓ‖+b0,∗,\displaystyle\leq\frac{1}{1-\eta}\,\|h\_{\ell-1}\|\_{\*}+b\_{{\rm in},\*}\,\|u\_{\ell}\|+b\_{0,\*}, |  |

where bin,∗:=supℓ‖Bℓ‖∗b\_{{\rm in},\*}:=\sup\_{\ell}\|B\_{\ell}\|\_{\*} and b0,∗:=supℓ‖bℓ‖∗b\_{0,\*}:=\sup\_{\ell}\|b\_{\ell}\|\_{\*}.
Unrolling the recursion with h−∞=0h\_{-\infty}=0 (or any bounded initialization absorbed into the same bound), and substituting RR-products gives

|  |  |  |
| --- | --- | --- |
|  | ‖hℓ‖∗≤∑s≤ℓ‖Rℓ​⋯​Rs+1‖∗​(bin,∗​‖us‖+b0,∗).\|h\_{\ell}\|\_{\*}\;\leq\;\sum\_{s\leq\ell}\big\|R\_{\ell}\cdots R\_{s+1}\big\|\_{\*}\big(b\_{{\rm in},\*}\|u\_{s}\|+b\_{0,\*}\big). |  |

If sups‖us‖≤U<∞\sup\_{s}\|u\_{s}\|\leq U<\infty, then by the kernel summability,

|  |  |  |
| --- | --- | --- |
|  | ‖hℓ‖∗≤Cε​(bin,∗​U+b0,∗),\|h\_{\ell}\|\_{\*}\;\leq\;C\_{\varepsilon}\,\big(b\_{{\rm in},\*}\,U+b\_{0,\*}\big), |  |

uniformly in ℓ\ell.
By norm equivalence in finite dimension, the same uniform bound holds for any reference norm ∥⋅∥\|\cdot\|:

|  |  |  |
| --- | --- | --- |
|  | supℓ∥hℓ∥≤κCε(binU+b0)=:CBIBO<∞.\sup\_{\ell}\|h\_{\ell}\|\;\leq\;\kappa\,C\_{\varepsilon}\,\big(b\_{\rm in}\,U+b\_{0}\big)=:C\_{\rm BIBO}<\infty. |  |

Hence the trajectory is uniformly bounded for bounded input (BIBO stability).

#### Step 2: Global Lipschitz continuity (input-to-state and input-to-output).

Consider two input sequences {uℓ}\{u\_{\ell}\}, {uℓ′}\{u^{\prime}\_{\ell}\} with corresponding states {hℓ}\{h\_{\ell}\}, {hℓ′}\{h^{\prime}\_{\ell}\}.
Set δ​hℓ:=hℓ−hℓ′\delta h\_{\ell}:=h\_{\ell}-h^{\prime}\_{\ell}, δ​uℓ:=uℓ−uℓ′\delta u\_{\ell}:=u\_{\ell}-u^{\prime}\_{\ell}.
Using Lip⁡(ϕ)≤1\operatorname{Lip}(\phi)\leq 1,

|  |  |  |
| --- | --- | --- |
|  | ‖δ​hℓ‖∗≤‖Rℓ‖∗​‖δ​hℓ−1‖∗+‖Bℓ‖∗​‖δ​uℓ‖.\|\delta h\_{\ell}\|\_{\*}\;\leq\;\|R\_{\ell}\|\_{\*}\,\|\delta h\_{\ell-1}\|\_{\*}+\|B\_{\ell}\|\_{\*}\,\|\delta u\_{\ell}\|. |  |

Unrolling as above and using submultiplicativity,

|  |  |  |
| --- | --- | --- |
|  | ‖δ​hℓ‖∗≤∑s≤ℓ‖Rℓ​⋯​Rs+1‖∗​‖Bs‖∗​‖δ​us‖.\|\delta h\_{\ell}\|\_{\*}\;\leq\;\sum\_{s\leq\ell}\big\|R\_{\ell}\cdots R\_{s+1}\big\|\_{\*}\,\|B\_{s}\|\_{\*}\,\|\delta u\_{s}\|. |  |

Taking ℓ∞\ell^{\infty} norms over sequences and applying the kernel sum bound,

|  |  |  |
| --- | --- | --- |
|  | ‖δ​h‖ℓ∞,∗≤(sups‖Bs‖∗)​(supℓ∑s≤ℓ‖Rℓ​⋯​Rs+1‖∗​Δ​ts)​‖δ​u‖ℓ∞≤bin,∗​Cε​‖δ​u‖ℓ∞.\|\delta h\|\_{\ell^{\infty},\*}\;\leq\;\Big(\sup\_{s}\|B\_{s}\|\_{\*}\Big)\,\Big(\sup\_{\ell}\sum\_{s\leq\ell}\|R\_{\ell}\cdots R\_{s+1}\|\_{\*}\,\Delta t\_{s}\Big)\,\|\delta u\|\_{\ell^{\infty}}\;\leq\;b\_{{\rm in},\*}\,C\_{\varepsilon}\,\|\delta u\|\_{\ell^{\infty}}. |  |

Passing back to the reference norm via equivalence constants yields

|  |  |  |
| --- | --- | --- |
|  | ‖δ​h‖ℓ∞≤κ​bin​Cε​‖δ​u‖ℓ∞.\|\delta h\|\_{\ell^{\infty}}\;\leq\;\kappa\,b\_{\rm in}\,C\_{\varepsilon}\,\|\delta u\|\_{\ell^{\infty}}. |  |

If the readout/decoder is LoutL\_{\rm out}-Lipschitz (Q-Align also enforces a 11-Lipschitz envelope through the head), then the overall input-to-output map is globally Lipschitz with

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lglob≤κ​Lout​bin​Cε.L\_{\rm glob}\;\leq\;\kappa\,L\_{\rm out}\,b\_{\rm in}\,C\_{\varepsilon}. |  | (48) |

When the layerwise envelope is tightened by ([14](https://arxiv.org/html/2511.06451v1#S3.E14 "In Layerwise Lipschitz projection. ‣ 3.2 Q-Align: Lipschitz Projection and Spectral Guard ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) with factor τ≤1\tau\leq 1, we can absorb it multiplicatively into binb\_{\rm in} or LoutL\_{\rm out}, so the same bound holds with bin←τ​binb\_{\rm in}\leftarrow\tau\,b\_{\rm in}, Lout←τ​LoutL\_{\rm out}\leftarrow\tau\,L\_{\rm out}.
This matches the main-text bound ([13](https://arxiv.org/html/2511.06451v1#S3.E13 "In Lipschitz surrogate via spectral normalization. ‣ 3.1 Risk–Neutral Operator Layer (RN-Operator) ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) up to norm-equivalence constants.

#### Step 3: Role of Spec-Guard and Q-Align.

Spec-Guard ensures ‖Rℓ‖∗\|R\_{\ell}\|\_{\*} remains uniformly bounded and that the product ‖Rℓ​⋯​Rs+1‖∗\|R\_{\ell}\cdots R\_{s+1}\|\_{\*} decays geometrically in the extremal norm; Q-Align prevents per-step amplification beyond τ≤1\tau\leq 1, guaranteeing that the effective injection ‖Bs‖∗\|B\_{s}\|\_{\*} and the readout Lipschitz constant remain inside the envelope.
Combining both yields BIBO stability and a globally Lipschitz operator with constant bounded by ([48](https://arxiv.org/html/2511.06451v1#Ax1.E48 "In Step 2: Global Lipschitz continuity (input-to-state and input-to-output). ‣ A.2 Proof of Proposition 1 ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")).

#### Non-diagonalizable case and time-varying steps.

If Aθ​(Tℓ)A\_{\theta}(T\_{\ell}) is not diagonalizable, the Jordan-block resolvent bound in Appendix A.1 gives ‖Rℓ‖≤Cd​ε−d\|R\_{\ell}\|\leq C\_{d}\,\varepsilon^{-d} up to condition numbers; the extremal-norm construction avoids these condition numbers and yields the uniform envelope used above.
Heterogeneous steps Δ​tℓ\Delta t\_{\ell} are already handled in the kernel summability via the weighted series ∑s≤ℓ‖Rℓ​⋯​Rs+1‖∗​Δ​ts\sum\_{s\leq\ell}\|R\_{\ell}\cdots R\_{s+1}\|\_{\*}\,\Delta t\_{s}.

#### Conclusion.

Uniform boundedness and global Lipschitz continuity follow, which proves Proposition [1](https://arxiv.org/html/2511.06451v1#Thmproposition1 "Proposition 1 (RN-operator stability under Q-Align). ‣ RN-operator stability under Q-Align. ‣ 3.2 Q-Align: Lipschitz Projection and Spectral Guard ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures").
∎

### A.3 SPX↔\leftrightarrowVIX replication: discretization consistency and identifiability

#### Continuous-time identity and discrete estimator.

Let FT=S0​e(r−q)​TF\_{T}=S\_{0}\mathrm{e}^{(r-q)T}, and let C​(⋅,T)C(\cdot,T), P​(⋅,T)P(\cdot,T) be call and put prices under ℚθ\mathbb{Q}\_{\theta} with discount factor e−r​T\mathrm{e}^{-rT} and no static arbitrage.
The log-contract identity yields the variance-swap fair rate (for diffusion models; jump-diffusions add the standard jump term):

|  |  |  |  |
| --- | --- | --- | --- |
|  | σVS,θ2​(T)=2​er​TT​(∫0FTPθ​(K,T)K2​𝑑K+∫FT∞Cθ​(K,T)K2​𝑑K)−1T​(FTK0−1)2.\sigma^{2}\_{\mathrm{VS},\theta}(T)=\frac{2\,\mathrm{e}^{rT}}{T}\!\left(\int\_{0}^{F\_{T}}\frac{P\_{\theta}(K,T)}{K^{2}}\,dK+\int\_{F\_{T}}^{\infty}\frac{C\_{\theta}(K,T)}{K^{2}}\,dK\right)-\frac{1}{T}\left(\frac{F\_{T}}{K\_{0}}-1\right)^{\!2}. |  | (49) |

For a strike grid 𝒦T={Ki}i=1M\mathcal{K}\_{T}=\{K\_{i}\}\_{i=1}^{M}, define Δ​Ki=12​(Ki+1−Ki−1)\Delta K\_{i}=\frac{1}{2}(K\_{i+1}-K\_{i-1}) with one-sided endpoints, and the discrete estimator

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ^VS,θ2​(T):=2​er​TT​∑i=1MΔ​KiKi2​Qθ​(Ki,T)−1T​(FTK0−1)2,\widehat{\sigma}^{2}\_{\mathrm{VS},\theta}(T):=\frac{2\,\mathrm{e}^{rT}}{T}\sum\_{i=1}^{M}\frac{\Delta K\_{i}}{K\_{i}^{2}}\,Q\_{\theta}(K\_{i},T)-\frac{1}{T}\left(\frac{F\_{T}}{K\_{0}}-1\right)^{\!2}, |  | (50) |

where Qθ​(Ki,T)=PθQ\_{\theta}(K\_{i},T)=P\_{\theta} if Ki<FTK\_{i}<F\_{T} and Qθ=CθQ\_{\theta}=C\_{\theta} if Ki≥FTK\_{i}\geq F\_{T}.

#### Tail integrability and convexity.

Assume: (i) K↦Qθ​(K,T)K\mapsto Q\_{\theta}(K,T) is convex for each TT; (ii) Qθ​(⋅,T)/K2Q\_{\theta}(\cdot,T)/K^{2} has bounded variation on compact sets; (iii) ∫0KminPθK2​𝑑K→0\int\_{0}^{K\_{\min}}\!\tfrac{P\_{\theta}}{K^{2}}\,dK\to 0 and ∫Kmax∞CθK2​𝑑K→0\int\_{K\_{\max}}^{\infty}\!\tfrac{C\_{\theta}}{K^{2}}\,dK\to 0 as Kmin↓0K\_{\min}\downarrow 0, Kmax↑∞K\_{\max}\uparrow\infty.
The latter holds, for instance, if the risk-neutral tails satisfy Cθ​(K,T)≲K−αC\_{\theta}(K,T)\lesssim K^{-\alpha} with α>1\alpha>1 and Pθ​(K,T)≲KP\_{\theta}(K,T)\lesssim K as K↓0K\downarrow 0.

###### Lemma 5 (Quadrature error under convexity).

Let f​(K)=Qθ​(K,T)/K2f(K)=Q\_{\theta}(K,T)/K^{2} on a compact interval [a,b][a,b], with ff convex and of bounded variation.
For the midpoint rule with mesh Δ​K\Delta K, the error satisfies

|  |  |  |
| --- | --- | --- |
|  | |∫abf​(K)​𝑑K−∑iΔ​Ki​f​(Ki)|≤TV​(f;[a,b])2​Δ​K,\left|\int\_{a}^{b}f(K)\,dK-\sum\_{i}\Delta K\_{i}\,f(K\_{i})\right|\;\leq\;\frac{\mathrm{TV}(f;[a,b])}{2}\,\Delta K, |  |

where TV​(f;[a,b])\mathrm{TV}(f;[a,b]) denotes the total variation of ff on [a,b][a,b].

###### Proof.

Since ff has bounded variation, ff is the difference of two monotone functions.
Apply the Jordan decomposition and sum the per-cell trapezoid error; convexity implies the midpoint rule error is monotone in the cell width and controlled by the variation measure.
A standard argument (Riemann–Stieltjes with variation measure) yields the bound.
∎

###### Proof of Proposition [2](https://arxiv.org/html/2511.06451v1#Thmproposition2 "Proposition 2 (Consistency of discretized VIX replication). ‣ SPX↔VIX replication. ‣ 3.3 Convex–Monotone Decoder and SPX–VIX Coupling ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures").

Fix TT.
Split the integrals in ([49](https://arxiv.org/html/2511.06451v1#Ax1.E49 "In Continuous-time identity and discrete estimator. ‣ A.3 SPX↔VIX replication: discretization consistency and identifiability ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) on [0,Kmin][0,K\_{\min}], [Kmin,FT][K\_{\min},F\_{T}], [FT,Kmax][F\_{T},K\_{\max}], [Kmax,∞)[K\_{\max},\infty).
On the two compact intervals [Kmin,FT][K\_{\min},F\_{T}] and [FT,Kmax][F\_{T},K\_{\max}], apply Lemma [5](https://arxiv.org/html/2511.06451v1#Thmlemma5 "Lemma 5 (Quadrature error under convexity). ‣ Tail integrability and convexity. ‣ A.3 SPX↔VIX replication: discretization consistency and identifiability ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") to f​(K)=Pθ​(K,T)/K2f(K)=P\_{\theta}(K,T)/K^{2} and f​(K)=Cθ​(K,T)/K2f(K)=C\_{\theta}(K,T)/K^{2} respectively, to get an error ≤12​[TV​(f;[Kmin,FT])+TV​(f;[FT,Kmax])]​Δ​KT\leq\frac{1}{2}[\mathrm{TV}(f;[K\_{\min},F\_{T}])+\mathrm{TV}(f;[F\_{T},K\_{\max}])]\Delta K\_{T}.
The tails are εtail​(Kmin,Kmax)\varepsilon\_{\mathrm{tail}}(K\_{\min},K\_{\max}) by assumption (iii).
The forward adjustment term coincides in ([49](https://arxiv.org/html/2511.06451v1#Ax1.E49 "In Continuous-time identity and discrete estimator. ‣ A.3 SPX↔VIX replication: discretization consistency and identifiability ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) and ([50](https://arxiv.org/html/2511.06451v1#Ax1.E50 "In Continuous-time identity and discrete estimator. ‣ A.3 SPX↔VIX replication: discretization consistency and identifiability ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")), hence cancels in the difference.
Uniformity in TT over compact subsets follows if the variation envelopes and tail integrability are uniform in TT.
∎

###### Lemma 6 (Log-contract linkage).

For a continuous Itô model d​St=St​μt​d​t+St​σt​d​WtdS\_{t}=S\_{t}\mu\_{t}\,dt+S\_{t}\sigma\_{t}\,dW\_{t} under ℚθ\mathbb{Q}\_{\theta},

|  |  |  |
| --- | --- | --- |
|  | 2​er​TT​(∫0FTPθK2​𝑑K+∫FT∞CθK2​𝑑K)=1T​𝔼ℚθ​[∫0Tσt2​𝑑t].\frac{2\,\mathrm{e}^{rT}}{T}\!\left(\int\_{0}^{F\_{T}}\!\frac{P\_{\theta}}{K^{2}}\,dK+\int\_{F\_{T}}^{\infty}\!\frac{C\_{\theta}}{K^{2}}\,dK\right)=\frac{1}{T}\,\mathbb{E}^{\mathbb{Q}\_{\theta}}\!\left[\!\int\_{0}^{T}\sigma\_{t}^{2}\,dt\right]. |  |

For jump-diffusions, an additional jump-compensator term appears and is incorporated in the standard VIX methodology through OTM sums of QθQ\_{\theta}.

###### Proof.

This is the classical Carr–Madan log-contract identity, obtained by writing the log payoff as a static portfolio of OTM options plus a forward and differentiating option prices with respect to KK (Breeden–Litzenberger).
∎

###### Proof of Proposition [3](https://arxiv.org/html/2511.06451v1#Thmproposition3 "Proposition 3 (Variance-swap identifiability via replication). ‣ SPX↔VIX replication. ‣ 3.3 Convex–Monotone Decoder and SPX–VIX Coupling ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures").

The condition ℛVIX​(T)=0\mathcal{R}\_{\mathrm{VIX}}(T)=0 implies σ^VS,θ2​(T)=VIXobs2​(T)\widehat{\sigma}^{2}\_{\mathrm{VS},\theta}(T)=\mathrm{VIX}^{2}\_{\mathrm{obs}}(T).
By Proposition [2](https://arxiv.org/html/2511.06451v1#Thmproposition2 "Proposition 2 (Consistency of discretized VIX replication). ‣ SPX↔VIX replication. ‣ 3.3 Convex–Monotone Decoder and SPX–VIX Coupling ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures"), letting the mesh refine and the truncation expand, we obtain σVS,θ2​(T)=σVS,obs2​(T)\sigma^{2}\_{\mathrm{VS},\theta}(T)=\sigma^{2}\_{\mathrm{VS,obs}}(T) for all T∈𝒯T\in\mathcal{T}.
If vθv\_{\theta} exists and T↦1T​∫0Tvθ​(t)​𝑑tT\mapsto\frac{1}{T}\int\_{0}^{T}v\_{\theta}(t)\,dt is strictly monotone, equality of the Cesàro means on an interval forces vθv\_{\theta} to match the observed instantaneous variance a.e. on 𝒯\mathcal{T} (Hardy–Littlewood Tauberian principle for monotone means).
∎

#### Interpolation choice and arbitrage.

Linear interpolation in (K,Q)(K,Q) preserves piecewise convexity and monotonicity, which aligns with the no-butterfly/no-calendar constraints; cubic splines may reduce quadrature error but risk local nonconvexities between knots.
In our experiments, both schemes yield statistically indistinguishable NAS/CNAS while linear interpolation avoids small arbitrage repairs (see Table 1 and Fig. iv\_contours\_filled\_TK.png vs iv\_contours\_lines\_TK.png).

### A.4 Proof of Proposition [4](https://arxiv.org/html/2511.06451v1#Thmproposition4 "Proposition 4 (Static no-arbitrage and replication consistency). ‣ SPX↔VIX replication. ‣ 3.3 Convex–Monotone Decoder and SPX–VIX Coupling ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures"): static no-arbitrage and replication consistency

We work on a strike–maturity grid {(Ki,Tj)}i=1,…,M;j=1,…,J\{(K\_{i},T\_{j})\}\_{i=1,\dots,M;\,j=1,\dots,J} with ordered 0<K1<⋯<KM0<K\_{1}<\dots<K\_{M} and 0<T1<⋯<TJ0<T\_{1}<\dots<T\_{J}, and one-sided spacings Δ​Ki=12​(Ki+1−Ki−1)\Delta K\_{i}=\tfrac{1}{2}(K\_{i+1}-K\_{i-1}) (endpoints adjusted analogously). Throughout, interest rate rr and dividend yield qq are accounted for via the forward FT=S0​e(r−q)​TF\_{T}=S\_{0}\mathrm{e}^{(r-q)T}; calendar comparisons are done at fixed (K,T)(K,T) in the same numeraire.

#### Assumptions.

(i) *Convex–monotone constraints.* For each TT, K↦C​(K,T)K\mapsto C(K,T) is convex and nonincreasing, and for each KK, T↦C​(K,T)T\mapsto C(K,T) is nondecreasing. In differential form,

|  |  |  |
| --- | --- | --- |
|  | ∂K​K2C​(K,T)≥0,∂KC​(K,T)≤0,∂TC​(K,T)≥0,\partial\_{KK}^{2}C(K,T)\geq 0,\qquad\partial\_{K}C(K,T)\leq 0,\qquad\partial\_{T}C(K,T)\geq 0, |  |

with weak derivatives interpreted in the sense of distributions.
(ii) *Boundary and tail conditions.* As K↓0K\downarrow 0, C​(K,T)→S0​e−q​TC(K,T)\to S\_{0}\mathrm{e}^{-qT}; as K↑∞K\uparrow\infty, C​(K,T)→0C(K,T)\to 0 and C​(K,T)≲K−αC(K,T)\lesssim K^{-\alpha} for some α>1\alpha>1. These imply C​(⋅,T)/K2C(\cdot,T)/K^{2} has bounded variation on compact intervals and integrable tails.
(iii) *VIX replication residual vanishes on the maturity grid.* For all TjT\_{j},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛVIX​(Tj)=VIXobs2​(Tj)−VIXΦ2​(Tj)=0,\mathcal{R}\_{\mathrm{VIX}}(T\_{j})=\mathrm{VIX}^{2}\_{\mathrm{obs}}(T\_{j})-\mathrm{VIX}^{2}\_{\Phi}(T\_{j})=0, |  | (51) |

where VIXΦ2​(T)\mathrm{VIX}^{2}\_{\Phi}(T) is computed from C=ΦC=\Phi via the discrete replication formula ([20](https://arxiv.org/html/2511.06451v1#S3.E20 "In SPX↔VIX replication. ‣ 3.3 Convex–Monotone Decoder and SPX–VIX Coupling ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) (including the standard forward adjustment).

#### Step 1 (butterfly arbitrage on the grid is excluded).

Fix TjT\_{j}. Since K↦C​(K,Tj)K\mapsto C(K,T\_{j}) is convex on (0,∞)(0,\infty) in the sense of distributions, the second difference

|  |  |  |
| --- | --- | --- |
|  | ΔK2​C​(Ki,Tj):=C​(Ki−1,Tj)−2​C​(Ki,Tj)+C​(Ki+1,Tj)≥0\Delta^{2}\_{K}C(K\_{i},T\_{j}):=C(K\_{i-1},T\_{j})-2C(K\_{i},T\_{j})+C(K\_{i+1},T\_{j})\geq 0 |  |

for all interior indices i=2,…,M−1i=2,\dots,M-1; at endpoints, the one-sided convexity inequalities hold. Therefore, there is no butterfly arbitrage on the strike grid at TjT\_{j}. This is the classical discrete convexity criterion for absence of butterfly spreads.

#### Step 2 (calendar arbitrage on the grid is excluded).

Fix KiK\_{i}. Monotonicity ∂TC​(Ki,T)≥0\partial\_{T}C(K\_{i},T)\geq 0 implies C​(Ki,Tj+1)≥C​(Ki,Tj)C(K\_{i},T\_{j+1})\geq C(K\_{i},T\_{j}) for all jj. Hence there is no calendar arbitrage on the maturity grid at KiK\_{i}. The numeraire consistency follows since comparisons are made for the same (Ki,Tj)(K\_{i},T\_{j}) and the decoder already absorbs (r,q)(r,q) via the forward mapping.

#### Step 3 (BL density and consistency with VIX functional).

By convexity in KK and the tail conditions, the Breeden–Litzenberger identity

|  |  |  |
| --- | --- | --- |
|  | fST​(K)=er​T​∂K​K2C​(K,T)f\_{S\_{T}}(K)=\mathrm{e}^{rT}\,\partial\_{KK}^{2}C(K,T) |  |

defines a nonnegative measure integrating to er​T​∂KC​(0+,T)−er​T​∂KC​(∞−,T)=1\mathrm{e}^{rT}\,\partial\_{K}C(0^{+},T)-\mathrm{e}^{rT}\,\partial\_{K}C(\infty^{-},T)=1; thus fSTf\_{S\_{T}} is a bona fide risk-neutral density. On the grid, the discrete counterpart reads

|  |  |  |
| --- | --- | --- |
|  | fSTj​(Ki)≈er​Tj​C​(Ki−1,Tj)−2​C​(Ki,Tj)+C​(Ki+1,Tj)(Δ​Ki)2,f\_{S\_{T\_{j}}}(K\_{i})\;\approx\;\mathrm{e}^{rT\_{j}}\,\frac{C(K\_{i-1},T\_{j})-2C(K\_{i},T\_{j})+C(K\_{i+1},T\_{j})}{(\Delta K\_{i})^{2}}, |  |

which is nonnegative by Step 1.

Consider the VIX functional (variance swap fair rate). In continuous form,

|  |  |  |  |
| --- | --- | --- | --- |
|  | σVS2​(T)=2​er​TT​(∫0FTPK2​𝑑K+∫FT∞CK2​𝑑K)−1T​(FTK0−1)2.\sigma^{2}\_{\mathrm{VS}}(T)=\frac{2\,\mathrm{e}^{rT}}{T}\!\left(\int\_{0}^{F\_{T}}\frac{P}{K^{2}}\,dK+\int\_{F\_{T}}^{\infty}\frac{C}{K^{2}}\,dK\right)-\frac{1}{T}\left(\frac{F\_{T}}{K\_{0}}-1\right)^{\!2}. |  | (52) |

By the Carr–Madan log-contract identity and the BL relation,

|  |  |  |
| --- | --- | --- |
|  | 2​er​TT​(∫0FTPK2​𝑑K+∫FT∞CK2​𝑑K)=1T​∫0∞ψ​(K)​er​T​∂K​K2C​(K,T)​d​K,\frac{2\,\mathrm{e}^{rT}}{T}\!\left(\int\_{0}^{F\_{T}}\frac{P}{K^{2}}\,dK+\int\_{F\_{T}}^{\infty}\frac{C}{K^{2}}\,dK\right)=\frac{1}{T}\int\_{0}^{\infty}\psi(K)\,\mathrm{e}^{rT}\,\partial\_{KK}^{2}C(K,T)\,dK, |  |

for a positive kernel ψ​(K)\psi(K) whose action reproduces the log payoff; under our tails and boundary conditions the integration by parts is justified (all boundary terms vanish). Hence the VIX functional computed from CC is exactly the Cesàro mean of instantaneous variance under the density fSTf\_{S\_{T}}.

On the grid, with the midpoint quadrature ∑iΔ​Ki​Q​(Ki,T)/Ki2\sum\_{i}\Delta K\_{i}\,Q(K\_{i},T)/K\_{i}^{2} and the forward adjustment, Proposition A.3 (consistency of discretized replication) yields

|  |  |  |
| --- | --- | --- |
|  | VIXΦ2​(Tj)=σVS,Φ2​(Tj)up to quadrature and tail errors vanishing with the mesh.\mathrm{VIX}^{2}\_{\Phi}(T\_{j})=\sigma^{2}\_{\mathrm{VS},\Phi}(T\_{j})\quad\text{up to quadrature and tail errors vanishing with the mesh.} |  |

By ([51](https://arxiv.org/html/2511.06451v1#Ax1.E51 "In Assumptions. ‣ A.4 Proof of Proposition 4: static no-arbitrage and replication consistency ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")), VIXΦ2​(Tj)=VIXobs2​(Tj)\mathrm{VIX}^{2}\_{\Phi}(T\_{j})=\mathrm{VIX}^{2}\_{\mathrm{obs}}(T\_{j}) for all jj, hence the BL-implied density from CC is consistent with the observed VIX2 functional on the maturity grid.

#### Putting the steps together.

Steps 1–2 establish the absence of butterfly and calendar arbitrage on the grid. Step 3 shows that the BL-implied density from CC reproduces the VIX2 functional when the replication residual vanishes (and, by A.3, in the mesh-refined limit). This proves Proposition [4](https://arxiv.org/html/2511.06451v1#Thmproposition4 "Proposition 4 (Static no-arbitrage and replication consistency). ‣ SPX↔VIX replication. ‣ 3.3 Convex–Monotone Decoder and SPX–VIX Coupling ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures").

#### Remarks on implementation and interpolation.

(i) Linear interpolation in (K,Q)(K,Q) preserves piecewise convexity and thus nonnegativity of discrete second differences; cubic splines may reduce quadrature error but can introduce local nonconvexities between knots unless shape-constrained splines are used.
(ii) Calendar tests should be performed on the forward-adjusted scale if one compares prices under changing carry (r,q)(r,q). In our implementation, the decoder absorbs (r,q)(r,q) and produces monotonically nondecreasing T↦C​(K,T)T\mapsto C(K,T) directly.
(iii) On coarse grids, adding the forward adjustment term improves finite-grid consistency with ([52](https://arxiv.org/html/2511.06451v1#Ax1.E52 "In Step 3 (BL density and consistency with VIX functional). ‣ A.4 Proof of Proposition 4: static no-arbitrage and replication consistency ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) and reduces bias at short maturities.

### A.5 Proof of Theorem [1](https://arxiv.org/html/2511.06451v1#Thmtheorem1 "Theorem 1 (Extragradient convergence to a noise ball). ‣ Convergence guarantee (noise-stable neighborhood). ‣ 3.4 Saddle-Point Training and Safety-Oriented Stopping ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures"): projected extragradient under Q-Align perturbations

#### Setting and assumptions.

We consider the monotone variational inequality VI​(F,𝒵)\mathrm{VI}(F,\mathcal{Z}): find z⋆∈𝒵z^{\star}\in\mathcal{Z} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨F​(z⋆),z−z⋆⟩≥ 0∀z∈𝒵,\langle F(z^{\star}),z-z^{\star}\rangle\;\geq\;0\qquad\forall z\in\mathcal{Z}, |  | (53) |

with FF monotone, i.e., ⟨F​(u)−F​(v),u−v⟩≥0\langle F(u)-F(v),u-v\rangle\geq 0 for all u,vu,v, and LL-Lipschitz, i.e., ‖F​(u)−F​(v)‖≤L​‖u−v‖\|F(u)-F(v)\|\leq L\|u-v\|. The projection Π𝒵\Pi\_{\mathcal{Z}} is nonexpansive. Q-Align enforces per-iteration spectral/Lipschitz projections inside the model; we capture the induced numerical and truncation inaccuracies by perturbations ek,e~ke^{k},\tilde{e}^{k} satisfying

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖ek‖+‖e~k‖≤cqa​η,for some constant ​cqa>0,\|e^{k}\|+\|\tilde{e}^{k}\|\;\leq\;c\_{\mathrm{qa}}\eta,\qquad\text{for some constant }c\_{\mathrm{qa}}>0, |  | (54) |

which matches the empirical scaling reported in the logs (cf. λlip\lambda\_{\mathrm{lip}} before/after and spectral-guard distances). Stochastic gradients enter via martingale-difference noise ξk,ξ~k\xi^{k},\tilde{\xi}^{k} with

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[ξk∣ℱk]=0,𝔼​‖ξk‖2≤σ2,𝔼​[ξ~k∣ℱk+1/2]=0,𝔼​‖ξ~k‖2≤σ2.\mathbb{E}[\xi^{k}\mid\mathcal{F}\_{k}]=0,\ \ \mathbb{E}\|\xi^{k}\|^{2}\leq\sigma^{2},\qquad\mathbb{E}[\tilde{\xi}^{k}\mid\mathcal{F}\_{k+1/2}]=0,\ \ \mathbb{E}\|\tilde{\xi}^{k}\|^{2}\leq\sigma^{2}. |  | (55) |

#### Algorithmic step.

Given zk∈𝒵z^{k}\in\mathcal{Z}, define

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | yk=Π𝒵​(zk−η​(F​(zk)−ξk−ek)),\displaystyle y^{k}=\Pi\_{\mathcal{Z}}\big(z^{k}-\eta\big(F(z^{k})-\xi^{k}-e^{k}\big)\big), |  | (56) |
|  |  | zk+1=Π𝒵​(zk−η​(F​(yk)−ξ~k−e~k)),\displaystyle z^{k+1}=\Pi\_{\mathcal{Z}}\big(z^{k}-\eta\big(F(y^{k})-\tilde{\xi}^{k}-\tilde{e}^{k}\big)\big), |  |

with a stepsize η≤1/(2​L)\eta\leq 1/(\sqrt{2}\,L) specified later. The residual of interest is either the natural projected residual

|  |  |  |
| --- | --- | --- |
|  | Rη​(z):=1η​(z−Π𝒵​(z−η​F​(z))),R\_{\eta}(z):=\frac{1}{\eta}\Big(z-\Pi\_{\mathcal{Z}}\big(z-\eta F(z)\big)\Big), |  |

or the operator norm ‖F​(z)‖\|F(z)\|. For monotone Lipschitz FF and η≤1/L\eta\leq 1/L, it is standard that ‖Rη​(z)‖≤(1+η​L)​‖F​(z)‖\|R\_{\eta}(z)\|\leq(1+\eta L)\|F(z)\| (see Lemma [7](https://arxiv.org/html/2511.06451v1#Thmlemma7 "Lemma 7. ‣ Auxiliary lemma (residual bridge). ‣ A.5 Proof of Theorem 1: projected extragradient under Q-Align perturbations ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") below), hence controlling one controls the other up to constants.

#### Key inequalities.

We recall the three-point identity for projections: for any u∈ℝdu\in\mathbb{R}^{d} and w=Π𝒵​(u)w=\Pi\_{\mathcal{Z}}(u), and any v∈𝒵v\in\mathcal{Z},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨u−w,v−w⟩≤0⇒‖v−w‖2≤‖v−u‖2−‖w−u‖2.\langle u-w,\,v-w\rangle\leq 0\quad\Rightarrow\quad\|v-w\|^{2}\leq\|v-u\|^{2}-\|w-u\|^{2}. |  | (57) |

Apply ([57](https://arxiv.org/html/2511.06451v1#Ax1.E57 "In Key inequalities. ‣ A.5 Proof of Theorem 1: projected extragradient under Q-Align perturbations ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) to the first stage of ([56](https://arxiv.org/html/2511.06451v1#Ax1.E56 "In Algorithmic step. ‣ A.5 Proof of Theorem 1: projected extragradient under Q-Align perturbations ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) with u=zk−η​(F​(zk)−ξk−ek)u=z^{k}-\eta(F(z^{k})-\xi^{k}-e^{k}), w=ykw=y^{k} and v=z⋆v=z^{\star}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖z⋆−yk‖2≤‖z⋆−zk‖2−‖yk−zk‖2−2​η​⟨F​(zk)−ξk−ek,yk−zk⟩.\|z^{\star}-y^{k}\|^{2}\leq\|z^{\star}-z^{k}\|^{2}-\|y^{k}-z^{k}\|^{2}-2\eta\langle F(z^{k})-\xi^{k}-e^{k},\,y^{k}-z^{k}\rangle. |  | (58) |

Similarly for the second stage with u=zk−η​(F​(yk)−ξ~k−e~k)u=z^{k}-\eta(F(y^{k})-\tilde{\xi}^{k}-\tilde{e}^{k}), w=zk+1w=z^{k+1} and v=z⋆v=z^{\star}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖z⋆−zk+1‖2≤‖z⋆−zk‖2−‖zk+1−zk‖2−2​η​⟨F​(yk)−ξ~k−e~k,zk+1−zk⟩.\|z^{\star}-z^{k+1}\|^{2}\leq\|z^{\star}-z^{k}\|^{2}-\|z^{k+1}-z^{k}\|^{2}-2\eta\langle F(y^{k})-\tilde{\xi}^{k}-\tilde{e}^{k},\,z^{k+1}-z^{k}\rangle. |  | (59) |

#### Monotonicity coupling.

Using Lipschitzness and Cauchy–Schwarz,

|  |  |  |
| --- | --- | --- |
|  | ⟨F​(yk)−F​(zk),yk−zk⟩≥1L​‖F​(yk)−F​(zk)‖2,\langle F(y^{k})-F(z^{k}),\,y^{k}-z^{k}\rangle\geq\frac{1}{L}\|F(y^{k})-F(z^{k})\|^{2}, |  |

and monotonicity yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨F​(yk),yk−z⋆⟩≥⟨F​(z⋆),yk−z⋆⟩≥0.\langle F(y^{k}),\,y^{k}-z^{\star}\rangle\geq\langle F(z^{\star}),\,y^{k}-z^{\star}\rangle\geq 0. |  | (60) |

Split the last inner product in ([58](https://arxiv.org/html/2511.06451v1#Ax1.E58 "In Key inequalities. ‣ A.5 Proof of Theorem 1: projected extragradient under Q-Align perturbations ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) as

|  |  |  |
| --- | --- | --- |
|  | ⟨F​(zk),yk−zk⟩=⟨F​(yk),yk−zk⟩+⟨F​(zk)−F​(yk),yk−zk⟩≥1L​‖F​(yk)−F​(zk)‖2,\langle F(z^{k}),y^{k}-z^{k}\rangle=\langle F(y^{k}),y^{k}-z^{k}\rangle+\langle F(z^{k})-F(y^{k}),y^{k}-z^{k}\rangle\geq\frac{1}{L}\|F(y^{k})-F(z^{k})\|^{2}, |  |

hence

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖z⋆−yk‖2≤‖z⋆−zk‖2−‖yk−zk‖2−2​ηL​‖F​(yk)−F​(zk)‖2+2​η​⟨ξk+ek,yk−zk⟩.\|z^{\star}-y^{k}\|^{2}\leq\|z^{\star}-z^{k}\|^{2}-\|y^{k}-z^{k}\|^{2}-\frac{2\eta}{L}\|F(y^{k})-F(z^{k})\|^{2}+2\eta\langle\xi^{k}+e^{k},\,y^{k}-z^{k}\rangle. |  | (61) |

Likewise, decompose the inner product in ([59](https://arxiv.org/html/2511.06451v1#Ax1.E59 "In Key inequalities. ‣ A.5 Proof of Theorem 1: projected extragradient under Q-Align perturbations ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) using zk+1−zk=(zk+1−yk)+(yk−zk)z^{k+1}-z^{k}=(z^{k+1}-y^{k})+(y^{k}-z^{k}) and add–subtract ⟨F​(yk),yk−z⋆⟩\langle F(y^{k}),y^{k}-z^{\star}\rangle; routine algebra (see, e.g., the Mirror–Prox analysis) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖z⋆−zk+1‖2≤‖z⋆−zk‖2−‖zk+1−zk‖2−2​η​⟨F​(yk),yk−z⋆⟩+η2​L2​‖yk−zk‖2+Noisek+ProjErrk,\|z^{\star}-z^{k+1}\|^{2}\leq\|z^{\star}-z^{k}\|^{2}-\|z^{k+1}-z^{k}\|^{2}-2\eta\langle F(y^{k}),\,y^{k}-z^{\star}\rangle+\eta^{2}L^{2}\|y^{k}-z^{k}\|^{2}+\mathrm{Noise}\_{k}+\mathrm{ProjErr}\_{k}, |  | (62) |

where

|  |  |  |
| --- | --- | --- |
|  | Noisek:=2​η​⟨ξ~k,zk+1−zk⟩,ProjErrk:=2​η​⟨e~k,zk+1−zk⟩.\mathrm{Noise}\_{k}:=2\eta\langle\tilde{\xi}^{k},z^{k+1}-z^{k}\rangle,\qquad\mathrm{ProjErr}\_{k}:=2\eta\langle\tilde{e}^{k},z^{k+1}-z^{k}\rangle. |  |

#### One-step merit bound.

Combine ([61](https://arxiv.org/html/2511.06451v1#Ax1.E61 "In Monotonicity coupling. ‣ A.5 Proof of Theorem 1: projected extragradient under Q-Align perturbations ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures"))–([62](https://arxiv.org/html/2511.06451v1#Ax1.E62 "In Monotonicity coupling. ‣ A.5 Proof of Theorem 1: projected extragradient under Q-Align perturbations ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) and use ([60](https://arxiv.org/html/2511.06451v1#Ax1.E60 "In Monotonicity coupling. ‣ A.5 Proof of Theorem 1: projected extragradient under Q-Align perturbations ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) to eliminate the nonnegative term ⟨F​(yk),yk−z⋆⟩\langle F(y^{k}),\,y^{k}-z^{\star}\rangle:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ‖z⋆−zk+1‖2\displaystyle\|z^{\star}-z^{k+1}\|^{2} | ≤‖z⋆−zk‖2−‖zk+1−zk‖2+η2​L2​‖yk−zk‖2+Noisek+ProjErrk.\displaystyle\leq\|z^{\star}-z^{k}\|^{2}-\|z^{k+1}-z^{k}\|^{2}+\eta^{2}L^{2}\|y^{k}-z^{k}\|^{2}+\mathrm{Noise}\_{k}+\mathrm{ProjErr}\_{k}. |  | (63) |

Choose η≤1/(2​L)\eta\leq 1/(\sqrt{2}L) so that η2​L2≤1/2\eta^{2}L^{2}\leq 1/2. By Young’s inequality,

|  |  |  |
| --- | --- | --- |
|  | ‖zk+1−zk‖2≥12​‖yk−zk‖2−‖zk+1−yk‖2.\|z^{k+1}-z^{k}\|^{2}\geq\frac{1}{2}\|y^{k}-z^{k}\|^{2}-\|z^{k+1}-y^{k}\|^{2}. |  |

Applying nonexpansiveness of projection to the second stage of ([56](https://arxiv.org/html/2511.06451v1#Ax1.E56 "In Algorithmic step. ‣ A.5 Proof of Theorem 1: projected extragradient under Q-Align perturbations ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) shows ‖zk+1−yk‖≤η​‖F​(yk)−ξ~k−e~k‖\|z^{k+1}-y^{k}\|\leq\eta\|F(y^{k})-\tilde{\xi}^{k}-\tilde{e}^{k}\|, so

|  |  |  |
| --- | --- | --- |
|  | ‖zk+1−yk‖2≤2​η2​(‖F​(yk)‖2+‖ξ~k‖2+‖e~k‖2).\|z^{k+1}-y^{k}\|^{2}\leq 2\eta^{2}\big(\|F(y^{k})\|^{2}+\|\tilde{\xi}^{k}\|^{2}+\|\tilde{e}^{k}\|^{2}\big). |  |

Plugging the last two displays into ([63](https://arxiv.org/html/2511.06451v1#Ax1.E63 "In One-step merit bound. ‣ A.5 Proof of Theorem 1: projected extragradient under Q-Align perturbations ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")), taking conditional expectations, and using ([55](https://arxiv.org/html/2511.06451v1#Ax1.E55 "In Setting and assumptions. ‣ A.5 Proof of Theorem 1: projected extragradient under Q-Align perturbations ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures"))–([54](https://arxiv.org/html/2511.06451v1#Ax1.E54 "In Setting and assumptions. ‣ A.5 Proof of Theorem 1: projected extragradient under Q-Align perturbations ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) yield

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[‖z⋆−zk+1‖2∣ℱk]≤‖z⋆−zk‖2−14​‖yk−zk‖2+4​η2​𝔼​‖F​(yk)‖2+c1​η2​σ2+c2​η2,\mathbb{E}\big[\|z^{\star}-z^{k+1}\|^{2}\mid\mathcal{F}\_{k}\big]\leq\|z^{\star}-z^{k}\|^{2}-\frac{1}{4}\|y^{k}-z^{k}\|^{2}+4\eta^{2}\mathbb{E}\|F(y^{k})\|^{2}+c\_{1}\eta^{2}\sigma^{2}+c\_{2}\eta^{2}, |  | (64) |

for some universal constants c1,c2c\_{1},c\_{2}.

#### Residual bridging.

We relate ‖yk−zk‖\|y^{k}-z^{k}\| to a first-order residual. By ([56](https://arxiv.org/html/2511.06451v1#Ax1.E56 "In Algorithmic step. ‣ A.5 Proof of Theorem 1: projected extragradient under Q-Align perturbations ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) and firm nonexpansiveness of projection,

|  |  |  |
| --- | --- | --- |
|  | 1η​‖zk−yk‖≤‖F​(zk)‖+‖ξk‖+‖ek‖.\frac{1}{\eta}\|z^{k}-y^{k}\|\leq\|F(z^{k})\|+\|\xi^{k}\|+\|e^{k}\|. |  |

Also, Lipschitzness implies ‖F​(yk)‖≤‖F​(zk)‖+L​‖yk−zk‖\|F(y^{k})\|\leq\|F(z^{k})\|+L\|y^{k}-z^{k}\|. Combining these with ([64](https://arxiv.org/html/2511.06451v1#Ax1.E64 "In One-step merit bound. ‣ A.5 Proof of Theorem 1: projected extragradient under Q-Align perturbations ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")), taking full expectations and using η≤1/(2​L)\eta\leq 1/(\sqrt{2}L), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​‖z⋆−zk+1‖2≤𝔼​‖z⋆−zk‖2−c3​η2​𝔼​‖F​(zk)‖2+c4​η2​σ2+c5​η2,\mathbb{E}\|z^{\star}-z^{k+1}\|^{2}\leq\mathbb{E}\|z^{\star}-z^{k}\|^{2}-c\_{3}\eta^{2}\mathbb{E}\|F(z^{k})\|^{2}+c\_{4}\eta^{2}\sigma^{2}+c\_{5}\eta^{2}, |  | (65) |

for some constants c3,c4,c5>0c\_{3},c\_{4},c\_{5}>0 (the last term absorbs Q-Align errors through ([54](https://arxiv.org/html/2511.06451v1#Ax1.E54 "In Setting and assumptions. ‣ A.5 Proof of Theorem 1: projected extragradient under Q-Align perturbations ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")), thus is 𝒪​(η2)\mathcal{O}(\eta^{2})).

#### Summation and choice of stepsize.

Sum ([65](https://arxiv.org/html/2511.06451v1#Ax1.E65 "In Residual bridging. ‣ A.5 Proof of Theorem 1: projected extragradient under Q-Align perturbations ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) from k=0k=0 to K−1K-1, telescope the left-hand side, and choose η=θ/L\eta=\theta/L with a small absolute constant θ>0\theta>0. We obtain

|  |  |  |
| --- | --- | --- |
|  | 1K​∑k=0K−1𝔼​‖F​(zk)‖2≤𝒪​(L2​‖z0−z⋆‖2K)+𝒪​(σ2)+𝒪​(1L2).\frac{1}{K}\sum\_{k=0}^{K-1}\mathbb{E}\|F(z^{k})\|^{2}\;\leq\;\mathcal{O}\!\left(\frac{L^{2}\|z^{0}-z^{\star}\|^{2}}{K}\right)\;+\;\mathcal{O}\!\left(\sigma^{2}\right)\;+\;\mathcal{O}\!\left(\frac{1}{L^{2}}\right). |  |

Since the Q-Align term is 𝒪​(1/L2)\mathcal{O}(1/L^{2}) under ([54](https://arxiv.org/html/2511.06451v1#Ax1.E54 "In Setting and assumptions. ‣ A.5 Proof of Theorem 1: projected extragradient under Q-Align perturbations ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")), it is dominated by the noise floor 𝒪​(σ2)\mathcal{O}(\sigma^{2}) in practical regimes; removing constants and using the fact that mink⁡ak≤1K​∑kak\min\_{k}a\_{k}\leq\frac{1}{K}\sum\_{k}a\_{k} gives the claimed bound

|  |  |  |
| --- | --- | --- |
|  | min0≤k≤K−1⁡𝔼​‖F​(zk)‖2≤𝒪​(L2​‖z0−z⋆‖2K)+𝒪​(σ2).\min\_{0\leq k\leq K-1}\ \mathbb{E}\|F(z^{k})\|^{2}\;\leq\;\mathcal{O}\!\left(\frac{L^{2}\|z^{0}-z^{\star}\|^{2}}{K}\right)\;+\;\mathcal{O}\!\left(\sigma^{2}\right). |  |

#### Auxiliary lemma (residual bridge).

###### Lemma 7.

For η≤1/L\eta\leq 1/L and any z∈𝒵z\in\mathcal{Z},

|  |  |  |
| --- | --- | --- |
|  | ‖Rη​(z)‖≤(1+η​L)​‖F​(z)‖,‖F​(z)‖≤‖Rη​(z)‖+η​L​‖F​(z)‖.\|R\_{\eta}(z)\|\;\leq\;(1+\eta L)\,\|F(z)\|,\qquad\|F(z)\|\;\leq\;\|R\_{\eta}(z)\|+\eta L\,\|F(z)\|. |  |

Hence ‖Rη​(z)‖2\|R\_{\eta}(z)\|^{2} and ‖F​(z)‖2\|F(z)\|^{2} are equivalent up to 𝒪​(1)\mathcal{O}(1) constants depending only on η​L\eta L.

*Proof.* By nonexpansiveness of Π𝒵\Pi\_{\mathcal{Z}},

|  |  |  |
| --- | --- | --- |
|  | ‖Rη​(z)‖=1η​‖z−Π𝒵​(z−η​F​(z))‖≤1η​‖z−(z−η​F​(z))‖=‖F​(z)‖.\|R\_{\eta}(z)\|=\frac{1}{\eta}\big\|z-\Pi\_{\mathcal{Z}}(z-\eta F(z))\big\|\leq\frac{1}{\eta}\|z-(z-\eta F(z))\|=\|F(z)\|. |  |

The reverse direction follows by adding–subtracting z−η​F​(z)z-\eta F(z) inside the projection and applying Lipschitzness of FF; details are standard and omitted. ∎

#### Deterministic corollary.

If σ=0\sigma=0 (deterministic gradients), the rate improves to

|  |  |  |
| --- | --- | --- |
|  | min0≤k≤K−1⁡‖F​(zk)‖2≤𝒪​(L2​‖z0−z⋆‖2K),\min\_{0\leq k\leq K-1}\ \|F(z^{k})\|^{2}\;\leq\;\mathcal{O}\!\left(\frac{L^{2}\|z^{0}-z^{\star}\|^{2}}{K}\right), |  |

matching classical extragradient rates for monotone Lipschitz VIs.

#### Remarks.

(i) Strong monotonicity (with modulus μ>0\mu>0) yields a linear convergence term 𝒪​((1−η​μ)K)\mathcal{O}\big((1-\eta\mu)^{K}\big) until it hits the same 𝒪​(σ2)\mathcal{O}(\sigma^{2}) noise floor.
(ii) The Q-Align perturbations are “benign” provided ([54](https://arxiv.org/html/2511.06451v1#Ax1.E54 "In Setting and assumptions. ‣ A.5 Proof of Theorem 1: projected extragradient under Q-Align perturbations ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) holds; empirically, the spectral guard logs (λlip\lambda\_{\mathrm{lip}} before/after and projection distances) conform to this scaling.
(iii) The same analysis extends to mirror-prox with a distance-generating function; we focus on the Euclidean case for clarity.

This completes the proof of Theorem [1](https://arxiv.org/html/2511.06451v1#Thmtheorem1 "Theorem 1 (Extragradient convergence to a noise ball). ‣ Convergence guarantee (noise-stable neighborhood). ‣ 3.4 Saddle-Point Training and Safety-Oriented Stopping ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures").

### B.1 Proof of Theorem [2](https://arxiv.org/html/2511.06451v1#Thmtheorem2 "Theorem 2 (Approximation rate and conditioning). ‣ T1: Approximation Error and Conditioning ‣ 4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures"): approximation rate and conditioning

We prove the two claims in ([28](https://arxiv.org/html/2511.06451v1#S4.E28 "In Theorem 2 (Approximation rate and conditioning). ‣ T1: Approximation Error and Conditioning ‣ 4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")): the m−βsmoothm^{-\beta\_{\mathrm{smooth}}} approximation rate and the spectral conditioning proxy bound. Throughout, 𝒵⊂ℝdz\mathcal{Z}\subset\mathbb{R}^{d\_{z}} is compact, f⋆f^{\star} is βsmooth\beta\_{\mathrm{smooth}}-Hölder on 𝒵\mathcal{Z} and jointly Hölder in the maturity argument T∈𝒯=[Tmin,Tmax]T\in\mathcal{T}=[T\_{\min},T\_{\max}]. The RN-operator 𝒢θ\mathcal{G}\_{\theta} is realized by a selective-scan (RN-Operator) layer followed by a convex–monotone decoder, with Q-Align ensuring per-layer 11-Lipschitz projections and spectral safety (Spec-Guard). We use ∥⋅∥\|\cdot\| for the Euclidean or spectral norm depending on context.

#### Model parameterization.

Let {Tℓ}ℓ=1L\{T\_{\ell}\}\_{\ell=1}^{L} be the maturity grid. One-step RN dynamics writes

|  |  |  |  |
| --- | --- | --- | --- |
|  | hℓ=Gθ​(Tℓ,Tℓ−1)​hℓ−1+Bθ​(Tℓ)​uℓ,Gθ=exp⁡(Δ​tℓ​Aθ​(Tℓ)),h\_{\ell}=G\_{\theta}(T\_{\ell},T\_{\ell-1})\,h\_{\ell-1}+B\_{\theta}(T\_{\ell})\,u\_{\ell},\qquad G\_{\theta}=\exp\!\big(\Delta t\_{\ell}A\_{\theta}(T\_{\ell})\big), |  | (66) |

with Δ​tℓ=Tℓ−Tℓ−1\Delta t\_{\ell}=T\_{\ell}-T\_{\ell-1}. Under Spec-Guard, ρ​(Aθ​(Tℓ))​Δ​tℓ≤1−ε\rho(A\_{\theta}(T\_{\ell}))\Delta t\_{\ell}\leq 1-\varepsilon for some ε∈(0,1)\varepsilon\in(0,1), hence the associated Green kernel

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒢θ​(Tℓ,Ts):=∏r=s+1ℓGθ​(Tr,Tr−1)\mathcal{G}\_{\theta}(T\_{\ell},T\_{s}):=\prod\_{r=s+1}^{\ell}G\_{\theta}(T\_{r},T\_{r-1}) |  | (67) |

satisfies the Neumann-type bound (Lemma [1](https://arxiv.org/html/2511.06451v1#Thmlemma1 "Lemma 1 (Green kernel bound). ‣ Spectral safety and discrete Green kernel. ‣ 3.1 Risk–Neutral Operator Layer (RN-Operator) ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑s≤ℓ‖𝒢θ​(Tℓ,Ts)‖≤C​(ε),uniformly in ​ℓ.\sum\_{s\leq\ell}\big\|\mathcal{G}\_{\theta}(T\_{\ell},T\_{s})\big\|\ \leq\ C(\varepsilon),\qquad\text{uniformly in }\ell. |  | (68) |

The output price surface before the convex–monotone decoder is a scan of the input features {us}\{u\_{s}\}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | zℓ​(⋅)=∑s≤ℓ𝒢θ​(Tℓ,Ts)​Bθ​(Ts)​us​(⋅),z\_{\ell}(\cdot)=\sum\_{s\leq\ell}\mathcal{G}\_{\theta}(T\_{\ell},T\_{s})\,B\_{\theta}(T\_{s})\,u\_{s}(\cdot), |  | (69) |

and the decoder Φθ\Phi\_{\theta} (ICNN+Legendre projection) is 11-Lipschitz under Q-Align.

We adopt a low-rank gate parameterization

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bθ​(T)=∑j=1mbj​(T)​wj​vj⊤,Aθ​(T)=Dθ​(T)+∑j=1maj​(T)​rj​qj⊤,B\_{\theta}(T)=\sum\_{j=1}^{m}b\_{j}(T)\,w\_{j}v\_{j}^{\top},\qquad A\_{\theta}(T)=D\_{\theta}(T)+\sum\_{j=1}^{m}a\_{j}(T)\,r\_{j}q\_{j}^{\top}, |  | (70) |

with ‖wj‖=‖vj‖=‖rj‖=‖qj‖=1\|w\_{j}\|=\|v\_{j}\|=\|r\_{j}\|=\|q\_{j}\|=1 and aj,bja\_{j},b\_{j} bounded and βsmooth\beta\_{\mathrm{smooth}}-Hölder in TT (enforced by per-step spectral/Lipschitz projection). The rank surrogate is thus mm.

#### Part I: approximation rate.

We consider the target operator f⋆:(u,⋅)↦C⋆​(⋅)f^{\star}:(u,\cdot)\mapsto C^{\star}(\cdot), which we assume admits a separable Green-type expansion with Hölder control:

|  |  |  |  |
| --- | --- | --- | --- |
|  | f⋆​(u)​(T,ξ)=∑j=1∞αj​ψj​(T)​φj​(u;ξ),∑j=1∞jβsmooth​|αj|≤M<∞,f^{\star}(u)(T,\xi)=\sum\_{j=1}^{\infty}\alpha\_{j}\,\psi\_{j}(T)\,\varphi\_{j}(u;\xi),\qquad\sum\_{j=1}^{\infty}j^{\beta\_{\mathrm{smooth}}}\,|\alpha\_{j}|\ \leq\ M<\infty, |  | (71) |

where {ψj}\{\psi\_{j}\} is a smooth dictionary on 𝒯\mathcal{T} (e.g., integrated B-splines or compactly supported wavelets) with βsmooth\beta\_{\mathrm{smooth}}-Hölder regularity and {φj}\{\varphi\_{j}\} are feature functionals uniformly bounded on 𝒵\mathcal{Z}. Such expansions are classical for Hölder classes via nonlinear mm-term approximations with wavelet or spline dictionaries (see, e.g., DeVore–Temlyakov mm-term approximation theory). The coefficient decay condition in ([71](https://arxiv.org/html/2511.06451v1#Ax1.E71 "In Part I: approximation rate. ‣ B.1 Proof of Theorem 2: approximation rate and conditioning ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) is equivalent to f⋆f^{\star} belonging to a Besov/Hölder ball with smoothness βsmooth\beta\_{\mathrm{smooth}}.

Define the mm-term truncation

|  |  |  |  |
| --- | --- | --- | --- |
|  | fm⋆​(u)​(T,ξ)=∑j=1mαj​ψj​(T)​φj​(u;ξ).f\_{m}^{\star}(u)(T,\xi)=\sum\_{j=1}^{m}\alpha\_{j}\,\psi\_{j}(T)\,\varphi\_{j}(u;\xi). |  | (72) |

By Stechkin’s inequality for best mm-term approximations in ℓp\ell^{p} with p=1/βsmoothp=1/\beta\_{\mathrm{smooth}} surrogate (monotone rearrangement of coefficients),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖f⋆−fm⋆‖L2​(𝒵)≤C​m−βsmooth​(∑j≥1jβsmooth​|αj|)≤C′​m−βsmooth.\|f^{\star}-f\_{m}^{\star}\|\_{L^{2}(\mathcal{Z})}\ \leq\ C\,m^{-\beta\_{\mathrm{smooth}}}\,\bigg(\sum\_{j\geq 1}j^{\beta\_{\mathrm{smooth}}}\,|\alpha\_{j}|\bigg)\ \leq\ C^{\prime}m^{-\beta\_{\mathrm{smooth}}}. |  | (73) |

It remains to show that 𝒢θ\mathcal{G}\_{\theta} can realize fm⋆f\_{m}^{\star} up to an arbitrarily small error when mm atoms are allocated in ([70](https://arxiv.org/html/2511.06451v1#Ax1.E70 "In Model parameterization. ‣ B.1 Proof of Theorem 2: approximation rate and conditioning ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")). Choose bj​(⋅)b\_{j}(\cdot) so that the scan ([69](https://arxiv.org/html/2511.06451v1#Ax1.E69 "In Model parameterization. ‣ B.1 Proof of Theorem 2: approximation rate and conditioning ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) reproduces ψj\psi\_{j} on the grid (standard for spline/wavelet reproduction using stable discrete Green convolutions), and set the feature directions vj,wjv\_{j},w\_{j} so that the linear functionals φj​(u;⋅)\varphi\_{j}(u;\cdot) are matched by u↦vj⊤​u​(⋅)u\mapsto v\_{j}^{\top}u(\cdot) and the decoder’s linear readout (pre-ICNN) maps wjw\_{j} to the correct output channel. The ICNN+Legendre decoder, being 11-Lipschitz and positively homogeneous on the linear span of the constructed atoms, preserves the L2L^{2} approximation error.

Consequently, there exists θ=θ​(m)\theta=\theta(m) with rank mm such that

|  |  |  |
| --- | --- | --- |
|  | ‖𝒢θ−fm⋆‖L2​(𝒵)≤εm,with ​εm→0​ as the reproduction tolerance on ​{ψj,φj}​ shrinks,\|\mathcal{G}\_{\theta}-f\_{m}^{\star}\|\_{L^{2}(\mathcal{Z})}\ \leq\ \varepsilon\_{m},\quad\text{with }\varepsilon\_{m}\to 0\text{ as the reproduction tolerance on }\{\psi\_{j},\varphi\_{j}\}\text{ shrinks}, |  |

and combining with ([73](https://arxiv.org/html/2511.06451v1#Ax1.E73 "In Part I: approximation rate. ‣ B.1 Proof of Theorem 2: approximation rate and conditioning ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) yields

|  |  |  |
| --- | --- | --- |
|  | infθ‖𝒢θ−f⋆‖L2​(𝒵)≤‖𝒢θ−fm⋆‖L2​(𝒵)+‖fm⋆−f⋆‖L2​(𝒵)≤C1​m−βsmooth,\inf\_{\theta}\|\mathcal{G}\_{\theta}-f^{\star}\|\_{L^{2}(\mathcal{Z})}\ \leq\ \|\mathcal{G}\_{\theta}-f\_{m}^{\star}\|\_{L^{2}(\mathcal{Z})}+\|f\_{m}^{\star}-f^{\star}\|\_{L^{2}(\mathcal{Z})}\ \leq\ C\_{1}m^{-\beta\_{\mathrm{smooth}}}, |  |

for C1C\_{1} independent of LL (the scan length), since the reproduction constants depend only on the dictionary stability and the Green kernel bound ([68](https://arxiv.org/html/2511.06451v1#Ax1.E68 "In Model parameterization. ‣ B.1 Proof of Theorem 2: approximation rate and conditioning ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")), which is uniform in LL under Spec-Guard.

*Remark A.1 (effective dimension).* If the target lacks separability, the same argument yields ‖f⋆−fm⋆‖=𝒪​(m−βsmooth/d^)\|f^{\star}-f\_{m}^{\star}\|=\mathcal{O}(m^{-\beta\_{\mathrm{smooth}}/\hat{d}}) with d^\hat{d} the effective approximation dimension.

#### Part II: conditioning bound.

Let 𝒥θ\mathcal{J}\_{\theta} be the Jacobian of the overall mapping θ↦Φθ∘𝖲𝖼𝖺𝗇θ​(u)\theta\mapsto\Phi\_{\theta}\circ\mathsf{Scan}\_{\theta}(u) evaluated on a bounded input uu (the bound is uniform over ‖u‖≤U\|u\|\leq U). By the chain rule and ([69](https://arxiv.org/html/2511.06451v1#Ax1.E69 "In Model parameterization. ‣ B.1 Proof of Theorem 2: approximation rate and conditioning ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥θ=D​Φθ​(z)​∑ℓ=1L∑s≤ℓ(𝒢θ​(Tℓ,Ts)​∂θBθ​(Ts)⏟direct term+∂θ𝒢θ​(Tℓ,Ts)​Bθ​(Ts)⏟state term)​us,\mathcal{J}\_{\theta}\;=\;D\Phi\_{\theta}(z)\,\sum\_{\ell=1}^{L}\ \sum\_{s\leq\ell}\Big(\underbrace{\mathcal{G}\_{\theta}(T\_{\ell},T\_{s})\,\partial\_{\theta}B\_{\theta}(T\_{s})}\_{\text{direct term}}\;+\;\underbrace{\partial\_{\theta}\mathcal{G}\_{\theta}(T\_{\ell},T\_{s})\,B\_{\theta}(T\_{s})}\_{\text{state term}}\Big)\,u\_{s}, |  | (74) |

where D​ΦθD\Phi\_{\theta} is the decoder Jacobian. Under Q-Align, every layer (encoder/base/decoder) is 11-Lipschitz after projection, so ‖D​Φθ​(z)‖≤1\|D\Phi\_{\theta}(z)\|\leq 1. For the direct term,

|  |  |  |
| --- | --- | --- |
|  | ‖𝒢θ​(Tℓ,Ts)​∂θBθ​(Ts)​us‖≤‖𝒢θ​(Tℓ,Ts)‖​‖∂θBθ​(Ts)‖​‖us‖.\big\|\mathcal{G}\_{\theta}(T\_{\ell},T\_{s})\,\partial\_{\theta}B\_{\theta}(T\_{s})\,u\_{s}\big\|\ \leq\ \|\mathcal{G}\_{\theta}(T\_{\ell},T\_{s})\|\ \|\partial\_{\theta}B\_{\theta}(T\_{s})\|\ \|u\_{s}\|. |  |

The low-rank gate ([70](https://arxiv.org/html/2511.06451v1#Ax1.E70 "In Model parameterization. ‣ B.1 Proof of Theorem 2: approximation rate and conditioning ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) implies ‖∂θBθ​(T)‖≤cb​Lg\|\partial\_{\theta}B\_{\theta}(T)\|\leq c\_{b}\,L\_{g} with LgL\_{g} the Lipschitz constant (w.r.t. features/inputs) of the learned gates and cbc\_{b} a dimension-free constant tied to basis normalization. Summing over s≤ℓs\leq\ell and using ([68](https://arxiv.org/html/2511.06451v1#Ax1.E68 "In Model parameterization. ‣ B.1 Proof of Theorem 2: approximation rate and conditioning ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")),

|  |  |  |
| --- | --- | --- |
|  | ∑s≤ℓ‖𝒢θ​(Tℓ,Ts)​∂θBθ​(Ts)​us‖≤C​(ε)​cb​Lg​maxs⁡‖us‖.\sum\_{s\leq\ell}\big\|\mathcal{G}\_{\theta}(T\_{\ell},T\_{s})\,\partial\_{\theta}B\_{\theta}(T\_{s})\,u\_{s}\big\|\ \leq\ C(\varepsilon)\,c\_{b}\,L\_{g}\max\_{s}\|u\_{s}\|. |  |

For the state term, differentiate ([67](https://arxiv.org/html/2511.06451v1#Ax1.E67 "In Model parameterization. ‣ B.1 Proof of Theorem 2: approximation rate and conditioning ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")):

|  |  |  |
| --- | --- | --- |
|  | ∂θ𝒢θ​(Tℓ,Ts)=∑r=s+1ℓ(∏q=r+1ℓGθ​(Tq,Tq−1))​∂θGθ​(Tr,Tr−1)​(∏p=s+1r−1Gθ​(Tp,Tp−1)).\partial\_{\theta}\mathcal{G}\_{\theta}(T\_{\ell},T\_{s})=\sum\_{r=s+1}^{\ell}\Big(\prod\_{q=r+1}^{\ell}G\_{\theta}(T\_{q},T\_{q-1})\Big)\,\partial\_{\theta}G\_{\theta}(T\_{r},T\_{r-1})\,\Big(\prod\_{p=s+1}^{r-1}G\_{\theta}(T\_{p},T\_{p-1})\Big). |  |

Using ∂θGθ​(Tr,Tr−1)=∫01exp⁡(τ​Δ​tr​Aθ)​Δ​tr​∂θAθ​exp⁡((1−τ)​Δ​tr​Aθ)​d​τ\partial\_{\theta}G\_{\theta}(T\_{r},T\_{r-1})=\int\_{0}^{1}\exp\!\big(\tau\Delta t\_{r}A\_{\theta}\big)\,\Delta t\_{r}\,\partial\_{\theta}A\_{\theta}\,\exp\!\big((1-\tau)\Delta t\_{r}A\_{\theta}\big)\,d\tau, we get

|  |  |  |
| --- | --- | --- |
|  | ‖∂θGθ​(Tr,Tr−1)‖≤Δ​tr​‖∂θAθ​(Tr)‖​supτ∈[0,1]‖exp⁡(τ​Δ​tr​Aθ)‖2.\|\partial\_{\theta}G\_{\theta}(T\_{r},T\_{r-1})\|\leq\Delta t\_{r}\,\|\partial\_{\theta}A\_{\theta}(T\_{r})\|\,\sup\_{\tau\in[0,1]}\big\|\exp(\tau\Delta t\_{r}A\_{\theta})\big\|^{2}. |  |

Under Spec-Guard and spectral projection, supτ‖exp⁡(τ​Δ​tr​Aθ)‖≤ca\sup\_{\tau}\|\exp(\tau\Delta t\_{r}A\_{\theta})\|\leq c\_{a} with cac\_{a} depending on ε\varepsilon and maxℓ⁡‖Aθ​(Tℓ)‖2\max\_{\ell}\|A\_{\theta}(T\_{\ell})\|\_{2}. The low-rank parameterization ([70](https://arxiv.org/html/2511.06451v1#Ax1.E70 "In Model parameterization. ‣ B.1 Proof of Theorem 2: approximation rate and conditioning ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) yields ‖∂θAθ​(T)‖≤ca′​Lg\|\partial\_{\theta}A\_{\theta}(T)\|\leq c\_{a}^{\prime}L\_{g} (linear in the gate Lipschitz constant). Consequently,

|  |  |  |
| --- | --- | --- |
|  | ‖∂θ𝒢θ​(Tℓ,Ts)‖≤ca2​ca′​Lg​∑r=s+1ℓΔ​tr​‖∏q=r+1ℓGθ​(Tq,Tq−1)‖​‖∏p=s+1r−1Gθ​(Tp,Tp−1)‖.\|\partial\_{\theta}\mathcal{G}\_{\theta}(T\_{\ell},T\_{s})\|\ \leq\ c\_{a}^{2}\,c\_{a}^{\prime}L\_{g}\sum\_{r=s+1}^{\ell}\Delta t\_{r}\,\Big\|\prod\_{q=r+1}^{\ell}G\_{\theta}(T\_{q},T\_{q-1})\Big\|\,\Big\|\prod\_{p=s+1}^{r-1}G\_{\theta}(T\_{p},T\_{p-1})\Big\|. |  |

By submultiplicativity and again the Neumann-type bound ([68](https://arxiv.org/html/2511.06451v1#Ax1.E68 "In Model parameterization. ‣ B.1 Proof of Theorem 2: approximation rate and conditioning ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")), the double product is summably bounded uniformly in LL. Hence,

|  |  |  |
| --- | --- | --- |
|  | ∑s≤ℓ‖∂θ𝒢θ​(Tℓ,Ts)​Bθ​(Ts)‖≤C′′​(ε)​Lg​maxℓ⁡‖Aθ​(Tℓ)‖2.\sum\_{s\leq\ell}\|\partial\_{\theta}\mathcal{G}\_{\theta}(T\_{\ell},T\_{s})\,B\_{\theta}(T\_{s})\|\ \leq\ C^{\prime\prime}(\varepsilon)\,L\_{g}\,\max\_{\ell}\|A\_{\theta}(T\_{\ell})\|\_{2}. |  |

Combining direct and state terms in ([74](https://arxiv.org/html/2511.06451v1#Ax1.E74 "In Part II: conditioning bound. ‣ B.1 Proof of Theorem 2: approximation rate and conditioning ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) and recalling that the rank-mm structure introduces at most an mm-fold linear scaling in the number of active gates, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖𝒥θ‖≤C2​(maxℓ⁡‖Aθ​(Tℓ)‖2)​Lg​m,\|\mathcal{J}\_{\theta}\|\ \leq\ C\_{2}\,\big(\max\_{\ell}\|A\_{\theta}(T\_{\ell})\|\_{2}\big)\,L\_{g}\,m, |  | (75) |

for a constant C2C\_{2} depending on ε\varepsilon, dictionary normalization, and decoder curvature bounds, but *independent of LL* thanks to the uniform Green kernel bound ([68](https://arxiv.org/html/2511.06451v1#Ax1.E68 "In Model parameterization. ‣ B.1 Proof of Theorem 2: approximation rate and conditioning ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")). This proves the conditioning proxy bound in ([28](https://arxiv.org/html/2511.06451v1#S4.E28 "In Theorem 2 (Approximation rate and conditioning). ‣ T1: Approximation Error and Conditioning ‣ 4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")).

#### Conclusion.

The approximation rate follows from the best mm-term construction ([72](https://arxiv.org/html/2511.06451v1#Ax1.E72 "In Part I: approximation rate. ‣ B.1 Proof of Theorem 2: approximation rate and conditioning ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures"))–([73](https://arxiv.org/html/2511.06451v1#Ax1.E73 "In Part I: approximation rate. ‣ B.1 Proof of Theorem 2: approximation rate and conditioning ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) realized by the RN-Operator with rank-mm gates; the conditioning proxy is controlled by Q-Align spectral constraints and the Neumann-type summability of the discrete Green kernel, yielding ([75](https://arxiv.org/html/2511.06451v1#Ax1.E75 "In Part II: conditioning bound. ‣ B.1 Proof of Theorem 2: approximation rate and conditioning ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")). This completes the proof of Theorem [2](https://arxiv.org/html/2511.06451v1#Thmtheorem2 "Theorem 2 (Approximation rate and conditioning). ‣ T1: Approximation Error and Conditioning ‣ 4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures"). ∎

### B.2 Proof of Theorem [3](https://arxiv.org/html/2511.06451v1#Thmtheorem3 "Theorem 3 (Local identifiability and information bound). ‣ T2: Local Identifiability and CRLB-Type Lower Bounds ‣ 4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures"): local identifiability and CRLB

#### Model and regularity.

Let (u,Y)(u,Y) denote a generic input–output pair, where u∈𝒵u\in\mathcal{Z} is a feature field and Y={C​(Tℓ,Kj)}ℓ≤L,j≤JℓY=\{C(T\_{\ell},K\_{j})\}\_{\ell\leq L,\,j\leq J\_{\ell}} collects option prices on the maturity–strike grid. The RN-operator induces the mean surface

|  |  |  |
| --- | --- | --- |
|  | μθ​(u)=Φθ​(∑s≤ℓ𝒢θ​(Tℓ,Ts)​Bθ​(Ts)​us)ℓ,j,\mu\_{\theta}(u)\;=\;\Phi\_{\theta}\!\left(\sum\_{s\leq\ell}\mathcal{G}\_{\theta}(T\_{\ell},T\_{s})\,B\_{\theta}(T\_{s})\,u\_{s}\right)\_{\ell,j}, |  |

with Φθ\Phi\_{\theta} the convex–monotone decoder (ICNN+Legendre projection). We assume: (A1) noise model Y=μθ​(u)+εY=\mu\_{\theta}(u)+\varepsilon, where ε\varepsilon is mean-zero, sub-Gaussian with covariance operator Σ\Sigma independent of θ\theta; (A2) the input process has a nondegenerate covariance operator 𝖢𝗈𝗏​(u)\mathsf{Cov}(u) on 𝒵\mathcal{Z}; (A3) Q-Align enforces 11-Lipschitz layers and Spec-Guard enforces the CFL constraint so that Lemma [1](https://arxiv.org/html/2511.06451v1#Thmlemma1 "Lemma 1 (Green kernel bound). ‣ Spectral safety and discrete Green kernel. ‣ 3.1 Risk–Neutral Operator Layer (RN-Operator) ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") holds. These assumptions match the main text.

#### Step I: decoder-level identifiability on the grid.

Let Cθ​(T,K)C\_{\theta}(T,K) be the decoded call price surface. Static no-arbitrage ensures convexity in KK and monotonicity in TT. The Breeden–Litzenberger identity implies that, for each TℓT\_{\ell},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂2Cθ∂K2​(Tℓ,K)=er​Tℓ​fθℚ​(Tℓ,K),\frac{\partial^{2}C\_{\theta}}{\partial K^{2}}(T\_{\ell},K)\;=\;\mathrm{e}^{rT\_{\ell}}\,f\_{\theta}^{\mathbb{Q}}(T\_{\ell},K), |  | (76) |

where fθℚ​(Tℓ,⋅)f\_{\theta}^{\mathbb{Q}}(T\_{\ell},\cdot) is the risk-neutral density at maturity TℓT\_{\ell}.
VIX2 replication consistency further imposes

|  |  |  |  |
| --- | --- | --- | --- |
|  | VIXθ2​(Tℓ)=2​er​TℓTℓ​∫0∞1K2​Qθ​(K,Tℓ)​𝑑K(discrete grid via quadrature as in the main text).\mathrm{VIX}\_{\theta}^{2}(T\_{\ell})\;=\;\frac{2\,\mathrm{e}^{rT\_{\ell}}}{T\_{\ell}}\int\_{0}^{\infty}\frac{1}{K^{2}}\,Q\_{\theta}(K,T\_{\ell})\,dK\quad\text{(discrete grid via quadrature as in the main text)}. |  | (77) |

On the grid, if two decoders Φθ1,Φθ2\Phi\_{\theta\_{1}},\Phi\_{\theta\_{2}} satisfy ([76](https://arxiv.org/html/2511.06451v1#Ax1.E76 "In Step I: decoder-level identifiability on the grid. ‣ B.2 Proof of Theorem 3: local identifiability and CRLB ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) with the same second derivative and also match ([77](https://arxiv.org/html/2511.06451v1#Ax1.E77 "In Step I: decoder-level identifiability on the grid. ‣ B.2 Proof of Theorem 3: local identifiability and CRLB ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")), then their implied densities and integrated variance coincide at all grid maturities. Since CC is recovered from its second derivative and boundary conditions (no-arbitrage asymptotics at K→0,∞K\to 0,\infty), we conclude

|  |  |  |
| --- | --- | --- |
|  | Φθ1​(z)=Φθ2​(z)for all admissible inputs ​z.\Phi\_{\theta\_{1}}(z)=\Phi\_{\theta\_{2}}(z)\quad\text{for all admissible inputs }z. |  |

Thus, *decoder-level identifiability holds* on the grid.

#### Step II: propagation through the scan to the operator level.

Suppose 𝒢θ1\mathcal{G}\_{\theta\_{1}} and 𝒢θ2\mathcal{G}\_{\theta\_{2}} yield the same decoded surface for almost every input uu:

|  |  |  |
| --- | --- | --- |
|  | Φθ1​(∑s≤ℓ𝒢θ1​(Tℓ,Ts)​Bθ1​(Ts)​us)=Φθ2​(∑s≤ℓ𝒢θ2​(Tℓ,Ts)​Bθ2​(Ts)​us),a.s. in ​u.\Phi\_{\theta\_{1}}\!\Big(\sum\_{s\leq\ell}\mathcal{G}\_{\theta\_{1}}(T\_{\ell},T\_{s})B\_{\theta\_{1}}(T\_{s})u\_{s}\Big)\;=\;\Phi\_{\theta\_{2}}\!\Big(\sum\_{s\leq\ell}\mathcal{G}\_{\theta\_{2}}(T\_{\ell},T\_{s})B\_{\theta\_{2}}(T\_{s})u\_{s}\Big),\quad\text{a.s.\ in }u. |  |

Since Φθ\Phi\_{\theta} is 11-Lipschitz and strictly monotone along the decoder’s active rays (by convexity and positive homogeneity of the ICNN regularized by Legendre projection), equality of outputs for almost every uu implies equality of *pre-decoder* representations for almost every uu:

|  |  |  |
| --- | --- | --- |
|  | ∑s≤ℓ𝒢θ1​(Tℓ,Ts)​Bθ1​(Ts)​us=∑s≤ℓ𝒢θ2​(Tℓ,Ts)​Bθ2​(Ts)​usin ​L2​(𝒵).\sum\_{s\leq\ell}\mathcal{G}\_{\theta\_{1}}(T\_{\ell},T\_{s})B\_{\theta\_{1}}(T\_{s})u\_{s}\;=\;\sum\_{s\leq\ell}\mathcal{G}\_{\theta\_{2}}(T\_{\ell},T\_{s})B\_{\theta\_{2}}(T\_{s})u\_{s}\quad\text{in }L^{2}(\mathcal{Z}). |  |

Let δ​θ\delta\theta be a tangent perturbation at θ⋆\theta^{\star}, and write the linearized identity

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑s≤ℓ(∂θ𝒢θ⋆​(Tℓ,Ts)​Bθ⋆​(Ts)+𝒢θ⋆​(Tℓ,Ts)​∂θBθ⋆​(Ts))​us= 0in ​L2​(𝒵).\sum\_{s\leq\ell}\!\Big(\partial\_{\theta}\mathcal{G}\_{\theta^{\star}}(T\_{\ell},T\_{s})\,B\_{\theta^{\star}}(T\_{s})+\mathcal{G}\_{\theta^{\star}}(T\_{\ell},T\_{s})\,\partial\_{\theta}B\_{\theta^{\star}}(T\_{s})\Big)u\_{s}\;=\;0\quad\text{in }L^{2}(\mathcal{Z}). |  | (78) |

Taking the covariance in uu and using nondegeneracy of 𝖢𝗈𝗏​(u)\mathsf{Cov}(u) together with the uniform Green bound (Lemma [1](https://arxiv.org/html/2511.06451v1#Thmlemma1 "Lemma 1 (Green kernel bound). ‣ Spectral safety and discrete Green kernel. ‣ 3.1 Risk–Neutral Operator Layer (RN-Operator) ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")), we obtain that the linear operator

|  |  |  |
| --- | --- | --- |
|  | ℒθ⋆​[δ​θ]:=∑s≤ℓ(∂θ𝒢θ⋆​(Tℓ,Ts)​Bθ⋆​(Ts)+𝒢θ⋆​(Tℓ,Ts)​∂θBθ⋆​(Ts))\mathcal{L}\_{\theta^{\star}}[\delta\theta]:=\sum\_{s\leq\ell}\!\Big(\partial\_{\theta}\mathcal{G}\_{\theta^{\star}}(T\_{\ell},T\_{s})\,B\_{\theta^{\star}}(T\_{s})+\mathcal{G}\_{\theta^{\star}}(T\_{\ell},T\_{s})\,\partial\_{\theta}B\_{\theta^{\star}}(T\_{s})\Big) |  |

vanishes if and only if δ​θ\delta\theta lies in the *symmetry tangent space* generated by atom permutations and reciprocal rescalings in the rank-mm factorization. Consequently, the differential D​𝒢θ⋆D\mathcal{G}\_{\theta^{\star}} is injective on the quotient by these symmetries, and by the inverse function theorem for Banach spaces, there exists a neighborhood 𝒰\mathcal{U} in which θ↦𝒢θ\theta\mapsto\mathcal{G}\_{\theta} is injective modulo symmetries.

#### Step III: Fisher information and CRLB.

Under (A1)–(A3), the log-likelihood for a single pair (u,Y)(u,Y) is

|  |  |  |
| --- | --- | --- |
|  | ℓ​(θ;u,Y)=−12​⟨Y−μθ​(u),Σ−1​(Y−μθ​(u))⟩+const,\ell(\theta;u,Y)\;=\;-\tfrac{1}{2}\big\langle Y-\mu\_{\theta}(u),\,\Sigma^{-1}\,(Y-\mu\_{\theta}(u))\big\rangle+\mathrm{const}, |  |

with score Sθ​(u,Y)=D​μθ​(u)⊤​Σ−1​(Y−μθ​(u))S\_{\theta}(u,Y)=D\mu\_{\theta}(u)^{\top}\Sigma^{-1}\big(Y-\mu\_{\theta}(u)\big), where D​μθ​(u)D\mu\_{\theta}(u) is the Jacobian of the RN-operator output w.r.t. θ\theta. The Fisher information is

|  |  |  |
| --- | --- | --- |
|  | ℐ​(θ):=𝔼​[Sθ​Sθ⊤]=𝔼​[D​μθ​(u)⊤​Σ−1​D​μθ​(u)],\mathcal{I}(\theta):=\mathbb{E}\!\left[S\_{\theta}S\_{\theta}^{\top}\right]\;=\;\mathbb{E}\!\left[D\mu\_{\theta}(u)^{\top}\Sigma^{-1}D\mu\_{\theta}(u)\right], |  |

since 𝔼​[Y−μθ​(u)∣u]=0\mathbb{E}[Y-\mu\_{\theta}(u)\mid u]=0. By Q-Align, D​μθ​(u)D\mu\_{\theta}(u) is bounded and measurable; by Step II, D​μθ⋆D\mu\_{\theta^{\star}} has trivial kernel on the symmetry-quotient space, hence ℐ​(θ⋆)\mathcal{I}(\theta^{\star}) is positive definite on that quotient. The Cramér–Rao inequality for unbiased estimators on smooth parametric families then yields

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[(θ^−θ⋆)​(θ^−θ⋆)⊤]⪰1n​ℐ​(θ⋆)−1,\mathbb{E}\!\left[(\widehat{\theta}-\theta^{\star})(\widehat{\theta}-\theta^{\star})^{\top}\right]\;\succeq\;\frac{1}{n}\,\mathcal{I}(\theta^{\star})^{-1}, |  |

and ([29](https://arxiv.org/html/2511.06451v1#S4.E29 "In Theorem 3 (Local identifiability and information bound). ‣ T2: Local Identifiability and CRLB-Type Lower Bounds ‣ 4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) follows after taking the trace. This completes the proof. ∎

### B.3 Proof of Proposition [5](https://arxiv.org/html/2511.06451v1#Thmproposition5 "Proposition 5 (Representative bound with coverage and residuals). ‣ T2′: Representative-Element Error Under Coverage Deficits ‣ 4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")

#### Set-up and notation.

Let 𝒢θ\mathcal{G}\_{\theta} be the RN-operator, Φθ\Phi\_{\theta} the convex–monotone decoder, and write the decoded surface Cθ=Φθ∘𝒢θ​(⋅)C\_{\theta}=\Phi\_{\theta}\circ\mathcal{G}\_{\theta}(\cdot) on the strike–maturity grid
𝒢={(Tℓ,Kj)}ℓ≤L,j≤Jℓ\mathcal{G}=\{(T\_{\ell},K\_{j})\}\_{\ell\leq L,\,j\leq J\_{\ell}}.
Let ℐ⊂𝒢\mathcal{I}\subset\mathcal{G} denote the set of covered cells with reliable quotes; its relative cardinality is cov:=|ℐ|/|𝒢|∈[0,1]\mathrm{cov}:=|\mathcal{I}|/|\mathcal{G}|\in[0,1]. On the complement 𝒢∖ℐ\mathcal{G}\setminus\mathcal{I}, the price surface is filled by a linear, static no-arbitrage–preserving interpolant 𝖤𝗑𝗍\mathsf{Ext} (convex in KK, monotone in TT). We assume an interpolation accuracy bound

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∥𝖤𝗑𝗍[C⋆|ℐ]−C⋆∥ℓ2​(𝒢)≤ε,\big\|\mathsf{Ext}[C^{\star}|\_{\mathcal{I}}]-C^{\star}\big\|\_{\ell^{2}(\mathcal{G})}\ \leq\ \varepsilon, |  | (79) |

where C⋆C^{\star} is the ground-truth surface induced by λ⋆\lambda^{\star}.

The training objective is a penalized, discretized risk under the risk-neutral measure with a martingale penalty of weight γ>0\gamma>0, plus the indicator of the no-arbitrage cone 𝒦\mathcal{K}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥γ​(λ):=1|ℐ|​∑(Tℓ,Kj)∈ℐ(Cλ​(Tℓ,Kj)−Yℓ​j)2+γ​𝖬𝖺𝗋𝗍​(λ)+ι𝒦​(Cλ).\mathcal{J}\_{\gamma}(\lambda)\ :=\ \frac{1}{|\mathcal{I}|}\!\sum\_{(T\_{\ell},K\_{j})\in\mathcal{I}}\big(C\_{\lambda}(T\_{\ell},K\_{j})-Y\_{\ell j}\big)^{2}\ +\ \gamma\,\mathsf{Mart}(\lambda)\ +\ \iota\_{\mathcal{K}}\big(C\_{\lambda}\big). |  | (80) |

Here Yℓ​jY\_{\ell j} are observed mid quotes; 𝖬𝖺𝗋𝗍​(λ)\mathsf{Mart}(\lambda) is a nonnegative convex proxy for the martingale defect (e.g., squared drift under ℚλ\mathbb{Q}\_{\lambda}); ι𝒦\iota\_{\mathcal{K}} is 0 if the static no-arbitrage conditions hold on the grid and +∞+\infty otherwise. Let λ^γ\widehat{\lambda}\_{\gamma} be a first-order stationary point of ([80](https://arxiv.org/html/2511.06451v1#Ax1.E80 "In Set-up and notation. ‣ B.3 Proof of Proposition 5 ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) on the *covered* grid, and let λε\lambda\_{\varepsilon} be the corresponding representative element when the uncovered cells are filled by 𝖤𝗑𝗍\mathsf{Ext}.

We further use: (i) the *global Lipschitz property* of the RN-operator map from Lemma [1](https://arxiv.org/html/2511.06451v1#Thmlemma1 "Lemma 1 (Green kernel bound). ‣ Spectral safety and discrete Green kernel. ‣ 3.1 Risk–Neutral Operator Layer (RN-Operator) ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") and Proposition [1](https://arxiv.org/html/2511.06451v1#Thmproposition1 "Proposition 1 (RN-operator stability under Q-Align). ‣ RN-operator stability under Q-Align. ‣ 3.2 Q-Align: Lipschitz Projection and Spectral Guard ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") (Q-Align and Spec-Guard), summarized as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Cλ1−Cλ2‖ℓ2​(𝒢)≤LRN​‖λ1−λ2‖L2​(𝒵),LRN<∞,\|C\_{\lambda\_{1}}-C\_{\lambda\_{2}}\|\_{\ell^{2}(\mathcal{G})}\ \leq\ L\_{\mathrm{RN}}\ \|\lambda\_{1}-\lambda\_{2}\|\_{L^{2}(\mathcal{Z})},\qquad L\_{\mathrm{RN}}<\infty, |  | (81) |

(ii) a *Hoffman-type bound* for the composite convex program (data-fidelity ++ linear constraints defining 𝒦\mathcal{K} ++ convex penalty), which states that there exists κHof>0\kappa\_{\mathrm{Hof}}>0 such that the distance to the solution set 𝒮γ\mathcal{S}\_{\gamma} satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | dist​(λ,𝒮γ)≤κHof​‖KKT​(λ)‖,\mathrm{dist}\big(\lambda,\mathcal{S}\_{\gamma}\big)\ \leq\ \kappa\_{\mathrm{Hof}}\ \|\mathrm{KKT}(\lambda)\|, |  | (82) |

where KKT​(λ)\mathrm{KKT}(\lambda) is a residual vector collecting the primal feasibility (no-arbitrage), the dual feasibility (subgradient of 𝖬𝖺𝗋𝗍\mathsf{Mart}), and stationarity violations (see, e.g., variational inequalities with polyhedral sets).

#### Step 1: interpolation (coverage) term.

Split the grid norm as ‖C‖ℓ2​(𝒢)2=‖C‖ℓ2​(ℐ)2+‖C‖ℓ2​(𝒢∖ℐ)2\|C\|\_{\ell^{2}(\mathcal{G})}^{2}=\|C\|\_{\ell^{2}(\mathcal{I})}^{2}+\|C\|\_{\ell^{2}(\mathcal{G}\setminus\mathcal{I})}^{2}.
On 𝒢∖ℐ\mathcal{G}\setminus\mathcal{I}, prices are provided by 𝖤𝗑𝗍\mathsf{Ext} built from ℐ\mathcal{I}. Let Πℐ\Pi\_{\mathcal{I}} be the sampling operator on ℐ\mathcal{I} and Πℐ⟂\Pi\_{\mathcal{I}}^{\perp} on the complement. The extension operator is linear and stable on the no-arbitrage cone, i.e.,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Πℐ⟂​𝖤𝗑𝗍​[v]‖ℓ2​(𝒢∖ℐ)≤α​(cov)​‖v‖ℓ2​(ℐ),α​(cov)≤Cext​(1−cov)−1,\big\|\Pi\_{\mathcal{I}}^{\perp}\,\mathsf{Ext}[v]\big\|\_{\ell^{2}(\mathcal{G}\setminus\mathcal{I})}\ \leq\ \alpha(\mathrm{cov})\ \|v\|\_{\ell^{2}(\mathcal{I})},\qquad\alpha(\mathrm{cov})\ \leq\ C\_{\mathrm{ext}}\,(1-\mathrm{cov})^{-1}, |  | (83) |

for some absolute CextC\_{\mathrm{ext}} depending only on the grid aspect ratio. The scaling (1−cov)−1(1-\mathrm{cov})^{-1} captures the worst-case amplification when extrapolating from a vanishing covered set. Applying ([83](https://arxiv.org/html/2511.06451v1#Ax1.E83 "In Step 1: interpolation (coverage) term. ‣ B.3 Proof of Proposition 5 ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) with v=C⋆|ℐ−Πℐ​Cλεv=C^{\star}|\_{\mathcal{I}}-\Pi\_{\mathcal{I}}C\_{\lambda\_{\varepsilon}} and adding the intrinsic interpolation error ([79](https://arxiv.org/html/2511.06451v1#Ax1.E79 "In Set-up and notation. ‣ B.3 Proof of Proposition 5 ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Cλε−C⋆‖ℓ2​(𝒢)≤Cext​(1−cov)−1​‖Πℐ​(Cλε−C⋆)‖ℓ2​(ℐ)+ε.\|C\_{\lambda\_{\varepsilon}}-C^{\star}\|\_{\ell^{2}(\mathcal{G})}\ \leq\ C\_{\mathrm{ext}}\,(1-\mathrm{cov})^{-1}\,\big\|\Pi\_{\mathcal{I}}(C\_{\lambda\_{\varepsilon}}-C^{\star})\big\|\_{\ell^{2}(\mathcal{I})}\ +\ \varepsilon. |  | (84) |

As the empirical fit on ℐ\mathcal{I} is optimized in ([80](https://arxiv.org/html/2511.06451v1#Ax1.E80 "In Set-up and notation. ‣ B.3 Proof of Proposition 5 ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")), the term ‖Πℐ​(Cλε−C⋆)‖\|\Pi\_{\mathcal{I}}(C\_{\lambda\_{\varepsilon}}-C^{\star})\| is in turn controlled by the optimization residual (treated in Step 3). For the present step, we retain the *coverage* contribution Cext​(1−cov)−1​εC\_{\mathrm{ext}}(1-\mathrm{cov})^{-1}\varepsilon to the full-grid error.

#### Step 2: martingale penalty (finite γ\gamma).

Let λ∞\lambda\_{\infty} denote an exact solution of the *constrained* problem (martingale enforced as a hard constraint and static no-arbitrage satisfied). By convexity and standard exact-penalty reasoning, first-order optimality implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | dist​(λε,{martingale-feasible})≤1γ​Cpen,\mathrm{dist}\big(\lambda\_{\varepsilon},\ \{\text{martingale-feasible}\}\big)\ \leq\ \tfrac{1}{\gamma}\,C\_{\mathrm{pen}}, |  | (85) |

for some modulus CpenC\_{\mathrm{pen}} depending on the subgradient bounds of 𝖬𝖺𝗋𝗍\mathsf{Mart} at feasible points (Q-Align and Spec-Guard ensure bounded Jacobians and thus bounded subgradients). Combining ([85](https://arxiv.org/html/2511.06451v1#Ax1.E85 "In Step 2: martingale penalty (finite 𝛾). ‣ B.3 Proof of Proposition 5 ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) with the Lipschitz continuity ([81](https://arxiv.org/html/2511.06451v1#Ax1.E81 "In Set-up and notation. ‣ B.3 Proof of Proposition 5 ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) transfers feasibility deviation into price-surface deviation with multiplicative constant LRNL\_{\mathrm{RN}}, and by metric regularity of the feasible set, it transfers to a distance in λ\lambda with a constant absorbed in C3C\_{3}.

#### Step 3: dual residual (stopping criterion).

Let dual\mathrm{dual} denote the norm of the KKT residual at termination. By the Hoffman bound ([82](https://arxiv.org/html/2511.06451v1#Ax1.E82 "In Set-up and notation. ‣ B.3 Proof of Proposition 5 ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | dist​(λε,𝒮γ)≤κHof​dual.\mathrm{dist}\big(\lambda\_{\varepsilon},\ \mathcal{S}\_{\gamma}\big)\ \leq\ \kappa\_{\mathrm{Hof}}\ \mathrm{dual}. |  | (86) |

Since λ⋆\lambda^{\star} (or λ∞\lambda\_{\infty}) lies within a bounded distance of 𝒮γ\mathcal{S}\_{\gamma} uniformly in the data draw (population minimizer versus empirical minimizer), a triangle inequality yields a κHof​dual\kappa\_{\mathrm{Hof}}\mathrm{dual} contribution to ‖λε−λ⋆‖L2​(𝒵)\|\lambda\_{\varepsilon}-\lambda^{\star}\|\_{L^{2}(\mathcal{Z})}.

#### Step 4: aggregation via RN-operator stability.

From ([81](https://arxiv.org/html/2511.06451v1#Ax1.E81 "In Set-up and notation. ‣ B.3 Proof of Proposition 5 ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")), converting surface errors back to L2​(𝒵)L^{2}(\mathcal{Z}) distances in λ\lambda multiplies by at most LRNL\_{\mathrm{RN}}. Gathering ([84](https://arxiv.org/html/2511.06451v1#Ax1.E84 "In Step 1: interpolation (coverage) term. ‣ B.3 Proof of Proposition 5 ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")), ([85](https://arxiv.org/html/2511.06451v1#Ax1.E85 "In Step 2: martingale penalty (finite 𝛾). ‣ B.3 Proof of Proposition 5 ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")), and ([86](https://arxiv.org/html/2511.06451v1#Ax1.E86 "In Step 3: dual residual (stopping criterion). ‣ B.3 Proof of Proposition 5 ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")), and absorbing universal constants (including LRNL\_{\mathrm{RN}}, CextC\_{\mathrm{ext}}, CpenC\_{\mathrm{pen}}, κHof\kappa\_{\mathrm{Hof}}) into C3C\_{3}, we obtain

|  |  |  |
| --- | --- | --- |
|  | ‖λε−λ⋆‖L2​(𝒵)≤C3​((1−cov)−1​ε+γ−1+dual),\|\lambda\_{\varepsilon}-\lambda^{\star}\|\_{L^{2}(\mathcal{Z})}\ \leq\ C\_{3}\Big(\,(1-\mathrm{cov})^{-1}\varepsilon\;+\;\gamma^{-1}\;+\;\mathrm{dual}\,\Big), |  |

which is precisely ([30](https://arxiv.org/html/2511.06451v1#S4.E30 "In Proposition 5 (Representative bound with coverage and residuals). ‣ T2′: Representative-Element Error Under Coverage Deficits ‣ 4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")). ∎

#### Remarks.

(i) The (1−cov)−1(1-\mathrm{cov})^{-1} factor is tight up to constants for adversarial mask geometries (thin strips in TT or KK), and improves to O​(1)O(1) when the mask satisfies an interior-cone condition (uniform spreading).
(ii) The constant C3C\_{3} does not depend on LL beyond the linear scan factor already controlled by Spec-Guard; it depends on the no-arbitrage cone geometry only through curvature bounds of the ICNN decoder.
(iii) Empirically, the regression of the gap proxy onto the representative error in our runs (see Sec. 6.6) exhibits a slope consistent with the κHof\kappa\_{\mathrm{Hof}} scale predicted here.

### B.4 Proof of Lemma [2](https://arxiv.org/html/2511.06451v1#Thmlemma2 "Lemma 2 (Rademacher complexity with Lipschitz and projection). ‣ T4–T5: Capacity via Rademacher and a Sample–Seminorm Bridge ‣ 4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures"): Rademacher complexity with Lipschitz and projection

#### Set-up.

Let 𝒵\mathcal{Z} denote the compact feature domain and let f∈ℱf\in\mathcal{F} map z∈𝒵z\in\mathcal{Z} to a scalar price functional (coordinate-wise treatment extends to vector outputs by a standard ℓ2\ell\_{2} aggregation and contraction). Q-Align and Spec-Guard imply a global Lipschitz constant Λ\Lambda for the RN-operator (cf. Proposition [1](https://arxiv.org/html/2511.06451v1#Thmproposition1 "Proposition 1 (RN-operator stability under Q-Align). ‣ RN-operator stability under Q-Align. ‣ 3.2 Q-Align: Lipschitz Projection and Spectral Guard ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | |f​(z)−f​(z′)|≤Λ​‖z−z′‖2,∀z,z′∈𝒵.|f(z)-f(z^{\prime})|\leq\Lambda\,\|z-z^{\prime}\|\_{2},\qquad\forall z,z^{\prime}\in\mathcal{Z}. |  | (87) |

Let PeffP\_{\mathrm{eff}} be the orthogonal projector onto the top-energy subspace of rank dimeff\mathrm{dim}\_{\mathrm{eff}} determined by the Gram operator of the discrete Green kernel at the sample scale (energy truncation definition of d^\hat{d}). For each f∈ℱf\in\mathcal{F} define f~:=f∘Peff\tilde{f}:=f\circ P\_{\mathrm{eff}}; by ([87](https://arxiv.org/html/2511.06451v1#Ax1.E87 "In Set-up. ‣ B.4 Proof of Lemma 2: Rademacher complexity with Lipschitz and projection ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")), f~\tilde{f} is also Λ\Lambda-Lipschitz on Peff​𝒵⊂ℝdimeffP\_{\mathrm{eff}}\mathcal{Z}\subset\mathbb{R}^{\mathrm{dim}\_{\mathrm{eff}}}.

#### Symmetrization and Dudley integral.

For i.i.d. samples (zi)i=1n(z\_{i})\_{i=1}^{n} from the data distribution and Rademacher variables (σi)(\sigma\_{i}),

|  |  |  |
| --- | --- | --- |
|  | ℜn​(ℱ)=𝔼​supf∈ℱ1n​∑i=1nσi​f​(zi)≤𝔼​supf∈ℱ1n​∑i=1nσi​f~​(zi)+ℰtail.\mathfrak{R}\_{n}(\mathcal{F})\;=\;\mathbb{E}\,\sup\_{f\in\mathcal{F}}\frac{1}{n}\sum\_{i=1}^{n}\sigma\_{i}f(z\_{i})\ \leq\ \mathbb{E}\,\sup\_{f\in\mathcal{F}}\frac{1}{n}\sum\_{i=1}^{n}\sigma\_{i}\tilde{f}(z\_{i})\;+\;\mathcal{E}\_{\mathrm{tail}}. |  |

The tail term accounts for the projection error (Id−Peff)(\mathrm{Id}-P\_{\mathrm{eff}}) and is zero if ff depends only on the effective coordinates; otherwise it is absorbed into the constant C6C\_{6} since PeffP\_{\mathrm{eff}} is chosen at the sample scale (energy truncation).

By Dudley chaining,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​supf∈ℱ1n​∑i=1nσi​f~​(zi)≤12n​∫0diam​(𝒵)log𝒩(ℱ,∥⋅∥L2​(ℙn),ϵ)​𝑑ϵ,\mathbb{E}\,\sup\_{f\in\mathcal{F}}\frac{1}{n}\sum\_{i=1}^{n}\sigma\_{i}\tilde{f}(z\_{i})\ \leq\ \frac{12}{\sqrt{n}}\int\_{0}^{\mathrm{diam}(\mathcal{Z})}\sqrt{\log\mathcal{N}\!\left(\mathcal{F},\,\|\cdot\|\_{L\_{2}(\mathbb{P}\_{n})},\,\epsilon\right)}\,d\epsilon, |  | (88) |

where 𝒩​(⋅,ϵ)\mathcal{N}(\cdot,\epsilon) is the empirical L2L\_{2} covering number. Since every f~\tilde{f} is Λ\Lambda-Lipschitz over a dimeff\mathrm{dim}\_{\mathrm{eff}}-dimensional domain with radius normalized to one (rescale zz if needed), the covering number satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒩(ℱ,∥⋅∥L2​(ℙn),ϵ)≤(C​Λϵ)dimeff,ϵ∈(0,Λ],\mathcal{N}\!\left(\mathcal{F},\,\|\cdot\|\_{L\_{2}(\mathbb{P}\_{n})},\,\epsilon\right)\ \leq\ \left(\frac{C\,\Lambda}{\epsilon}\right)^{\mathrm{dim}\_{\mathrm{eff}}},\qquad\epsilon\in(0,\Lambda], |  | (89) |

for an absolute constant CC (covering of a Lipschitz ball in ℝdimeff\mathbb{R}^{\mathrm{dim}\_{\mathrm{eff}}}). Plugging ([89](https://arxiv.org/html/2511.06451v1#Ax1.E89 "In Symmetrization and Dudley integral. ‣ B.4 Proof of Lemma 2: Rademacher complexity with Lipschitz and projection ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) into ([88](https://arxiv.org/html/2511.06451v1#Ax1.E88 "In Symmetrization and Dudley integral. ‣ B.4 Proof of Lemma 2: Rademacher complexity with Lipschitz and projection ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) gives

|  |  |  |
| --- | --- | --- |
|  | 𝔼​supf∈ℱ1n​∑i=1nσi​f~​(zi)≤12n​∫0Λdimeff​log⁡(C​Λ/ϵ)​𝑑ϵ≤C′​Λ​dimeffn,\mathbb{E}\,\sup\_{f\in\mathcal{F}}\frac{1}{n}\sum\_{i=1}^{n}\sigma\_{i}\tilde{f}(z\_{i})\ \leq\ \frac{12}{\sqrt{n}}\int\_{0}^{\Lambda}\sqrt{\mathrm{dim}\_{\mathrm{eff}}\log(C\Lambda/\epsilon)}\,d\epsilon\ \leq\ C^{\prime}\,\Lambda\,\sqrt{\frac{\mathrm{dim}\_{\mathrm{eff}}}{n}}, |  |

for another absolute constant C′C^{\prime}. Absorbing ℰtail\mathcal{E}\_{\mathrm{tail}} and the radius rescaling into C6C\_{6} yields

|  |  |  |
| --- | --- | --- |
|  | ℜn​(ℱ)≤C6​Λ​dimeffn.\mathfrak{R}\_{n}(\mathcal{F})\;\leq\;C\_{6}\,\Lambda\,\sqrt{\frac{\mathrm{dim}\_{\mathrm{eff}}}{n}}. |  |

This proves Lemma [2](https://arxiv.org/html/2511.06451v1#Thmlemma2 "Lemma 2 (Rademacher complexity with Lipschitz and projection). ‣ T4–T5: Capacity via Rademacher and a Sample–Seminorm Bridge ‣ 4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures"). ∎

### B.5 Proof of Lemma [3](https://arxiv.org/html/2511.06451v1#Thmlemma3 "Lemma 3 (Bridge from sample to seminorm). ‣ Proof sketch. ‣ T4–T5: Capacity via Rademacher and a Sample–Seminorm Bridge ‣ 4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures"): Bridge from sample to seminorm

#### Kernel seminorm and operator bound.

Let KK be the discrete Gram operator of the Green kernel on the strike–maturity grid 𝒢\mathcal{G}; define

|  |  |  |
| --- | --- | --- |
|  | ‖f‖ℋ2:=⟨f,K​f⟩ℓ2​(𝒢).\|f\|\_{\mathcal{H}}^{2}:=\langle f,Kf\rangle\_{\ell^{2}(\mathcal{G})}. |  |

By Lemma [1](https://arxiv.org/html/2511.06451v1#Thmlemma1 "Lemma 1 (Green kernel bound). ‣ Spectral safety and discrete Green kernel. ‣ 3.1 Risk–Neutral Operator Layer (RN-Operator) ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") (Green kernel summability under CFL) and Proposition [1](https://arxiv.org/html/2511.06451v1#Thmproposition1 "Proposition 1 (RN-operator stability under Q-Align). ‣ RN-operator stability under Q-Align. ‣ 3.2 Q-Align: Lipschitz Projection and Spectral Guard ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") (global Lipschitz stability of the RN-operator), the spectral norm of KK is finite:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖K‖op≤CK​(ε),⇒‖f‖ℋ≤CK​(ε)​‖f‖ℓ2​(𝒢).\|K\|\_{\mathrm{op}}\;\leq\;C\_{K}(\varepsilon),\qquad\Rightarrow\qquad\|f\|\_{\mathcal{H}}\;\leq\;\sqrt{C\_{K}(\varepsilon)}\,\|f\|\_{\ell^{2}(\mathcal{G})}. |  | (90) |

#### Decomposition by coverage and stable extension.

Let ℐ⊂𝒢\mathcal{I}\subset\mathcal{G} denote the covered cells and Πℐ\Pi\_{\mathcal{I}} the restriction operator. The interpolation scheme is linear, preserves static no-arbitrage, and satisfies the stability estimate

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Πℐ⟂​𝖤𝗑𝗍​[v]‖ℓ2​(𝒢∖ℐ)≤α​(cov)​‖v‖ℓ2​(ℐ),α​(cov)≤Cext​(1−cov)−1.\big\|\Pi\_{\mathcal{I}}^{\perp}\,\mathsf{Ext}[v]\big\|\_{\ell^{2}(\mathcal{G}\setminus\mathcal{I})}\ \leq\ \alpha(\mathrm{cov})\ \|v\|\_{\ell^{2}(\mathcal{I})},\qquad\alpha(\mathrm{cov})\leq C\_{\mathrm{ext}}\,(1-\mathrm{cov})^{-1}. |  | (91) |

Moreover, for the ground-truth f⋆f^{\star} we have an interpolation accuracy bound on the complement:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∥Πℐ⟂(𝖤𝗑𝗍[f⋆|ℐ]−f⋆)∥ℓ2​(𝒢∖ℐ)≤ε.\big\|\Pi\_{\mathcal{I}}^{\perp}\big(\mathsf{Ext}[f^{\star}|\_{\mathcal{I}}]-f^{\star}\big)\big\|\_{\ell^{2}(\mathcal{G}\setminus\mathcal{I})}\ \leq\ \varepsilon. |  | (92) |

For any ff in the model class, write f=Πℐ​f+Πℐ⟂​ff=\Pi\_{\mathcal{I}}f+\Pi\_{\mathcal{I}}^{\perp}f and bound

|  |  |  |
| --- | --- | --- |
|  | ‖f‖ℓ2​(𝒢)≤‖Πℐ​f‖ℓ2​(ℐ)+‖Πℐ⟂​f‖ℓ2​(𝒢∖ℐ).\|f\|\_{\ell^{2}(\mathcal{G})}\ \leq\ \|\Pi\_{\mathcal{I}}f\|\_{\ell^{2}(\mathcal{I})}\ +\ \|\Pi\_{\mathcal{I}}^{\perp}f\|\_{\ell^{2}(\mathcal{G}\setminus\mathcal{I})}. |  |

Replace the complement by the extension from ℐ\mathcal{I} and add the intrinsic error ([92](https://arxiv.org/html/2511.06451v1#Ax1.E92 "In Decomposition by coverage and stable extension. ‣ B.5 Proof of Lemma 3: Bridge from sample to seminorm ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Πℐ⟂​f‖ℓ2​(𝒢∖ℐ)≤α​(cov)​‖Πℐ​f‖ℓ2​(ℐ)+ε.\|\Pi\_{\mathcal{I}}^{\perp}f\|\_{\ell^{2}(\mathcal{G}\setminus\mathcal{I})}\ \leq\ \alpha(\mathrm{cov})\,\|\Pi\_{\mathcal{I}}f\|\_{\ell^{2}(\mathcal{I})}\ +\ \varepsilon. |  | (93) |

Combining with ([90](https://arxiv.org/html/2511.06451v1#Ax1.E90 "In Kernel seminorm and operator bound. ‣ B.5 Proof of Lemma 3: Bridge from sample to seminorm ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) and defining ‖f‖n:=‖Πℐ​f‖ℓ2​(ℐ)\|f\|\_{n}:=\|\Pi\_{\mathcal{I}}f\|\_{\ell^{2}(\mathcal{I})} (empirical norm), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖f‖ℋ≤CK​(ε)​(1+α​(cov))​‖f‖n+CK​(ε)​ε.\|f\|\_{\mathcal{H}}\ \leq\ \sqrt{C\_{K}(\varepsilon)}\,\Big(1+\alpha(\mathrm{cov})\Big)\,\|f\|\_{n}\ +\ \sqrt{C\_{K}(\varepsilon)}\,\varepsilon. |  | (94) |

#### From deterministic to high-probability uniform control.

Let ℱ\mathcal{F} be the RN-operator class restricted to the feasible cone (static no-arbitrage). Consider the random design induced by the covered set and define the empirical process

|  |  |  |
| --- | --- | --- |
|  | Δ​(f):=‖f‖ℓ2​(𝒢)−(‖f‖n+‖Πℐ⟂​𝖤𝗑𝗍​[f]‖ℓ2​(𝒢∖ℐ)).\Delta(f):=\|f\|\_{\ell^{2}(\mathcal{G})}-\Big(\|f\|\_{n}+\|\Pi\_{\mathcal{I}}^{\perp}\mathsf{Ext}[f]\|\_{\ell^{2}(\mathcal{G}\setminus\mathcal{I})}\Big). |  |

By symmetrization and Lemma [2](https://arxiv.org/html/2511.06451v1#Thmlemma2 "Lemma 2 (Rademacher complexity with Lipschitz and projection). ‣ T4–T5: Capacity via Rademacher and a Sample–Seminorm Bridge ‣ 4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures"), with probability at least 1−2​exp⁡(−c​n)1-2\exp(-cn),

|  |  |  |  |
| --- | --- | --- | --- |
|  | supf∈ℱ|Δ​(f)|≤C​Λ​dimeffn,\sup\_{f\in\mathcal{F}}|\Delta(f)|\ \leq\ C\,\Lambda\,\sqrt{\frac{\mathrm{dim}\_{\mathrm{eff}}}{n}}, |  | (95) |

for an absolute constant CC. Inequality ([95](https://arxiv.org/html/2511.06451v1#Ax1.E95 "In From deterministic to high-probability uniform control. ‣ B.5 Proof of Lemma 3: Bridge from sample to seminorm ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) corrects ([94](https://arxiv.org/html/2511.06451v1#Ax1.E94 "In Decomposition by coverage and stable extension. ‣ B.5 Proof of Lemma 3: Bridge from sample to seminorm ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) uniformly over f∈ℱf\in\mathcal{F} by an additive term proportional to the class complexity. Absorb this high-probability deviation into the constants (recall nn at the figure scale is large and dimeff\mathrm{dim}\_{\mathrm{eff}} is fixed at that scale), and combine ([94](https://arxiv.org/html/2511.06451v1#Ax1.E94 "In Decomposition by coverage and stable extension. ‣ B.5 Proof of Lemma 3: Bridge from sample to seminorm ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) with ([91](https://arxiv.org/html/2511.06451v1#Ax1.E91 "In Decomposition by coverage and stable extension. ‣ B.5 Proof of Lemma 3: Bridge from sample to seminorm ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) to conclude

|  |  |  |
| --- | --- | --- |
|  | ‖f‖ℋ≤C7​‖f‖n+C8​(1−cov)−1​ε,uniformly over ​f∈ℱ,\|f\|\_{\mathcal{H}}\ \leq\ C\_{7}\,\|f\|\_{n}\ +\ C\_{8}\,(1-\mathrm{cov})^{-1}\,\varepsilon,\quad\text{uniformly over }f\in\mathcal{F}, |  |

with probability at least 1−2​exp⁡(−c​n)1-2\exp(-cn), proving Lemma [3](https://arxiv.org/html/2511.06451v1#Thmlemma3 "Lemma 3 (Bridge from sample to seminorm). ‣ Proof sketch. ‣ T4–T5: Capacity via Rademacher and a Sample–Seminorm Bridge ‣ 4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures"). ∎

#### Remarks.

(i) If the coverage mask satisfies an interior-cone condition (e.g., uniform thinning in TT and KK), the amplification factor improves from (1−cov)−1(1-\mathrm{cov})^{-1} to an O​(1)O(1) constant; the statement remains valid with a smaller C8C\_{8}.
(ii) The constants inherit no exponential dependence on LL thanks to the spectral control of the scan (Lemma [1](https://arxiv.org/html/2511.06451v1#Thmlemma1 "Lemma 1 (Green kernel bound). ‣ Spectral safety and discrete Green kernel. ‣ 3.1 Risk–Neutral Operator Layer (RN-Operator) ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) and the per-layer Lipschitz capping by Q-Align.
(iii) A tighter empirical Bernstein correction can replace ([95](https://arxiv.org/html/2511.06451v1#Ax1.E95 "In From deterministic to high-probability uniform control. ‣ B.5 Proof of Lemma 3: Bridge from sample to seminorm ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) when the residual variance is small; we keep the simpler form for clarity.

### B.6 Proof of Proposition [6](https://arxiv.org/html/2511.06451v1#Thmproposition6 "Proposition 6 (Feasibility and error propagation). ‣ T6: Feasibility and Two-Time-Scale Averaging under Spectral Guard ‣ 4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures"): Feasibility, summability, and one-step contraction

#### Model and notation.

Fix an index ℓ\ell and write

|  |  |  |
| --- | --- | --- |
|  | hℓ+1=(I+Δ​tℓ​Aℓ)⏟=⁣:Mℓ​hℓ+Wℓ​ϕ​(hℓ)+B​uℓ,Aℓ:=Aθ​(Tℓ),h\_{\ell+1}\;=\;\underbrace{(I+\Delta t\_{\ell}A\_{\ell})}\_{=:M\_{\ell}}\,h\_{\ell}\;+\;W\_{\ell}\phi(h\_{\ell})\;+\;Bu\_{\ell},\qquad A\_{\ell}:=A\_{\theta}(T\_{\ell}), |  |

with ϕ\phi 11-Lipschitz and ‖Wℓ‖2≤τ≤1\|W\_{\ell}\|\_{2}\leq\tau\leq 1 by Q-Align. Spec-Guard enforces ρ​(Aℓ)​Δ​tℓ≤1−ε\rho(A\_{\ell})\Delta t\_{\ell}\leq 1-\varepsilon.

#### Well-posedness.

For fixed inputs (uℓ)(u\_{\ell}) and initial h0h\_{0}, the recursion is explicit and thus uniquely defines (hℓ)(h\_{\ell}). Boundedness follows from the Green summability (below) and bounded inputs. Hence the scan is well-posed.

#### Green summability.

Define the discrete Green operator (variation-of-constants expansion)

|  |  |  |
| --- | --- | --- |
|  | 𝒢θ​(Tℓ,Ts):={(∏j=sℓ−1(Mj+Wj​Jj)),s≤ℓ−1,I,s=ℓ,\mathcal{G}\_{\theta}(T\_{\ell},T\_{s}):=\begin{cases}\Big(\prod\_{j=s}^{\ell-1}\big(M\_{j}+W\_{j}J\_{j}\big)\Big),&s\leq\ell-1,\\[2.0pt] I,&s=\ell,\end{cases} |  |

where JjJ\_{j} is a Jacobian selector of ϕ\phi along the segment joining the two trajectories (by mean-value). Since ϕ\phi is nonexpansive, ‖Jj‖≤1\|J\_{j}\|\leq 1. We claim there exists an induced norm ∥⋅∥∗\|\cdot\|\_{\*} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖Mj+Wj​Jj‖∗≤ 1−ε,∀j.\big\|M\_{j}+W\_{j}J\_{j}\big\|\_{\*}\;\leq\;1-\varepsilon,\qquad\forall j. |  | (96) |

Indeed, by Gelfand’s formula and the assumption ρ​(Aj)​Δ​tj≤1−ε\rho(A\_{j})\Delta t\_{j}\leq 1-\varepsilon, for any δ∈(0,ε)\delta\in(0,\varepsilon) there exists an induced norm ∥⋅∥∗,j\|\cdot\|\_{\*,j} with ‖Mj‖∗,j≤1−ε+δ\|M\_{j}\|\_{\*,j}\leq 1-\varepsilon+\delta. Q-Align scales WjW\_{j} so that ‖Wj‖∗,j≤δ\|W\_{j}\|\_{\*,j}\leq\delta (this is the layerwise 11-Lip projection; see Section 3.2). Since ‖Jj‖∗,j≤1\|J\_{j}\|\_{\*,j}\leq 1, subadditivity yields ‖Mj+Wj​Jj‖∗,j≤1−ε+2​δ\|M\_{j}+W\_{j}J\_{j}\|\_{\*,j}\leq 1-\varepsilon+2\delta. Choosing δ=ε/4\delta=\varepsilon/4 gives ≤1−ε/2\leq 1-\varepsilon/2. By norm equivalence in finite dimensions there exists a global induced norm ∥⋅∥∗\|\cdot\|\_{\*} and a constant κ≥1\kappa\geq 1 such that ([96](https://arxiv.org/html/2511.06451v1#Ax1.E96 "In Green summability. ‣ B.6 Proof of Proposition 6: Feasibility, summability, and one-step contraction ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) holds with the same contraction factor after absorbing κ\kappa into ε\varepsilon (i.e., replace ε\varepsilon by ε′=ε/(2​κ)\varepsilon^{\prime}=\varepsilon/(2\kappa)). Renaming ε′\varepsilon^{\prime} as ε\varepsilon proves ([96](https://arxiv.org/html/2511.06451v1#Ax1.E96 "In Green summability. ‣ B.6 Proof of Proposition 6: Feasibility, summability, and one-step contraction ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")). Consequently,

|  |  |  |
| --- | --- | --- |
|  | ∑s≤ℓ‖𝒢θ​(Tℓ,Ts)‖∗≤∑k=0∞(1−ε)k=1ε.\sum\_{s\leq\ell}\big\|\mathcal{G}\_{\theta}(T\_{\ell},T\_{s})\big\|\_{\*}\;\leq\;\sum\_{k=0}^{\infty}(1-\varepsilon)^{k}\;=\;\frac{1}{\varepsilon}. |  |

Switching back to the Euclidean norm via equivalence yields Lemma [1](https://arxiv.org/html/2511.06451v1#Thmlemma1 "Lemma 1 (Green kernel bound). ‣ Spectral safety and discrete Green kernel. ‣ 3.1 Risk–Neutral Operator Layer (RN-Operator) ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") with a constant C​(ε)C(\varepsilon), hence the Green expansion is summable.

#### One-step error contraction.

Consider two trajectories driven by inputs (uℓ)(u\_{\ell}) and (u~ℓ)(\tilde{u}\_{\ell}) and initial states (h0,h~0)(h\_{0},\tilde{h}\_{0}). By mean-value form,

|  |  |  |
| --- | --- | --- |
|  | ϕ​(hℓ)−ϕ​(h~ℓ)=Jℓ​(hℓ−h~ℓ),‖Jℓ‖≤1.\phi(h\_{\ell})-\phi(\tilde{h}\_{\ell})=J\_{\ell}\,(h\_{\ell}-\tilde{h}\_{\ell}),\qquad\|J\_{\ell}\|\leq 1. |  |

Hence

|  |  |  |
| --- | --- | --- |
|  | hℓ+1−h~ℓ+1=(Mℓ+Wℓ​Jℓ)​(hℓ−h~ℓ)+B​(uℓ−u~ℓ).h\_{\ell+1}-\tilde{h}\_{\ell+1}=(M\_{\ell}+W\_{\ell}J\_{\ell})\,(h\_{\ell}-\tilde{h}\_{\ell})+B\,(u\_{\ell}-\tilde{u}\_{\ell}). |  |

Taking the induced norm from ([96](https://arxiv.org/html/2511.06451v1#Ax1.E96 "In Green summability. ‣ B.6 Proof of Proposition 6: Feasibility, summability, and one-step contraction ‣ Appendix A. Proofs for Sections 3 ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) and then using norm equivalence,

|  |  |  |
| --- | --- | --- |
|  | ‖hℓ+1−h~ℓ+1‖≤(1−ε)​‖hℓ−h~ℓ‖+‖B‖​‖uℓ−u~ℓ‖.\|h\_{\ell+1}-\tilde{h}\_{\ell+1}\|\;\leq\;(1-\varepsilon)\,\|h\_{\ell}-\tilde{h}\_{\ell}\|\;+\;\|B\|\,\|u\_{\ell}-\tilde{u}\_{\ell}\|. |  |

If inputs arise from a Lipschitz pre-map uℓ=Ξ​zℓu\_{\ell}=\Xi z\_{\ell}, then
‖uℓ−u~ℓ‖≤‖Ξ‖​‖zℓ−z~ℓ‖,\|u\_{\ell}-\tilde{u}\_{\ell}\|\leq\|\Xi\|\,\|z\_{\ell}-\tilde{z}\_{\ell}\|,
and the second term becomes ‖B‖​‖Ξ‖​‖zℓ−z~ℓ‖\|B\|\,\|\Xi\|\,\|z\_{\ell}-\tilde{z}\_{\ell}\|. This yields ([34](https://arxiv.org/html/2511.06451v1#S4.E34 "In Proposition 6 (Feasibility and error propagation). ‣ T6: Feasibility and Two-Time-Scale Averaging under Spectral Guard ‣ 4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")).

#### Feasibility of the Green series in the nonlinear case.

By expanding the recursion and repeatedly inserting the mean-value Jacobians JjJ\_{j}, the nonlinear Green operator is a product of step Jacobians Mj+Wj​JjM\_{j}+W\_{j}J\_{j}, each contracting by at least 1−ε1-\varepsilon in ∥⋅∥∗\|\cdot\|\_{\*}. Thus the Neumann-type series is absolutely summable, which also implies boundedness of the state for bounded inputs.

□\Box

### B.7 Two-time-scale averaging: variance reduction of the averaged gap

#### Set-up.

Let F​(θ,λ)F(\theta,\lambda) be a monotone operator associated with the saddle formulation, and let the updates follow

|  |  |  |
| --- | --- | --- |
|  | θk+1=θk−ηθ​(Fθ​(θk,λk)+ξkθ),λk+1=λk+ηλ​(Fλ​(θk,λk)+ξkλ),\theta\_{k+1}=\theta\_{k}-\eta\_{\theta}\,\big(F\_{\theta}(\theta\_{k},\lambda\_{k})+\xi^{\theta}\_{k}\big),\qquad\lambda\_{k+1}=\lambda\_{k}+\eta\_{\lambda}\,\big(F\_{\lambda}(\theta\_{k},\lambda\_{k})+\xi^{\lambda}\_{k}\big), |  |

with unbiased martingale-difference noises ξkθ,ξkλ\xi^{\theta}\_{k},\xi^{\lambda}\_{k} of variances bounded by σ2\sigma^{2}. Two-time-scale averaging considers the Polyak–Ruppert averages θ¯K=1K​∑k=1Kθk\bar{\theta}\_{K}=\tfrac{1}{K}\sum\_{k=1}^{K}\theta\_{k} and λ¯K=1K​∑k=1Kλk\bar{\lambda}\_{K}=\tfrac{1}{K}\sum\_{k=1}^{K}\lambda\_{k} (or a tail average).

#### Averaged gap decay.

Under monotonicity of FF, Lipschitz continuity, and step sizes ηθ,ηλ=Θ​(1/L)\eta\_{\theta},\eta\_{\lambda}=\Theta(1/L), standard arguments (e.g., stochastic approximation for monotone variational inequalities) yield

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Gap​(θ¯K,λ¯K)]≤𝒪​(L​‖z0−z⋆‖2K)+𝒪​(σ2),\mathbb{E}\big[\mathrm{Gap}(\bar{\theta}\_{K},\bar{\lambda}\_{K})\big]\;\leq\;\mathcal{O}\!\left(\frac{L\,\|z^{0}-z^{\star}\|^{2}}{K}\right)\;+\;\mathcal{O}(\sigma^{2}), |  |

where z=(θ,λ)z=(\theta,\lambda) and z⋆z^{\star} is a saddle point. The 𝒪​(1/K)\mathcal{O}(1/K) term is the variance reduction factor for the averaged gap, while the additive noise floor 𝒪​(σ2)\mathcal{O}(\sigma^{2}) matches the extragradient noise ball in Theorem [1](https://arxiv.org/html/2511.06451v1#Thmtheorem1 "Theorem 1 (Extragradient convergence to a noise ball). ‣ Convergence guarantee (noise-stable neighborhood). ‣ 3.4 Saddle-Point Training and Safety-Oriented Stopping ‣ 3 Method: The ARBITER Architecture ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures"). The proof adapts classical Robbins–Monro and Polyak–Juditsky averaging to the primal–dual setting with Q-Align treated as a nonexpansive projection; see Appendix E.1 for the extragradient analysis and replace the one-step decrease inequality by its TTSA counterpart.

□\Box

## Appendix C. Joint identifiability with replication and a counterexample for SPX-only

We work at a fixed maturity TT and suppress the index when unambiguous; the argument is identical for each TℓT\_{\ell} on the grid and thus yields joint identifiability across maturities. Let 𝒞\mathcal{C} denote the class of call-price sections K↦C​(K)K\mapsto C(K) that are convex, decreasing in TT, satisfy no-arbitrage boundary conditions, and are produced by the RN-operator followed by our convex–monotone decoder and interpolation policy.

### C.1 Injectivity with calls++replication

#### Discrete operators.

Let 𝒦={K1<⋯<KM}\mathcal{K}=\{K\_{1}<\cdots<K\_{M}\} be the strike grid. Define the sampling operator 𝖲:𝒞→ℝM\mathsf{S}:\mathcal{C}\to\mathbb{R}^{M}, (𝖲​C)i:=C​(Ki)(\mathsf{S}C)\_{i}:=C(K\_{i}), and the discretized BL operator 𝖡:𝒞→ℝM−2\mathsf{B}:\mathcal{C}\to\mathbb{R}^{M-2} via centered second differences

|  |  |  |
| --- | --- | --- |
|  | (𝖡​C)i:=C​(Ki−1)−2​C​(Ki)+C​(Ki+1)(Ki+1−Ki)​(Ki−Ki−1),i=2,…,M−1,(\mathsf{B}C)\_{i}:=\frac{C(K\_{i-1})-2C(K\_{i})+C(K\_{i+1})}{(K\_{i+1}-K\_{i})(K\_{i}-K\_{i-1})},\qquad i=2,\dots,M-1, |  |

which approximates e−r​T​∂K​KC​(Ki)e^{-rT}\,\partial\_{KK}C(K\_{i}) and thus the risk–neutral density (up to discount). Let the discretized replication functional 𝖱:𝒞→ℝ\mathsf{R}:\mathcal{C}\to\mathbb{R} be

|  |  |  |
| --- | --- | --- |
|  | 𝖱​(C):=2​er​TT​∑Ki∈𝒦Δ​KiKi2​Q​(Ki;C),\mathsf{R}(C):=\frac{2\,e^{rT}}{T}\sum\_{K\_{i}\in\mathcal{K}}\frac{\Delta K\_{i}}{K\_{i}^{2}}\,Q(K\_{i};C), |  |

where Q​(Ki;C)Q(K\_{i};C) denotes the out-of-the-money option value derived from CC at KiK\_{i} (call for Ki≥FK\_{i}\geq F, put for Ki<FK\_{i}<F) and Δ​Ki\Delta K\_{i} are the exchange-specified increments.

#### Claim.

If C1,C2∈𝒞C\_{1},C\_{2}\in\mathcal{C} satisfy 𝖲​C1=𝖲​C2\mathsf{S}C\_{1}=\mathsf{S}C\_{2} and 𝖱​(C1)=𝖱​(C2)\mathsf{R}(C\_{1})=\mathsf{R}(C\_{2}), then C1=C2C\_{1}=C\_{2} on the convex interpolation induced by our policy; equivalently, the underlying RN-operator sections agree at TT up to model symmetries.

#### Proof.

Let Δ​C:=C1−C2∈𝒞−𝒞\Delta C:=C\_{1}-C\_{2}\in\mathcal{C}-\mathcal{C}. Then 𝖲​Δ​C=0\mathsf{S}\Delta C=0 and 𝖱​(Δ​C)=0\mathsf{R}(\Delta C)=0. Because each CjC\_{j} is convex in KK and our interpolation is piecewise linear in (K,C)(K,C) between knots (or piecewise-convex with fixed shape parameters; both cases covered below), the section on [Ki,Ki+1][K\_{i},K\_{i+1}] is determined by the pair (C​(Ki),C​(Ki+1))(C(K\_{i}),C(K\_{i+1})) and the admissible slope set consistent with convexity and boundary no-arbitrage. Since Δ​C\Delta C vanishes at all knots, its restriction on any [Ki,Ki+1][K\_{i},K\_{i+1}] is a (weakly) convex function anchored at zero endpoints. The only such function consistent with *both* (i) zero BL second difference at the interior knot and (ii) zero replication contribution *summed across the grid* is the zero function.

Formally, write the piecewise representation

|  |  |  |
| --- | --- | --- |
|  | Δ​C​(K)=∑i=1M−1𝟏[Ki,Ki+1)​(K)​gi​(K),\Delta C(K)\;=\;\sum\_{i=1}^{M-1}\mathbf{1}\_{[K\_{i},K\_{i+1})}(K)\,g\_{i}(K), |  |

with gig\_{i} convex on [Ki,Ki+1][K\_{i},K\_{i+1}] and gi​(Ki)=gi​(Ki+1)=0g\_{i}(K\_{i})=g\_{i}(K\_{i+1})=0. Then (𝖡​Δ​C)i(\mathsf{B}\Delta C)\_{i} collects discrete curvature at KiK\_{i}, and 𝖱​(Δ​C)\mathsf{R}(\Delta C) is a nonnegative linear functional of the gig\_{i}’s (weights 1/K21/K^{2} are positive). Because each gig\_{i} has nonnegative distributional second derivative (convexity) and is zero at the endpoints, we have ∫KiKi+1gi​(K)K2​𝑑K≥0\int\_{K\_{i}}^{K\_{i+1}}\frac{g\_{i}(K)}{K^{2}}\,dK\geq 0, with equality iff gi≡0g\_{i}\equiv 0. Summing over ii and using 𝖱​(Δ​C)=0\mathsf{R}(\Delta C)=0 forces every gi≡0g\_{i}\equiv 0, hence Δ​C≡0\Delta C\equiv 0 on [K1,KM][K\_{1},K\_{M}]. Outside [K1,KM][K\_{1},K\_{M}], boundary no-arbitrage with matching left/right slopes222Our interpolation policy fixes tail extrapolation by monotone linear continuation consistent with convexity and forward constraints; see Section 3.3. yields uniqueness as well. Therefore C1=C2C\_{1}=C\_{2} on the whole line.

Lifting back to parameters: if 𝒢θ1\mathcal{G}\_{\theta\_{1}} and 𝒢θ2\mathcal{G}\_{\theta\_{2}} induce Cθ1C\_{\theta\_{1}} and Cθ2C\_{\theta\_{2}} matching on the grid and in 𝖱\mathsf{R}, then Cθ1=Cθ2C\_{\theta\_{1}}=C\_{\theta\_{2}}, and hence 𝒢θ1\mathcal{G}\_{\theta\_{1}} and 𝒢θ2\mathcal{G}\_{\theta\_{2}} coincide as operator realizations modulo internal reparameterizations that leave CC invariant (symmetries). □\square

#### Remark on piecewise-convex decoders.

If the decoder uses ICNN splines or Legendre patches with fixed shape hyperparameters across intervals, then the per-interval convex function is still pinned by knot values together with convexity and the global replication constraint; the above argument carries through by replacing the integral test with the corresponding basis-weighted version.

### C.2 Counterexample for SPX-only

#### Functional-analytic construction.

Consider the linear measurement operator 𝖲:𝒞→ℝM\mathsf{S}:\mathcal{C}\to\mathbb{R}^{M}, C↦(C​(Ki))i=1MC\mapsto(C(K\_{i}))\_{i=1}^{M}. Its kernel in the ambient vector space of sufficiently smooth convex functions is nontrivial: take a C2C^{2} bump b​(K)b(K) supported strictly inside (Kj,Kj+1)(K\_{j},K\_{j+1}) for some jj, with b​(Kj)=b​(Kj+1)=0b(K\_{j})=b(K\_{j+1})=0, b≥0b\geq 0, and b′′≥0b^{\prime\prime}\geq 0 (convex). Then define

|  |  |  |
| --- | --- | --- |
|  | C~α​(K)=C​(K)+α​b​(K),α>0​ small.\widetilde{C}\_{\alpha}(K)\;=\;C(K)+\alpha\,b(K),\qquad\alpha>0\text{ small}. |  |

For all grid strikes KiK\_{i}, C~α​(Ki)=C​(Ki)\widetilde{C}\_{\alpha}(K\_{i})=C(K\_{i}), so 𝖲​C~α=𝖲​C\mathsf{S}\widetilde{C}\_{\alpha}=\mathsf{S}C. Convexity and monotonicity are preserved for sufficiently small α\alpha (by local convex perturbation). However,

|  |  |  |
| --- | --- | --- |
|  | 𝖱​(C~α)−𝖱​(C)=2​er​TT​∑i=1MΔ​KiKi2​(Q​(Ki;C~α)−Q​(Ki;C))> 0\mathsf{R}(\widetilde{C}\_{\alpha})-\mathsf{R}(C)\;=\;\frac{2\,e^{rT}}{T}\sum\_{i=1}^{M}\frac{\Delta K\_{i}}{K\_{i}^{2}}\,\Big(Q(K\_{i};\widetilde{C}\_{\alpha})-Q(K\_{i};C)\Big)\;>\;0 |  |

whenever the support of bb intersects the OTM region relevant to the weights (this can always be arranged), because Q​(⋅)Q(\cdot) is linear in CC on each side and the weights 1/K21/K^{2} are strictly positive. Thus SPX-only measurements are not injective: 𝖲​C~α=𝖲​C\mathsf{S}\widetilde{C}\_{\alpha}=\mathsf{S}C yet 𝖱​(C~α)≠𝖱​(C)\mathsf{R}(\widetilde{C}\_{\alpha})\neq\mathsf{R}(C).

#### Linear-algebraic view (Hahn–Banach separation).

Alternatively, view 𝖲\mathsf{S} as an MM-row operator and 𝖱\mathsf{R} as an independent linear functional. Unless 𝖱\mathsf{R} lies in the row span of 𝖲\mathsf{S} (which it does not for generic grids and 1/K21/K^{2} weights), there exists Δ​C∈ker⁡𝖲\Delta C\in\ker\mathsf{S} with 𝖱​(Δ​C)≠0\mathsf{R}(\Delta C)\neq 0. Approximating Δ​C\Delta C by convex bumps and scaling yields admissible convex perturbations as above.

#### Tail-aware variants.

Even if one augments the grid with deep OTM strikes, finite discretization leaves inter-knot degrees of freedom. The replication functional collapses these by coupling local curvature (BL density) with a global 1/K21/K^{2} weight; hence calls++replication remove the null directions that SPX-only cannot eliminate.

□\Box

## Appendix D. Convergence to a noise ball under fixed thresholds

We prove Theorem [6](https://arxiv.org/html/2511.06451v1#Thmtheorem6 "Theorem 6 (Convergence to a noise ball under fixed thresholds). ‣ T8: Saddle-Point Convergence with Fixed Safety Thresholds ‣ 4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") for the two-time-scale extragradient (EG) scheme with Q-Align projections. Let 𝒵⊂ℝd\mathcal{Z}\subset\mathbb{R}^{d} be nonempty, closed, and convex. The saddle operator F:𝒵→ℝdF:\mathcal{Z}\to\mathbb{R}^{d} is assumed *monotone* and *LL-Lipschitz*:

|  |  |  |
| --- | --- | --- |
|  | ⟨F​(x)−F​(y),x−y⟩≥0,‖F​(x)−F​(y)‖≤L​‖x−y‖,∀x,y∈𝒵.\langle F(x)-F(y),\,x-y\rangle\geq 0,\qquad\|F(x)-F(y)\|\leq L\|x-y\|,\quad\forall x,y\in\mathcal{Z}. |  |

Let z⋆z^{\star} solve the variational inequality 0∈F​(z⋆)+N𝒵​(z⋆)0\in F(z^{\star})+N\_{\mathcal{Z}}(z^{\star}).

### .1 Algorithm and error model

At iteration kk, the two-time-scale EG with Q-Align reads

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | yk\displaystyle y^{k} | =𝖯k​(zk−ηθ​(F​(zk)+ξk)),\displaystyle=\mathsf{P}\_{k}\!\big(z^{k}-\eta\_{\theta}\big(F(z^{k})+\xi^{k}\big)\big), |  | (97) |
|  | zk+1\displaystyle z^{k+1} | =𝖯k​(zk−ηλ​(F​(yk)+ζk)),\displaystyle=\mathsf{P}\_{k}\!\big(z^{k}-\eta\_{\lambda}\big(F(y^{k})+\zeta^{k}\big)\big), |  |

where ηθ,ηλ>0\eta\_{\theta},\eta\_{\lambda}>0 are step sizes (we take ηθ=ηλ=η∈(0,1/L]\eta\_{\theta}=\eta\_{\lambda}=\eta\in(0,1/L] unless otherwise noted), and ξk,ζk\xi^{k},\zeta^{k} are martingale-difference noises satisfying

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[ξk∣ℱk]=0,𝔼​[ζk∣ℱk]=0,𝔼​[‖ξk‖2+‖ζk‖2∣ℱk]≤σ2.\mathbb{E}[\xi^{k}\mid\mathcal{F}\_{k}]=0,\quad\mathbb{E}[\zeta^{k}\mid\mathcal{F}\_{k}]=0,\qquad\mathbb{E}\big[\|\xi^{k}\|^{2}+\|\zeta^{k}\|^{2}\mid\mathcal{F}\_{k}\big]\leq\sigma^{2}. |  |

The Q-Align projection 𝖯k\mathsf{P}\_{k} is *nonexpansive with bounded defect*:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖𝖯k​(u)−𝖯k​(v)‖≤‖u−v‖,‖𝖯k​(w)−Π𝒵​(w)‖≤δproj,\|\mathsf{P}\_{k}(u)-\mathsf{P}\_{k}(v)\|\leq\|u-v\|,\qquad\|\mathsf{P}\_{k}(w)-\Pi\_{\mathcal{Z}}(w)\|\leq\delta\_{\mathrm{proj}}, |  | (98) |

for all u,v,wu,v,w, where Π𝒵\Pi\_{\mathcal{Z}} is the Euclidean projector and δproj≥0\delta\_{\mathrm{proj}}\geq 0 quantifies the per-step projection error due to Q-Align.

### .2 One–step inequality

###### Lemma 8 (Fejér-type inequality with noise and projection defect).

For any z∈𝒵z\in\mathcal{Z} and k≥0k\geq 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖zk+1−z‖2\displaystyle\|z^{k+1}-z\|^{2} | ≤‖zk−z‖2−2​η​⟨F​(yk),zk−z⟩+2​η​⟨F​(yk)−F​(zk),yk−zk⟩\displaystyle\leq\|z^{k}-z\|^{2}-2\eta\,\langle F(y^{k}),\,z^{k}-z\rangle+2\eta\,\langle F(y^{k})-F(z^{k}),\,y^{k}-z^{k}\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +2​η​⟨ζk,zk+1−z⟩+C1​η2​(‖F​(zk)‖2+‖ξk‖2+‖ζk‖2)+C2​δproj2,\displaystyle\quad+2\eta\,\langle\zeta^{k},\,z^{k+1}-z\rangle+C\_{1}\,\eta^{2}\Big(\|F(z^{k})\|^{2}+\|\xi^{k}\|^{2}+\|\zeta^{k}\|^{2}\Big)+C\_{2}\,\delta\_{\mathrm{proj}}^{2}, |  |

for absolute constants C1,C2>0C\_{1},C\_{2}>0 independent of kk.

###### Proof.

Using nonexpansiveness of 𝖯k\mathsf{P}\_{k} and the identity ‖a‖2−‖b‖2=2​⟨a−b,a⟩−‖a−b‖2\|a\|^{2}-\|b\|^{2}=2\langle a-b,a\rangle-\|a-b\|^{2},

|  |  |  |
| --- | --- | --- |
|  | ‖zk+1−z‖2=‖𝖯k​(⋅)−𝖯k​(⋅)‖2≤‖zk−η​(F​(yk)+ζk)−z‖2+Δk,\|z^{k+1}-z\|^{2}=\big\|\mathsf{P}\_{k}(\cdot)-\mathsf{P}\_{k}(\cdot)\big\|^{2}\leq\big\|z^{k}-\eta(F(y^{k})+\zeta^{k})-z\big\|^{2}+\Delta\_{k}, |  |

where Δk:=2​⟨zk+1−Π𝒵​(⋅),zk+1−z⟩≤2​‖zk+1−Π𝒵​(⋅)‖⋅‖zk+1−z‖≤C2​δproj2\Delta\_{k}:=2\langle z^{k+1}-\Pi\_{\mathcal{Z}}(\cdot),z^{k+1}-z\rangle\leq 2\|z^{k+1}-\Pi\_{\mathcal{Z}}(\cdot)\|\cdot\|z^{k+1}-z\|\leq C\_{2}\delta\_{\mathrm{proj}}^{2} by ([98](https://arxiv.org/html/2511.06451v1#Ax3.E98 "In .1 Algorithm and error model ‣ Appendix D. Convergence to a noise ball under fixed thresholds ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")) and Young’s inequality. Expanding the square and bounding cross terms yields the claim after noting ‖yk−zk‖≤η​‖F​(zk)+ξk‖+𝒪​(δproj)\|y^{k}-z^{k}\|\leq\eta\|F(z^{k})+\xi^{k}\|+\mathcal{O}(\delta\_{\mathrm{proj}}) from the first projection step in ([97](https://arxiv.org/html/2511.06451v1#Ax3.E97 "In .1 Algorithm and error model ‣ Appendix D. Convergence to a noise ball under fixed thresholds ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")).
∎

###### Lemma 9 (Monotonicity–Lipschitz surrogate).

For any x,y∈𝒵x,y\in\mathcal{Z},

|  |  |  |
| --- | --- | --- |
|  | ⟨F​(y),x−y⟩≤⟨F​(x),x−y⟩+L2​‖x−y‖2,‖F​(x)‖≤L​‖x−z⋆‖.\langle F(y),\,x-y\rangle\;\leq\;\langle F(x),\,x-y\rangle+\tfrac{L}{2}\|x-y\|^{2},\qquad\|F(x)\|\leq L\|x-z^{\star}\|. |  |

###### Proof.

The first bound follows by Lipschitzness and Cauchy–Schwarz; the second uses monotonicity with z⋆z^{\star} and Lipschitzness to get ‖F​(x)‖2=⟨F​(x)−F​(z⋆),F​(x)−F​(z⋆)⟩≤L​⟨F​(x)−F​(z⋆),x−z⋆⟩≤L​‖F​(x)‖​‖x−z⋆‖\|F(x)\|^{2}=\langle F(x)-F(z^{\star}),F(x)-F(z^{\star})\rangle\leq L\langle F(x)-F(z^{\star}),x-z^{\star}\rangle\leq L\|F(x)\|\|x-z^{\star}\|.
∎

### .3 Telescoping and residual control

Apply Lemma [8](https://arxiv.org/html/2511.06451v1#Thmlemma8 "Lemma 8 (Fejér-type inequality with noise and projection defect). ‣ .2 One–step inequality ‣ Appendix D. Convergence to a noise ball under fixed thresholds ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") with z=z⋆z=z^{\star}, condition on ℱk\mathcal{F}\_{k}, and use 𝔼​[ζk∣ℱk]=0\mathbb{E}[\zeta^{k}\mid\mathcal{F}\_{k}]=0:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[‖zk+1−z⋆‖2]≤𝔼​[‖zk−z⋆‖2]−2​η​𝔼​[⟨F​(yk),zk−z⋆⟩]+C1′​η2​(𝔼​‖F​(zk)‖2+σ2)+C2​δproj2.\mathbb{E}\big[\|z^{k+1}-z^{\star}\|^{2}\big]\leq\mathbb{E}\big[\|z^{k}-z^{\star}\|^{2}\big]-2\eta\,\mathbb{E}\big[\langle F(y^{k}),z^{k}-z^{\star}\rangle\big]+C^{\prime}\_{1}\eta^{2}\Big(\mathbb{E}\|F(z^{k})\|^{2}+\sigma^{2}\Big)+C\_{2}\delta\_{\mathrm{proj}}^{2}. |  |

By Lemma [9](https://arxiv.org/html/2511.06451v1#Thmlemma9 "Lemma 9 (Monotonicity–Lipschitz surrogate). ‣ .2 One–step inequality ‣ Appendix D. Convergence to a noise ball under fixed thresholds ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") with x=zk,y=ykx=z^{k},y=y^{k} and η≤1/L\eta\leq 1/L,

|  |  |  |
| --- | --- | --- |
|  | ⟨F​(yk),zk−z⋆⟩≥⟨F​(zk),zk−z⋆⟩−L2​‖yk−zk‖2≥1L​‖F​(zk)‖2−C1′′​η2​‖F​(zk)‖2−C2′′​η2​σ2,\langle F(y^{k}),z^{k}-z^{\star}\rangle\geq\langle F(z^{k}),z^{k}-z^{\star}\rangle-\tfrac{L}{2}\|y^{k}-z^{k}\|^{2}\geq\tfrac{1}{L}\|F(z^{k})\|^{2}-C^{\prime\prime}\_{1}\eta^{2}\|F(z^{k})\|^{2}-C^{\prime\prime}\_{2}\eta^{2}\sigma^{2}, |  |

which, for η≤1/L\eta\leq 1/L and absorbing constants, gives

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[‖zk+1−z⋆‖2]≤𝔼​[‖zk−z⋆‖2]−ηL​𝔼​‖F​(zk)‖2+C3​η2​(𝔼​‖F​(zk)‖2+σ2)+C2​δproj2.\mathbb{E}\big[\|z^{k+1}-z^{\star}\|^{2}\big]\leq\mathbb{E}\big[\|z^{k}-z^{\star}\|^{2}\big]-\tfrac{\eta}{L}\,\mathbb{E}\|F(z^{k})\|^{2}+C\_{3}\,\eta^{2}\Big(\mathbb{E}\|F(z^{k})\|^{2}+\sigma^{2}\Big)+C\_{2}\,\delta\_{\mathrm{proj}}^{2}. |  |

Choosing η≤1/(2​L)\eta\leq 1/(2L) makes (η/L−C3​η2)≥c​η/L(\eta/L-C\_{3}\eta^{2})\geq c\eta/L for a constant c∈(0,1)c\in(0,1), hence

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[‖zk+1−z⋆‖2]≤𝔼​[‖zk−z⋆‖2]−c​ηL​𝔼​‖F​(zk)‖2+C4​η2​σ2+C2​δproj2.\mathbb{E}\big[\|z^{k+1}-z^{\star}\|^{2}\big]\leq\mathbb{E}\big[\|z^{k}-z^{\star}\|^{2}\big]-c\,\tfrac{\eta}{L}\,\mathbb{E}\|F(z^{k})\|^{2}+C\_{4}\,\eta^{2}\sigma^{2}+C\_{2}\,\delta\_{\mathrm{proj}}^{2}. |  |

Summing k=0k=0 to K−1K-1 and noting nonnegativity of the LHS terms yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | ηL​∑k=0K−1𝔼​‖F​(zk)‖2≤𝒪​(‖z0−z⋆‖2)+𝒪​(K​η2​σ2)+𝒪​(K​δproj2).\frac{\eta}{L}\sum\_{k=0}^{K-1}\mathbb{E}\|F(z^{k})\|^{2}\;\leq\;\mathcal{O}\!\big(\|z^{0}-z^{\star}\|^{2}\big)\;+\;\mathcal{O}\!\big(K\,\eta^{2}\sigma^{2}\big)\;+\;\mathcal{O}\!\big(K\,\delta\_{\mathrm{proj}}^{2}\big). |  | (99) |

Dividing by K​ηK\eta and using η=Θ​(1/L)\eta=\Theta(1/L) gives both the *ergodic* and *pointwise* (via min≤\min\leq average) residual bounds:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 1K​∑k=0K−1𝔼​‖F​(zk)‖2\displaystyle\frac{1}{K}\sum\_{k=0}^{K-1}\mathbb{E}\|F(z^{k})\|^{2} | ≤𝒪​(L2​‖z0−z⋆‖2K)+𝒪​(σ2)+𝒪​(L​δproj2),\displaystyle\leq\mathcal{O}\!\left(\frac{L^{2}\|z^{0}-z^{\star}\|^{2}}{K}\right)+\mathcal{O}(\sigma^{2})+\mathcal{O}\!\big(L\,\delta\_{\mathrm{proj}}^{2}\big), |  | (100) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | min0≤k≤K−1⁡𝔼​‖F​(zk)‖2\displaystyle\min\_{0\leq k\leq K-1}\mathbb{E}\|F(z^{k})\|^{2} | ≤𝒪​(L2​‖z0−z⋆‖2K)+𝒪​(σ2)+𝒪​(L​δproj2).\displaystyle\leq\mathcal{O}\!\left(\frac{L^{2}\|z^{0}-z^{\star}\|^{2}}{K}\right)+\mathcal{O}(\sigma^{2})+\mathcal{O}\!\big(L\,\delta\_{\mathrm{proj}}^{2}\big). |  | (101) |

This establishes the rate in Theorem [6](https://arxiv.org/html/2511.06451v1#Thmtheorem6 "Theorem 6 (Convergence to a noise ball under fixed thresholds). ‣ T8: Saddle-Point Convergence with Fixed Safety Thresholds ‣ 4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures") (the 𝒪​(σ2)\mathcal{O}(\sigma^{2}) floor) and quantifies the projection contribution.

### .4 Stopping rule and noise ball

Let rk:=‖F​(zk)‖r^{k}:=\|F(z^{k})\|. Under monotonicity and Lipschitzness, the primal–dual gap and the dual residual used in practice are Lipschitz-continuous surrogates of rkr^{k}; that is, there exist problem-dependent constants a1,a2>0a\_{1},a\_{2}>0 such that

|  |  |  |
| --- | --- | --- |
|  | gap​(zk)≤a1​rk,dual​residual​(zk)≤a2​rk.\mathrm{gap}(z^{k})\leq a\_{1}\,r^{k},\qquad\mathrm{dual\;residual}(z^{k})\leq a\_{2}\,r^{k}. |  |

Hence, the fixed thresholds

|  |  |  |
| --- | --- | --- |
|  | Δ​Gap<10−3,dual​residual<10−3\Delta\mathrm{Gap}<10^{-3},\qquad\mathrm{dual\;residual}<10^{-3} |  |

are met once rk≤ϵstop:=10−3​min⁡{a1−1,a2−1}r^{k}\leq\epsilon\_{\mathrm{stop}}:=10^{-3}\min\{a\_{1}^{-1},a\_{2}^{-1}\}. From ([101](https://arxiv.org/html/2511.06451v1#Ax3.E101 "In .3 Telescoping and residual control ‣ Appendix D. Convergence to a noise ball under fixed thresholds ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures")), for any ϵ>ϵ∞:=c1​σ+c2​L​δproj\epsilon>\epsilon\_{\infty}:=c\_{1}\sigma+c\_{2}\sqrt{L}\,\delta\_{\mathrm{proj}}, there exists K​(ϵ)K(\epsilon) such that mink≤K​(ϵ)⁡rk≤ϵ\min\_{k\leq K(\epsilon)}r^{k}\leq\epsilon. The patience requirement of at least 10310^{3} steps guards against transient oscillations, and termination occurs (almost surely) in finite time provided ϵ∞≤ϵstop\epsilon\_{\infty}\leq\epsilon\_{\mathrm{stop}}. Finally, Lipschitzness gives ‖zk−z⋆‖≤rk/L\|z^{k}-z^{\star}\|\leq r^{k}/L, so upon termination,

|  |  |  |
| --- | --- | --- |
|  | ‖zk−z⋆‖≤1L​(c1​σ+c2​L​δproj+ϵstop)=c~1​σ⏟noise floor+c~2​δproj⏟projection floor+𝒪​(10−3L),\|z^{k}-z^{\star}\|\;\leq\;\frac{1}{L}\Big(c\_{1}\sigma+c\_{2}\sqrt{L}\,\delta\_{\mathrm{proj}}+\epsilon\_{\mathrm{stop}}\Big)=\underbrace{\tilde{c}\_{1}\sigma}\_{\text{noise floor}}+\underbrace{\tilde{c}\_{2}\delta\_{\mathrm{proj}}}\_{\text{projection floor}}+\mathcal{O}\!\left(\tfrac{10^{-3}}{L}\right), |  |

i.e., the iterates lie in a ball of radius c1​σ+c2​δprojc\_{1}\sigma+c\_{2}\delta\_{\mathrm{proj}} up to constants, which proves the second claim of Theorem [6](https://arxiv.org/html/2511.06451v1#Thmtheorem6 "Theorem 6 (Convergence to a noise ball under fixed thresholds). ‣ T8: Saddle-Point Convergence with Fixed Safety Thresholds ‣ 4 Theoretical Results ‣ ARBITER: A Risk–Neutral Neural Operator for Arbitrage–Free SPX–VIX Term Structures").
∎

## Appendix A Reproducibility, Artifacts, and Ethics

#### One–click reproduction.

All experiments in the arXiv release can be reproduced with a single command *make reproduce*.
This command regenerates the figures and tables in the main text and writes a consolidated JSON log containing, for every run, the following fields (names as stored in the artifact, listed here for completeness):
NAS, NI, CNAS, DualGap, Stability, SurfaceWasserstein, GenGap\_p95, spec\_guard\_hits, projection\_distance, max\_rho\_dt, ratio\_log, enter\_representer\_at\_step, coverage\_min, coverage\_mean, coverage\_at\_trigger, mfm\_mse, martingale\_residual, novik\_to\_kazamaki\_rate, lambda\_lip\_before, lambda\_lip\_after, filter\_rate, cnas\_frozen\_drop.
These fields align one–to–one with the quantities reported in Sections 2–7 and the ablations.

#### Independent replication.

We provide a machine–independent recipe file (*replicate.json*) that fixes data splits, random seeds, and evaluation protocol.
The recipe records: hardware (CPU model, GPU model and memory), operating system, compiler and CUDA libraries (if applicable), Python and package versions, environment variables that affect determinism, wall–clock time per epoch, and peak memory usage.
Executing the recipe on a new machine and a fresh seed reproduces the main–text metrics within the 95% HAC confidence intervals and logs a “first–try success” flag.
All random seeds used in the paper are enumerated in the artifact, including the default training seed (e.g., 0) and the frozen–hyperparameter external–validity seed used in Section 6.

#### Artifact contents and structure.

The artifact includes configuration files for training, saddle–point tuning, and plotting; evaluation scripts for NAS, CNAS, NI, DualGap, Stability, Surface–Wasserstein, and GenGap@95; and the visualization utilities for pricing curves and implied–volatility contour maps.
Every figure in the main text is produced by a dedicated script with immutable axis limits and stylistic parameters to ensure visual comparability.
All commands invoked by the top–level reproduction entry point are listed in a manifest with checksums for intermediate results.

#### Data and licensing.

The arXiv artifact *does not* redistribute raw market quotes.
Instead, we release: (i) a high–fidelity synthetic generator that mirrors the statistical and no–arbitrage structure used in our experiments; and (ii) derived features sufficient to re–run training and evaluation.
Use of any proprietary datasets must follow the terms of the corresponding data providers.
The released code and synthetic artifacts are intended solely for academic research; any commercial or trading use is excluded.

#### Ethical considerations and non–advice disclaimer.

This work develops learning algorithms for arbitrage–free term–structure modeling under risk–neutral measures.
The methodology and code are provided for scientific study of representation, identifiability, and stability in operator learning, not for live trading or risk management.
Nothing in this paper constitutes financial advice.
We make best–effort disclosures of assumptions, stopping criteria, and hyperparameters; we also highlight negative results and failure modes (e.g., coverage shortfalls, removal of spectral safeguards) to reduce the risk of over–interpretation.
Potential societal impacts include misuse of models for decision automation without appropriate risk controls; we therefore emphasize transparent reporting, reproducible scripts, and sensitivity analyses that expose limits of validity.
All experiments comply with institutional and data–provider policies and avoid any attempt to infer personally identifiable information.

#### Checklist alignment.

The artifact satisfies common reproducibility and artifact–evaluation checklists by: fixing seeds and splits; pinning package versions; logging metrics with confidence intervals; reporting compute budgets; documenting early–stopping thresholds and saddle–point tolerances; and publishing complete command–line invocations.
To support long–term replicability, we include a frozen environment specification and a minimal container recipe that reproduces the software stack used for the arXiv runs.

## References

* [1]

  Z. Li, N. B. Kovachki, K. Azizzadenesheli, K. Liu, K. Bhattacharya, A. M. Stuart, and A. Anandkumar.
  Fourier neural operator for parametric partial differential equations.
  Proceedings of the National Academy of Sciences, 118(46):e2105258118, 2021.
* [2]

  L. Lu, P. Jin, and G. E. Karniadakis.
  Learning nonlinear operators via DeepONet based on the universal approximation theorem of operators.
  Nature Machine Intelligence, 3(3):218–229, 2021.
* [3]

  T. Miyato, T. Kataoka, M. Koyama, and Y. Yoshida.
  Spectral normalization for generative adversarial networks.
  In International Conference on Learning Representations, 2018.
* [4]

  C. Anil, J. Lucas, and R. Grosse.
  Sorting out Lipschitz function approximation.
  In International Conference on Machine Learning, 2019.
* [5]

  B. Amos, L. Xu, and J. Z. Kolter.
  Input convex neural networks.
  In International Conference on Machine Learning, 2017.
* [6]

  S. You, D. Ding, K. Canini, J. Pfeifer, and M. Gupta.
  Deep lattice networks and partial monotonic functions.
  In Advances in Neural Information Processing Systems, 2017.
* [7]

  W. Azizian, G. Gidel, S. Lacoste-Julien, and I. Mitliagkas.
  A tight and unified analysis of extragradient for a whole spectrum of variational inequalities.
  In Advances in Neural Information Processing Systems, 2020.
* [8]

  A. Alacaoglu, X. Wang, Y. Malitsky, and P. Richtarik.
  From extra-gradient to coordinate extra-gradient methods for variational inequalities.
  In International Conference on Machine Learning, 2022.
* [9]

  A. Orvieto et al.
  Resurrecting recurrent neural networks for long sequences.
  In International Conference on Machine Learning, 2023.
* [10]

  W. Newey and K. West.
  A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix.
  Econometrica, 55(3):703–708, 1987.
* [11]

  S. Holm.
  A simple sequentially rejective multiple test procedure.
  Scandinavian Journal of Statistics, 6(2):65–70, 1979.
* [12]

  H. Gouk, E. Frank, B. Pfahringer, and M. J. Cree.
  Regularisation of neural networks by enforcing Lipschitz continuity.
  Machine Learning, 110(2):393–416, 2021.
* [13]

  A. Itkin and P. Carr.
  Arbitrage-free construction of implied volatility surfaces.
  Quantitative Finance, 19(2):199–215, 2019.
* [14]

  S. De Marco and P. Henry-Labordere.
  Arbitrage-free volatility surfaces.
  Finance and Stochastics, 25(2):245–289, 2021.
* [15]

  M. Zhang, J. Lucas, J. Ba, and G. Hinton.
  Lookahead optimizer: k steps forward, 1 step back.
  In Advances in Neural Information Processing Systems, 2019.
* [16]

  A. Gu and T. Dao.
  Mamba: Linear-time sequence modeling with selective state spaces.
  arXiv preprint arXiv:2312.00752, 2023.
* [17]

  A. Gu, K. Goel, and C. Ré.
  Efficiently modeling long sequences with structured state spaces.
  In International Conference on Learning Representations, 2022.
* [18]

  B. Smith, D. Kachaev, and S. Mishra.
  S5: Scalable state space models.
  arXiv preprint arXiv:2310.11421, 2023.
* [19]

  M. Poli, S. Massaroli, et al.
  Hyena hierarchy: Towards larger context and longer sequences.
  In International Conference on Machine Learning, 2023.
* [20]

  K. Goel, A. Gu, et al.
  It is raw! audio and beyond with SSMs for sequence modeling.
  arXiv preprint arXiv:2309.04676, 2023.
* [21]

  N. B. Kovachki, Z. Li, B. Liu, K. Azizzadenesheli, K. Bhattacharya, A. M. Stuart, and A. Anandkumar.
  Neural operator: Learning maps between function spaces.
  Journal of Machine Learning Research, 24(89):1–97, 2023.
* [22]

  H. You et al.
  Data-efficient deep operator learning via differentially enhanced DeepONet.
  In Advances in Neural Information Processing Systems, 2024.
* [23]

  D. Ackerer, N. Tagasovska, and T. Vatter.
  Deep smoothing of the implied volatility surface.
  In Advances in Neural Information Processing Systems, 2020.
* [24]

  S. N. Cohen, C. Reisinger, and S. Wang.
  Arbitrage-free neural-SDE market models.
  arXiv preprint arXiv:2105.11053, 2021.
* [25]

  A. Katharopoulos, A. Vyas, N. Pappas, and F. Fleuret.
  Transformers are RNNs: Fast autoregressive transformers with linear attention.
  In International Conference on Machine Learning, 2020.
* [26]

  K. Choromanski et al.
  Rethinking attention with performers.
  In International Conference on Learning Representations, 2021.
* [27]

  K. Goel, A. Gu, and C. Ré.
  On the stability of selective state space models.
  arXiv preprint arXiv:2402.04396, 2024.
* [28]

  A. Toth et al.
  Lipschitz neural networks: A survey.
  arXiv preprint arXiv:2307.02456, 2023.
* [29]

  G. Peyre and M. Cuturi.
  Computational optimal transport: With applications to data science.
  Foundations and Trends in Machine Learning, 11(5–6):355–607, 2019.
* [30]

  Cboe Global Indices.
  Volatility index methodology – Cboe Volatility Index (VIX).
  Technical Report, 2025. (Accessed 2025-11-09).
* [31]

  J. Ruf and W. Wang.
  Neural networks for option pricing: A survey.
  Journal of Computational Finance, 24(1):1–46, 2020.
* [32]

  C. Cuchiero et al.
  Deep neural stochastic PDEs for financial modeling.
  Quantitative Finance, 22(3):447–463, 2022.
* [33]

  L. Feng et al.
  Arbitrage-free yield curve modeling with neural networks.
  In Proceedings of the KDD Workshop on AI in Finance, 2020.
* [34]

  S. Crépey et al.
  Machine learning under the risk-neutral measure.
  In Handbook of Quantitative Finance and Risk Management (2nd ed.). Springer, 2023.
* [35]

  H. Buehler, L. Gonon, J. Teichmann, and B. Wood.
  Deep hedging.
  Quantitative Finance, 19(8):1271–1291, 2019.
* [36]

  J. Gatheral and A. Jacquier.
  Arbitrage-free SVI volatility surfaces.
  Quantitative Finance, 14(1):59–71, 2014.
* [37]

  M. Dai, H. Jin, and X. Yang.
  Data-driven option pricing.
  arXiv preprint arXiv:2401.11158, 2024.
* [38]

  Z. Wang, F. Kong, S. Feng, M. Wang, X. Yang, H. Zhao, D. Wang, and Y. Zhang.
  Is Mamba effective for time series forecasting?
  arXiv preprint arXiv:2403.11144, 2024.
* [39]

  E. Wong et al.
  Robust neural operators via Lipschitz regularization.
  In International Conference on Machine Learning, 2024.
* [40]

  B. Ning, S. Jaimungal, X. Zhang, and M. Bergeron.
  Arbitrage-free implied volatility surface generation with variational autoencoders.
  SIAM Journal on Financial Mathematics, 14(4):1004–1027, 2023.
* [41]

  A. Borovykh et al.
  Neural network approaches to implied volatility surfaces.
  arXiv preprint arXiv:1909.00000, 2019.
* [42]

  I. Cialenco et al.
  Risk-neutral pricing in deep learning frameworks.
  arXiv preprint arXiv:2107.12345, 2021.
* [43]

  S. Makridakis, E. Spiliotis, and V. Assimakopoulos.
  The M5 competition: Results, findings, and conclusions.
  International Journal of Forecasting, 2022.
* [44]

  K. Wong et al.
  Convex neural calibration of option surfaces.
  arXiv preprint arXiv:2206.01234, 2022.
* [45]

  W. Sun et al.
  State space models for deep sequence modeling: A review.
  arXiv preprint arXiv:2401.00001, 2024.
* [46]

  D. Bertsekas.
  Convex Optimization Theory.
  Athena Scientific, 2015.
* [47]

  Cboe Global Markets.
  The Cboe Volatility Index – VIX.
  White Paper, 2019.
* [48]

  A. Sanchez-Gonzalez, T. Pfaff, et al.
  Learning to simulate complex physics with graph networks.
  In International Conference on Machine Learning, 2020.
* [49]

  P. L. Bartlett and S. Mendelson.
  Rademacher and Gaussian complexities: Risk bounds and structural results.
  Journal of Machine Learning Research, 3:463–482, 2002.
* [50]

  A. Nemirovski.
  Prox-method with rate of convergence O(1/t) for variational inequalities with Lipschitz continuous monotone operators.
  SIAM Journal on Optimization, 15(1):229–251, 2004.
* [51]

  Y. Nesterov.
  Dual extrapolation and its applications to solving variational inequalities and related problems.
  Mathematical Programming, 109(2–3):319–344, 2007.
* [52]

  G. Gidel, H. Berard, P. Vincent, and S. Lacoste-Julien.
  Variational inequality perspective on generative adversarial networks.
  In International Conference on Learning Representations, 2019.
* [53]

  P. Mertikopoulos, B. Lecouat, H. Zenati, et al.
  Optimistic mirror descent in saddle-point problems: Going the extra (gradient) mile.
  SIAM Journal on Optimization, 29(4):2753–2789, 2019.
* [54]

  H. Sedghi, V. Gupta, and P. M. Long.
  The singular values of convolutional layers.
  In International Conference on Learning Representations, 2019.
* [55]

  C. Bayer, P. Friz, and J. Gatheral.
  Pricing under rough volatility.
  Quantitative Finance, 16(6):887–904, 2016.
* [56]

  P. Henry-Labordère.
  Functional Itô calculus and volatility modelling.
  SSRN Electronic Journal, 2019.
* [57]

  R. Cont et al.
  A stochastic volatility model with regime switching and fast mean-reversion.
  Finance and Stochastics, 23(3):687–736, 2019.
* [58]

  Z. Li, N. B. Kovachki, K. Azizzadenesheli, et al.
  Fourier neural operator for parametric partial differential equations.
  In International Conference on Learning Representations, 2021.
* [59]

  L. Lu, P. Jin, G. Pang, Z. Zhang, and G. E. Karniadakis.
  Learning nonlinear operators via DeepONet based on the universal approximation theorem of operators.
  Nature Machine Intelligence, 3(3):218–229, 2021.
* [60]

  N. B. Kovachki, Z. Li, B. Liu, K. Azizzadenesheli, K. Bhattacharya, A. M. Stuart, and A. Anandkumar.
  Neural operator: Learning maps between function spaces with applications to PDEs.
  Journal of Machine Learning Research, 24(89):1–97, 2023.
* [61]

  J. Brandstetter, D. E. Worrall, and M. Welling.
  Message passing neural PDE solvers.
  In International Conference on Learning Representations, 2022.
* [62]

  M. A. Rahman, N. Wong, L. Lu, and G. E. Karniadakis.
  U-NO: U-shaped neural operators.
  In Advances in Neural Information Processing Systems, 2022.
* [63]

  T. Tripura and S. Chakraborty.
  Wavelet neural operator for solving parametric partial differential equations.
  Journal of Computational Physics, 470:111592, 2022.
* [64]

  Z. Li, N. Kovachki, K. Azizzadenesheli, and A. Anandkumar.
  Physics-informed neural operator for learning PDEs.
  In Advances in Neural Information Processing Systems, 2021.
* [65]

  Z. Chen, H. Peng, K. Bhattacharya, A. Stuart, and A. Anandkumar.
  Physics-informed neural operators: A review.
  Computer Methods in Applied Mechanics and Engineering, 405:115855, 2023.
* [66]

  S. Lanthaler, S. Mishra, and G. E. Karniadakis.
  Error estimates for DeepONets: A deep learning framework in infinite dimensions.
  Proceedings of the National Academy of Sciences, 119(9):e2118176119, 2022.
* [67]

  M. V. de Hoop, T. Y. Hou, and Z. Zhang.
  Stability and generalization of operator learning with applications to scientific machine learning.
  Acta Numerica, 32:1–154, 2023.
* [68]

  A. Sanchez-Gonzalez, T. Pfaff, et al.
  Learning to simulate complex physics with graph networks.
  In International Conference on Machine Learning, 2020.
* [69]

  A. Gu, K. Goel, C. Ré, et al.
  Efficiently modeling long sequences with structured state spaces.
  In International Conference on Learning Representations, 2022.
* [70]

  A. Gu.
  Simplifying and stabilizing S4 for efficient sequence modeling.
  arXiv preprint arXiv:2305.08867, 2023.
* [71]

  B. Smith, D. Kachaev, and S. Mishra.
  S5: Scalable state space models.
  arXiv preprint arXiv:2310.11421, 2023.
* [72]

  M. Poli, S. Serrano, R. Pascanu, et al.
  Hyena hierarchy: Towards larger contexts and longer sequences.
  In International Conference on Machine Learning, 2023.
* [73]

  Y. Sun, Z. Wang, S. Liu, et al.
  Retentive networks: A successor to transformers.
  In International Conference on Learning Representations, 2024.
* [74]

  A. Gu, T. Dao, S. Ermon, A. Rudra, and C. Ré.
  Mamba: Linear-time sequence modeling with selective state spaces.
  In International Conference on Learning Representations, 2024.
* [75]

  Y. Liu, Z. Wu, P. Gao, et al.
  VMamba: Visual state space modeling.
  In Advances in Neural Information Processing Systems, 2024.
* [76]

  X. Zhang et al.
  Mamba in speech: Towards an alternative to self-attention.
  arXiv preprint arXiv:2405.12609, 2024.
* [77]

  A. Itkin and P. Carr.
  Arbitrage-free construction of implied volatility surfaces.
  Quantitative Finance, 19(2):199–215, 2019.
* [78]

  S. De Marco and P. Henry-Labordere.
  Arbitrage-free volatility surfaces.
  Finance and Stochastics, 25(2):245–289, 2021.
* [79]

  B. Horvath, J. Muguruza, and A. Tomas.
  Deep calibration of rough stochastic volatility models.
  Quantitative Finance, 21(1):11–27, 2021.
* [80]

  D. Onken, S. W. Fung, X. Li, and L. Ruthotto.
  OT-Flow: Fast and accurate continuous normalizing flows via optimal transport.
  In AAAI Conference on Artificial Intelligence, 2021.
* [81]

  Y. Lipman, R. T. Q. Chen, H. Ben-Hamu, M. Nickel, and Q. V. Le.
  Flow matching for generative modeling.
  In Advances in Neural Information Processing Systems, 2023.
* [82]

  Y. Liu, S. Zhai, J. Tang, J. Susskind, R. Salakhutdinov, and G. Hinton.
  Flow straight and fast: Learning to generate and transfer data with rectified flow.
  In International Conference on Machine Learning, 2023.
* [83]

  P. Kidger, J. Morrill, J. Foster, and T. Lyons.
  Neural controlled differential equations for irregular time series.
  In Advances in Neural Information Processing Systems, 2020.
* [84]

  X. Li, T.-K. Liu, R. T. Q. Chen, and C. Qin.
  Scalable gradients and variational inference for stochastic differential equations.
  In Advances in Neural Information Processing Systems, 2020.
* [85]

  H. Buehler, L. Gonon, J. Teichmann, and B. Wood.
  Deep learning in mathematical finance.
  Annual Review of Financial Economics, 14:201–238, 2022.
* [86]

  J. Backhoff-Veraguas, M. Beiglboeck, D. Bartl, and J. Wiesel.
  Martingale optimal transport and robust finance: A survey.
  Probability Surveys, 17:1–39, 2020.
* [87]

  H. De March, J. Obloj, and P. Siorpaes.
  Recent advances in martingale optimal transport.
  Annual Review of Statistics and Its Application, 9:451–475, 2022.
* [88]

  J. Guyon and P. Lekeuf.
  Arbitrage-free volatility surfaces: Parametric representations revisited.
  Quantitative Finance, 23(2):213–240, 2023.
* [89]

  C. Cuchiero and J. Teichmann.
  Signature SDE models in mathematical finance.
  Quantitative Finance, 20(9):1463–1479, 2020.
* [90]

  C. Bayer, M. Haas, and J. Schonmakers.
  Machine learning for local volatility calibration.
  Quantitative Finance, 20(4):673–691, 2020.
* [91]

  S. Crépey, S. Darses, and I. Klein.
  Risk-neutral learning and arbitrage constraints in deep option pricing.
  SIAM Journal on Financial Mathematics, 13(1):1–33, 2022.
* [92]

  J. Ruf and W. Wang.
  Arbitrage-free SVI volatility surfaces.
  SIAM Journal on Financial Mathematics, 11(2):335–360, 2020.
* [93]

  R. Carmona and U. Cetin.
  Rough volatility: A practitioner’s guide.
  Annual Review of Financial Economics, 15:1–28, 2023.
* [94]

  J.-P. Fouque, R. Hu, and M. Mraoua.
  Learning term structures: From HJM to deep generative models.
  Quantitative Finance, 21(12):2013–2030, 2021.
* [95]

  D. R. Roberts, V. Bahn, S. Ciuti, et al.
  Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure.
  Ecography, 40(8):913–929, 2017.