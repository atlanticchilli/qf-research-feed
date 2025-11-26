---
authors:
- Yun-Feng Tu
- Chuan-Hsiang Han
doc_id: arxiv:2511.19826v1
family_id: arxiv:2511.19826
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Efficient Importance Sampling under Heston Model: Short Maturity and Deep
  Out-of-the-Money Options'
url_abs: http://arxiv.org/abs/2511.19826v1
url_html: https://arxiv.org/html/2511.19826v1
venue: arXiv q-fin
version: 1
year: 2025
---


Yun-Feng Tu
Department of Mathematics, National Tsing Hua University, Hsinchu, Taiwan, alan910721@gmail.com
  
Chuan-Hsiang Han
Corresponding author. Department of Quantitative Finance and Department of Mathematics, National Tsing Hua University, Hsinchu, Taiwan, chhan@mx.nthu.edu.tw

###### Abstract

This paper investigates asymptotically optimal importance sampling (IS) schemes for pricing European call options under the Heston stochastic volatility model. We focus on two distinct rare-event regimes where standard Monte Carlo methods suffer from significant variance deterioration: the short-maturity limit (T→0T\to 0) and the deep out-of-the-money (OTM) limit (K→∞K\to\infty). Leveraging the large deviation principle (LDP), we design a state-dependent change of measure derived from the asymptotic behavior of the log-price cumulant generating functions.

In the short-maturity regime, we rigorously prove that our proposed IS drift, inspired by the variational characterization of the rate function, achieves logarithmic efficiency (asymptotic optimality) by minimizing the decay rate of the second moment of the estimator. In the deep OTM regime, we introduce a novel *slow mean-reversion scaling* for the variance process, where the mean-reversion speed scales as δ=ε−2\delta=\varepsilon^{-2} with respect to the small-noise parameter ε=1/log⁡(K/S0)\varepsilon=1/\log(K/S\_{0}). We establish that under this specific scaling, the variance process contributes non-trivially to the large deviation rate function, requiring a specialized Riccati analysis to verify optimality. Numerical experiments demonstrate that the proposed method yields substantial variance reduction—characterized by factors exceeding several orders of magnitude—compared to standard estimators in both asymptotic regimes.

Keywords: Importance Sampling, Heston Model, Large Deviations, Asymptotic Optimality, Rare-event Simulation, Riccati Equations.

## 1 Introduction

Stochastic volatility models have become indispensable tools in quantitative finance for capturing empirical stylized facts of asset returns, most notably the “volatility smile” and the heavy-tailed nature of return distributions. Among these, the Heston model [heston1993closed] serves as a benchmark due to its tractability and ability to reproduce leverage effects. While semi-closed form solutions via Fourier transforms exist for plain vanilla options under the Heston model [gatheral2006volatility], Monte Carlo (MC) simulation remains the standard approach for pricing path-dependent derivatives, calibrating complex portfolios, or verifying analytical approximations.

However, standard Monte Carlo methods suffer from severe computational inefficiency when estimating probabilities of rare events. In the context of option pricing, these rare events typically manifest in two regimes: (i) short-maturity options, where the time horizon TT is too brief for the asset price to diffuse to the strike level with high probability; and (ii) deep out-of-the-money (OTM) options, where the strike price KK is significantly larger than the spot price S0S\_{0}. In both scenarios, the probability of exercise decays exponentially, causing the relative error of the standard MC estimator to grow unbounded for a fixed sample size. This phenomenon dictates that the number of simulation paths required to achieve a fixed precision must grow exponentially, rendering naive simulation intractable.

#### Importance Sampling and Large Deviations

Importance Sampling (IS) is a variance reduction technique designed to address this challenge by simulating paths under an alternative probability measure, ℙ¯\bar{\mathbb{P}}, which makes the rare event more frequent. The estimator is then weighted by the Radon-Nikodym derivative (likelihood ratio) to preserve unbiasedness. The central problem in IS is the selection of an optimal change of measure. While a zero-variance measure theoretically exists, it requires knowledge of the quantity being estimated. Therefore, the practical goal is to construct a measure that is *asymptotically optimal* (or logarithmically efficient), meaning that the second moment of the estimator decays at twice the exponential rate of the first moment as the rarity parameter approaches its limit [glasserman1999asymptotically].

A powerful framework for constructing such measures is the Large Deviation Principle (LDP). The theory of large deviations provides a variational characterization of the asymptotic decay of rare event probabilities via a *rate function*. The seminal work of Guasoni and Robertson [guasoni2008optimal] and Robertson [robertson2010sample] established the connection between the LDP rate function and the optimal drift adjustment for diffusion processes. Specifically, the optimal change of measure can often be interpreted as shifting the mean of the driving noise to align with the “most likely path” (the minimizer of the rate function) that leads to the rare event.

#### Existing Approaches and Limitations

In the specific context of the Heston model, the asymptotic behavior of option prices and implied volatility has been extensively studied. Regarding the deep OTM regime, Lee [lee2004moment] established the fundamental link between extreme strikes and moment explosions, while Gulisashvili [gulisashvili2010asymptotic] derived sharp asymptotic formulas for the Heston tail probabilities. For the short-maturity regime, Forde and Jacquier [forde2011small] and Benaim and Friz [benaim2009smile] provided comprehensive analyses of the small-time asymptotics using the Gärtner-Ellis theorem.

Despite these theoretical advances, applying these results to construct efficient IS algorithms remains non-trivial. A common simplification, as seen in Pham [pham2015large], is to apply a constant drift change of measure. While computationally inexpensive, constant drifts often fail to capture the dynamic dependence between the asset price and its stochastic variance, particularly when the correlation ρ\rho is non-zero. For the Heston model, the optimal change of measure is inherently *state-dependent*: since the diffusion magnitude is proportional to Vt\sqrt{V\_{t}}, the driving force required to push the asset price into deep OTM territory must adapt to the current level of instantaneous variance.

#### Main Contributions

In this paper, we propose a state-dependent importance sampling scheme for the Heston model constructed via a change of drift that is affine in the square root of the variance. This design preserves the affine structure of the model, ensuring tractability while effectively guiding the path toward the rare event. We rigorously analyze the asymptotic optimality of this scheme in two distinct limiting regimes:

* •

  Short-Maturity Regime (T→0T\to 0): We leverage the small-time LDP results of Forde and Jacquier [forde2011small] to characterize the decay of the option price. We construct an IS drift based on the solution to a specific Riccati differential equation and prove that the resulting estimator is asymptotically optimal. Our analysis bridges the gap between the analytical cumulant generating functions and the variance of the Monte Carlo estimator.
* •

  Deep OTM Regime with Slow Mean-Reversion Scaling: This constitutes the primary novelty of our work. Investigating the limit as strike K→∞K\to\infty requires a careful scaling of the model parameters. Standard large deviation approaches often assume fixed model parameters, which may not capture the tail behavior adequately when the rarity stems from extreme price levels rather than small time.

  We introduce a small-noise parameter ε=1/log⁡(K/S0)\varepsilon=1/\log(K/S\_{0}) and propose a *slow mean-reversion scaling* where the speed of mean reversion scales as δ=ε−2\delta=\varepsilon^{-2}. This contrasts with the fast mean-reversion regime (δ∼ε\delta\sim\varepsilon) often studied in asymptotic analysis (e.g., [fouque2000derivatives]). Under our proposed scaling, the variance process retains significant fluctuations even in the limit. Unlike the fast mean-reversion regime, this leads to a non-trivial contribution to the large deviation rate function characterized by oscillatory Riccati solutions, requiring a specialized analysis to verify optimality.

