---
authors:
- Wenxuan Zhang
- Yixiao Guo
- Benzhuo Lu
doc_id: arxiv:2510.27132v1
family_id: arxiv:2510.27132
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Exact Terminal Condition Neural Network for American Option Pricing Based on
  the Black-Scholes-Merton Equations
url_abs: http://arxiv.org/abs/2510.27132v1
url_html: https://arxiv.org/html/2510.27132v1
venue: arXiv q-fin
version: 1
year: 2025
---


Wenxuan Zhang111These authors contributed equally.
[zhangwenxuan17@mails.ucas.ac.cn](mailto:zhangwenxuan17@mails.ucas.ac.cn)

Yixiao Guo222These authors contributed equally.
[guoyixiao@lsec.cc.ac.cn](mailto:guoyixiao@lsec.cc.ac.cn)

Benzhuo Lu
[bzlu@lsec.cc.ac.cn](mailto:bzlu@lsec.cc.ac.cn)
SKLMS, ICMSEC, NCMIS, Academy of Mathematics and Systems Science, Chinese Academy of Sciences, Beijing 100190, China
SKLMS, Institute of Computational Mathematics and Scientific/Engineering Computing, Academy of Mathematics and Systems Science, Chinese Academy of Sciences, Beijing 100190, China
School of Mathematical Sciences, University of Chinese Academy of Sciences, Beijing 100049, China

###### Abstract

This paper proposes the Exact Terminal Condition Neural Network (ETCNN), a deep learning framework for accurately pricing American options by solving the Black-Scholes-Merton (BSM) equations.
The ETCNN incorporates carefully designed functions that ensure the numerical solution not only exactly satisfies the terminal condition of the BSM equations but also matches the non-smooth and singular behavior of the option price near expiration.
This method effectively addresses the challenges posed by the inequality constraints in the BSM equations and can be easily extended to high-dimensional scenarios. Additionally, input normalization is employed to maintain the homogeneity. Multiple experiments are conducted to demonstrate that the proposed method achieves high accuracy and exhibits robustness across various situations, outperforming both traditional numerical methods and other machine learning approaches.

###### keywords:

Black-Scholes-Merton equations, American option pricing, Deep learning, Exact terminal condition, Singularity

## 1 Introduction

