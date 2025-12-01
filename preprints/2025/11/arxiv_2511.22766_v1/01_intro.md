---
authors:
- Haoying Dai
doc_id: arxiv:2511.22766v1
family_id: arxiv:2511.22766
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option
  Markets
url_abs: http://arxiv.org/abs/2511.22766v1
url_html: https://arxiv.org/html/2511.22766v1
venue: arXiv q-fin
version: 1
year: 2025
---


Haoying Dai
[dhy@terpmail.umd.edu](mailto:dhy@terpmail.umd.edu)

###### Abstract

We develop a theoretical framework that aims to link micro-level option hedging and stock-specific factor exposure with macro-level market turbulence and explain endogenous volatility amplification during gamma-squeeze events.
By explicitly modeling market-maker delta-neutral hedging and incorporating beta-dependent volatility normalization, we derive a stability condition that characterizes the onset of a gamma-squeeze event.
The model captures a nonlinear recursive feedback loop between market-maker hedging and price movements and the resulting self-reinforcing dynamics.
From a complex-systems perspective, the dynamics represent a bounded nonlinear response in which effective gain depends jointly on beta-normalized shock perception and gamma-scaled sensitivity.
Our analysis highlights that low-beta stocks exhibit disproportionately strong feedback even for modest absolute price movements.

###### keywords:

Gamma squeeze , Delta-neutral hedging , Endogenous volatility , Beta normalization , Market microstructure , Nonlinear recursive feedback

\affiliation

[sigma]
organization=Eight Sigma Research,
city=College Park,
state=MD,
postcode=20740,
country=USA

## 1 Introduction

Financial markets frequently exhibit nonlinear price dynamics that appear disproportionate to underlying shocks, reflecting the complex interplay between derivative trading, market microstructure, and investor behavior. A salient manifestation of this recursive feedback behavior is the gamma squeeze, in which large option positions compel market makers to adjust their holdings of the underlying asset to maintain delta-neutrality. These hedging flows can self-reinforce, occasionally producing transient deviations far exceed typical volatility. Recent retail-driven episodes, notably in GameStop (GME) and AMC, underscore the practical significance of this nonlinear amplification and its potential implications for market stability[chaumont2021gamestop, lyocsa2022yolo].

Prior research has established that dealer hedging can generate endogenous price impact. [garleanu2007, garleanu2011] show that option-market liquidity and hedging flows materially affect price formation, while brunnermeier2009 examine how feedback trading amplifies volatility under varying liquidity conditions. Complementary studies on factor models and systemic risk [adrian2010, engle2002, longin2001] highlight the role of stock-specific sensitivities in propagating volatility, yet most formulations treat feedback as approximately linear and assume constant sensitivity. A broader literature further shows that dynamic hedging, order-flow imbalance, and liquidity fluctuations can produce nonlinear amplification [avellaneda2003, farmer2013, bouchaud2018, cont2014, donier2015], and that concentrated options positions may trigger abrupt rallies through mechanical gamma rebalancing [ni2008], consistent with empirical evidence from the 2021 meme-stock events [fisch2022gamestop, huffman2025rise, aggarwal2022meme]. Insights from factor pricing [ang2006cross, campbell1997econometrics, andersen2007, barunik2018] and from nonlinear and critical-transition dynamics [sornette2003, mantegna2000, lux1999, guckenheimer1983, ott2002, kantz2004, farmer2002, lorenz1963, mandelbrot1977, bak1987, bak1988] similarly emphasize how small disturbances can escalate when interacting with constrained liquidity. However, these frameworks still overlook a central asymmetry: feedback intensity depends strongly on how unusual a price change appears relative to a stock’s typical volatility regime.

Empirical observation suggests that identical absolute price changes can elicit markedly different reactions across stocks. For example, a 3%3\% move in a low-beta stock may represent a deviation several times larger than its typical volatility, attracting a large volumes of call options that prompting aggressive hedging adjustments, whereas a 10%10\% move in a high-beta stock may constitute a routine fluctuation. Such nonlinear sensitivity implies that the same exogenous perturbation can trigger vastly different feedback intensities depending on local volatility norms. Hence, it is not appropriate to treat stocks with different β\beta levels equivalently when analyzing these events. Capturing this perceived shock intensity relative to stock-specific volatility is essential for understanding differential gamma feedback and the conditions under which a squeeze occurs.

This paper introduces a beta-dependent gamma-feedback framework that integrates delta-gamma hedging mechanics with stock-specific volatility scaling. It considers the relative sensitivity of a specific stock to broader market behavior. The model defines a relative shock measure normalized by β\beta, enabling a rigorous characterization of conditions under which hedging flows can generate nonlinear amplification. It provides both a mathematically tractable stability condition for gamma squeezes and an intuitive interpretation of why low-beta stocks are disproportionately sensitive to modest shocks.

The main contributions of this work are:

1. 1.

   Formal derivation of gamma-squeeze thresholds: Establishing a condition for endogenous volatility amplification grounded in delta-neutral hedging mechanics.
2. 2.

   Integration of beta-normalized shock perception: Providing a framework to study the different behaviors of stocks with varying sensitive to the market turbulence, i.e., different β\betas.
3. 3.

   Simulation and empirical applicability: The numerical frameworks can be used to synthetic and real market data.
4. 4.

   A trackable model that can be interpreted to understand market mechanism: Providing an interpretable model that links option microstructure, market-maker behavior, and factor-driven stock dynamics.

## 2 The Model

### 2.1 Formal Gamma-Squeeze Derivation via Delta-Neutral Hedging

The gamma squeeze can be viewed as a recursive feedback system arising from a market maker’s effort to maintain delta-neutrality. When a market maker sells NN call options on a stock with price StS\_{t}, they are exposed to changes in delta. Let C​(St,t)C(S\_{t},t) denote the option price. The delta of a single option is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δc=∂C∂S,\Delta\_{c}=\frac{\partial C}{\partial S}, |  | (1) |

and the total option delta is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δtotal=N​Δc.\Delta\_{\mathrm{total}}=N\Delta\_{c}. |  | (2) |

To remain delta-neutral the market maker holds a stock position HtH\_{t} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δtotal−Ht=0⇒Ht=N​Δc.\Delta\_{\mathrm{total}}-H\_{t}=0\quad\Rightarrow\quad H\_{t}=N\Delta\_{c}. |  | (3) |

When the underlying price moves, the option’s delta changes; market makers must buy or sell the underlying to restore neutrality. This dynamic creates a *feedback loop*: as market makers buy to hedge short-call exposure, buying pressure pushes the price up, which increases option deltas further and forces additional hedging purchases.

Thus, the sensitivity of delta to changes in the underlying price can be captured:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γ=∂Δc∂S=∂2C∂S2.\Gamma=\frac{\partial\Delta\_{c}}{\partial S}=\frac{\partial^{2}C}{\partial S^{2}}. |  | (4) |

For a small price change Δ​S\Delta S the option delta changes approximately as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Δc≈Γ​Δ​S.\Delta\Delta\_{c}\approx\Gamma\,\Delta S. |  | (5) |

