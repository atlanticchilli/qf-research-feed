---
authors:
- Pere Diaz-Lozano
- Thomas K. Kloster
doc_id: arxiv:2602.16232v1
family_id: arxiv:2602.16232
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration
url_abs: http://arxiv.org/abs/2602.16232v1
url_html: https://arxiv.org/html/2602.16232v1
venue: arXiv q-fin
version: 1
year: 2026
---


Pere Diaz-Lozano
peredl@math.uio.no
Department of Mathematics, University of Oslo

Thomas K. Kloster
tkk@econ.au.dk
Department of Economics and Business Economics, Aarhus University
CoRE, Center for Research in Energy: Economics and Markets

###### Abstract

Calibration to a surface of option prices requires specifying a suitably flexible martingale model for the discounted asset price under a risk-neutral measure. Assuming Brownian noise and mean-square integrability, we construct an over-parameterized model based on the martingale representation theorem. In particular, we approximate the terminal value of the martingale via a truncated Wiener–chaos expansion and recover the intermediate dynamics by computing the corresponding conditional expectations.
Using the Hermite-polynomial formulation of the Wiener chaos, we obtain easily implementable expressions that enable fast calibration to a target implied-volatility surface.
We illustrate the flexibility and expressive power of the resulting model through numerical experiments on both simulated and real market data.

Keywords: Wiener chaos expansion, calibration of financial models, Monte Carlo methods, martingale modelling

## 1 Introduction

Option pricing models are often assessed by their ability to reproduce observed market implied volatilities of liquidly traded options. Traditionally, models are built bottom-up by specifying risk-neutral dynamics for the underlying price process, aiming for dynamics that are both reasonable and interpretable. Typically, these dynamics are chosen within a parametric family with a small number of economically and statistically meaningful parameters. If the model calibrates well to market prices, it can then be used to compute hedge ratios and to price illiquid or exotic contracts in an arbitrage-free and consistent way. There is a large literature on parametric option pricing models and their relative performance; see, e.g., [Bakshi1997, Eraker2004, AndersenFusariTodorov2015, Romer2022, math11194201] for extensive studies and comparisons.

A more recent approach that has gained considerable popularity is to model the underlying price using highly over-parameterized architectures, where their degrees of freedom are generic and not directly interpretable. Examples include signature-based expansions [Signatures1, Signatures2, Signatures3, see, e.g.,] and neural SDE models [NeuralSDE1, NeuralSDE2, see, e.g,]. These model classes can calibrate well to observed market data across different market regimes, but compared to the parametric approach, it is less clear how their implied dynamics behave and how well they price exotic derivatives.

This work introduces a new over-parameterized martingale model for the discounted asset price process (St)t∈[0,𝒯](S\_{t})\_{t\in[0,\mathcal{T}]}. Let (Ω,ℱ,ℚ,𝔽)(\Omega,\mathcal{F},\mathbb{Q},\mathbb{F}) be a filtered probability space and fix a time horizon 𝒯>0\mathcal{T}>0. We work under a risk-neutral measure ℚ\mathbb{Q}, so that the discounted price process is a (ℚ,𝔽)(\mathbb{Q},\mathbb{F})-martingale. That is, for any t≤𝒯t\leq\mathcal{T},

|  |  |  |  |
| --- | --- | --- | --- |
|  | St=𝔼​[S𝒯∣ℱt].\displaystyle S\_{t}=\mathbb{E}\!\left[S\_{\mathcal{T}}\mid\mathcal{F}\_{t}\right]. |  | (1.1) |

