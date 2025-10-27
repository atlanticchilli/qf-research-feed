---
authors:
- Dong Yan
- Ke Zhou
- Zirun Wang
- Xin-Jiang He
doc_id: arxiv:2510.21156v1
family_id: arxiv:2510.21156
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Portfolio selection with exogenous and endogenous transaction costs under a
  two-factor stochastic volatility model
url_abs: http://arxiv.org/abs/2510.21156v1
url_html: https://arxiv.org/html/2510.21156v1
venue: arXiv q-fin
version: 1
year: 2025
---


Dong Yana, Ke Zhoua, Zirun Wanga, Xin-Jiang Heb,c,
  
a. School of Statistics, University of International Business and Economics, Beijing, China.
  
b. School of Economics, Zhejiang University of Technology, Hangzhou, China.
  
c. Institute for Industrial System Modernization, Zhejiang University of Technology, Hangzhou, China.
Corresponding author: xinjiang@zjut.edu.cn.

###### Abstract

In this paper, we investigate a portfolio selection problem with transaction costs under a two-factor stochastic volatility structure, where volatility follows a mean-reverting process with a stochastic mean-reversion level. The model incorporates both proportional exogenous transaction costs and endogenous costs modeled by a stochastic liquidity risk process. Using an option-implied approach, we extract an S-shaped utility function that reflects investor behavior and apply its concave envelope transformation to handle the non-concavity. The resulting problem reduces to solving a five-dimensional nonlinear Hamilton–Jacobi–Bellman equation. We employ a deep learning-based policy iteration scheme to numerically compute the value function and the optimal policy. Numerical experiments are conducted to analyze how both types of transaction costs and stochastic volatility affect optimal investment decisions.

Keywords: Portfolio selection; Transaction costs; Stochastic volatility; S-shaped utility function; Deep learning.

## 1 Introduction

