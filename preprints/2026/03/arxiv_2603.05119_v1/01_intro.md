---
authors:
- Sourojyoti Barick
doc_id: arxiv:2603.05119v1
family_id: arxiv:2603.05119
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Asymptotic Separability of Diffusion and Jump Components in High-Frequency
  CIR and CKLS Models
url_abs: http://arxiv.org/abs/2603.05119v1
url_html: https://arxiv.org/html/2603.05119v1
venue: arXiv q-fin
version: 1
year: 2026
---


Sourojyoti Barick
  
Interdisciplinary Statistical Research Unit, Indian Statistical Institute, Kolkata

###### Abstract

This paper develops a robust parametric framework for jump detection in discretely observed CKLS-type jump–diffusion processes with high-frequency asymptotics, based on the minimum density power divergence estimator (MDPDE). The methodology exploits the intrinsic asymptotic scale separation between diffusion increments, which decay at rate Δn\sqrt{\Delta\_{n}}, and jump increments, which remain of non-vanishing stochastic magnitude. Using robust MDPDE-based estimators of the drift and diffusion coefficients, we construct standardized residuals whose extremal behavior provides a principled basis for statistical discrimination between continuous and discontinuous components. We establish that, over diffusion intervals, the maximum of the normalized residuals converges to the Gumbel extreme-value distribution, yielding an explicit and asymptotically valid detection threshold. Building on this result, we prove classification consistency of the proposed robust detection procedure: the probability of correctly identifying all jump and diffusion increments converges to one under proper asymptotics. The MDPDE-based normalization attenuates the influence of atypical increments and stabilizes the detection boundary in the presence of discontinuities. Simulation results confirm that robustness improves finite-sample stability and reduces spurious detections without compromising asymptotic validity. The proposed methodology provides a theoretically rigorous and practically resilient robust approach to jump identification in high-frequency stochastic systems.

## 1 Introduction