In particular, once S𝒯S\_{\mathcal{T}} is specified, the process on [0,𝒯][0,\mathcal{T}] is determined (up to modification) by ([1.1](https://arxiv.org/html/2602.16232v1#S1.E1 "In 1 Introduction ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration")). Throughout, we assume that 𝔽\mathbb{F} is the natural filtration of a dd-dimensional ℚ\mathbb{Q}-Brownian motion, and that the martingale is square-integrable. In this setting, S𝒯∈L2​(ℱ𝒯)S\_{\mathcal{T}}\in L^{2}(\mathcal{F}\_{\mathcal{T}}) admits a Wiener chaos expansion of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | S𝒯=∑n≥0∑|a|=nda​Φa,da≔a!​⟨Φa,S𝒯⟩L2​(ℱ𝒯),S\_{\mathcal{T}}=\sum\_{n\geq 0}\sum\_{\lvert a\rvert=n}d\_{a}\Phi\_{a},\quad d\_{a}\coloneqq a!\langle\Phi\_{a},S\_{\mathcal{T}}\rangle\_{L^{2}(\mathcal{F}\_{\mathcal{T}})}, |  | (1.2) |

where the sum converges in L2​(ℱ𝒯)L^{2}(\mathcal{F}\_{\mathcal{T}}) and (a!​Φa)a(\sqrt{a!}\Phi\_{a})\_{a} is an orthonormal basis of L2​(ℱ𝒯)L^{2}(\mathcal{F}\_{\mathcal{T}}).
We truncate ([1.2](https://arxiv.org/html/2602.16232v1#S1.E2 "In 1 Introduction ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration")) and derive explicit closed-form expressions for the conditional expectations 𝔼​[Φa∣ℱt]\mathbb{E}[\Phi\_{a}\mid\mathcal{F}\_{t}]. Treating the coefficients (da)a(d\_{a})\_{a} as trainable weights yields a flexible model class which is universal among square-integrable (ℚ,𝔽)(\mathbb{Q},\mathbb{F})-martingales. We call it the *Wiener chaos martingale model*.

Consequently, the proposed class can reproduce price processes generated by Brownian-driven models (e.g., Heston or SABR) arbitrarily well in mean square, as long as these define square-integrable (ℚ,𝔽)(\mathbb{Q},\mathbb{F})-martingales. The same holds for Volterra-type rough-volatility models with a weakly singular kernel in the volatility.

In practice, calibration is performed on market call option prices observed across strikes and maturities. Under the risk-neutral measure ℚ\mathbb{Q}, assuming zero interest rates, the discounted model price of a European call with maturity T≤𝒯T\leq\mathcal{T} and strike KK is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cmodel​(T,K)=𝔼​[(ST−K)+].\displaystyle C^{\mathrm{model}}(T,K)=\mathbb{E}\!\left[(S\_{T}-K)\_{+}\right]. |  | (1.3) |

Given quoted prices {Cmkt​(T,K):(T,K)∈𝐓×𝐊}\{C^{\mathrm{mkt}}(T,K)\,:\,(T,K)\in\mathbf{T}\times\mathbf{K}\}, calibration amounts to fitting the coefficients by minimizing a loss that measures the discrepancy with the corresponding model prices. While ([1.3](https://arxiv.org/html/2602.16232v1#S1.E3 "In 1 Introduction ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration")) is typically evaluated by Monte Carlo, calibration remains efficient and can be carried out in two steps. We first pre-compute samples of the conditional expectations 𝔼​[Φa∣ℱt]\mathbb{E}[\Phi\_{a}\mid\mathcal{F}\_{t}], and then fit (da)a(d\_{a})\_{a} using a gradient-based optimization method.

We conduct an extensive study of the proposed model by calibrating it to option price surfaces generated by established parametric models that can be cast in our framework, namely the Heston and rough Heston models. We find that the model fits the resulting implied volatility surfaces accurately when the driving noise is taken to be a 22-dimensional Brownian motion. To assess whether the over-parameterized model merely overfits, we evaluate out-of-sample quantities, including call prices at maturities not used in calibration and prices of several path-dependent options. In all cases, the Wiener chaos martingale model reproduces these prices with reasonable accuracy, suggesting that the learned dynamics remain economically plausible and useful for pricing and hedging beyond the European option surface. As a final test, we demonstrate that the model also calibrates efficiently and accurately to real SPX option data.

### 1.1 Related Literature

Before proceeding, we briefly comment on previous works that employ chaos expansions for option pricing and hedging.

In [Chaos\_Funahashi], the authors develop a closed-form approximation for European option prices in Markovian diffusion models of the form d​St=St​σ​(St,t)​d​WtdS\_{t}=S\_{t}\,\sigma(S\_{t},t)\,dW\_{t}, where σ\sigma is a deterministic local-volatility function. Their method combines a Wiener chaos expansion with a successive substitution scheme, yielding explicit low-order formulas for the characteristic function of the normalized return, which is then integrated to obtain call prices. They illustrate the approach on parametric local-volatility specifications such as CEV. In [Chaos\_BasketOption], this methodology is extended to multi-asset settings for basket-type payoffs. Our perspective differs in that we do not start from a parametric diffusion and derive an expansion from it; instead, we treat the chaos expansion as the model itself and calibrate the expansion coefficients directly.

In [neufeld2025chaotichedgingiteratedintegrals], the market is taken as given and the goal is to hedge contingent claims, rather than to fit a model to observed option data. Starting from a general exponentially integrable semimartingale SS, the authors show that any contingent claim that is an LpL^{p}-functional of SS can be approximated arbitrarily well by a finite number of terms in the iterated-integral chaos expansion of SS. They then approximate the associated kernels with neural networks and use this representation to solve the LpL^{p} hedging problem.

A paper closer in spirit to our approach is [Chaos\_RiskNeutralDistribution]. There, the marginal distribution of StS\_{t} is modeled via a truncated Wiener chaos expansion in a Hermite basis, and the coefficients are calibrated to option data separately at each maturity. Because calibration is performed independently across maturities, the resulting collection of risk-neutral marginals need not be consistent with a single arbitrage-free price process. In contrast, our framework starts from a single chaos-driven model and derives all maturities from it in a time-consistent and arbitrage-free manner.

### 1.2 Structure of the paper

The paper is organized as follows. Section [2](https://arxiv.org/html/2602.16232v1#S2 "2 Preliminaries ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration") introduces the notation and recalls the main ingredients of Wiener chaos expansions used throughout. Section [3](https://arxiv.org/html/2602.16232v1#S3 "3 The Wiener Chaos Martingale Model ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration") presents the Wiener chaos martingale model and establishes its universality over square-integrable Brownian martingales. In Section [4](https://arxiv.org/html/2602.16232v1#S4 "4 Computation of conditional expectations ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration"), we derive explicit expressions for the conditional expectations of the chaos basis elements, which are then used in the calibration procedure of Section [5](https://arxiv.org/html/2602.16232v1#S5 "5 Calibration procedure ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration"). Section [6](https://arxiv.org/html/2602.16232v1#S6 "6 Numerical experiments ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration") reports numerical experiments, including calibration to synthetic option surfaces generated by standard parametric models and a range of robustness checks. Finally, we fit the model to SPX option data.

## 2 Preliminaries

### 2.1 Definitions and notation

Let 𝒯>0\mathcal{T}>0 be a fixed time horizon, and let B=(Bt)t∈[0,𝒯]B=(B\_{t})\_{t\in[0,\mathcal{T}]} be a dd-dimensional Brownian motion defined on a complete probability space (Ω,ℱ,ℚ)(\Omega,\mathcal{F},\mathbb{Q}). We use the following spaces and notational conventions:

* •

  𝔽=(ℱt)t∈[0,𝒯]\mathbb{F}=(\mathcal{F}\_{t})\_{t\in[0,\mathcal{T}]} is the filtration generated by the Brownian motion BB and augmented with the ℚ\mathbb{Q}-null sets. We assume that ℱ=ℱ𝒯\mathcal{F}=\mathcal{F}\_{\mathcal{T}}.
* •

  𝔼[⋅∣ℱt]\mathbb{E}[\ \cdot\mid\mathcal{F}\_{t}] denotes conditional expectation under ℚ\mathbb{Q}, and 𝔼​[⋅]\mathbb{E}[\cdot] the corresponding expectation.
* •

  Lb​(ℱt)L^{b}(\mathcal{F}\_{t}), t∈[0,𝒯]t\in[0,\mathcal{T}] and b≥1b\geq 1, is the space of all ℱt\mathcal{F}\_{t}-measurable random variables X:Ω→ℝX\colon\Omega\to\mathbb{R} satisfying ∥X∥b≔𝔼​[|X|b]1/b<∞\lVert X\rVert\_{b}\coloneqq\mathbb{E}\![\lvert X\rvert^{b}]^{1/b}<\infty.
* •

  ℳ𝒯2\mathcal{M}\_{\mathcal{T}}^{2} denotes the space of all continuous, real-valued (ℚ,𝔽)(\mathbb{Q},\mathbb{F})-martingales M=(Mt)t∈[0,𝒯]M=(M\_{t})\_{t\in[0,\mathcal{T}]} such that ‖M‖ℳ𝒯≔𝔼​[|M𝒯|2]1/2<∞\|M\|\_{\mathcal{M}\_{\mathcal{T}}}\coloneqq\mathbb{E}\!\left[|M\_{\mathcal{T}}|^{2}\right]^{1/2}<\infty.
* •

  Cp∞​(ℝn×d)C\_{p}^{\infty}(\mathbb{R}^{n\times d}) is the space of smooth functions ϕ:ℝn×d→ℝ\phi:\mathbb{R}^{n\times d}\to\mathbb{R} such that ϕ\phi and all its partial derivatives have polynomial growth.

We also recall some basic definitions related to Malliavin calculus.

* •

  ℍ𝒯=L2​([0,𝒯];ℝd)\mathbb{H}\_{\mathcal{T}}=L^{2}([0,\mathcal{T}];\mathbb{R}^{d}) is the space of functions h:[0,𝒯]→ℝdh\colon[0,\mathcal{T}]\to\mathbb{R}^{d} such that

  |  |  |  |
  | --- | --- | --- |
  |  | ∥h∥𝒯≔(∫0𝒯|h​(s)|2​𝑑s)1/2<∞.\displaystyle\lVert h\rVert\_{\mathcal{T}}\coloneqq\Big(\int\_{0}^{\mathcal{T}}|h(s)|^{2}ds\Big)^{1/2}<\infty. |  |
* •

  For h=(h1,…,hd)∈ℍ𝒯h=(h^{1},\dots,h^{d})\in\mathbb{H}\_{\mathcal{T}}, we define the random vector

  |  |  |  |
  | --- | --- | --- |
  |  | 𝐁​(h)≔(∫0𝒯h1​(s)​𝑑Bs1,…,∫0𝒯hd​(s)​𝑑Bsd).\displaystyle\mathbf{B}(h)\coloneqq\Big(\int\_{0}^{\mathcal{T}}h^{1}(s)dB\_{s}^{1},\dots,\int\_{0}^{\mathcal{T}}h^{d}(s)dB\_{s}^{d}\Big). |  |
* •

  𝒮𝒯\mathcal{S}\_{\mathcal{T}} denotes the class of smooth random variables that are ℱ𝒯\mathcal{F}\_{\mathcal{T}}-measurable, which have the form

  |  |  |  |
  | --- | --- | --- |
  |  | F=ϕ​(𝐁​(h1),…,𝐁​(hn)),\displaystyle F=\phi(\mathbf{B}(h\_{1}),\dots,\mathbf{B}(h\_{n})), |  |

  where the function ϕ​((x11,…,x1d),…,(xn1,…,xnd))\phi((x\_{1}^{1},\dots,x\_{1}^{d}),\dots,(x\_{n}^{1},\dots,x\_{n}^{d})) belongs to Cp∞​(ℝn×d)C\_{p}^{\infty}(\mathbb{R}^{n\times d}), and for all i≤ni\leq n we have hi=(hi1,…,hid)∈ℍ𝒯h\_{i}=(h\_{i}^{1},\dots,h\_{i}^{d})\in\mathbb{H}\_{\mathcal{T}}.
* •

  The Malliavin derivative of a random variable F∈𝒮𝒯F\in\mathcal{S}\_{\mathcal{T}} is defined as the dd-dimensional stochastic process

  |  |  |  |
  | --- | --- | --- |
  |  | Dsj​F=∑i=1n∂ϕ∂xij​(𝐁​(h1),…,𝐁​(hn))​hij​(s),s∈[0,𝒯]j=1,…,d.\displaystyle D\_{s}^{j}F=\sum\_{i=1}^{n}\frac{\partial\phi}{\partial x\_{i}^{j}}\big(\mathbf{B}(h\_{1}),\dots,\mathbf{B}(h\_{n})\big)h\_{i}^{j}(s),\quad s\in[0,\mathcal{T}]\quad j=1,\dots,d. |  |
* •

  More generally, for k≥2k\geq 2, we define the kk-th Malliavin derivative of F∈𝒮𝒯F\in\mathcal{S}\_{\mathcal{T}} along the direction α=(α1,…,αk)∈{1,…,d}k\alpha=(\alpha\_{1},\dots,\alpha\_{k})\in\{1,\dots,d\}^{k} evaluated at 𝐬=(s1,…,sk)∈[0,𝒯]k\mathbf{s}=(s\_{1},\dots,s\_{k})\in[0,\mathcal{T}]^{k} as the real-valued random variable

  |  |  |  |
  | --- | --- | --- |
  |  | D𝐬α​F≔∑i1,…,ik=1n∂kϕ∂xi1α1​⋯​∂xikαk​(𝐁​(h1),…,𝐁​(hn))​hi1α1​(s1)​⋯​hikαk​(sk).\displaystyle D\_{\mathbf{s}}^{\alpha}F\coloneqq\sum\_{i\_{1},\dots,i\_{k}=1}^{n}\frac{\partial^{k}\phi}{\partial x\_{i\_{1}}^{\alpha\_{1}}\cdots\partial x\_{i\_{k}}^{\alpha\_{k}}}\big(\mathbf{B}(h\_{1}),\dots,\mathbf{B}(h\_{n})\big)h\_{i\_{1}}^{\alpha\_{1}}(s\_{1})\cdots h\_{i\_{k}}^{\alpha\_{k}}(s\_{k}). |  |

### 2.2 Wiener chaos expansion and Hermite polynomials

We now present an elementary introduction to the Wiener chaos expansion of L2​(ℱ𝒯)L^{2}(\mathcal{F}\_{\mathcal{T}}) using Hermite polynomials. We refer to [NualartDavidTMCa, Section 1.1] for more details on this topic.

Let Hn​(x)H\_{n}(x) denote the nn-th Hermite polynomial, defined by

|  |  |  |
| --- | --- | --- |
|  | Hn​(x)=(−1)nn!​ex22​dnd​xn​(e−x22),n≥1,H0​(x)=1.\displaystyle H\_{n}(x)=\frac{(-1)^{n}}{n!}e^{\frac{x^{2}}{2}}\frac{d^{n}}{dx^{n}}\big(e^{\frac{-x^{2}}{2}}\big),\quad n\geq 1,\quad H\_{0}(x)=1. |  |

These polynomials are the coefficients of the expansion in powers of tt of the function F​(x,t)=exp⁡(t​x−t22)F(x,t)=\exp\big(tx-\frac{t^{2}}{2}\big). In fact, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(x,t)=exp⁡(x22−12​(x−t)2)\displaystyle F(x,t)=\exp\Big(\frac{x^{2}}{2}-\frac{1}{2}(x-t)^{2}\Big) | =ex22​∑n=0∞tnn!​(dnd​tn​e−(x−t)22)|t=0=∑n=0∞tn​Hn​(x).\displaystyle=e^{\frac{x^{2}}{2}}\sum\_{n=0}^{\infty}\frac{t^{n}}{n!}\Big(\frac{d^{n}}{dt^{n}}e^{-\frac{(x-t)^{2}}{2}}\Big)\Big|\_{t=0}=\sum\_{n=0}^{\infty}t^{n}H\_{n}(x). |  |

Furthermore, since ∂xF​(x,t)=t​exp⁡(x22−12​(x−t)2)\partial\_{x}F(x,t)=t\exp\Big(\frac{x^{2}}{2}-\frac{1}{2}(x-t)^{2}\Big), it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hn′​(x)\displaystyle H\_{n}^{\prime}(x) | =Hn−1​(x),n≥0,\displaystyle=H\_{n-1}(x),\quad n\geq 0, |  |

with the convention H−1​(x)≡0H\_{-1}(x)\equiv 0. We fix an orthonormal basis of L2​([0,𝒯];ℝ)L^{2}([0,\mathcal{T}];\mathbb{R}), denoted by (hi)i≥1(h\_{i})\_{i\geq 1}, and define

|  |  |  |
| --- | --- | --- |
|  | hij​(s)≔ej​hi​(s),\displaystyle h\_{i}^{j}(s)\coloneqq e\_{j}\ h\_{i}(s), |  |

where (ej)1≤j≤d(e\_{j})\_{1\leq j\leq d} denotes the canonical basis of ℝd\mathbb{R}^{d}. Notice that this forms an orthonormal basis of L2​([0,𝒯];ℝd)L^{2}([0,\mathcal{T}];\mathbb{R}^{d}). Consider then the set formed by a=(a1,…,ad)a=(a^{1},\dots,a^{d}), where aj=(a1j,a2j,…)a^{j}=(a\_{1}^{j},a\_{2}^{j},\dots) is a sequence of nonnegative integers such that all the terms, except a finite number of them, vanish. Set a!=∏j=1d∏i≥1aij!a!=\prod\_{j=1}^{d}\prod\_{i\geq 1}a\_{i}^{j}! and |a|=∑j=1d∑i≥1aij|a|=\sum\_{j=1}^{d}\sum\_{i\geq 1}a\_{i}^{j}, and define

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φa=∏j=1d∏i≥1Haij​(∫0𝒯hij​(s)​𝑑Bsj).\displaystyle\Phi\_{a}=\prod\_{j=1}^{d}\prod\_{i\geq 1}H\_{a\_{i}^{j}}\Big(\int\_{0}^{\mathcal{T}}h\_{i}^{j}(s)dB\_{s}^{j}\Big). |  | (2.1) |

Notice that the infinite product in ([2.1](https://arxiv.org/html/2602.16232v1#S2.E1 "In 2.2 Wiener chaos expansion and Hermite polynomials ‣ 2 Preliminaries ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration")) is well defined because H0≡1H\_{0}\equiv 1 and aij≠0a\_{i}^{j}\neq 0 only for a finite number of indices.

For each n≥0n\geq 0, let ℋ𝒯n\mathcal{H}\_{\mathcal{T}}^{n} denote the closed linear subspace of L2​(ℱ𝒯)L^{2}(\mathcal{F}\_{\mathcal{T}}) generated by the random variables {Φa,|a|=n}\{\Phi\_{a},|a|=n\}. This space is called the Wiener chaos of order nn. We then have the following orthogonal expansion, see Theorem 1.1.1 and Proposition 1.1.1 in [NualartDavidTMCa].

###### Theorem 2.1.

1. 1.

   The space L2​(ℱ𝒯)L^{2}(\mathcal{F}\_{\mathcal{T}}) can be decomposed into the infinite orthogonal sum of the subspaces ℋ𝒯n\mathcal{H}\_{\mathcal{T}}^{n}.
2. 2.

   The collection of random variables {a!​Φa,|a|=n}\{\sqrt{a!}\Phi\_{a},|a|=n\} forms a complete orthonormal system in ℋ𝒯n\mathcal{H}\_{\mathcal{T}}^{n}.

We therefore deduce the following result, called the Wiener chaos expansion of L2​(ℱ𝒯)L^{2}(\mathcal{F}\_{\mathcal{T}}).

###### Theorem 2.2.

For any F∈L2​(ℱ𝒯)F\in L^{2}(\mathcal{F}\_{\mathcal{T}}), we have the expansion

|  |  |  |  |
| --- | --- | --- | --- |
|  | F=∑k≥0∑|a|=ka!​⟨Φa,F⟩L2​(ℱ𝒯)​Φa,\displaystyle F=\sum\_{k\geq 0}\sum\_{|a|=k}a!\langle\Phi\_{a},F\rangle\_{L^{2}(\mathcal{F}\_{\mathcal{T}})}\Phi\_{a}, |  | (2.2) |

where the sum converges in L2​(ℱ𝒯)L^{2}(\mathcal{F}\_{\mathcal{T}}).

We conclude this section by introducing the finite-dimensional subspace of L2​(ℱ𝒯)L^{2}(\mathcal{F}\_{\mathcal{T}}) that will serve as the foundation for our model.

###### Definition 2.3.

Let P,M∈ℕP,M\in\mathbb{N}, and let us define the index set given by

|  |  |  |
| --- | --- | --- |
|  | 𝒜P,M,d≔{a=(a1,…,ad)∣aj=(a1j,…,aMj),1≤|a|≤P}.\displaystyle\mathcal{A}\_{P,M,d}\coloneqq\big\{a=(a^{1},\dots,a^{d})\mid a^{j}=(a\_{1}^{j},\dots,a\_{M}^{j}),1\leq|a|\leq P\big\}. |  |

We then define the finite-dimensional space

|  |  |  |
| --- | --- | --- |
|  | L2​(ℱ𝒯)⊃ℋ𝒯(P,M)≔span​{1}⊕span​{Φa∣a∈𝒜P,M,d}.\displaystyle L^{2}(\mathcal{F}\_{\mathcal{T}})\supset\mathcal{H}\_{\mathcal{T}}^{(P,M)}\coloneqq\text{span}\{1\}\oplus\text{span}\big\{\Phi\_{a}\mid a\in\mathcal{A}\_{P,M,d}\big\}. |  |

The dimension of this space can be obtained by using Stars and Bars and Pascal’s identity e.g. [FellerWilliam1968Aitp, see, e.g.,]

|  |  |  |
| --- | --- | --- |
|  | ∑k=0P(M​d+k−1)!(M​d−1)!​k!=(M​d+P)!(M​d)!​P!.\displaystyle\sum\_{k=0}^{P}\frac{(Md+k-1)!}{(Md-1)!k!}=\frac{(Md+P)!}{(Md)!P!}. |  |

## 3 The Wiener Chaos Martingale Model

With the Wiener chaos expansion in place, we can now define a martingale model for the (discounted) underlying asset price process.

Similarly to many other works, we choose to model the price process directly under a risk-neutral measure ℚ\mathbb{Q}. Recall that ℚ\mathbb{Q} is called risk-neutral if it is equivalent to the physical measure ℙ\mathbb{P} and the discounted asset price process is a local (ℚ,𝔽)(\mathbb{Q},\mathbb{F})–martingale. Under the standard no-arbitrage notion of no free lunch with vanishing risk (NFLVR), the existence of a risk-neutral probability measure implies the abscence of arbitrage; see, e.g., [DelbaenSchachermayer1994, GuasoniRasonyiScachermayer2008]. For ease of notation, we shall always assume here that interest rates and dividend yields are zero, so that the asset is already discounted.

We therefore propose the following martingale model for the price process, which we call the *Wiener chaos martingale model*.

###### Definition 3.1 (Wiener chaos martingale model).

Fix truncation levels P,M∈ℕP,M\in\mathbb{N}, a dimension d∈ℕd\in\mathbb{N}, and an orthonormal family (hi)1≤i≤M(h\_{i})\_{1\leq i\leq M} in L2​([0,𝒯])L^{2}([0,\mathcal{T}]).

Let us set the terminal price to be the random variable in ℋ𝒯(P,M)\mathcal{H}\_{\mathcal{T}}^{(P,M)} given by

|  |  |  |
| --- | --- | --- |
|  | S𝒯θ≔S0+∑a∈𝒜P,M,dda​Φa.S\_{\mathcal{T}}^{\theta}\coloneqq S\_{0}+\sum\_{a\in\mathcal{A}\_{P,M,d}}d\_{a}\,\Phi\_{a}. |  |

We then define the price process as the square-integrable (𝔽,ℚ)(\mathbb{F},\mathbb{Q})–martingale

|  |  |  |  |
| --- | --- | --- | --- |
|  | Stθ≔𝔼​[S𝒯θ∣ℱt]=S0+∑a∈𝒜P,M,dda​𝔼​[Φa∣ℱt],t∈[0,𝒯].\displaystyle S\_{t}^{\theta}\coloneqq\mathbb{E}\!\big[S\_{\mathcal{T}}^{\theta}\mid\mathcal{F}\_{t}\big]=S\_{0}+\sum\_{a\in\mathcal{A}\_{P,M,d}}d\_{a}\,\mathbb{E}\!\big[\Phi\_{a}\mid\mathcal{F}\_{t}\big],\qquad t\in[0,\mathcal{T}]. |  | (3.1) |

The model parameters are the chaos coefficients θ={da:a∈𝒜P,M,d}\theta=\{d\_{a}:a\in\mathcal{A}\_{P,M,d}\}, which are fitted to option data during calibration. The truncation levels PP, MM and the basis functions (hi)1≤i≤M(h\_{i})\_{1\leq i\leq M} are fixed in advance and treated as hyperparameters. We stress that a pricing model based on ([3.1](https://arxiv.org/html/2602.16232v1#S3.E1 "In Definition 3.1 (Wiener chaos martingale model). ‣ 3 The Wiener Chaos Martingale Model ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration")) is arbitrage-free, since StθS\_{t}^{\theta} is a (ℚ,𝔽)(\mathbb{Q},\mathbb{F})-martingale by construction.

###### Remark 3.2.

The model defined in ([3.1](https://arxiv.org/html/2602.16232v1#S3.E1 "In Definition 3.1 (Wiener chaos martingale model). ‣ 3 The Wiener Chaos Martingale Model ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration")) may generate sample paths that take negative values, in a manner similar to the model proposed in [Signatures1]. Nevertheless, the numerical experiments indicate that, after calibration, the model is sufficiently flexible to learn dynamics that remain positive.

### 3.1 Universality property

The following proposition shows that the model class in Definition [3.1](https://arxiv.org/html/2602.16232v1#S3.Thmtheorem1 "Definition 3.1 (Wiener chaos martingale model). ‣ 3 The Wiener Chaos Martingale Model ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration") is universal in ℳ𝒯2\mathcal{M}\_{\mathcal{T}}^{2}.

###### Proposition 3.3.

Assume S∈ℳ𝒯2S\in\mathcal{M}\_{\mathcal{T}}^{2} and fix a complete orthonormal system (hi)i≥1(h\_{i})\_{i\geq 1} of L2​([0,𝒯])L^{2}([0,\mathcal{T}]). Then, for any ϵ>0\epsilon>0, there exist P,M∈ℕP,M\in\mathbb{N} and θ∈Θ\theta\in\Theta such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖S−Sθ‖ℳ𝒯22=𝔼​[|S𝒯−S𝒯θ|2]≤ϵ.\displaystyle\|S-S^{\theta}\|\_{\mathcal{M}\_{\mathcal{T}}^{2}}^{2}=\mathbb{E}\!\big[|S\_{\mathcal{T}}-S\_{\mathcal{T}}^{\theta}|^{2}\big]\leq\epsilon. |  | (3.2) |

###### Proof.

Since S∈ℳ𝒯2S\in\mathcal{M}\_{\mathcal{T}}^{2}, we have S𝒯∈L2​(ℱ𝒯)S\_{\mathcal{T}}\in L^{2}(\mathcal{F}\_{\mathcal{T}}).
We therefore have that S𝒯S\_{\mathcal{T}} admits the Wiener chaos representation

|  |  |  |
| --- | --- | --- |
|  | S𝒯=∑k≥0∑|a|=ka!​⟨Φa,S𝒯⟩L2​(ℱ𝒯)​Φa,S\_{\mathcal{T}}=\sum\_{k\geq 0}\sum\_{|a|=k}a!\,\langle\Phi\_{a},S\_{\mathcal{T}}\rangle\_{L^{2}(\mathcal{F}\_{\mathcal{T}})}\,\Phi\_{a}, |  |

where the series converges in L2​(ℱ𝒯)L^{2}(\mathcal{F}\_{\mathcal{T}}). Let P,M∈ℕP,M\in\mathbb{N} and define S𝒯θS\_{\mathcal{T}}^{\theta} as the truncation of this expansion to the index set 𝒜P,M,d\mathcal{A}\_{P,M,d}, and let us set

|  |  |  |
| --- | --- | --- |
|  | da=a!​⟨Φa,S𝒯⟩L2​(ℱ𝒯).d\_{a}=a!\,\langle\Phi\_{a},S\_{\mathcal{T}}\rangle\_{L^{2}(\mathcal{F}\_{\mathcal{T}})}. |  |

Since the chaos expansion converges in L2​(ℱ𝒯)L^{2}(\mathcal{F}\_{\mathcal{T}}), the truncated sum converges to S𝒯S\_{\mathcal{T}} in L2​(ℱ𝒯)L^{2}(\mathcal{F}\_{\mathcal{T}}) as P,M→∞P,M\to\infty. Therefore, for any ϵ>0\epsilon>0, one can choose PP and MM large enough so that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|S𝒯−S𝒯θ|2]≤ϵ.\mathbb{E}\!\left[\,|S\_{\mathcal{T}}-S\_{\mathcal{T}}^{\theta}|^{2}\right]\leq\epsilon. |  |

∎

###### Remark 3.4.

To obtain an explicit error bound for ([3.2](https://arxiv.org/html/2602.16232v1#S3.E2 "In Proposition 3.3. ‣ 3.1 Universality property ‣ 3 The Wiener Chaos Martingale Model ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration")) in terms of the truncation parameters PP and MM, one needs to assume sufficient Malliavin regularity of the random variable S𝒯S\_{\mathcal{T}}; see [lozano2025eulerschemebsdeswiener]. Such regularity is typically satisfied when S𝒯S\_{\mathcal{T}} is the terminal value of an SDE with smooth coefficients [NualartDavidTMCa, see, e.g.,].

A similar approximation result can be obtained for the price of contingent claims whose payoff depends on SS through a Hölder-continuous functional. This includes, for instance, European call options.

###### Proposition 3.5.

Assume that ([3.2](https://arxiv.org/html/2602.16232v1#S3.E2 "In Proposition 3.3. ‣ 3.1 Universality property ‣ 3 The Wiener Chaos Martingale Model ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration")) holds. Let T≤𝒯T\leq\mathcal{T} and F:C​([0,T])→ℝF:C([0,T])\to\mathbb{R} be a Hölder-continuous functional with exponent α∈(0,1]\alpha\in(0,1] and constant L>0L>0, that is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |F​(x)−F​(y)|≤L​‖x−y‖∞αfor all ​x,y∈C​([0,T]).\displaystyle|F(x)-F(y)|\leq L\|x-y\|\_{\infty}^{\alpha}\qquad\text{for all }x,y\in C([0,T]). |  | (3.3) |

Then there exists a constant ℓ>0\ell>0, independent of ϵ\epsilon, such that

|  |  |  |
| --- | --- | --- |
|  | |𝔼​[F​((St)t≤T)]−𝔼​[F​((Stθ)t≤T)]|≤ℓ​ϵα/2.\displaystyle\Big|\mathbb{E}\big[F((S\_{t})\_{t\leq T})\big]-\mathbb{E}\big[F((S\_{t}^{\theta})\_{t\leq T})\big]\Big|\leq\ell\ \epsilon^{\alpha/2}. |  |

###### Proof.

Using ([3.3](https://arxiv.org/html/2602.16232v1#S3.E3 "In Proposition 3.5. ‣ 3.1 Universality property ‣ 3 The Wiener Chaos Martingale Model ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration")), together with Jensen’s inequality and Cauchy-Schwarz, we get

|  |  |  |
| --- | --- | --- |
|  | |𝔼​[F​((St)t≤T)]−𝔼​[F​((Stθ)t≤T)]|≤L​(𝔼​[supt≤T|St−Stθ|2])α/2.\displaystyle\Big|\mathbb{E}\big[F((S\_{t})\_{t\leq T})\big]-\mathbb{E}\big[F((S\_{t}^{\theta})\_{t\leq T})\big]\Big|\leq L\ \Big(\mathbb{E}\Big[\sup\_{t\leq T}|S\_{t}-S\_{t}^{\theta}|^{2}\Big]\Big)^{\alpha/2}. |  |

Using Doob’s L2L^{2} martingale inequality,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[supt≤T|St−Stθ|2]≤4​𝔼​[|ST−STθ|2],\displaystyle\mathbb{E}\Big[\sup\_{t\leq T}|S\_{t}-S\_{t}^{\theta}|^{2}\Big]\leq 4\mathbb{E}\big[|S\_{T}-S\_{T}^{\theta}|^{2}\big], |  |

and because |St−Stθ|2|S\_{t}-S\_{t}^{\theta}|^{2} is a submartingale, for T≤𝒯T\leq\mathcal{T} we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[|ST−STθ|2]≤𝔼​[|S𝒯−S𝒯θ|2]≤ϵ,\displaystyle\mathbb{E}\big[|S\_{T}-S\_{T}^{\theta}|^{2}\big]\leq\mathbb{E}\big[|S\_{\mathcal{T}}-S\_{\mathcal{T}}^{\theta}|^{2}\big]\leq\epsilon, |  |

where we used ([3.2](https://arxiv.org/html/2602.16232v1#S3.E2 "In Proposition 3.3. ‣ 3.1 Universality property ‣ 3 The Wiener Chaos Martingale Model ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration")). Putting everything together gives us

|  |  |  |
| --- | --- | --- |
|  | |𝔼​[F​((St)t≤T)]−𝔼​[F​((Stθ)t≤T)]|≤L​ 2α​ϵα/2.\displaystyle\Big|\mathbb{E}\big[F((S\_{t})\_{t\leq T})\big]-\mathbb{E}\big[F((S\_{t}^{\theta})\_{t\leq T})\big]\Big|\leq L\ \ 2^{\alpha}\ \epsilon^{\alpha/2}. |  |

∎

## 4 Computation of conditional expectations

We now turn to the issue of computing the conditional expectations appearing in ([3.1](https://arxiv.org/html/2602.16232v1#S3.E1 "In Definition 3.1 (Wiener chaos martingale model). ‣ 3 The Wiener Chaos Martingale Model ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration")), namely

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Φa∣ℱt]for each a∈𝒜P,M,d.\displaystyle\mathbb{E}\!\big[\Phi\_{a}\mid\mathcal{F}\_{t}\big]\quad\text{for each $a\in\mathcal{A}\_{P,M,d}$}. |  |

Since the components of the Brownian motion BB are independent, we can factorize the product over each dimension,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[∏j=1d∏i=1MHaij​(∫0𝒯hij​(s)​𝑑Bsj)∣ℱt]=∏j=1d𝔼​[∏i=1MHaij​(∫0𝒯hij​(s)​𝑑Bsj)∣ℱtj],\displaystyle\mathbb{E}\!\Big[\prod\_{j=1}^{d}\prod\_{i=1}^{M}H\_{a\_{i}^{j}}\Big(\int\_{0}^{\mathcal{T}}h\_{i}^{j}(s)dB\_{s}^{j}\Big)\mid\mathcal{F}\_{t}\Big]=\prod\_{j=1}^{d}\mathbb{E}\!\Big[\prod\_{i=1}^{M}H\_{a\_{i}^{j}}\Big(\int\_{0}^{\mathcal{T}}h\_{i}^{j}(s)dB\_{s}^{j}\Big)\mid\mathcal{F}\_{t}^{j}\Big], |  |

where 𝔽j=(ℱtj)t∈[0,𝒯]\mathbb{F}^{j}=(\mathcal{F}\_{t}^{j})\_{t\in[0,\mathcal{T}]} denotes the filtration generated by the jj-th component of the Brownian motion BB. Hence, it suffices to work in the one-dimensional setting, which we assume throughout the remainder of this section.

### 4.1 The case of piecewise-constant functions

The most straightforward choice for (hi)1≤i≤M(h\_{i})\_{1\leq i\leq M} under which one can easily compute the conditional expectations of

|  |  |  |  |
| --- | --- | --- | --- |
|  | Φa=∏i=1MHai​(∫0𝒯hi​(s)​𝑑Bs),a=(a1,…,aM),\displaystyle\Phi\_{a}=\prod\_{i=1}^{M}H\_{a\_{i}}\Big(\int\_{0}^{\mathcal{T}}h\_{i}(s)dB\_{s}\Big),\quad a=(a\_{1},\dots,a\_{M}), |  | (4.1) |

is given by piecewise-constant step functions. These have been already used in [BriandPhilippe2014SOBB], [lozano2025eulerschemebsdeswiener], and are defined by

|  |  |  |
| --- | --- | --- |
|  | hi​(s)≔𝟏(si−1,si]​(s)/δi,δi≔si−si−1,i=1,…,M,\displaystyle h\_{i}(s)\coloneqq\mathbf{1}\_{(s\_{i-1},s\_{i}]}(s)/\sqrt{\delta\_{i}},\quad\delta\_{i}\coloneqq s\_{i}-s\_{i-1},\quad i=1,\dots,M, |  |

where {0=s0<s1<⋯<sM=𝒯}\{0=s\_{0}<s\_{1}<\cdots<s\_{M}=\mathcal{T}\} is some partition of [0,𝒯][0,\mathcal{T}]. Notice that this can be seen as the truncation of an orthonormal system in L2​([0,𝒯];ℝ)L^{2}([0,\mathcal{T}];\mathbb{R}), for example by completing it with the Haar basis in each sub-interval. With this choice, we have that the random variable ([4.1](https://arxiv.org/html/2602.16232v1#S4.E1 "In 4.1 The case of piecewise-constant functions ‣ 4 Computation of conditional expectations ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration")) looks like

|  |  |  |
| --- | --- | --- |
|  | Φa=∏i=1MHai​(Bsi−Bsi−1δi).\displaystyle\Phi\_{a}=\prod\_{i=1}^{M}H\_{a\_{i}}\Big(\frac{B\_{s\_{i}}-B\_{s\_{i-1}}}{\sqrt{\delta\_{i}}}\Big). |  |

In order to compute the conditional expectation, we will use the following lemma, whose proof can be found in [BriandPhilippe2014SOBB, Lemma 2.5].

###### Lemma 4.1.

Let g∈L2​([0,𝒯])g\in L^{2}([0,\mathcal{T}]), and let Ut=∫0tg2​(s)​𝑑sU\_{t}=\int\_{0}^{t}g^{2}(s)ds. For n∈ℕn\in\mathbb{N}, let us define

|  |  |  |
| --- | --- | --- |
|  | Mtn=Utn/2​Hn​(B​(g)t/Ut),B​(g)t=∫0tg​(s)​𝑑Bs.\displaystyle M\_{t}^{n}=U\_{t}^{n/2}H\_{n}\big(B(g)\_{t}/\sqrt{U\_{t}}\big),\quad B(g)\_{t}=\int\_{0}^{t}g(s)dB\_{s}. |  |

Then {Mtn}0≤t≤𝒯\{M\_{t}^{n}\}\_{0\leq t\leq\mathcal{T}} is a martingale. Moreover, we have

|  |  |  |
| --- | --- | --- |
|  | d​Mtn=g​(t)​Mtn−1​d​Bt.\displaystyle dM\_{t}^{n}=g(t)M\_{t}^{n-1}dB\_{t}. |  |

We then obtain the following formula, which was first proved in [BriandPhilippe2014SOBB, Proposition 2.7]. We reproduce here the proof for completeness.

###### Proposition 4.2.

Fix t∈[0,𝒯]t\in[0,\mathcal{T}] and let u∈{1,…,M}u\in\{1,\dots,M\} be such that t∈(su−1,su]t\in(s\_{u-1},s\_{u}]. If a=(a1,…,aM)a=(a\_{1},\dots,a\_{M}) satisfies au+1=⋯=aM=0a\_{u+1}=\cdots=a\_{M}=0, then

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Φa∣ℱt]=∏i<uHai​(Bsi−Bsi−1δi)​(t−su−1δu)au/2​Hau​(Bt−Bsu−1t−su−1).\displaystyle\mathbb{E}\!\big[\Phi\_{a}\mid\mathcal{F}\_{t}\big]=\prod\_{i<u}H\_{a\_{i}}\!\Big(\frac{B\_{s\_{i}}-B\_{s\_{i-1}}}{\sqrt{\delta\_{i}}}\Big)\,\Big(\frac{t-s\_{u-1}}{\delta\_{u}}\Big)^{a\_{u}/2}H\_{a\_{u}}\!\Big(\frac{B\_{t}-B\_{s\_{u-1}}}{\sqrt{t-s\_{u-1}}}\Big). |  |

Otherwise, we have that 𝔼​[Φa∣ℱt]=0\mathbb{E}\!\big[\Phi\_{a}\mid\mathcal{F}\_{t}\big]=0.

###### Proof.

Using the ℱt\mathcal{F}\_{t}-measurability of Brownian motion up until time su−1s\_{u-1}, together with the independence of Brownian increments, we get

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Φa∣ℱt]=∏i<uHai​(Bsi−Bsi−1δi)​𝔼​[Hau​(Bsu−Bsu−1δu)|ℱt]​∏i>u𝔼​[Hai​(Bsi−Bsi−1δi)],\displaystyle\mathbb{E}\!\big[\Phi\_{a}\mid\mathcal{F}\_{t}\big]=\prod\_{i<u}H\_{a\_{i}}\Big(\frac{B\_{s\_{i}}-B\_{s\_{i-1}}}{\sqrt{\delta\_{i}}}\Big)\ \mathbb{E}\Big[H\_{a\_{u}}\Big(\frac{B\_{s\_{u}}-B\_{s\_{u-1}}}{\sqrt{\delta\_{u}}}\Big)\ \Big|\ \mathcal{F}\_{t}\Big]\prod\_{i>u}\mathbb{E}\Big[H\_{a\_{i}}\Big(\frac{B\_{s\_{i}}-B\_{s\_{i-1}}}{\sqrt{\delta\_{i}}}\Big)\Big], |  |

which is null as soon as ai>0a\_{i}>0 for some i∈{u+1,…,M}i\in\{u+1,\dots,M\}. One can then conclude by applying Lemma [4.1](https://arxiv.org/html/2602.16232v1#S4.Thmtheorem1 "Lemma 4.1. ‣ 4.1 The case of piecewise-constant functions ‣ 4 Computation of conditional expectations ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration") with g​(s)=𝟏(su−1,su]​(s)g(s)=\mathbf{1}\_{(s\_{u-1},s\_{u}]}(s), obtaining that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Hau​(Bsu−Bsu−1δu)|ℱt]=(t−su−1δu)au/2​Hau​(Bt−Bsu−1t−su−1).\displaystyle\mathbb{E}\Big[H\_{a\_{u}}\Big(\frac{B\_{s\_{u}}-B\_{s\_{u-1}}}{\sqrt{\delta\_{u}}}\Big)\ \Big|\ \mathcal{F}\_{t}\Big]=\Bigg(\frac{t-s\_{u-1}}{\delta\_{u}}\Bigg)^{a\_{u}/2}H\_{a\_{u}}\Bigg(\frac{B\_{t}-B\_{s\_{u-1}}}{\sqrt{t-s\_{u-1}}}\Bigg). |  |

∎

###### Corollary 4.3.

For t∈(su−1,su]t\in(s\_{u-1},s\_{u}], we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[S𝒯θ∣ℱt]=S0+∑k=1P∑|a​(u)|=kda​∏i<uHai​(Bsi−Bsi−1δi)×(t−su−1δu)au/2​Hau​(Bt−Bsu−1t−su−1)\displaystyle\mathbb{E}\!\big[S\_{\mathcal{T}}^{\theta}\mid\mathcal{F}\_{t}\big]=S\_{0}+\sum\_{k=1}^{P}\sum\_{|a(u)|=k}d\_{a}\prod\_{i<u}H\_{a\_{i}}\Big(\frac{B\_{s\_{i}}-B\_{s\_{i-1}}}{\sqrt{\delta\_{i}}}\Big)\times\Bigg(\frac{t-s\_{u-1}}{\delta\_{u}}\Bigg)^{a\_{u}/2}H\_{a\_{u}}\Bigg(\frac{B\_{t}-B\_{s\_{u-1}}}{\sqrt{t-s\_{u-1}}}\Bigg) |  | (4.2) |

where a​(u)=(a1,…,au,0,…,0)a(u)=(a\_{1},\dots,a\_{u},0,\dots,0).

The following remark will be useful in Section [5](https://arxiv.org/html/2602.16232v1#S5 "5 Calibration procedure ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration").

###### Remark 4.4.

By Corollary [4.3](https://arxiv.org/html/2602.16232v1#S4.Thmtheorem3 "Corollary 4.3. ‣ 4.1 The case of piecewise-constant functions ‣ 4 Computation of conditional expectations ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration"), we have that the random variable given by ([4.2](https://arxiv.org/html/2602.16232v1#S4.E2 "In Corollary 4.3. ‣ 4.1 The case of piecewise-constant functions ‣ 4 Computation of conditional expectations ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration")):

1. 1.

   Depends only on u≤Mu\leq M i.i.d. Gaussian random variables.
2. 2.

   Gives us an orthonormal expansion, meaning that the random variables

   |  |  |  |
   | --- | --- | --- |
   |  | ∏i<uHai​(Bsi−Bsi−1δi)​Hau​(Bt−Bsu−1t−su−1)\displaystyle\prod\_{i<u}H\_{a\_{i}}\Big(\frac{B\_{s\_{i}}-B\_{s\_{i-1}}}{\sqrt{\delta\_{i}}}\Big)H\_{a\_{u}}\Bigg(\frac{B\_{t}-B\_{s\_{u-1}}}{\sqrt{t-s\_{u-1}}}\Bigg) |  |

   are orthonormal.

### 4.2 The general case

Under the piecewise-constant basis, computing conditional expectations is straightforward because, for each t∈[0,𝒯]t\in[0,\mathcal{T}], all but one of the random variables ∫0𝒯hi​(s)​𝑑Bs\int\_{0}^{\mathcal{T}}h\_{i}(s)\,dB\_{s} are either ℱt\mathcal{F}\_{t}-measurable or independent of ℱt\mathcal{F}\_{t}. This simplification typically fails for a general orthonormal family (hi)1≤i≤M(h\_{i})\_{1\leq i\leq M}. We therefore develop an alternative approach to compute these conditional expectations in the general case.

To this end, we use the Dyson formula of [Jin03072016] to compute conditional expectations of random variables satisfying certain technical conditions which are imposed to use Malliavin calculus techniques. We present here the result for random variables with finite-dimensional chaos expansion, which is a direct consequence of (2.20) in [Jin03072016].

In order to shorten the notation, we define the time-truncated Gram matrix

|  |  |  |
| --- | --- | --- |
|  | Gi​k​(t)≔∫t𝒯hi​(s)​hk​(s)​𝑑s,and letIt≔(∫0th1​𝑑B,⋯,∫0thM​𝑑B).\displaystyle G\_{ik}(t)\coloneqq\int\_{t}^{\mathcal{T}}h\_{i}(s)h\_{k}(s)ds,\quad\text{and let}\quad I^{t}\coloneqq\Big(\int\_{0}^{t}h\_{1}dB,\cdots,\int\_{0}^{t}h\_{M}dB\Big). |  |

###### Proposition 4.5.

Let Φa\Phi\_{a} be a random variable with representation ([4.1](https://arxiv.org/html/2602.16232v1#S4.E1 "In 4.1 The case of piecewise-constant functions ‣ 4 Computation of conditional expectations ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration")). Define the operator

|  |  |  |
| --- | --- | --- |
|  | 𝒜t≔∑i,k=1MGi​k​(t)​∂xi∂xk,acting on smooth f​(x1,…,xM).\displaystyle\mathcal{A}\_{t}\coloneqq\sum\_{i,k=1}^{M}G\_{ik}(t)\partial\_{x\_{i}}\partial\_{x\_{k}},\quad\text{acting on smooth $f(x\_{1},\dots,x\_{M})$.} |  |

Then, if f​(x)=∏i=1MHai​(xi)f(x)=\prod\_{i=1}^{M}H\_{a\_{i}}(x\_{i}), we have that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Φa∣ℱt]\displaystyle\mathbb{E}\!\left[\Phi\_{a}\mid\mathcal{F}\_{t}\right] | =∑n=0⌊|a|/2⌋12n​n!​(𝒜t)n​f​(It),\displaystyle=\sum\_{n=0}^{\lfloor|a|/2\rfloor}\frac{1}{2^{n}n!}(\mathcal{A}\_{t})^{n}f(I^{t}), |  |

where (𝒜t)n(\mathcal{A}\_{t})^{n} denotes the nn-fold composition of 𝒜t\mathcal{A}\_{t}.

Notice that the partial derivatives in (𝒜t)n​f(\mathcal{A}\_{t})^{n}f can be computed explicitly using the product rule for derivatives and the fact that Hn′=Hn−1H\_{n}^{\prime}=H\_{n-1}.

###### Example 4.6 (Legendre basis).

An example of an orthonormal basis of L2​([0,𝒯])L^{2}([0,\mathcal{T}]), which we use in the numerical experiments, can be constructed from the Legendre polynomials. These are polynomials {ℒn}n≥0\{\mathcal{L}\_{n}\}\_{n\geq 0} on [−1,1][-1,1] defined by

|  |  |  |
| --- | --- | --- |
|  | ℒn​(x)=12n​n!​dnd​xn​[(x2−1)n],x∈[−1,1],\mathcal{L}\_{n}(x)=\frac{1}{2^{n}n!}\frac{d^{n}}{dx^{n}}\bigl[(x^{2}-1)^{n}\bigr],\qquad x\in[-1,1], |  |

and they satisfy the orthogonality relation

|  |  |  |
| --- | --- | --- |
|  | ∫−11ℒn​(x)​ℒm​(x)​𝑑x=22​n+1​δn​m.\int\_{-1}^{1}\mathcal{L}\_{n}(x)\,\mathcal{L}\_{m}(x)\,dx=\frac{2}{2n+1}\,\delta\_{nm}. |  |

If we define, for i≥1i\geq 1,

|  |  |  |
| --- | --- | --- |
|  | hi​(s):=2​i−1𝒯​ℒi−1​(2​s𝒯−1),s∈[0,𝒯],h\_{i}(s):=\sqrt{\frac{2i-1}{\mathcal{T}}}\;\mathcal{L}\_{\,i-1}\!\left(\frac{2s}{\mathcal{T}}-1\right),\qquad s\in[0,\mathcal{T}], |  |

then {hi}i≥1\{h\_{i}\}\_{i\geq 1} forms an orthonormal basis of L2​([0,𝒯])L^{2}([0,\mathcal{T}]).

## 5 Calibration procedure

In Section [4](https://arxiv.org/html/2602.16232v1#S4 "4 Computation of conditional expectations ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration"), we derived expressions for the conditional expectations of the chaos basis {Φa:a∈𝒜P,M,d}\{\Phi\_{a}:a\in\mathcal{A}\_{P,M,d}\}, which yield an explicit representation of the Wiener chaos martingale model via ([3.1](https://arxiv.org/html/2602.16232v1#S3.E1 "In Definition 3.1 (Wiener chaos martingale model). ‣ 3 The Wiener Chaos Martingale Model ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration")). In this section, we explain how this can be calibrated to observed market data.

A standard approach to calibration under the risk-neutral measure ℚ\mathbb{Q} is to fit the model to prices of liquidly traded European plain-vanilla options, either calls or puts. We calibrate the model to European call options, whose payoff is given by (ST−K)+(S\_{T}-K)\_{+}, where TT and KK denote the maturity and the strike, respectively. The arbitrage-free price at time t=0t=0 in our model is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cθmodel​(T,K)=𝔼​[(STθ−K)+].\displaystyle C\_{\theta}^{\mathrm{model}}(T,K)=\mathbb{E}\!\big[(S\_{T}^{\theta}-K)\_{+}\big]. |  | (5.1) |

Given NN observations of market call prices with maturity–strike pairs (Ti,Ki)(T\_{i},K\_{i}),

|  |  |  |
| --- | --- | --- |
|  | Cmkt​(T1,K1),…,Cmkt​(TN,KN),C^{\mathrm{mkt}}(T\_{1},K\_{1}),\dots,C^{\mathrm{mkt}}(T\_{N},K\_{N}), |  |

we follow the standard approach of [Signatures1, ChristoffersenHestonJacobs2009] and formulate calibration as the optimization problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ∗∈argminθ∈Θ​∑i=1Nγi​(Cmkt​(Ti,Ki)−Cθmodel​(Ti,Ki))2,\displaystyle\theta^{\*}\in\operatorname\*{argmin}\_{\theta\in\Theta}\sum\_{i=1}^{N}\gamma\_{i}\Big(C^{\mathrm{mkt}}(T\_{i},K\_{i})-C\_{\theta}^{\mathrm{model}}(T\_{i},K\_{i})\Big)^{2}, |  | (5.2) |

where γi\gamma\_{i} denotes the Vega weight associated with the ii-th option. These are defined by

|  |  |  |
| --- | --- | --- |
|  | γi≔1Vegai2,Vegai≔∂∂σ​CBS​(Ti,Ki,σ)|σ=σimkt,\gamma\_{i}\coloneqq\frac{1}{\mathrm{Vega}\_{i}^{2}},\qquad\mathrm{Vega}\_{i}\coloneqq\frac{\partial}{\partial\sigma}\,C^{\mathrm{BS}}(T\_{i},K\_{i},\sigma)\Big|\_{\sigma=\sigma\_{i}^{\mathrm{mkt}}}, |  |

where CBS​(T,K,σ)C^{\mathrm{BS}}(T,K,\sigma) denotes the Black–Scholes call price as a function of volatility and σimkt\sigma\_{i}^{\mathrm{mkt}} is the market implied volatility corresponding to (Ti,Ki)(T\_{i},K\_{i}).

The optimization problem ([5.2](https://arxiv.org/html/2602.16232v1#S5.E2 "In 5 Calibration procedure ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration")) is typically solved using an iterative scheme, such as stochastic gradient descent (SGD). As a result, calibration requires repeated evaluations of model option prices for many values of θ∈Θ\theta\in\Theta. It is therefore crucial to compute the expectations in ([5.1](https://arxiv.org/html/2602.16232v1#S5.E1 "In 5 Calibration procedure ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration")) efficiently. In the following, we present two approaches for doing so: The first is broadly applicable, while the second is tailored to short maturities and the choice of piecewise-constant basis functions introduced in Section [4.1](https://arxiv.org/html/2602.16232v1#S4.SS1 "4.1 The case of piecewise-constant functions ‣ 4 Computation of conditional expectations ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration").

### 5.1 Monte Carlo pricing

The most direct way to approximate ([5.1](https://arxiv.org/html/2602.16232v1#S5.E1 "In 5 Calibration procedure ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration")) is by Monte Carlo simulation,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cθmodel​(T,K)=𝔼​[(STθ−K)+]≈1nM​C​∑j=1nM​C(STθ​(ωj)−K)+.\displaystyle C\_{\theta}^{\mathrm{model}}(T,K)=\mathbb{E}\big[(S\_{T}^{\theta}-K)\_{+}\big]\approx\frac{1}{n\_{MC}}\sum\_{j=1}^{n\_{MC}}(S\_{T}^{\theta}(\omega\_{j})-K)\_{+}. |  | (5.3) |

A key observation is that, in the model ([3.1](https://arxiv.org/html/2602.16232v1#S3.E1 "In Definition 3.1 (Wiener chaos martingale model). ‣ 3 The Wiener Chaos Martingale Model ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration")), the samples for the conditional expectations

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[Φa∣ℱT]​(ωj),j=1,…,nM​C,\displaystyle\mathbb{E}\!\big[\Phi\_{a}\mid\mathcal{F}\_{T}\big](\omega\_{j}),\qquad j=1,\dots,n\_{MC}, |  | (5.4) |

can be simulated *offline*, i.e., prior to the calibration of the parameters θ\theta. During the optimization, the same Monte Carlo paths are reused at each iteration, and the values STθ​(ωj)S\_{T}^{\theta}(\omega\_{j}) are obtained simply as the vector–scalar product between ([5.4](https://arxiv.org/html/2602.16232v1#S5.E4 "In 5.1 Monte Carlo pricing ‣ 5 Calibration procedure ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration")) and the coefficients {da,a∈𝒜P,M,d}\{d\_{a},\ a\in\mathcal{A}\_{P,M,d}\}.

#### 5.1.1 Control variates for variance reduction

We now discuss how to incorporate variance reduction techniques [GlassermanPaul2004MCMi, AsmussenGlynn2007, see, e.g.,] into the Monte Carlo estimator described in Section [5.1](https://arxiv.org/html/2602.16232v1#S5.SS1 "5.1 Monte Carlo pricing ‣ 5 Calibration procedure ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration"). For ease of notation, fix (T,K)(T,K) and θ∈Θ\theta\in\Theta, and set

|  |  |  |
| --- | --- | --- |
|  | Y=(STθ−K)+.Y=(S\_{T}^{\theta}-K)\_{+}. |  |

The variance of the MC estimator given by ([5.3](https://arxiv.org/html/2602.16232v1#S5.E3 "In 5.1 Monte Carlo pricing ‣ 5 Calibration procedure ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration")) is Var​(Y)/nM​C\text{Var}(Y)/n\_{MC}. In order to reduce this, we use as control variate the centered random variable

|  |  |  |
| --- | --- | --- |
|  | X1=STθ−S0.X\_{1}=S\_{T}^{\theta}-S\_{0}. |  |

The Monte Carlo estimator then becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1nM​C​∑j=1nM​C{Y​(ωj)−β​X1​(ωj)},β=Cov​(Y,X1)Var​(X1),\displaystyle\frac{1}{n\_{MC}}\sum\_{j=1}^{n\_{MC}}\Big\{Y(\omega\_{j})-\beta\,X\_{1}(\omega\_{j})\Big\},\qquad\beta=\frac{\mathrm{Cov}(Y,X\_{1})}{\mathrm{Var}(X\_{1})}, |  | (5.5) |

where β\beta is estimated from an independent set of simulated samples. Notice that, since X1X\_{1} is centered, the estimator ([5.5](https://arxiv.org/html/2602.16232v1#S5.E5 "In 5.1.1 Control variates for variance reduction ‣ 5.1 Monte Carlo pricing ‣ 5 Calibration procedure ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration")) is still unbiased. Moreover, if β\beta is chosen exactly, the variance of the estimator becomes

|  |  |  |
| --- | --- | --- |
|  | 1nM​C​Var​(Y−β​X1)=1nM​C​Var​(Y)​(1−ρ2),ρ=Corr​(Y,X1).\frac{1}{n\_{MC}}\mathrm{Var}\!\left(Y-\beta X\_{1}\right)=\frac{1}{n\_{MC}}\mathrm{Var}(Y)\left(1-\rho^{2}\right),\qquad\rho=\mathrm{Corr}(Y,X\_{1}). |  |

Hence, the variance is reduced by the factor 1−ρ21-\rho^{2}. In particular, the closer the correlation between YY and X1X\_{1} is to ±1\pm 1, the larger the reduction.

In the case of piecewise-constant kernels, a further variance reduction is possible. By Corollary [4.3](https://arxiv.org/html/2602.16232v1#S4.Thmtheorem3 "Corollary 4.3. ‣ 4.1 The case of piecewise-constant functions ‣ 4 Computation of conditional expectations ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration") and Remark [4.4](https://arxiv.org/html/2602.16232v1#S4.Thmtheorem4 "Remark 4.4. ‣ 4.1 The case of piecewise-constant functions ‣ 4 Computation of conditional expectations ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration") (ii), the second centered moment of STθS\_{T}^{\theta} for T∈(su−1,su]T\in(s\_{u-1},s\_{u}] can be computed explicitly as

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[(STθ)2]=∑k=0P∑|a​(u)|=k(t−su−1δu)au1+⋯+aud​da2a!,\mathbb{E}\big[(S\_{T}^{\theta})^{2}\big]=\sum\_{k=0}^{P}\sum\_{|a(u)|=k}\bigg(\frac{t-s\_{u-1}}{\delta\_{u}}\bigg)^{a\_{u}^{1}+\cdots+a\_{u}^{d}}\frac{d\_{a}^{2}}{a!}, |  |

where a​(u)=(a1​(u),…,ad​(u))a(u)=(a^{1}(u),\dots,a^{d}(u)) with
aj​(u)=(a1j,…,auj,0,…,0)a^{j}(u)=(a\_{1}^{j},\dots,a\_{u}^{j},0,\dots,0) for 1≤j≤d1\leq j\leq d. This allows us to introduce a second control variate and use the estimator

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1nM​C​∑j=1nM​C{Y​(ωj)−β1​X1​(ωj)−β2​X2​(ωj)},\displaystyle\frac{1}{n\_{MC}}\sum\_{j=1}^{n\_{MC}}\Big\{Y(\omega\_{j})-\beta\_{1}X\_{1}(\omega\_{j})-\beta\_{2}X\_{2}(\omega\_{j})\Big\}, |  | (5.6) |

where X=(X1,X2)X=(X\_{1},X\_{2}) and

|  |  |  |
| --- | --- | --- |
|  | (β1β2)=ΣX−1​ΣY​X,ΣX=Cov​(X,X)∈ℝ2×2,ΣY​X=Cov​(Y,X)∈ℝ2.\begin{pmatrix}\beta\_{1}\\ \beta\_{2}\end{pmatrix}=\Sigma\_{X}^{-1}\Sigma\_{YX},\qquad\Sigma\_{X}=\mathrm{Cov}(X,X)\in\mathbb{R}^{2\times 2},\qquad\Sigma\_{YX}=\mathrm{Cov}(Y,X)\in\mathbb{R}^{2}. |  |

In this case, the variance reduction can be expressed in terms of the multiple correlation between YY and the vector X=(X1,X2)X=(X\_{1},X\_{2}). With the optimal choice of coefficients (β1,β2)(\beta\_{1},\beta\_{2}), one has that the variance of ([5.5](https://arxiv.org/html/2602.16232v1#S5.E5 "In 5.1.1 Control variates for variance reduction ‣ 5.1 Monte Carlo pricing ‣ 5 Calibration procedure ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration")) is given by

|  |  |  |
| --- | --- | --- |
|  | Var​(Y−β1​X1−β2​X2)=Var​(Y)​(1−R2),\mathrm{Var}\left(Y-\beta\_{1}X\_{1}-\beta\_{2}X\_{2}\right)=\mathrm{Var}(Y)\left(1-R^{2}\right), |  |

where

|  |  |  |
| --- | --- | --- |
|  | R2=ΣY​X⊤​ΣX−1​ΣY​XVar​(Y)R^{2}=\frac{\Sigma\_{YX}^{\top}\Sigma\_{X}^{-1}\Sigma\_{YX}}{\mathrm{Var}(Y)} |  |

is the coefficient of determination associated with the linear projection of YY onto the span of (X1,X2)(X\_{1},X\_{2}). Thus, the variance is reduced by the factor 1−R21-R^{2}, which is typically smaller than in the single control variate case.

### 5.2 Quadrature-based pricing

As explained in Remark [4.4](https://arxiv.org/html/2602.16232v1#S4.Thmtheorem4 "Remark 4.4. ‣ 4.1 The case of piecewise-constant functions ‣ 4 Computation of conditional expectations ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration"), when the basis functions (hij)1≤i≤M, 1≤j≤d(h\_{i}^{j})\_{1\leq i\leq M,\;1\leq j\leq d} are chosen to be piecewise-constant on a time grid

|  |  |  |
| --- | --- | --- |
|  | {0=s0<s1<⋯<sM=𝒯},\{0=s\_{0}<s\_{1}<\cdots<s\_{M}=\mathcal{T}\}, |  |

the payoff (STθ−K)+(S\_{T}^{\theta}-K)\_{+} depends on u×du\times d independent Gaussian random variables, where u≤Mu\leq M is such that T∈(su−1,su]T\in(s\_{u-1},s\_{u}]. Define, for z∈ℝu×dz\in\mathbb{R}^{u\times d},

|  |  |  |
| --- | --- | --- |
|  | gθ​(z)≔∑k=0P∑|a​(u)|=kda​(T−su−1δu)au/2​∏j=1d∏i=1uHai​(zij).g\_{\theta}(z)\coloneqq\sum\_{k=0}^{P}\sum\_{|a(u)|=k}d\_{a}\Big(\frac{T-s\_{u-1}}{\delta\_{u}}\Big)^{a\_{u}/2}\prod\_{j=1}^{d}\prod\_{i=1}^{u}H\_{a\_{i}}(z\_{i}^{j}). |  |

We then can express

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[(STθ−K)+]=∫ℝu×d(gθ​(z)−K)+​f(u,d)​(z)​𝑑z,\mathbb{E}\big[(S\_{T}^{\theta}-K)\_{+}\big]=\int\_{\mathbb{R}^{u\times d}}\big(g\_{\theta}(z)-K\big)\_{+}\,f\_{(u,d)}(z)\,dz, |  |

where f(u,d)f\_{(u,d)} denotes the density of a standard Gaussian vector in ℝu×d\mathbb{R}^{u\times d}.

When uu is relatively small, this representation makes it feasible to approximate ([5.1](https://arxiv.org/html/2602.16232v1#S5.E1 "In 5 Calibration procedure ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration")) by quadrature instead of Monte Carlo. In this case, we approximate the above integral using Gauss–-Hermite quadrature [HildebrandFrancisBegnaud1956Itna, see, e.g.,].

This approach is particularly effective for short maturities and deep out-of-the-money options, where Monte Carlo can struggle because the event {STθ>K}\{S\_{T}^{\theta}>K\} becomes rare.

## 6 Numerical experiments

In this section, we calibrate the Wiener chaos martingale model introduced in Section [3](https://arxiv.org/html/2602.16232v1#S3 "3 The Wiener Chaos Martingale Model ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration") to option price data. We consider synthetic prices generated by the Heston and rough Heston models, as well as real SPX option data. We use the calibration procedure described in Section [5](https://arxiv.org/html/2602.16232v1#S5 "5 Calibration procedure ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration") with the implementation details provided in Appendix [A](https://arxiv.org/html/2602.16232v1#A1 "Appendix A Calibration details ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration").

The code used in the numerical experiments will be made publicly available in a future release.

### 6.1 The Heston model

The classical Heston model of [Heston1993] is a stochastic volatility model in which the log-price X=log⁡(S)X=\log(S) has the risk-neutral dynamics

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Xt\displaystyle dX\_{t} | =−12​Vt​d​t+Vt​(ρ​d​Bt1+1−ρ2​d​Bt2),\displaystyle=-\tfrac{1}{2}V\_{t}\,dt+\sqrt{V\_{t}}\left(\rho\,dB\_{t}^{1}+\sqrt{1-\rho^{2}}\,dB\_{t}^{2}\right), |  | (6.1) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Vt\displaystyle dV\_{t} | =κ​(v¯−Vt)​d​t+ε​Vt​d​Bt2,V0=v0,\displaystyle=\kappa(\overline{v}-V\_{t})\,dt+\varepsilon\sqrt{V\_{t}}\,dB\_{t}^{2},\quad V\_{0}=v\_{0}, |  |

where B1B^{1} and B2B^{2} are independent Brownian motions. The characteristic function of XtX\_{t} is available in closed form; see, e.g., [Gatheral2006]. For completeness, we recall it in Appendix [B.1](https://arxiv.org/html/2602.16232v1#A2.SS1 "B.1 Heston model ‣ Appendix B Characteristic functions of the log-price under the Heston and Rough Heston models ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration").

To apply Proposition [3.3](https://arxiv.org/html/2602.16232v1#S3.Thmtheorem3 "Proposition 3.3. ‣ 3.1 Universality property ‣ 3 The Wiener Chaos Martingale Model ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration") and justify that the Wiener chaos martingale model can approximate the Heston model, we need 𝔼​[|S𝒯|2]<∞\mathbb{E}[|S\_{\mathcal{T}}|^{2}]<\infty. Parameter conditions ensuring the finiteness of this second moment are given in Appendix [B.1](https://arxiv.org/html/2602.16232v1#A2.SS1 "B.1 Heston model ‣ Appendix B Characteristic functions of the log-price under the Heston and Rough Heston models ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration"), and they are satisfied for the parameter values used in the numerical experiments below.

#### 6.1.1 Fit to option implied volatilities

We consider the Heston model ([6.1](https://arxiv.org/html/2602.16232v1#S6.E1 "In 6.1 The Heston model ‣ 6 Numerical experiments ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration")) with parameters

|  |  |  |  |
| --- | --- | --- | --- |
|  | S0=100,κ=1.5,v¯=0.04,ε=0.5,ρ=−0.7,V0=0.04.S\_{0}=100,\quad\kappa=1.5,\quad\bar{v}=0.04,\quad\varepsilon=0.5,\quad\rho=-0.7,\quad V\_{0}=0.04. |  | (6.2) |

For the Wiener chaos martingale model, we set the time horizon to 𝒯=1.974\mathcal{T}=1.974 and compare two orthonormal truncated bases: the piecewise-constant basis of Section [4.1](https://arxiv.org/html/2602.16232v1#S4.SS1 "4.1 The case of piecewise-constant functions ‣ 4 Computation of conditional expectations ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration") and the Legendre basis of Example [4.6](https://arxiv.org/html/2602.16232v1#S4.Thmtheorem6 "Example 4.6 (Legendre basis). ‣ 4.2 The general case ‣ 4 Computation of conditional expectations ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration"). For the piecewise-constant basis we take M=7M=7 sub-intervals on [0,𝒯][0,\mathcal{T}], while for the Legendre basis we use M=12M=12 functions. In both cases, we truncate the chaos expansion at order P=2P=2, which yields 119 parameters in the piecewise-constant case and 324 parameters in the Legendre case.

We calibrate to call option prices on a grid of seven maturities, from one month to two years, and nine strikes spanning a moneyness range of ±20%\pm 20\%, following [Signatures1]. To assess interpolation across maturities, we also evaluate the fit at six additional maturities that are not used in calibration.

We run 100 independent calibrations and report in Table [1](https://arxiv.org/html/2602.16232v1#S6.T1 "Table 1 ‣ 6.1.1 Fit to option implied volatilities ‣ 6.1 The Heston model ‣ 6 Numerical experiments ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration") the mean absolute error (MAE) of the implied-volatility smiles and the calibration time, given as mean ±\pm standard deviation. The errors are reported in basis points.

|  |  |  |  |
| --- | --- | --- | --- |
|  | MAE (bp) | | Calibration Time (s) |
| Basis | Calibrated | Non-calibrated | Mean ±\pm Std |
| piecewise-constant | 7.37±2.367.37\pm 2.36 | 19.19±2.3619.19\pm 2.36 | 64.29±32.3364.29\pm 32.33 |
| Legendre | 9.82±1.159.82\pm 1.15 | 36.17±9.6836.17\pm 9.68 | 116.75±35.71116.75\pm 35.71 |

Table 1: MAE (bp) of implied volatility surfaces and calibration times (s), reported as mean ±\pm standard deviation over 100 calibrations.

In Figures [1](https://arxiv.org/html/2602.16232v1#S6.F1 "Figure 1 ‣ 6.1.1 Fit to option implied volatilities ‣ 6.1 The Heston model ‣ 6 Numerical experiments ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration") and [2](https://arxiv.org/html/2602.16232v1#S6.F2 "Figure 2 ‣ 6.1.1 Fit to option implied volatilities ‣ 6.1 The Heston model ‣ 6 Numerical experiments ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration"), we show a representative fitted implied volatility surface together with the corresponding surface of absolute errors. Figure [1](https://arxiv.org/html/2602.16232v1#S6.F1 "Figure 1 ‣ 6.1.1 Fit to option implied volatilities ‣ 6.1 The Heston model ‣ 6 Numerical experiments ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration") displays the calibrated maturities, while Figure [2](https://arxiv.org/html/2602.16232v1#S6.F2 "Figure 2 ‣ 6.1.1 Fit to option implied volatilities ‣ 6.1 The Heston model ‣ 6 Numerical experiments ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration") shows the same comparison for the non-calibrated maturities.

![Refer to caption](x1.png)

![Refer to caption](x2.png)

![Refer to caption](x3.png)

Figure 1: Implied-volatility surfaces at the calibrated maturities for the Heston model (top left) and the corresponding absolute-error surfaces (top right), obtained with the piecewise-constant and Legendre bases. The bottom panel shows the implied-volatility smiles. The MAE is 7.23 bp for the piecewise-constant basis and 8.80 bp for the Legendre basis.



![Refer to caption](x4.png)

![Refer to caption](x5.png)

![Refer to caption](x6.png)

Figure 2: Implied-volatility surfaces at the non-calibrated maturities for the Heston model (top left) and the corresponding absolute-error surfaces (top right), obtained with the piecewise-constant and Legendre bases. The bottom panel shows the implied-volatility smiles. The MAE is 16.62 bp for the piecewise-constant basis and 34.95 bp for the Legendre basis.

For the calibrated maturities, both specifications fit the Heston implied-volatility surface very well, and the two fitted surfaces are visually indistinguishable. The piecewise-constant basis performs better in MAE. This is consistent with the fact that the piecewise-constant case allows additional numerical improvements, such as quadrature for short maturities and second moment-based variance reduction. Similar conclusions hold for the non-calibrated maturities. Finally, the piecewise-constant specification is roughly twice as fast to calibrate.

#### 6.1.2 Out-of-sample pricing of path-dependent options

In the previous example, the Wiener chaos martingale model reproduces the calibrated option prices with high accuracy. Since the model is highly over-parameterized, it is natural to ask whether this performance could be due to overfitting, in the sense that the model matches call prices at the calibrated maturities due to its many degrees of freedom, while producing unrealistic dynamics at the path level.

The fact that the model also performs well at maturities not included in calibration suggests that it is not merely fitting noise, but is capturing meaningful features of the marginal distributions of the underlying price process.

A more demanding test is to compare prices of path-dependent options produced by the calibrated model with those generated by the true model. Such tests are known to be challenging for some model classes. For instance, local-volatility models can match the European option surface almost exactly, yet still misprice exotic derivatives because the implied dynamics are unrealistic. Moreover, [SchoutensPerfectCalibration] illustrates that models with similarly good fits to plain-vanilla options can produce widely different exotic prices.

For this exercise, we consider three exotic options: forward-starting call options, down-and-out call options, and floating-strike lookback call options. All three admit closed-form pricing formulas in the Black–Scholes model, which allows us to report results in terms of implied volatilities by numerically inverting the Black–Scholes formula with respect to the volatility parameter. We carry out this analysis only for the Heston model, where computing reference prices is straightforward and computationally efficient.

The formulas used to compute the corresponding implied volatilities are given in Appendix [C](https://arxiv.org/html/2602.16232v1#A3 "Appendix C Exotic option prices and implied volatilities ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration"). The reference prices under the Heston model are obtained by simulating the dynamics with the quadratic–exponential scheme of [AndersenHeston2008] and estimating the option prices by Monte Carlo.

![Refer to caption](x7.png)

![Refer to caption](x8.png)

Figure 3: Forward starting call option comparison, price (top) and Implied Volatility (bottom).



![Refer to caption](x9.png)

![Refer to caption](x10.png)

Figure 4: Down-and-Out call option comparison, price (top) and Implied Volatility (bottom).



![Refer to caption](x11.png)

![Refer to caption](x12.png)

Figure 5: Floating strike lookback call options comparison, price (top) and Implied Volatility (bottom).

Figures [3](https://arxiv.org/html/2602.16232v1#S6.F3 "Figure 3 ‣ 6.1.2 Out-of-sample pricing of path-dependent options ‣ 6.1 The Heston model ‣ 6 Numerical experiments ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration")–[5](https://arxiv.org/html/2602.16232v1#S6.F5 "Figure 5 ‣ 6.1.2 Out-of-sample pricing of path-dependent options ‣ 6.1 The Heston model ‣ 6 Numerical experiments ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration") compare prices and implied volatilities for the three exotic contracts. For forward-starting calls (maturity one year and start times τ∈{0.1,0.2,0.3}\tau\in\{0.1,0.2,0.3\}), the model matches Heston prices well across strikes, although for larger τ\tau it produces slightly too much curvature in implied volatility.

For down-and-out calls, we test several maturity–barrier combinations. In this case, both prices and implied volatilities are matched closely across strikes.

For floating-strike lookback calls, both bases capture the overall term-structure shape. The piecewise-constant basis is slightly below the Heston implied volatilities for intermediate maturities and slightly above at the longest maturity. The Legendre basis shows a more pronounced hump, overshooting Heston for maturities around T≈0.7T\approx 0.7–0.90.9.

Overall, the chaos-based model provides a reasonable approximation of exotic option prices and implied volatilities, suggesting that the learned dynamics remain useful for pricing and hedging beyond the European option surface used in calibration.

### 6.2 The rough Heston model

The rough Heston model of [RoughHeston1, RoughHeston2, AffineVolterraProcesses] is a stochastic volatility model in which the log-price X=log⁡(S)X=\log(S) has risk-neutral dynamics

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt\displaystyle dX\_{t} | =−12​Vt​d​t+Vt​(ρ​d​Bt1+1−ρ2​d​Bt2),\displaystyle=-\tfrac{1}{2}V\_{t}\,dt+\sqrt{V\_{t}}\Big(\rho\,dB\_{t}^{1}+\sqrt{1-\rho^{2}}\,dB\_{t}^{2}\Big), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt\displaystyle V\_{t} | =V0+κ​∫0t(t−s)α−1​(v¯−Vs)​𝑑s+ε​∫0t(t−s)α−1​Vs​𝑑Bs1,\displaystyle=V\_{0}+\kappa\int\_{0}^{t}(t-s)^{\alpha-1}(\bar{v}-V\_{s})\,ds+\varepsilon\int\_{0}^{t}(t-s)^{\alpha-1}\sqrt{V\_{s}}\,dB\_{s}^{1}, |  |

where B1B^{1} and B2B^{2} are independent Brownian motions and κ,v¯,ε>0\kappa,\bar{v},\varepsilon>0 play roles analogous to those in the classical Heston model.

The key difference from the Heston model is the convolution kernel (t−s)α−1(t-s)^{\alpha-1} with α∈(1/2,1]\alpha\in(1/2,1]; the case α=1\alpha=1 reduces to the classical Heston model. The kernel introduces memory into the variance process, so the model is no longer Markovian. When α<1\alpha<1, the variance process VV has sample paths that are only Hölder continuous with exponent α−12\alpha-\tfrac{1}{2}. It has been argued that such roughness is important to reproduce empirically observed features of implied-volatility surfaces [Fukasawa2011, RoughVolPricing, see, e.g.,].

Regarding the finiteness of the second moment, Appendix [B.2](https://arxiv.org/html/2602.16232v1#A2.SS2 "B.2 Rough Heston model ‣ Appendix B Characteristic functions of the log-price under the Heston and Rough Heston models ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration") shows that 𝔼​[|S𝒯|2]<∞\mathbb{E}[|S\_{\mathcal{T}}|^{2}]<\infty for the parameter values used in the numerical experiments below.

#### 6.2.1 Fit to option implied volatilities

For this numerical example, we consider the set of parameters (S0,κ,v¯,ε,ρ,V0)(S\_{0},\kappa,\bar{v},\varepsilon,\rho,V\_{0}) to be the same ones as in ([6.2](https://arxiv.org/html/2602.16232v1#S6.E2 "In 6.1.1 Fit to option implied volatilities ‣ 6.1 The Heston model ‣ 6 Numerical experiments ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration")). The roughness parameter α\alpha is set to α=0.55\alpha=0.55, which corresponds to very irregular sample paths of VtV\_{t} and reflects the values typically found in empirical applications.

For the Wiener chaos martingale model, we fix the time horizon to 𝒯=1.5\mathcal{T}=1.5. As discussed in the previous numerical example, the piecewise-constant basis consistently outperformed the Legendre basis across all reported metrics. The same behavior was observed in the rough Heston experiments. For this reason, and to keep the presentation concise, in what follows we report only the results obtained with the piecewise-constant basis.

The time grid used to construct the piecewise-constant basis functions is build by partitioning [0,𝒯][0,\mathcal{T}] into M=10M=10 sub-intervals. The Wiener chaos expansion is truncated at order P=3P=3. This results in a model with 1,770 parameters.

To fit the model, we compute call option prices on a grid of ten maturities, ranging from one week to 18 months, and nine strikes spanning a moneyness range of ±20%\pm 20\%. Compared to the Heston case, we focus on shorter maturities to make the calibration more challenging, since the pronounced short-maturity skew generated by the rough Heston model is known to be difficult to match with standard stochastic volatility models.

Figure [6](https://arxiv.org/html/2602.16232v1#S6.F6 "Figure 6 ‣ 6.2.1 Fit to option implied volatilities ‣ 6.2 The rough Heston model ‣ 6 Numerical experiments ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration") shows the implied volatility surface generated by the rough Heston model together with the calibrated Wiener chaos martingale model surface, while the corresponding error statistics are reported in Table [2](https://arxiv.org/html/2602.16232v1#S6.T2 "Table 2 ‣ 6.2.1 Fit to option implied volatilities ‣ 6.2 The rough Heston model ‣ 6 Numerical experiments ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration"). Figure [8](https://arxiv.org/html/2602.16232v1#S6.F8 "Figure 8 ‣ 6.2.1 Fit to option implied volatilities ‣ 6.2 The rough Heston model ‣ 6 Numerical experiments ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration") focuses on the three shortest maturities (one week, two weeks, and one month), where the model reproduces the implied volatility smiles almost exactly, even beyond the range of strikes that are typically liquid. Figure [7](https://arxiv.org/html/2602.16232v1#S6.F7 "Figure 7 ‣ 6.2.1 Fit to option implied volatilities ‣ 6.2 The rough Heston model ‣ 6 Numerical experiments ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration") depicts the fits to out of sample maturities, which are also very well matched.

|  |  |  |  |
| --- | --- | --- | --- |
|  | MAE (bp) | | Calibration Time (s) |
| Basis | Calibrated | Non-calibrated | Mean ±\pm Std |
| piecewise-constant | 6.44±0.676.44\pm 0.67 | 21.20±2.2221.20\pm 2.22 | 99.25±31.7499.25\pm 31.74 |

Table 2: Statistics over 100 calibrations to Rough Heston option prices. We report the mean absolute error (MAE) of the implied volatility surfaces in basis points (mean ±\pm standard deviation) for calibrated and non-calibrated maturities, together with the average calibration time in seconds (mean ±\pm standard deviation).



![Refer to caption](x13.png)

![Refer to caption](x14.png)

![Refer to caption](x15.png)

Figure 6: Implied volatility surfaces at the calibrated maturities in the rough Heston model (top left) and surfaces of absolute errors (top right). The bottom panel shows the individual implied volatility smiles. The MAE for these smiles is 6.75 bp.



![Refer to caption](x16.png)

![Refer to caption](x17.png)

![Refer to caption](x18.png)

Figure 7: Implied volatility surfaces at the non-calibrated maturities in the rough Heston model (top left) and surfaces of absolute errors (top right). The bottom panel shows the individual implied volatility smiles. The MAE for these smiles is 23.35 bp.



T = 1 week

![Refer to caption](x19.png)

T = 2 weeks

![Refer to caption](x20.png)

T = 1 month

![Refer to caption](x21.png)

Figure 8: Implied volatility fits to short maturities in the rough Heston model.

### 6.3 Fit to SPX options data

We conclude the numerical experiments by fitting the model to real option data. We use SPX option prices from August 24, 2022, obtained from OptionMetrics. We consider nine maturities between 9 days and 16 months; the available moneyness range varies across maturities depending on quote liquidity. In total, this yields 188 option prices. Discount factors and a constant dividend yield are extracted from the observed prices at each maturity, based on the put-call parity and are included in the calibration.

As in the previous example, we only consider the model with the piecewise-constant basis. We fix the time horizon 𝒯=1.30\mathcal{T}=1.30 and build the time grid used to construct the piecewise-constant basis functions by partitioning [0,𝒯][0,\mathcal{T}] into M=10M=10 sub-intervals. The Wiener chaos expansion is truncated at order P=3P=3. This results in a model with 1,770 parameters.

Figure [9](https://arxiv.org/html/2602.16232v1#S6.F9 "Figure 9 ‣ 6.3 Fit to SPX options data ‣ 6 Numerical experiments ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration") compares the market implied-volatility smiles with those produced by the calibrated Wiener chaos martingale model, and Table [3](https://arxiv.org/html/2602.16232v1#S6.T3 "Table 3 ‣ 6.3 Fit to SPX options data ‣ 6 Numerical experiments ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration") reports the corresponding error statistics over 100 calibrations.

The total time to calibrate is around 60 seconds and the resulting implied volatility surface is depicted on Figure [9](https://arxiv.org/html/2602.16232v1#S6.F9 "Figure 9 ‣ 6.3 Fit to SPX options data ‣ 6 Numerical experiments ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration"), with errors tabulated in Table [3](https://arxiv.org/html/2602.16232v1#S6.T3 "Table 3 ‣ 6.3 Fit to SPX options data ‣ 6 Numerical experiments ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration"). We can see how the Wiener chaos martingale model is able to fit very accurately to the observed implied volatility surface.

|  |  |  |
| --- | --- | --- |
|  | MAE (bp) | Calibration Time (s) |
| Basis | Calibrated | Mean ±\pm Std |
| piecewise-constant | 10.14±1.1410.14\pm 1.14 | 97.85±11.7497.85\pm 11.74 |

Table 3: Statistics over 100 calibrations to SPX option prices. We report the mean absolute error (MAE) of the implied volatility surface in basis points (mean ±\pm standard deviation), together with the average calibration time in seconds (mean ±\pm standard deviation).



T=9 days

![Refer to caption](x22.png)

T=16 days

![Refer to caption](x23.png)

T=23 days

![Refer to caption](x24.png)

T=58 days

![Refer to caption](x25.png)

T=86 days

![Refer to caption](x26.png)

T=114 days

![Refer to caption](x27.png)

T=296 days

![Refer to caption](x28.png)

T=359 days

![Refer to caption](x29.png)

T=478 days

![Refer to caption](x30.png)

Figure 9: Calibrated implied volatility smiles from SPX data. The blue crosses represent the observed implied volatilities and the orange circles represent the fitted implied volatilities. The MAE for these smiles is 11.32 bp.

## Funding

Pere Diaz-Lozano gratefully acknowledges support from the SURE-AI Center, funded by the Research Council of Norway (grant no. 357482).

Thomas K. Kloster gratefully acknowledges financial support from the Center of Research in Energy: Economics and Markets and The Danish Council of Independent Research under DFF grant 10.46540/5247-00005B.

## Appendix A Calibration details

In this section, we provide implementation details for the calibration procedure used in the numerical experiments of Section [6](https://arxiv.org/html/2602.16232v1#S6 "6 Numerical experiments ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration").

### A.1 Calibration hyperparameters

In all cases, we initialize θ\theta by sampling from a centered multivariate normal distribution with independent components and standard deviation 10−410^{-4}.

As discussed in Section [5](https://arxiv.org/html/2602.16232v1#S5 "5 Calibration procedure ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration"), the parameters of the model are calibrated by minimizing the Vega-weighted mean squared error between market and model option prices using a stochastic gradient-based optimizer. In all experiments, we employ the AdamW algorithm, which combines adaptive learning rates with weight decay regularization to stabilize training in the presence of a large number of parameters.

The optimization is run for 10,00010{,}000 iterations with a learning rate of 10−310^{-3}. A weight decay coefficient of 11 is used as L2L^{2} regularization on the chaos coefficients in order to prevent overfitting and to promote numerical stability.

As described in Section [5.1](https://arxiv.org/html/2602.16232v1#S5.SS1 "5.1 Monte Carlo pricing ‣ 5 Calibration procedure ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration"), control variates are employed in the Monte Carlo pricing approximation. For piecewise-constant kernels, we use control variates of polynomial degree 22, whereas for the Legendre basis we use degree 11. In all cases, the corresponding coefficients β\beta are estimated using an independent set of 10410^{4} Monte Carlo samples. To further reduce overfitting of the MC estimator during calibration, the underlying Brownian paths are periodically resimulated every 5050 iterations.

A patience-based stopping criterion is used: The optimizer continues updating the parameters as long as the loss decreases by more than a tolerance of 10−710^{-7}. If the loss doesn’t decrease by the tolerance within 1,000 steps, training is concluded.

All reported results correspond to the parameter set achieving the lowest observed calibration loss during the optimization. In the MC estimators, we show the results corresponding to simulated samples not used in the calibration.

We next specify, for each maturity, the corresponding details used to approximate model option prices. Recall that we propose two pricing approaches: a Monte Carlo estimator (MC) and Gauss–Hermite quadrature (Q). For the Monte Carlo method, we report the number of simulated paths, while for Gauss–Hermite quadrature we report the number of nodes used.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Basis | T1T\_{1}  (0.0821) | T2T\_{2}  (0.1725) | T3T\_{3}  (0.2491) | T4T\_{4}  (0.4983) | T5T\_{5}  (0.9884) | T6T\_{6}  (1.4867) | T7T\_{7}  (1.974) |
| Piecewise-constant | Q 40 | Q 25 | MC 100k | MC 100k | MC 100k | MC 100k | MC 100k |
| Legendre | MC 1M | MC 500k | MC 100k | MC 100k | MC 100k | MC 100k | MC 100k |

Table 4: Pricing method used for the calibrated maturities in the Heston example.



|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Basis | T1T\_{1}  (0.13) | T2T\_{2}  (0.21) | T3T\_{3}  (0.35) | T4T\_{4}  (0.75) | T5T\_{5}  (1.25) | T6T\_{6}  (1.75) |
| Piecewise-constant | Q 30 | Q 15 | MC 100k | MC 100k | MC 100k | MC 100k |
| Legendre | MC 1M | MC 1M | MC 100k | MC 100k | MC 100k | MC 100k |

Table 5: Pricing method used for the non-calibrated maturities in the Heston example.



|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Basis | T1T\_{1}  (0.0191) | T2T\_{2}  (0.0383) | T3T\_{3}  (0.0821) | T4T\_{4}  (0.1642) | T5T\_{5}  (0.2464) | T6T\_{6}  (0.3285) | T7T\_{7}  (0.4928) | T8T\_{8}  (0.6844) | T9T\_{9}  (1.0000) | T10T\_{10}  (1.5000) |
| Piecewise-constant | Q 40 | Q 25 | MC 500k | MC 500k | MC 100k | MC 100k | MC 100k | MC 100k | MC 100k | MC 100k |

Table 6: Pricing method used for the calibrated maturities in the rough Heston example.



|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Basis | T1T\_{1}  (0.02) | T2T\_{2}  (0.05) | T3T\_{3}  (0.10) | T4T\_{4}  (0.28) | T5T\_{5}  (0.40) | T6T\_{6}  (0.85) | T7T\_{7}  (1.25) |
| Piecewise-constant | Q 30 | Q 15 | MC 100k | MC 100k | MC 100k | MC 100k | MC 100k |

Table 7: Pricing method used for the non-calibrated maturities in the rough Heston example.



|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Basis | T1T\_{1}  (0.0246) | T2T\_{2}  (0.0438) | T3T\_{3}  (0.0629) | T4T\_{4}  (0.1587) | T5T\_{5}  (0.2354) | T6T\_{6}  (0.3121) | T7T\_{7}  (0.3504) | T8T\_{8}  (0.8104) | T9T\_{9}  (0.9828) | T10T\_{10}  (1.3086) |
| Piecewise-constant | Q 40 | Q 25 | MC 100k | MC 100k | MC 50k | MC 50k | MC 50k | MC 50k | MC 50k | MC 50k |

Table 8: Pricing method used for the calibrated maturities in the SPX example.

## Appendix B Characteristic functions of the log-price under the Heston and Rough Heston models

Both the Heston and Rough Heston models admit semi-closed-form expressions for the characteristic function of the log-price. This allows European call option prices to be computed accurately using transform inversion techniques, such as the Lewis formula
of [Lewis2000]

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[(ST−K)+]=S0​e−q​T−e−r​T​Kπ​∫0∞ℜ⁡{e(i​u+12)​(log⁡(S0K)+(r−q)​T)​φXT​(u−i2)​1u2+14}​𝑑u,\mathbb{E}\!\left[(S\_{T}-K)^{+}\right]=S\_{0}e^{-qT}-\frac{e^{-rT}K}{\pi}\int\_{0}^{\infty}\Re\left\{e^{\left(\mathrm{i}u+\tfrac{1}{2}\right)\left(\log\left(\tfrac{S\_{0}}{K}\right)+(r-q)T\right)}\varphi\_{X\_{T}}(u-\tfrac{\mathrm{i}}{2})\frac{1}{u^{2}+\tfrac{1}{4}}\right\}du, |  | (B.1) |

where φXT​(u)=𝔼​[ei​u​XT]\varphi\_{X\_{T}}(u)=\mathbb{E}\!\left[e^{\mathrm{i}uX\_{T}}\right] is the characteristic function of the log-price XT=log⁡(ST)X\_{T}=\log(S\_{T}).

### B.1 Heston model

Characteristic function. The characteristic function of the log-price for the Heston model is available in closed form, see e.g. [Gatheral2006]. This is given by

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[ei​u​Xt]=exp⁡(u​X0+a​(t)+b​(t)​V0),\mathbb{E}\!\left[e^{\mathrm{i}uX\_{t}}\right]=\exp\left(uX\_{0}+a(t)+b(t)V\_{0}\right), |  |

where the coefficients a​(t),b​(t)a(t),b(t) are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | a​(t)\displaystyle a(t) | =−κ​v¯​(γ+βε2​t+2ε​log⁡(1−γ+β2​γ​(1−e−γ​t))),\displaystyle=-\kappa\bar{v}\left(\frac{\gamma+\beta}{\varepsilon^{2}}t+\frac{2}{\varepsilon}\log\left(1-\frac{\gamma+\beta}{2\gamma}\left(1-e^{-\gamma t}\right)\right)\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | b​(t)\displaystyle b(t) | =u​(1−u)​(1−e−γ​t)2​γ−(γ+β)​(1−e−γ​t),\displaystyle=\frac{u(1-u)(1-e^{-\gamma t})}{2\gamma-(\gamma+\beta)(1-e^{-\gamma t})}, |  |

with β=u​ρ​ε−κ\beta=u\rho\varepsilon-\kappa and γ=(κ−u​ρ​ε)2−ε2​(u2−u)\gamma=\sqrt{(\kappa-u\rho\varepsilon)^{2}-\varepsilon^{2}(u^{2}-u)}.

Moment explosions. In the Heston model, the moment explosion time

|  |  |  |
| --- | --- | --- |
|  | T∗​(u)=sup{t≥0:𝔼​[Stu]<∞}T^{\ast}(u)=\sup\left\{t\geq 0:\mathbb{E}\!\left[S\_{t}^{\,u}\right]<\infty\right\} |  |

has been explicitly characterized in [AndersenPiterbarg2007, KellerRessel2011momentexplosions]. Specializing to the case u=2u=2, one obtains that 𝔼​[St2]<∞\mathbb{E}[S\_{t}^{2}]<\infty for all t≥0t\geq 0 (equivalently, T∗​(1.974)=∞T^{\ast}(1.974)=\infty) if and only if

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ2=(2​ρ​ε−κ)2−2​ε2≥0,χ2=2​ρ​ε−κ<0.\Delta\_{2}=(2\rho\varepsilon-\kappa)^{2}-2\varepsilon^{2}\geq 0,\qquad\chi\_{2}=2\rho\varepsilon-\kappa<0. |  | (B.2) |

### B.2 Rough Heston model

Characteristic function. The characteristic function of the log-price in the rough Heston model is available in semi-closed form; see, for instance, [RoughHeston1]. It can be written as

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[ei​u​Xt]=exp⁡(i​u​Xt+κ​v¯​∫0tψ​(s)​𝑑s+V0​∫0tR​(u,ψ​(s))​𝑑s),\mathbb{E}\!\left[e^{\mathrm{i}uX\_{t}}\right]=\exp\!\left(\mathrm{i}uX\_{t}+\kappa\bar{v}\int\_{0}^{t}\psi(s)\,ds+V\_{0}\int\_{0}^{t}R\big(u,\psi(s)\big)\,ds\right), |  |

where

|  |  |  |
| --- | --- | --- |
|  | R​(u,w)=u2−u2−(κ−u​ρ​ε)​w+ε22​w2,R(u,w)=\frac{u^{2}-u}{2}-(\kappa-u\rho\varepsilon)w+\frac{\varepsilon^{2}}{2}w^{2}, |  |

and ψ\psi solves the fractional Riccati equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dα​ψ​(t)=R​(u,ψ​(t)).D^{\alpha}\psi(t)=R\big(u,\psi(t)\big). |  | (B.3) |

The fractional Riccati equation ([B.3](https://arxiv.org/html/2602.16232v1#A2.E3 "In B.2 Rough Heston model ‣ Appendix B Characteristic functions of the log-price under the Heston and Rough Heston models ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration")) does not admit a closed-form solution and must be solved numerically, which can be computationally demanding. To address this issue, [RationalApproximations] propose an accurate approximation of the rough Heston solution ψ\psi based on rational functions. This approximation allows option prices to be computed both efficiently and with high accuracy.

Moment explosions. Moment explosions in the rough Heston model are analyzed in [RoughHestonMomentExplosions]. Although the analysis is more involved than in the classical Heston setting, Theorem 2.4 in [RoughHestonMomentExplosions] shows that the explosion time T∗​(u)T^{\ast}(u) is finite in the rough Heston model if and only if it is finite in the corresponding classical Heston model obtained by setting α=1\alpha=1. Based on the analysis in [B.1](https://arxiv.org/html/2602.16232v1#A2.SS1 "B.1 Heston model ‣ Appendix B Characteristic functions of the log-price under the Heston and Rough Heston models ‣ A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration") we thus conclude that T∗​(1.5)=∞T^{\ast}(1.5)=\infty.

## Appendix C Exotic option prices and implied volatilities

In the numerical experiments with the Heston model, we consider how well the calibrated model matches implied volatilities of some path dependent exotic options to which the model is *not* calibrated. We consider the following three types of exotic options, which all admit closed form prices in the Black-Scholes model. Up to strike, maturity, interest rate, and dividend yield, these prices all depend only on the model parameter σ\sigma, and we can thus define the corresponding exotic option implied volatilities by numerical inversion in σ\sigma, once the prices are computed via simulation.

1. 1.

   Forward starting call options: These are simply call options that start at a pre-specified future date, τ\tau, and their prices are therefore sensitive to the forward evolution of the model implied volatility surface. The Black-Scholes price of a forward starting option is

   |  |  |  |
   | --- | --- | --- |
   |  | CB​Sfwd​(S0,T,K,τ;σ)=e−q​τ​CB​S​(S0,T−τ,K;σ),C\_{BS}^{\mathrm{fwd}}(S\_{0},T,K,\tau;\sigma)=e^{-q\tau}C\_{BS}(S\_{0},T-\tau,K;\sigma), |  |

   where CB​SC\_{BS} denotes the Black-Scholes call option price.
2. 2.

   Down-and-out call options: These have payoff f​(ST)=(ST−K)+​𝟏{inft∈[0,T]St>L},f(S\_{T})=(S\_{T}-K)^{+}\mathbf{1}\_{\{\inf\_{t\in[0,T]}S\_{t}>L\}}, for some lower barrier L>0L>0. The Black-Scholes price of a down-and-out call option is

   |  |  |  |
   | --- | --- | --- |
   |  | CB​Sdao​(S0,T,K,L;σ)=CB​S​(S0,T,K;σ)−(LS0)r−q−σ2/2σ2​CB​S​(L2/S0,T,K;σ).C\_{BS}^{\mathrm{dao}}(S\_{0},T,K,L;\sigma)=C\_{BS}(S\_{0},T,K;\sigma)-\left(\frac{L}{S\_{0}}\right)^{\frac{r-q-\sigma^{2}/2}{\sigma^{2}}}C\_{BS}(L^{2}/S\_{0},T,K;\sigma). |  |
3. 3.

   Floating strike lookback call options: These have payoff f​(ST)=(ST−inft∈[0,T]St)+f(S\_{T})=(S\_{T}-\inf\_{t\in[0,T]}S\_{t})^{+}. The Black-Scholes price of a lookback call option is

   |  |  |  |
   | --- | --- | --- |
   |  | CB​Slb​(S0,T;σ)=CB​S​(S0,T,S0;σ)−S0​e−q​T​σ22​(r−q)​(Φ​(−d1)−e−(r−q)​T​Φ​(−d3)),C\_{BS}^{\mathrm{lb}}(S\_{0},T;\sigma)=C\_{BS}(S\_{0},T,S\_{0};\sigma)-\frac{S\_{0}e^{-qT}\sigma^{2}}{2(r-q)}\left(\Phi(-d\_{1})-e^{-(r-q)T}\Phi(-d\_{3})\right), |  |

   where d1=(r−q+12​σ2)​Tσ​Td\_{1}=\frac{(r-q+\frac{1}{2}\sigma^{2})T}{\sigma\sqrt{T}} and d3=d1−2​(r−q)​Tσd\_{3}=d\_{1}-\frac{2(r-q)\sqrt{T}}{\sigma}.

## References