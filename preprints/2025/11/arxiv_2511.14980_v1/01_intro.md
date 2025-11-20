---
authors:
- Ahmet Umur Özsoy
doc_id: arxiv:2511.14980v1
family_id: arxiv:2511.14980
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton
  Framework'
url_abs: http://arxiv.org/abs/2511.14980v1
url_html: https://arxiv.org/html/2511.14980v1
venue: arXiv q-fin
version: 1
year: 2025
---


[umurozsoy@gmail.com](mailto:umurozsoy@gmail.com)
[

###### Abstract

Calibration of option pricing models is routinely repeated as markets evolve, yet modern systems lack an operator for removing data from a calibrated model without full retraining. When quotes become stale, corrupted, or subject to deletion requirements, existing calibration pipelines must rebuild the entire nonlinear least-squares problem, even if only a small subset of data must be excluded. In this work, we introduce a principled framework for selective forgetting (machine unlearning) in parametric option calibration. We provide stability guarantees, perturbation bounds, and show that the proposed operators satisfy local exactness under standard regularity assumptions.

###### keywords:

selective forgetting, option calibration, Gauss–Newton methods,
sufficient statistics, numerical unlearning, Heston model

## 1 Introduction

Modern financial models are not static; they are recalibrated as market conditions change.
Therefore calibrating parametric asset-pricing models to market data has always been an ongoing interest for both practitioners and academics in the field of mathematical finance.
Risk management systems along with trading desks rely heavily on the repeated solutions of inverse problems aimed at calibrating and adjusting parameters θ\theta so that the model-based prices m​(x;θ)m(x;\theta) reproduce observed quotes to some extent of accuracy.
Option-implied volatility surfaces evolve minute by minute, and model parameters such as
mean reversion, volatility of volatility, or correlation etc. are adapted to new market information.
Formally, calibration seeks parameters θ\theta minimizing a discrepancy between model generated prices
m​(x;θ)m(x;\theta) and observed quotes, typically through nonlinear least squares or
maximum-likelihood estimation.
This sort of inverse problem is present at models such as Heston and SABR
to structural credit, interest rate, and hybrid models and lies at almost all the operational core of
risk engines and trading platforms.

While long-standing research have refined the *estimating* or *learning* side of calibration of financial derivatives, options in our case, no interest has been shown to its conceptual dual, *unlearning*.
When certain data becomes corrupted, obsolete, or subject to possible deletion requests,
the model should exclude its influence without a full recalibration from scratch.
Therefore deletion and data retraction could become necessities as quotes expire, bad ticks or outlier surfaces are purged, and perhaps regulatory obligations (e.g. GDPR, audit requests, or data licensing constraints) require that specific records be removed from already-calibrated models.
The question is immediate yet unsolved, therefore the question becomes how a calibrated model retract the influence of certain data without a full recalibration from scratch.
The removal (i.e., deletion) of certain subsets of available data from an already trained models has emerged recently in machine learning as *Machine Unlearning* or *Selective Forgetting*.
The essence of such approaches casts a simple question whether or not the exclusion of a subset of data requires retraining on the remaining data, [ginart2019making, bourtoule2021machine, sekhari2021remember, qu2024learn, guo2019certified],
and has become central to privacy-aware and data-efficient algorithm design.

In financial modeling, however, unlearning has not been formalized.
To address this, we introduce a principled framework for *machine unlearning in option calibration*.
Our goal is to update calibrated parameters as if certain quotes had never been observed,
without re-accessing or reprocessing the entire dataset.
We cast calibration as a nonlinear least-squares problem solved by Gauss–Newton iterations
and show that the normal-equation structure naturally supports machine unlearning.

The term *machine unlearning* has traditionally referred to privacy-motivated deletion in which the goal is to modify a trained model so that it becomes indistinguishable from one that
was never exposed to the deleted data [ginart2019making].
That definition requires a probabilistic or differential-privacy guarantee, an epistemic statement that an observer cannot tell whether the forgotten data ever influenced the model.

Our work adopts the unlearning viewpoint in a different, numerical sense that is particularly natural for calibration.
We are not concerned with information-theoretic indistinguishability, but with the *computational removal of numerical influence*.
Given a parametric model m​(x;θ)m(x;\theta) calibrated on market data DD, and a subset F⊂DF\subset D of quotes to be discarded (e.g., due to stale prices or data errors), our
objective is to obtain parameters

|  |  |  |
| --- | --- | --- |
|  | θ′=arg⁡minθ⁡J​(θ;D∖F),\theta^{\prime}\;=\;\arg\min\_{\theta}J(\theta;D\setminus F), |  |

*without reprocessing all of DD*.
In this setting, unlearning means reproducing the same parameter update that full retraining on D∖FD\setminus F would yield, up to machine precision.
This provides a strict advantage as retraining on large option datasets could be expensive, especially for models with higher complexity.
Hence the *forgetting* is not about privacy or randomness in our point of view, but about *efficiently erasing the numerical footprint* of specific data in parameter space. We refer to [zhang2023review] and [nguyen2025survey] for recent and well articulated examples of review of *Machine Unlearning* as the literature is quite vast to provide deep holistic view.

Even though we touch upon the fact that no interest has been shown to the removal of data that compels a recalibration, there are studies that are directionally *forward in time* in which the models are refit periodically conditional on the accumulation of *new* data, for instance  [date2011linear], [broto2004estimation], [bakshi1997empirical], [broadie2007model].
Such studies perform incremental steps on new samples, by the very nature of it.
By construction, however, they do not address the inverse problem of properly removing the informational contribution of a specific subset of observations while reproducing the solution that would have been obtained had those observations never been used.

Calibration could be repeated thousands of times as market conditions evolve, often under strict latency and consistency constraints.
This increases our interest in *Machine Unlearning* as a strong reason of removal bulk amount of data might be on cleaning corrupted data.
Even in stable markets, bad ticks, stale or misrecorded quotes could exist and distort calibration.
Therefore unlearning such contaminated shards of data could improve calibration precision without retraining the model from scratch.
Consider that a pricing engine or feed producing several days of quotes with a decimal-shift bug, instead of full retrain; unlearning those days might realign the parameters with the clean market.
Therefore, especially inspired by the SISA (Sharded Isolated Sliced Aggregation) paradigm from [bourtoule2021machine], we suggest two unlearning operators by showing that in nonlinear calibration, the Gauss–Newton equations can be reorganized into algebraically additive terms that admit exact deletion operators as the apparent simplicity hides a structural insight.

This work introduces a principled framework for *selective forgetting* (machine unlearning) in parametric option calibration, formulated under the standard Gauss–Newton (GN) least-squares setting used in Heston-type models.
Given an initially calibrated parameter vector θ\theta fitted on a dataset of option quotes D={(xi,yi)}D=\{(x\_{i},y\_{i})\}, the goal is to efficiently update θ\theta to the parameter that would result from retraining on the retained subset D∖FD\setminus F, without accessing the full dataset again.
Our contributions are both algorithmic and theoretical.
We first design a shard-aware decomposition of the GN normal equations and then we prove that this system coincides exactly with the one obtained by retraining on D∖FD\setminus F at a fixed linearization. We term this approach the sharded recompute as it enables machine-precision unlearning with partial data access and provides a scalable, shard-local recalibration architecture for option models.
We then develop a data-free *refactor* operator that realizes exact forgetting without reopening any raw quotes making this the first exact forgetting operator for nonlinear least-squares calibration models, to our knowledge.
The approach achieves retraining-level accuracy while remaining completely data-free once the sufficient statistics (ui,ψi)(u\_{i},\psi\_{i}) are cached.

We further show in synthetic option datasets that our framework achieves near-zero degradation in calibration accuracy compared to full retraining, while reducing computational cost by an order of magnitude or more.
The proposed framework supports operational scenarios in which data must be removed due to regulatory, contractual, or quality-control reasons, providing a principled and efficient alternative to discarding and recalibrating the entire dataset.
By applying selective forgetting to targeted subsets (e.g., quotes from specific dates or sources), we measure their influence on calibrated parameters and pricing accuracy, enabling a form of leave-one-shard-out sensitivity analysis for option pricing models.
Overall, this study bridges the emerging field of machine unlearning with the long-standing problem of derivative model calibration, introducing both a novel theoretical framework and an immediately applicable methodology for real-world financial modeling.
Beyond computational efficiency, the proposed framework positions unlearning as a fundamental complement to calibration in model management.
In large-scale pricing and risk systems, models must not only learn from new data but also *forget* obsolete or restricted information.
The machine unlearning operators developed here establish an analytical bridge between machine unlearning and quantitative finance, enabling the first operator-theoretic treatment of data deletion in stochastic-volatility model calibration.

## 2 Formulation of the unlearning problem

The unlearning procedure proposed in this study operates purely on the normal equations of the Gauss–Newton method.
As such, it does not modify the underlying option pricing model, the risk-neutral pricing map, or any no-arbitrage structure inherent to the parametric family.
While the numerical experiments use European calls under the Heston model for analytical clarity,
the proposed forgetting framework extends to any differentiable pricing map,
including exotic or path-dependent contracts evaluated by Monte Carlo or adjoint methods.
The machine unlearning calibration framework developed here does respect all classical no-arbitrage and mathematical finance principles (i.e., monotonicity, convexity, existence of the equivalent martingale measures etc.) to the same extent as the underlying model calibrated.
In this section, we first discuss preliminaries and then mathematically develop the machine unlearning operators.

### 2.1 Preliminaries

We consider the problem of calibration of the Heston model to European call option prices.
Under the risk–neutral measure, the Heston dynamics for the asset price StS\_{t} and its variance vtv\_{t} are

|  |  |  |
| --- | --- | --- |
|  | d​St=r​St​d​t+vt​St​d​WtS,d​vt=κ​(θv−vt)​d​t+σv​vt​d​Wtv,\mathrm{d}S\_{t}=rS\_{t}\,\mathrm{d}t+\sqrt{v\_{t}}S\_{t}\,\mathrm{d}W\_{t}^{S},\qquad\mathrm{d}v\_{t}=\kappa(\theta\_{v}-v\_{t})\,\mathrm{d}t+\sigma\_{v}\sqrt{v\_{t}}\,\mathrm{d}W\_{t}^{v}, |  |

with d​⟨WS,Wv⟩t=ρ​d​t\mathrm{d}\langle W^{S},W^{v}\rangle\_{t}=\rho\,\mathrm{d}t.
The parameter vector is
θ=(κ,θv,σv,ρ,v0)\theta=(\kappa,\theta\_{v},\sigma\_{v},\rho,v\_{0}).
Call option prices m​(x;θ)m(x;\theta) are given in semi-closed form via the characteristic function of log⁡ST\log S\_{T} [heston1993closed].
European call prices under the Heston model admit the semi-analytical representation

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(S0,K,T;θ)=S0​P1−K​e−r​T​P2,C(S\_{0},K,T;\theta)=S\_{0}P\_{1}-Ke^{-rT}P\_{2}, |  | (1) |

where the risk–neutral probabilities, PjP\_{j}, are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pj=12+1π​∫0∞ℜ⁡(e−i​u​ln⁡K​ϕj​(u)i​u)​du,j∈{1,2}.P\_{j}=\tfrac{1}{2}+\tfrac{1}{\pi}\int\_{0}^{\infty}\Re\!\left(\frac{e^{-iu\ln K}\,\phi\_{j}(u)}{iu}\right)\mathrm{d}u,\qquad j\in\{1,2\}. |  | (2) |

The characteristic function ϕj​(u)\phi\_{j}(u) follows the standard form of [heston1993closed], depending on parameters θ=(κ,θv,σv,ρ,v0)\theta=(\kappa,\theta\_{v},\sigma\_{v},\rho,v\_{0}).
We evaluate ([2](https://arxiv.org/html/2511.14980v1#S2.E2 "In 2.1 Preliminaries ‣ 2 Formulation of the unlearning problem ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework")) numerically via Simpson integration with an upper bound UmaxU\_{\max} and NN sub-intervals, which ensures differentiability of C​(⋅;θ)C(\cdot;\theta) with respect to each parameter which ensures that the Jacobian Ji​(θ)=∇θm​(xi;θ)J\_{i}(\theta)=\nabla\_{\theta}m(x\_{i};\theta) exists for each quote given that xix\_{i} m​(x;θ)m(x;\theta) the parametric pricing map (e.g., Heston) with θ∈Θ⊂ℝp\theta\in\Theta\subset\mathbb{R}^{p} with D={(xi,yi)}i=1ND=\{(x\_{i},y\_{i})\}\_{i=1}^{N} denoting the dataset of option quotes (features xix\_{i} and responses yiy\_{i}).
Further, let x=(S,K,T,r)x=(S,K,T,r) denote the market features of a European call option quote,
and let θ=(κ,θv,σv,ρ,v0)\theta=(\kappa,\theta\_{v},\sigma\_{v},\rho,v\_{0}) be the Heston parameter vector.
We define the parametric pricing map

|  |  |  |
| --- | --- | --- |
|  | m​(x;θ)=S​P1​(S,K,T,r;θ)−K​e−r​T​P2​(S,K,T,r;θ),m(x;\theta)=S\,P\_{1}(S,K,T,r;\theta)-Ke^{-rT}P\_{2}(S,K,T,r;\theta), |  |

where P1P\_{1} and P2P\_{2} are the risk–neutral probabilities given by the
Fourier–Laplace integrals of ([2](https://arxiv.org/html/2511.14980v1#S2.E2 "In 2.1 Preliminaries ‣ 2 Formulation of the unlearning problem ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework")).
The calibration problem then seeks

|  |  |  |
| --- | --- | --- |
|  | θ⋆=arg⁡minθ⁡J​(θ;D),J​(θ;D)=∑i∈D(yi−m​(xi;θ))2.\theta^{\star}=\arg\min\_{\theta}J(\theta;D),\qquad J(\theta;D)=\sum\_{i\in D}\big(y\_{i}-m(x\_{i};\theta)\big)^{2}. |  |

With ri​(θ)=yi−m​(xi;θ)r\_{i}(\theta)=y\_{i}-m(x\_{i};\theta), linearizing each residual around a reference θref\theta^{\mathrm{ref}} gives ri​(θref+Δ​θ)≈ri​(θref)−Ji​(θref)​Δ​θr\_{i}(\theta^{\mathrm{ref}}+\Delta\theta)\approx r\_{i}(\theta^{\mathrm{ref}})-J\_{i}(\theta^{\mathrm{ref}})\Delta\theta, where Ji​(θ)=∇θm​(xi;θ)J\_{i}(\theta)=\nabla\_{\theta}m(x\_{i};\theta) is the sensitivity (Jacobian) of the model output with respect to parameters.
Substituting into J​(θ)J(\theta) and minimizing the quadratic approximation yields
the *Gauss–Newton normal equations*

|  |  |  |
| --- | --- | --- |
|  | H​(θref)​Δ​θ=G​(θref),H=∑iJi⊤​Ji,G=∑iJi⊤​ri.H(\theta^{\mathrm{ref}})\,\Delta\theta=G(\theta^{\mathrm{ref}}),\qquad H=\sum\_{i}J\_{i}^{\top}J\_{i},\quad G=\sum\_{i}J\_{i}^{\top}r\_{i}. |  |

Solving for Δ​θ\Delta\theta provides the parameter correction that minimizes the
local linearized loss:
θ′=θref+Δ​θ\theta^{\prime}=\theta^{\mathrm{ref}}+\Delta\theta.
Because HH and GG are additive across data points, any subset of quotes can be
removed or updated by simple algebraic subtraction of their local contributions.
This additive structure underpins the exactness of the proposed forgetting
operator.
Therefore, we build upon this simplistic yet structural insightful observation of additivity in designing the unlearning operators.

### 2.2 Sharded recompute operator

The idea of dividing a dataset into shards for efficient unlearning has appeared in the
machine-learning literature, notably in the “SISA” framework of [bourtoule2021machine], which trains isolated submodels that can be retrained independently upon deletion requests.
Our sharded design which we now present is mathematically different; rather than training independent submodels, we partition the Gauss–Newton normal equations themselves into additive
shard contributions (Hk,Gk)(H\_{k},G\_{k}), allowing exact recomputation of the global system after a shard-level deletion.

Let xix\_{i} be features (e.g., moneyness, maturity etc) and yiy\_{i} be the observed price (or implied volatility); together constituting the set option quotes (xi,yi)(x\_{i},y\_{i}) with i∈Di\in D (finite index set).
We define m​(x;θ)m(x;\theta) as the parametric pricing map (e.g., Heston) with parameters θ∈Θ⊂ℝp\theta\in\Theta\subset\mathbb{R}^{p} and Loss as ℓ​(y,y^)\ell(y,\hat{y}), typically squared error on prices.
And calibration minimizes the empirical loss of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | J​(θ;D)=∑i∈Dℓ​(yi,m​(xi;θ)).J(\theta;D)=\sum\_{i\in D}\ell(y\_{i},m(x\_{i};\theta)). |  | (3) |

At a reference θ\theta, We use Gauss–Newton to solve

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(θ)​Δ​θ=g​(θ),\quad H(\theta)\Delta\theta=g(\theta), |  | (4) |

where g​(θ)=∑iJi​(θ)⊤​ri​(θ)g(\theta)=\sum\_{i}J\_{i}(\theta)^{\top}r\_{i}(\theta), H​(θ)=∑iJi​(θ)⊤​Ji​(θ)H(\theta)=\sum\_{i}J\_{i}(\theta)^{\top}J\_{i}(\theta), ri​(θ)=yi−m​(xi;θ)r\_{i}(\theta)=y\_{i}-m(x\_{i};\theta), Ji​(θ)=∇θm​(xi;θ)J\_{i}(\theta)=\nabla\_{\theta}m(x\_{i};\theta).
Given a trained model on DD, and a subset F⊂DF\subset D to "forget", update θ\theta so the new parameter equals (or closely matches) the parameter you would obtain by retraining on D∖FD\setminus F, without sweeping the entire DD again.
Sharded recomputation first partitions the data set into KK shards D=⋃k=1KDkD=\bigcup\_{k=1}^{K}D\_{k}.
Sharding could be by time (e.g., month).We remark an important suggestion on the shard sizes.
Given the assumption that some parts of data will be unlearned, keeping shards moderately sized so that removing a subset touches few shards .
For any reference θ\theta, we define per-shard Gauss–Newton aggregates:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gk​(θ)=∑i∈DkJi​(θ)⊤​ri​(θ),Hk​(θ)=∑i∈DkJi​(θ)⊤​Ji​(θ).G\_{k}(\theta)=\sum\_{i\in D\_{k}}J\_{i}(\theta)^{\top}r\_{i}(\theta),\quad H\_{k}(\theta)=\sum\_{i\in D\_{k}}J\_{i}(\theta)^{\top}J\_{i}(\theta). |  | (5) |

Global aggregates are sums across shards:

|  |  |  |  |
| --- | --- | --- | --- |
|  | G​(θ)=∑k=1KGk​(θ),H​(θ)=∑k=1KHk​(θ).G(\theta)=\sum\_{k=1}^{K}G\_{k}(\theta),\quad H(\theta)=\sum\_{k=1}^{K}H\_{k}(\theta). |  | (6) |

The methodology with reference θref\theta^{\text{ref}}.
First compute Gk​(θref)G\_{k}(\theta^{\text{ref}}), Hk​(θref)H\_{k}(\theta^{\text{ref}}) for each shard kk, sum to GG, HH; solve H​Δ​θ=GH\Delta\theta=G and finally update θ←θref+Δ​θ\theta\leftarrow\theta^{\text{ref}}+\Delta\theta.
One can optionally relinearize once or twice (update reference and re-compute shard stats).
This, rather, describes the baseline calibration procedure when no data has been forgotten.
For F⊂DF\subset D, unlearning phase includes identifying the set of affected shards 𝒦​(F)={k:Dk∩F≠∅}\mathcal{K}(F)=\{k:D\_{k}\cap F\neq\emptyset\} first, then recomputing only those shards such that
k∈𝒦​(F)k\in\mathcal{K}(F) on Dk∖FD\_{k}\setminus F to obtain Gk′G\_{k}^{\prime}, Hk′H\_{k}^{\prime}.
We note that unaffected shards keep their statistics GkG\_{k}, HkH\_{k} while new global stats become

|  |  |  |  |
| --- | --- | --- | --- |
|  | G′=∑k∉𝒦​(F)Gk+∑k∈𝒦​(F)Gk′,G^{\prime}=\sum\_{k\notin\mathcal{K}(F)}G\_{k}+\sum\_{k\in\mathcal{K}(F)}G\_{k}^{\prime}, |  | (7) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | H′=∑k∉𝒦​(F)Hk+∑k∈𝒦​(F)Hk′,H^{\prime}=\sum\_{k\notin\mathcal{K}(F)}H\_{k}+\sum\_{k\in\mathcal{K}(F)}H\_{k}^{\prime}, |  | (8) |

with ([7](https://arxiv.org/html/2511.14980v1#S2.E7 "In 2.2 Sharded recompute operator ‣ 2 Formulation of the unlearning problem ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework")) and ([8](https://arxiv.org/html/2511.14980v1#S2.E8 "In 2.2 Sharded recompute operator ‣ 2 Formulation of the unlearning problem ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework")), we solve for H′​Δ​θ′=G′H^{\prime}\Delta\theta^{\prime}=G^{\prime} and update accordingly.
Although the discussion above is straightforward, presenting the intuition of sharding is timely.
The idea of grouping the option (panel) data into subgroups before calibration is already well known in the literature; for instance we refer to [dumas1998implied], [ulrich2023implied], [homescu2011implied] and [friedman2014some].
As suggested, bucketing option data is already a common practice and we repurpose it in our analogy to share the same sharding narrative presented in [bourtoule2021machine].
On the broader terms, there are possible alternatives in sharding which will ultimately depend on the unlearning requests or necessities.
In our study, we simply do it by time as it is simple and stable.
This approach is particularly useful if the quotes arrive over days and forgetting targets a *date range*.
Another possibility is through product structure, for instance one shard including ATM with fewer than 30 days to expiration and another for OTMs with fewer than 60 days to expiration.
Possible scenario might include forgetting particular short-dated options from the dataset or removing bad surface are around 1M tenor.
This could provide better locality than time-sharding and perhaps the one that could contribute to model validation procedures given sharding targets after specific questions raised.
Finally we could suggest a hybrid version of what we discussed so far yet we leave such possibilities for further studies.

To ensure validity, we have standard stability and regularity assumptions.
We assume that m​(x;θ)m(x;\theta) is twice continuously differentiable in θ\theta on Θ\Theta so that the model’s pricing map is smooth enough.
Further, the Jacobian J​(θ)J(\theta) should exist and local Taylor expansion, r​(θ+Δ​θ)≈r​(θ)+J​Δ​θr(\theta+\Delta\theta)\approx r(\theta)+J\Delta\theta, does not lead to instability in residuals.
Secondly we assume that per-shard sums Hk​(θref)H\_{k}(\theta^{\text{ref}}) are positive semidefinite so that local curvature remains nonnegative; i.e. shards contribute non-negative information.
And lastly we assume that global H​(θref)H(\theta^{\text{ref}}) is positive definite with minimal eigenvalue λmin>0\lambda\_{\min}>0 so that local strong convexity is established at θr​e​f\theta^{ref} and the global normal equation has a unique solution.

###### Proposition 1.

(Shard-level exactness at a fixed linearization)
Fix the reference θref\theta^{\text{ref}}. Consider the Gauss–Newton normal equations at that reference. If we recompute exactly Gk′G^{\prime}\_{k}, Hk′H^{\prime}\_{k} for all affected shards on Dk∖FD\_{k}\setminus F and keep (Gk,Hk)(G\_{k},H\_{k}) for unaffected shards, then the global system

|  |  |  |
| --- | --- | --- |
|  | (∑k∉𝒦​(F)Hk+∑k∈𝒦​(F)Hk′)​Δ​θ′=∑k∉𝒦​(F)Gk+∑k∈𝒦​(F)Gk′\left(\sum\_{k\notin\mathcal{K}(F)}H\_{k}+\sum\_{k\in\mathcal{K}(F)}H^{\prime}\_{k}\right)\Delta\theta^{\prime}=\sum\_{k\notin\mathcal{K}(F)}G\_{k}+\sum\_{k\in\mathcal{K}(F)}G^{\prime}\_{k} |  |

is identical to the Gauss–Newton system built by running over the full retained set D∖FD\setminus F at θref\theta^{\text{ref}}. Consequently, the update θ′=θref+Δ​θ′\theta^{\prime}=\theta^{\text{ref}}+\Delta\theta^{\prime} matches full retraining under the same linearization.

Proof is trivial as both sides are linear sums over i∈D∖Fi\in D\setminus F; sharding is just a partition.
The reason we put forward Proposition [1](https://arxiv.org/html/2511.14980v1#Thmtheorem1 "Proposition 1. ‣ 2.2 Sharded recompute operator ‣ 2 Formulation of the unlearning problem ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework") is straightforward.
Linearization, in our context, refers to the first-order approximation of the residual between model-generated prices and observed quotes, i.e., the loss surface around the current parameter estimate.
With this, Proposition [1](https://arxiv.org/html/2511.14980v1#Thmtheorem1 "Proposition 1. ‣ 2.2 Sharded recompute operator ‣ 2 Formulation of the unlearning problem ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework") simply formalizes that under a fixed linearization, sharding recomputation is *exactly equivalent* to full recalibration on the retained data (the data left upon removal of some data).
Formally, the unlearning operation becomes linear in the data as it is the bridge from nonlinear calibration to unlearning operator and justifies our sharded recomputation unlearning operator as an analytically consistent replacement for full retraining.
The following result adapts the classical local error bound of Gauss–Newton iterations to our sharded-unlearning framework.
Here, the bound quantifies the accuracy gained after one local relinearization on affected shards, rather than the asymptotic convergence of a full iterative scheme.

###### Proposition 2 (Accuracy after one relinearization on affected shards).

Under the same smoothness and strong-convexity assumptions as before,
and additionally assuming that the Jacobian J​(θ)J(\theta) is Lipschitz
continuous in a neighborhood of θref\theta^{\text{ref}}
Let θ′=θref+Δ​θ′\theta^{\prime}=\theta^{\text{ref}}+\Delta\theta^{\prime} be the parameter produced by the shard-level update of Proposition [1](https://arxiv.org/html/2511.14980v1#Thmtheorem1 "Proposition 1. ‣ 2.2 Sharded recompute operator ‣ 2 Formulation of the unlearning problem ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework") at a fixed reference θref\theta^{\text{ref}} on the retained dataset D∖FD\setminus F.
Let θ^\hat{\theta} denote the parameter obtained by performing one relinearization at θ′\theta^{\prime} and resolving the Gauss–Newton system on D∖FD\setminus F.
Then there exist constants C1,C2>0C\_{1},C\_{2}>0 depending on LJL\_{J}, RmaxR\_{\max}, and the conditioning of H′​(θref)H^{\prime}(\theta^{\text{ref}}) such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖θ^−θ′‖≤C1​‖r​(θref)‖​‖Δ​θ′‖+C2​‖Δ​θ′‖2.\|\hat{\theta}-\theta^{\prime}\|\;\leq\;C\_{1}\,\|r(\theta^{\text{ref}})\|\,\|\Delta\theta^{\prime}\|\;+\;C\_{2}\,\|\Delta\theta^{\prime}\|^{2}. |  | (9) |

###### Remark 1 (Quadratic accuracy under small residuals).

If, in addition, the residual norm at the reference satisfies
‖r​(θref)‖≤c​‖Δ​θ′‖\|r(\theta^{\text{ref}})\|\leq c\,\|\Delta\theta^{\prime}\| for some c>0c>0,
then inequality ([9](https://arxiv.org/html/2511.14980v1#S2.E9 "In Proposition 2 (Accuracy after one relinearization on affected shards). ‣ 2.2 Sharded recompute operator ‣ 2 Formulation of the unlearning problem ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework")) reduces to

|  |  |  |
| --- | --- | --- |
|  | ‖θ^−θ′‖≤C​‖Δ​θ′‖2,C:=C1​c+C2.\|\hat{\theta}-\theta^{\prime}\|\;\leq\;C\,\|\Delta\theta^{\prime}\|^{2},\quad C:=C\_{1}c+C\_{2}. |  |

Hence, a single relinearization on the affected shards yields a second-order accurate refinement of the fixed-linearization update.

###### Proof of Proposition [2](https://arxiv.org/html/2511.14980v1#Thmtheorem2 "Proposition 2 (Accuracy after one relinearization on affected shards). ‣ 2.2 Sharded recompute operator ‣ 2 Formulation of the unlearning problem ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework").

Write aggregated quantities on D∖FD\setminus F as

|  |  |  |
| --- | --- | --- |
|  | H​(θ)=J​(θ)⊤​J​(θ),G​(θ)=J​(θ)⊤​r​(θ).H(\theta)=J(\theta)^{\top}J(\theta),\qquad G(\theta)=J(\theta)^{\top}r(\theta). |  |

By the Lipschitz property and twice differentiability of mm, for Δ=Δ​θ′\Delta=\Delta\theta^{\prime} we have

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | J​(θ′)\displaystyle J(\theta^{\prime}) | =J​(θref)+EJ,\displaystyle=J(\theta^{\text{ref}})+E\_{J},\qquad |  | ‖EJ‖≤LJ​‖Δ‖,\displaystyle\|E\_{J}\|\leq L\_{J}\|\Delta\|, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | r​(θ′)\displaystyle r(\theta^{\prime}) | =r​(θref)+J​(θref)​Δ+Rr,\displaystyle=r(\theta^{\text{ref}})+J(\theta^{\text{ref}})\Delta+R\_{r},\qquad |  | ‖Rr‖≤Cr​‖Δ‖2,\displaystyle\|R\_{r}\|\leq C\_{r}\|\Delta\|^{2}, |  |

for some constant Cr=O​(LJ)C\_{r}=O(L\_{J}).
Expanding G​(θ′)G(\theta^{\prime}) and H​(θ′)H(\theta^{\prime}) gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | G​(θ′)\displaystyle G(\theta^{\prime}) | =J​(θ′)⊤​r​(θ′)=J⊤​r+J⊤​J​Δ+EJ⊤​r+O​(‖Δ‖2),\displaystyle=J(\theta^{\prime})^{\top}r(\theta^{\prime})=J^{\top}r+J^{\top}J\Delta+E\_{J}^{\top}r+O(\|\Delta\|^{2}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(θ′)\displaystyle H(\theta^{\prime}) | =J​(θ′)⊤​J​(θ′)=H​(θref)+Δ​H,‖Δ​H‖≤CH​‖Δ‖,\displaystyle=J(\theta^{\prime})^{\top}J(\theta^{\prime})=H(\theta^{\text{ref}})+\Delta H,\qquad\|\Delta H\|\leq C\_{H}\|\Delta\|, |  |

with CH=O​(‖J​(θref)‖​LJ+LJ2)C\_{H}=O(\|J(\theta^{\text{ref}})\|L\_{J}+L\_{J}^{2}).
Let Δ+\Delta^{+} solve the relinearized system H​(θ′)​Δ+=G​(θ′)H(\theta^{\prime})\Delta^{+}=G(\theta^{\prime}).
Subtracting the fixed-linearization equation H​(θref)​Δ=G​(θref)H(\theta^{\text{ref}})\Delta=G(\theta^{\text{ref}}) yields

|  |  |  |
| --- | --- | --- |
|  | H​(θ′)​(Δ+−Δ)=EJ⊤​r+O​(‖Δ‖2)+Δ​H​Δ.H(\theta^{\prime})(\Delta^{+}-\Delta)=E\_{J}^{\top}r+O(\|\Delta\|^{2})+\Delta H\,\Delta. |  |

Taking norms and using ‖H​(θ′)−1‖≤2/λmin\|H(\theta^{\prime})^{-1}\|\leq 2/\lambda\_{\min} for ‖Δ‖\|\Delta\| small gives

|  |  |  |
| --- | --- | --- |
|  | ‖Δ+−Δ‖≤2​LJλmin​‖r​(θref)‖​‖Δ‖+C2′​‖Δ‖2,\|\Delta^{+}-\Delta\|\;\leq\;\frac{2L\_{J}}{\lambda\_{\min}}\,\|r(\theta^{\text{ref}})\|\,\|\Delta\|\;+\;C\_{2}^{\prime}\|\Delta\|^{2}, |  |

for a constant C2′C\_{2}^{\prime} depending on LJL\_{J} and λmin−1\lambda\_{\min}^{-1}. Since
θ^−θ′=(θref+Δ+)−(θref+Δ)=Δ+−Δ\hat{\theta}-\theta^{\prime}=(\theta^{\text{ref}}+\Delta^{+})-(\theta^{\text{ref}}+\Delta)=\Delta^{+}-\Delta,
this proves ([9](https://arxiv.org/html/2511.14980v1#S2.E9 "In Proposition 2 (Accuracy after one relinearization on affected shards). ‣ 2.2 Sharded recompute operator ‣ 2 Formulation of the unlearning problem ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework")) with C1=2​LJ/λminC\_{1}=2L\_{J}/\lambda\_{\min} and C2=C2′C\_{2}=C\_{2}^{\prime}.
The corollary follows by substituting ‖r​(θref)‖≤c​‖Δ‖\|r(\theta^{\text{ref}})\|\leq c\|\Delta\| and absorbing constants. ∎

The quadratic accuracy bound derived above is structurally related to the classical local error analysis of Gauss–Newton and Newton–Kantorovich iterations.
Here, however, the theorem is not invoked to study asymptotic convergence of an iterative solver, but to establish the *fidelity of machine unlearning* within a sharded calibration framework.
In our setting, the relinearization step is applied only to the affected shards after a data-deletion event, and the resulting bound quantifies how closely this partial update reproduces the fully retrained Gauss–Newton solution on the retained data set.
The adaptation of a classical local error argument to the context of selective unlearning therefore provides new insight into the stability and precision of unlearning operations in financial model
calibration.
The following adapts a standard perturbation bound for linear systems to our Gauss–Newton unlearning update.
It provides an upper limit on the parameter deviation induced by downdating the curvature and gradient terms.

###### Proposition 3 (Stability of the unlearning update).

Let θ=θref+Δ​θ\theta=\theta^{\mathrm{ref}}+\Delta\theta solve the fixed linearization system
H​Δ​θ=GH\Delta\theta=G on DD, and let θ′=θref+Δ​θ′\theta^{\prime}=\theta^{\mathrm{ref}}+\Delta\theta^{\prime} solve
H′​Δ​θ′=G′H^{\prime}\Delta\theta^{\prime}=G^{\prime} on D∖FD\setminus F, where

|  |  |  |
| --- | --- | --- |
|  | H′=H+Δ​H,G′=G+Δ​G.H^{\prime}=H+\Delta H,\qquad G^{\prime}=G+\Delta G. |  |

Assume H′H^{\prime} is invertible. Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖θ′−θ‖=‖Δ​θ′−Δ​θ‖≤‖H′⁣−1‖​(‖Δ​G‖+‖Δ​H‖​‖Δ​θ‖).\|\theta^{\prime}-\theta\|\;=\;\|\Delta\theta^{\prime}-\Delta\theta\|\;\leq\;\|H^{\prime-1}\|\,\big(\,\|\Delta G\|+\|\Delta H\|\,\|\Delta\theta\|\,\big). |  | (10) |

Moreover, if ‖H−1‖​‖Δ​H‖<1\|H^{-1}\|\,\|\Delta H\|<1, then

|  |  |  |
| --- | --- | --- |
|  | ‖H′⁣−1‖≤‖H−1‖1−‖H−1‖​‖Δ​H‖.\|H^{\prime-1}\|\;\leq\;\frac{\|H^{-1}\|}{1-\|H^{-1}\|\,\|\Delta H\|}. |  |

###### Proof.

From H​Δ​θ=GH\Delta\theta=G and (H+Δ​H)​Δ​θ′=G+Δ​G(H+\Delta H)\Delta\theta^{\prime}=G+\Delta G,

|  |  |  |
| --- | --- | --- |
|  | H′​(Δ​θ′−Δ​θ)=Δ​G−Δ​H​Δ​θ.H^{\prime}(\Delta\theta^{\prime}-\Delta\theta)\;=\;\Delta G-\Delta H\,\Delta\theta. |  |

Multiply by H′⁣−1H^{\prime-1} and take norms; the Neumann bound follows from
H′⁣−1=(I+H−1​Δ​H)−1​H−1H^{\prime-1}=(I+H^{-1}\Delta H)^{-1}H^{-1} whenever ‖H−1​Δ​H‖<1\|H^{-1}\Delta H\|<1.
∎

###### Remark 2 (Robust loss control).

Suppose the per-quote loss is Huber with threshold c>0c>0 and residuals are
locally bounded. Then each quote’s influence function is bounded by cc,
so there exist constants CJ,CJ​JC\_{J},C\_{JJ} (depending on Jacobian norms) such that,
for forgetting FF,

|  |  |  |
| --- | --- | --- |
|  | ‖Δ​G‖≤CJ​c​|F|,‖Δ​H‖≤CJ​J​|F|.\|\Delta G\|\;\leq\;C\_{J}\,c\,|F|,\qquad\|\Delta H\|\;\leq\;C\_{JJ}\,|F|. |  |

Consequently, if H′H^{\prime} is well conditioned,

|  |  |  |
| --- | --- | --- |
|  | ‖θ′−θ‖≲κ​(H′)​(c​|F|+|F|​‖Δ​θ‖),\|\theta^{\prime}-\theta\|\;\lesssim\;\kappa(H^{\prime})\big(c\,|F|+|F|\,\|\Delta\theta\|\big), |  |

i.e., the change scales linearly with the forgotten mass and the conditioning.

###### Remark 3 (Conditioning links: eigenvalues and Neumann bound).

Assume throughout the spectral (2-)norm and that H,H′H,H^{\prime} are symmetric positive definite.
Then ‖H′⁣−1‖2=1/λmin​(H′)\|H^{\prime-1}\|\_{2}=1/\lambda\_{\min}(H^{\prime}), and the stability estimate

|  |  |  |
| --- | --- | --- |
|  | ‖Δ​θ′−Δ​θ‖≤‖Δ​G‖2+‖Δ​H‖2​‖Δ​θ‖2λmin​(H′)\|\Delta\theta^{\prime}-\Delta\theta\|\;\leq\;\frac{\|\Delta G\|\_{2}+\|\Delta H\|\_{2}\,\|\Delta\theta\|\_{2}}{\lambda\_{\min}(H^{\prime})} |  |

shows that larger λmin​(H′)\lambda\_{\min}(H^{\prime}) (better conditioning) improves robustness.
Moreover, if ‖H−1​Δ​H‖2<1\|H^{-1}\Delta H\|\_{2}<1, the Neumann expansion yields

|  |  |  |
| --- | --- | --- |
|  | ‖H′⁣−1‖2≤‖H−1‖2 1−‖H−1​Δ​H‖2=1λmin​(H)​(1−‖H−1​Δ​H‖2),\|H^{\prime-1}\|\_{2}\;\leq\;\frac{\|H^{-1}\|\_{2}}{\,1-\|H^{-1}\Delta H\|\_{2}\,}\;=\;\frac{1}{\,\lambda\_{\min}(H)\,\big(1-\|H^{-1}\Delta H\|\_{2}\big)}\,, |  |

and consequently

|  |  |  |
| --- | --- | --- |
|  | ‖Δ​θ′−Δ​θ‖≤‖Δ​G‖2+‖Δ​H‖2​‖Δ​θ‖2λmin​(H)​(1−‖H−1​Δ​H‖2).\|\Delta\theta^{\prime}-\Delta\theta\|\;\leq\;\frac{\|\Delta G\|\_{2}+\|\Delta H\|\_{2}\,\|\Delta\theta\|\_{2}}{\lambda\_{\min}(H)\,\big(1-\|H^{-1}\Delta H\|\_{2}\big)}. |  |

Finally, by Weyl’s inequality,
λmin​(H′)≥λmin​(H)−‖Δ​H‖2\lambda\_{\min}(H^{\prime})\geq\lambda\_{\min}(H)-\|\Delta H\|\_{2},
so H′H^{\prime} remains positive definite whenever ‖Δ​H‖2<λmin​(H)\|\Delta H\|\_{2}<\lambda\_{\min}(H).

The above results collectively ensure that the curvature downdate remains numerically stable and the Gauss–Newton step is well defined under moderate forgetting.
Having established the local stability and conditioning properties, we next turn to the fast refactorization approach.

### 2.3 Fast refactor operator

Machine unlearning is not defined by the speed of recomputation, but rather by the semantics of the data removal.
We could formalize it such that an algorithm carries an unlearning spirit after deleting subset F⊂DF\subset D and the resulting model parameters are *indistinguishable* from those obtained by retraining on D∖FD\setminus F.
Therefore, in the sense of [bourtoule2021machine], the sharded recomputation remains a legitimate unlearning operator, laying the conceptual definition of unlearning in our framework.
Given our points of concern embark on computational capability rather than on issues related to the well articulated purposes of machine unlearning (eg. privacy), we remark the necessity of offering an efficient implementation of that same operator for reasons we discuss shortly.

We now introduce a faster data-free forgetting operator that yields the same Gauss–Newton (GN) update as retraining on the retained set, without accessing raw quotes once a cache is built.
Throughout, we fix a reference parameter θref∈Θ\theta^{\mathrm{ref}}\in\Theta and work with the GN normal equations at this reference.
Let F⊂DF\subset D denote a subset of quotes to be forgotten and (H′,G′)(H^{\prime},G^{\prime}) denote the post-forgetting aggregates obtained by subtracting the contributions of F⊂DF\subset D.
Given the Gauss–Newton aggregates are linear in {ui,ψi}\{u\_{i},\psi\_{i}\}, the effect of removing
FF can be represented exactly by subtraction:

|  |  |  |  |
| --- | --- | --- | --- |
|  | H′=H−∑i∈Fψi,G′=G−∑i∈Fui.H^{\prime}\;=\;H-\sum\_{i\in F}\psi\_{i},\qquad G^{\prime}\;=\;G-\sum\_{i\in F}u\_{i}. |  | (11) |

The updated parameter is then obtained by solving once

|  |  |  |  |
| --- | --- | --- | --- |
|  | (H′+λ​I)​Δ​θ′=G′,θ′=θref+Δ​θ′.(H^{\prime}+\lambda I)\,\Delta\theta^{\prime}=G^{\prime},\qquad\theta^{\prime}=\theta^{\mathrm{ref}}+\Delta\theta^{\prime}. |  | (12) |

Equations ([12](https://arxiv.org/html/2511.14980v1#S2.E12 "In 2.3 Fast refactor operator ‣ 2 Formulation of the unlearning problem ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework")) require only the cached statistics (ui,ψi)(u\_{i},\psi\_{i}), not the raw market data (xi,yi)(x\_{i},y\_{i}), and thus implement a *data-free forgetting operator*.
At the fixed linearization θref\theta^{\mathrm{ref}}, this refactoring exactly removes the influence of the
forgotten subset from the calibration system.
The procedure achieves the same solution as a full retraining on D∖FD\setminus F, up to machine precision, while
avoiding all repricing and re-differentiation.
Fast refactorization operates under the same local regularity conditions introduced in Section [2.2](https://arxiv.org/html/2511.14980v1#S2.SS2 "2.2 Sharded recompute operator ‣ 2 Formulation of the unlearning problem ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework"), namely smoothness, local strong convexity (possibly enforced via a small ridge term λ​I\lambda I), Lipschitz continuity of the Jacobian, and bounded residuals.
These ensure that the refactorized system (H′+λ​I)​Δ​θ′=G′(H^{\prime}+\lambda I)\Delta\theta^{\prime}=G^{\prime} remains well-posed and that all prior analytical results remain valid.

Each option quote ii contributes via its residual
ri​(θref)=yi−m​(xi;θref)r\_{i}(\theta^{\mathrm{ref}})=y\_{i}-m(x\_{i};\theta^{\mathrm{ref}}) and local sensitivity Ji​(θref)=∇θm​(xi;θref)J\_{i}(\theta^{\mathrm{ref}})=\nabla\_{\theta}m(x\_{i};\theta^{\mathrm{ref}}).
Define ui:=Ji⊤​riu\_{i}:=J\_{i}^{\top}r\_{i} and ψi:=Ji⊤​Ji\psi\_{i}:=J\_{i}^{\top}J\_{i}.
Then G=∑iuiG=\sum\_{i}u\_{i} and H=∑iψiH=\sum\_{i}\psi\_{i} are the Gauss–Newton aggregates at θref\theta^{\mathrm{ref}}, and the update solves H​Δ​θ=GH\,\Delta\theta=G.
Thus the collection {(ui,ψi)}i\{(u\_{i},\psi\_{i})\}\_{i} is *algebraically sufficient for the linearized calibration at θref\theta^{\mathrm{ref}}*: once stored, the influence of any subset FF can be removed exactly by subtraction, H′=H−∑i∈FψiH^{\prime}=H-\sum\_{i\in F}\psi\_{i} and G′=G−∑i∈FuiG^{\prime}=G-\sum\_{i\in F}u\_{i},
without revisiting raw data.
If a robust loss is used, the same identities hold with per-quote weights (ui=wi​Ji⊤​riu\_{i}=w\_{i}J\_{i}^{\top}r\_{i}, ψi=wi​Ji⊤​Ji\psi\_{i}=w\_{i}J\_{i}^{\top}J\_{i}).
These statistics are tied to the chosen reference; upon relinearization (θref↦θnew\theta^{\mathrm{ref}}\mapsto\theta^{\mathrm{new}}), the pairs (ui,ψi)(u\_{i},\psi\_{i}) should be recomputed at the new reference.

Although we build fast refactor operator on the foundations of the sharded recomputation, the latter does not actually need shards.
During the initial training we build caches, (H,G)(H,G), and per-shard aggregates, (Hk,Gk)(H\_{k},G\_{k}).
In the sharded recomputation, with some quotes removed, we reopen only the shards that contain them, then recompute (Hk,Gk)(H\_{k},G\_{k}) for those shards and sum up with others.
In fast refactor we go one step further and directly subtract each forgotten quote’s contribution from the cached global (H,K)(H,K) so that there no longer exists the need to reopen or recompute the shards, making it completely data-free and instantaneous.
Inclusion of shards, then, in fast refactor might seem contradictory.
However, we remark that the shards play important roles in categorizing the forgetting set (although removal is not driven by shards) and more importantly it provides security in the case some of quotes lacking cached Jacobians, JiJ\_{i}.

Technically speaking, in the fast refactor variant, unlearning operates at quote granularity as once per-quote GN statistics (JiT​Ji,JiT​ri)(J\_{i}^{T}J\_{i},J\_{i}^{T}r\_{i}) are cashed at the reference point, removing any subset F⊂DF\subset D amounts to simplistic algebraic operations of the global normal equations, unrelated to how the data were originally sharded.
In our implementation, the fast refactorization step forms H′=H−∑i∈FJi⊤​JiH^{\prime}=H-\sum\_{i\in F}J\_{i}^{\top}J\_{i} and G′=G−∑i∈FJi⊤​riG^{\prime}=G-\sum\_{i\in F}J\_{i}^{\top}r\_{i} explicitly, followed by a fresh Cholesky factorization of H′H^{\prime}.
This retains exactness under the fixed linearization while avoiding any recomputation over the retained dataset.
Although a true rank-1 Cholesky downdate would further reduce cost to O​(p2​|F|)O(p^{2}|F|), we found the explicit rebuild to be numerically safer and sufficiently fast for moderate pp.

While the concept of subtracting per-sample statistics is trivial for linear models,
it becomes nontrivial for nonlinear calibration because the residuals and Jacobians
depend on the current parameter estimate.
Naively removing quotes invalidates the current linearization, so retraining from scratch remains the default.
Yet, in practice, calibration pipelines already store large intermediate structures’
per-quote sensitivities, residuals, and curvature estimates for diagnostic or
parallel-computation purposes.
This suggests the possibility of an *operator-level unlearning* mechanism: removing data by algebraic downdating of the cached normal equations, without reprocessing the raw option surface.
In our framework, this takes the form of Gauss–Newton updates on refactored (H′,G′)(H^{\prime},G^{\prime}), achieving exact unlearning at a fixed linearization.

The subtraction step removes the statistical influence of each forgotten quote because,
under Gauss–Newton linearization, the normal equations decompose additively across data points.
Each quote ii contributes (ψi,ui)=(Ji⊤​Ji,Ji⊤​ri)(\psi\_{i},u\_{i})=(J\_{i}^{\top}J\_{i},\,J\_{i}^{\top}r\_{i}) to the global
system (H,G)(H,G). Solving (H+λ​I)​Δ​θ=G(H+\lambda I)\Delta\theta=G thus depends on the data only
through these linear aggregates. Forgetting a subset FF corresponds to replacing

|  |  |  |  |
| --- | --- | --- | --- |
|  | (H′,G′)=(H−∑i∈Fψi,G−∑i∈Fui),(H^{\prime},G^{\prime})=\big(H-\sum\_{i\in F}\psi\_{i},\;G-\sum\_{i\in F}u\_{i}\big), |  | (13) |

which is identical to the system built on D∖FD\setminus F.
Consequently, the updated parameter θ′=θref+Δ​θ′\theta^{\prime}=\theta^{\mathrm{ref}}+\Delta\theta^{\prime}
matches the retraining result under the same linearization, with no residual dependence on FF.
This equality H′=H⋆H^{\prime}=H^{\star}, G′=G⋆G^{\prime}=G^{\star} is formalized in such as:

###### Proposition 4 (Exactness under fixed linearization).

Let H⋆,G⋆H^{\star},G^{\star} denote the Gauss–Newton aggregates constructed directly on
the retained set D∖FD\setminus F at θref\theta^{\mathrm{ref}}:

|  |  |  |
| --- | --- | --- |
|  | H⋆=∑i∈D∖FJi​(θref)⊤​Ji​(θref),G⋆=∑i∈D∖FJi​(θref)⊤​ri​(θref).H^{\star}=\sum\_{i\in D\setminus F}J\_{i}(\theta^{\mathrm{ref}})^{\top}J\_{i}(\theta^{\mathrm{ref}}),\qquad G^{\star}=\sum\_{i\in D\setminus F}J\_{i}(\theta^{\mathrm{ref}})^{\top}r\_{i}(\theta^{\mathrm{ref}}). |  |

Then H⋆=H′H^{\star}=H^{\prime} and G⋆=G′G^{\star}=G^{\prime}, where
(H′,G′)=(H−∑i∈Fψi,G−∑i∈Fui)(H^{\prime},G^{\prime})=(H-\sum\_{i\in F}\psi\_{i},\,G-\sum\_{i\in F}u\_{i}) are the refactored
aggregates at θref\theta^{\mathrm{ref}}.
Consequently, for the same λ≥0\lambda\geq 0, the update θ′\theta^{\prime} produced by
(H′+λ​I)​Δ​θ′=G′(H^{\prime}+\lambda I)\Delta\theta^{\prime}=G^{\prime} coincides with the parameter obtained by
retraining the Gauss–Newton system on D∖FD\setminus F at θref\theta^{\mathrm{ref}}.

###### Proof.

By the additive decompositions at θref\theta^{\mathrm{ref}},
H=∑i∈Dψi=∑i∈DJi⊤​JiH=\sum\_{i\in D}\psi\_{i}=\sum\_{i\in D}J\_{i}^{\top}J\_{i} and
G=∑i∈Dui=∑i∈DJi⊤​riG=\sum\_{i\in D}u\_{i}=\sum\_{i\in D}J\_{i}^{\top}r\_{i}.
Subtracting forgotten contributions gives
H′=H−∑i∈Fψi=∑i∈D∖FJi⊤​Ji=H⋆H^{\prime}=H-\sum\_{i\in F}\psi\_{i}=\sum\_{i\in D\setminus F}J\_{i}^{\top}J\_{i}=H^{\star}
and similarly G′=∑i∈D∖FJi⊤​ri=G⋆G^{\prime}=\sum\_{i\in D\setminus F}J\_{i}^{\top}r\_{i}=G^{\star}.
Thus the regularized systems (H′+λ​I)​Δ​θ′=G′(H^{\prime}+\lambda I)\Delta\theta^{\prime}=G^{\prime} and
(H⋆+λ​I)​Δ​θ⋆=G⋆(H^{\star}+\lambda I)\Delta\theta^{\star}=G^{\star} are identical, yielding
Δ​θ′=Δ​θ⋆\Delta\theta^{\prime}=\Delta\theta^{\star} and hence the same θ′\theta^{\prime}.
∎

###### Remark 4.

The operator we suggest in this part acts solely on the cached per-quote statistics (ui,ψi)(u\_{i},\psi\_{i}) and the precomputed global aggregates (H,G)(H,G) at θref\theta^{\mathrm{ref}}.
It therefore removes the influence of the forgotten set FF exactly under the Gauss–Newton linearization without accessing any raw market quotes or re-evaluating model prices.

Let Δ​H:=H′−H\Delta H:=H^{\prime}-H and Δ​G:=G′−G\Delta G:=G^{\prime}-G. Let Δ​θ\Delta\theta and Δ​θ′\Delta\theta^{\prime} be the GN steps at θref\theta^{\mathrm{ref}} on DD and D∖FD\setminus F, respectively, both with the same λ\lambda.
We use the vector 2−2-norm and the induced operator norm for matrices.

###### Proposition 5 (Linearized stability).

With the same λ\lambda (so H′+λ​IH^{\prime}+\lambda I is invertible),

|  |  |  |
| --- | --- | --- |
|  | ‖Δ​θ′−Δ​θ‖≤‖(H′+λ​I)−1‖​(‖Δ​G‖+‖Δ​H‖​‖Δ​θ‖).\|\Delta\theta^{\prime}-\Delta\theta\|\;\leq\;\|(H^{\prime}+\lambda I)^{-1}\|\;\Big(\|\Delta G\|+\|\Delta H\|\,\|\Delta\theta\|\Big). |  |

In particular, if |F|/|D||F|/|D| is small and H′+λ​IH^{\prime}+\lambda I is well conditioned, then ‖Δ​θ′−Δ​θ‖\|\Delta\theta^{\prime}-\Delta\theta\| is small.

###### Sketch.

Write (H+λ​I)​Δ​θ=G(H+\lambda I)\Delta\theta=G and (H′+λ​I)​Δ​θ′=G′(H^{\prime}+\lambda I)\Delta\theta^{\prime}=G^{\prime}. Subtract to obtain

|  |  |  |
| --- | --- | --- |
|  | (H′+λ​I)​(Δ​θ′−Δ​θ)=Δ​G−Δ​H​Δ​θ,(H^{\prime}+\lambda I)(\Delta\theta^{\prime}-\Delta\theta)\;=\;\Delta G-\Delta H\,\Delta\theta, |  |

then multiply by (H′+λ​I)−1(H^{\prime}+\lambda I)^{-1} and take norms.
∎

###### Proposition 6 (Accuracy after one relinearization).

Let θ⋆\theta^{\star} denote the (local) least-squares solution on D∖ℱD\setminus\mathcal{F}.
Assume: (i) J​(θ)J(\theta) is Lipschitz in a neighborhood of θ⋆\theta^{\star} with constant LJL\_{J},
(ii) J​(θ⋆)J(\theta^{\star}) has full column rank, and
(iii) the residual at the solution is small, ‖r​(θ⋆)‖≤ε\|r(\theta^{\star})\|\leq\varepsilon.
Let θ^\widehat{\theta} be the GN/LM (Levenberg–Marquardt) solution obtained on D∖ℱD\setminus\mathcal{F} after
one relinearization at θref+Δ​θ′\theta^{\mathrm{ref}}+\Delta\theta^{\prime} (same λ\lambda).
Then there exist constants C1,C2>0C\_{1},C\_{2}>0 (depending on LJL\_{J}, local bounds, and ‖(H′+λ​I)−1‖\|(H^{\prime}+\lambda I)^{-1}\|) such that

|  |  |  |
| --- | --- | --- |
|  | ‖θ^−θ⋆‖≤C1​‖Δ​θ′‖2+C2​ε​‖Δ​θ′‖.\|\widehat{\theta}-\theta^{\star}\|\;\leq\;C\_{1}\,\|\Delta\theta^{\prime}\|^{2}\;+\;C\_{2}\,\varepsilon\,\|\Delta\theta^{\prime}\|. |  |

In particular, in the small-residual regime (ε≈0)(\varepsilon\approx 0),
‖θ^−θ⋆‖=𝒪​(‖Δ​θ′‖2)\|\widehat{\theta}-\theta^{\star}\|=\mathcal{O}(\|\Delta\theta^{\prime}\|^{2}).

###### Sketch.

Standard Gauss–Newton local analysis (Newton–Kantorovich style):
the model error from relinearization is 𝒪​(‖Δ​θ′‖2)\mathcal{O}(\|\Delta\theta^{\prime}\|^{2}) by Lipschitz JJ.
Mapping this through the normal equations introduces ‖(H′+λ​I)−1‖\|(H^{\prime}+\lambda I)^{-1}\|.
The residual term yields the mixed ε​‖Δ​θ′‖\varepsilon\,\|\Delta\theta^{\prime}\| contribution.
∎

Shard-level recompute is exact at a fixed linearization by linearity of sums yet it still requires opening the affected shards.
The refactor operator strengthens this to a *data-free* update by using cached per-quote statistics.
In linearity, forgetting is exact by subtraction Our result lifts this idea to *nonlinear* parametric models via Gauss–Newton linearization, providing (to our knowledge) the first data-free exact forgetting operator for nonlinear least squares in financial calibration.
Once (ui,ψi)(u\_{i},\psi\_{i}) are retained and raw quotes purged, subsequent unlearning requests are executed algebraically.
If (ui,ψi)(u\_{i},\psi\_{i}) are deemed sensitive, they can be encrypted or perturbed; bounds in Proposition [5](https://arxiv.org/html/2511.14980v1#Thmtheorem5 "Proposition 5 (Linearized stability). ‣ 2.3 Fast refactor operator ‣ 2 Formulation of the unlearning problem ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework") quantify the resulting parameter drift.
We remark that the cache does not contain raw market quotes or strike–maturity grids.
Instead it stores derived Jacobian vectors ui=Jiu\_{i}=J\_{i} and ψi=Ji​ri\psi\_{i}=J\_{i}r\_{i}, together with the global normal equations H=∑iJi⊤​JiH=\sum\_{i}J\_{i}^{\top}J\_{i}, G=∑iJi​riG=\sum\_{i}J\_{i}r\_{i}
evaluated at the calibrated parameter θ⋆\theta^{\star}.
These quantities are sufficient for a local Gauss–Newton update but
contain no reconstructive information about individual data points.

###### Remark 5.

Machine unlearning is effected by removing the contributions of
forgotten quotes from the cached statistics:

|  |  |  |
| --- | --- | --- |
|  | H′=H−∑i∈ℱJi⊤​Ji,G′=G−∑i∈ℱJi​ri.H^{\prime}=H-\sum\_{i\in\mathcal{F}}J\_{i}^{\top}J\_{i},\qquad G^{\prime}=G-\sum\_{i\in\mathcal{F}}J\_{i}r\_{i}. |  |

The updated parameters
θfast=(H′+λ​I)−1​G′\theta\_{\text{fast}}=(H^{\prime}+\lambda I)^{-1}G^{\prime}
coincide with those obtained by full retraining on the retained set
(up to numerical precision).
Hence the method satisfies the formal definition of *machine unlearning*
as the ability to expunge a subset’s influence from the trained model
without re-accessing the original data, [guo2019certified, bourtoule2021machine].

We have several remarks that we believe is timely.
While the proposed unlearning operators reproduce the Gauss–Newton update on the retained dataset, occasional increases in performance metrics (RMSE, in our case) may still be observed when unlearning is applied to very small subsets of option quotes.
Two conceptually distinct mechanisms may explain this behavior.
A single Gauss–Newton step is locally exact only in a neighborhood of a previously converged solution.
When the forget set is small, the displacement of the optimum is also small, and one correction typically recovers the new minimizer to machine precision.
However, when the retained dataset becomes extremely small, the linearization may no longer be valid, and the residuals may appear unstable.
Another one is, independently of the Gauss–Newton linearization error, numerical instability
could arise if the curvature matrix H′H^{\prime} becomes ill-conditioned after forgetting111This could especially amplify if you remove a few influential quotes (e.g. some maturities or deep-OTMs that strongly shape volatility) which leaves the new curvature matrix with extremely small eigenvalues (large condition number) and perhaps with directions in parameter space that are almost unconstrained by the retained data..
This occurs when the retained quotes provide insufficient informational content, leading to exceedingly small eigenvalues and nearly unconstrained parameter directions.
In such cases, even correct cached gradients could produce large parameter excursions and elevated RMSE.
Such optimization refinements fall outside the scope of our unlearning study as it is sampling related rather than the methodology.
In summary, the occasional RMSE deviations observed for extremely small retained
datasets arise from the standard numerical behavior of Gauss–Newton and Levenberg–Marquardt schemes, rather than from the unlearning operators themselves, [ait1998nonparametric].

Before closing the section, we include another proposition on the computational complexity of the calibration and both unlearning operators.
We defer this result to the end of the section so as not to interrupt the flow of the theoretical development in the previous subsections as the developed approaches are not related to the Heston model that we use for exemplary purposes.
Given our framework is fully model-agnostic and applies to any differentiable option pricing map, the complexity statement becomes most transparent when expressed for the Heston model, where each price evaluation is performed via a Fourier–Simpson integral with NuN\_{u} frequency nodes.
The following proposition therefore specializes the analysis to this setting, which is also the one used in our numerical experiments.

###### Proposition 7 (Computational complexity of calibration and unlearning operators).

Let NN denote the number of option quotes, NuN\_{u} the number of Fourier–Simpson integration nodes used in the Heston pricer, and pp the dimension of the parameter vector (e.g. p=5p=5 for the Heston model). Assume pp is fixed and small. Then, under a Gauss–Newton calibration scheme at a fixed reference θref\theta^{\mathrm{ref}}, the following complexity bounds hold:

1. [(i)]
2. 1.

   Full recalibration. A single Gauss–Newton iteration on a dataset of size NN has time complexity

   |  |  |  |
   | --- | --- | --- |
   |  | Tretrain=𝒪​(N​Nu)+𝒪​(p3),T\_{\mathrm{retrain}}=\mathcal{O}(N\,N\_{u})+\mathcal{O}(p^{3}), |  |

   where the dominant cost is the evaluation of NN Heston prices via Fourier–Simpson quadrature. The 𝒪​(p3)\mathcal{O}(p^{3}) term arises from assembling and solving the p×pp\times p normal equations.
3. 2.

   Sharded recomputation. Let D=⋃k=1KDkD=\bigcup\_{k=1}^{K}D\_{k} be a partition of the data into KK shards and let K​(F)⊆{1,…,K}K(F)\subseteq\{1,\dots,K\} denote the set of shards affected by a forget set F⊂DF\subset D. Denote by Neff​(F)N\_{\mathrm{eff}}(F) the number of quotes in ⋃k∈K​(F)Dk\bigcup\_{k\in K(F)}D\_{k}. Then a sharded recomputation step has time complexity

   |  |  |  |
   | --- | --- | --- |
   |  | Trecomp​(F)=𝒪​(Neff​(F)​Nu)+𝒪​(p3),T\_{\mathrm{recomp}}(F)=\mathcal{O}\big(N\_{\mathrm{eff}}(F)\,N\_{u}\big)+\mathcal{O}(p^{3}), |  |

   i.e. it is equivalent to a full Gauss–Newton step restricted to the affected shards. In the worst case Neff​(F)≈NN\_{\mathrm{eff}}(F)\approx N, and Trecomp​(F)T\_{\mathrm{recomp}}(F) degenerates to TretrainT\_{\mathrm{retrain}}.
4. 3.

   Fast refactorization. Suppose that, at θref\theta^{\mathrm{ref}}, per-quote Gauss–Newton statistics

   |  |  |  |
   | --- | --- | --- |
   |  | ui=Ji​(θref)⊤​ri​(θref),ψi=Ji​(θref)⊤​Ji​(θref)u\_{i}=J\_{i}(\theta^{\mathrm{ref}})^{\top}r\_{i}(\theta^{\mathrm{ref}}),\qquad\psi\_{i}=J\_{i}(\theta^{\mathrm{ref}})^{\top}J\_{i}(\theta^{\mathrm{ref}}) |  |

   and the global aggregates H=∑iψiH=\sum\_{i}\psi\_{i}, G=∑iuiG=\sum\_{i}u\_{i} have been cached. Then a fast refactorization unlearning request for a forget set FF can be carried out in

   |  |  |  |
   | --- | --- | --- |
   |  | Tfast​(F)=𝒪​(|F|​p2)+𝒪​(p3)T\_{\mathrm{fast}}(F)=\mathcal{O}(|F|\,p^{2})+\mathcal{O}(p^{3}) |  |

   time, corresponding to subtracting {ψi,ui}i∈F\{\psi\_{i},u\_{i}\}\_{i\in F} from (H,G)(H,G) and solving the refactored p×pp\times p linear system. For fixed pp, this is 𝒪​(|F|)+𝒪​(1)\mathcal{O}(|F|)+\mathcal{O}(1), independent of NN and NuN\_{u}.

In particular, for fixed pp, both full recalibration and sharded recomputation scale linearly in NN and approximately linearly in NuN\_{u}, i.e. 𝒪​(N​Nu)\mathcal{O}(N\,N\_{u}) in the dominant term, whereas the fast refactorization operator has per-request complexity independent of NN and NuN\_{u} and grows only with the size of the forget set FF.

###### Proof.

For each quote ii, evaluation of the Heston price m​(xi;θ)m(x\_{i};\theta) via Fourier–Simpson quadrature requires 𝒪​(Nu)\mathcal{O}(N\_{u}) floating point operations, as the characteristic function φ​(u;θ)\varphi(u;\theta) and the integrand are evaluated at NuN\_{u} frequency nodes and combined by a weighted summation. Thus, pricing all NN quotes at a fixed parameter vector costs 𝒪​(N​Nu)\mathcal{O}(N\,N\_{u}) operations. The Gauss–Newton step additionally forms residuals rir\_{i} and Jacobians JiJ\_{i}, and accumulates

|  |  |  |
| --- | --- | --- |
|  | H=∑i=1NJi⊤​Ji,G=∑i=1NJi⊤​ri,H=\sum\_{i=1}^{N}J\_{i}^{\top}J\_{i},\qquad G=\sum\_{i=1}^{N}J\_{i}^{\top}r\_{i}, |  |

which require at most a constant factor overhead per quote when pp is fixed. Solving the normal equations (H+λ​I)​Δ​θ=G(H+\lambda I)\Delta\theta=G by, e.g., Cholesky factorization, has cost 𝒪​(p3)\mathcal{O}(p^{3}). This proves (i).

For sharded recomputation, only quotes in shards k∈K​(F)k\in K(F) are repriced and their Jacobians recomputed, while unaffected shards reuse their cached (Hk,Gk)(H\_{k},G\_{k}). If Neff​(F)N\_{\mathrm{eff}}(F) denotes the total number of quotes in the affected shards, then the cost of recomputing their contributions is 𝒪​(Neff​(F)​Nu)\mathcal{O}(N\_{\mathrm{eff}}(F)\,N\_{u}), followed by the same 𝒪​(p3)\mathcal{O}(p^{3}) solve on the updated global system. In the worst case, if K​(F)={1,…,K}K(F)=\{1,\dots,K\}, then Neff​(F)≈NN\_{\mathrm{eff}}(F)\approx N and the complexity coincides with full recalibration, establishing (ii).

For fast refactorization, no repricing or Jacobian evaluation is performed once the cache is built. Each forgotten quote i∈Fi\in F contributes a rank-one downdate222Each forgotten quote ii contributes a small p×pp\times p matrix
ψi=Ji⊤​Ji\psi\_{i}=J\_{i}^{\top}J\_{i} and vector ui=Ji⊤​riu\_{i}=J\_{i}^{\top}r\_{i} to the downdate
of (H,G)(H,G).
 ψi∈ℝp×p\psi\_{i}\in\mathbb{R}^{p\times p} and a vector downdate ui∈ℝpu\_{i}\in\mathbb{R}^{p} to (H,G)(H,G). Updating

|  |  |  |
| --- | --- | --- |
|  | H′=H−∑i∈Fψi,G′=G−∑i∈FuiH^{\prime}=H-\sum\_{i\in F}\psi\_{i},\qquad G^{\prime}=G-\sum\_{i\in F}u\_{i} |  |

requires 𝒪​(|F|​p2)\mathcal{O}(|F|\,p^{2}) operations. A fresh Cholesky factorization of H′H^{\prime} and back-substitution then cost 𝒪​(p3)\mathcal{O}(p^{3}). Since pp is fixed and small, these costs are independent of NN and NuN\_{u}, and the total complexity is 𝒪​(|F|​p2)+𝒪​(p3)\mathcal{O}(|F|\,p^{2})+\mathcal{O}(p^{3}), proving (iii).
∎

We finally note that our exactness statements are always with respect to the Gauss–Newton linearization at a reference point, not claiming global equivalence of fully iterated nonlinear solvers.
In practice, however, calibration is often near an optimum and a single GN/LM step is used as a local adjustment, which is precisely the regime our operators are designed for.

## 3 Illustrations

First333All scripts are in Python and all associated numerical illustrations presented in this manuscript are carried out on a system with i7 Core with 2.20 GHz and 16 GB RAM., we remark that in Figures of this section, unless stated otherwise, report the median over 3-5 random unlearning realizations per fraction, ensuring robustness to randomness in forgotten subsets.
We synthetically generate a surface of European call prices under the Heston model with known ground-truth parameters such as θtrue=(κ,θv,σv,ρ,v0)=(2.0, 0.06, 0.30,−0.6, 0.06),\theta\_{\mathrm{true}}=(\kappa,\theta\_{v},\sigma\_{v},\rho,v\_{0})=(2.0,\,0.06,\,0.30,\,-0.6,\,0.06), with r=0.01,S0=100.r=0.01,S\_{0}=100.
We generate a path of either 90 trading days for a small sample experiment or 180 trading days for a large sample experiment (Euler–Maruyama with correlated Brownian shocks; with Δ​t=1/252\Delta t=1/252 throughout this section).
For each day in the path we form European call quotes at maturities T∈{30,60}T\in\{30,60\} days (i.e., {30,60}/252\{30,60\}/252 years) and strikes X∈{90,100,110}X\in\{90,100,110\} for small sample experiment and maturities T∈{30,60,90}T\in\{30,60,90\} days and strikes X∈{80,90,100,110,120}X\in\{80,90,100,110,120\} for large sample experiment.
Option prices m​(xi;θ)m(x\_{i};\theta) are computed with the semi-analytic Heston formula via Fourier inversion and Simpson’s rule with either Umax=50U\_{\max}=50 and Nu=180N\_{u}=180 nodes or Umax=120,Nu=800U\_{\max}=120,\;N\_{u}=800 again depending on the sample size.
To emulate measurement noise, we perturb each price either by εi∼𝒩​(0,σ2)\varepsilon\_{i}\sim\mathcal{N}(0,\sigma^{2}) with σ=10−3\sigma=10^{-3} or εi∼𝒩​(0,(5×10−4)2)\varepsilon\_{i}\sim\mathcal{N}(0,(5\times 10^{-4})^{2}) for the small and large sample size, respectively.
We remark that the total number of quotes, NN, depend on the path horizon and coverage and is thus not fixed a priori.
We partition the quotes by calendar time into contiguous shards of either 10 or 30 days, similarly.
Starting from θref=(1.0, 0.04, 0.20,−0.3, 0.04)\theta^{\text{ref}}=(1.0,\,0.04,\,0.20,\,-0.3,\,0.04), we run a short Levenberg–Marquardt loop (Gauss–Newton with adaptive damping) to obtain θ⋆\theta^{\star}.
At θ⋆\theta^{\star}, we compute central finite-difference Jacobians Ji=∇θm​(xi;θ⋆)J\_{i}=\nabla\_{\theta}m(x\_{i};\theta^{\star}) and residuals ri=yi−m​(xi;θ⋆)r\_{i}=y\_{i}-m(x\_{i};\theta^{\star}).
We cache, for each quote ii, ui,ψi∈ℝ5u\_{i},\psi\_{i}\in\mathbb{R}^{5} and the global normal equations, (H,G)(H,G) together with a small Tikhonov term λ=10−6\lambda=10^{-6} (i.e., we solve with H+λ​IH+\lambda I).
We also store per-shard, (Hk,Gk)(H\_{k},G\_{k}) given a forget set ℱ⊂{1,…,N}\mathcal{F}\subset\{1,\dots,N\}.

Speaking of the cache, we remind that it is not a replica of the training data.
It stores only derivative-based sufficient statistics that summarize the model’s local curvature at the calibration optimum.
Forgetting operates by algebraic removal of those statistics associated with the forgotten samples, which is exactly what the unlearning literature defines as *data deletion at the parameter level*.
No raw strikes, maturities, or prices are revisited once the cache is built.

Our baseline, as we mentioned before, is the recalibration, full retraining in which we recompute all Jacobians and residuals on the retained subset from the raw quotes, thereby rebuilding the normal equations (H′,G′)(H^{\prime},G^{\prime})
and take one Gauss–Newton step to obtain θret=(θref+(H′+λ​I)−1​G′)\theta\_{\text{ret}}=(\theta^{\text{ref}}+(H^{\prime}+\lambda I)^{-1}G^{\prime}).
This represents a full recalibration from scratch and serves as the ground–truth
baseline for evaluating the two unlearning operators.

All timings are on a single laptop core (NumPy/BLAS pinned to one thread).
Because each calibration step involves only a few thousand Heston price evaluations and a single 5×55\times 5 linear solve, wall-clock runtimes are on the order of seconds even in the full configuration (Umax=120,Nu=800U\_{\max}=120,\,N\_{u}=800).
Subsequent unlearning operations reuse cached Jacobians and require no re-pricing, yielding sub-second updates.
This behavior is consistent with the 𝒪​(p3)\mathcal{O}(p^{3}) cost of the
Gauss–Newton linear system and the modest number of Fourier nodes per price evaluation.
More intuitively speaking, it is as we are not performing a full market-scale optimization but a one-step linearized Gauss–Newton update on a small synthetic grid.
We also stress that every plotted point is a median across independent random forget sets so that the figures already represents typical behavior, not a single lucky case.

We start by showing equivalence between retraining and our proposed machine unlearning approach, the fast factorization in this case.
By equivalence, we mean that up to machine precision (mostly on the order of 10−1310^{-13}); both approaches provide identical results.
We observe an exemplary comparison in Figure [1](https://arxiv.org/html/2511.14980v1#S3.F1 "Figure 1 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework") with the Heston variables separately shown, and the yy-axis shows the difference of θfast−θretrain\theta\_{\text{fast}}-\theta\_{\text{retrain}}.
We remark again that we reserve θv\theta\_{v} for a parameter of the Heston model, and θ\theta for the parameter space of the Heston model.
Subfigure [1(a)](https://arxiv.org/html/2511.14980v1#S3.F1.sf1 "In Figure 1 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework") shows per-parameter distributions of the same differences across all runs. The difference distribution of each parameter collapses around zero, and even that κ\kappa has broader variance it still is on the order of 10−1310^{-13}; meaning purely numerical floating-point variation.
Another note is that the *vase* in κ\kappa shows slightly more spread around zero, but still zero bias.

![Refer to caption](prec1.png)


(a) Per-parameter (all runs)

![Refer to caption](prec2.png)


(b) κ\kappa

![Refer to caption](prec3.png)


(c)  θv\theta\_{v}

![Refer to caption](prec4.png)


(d)  σv\sigma\_{v}

![Refer to caption](prec5.png)


(e)  ρ\rho

![Refer to caption](prec6.png)


(f)  v0v\_{0}

Figure 1: An exemplary comparison of equivalence of retraining and fast factorization with a smaller sample

Subfigures [1(b)](https://arxiv.org/html/2511.14980v1#S3.F1.sf2 "In Figure 1 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework")–[1(f)](https://arxiv.org/html/2511.14980v1#S3.F1.sf6 "In Figure 1 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework") compare parameter wise, while xx-axis indicates the mean of the two estimates (of retraining and fast factorization) for each parameter across runs (i.e., trials or experiments).
We remark that the vertical scale is around 10−1310^{-13}, and expectedly κ\kappa has higher variation due to pure round-off noise (i.e., the mean reversion speed is the most sensitive numerically).
We therefore conclude that the recalibration of the fast factorization is statistically indistinguishable from retraining fully, indicating perfect numerical agreement and no systematic bias across the parameters.
While we are aware of the fact that we provide an exemplary comparison, we remark that in several hundreds of trials based on different sources of randomness; we failed to see different behavior than that of in Figure [1](https://arxiv.org/html/2511.14980v1#S3.F1 "Figure 1 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework")444We present both estimates with the same color dots given that the dispersion is almost non-existent under the equivalence of machine precision..
Unlike the results presented in Figure [1](https://arxiv.org/html/2511.14980v1#S3.F1 "Figure 1 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework")–[2](https://arxiv.org/html/2511.14980v1#S3.F2 "Figure 2 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework") describes an exemplary comparison of all parameters and κ\kappa for a larger sample.
Especially, in Subfigure [2(a)](https://arxiv.org/html/2511.14980v1#S3.F2.sf1 "In Figure 2 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework"), we see more regular behavior due to the possible reasons we discussed in an earlier section, [2.3](https://arxiv.org/html/2511.14980v1#S2.SS3 "2.3 Fast refactor operator ‣ 2 Formulation of the unlearning problem ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework").
Even though we, for the time being, exclude the sharded recomputation for brevity in Figures [1](https://arxiv.org/html/2511.14980v1#S3.F1 "Figure 1 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework")–[2](https://arxiv.org/html/2511.14980v1#S3.F2 "Figure 2 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework"); similar visualizations could be constructed on the exactness of the sharded recomputation.
We remark, however, that there is no difference between all three approaches up to machine precision, i.e., ‖θfast−θretrain‖2<10−8\|\theta\_{\text{fast}}-\theta\_{\text{retrain}}\|\_{2}<10^{-8} and ‖θrecomp−θretrain‖2<10−8\|\theta\_{\text{recomp}}-\theta\_{\text{retrain}}\|\_{2}<10^{-8} in all instances we observed in large sample experiments along with.
Another reason for the exclusion of the sharded computation is timely, as it is highly sensitive to the forgetting set which we now discuss in Figure [3](https://arxiv.org/html/2511.14980v1#S3.F3 "Figure 3 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework").

![Refer to caption](prec_b_1.png)


(a)  Per parameter (all runs)

![Refer to caption](prec_b_2.png)


(b) κ\kappa

Figure 2: An exemplary comparison of equivalence of retraining and fast factorization with a larger sample

Full recalibration scales with the data set size since each quote requires multiple finite-difference Heston evaluations.
In contrast, the proposed fast refactor requires no re-pricing and runs in sub-millisecond time, as it merely updates the cached curvature system, unlike the sharded recomputation approach for reason we discuss now.
Recall that FF refers to the forget set, i.e. the subset of quotes the user asked to *unlearn*, 𝒦​(F)\mathcal{K}(F) refers to the set of affected shards with KK being the total number of shards.
The sharded recomputation should be faster than retraining only if the number of affected shard is smaller than number of shards, ∣𝒦​(F)∣≪K\mid\mathcal{K}(F)\mid\ll K.
Therefore, two cases become interesting that either there exists a small number of shards, or with higher likelihood that the forget set is spread *roughly uniformly* across all shards.
The second case suggests that almost every shard is affected.
In small experiments (few data per shard), shard recomputation skips a few shards and is faster.
In full-scale runs, when almost every shard contains forgotten quotes, recomputation is likely to degenerates to full retraining.
The recomputation cost approaches full retraining when the forget set is evenly distributed across shards.
Only the fast refactorization operator retains sub-millisecond latency regardless of shard coverage.

![Refer to caption](recomp_equal_almost_1_seed_42.png)


(a) Larger-sample configuration

![Refer to caption](recomp_equal_almost_1_seed_60.png)


(b) Larger-sample configuration

![Refer to caption](recomp_equal_almost_2_seed_42_debug.png)


(c) Smaller-sample configuration

![Refer to caption](recomp_equal_almost_2_seed_60_debug.png)


(d) Smaller-sample configuration

Figure 3: Example on the importance of the forgetting set for the sharded recomputation

We show this aspect in Figure [3](https://arxiv.org/html/2511.14980v1#S3.F3 "Figure 3 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework"), in which Subfigures [3(a)](https://arxiv.org/html/2511.14980v1#S3.F3.sf1 "In Figure 3 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework")–[3(b)](https://arxiv.org/html/2511.14980v1#S3.F3.sf2 "In Figure 3 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework") are based on a larger sample with the fixed random forgetting but different sources of randomness in the underlying paths leading to different quotes, the ones on the lower panel are from a smaller sample with the same characteristics; hence much lower computational time given in Subfigures [3(a)](https://arxiv.org/html/2511.14980v1#S3.F3.sf1 "In Figure 3 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework")–[3(b)](https://arxiv.org/html/2511.14980v1#S3.F3.sf2 "In Figure 3 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework").
In each example observable in Figure [3](https://arxiv.org/html/2511.14980v1#S3.F3 "Figure 3 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework"), the sharded recomputation tends to be in a co-movement with the retraining fully, especially after higher percentage of unlearned quotes.
So that in case of worst-case dispersion of deletions, i.e. too many shards being affected, the sharded recomputation is no longer cheap in computational cost.

![Refer to caption](when1.png)


(a) Effect of earlier shards

![Refer to caption](when2.png)


(b) Effect of no earlier shards

Figure 4: Exemplary demonstration of the sharding positions in sharded recomputation

In Figure [4](https://arxiv.org/html/2511.14980v1#S3.F4 "Figure 4 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework"), we demonstrate different forgetting parts and its effect on the relative computation time of the sharded recomputation by retraining.
Time ration on the yy-axis shows that if the time ratio is lower than one, the sharded recomputation is faster than retraining on the retained data.
By construction, xx-axis shows how many shards contain at least one forgotten quote.
While the second shard affected in Subfigure [4(a)](https://arxiv.org/html/2511.14980v1#S3.F4.sf1 "In Figure 4 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework"), Subfigure [4(b)](https://arxiv.org/html/2511.14980v1#S3.F4.sf2 "In Figure 4 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework") illustrates the first three shard is not affected.
If we were to decide not to unlearn some of the quotes in the experiments, this could overall be efficient in the first example, and with likely none to little effect on the second example in Subfigure [4(b)](https://arxiv.org/html/2511.14980v1#S3.F4.sf2 "In Figure 4 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework") as the current set-up is saving so little time given the affected shards.
Therefore, we stress strongly that the sharded recomputation method’s efficiency is governed by the locality of the forgotten data.

Across multiple independent runs, the relative parameter error consistently remained at machine precision, confirming the generality of the result.
The surface is fixed intentionally to ensure that performance differences stem solely from the unlearning mechanism, not from new random draws.
Additional seeds produced qualitatively identical behavior
The reported numbers in Tables [1](https://arxiv.org/html/2511.14980v1#S3.T1 "Table 1 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework") and [2](https://arxiv.org/html/2511.14980v1#S3.T2 "Table 2 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework") are medians across 10 runs and variability was negligible (IQR555IQR stands for interquartile range. below 1%\%).
While ss refers to seconds, m​sms refers to milliseconds (10−3​s10^{-3}s) and μ​s\mu s refers to microseconds (10−6​s10^{-6}s).

Table 1: Benchmark results across forgetting fractions.
Median runtimes and parameter deviations are reported.
The fast-refactor approach achieves identical accuracy to full retraining
with several orders of magnitude speedup.

| F(%) | Retrain | Recompute | Fast | RMSE kept (fast/retr) | Speedup |
| --- | --- | --- | --- | --- | --- |
| 1%\% | 21.06 s | 20.44 s | 174.2 μ​s\mu s | 0.00049 / 0.00049 | ×\times120,886.6 |
| 2%\% | 18.36 s | 18.05 s | 242.8 μ​s\mu s | 0.00049 / 0.00049 | ×\times75,639.3 |
| 5%\% | 17.71 s | 17.53 s | 436.9 μ​s\mu s | 0.00049 / 0.00049 | ×\times40,414.3 |
| 10%\% | 16.79 s | 16.61 s | 882.0 μ​s\mu s | 0.00049 / 0.00049 | ×\times19,268.7 |
| 25%\% | 14.31 s | 13.93 s | 2.12 m​sms | 0.00050 / 0.00050 | ×\times6,565.9 |

Although in Tables [1](https://arxiv.org/html/2511.14980v1#S3.T1 "Table 1 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework")–[2](https://arxiv.org/html/2511.14980v1#S3.T2 "Table 2 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework"), we employ different underlying paths so that different quotes could be generated, yet the forgetting sets are fixed across runs.
The first columns refer the fraction of data forgotten, and throughout the study we never control the forgetting set; we simply randomize it.
Reported values show that, on general, even in the worst case scenario the fast factorization speeds up the calibration by six thousand times, roughly four to five orders of magnitude speedup remarking strong evidence of the efficiency of the unlearning operator.
We remark that the speedup is measured as the ratio of median computation time taken via retraining by the median computation time taken via the fast factorization operator.
The fifth columns in Tables [1](https://arxiv.org/html/2511.14980v1#S3.T1 "Table 1 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework")–[2](https://arxiv.org/html/2511.14980v1#S3.T2 "Table 2 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework") measure the validation error on retained quotes,

Table 2: Benchmark results across forgetting fractions.
Median runtimes and parameter deviations are reported.
The fast-refactor approach achieves identical accuracy to full retraining
with several orders of magnitude speedup.

| F(%) | Retrain | Recompute | Fast | RMSE kept (fast/retr) | Speedup |
| --- | --- | --- | --- | --- | --- |
| 1%\% | 18.16 s | 17.63 s | 154.0 μ​s\mu s | 0.00049 / 0.00049 | ×\times120,110.6 |
| 2%\% | 18.01 s | 17.42 s | 230.0 μ​s\mu s | 0.00049 / 0.00049 | ×\times78,171.0 |
| 5%\% | 17.13 s | 17.08 s | 444.2 μ​s\mu s | 0.00049 / 0.00049 | ×\times38,550.8 |
| 10%\% | 16.19 s | 16.17 s | 816.2 μ​s\mu s | 0.00049 / 0.00049 | ×\times20,276.0 |
| 25%\% | 13.39 s | 13.37 s | 1.90 ms | 0.00050 / 0.00050 | ×\times7,059.7 |

Tables [1](https://arxiv.org/html/2511.14980v1#S3.T1 "Table 1 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework")–[2](https://arxiv.org/html/2511.14980v1#S3.T2 "Table 2 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework") illustrate retraining time does not scale perfectly linearly (since GN step cost flattens with fewer quotes).
Therefore, denominator decreases slightly faster than numerator.
We also observe that the effective speedup decreases monotonically with the forgotten fraction since a larger fraction of the cached structure must be updated or recomputed.
This scaling is consistent with the theoretical expectation that the cost advantage of refactorization diminishes as the retained set shrinks.
All timings were measured as median wall-clock durations over 10 runs using identical random seeds and quote subsets.
We now provide visual presentation of the experiments reported in Tables [1](https://arxiv.org/html/2511.14980v1#S3.T1 "Table 1 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework")–[2](https://arxiv.org/html/2511.14980v1#S3.T2 "Table 2 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework").

![Refer to caption](relative_error_1a_42.png)


(a) Typical behavior

![Refer to caption](relative_error_1a_60.png)


(b) Slight differencing at machine precision

Figure 5: Exemplary comparison of relative parameter error and runtime across forgetting fractions

Figure [5](https://arxiv.org/html/2511.14980v1#S3.F5 "Figure 5 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework") demonstrates relative parameter error against runtime across various forgetting fractions.
In Subfigures [5(a)](https://arxiv.org/html/2511.14980v1#S3.F5.sf1 "In Figure 5 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework")–[5(b)](https://arxiv.org/html/2511.14980v1#S3.F5.sf2 "In Figure 5 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework"), the deviation is calculated by ‖θf​a​s​t−θr​e​t​r​a​i​n‖2/‖θr​e​t​r​a​i​n‖2\|\theta\_{fast}-\theta\_{retrain}\|\_{2}/\|\theta\_{retrain}\|\_{2} given D∖FD\setminus F.
In Subfigure [5(a)](https://arxiv.org/html/2511.14980v1#S3.F5.sf1 "In Figure 5 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework"), we observe a perfectly flat blue line, all around 10−1510^{-15}, whereas Subfigure [5(b)](https://arxiv.org/html/2511.14980v1#S3.F5.sf2 "In Figure 5 ‣ 3 Illustrations ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework") demonstrates that the blue line jumps upward near 25%25\% around 10−1210^{-12}.
That single-point rise indicates that, for one run at the highest forgetting fraction fast and retrain parameters differed slightly more, probably due to numerical conditioning or cache subtraction noise.
Although this is evident that the unlearning operator behaves stably as relative parameter deviation remains near machine precision; an exemplary case such as this requires several remarks.
Higher percentage removals are actually a loss of too many informative points on the surface, carrying the risk of H′H^{\prime} becoming poorly conditioned and amplifying small floating-point noise in G′G^{\prime}.
Even with that, we remark that fast refactor method reproduces the retraining solution to floating-point accuracy.

A crucial remark is that we empirically observe that the positive-definiteness condition λmin​(H′)>0\lambda\_{\min}(H^{\prime})>0 remains satisfied well beyond typical forgetting levels.
In particular, the theoretical bound, ‖∑i∈Fψi‖2<λmin​(H)\|\sum\_{i\in F}\psi\_{i}\|\_{2}<\lambda\_{\min}(H), ensures that H′H^{\prime} remains positive definite, is rarely active until more than approximately 70%70\% of quotes are removed.
This indicates a strong numerical robustness of the downdate procedure and supports the stability of the fast-refactor updates under realistic unlearning scenarios.
We deem a further examination of the eigenvalue structure of the curvature matrix H′H^{\prime}
after forgetting to be of deeper interest to optimization algorithms rather than to the methodological structure of our unlearning framework.
Therefore, we keep this discussion brief and do not pursue an extensive numerical analysis beyond stability verification.

Empirically, calibration runtimes scale linearly in the number of quotes NN
and approximately quadratically in the number of Fourier–Simpson integration
nodes NuN\_{u}, in line with the overall 𝒪​(N​Nu)\mathcal{O}(N\,N\_{u}) cost of evaluating
the Heston pricing integral.
Since the parameter dimension pp is fixed and relatively small, the memory and computational cost of assembling and solving the Gauss–Newton normal equations is negligible.
The reported wall–clock times therefore match the analytic complexity of the pricing integral and the minimal number of nonlinear iterations typically required for Heston calibration.

The goal of our benchmark is not large–scale industrial calibration but a controlled and reproducible comparison of unlearning operators.
In this setting, second-level runtimes are representative and analytically consistent. The key
question is whether the proposed operators reproduce the calibration update on
the reduced dataset. Both unlearning operators achieve numerical agreement up to
machine precision, and the fast refactorization operator does so at a small
fraction of the computational cost; see Proposition [7](https://arxiv.org/html/2511.14980v1#Thmtheorem7 "Proposition 7 (Computational complexity of calibration and unlearning operators). ‣ 2.3 Fast refactor operator ‣ 2 Formulation of the unlearning problem ‣ Selective Forgetting in Option Calibration: An Operator-Theoretic Gauss–Newton Framework").

## 4 Conclusion

We have shown that the proposed unlearning operators admit rigorous guarantees; local exactness under fixed linearization and stability under curvature perturbations
Numerical experiments further confirm that the fast refactorization operator matches full retraining to floating-point precision and achieves several orders of magnitude speedup, even for substantial forgetting fractions.
Although algebraically simple, these operators rely on the observation that the Gauss–Newton normal equations encode a sufficient-statistics structure for nonlinear calibration.
Identifying the exact additive quantities whose removal preserves the optimality conditions under fixed linearization is, in our view, a nontrivial contribution and appears not to have been articulated previously in either the calibration or unlearning literature.

From a computational perspective, recalibration of the Heston model involves the evaluation of semi-analytic Fourier–Simpson integrals and accumulation of the p×pp\times p curvature matrix H=∑iJi⊤​JiH=\sum\_{i}J\_{i}^{\top}J\_{i}.
Even in the full configuration (Umax=120U\_{\max}=120, Nu=800N\_{u}=800), this entails only N×Nu≈106N\times N\_{u}\approx 10^{6} function evaluations for datasets of typical size (N≈103−104N\approx 10^{3}{-}10^{4}).
Such runtimes are modest in isolation, but financial institutions routinely process thousands of option books or parameter updates per day.
Recomputing all normal equations after each deletion therefore becomes costly, whereas the proposed unlearning operators perform mathematically exact deletions using only cached curvature statistics. The contribution is thus not raw speed alone, but the ability to *delete data deterministically without retraining*, enabling reversible and auditable calibration updates at negligible incremental cost.

Beyond computational gains, the framework reframes recalibration as an additive-subtractive operator calculus, enabling principled deletion of corrupted, stale, or restricted data.
This expands calibration from a purely forward-learning procedure into a bidirectional model-management process, useful for regulatory compliance, data-quality control, and influence diagnostics.
Although it is not in our interest yet our framework could also be used to quantify the influence of the subsets of data.
Questions such as which period affecting the calibration most, or what happens in case of exclusion of a data source might also be asked.

We focus on one representative semi-analytic model to isolate the operator behavior; extension to other models and real data is left for future work.
Future work may explore whether the operator perspective developed here extends beyond the static Gauss–Newton setting.
One natural question is how additive-subtractive updates interact with models that contain latent or filtered state variables, such as stochastic-volatility or regime-switching specifications, where forgetting would couple to the underlying filter-smoother structure.
Another possible direction concerns the use of the resulting sufficient-statistics calculus for influence diagnostics, for example to quantify the leverage of particular maturities, regimes, or data sources on the calibrated parameters.
The same viewpoint also suggests potential analogues for rolling-window or online calibration procedures, where the removal of stale information must be carried out without repeatedly rebuilding the normal equations from scratch.
Finally, a more ambitious line of inquiry is whether analogous operator rules exist for quasi-Newton or higher-order curvature representations.
Overall, these directions emphasize that machine unlearning should be regarded not only as a computational device, but as part of a broader operator-theoretic framework for interpretable, auditable, and dynamically maintainable calibration pipelines.

## Compliance with Ethical Standards

\bmhead

\*Competing Interests
There are no financial or non-financial interests directly or indirectly related to the work submitted for publication.
\bmhead\*Funding
There is no funding received in the making of this manuscript.