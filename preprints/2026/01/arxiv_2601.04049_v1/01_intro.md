---
authors:
- Julien Hok
- Álvaro Leitao
doc_id: arxiv:2601.04049v1
family_id: arxiv:2601.04049
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Quantum computing for multidimensional option pricing: End-to-end pipeline'
url_abs: http://arxiv.org/abs/2601.04049v1
url_html: https://arxiv.org/html/2601.04049v1
venue: arXiv q-fin
version: 1
year: 2026
---


Julien Hok
Investec Bank, UK

Álvaro Leitao
CITIC Research center, Spain
Department of Mathematics, University of A Coruña, Spain
Corresponding author: alvaro.leitao@udc.gal

(January 8, 2026)

###### Abstract

This work introduces an end-to-end framework for multi-asset option pricing that combines market-consistent risk-neutral density recovery with quantum-accelerated numerical integration. We first calibrate arbitrage-free marginal distributions from European option quotes using the Normal Inverse Gaussian (NIG) model, leveraging its analytical tractability and ability to capture skewness and fat tails. Marginals are coupled via a Gaussian copula to construct joint distributions. To address the computational bottleneck of the high-dimensional integration required to solve the option pricing formula, we employ Quantum Accelerated Monte Carlo (QAMC) techniques based on Quantum Amplitude Estimation (QAE), achieving quadratic convergence improvements over classical Monte Carlo (CMC) methods. Theoretical results establish accuracy bounds and query complexity for both marginal density estimation (via cosine-series expansions) and multidimensional pricing. Empirical tests on liquid equity entities (Credit Agricole, AXA, Michelin) confirm high calibration accuracy and demonstrate that QAMC requires 10–100 times fewer queries than classical methods for comparable precision. This study provides a practical route to integrate arbitrage-aware modelling with quantum computing, highlighting implications for scalability and future extensions to complex derivatives.

## 1 Introduction

Pricing options on multiple underlying assets is a central problem in quantitative finance, with broad relevance for risk management, structured products, and trading of multi-asset exotics. In high dimensions, classical valuation workflows (spanning construction of risk-neutral distributions, consistent interpolation/extrapolation of market surfaces, and numerical integration of complex payoffs) face significant computational and modelling challenges. A central requirement is the recovery of arbitrage-free marginal risk-neutral densities from observed vanilla options and their implied volatilities, together with a tractable and realistic representation of inter-asset dependence to obtain joint distributions suitable for pricing basket, spread, worst-of, and other path-independent multivariate payoffs. In this context, traditional approaches rely heavily on simplistic stochastic models and numerical techniques such as classical Monte Carlo (CMC) simulation, which, while robust, often suffer from lack of representativeness and high computational costs when extended to high-dimensional settings.