Numerous scholars have contributed to the study of portfolio selection, with seminal works such as the single-period mean-variance framework introduced by [[15](https://arxiv.org/html/2510.21156v1#bib.bib15)] and the continuous-time expected utility maximization approach developed by [[16](https://arxiv.org/html/2510.21156v1#bib.bib16)]. These foundational models have laid the groundwork for subsequent research in the field. However, classical models, along with much of the literature built upon them, often operate under the assumption of an idealized, complete market. In reality, financial markets are plagued by frictions, moral hazard, and information asymmetry. To better reflect empirical conditions, this paper focuses on the more realistic setting of an incomplete market, with particular emphasis on transaction costs. Based on their nature, we classify these costs into two categories: exogenous and endogenous transaction costs.

Exogenous transaction costs refer to explicit, directly observable fees incurred per trade, typically including taxes, commissions, and other charges in various forms. Due to the highly heterogeneous and complex nature of such fees, it is difficult to capture exogenous costs using a single realized expression. As a result, numerous studies have explored different functional forms of these costs within the Markowitz framework. Proposed models range from simple fixed transaction costs [[17](https://arxiv.org/html/2510.21156v1#bib.bib17)], linear transaction costs [[18](https://arxiv.org/html/2510.21156v1#bib.bib18)], nonlinear transaction costs [[19](https://arxiv.org/html/2510.21156v1#bib.bib19), [20](https://arxiv.org/html/2510.21156v1#bib.bib20)], to conditionally linear transaction costs that incorporate minimum charge thresholds [[21](https://arxiv.org/html/2510.21156v1#bib.bib21), [22](https://arxiv.org/html/2510.21156v1#bib.bib22)]. Among these, the proportional transaction cost model remains the most widely adopted and extensively studied specification in the literature. Proportional transaction costs can be further divided into two types. Although both assume a fixed cost rate, some studies model costs as proportional to the total trade value [[23](https://arxiv.org/html/2510.21156v1#bib.bib23)], while a larger body of work focuses on costs proportional to the change in asset value resulting from the transaction [[24](https://arxiv.org/html/2510.21156v1#bib.bib24), [25](https://arxiv.org/html/2510.21156v1#bib.bib25), [26](https://arxiv.org/html/2510.21156v1#bib.bib26)]. The latter approach has gained broader acceptance and is generally considered more reflective of real-world market conditions.

While the aforementioned studies are primarily set within the discrete-time Markowitz framework, this approach is inherently static and single-period. It thus fails to accommodate dynamic decision-making that adjusts to evolving market environments. Moreover, a naive extension to a multi-period setting introduces time inconsistency, violating Bellman’s principle of optimality. To address these limitations, this paper adopts Merton’s continuous-time framework and formulates the problem as one of expected utility maximization over time. Several studies on exogenous transaction costs have been developed within the Merton framework [[27](https://arxiv.org/html/2510.21156v1#bib.bib27), [28](https://arxiv.org/html/2510.21156v1#bib.bib28), [61](https://arxiv.org/html/2510.21156v1#bib.bib61)], most of which also employ proportional transaction costs. However, research in continuous time is considerably more challenging than in the single-period case, as it generally requires solving a Hamilton-Jacobi-Bellman (HJB) equation, a process that entails significant mathematical and computational difficulties.

Distinct from exogenous transaction costs, endogenous transaction costs originate from within the transaction process itself and are directly shaped by the behaviors of participating agents. A prominent example is the liquidity cost, which stems from liquidity risk, a pervasive feature of real financial markets. Liquidity risk significantly influences asset pricing, making its integration essential both in derivative valuation and in optimal portfolio selection strategies. As a result, effectively modeling liquidity risk has become an important research focus, spurring investigations into its financial properties and empirical characteristics.

The literature has approached liquidity risk modeling from multiple perspectives. Some studies characterize it through the bid-ask spread [[29](https://arxiv.org/html/2510.21156v1#bib.bib29), [30](https://arxiv.org/html/2510.21156v1#bib.bib30)], while others extend traditional Value-at-Risk (VaR) models by incorporating regularization penalty terms [[31](https://arxiv.org/html/2510.21156v1#bib.bib31), [32](https://arxiv.org/html/2510.21156v1#bib.bib32)]. Another strand of research constructs market-impact functions to capture liquidity effects [[33](https://arxiv.org/html/2510.21156v1#bib.bib33), [34](https://arxiv.org/html/2510.21156v1#bib.bib34), [35](https://arxiv.org/html/2510.21156v1#bib.bib35)]. Additionally, a number of studies model liquidity risk directly as a stochastic process [[36](https://arxiv.org/html/2510.21156v1#bib.bib36), [40](https://arxiv.org/html/2510.21156v1#bib.bib40), [37](https://arxiv.org/html/2510.21156v1#bib.bib37), [38](https://arxiv.org/html/2510.21156v1#bib.bib38), [39](https://arxiv.org/html/2510.21156v1#bib.bib39)].

Notably, [[36](https://arxiv.org/html/2510.21156v1#bib.bib36)] formalized this approach by proposing that the liquidity discount factor follows a stochastic process, while also modeling market liquidity as a mean-reverting stochastic process. These two interrelated processes jointly characterize liquidity risk. In subsequent work, [[40](https://arxiv.org/html/2510.21156v1#bib.bib40)] empirically demonstrated the superiority of this stochastic liquidity modeling approach in the context of European option pricing. More recently, [[39](https://arxiv.org/html/2510.21156v1#bib.bib39)] extended the framework by introducing a more generalized correlation structure among the driving Brownian motions, further generalizing the model originally proposed by [[36](https://arxiv.org/html/2510.21156v1#bib.bib36)].

Beyond transaction costs, the accurate modeling of volatility is equally critical. Early studies, notably the Black-Scholes option pricing model [[41](https://arxiv.org/html/2510.21156v1#bib.bib41)], were built on the assumption of constant volatility. However, this assumption has been widely shown to fail in capturing the dynamic behavior of real-world market volatility. In response, substantial research efforts have been directed toward developing more realistic volatility models. Among these, the stochastic volatility model proposed by [[42](https://arxiv.org/html/2510.21156v1#bib.bib42)] has gained considerable prominence. In this framework, the volatility of the underlying asset is modeled as a stochastic process governed by Cox-Ingersoll-Ross (CIR) dynamics. This formulation not only enables the derivation of semi-analytical solutions for European option prices but also guarantees the non-negativity and mean-reverting property of volatility. Thanks to these desirable features, the Heston model has been widely adopted in numerous portfolio selection studies within the Merton framework [[43](https://arxiv.org/html/2510.21156v1#bib.bib43), [44](https://arxiv.org/html/2510.21156v1#bib.bib44), [45](https://arxiv.org/html/2510.21156v1#bib.bib45)]. Furthermore, building on the Heston model, [[46](https://arxiv.org/html/2510.21156v1#bib.bib46)] introduced a refinement to overcome its limitation in adequately capturing nonlinear mean reversion. Their approach assumes that the mean reversion level itself follows a stochastic process, thereby extending the original Heston model into a two-factor stochastic volatility framework. This enhanced model is adopted in the present study.

Furthermore, the expected utility maximization problem in the Merton framework requires the explicit specification of a utility function. A significant body of literature employs market data from stocks or options to estimate investor utility functions. Researchers have primarily pursued two approaches: some have developed nonparametric methods to recover state-dependent risk aversion functions from observed market data [[47](https://arxiv.org/html/2510.21156v1#bib.bib47), [48](https://arxiv.org/html/2510.21156v1#bib.bib48), [49](https://arxiv.org/html/2510.21156v1#bib.bib49)], while others have calibrated preference parameters by testing parametric asset pricing models against various hypothesized utility specifications [[50](https://arxiv.org/html/2510.21156v1#bib.bib50), [9](https://arxiv.org/html/2510.21156v1#bib.bib9)]. Among these, the option-implied methodology has gained considerable prominence for extracting risk aversion functions. This approach infers the risk-neutral probability density function (PDF) from the implied volatility smile of options. The estimated utility function is then applied to transform this risk-neutral PDF into a subjective PDF, after which the optimal utility function is selected using statistical techniques. A major advantage of this method is that it facilitates clear comparative analysis across different utility functions by maintaining a consistent structural form during estimation. To date, applications have been largely confined to classical utility functions, as exemplified by [[9](https://arxiv.org/html/2510.21156v1#bib.bib9)], although [[4](https://arxiv.org/html/2510.21156v1#bib.bib4)] extended the approach to include HARA-type and certain composite utility functions. This paper substantially broadens the scope by incorporating the S-shaped utility function from prospect theory [[11](https://arxiv.org/html/2510.21156v1#bib.bib11)], which is widely acknowledged for its descriptive accuracy of real investor behavior. Notably, the application of the option-implied approach to recover such an S-shaped utility specification remains scarce [[51](https://arxiv.org/html/2510.21156v1#bib.bib51)], positioning our study as a meaningful contribution toward addressing this gap in the literature.

This paper investigates the continuous-time portfolio selection problem within the Merton framework, formulated as an expected utility maximization problem. We adopt an S-shaped utility function and account for the effects of both exogenous and endogenous transaction costs. To model volatility, we develop a two-factor stochastic model that captures its inherent randomness. This leads to the formulation of an HJB equation, which must be solved numerically. The core computational challenge thus reduces to solving a five-dimensional nonlinear HJB equation. Given the high dimensionality and strong nonlinearity of this equation, we employ Physics-Informed Neural Networks (PINNs) [[52](https://arxiv.org/html/2510.21156v1#bib.bib52)] combined with a deep learning-based policy iteration scheme to obtain accurate and reliable numerical solutions [[53](https://arxiv.org/html/2510.21156v1#bib.bib53), [54](https://arxiv.org/html/2510.21156v1#bib.bib54), [55](https://arxiv.org/html/2510.21156v1#bib.bib55)]. Additionally, the non-concave regions of the S-shaped utility function pose significant optimization difficulties. To overcome this, we primarily utilize the concave envelope transformation technique, which is a well-established approach in the literature for handling non-concave utilities [[56](https://arxiv.org/html/2510.21156v1#bib.bib56), [57](https://arxiv.org/html/2510.21156v1#bib.bib57), [58](https://arxiv.org/html/2510.21156v1#bib.bib58), [59](https://arxiv.org/html/2510.21156v1#bib.bib59), [60](https://arxiv.org/html/2510.21156v1#bib.bib60)]. This treatment significantly improves the stability and tractability of our numerical optimization procedure.

The remainder of this paper is structured as follows. Section 2 develops the wealth dynamics model, incorporating both exogenous and endogenous transaction costs as well as a two-factor stochastic volatility specification. This formulation leads to the expected utility maximization objective and the corresponding five-dimensional HJB equation. In Section 3, we apply an option-implied methodology to comparatively analyze and calibrate the parameters of the S-shaped utility function. Section 4 implements the concave envelope transformation for the utility function and proceeds with the numerical solution of the HJB equation. This section further conducts a comprehensive numerical analysis, providing illustrative examples to investigate the sensitivity of optimal investment strategies to key parameters, particularly the effects of varying exogenous and endogenous transaction costs and stochastic volatility.

## 2 The mode formulation

In this section, we formulate a dynamic portfolio selection model based on a two-factor stochastic volatility model [[2](https://arxiv.org/html/2510.21156v1#bib.bib2)], where stock trading incurs both exogenous transaction costs (proportional transaction costs) and endogenous transaction costs (implicitly resulting from liquidity risks). Consider a financial market consisting of two types of assets: risky stocks and risk-free money accounts with an interest rate rr. We assume that the market is illiquid and that the stochastic processes of stock price, volatility and liquidity risk are established under a physical measure.

To model how liquidity influences equity prices, a market liquidity variable LL is defined, which follows a mean-reverting Ornstein-Uhlenbeck stochastic process as detailed in [[36](https://arxiv.org/html/2510.21156v1#bib.bib36)]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​L=α​(θL−L)​d​t+σL​d​BL,dL=\alpha(\theta\_{L}-L)dt+\sigma\_{L}dB^{L}, |  | (1) |

where α\alpha is the mean-reversion speed, θL\theta\_{L} is the mean-reversion level, and σL\sigma\_{L} is the volatility of market liquidity.

Moreover, the incorporation of proportional transaction costs must address their intrinsic relationship with liquidity risk. From a theoretical perspective, the rise in exogenous transaction costs diminishes trading incentives by compressing profit margins, thereby increasing market illiquidity. We therefore modify the liquidity risk model in Eq. ([1](https://arxiv.org/html/2510.21156v1#S2.E1 "In 2 The mode formulation ‣ Portfolio selection with exogenous and endogenous transaction costs under a two-factor stochastic volatility model")) by introducing a mean-reversion level that increases with the transaction cost rate:

|  |  |  |  |
| --- | --- | --- | --- |
|  | θL​(L)=θ^L+λT​C⋅κT​C⋅Lξ,\theta\_{L}(L)=\hat{\theta}\_{L}+\lambda\_{TC}\cdot\kappa\_{TC}\cdot L^{\xi}, |  | (2) |

where θ^L\hat{\theta}\_{L} denotes the current illiquidity level unaffected by transaction costs, λT​C\lambda\_{TC} represents the sensitivity coefficient quantifying the marginal impact of transaction costs on illiquidity, κT​C\kappa\_{TC} is the proportional transaction costs rate, and ξ∈(0,1)\xi\in(0,1) governs the curvature of the power function. Such a concave function is adopted for its flexibility in modeling how transaction costs nonlinearly increase liquidity risk through curvature adjustments.

Then the price of the underlying asset SS, stochastic volatility vv with its stochastic mean-reversion level θ\theta, and liquidity risk LL satisfy the following stochastic differential equations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {d​St=μ​St​d​t+v​St​d​BtS+β​Lt​St​d​Btγ,d​vt=κ​(θt−vt)​d​t+σ1​vt​d​Btv,d​θt=λ​(η−θt)​d​t+σ2​θt​d​Btθ,d​Lt=α​(θ^L+λT​C⋅κT​C⋅Ltξ−Lt)​d​t+σL​d​BtL,\begin{cases}dS\_{t}=\mu S\_{t}dt+\sqrt{v}S\_{t}dB^{S}\_{t}+\beta L\_{t}S\_{t}dB^{\gamma}\_{t},\\ dv\_{t}=\kappa(\theta\_{t}-v\_{t})dt+\sigma\_{1}\sqrt{v\_{t}}dB^{v}\_{t},\\ d\theta\_{t}=\lambda(\eta-\theta\_{t})dt+\sigma\_{2}\sqrt{\theta\_{t}}dB^{\theta}\_{t},\\ dL\_{t}=\alpha(\hat{\theta}\_{L}+\lambda\_{TC}\cdot\kappa\_{TC}\cdot L^{\xi}\_{t}-L\_{t})dt+\sigma\_{L}dB^{L}\_{t},\end{cases} |  | (3) |

where μ\mu is the drift, and the strictly positive parameter β\beta measures the sensitivity to the level of market liquidity of the asset price. The stochastic volatility vv and its mean-reversion level θ\theta follow mean-reversion processes with their respective mean-reversion levels and speeds. σ1\sigma\_{1} and σ2\sigma\_{2} correspond to the volatility of volatility and the volatility of the stochastic mean-reversion level, respectively. BSB^{S}, BγB^{\gamma}, BvB^{v}, BθB^{\theta} and BLB^{L} are correlated Wiener processes with coefficients specified as: d​BtS​d​Btv=ρ1​d​tdB^{S}\_{t}dB^{v}\_{t}=\rho\_{1}dt, d​BtS​d​Btθ=ρ2​d​tdB^{S}\_{t}dB^{\theta}\_{t}=\rho\_{2}dt, d​Btv​d​Btθ=ρ3​d​tdB^{v}\_{t}dB^{\theta}\_{t}=\rho\_{3}dt, d​BtS​d​Btγ=ρ4​d​tdB^{S}\_{t}dB^{\gamma}\_{t}=\rho\_{4}dt, d​BtS​d​BtL=ρ5​d​tdB\_{t}^{S}dB^{L}\_{t}=\rho\_{5}dt, and d​Btγ​d​BtL=ρ6​d​tdB^{\gamma}\_{t}dB^{L}\_{t}=\rho\_{6}dt.

Now consider an investor who invests an initial endowment of W0W\_{0}, allocating a fraction ω​(t)∈[0,1]\omega(t)\in[0,1] to stocks and the remainder to a bank account earning the risk-free rate rr. To avoid excessive costs from continuous trading, we instead hedge the portfolio in a non-infinitesimal time step of length δ​t\delta t. The associated exogenous transaction costs are assumed to be proportional to the monetary value of the traded stocks. Consequently, the net change in the investor’s wealth over one time step is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​Wt=[r​Wt+(μ−r)​ωt​Wt]​δ​t+β​ωt​Lt​Wt​δ​Btγ+ω​vt​Wt​δ​BtS−κT​C​St​|νt|,\delta W\_{t}=[rW\_{t}+(\mu-r)\omega\_{t}W\_{t}]\delta t+\beta\omega\_{t}L\_{t}W\_{t}\delta B\_{t}^{\gamma}+\omega\sqrt{v\_{t}}W\_{t}\delta B\_{t}^{S}-\kappa\_{TC}S\_{t}|\nu\_{t}|, |  | (4) |

where ν\nu represents the traded number of stocks per period.

Given that the number of stocks held at time tt is ω​(t)​W​(t)S​(t)\frac{\omega(t)W(t)}{S(t)}, we derive an explicit expression for ν\nu by applying Ito^\hat{\text{o}}’s lemma to ν=δ​(ω​WS)\nu=\delta\big(\frac{\omega W}{S}\big) and keeping terms of order O​(δ​t)O(\sqrt{\delta t}):

|  |  |  |
| --- | --- | --- |
|  | ν=(ω−1)​ωS⋅[β​L​W​δ​Bγ+v​W​δ​BS1+κT​C⋅sign​(ν)⋅ω].\nu=\frac{(\omega-1)\omega}{S}\cdot\bigg[\frac{\beta LW\delta B^{\gamma}+\sqrt{v}W\delta B^{S}}{1+\kappa\_{TC}\cdot\text{sign}(\nu)\cdot\omega}\bigg]. |  |

While the precise number of traded stocks cannot be determined in advance, we can calculate the expected transaction costs in a time step as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​{κT​C​S​|ν|}=κT​C1+κT​C⋅sign​(ν)​ω⋅|ω−1|​ω​W⋅𝔼​{|β​L​δ​Bγ+v​δ​BS|}.\mathbb{E}\{\kappa\_{TC}S|\nu|\}=\frac{\kappa\_{TC}}{1+\kappa\_{TC}\cdot\text{sign}(\nu)\omega}\cdot|\omega-1|\omega W\cdot\mathbb{E}\bigg\{\bigg|\beta L\delta B^{\gamma}+\sqrt{v}\delta B^{S}\bigg|\bigg\}. |  | (5) |

Noting the transaction costs rate κT​C<1\kappa\_{TC}<1 and the fraction ω∈[0,1]\omega\in[0,1], κT​C2​ω≪1\kappa\_{TC}^{2}\omega\ll 1, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | κT​C1+κT​C⋅sign​(ν)​ω≈κT​C±κT​C2​ω≈κT​C.\frac{\kappa\_{TC}}{1+\kappa\_{TC}\cdot\text{sign}(\nu)\omega}\approx\kappa\_{TC}\pm\kappa\_{TC}^{2}\omega\approx\kappa\_{TC}. |  | (6) |

To compute the expected absolute value of the sum of two correlated Brownian motions in Eq. ([5](https://arxiv.org/html/2510.21156v1#S2.E5 "In 2 The mode formulation ‣ Portfolio selection with exogenous and endogenous transaction costs under a two-factor stochastic volatility model")), we firstly re-write δ​Bγ\delta B^{\gamma} and δ​BS\delta B^{S} as

|  |  |  |
| --- | --- | --- |
|  | {δ​Bγ=δ​t​Z1,δ​BS=ρ4​δ​t​Z1+1−ρ42​δ​t​Z2,\displaystyle\begin{cases}\delta B^{\gamma}&=\sqrt{\delta t}Z\_{1},\\ \delta B^{S}&=\rho\_{4}\sqrt{\delta t}Z\_{1}+\sqrt{1-\rho\_{4}^{2}}\sqrt{\delta t}Z\_{2},\end{cases} |  |

where Z1,Z2∼𝒩​(0,1)Z\_{1},Z\_{2}\sim\mathscr{N}(0,1), and thus

|  |  |  |
| --- | --- | --- |
|  | 𝔼​{|β​L​δ​Bγ+v​δ​BS|}=2π⋅(β​L+ρ4​v)2+(1−ρ42)​v⋅δ​t\mathbb{E}\bigg\{\bigg|\beta L\delta B^{\gamma}+\sqrt{v}\delta B^{S}\bigg|\bigg\}=\sqrt{\frac{2}{\pi}}\cdot\sqrt{(\beta L+\rho\_{4}\sqrt{v})^{2}+(1-\rho\_{4}^{2})v}\cdot\sqrt{\delta t} |  |

Then the expected proportional transaction costs in one time step can be approximated as

|  |  |  |
| --- | --- | --- |
|  | 𝔼​{κT​C​S​|ν|}=2π​δ​t​κT​C​(1−ω)​ω​W​(β​L+ρ4​v)2+(1−ρ42)​v⋅δ​t.\mathbb{E}\{\kappa\_{TC}S|\nu|\}=\sqrt{\frac{2}{\pi\delta t}}\kappa\_{TC}(1-\omega)\omega W\sqrt{(\beta L+\rho\_{4}\sqrt{v})^{2}+(1-\rho\_{4}^{2})v}\cdot\delta t. |  |

Therefore, in an illiquid market with proportional transaction costs under two-factor stochastic volatility, the investor’s wealth process follows the following dynamics:

|  |  |  |  |
| --- | --- | --- | --- |
|  | δ​W=[r​W+(μ−r)​ω​W]​δ​t+β​ω​L​W​δ​Bγ+ω​v​W​δ​BS−2π​δ​t​κT​C​(1−ω)​ω​W​(β​L+ρ4​v)2+(1−ρ42)​v⋅δ​t.\delta W=[rW+(\mu-r)\omega W]\delta t+\beta\omega LW\delta B^{\gamma}+\omega\sqrt{v}W\delta B^{S}-\sqrt{\frac{2}{\pi\delta t}}\kappa\_{TC}(1-\omega)\omega W\sqrt{(\beta L+\rho\_{4}\sqrt{v})^{2}+(1-\rho\_{4}^{2})v}\cdot\delta t. |  | (7) |

We now formulate a utility maximization model for an investor allocating his or her wealth dynamically between bonds and stocks. The investor’s objective is to maximize the expected utility of terminal wealth at time TT by employing admissible trading strategies 𝒜\mathscr{A}, which adjust portfolio weights between these two assets. The corresponding value function QQ is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Q​(W,v,θ,L,t)=maxω∈𝒜⁡𝔼t​{U​(WT)|Wt=W,vt=v,θt=θ,Lt=L},Q(W,v,\theta,L,t)=\max\_{\omega\in\mathscr{A}}\mathbb{E}\_{t}\bigg\{U(W\_{T})\bigg|W\_{t}=W,v\_{t}=v,\theta\_{t}=\theta,L\_{t}=L\bigg\}, |  | (8) |

where U​(⋅)U(\cdot) denotes the investor’s utility function. The choice of U​(⋅)U(\cdot) is crucial as it should accurately reflect the investor’s risk aversion. Rather than adopting classic utility functions (e.g., exponential, logarithmic or power utilities) directly, we derive the utility function empirically from option prices. Our approach combines statistical methods with machine learning techniques, achieving substantially better performance compared to single classic utility specifications.

With the dynamics of state variables specified in Eqs. ([3](https://arxiv.org/html/2510.21156v1#S2.E3 "In 2 The mode formulation ‣ Portfolio selection with exogenous and endogenous transaction costs under a two-factor stochastic volatility model")) and ([7](https://arxiv.org/html/2510.21156v1#S2.E7 "In 2 The mode formulation ‣ Portfolio selection with exogenous and endogenous transaction costs under a two-factor stochastic volatility model")), the HJB equation is derived as

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxω∈[0,1]⁡{ℒ​Q​(W,v,θ,L,t)}=0,∀(W,v,θ,L,t)∈ΩT,\max\_{\omega\in[0,1]}\bigg\{\mathscr{L}Q(W,v,\theta,L,t)\bigg\}=0,\quad\forall(W,v,\theta,L,t)\in\Omega\_{T}, |  | (9) |

where ΩT=ℝ+×ℝ+×ℝ+×ℝ+×[0,T]\Omega\_{T}=\mathbb{R}\_{+}\times\mathbb{R}\_{+}\times\mathbb{R}\_{+}\times\mathbb{R}\_{+}\times[0,T], and the operator ℒ\mathscr{L} is given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℒ\displaystyle\mathscr{L} | =∂∂t+(r+(μ−r)​ω−2π​δ​t​κT​C​(1−ω)​ω​(β​L+ρ4​v)2+(1−ρ42)​v)​W​∂∂W\displaystyle=\frac{\partial}{\partial t}+\bigg(r+(\mu-r)\omega-\sqrt{\frac{2}{\pi\delta t}}\kappa\_{TC}(1-\omega)\omega\sqrt{(\beta L+\rho\_{4}\sqrt{v})^{2}+(1-\rho\_{4}^{2})v}\bigg)W\frac{\partial}{\partial W} |  | (10) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +12​(β2​L2+v+2​ρ4​β​v​L)​ω2​W2​∂2∂W2+κ​(θ−v)​∂∂v+12​σ12​v​∂2∂v2+λ​(η−θ)​∂∂θ\displaystyle+\frac{1}{2}\bigg(\beta^{2}L^{2}+v+2\rho\_{4}\beta\sqrt{v}L\bigg)\omega^{2}W^{2}\frac{\partial^{2}}{\partial W^{2}}+\kappa(\theta-v)\frac{\partial}{\partial v}+\frac{1}{2}\sigma\_{1}^{2}v\frac{\partial^{2}}{\partial v^{2}}+\lambda(\eta-\theta)\frac{\partial}{\partial\theta} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +12​σ22​θ​∂2∂θ2+α​(θ^+λT​C​κT​C​Lξ−L)​∂∂L+12​σL2​∂2∂L2+ρ1​σ1​v​ω​W​∂2∂W​∂v\displaystyle+\frac{1}{2}\sigma^{2}\_{2}\theta\frac{\partial^{2}}{\partial\theta^{2}}+\alpha(\hat{\theta}+\lambda\_{TC}\kappa\_{TC}L^{\xi}-L)\frac{\partial}{\partial L}+\frac{1}{2}\sigma\_{L}^{2}\frac{\partial^{2}}{\partial L^{2}}+\rho\_{1}\sigma\_{1}v\omega W\frac{\partial^{2}}{\partial W\partial v} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +ρ2​σ2​v​θ​ω​W​∂2∂W​∂θ+(ρ6​β​L+ρ5​v)​σL​ω​W​∂2∂W​∂L+ρ3​σ1​σ2​v​θ​∂2∂v​∂θ,\displaystyle+\rho\_{2}\sigma\_{2}\sqrt{v\theta}\omega W\frac{\partial^{2}}{\partial W\partial\theta}+\bigg(\rho\_{6}\beta L+\rho\_{5}\sqrt{v}\bigg)\sigma\_{L}\omega W\frac{\partial^{2}}{\partial W\partial L}+\rho\_{3}\sigma\_{1}\sigma\_{2}\sqrt{v\theta}\frac{\partial^{2}}{\partial v\partial\theta}, |  |

with the terminal condition Q​(W,v,θ,L,T)=U​(W)Q(W,v,\theta,L,T)=U(W).

## 3 The option-implied utility function

The utility function plays a fundamental role in portfolio optimization models by providing a quantitative characterization of investor risk aversion and formally establishing the risk-return tradeoff. If the utility function is improperly specified, the portfolio optimization framework may become invalid. To develop an appropriate utility specification, we derive the utility function empirically from option prices [[4](https://arxiv.org/html/2510.21156v1#bib.bib4)] by exploiting the theoretical relationship between: (i) the subjective probability density function (PDF) PP, (ii) the risk-neutral probability density function (RN-PDF) QQ, and (iii) the utility function itself:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(ST)=Q​(ST)/U′​(ST)∫(Q​(x)/U′​(x))​𝑑x.P(S\_{T})=\frac{Q(S\_{T})/U^{\prime}(S\_{T})}{\int\big(Q(x)/U^{\prime}(x)\big)dx}. |  | (11) |

Then, once the estimates of PP (subjective PDF) and QQ (RN-PDF) are obtained, we can select a well-behaved functional form for the utility function and calibrate its parameters using machine learning techniques.

### 3.1 Data

China’s options market has grown rapidly in recent years, supported by one of the world’s largest retail and institutional investor bases. To capture utility-based investor preferences in such an active market, we analyze CSI 300 ETF options traded on the Shanghai Stock Exchange (SSE) from June 2020 to June 2024. These European-style options expire on the fourth Wednesday of each month. In this study, we use SSE-reported settlement prices and derive the risk-free rate from Shanghai Interbank Offered Rate (Shibor) overnight rates.

The Chinese options market exhibits distinctive characteristics that necessitate specialized data processing. Our study focuses on pronounced liquidity clustering around at-the-money (ATM) options, with severe illiquidity in deep in-the-money (ITM) or out-of-the-money (OTM) contracts. To address this liquidity concentration while preserving more valuable option types, we filter out contracts with daily trading volumes below 10,000 - a threshold where delta values approach 0 or 1 (indicating deep ITM or deep OTM positions, respectively) - rather than eliminating all ITM options.

Following the aforementioned processing steps, we eliminate options that violate general arbitrage constraints, exhibit implied volatility exceeding 100%, or are priced below two minimum tick sizes. Ultimately, we retain expiration series containing at least five valid option contracts for subsequent analysis.

### 3.2 Estimation of the risk-neutral probability density function

Following the results of [[7](https://arxiv.org/html/2510.21156v1#bib.bib7)], we estimate the RN-PDF through second-order differentiation of option prices:

|  |  |  |  |
| --- | --- | --- | --- |
|  | q​(ST)=er​t​∂2C​(K,t)∂K2|K=ST,q(S\_{T})=e^{rt}\left.\frac{\partial^{2}C(K,t)}{\partial K^{2}}\right|\_{K=S\_{T}}, |  | (12) |

where C​(K,t)C(K,t) denotes the price of a European call option at time tt with strike price KK.

To ensure accurate conversion from implied volatilities to call option prices, we employ the smoothed implied volatility smile method [[14](https://arxiv.org/html/2510.21156v1#bib.bib14)] to obtain fitted implied volatilities. Specifically, we apply the cubic spline method [[8](https://arxiv.org/html/2510.21156v1#bib.bib8)] on the option’s delta spaces to guarantee the fitted volatility curve satisfies arbitrage-free conditions. For extrapolation beyond observable strike prices, we extend the spline function horizontally outside the data range following the idea of [[9](https://arxiv.org/html/2510.21156v1#bib.bib9)]. Then the parameter estimation can be formalized as the following optimization problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | minϕ⁡[λ​∑i=1nwi​[yi−f​(xi;ϕ)]2+(1−λ)​∫[f′′​(x;ϕ)]2​𝑑x],\min\_{\phi}\left[\lambda\sum\_{i=1}^{n}w\_{i}\bigl[y\_{i}-f(x\_{i};\phi)\bigr]^{2}+(1-\lambda)\int\bigl[f^{\prime\prime}(x;\phi)\bigr]^{2}\,dx\right], |  | (13) |

where xix\_{i} and yiy\_{i} denote the delta and implied volatility of option ii respectively, f​(x;ϕ)f(x;\phi) represents the fitted spline function with parameter matrix ϕ\phi, wiw\_{i} is the weighting factor for observation ii, determined by its proportional daily trading volume. The smoothing parameter λ\lambda is set to 0.990.99 to ensure robust fitting performance [[9](https://arxiv.org/html/2510.21156v1#bib.bib9)].

Estimating the RN-PDF reduces to solving an optimization problem efficiently, for which we employ the quasi-Newton algorithm—a second-order method in machine learning. Compared to first-order methods like gradient descent, this approach converges significantly faster while avoiding expensive second-order derivative computations. It demonstrates particular advantages for large-scale parameter optimization, exhibiting numerical stability, robustness, and insensitivity to initial point selection. These characteristics make it especially suitable for our problem of large parameter matrix estimation.

### 3.3 Testing the forecast ability of derived subjective PDFs

Once the RN-PDFs are obtained, one needs to test whether the subjective PDFs estimated via RN-PDFs and utility functions demonstrate strong forecast ability. We first establish the null hypothesis that the estimated subjective PDFs are valid and that option payoffs across different expiration dates are independent. Under this null hypothesis, the inverse probability transformations of the realizations should be independent and uniformly distributed, as specified below:

|  |  |  |  |
| --- | --- | --- | --- |
|  | yt=∫−∞XtP^t​(s)​ds∼i.i.d.​𝒰​(0,1),y\_{t}=\int\_{-\infty}^{X\_{t}}\hat{P}\_{t}(s)\,\mathrm{d}s\sim\text{i.i.d.}\ \mathcal{U}(0,1), |  | (14) |

where XtX\_{t} is a realization at an option expiration date and P^t​(⋅)\hat{P}\_{t}(\cdot) is an estimated subjective PDF.

Following the work of [[10](https://arxiv.org/html/2510.21156v1#bib.bib10)], we conduct a joint test for both uniformity and independence by estimating the following AR(1) model and performing a likelihood ratio test:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Zt−μ=ρ​(Zt−1−μ)+εt,Z\_{t}-\mu=\rho(Z\_{t-1}-\mu)+\varepsilon\_{t}, |  | (15) |

where Zt=Φ−1​(yt)Z\_{t}=\Phi^{-1}(y\_{t}), with Φ\Phi being the standard normal cumulative PDF.

Under the null hypothesis, the parameters in the above equation should satisfy: μ=0,ρ=0\mu=0,\rho=0, and σεt=1\sigma\_{\varepsilon\_{t}}=1. Then we estimate the utility function parameters by solving the likelihood ratio minimization problem:

|  |  |  |  |
| --- | --- | --- | --- |
|  | min⁡LR3=−2​[L​(0,1,0)−L​(μ,σ2,ρ)],\min\mathrm{LR3}=-2\left[L(0,1,0)-L(\mu,\sigma^{2},\rho)\right], |  | (16) |

using the quasi-Newton algorithm, where L​(μ,σ2,ρ)L(\mu,\sigma^{2},\rho) represents the log-likelihood function from Eq. ([15](https://arxiv.org/html/2510.21156v1#S3.E15 "In 3.3 Testing the forecast ability of derived subjective PDFs ‣ 3 The option-implied utility function ‣ Portfolio selection with exogenous and endogenous transaction costs under a two-factor stochastic volatility model")).

We employ the LR3-statistic to jointly test for uniformity and independence, and the LR1-statistic (defined as =−2​[L​(μ^,σ^2,0)−L​(μ^,σ^2,ρ^)]=-2\left[L(\hat{\mu},\hat{\sigma}^{2},0)-L(\hat{\mu},\hat{\sigma}^{2},\hat{\rho})\right]) to test independence individually. Through analysis of these test statistics, we assess whether the estimated subjective PDFs match the true PDFs. When both statistics fail to reject the null hypotheses, we conclude that the derived subjective PDFs accurately predict the true PDFs.

### 3.4 Selecting utility functions using machine learning

We now select an appropriate utility function form whose generated subjective PDFs demonstrate strong forecasting accuracy for the true PDFs. In addition to classical utility functions adopted in [[9](https://arxiv.org/html/2510.21156v1#bib.bib9), [4](https://arxiv.org/html/2510.21156v1#bib.bib4)] (see Appendix [A](https://arxiv.org/html/2510.21156v1#A1 "Appendix A Utility functions in Section 3.4 ‣ Portfolio selection with exogenous and endogenous transaction costs under a two-factor stochastic volatility model") for specifications), we incorporate an S-shaped utility function from prospect theory. The S-shaped function captures loss aversion psychology, characterized by concave utility in the gain domain and convex utility in the loss domain, which makes it particularly well-suited for modeling investor behavior.

However, classical S-shaped utility functions adopted in [[11](https://arxiv.org/html/2510.21156v1#bib.bib11), [12](https://arxiv.org/html/2510.21156v1#bib.bib12)] lack smooth differentiability at the reference point, making them unsuitable for our analysis, requiring continuously differentiable functions. To overcome this limitation, we therefore adopt the hyperbolic tangent utility function recently proposed by [[13](https://arxiv.org/html/2510.21156v1#bib.bib13)], which preserves prospect-theoretic curvature while guaranteeing continuous differentiability. This formulation offers dual advantages: direct parameter control for smoothness requirements and inherited desirable nonlinear properties from its widespread use as a machine learning activation function. The explicit functional form of our selected S-shaped utility function is as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | U​(W)={tanh⁡(k1​(W−W0)),if ​W≥W0−k1k2​tanh⁡(k2​(W0−W)),if ​W<W0,U(W)=\begin{dcases}\tanh(k\_{1}(W-W\_{0})),&\text{if }W\geq W\_{0}\\ -\frac{k\_{1}}{k\_{2}}\tanh(k\_{2}(W\_{0}-W)),&\text{if }W<W\_{0}\end{dcases}, |  | (17) |

where W0W\_{0} denotes the reference point that endogenously partitions outcomes into gain and loss domains, with (k1k\_{1}, k2k\_{2}) parameterizing the differential risk attitudes in these two domains.

To evaluate the forecasting performance of the subjective PDFs generated by these utility functions, we compare their Berkowitz p-values across four distinct forecast horizons, as presented in Table [1](https://arxiv.org/html/2510.21156v1#S3.T1 "Table 1 ‣ 3.4 Selecting utility functions using machine learning ‣ 3 The option-implied utility function ‣ Portfolio selection with exogenous and endogenous transaction costs under a two-factor stochastic volatility model"). All reported p-values are adjusted using Monte Carlo tests as proposed by [[9](https://arxiv.org/html/2510.21156v1#bib.bib9)], where actual realizations of underlying asset prices are repeatedly replaced with pseudo-realizations.

Table 1: Berkowitz statistic p-values(adjusted)

| Forecast Horizon | PDF | LR3 p-value | LR1 p-value |
| --- | --- | --- | --- |
| 1 weeks | Risk neutral | 0.007 | 0.150 |
| Power | 0.057 | 0.098 |
| Exponential | 0.076 | 0.087 |
| HARA | 0.004 | 0.154 |
| Log-power | 0.053 | 0.099 |
| Linear-exponential | 0.073 | 0.087 |
| S-type | 0.211 | 0.085 |
| 2 weeks | Risk neutral | 0.033 | 0.158 |
| Power | 0.101 | 0.117 |
| Exponential | 0.099 | 0.091 |
| HARA | 0.017 | 0.162 |
| Log-power | 0.101 | 0.091 |
| Linear-exponential | 0.098 | 0.117 |
| S-type | 0.199 | 0.106 |
| 3 weeks | Risk neutral | 0.027 | 0.038 |
| Power | 0.048 | 0.039 |
| Exponential | 0.049 | 0.040 |
| HARA | 0.014 | 0.038 |
| Log-power | 0.048 | 0.039 |
| Linear-exponential | 0.049 | 0.040 |
| S-type | 0.033 | 0.043 |
| 4 weeks | Risk neutral | 0.000 | 0.000 |
| Power | 0.000 | 0.000 |
| Exponential | 0.000 | 0.000 |
| HARA | 0.000 | 0.000 |
| Log-power | 0.000 | 0.000 |
| Linear-exponential | 0.000 | 0.000 |
| S-type | 0.001 | 0.000 |

As shown in the Table above, at the three- and four-week horizons, all utility functions fail the LR1 independence test. For the remaining two horizons, most utility functions pass the tests, with the S-shaped specification showing statistically superior performance across all model specifications. These results confirm that the S-shaped utility function generates subjective PDFs with significantly greater predictive capability than alternative functional forms. Based on a comprehensive horizon analysis, we selected the parameter-optimized S-shaped utility function (Eq. [17](https://arxiv.org/html/2510.21156v1#S3.E17 "In 3.4 Selecting utility functions using machine learning ‣ 3 The option-implied utility function ‣ Portfolio selection with exogenous and endogenous transaction costs under a two-factor stochastic volatility model")) at the two-week forecast horizon for subsequent calculations, with the parameters k1=2.27k\_{1}=2.27, k2=2.81k\_{2}=2.81, and W0=4.76W\_{0}=4.76 determined via quasi-Newton optimization.

### 3.5 Concavification of the S-shaped utility

Considering S-shaped utility in a portfolio optimization problem introduces significant mathematical complexities that require careful treatment. The fundamental challenge arises from the fact that the S-shaped utility function destroys the concavity of the value function, causing the associated HJB equation to lack a unique classical solution or even a well-defined viscosity solution in certain regions of the state space. Following the comparison principle established by [[58](https://arxiv.org/html/2510.21156v1#bib.bib58)], under their new definition of viscosity solution, we replace the S-shaped utility with its concave envelope, thereby reducing the original non-concave utility maximization problem to a concave one. This reformulated problem can then be solved using standard analytical or numerical approaches.

For clarity, let U1​(W)U\_{1}(W) and −U2​(−W)-U\_{2}(-W) denote the first and second functions of the S-shaped utility function in Eq. ([17](https://arxiv.org/html/2510.21156v1#S3.E17 "In 3.4 Selecting utility functions using machine learning ‣ 3 The option-implied utility function ‣ Portfolio selection with exogenous and endogenous transaction costs under a two-factor stochastic volatility model")), respectively. Then, there exists a function g:[0,∞)→[0,∞)g\colon[0,\infty)\to[0,\infty) such that g​(W0)≥W0g(W\_{0})\geq W\_{0} for all W0∈[0,∞)W\_{0}\in[0,\infty), satisfying:

|  |  |  |  |
| --- | --- | --- | --- |
|  | U1​(g​(W0)−W0)+U2​(W0)−g​(W0)​U1′​(g​(W0)−W0)=0,U\_{1}(g(W\_{0})-W\_{0})+U\_{2}(W\_{0})-g(W\_{0})U\_{1}^{\prime}(g(W\_{0})-W\_{0})=0, |  | (18) |

and the concave envelope is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | U^​(W)={tanh⁡(2.27⋅(W−4.76)),W≥5.48−0.81+0.32⋅W,W<5.48,\hat{U}(W)=\begin{cases}\tanh\left(2.27\cdot(W-4.76)\right),&W\geq 5.48\\ -0.81+0.32\cdot W,&W<5.48\\ \end{cases}, |  | (19) |

with Wt​p≈5.48W\_{tp}\approx 5.48 being the tangent point of the line from (0,U​(0))(0,U(0)) to the original utility function. The concave envelope U^\hat{U} is constructed by combining this tangent line for lower wealth levels (W<Wt​pW<W\_{tp}) with the original concave segment of the utility function for higher wealth levels (W≥Wt​pW\geq W\_{tp}). As a result, U^\hat{U} is a concave, monotonically increasing, and C1C^{1}-smooth function. It should be noted that since the tangent line is linear in wealth, the investor exhibits risk-neutral behavior within this region. Consequently, for the case where μ>r\mu>r, the optimal allocation to the risky asset is 100% when wealth is below Wt​pW\_{tp}. To illustrate the construction of the concave envelope, we plot the resulting function in Figure [1](https://arxiv.org/html/2510.21156v1#S3.F1 "Figure 1 ‣ 3.5 Concavification of the S-shaped utility ‣ 3 The option-implied utility function ‣ Portfolio selection with exogenous and endogenous transaction costs under a two-factor stochastic volatility model").

![Refer to caption](utility.jpg)


Figure 1: The original S-shaped utility and its concave envelope

## 4 Numerical experiments

### 4.1 Deep learning-driven policy iteration scheme

We note that the operator in Eq. ([10](https://arxiv.org/html/2510.21156v1#S2.E10 "In 2 The mode formulation ‣ Portfolio selection with exogenous and endogenous transaction costs under a two-factor stochastic volatility model")) is quadratic in ω\omega, which allows the optimal policy for the corresponding maximization problem to be expressed explicitly under certain conditions. However, the quotient involving partial derivatives may cause computational issues. To efficiently find optimal policies for our high-dimensional portfolio selection problem, we avoid classical mesh-based iteration schemes, as they are computationally expensive and suffer from the curse of dimensionality. Instead, we employ the method derived from PINNs [[52](https://arxiv.org/html/2510.21156v1#bib.bib52)], a deep learning technique for solving the resulting PDEs. PINNs have emerged as a powerful technique in recent years, achieving remarkable success across a wide range of applications. In our algorithm, according to the universal approximation theorem [[1](https://arxiv.org/html/2510.21156v1#bib.bib1)], both the value function and the optimal policy are approximated by corresponding well-constructed neural networks. Specifically, we define the value network Qϕ:ΩT→ℝQ\_{\phi}:\Omega\_{T}\to\mathbb{R} and the policy network ωψ:ΩT→[0,1]1\omega\_{\psi}:\Omega\_{T}\to[0,1]^{1} as three-layer neural networks:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Qϕ\displaystyle Q\_{\phi} | =f3Q∘tanh∘f2Q∘tanh∘f1Q,\displaystyle=f\_{3}^{Q}\circ\tanh\circ f\_{2}^{Q}\circ\tanh\circ f\_{1}^{Q}, |  | (20) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ωψ\displaystyle\omega\_{\psi} | =sigmoid∘f3ω∘tanh∘f2ω∘tanh∘f1ω,\displaystyle=\operatorname{sigmoid}\circ f\_{3}^{\omega}\circ\tanh\circ f\_{2}^{\omega}\circ\tanh\circ f\_{1}^{\omega}, |  |

where ϕ\phi and ψ\psi denote the network parameters, and the description of the network structures is detailed in Appendix [B](https://arxiv.org/html/2510.21156v1#A2 "Appendix B Components of neural networks ‣ Portfolio selection with exogenous and endogenous transaction costs under a two-factor stochastic volatility model").

Subsequently, in the policy evaluation step, the associated PDE is solved for a given policy by approximating the value function QQ with a neural network. The solution is obtained by minimizing a loss function formed by a summation of the PDE residuals and the terminal condition residuals. Specifically, the loss function during the k-th iteration is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ(k)​(ϕ)=𝔼W,v,θ,L,t​[(ℒωψ(k−1)​Qϕ​(W,v,θ,L,t))2]+𝔼W,v,θ,L​[|Qϕ​(W,v,θ,L,T)−U^​(W)|2].\mathcal{L}^{(k)}(\phi)=\mathbb{E}\_{W,v,\theta,L,t}\left[\left(\mathcal{L}^{\omega\_{\psi^{(k-1)}}}Q\_{\phi}(W,v,\theta,L,t)\right)^{2}\right]+\mathbb{E}\_{W,v,\theta,L}\left[\left|Q\_{\phi}(W,v,\theta,L,T)-\hat{U}(W)\right|^{2}\right]. |  | (21) |

In addition, to enhance the convergence behavior of value function, we adopt a strategic sampling approach that increases the density of interior collocation points relative to boundary points at a ratio of approximately 4:1. Following this, the value network parameters ϕ(k)\phi^{(k)} at the k-th iteration are determined, leading to the policy improvement step where the following optimization problem is solved:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψ(k)=argmax𝜓​𝔼W,v,θ,L,t​[ℒωψ​Qϕ(k)​(W,v,θ,L,t)].\psi^{(k)}=\underset{\psi}{\operatorname{argmax}}\,\mathbb{E}\_{W,v,\theta,L,t}\left[\mathscr{L}^{\omega\_{\psi}}Q\_{\phi^{(k)}}(W,v,\theta,L,t)\right]. |  | (22) |

This maximization step empirically implements the policy improvement procedure by refining the policy network approximation using the newly updated value network. As a result, through alternating steps of policy evaluation and improvement, we obtain the following iteration scheme for solving Eq. ([9](https://arxiv.org/html/2510.21156v1#S2.E9 "In 2 The mode formulation ‣ Portfolio selection with exogenous and endogenous transaction costs under a two-factor stochastic volatility model")) with classical and concavified utility functions:

Algorithm 1  The deep learning-driven policy iteration scheme

1:Given initial values of trainable parameters of networks ϕ(0),ψ(0)\phi^{(0)},\psi^{(0)}

2:Construct value network and control network

3:for k=1,…,Nk=1,\ldots,N do

4:  Conduct the step of policy evaluation by calculating

5:  ϕ(k)=argminϕ​𝔼W,v,θ,L,t​[(ℒωψ(k−1)​Qϕ​(W,v,θ,L,t))2]+𝔼W,v,θ,L​[|Qϕ​(W,v,θ,L,T)−U^​(W)|2]\phi^{(k)}=\underset{\phi}{\operatorname{argmin}}\mathbb{E}\_{W,v,\theta,L,t}\left[\left(\mathcal{L}^{\omega\_{\psi^{(k-1)}}}Q\_{\phi}(W,v,\theta,L,t)\right)^{2}\right]+\mathbb{E}\_{W,v,\theta,L}\left[\left|Q\_{\phi}(W,v,\theta,L,T)-\hat{U}(W)\right|^{2}\right]

6:  if the maximum relative difference between Qϕ(k)Q\_{\phi^{(k)}} and Qϕ(k−1)Q\_{\phi^{(k-1)}} is smaller than 10−410^{-4} then

7:   break

8:  end if

9:  Conduct the step of policy improvement by calculating

10:  ψ(k)=argmax𝜓​𝔼W,v,θ,L,t​[ℒωψ​Qϕ(k)​(W,v,θ,L,t)]\psi^{(k)}=\underset{\psi}{\operatorname{argmax}}\mathbb{E}\_{W,v,\theta,L,t}\left[\mathcal{L}^{\omega\_{\psi}}Q\_{\phi^{(k)}}(W,v,\theta,L,t)\right]

11:end for

12:return Qϕ(k),ωψ(k)Q\_{\phi^{(k)}},\omega\_{\psi^{(k)}}

### 4.2 Validation and order of convergence of our numerical scheme

Given the absence of an analytical solution for the HJB equation ([9](https://arxiv.org/html/2510.21156v1#S2.E9 "In 2 The mode formulation ‣ Portfolio selection with exogenous and endogenous transaction costs under a two-factor stochastic volatility model")), we refer to the classical Merton’s problem [[16](https://arxiv.org/html/2510.21156v1#bib.bib16)] to validate our model formulation. This is done by adopting a power utility function U​(W)=W1−γ1−γU(W)=\frac{W^{1-\gamma}}{1-\gamma} and configuring the parameters in Eq. ([9](https://arxiv.org/html/2510.21156v1#S2.E9 "In 2 The mode formulation ‣ Portfolio selection with exogenous and endogenous transaction costs under a two-factor stochastic volatility model")) accordingly. The parameters are set as follows: γ=0.5\gamma=0.5, r=0.02r=0.02, T=1T=1, μ=0.05\mu=0.05, and the volatility v\sqrt{v} is fixed at 0.160.16. All other parameters in the model are set to zero.

![Refer to caption](figure2.png)


Figure 2: Validation of numerical scheme with zero liquidity risk and zero transaction costs

In Figure [2](https://arxiv.org/html/2510.21156v1#S4.F2 "Figure 2 ‣ 4.2 Validation and order of convergence of our numerical scheme ‣ 4 Numerical experiments ‣ Portfolio selection with exogenous and endogenous transaction costs under a two-factor stochastic volatility model"), for both the values of the value function and the optimal policy, two time points are selected for analysis: t=0 and t=0.5, corresponding to the initial and intermediate stages of the strategy, respectively. In this case, ω∗=μ−rγ​σ2=0.375\omega^{\*}=\frac{\mu-r}{\gamma\sigma^{2}}=0.375. The comparison shows that our algorithm yields a highly accurate estimation, closely matching the analytical solution.

The convergence behavior of our numerical scheme is illustrated in Figure [3](https://arxiv.org/html/2510.21156v1#S4.F3 "Figure 3 ‣ 4.2 Validation and order of convergence of our numerical scheme ‣ 4 Numerical experiments ‣ Portfolio selection with exogenous and endogenous transaction costs under a two-factor stochastic volatility model"), which shows the log distance between our numerical results and the analytical solution to Merton’s problem for each iteration. The rapid convergence of the value function after only a few iterations validates the robustness of our model within the Merton framework.

![Refer to caption](LogDistance.jpg)


Figure 3: Experimental convergence rates with zero liquidity risk and zero transaction costs

### 4.3 Numerical experiments and discussions

In this subsection, we return to the five-dimensional problem, aiming to investigate the convergence behavior of the value function and the numerical solution of the optimal policy under the assumption of an S-shaped utility function. Furthermore, by adjusting the parameters associated with exogenous and endogenous transaction costs, we examine how changes in these cost structures influence the optimal policy, i.e., the resulting shifts in the portfolio of the investors.

Upon finalizing the form of the S-shaped utility function in the , this subsection examines how key parameters, i.e., those governing exogenous and endogenous transaction costs, as well as volatility, affect the optimal investment policy. We analyze the influence of variations in these parameters on the optimal strategy and evaluate whether the resulting changes are consistent with economic intuition. For clarity of exposition, we set t=0.5t=0.5 and fixed W=5.5W=5.5 generate two representative subplots illustrating how the optimal policy evolves with changes in other parameters. The remaining variables are fixed at θ=0.2\theta=0.2, v=0.1v=0.1, L=0.3L=0.3, while all other parameter values are held at their baseline levels, as provided in Table LABEL:tab:default\_params, unless otherwise specified.

Table 2: Default Parameters

| Parameter | Value | Parameter | Value |
| --- | --- | --- | --- |
| rr | 0.010.01 | θ¯\bar{\theta} | 0.60.6 |
| μ\mu | 0.050.05 | λ\lambda | 1.51.5 |
| ρ1\rho\_{1} | 0.50.5 | α\alpha | 2.02.0 |
| ρ2\rho\_{2} | 0.20.2 | β\beta | 0.30.3 |
| ρ3\rho\_{3} | 0.30.3 | κ\kappa | 5.05.0 |
| ρ4\rho\_{4} | 0.50.5 | λT​C\lambda\_{TC} | 5.05.0 |
| ρ5\rho\_{5} | 0.50.5 | κT​C\kappa\_{TC} | 0.4%0.4\% |
| ρ6\rho\_{6} | 0.50.5 | σ1\sigma\_{1} | 0.10.1 |
| σ2\sigma\_{2} | 0.10.1 | σL\sigma\_{L} | 0.20.2 |
| γ\gamma | 0.50.5 | η\eta | 0.150.15 |
| δ​t\delta t | 112\frac{1}{12} | TT | 11 |

#### 4.3.1 The changing of β\beta

![Refer to caption](beta_W.jpg)


(a) The variation with wealth.

![Refer to caption](beta_t.jpg)


(b) The variation with time.

Figure 4: Different β\beta.

We begin by analyzing the effect of β\beta, a parameter that captures the sensitivity of the asset price to the level of market liquidity. Figure [4](https://arxiv.org/html/2510.21156v1#S4.F4 "Figure 4 ‣ 4.3.1 The changing of 𝛽 ‣ 4.3 Numerical experiments and discussions ‣ 4 Numerical experiments ‣ Portfolio selection with exogenous and endogenous transaction costs under a two-factor stochastic volatility model") presents numerical results for β=0.1\beta=0.1, 0.30.3, and 0.50.5, with all other parameters held constant. At a wealth level of W=5W=5, situated in the convex (risk-averse) region of the S-shaped utility function, the investor exhibits cautious behavior. As β\beta increases, indicating that the asset price becomes more responsive to liquidity conditions, the optimal stock holding ratio declines. This response aligns with economic intuition: when asset values are more vulnerable to liquidity shocks, a risk-averse investor will reduce equity exposure to mitigate potential losses. Moreover, at a fixed time t=0.5t=0.5, the relationship between wealth and the optimal stock holding ratio exhibits an inverted S-shaped pattern. In the risk-averse region, a lower β\beta, reflecting lower liquidity-driven price sensitivity, is associated with a higher optimal allocation to stocks. In contrast, within the risk-seeking region of the utility function, the pattern reverses: a higher β\beta leads to a greater stock holding ratio. This asymmetry underscores how investor response to liquidity risk depends critically on the underlying risk preference regime.

#### 4.3.2 The changing of κT​C\kappa\_{TC}

![Refer to caption](ktc_W.jpg)


(a) The variation with wealth.

![Refer to caption](ktc_t.jpg)


(b) The variation with time.

Figure 5: Different κT​C\kappa\_{TC}.

We now turn to the parameter κT​C\kappa\_{TC}, which represents the proportional transaction cost rate. Figure [5](https://arxiv.org/html/2510.21156v1#S4.F5 "Figure 5 ‣ 4.3.2 The changing of 𝜅_{𝑇⁢𝐶} ‣ 4.3 Numerical experiments and discussions ‣ 4 Numerical experiments ‣ Portfolio selection with exogenous and endogenous transaction costs under a two-factor stochastic volatility model") illustrates the optimal stock holding ratio for values of κT​C=0.0%\kappa\_{TC}=0.0\%, 0.4%0.4\%, and 0.8%0.8\%, with all other parameters held constant. The results indicate that variation in κT​C\kappa\_{TC} influences the optimal strategy in a manner qualitatively similar to the liquidity sensitivity parameter β\beta. Although the quantitative impact of κT​C\kappa\_{TC} is more moderate compared to that of β\beta, as reflected by the narrower spread between the curves. Despite this weaker magnitude, the corresponding trend remains statistically and economically discernible, underscoring the importance of incorporating even modest frictions into portfolio choice models.

#### 4.3.3 The changing of σL\sigma\_{L}

![Refer to caption](sigmaL_W.jpg)


(a) The variation with wealth.

![Refer to caption](sigmaL_t.jpg)


(b) The variation with time.

Figure 6: Different σL\sigma\_{L}.

We now examine the effect of σL\sigma\_{L}, the volatility of market liquidity. Figure [6](https://arxiv.org/html/2510.21156v1#S4.F6 "Figure 6 ‣ 4.3.3 The changing of 𝜎_𝐿 ‣ 4.3 Numerical experiments and discussions ‣ 4 Numerical experiments ‣ Portfolio selection with exogenous and endogenous transaction costs under a two-factor stochastic volatility model") displays the optimal stock proportion for values of σL=0.1\sigma\_{L}=0.1, 0.20.2, and 0.30.3, with all other parameters held constant. The results reveal that an increase in σL\sigma\_{L}, while moderate in magnitude, leads to a discernible reduction in the optimal allocation to stocks. This outcome aligns with financial theory: heightened volatility in market liquidity amplifies the uncertainty of transaction execution and potential price impact, thereby increasing the implicit cost of trading. For a risk-averse investor, this elevated uncertainty serves as a deterrent to holding risky assets, prompting a shift toward a more conservative portfolio. The observed inverse relationship underscores the role of liquidity stability as a distinct risk factor in investment decisions, even when its quantitative effect is less pronounced than other market parameters.

#### 4.3.4 The changing of v0v\_{0}

![Refer to caption](v0_W.jpg)


(a) The variation with wealth.

![Refer to caption](v0_t.jpg)


(b) The variation with time.

Figure 7: Different v0v\_{0}.

Finally, we analyze the impact of the initial volatility level, v0v\_{0}, on the optimal investment strategy, as illustrated in Figure [7](https://arxiv.org/html/2510.21156v1#S4.F7 "Figure 7 ‣ 4.3.4 The changing of 𝑣₀ ‣ 4.3 Numerical experiments and discussions ‣ 4 Numerical experiments ‣ Portfolio selection with exogenous and endogenous transaction costs under a two-factor stochastic volatility model"). Given the multi‐dimensional nature of the volatility structure, we focus specifically on v0v\_{0} to isolate its effect, holding all other parameters constant. Numerical results are compared across v0=0.1v\_{0}=0.1, 0.20.2, and 0.30.3. A pronounced inverse relationship is observed: as v0v\_{0} rises, the optimal stock proportion declines significantly. This pattern is consistent with portfolio theory: higher initial volatility elevates the perceived risk of equity holdings, prompting risk-averse investors to reduce their exposure to stocks. The strong sensitivity to v0v\_{0} underscores the critical role of volatility expectations in shaping portfolio choice. It also highlights that, even in a market with liquidity frictions and transaction costs, traditional risk-return considerations remain a dominant driver of investor behavior.

## 5 Conclusion

This study has developed and analyzed a portfolio selection model within a Merton continuous-time framework, incorporating several key features of real-world financial markets. The model accounts for both exogenous proportional transaction costs and endogenous liquidity risk, the latter modeled as a stochastic process, and examines their interplay in an incomplete market setting. A two-factor stochastic volatility structure is integrated, where volatility follows a mean-reverting process with a stochastic long-term mean, allowing for a more realistic representation of market dynamics.

In selecting the investor’s utility function, an option-implied approach was employed to align with observed market behavior. The S-shaped utility function, grounded in prospect theory, was identified as the most statistically suitable specification. To address its inherent non-concavity, a concave envelope transformation was applied, ensuring the resulting optimization problem remains well-posed and computationally tractable. The resulting high-dimensional nonlinear HJB equation was solved using a deep learning-based policy iteration scheme. By leveraging PINNs, the algorithm effectively learned both the value and policy functions, overcoming challenges associated with dimensionality and nonlinearity.

A series of numerical experiments were conducted, validating the robustness and efficiency of the proposed method. More importantly, these experiments quantitatively assessed the distinct influences of exogenous and endogenous transaction costs, as well as stochastic volatility factors, on optimal portfolio allocation. The results underscore the importance of incorporating market frictions and behavioral preferences into dynamic asset allocation models, offering both theoretical insight and practical relevance for portfolio management under realistic financial conditions.

## Appendix A Utility functions in Section 3.4

Below are several classical utility functions frequently referenced in economic analysis. We present their functional forms along with relative risk aversion (RRA):

Example 1: Power utility

The Power utility can be defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | U​(W)=11−k​W1−k,U(W)=\frac{1}{1-k}W^{1-k}, |  | (23) |

Additionally, the relative risk aversion (RRA) of the Power utility can be calculated based on the following formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | R​R​A​(W)=−U′′​(W)U′​(W)​W=k.RRA(W)=-\frac{U^{\prime\prime}(W)}{U^{\prime}(W)}W=k. |  | (24) |

Example 2: Exponential utility

The Exponential utility can be defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | U​(W)=−e−k​Wk,U(W)=-\frac{e^{-kW}}{k}, |  | (25) |

Additionally, the relative risk aversion (RRA) of the Exponential utility can be calculated based on the following formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | R​R​A​(W)=−U′′​(W)U′​(W)​W=k​W.RRA(W)=-\frac{U^{\prime\prime}(W)}{U^{\prime}(W)}W=kW. |  | (26) |

Example 3: HARA utility

The HARA utility can be defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | U​(W)=1k1−1​[k1​W+k2]1−1k1,U(W)=\frac{1}{k\_{1}-1}\left[k\_{1}W+k\_{2}\right]^{1-\frac{1}{k\_{1}}}, |  | (27) |

Additionally, the relative risk aversion (RRA) of the HARA utility can be calculated based on the following formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | R​R​A​(W)=−U′′​(W)U′​(W)​W=Wk1​W+k2.RRA(W)=-\frac{U^{\prime\prime}(W)}{U^{\prime}(W)}W=\frac{W}{k\_{1}W+k\_{2}}. |  | (28) |

Example 4: Log plus power utility

The Log plus power utility is a combination of the logarithmic utility and the power utility, which can be defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | U​(W)=k1​log⁡W+1k2​Wk2,U(W)=k\_{1}\log W+\frac{1}{k\_{2}}W^{k\_{2}}, |  | (29) |

Additionally, the relative risk aversion (RRA) of the Log plus power utility can be calculated based on the following formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | R​R​A​(W)=−U′′​(W)U′​(W)​W=k1+(1−k2)​Wk2k1+Wk2.RRA(W)=-\frac{U^{\prime\prime}(W)}{U^{\prime}(W)}W=\frac{k\_{1}+(1-k\_{2})W^{k\_{2}}}{k\_{1}+W^{k\_{2}}}. |  | (30) |

Example 5: Linear plus exponential utility

The Linear plus exponential utility is a combination of the linear utility and the exponential utility, which can be defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | U​(W)=k1​W−1k2​e−k2​W,U(W)=k\_{1}W-\frac{1}{k\_{2}}e^{-k\_{2}W}, |  | (31) |

Additionally, the relative risk aversion (RRA) of the Linear plus exponential utility can be calculated based on the following formula:

|  |  |  |  |
| --- | --- | --- | --- |
|  | R​R​A​(W)=−U′′​(W)U′​(W)​W=k2​W​e−k2​Wk1+e−k2​W.RRA(W)=-\frac{U^{\prime\prime}(W)}{U^{\prime}(W)}W=\frac{k\_{2}We^{-k\_{2}W}}{k\_{1}+e^{-k\_{2}W}}. |  | (32) |

## Appendix B Components of neural networks

For each layer, the components for the values network Qϕ=f3Q∘tanh∘f2Q∘tanh∘f1QQ\_{\phi}=f\_{3}^{Q}\circ\tanh\circ f\_{2}^{Q}\circ\tanh\circ f\_{1}^{Q} are defined as

|  |  |  |
| --- | --- | --- |
|  | f3Q:ℝNQ→ℝ,x↦W3Q​x+b3Q,f\_{3}^{Q}:\mathbb{R}^{N^{Q}}\rightarrow\mathbb{R},\quad x\mapsto W\_{3}^{Q}x+b\_{3}^{Q}, |  |

|  |  |  |
| --- | --- | --- |
|  | tanh:ℝNQ→ℝNQ,x↦tanh⁡(x),\tanh:\mathbb{R}^{N^{Q}}\rightarrow\mathbb{R}^{N^{Q}},\quad x\mapsto\tanh(x), |  |

|  |  |  |
| --- | --- | --- |
|  | f2Q:ℝNQ→ℝNQ,x↦W2Q​x+b2Q,f\_{2}^{Q}:\mathbb{R}^{N^{Q}}\rightarrow\mathbb{R}^{N^{Q}},\quad x\mapsto W\_{2}^{Q}x+b\_{2}^{Q}, |  |

|  |  |  |
| --- | --- | --- |
|  | tanh:ℝNQ→ℝNQ,x↦tanh⁡(x),\tanh:\mathbb{R}^{N^{Q}}\rightarrow\mathbb{R}^{N^{Q}},\quad x\mapsto\tanh(x), |  |

|  |  |  |
| --- | --- | --- |
|  | f1Q:ℝ5→ℝNQ,x↦W1Q​x+b1Q,f\_{1}^{Q}:\mathbb{R}^{5}\rightarrow\mathbb{R}^{N^{Q}},\quad x\mapsto W\_{1}^{Q}x+b\_{1}^{Q}, |  |

and the components for the control network ωψ=sigmoid∘f3ω∘tanh∘f2ω∘tanh∘f1ω\omega\_{\psi}=\operatorname{sigmoid}\circ f\_{3}^{\omega}\circ\tanh\circ f\_{2}^{\omega}\circ\tanh\circ f\_{1}^{\omega} are given by

|  |  |  |
| --- | --- | --- |
|  | sigmoid:ℝ→ℝ,x↦11+e−x,\operatorname{sigmoid}:\mathbb{R}\rightarrow\mathbb{R},\quad x\mapsto\frac{1}{1+\mathrm{e}^{-x}}, |  |

|  |  |  |
| --- | --- | --- |
|  | f3ω:ℝNω→ℝ,x↦W3ω​x+b3ω,f\_{3}^{\omega}:\mathbb{R}^{N^{\omega}}\rightarrow\mathbb{R},\quad x\mapsto W\_{3}^{\omega}x+b\_{3}^{\omega}, |  |

|  |  |  |
| --- | --- | --- |
|  | tanh:ℝNω→ℝNω,x↦tanh⁡(x),\tanh:\mathbb{R}^{N^{\omega}}\rightarrow\mathbb{R}^{N^{\omega}},\quad x\mapsto\tanh(x), |  |

|  |  |  |
| --- | --- | --- |
|  | f2ω:ℝNω→ℝNω,x↦W2ω​x+b2ω,f\_{2}^{\omega}:\mathbb{R}^{N^{\omega}}\rightarrow\mathbb{R}^{N^{\omega}},\quad x\mapsto W\_{2}^{\omega}x+b\_{2}^{\omega}, |  |

|  |  |  |
| --- | --- | --- |
|  | tanh:ℝNω→ℝNω,x↦tanh⁡(x),\tanh:\mathbb{R}^{N^{\omega}}\rightarrow\mathbb{R}^{N^{\omega}},\quad x\mapsto\tanh(x), |  |

|  |  |  |
| --- | --- | --- |
|  | f1ω:ℝ5→ℝNω,x↦W1ω​x+b1ω.f\_{1}^{\omega}:\mathbb{R}^{5}\rightarrow\mathbb{R}^{N^{\omega}},\quad x\mapsto W\_{1}^{\omega}x+b\_{1}^{\omega}. |  |

Here, NQN\_{Q} and NωN\_{\omega} denote the hidden layer sizes for each network. Unless specified otherwise, these values are set to 64. Note that both networks are optimized using the LBFGS optimizer, with a learning rate set to 10−110^{-1}.

## References

* [1]

  Funahashi, K.-I.
  On the approximate realization of continuous mappings by neural networks.
  Neural networks, 2(3):183–192, 1989.
* [2]

  Lin, S., Lin, X., and He, X.-J.
  Analytically pricing European options with a two-factor Stein–Stein model.
  Journal of Computational and Applied Mathematics, 440:115662, 2024.
* [3]

  Feng, S.-P., Hung, M.-W., and Wang, Y.-H.
  Option pricing with stochastic liquidity risk: Theory and evidence.
  Journal of Financial Markets, 18:77–95, 2014.
* [4]

  Kang, B. J. and Kim, T. S.
  Option-implied risk preferences: an extension to wider classes of utility functions.
  Journal of Financial Markets, 9(2):180–198, 2006.
* [5]

  Carpenter, J. N., Lu, F., and Whitelaw, R. F.
  The real value of China’s stock market.
  Journal of Financial Economics, 139(3):679–696, 2021.
* [6]

  Xue, W.-J. and Zhang, L.-W.
  Stock return autocorrelations and predictability in the Chinese stock market—Evidence from threshold quantile autoregressive models.
  Economic Modelling, 60:391–401, 2017.
* [7]

  Breeden, D. T. and Litzenberger, R. H.
  Prices of state-contingent claims implicit in option prices.
  Journal of business, 621–651, 1978.
* [8]

  Bliss, R. R. and Panigirtzoglou, N.
  Testing the stability of implied probability density functions.
  Journal of Banking and Finance, 26(2-3):381–422, 2002.
* [9]

  Bliss, R. R. and Panigirtzoglou, N.
  Option-implied risk aversion estimates.
  The Journal of Finance, 59(1):407–446, 2004.
* [10]

  Berkowitz, J.
  Testing density forecasts, with applications to risk management.
  Journal of Business and Economic Statistics, 19(4):465–474, 2001.
* [11]

  Kahneman, D. and Tversky, A.
  Prospect theory: An analysis of decision under risk.
  Econometrica, 47(2):263–291, 1979.
* [12]

  Hu, S., Obloj, J., and Zhou, X. Y.
  A casino gambling model under cumulative prospect theory: analysis and algorithm.
  Management Science, 69(4):2474–2496, 2023.
* [13]

  Adjei, P., Gomez-Rosero, S., and Capretz, M. A. M.
  Prospect Utility with Hyperbolic Tangent Function.
  International Journal of Approximate Reasoning, 109440, 2025.
* [14]

  Shimko, D.
  Bounds of probability.
  Risk, 6(4):33–37, 1993.
* [15]

  Markowitz, H. M.
  Portfolio selection.
  The Journal of Finance, 7(1):77–91, 1952.
* [16]

  Merton, R. C.
  Optimum consumption and portfolio rules in a continuous-time model.
  Stochastic Optimization Models in Finance, 621–661, Elsevier, 1975.
* [17]

  Patel, N. R. and Subrahmanyam, M. G.
  A simple algorithm for optimal portfolio selection with fixed transaction costs.
  Management Science, 28(3):303–314, 1982.
* [18]

  Best, M. J. and Hlouskova, J.
  An algorithm for portfolio optimization with transaction costs.
  Management Science, 51(11):1676–1688, 2005.
* [19]

  Olivares-Nadal, A. V. and DeMiguel, V.
  A robust perspective on transaction costs in portfolio optimization.
  Operations Research, 66(3):733–739, 2018.
* [20]

  Chellathurai, T. and Draviam, T.
  Dynamic portfolio selection with nonlinear transaction costs.
  Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences, 461(2062):3183–3212, 2005.
* [21]

  Baule, R.
  Optimal portfolio selection for the small investor considering risk and transaction costs.
  OR Spectrum, 32(1):61–76, 2010.
* [22]

  Lobo, M. S., Fazel, M., and Boyd, S.
  Portfolio optimization with linear and fixed transaction costs.
  Annals of Operations Research, 152(1):341–365, 2007.
* [23]

  Davis, M. H. A. and Norman, A. R.
  Portfolio selection with transaction costs.
  Mathematics of Operations Research, 15(4):676–713, 1990.
* [24]

  Li, B., Wang, J., Huang, D., and Hoi, S. C. H.
  Transaction cost optimization for online portfolio selection.
  Quantitative Finance, 18(8):1411–1424, 2018.
* [25]

  Peng, H., Gan, M., and Chen, X.
  A mean-variance model for optimal portfolio selection with transaction costs.
  IFAC Proceedings Volumes, 41(2):1627–1632, 2008.
* [26]

  Dybvig, P. H. and Pezzo, L.
  Mean-variance portfolio rebalancing with transaction costs.
  Available at SSRN 3373329, 2020.
* [27]

  Choi, U. J., Jang, B.-G., and Koo, H.-K.
  An algorithm for optimal portfolio selection problem with transaction costs and random lifetimes.
  Applied Mathematics and Computation, 191(1):239–252, 2007.
* [28]

  Dai, M. and Zhong, Y.
  Penalty methods for continuous-time portfolio selection with proportional transaction costs.
  Available at SSRN 1210105, 2008.
* [29]

  Bangia, A., Diebold, F. X., Schuermann, T., and Stroughair, J. D.
  Modeling liquidity risk with implications for traditional market risk measurement and management.
  2008.
* [30]

  Abensur, E. O. and de Carvalho, W. P.
  Improving portfolio selection by balancing liquidity-risk-return: Evidence from stock markets.
  Theoretical Economics Letters, 12(2):479–497, 2022.
* [31]

  Al Janabi, M. A. M.
  Multivariate portfolio optimization under illiquid market prospects: a review of theoretical algorithms and practical techniques for liquidity risk management.
  Journal of Modelling in Management, 16(1):288–309, 2021.
* [32]

  Botha, M.
  Portfolio liquidity-adjusted value-at-risk.
  South African Journal of Economic and Management Sciences, 11(2):203–216, 2008.
* [33]

  Ly Vath, V., Mnif, M., and Pham, H.
  A model of optimal portfolio selection under liquidity risk and price impact.
  Finance and Stochastics, 11(1):51–90, 2007.
* [34]

  Caccioli, F., Kondor, I., Marsili, M., and Still, S.
  Liquidity risk and instabilities in portfolio optimization.
  International Journal of Theoretical and Applied Finance, 19(05):1650035, 2016.
* [35]

  Ha, Y. and Zhang, H.
  Algorithmic trading for online portfolio selection under limited market liquidity.
  European Journal of Operational Research, 286(3):1033–1051, 2020.
* [36]

  Feng, S.-P., Hung, M.-W., and Wang, Y.-H.
  Option pricing with stochastic liquidity risk: Theory and evidence.
  Journal of Financial Markets, 18:77–95, 2014.
* [37]

  Tian, Y., Rood, R., and Oosterlee, C. W.
  Efficient portfolio valuation incorporating liquidity risk.
  Quantitative Finance, 13(10):1575–1586, 2013.
* [38]

  Abensur, E. O., Saigal, R., Zhang, S., Song, Y., and Yu, H.
  Stochastic Liquidity Model and Its Applications to Portfolio Selection.
  International Joint Conference on Industrial Engineering and Operations Management, 42–51, Springer, 2019.
* [39]

  Pasricha, P. and He, X.-J.
  Exchange options with stochastic liquidity risk.
  Expert Systems with Applications, 223:119915, 2023.
* [40]

  Feng, S.-P., Hung, M.-W., and Wang, Y.-H.
  The importance of stock liquidity on option pricing.
  International Review of Economics and Finance, 43:457–467, 2016.
* [41]

  Black, F. and Scholes, M.
  The pricing of options and corporate liabilities.
  Journal of Political Economy, 81(3):637–654, 1973.
* [42]

  Heston, S. L.
  A closed-form solution for options with stochastic volatility with applications to bond and currency options.
  The Review of Financial Studies, 6(2):327–343, 1993.
* [43]

  Fouque, J.-P., Sircar, R., and Zariphopoulou, T.
  Portfolio optimization and stochastic volatility asymptotics.
  Mathematical Finance, 27(3):704–745, 2017.
* [44]

  Kraft, H.
  Optimal portfolios and Heston’s stochastic volatility model: an explicit solution for power utility.
  Quantitative Finance, 5(3):303–313, 2005.
* [45]

  Zeng, X. and Taksar, M.
  A stochastic volatility model and optimal portfolio selection.
  Quantitative Finance, 13(10):1547–1558, 2013.
* [46]

  He, X.-J. and Chen, W.
  A closed-form pricing formula for European options under a new stochastic volatility model with a stochastic long-term mean.
  Mathematics and Financial Economics, 15(2):381–396, 2021.
* [47]

  Ait-Sahalia, Y. and Lo, A. W.
  Nonparametric risk management and implied risk aversion.
  Journal of Econometrics, 94(1-2):9–51, 2000.
* [48]

  Jackwerth, J. C.
  Recovering risk aversion from option prices and realized returns.
  The Review of Financial Studies, 13(2):433–451, 2000.
* [49]

  Rosenberg, J. V. and Engle, R. F.
  Empirical pricing kernels.
  Journal of Financial Economics, 64(3):341–372, 2002.
* [50]

  Garcia, R., Luger, R., and Renault, E.
  Empirical assessment of an intertemporal option pricing model with latent variables.
  Journal of Econometrics, 116(1-2):49–83, 2003.
* [51]

  Driessen, J. and Maenhout, P.
  An empirical portfolio perspective on option pricing anomalies.
  Review of Finance, 11(4):561–603, 2007.
* [52]

  Raissi, M., Perdikaris, P., and Karniadakis, G. E.
  Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations.
  Journal of Computational Physics, 378:686–707, 2019.
* [53]

  Alla, A., Falcone, M., and Kalise, D.
  An efficient policy iteration algorithm for dynamic programming equations.
  SIAM Journal on Scientific Computing, 37(1):A181–A200, 2015.
* [54]

  Forsyth, P. A. and Labahn, G.
  Numerical methods for controlled Hamilton-Jacobi-Bellman PDEs in finance.
  Journal of Computational Finance, 11(2):1, 2007.
* [55]

  Kerimkulov, B., Siska, D., and Szpruch, L.
  Exponential convergence and stability of Howard’s policy improvement algorithm for controlled diffusions.
  SIAM Journal on Control and Optimization, 58(3):1314–1340, 2020.
* [56]

  Liang, Z. and Liu, Y.
  A classification approach to general S-shaped utility optimization with principals’ constraints.
  SIAM Journal on Control and Optimization, 58(6):3734–3762, 2020.
* [57]

  Davey, A. and Zheng, H.
  Deep Learning Methods for S Shaped Utility Maximisation with a Random Reference Point.
  arXiv preprint arXiv:2410.05524, 2024.
* [58]

  Dai, M., Kou, S., Qian, S., and Wan, X.
  Nonconcave utility maximization with portfolio bounds.
  Management Science, 68(11):8368–8385, 2022.
* [59]

  Reichlin, C.
  Utility maximization with a given pricing measure when the utility is not necessarily concave.
  Mathematics and Financial Economics, 7(4):531–556, 2013.
* [60]

  Bian, B., Chen, X., and Xu, Z. Q.
  Utility maximization under trading constraints with discontinuous utility.
  SIAM Journal on Financial Mathematics, 10(1):243–260, 2019.
* [61]

  Dai, M., Xu, Z. Q., and Zhou, X. Y.
  Continuous-time Markowitz’s model with transaction costs.
  SIAM Journal on Financial Mathematics, 1(1):96–125, 2010.