Options are an important class of financial derivatives, and their valuation is a central issue in quantitative finance.
Fairly pricing options has been a longstanding challenge, especially for complex options.
Since Black, Scholes, and Merton proposed the revolutionary Black-Scholes-Merton (BSM) model [[27](https://arxiv.org/html/2510.27132v1#bib.bib27), [33](https://arxiv.org/html/2510.27132v1#bib.bib33)], the field of option pricing has experienced rapid and significant development.
However, explicit analytical solutions to the BSM equations are available only for a limited number of cases, such as single-asset European options [[27](https://arxiv.org/html/2510.27132v1#bib.bib27), [33](https://arxiv.org/html/2510.27132v1#bib.bib33)], European options on the maximum or minimum of two assets without dividends [[25](https://arxiv.org/html/2510.27132v1#bib.bib25)], European options to exchange one asset for another [[17](https://arxiv.org/html/2510.27132v1#bib.bib17)], and certain European lookback options [[5](https://arxiv.org/html/2510.27132v1#bib.bib5)]. For most other types of options, pricing still relies on numerical and approximate methods.

The pricing of American options is inherently more complicated than that of European options, as option holders have the right to exercise their options at any time prior to expiration.
Explicit solutions for American options are generally far from available.
As a result, numerical approximation techniques, such as the Barone-Adesi-Whaley (BAW) method,
the binomial tree (BT) model, finite difference (FD) methods, and Monte Carlo (MC) simulations, are widely employed in the industry to price American options.
By dropping a small term in the partial differential equation (PDE), Barone-Adesi and Whaley derived an analytical approximation for American options within the BSM framework [[4](https://arxiv.org/html/2510.27132v1#bib.bib4)].
An early attempt using the binomial tree model was made by Cox, Ross, and Rubinstein (CRR model) [[21](https://arxiv.org/html/2510.27132v1#bib.bib21)], while [[19](https://arxiv.org/html/2510.27132v1#bib.bib19), [30](https://arxiv.org/html/2510.27132v1#bib.bib30), [20](https://arxiv.org/html/2510.27132v1#bib.bib20), [31](https://arxiv.org/html/2510.27132v1#bib.bib31)] proposed some advanced tree methods that converge faster.
Brennan and Schwartz proposed a finite difference method for solving the BSM equations for American put options [[18](https://arxiv.org/html/2510.27132v1#bib.bib18)].
Broadie and Glasserman developed a general algorithm based on Monte Carlo simulation to price options [[35](https://arxiv.org/html/2510.27132v1#bib.bib35)].
Longstaff and Schwartz further refined this approach by introducing the Least Squares Monte Carlo (LSM) method, which prices American options by replacing the future expectation with a least squares interpolation [[26](https://arxiv.org/html/2510.27132v1#bib.bib26)].

Compared to single-asset options, multi-asset options are more complicated to price since there are more sources of randomness to consider.
Numerous attempts have been made to employ numerical methods to price them.
The BEG method, introduced by Boyle, Evnine, and Gibbs, utilized the binomial tree method for multi-asset scenarios by incorporating correlated asset price paths across multiple dimensions [[28](https://arxiv.org/html/2510.27132v1#bib.bib28)].
The finite difference method can also be applied in high-dimensional situations [[34](https://arxiv.org/html/2510.27132v1#bib.bib34)].
However, both the binomial tree (BT) and finite difference (FD) methods become computationally expensive when extended to high-dimensional cases, especially when more than three underlying assets are involved [[32](https://arxiv.org/html/2510.27132v1#bib.bib32)].
Monte Carlo (MC) simulations can be more easily applied in high-dimensional cases, but they suffer from slow convergence rates and face difficulties in accurately addressing the free boundary issue inherent in American options [[35](https://arxiv.org/html/2510.27132v1#bib.bib35)].

To address these challenges, deep learning approaches have emerged as promising alternatives in recent years.
Dhiman and Hu applied physics-informed neural network (PINN) [[1](https://arxiv.org/html/2510.27132v1#bib.bib1)] to solve BSM equations for single-asset options [[6](https://arxiv.org/html/2510.27132v1#bib.bib6)], while Gatta et al. extended PINN to multi-asset American put options [[37](https://arxiv.org/html/2510.27132v1#bib.bib37)].
Sirignano and Spiliopoulos explored the multi-asset BSM equations using the deep Galerkin method (DGM) with similar loss functions [[46](https://arxiv.org/html/2510.27132v1#bib.bib46)].
The deep parametric PDE method [[9](https://arxiv.org/html/2510.27132v1#bib.bib9)], developed by Glau and Wunderlich, trains neural networks to approximate BSM solutions across a wide range of input parameters.
Another influential framework, the deep BSDE method, developed by Han, Jentzen, and E [[7](https://arxiv.org/html/2510.27132v1#bib.bib7)], reformulates the PDE as a backward stochastic differential equation.
This method has been extended to multi-asset American options by Negyesi and Oosterlee [[8](https://arxiv.org/html/2510.27132v1#bib.bib8)].
However, the deep BSDE framework is limited to producing solutions at individual points, rather than pricing the entire surface.

In this paper, we focus on American options and provide approximate solutions over the spatial-temporal domain.
The problem is formulated as a partial differential equation (PDE) in a linear complementarity form, which includes both equalities and inequalities, as well as a terminal boundary condition.
Two primary challenges arise when solving these equations.
First, the presence of inequalities complicates the solution process, as the problem can be reformulated as a Stefan-type free-boundary problem, where the boundaries are unknown [[10](https://arxiv.org/html/2510.27132v1#bib.bib10)].
Second, singular behaviors may arise near maturity due to the non-differentiability of the payoff function.
These singularities cause the derivative of the option price to approach infinity near the terminal, posing challenges for directly using neural network methods to obtain high-accuracy solutions.
As shown in our experiments in Section [4](https://arxiv.org/html/2510.27132v1#S4 "4 Numerical Results for American Options ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations"), the accuracy of the solution deteriorates significantly near these critical points if singularities are not appropriately addressed.

To address these challenges, we introduce the Exact Terminal Condition Neural Network (ETCNN), a deep learning method designed to automatically satisfy the terminal condition.
The primary approach involves constructing a function g2g\_{2} that exactly satisfies the terminal condition. The solution is then formulated as the sum of g2g\_{2} and the product of a certain function g1g\_{1} and a neural network approximation, where g1g\_{1} vanishes at the terminal.
However, our experiments indicate that not all functions satisfying the terminal conditions necessarily yield higher accuracy. The effectiveness of the method is heavily dependent on the smoothness and structure of the residual difference between the true solution and the chosen function g2g\_{2}.
Therefore, g2g\_{2} is carefully constructed not only to satisfy the terminal condition, but also to preserve the differentiability characteristics of the exact solution and exhibit appropriate asymptotic behavior as time approaches expiration.
We provide both mathematical analysis and financial interpretations for designing suitable forms of g2g\_{2} applicable to a wide range of American option pricing scenarios.
Additionally, we design an input normalization layer to normalize the underlying asset prices in the input vector of the network, which can further improve the accuracy of the model.

Our approach has the following primary advantages. First, compared to PINN, ETCNN fully aligns with the true solution at the terminal, eliminating boundary condition errors associated with collocation methods and significantly improving solution accuracy.
Second, our network eliminates the need to include the boundary term in the objective loss function. This removes the hyperparameter assigned to the weight of the boundary loss term, thus simplifying hyperparameter tuning and reducing training complexity.
Third, the method effectively addresses the free-boundary challenge inherent in BSM equations for American options. Rather than directly solving for the free boundary, it enables an accurate determination of the boundary in an indirect way.
Fourth, ETCNN accurately captures the singularity behavior near the terminal, enhancing solution precision in these critical regions.
Finally, our method can be easily extended to high-dimensional cases, maintaining high accuracy in complex multi-asset scenarios where traditional methods are often ineffective.

We conduct extensive experiments on both single-asset and multi-asset American options, corresponding to low-dimensional and high-dimensional BSM equations.
These experiments consider various terminal boundary conditions and a wide range of equation coefficients, highlighting the universality and robustness of our method.
The results demonstrate that our ETCNN improves accuracy by 1-2 orders of magnitude compared to PINN and achieves or even exceeds the accuracy of traditional numerical methods in low-dimensional cases. Moreover, in high-dimensional scenarios where traditional methods face significant challenges, our approach consistently achieves high accuracy.

The structure of this paper is organized as follows.
Section [2](https://arxiv.org/html/2510.27132v1#S2 "2 Preliminaries ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations") introduces the mathematical formulation of the BSM model for option pricing and provides an overview of the PINN framework.
Section [3](https://arxiv.org/html/2510.27132v1#S3 "3 Methodology and Formulation ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations") presents the architecture of the ETCNN, key criteria for designing the exact terminal function g2g\_{2}, and the methodological formulation for American options.
Section [4](https://arxiv.org/html/2510.27132v1#S4 "4 Numerical Results for American Options ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations") reports the result of numerical experiments, and compares the performance of our method with PINN and other numerical approaches.
Finally, Section [5](https://arxiv.org/html/2510.27132v1#S5 "5 Conclusions ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations") summarizes our work and outlines potential directions for future research.

## 2 Preliminaries

### 2.1 BSM Equations for Option Pricing

This section presents the BSM equations for option pricing problems. Section [2.1.1](https://arxiv.org/html/2510.27132v1#S2.SS1.SSS1 "2.1.1 BSM Equations for European Options ‣ 2.1 BSM Equations for Option Pricing ‣ 2 Preliminaries ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations") introduces the BSM equations for European options, which have the simplest form of these equations. Section [2.1.2](https://arxiv.org/html/2510.27132v1#S2.SS1.SSS2 "2.1.2 BSM Equations for American Options ‣ 2.1 BSM Equations for Option Pricing ‣ 2 Preliminaries ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations") to [2.1.4](https://arxiv.org/html/2510.27132v1#S2.SS1.SSS4 "2.1.4 High-Dimensional BSM Equations for Multi-Asset Options ‣ 2.1 BSM Equations for Option Pricing ‣ 2 Preliminaries ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations") focuses on the BSM equations for American options, which are the central theme of this article. These sections will cover low and high-dimensional forms, along with a discussion of their properties.

#### 2.1.1 BSM Equations for European Options

This model includes two types of assets, risk-free assets and risky assets. The value of risk-free assets can be described by a deterministic process,

|  |  |  |
| --- | --- | --- |
|  | d​R​(t)=r​R​(t)​d​t,dR(t)=rR(t)dt, |  |

where rr is the risk-free rate and is assumed to be a constant under the BSM model. Risky assets typically serve as the underlying assets for options contracts and include different financial products such as stocks, stock indices, and futures. The BSM model assumes that
the value of risky assets s=S​(t)s=S(t) follows a geometric Brownian motion,

|  |  |  |
| --- | --- | --- |
|  | d​S​(t)=μ​S​(t)​d​t+σ​S​(t)​d​W​(t),dS(t)=\mu S(t)dt+\sigma S(t)dW(t), |  |

where μ\mu is the drift, σ>0\sigma>0 is the volatility, and W​(t)W(t) is a standard Brownian motion. Both σ\sigma and rr are expressed in annualized terms. In the geometric Brownian motion framework, the drift and volatility are assumed to remain constant.

Let V=V​(s,t)=V​(S​(t),t)V=V(s,t)=V(S(t),t) be the price of a single-asset European option. According to Ito^\hat{\text{o}}’s lemma,

|  |  |  |
| --- | --- | --- |
|  | d​V​(S​(t),t)=(∂V∂t+μ​S​(t)​∂V∂s+12​σ2​S​(t)2​∂2V∂s2)​d​t+σ​S​(t)​∂V∂s​d​W​(t).dV(S(t),t)=\Big(\frac{\partial V}{\partial t}+\mu S(t)\frac{\partial V}{\partial s}+\frac{1}{2}\sigma^{2}S(t)^{2}\frac{\partial^{2}V}{\partial s^{2}}\Big)dt+\sigma S(t)\frac{\partial V}{\partial s}dW(t). |  |

To determine the price of an option with an underlying asset following the above geometric Brownian motion, a self-financing trading strategy is used. This strategy dynamically adjusts the risk-free asset and the underlying asset to replicate the option’s payoff profile. Let X​(t)X(t) denote the value of a portfolio at time tt, consisting of Δ​(t)\Delta(t) shares of the underlying asset, with the remainder X​(t)−Δ​(t)​S​(t)X(t)-\Delta(t)S(t) invested in a risk-free asset at rate rr.
The self-financing assumption implies that changes in the
portfolio are solely attributed to gains or losses in the underlying securities, with no impact from changes in the holdings [[29](https://arxiv.org/html/2510.27132v1#bib.bib29)]. The
change of the portfolio is

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​X​(t)\displaystyle dX(t) | =Δ​(t)​d​S​(t)+r​(X​(t)−Δ​(t)​S​(t))​d​t\displaystyle=\Delta(t)dS(t)+r(X(t)-\Delta(t)S(t))dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(r​X​(t)+(μ−r)​Δ​(t)​S​(t))​d​t+σ​Δ​(t)​S​(t)​d​W​(t).\displaystyle=\big(rX(t)+(\mu-r)\Delta(t)S(t)\big)dt+\sigma\Delta(t)S(t)dW(t). |  |

By selecting the hedge ratio Δ​(t)\Delta(t) and portfolio value X​(t)X(t) such that the terminal payoff of X​(T)X(T) matches the payoff of the option V​(T)V(T) and ensuring
d​X​(t)=d​V​(t)dX(t)=dV(t) for all tt, the portfolio value X​(t)X(t) at any time tt equals the option’s theoretical price. From this, we have the following equations,

|  |  |  |
| --- | --- | --- |
|  | {∂V∂t+μ​S​(t)​∂V∂s+12​σ2​S​(t)2​∂2V∂s2=r​X​(t)+(μ−r)​Δ​(t)​S​(t),σ​S​(t)​∂V∂s=σ​Δ​(t)​S​(t),X​(t)=V​(t).\left\{\begin{aligned} &\quad\frac{\partial V}{\partial t}+\mu S(t)\frac{\partial V}{\partial s}+\frac{1}{2}\sigma^{2}S(t)^{2}\frac{\partial^{2}V}{\partial s^{2}}=rX(t)+(\mu-r)\Delta(t)S(t),\\ &\quad\sigma S(t)\frac{\partial V}{\partial s}=\sigma\Delta(t)S(t),\\ &\quad X(t)=V(t).\end{aligned}\right. |  |

By simplifying the above equations and considering the boundary conditions, the celebrated BSM equation for single-asset European options is obtained,

|  |  |  |  |
| --- | --- | --- | --- |
|  | {∂V∂t+12​σ2​s2​∂2V∂s2+r​s​∂V∂s−r​V=0,∀s≥0,t∈[0,T),V​(s,T)=Φ​(s),∀s≥0.\left\{\begin{aligned} &\quad\frac{\partial V}{\partial t}+\frac{1}{2}\sigma^{2}s^{2}\frac{\partial^{2}V}{\partial s^{2}}+rs\frac{\partial V}{\partial s}-rV=0,\quad\forall s\geq 0,t\in[0,T),\\ &\quad V(s,T)=\Phi(s),\quad\forall s\geq 0.\end{aligned}\right. |  | (1) |

The solution to this equation yields the price of European options. The boundary condition is applied at the expiration date t=Tt=T, thus it is referred to as a terminal condition. Φ​(s)\Phi(s) is the payoff of the function at t=Tt=T. Denote

|  |  |  |
| --- | --- | --- |
|  | x+=max⁡(x,0)={xif​x≥0,0if​x<0,x^{+}=\max(x,0)=\begin{cases}x&\text{if}\ x\geq 0,\\ 0&\text{if}\ x<0,\end{cases} |  |

as an abbreviation.
For European call options, Φ​(s)=(s−K)+\Phi(s)=(s-K)^{+} and for European put options, Φ​(s)=(K−s)+\Phi(s)=(K-s)^{+}. Here, KK is the strike price, which is predetermined in the contract.

If the underlying asset pays a constant continuous dividend yield qq, the BSM equation is modified as:

|  |  |  |
| --- | --- | --- |
|  | {∂V∂t+12​σ2​s2​∂2V∂s2+(r−q)​s​∂V∂s−r​V=0,∀s≥0,t∈[0,T),V​(s,T)=Φ​(s),∀s≥0.\left\{\begin{aligned} &\quad\frac{\partial V}{\partial t}+\frac{1}{2}\sigma^{2}s^{2}\frac{\partial^{2}V}{\partial s^{2}}+(r-q)s\frac{\partial V}{\partial s}-rV=0,\quad\forall s\geq 0,t\in[0,T),\\ &\quad V(s,T)=\Phi(s),\quad\forall s\geq 0.\end{aligned}\right. |  |

Note that qq only appears in the coefficients of the first-order derivative, but not in the coefficients of VV. Therefore, it is not simply a replacement of rr with r−qr-q.

#### 2.1.2 BSM Equations for American Options

American options differ from European ones in that they can be exercised early. The BSM equations for American options can be formulated similarly to Eq. ([1](https://arxiv.org/html/2510.27132v1#S2.E1 "In 2.1.1 BSM Equations for European Options ‣ 2.1 BSM Equations for Option Pricing ‣ 2 Preliminaries ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations")), but with modifications to incorporate their early exercise feature. We define the following operator for the primary equation,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℱ​(V​(s,t))=∂V∂t+12​σ2​s2​∂2V∂s2+(r−q)​s​∂V∂s−r​V.\mathcal{F}\big(V(s,t)\big)=\frac{\partial V}{\partial t}+\frac{1}{2}\sigma^{2}s^{2}\frac{\partial^{2}V}{\partial s^{2}}+(r-q)s\frac{\partial V}{\partial s}-rV. |  | (2) |

The terminal condition Φ​(s)\Phi(s) also represents the intrinsic value, as it is the payoff obtained by exercising the option immediately. The time value of the option is defined as the difference between an option price and its intrinsic value, expressed as follows,

|  |  |  |
| --- | --- | --- |
|  | 𝒯​𝒱​(V​(s,t))=V​(s,t)−Φ​(s).\mathcal{TV}\big(V(s,t)\big)=V(s,t)-\Phi(s). |  |

The time value of an American option must always be nonnegative to avoid risk-free arbitrage opportunities. Otherwise, arbitrageurs can buy options at price V​(s,t)V(s,t), exercise them immediately to receive the payoff Φ​(s)\Phi(s), and secure a risk-free positive profit of Φ​(s)−V​(s,t)\Phi(s)-V(s,t). To prevent arbitrage opportunities, the price of American options V​(s,t)V(s,t) satisfies the following linear complementarity conditions
[[36](https://arxiv.org/html/2510.27132v1#bib.bib36)],

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | | | | | |
|  |  | ℱ​(V​(s,t))≤0,∀s≥0,t∈[0,T),\displaystyle\quad\mathcal{F}\big(V(s,t)\big)\leq 0,\quad\forall s\geq 0,t\in[0,T), |  |  | (3a) |
|  |  | 𝒯​𝒱​(V​(s,t))≥0,∀s≥0,t∈[0,T),\displaystyle\quad\mathcal{TV}\big(V(s,t)\big)\geq 0,\quad\forall s\geq 0,t\in[0,T), |  |  | (3b) |
|  |  | ℱ​(V​(s,t))⋅𝒯​𝒱​(V​(s,t))=0,∀s≥0,t∈[0,T),\displaystyle\quad\mathcal{F}\big(V(s,t)\big)\cdot\mathcal{TV}\big(V(s,t)\big)=0,\quad\forall s\geq 0,t\in[0,T), |  |  | (3c) |
|  |  | V​(s,T)=Φ​(s),∀s≥0,\displaystyle\quad V(s,T)=\Phi(s),\quad\forall s\geq 0, |  |  | (3d) |

These complementarity conditions introduce additional complexities compared to Eq. ([1](https://arxiv.org/html/2510.27132v1#S2.E1 "In 2.1.1 BSM Equations for European Options ‣ 2.1 BSM Equations for Option Pricing ‣ 2 Preliminaries ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations")). Specifically, they contain inequality constraints that complicate both analytical and numerical methods. Moreover, Eq. ([3c](https://arxiv.org/html/2510.27132v1#S2.E3.3 "In 3 ‣ 2.1.2 BSM Equations for American Options ‣ 2.1 BSM Equations for Option Pricing ‣ 2 Preliminaries ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations")) ensures that at least one of the inequalities must hold with equality, but the specific regions where each inequality becomes an equality are unknown in advance. Additionally, Φ​(s)\Phi(s) is typically non-differentiable, which adds further challenges in numerical approximation.

#### 2.1.3 Free Boundary Property in American Options

The inequality constraints give rise to the free boundary problem, which poses a significant challenge in the valuation of American options. To illustrate this, consider the case of an American put option. When the price of the underlying asset ss is low enough, immediate exercise of the option yields a payoff that exceeds the expected benefit of holding the option. This region is referred to as the stopping region.
There exists a function S∗​(t)S^{\*}(t),
which defines the stopping region as the set of points below its curve,

|  |  |  |
| --- | --- | --- |
|  | 𝒮={0≤s≤S∗(t),0≤t≤T}={(s,t):V(s,t)=(K−s)+}.\mathcal{S}=\{0\leq s\leq S^{\*}(t),0\leq t\leq T\}=\{(s,t):V(s,t)=(K-s)^{+}\}. |  |

The complementary region is called the continuation region, denoted by

|  |  |  |
| --- | --- | --- |
|  | 𝒞={s>S∗​(t),0≤t≤T}={(s,t):V​(s,t)>(K−s)+}.\mathcal{C}=\{s>S^{\*}(t),0\leq t\leq T\}=\{(s,t):V(s,t)>(K-s)^{+}\}. |  |

However, S∗​(t)S^{\*}(t) is an unknown function, thus, its function curve is called a free boundary.

In the stopping region, Eq. ([3b](https://arxiv.org/html/2510.27132v1#S2.E3.2 "In 3 ‣ 2.1.2 BSM Equations for American Options ‣ 2.1 BSM Equations for Option Pricing ‣ 2 Preliminaries ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations")) holds equal.
If (s,t)(s,t) falls into this area, the optimal strategy for the option holder is to exercise the option immediately. Hence, S∗​(t)S^{\*}(t) is also referred to as the optimal exercise boundary [[37](https://arxiv.org/html/2510.27132v1#bib.bib37)]. Conversely, in the continuation region, Eq. ([3a](https://arxiv.org/html/2510.27132v1#S2.E3.1 "In 3 ‣ 2.1.2 BSM Equations for American Options ‣ 2.1 BSM Equations for Option Pricing ‣ 2 Preliminaries ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations")) holds equal and V​(s,t)>(K−s)+V(s,t)>(K-s)^{+}.
In this region, the holder will choose to hold the option. S∗​(t)S^{\*}(t) represents the maximum price at which the holder will choose to exercise the option early, i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | S∗​(t)=sup{s∈ℝ+:V​(s,t)=(K−s)+}.S^{\*}(t)=\sup\{s\in\mathbb{R}^{+}:V(s,t)=(K-s)^{+}\}. |  | (4) |

For American call options, a free boundary is similarly defined. Unlike put options, the region above the boundary represents the stopping region, while the region below corresponds to the continuation region.

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒮={s≥S∗​(t),0≤t≤T}\displaystyle\mathcal{S}=\{s\geq S^{\*}(t),0\leq t\leq T\} | ={(s,t):V​(s,t)=(s−K)+},\displaystyle=\{(s,t):V(s,t)=(s-K)^{+}\}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒞={0≤s<S∗(t),0≤t≤T}\displaystyle\mathcal{C}=\{0\leq s<S^{\*}(t),0\leq t\leq T\} | ={(s,t):V​(s,t)>(s−K)+},\displaystyle=\{(s,t):V(s,t)>(s-K)^{+}\}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | S∗​(t)\displaystyle S^{\*}(t) | =inf{s∈ℝ+:V​(s,t)=(s−K)+}.\displaystyle=\inf\{s\in\mathbb{R}^{+}:V(s,t)=(s-K)^{+}\}. |  | (5) |

We plot the free boundary for both American put and call options in Figure [1](https://arxiv.org/html/2510.27132v1#S2.F1 "Figure 1 ‣ 2.1.3 Free Boundary Property in American Options ‣ 2.1 BSM Equations for Option Pricing ‣ 2 Preliminaries ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations"), using the solution obtained from the binomial tree method with
N=4000N=4000 as the reference solution. The free boundary S∗​(t)S^{\*}(t) is then calculated by Eq. ([4](https://arxiv.org/html/2510.27132v1#S2.E4 "In 2.1.3 Free Boundary Property in American Options ‣ 2.1 BSM Equations for Option Pricing ‣ 2 Preliminaries ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations")) and ([5](https://arxiv.org/html/2510.27132v1#S2.E5 "In 2.1.3 Free Boundary Property in American Options ‣ 2.1 BSM Equations for Option Pricing ‣ 2 Preliminaries ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations")).
The uncertainty of S∗​(t)S^{\*}(t) turns it into a free boundary problem, making the pricing of American options more complex than European options. Eq. ([3a](https://arxiv.org/html/2510.27132v1#S2.E3.1 "In 3 ‣ 2.1.2 BSM Equations for American Options ‣ 2.1 BSM Equations for Option Pricing ‣ 2 Preliminaries ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations")) - ([3d](https://arxiv.org/html/2510.27132v1#S2.E3.4 "In 3 ‣ 2.1.2 BSM Equations for American Options ‣ 2.1 BSM Equations for Option Pricing ‣ 2 Preliminaries ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations")) has no explicit analytical solutions and must therefore be solved by numerical methods.

![Refer to caption](Early_boundary_put.png)


(a)

![Refer to caption](Early_boundary_call.png)


(b)

Figure 1: Free boundary for American options obtained by binomial tree method. (a),(a), Free boundary for American put option with K=100,r=0.02,σ=0.25,T=1,q=0K=100,r=0.02,\sigma=0.25,T=1,q=0. (b),(b), Free boundary for American call option with K=200,r=0.05,σ=0.25,T=2,q=0.03K=200,r=0.05,\sigma=0.25,T=2,q=0.03.

#### 2.1.4 High-Dimensional BSM Equations for Multi-Asset Options

In addition to single-asset options, the BSM model can be extended to high-dimensional multi-asset models. This section focuses on the BSM framework for options on nn underlying assets. The price dynamics of these assets are described by the following nn-dimensional geometric Brownian motions in the risk-neutral form [[47](https://arxiv.org/html/2510.27132v1#bib.bib47)],

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Si​(t)=(r−qi)​Si​(t)​d​t+σi​Si​(t)​d​Wi,dS\_{i}(t)=(r-q\_{i})S\_{i}(t)dt+\sigma\_{i}S\_{i}(t)dW\_{i}, |  | (6) |

where rr is the risk-free rate, σi\sigma\_{i} is the volatility of the ii-th asset, and qiq\_{i} is the dividend yield. TT is the expiration date. {Wi}\{W\_{i}\} are nn standard Brownian motions with instantaneous coefficients of correlation denoted by ρi​j\rho\_{ij},

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Wi​d​Wj=ρi​j​d​t.dW\_{i}dW\_{j}=\rho\_{ij}dt. |  | (7) |

We consider an American option with a payoff function Φ=Φ​(S1​(t),⋯,Sn​(t))\Phi=\Phi(S\_{1}(t),\cdots,S\_{n}(t)).
Then the value of this American option of nn underlying assets V=V​(s1,⋯,sn,t)V=V(s\_{1},\cdots,s\_{n},t) satisfies the following BSM model [[43](https://arxiv.org/html/2510.27132v1#bib.bib43), [44](https://arxiv.org/html/2510.27132v1#bib.bib44)],

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ℱ​(V​(s1,⋯,sn,t))≤0,∀si≥0,t∈[0,T),\displaystyle\quad\mathcal{F}\big(V(s\_{1},\cdots,s\_{n},t)\big)\leq 0,\quad\forall s\_{i}\geq 0,t\in[0,T), |  |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | 𝒯​𝒱​(V​(s1,⋯,sn,t))≥0,∀si≥0,t∈[0,T),\displaystyle\quad\mathcal{TV}\big(V(s\_{1},\cdots,s\_{n},t)\big)\geq 0,\quad\forall s\_{i}\geq 0,t\in[0,T), |  |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ℱ​(V​(s1,⋯,sn,t))⋅𝒯​𝒱​(V​(s1,⋯,sn,t))=0,∀si≥0,t∈[0,T),\displaystyle\quad\mathcal{F}\big(V(s\_{1},\cdots,s\_{n},t)\big)\cdot\mathcal{TV}\big(V(s\_{1},\cdots,s\_{n},t)\big)=0,\quad\forall s\_{i}\geq 0,t\in[0,T), |  |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | V​(s1,⋯,sn,T)=Φ​(s1,⋯,sn),∀si≥0,\displaystyle\quad V(s\_{1},\cdots,s\_{n},T)=\Phi(s\_{1},\cdots,s\_{n}),\quad\forall s\_{i}\geq 0, |  |  |

where in the multi-asset cases, the operators are defined as follows,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℱ​(V​(s1,⋯,sn,t))\displaystyle\mathcal{F}(V(s\_{1},\cdots,s\_{n},t)) | =∂V∂t+12​∑i,j=1nσi​σj​ρi​j​si​sj​∂2V∂si​∂sj+∑i=1n(r−qi)​si​∂V∂si−r​V.\displaystyle=\frac{\partial V}{\partial t}+\frac{1}{2}\sum\limits\_{i,j=1}^{n}\sigma\_{i}\sigma\_{j}\rho\_{ij}s\_{i}s\_{j}\frac{\partial^{2}V}{\partial s\_{i}\partial s\_{j}}+\sum\limits\_{i=1}^{n}(r-q\_{i})s\_{i}\frac{\partial V}{\partial s\_{i}}-rV. |  | (8) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒯​𝒱​(V​(s1,⋯,sn,t))\displaystyle\mathcal{TV}\big(V(s\_{1},\cdots,s\_{n},t)\big) | =V​(s1,⋯,sn,t)−Φ​(s1,⋯,sn).\displaystyle=V(s\_{1},\cdots,s\_{n},t)-\Phi(s\_{1},\cdots,s\_{n}). |  |

In practice, there are various types of American multi-asset options with different payoff functions Φ​(s1,⋯,sn)\Phi(s\_{1},\cdots,s\_{n}). Common types of payoffs include options based on the maximum or minimum of several asset prices, spread options that consider the difference between two prices, and portfolio options that average prices. Contingent claims with these features are prevalent in financial exchanges, over-the-counter transactions, cash flows resulting from corporate investment decisions, and executive compensation plans [[11](https://arxiv.org/html/2510.27132v1#bib.bib11)]. Table [1](https://arxiv.org/html/2510.27132v1#S2.T1 "Table 1 ‣ 2.1.4 High-Dimensional BSM Equations for Multi-Asset Options ‣ 2.1 BSM Equations for Option Pricing ‣ 2 Preliminaries ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations") provides examples of some commonly used American multi-asset options.

Table 1: Different types of multi-asset options and their payoff functions

|  |  |  |  |
| --- | --- | --- | --- |
| Type of option | Φ​(s1,⋯,sn)\Phi(s\_{1},\cdots,s\_{n}) | Type of option | Φ​(s1,⋯,sn)\Phi(s\_{1},\cdots,s\_{n}) |
| Call-on-max [[15](https://arxiv.org/html/2510.27132v1#bib.bib15)] | [max{si}i=1n−K]+\big[\max\{s\_{i}\}\_{i=1}^{n}-K\big]^{+} | Call on geometric mean [[48](https://arxiv.org/html/2510.27132v1#bib.bib48)] | [(∏i=1nsi)1n−K]+\big[(\prod\limits\_{i=1}^{n}s\_{i})^{\frac{1}{n}}-K\big]^{+} |
| Call-on-min [[15](https://arxiv.org/html/2510.27132v1#bib.bib15)] | [min{si}i=1n−K]+\big[\min\{s\_{i}\}\_{i=1}^{n}-K\big]^{+} | Call on arithmetic mean [[46](https://arxiv.org/html/2510.27132v1#bib.bib46)] | [(1n​∑i=1nsi)−K]+\big[(\frac{1}{n}\sum\limits\_{i=1}^{n}s\_{i})-K\big]^{+} |
| Put-on-max [[14](https://arxiv.org/html/2510.27132v1#bib.bib14)] | [K−max{si}i=1n]+\big[K-\max\{s\_{i}\}\_{i=1}^{n}\big]^{+} | Put on geometric mean [[47](https://arxiv.org/html/2510.27132v1#bib.bib47)] | [K−(∏i=1nsi)1n]+\big[K-(\prod\limits\_{i=1}^{n}s\_{i})^{\frac{1}{n}}\big]^{+} |
| Put-on-min [[13](https://arxiv.org/html/2510.27132v1#bib.bib13)] | [K−min{si}i=1n]+\big[K-\min\{s\_{i}\}\_{i=1}^{n}\big]^{+} | Put on arithmetic mean [[45](https://arxiv.org/html/2510.27132v1#bib.bib45)] | [K−(1n​∑i=1nsi)]+\big[K-(\frac{1}{n}\sum\limits\_{i=1}^{n}s\_{i})\big]^{+} |

### 2.2 Physics-Informed Neural Networks

This section introduces the concept of Physics-Informed Neural Networks (PINN) [[1](https://arxiv.org/html/2510.27132v1#bib.bib1)] and discusses their modification for PDEs subject to inequality constraints, as encountered in the pricing of American options.

#### 2.2.1 General Framework

In the context of PINN, partial differential equations in the following form are usually considered

|  |  |  |
| --- | --- | --- |
|  | 𝒢​(u)=ut+𝒩​(u)=0,∀x∈𝒟,t∈[0,T),\mathcal{G}(u)=u\_{t}+\mathcal{N}(u)=0,\quad\forall x\in\mathcal{D},t\in[0,T), |  |

subject to the initial and boundary conditions

|  |  |  |
| --- | --- | --- |
|  | {u​(x,0)=g​(x),∀x∈𝒟,ℬ​(u)=0,∀x∈∂𝒟,t∈[0,T],\left\{\begin{aligned} &\quad u(x,0)=g(x),\quad\forall x\in\mathcal{D},\\ &\quad\mathcal{B}(u)=0,\quad\forall x\in\partial\mathcal{D},t\in[0,T],\end{aligned}\right. |  |

where 𝒩​[⋅]\mathcal{N}[\cdot] is a differential operator, ℬ​[⋅]\mathcal{B}[\cdot] is a boundary operator representing Dirichlet, Neumann, Robin, or periodic boundary conditions, and 𝒟\mathcal{D} is a subset of ℝd\mathbb{R}^{d}. The purpose is to approximate the unknown solution u​(x,t)u(x,t) by a deep neural network uθ​(x,t)u\_{\theta}(x,t), referred to as PINN, where θ\theta is the parameter of the network. The model can be trained by minimizing the following composite loss function,

|  |  |  |
| --- | --- | --- |
|  | ℒ​(θ)=λf​ℒf​(θ)+λi​c​ℒi​c​(θ)+λb​c​ℒb​c​(θ).\mathcal{L}(\theta)=\lambda\_{f}\mathcal{L}\_{f}(\theta)+\lambda\_{ic}\mathcal{L}\_{ic}(\theta)+\lambda\_{bc}\mathcal{L}\_{bc}(\theta). |  |

Each term is specifically defined as follows,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒf​(θ)\displaystyle\mathcal{L}\_{f}(\theta) | =1Nf​∑i=1Nf|𝒢​(uθ​(xfi,tfi))|2,\displaystyle=\frac{1}{N\_{f}}\sum\limits\_{i=1}^{N\_{f}}|\mathcal{G}(u\_{\theta}(x\_{f}^{i},t\_{f}^{i}))|^{2}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℒi​c​(θ)\displaystyle\mathcal{L}\_{ic}(\theta) | =1Ni​c​∑i=1Ni​c|uθ​(xi​ci,0)−g​(xi​ci)|2,\displaystyle=\frac{1}{N\_{ic}}\sum\limits\_{i=1}^{N\_{ic}}|u\_{\theta}(x\_{ic}^{i},0)-g(x\_{ic}^{i})|^{2}, |  | (9) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒb​c​(θ)\displaystyle\mathcal{L}\_{bc}(\theta) | =1Nb​c​∑i=1Nb​c|ℬ​(uθ​(xb​ci,tb​ci))|2.\displaystyle=\frac{1}{N\_{bc}}\sum\limits\_{i=1}^{N\_{bc}}|\mathcal{B}(u\_{\theta}(x\_{bc}^{i},t\_{bc}^{i}))|^{2}. |  |

Here {xfi,tfi}i=1Nf\{x\_{f}^{i},t\_{f}^{i}\}\_{i=1}^{N\_{f}} denotes the collocations points for 𝒢​(u)\mathcal{G}(u). {xi​ci,0}i=1Ni​c\{x\_{ic}^{i},0\}\_{i=1}^{N\_{ic}} and {xb​ci,tb​ci}i=1Nb​c\{x\_{bc}^{i},t\_{bc}^{i}\}\_{i=1}^{N\_{bc}} are collocations points for initial and boundary conditions. {λf,λi​c,λb​c}\{\lambda\_{f},\lambda\_{ic},\lambda\_{bc}\} are hyperparameters that assign weights to different loss terms.

#### 2.2.2 Loss Design for PDEs with Inequalities

BSM equations for European options only contain equality constraints, such as Eq. ([1](https://arxiv.org/html/2510.27132v1#S2.E1 "In 2.1.1 BSM Equations for European Options ‣ 2.1 BSM Equations for Option Pricing ‣ 2 Preliminaries ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations")). Therefore, the loss function adopts a structure similar to that of PINN,

|  |  |  |
| --- | --- | --- |
|  | ℒ​(θ)=λf​ℒf​(θ)+λt​c​ℒt​c​(θ).\mathcal{L}(\theta)=\lambda\_{f}\mathcal{L}\_{f}(\theta)+\lambda\_{tc}\mathcal{L}\_{tc}(\theta). |  |

Here ℒt​c\mathcal{L}\_{tc} represents the terminal condition term, which is similar to Eq. ([9](https://arxiv.org/html/2510.27132v1#S2.E9 "In 2.2.1 General Framework ‣ 2.2 Physics-Informed Neural Networks ‣ 2 Preliminaries ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations")),

|  |  |  |
| --- | --- | --- |
|  | ℒt​c​(θ)=1Nt​c​∑i=1Nt​c|(uθ​(xt​ci,T)−Φ​(xt​ci))|2.\mathcal{L}\_{tc}(\theta)=\frac{1}{N\_{tc}}\sum\limits\_{i=1}^{N\_{tc}}\Big|(u\_{\theta}(x\_{tc}^{i},T)-\Phi(x\_{tc}^{i}))\Big|^{2}. |  |

To address the challenges posed by inequalities in the system of Eq. ([3a](https://arxiv.org/html/2510.27132v1#S2.E3.1 "In 3 ‣ 2.1.2 BSM Equations for American Options ‣ 2.1 BSM Equations for Option Pricing ‣ 2 Preliminaries ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations"))-([3d](https://arxiv.org/html/2510.27132v1#S2.E3.4 "In 3 ‣ 2.1.2 BSM Equations for American Options ‣ 2.1 BSM Equations for Option Pricing ‣ 2 Preliminaries ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations")) for American options, we modify the loss function as follows,

|  |  |  |
| --- | --- | --- |
|  | ℒ​(θ)=λb​s​ℒb​s​(θ)+λt​v​ℒt​v​(θ)+λe​q​ℒe​q​(θ)+λt​c​ℒt​c​(θ),\mathcal{L}(\theta)=\lambda\_{bs}\mathcal{L}\_{bs}(\theta)+\lambda\_{tv}\mathcal{L}\_{tv}(\theta)+\lambda\_{eq}\mathcal{L}\_{eq}(\theta)+\lambda\_{tc}\mathcal{L}\_{tc}(\theta), |  |

where {λb​s,λt​v,λe​q,λt​c}\{\lambda\_{bs},\lambda\_{tv},\lambda\_{eq},\lambda\_{tc}\} are hyperparameters that assign weights to different loss terms. The first term ℒb​s\mathcal{L}\_{bs} is defined as

|  |  |  |
| --- | --- | --- |
|  | ℒb​s​(θ)=1Nb​s​∑i=1Nb​s|max⁡(ℱ​(uθ​(sb​si,tb​si)),0)|2.\mathcal{L}\_{bs}(\theta)=\frac{1}{N\_{bs}}\sum\limits\_{i=1}^{N\_{bs}}\Big|\max\Big(\mathcal{F}\big(u\_{\theta}(s\_{bs}^{i},t\_{bs}^{i})\big),0\Big)\Big|^{2}. |  |

where ℱ​(V​(s,t))\mathcal{F}(V(s,t)) is defined in Eq. ([2](https://arxiv.org/html/2510.27132v1#S2.E2 "In 2.1.2 BSM Equations for American Options ‣ 2.1 BSM Equations for Option Pricing ‣ 2 Preliminaries ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations")) for single-asset options and Eq. ([8](https://arxiv.org/html/2510.27132v1#S2.E8 "In 2.1.4 High-Dimensional BSM Equations for Multi-Asset Options ‣ 2.1 BSM Equations for Option Pricing ‣ 2 Preliminaries ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations")) for multi-asset options. sb​sis\_{bs}^{i} is the vector of underlying asset prices at the ii-th collocation point. Since the linear complementarity conditions require ℱ​(V)≤0\mathcal{F}(V)\leq 0, the term ℒb​s\mathcal{L}\_{bs} serves as a penalty to enforce this constraint. Specifically, ℒb​s\mathcal{L}\_{bs} imposes a penalty whenever the predicted value uθu\_{\theta} results in ℱ​(uθ)>0\mathcal{F}(u\_{\theta})>0. When ℱ​(uθ)≤0\mathcal{F}(u\_{\theta})\leq 0, this term degenerate to 0.

The time value of American options should be nonnegative. Consequently, the loss term associated with this constraint is defined as follows,

|  |  |  |
| --- | --- | --- |
|  | ℒt​v​(θ)=1Nt​v​∑i=1Nt​v|−min⁡(𝒯​𝒱​(uθ​(st​vi,tt​vi)),0)|2.\mathcal{L}\_{tv}(\theta)=\frac{1}{N\_{tv}}\sum\limits\_{i=1}^{N\_{tv}}\Big|-\min\Big(\mathcal{TV}\big(u\_{\theta}(s\_{tv}^{i},t\_{tv}^{i})\big),0\Big)\Big|^{2}. |  |

Similar to ℒb​s\mathcal{L}\_{bs}, this term acts as a penalty term to enforce the non-negativity of the time value, ensuring it remains greater than or equal to zero. This term degenerates to 0 when this inequality is satisfied.
To account for the equality in the linear complementarity conditions, we introduce a third term in the loss function defined,

|  |  |  |
| --- | --- | --- |
|  | ℒe​q​(θ)=1Ne​q​∑i=1Ne​q|ℱ​(uθ​(se​qi,te​qi))⋅𝒯​𝒱​(uθ​(se​qi,te​qi))|2.\mathcal{L}\_{eq}(\theta)=\frac{1}{N\_{eq}}\sum\limits\_{i=1}^{N\_{eq}}\Big|\mathcal{F}\big(u\_{\theta}(s\_{eq}^{i},t\_{eq}^{i})\big)\cdot\mathcal{TV}\big(u\_{\theta}(s\_{eq}^{i},t\_{eq}^{i})\big)\Big|^{2}. |  |

This loss term is designed to ensure that at least one of the inequalities is satisfied as an equality.
By weighting and summing these four terms, the loss function for solving the system of inequality equations is obtained.

## 3 Methodology and Formulation

In this section, we present the methodological framework of the proposed Exact Terminal Condition Neural Network (ETCNN). Section [3.1](https://arxiv.org/html/2510.27132v1#S3.SS1 "3.1 Imposing Exact Terminal Conditions ‣ 3 Methodology and Formulation ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations") introduces the core idea of the ETCNN approach, followed by a description of the network architecture in Section [3.2](https://arxiv.org/html/2510.27132v1#S3.SS2 "3.2 Neural Network Structure ‣ 3 Methodology and Formulation ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations") and the input normalization strategy in Section [3.3](https://arxiv.org/html/2510.27132v1#S3.SS3 "3.3 Input Normalization ‣ 3 Methodology and Formulation ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations"). Section [3.4](https://arxiv.org/html/2510.27132v1#S3.SS4 "3.4 Illustrative Example: European Option ‣ 3 Methodology and Formulation ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations") applies the proposed framework to a European option, serving as a toy model to illustrate the fundamental mechanism of the method. Finally, Section [3.5](https://arxiv.org/html/2510.27132v1#S3.SS5 "3.5 Methodological Formulation for American Options ‣ 3 Methodology and Formulation ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations") extends the formulation to American options, laying the foundation for the numerical experiments presented in Section 4.

### 3.1 Imposing Exact Terminal Conditions

As we will show in Figure [6](https://arxiv.org/html/2510.27132v1#S4.F6 "Figure 6 ‣ 4.1.2 Numerical Results ‣ 4.1 Single-Asset American Put Options ‣ 4 Numerical Results for American Options ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations"), the standard PINN method suffers from low solution accuracy, partly due to the non-differentiability of terminal conditions at specific points and the near-singular behavior close to the terminal. To address these limitations, we propose the ETCNN in this section.

The core idea of imposing the exact terminal conditions method is to choose a trial function that automatically satisfies the terminal condition to approximate the solution. The idea of embedding exact boundary conditions into neural network trial functions has been considered in prior studies [[2](https://arxiv.org/html/2510.27132v1#bib.bib2), [24](https://arxiv.org/html/2510.27132v1#bib.bib24)], and we build upon this line of work by introducing a tailored design for the BSM equations. Consider a system of differential equations formulated as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | {𝒢​(V​(s,t))=0,∀s∈𝒟,t∈[0,T),V​(s,T)=Φ​(s),∀s∈𝒟.\left\{\begin{aligned} \quad&\mathcal{G}(V(s,t))=0,\quad\forall s\in\mathcal{D},t\in[0,T),\\ \quad&V(s,T)=\Phi(s),\quad\forall s\in\mathcal{D}.\end{aligned}\right. |  | (10) |

where tt is the current time, ss is a scaler or a vector defined on a region 𝒟\mathcal{D}. The equality sign in the first line is not necessarily required and can be an inequality, similar to the BSM equation for American options. This equation is subject to some terminal condition function Φ​(s)\Phi(s).

The trial solution is chosen as

|  |  |  |
| --- | --- | --- |
|  | u~N​N​(s,t)=g1​(s,t)​uN​N​(s,t)+g2​(s,t).\tilde{u}\_{NN}(s,t)=g\_{1}(s,t)u\_{NN}(s,t)+g\_{2}(s,t). |  |

where g1,g2g\_{1},g\_{2} are constructed to satisfy specific constraints,

|  |  |  |
| --- | --- | --- |
|  | g1​(s,T)=0,g2​(s,T)=Φ​(s),∀s∈𝒟.g\_{1}(s,T)=0,\quad g\_{2}(s,T)=\Phi(s),\quad\forall s\in\mathcal{D}. |  |

By this construction, the overall trial solution u~N​N\tilde{u}\_{NN} inherently satisfies the terminal conditions.

The main advantage of this approach is that the resulting solution exactly satisfies the boundary conditions, thereby eliminating the errors in boundary condition enforcement that are typical of conventional PINNs and consequently improving solution accuracy. Another advantage is that our designed g2g\_{2} is constructed to preserve key properties of the true solution.
In addition to satisfying the terminal conditions, it is desirable for g2g\_{2} to ensure that the trial solution captures key properties of the true solution, such as smoothness and singular behaviors. True solutions are often non-differentiable at some points on the terminal but are smooth anywhere else. They also exhibit near-singularity near the terminal. Therefore, it is generally inappropriate to simply set g2​(s,t)=Φ​(s)g\_{2}(s,t)=\Phi(s), as this function neither preserves the differentiability nor captures the singularities present in the true solution. As demonstrated in
Section [4.1](https://arxiv.org/html/2510.27132v1#S4.SS1 "4.1 Single-Asset American Put Options ‣ 4 Numerical Results for American Options ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations"), poor choice of g2g\_{2} may even reduce the accuracy of the network. In the subsequent sections, we will discuss how to appropriately select g2g\_{2} for the BSM equations for both European and American options.

### 3.2 Neural Network Structure

In the context of applying deep learning to solve partial differential equation
problems, residual networks (ResNet) are commonly used for function approximation. Deep residual learning, introduced by He et al. [[41](https://arxiv.org/html/2510.27132v1#bib.bib41)], is a neural network architecture based on the concept of residual blocks. Each residual block consists of several fully connected layers, where the final output is computed by adding the input of the block to the output of its last layer.
In this section, we provide an overview of the ResNet structure and explain how it is adapted to satisfy accurate terminal conditions.

Consider a ResNet containing MM residual blocks, each consisting of LL layers with nn neurons per layer.
When solving Eq. ([10](https://arxiv.org/html/2510.27132v1#S3.E10 "In 3.1 Imposing Exact Terminal Conditions ‣ 3 Methodology and Formulation ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations")), suppose the input vector x=(s,t)x=(s,t) has a dimension di​nd\_{in}. The network begins with a fully connected layer, transforming the input into an nn-dimensional vector,

|  |  |  |
| --- | --- | --- |
|  | g(1,0)​(x)=σ​(Wi​n⋅x+bi​n),g^{(1,0)}(x)=\sigma(W^{in}\cdot x+b^{in}), |  |

where Wi​n∈ℝn×di​nW^{in}\in\mathbb{R}^{n\times d\_{in}} is a weight matrix, bi​n∈ℝnb^{in}\in\mathbb{R}^{n} is a bias vector and σ\sigma is the activation function. We use the tanh\tanh function in this work. Let g(m,0)​(x)g^{(m,0)}(x) be the input of the mm-th block, the structure of the mm-th block is defined as follows,

|  |  |  |
| --- | --- | --- |
|  | fθ(m,l)​(x)=W(m,l)⋅g(m,l−1)​(x)+b(m,l),g(m,l)​(x)=σ​(fθ(m,l)​(x)),1≤l≤L,1≤m≤M.f\_{\theta}^{(m,l)}(x)=W^{(m,l)}\cdot g^{(m,l-1)}(x)+b^{(m,l)},\quad g^{(m,l)}(x)=\sigma(f\_{\theta}^{(m,l)}(x)),\quad 1\leq l\leq L,1\leq m\leq M. |  |

Here, W(m,l)∈ℝn×nW^{(m,l)}\in\mathbb{R}^{n\times n} is the weight matrix in the ll-th layer. b(m,l)∈ℝnb^{(m,l)}\in\mathbb{R}^{n} is the bias vector. The final output of the mm-th block, which is the input of the next part, is

|  |  |  |
| --- | --- | --- |
|  | g(m+1,0)​(x)=fθ(m,L)​(x)+g(m,0)​(x),1≤m≤Mg^{(m+1,0)}(x)=f\_{\theta}^{(m,L)}(x)+g^{(m,0)}(x),\quad 1\leq m\leq M |  |

Finally, the output of the network is

|  |  |  |  |
| --- | --- | --- | --- |
|  | fθ​(x)=Wo​u​t⋅g(M+1,0)​(x)+bo​u​t.f\_{\theta}(x)=W^{out}\cdot g^{(M+1,0)}(x)+b^{out}. |  | (11) |

Here, Wo​u​t∈ℝdo​u​t×n,bo​u​t∈ℝdo​u​tW^{out}\in\mathbb{R}^{d\_{out}\times n},b^{out}\in\mathbb{R}^{d\_{out}}, where do​u​td\_{out} is the dimension of solution. Figure [2](https://arxiv.org/html/2510.27132v1#S3.F2 "Figure 2 ‣ 3.2 Neural Network Structure ‣ 3 Methodology and Formulation ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations") illustrates the structure of a ResNet with parameters M=2,L=3,n=5,di​n=4M=2,L=3,n=5,d\_{in}=4 and do​u​t=1d\_{out}=1.

![Refer to caption](ResNet.png)
  


Figure 2: Structure of a ResNet with M=2,L=3,n=5,di​n=4,do​u​t=1M=2,L=3,n=5,d\_{in}=4,d\_{out}=1.

In the exact terminal method, the output layer of the network is modified to ensure that the terminal conditions are satisfied, in a manner similar in [[49](https://arxiv.org/html/2510.27132v1#bib.bib49)].
The network architecture in front of the output layer remains unchanged, only the last layer is modified.
For ResNet, Eq. ([11](https://arxiv.org/html/2510.27132v1#S3.E11 "In 3.2 Neural Network Structure ‣ 3 Methodology and Formulation ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations")) is modified as

|  |  |  |
| --- | --- | --- |
|  | fθ​(x)=g1​(x)⋅(Wo​u​t⋅g(M+1,0)​(x)+bo​u​t)+g2​(x).f\_{\theta}(x)=g\_{1}(x)\cdot(W^{out}\cdot g^{(M+1,0)}(x)+b^{out})+g\_{2}(x). |  |

Here, g1g\_{1} and g2g\_{2} are functions that need to be assigned before training which satisfy the following conditions,

|  |  |  |
| --- | --- | --- |
|  | g1​(x)=0,g2​(x)=Φ​(s),∀x=(s,T)∈𝒟×{T}.g\_{1}(x)=0,\quad g\_{2}(x)=\Phi(s),\quad\forall x=(s,T)\in\mathcal{D}\times\{T\}. |  |

Figure [3](https://arxiv.org/html/2510.27132v1#S3.F3 "Figure 3 ‣ 3.2 Neural Network Structure ‣ 3 Methodology and Formulation ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations") shows the structure of our ETCNN.

![Refer to caption](ETCNN0.png)
  


Figure 3: Structure of our exact terminal method.

### 3.3 Input Normalization

We further investigate normalizing the input variables by transforming the asset price ss into its moneyness, defined as the ratio s/Ks/K. This normalization ensures that the input variables are of similar orders of magnitude, as the time variable tt is typically of order 𝒪​(1)\mathcal{O}(1) since the term of an option is usually a few months or years.
A more significant reason to do such normalization lies in the homogeneity property of the option pricing function VV with respect to ss. When the option pricing formula VV is expressed as a function of asset price, strike price and time, it exhibits a homogeneous property [[33](https://arxiv.org/html/2510.27132v1#bib.bib33)],

|  |  |  |
| --- | --- | --- |
|  | α⋅V​(s,K,t)=V​(α​s,α​K,t)\alpha\cdot V(s,K,t)=V(\alpha s,\alpha K,t) |  |

This property can be easily derived from the characteristics of geometric Brownian motion. For the options under our consideration, a fixed strike price KK is predetermined. Consequently, the solution depends on the ratio s/Ks/K.

The input normalization structure introduced in this section is designed to maintain this property for the neural network solution. When the input vector (s,t)(s,t) enters the network, the asset price vector ss is first normalized by dividing each of its dimensions by KK, while the temporal component tt remains unchanged. The normalized input (s/K,t)(s/K,t) is then passed into the network. In this way, the output of the network will be a function of s/Ks/K. Figure [4](https://arxiv.org/html/2510.27132v1#S3.F4 "Figure 4 ‣ 3.3 Input Normalization ‣ 3 Methodology and Formulation ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations") shows the overall structure of our ECTNN with an input normalization layer.

![Refer to caption](ETCNN.png)
  


Figure 4: Structure of our exact terminal method with input normalization.

### 3.4 Illustrative Example: European Option

This example serves as a toy model for solving a basic BSM equation for pricing single-asset European options, which are the simplest type of option. We use this experiment to demonstrate the effectiveness of our ETCNN, to assess which network structures are most suitable, and to explore the criteria necessary for selecting exact terminal functions. These criteria will later be applied to provide exact terminal functions for American options, which are the primary focus of this article. Meanwhile, the analytical solution for European options will serve as the foundation for determining exact terminal functions for American options in the next subsections.

Single-asset European call options satisfy the following BSM equation,

|  |  |  |
| --- | --- | --- |
|  | {ℱ​(V)=∂V∂t+12​σ2​s2​∂2V∂s2+r​s​∂V∂s−r​V=0,∀s≥0,t∈[0,T),V​(s,T)=(s−K)+,∀s≥0.\left\{\begin{aligned} \quad&\mathcal{F}(V)=\frac{\partial V}{\partial t}+\frac{1}{2}\sigma^{2}s^{2}\frac{\partial^{2}V}{\partial s^{2}}+rs\frac{\partial V}{\partial s}-rV=0,\quad\forall s\geq 0,t\in[0,T),\\ \quad&V(s,T)=(s-K)^{+},\quad\forall s\geq 0.\end{aligned}\right. |  |

This equation has an explicit solution,

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(s,t)=s⋅N​(d1​(s,τ,K))−K​e−r​τ⋅N​(d2​(s,τ,K)),V(s,t)=s\cdot N\big(d\_{1}(s,\tau,K)\big)-Ke^{-r\tau}\cdot N\big(d\_{2}(s,\tau,K)\big), |  | (12) |

where τ=T−t\tau=T-t is the time to maturity. N​(⋅)N(\cdot) is the cumulative distribution function of the standard normal distribution. d1,d2d\_{1},d\_{2} are defined as follows,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d1​(s,τ,K)=1σ​τ​(ln⁡sK+(r+σ22)​τ),d2​(s,τ,K)=d1​(s,τ,K)−σ​τ=1σ​τ​(ln⁡sK+(r−σ22)​τ).d\_{1}(s,\tau,K)=\frac{1}{\sigma\sqrt{\tau}}\big(\ln{\frac{s}{K}}+(r+\frac{\sigma^{2}}{2})\tau\big),\quad d\_{2}(s,\tau,K)=d\_{1}(s,\tau,K)-\sigma\sqrt{\tau}=\frac{1}{\sigma\sqrt{\tau}}\big(\ln{\frac{s}{K}}+(r-\frac{\sigma^{2}}{2})\tau\big). |  | (13) |

When τ=0\tau=0, we define

|  |  |  |
| --- | --- | --- |
|  | N​(d1​(s,0,K))=N​(limτ→0d1​(s,τ,K))={1,if​s>K,12,if​s=K,0,if​s<K.N\big(d\_{1}(s,0,K)\big)=N\big(\lim\limits\_{\tau\to 0}d\_{1}(s,\tau,K)\big)=\begin{cases}1,&\text{if}\ s>K,\\ \frac{1}{2},&\text{if}\ s=K,\\ 0,&\text{if}\ s<K.\end{cases} |  |

We take K=100,r=0.05,σ=0.15,T=1K=100,r=0.05,\sigma=0.15,T=1 in this experiment. The strike price of options traded on exchanges usually does not deviate too much from the underlying assets’ prices. In this case, the network is trained on [50,150]×[0,T][50,150]\times[0,T] and evaluated on [80,120]×[0,T][80,120]\times[0,T], which covers the vast majority of situations in actual transactions. The training domain is set slightly wider than the testing domain to ensure reliable accuracy within the region of practical interest.

The terminal condition in this case is

|  |  |  |
| --- | --- | --- |
|  | Φ​(s)=(s−K)+=12​(s−K+s2+K2−2​s​K).\Phi(s)=(s-K)^{+}=\frac{1}{2}(s-K+\sqrt{s^{2}+K^{2}-2sK}). |  |

To construct an appropriate g2g\_{2}, we slightly modify Φ​(s)\Phi(s) by introducing the time variable tt and
obtain a function on (s,t)(s,t) that both satisfies the terminal conditions at t=Tt=T and is a differentiable function when t<Tt<T. A common technique in the analysis of European options at time tt is to discount strike price KK at a discount rate rr to time tt. Inspired by this, we naturally extend the idea of discounting KK and define

|  |  |  |
| --- | --- | --- |
|  | g1​(s,t)=T−t,g2​(s,t)=12​(s−K+s2+K2−2​s​K​e−r​(T−t)).g\_{1}(s,t)=T-t,\quad g\_{2}(s,t)=\frac{1}{2}(s-K+\sqrt{s^{2}+K^{2}-2sKe^{-r(T-t)}}). |  |

With this construction, the solution u~N​N=g1⋅uN​N+g2\tilde{u}\_{NN}=g\_{1}\cdot u\_{NN}+g\_{2} accurately satisfies the terminal condition u~N​N​(s,T)=(s−K)+\tilde{u}\_{NN}(s,T)=(s-K)^{+}. Furthermore, u~N​N\tilde{u}\_{NN} retains non-differentiability at the point (K,T)(K,T) while remaining smooth elsewhere. This design ensures that u~N​N\tilde{u}\_{NN} matches the differentiability properties of the true solution.

In this case, and throughout all experiments in Section [4](https://arxiv.org/html/2510.27132v1#S4 "4 Numerical Results for American Options ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations"), the Adam [[3](https://arxiv.org/html/2510.27132v1#bib.bib3)] optimization algorithm is employed to obtain the network parameters θ\theta. The hyperparameter β\beta in Adam denotes the pair of exponential decay rates (β1,β2)(\beta\_{1},\beta\_{2}) for the first- and second-moment estimates. In our implementation, we adopt the standard setting (β1,β2)=(0.9,0.999)(\beta\_{1},\beta\_{2})=(0.9,0.999). The learning rate l​rlr starts at an initial value l​rs​t​a​r​tlr\_{start} and decays exponentially with a decay factor γ\gamma. To be specific, each of our experiments involves 200,000 training iterations. During the first 40,000 iterations, the learning rate decays by a factor of γ\gamma every 2,000 iterations. In the remaining 160,000 iterations, the decay occurs every 5,000 iterations. This two-stage schedule was empirically designed: the initial frequent decays help the network quickly reach a reasonable solution, while the subsequent slower decay pace allows for more precise convergence in the later stages of optimization.
Both l​rs​t​a​r​tlr\_{start} and γ\gamma are hyperparameters tuned for each experiment. Details of the hyperparameters {λ}\{\lambda\}, l​rs​t​a​r​tlr\_{start} and γ\gamma
will be provided in the context of individual experiments.

For the toy model under consideration, the parameters are set as λf=20,λt​c=1\lambda\_{f}=20,\lambda\_{tc}=1. For loss computation, Nt​c=1024N\_{tc}=1024 points are sampled to calculate ℒt​c\mathcal{L}\_{tc}, and Nf=4​Nt​cN\_{f}=4N\_{tc} to calculate ℒf\mathcal{L}\_{f}. Notably, ETCNN eliminates the need for tuning λt​c\lambda\_{tc}. For consistency, ETCNN uses the same value of λf\lambda\_{f} and NfN\_{f}. The learning rate is initialized at l​rs​t​a​r​t=0.01lr\_{start}=0.01, with a decay factor of γ=0.85\gamma=0.85.
To evaluate the effectiveness of ETCNN and the impact of input normalization, we employ ResNet architectures with four and five blocks, where each block consists of two layers, and each layer contains 50 neurons. Both configurations are tested with and without the input normalization layer. The performance is assessed by the L2L^{2} relative errors between the computed solutions and the exact solution. Each experiment is repeated three times, and the average results are reported. The outcomes are summarized in Table [2](https://arxiv.org/html/2510.27132v1#S3.T2 "Table 2 ‣ 3.4 Illustrative Example: European Option ‣ 3 Methodology and Formulation ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations").

The results demonstrate that applying exact terminal conditions significantly enhances accuracy, improving it by approximately one order of magnitude. Furthermore, combining normalization with exact terminal conditions yields the best results. The performance of the 5-block network is comparable to that of the 4-block network. However, the 4-block network requires fewer parameters. This suggests that a 4-block network may represent an optimal choice for the number of blocks. Based on these findings, we adopt a 4-block ResNet for subsequent numerical experiments.

Table 2: Relative L2L^{2} error on PINN and ETCNN. Norm refers to the input normalization. Bold font represents the best result in each row.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ResNet | PINN | PINN+Norm | ETCNN | ETCNN+Norm |
| 4-block | 2.13×10−32.13\times 10^{-3} | 1.65×10−31.65\times 10^{-3} | 4.63×10−44.63\times 10^{-4} | 2.94×10-4\textbf{2.94}\times\textbf{10}^{\textbf{-4}} |
| 5-block | 2.33×10−32.33\times 10^{-3} | 1.68×10−31.68\times 10^{-3} | 4.37×10−44.37\times 10^{-4} | 3.83×10-4\textbf{3.83}\times\textbf{10}^{\textbf{-4}} |

### 3.5 Methodological Formulation for American Options

The American BSM equation is more complex to solve due to inequality constraints. In order to improve the accuracy of the solution, it is necessary to carefully select g2g\_{2}. We propose the exact terminal conditions methods based on our understanding of the financial properties of options, and by borrowing knowledge from European options. It is natural to view the price of American options as the sum of the price of an equivalent European option and an early exercise premium.
Several papers have provided a theoretical basis for this [[38](https://arxiv.org/html/2510.27132v1#bib.bib38), [39](https://arxiv.org/html/2510.27132v1#bib.bib39), [40](https://arxiv.org/html/2510.27132v1#bib.bib40)].

|  |  |  |
| --- | --- | --- |
|  | Va​(s,t)=Ve​(s,t)+p​(s,t),V^{a}(s,t)=V^{e}(s,t)+p(s,t), |  |

where s∈ℝns\in\mathbb{R}^{n} is the price of nn underlying assets. Va​(s,t)V^{a}(s,t) represents the price of the American option. Ve​(s,t)V^{e}(s,t) is the value of its corresponding European option, which shares the same parameters as the American option but can only be exercised at the expiration date. p​(s,t)p(s,t) is the early exercise premium.

Klimsiak and Rozkosz [[22](https://arxiv.org/html/2510.27132v1#bib.bib22)] provided an implicit integral representation for
the premium p​(s,t)p(s,t) under specific assumptions.
If the terminal payoff Φ\Phi is a nonnegative continuous function and is smooth on {Va​(s,t)=Φ​(s)}∩ℝn×[0,t]\{V^{a}(s,t)=\Phi(s)\}\cap\mathbb{R}^{n}\times[0,t] for every t∈(0,T)t\in(0,T), or Φ\Phi is a nonnegative convex function, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(s,t)=𝐄t,s​[∫tTe−r​(u−t)​I​{Va​(s​(u),u)=Φ​(s​(u))}​H​(s​(u),u)​𝑑u],p(s,t)=\mathbf{E}\_{t,s}\left[\int\_{t}^{T}e^{-r(u-t)}\textit{I}\{V^{a}(s(u),u)=\Phi(s(u))\}H(s(u),u)du\right], |  | (14) |

where 𝐄t,s\mathbf{E}\_{t,s} is the expectation under risk-neutral measure and I​(⋅)\textit{I}(\cdot) is the indicator function. H​(s,t)=−ℱ​(Φ​(s​(u),u))H(s,t)=-\mathcal{F}(\Phi(s(u),u)) where ℱ\mathcal{F} is the PDE operator defined in Eq. ([8](https://arxiv.org/html/2510.27132v1#S2.E8 "In 2.1.4 High-Dimensional BSM Equations for Multi-Asset Options ‣ 2.1 BSM Equations for Option Pricing ‣ 2 Preliminaries ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations")). The region {Va​(S​(u),u)=Φ​(S​(u))}\{V^{a}(S(u),u)=\Phi(S(u))\} corresponds to the stopping region and is unknown since the free boundary S∗​(t)S^{\*}(t) is unknown.

Note that Ve​(s,t)V^{e}(s,t) inherently satisfies the terminal condition, as the corresponding European option shares the same terminal condition. This observation naturally leads to the idea of extracting information from Ve​(s,t)V^{e}(s,t) to construct g2​(s,t)g\_{2}(s,t).
Furthermore, p​(s,t)p(s,t) involves an integral over time. If p​(s,t)p(s,t) does not include singular integrals or contains nearly singular terms with minimal impact after integration, then the singularities in Va​(s,t)V^{a}(s,t) primarily originate from Ve​(s,t)V^{e}(s,t). Consequently, we design a function g2​(s,t)g\_{2}(s,t) that approximates Ve​(s,t)V^{e}(s,t), such that g2g\_{2} satisfies exact boundary conditions while also incorporating the singularity in VeV^{e}. This way, the remaining residue Va−g2V^{a}-g\_{2} becomes smooth, making it easier for the neural network to learn.
The subsequent section provides detailed examples and the explicit construction of g2g\_{2}.

## 4 Numerical Results for American Options

To illustrate the broad applicability of our method, we consider four distinct examples in this section, each with different settings and parameters. Section [4.1](https://arxiv.org/html/2510.27132v1#S4.SS1 "4.1 Single-Asset American Put Options ‣ 4 Numerical Results for American Options ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations") presents a single-asset American put option, while Section [4.2](https://arxiv.org/html/2510.27132v1#S4.SS2 "4.2 American Call Options with Dividends ‣ 4 Numerical Results for American Options ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations") studies single-asset American call options with dividends, including variations in volatility and dividend rates. We provide comparisons with traditional numerical methods for these two examples. Section [4.3](https://arxiv.org/html/2510.27132v1#S4.SS3 "4.3 Multi-Asset Options with Geometric Average Payoffs ‣ 4 Numerical Results for American Options ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations") examines multi-asset options with a geometric-average payoff, considering different numbers of underlying assets, and Section [4.4](https://arxiv.org/html/2510.27132v1#S4.SS4 "4.4 Call-on-Max American Options ‣ 4 Numerical Results for American Options ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations") focuses on a two-asset call-on-max option with varying volatilities and dividend rates. Comparisons with traditional methods are not included in these two high-dimensional examples, as they become computationally infeasible. The parameters such as K,rK,r, and ρ\rho are chosen differently in these examples. By presenting this variety of examples with differing parameters and characteristics, we aim to demonstrate that the proposed method is robust and effective across a wide range of option types, dimensionalities, and market conditions.

For all experiments in this section, we employ a ResNet architecture consisting of M=4M=4 blocks, where each block contains L=2L=2 layers with 5050 nodes per layer. The hyperparameters are set as follows, λb​s=λt​v=λe​q=λt​c=1,l​rs​t​a​r​t=0.01,γ=0.9\lambda\_{bs}=\lambda\_{tv}=\lambda\_{eq}=\lambda\_{tc}=1,lr\_{start}=0.01,\gamma=0.9. The ETCNN takes the same λb​s,λt​v\lambda\_{bs},\lambda\_{tv} and λe​q\lambda\_{eq}. Additionally, the number of sampling points doubles every 80,000 iterations. Network architecture and hyperparameters were chosen based on standard practices in the literature and our own preliminary tests. Each experiment in this study is repeated three times, and the average results are reported to mitigate the stochastic effects of neural network training and ensure result reliability. All experiments are conducted on an NVIDIA A800 GPU.

### 4.1 Single-Asset American Put Options

This example considers a single-asset non-dividend-paying American put option. The value of the option V​(s,t)V(s,t) satisfies the following complementarity conditions,

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | | | | | |
|  |  | V​(s,t)≥(K−s)+,∀s≥0,t∈[0,T),\displaystyle\quad V(s,t)\geq(K-s)^{+},\quad\forall s\geq 0,t\in[0,T), |  |  | (15a) |
|  |  | ∂V∂t+12​σ2​s2​∂2V∂s2+r​s​∂V∂s−r​V≤0,∀s≥0,t∈[0,T),\displaystyle\quad\frac{\partial V}{\partial t}+\frac{1}{2}\sigma^{2}s^{2}\frac{\partial^{2}V}{\partial s^{2}}+rs\frac{\partial V}{\partial s}-rV\leq 0,\quad\forall s\geq 0,t\in[0,T), |  |  | (15b) |
|  |  | (∂V∂t+12​σ2​s2​∂2V∂s2+r​s​∂V∂s−r​V)⋅(V−(K−s)+)=0,∀s≥0,t∈[0,T),\displaystyle\quad\big(\frac{\partial V}{\partial t}+\frac{1}{2}\sigma^{2}s^{2}\frac{\partial^{2}V}{\partial s^{2}}+rs\frac{\partial V}{\partial s}-rV\big)\cdot\big(V-(K-s)^{+}\big)=0,\quad\forall s\geq 0,t\in[0,T), |  |  | (15c) |
|  |  | V​(s,T)=(K−s)+.\displaystyle\quad V(s,T)=(K-s)^{+}. |  |  | (15d) |

The term (K−s)+(K-s)^{+} denotes the terminal payoff. We design some terminal functions g2g\_{2} with specific properties to promote solution accuracy and stability.

#### 4.1.1 Exact Terminal Function Design

As previously stated, the value of an American put option can be written as

|  |  |  |
| --- | --- | --- |
|  | Va​(s,t)=Ve​(s,t)+p​(s,t),V^{a}(s,t)=V^{e}(s,t)+p(s,t), |  |

where Ve​(s,t)V^{e}(s,t) is the value of the corresponding European put. For simplicity of symbols, denote d1~\tilde{d\_{1}} and d2~\tilde{d\_{2}} as

|  |  |  |
| --- | --- | --- |
|  | d1~​(s,τ,K)=−1σ​τ​(ln⁡sK+(r+σ22)​τ),d2~​(s,τ,K)=−1σ​τ​(ln⁡sK+(r−σ22)​τ).\tilde{d\_{1}}(s,\tau,K)=-\frac{1}{\sigma\sqrt{\tau}}\big(\ln\frac{s}{K}+(r+\frac{\sigma^{2}}{2})\tau\big),\quad\tilde{d\_{2}}(s,\tau,K)=-\frac{1}{\sigma\sqrt{\tau}}\big(\ln\frac{s}{K}+(r-\frac{\sigma^{2}}{2})\tau\big). |  |

The value of the European option is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ve​(s,t)=K​e−r​τ⋅N​(d2~​(s,τ,K))−s⋅N​(d1~​(s,τ,K)).V^{e}(s,t)=Ke^{-r\tau}\cdot N\big(\tilde{d\_{2}}(s,\tau,K)\big)-s\cdot N\big(\tilde{d\_{1}}(s,\tau,K)\big). |  | (16) |

The term p​(s,t)p(s,t) is the early exercise premium. In Eq. ([14](https://arxiv.org/html/2510.27132v1#S3.E14 "In 3.5 Methodological Formulation for American Options ‣ 3 Methodology and Formulation ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations")), for an non-dividend American put option, Va​(S​(u),u)=Φ​(S​(u))V^{a}(S(u),u)=\Phi(S(u)) means (S​(u),u)(S(u),u) is in the stopping region and H​(s​(u),u)=r​KH(s(u),u)=rK [[16](https://arxiv.org/html/2510.27132v1#bib.bib16)]. Thus, we have the following expression for the premium,

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(s,t)\displaystyle p(s,t) | =𝐄t,s​[∫tTr​K​e−r​(u−t)​I​{s​(u)≤S∗​(u)}​𝑑u]\displaystyle=\mathbf{E}\_{t,s}\left[\int\_{t}^{T}rKe^{-r(u-t)}\textit{I}\{s(u)\leq S^{\*}(u)\}du\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =r​K​∫tTe−r​(u−t)​N​(−1σ​u−t​[ln⁡sS∗​(u)+(r−σ22)​(u−t)])​𝑑u\displaystyle=rK\int\_{t}^{T}e^{-r(u-t)}N\big(-\frac{1}{\sigma\sqrt{u-t}}[\ln\frac{s}{S^{\*}(u)}+(r-\frac{\sigma^{2}}{2})(u-t)]\big)du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =r​K​∫tTe−r​(u−t)​N​(−d2​(s,u−t,S∗​(u)))​𝑑u,\displaystyle=rK\int\_{t}^{T}e^{-r(u-t)}N(-d\_{2}(s,u-t,S^{\*}(u)))du, |  |

Here d2d\_{2} is defined in Eq. ([13](https://arxiv.org/html/2510.27132v1#S3.E13 "In 3.4 Illustrative Example: European Option ‣ 3 Methodology and Formulation ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations")). Therefore, the value of an American put option can be written as

|  |  |  |
| --- | --- | --- |
|  | Va​(s,t)=Ve​(s,t)+r​K​∫tTe−r​(u−t)​N​(−d2​(s,u−t,S∗​(u)))​𝑑u.V^{a}(s,t)=V^{e}(s,t)+rK\int\_{t}^{T}e^{-r(u-t)}N(-d\_{2}(s,u-t,S^{\*}(u)))du. |  |

The unknown boundary S∗​(t)S^{\*}(t) satisfies the following nonlinear Volterra integral equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | K−S∗​(t)\displaystyle K-S^{\*}(t) | =Ve​(S∗​(t),t)+r​K​∫tTe−r​(u−t)​N​(−1σ​u−t​[ln⁡S∗​(t)S∗​(u)+(r−σ22)​(u−t)])​𝑑u\displaystyle=V^{e}(S^{\*}(t),t)+rK\int\_{t}^{T}e^{-r(u-t)}N\big(-\frac{1}{\sigma\sqrt{u-t}}[\ln\frac{S^{\*}(t)}{S^{\*}(u)}+(r-\frac{\sigma^{2}}{2})(u-t)]\big)du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Ve​(S∗​(t),t)+r​K​∫tTe−r​(u−t)​N​(−d2​(S∗​(t),u−t,S∗​(u)))​𝑑u.\displaystyle=V^{e}(S^{\*}(t),t)+rK\int\_{t}^{T}e^{-r(u-t)}N\big(-d\_{2}(S^{\*}(t),u-t,S^{\*}(u))\big)du. |  |

However, S∗​(t)S^{\*}(t) has no explicit formula and is challenging to determine, which makes it difficult to find p​(s,t)p(s,t). As a result, the value function Va​(s,t)V^{a}(s,t) lacks a closed-form analytical solution.

The properties of S∗​(t)S^{\*}(t) have been widely studied in the literature, with a key property being its continuity in tt [[16](https://arxiv.org/html/2510.27132v1#bib.bib16)]. From the integral representation, p​(s,t)p(s,t) is differentiable when t<Tt<T and vanishes at t=Tt=T. However, Ve​(s,t)V^{e}(s,t) exhibits two types of singularities. First, it is non-differentiable at s=Ks=K when t=Tt=T. Second, it contains τ\sqrt{\tau} in denominators, which approaches 0 as t→Tt\rightarrow T. As a result, the term p​(s,t)p(s,t) is relatively easy for neural networks to approximate, whereas Ve​(s,t)V^{e}(s,t) is challenging due to these singularities. Given that European options share the same terminal conditions as American options, the term Ve​(s,t)V^{e}(s,t) not only encapsulates the singularity of Va​(s,t)V^{a}(s,t) but also adheres to the terminal conditions.

To solve for Va​(s,t)V^{a}(s,t), it is crucial to design a function g2g\_{2} that satisfies two key properties. First, it exactly satisfies the terminal conditions. Second, it incorporates both types of singularities inherent in Ve​(s,t)V^{e}(s,t). Such design makes the residual component Va​(s,t)−g2​(s,t)V^{a}(s,t)-g\_{2}(s,t) smoother and easier for the neural network to approximate.
A straightforward approach would be to set g2​(s,t)=Ve​(s,t)g\_{2}(s,t)=V^{e}(s,t). However, directly calculating Ve​(s,t)V^{e}(s,t) is computationally expensive. Instead, g2​(s,t)g\_{2}(s,t) is constructed as approximations of Ve​(s,t)V^{e}(s,t) that retain the singularities and exactly satisfy the terminal conditions, providing a more efficient and practical alternative.

Consider the term

|  |  |  |
| --- | --- | --- |
|  | d0~​(s,τ,K)=12​[d1~​(s,τ,K)+d2~​(s,τ,K)]=−1σ​τ​(ln⁡sK+r​τ).\tilde{d\_{0}}(s,\tau,K)=\frac{1}{2}\left[\tilde{d\_{1}}(s,\tau,K)+\tilde{d\_{2}}(s,\tau,K)\right]=-\frac{1}{\sigma\sqrt{\tau}}(\ln\frac{s}{K}+r\tau). |  |

The Taylor expansion of N​(x)N(x) at d0~\tilde{d\_{0}} can be written as

|  |  |  |
| --- | --- | --- |
|  | N​(x)=N​(d0~)+N′​(d0~)​(x−d0~)+𝒪​(x−d0~).N(x)=N(\tilde{d\_{0}})+N^{\prime}(\tilde{d\_{0}})(x-\tilde{d\_{0}})+{{\scriptscriptstyle\mathcal{O}}}(x-\tilde{d\_{0}}). |  |

Therefore N​(d1~)N(\tilde{d\_{1}}) and N​(d2~)N(\tilde{d\_{2}}) can be expanded as

|  |  |  |  |
| --- | --- | --- | --- |
|  | N​(d1~)\displaystyle N(\tilde{d\_{1}}) | =N​(d0~)+N′​(d0~)​(d1~−d0~)+𝒪​(d1~−d0~)=N​(d0~)−σ2​τ​N′​(d0~)+𝒪​(τ),\displaystyle=N(\tilde{d\_{0}})+N^{\prime}(\tilde{d\_{0}})(\tilde{d\_{1}}-\tilde{d\_{0}})+{{\scriptscriptstyle\mathcal{O}}}(\tilde{d\_{1}}-\tilde{d\_{0}})=N(\tilde{d\_{0}})-\frac{\sigma}{2}\sqrt{\tau}N^{\prime}(\tilde{d\_{0}})+{{\scriptscriptstyle\mathcal{O}}}(\sqrt{\tau}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | N​(d2~)\displaystyle N(\tilde{d\_{2}}) | =N​(d0~)+N′​(d0~)​(d2~−d0~)+𝒪​(d2~−d0~)=N​(d0~)+σ2​τ​N′​(d0~)+𝒪​(τ).\displaystyle=N(\tilde{d\_{0}})+N^{\prime}(\tilde{d\_{0}})(\tilde{d\_{2}}-\tilde{d\_{0}})+{{\scriptscriptstyle\mathcal{O}}}(\tilde{d\_{2}}-\tilde{d\_{0}})=N(\tilde{d\_{0}})+\frac{\sigma}{2}\sqrt{\tau}N^{\prime}(\tilde{d\_{0}})+{{\scriptscriptstyle\mathcal{O}}}(\sqrt{\tau}). |  |

Then the value of European put can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ve​(s,t)\displaystyle V^{e}(s,t) | =K​e−r​τ⋅N​(d2~​(s,τ,K))−s⋅N​(d1~​(s,τ,K))\displaystyle=Ke^{-r\tau}\cdot N\big(\tilde{d\_{2}}(s,\tau,K)\big)-s\cdot N\big(\tilde{d\_{1}}(s,\tau,K)\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =K​e−r​τ⋅[N​(d0~)+σ2​τ​N′​(d0~)+𝒪​(τ)]−s⋅[N​(d0~)−σ2​τ​N′​(d0~)+𝒪​(τ)]\displaystyle=Ke^{-r\tau}\cdot[N(\tilde{d\_{0}})+\frac{\sigma}{2}\sqrt{\tau}N^{\prime}(\tilde{d\_{0}})+{{\scriptscriptstyle\mathcal{O}}}(\sqrt{\tau})]-s\cdot[N(\tilde{d\_{0}})-\frac{\sigma}{2}\sqrt{\tau}N^{\prime}(\tilde{d\_{0}})+{{\scriptscriptstyle\mathcal{O}}}(\sqrt{\tau})] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =N​(d0~)⋅(K​e−r​τ−s)+σ2​τ​N′​(d0~)⋅(K​e−r​τ+s)+𝒪​(τ)\displaystyle=N(\tilde{d\_{0}})\cdot(Ke^{-r\tau}-s)+\frac{\sigma}{2}\sqrt{\tau}N^{\prime}(\tilde{d\_{0}})\cdot(Ke^{-r\tau}+s)+{{\scriptscriptstyle\mathcal{O}}}(\sqrt{\tau}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =N​(d0~)⋅(K​e−r​τ−s)+σ​τ2​2​π​e−d0~22⋅(K​e−r​τ+s)+𝒪​(τ).\displaystyle=N(\tilde{d\_{0}})\cdot(Ke^{-r\tau}-s)+\frac{\sigma\sqrt{\tau}}{2\sqrt{2\pi}}e^{-\frac{\tilde{d\_{0}}^{2}}{2}}\cdot(Ke^{-r\tau}+s)+{{\scriptscriptstyle\mathcal{O}}}(\sqrt{\tau}). |  |

Denote the first and second terms of the Taylor expansion of Ve​(s,t)V^{e}(s,t) as

|  |  |  |
| --- | --- | --- |
|  | V1e​(s,t)=N​(d0~)⋅(K​e−r​τ−s),V2e​(s,t)=σ​τ2​2​π​e−d0~22⋅(K​e−r​τ+s),V\_{1}^{e}(s,t)=N(\tilde{d\_{0}})\cdot(Ke^{-r\tau}-s),\quad V\_{2}^{e}(s,t)=\frac{\sigma\sqrt{\tau}}{2\sqrt{2\pi}}e^{-\frac{\tilde{d\_{0}}^{2}}{2}}\cdot(Ke^{-r\tau}+s), |  |

The value of Ve​(s,t)V^{e}(s,t) is then expressed as

|  |  |  |
| --- | --- | --- |
|  | Ve​(s,t)=V1e​(s,t)+V2e​(s,t)+𝒪​(τ).V^{e}(s,t)=V\_{1}^{e}(s,t)+V\_{2}^{e}(s,t)+{{\scriptscriptstyle\mathcal{O}}}(\sqrt{\tau}). |  |

It is easy to prove that both V1e​(s,t)V\_{1}^{e}(s,t) and V1e​(s,t)+V2e​(s,t)V\_{1}^{e}(s,t)+V\_{2}^{e}(s,t) satisfy the terminal condition ([15d](https://arxiv.org/html/2510.27132v1#S4.E15.4 "In 15 ‣ 4.1 Single-Asset American Put Options ‣ 4 Numerical Results for American Options ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations")).

Based on these observations, three candidate functions can be considered for the role of g2g\_{2} in the exact terminal method, V1e​(s,t),V1e​(s,t)+V2e​(s,t)V^{e}\_{1}(s,t),V^{e}\_{1}(s,t)+V^{e}\_{2}(s,t), and Ve​(s,t)V^{e}(s,t) itself. Both V1eV^{e}\_{1} and V1e+V2eV^{e}\_{1}+V^{e}\_{2}
preserve the non-differentiability at the terminal t=Tt=T.
However, only V1e+V2eV\_{1}^{e}+V\_{2}^{e}
captures the singular behavior associated with the denominator containing τ\sqrt{\tau} as t→Tt\rightarrow T. Consider the behavior of these functions as s=Ks=K when t→Tt\rightarrow T. The option when s=Ks=K is called an at-the-money option.
It is widely recognized in the literature that at-the-money options nearing their expiration date tend to approximate the value of 12​π​s​σ​τ\frac{1}{\sqrt{2\pi}}s\sigma\sqrt{\tau} [[42](https://arxiv.org/html/2510.27132v1#bib.bib42)]. For V1eV\_{1}^{e} and V1e+V2eV\_{1}^{e}+V\_{2}^{e}, consider the behavior at s=Ks=K when t→Tt\to T, and ignore higher-order terms than T−t=τ\sqrt{T-t}=\sqrt{\tau},

|  |  |  |  |
| --- | --- | --- | --- |
|  | limt→TV1e​(s,t)\displaystyle\lim\limits\_{t\to T}V\_{1}^{e}(s,t) | =N​(0)⋅K​(e−r⋅0−1)=0,\displaystyle=N(0)\cdot K(e^{-r\cdot 0}-1)=0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | limt→TV2e​(s,t)\displaystyle\lim\limits\_{t\to T}V\_{2}^{e}(s,t) | =σ​τ2​2​π​e−r2⋅02​σ2⋅K​(e−r⋅0+1)=12​π​K​σ​τ.\displaystyle=\frac{\sigma\sqrt{\tau}}{2\sqrt{2\pi}}e^{-\frac{r^{2}\cdot 0}{2\sigma^{2}}}\cdot K(e^{-r\cdot 0}+1)=\frac{1}{\sqrt{2\pi}}K\sigma\sqrt{\tau}. |  |

These results indicate that the behavior of V1e​(s,t)+V2e​(s,t)V^{e}\_{1}(s,t)+V^{e}\_{2}(s,t) captures the singular features present in Ve​(s,t)V^{e}(s,t) at s=Ks=K nearing t=Tt=T, while V1e​(s,t)V^{e}\_{1}(s,t) alone does not. Therefore, the residual part of VaV^{a} subtracting V1eV^{e}\_{1} alone does not prevent the network from encountering challenges associated with learning the singular features.

In summary, V1e​(s,t)V\_{1}^{e}(s,t) satisfies the terminal conditions, while V2e​(s,t)V\_{2}^{e}(s,t) captures the singular behavior of the option value around s=Ks=K as tt approaches the expiration TT. The combination V1e​(s,t)+V2e​(s,t)V\_{1}^{e}(s,t)+V\_{2}^{e}(s,t) simultaneously satisfies the terminal conditions and matches the singularity of Ve​(s,t)V^{e}(s,t). Moreover, it has a lower computational cost than Ve​(s,t)V^{e}(s,t). Therefore, V1e​(s,t)+V2e​(s,t)V\_{1}^{e}(s,t)+V\_{2}^{e}(s,t) is a suitable candidate for the exact terminal function g2​(s,t)g\_{2}(s,t). In the following analysis, we evaluate the performance of our ETCNN when g2g\_{2} takes these three functions V1e,V1e+V2eV\_{1}^{e},V\_{1}^{e}+V\_{2}^{e}, and VeV^{e} separately to determine which function yields the best results through a comparative analysis.

![Refer to caption](total_loss_norm.png)


(a) Total loss ℒ\mathcal{L} for models with input normalization

![Refer to caption](Loss_bs.png)


(b) ℒb​s\mathcal{L}\_{bs} for models with input normalization

![Refer to caption](Loss_tv.png)


(c) ℒt​v\mathcal{L}\_{tv} for models with input normalization

![Refer to caption](Loss_eq.png)


(d) ℒe​q\mathcal{L}\_{eq} for models with input normalization

Figure 5: Total loss and each loss terms for the four models.

#### 4.1.2 Numerical Results

The parameters for the experiments are set as K=100,r=0.02,T=1,σ=0.25K=100,r=0.02,T=1,\sigma=0.25. To evaluate the performance of PINN and ETCNN, experiments are conducted using all three exact terminal functions as g2g\_{2} to compare their effectiveness. We define g1​(s,t)=T−tg\_{1}(s,t)=T-t. The influence of input normalization on model performance is also examined. The binomial tree method with N=4000N=4000 steps is employed to compute the reference solution, serving as the benchmark for accuracy evaluation. We take Nt​c=512N\_{tc}=512 sampling points to calculate ℒt​c\mathcal{L}\_{tc}, and Nb​s=Nt​v=Ne​q=4​Nt​cN\_{bs}=N\_{tv}=N\_{eq}=4N\_{tc} to calculate the other three loss terms. Training is performed over the interval [20,160]×[0,T][20,160]\times[0,T], with error evaluation focused on the subset [60,120]×[0,T][60,120]\times[0,T].

We first analyze the evolution of the loss terms during the training process. The total loss, along with each individual loss term for the four models with input normalization, are illustrated in Figure [5](https://arxiv.org/html/2510.27132v1#S4.F5 "Figure 5 ‣ 4.1.1 Exact Terminal Function Design ‣ 4.1 Single-Asset American Put Options ‣ 4 Numerical Results for American Options ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations"). The last term ℒt​c=0\mathcal{L}\_{tc}=0 is inherently satisfied in the exact terminal methods. Therefore we only present results for ℒb​s,ℒt​v\mathcal{L}\_{bs},\mathcal{L}\_{tv} and ℒe​q\mathcal{L}\_{eq}. All plots are shown in logarithmic scale.
The results reveal that employing the exact terminal function with either g2​(s,t)=V1e​(s,t)+V2e​(s,t)g\_{2}(s,t)=V\_{1}^{e}(s,t)+V\_{2}^{e}(s,t) or g2​(s,t)=Ve​(s,t)g\_{2}(s,t)=V^{e}(s,t) significantly reduces the magnitude of each loss term. These values are several orders of magnitude smaller than those observed with PINN, demonstrating the effectiveness of the exact terminal methods. Additionally, ETCNN exhibits much faster convergence, achieving an accuracy comparable to that of a PINN trained for 200,000 epochs within only 10,000 epochs.
However, the performance of ETCNN with g2​(s,t)=V1e​(s,t)g\_{2}(s,t)=V\_{1}^{e}(s,t) is noticeably inferior, with loss terms exceeding those of the standard PINN. This result suggests that g2​(s,t)=V1e​(s,t)g\_{2}(s,t)=V\_{1}^{e}(s,t) is less effective compared to the other two choices of g2g\_{2} and highlights the importance of selecting an appropriate exact terminal function to ensure optimal model performance.

To further evaluate the accuracy of the solutions produced by the models, we employ two metrics, relative L2L^{2} error and maximum absolute error (MAE). The relative L2L^{2} error is defined as

|  |  |  |
| --- | --- | --- |
|  | εL2=‖Vt​r​u​e−Vp​r​e​d‖2‖Vt​r​u​e‖2=1N​∑i=1N(Vit​r​u​e−Vip​r​e​d)21N​∑i=1N(Vit​r​u​e)2,\varepsilon\_{L^{2}}=\frac{||V^{true}-V^{pred}||\_{2}}{||V^{true}||\_{2}}=\frac{\sqrt{\frac{1}{N}\sum\limits\_{i=1}^{N}(V\_{i}^{true}-V\_{i}^{pred})^{2}}}{\sqrt{\frac{1}{N}\sum\limits\_{i=1}^{N}(V\_{i}^{true})^{2}}}, |  |

where ||⋅||2||\cdot||\_{2} is the L2L\_{2} norm. Vp​r​e​d​(s,t)V^{pred}(s,t) is solution given by the model. NN is the number of samples taken to calculate the error. The MAE is defined as follows,

|  |  |  |
| --- | --- | --- |
|  | M​A​E=maxi⁡|Vit​r​u​e−Vip​r​e​d|.MAE=\max\limits\_{i}|V\_{i}^{true}-V\_{i}^{pred}|. |  |

Each experiment was repeated three times, and the average results were recorded in Table [3](https://arxiv.org/html/2510.27132v1#S4.T3 "Table 3 ‣ 4.1.2 Numerical Results ‣ 4.1 Single-Asset American Put Options ‣ 4 Numerical Results for American Options ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations").
The result indicates that the accuracy of solutions obtained by models with input normalization is better than those without it. This improvement shows the importance of designing an input normalization layer to preserve the homogeneous structure of the option value function with respect to the asset price ss.

Table 3: Relative L2L^{2} error and MAE in the ablation experiments. The first column on the left is the result of PINN. The last three columns are the results of ETCNN with three different exact terminal functions. The first two rows are the results of direct input, while the last two rows are the results of networks with input normalization. Bold font represents the best result in each row.

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Error | PINN | |  | | --- | | ETCNN | | g2=V1eg\_{2}=V\_{1}^{e} | | |  | | --- | | ETCNN | | g2=V1e+V2eg\_{2}=V\_{1}^{e}+V\_{2}^{e} | | |  | | --- | | ETCNN | | g2=Veg\_{2}=V^{e} | |
| Without normalization | Rel. L2L^{2} error | 1.87×10−31.87\times 10^{-3} | 4.12×10−34.12\times 10^{-3} | 1.08×10−41.08\times 10^{-4} | 6.91×10-5\textbf{6.91}\times\textbf{10}^{\textbf{-5}} |
| MAE | 2.23×10−12.23\times 10^{-1} | 1.76×10−11.76\times 10^{-1} | 8.52×10-3\textbf{8.52}\times\textbf{10}^{\textbf{-3}} | 1.06×10−21.06\times 10^{-2} |
| With normalization | Rel. L2L^{2} error | 1.20×10−31.20\times 10^{-3} | 3.35×10−33.35\times 10^{-3} | 5.72×10−55.72\times 10^{-5} | 5.34×10-5\textbf{5.34}\times\textbf{10}^{\textbf{-5}} |
| MAE | 1.16×10−11.16\times 10^{-1} | 1.31×10−11.31\times 10^{-1} | 5.71×10-3\textbf{5.71}\times\textbf{10}^{\textbf{-3}} | 6.90×10−36.90\times 10^{-3} |

ETCNN with both g2​(s,t)=Ve​(s,t)g\_{2}(s,t)=V^{e}(s,t) and g2​(s,t)=V1e​(s,t)+V2e​(s,t)g\_{2}(s,t)=V\_{1}^{e}(s,t)+V\_{2}^{e}(s,t)
exhibit significant improvements in accuracy compared to PINN, reducing errors by 1-2 orders of magnitude. In terms of the L2L^{2} error, ETCNN with g2=Veg\_{2}=V^{e} achieves the lowest error, followed closely by g2=V1e+V2eg\_{2}=V\_{1}^{e}+V\_{2}^{e}. In terms of MAE, the lowest value is obtained by ETCNN with g2=V1e+V2eg\_{2}=V\_{1}^{e}+V\_{2}^{e}, followed by g2=Veg\_{2}=V^{e}. When input normalization is applied, the performance of ETCNN with g2=V1e+V2eg\_{2}=V\_{1}^{e}+V\_{2}^{e} is nearly indistinguishable from ETCNN with g2=Veg\_{2}=V^{e}, both achieving remarkably low error values. Specifically, the L2L^{2} errors for both models are approximately 5×10−55\times 10^{-5}, while their MAE values are around 6×10−36\times 10^{-3}. These results imply that, for an option with an exercise price of K=100K=100 units of currency, the maximum absolute error of the solutions obtained using ETCNN with g2=V1e+V2eg\_{2}=V\_{1}^{e}+V\_{2}^{e} or g2=Veg\_{2}=V^{e} is less than one cent, which is a very low error in practice.
In contrast, ETCNN with g2=V1eg\_{2}=V\_{1}^{e} yields the poorest performance, even worse than PINN. This outcome highlights that not all solutions that exactly satisfy boundary conditions lead to lower errors.
Merely fulfilling the terminal conditions is insufficient to ensure accurate solutions. The effectiveness of the method is strongly dependent on the smoothness and structure of the residual difference between Vt​r​u​eV^{true} and the chosen g2g\_{2}. This observation emphasizes the critical importance of selecting an appropriate g2g\_{2}.

![Refer to caption](Diff12.png)
  


Figure 6: Pointwise difference between the true solution and predicted solution obtained by the PINN and ETCNN with three g2g\_{2} functions. (a​1)(a1), PINN. (a​2)(a2), PINN + Norm. (b​1)(b1), ETCNN (g2=V1e)(g\_{2}=V\_{1}^{e}). (b​2)(b2), ETCNN (g2=V1e)(g\_{2}=V\_{1}^{e}) + Norm. (c​1)(c1), ETCNN (g2=V1e+V2e)(g\_{2}=V\_{1}^{e}+V\_{2}^{e}). (c​2)(c2), ETCNN (g2=V1e+V2e)(g\_{2}=V\_{1}^{e}+V\_{2}^{e}) + Norm. (d​1)(d1), ETCNN (g2=Ve)(g\_{2}=V^{e}). (d​2)(d2), ETCNN (g2=Ve)(g\_{2}=V^{e}) + Norm.

To better illustrate the results of the previous table, Figure [6](https://arxiv.org/html/2510.27132v1#S4.F6 "Figure 6 ‣ 4.1.2 Numerical Results ‣ 4.1 Single-Asset American Put Options ‣ 4 Numerical Results for American Options ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations") shows the pointwise difference between the predicted solution by PINN or ETCNN and the true solution. The pointwise difference is defined as the difference between the true solution and the model prediction,

|  |  |  |
| --- | --- | --- |
|  | Diff​(s,t)=Vt​r​u​e​(s,t)−Vp​r​e​d​(s,t).\text{Diff}(s,t)=V^{true}(s,t)-V^{pred}(s,t). |  |

Models incorporating an input normalization layer consistently achieve lower absolute errors compared to those without. Among the ETCNN models, g2=Veg\_{2}=V^{e} and g2=V1e+V2eg\_{2}=V\_{1}^{e}+V\_{2}^{e} exhibit far superior performance relative to PINN, whereas the performance of g2=V1eg\_{2}=V^{e}\_{1} falls below that of PINN.
Notably, when input normalization is applied,
the performance of g2=V1e+V2eg\_{2}=V\_{1}^{e}+V\_{2}^{e} is comparable to that of g2=Veg\_{2}=V^{e}.
However, computing VeV^{e} is more computationally expensive than calculating V1e+V2eV\_{1}^{e}+V\_{2}^{e}, as it requires evaluating the cumulative distribution function twice at different points. Therefore, we select the ETCNN model using g2=V1e+V2eg\_{2}=V\_{1}^{e}+V\_{2}^{e} and with an input normalization layer as the final model. A detailed analysis of this model’s results is provided in the following paragraph.

Additionally, Figure [6](https://arxiv.org/html/2510.27132v1#S4.F6 "Figure 6 ‣ 4.1.2 Numerical Results ‣ 4.1 Single-Asset American Put Options ‣ 4 Numerical Results for American Options ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations") reveals an increase in error near the early exercise boundary, highlighting the added complexity of solving equations with unknown free boundaries. This behavior reflects the additional challenge introduced by the free-boundary feature in option pricing. Figure [7](https://arxiv.org/html/2510.27132v1#S4.F7 "Figure 7 ‣ 4.1.2 Numerical Results ‣ 4.1 Single-Asset American Put Options ‣ 4 Numerical Results for American Options ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations") compares the free boundary obtained from the true solution, the PINN solution, and the ETCNN solution with g2​(s,t)=V1e​(s,t)+V2e​(s,t)g\_{2}(s,t)=V^{e}\_{1}(s,t)+V^{e}\_{2}(s,t).
The early exercise boundary derived from ETCNN closely aligns with the true early exercise boundary, showing near-complete overlap. In contrast, the early exercise boundary derived from the PINN shows noticeable deviations, particularly at points far from the expiration date.
These results show the capability of our method to effectively handle the challenges posed by free boundary problems.

![Refer to caption](Early_exercise_boundary_for_PINN_and_ECTNN.png)
  


Figure 7: Early exercise boundary. (a), Early exercise boundary obtained by the exact solution and PINN. (b), Early exercise boundary obtained by the exact solution and ECTNN with g2​(s,t)=V1e​(s,t)+V2e​(s,t)g\_{2}(s,t)=V^{e}\_{1}(s,t)+V^{e}\_{2}(s,t). Both PINN and ETCNN implement input normalization.

We extend our analysis by comparing the performance of ETCNN with some traditional methods: Barone-Adesi and Whaley (BAW) method, the binomial tree (BT), finite difference (FD), and least squares Monte Carlo (LSM) method. For the BT and FD methods, results are evaluated using N=100,200N=100,200, and 400400 steps. In the case of the LSM approach, simulations are performed with M=10,000M=10,000 paths, and results are obtained for N=100,200N=100,200, and 400400 steps as well. The comparative results of these methods are summarized in Table [4](https://arxiv.org/html/2510.27132v1#S4.T4 "Table 4 ‣ 4.1.2 Numerical Results ‣ 4.1 Single-Asset American Put Options ‣ 4 Numerical Results for American Options ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations").

Table 4: Relative L2L^{2} error and MAE comparison of ETCNN, PINN, and traditional numerical methods. ETCNN takes g2=V1e+V2eg\_{2}=V\_{1}^{e}+V\_{2}^{e}. Both PINN and ECTNN implement input normalization. Bold font represents the best result.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Methods | Rel. L2L^{2} error | MAE | Methods | Rel. L2L^{2} error | MAE |
| ETCNN | 5.72×10-5\textbf{5.72}\times\textbf{10}^{\textbf{-5}} | 5.71×10-3\textbf{5.71}\times\textbf{10}^{\textbf{-3}} | FD(N=100N=100) | 5.36×10−45.36\times 10^{-4} | 3.82×10−23.82\times 10^{-2} |
| PINN | 1.20×10−31.20\times 10^{-3} | 1.16×10−11.16\times 10^{-1} | FD(N=200N=200) | 2.78×10−42.78\times 10^{-4} | 2.00×10−22.00\times 10^{-2} |
| BAW | 1.49×10−31.49\times 10^{-3} | 9.03×10−29.03\times 10^{-2} | FD(N=400N=400) | 1.46×10−41.46\times 10^{-4} | 1.05×10−21.05\times 10^{-2} |
| BT(N=100N=100) | 3.99×10−43.99\times 10^{-4} | 2.46×10−22.46\times 10^{-2} | LSM(N=100N=100) | 2.38×10−32.38\times 10^{-3} | 2.24×10−12.24\times 10^{-1} |
| BT(N=200N=200) | 1.97×10−41.97\times 10^{-4} | 1.27×10−21.27\times 10^{-2} | LSM(N=200N=200) | 2.45×10−32.45\times 10^{-3} | 2.53×10−12.53\times 10^{-1} |
| BT(N=400N=400) | 9.78×10−59.78\times 10^{-5} | 6.61×10−36.61\times 10^{-3} | LSM(N=400N=400) | 2.61×10−32.61\times 10^{-3} | 2.21×10−12.21\times 10^{-1} |

The performance of the LSM method is the least favorable among the evaluated approaches, while the BAW approximation performs slightly better but remains among the less accurate methods. PINN yields higher accuracy than both LSM and BAW but still falls short of the FD and BT methods. This suggests that solutions obtained using a neural network without any specific design are less accurate than traditional numerical methods.
In contrast, our ETCNN not only surpasses PINN but also outperforms several traditional numerical methods in terms of accuracy. Specifically, our ETCNN achieves the lowest relative L2L^{2} error and the smallest MAE. Among all evaluated methods, only ETCNN and the BT method with larger step sizes can achieve an MAE on the order of 10−310^{-3}, which is a huge advantage in actual transactions.

To further illustrate the accuracy of the proposed approach, Table [5](https://arxiv.org/html/2510.27132v1#S4.T5 "Table 5 ‣ 4.1.2 Numerical Results ‣ 4.1 Single-Asset American Put Options ‣ 4 Numerical Results for American Options ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations") reports the option values at several fixed (s,t)(s,t) points (tt is the current time and T−tT-t is the time to maturity), along with the average computation time required by each method. For the ETCNN and PINN models, the reported times correspond to the evaluation phase of the trained networks, excluding the training process. The remaining model parameters are fixed as before (K=100K=100, r=0.02r=0.02, σ=0.25,T=1\sigma=0.25,T=1). The reference values in the first column are obtained using the BT method with N=4000N=4000, which serves as a benchmark for the true solution. The second column presents the corresponding European option prices under the same parameters, computed from Eq. ([16](https://arxiv.org/html/2510.27132v1#S4.E16 "In 4.1.1 Exact Terminal Function Design ‣ 4.1 Single-Asset American Put Options ‣ 4 Numerical Results for American Options ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations")). The difference between these two columns represents the early exercise premium. The subsequent columns list the results obtained from the proposed ETCNN (g2=V1e+V2eg\_{2}=V\_{1}^{e}+V\_{2}^{e}), PINN, BAW, BT (N=400N=400), FD (N=400N=400), and LSM (N=400N=400) methods. This comparison clearly shows the deviations of each method from the benchmark solution.

Table 5: The price of American put options with fixed model parameters (K=100K=100, r=0.02r=0.02, σ=0.25,T=1\sigma=0.25,T=1) calculated by ETCNN, PINN, and traditional methods. The binomial tree method with N=4000N=4000 serves as the reference solution. Ve​(s,t)V^{e}(s,t) denotes the price of European options with the same parameters (calculated by Eq. ([16](https://arxiv.org/html/2510.27132v1#S4.E16 "In 4.1.1 Exact Terminal Function Design ‣ 4.1 Single-Asset American Put Options ‣ 4 Numerical Results for American Options ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations"))). Bold represents the solution closest to the reference solution among the six methods. The average time consumption (in milliseconds) for each method represents the mean evaluation time over all sample points listed in the table.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Time to  expiration  T−tT-t | Underlying  price ss | Ref. solution  BT(N=4000) | European  Ve​(s,t)V^{e}(s,t) | ETCNN | PINN | BAW | BT  (N=400) | FD  (N=400) | LSM  (N=400) |
| 0.25 | 80 | 20.010 | 19.684 | 20.011 | 20.022 | 20.000 | 20.010 | 20.009 | 20.036 |
| 90 | 11.030 | 10.914 | 11.030 | 11.052 | 10.999 | 11.032 | 11.029 | 11.005 |
| 100 | 4.759 | 4.726 | 4.759 | 4.786 | 4.752 | 4.757 | 4.754 | 4.660 |
| 110 | 1.571 | 1.563 | 1.572 | 1.603 | 1.572 | 1.573 | 1.570 | 1.562 |
| 120 | 0.403 | 0.401 | 0.404 | 0.436 | 0.404 | 0.403 | 0.403 | 0.417 |
| 0.5 | 80 | 20.306 | 19.875 | 20.307 | 20.323 | 20.247 | 20.307 | 20.305 | 20.475 |
| 90 | 12.289 | 12.101 | 12.289 | 12.314 | 12.249 | 12.287 | 12.285 | 12.239 |
| 100 | 6.597 | 6.522 | 6.598 | 6.626 | 6.587 | 6.595 | 6.590 | 6.665 |
| 110 | 3.155 | 3.127 | 3.156 | 3.185 | 3.157 | 3.159 | 3.153 | 3.158 |
| 120 | 1.361 | 1.351 | 1.362 | 1.390 | 1.366 | 1.362 | 1.359 | 1.333 |
| 0.75 | 80 | 20.761 | 20.228 | 20.762 | 20.778 | 20.684 | 20.762 | 20.757 | 20.671 |
| 90 | 13.336 | 13.075 | 13.337 | 13.360 | 13.290 | 13.336 | 13.333 | 13.341 |
| 100 | 7.955 | 7.832 | 7.956 | 7.983 | 7.942 | 7.951 | 7.946 | 8.036 |
| 110 | 4.435 | 4.379 | 4.436 | 4.463 | 4.439 | 4.439 | 4.429 | 4.475 |
| 120 | 2.332 | 2.307 | 2.333 | 2.361 | 2.341 | 2.334 | 2.331 | 2.317 |
| Ave. computational  time (ms) | | - | - | 1.095 | 0.447 | 7.654 | 60.22 | 453.98 | 476.11 |

The results show that the proposed method consistently achieves the highest accuracy across various (s,t)(s,t) cases, including scenarios close to maturity as well as those far from maturity, and for options that are in-the-money, at-the-money, or out-of-the-money. This demonstrates the strong robustness and stability of the proposed approach under different market conditions.
Furthermore, a trained ETCNN can efficiently compute option values at a large number of points, whereas traditional methods require longer computation time, especially when estimating values across multiple points. For instance, both the BT and FD methods require NN iterative steps, calculating each step sequentially. Similarly, LSM needs to generate MM simulation paths and perform least squares fitting. The BAW method, although faster than other numerical schemes, still cannot match the evaluation speed of a well-trained ETCNN when applied repeatedly. Therefore, our ETCNN with a carefully designed g2g\_{2} function not only offers superior accuracy but also provides an advantage in computational speed.

### 4.2 American Call Options with Dividends

The valuation of a single-asset American call option without dividends is equivalent to its European counterpart, making its value straightforward to compute. However, when the underlying asset pays dividends, the American call option typically holds a premium over its European counterpart, and its value does not have a closed-form solution.

For an American call option on an asset with a continuous dividend yield qq, its value satisfies the following modified
version linear complementarity conditions,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | V​(s,t)≥(s−K)+,∀s≥0,t∈[0,T),\displaystyle\quad V(s,t)\geq(s-K)^{+},\quad\forall s\geq 0,t\in[0,T), |  |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ∂V∂t+12​σ2​s2​∂2V∂s2+(r−q)​s​∂V∂s−r​V≤0,∀s≥0,t∈[0,T),\displaystyle\quad\frac{\partial V}{\partial t}+\frac{1}{2}\sigma^{2}s^{2}\frac{\partial^{2}V}{\partial s^{2}}+(r-q)s\frac{\partial V}{\partial s}-rV\leq 0,\quad\forall s\geq 0,t\in[0,T), |  |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | (∂V∂t+12​σ2​s2​∂2V∂s2+(r−q)​s​∂V∂s−r​V)⋅(V−(s−K)+)=0,∀s≥0,t∈[0,T),\displaystyle\quad\big(\frac{\partial V}{\partial t}+\frac{1}{2}\sigma^{2}s^{2}\frac{\partial^{2}V}{\partial s^{2}}+(r-q)s\frac{\partial V}{\partial s}-rV\big)\cdot\big(V-(s-K)^{+}\big)=0,\quad\forall s\geq 0,t\in[0,T), |  |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | V​(s,T)=(s−K)+.\displaystyle\quad V(s,T)=(s-K)^{+}. |  |  |

The exact solution for its European counterpart differs slightly from Eq. ([12](https://arxiv.org/html/2510.27132v1#S3.E12 "In 3.4 Illustrative Example: European Option ‣ 3 Methodology and Formulation ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations")) due to the inclusion of the dividend term. The modified form is given as follows,

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(s,t)=s​e−q​τ​N​(d1^​(s,τ,K))−K​e−r​τ​N​(d2^​(s,τ,K)).V(s,t)=se^{-q\tau}N(\hat{d\_{1}}(s,\tau,K))-Ke^{-r\tau}N(\hat{d\_{2}}(s,\tau,K)). |  | (17) |

Here, d1^,d2^\hat{d\_{1}},\hat{d\_{2}} are defined as :

|  |  |  |
| --- | --- | --- |
|  | {d1^​(s,τ,K)=1σ​τ​(ln⁡sK+(r−q+σ22)​τ),d2^​(s,τ,K)=d1^​(s,τ,K)−σ​τ=1σ​τ​(ln⁡sK+(r−q−σ22)​τ).\displaystyle\left\{\begin{aligned} \quad&\hat{d\_{1}}(s,\tau,K)=\frac{1}{\sigma\sqrt{\tau}}\big(\ln{\frac{s}{K}}+(r-q+\frac{\sigma^{2}}{2})\tau\big),\\ \quad&\hat{d\_{2}}(s,\tau,K)=\hat{d\_{1}}(s,\tau,K)-\sigma\sqrt{\tau}=\frac{1}{\sigma\sqrt{\tau}}\big(\ln{\frac{s}{K}}+(r-q-\frac{\sigma^{2}}{2})\tau\big).\end{aligned}\right. |  |

Similar to the previous example, we take

|  |  |  |
| --- | --- | --- |
|  | d0^​(s,τ,K)=12​(d1^​(s,τ,K)+d2^​(s,τ,K)).\hat{d\_{0}}(s,\tau,K)=\frac{1}{2}(\hat{d\_{1}}(s,\tau,K)+\hat{d\_{2}}(s,\tau,K)). |  |

By applying a first-order Taylor expansion to N​(⋅)N(\cdot) and substituting the result into Eq. ([17](https://arxiv.org/html/2510.27132v1#S4.E17 "In 4.2 American Call Options with Dividends ‣ 4 Numerical Results for American Options ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations"))(\ref{new\_17a}), an exact terminal function g2​(s,t)g\_{2}(s,t) is derived for single-asset American call options with continuous dividend payments,

|  |  |  |  |
| --- | --- | --- | --- |
|  | g2​(s,t)=N​(d0^)​[s​e−q​τ−K​e−r​τ]+12​2​π​σ​τ​e−d0^22​[s​e−q​τ+K​e−r​τ].g\_{2}(s,t)=N(\hat{d\_{0}})[se^{-q\tau}-Ke^{-r\tau}]+\frac{1}{2\sqrt{2\pi}}\sigma\sqrt{\tau}e^{-\frac{\hat{d\_{0}}^{2}}{2}}[se^{-q\tau}+Ke^{-r\tau}]. |  | (18) |

The output of our ETCNN in this experiment is u~N​N​(s,t)=g1​(s,t)​uN​N​(s,t)+g2​(s,t)\tilde{u}\_{NN}(s,t)=g\_{1}(s,t)u\_{NN}(s,t)+g\_{2}(s,t), where g2g\_{2} is defined in Eq. ([18](https://arxiv.org/html/2510.27132v1#S4.E18 "In 4.2 American Call Options with Dividends ‣ 4 Numerical Results for American Options ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations")) and g1​(s,t)=T−tg\_{1}(s,t)=T-t.

In this example, we set K=200,r=0.05,T=2K=200,r=0.05,T=2. To demonstrate the robustness of our ETCNN, various parameter configurations have been applied.
The volatility level σ\sigma is chosen to take values of 0.1,0.250.1,0.25, and 0.40.4, representing markets with different volatility conditions. Dividend yields are varied across {0.01,0.03,0.05,0.07}\{0.01,0.03,0.05,0.07\} to assess applicability to both low-dividend and high-dividend-paying assets.
Input normalization is applied in all experiments for both PINN and ETCNN models.
The number of sampling points for calculating ℒt​c\mathcal{L}\_{tc} is Nt​c=8192N\_{tc}=8192, while ℒb​s,ℒt​v\mathcal{L}\_{bs},\mathcal{L}\_{tv} and ℒe​q\mathcal{L}\_{eq} uses 4​Nt​c4N\_{tc} points. Training is conducted over
[0,800]×[0,T][0,800]\times[0,T], with evaluation of errors on the subdomain [160,240]×[0,T][160,240]\times[0,T] to measure performance. The solution obtained by the binomial tree method with N=4000N=4000 serves as the reference for the true solution. The relative L2L^{2} errors between the solutions obtained from different methods and the reference solution are compared. The results are reported in Table [6](https://arxiv.org/html/2510.27132v1#S4.T6 "Table 6 ‣ 4.2 American Call Options with Dividends ‣ 4 Numerical Results for American Options ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations").

Table 6: Relative L2L^{2} error for American call options with different volatility σ\sigma and dividend rate qq. Comparisons are made between our ETCNN and other methods. Both PINN and ETCNN apply the input normalization technique. Bold font represents the best result in each column.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Methods | σ=0.1\sigma=0.1 | | | |
| q=0.01q=0.01 | q=0.03q=0.03 | q=0.05q=0.05 | q=0.07q=0.07 |
| ETCNN | 3.79×10−53.79\times 10^{-5} | 5.98×10-5\textbf{5.98}\times\textbf{10}^{\textbf{-5}} | 1.69×10−41.69\times 10^{-4} | 4.15×10−44.15\times 10^{-4} |
| PINN | 2.81×10−32.81\times 10^{-3} | 3.00×10−33.00\times 10^{-3} | 4.48×10−34.48\times 10^{-3} | 4.02×10−34.02\times 10^{-3} |
| BAW | 1.05×10-5\textbf{1.05}\times\textbf{10}^{\textbf{-5}} | 4.02×10−44.02\times 10^{-4} | 1.86×10−31.86\times 10^{-3} | 2.45×10−32.45\times 10^{-3} |
| BT(N = 400) | 9.34×10−59.34\times 10^{-5} | 9.67×10−59.67\times 10^{-5} | 9.87×10-5\textbf{9.87}\times\textbf{10}^{\textbf{-5}} | 6.48×10-5\textbf{6.48}\times\textbf{10}^{\textbf{-5}} |
| FD(N = 400) | 1.06×10−41.06\times 10^{-4} | 1.06×10−41.06\times 10^{-4} | 1.68×10−41.68\times 10^{-4} | 3.01×10−43.01\times 10^{-4} |
| LSM(N = 400) | 3.02×10−33.02\times 10^{-3} | 5.27×10−35.27\times 10^{-3} | 3.67×10−33.67\times 10^{-3} | 2.53×10−32.53\times 10^{-3} |
| Methods | σ=0.25\sigma=0.25 | | | |
| q=0.01q=0.01 | q=0.03q=0.03 | q=0.05q=0.05 | q=0.07q=0.07 |
| ETCNN | 7.16×10−57.16\times 10^{-5} | 1.78×10-4\textbf{1.78}\times\textbf{10}^{\textbf{-4}} | 2.18×10-4\textbf{2.18}\times\textbf{10}^{\textbf{-4}} | 2.23×10-4\textbf{2.23}\times\textbf{10}^{\textbf{-4}} |
| PINN | 2.43×10−32.43\times 10^{-3} | 3.28×10−33.28\times 10^{-3} | 3.86×10−33.86\times 10^{-3} | 4.33×10−34.33\times 10^{-3} |
| BAW | 5.15×10-5\textbf{5.15}\times\textbf{10}^{\textbf{-5}} | 2.98×10−32.98\times 10^{-3} | 4.49×10−34.49\times 10^{-3} | 5.12×10−35.12\times 10^{-3} |
| BT(N = 400) | 2.33×10−42.33\times 10^{-4} | 2.59×10−42.59\times 10^{-4} | 2.72×10−42.72\times 10^{-4} | 2.52×10−42.52\times 10^{-4} |
| FD(N = 400) | 1.77×10−41.77\times 10^{-4} | 2.12×10−42.12\times 10^{-4} | 3.59×10−43.59\times 10^{-4} | 5.74×10−45.74\times 10^{-4} |
| LSM(N = 400) | 1.45×10−21.45\times 10^{-2} | 1.06×10−21.06\times 10^{-2} | 8.27×10−38.27\times 10^{-3} | 7.52×10−37.52\times 10^{-3} |
| Methods | σ=0.4\sigma=0.4 | | | |
| q=0.01q=0.01 | q=0.03q=0.03 | q=0.05q=0.05 | q=0.07q=0.07 |
| ETCNN | 8.45×10-5\textbf{8.45}\times\textbf{10}^{\textbf{-5}} | 1.85×10-4\textbf{1.85}\times\textbf{10}^{\textbf{-4}} | 1.68×10-4\textbf{1.68}\times\textbf{10}^{\textbf{-4}} | 2.53×10-4\textbf{2.53}\times\textbf{10}^{\textbf{-4}} |
| PINN | 2.57×10−32.57\times 10^{-3} | 2.72×10−32.72\times 10^{-3} | 3.19×10−33.19\times 10^{-3} | 3.72×10−33.72\times 10^{-3} |
| BAW | 3.50×10−43.50\times 10^{-4} | 4.08×10−34.08\times 10^{-3} | 5.53×10−35.53\times 10^{-3} | 6.54×10−36.54\times 10^{-3} |
| BT(N = 400) | 2.96×10−42.96\times 10^{-4} | 3.14×10−43.14\times 10^{-4} | 3.24×10−43.24\times 10^{-4} | 3.17×10−43.17\times 10^{-4} |
| FD(N = 400) | 2.58×10−42.58\times 10^{-4} | 3.24×10−43.24\times 10^{-4} | 5.02×10−45.02\times 10^{-4} | 7.01×10−47.01\times 10^{-4} |
| LSM(N = 400) | 1.81×10−21.81\times 10^{-2} | 1.45×10−21.45\times 10^{-2} | 1.11×10−21.11\times 10^{-2} | 1.07×10−21.07\times 10^{-2} |

The results demonstrate that the proposed ETCNN outperforms other methods across most of the various scenarios, particularly in high-volatility markets. Compared to PINN, ETCNN achieves a reduction in L2L^{2} error by an order of magnitude.
When compared with traditional numerical methods, ETCNN exhibits superior robustness under challenging market conditions. As volatility and dividend yields increase, the errors associated with traditional methods grow substantially, whereas ETCNN maintains an L2L^{2} error of approximately 2×10−42\times 10^{-4}, showing its robustness and adaptability to diverse and fluctuating market conditions.

Among the tested approaches, LSM shows the poorest performance, while BAW performs slightly better than LSM and is comparable to PINN. It is worth noting that BAW achieves relatively high accuracy when the dividend yield is small, as the option price becomes closer to that of a European option under such conditions.
Overall, ETCNN outperforms traditional approaches and standard PINN in terms of accuracy across most scenarios.
This makes ETCNN a more reliable and practical solution compared to both traditional methods and standard PINN.

We further evaluated the proposed method under fixed option parameters by setting K=2K=2, r=0.05r=0.05, and T=2T=2, while varying the volatility, dividend yield, time, and underlying asset price. Table [7](https://arxiv.org/html/2510.27132v1#S4.T7 "Table 7 ‣ 4.2 American Call Options with Dividends ‣ 4 Numerical Results for American Options ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations") shows that our method consistently achieves the highest accuracy across different parameter settings, demonstrating strong robustness to changes in market conditions. Moreover, the trained network exhibits a high computational efficiency, achieving rapid inference once training is completed.

Table 7: The price of American call options with fixed model parameters (K=200K=200, r=0.05r=0.05, T=2T=2) calculated by ETCNN, PINN, and traditional methods. The binomial tree method with N=4000N=4000 serves as the reference solution. Ve​(s,t)V^{e}(s,t) denotes the price of European options with the same parameters (calculated by Eq. ([17](https://arxiv.org/html/2510.27132v1#S4.E17 "In 4.2 American Call Options with Dividends ‣ 4 Numerical Results for American Options ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations"))). Bold represents the solution closest to the reference solution among the six methods. The average time consumption (in milliseconds) for each method represents the mean evaluation time over all sample points listed in the table.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Option  parameters | Underlying  price ss | Ref. solution  BT(N=4000) | European  Ve​(s,t)V^{e}(s,t) | ETCNN | PINN | BAW | BT  (N=400) | FD  (N=400) | LSM  (N=400) |
| σ=0.25\sigma=0.25  q=0.05q=0.05  T−t=0.5T-t=0.5 | 180 | 5.560 | 5.542 | 5.561 | 5.650 | 5.577 | 5.555 | 5.555 | 5.715 |
| 200 | 13.805 | 13.739 | 13.805 | 13.890 | 13.824 | 13.798 | 13.792 | 13.755 |
| 220 | 26.409 | 26.219 | 26.410 | 26.484 | 26.413 | 26.416 | 26.405 | 26.149 |
| σ=0.4\sigma=0.4  q=0.05q=0.05  T−t=0.5T-t=0.5 | 180 | 12.553 | 12.506 | 12.556 | 12.661 | 12.582 | 12.560 | 12.548 | 12.752 |
| 200 | 22.044 | 21.937 | 22.047 | 22.154 | 22.075 | 22.033 | 22.022 | 21.612 |
| 220 | 34.288 | 34.073 | 34.288 | 34.394 | 34.306 | 34.299 | 34.273 | 33.995 |
| σ=0.25\sigma=0.25  q=0.07q=0.07  T−t=0.5T-t=0.5 | 180 | 5.095 | 5.025 | 5.098 | 5.178 | 5.125 | 5.091 | 5.088 | 5.245 |
| 200 | 12.966 | 12.722 | 12.969 | 13.038 | 12.979 | 12.961 | 12.951 | 13.029 |
| 220 | 25.321 | 24.670 | 25.326 | 25.380 | 25.270 | 25.328 | 25.313 | 25.263 |
| σ=0.25\sigma=0.25  q=0.05q=0.05  T−t=1T-t=1 | 180 | 10.114 | 10.030 | 10.118 | 10.199 | 10.179 | 10.117 | 10.104 | 10.388 |
| 200 | 19.138 | 18.925 | 19.142 | 19.221 | 19.213 | 19.129 | 19.120 | 19.300 |
| 220 | 31.264 | 30.802 | 31.268 | 31.344 | 31.324 | 31.267 | 31.260 | 30.956 |
| Ave. computational  time (in ms) | | - | - | 1.897 | 0.431 | 9.265 | 60.08 | 485.46 | 548.32 |

### 4.3 Multi-Asset Options with Geometric Average Payoffs

In this example, the focus is on multi-asset American put options, where the payoff function is defined as the geometric mean of the prices of nn underlying assets.
Let I=I​(s1,⋯,sn)=(∏i=1nsi​(t))1nI=I(s\_{1},\cdots,s\_{n})=\big(\prod\_{i=1}^{n}s\_{i}(t)\big)^{\frac{1}{n}} be the geometric mean of {s1,⋯,sn}\{s\_{1},\cdots,s\_{n}\}. The payoff function is defined as

|  |  |  |
| --- | --- | --- |
|  | Φ​(s1,⋯,sn)=(K−(∏i=1nsi)1n)+=(K−I)+.\Phi(s\_{1},\cdots,s\_{n})=\Big(K-\big(\prod\_{i=1}^{n}s\_{i}\big)^{\frac{1}{n}}\Big)^{+}=(K-I)^{+}. |  |

The PDE operator is

|  |  |  |
| --- | --- | --- |
|  | ℱ​(V​(s1,⋯,sn,t))=∂V∂t+12​∑i,j=1nσi​σj​ρi​j​si​sj​∂2V∂si​∂sj+∑i=1n(r−qi)​si​∂V∂si−r​V.\mathcal{F}(V(s\_{1},\cdots,s\_{n},t))=\frac{\partial V}{\partial t}+\frac{1}{2}\sum\limits\_{i,j=1}^{n}\sigma\_{i}\sigma\_{j}\rho\_{ij}s\_{i}s\_{j}\frac{\partial^{2}V}{\partial s\_{i}\partial s\_{j}}+\sum\limits\_{i=1}^{n}(r-q\_{i})s\_{i}\frac{\partial V}{\partial s\_{i}}-rV. |  |

Then the value of a multi-asset American put option on the geometric mean of nn underlying assets V=V​(s1,⋯,sn)V=V(s\_{1},\cdots,s\_{n}) satisfies the following BSM equations,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | V​(s1,⋯,sn,t)≥(K−I)+,∀si≥0,t∈[0,T),\displaystyle\quad V(s\_{1},\cdots,s\_{n},t)\geq(K-I)^{+},\quad\forall s\_{i}\geq 0,t\in[0,T), |  |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ℱ​(V​(s1,⋯,sn,t))≤0,∀si≥0,t∈[0,T),\displaystyle\quad\mathcal{F}(V(s\_{1},\cdots,s\_{n},t))\leq 0,\quad\forall s\_{i}\geq 0,t\in[0,T), |  |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ℱ​(V​(s1,⋯,sn,t))⋅(V−(K−I)+)=0,∀si≥0,t∈[0,T),\displaystyle\quad\mathcal{F}(V(s\_{1},\cdots,s\_{n},t))\cdot\big(V-(K-I)^{+}\big)=0,\quad\forall s\_{i}\geq 0,t\in[0,T),\quad |  |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | V​(s1,⋯,sn,T)=(K−I)+,∀si≥0.\displaystyle\quad V(s\_{1},\cdots,s\_{n},T)=(K-I)^{+},\quad\forall s\_{i}\geq 0. |  |  |

The geometric average ItI\_{t} of nn geometric Brownian motion processes {Si}i=1n\{S\_{i}\}\_{i=1}^{n} is itself a geometric Brownian motion [[48](https://arxiv.org/html/2510.27132v1#bib.bib48)]. From the high-dimensional Ito^\hat{\text{o}}’s lemma, the dynamics of
II can be expressed as

|  |  |  |
| --- | --- | --- |
|  | d​I=∑i=1n∂I∂si​d​Si+12​∑i,j=1n∂2I∂si​∂sj​d​Si​d​Sj.dI=\sum\limits\_{i=1}^{n}\frac{\partial I}{\partial s\_{i}}dS\_{i}+\frac{1}{2}\sum\limits\_{i,j=1}^{n}\frac{\partial^{2}I}{\partial s\_{i}\partial s\_{j}}dS\_{i}dS\_{j}. |  |

Substituting into the dynamics of sis\_{i} in Eq. ([6](https://arxiv.org/html/2510.27132v1#S2.E6 "In 2.1.4 High-Dimensional BSM Equations for Multi-Asset Options ‣ 2.1 BSM Equations for Option Pricing ‣ 2 Preliminaries ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations")) and ([7](https://arxiv.org/html/2510.27132v1#S2.E7 "In 2.1.4 High-Dimensional BSM Equations for Multi-Asset Options ‣ 2.1 BSM Equations for Option Pricing ‣ 2 Preliminaries ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations")) yields

|  |  |  |
| --- | --- | --- |
|  | d​I=∑i=1n∂I∂si​[(r−qi)​Si+σi​Si​d​Wi]+12​∑i,j=1n∂2I∂si​∂sj​ρi​j​σi​σj​d​t.dI=\sum\limits\_{i=1}^{n}\frac{\partial I}{\partial s\_{i}}\left[(r-q\_{i})S\_{i}+\sigma\_{i}S\_{i}dW\_{i}\right]+\frac{1}{2}\sum\limits\_{i,j=1}^{n}\frac{\partial^{2}I}{\partial s\_{i}\partial s\_{j}}\rho\_{ij}\sigma\_{i}\sigma\_{j}dt. |  |

The first and second partial derivatives of
II are calculated as

|  |  |  |
| --- | --- | --- |
|  | ∂I∂si=In​Si,∂2I∂si​∂sj={1n2​ISi​Sjif​i≠j,1n​(1n−1)​ISi2if​i=j.\frac{\partial I}{\partial s\_{i}}=\frac{I}{nS\_{i}},\quad\frac{\partial^{2}I}{\partial s\_{i}\partial s\_{j}}=\begin{cases}\frac{1}{n^{2}}\frac{I}{S\_{i}S\_{j}}&\text{if}\ i\neq j,\\ \frac{1}{n}(\frac{1}{n}-1)\frac{I}{S\_{i}^{2}}&\text{if}\ i=j.\end{cases} |  |

Substituting these expressions into the dynamics of II, the simplified expression becomes

|  |  |  |
| --- | --- | --- |
|  | d​I​(t)=[1n​∑i=1n(r−qi−12​σi2)+12​n2​∑i,j=1nρi​j​σi​σj]​I​(t)​d​t+1n​∑i=1nσi​I​(t)​d​Wi.dI(t)=\left[\frac{1}{n}\sum\limits\_{i=1}^{n}(r-q\_{i}-\frac{1}{2}\sigma\_{i}^{2})+\frac{1}{2n^{2}}\sum\limits\_{i,j=1}^{n}\rho\_{ij}\sigma\_{i}\sigma\_{j}\right]I(t)dt+\frac{1}{n}\sum\limits\_{i=1}^{n}\sigma\_{i}I(t)dW\_{i}. |  |

To further simplify, the following definitions are introduced,

|  |  |  |
| --- | --- | --- |
|  | σI2=1n2​∑i,j=1nρi​j​σi​σj,qI=1n​∑i=1n(qi+12​σi2)−12​σI2,W=1n​σI​∑i=1nσi​Wi.\sigma\_{I}^{2}=\frac{1}{n^{2}}\sum\limits\_{i,j=1}^{n}\rho\_{ij}\sigma\_{i}\sigma\_{j},\quad q\_{I}=\frac{1}{n}\sum\limits\_{i=1}^{n}(q\_{i}+\frac{1}{2}\sigma\_{i}^{2})-\frac{1}{2}\sigma\_{I}^{2},\quad W=\frac{1}{n\sigma\_{I}}\sum\limits\_{i=1}^{n}\sigma\_{i}W\_{i}. |  |

With these definitions, the dynamics of I​(t)I(t) reduce to

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​I​(t)=(r−qI)​I​(t)​d​t+σI​I​(t)​d​W.dI(t)=(r-q\_{I})I(t)dt+\sigma\_{I}I(t)dW. |  | (19) |

Note that

|  |  |  |
| --- | --- | --- |
|  | d​W​d​W=1n2​σI2​∑i,j=1nσi​σj​d​Wi​d​Wj=1n2​σI2​∑i,j=1nσi​σj​ρi​j​d​t=d​tdWdW=\frac{1}{n^{2}\sigma\_{I}^{2}}\sum\limits\_{i,j=1}^{n}\sigma\_{i}\sigma\_{j}dW\_{i}dW\_{j}=\frac{1}{n^{2}\sigma\_{I}^{2}}\sum\limits\_{i,j=1}^{n}\sigma\_{i}\sigma\_{j}\rho\_{ij}dt=dt |  |

By Le´\acute{\text{e}}vy’s Characterization Theorem of Brownian Motion [[36](https://arxiv.org/html/2510.27132v1#bib.bib36)], the quadratic variation of WW is tt, then WW is a standard Brownian motion. Thus, from Eq. ([19](https://arxiv.org/html/2510.27132v1#S4.E19 "In 4.3 Multi-Asset Options with Geometric Average Payoffs ‣ 4 Numerical Results for American Options ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations")), ItI\_{t} is a geometric Brownian motion process. This enables us to use the binomial tree method to solve a one-dimensional option pricing problem with dividend qIq\_{I} and volatility σI\sigma\_{I} as an accurate approximation of the exact solution, and can be used as a benchmark to evaluate the accuracy of our methods.

The method for constructing g2g\_{2} here is still to perform a first-order Taylor expansion on its European analytical solution. Take

|  |  |  |
| --- | --- | --- |
|  | d0=−1σI​τ​(ln⁡IK+(r−qI)​τ).d\_{0}=-\frac{1}{\sigma\_{I}\sqrt{\tau}}\big(\ln{\frac{I}{K}}+(r-q\_{I})\tau\big). |  |

Then the expression of g2g\_{2} is

|  |  |  |
| --- | --- | --- |
|  | g2​(s1,⋯,sn,t)=N​(d0)​[K​e−r​τ−I​e−qI​τ]+σI​τ2​2​π​e−d022⋅(K​e−r​τ+I)g\_{2}(s\_{1},\cdots,s\_{n},t)=N(d\_{0})[Ke^{-r\tau}-Ie^{-q\_{I}\tau}]+\frac{\sigma\_{I}\sqrt{\tau}}{2\sqrt{2\pi}}e^{-\frac{d\_{0}^{2}}{2}}\cdot(Ke^{-r\tau}+I) |  |

Such g2g\_{2} exactly satisfies the terminal condition. We take g1​(s1,⋯,sn,t)=T−tg\_{1}(s\_{1},\cdots,s\_{n},t)=T-t in our ETCNN.

The experiment considers cases with n=2,3,4,5n=2,3,4,5 underlying assets, using the parameters K=100,T=1,r=0.05K=100,T=1,r=0.05. For the case of n=5n=5 assets, we arbitrarily assign parameter values as follows,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d\displaystyle d | =[0.02,0.03,0.04,0.05,0.03],\displaystyle=[0.02,0.03,0.04,0.05,0.03], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | σ\displaystyle\sigma | =[0.15,0.2,0.25,0.3,0.22],\displaystyle=[0.15,0.2,0.25,0.3,0.22], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ\displaystyle\rho | =(10.20.30.10.40.210.250.150.30.30.2510.20.230.10.150.210.260.40.30.230.261).\displaystyle=\begin{pmatrix}1&0.2&0.3&0.1&0.4\\ 0.2&1&0.25&0.15&0.3\\ 0.3&0.25&1&0.2&0.23\\ 0.1&0.15&0.2&1&0.26\\ 0.4&0.3&0.23&0.26&1\end{pmatrix}. |  |

Here, dd denotes the dividend rates. The dividend rate of sis\_{i} is did\_{i}, the ii-th element of dd. σ\sigma denotes the volatility, where σi\sigma\_{i} is the volatility of sis\_{i}. The correlation matrix ρ\rho specifies the correlations between the assets, where ρi​j\rho\_{ij} is the correlation between sis\_{i} and sjs\_{j}. For scenarios with n=2,3,4n=2,3,4, the dividend rates, volatilities, and correlation matrices are derived by taking the first nn elements of dd and σ\sigma, along with the n×nn\times n submatrix from the upper-left corner of ρ\rho.
Input normalization is applied to both PINN and ETCNN. For n=2,3n=2,3, the number of sampling points for ℒt​c\mathcal{L}\_{tc} are set to Nt​c=8192N\_{tc}=8192. For n=4,5n=4,5, the number of sampling points is increased to Nt​c=16384N\_{tc}=16384 to accommodate the higher input dimensionality. For the other three loss terms, the sampling points are set to Nb​s=Nt​v=Ne​q=4​Nt​cN\_{bs}=N\_{tv}=N\_{eq}=4N\_{tc}.
Training is performed on the range [0,400]n×[0,T][0,400]^{n}\times[0,T], while accuracy is evaluated on the interval [80,120]n×[0,T][80,120]^{n}\times[0,T]. The results of the experiments are summarized in Table [8](https://arxiv.org/html/2510.27132v1#S4.T8 "Table 8 ‣ 4.3 Multi-Asset Options with Geometric Average Payoffs ‣ 4 Numerical Results for American Options ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations").

Table 8: Relative L2L^{2} error and MAE for options on geometric average of nn assets. The input of networks in PINN and ETCNN has n+1n+1 dimensions. Both PINN and ETCNN apply the input normalization layer.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Method | Error | n=2n=2 | n=3n=3 | n=4n=4 | n=5n=5 |
| PINN | Rel. L2L^{2} error | 2.00×10−22.00\times 10^{-2} | 2.79×10−22.79\times 10^{-2} | 1.48×10−11.48\times 10^{-1} | 1.72×10−11.72\times 10^{-1} |
| MAE | 7.75×10−17.75\times 10^{-1} | 1.15×1001.15\times 10^{0} | 2.53×1002.53\times 10^{0} | 2.02×1002.02\times 10^{0} |
| ETCNN | Rel. L2L^{2} error | 1.53×10−31.53\times 10^{-3} | 1.69×10−31.69\times 10^{-3} | 1.07×10−31.07\times 10^{-3} | 1.24×10−31.24\times 10^{-3} |
| MAE | 2.49×10−22.49\times 10^{-2} | 2.45×10−22.45\times 10^{-2} | 3.35×10−23.35\times 10^{-2} | 2.18×10−22.18\times 10^{-2} |

The experimental results indicate that ETCNN significantly outperforms PINN in both relative L2L^{2} error and MAE, achieving improvements of 1–2 orders of magnitude. This performance advantage becomes increasingly evident as the input dimensionality grows.
The performance of PINN deteriorates significantly as the dimensionality of the input space increases. When the number of underlying assets reaches 4 or more (i.e., when the input dimensionality exceeds 5), the error rates for PINN often exceed
10−110^{-1}, which is not applicable in practice. In contrast, ETCNN demonstrates remarkable robustness to the dimensionality increase, maintaining an accuracy level of approximately 10−310^{-3} even in high-dimensional scenarios. This stability and precision suggest that ETCNN is sufficiently accurate to be applied in real-world option pricing tasks.

### 4.4 Call-on-Max American Options

In this example, we study call-on-max options.
Let

|  |  |  |
| --- | --- | --- |
|  | ℱ​(V​(s1,⋯,sn,t))=∂V∂t+12​∑i,j=1nσi​σj​ρi​j​si​sj​∂2V∂si​∂sj+∑i=1n(r−qi)​si​∂V∂si−r​V.\mathcal{F}(V(s\_{1},\cdots,s\_{n},t))=\frac{\partial V}{\partial t}+\frac{1}{2}\sum\limits\_{i,j=1}^{n}\sigma\_{i}\sigma\_{j}\rho\_{ij}s\_{i}s\_{j}\frac{\partial^{2}V}{\partial s\_{i}\partial s\_{j}}+\sum\limits\_{i=1}^{n}(r-q\_{i})s\_{i}\frac{\partial V}{\partial s\_{i}}-rV. |  |

The value of the American call option on the maximum value of nn underlying assets satisfies the following BSM equations,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | V​(s1,⋯,sn,t)≥(max⁡(s1,⋯,sn)−K)+,∀si≥0,t∈[0,T),\displaystyle\quad V(s\_{1},\cdots,s\_{n},t)\geq(\max(s\_{1},\cdots,s\_{n})-K)^{+},\quad\forall s\_{i}\geq 0,t\in[0,T), |  |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ℱ​(V​(s1,⋯,sn,t))≤0,∀si≥0,t∈[0,T),\displaystyle\quad\mathcal{F}(V(s\_{1},\cdots,s\_{n},t))\leq 0,\quad\forall s\_{i}\geq 0,t\in[0,T), |  |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ℱ​(V​(s1,⋯,sn,t))⋅(V−(max⁡(s1,⋯,sn)−K)+)=0,∀si≥0,t∈[0,T),\displaystyle\quad\mathcal{F}(V(s\_{1},\cdots,s\_{n},t))\cdot\big(V-(\max(s\_{1},\cdots,s\_{n})-K)^{+}\big)=0,\quad\forall s\_{i}\geq 0,t\in[0,T),\quad |  |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | V​(s1,⋯,sn,T)=(max⁡(s1,⋯,sn)−K)+,∀si≥0.\displaystyle\quad V(s\_{1},\cdots,s\_{n},T)=(\max(s\_{1},\cdots,s\_{n})-K)^{+},\quad\forall s\_{i}\geq 0. |  |  |

This option is of research significance for two reasons. First, options on the maximum of two or more asset prices are widely used in practice. Examples include corporate bonds and managerial contracts with warrants [[23](https://arxiv.org/html/2510.27132v1#bib.bib23), [11](https://arxiv.org/html/2510.27132v1#bib.bib11)]. Second, the price of call-on-max options can be used to determine the prices of other related options, such as call-on-min, put-on-max, and put-on-min options [[25](https://arxiv.org/html/2510.27132v1#bib.bib25)].

This section analyzes the American call option on the maximum of two assets, setting the strike price K=100K=100 and maturity T=1T=1.
To demonstrate the universality and robustness of our method, we consider four market scenarios: low-volatility low-dividend, low-volatility high-dividend, high-volatility low-dividend, and high-volatility high-dividend. The dividend level here is relative to the risk-free rate rr. For each scenario, we provide a representative example, with parameters specified as follows.

Table 9: Parameters for examples in each scenario.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Number | Description | σ1\sigma\_{1} | σ2\sigma\_{2} | ρ\rho | q1q\_{1} | q2q\_{2} | rr |
| Scenario 1 | low-volatility low-dividend | 0.150.15 | 0.250.25 | 0.20.2 | 0.020.02 | 0.040.04 | 0.060.06 |
| Scenario 2 | low-volatility high-dividend | 0.150.15 | 0.250.25 | 0.20.2 | 0.030.03 | 0.060.06 | 0.020.02 |
| Scenario 3 | high-volatility low-dividend | 0.40.4 | 0.30.3 | 0.20.2 | 0.020.02 | 0.040.04 | 0.060.06 |
| Scenario 4 | high-volatility high-dividend | 0.40.4 | 0.30.3 | 0.20.2 | 0.030.03 | 0.060.06 | 0.020.02 |

#### 4.4.1 Exact Terminal Function Design

This section explores the properties of the above differential equations and designs an exact terminal function g2g\_{2}. It also illustrates the stopping region and provides the representation of the early exercise premium for call-on-max options [[23](https://arxiv.org/html/2510.27132v1#bib.bib23), [11](https://arxiv.org/html/2510.27132v1#bib.bib11)].
Let the value of the option be V=V​(s1,s2,t)V=V(s\_{1},s\_{2},t). The payoff function is Φ​(s1,s2)=(max⁡(s1,s2)−K)+.\Phi(s\_{1},s\_{2})=(\max(s\_{1},s\_{2})-K)^{+}. The stopping region is the set

|  |  |  |
| --- | --- | --- |
|  | 𝒮={(s1,s2,t):V​(s1,s2,t)=(max⁡(s1,s2)−K)+}\mathcal{S}=\{(s\_{1},s\_{2},t):V(s\_{1},s\_{2},t)=(\max(s\_{1},s\_{2})-K)^{+}\} |  |

of price-date points on which the value of the options equals the immediate exercise payoff. The continuation region is defined as the complementary region of 𝒮\mathcal{S}, i.e.

|  |  |  |
| --- | --- | --- |
|  | 𝒞={V​(s1,s2,t):V​(s1,s2,t)>(max⁡(s1,s2)−K)+}.\mathcal{C}=\{V(s\_{1},s\_{2},t):V(s\_{1},s\_{2},t)>(\max(s\_{1},s\_{2})-K)^{+}\}. |  |

Let 𝒢i={(s1,s2,t):si=max⁡(s1,s2)}\mathcal{G}\_{i}=\{(s\_{1},s\_{2},t):s\_{i}=\max(s\_{1},s\_{2})\}. The subregion 𝒮i=𝒮∩𝒢i\mathcal{S}\_{i}=\mathcal{S}\cap\mathcal{G}\_{i} is the subset of 𝒮\mathcal{S} where asset ii is more expensive. The tt-section, defined as 𝒮​(t)={(s1,s2):(s1,s2,t)∈𝒮}\mathcal{S}(t)=\{(s\_{1},s\_{2}):(s\_{1},s\_{2},t)\in\mathcal{S}\} is the set of price pairs (s1,s2)(s\_{1},s\_{2}) in the stopping region at the fixed time tt. Similarly define 𝒮i​(t)={(s1,s2):(s1,s2,t)∈𝒮i}\mathcal{S}\_{i}(t)=\{(s\_{1},s\_{2}):(s\_{1},s\_{2},t)\in\mathcal{S}\_{i}\}. Based on these definitions, we can finally define the free boundary functions of multi-asset options,

|  |  |  |
| --- | --- | --- |
|  | S1∗​(s2,t)=inf{s1∈ℝ+:(s1,s2)∈𝒮1​(t)},\displaystyle S\_{1}^{\*}(s\_{2},t)=\inf\{s\_{1}\in\mathbb{R}^{+}:(s\_{1},s\_{2})\in\mathcal{S}\_{1}(t)\}, |  |
|  |  |  |
| --- | --- | --- |
|  | S2∗​(s1,t)=inf{s2∈ℝ+:(s1,s2)∈𝒮2​(t)}.\displaystyle S\_{2}^{\*}(s\_{1},t)=\inf\{s\_{2}\in\mathbb{R}^{+}:(s\_{1},s\_{2})\in\mathcal{S}\_{2}(t)\}. |  |

These two functions represent the boundary of the tt-sections 𝒮1​(t)\mathcal{S}\_{1}(t) and 𝒮2​(t)\mathcal{S}\_{2}(t) respectively. Then the value of an American option on the maximum of two assets has the early exercise premium representation

|  |  |  |
| --- | --- | --- |
|  | Va​(s1,s2,t)=Ve​(s1,s2,t)+p​(s1,s2,t),V^{a}(s\_{1},s\_{2},t)=V^{e}(s\_{1},s\_{2},t)+p(s\_{1},s\_{2},t), |  |

where the premium function p​(s1,s2,t)p(s\_{1},s\_{2},t) has two components,

|  |  |  |  |
| --- | --- | --- | --- |
|  | p​(s1,s2,t)\displaystyle p(s\_{1},s\_{2},t) | =p1​(s1,s2,t;S1∗)+p2​(s1,s2,t;S2∗),\displaystyle=p\_{1}(s\_{1},s\_{2},t;S\_{1}^{\*})+p\_{2}(s\_{1},s\_{2},t;S\_{2}^{\*}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | p1​(s1,s2,t;S1∗)\displaystyle p\_{1}(s\_{1},s\_{2},t;S\_{1}^{\*}) | =𝐄t,s​∫tTe−r​(u−t)​(d1​s1​(u)−r​K)​I​{s1≤S1∗​(s2,t)}​𝑑u,\displaystyle=\mathbf{E}\_{t,s}\int\_{t}^{T}e^{-r(u-t)}(d\_{1}s\_{1}(u)-rK)\textit{I}\{s\_{1}\leq S\_{1}^{\*}(s\_{2},t)\}du, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | p2​(s1,s2,t;S2∗)\displaystyle p\_{2}(s\_{1},s\_{2},t;S\_{2}^{\*}) | =𝐄t,s​∫tTe−r​(u−t)​(d2​s2​(u)−r​K)​I​{s2≤S2∗​(s1,t)}​𝑑u.\displaystyle=\mathbf{E}\_{t,s}\int\_{t}^{T}e^{-r(u-t)}(d\_{2}s\_{2}(u)-rK)\textit{I}\{s\_{2}\leq S\_{2}^{\*}(s\_{1},t)\}du. |  |

pi​(s1,s2,t;Si∗)p\_{i}(s\_{1},s\_{2},t;S\_{i}^{\*}) is defined for the continuous surface Si∗S^{\*}\_{i}. The free boundaries S1∗S^{\*}\_{1} and S2∗S^{\*}\_{2} are the solutions to the system of recursive integral equations,

|  |  |  |  |
| --- | --- | --- | --- |
|  | S1∗​(s2,t)−K\displaystyle S\_{1}^{\*}(s\_{2},t)-K | =Va​(S1∗​(s2,t),s2,t)\displaystyle=V^{a}(S\_{1}^{\*}(s\_{2},t),s\_{2},t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Ve​(S1∗​(s2,t),s2,t)+p1​(S1∗​(s2,t),s2,t;S1∗)+p2​(S1∗​(s2,t),s2,t;S2∗),\displaystyle=V^{e}(S\_{1}^{\*}(s\_{2},t),s\_{2},t)+p\_{1}(S\_{1}^{\*}(s\_{2},t),s\_{2},t;S\_{1}^{\*})+p\_{2}(S\_{1}^{\*}(s\_{2},t),s\_{2},t;S\_{2}^{\*}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | S2∗​(s1,t)−K\displaystyle S\_{2}^{\*}(s\_{1},t)-K | =Va​(s1,S2∗​(s1,t),t)\displaystyle=V^{a}(s\_{1},S\_{2}^{\*}(s\_{1},t),t) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Ve​(s1,S2∗​(s1,t),t)+p1​(s1,S2∗​(s1,t),t;S1∗)+p2​(s1,S2∗​(s1,t),t;S2∗),\displaystyle=V^{e}(s\_{1},S\_{2}^{\*}(s\_{1},t),t)+p\_{1}(s\_{1},S\_{2}^{\*}(s\_{1},t),t;S\_{1}^{\*})+p\_{2}(s\_{1},S\_{2}^{\*}(s\_{1},t),t;S\_{2}^{\*}), |  |

Therefore, Va​(s1,s2,t),S1∗​(s2,t)V^{a}(s\_{1},s\_{2},t),S\_{1}^{\*}(s\_{2},t) and S2∗​(s1,t)S\_{2}^{\*}(s\_{1},t) form a coupled system of equations, which includes integration and expectation calculation. This makes it very difficult to solve Va​(s1,s2,t)V^{a}(s\_{1},s\_{2},t) and find the free boundaries.

Ve​(s1,s2,t)V^{e}(s\_{1},s\_{2},t) is the value of the counterpart European option. Johnson [[12](https://arxiv.org/html/2510.27132v1#bib.bib12)] and Stulz [[25](https://arxiv.org/html/2510.27132v1#bib.bib25)] give the analytical formulas for the European call options on the maximum of two asset prices without dividends. Here, we derive the analytical formula for European call-on-max options with dividends.
Consider the following notations,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d1​(si,σ;K,τ)\displaystyle d\_{1}(s\_{i},\sigma;K,\tau) | =1σ​τ[ln(siK)+(r−qi+12σ2)τ)],i=1,2,\displaystyle=\frac{1}{\sigma\sqrt{\tau}}\Big[\ln(\frac{s\_{i}}{K})+(r-q\_{i}+\frac{1}{2}\sigma^{2})\tau)\Big],\quad i=1,2, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d2​(si,σ;K,τ)\displaystyle d\_{2}(s\_{i},\sigma;K,\tau) | =1σ​τ[ln(siK)+(r−qi−12σ2)τ)],i=1,2,\displaystyle=\frac{1}{\sigma\sqrt{\tau}}\Big[\ln(\frac{s\_{i}}{K})+(r-q\_{i}-\frac{1}{2}\sigma^{2})\tau)\Big],\quad i=1,2, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d1′​(si,sj,σ;τ)\displaystyle d\_{1}^{\prime}(s\_{i},s\_{j},\sigma;\tau) | =1σ​τ[ln(sisj)+(qj−qi+12σ2)τ)],i,j=1,2,\displaystyle=\frac{1}{\sigma\sqrt{\tau}}\Big[\ln(\frac{s\_{i}}{s\_{j}})+(q\_{j}-q\_{i}+\frac{1}{2}\sigma^{2})\tau)\Big],\quad i,j=1,2, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d2′​(si,sj,σ;τ)\displaystyle d\_{2}^{\prime}(s\_{i},s\_{j},\sigma;\tau) | =1σ​τ[ln(sisj)+(qj−qi−12σ2)τ)],i,j=1,2.\displaystyle=\frac{1}{\sigma\sqrt{\tau}}\Big[\ln(\frac{s\_{i}}{s\_{j}})+(q\_{j}-q\_{i}-\frac{1}{2}\sigma^{2})\tau)\Big],\quad i,j=1,2. |  |

The parameters involved in this derivation include

|  |  |  |
| --- | --- | --- |
|  | σ122=σ12−2​ρ​σ1​σ2+σ22,ρ1=σ1−ρ​σ2σ12,ρ2=σ2−ρ​σ1σ12.\displaystyle\sigma\_{12}^{2}=\sigma\_{1}^{2}-2\rho\sigma\_{1}\sigma\_{2}+\sigma\_{2}^{2},\quad\rho\_{1}=\frac{\sigma\_{1}-\rho\sigma\_{2}}{\sigma\_{12}},\quad\rho\_{2}=\frac{\sigma\_{2}-\rho\sigma\_{1}}{\sigma\_{12}}. |  |

With τ=T−t\tau=T-t denoting the time to maturity, the analytical formula for European call-on-max options with dividends is as follows,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ve​(s1,s2,t)\displaystyle V^{e}(s\_{1},s\_{2},t) | =s1​e−q1​τ​N2​(d1​(s1,σ1;K,τ),d1′​(s1,s2,σ12;τ),ρ1)\displaystyle=s\_{1}e^{-q\_{1}\tau}N\_{2}(d\_{1}(s\_{1},\sigma\_{1};K,\tau),d\_{1}^{\prime}(s\_{1},s\_{2},\sigma\_{12};\tau),\rho\_{1}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +s2​e−q2​τ​N2​(d1​(s2,σ2;K,τ),d1′​(s2,s1,σ12;τ),ρ2)\displaystyle+s\_{2}e^{-q\_{2}\tau}N\_{2}(d\_{1}(s\_{2},\sigma\_{2};K,\tau),d\_{1}^{\prime}(s\_{2},s\_{1},\sigma\_{12};\tau),\rho\_{2}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −K​e−r​τ​[1−N2​(−d2​(s1,σ1;K,τ),−d2​(s2,σ2;K,τ),ρ)].\displaystyle-Ke^{-r\tau}\big[1-N\_{2}(-d\_{2}(s\_{1},\sigma\_{1};K,\tau),-d\_{2}(s\_{2},\sigma\_{2};K,\tau),\rho)\big]. |  |

Here N2​(x,y,ρ)N\_{2}(x,y,\rho) is the cumulative distribution function of the bivariate standard normal distribution. Note that Ve​(s1,s2,t)V^{e}(s\_{1},s\_{2},t) satisfies the same terminal conditions as Va​(s1,s2,t)V^{a}(s\_{1},s\_{2},t). Since it has a complex form, it is difficult to find a d0d\_{0} like in the single-asset case. Therefore we choose g2​(s1,s2,t)=Ve​(s1,s2,t)g\_{2}(s\_{1},s\_{2},t)=V^{e}(s\_{1},s\_{2},t) in this experiment. The definition of g1g\_{1} is still g1​(s1,s2,t)=T−tg\_{1}(s\_{1},s\_{2},t)=T-t.

Calculating Ve​(s1,s2,t)V^{e}(s\_{1},s\_{2},t) is time-expensive due to the double integrals involved in the bivariate normal distribution. Moreover, when calculating the loss function, its derivatives are involved, which are more complicated.
To accelerate the training process, we implement the following two techniques.
First, we employ the method proposed in [[50](https://arxiv.org/html/2510.27132v1#bib.bib50), [51](https://arxiv.org/html/2510.27132v1#bib.bib51)] to numerically approximate the bivariate normal distribution. Gauss-Legendre integration rule and Taylor expansion approximation are used here.
The error caused by using the approximation here is greatly smaller than the errors elsewhere. Therefore, it would not affect the accuracy.
Second, given that ℱ​(Va)≤0,ℱ​(Ve)=0\mathcal{F}(V^{a})\leq 0,\mathcal{F}(V^{e})=0, if the network prediction g1​uN​N+g2g\_{1}u\_{NN}+g\_{2} represents the solution of VaV^{a} and g2=Veg\_{2}=V^{e}, then it follows that ℱ​(g1​uN​N)≤0\mathcal{F}(g\_{1}u\_{NN})\leq 0. Therefore in the loss term ℒb​s\mathcal{L}\_{bs}, we use ℱ​(g1​uN​N)\mathcal{F}(g\_{1}u\_{NN}) instead of using ℱ​(g1​uN​N+g​2)\mathcal{F}(g\_{1}u\_{NN}+g2), as ℱ​(g2)=0\mathcal{F}(g\_{2})=0 is automatically satisfied. This approach removes the need to differentiate g2g\_{2}, thereby saving computation time.

![Refer to caption](Maxcall_Early_exercise_boundary_for_PINN_and_ECTNN.png)
  


Figure 8: Illustration of stopping regions and continuation region for a call-on-max option with σ1=0.1,σ2=0.25,ρ=0.2,d1=0.02,d2=0.04,r=0.06,K=100,T=1\sigma\_{1}=0.1,\sigma\_{2}=0.25,\rho=0.2,d\_{1}=0.02,d\_{2}=0.04,r=0.06,K=100,T=1, at time t=0.75t=0.75 (i.e., this option is three months before maturity). (a)(a), The free boundaries S1∗​(s2,t)S\_{1}^{\*}(s\_{2},t) and S2∗​(s1,t)S\_{2}^{\*}(s\_{1},t) obtained by BT and PINN. (b)(b), The free boundaries S1∗​(s2,t)S\_{1}^{\*}(s\_{2},t) and S2∗​(s1,t)S\_{2}^{\*}(s\_{1},t) obtained by BT and ETCNN.

#### 4.4.2 Numerical Results

The solution obtained by BT with N=400N=400 serves as the reference solution. Here NN is reduced by an order of magnitude compared with the previous cases because the complexity increases exponentially with NN in high-dimensional situations.
The network input consists of three dimensions, s1,s2s\_{1},s\_{2}, and tt, with normalization applied to s1s\_{1} and s2s\_{2}. For the loss calculations, Nt​c=8192N\_{tc}=8192 sampling points are used to compute
ℒt​c\mathcal{L}\_{tc}, while Nb​s=Nt​v=Ne​q=4​Nt​cN\_{bs}=N\_{tv}=N\_{eq}=4N\_{tc} are used for the other three loss terms. The network is trained over the domain [0,400]2×[0,T][0,400]^{2}\times[0,T] with error evaluation performed on [80,150]2×[0,T][80,150]^{2}\times[0,T]. Both PINN and ETCNN are evaluated under four typical market scenarios, with the results summarized in Table [10](https://arxiv.org/html/2510.27132v1#S4.T10 "Table 10 ‣ 4.4.2 Numerical Results ‣ 4.4 Call-on-Max American Options ‣ 4 Numerical Results for American Options ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations").

Table 10: Relative L2L^{2} error and MAE for the four market scenarios. The input of networks for PINN and ETCNN has 3 dimensions. Both PINN and ETCNN implement the input normalization.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Method | Error | Scenario 1 | Scenario 2 | Scenario 3 | Scenario 4 |
| PINN | Rel. L2L^{2} error | 3.18×10−23.18\times 10^{-2} | 3.30×10−23.30\times 10^{-2} | 3.55×10−23.55\times 10^{-2} | 4.53×10−24.53\times 10^{-2} |
| MAE | 1.53×1001.53\times 10^{0} | 1.72×1001.72\times 10^{0} | 2.25×1002.25\times 10^{0} | 2.91×1002.91\times 10^{0} |
| ETCNN | Rel. L2L^{2} error | 1.13×10−41.13\times 10^{-4} | 2.01×10−42.01\times 10^{-4} | 9.84×10−59.84\times 10^{-5} | 2.12×10−42.12\times 10^{-4} |
| MAE | 1.77×10−21.77\times 10^{-2} | 3.53×10−23.53\times 10^{-2} | 2.06×10−22.06\times 10^{-2} | 5.06×10−25.06\times 10^{-2} |

As demonstrated in Table [10](https://arxiv.org/html/2510.27132v1#S4.T10 "Table 10 ‣ 4.4.2 Numerical Results ‣ 4.4 Call-on-Max American Options ‣ 4 Numerical Results for American Options ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations"), our approach has a significant improvement over PINN, reducing the L2L^{2} error by two orders of magnitude and achieving an MAE on the order of 10−210^{-2}. In high-dimensional cases, traditional numerical methods are hard to implement, while PINN is difficult to calculate accurate solutions. However, our ECTNN is easy to implement and can achieve high accuracy. Furthermore, the four market scenarios presented cover a broad range of market conditions, and our method performs well across all scenarios, indicating its robustness and versatility.

Figure [8](https://arxiv.org/html/2510.27132v1#S4.F8 "Figure 8 ‣ 4.4.1 Exact Terminal Function Design ‣ 4.4 Call-on-Max American Options ‣ 4 Numerical Results for American Options ‣ Exact Terminal Condition Neural Network for American Option Pricing Based on the Black-Scholes-Merton Equations") illustrates the free boundaries obtained by PINN and ETCNN for Scenario 1 at t=0.75t=0.75. Since the option has a maturity of T=1T=1, t=0.75t=0.75 means it is 0.250.25 year, or three months before maturity. The free boundaries computed from the reference solution are considered as the true free boundaries.
As shown in it, the free boundaries identified by our ETCNN method align closely with the true ones, while the free boundaries obtained by PINN exhibit obvious deviations, particularly at lower asset prices. This comparison indicates that our method achieves relatively high accuracy in determining complex free boundaries in high-dimensional problems.

## 5 Conclusions

This study introduces the exact terminal condition neural network (ETCNN) framework to solve the Black-Scholes-Merton equation with inequality constraints.
By incorporating exact terminal functions that exactly satisfy terminal conditions and capture the singular behaviors of the true solution, ETCNN effectively reduces approximation complexity and improves accuracy compared to other neural network-based methods.
The proposed approach has been tested across a variety of scenarios, including both single-asset and multi-asset cases with different parameters.
Numerical results further demonstrate that ETCNN consistently outperforms both traditional approaches and other neural network methods in terms of accuracy, while maintaining computational efficiency.

Despite these promising results, several directions for future research remain.
Future studies could explore extending this approach to options with more complex terminal conditions, such as Asian options, barrier options, and other exotic derivatives.
Moreover, the framework could be adapted to more advanced models, such as local volatility models and stochastic volatility models, which present additional mathematical and computational challenges.
Addressing these challenges could significantly expand the scope and applicability of the ETCNN framework in financial modeling.

## Acknowledgments

The authors sincerely appreciate the anonymous reviewers for their valuable comments and suggestions, which significantly enhance the quality and clarity of this work.
The work of Lu and Zhang was funded by the Strategic Priority Research Program of Chinese Academy of Sciences (Grant No. XDB0500000)
and the National Natural Science Foundation of China (Grant No. 12371413, No. 22073110).
The work of Guo was supported by the National Natural Science Foundation of China (Grant No. 12371438).
The AI-driven experiments, simulations and model training were performed on the GPU computing platform of the Academy of Mathematics and Systems Science, Chinese Academy of Sciences
and the robotic AI-Scientist platform of Chinese Academy of Sciences.

## References

* [1]

  M. Raissi, P. Perdikaris, G. Karniadakis, Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations, Journal of Computational Physics 378 (2019) 686–707.
* [2]

  J. Berg, K. Nyström, A unified deep artificial neural network approach to partial differential equations in complex geometries, Neurocomputing 317 (2018) 28–41.
* [3]

  D. P. Kingma, J. Ba, Adam: A method for stochastic optimization, arXiv preprint arXiv:1412.6980 (2014).
* [4]

  G. Barone-Adesi, R. E. Whaley, Efficient analytic approximation of american option values, The Journal of Finance 42 (2) (1987) 301–320.
* [5]

  A. Conze, Viswanathan, Path dependent options: The case of lookback options, The Journal of Finance 46 (5) (1991) 1893–1907.
* [6]

  A. Dhiman, Y. Hu, Physics informed neural network for option pricing, arXiv preprint arXiv:2312.06711 (2023).
* [7]

  J. Han, A. Jentzen, W. E, Solving high-dimensional partial differential equations using deep learning, Proceedings of the National Academy of Sciences 115 (34) (2018) 8505–8510.
* [8]

  B. Negyesi, C. W. Oosterlee, A deep bsde approach for the simultaneous pricing and delta-gamma hedging of large portfolios consisting of high-dimensional multi-asset bermudan options, arXiv preprint arXiv:2502.11706 (2025).
* [9]

  K. Glau, L. Wunderlich, The deep parametric pde method and applications to option pricing, Applied Mathematics and Computation 432 (2022) 127355.
* [10]

  P. Van Moerbeke, On optimal stopping and free boundary problems, Archive for Rational Mechanics and Analysis 60 (2) (1976) 101–148.
* [11]

  J. Detemple, American-style derivatives: Valuation and computation, Chapman and Hall/CRC, 2005.
* [12]

  H. Johnson, Options on the maximum or the minimum of several assets, Journal of Financial and Quantitative Analysis 22 (3) (1987) 277–283.
* [13]

  L. C. Rogers, Monte carlo valuation of american options, Mathematical Finance 12 (3) (2002) 271–286.
* [14]

  R. H. Chan, C.-Y. Wong, K.-M. Yeung, Pricing multi-asset american-style options by memory reduction monte carlo methods, Applied Mathematics and Computation 179 (2) (2006) 535–544.
* [15]

  J. Detemple, S. Feng, W. Tian, The valuation of american call options on the minimum of two dividend-paying assets, The Annals of Applied Probability 13 (3) (2003) 953–983.
* [16]

  G. Peskir, A. Shiriaev, Optimal stopping and free-boundary problems, Birkhäuser Basel, 2006.
* [17]

  W. Margrabe, The value of an option to exchange one asset for another, The Journal of Finance 33 (1) (1978) 177–186.
* [18]

  M. J. Brennan, E. S. Schwartz, The valuation of american put options, The Journal of Finance 32 (2) (1977) 449–462.
* [19]

  R. J. Rendleman, Two-state option pricing, The Journal of Finance 34 (5) (1979) 1093–1110.
* [20]

  L. Trigeorgis, A log-transformed binomial numerical analysis method for valuing complex multi-option investments, Journal of Financial and Quantitative Analysis 26 (3) (1991) 309–326.
* [21]

  J. C. Cox, S. A. Ross, M. Rubinstein, Option pricing: A simplified approach, Journal of Financial Economics 7 (3) (1979) 229–263.
* [22]

  T. Klimsiak, A. Rozkosz, The early exercise premium representation for american options on multiply assets, Applied Mathematics & Optimization 73 (2016) 99–114.
* [23]

  M. Broadie, J. Detemple, The valuation of american options on multiple assets, Mathematical Finance 7 (3) (1997) 241–286.
* [24]

  I. E. Lagaris, A. Likas, D. I. Fotiadis, Artificial neural networks for solving ordinary and partial differential equations, IEEE Transactions on Neural Networks 9 (5) (1998) 987–1000.
* [25]

  R. Stulz, Options on the minimum or the maximum of two risky assets: analysis and applications, Journal of Financial Economics 10 (2) (1982) 161–185.
* [26]

  F. A. Longstaff, E. S. Schwartz, Valuing american options by simulation: a simple least-squares approach, The Review of Financial Studies 14 (1) (2001) 113–147.
* [27]

  F. Black, M. Scholes, The pricing of options and corporate liabilities, Journal of Political Economy 81 (3) (1973) 637–654.
* [28]

  P. P. Boyle, J. Evnine, S. Gibbs, Numerical evaluation of multivariate contingent claims, The Review of Financial Studies 2 (2) (1989) 241–250.
* [29]

  J. M. Harrison, S. R. Pliska, Martingales and stochastic integrals in the theory of continuous trading, Stochastic Processes and their Applications 11 (3) (1981) 215–260.
* [30]

  P. P. Boyle, A lattice framework for option pricing with two state variables, Journal of Financial and Quantitative Analysis 23 (1) (1988) 1–12.
* [31]

  C.-F. Lee, H.-Y. Chen, J. Lee, C.-F. Lee, H.-Y. Chen, J. Lee, The binomial, multinomial distributions, and option pricing model, Financial Econometrics, Mathematics and Statistics: Theory, Method and Application (2019) 357–378.
* [32]

  K.-S. Moon, W.-J. Kim, H. Kim, Adaptive lattice methods for multi-asset models, Computers & Mathematics with Applications 56 (2) (2008) 352–366.
* [33]

  R. C. Merton, Theory of rational option pricing, The Bell Journal of Economics and Management Science (1973) 141–183.
* [34]

  J. B. Cole, Generalized nonstandard finite differences and physical applications, Computers in Physics 12 (1) (1998) 82–87.
* [35]

  M. Broadie, P. Glasserman, Pricing american-style securities using simulation, Journal of Economic Dynamics and Control 21 (8-9) (1997) 1323–1352.
* [36]

  S. Shreve, Stochastic calculus for finance II: Continuous-time models, Springer New York, 2004.
* [37]

  F. Gatta, V. S. Di Cola, F. Giampaolo, F. Piccialli, S. Cuomo, Meshless methods for american option pricing through physics-informed neural networks, Engineering Analysis with Boundary Elements 151 (2023) 68–82.
* [38]

  I. J. Kim, The analytic valuation of american options, The Review of Financial Studies 3 (4) (1990) 547–572.
* [39]

  P. Carr, R. Jarrow, R. Myneni, Alternative characterizations of american put options, Mathematical Finance 2 (2) (1992) 87–106.
* [40]

  Y. Kitapbayev, Closed form optimal exercise boundary of the american put option, International Journal of Theoretical and Applied Finance 24 (01) (2021) 2150004.
* [41]

  K. He, X. Zhang, S. Ren, J. Sun, Deep residual learning for image recognition, in: 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2016, pp. 770–778.
* [42]

  M. Brenner, M. G. Subrahmanyan, A simple formula to compute the implied standard deviation, Financial Analysts Journal 44 (5) (1988) 80–83.
* [43]

  R. Zhang, Q. Zhang, H. Song, An efficient finite element method for pricing american multi-asset put options, Communications in Nonlinear Science and Numerical Simulation 29 (1-3) (2015) 25–36.
* [44]

  M. Bustamante, M. Contreras, Multi-asset black–scholes model as a variable second class constrained dynamical system, Physica A: Statistical Mechanics and its Applications 457 (2016) 540–572.
* [45]

  X. Jin, C.-Y. Yang, Efficient estimation of lower and upper bounds for pricing higher-dimensional american arithmetic average options by approximating their payoff functions, International Review of Financial Analysis 44 (2016) 65–77.
* [46]

  J. Sirignano, K. Spiliopoulos, DGM: A deep learning algorithm for solving partial differential equations, Journal of Computational Physics 375 (2018) 1339–1364.
* [47]

  P. Kovalov, V. Linetsky, M. Marcozzi, Pricing multi-asset american options: A finite element method-of-lines with smooth penalty, Journal of Scientific Computing 33 (3) (2007) 209–237.
* [48]

  T. H. Eytan, G. Harpaz, The pricing of futures and options contracts on the value line index, The Journal of Finance 41 (4) (1986) 843–855.
* [49]

  Y. Guo, P. Ming, A deep learning method for computing eigenvalues of the fractional schrödinger operator, Journal of Systems Science and Complexity 37 (2) (2024) 391–412.
* [50]

  Z. Drezner, G. O. Wesolowsky, On the computation of the bivariate normal integral, Journal of Statistical Computation and Simulation 35 (1-2) (1990) 101–107.
* [51]

  A. Genz, Numerical computation of rectangular bivariate and trivariate normal and t probabilities, Statistics and Computing 14 (2004) 251–260.