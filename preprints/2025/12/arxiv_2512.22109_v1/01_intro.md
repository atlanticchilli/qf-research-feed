---
authors:
- Dimitrios Roxanas
doc_id: arxiv:2512.22109v1
family_id: arxiv:2512.22109
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse
  Modelling and Uncertainty Quantification
url_abs: http://arxiv.org/abs/2512.22109v1
url_html: https://arxiv.org/html/2512.22109v1
venue: arXiv q-fin
version: 1
year: 2025
---


Dimitrios Roxanas

###### Abstract

We study the construction and rebalancing of sparse index-tracking portfolios from an operational research perspective, with explicit emphasis on uncertainty quantification and implementability. The decision variables are portfolio weights constrained to sum to one; the aims are to track a reference index closely while controlling the number of names and the turnover induced by rebalancing. We cast index tracking as a high-dimensional linear regression of index returns on constituent returns, and employ a sparsity-inducing Laplace prior on the weights. A single global shrinkage parameter controls the trade-off between tracking error and sparsity, and is calibrated by an empirical-Bayes stochastic approximation scheme. Conditional on this calibration, we approximate the posterior distribution of the portfolio weights using proximal Langevin-type Markov chain Monte Carlo algorithms tailored to the budget constraint. This yields posterior uncertainty on tracking error, portfolio composition and prospective rebalancing moves. Building on these posterior samples, we propose rules for rebalancing that gate trades through magnitude-based thresholds and posterior activation probabilities, thereby trading off expected tracking error against turnover and portfolio size. A case study on tracking the S&P 500 index is carried out to showcase how our tools shape the decision process from portfolio construction to rebalancing.

Keywords: Portfolio optimization; Index tracking; Uncertainty Quantification; Proximal MCMC; Rebalancing.

## 1 Introduction

Index-tracking funds seek to reproduce the performance of a market index
using a portfolio of its constituents. In practice, investors rarely hold all the names: they impose constraints on the number of assets, turnover, sector exposures, etc. This leads to an optimisation problem where one aims to minimise tracking error (TE) subject to budget and implementability constraints, and possibly with an explicit sparsity requirement on the weights.

A vast literature formulates index tracking as a deterministic optimisation problem, often using mixed-integer programming or convex relaxations; see, for example, (?, ?, ?, ?, ?, ?, ?, ?) and the references therein. The classical approaches deliver point portfolios but do not quantify uncertainty about the weights, the realised TE, or the need for rebalancing. Moreover, the cardinality of the tracking portfolio is either predetermined or controlled through a tuning parameter. In the latter case, a TE vs sparsity trade-off curve is commonly computed to help choose a good operating point, resulting in a large number of optimisation problems needing to be solved.

In parallel, Bayesian methods in portfolio optimisation have explored priors on weights and analytical posterior calculations in conjugate settings (e.g., (?, ?)). However, full posterior sampling over portfolio weights remains rare, particularly for index tracking, where the combination of high dimension, constraints and sparsity makes classical Markov chain Monte Carlo (MCMC) challenging. While a Bayesian *interpretation* is sometimes given for norm-constrained or penalised, e.g., with an ℓ1\ell\_{1} penalty augmentation, portfolios, e.g., (?, ?, ?, ?, ?, ?), *inference* on portfolio weights in a Bayesian framework is rarely employed. Existing sampling work is practically non-existent, and only focuses on subset selection, where one samples subsets of assets and fits weights conditionally, rather than sampling the full weight vector (?, ?, ?).

We address this gap by developing a *Bayesian* index-tracking formulation: a Gaussian regression likelihood, a sparsity-inducing Laplace prior on weights, and a soft budget constraint modelled as a Gaussian pseudo-observation. By sampling a posterior *over weights* directly, we obtain uncertainty quantification (UQ) on both magnitudes and support, enabling risk-aware decisions and hyperparameter learning within one probabilistic framework.

In particular, our approach will be based on the posterior distribution of weights ww, based on the observed data on index and asset returns,

|  |  |  |
| --- | --- | --- |
|  | π​(w):=p​(w|y)∝p​(y|w)​p​(w)\pi(w):=p(w|y)\propto\displaystyle p(y|w)\;p(w) |  |

All the models that we will consider will be of the form (up to a normalising factor)

|  |  |  |
| --- | --- | --- |
|  | π​(w)∝e−fy​(w)−θ​g​(w),\pi(w)\propto e^{-f\_{y}(w)-\theta g(w)}, |  |

the first factor corresponding to the likelihood (or model) part, while the second corresponds to the prior (here chosen to promote sparsity).

The contribution of this paper is to develop and study a *sampling-based* framework for sparse index tracking that connects modern optimisation and MCMC with decision support for portfolio construction and rebalancing. Our starting point is a regression formulation of index tracking, combined with a sparsity-inducing Laplace prior on the weights and a soft budget constraint introduced through a Gaussian pseudo-observation.

In particular, we

1. (C1)

   adopt an empirical-Bayes perspective and estimate a single global sparsity parameter by stochastic approximation (SAPG) (?, ?), rather than imposing it by hand;
2. (C2)

   approximate the resulting posterior distribution using proximal
   Langevin-type MCMC (MYULA and preconditioned MALA) (?, ?, ?), which leverage
   Moreau–Yosida regularisation and proximal mappings to handle the
   nonsmooth Laplace term under constraints;
3. (C3)

   use posterior samples to define simple, interpretable rules that
   connect UQ to implementable decisions: support selection, long-only portfolio construction and TE/turnover-aware rebalancing.

We illustrate the approach on a case study tracking the S&P 500 index
using a universe of several hundred constituents, over multiple fitting and holding periods. The case study highlights: (i) the quality of the sparse trackers obtained after posterior-informed selection, (ii) how posterior uncertainty on weight changes can be used to gate rebalancing decisions, and (iii) the trade-off between tracking error and turnover induced by different choices of thresholds.

We remark that the methodology can be easily extended beyond index tracking. It can also be applied to other sparse feature selection, and linear inverse problems with linear equality constraints, where one wishes to combine regularised optimisation, empirical-Bayes tuning of penalty scales and UQ-informed decision rules.