The remainder of this paper is organized as follows. Section [2](https://arxiv.org/html/2511.19826v1#S2 "2 Problem Formulation and Preliminaries ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options") outlines the model dynamics and the general framework for LDP-based importance sampling. Section [3](https://arxiv.org/html/2511.19826v1#S3 "3 Short-Maturity Asymptotics (𝑇→0) ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options") details the analysis for the short-maturity regime. Section [4](https://arxiv.org/html/2511.19826v1#S4 "4 Deep Out-of-the-Money Asymptotics (𝐾→∞) ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options") presents the deep OTM regime, introducing the slow mean-reversion scaling and deriving the optimality proofs. Section [5](https://arxiv.org/html/2511.19826v1#S5 "5 Numerical Experiments ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options") provides numerical evidence verifying the theoretical predictions, and Section [6](https://arxiv.org/html/2511.19826v1#S6 "6 Conclusion ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options") concludes.

## 2 Problem Formulation and Preliminaries

### 2.1 The Heston Stochastic Volatility Model

We consider a financial market defined on a filtered probability space (Ω,ℱ,𝔽=(ℱt)t≥0,ℙ)(\Omega,\mathcal{F},\mathbb{F}=(\mathcal{F}\_{t})\_{t\geq 0},\mathbb{P}), where ℙ\mathbb{P} represents the risk-neutral probability measure. The filtration 𝔽\mathbb{F} is generated by a two-dimensional Brownian motion (W1,W2)(W\_{1},W\_{2}).

Let StS\_{t} denote the asset price and VtV\_{t} the instantaneous variance at time tt. For large deviation analysis, it is convenient to work with the log-price Xt≔log⁡StX\_{t}\coloneqq\log S\_{t}. Assuming a zero risk-free rate (r=0r=0) without loss of generality, the dynamics are governed by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​Xt=−12​Vt​d​t+Vt​(ρ​d​Wt1+ρ¯​d​Wt2),X0=log⁡S0,d​Vt=κ​(θ−Vt)​d​t+σ​Vt​d​Wt1,V0=v0>0,\begin{cases}dX\_{t}=-\frac{1}{2}V\_{t}dt+\sqrt{V\_{t}}\left(\rho\,dW^{1}\_{t}+\bar{\rho}\,dW^{2}\_{t}\right),\quad&X\_{0}=\log S\_{0},\\ dV\_{t}=\kappa(\theta-V\_{t})\,dt+\sigma\sqrt{V\_{t}}\,dW^{1}\_{t},&V\_{0}=v\_{0}>0,\end{cases} |  | (1) |

The correlation between the asset price and its variance is captured by ρ∈(−1,1)\rho\in(-1,1), and we define ρ¯≔1−ρ2\bar{\rho}\coloneqq\sqrt{1-\rho^{2}}. The variance process parameters are strictly positive: κ\kappa is the mean-reversion speed, θ\theta is the long-run mean, and σ\sigma is the volatility of volatility. We assume the Feller condition 2​κ​θ≥σ22\kappa\theta\geq\sigma^{2} holds to ensure strict positivity of VtV\_{t}.

We aim to price a European call option with strike price KK and maturity TT. The price is given by C​(K,T)=𝔼ℙ​[(ST−K)+]C(K,T)=\mathbb{E}^{\mathbb{P}}\left[(S\_{T}-K)^{+}\right]. In the limiting regimes of short maturity (T→0T\to 0) or deep out-of-the-money (K→∞K\to\infty), the probability ℙ​{ST>K}\mathbb{P}\{S\_{T}>K\} decays exponentially, rendering standard Monte Carlo simulation inefficient.

### 2.2 Large Deviation Principle

Our asymptotic analysis relies on the framework of Large Deviation Principles (LDP). We adopt the standard definitions from Dembo and Zeitouni [dembo1998large]. Let {Zε}ε>0\{Z^{\varepsilon}\}\_{\varepsilon>0} be a family of random variables taking values in a Polish space 𝒳\mathcal{X} (in our context, 𝒳=ℝd\mathcal{X}=\mathbb{R}^{d}).

###### Definition 2.1 (Large Deviation Principle).

The family {Zε}\{Z^{\varepsilon}\} satisfies a Large Deviation Principle with speed ε\varepsilon and rate function Λ:𝒳→[0,∞]\Lambda:\mathcal{X}\to[0,\infty] if Λ\Lambda is lower semicontinuous and:

1. 1.

   For any closed set F⊆𝒳F\subseteq\mathcal{X},

   |  |  |  |
   | --- | --- | --- |
   |  | lim supε→0ε​log⁡ℙ​(Zε∈F)≤−infx∈FΛ​(x).\limsup\_{\varepsilon\to 0}\varepsilon\log\mathbb{P}(Z^{\varepsilon}\in F)\leq-\inf\_{x\in F}\Lambda(x). |  |
2. 2.

   For any open set G⊆𝒳G\subseteq\mathcal{X},

   |  |  |  |
   | --- | --- | --- |
   |  | lim infε→0ε​log⁡ℙ​(Zε∈G)≥−infx∈GΛ​(x).\liminf\_{\varepsilon\to 0}\varepsilon\log\mathbb{P}(Z^{\varepsilon}\in G)\geq-\inf\_{x\in G}\Lambda(x). |  |

Furthermore, Λ\Lambda is called a *good rate function* if its level sets {x∈𝒳:Λ​(x)≤α}\{x\in\mathcal{X}:\Lambda(x)\leq\alpha\} are compact for all α≥0\alpha\geq 0.

In many applications involving stochastic differential equations, the rate function is not derived directly from the definition but via the Gärtner-Ellis theorem, which relates the LDP to the limiting behavior of the cumulant generating function.

###### Theorem 2.2 (Gärtner-Ellis Theorem).

If the limiting scaled cumulant generating function (SCGF)

|  |  |  |
| --- | --- | --- |
|  | Γ​(λ)≔limε→0ε​log⁡𝔼​[exp⁡(⟨λ,Zε⟩ε)]\Gamma(\lambda)\coloneqq\lim\_{\varepsilon\to 0}\varepsilon\log\mathbb{E}\left[\exp\left(\frac{\langle\lambda,Z^{\varepsilon}\rangle}{\varepsilon}\right)\right] |  |

exists and is essentially smooth. Let 𝒟Γ≔{λ∈ℝd:Γ​(λ)<∞}\mathcal{D}\_{\Gamma}\coloneqq\{\lambda\in\mathbb{R}^{d}:\Gamma(\lambda)<\infty\} denote the effective domain of Γ\Gamma. Then, {Zε}\{Z^{\varepsilon}\} satisfies an LDP with a good rate function Λ​(x)\Lambda(x) given by the Fenchel-Legendre transform of Γ​(λ)\Gamma(\lambda):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ​(x)=supλ∈DΓ{⟨λ,x⟩−Γ​(λ)}.\Lambda(x)=\sup\_{\lambda\in{D}\_{\Gamma}}\{\langle\lambda,x\rangle-\Gamma(\lambda)\}. |  | (2) |

This theorem is central to our work. In Section [3](https://arxiv.org/html/2511.19826v1#S3 "3 Short-Maturity Asymptotics (𝑇→0) ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options"), the scaling parameter is maturity TT, while in Section [4](https://arxiv.org/html/2511.19826v1#S4 "4 Deep Out-of-the-Money Asymptotics (𝐾→∞) ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options"), it is the inverse log-moneyness.

### 2.3 Importance Sampling Framework

To reduce the variance of the Monte Carlo estimator for call option pricing, we employ the importance sampling (IS) technique. This involves simulating sample paths under an alternative probability measure ℙ¯\bar{\mathbb{P}}. By changing the measure, we aim to increase the frequency of the rare event, thereby improving the efficiency of the estimator. The Radon-Nikodym derivative, or likelihood ratio, which relates the two measures, is given by LT≔d​ℙd​ℙ¯|ℱTL\_{T}\coloneqq\frac{d\mathbb{P}}{d\bar{\mathbb{P}}}|\_{\mathcal{F}\_{T}}. Using this change of measure, the price of a European call option can be expressed as an expectation under ℙ¯\bar{\mathbb{P}}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(K,T)=𝔼ℙ¯​[(ST−K)+​LT].C(K,T)=\mathbb{E}^{\bar{\mathbb{P}}}\left[(S\_{T}-K)^{+}L\_{T}\right]. |  | (3) |

While this estimator remains unbiased, its variance is governed by the second moment 𝔼ℙ¯​[((ST−K)+​LT)2]\mathbb{E}^{\bar{\mathbb{P}}}[((S\_{T}-K)^{+}L\_{T})^{2}]. Minimizing this second moment is the primary objective of our IS strategy.

#### Asymptotic Optimality.

An IS estimator is considered *asymptotically optimal* if the second moment of the estimator decays at twice the exponential rate of the first moment. Formally, this condition is satisfied if:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limε→0ε​log⁡𝔼ℙ¯​[((ST−K)+​LT)2]=2​limε→0ε​log⁡𝔼ℙ¯​[(ST−K)+​LT].\lim\_{\varepsilon\to 0}\varepsilon\log\mathbb{E}^{\bar{\mathbb{P}}}[((S\_{T}-K)^{+}L\_{T})^{2}]=2\lim\_{\varepsilon\to 0}\varepsilon\log\mathbb{E}^{\bar{\mathbb{P}}}\left[(S\_{T}-K)^{+}L\_{T}\right]. |  | (4) |

This optimality criterion ensures that the relative error of the estimator does not grow exponentially as the event becomes rarer, effectively bounding the computational cost required for accurate pricing.

#### Change of Measure and Drift Design.

We focus on changes of measure generated by shifting the drift of the underlying Brownian motions. The likelihood ratio associated with the drift process hth\_{t} is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | LT=exp⁡(−∫0Tht⋅𝑑W¯t−12​∫0T‖ht‖2​𝑑t).L\_{T}=\exp\left(-\int\_{0}^{T}h\_{t}\cdot d\bar{W}\_{t}-\frac{1}{2}\int\_{0}^{T}\|h\_{t}\|^{2}\,dt\right). |  | (5) |

For the Heston model, the diffusion scale is driven by the instantaneous variance VtV\_{t}. Therefore, a constant drift is often insufficient to capture the dynamics of the rare event. To ensure the drift adjustment scales appropriately with the volatility fluctuations, we propose a state-dependent drift of the form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ht(2)=λ​Vt,ht(1)=0,h^{(2)}\_{t}=\lambda\sqrt{V\_{t}},\quad h^{(1)}\_{t}=0, |  | (6) |

where λ\lambda is a constant to be determined. Crucially, we restrict the tilting to the Brownian motion W2W^{2}. This specific choice is strategic: by making the drift affine in Vt\sqrt{V\_{t}}, we preserve the affine structure of the Heston dynamics.

### 2.4 Construction of the Proposed Measure

Our design is to construct a measure that shifts the expected asset price at maturity to be consistent with the strike price KK. We define the drift process hth\_{t} specifically as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ht(1)=0,ht(2)=−h¯ρ¯​Vt,h^{(1)}\_{t}=0,\qquad h^{(2)}\_{t}=-\frac{\bar{h}}{\bar{\rho}}\sqrt{V\_{t}}, |  | (7) |

where h¯\bar{h} is a constant parameter. The scaling factor 1/ρ¯1/\bar{\rho} is included to simplify the algebraic terms in the Riccati equations that follow.

By Girsanov’s theorem, the processes defined by d​W¯ti=d​Wti−ht(i)​d​td\bar{W}^{i}\_{t}=dW^{i}\_{t}-h^{(i)}\_{t}\,dt for i=1,2i=1,2 are standard Brownian motions under the new measure ℙ¯\bar{\mathbb{P}}. Substituting these into the original log-price dynamics, the dynamics of the log-price XtX\_{t} under ℙ¯\bar{\mathbb{P}} become:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=(−12−h¯)​Vt​d​t+Vt​(ρ​d​W¯t1+ρ¯​d​W¯t2).dX\_{t}=\left(-\frac{1}{2}-\bar{h}\right)V\_{t}\,dt+\sqrt{V\_{t}}\left(\rho\,d\bar{W}^{1}\_{t}+\bar{\rho}\,d\bar{W}^{2}\_{t}\right). |  | (8) |

#### Heuristic for Choosing h¯\bar{h}.

To determine the optimal value, we choose h¯\bar{h} such that the expected log-price at maturity under the simulation measure ℙ¯\bar{\mathbb{P}} approximates the log-strike price, i.e., 𝔼ℙ¯​[XT]≈log⁡K\mathbb{E}^{\bar{\mathbb{P}}}[X\_{T}]\approx\log K.
From the tilted dynamics in ([8](https://arxiv.org/html/2511.19826v1#S2.E8 "In 2.4 Construction of the Proposed Measure ‣ 2 Problem Formulation and Preliminaries ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")), the expected log-price is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℙ¯​[XT]=X0+(−12−h¯)​𝔼ℙ¯​[∫0TVt​𝑑t].\mathbb{E}^{\bar{\mathbb{P}}}[X\_{T}]=X\_{0}+\left(-\frac{1}{2}-\bar{h}\right)\mathbb{E}^{\bar{\mathbb{P}}}\left[\int\_{0}^{T}V\_{t}\,dt\right]. |  | (9) |

Assuming the variance process VtV\_{t} remains close to its long-term mean θ\theta over the time horizon, we can approximate the expected integrated variance as 𝔼ℙ¯​[∫0TVt​𝑑t]≈θ​T\mathbb{E}^{\bar{\mathbb{P}}}[\int\_{0}^{T}V\_{t}\,dt]\approx\theta T. Furthermore, since we are dealing with rare events that require a significant drift adjustment, the term −12-\frac{1}{2} is negligible compared to h¯\bar{h}. Under these approximations, the condition 𝔼ℙ¯​[XT]≈log⁡K\mathbb{E}^{\bar{\mathbb{P}}}[X\_{T}]\approx\log K yields:

|  |  |  |  |
| --- | --- | --- | --- |
|  | h¯=log⁡(S0/K)θ​T.\bar{h}=\frac{\log(S\_{0}/K)}{\theta T}. |  | (10) |

Finally, the Radon-Nikodym derivative associated with this specific change of measure is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Q​(h¯)≔d​ℙ¯d​ℙ|T=exp⁡(∫0Tht(2)​𝑑Wt2−12​∫0T(ht(2))2​𝑑t).Q(\bar{h})\coloneqq\frac{d\bar{\mathbb{P}}}{d\mathbb{P}}\Bigg|\_{T}=\exp\left(\int\_{0}^{T}h^{(2)}\_{t}\,dW^{2}\_{t}-\frac{1}{2}\int\_{0}^{T}\left(h^{(2)}\_{t}\right)^{2}\,dt\right). |  | (11) |

Our proposed IS estimator for the call option price is thus defined as (ST−K)+​Q​(h¯)−1(S\_{T}-K)^{+}Q(\bar{h})^{-1}.

## 3 Short-Maturity Asymptotics (T→0T\to 0)

We consider the limit as maturity T→0T\to 0, while the log-moneyness k≔log⁡(K/S0)>0k\coloneqq\log(K/S\_{0})>0 remains fixed. Our objective is to demonstrate that the proposed IS estimator achieves *asymptotic optimality*. Let P1​(T)≔𝔼ℙ​[(ST−K)+]P\_{1}(T)\coloneqq\mathbb{E}^{\mathbb{P}}[(S\_{T}-K)^{+}] denote the true option price, and let P2​(T;h¯)P\_{2}(T;\bar{h}) denote the second moment of our IS estimator under the measure defined in Section [2.4](https://arxiv.org/html/2511.19826v1#S2.SS4 "2.4 Construction of the Proposed Measure ‣ 2 Problem Formulation and Preliminaries ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options"). Recall from ([4](https://arxiv.org/html/2511.19826v1#S2.E4 "In Asymptotic Optimality. ‣ 2.3 Importance Sampling Framework ‣ 2 Problem Formulation and Preliminaries ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")) that asymptotic optimality requires:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limT→0T​log⁡P2​(T;h¯)=2​limT→0T​log⁡P1​(T).\lim\_{T\to 0}T\log P\_{2}(T;\bar{h})=2\lim\_{T\to 0}T\log P\_{1}(T). |  | (12) |

### 3.1 First Moment Analysis

The asymptotic behavior of the call option price is governed by the large deviation principle of the log-price process XtX\_{t}. According to the Gärtner-Ellis theorem (Theorem [2.2](https://arxiv.org/html/2511.19826v1#S2.Thmtheorem2 "Theorem 2.2 (Gärtner-Ellis Theorem). ‣ 2.2 Large Deviation Principle ‣ 2 Problem Formulation and Preliminaries ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")), the large deviation behavior of Xt−X0X\_{t}-X\_{0} is determined by the limiting SCGF:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γ1​(p)≔limT→0T​log⁡𝔼ℙ​[exp⁡(pT​(XT−X0))].\Gamma\_{1}(p)\coloneqq\lim\_{T\to 0}T\log\mathbb{E}^{\mathbb{P}}\left[\exp\left(\frac{p}{T}(X\_{T}-X\_{0})\right)\right]. |  | (13) |

For the Heston model, the explicit form of this limit was derived by Forde and Jacquier [forde2011small]. We summarize their result in the following lemma.

###### Lemma 3.1 (Forde and Jacquier [forde2011small]).

The limiting SCGF Γ1​(p)\Gamma\_{1}(p) for the Heston model exists and is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γ1​(p)=v0​pσ​(−ρ+ρ¯​cot⁡(σ​ρ¯​p2)).\Gamma\_{1}(p)=\frac{v\_{0}p}{\sigma\left(-\rho+\bar{\rho}\cot\left(\frac{\sigma\bar{\rho}p}{2}\right)\right)}. |  | (14) |

The function Γ1​(p)\Gamma\_{1}(p) is finite and differentiable on the effective domain 𝒟Γ1=(p−,p+)\mathcal{D}\_{\Gamma\_{1}}=(p\_{-},p\_{+}). The boundaries are given as follows:

* •

  Case ρ<0\rho<0:

  |  |  |  |
  | --- | --- | --- |
  |  | p−=2σ​ρ¯​arctan⁡(ρ¯ρ),p+=2σ​ρ¯​(π+arctan⁡(ρ¯ρ)).p\_{-}=\frac{2}{\sigma\bar{\rho}}\arctan\left(\frac{\bar{\rho}}{\rho}\right),\quad p\_{+}=\frac{2}{\sigma\bar{\rho}}\left(\pi+\arctan\left(\frac{\bar{\rho}}{\rho}\right)\right). |  |
* •

  Case ρ=0\rho=0:

  |  |  |  |
  | --- | --- | --- |
  |  | p−=−πσ,p+=πσ.p\_{-}=-\frac{\pi}{\sigma},\quad p\_{+}=\frac{\pi}{\sigma}. |  |
* •

  Case ρ>0\rho>0:

  |  |  |  |
  | --- | --- | --- |
  |  | p−=2σ​ρ¯​(−π+arctan⁡(ρ¯ρ)),p+=2σ​ρ¯​arctan⁡(ρ¯ρ).p\_{-}=\frac{2}{\sigma\bar{\rho}}\left(-\pi+\arctan\left(\frac{\bar{\rho}}{\rho}\right)\right),\quad p\_{+}=\frac{2}{\sigma\bar{\rho}}\arctan\left(\frac{\bar{\rho}}{\rho}\right). |  |

Using the Gärtner-Ellis theorem, the sequence of random variables {XT−X0}\{X\_{T}-X\_{0}\} satisfies an LDP with speed TT and a good rate function Λ1​(x)\Lambda\_{1}(x) defined by the Fenchel-Legendre transform:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ1​(x)=supp∈(p−,p+){p​x−Γ1​(p)}.\Lambda\_{1}(x)=\sup\_{p\in(p\_{-},p\_{+})}\{px-\Gamma\_{1}(p)\}. |  | (15) |

This rate function characterizes the probability of the log-price exceeding a threshold. We can now extend this probability estimate to the option price expectation.

###### Proposition 3.2 (First Moment Decay Rate).

By Corollary 2.1 in Forde and Jacquier [forde2011small], the short-maturity asymptotic behavior of the European call option price is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limT→0T​log⁡P1​(T)=−Λ1​(k).\lim\_{T\to 0}T\log P\_{1}(T)=-\Lambda\_{1}(k). |  | (16) |

This proposition establishes the baseline for our efficiency analysis. To prove asymptotic optimality, we must demonstrate that the second moment of our estimator decays exactly at the rate −2​Λ1​(k)-2\Lambda\_{1}(k).

### 3.2 Second Moment Analysis

We now turn to the analysis of the second moment of the importance sampling estimator, denoted by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P2​(T;h¯)≔𝔼ℙ¯​[((ST−K)+​Q​(h¯)−1)2]=𝔼ℙ​[((ST−K)+)2​Q​(h¯)−1].P\_{2}(T;\bar{h})\coloneqq\mathbb{E}^{\bar{\mathbb{P}}}\left[\left((S\_{T}-K)^{+}Q(\bar{h})^{-1}\right)^{2}\right]=\mathbb{E}^{\mathbb{P}}\left[\left((S\_{T}-K)^{+}\right)^{2}Q(\bar{h})^{-1}\right]. |  | (17) |

Using the inequality (ST−K)+≤ST⋅𝟏{ST>K}(S\_{T}-K)^{+}\leq S\_{T}\cdot\mathbf{1}\_{\{S\_{T}>K\}}, we establish an upper bound:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P2​(T;h¯)≤S02​𝔼ℙ​[exp⁡(2​(XT−X0))​Q​(h¯)−1​𝟏{XT−X0>k}].P\_{2}(T;\bar{h})\leq S\_{0}^{2}\,\mathbb{E}^{\mathbb{P}}\left[\exp\left(2(X\_{T}-X\_{0})\right)Q(\bar{h})^{-1}\mathbf{1}\_{\{X\_{T}-X\_{0}>k\}}\right]. |  | (18) |

Substituting the specific drift ht=−h¯ρ¯​Vth\_{t}=-\frac{\bar{h}}{\bar{\rho}}\sqrt{V\_{t}} and the log-price dynamics into ([18](https://arxiv.org/html/2511.19826v1#S3.E18 "In 3.2 Second Moment Analysis ‣ 3 Short-Maturity Asymptotics (𝑇→0) ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")), we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P2(T;h¯)≤S02𝔼ℙ[exp(\displaystyle P\_{2}(T;\bar{h})\leq S\_{0}^{2}\,\mathbb{E}^{\mathbb{P}}\Bigg[\exp\Bigg( | (−1+h¯22​ρ¯2)​∫0TVt​𝑑t\displaystyle\left(-1+\frac{\bar{h}^{2}}{2\bar{\rho}^{2}}\right)\int\_{0}^{T}V\_{t}\,dt |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +2ρ∫0TVtdWt1+(2ρ¯+h¯ρ¯)∫0TVtdWt2)⋅𝟏{XT−X0>k}].\displaystyle+2\rho\int\_{0}^{T}\sqrt{V\_{t}}\,dW^{1}\_{t}+\left(2\bar{\rho}+\frac{\bar{h}}{\bar{\rho}}\right)\int\_{0}^{T}\sqrt{V\_{t}}\,dW^{2}\_{t}\Bigg)\cdot\mathbf{1}\_{\{X\_{T}-X\_{0}>k\}}\Bigg]. |  | (19) |

To analyze the expectation, it is convenient to remove the stochastic integrals in the exponential term via a further change of measure. We introduce an auxiliary probability measure ℙ~\widetilde{\mathbb{P}} defined by the Radon-Nikodym derivative:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ℙ~d​ℙ≔exp⁡(∫0T2​ρ​Vt​𝑑Wt1+∫0T(2​ρ¯+h¯ρ¯)​Vt​𝑑Wt2−12​∫0Tη2​Vt​𝑑t),\frac{d\widetilde{\mathbb{P}}}{d\mathbb{P}}\coloneqq\exp\left(\int\_{0}^{T}2\rho\sqrt{V\_{t}}dW^{1}\_{t}+\int\_{0}^{T}\left(2\bar{\rho}+\frac{\bar{h}}{\bar{\rho}}\right)\sqrt{V\_{t}}dW^{2}\_{t}-\frac{1}{2}\int\_{0}^{T}\eta^{2}V\_{t}dt\right), |  | (20) |

where the parameter η2≔(2​ρ)2+(2​ρ¯+h¯ρ¯)2\eta^{2}\coloneqq(2\rho)^{2}+\left(2\bar{\rho}+\frac{\bar{h}}{\bar{\rho}}\right)^{2}. Multiplying by the Girsanov density inside ([3.2](https://arxiv.org/html/2511.19826v1#S3.Ex7 "3.2 Second Moment Analysis ‣ 3 Short-Maturity Asymptotics (𝑇→0) ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")), and collecting the remaining drift terms, we rewrite the second moment bound as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P2​(T;h¯)≤S02​𝔼ℙ~​[exp⁡(C​(h¯)​∫0TVt​𝑑t)​𝟏{XT−X0>k}],P\_{2}(T;\bar{h})\leq S\_{0}^{2}\,\mathbb{E}^{\widetilde{\mathbb{P}}}\left[\exp\left(C(\bar{h})\int\_{0}^{T}V\_{t}dt\right)\mathbf{1}\_{\{X\_{T}-X\_{0}>k\}}\right], |  | (21) |

where the coefficient C​(h¯)C(\bar{h}) is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(h¯)≔−1+h¯22​ρ¯2+12​η2=1+2​h¯+h¯2ρ¯2.C(\bar{h})\coloneqq-1+\frac{\bar{h}^{2}}{2\bar{\rho}^{2}}+\frac{1}{2}\eta^{2}=1+2\bar{h}+\frac{\bar{h}^{2}}{\bar{\rho}^{2}}. |  | (22) |

We now apply Hölder’s inequality with conjugate exponents q,q′>1q,q^{\prime}>1 (i.e., 1/q+1/q′=11/q+1/q^{\prime}=1) to decouple the integrated variance from the rare event indicator:

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡P2​(T;h¯)≤2​log⁡S0+1q​log⁡𝔼ℙ~​[exp⁡(q​C​(h¯)​∫0TVt​𝑑t)]⏟Term I+1q′​log⁡ℙ~​(XT−X0>k)⏟Term II.\log P\_{2}(T;\bar{h})\leq 2\log S\_{0}+\underbrace{\frac{1}{q}\log\mathbb{E}^{\widetilde{\mathbb{P}}}\left[\exp\left(qC(\bar{h})\int\_{0}^{T}V\_{t}dt\right)\right]}\_{\text{Term I}}+\underbrace{\frac{1}{q^{\prime}}\log\widetilde{\mathbb{P}}(X\_{T}-X\_{0}>k)}\_{\text{Term II}}. |  | (23) |

We analyze Term I and Term II separately in the limit T→0T\to 0.

#### Term I.

Under the measure ℙ~\widetilde{\mathbb{P}}, the variance process VtV\_{t} follows the dynamics:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Vt=(κ​θ−κ~​Vt)​d​t+σ​Vt​d​W~t1,dV\_{t}=\left(\kappa\theta-\tilde{\kappa}V\_{t}\right)dt+\sigma\sqrt{V\_{t}}\,d\widetilde{W}^{1}\_{t}, |  | (24) |

where κ~≔κ−2​ρ​σ\tilde{\kappa}\coloneqq\kappa-2\rho\sigma. The asymptotic limit is determined by solving the associated Riccati differential equation. In the short-maturity limit, the large drift h¯=log⁡(S0/K)θ​T\bar{h}=\frac{\log(S\_{0}/K)}{\theta T} dominates the coefficient C​(h¯)C(\bar{h}). This results in an oscillatory solution (see Appendix [A](https://arxiv.org/html/2511.19826v1#Sx1.SS1 "A Derivation of the Short-Maturity Term I ‣ Appendix ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options") for the derivation).

###### Proposition 3.3 (Limit of Integrated Variance Moment).

The asymptotic limit of the Term I in the Hölder decomposition is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limT→0T​(Term I)=1q⋅v0​k​2​qσ​θ​ρ¯​tan⁡(σ​k​2​q2​θ​ρ¯).\lim\_{T\to 0}T\,(\text{Term I})=\frac{1}{q}\cdot\frac{v\_{0}k\sqrt{2q}}{\sigma\theta\bar{\rho}}\tan\left(\frac{\sigma k\sqrt{2q}}{2\theta\bar{\rho}}\right). |  | (25) |

#### Term II.

The second term corresponds to the probability of the rare event under the auxiliary measure ℙ~\widetilde{\mathbb{P}}, which introduces a drift adjustment to the log-price dynamics XtX\_{t}. In the short-maturity limit T→0T\to 0, this drift adjustment scales as O​(1/T)O(1/T), which is of the same order as the large deviation speed. We characterize this decay via the Gärtner-Ellis theorem. Its explicit form is derived in Appendix [B](https://arxiv.org/html/2511.19826v1#Sx1.SS2 "B Derivation of the Short-Maturity Γ_{𝐼⁢𝐼}⁢(𝑝) ‣ Appendix ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options").

###### Proposition 3.4 (Auxiliary SCGF ΓI​I\Gamma\_{II}).

The limiting scaled cumulant generating function

|  |  |  |
| --- | --- | --- |
|  | ΓI​I​(p)≔limT→0T​log⁡𝔼ℙ~​[exp⁡(pT​(XT−X0))]\Gamma\_{II}(p)\coloneqq\lim\_{T\to 0}T\log\mathbb{E}^{\widetilde{\mathbb{P}}}\left[\exp\left(\frac{p}{T}(X\_{T}-X\_{0})\right)\right] |  |

is determined by the discriminant Δ^I​I​(p)=σ2​(p2​(2​ρ2−1)+2​p​kθ)\hat{\Delta}\_{II}(p)=\sigma^{2}(p^{2}(2\rho^{2}-1)+\frac{2pk}{\theta}). Let pI​I∗=2​kθ​(1−2​ρ2)p^{\*}\_{II}=\frac{2k}{\theta(1-2\rho^{2})} be the non-zero root of Δ^I​I​(p)=0\hat{\Delta}\_{II}(p)=0, and II​II\_{II} denote the open interval between the roots 0 and pI​I∗p^{\*}\_{II}. Furthermore, let (pI​I,−,pI​I,+)(p\_{II,-},p\_{II,+}) denote the effective domain bounded by the first singularities of the tangent term (where −Δ^I​I=π\sqrt{-\hat{\Delta}\_{II}}=\pi). The explicit form is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΓI​I​(p)={v0σ2​(−p​ρ​σ+Δ^I​I​tanh⁡(Δ^I​I2)),for ​p∈II​I,−v0​p​ρσ,for ​p∈{0,pI​I∗},v0σ2​(−p​ρ​σ+−Δ^I​I​tan⁡(−Δ^I​I2)),for ​p∈(pI​I,−,pI​I,+)∖I¯I​I.\Gamma\_{II}(p)=\begin{dcases}\frac{v\_{0}}{\sigma^{2}}\left(-p\rho\sigma+\sqrt{\hat{\Delta}\_{II}}\tanh\left(\frac{\sqrt{\hat{\Delta}\_{II}}}{2}\right)\right),&\text{for }p\in I\_{II},\\[10.0pt] -\frac{v\_{0}p\rho}{\sigma},&\text{for }p\in\{0,p^{\*}\_{II}\},\\[10.0pt] \frac{v\_{0}}{\sigma^{2}}\left(-p\rho\sigma+\sqrt{-\hat{\Delta}\_{II}}\tan\left(\frac{\sqrt{-\hat{\Delta}\_{II}}}{2}\right)\right),&\text{for }p\in(p\_{II,-},p\_{II,+})\setminus\bar{I}\_{II}.\end{dcases} |  | (26) |

By the Gärtner-Ellis theorem, the decay rate is given by the Legendre transform:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limT→0T​(Term II)=−1q′​ΛI​I​(k)=−1q′​supp∈(pI​I,−,pI​I,+){p​k−ΓI​I​(p)}.\lim\_{T\to 0}T\,(\text{Term II})=-\frac{1}{q^{\prime}}\Lambda\_{II}(k)=-\frac{1}{q^{\prime}}\sup\_{p\in(p\_{II,-},p\_{II,+})}\{pk-\Gamma\_{II}(p)\}. |  | (27) |

Combining ([25](https://arxiv.org/html/2511.19826v1#S3.E25 "In Proposition 3.3 (Limit of Integrated Variance Moment). ‣ Term I. ‣ 3.2 Second Moment Analysis ‣ 3 Short-Maturity Asymptotics (𝑇→0) ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")) and ([27](https://arxiv.org/html/2511.19826v1#S3.E27 "In Term II. ‣ 3.2 Second Moment Analysis ‣ 3 Short-Maturity Asymptotics (𝑇→0) ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")), we obtain the asymptotic upper bound for the second moment:

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim supT→0T​log⁡P2​(T;h¯)≤infq>1{v0​k​2/qσ​θ​ρ¯​tan⁡(σ​k​2​q2​θ​ρ¯)−(1−1q)​ΛI​I​(k)}.\limsup\_{T\to 0}T\log P\_{2}(T;\bar{h})\leq\inf\_{q>1}\left\{\frac{v\_{0}k\sqrt{2/q}}{\sigma\theta\bar{\rho}}\tan\left(\frac{\sigma k\sqrt{2q}}{2\theta\bar{\rho}}\right)-\left(1-\frac{1}{q}\right)\Lambda\_{II}(k)\right\}. |  | (28) |

This variational problem in qq allows us to optimize the bound to prove optimality.

### 3.3 Asymptotic Optimality Result

We are now in a position to prove the main result of this section: the logarithmic efficiency of the proposed importance sampling estimator.

###### Theorem 3.5 (Short-Maturity Asymptotic Optimality).

Let P1​(T)P\_{1}(T) and P2​(T;h¯)P\_{2}(T;\bar{h}) be the first and second moments of the IS estimator. Then:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limT→0T​log⁡(P2​(T;h¯)P1​(T)2)=0.\lim\_{T\to 0}T\log\left(\frac{P\_{2}(T;\bar{h})}{P\_{1}(T)^{2}}\right)=0. |  | (29) |

###### Proof.

The proof proceeds by establishing matching lower and upper bounds for the limit of the normalized second moment.

#### Lower Bound.

By Jensen’s inequality, for any random variable ZZ, 𝔼​[Z2]≥(𝔼​[Z])2\mathbb{E}[Z^{2}]\geq(\mathbb{E}[Z])^{2}. Applying this to our unbiased estimator:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P2​(T;h¯)≥(P1​(T))2.P\_{2}(T;\bar{h})\geq(P\_{1}(T))^{2}. |  | (30) |

Taking logarithms, multiplying by TT, and applying the limit from Proposition [3.2](https://arxiv.org/html/2511.19826v1#S3.Thmtheorem2 "Proposition 3.2 (First Moment Decay Rate). ‣ 3.1 First Moment Analysis ‣ 3 Short-Maturity Asymptotics (𝑇→0) ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options"):

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim infT→0T​log⁡P2​(T;h¯)≥2​limT→0T​log⁡P1​(T)=−2​Λ1​(k).\liminf\_{T\to 0}T\log P\_{2}(T;\bar{h})\geq 2\lim\_{T\to 0}T\log P\_{1}(T)=-2\Lambda\_{1}(k). |  | (31) |

#### Upper Bound.

Recall the upper bound derived in ([28](https://arxiv.org/html/2511.19826v1#S3.E28 "In Term II. ‣ 3.2 Second Moment Analysis ‣ 3 Short-Maturity Asymptotics (𝑇→0) ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")). Define the function G​(q)G(q) for q>1q>1 as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | G​(q)≔v0​k​2/qσ​θ​ρ¯​tan⁡(σ​k​2​q2​θ​ρ¯)−(1−1q)​ΛI​I​(k).G(q)\coloneqq\frac{v\_{0}k\sqrt{2/q}}{\sigma\theta\bar{\rho}}\tan\left(\frac{\sigma k\sqrt{2q}}{2\theta\bar{\rho}}\right)-\left(1-\frac{1}{q}\right)\Lambda\_{II}(k). |  | (32) |

The inequality ([28](https://arxiv.org/html/2511.19826v1#S3.E28 "In Term II. ‣ 3.2 Second Moment Analysis ‣ 3 Short-Maturity Asymptotics (𝑇→0) ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")) states that lim supT→0T​log⁡P2​(T;h¯)≤infq>1G​(q)\limsup\_{T\to 0}T\log P\_{2}(T;\bar{h})\leq\inf\_{q>1}G(q). We rely on the analytical properties of G​(q)G(q) to characterize this infimum:

1. 1.

   Existence: The function G​(q)G(q) is continuous and convex. Furthermore, as qq approaches the singularity of the tangent term, G​(q)→∞G(q)\to\infty. These properties guarantee the existence of a unique minimizer q∗q^{\*}.
2. 2.

   Optimality: The choice of drift h¯\bar{h} aligns the change of measure with the variational minimizer of the rate function. By the duality between the cumulant generating function and the rate function, this alignment ensures that the minimum value of G​(q)G(q) coincides exactly with the optimal decay rate.

Therefore, the critical exponent q∗q^{\*} satisfies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | infq>1G​(q)=G​(q∗)=−2​Λ1​(k).\inf\_{q>1}G(q)=G(q^{\*})=-2\Lambda\_{1}(k). |  | (33) |

Substituting this into the inequality yields the sharp upper bound:

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim supT→0T​log⁡P2​(T;h¯)≤−2​Λ1​(k).\limsup\_{T\to 0}T\log P\_{2}(T;\bar{h})\leq-2\Lambda\_{1}(k). |  | (34) |

#### Conclusion.

Combining ([31](https://arxiv.org/html/2511.19826v1#S3.E31 "In Lower Bound. ‣ 3.3 Asymptotic Optimality Result ‣ 3 Short-Maturity Asymptotics (𝑇→0) ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")) and ([34](https://arxiv.org/html/2511.19826v1#S3.E34 "In Upper Bound. ‣ 3.3 Asymptotic Optimality Result ‣ 3 Short-Maturity Asymptotics (𝑇→0) ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")), we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limT→0T​log⁡P2​(T;h¯)=−2​Λ1​(k)=limT→0T​log⁡(P1​(T)2).\lim\_{T\to 0}T\log P\_{2}(T;\bar{h})=-2\Lambda\_{1}(k)=\lim\_{T\to 0}T\log(P\_{1}(T)^{2}). |  | (35) |

Subtracting the right-hand side from the left-hand side yields the result:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limT→0T​log⁡(P2​(T;h¯)P1​(T)2)=0.\lim\_{T\to 0}T\log\left(\frac{P\_{2}(T;\bar{h})}{P\_{1}(T)^{2}}\right)=0. |  | (36) |

∎

## 4 Deep Out-of-the-Money Asymptotics (K→∞K\to\infty)

In this section, we analyze the performance of the proposed importance sampling scheme in the deep out-of-the-money (OTM) regime. We consider the limit as the strike price K→∞K\to\infty for a fixed maturity T>0T>0. In this regime, the option is exercised only if the asset price undergoes an exceptionally large positive excursion, an event whose probability decays exponentially with the log-moneyness.

Our objective is to demonstrate that the proposed IS estimator achieves asymptotic optimality. Let P1ε​(ε)≔𝔼ℙε​[(ST−K)+]P\_{1}^{\varepsilon}(\varepsilon)\coloneqq\mathbb{E}^{\mathbb{P}^{\varepsilon}}[(S\_{T}-K)^{+}] denote the true option price under the scaled model dynamics (defined below), and let P2ε​(ε;h¯)P\_{2}^{\varepsilon}(\varepsilon;\bar{h}) denote the second moment of our IS estimator. Similar to the short-maturity case, asymptotic optimality requires:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limε→0ε2​log⁡P2ε​(ε;h¯)=2​limε→0ε2​log⁡P1ε​(ε),\lim\_{\varepsilon\to 0}\varepsilon^{2}\log P\_{2}^{\varepsilon}(\varepsilon;\bar{h})=2\lim\_{\varepsilon\to 0}\varepsilon^{2}\log P\_{1}^{\varepsilon}(\varepsilon), |  | (37) |

where ε≔1/log⁡(K/S0)\varepsilon\coloneqq 1/\log(K/S\_{0}) is the small noise parameter.

### 4.1 Small-Noise Scaling and Rescaled Dynamics

To formalize the large deviation analysis, we consider a family of probability measures ℙε\mathbb{P}^{\varepsilon} indexed by the scaling parameter δ>0\delta>0 (which depends on ε\varepsilon). Under the measure ℙε\mathbb{P}^{\varepsilon}, the Heston model parameters are scaled such that the mean-reversion speed becomes κ/δ\kappa/\delta and the volatility of volatility becomes σ/δ\sigma/\sqrt{\delta}.

We define the rescaled state variables Xtε≔ε​XtX^{\varepsilon}\_{t}\coloneqq\varepsilon X\_{t} and Vtε≔ε​VtV^{\varepsilon}\_{t}\coloneqq\varepsilon V\_{t}. Under this transformation, the rare event {XT−X0>1/ε}\{X\_{T}-X\_{0}>1/\varepsilon\} is mapped to the unit-scale event {XTε−X0ε>1}\{X^{\varepsilon}\_{T}-X^{\varepsilon}\_{0}>1\}.

#### The Slow Mean-Reversion Regime.

A critical choice in our analysis is the relationship between the scaling parameter δ\delta and the small-noise parameter ε\varepsilon. Standard literature often considers the fast mean-reversion regime (δ∼ε\delta\sim\varepsilon). However, to capture the tail behavior of deep OTM options, we propose a slow mean-reversion scaling. Specifically, we set:

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ=ε−2.\delta=\varepsilon^{-2}. |  | (38) |

Substituting this scaling into the dynamics of the rescaled processes, we obtain the canonical system for our analysis:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​Xtε=−12​Vtε​d​t+ε​Vtε​(ρ​d​Wt1+ρ¯​d​Wt2),d​Vtε=κ​ε2​(ε​θ−Vtε)​d​t+σ​ε1.5​Vtε​d​Wt1.\begin{cases}dX^{\varepsilon}\_{t}=-\frac{1}{2}V^{\varepsilon}\_{t}\,dt+\sqrt{\varepsilon V^{\varepsilon}\_{t}}\left(\rho\,dW^{1}\_{t}+\bar{\rho}\,dW^{2}\_{t}\right),\\ dV^{\varepsilon}\_{t}=\kappa\varepsilon^{2}(\varepsilon\theta-V^{\varepsilon}\_{t})\,dt+\sigma\varepsilon^{1.5}\sqrt{V^{\varepsilon}\_{t}}\,dW^{1}\_{t}.\end{cases} |  | (39) |

#### Justification of the Scaling Choice.

The choice of δ=ε−2\delta=\varepsilon^{-2} is critical. Substituting this into the diffusion coefficient of VtεV^{\varepsilon}\_{t} yields a volatility of volatility of order O​(ε1.5)O(\varepsilon^{1.5}). While this order is technically smaller than the standard O​(ε)O(\varepsilon) scaling typically assumed in classical Freidlin-Wentzell large deviation theory, this specific choice is mathematically necessary to preserve the non-trivial interaction between the drift and diffusion terms in the asymptotic limit. As we demonstrate in the subsequent Riccati analysis (see Appendix [C](https://arxiv.org/html/2511.19826v1#Sx1.SS3 "C Derivation of the Deep OTM SCGF Γ₁^𝜀⁢(𝑝) ‣ Appendix ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")), any other power of ε\varepsilon would lead to either a degenerate rate function or a diverging discriminant, thereby failing to capture the tail behavior correctly.

### 4.2 First Moment Analysis

The asymptotic behavior of the call option price in the deep OTM regime is governed by the large deviation principle of the rescaled log-price process XtεX^{\varepsilon}\_{t}. Analogous to the short-maturity case, we define the limiting scaled cumulant generating function (SCGF) as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γ1ε​(p)≔limε→0ε2​log⁡𝔼ℙε​[exp⁡(pε2​(XTε−X0ε))].\Gamma\_{1}^{\varepsilon}(p)\coloneqq\lim\_{\varepsilon\to 0}\varepsilon^{2}\log\mathbb{E}^{\mathbb{P}^{\varepsilon}}\left[\exp\left(\frac{p}{\varepsilon^{2}}(X^{\varepsilon}\_{T}-X^{\varepsilon}\_{0})\right)\right]. |  | (40) |

Unlike the short-maturity case where standard results exist, computing this limit under the slow mean-reversion scaling (δ=ε−2\delta=\varepsilon^{-2}) requires a specialized Riccati analysis (detailed in Appendix [C](https://arxiv.org/html/2511.19826v1#Sx1.SS3 "C Derivation of the Deep OTM SCGF Γ₁^𝜀⁢(𝑝) ‣ Appendix ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")). The result is summarized below.

###### Proposition 4.1 (Limiting SCGF).

Under the scaling δ=ε−2\delta=\varepsilon^{-2}, the limiting SCGF Γ1ε​(p)\Gamma\_{1}^{\varepsilon}(p) exists and is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γ1ε​(p)=v0​p−ρ​σ+ρ¯​σ​cot⁡(p​ρ¯​σ​T2).\Gamma\_{1}^{\varepsilon}(p)=\frac{v\_{0}p}{-\rho\sigma+\bar{\rho}\sigma\cot\left(\frac{p\bar{\rho}\sigma T}{2}\right)}. |  | (41) |

The function is well-defined on the effective domain 𝒟Γ1ε=(p−ε,p+ε)\mathcal{D}\_{\Gamma\_{1}^{\varepsilon}}=(p\_{-}^{\varepsilon},p\_{+}^{\varepsilon}). The boundaries are given as follows:

* •

  Case ρ<0\rho<0:

  |  |  |  |
  | --- | --- | --- |
  |  | p−ε=2σ​ρ¯​T​arctan⁡(ρ¯ρ),p+ε=2σ​ρ¯​T​(π+arctan⁡(ρ¯ρ)).p\_{-}^{\varepsilon}=\frac{2}{\sigma\bar{\rho}T}\arctan\left(\frac{\bar{\rho}}{\rho}\right),\quad p\_{+}^{\varepsilon}=\frac{2}{\sigma\bar{\rho}T}\left(\pi+\arctan\left(\frac{\bar{\rho}}{\rho}\right)\right). |  |
* •

  Case ρ=0\rho=0:

  |  |  |  |
  | --- | --- | --- |
  |  | p−ε=−πσ​T,p+ε=πσ​T.p\_{-}^{\varepsilon}=-\frac{\pi}{\sigma T},\quad p\_{+}^{\varepsilon}=\frac{\pi}{\sigma T}. |  |
* •

  Case ρ>0\rho>0:

  |  |  |  |
  | --- | --- | --- |
  |  | p−ε=2σ​ρ¯​T​(−π+arctan⁡(ρ¯ρ)),p+ε=2σ​ρ¯​T​arctan⁡(ρ¯ρ).p\_{-}^{\varepsilon}=\frac{2}{\sigma\bar{\rho}T}\left(-\pi+\arctan\left(\frac{\bar{\rho}}{\rho}\right)\right),\quad p\_{+}^{\varepsilon}=\frac{2}{\sigma\bar{\rho}T}\arctan\left(\frac{\bar{\rho}}{\rho}\right). |  |

By the Gärtner-Ellis theorem, the sequence {XTε−X0ε}\{X^{\varepsilon}\_{T}-X^{\varepsilon}\_{0}\} satisfies an LDP with speed ε2\varepsilon^{2} and a good rate function Λ1ε​(x)\Lambda\_{1}^{\varepsilon}(x) defined by the Legendre transform:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ1ε​(x)=supp∈(p−ε,p+ε){p​x−Γ1ε​(p)}.\Lambda\_{1}^{\varepsilon}(x)=\sup\_{p\in(p\_{-}^{\varepsilon},p\_{+}^{\varepsilon})}\{px-\Gamma\_{1}^{\varepsilon}(p)\}. |  | (42) |

This allows us to characterize the exponential decay of the option price.

###### Proposition 4.2 (First Moment Decay Rate).

The asymptotic behavior of the deep OTM European call option price is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limε→0ε2​log⁡P1ε​(ε)=−Λ1ε​(1),\lim\_{\varepsilon\to 0}\varepsilon^{2}\log P\_{1}^{\varepsilon}(\varepsilon)=-\Lambda\_{1}^{\varepsilon}(1), |  | (43) |

where Λ1ε​(1)\Lambda\_{1}^{\varepsilon}(1) is the rate function evaluated at the scaled threshold x=1x=1 (corresponding to log-moneyness 1/ε1/\varepsilon).

###### Proof.

The proof proceeds by establishing matching lower and upper bounds for the decay rate.

#### Lower Bound.

For any η>0\eta>0, consider the open set Gη≔{y∈ℝ:y>1+η}G\_{\eta}\coloneqq\{y\in\mathbb{R}:y>1+\eta\}. On the event {XTε−X0ε∈Gη}\{X^{\varepsilon}\_{T}-X^{\varepsilon}\_{0}\in G\_{\eta}\}, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ST=S0​e(XTε−X0ε)/ε>S0​e(1+η)/ε=K​eη/ε.S\_{T}=S\_{0}e^{(X^{\varepsilon}\_{T}-X^{\varepsilon}\_{0})/\varepsilon}>S\_{0}e^{(1+\eta)/\varepsilon}=Ke^{\eta/\varepsilon}. |  | (44) |

Consequently, the option payoff is bounded from below by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ST−K)+>K​(eη/ε−1)on ​{XTε−X0ε∈Gη}.(S\_{T}-K)^{+}>K(e^{\eta/\varepsilon}-1)\quad\text{on }\{X^{\varepsilon}\_{T}-X^{\varepsilon}\_{0}\in G\_{\eta}\}. |  | (45) |

Taking the expectation and applying the LDP lower bound for open sets:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | lim infε→0ε2​log⁡P1ε​(ε)\displaystyle\liminf\_{\varepsilon\to 0}\varepsilon^{2}\log P\_{1}^{\varepsilon}(\varepsilon) | ≥lim infε→0[ε2​log⁡(K​(eη/ε−1))+ε2​log⁡ℙε​(XTε−X0ε∈Gη)]\displaystyle\geq\liminf\_{\varepsilon\to 0}\left[\varepsilon^{2}\log\left(K(e^{\eta/\varepsilon}-1)\right)+\varepsilon^{2}\log\mathbb{P}^{\varepsilon}(X^{\varepsilon}\_{T}-X^{\varepsilon}\_{0}\in G\_{\eta})\right] |  | (46) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≥lim infε→0[ε2​log⁡(K)+ε2​log⁡(eη/ε−1)]−infy∈GηΛ1ε​(y).\displaystyle\geq\liminf\_{\varepsilon\to 0}\left[\varepsilon^{2}\log(K)+\varepsilon^{2}\log(e^{\eta/\varepsilon}-1)\right]-\inf\_{y\in G\_{\eta}}\Lambda\_{1}^{\varepsilon}(y). |  | (47) |

Note that limε→0ε2​log⁡(eη/ε−1)=limε→0ε2​(η/ε)=0\lim\_{\varepsilon\to 0}\varepsilon^{2}\log(e^{\eta/\varepsilon}-1)=\lim\_{\varepsilon\to 0}\varepsilon^{2}(\eta/\varepsilon)=0. Thus, the first term vanishes. Since Λ1ε\Lambda\_{1}^{\varepsilon} is a good rate function (lower semicontinuous), taking the limit η→0\eta\to 0 yields the lower bound:

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim infε→0ε2​log⁡P1ε​(ε)≥−Λ1ε​(1).\liminf\_{\varepsilon\to 0}\varepsilon^{2}\log P\_{1}^{\varepsilon}(\varepsilon)\geq-\Lambda\_{1}^{\varepsilon}(1). |  | (48) |

#### Upper Bound.

We apply Hölder’s inequality with conjugate exponents q,q′>1q,q^{\prime}>1 (where 1/q+1/q′=11/q+1/q^{\prime}=1):

|  |  |  |  |
| --- | --- | --- | --- |
|  | P1ε​(ε)=𝔼ℙε​[(ST−K)+​𝟏{ST>K}]≤𝔼ℙε​[(ST)q]1/q⋅ℙε​(ST>K)1/q′.P\_{1}^{\varepsilon}(\varepsilon)=\mathbb{E}^{\mathbb{P}^{\varepsilon}}\left[(S\_{T}-K)^{+}\mathbf{1}\_{\{S\_{T}>K\}}\right]\leq\mathbb{E}^{\mathbb{P}^{\varepsilon}}[(S\_{T})^{q}]^{1/q}\cdot\mathbb{P}^{\varepsilon}(S\_{T}>K)^{1/q^{\prime}}. |  | (49) |

Taking logarithms and multiplying by ε2\varepsilon^{2}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ε2​log⁡P1ε​(ε)≤ε2q​log⁡𝔼ℙε​[STq]+ε2q′​log⁡ℙε​(XTε−X0ε>1).\varepsilon^{2}\log P\_{1}^{\varepsilon}(\varepsilon)\leq\frac{\varepsilon^{2}}{q}\log\mathbb{E}^{\mathbb{P}^{\varepsilon}}[S\_{T}^{q}]+\frac{\varepsilon^{2}}{q^{\prime}}\log\mathbb{P}^{\varepsilon}(X^{\varepsilon}\_{T}-X^{\varepsilon}\_{0}>1). |  | (50) |

The first term involves the qq-th moment of the Heston price process, which is finite for fixed TT and does not scale exponentially with 1/ε21/\varepsilon^{2} (i.e., its decay rate is 0). For the second term, applying the LDP upper bound for the closed set F=[1,∞)F=[1,\infty) yields:

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim supε→0ε2​log⁡P1ε​(ε)≤0−1q′​infy≥1Λ1ε​(y)=−1q′​Λ1ε​(1).\limsup\_{\varepsilon\to 0}\varepsilon^{2}\log P\_{1}^{\varepsilon}(\varepsilon)\leq 0-\frac{1}{q^{\prime}}\inf\_{y\geq 1}\Lambda\_{1}^{\varepsilon}(y)=-\frac{1}{q^{\prime}}\Lambda\_{1}^{\varepsilon}(1). |  | (51) |

Since this inequality holds for any q>1q>1, we take the limit q→∞q\to\infty (which implies q′→1q^{\prime}\to 1) to obtain the sharp upper bound:

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim supε→0ε2​log⁡P1ε​(ε)≤−Λ1ε​(1).\limsup\_{\varepsilon\to 0}\varepsilon^{2}\log P\_{1}^{\varepsilon}(\varepsilon)\leq-\Lambda\_{1}^{\varepsilon}(1). |  | (52) |

Combining the lower and upper bounds completes the proof.
∎

### 4.3 Second Moment Analysis

We now turn to the analysis of the second moment of the importance sampling estimator.
We employ the same change of measure structure defined in Section [2.4](https://arxiv.org/html/2511.19826v1#S2.SS4 "2.4 Construction of the Proposed Measure ‣ 2 Problem Formulation and Preliminaries ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options"), where the drift adjustment is ht2=−(h¯/ρ¯)​Vth^{2}\_{t}=-(\bar{h}/\bar{\rho})\sqrt{V\_{t}}. Based on the heuristic that the expected log-price should reach the barrier k=1/εk=1/\varepsilon, we require the drift contribution ∫0Th¯​Vt​𝑑t≈k\int\_{0}^{T}\bar{h}V\_{t}dt\approx k. Under the slow mean-reversion scaling, 𝔼​[∫Vt]≈θ​T\mathbb{E}[\int V\_{t}]\approx\theta T. This suggests the choice:

|  |  |  |  |
| --- | --- | --- | --- |
|  | h¯=−1ε​θ​T.\bar{h}=-\frac{1}{\varepsilon\theta T}. |  | (53) |

This large drift is necessary to force the rare event {XTε−X0ε>1}\{X^{\varepsilon}\_{T}-X^{\varepsilon}\_{0}>1\} to occur with high probability.

The second moment is given by P2ε​(ε;h¯)≔𝔼ℙ¯ε​[((ST−K)+​Q​(h¯)−1)2]P\_{2}^{\varepsilon}(\varepsilon;\bar{h})\coloneqq\mathbb{E}^{\bar{\mathbb{P}}^{\varepsilon}}[((S\_{T}-K)^{+}Q(\bar{h})^{-1})^{2}].
Following the same bounding procedure as in the short-maturity case, we use the inequality (ST−K)+≤ST⋅𝟏{ST>K}(S\_{T}-K)^{+}\leq S\_{T}\cdot\mathbf{1}\_{\{S\_{T}>K\}}. The second moment is bounded by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P2ε​(ε;h¯)≤S02​𝔼ℙ​[e2​(XTε−X0ε)/ε​Q​(h¯)−1​𝟏{XTε−X0ε>1}].P\_{2}^{\varepsilon}(\varepsilon;\bar{h})\leq S\_{0}^{2}\,\mathbb{E}^{\mathbb{P}}\left[e^{2(X^{\varepsilon}\_{T}-X^{\varepsilon}\_{0})/\varepsilon}Q(\bar{h})^{-1}\mathbf{1}\_{\{X^{\varepsilon}\_{T}-X^{\varepsilon}\_{0}>1\}}\right]. |  | (54) |

To analyze this expectation, it is convenient to remove the stochastic integrals appearing in the exponential term via a further change of measure. We introduce an auxiliary probability measure ℙ~ε\widetilde{\mathbb{P}}^{\varepsilon} defined by the Radon-Nikodym derivative:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ℙ~εd​ℙε≔exp⁡(∫0T2​ρε​Vtε​𝑑Wt1+∫0T(2​ρ¯ε+h¯ρ¯)​Vtε​𝑑Wt2−12​∫0Tηε2​Vtε​𝑑t),\frac{d\widetilde{\mathbb{P}}^{\varepsilon}}{d\mathbb{P}^{\varepsilon}}\coloneqq\exp\left(\int\_{0}^{T}\frac{2\rho}{\sqrt{\varepsilon}}\sqrt{V^{\varepsilon}\_{t}}dW^{1}\_{t}+\int\_{0}^{T}\left(\frac{2\bar{\rho}}{\sqrt{\varepsilon}}+\frac{\bar{h}}{\bar{\rho}}\right)\sqrt{V^{\varepsilon}\_{t}}dW^{2}\_{t}-\frac{1}{2}\int\_{0}^{T}\eta\_{\varepsilon}^{2}V^{\varepsilon}\_{t}dt\right), |  | (55) |

where ηε2≔(2​ρε)2+(2​ρ¯ε+h¯ρ¯)2\eta\_{\varepsilon}^{2}\coloneqq\left(\frac{2\rho}{\sqrt{\varepsilon}}\right)^{2}+\left(\frac{2\bar{\rho}}{\sqrt{\varepsilon}}+\frac{\bar{h}}{\bar{\rho}}\right)^{2}.
Under ℙ~ε\widetilde{\mathbb{P}}^{\varepsilon}, the stochastic integrals are absorbed, and the exponent becomes a functional of the integrated variance.

Applying Hölder’s inequality with conjugate exponents q,q′>1q,q^{\prime}>1, we arrive at the decomposition:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ε2​log⁡P2ε​(ε;h¯)≤2​ε2​log⁡S0+ε2q​log⁡𝔼ℙ~ε​[exp⁡(q​C​(h¯)​∫0TVtε​d​tε)]⏟Term I+ε2q′​log⁡ℙ~ε​(XTε−X0ε>1)⏟Term II,\varepsilon^{2}\log P\_{2}^{\varepsilon}(\varepsilon;\bar{h})\leq 2\varepsilon^{2}\log S\_{0}+\underbrace{\frac{\varepsilon^{2}}{q}\log\mathbb{E}^{\widetilde{\mathbb{P}}^{\varepsilon}}\left[\exp\left(qC(\bar{h})\int\_{0}^{T}V^{\varepsilon}\_{t}\frac{dt}{\varepsilon}\right)\right]}\_{\text{Term I}}+\underbrace{\frac{\varepsilon^{2}}{q^{\prime}}\log\widetilde{\mathbb{P}}^{\varepsilon}(X^{\varepsilon}\_{T}-X^{\varepsilon}\_{0}>1)}\_{\text{Term II}}, |  | (56) |

where the coefficient C​(h¯)=1+2​h¯+h¯2/ρ¯2C(\bar{h})=1+2\bar{h}+\bar{h}^{2}/\bar{\rho}^{2}.

We analyze the two resulting terms separately in the limit ε→0\varepsilon\to 0.

#### Term I.

Term I represents the moment of the integrated variance under the auxiliary measure. As derived in Appendix [D](https://arxiv.org/html/2511.19826v1#Sx1.SS4 "D Derivation of the Deep OTM Term I ‣ Appendix ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options"), although the volatility of volatility scales as O​(ε1.5)O(\varepsilon^{1.5}), the large drift h¯\bar{h} introduces a quadratic term of order O​(ε−2)O(\varepsilon^{-2}) in the Riccati equation. This delicate balance ensures that the discriminant of the characteristic equation is finite and negative in the limit. Consequently, the solution enters an oscillatory regime.

###### Proposition 4.3 (Limit of Integrated Variance Moment).

The asymptotic limit of the first term in the Hölder decomposition is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limε→0(Term I)=1q⋅v0​2​qσ​θ​ρ¯​T​tan⁡(σ​2​q2​θ​ρ¯).\lim\_{\varepsilon\to 0}(\text{Term I})=\frac{1}{q}\cdot\frac{v\_{0}\sqrt{2q}}{\sigma\theta\bar{\rho}T}\tan\left(\frac{\sigma\sqrt{2q}}{2\theta\bar{\rho}}\right). |  | (57) |

#### Term II.

Term II corresponds to the residual probability of the rare event under ℙ~ε\widetilde{\mathbb{P}}^{\varepsilon}. The measure ℙ~ε\widetilde{\mathbb{P}}^{\varepsilon} effectively shifts the drift of the price process by O​(1/ε)O(1/\varepsilon), modifying the "energy" cost required to reach the target level. The large deviation behavior is governed by a modified rate function ΛI​Iε\Lambda\_{II}^{\varepsilon}, defined as the Legendre transform of the auxiliary SCGF ΓI​Iε​(p)\Gamma\_{II}^{\varepsilon}(p). The explicit form is derived in Appendix [E](https://arxiv.org/html/2511.19826v1#Sx1.SS5 "E Derivation of the Deep OTM Auxiliary SCGF Γ₃^𝜀⁢(𝑝) ‣ Appendix ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options").

###### Proposition 4.4 (Auxiliary SCGF ΓI​Iε\Gamma^{\varepsilon}\_{II}).

The limiting scaled cumulant generating function under ℙ~ε\widetilde{\mathbb{P}}^{\varepsilon} is given piecewise depending on the parameter pp. Let Δ^I​Iε​(p)≔σ2​(−p2​ρ¯2+2​pθ​T)\hat{\Delta}^{\varepsilon}\_{II}(p)\coloneqq\sigma^{2}\left(-p^{2}\bar{\rho}^{2}+\frac{2p}{\theta T}\right) be the discriminant. Let (pI​I,−ε,pI​I,+ε)(p^{\varepsilon}\_{II,-},p^{\varepsilon}\_{II,+}) denote the effective domain boundaries. The explicit form of ΓI​Iε​(p)\Gamma^{\varepsilon}\_{II}(p) is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΓI​Iε​(p)={v0σ2​(−p​ρ​σ+Δ^I​Iε​(p)​tanh⁡(Δ^I​Iε​(p)2​T)),for ​p∈(0,2θ​T​ρ¯2),−v0​p​ρσ,for ​p∈{0,2θ​T​ρ¯2},v0σ2​(−p​ρ​σ+−Δ^I​Iε​(p)​tan⁡(−Δ^I​Iε​(p)2​T)),for ​p∈(pI​I,−ε,0)∪(2θ​T​ρ¯2,pI​I,+ε).\Gamma^{\varepsilon}\_{II}(p)=\begin{dcases}\frac{v\_{0}}{\sigma^{2}}\left(-p\rho\sigma+\sqrt{\hat{\Delta}^{\varepsilon}\_{II}(p)}\tanh\left(\frac{\sqrt{\hat{\Delta}^{\varepsilon}\_{II}(p)}}{2}T\right)\right),&\text{for }p\in\left(0,\frac{2}{\theta T\bar{\rho}^{2}}\right),\\[10.0pt] -\frac{v\_{0}p\rho}{\sigma},&\text{for }p\in\left\{0,\frac{2}{\theta T\bar{\rho}^{2}}\right\},\\[10.0pt] \frac{v\_{0}}{\sigma^{2}}\left(-p\rho\sigma+\sqrt{-\hat{\Delta}^{\varepsilon}\_{II}(p)}\tan\left(\frac{\sqrt{-\hat{\Delta}^{\varepsilon}\_{II}(p)}}{2}T\right)\right),&\text{for }p\in(p^{\varepsilon}\_{II,-},0)\cup\left(\frac{2}{\theta T\bar{\rho}^{2}},p^{\varepsilon}\_{II,+}\right).\end{dcases} |  | (58) |

The decay rate for Term II is then:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limε→0(Term II)=−1q′​ΛI​Iε​(1)=−1q′​supp{p−ΓI​Iε​(p)}.\lim\_{\varepsilon\to 0}(\text{Term II})=-\frac{1}{q^{\prime}}\Lambda^{\varepsilon}\_{II}(1)=-\frac{1}{q^{\prime}}\sup\_{p}\{p-\Gamma^{\varepsilon}\_{II}(p)\}. |  | (59) |

Combining these results allows us to establish the upper bound for the second moment decay rate.

### 4.4 Asymptotic Optimality Result

We are now in a position to prove the main result of this section: the logarithmic efficiency of the proposed importance sampling estimator in the deep out-of-the-money regime.

###### Theorem 4.5 (Deep OTM Asymptotic Optimality).

Let P1ε​(ε)P\_{1}^{\varepsilon}(\varepsilon) and P2ε​(ε;h¯)P\_{2}^{\varepsilon}(\varepsilon;\bar{h}) be the first and second moments of the IS estimator with the drift defined in Equation ([7](https://arxiv.org/html/2511.19826v1#S2.E7 "In 2.4 Construction of the Proposed Measure ‣ 2 Problem Formulation and Preliminaries ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")) and h¯=−1ε​θ​T\bar{h}=-\frac{1}{\varepsilon\theta T}. Then:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limε→0ε2​log⁡(P2ε​(ε;h¯)P1ε​(ε)2)=0.\lim\_{\varepsilon\to 0}\varepsilon^{2}\log\left(\frac{P\_{2}^{\varepsilon}(\varepsilon;\bar{h})}{P\_{1}^{\varepsilon}(\varepsilon)^{2}}\right)=0. |  | (60) |

###### Proof.

The proof proceeds by establishing matching lower and upper bounds for the limit of the normalized second moment.

#### Lower Bound.

By Jensen’s inequality, for any random variable ZZ, 𝔼​[Z2]≥(𝔼​[Z])2\mathbb{E}[Z^{2}]\geq(\mathbb{E}[Z])^{2}. Applying this to our unbiased estimator:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P2ε​(ε;h¯)≥(P1ε​(ε))2.P\_{2}^{\varepsilon}(\varepsilon;\bar{h})\geq(P\_{1}^{\varepsilon}(\varepsilon))^{2}. |  | (61) |

Taking logarithms, multiplying by ε2\varepsilon^{2}, and applying the limit from Proposition [4.2](https://arxiv.org/html/2511.19826v1#S4.Thmtheorem2 "Proposition 4.2 (First Moment Decay Rate). ‣ 4.2 First Moment Analysis ‣ 4 Deep Out-of-the-Money Asymptotics (𝐾→∞) ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options"):

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim infε→0ε2​log⁡P2ε​(ε;h¯)≥2​limε→0ε2​log⁡P1ε​(ε)=−2​Λ1ε​(1).\liminf\_{\varepsilon\to 0}\varepsilon^{2}\log P\_{2}^{\varepsilon}(\varepsilon;\bar{h})\geq 2\lim\_{\varepsilon\to 0}\varepsilon^{2}\log P\_{1}^{\varepsilon}(\varepsilon)=-2\Lambda\_{1}^{\varepsilon}(1). |  | (62) |

#### Upper Bound.

Recall the upper bound derived from the Hölder decomposition in Section [4.3](https://arxiv.org/html/2511.19826v1#S4.SS3 "4.3 Second Moment Analysis ‣ 4 Deep Out-of-the-Money Asymptotics (𝐾→∞) ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options"). Define the function Gε​(q)G^{\varepsilon}(q) for q>1q>1 as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gε​(q)≔v0​2/qσ​θ​ρ¯​T​tan⁡(σ​2​q2​θ​ρ¯)−(1−1q)​ΛI​Iε​(1).G^{\varepsilon}(q)\coloneqq\frac{v\_{0}\sqrt{2/q}}{\sigma\theta\bar{\rho}T}\tan\left(\frac{\sigma\sqrt{2q}}{2\theta\bar{\rho}}\right)-\left(1-\frac{1}{q}\right)\Lambda^{\varepsilon}\_{II}(1). |  | (63) |

The inequality derived in Equation ([56](https://arxiv.org/html/2511.19826v1#S4.E56 "In 4.3 Second Moment Analysis ‣ 4 Deep Out-of-the-Money Asymptotics (𝐾→∞) ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")) states that lim supε→0ε2​log⁡P2ε​(ε;h¯)≤infq>1Gε​(q)\limsup\_{\varepsilon\to 0}\varepsilon^{2}\log P\_{2}^{\varepsilon}(\varepsilon;\bar{h})\leq\inf\_{q>1}G^{\varepsilon}(q).

We rely on the analytical properties of Gε​(q)G^{\varepsilon}(q) to characterize this infimum:

1. 1.

   Existence: The function Gε​(q)G^{\varepsilon}(q) is continuous and convex. Furthermore, as qq approaches the singularity of the tangent term, Gε​(q)→∞G^{\varepsilon}(q)\to\infty. These properties guarantee the existence of a unique minimizer q∗q^{\*}.
2. 2.

   Optimality: The choice of drift h¯\bar{h} aligns the change of measure with the variational minimizer of the rate function. By the duality between the cumulant generating function and the rate function, this alignment ensures that the minimum value of Gε​(q)G^{\varepsilon}(q) coincides exactly with the optimal decay rate.

Therefore, the critical exponent q∗q^{\*} satisfies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | infq>1Gε​(q)=Gε​(q∗)=−2​Λ1ε​(1).\inf\_{q>1}G^{\varepsilon}(q)=G^{\varepsilon}(q^{\*})=-2\Lambda\_{1}^{\varepsilon}(1). |  | (64) |

Substituting this into the inequality yields the sharp upper bound:

|  |  |  |  |
| --- | --- | --- | --- |
|  | lim supε→0ε2​log⁡P2ε​(ε;h¯)≤−2​Λ1ε​(1).\limsup\_{\varepsilon\to 0}\varepsilon^{2}\log P\_{2}^{\varepsilon}(\varepsilon;\bar{h})\leq-2\Lambda\_{1}^{\varepsilon}(1). |  | (65) |

#### Conclusion.

Combining ([62](https://arxiv.org/html/2511.19826v1#S4.E62 "In Lower Bound. ‣ 4.4 Asymptotic Optimality Result ‣ 4 Deep Out-of-the-Money Asymptotics (𝐾→∞) ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")) and ([65](https://arxiv.org/html/2511.19826v1#S4.E65 "In Upper Bound. ‣ 4.4 Asymptotic Optimality Result ‣ 4 Deep Out-of-the-Money Asymptotics (𝐾→∞) ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")), we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limε→0ε2​log⁡P2ε​(ε;h¯)=−2​Λ1ε​(1)=limε→0ε2​log⁡(P1ε​(ε)2).\lim\_{\varepsilon\to 0}\varepsilon^{2}\log P\_{2}^{\varepsilon}(\varepsilon;\bar{h})=-2\Lambda\_{1}^{\varepsilon}(1)=\lim\_{\varepsilon\to 0}\varepsilon^{2}\log(P\_{1}^{\varepsilon}(\varepsilon)^{2}). |  | (66) |

Subtracting the right-hand side from the left-hand side yields the result:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limε→0ε2​log⁡(P2ε​(ε;h¯)P1ε​(ε)2)=0.\lim\_{\varepsilon\to 0}\varepsilon^{2}\log\left(\frac{P\_{2}^{\varepsilon}(\varepsilon;\bar{h})}{P\_{1}^{\varepsilon}(\varepsilon)^{2}}\right)=0. |  | (67) |

∎

## 5 Numerical Experiments

In this section, we assess the practical performance of the proposed state-dependent importance sampling scheme. We compare the standard error and computational efficiency of our IS estimator against the standard "Brute-Force" Monte Carlo (BMC) method.
The efficiency gain is quantified by the Variance Reduction Ratio (VRR), defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | VRR≔Var​(BMC Estimator)Var​(IS Estimator)≈(SEBMCSEIS)2,\text{VRR}\coloneqq\frac{\text{Var}(\text{BMC Estimator})}{\text{Var}(\text{IS Estimator})}\approx\left(\frac{\text{SE}\_{\text{BMC}}}{\text{SE}\_{\text{IS}}}\right)^{2}, |  | (68) |

where variance is estimated using sample variance over MM independent paths. All simulations are performed using a high-order discretization scheme (e.g., Milstein scheme for the variance process) to minimize discretization bias.

### 5.1 Short-Maturity Regime Performance

We first investigate the short-maturity limit. The model parameters are chosen to reflect a high-volatility regime often used in short-term asymptotics literature (e.g., [feng2012short]):

|  |  |  |
| --- | --- | --- |
|  | S0=2000,K=2200,v0=θ=0.36,κ=60,σ=3,ρ=−0.1,r=0.S\_{0}=2000,\quad K=2200,\quad v\_{0}=\theta=0.36,\quad\kappa=60,\quad\sigma=3,\quad\rho=-0.1,\quad r=0. |  |

We compare two maturities: T=1/252T=1/252 (1 day) and T=21/252T=21/252 (1 month). The number of sample paths is fixed at M=218M=2^{18}.

Table 1: Comparison of BMC and IS estimators in the short-maturity regime (K/S0=1.1K/S\_{0}=1.1).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Maturity | Method | Price | Std. Error (SE) | Rel. Error |
| T=1/252T=1/252 | BMC | 0.150070 | 0.005682 | 3.79% |
| (1 Day) | IS | 0.147814 | 0.000472 | 0.32% |
|  |  | VRR ≈\approx 144.9 | | |
| T=21/252T=21/252 | BMC | 64.825366 | 0.307750 | 0.47% |
| (1 Month) | IS | 64.833236 | 0.172721 | 0.27% |
|  |  | VRR ≈\approx 3.17 | | |

The results in Table [1](https://arxiv.org/html/2511.19826v1#S5.T1 "Table 1 ‣ 5.1 Short-Maturity Regime Performance ‣ 5 Numerical Experiments ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options") strongly validate the theoretical predictions. For the 1-day maturity, where the option is deep OTM in terms of time-scaled deviations, the IS method achieves a massive variance reduction factor of approximately 145. This confirms that the drift adjustment effectively counteracts the rarity of the event.
As maturity increases to 1 month, the event becomes less rare (the option is closer to the money in probability terms), and the VRR decreases to a modest factor of 3.17. This behavior is consistent with the definition of asymptotic optimality: the benefits are most pronounced in the limit T→0T\to 0.

### 5.2 Deep Out-of-the-Money Regime Performance

Next, we examine the deep OTM regime. Here, we use a parameter set with slower mean reversion to highlight the impact of the scaling analyzed in Section [4](https://arxiv.org/html/2511.19826v1#S4 "4 Deep Out-of-the-Money Asymptotics (𝐾→∞) ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options"):

|  |  |  |
| --- | --- | --- |
|  | S0=2000,v0=θ=0.5,κ=15,σ=1,ρ=−0.1,r=0.S\_{0}=2000,\quad v\_{0}=\theta=0.5,\quad\kappa=15,\quad\sigma=1,\quad\rho=-0.1,\quad r=0. |  |

We vary the strike price KK to span a range of moneyness K/S0∈[1.0,2.0]K/S\_{0}\in[1.0,2.0] and measure the VRR across three maturities: Short (1 day), Medium (1 month), and Long (1 year).

![Refer to caption](vrr_short.png)


Figure 1: VRR vs. Moneyness for T=1/252T=1/252 (1 Day). The VRR grows exponentially with moneyness, exceeding 2500 for deep OTM strikes.

![Refer to caption](vrr_medium.png)


Figure 2: VRR vs. Moneyness for T=21/252T=21/252 (1 Month). Significant variance reduction is maintained, peaking around 450.

![Refer to caption](vrr_long.png)


Figure 3: VRR vs. Moneyness for T=1T=1 (1 Year). The VRR saturates below 250, indicating the diminishing effectiveness of the specific drift as the time horizon allows for more complex path dynamics.

#### Discussion.

Figures [1](https://arxiv.org/html/2511.19826v1#S5.F1 "Figure 1 ‣ 5.2 Deep Out-of-the-Money Regime Performance ‣ 5 Numerical Experiments ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options") through [3](https://arxiv.org/html/2511.19826v1#S5.F3 "Figure 3 ‣ 5.2 Deep Out-of-the-Money Regime Performance ‣ 5 Numerical Experiments ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options") illustrate the exponential efficiency of the proposed scheme.

* •

  In the Short Maturity case (Fig. [1](https://arxiv.org/html/2511.19826v1#S5.F1 "Figure 1 ‣ 5.2 Deep Out-of-the-Money Regime Performance ‣ 5 Numerical Experiments ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")), the VRR explodes as KK increases, reaching values over 2500. This confirms that our IS density Q​(h¯)Q(\bar{h}) captures the large deviation optimal path almost perfectly in this regime.
* •

  In the Medium Maturity case (Fig. [2](https://arxiv.org/html/2511.19826v1#S5.F2 "Figure 2 ‣ 5.2 Deep Out-of-the-Money Regime Performance ‣ 5 Numerical Experiments ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")), the method remains highly effective (VRR ∼450\sim 450), demonstrating robustness.
* •

  In the Long Maturity case (Fig. [3](https://arxiv.org/html/2511.19826v1#S5.F3 "Figure 3 ‣ 5.2 Deep Out-of-the-Money Regime Performance ‣ 5 Numerical Experiments ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")), while still providing useful variance reduction (VRR ∼100−250\sim 100-250), the growth rate slows down. This is physically intuitive: over long horizons, the variance process can fluctuate significantly away from its initial value, and a drift proportional to Vt\sqrt{V\_{t}} (based on the slowly-varying assumption) captures the dominant behavior but may miss second-order path fluctuations. Nevertheless, the method remains superior to standard MC.

## 6 Conclusion

In this paper, we have developed and analyzed an asymptotically optimal importance sampling strategy for pricing European call options under the Heston model. By leveraging the Large Deviation Principle, we constructed a state-dependent change of measure where the drift of the driving Brownian motions is scaled by the instantaneous volatility.

Our theoretical contributions are twofold. First, in the short-maturity regime, we bridged the gap between the known implied volatility asymptotics and Monte Carlo variance reduction, proving via Riccati analysis that our scheme achieves logarithmic efficiency. Second, and more significantly, we introduced a novel slow mean-reversion scaling (δ=ε−2\delta=\varepsilon^{-2}) for the deep OTM regime. We demonstrated that under this scaling, the stochastic volatility contributes non-trivially to the rate function, and our specific drift design is required to match the asymptotic decay of the second moment.

Numerical experiments confirmed our theoretical findings, showing substantial variance reduction ratios—spanning from two to three orders of magnitude—particularly in the regimes where standard estimators fail most severely. These results highlight the power of combining large deviation theory with singular perturbation techniques to design efficient simulation algorithms for complex path-dependent derivatives. Future work may extend this framework to path-dependent options (e.g., Asian or Barrier options) or Rough Volatility models, where the non-Markovian nature of volatility poses new challenges for importance sampling design.

## Appendix

### A Derivation of the Short-Maturity Term I

In this appendix, we derive the asymptotic limit of the integrated variance moment presented in Equation ([25](https://arxiv.org/html/2511.19826v1#S3.E25 "In Proposition 3.3 (Limit of Integrated Variance Moment). ‣ Term I. ‣ 3.2 Second Moment Analysis ‣ 3 Short-Maturity Asymptotics (𝑇→0) ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")). We aim to evaluate the limit of the moment generating function at maturity TT, defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | LI≔limT→0T​log⁡𝔼ℙ~​[exp⁡(q​C​(h¯)​∫0TVs​𝑑s)∣V0=v0]L\_{I}\coloneqq\lim\_{T\to 0}T\log{\mathbb{E}^{\widetilde{\mathbb{P}}}\left[\exp\left(qC(\bar{h})\int\_{0}^{T}V\_{s}ds\right)\mid V\_{0}=v\_{0}\right]} |  | (69) |

#### Feynman-Kac and Riccati Equation

Let FI​(t,v)≔𝔼ℙ~​[exp⁡(q​C​(h¯)​∫0tVs​𝑑s)∣V0=v]F\_{I}(t,v)\coloneqq\mathbb{E}^{\widetilde{\mathbb{P}}}\left[\exp\left(qC(\bar{h})\int\_{0}^{t}V\_{s}ds\right)\mid V\_{0}=v\right] denote the expectation term over the horizon tt. By the Feynman-Kac theorem, FI​(t,v)F\_{I}(t,v) satisfies the following partial differential equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂FI∂t=12​σ2​v​∂2FI∂v2+(κ​θ−κ~I​v)​∂FI∂v+q​C​(h¯)​v​FI,\frac{\partial F\_{I}}{\partial t}=\frac{1}{2}\sigma^{2}v\frac{\partial^{2}F\_{I}}{\partial v^{2}}+(\kappa\theta-\tilde{\kappa}\_{I}v)\frac{\partial F\_{I}}{\partial v}+qC(\bar{h})vF\_{I}, |  | (70) |

subject to the initial condition FI​(0,v)=1F\_{I}(0,v)=1. The effective mean-reversion is κ~I=κ−2​ρ​σ\tilde{\kappa}\_{I}=\kappa-2\rho\sigma.
Given the affine structure of the Heston model, we adopt the exponential-affine ansatz FI​(t,v)=exp⁡(ϕI​(t)+v​ψI​(t))F\_{I}(t,v)=\exp(\phi\_{I}(t)+v\psi\_{I}(t)). Substituting this ansatz into ([70](https://arxiv.org/html/2511.19826v1#Sx1.E70 "In Feynman-Kac and Riccati Equation ‣ A Derivation of the Short-Maturity Term I ‣ Appendix ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")) yields a system of ODEs, where the Riccati equation for ψI​(t)\psi\_{I}(t) is decoupled:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψI′​(t)=C0−C1​ψI​(t)+C2​ψI​(t)2,ψI​(0)=0,\psi\_{I}^{\prime}(t)=C\_{0}-C\_{1}\psi\_{I}(t)+C\_{2}\psi\_{I}(t)^{2},\quad\psi\_{I}(0)=0, |  | (71) |

Here, the coefficients are defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | CI,0=q​(1+2​h¯+h¯2ρ¯2),CI,1=κ~I,CI,2=σ22.C\_{I,0}=q\left(1+2\bar{h}+\frac{\bar{h}^{2}}{\bar{\rho}^{2}}\right),\quad C\_{I,1}=\tilde{\kappa}\_{I},\quad C\_{I,2}=\frac{\sigma^{2}}{2}. |  | (72) |

To linearize ([71](https://arxiv.org/html/2511.19826v1#Sx1.E71 "In Feynman-Kac and Riccati Equation ‣ A Derivation of the Short-Maturity Term I ‣ Appendix ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")), we employ the standard variable transformation ψI​(t)=−2σ2​uI′​(t)uI​(t)\psi\_{I}(t)=-\frac{2}{\sigma^{2}}\frac{u\_{I}^{\prime}(t)}{u\_{I}(t)}.
The function uI​(t)u\_{I}(t) then satisfies the second-order linear ODE:

|  |  |  |  |
| --- | --- | --- | --- |
|  | uI′′​(t)+CI,1​uI′​(t)+CI,0​CI,2​uI​(t)=0,u\_{I}^{\prime\prime}(t)+C\_{I,1}u\_{I}^{\prime}(t)+C\_{I,0}C\_{I,2}u\_{I}(t)=0, |  | (73) |

with initial conditions uI​(0)=1u\_{I}(0)=1 and uI′​(0)=0u\_{I}^{\prime}(0)=0 (implied by ψI​(0)=0\psi\_{I}(0)=0).

#### Asymptotic Analysis

We now consider the regime where the maturity T→0T\to 0. Recall the importance sampling drift is chosen as h¯=−kθ​T\bar{h}=-\frac{k}{\theta T}. This implies the coefficient CI,0C\_{I,0} scales as O​(T−2)O(T^{-2}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | CI,0∼q​k2ρ¯2​θ2​T2.C\_{I,0}\sim\frac{qk^{2}}{\bar{\rho}^{2}\theta^{2}T^{2}}. |  | (74) |

Consequently, the discriminant of the characteristic equation is dominated by the product term 4​CI,0​CI,24C\_{I,0}C\_{I,2}, leading to a large negative value:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΔI=CI,12−4​CI,0​CI,2∼−2​σ2​q​k2ρ¯2​θ2​T2.\Delta\_{I}=C\_{I,1}^{2}-4C\_{I,0}C\_{I,2}\sim-\frac{2\sigma^{2}qk^{2}}{\bar{\rho}^{2}\theta^{2}T^{2}}. |  | (75) |

The negative discriminant indicated that the system operates in a highly oscillatory regime. Let ωI≔12​−ΔI\omega\_{I}\coloneqq\frac{1}{2}\sqrt{-\Delta\_{I}}. The asymptotic frequency is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ωI∼σ​k​2​q2​ρ¯​θ​T.\omega\_{I}\sim\frac{\sigma k\sqrt{2q}}{2\bar{\rho}\theta T}. |  | (76) |

The general solution for ([73](https://arxiv.org/html/2511.19826v1#Sx1.E73 "In Feynman-Kac and Riccati Equation ‣ A Derivation of the Short-Maturity Term I ‣ Appendix ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")) is thus:

|  |  |  |  |
| --- | --- | --- | --- |
|  | uI​(t)=eCI,1​t/2​(cos⁡(ωI​t)+CI,12​ωI​sin⁡(ωI​t)).u\_{I}(t)=e^{C\_{I,1}t/2}\left(\cos(\omega\_{I}t)+\frac{C\_{I,1}}{2\omega\_{I}}\sin(\omega\_{I}t)\right). |  | (77) |

In the limit t=T→0t=T\rightarrow 0, the damping term eCI,1​t/2→1e^{C\_{I,1}t/2}\rightarrow 1, and the ratio CI,12​ωI​sin⁡(ωI​t)→0\frac{C\_{I,1}}{2\omega\_{I}}\sin(\omega\_{I}t)\rightarrow 0. We approximate the solution and its derivative as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | uI​(T)∼cos⁡ωI​T,uI′​(T)∼−ωI​sin⁡ωI​T.u\_{I}(T)\sim\cos{\omega\_{I}T},\quad u\_{I}^{\prime}(T)\sim-\omega\_{I}\sin{\omega\_{I}T}. |  | (78) |

Substituting these back into the transformation for ψI​(T)\psi\_{I}(T):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψI​(T)=−2σ2​uI′​(T)uI​(T)∼2​ωIσ2​tan⁡(ωI​T).\psi\_{I}(T)=-\frac{2}{\sigma^{2}}\frac{u\_{I}^{\prime}(T)}{u\_{I}(T)}\sim\frac{2\omega\_{I}}{\sigma^{2}}\tan(\omega\_{I}T). |  | (79) |

Finally, we compute the limit of the exponent. Note that the constant term ϕI​(T)\phi\_{I}(T) scales as O​(1)O(1) and vanishes under the T​log⁡(⋅)T\log(\cdot) scaling. The limit is determined entirely by the v0​ψI​(T)v\_{0}\psi\_{I}(T) term:

|  |  |  |  |
| --- | --- | --- | --- |
|  | LI=v0​limT→0T​ψI​(T)=v0⋅k​2​qσ​ρ¯​θ​tan⁡(σ​k​2​q2​ρ¯​θ).L\_{I}=v\_{0}\lim\_{T\to 0}T\psi\_{I}(T)=v\_{0}\cdot\frac{k\sqrt{2q}}{\sigma\bar{\rho}\theta}\tan\left(\frac{\sigma k\sqrt{2q}}{2\bar{\rho}\theta}\right). |  | (80) |

Multiplying by the factor 1/q1/q from the Hölder decomposition, we obtain the final result:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limT→0(Term I)=v0​k​2/qσ​θ​ρ¯​tan⁡(σ​k​2​q2​θ​ρ¯).\lim\_{T\rightarrow 0}(\text{Term I})=\frac{v\_{0}k\sqrt{2/q}}{\sigma\theta\bar{\rho}}\tan\left(\frac{\sigma k\sqrt{2q}}{2\theta\bar{\rho}}\right). |  | (81) |

### B Derivation of the Short-Maturity ΓI​I​(p)\Gamma\_{II}(p)

In this section, we determine the limiting SCGF for the log-price process under the auxiliary measure ℙ~\widetilde{\mathbb{P}}. Our objective is to evaluate the limit:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΓI​I​(p)≔limT→0T​log⁡𝔼ℙ~​[exp⁡(pT​(XT−X0))].\Gamma\_{II}(p)\coloneqq\lim\_{T\to 0}T\log\mathbb{E}^{\widetilde{\mathbb{P}}}\left[\exp\left(\frac{p}{T}(X\_{T}-X\_{0})\right)\right]. |  | (82) |

#### Feynman-Kac and Riccati Equation

Let FI​I​(t,v)=𝔼ℙ~​[exp⁡(pT​(XT−Xt))∣Vt=v]F\_{II}(t,v)=\mathbb{E}^{\widetilde{\mathbb{P}}}[\exp(\frac{p}{T}(X\_{T}-X\_{t}))\mid V\_{t}=v] denote the moment generating function. Under ℙ~\widetilde{\mathbb{P}}, the drift of XtX\_{t} is modified to (32+h¯)​Vt(\frac{3}{2}+\bar{h})V\_{t}. By the Feynman-Kac theorem, FI​IF\_{II} satisfies the following PDE:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂FI​I∂t=12​σ2​v​∂2FI​I∂v2+(κ​θ−κ~I​I​v)​∂FI​I∂v+[(32+h¯)​pT+12​ρ¯2​(pT)2]​v​FI​I,\frac{\partial F\_{II}}{\partial t}=\frac{1}{2}\sigma^{2}v\frac{\partial^{2}F\_{II}}{\partial v^{2}}+\left(\kappa\theta-\tilde{\kappa}\_{II}v\right)\frac{\partial F\_{II}}{\partial v}+\left[\left(\frac{3}{2}+\bar{h}\right)\frac{p}{T}+\frac{1}{2}\bar{\rho}^{2}\left(\frac{p}{T}\right)^{2}\right]vF\_{II}, |  | (83) |

subject to FI​I​(0,v)=1F\_{II}(0,v)=1. The effective mean-reversion speed is κ~I​I=κ−2​ρ​σ\tilde{\kappa}\_{II}=\kappa-2\rho\sigma.
Applying the affine ansatz FI​I​(t,v)=exp⁡(ϕI​I​(t)+v​ψI​I​(t))F\_{II}(t,v)=\exp(\phi\_{II}(t)+v\psi\_{II}(t)) yields the Riccati ODE for ψI​I​(t)\psi\_{II}(t):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψI​I′​(t)=CI​I,0​(T)−CI​I,1​(T)​ψI​I​(t)+CI​I,2​ψI​I​(t)2,ψI​I​(0)=0.\psi\_{II}^{\prime}(t)=C\_{II,0}(T)-C\_{II,1}(T)\psi\_{II}(t)+C\_{II,2}\psi\_{II}(t)^{2},\quad\psi\_{II}(0)=0. |  | (84) |

Unlike the variance moment case (Appendix [A](https://arxiv.org/html/2511.19826v1#Sx1.SS1 "A Derivation of the Short-Maturity Term I ‣ Appendix ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")), the coefficients here depend explicitly on TT:

|  |  |  |  |
| --- | --- | --- | --- |
|  | CI​I,0​(T)=pT​(32+h¯)+12​(pT)2​ρ¯2,CI​I,1​(T)=κ~I​I−pT​ρ​σ,CI​I,2=σ22.C\_{II,0}(T)=\frac{p}{T}\left(\frac{3}{2}+\bar{h}\right)+\frac{1}{2}\left(\frac{p}{T}\right)^{2}\bar{\rho}^{2},\quad C\_{II,1}(T)=\tilde{\kappa}\_{II}-\frac{p}{T}\rho\sigma,\quad C\_{II,2}=\frac{\sigma^{2}}{2}. |  | (85) |

Using the transformation ψI​I​(t)=−2σ2​uI​I′​(t)uI​I​(t)\psi\_{II}(t)=-\frac{2}{\sigma^{2}}\frac{u\_{II}^{\prime}(t)}{u\_{II}(t)}, we obtain the second-order linear ODE:

|  |  |  |  |
| --- | --- | --- | --- |
|  | uI​I′′​(t)+CI​I,1​(T)​uI​I′​(t)+CI​I,0​(T)​CI​I,2​uI​I​(t)=0u\_{II}^{\prime\prime}(t)+C\_{II,1}(T)u\_{II}^{\prime}(t)+C\_{II,0}(T)C\_{II,2}u\_{II}(t)=0 |  | (86) |

with initial conditions uI​I​(0)=1u\_{II}(0)=1 and uI​I′​(0)=0u\_{II}^{\prime}(0)=0.

#### Asymptotic Analysis

We now analyze the coefficients in the limit T→0T\rightarrow 0. Substituting the importance sampling drift h¯\bar{h}, we observe the following scaling behaviors:

|  |  |  |  |
| --- | --- | --- | --- |
|  | CI​I,0​(T)≈1T2​(−p​kθ+p2​ρ¯22),CI​I,1​(T)≈−p​ρ​σT.C\_{II,0}(T)\approx\frac{1}{T^{2}}\left(-\frac{pk}{\theta}+\frac{p^{2}\bar{\rho}^{2}}{2}\right),\quad C\_{II,1}(T)\approx-\frac{p\rho\sigma}{T}. |  | (87) |

A distinct feature of this regime is that the linear coefficient CI​I,1​(T)C\_{II,1}(T) scales as O​(T−1)O(T^{-1}). Consequently, its square contributes to the leading order of the discriminant:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΔI​I=CI​I,1​(T)2−4​CI​I,0​(T)​CI​I,2≈1T2​[(−p​ρ​σ)2−2​σ2​(−p​kθ+p2​ρ¯22)].\Delta\_{II}=C\_{II,1}(T)^{2}-4C\_{II,0}(T)C\_{II,2}\approx\frac{1}{T^{2}}\left[\left(-{p\rho\sigma}\right)^{2}-2\sigma^{2}\left(-\frac{pk}{\theta}+\frac{p^{2}\bar{\rho}^{2}}{2}\right)\right]. |  | (88) |

We define the scaled discriminant Δ^I​I≔T2​ΔI​I=σ2​(p2​(2​ρ2−1)+2​p​kθ)\hat{\Delta}\_{II}\coloneqq T^{2}\Delta\_{II}=\sigma^{2}\left(p^{2}(2\rho^{2}-1)+\frac{2pk}{\theta}\right). The nature of the solution depends on the sign of Δ^I​I​(p)\hat{\Delta}\_{II}(p):

* •

  Exponential Regime (Δ^I​I>0\hat{\Delta}\_{II}>0): The characteristic roots are real. The solution involves hyperbolic functions, and the limit yields:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ΓI​I​(p)=v0σ2​(−p​ρ​σ+Δ^I​I​tanh⁡(Δ^I​I2)).\Gamma\_{II}(p)=\frac{v\_{0}}{\sigma^{2}}\left(-p\rho\sigma+\sqrt{\hat{\Delta}\_{II}}\tanh{\left(\frac{\sqrt{\hat{\Delta}\_{II}}}{2}\right)}\right). |  | (89) |
* •

  Linear Regime (Δ^I​I=0\hat{\Delta}\_{II}=0): The ODE degenerates, and the solution uI​I​(T)u\_{II}(T) behaves such that the log-derivative is linear. This occurs at the critical points p∈{0,pI​I∗}p\in\{0,p^{\*}\_{II}\}, yielding:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ΓI​I​(p)=−v0​p​ρσ.\Gamma\_{II}(p)=-\frac{v\_{0}p\rho}{\sigma}. |  | (90) |
* •

  Oscillatory Regime (Δ^I​I<0\hat{\Delta}\_{II}<0): The characteristic roots are imaginary. The solution involves trigonometric functions similar to Appendix [A](https://arxiv.org/html/2511.19826v1#Sx1.SS1 "A Derivation of the Short-Maturity Term I ‣ Appendix ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options"). The asymptotic limit is:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ΓI​I​(p)=v0σ2​(−p​ρ​σ+−Δ^I​I​tan⁡(−Δ^I​I2)).\Gamma\_{II}(p)=\frac{v\_{0}}{\sigma^{2}}\left(-p\rho\sigma+\sqrt{-\hat{\Delta}\_{II}}\tan\left(\frac{\sqrt{-\hat{\Delta}\_{II}}}{2}\right)\right). |  | (91) |

These three cases constitute the piecewise definition of the SCGF presented in Equation [26](https://arxiv.org/html/2511.19826v1#S3.E26 "In Proposition 3.4 (Auxiliary SCGF Γ_{𝐼⁢𝐼}). ‣ Term II. ‣ 3.2 Second Moment Analysis ‣ 3 Short-Maturity Asymptotics (𝑇→0) ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")

### C Derivation of the Deep OTM SCGF Γ1ε​(p)\Gamma\_{1}^{\varepsilon}(p)

In this appendix, we rigorously derive the limiting SCGF for the Deep OTM regime, denoted as Γ1ε​(p)\Gamma\_{1}^{\varepsilon}(p), and determine its domain (p−ε,p+ε)(p^{\varepsilon}\_{-},p^{\varepsilon}\_{+}). Recall the definition:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γ1ε​(p)≔limε→0ε2​log⁡𝔼ℙε​[exp⁡(pε2​(XTε−X0ε))].\Gamma\_{1}^{\varepsilon}(p)\coloneqq\lim\_{\varepsilon\to 0}\varepsilon^{2}\log\mathbb{E}^{\mathbb{P}^{\varepsilon}}\left[\exp\left(\frac{p}{\varepsilon^{2}}(X^{\varepsilon}\_{T}-X^{\varepsilon}\_{0})\right)\right]. |  | (92) |

The dynamics under the scaling δ=ε−2\delta=\varepsilon^{-2} follow System ([39](https://arxiv.org/html/2511.19826v1#S4.E39 "In The Slow Mean-Reversion Regime. ‣ 4.1 Small-Noise Scaling and Rescaled Dynamics ‣ 4 Deep Out-of-the-Money Asymptotics (𝐾→∞) ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")).

#### Measure Change

To facilitate the expectation calculation, we perform a Girsanov transformation to eliminate the stochastic integral with respect to W1W^{1}. Let ℚ~\widetilde{\mathbb{Q}} be the measure defined by the Radon-Nikodym derivative:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ℚ~d​ℙε≔exp⁡(p​ρε1.5​∫0TVtε​𝑑Wt1−12​p2​ρ2ε3​∫0TVtε​𝑑t).\frac{d\widetilde{\mathbb{Q}}}{d\mathbb{P}^{\varepsilon}}\coloneqq\exp\left(\frac{p\rho}{\varepsilon^{1.5}}\int\_{0}^{T}\sqrt{V^{\varepsilon}\_{t}}dW^{1}\_{t}-\frac{1}{2}\frac{p^{2}\rho^{2}}{\varepsilon^{3}}\int\_{0}^{T}V^{\varepsilon}\_{t}dt\right). |  | (93) |

Under ℚ~\widetilde{\mathbb{Q}}, the expectation reduces to a functional of the the integrated variance with an effective coefficient JεJ^{\varepsilon}. This coefficient collects contributions from the original drift, the measure change compensator, and the quadratic variation from W2W^{2}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jε=−p2​ε2+12​(p​ρε1.5)2+12​(p​ρ¯ε1.5)2=p22​ε3−p2​ε2.J^{\varepsilon}=-\frac{p}{2\varepsilon^{2}}+\frac{1}{2}\left(\frac{p\rho}{\varepsilon^{1.5}}\right)^{2}+\frac{1}{2}\left(\frac{p\bar{\rho}}{\varepsilon^{1.5}}\right)^{2}=\frac{p^{2}}{2\varepsilon^{3}}-\frac{p}{2\varepsilon^{2}}. |  | (94) |

#### Feynman-Kac and Riccati Equation

Let Fε​(t,v)=𝔼ℚ~​[exp⁡(∫0tJε​Vsε​𝑑s)∣V0ε=v]F^{\varepsilon}(t,v)=\mathbb{E}^{\widetilde{\mathbb{Q}}}[\exp(\int\_{0}^{t}J^{\varepsilon}V^{\varepsilon}\_{s}ds)\mid V^{\varepsilon}\_{0}=v]. By the Feynman-Kac theorem, Fε​(t,v)F^{\varepsilon}(t,v) satisfies the PDE:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂Fε∂t=12​(σ​ε1.5)2​v​∂2Fε∂v2+(κ​ε3​θ−κ~ε​v)​∂Fε∂v+Jε​v​Fε,\frac{\partial F^{\varepsilon}}{\partial t}=\frac{1}{2}(\sigma\varepsilon^{1.5})^{2}v\frac{\partial^{2}F^{\varepsilon}}{\partial v^{2}}+(\kappa\varepsilon^{3}\theta-\tilde{\kappa}^{\varepsilon}v)\frac{\partial F^{\varepsilon}}{\partial v}+J\_{\varepsilon}vF^{\varepsilon}, |  | (95) |

subject to Fε​(0,v)=1F^{\varepsilon}(0,v)=1. Here, κ~ε=κ​ε2−p​ρ​σ\tilde{\kappa}^{\varepsilon}=\kappa\varepsilon^{2}-p\rho\sigma is the effective mean-reversion speed.
Substituting the affine ansatz Fε​(t,v)=exp⁡(ϕε​(t)+v​ψε​(t))F^{\varepsilon}(t,v)=\exp(\phi^{\varepsilon}(t)+v\psi^{\varepsilon}(t)) into ([95](https://arxiv.org/html/2511.19826v1#Sx1.E95 "In Feynman-Kac and Riccati Equation ‣ C Derivation of the Deep OTM SCGF Γ₁^𝜀⁢(𝑝) ‣ Appendix ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")), we obtain the Riccati ODE for ψε​(t)\psi^{\varepsilon}(t):

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ψε)′​(t)=Jε−κ~ε​ψε​(t)+12​(σ​ε1.5)2​ψε​(t)2,ψε​(0)=0.(\psi^{\varepsilon})^{\prime}(t)=J^{\varepsilon}-\tilde{\kappa}^{\varepsilon}\psi^{\varepsilon}(t)+\frac{1}{2}(\sigma\varepsilon^{1.5})^{2}\psi^{\varepsilon}(t)^{2},\quad\psi^{\varepsilon}(0)=0. |  | (96) |

To solve this, we use the transformation ψε​(t)=−2σ2​ε3​(uε)′​(t)uε​(t)\psi^{\varepsilon}(t)=-\frac{2}{\sigma^{2}\varepsilon^{3}}\frac{(u^{\varepsilon})^{\prime}(t)}{u^{\varepsilon}(t)}, we obtain linear ODE:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (uε)′′​(t)+κ~ε​(uε)′​(t)+(Jε​σ2​ε32)​uε​(t)=0.(u^{\varepsilon})^{\prime\prime}(t)+\tilde{\kappa}^{\varepsilon}(u^{\varepsilon})^{\prime}(t)+\left(J^{\varepsilon}\frac{\sigma^{2}\varepsilon^{3}}{2}\right)u^{\varepsilon}(t)=0. |  | (97) |

with initial conditions uε​(0)=1,(uε)′​(0)=0u^{\varepsilon}(0)=1,(u^{\varepsilon})^{\prime}(0)=0.

#### Asymptotic Analysis

We now consider the limit ε→0\varepsilon\to 0. The constant term in the ODE simplifies as the ε3\varepsilon^{3} factors cancel:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limε→0(Jε​σ2​ε32)=limε→0(p22​ε3−p2​ε2)​σ2​ε32=p2​σ24.\lim\_{\varepsilon\rightarrow 0}\left(J^{\varepsilon}\frac{\sigma^{2}\varepsilon^{3}}{2}\right)=\lim\_{\varepsilon\rightarrow 0}\left(\frac{p^{2}}{2\varepsilon^{3}}-\frac{p}{2\varepsilon^{2}}\right)\frac{\sigma^{2}\varepsilon^{3}}{2}=\frac{p^{2}\sigma^{2}}{4}. |  | (98) |

Similarly, the damping term κ~ε→−p​ρ​σ\tilde{\kappa}^{\varepsilon}\rightarrow-p\rho\sigma. The limiting ODE becomes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (uε)′′​(t)−p​ρ​σ​(uε)′​(t)+p2​σ24​uε​(t)=0.(u^{\varepsilon})^{\prime\prime}(t)-p\rho\sigma(u^{\varepsilon})^{\prime}(t)+\frac{p^{2}\sigma^{2}}{4}u^{\varepsilon}(t)=0. |  | (99) |

The discriminant of the characteristic equation is Δε=(−p​ρ​σ)2−p2​σ2=−p2​σ2​ρ¯2\Delta^{\varepsilon}=(-p\rho\sigma)^{2}-p^{2}\sigma^{2}=-p^{2}\sigma^{2}\bar{\rho}^{2}. Since Δε<0\Delta^{\varepsilon}<0 for p≠0p\neq 0, the solution is strictly oscillatory. Define the frequency ωε=|p|​ρ¯​σ2\omega^{\varepsilon}=\frac{|p|\bar{\rho}\sigma}{2}. The solution evaluated at maturity TT is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | uε​(T)≈ep​ρ​σ​T2​cos⁡(ωε​T),u^{\varepsilon}(T)\approx e^{\frac{p\rho\sigma T}{2}}\cos(\omega^{\varepsilon}T), |  | (100) |

Substituting this back into expression for ψε​(T)\psi^{\varepsilon}(T). Recall that the initial variance scales as V0ε=ε​v0V^{\varepsilon}\_{0}=\varepsilon v\_{0}. Therefore, the limit of the SCGF is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γ1ε​(p)=limε→0ε2​(ε​v0)​ψε​(T)=v0​p−ρ​σ+ρ¯​σ​cot⁡(p​ρ¯​σ​T2).\Gamma\_{1}^{\varepsilon}(p)=\lim\_{\varepsilon\rightarrow 0}\varepsilon^{2}(\varepsilon v\_{0})\psi^{\varepsilon}(T)=\frac{v\_{0}p}{-\rho\sigma+\bar{\rho}\sigma\cot\left(\frac{p\bar{\rho}\sigma T}{2}\right)}. |  | (101) |

#### Effective Domain

The function Γ1ε​(p)\Gamma\_{1}^{\varepsilon}(p) is well-defined in the interval containing zero where the denominator does not vanish. The boundaries (p−ε,p+ε)(p^{\varepsilon}\_{-},p^{\varepsilon}\_{+}) are determined by the first singularities (ξ−ε,ξ+ε)(\xi^{\varepsilon}\_{-},\xi^{\varepsilon}\_{+}):

* •

  Case ρ>0\rho>0: ξ+ε=arctan⁡(ρ¯/ρ),ξ−ε=arctan⁡(ρ¯/ρ)−π\xi^{\varepsilon}\_{+}=\arctan(\bar{\rho}/\rho),\xi^{\varepsilon}\_{-}=\arctan(\bar{\rho}/\rho)-\pi. Thus,

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | p+ε=2σ​ρ¯​T​arctan⁡(ρ¯ρ),p−ε=2σ​ρ¯​T​(arctan⁡(ρ¯ρ)−π).p^{\varepsilon}\_{+}=\frac{2}{\sigma\bar{\rho}T}\arctan\left(\frac{\bar{\rho}}{\rho}\right),\quad p^{\varepsilon}\_{-}=\frac{2}{\sigma\bar{\rho}T}\left(\arctan\left(\frac{\bar{\rho}}{\rho}\right)-\pi\right). |  | (102) |
* •

  Case ρ<0\rho<0: ξ+ε=arctan⁡(ρ¯/ρ),ξ−ε=arctan⁡(ρ¯/ρ)−π\xi^{\varepsilon}\_{+}=\arctan(\bar{\rho}/\rho),\xi^{\varepsilon}\_{-}=\arctan(\bar{\rho}/\rho)-\pi. Thus,

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | p+ε=2σ​ρ¯​T​arctan⁡(ρ¯ρ),p−ε=2σ​ρ¯​T​(arctan⁡(ρ¯ρ)−π).p^{\varepsilon}\_{+}=\frac{2}{\sigma\bar{\rho}T}\arctan\left(\frac{\bar{\rho}}{\rho}\right),\quad p^{\varepsilon}\_{-}=\frac{2}{\sigma\bar{\rho}T}\left(\arctan\left(\frac{\bar{\rho}}{\rho}\right)-\pi\right). |  | (103) |
* •

  Case ρ=0\rho=0: The condition becomes cot⁡(ξ±ε)=0\cot(\xi^{\varepsilon}\_{\pm})=0, yielding p±ε=±πσ​Tp^{\varepsilon}\_{\pm}=\pm\frac{\pi}{\sigma T}.

Within (p−ε,p+ε)(p^{\varepsilon}\_{-},p^{\varepsilon}\_{+}), Γ1ε​(p)\Gamma\_{1}^{\varepsilon}(p) is essentially smooth, satisfying the requirements of the Gärtner-Ellis theorem.

### D Derivation of the Deep OTM Term I

In this appendix, we derive the asymptotic limit of the Deep OTM Term I. We aim to compute the limit:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limε→0ε2q​log⁡𝔼ℙ~ε​[exp⁡(q​C​(h¯)​∫0TVtε​d​tε)].\lim\_{\varepsilon\to 0}\frac{\varepsilon^{2}}{q}\log\mathbb{E}^{\widetilde{\mathbb{P}}^{\varepsilon}}\left[\exp\left(qC(\bar{h})\int\_{0}^{T}V^{\varepsilon}\_{t}\frac{dt}{\varepsilon}\right)\right]. |  | (104) |

#### Feynman-Kac and Riccati Equation

Let FIε​(t,v)=𝔼ℙ~ε​[exp⁡(q​C​(h¯)​ε−1​∫0tVsε​𝑑s)∣V0ε=v]F^{\varepsilon}\_{I}(t,v)=\mathbb{E}^{\widetilde{\mathbb{P}}^{\varepsilon}}[\exp(qC(\bar{h})\varepsilon^{-1}\int\_{0}^{t}V^{\varepsilon}\_{s}ds)\mid V^{\varepsilon}\_{0}=v]. By the Feynman-Kac theorem, FIε​(t,v)F^{\varepsilon}\_{I}(t,v) satisfies the following partial differential equation (PDE):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂FIε∂t=12​(σ​ε1.5)2​v​∂2FIε∂v2+(κ​ε3​θ−κ~Iε​v)​∂FIε∂v+q​C​(h¯)ε​v​FIε,\frac{\partial F^{\varepsilon}\_{I}}{\partial t}=\frac{1}{2}(\sigma\varepsilon^{1.5})^{2}v\frac{\partial^{2}F^{\varepsilon}\_{I}}{\partial v^{2}}+(\kappa\varepsilon^{3}\theta-\tilde{\kappa}^{\varepsilon}\_{I}v)\frac{\partial F^{\varepsilon}\_{I}}{\partial v}+\frac{qC(\bar{h})}{\varepsilon}vF^{\varepsilon}\_{I}, |  | (105) |

subject to the initial condition FIε​(0,v)=1F^{\varepsilon}\_{I}(0,v)=1. Here, the effective mean-reversion speed under ℙ~ε\widetilde{\mathbb{P}}^{\varepsilon} is κ~Iε=κ​ε2−2​ρ​σ​ε\tilde{\kappa}^{\varepsilon}\_{I}=\kappa\varepsilon^{2}-2\rho\sigma\varepsilon.

By the affine structure, the solution takes the form FIε​(t,v)=exp⁡(ϕIε​(t)+v​ψIε​(t))F^{\varepsilon}\_{I}(t,v)=\exp(\phi^{\varepsilon}\_{I}(t)+v\psi^{\varepsilon}\_{I}(t)). Substituting this ansatz into ([105](https://arxiv.org/html/2511.19826v1#Sx1.E105 "In Feynman-Kac and Riccati Equation ‣ D Derivation of the Deep OTM Term I ‣ Appendix ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")) leads to the Riccati ODE for ψIε​(t)\psi^{\varepsilon}\_{I}(t):

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ψIε)′​(t)=CI,0ε−CI,1ε​ψIε​(t)+CI,2ε​ψIε​(t)2,ψIε​(0)=0.\left({\psi^{\varepsilon}\_{I}}\right)^{\prime}(t)=C\_{I,0}^{\varepsilon}-C\_{I,1}^{\varepsilon}\psi^{\varepsilon}\_{I}(t)+C\_{I,2}^{\varepsilon}\psi^{\varepsilon}\_{I}(t)^{2},\quad\psi^{\varepsilon}\_{I}(0)=0. |  | (106) |

The coefficients correspond to the terms in the PDE:

|  |  |  |  |
| --- | --- | --- | --- |
|  | CI,0ε=q​C​(h¯)ε,CI,1ε=κ~Iε,CI,2ε=12​(σ​ε1.5)2.C\_{I,0}^{\varepsilon}=\frac{qC(\bar{h})}{\varepsilon},\quad C\_{I,1}^{\varepsilon}=\tilde{\kappa}^{\varepsilon}\_{I},\quad C\_{I,2}^{\varepsilon}=\frac{1}{2}(\sigma\varepsilon^{1.5})^{2}. |  | (107) |

We linearize the equation using the transformation ψIε​(t)=−1CI,2ε​(uIε)′​(t)uIε​(t)\psi^{\varepsilon}\_{I}(t)=-\frac{1}{C\_{I,2}^{\varepsilon}}\frac{(u^{\varepsilon}\_{I})^{\prime}(t)}{u^{\varepsilon}\_{I}(t)}. Substituting this into ([106](https://arxiv.org/html/2511.19826v1#Sx1.E106 "In Feynman-Kac and Riccati Equation ‣ D Derivation of the Deep OTM Term I ‣ Appendix ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")) yields the second-order linear ODE:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (uIε)′′​(t)+CI,1ε​(uIε)′​(t)+CI,0ε​CI,2ε​uIε​(t)=0,(u^{\varepsilon}\_{I})^{\prime\prime}(t)+C\_{I,1}^{\varepsilon}(u^{\varepsilon}\_{I})^{\prime}(t)+C\_{I,0}^{\varepsilon}C\_{I,2}^{\varepsilon}u^{\varepsilon}\_{I}(t)=0, |  | (108) |

with initial conditions uIε​(0)=1,(uIε)′​(0)=0u^{\varepsilon}\_{I}(0)=1,(u^{\varepsilon}\_{I})^{\prime}(0)=0.

#### Asymptotic Analysis

We now analyze the coefficients in the small-noise limit. The drift parameter is h¯=−1/(ε​θ​T)\bar{h}=-1/(\varepsilon\theta T). Substituting this into the constant term, we find:

|  |  |  |  |
| --- | --- | --- | --- |
|  | CI,0ε​CI,2ε≈(qε3​θ2​T2​ρ¯2)​(σ2​ε32)=q​σ22​θ2​T2​ρ¯2.C\_{I,0}^{\varepsilon}C\_{I,2}^{\varepsilon}\approx\left(\frac{q}{\varepsilon^{3}\theta^{2}T^{2}\bar{\rho}^{2}}\right)\left(\frac{\sigma^{2}\varepsilon^{3}}{2}\right)=\frac{q\sigma^{2}}{2\theta^{2}T^{2}\bar{\rho}^{2}}. |  | (109) |

Crucially, the ε3\varepsilon^{3} scaling factors cancel exactly, leaving and O​(1)O(1) constant term. The discriminant of the characteristic equation becomes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΔIε=(CI,1ε)2−4​CI,0ε​CI,2ε≈(κ​ε2−2​ρ​σ​ε)2−2​q​σ2θ2​T2​ρ¯2.\Delta^{\varepsilon}\_{I}=(C\_{I,1}^{\varepsilon})^{2}-4C\_{I,0}^{\varepsilon}C\_{I,2}^{\varepsilon}\approx(\kappa\varepsilon^{2}-2\rho\sigma\varepsilon)^{2}-\frac{2q\sigma^{2}}{\theta^{2}T^{2}\bar{\rho}^{2}}. |  | (110) |

As ε→0\varepsilon\to 0, the first term (CI,1ε)2∼O​(ε2)(C\_{I,1}^{\varepsilon})^{2}\sim O(\varepsilon^{2}) vanishes, and the discriminant converges to a negative constant:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limε→0ΔIε=Δ^Iε≔−2​q​σ2θ2​T2​ρ¯2.\lim\_{\varepsilon\rightarrow 0}\Delta^{\varepsilon}\_{I}=\hat{\Delta}\_{I}^{\varepsilon}\coloneqq-\frac{2q\sigma^{2}}{\theta^{2}T^{2}\bar{\rho}^{2}}. |  | (111) |

This negative discriminant implies an oscillatory solution regime. Let ωIε≔12​−Δ^Iε\omega\_{I}^{\varepsilon}\coloneqq\frac{1}{2}\sqrt{-\hat{\Delta}\_{I}^{\varepsilon}}. In the limit, the damping term vanishes (CI,1ε→0C\_{I,1}^{\varepsilon}\to 0), and the solution behaves as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | uIε​(T)∼cos⁡(ωIε​T)u^{\varepsilon}\_{I}(T)\sim\cos(\omega\_{I}^{\varepsilon}T) |  | (112) |

The logarithm derivative is thus:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψIε​(T)=−2σ2​ε3​(uIε)′​(T)uIε​(T)∼2​ωIεσ2​ε3​tan⁡(ωIε​T).\psi^{\varepsilon}\_{I}(T)=-\frac{2}{\sigma^{2}\varepsilon^{3}}\frac{(u^{\varepsilon}\_{I})^{\prime}(T)}{u^{\varepsilon}\_{I}(T)}\sim\frac{2\omega\_{I}^{\varepsilon}}{\sigma^{2}\varepsilon^{3}}\tan(\omega\_{I}^{\varepsilon}T). |  | (113) |

Finally, we compute the limit of the log-expectation LIεL^{\varepsilon}\_{I}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limε→0ε2​(ε​v0)q​ψIε​(T)=1q⋅v0​2​qσ​θ​ρ¯​T​tan⁡(σ​2​q2​θ​ρ¯).\lim\_{\varepsilon\to 0}\frac{\varepsilon^{2}(\varepsilon v\_{0})}{q}\psi^{\varepsilon}\_{I}(T)=\frac{1}{q}\cdot\frac{v\_{0}\sqrt{2q}}{\sigma\theta\bar{\rho}T}\tan\left(\frac{\sigma\sqrt{2q}}{2\theta\bar{\rho}}\right). |  | (114) |

### E Derivation of the Deep OTM Auxiliary SCGF Γ3ε​(p)\Gamma\_{3}^{\varepsilon}(p)

In this appendix, we derive the limiting SCGF under the auxiliary measure ℙ~ε\widetilde{\mathbb{P}}^{\varepsilon}, denoted as ΓI​Iε​(p)\Gamma^{\varepsilon}\_{II}(p). This function is required to evaluate Term II in Section [4.3](https://arxiv.org/html/2511.19826v1#S4.SS3 "4.3 Second Moment Analysis ‣ 4 Deep Out-of-the-Money Asymptotics (𝐾→∞) ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options"). We define:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΓI​Iε​(p)≔limε→0ε2​log⁡𝔼ℙ~ε​[exp⁡(pε2​(XTε−X0ε))].\Gamma^{\varepsilon}\_{II}(p)\coloneqq\lim\_{\varepsilon\to 0}\varepsilon^{2}\log\mathbb{E}^{\widetilde{\mathbb{P}}^{\varepsilon}}\left[\exp\left(\frac{p}{\varepsilon^{2}}(X^{\varepsilon}\_{T}-X^{\varepsilon}\_{0})\right)\right]. |  | (115) |

#### Feynman-Kac and Riccati Equation

The expectation can be reduced to a functional of the integrated variance. We define the effective coefficient JI​IεJ^{\varepsilon}\_{II} which collects the contributions from the drift of the scaled log-price and the quadratic variation compensator.
Under ℙ~ε\widetilde{\mathbb{P}}^{\varepsilon}, the drift of XtεX^{\varepsilon}\_{t} is dominated by ε​h¯​Vt≈−1ε​θ​T​Vtε\varepsilon\bar{h}V\_{t}\approx-\frac{1}{\varepsilon\theta T}V^{\varepsilon}\_{t}. Combined with the exponent p/ε2p/\varepsilon^{2} and the standard quadratic variation p22​ε3\frac{p^{2}}{2\varepsilon^{3}}, we define:

|  |  |  |  |
| --- | --- | --- | --- |
|  | JI​Iε≔p22​ε3−pε3​θ​T=1ε3​(p22−pθ​T).J^{\varepsilon}\_{II}\coloneqq\frac{p^{2}}{2\varepsilon^{3}}-\frac{p}{\varepsilon^{3}\theta T}=\frac{1}{\varepsilon^{3}}\left(\frac{p^{2}}{2}-\frac{p}{\theta T}\right). |  | (116) |

Both terms are of order O​(ε−3)O(\varepsilon^{-3}), which balances the diffusion coefficient in the limit.

Let FI​Iε​(t,v)=𝔼ℙ~ε​[exp⁡(∫0tJI​Iε​Vsε​𝑑s)∣V0ε=v]F^{\varepsilon}\_{II}(t,v)=\mathbb{E}^{\widetilde{\mathbb{P}}^{\varepsilon}}[\exp(\int\_{0}^{t}J^{\varepsilon}\_{II}V^{\varepsilon}\_{s}ds)\mid V^{\varepsilon}\_{0}=v]. By the Feynman-Kac theorem, FI​IεF^{\varepsilon}\_{II} satisfies the following PDE:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂FI​Iε∂t=12​(σ​ε1.5)2​v​∂2FI​Iε∂v2+(κ​ε3​θ−κ~I​Iε​v)​∂FI​Iε∂v+JI​Iε​v​FI​Iε,\frac{\partial F^{\varepsilon}\_{II}}{\partial t}=\frac{1}{2}(\sigma\varepsilon^{1.5})^{2}v\frac{\partial^{2}F^{\varepsilon}\_{II}}{\partial v^{2}}+(\kappa\varepsilon^{3}\theta-\tilde{\kappa}^{\varepsilon}\_{II}v)\frac{\partial F^{\varepsilon}\_{II}}{\partial v}+J^{\varepsilon}\_{II}vF^{\varepsilon}\_{II}, |  | (117) |

subject to FI​Iε​(0,v)=1F^{\varepsilon}\_{II}(0,v)=1. Here, κ~I​Iε=κ​ε2−p​ρ​σ\tilde{\kappa}^{\varepsilon}\_{II}=\kappa\varepsilon^{2}-p\rho\sigma represents the effective mean-reversion speed under the measure ℙ~ε\widetilde{\mathbb{P}}^{\varepsilon}.

Substituting the affine ansatz FI​Iε​(t,v)=exp⁡(ϕI​Iε​(t)+v​ψI​Iε​(t))F^{\varepsilon}\_{II}(t,v)=\exp(\phi^{\varepsilon}\_{II}(t)+v\psi^{\varepsilon}\_{II}(t)) into the PDE yields the Riccati ODE for ψI​Iε​(t)\psi^{\varepsilon}\_{II}(t):

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ψI​Iε)′​(t)=JI​Iε−κ~I​Iε​ψI​Iε​(t)+12​(σ​ε1.5)2​ψI​Iε​(t)2,ψI​Iε​(0)=0.\left({\psi^{\varepsilon}\_{II}}\right)^{\prime}(t)=J^{\varepsilon}\_{II}-\tilde{\kappa}^{\varepsilon}\_{II}\psi^{\varepsilon}\_{II}(t)+\frac{1}{2}(\sigma\varepsilon^{1.5})^{2}\psi^{\varepsilon}\_{II}(t)^{2},\quad\psi^{\varepsilon}\_{II}(0)=0. |  | (118) |

To solve this, we employ the transformation ψI​Iε​(t)=−2σ2​ε3​(uI​Iε)′​(t)uI​Iε​(t)\psi^{\varepsilon}\_{II}(t)=-\frac{2}{\sigma^{2}\varepsilon^{3}}\frac{(u^{\varepsilon}\_{II})^{\prime}(t)}{u^{\varepsilon}\_{II}(t)}. Substituting this into ([118](https://arxiv.org/html/2511.19826v1#Sx1.E118 "In Feynman-Kac and Riccati Equation ‣ E Derivation of the Deep OTM Auxiliary SCGF Γ₃^𝜀⁢(𝑝) ‣ Appendix ‣ Efficient Importance Sampling under Heston Model: Short Maturity and Deep Out-of-the-Money Options")) yields the second-order linear ODE for uI​I​(t)u\_{II}(t):

|  |  |  |  |
| --- | --- | --- | --- |
|  | (uI​Iε)′′​(t)+κ~I​Iε​(uI​Iε)′​(t)+(JI​Iε​σ2​ε32)​uI​Iε​(t)=0,{(u^{\varepsilon}\_{II})}^{\prime\prime}(t)+\tilde{\kappa}^{\varepsilon}\_{II}{(u^{\varepsilon}\_{II})}^{\prime}(t)+\left(J^{\varepsilon}\_{II}\frac{\sigma^{2}\varepsilon^{3}}{2}\right)u^{\varepsilon}\_{II}(t)=0, |  | (119) |

with initial conditions uI​Iε​(0)=1,(uI​Iε)′​(0)=0u^{\varepsilon}\_{II}(0)=1,(u^{\varepsilon}\_{II})^{\prime}(0)=0.

#### Asymptotic Analysis

We evaluate the coefficients in the limit. The ε3\varepsilon^{3} terms in the constant coefficient cancel out:

|  |  |  |  |
| --- | --- | --- | --- |
|  | limε→0(JI​Iε​σ2​ε32)=σ24​(p2−2​pθ​T).\lim\_{\varepsilon\to 0}\left(J^{\varepsilon}\_{II}\frac{\sigma^{2}\varepsilon^{3}}{2}\right)=\frac{\sigma^{2}}{4}\left(p^{2}-\frac{2p}{\theta T}\right). |  | (120) |

The damping term converges to a constant drift Since κ~I​Iε→−p​ρ​σ\tilde{\kappa}^{\varepsilon}\_{II}\to-p\rho\sigma. The limiting characteristic equation has the discriminant:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ^I​Iε≔(−p​ρ​σ)2−4​[σ24​(p2−2​pθ​T)]=σ2​(−p2​ρ¯2+2​pθ​T).\hat{\Delta}^{\varepsilon}\_{II}\coloneqq(-p\rho\sigma)^{2}-4\left[\frac{\sigma^{2}}{4}\left(p^{2}-\frac{2p}{\theta T}\right)\right]=\sigma^{2}\left(-p^{2}\bar{\rho}^{2}+\frac{2p}{\theta T}\right). |  | (121) |

The roots of Δ^I​Iε=0\hat{\Delta}^{\varepsilon}\_{II}=0 are p=0p=0 and pI​Iε,∗=2θ​T​ρ¯2p^{\varepsilon,\*}\_{II}=\frac{2}{\theta T\bar{\rho}^{2}}. This quadratic structure leads to three distinct regimes for the SCGF ΓI​Iε​(p)\Gamma^{\varepsilon}\_{II}(p):

* •

  Exponential Regime (Δ^I​Iε>0\hat{\Delta}^{\varepsilon}\_{II}>0): For p∈(0,pI​Iε,∗)p\in(0,p^{\varepsilon,\*}\_{II}), the roots are real. The solution involves hyperbolic functions, yielding

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ΓI​Iε​(p)=v0σ2​(−p​ρ​σ+Δ^I​Iε​tanh⁡(Δ^I​Iε2​T)).\Gamma^{\varepsilon}\_{II}(p)=\frac{v\_{0}}{\sigma^{2}}\left(-p\rho\sigma+\sqrt{\hat{\Delta}^{\varepsilon}\_{II}}\tanh\left(\frac{\sqrt{\hat{\Delta}^{\varepsilon}\_{II}}}{2}T\right)\right). |  | (122) |
* •

  Linear Regime (Δ^I​Iε=0\hat{\Delta}^{\varepsilon}\_{II}=0): For p∈{0,pI​Iε,∗}p\in\{0,p^{\varepsilon,\*}\_{II}\},the discriminant vanishes. The solution is linear in time, and the SCGF simplifies to:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ΓI​Iε​(p)=−v0​p​ρσ.\Gamma^{\varepsilon}\_{II}(p)=-\frac{v\_{0}p\rho}{\sigma}. |  | (123) |
* •

  Oscillatory Regime (Δ^I​Iε<0\hat{\Delta}^{\varepsilon}\_{II}<0): Outside the interval [0,pI​Iε,∗][0,p^{\varepsilon,\*}\_{II}], the roots are imaginary. Define the frequency ωI​Iε=12​−Δ^I​Iε\omega^{\varepsilon}\_{II}=\frac{1}{2}\sqrt{-\hat{\Delta}^{\varepsilon}\_{II}}. The solution involves trigonometric functions, and the limit is

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ΓI​Iε​(p)=v0σ2​(−p​ρ​σ+−Δ^I​Iε​tan⁡(−Δ^I​Iε2​T)).\Gamma^{\varepsilon}\_{II}(p)=\frac{v\_{0}}{\sigma^{2}}\left(-p\rho\sigma+\sqrt{-\hat{\Delta}^{\varepsilon}\_{II}}\tan\left(\frac{\sqrt{-\hat{\Delta}^{\varepsilon}\_{II}}}{2}T\right)\right). |  | (124) |

This explicitly characterizes ΓI​Iε​(p)\Gamma^{\varepsilon}\_{II}(p) within its effective domain (pI​I,−ε,pI​I,+ε)(p^{\varepsilon}\_{II,-},p^{\varepsilon}\_{II,+}).