---
authors:
- Harrison Katz
doc_id: arxiv:2510.18903v1
family_id: arxiv:2510.18903
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Centered MA Dirichlet ARMA for Financial Compositions: Theory & Empirical
  Evidence'
url_abs: http://arxiv.org/abs/2510.18903v1
url_html: https://arxiv.org/html/2510.18903v1
venue: arXiv q-fin
version: 1
year: 2025
---


Harrison Katz
Forecasting, Data Science, Airbnb

###### Abstract

Observation–driven Dirichlet models for compositional time series often use the additive log–ratio (ALR) link and include a moving–average (MA) term built from ALR “residuals.” In the standard B–DARMA recursion, the usual MA regressor alr⁡(𝐘t)−𝜼t\operatorname{alr}(\mathbf{Y}\_{t})-\bm{\eta}\_{t} has nonzero conditional mean under the Dirichlet likelihood, which biases the mean path and blurs the interpretation of MA coefficients. We propose a minimal change: replace the raw regressor with a *centered* innovation ϵt∘=alr⁡(𝐘t)−𝔼​{alr⁡(𝐘t)∣𝜼t,ϕt}\bm{\epsilon}\_{t}^{\circ}=\operatorname{alr}(\mathbf{Y}\_{t})-\mathbb{E}\{\operatorname{alr}(\mathbf{Y}\_{t})\mid\bm{\eta}\_{t},\phi\_{t}\}, computable in closed form via digamma functions. Centering restores mean–zero innovations for the MA block without altering either the likelihood or the ALR link. We provide simple identities for the conditional mean and the forecast recursion, show first–order equivalence to a digamma–link DARMA while retaining a closed–form inverse to 𝝁t\bm{\mu}\_{t}, and give ready–to–use code. A weekly application to the Federal Reserve H.8 bank–asset composition compares the original (raw–MA) and centered specifications under a fixed holdout and rolling one–step origins. The centered formulation improves log predictive scores with essentially identical point error and markedly cleaner HMC diagnostics.

Keywords: Compositional time series; Dirichlet ARMA (B-DARMA); additive log–ratio (ALR); centered innovations; Bayesian forecasting; expected log predictive density (ELPD); financial compositions; H.8 bank assets.

## 1 Introduction

Compositional time series arise whenever a fixed total is allocated across categories through time. Finance and data science provide many examples: allocations of earned fees into future recognition buckets for planning and staffing, evolving market or sector shares in portfolio analytics, the distribution of transactions across settlement currencies that drives treasury, hedging, and consolidated reporting, and bank balance sheet shares such as cash, securities, loans, and other assets in the Federal Reserve’s H.8 release. Valid forecasts must respect the simplex constraints, so they must remain nonnegative and sum to one.