The rest of the paper is organised as follows. [Section˜2](https://arxiv.org/html/2512.22109v1#S2 "2 Model considerations ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification") introduces the Bayesian regression model, the soft budget constraint and the Laplace prior, and briefly describes empirical-Bayes calibration. [Section˜3](https://arxiv.org/html/2512.22109v1#S3 "3 Proximal MCMC for the posterior ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification") outlines the proximal MCMC algorithms used for posterior approximation. [Section˜4](https://arxiv.org/html/2512.22109v1#S4 "4 Posterior–informed support selection ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification") discusses the construction of a toolset based on posterior information, which is later used in [Section˜5](https://arxiv.org/html/2512.22109v1#S5 "5 Construction of a tradeable portfolio ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification") to construct a sparse, tradeable portfolio. [Section˜6](https://arxiv.org/html/2512.22109v1#S6 "6 Rebalancing ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification") presents a rebalancing
formulation based on weight adjustments and uncertainty-based gating
rules. [Section˜7](https://arxiv.org/html/2512.22109v1#S7 "7 A case study: tracking the S&P 500 ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification") documents a full case study on S&P 500 tracking. [Section˜8](https://arxiv.org/html/2512.22109v1#S8 "8 Discussion ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification") summarises the findings and outlines extensions.
Theoretical and technical details, as well as implementation guidelines and diagnostics, are left for the Appendices.

##### Acknowledgements:

The author wishes to thank K. Triantafyllopoulos (University of Sheffield) and K. Zygalakis (University of Edinburgh) for useful discussions.

## 2 Model considerations

### 2.1 Regression view and soft budget constraint

Let yty\_{t} denote the returns of the index at time tt and
rt∈ℝpr\_{t}\in\mathbb{R}^{p} the vector of returns of the pp constituents,
for t=1,…,Tt=1,\dots,T. We collect the data in y∈ℝTy\in\mathbb{R}^{T} and
R∈ℝT×pR\in\mathbb{R}^{T\times p}, and consider the regression

|  |  |  |  |
| --- | --- | --- | --- |
|  | yt=rt⊤​w+εt,εt∼𝒩​(0,σ2),y\_{t}=r\_{t}^{\top}w+\varepsilon\_{t},\qquad\varepsilon\_{t}\sim\mathcal{N}(0,\sigma^{2}), |  | (1) |

or in vector form y=R​w+εy=Rw+\varepsilon with ε∼𝒩​(0,σ2​IT)\varepsilon\sim\mathcal{N}(0,\sigma^{2}I\_{T}).
The portfolio weights w∈ℝpw\in\mathbb{R}^{p} must satisfy a budget constraint
1⊤​w=11^{\top}w=1, and we enforce long-only constraints wj≥0w\_{j}\geq 0 when constructing the final tradeable portfolio.

Working with a *hard* budget constraint inside the prior is natural
but makes empirical-Bayes updates and proximal MCMC more cumbersome.
Instead, we follow a pseudo-observation approach: we introduce
a Gaussian penalty that softly enforces the budget,

|  |  |  |  |
| --- | --- | --- | --- |
|  | fy​(w)=12​σ2​‖y−R​w‖22+Λ​(1⊤​w−1)2,f\_{y}(w)=\frac{1}{2\sigma^{2}}\|y-Rw\|\_{2}^{2}+\Lambda\bigl(1^{\top}w-1\bigr)^{2}, |  | (2) |

where Λ=1/(2​τc2)\Lambda=1/(2\tau\_{c}^{2}) and τc>0\tau\_{c}>0 encodes a tolerated
deviation from the exact budget. This yields the likelihood

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(y∣w)∝exp⁡{−fy​(w)}.p(y\mid w)\propto\exp\{-f\_{y}(w)\}. |  | (3) |

The budget constraint is enforced *exactly* at the portfolio
construction and rebalancing stages, but appears here as a soft penalty
to keep the prior separable.

### 2.2 Sparsity-inducing prior

We promote sparsity in ww through a weighted Laplace prior

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(w∣θ)∝exp⁡(−θ​∑j=1pαj​|wj|),θ>0,p(w\mid\theta)\propto\exp\,\!\Bigl(-\theta\sum\_{j=1}^{p}\alpha\_{j}|w\_{j}|\Bigr),\qquad\theta>0, |  | (4) |

where θ\theta is a global scale controlling shrinkage and
the weights αj>0\alpha\_{j}>0 encode per-asset sensitivity.

Following ideas from regularised regression, we choose
per-coordinate scales based on the columns of RR, for example

|  |  |  |  |
| --- | --- | --- | --- |
|  | sj=‖R⋅j‖2T,αj=max⁡{sj,ε}1p​∑k=1pmax⁡{sk,ε},s\_{j}=\frac{\|R\_{\cdot j}\|\_{2}}{\sqrt{T}},\qquad\alpha\_{j}=\frac{\max\{s\_{j},\varepsilon\}}{\frac{1}{p}\sum\_{k=1}^{p}\max\{s\_{k},\varepsilon\}}, |  | (5) |

with a small ε>0\varepsilon>0 to avoid numerical issues.
This yields a prior penalty θ​∑jαj​|wj|\theta\sum\_{j}\alpha\_{j}|w\_{j}|
that is roughly balanced across coordinates.

Combining likelihood and prior, the unnormalised posterior reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | π​(w∣y,θ)∝exp⁡{−fy​(w)−θ​g​(w)},g​(w)=∑j=1pαj​|wj|.\pi(w\mid y,\theta)\propto\exp\{-f\_{y}(w)-\theta g(w)\},\qquad g(w)=\sum\_{j=1}^{p}\alpha\_{j}|w\_{j}|. |  | (6) |

### 2.3 Role and effect of the likelihood parameters

The design of the likelihood part, as reflected in ([2](https://arxiv.org/html/2512.22109v1#S2.E2 "Equation 2 ‣ 2.1 Regression view and soft budget constraint ‣ 2 Model considerations ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification")), involves the parameters Λ\Lambda and σ2.\sigma^{2}.

Our feasible set is 𝒞:={w∈ℝp: 1p⊤​w=1},\mathcal{C}:=\{w\in\mathbb{R}^{p}:\ \mathbf{1}\_{p}^{\top}w=1\}, and one could incorporate this constraint by including the indicator function ι𝒞​(w)\iota\_{\mathcal{C}}(w) into the penalty/prior term. However, this creates complications in applying the SAPG algorithm of (?, ?). In short, the issue is that the constraint breaks the homogeneity of the Laplace prior (in a scaling sense, see the above work for more information). Akin to the constrained optimisation idea of using Lagrange multipliers, we incorporate the constraint via the term Λ​(𝟏⊤​w−1)2\Lambda\,(\mathbf{1}^{\top}w-1)^{2}, which will force near-satisfaction of the constraint.111We can tune it as desired: larger Λ\Lambda tightens sampling along the “budget axis” and shifts the MAP toward budget fidelity. However, we saw rather insubstantial differences in our experiments, so in the end we decided to keep Λ\Lambda fixed to avoid the need for excessive tuning, and to decouple it from the sparsity parameter selection.
We readjust at a later time by projecting the allocation vector to 𝒞\mathcal{C} to satisfy the constraint exactly. We set Λ=12​τc2,\Lambda\;=\;\frac{1}{2\tau\_{c}^{2}}, with τc\tau\_{c} a fixed user-defined allowed deviation from the hard constraint. This way, we treat the budget as a soft constraint via a quadratic penalty and enforce it with a convex and smooth term. The penalty can then be interpreted as a Gaussian “pseudo-measurement” on b=𝟏⊤​w−1b=\mathbf{1}^{\top}w-1, making τc\tau\_{c} a target standard deviation of the budget residual.

The final consideration when it comes to the likelihood is the *σ2\sigma^{2} factor*. From a modelling viewpoint, this can be seen as the noise variance or as a goodness-of-fit indicator in the regression with the index and its constituent asset returns. Therefore, any regression approach would yield very small σ2\sigma^{2}-values (for us, of the order of 10−910^{-9}, 10−710^{-7} at best). The role of σ2\sigma^{2} is much more pronounced in the rebalancing stage, where we construct the new portfolio wneww\_{\text{new}} by using the previous one, woldw\_{\text{old}}, as a baseline and focus on the vector of modifications, Δ​w,\Delta w, which, once selected, will yield wnew=wold+Δ​w, 1⊤​Δ​w=0.w\_{\text{new}}=w\_{\text{old}}+\Delta w,\;\mathbf{1}^{\top}\Delta w=0. Given that the rebalancing window is treated as a new data block, the posterior sees woldw\_{\text{old}} merely as a prior guess, and appears to be quite willing to move away from it when the data suggest that a richer combination can reduce TE. From a rebalancing or feature–adjustment perspective, this is exactly the opposite of the desired narrative: we want the *old* solution to be treated as “nearly optimal”, with only a small number of carefully chosen, posterior–justified tweaks. This suggests that for rebalancing, it can be more meaningful to use a *deliberately larger* σΔ​w2\sigma^{2}\_{\Delta w} that encodes the idea that pushing TE below a certain threshold is not worth additional turnover. Our method for this tuning is explained in Section [6](https://arxiv.org/html/2512.22109v1#S6 "6 Rebalancing ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification").

From a *computational* viewpoint, the effect of both parameters is reflected in the MCMC timestep. For stability, the timesteps we are allowed to use have to be smaller than 1/Lf,1/L\_{f}, where

|  |  |  |
| --- | --- | --- |
|  | Lf=1σ2​λmax​(RT​R+2​Λ​𝟏𝟏⊤).L\_{f}=\frac{1}{\sigma^{2}}\,\lambda\_{\max}(R^{T}R+2\Lambda\mathbf{1}\mathbf{1}^{\top}). |  |

Here LfL\_{f} is the Lipschitz constant from the likelihood part. It is an easy calculation to verify that when the soft constraint is absent from the likelihood, Lf′=1σ2​λmax​(RT​R),L\_{f}^{\prime}=\frac{1}{\sigma^{2}}\,\lambda\_{\max}(R^{T}R), where λm​a​x\lambda\_{max} is the largest eigenvalue of the RT​RR^{T}R matrix. In contrast, adding the quadratic soft-constraint term in the likelihood results in Lf=1σ2​λmax​(RT​R+2​Λ​𝟏𝟏⊤).L\_{f}=\frac{1}{\sigma^{2}}\,\lambda\_{\max}(R^{T}R+2\Lambda\mathbf{1}\mathbf{1}^{\top}). It turns out that, at least in the data sets we explored, the quadratic budget penalty adds a relatively small amount to the dominant eigenvalue. The main driver of stiffness is the combination of a very small σ2\sigma^{2}, and to a lesser extent, the spectrum of R⊤​RR^{\top}R, rather than Λ\Lambda itself. It is exactly the smallness of σ2\sigma^{2} that results in a very small timestep and slow mixing. We resort to preconditioning to counteract these issues.

## 3 Proximal MCMC for the posterior

(Theoretical and technical details, as well as implementation specifics, are provided in the Appendix.)

### 3.1 Moreau–Yosida smoothing and proximal gradient structure

The posterior π​(w∣y,θ⋆)\pi(w\mid y,\theta\_{\star}) combines a smooth quadratic
term fyf\_{y} with a convex but nonsmooth ℓ1\ell\_{1} term. Proximal MCMC
methods exploit this structure by replacing gg with its (differentiable) Moreau–Yosida envelope gλg\_{\lambda},

|  |  |  |  |
| --- | --- | --- | --- |
|  | gλ​(w)=minu∈ℝp⁡{g​(u)+12​λ​‖u−w‖22},for a chosen​λ>0g\_{\lambda}(w)=\min\_{u\in\mathbb{R}^{p}}\Bigl\{g(u)+\frac{1}{2\lambda}\|u-w\|\_{2}^{2}\Bigr\},\quad\text{for a chosen}\;\lambda>0 |  | (7) |

whose gradient is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇gλ​(w)=1λ​(w−proxλ​g⁡(w)),\nabla g\_{\lambda}(w)=\frac{1}{\lambda}\Bigl(w-\operatorname{prox}\_{\lambda g}(w)\Bigr), |  | (8) |

with proxλ​g\operatorname{prox}\_{\lambda g} the proximal mapping of gg.
For weighted ℓ1\ell\_{1} penalties, the prox reduces to componentwise soft-thresholding. Interest in these convex analysis tools originated from the popularity of non-smooth regularisers in applications to optimisation and statistical learning. It turns out that many of these regularisers have unique proximal maps that either have explicit formulas (as our example above) or can be computed efficiently (?, ?).

We work with a smoothed potential

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φλ​(w)=fy​(w)+θ⋆​gλ​(w),\Phi\_{\lambda}(w)=f\_{y}(w)+\theta\_{\star}g\_{\lambda}(w), |  | (9) |

whose gradient is Lipschitz continuous with constant LfL\_{f} that can be
bounded in terms of R⊤​RR^{\top}R, the budget penalty Λ\Lambda and λ\lambda.
This allows Langevin-type discretisations with principled step-size choices.

### 3.2 MYULA and preconditioned MALA

The Moreau–Yosida Unadjusted Langevin Algorithm (MYULA) (e.g., (?, ?, ?, ?, ?)) targets an
approximation πλ​(w∣y)\pi\_{\lambda}(w\mid y) to the posterior by iterating

|  |  |  |  |
| --- | --- | --- | --- |
|  | w(k+1)=w(k)−δ​∇Φλ​(w(k))+2​δ​ξ(k),ξ(k)∼𝒩​(0,Ip),w^{(k+1)}=w^{(k)}-\delta\nabla\Phi\_{\lambda}(w^{(k)})+\sqrt{2\delta}\,\xi^{(k)},\qquad\xi^{(k)}\sim\mathcal{N}(0,I\_{p}), |  | (10) |

with step size δ>0\delta>0. For a fixed θ⋆,\theta\_{\star}, the smoothed gradient for θ⋆​g\theta\_{\star}g is

|  |  |  |
| --- | --- | --- |
|  | ∇Φλ,θ⋆=∇fy​(w)+1λ​(w−proxλ​θ⋆​g⁡(w)),\nabla\Phi\_{\lambda,\,\theta\_{\star}}=\nabla f\_{y}(w)+\frac{1}{\lambda}\bigl(w-\operatorname{prox}\_{{\lambda\,\theta\_{\star}}g}(w)\bigr), |  |

We choose δ=0.9/(2​Lf)\delta=0.9/(2L\_{f}) and
λ=1/Lf\lambda=1/L\_{f}, which provides a good compromise between stability
and mixing in our experiments. In this work, MYULA is used both as an inner kernel
within SAPG and as a fast approximate sampler for exploratory runs.

To obtain higher-quality samples for reporting and UQ, we use a
preconditioned Metropolis-adjusted Langevin algorithm (MALA) targeting
πλ​(w∣y)\pi\_{\lambda}(w\mid y) more accurately. The proposal takes the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | w′=w−δ​P2​∇Φλ​(w)+2​δ​P​ξ,ξ∼𝒩​(0,Ip),w^{\prime}=w-\delta P^{2}\nabla\Phi\_{\lambda}(w)+\sqrt{2\delta}\,P\xi,\qquad\xi\sim\mathcal{N}(0,I\_{p}), |  | (11) |

where PP is a Jacobi preconditioner built from the diagonal of
R⊤​R/σ2R^{\top}R/\sigma^{2} (rescaled to balance coordinates), given by

|  |  |  |
| --- | --- | --- |
|  | P=D−1/2,where,D=diag⁡(1σ2​diag⁡(R⊤​R)+ 2​Λ​p).P=D^{-1/2},\quad\text{where,}\quad D=\operatorname{diag}\!\Big(\frac{1}{\sigma^{2}}\operatorname{diag}(R^{\top}R)\;+\;2\Lambda\,p\Big). |  |

that can equalise the curvature across coordinates (significantly improving mixing) without introducing too much complexity. In our experiments, the use of this preconditioning shrank the workable Lipschitz constant from 𝒪​(109)\mathcal{O}(10^{9}) to 𝒪​(102)\mathcal{O}(10^{2}), allowing proposal steps
δ≈0.9/(2​Lpre)\delta\approx 0.9/(2L\_{\mathrm{pre}}) in the 10−310^{-3}–10−210^{-2} range instead of 10−1110^{-11}.

To target bias, we complement the above with a MH correction using the usual Gaussian forward/backward densities. We use a short tuning phase to adjust δ\delta to yield an acceptance rate around 0.60,0.60, which is considered desirable.

### 3.3 Empirical-Bayes calibration of the sparsity parameter

The global scale θ\theta in ([4](https://arxiv.org/html/2512.22109v1#S2.E4 "Equation 4 ‣ 2.2 Sparsity-inducing prior ‣ 2 Model considerations ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification")) controls sparsity and is crucial for the trade-off between TE and the number of active assets. Rather than fixing θ\theta in ad hoc fashion, we adopt an empirical-Bayes approach and automatically estimate θ⋆\theta\_{\star} by maximising the marginal likelihood p​(y∣θ)p(y\mid\theta).

Direct optimisation of p​(y∣θ)p(y\mid\theta) is intractable because of the
Laplace prior in the presence of the budget constraint, and the high-dimensional integral. We therefore apply
the stochastic approximation proximal gradient (SAPG) scheme, developed
in (?, ?), to iteratively update θ\theta using Monte Carlo
estimates of the gradient of the log-marginal likelihood.

The SAPG algorithm is summarised in [Algorithm˜1](https://arxiv.org/html/2512.22109v1#alg1 "In 3.3 Empirical-Bayes calibration of the sparsity parameter ‣ 3 Proximal MCMC for the posterior ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification"). At iteration kk,
we generate a short Markov chain targeting (an approximation of)
π(⋅∣y,θk)\pi(\cdot\mid y,\theta\_{k}) and use the resulting sample to build a noisy
estimate of the gradient with respect to ηk\eta\_{k}. A Robbins–Monro
step-size schedule drives the updates, and a weighted average over
the tail of the run yields the empirical-Bayes estimate θ⋆\theta\_{\star}.

Algorithm 1  Empirical-Bayes calibration of θ\theta via SAPG (schematic)

1:Choose initial θ0>0\theta\_{0}>0 from a simple moment-matching rule and bounds

2:0<θmin≤θmax0<\theta\_{\min}\leq\theta\_{\max}; set η0=log⁡θ0\eta\_{0}=\log\theta\_{0}.

3:for k=0,1,…,Kk=0,1,\dots,K do

4:  Run a short MCMC chain targeting π(⋅∣y,θk)\pi(\cdot\mid y,\theta\_{k}), and obtain a sample
w(1),…,w(mk)w^{(1)},\dots,w^{(m\_{k})}.

5:  Form a Monte Carlo estimate of the gradient
Δk≈∂ηlog⁡p​(y∣θ)|θ=θk\Delta\_{k}\approx\partial\_{\eta}\log p(y\mid\theta)\big|\_{\theta=\theta\_{k}}.

6:  Update

|  |  |  |
| --- | --- | --- |
|  | ηk+1=Π[log⁡θmin,log⁡θmax]​{ηk+ρk​Δk},ρk=ck+k0,\eta\_{k+1}=\Pi\_{[\log\theta\_{\min},\log\theta\_{\max}]}\bigl\{\eta\_{k}+\rho\_{k}\Delta\_{k}\bigr\},\qquad\rho\_{k}=\frac{c}{k+k\_{0}}, |  |

and set θk+1=exp⁡(ηk+1)\theta\_{k+1}=\exp(\eta\_{k+1}).

7:end for

8:Return a Polyak–Ruppert average of the iterates as θ⋆\theta\_{\star}.

In more detail:

##### Heuristic initialisation.

In theory, the choice of the initial θ0\theta\_{0} for the SAPG iteration will not matter (asymptotically), but in practice, we saw that this wasn’t always the case. For this reason, based on an initial least-squares solution and a moment-matching argument we defined, for a small ϵ>0,\epsilon>0,

|  |  |  |
| --- | --- | --- |
|  | θ0=max⁡{p∑j=1pαj​|(wr​e​f)j|,ϵ},\theta\_{0}=\max\!\left\{\frac{p}{\sum\_{j=1}^{p}\alpha\_{j}|(w\_{ref})\_{j}|},\,\epsilon\right\}, |  |

using a reference solution wr​e​fw\_{ref} (see Appendix [A.1](https://arxiv.org/html/2512.22109v1#A1.SS1 "A.1 Heuristic choice of the initial scale 𝜃₀ ‣ Appendix A Stochastic Approximation Proximal Gradient algorithm (SAPG) ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification") for details).
We define Θ=[θ0/10,10​θ0]\Theta=[\theta\_{0}/10,10\,\theta\_{0}] and enforce θ∈Θ\theta\in\Theta to prevent numerically extreme values.

##### MYULA kernel for ww.

For a fixed θ\theta, we approximate the posterior p​(w∣θ)p(w\mid\theta) using the MYULA kernel on a Moreau–Yosida smoothed potential. We define the weighted proximal map (soft-thresholding)

|  |  |  |
| --- | --- | --- |
|  | proxλMY​θ(w)j=sign(wj)max{|wj|−λMYθαj, 0}.\operatorname{prox}\_{\lambda\_{\mathrm{MY}}\,\theta}(w)\_{j}=\operatorname{sign}(w\_{j})\,\max\bigl\{|w\_{j}|-\lambda\_{\mathrm{MY}}\,\theta\,\alpha\_{j},\,0\bigr\}. |  |

The MYULA step used inside SAPG is

|  |  |  |
| --- | --- | --- |
|  | w(k+1)=w(k)+δMYULA​(−∇fy​(w(k))−1λMY​(w(k)−proxλMY​θ⁡(w(k))))+2​δMYULA​ξ(k),w^{(k+1)}=w^{(k)}+\delta\_{\mathrm{MYULA}}\Bigl(-\nabla f\_{y}(w^{(k)})-\tfrac{1}{\lambda\_{\mathrm{MY}}}(w^{(k)}-\operatorname{prox}\_{\lambda\_{\mathrm{MY}}\theta}(w^{(k)}))\Bigr)+\sqrt{2\delta\_{\mathrm{MYULA}}}\,\xi^{(k)}, |  |

with ξ(k)∼𝒩​(0,Ip)\xi^{(k)}\sim\mathcal{N}(0,I\_{p}).

We warm-start the chain with θ=θ0\theta=\theta\_{0} before the SAPG updates.

##### SAPG update for θ\theta.

Let

|  |  |  |
| --- | --- | --- |
|  | g​(w)=∑j=1pαj​|wj|g(w)=\sum\_{j=1}^{p}\alpha\_{j}|w\_{j}| |  |

be the (scaled) ℓ1\ell\_{1} mass. We work on a logarithmic scale for the updates, and set η=log⁡θ\eta=\log\theta:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ηk+1=Π[log⁡θmin,log⁡θmax]​(ηk+ρk​(p−θk​S​(w(k)))),θk=eηk,\eta\_{k+1}=\Pi\_{[\log\theta\_{\min},\log\theta\_{\max}]}\Bigl(\eta\_{k}+\rho\_{k}(p-\theta\_{k}S(w^{(k)}))\Bigr),\qquad\theta\_{k}=e^{\eta\_{k}}, |  | (12) |

with step–size schedule ρk=c/(k+k0)\rho\_{k}=c/(k+k\_{0}). The chain {w(k)}\{w^{(k)}\} is driven by the MYULA kernel described above with the current θk\theta\_{k}.

After a burn–in of kburnk\_{\texttt{burn}} iterations, we compute a Polyak–Ruppert weighted average

|  |  |  |  |
| --- | --- | --- | --- |
|  | η¯=∑k>kburnωk​ηk∑k>kburnωk,ωk∝(k−kburn)q,\bar{\eta}=\displaystyle\frac{\sum\_{k>k\_{\mathrm{burn}}}\omega\_{k}\,\eta\_{k}}{\sum\_{k>k\_{\mathrm{burn}}}\omega\_{k}},\qquad\omega\_{k}\propto(k-k\_{\mathrm{burn}})^{q}, |  | (13) |

and define the empirical–Bayes estimate

|  |  |  |
| --- | --- | --- |
|  | θ⋆=eη¯.\theta\_{\star}=e^{\bar{\eta}}. |  |

Once θ⋆\theta\_{\star} has been obtained, the posterior for ww becomes

|  |  |  |
| --- | --- | --- |
|  | π​(w∣y):=π​(w∣y,θ⋆),\pi(w\mid y):=\pi(w\mid y,\theta\_{\star}), |  |

and all subsequent steps (posterior sampling, support selection,
rebalancing) are conditional on this empirical-Bayes choice.

## 4 Posterior–informed support selection

Unsurprisingly, given the choice of the prior, in our case studies, the MAP estimator has a significant number of very small (both positive and negative) but nonzero weights. From a practical point of view, an investor clearly would not want to take too many small positions, especially with no guarantees that they are indispensable for a low TE. We therefore seek to determine cut-off threshold(s) to determine which nonzero weights will automatically be set to zero. This applies to the process for designing both the original and the rebalanced portfolio.

### 4.1 Decoupling shrinkage from selection

Raw cardinality (the number of nonzero elements in the MAP) can overstate “effective” exposure when many coefficients are extremely small, but not exactly zero. Regardless of what prior is used, to go from the posterior to a sparse (enough) point estimate will typically require additional post-processing. As the authors of (?, ?) remark, thresholding rules provide an imperfect tool for cases where continuous (non-point mass) priors are placed on the regressors. We embrace this philosophy, also reflected in works on “projective inference” (e.g., see (?, ?) and later research). Essentially, a possibly not-extremely-sparse model that predicts well is constructed first, and then one proceeds (e.g., by either thresholding rules or “projection onto submodels”) by finding a sparser subset of the features that will characterise the predictions.

In our pipeline, we too decouple shrinkage and selection. First, we use the weighted-Laplace prior for sparsity, and then we allow the data to inform the selection of the parameter controlling the amount of sparsity enforced. From a Decision Theory point of view, this is equivalent to Bayesian model selection. Then, we craft decision rules for selection, based on UQ metrics obtained from sampling with this model. This allows us to optimise out-of-sample predictive scores under a size penalty in a principled, posterior-informed way.

### 4.2 Effective support

We now show how the results from the long MALA run can inform the formation of the holdable portfolio, and we do this by developing two tools to complement the MAP cardinality information. Unless otherwise specified, the same process applies to rebalancing, but we demonstrate the approach using the notation for the first portfolio.

#### 4.2.1 A noise-floor threshold

The first *effective sparsity* measure is based on a “noise-floor threshold”, τpost,\tau\_{\mathrm{post}}, based on which we will prune the very small MAP weights, by only keeping

|  |  |  |
| --- | --- | --- |
|  | SMAP={j:|wMAP,j|≥τpost}.S\_{\mathrm{MAP}}=\{j:|w\_{\mathrm{MAP},j}|\geq\tau\_{\mathrm{post}}\}. |  |

From the MALA samples, we estimate per-coordinate posterior standard deviations

|  |  |  |
| --- | --- | --- |
|  | s^j=sd⁡(wj(m)),j=1,…,p,\hat{s}\_{j}=\operatorname{sd}\bigl(w^{(m)}\_{j}\bigr),\qquad j=1,\dots,p, |  |

and define the posterior scale threshold

|  |  |  |  |
| --- | --- | --- | --- |
|  | τpost=k⋅medianjs^j\tau\_{\mathrm{post}}=k\cdot\operatorname\*{median}\_{j}\hat{s}\_{j} |  | (14) |

with a default k=2.5k=2.5.

This is in the same spirit as posterior-median thresholding/spike-and-slab rules (e.g., (?, ?)), where “effectively zero” is defined in terms of the posterior distribution, rather than arbitrary absolute cutoffs (e.g., posterior median shrinks small coefficients to zero and leaves big ones unchanged.)

In this case, ([14](https://arxiv.org/html/2512.22109v1#S4.E14 "Equation 14 ‣ 4.2.1 A noise-floor threshold ‣ 4.2 Effective support ‣ 4 Posterior–informed support selection ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification")) provides a robust way of estimating the “typical” posterior scale directly from the sampler, and reports it in “sigma” units. The decision to report a single, global τpost,\tau\_{\mathrm{post}}, rather than one per coordinate, is mostly for simplicity: notice that our choice ensures a monotone, with-a-single-parameter rule of controlling sparsity. Increasing kk always reduces the cardinality of the support, SS. Choosing k≈2.5k\approx 2.5 is more conservative than a loose 2​σ2\sigma rule (to avoid spurious tiny positions), but not as extreme as 3​σ3\sigma, which tends to prune more aggressively.

#### 4.2.2 Activation probabilities

We see τpost\tau\_{\mathrm{post}} as an indicator of what is “meaningfully non-zero” (relative to the posterior noise). Motivated to explicitly incorporate uncertainty quantification, we also compute “activation” probabilities

|  |  |  |  |
| --- | --- | --- | --- |
|  | π^j=Pr⁡(|wj|≥τpost∣data)≈1M​∑m=1M𝟏​{|wj(m)|≥τpost}.\hat{\pi}\_{j}=\Pr\bigl(|w\_{j}|\geq\tau\_{\mathrm{post}}\mid\text{data}\bigr)\approx\frac{1}{M}\sum\_{m=1}^{M}\mathbf{1}\{|w^{(m)}\_{j}|\geq\tau\_{\mathrm{post}}\}. |  | (15) |

Unlike spike–slab formulations with an explicit inclusion indicator
γj\gamma\_{j} and posterior inclusion probabilities P​(γj=1∣y)P(\gamma\_{j}=1\mid y), our
Laplace/MYULA setup works with a fully continuous posterior on the weights.

Metric ([15](https://arxiv.org/html/2512.22109v1#S4.E15 "Equation 15 ‣ 4.2.2 Activation probabilities ‣ 4.2 Effective support ‣ 4 Posterior–informed support selection ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification")) can be viewed as an inclusion probability
for the event “coefficient jj is meaningfully non-zero”, in the sense that its magnitude exceeds a data-adaptive multiple of the typical posterior standard deviation. This is analogous
in spirit to classical posterior inclusion probabilities (PIP), but with the “inclusion event” defined via a posterior scale threshold rather than a latent spike at zero.

#### 4.2.3 Selection rule

Our selection rule combines the above two tools, i.e., a *magnitude constraint*

|  |  |  |
| --- | --- | --- |
|  | |wjMAP|≥τpost|w\_{j}^{\mathrm{MAP}}|\geq\tau\_{\mathrm{post}} |  |

with a *certainty constraint*

|  |  |  |
| --- | --- | --- |
|  | P​(|wj|≥τpost∣y)≥π∗,P\bigl(|w\_{j}|\geq\tau\_{\mathrm{post}}\mid y\bigr)\geq\pi^{\ast}, |  |

for some π∗∈(0,1).\pi^{\ast}\in(0,1).

For a user–chosen activation threshold π⋆\pi^{\star}, we define:

|  |  |  |  |
| --- | --- | --- | --- |
|  | SUQ={j:|wMAP,j|≥τpost,π^j≥π⋆}.S\_{\mathrm{UQ}}=\{j:|w\_{\mathrm{MAP},j}|\geq\tau\_{\mathrm{post}},\;\hat{\pi}\_{j}\geq\pi^{\star}\}. |  | (16) |

Thus, the selected support consists of
*weights that are both large enough (in sigma units) and have high
posterior evidence for being that large*. This is in line with the
use of posterior quantities such as local false sign or discovery
rates for decision-making (see, e.g., (?, ?) for an empirical-Bayes treatment of such quantities in large-scale testing).

### 4.3 Short positions

In our baseline experiments, we ultimately implement long‐only tracking portfolios, even though the Bayesian machinery is formulated on the unconstrained long–short space (via the choice of the symmetric Laplace prior). The long-only decision reflects the practical mandate and operational reality of plain index trackers: maintaining short positions requires margin, additional broker arrangements and monitoring, which are rarely justifiable for passive, infrequently rebalanced products. We therefore use the full long–short posterior only as a statistical engine—to estimate activation probabilities, posterior scales and sign probabilities—and then apply a simple long‐only decision rule at the end: negative weights are set to zero (or, in the *rebalancing step* where negative adjustments are acceptable, any proposed move that would cross through zero is truncated at zero); we then restore the budget over the remaining active names. Note that our original machinery, which allows shorts, can be beneficial both in applications of *enhanced index tracking* and other portfolio optimisation problems.

## 5 Construction of a tradeable portfolio

In this section, we elaborate on our method for designing a tracking portfolio for the first trading period. We remark that our method is general enough to apply to other sparse feature selection problems practically as is.

##### Centering and scaling

To avoid having to include an intercept (and for numerical stability), we centre both index and regressors on the estimation window (which we refer to as the FIT–1 period):

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | yμ\displaystyle y\_{\mu} | =1T​∑t=1Tyt,\displaystyle=\frac{1}{T}\sum\_{t=1}^{T}y\_{t}, | Rμ\displaystyle R\_{\mu} | ∈ℝp,(Rμ)j=1T​∑t=1TRt​j,\displaystyle\in\mathbb{R}^{p},\quad(R\_{\mu})\_{j}=\frac{1}{T}\sum\_{t=1}^{T}R\_{tj}, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | yc\displaystyle y\_{c} | =y−yμ​𝟏T,\displaystyle=y-y\_{\mu}\mathbf{1}\_{T}, | Rc\displaystyle R\_{c} | =Rfit−𝟏T​Rμ⊤,\displaystyle=R\_{\mathrm{fit}}-\mathbf{1}\_{T}R\_{\mu}^{\top}, |  |

where TT is the length of the FIT–1 window. We then work with the centred Gaussian likelihood,

|  |  |  |
| --- | --- | --- |
|  | yc∣w∼𝒩​(Rc​w,σ2​IT).y\_{c}\mid w\sim\mathcal{N}(R\_{c}w,\;\sigma^{2}I\_{T}). |  |

where σ2\sigma^{2} is the noise variance estimated on (yc,Rc).(y\_{c},R\_{c}).

### 5.1 Noise variance estimation

We start by pre-estimating (see Appendix [C](https://arxiv.org/html/2512.22109v1#A3 "Appendix C Noise variance estimation ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification")) the noise variance σ2\sigma^{2}, which appears as a parameter in the likelihood. We tested several estimators that operate on the residuals of the regression model, and we chose the *median absolute deviation* (MAD) estimator (?, ?) because of its robustness to outliers; we report σ^2=σ^MAD2.\widehat{\sigma}^{2}\;=\;\widehat{\sigma}\_{\mathrm{MAD}}^{2}. We note that the budget constraint
𝟏⊤​w=1\mathbf{1}^{\top}w=1
*does not enter* the variance estimation at all: we work with the unconstrained OLS fit and its residuals. The rationale is that
σ^2\widehat{\sigma}^{2} should reflect the scale of the *tracking
error* yt−rt⊤​wy\_{t}-r\_{t}^{\top}w under a purely data-driven fit, without being distorted by how we choose to enforce the budget constraint. The constraint is imposed later, at the level of the prior
and posterior geometry, but not in the noise-scale estimation stage.

### 5.2 The MAP estimator

Having estimated σ^2=σ^MAD2,\widehat{\sigma}^{2}\;=\;\widehat{\sigma}\_{\mathrm{MAD}}^{2}, we are in a position to calculate the timestep for the MCMC chain ([10](https://arxiv.org/html/2512.22109v1#S3.E10 "Equation 10 ‣ 3.2 MYULA and preconditioned MALA ‣ 3 Proximal MCMC for the posterior ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification")), and employ the SAPG algorithm described in subsection [3.3](https://arxiv.org/html/2512.22109v1#S3.SS3 "3.3 Empirical-Bayes calibration of the sparsity parameter ‣ 3 Proximal MCMC for the posterior ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification").

Given θ⋆,\theta\_{\star}, the output of SAPG, we first
compute a maximum a posteriori (MAP) estimator of ww,

|  |  |  |  |
| --- | --- | --- | --- |
|  | w^MAP∈arg​minw∈ℝp⁡{fy​(w)+θ⋆​g​(w)},\hat{w}\_{\text{MAP}}\in\operatorname\*{arg\,min}\_{w\in\mathbb{R}^{p}}\bigl\{f\_{y}(w)+\theta\_{\star}g(w)\bigr\}, |  | (17) |

using FISTA (?, ?). The smooth part fyf\_{y} is treated
by a gradient step with step size 1/Lf1/L\_{f}, while gg is handled via the
weighted soft-thresholding prox. The algorithm stops when the objective difference falls below a relative tolerance threshold. This yields a dense but heavily shrunk vector of weights.

### 5.3 Long MALA run

For posterior summaries, we run a long Markov chain with θ⋆\theta\_{\star} fixed, targeting the MY smoothed posterior

|  |  |  |
| --- | --- | --- |
|  | π~​(w)∝exp⁡(−Φλ,θ⋆​(w)),\tilde{\pi}(w)\propto\exp\bigl(-\Phi\_{\lambda,\,\theta\_{\star}}(w)\bigr), |  |

as described in Subsection [3.2](https://arxiv.org/html/2512.22109v1#S3.SS2 "3.2 MYULA and preconditioned MALA ‣ 3 Proximal MCMC for the posterior ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification"). In particular, we run a long MALA chain with the preconditioned kernel starting from wMAPw\_{\mathrm{MAP}} and, after discarding the samples of a burn-in stage, we form

|  |  |  |
| --- | --- | --- |
|  | {w(m)}m=1M≡Wlong∈ℝM×p.\{w^{(m)}\}\_{m=1}^{M}\equiv W\_{\mathrm{long}}\in\mathbb{R}^{M\times p}. |  |

During this stage, we monitor the trace *log⁡π​(w)=Φλ,θ⋆​(w)\log\pi(w)=\Phi\_{\lambda,\theta\_{\star}}(w)* for stationarity, and also the ACF decay and effective sample sizes (ESS) for selected coordinates as indicators of the quality of mixing.

### 5.4 Posterior-informed support selection and the tradeable portfolio

Recall from Section [4.2.3](https://arxiv.org/html/2512.22109v1#S4.SS2.SSS3 "4.2.3 Selection rule ‣ 4.2 Effective support ‣ 4 Posterior–informed support selection ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification") that our selection rule combines two tools, i.e., a *magnitude constraint*

|  |  |  |
| --- | --- | --- |
|  | |wjMAP|≥τpost|w\_{j}^{\mathrm{MAP}}|\geq\tau\_{\mathrm{post}} |  |

with a *certainty constraint*

|  |  |  |
| --- | --- | --- |
|  | P​(|wj|≥τpost∣y)≥π∗,P\bigl(|w\_{j}|\geq\tau\_{\mathrm{post}}\mid y\bigr)\geq\pi^{\ast}, |  |

for some π∗∈(0,1)\pi^{\ast}\in(0,1). For a chosen activation threshold π⋆\pi^{\star}, we collect the indices of the kept weights in the set

|  |  |  |  |
| --- | --- | --- | --- |
|  | S0={j:|wMAP,j|≥τpost,π^j≥π⋆}.S\_{0}=\{j:|w\_{\mathrm{MAP},j}|\geq\tau\_{\mathrm{post}},\;\hat{\pi}\_{j}\geq\pi^{\star}\}. |  | (18) |

##### Long-only refinement.

For passive index tracking with infrequent rebalancing, we prefer to avoid explicit short positions in the *inception* portfolio even if the underlying prior is symmetric. To this end, we refine the set S0S\_{0} to a long-only active set

|  |  |  |  |
| --- | --- | --- | --- |
|  | S={j:|wMAP,j|≥τpost,π^j≥π⋆;wj≥0}.S=\{j:|w\_{\mathrm{MAP},j}|\geq\tau\_{\mathrm{post}},\;\hat{\pi}\_{j}\geq\pi^{\star};w\_{j}\geq 0\}. |  | (19) |

### Construction of a tradeable portfolio

We refer to the weights of the assets corresponding to the above SS by

|  |  |  |
| --- | --- | --- |
|  | (wpruned)j={(wMAP)j,j∈S,0,j∉S.(w\_{\mathrm{pruned}})\_{j}=\begin{cases}(w\_{\mathrm{MAP}})\_{j},&j\in S,\\[1.99997pt] 0,&j\notin S.\end{cases} |  |

In what follows, Rc,SR\_{c,S} is the submatrix of RcR\_{c} with columns in SS.

Based on these weights, one can form and invest in several sparse portfolios; some examples are given below:

1. (a)

   Pruned portfolio with budget projection.
   We project wprunedw\_{\mathrm{pruned}} back to the budget hyperplane by an equal shift222While this is not the only option, note that we don’t want to simply project wprunedw\_{\mathrm{pruned}} onto the constraint set as this reintroduces non-zero entries in coordinates that were found to be (or made) zero.
   on SS:

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | wpruned,proj,j={(wpruned)j+δ,j∈S,0,j∉S,δ=1−∑j∈S(wpruned)j|S|.w\_{\mathrm{pruned,proj},j}=\begin{cases}(w\_{\mathrm{pruned}})\_{j}+\delta,&j\in S,\\[1.99997pt] 0,&j\notin S,\end{cases}\qquad\delta=\frac{1-\sum\_{j\in S}(w\_{\mathrm{pruned}})\_{j}}{|S|}. |  | (20) |
2. (b)

   Refitting on SS with FISTA - (this is the one we will hold)

   To allow the penalty to reshape the weights on SS, we re–solve the MAP problem restricted to SS. However, even on the long-only SS FISTA can still produce negative entries, unless we explicitly enforce wj≥0.w\_{j}\geq 0. So we now solve,

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | minwS∈ℝ|S|⁡12​σ2​‖yc−Rc,S​wS‖22+Λ​(1⊤​wS−1)2+θ⋆​∑j∈Sαj​|(wS)j|+ιw≥0​(w),\min\_{w\_{S}\in\mathbb{R}^{|S|}}\frac{1}{2\sigma^{2}}\,\|y\_{c}-R\_{c,S}w\_{S}\|\_{2}^{2}+\Lambda(1^{\top}w\_{S}-1)^{2}+\theta\_{\star}\sum\_{j\in S}\alpha\_{j}|(w\_{S})\_{j}|+\iota\_{w\geq 0}(w), |  | (21) |

   where w≥0w\geq 0 is interpreted entry-wise, and ιw≥0\iota\_{w\geq 0} is the corresponding indicator function. Then the proximal step (with the notation g+g\_{+} to signify the incorporation of the constraint) becomes

   |  |  |  |
   | --- | --- | --- |
   |  | proxt​g+⁡(w)=arg​minz≥0⁡12​‖z−w‖2+t​θ⋆​∑j∈Sαj​|zj|.\operatorname{prox}\_{tg\_{+}}(w)=\operatorname\*{arg\,min}\_{z\geq 0}\frac{1}{2}\|z-w\|^{2}+t\;\theta\_{\star}\sum\_{j\in S}\alpha\_{j}|z\_{j}|. |  |

   As the constraint is separable and |wj|=wj,for​wj≥0,|w\_{j}|=w\_{j},\;\text{for}\,w\_{j}\geq 0, this prox is just positive soft-thresholding, i.e., coordinate-wise:

   |  |  |  |
   | --- | --- | --- |
   |  | proxt​g+(w))j=max{wj−tθ⋆αj,0}.\operatorname{prox}\_{tg\_{+}}(w))\_{j}=\max\{w\_{j}-t\,\theta\_{\star}\,{\alpha}\_{j},0\}. |  |

   A separate Lipschitz constant LSL\_{S} is estimated for the restricted Hessian

   |  |  |  |
   | --- | --- | --- |
   |  | ∇2fS=1σ2​Rc,S⊤​Rc,S+2​Λ​ 11⊤,\nabla^{2}f\_{S}=\frac{1}{\sigma^{2}}R\_{c,S}^{\top}R\_{c,S}+2\Lambda\,11^{\top}, |  |

   and we run FISTA to obtain wS,FISTAw\_{S,\mathrm{FISTA}}. A final optional budget correction shift, i.e., as in ([20](https://arxiv.org/html/2512.22109v1#S5.E20 "Equation 20 ‣ Item (a) ‣ Construction of a tradeable portfolio ‣ 5 Construction of a tradeable portfolio ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification")), wS,FISTAw\_{S,\mathrm{FISTA}} to enforce 𝟏⊤​𝐰𝐒,FISTA=1{\bf 1^{\top}w\_{S,\mathrm{FISTA}}}=1 exactly. Embedding back to ℝp\mathbb{R}^{p} with zeros off SS gives

   |  |  |  |
   | --- | --- | --- |
   |  | wFISTA​\_​S∈ℝp.w\_{\mathrm{FISTA\\_S}}\in\mathbb{R}^{p}. |  |
3. (c)

   De-biased on SS with exact budget.
   If the long-only constraint were not imposed, we would solve the constrained least–squares problem

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | minu∈ℝ|S|⁡12​σ^2​‖yc−Rc,S​u‖22s.t.1⊤​u=1.\min\_{u\in\mathbb{R}^{|S|}}\frac{1}{2\hat{\sigma}^{2}}\,\|y\_{c}-R\_{c,S}u\|\_{2}^{2}\quad\text{s.t.}\quad 1^{\top}u=1. |  | (22) |

   This is done via a KKT system

   |  |  |  |
   | --- | --- | --- |
   |  | [H11⊤0]​[uμ]=[Rc,S⊤​yc/σ21],H=1σ2​Rc,S⊤​Rc,S+ρ​I,\begin{bmatrix}H&1\\[1.00006pt] 1^{\top}&0\end{bmatrix}\begin{bmatrix}u\\ \mu\end{bmatrix}=\begin{bmatrix}R\_{c,S}^{\top}\,y\_{c}\,/\,\sigma^{2}\\ 1\end{bmatrix},\qquad H=\frac{1}{\sigma^{2}}R\_{c,S}^{\top}R\_{c,S}+\rho I, |  |

   with a very small (user-defined) ridge ρ>0\rho>0 and Lagrange multiplier μ\mu.The resulting uu is embedded into ℝp\mathbb{R}^{p} by zero–padding to yield wdebiasw\_{\mathrm{debias}}. The idea is to, after selecting the active set SS, de-bias on that support under the exact budget constraint to remove shrinkage bias.

   However, with the non-negativity constraint, we need to solve

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | minu∈ℝ|S|⁡12​σ^2​‖yc−Rc,S​u‖22s.t.1⊤​u=1,w≥0,\min\_{u\in\mathbb{R}^{|S|}}\frac{1}{2\hat{\sigma}^{2}}\,\|y\_{c}-R\_{c,S}u\|\_{2}^{2}\quad\text{s.t.}\quad 1^{\top}u=1,\quad w\geq 0, |  | (23) |

   which is a convex quadratic program with no closed-form KKT anymore. In this case (but we don’t pursue it here), one could instead use, e.g., gradient descent on the smooth part and project each iterate onto the simplex (computationally cheap).

For single-period strategies or myopic formulations with linear/fixed costs, this would be the last step of the workflow.

## 6 Rebalancing

Our focus here is passive index tracking, therefore our working assumption is that the investor follows a buy–and–hold over a trading window with no daily rebalancing. At the end of the trading period (typically four, six or twelve months), one would evaluate the performance of the held portfolio and compute structural diagnostics that will inform their next steps. In this work, we focus on maintaining a low TE rather than trying to beat the index in terms of returns or drawdown. We warn against trying to aggressively shrink the TE, as this is very likely to result in overfitting and suboptimal out-of-sample results.

We frame the rebalancing problem as an optimisation problem with adjustment vector Δ​w\Delta w playing the role of the decision variable. The new allocation vector will be

|  |  |  |
| --- | --- | --- |
|  | wnew=wold+Δ​w,w\_{\text{new}}=w\_{\text{old}}+\Delta w, |  |

where woldw\_{\text{old}} is the portfolio held up to this point. To maintain the budget constraint on wneww\_{\text{new}}
we enforce the hard sum–zero constraint

|  |  |  |
| --- | --- | --- |
|  | 1⊤​Δ​w=01^{\top}\Delta w=0 |  |

for Δ​w\Delta w so that the budget constraint is preserved exactly.

### 6.1 Tracking error and sparsity considerations for rebalancing

##### The fitting window

Using the same length as before, TT, we construct a second fitting window ending at the evaluation date of the first portfolio; we refer to this as the “FIT–2” window. We operate with the vector y2∈RTy\_{2}\in R^{T} of index returns, and the matrix R2∈ℝT×pR\_{2}\in\mathbb{R}^{T\times p} of asset returns.

As before, we centre:

|  |  |  |
| --- | --- | --- |
|  | y2,μ=1T​∑ty2,t,R2,μ,j=1T​∑tR2,t​j,j∈{1,…,p}y2,c=y2−y2,μ​𝟏T,R2,c=R2−𝟏T​R2,μ⊤,\begin{split}y\_{2,\mu}&=\frac{1}{T}\sum\_{t}y\_{2,t},\quad R\_{2,\mu,j}=\frac{1}{T}\sum\_{t}R\_{2,tj},\qquad j\in\{1,\dots,p\}\\ y\_{2,c}&=y\_{2}-y\_{2,\mu}\mathbf{1}\_{T},\qquad R\_{2,c}=R\_{2}-\mathbf{1}\_{T}R\_{2,\mu}^{\top},\end{split} |  |

and build a new set of scales α(2)\alpha^{(2)} based on R2,cR\_{2,c}. Define the residual target

|  |  |  |
| --- | --- | --- |
|  | y2,res=y2,c−R2,c​wold.y\_{2,\mathrm{res}}\;=\;y\_{2,c}-R\_{2,c}w\_{\text{old}}. |  |

Then, for any Δ​w\Delta w we have the algebraic identity

|  |  |  |
| --- | --- | --- |
|  | y2,c−R2,c​(wold+Δ​w)=y2,res−R2,c​Δ​w.y\_{2,c}-R\_{2,c}(w\_{\text{old}}+\Delta w)\;=\;y\_{2,\mathrm{res}}-R\_{2,c}\Delta w. |  |

##### Laplace prior and choice of weights on Δ​w\Delta w.

On FIT–2 we build a weighted Laplace prior on Δ​w\Delta w,

|  |  |  |
| --- | --- | --- |
|  | p​(Δ​w∣κ)∝exp⁡(−κ​SΔ​(Δ​w))​ι{𝟏⊤​Δ​w=0},SΔ​(Δ​w)=∑j=1pαj(Δ)​|Δ​wj|.p(\Delta w\mid\kappa)\;\propto\;\exp\!\Bigl(-\kappa\,S\_{\Delta}(\Delta w)\Bigr)\;\mathbb{\iota}\_{\{\mathbf{1}^{\top}\Delta w=0\}},\qquad S\_{\Delta}(\Delta w)\;=\;\sum\_{j=1}^{p}\alpha^{(\Delta)}\_{j}\,|\Delta w\_{j}|. |  |

The base scales are recomputed from R2,cR\_{2,c} using the same
column-norm recipe as in FIT–1,

|  |  |  |
| --- | --- | --- |
|  | α~j=‖R2,c(:,j)‖2T,α~j←α~j/α~¯,\tilde{\alpha}\_{j}\;=\;\frac{\|R\_{2,c}^{(:,j)}\|\_{2}}{\sqrt{T}},\qquad\tilde{\alpha}\_{j}\leftarrow\tilde{\alpha}\_{j}/\overline{\tilde{\alpha}}, |  |

and we then *square* them for the rebalancing prior,

|  |  |  |
| --- | --- | --- |
|  | αj(Δ)=(α~j)2.\alpha^{(\Delta)}\_{j}\;=\;\bigl(\tilde{\alpha}\_{j}\bigr)^{2}. |  |

This decision deliberately penalises high-volatility names more strongly:
if α~j\tilde{\alpha}\_{j} is large (volatile column), then αj(Δ)\alpha^{(\Delta)}\_{j} is
larger still, so the Laplace penalty discourages frequent sign changes or
small adjustments in such components. Intuitively, this introduces a
“hysteresis” effect: noisy names must present a clearer signal before
their Δ​wj\Delta w\_{j} is moved away from zero.

##### Target and constraint domain.

The working posterior on FIT--2 is

|  |  |  |  |
| --- | --- | --- | --- |
|  | πκ​(Δ​w∣data)∝exp⁡{−12​σΔ​w2​‖y2,res−R2,c​Δ​w‖22−κ​SΔ​(Δ​w)}​ι{𝟏⊤​Δ​w=0}.\pi\_{\kappa}(\Delta w\mid\text{data})\;\propto\;\exp\!\left\{-\frac{1}{2\sigma^{2}\_{\Delta w}}\,\bigl\|y\_{2,\mathrm{res}}-R\_{2,c}\Delta w\bigr\|\_{2}^{2}-\kappa\,S\_{\Delta}(\Delta w)\right\}\;\iota\_{\{\mathbf{1}^{\top}\Delta w=0\}}. |  | (24) |

We work on the sum-zero subspace

|  |  |  |
| --- | --- | --- |
|  | H={Δ​w∈ℝp:𝟏⊤​Δ​w=0},H\;=\;\{\Delta w\in\mathbb{R}^{p}:\mathbf{1}^{\top}\Delta w=0\}, |  |

which is a subspace of dimension d=p−1d=p-1.
Thanks to the 1–homogeneity of SΔS\_{\Delta}, it follows that, under the prior alone,
𝔼κ​[SΔ​(Δ​W)]=d/κ.\mathbb{E}\_{\kappa}[S\_{\Delta}(\Delta W)]=d/\kappa.
This leads to the mean-zero score

|  |  |  |
| --- | --- | --- |
|  | g​(η;Δ​w)=d−κ​SΔ​(Δ​w),η=log⁡κ,g(\eta;\Delta w)\;=\;d-\kappa\,S\_{\Delta}(\Delta w),\qquad\eta=\log\kappa, |  |

which we use inside SAPG. In practical terms, this allows for the application of the most straightforward of the SAPG variants put forward in (?, ?).

##### Treating the noise scale as a TE–related parameter.

We estimate σ2\sigma^{2} for the new period using the MAD estimator as before. However, as expected, the baseline estimator σΔ​w,base2\sigma^{2}\_{\Delta w,\mathrm{base}} is numerically too small to be trusted as a direct description of the out–of–sample TE: it merely reflects the in–sample fit of an aggressively optimised constrained LS portfolio. As discussed in Section [2.3](https://arxiv.org/html/2512.22109v1#S2.SS3 "2.3 Role and effect of the likelihood parameters ‣ 2 Model considerations ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification"), in practice we wish to *choose* a “noise level” that is consistent with the realised TE over the FIT–2 window for the existing portfolio woldw\_{\mathrm{old}}, but still allows the prior to exert substantial influence.

To this end we introduce a scalar multiplier c>0c>0 and consider the
family

|  |  |  |
| --- | --- | --- |
|  | σΔ​w2​(c)=c​σΔ​w,base2,c∈𝒞0,\sigma^{2}\_{\Delta w}(c)\;=\;c\,\sigma^{2}\_{\Delta w,\mathrm{base}},\qquad c\in\mathcal{C}\_{0}, |  |

for a grid 𝒞0\mathcal{C}\_{0} of candidate values (e.g.,
𝒞0={1,20,50,…,200}\mathcal{C}\_{0}=\{1,20,50,\dots,200\}). For each cc the likelihood
in ([7.4](https://arxiv.org/html/2512.22109v1#S7.Ex93 "7.4 Rebalancing ‣ 7 A case study: tracking the S&P 500 ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification")) is scaled accordingly; in particular
increasing cc flattens the likelihood, which in turn gives SAPG more
freedom to drive the posterior towards sparser solutions.

We measure tracking performance on FIT–2 via the usual RMS tracking error (on the uncentred returns)

|  |  |  |
| --- | --- | --- |
|  | TEFIT2​(w)=(1T​∑t∈FIT–2(yt−(Rt​w))2)1/2,\mathrm{TE}\_{\mathrm{FIT2}}(w)\;=\;\biggl(\frac{1}{T}\sum\_{t\in\text{FIT--2}}\bigl(y\_{t}-(R\_{t}w)\bigr)^{2}\biggr)^{1/2}, |  |

and we denote by TEold\mathrm{TE}\_{\mathrm{old}} the TE of
woldw\_{\mathrm{old}} on FIT–2. This quantity is used to anchor the acceptable range of TE for the rebalanced portfolio.

##### Empirical Bayes learning of κ​(c)\kappa(c) via SAPG.

For each candidate c∈𝒞c\in\mathcal{C} we treat σΔ​w2​(c)\sigma^{2}\_{\Delta w}(c)
as fixed, and we estimate κ⋆​(c)\kappa\_{\star}(c) by SAPG on the smoothed posterior π​(Δ​w∣c,κ)\pi(\Delta w\mid c,\kappa)
associated with ([7.4](https://arxiv.org/html/2512.22109v1#S7.Ex93 "7.4 Rebalancing ‣ 7 A case study: tracking the S&P 500 ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification")). Of course, we can only do this because of how fast SAPG and FISTA are; in our experiments, we computed 10 pairs of (κ(c),ΔwM​A​P(κ(c))(\kappa(c),\Delta w\_{MAP}(\kappa(c)) in less than two minutes. Writing
η=log⁡κ\eta=\log\kappa, the SAPG update has the generic form

|  |  |  |
| --- | --- | --- |
|  | ηk+1=Π[log⁡κmin,log⁡κmax]​(ηk+ρk​Δ​gk),\eta\_{k+1}\;=\;\Pi\_{[\log\kappa\_{\min},\,\log\kappa\_{\max}]}\Bigl(\eta\_{k}+\rho\_{k}\,\Delta g\_{k}\Bigr), |  |

where, as in FIT–1, ρk=cSAPG/(k+k0)\rho\_{k}=c\_{\mathrm{SAPG}}/(k+k\_{0}) is a decaying step size
and Δ​gk\Delta g\_{k} is a noisy estimate of the derivative of the
log–marginal likelihood with respect η\eta. In our implementation, the inner kernel is a MYULA–type chain on
Δ​w\Delta w targeting the smoothed posterior, and at iteration kk we
compute

|  |  |  |
| --- | --- | --- |
|  | uk=proxλMY​g​(Δ​wk),Sk=∑j=1pαjΔ​|uk,j|,u\_{k}\;=\;\mathrm{prox}\_{\lambda\_{\mathrm{MY}}g}(\Delta w\_{k}),\qquad S\_{k}\;=\;\sum\_{j=1}^{p}\alpha^{\Delta}\_{j}|u\_{k,j}|, |  |

from which a simple moment condition suggests the update direction
Δ​gk≈d−κk​Sk\Delta g\_{k}\approx d-\kappa\_{k}S\_{k}, with d=p−1d=p-1 the dimension
of the sum–zero hyperplane (as explained in the Appendix). Polyak–Ruppert averaging of the ηk\eta\_{k}
sequence over the tail of the run yields an empirical–Bayes estimate
κ⋆​(c)\kappa\_{\star}(c) for that particular noise scale c.c.

##### MAP estimation and effective sparsity.

Once κ⋆​(c)\kappa\_{\star}(c) has been learned, we fix the pair
(σΔ​w2​(c),κ⋆​(c))(\sigma^{2}\_{\Delta w}(c),\kappa\_{\star}(c)) and compute the
smoothed MAP

|  |  |  |
| --- | --- | --- |
|  | Δ​wMAP​(c)=arg⁡minΔ​w∈ℝp⁡Φ​(Δ​w;κ⋆​(c),σΔ​w2​(c)),\Delta w\_{\mathrm{MAP}}(c)\;=\;\arg\min\_{\Delta w\in\mathbb{R}^{p}}\Phi\bigl(\Delta w;\,\kappa\_{\star}(c),\sigma^{2}\_{\Delta w}(c)\bigr), |  |

using a FISTA scheme on ([7.4](https://arxiv.org/html/2512.22109v1#S7.Ex93 "7.4 Rebalancing ‣ 7 A case study: tracking the S&P 500 ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification")) with the
budget–constrained proximal map
proxλMY​g\mathrm{prox}\_{\lambda\_{\mathrm{MY}}g}.

The rebalanced portfolio
is then
wnew​(c)=wold+Δ​wMAP​(c)w\_{\mathrm{new}}(c)=w\_{\mathrm{old}}+\Delta w\_{\mathrm{MAP}}(c),
automatically satisfying 𝟏⊤​wnew​(c)=1\mathbf{1}^{\top}w\_{\mathrm{new}}(c)=1.

Because the smoothed objective does not produce exact zeros, we define
an *effective* cardinality

|  |  |  |
| --- | --- | --- |
|  | nnzeff​(c)=#​{j∈{1,…,p}:|Δ​wMAPj​(c)|≥τeff},\mathrm{nnz}\_{\mathrm{eff}}(c)\;=\;\#\Bigl\{j\in\{1,\dots,p\}:\bigl|\Delta{w\_{\mathrm{MAP}}}\_{j}(c)\bigr|\geq\tau\_{\mathrm{eff}}\Bigr\}, |  |

where τeff>0\tau\_{\mathrm{eff}}>0 is a small fixed threshold chosen to
ignore numerically negligible weight adjustments. We also record the
raw cardinality
nnzraw​(c)=#​{j:Δ​wMAPj​(c)≠0}\mathrm{nnz}\_{\mathrm{raw}}(c)=\#\{j:\Delta{w\_{\mathrm{MAP}}}\_{j}(c)\neq 0\}
for diagnostic purposes, but all decisions are based on
nnzeff​(c)\mathrm{nnz}\_{\mathrm{eff}}(c).

##### A scalar decision metric over the cc–grid.

For each c∈𝒞0c\in\mathcal{C}\_{0} we evaluate both the TE
TEFIT2​(wnew​(c))\mathrm{TE}\_{\mathrm{FIT2}}(w\_{\mathrm{new}}(c)) and the effective
adjustment size nnzeff​(c)\mathrm{nnz}\_{\mathrm{eff}}(c). We then define a
simple scalar score

|  |  |  |
| --- | --- | --- |
|  | d​(c)=ϕTE​(c)​wnnz​(c),d(c)\;=\;\phi\_{\mathrm{TE}}(c)\,w\_{\mathrm{nnz}}(c), |  |

where:

* •

  We specify lower and upper fractions
  0<γlo<1<γhi0<\gamma\_{\mathrm{lo}}<1<\gamma\_{\mathrm{hi}} and set

  |  |  |  |
  | --- | --- | --- |
  |  | ϕTE​(c)={1,if ​γlo​TEold≤TEFIT2​(wreb​(c))≤γhi​TEold,0,otherwise.\phi\_{\mathrm{TE}}(c)\;=\;\begin{cases}1,&\text{if }\gamma\_{\mathrm{lo}}\,\mathrm{TE}\_{\mathrm{old}}\leq\mathrm{TE}\_{\mathrm{FIT2}}(w^{\mathrm{reb}}(c))\leq\gamma\_{\mathrm{hi}}\,\mathrm{TE}\_{\mathrm{old}},\\[2.5pt] 0,&\text{otherwise.}\end{cases} |  |

  In our experiments we use γlo=0.2\gamma\_{\mathrm{lo}}=0.2 and
  γhi=1.2\gamma\_{\mathrm{hi}}=1.2, reflecting the view that (i) TE values
  much smaller than 0.2​TEold0.2\,\mathrm{TE}\_{\mathrm{old}} are likely to
  correspond to overfitting on FIT–2, whereas (ii) TE values much larger than 1.2​TEold1.2\,\mathrm{TE}\_{\mathrm{old}} indicate ineffective
  tracking.
* •

  *Gaussian preference over effective cardinality.*
  Let nnzprev\mathrm{nnz}\_{\mathrm{prev}} denote the cardinality of the
  existing portfolio woldw^{\mathrm{old}}, and set a target adjustment
  size

  |  |  |  |
  | --- | --- | --- |
  |  | n⋆=γnnz​nnzprev,n\_{\star}\;=\;\gamma\_{\mathrm{nnz}}\,\mathrm{nnz}\_{\mathrm{prev}}, |  |

  with γnnz≈0.25\gamma\_{\mathrm{nnz}}\approx 0.25: we prefer to adjust only
  a moderate fraction of the currently held names. Given a scale
  parameter σnnz>0\sigma\_{\mathrm{nnz}}>0 (in units of “names”),
  we define

  |  |  |  |
  | --- | --- | --- |
  |  | wnnz​(c)=exp⁡(−12​(nnzeff​(c)−n⋆σnnz)2).w\_{\mathrm{nnz}}(c)\;=\;\exp\!\left(-\frac{1}{2}\left(\frac{\mathrm{nnz}\_{\mathrm{eff}}(c)-n\_{\star}}{\sigma\_{\mathrm{nnz}}}\right)^{2}\right). |  |

The score d​(c)d(c) is thus nonzero only for settings where the TE lies
in a plausible range, and among those, it favours configurations where
the effective number of adjusted names is neither too small nor too
large. To provide a sense of the scales involved, in the S&P 500 experiment of our Case Study, this procedure selects a value
c∗=60c^{\*}=60, with
TEFIT2​(wnew​(c∗))\mathrm{TE}\_{\mathrm{FIT2}}(w\_{\mathrm{new}}(c^{\*})) slightly lower than
TEold\mathrm{TE}\_{\mathrm{old}} and an effective adjustment size of
nnzeff​(c∗)=34\mathrm{nnz}\_{\mathrm{eff}}(c^{\*})=34 starting from
nnzold=155\mathrm{nnz}\_{\mathrm{old}}=155. The above is a crude example of a possible metric, that nevertheless captures well our intentions; refinements are of course possible.

##### Rebalancing parameters for UQ.

Once c∗c^{\*} has been selected on the grid, we lock in the corresponding
noise variance and sparsity level,

|  |  |  |
| --- | --- | --- |
|  | σΔ​w,final2=σΔ​w2​(c∗),κ⋆,final=κ⋆​(c∗),\sigma^{2}\_{\Delta w,\mathrm{final}}\;=\;\sigma^{2}\_{\Delta w}(c^{\*}),\qquad{\kappa\_{\star}}\_{,{\text{final}}}\;=\;\kappa\_{\star}(c^{\*}), |  |

together with the associated smoothed MAP rebalancing move
Δ​wMAP=Δ​wMAP​(c∗)\Delta w\_{\mathrm{MAP}}=\Delta w\_{\mathrm{MAP}}(c^{\*}) and
rebalanced portfolio wnew=wnew​(c∗)w\_{\mathrm{new}}=w\_{\mathrm{new}}(c^{\*}).
These now define a fixed target posterior for uncertainty quantification
on FIT–2. In particular, the subsequent preconditioned MALA sampler in
Section [6.2](https://arxiv.org/html/2512.22109v1#S6.SS2 "6.2 Long MALA run for rebalancing ‣ 6 Rebalancing ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification") will be constructed around
Φ​(Δ​w;κ⋆,final,σΔ​w,final2)\Phi\left(\Delta w;{\kappa\_{\star}}\_{,{\text{final}}},\sigma^{2}\_{\Delta w,\mathrm{final}}\right)
and initialised at Δ​wMAP\Delta w\_{\mathrm{MAP}}.

### 6.2 Long MALA run for rebalancing

We mirror the MALA construction for ww, now targeting the smoothed posterior for Δ​w\Delta w.

##### Preconditioner and smoothing.

We build a Jacobi preconditioner

|  |  |  |
| --- | --- | --- |
|  | Pj(Δ)=((R2,c⊤​R2,c)j​jσΔ​w2)−1/2,P^{(\Delta)}\_{j}=\left(\frac{(R\_{2,c}^{\top}R\_{2,c})\_{jj}}{\sigma^{2}\_{\Delta w}}\right)^{-1/2}, |  |

and estimate Lpre(Δ)≈λmax​(P(Δ)​(R2,c⊤​R2,c/σΔ​w2)​P(Δ))L^{(\Delta)}\_{\mathrm{pre}}\approx\lambda\_{\max}(P^{(\Delta)}(R\_{2,c}^{\top}R\_{2,c}/\sigma^{2}\_{\Delta w})P^{(\Delta)}). The MY smoothing and step–size are chosen as

|  |  |  |
| --- | --- | --- |
|  | λMY,pre(Δ)=1Lpre(Δ),δ(Δ)=0.92​Lpre(Δ)\lambda^{(\Delta)}\_{\mathrm{MY,pre}}=\frac{1}{L^{(\Delta)}\_{\mathrm{pre}}},\qquad\delta^{(\Delta)}=\frac{0.9}{2L^{(\Delta)}\_{\mathrm{pre}}} |  |

with small adaptive adjustments to target a MH acceptance rate around 0.600.60.

##### MALA kernel.

Let ΦΔ,λ\Phi\_{\Delta,\lambda} denote the smoothed potential, using the sum–zero constrained prox (the same as in the MAP step). The preconditioned MALA proposal for Δ​w\Delta w is

|  |  |  |
| --- | --- | --- |
|  | Δ​w′=Δ​w−δ(Δ)​(P(Δ))2​∇ΦΔ,λ​(Δ​w)+2​δ(Δ)​P(Δ)​ξ,ξ∼𝒩​(0,Ip),\Delta w^{\prime}=\Delta w-\delta^{(\Delta)}(P^{(\Delta)})^{2}\nabla\Phi\_{\Delta,\lambda}(\Delta w)+\sqrt{2\delta^{(\Delta)}}\,P^{(\Delta)}\xi,\quad\xi\sim\mathcal{N}(0,I\_{p}), |  |

with MH accept/reject. The chain is initialised at Δ​wMAP\Delta w\_{\mathrm{MAP}} and run for a long horizon; an initial number of draws is discarded as burn–in.

Post–burn we retain

|  |  |  |
| --- | --- | --- |
|  | {Δ​w(m)}m=1Mpost≡Wpost(Δ).\{\Delta w^{(m)}\}\_{m=1}^{M\_{\mathrm{post}}}\equiv W^{(\Delta)}\_{\mathrm{post}}. |  |

We assess mixing via coordinate–wise ESS and ACF for selected Δ​wj\Delta w\_{j}.

### 6.3 Posterior-informed rebalancing rules

The long MALA run on the smoothed Δ​w\Delta w posterior provides, for each coordinate j=1,…,pj=1,\dots,p, an empirical posterior standard deviation
sd^j\widehat{\mathrm{sd}}\_{j} and an activation probability

|  |  |  |
| --- | --- | --- |
|  | π^j=ℙ​(|Δ​wj|≥τpost|yFIT2),\hat{\pi}\_{j}\;=\;\mathbb{P}\bigl(|\Delta w\_{j}|\geq\tau\_{\mathrm{post}}\,\big|\,y\_{\text{FIT2}}\bigr), |  |

estimated from post-burn MCMC samples. Following the scale-based thresholding idea discussed earlier, we define a global posterior
scale threshold

|  |  |  |  |
| --- | --- | --- | --- |
|  | τpost=k⋅median​(sd^1,…,sd^p),k>0,\tau\_{\mathrm{post}}\;=\;k\cdot\mathrm{median}\bigl(\widehat{\mathrm{sd}}\_{1},\dots,\widehat{\mathrm{sd}}\_{p}\bigr),\qquad k>0, |  | (25) |

and use both τpost\tau\_{\mathrm{post}} and the activation probabilities
π^j\hat{\pi}\_{j} to gate which coordinates are eligible for rebalancing.

##### Scale and probability gates.

Let Δ​wMAP\Delta w\_{\mathrm{MAP}} denote the smoothed MAP solution for the
rebalancing model at the selected noise scale c∗c^{\ast}.
We define:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Sτ\displaystyle S\_{\tau} | ={j:|Δ​wMAPj|≥τpost},\displaystyle=\bigl\{j:|\Delta{w\_{\mathrm{MAP}}}\_{j}|\,\geq\,\tau\_{\mathrm{post}}\bigr\}, |  | (26) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Sπ​(π⋆)\displaystyle S\_{\pi}(\pi^{\star}) | ={j:π^j≥π⋆},\displaystyle=\bigl\{j:\hat{\pi}\_{j}\,\geq\,\pi^{\star}\bigr\}, |  | (27) |

where π⋆∈(0,1)\pi^{\star}\in(0,1) is a user–chosen activation probability
threshold. The intersection

|  |  |  |  |
| --- | --- | --- | --- |
|  | Srule​(π⋆)=Sτ∩Sπ​(π⋆)S\_{\mathrm{rule}}(\pi^{\star})\;=\;S\_{\tau}\,\cap\,S\_{\pi}(\pi^{\star}) |  | (28) |

collects those coordinates that are simultaneously “large” in the MAP
sense and frequently active under the posterior.

Finally, while negative entries in Δ​w\Delta w are meaningful, under the mandate of no-shorts, one also needs to impose that wn​e​w,j=wo​l​d,j+(Δ​wMAP)j≥0,w\_{new,j}=w\_{old,j}+(\Delta{w\_{\mathrm{MAP}}})\_{j}\geq 0, clipping to zero if not.

##### Implementable rebalancing within the active set.

Let SruleS\_{\mathrm{rule}} have cardinality m≥2m\geq 2 and define
𝒮=Srule\mathcal{S}=S\_{\mathrm{rule}} for brevity. We start from the
smoothed MAP increment Δ​wMAP\Delta w^{\mathrm{MAP}} and restrict it to the
active coordinates,

|  |  |  |
| --- | --- | --- |
|  | Δ​w~j={Δ​wMAPj,j∈𝒮,0,j∉𝒮,\tilde{\Delta w}\_{j}=\begin{cases}\Delta{w\_{\mathrm{MAP}}}\_{j},&j\in\mathcal{S},\\ 0,&j\notin\mathcal{S},\end{cases} |  |

so that only assets in 𝒮\mathcal{S} are eligible for adjustment.
Because the original MAP increment Δ​wMAP\Delta w\_{\mathrm{MAP}} satisfies
the budget constraint ∑jΔ​wMAPj=0\sum\_{j}\Delta{w\_{\mathrm{MAP}}}\_{j}=0 on the full
universe, the restricted vector Δ​w~\tilde{\Delta w} will in general have
a nonzero sum over 𝒮\mathcal{S}. To preserve the budget while
avoiding new nonzero positions (and consequently more trades and fees) outside 𝒮\mathcal{S} we apply (for example) a
simple recentering within the active set:

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ¯=1m​∑j∈𝒮Δ​w~j,Δ​wjimpl={Δ​w~j−δ¯,j∈𝒮,0,j∉𝒮.\bar{\delta}\;=\;\frac{1}{m}\sum\_{j\in\mathcal{S}}\tilde{\Delta w}\_{j},\qquad\Delta w^{\mathrm{impl}}\_{j}=\begin{cases}\tilde{\Delta w}\_{j}-\bar{\delta},&j\in\mathcal{S},\\[2.5pt] 0,&j\notin\mathcal{S}.\end{cases} |  | (29) |

By construction ∑jΔ​wjimpl=0\sum\_{j}\Delta w^{\mathrm{impl}}\_{j}=0 and the
support of Δ​wimpl\Delta w^{\mathrm{impl}} is exactly 𝒮\mathcal{S}. The new
portfolio used for reporting and out–of–sample testing is then

|  |  |  |  |
| --- | --- | --- | --- |
|  | wnew=wold+Δ​wimpl.w\_{\mathrm{new}}\;=\;w\_{\mathrm{old}}+\Delta w^{\mathrm{impl}}. |  | (30) |

This rule ensures that rebalancing decisions are driven jointly by the
MAP magnitude and the posterior activation probabilities, and that the
resulting trades remain sparse and interpretable: only a small set of assets is modified, and the budget constraint is enforced by a local
correction within that set, rather than by a global projection that
would introduce many tiny, nonzero positions.

## 7 A case study: tracking the S&P 500

### 7.1 Data

We obtained freely available data from *Yahoo Finance* from *January 1st 2017 to January 1st 2020*, a recent, not-too-turbulent window. The data are in the form of daily adjusted closing prices for the constituent assets of the S&P 500, and the index itself. Our experiments intentionally restrict attention to a fixed universe of assets (478) that survive the entire study horizon. This design isolates the methodological contributions from confounds due to changing constituent sets. A consequence is *survivorship bias*: the sample excludes delisted or newly listed names. In practice, this may understate real-world turnover and TE when reconstitutions occur. We make two mitigations explicit: (i) we use fixed-length (500 trading days) rolling fit windows and fixed hold periods (125 days) so that all estimates are *out-of-sample* relative to the subsequent hold; and (ii) we report implementability proxies (turnover, active names) alongside TE. Extending the pipeline to live universes with entry/exit events is feasible (rebuild the design matrix RR each window and carry inherited positions through reconstitution dates), but is outside our proof-of-concept scope.

All experiments were conducted on a MacBook Air (Apple M1 Chip: 8-core CPU), running Python 3.12.

### 7.2 Creating a tradeable portfolio

### FIT and HOLD windows

We split our data into three fitting and two holding periods, with some overlaps as outlined and shown schematically below:

* •

  FIT–1 period: *2017-01-03 to 2018-12-31*, 500 trading days, that is used for the design of the first tradeable portfolio.
* •

  HOLD–1 period: *2019-01-02 to 2019-06-28*, 128 trading days, when the above portfolio is held out-of-sample for the first time immediately following its design. Upon evaluation at the end of this period, we focus on rebalancing, working with data in the
* •

  FIT–2 period: *2017-07-03 to 2019-06-28*, 500 trading days, ending on the last HOLD–1 day. We rebalance the first portfolio and hold it throughout the out-of-sample
* •

  HOLD–2 period: *2019-07-01 to 2019-12-31*, 124 days. Again, upon evaluation, we use one last fitting period,
* •

  FIT–3 period: *2018-01-04 to 2019-12-31*, 500 trading days, ending on the last HOLD–2 day.

calendar time2017201820192020FIT–1FIT–2FIT–3HOLD–1HOLD–2FIT window (in-sampleHOLD window (out-of-sample evaluation)


Figure 1: Timeline of fitting (FIT) and holding (HOLD) periods used in the empirical study.

### Model setup on FIT–1

We use a rolling window of length T=500T=500 for all the FIT periods. The same 478 assets (all are S&P 500 constituents for the full 2017-2020 period) are considered.

We first centre both the index and the regressors returns on FIT–1. Moreover, we incorporate the budget constraint through a Gaussian pseudo-observation term. The corresponding log-likelihood is

|  |  |  |
| --- | --- | --- |
|  | fy​(w)=12​σ2​‖yc−Rc​w‖22+Λ​(𝟏⊤​w−1)2,f\_{y}(w)\;=\;\frac{1}{2\sigma^{2}}\,\|y\_{c}-R\_{c}w\|\_{2}^{2}\;+\;\Lambda\bigl(\mathbf{1}^{\top}w-1\bigr)^{2}, |  |

where Λ=12​τc2.\Lambda\;=\;\frac{1}{2\tau\_{c}^{2}}. The parameter τc\tau\_{c} is a fixed, user-defined allowed deviation from the hard constraint, and the first of only two parameters a user would have to input for FIT–1 (the other being π∗\pi^{\ast} at the final selection stage).

Here we set τc=2⋅10−3,\tau\_{c}=2\cdot 10^{-3}, which in turn yields Λ=1.25⋅105.\Lambda=1.25\cdot 10^{5}.

Next, we calculate the MAD estimator for the noise variance as described in Section [C](https://arxiv.org/html/2512.22109v1#A3 "Appendix C Noise variance estimation ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification"). For this window we calculated σ^2=3.26⋅10−9.\hat{\sigma}^{2}=3.26\cdot 10^{-9}.

For the prior, following the discussion from Section [2.2](https://arxiv.org/html/2512.22109v1#S2.SS2 "2.2 Sparsity-inducing prior ‣ 2 Model considerations ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification"),
we calculate per–asset scaling factors for the weighted ℓ1\ell\_{1} penalty; pp is the number of assets, here p=478.p=478. We set

|  |  |  |  |
| --- | --- | --- | --- |
|  | sj=‖Rc,⋅j‖2T,αj=max⁡{sj,ε}1p​∑k=1pmax⁡{sk,ε},s\_{j}\;=\;\frac{\big\|R\_{c,\cdot j}\big\|\_{2}}{\sqrt{T}},\qquad\alpha\_{j}\;=\;\frac{\max\{s\_{j},\varepsilon\}}{\frac{1}{p}\displaystyle\sum\_{k=1}^{p}\max\{s\_{k},\varepsilon\}}, |  | (31) |

(by default, ε=10−8\varepsilon=10^{-8}). We recorded the minimal, maximal, and mean weights as 0.51,3.492,10.51,3.492,1 respectively.

### SAPG to select θ⋆\theta\_{\star}

We have seen that for stability, the MYULA timestep is selected to satisfy it

|  |  |  |
| --- | --- | --- |
|  | δMYULA=0.92​Lf,\delta\_{\mathrm{MYULA}}=\frac{0.9}{2L\_{f}}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | Lf=1σ^2​λmax​(Rc⊤​Rc+2​Λ​𝟏𝟏⊤).L\_{f}=\frac{1}{\hat{\sigma}^{2}}\,\lambda\_{\max}(R\_{c}^{\top}R\_{c}+2\Lambda\mathbf{1}\mathbf{1}^{\top}). |  |

We estimate the maximal eigenvalue of Rc⊤​Rc+2​Λ​𝟏𝟏⊤R\_{c}^{\top}R\_{c}+2\Lambda\mathbf{1}\mathbf{1}^{\top} (with the Λ\Lambda found earlier) using the power method, and with the previously computed value for σ^2\hat{\sigma}^{2}, we find

|  |  |  |
| --- | --- | --- |
|  | Lf=5.044⋅109,λM​Y=1.982⋅10−10,δM​Y​U​L​A=8.921⋅10−11.L\_{f}=5.044\cdot 10^{9},\qquad\lambda\_{MY}=1.982\cdot 10^{-10},\qquad\delta\_{MYULA}=8.921\cdot 10^{-11}. |  |

Before SAPG, we warmstart the MYULA chain with a fixed value θ0\theta\_{0}, whose selection we explain in Appendix [A.1](https://arxiv.org/html/2512.22109v1#A1.SS1 "A.1 Heuristic choice of the initial scale 𝜃₀ ‣ Appendix A Stochastic Approximation Proximal Gradient algorithm (SAPG) ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification"). Based on the value of θ0,\theta\_{0}, we also define the admissibility set Θ=[θ0/10,10​θ0]\Theta=[\theta\_{0}/10,10\,\theta\_{0}]. We find θ0=198.7,\theta\_{0}=198.7, and then set Θ=[19.87,1987].\Theta=[19.87,1987]. We plot the trace of the log-posterior (up to a constant) as an indication of stationarity in Fig. [2](https://arxiv.org/html/2512.22109v1#S7.F2 "Figure 2 ‣ SAPG to select 𝜃_⋆ ‣ 7 A case study: tracking the S&P 500 ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification"). It stabilises very quickly, evidence that we are indeed working with a stable timestep.

We are now ready to run SAPG using iteration ([12](https://arxiv.org/html/2512.22109v1#S3.E12 "Equation 12 ‣ SAPG update for 𝜃. ‣ 3.3 Empirical-Bayes calibration of the sparsity parameter ‣ 3 Proximal MCMC for the posterior ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification")), in logarithmic coordinates. The projection on Θ\Theta is implemented by a simple “clipping” should an iterate exceed its bounds.

We ran 20000 iterations, of which the first 4000 were discarded as burn-in. For the SAPG timestep ρk\rho\_{k} we used c=1c=1, k0=200k\_{0}=200. Based on the kept samples, we compute a Polyak-Ruppert weighted average as in ([13](https://arxiv.org/html/2512.22109v1#S3.E13 "Equation 13 ‣ SAPG update for 𝜃. ‣ 3.3 Empirical-Bayes calibration of the sparsity parameter ‣ 3 Proximal MCMC for the posterior ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification")) using q=1.q=1. The output of this process is what we report as θ⋆,\theta\_{\star}, which in this case assumed the value 391.1.391.1. The graph below captures the evolution of θ\theta; after an initial jump, it stabilises very quickly, Fig. [3](https://arxiv.org/html/2512.22109v1#S7.F3 "Figure 3 ‣ SAPG to select 𝜃_⋆ ‣ 7 A case study: tracking the S&P 500 ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification").

![[Uncaptioned image]](myula_logpost_warmup.png)



Figure 2: MYULA warm-up with θ0\theta\_{0}.

![[Uncaptioned image]](sapg_theta_trace.png)



Figure 3: SAPG evolution of θ\theta.

We note that the above (solving for θ0\theta\_{0}, warm-starting the chain with θ0\theta\_{0} and SAPG) combined took 8 seconds to run.

### FISTA for MAP

With (σ^2,Λ,θ⋆)(\hat{\sigma}^{2},\Lambda,\theta\_{\star}) set as above, we compute the full–support maximum a posteriori (MAP) estimator

|  |  |  |
| --- | --- | --- |
|  | w^MAP∈arg⁡minw∈ℝp⁡12​σ^2​‖yc−Rc​w‖2+Λ​(1p⊤​w−1)2+θ⋆​[∑jαj​|wj|].\hat{w}\_{\mathrm{MAP}}\in\arg\min\_{w\in\mathbb{R}^{p}}\frac{1}{2\hat{\sigma}^{2}}\|y\_{c}-R\_{c}w\|^{2}+\Lambda(1\_{p}^{\top}w-1)^{2}\;+\;\theta\_{\star}\Big[\sum\_{j}\alpha\_{j}|w\_{j}|\Big]. |  |

We solve this convex problem with FISTA: the smooth part (data fit and budget constraint) is handled in the gradient step; the ℓ1\ell\_{1} uses a weighted soft-thresholding proximal operator. The time-step is chosen to be 1/Lf.1/L\_{f}.

Writing gθ⋆​(w)=θ⋆​∑jαj​|wj|g\_{\theta\_{\star}}(w)=\theta\_{\star}\sum\_{j}\alpha\_{j}|w\_{j}|, the FISTA iteration is

|  |  |  |  |
| --- | --- | --- | --- |
|  | w(k+1)\displaystyle w^{(k+1)} | =prox1Lf​gθ⋆⁡(z(k)−1Lf​∇fy​(z(k))),\displaystyle=\operatorname{prox}\_{\frac{1}{L\_{f}}g\_{\theta\_{\star}}}\!\Bigl(z^{(k)}-\tfrac{1}{L\_{f}}\nabla f\_{y}(z^{(k)})\Bigr), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | tk+1\displaystyle t\_{k+1} | =1+1+4​tk22,\displaystyle=\frac{1+\sqrt{1+4t\_{k}^{2}}}{2}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | z(k+1)\displaystyle z^{(k+1)} | =w(k+1)+tk−1tk+1​(w(k+1)−w(k)),\displaystyle=w^{(k+1)}+\frac{t\_{k}-1}{t\_{k+1}}\bigl(w^{(k+1)}-w^{(k)}\bigr), |  |

starting from w(0)=0w^{(0)}=0, z(0)=0z^{(0)}=0, t0=1t\_{0}=1, and stopping when the objective difference falls below a relative tolerance threshold.

![Refer to caption](FISTA_for_MAP_iterations.png)


Figure 4: Trace: FISTA iterations for MAP. Stopped after 1385 iterations, which took less than 1 sec.

For reference, the unprocessed MAP recorded an in-sample TE of 7.1754​𝐞−𝟎𝟓.{\bf 7.1754e-05}. As seen in the histograms below, most of the weights are very small, but only 454/478 of its weights are nonzero. About 30% (139) of the MAP entries are negative.

![[Uncaptioned image]](hist_MAP.png)



Figure 5: Histogram of the MAP

![[Uncaptioned image]](w_hist_abs.png)



Figure 6: Visualising the sizes of the MAP weights.

### The long MALA run (with preconditioning)

Note that one can first run MALA and then solve for the MAP (or at the same time, although FISTA takes a few seconds (at most) and MALA takes about 10 minutes because of the MH step). We opted for this order because it is convenient to initialise MALA (at the burn-in stage) from the MAP.

### Tuning timestep for acceptance ratio

We first tune the stepsize δ\delta to target an acceptance rate in the 0.550.55–0.650.65 band, using a sequence of short, fixed-length pilot runs. For MALA, in many regimes, the asymptotically optimal acceptance rate is known to be ≈0.574\approx 0.574.

Starting from an initial guess

|  |  |  |
| --- | --- | --- |
|  | δ0=0.90Lpre+1/λMY,pre,\delta\_{0}\;=\;\frac{0.90}{L\_{\mathrm{pre}}+1/\lambda\_{\mathrm{MY,pre}}}\!, |  |

based on the preconditioned Lipschitz constant LpreL\_{\mathrm{pre}} and the MY smoothing parameter λMY,pre\lambda\_{\mathrm{MY,pre}}, we iterate the following scheme:

1. 1.

   Run a short MALA chain (e.g. 10001000 proposals) at the current step size δ\delta.
2. 2.

   Compute the empirical acceptance rate a^​(δ)\hat{a}(\delta).
3. 3.

   Update δ\delta multiplicatively according to

   |  |  |  |
   | --- | --- | --- |
   |  | δ←{1.25​δ,if ​a^​(δ)>target+0.05,0.50​δ,if ​a^​(δ)<target−0.10,δ,otherwise,\delta\leftarrow\begin{cases}1.25\,\delta,&\text{if }\hat{a}(\delta)>\text{target}+0.05,\\[3.00003pt] 0.50\,\delta,&\text{if }\hat{a}(\delta)<\text{target}-0.10,\\[3.00003pt] \delta,&\text{otherwise},\end{cases} |  |

   where target=0.60\text{target}=0.60 in our experiments.

If the acceptance rate falls within the band [target−0.10,target+0.05][\text{target}-0.10,\text{target}+0.05]
(approximately [0.50,0.65][0.50,0.65] with the current thresholds), we stop and take the
current value as the tuned step size δ⋆\delta\_{\star}. Importantly, this adaptation is performed only in a preliminary tuning phase. The final long MALA run for inference is then conducted with a fixed step size
δ⋆\delta\_{\star}, so the production chain is time-homogeneous and standard MCMC theory applies to the resulting samples.

We summarise the tuning step below

|  |  |  |
| --- | --- | --- |
|  | TimestepAcc. Rate1.465​e−020.931.832​e−020.912.290​e−020.882.862​e−020.823.578​e−020.764.472​e−020.675.590​𝐞−𝟎𝟐0.56\begin{array}[]{r r}\hline\cr\hline\cr\text{\bf Timestep}&\text{\bf Acc. Rate}\\ \hline\cr\hline\cr 1.465e-02&0.93\\ \hline\cr 1.832e-02&0.91\\ \hline\cr 2.290e-02&0.88\\ \hline\cr 2.862e-02&0.82\\ \hline\cr 3.578e-02&0.76\\ \hline\cr 4.472e-02&0.67\\ \hline\cr{\bf 5.590e-02}&0.56\\ \hline\cr\hline\cr\end{array} |  |

### Effective sample size diagnostics

We monitor mixing of the MALA chains both on a function of direct interest
(the tracking error, TE) and on a set of portfolio weights.
Diagnostic summaries are based on effective sample sizes (ESS), computed from
empirical autocorrelation functions.

### ESS for a scalar Markov chain

Let x(1),…,x(M)x^{(1)},\dots,x^{(M)} denote a scalar time series extracted from the
kept MCMC draws after thinning (for example, a single portfolio weight at
successive iterations, or the TE evaluated at each draw). Denote by
r^k\widehat{r}\_{k} the empirical autocorrelation at lag kk:

|  |  |  |
| --- | --- | --- |
|  | r^k=∑m=1M−k(x(m)−x¯)​(x(m+k)−x¯)∑m=1M(x(m)−x¯)2,x¯=1M​∑m=1Mx(m).\widehat{r}\_{k}\;=\;\frac{\sum\_{m=1}^{M-k}(x^{(m)}-\bar{x})(x^{(m+k)}-\bar{x})}{\sum\_{m=1}^{M}(x^{(m)}-\bar{x})^{2}},\qquad\bar{x}=\frac{1}{M}\sum\_{m=1}^{M}x^{(m)}. |  |

We estimate the integrated autocorrelation time by

|  |  |  |
| --- | --- | --- |
|  | τ= 1+2​∑k=1Kr^k,\tau\;=\;1+2\sum\_{k=1}^{K}\widehat{r}\_{k}, |  |

where we truncate the sum at the first non-positive autocorrelation,

|  |  |  |
| --- | --- | --- |
|  | K=min⁡{k≥1:r^k<0},K=\min\{k\geq 1:\widehat{r}\_{k}<0\}, |  |

or at a fixed maximum lag if no sign change is observed. The effective sample
size for the series is then defined as

|  |  |  |
| --- | --- | --- |
|  | ESS​(x)=Mτ.\mathrm{ESS}(x)\;=\;\frac{M}{\tau}. |  |

### ESS for the tracking error, ESS​(TE)\mathrm{ESS}(\mathrm{TE})

Let w(m)∈ℝpw^{(m)}\in\mathbb{R}^{p} denote the portfolio weights at the mm-th kept
draw from the chain, and let yrawy\_{\mathrm{raw}} and RrawR\_{\mathrm{raw}} denote
the raw (uncentred) index and asset returns on the fit window, with centering
statistics (yμ,Rμ)(y\_{\mu},R\_{\mu}). For each draw mm we compute a tracking error

|  |  |  |
| --- | --- | --- |
|  | TE(m)=TE​(yraw,Rraw,w(m),yμ,Rμ)=1T​∑t=1T(yt−y^t​(w(m)))2,\mathrm{TE}^{(m)}\;=\;\mathrm{TE}\!\left(y\_{\mathrm{raw}},R\_{\mathrm{raw}},w^{(m)},y\_{\mu},R\_{\mu}\right)\;=\;\sqrt{\frac{1}{T}\sum\_{t=1}^{T}\bigl(y\_{t}-\hat{y}\_{t}(w^{(m)})\bigr)^{2}}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | y^t​(w)=(Rraw,t⁣⋅−Rμ)​w+yμ\hat{y}\_{t}(w)\;=\;\bigl(R\_{\mathrm{raw},t\cdot}-R\_{\mu}\bigr)w+y\_{\mu} |  |

is the portfolio return implied by ww at time tt.

We then compute

|  |  |  |
| --- | --- | --- |
|  | ESS​(TE)=ESS​(TE(1),…,TE(M))\mathrm{ESS}(\mathrm{TE})\;=\;\mathrm{ESS}\!\bigl(\mathrm{TE}^{(1)},\dots,\mathrm{TE}^{(M)}\bigr) |  |

using the generic scalar ESS logic above. This quantity measures how many
*independent* draws from the posterior would provide the same amount of
Monte Carlo information about the TE as the correlated MALA chain delivers.

A closely related quantity, useful for interpretation, is the Monte Carlo
standard error of the posterior mean tracking error

|  |  |  |
| --- | --- | --- |
|  | TE¯=1M​∑m=1MTE(m).\bar{\mathrm{TE}}=\frac{1}{M}\sum\_{m=1}^{M}\mathrm{TE}^{(m)}. |  |

If sd^​(TE)\widehat{\mathrm{sd}}(\mathrm{TE}) is the empirical standard deviation of
the TE(m)\mathrm{TE}^{(m)} samples, then

|  |  |  |
| --- | --- | --- |
|  | MCSE​(TE¯)≈sd^​(TE)ESS​(TE).\mathrm{MCSE}(\bar{\mathrm{TE}})\;\approx\;\frac{\widehat{\mathrm{sd}}(\mathrm{TE})}{\sqrt{\mathrm{ESS}(\mathrm{TE})}}. |  |

A large ESS​(TE)\mathrm{ESS}(\mathrm{TE}) therefore translates directly into a
small Monte Carlo uncertainty on the TE summary that is used for reporting
and for comparing different chains or different priors.

### ESS for coordinates and ESSmin​(S)\mathrm{ESS}\_{\min}(S)

In addition to TE, we monitor mixing on a subset of portfolio weights that
are most relevant for sparsity and rebalancing decisions. Let wMAPw\_{\mathrm{MAP}}
denote the MAP weights under the chosen prior, and define a sentinel index set
SS by selecting the |S||S| largest coordinates in magnitude,

|  |  |  |
| --- | --- | --- |
|  | S={j:j among the top |S| indices by ​|wMAP,j|}.S=\left\{j:\text{$j$ among the top $|S|$ indices by }|w\_{\mathrm{MAP},j}|\right\}. |  |

For each j∈Sj\in S we consider the scalar series

|  |  |  |
| --- | --- | --- |
|  | wj(1),…,wj(M),w\_{j}^{(1)},\dots,w\_{j}^{(M)}, |  |

and compute an effective sample size

|  |  |  |
| --- | --- | --- |
|  | ESSj=ESS​(wj(1),…,wj(M)).\mathrm{ESS}\_{j}\;=\;\mathrm{ESS}\!\bigl(w\_{j}^{(1)},\dots,w\_{j}^{(M)}\bigr). |  |

As a conservative scalar summary of mixing on these active coordinates, we
report the minimum effective sample size

|  |  |  |
| --- | --- | --- |
|  | ESSmin​(S)=minj∈S⁡ESSj.\mathrm{ESS}\_{\min}(S)\;=\;\min\_{j\in S}\mathrm{ESS}\_{j}. |  |

We summarise the run with the following tables

|  |  |  |
| --- | --- | --- |
|  | SamplesBurn-inESS​(TE)ESSmin​(S)sd​(TE)MCSE​(TE¯)Run durationAcceptance25000020000837.1624.71.3943​e−064.8190​e−081033.4​s0.57\begin{array}[]{rrrrrrrr}\hline\cr\hline\cr\text{Samples}&\text{Burn-in}&\mathrm{ESS}(\mathrm{TE})&\mathrm{ESS}\_{\min}(S)&\mathrm{sd}(\mathrm{TE})&\mathrm{MCSE}(\bar{\mathrm{TE}})&\text{Run duration}&\text{Acceptance}\\ \hline\cr 250000&20000&837.1&624.7&1.3943e-06&4.8190e-08&1033.4s&0.57\\ \hline\cr\hline\cr\end{array} |  |

Here MCSE​(TE¯)\mathrm{MCSE}(\bar{\mathrm{TE}}) is computed as described above.

We also record the ESS for certain coordinates

|  |  |  |
| --- | --- | --- |
|  | Coordinate Index154107160213266319372425478E​S​S628.1639.3632.8628.9628.1629.9631.8632.6668.7632.4\begin{array}[]{lrrrrrrrrrr}\hline\cr\hline\cr\text{Coordinate Index}&1&54&107&160&213&266&319&372&425&478\\ \hline\cr ESS&628.1&639.3&632.8&628.9&628.1&629.9&631.8&632.6&668.7&632.4\\ \hline\cr\hline\cr\end{array} |  |

### Posterior-informed support selection and the tradeable portfolio

We have solved for the MAP and have collected the samples from a long MALA run. We can proceed now with constructing candidate portfolios. We look at their sparsity levels, and also report experiments by looking at the effect of changing the parameters τp​o​s​t\tau\_{post} and π∗.\pi^{\ast}.

In this experiment, we will start from the support determined by the MAP as obtained from FISTA, i.e.,

|  |  |  |
| --- | --- | --- |
|  | S′:={i∈{1,…,p}:wj≠0}.S^{\prime}:=\{i\in\{1,\dots,p\}:w\_{j}\neq 0\}. |  |

We assess the effect of our gating rules on the support, applying one rule at a time. Based on this thresholding, we declare the weight of certain assets to be zero, and form the new support, which we generically refer to as SS. Finally, we impose the non-negativity condition For every such support, we form three portfolios (as described in Section [5.4](https://arxiv.org/html/2512.22109v1#S5.SS4 "5.4 Posterior-informed support selection and the tradeable portfolio ‣ 5 Construction of a tradeable portfolio ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification")) on the new support, and then compare their in-sample TE.

One caveat for the reporting below is that the D​E​B​I​A​SDEBIAS portfolio is not completely “honest” (hence the ∗\ast attached to it in the tables). By that we mean, that we debiased on the long-only support but didn’t enforce the non-negativity constraint in the optimisation and this gave five negative entries (though, none of them in the top-25 entries). We kept it here for comparison only. In contrast, the refit-on-S with FISTA was checked before enforcing non-negativity in the FISTA solve and it had produced four negative-entries (also not in the top-25). Once the constraint has been incorporated into FISTA, all entries are non-negative.

1. (a)

   We vary kk in the posterior scale threshold, τp​o​s​t​(k)=k⋅medianjs^j,\tau\_{post}(k)=k\cdot\operatorname\*{median}\_{j}\hat{s}\_{j},
   based on the MALA estimates of the, per-coordinate, posterior standard deviations

   |  |  |  |
   | --- | --- | --- |
   |  | s^j=sd⁡(wj(m)),j=1,…,p.\hat{s}\_{j}=\operatorname{sd}\bigl(w^{(m)}\_{j}\bigr),\qquad j=1,\dots,p. |  |

   The choice of our default kk is not unique, merely pragmatic. If the posterior for each wjw\_{j} were roughly Gaussian, then the
   condition

   |  |  |  |
   | --- | --- | --- |
   |  | |wj|≳k⋅sd^j|w\_{j}|\;\gtrsim\;k\cdot\widehat{\mathrm{sd}}\_{j} |  |

   is akin to demanding a |z||z|-score of about kk:

   * •

     k=2k=2 corresponds roughly to the familiar “95%95\%-ish” significance threshold; on the other hand,
   * •

     k=3k=3 corresponds to a very exacting “3​σ3\sigma” rule.

   The results are reported in Table [1](https://arxiv.org/html/2512.22109v1#S7.T1 "Table 1 ‣ Item (a) ‣ Posterior-informed support selection and the tradeable portfolio ‣ 7 A case study: tracking the S&P 500 ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification") below

   | kk | |S||S| | massk​e​p​t\text{mass}\_{kept} | TEp​r​u​n​e​d\text{TE}\_{pruned} | TEd​e​b​i​a​s∗\text{TE}\_{debias}^{\ast} | TEF​I​S​T​A\text{TE}\_{FISTA} |
   | --- | --- | --- | --- | --- | --- |
   | 2.00 | 176 | 0.709 | 8.960e-04 | 2.392e-04 | 2.423e-04 |
   | 2.25 | 166 | 0.693 | 7.406e-04 | 2.583e-04 | 2.612e-04 |
   | 2.50 | 155 | 0.674 | 6.039e-04 | 2.792e-04 | 2.809e-04 |
   | 3.00 | 130 | 0.628 | 5.714e-04 | 3.308e-04 | 3.322e-04 |

   Table 1: We vary kk to change the posterior scale threshold τp​o​s​t=k⋅medianjs^j\tau\_{post}=k\cdot\operatorname\*{median}\_{j}\hat{s}\_{j}.

   The “mass kept” by SS in the MAP tail is reported as

   |  |  |  |
   | --- | --- | --- |
   |  | mass kept=∑j∈S|wMAP,j|∑j=1p|wMAP,j|.\text{mass kept}=\frac{\sum\_{j\in S}|w\_{\mathrm{MAP},j}|}{\sum\_{j=1}^{p}|w\_{\mathrm{MAP},j}|}. |  |
2. (b)

   We fix k=2.5k=2.5 for τp​o​s​t,\tau\_{post}, and then vary the “activation probabilities” π∗\pi^{\ast}. We report the results in Table [2](https://arxiv.org/html/2512.22109v1#S7.T2 "Table 2 ‣ Item (b) ‣ Posterior-informed support selection and the tradeable portfolio ‣ 7 A case study: tracking the S&P 500 ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification").

   | π∗\pi^{\ast} | |S||S| | massk​e​p​t\text{mass}\_{kept} | TEp​r​u​n​e​d\text{TE}\_{pruned} | TEd​e​b​i​a​s∗\text{TE}\_{debias}^{\ast} | TEF​I​S​T​A\text{TE}\_{FISTA} |
   | --- | --- | --- | --- | --- | --- |
   | 0.50 | 159 | 0.683 | 6.541e-04 | 2.704e-04 | 2.722e-04 |
   | 0.60 | 157 | 0.679 | 6.341e-04 | 2.774e-04 | 2.790e-04 |
   | 0.65 | 155 | 0.674 | 6.039e-04 | 2.792e-04 | 2.809e-04 |
   | 0.70 | 149 | 0.663 | 5.394e-04 | 2.943e-04 | 2.953e-04 |
   | 0.75 | 146 | 0.656 | 5.164e-04 | 3.007e-04 | 3.014e-04 |
   | 0.80 | 144 | 0.652 | 5.154e-04 | 3.033e-04 | 3.042e-04 |

   Table 2: Changing the active set by varying π∗\pi^{\ast} and measuring TE of the portfolios.

From the above tables, we see that the moderate choices (k,π∗)=(2.5,0.65)(k,\pi^{\ast})=(2.5,0.65) (the framed row) give a good balance between sparsity and TE. Of course, the decision to use these values should not be seen as “optimised”, this is merely for a proof of concept demonstration. It is clear, though, that we can’t expect to squeeze more sparsity through π∗\pi^{\ast}, and trying to do so through a higher value of kk is likely to negatively affect TE, and more seriously, lead to overfitting.

We summarise the results in the following table

| Parameters and results (FIT–1 window) | |
| --- | --- |
| |S||S| | 155 |
| #​wMAP<0\#w\_{\text{MAP}}<0 | 139 |
| #​n​n​z​wMAP\#\;nnz\,w\_{\text{MAP}} | 454 |
| T​EMAP{TE}\_{\text{MAP}} | 7.156e-05 |
| T​EPRUNED{TE}\_{\text{PRUNED}} | 6.039e-04 |
| T​EDEBIAS∗{TE}\_{\text{DEBIAS}^{\ast}} | 2.792e-04 |
| T​EFISTA{TE}\_{\text{FISTA}} | 2.809e-04 |

Table 3: Summary of the long-only active set SS and tracking-error diagnostics on the fit window.

We also calculate the sum of the weights after the estimation of the MAP. Recall that we have enforced the budget constraint in a soft way, happy to compromise for an error of the order of 10−310^{-3} (set through τc\tau\_{c}); For the MAP itself, the sum of weights is 0.9980.998. The three portfolios based on the MAP (after thresholding) are already incorporating the hard constraint, so it comes as no surprise to report that the sum of the weights for all three is exactly 11.

Before filtering out the short positions from the active set, we checked its cardinality (corresponding to the same thresholds (k,π∗)=(2.5,0.65),(k,\pi^{\ast})=(2.5,0.65), and recorded Swith negative=196.S\_{\text{with negative}}=196. In other words, the sign filter eliminated an additional 4141 names. For comparison, we also record the TE for the three portfolios when we allow negative weights.

| TE when allowing shorts (FIT–1 window) | |
| --- | --- |
| #​n​n​z​wMAP\#\;nnz\,w\_{\text{MAP}} | 454 |
| |S||S| | 196 |
| #​wMAP<0\#w\_{\text{MAP}}<0 | 139 |
| T​EMAP{TE}\_{\text{MAP}} | 7.156e-05 |
| T​EPRUNED{TE}\_{\text{PRUNED}} | 9.877e-04 |
| T​EDEBIAS{TE}\_{\text{DEBIAS}} | 2.342e-04 |
| T​EFISTA{TE}\_{\text{FISTA}} | 2.361e-04 |

Table 4: Summary of the long-short active set SS and tracking-error diagnostics on the fit window.

It is quite clear that eliminating the shorts and refitting on the new active set results in a small increase in TE, providing further support to the decision to produce long-only portfolios. Compared to the MAP, the increase in TE is significant, but of course, this is the price to pay for sparsity.

For the rest of this case study we will hold (and later rebalance) the refit-on-S-with-FISTA, wF​I​S​T​Aw\_{FISTA} for short (but not to be confused with the unprocessed MAP, also found by FISTA). Below is a list of the top-25 assets as determined by our approach

| rank | ticker | w |
| --- | --- | --- |
| 1 | AAPL | +4.055e-02 |
| 2 | MSFT | +3.292e-02 |
| 3 | AMZN | +2.685e-02 |
| 4 | GOOGL | +2.556e-02 |
| 5 | UNH | +2.119e-02 |
| 6 | HD | +2.014e-02 |
| 7 | KO | +1.879e-02 |
| 8 | DIS | +1.831e-02 |
| 9 | META | +1.725e-02 |
| 10 | CVX | +1.667e-02 |
| 11 | WFC | +1.636e-02 |
| 12 | VZ | +1.582e-02 |
| 13 | MRK | +1.502e-02 |

| rank | ticker | w |
| --- | --- | --- |
| 14 | BRK-B | +1.384e-02 |
| 15 | MA | +1.355e-02 |
| 16 | MDT | +1.275e-02 |
| 17 | DD | +1.257e-02 |
| 18 | BAC | +1.241e-02 |
| 19 | JNJ | +1.231e-02 |
| 20 | JPM | +1.221e-02 |
| 21 | COST | +1.202e-02 |
| 22 | XOM | +1.165e-02 |
| 23 | INTC | +1.133e-02 |
| 24 | CSCO | +1.116e-02 |
| 25 | ADBE | +1.031e-02 |

Table 5: Top ww holdings (FISTA on SS).

### Performance out-of-sample

We now hold the constructed portfolio for 6 months (128 trading days) for what we refer to as the “HOLD-1” period, which starts on the first trading day after the end of the “FIT-1” window used for the construction. At the start of HOLD-1 we select wFISTAw\_{\mathrm{FISTA}} and hold it buy–and–hold over [tH1,start,tH1,end][t\_{\mathrm{H1,start}},t\_{\mathrm{H1,end}}]. We look at the realised TE (daily, RMSE of TE on a rolling 20-day window, and cumulative returns).

These are summarised in the following figures3331​bp=10−41\,\text{bp}\,=10^{-4} in return units.

![[Uncaptioned image]](hold1_cum_returns.png)



Figure 7: Index tracking (cumulative returns).



![Refer to caption](RMSE_rolling_bp_hold1.png)


Figure 8: Rolling RMSE TE (20-days window) in bp units.

![Refer to caption](daily_TE_bp_hold1.png)


Figure 9: Daily TE in bp units.

We can clearly see excellent tracking performance, especially for the first 5 months.

For single-period strategies or myopic formulations with linear/fixed costs, this would be the last step of the workflow before investing in the portfolio. Additional considerations, such as different rules for thresholding for more/less sparsity, net and gross exposures via simple caps, etc, are possible, if desired.

To keep the focus on the computational and methodological aspects of our approach, we don’t pursue these further; nevertheless, all the information to post-process the portfolio for all of the above goals is already available from the previous steps. If more sparsity is desired, there are three main parameters (and combinations thereof) one can further tune: *first*, the gating parameter π∗\pi^{\ast}: increasing it corresponds to requiring higher levels of confidence and will further sift the remaining assets. *Second*, the magnitude constraint parameter τp​o​s​t\tau\_{post} which similarly decreases the active support when increased. We do, however, note that here we selected this parameter automatically learning from the long-MALA run, and we didn’t set it in an ad hoc way. *Third*, treating σ2\sigma^{2} as a TE-related parameter rather than noise variance (as we do in the rebalancing step), one could increase it by 1-2 orders of magnitude. SAPG will adapt to the new reality and select a parameter θ^⋆\hat{\theta}\_{\star} that enforces even more sparsity

### 7.3 What if we don’t rebalance?

Before proceeding with the rebalancing step, we look at the performance of the original portfolio on HOLD-2. This is the second trading period, whose first day is the first trading day after the end of HOLD-1.

These are summarised in the following figures showing both periods

![[Uncaptioned image]](hold12_te_rmse20_bp.png)



Figure 10: Rolling RMSE TE in bp units.

![[Uncaptioned image]](daily_TE_bp_hold12.png)



Figure 11: Daily TE in bp units.



![[Uncaptioned image]](HOLD12_cum_returns.png)



Figure 12: Index tracking (cumulative returns).

We have clearly labelled the start of the HOLD-2 period, and replicated the performance plots from the first period.

The above graphs suggest that even if we had chosen not to rebalance, the tracking performance of the original portfolio remains extremely good, a year after its design. Of course, one should not rush to conclude that this will always be the case, after all, this was a rather non-turbulent period. However, it does suggest that our method is quite robust, and it also supports the rebalancing strategy we advocate for here, i.e., to construct new portfolios built upon the originally held.

### 7.4 Rebalancing

We frame the rebalancing problem as an optimisation problem with adjustment vector Δ​w\Delta w playing the role of the decision variable. The new allocation vector will be

|  |  |  |
| --- | --- | --- |
|  | wnew=wold+Δ​w,w\_{\text{new}}=w\_{\text{old}}+\Delta w, |  |

where woldw\_{\text{old}} is the portfolio held up to this point. To maintain the budget constraint on wneww\_{\text{new}}
we enforce the hard sum–zero constraint

|  |  |  |
| --- | --- | --- |
|  | 1⊤​Δ​w=01^{\top}\Delta w=0 |  |

for Δ​w\Delta w so that the budget constraint is preserved exactly.

Using the same length as before, T=500T=500, we construct a second fitting window ending at the evaluation date of the first portfolio; we refer to this as the “FIT–2 ” window. We operate with the vector y2∈RTy\_{2}\in R^{T} of index returns, and the matrix R2∈ℝT×pR\_{2}\in\mathbb{R}^{T\times p} of asset returns.

As before, we centre:

|  |  |  |
| --- | --- | --- |
|  | y2,μ=1T​∑ty2,t,R2,μ,j=1T​∑tR2,t​j,j∈{1,…,p}y2,c=y2−y2,μ​𝟏T,R2,c=R2−𝟏T​R2,μ⊤,\begin{split}y\_{2,\mu}&=\frac{1}{T}\sum\_{t}y\_{2,t},\quad R\_{2,\mu,j}=\frac{1}{T}\sum\_{t}R\_{2,tj},\qquad j\in\{1,\dots,p\}\\ y\_{2,c}&=y\_{2}-y\_{2,\mu}\mathbf{1}\_{T},\qquad R\_{2,c}=R\_{2}-\mathbf{1}\_{T}R\_{2,\mu}^{\top},\end{split} |  |

and build a new set of scales α(2)\alpha^{(2)} based on R2,cR\_{2,c}. On FIT–2, we build a weighted Laplace prior on Δ​w\Delta w,

|  |  |  |
| --- | --- | --- |
|  | p​(Δ​w∣κ)∝exp⁡(−κ​SΔ​(Δ​w))​ι{𝟏⊤​Δ​w=0},SΔ​(Δ​w)=∑j=1pαj(Δ)​|Δ​wj|.p(\Delta w\mid\kappa)\;\propto\;\exp\!\Bigl(-\kappa\,S\_{\Delta}(\Delta w)\Bigr)\;\mathbb{\iota}\_{\{\mathbf{1}^{\top}\Delta w=0\}},\qquad S\_{\Delta}(\Delta w)\;=\;\sum\_{j=1}^{p}\alpha^{(\Delta)}\_{j}\,|\Delta w\_{j}|. |  |

The base scales are recomputed from R2,cR\_{2,c} using the same
column-norm recipe as in FIT–1,

|  |  |  |
| --- | --- | --- |
|  | α~j=‖R2,c(:,j)‖2T,α~j←α~j/α~¯,\tilde{\alpha}\_{j}\;=\;\frac{\|R\_{2,c}^{(:,j)}\|\_{2}}{\sqrt{T}},\qquad\tilde{\alpha}\_{j}\leftarrow\tilde{\alpha}\_{j}/\overline{\tilde{\alpha}}, |  |

and we then *square* them for the rebalancing prior,

|  |  |  |
| --- | --- | --- |
|  | αj(Δ)=(α~j)2.\alpha^{(\Delta)}\_{j}\;=\;\bigl(\tilde{\alpha}\_{j}\bigr)^{2}. |  |

As before, we recorded the minimal, maximal, and mean weights as 0.297,12.011,10.297,12.011,1 respectively.

The working posterior on FIT--2 is

|  |  |  |
| --- | --- | --- |
|  | πκ​(Δ​w∣data)∝exp⁡{−12​σΔ​w2​‖y2,res−R2,c​Δ​w‖22−κ​SΔ​(Δ​w)}​ι{𝟏⊤​Δ​w=0}.\pi\_{\kappa}(\Delta w\mid\text{data})\;\propto\;\exp\!\left\{-\frac{1}{2\sigma^{2}\_{\Delta w}}\,\bigl\|y\_{2,\mathrm{res}}-R\_{2,c}\Delta w\bigr\|\_{2}^{2}-\kappa\,S\_{\Delta}(\Delta w)\right\}\;\iota\_{\{\mathbf{1}^{\top}\Delta w=0\}}. |  |

Next, we calculate the MAD estimator for the (baseline) noise variance as described in Section [C](https://arxiv.org/html/2512.22109v1#A3 "Appendix C Noise variance estimation ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification"). For this window we calculated σ^Δ​w2=2.510⋅10−9.\hat{\sigma}\_{\Delta w}^{2}=2.510\cdot 10^{-9}. Mirroring the earlier procedure (MAD, then SAPG, then MAP), we compute Δ​wM​A​P\Delta w\_{MAP} for the baseline case. From the figure and the table below, we see that the smoothed objective does not produce exact zeros,

![[Uncaptioned image]](dw_map_hist_nz.png)



Figure 13:  Δ​wM​A​P\Delta w\_{MAP}.



| bin |  | ℓ1\ell\_{1} mass in bin | share (%) |
| --- | --- | --- | --- |
| 1 | [6.030×10−9, 3.090×10−8][6.030\times 10^{-9},\,3.090\times 10^{-8}] | 2.661×10−82.661\times 10^{-8} | 0.00 |
| 2 | [3.090×10−8, 1.583×10−7][3.090\times 10^{-8},\,1.583\times 10^{-7}] | 7.870×10−77.870\times 10^{-7} | 0.00 |
| 3 | [1.583×10−7, 8.110×10−7][1.583\times 10^{-7},\,8.110\times 10^{-7}] | 2.704×10−52.704\times 10^{-5} | 0.09 |
| 4 | [8.110×10−7, 4.155×10−6][8.110\times 10^{-7},\,4.155\times 10^{-6}] | 4.395×10−44.395\times 10^{-4} | 1.51 |
| 5 | [4.155×10−6, 2.129×10−5][4.155\times 10^{-6},\,2.129\times 10^{-5}] | 1.421×10−31.421\times 10^{-3} | 4.88 |
| 6 | [2.129×10−5, 1.091×10−4][2.129\times 10^{-5},\,1.091\times 10^{-4}] | 4.824×10−44.824\times 10^{-4} | 1.66 |
| 7 | [1.091×10−4, 5.589×10−4][1.091\times 10^{-4},\,5.589\times 10^{-4}] | 5.527×10−35.527\times 10^{-3} | 18.97 |
| 8 | [5.589×10−4, 2.863×10−3][5.589\times 10^{-4},\,2.863\times 10^{-3}] | 2.123×10−22.123\times 10^{-2} | 72.89 |

Table 6: Baseline (c=1)(c=1) ℓ1\ell\_{1} mass share by |Δ​w||\Delta w| bin for the Δ​w\Delta w MAP estimate. We also record
  
(min|Δw|=6.030e−09,max|Δw|=2.863e−03)\min|\Delta w|=6.030e-09,\max|\Delta w|=2.863e-03).

Recall that we wish to *choose* a “noise level” that is consistent with the realised TE over the FIT–2 window for the existing portfolio woldw\_{\mathrm{old}}, but still
allows the prior to exert substantial influence. To this end we introduce a scalar multiplier c>0c>0 and consider the
family

|  |  |  |
| --- | --- | --- |
|  | σΔ​w2​(c)=c​σΔ​w,base2,c∈𝒞0,\sigma^{2}\_{\Delta w}(c)\;=\;c\,\sigma^{2}\_{\Delta w,\mathrm{base}},\qquad c\in\mathcal{C}\_{0}, |  |

for a grid 𝒞0\mathcal{C}\_{0} of candidate values. For each value of candidate c,c, we employ SAPG to find the corresponding κ​(c)\kappa(c). Note that c​σ2c\,\sigma^{2} feeds into the Lipschitz constant of the likelihood term and thus directly affects the timestep of the MYULA chains involved. For the SAPG runs, we used 15000 iterations with the first 4000 treated as burn-in.

We then fix the pair
(σΔ​w2​(c),κ⋆​(c))(\sigma^{2}\_{\Delta w}(c),\kappa\_{\star}(c)) and use FISTA (4000 iterations at most) to compute the corresponding
smoothed MAP

|  |  |  |
| --- | --- | --- |
|  | Δ​wMAP​(c)=arg⁡minΔ​w∈ℝp⁡Φ​(Δ​w;κ⋆​(c),σΔ​w2​(c)),\Delta w\_{\mathrm{MAP}}(c)\;=\;\arg\min\_{\Delta w\in\mathbb{R}^{p}}\Phi\bigl(\Delta w;\,\kappa\_{\star}(c),\sigma^{2}\_{\Delta w}(c)\bigr), |  |

using a FISTA scheme on ([7.4](https://arxiv.org/html/2512.22109v1#S7.Ex93 "7.4 Rebalancing ‣ 7 A case study: tracking the S&P 500 ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification")) with the
budget–constrained proximal map
proxλMY​g\mathrm{prox}\_{\lambda\_{\mathrm{MY}}g}.

The rebalanced portfolio
is then
wnew​(c)=wold+Δ​wMAP​(c)w\_{\mathrm{new}}(c)=w\_{\mathrm{old}}+\Delta w\_{\mathrm{MAP}}(c),
automatically satisfying 𝟏⊤​wnew​(c)=1\mathbf{1}^{\top}w\_{\mathrm{new}}(c)=1.

As before, we define
an *effective* cardinality

|  |  |  |
| --- | --- | --- |
|  | nnzeff​(c)=#​{j∈{1,…,p}:|Δ​wMAPj​(c)|≥τeff},\mathrm{nnz}\_{\mathrm{eff}}(c)\;=\;\#\Bigl\{j\in\{1,\dots,p\}:\bigl|\Delta{w\_{\mathrm{MAP}}}\_{j}(c)\bigr|\geq\tau\_{\mathrm{eff}}\Bigr\}, |  |

where here τeff=10−4\tau\_{\mathrm{eff}}=10^{-4} is a small fixed threshold chosen to ignore numerically negligible weight adjustments. We also record the
raw cardinality
nnzraw​(c)=#​{j:Δ​wMAPj​(c)≠0}\mathrm{nnz}\_{\mathrm{raw}}(c)=\#\{j:\Delta{w\_{\mathrm{MAP}}}\_{j}(c)\neq 0\}
for diagnostic purposes, but all decisions are based on
nnzeff​(c)\mathrm{nnz}\_{\mathrm{eff}}(c).

For each c∈𝒞0c\in\mathcal{C}\_{0} we evaluate both the TE
TEFIT2​(wnew​(c))\mathrm{TE}\_{\mathrm{FIT2}}(w\_{\mathrm{new}}(c)) and the effective
adjustment size nnzeff​(c)\mathrm{nnz}\_{\mathrm{eff}}(c). We then use our
scalar score

|  |  |  |
| --- | --- | --- |
|  | d​(c)=ϕTE​(c)​wnnz​(c),d(c)\;=\;\phi\_{\mathrm{TE}}(c)\,w\_{\mathrm{nnz}}(c), |  |

where:

* •

  We specify lower and upper fractions
  0<γlo<1<γhi0<\gamma\_{\mathrm{lo}}<1<\gamma\_{\mathrm{hi}} and set

  |  |  |  |
  | --- | --- | --- |
  |  | ϕTE​(c)={1,if ​γlo​TEold≤TEFIT2​(wreb​(c))≤γhi​TEold,0,otherwise.\phi\_{\mathrm{TE}}(c)\;=\;\begin{cases}1,&\text{if }\gamma\_{\mathrm{lo}}\,\mathrm{TE}\_{\mathrm{old}}\leq\mathrm{TE}\_{\mathrm{FIT2}}(w\_{\mathrm{reb}}(c))\leq\gamma\_{\mathrm{hi}}\,\mathrm{TE}\_{\mathrm{old}},\\[2.5pt] 0,&\text{otherwise.}\end{cases} |  |

  In our experiments we use γlo=0.2\gamma\_{\mathrm{lo}}=0.2 and
  γhi=1.2\gamma\_{\mathrm{hi}}=1.2, reflecting the view that (i) TE values
  much smaller than 0.2​TEold0.2\,\mathrm{TE}\_{\mathrm{old}} are likely to
  correspond to overfitting on FIT–2, whereas (ii) TE values much larger than 1.2​TEold1.2\,\mathrm{TE}\_{\mathrm{old}} indicate ineffective
  tracking.
* •

  *Gaussian preference over effective cardinality.*
  Let nnzprev\mathrm{nnz}\_{\mathrm{prev}} denote the cardinality of the
  existing portfolio woldw^{\mathrm{old}}, and set a target adjustment
  size

  |  |  |  |
  | --- | --- | --- |
  |  | n⋆=γnnz​nnzprev,n\_{\star}\;=\;\gamma\_{\mathrm{nnz}}\,\mathrm{nnz}\_{\mathrm{prev}}, |  |

  with γnnz≈0.25\gamma\_{\mathrm{nnz}}\approx 0.25: we prefer to adjust only
  a moderate fraction of the currently held names. Given a scale
  parameter σnnz=5\sigma\_{\mathrm{nnz}}=5 (in units of “names”),
  we define

  |  |  |  |
  | --- | --- | --- |
  |  | wnnz​(c)=exp⁡(−12​(nnzeff​(c)−n⋆σnnz)2).w\_{\mathrm{nnz}}(c)\;=\;\exp\!\left(-\frac{1}{2}\left(\frac{\mathrm{nnz}\_{\mathrm{eff}}(c)-n\_{\star}}{\sigma\_{\mathrm{nnz}}}\right)^{2}\right). |  |

The score d​(c)d(c) is thus nonzero only for settings where the TE lies
in a plausible range, and among those, it favours configurations where
the effective number of adjusted names is neither too small nor too
large. For this run, we used the grid

|  |  |  |
| --- | --- | --- |
|  | 𝒞0=[1.0,15,25,35,45,50,55,60,65,70.0,80.0,90.0,100.0].\mathcal{C}\_{0}=[1.0,15,25,35,45,50,55,60,65,70.0,80.0,90.0,100.0]. |  |

The results are reported in Table [7](https://arxiv.org/html/2512.22109v1#S7.T7 "Table 7 ‣ 7.4 Rebalancing ‣ 7 A case study: tracking the S&P 500 ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification").

| cc | σΔ​w2​(c)\sigma\_{\Delta w}^{2}(c) | κEB​(c)\kappa\_{\mathrm{EB}}(c) | TEFIT2\mathrm{TE}\_{\mathrm{FIT2}} | #​{Δ​w≠0}\#\{\Delta w\neq 0\} | nnzeff\mathrm{nnz}\_{\mathrm{eff}} | ϕTE\phi\_{\mathrm{TE}} | wnnzw\_{\mathrm{nnz}} | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.000 | 2.510e-09 | 7.014e+02 | 7.8032e-05 | 478 | 436 | 0.000 | 0.000 | 0.000 |
| 15.000 | 3.765e-08 | 9.616e+02 | 1.8504e-04 | 478 | 243 | 1.000 | 0.000 | 0.000 |
| 25.000 | 6.275e-08 | 1.267e+03 | 2.5863e-04 | 478 | 152 | 1.000 | 0.000 | 0.000 |
| 35.000 | 8.784e-08 | 1.442e+03 | 3.0548e-04 | 478 | 93 | 1.000 | 0.000 | 0.000 |
| 45.000 | 1.129e-07 | 1.694e+03 | 3.4440e-04 | 478 | 62 | 1.000 | 0.000 | 0.000 |
| 50.000 | 1.255e-07 | 1.699e+03 | 3.5506e-04 | 478 | 54 | 1.000 | 0.010 | 0.010 |
| 55.000 | 1.380e-07 | 1.671e+03 | 3.6336e-04 | 478 | 45 | 1.000 | 0.458 | 0.458 |
| 60.000 | 1.506e-07 | 1.712e+03 | 3.7475e-04 | 478 | 34 | 1.000 | 0.637 | 0.637 |
| 65.000 | 1.631e-07 | 1.713e+03 | 3.8197e-04 | 478 | 25 | 1.000 | 0.023 | 0.023 |
| 70.000 | 1.757e-07 | 1.714e+03 | 3.8711e-04 | 478 | 21 | 1.000 | 0.002 | 0.002 |
| 80.000 | 2.008e-07 | 1.713e+03 | 3.9469e-04 | 478 | 16 | 1.000 | 0.000 | 0.000 |
| 90.000 | 2.259e-07 | 1.714e+03 | 4.0019e-04 | 478 | 7 | 1.000 | 0.000 | 0.000 |
| 100.000 | 2.510e-07 | 1.714e+03 | 4.0385e-04 | 478 | 4 | 1.000 | 0.000 | 0.000 |

Table 7: Grid over noise scale factors cc for the rebalancing model on the FIT–2 window. For each cc we set σΔ​w2​(c)=c​σΔ​w,base2\sigma\_{\Delta w}^{2}(c)=c\,\sigma\_{\Delta w,\mathrm{base}}^{2}, recompute κE​B​(c)\kappa\_{EB}(c) via SAPG on the smoothed objective, and solve the corresponding MAP problem. The score combines a TE-acceptance window and a Gaussian preference for moderate effective adjustment size nnzeff​(Δ​w)\mathrm{nnz}\_{\mathrm{eff}}(\Delta w).

Once c∗c^{\*} has been selected on the grid, we lock in the corresponding
noise variance and sparsity level,

|  |  |  |
| --- | --- | --- |
|  | σΔ​w,final2=σΔ​w2​(c∗)=1.506​e−07,κ⋆,final=κ⋆​(c∗)=1.712​e+03,\sigma^{2}\_{\Delta w,\mathrm{final}}\;=\;\sigma^{2}\_{\Delta w}(c^{\*})=1.506e-07,\qquad{\kappa\_{\star}}\_{,{\text{final}}}\;=\;\kappa\_{\star}(c^{\*})=1.712e+03, |  |

together with the associated smoothed MAP rebalancing move
Δ​wMAP=Δ​wMAP​(c∗)\Delta w\_{\mathrm{MAP}}=\Delta w\_{\mathrm{MAP}}(c^{\*}) and
rebalanced portfolio wnew=wnew​(c∗)w\_{\mathrm{new}}=w\_{\mathrm{new}}(c^{\*}).
These now define a fixed target posterior for uncertainty quantification
on FIT–2. In particular, the subsequent (again preconditioned) MALA sampler is constructed around
Φ​(Δ​w;κ⋆,final,σΔ​w,final2)\Phi\left(\Delta w;{\kappa\_{\star}}\_{,{\text{final}}},\sigma^{2}\_{\Delta w,\mathrm{final}}\right)
and initialised at Δ​wMAP\Delta w\_{\mathrm{MAP}}.

We use σ2=1.506​e−07,κ=1.712​e+03,λM​Y=7.997​e−09,\sigma^{2}=1.506e-07,\kappa=1.712e+03,\lambda\_{MY}=7.997e-09, and from the preconditioning, we calculate Lp​r​e=1.415​e+02L\_{pre}=1.415e+02 and with it a baseline timestep γ0(p​r​e)=3.180​e−03.{\gamma\_{0}}\_{(pre)}=3.180e-03. As before, we run a few short chains to determine a timestep that will result in a good acceptance rate ∼0.60.\sim 0.60.

| Timestep | Acceptance Rate |
| --- | --- |
| 1.240×10−31.240\times 10^{-3} | 0.891 |
| 1.550×10−31.550\times 10^{-3} | 0.865 |
| 1.937×10−31.937\times 10^{-3} | 0.829 |
| 2.422×10−32.422\times 10^{-3} | 0.779 |
| 3.027×10−33.027\times 10^{-3} | 0.715 |
| 3.784×10−33.784\times 10^{-3} | 0.630 |

Table 8: Tuning (γ\gamma) and acceptance rate.

We run a long (250000 (thin=6), 50000 burn-in) MALA chain using a timestep of 3.784×10−33.784\times 10^{-3}, which resulted in an acceptance rate of 0.6330.633. As before, we record ACF/ESS for mixing purposes, e.g., see the figure below for some ACF plots.

![Refer to caption](dw_mala_acf_TE_postburn.png)


(a) ACF of TE.

![Refer to caption](dw_mala_acf_dw_j148_postburn.png)


(b) ACF of asset 148.

![Refer to caption](dw_mala_acf_dw_j359_postburn.png)


(c) ACF of asset 359.

Figure 14: Post-burn ACF diagnostics for the Δ​w\Delta w MALA.

Following the scale-based thresholding idea discussed earlier, we define a global posterior
scale threshold

|  |  |  |
| --- | --- | --- |
|  | τpost=k⋅median​(sd^1,…,sd^p),k>0,\tau\_{\mathrm{post}}\;=\;k\cdot\mathrm{median}\bigl(\widehat{\mathrm{sd}}\_{1},\dots,\widehat{\mathrm{sd}}\_{p}\bigr),\qquad k>0, |  |

and use both τpost\tau\_{\mathrm{post}} and the activation probabilities
π^j\hat{\pi}\_{j} to gate which coordinates are eligible for rebalancing.

Let Δ​wMAP\Delta w\_{\mathrm{MAP}} denote the smoothed MAP solution for the
rebalancing model at the selected noise scale c∗c^{\ast}.
We recall the definitions

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sτ\displaystyle S\_{\tau} | ={j:|Δ​wMAPj|≥τpost},\displaystyle=\bigl\{j:|\Delta{w\_{\mathrm{MAP}}}\_{j}|\,\geq\,\tau\_{\mathrm{post}}\bigr\}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Sπ​(π⋆)\displaystyle S\_{\pi}(\pi^{\star}) | ={j:π^j≥π⋆},\displaystyle=\bigl\{j:\hat{\pi}\_{j}\,\geq\,\pi^{\star}\bigr\}, |  |

where π⋆∈(0,1)\pi^{\star}\in(0,1) is a user–chosen activation probability
threshold. The intersection

|  |  |  |
| --- | --- | --- |
|  | Srule​(π⋆)=Sτ∩Sπ​(π⋆)S\_{\mathrm{rule}}(\pi^{\star})\;=\;S\_{\tau}\,\cap\,S\_{\pi}(\pi^{\star}) |  |

collects those coordinates that are simultaneously “large” in the MAP
sense and frequently active under the posterior.444Other ideas are also possible: for example, one could form “confidence intervals (CI)” based on the samples obtained and design a rule such as “if the 95% CI for asset jj contains 0, we declare Δ​wj=0.\Delta w\_{j}=0. Finally, while negative entries in Δ​w\Delta w are meaningful, under the mandate of no-shorts, one also needs to impose that wn​e​w,j=wo​l​d,j+(Δ​wMAP)j≥0,w\_{new,j}=w\_{old,j}+(\Delta{w\_{\mathrm{MAP}}})\_{j}\geq 0, clipping to zero if not.

In our experiments, we fix k=2.5k=2.5 in the definition of
τpost\tau\_{\mathrm{post}} and use π⋆=0.8\pi^{\star}=0.8 as a high–confidence
activation threshold. The corresponding posterior scale
τpost\tau\_{\mathrm{post}} and the resulting cardinalities
#​Sτ,#​Sπ​(π⋆)\#S\_{\tau},\#S\_{\pi}(\pi^{\star}) and
#​(Sτ∩Sπ​(π⋆))\#\bigl(S\_{\tau}\cap S\_{\pi}(\pi^{\star})\bigr) are summarised in
Table [9](https://arxiv.org/html/2512.22109v1#S7.T9 "Table 9 ‣ 7.4 Rebalancing ‣ 7 A case study: tracking the S&P 500 ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification").

| π⋆\pi^{\star} | kk in τpost\tau\_{\mathrm{post}} | #​Sτ\#S\_{\tau} | #​Sπ⋆\#S\_{\pi^{\star}} | #​(Sτ∧Sπ⋆)\#(S\_{\tau}\wedge S\_{\pi^{\star}}) |
| --- | --- | --- | --- | --- |
| 0.60 | 2.50 | 2 | 1 | 1 |
| 0.70 | 2.50 | 2 | 0 | 0 |
| 0.80 | 2.50 | 2 | 0 | 0 |
| 0.90 | 2.50 | 2 | 0 | 0 |

Table 9: Summary of activation sets for the Δ​w\Delta w rebalancing step. The posterior scale threshold is τpost=k​median​(sd^j)\tau\_{\mathrm{post}}=k\,\mathrm{median}(\widehat{\mathrm{sd}}\_{j}) with kk given in the table. For each π⋆\pi^{\star} we report three cardinalities: the τ\tau-only rule, the π⋆\pi^{\star}-only rule, and the intersection τ∧π⋆\tau\wedge\pi^{\star}.



| Ticker | jj | wjoldw\_{j}^{\mathrm{old}} | Δ​wjMAP\Delta w\_{j}^{\mathrm{MAP}} | wjneww\_{j}^{\mathrm{new}} | π^j\hat{\pi}\_{j} |
| --- | --- | --- | --- | --- | --- |
| DD | 148 | +1.2572e-02 | -2.8633e-03 | +9.7083e-03 | 0.656 |
| PG | 359 | +0.0000e+00 | +2.6046e-03 | +2.6046e-03 | 0.588 |

Table 10: Active coordinates under the τpost\tau\_{\mathrm{post}}-only rule for the Δ​w\Delta w rebalancing model. The columns report the ticker, coordinate index, previous weight wjoldw\_{j}^{\mathrm{old}}, proposed change Δ​wjMAP\Delta w\_{j}^{\mathrm{MAP}}, updated weight wjnew=wjold+Δ​wjMAPw\_{j}^{\mathrm{new}}=w\_{j}^{\mathrm{old}}+\Delta w\_{j}^{\mathrm{MAP}}, and the posterior activation probability π^j=ℙ​(|Δ​wj|≥τpost)\hat{\pi}\_{j}=\mathbb{P}(|\Delta w\_{j}|\geq\tau\_{\mathrm{post}}).

In this instance, our gating metrics have identified two tickers for rebalancing consideration: there is a proposed reduction in the weight of the asset with index 148 (backed up by a probability of ≈66%\approx 66\%), and a proposal for opening a position in the (previously inactive) asset with index 359.

For demonstration only, and to show how to make the process fully automatic (up to the input of π⋆\pi^{\star}), we adopt the following *UQ–gated rule* for rebalancing in the
Δ​w\Delta w stage:

* •

  Let Srule=Srule​(π⋆)S\_{\mathrm{rule}}=S\_{\mathrm{rule}}(\pi^{\star}) with
  π⋆=0.8\pi^{\star}=0.8.
* •

  With the sum-to-zero constraint, a nontrivial rebalance needs at least two names (decrease one, increase another) unless you allow cash/leverage. If #​Srule<2\#S\_{\mathrm{rule}}<2, we declare the posterior evidence too weak or too concentrated to justify a structural change and
  perform no rebalance, i.e. we keep wnew=woldw\_{\mathrm{new}}=w\_{\mathrm{old}}.
* •

  If #​Srule≥2\#S\_{\mathrm{rule}}\geq 2, we construct an implementable
  Δ​w\Delta w confined to SruleS\_{\mathrm{rule}} and adjust the portfolio
  only on that active set.

In this case, we are not confident enough in the proposed moves, so our rules will preserve the current portfolio. This is, of course, up to the trader to decide, but the rationale here was to discourage many moves without “strong signals”.

| Ticker | jj | wjoldw\_{j}^{\mathrm{old}} | Δ​wjMAP\Delta w\_{j}^{\mathrm{MAP}} | wjneww\_{j}^{\mathrm{new}} | π^j\hat{\pi}\_{j} |
| --- | --- | --- | --- | --- | --- |
| *No active coordinates under this gating rule.* | | | | | |

Table 11: Active coordinates under the τpost∧π⋆=0.80\tau\_{\mathrm{post}}\wedge\pi^{\star}=0.80 rule for the Δ​w\Delta w rebalancing model. The columns report the ticker, coordinate index, previous weight wjoldw\_{j}^{\mathrm{old}}, proposed change Δ​wjMAP\Delta w\_{j}^{\mathrm{MAP}}, updated weight wjnew=wjold+Δ​wjMAPw\_{j}^{\mathrm{new}}=w\_{j}^{\mathrm{old}}+\Delta w\_{j}^{\mathrm{MAP}}, and the posterior activation probability π^j=ℙ​(|Δ​wj|≥τpost)\hat{\pi}\_{j}=\mathbb{P}(|\Delta w\_{j}|\geq\tau\_{\mathrm{post}}).

We highlight here the important role of the UQ metrics in the decision-making stage, which in turn necessitates high-quality samples.

### 7.5 One more trading period. What if we rebalanced?

At the end of the HOLD–1 period, based on the above rebalancing considerations, we decide on whether and how to adjust our portfolio before the next trading period, HOLD–2.

As our rules indicated, no changes were made, and our portfolio remains wF​I​S​T​Aw\_{FISTA}, which was designed using FIT–1 data, held in HOLD–1, and has not been adjusted based on the FIT–2 data or our gating rules. However, we decided also to hold a second portfolio, the one formed by following the weak rebalancing suggestions from before. Given that the magnitude of the proposed changes for the two assets is nearly the same and in the opposite direction, we simply open a position in “PG” and reduce the weight of “DD” by the same amount. This ensures that the budget constraint is satisfied, but now this portfolio, referred to as “Rebalanced”, has an additional asset.

These are summarised in the following figures

![[Uncaptioned image]](hold2_cumret_overlay.png)



Figure 15: Index tracking (cumulative returns).



![Refer to caption](hold2_te_rmse20_bp.png)


Figure 16: Rolling RMSE TE (20-day window) in bp units.

![Refer to caption](hold2_te_daily_bp.png)


Figure 17: Daily TE in bp units.

We see that the rebalanced portfolio is nearly identical to the original one in terms of tracking performance, suggesting that the effect of the moves was minimal in both TE and returns.

### 7.6 Rebalancing considerations for the next period

At the end of HOLD–2, we create again a T=500T=500 window ending on the last day of HOLD–2 (we refer to this period as “FIT–3”), and submit both of these portfolios to the same pipeline to determine the need for rebalancing. As this mirrors very closely the steps shown for FIT–2, we only show the more interesting results and the output of the gating rules. We abuse notation and reuse “Δ​w\Delta w” to signify the vector of adjustments from the current portfolio.

### The original portfolio

| π⋆\pi^{\star} | kk in τpost\tau\_{\mathrm{post}} | #​Sτ\#S\_{\tau} | #​Sπ⋆\#S\_{\pi^{\star}} | #​(Sτ∧Sπ⋆)\#(S\_{\tau}\wedge S\_{\pi^{\star}}) |
| --- | --- | --- | --- | --- |
| 0.60 | 2.50 | 11 | 1 | 1 |
| 0.70 | 2.50 | 11 | 0 | 0 |
| 0.80 | 2.50 | 11 | 0 | 0 |
| 0.90 | 2.50 | 11 | 0 | 0 |

Table 12: Summary of activation sets for the Δ​w\Delta w rebalancing step on the FIT–3 window. The posterior scale threshold is τpost=k​median​(sd^j)\tau\_{\mathrm{post}}=k\,\mathrm{median}(\widehat{\mathrm{sd}}\_{j}) with kk given in the table. For each π⋆\pi^{\star} we report three cardinalities: the τ\tau-only rule, the π⋆\pi^{\star}-only rule, and the intersection τ∧π⋆\tau\wedge\pi^{\star}.



| Ticker | jj | wjoldw\_{j}^{\mathrm{old}} | Δ​wjMAP\Delta w\_{j}^{\mathrm{MAP}} | wjneww\_{j}^{\mathrm{new}} | π^j\hat{\pi}\_{j} |
| --- | --- | --- | --- | --- | --- |
| AFL | 8 | +6.9100e-03 | -4.2257e-03 | +2.6843e-03 | 0.521 |
| AMT | 27 | +2.2742e-03 | +2.7703e-03 | +5.0445e-03 | 0.352 |
| KO | 110 | +1.8787e-02 | -2.1971e-03 | +1.6590e-02 | 0.489 |
| DD | 148 | +1.2572e-02 | -3.3547e-03 | +9.2170e-03 | 0.668 |
| XOM | 176 | +1.1652e-02 | -3.6003e-03 | +8.0522e-03 | 0.290 |
| GPC | 201 | +5.8994e-03 | -2.4848e-03 | +3.4145e-03 | 0.414 |
| MKC | 289 | +0.0000e+00 | +2.5596e-03 | +2.5596e-03 | 0.317 |
| MCD | 290 | +2.3230e-03 | +3.4824e-03 | +5.8054e-03 | 0.493 |
| PG | 359 | +0.0000e+00 | +3.4678e-03 | +3.4678e-03 | 0.571 |
| SNPS | 407 | +0.0000e+00 | +3.2882e-03 | +3.2882e-03 | 0.140 |
| TRV | 428 | +0.0000e+00 | +3.4885e-03 | +3.4885e-03 | 0.432 |

Table 13: Active coordinates under the τpost\tau\_{\mathrm{post}}-only rule for the Δ​w\Delta w rebalancing model on FIT–3. The columns report the ticker, coordinate index, previous weight wjoldw\_{j}^{\mathrm{old}}, proposed change Δ​wjMAP\Delta w\_{j}^{\mathrm{MAP}}, updated weight wjnew=wjold+Δ​wjMAPw\_{j}^{\mathrm{new}}=w\_{j}^{\mathrm{old}}+\Delta w\_{j}^{\mathrm{MAP}}, and the posterior activation probability π^j=ℙ​(|Δ​wj|≥τpost)\hat{\pi}\_{j}=\mathbb{P}(|\Delta w\_{j}|\geq\tau\_{\mathrm{post}}).

Interestingly, the two assets we decided not to adjust (for the original portfolio), namely “DD” and “PG” are again begging to be considered. Still, under our playbook, there is not enough evidence to change their weights (or any of the others).

### The rebalanced portfolio

We assume now that we have been holding the “rebalanced” portfolio, for which, as an experiment, we previously decided to act on somewhat weak rebalancing suggestions, and we reduced the weight of “DD” while taking a long position in “PG”.

| π⋆\pi^{\star} | kk | #​Sτ\#S\_{\tau} | #​Sπ⋆\#S\_{\pi^{\star}} | #​(Sτ∧Sπ⋆)\#(S\_{\tau}\wedge S\_{\pi^{\star}}) |
| --- | --- | --- | --- | --- |
| 0.60 | 2.50 | 11 | 1 | 1 |
| 0.70 | 2.50 | 11 | 0 | 0 |
| 0.80 | 2.50 | 11 | 0 | 0 |
| 0.90 | 2.50 | 11 | 0 | 0 |

Table 14: Summary of activation sets for the Δ​w\Delta w rebalancing step on the FIT–3 window. The posterior scale threshold is τpost=k​median​(sd^j)\tau\_{\mathrm{post}}=k\,\mathrm{median}(\widehat{\mathrm{sd}}\_{j}). For each π⋆\pi^{\star} we report the τ\tau-only rule, the π⋆\pi^{\star}-only rule, and the intersection τ∧π⋆\tau\wedge\pi^{\star}.



| Ticker | jj | wjoldw\_{j}^{\mathrm{old}} | Δ​wjMAP\Delta w\_{j}^{\mathrm{MAP}} | wjneww\_{j}^{\mathrm{new}} | π^j\hat{\pi}\_{j} |
| --- | --- | --- | --- | --- | --- |
| AFL | 8 | +6.9100e-03 | -4.2257e-03 | +2.6843e-03 | 0.635 |
| AMT | 27 | +2.2742e-03 | +2.7703e-03 | +5.0445e-03 | 0.403 |
| KO | 110 | +1.8787e-02 | -2.1971e-03 | +1.6590e-02 | 0.566 |
| DD | 148 | +9.9678e-03 | -3.3547e-03 | +6.6132e-03 | 0.216 |
| XOM | 176 | +1.1652e-02 | -3.6003e-03 | +8.0522e-03 | 0.301 |
| GPC | 201 | +5.8994e-03 | -2.4848e-03 | +3.4145e-03 | 0.341 |
| MKC | 289 | +0.0000e+00 | +2.5596e-03 | +2.5596e-03 | 0.312 |
| MCD | 290 | +2.3230e-03 | +3.4824e-03 | +5.8054e-03 | 0.528 |
| PG | 359 | +2.6038e-03 | +3.4678e-03 | +6.0716e-03 | 0.338 |
| SNPS | 407 | +0.0000e+00 | +3.2882e-03 | +3.2882e-03 | 0.202 |
| TRV | 428 | +0.0000e+00 | +3.4885e-03 | +3.4885e-03 | 0.519 |

Table 15: Active coordinates under the τpost\tau\_{\mathrm{post}}-only rule for the Δ​w\Delta w rebalancing model on FIT–3. Columns: ticker, index jj, wjoldw\_{j}^{\mathrm{old}}, Δ​wjMAP\Delta w\_{j}^{\mathrm{MAP}}, wjneww\_{j}^{\mathrm{new}}, and π^j\hat{\pi}\_{j}.

Once more, we see no strong indication to rebalance, based on the reported π^j\hat{\pi}\_{j}.

It is unsurprising that after this long period, there are more suggestions for rebalancing (for both portfolios), but encouragingly, involving the same names for two closely-related portfolios. At the same time, the suggested moves are small and not supported by high “activation probabilities.” Ultimately, this comes down to the data and the market conditions, and of course, the trading mentality of individual investors. For a more complete analysis, the explicit incorporation of transaction costs and net returns should be embedded in this process.

## 8 Discussion

We have proposed a Bayesian framework for sparse index tracking that
combines empirical-Bayes calibration, proximal MCMC and UQ-informed
decision rules for portfolio construction and rebalancing. From an
operational-research perspective, the main advantages are:

* •

  *Integrated tuning and inference.* The sparsity parameter is
  learned from the data via SAPG, avoiding external cross-validation or
  ad hoc grid searches, and yielding a coherent probabilistic model.
* •

  *Uncertainty-aware decisions.* Posterior samples inform both
  the choice of active assets and the gating of rebalancing moves. This
  supports decisions about whether to trade at all, and by how much, in a
  transparent way.
* •

  *Practical implementability.* The final portfolios satisfy
  hard budget constraints and long-only requirements, with explicit control
  over the number of names and the size of adjustments, linking directly
  to transaction costs and operational complexity.

The S&P 500 case study shows that the method delivers competitive
tracking performance with relatively sparse portfolios and, in the
period considered, suggests a cautious rebalancing stance: posterior
uncertainty does not justify large structural changes. Of course, in more turbulent periods or with different tuning choices, the same framework would support more active rebalancing.

Several extensions are natural. First, transaction costs and net returns
could be incorporated explicitly, for example via linear or fixed cost
terms in the likelihood or prior, leading to cost-aware rebalancing
rules. Second, alternative sparsity priors—such as group penalties,
structured sparsity or spike-and-slab formulations—could be explored
within the same proximal MCMC and SAPG framework. Third, the approach
extends directly to other regression-based feature selection, or inverse problems with equality constraints, beyond portfolio optimisation, where one wishes to combine regularisation, empirical-Bayes calibration and uncertainty quantification.

Finally, our focus here has been on an empirical-Bayes treatment of the
global sparsity scale. Fully hierarchical specifications, where θ\theta
and related hyperparameters are assigned priors and sampled jointly
with ww, can offer richer uncertainty statements at the cost of additional computational complexity. This is the subject of ongoing work.

## Appendix A Stochastic Approximation Proximal Gradient algorithm (SAPG)

How to appropriately select a regularisation parameter is a well-known problem in the treatment of ill-posed inverse problems (but also in feature selection in statistical settings). For optimisation approaches using an ℓ1\ell\_{1}-penalty (e.g., such as in (?, ?, ?, ?, ?), the parameter is typically chosen in a way that guarantees the required level of sparsity. I.e., one decides in advance what cardinality to target for their portfolio, and adjusts the tuning parameter so that this is the sparsity level enforced. For the index tracking problem,
a TE vs sparsity trade-off curve is commonly computed to help choose a good operating point. Either way, a large number of optimisation problems need to be solved.

Under an empirical Bayesian paradigm, the regularization parameter θ∈Θ,\theta\in\Theta, (for some convex compact set Θ\Theta) is estimated directly from the observed data yy, for example, by maximum marginal likelihood estimation. That is, we compute

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ⋆∈argmaxθ∈Θ​p​(y|θ),\theta\_{\star}\in\underset{\theta\in\Theta}{\mathrm{argmax}}~p(y|\theta)\,, |  | (32) |

where, for any θ∈Θ,\theta\in\Theta, the marginal likelihood p​(y|θ)p(y|\theta) is given, by

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(y|θ)=∫ℝpp​(y|w)​p​(w|θ)​𝑑w.p(y|\theta)=\int\_{\mathbb{R}^{p}}p(y|w)\,p(w|\theta)\,dw\;. |  | (33) |

Given θ⋆\theta\_{\star}, empirical Bayesian approaches base inferences on the pseudo-posterior distribution w↦p​(w|y,θ⋆)w\mapsto p(w|y,\theta\_{\star}), which, for any w∈ℝpw\in\mathbb{R}^{p} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | p(w|y,θ⋆)=exp[−fy(w)−θ⋆g(w)]/∫ℝpexp[−fy(w)−θ⋆g(w)]dw.p(w|y,\theta\_{\star})=\left.\exp[-f\_{y}(w)-\theta\_{\star}g(w)]\middle/\int\_{\mathbb{R}^{p}}\exp[-f\_{y}(w)-\theta\_{\star}g(w)]\;dw\right.\;. |  | (34) |

To be more specific, once SAPG has found θ⋆\theta\_{\star}, we will calculate using FISTA (?, ?), the MAP, namely,

|  |  |  |
| --- | --- | --- |
|  | w^θ⋆,MAP∈arg​minw∈ℝp⁡{fy​(w)+θ⋆​g​(w)},\hat{w}\_{\theta\_{\star},\,\text{MAP}}\in\operatorname\*{arg\,min}\_{w\in\mathbb{R}^{p}}\left\{f\_{y}(w)+\theta\_{\star}\;g(w)\right\}, |  |

before exploring the posterior and reporting estimates. UQ-gating and size-informed hard thresholding will build upon the MAP to produce the tracking portfolio to hold.

We adopt the empirical Bayesian approach of (?, ?)
for the automatic, completely unsupervised selection of the scalar parameter controlling the sparsity level. The maximum marginal likelihood estimation SAPG is a stochastic proximal gradient algorithm driven by proximal Markov chain Monte Carlo samplers of MYULA-type. The method is highly efficient, easy to implement, and comes with theoretical guarantees (?, ?). The motivation behind SAPG is that one could try to find the maximiser using the projected gradient algorithm (?, ?), which is given by (θn)n∈ℕ,(\theta\_{n})\_{n\in\mathbb{N}}, with θ0∈Θ\theta\_{0}\in\Theta and associated with the following recursion

|  |  |  |  |
| --- | --- | --- | --- |
|  | θn+1=ΠΘ​[θn+δn​∇θlog⁡p​(y|θn)],\theta\_{n+1}=\Pi\_{\Theta}\,\left[\theta\_{n}+\delta\_{n}\nabla\_{\theta}\log~p(y|\theta\_{n})\,\right]\;, |  | (35) |

where ΠΘ\Pi\_{\Theta} is the projection onto Θ\Theta and (δn)n∈ℕ(\delta\_{n})\_{n\in\mathbb{N}} is a sequence of non-increasing step-sizes. The problem is that typically, the marginal likelihood θ↦p​(y|θ)\theta\mapsto p(y|\theta) is intractable. The authors of (?, ?) manage to express

|  |  |  |
| --- | --- | --- |
|  | θ↦∇θlog⁡p​(y|θn)\theta\mapsto\nabla\_{\theta}\log~p(y|\theta\_{n}) |  |

of ([35](https://arxiv.org/html/2512.22109v1#A1.E35 "Equation 35 ‣ Appendix A Stochastic Approximation Proximal Gradient algorithm (SAPG) ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification")) through expectations, making the problem amenable to MCMC approaches, in essence, a stochastic gradient descent.

It is shown that for any θ∈Θ\theta\in\Theta

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇θlog⁡p​(y|θ)=∫ℝpp​(w|y,θ)​∇θlog⁡p​(w,y|θ)​𝑑w=−∫ℝpg​(w)​p​(w|y,θ)​𝑑w−∇θlog⁡(Z​(θ)),\begin{split}\nabla\_{\theta}\log p(y|\theta)&=\int\_{\mathbb{R}^{p}}p(w|y,\theta)\,\nabla\_{\theta}\log p(w,y|\theta)\,dw\\ &=-\int\_{\mathbb{R}^{p}}g(w)p(w|y,\theta)\,dw-\nabla\_{\theta}\log(\mathrm{Z}(\theta))\;,\end{split} |  | (36) |

where Z​(θ)\mathrm{Z}(\theta) is the normalizing constant of the prior distribution p​(w|θ)p(w|\theta), i.e.,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Z​(θ)=∫ℝpexp⁡(−θ​g​(w))​𝑑x.\mathrm{Z}(\theta)=\int\_{\mathbb{R}^{p}}\exp(-\theta\,g(w))dx\;. |  | (37) |

In particular, the expectation ∫ℝpg​(w)​p​(w|y,θ)​𝑑w\int\_{\mathbb{R}^{p}}g(w)\,p(w|y,\theta)\,dw is replaced by a Monte Carlo estimator targeting the prior, leading to the following gradient estimate, for any θ∈Θ,\theta\in\Theta,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δm,θ=1m​∑k=1m∇θlog⁡p​(Xk,y|θ)=−∇θlog⁡Z​(θ)−1m​∑k=1mg​(Xk),\Delta\_{m,\theta}=\frac{1}{m}\sum\_{k=1}^{m}\nabla\_{\theta}\log p(X\_{k},y|\theta)=-\nabla\_{\theta}\log\mathrm{Z}(\theta)-\frac{1}{m}\sum\_{k=1}^{m}g(X\_{k})\;, |  | (38) |

where (Xk)k∈{0,…,m}(X\_{k})\_{k\in\{0,\dots,m\}} is a sample of size m∈ℕm\in\mathbb{N} generated by using a Markov Chain targeting p​(w|y,θ)=p​(w,y|θ)/p​(y|θ)p(w|y,\theta)=p(w,y|\theta)/p(y|\theta), (in our MYULA scheme, this would actually be a regularized approximation of this density). Therefore, to compute θ⋆\theta\_{\star}, we can build a new sequence (θn)n∈ℕ(\theta\_{n})\_{n\in\mathbb{N}} associated with the following recursion

|  |  |  |  |
| --- | --- | --- | --- |
|  | θn+1=ΠΘ​[θn+δn+1​Δmn,θn],Δmn,θn=−∇θlog⁡Z​(θn)−1mn​∑k=1mng​(Xkn),\theta\_{n+1}=\Pi\_{\Theta}\,[\theta\_{n}+\delta\_{n+1}\Delta\_{m\_{n},\theta\_{n}}\,]\;,\qquad\Delta\_{m\_{n},\theta\_{n}}=-\nabla\_{\theta}\log\mathrm{Z}(\theta\_{n})-\frac{1}{m\_{n}}\sum\_{k=1}^{m\_{n}}g(X\_{k}^{n})\;, |  | (39) |

starting from some θ0∈Θ\theta\_{0}\in\Theta, and where (mn)n∈ℕ(m\_{n})\_{n\in\mathbb{N}} is a sequence of non-decreasing sample sizes. Under some assumptions on (mn)n∈ℕ,(δn)n∈ℕ(m\_{n})\_{n\in\mathbb{N}},\,(\delta\_{n})\_{n\in\mathbb{N}} and on the Markov kernels, the errors in the gradient estimates asymptotically average out and the algorithm converges to a maximizer of θ↦p​(y|θ)\theta\mapsto p(y|\theta). More precisely, as is standard (e.g., Polyak-Ruppert ideas) in stochastic approximation algorithms, given N∈ℕN\in\mathbb{N}, a sequence of non-increasing weights (ωn)n∈ℕ(\omega\_{n})\_{n\in\mathbb{N}}, and a sequence (θn)n=0N−1(\theta\_{n})\_{n=0}^{N-1} generated using ([39](https://arxiv.org/html/2512.22109v1#A1.E39 "Equation 39 ‣ Appendix A Stochastic Approximation Proximal Gradient algorithm (SAPG) ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification")), an approximate solution of ([32](https://arxiv.org/html/2512.22109v1#A1.E32 "Equation 32 ‣ Appendix A Stochastic Approximation Proximal Gradient algorithm (SAPG) ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification")) can be obtained by calculating the weighted average

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ¯N=∑n=0N−1ωnθn/∑n=0N−1ωn.\bar{\theta}\_{N}=\left.\sum\_{n=0}^{N-1}\omega\_{n}\theta\_{n}\middle/\sum\_{n=0}^{N-1}\omega\_{n}\right.\;. |  | (40) |

which converges asymptotically to a solution of ([32](https://arxiv.org/html/2512.22109v1#A1.E32 "Equation 32 ‣ Appendix A Stochastic Approximation Proximal Gradient algorithm (SAPG) ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification")) as N→∞N\rightarrow\infty.

The SAPG optimisation scheme in this work makes use of the MYULA approach described earlier. Accordingly, to draw samples from the posterior p​(w|y,θ)=p​(w,y|θ)/p​(y|θ)p(w|y,\theta)=p(w,y|\theta)/p(y|\theta), we will define a Markov chain (Xk)k∈ℕ(X\_{k})\_{k\in\mathbb{N}}, starting from X0∈ℝpX\_{0}\in\mathbb{R}^{p}, given by the recursion

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xk+1=Xk−δ​∇wf​(Xk)−δλ​{Xk−proxθ​gλ⁡(Xk)}+2​δ​Bk+1,X\_{k+1}=X\_{k}-\delta\nabla\_{w}f(X\_{k})-\frac{\delta}{\lambda}\left\{X\_{k}-\operatorname{prox}\_{\theta g}^{\lambda}(X\_{k})\right\}+\sqrt{2\delta}\,B\_{k+1}\;, |  | (41) |

where proxθ​gλ\operatorname{prox}\_{\theta g}^{\lambda} defined as in
([7](https://arxiv.org/html/2512.22109v1#S3.E7 "Equation 7 ‣ 3.1 Moreau–Yosida smoothing and proximal gradient structure ‣ 3 Proximal MCMC for the posterior ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification")), λ∈ℝ+\lambda\in\mathbb{R}^{+} is
the smoothing parameter for the Moreau-Yosida envelope of g, δ∈ℝ+\delta\in\mathbb{R}^{+} is the discretisation step-size
and (Bk)k∈ℕ∗(B\_{k})\_{k\in\mathbb{N}^{\*}} is a
sequence of i.i.d. pp-dimensional zero-mean Gaussian
random variables with an identity covariance matrix.

Last but not least, we would like to draw attention to the fact that to use ([39](https://arxiv.org/html/2512.22109v1#A1.E39 "Equation 39 ‣ Appendix A Stochastic Approximation Proximal Gradient algorithm (SAPG) ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification")) it is necessary to evaluate θ↦∇θlog⁡Z​(θ)\theta\mapsto\nabla\_{\theta}\log\mathrm{Z}(\theta). Generally, this cannot be computed exactly and has to be approximated; the authors in (?, ?) propose three different strategies to address such a calculation/approximation depending on whether gg is a homogeneous function or not. We will adapt their version for scalar parameters, multiplying a 1-homogeneous regulariser.555A function gg is α\alpha-positively homogeneous if there exists α∈ℝ\{0}\alpha\in\mathbb{R}\backslash\{0\} such that for any x∈ℝpx\in\mathbb{R}^{p} and t>0t>0, g​(t​x)=tα​g​(x)g(tx)=t^{\alpha}g(x). In this case, an easy calculation shows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​θ​log⁡Z​(θ)=−pθ.\frac{\textrm{d}}{\textrm{d}{\theta}}\log\mathrm{Z}(\theta)=-\frac{p}{\theta}. |  | (42) |

### A.1 Heuristic choice of the initial scale θ0\theta\_{0}

This section records the calculations that justify the heuristic (“method-of-moments”) choice of
θ0.\theta\_{0}.

On the FIT window, we compute an initial least–squares solution

|  |  |  |
| --- | --- | --- |
|  | wL​S′=Rc†​yc,w^{\prime}\_{LS}=R\_{c}^{\dagger}\;y\_{c}, |  |

which we project down666It is easy to see that the projector has the form PC​(w)=w−(𝟏⊤​w−1)p​𝟏P\_{C}(w)=w-\frac{(\mathbf{1}^{\top}w-1)}{p}\mathbf{1} to the affine hyperplane

|  |  |  |
| --- | --- | --- |
|  | 𝒞={w:𝟏⊤​w=1}\mathcal{C}=\{w:\mathbf{1}^{\top}w=1\} |  |

to obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | wLS=(wL​S)−(𝟏⊤​wL​S−1)p​ 1,w\_{\mathrm{LS}}=(w\_{LS})-\frac{\bigl(\mathbf{1}^{\top}w\_{LS}-1\bigr)}{p}\,\mathbf{1}, |  | (43) |

which satisfies the budget constraint.

Consider a weighted Laplace prior with independent coordinates,

|  |  |  |
| --- | --- | --- |
|  | π​(w∣θ)∝∏j=1pθ​αj2​exp⁡(−θ​αj​|wj|),\pi(w\mid\theta)\;\propto\;\prod\_{j=1}^{p}\frac{\theta\alpha\_{j}}{2}\exp\!\bigl(-\theta\alpha\_{j}|w\_{j}|\bigr), |  |

and “precision”
λj=θ​αj\lambda\_{j}=\theta\alpha\_{j}. For a scalar Laplace random variable
W∼Laplace​(0,1/λ)W\sim\mathrm{Laplace}(0,1/\lambda) we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​|W|=1λ⇒𝔼​[λ​|W|]=1.\mathbb{E}|W|\;=\;\frac{1}{\lambda}\quad\Rightarrow\quad\mathbb{E}[\lambda\;|W|]=1. |  |

Thus, under the prior above,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[θ​αj​|wj|]=1⇒𝔼​[θ​∑j=1pαj​|wj|]≈p.\mathbb{E}\bigl[\theta\alpha\_{j}|w\_{j}|\bigr]=1\quad\Rightarrow\quad\mathbb{E}\Bigl[\theta\sum\_{j=1}^{p}\alpha\_{j}|w\_{j}|\Bigr]\;\approx\;p. |  |

Informally: a “typical” draw from the prior satisfies

|  |  |  |
| --- | --- | --- |
|  | θ​∑j=1pαj​|wj|≈p.\theta\sum\_{j=1}^{p}\alpha\_{j}|w\_{j}|\approx p. |  |

Let wLSw\_{\mathrm{LS}} be a reference solution, e.g., ([43](https://arxiv.org/html/2512.22109v1#A1.E43 "Equation 43 ‣ A.1 Heuristic choice of the initial scale 𝜃₀ ‣ Appendix A Stochastic Approximation Proximal Gradient algorithm (SAPG) ‣ Index-Tracking Portfolio Construction and Rebalancing under Bayesian Sparse Modelling and Uncertainty Quantification")). We choose θ0\theta\_{0} so that wLSw\_{\mathrm{LS}} looks
like a *typical* draw from the Laplace prior in the sense of the
penalty scale. Concretely, we impose

|  |  |  |
| --- | --- | --- |
|  | θ0​∑j=1pαj​|(wLS)j|≈p,\theta\_{0}\sum\_{j=1}^{p}\alpha\_{j}|(w\_{\mathrm{LS}})\_{j}|\;\approx\;p, |  |

which yields the closed-form choice

|  |  |  |
| --- | --- | --- |
|  | θ0≈p∑j=1pαj​|(wLS)j|.\theta\_{0}\;\approx\;\frac{p}{\sum\_{j=1}^{p}\alpha\_{j}|(w\_{\mathrm{LS}})\_{j}|}. |  |

Because the weights αj\alpha\_{j} have been normalized to have mean
1p​∑j=1pαj≈1\frac{1}{p}\sum\_{j=1}^{p}\alpha\_{j}\approx 1, this can be seen as an
“average-scale” matching condition: by that we mean that, on average,
αj​|(wLS)j|\alpha\_{j}|(w\_{\mathrm{LS}})\_{j}| will roughly be of the same order as the
prior mean absolute value 1/θ01/\theta\_{0}.

A slightly different interpretation is to say that we are
choosing θ0\theta\_{0} so that there is about one unit of Laplace
penalty per coordinate:

|  |  |  |
| --- | --- | --- |
|  | θ0​∑jαj​|(wLS)j|≈p.\theta\_{0}\sum\_{j}\alpha\_{j}|(w\_{\mathrm{LS}})\_{j}|\approx p. |  |

In practice we do not use θ0\theta\_{0} completely unconstrained, but
regularise it as

|  |  |  |
| --- | --- | --- |
|  | θ0=max⁡{p∑j=1pαj​|(wLS)j|, 10−6},\theta\_{0}\;=\;\max\!\left\{\frac{p}{\sum\_{j=1}^{p}\alpha\_{j}|(w\_{\mathrm{LS}})\_{j}|},\,10^{-6}\right\}, |  |

and then constrain the SAPG updates to the box

|  |  |  |
| --- | --- | --- |
|  | θ∈Θ=[θ0/10, 10​θ0].\theta\in\Theta=[\theta\_{0}/10,\,10\,\theta\_{0}]. |  |

The lower bound 10−610^{-6} prevents θ0\theta\_{0} from becoming
numerically very small in cases where
∑jαj​|(wLS)j|\sum\_{j}\alpha\_{j}|(w\_{\mathrm{LS}})\_{j}| is very large (for example,
if wLSw\_{\mathrm{LS}} is noisy or poorly identified), which would
flatten the prior, reduce effective regularisation, and harm both
the identifiability of θ\theta and SAPG stability.

The interval [θ0/10,10​θ0][\theta\_{0}/10,10\,\theta\_{0}] encodes the belief that the
LS-matched θ0\theta\_{0} is accurate up to roughly one order of
magnitude. Within this range, the SAPG algorithm can adapt the scale
parameter to the data, but it is prevented from drifting to
*extremely* small values (prior almost flat, very high effective
dimension, ill-conditioned geometry) or to *extremely* large
values (e.g., prior overly spiky, weights nearly all shrunk to zero, inhomogeneous
posterior geometry).

## Appendix B Preconditioning and Metropolis-Hastings for the long MALA run

### B.1 Preconditioning

For future reference, ignoring constants, we record here the negative log–posterior with (σ^2,Λ,θ⋆)(\hat{\sigma}^{2},\Lambda,\theta\_{\star}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φθ⋆​(w)=fy​(w)+g​(w;θ⋆)=12​σ^2​‖yc−Rc​w‖22+Λ​(1⊤​w−1)2+θ⋆​∑j=1pαj​|wj|,\Phi\_{\theta\_{\star}}(w)=f\_{y}(w)+g(w;\theta\_{\star})=\frac{1}{2\hat{\sigma}^{2}}\,\|y\_{c}-R\_{c}w\|\_{2}^{2}+\Lambda(1^{\top}w-1)^{2}+\theta\_{\star}\sum\_{j=1}^{p}\alpha\_{j}|w\_{j}|, |  | (44) |

and with Φλ,θ⋆\Phi\_{\lambda,\,\theta\_{\star}} its smoothed analogue, defined by replacing gg with its MY–envelope,

|  |  |  |
| --- | --- | --- |
|  | gλ​(w)=minu⁡{12​λ​‖w−u‖22+θ⋆​∑jαj​|uj|},i.e.​Φλ,θ⋆​(w)=fy​(w)+gλ,θ⋆​(w).g\_{\lambda}(w)=\min\_{u}\left\{\frac{1}{2\lambda}\|w-u\|\_{2}^{2}+\theta\_{\star}\sum\_{j}\alpha\_{j}|u\_{j}|\right\},\quad\text{i.e.}\;\;\Phi\_{\lambda,\,\theta\_{\star}}(w)=f\_{y}(w)+g\_{\lambda,\,\theta\_{\star}}(w). |  |

To counteract the slow mixing in MALA, due to the stiff likelihood, we adopt a diagonal (Jacobi) preconditioner, P,P,

|  |  |  |
| --- | --- | --- |
|  | P=D−1/2,where,D=diag⁡(1σ^2​diag⁡(R⊤​R)+ 2​Λ).P=D^{-1/2},\quad\text{where,}\quad D=\operatorname{diag}\!\Big(\frac{1}{\hat{\sigma}^{2}}\operatorname{diag}(R^{\top}R)\;+\;2\Lambda\Big). |  |

This essentially results in a variable-metric MYULA update with metric P−2P^{-2}, which amounts to rescaling the gradient and the Moreau term, coordinate-wise. We *retune* the steps by recomputing the Lipschitz bound in the preconditioned geometry,

|  |  |  |
| --- | --- | --- |
|  | Lpre=λmax​(P​A​P),A=1σ^2​R⊤​R+2​Λ​ 11⊤,L\_{\mathrm{pre}}=\lambda\_{\max}(PAP),\quad A=\tfrac{1}{\hat{\sigma}^{2}}R^{\top}R+2\Lambda\,\bm{1}\bm{1}^{\top}, |  |

with the same principled formulas as with our main MYULA approach, i.e.,

|  |  |  |
| --- | --- | --- |
|  | λMYpre=1Lpre,δpre=0.92​Lpre.\lambda\_{\mathrm{MY}}^{\mathrm{pre}}=\frac{1}{L\_{\mathrm{pre}}},\qquad\delta^{\mathrm{pre}}=\frac{0.9}{2L\_{\mathrm{pre}}}. |  |

This preserves the target posterior and helps in substantially increasing the ESS, and also exhibits much improved autocorrelation decay. Moreover, being diagonal, it is cheap to compute.

With this choice, the preconditioned MALA proposal reads

|  |  |  |
| --- | --- | --- |
|  | w′=w−δpre​P2​∇Φλ,θ⋆​(w)+2​δpre​P​ξ,ξ∼𝒩​(0,Ip).w^{\prime}=w-\delta^{\mathrm{pre}}P^{2}\nabla\Phi\_{\lambda,\,\theta\_{\star}}(w)+\sqrt{2\delta^{\mathrm{pre}}}\,P\,\xi,\quad\xi\sim\mathcal{N}(0,I\_{p}). |  |

### B.2 MALA–style proposal

Given the current state ww, the proposal is

|  |  |  |
| --- | --- | --- |
|  | w′∼𝒩​(m​(w), 2​δpre​P2),m​(w)=w−δpre​P2​∇Φλ​(w).w^{\prime}\;\sim\;\mathcal{N}\!\Big(m(w),\,2\delta^{\mathrm{pre}}\,P^{2}\Big),\qquad m(w)\;=\;w-\delta^{\mathrm{pre}}\,P^{2}\,\nabla\Phi\_{\lambda}(w). |  |

This is the preconditioned MYULA step wrapped in a Metropolis–Hastings correction so that the chain is *exact* for πλ,θ⋆\pi\_{\lambda,\theta\_{\star}}.

Let q​(w′∣w)=𝒩​(w′;m​(w), 2​δ​P2)q(w^{\prime}\mid w)=\mathcal{N}(w^{\prime};\,m(w),\,2\delta P^{2}). The MH acceptance ratio is

|  |  |  |
| --- | --- | --- |
|  | log⁡α​(w,w′)=−Φλ,θ⋆​(w′)+Φλ,θ⋆​(w)−14​δ​(‖w−m​(w′)‖(P2)−12−‖w′−m​(w)‖(P2)−12),\log\alpha(w,w^{\prime})\;=\;-\Phi\_{\lambda,\,\theta\_{\star}}(w^{\prime})+\Phi\_{\lambda,\,\theta\_{\star}}(w)\;-\;\frac{1}{4\delta}\,\Big(\|w-m(w^{\prime})\|\_{\left(P^{2}\right)^{-1}}^{2}-\|w^{\prime}-m(w)\|\_{(P^{2})^{-1}}^{2}\Big), |  |

where ‖v‖(P2)−12=∑jvj2/pj2\|v\|\_{(P^{2})^{-1}}^{2}=\sum\_{j}v\_{j}^{2}/p\_{j}^{2} is the (squared) Mahalanobis norm in metric (P2)−1(P^{2})^{-1}.
We accept with probability α​(w,w′)=min⁡{1,exp⁡(log⁡α)}\alpha(w,w^{\prime})=\min\{1,\exp(\log\alpha)\}.

## Appendix C Noise variance estimation

As part of the model setup, we pre-estimate the noise variance σ2\sigma^{2}, which appears as a parameter in the likelihood. We tested several estimators and narrowed the choice down to the *median absolute deviation* (MAD) estimator (?, ?) and the *classical residual variance estimator*; we chose the former because of its robustness to outliers. Both operate on the residuals of the regression model. However, note that the budget constraint
1⊤​w=11^{\top}w=1
*does not enter* the variance estimation at all: we work with the unconstrained OLS fit and its residuals. The rationale is that
σ^2\widehat{\sigma}^{2} should reflect the scale of the *tracking
error* yt−rt⊤​wy\_{t}-r\_{t}^{\top}w under a purely data-driven fit, without being distorted by how we choose to enforce the budget constraint. The constraint is imposed later, at the level of the prior
and posterior geometry, but not in the noise-scale estimation.

#### Median Absolute Deviation estimator (MAD)-based variance estimation

We work with the centred index-tracking regression

|  |  |  |  |
| --- | --- | --- | --- |
|  | yt=rt⊤​w+εt,t=1,…,T,y\_{t}\;=\;r\_{t}^{\top}w\;+\;\varepsilon\_{t},\qquad t=1,\dots,T, |  | (45) |

where yty\_{t} is the (centred) index return, rt∈ℝpr\_{t}\in\mathbb{R}^{p} is the (centred) vector of asset returns,
w∈ℝpw\in\mathbb{R}^{p} is the portfolio weight vector, and the noise is assumed i.i.d.

|  |  |  |  |
| --- | --- | --- | --- |
|  | εt∼𝒩​(0,σ2).\varepsilon\_{t}\sim\mathcal{N}(0,\sigma^{2}). |  | (46) |

Let y∈ℝTy\in\mathbb{R}^{T} and R∈ℝT×pR\in\mathbb{R}^{T\times p} denote the stacked observations
after centring,

|  |  |  |
| --- | --- | --- |
|  | yc=(y1,…,yT)⊤,Rc=[r1⊤⋮rT⊤],y\_{c}=(y\_{1},\dots,y\_{T})^{\top},\qquad R\_{c}=\begin{bmatrix}r\_{1}^{\top}\\ \vdots\\ r\_{T}^{\top}\end{bmatrix}, |  |

so that the model can be written compactly as

|  |  |  |  |
| --- | --- | --- | --- |
|  | yc=Rc​w+ε,ε∼𝒩​(0,σ2​IT).y\_{c}\;=\;R\_{c}w+\varepsilon,\qquad\varepsilon\sim\mathcal{N}(0,\sigma^{2}I\_{T}). |  | (47) |

##### Step 1: unconstrained least-squares fit.

The variance estimator is based on residuals from the *unconstrained*
ordinary least-squares (OLS) fit,

|  |  |  |  |
| --- | --- | --- | --- |
|  | w^OLS∈arg⁡minw∈ℝp⁡12​∥yc−Rc​w∥22.\widehat{w}\_{\mathrm{OLS}}\;\in\;\arg\min\_{w\in\mathbb{R}^{p}}\frac{1}{2}\,\lVert y\_{c}-R\_{c}w\rVert\_{2}^{2}. |  | (48) |

In practice we compute w^OLS\widehat{w}\_{\mathrm{OLS}}
via a pseudoinverse or least-squares solver, e.g.

|  |  |  |  |
| --- | --- | --- | --- |
|  | w^OLS=Rc†​yc=(Rc⊤​Rc)−1​Rc⊤​yc.\widehat{w}\_{\mathrm{OLS}}=R\_{c}^{\dagger}\,y\_{c}=(R\_{c}^{\top}R\_{c})^{-1}R\_{c}^{\top}\,y\_{c}. |  | (49) |

##### Step 2: residuals.

Define the OLS residuals

|  |  |  |  |
| --- | --- | --- | --- |
|  | r^t=yt−rt⊤​w^OLS,t=1,…,T,\widehat{r}\_{t}\;=\;y\_{t}-r\_{t}^{\top}\widehat{w}\_{\mathrm{OLS}},\qquad t=1,\dots,T, |  | (50) |

and collect them into r^∈ℝT\widehat{r}\in\mathbb{R}^{T}.
Under the Gaussian model, and ignoring estimation error in
w^OLS\widehat{w}\_{\mathrm{OLS}}, these residuals behave approximately like
realizations of εt\varepsilon\_{t} and are therefore informative about σ2\sigma^{2}.

##### Step 3: MAD and a robust scale estimate.

The MAD of a sample
x1,…,xTx\_{1},\dots,x\_{T} is

|  |  |  |  |
| --- | --- | --- | --- |
|  | MAD​(x1,…,xT)=median1≤t≤T|xt−median1≤s≤Txs|.\mathrm{MAD}(x\_{1},\dots,x\_{T})\;=\;\operatorname\*{median}\_{1\leq t\leq T}\,\bigl|\;x\_{t}-\operatorname\*{median}\_{1\leq s\leq T}x\_{s}\;\bigr|. |  | (51) |

If X∼𝒩​(0,σ2)X\sim\mathcal{N}(0,\sigma^{2}) then

|  |  |  |
| --- | --- | --- |
|  | MAD​(X1,…,XT)≈σ​Φ−1​(0.75),\mathrm{MAD}(X\_{1},\dots,X\_{T})\;\approx\;\sigma\,\Phi^{-1}(0.75), |  |

where Φ−1\Phi^{-1} is the standard normal quantile function.
Thus a consistent estimator of σ\sigma is

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ^MAD=cMAD​MAD​(r^1,…,r^T),cMAD=1Φ−1​(0.75)≈1.4826.\widehat{\sigma}\_{\mathrm{MAD}}\;=\;c\_{\mathrm{MAD}}\;\mathrm{MAD}(\widehat{r}\_{1},\dots,\widehat{r}\_{T}),\qquad c\_{\mathrm{MAD}}=\frac{1}{\Phi^{-1}(0.75)}\approx 1.4826. |  | (52) |

Our working variance estimate is then

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ^2=σ^MAD2=(1.4826×MAD​(r^1,…,r^T))2.\widehat{\sigma}^{2}\;=\;\widehat{\sigma}\_{\mathrm{MAD}}^{2}\;=\;\bigl(1.4826\times\mathrm{MAD}(\widehat{r}\_{1},\dots,\widehat{r}\_{T})\bigr)^{2}. |  | (53) |