Consequently, to remain delta-neutral the market maker adjusts their stock holdings by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Ht=N​Γ​Δ​S.\Delta H\_{t}=N\Gamma\,\Delta S. |  | (6) |

Empirical microstructure literature models the impact of net order flow on prices with a (first-order) linear price–impact coefficient λ\lambda [cetin2004liquidity, garleanu2013dynamic]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​St=μ​St+λ​Δ​Ht,\Delta S\_{t}=\mu S\_{t}+\lambda\,\Delta H\_{t}, |  | (7) |

where μ​St\mu S\_{t} denotes exogenous drift or shock that ignites a price change and μ\mu measures the level of surprise and λ\lambda summarizes liquidity/price–impact properties of the market. Substituting the hedging adjustment Δ​Ht=N​Γ​Δ​St\Delta H\_{t}=N\Gamma\,\Delta S\_{t} yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​St=μ​St+λ​N​Γ​Δ​St⇒Δ​St​(1−λ​G)=μ​St,\Delta S\_{t}=\mu S\_{t}+\lambda N\Gamma\,\Delta S\_{t}\quad\Rightarrow\quad\Delta S\_{t}(1-\lambda G)=\mu S\_{t}, |  | (8) |

where we define total gamma exposure G≡N​ΓG\equiv N\Gamma.

### 2.2 Beta-Normalized Intuition