Two strands of progress have shaped this landscape. First, on the distributional modelling side, the industry has moved beyond lognormal assumptions, motivated by empirical features such as negative skew and fat tails in equity returns. Lévy models capture jumps and heavy tails while retaining analytical tractability through characteristic functions, facilitating Fourier-based valuation [[6](https://arxiv.org/html/2601.04049v1#bib.bib37 "Option valuation using the fast fourier transform"), [38](https://arxiv.org/html/2601.04049v1#bib.bib36 "Lévy processes in finance: pricing financial derivatives"), [14](https://arxiv.org/html/2601.04049v1#bib.bib20 "A novel pricing method for european options based on fourier–cosine series expansions"), [26](https://arxiv.org/html/2601.04049v1#bib.bib38 "Option pricing with Legendre polynomials")]. Within this class, the Normal Inverse Gaussian (NIG) model is particularly attractive: smooth densities, tuneable skew/kurtosis, arbitrage-free time-slice calibration, and empirically validated fits to equity options [[13](https://arxiv.org/html/2601.04049v1#bib.bib9 "The normal inverse gaussian distribution and the pricing of derivatives"), [30](https://arxiv.org/html/2601.04049v1#bib.bib12 "Option pricing under nig distribution: the empirical analysis of nikkei 225 option")]. These properties make NIG well-suited for constructing marginal market distributions required for multi-asset pricing. In contrast, the CMC simulation of the NIG process is not trivial and rather inefficient, specially in high dimensions. Regarding the dependence structure, in finance, it is often modelled separately from the marginals by employing copulas [[8](https://arxiv.org/html/2601.04049v1#bib.bib39 "Copula methods in finance")]. The well-known Sklar’s theorem guarantees that a copula combined with marginals yields a valid joint distribution [[35](https://arxiv.org/html/2601.04049v1#bib.bib16 "An introduction to copulas")]. Second, On the computational side, CMC methods have long been the workhorse for option pricing (see [[20](https://arxiv.org/html/2601.04049v1#bib.bib23 "Monte Carlo methods in financial engineering")]), but their slow convergence rate, O​(1/ϵ2)O(1/\epsilon^{2})), poses challenges for high accuracy in large dimensions. Native quantum algorithms, particularly those proposed in [[4](https://arxiv.org/html/2601.04049v1#bib.bib22 "Quantum amplitud amplification and estimation"), [33](https://arxiv.org/html/2601.04049v1#bib.bib21 "Quantum speedup of monte carlo methods"), [37](https://arxiv.org/html/2601.04049v1#bib.bib30 "Quantum computational finance: Monte Carlo pricing of financial derivatives")], exploit the so-called Quantum Amplitude Estimation (QAE) to achieve O​(1/ϵ)O(1/\epsilon) convergence, offering a theoretical quadratic improvement. The confluence of these strands raises a compelling question: can a market-data-driven, arbitrage-aware construction of multi-asset pricing distributions be paired with quantum-accelerated estimators to achieve practical gains in accuracy-vs-cost for multidimensional option pricing? Before describing our proposal to address this question, let us discuss some related literature review.

In order to encapsulate the market information of each individual asset, practitioners typically work with implied volatility surfaces, motivating robust interpolation/extrapolation that avoids static arbitrage. The Stochastic Volatility Inspired (SVI) parameterization [[19](https://arxiv.org/html/2601.04049v1#bib.bib3 "A parsimonious arbitrage-free implied volatility parameterization with application to the valuation of volatility derivatives")] and its arbitrage-free extensions [[18](https://arxiv.org/html/2601.04049v1#bib.bib4 "Arbitrage-free SVI volatility surfaces")] are widely adopted due to parsimony and control over convexity and butterfly arbitrage. Alternatives include local volatility bootstrapping and tied time-dependent parameters [[2](https://arxiv.org/html/2601.04049v1#bib.bib6 "Volatility interpolation"), [29](https://arxiv.org/html/2601.04049v1#bib.bib7 "Filling the gaps")], stochastic volatility families such as  [[25](https://arxiv.org/html/2601.04049v1#bib.bib40 "A closed-form solution for options with stochastic volatility with applications to bond and currency options"), [24](https://arxiv.org/html/2601.04049v1#bib.bib5 "Managing smile risk")], and all-maturities non-parametric approaches imposing global no-arbitrage constraints [[12](https://arxiv.org/html/2601.04049v1#bib.bib8 "Building arbitrage-free implied volatility: sinkhorn’s algorithm and variants")]. Regularization techniques (e.g., Tikhonov) are standard for stabilizing ill-posed calibration [[10](https://arxiv.org/html/2601.04049v1#bib.bib14 "Financial modelling with jump processes"), [11](https://arxiv.org/html/2601.04049v1#bib.bib13 "Calibration of the local volatility in a generalized black–scholes model using tikhonov regularization")]. The calibration of some of the aforementioned models is treated in, for example, [[15](https://arxiv.org/html/2601.04049v1#bib.bib42 "Static and dynamic SABR stochastic volatility models: calibration and option pricing using GPUs"), [27](https://arxiv.org/html/2601.04049v1#bib.bib44 "Calibration of local volatility model with stochastic interest rates by efficient numerical pde methods"), [28](https://arxiv.org/html/2601.04049v1#bib.bib41 "The CTMC–Heston model: calibration and exotic option pricing with SWIFT")].

Quantum computing explores how the principles of quantum mechanics can be harnessed to enhance information processing beyond classical limits. Since its inception, the field has witnessed remarkable progress in algorithm design and hardware development, driving rapid growth in quantum technologies and fuelling the search for practical applications across diverse domains. Among these emerging areas, quantitative finance has attracted significant attention as a promising candidate for quantum-enabled innovation, see [[36](https://arxiv.org/html/2601.04049v1#bib.bib43 "Quantum computing for finance: overview and prospects"), [21](https://arxiv.org/html/2601.04049v1#bib.bib29 "A survey on quantum computational finance for derivatives pricing and VaR")] and the references therein. For the particular task of options pricing via Monte Carlo-like methods, recent works (see [[39](https://arxiv.org/html/2601.04049v1#bib.bib32 "Option pricing using quantum computers"), [7](https://arxiv.org/html/2601.04049v1#bib.bib33 "Efficient state preparation for quantum amplitude estimation"), [31](https://arxiv.org/html/2601.04049v1#bib.bib26 "Alternative pipeline for option pricing using quantum computers"), [1](https://arxiv.org/html/2601.04049v1#bib.bib45 "Quantum machine learning methods for Fourier-based distribution estimation with application in option pricing")]) have demonstrated practical pipelines for quantum-based approaches, including state preparation and encoding strategies. Within this framework, quantum advantage arises from applying the QAE routine to integral-based formulations, such as those used in option pricing. However, the original QAE implementation remains impractical under current hardware constraints. To address this limitation, several hardware-efficient variants have emerged in recent years, [[22](https://arxiv.org/html/2601.04049v1#bib.bib28 "Iterative quantum amplitude estimation"), [17](https://arxiv.org/html/2601.04049v1#bib.bib27 "Modified iterative quantum amplitude estimation is asymptotically optimal"), [32](https://arxiv.org/html/2601.04049v1#bib.bib25 "Real quantum amplitude estimation"), [31](https://arxiv.org/html/2601.04049v1#bib.bib26 "Alternative pipeline for option pricing using quantum computers")] among others, enabling the deployment of QAE on near-term quantum devices. Still, most quantum computing demonstrations applied to financial derivatives problems use stylized distributions or toy payoffs. There is a lack of end-to-end pipelines that: (a) infer arbitrage-free risk-neutral marginals from real option quotes, (b) assemble joint distributions with empirically meaningful dependence, and (c) perform quantum-accelerated valuation.

Then, this paper addresses the previous points (so it tries to answer the question above) by presenting a full pipeline: (i) recovery of market-consistent marginal risk-neutral densities using the exponential NIG model, (ii) assembly of joint distributions via copulas (Gaussian copula for tractability), and (iii) deployment of a Quantum Accelerated Monte Carlo (QAMC) approach which acts on both the marginal density estimation (via orthogonal cosine expansions) and on the final multidimensional option valuation. The pipeline is modular (amenable to alternative marginals and copulas) and quantifies the accuracy–cost trade‑offs under both classical and quantum estimators. From the market distribution construction viewpoint, we provide relevant practical results (independence of prices from NIG location parameter, continuity and existence of regularized calibration solutions), arbitrage sanity checks, and empirical validation on liquid single-name equities (Credit Agricole, AXA, Michelin), which allows us to come up with calibrated distributions that match market skew and tails. In regard with the proposed quantum computing-based solution for multivariate pricing, we demonstrate, both theoretically and empirically, that QAMC achieves the expected quadratic convergence improvement compared with CMC when applied to crucial points in the whole pipeline, namely, the marginal distribution reconstruction and final multi-asset option valuation. In this sense, the choice of the NIG model is not arbitrary since, under its formulation, the density function driving the asset evolution present an analytical expression while the distribution and quantile functions (required for the CMC simulation) are not available in closed-form, resulting in computational expensive sampling procedures.

The paper is organized as follows. Section [2](https://arxiv.org/html/2601.04049v1#S2 "2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline") describes how to construct the asset distributions from the market information, including details of procedural issues (Sections [2.1](https://arxiv.org/html/2601.04049v1#S2.SS1 "2.1 Market European call and put options prices ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline") and [2.2](https://arxiv.org/html/2601.04049v1#S2.SS2 "2.2 Fitting and interpolation methods ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")), the exponential NIG model (Section [2.3](https://arxiv.org/html/2601.04049v1#S2.SS3 "2.3 The exponential NIG model ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) and calibration results ([2.4](https://arxiv.org/html/2601.04049v1#S2.SS4 "2.4 Calibration methodology and practical implementation ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")). In Section [3](https://arxiv.org/html/2601.04049v1#S3 "3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"), the different components of the quantum-based multidimensional option valuation are presented: the general pricing formula and the inclusion of copulas in it (Section [3.1](https://arxiv.org/html/2601.04049v1#S3.SS1 "3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")), the QAMC method applied to both marginals recovery and final option price calculation along with a rigorous theoretical analysis (Section [3.2](https://arxiv.org/html/2601.04049v1#S3.SS2 "3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) and the experimental outcomes (Section [3.3](https://arxiv.org/html/2601.04049v1#S3.SS3 "3.3 Experimental results ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")). Finally, Section [4](https://arxiv.org/html/2601.04049v1#S4 "4 Conclusions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline") concludes with a discussion of the main findings.

## 2 Construction of the market distributions

To construct a multidimensional market risk-neutral distribution using the copula framework, we begin by modelling the marginal distributions of each underlying asset. This step involves fitting a parametric distribution to European option prices observed in the market for each maturity. In this work, we adopt the NIG distribution introduced in Section [2.3](https://arxiv.org/html/2601.04049v1#S2.SS3 "2.3 The exponential NIG model ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").

### 2.1 Market European call and put options prices

The prices of European call and put options under the risk-neutral measure, expressed in terms of the risk-neutral density f​(ST)f(S\_{T}), are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(T,K)\displaystyle C(T,K) | =e−r​T​∫K∞f​(ST)​(ST−K)​dST,\displaystyle=e^{-rT}\int\_{K}^{\infty}f(S\_{T})(S\_{T}-K)\,\mathrm{d}S\_{T}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(T,K)\displaystyle P(T,K) | =e−r​T​∫0Kf​(ST)​(K−ST)​dST,\displaystyle=e^{-rT}\int\_{0}^{K}f(S\_{T})(K-S\_{T})\,\mathrm{d}S\_{T}, |  |

where TT option maturity, KK strike price, rr risk-free interest rate and f​(ST)f(S\_{T}) risk-neutral density of the underlying asset at maturity.

From Breeden and Litzenberger [[5](https://arxiv.org/html/2601.04049v1#bib.bib10 "Prices of state-contingent claims implicit in option prices")] and assuming enough regularity, differentiating once with respect to KK yields the cumulative distribution function,

|  |  |  |
| --- | --- | --- |
|  | ∂C​(T,K)∂K=−e−r​T​∫K∞f​(ST)​dST,\frac{\partial C(T,K)}{\partial K}=-e^{-rT}\int\_{K}^{\infty}f(S\_{T})\,\mathrm{d}S\_{T}, |  |

while differentiating twice produces the probability density function,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂2C​(T,K)∂K2=e−r​T​f​(K).\frac{\partial^{2}C(T,K)}{\partial K^{2}}=e^{-rT}f(K). |  | (1) |

Usually, market vanilla prices are first converted to implied volatilities using the Black-Scholes options pricing formula,

|  |  |  |  |
| --- | --- | --- | --- |
|  | CBS​(T,K)\displaystyle C^{\text{BS}}(T,K) | =S0​e−q​T​Φ​(d1)−K​e−r​T​Φ​(d2),\displaystyle=S\_{0}e^{-qT}\Phi(d\_{1})-Ke^{-rT}\Phi(d\_{2}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | PBS​(T,K)\displaystyle P^{\text{BS}}(T,K) | =K​e−r​T​Φ​(−d2)−S0​e−q​T​Φ​(−d1),\displaystyle=Ke^{-rT}\Phi(-d\_{2})-S\_{0}e^{-qT}\Phi(-d\_{1}), |  |

where

|  |  |  |
| --- | --- | --- |
|  | d1=log⁡(S0K)+(r−q+12​σ2)​Tσ​T,d2=d1−σ​T,d\_{1}=\frac{\log\left(\frac{S\_{0}}{K}\right)+\left(r-q+\frac{1}{2}\sigma^{2}\right)T}{\sigma\sqrt{T}},\quad d\_{2}=d\_{1}-\sigma\sqrt{T}, |  |

with S0S\_{0} the underlying asset spot price, qq the continuous dividend yield, σ\sigma the volatility of the underlying asset and Φ(.)\Phi(.) the cumulative distribution function of the standard normal distribution. The implied volatility σimp​(T,K)\sigma\_{\text{imp}}(T,K) associated to an expiry TT and strike KK is defined by matching market, V¯\bar{V}, and Black-scholes prices, i.e,

|  |  |  |
| --- | --- | --- |
|  | VBS​(T,K;σimp)=V¯​(T,K),V∈{C,P},V^{\text{BS}}(T,K;\sigma\_{\text{imp}})=\bar{V}(T,K),\quad V\in\{C,P\}, |  |

which is well-defined by the strictly increasing Black-Scholes price with respect to the volatility parameter. So there is a one to one mapping between vanilla prices and the implied volatilities. Practitioners represent vanilla options market data as implied volatility because it is easier to interpret and to monitor. For a given maturity, implied volatility as a function of strike is not constant and often smile shaped or skewed. It is usually called volatility smile.

To work with the risk-neutral density formula ([1](https://arxiv.org/html/2601.04049v1#S2.E1 "In 2.1 Market European call and put options prices ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) one needs the vanilla prices or implied volatilities at any
positive strike. Market data for traded options is only available at discrete strike points. As a consequence, we need an interpolation/extrapolation engine to produce a smooth function C¯​(T,K)/P¯​(T,K)\bar{C}(T,K)/\bar{P}(T,K) or σimp​(T,K)\sigma\_{\text{imp}}(T,K), given a discrete market data set, which is discussed in the next section.

### 2.2 Fitting and interpolation methods

The available fitting methods for implied volatility surfaces can be grouped into several categories, depending on how the market information is represented. These include:

* •

  Implied-volatility – describes directly the implied volatility as a function of strike and maturity. Different parametrizations are used across the industry, from simplistic (and arbitrageable) quadratic skew with cutoffs, to splines or to SVI parametrization [[19](https://arxiv.org/html/2601.04049v1#bib.bib3 "A parsimonious arbitrage-free implied volatility parameterization with application to the valuation of volatility derivatives"), [18](https://arxiv.org/html/2601.04049v1#bib.bib4 "Arbitrage-free SVI volatility surfaces")].
* •

  Time-slice distribution – defines the distribution of the stock price independently for every maturity. Typical examples include usage of a stochastic volatility model generated distribution, like the SABR model [[24](https://arxiv.org/html/2601.04049v1#bib.bib5 "Managing smile risk")], or directly a parametrization of the stock probability density function.
* •

  Non-homogeneous stochastic process – bootstraps time-dependent parameters of a stochastic process by fitting the implied volatilities at each maturity chronologically. A good example is the tied local volatility approach introduced in [[2](https://arxiv.org/html/2601.04049v1#bib.bib6 "Volatility interpolation")] and improved in [[29](https://arxiv.org/html/2601.04049v1#bib.bib7 "Filling the gaps")].
* •

  All-maturities non-parametric density – fits all the maturities together in a non-arbitrageable way. An interesting approach has been developed in [[12](https://arxiv.org/html/2601.04049v1#bib.bib8 "Building arbitrage-free implied volatility: sinkhorn’s algorithm and variants")].

All these methods have their advantages and disadvantages that have been discussed in e.g. [[12](https://arxiv.org/html/2601.04049v1#bib.bib8 "Building arbitrage-free implied volatility: sinkhorn’s algorithm and variants")]. In this work, we adopt the time-slice distribution method, using the NIG distribution to parametrize the risk-neutral probability density function of the underlying asset at each maturity as illustration. Others methods discussed above can also be used to build the market distributions.

### 2.3 The exponential NIG model

Let T>0T>0 be a fixed time horizon, and let S:t∈[0,T]↦S​(t)S:t\in[0,T]\mapsto S(t) denote the market price of a financial asset. We assume that, under the risk neutral probability ℚ\mathbb{Q}, the dynamics of S​(t)S(t) follow

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​S​(t)S​(t)=(r−q)​d​t+d​X​(t),t∈[0,T],\frac{\mathrm{d}S(t)}{S(t)}=(r-q)\,\mathrm{d}t+\mathrm{d}X(t),\quad t\in[0,T], |  | (2) |

where the initial value is given, i.e., S​(0)=S0S(0)=S\_{0}, r≥0r\geq 0 is the risk-free interest rate, q≥0q\geq 0 is the continuous dividend yield (both deterministic and continuously compounded) and {X​(t)}t∈[0,T]\{X(t)\}\_{t\in[0,T]} is a NIG Levy process with X​(0)=0X(0)=0, whose increments satisfy

|  |  |  |
| --- | --- | --- |
|  | X​(t+Δ​t)−X​(t)∼NIG​(α,β,δ​Δ​t,μ​Δ​t)for all ​Δ​t≥0,X(t+\Delta t)-X(t)\sim\text{NIG}(\alpha,\beta,\delta\Delta t,\mu\Delta t)\quad\text{for all }\Delta t\geq 0, |  |

with the NIG distribution with parameters (α,β,δ,μ)(\alpha,\beta,\delta,\mu), written as NIG​(α,β,δ,μ)\text{NIG}(\alpha,\beta,\delta,\mu), has the following density function,

|  |  |  |  |
| --- | --- | --- | --- |
|  | fNIG​(x;α,β,δ,μ)=α​δπ​eδ​α2−β2+β​(x−μ)​K1​(α​δ2+(x−μ)2)δ2+(x−μ)2,x∈ℝf\_{\mathrm{NIG}}(x;\alpha,\beta,\delta,\mu)=\frac{\alpha\delta}{\pi}e^{\delta\sqrt{\alpha^{2}-\beta^{2}}+\beta(x-\mu)}\frac{\mathrm{K}\_{1}\left(\alpha\sqrt{\delta^{2}+(x-\mu)^{2}}\right)}{\sqrt{\delta^{2}+(x-\mu)^{2}}},\hskip 14.22636ptx\in\mathbb{R} |  | (3) |

where:

* •

  K1​(z)\mathrm{K}\_{1}(z) is the modified Bessel function of the second kind with index 1,
* •

  α>0\alpha>0 is the tail (steepness) parameter which controls the kurtosis (larger α\alpha gives lighter tails),
* •

  β∈(−α,α)\beta\in(-\alpha,\alpha) is the skewness parameter (β<0\beta<0 implies left skewness, β>0\beta>0 right skewness, and β=0\beta=0 yields symmetry),
* •

  δ>0\delta>0 is the scale parameter,
* •

  μ∈ℝ\mu\in\mathbb{R} is the location parameter.

The NIG process characteristic function φ​(u;t):=𝔼​[ei​u​Xt]\varphi(u;t):=\mathbb{E}\left[e^{iuX\_{t}}\right] can be written down as
φ​(u;t)=et⋅ϑ​(u)\varphi(u;t)=e^{t\cdot\vartheta(u)},
where the characteristic exponent or Lévy symbol, is known in exact form

|  |  |  |
| --- | --- | --- |
|  | ϑ​(u):=log⁡φ​(u;1)=i​μ​u−δ​(α2−(β+i​u)2−α2−β2).\vartheta(u):=\log\varphi(u;1)=i\mu u-\delta\left(\sqrt{\alpha^{2}-(\beta+iu)^{2}}-\sqrt{\alpha^{2}-\beta^{2}}\right). |  |

The solution to the stochastic differential equation ([2](https://arxiv.org/html/2601.04049v1#S2.E2 "In 2.3 The exponential NIG model ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) is given by the exponential NIG process

|  |  |  |
| --- | --- | --- |
|  | S​(T)=S​(t)​exp⁡((r−q+ω)​τ+X​(τ)),τ:=T−t,S(T)=S(t)\exp\left((r-q+\omega)\tau+X(\tau)\right),\quad\tau:=T-t, |  |

where ω\omega is the martingale or compensator adjustment. It ensures that the discounted asset price is a true ℚ\mathbb{Q}-martingale, by enforcing

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℚ​[S​(T)∣ℱt]=e(r−q)​τ​S​(t).\mathbb{E}^{\mathbb{Q}}[S(T)\mid\mathcal{F}\_{t}]=e^{(r-q)\tau}S(t). |  |

which leads to the condition

|  |  |  |
| --- | --- | --- |
|  | ω=−μ+δ​(α2−(β+1)2−α2−β2).\omega=-\mu+\delta\left(\sqrt{\alpha^{2}-(\beta+1)^{2}}-\sqrt{\alpha^{2}-\beta^{2}}\right). |  |

The NIG distribution enjoys the following desirable properties in our context:

* •

  It admits an explicit density function, which is smooth and differentiable, ensuring numerical stability.
* •

  It is arbitrage-free across time slices when calibrated individually per maturity.
* •

  The characteristic function is known in closed form, enabling efficient pricing via Fourier inversion techniques.
* •

  Its flexible tail behaviour and skewness allow it to fit market-implied distributions accurately (see e.g [[13](https://arxiv.org/html/2601.04049v1#bib.bib9 "The normal inverse gaussian distribution and the pricing of derivatives"), [40](https://arxiv.org/html/2601.04049v1#bib.bib11 "Implied distribution as a function of the volatility smile"), [30](https://arxiv.org/html/2601.04049v1#bib.bib12 "Option pricing under nig distribution: the empirical analysis of nikkei 225 option")]).

By obtained a set of calibrated NIG parameters (α¯,β¯,δ¯,μ¯)(\bar{\alpha},\bar{\beta},\bar{\delta},\bar{\mu}) for each maturity TT to the observed market option prices or implied volatilities, we can recover a smooth, arbitrage-free risk-neutral density f¯NIG​(x)\bar{f}\_{\mathrm{NIG}}(x). This calibrated NIG density serves as the marginal distribution for the asset price at maturity TT, and will be later coupled across assets using a copula function as described in Section [3.1.1](https://arxiv.org/html/2601.04049v1#S3.SS1.SSS1 "3.1.1 Joint distribution via copulas ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").

#### 2.3.1 NIG model calibration

In the following, some useful results on the calibration of the NIG model are provided.

###### Proposition 2.1 (Independence of the NIG price on the location parameter).

Given the NIG pricing model in Section [2.3](https://arxiv.org/html/2601.04049v1#S2.SS3 "2.3 The exponential NIG model ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline") and let h:ℝ+→ℝh:\mathbb{R}\_{+}\to\mathbb{R} be a measurable payoff function (e.g., a European call or put payoff) such that the European option price,

|  |  |  |
| --- | --- | --- |
|  | VNIG​(T,K;θ)=e−r​T​𝔼ℚ​[h​(S​(T),K)],V^{\mathrm{NIG}}(T,K;\theta)=e^{-rT}\mathbb{E}^{\mathbb{Q}}[h(S(T),K)], |  |

is well-defined and finite. Then VNIG​(T,K;θ)V^{\mathrm{NIG}}(T,K;\theta) is independent of the location parameter μ\mu.

###### Proof.

The log-price at time TT can be expressed as

|  |  |  |
| --- | --- | --- |
|  | log⁡S​(T)=log⁡S0+(r−q+ω)​T+X​(T),\log S(T)=\log S\_{0}+(r-q+\omega)T+X(T), |  |

where X​(T)∼NIG​(α,β,δ​T,μ​T)X(T)\sim\mathrm{NIG}(\alpha,\beta,\delta T,\mu T).

The density of X​(T)X(T) depends on μ​T\mu T as a location shift.
The martingale correction ω\omega is explicitly given by

|  |  |  |
| --- | --- | --- |
|  | ω=−μ+δ​(α2−(β+1)2−α2−β2),\omega=-\mu+\delta\left(\sqrt{\alpha^{2}-(\beta+1)^{2}}-\sqrt{\alpha^{2}-\beta^{2}}\right), |  |

which depends linearly on −μ-\mu.

Substituting, the random variable log⁡S​(T)\log S(T) can be rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡S​(T)\displaystyle\log S(T) | =log⁡S0+(r−q)​T+ω​T+X​(T)\displaystyle=\log S\_{0}+(r-q)T+\omega T+X(T) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =log⁡S0+(r−q)​T+T​(−μ+δ​(α2−(β+1)2−α2−β2))+X​(T)\displaystyle=\log S\_{0}+(r-q)T+T\left(-\mu+\delta\left(\sqrt{\alpha^{2}-(\beta+1)^{2}}-\sqrt{\alpha^{2}-\beta^{2}}\right)\right)+X(T) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =log⁡S0+(r−q)​T+δ​T​(α2−(β+1)2−α2−β2)+(X​(T)−μ​T).\displaystyle=\log S\_{0}+(r-q)T+\delta T\left(\sqrt{\alpha^{2}-(\beta+1)^{2}}-\sqrt{\alpha^{2}-\beta^{2}}\right)+(X(T)-\mu T). |  |

Since X​(T)−μ​T∼NIG​(α,β,δ​T,0)X(T)-\mu T\sim\mathrm{NIG}(\alpha,\beta,\delta T,0), the distribution of log⁡S​(T)\log S(T) under ℚ\mathbb{Q} depends only on α,β,δ\alpha,\beta,\delta and not on μ\mu. Hence, the distribution of S​(T)S(T) and therefore the expectation 𝔼ℚ​[h​(S​(T),K)]\mathbb{E}^{\mathbb{Q}}[h(S(T),K)] are independent of μ\mu.

∎

This result justifies fixing μ=0\mu=0 during calibration without loss of generality. To prepare for the proof of Proposition [2.3](https://arxiv.org/html/2601.04049v1#S2.Thmtheorem3 "Proposition 2.3 (Existence of Solution to the Regularized Calibration Problem). ‣ 2.3.1 NIG model calibration ‣ 2.3 The exponential NIG model ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"), we first establish that the model option prices are continuous with respect to the NIG parameters.

###### Lemma 2.2 (Continuity of NIG Option Prices).

Let VmNIG​(T,K;θ)V\_{m}^{\mathrm{NIG}}(T,K;\theta) denote the price of the mm-th call/put European option under the NIG model with parameter θ=(α,β,δ)∈Θ\theta=(\alpha,\beta,\delta)\in\Theta, with Θ\Theta a non empty compact set defined in Proposition [2.3](https://arxiv.org/html/2601.04049v1#S2.Thmtheorem3 "Proposition 2.3 (Existence of Solution to the Regularized Calibration Problem). ‣ 2.3.1 NIG model calibration ‣ 2.3 The exponential NIG model ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")
Then, for each mm, the mapping

|  |  |  |
| --- | --- | --- |
|  | θ↦VmNIG​(T,K;θ)\theta\mapsto V\_{m}^{\mathrm{NIG}}(T,K;\theta) |  |

is continuous on Θ\Theta.

###### Proof.

Let θ=(α,β,δ)∈Θ\theta=(\alpha,\beta,\delta)\in\Theta, and consider the price of the mm-th European option under the NIG model,

|  |  |  |
| --- | --- | --- |
|  | VmNIG​(T,K;θ)=e−r​T​∫ℝh​(S0​eω​(θ)​T+x,K)​fNIG​(x;θ)​dx,V\_{m}^{\mathrm{NIG}}(T,K;\theta)=e^{-rT}\int\_{\mathbb{R}}h\left(S\_{0}e^{\omega(\theta)T+x},K\right)f\_{\mathrm{NIG}}(x;\theta)\,\mathrm{d}x, |  |

where fNIG​(x;θ)f\_{\mathrm{NIG}}(x;\theta) is the NIG density with parameters (α,β,δ​T,0)(\alpha,\beta,\delta T,0), and ω​(θ)\omega(\theta) is the martingale correction term.
The map θ↦ω​(θ)\theta\mapsto\omega(\theta) is continuous, and fNIG​(x;θ)f\_{\mathrm{NIG}}(x;\theta) is jointly continuous in (x,θ)(x,\theta) on ℝ×Θ\mathbb{R}\times\Theta. Hence, the integrand is pointwise continuous in θ\theta for each fixed x∈ℝx\in\mathbb{R}.
To apply the Dominated Convergence Theorem, we note that the admissibility conditions α2>β2\alpha^{2}>\beta^{2} and α2>(β+1)2\alpha^{2}>(\beta+1)^{2} ensure that the NIG density decays exponentially in |x||x|, uniformly over θ∈Θ\theta\in\Theta. For European call options, the payoff behaves like h​(S,K)∼S∼exh(S,K)\sim S\sim e^{x}, so the integrand satisfies

|  |  |  |
| --- | --- | --- |
|  | h​(S0​eω​T+x)⋅fNIG​(x;θ)∼e(1+β)​x−α​|x|,h(S\_{0}e^{\omega T+x})\cdot f\_{\mathrm{NIG}}(x;\theta)\sim e^{(1+\beta)x-\alpha|x|}, |  |

which is integrable when α>β+1\alpha>\beta+1. For put options, the payoff is bounded, and integrability follows directly from the exponential decay of fNIGf\_{\mathrm{NIG}}.
Therefore, the integrands are uniformly dominated by an integrable function independent of θ\theta, and the Dominated Convergence Theorem yields

|  |  |  |
| --- | --- | --- |
|  | lims→∞VmNIG​(T,K;θs)=VmNIG​(T,K;θ),\lim\_{s\to\infty}V\_{m}^{\mathrm{NIG}}(T,K;\theta\_{s})=V\_{m}^{\mathrm{NIG}}(T,K;\theta), |  |

for any sequence θs→θ\theta\_{s}\to\theta in Θ\Theta. This proves continuity of θ↦VmNIG​(T,K;θ)\theta\mapsto V\_{m}^{\mathrm{NIG}}(T,K;\theta).
∎

###### Proposition 2.3 (Existence of Solution to the Regularized Calibration Problem).

Let Θ⊂ℝ3\Theta\subset\mathbb{R}^{3} be a non-empty, compact subset of admissible parameters θ:=(α,β,δ)\theta:=(\alpha,\beta,\delta) for the NIG model with fixed μ:=0\mu:=0, satisfying the constraints

|  |  |  |
| --- | --- | --- |
|  | α>0,δ>0,β2<α2,(β+1)2<α2.\alpha>0,\quad\delta>0,\quad\beta^{2}<\alpha^{2},\quad(\beta+1)^{2}<\alpha^{2}. |  |

Define the Tikhonov-regularized least-squares objective function,

|  |  |  |
| --- | --- | --- |
|  | 𝒥​(θ):=∑m=1Mwm​(VmNIG​(T,K;θ)−V¯m​(T,K))2+λ​‖θ−θ0‖2,\mathcal{J}(\theta):=\sum\_{m=1}^{M}w\_{m}\left(V\_{m}^{\mathrm{NIG}}(T,K;\theta)-\bar{V}\_{m}(T,K)\right)^{2}+\lambda\|\theta-\theta\_{0}\|^{2}, |  |

where {V¯m​(T,K)}m=1M\{\bar{V}\_{m}(T,K)\}\_{m=1}^{M} are observed market European call/put option prices, VmNIG​(T,K;θ)V\_{m}^{\mathrm{NIG}}(T,K;\theta) are model European call/put option prices under the NIG model with parameter θ\theta, wm≥0w\_{m}\geq 0 are fixed weights, θ0∈Θ\theta\_{0}\in\Theta is a fixed prior (reference) parameter vector, λ≥0\lambda\geq 0 is the regularization parameter and ∥⋅∥\|\cdot\| is the Euclidean norm on ℝ3\mathbb{R}^{3}.

Then the minimization problem

|  |  |  |
| --- | --- | --- |
|  | minθ∈Θ⁡𝒥​(θ)\min\_{\theta\in\Theta}\mathcal{J}(\theta) |  |

admits at least one solution.

###### Proof.

The parameter set Θ\Theta is compact, and all quantities in the objective function are finite by assumption. By Lemma [2.2](https://arxiv.org/html/2601.04049v1#S2.Thmtheorem2 "Lemma 2.2 (Continuity of NIG Option Prices). ‣ 2.3.1 NIG model calibration ‣ 2.3 The exponential NIG model ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"), the map θ↦Vm​(T,K;θ)\theta\mapsto V\_{m}(T,K;\theta) is continuous for each mm. Therefore, 𝒥​(θ)\mathcal{J}(\theta) is a continuous real-valued function on a compact domain. By the Weierstrass Extreme Value Theorem, 𝒥\mathcal{J} attains a global minimum on Θ\Theta.
∎

###### Remark (Non-uniqueness).

The existence of a solution to the regularized calibration problem does not imply uniqueness. The objective function 𝒥​(θ)\mathcal{J}(\theta) is generally non-convex due to the nonlinear dependence of option prices on the NIG parameters. Multiple local minima may exist, and standard optimization algorithms may converge to different solutions depending on the initial guess.

###### Remark (Stability and sensitivity).

While Proposition [2.3](https://arxiv.org/html/2601.04049v1#S2.Thmtheorem3 "Proposition 2.3 (Existence of Solution to the Regularized Calibration Problem). ‣ 2.3.1 NIG model calibration ‣ 2.3 The exponential NIG model ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline") guarantees the existence of a minimizer, the stability of the solution with respect to perturbations in the market data {V¯m}\{\bar{V}\_{m}\} is not addressed. In ill-posed inverse problems such as model calibration, small changes in the input can result in large variations in the estimated parameters. The Tikhonov regularization term λ​‖θ−θ0‖2\lambda\|\theta-\theta\_{0}\|^{2} is introduced precisely to mitigate such instability by enforcing proximity to a reference parameter θ0\theta\_{0}. The choice of λ>0\lambda>0 thus balances calibration accuracy and stability (see e.g Chapter 3, Section 13 in [[10](https://arxiv.org/html/2601.04049v1#bib.bib14 "Financial modelling with jump processes")], [[9](https://arxiv.org/html/2601.04049v1#bib.bib15 "Option pricing models with jumps: integro‐differential equations and inverse problems")] or [[11](https://arxiv.org/html/2601.04049v1#bib.bib13 "Calibration of the local volatility in a generalized black–scholes model using tikhonov regularization")] for more details).

### 2.4 Calibration methodology and practical implementation

#### 2.4.1 Market data

The market data used in our numerical experiments consists of European call and put option quotes on Credit Agricole, AXA, and Michelin (three major French companies) sourced from Euronext as of 24/12/2024. The dataset spans multiple maturities and, for each expiry, includes strike levels and bid-ask quotes for European call and put options. In addition, the data provides stock futures curves. Spot prices are taken from market closing levels retrieved via Yahoo Finance.

#### 2.4.2 Market-implied discount, forward, and dividend curves

In our methodology, we construct market-implied discount factors, forward prices, and dividend yields to ensure consistency with observed European vanilla option prices. This step is essential to transition from market quotes to risk-neutral distributions used in option pricing and density recovery.

We leverage the classical *put-call parity* relation for European vanilla options. For a given strike KK and maturity TT, the parity reads

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(T,K)−P​(T,K)=F​W​(T)⋅D​F​(T)−K⋅D​F​(T),C(T,K)-P(T,K)=FW(T)\cdot DF(T)-K\cdot DF(T), |  | (4) |

where C​(T,K)C(T,K) and P​(T,K)P(T,K) denote the market prices of the European call and put options, respectively, F​W​(T)FW(T) is the forward price of the underlying asset at maturity TT and D​F​(T)DF(T) is the risk-free discount factor at maturity TT.

From the bid and ask quotes, we compute mid-prices for European call and put options. We then apply equation ([4](https://arxiv.org/html/2601.04049v1#S2.E4 "In 2.4.2 Market-implied discount, forward, and dividend curves ‣ 2.4 Calibration methodology and practical implementation ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) to perform a linear regression in the strike KK. The slope and intercept of this regression allow us to estimate the discount factor D​F​(T)DF(T) and the forward price F​W​(T)FW(T) for each expiry.

Using the inferred forward price, we deduce the continuous dividend yield qq using the standard spot-forward relationship

|  |  |  |
| --- | --- | --- |
|  | F​W​(T)=S0​e(r−q)​T,FW(T)=S\_{0}e^{(r-q)T}, |  |

where S0S\_{0} is the spot price and rr is the risk-free interest rate.

This procedure ensures internal consistency across the inferred market curves and aligns all inputs (spot prices, forwards, and discounting factors) with actual observed option market data. By doing so, we avoid relying on external estimates of interest rates or dividend yields, which could introduce inconsistencies or arbitrage opportunities.

#### 2.4.3 Arbitrage sanity check

Our pricing model is grounded in arbitrage-free principles. Accordingly, it is crucial that the input data exhibit internal consistency. For each option expiry, we verify the absence of digital and butterfly arbitrage, removing any violations prior to model calibration.

For a strictly increasing sequence of strikes K1<K2<K3K\_{1}<K\_{2}<K\_{3}, we approximate digital call and put prices using one-sided finite differences of vanilla option prices. The absence of arbitrage requires that the following inequalities hold,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | <C​(T,K1)−C​(T,K2)K2−K1<1,\displaystyle<\frac{C(T,K\_{1})-C(T,K\_{2})}{K\_{2}-K\_{1}}<1, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 0\displaystyle 0 | <P​(T,K2)−P​(T,K1)K2−K1<1.\displaystyle<\frac{P(T,K\_{2})-P(T,K\_{1})}{K\_{2}-K\_{1}}<1. |  |

These expressions correspond to the implied prices of digital calls and puts, which must lie strictly between 0 and 1 under the no-arbitrage assumption.

Butterfly arbitrage arises when the option price surface fails to exhibit convexity in strike. For European call options, the following convexity condition must be satisfied,

|  |  |  |
| --- | --- | --- |
|  | C​(T,K1)−C​(T,K2)−K2−K1K3−K2​(C​(T,K2)−C​(T,K3))≥0.C(T,K\_{1})-C(T,K\_{2})-\frac{K\_{2}-K\_{1}}{K\_{3}-K\_{2}}\left(C(T,K\_{2})-C(T,K\_{3})\right)\geq 0. |  |

An analogous condition applies to European put options, i.e.,

|  |  |  |
| --- | --- | --- |
|  | P​(T,K1)−P​(T,K2)−K2−K1K3−K2​(P​(T,K2)−P​(T,K3))≥0.P(T,K\_{1})-P(T,K\_{2})-\frac{K\_{2}-K\_{1}}{K\_{3}-K\_{2}}\left(P(T,K\_{2})-P(T,K\_{3})\right)\geq 0. |  |

Violations of these conditions imply inconsistency in the implied risk-neutral probability distribution. In our dataset, we detect a small number of violations, specifically, digital put arbitrage in the far tails. These inconsistencies have been removed prior to the fitting procedure.

#### 2.4.4 Calibration methodology

We calibrate the NIG distribution to market option prices for each asset and maturity by solving a regularized, constrained nonlinear least squares problem as presented in Proposition [2.3](https://arxiv.org/html/2601.04049v1#S2.Thmtheorem3 "Proposition 2.3 (Existence of Solution to the Regularized Calibration Problem). ‣ 2.3.1 NIG model calibration ‣ 2.3 The exponential NIG model ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"). Recall that, this procedure is designed to recover smooth and arbitrage-free marginal risk-neutral densities, suitable for copula-based joint distribution construction.

Next, we adapt the result from Proposition [2.3](https://arxiv.org/html/2601.04049v1#S2.Thmtheorem3 "Proposition 2.3 (Existence of Solution to the Regularized Calibration Problem). ‣ 2.3.1 NIG model calibration ‣ 2.3 The exponential NIG model ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline") accounting for the methodological considerations described above. Let θ=(α,β,δ)\theta=(\alpha,\beta,\delta) denote the NIG parameters to be calibrated, with location μ\mu fixed to zero (justified analytically in Proposition [2.1](https://arxiv.org/html/2601.04049v1#S2.Thmtheorem1 "Proposition 2.1 (Independence of the NIG price on the location parameter). ‣ 2.3.1 NIG model calibration ‣ 2.3 The exponential NIG model ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")). Then, the calibration minimizes the following objective function,

|  |  |  |
| --- | --- | --- |
|  | 𝒥​(θ)=∑m=1Mwm​(VmNIG​(T,K;θ)−V¯m​(T,K))2+λ​‖θ−θ0‖2,\mathcal{J}(\theta)=\sum\_{m=1}^{M}w\_{m}\left(V\_{m}^{\text{NIG}}(T,K;\theta)-\bar{V}\_{m}(T,K)\right)^{2}+\lambda\|\theta-\theta\_{0}\|^{2}, |  |

where:

* •

  V¯m​(T,K)\bar{V}\_{m}(T,K) are the mid-market prices of liquid European call/put options with various strikes and maturities,
* •

  VmNIG​(T,K;θ)V\_{m}^{\text{NIG}}(T,K;\theta) are again model prices computed using the exponential NIG model,
* •

  wmw\_{m} are weights inversely proportional to the bid-ask spreads (to reflect pricing uncertainty),
* •

  θ0\theta\_{0} is a prior guess for the parameters and chosen to be given by the Black-Scholes model using the ATM implied volatility, and
* •

  λ≥0\lambda\geq 0 is a regularization coefficient that controls proximity to the prior.

This objective balances accuracy to market data with stability, following Tikhonov-style regularization as discussed in Cont and Tankov [[10](https://arxiv.org/html/2601.04049v1#bib.bib14 "Financial modelling with jump processes")].
Since the objective function is non-convex, careful initialization is essential. We perform a grid search over plausible starting points for (α,β,δ)(\alpha,\beta,\delta), selecting the one with the lowest pre-optimization objective value. This heuristic helps mitigate convergence to poor local minima.
As optimizer, we use the trust-constr algorithm from scipy.optimize.minimize, which supports constraints, bounds, and robust convergence settings. Optimization tolerances are tightened to ensure precise convergence. This yields a calibrated set of parameters (α¯,β¯,δ¯)(\bar{\alpha},\bar{\beta},\bar{\delta}) for each asset and maturity.

#### 2.4.5 Calibration outcomes

The calibrated NIG densities exhibit strong agreement with observed market option prices, capturing key features such as skew and smile. The resulting risk-neutral densities are arbitrage-free at each time slice. For Credit Agricole, the largest pricing error (normalized by the spot) is approximately 21 basis points, occurring in the tails. Around the ATM strike, errors are typically around 10 basis points (see Figure [1](https://arxiv.org/html/2601.04049v1#S2.F1 "Figure 1 ‣ 2.4.5 Calibration outcomes ‣ 2.4 Calibration methodology and practical implementation ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")). For AXA, the maximum discrepancy is about 10 basis points (see Figure [2](https://arxiv.org/html/2601.04049v1#S2.F2 "Figure 2 ‣ 2.4.5 Calibration outcomes ‣ 2.4 Calibration methodology and practical implementation ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")), while for Michelin, it is approximately 6 basis points (see Figure [3](https://arxiv.org/html/2601.04049v1#S2.F3 "Figure 3 ‣ 2.4.5 Calibration outcomes ‣ 2.4 Calibration methodology and practical implementation ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")), indicating high calibration accuracy across all three assets. Each figure compares the calibrated NIG density with the prior lognormal distribution based on ATM implied volatility. As expected for equity markets, all distributions display fat tails and left skew, which the NIG model captures well. The inclusion of a Tikhonov regularization term stabilizes parameter estimates and prevents overfitting in regions with sparse or noisy quotes. Overall, the results confirm the NIG model’s ability to reflect empirical skewness and kurtosis, supporting its use in downstream tasks such as quantum-based pricing and copula-like multivariate modelling.

![Refer to caption](x1.png)


Figure 1: Credit Agricole, 1-year expiry (19/12/2025), data as of 24/12/2024 with closing spot price at 12.91 EUR. Calibrated parameters: α¯=4.69,β¯=−3.06,δ¯=0.18\bar{\alpha}=4.69,\bar{\beta}=-3.06,\bar{\delta}=0.18 with λ=5×10−7\lambda=5\times 10^{-7}. Left: market vs calibrated implied volatilities. Right: prior log-normal density function using ATM implied volatility vs calibrated density function.

![Refer to caption](x2.png)


Figure 2: AXA, 1-year expiry (19/12/2025), data as of 24/12/2024 with closing spot price at 33.8 EUR. Calibrated parameters: α¯=5.24,β¯=−3.26,δ¯=0.18\bar{\alpha}=5.24,\bar{\beta}=-3.26,\bar{\delta}=0.18 with λ=5×10−7\lambda=5\times 10^{-7}. Left: market vs calibrated implied volatilities. Right: prior log-normal density function using ATM implied volatility vs calibrated density function.

![Refer to caption](x3.png)


Figure 3: Michelin, 1-year expiry (19/12/2025), data as of 24/12/2024 with closing spot price at 31.76 EUR. Calibrated parameters: α¯=6.2,β¯=−3.31,δ¯=0.26\bar{\alpha}=6.2,\bar{\beta}=-3.31,\bar{\delta}=0.26 with λ=5×10−7\lambda=5\times 10^{-7}. Left: market vs calibrated implied volatilities. Right: prior log-normal density function using ATM implied volatility vs calibrated density function.

## 3 Multidimensional option pricing using quantum computing

We explore the power of quantum computing when addressing the problem of multidimensional option pricing.

### 3.1 Multidimensional option pricing using copulas

We are interested in multivariate option pricing of European-like options, where the payoff function can be written in general form as

|  |  |  |
| --- | --- | --- |
|  | h(𝐒,K),𝐒=(Si(T),i=1,2,…,N),h\left(\mathbf{S},K\right),\quad\mathbf{S}=\left(S\_{i}(T),\,i=1,2,\ldots,N\right), |  |

where, as usual, h​(⋅)h(\cdot) is a univariate payoff function that identifies the derivative contract, SiS\_{i} denotes the price of the ithi^{\text{th}} underlying security, TT is the contract maturity and KK represents the contract strike. Below lists some common examples:

1. 1.

   Arithmetic basket call option,

   |  |  |  |
   | --- | --- | --- |
   |  | h​(Si​(T),K)=max⁡(1N​∑i=1NSi​(T)−K, 0),h\left(S\_{i}(T),K\right)=\max\left(\frac{1}{N}\sum\_{i=1}^{N}S\_{i}(T)-K,\,0\right), |  |
2. 2.

   Worst-of put option,

   |  |  |  |
   | --- | --- | --- |
   |  | h​(Si​(T),K)=max⁡(K−mini=1,…,N⁡Si​(T), 0),h\left(S\_{i}(T),K\right)=\max\left(K-\min\_{i=1,\ldots,N}S\_{i}(T),\,0\right), |  |
3. 3.

   Spread call option,

   |  |  |  |
   | --- | --- | --- |
   |  | h​(S1​(T),S2​(T),K)=max⁡(S1​(T)−S2​(T)−K, 0).h\left(S\_{1}(T),S\_{2}(T),K\right)=\max\left(S\_{1}(T)-S\_{2}(T)-K,\,0\right). |  |

In general, given a multivariate payoff, the option value can be then formulated in terms of an expectation as

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(T,K)=e−r​T​𝔼​[h​(𝐒,K)]=e−r​T​∫Ωf​(𝐒)​h​(𝐒,K)​dN​𝐒,V(T,K)=e^{-rT}\mathbb{E}[h(\mathbf{S},K)]=e^{-rT}\int\_{\Omega}f(\mathbf{S})h(\mathbf{S},K)\,\mathrm{d}^{N}\mathbf{S}, |  | (5) |

here written as well in integral form for convenience. In order to address the resolution of that integral via numerical techniques, the availability of the joint density function of the underlying assets is desired. In the following, a copula-based approach for deriving such joint density is described.

#### 3.1.1 Joint distribution via copulas

In the context of multivariate option pricing, especially when dealing with multiple underlying assets, it is essential to model the joint distribution of asset prices at maturity. While the marginal distributions of each asset can be independently inferred from market option prices (see Section [2.3.1](https://arxiv.org/html/2601.04049v1#S2.SS3.SSS1 "2.3.1 NIG model calibration ‣ 2.3 The exponential NIG model ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")), their joint behaviour must account for inter-asset dependencies.

Copulas provide a powerful and flexible tool to model this dependence structure separately from the marginals. A copula is a multivariate distribution function defined on the unit cube [0,1]N[0,1]^{N} with uniform marginals, which allows the construction of joint distributions from given marginals. More precisely, by using a copula, we can handle the individual univariate marginal distributions
and their dependency separately, thanks to Sklar’s theorem, which guarantees the consistency between the copula-based
joint distribution and each marginal distribution.

###### Theorem 3.1 (Sklar’s Theorem [[35](https://arxiv.org/html/2601.04049v1#bib.bib16 "An introduction to copulas")]).

For any joint distribution function FF on ℝN\mathbb{R}^{N} of a random vector 𝐗=(X1,…,XN)\mathbf{X}=(X\_{1},\dots,X\_{N}) with marginal distribution functions F1,…,FNF\_{1},\dots,F\_{N}, there exists a copula CC such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(x1,…,xN)=𝒞​(F1​(x1),…,Fd​(xN)),F(x\_{1},\dots,x\_{N})=\mathcal{C}(F\_{1}(x\_{1}),\dots,F\_{d}(x\_{N})), |  | (6) |

for any (x1,…,xN)∈ℝN(x\_{1},\dots,x\_{N})\in\mathbb{R}^{N}. If F1,…,FNF\_{1},\dots,F\_{N} are continuous, then the copula 𝒞\mathcal{C} is unique. Conversely, for any marginal distributions F1,…,FNF\_{1},\dots,F\_{N} and a NN-variate copula 𝒞\mathcal{C}, the function FF defined as in ([6](https://arxiv.org/html/2601.04049v1#S3.E6 "In Theorem 3.1 (Sklar’s Theorem [35]). ‣ 3.1.1 Joint distribution via copulas ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) is a valid joint distribution function with marginals F1,…,FNF\_{1},\dots,F\_{N}.

From formula ([6](https://arxiv.org/html/2601.04049v1#S3.E6 "In Theorem 3.1 (Sklar’s Theorem [35]). ‣ 3.1.1 Joint distribution via copulas ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")), if the marginals F1,…,FNF\_{1},\dots,F\_{N} are differentiable with densities f1,…,fNf\_{1},\dots,f\_{N}, the copula 𝒞\mathcal{C} is differentiable with density cc given by

|  |  |  |
| --- | --- | --- |
|  | c​(u1,…,uN)=∂N∂u1​⋯​∂uN​𝒞​(u1,…,uN),c(u\_{1},\dots,u\_{N})=\frac{\partial^{N}}{\partial u\_{1}\cdots\partial u\_{N}}\mathcal{C}(u\_{1},\dots,u\_{N}), |  |

then, with a direct derivation, the joint density ff of the vector (X1,…,XN)(X\_{1},\dots,X\_{N}) can be written as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(x1,…,xN)=c​(F1​(x1),…,FN​(xN))⋅∏i=1Nfi​(xi).f(x\_{1},\dots,x\_{N})=c\left(F\_{1}(x\_{1}),\dots,F\_{N}(x\_{N})\right)\cdot\prod\_{i=1}^{N}f\_{i}(x\_{i}). |  | (7) |

This formula expresses the joint density as the product of two components:

* •

  The copula density evaluated at the marginal distribution functions, which captures the interdependence between variables;
* •

  The product of the marginal densities, which captures the individual behaviour of each variable.

A popular choice of copula (and the one that will be considered in this work) is the Gaussian copula, due to its tractability. Let ΦN​(⋅;Σ)\Phi\_{N}(\cdot;\Sigma) be the NN-dimensional standard normal cumulative distribution function with correlation matrix Σ∈ℝN×N\Sigma\in\mathbb{R}^{N\times N}, and let Φ−1\Phi^{-1} denote the univariate standard normal quantile function. The Gaussian copula is defined as

|  |  |  |
| --- | --- | --- |
|  | 𝒞Σ​(u1,…,uN)=ΦN​(Φ−1​(u1),…,Φ−1​(uN);Σ).\mathcal{C}\_{\Sigma}(u\_{1},\dots,u\_{N})=\Phi\_{N}\left(\Phi^{-1}(u\_{1}),\dots,\Phi^{-1}(u\_{N});\Sigma\right). |  |

The corresponding copula density is

|  |  |  |
| --- | --- | --- |
|  | cΣ​(u1,…,uN)=1detΣ​exp⁡(−12​𝐳⊤​(Σ−1−ℐ)​𝐳),c\_{\Sigma}(u\_{1},\dots,u\_{N})=\frac{1}{\sqrt{\det\Sigma}}\exp\left(-\frac{1}{2}\mathbf{z}^{\top}(\Sigma^{-1}-\mathcal{I})\mathbf{z}\right), |  |

where 𝐳=(Φ−1​(u1),…,Φ−1​(uN))\mathbf{z}=(\Phi^{-1}(u\_{1}),\dots,\Phi^{-1}(u\_{N})) and ℐ\mathcal{I} is the identity matrix.

#### Multidimensional option valuation with copulas

Employing ([7](https://arxiv.org/html/2601.04049v1#S3.E7 "In 3.1.1 Joint distribution via copulas ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")), we can rewrite the pricing formulation in ([5](https://arxiv.org/html/2601.04049v1#S3.E5 "In 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | V​(T,K)\displaystyle V(T,K) | =e−r​T​𝔼​[h​(𝐒,K)]\displaystyle=e^{-rT}\mathbb{E}[h(\mathbf{S},K)] |  | (8) |
|  |  | =e−r​T​∫Ωh​(𝐒,K)​c​(F1​(S1),…,FN​(SN))⋅∏i=1Nfi​(Si)​dN​𝐒\displaystyle=e^{-rT}\int\_{\Omega}h(\mathbf{S},K)c\left(F\_{1}(S\_{1}),\dots,F\_{N}(S\_{N})\right)\cdot\prod\_{i=1}^{N}f\_{i}(S\_{i})\mathrm{d}^{N}\mathbf{S} |  |
|  |  | =e−r​T​𝔼ind​[h​(𝐒,K)​c​(F1​(S1),…,FN​(SN))],\displaystyle=e^{-rT}\mathbb{E}^{\mathrm{ind}}[h(\mathbf{S},K)c\left(F\_{1}(S\_{1}),\dots,F\_{N}(S\_{N})\right)], |  |

where, again, 𝐒\mathbf{S} is the vector of random variables representing the asset prices at expiry TT, h​(x)h(x) is the final payoff function and 𝔼i​n​d​[⋅]\mathbb{E}^{ind}[\cdot] is the expectation operator applied to 𝐒\mathbf{S} by considering its components SiS\_{i} as independent. By using ([8](https://arxiv.org/html/2601.04049v1#S3.E8 "In Multidimensional option valuation with copulas ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")), the pricing of a payoff under a *correlated* joint distribution can be rewritten as an expectation under *independent* marginals, at the cost of weighting the payoff by the copula density c​(F1​(⋅),…,FN​(⋅))c(F\_{1}(\cdot),\dots,F\_{N}(\cdot)). In other words, correlation is entirely captured by this multiplicative weight.

Note then that, in order to build (and work with) the copula approach described above, both the marginal density and distribution functions are required. In the derivatives pricing framework, it is often the case that no analytical closed-form for such expressions are available, or their tractability is not efficient in numerical and/or computational terms. As example, for the NIG model presented in Section [2.3](https://arxiv.org/html/2601.04049v1#S2.SS3 "2.3 The exponential NIG model ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"), although the density function is known, given by ([3](https://arxiv.org/html/2601.04049v1#S2.E3 "In 2.3 The exponential NIG model ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")), the distribution function (and its inverse, the quantile function) needs to be treated numerically, typically incurring in high computational costs and instabilities. Thus, to make our approach generally applicable (and open the door for the utilisation of quantum algorithms which can potentially provide remarkable computational benefits), in next Section [3.1.2](https://arxiv.org/html/2601.04049v1#S3.SS1.SSS2 "3.1.2 Cosine-series density (and distribution) estimation ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"), a non-parametric density estimation relying on cosine basis functions is proposed, recalling its main theoretical properties, which will be later used to theoretically prove the quantum advantage.

#### 3.1.2 Cosine-series density (and distribution) estimation

Let f:ℝ→ℝ≥0f:\mathbb{R}\to\mathbb{R}\_{\geq 0} be a probability density function supported (or effectively supported) on a finite interval [a,b][a,b], associated to a random variable XX.
In orthogonal-series density estimation, the target density is expanded in a complete orthonormal basis of functions on [a,b][a,b],
and its coefficients are obtained by projection under the L2L^{2} inner product.
For the cosine basis

|  |  |  |
| --- | --- | --- |
|  | γk​(x)={1b−a,k=0,2b−a​cos⁡(k​π​(x−a)b−a),k≥1,\gamma\_{k}(x)=\begin{cases}\displaystyle\frac{1}{\sqrt{b-a}},&k=0,\\[8.0pt] \displaystyle\sqrt{\frac{2}{b-a}}\,\cos\!\Big(\frac{k\pi(x-a)}{b-a}\Big),&k\geq 1,\end{cases} |  |

we have the orthonormality property

|  |  |  |
| --- | --- | --- |
|  | ∫abγk​(x)​γℓ​(x)​dx=δk​ℓ,k,ℓ≥0,\int\_{a}^{b}\gamma\_{k}(x)\,\gamma\_{\ell}(x)\,\mathrm{d}x=\delta\_{k\ell},\qquad k,\ell\geq 0, |  |

with each basis function uniformly bounded by

|  |  |  |  |
| --- | --- | --- | --- |
|  | |γk​(x)|≤2b−a,x∈[a,b],k≥0,|\gamma\_{k}(x)|\leq\sqrt{\frac{2}{b-a}},\qquad x\in[a,b],\ k\geq 0, |  | (9) |

so that any square-integrable function f∈L2​([a,b])f\in L^{2}([a,b]) admits the cosine expansion

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(x)=∑k=0∞ak​γk​(x),f(x)=\sum\_{k=0}^{\infty}a\_{k}\,\gamma\_{k}(x), |  | (10) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | ak:=𝔼​[γk​(X)]=∫abf​(x)​γk​(x)​dx.a\_{k}:=\mathbb{E}[\gamma\_{k}(X)]=\int\_{a}^{b}f(x)\,\gamma\_{k}(x)\,\mathrm{d}x. |  | (11) |

###### Remark.

Sometimes, to obtain the aka\_{k} coefficients, it might be convenient to work with strictly positive basis functions. In that case, the following transformation can be applied,

|  |  |  |
| --- | --- | --- |
|  | γk+​(x)=12+12​b−a2​γk​(x),\gamma^{+}\_{k}(x)=\frac{1}{2}+\frac{1}{2}\sqrt{\frac{b-a}{2}}\gamma\_{k}(x), |  |

which satisfies 0≤γk+​(x)≤10\leq\gamma^{+}\_{k}(x)\leq 1. Then, the cosine coefficients can be equivalently obtained by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ak:=𝔼​[γk​(X)]=2b−a​(2​𝔼​[γk+​(X)]−1).a\_{k}:=\mathbb{E}[\gamma\_{k}(X)]=\sqrt{\frac{2}{b-a}}\left(2\mathbb{E}[\gamma^{+}\_{k}(X)]-1\right). |  | (12) |

Truncating the series in ([10](https://arxiv.org/html/2601.04049v1#S3.E10 "In 3.1.2 Cosine-series density (and distribution) estimation ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) to 𝒦\mathcal{K} terms yields the approximation

|  |  |  |
| --- | --- | --- |
|  | f​(x)≈f𝒦​(x):=∑k=0𝒦−1ak​γk​(x),f(x)\approx f^{\mathcal{K}}(x):=\sum\_{k=0}^{\mathcal{K}-1}a\_{k}\,\gamma\_{k}(x), |  |

which forms the basis of the Fourier–cosine (COS) method, widely used for density and option pricing computations (see e.g [[14](https://arxiv.org/html/2601.04049v1#bib.bib20 "A novel pricing method for european options based on fourier–cosine series expansions")]).
The convergence of f𝒦f^{\mathcal{K}} to ff depends on the smoothness or analyticity of ff,
as established in the following theorem.

###### Theorem 3.2 (Uniform cosine–series approximation on a finite interval).

Let f:[a,b]→ℝf:[a,b]\to\mathbb{R} be a real-valued function, and define its cosine coefficients

|  |  |  |
| --- | --- | --- |
|  | a0:=1b−a​∫abf​(x)​dx,ak:=2b−a​∫abf​(x)​cos⁡(k​π​(x−a)b−a)​dx,k≥1.a\_{0}:=\frac{1}{b-a}\int\_{a}^{b}f(x)\,\mathrm{d}x,\qquad a\_{k}:=\frac{2}{b-a}\int\_{a}^{b}f(x)\cos\!\left(\frac{k\pi(x-a)}{b-a}\right)\,\mathrm{d}x,\quad k\geq 1. |  |

Define the 𝒦\mathcal{K}-term partial sum

|  |  |  |
| --- | --- | --- |
|  | f𝒦​(x):=∑k=0𝒦−1ak​cos⁡(k​π​(x−a)b−a),x∈[a,b].f^{\mathcal{K}}(x):=\sum\_{k=0}^{\mathcal{K}-1}a\_{k}\cos\!\left(\frac{k\pi(x-a)}{b-a}\right),\qquad x\in[a,b]. |  |

Assume that the truncation interval [a,b][a,b] is chosen such that ff and its first m−1m-1 derivatives vanish (or are negligible) at the endpoints:

|  |  |  |
| --- | --- | --- |
|  | f(j)​(a)=f(j)​(b)=0,j=0,…,m−1.f^{(j)}(a)=f^{(j)}(b)=0,\qquad j=0,\ldots,m-1. |  |

This condition is satisfied, in practice, when ff is smooth and rapidly decaying outside [a,b][a,b].

Then:

1. 1.

   (Algebraic case)
   If f∈Cm​([a,b])f\in C^{m}([a,b]) and f(m)f^{(m)} has bounded variation on [a,b][a,b], there exists ζalg>0\zeta^{\mathrm{alg}}>0 such that, for every 𝒦≥1\mathcal{K}\geq 1,

   |  |  |  |
   | --- | --- | --- |
   |  | supx∈[a,b]|f​(x)−f𝒦​(x)|≤ζalg​𝒦−m,\sup\_{x\in[a,b]}|f(x)-f^{\mathcal{K}}(x)|\leq\zeta^{\mathrm{alg}}\mathcal{K}^{-m}, |  |

   and equivalently, the coefficients satisfy |ak|=O​(k−(m+1))|a\_{k}|=O(k^{-(m+1)}).
2. 2.

   (Exponential case)
   If ff extends analytically to the complex strip

   |  |  |  |
   | --- | --- | --- |
   |  | {z∈ℂ:|ℑ⁡z|<ρ}\{\,z\in\mathbb{C}:|\Im z|<\rho\,\} |  |

   containing [a,b][a,b] for some ρ>0\rho>0, then there exist constants ζexp,ν>0\zeta^{\mathrm{exp}},\nu>0 such that, for every 𝒦≥1\mathcal{K}\geq 1,

   |  |  |  |
   | --- | --- | --- |
   |  | supx∈[a,b]|f​(x)−f𝒦​(x)|≤ζexp​e−ν​𝒦,\sup\_{x\in[a,b]}|f(x)-f^{\mathcal{K}}(x)|\leq\zeta^{\mathrm{exp}}e^{-\nu\mathcal{K}}, |  |

   i.e. the cosine expansion converges uniformly at an exponential rate.

The constants ζalg,ζexp,ν\zeta^{\mathrm{alg}},\zeta^{\mathrm{exp}},\nu depend on ff, the interval [a,b][a,b], and the regularity parameters, but not on 𝒦\mathcal{K}.

###### Remark.

The endpoint assumption effectively enforces a compactly supported of ff on [a,b][a,b], ensuring the boundary terms vanish in repeated integration by parts. This is standard in Fourier–cosine and spectral approximation theory; see, e.g.,
Boyd [[3](https://arxiv.org/html/2601.04049v1#bib.bib18 "Chebyshev and fourier spectral methods")],
Trefethen [[41](https://arxiv.org/html/2601.04049v1#bib.bib19 "Spectral methods in matlab")],
Zygmund [[43](https://arxiv.org/html/2601.04049v1#bib.bib17 "Trigonometric series")],
and Fang and Oosterlee [[14](https://arxiv.org/html/2601.04049v1#bib.bib20 "A novel pricing method for european options based on fourier–cosine series expansions")].

#### 3.1.3 Estimating the marginal distributions

Next, we explain the process to estimate the marginal cumulative distribution functions. Here, we only consider sufficiently smooth marginal distributions that can be well approximated by cosine series (see the assumptions in Theorem [3.2](https://arxiv.org/html/2601.04049v1#S3.Thmtheorem2 "Theorem 3.2 (Uniform cosine–series approximation on a finite interval). ‣ 3.1.2 Cosine-series density (and distribution) estimation ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")), which is usually the case in option pricing.

Let XiX\_{i} denote the marginal random variable, whose corresponding density and distribution functions are fif\_{i} and FiF\_{i}, respectively. Then, given estimated coefficients a^kXi≈akXi:=𝔼​[γk​(Xi)]\hat{a}^{X\_{i}}\_{k}\approx a^{X\_{i}}\_{k}:=\mathbb{E}[\gamma\_{k}(X\_{i})] (see Equation ([11](https://arxiv.org/html/2601.04049v1#S3.E11 "In 3.1.2 Cosine-series density (and distribution) estimation ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"))), we have a cosine series approximating fif\_{i} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | fi≈f^i​(x):=∑k=0𝒦i−1a^kXi​γk​(x).f\_{i}\approx\hat{f}\_{i}(x):=\sum\_{k=0}^{\mathcal{K}\_{i}-1}\hat{a}^{X\_{i}}\_{k}\,\gamma\_{k}(x). |  | (13) |

Furthermore, by integrating this, we get an approximation F^i\hat{F}\_{i} for FiF\_{i}. In fact, since the accuracy of the cosine series approximation is guaranteed not on the entire real axis but in a finite interval, we set F^i\hat{F}\_{i} to 0 or 1 outside the interval. Namely, we define

|  |  |  |  |
| --- | --- | --- | --- |
|  | F^i​(x):={0,x<ai,∑k=0𝒦ia^kXi​Γk,[ai,bi]​(x),ai≤x<bi,1,x≥bi,\hat{F}\_{i}(x):=\begin{cases}0,&x<a\_{i},\\ \displaystyle\sum\_{k=0}^{\mathcal{K}\_{i}}\hat{a}^{X\_{i}}\_{k}\,\Gamma\_{k,[a\_{i},b\_{i}]}(x),&a\_{i}\leq x<b\_{i},\\ 1,&x\geq b\_{i},\end{cases} |  | (14) |

where,

|  |  |  |
| --- | --- | --- |
|  | Γk,[ai,bi]​(x):=∫aixγk​(t)​dt,\Gamma\_{k,[a\_{i},b\_{i}]}(x):=\int\_{a\_{i}}^{x}\gamma\_{k}(t)\,\mathrm{d}t, |  |

is given by

|  |  |  |
| --- | --- | --- |
|  | Γk,[ai,bi]​(x)={x−aibi−ai,k=0,2​(bi−ai)k​π​sin⁡(k​π​(x−ai)bi−ai),k≥1.\Gamma\_{k,[a\_{i},b\_{i}]}(x)=\begin{cases}\dfrac{x-a\_{i}}{\sqrt{\,b\_{i}-a\_{i}\,}},&k=0,\\[10.0pt] \dfrac{\sqrt{2(b\_{i}-a\_{i})}}{k\pi}\,\sin\!\displaystyle\Big(\dfrac{k\pi(x-a\_{i})}{b\_{i}-a\_{i}}\Big),&k\geq 1.\end{cases} |  |

### 3.2 Quantum algorithm for multidimensional options pricing

In this section, a quantum computing-based approach to address the problem of multidimensional option valuation formulated above is proposed, discussing both theoretical and practical implications. We begin summarizing the employed quantum routine, followed by some theoretical results supporting the quantum advantage, which will be empirically confirmed by the experiments in the next Section [3.3](https://arxiv.org/html/2601.04049v1#S3.SS3 "3.3 Experimental results ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").

#### 3.2.1 Quantum Accelerated Monte Carlo techniques

The Monte Carlo methods are well-known integration techniques for solving option pricing problems, when formulated in terms of expectations. This method gives an approximation of the value of definite integrals by generating random samples within the integration region and computing the average value of the function evaluated in these samples [[20](https://arxiv.org/html/2601.04049v1#bib.bib23 "Monte Carlo methods in financial engineering")].

Let us consider the computation of an expectation of a function of interest ϕ\phi (for example, the payoff hh in the options pricing problem described in Section [3.1](https://arxiv.org/html/2601.04049v1#S3.SS1 "3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline") or the cosine basis functions γk\gamma\_{k} as in Section [3.1.2](https://arxiv.org/html/2601.04049v1#S3.SS1.SSS2 "3.1.2 Cosine-series density (and distribution) estimation ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) acting on a multidimensional random variable 𝐗\mathbf{X}, given in the form of a NN-dimensional definite integral, namely,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[ϕ​(𝐗)]=∫Ωf​(𝐱)​ϕ​(𝐱)​dN​𝐱,\mathbb{E}[\phi(\mathbf{X})]=\int\_{\Omega}f(\mathbf{x})\phi(\mathbf{x})\,\mathrm{d}^{N}\mathbf{x}, |  |

where ff is a density with compact support Ω\Omega. Note that the definitions of both the price of a multidimensional option in ([5](https://arxiv.org/html/2601.04049v1#S3.E5 "In 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) and the cosine series expansion coefficients in ([11](https://arxiv.org/html/2601.04049v1#S3.E11 "In 3.1.2 Cosine-series density (and distribution) estimation ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) can be cast into this formulation.

Thus, the well-established CMC method consists in generating LL independent and identically distributed NN-dimensional samples 𝐗l\mathbf{X}\_{l}, for l=0,…,L−1l=0,\dots,L-1, drawn from the distribution associated with ff, such that the value of the integral is approximated by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫Ωf​(𝐱)​ϕ​(𝐱)​dN​𝐱≈1L​∑l=0L−1ϕ​(𝐗l).\int\_{\Omega}f(\mathbf{x})\phi(\mathbf{x})\,\mathrm{d}^{N}\mathbf{x}\approx\frac{1}{L}\sum\_{l=0}^{L-1}\phi(\mathbf{X}\_{l}). |  | (15) |

Since this method can be computationally demanding for certain types of integrals, in recent years the advantages offered by quantum computing have been exploited to develop QAMC techniques [[33](https://arxiv.org/html/2601.04049v1#bib.bib21 "Quantum speedup of monte carlo methods"), [37](https://arxiv.org/html/2601.04049v1#bib.bib30 "Quantum computational finance: Monte Carlo pricing of financial derivatives"), [21](https://arxiv.org/html/2601.04049v1#bib.bib29 "A survey on quantum computational finance for derivatives pricing and VaR")], which promise a quadratic improvement, in terms of the estimation error, in the number of queries required compared to its classical counterpart.

The common starting point relies on a discrete version of the integral, namely a Riemann sum, defined in J=2N​nJ=2^{Nn} discrete points, being nn the number of qubits employed in the discretization for each dimension111We have assumed, without any loss of generality, the same number of discrete points in every space direction., which is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫Ωf​(𝐱)​ϕ​(𝐱)​dN​𝐱≈∑j=0J−1f​(𝐱j)​ϕ​(𝐱j).\int\_{\Omega}f(\mathbf{x})\phi(\mathbf{x})\,\mathrm{d}^{N}\mathbf{x}\approx\sum\_{j=0}^{J-1}f(\mathbf{x}\_{j})\phi(\mathbf{x}\_{j}). |  | (16) |

The idea behind the QAMC method is to encapsulate the value of the integral within the amplitudes of a quantum state, and then maximize the probability of obtaining this value when performing a measurement. For this purpose, we then assume that the following state on a circuit of N​n+1Nn+1 qubits can be constructed222We have intentionally omitted the normalization constants for the sake of clarity.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |ψ⟩=𝒰​|x1⟩n​…​|xN⟩n​|0⟩\displaystyle|\psi\rangle=\mathcal{U}|x\_{1}\rangle^{n}\dots|x\_{N}\rangle^{n}|0\rangle | =∑j=02N​n−1f​(𝐱j)​ϕ​(𝐱j)​|x1⟩n​…​|xN⟩n​|1⟩\displaystyle=\sum\_{j=0}^{2^{Nn}-1}\sqrt{f(\mathbf{x}\_{j})\phi(\mathbf{x}\_{j})}\,|x\_{1}\rangle^{n}\dots|x\_{N}\rangle^{n}|1\rangle |  | (17) |
|  |  | +∑j=02N​n−11−f​(𝐱j)​ϕ​(𝐱j)​|x1⟩n​…​|xN⟩n​|0⟩,\displaystyle+\sum\_{j=0}^{2^{Nn}-1}\sqrt{1-f(\mathbf{x}\_{j})\phi(\mathbf{x}\_{j})}\,|x\_{1}\rangle^{n}\dots|x\_{N}\rangle^{n}|0\rangle, |  |

where 𝒰\mathcal{U} is a quantum operator which encapsulates the (square root of the) Riemann sum that approximates the desired integral into the amplitude of the ancillary qubit’s state |1⟩|1\rangle. The oracle 𝒰\mathcal{U} is typically composed of two operators, one loading the density, ff, and one loading the function of interest, ϕ\phi. There exist many methods in the literature to perform this type of quantum state preparation, see e.g. [[23](https://arxiv.org/html/2601.04049v1#bib.bib31 "Creating superpositions that correspond to efficiently integrable probability distributions"), [42](https://arxiv.org/html/2601.04049v1#bib.bib35 "Quantum generative adversarial networks for learning and loading random distributions"), [39](https://arxiv.org/html/2601.04049v1#bib.bib32 "Option pricing using quantum computers"), [7](https://arxiv.org/html/2601.04049v1#bib.bib33 "Efficient state preparation for quantum amplitude estimation"), [34](https://arxiv.org/html/2601.04049v1#bib.bib34 "Linear-depth quantum circuits for loading Fourier approximations of arbitrary functions")], for which, as considered here, an auxiliary ancilla qubit is typically required (the last qubit of the quantum state |ψ⟩|\psi\rangle in ([17](https://arxiv.org/html/2601.04049v1#S3.E17 "In 3.2.1 Quantum Accelerated Monte Carlo techniques ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"))).

Then, the value of the integral can be estimated through the QAE routine [[4](https://arxiv.org/html/2601.04049v1#bib.bib22 "Quantum amplitud amplification and estimation"), [33](https://arxiv.org/html/2601.04049v1#bib.bib21 "Quantum speedup of monte carlo methods")], a quantum algorithm that allows to efficiently retrieve the amplitude information from a quantum state. In this particular formulation (where a square root encoding is employed), the probability of obtaining |1⟩|1\rangle when measuring the state |ψ⟩|\psi\rangle, i.e., the squared amplitude of the state, is precisely the Riemann estimator of the integral in ([16](https://arxiv.org/html/2601.04049v1#S3.E16 "In 3.2.1 Quantum Accelerated Monte Carlo techniques ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) that, in turn, approximates 𝔼​[ϕ​(𝐱)]\mathbb{E}[\phi(\mathbf{x})]. As it will be shown in the following Sections [3.2.2](https://arxiv.org/html/2601.04049v1#S3.SS2.SSS2 "3.2.2 Quantum advantage: theoretical results ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline") and [3.3](https://arxiv.org/html/2601.04049v1#S3.SS3 "3.3 Experimental results ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"), the application of the QAE to the proposed multivariate option valuation methodology results in remarkable accelerations with respect to the CMC approaches, from both theoretical and empirical viewpoints.

#### 3.2.2 Quantum advantage: theoretical results

Let us first recall the well-known result that forms the basis of the QAMC method, namely the QAE routine, formulated in the next theorem.

###### Theorem 3.3 (Quantum Amplitude Estimation; Theorem 2.3 in [[33](https://arxiv.org/html/2601.04049v1#bib.bib21 "Quantum speedup of monte carlo methods")]).

Let ϱ,ϵ∈(0,1)\varrho,\epsilon\in(0,1).
Assuming we have access to the state preparation oracle 𝒜Y\mathcal{A}\_{Y} for a random variable Y∈ℝNY\in\mathbb{R}^{N} and the controlled rotation oracle WϕW\_{\phi} for a function ϕ:ℝN→[0,1]\phi:\mathbb{R}^{N}\to[0,1], there exists a quantum algorithm that, with probability at least 1−ϱ1-\varrho, outputs an ϵ\epsilon-approximation of 𝔼Y​[ϕ​(Y)]\mathbb{E}\_{Y}[\phi(Y)], querying 𝒜Y\mathcal{A}\_{Y} and WϕW\_{\phi}

|  |  |  |
| --- | --- | --- |
|  | O​(1ϵ​log⁡1ϱ)O\!\left(\frac{1}{\epsilon}\log\!\frac{1}{\varrho}\right) |  |

times each.

###### Remark.

Note that, in this context, we assume that querying a quantum oracle one time is equivalent to draw a single sample from a given distribution in the classical computation, avoiding as well the discussion on any particular computational capability aspect or technology readiness. Then, in Section [3.3](https://arxiv.org/html/2601.04049v1#S3.SS3 "3.3 Experimental results ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"), the number of samples and queries will be fairly compared under these premises.

#### Quantum estimation of the marginal distributions

Before deriving a rigorous theoretical result for the convergence in estimating the marginal distributions with QAMC techniques, we briefly discuss how to build the quantum state required to apply them (see Section [3.2.1](https://arxiv.org/html/2601.04049v1#S3.SS2.SSS1 "3.2.1 Quantum Accelerated Monte Carlo techniques ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")). First, to follow the approach described in Sections [3.1.2](https://arxiv.org/html/2601.04049v1#S3.SS1.SSS2 "3.1.2 Cosine-series density (and distribution) estimation ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline") and [3.1.3](https://arxiv.org/html/2601.04049v1#S3.SS1.SSS3 "3.1.3 Estimating the marginal distributions ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"), we need to define an oracle that encapsulates the Riemann sum approximating the expectation in ([11](https://arxiv.org/html/2601.04049v1#S3.E11 "In 3.1.2 Cosine-series density (and distribution) estimation ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")). For that, as it is common in the literature, two quantum operations are combined, loading the probability density function and a function of interest into the amplitude of a quantum state. In this case, to load fif\_{i}, we assume the availability of an oracle 𝒜Xi\mathcal{A}\_{X\_{i}} such that333As we are treating with marginal distributions, the dimensionality of the problem is one, allowing us to avoid the vector-like bold notation.

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜Xi​|0⟩n=∑j=02n−1fi​(xj)​|x⟩n.\mathcal{A}\_{X\_{i}}|0\rangle^{n}=\sum\_{j=0}^{2^{n}-1}\sqrt{f\_{i}(x\_{j})}\,|x\rangle^{n}. |  | (18) |

Next, by employing a controlled rotation, the function of interest is loaded. Then, let us assume that we have access to the controlled rotation operation WγkW\_{\gamma\_{k}}, for k=0,…,𝒦i−1k=0,\ldots,\mathcal{K}\_{i}-1, which transforms state ([18](https://arxiv.org/html/2601.04049v1#S3.E18 "In Quantum estimation of the marginal distributions ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) into the state

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝒰ak​|0⟩n​|0⟩:=Wγk​(AXi⊗ℐ)​|0⟩n​|0⟩\displaystyle\mathcal{U}\_{a\_{k}}|0\rangle^{n}|0\rangle=W\_{\gamma\_{k}}(A\_{X\_{i}}\otimes\mathcal{I})|0\rangle^{n}|0\rangle | =∑j=02n−1fi​(xj)​γk​(xj)​|x⟩n​|1⟩\displaystyle=\sum\_{j=0}^{2^{n}-1}\sqrt{f\_{i}(x\_{j})\gamma\_{k}(x\_{j})}\,|x\rangle^{n}|1\rangle |  | (19) |
|  |  | +∑j=02n−1(1−fi(xj)γk(xj)​|x⟩n​|0⟩,\displaystyle+\sum\_{j=0}^{2^{n}-1}\sqrt{(1-f\_{i}(x\_{j})\gamma\_{k}(x\_{j})}\,|x\rangle^{n}|0\rangle, |  |

where ℐ\mathcal{I} is the identity matrix and we have defined the operator 𝒰ak:=Wγk​(AXi⊗ℐ)\mathcal{U}\_{a\_{k}}:=W\_{\gamma\_{k}}(A\_{X\_{i}}\otimes\mathcal{I}), which fit into the general description of QAMC in Section [3.2.1](https://arxiv.org/html/2601.04049v1#S3.SS2.SSS1 "3.2.1 Quantum Accelerated Monte Carlo techniques ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"). Below, the main theorem providing the accuracy of the QAMC method and the costs associated when applied it to recover the marginal distributions is presented.

###### Theorem 3.4 (Quantum complexity recovering the marginal distributions).

Let ϱi,ϵi∈(0,1)\varrho\_{i},\epsilon\_{i}\in(0,1). Let XiX\_{i} be a real-valued random variable following the distribution fif\_{i}.
Assume the following:

1. 1.

   fif\_{i} has the properties of Theorem [3.2](https://arxiv.org/html/2601.04049v1#S3.Thmtheorem2 "Theorem 3.2 (Uniform cosine–series approximation on a finite interval). ‣ 3.1.2 Cosine-series density (and distribution) estimation ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
2. 2.

   Access to the oracle 𝒰ak\mathcal{U}\_{a\_{k}} as in ([19](https://arxiv.org/html/2601.04049v1#S3.E19 "In Quantum estimation of the marginal distributions ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) for k=0,…,𝒦i−1k=0,\ldots,\mathcal{K}\_{i}-1.
3. 3.

   For some [ai,bi][a\_{i},b\_{i}], Fi​(ai)≤ϵi/2F\_{i}(a\_{i})\leq\epsilon\_{i}/2 and Fi​(bi)≥1−ϵiF\_{i}(b\_{i})\geq 1-\epsilon\_{i} hold.

Then, with probability at least 1−ϱi1-\varrho\_{i}, we get F^i\hat{F}\_{i} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |F^i​(x)−Fi​(x)|≤ϵi\left|\hat{F}\_{i}(x)-F\_{i}(x)\right|\leq\epsilon\_{i} |  | (20) |

for any x∈ℝx\in\mathbb{R} by Theorem [3.3](https://arxiv.org/html/2601.04049v1#S3.Thmtheorem3 "Theorem 3.3 (Quantum Amplitude Estimation; Theorem 2.3 in [33]). ‣ 3.2.2 Quantum advantage: theoretical results ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"), querying 𝒰ak\mathcal{U}\_{a\_{k}}
for k=0,…,𝒦i−1k=0,\ldots,\mathcal{K}\_{i}-1

|  |  |  |
| --- | --- | --- |
|  | O​(bi−ai​𝒦i2ϵi​log⁡𝒦iϱi)O\!\left(\frac{\sqrt{b\_{i}-a\_{i}}\mathcal{K}^{2}\_{i}}{\epsilon\_{i}}\log\!\frac{\mathcal{K}\_{i}}{\varrho\_{i}}\right) |  |

times.

* •

  For the algebraic case, we set

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 𝒦i=⌈(4​ζialg​(bi−ai)ϵi)1mi⌉,\mathcal{K}\_{i}=\left\lceil\left(\frac{4\zeta^{\mathrm{alg}}\_{i}(b\_{i}-a\_{i})}{\epsilon\_{i}}\right)^{\frac{1}{m\_{i}}}\right\rceil, |  | (21) |

  where ζialg\zeta^{\mathrm{alg}}\_{i} is a real number such that

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | supx∈[ai,bi]|fi𝒦​(x)−fi​(x)|≤ζialg​𝒦−mi\sup\_{x\in[a\_{i},b\_{i}]}\left|f\_{i}^{\mathcal{K}}(x)-f\_{i}(x)\right|\leq\zeta^{\mathrm{alg}}\_{i}\mathcal{K}^{-m\_{i}} |  | (22) |

  holds for any 𝒦∈ℕ\mathcal{K}\in\mathbb{N}.
* •

  For the exponential case, we set

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 𝒦i=⌈log⁡[(4​ζiexp​(bi−ai)ϵi)1νi]⌉,\mathcal{K}\_{i}=\left\lceil\log\left[\left(\frac{4\zeta^{\mathrm{exp}}\_{i}(b\_{i}-a\_{i})}{\epsilon\_{i}}\right)^{\frac{1}{\nu\_{i}}}\right]\right\rceil, |  | (23) |

  where ζiexp\zeta^{\mathrm{exp}}\_{i} is a real number such that

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | supx∈[ai,bi]|fi𝒦​(x)−fi​(x)|≤ζiexp​e−νi​𝒦\sup\_{x\in[a\_{i},b\_{i}]}\left|f\_{i}^{\mathcal{K}}(x)-f\_{i}(x)\right|\leq\zeta^{\mathrm{exp}}\_{i}e^{-\nu\_{i}\mathcal{K}} |  | (24) |

  holds for any 𝒦∈ℕ\mathcal{K}\in\mathbb{N}.

###### Proof.

Because of the definition of F^i\hat{F}\_{i} in ([14](https://arxiv.org/html/2601.04049v1#S3.E14 "In 3.1.3 Estimating the marginal distributions ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) and Assumption [3](https://arxiv.org/html/2601.04049v1#S3.I4.i3 "item 3 ‣ Theorem 3.4 (Quantum complexity recovering the marginal distributions). ‣ Quantum estimation of the marginal distributions ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"), it is immediately seen that ([20](https://arxiv.org/html/2601.04049v1#S3.E20 "In Theorem 3.4 (Quantum complexity recovering the marginal distributions). ‣ Quantum estimation of the marginal distributions ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) holds for any x∈(−∞,−ai]∪[bi,∞)x\in(-\infty,-a\_{i}]\cup[b\_{i},\infty).
Thus, we hereafter focus on the case that x∈(ai,bi)x\in(a\_{i},b\_{i}).
We start by evaluating |f^i​(x)−fi​(x)||\hat{f}\_{i}(x)-f\_{i}(x)|. Decomposing it as

|  |  |  |  |
| --- | --- | --- | --- |
|  | |f^i​(x)−fi​(x)|≤|f^i​(x)−fi𝒦i​(x)|+|fi𝒦i​(x)−fi​(x)||\hat{f}\_{i}(x)-f\_{i}(x)|\leq|\hat{f}\_{i}(x)-f\_{i}^{\mathcal{K}\_{i}}(x)|+|f\_{i}^{\mathcal{K}\_{i}}(x)-f\_{i}(x)| |  | (25) |

The first term is the Monte Carlo error and the second one the series truncation error.
We bound each term separately. For the second term, for x∈(ai,bi)x\in(a\_{i},b\_{i}), in the algebraic convergence case, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | |fi𝒦i​(x)−fi​(x)|≤ζialg​𝒦i−mi≤ϵi4​(bi−ai),\left|f\_{i}^{\mathcal{K}\_{i}}(x)-f\_{i}(x)\right|\leq\zeta^{\mathrm{alg}}\_{i}\mathcal{K}\_{i}^{-m\_{i}}\leq\frac{\epsilon\_{i}}{4(b\_{i}-a\_{i})}, |  | (26) |

where we use ([22](https://arxiv.org/html/2601.04049v1#S3.E22 "In 1st item ‣ Theorem 3.4 (Quantum complexity recovering the marginal distributions). ‣ Quantum estimation of the marginal distributions ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) with 𝒦i\mathcal{K}\_{i} defined as in ([21](https://arxiv.org/html/2601.04049v1#S3.E21 "In 1st item ‣ Theorem 3.4 (Quantum complexity recovering the marginal distributions). ‣ Quantum estimation of the marginal distributions ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")). In the exponential convergence case, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | |fi𝒦i​(x)−fi​(x)|≤ζiexp​e−νi​𝒦i≤ϵi4​(bi−ai),\left|f\_{i}^{\mathcal{K}\_{i}}(x)-f\_{i}(x)\right|\leq\zeta^{\mathrm{exp}}\_{i}e^{-\nu\_{i}\mathcal{K}\_{i}}\leq\frac{\epsilon\_{i}}{4(b\_{i}-a\_{i})}, |  | (27) |

where we use ([24](https://arxiv.org/html/2601.04049v1#S3.E24 "In 2nd item ‣ Theorem 3.4 (Quantum complexity recovering the marginal distributions). ‣ Quantum estimation of the marginal distributions ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) with 𝒦i\mathcal{K}\_{i} defined as in ([23](https://arxiv.org/html/2601.04049v1#S3.E23 "In 2nd item ‣ Theorem 3.4 (Quantum complexity recovering the marginal distributions). ‣ Quantum estimation of the marginal distributions ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")). To bound the first one, we temporarily assume that,
relying on Theorem [3.3](https://arxiv.org/html/2601.04049v1#S3.Thmtheorem3 "Theorem 3.3 (Quantum Amplitude Estimation; Theorem 2.3 in [33]). ‣ 3.2.2 Quantum advantage: theoretical results ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline") with δ=ϱi𝒦i\delta=\frac{\varrho\_{i}}{\mathcal{K}\_{i}} and ϵ=ϵi4​𝒦i​2​(bi−ai)\epsilon=\frac{\epsilon\_{i}}{4\mathcal{K}\_{i}\sqrt{2(b\_{i}-a\_{i})}}, a quantum algorithm outputs the estimation 𝔼^Xi​[γk​(Xi)]\widehat{\mathbb{E}}\_{X\_{i}}[\gamma\_{k}(X\_{i})] for every k=0,…,𝒦i−1k=0,...,\mathcal{K}\_{i}-1 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |𝔼^Xi​[γk​(Xi)]−𝔼Xi​[γk​(Xi)]|=|a^kXi−akXi|≤ϵi4​𝒦i​2​(bi−ai).\left|\widehat{\mathbb{E}}\_{X\_{i}}[\gamma\_{k}(X\_{i})]-\mathbb{E}\_{X\_{i}}[\gamma\_{k}(X\_{i})]\right|=|\hat{a}^{X\_{i}}\_{k}-a^{X\_{i}}\_{k}|\leq\frac{\epsilon\_{i}}{4\mathcal{K}\_{i}\sqrt{2(b\_{i}-a\_{i})}}. |  | (28) |

We then have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |f^i​(x)−fi𝒦i​(x)|\displaystyle\left|\hat{f}\_{i}(x)-f\_{i}^{\mathcal{K}\_{i}}(x)\right| | =|∑k=0𝒦i−1(a^kXi−akXi)​γk​(x)|\displaystyle=\left|\sum\_{k=0}^{\mathcal{K}\_{i}-1}\left(\hat{a}\_{k}^{X\_{i}}-a\_{k}^{X\_{i}}\right)\gamma\_{k}(x)\right| |  | (29) |
|  |  | ≤∑k=0𝒦i−1|a^kXi−akXi|​2bi−ai\displaystyle\leq\sum\_{k=0}^{\mathcal{K}\_{i}-1}\left|\hat{a}\_{k}^{X\_{i}}-a\_{k}^{X\_{i}}\right|\sqrt{\frac{2}{b\_{i}-a\_{i}}} |  |
|  |  | ≤ϵi4​(bi−ai)\displaystyle\leq\frac{\epsilon\_{i}}{4(b\_{i}-a\_{i})} |  |

where we use ([9](https://arxiv.org/html/2601.04049v1#S3.E9 "In 3.1.2 Cosine-series density (and distribution) estimation ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) at the first inequality and ([28](https://arxiv.org/html/2601.04049v1#S3.E28 "In Proof. ‣ Quantum estimation of the marginal distributions ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) at the second inequality.

Combining ([25](https://arxiv.org/html/2601.04049v1#S3.E25 "In Proof. ‣ Quantum estimation of the marginal distributions ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")), ([26](https://arxiv.org/html/2601.04049v1#S3.E26 "In Proof. ‣ Quantum estimation of the marginal distributions ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) (or ([27](https://arxiv.org/html/2601.04049v1#S3.E27 "In Proof. ‣ Quantum estimation of the marginal distributions ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"))) and ([29](https://arxiv.org/html/2601.04049v1#S3.E29 "In Proof. ‣ Quantum estimation of the marginal distributions ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) gives

|  |  |  |
| --- | --- | --- |
|  | |f^i​(x)−fi​(x)|≤ϵi2​(bi−ai).\left|\hat{f}\_{i}(x)-f\_{i}(x)\right|\leq\frac{\epsilon\_{i}}{2(b\_{i}-a\_{i})}. |  |

Integrating this over (ai,x](a\_{i},x] yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Fi​(x)−F^i​(x)|\displaystyle\left|F\_{i}(x)-\hat{F}\_{i}(x)\right| | ≤|Fi​(ai)|+∫aix|f^i​(y)−fi​(y)|​dy\displaystyle\leq|F\_{i}(a\_{i})|+\int\_{a\_{i}}^{x}\left|\hat{f}\_{i}(y)-f\_{i}(y)\right|\mathrm{d}y |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤ϵi2+ϵi2​(bi−ai)​(x−ai)\displaystyle\leq\frac{\epsilon\_{i}}{2}+\frac{\epsilon\_{i}}{2(b\_{i}-a\_{i})}(x-a\_{i}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤ϵi\displaystyle\leq\epsilon\_{i} |  |

for x∈(ai,bi)x\in(a\_{i},b\_{i}).

To complete the proof, let us prove the statements on the success probability and complexity.
Since the probability that each of
the applications of Theorem [3.3](https://arxiv.org/html/2601.04049v1#S3.Thmtheorem3 "Theorem 3.3 (Quantum Amplitude Estimation; Theorem 2.3 in [33]). ‣ 3.2.2 Quantum advantage: theoretical results ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline") with ϱ=ϱi𝒦i\varrho=\frac{\varrho\_{i}}{\mathcal{K}\_{i}} and ϵ=ϵi4​𝒦i​2​(bi−ai)\epsilon=\frac{\epsilon\_{i}}{4\mathcal{K}\_{i}\sqrt{2(b\_{i}-a\_{i})}} for every k=0,…,𝒦i−1k=0,...,\mathcal{K}\_{i}-1 outputs 𝔼^Xi​[γk​(Xi)]\widehat{\mathbb{E}}\_{X\_{i}}[\gamma\_{k}(X\_{i})] satisfying ([28](https://arxiv.org/html/2601.04049v1#S3.E28 "In Proof. ‣ Quantum estimation of the marginal distributions ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) is at least 1−ϱi𝒦i1-\frac{\varrho\_{i}}{\mathcal{K}\_{i}},
the probability that *all* of them output such estimations is

|  |  |  |
| --- | --- | --- |
|  | ∏k=0𝒦i−1(1−ϱi𝒦i)=(1−ϱi𝒦i)𝒦i.\prod\_{k=0}^{\mathcal{K}\_{i}-1}\left(1-\frac{\varrho\_{i}}{\mathcal{K}\_{i}}\right)=\left(1-\frac{\varrho\_{i}}{\mathcal{K}\_{i}}\right)^{\mathcal{K}\_{i}}. |  |

Using the inequality (1−x)p≥1−p​x(1-x)^{p}\geq 1-px for x∈[0,1]x\in[0,1] and integer p∈ℕp\in\mathbb{N}, we obtain

|  |  |  |
| --- | --- | --- |
|  | (1−ϱi𝒦i)𝒦i≥1−ϱi.\left(1-\frac{\varrho\_{i}}{\mathcal{K}\_{i}}\right)^{\mathcal{K}\_{i}}\geq 1-\varrho\_{i}. |  |

From Theorem [3.3](https://arxiv.org/html/2601.04049v1#S3.Thmtheorem3 "Theorem 3.3 (Quantum Amplitude Estimation; Theorem 2.3 in [33]). ‣ 3.2.2 Quantum advantage: theoretical results ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"), the number of queries to each 𝒰ak\mathcal{U}\_{a\_{k}} (composed of the state preparation oracle 𝒜Xi\mathcal{A}\_{X\_{i}} and the controlled rotation oracle WγkW\_{\gamma\_{k}}, see ([19](https://arxiv.org/html/2601.04049v1#S3.E19 "In Quantum estimation of the marginal distributions ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"))) is

|  |  |  |
| --- | --- | --- |
|  | O​(bi−ai​𝒦iϵi​log⁡(𝒦iϱi)).O\!\left(\frac{\sqrt{b\_{i}-a\_{i}}\mathcal{K}\_{i}}{\epsilon\_{i}}\log\!\left(\frac{\mathcal{K}\_{i}}{\varrho\_{i}}\right)\right). |  |

Finally, summing them up for k=0,…,𝒦i−1k=0,...,\mathcal{K}\_{i}-1, we get

|  |  |  |
| --- | --- | --- |
|  | O​(bi−ai​𝒦i2ϵi​log⁡(𝒦iϱi)).O\!\left(\frac{\sqrt{b\_{i}-a\_{i}}\mathcal{K}\_{i}^{2}}{\epsilon\_{i}}\log\!\left(\frac{\mathcal{K}\_{i}}{\varrho\_{i}}\right)\right). |  |

∎

#### Quantum estimation of the multidimensional option price

Once the marginal distribution functions are computed (and having defined a copula), the multidimensional option pricing machinery described in Section [3.1](https://arxiv.org/html/2601.04049v1#S3.SS1 "3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline") can be readily applied, where the QAMC methods can be further employed, specifically, in the computation of the integral/expectation in either expression ([5](https://arxiv.org/html/2601.04049v1#S3.E5 "In 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) or expression ([8](https://arxiv.org/html/2601.04049v1#S3.E8 "In Multidimensional option valuation with copulas ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")). Next, we describe how to proceed to encapsulate the required quantum state in each case which, from now on, we termed as joint and independent formulations, respectively.

For the joint case, we need to build a quantum state that resembles the integral value in ([5](https://arxiv.org/html/2601.04049v1#S3.E5 "In 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) using an approximated joint density obtained via copulas as

|  |  |  |
| --- | --- | --- |
|  | f^​(𝐱)=f^​(x1,…,xN):=c​(F^1​(x1),…,F^N​(xN))⋅∏i=1Nf^i​(xi),\hat{f}(\mathbf{x})=\hat{f}(x\_{1},\dots,x\_{N}):=c\left(\hat{F}\_{1}(x\_{1}),\dots,\hat{F}\_{N}(x\_{N})\right)\cdot\prod\_{i=1}^{N}\hat{f}\_{i}(x\_{i}), |  |

where f^i\hat{f}\_{i} and F^i\hat{F}\_{i}, i=1,…,Ni=1,\dots,N, are approximated density and distribution functions given by ([13](https://arxiv.org/html/2601.04049v1#S3.E13 "In 3.1.3 Estimating the marginal distributions ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) and ([14](https://arxiv.org/html/2601.04049v1#S3.E14 "In 3.1.3 Estimating the marginal distributions ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")), respectively. Then, let us now assume the access to a quantum operator 𝒜𝐗\mathcal{A}\_{\mathbf{X}} which acts on an initial zero state as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜𝐗​|0⟩n​…​|0⟩n=∑j=02N​n−1f^​(𝐱j)​|x1⟩n​…​|xN⟩n,\mathcal{A}\_{\mathbf{X}}|0\rangle^{n}\dots|0\rangle^{n}=\sum\_{j=0}^{2^{Nn}-1}\sqrt{\hat{f}(\mathbf{x}\_{j})}\,|x\_{1}\rangle^{n}\dots|x\_{N}\rangle^{n}, |  | (30) |

so it loads the square root of the approximated joint density function f^\hat{f} in the amplitude of a quantum state. Next, to approximate the option price, we then need to load the payoff function h​(⋅)h(\cdot), for which, an oracle WhW\_{h} is required, after whose application to the previously defined state ([30](https://arxiv.org/html/2601.04049v1#S3.E30 "In Quantum estimation of the multidimensional option price ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")), we obtain

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Wh​(𝒜𝐗⊗ℐ)​|0⟩n​…​|0⟩n​|0⟩\displaystyle W\_{h}(\mathcal{A}\_{\mathbf{X}}\otimes\mathcal{I})|0\rangle^{n}\dots|0\rangle^{n}|0\rangle | =∑j=02N​n−1f^​(𝐱j)​h​(𝐱j)​|x1⟩n​…​|xN⟩n​|1⟩\displaystyle=\sum\_{j=0}^{2^{Nn}-1}\sqrt{\hat{f}(\mathbf{x}\_{j})h(\mathbf{x}\_{j})}\,|x\_{1}\rangle^{n}\dots|x\_{N}\rangle^{n}|1\rangle |  | (31) |
|  |  | +∑j=02N​n−1(1−f^(𝐱j)h(𝐱j)​|x1⟩n​…​|xN⟩n​|0⟩.\displaystyle+\sum\_{j=0}^{2^{Nn}-1}\sqrt{(1-\hat{f}(\mathbf{x}\_{j})h(\mathbf{x}\_{j})}\,|x\_{1}\rangle^{n}\dots|x\_{N}\rangle^{n}|0\rangle. |  |

In order to cast these derivations into the general description of QAMC from Section [3.2.1](https://arxiv.org/html/2601.04049v1#S3.SS2.SSS1 "3.2.1 Quantum Accelerated Monte Carlo techniques ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"), we denote by 𝒰V:=Wh​(𝒜𝐗⊗ℐ)\mathcal{U}\_{V}:=W\_{h}(\mathcal{A}\_{\mathbf{X}}\otimes\mathcal{I}) the oracle that constructs a quantum state which allows to estimate the multidimendional option price emplyoing the joint formulation. Under the premises of Theorem [3.3](https://arxiv.org/html/2601.04049v1#S3.Thmtheorem3 "Theorem 3.3 (Quantum Amplitude Estimation; Theorem 2.3 in [33]). ‣ 3.2.2 Quantum advantage: theoretical results ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"), a QAMC algorithm provides an approximation of the (non-discounted) price given by the 𝔼​[h​(𝐗)]\mathbb{E}[h(\mathbf{X})] with precision less than a prescribed ϵV\epsilon\_{V}, within a given confidence 1−ϱV1-\varrho\_{V}, and querying 𝒰V\mathcal{U}\_{V} an order O​(1ϵV​log⁡1ϱV)O\left(\frac{1}{\epsilon\_{V}}\log\frac{1}{\varrho\_{V}}\right) of times.

The independent case leverages the decomposition, thanks to the copula properties, of the joint density in two terms as shown in ([7](https://arxiv.org/html/2601.04049v1#S3.E7 "In 3.1.1 Joint distribution via copulas ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")), and already exploited in ([8](https://arxiv.org/html/2601.04049v1#S3.E8 "In Multidimensional option valuation with copulas ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")).
Again, given the approximations of the distribution functions F^1,…,F^N\widehat{F}\_{1},\ldots,\widehat{F}\_{N} in the form of ([14](https://arxiv.org/html/2601.04049v1#S3.E14 "In 3.1.3 Estimating the marginal distributions ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")), we define an adjusted payoff function as

|  |  |  |  |
| --- | --- | --- | --- |
|  | H^​(𝐱)=H^​(x1,…,xN):=1cmax​h​(x)​c​(F^1​(x1),…,F^N​(xN)),cmax:=maxu∈[0,1]N⁡c​(u),\hat{H}(\mathbf{x})=\hat{H}(x\_{1},\dots,x\_{N}):=\frac{1}{c\_{\max}}\,h(x)\,c\!\left(\hat{F}\_{1}(x\_{1}),\ldots,\hat{F}\_{N}(x\_{N})\right),\quad c\_{\max}:=\max\_{u\in[0,1]^{N}}c(u), |  | (32) |

which is an approximation of

|  |  |  |  |
| --- | --- | --- | --- |
|  | H​(𝐱)=1cmax​h​(x)​c​(F1​(x1),…,FN​(xN)).H(\mathbf{x})=\frac{1}{c\_{\max}}\,h(x)\,c\!\left(F\_{1}(x\_{1}),\ldots,F\_{N}(x\_{N})\right). |  | (33) |

Next, an oracle, 𝒜𝐗ind\mathcal{A}^{\mathrm{ind}}\_{\mathbf{X}}, encapsulating the *independent* joint distribution, find​(𝐱)=find​(x1,…,xN):=∏i=1Nfi​(xi)f^{\mathrm{ind}}(\mathbf{x})=f^{\mathrm{ind}}(x\_{1},\dots,x\_{N}):=\prod\_{i=1}^{N}f\_{i}(x\_{i}) is required. Thus, let us assume that we can build, as before, a N​nNn-qubit quantum state as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜𝐗ind​|0⟩n​…​|0⟩n=∑j=02N​n−1find​(𝐱j)​|x1⟩n​…​|xN⟩n.\mathcal{A}^{\mathrm{ind}}\_{\mathbf{X}}|0\rangle^{n}\dots|0\rangle^{n}=\sum\_{j=0}^{2^{Nn}-1}\sqrt{f^{\mathrm{ind}}(\mathbf{x}\_{j})}\,|x\_{1}\rangle^{n}\dots|x\_{N}\rangle^{n}. |  | (34) |

In order to load the (approximated) adjusted payoff function from ([32](https://arxiv.org/html/2601.04049v1#S3.E32 "In Quantum estimation of the multidimensional option price ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")), we again consider a quantum rotation operator WH^W\_{\hat{H}} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | WH^​(𝒜𝐗ind⊗ℐ)​|0⟩n​…​|0⟩n​|0⟩\displaystyle W\_{\hat{H}}(\mathcal{A}^{\mathrm{ind}}\_{\mathbf{X}}\otimes\mathcal{I})|0\rangle^{n}\dots|0\rangle^{n}|0\rangle | =∑j=02N​n−1find​(𝐱j)​H^​(𝐱j)​|x1⟩n​…​|xN⟩n​|1⟩\displaystyle=\sum\_{j=0}^{2^{Nn}-1}\sqrt{f^{\mathrm{ind}}(\mathbf{x}\_{j})\hat{H}(\mathbf{x}\_{j})}\,|x\_{1}\rangle^{n}\dots|x\_{N}\rangle^{n}|1\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑j=02N​n−1(1−find(𝐱j)H^(𝐱j)​|x1⟩n​…​|xN⟩n​|0⟩.\displaystyle+\sum\_{j=0}^{2^{Nn}-1}\sqrt{(1-f^{\mathrm{ind}}(\mathbf{x}\_{j})\hat{H}(\mathbf{x}\_{j})}\,|x\_{1}\rangle^{n}\dots|x\_{N}\rangle^{n}|0\rangle. |  |

As before, let us denote by 𝒰Vind:=WH^​(𝒜𝐗ind⊗ℐ)\mathcal{U}\_{V^{\mathrm{ind}}}:=W\_{\hat{H}}(\mathcal{A}^{\mathrm{ind}}\_{\mathbf{X}}\otimes\mathcal{I}) to fit the previous quantum state construction into the QAMC description from Section [3.2.1](https://arxiv.org/html/2601.04049v1#S3.SS2.SSS1 "3.2.1 Quantum Accelerated Monte Carlo techniques ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"). Note that this formulation allows to use, when available, the exact real density functions to define the independent joint density findf^{\mathrm{ind}}.

The following theorem is on the accuracy and complexity of the pricing algorithm following the independent approach.

###### Theorem 3.5 (Quantum complexity estimating the option price from independent marginals).

Let ϱc,ϵc∈(0,1)\varrho\_{c},\epsilon\_{c}\in(0,1). Let c:[0,1]N→ℝc:[0,1]^{N}\to\mathbb{R} be the
density of a copula and suppose that there exists cmax′∈ℝc^{\prime}\_{\max}\in\mathbb{R} such that, for any i=1,…,Ni=1,\ldots,N and any u∈[0,1]Nu\in[0,1]^{N},

|  |  |  |  |
| --- | --- | --- | --- |
|  | |∂∂ui​c​(u1,…,uN)|≤cmax′.\left|\frac{\partial}{\partial u\_{i}}c(u\_{1},\ldots,u\_{N})\right|\leq c^{\prime}\_{\max}. |  | (35) |

Let X1,…,XNX\_{1},\ldots,X\_{N} be real-valued random variables and suppose
that all the assumptions in Theorem [3.4](https://arxiv.org/html/2601.04049v1#S3.Thmtheorem4 "Theorem 3.4 (Quantum complexity recovering the marginal distributions). ‣ Quantum estimation of the marginal distributions ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline") are satisfied for every XiX\_{i}. Suppose that we have access to the rotation oracle WH^W\_{\hat{H}} for any function in the form of ([32](https://arxiv.org/html/2601.04049v1#S3.E32 "In Quantum estimation of the multidimensional option price ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) with h:ℝN→[0,1]h:\mathbb{R}^{N}\to[0,1]. Then, with probability at least 1−ϱc1-\varrho\_{c}, a QAMC algorithm outputs an ϵc\epsilon\_{c}-approximation of 𝔼​[h​(𝐗)]\mathbb{E}[h(\mathbf{X})], querying WγkW\_{\gamma\_{k}}

|  |  |  |  |
| --- | --- | --- | --- |
|  | O​(N2​cmax′​Imax​𝒦max2ϵc​log⁡(N​𝒦maxϱc))O\left(\frac{N^{2}c^{\prime}\_{\max}\sqrt{I\_{\max}}\mathcal{K}\_{\max}^{2}}{\epsilon\_{c}}\log\!\left(\frac{N\mathcal{K}\_{\max}}{\varrho\_{c}}\right)\right) |  | (36) |

times, WH^W\_{\hat{H}}

|  |  |  |  |
| --- | --- | --- | --- |
|  | O​(cmaxϵc​log⁡(1ϱc))O\!\left(\frac{c\_{\max}}{\epsilon\_{c}}\log\!\left(\frac{1}{\varrho\_{c}}\right)\right) |  | (37) |

times, and 𝒜Xi\mathcal{A}\_{X\_{i}}

|  |  |  |  |
| --- | --- | --- | --- |
|  | O​(N2​cmax′​Imax​𝒦max2ϵc​log⁡(N​𝒦maxϱc)+N​cmaxϵc​log⁡(1ϱc))O\!\left(\frac{N^{2}c^{\prime}\_{\max}I\_{\max}\mathcal{K}\_{\max}^{2}}{\epsilon\_{c}}\log\!\left(\frac{N\mathcal{K}\_{\max}}{\varrho\_{c}}\right)+\frac{Nc\_{\max}}{\epsilon\_{c}}\log\!\left(\frac{1}{\varrho\_{c}}\right)\right) |  | (38) |

times, where Imax:=maxi=1,…,N⁡(bi−ai)I\_{\max}:=\max\_{i=1,\ldots,N}(b\_{i}-a\_{i})
and 𝒦max:=maxi=1,…,N⁡𝒦i\mathcal{K}\_{\max}:=\max\_{i=1,\ldots,N}\mathcal{K}\_{i}.

###### Proof.

By applying Theorem [3.4](https://arxiv.org/html/2601.04049v1#S3.Thmtheorem4 "Theorem 3.4 (Quantum complexity recovering the marginal distributions). ‣ Quantum estimation of the marginal distributions ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline") to each XiX\_{i} with ϵi=ϵc2​N​cmax′\epsilon\_{i}=\frac{\epsilon\_{c}}{2Nc^{\prime}\_{\max}} and ϱi=ϱc2​N\varrho\_{i}=\frac{\varrho\_{c}}{2N}, each estimator F^i\hat{F}\_{i} satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∀x∈ℝ,|F^i​(x)−Fi​(x)|≤ϵc2​N​cmax′\forall x\in\mathbb{R},\qquad\bigl|\hat{F}\_{i}(x)-F\_{i}(x)\bigr|\leq\frac{\epsilon\_{c}}{2Nc^{\prime}\_{\max}} |  | (39) |

with probability at least 1−ϱc2​N1-\frac{\varrho\_{c}}{2N}. For any 𝐱∈ℝN\mathbf{x}\in\mathbb{R}^{N}, using Taylor’s theorem with ([35](https://arxiv.org/html/2601.04049v1#S3.E35 "In Theorem 3.5 (Quantum complexity estimating the option price from independent marginals). ‣ Quantum estimation of the multidimensional option price ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | |H^​(𝐱)−H​(𝐱)|\displaystyle\left|\hat{H}(\mathbf{x})-H(\mathbf{x})\right| | =h​(𝐱)cmax​|c​(F^1​(x1),…,F^N​(xN))−c​(F1​(x1),…,FN​(xN))|\displaystyle=\frac{h(\mathbf{x})}{c\_{\max}}\,\left|\,c\!\left(\hat{F}\_{1}(x\_{1}),\dots,\hat{F}\_{N}(x\_{N})\right)-c\!\left(F\_{1}(x\_{1}),\dots,F\_{N}(x\_{N})\right)\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤cmax′​h​(x)cmax​∑i=1N|F^i​(xi)−Fi​(xi)|\displaystyle\leq\frac{c^{\prime}\_{\max}h(x)}{c\_{\max}}\sum\_{i=1}^{N}\left|\hat{F}\_{i}(x\_{i})-F\_{i}(x\_{i})\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤ϵc2​cmax.\displaystyle\leq\frac{\epsilon\_{c}}{2c\_{\max}}. |  |

We then have

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |𝔼ind​[H^​(𝐗)]−𝔼ind​[H​(𝐗)]|\displaystyle\left|\mathbb{E}^{\mathrm{ind}}[\hat{H}(\mathbf{X})]-\mathbb{E}^{\mathrm{ind}}[H(\mathbf{X})]\right| | =|∑j=02N​n−1(H^​(𝐱j)−H​(𝐱j))​find​(𝐱j)|\displaystyle=\left|\sum\_{j=0}^{2^{Nn}-1}\left(\hat{H}(\mathbf{x}\_{j})-H(\mathbf{x}\_{j})\right)f^{\mathrm{ind}}(\mathbf{x}\_{j})\right| |  | (40) |
|  |  | ≤∑j=02N​n−1|H^​(𝐱j)−H​(𝐱j)|​find​(𝐱j)\displaystyle\leq\sum\_{j=0}^{2^{Nn}-1}\left|\hat{H}(\mathbf{x}\_{j})-H(\mathbf{x}\_{j})\right|f^{\mathrm{ind}}(\mathbf{x}\_{j}) |  |
|  |  | ≤ϵc2​cmax,\displaystyle\leq\frac{\epsilon\_{c}}{2c\_{\max}}, |  |

where, again, N​nNn denotes the number of qubits employed for the QAMC estimation as described in Section [3.2.1](https://arxiv.org/html/2601.04049v1#S3.SS2.SSS1 "3.2.1 Quantum Accelerated Monte Carlo techniques ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline") and, recalling that find​(𝐱)=∏i=1Nfi​(xi)f^{\mathrm{ind}}(\mathbf{x})=\prod\_{i=1}^{N}f\_{i}(x\_{i}).

On the other hand, the QAE in Theorem [3.3](https://arxiv.org/html/2601.04049v1#S3.Thmtheorem3 "Theorem 3.3 (Quantum Amplitude Estimation; Theorem 2.3 in [33]). ‣ 3.2.2 Quantum advantage: theoretical results ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline") with parameters ϵ=ϵc2​cmax\epsilon=\frac{\epsilon\_{c}}{2c\_{\max}} and ϱ=ϱc2\varrho=\frac{\varrho\_{c}}{2} outputs
𝔼^ind​[H^​(𝐗)]\widehat{\mathbb{E}}^{\mathrm{ind}}[\hat{H}(\mathbf{X})] such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |𝔼^ind​[H^​(𝐗)]−𝔼ind​[H^​(𝐗)]|≤ϵc2​cmax\left|\widehat{\mathbb{E}}^{\mathrm{ind}}[\hat{H}(\mathbf{X})]-\mathbb{E}^{\mathrm{ind}}[\hat{H}(\mathbf{X})]\right|\leq\frac{\epsilon\_{c}}{2c\_{\max}} |  | (41) |

with probability at least 1−ϱc21-\frac{\varrho\_{c}}{2}.

Combining ([40](https://arxiv.org/html/2601.04049v1#S3.E40 "In Proof. ‣ Quantum estimation of the multidimensional option price ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) and ([41](https://arxiv.org/html/2601.04049v1#S3.E41 "In Proof. ‣ Quantum estimation of the multidimensional option price ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")), we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | |cmax​𝔼^ind​[H^​(𝐗)]−𝔼X​[h​(𝐗)]|\displaystyle\left|c\_{\max}\,\hat{\mathbb{E}}^{\mathrm{ind}}[\hat{H}(\mathbf{X})]-\mathbb{E}\_{X}[h(\mathbf{X})]\right| | ≤cmax​(|𝔼^ind​[H^​(𝐗)]−𝔼ind​[H^​(𝐗)]|+|𝔼ind​[H^​(𝐗)]−𝔼ind​[H​(𝐗)]|)\displaystyle\leq c\_{\max}\left(\left|\hat{\mathbb{E}}^{\mathrm{ind}}[\hat{H}(\mathbf{X})]-\mathbb{E}^{\mathrm{ind}}[\hat{H}(\mathbf{X})]\right|+\left|\mathbb{E}^{\mathrm{ind}}[\hat{H}(\mathbf{X})]-\mathbb{E}^{\mathrm{ind}}[H(\mathbf{X})]\right|\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤ϵc.\displaystyle\leq\epsilon\_{c}. |  |

This holds if every F^i\hat{F}\_{i} satisfies ([39](https://arxiv.org/html/2601.04049v1#S3.E39 "In Proof. ‣ Quantum estimation of the multidimensional option price ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) and ([41](https://arxiv.org/html/2601.04049v1#S3.E41 "In Proof. ‣ Quantum estimation of the multidimensional option price ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")), whose
probability is at least

|  |  |  |
| --- | --- | --- |
|  | (1−ϱc2​N)N​(1−ϱc2)≥ 1−ϱc,\left(1-\frac{\varrho\_{c}}{2N}\right)^{N}\left(1-\frac{\varrho\_{c}}{2}\right)\;\geq\;1-\varrho\_{c}, |  |

by using successively the inequality (1−x)p≥1−p​x(1-x)^{p}\geq 1-px for x∈[0,1]x\in[0,1] and integer p∈ℕp\in\mathbb{N}.

Lastly, let us evaluate the query complexity of the algorithm. In estimating each F^i\hat{F}\_{i}, 𝒜Xi\mathcal{A}\_{X\_{i}} and {Wγk}k\{W\_{\gamma\_{k}}\}\_{k} are queried

|  |  |  |
| --- | --- | --- |
|  | O​(N​cmax′​bi−ai​𝒦i2ϵc​log⁡(N​𝒦iϱc))O\!\left(\frac{Nc^{\prime}\_{\max}\sqrt{b\_{i}-a\_{i}}\mathcal{K}\_{i}^{2}}{\epsilon\_{c}}\log\!\left(\frac{N\mathcal{K}\_{i}}{\varrho\_{c}}\right)\right) |  |

times, and, in estimating all of F^1,…,F^d\hat{F}\_{1},\ldots,\hat{F}\_{d}, this is multiplied by NN. In the estimate ([41](https://arxiv.org/html/2601.04049v1#S3.E41 "In Proof. ‣ Quantum estimation of the multidimensional option price ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")), an oracle 𝒜𝐗ind\mathcal{A}^{\mathrm{ind}}\_{\mathbf{X}} loading findf^{\mathrm{ind}} and WH^W\_{\hat{H}} are called the numbers of times of order ([37](https://arxiv.org/html/2601.04049v1#S3.E37 "In Theorem 3.5 (Quantum complexity estimating the option price from independent marginals). ‣ Quantum estimation of the multidimensional option price ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")). In 𝒜𝐗ind\mathcal{A}^{\mathrm{ind}}\_{\mathbf{X}}, the oracles 𝒜X1,…,𝒜XN\mathcal{A}\_{X\_{1}},\ldots,\mathcal{A}\_{X\_{N}} are called once each, and NN times in total. Combining these observations, we reach the query number bounds in ([36](https://arxiv.org/html/2601.04049v1#S3.E36 "In Theorem 3.5 (Quantum complexity estimating the option price from independent marginals). ‣ Quantum estimation of the multidimensional option price ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")), ([37](https://arxiv.org/html/2601.04049v1#S3.E37 "In Theorem 3.5 (Quantum complexity estimating the option price from independent marginals). ‣ Quantum estimation of the multidimensional option price ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")), and ([38](https://arxiv.org/html/2601.04049v1#S3.E38 "In Theorem 3.5 (Quantum complexity estimating the option price from independent marginals). ‣ Quantum estimation of the multidimensional option price ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")).

∎

### 3.3 Experimental results

In this section, the performance of the proposed quantum-based methodology is experimentally tested, specifically when applied to estimate the expectations for, on the one hand, the coefficients of the cosine series expansions of the marginal densities (see ([11](https://arxiv.org/html/2601.04049v1#S3.E11 "In 3.1.2 Cosine-series density (and distribution) estimation ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"))), and, on the other hand, the final multidimensional option price (see ([5](https://arxiv.org/html/2601.04049v1#S3.E5 "In 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) or ([8](https://arxiv.org/html/2601.04049v1#S3.E8 "In Multidimensional option valuation with copulas ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"))). We will compare the precision convergence patterns of both the CMC estimator given by ([15](https://arxiv.org/html/2601.04049v1#S3.E15 "In 3.2.1 Quantum Accelerated Monte Carlo techniques ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) and the analogous QAMC, resulting after applying QAE algorithms to the states of the form ([17](https://arxiv.org/html/2601.04049v1#S3.E17 "In 3.2.1 Quantum Accelerated Monte Carlo techniques ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")). To that end, given a prescribed accuracy, the number of samples LL for CMC and the number of queries to the quantum oracle 𝒰y,y∈{ak,V,Vind}\mathcal{U}\_{y},\;y\in\{a\_{k},V,V^{\mathrm{ind}}\} for QAMC are reported. Moreover, since these techniques intrinsically present a random nature, each estimation experiment is repeated 252^{5} times, such that we can then provide statistics like the averages or confidence intervals.

As marginals, we consider the NIG distributions fitted to the market quotes of Credit Agricole, Axa and Michelin (see Section [2.4](https://arxiv.org/html/2601.04049v1#S2.SS4 "2.4 Calibration methodology and practical implementation ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")). The employed calibrated parameters are reported in Figures [1](https://arxiv.org/html/2601.04049v1#S2.F1 "Figure 1 ‣ 2.4.5 Calibration outcomes ‣ 2.4 Calibration methodology and practical implementation ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"), [2](https://arxiv.org/html/2601.04049v1#S2.F2 "Figure 2 ‣ 2.4.5 Calibration outcomes ‣ 2.4 Calibration methodology and practical implementation ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"), and [3](https://arxiv.org/html/2601.04049v1#S2.F3 "Figure 3 ‣ 2.4.5 Calibration outcomes ‣ 2.4 Calibration methodology and practical implementation ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"), for Credit Agricole, Axa, and Michelin, respectively. The remaining market data has been extracted from Euronext as explained in Section [2.4.1](https://arxiv.org/html/2601.04049v1#S2.SS4.SSS1 "2.4.1 Market data ‣ 2.4 Calibration methodology and practical implementation ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").

All the experiments have been conducted in a system with processor Intel Core Ultra 9 285H and RAM of 64 GB. The codes are implemented in Python 3.10, and employing the NEASQC: Financial Applications Library [[16](https://arxiv.org/html/2601.04049v1#bib.bib24 "NEASQC: Financial Applications")] under the quantum package myQLM 1.12.2. The quantum simulator relies on C-based linear algebra libraries, becoming an ideal444It does not include system noise, qubit coherence times, etc. simulator. As QAE routines, we employ the modified versions of the Real Quantum Amplitude Estimation proposed in [[32](https://arxiv.org/html/2601.04049v1#bib.bib25 "Real quantum amplitude estimation"), [31](https://arxiv.org/html/2601.04049v1#bib.bib26 "Alternative pipeline for option pricing using quantum computers")] to compute the cosine series coefficients (where the sign of the quantity is relevant) and the Iterative Quantum Amplitude Estimation from [[22](https://arxiv.org/html/2601.04049v1#bib.bib28 "Iterative quantum amplitude estimation"), [17](https://arxiv.org/html/2601.04049v1#bib.bib27 "Modified iterative quantum amplitude estimation is asymptotically optimal")] for the estimation of the option price (assumed positive). Both quantum algorithms come along with rigorous theoretical analysis in terms of error convergence, strictly complying with the order stated in Theorem [3.3](https://arxiv.org/html/2601.04049v1#S3.Thmtheorem3 "Theorem 3.3 (Quantum Amplitude Estimation; Theorem 2.3 in [33]). ‣ 3.2.2 Quantum advantage: theoretical results ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").

#### 3.3.1 Convergence in estimating the density cosine expansion coefficients

In the first experiment, the precision convergence in number of samples and oracle queries for the CMC and QAMC estimators, respectively, is analysed, when applied to recover the calibrated NIG density555We consider the NIG component of the exponential NIG model, so the densities depicted here correspond to expression ([3](https://arxiv.org/html/2601.04049v1#S2.E3 "In 2.3 The exponential NIG model ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")). corresponding to AXA. For that, the error between the approximated coefficients and a reference value (given by the Riemann quadrature in ([16](https://arxiv.org/html/2601.04049v1#S3.E16 "In 3.2.1 Quantum Accelerated Monte Carlo techniques ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")) computed classically) is considered. The number of discrete points in the quadrature is set to J=25J=2^{5}, which corresponds to n=5n=5 qubits employed for the QAMC method. In Figure [4](https://arxiv.org/html/2601.04049v1#S3.F4 "Figure 4 ‣ 3.3.1 Convergence in estimating the density cosine expansion coefficients ‣ 3.3 Experimental results ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"), the obtained results are shown, taking 𝒦=24\mathcal{K}=2^{4}. In the left panel, the error convergence lines for the first four (out of sixteen) relevant coefficients (excluding the coefficient a0a\_{0} which presents exact solution) are depicted as the average of experiment trials. In the right panel, the average error for all the coefficients (jointly with the 90%90\% confidence intervals over the repetitions) are represented. We observe that the CMC estimator deteriorates for higher index coefficients (those with smaller magnitude), while QAMC does not suffer from this issue, due to the natural intrinsic normalization of the amplitudes in a quantum state. All in all, the global expected behaviour is achieved, with QAMC providing a consistent quadratic advantage with respect to CMC.

![Refer to caption](x4.png)


(a)

![Refer to caption](x5.png)


(b)

Figure 4: Convergence in accuracy estimating aka\_{k} by CMC and QAMC.

Further, Figure [5](https://arxiv.org/html/2601.04049v1#S3.F5 "Figure 5 ‣ 3.3.1 Convergence in estimating the density cosine expansion coefficients ‣ 3.3 Experimental results ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline") shows the recovered density and distribution functions for an increasing number of expansion terms 𝒦\mathcal{K} whose coefficients are computed by using the CMC and the QAMC methods with the same number of samples/queries (∼5000\sim 5000). As we can see, both methods perform very similarly, practically indistinguishably, for lower 𝒦\mathcal{K}s, while, in the case of larger number of terms, the QAMC-based estimations outperform those given by the CMC equivalent. Note as well that, as expected, when 𝒦\mathcal{K} increases, the global estimations improve.

![Refer to caption](x6.png)


(a)

![Refer to caption](x7.png)


(b)

![Refer to caption](x8.png)


(c)

![Refer to caption](x9.png)


(d)

![Refer to caption](x10.png)


(e)

![Refer to caption](x11.png)


(f)

Figure 5: NIG density and distribution functions for AXA, estimated by CMC and QAMC varying 𝒦\mathcal{K}.

#### 3.3.2 Convergence in estimating the option price

Next, we assess the performance of the QAMC estimator in solving the final multidimensional option valuation problem by comparing it, as in the previous experiment, against the CMC estimator in terms of error convergence in samples/queries. We consider two pricing problems (see Section [3.1](https://arxiv.org/html/2601.04049v1#S3.SS1 "3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline")):

1. 1.

   Spread 1-year expiry call option with AXA and Michelin as underlying assets. The strike is set to and K=0K=0 and we model the joint distribution by a Gaussian copula with correlation matrix

   |  |  |  |
   | --- | --- | --- |
   |  | Σ=(1−0.25−0.251).\Sigma=\begin{pmatrix}1&-0.25\\ -0.25&1\end{pmatrix}. |  |
2. 2.

   Arithmetic basket 1-year expiry call option with AXA, Credit Agricole and Michelin as underlying assets. The strike is set to K=25K=25 and we model the joint distribution by a Gaussian copula with correlation matrix

   |  |  |  |
   | --- | --- | --- |
   |  | Σ=(1−0.2−0.25−0.21−0.15−0.25−0.151).\Sigma=\begin{pmatrix}1&-0.2&-0.25\\ -0.2&1&-0.15\\ -0.25&-0.15&1\end{pmatrix}. |  |

Again, the accuracy in the estimation is measured against a reference price obtained via a classically computed Riemann sum. Due to the extremely high computational demand of the considered quantum simulator, we adapt the number of employed discrete points to the dimensionality of the problem at hand. Then, for the spread option, we choose J=23J=2^{3} points in each space direction (N=2N=2), while, in the case of the arithmetic basket option valuation, we select J=22J=2^{2} discrete points per dimension (N=3N=3). This then entails that, in both cases, we employ a total of N​n=6Nn=6 qubits to apply the QAMC technique. In order to isolate the error due to the computation of the final price, the marginal densities are recovered with 𝒦=27\mathcal{K}=2^{7} cosine series coefficients, computed classically (so no quantum-related approximation error arises from them). In Figure [6](https://arxiv.org/html/2601.04049v1#S3.F6 "Figure 6 ‣ 3.3.2 Convergence in estimating the option price ‣ 3.3 Experimental results ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"), the accuracy convergence results for CMC and QAMC estimators (utilising both joint and independent formulations) are presented for spread call and arithmetic basket call options in the left and right panels, respectively. Again, we show the average estimation among several repetitions, as well as the 90%90\% confidence interval.

![Refer to caption](x12.png)


(a)

![Refer to caption](x13.png)


(b)

Figure 6: Convergence in accuracy estimating the multidimensional option price.

We can extract the following insights from the pricing experiments:

* •

  Both CMC and QAMC algorithms converge at their theoretical orders, namely, 1/ϵ21/\epsilon^{2} and 1/ϵ1/\epsilon, respectively, which, again, empirically demonstrates the quadratic improvement provided by the QAMC-based solutions as alternatives to the CMC versions in multidimensional option pricing.
* •

  Although keeping the order of convergence, for this specific valuation problem, the QAMC relying on the joint formulation significantly outperforms the independent analogous, showing a lower intercept in terms of the number of queries.
* •

  The CMC convergence even deteriorates for larger number of samples, suggesting that it might be saturating.
* •

  In practical terms, when high accuracy is required (below 10−310^{-3}), QAMC needs 10−10010-100 fewer samples/queries than CMC, to achieve a prescribed precision.

## 4 Conclusions

This work presents a comprehensive framework for multi-asset option pricing that integrates market-consistent modelling with quantum-accelerated computation. By calibrating NIG marginals to real option quotes and coupling them through a Gaussian copula, we construct arbitrage-free joint distributions capable of capturing skewness and fat tails observed in equity markets. The proposed calibration procedure, supported by theoretical guarantees of existence and continuity, achieves high accuracy with minimal pricing errors across multiple assets.

On the computational front, we demonstrate that QAMC methods, based on QAE, deliver the expected quadratic improvement in convergence compared to CMC. Empirical experiments confirm that QAMC requires significantly fewer queries (by one to two orders of magnitude) for comparable precision, particularly in high-dimensional settings. These results validate the practical feasibility of quantum algorithms for complex derivative pricing and highlight their potential to overcome scalability limitations inherent in classical approaches.

Beyond immediate performance gains, this work underscores the importance of combining arbitrage-aware modelling with quantum techniques to ensure both financial soundness and computational efficiency. Future research should explore richer dependence structures beyond Gaussian copulas, extend the pipeline to path-dependent payoffs, and investigate hardware implementations to assess real-world resource constraints. By bridging rigorous market modelling and quantum computing, this study contributes a foundational step toward deployable quantum solutions in quantitative finance.

## Acknowledgements

Both authors thank the Euronext data support team for their kind assistance in providing and clarifying the option data used in our analysis.

Á. Leitao acknowledges the funding from the Ministry of Science and Innovation of Spain through the Ramón y Cajal 2022 grant and the program with reference PID2022-141058OB-I00, and from the Department of Education, Science, Universities, and Vocational Training of the Xunta de Galicia through the programs with references ED451C 2022/047 and ED431F 2025/032, as well as the support from CITIC, as a centre accredited for excellence within the Galician University System and a member of the CIGUS Network, receiving subsidies from the Department of Education, Science, Universities, and Vocational Training of the Xunta de Galicia. Additionally, it is co-financed by the EU through the FEDER Galicia 2021-27 operational program (ref. ED451G 2023/01).

## References

* [1]
  F. Alonso, Á. Leitao, and C. Vázquez (2025)
  Quantum machine learning methods for Fourier-based distribution estimation with application in option pricing.
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p4.1 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [2]
  J. Andreasen and B. Huge (2011)
  Volatility interpolation.
  Risk Magazine,  pp. 76–79.
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p3.1 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"),
  [3rd item](https://arxiv.org/html/2601.04049v1#S2.I1.i3.p1.1 "In 2.2 Fitting and interpolation methods ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [3]
  J. P. Boyd (2001)
  Chebyshev and fourier spectral methods.
   Dover.
  Cited by: [Remark](https://arxiv.org/html/2601.04049v1#Thmremarkx4.p1.2.2 "Remark. ‣ 3.1.2 Cosine-series density (and distribution) estimation ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [4]
  G. Brassard, P. Høyer, M. Mosca, and A. Tapp (2002)
  Quantum amplitud amplification and estimation.
  In Quantum Computation and Information, S. J. L. Jr and H. E. Brandt (Eds.),
  Contemporary Mathematics, Vol. 305,  pp. 53–74.
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p2.2 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"),
  [§3.2.1](https://arxiv.org/html/2601.04049v1#S3.SS2.SSS1.p7.3 "3.2.1 Quantum Accelerated Monte Carlo techniques ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [5]
  D. T. Breeden and R. H. Litzenberger (1978)
  Prices of state-contingent claims implicit in option prices.
  Journal of Business 51 (4),  pp. 621–651.
  Cited by: [§2.1](https://arxiv.org/html/2601.04049v1#S2.SS1.p3.1 "2.1 Market European call and put options prices ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [6]
  P. Carr and D. B. Madan (1999)
  Option valuation using the fast fourier transform.
  2 (4),  pp. 61–73.
  External Links: [Document](https://dx.doi.org/10.21314/JCF.1999.043)
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p2.2 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [7]
  A. Carrera Vazquez and S. Woerner (2021)
  Efficient state preparation for quantum amplitude estimation.
  Physical Review Applied 15 (3),  pp. 034027.
  External Links: [Document](https://dx.doi.org/10.1103/PhysRevApplied.15.034027)
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p4.1 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"),
  [§3.2.1](https://arxiv.org/html/2601.04049v1#S3.SS2.SSS1.p6.7 "3.2.1 Quantum Accelerated Monte Carlo techniques ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [8]
  U. Cherubini, E. Luciano, and W. Vecchiato (2004)
  Copula methods in finance.
  1st edition, Wiley Finance Series, John Wiley & Sons, Hoboken, NJ.
  External Links: ISBN 978-0-470-86344-2,
  [Document](https://dx.doi.org/10.1002/9781118673331)
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p2.2 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [9]
  R. Cont, P. Tankov, and E. Voltchkova (2004)
  Option pricing models with jumps: integro‐differential equations and inverse problems.
  In European Congress on Computational Methods in Applied Sciences and Engineering (ECCOMAS), P. Neittänmäki, T. Rossi, S. Korotov, E. Oñate, J. Périaux, and D. Knörzer (Eds.),
  Jyväskylä, Finland.
  Cited by: [Remark](https://arxiv.org/html/2601.04049v1#Thmremarkx2.p1.4.4 "Remark (Stability and sensitivity). ‣ 2.3.1 NIG model calibration ‣ 2.3 The exponential NIG model ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [10]
  R. Cont and P. Tankov (2004)
  Financial modelling with jump processes.
  Financial Mathematics Series, Chapman and Hall/CRC.
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p3.1 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"),
  [§2.4.4](https://arxiv.org/html/2601.04049v1#S2.SS4.SSS4.p3.2 "2.4.4 Calibration methodology ‣ 2.4 Calibration methodology and practical implementation ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"),
  [Remark](https://arxiv.org/html/2601.04049v1#Thmremarkx2.p1.4.4 "Remark (Stability and sensitivity). ‣ 2.3.1 NIG model calibration ‣ 2.3 The exponential NIG model ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [11]
  S. Crépey (2003)
  Calibration of the local volatility in a generalized black–scholes model using tikhonov regularization.
  SIAM Journal on Mathematical Analysis 34 (5),  pp. 1183–1206.
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p3.1 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"),
  [Remark](https://arxiv.org/html/2601.04049v1#Thmremarkx2.p1.4.4 "Remark (Stability and sensitivity). ‣ 2.3.1 NIG model calibration ‣ 2.3 The exponential NIG model ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [12]
  H. de March and P. Henry-Labordère (2019)
  Building arbitrage-free implied volatility: sinkhorn’s algorithm and variants.
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p3.1 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"),
  [4th item](https://arxiv.org/html/2601.04049v1#S2.I1.i4.p1.1 "In 2.2 Fitting and interpolation methods ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"),
  [§2.2](https://arxiv.org/html/2601.04049v1#S2.SS2.p2.1 "2.2 Fitting and interpolation methods ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [13]
  A. Eriksson, E. Ghysels, and F. Wang (2009)
  The normal inverse gaussian distribution and the pricing of derivatives.
  The Journal of Derivatives 16 (3),  pp. 23–37.
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p2.2 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"),
  [4th item](https://arxiv.org/html/2601.04049v1#S2.I3.i4.p1.1 "In 2.3 The exponential NIG model ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [14]
  F. Fang and C. W. Oosterlee (2008)
  A novel pricing method for european options based on fourier–cosine series expansions.
  SIAM Journal on Scientific Computing 31 (2),  pp. 826–848.
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p2.2 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"),
  [§3.1.2](https://arxiv.org/html/2601.04049v1#S3.SS1.SSS2.p2.4 "3.1.2 Cosine-series density (and distribution) estimation ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"),
  [Remark](https://arxiv.org/html/2601.04049v1#Thmremarkx4.p1.2.2 "Remark. ‣ 3.1.2 Cosine-series density (and distribution) estimation ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [15]
  J. L. Fernández, A. M. Ferreiro, J. A. García-Rodríguez, Á. Leitao, J. G. López-Salas, and C. Vázquez (2013)
  Static and dynamic SABR stochastic volatility models: calibration and option pricing using GPUs.
  94,  pp. 55–75.
  External Links: [Document](https://dx.doi.org/10.1016/j.matcom.2013.05.007)
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p3.1 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [16]
  G. Ferro and A. Manzano (2024)
  NEASQC: Financial Applications.
   GitHub.
  External Links: [Link](https://github.com/NEASQC/FinancialApplications)
  Cited by: [§3.3](https://arxiv.org/html/2601.04049v1#S3.SS3.p3.1 "3.3 Experimental results ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [17]
  S. Fukuzawa, C. Ho, S. Irani, and J. Zion (2023-01)
  Modified iterative quantum amplitude estimation is asymptotically optimal.
  In 2023 Proceedings of the Symposium on Algorithm Engineering and Experiments (ALENEX),
   pp. 135–147.
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p4.1 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"),
  [§3.3](https://arxiv.org/html/2601.04049v1#S3.SS3.p3.1 "3.3 Experimental results ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [18]
  J. Gatheral and A. Jacquier (2014)
  Arbitrage-free SVI volatility surfaces.
  Quantitative Finance 14 (1),  pp. 59–71.
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p3.1 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"),
  [1st item](https://arxiv.org/html/2601.04049v1#S2.I1.i1.p1.1 "In 2.2 Fitting and interpolation methods ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [19]
  J. Gatheral (2004)
  A parsimonious arbitrage-free implied volatility parameterization with application to the valuation of volatility derivatives.
  In Global Derivatives Conference,
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p3.1 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"),
  [1st item](https://arxiv.org/html/2601.04049v1#S2.I1.i1.p1.1 "In 2.2 Fitting and interpolation methods ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [20]
  P. Glassermann (2004)
  Monte Carlo methods in financial engineering.
   Springer.
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p2.2 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"),
  [§3.2.1](https://arxiv.org/html/2601.04049v1#S3.SS2.SSS1.p1.1 "3.2.1 Quantum Accelerated Monte Carlo techniques ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [21]
  A. Gómez, Á. Leitao, A. P. Manzano, M. R. Nogueiras, G. Ordóñez, and C. Vázquez (2022)
  A survey on quantum computational finance for derivatives pricing and VaR.
  Archives of Computational Methods in Engineering 9,  pp. 4137–4163.
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p4.1 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"),
  [§3.2.1](https://arxiv.org/html/2601.04049v1#S3.SS2.SSS1.p4.1 "3.2.1 Quantum Accelerated Monte Carlo techniques ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [22]
  D. Grinko, J. Gacon, C. Zoufal, and S. Woerner (2021)
  Iterative quantum amplitude estimation.
  npj Quantum Information 7 (1).
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p4.1 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"),
  [§3.3](https://arxiv.org/html/2601.04049v1#S3.SS3.p3.1 "3.3 Experimental results ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [23]
  L. Grover and T. Rudolph (2002)
  Creating superpositions that correspond to efficiently integrable probability distributions.
  External Links: quant-ph/0208112,
  [Link](https://arxiv.org/abs/quant-ph/0208112)
  Cited by: [§3.2.1](https://arxiv.org/html/2601.04049v1#S3.SS2.SSS1.p6.7 "3.2.1 Quantum Accelerated Monte Carlo techniques ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [24]
  P. Hagan, D. Kumar, A. Lesniewski, and D. Woodward (2002)
  Managing smile risk.
  Wilmott Magazine,  pp. 84–108.
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p3.1 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"),
  [2nd item](https://arxiv.org/html/2601.04049v1#S2.I1.i2.p1.1 "In 2.2 Fitting and interpolation methods ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [25]
  S. L. Heston (1993)
  A closed-form solution for options with stochastic volatility with applications to bond and currency options.
  6 (2),  pp. 327–343.
  External Links: [Document](https://dx.doi.org/10.1093/rfs/6.2.327)
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p3.1 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [26]
  J. Hok and T. L. (. Chan (2017)
  Option pricing with Legendre polynomials.
  322,  pp. 25–45.
  External Links: [Document](https://dx.doi.org/10.1016/j.cam.2017.03.027)
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p2.2 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [27]
  J. Hok and S. Tan (2019)
  Calibration of local volatility model with stochastic interest rates by efficient numerical pde methods.
  42 (2),  pp. 609–637.
  External Links: [Document](https://dx.doi.org/10.1007/s10203-019-00232-3)
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p3.1 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [28]
  Á. Leitao, J. L. Kirkby, and L. Ortiz-Gracia (2021)
  The CTMC–Heston model: calibration and exotic option pricing with SWIFT.
  24 (4),  pp. 71–114.
  External Links: [Document](https://dx.doi.org/10.21314/JCF.2020.398)
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p3.1 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [29]
  A. Lipton and A. Sepp (2011-10)
  Filling the gaps.
  Risk Magazine,  pp. 66–71.
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p3.1 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"),
  [3rd item](https://arxiv.org/html/2601.04049v1#S2.I1.i3.p1.1 "In 2.2 Fitting and interpolation methods ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [30]
  K. Maekawa and K. Kawai (2004-08)
  Option pricing under nig distribution: the empirical analysis of nikkei 225 option.
  Econometric Society 2004 Far Eastern Meetings
  Technical Report 607, Econometric Society.
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p2.2 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"),
  [4th item](https://arxiv.org/html/2601.04049v1#S2.I3.i4.p1.1 "In 2.3 The exponential NIG model ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [31]
  A. P. Manzano, G. Ferro, Á. Leitao, C. Vázquez, and A. Gómez (2025)
  Alternative pipeline for option pricing using quantum computers.
  EPJ Quantum Technology 12.
  Note: 28
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p4.1 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"),
  [§3.3](https://arxiv.org/html/2601.04049v1#S3.SS3.p3.1 "3.3 Experimental results ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [32]
  A. P. Manzano, D. Musso, and Á. Leitao (2023)
  Real quantum amplitude estimation.
  EPJ Quantum Technology 10 (1),  pp. 1–24.
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p4.1 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"),
  [§3.3](https://arxiv.org/html/2601.04049v1#S3.SS3.p3.1 "3.3 Experimental results ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [33]
  A. Montanaro (2015)
  Quantum speedup of monte carlo methods.
  Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences 471 (2181).
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p2.2 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"),
  [§3.2.1](https://arxiv.org/html/2601.04049v1#S3.SS2.SSS1.p4.1 "3.2.1 Quantum Accelerated Monte Carlo techniques ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"),
  [§3.2.1](https://arxiv.org/html/2601.04049v1#S3.SS2.SSS1.p7.3 "3.2.1 Quantum Accelerated Monte Carlo techniques ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"),
  [Theorem 3.3](https://arxiv.org/html/2601.04049v1#S3.Thmtheorem3 "Theorem 3.3 (Quantum Amplitude Estimation; Theorem 2.3 in [33]). ‣ 3.2.2 Quantum advantage: theoretical results ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [34]
  M. Moosa, T. W. Watts, Y. Chen, A. Sarma, and P. L. McMahon (2023)
  Linear-depth quantum circuits for loading Fourier approximations of arbitrary functions.
  Quantum Science and TechnologyQuantum InformationJournal of Computational FinanceJournal of Computational and Applied MathematicsThe Review of Financial StudiesJournal of Computational FinanceMathematics and Computers in SimulationReviews in PhysicsDecisions in Economics and Finance 9 (1),  pp. 015002.
  External Links: [Document](https://dx.doi.org/10.1088/2058-9565/acfc62),
  [Link](https://doi.org/10.1088/2058-9565/acfc62)
  Cited by: [§3.2.1](https://arxiv.org/html/2601.04049v1#S3.SS2.SSS1.p6.7 "3.2.1 Quantum Accelerated Monte Carlo techniques ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [35]
  R. B. Nelsen (2006)
  An introduction to copulas.
  2nd edition, Springer Series in Statistics, Springer.
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p2.2 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"),
  [Theorem 3.1](https://arxiv.org/html/2601.04049v1#S3.Thmtheorem1 "Theorem 3.1 (Sklar’s Theorem [35]). ‣ 3.1.1 Joint distribution via copulas ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [36]
  R. Orús, S. Mugel, and E. Lizaso (2019)
  Quantum computing for finance: overview and prospects.
  4,  pp. 100028.
  External Links: [Document](https://dx.doi.org/10.1016/j.revip.2019.100028)
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p4.1 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [37]
  P. Rebentrost, B. Gupt, and T. R. Bromley (2018)
  Quantum computational finance: Monte Carlo pricing of financial derivatives.
  Physical Review A 98 (2).
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p2.2 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"),
  [§3.2.1](https://arxiv.org/html/2601.04049v1#S3.SS2.SSS1.p4.1 "3.2.1 Quantum Accelerated Monte Carlo techniques ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [38]
  W. Schoutens (2003)
  Lévy processes in finance: pricing financial derivatives.
  1st edition, Wiley Series in Probability and Statistics, John Wiley & Sons, Chichester, West Sussex; New York.
  Note: Volume 534 of the Wiley Series in Probability and Statistics
  External Links: ISBN 0-470-85156-2, 978-0-470-85156-2
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p2.2 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [39]
  N. Stamatopoulos, D. J. Egger, Y. Sun, C. Zoufal, R. Iten, N. Shen, and S. Woerner (2020)
  Option pricing using quantum computers.
  Quantum 4,  pp. 291.
  Cited by: [§1](https://arxiv.org/html/2601.04049v1#S1.p4.1 "1 Introduction ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline"),
  [§3.2.1](https://arxiv.org/html/2601.04049v1#S3.SS2.SSS1.p6.7 "3.2.1 Quantum Accelerated Monte Carlo techniques ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [40]
  B. Tavin (2012-07)
  Implied distribution as a function of the volatility smile.
  Bankers, Markets and Investors 119,  pp. 31–42.
  Cited by: [4th item](https://arxiv.org/html/2601.04049v1#S2.I3.i4.p1.1 "In 2.3 The exponential NIG model ‣ 2 Construction of the market distributions ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [41]
  L. N. Trefethen (2000)
  Spectral methods in matlab.
   SIAM.
  Cited by: [Remark](https://arxiv.org/html/2601.04049v1#Thmremarkx4.p1.2.2 "Remark. ‣ 3.1.2 Cosine-series density (and distribution) estimation ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [42]
  C. Zoufal, A. Lucchi, and S. Woerner (2019)
  Quantum generative adversarial networks for learning and loading random distributions.
  7 (103).
  Cited by: [§3.2.1](https://arxiv.org/html/2601.04049v1#S3.SS2.SSS1.p6.7 "3.2.1 Quantum Accelerated Monte Carlo techniques ‣ 3.2 Quantum algorithm for multidimensional options pricing ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").
* [43]
  A. Zygmund (1959)
  Trigonometric series.
   Cambridge University Press.
  Cited by: [Remark](https://arxiv.org/html/2601.04049v1#Thmremarkx4.p1.2.2 "Remark. ‣ 3.1.2 Cosine-series density (and distribution) estimation ‣ 3.1 Multidimensional option pricing using copulas ‣ 3 Multidimensional option pricing using quantum computing ‣ Quantum computing for multidimensional option pricing: End-to-end pipeline").