Classical work maps compositions to Euclidean space with log ratios. Additive, centered, and isometric log-ratio transformations enable standard multivariate tools while preserving the subcompositional coherence that practitioners care about (Aitchison, [1982](https://arxiv.org/html/2510.18903v1#bib.bib1); Egozcue et al., [2003](https://arxiv.org/html/2510.18903v1#bib.bib16)). These mappings motivate transformed VARMA and state space approaches across marketing, demographics, ecology, environmental science, and forecasting (Cargnoni et al., [1997](https://arxiv.org/html/2510.18903v1#bib.bib11); Ravishanker et al., [2001](https://arxiv.org/html/2510.18903v1#bib.bib40); Silva and Smith, [2001](https://arxiv.org/html/2510.18903v1#bib.bib42); Brunsdon and Smith, [1998](https://arxiv.org/html/2510.18903v1#bib.bib9); Mills, [2010](https://arxiv.org/html/2510.18903v1#bib.bib35); Barceló-Vidal et al., [2011](https://arxiv.org/html/2510.18903v1#bib.bib4); Koehler et al., [2010](https://arxiv.org/html/2510.18903v1#bib.bib32); Kynčlová et al., [2015](https://arxiv.org/html/2510.18903v1#bib.bib33); Snyder et al., [2017](https://arxiv.org/html/2510.18903v1#bib.bib45); AL-Dhurafi et al., [2018](https://arxiv.org/html/2510.18903v1#bib.bib2)). Modeling directly on the simplex is an alternative that avoids ad hoc renormalization and yields coherent predictive distributions. For shares and market fractions, Dirichlet regression and its variants are widely used, and there is a growing literature on Dirichlet time series in both state space and observation-driven forms (Hijazi and Jernigan, [2009](https://arxiv.org/html/2510.18903v1#bib.bib23); Grunwald et al., [1993](https://arxiv.org/html/2510.18903v1#bib.bib22); da Silva et al., [2011](https://arxiv.org/html/2510.18903v1#bib.bib14); da Silva and Rodrigues, [2015](https://arxiv.org/html/2510.18903v1#bib.bib15); Zheng and Chen, [2017](https://arxiv.org/html/2510.18903v1#bib.bib54); Morais et al., [2018](https://arxiv.org/html/2510.18903v1#bib.bib36); Giller, [2020](https://arxiv.org/html/2510.18903v1#bib.bib21); Creus-Martí et al., [2021](https://arxiv.org/html/2510.18903v1#bib.bib13); Tsagris and Stewart, [2018](https://arxiv.org/html/2510.18903v1#bib.bib47)).

Within this class, the Bayesian Dirichlet ARMA framework (B–DARMA) evolves the Dirichlet mean on the additive log-ratio (ALR) scale with a VARMA process and has been used for forecasting lead times, investigating prior sensitivity, and modeling energy mixes (Katz et al., [2024](https://arxiv.org/html/2510.18903v1#bib.bib29), [2025](https://arxiv.org/html/2510.18903v1#bib.bib30); Katz, [2025](https://arxiv.org/html/2510.18903v1#bib.bib28)). Time-varying precision accommodates volatility clustering on the simplex in a Dirichlet–ARCH spirit (Katz and Weiss, [2025](https://arxiv.org/html/2510.18903v1#bib.bib31)). These ideas connect to broader Bayesian time series references (Prado and West, [2010](https://arxiv.org/html/2510.18903v1#bib.bib38); West, [1996](https://arxiv.org/html/2510.18903v1#bib.bib53)) and to Bayesian VAR and VARMA models with shrinkage or stochastic volatility (Bańbura et al., [2010](https://arxiv.org/html/2510.18903v1#bib.bib3); Karlsson, [2013](https://arxiv.org/html/2510.18903v1#bib.bib26); Huber and Feldkircher, [2019](https://arxiv.org/html/2510.18903v1#bib.bib24); Kastner and Huber, [2020](https://arxiv.org/html/2510.18903v1#bib.bib27)). They also sit alongside generalized linear time-series designs for non-Gaussian data (Brandt and Sandler, [2012](https://arxiv.org/html/2510.18903v1#bib.bib8); Roberts and Penny, [2002](https://arxiv.org/html/2510.18903v1#bib.bib41); Chen and Lee, [2016](https://arxiv.org/html/2510.18903v1#bib.bib12); McCabe and Martin, [2005](https://arxiv.org/html/2510.18903v1#bib.bib34); Berry and West, [2020](https://arxiv.org/html/2510.18903v1#bib.bib6); Fukumoto et al., [2019](https://arxiv.org/html/2510.18903v1#bib.bib20); Silveira de Andrade et al., [2015](https://arxiv.org/html/2510.18903v1#bib.bib43)) and the volatility literature that motivates precision dynamics (Engle, [1982](https://arxiv.org/html/2510.18903v1#bib.bib18); Bollerslev, [1986](https://arxiv.org/html/2510.18903v1#bib.bib7); Nelson, [1991](https://arxiv.org/html/2510.18903v1#bib.bib37); Bauwens et al., [2006](https://arxiv.org/html/2510.18903v1#bib.bib5); Engle, [2001](https://arxiv.org/html/2510.18903v1#bib.bib17); Francq and Zakoïan, [2019](https://arxiv.org/html/2510.18903v1#bib.bib19); Silvennoinen and Teräsvirta, [2009](https://arxiv.org/html/2510.18903v1#bib.bib44); Tsay, [2005](https://arxiv.org/html/2510.18903v1#bib.bib48)).

A practical issue arises for moving-average terms under a Dirichlet likelihood. With finite precision, the conditional expectation of alr⁡(𝐘t)\operatorname{alr}(\mathbf{Y}\_{t}) is a digamma function of the concentration parameters and is not equal to the linear predictor. The commonly used regressor alr⁡(𝐲t)−𝜼t\operatorname{alr}(\mathbf{y}\_{t})-\bm{\eta}\_{t} therefore has nonzero conditional mean, which biases the conditional mean path and obscures the interpretation of MA coefficients. Frequentist Dirichlet ARMA designs sidestep this by using a digamma-based link whose inverse depends on precision and is not available in closed form (Zheng and Chen, [2017](https://arxiv.org/html/2510.18903v1#bib.bib54)). We study a minimal fix that keeps the Dirichlet likelihood and the ALR link: replace the raw regressor with a centered innovation et∘=alr⁡(𝐲t)−𝔼​{alr⁡(𝐘t)∣𝝁t,ϕt}e\_{t}^{\circ}=\operatorname{alr}(\mathbf{y}\_{t})-\mathbb{E}\{\operatorname{alr}(\mathbf{Y}\_{t})\mid\bm{\mu}\_{t},\phi\_{t}\}. The expectation has a closed form via digamma functions, so the centering is straightforward to compute, restores mean-zero innovations for the MA block, and delivers mean-consistent forecasts without changing the likelihood or requiring numerical inversion.

We evaluate with predictive tools standard in Bayesian time series. We summarize out-of-sample fit with expected log predictive density and approximate leave-future-out cross-validation (Vehtari et al., [2017](https://arxiv.org/html/2510.18903v1#bib.bib50), [2015](https://arxiv.org/html/2510.18903v1#bib.bib52); Vehtari and Ojanen, [2012](https://arxiv.org/html/2510.18903v1#bib.bib51); Bürkner et al., [2020](https://arxiv.org/html/2510.18903v1#bib.bib10)), and we report interpretable point-error summaries for compositions. The empirical study focuses on public weekly H.8 bank asset shares, compares Raw–MA and Centered–MA under identical covariates and priors, uses a fixed 104-week holdout, and then runs a rolling one-step evaluation over the last two years to accumulate differences in expected log predictive density and track coverage. The code follows modern Bayesian forecasting workflows (R Core Team, [2022](https://arxiv.org/html/2510.18903v1#bib.bib39); Stan Development Team, [2022](https://arxiv.org/html/2510.18903v1#bib.bib46); Tsay et al., [2022](https://arxiv.org/html/2510.18903v1#bib.bib49); Hyndman and Athanasopoulos, [2018](https://arxiv.org/html/2510.18903v1#bib.bib25)).

## 2 Model recap and centered innovations

Let 𝐲t=(yt​1,…,yt​J)′\mathbf{y}\_{t}=(y\_{t1},\dots,y\_{tJ})^{\prime} be a JJ–part composition. Conditional on a mean 𝝁t∈ΔJ−1\bm{\mu}\_{t}\in\Delta^{J-1} and precision ϕt>0\phi\_{t}>0,

|  |  |  |
| --- | --- | --- |
|  | 𝐲t∣𝝁t,ϕt∼Dir​(ϕt​𝝁t).\mathbf{y}\_{t}\mid\bm{\mu}\_{t},\phi\_{t}\sim\mathrm{Dir}(\phi\_{t}\bm{\mu}\_{t}). |  |

Fix a reference component j⋆j^{\star} and define alr⁡(𝐲t)∈ℝJ−1\operatorname{alr}(\mathbf{y}\_{t})\in\mathbb{R}^{J-1} by alrj⁡(𝐲t)=log⁡(yt​j/yt​j⋆)\operatorname{alr}\_{j}(\mathbf{y}\_{t})=\log(y\_{tj}/y\_{tj^{\star}}) for j≠j⋆j\neq j^{\star}. The inverse is the softmax: 𝝁t=alr−1⁡(𝜼t)\bm{\mu}\_{t}=\operatorname{alr}^{-1}(\bm{\eta}\_{t}) with (μt​j⋆,μt​j)∝(1,exp⁡ηt​j)(\mu\_{tj^{\star}},\mu\_{tj})\propto(1,\exp\eta\_{tj}).

We consider the observation–driven recursion

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜼t=∑p=1P𝐀p​{alr⁡(𝐲t−p)−𝐗t−p​𝜷}+∑q=1Q𝐁q​ϵt−q+𝐗t​𝜷,ϕt=exp⁡(𝐙t​𝜸),\bm{\eta}\_{t}=\sum\_{p=1}^{P}\mathbf{A}\_{p}\{\operatorname{alr}(\mathbf{y}\_{t-p})-\mathbf{X}\_{t-p}\bm{\beta}\}+\sum\_{q=1}^{Q}\mathbf{B}\_{q}\,\bm{\epsilon}\_{t-q}+\mathbf{X}\_{t}\bm{\beta},\qquad\phi\_{t}=\exp(\mathbf{Z}\_{t}\bm{\gamma}), |  | (1) |

with bounded, deterministic covariates 𝐗t,𝐙t\mathbf{X}\_{t},\mathbf{Z}\_{t}. In the *raw* B–DARMA, ϵtraw=alr⁡(𝐲t)−𝜼t\bm{\epsilon}\_{t}^{\text{raw}}=\operatorname{alr}(\mathbf{y}\_{t})-\bm{\eta}\_{t} drives the MA block. We instead define the *centered* innovation

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϵt∘≡alr⁡(𝐲t)−𝔼​[alr⁡(𝐘t)∣𝜼t,ϕt]=alr⁡(𝐲t)−𝐠​(𝝁t,ϕt),\bm{\epsilon}\_{t}^{\circ}\equiv\operatorname{alr}(\mathbf{y}\_{t})-\mathbb{E}\!\big[\operatorname{alr}(\mathbf{Y}\_{t})\mid\bm{\eta}\_{t},\phi\_{t}\big]=\operatorname{alr}(\mathbf{y}\_{t})-\mathbf{g}(\bm{\mu}\_{t},\phi\_{t}), |  | (2) |

where the conditional ALR mean under the Dirichlet is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐠​(𝝁t,ϕt)j=ψ​(ϕt​μt​j)−ψ​(ϕt​μt​j⋆),j≠j⋆,\mathbf{g}(\bm{\mu}\_{t},\phi\_{t})\_{j}=\psi(\phi\_{t}\mu\_{tj})-\psi(\phi\_{t}\mu\_{tj^{\star}}),\qquad j\neq j^{\star}, |  | (3) |

and ψ​(⋅)\psi(\cdot) is the digamma function. The likelihood and link remain unchanged.

## 3 Main properties

Let {ℱt}\{\mathcal{F}\_{t}\} be the natural filtration generated by {𝐲s:s≤t}\{\mathbf{y}\_{s}:s\leq t\}. Under ([1](https://arxiv.org/html/2510.18903v1#S2.E1 "In 2 Model recap and centered innovations ‣ Centered MA Dirichlet ARMA for Financial Compositions: Theory & Empirical Evidence"))–([3](https://arxiv.org/html/2510.18903v1#S2.E3 "In 2 Model recap and centered innovations ‣ Centered MA Dirichlet ARMA for Financial Compositions: Theory & Empirical Evidence")), (𝝁t,ϕt)(\bm{\mu}\_{t},\phi\_{t}) are ℱt−1\mathcal{F}\_{t-1}–measurable.

### 3.1 Dirichlet log–moment identity and conditional ALR mean

###### Lemma 1 (Dirichlet log–moment identity).

If 𝐘∼Dir​(𝜶)\mathbf{Y}\sim\mathrm{Dir}(\bm{\alpha}) with α0=∑k=1Jαk\alpha\_{0}=\sum\_{k=1}^{J}\alpha\_{k}, then

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[log⁡Yj]=ψ​(αj)−ψ​(α0),j=1,…,J.\mathbb{E}[\log Y\_{j}]=\psi(\alpha\_{j})-\psi(\alpha\_{0}),\qquad j=1,\dots,J. |  |

###### Proof.

Write the Dirichlet density as
f​(𝐲∣𝜶)=Γ​(α0)∏k=1JΓ​(αk)​∏k=1Jykαk−1f(\mathbf{y}\mid\bm{\alpha})=\dfrac{\Gamma(\alpha\_{0})}{\prod\_{k=1}^{J}\Gamma(\alpha\_{k})}\prod\_{k=1}^{J}y\_{k}^{\alpha\_{k}-1}.
The zero–score identity gives
0=𝔼​[∂log⁡f/∂αj]=−∂log⁡B​(𝜶)/∂αj+𝔼​[log⁡Yj]0=\mathbb{E}\!\left[\partial\log f/\partial\alpha\_{j}\right]=-\partial\log B(\bm{\alpha})/\partial\alpha\_{j}+\mathbb{E}[\log Y\_{j}],
where B​(𝜶)=∏k=1JΓ​(αk)/Γ​(α0)B(\bm{\alpha})=\prod\_{k=1}^{J}\Gamma(\alpha\_{k})/\Gamma(\alpha\_{0}).
Since ∂log⁡Γ​(x)/∂x=ψ​(x)\partial\log\Gamma(x)/\partial x=\psi(x),
∂log⁡B/∂αj=ψ​(αj)−ψ​(α0)\partial\log B/\partial\alpha\_{j}=\psi(\alpha\_{j})-\psi(\alpha\_{0}), proving the claim.
∎

###### Proposition 1 (Conditional ALR mean).

With 𝐘t∣𝝁t,ϕt∼Dir​(ϕt​𝝁t)\mathbf{Y}\_{t}\mid\bm{\mu}\_{t},\phi\_{t}\sim\mathrm{Dir}(\phi\_{t}\bm{\mu}\_{t}) and reference j⋆j^{\star},

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[alr⁡(𝐘t)∣𝝁t,ϕt]j=ψ​(ϕt​μt​j)−ψ​(ϕt​μt​j⋆)≡𝐠​(𝝁t,ϕt)j(j≠j⋆).\mathbb{E}\!\big[\operatorname{alr}(\mathbf{Y}\_{t})\mid\bm{\mu}\_{t},\phi\_{t}\big]\_{j}=\psi(\phi\_{t}\mu\_{tj})-\psi(\phi\_{t}\mu\_{tj^{\star}})\equiv\mathbf{g}(\bm{\mu}\_{t},\phi\_{t})\_{j}\quad(j\neq j^{\star}). |  |

Consequently, 𝔼​[alr⁡(𝐘t)∣ℱt−1]=𝐠​(𝝁t,ϕt)\mathbb{E}\!\big[\operatorname{alr}(\mathbf{Y}\_{t})\mid\mathcal{F}\_{t-1}\big]=\mathbf{g}(\bm{\mu}\_{t},\phi\_{t}).

###### Proof.

By Lemma [1](https://arxiv.org/html/2510.18903v1#Thmlemma1 "Lemma 1 (Dirichlet log–moment identity). ‣ 3.1 Dirichlet log–moment identity and conditional ALR mean ‣ 3 Main properties ‣ Centered MA Dirichlet ARMA for Financial Compositions: Theory & Empirical Evidence"), 𝔼​[log⁡Yt​j∣𝝁t,ϕt]=ψ​(ϕt​μt​j)−ψ​(ϕt)\mathbb{E}[\log Y\_{tj}\mid\bm{\mu}\_{t},\phi\_{t}]=\psi(\phi\_{t}\mu\_{tj})-\psi(\phi\_{t}).
Hence 𝔼​[alrj⁡(𝐘t)∣𝝁t,ϕt]=ψ​(ϕt​μt​j)−ψ​(ϕt​μt​j⋆)\mathbb{E}[\operatorname{alr}\_{j}(\mathbf{Y}\_{t})\mid\bm{\mu}\_{t},\phi\_{t}]=\psi(\phi\_{t}\mu\_{tj})-\psi(\phi\_{t}\mu\_{tj^{\star}}).
∎

### 3.2 Mean–zero innovations and forecast recursion

###### Proposition 2 (Mean–zero MA innovations).

The centered innovation ϵt∘\bm{\epsilon}\_{t}^{\circ} in ([2](https://arxiv.org/html/2510.18903v1#S2.E2 "In 2 Model recap and centered innovations ‣ Centered MA Dirichlet ARMA for Financial Compositions: Theory & Empirical Evidence")) satisfies 𝔼​[ϵt∘∣ℱt−1]=𝟎\mathbb{E}[\bm{\epsilon}\_{t}^{\circ}\mid\mathcal{F}\_{t-1}]=\mathbf{0}.

###### Proof.

By Proposition [1](https://arxiv.org/html/2510.18903v1#Thmprop1 "Proposition 1 (Conditional ALR mean). ‣ 3.1 Dirichlet log–moment identity and conditional ALR mean ‣ 3 Main properties ‣ Centered MA Dirichlet ARMA for Financial Compositions: Theory & Empirical Evidence"), 𝔼​[alr⁡(𝐘t)∣ℱt−1]=𝐠​(𝝁t,ϕt)\mathbb{E}[\operatorname{alr}(\mathbf{Y}\_{t})\mid\mathcal{F}\_{t-1}]=\mathbf{g}(\bm{\mu}\_{t},\phi\_{t}).
Subtracting this conditional mean yields zero.
∎

###### Proposition 3 (Forecast recursion).

Write the recursion as

|  |  |  |
| --- | --- | --- |
|  | ηt=Ct+∑q=1QBq​ϵt−q,Ct​ is ​ℱt−1​-measurable.\eta\_{t}\;=\;C\_{t}\;+\;\sum\_{q=1}^{Q}B\_{q}\,\epsilon\_{t-q},\qquad C\_{t}\text{ is }\mathcal{F}\_{t-1}\text{-measurable}. |  |

Let η^T+h∣T≡𝔼​[ηT+h∣ℱT]\widehat{\eta}\_{T+h\mid T}\equiv\mathbb{E}[\eta\_{T+h}\mid\mathcal{F}\_{T}].

(i) Centered innovations.
If ϵt=ϵt∘\epsilon\_{t}=\epsilon\_{t}^{\circ} with 𝔼​[ϵt∘∣ℱt−1]=0\mathbb{E}[\epsilon\_{t}^{\circ}\mid\mathcal{F}\_{t-1}]=0, then for any h≥1h\geq 1,

|  |  |  |
| --- | --- | --- |
|  | η^T+h∣T=𝔼​[CT+h∣ℱT]+∑q=hQBq​ϵT+h−q∘\boxed{\;\widehat{\eta}\_{T+h\mid T}=\mathbb{E}[C\_{T+h}\mid\mathcal{F}\_{T}]\;+\;\sum\_{q=h}^{Q}B\_{q}\,\epsilon\_{T+h-q}^{\circ}\;} |  |

(with the sum understood as 0 when h>Qh>Q). Only already‑realized shocks enter the mean path.

(ii) Raw residuals.
If ϵt=ϵtraw=alr⁡(yt)−ηt\epsilon\_{t}=\epsilon\_{t}^{\mathrm{raw}}=\operatorname{alr}(y\_{t})-\eta\_{t}, then with
bt≡g​(μt,ϕt)−ηtb\_{t}\equiv g(\mu\_{t},\phi\_{t})-\eta\_{t},

|  |  |  |
| --- | --- | --- |
|  | η^T+h∣T=𝔼​[CT+h∣ℱT]+∑q=hQBq​ϵT+h−qraw+∑q=1min⁡(Q,h−1)Bq​𝔼​[bT+h−q|ℱT]\boxed{\;\widehat{\eta}\_{T+h\mid T}=\mathbb{E}[C\_{T+h}\mid\mathcal{F}\_{T}]\;+\;\sum\_{q=h}^{Q}B\_{q}\,\epsilon\_{T+h-q}^{\mathrm{raw}}\;+\;\sum\_{q=1}^{\min(Q,h-1)}B\_{q}\,\mathbb{E}\!\big[b\_{T+h-q}\,\big|\,\mathcal{F}\_{T}\big]\;} |  |

so future raw residuals contribute via their nonzero conditional mean btb\_{t}.

###### Proof.

Fix h≥1h\geq 1. Expanding at T+hT+h gives

|  |  |  |
| --- | --- | --- |
|  | ηT+h=CT+h+∑q=1QBq​ϵT+h−q=CT+h+∑q=hQBq​ϵT+h−q⏟indices ≤T+∑q=1min⁡(Q,h−1)Bq​ϵT+h−q⏟indices >T.\eta\_{T+h}=C\_{T+h}+\sum\_{q=1}^{Q}B\_{q}\,\epsilon\_{T+h-q}=C\_{T+h}+\underbrace{\sum\_{q=h}^{Q}B\_{q}\,\epsilon\_{T+h-q}}\_{\text{indices }\leq T}+\underbrace{\sum\_{q=1}^{\min(Q,h-1)}B\_{q}\,\epsilon\_{T+h-q}}\_{\text{indices }>T}. |  |

Taking 𝔼[⋅∣ℱT]\mathbb{E}[\cdot\mid\mathcal{F}\_{T}],

|  |  |  |
| --- | --- | --- |
|  | η^T+h∣T=𝔼​[CT+h∣ℱT]+∑q=hQBq​ϵT+h−q+∑q=1min⁡(Q,h−1)Bq​𝔼​[ϵT+h−q∣ℱT].\widehat{\eta}\_{T+h\mid T}=\mathbb{E}[C\_{T+h}\mid\mathcal{F}\_{T}]+\sum\_{q=h}^{Q}B\_{q}\,\epsilon\_{T+h-q}+\sum\_{q=1}^{\min(Q,h-1)}B\_{q}\,\mathbb{E}[\epsilon\_{T+h-q}\mid\mathcal{F}\_{T}]. |  |

For centered innovations, 𝔼​[ϵt∘∣ℱt−1]=0\mathbb{E}[\epsilon\_{t}^{\circ}\mid\mathcal{F}\_{t-1}]=0 (Prop. 2),
and by the tower property with ℱT⊆ℱt−1\mathcal{F}\_{T}\subseteq\mathcal{F}\_{t-1} for t>Tt>T,
𝔼​[ϵT+h−q∘∣ℱT]=0\mathbb{E}[\epsilon\_{T+h-q}^{\circ}\mid\mathcal{F}\_{T}]=0 for q≤h−1q\leq h-1, yielding (i).
For raw residuals, 𝔼​[ϵtraw∣ℱt−1]=bt\mathbb{E}[\epsilon\_{t}^{\mathrm{raw}}\mid\mathcal{F}\_{t-1}]=b\_{t},
so 𝔼​[ϵT+h−qraw∣ℱT]=𝔼​[bT+h−q∣ℱT]\mathbb{E}[\epsilon\_{T+h-q}^{\mathrm{raw}}\mid\mathcal{F}\_{T}]=\mathbb{E}[b\_{T+h-q}\mid\mathcal{F}\_{T}], yielding (ii).
∎

###### Remark (One‑step case).

For h=1h=1,

|  |  |  |
| --- | --- | --- |
|  | η^T+1∣T=𝔼​[CT+1∣ℱT]+∑q=1QBq​ϵT+1−q∘,\widehat{\eta}\_{T+1\mid T}=\mathbb{E}[C\_{T+1}\mid\mathcal{F}\_{T}]+\sum\_{q=1}^{Q}B\_{q}\,\epsilon\_{T+1-q}^{\circ}, |  |

so all QQ past shocks {ϵT∘,ϵT−1∘,…,ϵT+1−Q∘}\{\epsilon\_{T}^{\circ},\epsilon\_{T-1}^{\circ},\dots,\epsilon\_{T+1-Q}^{\circ}\}
enter the forecast; none are dropped. In the raw case, add
∑q=10(⋯)=0\sum\_{q=1}^{0}(\cdots)=0, i.e., no bias term at one step.

### 3.3 Digamma–ALR expansion and first–order equivalence

###### Lemma 2 (Digamma–ALR expansion).

For each j≠j⋆j\neq j^{\star},

|  |  |  |
| --- | --- | --- |
|  | ψ​(ϕ​μj)−ψ​(ϕ​μj⋆)=log⁡μjμj⋆−12​ϕ​(1μj−1μj⋆)+O​(ϕ−2),ϕ→∞,\psi(\phi\mu\_{j})-\psi(\phi\mu\_{j^{\star}})=\log\frac{\mu\_{j}}{\mu\_{j^{\star}}}-\frac{1}{2\phi}\!\left(\frac{1}{\mu\_{j}}-\frac{1}{\mu\_{j^{\star}}}\right)+O(\phi^{-2}),\qquad\phi\to\infty, |  |

uniformly on compact subsets of the interior of the simplex.

###### Proof.

Use ψ​(x)=log⁡x−12​x+O​(x−2)\psi(x)=\log x-\tfrac{1}{2x}+O(x^{-2}) applied to x=ϕ​μjx=\phi\mu\_{j} and x⋆=ϕ​μj⋆x^{\star}=\phi\mu\_{j^{\star}}.
∎

###### Corollary 1 (First–order equivalence to digamma–link DARMA).

Let 𝜼~t=𝐠​(𝝁t,ϕt)\widetilde{\bm{\eta}}\_{t}=\mathbf{g}(\bm{\mu}\_{t},\phi\_{t}). Then 𝜼~t−𝜼t=O​(ϕt−1)\widetilde{\bm{\eta}}\_{t}-\bm{\eta}\_{t}=O(\phi\_{t}^{-1}) componentwise. Consequently, a DARMA recursion written on 𝜼~t\widetilde{\bm{\eta}}\_{t} with mean–zero innovations is first–order equivalent (in 1/ϕ1/\phi) to the centered–innovation ALR recursion.

## 4 Empirical application: Weekly H.8 bank–asset composition

Weekly H.8 balance sheet shares are a clean and useful test bed for the centered MA idea. The series are public, well curated, and available at a high enough frequency to support rolling origins. The composition has four interpretable parts that matter for risk, liquidity, and income. The last decade contains calm periods and shocks, which produces the kind of time variation in precision where centering should help. Our empirical questions are simple. First, does centering improve one–step density forecasts on the simplex relative to the raw MA construction while leaving point accuracy unchanged. Second, are the computational diagnostics cleaner under centering when we hold priors, regressors, and sampler settings fixed. Third, do any gains persist when we move from a single holdout window to a rolling evaluation with many refits.

### 4.1 Data and preprocessing

We use weekly, seasonally adjusted (SA) H.8 series from the Federal Reserve Bank of St. Louis (FRED). Our primary identifiers are TLAACBW027SBOG for total assets, CASACBW027SBOG for cash assets, and SBCACBW027SBOG for securities in bank credit, with an automatic fallback to the non–seasonally adjusted series SBCACBW027NBOG if the SA series is unavailable on a given run. To maintain consistent seasonal treatment across the composition, if the SA version of
*any* component is unavailable at runtime, we switch *all* components to their
NSA counterparts for that run; otherwise we use SA for all components. For loans we first attempt TOTLL and otherwise use LLBACBW027SBOG. We download each series as a CSV from FRED, parse the date column (DATE/date/observation\_date), and perform an inner join on calendar weeks to ensure a common support across all components. To control sampler pathologies in very long histories, we restrict the panel to the last ten calendar years of available weeks; the cutoff date is maxt⁡datet−10​years\max\_{t}\text{date}\_{t}-10\ \text{years}.

Let xt,tot,xt,cash,xt,secr,xt,loansx\_{t,\mathrm{tot}},x\_{t,\mathrm{cash}},x\_{t,\mathrm{secr}},x\_{t,\mathrm{loans}} denote the aligned level series. We define the residual “Other” level by

|  |  |  |
| --- | --- | --- |
|  | xt,other≡xt,tot−xt,cash−xt,secr−xt,loans.x\_{t,\mathrm{other}}\equiv x\_{t,\mathrm{tot}}-x\_{t,\mathrm{cash}}-x\_{t,\mathrm{secr}}-x\_{t,\mathrm{loans}}. |  |

As a data integrity check, we count rows with xt,other<0x\_{t,\mathrm{other}}<0. If more than 5%5\% of weeks are negative we abort the build and prompt the user to revisit the security/loan ID choices or SA/NSA consistency; otherwise we proceed, issuing a warning with the observed fraction.

We convert levels to raw shares by division through total assets and then enforce strict positivity with an explicit floor before renormalizing rows. Let

|  |  |  |
| --- | --- | --- |
|  | 𝐲traw=(xt,cashxt,tot,xt,secrxt,tot,xt,loansxt,tot,xt,otherxt,tot)∈[0,1]4,\mathbf{y}^{\text{raw}}\_{t}=\Big(\frac{x\_{t,\mathrm{cash}}}{x\_{t,\mathrm{tot}}},\ \frac{x\_{t,\mathrm{secr}}}{x\_{t,\mathrm{tot}}},\ \frac{x\_{t,\mathrm{loans}}}{x\_{t,\mathrm{tot}}},\ \frac{x\_{t,\mathrm{other}}}{x\_{t,\mathrm{tot}}}\Big)\in[0,1]^{4}, |  |

and set the probability floor to εprob≡10−10\varepsilon\_{\text{prob}}\equiv 10^{-10}.
We apply the floor componentwise, y~t​j=max⁡{yt​jraw,εprob}\tilde{y}\_{tj}=\max\{y^{\text{raw}}\_{tj},\varepsilon\_{\text{prob}}\}, and then renormalize

|  |  |  |
| --- | --- | --- |
|  | 𝐲t=𝐲~t∑j=14y~t​j,\mathbf{y}\_{t}=\frac{\tilde{\mathbf{y}}\_{t}}{\sum\_{j=1}^{4}\tilde{y}\_{tj}}, |  |

so that 𝐲t∈Δ3\mathbf{y}\_{t}\in\Delta^{3} and every entry is strictly positive. This ensures the support of the Dirichlet likelihood is respected and prevents log⁡0\log 0 in the ALR transform while leaving economic content unaffected; the total injected mass per row is at most 4×10−104\times 10^{-10}.

### 4.2 Exploratory composition dynamics

![Refer to caption](h8_weekly_stack_shares.png)


Figure 1: H.8 bank assets as weekly shares of total assets. Shaded bands show cash, securities, loans, and the residual other category over the last decade.

Figure [1](https://arxiv.org/html/2510.18903v1#S4.F1 "Figure 1 ‣ 4.2 Exploratory composition dynamics ‣ 4 Empirical application: Weekly H.8 bank–asset composition ‣ Centered MA Dirichlet ARMA for Financial Compositions: Theory & Empirical Evidence") plots the weekly shares of cash, securities, loans, and other assets in the H.8 aggregate over the last decade. Loans dominate the balance sheet throughout, generally near three fifths of total assets, with a visible compression around early 2020 followed by a partial recovery. Cash rises from the high teens before 2020 to roughly the low twenties by 2022, then settles slightly lower and edges up again into 2025. Securities hover in a narrow band around the low teens with mild drift, while the residual *Other* moves mechanically against loans. The ranking of components is stable over time and there are no boundary touches, so the probability floor imposed during construction does not bind in economically relevant weeks.

Two features in the figure motivate our specification choices. The first is the combination of smooth, low–frequency reallocations with episodic realignments, most notably in 2020 and again during pockets of volatility in 2025. This is where an AR(1) mean with an MA(1) shock on the ALR scale is useful. The AR captures persistent rebalancing and the MA soaks up short transients. The second is that realized ALR step sizes spike in those same episodes, which is why we drive the Dirichlet precision with a lagged, smoothed measure of ALR volatility computed without look‑ahead. The dominance and persistence of the loans share in the plot support choosing loans as the ALR reference j⋆j^{\star}, which stabilizes the transformed coordinates by anchoring them to the largest component.

### 4.3 ALR reference and unit‑root check

All modeling is on the additive log‑ratio (ALR) scale with the loans share as the reference component.
To verify weak stationarity on the ALR scale, we applied Augmented Dickey–Fuller (ADF) unit‑root tests with a drift term and six lags to each of the three ALR coordinates (cash/loans, securities/loans, other/loans). Using MacKinnon 5% critical values, the tests reject the unit‑root null for all three coordinates, indicating stationarity on the ALR scale. Table [1](https://arxiv.org/html/2510.18903v1#S4.T1 "Table 1 ‣ 4.3 ALR reference and unit‑root check ‣ 4 Empirical application: Weekly H.8 bank–asset composition ‣ Centered MA Dirichlet ARMA for Financial Compositions: Theory & Empirical Evidence") summarizes the decisions.

Table 1: ADF unit‑root tests on weekly ALR coordinates (loans as reference).

| ALR coordinate | Reject unit root at 5%? |
| --- | --- |
| cash / loans | Yes |
| securities / loans | Yes |
| other / loans | Yes |

*Notes*: ADF with drift and six lags for each coordinate. Decisions based on MacKinnon 5% critical values (critical value =−2.86=-2.86).

### 4.4 Precision regressor construction

The Dirichlet precision is time‑varying and driven by a two‑regressor design,

|  |  |  |
| --- | --- | --- |
|  | log⁡ϕt=γ0+γ1​zt,\log\phi\_{t}=\gamma\_{0}+\gamma\_{1}z\_{t}, |  |

where ztz\_{t} is a lagged, smoothed measure of realized ALR volatility. We compute one‑step ALR increments as

|  |  |  |
| --- | --- | --- |
|  | Δ​𝜼t=𝜼t−𝜼t−1(t≥2),Δ​𝜼1≡𝜼1,\Delta\bm{\eta}\_{t}=\bm{\eta}\_{t}-\bm{\eta}\_{t-1}\quad(t\geq 2),\qquad\Delta\bm{\eta}\_{1}\equiv\bm{\eta}\_{1}, |  |

and summarize them by a root‑mean‑square

|  |  |  |
| --- | --- | --- |
|  | rt≡1K​∑k=1K(Δ​ηt,k)2.r\_{t}\equiv\sqrt{\frac{1}{K}\sum\_{k=1}^{K}(\Delta\eta\_{t,k})^{2}}. |  |

We then apply a one‑sided four‑week trailing mean with equal weights,

|  |  |  |
| --- | --- | --- |
|  | r¯t(4)≡14​∑h=03rt−h,\bar{r}^{(4)}\_{t}\equiv\tfrac{1}{4}\sum\_{h=0}^{3}r\_{t-h}, |  |

implemented with a past‑only filter; the initial undefined values from the filter are filled with the first non‑missing value. To avoid look‑ahead we lag the smoother by one week,

|  |  |  |
| --- | --- | --- |
|  | ztvol≡r¯t−1(4)(t≥2),z1vol≡r¯1(4).z^{\text{vol}}\_{t}\equiv\bar{r}^{(4)}\_{t-1}\quad(t\geq 2),\qquad z^{\text{vol}}\_{1}\equiv\bar{r}^{(4)}\_{1}. |  |

To stabilize estimation and prevent leakage from the test period, we standardize ztvolz^{\text{vol}}\_{t} using only the training window: with z¯train\bar{z}\_{\text{train}} and strains\_{\text{train}} the mean and standard deviation of ztvolz^{\text{vol}}\_{t} over t≤Ttraint\leq T\_{\text{train}},

|  |  |  |
| --- | --- | --- |
|  | zt≡ztvol−z¯trainstrain,with ​strain:=1​ if ​strain≤0​ or not finite.z\_{t}\equiv\frac{z^{\text{vol}}\_{t}-\bar{z}\_{\text{train}}}{s\_{\text{train}}},\qquad\text{with }s\_{\text{train}}:=1\text{ if }s\_{\text{train}}\leq 0\text{ or not finite}. |  |

The intercept and ztz\_{t} together form the precision‑design vector 𝐙t=(1,zt)\mathbf{Z}\_{t}=(1,\ z\_{t}) with Rϕ=2R\_{\phi}=2.

#### Implementation constants.

We enforce strict positivity on the simplex with a probability floor εprob=10−10\varepsilon\_{\text{prob}}=10^{-10} before renormalization. We also guard Dirichlet shape parameters with a floor εshape=10−10\varepsilon\_{\text{shape}}=10^{-10}. These constants are used when computing the digamma centering term, evaluating log predictive densities, and simulating predictive draws; they only safeguard numerics and do not bind at economically relevant scales.

### 4.5 Competing specifications, estimation, and scoring

We estimate two observation–driven Dirichlet models that are identical in likelihood, link, covariates, and priors, and differ only in the moving–average regressor. Let J=4J=4 and K=J−1=3K=J-1=3. With loans as the ALR reference j⋆=loansj^{\star}=\mathrm{loans}, define 𝜼t=alr⁡(𝐲t)∈ℝK\bm{\eta}\_{t}=\operatorname{alr}(\mathbf{y}\_{t})\in\mathbb{R}^{K} and 𝝁t=alr−1​(𝜼t)∈ΔJ−1\bm{\mu}\_{t}=\mathrm{alr}^{-1}(\bm{\eta}\_{t})\in\Delta^{J-1}. The observation equation is

|  |  |  |
| --- | --- | --- |
|  | 𝐲t∣𝝁t,ϕt∼Dir​(ϕt​𝝁t),ϕt=exp⁡(𝐙t​𝜸),𝐙t=(1,zt),\mathbf{y}\_{t}\mid\bm{\mu}\_{t},\phi\_{t}\sim\mathrm{Dir}\!\big(\phi\_{t}\,\bm{\mu}\_{t}\big),\qquad\phi\_{t}=\exp(\mathbf{Z}\_{t}\bm{\gamma}),\quad\mathbf{Z}\_{t}=(1,\ z\_{t}), |  |

where ztz\_{t} is the one–sided 4‑week trailing mean of realized ALR volatility, lagged one week and standardized on the *training* window only (Section [4.4](https://arxiv.org/html/2510.18903v1#S4.SS4 "4.4 Precision regressor construction ‣ 4 Empirical application: Weekly H.8 bank–asset composition ‣ Centered MA Dirichlet ARMA for Financial Compositions: Theory & Empirical Evidence")). The mean recursion is a one‑lag DARMA on the ALR scale with intercept‑only 𝐗t≡1\mathbf{X}\_{t}\equiv 1; write 𝜷∈ℝK×1\bm{\beta}\in\mathbb{R}^{K\times 1} and 𝐀1,𝐁1∈ℝK×K\mathbf{A}\_{1},\mathbf{B}\_{1}\in\mathbb{R}^{K\times K}. The AR block is common:

|  |  |  |
| --- | --- | --- |
|  | 𝐀1​{alr⁡(𝐲t−1)−𝐗t−1​𝜷}.\mathbf{A}\_{1}\bigl\{\operatorname{alr}(\mathbf{y}\_{t-1})-\mathbf{X}\_{t-1}\bm{\beta}\bigr\}. |  |

The MA block differs as follows.

#### Raw–MA B–DARMA.

|  |  |  |
| --- | --- | --- |
|  | 𝜼t=𝐗t​𝜷+𝐀1​{alr⁡(𝐲t−1)−𝐗t−1​𝜷}+𝐁1​{alr⁡(𝐲t−1)−𝜼t−1}.\bm{\eta}\_{t}\;=\;\mathbf{X}\_{t}\bm{\beta}\;+\;\mathbf{A}\_{1}\{\operatorname{alr}(\mathbf{y}\_{t-1})-\mathbf{X}\_{t-1}\bm{\beta}\}\;+\;\mathbf{B}\_{1}\{\operatorname{alr}(\mathbf{y}\_{t-1})-\bm{\eta}\_{t-1}\}. |  |

#### Centered–MA B–DARMA.

|  |  |  |
| --- | --- | --- |
|  | 𝜼t=𝐗t​𝜷+𝐀1​{alr⁡(𝐲t−1)−𝐗t−1​𝜷}+𝐁1​ϵt−1∘,ϵt−1∘≡alr⁡(𝐲t−1)−𝐠​(𝝁t−1,ϕt−1),\bm{\eta}\_{t}\;=\;\mathbf{X}\_{t}\bm{\beta}\;+\;\mathbf{A}\_{1}\{\operatorname{alr}(\mathbf{y}\_{t-1})-\mathbf{X}\_{t-1}\bm{\beta}\}\;+\;\mathbf{B}\_{1}\,\bm{\epsilon}\_{t-1}^{\circ},\qquad\bm{\epsilon}\_{t-1}^{\circ}\equiv\operatorname{alr}(\mathbf{y}\_{t-1})-\mathbf{g}\!\left(\bm{\mu}\_{t-1},\phi\_{t-1}\right), |  |

with 𝐠​(𝝁,ϕ)j=ψ​(ϕ​μj)−ψ​(ϕ​μj⋆)\mathbf{g}\!\left(\bm{\mu},\phi\right)\_{j}=\psi(\phi\mu\_{j})-\psi(\phi\mu\_{j^{\star}}) the Dirichlet ALR mean from ([3](https://arxiv.org/html/2510.18903v1#S2.E3 "In 2 Model recap and centered innovations ‣ Centered MA Dirichlet ARMA for Financial Compositions: Theory & Empirical Evidence")). The likelihood, link, and inverse link are otherwise identical.

#### Priors and fixed numerical guards.

Elementwise

|  |  |  |
| --- | --- | --- |
|  | vec⁡(𝐀1)∼𝒩​(0,0.52),vec⁡(𝐁1)∼𝒩​(0,0.52),vec⁡(𝜷)∼𝒩​(0,12),𝜸∼𝒩​(𝟎,𝐈2).\operatorname{vec}(\mathbf{A}\_{1})\sim\mathcal{N}(0,0.5^{2}),\quad\operatorname{vec}(\mathbf{B}\_{1})\sim\mathcal{N}(0,0.5^{2}),\quad\operatorname{vec}(\bm{\beta})\sim\mathcal{N}(0,1^{2}),\quad\bm{\gamma}\sim\mathcal{N}(\mathbf{0},\mathbf{I}\_{2}). |  |

We floor shares at εprob=10−10\varepsilon\_{\text{prob}}=10^{-10} before row‑renormalization and floor Dirichlet shapes at εshape=10−10\varepsilon\_{\text{shape}}=10^{-10} inside predictive calculations. These constants only stabilize log\log and Γ\Gamma evaluations and never bind at the scales in H.8.

#### Estimation.

Let TT be the post‑trim sample size. We use a fixed one‑step holdout of the last Ttest=min⁡{104,⌊0.25​T⌋}T\_{\text{test}}=\min\{104,\lfloor 0.25\,T\rfloor\} weeks with Ttrain=T−TtestT\_{\text{train}}=T-T\_{\text{test}}. In both models we fit by MCMC in Stan with identical settings: 4 chains, 2,000 iterations, 1,000 warmup, adapt\_delta=0.90=0.90, max\_treedepth=12=12, init=0=0, single‑threaded math. An auto‑refit is triggered if there are any divergences, any R^>1.01\widehat{R}>1.01, or bulk ESS <400<400 on the monitored parameters; the refit doubles iterations and warmup and increases adapt\_delta by 0.010.01 up to 0.9990.999.

For a rolling one‑step evaluation over the most recent 104 weeks, we define weekly origins t0t\_{0} from max⁡{104,min\_train}\max\{104,\text{min\\_train}\} to T−1T-1. At each origin we restandardize ztz\_{t} using t≤t0t\leq t\_{0} only, refit both models on 1:t01{:}t\_{0} with a lighter sampler (2 chains, 1,200 iterations, 600 warmup, adapt\_delta=0.95=0.95, max\_treedepth=12=12), and forecast 𝐲t0+1\mathbf{y}\_{t\_{0}+1}.

#### Forecasting and scoring.

One‑step point means on the simplex are obtained by propagating posterior draws through the state recursion and alr−1​(⋅)\mathrm{alr}^{-1}(\cdot). For density scoring we use a mixture‑of‑parameters approximation:

|  |  |  |
| --- | --- | --- |
|  | lpdt=log⁡[1S​∑s=1SfDir​(𝐲t|ϕt(s)​𝝁t(s))],ELPD=∑t∈𝒯lpdt,\mathrm{lpd}\_{t}\;=\;\log\!\left[\frac{1}{S}\sum\_{s=1}^{S}f\_{\mathrm{Dir}}\!\big(\mathbf{y}\_{t}\ \big|\ \phi\_{t}^{(s)}\bm{\mu}\_{t}^{(s)}\big)\right],\qquad\mathrm{ELPD}\;=\;\sum\_{t\in\mathcal{T}}\mathrm{lpd}\_{t}, |  |

with S=400S=400 draws in the fixed holdout and S=200S=200 in the rolling exercise. Predictive 95%95\% coverage is computed by simulating 𝐲trep\mathbf{y}\_{t}^{\text{rep}} from the Dirichlet at each draw via gamma normalization and checking componentwise inclusion in the central interval. Point errors are summarized by RMSE and MAE on the full composition. All diagnostics (divergences, treedepth hits, R^\widehat{R}, bulk ESS, auto‑refits) are logged per fit.

### 4.6 Evaluation designs

We report results for two standard designs: (i) a fixed one‑step holdout using the last 104 weeks and (ii) a rolling one‑step evaluation over the most recent 104 weeks with weekly re‑estimation at each origin. The same covariates, priors, numerical guards, and scoring rules are used in both models and both designs.

## 5 Results

We compare the original B-DARMA with a raw MA regressor to the centered MA version in two complementary designs: a fixed one–step holdout of the last 104 weeks and a rolling one–step evaluation across the most recent two years of weekly H.8 data. In both designs the conditional mean for the Dirichlet composition is parameterized on the additive log–ratio (ALR) scale, the precision is time–varying via a log–linear function of lagged realized ALR volatility, and models are estimated by MCMC with identical priors and tuning, including the same auto–refit policy.

In the fixed holdout, point accuracy for the total composition is essentially tied. The centered model attains an RMSE of 0.001568 and an MAE of 0.000984, while the raw–MA model attains 0.001570 and 0.000985, respectively; the differences are at the fourth decimal place and not practically meaningful for weekly shares. Probabilistic accuracy, however, shows a measurable edge for the centered specification: the one–step expected log predictive density (ELPD) over the 104 test weeks is 785.913 versus 785.745 for the raw model, and empirical 95% coverage across components is 0.962 versus 0.952. Figure [4](https://arxiv.org/html/2510.18903v1#S6.F4 "Figure 4 ‣ Limitations and extensions. ‣ 6 Discussion ‣ Centered MA Dirichlet ARMA for Financial Compositions: Theory & Empirical Evidence") summarizes these fixed–holdout comparisons: the bars for RMSE are visually indistinguishable, yet the annotations reveal a small log–score and coverage gain in favor of centering. Sampler diagnostics reinforce the picture. With identical settings, the centered fit completes without divergent transitions, while the raw–MA fit exhibits several divergences and triggers a single auto–refit with doubled iterations and warmup, despite similar R^\hat{R} and bulk ESS elsewhere. This is consistent with the theoretical claim that subtracting the Dirichlet ALR mean removes a persistent shift from the MA regressor and smooths the posterior geometry of the MA block.

The rolling one–step experiment yields the same qualitative message in a more stringent setting. Figure [2](https://arxiv.org/html/2510.18903v1#S6.F2 "Figure 2 ‣ Limitations and extensions. ‣ 6 Discussion ‣ Centered MA Dirichlet ARMA for Financial Compositions: Theory & Empirical Evidence") plots the cumulative difference in log score, ∑s≤t{ELPDsCentered−ELPDsRaw}\sum\_{s\leq t}\{\mathrm{ELPD}\_{s}^{\text{Centered}}-\mathrm{ELPD}\_{s}^{\text{Raw}}\}, across 104 weekly origins. The curve starts near zero, spends most of the window above the axis, and ends around +0.42+0.42, indicating that small per–week advantages accumulate to a nontrivial probabilistic improvement over two years. The slope steepens during episodes of elevated ALR volatility (early 2025), precisely where the innovation centering should matter most because precision is lower and the O​(ϕ−1)O(\phi^{-1}) bias in the raw ALR residual is largest. By contrast, Figure [3](https://arxiv.org/html/2510.18903v1#S6.F3 "Figure 3 ‣ Limitations and extensions. ‣ 6 Discussion ‣ Centered MA Dirichlet ARMA for Financial Compositions: Theory & Empirical Evidence") shows that the total–share RMSE series for the two models lie almost on top of each other. Both spike in the same weeks and subsequently revert to their pre–shock level, indicating that the conditional mean dynamics are essentially matched while the predictive distributions differ in subtle but consistent ways. Empirically, coverage during the rolling window stays closer to the nominal 95% under the centered model, while the raw version slightly undercovers in volatile periods. Diagnostics in the rolling refits favor the centered specification as well: divergent transitions are rarer, maximum treedepth hits are less frequent, and the auto–refit mechanism is invoked less often, even though the rolling fits use a deliberately lighter sampler to make the exercise feasible.

Taken together, the results show that centering the MA innovation improves density forecasting, as measured by ELPD and empirical coverage, without sacrificing point accuracy, and that it does so while reducing sampler pathologies. Because the likelihood, link, and inverse link are unchanged, the computational cost per effective draw is also comparable or lower in practice.

## 6 Discussion

The empirical patterns align closely with the theoretical properties of the centered MA construction. Under a Dirichlet likelihood with finite precision ϕt\phi\_{t}, the conditional expectation of the ALR–transformed observation is a digamma function of the concentration parameters. The raw MA regressor, alr⁡(𝐲t)−𝜼t\operatorname{alr}(\mathbf{y}\_{t})-\bm{\eta}\_{t}, therefore has a nonzero conditional mean of order O​(ϕt−1)O(\phi\_{t}^{-1}) whenever 𝜼t\bm{\eta}\_{t} is interpreted as the ALR linear predictor. Feeding this biased quantity into the MA block simultaneously (i) perturbs the conditional mean path in a way that depends on the precision and on the composition itself and (ii) distorts the local curvature of the posterior for the MA coefficients, because the regressor systematically drifts away from zero. The centered innovation ϵt∘=alr⁡(𝐲t)−𝔼​{alr⁡(𝐘t)∣𝜼t,ϕt}\bm{\epsilon}\_{t}^{\circ}=\operatorname{alr}(\mathbf{y}\_{t})-\mathbb{E}\{\operatorname{alr}(\mathbf{Y}\_{t})\mid\bm{\eta}\_{t},\phi\_{t}\} removes precisely that drift. Because the correction is analytic and cheap—a pairwise subtraction of digamma functions—the likelihood, the ALR link, and its closed–form inverse back to 𝝁t\bm{\mu}\_{t} are preserved, and the computational profile is unchanged.

The fact that RMSE and MAE are virtually identical across specifications is exactly what one should expect. To first order in 1/ϕt1/\phi\_{t}, the centered recursion on the ALR scale is equivalent to running a DARMA on the digamma link *evaluated at the same mean path*. In other words, the two models share the same conditional mean to first order; the difference is in how they treat the transitory shocks that drive the MA component. Point forecasts that summarize the mean therefore move together, while density forecasts that integrate over the full Dirichlet predictive distribution penalize the small but systematic mean shift in the raw regressor. This is most visible in the rolling ELPD curve, where incremental advantages cluster in weeks with elevated realized ALR volatility and lower precision. In those periods, failing to center makes the model act as if the previous period’s innovation contained some mean signal, leading to slightly overconfident and mildly miscentered predictive distributions. Centering restores the martingale–difference property of the innovation and produces predictive densities that are better calibrated and marginally sharper, yielding a higher log score.

The computational consequences are material in practice. Divergent transitions in Hamiltonian Monte Carlo often signal that the posterior geometry has narrow, curved, or funnel–like regions. In the raw–MA specification, the MA block must reconcile a regressor that is anchored away from zero by construction with priors that implicitly shrink towards stationarity and with an ALR mean that already absorbs part of the dynamics through the AR and covariate terms. This creates unnecessary tension in the joint posterior for (𝐁,𝜷,𝜸)(\mathbf{B},\bm{\beta},\bm{\gamma}), especially when ϕt\phi\_{t} varies over time. By removing the deterministic shift from the MA regressor, the centered formulation flattens these curvatures and makes it easier for the sampler to explore the posterior with fewer divergences and fewer treedepth saturations. The improvement persists even in the rolling evaluation, where we purposefully use a lighter sampler to keep the computation manageable; in that regime, small geometric gains translate directly into fewer refits and more stable runs.

For applied work, the implication is straightforward: whenever an observation–driven Dirichlet model on the ALR scale includes an MA term, the innovation should be centered. The change is surgical, one–line, and backward–compatible with existing pipelines, yet it yields probabilistic gains that accumulate over time and cleaner computation with no penalty to point accuracy. The gains will be most pronounced in settings with moderate precision and time–varying volatility on the ALR scale, such as weekly financial compositions, market–share panels, and allocation series with episodic shocks. In high–precision regimes, the O​(ϕt−1)O(\phi\_{t}^{-1}) bias vanishes and the two specifications collapse, as our theory would predict, so centering is weakly dominant.

There are several natural extensions suggested by the H.8 results. First, the experiments here are strictly one–step; multi–step density forecasts on the simplex, scored with log scores or energy scores adapted to compositional constraints, would help quantify whether the calibration advantage persists as the horizon increases. Second, the current covariate for precision is a simple lagged smoother of realized ALR volatility; richer precision dynamics, including component–specific or seasonal volatility, may interact with the centering in interesting ways during prolonged stress episodes. Third, the reference choice for the ALR transform was fixed to the loans share because it is the largest and most persistent component; a systematic assessment of alternative references or isometric log–ratios could further stabilize inference in panels where the dominant component changes over time. Finally, hierarchical or panel versions of the model, where multiple banks, sectors, or geographies share information about the MA block and precision dynamics, would test whether the computational advantages of centering scale to higher dimensions without additional tricks.

In sum, the H.8 application demonstrates that the theoretical benefits of centering the MA innovation, mean–zero shocks under the Dirichlet likelihood and ARMA–consistent mean forecasts, translate into empirical improvements where it matters: better calibrated and higher–scoring predictive distributions, at essentially identical point accuracy and with noticeably cleaner computation. Given the minimal code change and the absence of trade–offs, centering should be regarded as the default specification for MA terms in ALR–Dirichlet time–series models.

#### Limitations and extensions.

Our analysis focuses on the MA construction; stability and ergodicity conditions for the observation–driven state should be verified as usual. Useful extensions include seasonal or calendar effects in 𝐗t\mathbf{X}\_{t}, hierarchical structures across ordered components, dynamic reference selection, and explicit handling of structural zeros. On the evaluation side, multi–step and density–forecast scoring (e.g., energy scores on the simplex) would complement the one–step design here.

![Refer to caption](rolling_elpd_cumdiff.png)


Figure 2: Rolling one–step cumulative ELPD difference (Centered −- Raw). Positive values favor the centered specification.

![Refer to caption](rolling_total_rmse.png)


Figure 3: Rolling one–step total–share RMSE by origin. The two series are nearly indistinguishable; both spike briefly in early 2025.

![Refer to caption](weekly_comparison_total.png)


Figure 4: Fixed–holdout comparison of total–share RMSE (bars) with MAE/ELPD/coverage annotations. Point accuracy is essentially tied; log score and coverage slightly favor the centered model.




Table 2: Rolling one–step summary over 104 weekly origins (Total composition).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Centered MA | Raw MA | Difference | Notes |
| ELPD (sum) | 99.57 | 99.14 | +0.424 | mean diff +0.0041+0.0041, sd 0.02350.0235 |
| Wins on ELPD | 66 vs 38 (ties: 0) | |  |  |
| RMSE (mean) | 1.169×10−31.169\!\times\!10^{-3} | 1.168×10−31.168\!\times\!10^{-3} | ≈0\approx 0 | per–origin mean |
| MAE (mean) | 7.74×10−47.74\!\times\!10^{-4} | 7.77×10−47.77\!\times\!10^{-4} | ≈0\approx 0 | per–origin mean |
| 95% Coverage (mean) | 0.9529 | 0.9505 | +0.0024 | closer to nominal |
| Divergences (total) | 16 | 119 | – | across 104 fits |
| Any divergence | 10.6% | 49.0% | – | share of origins |
| Avg attempts / origin | 1.85 | 1.95 | – | auto–refits enabled |

## Acknowledgement

The author thanks Sean Wilson, Jess Needleman and Liz Medina for helpful discussions, Ellie Mertz and Adam Liss for championing the research.

## References

* Aitchison (1982)

  Aitchison, J. (1982).
  The statistical analysis of compositional data.
  Journal of the Royal Statistical Society: Series B (Methodological) 44(2), 139–160.
* AL-Dhurafi et al. (2018)

  AL-Dhurafi, N. A., N. Masseran, and Z. H. Zamzuri (2018).
  Compositional time series analysis for air pollution index data.
  Stochastic Environmental Research and Risk Assessment 32(10), 2903–2911.
* Bańbura et al. (2010)

  Bańbura, M., D. Giannone, and L. Reichlin (2010).
  Large Bayesian vector auto regressions.
  Journal of Applied Econometrics 25(1), 71–92.
* Barceló-Vidal et al. (2011)

  Barceló-Vidal, C., L. Aguilar, and J. A. Martín-Fernández (2011).
  Compositional varima time series.
  In Compositional Data Analysis: Theory and Applications, pp. 87–101. John Wiley & Sons: Chichester.
* Bauwens et al. (2006)

  Bauwens, L., S. Laurent, and J. V. K. Rombouts (2006).
  Multivariate GARCH models: A survey.
  Journal of Applied Econometrics 21(1), 79–109.
* Berry and West (2020)

  Berry, L. R. and M. West (2020).
  Bayesian forecasting of many count-valued time series.
  Journal of Business & Economic Statistics 38(4), 872–887.
* Bollerslev (1986)

  Bollerslev, T. (1986).
  Generalized autoregressive conditional heteroskedasticity.
  Journal of Econometrics 31(3), 307–327.
* Brandt and Sandler (2012)

  Brandt, P. T. and T. Sandler (2012).
  A Bayesian Poisson vector autoregression model.
  Political Analysis 20(3), 292–315.
* Brunsdon and Smith (1998)

  Brunsdon, T. M. and T. M. F. Smith (1998).
  The time series analysis of compositional data.
  Journal of Official Statistics 14(3), 237.
* Bürkner et al. (2020)

  Bürkner, P.-C., J. Gabry, and A. Vehtari (2020).
  Approximate leave-future-out cross-validation for Bayesian time series models.
  Journal of Statistical Computation and Simulation 90(14), 2499–2523.
* Cargnoni et al. (1997)

  Cargnoni, C., P. Müller, and M. West (1997).
  Bayesian forecasting of multinomial time series through conditionally Gaussian dynamic models.
  Journal of the American Statistical Association 92, 640–647.
* Chen and Lee (2016)

  Chen, C. W. S. and S. Lee (2016).
  Generalized Poisson autoregressive models for time series of counts.
  Computational Statistics & Data Analysis 99, 51–67.
* Creus-Martí et al. (2021)

  Creus-Martí, I., A. Moya, and F. J. Santonja (2021).
  A Dirichlet autoregressive model for the analysis of microbiota time-series data.
  Complexity 2021.
* da Silva et al. (2011)

  da Silva, C. Q., H. S. Migon, and L. T. Correia (2011).
  Dynamic Bayesian beta models.
  Computational Statistics & Data Analysis 55(6), 2074–2089.
* da Silva and Rodrigues (2015)

  da Silva, C. Q. and G. S. Rodrigues (2015).
  Bayesian dynamic Dirichlet models.
  Communications in Statistics-Simulation and Computation 44(3), 787–818.
* Egozcue et al. (2003)

  Egozcue, J. J., V. Pawlowsky-Glahn, G. Mateu-Figueras, and C. Barcelo-Vidal (2003).
  Isometric logratio transformations for compositional data analysis.
  Mathematical Geology 35(3), 279–300.
* Engle (2001)

  Engle, R. (2001).
  Theoretical and empirical properties of dynamic conditional correlation multivariate GARCH.
  National Bureau of Economic Research Working Paper No. 8554.
* Engle (1982)

  Engle, R. F. (1982).
  Autoregressive conditional heteroscedasticity with estimates of the variance of united kingdom inflation.
  Econometrica 50(4), 987–1007.
* Francq and Zakoïan (2019)

  Francq, C. and J.-M. Zakoïan (2019).
  GARCH Models: Structure, Statistical Inference and Financial Applications.
  John Wiley & Sons.
* Fukumoto et al. (2019)

  Fukumoto, K., A. Beger, and W. H. Moore (2019).
  Bayesian modeling for overdispersed event-count time series.
  Behaviormetrika 46(2), 435–452.
* Giller (2020)

  Giller, G. L. (2020).
  Generalized autoregressive dirichlet multinomial models: Definition and stability.
  Available at SSRN 3512527.
* Grunwald et al. (1993)

  Grunwald, G. K., A. E. Raftery, and P. Guttorp (1993).
  Time series of continuous proportions.
  Journal of the Royal Statistical Society: Series B (Methodological) 55(1), 103–116.
* Hijazi and Jernigan (2009)

  Hijazi, R. H. and R. W. Jernigan (2009).
  Modelling compositional data using Dirichlet regression models.
  Journal of Applied Probability & Statistics 4(1), 77–91.
* Huber and Feldkircher (2019)

  Huber, F. and M. Feldkircher (2019).
  Adaptive shrinkage in Bayesian vector autoregressive models.
  Journal of Business & Economic Statistics 37(1), 27–39.
* Hyndman and Athanasopoulos (2018)

  Hyndman, R. J. and G. Athanasopoulos (2018).
  Forecasting: principles and practice.
  OTexts.
* Karlsson (2013)

  Karlsson, S. (2013).
  Forecasting with Bayesian vector autoregression.
  Handbook of Economic Forecasting 2, 791–897.
* Kastner and Huber (2020)

  Kastner, G. and F. Huber (2020).
  Sparse Bayesian vector autoregressions in huge dimensions.
  Journal of Forecasting 39(7), 1142–1165.
* Katz (2025)

  Katz, H. (2025).
  Forecasting the u.s. renewable-energy mix with an alr-bdarma compositional time-series framework.
* Katz et al. (2024)

  Katz, H., K. T. Brusch, and R. E. Weiss (2024).
  A Bayesian Dirichlet auto-regressive moving average model for forecasting lead times.
  International Journal of Forecasting 40(4), 1556–1567.
* Katz et al. (2025)

  Katz, H., L. Medina, and R. E. Weiss (2025).
  Sensitivity analysis of priors in the bayesian dirichlet auto-regressive moving average model.
  Forecasting 7(3).
* Katz and Weiss (2025)

  Katz, H. and R. E. Weiss (2025).
  A bayesian dirichlet auto-regressive conditional heteroskedasticity model for compositional time series.
* Koehler et al. (2010)

  Koehler, A. B., R. D. Snyder, J. K. Ord, and A. Beaumont (2010).
  Forecasting compositional time series with exponential smoothing methods.
  Technical report, Monash University, Department of Econometrics and Business Statistics.
* Kynčlová et al. (2015)

  Kynčlová, P., P. Filzmoser, and K. Hron (2015).
  Modeling compositional time series with vector autoregressive models.
  Journal of Forecasting 34(4), 303–314.
* McCabe and Martin (2005)

  McCabe, B. P. M. and G. M. Martin (2005).
  Bayesian predictions of low count time series.
  International Journal of Forecasting 21(2), 315–330.
* Mills (2010)

  Mills, T. C. (2010).
  Forecasting compositional time series.
  Quality & Quantity 44(4), 673–690.
* Morais et al. (2018)

  Morais, J., C. Thomas-Agnan, and M. Simioni (2018).
  Using compositional and dirichlet models for market share regression.
  Journal of Applied Statistics 45(9), 1670–1689.
* Nelson (1991)

  Nelson, D. B. (1991).
  Conditional heteroskedasticity in asset returns: A new approach.
  Econometrica 59(2), 347–370.
* Prado and West (2010)

  Prado, R. and M. West (2010).
  Time series: Modeling, Computation, and Inference.
  Chapman and Hall/CRC.
* R Core Team (2022)

  R Core Team (2022).
  R: A Language and Environment for Statistical Computing.
  Vienna, Austria: R Foundation for Statistical Computing.
* Ravishanker et al. (2001)

  Ravishanker, N., D. K. Dey, and M. Iyengar (2001).
  Compositional time series analysis of mortality proportions.
  Communications in Statistics-Theory and Methods 30(11), 2281–2291.
* Roberts and Penny (2002)

  Roberts, S. J. and W. D. Penny (2002).
  Variational Bayes for generalized autoregressive models.
  IEEE Transactions on Signal Processing 50(9), 2245–2257.
* Silva and Smith (2001)

  Silva, D. B. N. and T. M. F. Smith (2001).
  Modelling compositional time series from repeated surveys.
  Survey Methodology 27(2), 205–215.
* Silveira de Andrade et al. (2015)

  Silveira de Andrade, B., M. G. Andrade, and R. S. Ehlers (2015).
  Bayesian garma models for count data.
  Communications in Statistics: Case Studies, Data Analysis and Applications 1(4), 192–205.
* Silvennoinen and Teräsvirta (2009)

  Silvennoinen, A. and T. Teräsvirta (2009).
  Multivariate garch models.
  In Handbook of Financial Time Series, pp. 201–229. Springer.
* Snyder et al. (2017)

  Snyder, R. D., J. K. Ord, A. B. Koehler, K. R. McLaren, and A. N. Beaumont (2017).
  Forecasting compositional time series: A state space approach.
  International Journal of Forecasting 33(2), 502–512.
* Stan Development Team (2022)

  Stan Development Team (2022).
  RStan: the R interface to Stan.
  R package version 2.21.5.
* Tsagris and Stewart (2018)

  Tsagris, M. and C. Stewart (2018).
  A Dirichlet regression model for compositional data with zeros.
  Lobachevskii Journal of Mathematics 39(3), 398–412.
* Tsay (2005)

  Tsay, R. S. (2005).
  Analysis of Financial Time Series.
  John Wiley & Sons.
* Tsay et al. (2022)

  Tsay, R. S., D. Wood, and J. Lachmann (2022).
  MTS: All-Purpose Toolkit for Analyzing Multivariate Time Series (MTS) and Estimating Multivariate Volatility Models.
  R package version 1.2.1.
* Vehtari et al. (2017)

  Vehtari, A., A. Gelman, and J. Gabry (2017).
  Practical Bayesian model evaluation using leave-one-out cross-validation and waic.
  Statistics and Computing 27(5), 1413–1432.
* Vehtari and Ojanen (2012)

  Vehtari, A. and J. Ojanen (2012).
  A survey of Bayesian predictive methods for model assessment, selection and comparison.
  Statistics Surveys 6, 142–228.
* Vehtari et al. (2015)

  Vehtari, A., D. Simpson, A. Gelman, Y. Yao, and J. Gabry (2015).
  Pareto smoothed importance sampling.
  arXiv preprint arXiv:1507.02646.
* West (1996)

  West, M. (1996).
  Bayesian time series: Models and computations for the analysis of time series in the physical sciences.
  In Maximum Entropy and Bayesian Methods, pp. 23–34. Springer.
* Zheng and Chen (2017)

  Zheng, T. and R. Chen (2017).
  Dirichlet ARMA models for compositional time series.
  Journal of Multivariate Analysis 158, 31–46.