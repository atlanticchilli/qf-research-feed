---
authors:
- Dmitrii Vlasiuk
doc_id: arxiv:2511.07834v1
family_id: arxiv:2511.07834
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Lévy-stable scaling of risk and performance functionals
url_abs: http://arxiv.org/abs/2511.07834v1
url_html: https://arxiv.org/html/2511.07834v1
venue: arXiv q-fin
version: 1
year: 2025
---


Dmitrii Vlasiuk
  
Department of Mathematics, Columbia University

(November 2025)

###### Abstract

We develop a finite-horizon model in which liquid-asset returns exhibit Lévy-stable scaling on a data-driven window [τUV,τIR][\tau\_{\mathrm{UV}},\tau\_{\mathrm{IR}}] and aggregate into a finite-variance regime outside. The window and the tail index α\alpha are identified from the log-log slope of the central body and a two-segment fit of scale versus horizon. With an anchor horizon τ0\tau\_{0}, we derive horizon-correct formulas for Value-at-Risk, Expected Shortfall, Sharpe and Information ratios, Kelly under a Value-at-Risk constraint, and one-step drawdown, where each admits a closed-form Gaussian-bias term driven by the exponent gap 1/α−1/21/\alpha-1/2. The implementation is nonparametric up to α\alpha and fixed tail quantiles. The formulas are reproducible across horizons on the Lévy window.

## 1 Introduction

Previous empirical studies have shown that the price series of many liquid assets do not exhibit Gaussian behavior. Mandelbrot (1963) documented heavy tails and scale effects that invalidate routine Gaussian formulas in liquid markets. Cont (2001) summarized the core stylized facts: peaked centers, slowly decaying tails, and dependence structures that do not kill extremes fast enough for variance-based propagation. Bouchaud and Potters (2003) collected further evidence that return distributions are far from normal at trading horizons. Mantegna and Stanley (1995) showed that the central parts of index-return distributions collapse under Lévy-stable rescaling over a finite span of horizons, while Gopikrishnan, Plerou, Amaral, Meyer and Stanley (1999) reported coherent scaling of fluctuations across indices.