The derivation in Section [2.1](https://arxiv.org/html/2511.22766v1#S2.SS1 "2.1 Formal Gamma-Squeeze Derivation via Delta-Neutral Hedging ‣ 2 The Model ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets") captures the mechanical structure of gamma-induced feedback under delta-neutral hedging. However, it implicitly assumes that all price changes of equal absolute magnitude are perceived equally by market participants. In reality, the sharpness of a move is not an absolute quantity but a relative one: it depends on how unusual the move appears relative to the stock’s typical behavior and volatility regime.

To formalize this intuition, we introduce a beta-normalized relative surprise variable for a specific stock ii:

|  |  |  |  |
| --- | --- | --- | --- |
|  | xi=|Δ​S/S||βi|​σm,x\_{i}=\frac{|\Delta S/S|}{|\beta\_{i}|\sigma\_{m}}, |  | (9) |

where
σm\sigma\_{m} is aggregate market volatility, and β\beta measures the stock’s sensitivity to systematic market movements. The σm\sigma\_{m} captures behavior of the whole market with the implications that during a market-wide high-turbulent event, the stock-specific shocks will be perceived as relatively small and less likely to induce aggressive hedging. Moreover, by normalizing the absolute price change ratio Δ​S/S\Delta S/S with respect to β\beta, the perceived surprise is related to its normal price behavior, justifying the idea the high-volatile stock is less likely to incur gamma squeeze comparing to low-beta stock with the same ratio of price change.
Here, we focus on the positive beta stocks in a gamma-squeeze event, which leads to |β|=β|\beta|=\beta. This normalization follows the logic of factor-based volatility scaling in asset pricing and systemic risk models [engle2002, longin2001, adrian2019vulnerable], where β\beta effectively acts as a proportionality constant linking market-level shocks to firm-level responses.

### 2.3 Combined Gamma-Beta Model and Proposition

Building on Sections [2.1](https://arxiv.org/html/2511.22766v1#S2.SS1 "2.1 Formal Gamma-Squeeze Derivation via Delta-Neutral Hedging ‣ 2 The Model ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets") and [2.2](https://arxiv.org/html/2511.22766v1#S2.SS2 "2.2 Beta-Normalized Intuition ‣ 2 The Model ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets"), we integrate delta-neutral hedging mechanics with beta-normalized shock perception to construct a unified framework for gamma squeezes.

Let G=N​ΓG=N\Gamma denote total gamma exposure,
To remain delta-neutral, the hedging intensity of market makers can be written as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Ht=G​Δ​St​ϕ​(x),ϕ′​(x)>0.\Delta H\_{t}=G\,\Delta S\_{t}\,\phi(x),\quad\phi^{\prime}(x)>0. |  | (10) |

Here, we introduce ϕ​(x)\phi(x) as an increasing function that describes how abnormal price movements intensify the scale of hedging adjustments that is directly proportional to the surprise xix\_{i} with ϕ​(x)=1+k​x\phi(x)=1+kx, with k=2k=2. This form is consistent with both behavioral and empirical findings that order flow becomes more elastic and reactive under unusual price dynamics [bouchaud2018].

Here, the stability denominator of this stock can be rewritten as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Di=1−λ​G​ϕ​(xi).D\_{i}=1-\lambda\,G\,\phi(x\_{i}). |  | (11) |

From above derivation, it can be seen that gamma squeeze occurs when the stability denominator approaches zero:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Di⟶0.D\_{i}\longrightarrow 0. |  | (12) |

The condition Di→0D\_{i}\to 0 formalizes the threshold at which even modest exogenous shocks (μ​St\mu S\_{t}) are magnified into large price movements.

Sections [2.1](https://arxiv.org/html/2511.22766v1#S2.SS1 "2.1 Formal Gamma-Squeeze Derivation via Delta-Neutral Hedging ‣ 2 The Model ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets") to [2.3](https://arxiv.org/html/2511.22766v1#S2.SS3 "2.3 Combined Gamma-Beta Model and Proposition ‣ 2 The Model ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets") together establish a static theoretical framework for delta-neutral hedging with beta-normalized shock perception, which explains how endogenous volatility amplification can initiate a gamma squeeze event under specific initial conditions. However, a gamma squeeze is inherently a dynamic phenomenon, characterized by a self-reinforcing feedback loop: as market makers hedge by buying the underlying stock, their actions drive the price higher, which in turn attracts additional call-option activity and further intensifies the hedging demand. This dynamic interaction motivates the development of a time-evolving model, which will be discussed in the subsequent section.

### 2.4 Dynamic Beta-Normalized Recursive Feedback with Decay and Saturation

In real markets, gamma squeezes evolve through multiple recursive rounds of adjustment, where hedging activity itself becomes the primary driver of subsequent price movements. To capture this compounding mechanism, we formulate a discrete-time recursive model that integrates three interacting components: (i) position decay, representing the gradual reduction of dealer exposure as balance-sheet constraints, liquidity costs, or margin limits force contraction of open option positions; (ii) saturating hedging impact, which bounds the effective price response through nonlinear liquidity effects; (iii), a decaying exogenous shock term, μt​St\mu\_{t}S\_{t}, which models the transient initiation of the squeeze and diminishes with the reduction in active hedging exposure.

Let StS\_{t} denote the stock price at discrete time tt, and let market-makers maintain delta-neutrality by recursively adjusting their positions in response to price changes.
We can replace the static delta neutral hedging Equation [10](https://arxiv.org/html/2511.22766v1#S2.E10 "In 2.3 Combined Gamma-Beta Model and Proposition ‣ 2 The Model ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets") into a recursive one:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​Ht=Nt​Γt​Δ​Stobs,\Delta H\_{t}=N\_{t}\Gamma\_{t}\,\Delta S\_{t}^{\text{obs}}, |  | (13) |

where Δ​Stobs=St−St−1\Delta S\_{t}^{\text{obs}}=S\_{t}-S\_{t-1} is the observed price change, NtN\_{t} the active position size, and Γt\Gamma\_{t} the option gamma exposure.

To capture the feedback-sensitive erosion of liquidity and dealer balance-sheet capacity, we model position decay as a function of cumulative realized price movement according to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Nt=N01+η​(∑τ=0t−1|Δ​SτobsSτ|)ξ,η,ξ>0,N\_{t}=\frac{N\_{0}}{1+\eta\Big(\sum\_{\tau=0}^{t-1}\Big|\frac{\Delta S\_{\tau}^{\mathrm{obs}}}{S\_{\tau}}\Big|\Big)^{\xi}},\qquad\eta,\xi>0, |  | (14) |

where Δ​Sτobs=Sτ−Sτ−1\Delta S\_{\tau}^{\mathrm{obs}}=S\_{\tau}-S\_{\tau-1} and the summation accumulates the absolute relative movements of past price changes, η\eta and ξ\xi are hyper-parameters accounting the decay.
At the onset of a squeeze, cumulative movement is small, implying Nt≈N0N\_{t}\approx N\_{0} and strong recursive feedback;
as large realized moves accumulate, the denominator in ([14](https://arxiv.org/html/2511.22766v1#S2.E14 "In 2.4 Dynamic Beta-Normalized Recursive Feedback with Decay and Saturation ‣ 2 The Model ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets")) grows, compressing NtN\_{t} and reducing hedging pressure.

Market makers operate under finite inventory and hedging capacity, so their price-impact response cannot grow without bound. Classical inventory research[holt1960planning, arrow1951, arrow1951, sargent1978] shows that limited capacity naturally produces smooth, concave, saturating adjustments rather than unbounded linear responses.
Early models [baumol1952, scarf1960, howard1960] therefore used linear impact capped at a fixed threshold:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Imax​(y)=min⁡(Imax,max⁡(−Imax,y)).I\_{\max}(y)=\min\!\bigl(I\_{\max},\,\max(-I\_{\max},\,y)\bigr). |  | (15) |

However, such piecewise linear function introduces nondifferentiabilities and arbitrary turning points. They have been widely criticized for generating model artifacts, numerical instability, and analytical complications in dynamical systems analysis[tobin1969, goodwin1951, fleming2006controlled].

Thus, we propose the t​a​n​htanh to account for the market maker’s limited hedging capacity as a replacement of the piecewise linear function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I​(y)=tanh⁡(c​y),c>0,I(y)=\tanh(cy),\qquad c>0, |  | (16) |

since it is linear for small order imbalances similar to Equation [15](https://arxiv.org/html/2511.22766v1#S2.E15 "In 2.4 Dynamic Beta-Normalized Recursive Feedback with Decay and Saturation ‣ 2 The Model ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets") but gradually saturates when hedging demand grows and balance-sheet exhausted. It is smooth and avoids an artificial hard cap and abrupt changes that aligns with the idea form Avellaneda–Stoikov framework[avellaneda2008].

With this, the stock price evolution is modeled as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​St+1=μt​St+I​(λt​Nt​Γt​ϕ​(xt))​Δ​St,\Delta S\_{t+1}=\mu\_{t}S\_{t}+I\!\big(\lambda\_{t}N\_{t}\Gamma\_{t}\phi(x\_{t})\big)\,\Delta S\_{t}, |  | (17) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | St+1=St+Δ​St+1,S\_{t+1}=S\_{t}+\Delta S\_{t+1}, |  | (18) |

where λt\lambda\_{t} is the hedging impact coefficient and ϕ​(xt)\phi(x\_{t}) captures beta-adjusted amplification based on the normalized price surprise,

|  |  |  |  |
| --- | --- | --- | --- |
|  | xt=|Δ​Stobs|/Stβ​σm.x\_{t}=\frac{|\Delta S\_{t}^{\mathrm{obs}}|/S\_{t}}{\beta\sigma\_{m}}. |  | (19) |

The term μt​St\mu\_{t}S\_{t} represents exogenous or semi-endogenous shocks to price (e.g., initial option-driven imbalance). Following the initial disturbance, we model μt\mu\_{t} as proportional to the remaining active hedging pressure:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μt=μ0​NtN0,\mu\_{t}=\mu\_{0}\frac{N\_{t}}{N\_{0}}, |  | (20) |

so that new shocks gradually diminish as market-maker activity decays in proportion to realized cumulative movement.

Equation ([17](https://arxiv.org/html/2511.22766v1#S2.E17 "In 2.4 Dynamic Beta-Normalized Recursive Feedback with Decay and Saturation ‣ 2 The Model ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets")) describes a coupled recursive feedback loop in which price shocks propagate through market-maker adjustments and cumulative movement–driven decay of option exposure.

### 2.5 Stochastic Extension of Position Dynamics

In previous section, we modeled the dynamic response of market maker’s delta-neutral hedging with multiple feedback loops to the original surprise and active option size is gradually decayed by time without accounting the new incoming options. Now, we further extend that model with a stochastic imcoing of new options.

We can assume that after the initial large size option that triggers a gamma-squeeze event, a stochastic incoming of νt\nu\_{t} with the deterministic decaying NtN\_{t}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | N¯t=Nt+νt,\bar{N}\_{t}=N\_{t}+\nu\_{t}, |  | (21) |

Empirical evidence shows that option order flow exhibits persistence due to algorithmic execution,
inventory smoothing, and clustered retail activity [PanPoteshman2006].

Thus, we can assume that νt\nu\_{t} evolves as a state-dependent autoregressive process:

|  |  |  |  |
| --- | --- | --- | --- |
|  | νt+1=ρ​νt+σN​Nt​εt,εt∼𝒩​(0,1),|ρ|<1.\nu\_{t+1}=\rho\,\nu\_{t}+\sigma\_{N}\,N\_{t}\,\varepsilon\_{t},\qquad\varepsilon\_{t}\sim\mathcal{N}(0,1),\;|\rho|<1. |  | (22) |

The coefficient ρ\rho controls short-term persistence, while σN\sigma\_{N} governs the volatility of random deviations relative to the current exposure level NtN\_{t}.

To prevent unreasonable values of opening option size, we impose a one–sided censoring rule and define the effective exposure as

|  |  |  |  |
| --- | --- | --- | --- |
|  | N¯t=min⁡{max⁡{N¯t, 0},N¯}.\bar{N}\_{t}=\min\!\big\{\,\max\{\,\bar{N}\_{t},\,0\,\},\,\overline{N}\big\}. |  | (23) |

The lower bound enforces the standard no-short-inventory limit, while N¯\overline{N} acts as a conservative upper reference level derived from the stationary dispersion of the AR(1) deviation process:

|  |  |  |  |
| --- | --- | --- | --- |
|  | N¯=N0+κ​σN​N01−ρ2,κ=8.\overline{N}=N\_{0}+\kappa\,\frac{\sigma\_{N}N\_{0}}{\sqrt{1-\rho^{2}}},\qquad\kappa=8. |  | (24) |

This upper bound
serves as a conservative numerical safeguard that
prevents the AR(1)–driven deviations from generating unbounded trajectories in
the early stages of the simulation.
Varying κ\kappa within a wide range produces negligible changes in the simulated paths, confirming that the upper bound plays only a technical role in maintaining well-posed recursion and that the cap is effectively non-binding under realistic conditions.
The stochastic hybrid specification allows for temporary expansion of exposure early in the squeeze, while preserving convergence toward stability in later stages.
As cumulative movement builds and NtN\_{t} decays, the effective variance collapses, restoring smooth dynamics.
The model therefore reproduces both the explosive and the self-damping phases of gamma-induced price dislocation within a single, tractable recursive structure.

It is worth noting that the proposed stochastic model can be readily adapted to incorporate empirical market data. For example, the synthetic shocks and arrivals used in the simulations can be replaced by realized option-flow metrics or volatility-surface dynamics extracted from option transaction data. The stochastic component νt\nu\_{t} may be extracted directly from opening new incoming option size.
Meanwhile, from an econometric perspective, the structural parameters λt\lambda\_{t}, Γt\Gamma\_{t}, η\eta, and ξ\xi,
can be estimated or back-fitted using observed returns and option-flow series.
In sum, this recursive architecture connects theoretical amplification dynamics with data-driven calibration, offering a tractable empirical approach to study how real-world option positioning propagates into price instability. The framework is therefore ready for direct empirical implementation once market-based estimates of λt\lambda\_{t}, Γt\Gamma\_{t}, and NtN\_{t} are available.

## 3 Stability and Bifurcation Structure

This section connects the gamma-feedback mechanism to the formal stability
condition associated with the denominator DiD\_{i} in Equation [11](https://arxiv.org/html/2511.22766v1#S2.E11 "In 2.3 Combined Gamma-Beta Model and Proposition ‣ 2 The Model ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets").
The singularity Di→0D\_{i}\to 0 introduced earlier as the onset of a
gamma-squeeze event is shown to coincide with a stability loss in both the
static price–impact map and the recursive feedback dynamics.
The resulting threshold defines a codimension-one bifurcation surface in
(λ,G,β)(\lambda,G,\beta)-space.

### 3.1 Static stability of the price-impact map

Under the linear impact specification of Section [2.3](https://arxiv.org/html/2511.22766v1#S2.SS3 "2.3 Combined Gamma-Beta Model and Proposition ‣ 2 The Model ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets"), substituting
the delta-hedging relation of Equation [8](https://arxiv.org/html/2511.22766v1#S2.E8 "In 2.1 Formal Gamma-Squeeze Derivation via Delta-Neutral Hedging ‣ 2 The Model ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets") yields the closed-form
response

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​St=μ​StDi,\Delta S\_{t}=\frac{\mu S\_{t}}{D\_{i}}, |  | (25) |

where Di=1−λ​G​ϕ​(xi)D\_{i}=1-\lambda G\phi(x\_{i}).
When Di>0D\_{i}>0 the response is locally proportional to the initiating shock,
whereas Di→0D\_{i}\to 0 produces an unbounded linear amplification.
The static gamma-squeeze threshold therefore corresponds to

|  |  |  |  |
| --- | --- | --- | --- |
|  | Di=0⟺λ​G​ϕ​(xi)=1,D\_{i}=0\quad\Longleftrightarrow\quad\lambda G\phi(x\_{i})=1, |  | (26) |

which defines a codimension-one instability boundary.

### 3.2 Local stability of the recursive map

To relate the static condition to the dynamic model in
Equation [17](https://arxiv.org/html/2511.22766v1#S2.E17 "In 2.4 Dynamic Beta-Normalized Recursive Feedback with Decay and Saturation ‣ 2 The Model ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets"), we freeze the slowly varying
quantities (St,Nt,Γt,λt)(S\_{t},N\_{t},\Gamma\_{t},\lambda\_{t}) at initial values and obtain the
affine one-dimensional map

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​St+1=a+F​Δ​St,a=μ0​S0,F=I​(λ​N0​Γ0​ϕ​(x0)),\Delta S\_{t+1}=a+F\Delta S\_{t},\qquad a=\mu\_{0}S\_{0},\quad F=I\!\big(\lambda N\_{0}\Gamma\_{0}\phi(x\_{0})\big), |  | (27) |

from which the fixed point

|  |  |  |
| --- | --- | --- |
|  | Δ​S∗=a1−F\Delta S^{\*}=\frac{a}{1-F} |  |

is stable when

|  |  |  |  |
| --- | --- | --- | --- |
|  | |F|<1.|F|<1. |  | (28) |

In the linear-impact case I​(y)=yI(y)=y, the feedback factor becomes
F=λ​G0​ϕ​(x0)F=\lambda G\_{0}\phi(x\_{0}), and ([28](https://arxiv.org/html/2511.22766v1#S3.E28 "In 3.2 Local stability of the recursive map ‣ 3 Stability and Bifurcation Structure ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets")) reduces to

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ​G0​ϕ​(x0)<1,\lambda G\_{0}\phi(x\_{0})<1, |  | (29) |

which is identical to the static threshold ([26](https://arxiv.org/html/2511.22766v1#S3.E26 "In 3.1 Static stability of the price-impact map ‣ 3 Stability and Bifurcation Structure ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets")).
Thus the classical gamma-squeeze denominator DiD\_{i} also governs the
eigenvalue of the price-impact recursion.

### 3.3 Fast-subsystem stability and the role of decay

According Equation [17](https://arxiv.org/html/2511.22766v1#S2.E17 "In 2.4 Dynamic Beta-Normalized Recursive Feedback with Decay and Saturation ‣ 2 The Model ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets"), the map (St,Δ​St,Nt)↦(St+1,Δ​St+1,Nt+1)(S\_{t},\Delta S\_{t},N\_{t})\mapsto(S\_{t+1},\Delta S\_{t+1},N\_{t+1}) is generally non-autonomous, but over short horizons
the slow variables (St,Nt,Γt)(S\_{t},N\_{t},\Gamma\_{t}) evolve much more gradually than Δ​St\Delta S\_{t}.
We therefore analyze the fast subsystem obtained by treating (St,Nt,Γt,λt)(S\_{t},N\_{t},\Gamma\_{t},\lambda\_{t})
as quasi-static parameters. and macro-finance.
Setting Δ​St+1=Δ​St=Δ​S∗=0\Delta S\_{t+1}=\Delta S\_{t}=\Delta S^{\*}=0 we get,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​S∗​(1−F​(Δ​S∗))=μt​St,\Delta S^{\*}\big(1-F(\Delta S^{\*})\big)=\mu\_{t}S\_{t}, |  | (30) |

where

|  |  |  |
| --- | --- | --- |
|  | F​(Δ​S)=I​(λt​Nt​Γt​ϕ​(x)).F(\Delta S)=I\!\big(\lambda\_{t}N\_{t}\Gamma\_{t}\,\phi(x)\big). |  |

The economically natural equilibrium arises when the initiating shock vanishes,

|  |  |  |
| --- | --- | --- |
|  | μt​St=0⇒Δ​S∗=0.\mu\_{t}S\_{t}=0\quad\Rightarrow\quad\Delta S^{\*}=0. |  |

We now assess stability of the fixed point Δ​S∗=0\Delta S^{\*}=0.

Linearizing Equation [17](https://arxiv.org/html/2511.22766v1#S2.E17 "In 2.4 Dynamic Beta-Normalized Recursive Feedback with Decay and Saturation ‣ 2 The Model ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets") at Δ​St=0\Delta S\_{t}=0
gives a local feedback coefficient

|  |  |  |  |
| --- | --- | --- | --- |
|  | F0=I​(λt​Nt​Γt),F\_{0}=I\!\big(\lambda\_{t}N\_{t}\Gamma\_{t}\big), |  | (31) |

The fixed point Δ​S∗=0\Delta S^{\*}=0 is locally asymptotically stable if and only if

|  |  |  |
| --- | --- | --- |
|  | |F0|<1,|F\_{0}|<1, |  |

since the linearized map is Δ​St+1=F0​Δ​St\Delta S\_{t+1}=F\_{0}\Delta S\_{t}, a one-dimensional linear system with its stability requires |F0|<1|F\_{0}|<1.

### 3.4 Bifurcation structure

In the linear-impact benchmark I​(y)=c​yI(y)=cy and with fixed exposure G0=N0​Γ0G\_{0}=N\_{0}\Gamma\_{0},
the fast subsystem reduces to the affine one-dimensional map.

The equilibrium Δ​S∗=0\Delta S^{\*}=0 (for μ0​S0=0\mu\_{0}S\_{0}=0) is linearly stable if
|F0|<1|F\_{0}|<1 and loses stability as F0F\_{0} crosses the unit circle.
In particular, the fixed point undergoes a classical flip (period-doubling)
bifurcation at F0=−1F\_{0}=-1, while loss of stability relevant for gamma squeezes
occurs as F0↗1F\_{0}\nearrow 1.

Expressed in terms of the original parameters, the associated threshold is

|  |  |  |
| --- | --- | --- |
|  | λ​G0​ϕ​(x0,β)=1,\lambda G\_{0}\,\phi(x\_{0},\beta)=1, |  |

which coincides with the static singularity of the gamma-feedback denominator
Di=1−λ​G​ϕ​(xi)D\_{i}=1-\lambda G\phi(x\_{i}).
The corresponding bifurcation surface in parameter space can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℬ={(λ,G,β): 1−λ​G​ϕ​(x)=0},\mathcal{B}=\Big\{(\lambda,G,\beta)\;:\;1-\lambda G\,\phi(x)=0\Big\}, |  | (32) |

separating a weak-feedback region (Di>0D\_{i}>0, small amplification) from the
strong-feedback regime (Di≈0D\_{i}\approx 0) associated with extreme sensitivity
to shocks. In this linear benchmark, crossing ℬ\mathcal{B} would lead to
unbounded divergence of Δ​St\Delta S\_{t}.

### 3.5 Impact of saturation and self-limitation

The full model replaces linear impact with a saturating response
I​(y)=tanh⁡(c​y)I(y)=\tanh(cy). In this case the effective feedback coefficient

|  |  |  |
| --- | --- | --- |
|  | Ft=I​(λ​Gt​ϕ​(xt))F\_{t}=I\!\big(\lambda G\_{t}\,\phi(x\_{t})\big) |  |

is bounded in magnitude, with

|  |  |  |
| --- | --- | --- |
|  | tanh⁡(c​y)→1as​y→∞.\tanh(cy)\to 1\quad\text{as}\;y\to\infty. |  |

Thus, the strict divergence implied by the linear benchmark for F0>1F\_{0}>1
is replaced by large but finite excursions: as the system is pushed toward
the instability surface ℬ\mathcal{B}, the impact function saturates and
FtF\_{t} remains confined to (−1,1)(-1,1).

At the same time, the effective exposure Gt=Nt​ΓtG\_{t}=N\_{t}\Gamma\_{t} decays
endogenously as cumulative price movement increases. Early in a squeeze
we have Gt≈G0G\_{t}\approx G\_{0} and the dynamics are well approximated by the
linear threshold Di=0D\_{i}=0. As the episode unfolds and realized moves
accumulate, NtN\_{t} shrinks, GtG\_{t} falls, and the product
λ​Gt​ϕ​(xt)\lambda G\_{t}\,\phi(x\_{t}) is driven back below the instability
boundary. The combined effect of saturation and exposure decay therefore
produces a self-limiting mechanism: shocks can trigger large transient
amplification when parameters lie near ℬ\mathcal{B}, but the dynamics
remain bounded and eventually return to the stable regime.

## 4 Numerical Simulation and Illustrative Results

### 4.1 Stability Denominator DiD\_{i} and Extreme-Event Visualization

To provide a concrete illustration of the beta-dependent gamma feedback model introduced in Section [2](https://arxiv.org/html/2511.22766v1#S2 "2 The Model ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets"), we simulate the stability denominator DiD\_{i} over a finely discretized grid of stock betas (β\beta) and total gamma exposures (GG), holding the hedging sensitivity λ\lambda and the exogenous price shock Δ​S/S\Delta S/S fixed. The resulting heatmap, presented in Figure [1](https://arxiv.org/html/2511.22766v1#S4.F1 "Figure 1 ‣ 4.1 Stability Denominator 𝐷_𝑖 and Extreme-Event Visualization ‣ 4 Numerical Simulation and Illustrative Results ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets")(a), shows a continuous mapping of DiD\_{i} across the parameter space, with overlaid contour lines highlighting critical thresholds.
The black dashed line at Di=0D\_{i}=0 formally delineates the onset of instability, where the market-maker’s delta-hedging can amplify even modest shocks into rapid price escalation. This figure directly illustrates the theoretical stability condition derived in Section [2.3](https://arxiv.org/html/2511.22766v1#S2.SS3 "2.3 Combined Gamma-Beta Model and Proposition ‣ 2 The Model ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets"), which affirms findings link to the previous model to observable parameter combinations [garleanu2007, brunnermeier2009].

It confirms that Stocks with low systematic risk (β\beta) exhibit higher relative surprise for a given absolute shock as the same price move represents a larger deviation relative to typical fluctuations. Meanwhile, it also reveals total gamma exposure GG modulates the magnitude of feedback: larger gamma positions correspond to smaller DiD\_{i}, consistent with stronger delta-hedging-induced amplification [garleanu2011].

|  |  |
| --- | --- |
| Refer to caption | Refer to caption |
| (a) | (b) |

Figure 1: 
(a) Stability map of market-maker feedback dynamics. Color intensity represents the stability denominator DiD\_{i}, with warmer colors corresponding to higher stability. The black dashed line indicates the critical threshold Di=0D\_{i}=0, where even small exogenous shocks can produce disproportionately large price movements.
(b) Extreme-event amplification and stability contours. The red dash-dotted line indicates amplification ≥2\geq 2, while the black dashed line denotes the critical stability boundary Di=0D\_{i}=0. These contours reveal regions of pronounced gamma feedback and potential instability.

Next, we investigate extreme-event dynamics in the market-maker feedback model, focusing on regions where amplification is particularly pronounced and where stability may be compromised. Specifically, we examine regions in the parameter space where the amplification ratio Δ​St/Δ​S0\Delta S\_{t}/\Delta S\_{0} exceeds 2, highlighting scenarios in which small initial price shocks are significantly magnified due to feedback from gamma hedging. Concurrently, we consider the contour where the stability denominator DiD\_{i} approaches zero, identifying combinations of parameters at the boundary of instability beyond which the model predicts potential divergence in hedging feedback.

Similarly, we generate a heatmap of amplification across β\beta and Γ\Gamma for a representative hedging sensitivity (λ=0.003\lambda=0.003) and shock magnitude (Δ​S0=0.05\Delta S\_{0}=0.05). The heatmap is overlaid with two key contours: a red dash-dotted line marking amplification greater than or equal to 2, and a black dashed line representing Di=0D\_{i}=0.

Figure [1](https://arxiv.org/html/2511.22766v1#S4.F1 "Figure 1 ‣ 4.1 Stability Denominator 𝐷_𝑖 and Extreme-Event Visualization ‣ 4 Numerical Simulation and Illustrative Results ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets")(b) shows that extreme amplification occurs primarily at low values of β\beta combined with moderate-to-high gamma exposure Γ\Gamma. This observation aligns with the intuition that low market impact sensitivity and high gamma exposure amplify feedback effects. The Di=0D\_{i}=0 contour runs close to the amplification threshold, indicating that scenarios with extreme price amplification are often near the boundary of instability.

It also reveals that regions of high amplification (e.g., Δ​St/Δ​S0≥2\Delta S\_{t}/\Delta S\_{0}\geq 2) often coincide with or lie near the Di=0D\_{i}=0 contour. This alignment underscores the predictive value of the stability denominator in identifying zones of potential market instability. Lastly, the sensitivity of amplification to small variations in β\beta or GG suggests that even minor changes in market conditions could trigger significant price movements, consistent with observed phenomena in gamma squeezes and other short-term volatility spikes.

### 4.2 Time-Series Amplification Dynamics Due to Initial Hedging

In this section, we examine the initial delta-neutral hedging of market-maker to the shock and how that impact the stock price without recursive feedback.
Here, we set the initial price as S0=100S\_{0}=100 such that the stock price movement can be checked later without loss of generality. We set λ=0.05\lambda=0.05, G=200G=200 that resembles a common stock in market.
We compute Δ​St=μ​St+λ​G​Δ​St​ϕ​(xi)\Delta S\_{t}=\mu S\_{t}+\lambda G\Delta S\_{t}\,\phi(x\_{i}) iteratively over time as a one-time only hedging reaction.

Figure [2](https://arxiv.org/html/2511.22766v1#S4.F2 "Figure 2 ‣ 4.2 Time-Series Amplification Dynamics Due to Initial Hedging ‣ 4 Numerical Simulation and Illustrative Results ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets") shows the stock price response to different levels of initial μt\mu\_{t} shocks values μt=0.005,0.01,0.015,0.02,0.025\mu\_{t}=0.005,0.01,0.015,0.02,0.025.
It can be seen that a one-time delta-neutral hedging causes a sharp price rise in the underlying stock, followed by a plateau.
A larger shock leads to a more aggressive hedging, which in turn, increases the price more significantly.
Such behavior is consistent with the notion of a static initial trigger, where the price reacts to the immediate hedging demand but does not yet incorporate the recursive effects that can further amplify the stock movement.

![Refer to caption](x3.png)


Figure 2: Time-series response to initial μt\mu\_{t} shocks, using the first-step market impact.
Stock price changes are computed according to
Δ​St=μ​St+λ​G​Δ​St​ϕ​(xi)\Delta S\_{t}=\mu S\_{t}+\lambda G\Delta S\_{t}\,\phi(x\_{i}), applied iteratively to visualize the trajectory.
Different curves correspond to different shock values μt\mu\_{t}.

Then, we keep the shock μ=0.025\mu=0.025 and varies β\beta from 0.5−30.5-3 to check the price behavior of different stocks under the same level of “surprise”. Figure [3](https://arxiv.org/html/2511.22766v1#S4.F3 "Figure 3 ‣ 4.2 Time-Series Amplification Dynamics Due to Initial Hedging ‣ 4 Numerical Simulation and Illustrative Results ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets") displays the resulting price paths.
Although each curve corresponds to the same underlying shock, the magnitude of the
initial price jump varies systematically with β\beta. It can be seen that the same hedging leads to a shaper price change with respect to stock with lower β\beta, which is consistent with analysis.

![Refer to caption](x4.png)


Figure 3: Time-series response to a fixed initial shock μ=0.025\mu=0.025 under
varying levels of β\beta.
Lower-β\beta stocks perceive the same absolute price change as a larger
normalized surprise, yielding stronger hedging demand and a larger initial
price displacement. The trajectories reflect only the one-time
delta-neutral hedge and therefore plateau after the initial jump.

### 4.3 Simulation of Deterministic Recursive Feedback Dynamics

Building on the dynamic framework introduced in Section [2.4](https://arxiv.org/html/2511.22766v1#S2.SS4 "2.4 Dynamic Beta-Normalized Recursive Feedback with Decay and Saturation ‣ 2 The Model ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets"), we now conduct numerical simulations to analyze the nonlinear price dynamics arising from recursive hedging feedback.
The market volatility parameter is set to σm=0.03\sigma\_{m}=0.03 which corresponds to the averaged market volatility level.

![Refer to caption](x5.png)


Figure 4: Simulated stock price trajectories under recursive feedback with cumulative position decay and saturating impact.
Larger initial shocks produce steeper early-stage amplification, while cumulative decay of NtN\_{t} and saturation of I​(⋅)I(\cdot) gradually dampen recursive growth, leading to a stable plateau.

First, we check the price response to multiple initial shock magnitudes μ0∈{0.005,0.01,0.015,0.02,0.025}\mu\_{0}\in\{0.005,0.01,0.015,0.02,0.025\} with β=1\beta=1, η=2\eta=2, and ξ=5\xi=5, respectively.
Figure [4](https://arxiv.org/html/2511.22766v1#S4.F4 "Figure 4 ‣ 4.3 Simulation of Deterministic Recursive Feedback Dynamics ‣ 4 Numerical Simulation and Illustrative Results ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets") illustrates the stock price evolution under multiple exogenous shocks μt\mu\_{t}, demonstrating how recursive hedging amplifies price movements through nonlinear feedback and saturation.
Early in the process, recursive hedging induces rapid, nonlinear amplification of prices-consistent with the explosive onset of a squeeze event.
As both NtN\_{t} and μt\mu\_{t} decay via cumulative exposure effects, the effective feedback term weakens, and the dynamics transition toward a damped, quasi-stable regime.
The figure also highlights the role of nonlinear saturation and position limits, which prevent unbounded growth even under strong hedging pressure.

In contrast to Figure [2](https://arxiv.org/html/2511.22766v1#S4.F2 "Figure 2 ‣ 4.2 Time-Series Amplification Dynamics Due to Initial Hedging ‣ 4 Numerical Simulation and Illustrative Results ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets"), where only single-step hedging was considered, the recursive inclusion of beta-adjusted feedback in this simulation produces sustained, exponential-like growth before eventual stabilization. Figure [5](https://arxiv.org/html/2511.22766v1#S4.F5 "Figure 5 ‣ 4.3 Simulation of Deterministic Recursive Feedback Dynamics ‣ 4 Numerical Simulation and Illustrative Results ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets") shows that cross-sectional differences in β\beta
produce visible divergence at the onset of the shock: lower-β\beta stocks display sharper upward
movement because an identical surprise constitutes a larger normalized surprise xix\_{i},
leading to stronger initial delta-neutral hedging pressure.
As the system evolves, however, the recursive feedback loop combined with inventory decay and the
bounded impact function I​(y)I(y), progressively dominates the dynamics.

![Refer to caption](x6.png)


Figure 5: 
Time-series trajectories of stock prices under recursive hedging feedback for varying
β\beta values, given a fixed initial shock μ0=0.025\mu\_{0}=0.025.
Lower-β\beta stocks exhibit a stronger initial displacement, as the same absolute shock
corresponds to a larger normalized surprise xix\_{i}, triggering more aggressive hedging.
The inset highlights the early-stage divergence, while the long-run trajectories converge
as saturation and inventory decay dominate the dynamics.

This behavior provides a structural explanation for why many existing models treat stocks with
different β\beta values as exhibiting similar responses under option-driven feedback: the endogenous market mechanism reacts quickly to overwhelms the early
cross-sectional divergence.
However,
in early stage of gamma-squeeze event, low-beta stocks still experience disproportionately strong amplification before the market mechanism reasserts dominance.

### 4.4 Simulation of Recursive Feedback under Stochastic Option Exposure

In this section, we extend our simulation for a stochastic model.
Changing the NtN\_{t} by N¯t\bar{N}\_{t} in Equation ([17](https://arxiv.org/html/2511.22766v1#S2.E17 "In 2.4 Dynamic Beta-Normalized Recursive Feedback with Decay and Saturation ‣ 2 The Model ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets")), we get:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​St+1=μt​St+I​(λt​N¯t​Γt​ϕ​(xt))​Δ​St,\Delta S\_{t+1}=\mu\_{t}S\_{t}+I\!\big(\lambda\_{t}\bar{N}\_{t}\Gamma\_{t}\,\phi(x\_{t})\big)\,\Delta S\_{t}, |  | (33) |

Firstly, we will check the the a state-dependent autoregressive process of stochastic incoming options in Equation [22](https://arxiv.org/html/2511.22766v1#S2.E22 "In 2.5 Stochastic Extension of Position Dynamics ‣ 2 The Model ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets"). Meanwhile, as noted in Section [2.5](https://arxiv.org/html/2511.22766v1#S2.SS5 "2.5 Stochastic Extension of Position Dynamics ‣ 2 The Model ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets"), the recursive framework is designed to accept
empirical option-flow series or volatility-surface data like λt\lambda\_{t} and Γt\Gamma\_{t} as exogenous drivers.
In the absence of such data, we illustrate this “plug-in” capability using a
synthetic example with event-driven option arrivals with random spikes νt\nu\_{t} short-lived amplifications in the price trajectories. Specifically, at randomly selected discrete times t∈𝒯spikest\in\mathcal{T}\_{\text{spikes}},
the exposure receives an additive increment νt∼U​(0, 0.3​N0)\nu\_{t}\sim U(0,\,0.3N\_{0}) (with UU being a uniform distribution), while νt=0\nu\_{t}=0 otherwise. All the simulation parameters remain the same as previous section with the stochastic component ρ=0.9,σN=0.2.\rho=0.9,\ \sigma\_{N}=0.2.

Figure [6](https://arxiv.org/html/2511.22766v1#S4.F6 "Figure 6 ‣ 4.4 Simulation of Recursive Feedback under Stochastic Option Exposure ‣ 4 Numerical Simulation and Illustrative Results ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets") shows simulated price trajectories under the stochastic hybrid model.
Relative to the deterministic case (Figure [4](https://arxiv.org/html/2511.22766v1#S4.F4 "Figure 4 ‣ 4.3 Simulation of Deterministic Recursive Feedback Dynamics ‣ 4 Numerical Simulation and Illustrative Results ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets")), stochastic deviations in N¯t\bar{N}\_{t} produce brief secondary accelerations (“ripples”) early in the squeeze when exposure is still large.

The stochastic trajectories retain the characteristic two-phase pattern: an initial explosive amplification followed by gradual stabilization.
However, small fluctuations around the baseline path highlight how the incoming options temporarily impact the underlying stock prices.

Figure [7](https://arxiv.org/html/2511.22766v1#S4.F7 "Figure 7 ‣ 4.4 Simulation of Recursive Feedback under Stochastic Option Exposure ‣ 4 Numerical Simulation and Illustrative Results ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets") shows the simulated price trajectories under synthetic random arrivals νt\nu\_{t}.
Although each inflow represents at most 30%30\% of N0N\_{0}, these discrete perturbations induce short-lived secondary amplifications superimposed on the decaying price path.
The nonlinear feedback mechanism magnifies even modest synthetic arrivals, generating visible deviations in StS\_{t} analogous to transient “gamma ignition” episodes observed in real markets.

![Refer to caption](x7.png)


Figure 6: Stochastic recursive feedback with cumulative decay. Random deviations in N¯t\bar{N}\_{t} induce short-lived reactivations early in the squeeze, while cumulative decay and saturation restore stability.

The exercise confirms that the recursive structure can accommodate both continuous and discrete stochastic exposures within a unified analytical framework.
Meanwhile, this controlled extension also confirms that the recursive feedback framework is structurally flexible and empirically adaptable.

![Refer to caption](x8.png)


Figure 7: Event-driven stochastic extension with synthetic option arrivals νt\nu\_{t}.
Seventy random spikes νt∈[0,0.3​N0]\nu\_{t}\in[0,0.3N\_{0}] (blue stems, right axis) generate short-lived amplifications in the price trajectories StS\_{t} (left axis).
All other parameters follow Section [4.4](https://arxiv.org/html/2511.22766v1#S4.SS4 "4.4 Simulation of Recursive Feedback under Stochastic Option Exposure ‣ 4 Numerical Simulation and Illustrative Results ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets").

## 5 Discussion

A caveat in interpreting the static time-series experiment is that it assumes an instant, unsaturated delta-neutral hedge. This yields an upper-bound “free response,” in which the market maker lifts the price without inventory or risk limits. When contrasted with the recursive model, where exposure decays and saturation limits bind, a sharp discrepancy emerges. The unconstrained model produces strong β\beta-dependent divergence, whereas the recursive, capacity-limited system suppresses much of this cross-sectional spread. Once saturation dominates, feedback no longer scales linearly with β\beta, and the trajectories for low-β\beta and high-β\beta names converge.

This contrast highlights an important mechanism. Stronger hedging limits (larger η\eta, ξ\xi, or saturation cc) reduce the sensitivity of a gamma squeeze to underlying β\beta differences. In practical terms, well-capitalized or tightly risk-managed market makers may inadvertently reduce the visible influence of β\beta during turbulent periods. From a risk-management perspective, this suggests that robust inventory control can buffer β\beta-amplified instability and restrict the conditions under which a pronounced gamma squeeze can propagate through the cross-section.

More broadly, this attenuation of cross-sectional dispersion provides a natural explanation for why most existing studies largely overlook β\beta effects: in real markets, hedging capacity limits and saturation behavior tend to mask the very β\beta-dependent spread that the unsaturated model reveals. Consequently, the empirical prominence of β\beta is diminished unless hedging frictions are minimal or market stress forces the system into its unlimited regime.

While the present simulations rely on synthetic νt\nu\_{t} arrivals for clarity, the same recursive framework is immediately adaptable to empirical data.
As discussed in Section [2.5](https://arxiv.org/html/2511.22766v1#S2.SS5 "2.5 Stochastic Extension of Position Dynamics ‣ 2 The Model ‣ Beta-Dependent Gamma Feedback and Endogenous Volatility Amplification in Option Markets"), the stochastic component νt\nu\_{t} can be replaced with observed option-flow metrics, while λt\lambda\_{t} and Γt\Gamma\_{t} can be estimated dynamically from market microstructure data.
Thus, the model is structurally ready for calibration to actual trading environments, bridging theoretical simulation with empirical implementation.

As for limitations of current model, the framework abstracts several real-market complexities.
First, the price-impact coefficient λt\lambda\_{t} is modeled in reduced form, whereas empirical impact is known to be state-dependent and asymmetric.
Moreover, the decay rule for option exposure NtN\_{t} proxies for balance-sheet contraction but does not explicitly represent volatility targeting, or dealer optimization.

Finally, Γt\Gamma\_{t} and λt\lambda\_{t} are treated as exogenous or slow-moving despite evolving endogenously with order-flow and volatility-surface dynamics.
These simplifications do not alter the core stability insight but highlight directions for structural refinement and empirical calibration.

From a practical standpoint, the results provide quantitative guidance for risk management and hedging strategies. Traders and market participants can identify parameter regimes where feedback effects are likely to dominate, allowing for informed adjustments to position sizes, gamma exposure, or liquidity provisioning. For academic purposes, the model offers a tractable framework for exploring nonlinear feedback in derivative markets, with clear extensions possible for stochastic volatility, time-dependent hedging, or multi-asset interactions.
Future work could be further extended by empirically fitting I​()I() from real market data and adjust parameters to provide guidelines for risk managements.

## 6 Conclusion

In this study, we developed a quantitative framework to analyze market-maker feedback dynamics and amplification effects in the presence of gamma exposure, hedging sensitivity, and exogenous price shocks. A formal gamma-squeeze condition that combines classical delta-hedge mechanics with beta sensitivity has been derived. This quantitative framework,
through a combination of analytical derivations and numerical simulations, leads to a finding that low-beta, high gamma-exposure stocks are shown to be most vulnerable to endogenous volatility amplification.
These findings provide both theoretical insights and practical guidance for risk management, offering a structured approach to anticipate and mitigate destabilizing feedback effects in markets with significant derivative activity. The framework is suitable for simulation studies and empirical validation, offering both rigorous derivation and intuitive understanding.

## Appendix A. Summary of Symbols and Definitions

| Symbol | Definition / Economic Interpretation |
| --- | --- |
| StS\_{t} | Stock price at discrete time tt. |
| Δ​St\Delta S\_{t} | Incremental price change, Δ​St=St−St−1\Delta S\_{t}=S\_{t}-S\_{t-1}. |
| μt\mu\_{t} | Exogenous or semi-endogenous shock term; |
| NtN\_{t} | Active option position (option volume/exposure) decaying with cumulative movement. |
| N¯t\bar{N}\_{t} | Effective stochastic exposure: N¯t=Nt+νt\bar{N}\_{t}=N\_{t}+\nu\_{t}. |
| νt\nu\_{t} | Random incoming option exposure, |
| Γt\Gamma\_{t} | Option gamma, measuring curvature of option delta with respect to price. |
| λt\lambda\_{t} | Hedging impact coefficient capturing price sensitivity to dealer flow. |
| β\beta | Stock beta, linking idiosyncratic shocks to market-level volatility. |
| σm\sigma\_{m} | Market-level volatility |
| xtx\_{t} | Beta-normalized relative surprise: xt=|Δ​St|/(St​β​σm)x\_{t}=|\Delta S\_{t}|/(S\_{t}\beta\sigma\_{m}) |
| ϕ​(xt)\phi(x\_{t}) | Amplification function reflecting shock perception; typically ϕ=1+2​xt\phi=1+2x\_{t}. |
| I​(y)I(y) | Saturation function limiting nonlinear amplification, I​(y)=tanh⁡(c​y)I(y)=\tanh(cy). |
| η,ξ\eta,\xi | Decay parameters controlling the rate and curvature of position contraction. |
| ρ\rho | Persistence of stochastic deviations in νt\nu\_{t}. |
| σN\sigma\_{N} | Volatility scale of stochastic exposure noise. |
| GG | Total gamma exposure: G=Nt​ΓtG=N\_{t}\Gamma\_{t}. |
| DiD\_{i} | Stability denominator: Di=1−λ​G​ϕ​(xi)D\_{i}=1-\lambda G\phi(x\_{i}), threshold condition for squeeze onset. |
| TT | Simulation horizon (number of discrete time steps). |
| S0S\_{0} | Initial stock price. |

Table 1: Summary of principal symbols used in the gamma-feedback and stochastic recursive models. Only major variables necessary for model interpretation and simulation are listed.

## CRediT authorship contribution statement

Haoying Dai: conceptualization, methodology, formal analysis, writing – original draft, visualization, supervision.

## Declaration of competing interest

The author declares that there are no known competing financial interests or personal relationships that could have influenced the work reported in this paper.

## Acknowledgments

The author acknowledges independent research support provided by Eight Sigma Research, a privately operated research initiative.

## Data availability

The simulation code and data that support the findings of this study are available from the corresponding author upon reasonable request.

## Author biography

Haoying Dai received the B.S. degree in Electronics from Southeast University, Nanjing, China, in 2015, and the Ph.D. degree in Electrical and Computer Engineering from the University of Maryland, College Park, MD, USA, in 2025, where he conducted his doctoral research at the Institute for Research in Electronics and Applied Physics (IREAP). His research interests include machine learning based on microwave photonic systems and chaos prediction using machine learning algorithms. He also studies the dynamics of complex systems, including financial systems.