Stochastic differential equations (SDEs) constitute a fundamental mathematical
framework for modeling dynamically evolving systems subject to random
perturbations. In financial econometrics, such models play a central role in the
analysis of interest rate dynamics, asset prices, and volatility processes.
Among the most prominent specifications, the Cox–Ingersoll–Ross (CIR) process,
introduced by [[undefh](#bib.bibx9)], has received considerable attention due to its
ability to capture mean-reverting behavior while preserving strict positivity
of the state variable. The CIR model arises as a special case of the more
general Chan–Karolyi–Longstaff–Sanders (CKLS) model proposed by
[[undefg](#bib.bibx8)], which provides a flexible parametric family capable of
accommodating empirically observed features such as
state-dependent volatility, and heterogeneous diffusion elasticities.

The empirical relevance of mean–reverting diffusion processes in interest rate modeling is well established. Short-term interest rates exhibit a persistent tendency to revert toward a stochastic equilibrium level, reflecting macroeconomic fundamentals, monetary policy interventions, and market expectations. Such dynamics are naturally represented by continuous-time diffusion models, which provide a parsimonious and analytically tractable description of short-rate evolution. These models form the structural foundation of modern arbitrage-free term structure theory and have been systematically incorporated within general no-arbitrage frameworks; see, for example, [[undefn](#bib.bibx15)] and [[undefk](#bib.bibx12)]. Since derivative valuation, hedging, and risk management depend explicitly on the drift and diffusion coefficients governing the underlying rate dynamics, reliable statistical inference for discretely observed diffusions is essential. This has motivated extensive research on statistically efficient estimation procedures, most notably maximum likelihood estimation (MLE) and conditional least squares (CLS), which provide consistent and asymptotically normal estimators under high-frequency sampling schemes.

Early contributions to the statistical inference of the CIR process include the
work of [[undefx](#bib.bibx25)], who proposed CLS-type estimators and established
their strong consistency under both discrete and continuous observation schemes.
Subsequent investigations, including [[undefa](#bib.bibx2)] and [[undefb](#bib.bibx3)],
demonstrated that likelihood-based methods generally exhibit superior finite-sample
and asymptotic efficiency relative to CLS estimators, particularly under high-frequency
sampling regimes. These studies established consistency, asymptotic normality,
and improved efficiency properties of maximum likelihood estimators, especially
in regimes where the process approaches boundary regions. Extensions to the
more general CKLS framework were provided by [[undefu](#bib.bibx22)], who derived
asymptotic properties of CLS estimators under relaxed regularity conditions and
more general diffusion structures. Alternative inferential paradigms, including
Bayesian estimation procedures incorporating prior structural information, were
developed by [[undefl](#bib.bibx13)], offering enhanced inferential stability in
small-sample environments.

Despite their widespread applicability, classical diffusion models rely
fundamentally on the assumption that the underlying stochastic process evolves
continuously over time. However, empirical evidence from high-frequency
financial data unequivocally demonstrates the presence of discontinuities, or
*jumps*, arising from macroeconomic announcements, liquidity shocks,
institutional trading, and other structural market events. These observations
have motivated the development of jump–diffusion models, which augment the
continuous diffusion component with a discontinuous pure-jump process; see,
for example, the seminal contributions of [[undefv](#bib.bibx23)] and
[[undefj](#bib.bibx11)].

From a statistical standpoint, the presence of jumps introduces profound
challenges for inference. Under high frequency asymptotics, diffusion-driven increments
scale at rate 𝒪​(Δ​t)\mathcal{O}(\sqrt{\Delta t}), whereas jump-induced increments
remain of order 𝒪​(1)\mathcal{O}(1). This fundamental disparity in asymptotic
scaling provides the theoretical basis for statistical discrimination between
continuous and discontinuous components, and has motivated a substantial body
of literature devoted to jump detection and decomposition of semimartingale
dynamics.

Pioneering work by
[[undefd](#bib.bibx5), [undefe](#bib.bibx6)] introduced
nonparametric jump detection procedures based on realized variation measures,
exploiting the distinct asymptotic behavior of quadratic and bipower variation
in the presence of jumps. These methods were further developed by
[[undefo](#bib.bibx16)] and [[undef](#bib.bibx1)], who established rigorous
limit theorems and consistent statistical tests for detecting discontinuities
under general semimartingale models. A particularly influential contribution is
the locally normalized jump detection statistic proposed by
[[undeft](#bib.bibx21)], which converges weakly to a standard Gaussian
distribution in the absence of jumps while exhibiting divergent behavior in the
presence of discontinuities. This framework provides a statistically tractable
and asymptotically justified mechanism for identifying jump occurrences in
high-frequency observations.

Notwithstanding these advances, most existing jump detection methodologies are
formulated within a fully nonparametric framework and do not explicitly exploit
the structural information inherent in parametric diffusion models. In many
practical applications, parametric models such as the CIR and CKLS processes
remain indispensable due to their interpretability, tractability, and relevance
for structural and forecasting purposes. A common empirical strategy consists
of applying nonparametric jump detection procedures as a preliminary filtering
step, followed by parametric estimation based on the filtered sample. However,
such two-stage procedures introduce additional stochastic variability and are
inherently vulnerable to misclassification errors, which may propagate into the
parameter estimation stage and degrade statistical efficiency.

A central inferential challenge arises from the intrinsic sensitivity of
likelihood-based estimators to contamination by jump-induced increments.
Classical likelihood and quasi-likelihood methods assign quadratic penalties to
large deviations under Gaussian approximations, rendering them highly sensitive
to atypical observations. Consequently, even a relatively small number of jumps
may exert disproportionate influence on the resulting parameter estimates,
leading to bias, inefficiency, and instability in inference. This phenomenon has
been rigorously analyzed in the context of discretely observed diffusions; see,
for example, [[undefz](#bib.bibx27)], [[undefq](#bib.bibx18)], and
[[undefy](#bib.bibx26)].

These limitations underscore the necessity of robust statistical methodologies
capable of mitigating the influence of contamination while retaining asymptotic
efficiency under the correctly specified model. A principled and theoretically
well-founded approach is provided by divergence-based estimation methods, which
replace the classical likelihood function with a discrepancy functional between
the empirical and model-implied distributions. In particular, the minimum
density power divergence estimator introduced by [[undeff](#bib.bibx7)] provides a
continuous interpolation between maximum likelihood estimation and highly robust
procedures through a tuning parameter controlling the trade-off between
efficiency and robustness.

Density power divergence estimators possess several desirable theoretical
properties, including consistency, asymptotic normality, and bounded influence
functions, rendering them particularly suitable for inference in the presence of
contamination or model misspecification. Their statistical properties have been
extensively investigated in both independent and dependent data settings; see,
for example, [[undefm](#bib.bibx14)] and [[undefs](#bib.bibx20)]. In the context of
discretely observed diffusion processes, divergence-based methods provide a
natural and theoretically justified mechanism for attenuating the influence of
jump-induced increments, which manifest as localized deviations from the
continuous diffusion dynamics.

Motivated by these considerations, the present paper develops a unified
parametric framework for robust jump identification and parameter estimation in
CKLS-type diffusion models. The proposed methodology integrates robust
divergence-based estimation with a statistically principled jump identification
mechanism derived from the asymptotic behavior of locally normalized residuals.
This approach provides a coherent inferential framework that simultaneously
achieves robust parameter estimation and consistent jump detection within a
fully parametric setting.

The remainder of the paper is organized as follows. Section [2](#S2 "2 Theoretical Background and Illustration ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models")
reviews the parametric CKLS model and summarizes existing results on consistency
and asymptotic normality of classical estimators. Section [2.1](#S2.SS1 "2.1 Robust Estimation via Density Power Divergence ‣ 2 Theoretical Background and Illustration ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models")
introduces the proposed robust estimation framework and establishes its
asymptotic properties. Section [3](#S3 "3 Proposed Test for Jump ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models") develops a statistically
rigorous jump detection procedure and derives the associated asymptotic
critical thresholds. Section [4](#S4 "4 Simulation Study ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models") presents simulation studies illustrating
the finite-sample performance of the proposed methodology. Concluding remarks
are provided in Section [5](#S5 "5 Conclusion ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models"). All technical proofs and auxiliary results
are deferred to Appendix [A](#A1 "Appendix A Appendix ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models"), with additional simulation results provided
in the Supplementary Material.

## 2 Theoretical Background and Illustration

This section summarizes the probabilistic framework and classical asymptotic
results that form the benchmark for the robust methodology developed later.
All statements are standard and included only to fix notation and clarify the
reference model. Detailed derivations can be found in the cited literature.

We consider the CKLS diffusion process introduced by
[[undefg](#bib.bibx8)],

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=(β1−β2​Xt)​d​t+σ​Xtγ​d​Wt,dX\_{t}=(\beta\_{1}-\beta\_{2}X\_{t})\,dt+\sigma X\_{t}^{\gamma}\,dW\_{t}, |  | (1) |

where γ∈[1/2,1]\gamma\in[1/2,1] and (Wt)(W\_{t}) is a standard Brownian motion.Throughout the paper we impose the following standing conditions.

###### Assumption 1.

The parameters satisfy β1>0\beta\_{1}>0, β2>0\beta\_{2}>0, and σ>0\sigma>0, and the
initial condition satisfies X0>0X\_{0}>0.

The ergodic and boundary properties of ([1](#S2.E1 "In 2 Theoretical Background and Illustration ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models")) are well understood; see
[[undefg](#bib.bibx8)], [[undefp](#bib.bibx17)], and [[undefc](#bib.bibx4)]. Under
Assumption [1](#Thmassumption1 "Assumption 1. ‣ 2 Theoretical Background and Illustration ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models"), the process admits a unique stationary distribution.
The boundary at zero is unattainable for γ∈(1/2,1]\gamma\in(1/2,1], while in the
boundary case γ=1/2\gamma=1/2 unattainability holds provided 2​β1>σ22\beta\_{1}>\sigma^{2}.
The stationary density takes the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(r)=C​(γ)​r−2​γ​exp⁡{Q​(r;γ)},f(r)=C(\gamma)\,r^{-2\gamma}\exp\{Q(r;\gamma)\}, |  | (2) |

where Q​(⋅;γ)Q(\cdot;\gamma) is determined by the scale and speed measures.

To motivate the estimation framework, consider first the CIR specification
(γ=1/2\gamma=1/2),

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=(β1−β2​Xt)​d​t+σ​Xt​d​Wt,dX\_{t}=(\beta\_{1}-\beta\_{2}X\_{t})\,dt+\sigma\sqrt{X\_{t}}\,dW\_{t}, |  | (3) |

introduced by [[undefh](#bib.bibx9)]. Let {Xti}i=0n\{X\_{t\_{i}}\}\_{i=0}^{n} denote observations on
an equidistant grid with mesh Δn\Delta\_{n}. The Euler–Maruyama approximation
([[undefr](#bib.bibx19)]) yields

|  |  |  |
| --- | --- | --- |
|  | Xt+Δn=Xt+(β1−β2​Xt)​Δn+σ​Xt​Δ​Wt.X\_{t+\Delta\_{n}}=X\_{t}+(\beta\_{1}-\beta\_{2}X\_{t})\Delta\_{n}+\sigma\sqrt{X\_{t}}\Delta W\_{t}. |  |

Define

|  |  |  |
| --- | --- | --- |
|  | yt=Xt+Δn−XtXt​Δn,z1​t=ΔnXt,z2​t=−Xt​Δn.y\_{t}=\frac{X\_{t+\Delta\_{n}}-X\_{t}}{\sqrt{X\_{t}\Delta\_{n}}},\qquad z\_{1t}=\frac{\sqrt{\Delta\_{n}}}{\sqrt{X\_{t}}},\qquad z\_{2t}=-\sqrt{X\_{t}\Delta\_{n}}. |  |

Then the discretized model admits the linear representation

|  |  |  |  |
| --- | --- | --- | --- |
|  | yt=β1​z1​t+β2​z2​t+εt,εt=σΔn​Δ​Wt,y\_{t}=\beta\_{1}z\_{1t}+\beta\_{2}z\_{2t}+\varepsilon\_{t},\qquad\varepsilon\_{t}=\frac{\sigma}{\sqrt{\Delta\_{n}}}\Delta W\_{t}, |  | (4) |

which forms the basis for classical inference in discretely observed
diffusions; see [[undefq](#bib.bibx18)] and [[undefi](#bib.bibx10)].
Let 𝜷^n\hat{\bm{\beta}}\_{n} denote the OLS estimator associated with
([4](#S2.E4 "In 2 Theoretical Background and Illustration ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models")), and let σ^n2\widehat{\sigma}\_{n}^{2} denote the corresponding
residual variance estimator.

We consider the high-frequency asymptotic regime

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δn→0,n​Δn→∞,\Delta\_{n}\to 0,\qquad n\Delta\_{n}\to\infty, |  | (5) |

under which the observation grid becomes increasingly dense as the sample
size grows. This framework corresponds to an infill asymptotic scheme, where
the time discretization is progressively refined while the observation horizon
diverges.

Under ([5](#S2.E5 "In 2 Theoretical Background and Illustration ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models")), standard martingale arguments imply consistency and
asymptotic normality of the estimators.

###### Result 1 (Consistency).

𝜷^n→ℙ𝜷,σ^n2→ℙσ2.\hat{\bm{\beta}}\_{n}\xrightarrow{\mathbb{P}}\bm{\beta},\qquad\widehat{\sigma}\_{n}^{2}\xrightarrow{\mathbb{P}}\sigma^{2}.

###### Result 2 (Asymptotic normality).

n​Δnσ^n​(𝜷^n−𝜷)→𝒟𝒩​(0,Σ−1),\frac{\sqrt{n\Delta\_{n}}}{\widehat{\sigma}\_{n}}\left(\hat{\bm{\beta}}\_{n}-\bm{\beta}\right)\xrightarrow{\mathcal{D}}\mathcal{N}\!\left(0,\Sigma^{-1}\right),
where Σ\Sigma depends on moments of the stationary distribution; see
[[undefq](#bib.bibx18)].

For the CIR case,

|  |  |  |
| --- | --- | --- |
|  | Σ=(β2β1−σ2/2−1−1β1β2),\Sigma=\begin{pmatrix}\frac{\beta\_{2}}{\beta\_{1}-\sigma^{2}/2}&-1\\ -1&\frac{\beta\_{1}}{\beta\_{2}}\end{pmatrix}, |  |

while for the general CKLS model,

|  |  |  |
| --- | --- | --- |
|  | Σ=(∫0∞r−2​γ​f​(r)​𝑑r−∫0∞r1−2​γ​f​(r)​𝑑r−∫0∞r1−2​γ​f​(r)​𝑑r∫0∞r2−2​γ​f​(r)​𝑑r).\Sigma=\begin{pmatrix}\int\_{0}^{\infty}r^{-2\gamma}f(r)\,dr&-\int\_{0}^{\infty}r^{1-2\gamma}f(r)\,dr\\[6.0pt] -\int\_{0}^{\infty}r^{1-2\gamma}f(r)\,dr&\int\_{0}^{\infty}r^{2-2\gamma}f(r)\,dr\end{pmatrix}. |  |

Under infill asymptotics, both the ordinary least squares estimator and the Gaussian
quasi–maximum likelihood estimator are consistent for the same true parameter
vector; see [[undefi](#bib.bibx10)] and [[undefw](#bib.bibx24)]. Since both
estimators converge in probability to the identical deterministic limit,
their difference must vanish asymptotically. Consequently, the preceding
results apply equally to the likelihood-based estimator.

The preceding asymptotic analysis is derived under the Gaussian increment
structure implied by the pure diffusion specification. This structure ensures
local quadratic approximation of the likelihood and yields the standard
quasi-likelihood estimating equations. In empirical applications, however,
high-frequency financial series often display excess kurtosis and abrupt
movements incompatible with the Gaussian benchmark. Since least squares and
Gaussian quasi-likelihood estimators weight all increments equally, their
finite-sample behavior may be adversely affected by atypically large
increments. This consideration motivates an alternative estimating framework that
retains consistency under the diffusion model while reducing the influence
of extreme observations.

### 2.1 Robust Estimation via Density Power Divergence

To formalize robustness, we replace the Gaussian quasi-likelihood criterion
by a density power divergence objective in the sense of [[undeff](#bib.bibx7)].
Let f𝜽f\_{\bm{\theta}} denote the working Gaussian increment density.
For α≥0\alpha\geq 0, the density power divergence between the empirical
distribution and f𝜽f\_{\bm{\theta}} yields the estimating criterion

|  |  |  |
| --- | --- | --- |
|  | ℒn(α)​(𝜽)=1n​∑i=1n{∫f𝜽1+α​(x)​𝑑x−(1+1α)​f𝜽α​(Xi)+1α},\mathcal{L}\_{n}^{(\alpha)}(\bm{\theta})=\frac{1}{n}\sum\_{i=1}^{n}\left\{\int f\_{\bm{\theta}}^{1+\alpha}(x)\,dx-\left(1+\frac{1}{\alpha}\right)f\_{\bm{\theta}}^{\alpha}(X\_{i})+\frac{1}{\alpha}\right\}, |  |

with the usual likelihood recovered at α=0\alpha=0.

The resulting minimum density power divergence estimator (MDPDE)
downweights increments with small model-implied density and therefore
limits the influence of extreme observations while preserving
consistency under correct specification.

Let θ=(β1,β2,σ)⊤\theta=(\beta\_{1},\beta\_{2},\sigma)^{\top} denote the vector of unknown
parameters, and consider the Gaussian conditional density associated with the
Euler discretization of the diffusion process,

|  |  |  |
| --- | --- | --- |
|  | fθ​(yt∣Xt)=12​π​σ​exp⁡(−(yt−β1​z1​t−β2​z2​t)22​σ2),f\_{\theta}(y\_{t}\mid X\_{t})=\frac{1}{\sqrt{2\pi}\sigma}\exp\!\left(-\frac{(y\_{t}-\beta\_{1}z\_{1t}-\beta\_{2}z\_{2t})^{2}}{2\sigma^{2}}\right), |  |

where XtX\_{t} denotes the available conditioning information at time tt and
(z1​t,z2​t)(z\_{1t},z\_{2t}) are the corresponding regressors. This Gaussian approximation
serves as a working model for the conditional distribution of the increments and
constitutes the basis for both classical and robust inference.

For a robustness tuning parameter α>0\alpha>0, the empirical density power
divergence objective function is defined as

|  |  |  |
| --- | --- | --- |
|  | Hn(α)​(θ)=∑t=1n[∫fθ1+α​(y∣Xt)​𝑑y−1+αα​fθα​(yt∣Xt)+1α].H\_{n}^{(\alpha)}(\theta)=\sum\_{t=1}^{n}\left[\int f\_{\theta}^{1+\alpha}(y\mid X\_{t})\,dy-\frac{1+\alpha}{\alpha}f\_{\theta}^{\alpha}(y\_{t}\mid X\_{t})+\frac{1}{\alpha}\right]. |  |

The first term acts as a normalization component that depends only on the model,
while the second term downweights observations that are unlikely under the
postulated conditional density. As α↓0\alpha\downarrow 0, the criterion
Hn(α)​(θ)H\_{n}^{(\alpha)}(\theta) converges to the negative log-likelihood, and the
corresponding estimator reduces to the classical maximum likelihood estimator.

The MDPDE is then defined as

|  |  |  |
| --- | --- | --- |
|  | θ^n(α)=arg⁡minθ∈Θ⁡Hn(α)​(θ),\hat{\theta}\_{n}^{(\alpha)}=\arg\min\_{\theta\in\Theta}H\_{n}^{(\alpha)}(\theta), |  |

where Θ\Theta denotes the parameter space. The tuning parameter α\alpha
controls the trade-off between robustness and efficiency, with larger values of
α\alpha yielding increased resistance to outliers at the cost of some loss in
efficiency under the correctly specified Gaussian model.

###### Result 3 (Asymptotic properties of the MDPDE).

Suppose the regularity conditions of [[undefs](#bib.bibx20)] hold and the sampling
scheme satisfies the infill asymptotic regime ([5](#S2.E5 "In 2 Theoretical Background and Illustration ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models")). If in addition, n​(Δn)q→0for some ​q>1,n(\Delta\_{n})^{q}\to 0\quad\text{for some }q>1,
holds, then the minimum density power divergence estimator satisfies

|  |  |  |
| --- | --- | --- |
|  | θ^n(α)→ℙθ0,\hat{\theta}\_{n}^{(\alpha)}\xrightarrow{\mathbb{P}}\theta\_{0}, |  |

where θ0\theta\_{0} denotes the true parameter value. Furthermore, if n​(Δn)2→0,n(\Delta\_{n})^{2}\to 0,
the estimator is asymptotically normal with covariance matrix given explicitly
in [[undefs](#bib.bibx20)].

###### Remark 1.

A fundamental property of the minimum density power divergence estimator is its
bounded influence function, which ensures stability in the presence of atypically
large observations. In discretely observed diffusion models, unusually large
increments may arise from unmodeled jump components or mild departures from the
pure diffusion specification. Unlike classical likelihood-based estimators,
whose influence functions are unbounded, the MDPDE automatically downweights such
increments and prevents them from dominating the estimating equations. As a
result, systematic discrepancies between classical and robust estimators provide
a natural diagnostic signal of structural misspecification, including the presence
of jumps.

This distinction is particularly relevant in high-frequency settings. Diffusion
sample paths are almost surely continuous, and their increments vanish at the
rate Δn\sqrt{\Delta\_{n}} as Δn→0\Delta\_{n}\to 0, whereas jump-induced increments remain
of finite magnitude. Consequently, jump increments appear as local outliers
relative to the continuous diffusion dynamics and may exert disproportionate
influence on likelihood-based procedures, often leading to biased or unstable
estimates. Robust divergence-based estimators mitigate this effect by limiting
the contribution of extreme observations and thereby preserving stability and
interpretability of the fitted model.

An additional advantage arises in constrained parametric models, where extreme
increments may drive likelihood-based estimates toward the boundary of the
parameter space, potentially violating structural conditions such as positivity
or ergodicity. By attenuating the influence of atypical observations, robust
estimation maintains numerical stability and ensures that the estimated parameters
remain within economically and statistically meaningful regimes.

![Refer to caption](2603.05119v1/image/likelihood_plot.png)


(a) Pointwise contribution (influence) of standardized increments under jump contamination for different values of the robustness parameter α\alpha. Diffusion-driven increments are shown in gray, while jump-induced increments are shown in red.

![Refer to caption](2603.05119v1/image/pointwise_dnorm_using_different_alpha.png)


(b) Gaussian likelihood values φ​(R​e​s​i​d​u​a​l​s)\varphi(Residuals) of standardized increments with a horizontal reference line at φ​(3)\varphi(3), corresponding to the classical 3​σ3\sigma boundary, shown for different values of the robustness parameter α\alpha.

Figure 1: Effect of robustness on pointwise influence and likelihood contributions under jump contamination. Increasing α\alpha progressively bounds the influence of large, jump-induced increments while preserving the contribution of diffusion-driven observations.

Motivated by these considerations, we consider the CKLS diffusion augmented by a
jump component. Specifically, for known elasticity parameter γ\gamma, we study
the jump–diffusion model

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=(β1−β2​Xt)​d​t+σ​Xtγ​d​Wt+d​Jt,dX\_{t}=(\beta\_{1}-\beta\_{2}X\_{t})\,dt+\sigma X\_{t}^{\gamma}\,dW\_{t}+dJ\_{t}, |  | (6) |

where {Jt}t≥0\{J\_{t}\}\_{t\geq 0} is a pure-jump process independent of WtW\_{t}. Such models
are widely used in interest rate and volatility modeling to capture abrupt market
movements. The classical Cox–Ingersoll–Ross model arises as the special case
γ=1/2\gamma=1/2.

Figures [1(a)](#S2.F1.sf1 "In Figure 1 ‣ 2.1 Robust Estimation via Density Power Divergence ‣ 2 Theoretical Background and Illustration ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models") and [1(b)](#S2.F1.sf2 "In Figure 1 ‣ 2.1 Robust Estimation via Density Power Divergence ‣ 2 Theoretical Background and Illustration ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models") illustrate
the effect of robustness on the pointwise contribution of standardized increments.
When α=0\alpha=0, corresponding to Gaussian likelihood estimation, the influence
of extreme increments is unbounded, and jump observations may dominate the
estimating equations. As the robustness parameter α\alpha increases, the influence
function becomes bounded, and the contribution of jump-induced increments is
progressively attenuated, while diffusion-driven increments remain largely
unaffected. This behavior reflects the intrinsic robustness of the MDPDE and its
ability to isolate the continuous diffusion structure from jump contamination.

Taken together, these considerations highlight a fundamental advantage of
divergence-based estimation in high-frequency diffusion models. By exploiting the
distinct scaling behavior of diffusion and jump increments, the MDPDE provides
stable parameter estimates and offers a principled basis for detecting departures
from the pure diffusion assumption. This diagnostic capability will play a central
role in the development of the robust parametric jump detection methodology
presented in subsequent sections.

## 3 Proposed Test for Jump

Let {Xti}i=0n\{X\_{t\_{i}}\}\_{i=0}^{n} denote discrete observations of the process introduced
above equation ([6](#S2.E6 "In 2.1 Robust Estimation via Density Power Divergence ‣ 2 Theoretical Background and Illustration ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models")), recorded at equidistant times ti=i​Δnt\_{i}=i\Delta\_{n} over a fixed time horizon,
where Δn→0\Delta\_{n}\to 0. Denote the increments by

|  |  |  |
| --- | --- | --- |
|  | Δin​X:=Xti−Xti−1\Delta\_{i}^{n}X:=X\_{t\_{i}}-X\_{t\_{i-1}} |  |

and the jump increment be defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δin​J=Jti−Jti−1,\Delta\_{i}^{n}J=J\_{t\_{i}}-J\_{t\_{i-1}}, |  | (7) |

where the presence of a jump at index ii corresponds to the event Δi​J≠0\Delta\_{i}J\neq 0.
Let 𝜽^n:=(β^1​n,β^2​n,σ^n)\hat{\bm{\theta}}\_{n}:=(\hat{\beta}\_{1n},\hat{\beta}\_{2n},\hat{\sigma}\_{n}) denote
consistent estimators of the model parameters satisfying

|  |  |  |
| --- | --- | --- |
|  | β^1​n→𝑃β1,β^2​n→𝑃β2,σ^n→𝑃σ,Pr⁡(σ^n>0)→1.\hat{\beta}\_{1n}\xrightarrow{P}\beta\_{1},\qquad\hat{\beta}\_{2n}\xrightarrow{P}\beta\_{2},\qquad\hat{\sigma}\_{n}\xrightarrow{P}\sigma,\qquad\Pr(\hat{\sigma}\_{n}>0)\to 1. |  |

We define the normalized increment statistic

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zi,n=Δin​X−(β^1​n−β^2​n​Xti−1)​Δnσ^n​Xti−1γ​Δn.Z\_{i,n}=\frac{\Delta\_{i}^{n}X-(\hat{\beta}\_{1n}-\hat{\beta}\_{2n}X\_{t\_{i-1}})\Delta\_{n}}{\hat{\sigma}\_{n}X\_{t\_{i-1}}^{\gamma}\sqrt{\Delta\_{n}}}. |  | (8) |

This normalization removes the estimated drift and rescales the increment by the
estimated local diffusion magnitude. Consequently, increments generated by the
continuous martingale component are brought to a unit Gaussian scale, whereas
jump-induced increments remain asymptotically separated due to their larger order.
This separation forms the foundation of the parametric jump detection procedure
developed in the sequel.

The following theorem establishes the asymptotic decomposition of the normalized
increment statistic into its continuous martingale and jump components.

###### Theorem 1.

Suppose the parameter estimators are consistent. Then, for each fixed index ii,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zi,n=Δin​WΔn+Δin​Jσ​Xti−1γ​Δn+op​(1).Z\_{i,n}=\frac{\Delta\_{i}^{n}W}{\sqrt{\Delta\_{n}}}+\frac{\Delta\_{i}^{n}J}{\sigma X\_{t\_{i-1}}^{\gamma}\sqrt{\Delta\_{n}}}+o\_{p}(1). |  | (9) |

Consequently, if Δin​J=0\Delta\_{i}^{n}J=0, then

|  |  |  |
| --- | --- | --- |
|  | Zi,n→ℒ𝒩​(0,1),Z\_{i,n}\xrightarrow{\mathcal{L}}\mathcal{N}(0,1), |  |

whereas if Δin​J≠0\Delta\_{i}^{n}J\neq 0 and the jump magnitude is nondegenerate,

|  |  |  |
| --- | --- | --- |
|  | |Zi,n|→𝑃∞.|Z\_{i,n}|\xrightarrow{P}\infty. |  |

Theorem [1](#Thmtheorem1 "Theorem 1. ‣ 3 Proposed Test for Jump ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models") formalizes the pointwise asymptotic separation
between the continuous and discontinuous components. After normalization,
diffusion-driven increments remain stochastically bounded, while jump-induced
increments diverge at rate Δn−1/2\Delta\_{n}^{-1/2}.

We next characterize the maximal fluctuation of the statistic over intervals
free of jumps, which determines the natural detection boundary.

###### Theorem 2.

Let

|  |  |  |
| --- | --- | --- |
|  | 𝒞n={i∈{1,…,n}:Δin​J=0}.\mathcal{C}\_{n}=\{i\in\{1,\dots,n\}:\Delta\_{i}^{n}J=0\}. |  |

Under consistency of the parameter estimators,

|  |  |  |
| --- | --- | --- |
|  | maxi∈𝒞n⁡|Zi,n|=2​log⁡(n)+Op​(1),\max\_{i\in\mathcal{C}\_{n}}|Z\_{i,n}|=\sqrt{2\log(n)}+O\_{p}(1), |  |

and more precisely,

|  |  |  |
| --- | --- | --- |
|  | maxi∈𝒞n⁡|Zi,n|−anbn⇒Λ,\frac{\max\_{i\in\mathcal{C}\_{n}}|Z\_{i,n}|-a\_{n}}{b\_{n}}\Rightarrow\Lambda, |  |

where

|  |  |  |
| --- | --- | --- |
|  | an=2​log⁡n−log⁡log⁡n+log⁡(π)2​2​log⁡n,bn=12​log⁡n,a\_{n}=\sqrt{2\log n}-\frac{\log\log n+\log(\pi)}{2\sqrt{2\log n}},\qquad b\_{n}=\frac{1}{\sqrt{2\log n}}, |  |

and Λ\Lambda denotes the standard Gumbel distribution.

This extreme-value characterization determines the intrinsic growth rate of the
continuous-path maximum and provides a principled basis for threshold selection.

###### Corollary 1.

Under the same assumptions,

|  |  |  |
| --- | --- | --- |
|  | Pr⁡(maxi∈𝒞n⁡|Zi,n|<2​log⁡(n)<mini:Δin​J≠0⁡|Zi,n|)→1.\Pr\!\left(\max\_{i\in\mathcal{C}\_{n}}|Z\_{i,n}|<\sqrt{2\log(n)}<\min\_{i:\Delta\_{i}^{n}J\neq 0}|Z\_{i,n}|\right)\to 1. |  |

Corollary [1](#Thmcorollary1 "Corollary 1. ‣ 3 Proposed Test for Jump ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models") establishes uniform asymptotic separation
between the continuous and jump components, ensuring that a threshold of order
2​log⁡(1/Δn)\sqrt{2\log(1/\Delta\_{n})} asymptotically discriminates between the two regimes.

###### Theorem 3 (Consistency of parametric jump detection).

Suppose the assumptions of Theorems [1](#Thmtheorem1 "Theorem 1. ‣ 3 Proposed Test for Jump ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models"),
[2](#Thmtheorem2 "Theorem 2. ‣ 3 Proposed Test for Jump ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models"), and the consistency of the estimators hold. Then,

|  |  |  |
| --- | --- | --- |
|  | Pr⁡(maxi∈𝒞n⁡|Zi,n|>ξn)→0,\Pr\!\left(\max\_{i\in\mathcal{C}\_{n}}|Z\_{i,n}|>\xi\_{n}\right)\to 0, |  |

and, for any index ii such that Δin​J≠0\Delta\_{i}^{n}J\neq 0,

|  |  |  |
| --- | --- | --- |
|  | Pr⁡(|Zi,n|≤ξn)→0.\Pr\!\left(|Z\_{i,n}|\leq\xi\_{n}\right)\to 0. |  |

Consequently,

|  |  |  |
| --- | --- | --- |
|  | Pr⁡(correct classification of all increments)→1.\Pr(\text{correct classification of all increments})\to 1. |  |

Reliable separation requires stable estimation of the diffusion scale parameter.
Classical likelihood-based estimators may be severely distorted by jump-induced
contamination, compromising the normalization. To address this issue, we employ
robust estimators based on the minimum density power divergence.

Let 𝜽^nα:=(β^1​nα,β^2​nα,σ^nα)\hat{\bm{\theta}}\_{n}^{\alpha}:=(\hat{\beta}\_{1n}^{\alpha},\hat{\beta}\_{2n}^{\alpha},\hat{\sigma}\_{n}^{\alpha}) denote the robust
estimators, and define the corresponding normalized statistic

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zi,nα=Δin​X−(β^1​nα−β^2​nα​Xti−1)​Δnσ^nα​Xti−1γ​Δn.Z^{\alpha}\_{i,n}=\frac{\Delta\_{i}^{n}X-(\hat{\beta}\_{1n}^{\alpha}-\hat{\beta}\_{2n}^{\alpha}X\_{t\_{i-1}})\Delta\_{n}}{\hat{\sigma}\_{n}^{\alpha}X\_{t\_{i-1}}^{\gamma}\sqrt{\Delta\_{n}}}. |  | (10) |

By consistency of the robust estimators, the asymptotic expansion
([9](#S3.E9 "In Theorem 1. ‣ 3 Proposed Test for Jump ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models")) and the extreme-value result of
Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 3 Proposed Test for Jump ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models") remain valid for Zi,nαZ^{\alpha}\_{i,n}, while providing
enhanced stability under contamination.

We formulate jump identification at index ii as the testing problem

|  |  |  |
| --- | --- | --- |
|  | H0,i:Δin​J=0,H1,i:Δin​J≠0.H\_{0,i}:\Delta\_{i}^{n}J=0,\qquad H\_{1,i}:\Delta\_{i}^{n}J\neq 0. |  |

Under H0,iH\_{0,i},

|  |  |  |
| --- | --- | --- |
|  | Zi,nα⇒𝒩​(0,1),Z^{\alpha}\_{i,n}\Rightarrow\mathcal{N}(0,1), |  |

whereas under H1,iH\_{1,i} with nonvanishing jump magnitude,

|  |  |  |
| --- | --- | --- |
|  | |Zi,nα|→𝑃∞.|Z^{\alpha}\_{i,n}|\xrightarrow{P}\infty. |  |

Thus, the continuous and discontinuous regimes become asymptotically
distinguishable through the magnitude of the standardized statistic.
Motivated by Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 3 Proposed Test for Jump ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models"), we introduce the detection threshold

|  |  |  |
| --- | --- | --- |
|  | ξn=2​log⁡n+cn,cn→∞,\xi\_{n}=\sqrt{2\log n}+c\_{n},\qquad c\_{n}\to\infty, |  |

and declare a jump at time tit\_{i} whenever

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Zi,nα|>ξn.|Z^{\alpha}\_{i,n}|>\xi\_{n}. |  | (11) |

Define the true and estimated jump index sets by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒥n={i∈{1,…,n}:Δin​J≠0},𝒥^n={i∈{1,…,n}:|Zi,nα|>ξn}.\displaystyle\mathcal{J}\_{n}=\left\{i\in\{1,\ldots,n\}:\Delta\_{i}^{n}J\neq 0\right\},\qquad\hat{\mathcal{J}}\_{n}=\left\{i\in\{1,\ldots,n\}:|Z^{\alpha}\_{i,n}|>\xi\_{n}\right\}. |  | (12) |

Combining the consistency of the robust parameter estimator with
Theorem [3](#Thmtheorem3 "Theorem 3 (Consistency of parametric jump detection). ‣ 3 Proposed Test for Jump ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models") implies

|  |  |  |
| --- | --- | --- |
|  | Pr⁡(𝒥^n=𝒥n)→1.\Pr\!\left(\hat{\mathcal{J}}\_{n}=\mathcal{J}\_{n}\right)\to 1. |  |

Consequently, conditional on consistent identification of the jump indices,
the jump magnitude at detected times is estimated by

|  |  |  |
| --- | --- | --- |
|  | Δin​J^=Δin​X−(β^1​nα−β^2​nα​Xti−1)​Δn,i∈𝒥^n.\Delta\_{i}^{n}\hat{J}=\Delta\_{i}^{n}X-\bigl(\hat{\beta}\_{1n}^{\alpha}-\hat{\beta}\_{2n}^{\alpha}X\_{t\_{i-1}}\bigr)\Delta\_{n},\qquad i\in\hat{\mathcal{J}}\_{n}. |  |

The preceding result establishes asymptotic separation between the
continuous diffusion component and the jump component.
Specifically, the extreme–value growth of the maximal standardized
diffusion increment determines the appropriate detection boundary,
whereas the divergence of the statistic in the presence of jumps ensures
consistent identification of discontinuities.
The robust parametric normalization further stabilizes scale estimation,
thereby enhancing reliability under jump contamination and mild model
misspecification.

## 4 Simulation Study

We conduct a simulation study to examine the finite-sample behavior of the proposed robust parameter estimation and jump detection procedure. The data generating process is given by ([6](#S2.E6 "In 2.1 Robust Estimation via Density Power Divergence ‣ 2 Theoretical Background and Illustration ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models")). The jump component (Jt)(J\_{t}) is specified as a compound Poisson process

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jt=∑k=1NtYk,J\_{t}=\sum\_{k=1}^{N\_{t}}Y\_{k}, |  | (13) |

where (Nt)(N\_{t}) is a Poisson process with intensity λ\lambda, and the jump sizes (Yk)(Y\_{k}) are independent and identically distributed with

|  |  |  |
| --- | --- | --- |
|  | Yk∼𝒩​(μJ,σJ2).Y\_{k}\sim\mathcal{N}(\mu\_{J},\sigma\_{J}^{2}). |  |

The process is observed at equidistant time points with sampling interval
Δn=n−0.55,\Delta\_{n}=n^{-0.55},
corresponding to a high-frequency asymptotic regime in which
Δn→0\Delta\_{n}\to 0 as n→∞n\to\infty.
The underlying diffusion parameters are set to
β1=1\beta\_{1}=1, β2=0.8\beta\_{2}=0.8, σ=0.3\sigma=0.3, and γ=0.7\gamma=0.7.

The simulation study considers the following configurations for the
sample size and jump component parameters:

|  |  |  |  |
| --- | --- | --- | --- |
|  | n∈{200,500,1000,1500,2000},λ∈{1,2,3,5},μJ∈{1,2,3,4,5},σJ=0.1,\displaystyle n\in\{200,500,1000,1500,2000\},\quad\lambda\in\{1,2,3,5\},\quad\mu\_{J}\in\{1,2,3,4,5\},\quad\sigma\_{J}=0.1, |  | (14) |

in order to evaluate the performance of the proposed robust procedure
for jump isolation and detection.

We first examine performance through a visual comparison between true and
detected jump locations. For illustration, a representative trajectory is
generated under the configuration (n,λ,μJ)=(1000,5,3)(n,\lambda,\mu\_{J})=(1000,5,3).
Using this fixed sample path, jump classification is performed for
robustness parameters

|  |  |  |
| --- | --- | --- |
|  | α∈{0,0.05,0.1,0.15,0.2,0.25},\alpha\in\{0,0.05,0.1,0.15,0.2,0.25\}, |  |

where parameter estimation is carried out via the robust procedure and
the resulting estimates are used to classify increments as jump or
diffusion driven. The case α=0\alpha=0 corresponds to the classical
least-squares estimator, providing a non-robust benchmark.

Figure [2](#S4.F2 "Figure 2 ‣ 4 Simulation Study ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models") presents the jump detection results for the
values of the robustness parameter α\alpha specified above. Rather than
displaying the sample path itself, we plot the first-order increments
(Δin​X)(\Delta\_{i}^{n}X) to highlight discontinuities directly. The detection
threshold obtained from Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 3 Proposed Test for Jump ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models") is
ξn=3.512\xi\_{n}=3.512. True jump times are indicated by blue markers, while
detected jumps based on the thresholded standardized statistic are shown
in red.

When α=0\alpha=0, corresponding to the classical OLS estimator, the
procedure fails to identify several clearly separated jumps. As α\alpha
increases, detection improves substantially, reflecting the stabilizing
effect of robust normalization. The detection rate increases rapidly for
small positive values of α\alpha and stabilizes around
α=0.15\alpha=0.15, beyond which all true jumps are consistently
identified.

These results illustrate the role of the robustness parameter in
controlling the trade-off between sensitivity and stability. Small values
of α\alpha leave the normalization susceptible to diffusion-driven
extreme increments, leading to missed or unstable detections, whereas
moderate values attenuate this influence and reduce spurious
classifications while preserving detection power.

![Refer to caption](2603.05119v1/x1.png)


Figure 2: Visual comparison of true and detected jumps in the increment process Δin​X\Delta\_{i}^{n}X for different values of the robustness parameter α\alpha.
denotes true jumps, whereas 
denotes jumps detected by the proposed procedure.

To provide a more comprehensive assessment of the proposed procedure,
we summarize performance over the parameter configurations specified in
([14](#S4.E14 "In 4 Simulation Study ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models")) for robustness levels
α∈{0,0.05,0.1,…,0.5}\alpha\in\left\{0,0.05,0.1,\dots,0.5\right\}.
Performance is evaluated using classification accuracy and parameter
recovery metrics, namely the F1-score and a scaled estimation error.

Let 𝒥n\mathcal{J}\_{n} and 𝒥^n\hat{\mathcal{J}}\_{n} denote the true and estimated
jump sets, respectively, as defined in ([12](#S3.E12 "In 3 Proposed Test for Jump ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models")).
We define the classification counts

|  |  |  |  |
| --- | --- | --- | --- |
|  | TP\displaystyle\mathrm{TP} | =|𝒥n∩𝒥^n|,FN=|𝒥n∖𝒥^n|,FP=|𝒥^n∖𝒥n|.\displaystyle=|\mathcal{J}\_{n}\cap\hat{\mathcal{J}}\_{n}|,\qquad\mathrm{FN}=|\mathcal{J}\_{n}\setminus\hat{\mathcal{J}}\_{n}|,\qquad\mathrm{FP}=|\hat{\mathcal{J}}\_{n}\setminus\mathcal{J}\_{n}|. |  |

The corresponding performance measures are

|  |  |  |  |
| --- | --- | --- | --- |
|  | Precision | =TPTP+FP,Recall=TPTP+FN,\displaystyle=\frac{\mathrm{TP}}{\mathrm{TP}+\mathrm{FP}},\qquad\text{Recall}=\frac{\mathrm{TP}}{\mathrm{TP}+\mathrm{FN}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | F1-score | =2​Precision×RecallPrecision+Recall.\displaystyle=2\,\frac{\text{Precision}\times\text{Recall}}{\text{Precision}+\text{Recall}}. |  |

Although the jump intensity parameter λ\lambda is fixed in simulation,
the realized number of jumps varies across trajectories. Consequently,
evaluation based on the theoretical parameters may be misleading in
finite samples. We therefore compare estimators with the
*realized* jump characteristics. Define the realized jump mean and
intensity as

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ~J=1|𝒥n|​∑i∈𝒥nΔin​J,λ~=|𝒥n|n.\displaystyle\tilde{\mu}\_{J}=\frac{1}{|\mathcal{J}\_{n}|}\sum\_{i\in\mathcal{J}\_{n}}\Delta\_{i}^{n}J,\qquad\tilde{\lambda}=\frac{|\mathcal{J}\_{n}|}{n}. |  | (15) |

The corresponding estimators based on detected jumps are

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ^J=1|𝒥^n|​∑i∈𝒥^nΔin​J^,λ^=|𝒥^n|n.\displaystyle\hat{\mu}\_{J}=\frac{1}{|\hat{\mathcal{J}}\_{n}|}\sum\_{i\in\hat{\mathcal{J}}\_{n}}\Delta\_{i}^{n}\hat{J},\qquad\hat{\lambda}=\frac{|\hat{\mathcal{J}}\_{n}|}{n}. |  | (16) |

When both the sampling size nn and the jump intensity are moderate,
the number of realized jumps may be small, preventing reliable
convergence toward theoretical parameters. For this reason, estimation
accuracy is assessed relative to realized quantities rather than
population values. We measure the discrepancy via the scaled error
metric

|  |  |  |
| --- | --- | --- |
|  | dM:=(μ~Jμ^J−1)2+(λ~λ^−1)2,\displaystyle d\_{M}:=\sqrt{\left(\frac{\tilde{\mu}\_{J}}{\hat{\mu}\_{J}}-1\right)^{2}+\left(\frac{\tilde{\lambda}}{\hat{\lambda}}-1\right)^{2}}, |  |

which jointly evaluates the accuracy of estimated jump magnitude and
frequency.

Accordingly, detection performance and estimation accuracy are evaluated
jointly through the F1-score and the scaled error metric defined above.
The F1-score takes values in [0,1][0,1], with larger values indicating
improved classification performance; in particular, values closer to one
correspond to more accurate identification of jump indices.
While the
F1-score assesses detection accuracy through correct classification
counts, the metric dMd\_{M} quantifies the discrepancy between estimated and
realized jump characteristics.
dMd\_{M} is scale-free and equals zero if and only if the
estimated quantities coincide with their realized counterparts, that is,
μ^J=μ~J\hat{\mu}\_{J}=\tilde{\mu}\_{J} and λ^=λ~\hat{\lambda}=\tilde{\lambda}.
Consequently, smaller values of dMd\_{M} indicate greater estimation
accuracy, whereas larger values reflect increasing deviation from the
realized jump structure and hence reduced reliability of both parameter
estimation and detection. In this sense, the F1-score captures
classification performance, while dMd\_{M} measures parametric divergence,
providing complementary perspectives on the effectiveness of the proposed
procedure.

Figure [3](#S4.F3 "Figure 3 ‣ 4 Simulation Study ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models") reports the F1-score across the parameter
configurations defined in ([14](#S4.E14 "In 4 Simulation Study ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models")). The results show a clear
improvement in detection performance as the jump mean increases.
Moving from left to right in the figure, corresponding to larger values
of μJ\mu\_{J}, the F1-score increases monotonically and approaches one,
indicating nearly perfect recovery of the jump indices.
A similar improvement is observed when the sample size increases
(top to bottom panels). Larger samples lead to a faster convergence of
the F1-score toward one as the robustness parameter α\alpha increases.

For small sample sizes and higher jump intensities (large λ\lambda),
the number of jumps is relatively large compared with the available
observations, which reduces the power to correctly identify all true
jumps. Nevertheless, relative to the case α=0\alpha=0 (corresponding to
the OLS estimator), the detection accuracy improves substantially for
α>0\alpha>0, demonstrating the advantage of the proposed robust
normalization. These findings are consistent with the theoretical
result in Theorem [3](#Thmtheorem3 "Theorem 3 (Consistency of parametric jump detection). ‣ 3 Proposed Test for Jump ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models"), which implies
that diffusion increments remain of stochastic order
Δn\sqrt{\Delta\_{n}} while jump-induced increments diverge, yielding
increasing separation as Δn→0\Delta\_{n}\to 0.

A similar pattern is observed in the jump-parameter estimation results
shown in Figure [4](#S4.F4 "Figure 4 ‣ 4 Simulation Study ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models"). As the separation between the
diffusion increments and the realized jump mean (μ~J)(\tilde{\mu}\_{J})
increases (again moving from left to right), the proposed metric
converges more rapidly toward zero, indicating improved estimation
accuracy. When the jump intensity is very small (λ=1\lambda=1), the
performance of the OLS estimator is nearly indistinguishable from that
of the robust estimator with α>0\alpha>0. In contrast, for higher jump
intensities and small samples, the discrepancy between the estimated
and realized parameters becomes more pronounced. Increasing the sample
size substantially reduces this discrepancy, and the metric declines
more steeply toward zero, reflecting improved estimation precision.

![Refer to caption](2603.05119v1/x2.png)


Figure 3: F1 score as a function of the robustness parameter α\alpha for different sample sizes (nn), jump intensities (λ\lambda), and jump mean values (μJ\mu\_{J}). Panels are arranged by sample size (rows) and jump mean (columns), while curves correspond to different jump intensities. The figure illustrates how the robustness parameter affects jump detection accuracy and how this effect varies with jump magnitude, jump frequency, and sampling resolution.

Overall, the simulation results provide empirical support for the
theoretical separation mechanism underlying the proposed detection
procedure. The robust parametric normalization preserves the
asymptotic divergence of jump-induced increments while stabilizing the
estimation of the diffusion scale. As a consequence, the resulting
procedure achieves reliable identification of discontinuities across a
broad range of jump intensities and magnitudes, maintaining stable
performance even under moderate contamination through jumps.

![Refer to caption](2603.05119v1/x3.png)


Figure 4: Error metric (dMd\_{M}) as a function of the robustness parameter α\alpha under varying sample sizes (nn), jump intensities (λ\lambda), and jump mean values (μJ\mu\_{J}). Panels are arranged by sample size (rows) and jump mean (columns), while curves correspond to different jump intensities. The figure illustrates how the robustness tuning parameter influences the accuracy of jump parameter estimation and how this effect interacts with jump magnitude, jump frequency, and sampling resolution.

## 5 Conclusion

This paper develops a robust estimation and jump detection framework for discretely observed CKLS jump–diffusion processes under high–frequency asymptotics. The methodology combines a density power divergence–based estimator for drift parameters with an extreme–value–theoretic jump detection rule derived from standardized residuals. The proposed approach is designed to retain asymptotic validity under the diffusion benchmark while mitigating the influence of atypical increments arising from jumps or other departures from Gaussianity.

On the theoretical side, we establish consistency and asymptotic normality of the robust estimator under infill asymptotics and show that the associated residual normalization yields a detection statistic whose extremal behavior permits asymptotically valid separation of continuous and discontinuous components. The analysis demonstrates that robustness regularizes the normalization without altering the asymptotic classification boundary, thereby preserving identifiability of the jump component.

The finite–sample experiments corroborate the theoretical findings. The results show that moderate robustness improves stability of both parameter estimation and jump identification, particularly in regimes where jump magnitudes are small or sample sizes are limited. As the sampling frequency increases, detection performance approaches the asymptotic regime, confirming the theoretical scale separation between diffusion and jump increments.

Overall, the proposed framework provides a unified and theoretically grounded approach to robust inference in jump–diffusion models. It achieves reliable jump detection and stable parameter estimation across a broad range of regimes, while remaining consistent with classical likelihood–based inference under the pure diffusion specification. These results support the use of robustness as a principled mechanism for improving finite–sample performance without compromising asymptotic efficiency.

## Acknowledgments

The author would like to express special thanks to Prof. Diganta Mukherjee 111Professor, Indian Statistical Institute for his valuable guidance and insightful suggestions throughout this research. The author is also grateful to Prof. Indranil Sengupta222Professor, City University of New York for his assistance and support during the development of this work. Their contributions have been instrumental in shaping the final outcome of this paper.

1
1
1
1
1
1
2
3
2
2
1
1
1
1
1
1
1
3
1
3
1
1
1
1
1
1
1

## References

* [undef]
  Yacine Aït-Sahalia and Jean Jacod
  “Testing for Jumps in a Discretely Observed Process”
  In *The Annals of Statistics* 37.1
  Institute of Mathematical Statistics, 2009, pp. 184–222
  DOI: [10.1214/07-AOS568](https://dx.doi.org/10.1214/07-AOS568)
* [undefa]
  Mohamed Ben Alaya and Ahmed Kebaier
  “Parameter Estimation for the Square-Root Diffusions: Ergodic and Nonergodic Cases”
  In *Stochastic Models* 28.4
  Taylor & Francis, 2012, pp. 609–634
  DOI: [10.1080/15326349.2012.726042](https://dx.doi.org/10.1080/15326349.2012.726042)
* [undefb]
  Mohamed Ben Alaya and Ahmed Kebaier
  “Asymptotic Behavior of the Maximum Likelihood Estimator for Ergodic and Nonergodic Square-Root Diffusions”
  In *Stochastic Analysis and Applications* 31.4
  Taylor & Francis, 2013, pp. 552–573
  DOI: [10.1080/07362994.2013.798175](https://dx.doi.org/10.1080/07362994.2013.798175)
* [undefc]
  Leif Andersen and Vladimir Piterbarg
  “Moment Explosions in Stochastic Volatility Models”
  In *Finance and Stochastics* 11, 2007, pp. 29–50
  DOI: [10.1007/s00780-006-0011-7](https://dx.doi.org/10.1007/s00780-006-0011-7)
* [undefd]
  Ole E. Barndorff-Nielsen and Neil Shephard
  “Power and bipower variation”
  In *Journal of Financial Econometrics*, 2004
* [undefe]
  Ole E. Barndorff-Nielsen and Neil Shephard
  “Econometrics of Testing for Jumps in Financial Economics Using Bipower Variation”
  In *Journal of Financial Econometrics* 4.1
  Oxford University Press, 2006, pp. 1–30
  DOI: [10.1093/jjfinec/nbi022](https://dx.doi.org/10.1093/jjfinec/nbi022)
* [undeff]
  Ayanendranath Basu, Ian R. Harris, Nils L. Hjort and Michael C. Jones
  “Robust and Efficient Estimation by Minimising a Density Power Divergence”
  In *Biometrika* 85.3, 1998, pp. 549–559
  URL: <http://www.jstor.org/stable/2337385>
* [undefg]
  K.. Chan, G. Karolyi, Francis A. Longstaff and Anthony B. Sanders
  “An Empirical Comparison of Alternative Models of the Short-Term Interest Rate”
  In *The Journal of Finance* 47.3, 1992, pp. 1209–1227
  DOI: [https://doi.org/10.1111/j.1540-6261.1992.tb04011.x](https://dx.doi.org/https://doi.org/10.1111/j.1540-6261.1992.tb04011.x)
* [undefh]
  John C. Cox, Jonathan E. Ingersoll and Stephen A. Ross
  “A Theory of the Term Structure of Interest Rates”
  In *Econometrica* 53.2
  [Wiley, Econometric Society], 1985, pp. 385–407
  URL: <http://www.jstor.org/stable/1911242>
* [undefi]
  Olena Dehtiar, Yuliya Mishura and Kostiantyn Ralchenko
  “Two Methods of Estimation of the Drift Parameters of the Cox–Ingersoll–Ross Process: Continuous Observations”
  In *Communications in Statistics – Theory and Methods* 51.19
  Taylor & Francis, 2022, pp. 6818–6833
  DOI: [10.1080/03610926.2020.1866611](https://dx.doi.org/10.1080/03610926.2020.1866611)
* [undefj]
  Darrell Duffie, Jun Pan and Kenneth Singleton
  “Transform Analysis and Asset Pricing for Affine Jump-Diffusions”
  In *Econometrica* 68.6
  Wiley, 2000, pp. 1343–1376
  DOI: [10.1111/1468-0262.00164](https://dx.doi.org/10.1111/1468-0262.00164)
* [undefk]
  Darrell Duffie and Kenneth J. Singleton
  “Simulated Moments Estimation of Markov Models of Asset Prices”
  In *Econometrica* 61.4, 1993, pp. 929–952
* [undefl]
  Xiaoxia Feng and Dejun Xie
  “Bayesian Estimation of CIR Model”
  In *Journal of Data Science* 10.2
  School of Statistics, Renmin University of China, 2022, pp. 271–280
  DOI: [10.6339/JDS.2012.10(2).746](https://dx.doi.org/10.6339/JDS.2012.10(2).746)
* [undefm]
  Abhik Ghosh, Ayanendranath Basu and Leandro Pardo
  “Generalized Density Power Divergence and Robust Estimation”
  In *Journal of Statistical Planning and Inference* 143.7, 2013, pp. 1100–1114
* [undefn]
  David Heath, Robert Jarrow and Andrew Morton
  “Bond Pricing and the Term Structure of Interest Rates: A New Methodology”
  In *Econometrica* 60.1, 1992, pp. 77–105
* [undefo]
  Jean Jacod
  “Asymptotic properties of realized power variations”
  In *Annals of Probability*, 2008
* [undefp]
  Samuel Karlin and Howard Edward Taylor
  “A second course in stochastic processes”, 1981
  URL: <https://api.semanticscholar.org/CorpusID:118412345>
* [undefq]
  Mathieu Kessler
  “Estimation of an Ergodic Diffusion from Discrete Observations”
  In *Scandinavian Journal of Statistics* 24.2, 1997, pp. 211–229
* [undefr]
  Peter E. Kloeden and Eckhard Platen
  “Numerical Solution of Stochastic Differential Equations” 23, Stochastic Modelling and Applied Probability
  Berlin, Heidelberg: Springer, 1992
* [undefs]
  Sangyeol Lee and Junmo Song
  “Minimum Density Power Divergence Estimator for Diffusion Processes”
  In *Annals of the Institute of Statistical Mathematics* 65.2, 2013, pp. 213–236
  DOI: [10.1007/s10463-012-0366-9](https://dx.doi.org/10.1007/s10463-012-0366-9)
* [undeft]
  Suzanne S. Lee and Per A. Mykland
  “Jumps in Financial Markets: A New Nonparametric Test and Jump Dynamics”
  In *The Review of Financial Studies* 21.6
  Oxford University Press, 2008, pp. 2535–2563
  DOI: [10.1093/rfs/hhm056](https://dx.doi.org/10.1093/rfs/hhm056)
* [undefu]
  Zenghu Li and Chunhua Ma
  “Asymptotic properties of estimators in a stable Cox-Ingersoll-Ross model”, 2013
  arXiv: <https://arxiv.org/abs/1301.3243>
* [undefv]
  Robert C. Merton
  “Option Pricing When Underlying Stock Returns Are Discontinuous”
  In *Journal of Financial Economics* 3.1–2
  Elsevier, 1976, pp. 125–144
  DOI: [10.1016/0304-405X(76)90022-2](https://dx.doi.org/10.1016/0304-405X(76)90022-2)
* [undefw]
  Yuliya Mishura, Kostiantyn Ralchenko and Olena Dehtiar
  “Parameter estimation in CKLS model by continuous observations”
  In *Statistics & Probability Letters* 184.C, 2022
  DOI: [10.1016/j.spl.2022.109391](https://dx.doi.org/10.1016/j.spl.2022.109391)
* [undefx]
  Ludger Overbeck
  “Estimation for Continuous Branching Processes”
  In *Scandinavian Journal of Statistics* 25.1
  [Board of the Foundation of the Scandinavian Journal of Statistics, Wiley], 1998, pp. 111–126
  URL: <http://www.jstor.org/stable/4616488>
* [undefy]
  Masayuki Uchida and Nakahiro Yoshida
  “Adaptive estimation of an ergodic diffusion process based on sampled data”
  In *Stochastic Processes and their Applications* 122, 2012, pp. 2885–2924
* [undefz]
  Nobuaki Yoshida
  “Asymptotic behavior of M-estimator and related random field for diffusion processes”
  In *Annals of the Institute of Statistical Mathematics* 40.2, 1988, pp. 271–296
  DOI: [10.1007/BF00052393](https://dx.doi.org/10.1007/BF00052393)

## Appendix A Appendix

###### Proof of the theorem [1](#Thmtheorem1 "Theorem 1. ‣ 3 Proposed Test for Jump ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models").

Integrating ([6](#S2.E6 "In 2.1 Robust Estimation via Density Power Divergence ‣ 2 Theoretical Background and Illustration ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models")) over (ti−1,ti](t\_{i-1},t\_{i}] yields

|  |  |  |
| --- | --- | --- |
|  | Δin​X=∫ti−1tiκ​(θ−Xs)​𝑑s+∫ti−1tiσ​Xsγ​𝑑Ws+Δin​J.\Delta\_{i}^{n}X=\int\_{t\_{i-1}}^{t\_{i}}\kappa(\theta-X\_{s})\,ds+\int\_{t\_{i-1}}^{t\_{i}}\sigma{X\_{s}^{\gamma}}\,dW\_{s}+\Delta\_{i}^{n}J. |  |

A first-order Itô–Taylor expansion gives

|  |  |  |
| --- | --- | --- |
|  | Δin​X=κ​(θ−Xti−1)​Δn+σ​Xti−1γ​Δin​W+Δin​J+Op​(Δn).\Delta\_{i}^{n}X=\kappa(\theta-X\_{t\_{i-1}})\Delta\_{n}+\sigma{X\_{t\_{i-1}}^{\gamma}}\Delta\_{i}^{n}W+\Delta\_{i}^{n}J+O\_{p}(\Delta\_{n}). |  |

Subtracting the estimated drift component and invoking consistency of the parameters yields

|  |  |  |
| --- | --- | --- |
|  | Δin​X−κ^n​(θ^n−Xti−1)​Δn=σ​Xti−1γ​Δin​W+Δin​J+op​(Δn).\Delta\_{i}^{n}X-\hat{\kappa}\_{n}(\hat{\theta}\_{n}-X\_{t\_{i-1}})\Delta\_{n}=\sigma X\_{t\_{i-1}}^{\gamma}\Delta\_{i}^{n}W+\Delta\_{i}^{n}J+o\_{p}(\sqrt{\Delta\_{n}}). |  |

Since

|  |  |  |
| --- | --- | --- |
|  | σ^n​Xti−1γ​Δn=σ​Xti−1γ​Δn​(1+op​(1)),\hat{\sigma}\_{n}X\_{t\_{i-1}}^{\gamma}\sqrt{\Delta\_{n}}=\sigma X\_{t\_{i-1}}^{\gamma}\sqrt{\Delta\_{n}}(1+o\_{p}(1)), |  |

division yields ([9](#S3.E9 "In Theorem 1. ‣ 3 Proposed Test for Jump ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models")), from which the stated conclusions follow.
∎

###### Proof of Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 3 Proposed Test for Jump ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models").

Let

|  |  |  |
| --- | --- | --- |
|  | Mn:=maxi∈𝒞n⁡|Zi,n|.M\_{n}:=\max\_{i\in\mathcal{C}\_{n}}|Z\_{i,n}|. |  |

By consistency of the parameter estimators,

|  |  |  |
| --- | --- | --- |
|  | Zi,n=Δin​X−b​(Xti−1)​Δnσ​(Xti−1)​Δn+op​(1)=ξi+op​(1),Z\_{i,n}=\frac{\Delta\_{i}^{n}X-b(X\_{t\_{i-1}})\Delta\_{n}}{\sigma(X\_{t\_{i-1}})\sqrt{\Delta\_{n}}}+o\_{p}(1)=\xi\_{i}+o\_{p}(1), |  |

uniformly over i∈𝒞ni\in\mathcal{C}\_{n}, where {ξi}\{\xi\_{i}\} are independent N​(0,1)N(0,1) variables. Since |𝒞n|/n→𝑃1|\mathcal{C}\_{n}|/n\xrightarrow{P}1, it follows that

|  |  |  |
| --- | --- | --- |
|  | Mn=max1≤i≤n⁡|ξi|+op​(1).M\_{n}=\max\_{1\leq i\leq n}|\xi\_{i}|+o\_{p}(1). |  |

Thus, for any u>0u>0,

|  |  |  |
| --- | --- | --- |
|  | Pr⁡(Mn≤u)=[2​Φ​(u)−1]n+o​(1).\Pr(M\_{n}\leq u)=\left[2\Phi(u)-1\right]^{n}+o(1). |  |

Define the normalizing sequences

|  |  |  |
| --- | --- | --- |
|  | an=2​log⁡n−log⁡log⁡n+log⁡π2​2​log⁡n,bn=12​log⁡n,a\_{n}=\sqrt{2\log n}-\frac{\log\log n+\log\pi}{2\sqrt{2\log n}},\qquad b\_{n}=\frac{1}{\sqrt{2\log n}}, |  |

and let un​(x)=an+bn​xu\_{n}(x)=a\_{n}+b\_{n}x. Using the Gaussian tail expansion

|  |  |  |
| --- | --- | --- |
|  | 1−Φ​(u)=ϕ​(u)u​(1+o​(1)),u→∞,1-\Phi(u)=\frac{\phi(u)}{u}(1+o(1)),\qquad u\to\infty, |  |

we obtain

|  |  |  |
| --- | --- | --- |
|  | n​[1−Φ​(un​(x))]→e−x.n\left[1-\Phi(u\_{n}(x))\right]\to e^{-x}. |  |

Consequently,

|  |  |  |
| --- | --- | --- |
|  | Pr⁡(Mn−anbn≤x)→exp⁡(−e−x),\Pr\!\left(\frac{M\_{n}-a\_{n}}{b\_{n}}\leq x\right)\to\exp(-e^{-x}), |  |

which establishes convergence to the standard Gumbel law.

Finally, since (Mn−an)/bn=Op​(1)(M\_{n}-a\_{n})/b\_{n}=O\_{p}(1) and an=2​log⁡n+o​(1)a\_{n}=\sqrt{2\log n}+o(1),

|  |  |  |
| --- | --- | --- |
|  | Mn=2​log⁡n+Op​(1).M\_{n}=\sqrt{2\log n}+O\_{p}(1). |  |

∎

###### Proof of Theorem [3](#Thmtheorem3 "Theorem 3 (Consistency of parametric jump detection). ‣ 3 Proposed Test for Jump ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models").

Let

|  |  |  |
| --- | --- | --- |
|  | 𝒞n={i:Δin​J=0},𝒥n={i:Δin​J≠0},\mathcal{C}\_{n}=\{i:\Delta\_{i}^{n}J=0\},\qquad\mathcal{J}\_{n}=\{i:\Delta\_{i}^{n}J\neq 0\}, |  |

denote the sets of continuous and jump increments, respectively, and define the threshold

|  |  |  |
| --- | --- | --- |
|  | ξn=an+bn​G−1​(1−q),\xi\_{n}=a\_{n}+b\_{n}G^{-1}(1-q), |  |

where an,bna\_{n},b\_{n} are given in Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 3 Proposed Test for Jump ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models") and G−1G^{-1} is the Gumbel quantile function.

We first control false detections. By Theorem [2](#Thmtheorem2 "Theorem 2. ‣ 3 Proposed Test for Jump ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models"),

|  |  |  |
| --- | --- | --- |
|  | maxi∈𝒞n⁡|Zi,n|−anbn⇒Λ,\frac{\max\_{i\in\mathcal{C}\_{n}}|Z\_{i,n}|-a\_{n}}{b\_{n}}\Rightarrow\Lambda, |  |

where Λ\Lambda has the standard Gumbel distribution. Hence,

|  |  |  |
| --- | --- | --- |
|  | Pr⁡(maxi∈𝒞n⁡|Zi,n|>ξn)=Pr⁡(Λ>G−1​(1−q))+o​(1)=q+o​(1).\Pr\!\left(\max\_{i\in\mathcal{C}\_{n}}|Z\_{i,n}|>\xi\_{n}\right)=\Pr\!\left(\Lambda>G^{-1}(1-q)\right)+o(1)=q+o(1). |  |

Since q>0q>0 may be chosen arbitrarily small, false detections vanish asymptotically.

Next, consider detection under the alternative. For any fixed i∈𝒥ni\in\mathcal{J}\_{n}, Theorem [1](#Thmtheorem1 "Theorem 1. ‣ 3 Proposed Test for Jump ‣ Asymptotic Separability of Diffusion and Jump Components in High-Frequency CIR and CKLS Models") yields

|  |  |  |
| --- | --- | --- |
|  | |Zi,n|→𝑃∞.|Z\_{i,n}|\xrightarrow{P}\infty. |  |

Since ξn=O​(log⁡n)\xi\_{n}=O(\sqrt{\log n}), it follows that

|  |  |  |
| --- | --- | --- |
|  | Pr⁡(|Zi,n|≤ξn)→0,\Pr(|Z\_{i,n}|\leq\xi\_{n})\to 0, |  |

so each jump is detected with probability tending to one.

Finally, define the estimated jump set

|  |  |  |
| --- | --- | --- |
|  | 𝒥^n={i:|Zi,n|>ξn}.\widehat{\mathcal{J}}\_{n}=\{i:|Z\_{i,n}|>\xi\_{n}\}. |  |

The preceding bounds imply

|  |  |  |
| --- | --- | --- |
|  | Pr⁡(𝒥^n=𝒥n)→1,\Pr\!\left(\widehat{\mathcal{J}}\_{n}=\mathcal{J}\_{n}\right)\to 1, |  |

which establishes consistency of the classification.
∎

BETA