Our goal is to turn those observations into a finite-horizon model with an explicit Lévy window. We use it to revisit several risk and portfolio metrics for improved control over tail events. On [τUV,τIR][\tau\_{\mathrm{UV}},\tau\_{\mathrm{IR}}], the returns admit a location-scale representation with a standardized α\alpha-stable driver and scale τ1/α\tau^{1/\alpha}. Beyond the window, the dispersion aggregates towards a finite-variance τ\sqrt{\tau} regime. Section 2 identifies the window and scaling index: (i) a log-slope of the mode mass that is equal to −1/α-1/\alpha, and (ii) a fit of a homogeneous scale that locates the ultraviolet and infrared cutoffs. With an anchor horizon τ0\tau\_{0} fixed inside the window, Section [4](https://arxiv.org/html/2511.07834v1#S4 "4 Lévy-Stable Approach to Risk and Performance Metrics ‣ Lévy-stable scaling of risk and performance functionals") derives horizon-correct formulas for six widely used functionals: Value at Risk, Expected Shortfall, pp-Sharpe and pp-Information ratios under fractional dispersion, Kelly leverage under a Value-at-Risk constraint, and drawdown functionals. In each case, Gaussian propagation differs from the correct law by an explicit bias term proportional to [(τ/τ0)1/α−(τ/τ0)1/2]\left[(\tau/\tau\_{0})^{1/\alpha}-(\tau/\tau\_{0})^{1/2}\right], making the error measurable.

It is a framework that isolates an empirically justified Lévy window, provides consistent estimators for its parameters, and supplies closed-form, horizon-correct versions of standard risk and performance metrics. The results connect the classical Gaussian formulas to their Lévy counterparts and make the horizon dependence explicit.

## 2 Setup and Regimes

Let (Xt)t≥0(X\_{t})\_{t\geq 0} be the log price and for τ>0\tau>0 define the log return

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rτ:=Xt+τ−Xt.R\_{\tau}:=X\_{t+\tau}-X\_{t}. |  | (2.1) |

Write ℙτ\mathbb{P}\_{\tau} and fτf\_{\tau} for the law and density of RτR\_{\tau} when they exist. Let SS denote a location-invariant, positively homogeneous scale functional such as the median absolute deviation or the interquartile range, and set

|  |  |  |
| --- | --- | --- |
|  | Sτ:=S​(Rτ−𝔼​Rτ).S\_{\tau}:=S\big(R\_{\tau}-\mathbb{E}R\_{\tau}\big). |  |

The scale SτS\_{\tau} will be used to localize the ultraviolet and infrared cutoffs via g​(τ)=log⁡Sτg(\tau)=\log S\_{\tau} and, as a robustness check, to verify the slope 1/α1/\alpha on the window.

We consider two regimes separated by cutoffs. The ultraviolet cutoff τUV>0\tau\_{\mathrm{UV}}>0 is the smallest horizon above which microstructure effects such as discreteness, asynchronous trading, and bid-ask bounce do not control the dispersion law. The infrared cutoff τIR<∞\tau\_{\mathrm{IR}}<\infty is the largest horizon below which the central body still follows a Lévy-stable scaling before tempering and aggregation drive the dispersion toward a τ\sqrt{\tau} regime with finite variance. The empirical basis for the central Lévy-stable behavior is Mantegna and Stanley (1995), with related evidence in Gopikrishnan et al. (1999) and the surveys of Cont (2001) and Bouchaud and Potters (2003).

On the window [τUV,τIR][\tau\_{\mathrm{UV}},\tau\_{\mathrm{IR}}], we assume a location-scale representation with a standardized α\alpha-stable driver. The driver has index α∈(1,2)\alpha\in(1,2), skewness parameter β∈[−1,1]\beta\in[-1,1], and characteristic function

|  |  |  |
| --- | --- | --- |
|  | φZ​(u)=exp⁡{−|u|α​(1−i​β​tan⁡π​α2​sign​u)}(α≠1),\varphi\_{Z}(u)=\exp\!\left\{-|u|^{\alpha}\!\left(1-i\,\beta\,\tan\!\frac{\pi\alpha}{2}\,\mathrm{sign}\,u\right)\right\}\quad(\alpha\neq 1), |  |

with the Zolotarev modification when α=1\alpha=1, as shown by Nolan (2013) and Rachev and Mittnik (2000). Assume 𝔼​Z=0\mathbb{E}Z=0, that fZf\_{Z} exists and is continuous at the origin, and that 𝔼​|Z|p<∞\mathbb{E}|Z|^{p}<\infty holds for all p<αp<\alpha. The return process is strictly stationary and α\alpha-mixing with coefficients α​(h)→0\alpha(h)\to 0 and ∑h=1∞α​(h)δ/(2+δ)<∞\sum\_{h=1}^{\infty}\alpha(h)^{\delta/(2+\delta)}<\infty for some δ>0\delta>0, which yields uniform laws of large numbers for the frequency and scale statistics used below.

###### Assumption 2.1.

There exist 0<τUV<τIR<∞0<\tau\_{\mathrm{UV}}<\tau\_{\mathrm{IR}}<\infty, parameters α∈(1,2)\alpha\in(1,2), σ>0\sigma>0, μ∈ℝ\mu\in\mathbb{R}, and a standardized α\alpha-stable random variable ZZ with skewness β\beta such that, for all τ∈[τUV,τIR]\tau\in[\tau\_{\mathrm{UV}},\tau\_{\mathrm{IR}}],

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rτ=dμ​τ+σ​τ1/α​Z.R\_{\tau}\stackrel{{\scriptstyle d}}{{=}}\mu\tau+\sigma\,\tau^{1/\alpha}Z. |  | (2.2) |

###### Assumption 2.2.

For τ>τIR\tau>\tau\_{\mathrm{IR}} the dispersion obeys a finite-variance law

|  |  |  |
| --- | --- | --- |
|  | Sτ=C​τ​(1+o​(1))(τ→∞).S\_{\tau}=C\,\sqrt{\tau}\,\big(1+o(1)\big)\qquad(\tau\to\infty). |  |

No inference is drawn for τ<τUV\tau<\tau\_{\mathrm{UV}}.

## 3 Identification of the Window and Scaling Index

The purpose of this section is to obtain an estimator of the horizon-slope m∗m^{\ast} that equals −1/α-1/\alpha on the Lévy window, to prove that the estimator is consistent and that the fitted slope lies in the range (−1,−1/2)(-1,-1/2) corresponding to α∈(1,2)\alpha\in(1,2), and to localize the ultraviolet and infrared cutoffs. The construction relies only on the central body of the distribution and does not require second moments. The statistic P0​(τ)P\_{0}(\tau), defined as the probability mass in a fixed neighborhood of the mode, is used because it depends only on fτ​(μ​τ)f\_{\tau}(\mu\tau), is robust to tail behavior, and is first-order insensitive to skew.

We first derive the density scaling implied by ([2.2](https://arxiv.org/html/2511.07834v1#S2.E2 "In Assumption 2.1. ‣ 2 Setup and Regimes ‣ Lévy-stable scaling of risk and performance functionals")). This yields the central mass of a small neighborhood of the mode, the statistic that will generate the slope.

###### Lemma 3.1.

Under Assumption [2.1](https://arxiv.org/html/2511.07834v1#S2.Thmtheorem1 "Assumption 2.1. ‣ 2 Setup and Regimes ‣ Lévy-stable scaling of risk and performance functionals"), the density satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | fτ​(x)=σ−1​τ−1/α​fZ​(x−μ​τσ​τ1/α)for all ​x∈ℝ.f\_{\tau}(x)=\sigma^{-1}\,\tau^{-1/\alpha}\;f\_{Z}\!\left(\frac{x-\mu\tau}{\sigma\,\tau^{1/\alpha}}\right)\qquad\text{for all }x\in\mathbb{R}. |  | (3.1) |

###### Proof.

From ([2.2](https://arxiv.org/html/2511.07834v1#S2.E2 "In Assumption 2.1. ‣ 2 Setup and Regimes ‣ Lévy-stable scaling of risk and performance functionals")) one has Rτ=dμ​τ+σ​τ1/α​ZR\_{\tau}\stackrel{{\scriptstyle d}}{{=}}\mu\tau+\sigma\tau^{1/\alpha}Z. For any Borel set BB,

|  |  |  |
| --- | --- | --- |
|  | ℙ​{Rτ∈B}=ℙ​{Z∈B−μ​τσ​τ1/α}.\mathbb{P}\{R\_{\tau}\in B\}=\mathbb{P}\Big\{Z\in\frac{B-\mu\tau}{\sigma\tau^{1/\alpha}}\Big\}. |  |

Absolute continuity of ZZ implies absolute continuity of RτR\_{\tau}. The Radon-Nikodym derivative with respect to Lebesgue measure is exactly the right-hand side of ([3.1](https://arxiv.org/html/2511.07834v1#S3.E1 "In Lemma 3.1. ‣ 3 Identification of the Window and Scaling Index ‣ Lévy-stable scaling of risk and performance functionals")) by the change of variables.
∎

Fix δ>0\delta>0 and consider the central mass

|  |  |  |
| --- | --- | --- |
|  | P0​(τ):=ℙτ​(|Rτ−μ​τ|≤δ).P\_{0}(\tau):=\mathbb{P}\_{\tau}\big(|R\_{\tau}-\mu\tau|\leq\delta\big). |  |

Since fZf\_{Z} is C1C^{1} in a neighborhood of 0 and the integration window [−δ,δ][-\delta,\delta] is symmetric, the odd term in the Taylor expansion fZ​(u)=fZ​(0)+fZ′​(0)​u+O​(u2)f\_{Z}(u)=f\_{Z}(0)+f\_{Z}^{\prime}(0)u+O(u^{2}) integrates to zero, so asymmetry contributes only at order O​(τ−2/α)O(\tau^{-2/\alpha}). Using ([3.1](https://arxiv.org/html/2511.07834v1#S3.E1 "In Lemma 3.1. ‣ 3 Identification of the Window and Scaling Index ‣ Lévy-stable scaling of risk and performance functionals")) we obtain the scaling law for P0​(τ)P\_{0}(\tau).

###### Lemma 3.2.

If fZf\_{Z} is continuous at 0, then uniformly for τ∈[τUV,τIR]\tau\in[\tau\_{\mathrm{UV}},\tau\_{\mathrm{IR}}],

|  |  |  |  |
| --- | --- | --- | --- |
|  | P0​(τ)=2​δ​fZ​(0)​σ−1​τ−1/α​(1+o​(1)).P\_{0}(\tau)=2\delta\,f\_{Z}(0)\,\sigma^{-1}\,\tau^{-1/\alpha}\,(1+o(1)). |  | (3.2) |

###### Proof.

By ([3.1](https://arxiv.org/html/2511.07834v1#S3.E1 "In Lemma 3.1. ‣ 3 Identification of the Window and Scaling Index ‣ Lévy-stable scaling of risk and performance functionals")),

|  |  |  |
| --- | --- | --- |
|  | P0​(τ)=∫−δδfτ​(μ​τ+u)​𝑑u=∫−δδσ−1​τ−1/α​fZ​(uσ​τ1/α)​𝑑u.P\_{0}(\tau)=\int\_{-\delta}^{\delta}f\_{\tau}(\mu\tau+u)\,du=\int\_{-\delta}^{\delta}\sigma^{-1}\tau^{-1/\alpha}\,f\_{Z}\!\left(\frac{u}{\sigma\tau^{1/\alpha}}\right)du. |  |

Continuity at zero yields fZ​(u/(σ​τ1/α))=fZ​(0)+o​(1)f\_{Z}(u/(\sigma\tau^{1/\alpha}))=f\_{Z}(0)+o(1) uniformly in u∈[−δ,δ]u\in[-\delta,\delta], hence ([3.2](https://arxiv.org/html/2511.07834v1#S3.E2 "In Lemma 3.2. ‣ 3 Identification of the Window and Scaling Index ‣ Lévy-stable scaling of risk and performance functionals")).
∎

Taking logarithms of ([3.2](https://arxiv.org/html/2511.07834v1#S3.E2 "In Lemma 3.2. ‣ 3 Identification of the Window and Scaling Index ‣ Lévy-stable scaling of risk and performance functionals")) shows that on the window

|  |  |  |
| --- | --- | --- |
|  | log⁡P0​(τ)=c−1α​log⁡τ+o​(1),c:=log⁡(2​δ​fZ​(0)​σ−1),\log P\_{0}(\tau)\;=\;c-\frac{1}{\alpha}\,\log\tau+o(1),\qquad c:=\log\!\big(2\delta f\_{Z}(0)\sigma^{-1}\big), |  |

so the population slope of log⁡P0\log P\_{0} on log⁡τ\log\tau equals m∗=−1/αm^{\ast}=-1/\alpha.

For estimation, let {tk}k=1n\{t\_{k}\}\_{k=1}^{n} be equally spaced calendar times. For each grid horizon τj\tau\_{j} form overlapping returns Rτj​(tk)=Xtk+τj−XtkR\_{\tau\_{j}}(t\_{k})=X\_{t\_{k}+\tau\_{j}}-X\_{t\_{k}}. Overlap induces dependence, but the α\alpha-mixing condition with ∑hα​(h)δ/(2+δ)<∞\sum\_{h}\alpha(h)^{\delta/(2+\delta)}<\infty yields a uniform law of large numbers for the indicator arrays below. The indicator family {𝟏​{|Rτj​(tk)−μ​τj|≤δ}}\{\mathbf{1}\{|R\_{\tau\_{j}}(t\_{k})-\mu\tau\_{j}|\leq\delta\}\} is a VC-subgraph class; under the stated α\alpha-mixing summability, a uniform LLN holds over jj, as shown by Doukhan (1994), Bradley (2005), and Rio (2000).

Choose a fixed non-degenerate grid {τj}j=1m⊂[τUV,τIR]\{\tau\_{j}\}\_{j=1}^{m}\subset[\tau\_{\mathrm{UV}},\tau\_{\mathrm{IR}}]. Define the plug-in frequency estimator

|  |  |  |
| --- | --- | --- |
|  | P^0(n)​(τj)=1n​∑k=1n𝟏​{|Rτj​(tk)−μ​τj|≤δ},yj(n)=log⁡P^0(n)​(τj),xj=log⁡τj,\widehat{P}\_{0}^{(n)}(\tau\_{j})=\frac{1}{n}\sum\_{k=1}^{n}\mathbf{1}\big\{|R\_{\tau\_{j}}(t\_{k})-\mu\tau\_{j}|\leq\delta\big\},\quad y\_{j}^{(n)}=\log\widehat{P}\_{0}^{(n)}(\tau\_{j}),\quad x\_{j}=\log\tau\_{j}, |  |

and let m^n\widehat{m}\_{n} be the ordinary least-squares slope in the regression yj(n)=an+m^n​xj+εj,ny\_{j}^{(n)}=a\_{n}+\widehat{m}\_{n}x\_{j}+\varepsilon\_{j,n}. Since α∈(1,2)\alpha\in(1,2), the population slope satisfies m∗=−1/α∈(−1,−1/2)m^{\ast}=-1/\alpha\in(-1,-1/2); this interval is the diagnostic range for a valid Lévy window.

###### Proposition 3.3.

Under Assumption [2.1](https://arxiv.org/html/2511.07834v1#S2.Thmtheorem1 "Assumption 2.1. ‣ 2 Setup and Regimes ‣ Lévy-stable scaling of risk and performance functionals") and the mixing condition in Section [2](https://arxiv.org/html/2511.07834v1#S2 "2 Setup and Regimes ‣ Lévy-stable scaling of risk and performance functionals"),

|  |  |  |
| --- | --- | --- |
|  | m^n→ℙm∗=−1α,α^n:=−1m^n→ℙα.\widehat{m}\_{n}\xrightarrow{\mathbb{P}}m^{\ast}=-\frac{1}{\alpha},\qquad\widehat{\alpha}\_{n}:=-\frac{1}{\widehat{m}\_{n}}\xrightarrow{\mathbb{P}}\alpha. |  |

If the design {xj}\{x\_{j}\} is fixed and non-degenerate, meaning ∑j(xj−x¯)2>0\sum\_{j}(x\_{j}-\bar{x})^{2}>0, then
m​(m^n−m∗)⇒𝒩​(0,𝖵)\sqrt{m}\,(\widehat{m}\_{n}-m^{\ast})\Rightarrow\mathcal{N}(0,\mathsf{V}) for a finite 𝖵\mathsf{V}, so sandwich standard errors or a day-block bootstrap yield valid confidence intervals for α\alpha.

###### Proof.

Uniformly in jj, P^0(n)​(τj)→𝑝P0​(τj)\widehat{P}\_{0}^{(n)}(\tau\_{j})\xrightarrow{p}P\_{0}(\tau\_{j}) by a uniform LLN for α\alpha-mixing arrays, as shown by Rio (2000); hence yj(n)=log⁡P^0(n)​(τj)→𝑝yj:=log⁡P0​(τj)y\_{j}^{(n)}=\log\widehat{P}\_{0}^{(n)}(\tau\_{j})\xrightarrow{p}y\_{j}:=\log P\_{0}(\tau\_{j}) uniformly. With fixed non-degenerate design {xj}\{x\_{j}\}, the OLS slope m^n\widehat{m}\_{n} is a continuous functional of the empirical second moments; by the continuous mapping theorem m^n→𝑝m∗\widehat{m}\_{n}\xrightarrow{p}m^{\ast}. Lemma [3.2](https://arxiv.org/html/2511.07834v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3 Identification of the Window and Scaling Index ‣ Lévy-stable scaling of risk and performance functionals") gives m∗=−1/αm^{\ast}=-1/\alpha. Since x↦−1/xx\mapsto-1/x is continuous at m∗m^{\ast}, α^n=−1/m^n→𝑝α\widehat{\alpha}\_{n}=-1/\widehat{m}\_{n}\xrightarrow{p}\alpha. Asymptotic normality follows from linearization of the OLS normal equations under mixing, and the delta method gives the limit for α^n\widehat{\alpha}\_{n}.
∎

Remark. In practice one may replace μ​τ\mu\tau inside the indicator by a consistent center, such as the sample median mτm\_{\tau}. Continuity of fτf\_{\tau} at μ​τ\mu\tau implies mτ−μ​τ=op​(τ1/α)m\_{\tau}-\mu\tau=o\_{p}(\tau^{1/\alpha}), so log⁡P0​(τ)\log P\_{0}(\tau) retains slope −1/α-1/\alpha.

To locate the cutoffs, we exploit the change in slope of a homogeneous scale on the log horizon. For a fixed scale functional SS define g​(τ):=log⁡Sτg(\tau):=\log S\_{\tau}. On [τUV,τIR][\tau\_{\mathrm{UV}},\tau\_{\mathrm{IR}}], gg is approximately affine with slope 1/α1/\alpha; outside, gg has negative curvature and, in the infrared regime, approaches slope 1/21/2. Assume that the population two-segment least-squares approximation to gg on [τ¯,τ¯][\underline{\tau},\overline{\tau}] has a unique pair of kink points at (τUV,τIR)(\tau\_{\mathrm{UV}},\tau\_{\mathrm{IR}}).

###### Proposition 3.4.

Let g^n​(τ)\widehat{g}\_{n}(\tau) be the sample analogue of g​(τ)g(\tau) computed from a time series of length nn and suppose supτ∈T|g^n​(τ)−g​(τ)|→0\sup\_{\tau\in T}|\widehat{g}\_{n}(\tau)-g(\tau)|\to 0 in probability for compact T⊂(0,∞)T\subset(0,\infty). Let (τ^UV,τ^IR)(\widehat{\tau}\_{\mathrm{UV}},\widehat{\tau}\_{\mathrm{IR}}) minimize the least-squares error of a two-segment affine fit of g^n\widehat{g}\_{n} over log⁡τ∈[log⁡τ¯,log⁡τ¯]\log\tau\in[\log\underline{\tau},\log\overline{\tau}] with τ¯<τUV<τIR<τ¯\underline{\tau}<\tau\_{\mathrm{UV}}<\tau\_{\mathrm{IR}}<\overline{\tau}. Then (τ^UV,τ^IR)→ℙ(τUV,τIR)(\widehat{\tau}\_{\mathrm{UV}},\widehat{\tau}\_{\mathrm{IR}})\xrightarrow{\mathbb{P}}(\tau\_{\mathrm{UV}},\tau\_{\mathrm{IR}}).

###### Proof.

Uniform convergence of g^n\widehat{g}\_{n} to gg implies epi-convergence of the piecewise-affine objective We assume that the population two-segment objective admits a unique minimizer at (τUV,τIR)(\tau\_{\mathrm{UV}},\tau\_{\mathrm{IR}}). to its population counterpart, whose unique minimizer occurs at the true kink points. Consistency of the argmin follows by standard M-estimation arguments, as shown by van der Vaart and Wellner (1996) and Pollard (1991).
∎

The sequence of steps is, thus, as follows: fit the slope m∗m^{\ast} from the central masses {P0​(τj)}\{P\_{0}(\tau\_{j})\}; verify m∗∈(−1,−1/2)m^{\ast}\in(-1,-1/2) and, as a cross-check, fit the slope of log⁡Sτ\log S\_{\tau} on log⁡τ\log\tau to obtain 1/α∈(1/2,1)1/\alpha\in(1/2,1); then estimate the cutoffs by the two-segment fit of g​(τ)g(\tau). These calibrated objects (α^,τ^UV,τ^IR)(\widehat{\alpha},\widehat{\tau}\_{\mathrm{UV}},\widehat{\tau}\_{\mathrm{IR}}) will be used in later sections to state horizon-correct versions of the risk and portfolio metrics.

## 4 Lévy-Stable Approach to Risk and Performance Metrics

Throughout Section [4](https://arxiv.org/html/2511.07834v1#S4 "4 Lévy-Stable Approach to Risk and Performance Metrics ‣ Lévy-stable scaling of risk and performance functionals") we work under Assumption [2.1](https://arxiv.org/html/2511.07834v1#S2.Thmtheorem1 "Assumption 2.1. ‣ 2 Setup and Regimes ‣ Lévy-stable scaling of risk and performance functionals") and the mixing and empirical-process conditions stated in Section [2](https://arxiv.org/html/2511.07834v1#S2 "2 Setup and Regimes ‣ Lévy-stable scaling of risk and performance functionals"). In particular, on the Lévy window [τUV,τIR][\tau\_{\mathrm{UV}},\tau\_{\mathrm{IR}}] the scaling Rτ=dμτ+σ​τ1/α​ZR\_{\tau}\stackrel{{\scriptstyle d}}{{=}}\mu\_{\tau}+\sigma\,\tau^{1/\alpha}Z holds with a standardized α\alpha-stable ZZ.

Fix an anchor horizon τ0∈[τUV,τIR]\tau\_{0}\in[\tau\_{\mathrm{UV}},\tau\_{\mathrm{IR}}]. On the Lévy window of Section [2](https://arxiv.org/html/2511.07834v1#S2 "2 Setup and Regimes ‣ Lévy-stable scaling of risk and performance functionals") the returns satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rτ=dμτ+σ​τ1/α​Z,α∈(1,2),R\_{\tau}\stackrel{{\scriptstyle d}}{{=}}\mu\_{\tau}+\sigma\,\tau^{1/\alpha}Z,\qquad\alpha\in(1,2), |  | (4.1) |

where ZZ is a standardized α\alpha-stable random variable with continuous strictly increasing distribution function FZF\_{Z}. We write QY​(q)=inf{x:FY​(x)≥q}Q\_{Y}(q)=\inf\{x:F\_{Y}(x)\geq q\} for the qq-quantile of a random variable YY.

### 4.1 Value-at-Risk

Let Φ\Phi and ϕ\phi denote the standard normal cdf and pdf.

Value-at-Risk originated in industry through J. P. Morgan’s *RiskMetrics* (1996) and received a systematic treatment in Jorion (1997). For q∈(0,1)q\in(0,1) the (left-tail) Value-at-Risk at horizon τ\tau is

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaRτ​(q):=−QRτ​(q).\mathrm{VaR}\_{\tau}(q):=-\,Q\_{R\_{\tau}}(q). |  | (4.2) |

Rachev and Mittnik (2000) treated VaR under stable Paretian laws and emphasized that for 1<α<21<\alpha<2 the τ\sqrt{\tau} variance propagation is not defined, so quantiles must be computed directly from the α\alpha-stable law. Nolan (2013) showed numerically reliable evaluation of stable quantiles QZ​(⋅)Q\_{Z}(\cdot) and hence VaR for α\alpha-stable drivers. Our treatment differs in that we make the horizon effect explicit through τ1/α\tau^{1/\alpha}, anchor at τ0\tau\_{0}, and exhibit the exact Gaussian bias across τ\tau rather than only computing level-wise quantiles.

###### Lemma 4.1.

Under ([4.1](https://arxiv.org/html/2511.07834v1#S4.E1 "In 4 Lévy-Stable Approach to Risk and Performance Metrics ‣ Lévy-stable scaling of risk and performance functionals")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | QRτ​(q)=μτ+σ​τ1/α​QZ​(q),VaRτ​(q)=−μτ−σ​τ1/α​QZ​(q).Q\_{R\_{\tau}}(q)=\mu\_{\tau}+\sigma\,\tau^{1/\alpha}Q\_{Z}(q),\qquad\mathrm{VaR}\_{\tau}(q)=-\mu\_{\tau}-\sigma\,\tau^{1/\alpha}Q\_{Z}(q). |  | (4.3) |

###### Proof.

For x∈ℝx\in\mathbb{R}, FRτ​(x)=FZ​((x−μτ)/(σ​τ1/α))F\_{R\_{\tau}}(x)=F\_{Z}((x-\mu\_{\tau})/(\sigma\tau^{1/\alpha})). As FZF\_{Z} is continuous and strictly increasing, QZ​(FRτ​(x))=(x−μτ)/(σ​τ1/α)Q\_{Z}(F\_{R\_{\tau}}(x))=(x-\mu\_{\tau})/(\sigma\tau^{1/\alpha}). Taking x=QRτ​(q)x=Q\_{R\_{\tau}}(q) yields ([4.3](https://arxiv.org/html/2511.07834v1#S4.E3 "In Lemma 4.1. ‣ 4.1 Value-at-Risk ‣ 4 Lévy-Stable Approach to Risk and Performance Metrics ‣ Lévy-stable scaling of risk and performance functionals")).
∎

To compare with the Gaussian propagation, introduce a normal surrogate RτG∼𝒩​(μτ,σG2​τ)R\_{\tau}^{G}\sim\mathcal{N}(\mu\_{\tau},\sigma\_{G}^{2}\,\tau) whose qq-quantile is matched to ([4.3](https://arxiv.org/html/2511.07834v1#S4.E3 "In Lemma 4.1. ‣ 4.1 Value-at-Risk ‣ 4 Lévy-Stable Approach to Risk and Performance Metrics ‣ Lévy-stable scaling of risk and performance functionals")) at τ0\tau\_{0}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μτ0+σGτ0Φ−1(q)=μτ0+στ01/αQZ(q)=:Θ0(q).\mu\_{\tau\_{0}}+\sigma\_{G}\sqrt{\tau\_{0}}\,\Phi^{-1}(q)=\mu\_{\tau\_{0}}+\sigma\,\tau\_{0}^{1/\alpha}Q\_{Z}(q)=:\Theta\_{0}(q). |  | (4.4) |

Here Θ0\Theta\_{0} (and similarly Ξ0\Xi\_{0} for ES) depends only on τ0\tau\_{0}, α\alpha, and the tail level qq.

Then, for any τ>0\tau>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | QRτG​(q)=μτ+σG​τ​Φ−1​(q),VaRτG​(q)=−μτ−σG​τ​Φ−1​(q).Q^{G}\_{R\_{\tau}}(q)=\mu\_{\tau}+\sigma\_{G}\sqrt{\tau}\,\Phi^{-1}(q),\qquad\mathrm{VaR}^{G}\_{\tau}(q)=-\mu\_{\tau}-\sigma\_{G}\sqrt{\tau}\,\Phi^{-1}(q). |  | (4.5) |

###### Proposition 4.2.

With ([4.4](https://arxiv.org/html/2511.07834v1#S4.E4 "In 4.1 Value-at-Risk ‣ 4 Lévy-Stable Approach to Risk and Performance Metrics ‣ Lévy-stable scaling of risk and performance functionals")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | VaRτ​(q)−VaRτG​(q)=Θ0​(q)​[(ττ0)1/α−(ττ0)1/2].\mathrm{VaR}\_{\tau}(q)-\mathrm{VaR}^{G}\_{\tau}(q)=\Theta\_{0}(q)\left[\left(\frac{\tau}{\tau\_{0}}\right)^{1/\alpha}-\left(\frac{\tau}{\tau\_{0}}\right)^{1/2}\right]. |  | (4.6) |

Consequently, when α∈(1,2)\alpha\in(1,2) the Gaussian propagation understates tail risk on horizons τ>τ0\tau>\tau\_{0} and overstates it on τ<τ0\tau<\tau\_{0}. When α=2\alpha=2 the exponents coincide and ([4.6](https://arxiv.org/html/2511.07834v1#S4.E6 "In Proposition 4.2. ‣ 4.1 Value-at-Risk ‣ 4 Lévy-Stable Approach to Risk and Performance Metrics ‣ Lévy-stable scaling of risk and performance functionals")) vanishes, recovering the classical τ\sqrt{\tau} rule.

In implementation, Gaussian τ\sqrt{\tau} scaling produces horizon-dependent underestimation of exceedance rates on the Lévy window; replacing it by τ1/α\tau^{1/\alpha} restores uniform backtest exception frequencies across τ\tau and stabilizes capital attribution over holding periods.

### 4.2 Conditional Value-at-Risk (Expected Shortfall)

Expected Shortfall (also called CVaR) is the coherent tail functional developed by Rockafellar-Uryasev (2000) and Acerbi-Tasche (2002). Its integral form is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESτ​(q):=−1q​𝔼​[Rτ​ 1​{Rτ≤QRτ​(q)}],q∈(0,1).\mathrm{ES}\_{\tau}(q):=-\,\frac{1}{q}\,\mathbb{E}\!\left[R\_{\tau}\,\mathbf{1}\{R\_{\tau}\leq Q\_{R\_{\tau}}(q)\}\right],\qquad q\in(0,1). |  | (4.7) |

Rockafellar and Uryasev (2000) gave the convex optimization representation of ES, and Acerbi and Tasche (2002) established coherence and the integral characterization. For α\alpha-stable laws, Nolan (2013) provided accurate numerics for tail means, enabling ES to be computed directly from the stable driver. Our formula makes the horizon dependence explicit via τ1/α\tau^{1/\alpha} and connects it continuously to the finite-variance regime.

Define mZ​(q):=q−1​𝔼​[Z​ 1​{Z≤QZ​(q)}]m\_{Z}(q):=q^{-1}\mathbb{E}[Z\,\mathbf{1}\{Z\leq Q\_{Z}(q)\}], finite for α>1\alpha>1.

###### Lemma 4.3.

Under ([4.1](https://arxiv.org/html/2511.07834v1#S4.E1 "In 4 Lévy-Stable Approach to Risk and Performance Metrics ‣ Lévy-stable scaling of risk and performance functionals")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESτ​(q)=−μτ−σ​τ1/α​mZ​(q).\mathrm{ES}\_{\tau}(q)=-\mu\_{\tau}-\sigma\,\tau^{1/\alpha}m\_{Z}(q). |  | (4.8) |

For the Gaussian surrogate 𝒩​(μτ,σG2​τ)\mathcal{N}(\mu\_{\tau},\sigma\_{G}^{2}\tau),

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESτG​(q)=−μτ−σG​τ​mN​(q),mN​(q)=φ​(Φ−1​(q))q.\mathrm{ES}^{G}\_{\tau}(q)=-\mu\_{\tau}-\sigma\_{G}\sqrt{\tau}\,m\_{N}(q),\qquad m\_{N}(q)=\frac{\varphi(\Phi^{-1}(q))}{q}. |  | (4.9) |

###### Proof.

Apply the change of variable x=μτ+σ​τ1/α​zx=\mu\_{\tau}+\sigma\tau^{1/\alpha}z in ([4.7](https://arxiv.org/html/2511.07834v1#S4.E7 "In 4.2 Conditional Value-at-Risk (Expected Shortfall) ‣ 4 Lévy-Stable Approach to Risk and Performance Metrics ‣ Lévy-stable scaling of risk and performance functionals")) and use ([4.3](https://arxiv.org/html/2511.07834v1#S4.E3 "In Lemma 4.1. ‣ 4.1 Value-at-Risk ‣ 4 Lévy-Stable Approach to Risk and Performance Metrics ‣ Lévy-stable scaling of risk and performance functionals")).
∎

Matching at τ0\tau\_{0} gives στ01/αmZ(q)=σGτ0mN(q)=:Ξ0(q)\sigma\,\tau\_{0}^{1/\alpha}m\_{Z}(q)=\sigma\_{G}\sqrt{\tau\_{0}}m\_{N}(q)=:\Xi\_{0}(q) and therefore

|  |  |  |  |
| --- | --- | --- | --- |
|  | ESτ​(q)−ESτG​(q)=Ξ0​(q)​[(ττ0)1/α−(ττ0)1/2].\mathrm{ES}\_{\tau}(q)-\mathrm{ES}^{G}\_{\tau}(q)=\Xi\_{0}(q)\left[\left(\frac{\tau}{\tau\_{0}}\right)^{1/\alpha}-\left(\frac{\tau}{\tau\_{0}}\right)^{1/2}\right]. |  | (4.10) |

Thus the same qualitative bias holds for ES as for VaR on the Lévy window. Using Gaussian ES on the Lévy window systematically underallocates tail capital at longer horizons; the Lévy-correct ES aligns realized shortfall rates across τ\tau and removes artificial improvements from mere horizon changes.

### 4.3 Sharpe ratio

In this subsection we fix p∈(1,α)p\in(1,\alpha); the LpL^{p} scale is finite on the window and yields horizon-invariant ratios, whereas the classical p=2p=2 case is admissible only when α=2\alpha=2.

For a riskless benchmark with horizon-τ\tau return rτr\_{\tau}, the classical Sharpe ratio (Sharpe, 1966) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖲𝗁τ:=𝔼​[Rτ]−rτVar​(Rτ),\mathsf{Sh}\_{\tau}:=\frac{\mathbb{E}[R\_{\tau}]-r\_{\tau}}{\sqrt{\mathrm{Var}(R\_{\tau})}}, |  | (4.11) |

which is undefined on the Lévy window when α<2\alpha<2. Rachev and Mittnik (2000) pointed out that the variance diverges for 1<α<21<\alpha<2, making the classical Sharpe undefined. Stoyanov and Rachev (2005) proposed fractional lower-partial-moment denominators as a robust alternative under heavy tails; Lo (2002) analyzed sampling properties of Sharpe under dependence and non-Gaussianity but without Lévy scaling. We adopt the Lévy–Sharpe SRα=μ/σα{\rm SR}\_{\alpha}=\mu/\sigma\_{\alpha} with σα=(𝔼​|R−μ|α)1/α\sigma\_{\alpha}=(\mathbb{E}|R-\mu|^{\alpha})^{1/\alpha}, which obeys the strict-stability law σα,τ∝τ1/α\sigma\_{\alpha,\tau}\propto\tau^{1/\alpha} and is parameter-free once α\alpha is estimated.

A scale-consistent alternative is the pp-Sharpe with p∈(1,α)p\in(1,\alpha),

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖲𝗁τ,p:=𝔼​[Rτ]−rτ(𝔼​|Rτ−𝔼​[Rτ]|p)1/p.\mathsf{Sh}\_{\tau,p}:=\frac{\mathbb{E}[R\_{\tau}]-r\_{\tau}}{\left(\mathbb{E}\big|R\_{\tau}-\mathbb{E}[R\_{\tau}]\big|^{\,p}\right)^{1/p}}. |  | (4.12) |

###### Lemma 4.4.

Under ([4.1](https://arxiv.org/html/2511.07834v1#S4.E1 "In 4 Lévy-Stable Approach to Risk and Performance Metrics ‣ Lévy-stable scaling of risk and performance functionals")) with α∈(1,2)\alpha\in(1,2) and any fixed p∈(1,α)p\in(1,\alpha),

|  |  |  |
| --- | --- | --- |
|  | 𝔼​|Rτ−𝔼​[Rτ]|p=(σ​τ1/α)p​cZ,p,𝖲𝗁τ,p=𝔼​[Rτ]−rτσ​τ1/α​cZ,p1/p,\mathbb{E}\big|R\_{\tau}-\mathbb{E}[R\_{\tau}]\big|^{\,p}=(\sigma\,\tau^{1/\alpha})^{p}\,c\_{Z,p},\qquad\mathsf{Sh}\_{\tau,p}=\frac{\mathbb{E}[R\_{\tau}]-r\_{\tau}}{\sigma\,\tau^{1/\alpha}\,c\_{Z,p}^{1/p}}, |  |

where cZ,p:=𝔼​|Z−𝔼​Z|p∈(0,∞)c\_{Z,p}:=\mathbb{E}|Z-\mathbb{E}Z|^{p}\in(0,\infty).

For a Gaussian surrogate RτG∼𝒩​(μτ,σG2​τ)R\_{\tau}^{G}\sim\mathcal{N}(\mu\_{\tau},\sigma\_{G}^{2}\tau) matched at τ0\tau\_{0} by the pp-norm
σ​τ01/α​cZ,p1/p=σG​τ0​cN,p1/p\sigma\,\tau\_{0}^{1/\alpha}c\_{Z,p}^{1/p}=\sigma\_{G}\sqrt{\tau\_{0}}\,c\_{N,p}^{1/p} with cN,p:=𝔼​|N|pc\_{N,p}:=\mathbb{E}|N|^{p}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖲𝗁τ,p−𝖲𝗁τ,pG=𝔼​[Rτ]−rτΘp​(τ0)​[(ττ0)−1/α−(ττ0)−1/2],Θp​(τ0):=σ​τ01/α​cZ,p1/p,\mathsf{Sh}\_{\tau,p}-\mathsf{Sh}^{G}\_{\tau,p}=\frac{\mathbb{E}[R\_{\tau}]-r\_{\tau}}{\Theta\_{p}(\tau\_{0})}\left[\left(\frac{\tau}{\tau\_{0}}\right)^{-1/\alpha}-\left(\frac{\tau}{\tau\_{0}}\right)^{-1/2}\right],\quad\Theta\_{p}(\tau\_{0}):=\sigma\,\tau\_{0}^{1/\alpha}c\_{Z,p}^{1/p}, |  | (4.13) |

so a Gaussian propagation overstates Sharpe for long horizons on the window (τ>τ0\tau>\tau\_{0}) and understates it for τ<τ0\tau<\tau\_{0}. On the Lévy window, SRα{\rm SR}\_{\alpha} is horizon-invariant and reorders strategies primarily by tail thickness; Gaussian annualization with τ\sqrt{\tau} spuriously depresses Sharpe as τ\tau grows when α<2\alpha<2, a distortion removed by the τ1/α\tau^{1/\alpha} scale.

### 4.4 Information ratio

Let BτB\_{\tau} denote the benchmark return and define the active return Aτ:=Rτ−BτA\_{\tau}:=R\_{\tau}-B\_{\tau}.
Classically,

|  |  |  |
| --- | --- | --- |
|  | 𝖨𝖱τ=𝔼​[Aτ]Var​(Aτ),\mathsf{IR}\_{\tau}\;=\;\frac{\mathbb{E}[A\_{\tau}]}{\sqrt{\mathrm{Var}(A\_{\tau})}}, |  |

as formalized by Grinold (1989) and by Grinold and Kahn (1999). Robust variants replace the variance by alternative scales, but explicit Lévy-stable propagation for active returns is typically unstated.

On the Lévy window we model AτA\_{\tau} as location-scale stable,

|  |  |  |
| --- | --- | --- |
|  | Aτ=dmτ+σA​τ1/αA​ZA,A\_{\tau}\stackrel{{\scriptstyle d}}{{=}}m\_{\tau}+\sigma\_{A}\,\tau^{1/\alpha\_{A}}\,Z\_{A}, |  |

with standardized ZAZ\_{A} and tail index αA∈(1,2)\alpha\_{A}\in(1,2). When (Rτ,Bτ)(R\_{\tau},B\_{\tau}) is jointly α\alpha-stable, one has αA=α\alpha\_{A}=\alpha; otherwise all propagation and bias expressions below hold with α\alpha replaced by αA\alpha\_{A}.

Fix p∈(1,αA)p\in(1,\alpha\_{A}); the LpL^{p} scale is finite on the window (the classical variance case p=2p=2 is admissible only when αA=2\alpha\_{A}=2). Define the pp-Information ratio

|  |  |  |
| --- | --- | --- |
|  | 𝖨𝖱τ,p:=𝔼​[Aτ](𝔼​|Aτ−𝔼​[Aτ]|p)1/p=𝔼​[Aτ]σA​τ1/αA​cA,p1/p,cA,p:=𝔼​|ZA−𝔼​ZA|p.\mathsf{IR}\_{\tau,p}:=\frac{\mathbb{E}[A\_{\tau}]}{\big(\mathbb{E}\lvert A\_{\tau}-\mathbb{E}[A\_{\tau}]\rvert^{\,p}\big)^{1/p}}=\frac{\mathbb{E}[A\_{\tau}]}{\sigma\_{A}\,\tau^{1/\alpha\_{A}}\,c\_{A,p}^{1/p}},\qquad c\_{A,p}:=\mathbb{E}\lvert Z\_{A}-\mathbb{E}Z\_{A}\rvert^{p}. |  |

Anchoring a Gaussian surrogate for AτA\_{\tau} at τ0\tau\_{0} yields the same exponent gap as for Sharpe, now with αA\alpha\_{A}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖨𝖱τ,p−𝖨𝖱τ,pG=𝔼​[Aτ]ΘA,p​(τ0)​[(ττ0)−1/αA−(ττ0)−1/2],ΘA,p​(τ0):=σA​τ01/αA​cA,p1/p.\mathsf{IR}\_{\tau,p}-\mathsf{IR}^{G}\_{\tau,p}=\frac{\mathbb{E}[A\_{\tau}]}{\Theta\_{A,p}(\tau\_{0})}\left[\left(\frac{\tau}{\tau\_{0}}\right)^{-1/\alpha\_{A}}-\left(\frac{\tau}{\tau\_{0}}\right)^{-1/2}\right],\qquad\Theta\_{A,p}(\tau\_{0}):=\sigma\_{A}\,\tau\_{0}^{1/\alpha\_{A}}c\_{A,p}^{1/p}. |  | (4.14) |

We thus use an αA\alpha\_{A}-consistent dispersion in the denominator; Gaussian τ\sqrt{\tau} propagation artificially improves 𝖨𝖱τ,p\mathsf{IR}\_{\tau,p} as τ\tau increases on heavy-tailed active signals, whereas the Lévy propagation preserves the correct horizon scaling.

### 4.5 Kelly criterion

For a fraction f∈ℝf\in\mathbb{R} invested in the risky leg with one-period excess return Xτ:=Rτ−rτX\_{\tau}:=R\_{\tau}-r\_{\tau}, the Kelly log-growth is

|  |  |  |
| --- | --- | --- |
|  | gτ​(f):=𝔼​[log⁡(1+f​Xτ)],g\_{\tau}(f):=\mathbb{E}\big[\log(1+fX\_{\tau})\big], |  |

as introduced by Kelly (1956). We interpret XτX\_{\tau} as a simple excess return, so Xτ≥−1X\_{\tau}\geq-1 almost surely; hence gτ​(f)g\_{\tau}(f) is well defined on f∈[0,1)f\in[0,1). Allowing leverage f>1f>1 or modeling additive/log returns reintroduces the possibility that 1+f​Xτ≤01+fX\_{\tau}\leq 0 with positive probability and the pathology below. MacLean, Thorp and Ziemba (2011) emphasized practical risk constraints and fractional-Kelly usage under heavy tails, and Peters (2011) highlighted time-average growth pitfalls in fat-tailed settings.

###### Proposition 4.5.

If either *(i)* Xτ≥−1X\_{\tau}\geq-1 almost surely and ℙ​(Xτ<−1/f)>0\mathbb{P}(X\_{\tau}<-1/f)>0 for some f>1f>1, or *(ii)* XτX\_{\tau} has unbounded left support (e.g., an additive/log-return model), then gτ​(f)=−∞g\_{\tau}(f)=-\infty for that ff. In particular, the unconstrained optimum is not well defined once the feasible set includes such ff.

Indeed, on {Xτ<−1/f}\{X\_{\tau}<-1/f\} one has log⁡(1+f​Xτ)=−∞\log(1+fX\_{\tau})=-\infty, which forces 𝔼​[log⁡(1+f​Xτ)]=−∞\mathbb{E}[\log(1+fX\_{\tau})]=-\infty.

To align with the Lévy-correct risk metrics of Section [4.1](https://arxiv.org/html/2511.07834v1#S4.SS1 "4.1 Value-at-Risk ‣ 4 Lévy-Stable Approach to Risk and Performance Metrics ‣ Lévy-stable scaling of risk and performance functionals"), we adopt a one-step no-bankruptcy constraint at tail level q∈(0,1/2)q\in(0,1/2):

|  |  |  |
| --- | --- | --- |
|  | maxf∈ℝ⁡𝔼​[log⁡(1+f​Xτ)]subject to1+f​VaRτ​(q)≥0,\max\_{f\in\mathbb{R}}~\mathbb{E}\!\left[\log(1+fX\_{\tau})\right]\quad\text{subject to}\quad 1+f\,\mathrm{VaR}\_{\tau}(q)\geq 0, |  |

where VaRτ​(q)\mathrm{VaR}\_{\tau}(q) is the Lévy-correct quantile. The feasible set is

|  |  |  |
| --- | --- | --- |
|  | ℱτ​(q)={f: 0≤f≤fmax​(τ,q)},fmax​(τ,q):=1|VaRτ​(q)|.\mathcal{F}\_{\tau}(q)=\bigl\{f:\ 0\leq f\leq f\_{\max}(\tau,q)\bigr\},\qquad f\_{\max}(\tau,q):=\frac{1}{\lvert\mathrm{VaR}\_{\tau}(q)\rvert}. |  |

###### Lemma 4.6.

If f∈ℱτ​(q)f\in\mathcal{F}\_{\tau}(q) and 𝔼​|Xτ|<∞\mathbb{E}\lvert X\_{\tau}\rvert<\infty, then gτg\_{\tau} is strictly concave on ℱτ​(q)\mathcal{F}\_{\tau}(q) and the unique maximizer fτ∗​(q)f^{\ast}\_{\tau}(q) satisfies

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Xτ1+fτ∗​(q)​Xτ]=0,0≤fτ∗​(q)≤fmax​(τ,q).\mathbb{E}\!\left[\frac{X\_{\tau}}{1+f^{\ast}\_{\tau}(q)\,X\_{\tau}}\right]=0,\qquad 0\leq f^{\ast}\_{\tau}(q)\leq f\_{\max}(\tau,q). |  |

For small signal relative to scale, a second-order expansion that replaces the divergent second moment by its qq-trimmed counterpart yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | fτ∗​(q)=𝔼​[Xτ]𝔼​[Xτ 2​ 1​{|Xτ|≤cq​σ​τ1/α}]+o​(1)=μτ−rτKq​σ2​τ2/α+o​(τ−2/α),f^{\ast}\_{\tau}(q)=\frac{\mathbb{E}[X\_{\tau}]}{\mathbb{E}\!\big[X\_{\tau}^{\,2}\,\mathbf{1}\{|X\_{\tau}|\leq c\_{q}\,\sigma\,\tau^{1/\alpha}\}\big]}+o(1)=\frac{\mu\_{\tau}-r\_{\tau}}{K\_{q}\,\sigma^{2}\,\tau^{2/\alpha}}+o\!\left(\tau^{-2/\alpha}\right), |  | (4.15) |

where cq:=|QZ​(q)|c\_{q}:=\lvert Q\_{Z}(q)\rvert and Kq:=𝔼​[Z2​ 1​{|Z|≤cq}]K\_{q}:=\mathbb{E}[Z^{2}\,\mathbf{1}\{|Z|\leq c\_{q}\}] depends only on qq. In particular, if μτ=μ​τ\mu\_{\tau}=\mu\,\tau, then

|  |  |  |
| --- | --- | --- |
|  | fτ∗​(q)≍τ 1−2/α,f^{\ast}\_{\tau}(q)\asymp\tau^{\,1-2/\alpha}, |  |

which decreases with τ\tau on the Lévy window for α∈(1,2)\alpha\in(1,2) and reduces to horizon-invariance when α=2\alpha=2.

The VaR-constrained formulation avoids distribution editing and is consistent with the Lévy scaling. On the window, admissible leverage shrinks like τ−1/α\tau^{-1/\alpha} and the optimal fraction scales like τ1−2/α\tau^{1-2/\alpha}. Beyond the window, where aggregation yields finite-variance propagation, the classical unconstrained quadratic approximation is admissible on a fixed bounded feasible set f∈[0,1)f\in[0,1).

### 4.6 Drawdown

For a single horizon τ\tau, define the one-step drawdown magnitude Dτ:=(−Rτ)+=max⁡{−Rτ,0}D\_{\tau}:=(-R\_{\tau})\_{+}=\max\{-R\_{\tau},0\}. For p∈(0,α)p\in(0,\alpha) the LpL^{p}-drawdown is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖣𝖣τ,p:=(𝔼​(Dτ)p)1/p.\mathsf{DD}\_{\tau,p}:=\left(\mathbb{E}\,(D\_{\tau})^{p}\right)^{1/p}. |  | (4.16) |

Magdon-Ismail and Atiya (2004) analyzed maximum drawdown for random walks and provided distributional approximations, and Chekhlov, Uryasev and Zabarankin (2005) introduced Conditional Drawdown at Risk (CDaR) as a convex drawdown risk measure. On the Lévy window we focus on the one-step drawdown, which inherits the strict-stability scaling. Multi-step generalizations preserve the scaling exponent but depend on the temporal dependence structure.

###### Lemma 4.7.

Under ([4.1](https://arxiv.org/html/2511.07834v1#S4.E1 "In 4 Lévy-Stable Approach to Risk and Performance Metrics ‣ Lévy-stable scaling of risk and performance functionals")), for any p∈(0,α)p\in(0,\alpha),

|  |  |  |
| --- | --- | --- |
|  | 𝖣𝖣τ,p=σ​τ1/α​dZ,p+O​(|μτ|),dZ,p:=(𝔼​(−Z)+p)1/p.\mathsf{DD}\_{\tau,p}=\sigma\,\tau^{1/\alpha}\,d\_{Z,p}+O(|\mu\_{\tau}|),\qquad d\_{Z,p}:=\left(\mathbb{E}\,(\!-Z)\_{+}^{\,p}\right)^{1/p}. |  |

In particular, if |μτ|=o​(τ1/α)|\mu\_{\tau}|=o(\tau^{1/\alpha}) as τ↓0\tau\downarrow 0 on the high-frequency end of the window, then 𝖣𝖣τ,p∼σ​τ1/α​dZ,p\mathsf{DD}\_{\tau,p}\sim\sigma\,\tau^{1/\alpha}\,d\_{Z,p}.

The drawdown quantile at level q∈(0,1)q\in(0,1) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝖣𝖣τ(q):=QDτ​(q)=(−QRτ​(1−q))+=(−μτ−σ​τ1/α​QZ​(1−q))+,\mathsf{DD}\_{\tau}^{(q)}:=Q\_{D\_{\tau}}(q)=\left(-Q\_{R\_{\tau}}(1-q)\right)\_{+}=\left(-\mu\_{\tau}-\sigma\,\tau^{1/\alpha}Q\_{Z}(1-q)\right)\_{+}, |  | (4.17) |

so, under the Gaussian surrogate matched at τ0\tau\_{0}, it differs by the same exponent gap as in ([4.6](https://arxiv.org/html/2511.07834v1#S4.E6 "In Proposition 4.2. ‣ 4.1 Value-at-Risk ‣ 4 Lévy-Stable Approach to Risk and Performance Metrics ‣ Lévy-stable scaling of risk and performance functionals")) with q↦1−qq\mapsto 1-q.

Gaussian τ\sqrt{\tau} scaling understates high-quantile drawdowns as τ\tau grows on heavy-tailed data; the Lévy drawdown corrects exceedance frequencies and improves calibration of stop-loss and liquidation buffers across horizons.

## 5 Concluding remarks

We posited a finite-horizon model with a data-driven Lévy window [τUV,τIR][\tau\_{\mathrm{UV}},\tau\_{\mathrm{IR}}] on which
Rτ=dμτ+σ​τ1/α​ZR\_{\tau}\stackrel{{\scriptstyle d}}{{=}}\mu\_{\tau}+\sigma\,\tau^{1/\alpha}Z with a standardized α\alpha-stable driver. The window and α\alpha are identified from central-mass and piecewise-scale slopes, and an anchor τ0\tau\_{0} fixes the level. Closed-form, horizon-correct formulas were derived for VaR, ES, pp-Sharpe, pp-Information, Kelly under a Value-at-Risk constraint, and drawdown; in each case the Gaussian propagation differs by an explicit exponent-gap term (τ/τ0)1/α−(τ/τ0)1/2(\tau/\tau\_{0})^{1/\alpha}-(\tau/\tau\_{0})^{1/2}.

Empirically, the Lévy propagation delivers flat exception rates for VaR and ES across horizons on the window, horizon-invariant pp-Sharpe and pp-Information ratios, Kelly fractions that decay with τ\tau as τ1−2/α\tau^{1-2/\alpha}, and drawdown thresholds whose realized breach frequencies match their design levels. The construction is model-light: beyond estimating α\alpha and choosing a small set of tail quantiles, all metrics are propagated nonparametrically by the strict-stability scale law on the Lévy window.

Further research should address estimation error in α\alpha and window edges, nonstationarity across regimes, and dependence beyond the one-step setting. Natural extensions include multivariate Lévy windows via spectral measures, multi-step drawdown through ladder-variable methods, and state-dependent α​(τ)\alpha(\tau) with stability tests controlling for microstructure effects.

## References

* [1]

  Acerbi, C. and Tasche, D. (2002), ‘On the coherence of expected shortfall’, Journal of Banking and Finance 26(7), 1487–1503.
* [2]

  Bouchaud, J.-P. and Potters, M. (2003), Theory of Financial Risk and Derivative Pricing, Cambridge University Press.
* [3]

  Bradley, R. C. (2005), ‘Basic properties of strong mixing conditions, a survey and some open questions’, Probability Surveys 2, 107–144.
* [4]

  Chekhlov, A., Uryasev, S. and Zabarankin, M. (2005), ‘Drawdown measure in portfolio optimization’, International Journal of Theoretical and Applied Finance 8(1), 13–58.
* [5]

  Cont, R. (2001), ‘Empirical properties of asset returns: stylized facts and statistical issues’, Quantitative Finance 1(2), 223–236.
* [6]

  Doukhan, P. (1994), Mixing-Properties and Examples, Springer.
* [7]

  Plerou, V., Gopikrishnan, P., Amaral, L. A. N., Meyer, M. and Stanley, H. E. (1999), ‘Scaling of the distribution of fluctuations of financial market indices’, Physical Review E 60(5), 5305–5316.
* [8]

  Grinold, R. C. (1989), ‘The fundamental law of active management’, Journal of Portfolio Management 15(3), 30–37.
* [9]

  Grinold, R. C. and Kahn, R. N. (1999), Active Portfolio Management, 2nd ed., McGraw-Hill.
* [10]

  Hill, B. M. (1975), ‘A simple general approach to inference about the tail of a distribution’, Annals of Statistics 3(5), 1163–1174.
* [11]

  Jorion, P. (1997), Value at Risk-The New Benchmark for Managing Financial Risk, McGraw-Hill.
* [12]

  Kelly, J. L., Jr. (1956), ‘A new interpretation of information rate’, Bell System Technical Journal 35(4), 917–926.
* [13]

  Lo, A. W. (2002), ‘The statistics of Sharpe ratios’, Financial Analysts Journal 58(4), 36–52.
* [14]

  MacLean, L. C., Thorp, E. O. and Ziemba, W. T. (eds.) (2011), The Kelly Capital Growth Investment Criterion-Theory and Practice, World Scientific.
* [15]

  Magdon-Ismail, M. and Atiya, A. F. (2004), ‘Maximum drawdown of random walks’, SIAM Journal on Scientific Computing 26(4), 178–195.
* [16]

  Mandelbrot, B. (1963), ‘The variation of certain speculative prices’, Journal of Business 36(4), 394–419.
* [17]

  Mantegna, R. N. and Stanley, H. E. (1995), ‘Scaling behavior in the dynamics of an economic index’, Nature 376(6535), 46–49.
* [18]

  Nolan, J. P. (2013), Stable Distributions-Models for Heavy Tailed Data, Birkhäuser.
* [19]

  Peters, O. (2011), ‘The time resolution of the St Petersburg paradox’, Philosophical Transactions of the Royal Society A 369(1956), 4913–4931.
* [20]

  Pollard, D. (1991), ‘Asymptotics for least absolute deviation regression estimators’, Econometric Theory 7(2), 186–199.
* [21]

  Rachev, S. T. and Mittnik, S. (2000), Stable Paretian Models in Finance, Wiley.
* [22]

  Rio, E. (2000), Théorie asymptotique des processus aléatoires faiblement dépendants, Springer.
* [23]

  J. P. Morgan (1996), RiskMetrics-Technical Document, 4th ed.
* [24]

  Rockafellar, R. T. and Uryasev, S. (2000), ‘Optimization of conditional value-at-risk’, Journal of Risk 2(1), 21–41.
* [25]

  Samorodnitsky, G. and Taqqu, M. S. (1994), Stable Non-Gaussian Random Processes, Chapman and Hall-CRC.
* [26]

  Sharpe, W. F. (1966), ‘Mutual fund performance’, Journal of Business 39(1), 119–138.
* [27]

  Stoyanov, S. V. and Rachev, S. T. (2005), ‘Portfolio management with stable distributions-beyond variance’, working monograph.
* [28]

  van der Vaart, A. W. and Wellner, J. A. (1996), Weak Convergence and Empirical Processes, Springer.