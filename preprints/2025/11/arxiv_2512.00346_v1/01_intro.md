---
authors:
- Hiroki Yamamichi
doc_id: arxiv:2512.00346v1
family_id: arxiv:2512.00346
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor
  Models
url_abs: http://arxiv.org/abs/2512.00346v1
url_html: https://arxiv.org/html/2512.00346v1
venue: arXiv q-fin
version: 1
year: 2025
---


Hiroki Yamamichi111Graduate School of Engineering Science, The University of Osaka, 1-3, Machikaneyama, Toyonaka, Osaka, 560-8531, Japan, Email: yamamichi@sigmath.es.osaka-u.ac.jp

###### Abstract

Turnpike theorems state that if an investor’s utility is asymptotically equivalent to a power utility, then the optimal investment strategy converges to the CRRA strategy as the investment horizon tends to infinity. This paper aims to derive the convergence rates of the turnpike theorem for optimal feedback functions in stochastic factor models. In these models, optimal feedback functions can be decomposed into two terms: myopic portfolios and excess hedging demands. We obtain convergence rates for myopic portfolios in nonlinear stochastic factor models and for excess hedging demands in quadratic term structure models, where the interest rate is a quadratic function of a multivariate Ornstein–Uhlenbeck process. We show that the convergence rates are determined by (i) the decay speed of the price of a zero-coupon bond and (ii) how quickly the investor’s utility becomes power-like at high levels of wealth. As an application, we consider optimal collective investment problems and show that sharing rules for terminal wealth affect convergence rates.
  
Keywords: portfolio choice, turnpike property, convergence rate, stochastic opportunity sets, collective utility function.

## 1 Introduction

Since the seminal works of Merton [[30](https://arxiv.org/html/2512.00346v1#bib.bib30), [31](https://arxiv.org/html/2512.00346v1#bib.bib31)], optimal investment problems for continuous-time models have been developed in various directions. In particular, stochastic factor models have been used to capture stochastic investment opportunity sets, such as the predictability of stock returns, stochastic volatility, and stochastic interest rates. For an overview of optimal investment problems with stochastic factor models, we refer the reader to the review paper [[45](https://arxiv.org/html/2512.00346v1#bib.bib45)].
In these models, optimal investment strategies can be decomposed into two terms, namely, myopic portfolios and excess hedging demands. This means that at first investors choose the myopic portfolios as if the investment opportunity sets are constant, then they adjust their portfolios by adding the excess hedging demands to adapt to future changes in the investment environment. Although computing these terms typically requires analyzing fully nonlinear Hamilton–Jacobi–Bellman (HJB) equations, the computations become tractable for homothetic utilities, such as exponential, power, and log utilities. As a result, explicit formulas for optimal investment strategies are typically available for these special utilities. In contrast, it is challenging to analyze optimal investment strategies for generic utilities, and, to the best of our knowledge, only a few works have calculated the optimal strategies, including Detemple and Rindisbacher [[6](https://arxiv.org/html/2512.00346v1#bib.bib6)], Fukaya [[10](https://arxiv.org/html/2512.00346v1#bib.bib10)], Lakner [[26](https://arxiv.org/html/2512.00346v1#bib.bib26)], Ocone and Karatzas [[36](https://arxiv.org/html/2512.00346v1#bib.bib36)], and Putschögl and Sass [[37](https://arxiv.org/html/2512.00346v1#bib.bib37)].

Turnpike theorems fill this gap between power utilities and general utilities. Informally, turnpike theorems state that if a utility function is similar to a power utility at large wealth levels, then both the optimal wealth process and the optimal investment strategy converge to those for a power utility as the investment horizon tends to infinity. This paper aims to derive the convergence rates of turnpike theorems for both myopic portfolios and excess hedging demands in stochastic factor models.

Turnpike theorems originate in the classic work of von Neumann [[35](https://arxiv.org/html/2512.00346v1#bib.bib35)] in economic growth theory. In the context of optimal portfolios, Mossin [[32](https://arxiv.org/html/2512.00346v1#bib.bib32)] first proves portfolio turnpikes in discrete-time settings under the assumption that a utility function U\displaystyle U has affine risk tolerance, that is, −U′​(x)U′′​(x)=a​x+b\displaystyle-\frac{U^{\prime}(x)}{U^{\prime\prime}(x)}=ax+b. Mossin’s results are extended by Leland [[26](https://arxiv.org/html/2512.00346v1#bib.bib26)], Ross [[41](https://arxiv.org/html/2512.00346v1#bib.bib41)], and Hakansson [[14](https://arxiv.org/html/2512.00346v1#bib.bib14)] to include general utility functions. Huberman and Ross [[16](https://arxiv.org/html/2512.00346v1#bib.bib16)] derive a necessary and sufficient condition for the turnpike property. Cox and Huang [[5](https://arxiv.org/html/2512.00346v1#bib.bib5)] prove the first turnpike theorem in continuous-time settings using martingale methods under the assumption that there exist constants A1,A2,b,z∗>0\displaystyle A\_{1},A\_{2},b,z^{\ast}>0 such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |(U′)−1​(z)−A1​z−1b|≤A2​z−a,z∈(0,z∗]\left|(U^{\prime})^{-1}(z)-A\_{1}z^{-\frac{1}{b}}\right|\leq A\_{2}z^{-a},\quad z\in(0,z^{\ast}] |  | (1) |

holds for some a∈[0,1/b)\displaystyle a\in\left[0,1/b\right). Jin [[19](https://arxiv.org/html/2512.00346v1#bib.bib19)] extends their results to include consumption.
Huang and Zariphopoulou [[17](https://arxiv.org/html/2512.00346v1#bib.bib17)] show that the condition

|  |  |  |
| --- | --- | --- |
|  | limx↗∞U′​(x)xγ−1=K\lim\_{x\nearrow\infty}\frac{U^{\prime}(x)}{x^{\gamma-1}}=K |  |

for some K>0\displaystyle K>0, which is weaker than the condition ([1](https://arxiv.org/html/2512.00346v1#S1.E1 "In 1 Introduction ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")), is sufficient for the turnpike property, using viscosity solutions for the associated HJB equations. Dybvig et al. [[9](https://arxiv.org/html/2512.00346v1#bib.bib9)] prove portfolio turnpikes for complete markets in the Brownian filtration without assuming stationary investment opportunity sets. Guasoni et al. [[13](https://arxiv.org/html/2512.00346v1#bib.bib13)] consider general incomplete market models that include one-dimensional stochastic factor models, and they prove three types of turnpikes (abstract, classic, and explicit).

Although it is important to know how fast turnpike theorems hold in practice, the above works do not derive convergence rates. However, Bian and Zheng [[3](https://arxiv.org/html/2512.00346v1#bib.bib3)] first estimate the convergence rate of the turnpike property under the Black–Scholes model. Beyond the classical expected utility framework, Geng and Zariphopoulou [[12](https://arxiv.org/html/2512.00346v1#bib.bib12)] recently studied turnpike-type limiting properties and the convergence rate for the forward relative risk tolerance function under time-monotone forward performance criteria in Ito diffusion markets. Since Geng and Zariphopoulou [[12](https://arxiv.org/html/2512.00346v1#bib.bib12)] focus on the subclass of time-monotone forward utilities, there is still no result on convergence rates for excess hedging demands. In the present paper, we aim to derive convergence rates for both myopic portfolios and excess hedging demands in stochastic factor models.

Our contributions are fourfold. First, we derive convergence rates of turnpike theorems for myopic portfolios with general stochastic factor models in complete markets (Theorem [2.4](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem4 "Theorem 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")), which extends the results of Bian and Zheng [[3](https://arxiv.org/html/2512.00346v1#bib.bib3)] from the Black–Scholes model to more general settings. In particular, we find that the convergence rate is determined by the price of a zero-coupon bond and the rate at which the investor’s utility becomes power-like at high levels of wealth. As made precise in Remark [2.7](https://arxiv.org/html/2512.00346v1#S2.Thmremark7 "Remark 2.7. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), the rate is typically exponential. Moreover, we prove uniform convergence in the wealth variable for portfolio proportions (Theorem [2.5](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem5 "Theorem 2.5. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")), which has not yet been documented. Furthermore, we also derive the convergence rate for the optimal portfolio processes (Theorem [2.6](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem6 "Theorem 2.6. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")).

Second, we also derive convergence rates of turnpike theorems for excess hedging demands with quadratic term structure models (Theorem [2.7](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem7 "Theorem 2.7. ‣ 2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")), where the instantaneous rate is a quadratic function of the stochastic factor process.
To the best of our knowledge, no previous studies have derived the convergence rates for excess hedging demands. We find that the convergence rates are the same as those of myopic portfolios and uniform convergence in wealth holds (Theorem [2.8](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem8 "Theorem 2.8. ‣ 2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")).

Third, by applying our main results, we analyze the turnpike properties of the optimal strategies for optimal collective investment problems. In these problems, there are n\displaystyle n investors who delegate their portfolio management to a fund manager. The fund manager invests on their behalf to optimize the expected social utility, constructed from the individual utilities and a sharing rule, according to which the fund manager allocates the terminal wealth to individuals. We consider two sharing rules: a Pareto-optimal sharing rule and a linear sharing rule. We find that these sharing rules affect convergence rates (Theorems [2.10](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem10 "Theorem 2.10. ‣ 2.4.1 Pareto optimal sharing rule ‣ 2.4 Applications: optimal collective investment problems ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") and [2.12](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem12 "Theorem 2.12. ‣ 2.4.2 Linear sharing rule ‣ 2.4 Applications: optimal collective investment problems ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")). In particular, we show that the convergence rate for a linear sharing rule is faster than for a Pareto-optimal sharing rule when the least risk-averse investor among n\displaystyle n investors is no less risk-averse than the log investor.

Finally, we methodologically provide a probabilistic approach based on martingale duality methods and Malliavin calculus, in contrast to the PDE techniques used in prior work by Bian and Zheng [[3](https://arxiv.org/html/2512.00346v1#bib.bib3)]. When applying Malliavin calculus to optimal investment problems, previous research papers such as [[26](https://arxiv.org/html/2512.00346v1#bib.bib26), [37](https://arxiv.org/html/2512.00346v1#bib.bib37)] often assume conditions that depend on the investment horizon. In the present paper, we assume conditions (Assumptions [2.1](https://arxiv.org/html/2512.00346v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")–[2.3](https://arxiv.org/html/2512.00346v1#S2.Thmassumption3 "Assumption 2.3. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) that are independent of the investment horizon, allowing us to apply Malliavin calculus techniques when the investment horizon tends to infinity.

The rest of this paper is organized as follows. The main results are discussed in Sect. [2](https://arxiv.org/html/2512.00346v1#S2 "2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), which consists of four subsections. In Sect. [2.1](https://arxiv.org/html/2512.00346v1#S2.SS1 "2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), we provide stochastic flow representations of optimal feedback strategies for general utilities. Sect. [2.2](https://arxiv.org/html/2512.00346v1#S2.SS2 "2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") estimates the convergence rate of the turnpike theorem for myopic portfolios with general factor models. Sect. [2.3](https://arxiv.org/html/2512.00346v1#S2.SS3 "2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") estimates the rate for excess hedging demands with quadratic term structure models. In Sect. [2.4](https://arxiv.org/html/2512.00346v1#S2.SS4 "2.4 Applications: optimal collective investment problems ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), we offer applications of our main results to optimal collective investment problems. Sect. [3](https://arxiv.org/html/2512.00346v1#S3 "3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") contains proofs of our main results. The appendix contains short reviews of Malliavin calculus, option pricing theory in stochastic factor models, the relationship between stochastic control methods and martingale duality methods, and the matrix Riccati equation.

## 2 Main results

### 2.1 Stochastic flow representation of optimal feedback functions

Let (Ω,ℱ,ℙ,(ℱt)t∈[0,T])\displaystyle(\Omega,\mathcal{F},\mathbb{P},(\mathcal{F}\_{t})\_{t\in[0,T]}) be a filtered probability space endowed with (ℱt)t∈[0,T]\displaystyle(\mathcal{F}\_{t})\_{t\in[0,T]}, the augmentation of the natural filtration generated by the n\displaystyle n-dimensional Brownian motion W≔(W1,…,Wn)⊤\displaystyle W\coloneqq(W^{1},\dots,W^{n})^{\top}. We consider a financial market with one riskless bond and n\displaystyle n risky assets. The price processes of the riskless bond S0\displaystyle S^{0} and n\displaystyle n risky assets S=(S1,…,Sn)⊤\displaystyle S=(S^{1},\dots,S^{n})^{\top} are modeled as

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | d​St0\displaystyle dS^{0}\_{t} | =St0​r​(Yt)​d​t,\displaystyle=S^{0}\_{t}r(Y\_{t})dt, | S00\displaystyle S^{0}\_{0} | =1,\displaystyle=1, |  | (2) |
|  | d​St\displaystyle dS\_{t} | =diag(St)⁡{μ​(Yt)​d​t+σ​(Yt)​d​Wt},\displaystyle=\operatorname\*{diag}(S\_{t})\{\mu(Y\_{t})dt+\sigma(Y\_{t})dW\_{t}\}, | S0\displaystyle S\_{0} | =s0∈ℝ++n,\displaystyle=s\_{0}\in\mathbb{R}^{n}\_{++}, |  |
|  | d​Yt\displaystyle dY\_{t} | =b​(Yt)​d​t+a​(Yt)​d​Wt,\displaystyle=b(Y\_{t})dt+a(Y\_{t})dW\_{t}, | Y0\displaystyle Y\_{0} | =y∈ℝm,\displaystyle=y\in\mathbb{R}^{m}, |  |

where r:ℝm→ℝ,μ:ℝm→ℝn,σ:ℝm→ℝn×n,b:ℝm→ℝm,a:ℝm→ℝm×n\displaystyle r:\mathbb{R}^{m}\to\mathbb{R},\mu:\mathbb{R}^{m}\to\mathbb{R}^{n},\sigma:\mathbb{R}^{m}\to\mathbb{R}^{n\times n},b:\mathbb{R}^{m}\to\mathbb{R}^{m},a:\mathbb{R}^{m}\to\mathbb{R}^{m\times n} satisfy Assumption [2.1](https://arxiv.org/html/2512.00346v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") below, diag​(x)\displaystyle\mathrm{diag}(x) denotes the diagonal n×n\displaystyle n\times n matrix whose (i,i)\displaystyle(i,i)-th element is component xi\displaystyle x\_{i} of x=(x1,…,xn)⊤∈ℝn\displaystyle x=(x\_{1},\dots,x\_{n})^{\top}\in\mathbb{R}^{n}, and the m\displaystyle m-dimensional process Y=(Y1,…,Ym)⊤\displaystyle Y=(Y^{1},\dots,Y^{m})^{\top} is referred to as the stochastic factor processes, which affect the coefficients of the asset price processes. We denote the market price of risk as θ​(y)≔σ​(y)−1​{μ​(y)−r​(y)​𝟏}\displaystyle\theta(y)\coloneqq\sigma(y)^{-1}\{\mu(y)-r(y)\mathbf{1}\}, where 𝟏=(1,…,1)⊤∈ℝn\displaystyle\mathbf{1}=(1,\dots,1)^{\top}\in\mathbb{R}^{n}. Furthermore, we let β=(βt)t∈[0,T]\displaystyle\beta=(\beta\_{t})\_{t\in[0,T]} be a discounted price process, Z=(Zt)t∈[0,T]\displaystyle Z=(Z\_{t})\_{t\in[0,T]} be a likelihood ratio process, and H=(Ht)t∈[0,T]\displaystyle H=(H\_{t})\_{t\in[0,T]} be a state price density process as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | βt\displaystyle\displaystyle\beta\_{t} | ≔1St0=exp⁡(−∫0tr​(Ys)​𝑑s),\displaystyle\displaystyle\coloneqq\frac{1}{S^{0}\_{t}}=\exp\left(-\int\_{0}^{t}r(Y\_{s})ds\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Zt\displaystyle\displaystyle Z\_{t} | ≔exp⁡{−∫0tθ⊤​(Ys)​𝑑Ws−12​∫0t|θ​(Ys)|2​𝑑s},\displaystyle\displaystyle\coloneqq\exp\left\{-\int\_{0}^{t}\theta^{\top}(Y\_{s})dW\_{s}-\frac{1}{2}\int\_{0}^{t}|\theta(Y\_{s})|^{2}ds\right\}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Ht\displaystyle\displaystyle H\_{t} | ≔βt​Zt.\displaystyle\displaystyle\coloneqq\beta\_{t}Z\_{t}. |  |

We assume some conditions on these coefficient functions.

###### Assumption 2.1.

1. (i)

   All functions r,μ,σ,b,a,θ\displaystyle r,\mu,\sigma,b,a,\theta on ℝm\displaystyle\mathbb{R}^{m} are continuous functions.
2. (ii)

   σ​(y)\displaystyle\sigma(y) is invertible for all y∈ℝm\displaystyle y\in\mathbb{R}^{m}.
3. (iii)

   θ\displaystyle\theta has linear growth.
4. (iv)

   b,a\displaystyle b,a are Lipschitz continuous and a\displaystyle a is bounded.

Under Assumption [2.1](https://arxiv.org/html/2512.00346v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), a local martingale Z\displaystyle Z is a martingale. For the proof, see [[27](https://arxiv.org/html/2512.00346v1#bib.bib27), Section 6.2]. Therefore, we can define a unique equivalent martingale measure ℚ\displaystyle\mathbb{Q} and n\displaystyle n-dimensional ℚ\displaystyle\mathbb{Q}-Brownian motion Wℚ\displaystyle W^{\mathbb{Q}} as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​ℚ|ℱt\displaystyle\displaystyle d\mathbb{Q}|\_{\mathcal{F}\_{t}} | ≔Zt​d​ℙ|ℱt,\displaystyle\displaystyle\coloneqq Z\_{t}d\mathbb{P}|\_{\mathcal{F}\_{t}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Wtℚ\displaystyle\displaystyle W^{\mathbb{\mathbb{Q}}}\_{t} | ≔Wt+∫0tθ​(Ys)​𝑑s.\displaystyle\displaystyle\coloneqq W\_{t}+\int\_{0}^{t}\theta(Y\_{s})ds. |  |

π=(πt)t∈[0,T]\displaystyle\pi=(\pi\_{t})\_{t\in[0,T]} is a portfolio process if π\displaystyle\pi is an n\displaystyle n-dimensional (ℱt)t\displaystyle(\mathcal{F}\_{t})\_{t}-progressively measurable process and satisfies

|  |  |  |
| --- | --- | --- |
|  | ∫0T|πt|2​𝑑t<∞P−a.s.\int\_{0}^{T}|\pi\_{t}|^{2}dt<\infty\quad P-a.s. |  |

For each initial wealth x≥0\displaystyle x\geq 0 and portfolio process π\displaystyle\pi, we define the corresponding wealth process Xx,π=(Xtx,π)t∈[0,T]\displaystyle X^{x,\pi}=(X^{x,\pi}\_{t})\_{t\in[0,T]} as the solution to the following SDE:

|  |  |  |
| --- | --- | --- |
|  | d​Xtx,π=[r​(Yt)​Xtx,π+πt⊤​(μ​(Yt)−r​(Yt)​𝟏)]​d​t+πt⊤​σ​(Yt)​d​Wt,X0=x.dX^{x,\pi}\_{t}=\left[r(Y\_{t})X^{x,\pi}\_{t}+\pi^{\top}\_{t}(\mu(Y\_{t})-r(Y\_{t})\mathbf{1})\right]dt+\pi^{\top}\_{t}\sigma(Y\_{t})dW\_{t},\quad X\_{0}=x. |  |

Given x≥0\displaystyle x\geq 0, we say that a portfolio process π\displaystyle\pi is admissible at x\displaystyle x if the corresponding wealth process Xx,π\displaystyle X^{x,\pi} satisfies

|  |  |  |
| --- | --- | --- |
|  | Xtx,π≥0,t∈[0,T]X^{x,\pi}\_{t}\geq 0,\quad t\in[0,T] |  |

almost surely.

An investor’s risk preference is represented by a utility function U\displaystyle U.

###### Definition 2.1.

We call U:(0,∞)→ℝ\displaystyle U:(0,\infty)\to\mathbb{R} a utility function if U\displaystyle U is strictly increasing, strictly concave, and twice continuously differentiable on (0,∞)\displaystyle(0,\infty) and satisfies the Inada conditions

|  |  |  |
| --- | --- | --- |
|  | limx↘0U′​(x)=∞,limx↗∞U′​(x)=0.\lim\_{x\searrow 0}U^{\prime}(x)=\infty,\quad\lim\_{x\nearrow\infty}U^{\prime}(x)=0. |  |

Let I≔(U′)−1:(0,∞)→(0,∞)\displaystyle I\coloneqq(U^{\prime})^{-1}:(0,\infty)\to(0,\infty) be the inverse marginal utility U′\displaystyle U^{\prime}. By the definition of U\displaystyle U, I\displaystyle I is strictly decreasing and continuously differentiable on (0,∞)\displaystyle(0,\infty) and satisfies

|  |  |  |
| --- | --- | --- |
|  | limz↘0I​(z)=∞,limz↗∞I​(z)=0.\lim\_{z\searrow 0}I(z)=\infty,\quad\lim\_{z\nearrow\infty}I(z)=0. |  |

The investor in this paper desires to maximize their expected utility and find an optimal portfolio process π^\displaystyle\hat{\pi}.
This problem is formulated as follows.

###### Problem 2.2.

Find an optimal π∈𝒜​(x)\displaystyle\pi\in\mathcal{A}(x) for the problem

|  |  |  |
| --- | --- | --- |
|  | supπ∈𝒜​(x)𝔼​[U​(XTx,π)]\sup\_{\pi\in\mathcal{A}(x)}\mathbb{E}\left[U(X^{x,\pi}\_{T})\right] |  |

of maximizing expected utility from terminal wealth, where

|  |  |  |
| --- | --- | --- |
|  | 𝒜​(x)≔{π;π is admissible at x,𝔼​[U​(XTx,π)−]<∞}.\mathcal{A}(x)\coloneqq\left\{\pi;\text{$\displaystyle\pi$ is admissible at $\displaystyle x$},\mathbb{E}\left[U(X^{x,\pi}\_{T})^{-}\right]<\infty\right\}. |  |

To use the martingale method, we assume the following growth conditions.

###### Assumption 2.2.

* (i)

  There exist r0∈ℝ,r1∈ℝm\displaystyle r\_{0}\in\mathbb{R},\;r\_{1}\in\mathbb{R}^{m} such that for every y∈ℝm\displaystyle y\in\mathbb{R}^{m},

  |  |  |  |
  | --- | --- | --- |
  |  | r​(y)≥r0+r1⊤​y.r(y)\geq r\_{0}+r\_{1}^{\top}y. |  |
* (ii)

  There exist κ>0,ρ∈(0,1]\displaystyle\kappa>0,\;\rho\in(0,1] such that for every z>0\displaystyle z>0,

  |  |  |  |
  | --- | --- | --- |
  |  | I​(z)≤κ​(1+z−ρ).I(z)\leq\kappa(1+z^{-\rho}). |  |

Under Assumptions [2.1](https://arxiv.org/html/2512.00346v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") and [2.2](https://arxiv.org/html/2512.00346v1#S2.Thmassumption2 "Assumption 2.2. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), we can use the martingale method as in [[20](https://arxiv.org/html/2512.00346v1#bib.bib20), Theorem 3.7.6]. For the proof, see Sect. [3.1](https://arxiv.org/html/2512.00346v1#S3.SS1 "3.1 Proofs for Sect. 2.1 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models").

###### Theorem 2.1.

Under Assumptions [2.1](https://arxiv.org/html/2512.00346v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") and [2.2](https://arxiv.org/html/2512.00346v1#S2.Thmassumption2 "Assumption 2.2. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), for each x>0\displaystyle x>0, there exists λ^>0\displaystyle\hat{\lambda}>0 such that x=𝔼​[HT​I​(λ^​HT)]\displaystyle x=\mathbb{E}[H\_{T}I(\hat{\lambda}H\_{T})].
The optimal terminal wealth ξ\displaystyle\xi and the optimal wealth process X^=(X^t)t∈[0,T]\displaystyle\hat{X}=(\hat{X}\_{t})\_{t\in[0,T]} are

|  |  |  |
| --- | --- | --- |
|  | ξ=I​(λ^​HT),X^t=1Ht​𝔼t​[HT​I​(λ^​HT)].\xi=I(\hat{\lambda}H\_{T}),\quad\hat{X}\_{t}=\frac{1}{H\_{t}}\mathbb{E}\_{t}\left[H\_{T}I(\hat{\lambda}H\_{T})\right]. |  |

Moreover, the optimal portfolio process π^=(π^t)t∈[0,T]\displaystyle\hat{\pi}=(\hat{\pi}\_{t})\_{t\in[0,T]} is given by

|  |  |  |
| --- | --- | --- |
|  | π^t=(σ⊤​(Yt))−1​(ψtHt+Xt​θ​(Yt)),\hat{\pi}\_{t}=(\sigma^{\top}(Y\_{t}))^{-1}\left(\frac{\psi\_{t}}{H\_{t}}+X\_{t}\theta(Y\_{t})\right), |  |

where ψ\displaystyle\psi is the integrand in the stochastic integral representation Mt=x+∫0t(ψu)⊤​𝑑Wu\displaystyle M\_{t}=x+\int\_{0}^{t}(\psi\_{u})^{\top}dW\_{u} of the martingale (𝔼t​[HT​I​(λ^​HT)])t∈[0,T]\displaystyle\left(\mathbb{E}\_{t}[H\_{T}I(\hat{\lambda}H\_{T})]\right)\_{t\in[0,T]}.

To derive explicit formulas for ψ\displaystyle\psi, we assume regularity and growth conditions for the market coefficients, r,θ,b,a\displaystyle r,\theta,b,a, and the derivative of I\displaystyle I, which enable us to apply the results of the Malliavin calculus.

###### Assumption 2.3.

1. (i)

   r,θ\displaystyle r,\theta are continuously differentiable and of polynomial growth, and their Jacobian matrices D​r,D​θ\displaystyle Dr,D\theta are also of polynomial growth.
2. (ii)

   b,a\displaystyle b,a are continuously differentiable, and the Jacobian matrices D​b,D​a⋅l:ℝm→ℝm×m\displaystyle Db,Da\_{\cdot l}:\mathbb{R}^{m}\to\mathbb{R}^{m\times m} are bounded, where D​b=(∂bi∂xj)1≤i≤m1≤j≤m,D​a⋅l=(ai,l∂xj)1≤i≤m1≤j≤m,(l=1,…,n)\displaystyle Db=\left(\frac{\partial b\_{i}}{\partial x\_{j}}\right)\_{\begin{subarray}{c}1\leq i\leq m\\
   1\leq j\leq m\end{subarray}},\;Da\_{\cdot l}=\left(\frac{a\_{i,l}}{\partial x\_{j}}\right)\_{\begin{subarray}{c}1\leq i\leq m\\
   1\leq j\leq m\end{subarray}},\;(l=1,\dots,n).
3. (iii)

   There exists K>0\displaystyle K>0 such that for any y,z1,…,zn∈ℝm\displaystyle y,z\_{1},\dots,z\_{n}\in\mathbb{R}^{m},

   |  |  |  |
   | --- | --- | --- |
   |  | y⊤​(b​(y)−a​(y)​θ​(y))+∑j=1nzj⊤​(D​b​(y)−∑l=1nD​a⋅l​(y)​θl​(y))​zj≤K​(1+|y|2+∑j=1n|zj|2).y^{\top}\left(b(y)-a(y)\theta(y)\right)+\sum\_{j=1}^{n}z\_{j}^{\top}\left(Db(y)-\sum\_{l=1}^{n}Da\_{\cdot l}(y)\theta^{l}(y)\right)z\_{j}\leq K\left(1+|y|^{2}+\sum\_{j=1}^{n}|z\_{j}|^{2}\right). |  |
4. (iv)

   |z​I′​(z)|≤κ​(1+z−ρ)\displaystyle|zI^{\prime}(z)|\leq\kappa(1+z^{-\rho}) for some κ>0,ρ∈(0,1]\displaystyle\kappa>0,\;\rho\in(0,1].

For Theorem [2.2](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem2 "Theorem 2.2. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), we prepare some notation. Let a pair (Y,Z)\displaystyle(Y,Z) of ℝm\displaystyle\mathbb{R}^{m}-valued stochastic process Y\displaystyle Y and ℝm×m\displaystyle\mathbb{R}^{m\times m}-valued stochastic process Z\displaystyle Z be the solution to the following system of SDEs:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | d​Ys\displaystyle\displaystyle dY\_{s} | =b​(Ys)​d​s+a​(Ys)​d​Ws,\displaystyle\displaystyle=b(Y\_{s})ds+a(Y\_{s})dW\_{s}, | Yt\displaystyle\displaystyle Y\_{t} | =y,\displaystyle\displaystyle=y, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | d​Zs\displaystyle\displaystyle dZ\_{s} | =D​b​(Ys)​Zs​d​s+∑j=1nD​a⋅j​(Ys)​Zs​d​Wsj,\displaystyle\displaystyle=Db(Y\_{s})Z\_{s}ds+\sum\_{j=1}^{n}Da\_{\cdot j}(Y\_{s})Z\_{s}dW^{j}\_{s}, | Zt\displaystyle\displaystyle Z\_{t} | =I.\displaystyle\displaystyle=I. |  |

Then a pair (Y,Z)\displaystyle(Y,Z) is a Markov process and (Y(t,y),Z(t,y))\displaystyle(Y^{(t,y)},Z^{(t,y)}) denotes the solution to the above system of SDEs when (Y,Z)\displaystyle(Y,Z) starts from (y,I)∈ℝm×ℝm×m\displaystyle(y,I)\in\mathbb{R}^{m}\times\mathbb{R}^{m\times m} at time 0. Note that Z(t,y)\displaystyle Z^{(t,y)} always starts from the identity matrix I∈ℝm×m\displaystyle I\in\mathbb{R}^{m\times m} and Ys(0,y)=Ys(t,Yt(0,y))\displaystyle Y^{(0,y)}\_{s}=Y^{(t,Y\_{t}^{(0,y)})}\_{s} for s∈[t,T]\displaystyle s\in[t,T]. Because Z(t,y)\displaystyle Z^{(t,y)} can be thought of as the derivative of Y(t,y)\displaystyle Y^{(t,y)} with respect to the initial value y\displaystyle y, we use the notation ∇yY(t,y)≔Z(t,y)\displaystyle\nabla\_{y}Y^{(t,y)}\coloneqq Z^{(t,y)} instead of Z(t,y)\displaystyle Z^{(t,y)}.
Furthermore, let H(t,y)=(Hs(t,y))s∈[t,T]\displaystyle H^{(t,y)}=\left(H\_{s}^{(t,y)}\right)\_{s\in[t,T]} be a state price density process that starts at time t and is given by

|  |  |  |
| --- | --- | --- |
|  | Hs(t,y)≔exp⁡(−∫tsr​(Yu(t,y))​𝑑u−∫tsθ⊤​(Yu(t,y))​𝑑Wu−12​∫ts|θ​(Yu(t,y))|2​𝑑u).H\_{s}^{(t,y)}\coloneqq\exp\left(-\int\_{t}^{s}r(Y^{(t,y)}\_{u})du-\int\_{t}^{s}\theta^{\top}(Y^{(t,y)}\_{u})dW\_{u}-\frac{1}{2}\int\_{t}^{s}|\theta(Y^{(t,y)}\_{u})|^{2}du\right). |  |

Let ∇yH(t,y)=(∇yHs(t,y))s∈[t,T],L(t,y)=(Ls(t,y))s∈[t,T]\displaystyle\nabla\_{y}H^{(t,y)}=\left(\nabla\_{y}H\_{s}^{(t,y)}\right)\_{s\in[t,T]},\;L^{(t,y)}=\left(L\_{s}^{(t,y)}\right)\_{s\in[t,T]} be ℝm\displaystyle\mathbb{R}^{m}-valued stochastic processes given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ls(t,y)\displaystyle\displaystyle L\_{s}^{(t,y)} | ≔∫ts(D​r​(Yu(t,y))​∇yYu(t,y))⊤​𝑑u+∫ts(D​θ​(Yu(t,y))​∇yYu(t,y))⊤​𝑑Wu\displaystyle\displaystyle\coloneqq\int\_{t}^{s}(Dr(Y^{(t,y)}\_{u})\nabla\_{y}Y^{(t,y)}\_{u})^{\top}du+\int\_{t}^{s}\left(D\theta(Y^{(t,y)}\_{u})\nabla\_{y}Y^{(t,y)}\_{u}\right)^{\top}dW\_{u} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫ts(D​θ​(Yu(t,y))​∇yYu(t,y))⊤​θ​(Yu(t,y))​𝑑u,\displaystyle\displaystyle\qquad+\int\_{t}^{s}\left(D\theta(Y^{(t,y)}\_{u})\nabla\_{y}Y\_{u}^{(t,y)}\right)^{\top}\theta(Y\_{u}^{(t,y)})du, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇yHs(t,y)\displaystyle\displaystyle\nabla\_{y}H\_{s}^{(t,y)} | ≔−Hs(t,y)​Ls(t,y).\displaystyle\displaystyle\coloneqq-H\_{s}^{(t,y)}L\_{s}^{(t,y)}. |  |

We can also consider ∇yH(t,y)\displaystyle\nabla\_{y}H^{(t,y)} as the derivative of H(t,y)\displaystyle H^{(t,y)} with respect to y\displaystyle y. When Y\displaystyle Y starts from y\displaystyle y at time 0, we drop the superscripts (0,y)\displaystyle(0,y).

###### Theorem 2.2.

Under Assumptions [2.1](https://arxiv.org/html/2512.00346v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")–[2.3](https://arxiv.org/html/2512.00346v1#S2.Thmassumption3 "Assumption 2.3. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), the optimal portfolio process π^\displaystyle\hat{\pi} in Theorem [2.1](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") can be represented by

|  |  |  |  |
| --- | --- | --- | --- |
|  | π^t\displaystyle\displaystyle\hat{\pi}\_{t} | =−(σ⊤​(Yt))−1​θ​(Yt)​1Ht​𝔼t​[HT⋅λ^​HT​I′​(λ^​HT)]\displaystyle\displaystyle=-(\sigma^{\top}(Y\_{t}))^{-1}\theta(Y\_{t})\frac{1}{H\_{t}}\mathbb{E}\_{t}\left[H\_{T}\cdot\hat{\lambda}H\_{T}I^{\prime}(\hat{\lambda}H\_{T})\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(σ⊤​(Yt))−1​a⊤​(Yt)​𝔼t​[∇yHT(t,Yt)​(I​(λ​HT^)+λ^​HT​I′​(λ^​HT))].\displaystyle\displaystyle\qquad+(\sigma^{\top}(Y\_{t}))^{-1}a^{\top}(Y\_{t})\mathbb{E}\_{t}\left[\nabla\_{y}H^{(t,Y\_{t})}\_{T}\left(I(\hat{\lambda H\_{T}})+\hat{\lambda}H\_{T}I^{\prime}(\hat{\lambda}H\_{T})\right)\right]. |  |

###### Remark 2.1.

* (i)

  We can find similar results in [[6](https://arxiv.org/html/2512.00346v1#bib.bib6), [10](https://arxiv.org/html/2512.00346v1#bib.bib10), [24](https://arxiv.org/html/2512.00346v1#bib.bib24), [37](https://arxiv.org/html/2512.00346v1#bib.bib37)]. Here, we state the differences between our arguments and those of the previous papers. Firstly, [[6](https://arxiv.org/html/2512.00346v1#bib.bib6)] considers the same market model as ours and assumes that HT​I​(z​HT)∈𝔻2,1\displaystyle H\_{T}I(zH\_{T})\in\mathbb{D}\_{2,1}, which is difficult to check in general. In the present paper, we check that HT​I​(z​HT)∈𝔻1,1\displaystyle H\_{T}I(zH\_{T})\in\mathbb{D}\_{1,1}, which is enough to use Clark’s formula (Proposition [A.1](https://arxiv.org/html/2512.00346v1#A1.Thmtheorem1 "Proposition A.1. ‣ Appendix A Appendix: Malliavin calculus ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")), with the growth conditions for an inverse marginal utility I\displaystyle I, its derivative I′\displaystyle I^{\prime}, and market coefficients (Assumptions [2.1](https://arxiv.org/html/2512.00346v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")–[2.3](https://arxiv.org/html/2512.00346v1#S2.Thmassumption3 "Assumption 2.3. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")). Secondly, [[24](https://arxiv.org/html/2512.00346v1#bib.bib24), [37](https://arxiv.org/html/2512.00346v1#bib.bib37)] check the conditions that HT​I​(z​HT)∈𝔻1,1\displaystyle H\_{T}I(zH\_{T})\in\mathbb{D}\_{1,1} with linear Gaussian dynamics for the drift process μt\displaystyle\mu\_{t} under partial information. Their assumptions for market coefficients depend on the investment horizon T\displaystyle T, but our assumptions do not depend on T\displaystyle T, which is more useful for proving the turnpike theorem. Lastly, [[10](https://arxiv.org/html/2512.00346v1#bib.bib10)] uses stochastic flow techniques instead of Malliavin calculus. Because the assumptions in [[10](https://arxiv.org/html/2512.00346v1#bib.bib10)] also depend on T\displaystyle T and are difficult to check for our model, we do not use the results of [[10](https://arxiv.org/html/2512.00346v1#bib.bib10)].
* (ii)

  We can represent the optimal portfolio process π^\displaystyle\hat{\pi} by the Arrow–Pratt measure of absolute risk tolerance A​R​TU​(x)≔−U′​(x)U′′​(x)\displaystyle ART\_{U}(x)\coloneqq-\frac{U^{\prime}(x)}{U^{\prime\prime}(x)} as in [[6](https://arxiv.org/html/2512.00346v1#bib.bib6)]:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | π^t\displaystyle\displaystyle\hat{\pi}\_{t} | =(σ⊤​(Yt))−1​θ​(Yt)​1Ht​𝔼t​[HT⋅A​R​TU​(X^T)]\displaystyle\displaystyle=(\sigma^{\top}(Y\_{t}))^{-1}\theta(Y\_{t})\frac{1}{H\_{t}}\mathbb{E}\_{t}\left[H\_{T}\cdot ART\_{U}(\hat{X}\_{T})\right] |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | +(σ⊤​(Yt))−1​a⊤​(Yt)​𝔼t​[∇yHT(t,Yt)​(X^T−A​R​TU​(X^T))].\displaystyle\displaystyle\qquad+(\sigma^{\top}(Y\_{t}))^{-1}a^{\top}(Y\_{t})\mathbb{E}\_{t}\left[\nabla\_{y}H^{(t,Y\_{t})}\_{T}\left(\hat{X}\_{T}-ART\_{U}(\hat{X}\_{T})\right)\right]. |  |

  Moreover, the optimal portfolio π^\displaystyle\hat{\pi} can be divided into two components, namely, the myopic portfolio π^M\displaystyle\hat{\pi}^{M} and the excess hedging demand π^H\displaystyle\hat{\pi}^{H}:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | π^t\displaystyle\displaystyle\hat{\pi}\_{t} | =π^tM+π^tH,\displaystyle\displaystyle=\hat{\pi}^{M}\_{t}+\hat{\pi}^{H}\_{t}, |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | π^tM\displaystyle\displaystyle\hat{\pi}^{M}\_{t} | =(σ⊤​(Yt))−1​θ​(Yt)​1Ht​𝔼t​[HT⋅A​R​TU​(X^T)],\displaystyle\displaystyle=(\sigma^{\top}(Y\_{t}))^{-1}\theta(Y\_{t})\frac{1}{H\_{t}}\mathbb{E}\_{t}\left[H\_{T}\cdot ART\_{U}(\hat{X}\_{T})\right], |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | π^tH\displaystyle\displaystyle\hat{\pi}^{H}\_{t} | =(σ⊤​(Yt))−1​a⊤​(Yt)​𝔼t​[∇yHT(t,Yt)​(X^T−A​R​TU​(X^T))].\displaystyle\displaystyle=(\sigma^{\top}(Y\_{t}))^{-1}a^{\top}(Y\_{t})\mathbb{E}\_{t}\left[\nabla\_{y}H^{(t,Y\_{t})}\_{T}\left(\hat{X}\_{T}-ART\_{U}(\hat{X}\_{T})\right)\right]. |  |

By the Markov property of the market model, the optimal portfolio process π^\displaystyle\hat{\pi} obtained in Theorem [2.2](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem2 "Theorem 2.2. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") is given by a feedback form.

###### Proposition 2.3.

Under Assumptions [2.1](https://arxiv.org/html/2512.00346v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")–[2.3](https://arxiv.org/html/2512.00346v1#S2.Thmassumption3 "Assumption 2.3. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), the optimal portfolio process π^\displaystyle\hat{\pi} in Theorem [2.1](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") can be represented by a feedback form

|  |  |  |
| --- | --- | --- |
|  | π^t=π^​(T−t,X^t,Yt),t∈[0,T],\hat{\pi}\_{t}=\hat{\pi}(T-t,\hat{X}\_{t},Y\_{t}),\quad t\in[0,T], |  |

where π^:(0,∞)×(0,∞)×ℝm→ℝn\displaystyle\hat{\pi}:(0,\infty)\times(0,\infty)\times\mathbb{R}^{m}\to\mathbb{R}^{n} is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | π^​(τ,x,y)\displaystyle\displaystyle\hat{\pi}(\tau,x,y) | ≔π^M​(τ,x,y)+π^H​(τ,x,y),\displaystyle\displaystyle\coloneqq\hat{\pi}^{M}(\tau,x,y)+\hat{\pi}^{H}(\tau,x,y), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | π^M​(τ,x,y)\displaystyle\displaystyle\hat{\pi}^{M}(\tau,x,y) | ≔−(σ⊤​(y))−1​θ​(y)​𝔼y​[Hτ⋅λ^​Hτ​I′​(λ^​Hτ)],\displaystyle\displaystyle\coloneqq-(\sigma^{\top}(y))^{-1}\theta(y)\mathbb{E}^{y}\left[H\_{\tau}\cdot{\hat{\lambda}H\_{\tau}I^{\prime}(\hat{\lambda}H\_{\tau})}\right], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | π^H​(τ,x,y)\displaystyle\displaystyle\hat{\pi}^{H}(\tau,x,y) | ≔(σ⊤​(y))−1​a⊤​(y)​𝔼y​[∇yHτ​(I​(λ^​Hτ)+λ^​Hτ​I′​(λ^​Hτ))],\displaystyle\displaystyle\coloneqq(\sigma^{\top}(y))^{-1}a^{\top}(y)\mathbb{E}^{y}\left[\nabla\_{y}H\_{\tau}\left(I(\hat{\lambda}H\_{\tau})+\hat{\lambda}H\_{\tau}I^{\prime}(\hat{\lambda}H\_{\tau})\right)\right], |  |

and λ^=λ^​(τ,x,y)\displaystyle\hat{\lambda}=\hat{\lambda}(\tau,x,y) is defined by an equality x=𝔼y​[Hτ​I​(λ​Hτ)]\displaystyle x=\mathbb{E}^{y}[H\_{\tau}I(\lambda H\_{\tau})].

### 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models

In this subsection, we consider two investors with utility functions Ui:(0,∞)→(−∞,∞),(i=1,2)\displaystyle U\_{i}:(0,\infty)\to(-\infty,\infty),\;(i=1,2), and we fix an initial wealth x>0\displaystyle x>0 for both investors. We denote the corresponding optimal terminal wealth ξ\displaystyle\xi, optimal wealth process X^\displaystyle\hat{X}, and optimal feedback function π^\displaystyle\hat{\pi} for the i\displaystyle i-th investor by ξi,T,X^i,T\displaystyle\xi^{i,T},\hat{X}^{i,T}, and π^i\displaystyle\hat{\pi}^{i}, respectively.
In this subsection, we consider the turnpike theorem for myopic portfolios under general stochastic factor models ([2](https://arxiv.org/html/2512.00346v1#S2.E2 "In 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) introduced in the previous subsection. That is, we show that for each x\displaystyle x and y\displaystyle y,

|  |  |  |
| --- | --- | --- |
|  | |π^1,M​(T,x,y)−π^2,M​(T,x,y)|→0,(T↗∞),|\hat{\pi}^{1,M}(T,x,y)-\hat{\pi}^{2,M}(T,x,y)|\rightarrow 0,\quad(T\nearrow\infty), |  |

and we derive its convergence rate in terms of 𝔼​[HT]\displaystyle\mathbb{E}[H\_{T}].

###### Assumption 2.4.

1. (i)

   Let p∈(−∞,0]\displaystyle p\in(-\infty,0]. For p<0\displaystyle p<0, we set

   |  |  |  |
   | --- | --- | --- |
   |  | U2​(x)≔xpp,x∈(0,∞),U\_{2}(x)\coloneqq\frac{x^{p}}{p},\quad x\in(0,\infty), |  |

   for p=0\displaystyle p=0,

   |  |  |  |
   | --- | --- | --- |
   |  | U2​(x)≔log⁡x,x∈(0,∞).U\_{2}(x)\coloneqq\log x,\quad x\in(0,\infty). |  |
2. (ii)

   Let q≔pp−1∈[0,1)\displaystyle q\coloneqq\frac{p}{p-1}\in[0,1). There exist constants K∈[0,∞),α∈(q−1,0]\displaystyle K\in[0,\infty),\alpha\in(q-1,0] such that

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | |I1​(z)−I2​(z)|\displaystyle\displaystyle|I\_{1}(z)-I\_{2}(z)| | ≤K​(1+zα),z∈(0,∞),\displaystyle\displaystyle\leq K(1+z^{\alpha}),\quad z\in(0,\infty), |  | (3) |
   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | |z​I1′​(z)−z​I2′​(z)|\displaystyle\displaystyle|zI^{\prime}\_{1}(z)-zI^{\prime}\_{2}(z)| | ≤K​(1+zα),z∈(0,∞).\displaystyle\displaystyle\leq K(1+z^{\alpha}),\quad z\in(0,\infty). |  | (4) |
3. (iii)

   |  |  |  |
   | --- | --- | --- |
   |  | 𝔼​[HT]↘0,(T↗∞).\mathbb{E}[H\_{T}]\searrow 0,\quad(T\nearrow\infty). |  |

###### Remark 2.2.

Because the von Neumann–Morgenstern (vN-M) utility function U1\displaystyle U\_{1} for the first investor is uniquely determined up to positive affine transformations [[11](https://arxiv.org/html/2512.00346v1#bib.bib11), Theorem 2.21], any conditions for vN-M utility function U1\displaystyle U\_{1} must be invariant for positive affine transformations. In this case, we have to assume a generalized version of Assumption [2.4](https://arxiv.org/html/2512.00346v1#S2.Thmassumption4 "Assumption 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")(ii) as follows.

###### Assumption.

There exist constants C>0,K≥0,α∈(q−1,0]\displaystyle C>0,K\geq 0,\alpha\in(q-1,0] such that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |I1​(z)−C​I2​(z)|\displaystyle|I\_{1}(z)-CI\_{2}(z)| | ≤K​(1+zα),z∈(0,∞),\displaystyle\leq K(1+z^{\alpha}),\quad z\in(0,\infty), |  | (5) |
|  | |z​I1′​(z)−C​z​I2′​(z)|\displaystyle|zI^{\prime}\_{1}(z)-CzI^{\prime}\_{2}(z)| | ≤K​(1+zα),z∈(0,∞).\displaystyle\leq K(1+z^{\alpha}),\quad z\in(0,\infty). |  |

If U1\displaystyle U\_{1} satisfies ([5](https://arxiv.org/html/2512.00346v1#S2.E5 "In Assumption. ‣ Remark 2.2. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")), then U~1≔a​U1+b\displaystyle\tilde{U}\_{1}\coloneqq aU\_{1}+b also satisfies ([5](https://arxiv.org/html/2512.00346v1#S2.E5 "In Assumption. ‣ Remark 2.2. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) for any a>0,b∈ℝ\displaystyle a>0,\;b\in\mathbb{R}, which means that ([5](https://arxiv.org/html/2512.00346v1#S2.E5 "In Assumption. ‣ Remark 2.2. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) is invariant for positive affine transformations. In particular, if U1\displaystyle U\_{1} satisfies ([5](https://arxiv.org/html/2512.00346v1#S2.E5 "In Assumption. ‣ Remark 2.2. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")), then U~1≔a​U1,a≔C1q−1\displaystyle\tilde{U}\_{1}\coloneqq aU\_{1},\;a\coloneqq C^{\frac{1}{q-1}} satisfies ([5](https://arxiv.org/html/2512.00346v1#S2.E5 "In Assumption. ‣ Remark 2.2. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) for C=1\displaystyle C=1 and the optimal feedback function given by Proposition [2.3](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem3 "Proposition 2.3. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") is invariant, which means that without loss of generality, we can assume C=1\displaystyle C=1 in ([5](https://arxiv.org/html/2512.00346v1#S2.E5 "In Assumption. ‣ Remark 2.2. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")), that is, (ii) in Assumption [2.4](https://arxiv.org/html/2512.00346v1#S2.Thmassumption4 "Assumption 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models").

###### Remark 2.3.

If a function U\displaystyle U is twice differentiable and satisfies ([3](https://arxiv.org/html/2512.00346v1#S2.E3 "In item (ii) ‣ Assumption 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) in Assumption [2.4](https://arxiv.org/html/2512.00346v1#S2.Thmassumption4 "Assumption 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")(ii) for p∈(−∞,1)\displaystyle p\in(-\infty,1), then
U′\displaystyle U^{\prime} is regularly varying with an exponent p−1\displaystyle p-1 and

|  |  |  |
| --- | --- | --- |
|  | limx↗∞R​R​AU​(x)=limx↗∞−U′′​(x)​xU′​(x)=1−p.\lim\_{x\nearrow\infty}RRA\_{U}(x)=\lim\_{x\nearrow\infty}\frac{-U^{\prime\prime}(x)x}{U^{\prime}(x)}=1-p. |  |

For a proof, see [[5](https://arxiv.org/html/2512.00346v1#bib.bib5), Proposition 2]. Furthermore, by the identity I2​(z)=zq−1\displaystyle I\_{2}(z)=z^{q-1}, the ratio of the inverse marginal utilities, I1I2\displaystyle\frac{I\_{1}}{I\_{2}}, and the ratio of the derivatives, I1′I2′\displaystyle\frac{I\_{1}^{\prime}}{I^{\prime}\_{2}}, satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | |I1​(z)I2​(z)−1|\displaystyle\displaystyle\left|\frac{I\_{1}(z)}{I\_{2}(z)}-1\right| | ≤K​(z−(q−1)+zα−(q−1)),\displaystyle\displaystyle\leq K\left(z^{-(q-1)}+z^{\alpha-(q-1)}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | |I1′​(z)I2′​(z)−1|\displaystyle\displaystyle\left|\frac{I^{\prime}\_{1}(z)}{I\_{2}^{\prime}(z)}-1\right| | ≤K1−q​(z−(q−1)+zα−(q−1)).\displaystyle\displaystyle\leq\frac{K}{1-q}\left(z^{-(q-1)}+z^{\alpha-(q-1)}\right). |  |

These inequalities imply that these ratios converge to 1, and the speed of convergence is determined by α−(q−1)\displaystyle\alpha-(q-1).

###### Remark 2.4.

Although the inequality ([3](https://arxiv.org/html/2512.00346v1#S2.E3 "In item (ii) ‣ Assumption 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) can be derived from ([4](https://arxiv.org/html/2512.00346v1#S2.E4 "In item (ii) ‣ Assumption 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")), we assume both inequalities for simplicity.

###### Remark 2.5.

When showing turnpike theorems, Assumption [2.4](https://arxiv.org/html/2512.00346v1#S2.Thmassumption4 "Assumption 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")(iii) is the usual one in previous works. Indeed, Dybvig et al. [[9](https://arxiv.org/html/2512.00346v1#bib.bib9)] assume the same condition. Furthermore, Cox and Huang [[5](https://arxiv.org/html/2512.00346v1#bib.bib5)], Jin [[19](https://arxiv.org/html/2512.00346v1#bib.bib19)], Huang and Zariphopoulou[[17](https://arxiv.org/html/2512.00346v1#bib.bib17)], and Bian and Zheng [[3](https://arxiv.org/html/2512.00346v1#bib.bib3), [4](https://arxiv.org/html/2512.00346v1#bib.bib4)] consider the Black–Scholes model and assume that the interest rate r\displaystyle r is strictly positive, which is equivalent to 𝔼​[HT]↘0\displaystyle\mathbb{E}[H\_{T}]\searrow 0 in the model. Because

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[HT]=𝔼ℚ​[exp⁡(−∫0Tr​(Yt)​𝑑t)]\mathbb{E}[H\_{T}]=\mathbb{E}^{\mathbb{Q}}\left[\exp{\left(-\int\_{0}^{T}r(Y\_{t})dt\right)}\right] |  |

is the price of a zero-coupon bond with maturity T\displaystyle T at t=0\displaystyle t=0, Assumption [2.4](https://arxiv.org/html/2512.00346v1#S2.Thmassumption4 "Assumption 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")(iii) implies that the interest rate r​(Yt)\displaystyle r(Y\_{t}) is positive in the long run.

The following theorem is one of our main results.

###### Theorem 2.4.

Under Assumptions [2.1](https://arxiv.org/html/2512.00346v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")–[2.4](https://arxiv.org/html/2512.00346v1#S2.Thmassumption4 "Assumption 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), there exists an M=M​(x,y)∈(−∞,x]\displaystyle M=M(x,y)\in(-\infty,x] that is independent of T\displaystyle T such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |π^1,M​(T,x,y)−π^2,M​(T,x,y)|\displaystyle\displaystyle|\hat{\pi}^{1,M}(T,x,y)-\hat{\pi}^{2,M}(T,x,y)| | ≤K​(2−q)​|σ⊤​(y)−1​θ​(y)|​(𝔼​[HT]+(x−M)αq−1​𝔼​[HT]1−αq−1)\displaystyle\displaystyle\leq K(2-q)|\sigma^{\top}(y)^{-1}\theta(y)|\left(\mathbb{E}[H\_{T}]+(x-M)^{\frac{\alpha}{q-1}}\mathbb{E}[H\_{T}]^{1-\frac{\alpha}{q-1}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =O​(𝔼​[HT]1−αq−1),(T↗∞).\displaystyle\displaystyle=O\left(\mathbb{E}[H\_{T}]^{1-\frac{\alpha}{q-1}}\right),\quad(T\nearrow\infty). |  |

###### Remark 2.6.

Here we want to emphasize that the convergence rate of the turnpike theorem in stochastic factor models is determined by two components: (i) the speed of market growth, 𝔼​[HT]\displaystyle\mathbb{E}[H\_{T}], and (ii) the similarity between utilities captured by α\displaystyle\alpha and q\displaystyle q. In addition, if the interest rate is a positive constant, r​(Yt)=r>0\displaystyle r(Y\_{t})=r>0, then the convergence rate is e−r​(1−αq−1)​T\displaystyle e^{-r\left(1-\frac{\alpha}{q-1}\right)T}, which is the same rate as in Bian and Zheng [[3](https://arxiv.org/html/2512.00346v1#bib.bib3)]. Therefore, the rate 𝔼​[HT]1−αq−1\displaystyle\mathbb{E}[H\_{T}]^{1-\frac{\alpha}{q-1}} derived in the present paper is a natural extension of the rate in [[3](https://arxiv.org/html/2512.00346v1#bib.bib3)].

###### Remark 2.7.

As studied by Qin and Linetsky [[38](https://arxiv.org/html/2512.00346v1#bib.bib38)], the decay speed of 𝔼​[HT]\displaystyle\mathbb{E}[H\_{T}] is exponential in general.
Indeed, (ii) of Theorem 3.2 in [[38](https://arxiv.org/html/2512.00346v1#bib.bib38)] shows that under a general semimartingale model satisfying some assumptions,

|  |  |  |
| --- | --- | --- |
|  | limT↗∞−log⁡𝔼​[HT]T=λ\lim\_{T\nearrow\infty}\frac{-\log\mathbb{E}[H\_{T}]}{T}=\lambda |  |

holds for some λ∈ℝ\displaystyle\lambda\in\mathbb{R}. When all uncertainty is generated by a time-homogeneous Markov process X\displaystyle X, eλ​t\displaystyle e^{\lambda t} is an eigenvalue of the pricing operator 𝒫t​f​(x)≔𝔼​[Ht​f​(Xt)|X0=x]\displaystyle\mathcal{P}\_{t}f(x)\coloneqq\mathbb{E}[H\_{t}f(X\_{t})|X\_{0}=x]. For details, see [[38](https://arxiv.org/html/2512.00346v1#bib.bib38), [39](https://arxiv.org/html/2512.00346v1#bib.bib39), [40](https://arxiv.org/html/2512.00346v1#bib.bib40)].

Although Theorem [2.4](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem4 "Theorem 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") seems to imply that the convergence is not uniform in x\displaystyle x, we can prove uniform convergence in x\displaystyle x for portfolio proportions π^i,M​(T,x,y)x\displaystyle\frac{\hat{\pi}^{i,M}(T,x,y)}{x}.

###### Theorem 2.5.

Under Assumptions [2.1](https://arxiv.org/html/2512.00346v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")–[2.4](https://arxiv.org/html/2512.00346v1#S2.Thmassumption4 "Assumption 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), for any ϵ>0\displaystyle\epsilon>0,

|  |  |  |
| --- | --- | --- |
|  | supx>ϵ|π^1,M​(T,x,y)x−π^2,M​(T,x,y)x|=O​(𝔼​[HT]1−αq−1),(T↗∞).\displaystyle\displaystyle\sup\_{x>\epsilon}\left|\frac{\hat{\pi}^{1,M}(T,x,y)}{x}-\frac{\hat{\pi}^{2,M}(T,x,y)}{x}\right|=O\left(\mathbb{E}[H\_{T}]^{1-\frac{\alpha}{q-1}}\right),\quad(T\nearrow\infty). |  |

###### Remark 2.8.

We cannot prove uniform convergence in y\displaystyle y because y↦θ​(y)\displaystyle y\mapsto\theta(y) has linear growth and is generally unbounded.

We can also show that the time-0 value of the difference between the optimal wealth processes at time t\displaystyle t converges to 0 uniformly in t\displaystyle t and that the convergence rate is the same as in the above theorems.

###### Theorem 2.6.

Under Assumptions [2.1](https://arxiv.org/html/2512.00346v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")–[2.4](https://arxiv.org/html/2512.00346v1#S2.Thmassumption4 "Assumption 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"),

|  |  |  |  |
| --- | --- | --- | --- |
|  | supt∈[0,T]𝔼​[Ht​|X^t1,T−Xt2,T|]=O​(𝔼​[HT]1−αq−1),(T↗∞).\sup\_{t\in[0,T]}\mathbb{E}[H\_{t}|\hat{X}^{1,T}\_{t}-X^{2,T}\_{t}|]=O\left(\mathbb{E}[H\_{T}]^{1-\frac{\alpha}{q-1}}\right),\quad(T\nearrow\infty). |  | (6) |

###### Remark 2.9.

The convergence limT↗∞𝔼​[Ht​|X^t1,T−Xt2,T|]=0\displaystyle\lim\_{T\nearrow\infty}\mathbb{E}[H\_{t}|\hat{X}^{1,T}\_{t}-X^{2,T}\_{t}|]=0 is already proved in complete markets by Dybvig et al. [[9](https://arxiv.org/html/2512.00346v1#bib.bib9)]. Here, our focus is on the convergence rate.

### 2.3 Turnpike theorem for excess hedging demands under quadratic term structure models

In this subsection, we consider quadratic term structure models studied by [[1](https://arxiv.org/html/2512.00346v1#bib.bib1), [25](https://arxiv.org/html/2512.00346v1#bib.bib25)]. The market model consists of a riskless bond S0\displaystyle S^{0}, n\displaystyle n risky assets S=(S1,…,Sn)⊤\displaystyle S=(S^{1},\dots,S^{n})^{\top}, and an m\displaystyle m-dimensional factor process Y=(Y1,…,Ym)⊤\displaystyle Y=(Y^{1},\dots,Y^{m})^{\top} that affects the risk-free interest rate r​(Yt)\displaystyle r(Y\_{t}) of S0\displaystyle S^{0} and the mean return rate μ​(Yt)\displaystyle\mu(Y\_{t}) of S\displaystyle S:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | d​St0\displaystyle dS^{0}\_{t} | =St0​r​(Yt)​d​t,\displaystyle=S^{0}\_{t}r(Y\_{t})dt, | S00\displaystyle S^{0}\_{0} | =1,\displaystyle=1, |  | (7) |
|  | d​St\displaystyle dS\_{t} | =diag​(St)​{μ​(Yt)​d​t+Σ​d​Wt},\displaystyle=\mathrm{diag}(S\_{t})\left\{\mu(Y\_{t})dt+\Sigma dW\_{t}\right\}, | S0\displaystyle S\_{0} | ∈ℝ++n,\displaystyle\in\mathbb{R}^{n}\_{++}, |  |
|  | d​Yt\displaystyle dY\_{t} | =(b+B​Yt)​d​t+Λ​d​Wt,\displaystyle=(b+BY\_{t})dt+\Lambda dW\_{t}, | Y0\displaystyle Y\_{0} | =y∈ℝm,\displaystyle=y\in\mathbb{R}^{m}, |  |

where r:ℝm→ℝ,μ:ℝm→ℝn,Σ∈ℝn×n,b∈ℝm,B∈ℝm×m,Λ∈ℝm×n\displaystyle r:\mathbb{R}^{m}\to\mathbb{R},\;\mu:\mathbb{R}^{m}\to\mathbb{R}^{n},\;\Sigma\in\mathbb{R}^{n\times n},\;b\in\mathbb{R}^{m},\;B\in\mathbb{R}^{m\times m},\Lambda\in\mathbb{R}^{m\times n}. Furthermore, we assume that the risk-free interest rate r​(Yt)\displaystyle r(Y\_{t}) of S0\displaystyle S^{0} is a quadratic Gaussian process and the market price of risk θ​(Yt)≔Σ−1​(μ​(Yt)−𝟏​r​(Yt))\displaystyle\theta(Y\_{t})\coloneqq\Sigma^{-1}\left(\mu(Y\_{t})-\mathbf{1}r(Y\_{t})\right) is a linear Gaussian process as follows:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | r​(y)\displaystyle r(y) | ≔r0+r1⊤​y+12​y⊤​R2​y,\displaystyle\coloneqq r\_{0}+r\_{1}^{\top}y+\frac{1}{2}y^{\top}R\_{2}y, |  | (8) |
|  | θ​(y)\displaystyle\theta(y) | ≔a+A​y,\displaystyle\coloneqq a+Ay, |  |
|  | μ​(y)\displaystyle\mu(y) | ≔Σ​θ​(y)+𝟏​r​(y),\displaystyle\coloneqq\Sigma\theta(y)+\mathbf{1}r(y), |  |

where r0∈ℝ,r1∈ℝm,R2∈ℝm×m,a∈ℝn,A∈ℝn×m,\displaystyle r\_{0}\in\mathbb{R},\;r\_{1}\in\mathbb{R}^{m},\;R\_{2}\in\mathbb{R}^{m\times m},\;a\in\mathbb{R}^{n},\;A\in\mathbb{R}^{n\times m}, and 𝟏=(1,…,1)⊤∈ℝn\displaystyle\mathbf{1}=(1,\dots,1)^{\top}\in\mathbb{R}^{n}. We denote the totality of m×m\displaystyle m\times m, real, symmetric matrices by 𝕊m\displaystyle\mathbb{S}^{m} and 𝕊+m≔{M∈𝕊m;M≥0}\displaystyle\mathbb{S}^{m}\_{+}\coloneqq\left\{M\in\mathbb{S}^{m};\;M\geq 0\right\}, 𝕊++m≔{M∈𝕊m;M>0}\displaystyle\mathbb{S}^{m}\_{++}\coloneqq\left\{M\in\mathbb{S}^{m};\;M>0\right\}. We assume the following conditions.

###### Assumption 2.5.

* (i)

  Σ\displaystyle\Sigma is invertible.
* (ii)

  R2∈𝕊+m\displaystyle R\_{2}\in\mathbb{S}^{m}\_{+}.
* (iii)

  R2=0\displaystyle R\_{2}=0 or (γ​(1−γ)​A⊤​A+γ​R2)∈𝕊++m\displaystyle\left(\gamma(1-\gamma)A^{\top}A+\gamma R\_{2}\right)\in\mathbb{S}^{m}\_{++} for γ∈{q,1+α}\displaystyle\gamma\in\left\{q,1+\alpha\right\}.
* (iv)

  B\displaystyle B is stable; that is, all its eigenvalues have negative real parts.

Under Assumptions [2.4](https://arxiv.org/html/2512.00346v1#S2.Thmassumption4 "Assumption 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") and [2.5](https://arxiv.org/html/2512.00346v1#S2.Thmassumption5 "Assumption 2.5. ‣ 2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), the quadratic term structure model given by ([7](https://arxiv.org/html/2512.00346v1#S2.E7 "In 2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) and ([8](https://arxiv.org/html/2512.00346v1#S2.E8 "In 2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) satisfies Assumptions [2.1](https://arxiv.org/html/2512.00346v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")–[2.3](https://arxiv.org/html/2512.00346v1#S2.Thmassumption3 "Assumption 2.3. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"). Therefore, all main results in Sects. [2.1](https://arxiv.org/html/2512.00346v1#S2.SS1 "2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") and [2.2](https://arxiv.org/html/2512.00346v1#S2.SS2 "2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") are valid.

###### Remark 2.10.

Assumption [2.5](https://arxiv.org/html/2512.00346v1#S2.Thmassumption5 "Assumption 2.5. ‣ 2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")(iv) implies that Y\displaystyle Y is a multivariate Ornstein–Uhlenbeck process. In particular, the model includes well-known short-rate models, such as the Vasicek model and special versions of the CIR model; for details, see [[1](https://arxiv.org/html/2512.00346v1#bib.bib1)].

###### Remark 2.11.

We restrict our analysis to the quadratic term structure model given by ([7](https://arxiv.org/html/2512.00346v1#S2.E7 "In 2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) and ([8](https://arxiv.org/html/2512.00346v1#S2.E8 "In 2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) for the following reason. As Proposition [3.11](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem11 "Proposition 3.11. ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") says, to estimate the rates for excess hedging demands, we have to compute the asymptotic behavior of the stochastic factor process Y\displaystyle Y under myopic probability measures ℚTγ,γ∈[0,1],\displaystyle\mathbb{Q}^{\gamma}\_{T},\;\gamma\in[0,1], defined by

|  |  |  |
| --- | --- | --- |
|  | d​ℚTγ≔HTγ𝔼​[HTγ]​d​ℙ.d\mathbb{Q}^{\gamma}\_{T}\coloneqq\frac{H\_{T}^{\gamma}}{\mathbb{E}[H\_{T}^{\gamma}]}d\mathbb{P}. |  |

When γ=1\displaystyle\gamma=1, the myopic probability measure ℚT1\displaystyle\mathbb{Q}^{1}\_{T} is a T\displaystyle T-forward measure. When γ∈(0,1)\displaystyle\gamma\in(0,1), the measures are given by the optimal wealth processes X^TT\displaystyle\hat{X}^{T}\_{T} for CRRA investors:

|  |  |  |
| --- | --- | --- |
|  | d​ℚTγ=U​(X^TT)𝔼​[U​(X^TT)]​d​ℙ,d\mathbb{Q}^{\gamma}\_{T}=\frac{U(\hat{X}^{T}\_{T})}{\mathbb{E}\left[U(\hat{X}^{T}\_{T})\right]}d\mathbb{P}, |  |

where, U​(x)≔xpp,p≔γγ−1\displaystyle U(x)\coloneqq\frac{x^{p}}{p},\;p\coloneqq\frac{\gamma}{\gamma-1}. As Guasoni et al. [[13](https://arxiv.org/html/2512.00346v1#bib.bib13)] say, by using results on CRRA utility maximization problems, we can represent the probability density processes of ℚTγ\displaystyle\mathbb{Q}^{\gamma}\_{T} as stochastic exponential martingales in terms of the optimal portfolio processes. Therefore, in the quadratic term structure model given by ([7](https://arxiv.org/html/2512.00346v1#S2.E7 "In 2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) and ([8](https://arxiv.org/html/2512.00346v1#S2.E8 "In 2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")), we can analyze the asymptotic behavior of Y\displaystyle Y under ℚTγ\displaystyle\mathbb{Q}^{\gamma}\_{T} by using the asymptotic behavior of the solutions to Riccati differential equations. Because the optimal portfolios in nonlinear stochastic factor models ([2](https://arxiv.org/html/2512.00346v1#S2.E2 "In 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) are given by solutions of semilinear PDEs (see Nagai [[33](https://arxiv.org/html/2512.00346v1#bib.bib33)]), our analysis will require more-advanced techniques, and further research for nonlinear stochastic factor models will be addressed in future work.

Under these assumptions, we can also derive the convergence rates for excess hedging demands.

###### Theorem 2.7.

Under Assumptions [2.4](https://arxiv.org/html/2512.00346v1#S2.Thmassumption4 "Assumption 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") and [2.5](https://arxiv.org/html/2512.00346v1#S2.Thmassumption5 "Assumption 2.5. ‣ 2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"),

|  |  |  |
| --- | --- | --- |
|  | |π^1,H​(T,x,y)−π^2,H​(T,x,y)|=O​(𝔼​[HT]1−αq−1),(T↗∞).|\hat{\pi}^{1,H}(T,x,y)-\hat{\pi}^{2,H}(T,x,y)|=O\left(\mathbb{E}[H\_{T}]^{1-\frac{\alpha}{q-1}}\right),\quad(T\nearrow\infty). |  |

By combining the above theorem with Theorem [2.4](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem4 "Theorem 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), we obtain the convergence rates for the optimal feedback functions π^1=π^1,M+π^1,H\displaystyle\hat{\pi}^{1}=\hat{\pi}^{1,M}+\hat{\pi}^{1,H}.

###### Corollary 2.7.1.

Under Assumptions [2.4](https://arxiv.org/html/2512.00346v1#S2.Thmassumption4 "Assumption 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") and [2.5](https://arxiv.org/html/2512.00346v1#S2.Thmassumption5 "Assumption 2.5. ‣ 2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"),

|  |  |  |
| --- | --- | --- |
|  | |π^1​(T,x,y)−π^2​(T,x,y)|=O​(𝔼​[HT]1−αq−1),(T↗∞).|\hat{\pi}^{1}(T,x,y)-\hat{\pi}^{2}(T,x,y)|=O\left(\mathbb{E}[H\_{T}]^{1-\frac{\alpha}{q-1}}\right),\quad(T\nearrow\infty). |  |

Moreover, by considering portfolio proportions rather than dollar amounts, we can prove the uniform turnpike theorem for excess hedging demands and obtain its convergence rate.

###### Theorem 2.8.

Under Assumptions [2.4](https://arxiv.org/html/2512.00346v1#S2.Thmassumption4 "Assumption 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") and [2.5](https://arxiv.org/html/2512.00346v1#S2.Thmassumption5 "Assumption 2.5. ‣ 2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), for any ϵ>0\displaystyle\epsilon>0,

|  |  |  |
| --- | --- | --- |
|  | supx>ϵ|π^1,H​(T,x,y)x−π^2,H​(T,x,y)x|=O​(𝔼​[HT]1−αq−1),(T↗∞).\sup\_{x>\epsilon}\left|\frac{\hat{\pi}^{1,H}(T,x,y)}{x}-\frac{\hat{\pi}^{2,H}(T,x,y)}{x}\right|=O\left(\mathbb{E}[H\_{T}]^{1-\frac{\alpha}{q-1}}\right),\quad(T\nearrow\infty). |  |

###### Corollary 2.8.1.

Under Assumptions [2.4](https://arxiv.org/html/2512.00346v1#S2.Thmassumption4 "Assumption 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") and [2.5](https://arxiv.org/html/2512.00346v1#S2.Thmassumption5 "Assumption 2.5. ‣ 2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), for any ϵ>0\displaystyle\epsilon>0,

|  |  |  |
| --- | --- | --- |
|  | supx>ϵ|π^1​(T,x,y)x−π^2​(T,x,y)x|=O​(𝔼​[HT]1−αq−1),(T↗∞).\sup\_{x>\epsilon}\left|\frac{\hat{\pi}^{1}(T,x,y)}{x}-\frac{\hat{\pi}^{2}(T,x,y)}{x}\right|=O\left(\mathbb{E}[H\_{T}]^{1-\frac{\alpha}{q-1}}\right),\quad(T\nearrow\infty). |  |

### 2.4 Applications: optimal collective investment problems

In this subsection, we offer applications of our main results to optimal collective investment problems. For detailed descriptions of the problems, see [[2](https://arxiv.org/html/2512.00346v1#bib.bib2), [18](https://arxiv.org/html/2512.00346v1#bib.bib18)], for example. We consider the quadratic term structure model, given by ([7](https://arxiv.org/html/2512.00346v1#S2.E7 "In 2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) and ([8](https://arxiv.org/html/2512.00346v1#S2.E8 "In 2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")), that satisfies Assumptions [2.4](https://arxiv.org/html/2512.00346v1#S2.Thmassumption4 "Assumption 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")(iii) and [2.5](https://arxiv.org/html/2512.00346v1#S2.Thmassumption5 "Assumption 2.5. ‣ 2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") as described in Sect. [2.3](https://arxiv.org/html/2512.00346v1#S2.SS3 "2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"). We assume there are n\displaystyle n investors with CRRA utility functions Ui​(x)≔xpipi,(i=1,…,n),−∞<p1<…​pn≤0\displaystyle U\_{i}(x)\coloneqq\frac{x^{p\_{i}}}{p\_{i}},\;(i=1,\dots,n),\;-\infty<p\_{1}<\dots p\_{n}\leq 0, where the relative risk aversion level of the i\displaystyle i-th investor is given by γi≔1−pi\displaystyle\gamma\_{i}\coloneqq 1-p\_{i}. At the beginning of the investment period (t=0\displaystyle t=0), investors delegate their investment management to a fund manager. At the end of the investment period (t=T\displaystyle t=T), a fund manager distributes the aggregate terminal wealth among n\displaystyle n investors according to a sharing rule. In this paper, we consider two well-known sharing rules: a Pareto optimal sharing rule and a linear sharing rule.

#### 2.4.1 Pareto optimal sharing rule

We assume that a fund manager chooses a Pareto optimal distribution of the terminal wealth, which is represented by

|  |  |  |
| --- | --- | --- |
|  | U~​(x)≔max⁡{∑i=1nβi​Ui​(xi)|xi∈ℝ,∑i=1nxi=x},\tilde{U}(x)\coloneqq\max\left\{\sum\_{i=1}^{n}\beta\_{i}U\_{i}(x\_{i})\left|\;x\_{i}\in\mathbb{R},\;\sum\_{i=1}^{n}x\_{i}=x\right.\right\}, |  |

where βi\displaystyle\beta\_{i} is the weight granted to the i\displaystyle i-th investor and satisfies βi>0,(i=1,…,n),∑i=1nβi=1\displaystyle\beta\_{i}>0,\;(i=1,\dots,n),\;\sum\_{i=1}^{n}\beta\_{i}=1. [[2](https://arxiv.org/html/2512.00346v1#bib.bib2)] uses this utility function to analyze collective investment problems. U~\displaystyle\tilde{U} also appears as a utility function for a representative agent in the context of market equilibrium [[20](https://arxiv.org/html/2512.00346v1#bib.bib20), Chapter 4].
Because the operations of sup-convolution and addition are dual to each other, the inverse marginal utility of a fund manager is given by the sum of those of individuals.

###### Lemma 2.9.

U~\displaystyle\tilde{U} is a utility function in Definition [2.1](https://arxiv.org/html/2512.00346v1#S2.Thmdefinition1 "Definition 2.1. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") and the inverse marginal utility I~≔(U~)−1\displaystyle\tilde{I}\coloneqq(\tilde{U})^{-1} is given by

|  |  |  |
| --- | --- | --- |
|  | I~​(z)=∑i=1nIi​(zβi),Ii​(z)=zqi−1,qi≔pipi−1.\tilde{I}(z)=\sum\_{i=1}^{n}I\_{i}\left(\frac{z}{\beta\_{i}}\right),\quad I\_{i}(z)=z^{q\_{i}-1},\quad q\_{i}\coloneqq\frac{p\_{i}}{p\_{i}-1}. |  |

###### Proof.

See [[2](https://arxiv.org/html/2512.00346v1#bib.bib2), Appendix A].
∎

By using our main results in Sect. [2.3](https://arxiv.org/html/2512.00346v1#S2.SS3 "2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), we can show that the optimal feedback function of a fund manager converges to that of the most risk-seeking investor. The convergence rate is determined by the price of a zero-coupon bond and the relative difference between the relative risk aversion levels of the least risk-averse investor (i=n\displaystyle i=n) and the second least risk-averse investor (i=n−1\displaystyle i=n-1).

###### Theorem 2.10.

Let π^P\displaystyle\hat{\pi}^{P} be the optimal feedback function of a fund manager with the Pareto optimal sharing rule and π^i\displaystyle\hat{\pi}^{i} be that of the i\displaystyle i-th investor. Then

|  |  |  |
| --- | --- | --- |
|  | |π^P​(T,x,y)−π^n​(T,x,y)|=O​(𝔼​[HT]γn−1−γnγn−1),(T↗∞).\left|\hat{\pi}^{P}(T,x,y)-\hat{\pi}^{n}(T,x,y)\right|=O\left(\mathbb{E}[H\_{T}]^{\frac{\gamma\_{n-1}-\gamma\_{n}}{\gamma\_{n-1}}}\right),\quad(T\nearrow\infty). |  |

###### Proof.

It is enough to check that the inequalities ([5](https://arxiv.org/html/2512.00346v1#S2.E5 "In Assumption. ‣ Remark 2.2. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) hold for I1​(z)=I~​(z),I2​(z)=zqn−1,α=qn−1−1,C=(1βn)qn−1\displaystyle I\_{1}(z)=\tilde{I}(z),\;I\_{2}(z)=z^{q\_{n}-1},\;\alpha=q\_{n-1}-1,\;C=\left(\frac{1}{\beta\_{n}}\right)^{q\_{n}-1}. Because 0≤qn<qn−1<⋯<q1<1\displaystyle 0\leq q\_{n}<q\_{n-1}<\dots<q\_{1}<1, there exists some K>0\displaystyle K>0 such that for all z>0\displaystyle z>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |I~​(z)−(zβn)qn−1|\displaystyle\displaystyle\left|\tilde{I}(z)-\left(\frac{z}{\beta\_{n}}\right)^{q\_{n}-1}\right| | =∑i=1n−1(zβi)qi−1\displaystyle\displaystyle=\sum\_{i=1}^{n-1}\left(\frac{z}{\beta\_{i}}\right)^{q\_{i}-1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤K​(1+zqn−1−1)\displaystyle\displaystyle\leq K(1+z^{q\_{n-1}-1}) |  |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | |z​I~′​(z)−(qn−1)​(zβn)qn−1|\displaystyle\displaystyle\left|z\tilde{I}^{\prime}(z)-(q\_{n}-1)\left(\frac{z}{\beta\_{n}}\right)^{q\_{n}-1}\right| | =∑i=1n−1(1−qi)​(zβi)qi−1\displaystyle\displaystyle=\sum\_{i=1}^{n-1}(1-q\_{i})\left(\frac{z}{\beta\_{i}}\right)^{q\_{i}-1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤K​(1+zqn−1−1)\displaystyle\displaystyle\leq K(1+z^{q\_{n-1}-1}) |  |

hold. Moreover, the identity

|  |  |  |
| --- | --- | --- |
|  | αq−1=qn−1−1qn−1=1−pn1−pn−1=γnγn−1\displaystyle\displaystyle\frac{\alpha}{q-1}=\frac{q\_{n-1}-1}{q\_{n}-1}=\frac{1-p\_{n}}{1-p\_{n-1}}=\frac{\gamma\_{n}}{\gamma\_{n-1}} |  |

gives the convergence rate.
∎

#### 2.4.2 Linear sharing rule

Here, we assume that a fund manager allocates the terminal wealth according to a linear sharing rule, where the i\displaystyle i-th investor receives a fixed proportion αi\displaystyle\alpha\_{i} of the terminal wealth. This linear sharing rule is represented by

|  |  |  |
| --- | --- | --- |
|  | U​(x)≔∑i=1nβi​Ui​(αi​x),U(x)\coloneqq\sum\_{i=1}^{n}\beta\_{i}U\_{i}(\alpha\_{i}x), |  |

where αi,βi>0,(i=1,…,n),∑i=1nαi=∑i=1nβi=1\displaystyle\alpha\_{i},\;\beta\_{i}>0,\;(i=1,\dots,n),\;\sum\_{i=1}^{n}\alpha\_{i}=\sum\_{i=1}^{n}\beta\_{i}=1.
Although U\displaystyle U seems simpler than U~\displaystyle\tilde{U}, we cannot derive the inverse marginal utility of U\displaystyle U in general. Therefore, to estimate the differences between inverse marginal utilities and their derivatives, we perform complex calculations; for the proof, see Sect. [3.4](https://arxiv.org/html/2512.00346v1#S3.SS4 "3.4 Proofs for Sect. 2.4 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models").

###### Proposition 2.11.

Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | U1​(x)\displaystyle\displaystyle U\_{1}(x) | ≔∑i=1nβi​(αi​x)pipi=∑i=1nwi​xpipi,\displaystyle\displaystyle\coloneqq\sum\_{i=1}^{n}\beta\_{i}\frac{(\alpha\_{i}x)^{p\_{i}}}{p\_{i}}=\sum\_{i=1}^{n}w\_{i}\frac{x^{p\_{i}}}{p\_{i}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | U2​(x)\displaystyle\displaystyle U\_{2}(x) | ≔wn​xpnpn,\displaystyle\displaystyle\coloneqq w\_{n}\frac{x^{p\_{n}}}{p\_{n}}, |  |

where wi≔βi​αipi>0\displaystyle w\_{i}\coloneqq\beta\_{i}\alpha\_{i}^{p\_{i}}>0.
For any nonnegative β∈(1+pn−1−pn,1)\displaystyle\beta\in(1+p\_{n-1}-p\_{n},1), there exists K>0\displaystyle K>0 such that for all z>0\displaystyle z>0,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |I1​(z)−I2​(z)|\displaystyle\displaystyle|I\_{1}(z)-I\_{2}(z)| | ≤K​(1+zβ​(qn−1)),\displaystyle\displaystyle\leq K(1+z^{\beta(q\_{n}-1)}), |  | (9) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |z​I1′​(z)−z​I2′​(z)|\displaystyle\displaystyle|zI\_{1}^{\prime}(z)-zI\_{2}^{\prime}(z)| | ≤K​(1+zβ​(qn−1))\displaystyle\displaystyle\leq K(1+z^{\beta(q\_{n}-1)}) |  | (10) |

hold.

###### Theorem 2.12.

Let π^L\displaystyle\hat{\pi}^{L} be the optimal feedback function of a fund manager with the linear sharing rule and π^i\displaystyle\hat{\pi}^{i} be that of the i\displaystyle i-th investor. Then for any nonnegative β∈(1+pn−1−pn,1)\displaystyle\beta\in(1+p\_{n-1}-p\_{n},1),

|  |  |  |
| --- | --- | --- |
|  | |π^L​(T,x,y)−π^n​(T,x,y)|=O​(𝔼​[HT]1−β),(T↗∞)\left|\hat{\pi}^{L}(T,x,y)-\hat{\pi}^{n}(T,x,y)\right|=O\left(\mathbb{E}[H\_{T}]^{1-\beta}\right),\quad(T\nearrow\infty) |  |

holds.

###### Proof.

By Proposition [2.11](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem11 "Proposition 2.11. ‣ 2.4.2 Linear sharing rule ‣ 2.4 Applications: optimal collective investment problems ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") and the main results in Sects. [2.2](https://arxiv.org/html/2512.00346v1#S2.SS2 "2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") and [2.3](https://arxiv.org/html/2512.00346v1#S2.SS3 "2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), the convergence rate is given by

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[HT]1−β​(qn−1)qn−1=𝔼​[HT]1−β.\mathbb{E}[H\_{T}]^{1-\frac{\beta(q\_{n}-1)}{q\_{n}-1}}=\mathbb{E}[H\_{T}]^{1-\beta}. |  |

∎

###### Remark 2.12.

If 1+pn−1−pn≥0\displaystyle 1+p\_{n-1}-p\_{n}\geq 0, which is equivalent to γn−1≤γn+1\displaystyle\gamma\_{n-1}\leq\gamma\_{n}+1 in terms of relative risk aversion levels γi\displaystyle\gamma\_{i}, then the convergence rate is given by O​(𝔼​[HT]γn−1−γn−ϵ)\displaystyle O(\mathbb{E}[H\_{T}]^{\gamma\_{n-1}-\gamma\_{n}-\epsilon}) for any ϵ>0\displaystyle\epsilon>0. If 1+pn−1−pn<0\displaystyle 1+p\_{n-1}-p\_{n}<0, which is equivalent to γn−1>γn+1\displaystyle\gamma\_{n-1}>\gamma\_{n}+1, then the convergence rate is given by O​(𝔼​[HT])\displaystyle O(\mathbb{E}[H\_{T}]). These facts mean that for a fund manager with a linear sharing rule, the convergence rate is determined by γn−1−γn\displaystyle\gamma\_{n-1}-\gamma\_{n}, the absolute difference between the relative risk aversion levels of the least risk-averse investor and the second least risk-averse investor. On the other hand, for a fund manager with a Pareto optimal sharing rule, the convergence rate is determined by γn−1−γnγn−1\displaystyle\frac{\gamma\_{n-1}-\gamma\_{n}}{\gamma\_{n-1}}, the relative difference between the relative risk aversion levels for the same investors. In particular, because we consider the case γn−1>1\displaystyle\gamma\_{n-1}>1, the convergence rate under a linear sharing rule is faster than that under a Pareto optimal sharing rule.

## 3 Proofs for main results

### 3.1 Proofs for Sect. [2.1](https://arxiv.org/html/2512.00346v1#S2.SS1 "2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")

The following lemma is used in the proof of Theorem [2.1](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") and Lemma [3.6](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem6 "Lemma 3.6. ‣ 3.1 Proofs for Sect. 2.1 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), which shows HT∈𝔻1,1\displaystyle H\_{T}\in\mathbb{D}\_{1,1}.

###### Lemma 3.1.

Under Assumptions [2.1](https://arxiv.org/html/2512.00346v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") and [2.2](https://arxiv.org/html/2512.00346v1#S2.Thmassumption2 "Assumption 2.2. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), for any T>0,λ≥0,y∈ℝm\displaystyle T>0,\;\lambda\geq 0,\;y\in\mathbb{R}^{m},

|  |  |  |
| --- | --- | --- |
|  | 𝔼yℚ​[exp⁡(−λ​∫0Tr​(Yt)​𝑑t)]<∞.\mathbb{E}^{\mathbb{Q}}\_{y}\left[\exp\left(-\lambda\int\_{0}^{T}r(Y\_{t})dt\right)\right]<\infty. |  |

###### Proof.

We fix T>0,y∈ℝm\displaystyle T>0,\;y\in\mathbb{R}^{m} and for any λ≥0\displaystyle\lambda\geq 0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼yℚ​[exp⁡(−λ​∫0Tr​(Yt)​𝑑t)]\displaystyle\displaystyle\mathbb{E}^{\mathbb{Q}}\_{y}\left[\exp\left(-\lambda\int\_{0}^{T}r(Y\_{t})dt\right)\right] | ≤𝔼yℚ​[1T​∫0Texp⁡(−λ​T​r​(Yt))​𝑑t]\displaystyle\displaystyle\leq\mathbb{E}^{\mathbb{Q}}\_{y}\left[\frac{1}{T}\int\_{0}^{T}\exp\left(-\lambda Tr(Y\_{t})\right)dt\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤supt∈[0,T]𝔼yℚ​[exp⁡(−λ​T​r​(Yt))]\displaystyle\displaystyle\leq\sup\_{t\in[0,T]}\mathbb{E}^{\mathbb{Q}}\_{y}\left[\exp\left(-\lambda Tr(Y\_{t})\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤supt∈[0,T]𝔼yℚ​[exp⁡(−λ​T​(r0+r1⊤​Yt))]\displaystyle\displaystyle\leq\sup\_{t\in[0,T]}\mathbb{E}^{\mathbb{Q}}\_{y}\left[\exp\left(-\lambda T\left(r\_{0}+r\_{1}^{\top}Y\_{t}\right)\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =exp⁡(−λ​T​r0)​supt∈[0,T]𝔼yℚ​[exp⁡(−λ​T​r1⊤​Yt)]\displaystyle\displaystyle=\exp\left(-\lambda Tr\_{0}\right)\sup\_{t\in[0,T]}\mathbb{E}^{\mathbb{Q}}\_{y}\left[\exp\left(-\lambda Tr\_{1}^{\top}Y\_{t}\right)\right] |  |

holds, where the first inequality follows from Jensen’s inequality, and the third inequality follows from Assumption [2.2](https://arxiv.org/html/2512.00346v1#S2.Thmassumption2 "Assumption 2.2. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")(i). Therefore, it suffices to prove that for any λ≥0\displaystyle\lambda\geq 0,

|  |  |  |
| --- | --- | --- |
|  | supt∈[0,T]𝔼yℚ​[exp⁡(λ​|Yt|)]\sup\_{t\in[0,T]}\mathbb{E}^{\mathbb{Q}}\_{y}\left[\exp\left(\lambda|Y\_{t}|\right)\right] |  |

holds. Because Y\displaystyle Y satisfies the following SDE under ℚ\displaystyle\mathbb{Q},

|  |  |  |
| --- | --- | --- |
|  | Yt=y+∫0tb~​(Ys)​𝑑s+∫0ta​(Ys)​𝑑Wsℚ,Y\_{t}=y+\int\_{0}^{t}\tilde{b}(Y\_{s})ds+\int\_{0}^{t}a(Y\_{s})dW^{\mathbb{Q}}\_{s}, |  |

and b~​(y)=b​(y)−a​(y)​θ​(y)\displaystyle\tilde{b}(y)=b(y)-a(y)\theta(y) is of linear growth,
|Yt|\displaystyle|Y\_{t}| satisfies

|  |  |  |
| --- | --- | --- |
|  | |Yt|≤|y|+K​T+supt∈[0,T]|Mt|+∫0tK​|Ys|​𝑑s,|Y\_{t}|\leq|y|+KT+\sup\_{t\in[0,T]}|M\_{t}|+\int\_{0}^{t}K|Y\_{s}|ds, |  |

where K\displaystyle K is a some constant and Mt≔∫0ta​(Ys)​𝑑Wsℚ\displaystyle M\_{t}\coloneqq\int\_{0}^{t}a(Y\_{s})dW^{\mathbb{Q}}\_{s}. By Gronwall’s inequality,

|  |  |  |
| --- | --- | --- |
|  | |Yt|≤(|y|+K​T+supt∈[0,T]|Mt|)​exp⁡(K​T)|Y\_{t}|\leq\left(|y|+KT+\sup\_{t\in[0,T]}|M\_{t}|\right)\exp(KT) |  |

holds, which leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | exp⁡(λ​|Yt|)\displaystyle\displaystyle\exp\left(\lambda|Y\_{t}|\right) | ≤exp⁡{λ​(|y|+K​T+supt∈[0,T]|Mt|)​exp⁡(K​T)}\displaystyle\displaystyle\leq\exp\left\{\lambda\left(|y|+KT+\sup\_{t\in[0,T]}|M\_{t}|\right)\exp(KT)\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =C1​exp⁡(C2​supt∈[0,T]|Mt|)(C1≔exp⁡{λ​(|y|+K​T)​exp⁡(K​T)},C2≔λ​exp⁡(K​T))\displaystyle\displaystyle=C\_{1}\exp\left(C\_{2}\sup\_{t\in[0,T]}|M\_{t}|\right)\quad\left(C\_{1}\coloneqq\exp\{\lambda(|y|+KT)\exp(KT)\},\quad C\_{2}\coloneqq\lambda\exp(KT)\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C1​exp⁡(C2​∑i=1msupt∈[0,T]|Mti|)\displaystyle\displaystyle\leq C\_{1}\exp\left(C\_{2}\sum\_{i=1}^{m}\sup\_{t\in[0,T]}|M^{i}\_{t}|\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∑i=1mC1​exp⁡(m​C2​supt∈[0,T]|Mti|).\displaystyle\displaystyle\leq\sum\_{i=1}^{m}C\_{1}\exp\left(mC\_{2}\sup\_{t\in[0,T]}|M^{i}\_{t}|\right). |  |

As a result, it suffices to show that for any λ≥0,i=1,…,m\displaystyle\lambda\geq 0,\;i=1,\dots,m,

|  |  |  |
| --- | --- | --- |
|  | 𝔼yℚ​[exp⁡(λ​supt∈[0,T]|Mti|)]<∞\mathbb{E}^{\mathbb{Q}}\_{y}\left[\exp\left(\lambda\sup\_{t\in[0,T]}|M^{i}\_{t}|\right)\right]<\infty |  |

holds. The Dambis–Dubins–Schwarz theorem implies that there exists a Brownian motion βi\displaystyle\beta^{i} such that Mti=β⟨M⟩ti\displaystyle M^{i}\_{t}=\beta^{i}\_{\langle M\rangle\_{t}}, and because a\displaystyle a is bounded [Assumption [2.1](https://arxiv.org/html/2512.00346v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")(iv)], there exists a constant L\displaystyle L such that ⟨M⟩T≤L​T\displaystyle\langle M\rangle\_{T}\leq LT holds. Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼yℚ​[exp⁡(λ​supt∈[0,T]|Mti|)]\displaystyle\displaystyle\mathbb{E}^{\mathbb{Q}}\_{y}\left[\exp\left(\lambda\sup\_{t\in[0,T]}|M^{i}\_{t}|\right)\right] | =𝔼yℚ​[exp⁡(λ​supt∈[0,T]|β⟨M⟩ti|)]\displaystyle\displaystyle=\mathbb{E}^{\mathbb{Q}}\_{y}\left[\exp\left(\lambda\sup\_{t\in[0,T]}|\beta^{i}\_{\langle M\rangle\_{t}}|\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼yℚ​[exp⁡(λ​supt∈[0,L​T]|βti|)]\displaystyle\displaystyle\leq\mathbb{E}^{\mathbb{Q}}\_{y}\left[\exp\left(\lambda\sup\_{t\in[0,LT]}|\beta^{i}\_{t}|\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | <∞,\displaystyle\displaystyle<\infty, |  |

which completes the proof.
∎

###### Proof of Theorem [2.1](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models").

By [[20](https://arxiv.org/html/2512.00346v1#bib.bib20), Theorem 3.7.6], it suffices to check that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[HT]<∞,𝔼​[HT​I​(z​HT)]\mathbb{E}[H\_{T}]<\infty,\quad\mathbb{E}[H\_{T}I(zH\_{T})] |  |

for any z>0\displaystyle z>0. By Lemma [3.1](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem1 "Lemma 3.1. ‣ 3.1 Proofs for Sect. 2.1 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"),

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[HT]=𝔼ℚ​[exp⁡(−∫0Tr​(Yt)​𝑑t)]<∞.\displaystyle\displaystyle\mathbb{E}[H\_{T}]=\mathbb{E}^{\mathbb{Q}}\left[\exp\left(-\int\_{0}^{T}r(Y\_{t})dt\right)\right]<\infty. |  |

By Assumption [2.2](https://arxiv.org/html/2512.00346v1#S2.Thmassumption2 "Assumption 2.2. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")(ii),

|  |  |  |
| --- | --- | --- |
|  | HT​I​(z​HT)≤κ​(HT+z−ρ​HT1−ρ)\displaystyle\displaystyle H\_{T}I(zH\_{T})\leq\kappa\left(H\_{T}+z^{-\rho}H\_{T}^{1-\rho}\right) |  |

holds, and by Jensen’s inequality,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[HT​I​(z​HT)]\displaystyle\displaystyle\mathbb{E}[H\_{T}I(zH\_{T})] | ≤κ​(𝔼​[HT]+z−ρ​𝔼​[HT1−ρ])\displaystyle\displaystyle\leq\kappa\left(\mathbb{E}[H\_{T}]+z^{-\rho}\mathbb{E}\left[H\_{T}^{1-\rho}\right]\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤κ​(𝔼​[HT]+z−ρ​𝔼​[HT]1−ρ)\displaystyle\displaystyle\leq\kappa\left(\mathbb{E}[H\_{T}]+z^{-\rho}\mathbb{E}\left[H\_{T}\right]^{1-\rho}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | <∞\displaystyle\displaystyle<\infty |  |

holds, which completes the proof.
∎

Throughout this subsection, we assume Assumptions [2.1](https://arxiv.org/html/2512.00346v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")–[2.3](https://arxiv.org/html/2512.00346v1#S2.Thmassumption3 "Assumption 2.3. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models").
From Proposition [A.5](https://arxiv.org/html/2512.00346v1#A1.Thmtheorem5 "Proposition A.5. ‣ Appendix A Appendix: Malliavin calculus ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") and Assumption [2.3](https://arxiv.org/html/2512.00346v1#S2.Thmassumption3 "Assumption 2.3. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")(ii), the following holds.

###### Lemma 3.2.

Y=(Y1,…,Ym)\displaystyle Y=(Y^{1},\dots,Y^{m}) satisfies the following.

* (i)

  Ysk∈⋂p≥1𝔻p,1,k=1,…,m,s∈[0,T]\displaystyle Y^{k}\_{s}\in\bigcap\_{p\geq 1}\mathbb{D}\_{p,1},\quad k=1,\dots,m,\;s\in[0,T].
* (ii)

  Dt​Ys\displaystyle D\_{t}Y\_{s} satisfies

  |  |  |  |
  | --- | --- | --- |
  |  | Dt​Ys=a​(Yt)+∫tsD​b​(Yu)​Dt​Yu​𝑑u+∑l=1n∫tsD​a⋅l​(Yu)​Dt​Yu​𝑑WulD\_{t}Y\_{s}=a(Y\_{t})+\int\_{t}^{s}Db(Y\_{u})D\_{t}Y\_{u}du+\sum\_{l=1}^{n}\int\_{t}^{s}Da\_{\cdot l}(Y\_{u})D\_{t}Y\_{u}dW^{l}\_{u} |  |

  for t∈[0,s]\displaystyle t\in[0,s] and Dt​Ys=0\displaystyle D\_{t}Y\_{s}=0 for t∈(s,T]\displaystyle t\in(s,T].
* (iii)

  For j=1,…,n,p∈[1,∞),\displaystyle j=1,\dots,n,\;p\in[1,\infty),

  |  |  |  |
  | --- | --- | --- |
  |  | supr∈[0,T]𝔼​[sups∈[0,T]|Drj​Ysk|p]<∞.\sup\_{r\in[0,T]}\mathbb{E}\left[\sup\_{s\in[0,T]}\left|D^{j}\_{r}Y^{k}\_{s}\right|^{p}\right]<\infty. |  |
* (iv)

  Dt​Ys=∇yYs​(∇yYt)−1​a​(Yt)\displaystyle D\_{t}Y\_{s}=\nabla\_{y}Y\_{s}(\nabla\_{y}Y\_{t})^{-1}a(Y\_{t}) for t∈[0,s]\displaystyle t\in[0,s], where ∇yY\displaystyle\nabla\_{y}Y is an ℝm×m\displaystyle\mathbb{R}^{m\times m}-valued stochastic process satisfying

  |  |  |  |
  | --- | --- | --- |
  |  | ∇yYs=I+∫0sD​b​(Yu)​∇yYu​d​u+∑j=1n∫tsD​a⋅j​(Yu)​∇yYu​d​Wuj\nabla\_{y}Y\_{s}=I+\int\_{0}^{s}Db(Y\_{u})\nabla\_{y}Y\_{u}du+\sum\_{j=1}^{n}\int\_{t}^{s}Da\_{\cdot j}(Y\_{u})\nabla\_{y}Y\_{u}dW^{j}\_{u} |  |

  for s∈[0,T]\displaystyle s\in[0,T] and I∈ℝm×m\displaystyle I\in\mathbb{R}^{m\times m} is the identity matrix.

###### Lemma 3.3.

For s,t∈[0,T]\displaystyle s,t\in[0,T],

* (i)

  Ds​(r​(Yt))=D​r​(Yt)​Ds​Yt\displaystyle D\_{s}(r(Y\_{t}))=Dr(Y\_{t})D\_{s}Y\_{t},
* (ii)

  Ds​(θ​(Yt))=D​θ​(Yt)​Ds​Yt\displaystyle D\_{s}(\theta(Y\_{t}))=D\theta(Y\_{t})D\_{s}Y\_{t},
* (iii)

  Ds​(12​|θ​(Yt)|2)=θ⊤​(Yt)​D​θ​(Yt)​Ds​Yt\displaystyle D\_{s}\left(\frac{1}{2}|\theta(Y\_{t})|^{2}\right)=\theta^{\top}(Y\_{t})D\theta(Y\_{t})D\_{s}Y\_{t},
* (iv)

  Ds​∫0Tr​(Yt)​𝑑t=∫sTD​r​(Yt)​Ds​Yt​𝑑t\displaystyle D\_{s}\int\_{0}^{T}r(Y\_{t})dt=\int\_{s}^{T}Dr(Y\_{t})D\_{s}Y\_{t}dt,
* (v)

  Ds​(12​∫0T|θ​(Yt)|2​𝑑t)=∫sTθ⊤​(Yt)​D​θ​(Yt)​Ds​Yt​𝑑t\displaystyle D\_{s}\left(\frac{1}{2}\int\_{0}^{T}|\theta(Y\_{t})|^{2}dt\right)=\int\_{s}^{T}\theta^{\top}(Y\_{t})D\theta(Y\_{t})D\_{s}Y\_{t}dt,
* (vi)

  Ds​∫0Tθ⊤​(Yt)​𝑑Wt=θ⊤​(Ys)+(∫sT(D​θ​(Yt)​Ds​Yt)⊤​𝑑Wt)⊤\displaystyle D\_{s}\int\_{0}^{T}\theta^{\top}(Y\_{t})dW\_{t}=\theta^{\top}(Y\_{s})+\left(\int\_{s}^{T}(D\theta(Y\_{t})D\_{s}Y\_{t})^{\top}dW\_{t}\right)^{\top}.

###### Proof.

(i), (ii), and (iii) follow from Proposition [A.2](https://arxiv.org/html/2512.00346v1#A1.Thmtheorem2 "Proposition A.2. ‣ Appendix A Appendix: Malliavin calculus ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") with the remark below it, Lemma [3.2](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3.1 Proofs for Sect. 2.1 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), and Assumption [2.3](https://arxiv.org/html/2512.00346v1#S2.Thmassumption3 "Assumption 2.3. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")(i) that r,θ,D​r,D​θ\displaystyle r,\theta,Dr,D\theta are of polynomial growth. (iv) and (v) follow from Proposition [A.3](https://arxiv.org/html/2512.00346v1#A1.Thmtheorem3 "Proposition A.3. ‣ Appendix A Appendix: Malliavin calculus ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), and (vi) follows from Proposition [A.4](https://arxiv.org/html/2512.00346v1#A1.Thmtheorem4 "Proposition A.4. ‣ Appendix A Appendix: Malliavin calculus ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models").
∎

The following lemma implies finiteness for p\displaystyle p-th moments of supt∈[0,T]|Yt|\displaystyle\sup\_{t\in[0,T]}|Y\_{t}| and |Dt​Ys|\displaystyle|D\_{t}Y\_{s}| under the equivalent martingale measure ℚ\displaystyle\mathbb{Q}. In this lemma, we use (iii) of Assumption [2.3](https://arxiv.org/html/2512.00346v1#S2.Thmassumption3 "Assumption 2.3. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), which is a monotone condition for SDE ([12](https://arxiv.org/html/2512.00346v1#S3.E12 "In item (ii) ‣ 3.1 Proofs for Sect. 2.1 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) that (Ys,Dt1​Ys,…​Dtn​Ys)s∈[t,T]\displaystyle(Y\_{s},D^{1}\_{t}Y\_{s},\dots D^{n}\_{t}Y\_{s})\_{s\in[t,T]} satisfies under ℚ\displaystyle\mathbb{Q}.

###### Lemma 3.4.

For any p∈[1,∞)\displaystyle p\in[1,\infty),

1. (i)

   𝔼ℚ​[sups∈[0,T]|Ys|p]<∞,\displaystyle\mathbb{E}^{\mathbb{Q}}[\sup\_{s\in[0,T]}|Y\_{s}|^{p}]<\infty,
2. (ii)

   sups,t∈[0,T]𝔼ℚ​[|Dt​Ys|p]<∞.\displaystyle\sup\_{s,t\in[0,T]}\mathbb{E}^{\mathbb{Q}}[|D\_{t}Y\_{s}|^{p}]<\infty.

###### Proof.

1. (i)

   Y=(Yt)t∈[0,T]\displaystyle Y=(Y\_{t})\_{t\in[0,T]} satisfies

   |  |  |  |  |  |
   | --- | --- | --- | --- | --- |
   |  | d​Ys\displaystyle dY\_{s} | =b​(Ys)​d​s+a​(Ys)​d​Ws\displaystyle=b(Y\_{s})ds+a(Y\_{s})dW\_{s} |  | (11) |
   |  |  | ={b​(Ys)−a​(Ys)​θ​(Ys)}​d​s+a​(Ys)​d​Wsℚ.\displaystyle=\left\{b(Y\_{s})-a(Y\_{s})\theta(Y\_{s})\right\}ds+a(Y\_{s})dW^{\mathbb{Q}}\_{s}. |  |

   Because b\displaystyle b and θ\displaystyle\theta have linear growth and a\displaystyle a is bounded, SDE ([11](https://arxiv.org/html/2512.00346v1#S3.E11 "In item (i) ‣ 3.1 Proofs for Sect. 2.1 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) satisfies a linear growth condition and (i) follows from Theorem 4.4 in [[29](https://arxiv.org/html/2512.00346v1#bib.bib29), Chapter 2].
2. (ii)

   Let t∈[0,T]\displaystyle t\in[0,T].
   ℝm\displaystyle\mathbb{R}^{m}-valued stochastic processes (Dtj​Ys)s∈[t,T],j=1,…,n\displaystyle(D^{j}\_{t}Y\_{s})\_{s\in[t,T]},\;j=1,\dots,n satisfy

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Dtj​Ys\displaystyle D^{j}\_{t}Y\_{s} | =a⋅j​(Yt)+∫tsD​b​(Yu)​Dtj​Yu​𝑑u+∑l=1n∫tsD​a⋅l​(Yu)​Dtj​Yu​𝑑Wul\displaystyle=a\_{\cdot j}(Y\_{t})+\int\_{t}^{s}Db(Y\_{u})D^{j}\_{t}Y\_{u}du+\sum\_{l=1}^{n}\int\_{t}^{s}Da\_{\cdot l}(Y\_{u})D^{j}\_{t}Y\_{u}dW^{l}\_{u} |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | =a⋅j​(Yt)+∫ts(D​b​(Yu)−∑l=1nD​a⋅l​(Yu)​θl​(Yu))​Dtj​Yu​𝑑u+∑l=1n∫tsD​a⋅l​(Yu)​Dtj​Yu​𝑑Wuℚ,l.\displaystyle=a\_{\cdot j}(Y\_{t})+\int\_{t}^{s}\left(Db(Y\_{u})-\sum\_{l=1}^{n}Da\_{\cdot l}(Y\_{u})\theta^{l}(Y\_{u})\right)D^{j}\_{t}Y\_{u}du+\sum\_{l=1}^{n}\int\_{t}^{s}Da\_{\cdot l}(Y\_{u})D^{j}\_{t}Y\_{u}dW^{\mathbb{Q},l}\_{u}. |  |

   Set 𝕐=(Ys,Dt1​Ys,…​Dtn​Ys)s∈[t,T]⊤\displaystyle\mathbb{Y}=(Y\_{s},D^{1}\_{t}Y\_{s},\dots D^{n}\_{t}Y\_{s})^{\top}\_{s\in[t,T]}. Then, ℝm​(n+1)\displaystyle\mathbb{R}^{m(n+1)}-valued stochastic process 𝕐\displaystyle\mathbb{Y} satisfies

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | d​𝕐s=B​(𝕐s)​d​s+∑l=1nAl​(𝕐s)​d​Wsℚ,l,d\mathbb{Y}\_{s}=B(\mathbb{Y}\_{s})ds+\sum\_{l=1}^{n}A^{l}(\mathbb{Y}\_{s})dW^{\mathbb{Q},l}\_{s}, |  | (12) |

   with 𝕐t=(Yt,a⋅1​(Yt),…,a⋅n​(Yt))⊤\displaystyle\mathbb{Y}\_{t}=(Y\_{t},a\_{\cdot 1}(Y\_{t}),\dots,a\_{\cdot n}(Y\_{t}))^{\top}, where B,Al:ℝm​(n+1)→ℝm​(n+1),l=1,…,n\displaystyle B,A^{l}:\mathbb{R}^{m(n+1)}\to\mathbb{R}^{m(n+1)},\;l=1,\dots,n are given by

   |  |  |  |
   | --- | --- | --- |
   |  | B​(y,z1,…,zn)=(b​(y)−a​(y)​θ​(y)(D​b​(y)−∑l=1nD​a⋅l​(y)​θl​(y))​z1⋮(D​b​(y)−∑l=1nD​a⋅l​(y)​θl​(y))​zn),Al​(y,z1,…,zn)=(a⋅l​(y)D​a⋅l​(y)​z1⋮D​a⋅l​(y)​zn)\displaystyle\displaystyle B(y,z\_{1},\dots,z\_{n})=\begin{pmatrix}b(y)-a(y)\theta(y)\\ \left(Db(y)-\sum\_{l=1}^{n}Da\_{\cdot l}(y)\theta^{l}(y)\right)z\_{1}\\ \vdots\\ \left(Db(y)-\sum\_{l=1}^{n}Da\_{\cdot l}(y)\theta^{l}(y)\right)z\_{n}\end{pmatrix},\quad A^{l}(y,z\_{1},\dots,z\_{n})=\begin{pmatrix}a\_{\cdot l}(y)\\ Da\_{\cdot l}(y)z\_{1}\\ \vdots\\ Da\_{\cdot l}(y)z\_{n}\\ \end{pmatrix} |  |

   for y,z1​…,zn∈ℝm\displaystyle y,z\_{1}\dots,z\_{n}\in\mathbb{R}^{m}. By Assumption [2.3](https://arxiv.org/html/2512.00346v1#S2.Thmassumption3 "Assumption 2.3. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")(iii), SDE ([12](https://arxiv.org/html/2512.00346v1#S3.E12 "In item (ii) ‣ 3.1 Proofs for Sect. 2.1 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) satisfies a monotone condition, which leads to

   |  |  |  |
   | --- | --- | --- |
   |  | 𝔼ℚ​[|Ds​Yt|p]≤C​(1+𝔼ℚ​[|Yt|p])\mathbb{E}^{\mathbb{Q}}[|D\_{s}Y\_{t}|^{p}]\leq C(1+\mathbb{E}^{\mathbb{Q}}[|Y\_{t}|^{p}]) |  |

   from Theorem 4.1 in [[29](https://arxiv.org/html/2512.00346v1#bib.bib29), Chapter 2], where C>0\displaystyle C>0 does not depend on s,t\displaystyle s,t. Using (i) in this lemma, we complete the proof.

∎

###### Lemma 3.5.

Let L~=(L~s)s∈[0,T]\displaystyle\tilde{L}=(\tilde{L}\_{s})\_{s\in[0,T]} be given by

|  |  |  |
| --- | --- | --- |
|  | L~s≔∫sTD​r​(Yt)​Ds​Yt​𝑑t+θ⊤​(Ys)+(∫sT(D​θ​(Yt)​Ds​Yt)⊤​𝑑Wt)⊤+∫sTθ⊤​(Yt)​D​θ​(Yt)​Ds​Yt​𝑑t,s∈[0,T].\tilde{L}\_{s}\coloneqq\int\_{s}^{T}Dr(Y\_{t})D\_{s}Y\_{t}dt+\theta^{\top}(Y\_{s})+\left(\int\_{s}^{T}(D\theta(Y\_{t})D\_{s}Y\_{t})^{\top}dW\_{t}\right)^{\top}+\int\_{s}^{T}\theta^{\top}(Y\_{t})D\theta(Y\_{t})D\_{s}Y\_{t}dt,\quad s\in[0,T]. |  |

Then

|  |  |  |
| --- | --- | --- |
|  | sups∈[0,T]𝔼ℚ​[|L~s|2]<∞.\sup\_{s\in[0,T]}\mathbb{E}^{\mathbb{Q}}[|\tilde{L}\_{s}|^{2}]<\infty. |  |

###### Proof.

Using the assumption that D​r,θ,D​θ\displaystyle Dr,\theta,D\theta are of polynomial growth and Lemma [3.4](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem4 "Lemma 3.4. ‣ 3.1 Proofs for Sect. 2.1 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), we can easily prove this lemma.
∎

###### Lemma 3.6.

1. (i)

   HT∈𝔻1,1\displaystyle H\_{T}\in\mathbb{D}\_{1,1} and

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | Ds​HT\displaystyle\displaystyle D\_{s}H\_{T} | =−HT​(∫sTD​r​(Yt)​Ds​Yt​𝑑t+θ⊤​(Ys)+(∫sT(D​θ​(Yt)​Ds​Yt)⊤​𝑑Wt)⊤+∫sTθ⊤​(Yt)​D​θ​(Yt)​Ds​Yt​𝑑t)\displaystyle\displaystyle=-H\_{T}\left(\int\_{s}^{T}Dr(Y\_{t})D\_{s}Y\_{t}dt+\theta^{\top}(Y\_{s})+\left(\int\_{s}^{T}(D\theta(Y\_{t})D\_{s}Y\_{t})^{\top}dW\_{t}\right)^{\top}+\int\_{s}^{T}\theta^{\top}(Y\_{t})D\theta(Y\_{t})D\_{s}Y\_{t}dt\right) |  |
   |  |  |  |  |
   | --- | --- | --- | --- |
   |  |  | =−HT​L~s.\displaystyle\displaystyle=-H\_{T}\tilde{L}\_{s}. |  |
2. (ii)

   Let z>0\displaystyle z>0. HT​I​(z​HT)∈𝔻1,1\displaystyle H\_{T}I(zH\_{T})\in\mathbb{D}\_{1,1} and

   |  |  |  |
   | --- | --- | --- |
   |  | Ds​(HT​I​(z​HT))=−HT​L~s​(I​(z​HT)+z​HT​I′​(z​HT)).\displaystyle\displaystyle D\_{s}\left(H\_{T}I(zH\_{T})\right)=-H\_{T}\tilde{L}\_{s}(I(zH\_{T})+zH\_{T}I^{\prime}(zH\_{T})). |  |

###### Proof.

* (i)

  From Lemmas [3.1](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem1 "Lemma 3.1. ‣ 3.1 Proofs for Sect. 2.1 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") and [3.5](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem5 "Lemma 3.5. ‣ 3.1 Proofs for Sect. 2.1 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"),

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | 𝔼​[(∫0T|HT​L~s|2​𝑑s)12]\displaystyle\displaystyle\mathbb{E}\left[\left(\int\_{0}^{T}|H\_{T}\tilde{L}\_{s}|^{2}ds\right)^{\frac{1}{2}}\right] | =𝔼ℚ​[βT​(∫0T|L~s|2​𝑑s)12]\displaystyle\displaystyle=\mathbb{E}^{\mathbb{Q}}\left[\beta\_{T}\left(\int\_{0}^{T}|\tilde{L}\_{s}|^{2}ds\right)^{\frac{1}{2}}\right] |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | ≤𝔼ℚ​[βT2]12​(∫0T𝔼ℚ​[|L~s|2]​𝑑s)12\displaystyle\displaystyle\leq\mathbb{E}^{\mathbb{Q}}\left[\beta\_{T}^{2}\right]^{\frac{1}{2}}\left(\int\_{0}^{T}\mathbb{E}^{\mathbb{Q}}\left[|\tilde{L}\_{s}|^{2}\right]ds\right)^{\frac{1}{2}} |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | ≤𝔼ℚ​[βT2]12​(T⋅sups∈[0,T]𝔼ℚ​[|L~s|2])12\displaystyle\displaystyle\leq\mathbb{E}^{\mathbb{Q}}\left[\beta\_{T}^{2}\right]^{\frac{1}{2}}\left(T\cdot\sup\_{s\in[0,T]}\mathbb{E}^{\mathbb{Q}}\left[|\tilde{L}\_{s}|^{2}\right]\right)^{\frac{1}{2}} |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | <∞\displaystyle\displaystyle<\infty |  |

  holds. Therefore, we can use the chain rule (Proposition [A.2](https://arxiv.org/html/2512.00346v1#A1.Thmtheorem2 "Proposition A.2. ‣ Appendix A Appendix: Malliavin calculus ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")), which proves (i).
* (ii)

  By Assumptions [2.2](https://arxiv.org/html/2512.00346v1#S2.Thmassumption2 "Assumption 2.2. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")(ii) and [2.3](https://arxiv.org/html/2512.00346v1#S2.Thmassumption3 "Assumption 2.3. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")(iv), there exists κ>0\displaystyle\kappa>0 such that

  |  |  |  |
  | --- | --- | --- |
  |  | I​(z)+z​I′​(z)≤κ​(1+z−1)I(z)+zI^{\prime}(z)\leq\kappa(1+z^{-1}) |  |

  for any z>0\displaystyle z>0. As a result,

  |  |  |  |
  | --- | --- | --- |
  |  | |HT​L~s​(I​(z​HT)+z​HT​I′​(z​HT))|≤κ​HT​|L~s|+κz​|L~s|,\displaystyle\displaystyle|H\_{T}\tilde{L}\_{s}(I(zH\_{T})+zH\_{T}I^{\prime}(zH\_{T}))|\leq\kappa H\_{T}|\tilde{L}\_{s}|+\frac{\kappa}{z}|\tilde{L}\_{s}|, |  |

  and

  |  |  |  |
  | --- | --- | --- |
  |  | 𝔼​[(∫0T|HT​L~s|2​𝑑s)12]<∞,𝔼​[(∫0T|L~s|2​𝑑s)12]<∞\displaystyle\displaystyle\mathbb{E}\left[\left(\int\_{0}^{T}|H\_{T}\tilde{L}\_{s}|^{2}ds\right)^{\frac{1}{2}}\right]<\infty,\quad\mathbb{E}\left[\left(\int\_{0}^{T}|\tilde{L}\_{s}|^{2}ds\right)^{\frac{1}{2}}\right]<\infty |  |

  holds. Therefore, we can use the chain rule again and complete the proof.

∎

Let a pair (Y,Z)\displaystyle(Y,Z) of ℝm\displaystyle\mathbb{R}^{m}-valued stochastic process Y\displaystyle Y and ℝm×m\displaystyle\mathbb{R}^{m\times m}-valued stochastic process Z\displaystyle Z be the solution to the following system of SDEs:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | d​Ys\displaystyle\displaystyle dY\_{s} | =b​(Ys)​d​s+a​(Ys)​d​Ws,\displaystyle\displaystyle=b(Y\_{s})ds+a(Y\_{s})dW\_{s}, | Yt\displaystyle\displaystyle Y\_{t} | =y,\displaystyle\displaystyle=y, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | d​Zs\displaystyle\displaystyle dZ\_{s} | =D​b​(Ys)​Zs​d​s+∑j=1nD​a⋅j​(Ys)​Zs​d​Wsj,\displaystyle\displaystyle=Db(Y\_{s})Z\_{s}ds+\sum\_{j=1}^{n}Da\_{\cdot j}(Y\_{s})Z\_{s}dW^{j}\_{s}, | Zt\displaystyle\displaystyle Z\_{t} | =I.\displaystyle\displaystyle=I. |  |

Then (Y,Z)\displaystyle(Y,Z) is a Markov process and (Y(t,y),Z(t,y))\displaystyle(Y^{(t,y)},Z^{(t,y)}) denotes the solution to the above system of SDEs when (Y,Z)\displaystyle(Y,Z) starts from (y,I)∈ℝm×ℝm×m\displaystyle(y,I)\in\mathbb{R}^{m}\times\mathbb{R}^{m\times m}. Note that Z(t,y)\displaystyle Z^{(t,y)} always starts from the identity matrix I∈ℝm×m\displaystyle I\in\mathbb{R}^{m\times m} and Ys(0,y)=Ys(t,Yt(0,y))\displaystyle Y^{(0,y)}\_{s}=Y^{(t,Y\_{t}^{(0,y)})}\_{s} for s∈[t,T]\displaystyle s\in[t,T]. Because Z(t,y)\displaystyle Z^{(t,y)} can be thought of as the derivative of Y(t,y)\displaystyle Y^{(t,y)} with respect to the initial value y\displaystyle y, we use the notation ∇yY(t,y)≔Z(t,y)\displaystyle\nabla\_{y}Y^{(t,y)}\coloneqq Z^{(t,y)} instead of Z(t,y)\displaystyle Z^{(t,y)}. Using these notations and Lemma [3.2](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem2 "Lemma 3.2. ‣ 3.1 Proofs for Sect. 2.1 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"),

|  |  |  |
| --- | --- | --- |
|  | Dt​Ys=∇yYs(t,Yt)​a​(Yt),s∈[t,T],D\_{t}Y\_{s}=\nabla\_{y}Y\_{s}^{(t,Y\_{t})}a(Y\_{t}),\quad s\in[t,T], |  |

where Yt=Yt(0,y)\displaystyle Y\_{t}=Y^{(0,y)}\_{t}.
Furthermore, let H(t,y)=(Hs(t,y))s∈[t,T]\displaystyle H^{(t,y)}=\left(H\_{s}^{(t,y)}\right)\_{s\in[t,T]} be

|  |  |  |
| --- | --- | --- |
|  | Hs(t,y)≔exp⁡(−∫tsr​(Yu(t,y))​𝑑u−∫tsθ⊤​(Yu(t,y))​𝑑Wu−12​∫ts|θ​(Yu(t,y))|2​𝑑u),H\_{s}^{(t,y)}\coloneqq\exp\left(-\int\_{t}^{s}r(Y^{(t,y)}\_{u})du-\int\_{t}^{s}\theta^{\top}(Y^{(t,y)}\_{u})dW\_{u}-\frac{1}{2}\int\_{t}^{s}|\theta(Y^{(t,y)}\_{u})|^{2}du\right), |  |

and let ∇yH(t,y)=(∇yHs(t,y))s∈[t,T],L(t,y)=(Ls(t,y))s∈[t,T]\displaystyle\nabla\_{y}H^{(t,y)}=\left(\nabla\_{y}H\_{s}^{(t,y)}\right)\_{s\in[t,T]},\;L^{(t,y)}=\left(L\_{s}^{(t,y)}\right)\_{s\in[t,T]} be an ℝm\displaystyle\mathbb{R}^{m}-valued stochastic process given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ls(t,y)\displaystyle\displaystyle L\_{s}^{(t,y)} | ≔∫ts(D​r​(Yu(t,y))​∇yYu(t,y))⊤​𝑑u+∫ts(D​θ​(Yu(t,y))​∇yYu(t,y))⊤​𝑑Wu+∫ts(D​θ​(Yu(t,y))​∇yYu(t,y))⊤​θ​(Yu(t,y))​𝑑u,\displaystyle\displaystyle\coloneqq\int\_{t}^{s}(Dr(Y^{(t,y)}\_{u})\nabla\_{y}Y^{(t,y)}\_{u})^{\top}du+\int\_{t}^{s}\left(D\theta(Y^{(t,y)}\_{u})\nabla\_{y}Y^{(t,y)}\_{u}\right)^{\top}dW\_{u}+\int\_{t}^{s}\left(D\theta(Y^{(t,y)}\_{u})\nabla\_{y}Y\_{u}^{(t,y)}\right)^{\top}\theta(Y\_{u}^{(t,y)})du, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∇yHs(t,y)\displaystyle\displaystyle\nabla\_{y}H\_{s}^{(t,y)} | ≔−Hs(t,y)​Ls(t,y).\displaystyle\displaystyle\coloneqq-H\_{s}^{(t,y)}L\_{s}^{(t,y)}. |  |

From these notations,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dt​HT\displaystyle\displaystyle D\_{t}H\_{T} | =−HT​L~t\displaystyle\displaystyle=-H\_{T}\tilde{L}\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−HT​(∫tTD​r​(Ys)​Dt​Ys​𝑑s+θ⊤​(Yt)+(∫tT(D​θ​(Ys)​Dt​Ys)⊤​𝑑Ws)⊤+∫sTθ⊤​(Ys)​D​θ​(Ys)​Dt​Ys​𝑑s)\displaystyle\displaystyle=-H\_{T}\left(\int\_{t}^{T}Dr(Y\_{s})D\_{t}Y\_{s}ds+\theta^{\top}(Y\_{t})+\left(\int\_{t}^{T}(D\theta(Y\_{s})D\_{t}Y\_{s})^{\top}dW\_{s}\right)^{\top}+\int\_{s}^{T}\theta^{\top}(Y\_{s})D\theta(Y\_{s})D\_{t}Y\_{s}ds\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−HT​θ⊤​(Yt)−Ht(0,y)​HT(t,Yt)​(∫tTD​r​(Ys)​Dt​Ys​𝑑s+(∫tT(D​θ​(Ys)​Dt​Ys)⊤​𝑑Ws)⊤+∫sTθ⊤​(Ys)​D​θ​(Ys)​Dt​Ys​𝑑s)\displaystyle\displaystyle=-H\_{T}\theta^{\top}(Y\_{t})-H\_{t}^{(0,y)}H\_{T}^{(t,Y\_{t})}\left(\int\_{t}^{T}Dr(Y\_{s})D\_{t}Y\_{s}ds+\left(\int\_{t}^{T}(D\theta(Y\_{s})D\_{t}Y\_{s})^{\top}dW\_{s}\right)^{\top}+\int\_{s}^{T}\theta^{\top}(Y\_{s})D\theta(Y\_{s})D\_{t}Y\_{s}ds\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−HTθ⊤(Yt)−Ht(0,y)HT(t,Yt)(∫tTDr(Ys)∇yYs(t,Yt)ds+(∫tT(Dθ(Ys)∇yYs(t,Yt))⊤dWs)⊤+∫sTθ⊤(Ys)Dθ(Ys)∇yYs(t,Yt)ds)a(Yt)\displaystyle\displaystyle\begin{multlined}=-H\_{T}\theta^{\top}(Y\_{t})-H\_{t}^{(0,y)}H\_{T}^{(t,Y\_{t})}\left(\int\_{t}^{T}Dr(Y\_{s})\nabla\_{y}Y\_{s}^{(t,Y\_{t})}ds+\left(\int\_{t}^{T}(D\theta(Y\_{s})\nabla\_{y}Y\_{s}^{(t,Y\_{t})})^{\top}dW\_{s}\right)^{\top}\right.\\ \left.+\int\_{s}^{T}\theta^{\top}(Y\_{s})D\theta(Y\_{s})\nabla\_{y}Y\_{s}^{(t,Y\_{t})}ds\right)a(Y\_{t})\end{multlined}=-H\_{T}\theta^{\top}(Y\_{t})-H\_{t}^{(0,y)}H\_{T}^{(t,Y\_{t})}\left(\int\_{t}^{T}Dr(Y\_{s})\nabla\_{y}Y\_{s}^{(t,Y\_{t})}ds+\left(\int\_{t}^{T}(D\theta(Y\_{s})\nabla\_{y}Y\_{s}^{(t,Y\_{t})})^{\top}dW\_{s}\right)^{\top}\right.\\ \left.+\int\_{s}^{T}\theta^{\top}(Y\_{s})D\theta(Y\_{s})\nabla\_{y}Y\_{s}^{(t,Y\_{t})}ds\right)a(Y\_{t}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−HT​θ⊤​(Yt)+Ht(0,y)​(∇yHT(t,Yt))⊤​a​(Yt).\displaystyle\displaystyle=-H\_{T}\theta^{\top}(Y\_{t})+H\_{t}^{(0,y)}\left(\nabla\_{y}H\_{T}^{(t,Y\_{t})}\right)^{\top}a(Y\_{t}). |  |

###### Proof of Theorem [2.2](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem2 "Theorem 2.2. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models").

By Clark’s formula (Proposition [A.1](https://arxiv.org/html/2512.00346v1#A1.Thmtheorem1 "Proposition A.1. ‣ Appendix A Appendix: Malliavin calculus ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")),
ψ\displaystyle\psi in Theorem [2.1](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ψt\displaystyle\displaystyle\psi\_{t} | =𝔼t​[Dt​(HT​I​(λ^​HT))⊤]\displaystyle\displaystyle=\mathbb{E}\_{t}\left[D\_{t}\left(H\_{T}I(\hat{\lambda}H\_{T})\right)^{\top}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−𝔼t​[(HT​θ​(Yt)+Ht​a⊤​(Yt)​∇yHT(t,Yt))​(I​(λ^​HT)+λ^​HT​I′​(λ^​HT))]\displaystyle\displaystyle=-\mathbb{E}\_{t}\left[\left(H\_{T}\theta(Y\_{t})+H\_{t}a^{\top}(Y\_{t})\nabla\_{y}H\_{T}^{(t,Y\_{t})}\right)\left(I(\hat{\lambda}H\_{T})+\hat{\lambda}H\_{T}I^{\prime}(\hat{\lambda}H\_{T})\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−Ht​X^t​θ​(Yt)−θ​(Yt)​𝔼t​[HT⋅λ^​HT​I′​(λ^​HT)]+Ht​a⊤​(Yt)​𝔼t​[∇yHT(t,Yt)​(I​(λ^​HT)+λ^​HT​I′​(λ^​HT))].\displaystyle\displaystyle=-H\_{t}\hat{X}\_{t}\theta(Y\_{t})-\theta(Y\_{t})\mathbb{E}\_{t}\left[H\_{T}\cdot\hat{\lambda}H\_{T}I^{\prime}(\hat{\lambda}H\_{T})\right]+H\_{t}a^{\top}(Y\_{t})\mathbb{E}\_{t}\left[\nabla\_{y}H\_{T}^{(t,Y\_{t})}\left(I(\hat{\lambda}H\_{T})+\hat{\lambda}H\_{T}I^{\prime}(\hat{\lambda}H\_{T})\right)\right]. |  |

As a result,

|  |  |  |  |
| --- | --- | --- | --- |
|  | π^t\displaystyle\displaystyle\hat{\pi}\_{t} | =σ⊤​(Yt)−1​(ψtHt+X^t​θ​(Yt))\displaystyle\displaystyle=\sigma^{\top}(Y\_{t})^{-1}\left(\frac{\psi\_{t}}{H\_{t}}+\hat{X}\_{t}\theta(Y\_{t})\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−σ⊤​(Yt)−1​θ​(Yt)​1Ht​𝔼t​[HT⋅λ^​HT​I′​(λ^​HT)]+σ⊤​(Yt)−1​a⊤​(Yt)​𝔼t​[∇yHT(t,Yt)​(I​(λ^​HT)+λ^​HT​I′​(λ^​HT))].\displaystyle\displaystyle=-\sigma^{\top}(Y\_{t})^{-1}\theta(Y\_{t})\frac{1}{H\_{t}}\mathbb{E}\_{t}\left[H\_{T}\cdot\hat{\lambda}H\_{T}I^{\prime}(\hat{\lambda}H\_{T})\right]+\sigma^{\top}(Y\_{t})^{-1}a^{\top}(Y\_{t})\mathbb{E}\_{t}\left[\nabla\_{y}H\_{T}^{(t,Y\_{t})}\left(I(\hat{\lambda}H\_{T})+\hat{\lambda}H\_{T}I^{\prime}(\hat{\lambda}H\_{T})\right)\right]. |  |

∎

###### Proof of Proposition [2.3](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem3 "Proposition 2.3. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models").

Let 𝒳:[0,∞)×(0,∞)×ℝm→(0,∞)\displaystyle\mathcal{X}:[0,\infty)\times(0,\infty)\times\mathbb{R}^{m}\to(0,\infty) be

|  |  |  |
| --- | --- | --- |
|  | 𝒳​(t,z,y)≔𝔼y​[Ht​I​(z​Ht)],\mathcal{X}(t,z,y)\coloneqq\mathbb{E}^{y}\left[H\_{t}I(zH\_{t})\right], |  |

where 𝔼y​[⋅]\displaystyle\mathbb{E}^{y}[\cdot] stands for the expectation when Y\displaystyle Y starts from y∈ℝm\displaystyle y\in\mathbb{R}^{m} at time 0.
By the Markov property of Y\displaystyle Y, 𝒳​(T−t,z,Yt)=𝔼t​[HTHt​I​(z​HTHt)]\displaystyle\mathcal{X}(T-t,z,Y\_{t})=\mathbb{E}\_{t}\left[\frac{H\_{T}}{H\_{t}}I\left(z\frac{H\_{T}}{H\_{t}}\right)\right]. Furthermore, because Ht\displaystyle H\_{t} is ℱt\displaystyle\mathcal{F}\_{t}-measurable,

|  |  |  |
| --- | --- | --- |
|  | 𝒳​(T−t,λ^​Ht,Yt)=1Ht​𝔼t​[HT​I​(λ^​Ht⋅HTHt)]=X^t.\displaystyle\displaystyle\mathcal{X}(T-t,\hat{\lambda}H\_{t},Y\_{t})=\frac{1}{H\_{t}}\mathbb{E}\_{t}\left[H\_{T}I\left(\hat{\lambda}H\_{t}\cdot\frac{H\_{T}}{H\_{t}}\right)\right]=\hat{X}\_{t}. |  |

Therefore, if we let F​(t,⋅,y)≔(𝒳​(t,⋅,y))−1\displaystyle F(t,\cdot,y)\coloneqq\left(\mathcal{X}(t,\cdot,y)\right)^{-1}, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(T−t,X^t,Yt)=λ^​HtF(T-t,\hat{X}\_{t},Y\_{t})=\hat{\lambda}H\_{t} |  | (13) |

holds. Let π^M:[0,∞)×(0,∞)×ℝm→ℝn\displaystyle\hat{\pi}^{M}:[0,\infty)\times(0,\infty)\times\mathbb{R}^{m}\to\mathbb{R}^{n} be

|  |  |  |
| --- | --- | --- |
|  | π^M​(t,x,y)≔−(σ⊤​(y))−1​θ​(y)​F​(t,x,y)​𝔼y​[(Ht)2​I′​(F​(t,x,y)​Ht)].\hat{\pi}^{M}(t,x,y)\coloneqq-(\sigma^{\top}(y))^{-1}\theta(y)F(t,x,y)\mathbb{E}^{y}\left[\left(H\_{t}\right)^{2}I^{\prime}\left(F(t,x,y)H\_{t}\right)\right]. |  |

By the Markov property of Yt\displaystyle Y\_{t},

|  |  |  |
| --- | --- | --- |
|  | π^M​(T−t,x,Yt)=−(σ⊤​(Yt))−1​θ​(Yt)​F​(T−t,x,Yt)​𝔼t​[(HTHt)2​I′​(F​(T−t,x,Yt)​HTHt)]\hat{\pi}^{M}(T-t,x,Y\_{t})=-(\sigma^{\top}(Y\_{t}))^{-1}\theta(Y\_{t})F(T-t,x,Y\_{t})\mathbb{E}\_{t}\left[\left(\frac{H\_{T}}{H\_{t}}\right)^{2}I^{\prime}\left(F(T-t,x,Y\_{t})\frac{H\_{T}}{H\_{t}}\right)\right] |  |

holds. Moreover, by the identity ([13](https://arxiv.org/html/2512.00346v1#S3.E13 "In 3.1 Proofs for Sect. 2.1 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) and the ℱt\displaystyle\mathcal{F}\_{t}-measurability of X^t\displaystyle\hat{X}\_{t},

|  |  |  |  |
| --- | --- | --- | --- |
|  | π^M​(T−t,X^t,Yt)\displaystyle\displaystyle\hat{\pi}^{M}(T-t,\hat{X}\_{t},Y\_{t}) | =−(σ⊤​(Yt))−1​θ​(Yt)​F​(T−t,X^t,Yt)​𝔼t​[(HTHt)2​I′​(F​(T−t,X^t,Yt)​HTHt)]\displaystyle\displaystyle=-(\sigma^{\top}(Y\_{t}))^{-1}\theta(Y\_{t})F(T-t,\hat{X}\_{t},Y\_{t})\mathbb{E}\_{t}\left[\left(\frac{H\_{T}}{H\_{t}}\right)^{2}I^{\prime}\left(F(T-t,\hat{X}\_{t},Y\_{t})\frac{H\_{T}}{H\_{t}}\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−(σ⊤​(Yt))−1​θ​(Yt)​1Ht​𝔼t​[HT⋅λ^​HT​I′​(λ^​HT)]\displaystyle\displaystyle=-(\sigma^{\top}(Y\_{t}))^{-1}\theta(Y\_{t})\frac{1}{H\_{t}}\mathbb{E}\_{t}\left[H\_{T}\cdot\hat{\lambda}H\_{T}I^{\prime}\left(\hat{\lambda}H\_{T}\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =π^tM.\displaystyle\displaystyle=\hat{\pi}^{M}\_{t}. |  |

In particular, if we set T=τ,t=0\displaystyle T=\tau,\;t=0, then

|  |  |  |
| --- | --- | --- |
|  | π^M​(τ,x,y)=π^0M=−(σ⊤​(y))−1​θ​(y)​𝔼y​[Hτ⋅λ^​Hτ​I′​(λ^​Hτ)],\hat{\pi}^{M}(\tau,x,y)=\hat{\pi}^{M}\_{0}=-(\sigma^{\top}(y))^{-1}\theta(y)\mathbb{E}^{y}\left[H\_{\tau}\cdot{\hat{\lambda}H\_{\tau}I^{\prime}(\hat{\lambda}H\_{\tau})}\right], |  |

where λ^=λ^​(τ,x,y)\displaystyle\hat{\lambda}=\hat{\lambda}(\tau,x,y) is defined by an equality x=𝔼y​[Hτ​I​(λ​Hτ)]\displaystyle x=\mathbb{E}^{y}[H\_{\tau}I(\lambda H\_{\tau})].
As a result, we have proved that the myopic portfolio (π^tM)t∈[0,T]\displaystyle\left(\hat{\pi}^{M}\_{t}\right)\_{t\in[0,T]} can be represented by a feedback form. By the same argument, we can also prove that the excess hedging demand (π^tH)t∈[0,T]\displaystyle\left(\hat{\pi}^{H}\_{t}\right)\_{t\in[0,T]} has a feedback form, which completes the proof.
∎

### 3.2 Proofs for Sect. [2.2](https://arxiv.org/html/2512.00346v1#S2.SS2 "2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")

In this subsection, we assume Assumptions [2.1](https://arxiv.org/html/2512.00346v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")–[2.4](https://arxiv.org/html/2512.00346v1#S2.Thmassumption4 "Assumption 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") and prove the main results in Sect. [2.2](https://arxiv.org/html/2512.00346v1#S2.SS2 "2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"). Lemma [3.7](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem7 "Lemma 3.7. ‣ 3.2 Proofs for Sect. 2.2 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") and Proposition [3.8](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.2 Proofs for Sect. 2.2 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") are useful to estimate the rate of the turnpike theorem for myopic portfolios (Theorem [2.4](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem4 "Theorem 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) and optimal wealth processes (Theorem [2.6](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem6 "Theorem 2.6. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")). Lemmas [3.9](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem9 "Lemma 3.9. ‣ 3.2 Proofs for Sect. 2.2 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") and [3.10](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem10 "Lemma 3.10. ‣ 3.2 Proofs for Sect. 2.2 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") are used to prove the uniform turnpike theorem for optimal portfolio proportions (Theorem [2.5](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem5 "Theorem 2.5. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")).

###### Lemma 3.7.

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[HT1+α]≤𝔼​[HTq]αq−1​𝔼​[HT]1−αq−1.\mathbb{E}[H\_{T}^{1+\alpha}]\leq\mathbb{E}\left[H\_{T}^{q}\right]^{\frac{\alpha}{q-1}}\mathbb{E}\left[H\_{T}\right]^{1-\frac{\alpha}{q-1}}. |  |

###### Proof.

The case α=0\displaystyle\alpha=0 is trivial. When α∈(q−1,0)\displaystyle\alpha\in(q-1,0), using Hölder’s inequality leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[HT1+α]\displaystyle\displaystyle\mathbb{E}[H\_{T}^{1+\alpha}] | =𝔼​[HTq​αq−1​HTq−1−αq−1]\displaystyle\displaystyle=\mathbb{E}\left[H\_{T}^{\frac{q\alpha}{q-1}}H\_{T}^{\frac{q-1-\alpha}{q-1}}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝔼​[HTq​αq−1⋅q−1α]αq−1​𝔼​[HTq−1−αq−1⋅q−1q−1−α]q−1−αq−1\displaystyle\displaystyle\leq\mathbb{E}\left[H\_{T}^{\frac{q\alpha}{q-1}\cdot\frac{q-1}{\alpha}}\right]^{\frac{\alpha}{q-1}}\mathbb{E}\left[H\_{T}^{\frac{q-1-\alpha}{q-1}\cdot\frac{q-1}{q-1-\alpha}}\right]^{\frac{q-1-\alpha}{q-1}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[HTq]αq−1​𝔼​[HT]1−αq−1.\displaystyle\displaystyle=\mathbb{E}\left[H\_{T}^{q}\right]^{\frac{\alpha}{q-1}}\mathbb{E}\left[H\_{T}\right]^{1-\frac{\alpha}{q-1}}. |  |

∎

###### Proposition 3.8.

Let d​(z)≔I1​(z)−I2​(z)\displaystyle d(z)\coloneqq I\_{1}(z)-I\_{2}(z). Then, there exists an M=M​(x,y)∈(−∞,x]\displaystyle M=M(x,y)\in(-\infty,x], which is independent of T\displaystyle T, such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | |𝔼​[HT​d​(λ^1,T​HT)]|\displaystyle\displaystyle\left|\mathbb{E}[H\_{T}d(\hat{\lambda}^{1,T}H\_{T})]\right| | ≤K​(𝔼​[HT]+(λ^1,T)α​𝔼​[HT1+α])\displaystyle\displaystyle\leq K\left(\mathbb{E}[H\_{T}]+(\hat{\lambda}^{1,T})^{\alpha}\mathbb{E}[H\_{T}^{1+\alpha}]\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤K​(𝔼​[HT]+(x−M)αq−1​𝔼​[HT]1−αq−1),T>0.\displaystyle\displaystyle\leq K\left(\mathbb{E}[H\_{T}]+(x-M)^{\frac{\alpha}{q-1}}\mathbb{E}[H\_{T}]^{1-\frac{\alpha}{q-1}}\right),\quad T>0. |  |

In particular,

|  |  |  |
| --- | --- | --- |
|  | |𝔼​[HT​d​(λ^1,T​HT)]|=O​(𝔼​[HT]1−αq−1),(T↗∞).\left|\mathbb{E}[H\_{T}d(\hat{\lambda}^{1,T}H\_{T})]\right|=O\left(\mathbb{E}[H\_{T}]^{1-\frac{\alpha}{q-1}}\right),\quad(T\nearrow\infty). |  |

###### Proof.

Note that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[HT​d​(λ^1,T​HT)]=x−𝔼​[HT​I2​(λ^1,T​HT)]=x−(λ^1,T)q−1​𝔼​[HTq]≤x.\mathbb{E}[H\_{T}d(\hat{\lambda}^{1,T}H\_{T})]=x-\mathbb{E}[H\_{T}I\_{2}(\hat{\lambda}^{1,T}H\_{T})]=x-(\hat{\lambda}^{1,T})^{q-1}\mathbb{E}[H\_{T}^{q}]\leq x. |  | (14) |

We define M=M​(x,y)≔infT>0𝔼​[HT​d​(λ^1,T​HT)]∈[−∞,x]\displaystyle M=M(x,y)\coloneqq\inf\_{T>0}\mathbb{E}[H\_{T}d(\hat{\lambda}^{1,T}H\_{T})]\in[-\infty,x].
By Assumption [2.4](https://arxiv.org/html/2512.00346v1#S2.Thmassumption4 "Assumption 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")(ii), ([14](https://arxiv.org/html/2512.00346v1#S3.E14 "In 3.2 Proofs for Sect. 2.2 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")), and Lemma [3.7](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem7 "Lemma 3.7. ‣ 3.2 Proofs for Sect. 2.2 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"),

|  |  |  |  |
| --- | --- | --- | --- |
|  | |𝔼​[HT​d​(λ^1,T​HT)]|\displaystyle\displaystyle\left|\mathbb{E}[H\_{T}d(\hat{\lambda}^{1,T}H\_{T})]\right| | ≤K​(𝔼​[HT]+(λ^1,T)α​𝔼​[HT1+α])\displaystyle\displaystyle\leq K\left(\mathbb{E}[H\_{T}]+(\hat{\lambda}^{1,T})^{\alpha}\mathbb{E}[H\_{T}^{1+\alpha}]\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =K​{𝔼​[HT]+(x−𝔼​[HT​d​(λ^1,T​HT)]𝔼​[HTq])αq−1​𝔼​[HT1+α]}\displaystyle\displaystyle=K\left\{\mathbb{E}[H\_{T}]+\left(\frac{x-\mathbb{E}[H\_{T}d(\hat{\lambda}^{1,T}H\_{T})]}{\mathbb{E}[H\_{T}^{q}]}\right)^{\frac{\alpha}{q-1}}\mathbb{E}[H\_{T}^{1+\alpha}]\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤K​{𝔼​[HT]+(x−𝔼​[HT​d​(λ^1,T​HT)])αq−1​𝔼​[HT]1−αq−1}\displaystyle\displaystyle\leq K\left\{\mathbb{E}[H\_{T}]+\left(x-\mathbb{E}[H\_{T}d(\hat{\lambda}^{1,T}H\_{T})]\right)^{\frac{\alpha}{q-1}}\mathbb{E}[H\_{T}]^{1-\frac{\alpha}{q-1}}\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤K​{𝔼​[HT]+(x−M)αq−1​𝔼​[HT]1−αq−1}\displaystyle\displaystyle\leq K\left\{\mathbb{E}[H\_{T}]+\left(x-M\right)^{\frac{\alpha}{q-1}}\mathbb{E}[H\_{T}]^{1-\frac{\alpha}{q-1}}\right\} |  |

holds. Lastly, we prove that M>−∞\displaystyle M>-\infty. Because 𝔼​[HT]↘0\displaystyle\mathbb{E}[H\_{T}]\searrow 0, there exists some constant C\displaystyle C such that 𝔼​[HT]≤C​𝔼​[HT]1−αq−1\displaystyle\mathbb{E}[H\_{T}]\leq C\mathbb{E}[H\_{T}]^{1-\frac{\alpha}{q-1}}. As a result,

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |𝔼​[HT​d​(λ^1,T​HT)]|\displaystyle\displaystyle\left|\mathbb{E}[H\_{T}d(\hat{\lambda}^{1,T}H\_{T})]\right| | ≤K​{C+(x−𝔼​[HT​d​(λ^1,T​HT)])αq−1}​𝔼​[HT]1−αq−1\displaystyle\displaystyle\leq K\left\{C+\left(x-\mathbb{E}[H\_{T}d(\hat{\lambda}^{1,T}H\_{T})]\right)^{\frac{\alpha}{q-1}}\right\}\mathbb{E}[H\_{T}]^{1-\frac{\alpha}{q-1}} |  | (15) |

holds. Dividing both sides of the inequality ([15](https://arxiv.org/html/2512.00346v1#S3.E15 "In 3.2 Proofs for Sect. 2.2 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) by |𝔼​[HT​d​(λ^1,T)]|\displaystyle|\mathbb{E}[H\_{T}d(\hat{\lambda}^{1,T})]|, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1≤K​{C|𝔼​[HT​d​(λ^1,T​HT)]|+|x−𝔼​[HT​d​(λ^1,T​HT)]𝔼​[HT​d​(λ^1,T​HT)]|αq−1⋅1|𝔼​[HT​d​(λ^1,T​HT)]|1−αq−1}​𝔼​[HT]1−αq−1.1\leq K\left\{\frac{C}{\left|\mathbb{E}[H\_{T}d(\hat{\lambda}^{1,T}H\_{T})]\right|}+\left|\frac{x-\mathbb{E}[H\_{T}d(\hat{\lambda}^{1,T}H\_{T})]}{\mathbb{E}[H\_{T}d(\hat{\lambda}^{1,T}H\_{T})]}\right|^{\frac{\alpha}{q-1}}\cdot\frac{1}{\left|\mathbb{E}[H\_{T}d(\hat{\lambda}^{1,T}H\_{T})]\right|^{1-\frac{\alpha}{q-1}}}\right\}\mathbb{E}[H\_{T}]^{1-\frac{\alpha}{q-1}}. |  | (16) |

If M=−∞\displaystyle M=-\infty, there exists a sequence (Tn)n≥1\displaystyle(T\_{n})\_{n\geq 1} such that 𝔼​[HTn​d​(λ^1,Tn​HTn)]↘−∞\displaystyle\mathbb{E}\left[H\_{T\_{n}}d(\hat{\lambda}^{1,T\_{n}}H\_{T\_{n}})\right]\searrow-\infty and the inequality ([16](https://arxiv.org/html/2512.00346v1#S3.E16 "In 3.2 Proofs for Sect. 2.2 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) leads to 1≤0\displaystyle 1\leq 0. Therefore, M>−∞\displaystyle M>-\infty and the proof is completed.
∎

###### Proof of Theorem [2.4](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem4 "Theorem 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models").

Let Ji​(z)≔z​Ii′​(z),(i=1,2)\displaystyle J\_{i}(z)\coloneqq zI\_{i}^{\prime}(z),\;(i=1,2).

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[HT⋅J1​(λ^1,T​HT)]−𝔼​[HT⋅J2​(λ^2,T​HT)]\displaystyle\displaystyle\mathbb{E}\left[H\_{T}\cdot J\_{1}\left(\hat{\lambda}^{1,T}H\_{T}\right)\right]-\mathbb{E}\left[H\_{T}\cdot J\_{2}\left(\hat{\lambda}^{2,T}H\_{T}\right)\right] | =𝔼​[HT​{J1​(λ^1,T​HT)−J2​(λ^1,T​HT)}]\displaystyle\displaystyle=\mathbb{E}\left[H\_{T}\left\{J\_{1}\left(\hat{\lambda}^{1,T}H\_{T}\right)-J\_{2}\left(\hat{\lambda}^{1,T}H\_{T}\right)\right\}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝔼​[HT​{J2​(λ^1,T​HT)−J2​(λ^2,T​HT)}]\displaystyle\displaystyle\qquad+\mathbb{E}\left[H\_{T}\left\{J\_{2}\left(\hat{\lambda}^{1,T}H\_{T}\right)-J\_{2}\left(\hat{\lambda}^{2,T}H\_{T}\right)\right\}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≕(I)+(II).\displaystyle\displaystyle\eqqcolon(\text{I})+(\text{II}). |  |

Because J2​(z)=(q−1)​zq−1\displaystyle J\_{2}(z)=(q-1)z^{q-1},

|  |  |  |
| --- | --- | --- |
|  | (II)=(q−1)​{(λ^1,T)q−1−(λ^2,T)q−1}​𝔼​[HTq].\displaystyle\displaystyle(\text{II})=(q-1)\left\{\left(\hat{\lambda}^{1,T}\right)^{q-1}-\left(\hat{\lambda}^{2,T}\right)^{q-1}\right\}\mathbb{E}[H\_{T}^{q}]. |  |

By the definition of λ^i,T\displaystyle\hat{\lambda}^{i,T},

|  |  |  |  |
| --- | --- | --- | --- |
|  | x\displaystyle\displaystyle x | =𝔼​[HT​I1​(λ^1,T​HT)]=𝔼​[HT​d​(λ^1,T​HT)]+(λ^1,T)q−1​𝔼​[HTq],\displaystyle\displaystyle=\mathbb{E}[H\_{T}I\_{1}(\hat{\lambda}^{1,T}H\_{T})]=\mathbb{E}[H\_{T}d(\hat{\lambda}^{1,T}H\_{T})]+(\hat{\lambda}^{1,T})^{q-1}\mathbb{E}[H\_{T}^{q}], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | x\displaystyle\displaystyle x | =(λ^2,T)q−1​𝔼​[HTq]\displaystyle\displaystyle=(\hat{\lambda}^{2,T})^{q-1}\mathbb{E}[H\_{T}^{q}] |  |

hold, and it leads to

|  |  |  |  |
| --- | --- | --- | --- |
|  | (II)\displaystyle\displaystyle(\text{II}) | =(1−q)​𝔼​[HT​d​(λ^1,T​HT)].\displaystyle\displaystyle=(1-q)\mathbb{E}[H\_{T}d(\hat{\lambda}^{1,T}H\_{T})]. |  |

As a result, by Assumption [2.4](https://arxiv.org/html/2512.00346v1#S2.Thmassumption4 "Assumption 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")(ii) and Proposition [3.8](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.2 Proofs for Sect. 2.2 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | |π^1,M​(T,x,y)−π^2,M​(T,x,y)|\displaystyle\displaystyle|\hat{\pi}^{1,M}(T,x,y)-\hat{\pi}^{2,M}(T,x,y)| | ≤K​(2−q)​|(σ⊤​(y))−1​θ​(y)|​(𝔼​[HT]+(λ^1,T)α​𝔼​[HTα+1])\displaystyle\displaystyle\leq K(2-q)\left|(\sigma^{\top}(y))^{-1}\theta(y)\right|\left(\mathbb{E}\left[H\_{T}\right]+(\hat{\lambda}^{1,T})^{\alpha}\mathbb{E}\left[H\_{T}^{\alpha+1}\right]\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤K​(2−q)​|(σ⊤​(y))−1​θ​(y)|​(𝔼​[HT]+(x−M)αq−1​𝔼​[HT]1−αq−1).\displaystyle\displaystyle\leq K(2-q)\left|(\sigma^{\top}(y))^{-1}\theta(y)\right|\left(\mathbb{E}[H\_{T}]+(x-M)^{\frac{\alpha}{q-1}}\mathbb{E}[H\_{T}]^{1-\frac{\alpha}{q-1}}\right). |  |

∎

###### Lemma 3.9.

For constants C>0,γ∈[0,1)\displaystyle C>0,\;\gamma\in[0,1), we define a function f\displaystyle f by

|  |  |  |
| --- | --- | --- |
|  | f​(x,z)≔|z|C+(x−z)γ,x>0,z<−x.f(x,z)\coloneqq\frac{|z|}{C+(x-z)^{\gamma}},\quad x>0,\;z<-x. |  |

Then f\displaystyle f satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | z∈[−x,x)\displaystyle\displaystyle z\in[-x,x) | ⇒f​(x,z)≥|z|C+(2​x)γ,\displaystyle\displaystyle\Rightarrow f(x,z)\geq\frac{|z|}{C+(2x)^{\gamma}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | z∈(−∞,−x)\displaystyle\displaystyle z\in(-\infty,-x) | ⇒f​(x,z)≥|z|1−γC​x−γ+2γ.\displaystyle\displaystyle\Rightarrow f(x,z)\geq\frac{|z|^{1-\gamma}}{Cx^{-\gamma}+2^{\gamma}}. |  |

###### Proof.

When z∈[−x,x)\displaystyle z\in[-x,x),

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(x,z)\displaystyle\displaystyle f(x,z) | =|z|C+(x−z)γ\displaystyle\displaystyle=\frac{|z|}{C+(x-z)^{\gamma}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥|z|C+(x−(−x))γ\displaystyle\displaystyle\geq\frac{|z|}{C+(x-(-x))^{\gamma}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =|z|C+(2​x)γ.\displaystyle\displaystyle=\frac{|z|}{C+(2x)^{\gamma}}. |  |

When z∈(−∞,−x)\displaystyle z\in(-\infty,-x),

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(x,z)\displaystyle\displaystyle f(x,z) | =|z|C+(x+|z|)γ\displaystyle\displaystyle=\frac{|z|}{C+(x+|z|)^{\gamma}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =|z|1−γC​|z|−γ+(x|z|+1)γ\displaystyle\displaystyle=\frac{|z|^{1-\gamma}}{C|z|^{-\gamma}+\left(\frac{x}{|z|}+1\right)^{\gamma}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≥|z|1−γC​x−γ+2γ.\displaystyle\displaystyle\geq\frac{|z|^{1-\gamma}}{Cx^{-\gamma}+2^{\gamma}}. |  |

∎

###### Lemma 3.10.

For any ϵ>0\displaystyle\epsilon>0,

|  |  |  |
| --- | --- | --- |
|  | supx>ϵ(x−M​(x,y)x)<∞.\sup\_{x>\epsilon}\left(\frac{x-M(x,y)}{x}\right)<\infty. |  |

###### Proof.

Let G​(T,x,y)≔𝔼​[HT​d​(λ^1,T​HT)]\displaystyle G(T,x,y)\coloneqq\mathbb{E}[H\_{T}d(\hat{\lambda}^{1,T}H\_{T})].
Because

|  |  |  |
| --- | --- | --- |
|  | supx>ϵ(x−M​(x,y)x)=1−infx>ϵ,T>0G​(T,x,y)x,\sup\_{x>\epsilon}\left(\frac{x-M(x,y)}{x}\right)=1-\inf\_{x>\epsilon,T>0}\frac{G(T,x,y)}{x}, |  |

it suffices to prove

|  |  |  |
| --- | --- | --- |
|  | infx>ϵ,T>0G​(T,x,y)x>−∞.\inf\_{x>\epsilon,T>0}\frac{G(T,x,y)}{x}>-\infty. |  |

From ([15](https://arxiv.org/html/2512.00346v1#S3.E15 "In 3.2 Proofs for Sect. 2.2 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")),

|  |  |  |
| --- | --- | --- |
|  | f​(x,G)=|G|C+(x−G)αq−1≤K​E​[HT]1−αq−1,f(x,G)=\frac{|G|}{C+(x-G)^{\frac{\alpha}{q-1}}}\leq KE[H\_{T}]^{1-\frac{\alpha}{q-1}}, |  |

where we define f\displaystyle f as in Lemma [3.9](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem9 "Lemma 3.9. ‣ 3.2 Proofs for Sect. 2.2 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") with γ=αq−1\displaystyle\gamma=\frac{\alpha}{q-1}. Lemma [3.9](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem9 "Lemma 3.9. ‣ 3.2 Proofs for Sect. 2.2 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") implies that when Gx<−1\displaystyle\frac{G}{x}<-1,

|  |  |  |
| --- | --- | --- |
|  | |G|1−γC​x−γ+2γ≤f​(x,G)≤K​E​[HT]1−γ,\frac{|G|^{1-\gamma}}{Cx^{-\gamma}+2^{\gamma}}\leq f(x,G)\leq KE[H\_{T}]^{1-\gamma}, |  |

which means that

|  |  |  |  |
| --- | --- | --- | --- |
|  | Gx\displaystyle\displaystyle\frac{G}{x} | ≥−1x​{K​(C​x−γ+2γ)}11−γ​𝔼​[HT]\displaystyle\displaystyle\geq-\frac{1}{x}\left\{K\left(Cx^{-\gamma}+2^{\gamma}\right)\right\}^{\frac{1}{1-\gamma}}\mathbb{E}[H\_{T}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−{K​(C​x−1+2γ​xγ−1)}11−γ​𝔼​[HT]\displaystyle\displaystyle=-\left\{K\left(Cx^{-1}+2^{\gamma}x^{\gamma-1}\right)\right\}^{\frac{1}{1-\gamma}}\mathbb{E}[H\_{T}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | >−∞\displaystyle\displaystyle>-\infty |  |

Therefore, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | infx>ϵ,T>0G​(T,x,y)x\displaystyle\displaystyle\inf\_{x>\epsilon,T>0}\frac{G(T,x,y)}{x} | ≥−supx>ϵ{K​(C​x−1+2γ​xγ−1)}11−γ⋅supT>0𝔼​[HT]\displaystyle\displaystyle\geq-\sup\_{x>\epsilon}\left\{K\left(Cx^{-1}+2^{\gamma}x^{\gamma-1}\right)\right\}^{\frac{1}{1-\gamma}}\cdot\sup\_{T>0}\mathbb{E}[H\_{T}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−{K​(C​ϵ−1+2γ​ϵγ−1)}11−γ⋅supT>0𝔼​[HT]\displaystyle\displaystyle=-\left\{K\left(C\epsilon^{-1}+2^{\gamma}\epsilon^{\gamma-1}\right)\right\}^{\frac{1}{1-\gamma}}\cdot\sup\_{T>0}\mathbb{E}[H\_{T}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | >−∞.\displaystyle\displaystyle>-\infty. |  |

∎

###### Proof of Theorem [2.5](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem5 "Theorem 2.5. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models").

From Theorem [2.4](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem4 "Theorem 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") and Lemma [3.10](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem10 "Lemma 3.10. ‣ 3.2 Proofs for Sect. 2.2 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"),

|  |  |  |  |
| --- | --- | --- | --- |
|  | supx>ϵ|π^1,M​(T,x,y)x−π^2,M​(T,x,y)x|\displaystyle\displaystyle\sup\_{x>\epsilon}\left|\frac{\hat{\pi}^{1,M}(T,x,y)}{x}-\frac{\hat{\pi}^{2,M}(T,x,y)}{x}\right| | ≤K​(2−q)​|σ⊤​(y)−1​θ​(y)|​(𝔼​[HT]ϵ+supx>ϵ(x−Mx)αq−1​(𝔼​[HT]ϵ)1−αq−1)\displaystyle\displaystyle\leq K(2-q)|\sigma^{\top}(y)^{-1}\theta(y)|\left(\frac{\mathbb{E}[H\_{T}]}{\epsilon}+\sup\_{x>\epsilon}\left(\frac{x-M}{x}\right)^{\frac{\alpha}{q-1}}\left(\frac{\mathbb{E}[H\_{T}]}{\epsilon}\right)^{1-\frac{\alpha}{q-1}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =O​(𝔼​[HT]1−αq−1).\displaystyle\displaystyle=O\left(\mathbb{E}[H\_{T}]^{1-\frac{\alpha}{q-1}}\right). |  |

∎

###### Proof of Theorem [2.6](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem6 "Theorem 2.6. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models").

Because (Ht​|X^t1,T−X^t2,T|)t\displaystyle\left(H\_{t}|\hat{X}^{1,T}\_{t}-\hat{X}^{2,T}\_{t}|\right)\_{t} is a submartingale,

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Ht​|X^t1,T−X^t2,T|]≤𝔼​[HT​|X^T1,T−X^T2,T|]\mathbb{E}[H\_{t}|\hat{X}^{1,T}\_{t}-\hat{X}^{2,T}\_{t}|]\leq\mathbb{E}[H\_{T}|\hat{X}^{1,T}\_{T}-\hat{X}^{2,T}\_{T}|] |  |

holds. By the identity X^Ti,T=Ii​(λ^i,T​HT)\displaystyle\hat{X}^{i,T}\_{T}=I\_{i}\left(\hat{\lambda}^{i,T}H\_{T}\right) and 𝔼​[HT​d​(λ^1,T​HT)]={(λ^1,T)q−1−(λ^2,T)q−1}​𝔼​[HTq]\displaystyle\mathbb{E}[H\_{T}d(\hat{\lambda}^{1,T}H\_{T})]=\left\{\left(\hat{\lambda}^{1,T}\right)^{q-1}-\left(\hat{\lambda}^{2,T}\right)^{q-1}\right\}\mathbb{E}[H\_{T}^{q}], it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[HT​|X^T1,T−X^T2,T|]\displaystyle\displaystyle\mathbb{E}\left[H\_{T}|\hat{X}^{1,T}\_{T}-\hat{X}^{2,T}\_{T}|\right] | ≤𝔼​[HT​|I1​(λ^1,T​HT)−I2​(λ^1,T​HT)|]+𝔼​[HT​|I2​(λ^1,T​HT)−I2​(λ^2,T​HT)|]\displaystyle\displaystyle\leq\mathbb{E}\left[H\_{T}\left|I\_{1}\left(\hat{\lambda}^{1,T}H\_{T}\right)-I\_{2}\left(\hat{\lambda}^{1,T}H\_{T}\right)\right|\right]+\mathbb{E}\left[H\_{T}\left|I\_{2}\left(\hat{\lambda}^{1,T}H\_{T}\right)-I\_{2}\left(\hat{\lambda}^{2,T}H\_{T}\right)\right|\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[HT​|d​(λ^1,T​HT)|]+|(λ^1,T)q−1−(λ^2,T)q−1|⋅𝔼​[HTq]\displaystyle\displaystyle=\mathbb{E}\left[H\_{T}\left|d\left(\hat{\lambda}^{1,T}H\_{T}\right)\right|\right]+\left|\left(\hat{\lambda}^{1,T}\right)^{q-1}-\left(\hat{\lambda}^{2,T}\right)^{q-1}\right|\cdot\mathbb{E}\left[H\_{T}^{q}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2​𝔼​[HT​|d​(λ^1,T​HT)|].\displaystyle\displaystyle\leq 2\mathbb{E}\left[H\_{T}\left|d\left(\hat{\lambda}^{1,T}H\_{T}\right)\right|\right]. |  |

By combining the above inequalities with Proposition [3.8](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.2 Proofs for Sect. 2.2 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | supt∈[0,T]𝔼​[Ht​|X^t1,T−X^t2,T|]\displaystyle\displaystyle\sup\_{t\in[0,T]}\mathbb{E}[H\_{t}|\hat{X}^{1,T}\_{t}-\hat{X}^{2,T}\_{t}|] | ≤2​𝔼​[HT​|d​(λ^1,T​HT)|]\displaystyle\displaystyle\leq 2\mathbb{E}\left[H\_{T}\left|d\left(\hat{\lambda}^{1,T}H\_{T}\right)\right|\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2​K​(𝔼​[HT]+(λ^1,T)α​𝔼​[HT1+α])\displaystyle\displaystyle\leq 2K\left(\mathbb{E}[H\_{T}]+(\hat{\lambda}^{1,T})^{\alpha}\mathbb{E}[H\_{T}^{1+\alpha}]\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤2​K​(𝔼​[HT]+(x−M)αq−1​𝔼​[HT]1−αq−1)\displaystyle\displaystyle\leq 2K\left(\mathbb{E}[H\_{T}]+(x-M)^{\frac{\alpha}{q-1}}\mathbb{E}[H\_{T}]^{1-\frac{\alpha}{q-1}}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =O​(𝔼​[HT]1−αq−1),(T↗∞).\displaystyle\displaystyle=O\left(\mathbb{E}[H\_{T}]^{1-\frac{\alpha}{q-1}}\right),\quad(T\nearrow\infty). |  |

∎

### 3.3 Proofs for Sect. [2.3](https://arxiv.org/html/2512.00346v1#S2.SS3 "2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")

For excess hedging demands π^i,H\displaystyle\hat{\pi}^{i,H}, the following estimate holds under Assumptions [2.1](https://arxiv.org/html/2512.00346v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")–[2.4](https://arxiv.org/html/2512.00346v1#S2.Thmassumption4 "Assumption 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models").

###### Proposition 3.11.

We assume Assumptions [2.1](https://arxiv.org/html/2512.00346v1#S2.Thmassumption1 "Assumption 2.1. ‣ 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")–[2.4](https://arxiv.org/html/2512.00346v1#S2.Thmassumption4 "Assumption 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"). Let MTγ≔HTγ𝔼​[HTγ],d​ℚTγ≔MTγ​d​ℙ,γ∈[0,1],\displaystyle M\_{T}^{\gamma}\coloneqq\frac{H\_{T}^{\gamma}}{\mathbb{E}[H\_{T}^{\gamma}]},\;d\mathbb{Q}^{\gamma}\_{T}\coloneqq M\_{T}^{\gamma}d\mathbb{P},\;\gamma\in[0,1], and M∈(−∞,x]\displaystyle M\in(-\infty,x] be as in Proposition [3.8](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.2 Proofs for Sect. 2.2 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"). Then

|  |  |  |
| --- | --- | --- |
|  | |π^1,H(T,x,y)−π^2,H(T,x,y)|≤|(σ−1(y))⊤a⊤(y)|{q|𝔼[HTd(λ^1,THT)]|⋅𝔼ℚTq[|LT|]+2K(𝔼[HT]⋅𝔼ℚT1[|LT|]+(x−M)αq−1⋅𝔼[HT]1−αq−1⋅𝔼ℚT1+α[|LT|])},|\hat{\pi}^{1,H}(T,x,y)-\hat{\pi}^{2,H}(T,x,y)|\leq\left|(\sigma^{-1}(y))^{\top}a^{\top}(y)\right|\left\{q\left|\mathbb{E}[H\_{T}d(\hat{\lambda}^{1,T}H\_{T})]\right|\cdot\mathbb{E}^{\mathbb{Q}^{q}\_{T}}[|L\_{T}|]\right.\\ \left.+2K\left(\mathbb{E}[H\_{T}]\cdot\mathbb{E}^{\mathbb{Q}^{1}\_{T}}[|L\_{T}|]+(x-M)^{\frac{\alpha}{q-1}}\cdot\mathbb{E}[H\_{T}]^{1-\frac{\alpha}{q-1}}\cdot\mathbb{E}^{\mathbb{Q}^{1+\alpha}\_{T}}[|L\_{T}|]\right)\right\}, |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | LT≔∫0T(D​r​(Yu)​∇yYu)⊤​𝑑u+∫0T(D​θ​(Yu)​∇yYu)⊤​𝑑Wu+∫0T(D​θ​(Yu)​∇yYu)⊤​θ​(Yu)​𝑑u.L\_{T}\coloneqq\int\_{0}^{T}(Dr(Y\_{u})\nabla\_{y}Y\_{u})^{\top}du+\int\_{0}^{T}\left(D\theta(Y\_{u})\nabla\_{y}Y\_{u}\right)^{\top}dW\_{u}+\int\_{0}^{T}\left(D\theta(Y\_{u})\nabla\_{y}Y\_{u}\right)^{\top}\theta(Y\_{u})du. |  | (17) |

###### Proof.

Recall that the excess hedging demand is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | π^i,H​(T,x,y)\displaystyle\displaystyle\hat{\pi}^{i,H}(T,x,y) | =(σ⊤​(y))−1​a⊤​(y)​𝔼​[∇yHT​Fi​(λ^i,T​HT)],\displaystyle\displaystyle=(\sigma^{\top}(y))^{-1}a^{\top}(y)\mathbb{E}\left[\nabla\_{y}H\_{T}F\_{i}\left(\hat{\lambda}^{i,T}H\_{T}\right)\right], |  |

where Fi​(z)≔Ii​(z)+z​Ii′​(z)\displaystyle F\_{i}(z)\coloneqq I\_{i}(z)+zI\_{i}^{\prime}(z) and ∇yHT=−HT​LT\displaystyle\nabla\_{y}H\_{T}=-H\_{T}L\_{T}.

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[∇yHT​(F1​(λ^1,T​HT)−F2​(λ^2,T​HT))]\displaystyle\displaystyle\mathbb{E}\left[\nabla\_{y}H\_{T}\left(F\_{1}(\hat{\lambda}^{1,T}H\_{T})-F\_{2}(\hat{\lambda}^{2,T}H\_{T})\right)\right] | =𝔼​[∇yHT​(F1​(λ^1,T​HT)−F2​(λ^1,T​HT))]\displaystyle\displaystyle=\mathbb{E}\left[\nabla\_{y}H\_{T}\left(F\_{1}(\hat{\lambda}^{1,T}H\_{T})-F\_{2}(\hat{\lambda}^{1,T}H\_{T})\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +𝔼​[∇yHT​(F2​(λ^1,T​HT)−F2​(λ^2,T​HT))]\displaystyle\displaystyle\qquad\qquad\qquad+\mathbb{E}\left[\nabla\_{y}H\_{T}\left(F\_{2}(\hat{\lambda}^{1,T}H\_{T})-F\_{2}(\hat{\lambda}^{2,T}H\_{T})\right)\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≕(I)+(II).\displaystyle\displaystyle\eqqcolon(\text{I})+(\text{II}). |  |

First, we evaluate (I)\displaystyle(\text{I}). Assumption [2.4](https://arxiv.org/html/2512.00346v1#S2.Thmassumption4 "Assumption 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")(ii) implies |F1​(z)−F2​(z)|≤2​K​(1+zα)\displaystyle|F\_{1}(z)-F\_{2}(z)|\leq 2K(1+z^{\alpha}) and Proposition [3.8](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem8 "Proposition 3.8. ‣ 3.2 Proofs for Sect. 2.2 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") implies (λ^1,T)α​𝔼​[HT1+α]≤(x−M)αq−1​𝔼​[HT]1−αq−1\displaystyle(\hat{\lambda}^{1,T})^{\alpha}\mathbb{E}[H\_{T}^{1+\alpha}]\leq(x-M)^{\frac{\alpha}{q-1}}\mathbb{E}[H\_{T}]^{1-\frac{\alpha}{q-1}}. Using these inequalities and myopic probability measures d​ℚTγ≔HT𝔼​[HT]​d​ℙ\displaystyle d\mathbb{Q}^{\gamma}\_{T}\coloneqq\frac{H\_{T}}{\mathbb{E}[H\_{T}]}d\mathbb{P}, it follows that

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | |(I)|\displaystyle|(\text{I})| | ≤𝔼​[HT​|LT|​|F1​(λ^1,T​HT)−F2​(λ^1,T​HT)|]\displaystyle\leq\mathbb{E}\left[H\_{T}|L\_{T}|\left|F\_{1}(\hat{\lambda}^{1,T}H\_{T})-F\_{2}(\hat{\lambda}^{1,T}H\_{T})\right|\right] |  | (18) |
|  |  | ≤2​K​(𝔼​[|LT|​HT]+(λ^1,T)α​𝔼​[|LT|​HTα+1])\displaystyle\leq 2K\left(\mathbb{E}[|L\_{T}|H\_{T}]+\left(\hat{\lambda}^{1,T}\right)^{\alpha}\mathbb{E}[|L\_{T}|H\_{T}^{\alpha+1}]\right) |  |
|  |  | ≤2​K​(𝔼​[HT]​𝔼ℚT1​[|LT|]+(x−M)αq−1​𝔼​[HT]1−αq−1​𝔼ℚT1+α​[|LT|]).\displaystyle\leq 2K\left(\mathbb{E}[H\_{T}]\mathbb{E}^{\mathbb{Q}^{1}\_{T}}[|L\_{T}|]+(x-M)^{\frac{\alpha}{q-1}}\mathbb{E}[H\_{T}]^{1-\frac{\alpha}{q-1}}\mathbb{E}^{\mathbb{Q}^{1+\alpha}\_{T}}[|L\_{T}|]\right). |  |

Next, we evaluate (II)\displaystyle(\text{II}). Because F2​(z)=q​zq−1\displaystyle F\_{2}(z)=qz^{q-1},

|  |  |  |
| --- | --- | --- |
|  | (II)=q​{(λ^1,T)q−1−(λ^2,T)q−1}​𝔼​[∇yHT​HTq−1].(\text{II})=q\left\{\left(\hat{\lambda}^{1,T}\right)^{q-1}-\left(\hat{\lambda}^{2,T}\right)^{q-1}\right\}\mathbb{E}\left[\nabla\_{y}H\_{T}H\_{T}^{q-1}\right]. |  |

Because λ^i,T​(i=1,2)\displaystyle\hat{\lambda}^{i,T}\;(i=1,2) are determined by the identity

|  |  |  |  |
| --- | --- | --- | --- |
|  | x\displaystyle\displaystyle x | =𝔼​[HT​I1​(λ^1,T​HT)]=(λ^1,T)q−1​𝔼​[HTq]+𝔼​[HT​d​(λ^1,T​HT)],\displaystyle\displaystyle=\mathbb{E}\left[H\_{T}I\_{1}(\hat{\lambda}^{1,T}H\_{T})\right]=\left(\hat{\lambda}^{1,T}\right)^{q-1}\mathbb{E}\left[H\_{T}^{q}\right]+\mathbb{E}\left[H\_{T}d(\hat{\lambda}^{1,T}H\_{T})\right], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | x\displaystyle\displaystyle x | =𝔼​[HT​I2​(λ^2,T​HT)]=(λ^2,T)q−1​𝔼​[HTq],\displaystyle\displaystyle=\mathbb{E}\left[H\_{T}I\_{2}(\hat{\lambda}^{2,T}H\_{T})\right]=\left(\hat{\lambda}^{2,T}\right)^{q-1}\mathbb{E}\left[H\_{T}^{q}\right], |  |

it follows that

|  |  |  |
| --- | --- | --- |
|  | (λ^1,T)q−1−(λ^2,T)q−1=−𝔼​[HT​d​(λ^1,T​HT)]𝔼​[HTq],\left(\hat{\lambda}^{1,T}\right)^{q-1}-\left(\hat{\lambda}^{2,T}\right)^{q-1}=-\frac{\mathbb{E}\left[H\_{T}d(\hat{\lambda}^{1,T}H\_{T})\right]}{\mathbb{E}\left[H\_{T}^{q}\right]}, |  |

which leads to

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (II)\displaystyle(\text{II}) | =−q​𝔼​[HT​d​(λ^1,T​HT)]​𝔼​[∇yHT​HTq−1]𝔼​[HTq]\displaystyle=-q\mathbb{E}\left[H\_{T}d(\hat{\lambda}^{1,T}H\_{T})\right]\frac{\mathbb{E}\left[\nabla\_{y}H\_{T}H\_{T}^{q-1}\right]}{\mathbb{E}\left[H\_{T}^{q}\right]} |  | (19) |
|  |  | =q​𝔼​[HT​d​(λ^1,T​HT)]​𝔼ℚTq​[LT].\displaystyle=q\mathbb{E}\left[H\_{T}d(\hat{\lambda}^{1,T}H\_{T})\right]\mathbb{E}^{\mathbb{Q}^{q}\_{T}}\left[L\_{T}\right]. |  |

Therefore, the statement follows from ([18](https://arxiv.org/html/2512.00346v1#S3.E18 "In 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) and ([19](https://arxiv.org/html/2512.00346v1#S3.E19 "In 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")).
∎

To estimate the convergence rate of the turnpike theorem for excess hedging demands in stochastic factor models ([2](https://arxiv.org/html/2512.00346v1#S2.E2 "In 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")), the above proposition implies that it suffices to derive O​(𝔼ℚTγ​[|LT|])\displaystyle O\left(\mathbb{E}^{\mathbb{Q}\_{T}^{\gamma}}[|L\_{T}|]\right) for γ∈[0,1]\displaystyle\gamma\in[0,1], where ℚTγ\displaystyle\mathbb{Q}^{\gamma}\_{T} denotes the myopic probability measures used in [[13](https://arxiv.org/html/2512.00346v1#bib.bib13)] and LT\displaystyle L\_{T} is given by ([17](https://arxiv.org/html/2512.00346v1#S3.E17 "In Proposition 3.11. ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")).
Because the martingale density processes of myopic probabilities ℚTγ\displaystyle\mathbb{Q}^{\gamma}\_{T} can be computed by the optimal portfolios for CRRA investors, which can be represented by solutions to semilinear PDEs, the estimation of O​(𝔼ℚTγ​[|LT|])\displaystyle O\left(\mathbb{E}^{\mathbb{Q}\_{T}^{\gamma}}[|L\_{T}|]\right) requires the asymptotic behavior of the solutions to semilinear PDEs. Here, we restrict our models to the quadratic term structure model given by ([7](https://arxiv.org/html/2512.00346v1#S2.E7 "In 2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) and ([8](https://arxiv.org/html/2512.00346v1#S2.E8 "In 2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) and use the asymptotic properties of the solutions to the Riccati differential equations. Further research for general stochastic factor models ([2](https://arxiv.org/html/2512.00346v1#S2.E2 "In 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) is postponed to future work.

###### Remark 3.1.

When γ=0\displaystyle\gamma=0, ℚTγ=ℙ\displaystyle\mathbb{Q}^{\gamma}\_{T}=\mathbb{P}. When γ=1\displaystyle\gamma=1, d​ℚTγ=HT𝔼​[HT]​d​ℙ\displaystyle d\mathbb{Q}^{\gamma}\_{T}=\frac{H\_{T}}{\mathbb{E}[H\_{T}]}d\mathbb{P} is a T\displaystyle T-forward measure under which the price process of a zero-coupon bond is chosen as numéraire. When γ∈(0,1)\displaystyle\gamma\in(0,1), as Proposition [3.13](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem13 "Proposition 3.13. ‣ 3.3.1 Martingale density processes of the myopic probabilities ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") will say, d​ℚTγ=HT⋅X^TT​d​ℙ\displaystyle d\mathbb{Q}^{\gamma}\_{T}=H\_{T}\cdot\hat{X}^{T}\_{T}d\mathbb{P}, where X^T\displaystyle\hat{X}^{T} is the optimal wealth process for a CRRA investor with a utility function x↦xpp,p=γγ−1\displaystyle x\mapsto\frac{x^{p}}{p},\;p=\frac{\gamma}{\gamma-1} and initial unit wealth. Therefore, in the case of γ∈(0,1)\displaystyle\gamma\in(0,1), we choose X^T\displaystyle\hat{X}^{T} as numéraire under the myopic probability ℚTγ\displaystyle\mathbb{Q}^{\gamma}\_{T}.

#### 3.3.1 Martingale density processes of the myopic probabilities

In Sects. [3.3.1](https://arxiv.org/html/2512.00346v1#S3.SS3.SSS1 "3.3.1 Martingale density processes of the myopic probabilities ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") and [3.3.2](https://arxiv.org/html/2512.00346v1#S3.SS3.SSS2 "3.3.2 Proofs of main results in Sect. 2.3 ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), we consider the quadratic term structure model given by ([7](https://arxiv.org/html/2512.00346v1#S2.E7 "In 2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) and ([8](https://arxiv.org/html/2512.00346v1#S2.E8 "In 2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) and assume Assumptions [2.4](https://arxiv.org/html/2512.00346v1#S2.Thmassumption4 "Assumption 2.4. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") and [2.5](https://arxiv.org/html/2512.00346v1#S2.Thmassumption5 "Assumption 2.5. ‣ 2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models").
In this subsection, we first consider the pricing and hedging problem for a T\displaystyle T-bond (Proposition [3.12](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem12 "Proposition 3.12. ‣ 3.3.1 Martingale density processes of the myopic probabilities ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) and utility maximization problems for CRRA investors (Proposition [3.13](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem13 "Proposition 3.13. ‣ 3.3.1 Martingale density processes of the myopic probabilities ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")).
Using these results, we compute martingale density processes of myopic probabilities ℚTγ\displaystyle\mathbb{Q}^{\gamma}\_{T} (Proposition [3.14](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem14 "Proposition 3.14. ‣ 3.3.1 Martingale density processes of the myopic probabilities ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")).

###### Proposition 3.12.

The price of a T\displaystyle T-bond at time t\displaystyle t is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | F​(t,y)=𝔼ℚ​[exp⁡(−∫tTr​(Yv)​𝑑v)|Yt=y]=exp⁡(−α​(t;T)−β​(t;T)⊤​y−12​y⊤​C​(t;T)​y),F(t,y)=\mathbb{E}^{\mathbb{Q}}\left[\left.\exp\left(-\int\_{t}^{T}r(Y\_{v})dv\right)\right|Y\_{t}=y\right]=\exp\left(-\alpha(t;T)-\beta(t;T)^{\top}y-\frac{1}{2}y^{\top}C(t;T)y\right), |  | (20) |

where α​(⋅;T):[0,T]→ℝ,β​(⋅;T):[0,T]→ℝm,\displaystyle\alpha(\cdot;T):[0,T]\to\mathbb{R},\;\beta(\cdot;T):[0,T]\to\mathbb{R}^{m}, and C​(⋅;T):[0,T]→𝕊+m\displaystyle C(\cdot;T):[0,T]\to\mathbb{S}^{m}\_{+} solve the following system of ordinary differential equations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | C˙​(t)−C​(t)⊤​Λ​Λ⊤​C​(t)+B~⊤​C​(t)+C​(t)​B~+R2=0,C​(T)=0,\displaystyle\displaystyle\begin{aligned} &\dot{C}(t)-C(t)^{\top}\Lambda\Lambda^{\top}C(t)+\tilde{B}^{\top}C(t)+C(t)\tilde{B}+R\_{2}=0,\\ &C(T)=0,\end{aligned} |  | (21) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | β˙​(t)+(B~−Λ​Λ⊤​C​(t))​β​(t)+C⊤​(t)​b~+r1=0,β​(T)=0,\displaystyle\displaystyle\begin{aligned} &\dot{\beta}(t)+(\tilde{B}-\Lambda\Lambda^{\top}C(t))\beta(t)+C^{\top}(t)\tilde{b}+r\_{1}=0,\\ &\beta(T)=0,\\ \end{aligned} |  | (22) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | α˙​(t)+12​Tr​(Λ​Λ⊤​C​(t))−12​β⊤​(t)​Λ​Λ⊤​β​(t)+b~​β​(t)+r0=0,α​(T)=0,\displaystyle\displaystyle\begin{aligned} &\dot{\alpha}(t)+\frac{1}{2}\mathrm{Tr}(\Lambda\Lambda^{\top}C(t))-\frac{1}{2}\beta^{\top}(t)\Lambda\Lambda^{\top}\beta(t)+\tilde{b}\beta(t)+r\_{0}=0,\\ &\alpha(T)=0,\end{aligned} |  | (23) |

where B~≔B−Λ​A,b~≔b−Λ​a\displaystyle\tilde{B}\coloneqq B-\Lambda A,\;\tilde{b}\coloneqq b-\Lambda a.
Furthermore, the portfolio proportion process π^\displaystyle\hat{\pi} that hedges a T\displaystyle T-bond and the corresponding wealth process Xx,π^\displaystyle X^{x,\hat{\pi}} with initial wealth x=F​(0,y)\displaystyle x=F(0,y) are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | π^t\displaystyle\displaystyle\hat{\pi}\_{t} | =−(Λ​Σ−1)⊤​(β​(t;T)+C​(t;T)​Yt),\displaystyle\displaystyle=-(\Lambda\Sigma^{-1})^{\top}\left(\beta(t;T)+C(t;T)Y\_{t}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Xtx,π^\displaystyle\displaystyle X^{x,\hat{\pi}}\_{t} | =F​(t,Yt).\displaystyle\displaystyle=F(t,Y\_{t}). |  |

###### Proof.

This proposition follows from well-known arguments in option pricing theory, which for convenience we include in Appendix [B](https://arxiv.org/html/2512.00346v1#A2 "Appendix B Appendix: Option pricing theory with stochastic factor models in complete markets ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"). By Theorem [B.1](https://arxiv.org/html/2512.00346v1#A2.Thmtheorem1 "Theorem B.1. ‣ Appendix B Appendix: Option pricing theory with stochastic factor models in complete markets ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), it suffices to check that the pricing PDE ([24](https://arxiv.org/html/2512.00346v1#S3.E24 "In 3.3.1 Martingale density processes of the myopic probabilities ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) for a T\displaystyle T-bond has a unique solution F\displaystyle F and (Ht​Xtx,π)\displaystyle(H\_{t}X^{x,\pi}\_{t}) is ℙ\displaystyle\mathbb{P}-martingale, where x\displaystyle x and π\displaystyle\pi are given in terms of the solution F\displaystyle F.
First, the pricing PDE is given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂tF+Dy​F⊤​(b−Λ​a+(B−Λ​A)​y)+12​Tr​[Λ​Λ⊤​Dy​y​F]−r​(y)​F\displaystyle\partial\_{t}F+D\_{y}F^{\top}\left(b-\Lambda a+(B-\Lambda A)y\right)+\frac{1}{2}\mathrm{Tr}\left[\Lambda\Lambda^{\top}D\_{yy}F\right]-r(y)F | =0,\displaystyle=0, |  | (24) |
|  | F​(T,y)\displaystyle F(T,y) | =1.\displaystyle=1. |  |

If F\displaystyle F has the form

|  |  |  |
| --- | --- | --- |
|  | F​(t,y)=exp⁡(−α​(t;T)−β​(t;T)⊤​y−12​y⊤​C​(t;T)​y),F(t,y)=\exp\left(-\alpha(t;T)-\beta(t;T)^{\top}y-\frac{1}{2}y^{\top}C(t;T)y\right), |  |

then α​(⋅;T):[0,T]→ℝ,β​(⋅;T):[0,T]→ℝm,\displaystyle\alpha(\cdot;T):[0,T]\to\mathbb{R},\;\beta(\cdot;T):[0,T]\to\mathbb{R}^{m}, and C​(⋅;T):[0,T]→𝕊+m\displaystyle C(\cdot;T):[0,T]\to\mathbb{S}^{m}\_{+} are solutions to the ODEs (LABEL:C.Riccati), (LABEL:beta.Riccati), and (LABEL:alpha.Riccati).
By Theorem [D.1](https://arxiv.org/html/2512.00346v1#A4.Thmtheorem1 "Theorem D.1. ‣ Appendix D Appendix: Matrix Riccati equation ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), the Riccati equation (LABEL:C.Riccati) has a unique solution, and thus the linear ODEs (LABEL:beta.Riccati) and (LABEL:alpha.Riccati) have unique solutions. Therefore, Theorem [B.1](https://arxiv.org/html/2512.00346v1#A2.Thmtheorem1 "Theorem B.1. ‣ Appendix B Appendix: Option pricing theory with stochastic factor models in complete markets ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")(i) implies that the replicating cost x\displaystyle x, the hedging portfolio proportion process π^=(πt^)t∈[0,T]\displaystyle\hat{\pi}=(\hat{\pi\_{t}})\_{t\in[0,T]}, and the corresponding wealth process Xx,π^\displaystyle X^{x,\hat{\pi}} for a T\displaystyle T-bond are given by

|  |  |  |
| --- | --- | --- |
|  | x=F​(0,y),π^t=−(Λ​Σ−1)⊤​(β​(t;T)+C​(t;T)​Yt),Xtx,π^=F​(t,Yt).\displaystyle\displaystyle x=F(0,y),\quad\hat{\pi}\_{t}=-(\Lambda\Sigma^{-1})^{\top}\left(\beta(t;T)+C(t;T)Y\_{t}\right),\quad X^{x,\hat{\pi}}\_{t}=F(t,Y\_{t}). |  |

By Ito’s formula,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ht​Xtx,π^\displaystyle\displaystyle H\_{t}X^{x,\hat{\pi}}\_{t} | =x+∫0tHs​Xsx,π^​(Σ⊤​π^s−θ​(Ys))⊤​𝑑Ws\displaystyle\displaystyle=x+\int\_{0}^{t}H\_{s}X^{x,\hat{\pi}}\_{s}\left(\Sigma^{\top}\hat{\pi}\_{s}-\theta(Y\_{s})\right)^{\top}dW\_{s} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =x+∫0tHs​Xsx,π^​{−(Λ⊤​C​(s;T)+A)​Ys−Λ⊤​β​(s;T)−a}⊤​𝑑Ws,\displaystyle\displaystyle=x+\int\_{0}^{t}H\_{s}X^{x,\hat{\pi}}\_{s}\left\{-(\Lambda^{\top}C(s;T)+A)Y\_{s}-\Lambda^{\top}\beta(s;T)-a\right\}^{\top}dW\_{s}, |  |

which means that

|  |  |  |
| --- | --- | --- |
|  | Ht​Xtx,π^=x⋅ℰ​(∫0⋅{−(Λ⊤​C​(s;T)+A)​Ys−Λ⊤​β​(s;T)−a}⊤​𝑑Ws)t.\displaystyle\displaystyle H\_{t}X^{x,\hat{\pi}}\_{t}=x\cdot\mathcal{E}\left(\int\_{0}^{\cdot}\left\{-(\Lambda^{\top}C(s;T)+A)Y\_{s}-\Lambda^{\top}\beta(s;T)-a\right\}^{\top}dW\_{s}\right)\_{t}. |  |

By the same argument as in [[27](https://arxiv.org/html/2512.00346v1#bib.bib27), Section 6.2], (Ht​Xtx,π^)\displaystyle(H\_{t}X^{x,\hat{\pi}}\_{t}) is a ℙ\displaystyle\mathbb{P}-martingale and thus Theorem [B.1](https://arxiv.org/html/2512.00346v1#A2.Thmtheorem1 "Theorem B.1. ‣ Appendix B Appendix: Option pricing theory with stochastic factor models in complete markets ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")(ii) implies ([20](https://arxiv.org/html/2512.00346v1#S3.E20 "In Proposition 3.12. ‣ 3.3.1 Martingale density processes of the myopic probabilities ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")).
∎

Next, we recall results on a utility maximization problem for CRRA utility, x↦xpp,p<0\displaystyle x\mapsto\frac{x^{p}}{p},\;p<0.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | V​(t,x,y)\displaystyle V(t,x,y) | ≔supπ∈𝒜​(x)𝔼​[(XTπ)pp|Xtπ=x,Yt=y],\displaystyle\coloneqq\sup\_{\pi\in\mathcal{A}(x)}\mathbb{E}\left[\left.\frac{(X^{\pi}\_{T})^{p}}{p}\right|X^{\pi}\_{t}=x,Y\_{t}=y\right], | (t,x,y)\displaystyle(t,x,y) | ∈[0,T)×(0,∞)×ℝm.\displaystyle\in[0,T)\times(0,\infty)\times\mathbb{R}^{m}. |  | (25) |
|  | V​(T,x,y)\displaystyle V(T,x,y) | ≔xpp,\displaystyle\coloneqq\frac{x^{p}}{p}, | (x,y)\displaystyle(x,y) | ∈(0,∞)×ℝm.\displaystyle\in(0,\infty)\times\mathbb{R}^{m}. |  |

###### Proposition 3.13.

The value function V\displaystyle V is given by

|  |  |  |
| --- | --- | --- |
|  | V​(t,x,y)=xpp​exp⁡(−12​y⊤​P​(t;T)​y−q​(t;T)⊤​y−k​(t;T)),(t,x,y)∈[0,T]×(0,∞)×ℝm,V(t,x,y)=\frac{x^{p}}{p}\exp\left(-\frac{1}{2}y^{\top}P(t;T)y-q(t;T)^{\top}y-k(t;T)\right),\quad(t,x,y)\in[0,T]\times(0,\infty)\times\mathbb{R}^{m}, |  |

where P​(⋅;T):[0,T]→𝕊m,q​(⋅;T):[0,T]→ℝm,k​(⋅;T):[0,T]→ℝ\displaystyle P(\cdot;T):[0,T]\to\mathbb{S}^{m},q(\cdot;T):[0,T]\to\mathbb{R}^{m},k(\cdot;T):[0,T]\to\mathbb{R} satisfy the following system of ODEs:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P˙​(t)−P​(t)⊤​K0​P​(t)+K1⊤​P​(t)+P​(t)​K1+pp−1​A⊤​A−p​R2=0,P​(T)=0,\displaystyle\displaystyle\begin{aligned} &\dot{P}(t)-P(t)^{\top}K\_{0}P(t)+K\_{1}^{\top}P(t)+P(t)K\_{1}+\frac{p}{p-1}A^{\top}A-pR\_{2}=0,\\ &P(T)=0,\end{aligned} |  | (26) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | q˙​(t)+{K1−K0​P​(t)}⊤​q​(t)+P​(t)​b+pp−1​(A−Λ⊤​P​(t))⊤​a−p​r1=0,q​(T)=0,\displaystyle\displaystyle\begin{aligned} &\dot{q}(t)+\left\{K\_{1}-K\_{0}P(t)\right\}^{\top}q(t)+P(t)b+\frac{p}{p-1}\left(A-\Lambda^{\top}P(t)\right)^{\top}a-pr\_{1}=0,\\ &q(T)=0,\end{aligned} |  | (27) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | k˙​(t)+12​Tr​(Λ​Λ⊤​P​(t))+12​(p−1)​q​(t)⊤​Λ​Λ⊤​q​(t)+{b−pp−1​Λ​a}⊤​q​(t)+p2​(p−1)​‖a‖2−p​r0=0,k​(T)=0,\displaystyle\displaystyle\begin{aligned} &\begin{multlined}\dot{k}(t)+\frac{1}{2}\mathrm{Tr}(\Lambda\Lambda^{\top}P(t))+\frac{1}{2(p-1)}q(t)^{\top}\Lambda\Lambda^{\top}q(t)+\left\{b-\frac{p}{p-1}\Lambda a\right\}^{\top}q(t)\\ +\frac{p}{2(p-1)}||a||^{2}-pr\_{0}=0,\end{multlined}\dot{k}(t)+\frac{1}{2}\mathrm{Tr}(\Lambda\Lambda^{\top}P(t))+\frac{1}{2(p-1)}q(t)^{\top}\Lambda\Lambda^{\top}q(t)+\left\{b-\frac{p}{p-1}\Lambda a\right\}^{\top}q(t)\\ +\frac{p}{2(p-1)}||a||^{2}-pr\_{0}=0,\\ &k(T)=0,\end{aligned} |  | (28) |

where K0≔11−p​Λ​Λ⊤,K1≔B−pp−1​Λ​A\displaystyle K\_{0}\coloneqq\frac{1}{1-p}\Lambda\Lambda^{\top},\;K\_{1}\coloneqq B-\frac{p}{p-1}\Lambda A.
Moreover, the optimal portfolio proportion process π^t\displaystyle\hat{\pi}\_{t} and the optimal terminal wealth XTx,π^\displaystyle X^{x,\hat{\pi}}\_{T} for the problem ([25](https://arxiv.org/html/2512.00346v1#S3.E25 "In 3.3.1 Martingale density processes of the myopic probabilities ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) are given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | π^t\displaystyle\displaystyle\hat{\pi}\_{t} | =11−p​(Σ⊤)−1​θ​(Yt)−11−p​(Σ⊤)−1​Λ⊤​(P​(t;T)​Yt+q​(t;T)),\displaystyle\displaystyle=\frac{1}{1-p}(\Sigma^{\top})^{-1}\theta(Y\_{t})-\frac{1}{1-p}(\Sigma^{\top})^{-1}\Lambda^{\top}\left(P(t;T)Y\_{t}+q(t;T)\right), |  | (29) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | XTx,π^\displaystyle\displaystyle X^{x,\hat{\pi}}\_{T} | =x​HTq−1𝔼​[HTq].\displaystyle\displaystyle=x\frac{H\_{T}^{q-1}}{\mathbb{E}[H\_{T}^{q}]}. |  | (30) |

###### Proof.

By Theorem [D.1](https://arxiv.org/html/2512.00346v1#A4.Thmtheorem1 "Theorem D.1. ‣ Appendix D Appendix: Matrix Riccati equation ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), the Riccati equation (LABEL:P.Riccati) and linear ODEs (LABEL:q.Riccati) and (LABEL:k.Riccati) have unique solutions. Therefore

|  |  |  |
| --- | --- | --- |
|  | V​(t,x,y)≔xpp​exp⁡(−12​y⊤​P​(t;T)​y−q​(t;T)⊤​y−k​(t;T)),(t,x,y)∈[0,T]×(0,∞)×ℝmV(t,x,y)\coloneqq\frac{x^{p}}{p}\exp\left(-\frac{1}{2}y^{\top}P(t;T)y-q(t;T)^{\top}y-k(t;T)\right),\quad(t,x,y)\in[0,T]\times(0,\infty)\times\mathbb{R}^{m} |  |

is the solution to the HJB equation,

|  |  |  |
| --- | --- | --- |
|  | Vt+x​r​(y)​Vx+(b+B​y)⊤​Dy​V+12​Tr​(Λ​Λ⊤​Dy​y2​V)−12​Vx​x​|θ​(y)​Vx+Λ⊤​Dy​Vx|2=0,\displaystyle\displaystyle V\_{t}+xr(y)V\_{x}+(b+By)^{\top}D\_{y}V+\frac{1}{2}\mathrm{Tr}(\Lambda\Lambda^{\top}D^{2}\_{yy}V)-\frac{1}{2V\_{xx}}\left|\theta(y)V\_{x}+\Lambda^{\top}D\_{y}V\_{x}\right|^{2}=0, |  |
|  |  |  |
| --- | --- | --- |
|  | V​(T,x,y)=xpp,\displaystyle\displaystyle V(T,x,y)=\frac{x^{p}}{p}, |  |

and the candidate for the optimal portfolio proportion process π^\displaystyle\hat{\pi} is given by

|  |  |  |
| --- | --- | --- |
|  | π^t=11−p​(Σ⊤)−1​θ​(Yt)−11−p​(Σ⊤)−1​Λ⊤​(P​(t;T)​Yt+q​(t;T)).\hat{\pi}\_{t}=\frac{1}{1-p}(\Sigma^{\top})^{-1}\theta(Y\_{t})-\frac{1}{1-p}(\Sigma^{\top})^{-1}\Lambda^{\top}\left(P(t;T)Y\_{t}+q(t;T)\right). |  |

Here, we do not use standard verification arguments. Instead, we directly show that the terminal wealth obtained by the candidate π^\displaystyle\hat{\pi} matches that of the martingale methods, that is, we establish the identity ([30](https://arxiv.org/html/2512.00346v1#S3.E30 "In Proposition 3.13. ‣ 3.3.1 Martingale density processes of the myopic probabilities ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")). To do so, Theorem [C.1](https://arxiv.org/html/2512.00346v1#A3.Thmtheorem1 "Theorem C.1. ‣ Appendix C Appendix: Relationship between stochastic control methods and martingale methods ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") implies that it suffices to check that (Ht​Xtx,π^)t∈[0,T]\displaystyle\left(H\_{t}X^{x,\hat{\pi}}\_{t}\right)\_{t\in[0,T]} is a ℙ\displaystyle\mathbb{P}-martingale. Because

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ht​Xtx,π^\displaystyle H\_{t}X^{x,\hat{\pi}}\_{t} | =x⋅ℰ​(∫0⋅(Σ⊤​π^s−θ​(Ys))⊤​𝑑Ws)\displaystyle=x\cdot\mathcal{E}\left(\int\_{0}^{\cdot}\left(\Sigma^{\top}\hat{\pi}\_{s}-\theta(Y\_{s})\right)^{\top}dW\_{s}\right) |  | (31) |
|  |  | =x⋅ℰ​(∫0⋅(−pp−1​θ​(Ys)+1p−1​Λ⊤​(P​(s;T)​Ys+q​(s;T)))⊤​𝑑Ws)\displaystyle=x\cdot\mathcal{E}\left(\int\_{0}^{\cdot}\left(-\frac{p}{p-1}\theta(Y\_{s})+\frac{1}{p-1}\Lambda^{\top}\left(P(s;T)Y\_{s}+q(s;T)\right)\right)^{\top}dW\_{s}\right) |  |
|  |  | =x⋅ℰ​(∫0⋅{(−pp−1​A+1p−1​Λ⊤​P​(s;T))​Ys−pp−1​a+1p−1​Λ⊤​q​(s;T)}⊤​𝑑Ws)t,\displaystyle=x\cdot\mathcal{E}\left(\int\_{0}^{\cdot}\left\{\left(-\frac{p}{p-1}A+\frac{1}{p-1}\Lambda^{\top}P(s;T)\right)Y\_{s}-\frac{p}{p-1}a+\frac{1}{p-1}\Lambda^{\top}q(s;T)\right\}^{\top}dW\_{s}\right)\_{t}, |  |

the same argument as in [[27](https://arxiv.org/html/2512.00346v1#bib.bib27), Section 6.2] implies that (Ht​Xtx,π^)t∈[0,T]\displaystyle\left(H\_{t}X^{x,\hat{\pi}}\_{t}\right)\_{t\in[0,T]} is a ℙ\displaystyle\mathbb{P}-martingale, which completes the proof.
∎

###### Remark 3.2.

If p<0\displaystyle p<0, P​(t;T):[0,T]→𝕊+m\displaystyle P(t;T):[0,T]\to\mathbb{S}^{m}\_{+} always exists. If 0<p<1\displaystyle 0<p<1, the solution P\displaystyle P may blow up at a finite time. See [[15](https://arxiv.org/html/2512.00346v1#bib.bib15)] for details.

###### Proposition 3.14.

Let γ∈[0,1]\displaystyle\gamma\in[0,1]. We denote by Pγ,qγ\displaystyle P^{\gamma},q^{\gamma} the solutions to the system of ODEs (LABEL:P.Riccati), (LABEL:q.Riccati) for p=γγ−1,γ∈(0,1)\displaystyle p=\frac{\gamma}{\gamma-1},\;\gamma\in(0,1). Let Cγ​(⋅;T):[0,T]→𝕊+m,βγ​(⋅;T):[0,T]→ℝm\displaystyle C^{\gamma}(\cdot;T):[0,T]\to\mathbb{S}^{m}\_{+},\;\beta^{\gamma}(\cdot;T):[0,T]\to\mathbb{R}^{m} be given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cγ​(t;T)\displaystyle\displaystyle C^{\gamma}(t;T) | ≔{0,t∈[0,T],γ=0,(1−γ)​Pγ​(t;T),t∈[0,T],γ∈(0,1),C​(t;T),t∈[0,T],γ=1,\displaystyle\displaystyle\coloneqq\begin{cases}0,&t\in[0,T],\;\gamma=0,\\ (1-\gamma)P^{\gamma}(t;T),&t\in[0,T],\;\gamma\in(0,1),\\ C(t;T),&t\in[0,T],\;\gamma=1,\end{cases} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | βγ​(t;T)\displaystyle\displaystyle\beta^{\gamma}(t;T) | ≔{0,t∈[0,T],γ=0,(1−γ)​qγ​(t;T),t∈[0,T],γ∈(0,1),β​(t;T),t∈[0,T],γ=1.\displaystyle\displaystyle\coloneqq\begin{cases}0,&t\in[0,T],\;\gamma=0,\\ (1-\gamma)q^{\gamma}(t;T),&t\in[0,T],\;\gamma\in(0,1),\\ \beta(t;T),&t\in[0,T],\;\gamma=1.\end{cases} |  |

Then, the martingale density processes of myopic probability measures ℚTγ\displaystyle\mathbb{Q}^{\gamma}\_{T} are given by

|  |  |  |
| --- | --- | --- |
|  | MTγ=ℰ​(∫0⋅[−{γ​A+Λ⊤​Cγ​(t;T)}​Yt−{γ​a+Λ⊤​βγ​(t;T)}]⊤​𝑑Wt)T.M^{\gamma}\_{T}=\mathcal{E}\left(\int\_{0}^{\cdot}\left[-\left\{\gamma A+\Lambda^{\top}C^{\gamma}(t;T)\right\}Y\_{t}-\left\{\gamma a+\Lambda^{\top}\beta^{\gamma}(t;T)\right\}\right]^{\top}dW\_{t}\right)\_{T}. |  |

Hence, WℚTγ=(WtℚTγ)t∈[0,T]\displaystyle W^{\mathbb{Q}^{\gamma}\_{T}}=\left(W^{\mathbb{Q}^{\gamma}\_{T}}\_{t}\right)\_{t\in[0,T]}, given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | WtℚTγ≔Wt+{(γ​A+Λ⊤​Cγ​(t;T))​Yt+(γ​a+Λ⊤​βγ​(t;T))}​d​t,W^{\mathbb{Q}^{\gamma}\_{T}}\_{t}\coloneqq W\_{t}+\left\{\left(\gamma A+\Lambda^{\top}C^{\gamma}(t;T)\right)Y\_{t}+\left(\gamma a+\Lambda^{\top}\beta^{\gamma}(t;T)\right)\right\}dt, |  | (32) |

is an n\displaystyle n-dimensional Brownian motion under the myopic probability ℚTγ\displaystyle\mathbb{Q}^{\gamma}\_{T}.
Moreover, Y=(Yt)t∈[0,T]\displaystyle Y=(Y\_{t})\_{t\in[0,T]} satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Yt={b−γ​Λ​a−Λ​Λ⊤​βγ​(t;T)+(B−γ​Λ​A−Λ​Λ⊤​Cγ​(t;T))​Yt}​d​t+Λ​d​WtℚTγ,Y0=y.dY\_{t}=\left\{b-\gamma\Lambda a-\Lambda\Lambda^{\top}\beta^{\gamma}(t;T)+\left(B-\gamma\Lambda A-\Lambda\Lambda^{\top}C^{\gamma}(t;T)\right)Y\_{t}\right\}dt+\Lambda dW^{\mathbb{Q}^{\gamma}\_{T}}\_{t},\quad Y\_{0}=y. |  | (33) |

###### Proof.

For γ=0\displaystyle\gamma=0, ℚTγ=ℙ\displaystyle\mathbb{Q}^{\gamma}\_{T}=\mathbb{P} and the statements follow immediately. For γ=1\displaystyle\gamma=1, by Proposition [3.12](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem12 "Proposition 3.12. ‣ 3.3.1 Martingale density processes of the myopic probabilities ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") and its proof, the state price density process H\displaystyle H admits the following stochastic exponential representation:

|  |  |  |
| --- | --- | --- |
|  | HT𝔼​[HT]=ℰ​(∫0⋅{−(Λ⊤​C​(s;T)+A)​Ys−Λ⊤​β​(s;T)−a}⊤​𝑑Ws)T.\frac{H\_{T}}{\mathbb{E}[H\_{T}]}=\mathcal{E}\left(\int\_{0}^{\cdot}\left\{-(\Lambda^{\top}C(s;T)+A)Y\_{s}-\Lambda^{\top}\beta(s;T)-a\right\}^{\top}dW\_{s}\right)\_{T}. |  |

From Girsanov’s theorem, WℚTγ\displaystyle W^{\mathbb{Q}^{\gamma}\_{T}} given by ([32](https://arxiv.org/html/2512.00346v1#S3.E32 "In Proposition 3.14. ‣ 3.3.1 Martingale density processes of the myopic probabilities ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) is a Brownian motion under ℚTγ\displaystyle\mathbb{Q}^{\gamma}\_{T} and ([33](https://arxiv.org/html/2512.00346v1#S3.E33 "In Proposition 3.14. ‣ 3.3.1 Martingale density processes of the myopic probabilities ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) follows. Therefore, the statements hold for γ=1\displaystyle\gamma=1.
Next, we consider the case of γ∈(0,1)\displaystyle\gamma\in(0,1). By Proposition [3.13](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem13 "Proposition 3.13. ‣ 3.3.1 Martingale density processes of the myopic probabilities ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") and ([31](https://arxiv.org/html/2512.00346v1#S3.E31 "In 3.3.1 Martingale density processes of the myopic probabilities ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) for p=γγ−1\displaystyle p=\frac{\gamma}{\gamma-1}, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | MTγ\displaystyle\displaystyle M^{\gamma}\_{T} | =HT⋅HTγ−1𝔼​[HTγ]\displaystyle\displaystyle=H\_{T}\cdot\frac{H\_{T}^{\gamma-1}}{\mathbb{E}[H\_{T}^{\gamma}]} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1x⋅HT​XTx,π^\displaystyle\displaystyle=\frac{1}{x}\cdot H\_{T}X^{x,\hat{\pi}}\_{T} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℰ​(∫0⋅[{−γ​A+(γ−1)​Λ⊤​Pγ​(s;T)}​Ys−{γ​a+(1−γ)​Λ⊤​qγ​(s;T)}]⊤​𝑑Ws)T\displaystyle\displaystyle=\mathcal{E}\left(\int\_{0}^{\cdot}\left[\left\{-\gamma A+(\gamma-1)\Lambda^{\top}P^{\gamma}(s;T)\right\}Y\_{s}-\left\{\gamma a+(1-\gamma)\Lambda^{\top}q^{\gamma}(s;T)\right\}\right]^{\top}dW\_{s}\right)\_{T} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =ℰ​(∫0⋅[−{γ​A+Λ⊤​Cγ​(t;T)}​Yt−{γ​a+Λ⊤​βγ​(t;T)}]⊤​𝑑Wt)T.\displaystyle\displaystyle=\mathcal{E}\left(\int\_{0}^{\cdot}\left[-\left\{\gamma A+\Lambda^{\top}C^{\gamma}(t;T)\right\}Y\_{t}-\left\{\gamma a+\Lambda^{\top}\beta^{\gamma}(t;T)\right\}\right]^{\top}dW\_{t}\right)\_{T}. |  |

By Girsanov’s theorem again, the statements follow for γ∈(0,1)\displaystyle\gamma\in(0,1).
∎

###### Remark 3.3.

By (LABEL:P.Riccati) and (LABEL:q.Riccati), for γ∈(0,1)\displaystyle\gamma\in(0,1), Cγ​(⋅;T)\displaystyle C^{\gamma}(\cdot;T) and βγ​(⋅;T)\displaystyle\beta^{\gamma}(\cdot;T) satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | C˙γ​(t)−Cγ​(t)⊤​Λ​Λ⊤​Cγ​(t)+K1⊤​Cγ​(t)+Cγ​(t)​K1+γ​(1−γ)​A⊤​A+γ​R2=0,Cγ​(T)=0,\displaystyle\displaystyle\begin{aligned} &\dot{C}^{\gamma}(t)-C^{\gamma}(t)^{\top}\Lambda\Lambda^{\top}C^{\gamma}(t)+K\_{1}^{\top}C^{\gamma}(t)+C^{\gamma}(t)K\_{1}+\gamma(1-\gamma)A^{\top}A+\gamma R\_{2}=0,\\ &C^{\gamma}(T)=0,\end{aligned} |  | (34) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | β˙γ​(t)+{K1−Λ​Λ⊤​Cγ​(t)}⊤​βγ​(t)+Cγ​(t)​{b−γ​Λ​a}+γ​(1−γ)​A⊤​a+γ​r1=0,βγ​(T)=0,\displaystyle\displaystyle\begin{aligned} &\dot{\beta}^{\gamma}(t)+\left\{K\_{1}-\Lambda\Lambda^{\top}C^{\gamma}(t)\right\}^{\top}\beta^{\gamma}(t)+C^{\gamma}(t)\{b-\gamma\Lambda a\}+\gamma(1-\gamma)A^{\top}a+\gamma r\_{1}=0,\\ &\beta^{\gamma}(T)=0,\end{aligned} |  | (35) |

where K1≔B−γ​Λ​A\displaystyle K\_{1}\coloneqq B-\gamma\Lambda A.
Compared with (LABEL:C.Riccati) and (LABEL:beta.Riccati), Cγ​(⋅;T)\displaystyle C^{\gamma}(\cdot;T) and βγ​(⋅;T)\displaystyle\beta^{\gamma}(\cdot;T) seem to converge to C1​(⋅;T)≔C​(⋅;T)\displaystyle C^{1}(\cdot;T)\coloneqq C(\cdot;T) and β1​(⋅;T)≔β​(⋅;T)\displaystyle\beta^{1}(\cdot;T)\coloneqq\beta(\cdot;T) in some sense as γ↗1\displaystyle\gamma\nearrow 1. However, we do not prove it because it is not needed for our main results.

#### 3.3.2 Proofs of main results in Sect. [2.3](https://arxiv.org/html/2512.00346v1#S2.SS3 "2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")

In this subsection, we first consider the asymptotic behavior of Cγ​(t;T)\displaystyle C^{\gamma}(t;T) and βγ​(t;T)\displaystyle\beta^{\gamma}(t;T) when T↗∞\displaystyle T\nearrow\infty (Proposition [3.15](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem15 "Proposition 3.15. ‣ 3.3.2 Proofs of main results in Sect. 2.3 ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")), which affects the asymptotic moments of Yt\displaystyle Y\_{t} under myopic probabilities ℚ𝕋γ\displaystyle\mathbb{Q^{\gamma}\_{T}}. Using this proposition, we show

|  |  |  |
| --- | --- | --- |
|  | supt∈[0,T]𝔼ℚTγ​[|Yt|2]=O​(1),𝔼ℚTγ​[|LT|]=O​(1),(T↗∞)\sup\_{t\in[0,T]}\mathbb{E}^{\mathbb{Q}^{\gamma}\_{T}}[|Y\_{t}|^{2}]=O(1),\quad\quad\mathbb{E}^{\mathbb{Q}^{\gamma}\_{T}}[|L\_{T}|]=O(1),\quad(T\nearrow\infty) |  |

in Propositions [3.16](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem16 "Proposition 3.16. ‣ 3.3.2 Proofs of main results in Sect. 2.3 ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") and [3.17](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem17 "Proposition 3.17. ‣ 3.3.2 Proofs of main results in Sect. 2.3 ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models").
Combining these estimates with Proposition [3.11](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem11 "Proposition 3.11. ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), we can derive the rate of the turnpike theorem for excess hedging demands (Theorem [2.7](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem7 "Theorem 2.7. ‣ 2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")). We can also prove the uniform turnpike theorem (Theorem [2.8](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem8 "Theorem 2.8. ‣ 2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) by the same arguments as in the case of myopic portfolios.

###### Proposition 3.15.

For γ∈{q,α+1,1}\displaystyle\gamma\in\{q,\alpha+1,1\}, there exist C∞γ∈𝕊+m\displaystyle C^{\gamma}\_{\infty}\in\mathbb{S}^{m}\_{+} and β∞γ∈ℝm\displaystyle\beta^{\gamma}\_{\infty}\in\mathbb{R}^{m} such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | limT↗∞Cγ​(t;T)\displaystyle\displaystyle\lim\_{T\nearrow\infty}C^{\gamma}(t;T) | =C∞γ,\displaystyle\displaystyle=C^{\gamma}\_{\infty}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | limT↗∞βγ​(t;T)\displaystyle\displaystyle\lim\_{T\nearrow\infty}\beta^{\gamma}(t;T) | =β∞γ\displaystyle\displaystyle=\beta^{\gamma}\_{\infty} |  |

for any t\displaystyle t. In addition, B−γ​Λ​A−Λ​Λ⊤​C∞γ\displaystyle B-\gamma\Lambda A-\Lambda\Lambda^{\top}C^{\gamma}\_{\infty} is stable.

###### Proof.

Because the statements for γ=0\displaystyle\gamma=0 are obvious and those for γ=1\displaystyle\gamma=1 are along the lines for the case of γ∈(0,1)\displaystyle\gamma\in(0,1), we consider only the case of γ∈(0,1)\displaystyle\gamma\in(0,1). As Remark [3.3](https://arxiv.org/html/2512.00346v1#S3.Thmremark3 "Remark 3.3. ‣ 3.3.1 Martingale density processes of the myopic probabilities ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") shows, Cγ​(⋅;T)\displaystyle C^{\gamma}(\cdot;T) and βγ​(⋅;T)\displaystyle\beta^{\gamma}(\cdot;T) satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | C˙γ​(t)−Cγ​(t)⊤​Λ​Λ⊤​Cγ​(t)+K1⊤​Cγ​(t)+Cγ​(t)​K1+γ​(1−γ)​A⊤​A+γ​R2=0,Cγ​(T)=0,\displaystyle\displaystyle\begin{aligned} &\dot{C}^{\gamma}(t)-C^{\gamma}(t)^{\top}\Lambda\Lambda^{\top}C^{\gamma}(t)+K\_{1}^{\top}C^{\gamma}(t)+C^{\gamma}(t)K\_{1}+\gamma(1-\gamma)A^{\top}A+\gamma R\_{2}=0,\\ &C^{\gamma}(T)=0,\end{aligned} |  | (36) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | β˙γ​(t)+{K1−Λ​Λ⊤​Cγ​(t)}⊤​βγ​(t)+Cγ​(t)​{b−γ​Λ​a}+γ​(1−γ)​A⊤​a+γ​r1=0,βγ​(T)=0,\displaystyle\displaystyle\begin{aligned} &\dot{\beta}^{\gamma}(t)+\left\{K\_{1}-\Lambda\Lambda^{\top}C^{\gamma}(t)\right\}^{\top}\beta^{\gamma}(t)+C^{\gamma}(t)\{b-\gamma\Lambda a\}+\gamma(1-\gamma)A^{\top}a+\gamma r\_{1}=0,\\ &\beta^{\gamma}(T)=0,\end{aligned} |  | (37) |

where K1≔B−γ​Λ​A\displaystyle K\_{1}\coloneqq B-\gamma\Lambda A. By Theorems [D.2](https://arxiv.org/html/2512.00346v1#A4.Thmtheorem2 "Theorem D.2. ‣ Appendix D Appendix: Matrix Riccati equation ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") and [D.3](https://arxiv.org/html/2512.00346v1#A4.Thmtheorem3 "Theorem D.3. ‣ Appendix D Appendix: Matrix Riccati equation ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), we have to check that (K1,Λ)\displaystyle\left(K\_{1},\Lambda\right) is stabilizable and (C,K1)\displaystyle\left(C,K\_{1}\right) is detectable, where C∈ℝn×m\displaystyle C\in\mathbb{R}^{n\times m} satisfies C⊤​C=γ​(1−γ)​A⊤​A+γ​R2\displaystyle C^{\top}C=\gamma(1-\gamma)A^{\top}A+\gamma R\_{2}. The stabilizability of (K1,Λ)\displaystyle\left(K\_{1},\Lambda\right) can be seen from the fact that

|  |  |  |
| --- | --- | --- |
|  | K1+Λ​L=B\displaystyle\displaystyle K\_{1}+\Lambda L=B |  |

is stable when setting L≔γ​A\displaystyle L\coloneqq\gamma A. To see the detectability of (C,K1)\displaystyle\left(C,K\_{1}\right), we consider two cases of (iii) in Assumption [2.5](https://arxiv.org/html/2512.00346v1#S2.Thmassumption5 "Assumption 2.5. ‣ 2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"). If R2=0\displaystyle R\_{2}=0, then C=γ​(1−γ)​A\displaystyle C=\sqrt{\gamma(1-\gamma)}A and setting F=γ1−γ​Λ\displaystyle F=\sqrt{\frac{\gamma}{1-\gamma}}\Lambda implies that

|  |  |  |
| --- | --- | --- |
|  | F​C+K1=B,FC+K\_{1}=B, |  |

which means that (C,K1)\displaystyle\left(C,K\_{1}\right) is detectable. If (γ​(1−γ)​A⊤​A+γ​R2)\displaystyle\left(\gamma(1-\gamma)A^{\top}A+\gamma R\_{2}\right) is positive definite, then C≔(γ​(1−γ)​A⊤​A+γ​R2)12\displaystyle C\coloneqq\left(\gamma(1-\gamma)A^{\top}A+\gamma R\_{2}\right)^{\frac{1}{2}} is positive definite and thus (C,K1)\displaystyle\left(C,K\_{1}\right) is detectable. As a result, by Theorems [D.2](https://arxiv.org/html/2512.00346v1#A4.Thmtheorem2 "Theorem D.2. ‣ Appendix D Appendix: Matrix Riccati equation ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") and [D.3](https://arxiv.org/html/2512.00346v1#A4.Thmtheorem3 "Theorem D.3. ‣ Appendix D Appendix: Matrix Riccati equation ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models"), C∞γ≔limT↗∞Cγ​(t;T)\displaystyle C^{\gamma}\_{\infty}\coloneqq\lim\_{T\nearrow\infty}C^{\gamma}(t;T) and β∞γ≔limT↗∞βγ​(t;T)\displaystyle\beta^{\gamma}\_{\infty}\coloneqq\lim\_{T\nearrow\infty}\beta^{\gamma}(t;T) exist for any t≥0\displaystyle t\geq 0 and satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | −C∞γ​Λ​Λ⊤​C∞γ+K1⊤​C∞γ+C∞γ​K1+γ​(1−γ)​A⊤​A+γ​R2\displaystyle\displaystyle-C^{\gamma}\_{\infty}\Lambda\Lambda^{\top}C^{\gamma}\_{\infty}+K\_{1}^{\top}C^{\gamma}\_{\infty}+C^{\gamma}\_{\infty}K\_{1}+\gamma(1-\gamma)A^{\top}A+\gamma R\_{2} | =0,\displaystyle\displaystyle=0, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | {K1−Λ​Λ⊤​C∞γ}⊤​β∞γ+C∞γ​{b−γ​Λ​a}+γ​(1−γ)​A⊤​a+γ​r1\displaystyle\displaystyle\left\{K\_{1}-\Lambda\Lambda^{\top}C^{\gamma}\_{\infty}\right\}^{\top}\beta^{\gamma}\_{\infty}+C^{\gamma}\_{\infty}\{b-\gamma\Lambda a\}+\gamma(1-\gamma)A^{\top}a+\gamma r\_{1} | =0,\displaystyle\displaystyle=0, |  |

and

|  |  |  |
| --- | --- | --- |
|  | K1−Λ​Λ⊤​C∞γ=B−γ​Λ​A−Λ​Λ⊤​C∞γ\displaystyle\displaystyle K\_{1}-\Lambda\Lambda^{\top}C\_{\infty}^{\gamma}=B-\gamma\Lambda A-\Lambda\Lambda^{\top}C^{\gamma}\_{\infty} |  |

is stable.
∎

###### Proposition 3.16.

For γ∈{q,α+1,1}\displaystyle\gamma\in\{q,\alpha+1,1\},

|  |  |  |
| --- | --- | --- |
|  | supt∈[0,T]𝔼ℚTγ​[|Yt|2]=O​(1),(T↗∞).\sup\_{t\in[0,T]}\mathbb{E}^{\mathbb{Q}^{\gamma}\_{T}}[|Y\_{t}|^{2}]=O(1),\quad(T\nearrow\infty). |  |

###### Proof.

We define β~γ,C~γ\displaystyle\tilde{\beta}^{\gamma},\tilde{C}^{\gamma} by

|  |  |  |  |
| --- | --- | --- | --- |
|  | β~γ​(t;T)\displaystyle\displaystyle\tilde{\beta}^{\gamma}(t;T) | ≔b−γ​Λ​a−Λ​Λ⊤​βγ​(t;T),\displaystyle\displaystyle\coloneqq b-\gamma\Lambda a-\Lambda\Lambda^{\top}\beta^{\gamma}(t;T), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | C~γ​(t;T)\displaystyle\displaystyle\tilde{C}^{\gamma}(t;T) | ≔B−γ​Λ​A−Λ​Λ⊤​Cγ​(t;T),\displaystyle\displaystyle\coloneqq B-\gamma\Lambda A-\Lambda\Lambda^{\top}C^{\gamma}(t;T), |  |

and the SDE ([33](https://arxiv.org/html/2512.00346v1#S3.E33 "In Proposition 3.14. ‣ 3.3.1 Martingale density processes of the myopic probabilities ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) becomes

|  |  |  |
| --- | --- | --- |
|  | d​Yt=(β~γ​(t;T)+C~γ​(t;T)​Yt)​d​t+Λ​d​WtℚTγ,Y0=y.dY\_{t}=\left(\tilde{\beta}^{\gamma}(t;T)+\tilde{C}^{\gamma}(t;T)Y\_{t}\right)dt+\Lambda dW^{\mathbb{Q}^{\gamma}\_{T}}\_{t},\quad Y\_{0}=y. |  |

Because C~∞γ≔limT↗∞C~γ​(t;T)=B−γ​Λ​A−Λ​Λ⊤​C∞γ\displaystyle\tilde{C}^{\gamma}\_{\infty}\coloneqq\lim\_{T\nearrow\infty}\tilde{C}^{\gamma}(t;T)=B-\gamma\Lambda A-\Lambda\Lambda^{\top}C^{\gamma}\_{\infty} is stable, there exists U∈𝕊++m\displaystyle U\in\mathbb{S}^{m}\_{++} such that

|  |  |  |
| --- | --- | --- |
|  | (C~∞γ)⊤​U+U​C~∞γ<0.(\tilde{C}^{\gamma}\_{\infty})^{\top}U+U\tilde{C}^{\gamma}\_{\infty}<0. |  |

Therefore, there exist T1,ϵ>0\displaystyle T\_{1},\epsilon>0 such that

|  |  |  |
| --- | --- | --- |
|  | T−t≥T1⇒C~γ​(t;T)⊤​U+U​C~γ​(t;T)<−ϵ​Im,T-t\geq T\_{1}\Rightarrow\tilde{C}^{\gamma}(t;T)^{\top}U+U\tilde{C}^{\gamma}(t;T)<-\epsilon I\_{m}, |  |

where Im\displaystyle I\_{m} is an m×m\displaystyle m\times m identity matrix.
For 0≤s≤t≤T\displaystyle 0\leq s\leq t\leq T,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℚTγ​[⟨U​Yt,Yt⟩]\displaystyle\displaystyle\mathbb{E}^{\mathbb{Q}^{\gamma}\_{T}}\left[\langle UY\_{t},Y\_{t}\rangle\right] | =𝔼ℚTγ​[⟨U​Ys,Ys⟩]+∫st𝔼ℚTγ​[⟨(C~γ​(u;T)⊤​U+U​C~γ​(u;T))​Yu,Yu⟩+2​⟨U​β~γ​(u;T),Yu⟩]​𝑑u\displaystyle\displaystyle=\mathbb{E}^{\mathbb{Q}^{\gamma}\_{T}}\left[\langle UY\_{s},Y\_{s}\rangle\right]+\int\_{s}^{t}\mathbb{E}^{\mathbb{Q}^{\gamma}\_{T}}\left[\left\langle\left(\tilde{C}^{\gamma}(u;T)^{\top}U+U\tilde{C}^{\gamma}(u;T)\right)Y\_{u},Y\_{u}\right\rangle+2\left\langle U\tilde{\beta}^{\gamma}(u;T),Y\_{u}\right\rangle\right]du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +Tr​(U⊤​Λ​Λ⊤)​(t−s).\displaystyle\displaystyle\qquad\qquad\qquad\qquad\qquad+\mathrm{Tr}(U^{\top}\Lambda\Lambda^{\top})(t-s). |  |

Because U\displaystyle U is positive definite, the maximum and minimum of the eigenvalues, λmin,λmax>0\displaystyle\lambda\_{\min},\lambda\_{\max}>0, satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | λmin​|y|2≤⟨U​y,y⟩≤λmax​|y|2\lambda\_{\min}|y|^{2}\leq\langle Uy,y\rangle\leq\lambda\_{\max}|y|^{2} |  | (38) |

for all y∈ℝm\displaystyle y\in\mathbb{R}^{m}. Moreover, because the function β~\displaystyle\tilde{\beta} is a bounded function of (t,T)\displaystyle(t,T), there exist positive constants C\displaystyle C such that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 2ϵ​|U​β~​(t;T)|2+Tr​(U⊤​Λ​Λ⊤)≤C\displaystyle\displaystyle\frac{2}{\epsilon}|U\tilde{\beta}(t;T)|^{2}+\mathrm{Tr}(U^{\top}\Lambda\Lambda^{\top})\leq C |  | (39) |

for any t,T\displaystyle t,T with 0≤t≤T\displaystyle 0\leq t\leq T. From the above inequalities ([38](https://arxiv.org/html/2512.00346v1#S3.E38 "In 3.3.2 Proofs of main results in Sect. 2.3 ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) and ([39](https://arxiv.org/html/2512.00346v1#S3.E39 "In 3.3.2 Proofs of main results in Sect. 2.3 ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")), it follows that for t∈[0,T−T1]\displaystyle t\in[0,T-T\_{1}],

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​t​𝔼ℚTγ​[⟨U​Yt,Yt⟩]\displaystyle\displaystyle\frac{d}{dt}\mathbb{E}^{\mathbb{Q}^{\gamma}\_{T}}\left[\langle UY\_{t},Y\_{t}\rangle\right] | =𝔼ℚTγ​[⟨(C~γ​(t;T)⊤​U+U​C~γ​(t;T))​Yt,Yt⟩+2​⟨U​β~γ​(t;T),Yt⟩]+Tr​(U⊤​Λ​Λ⊤)\displaystyle\displaystyle=\mathbb{E}^{\mathbb{Q}^{\gamma}\_{T}}\left[\left\langle\left(\tilde{C}^{\gamma}(t;T)^{\top}U+U\tilde{C}^{\gamma}(t;T)\right)Y\_{t},Y\_{t}\right\rangle+2\left\langle U\tilde{\beta}^{\gamma}(t;T),Y\_{t}\right\rangle\right]+\mathrm{Tr}(U^{\top}\Lambda\Lambda^{\top}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤−ϵ​𝔼ℚTγ​[|Yt|2]+2​𝔼ℚTγ​[⟨U​β~​(t;T),Yt⟩]+Tr​(U⊤​Λ​Λ⊤)\displaystyle\displaystyle\leq-\epsilon\mathbb{E}^{\mathbb{Q}^{\gamma}\_{T}}\left[|Y\_{t}|^{2}\right]+2\mathbb{E}^{\mathbb{Q}^{\gamma}\_{T}}\left[\langle U\tilde{\beta}(t;T),Y\_{t}\rangle\right]+\mathrm{Tr}(U^{\top}\Lambda\Lambda^{\top}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤−ϵ2​𝔼ℚTγ​[|Yt|2]+2ϵ​|U​β~​(t;T)|2+Tr​(U⊤​Λ​Λ⊤)\displaystyle\displaystyle\leq-\frac{\epsilon}{2}\mathbb{E}^{\mathbb{Q}^{\gamma}\_{T}}\left[|Y\_{t}|^{2}\right]+\frac{2}{\epsilon}|U\tilde{\beta}(t;T)|^{2}+\mathrm{Tr}(U^{\top}\Lambda\Lambda^{\top}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤−ϵ2​λmax​𝔼ℚTγ​[⟨U​Yt,Yt⟩]+C,\displaystyle\displaystyle\leq-\frac{\epsilon}{2\lambda\_{\max}}\mathbb{E}^{\mathbb{Q}^{\gamma}\_{T}}\left[\langle UY\_{t},Y\_{t}\rangle\right]+C, |  |

where the second inequality follows from ϵ\displaystyle\epsilon-Hölder’s inequality.
By Gronwall’s inequality, there exists a constant C=C​(y)\displaystyle C=C(y) which depends only on y\displaystyle y such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℚTγ​[⟨U​Yt,Yt⟩]≤C​(y),t∈[0,T−T1].\mathbb{E}^{\mathbb{Q}^{\gamma}\_{T}}\left[\langle UY\_{t},Y\_{t}\rangle\right]\leq C(y),\quad t\in[0,T-T\_{1}]. |  |

The above inequalities and the right-hand side of ([38](https://arxiv.org/html/2512.00346v1#S3.E38 "In 3.3.2 Proofs of main results in Sect. 2.3 ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) lead to

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℚTγ​[|Yt|2]≤C​(y)λmin,t∈[0,T−T1].\mathbb{E}^{\mathbb{Q}^{\gamma}\_{T}}\left[|Y\_{t}|^{2}\right]\leq\frac{C(y)}{\lambda\_{\min}},\quad t\in[0,T-T\_{1}]. |  |

Furthermore, because the length of [T−T1,T]\displaystyle[T-T\_{1},T] is T1\displaystyle T\_{1}, there exists a constant C=C​(y,T1)\displaystyle C=C(y,T\_{1}) which depends only on y\displaystyle y and T1\displaystyle T\_{1} such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℚTγ​[|Yt|2]≤C​(y,T1),t∈[T−T1,T].\mathbb{E}^{\mathbb{Q}^{\gamma}\_{T}}\left[|Y\_{t}|^{2}\right]\leq C(y,T\_{1}),\quad t\in[T-T\_{1},T]. |  |

As a result, the proposition follows.
∎

###### Proposition 3.17.

For γ∈{q,α+1,1}\displaystyle\gamma\in\{q,\alpha+1,1\},

|  |  |  |
| --- | --- | --- |
|  | 𝔼ℚTγ​[|LT|]=O​(1),(T↗∞).\mathbb{E}^{\mathbb{Q}^{\gamma}\_{T}}[|L\_{T}|]=O(1),\quad(T\nearrow\infty). |  |

###### Proof.

Because D​r​(y)=r1+R2​y,D​θ​(y)=A,∇yYt=eB​t\displaystyle Dr(y)=r\_{1}+R\_{2}y,\;D\theta(y)=A,\;\nabla\_{y}Y\_{t}=e^{Bt}, ([17](https://arxiv.org/html/2512.00346v1#S3.E17 "In Proposition 3.11. ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | LT\displaystyle\displaystyle L\_{T} | =∫0T((r1+R2​Yt)⊤​eB​t)⊤​𝑑t+∫0T(A​eB​t)⊤​𝑑WtℚTγ\displaystyle\displaystyle=\int\_{0}^{T}((r\_{1}+R\_{2}Y\_{t})^{\top}e^{Bt})^{\top}dt+\int\_{0}^{T}(Ae^{Bt})^{\top}dW^{\mathbb{Q}^{\gamma}\_{T}}\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∫0T(A​eB​t)⊤​[{(γ−1)​A+Λ⊤​Cγ​(t;T)}​Yu+(γ−1)​a+Λ⊤​βγ​(t;T)]​𝑑t.\displaystyle\displaystyle\quad-\int\_{0}^{T}(Ae^{Bt})^{\top}\left[\left\{(\gamma-1)A+\Lambda^{\top}C^{\gamma}(t;T)\right\}Y\_{u}+(\gamma-1)a+\Lambda^{\top}\beta^{\gamma}(t;T)\right]dt. |  |

Because B\displaystyle B is stable, there exist M,ω>0\displaystyle M,\omega>0 such that

|  |  |  |
| --- | --- | --- |
|  | |eB​t|≤M​e−ω​t,(t≥0).|e^{Bt}|\leq Me^{-\omega t},\;(t\geq 0). |  |

Furthermore, Cγ,βγ\displaystyle C^{\gamma},\beta^{\gamma} are bounded as functions of (t,T)\displaystyle(t,T). Therefore, this proposition follows from Proposition [3.16](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem16 "Proposition 3.16. ‣ 3.3.2 Proofs of main results in Sect. 2.3 ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models").
∎

###### Proof of Theorem [2.7](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem7 "Theorem 2.7. ‣ 2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models").

The result follows from Propositions [3.11](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem11 "Proposition 3.11. ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") and [3.17](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem17 "Proposition 3.17. ‣ 3.3.2 Proofs of main results in Sect. 2.3 ‣ 3.3 Proofs for Sect. 2.3 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models").
∎

###### Proof of Theorem [2.8](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem8 "Theorem 2.8. ‣ 2.3 Turnpike theorem for excess hedging demands under quadratic term structure models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models").

We can prove the theorem in the same way as in the proof of Theorem [2.5](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem5 "Theorem 2.5. ‣ 2.2 Turnpike theorem for myopic portfolios under general stochastic factor models ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models").
∎

### 3.4 Proofs for Sect. [2.4](https://arxiv.org/html/2512.00346v1#S2.SS4 "2.4 Applications: optimal collective investment problems ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")

###### Lemma 3.18.

Let U1,U2\displaystyle U\_{1},U\_{2} be utility functions.

* (i)

  If there exist f,f~:(0,∞)→[0,∞)\displaystyle f,\tilde{f}:(0,\infty)\to[0,\infty) such that

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | U1′​(x+f​(x))≤U2′​(x)≤U1′​(x+f~​(x)),x>0U\_{1}^{\prime}(x+f(x))\leq U^{\prime}\_{2}(x)\leq U\_{1}^{\prime}(x+\tilde{f}(x)),\quad x>0 |  | (40) |

  holds, then

  |  |  |  |
  | --- | --- | --- |
  |  | |I1​(z)−I2​(z)|≤max⁡{f​(I2​(z)),f~​(I2​(z))},z>0|I\_{1}(z)-I\_{2}(z)|\leq\max\left\{f(I\_{2}(z)),\tilde{f}(I\_{2}(z))\right\},\quad z>0 |  |

  holds.
* (ii)

  In addition to the assumption in (i), if there exists g:(0,∞)→ℝ\displaystyle g:(0,\infty)\to\mathbb{R} such that

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | |A​R​T1​(x)−A​R​T2​(x)|≤g​(x),x>0\left|ART\_{1}(x)-ART\_{2}(x)\right|\leq g(x),\quad x>0 |  | (41) |

  holds and U2\displaystyle U\_{2} is the HARA utility, that is, A​R​T2​(x)=a​x+b​(x>0)\displaystyle ART\_{2}(x)=ax+b\;(x>0) for some constants a,b∈ℝ\displaystyle a,b\in\mathbb{R}, then

  |  |  |  |
  | --- | --- | --- |
  |  | |z​I1′​(z)−z​I2′​(z)|≤g​(I1​(z))+|a|​max⁡{f​(I2​(z)),f~​(I2​(z))},z>0|zI\_{1}^{\prime}(z)-zI\_{2}^{\prime}(z)|\leq g(I\_{1}(z))+|a|\max\left\{f(I\_{2}(z)),\tilde{f}(I\_{2}(z))\right\},\quad z>0 |  |

  holds.

###### Proof.

* (i)

  Substituting x=I2​(z),z>0\displaystyle x=I\_{2}(z),z>0 in ([40](https://arxiv.org/html/2512.00346v1#S3.E40 "In item (i) ‣ Lemma 3.18. ‣ 3.4 Proofs for Sect. 2.4 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")),

  |  |  |  |
  | --- | --- | --- |
  |  | U1′​(I2​(z)+f​(I2​(z)))≤z≤U1′​(I2​(z)+f~​(I2​(z)))U\_{1}^{\prime}(I\_{2}(z)+f(I\_{2}(z)))\leq z\leq U\_{1}^{\prime}(I\_{2}(z)+\tilde{f}(I\_{2}(z))) |  |

  holds. Because I1\displaystyle I\_{1} is decreasing, we get

  |  |  |  |
  | --- | --- | --- |
  |  | I2​(z)+f~​(I2​(z))≤I1​(z)≤I2​(z)+f​(I2​(z)),I\_{2}(z)+\tilde{f}(I\_{2}(z))\leq I\_{1}(z)\leq I\_{2}(z)+f(I\_{2}(z)), |  |

  which leads to

  |  |  |  |
  | --- | --- | --- |
  |  | |I1​(z)−I2​(z)|≤max⁡{f​(I2​(z)),f~​(I2​(z))}.|I\_{1}(z)-I\_{2}(z)|\leq\max\left\{f(I\_{2}(z)),\tilde{f}(I\_{2}(z))\right\}. |  |
* (ii)

  z​Ii′​(z)\displaystyle zI\_{i}^{\prime}(z) can be represented by the Arrow–Pratt measure of absolute risk tolerance A​R​Ti​(x)≔−Ui′​(x)Ui′′​(x)\displaystyle ART\_{i}(x)\coloneqq-\frac{U\_{i}^{\prime}(x)}{U\_{i}^{\prime\prime}(x)} as follows:

  |  |  |  |
  | --- | --- | --- |
  |  | z​Ii′​(z)=zUi′′​(Ii​(z))=Ui′​(Ii​(z))Ui′′​(Ii​(z))=−A​R​Ti​(Ii​(z)).\displaystyle\displaystyle zI\_{i}^{\prime}(z)=\frac{z}{U\_{i}^{\prime\prime}(I\_{i}(z))}=\frac{U\_{i}^{\prime}(I\_{i}(z))}{U\_{i}^{\prime\prime}(I\_{i}(z))}=-ART\_{i}(I\_{i}(z)). |  |

  Using ([41](https://arxiv.org/html/2512.00346v1#S3.E41 "In item (ii) ‣ Lemma 3.18. ‣ 3.4 Proofs for Sect. 2.4 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) and the assumption that U2\displaystyle U\_{2} is the HARA utility, we obtain

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | |z​I1′​(z)−z​I2′​(z)|\displaystyle\displaystyle|zI\_{1}^{\prime}(z)-zI\_{2}^{\prime}(z)| | =|A​R​T1​(I1​(z))−A​R​T2​(I2​(z))|\displaystyle\displaystyle=|ART\_{1}(I\_{1}(z))-ART\_{2}(I\_{2}(z))| |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | ≤|A​R​T1​(I1​(z))−A​R​T2​(I1​(z))|+|A​R​T2​(I1​(z))−A​R​T2​(I2​(z))|\displaystyle\displaystyle\leq|ART\_{1}(I\_{1}(z))-ART\_{2}(I\_{1}(z))|+|ART\_{2}(I\_{1}(z))-ART\_{2}(I\_{2}(z))| |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | ≤g​(I1​(z))+|a|​|I1​(z)−I2​(z)|\displaystyle\displaystyle\leq g(I\_{1}(z))+|a||I\_{1}(z)-I\_{2}(z)| |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  |  | ≤g​(I1​(z))+|a|​max⁡{f​(I2​(z)),f~​(I2​(z))},\displaystyle\displaystyle\leq g(I\_{1}(z))+|a|\max\left\{f(I\_{2}(z)),\tilde{f}(I\_{2}(z))\right\}, |  |

  which completes the proof.

∎

Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | U1​(x)\displaystyle\displaystyle U\_{1}(x) | ≔∑i=1nβi​(αi​x)pipi=∑i=1nwi​xpipi,\displaystyle\displaystyle\coloneqq\sum\_{i=1}^{n}\beta\_{i}\frac{(\alpha\_{i}x)^{p\_{i}}}{p\_{i}}=\sum\_{i=1}^{n}w\_{i}\frac{x^{p\_{i}}}{p\_{i}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | U2​(x)\displaystyle\displaystyle U\_{2}(x) | ≔wn​xpnpn,\displaystyle\displaystyle\coloneqq w\_{n}\frac{x^{p\_{n}}}{p\_{n}}, |  |

where wi≔βi​αipi>0\displaystyle w\_{i}\coloneqq\beta\_{i}\alpha\_{i}^{p\_{i}}>0.

###### Proof of Proposition [2.11](https://arxiv.org/html/2512.00346v1#S2.Thmtheorem11 "Proposition 2.11. ‣ 2.4.2 Linear sharing rule ‣ 2.4 Applications: optimal collective investment problems ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models").

First, we prove the inequality ([9](https://arxiv.org/html/2512.00346v1#S2.E9 "In Proposition 2.11. ‣ 2.4.2 Linear sharing rule ‣ 2.4 Applications: optimal collective investment problems ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")). Because U1′​(x)=∑i=1nwi​xpi−1,U2′​(x)=wn​xpn−1\displaystyle U\_{1}^{\prime}(x)=\sum\_{i=1}^{n}w\_{i}x^{p\_{i}-1},\;U\_{2}^{\prime}(x)=w\_{n}x^{p\_{n}-1},

|  |  |  |
| --- | --- | --- |
|  | U2′​(x)≤U1′​(x),x>0U\_{2}^{\prime}(x)\leq U\_{1}^{\prime}(x),\quad x>0 |  |

holds. To look for β∈ℝ\displaystyle\beta\in\mathbb{R} that satisfies

|  |  |  |
| --- | --- | --- |
|  | U1′​(x+xβ)≤U2′​(x)U\_{1}^{\prime}(x+x^{\beta})\leq U\_{2}^{\prime}(x) |  |

for large enough x>0\displaystyle x>0, we define h\displaystyle h by

|  |  |  |  |
| --- | --- | --- | --- |
|  | h​(x)\displaystyle\displaystyle h(x) | ≔U2′​(x)−U1′​(x+xβ)wn​(x+xβ)pn−1\displaystyle\displaystyle\coloneqq\frac{U\_{2}^{\prime}(x)-U\_{1}^{\prime}(x+x^{\beta})}{w\_{n}(x+x^{\beta})^{p\_{n}-1}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =(xx+xβ)pn−1−∑i=1n−1wiwn​(x+xβ)pi−pn−1\displaystyle\displaystyle=\left(\frac{x}{x+x^{\beta}}\right)^{p\_{n}-1}-\sum\_{i=1}^{n-1}\frac{w\_{i}}{w\_{n}}(x+x^{\beta})^{p\_{i}-p\_{n}}-1 |  |

for all x>0\displaystyle x>0. Then h′\displaystyle h^{\prime}, a derivative of h\displaystyle h, is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | h′​(x)\displaystyle\displaystyle h^{\prime}(x) | =(pn−1)​(1−β)​xpn−2+β(x+xβ)pn−∑i=1n−1wiwn​(pi−pn)​(x+xβ)pi−1(x+xβ)pn​(1+β​xβ−1)\displaystyle\displaystyle=\frac{(p\_{n}-1)(1-\beta)x^{p\_{n}-2+\beta}}{(x+x^{\beta})^{p\_{n}}}-\sum\_{i=1}^{n-1}\frac{w\_{i}}{w\_{n}}(p\_{i}-p\_{n})\frac{(x+x^{\beta})^{p\_{i}-1}}{(x+x^{\beta})^{p\_{n}}}(1+\beta x^{\beta-1}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−(pn−pn−1)​xpn+β−2(x+xβ)pn​{1−pnpn−pn−1​(1−β)−∑i=1n−1wiwn⋅pn−pipn−pn−1⋅(1+xβ−1)pi−1​(β​xpi−pn+x1+pi−pn−β)}.\displaystyle\displaystyle=-\frac{(p\_{n}-p\_{n-1})x^{p\_{n}+\beta-2}}{(x+x^{\beta})^{p\_{n}}}\left\{\frac{1-p\_{n}}{p\_{n}-p\_{n-1}}(1-\beta)-\sum\_{i=1}^{n-1}\frac{w\_{i}}{w\_{n}}\cdot\frac{p\_{n}-p\_{i}}{p\_{n}-p\_{n-1}}\cdot(1+x^{\beta-1})^{p\_{i}-1}\left(\beta x^{p\_{i}-p\_{n}}+x^{1+p\_{i}-p\_{n}-\beta}\right)\right\}. |  |

If β∈(1+pn−1−pn,1)\displaystyle\beta\in(1+p\_{n-1}-p\_{n},1), then

|  |  |  |
| --- | --- | --- |
|  | 1+pi−pn−β<1+pn−1−pn−β<0,(i=1,…,n−1),1+p\_{i}-p\_{n}-\beta<1+p\_{n-1}-p\_{n}-\beta<0,\quad(i=1,\dots,n-1), |  |

which means that

|  |  |  |
| --- | --- | --- |
|  | ∑i=1n−1wiwn⋅pn−pipn−pn−1⋅(1+xβ−1)pi−1​(β​xpi−pn+x1+pi−pn−β)→∑i=1n−1wiwn⋅pn−pipn−pn−1⋅(1+0)pi−1​(β⋅0+0)=0\sum\_{i=1}^{n-1}\frac{w\_{i}}{w\_{n}}\cdot\frac{p\_{n}-p\_{i}}{p\_{n}-p\_{n-1}}\cdot(1+x^{\beta-1})^{p\_{i}-1}\left(\beta x^{p\_{i}-p\_{n}}+x^{1+p\_{i}-p\_{n}-\beta}\right)\rightarrow\sum\_{i=1}^{n-1}\frac{w\_{i}}{w\_{n}}\cdot\frac{p\_{n}-p\_{i}}{p\_{n}-p\_{n-1}}\cdot(1+0)^{p\_{i}-1}\left(\beta\cdot 0+0\right)=0 |  |

as x↗∞\displaystyle x\nearrow\infty.
Therefore, h′​(x)<0\displaystyle h^{\prime}(x)<0 holds for large enough x>0\displaystyle x>0. Combining this with the fact that

|  |  |  |  |
| --- | --- | --- | --- |
|  | h​(x)\displaystyle\displaystyle h(x) | =(11+xβ−1)pn−1−∑i=1n−1wiwn​xpi−pn​(1+xβ−1)pi−pn−1\displaystyle\displaystyle=\left(\frac{1}{1+x^{\beta-1}}\right)^{p\_{n}-1}-\sum\_{i=1}^{n-1}\frac{w\_{i}}{w\_{n}}x^{p\_{i}-p\_{n}}(1+x^{\beta-1})^{p\_{i}-p\_{n}}-1 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | →1−∑i=1n−1wiwn⋅0⋅(1+0)pi−pn−1(x↗∞)\displaystyle\displaystyle\rightarrow 1-\sum\_{i=1}^{n-1}\frac{w\_{i}}{w\_{n}}\cdot 0\cdot(1+0)^{p\_{i}-p\_{n}}-1\quad(x\nearrow\infty) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =0\displaystyle\displaystyle=0 |  |

leads to h​(x)>0\displaystyle h(x)>0 for large enough x>0\displaystyle x>0. Using Lemma [3.18](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem18 "Lemma 3.18. ‣ 3.4 Proofs for Sect. 2.4 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")(i) with f​(x)=xβ,f~​(x)=0,\displaystyle f(x)=x^{\beta},\tilde{f}(x)=0, and β∈(1+pn−1−pn,1)\displaystyle\beta\in(1+p\_{n-1}-p\_{n},1) leads to

|  |  |  |
| --- | --- | --- |
|  | |I1​(z)−I2​(z)|≤(zwn)β​(qn−1)|I\_{1}(z)-I\_{2}(z)|\leq\left(\frac{z}{w\_{n}}\right)^{\beta(q\_{n}-1)} |  |

for small enough z>0\displaystyle z>0, which means that the inequality ([9](https://arxiv.org/html/2512.00346v1#S2.E9 "In Proposition 2.11. ‣ 2.4.2 Linear sharing rule ‣ 2.4 Applications: optimal collective investment problems ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) holds for any nonnegative β∈(1+pn−1−pn,1)\displaystyle\beta\in(1+p\_{n-1}-p\_{n},1) and a constant K>0\displaystyle K>0.
Next, we prove the inequality ([10](https://arxiv.org/html/2512.00346v1#S2.E10 "In Proposition 2.11. ‣ 2.4.2 Linear sharing rule ‣ 2.4 Applications: optimal collective investment problems ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")). Because

|  |  |  |  |
| --- | --- | --- | --- |
|  | |A​R​T1​(x)−A​R​T2​(x)|\displaystyle\displaystyle\left|ART\_{1}(x)-ART\_{2}(x)\right| | =|∑i=1nwi​xpi−1∑i=1nwi​(1−pi)​xpi−2−x1−pn|\displaystyle\displaystyle=\left|\frac{\sum\_{i=1}^{n}w\_{i}x^{p\_{i}-1}}{\sum\_{i=1}^{n}w\_{i}(1-p\_{i})x^{p\_{i}-2}}-\frac{x}{1-p\_{n}}\right| |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑i=1n−1(pn−pi)​wi​xpi−1(1−pn)​(∑i=1nwi​(1−pi)​xpi−2)\displaystyle\displaystyle=\frac{\sum\_{i=1}^{n-1}(p\_{n}-p\_{i})w\_{i}x^{p\_{i}-1}}{(1-p\_{n})\left(\sum\_{i=1}^{n}w\_{i}(1-p\_{i})x^{p\_{i}-2}\right)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤∑i=1n−1(pn−pi)​wi​xpi−1(1−pn)2​wn​xpn−2\displaystyle\displaystyle\leq\frac{\sum\_{i=1}^{n-1}(p\_{n}-p\_{i})w\_{i}x^{p\_{i}-1}}{(1-p\_{n})^{2}w\_{n}x^{p\_{n}-2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑i=1n−1pn−pi(1−pn)2⋅wiwn⋅xpi−pn+1\displaystyle\displaystyle=\sum\_{i=1}^{n-1}\frac{p\_{n}-p\_{i}}{(1-p\_{n})^{2}}\cdot\frac{w\_{i}}{w\_{n}}\cdot x^{p\_{i}-p\_{n}+1} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C​xpn−1−pn+1\displaystyle\displaystyle\leq Cx^{p\_{n-1}-p\_{n}+1} |  |

holds for large enough x>0\displaystyle x>0 and a constant C>0\displaystyle C>0, Lemma [3.18](https://arxiv.org/html/2512.00346v1#S3.Thmtheorem18 "Lemma 3.18. ‣ 3.4 Proofs for Sect. 2.4 ‣ 3 Proofs for main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")(ii) implies that for small enough z>0\displaystyle z>0,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |z​I1′​(z)−z​I2′​(z)|\displaystyle\displaystyle|zI\_{1}^{\prime}(z)-zI\_{2}^{\prime}(z)| | ≤C​I1​(z)pn−1−pn+1+11−pn​(zwn)β​(qn−1)\displaystyle\displaystyle\leq CI\_{1}(z)^{p\_{n-1}-p\_{n}+1}+\frac{1}{1-p\_{n}}\left(\frac{z}{w\_{n}}\right)^{\beta(q\_{n}-1)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C​((zwn)qn−1+(zwn)β​(qn−1))(pn−1−pn+1)++11−pn​(zwn)β​(qn−1)\displaystyle\displaystyle\leq C\left(\left(\frac{z}{w\_{n}}\right)^{q\_{n}-1}+\left(\frac{z}{w\_{n}}\right)^{\beta(q\_{n}-1)}\right)^{(p\_{n-1}-p\_{n}+1)^{+}}+\frac{1}{1-p\_{n}}\left(\frac{z}{w\_{n}}\right)^{\beta(q\_{n}-1)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤C~​(z(qn−1)​(pn−1−pn+1)++zβ​(qn−1)​(pn−1−pn+1)++zβ​(qn−1))\displaystyle\displaystyle\leq\tilde{C}\left(z^{(q\_{n}-1)(p\_{n-1}-p\_{n}+1)^{+}}+z^{\beta(q\_{n}-1)(p\_{n-1}-p\_{n}+1)^{+}}+z^{\beta(q\_{n}-1)}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤3​C~​zβ​(qn−1),\displaystyle\displaystyle\leq 3\tilde{C}z^{\beta(q\_{n}-1)}, |  |

where C~\displaystyle\tilde{C} is a constant, and the last inequality follows from

|  |  |  |
| --- | --- | --- |
|  | β​(qn−1)≤(qn−1)​(pn−1−pn+1)+≤β​(qn−1)​(pn−1−pn+1)+≤0.\beta(q\_{n}-1)\leq(q\_{n}-1)(p\_{n-1}-p\_{n}+1)^{+}\leq\beta(q\_{n}-1)(p\_{n-1}-p\_{n}+1)^{+}\leq 0. |  |

We have completed the proof.
∎

## Appendix A Appendix: Malliavin calculus

We recall some results on Malliavin calculus which allow us to derive an explicit stochastic flow representation for the optimal portfolio process π^\displaystyle\hat{\pi}. For details, see [[34](https://arxiv.org/html/2512.00346v1#bib.bib34), [36](https://arxiv.org/html/2512.00346v1#bib.bib36), [37](https://arxiv.org/html/2512.00346v1#bib.bib37), [43](https://arxiv.org/html/2512.00346v1#bib.bib43)].

Consider a complete probability space (Ω,ℱ,P)\displaystyle(\Omega,\mathcal{F},P) and a standard n\displaystyle n-dimensional Brownian motion W=(W1,…,Wn)⊤\displaystyle W=(W^{1},\dots,W^{n})^{\top} defined on (Ω,ℱ,P)\displaystyle(\Omega,\mathcal{F},P). We denote by (ℱt)t≥0\displaystyle(\mathcal{F}\_{t})\_{t\geq 0} the P\displaystyle P-augmentation of the natural filtration generated by W=(Wt)t≥0\displaystyle W=(W\_{t})\_{t\geq 0}.

We introduce the Malliavin derivative operator as in [[36](https://arxiv.org/html/2512.00346v1#bib.bib36)]. Fix T>0\displaystyle T>0.
Let Cb∞​(ℝm)\displaystyle C\_{b}^{\infty}(\mathbb{R}^{m}) be the space of infinitely differentiable functions on ℝm\displaystyle\mathbb{R}^{m} which, together with all partial derivatives, are bounded. By 𝒮\displaystyle\mathscr{S} we denote the class of smooth random variables, namely, random variables of the form

|  |  |  |
| --- | --- | --- |
|  | F=f​(Wt1,…,Wtm),F=f(W\_{t\_{1}},\dots,W\_{t\_{m}}), |  |

where (t1,…,tm)∈[0,T]m\displaystyle(t\_{1},\dots,t\_{m})\in[0,T]^{m} and the function f=f​(x11,…,xn​1,…,x1​m,…,xn​m)\displaystyle f=f(x^{11},\dots,x^{n1},\dots,x^{1m},\dots,x^{nm}) belongs to Cb∞​(ℝn​m)\displaystyle C\_{b}^{\infty}(\mathbb{R}^{nm}).
For each F∈𝒮\displaystyle F\in\mathscr{S}, the Malliavin derivative of F\displaystyle F is the L2​([0,T];ℝ)n\displaystyle L^{2}([0,T];\mathbb{R})^{n}-valued random variable D​F=(D1​F,…​Dn​F)\displaystyle DF=(D^{1}F,\dots D^{n}F) with components

|  |  |  |
| --- | --- | --- |
|  | Di​F​(⋅)≔∑j=1m∂f∂xi​j​(Wt1,…,Wtm)​1[0,tj]​(⋅),(i=1,…,n).D^{i}F(\cdot)\coloneqq\sum\_{j=1}^{m}\frac{\partial f}{\partial x^{ij}}(W\_{t\_{1}},\dots,W\_{t\_{m}})1\_{[0,t\_{j}]}(\cdot),\quad(i=1,\dots,n). |  |

Fix p∈[1,∞)\displaystyle p\in[1,\infty). Because we can view the operator D\displaystyle D as an operator from Lp​(Ω;ℝ)\displaystyle L^{p}(\Omega;\mathbb{R}) to Lp​(Ω;(L2​[0,T];ℝ)n)\displaystyle L^{p}\left(\Omega;(L^{2}[0,T];\mathbb{R})^{n}\right) and D\displaystyle D is closable, we denote the closure of D\displaystyle D again by D\displaystyle D and the domain of D\displaystyle D in Lp​(Ω;ℝ)\displaystyle L^{p}(\Omega;\mathbb{R}) by 𝔻p,1\displaystyle\mathbb{D}\_{p,1}. Thus, 𝔻p,1\displaystyle\mathbb{D}\_{p,1} is the closure of 𝒮\displaystyle\mathscr{S} with respect to the norm

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖F‖p,1\displaystyle\displaystyle||F||\_{p,1} | ≔‖F‖Lp​(Ω;ℝ)+‖D​F‖Lp​(Ω;(L2​[0,T];ℝ)n)\displaystyle\displaystyle\coloneqq||F||\_{L^{p}(\Omega;\mathbb{R})}+||DF||\_{L^{p}\left(\Omega;(L^{2}[0,T];\mathbb{R})^{n}\right)} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼​[|F|p]1p+𝔼​[(∫0T|D​F​(t)|2​𝑑t)p2]1p.\displaystyle\displaystyle=\mathbb{E}[|F|^{p}]^{\frac{1}{p}}+\mathbb{E}\left[\left(\int\_{0}^{T}|DF(t)|^{2}dt\right)^{\frac{p}{2}}\right]^{\frac{1}{p}}. |  |

Here, |⋅|\displaystyle|\cdot| denotes the Euclidean norm on ℝn\displaystyle\mathbb{R}^{n}.
𝔻p,1\displaystyle\mathbb{D}\_{p,1} is a Banach space with respect to the norm ||⋅||p,1\displaystyle||\cdot||\_{p,1}.
Given F∈𝔻p,1\displaystyle F\in\mathbb{D}\_{p,1}, D​F\displaystyle DF is an (L2​[0,T])n\displaystyle(L^{2}[0,T])^{n}-valued random variable. To each D​F\displaystyle DF, we can find a measurable process [0,T]×Ω∋(t,ω)↦Dt​F​(ω)∈ℝn\displaystyle[0,T]\times\Omega\ni(t,\omega)\mapsto D\_{t}F(\omega)\in\mathbb{R}^{n} such that for almost all ω∈Ω\displaystyle\omega\in\Omega, Dt​F​(ω)=D​F​(ω)​(t)\displaystyle D\_{t}F(\omega)=DF(\omega)(t) holds for almost everywhere t∈[0,T]\displaystyle t\in[0,T]. Therefore, we identify (L2​[0,T])n\displaystyle(L^{2}[0,T])^{n}-valued random variable D​F\displaystyle DF with ℝn\displaystyle\mathbb{R}^{n}-valued measurable process (t,ω)↦Dt​F​(ω)\displaystyle(t,\omega)\mapsto D\_{t}F(\omega) without further comment.

###### Remark A.1.

Note that for real-valued random variable F∈𝔻p,1\displaystyle F\in\mathbb{D}\_{p,1}, we define D​F=(D1​F,…,Dn​F)\displaystyle DF=(D^{1}F,\dots,D^{n}F) as a row vector; that is, D​F\displaystyle DF is an ℝ1×n\displaystyle\mathbb{R}^{1\times n}-valued stochastic process. For ℝm\displaystyle\mathbb{R}^{m}-valued random variable F=(F1,…,Fm)⊤∈𝔻p,1m\displaystyle F=(F\_{1},\dots,F\_{m})^{\top}\in\mathbb{D}\_{p,1}^{m} we define D​F=(Dj​Fi)1≤i≤m1≤j≤n\displaystyle DF=(D^{j}F\_{i})\_{\begin{subarray}{c}1\leq i\leq m\\
1\leq j\leq n\end{subarray}}, which is an ℝm×n\displaystyle\mathbb{R}^{m\times n}-valued stochastic process.

We collect well-known results on Malliavin calculus, that is, Clark’s formula (Proposition [A.1](https://arxiv.org/html/2512.00346v1#A1.Thmtheorem1 "Proposition A.1. ‣ Appendix A Appendix: Malliavin calculus ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")), chain rule (Proposition [A.2](https://arxiv.org/html/2512.00346v1#A1.Thmtheorem2 "Proposition A.2. ‣ Appendix A Appendix: Malliavin calculus ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")), and Malliavin derivatives of Lebesgue integrals, stochastic integrals, and solutions to SDEs (Propositions [A.3](https://arxiv.org/html/2512.00346v1#A1.Thmtheorem3 "Proposition A.3. ‣ Appendix A Appendix: Malliavin calculus ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")–[A.5](https://arxiv.org/html/2512.00346v1#A1.Thmtheorem5 "Proposition A.5. ‣ Appendix A Appendix: Malliavin calculus ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")).
Firstly, we quote Clark’s formula for random variables in 𝔻1,1\displaystyle\mathbb{D}\_{1,1}, which comes from [[23](https://arxiv.org/html/2512.00346v1#bib.bib23)].

###### Proposition A.1.

For every F∈𝔻1,1\displaystyle F\in\mathbb{D}\_{1,1} we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[F|ℱt]=𝔼​[F]+∫0t𝔼​[Ds​F|ℱs]​𝑑Ws,t∈[0,T].\mathbb{E}[F|\mathcal{F}\_{t}]=\mathbb{E}[F]+\int\_{0}^{t}\mathbb{E}\left[D\_{s}F|\mathcal{F}\_{s}\right]dW\_{s},\quad t\in[0,T]. |  |

The following proposition is a straightforward multidimensional version of Lemma A.1 in [[36](https://arxiv.org/html/2512.00346v1#bib.bib36)].

###### Proposition A.2.

Let F=(F1,…​Fm)⊤∈𝔻1,1m\displaystyle F=(F\_{1},\dots F\_{m})^{\top}\in\mathbb{D}\_{1,1}^{m}. Let ϕ=(ϕ1,…,ϕk)⊤∈C1​(ℝm;ℝk)\displaystyle\phi=(\phi^{1},\dots,\phi^{k})^{\top}\in C^{1}(\mathbb{R}^{m};\mathbb{R}^{k}). Assume that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[|ϕl​(F)|]+𝔼​[(∫0T|∑i=1m∂ϕl∂xi​(F)​Dt​Fi|2​𝑑t)12]<∞\mathbb{E}[|\phi^{l}(F)|]+\mathbb{E}\left[\left(\int\_{0}^{T}\left|\sum\_{i=1}^{m}\frac{\partial\phi^{l}}{\partial x\_{i}}(F)D\_{t}F\_{i}\right|^{2}dt\right)^{\frac{1}{2}}\right]<\infty |  | (42) |

for all l=1,…​k\displaystyle l=1,\dots k. Then ϕ​(F)∈𝔻1,1k\displaystyle\phi(F)\in\mathbb{D}\_{1,1}^{k} and

|  |  |  |
| --- | --- | --- |
|  | D​(ϕ​(F))=D​ϕ​(F)​D​F,D(\phi(F))=D\phi(F)DF, |  |

where D​ϕ=(∂ϕi∂xj)1≤i≤k1≤j≤m:ℝm→ℝk×m\displaystyle D\phi=\left(\frac{\partial\phi^{i}}{\partial x\_{j}}\right)\_{\begin{subarray}{c}1\leq i\leq k\\
1\leq j\leq m\end{subarray}}:\mathbb{R}^{m}\to\mathbb{R}^{k\times m} is the Jacobi matrix of ϕ\displaystyle\phi.

###### Remark A.2.

Hölder’s inequality implies that the condition ([42](https://arxiv.org/html/2512.00346v1#A1.E42 "In Proposition A.2. ‣ Appendix A Appendix: Malliavin calculus ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) holds if F∈𝔻p,1m,ϕl​(F)∈L1,∂ϕl∂xi​(F)∈Lq,l=1,…​k,i=1,…​m\displaystyle F\in\mathbb{D}\_{p,1}^{m},\;\phi^{l}(F)\in L^{1},\;\frac{\partial\phi^{l}}{\partial x\_{i}}(F)\in L^{q},\;l=1,\dots k,\;i=1,\dots m for some p∈[1,∞),q∈(1,∞]\displaystyle p\in[1,\infty),\;q\in(1,\infty] such that 1p+1q=1\displaystyle\frac{1}{p}+\frac{1}{q}=1. In particular, the condition ([42](https://arxiv.org/html/2512.00346v1#A1.E42 "In Proposition A.2. ‣ Appendix A Appendix: Malliavin calculus ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) holds if F∈⋂p≥1𝔻p,1m\displaystyle F\in\bigcap\_{p\geq 1}\mathbb{D}\_{p,1}^{m} and ϕ,D​ϕ\displaystyle\phi,D\phi are of polynomial growth.

Proposition [A.3](https://arxiv.org/html/2512.00346v1#A1.Thmtheorem3 "Proposition A.3. ‣ Appendix A Appendix: Malliavin calculus ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") is Lemma 5.1 in [[24](https://arxiv.org/html/2512.00346v1#bib.bib24)], Proposition [A.4](https://arxiv.org/html/2512.00346v1#A1.Thmtheorem4 "Proposition A.4. ‣ Appendix A Appendix: Malliavin calculus ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") is Proposition 2.3 in [[36](https://arxiv.org/html/2512.00346v1#bib.bib36)], and Proposition [A.5](https://arxiv.org/html/2512.00346v1#A1.Thmtheorem5 "Proposition A.5. ‣ Appendix A Appendix: Malliavin calculus ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models") is Proposition 8.2 in [[43](https://arxiv.org/html/2512.00346v1#bib.bib43)].

###### Proposition A.3.

Let u=(us)s∈[0,T]\displaystyle u=(u\_{s})\_{s\in[0,T]} be a real-valued, continuous, progressively measurable process such that

1. (i)

   us∈𝔻1,1\displaystyle u\_{s}\in\mathbb{D}\_{1,1} for every s∈[0,T]\displaystyle s\in[0,T],
2. (ii)

   sups∈[0,T]𝔼​[|us|q]<∞\displaystyle\sup\_{s\in[0,T]}\mathbb{E}\left[|u\_{s}|^{q}\right]<\infty for some q>1\displaystyle q>1, and sups∈[0,T]𝔼​[∫0T|Dtj​us|4​𝑑t]<∞\displaystyle\sup\_{s\in[0,T]}\mathbb{E}\left[\int\_{0}^{T}|D^{j}\_{t}u\_{s}|^{4}dt\right]<\infty for j=1,…,n\displaystyle j=1,\dots,n,
3. (iii)

   s↦Dt​u​(s,ω)\displaystyle s\mapsto D\_{t}u(s,\omega) is left (or right) continuous for almost every (t,ω)∈[0,T]×Ω\displaystyle(t,\omega)\in[0,T]\times\Omega.

Then ∫0Tus​𝑑s∈𝔻1,1\displaystyle\int\_{0}^{T}u\_{s}ds\in\mathbb{D}\_{1,1} and Dt​∫0Tus​𝑑s=∫tTDt​us​𝑑s\displaystyle D\_{t}\int\_{0}^{T}u\_{s}ds=\int\_{t}^{T}D\_{t}u\_{s}ds.

###### Proposition A.4.

Let u=(u1,…,un)⊤\displaystyle u=(u^{1},\dots,u^{n})^{\top} be an ℝn\displaystyle\mathbb{R}^{n}-valued progressively measurable process such that

* (i)

  us∈𝔻1,1n\displaystyle u\_{s}\in\mathbb{D}\_{1,1}^{n} for every s∈[0,T]\displaystyle s\in[0,T],
* (ii)

  [0,T]×Ω∋(x,ω)↦D​u​(s,ω)∈(L2​[0,T])n2\displaystyle[0,T]\times\Omega\ni(x,\omega)\mapsto Du(s,\omega)\in(L^{2}[0,T])^{n^{2}} admits a progressively measurable version,
* (iii)

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | ‖|u|‖1,1\displaystyle\displaystyle|||u|||\_{1,1} | ≔𝔼​[(∫0T|us|2​𝑑s)12]+𝔼​[{∫0T∫0T|Dt​us|2​𝑑t​𝑑s}12]<∞,\displaystyle\displaystyle\coloneqq\mathbb{E}\left[\left(\int\_{0}^{T}|u\_{s}|^{2}ds\right)^{\frac{1}{2}}\right]+\mathbb{E}\left[\left\{\int\_{0}^{T}\int\_{0}^{T}\left|D\_{t}u\_{s}\right|^{2}dtds\right\}^{\frac{1}{2}}\right]<\infty, |  |

  where |⋅|\displaystyle|\cdot| denotes Euclidean norm on ℝn×n\displaystyle\mathbb{R}^{n\times n}.

Then ∫0Tus⊤​𝑑Ws∈𝔻1,1\displaystyle\int\_{0}^{T}u^{\top}\_{s}dW\_{s}\in\mathbb{D}\_{1,1} and

|  |  |  |
| --- | --- | --- |
|  | Dt​∫0Tus⊤​𝑑Ws=ut⊤+(∫0T(Dt​us)⊤​𝑑Ws)⊤.D\_{t}\int\_{0}^{T}u^{\top}\_{s}dW\_{s}=u\_{t}^{\top}+\left(\int\_{0}^{T}(D\_{t}u\_{s})^{\top}dW\_{s}\right)^{\top}. |  |

###### Proposition A.5.

For d∈ℕ\displaystyle d\in\mathbb{N}, we consider the d\displaystyle d-dimensional SDE

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=μ​(Xt)​d​t+σ​(Xt)​d​Wt,X0=x∈ℝd,dX\_{t}=\mu(X\_{t})dt+\sigma(X\_{t})dW\_{t},\quad X\_{0}=x\in\mathbb{R}^{d}, |  | (43) |

where μ=(μ1,…​μd)⊤:ℝd→ℝd,σ=(σi,j)1≤i≤d1≤j≤n:ℝd→ℝd×n\displaystyle\mu=(\mu\_{1},\dots\mu\_{d})^{\top}:\mathbb{R}^{d}\to\mathbb{R}^{d},\;\sigma=(\sigma\_{i,j})\_{\begin{subarray}{c}1\leq i\leq d\\
1\leq j\leq n\end{subarray}}:\mathbb{R}^{d}\to\mathbb{R}^{d\times n} are continuously differentiable and satisfy

|  |  |  |
| --- | --- | --- |
|  | supx∈ℝd(|∂μi∂xk​(x)|+|∂σi,j∂xk​(x)|)<∞\sup\_{x\in\mathbb{R}^{d}}\left(\left|\frac{\partial\mu\_{i}}{\partial x\_{k}}(x)\right|+\left|\frac{\partial\sigma\_{i,j}}{\partial x\_{k}}(x)\right|\right)<\infty |  |

for i,k=1,…,d,j=1,…,n.\displaystyle i,k=1,\dots,d,\;j=1,\dots,n.
Then ([43](https://arxiv.org/html/2512.00346v1#A1.E43 "In Proposition A.5. ‣ Appendix A Appendix: Malliavin calculus ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) has a unique strong solution X=(X1,…,Xd)⊤\displaystyle X=(X^{1},\dots,X^{d})^{\top} which satisfies the following:

* (i)

  Xsk∈⋂p≥1𝔻p,1,k=1,…​d,s∈[0,T]\displaystyle X^{k}\_{s}\in\bigcap\_{p\geq 1}\mathbb{D}\_{p,1},\quad k=1,\dots d,\;s\in[0,T];
* (ii)

  Dt​Xs\displaystyle D\_{t}X\_{s} satisfies

  |  |  |  |
  | --- | --- | --- |
  |  | Dt​Xs=σ​(Xt)+∫tsD​μ​(Xu)​Dt​Xu​𝑑u+∑j=1n∫tsD​σ⋅j​(Xu)​Dt​Xu​𝑑WujD\_{t}X\_{s}=\sigma(X\_{t})+\int\_{t}^{s}D\mu(X\_{u})D\_{t}X\_{u}du+\sum\_{j=1}^{n}\int\_{t}^{s}D\sigma\_{\cdot j}(X\_{u})D\_{t}X\_{u}dW^{j}\_{u} |  |

  for t∈[0,s]\displaystyle t\in[0,s] and Dt​Xs=0\displaystyle D\_{t}X\_{s}=0 for t∈(s,T]\displaystyle t\in(s,T], where D​μ=(∂μi∂xj)1≤i≤d1≤j≤d,D​σ⋅j=(σi,j∂xl)1≤i≤d1≤l≤d\displaystyle D\mu=\left(\frac{\partial\mu\_{i}}{\partial x\_{j}}\right)\_{\begin{subarray}{c}1\leq i\leq d\\
  1\leq j\leq d\end{subarray}},\;D\sigma\_{\cdot j}=\left(\frac{\sigma\_{i,j}}{\partial x\_{l}}\right)\_{\begin{subarray}{c}1\leq i\leq d\\
  1\leq l\leq d\end{subarray}};
* (iii)

  for j=1,…,n,p∈[1,∞),\displaystyle j=1,\dots,n,\;p\in[1,\infty),

  |  |  |  |
  | --- | --- | --- |
  |  | supr∈[0,T]𝔼​[sups∈[0,T]|Drj​Xsk|p]<∞;\sup\_{r\in[0,T]}\mathbb{E}\left[\sup\_{s\in[0,T]}\left|D^{j}\_{r}X^{k}\_{s}\right|^{p}\right]<\infty; |  |
* (iv)

  Dt​Xs=∇xXs​(∇xXt)−1​σ​(Xt)\displaystyle D\_{t}X\_{s}=\nabla\_{x}X\_{s}(\nabla\_{x}X\_{t})^{-1}\sigma(X\_{t}) for t∈[0,s]\displaystyle t\in[0,s], where ∇xX\displaystyle\nabla\_{x}X is an ℝd×d\displaystyle\mathbb{R}^{d\times d}-valued stochastic process satisfying

  |  |  |  |
  | --- | --- | --- |
  |  | ∇xXs=I+∫0sD​μ​(Xu)​∇xXu​d​u+∑j=1n∫tsD​σ⋅j​(Xu)​∇xXu​d​Wuj\nabla\_{x}X\_{s}=I+\int\_{0}^{s}D\mu(X\_{u})\nabla\_{x}X\_{u}du+\sum\_{j=1}^{n}\int\_{t}^{s}D\sigma\_{\cdot j}(X\_{u})\nabla\_{x}X\_{u}dW^{j}\_{u} |  |

  for s∈[0,T]\displaystyle s\in[0,T] and I∈ℝd×d\displaystyle I\in\mathbb{R}^{d\times d} is the identity matrix.

## Appendix B Appendix: Option pricing theory with stochastic factor models in complete markets

In this appendix, we recall well-known results on pricing and hedging problems in a complete market with a stochastic factor process ([2](https://arxiv.org/html/2512.00346v1#S2.E2 "In 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")).
Under the equivalent martingale measure ℚ\displaystyle\mathbb{Q}, the dynamics of risky assets S\displaystyle S and the stochastic factor process Y\displaystyle Y are denoted by

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | d​St\displaystyle\displaystyle dS\_{t} | =diag(St)⁡(𝟏​r​(Yt)​d​t+σ​(Yt)​d​Wtℚ),\displaystyle\displaystyle=\operatorname\*{diag}(S\_{t})\left(\mathbf{1}r(Y\_{t})dt+\sigma(Y\_{t})dW^{\mathbb{Q}}\_{t}\right), | S0\displaystyle\displaystyle S\_{0} | =s0∈ℝ++n,\displaystyle\displaystyle=s\_{0}\in\mathbb{R}^{n}\_{++}, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | d​Yt\displaystyle\displaystyle dY\_{t} | =b~​(Yt)​d​t+a​(Yt)​d​Wtℚ,\displaystyle\displaystyle=\tilde{b}(Y\_{t})dt+a(Y\_{t})dW^{\mathbb{Q}}\_{t}, | Y0\displaystyle\displaystyle Y\_{0} | =y∈ℝm,\displaystyle\displaystyle=y\in\mathbb{R}^{m}, |  |

where b~​(y)≔b​(y)−a​(y)​θ​(y)\displaystyle\tilde{b}(y)\coloneqq b(y)-a(y)\theta(y).
Let ℒ\displaystyle\mathcal{L} be a generator of (S,Y)\displaystyle(S,Y) under ℚ\displaystyle\mathbb{Q}; that is, for f:[0,T]×ℝ++n×ℝm→ℝ\displaystyle f:[0,T]\times\mathbb{R}^{n}\_{++}\times\mathbb{R}^{m}\to\mathbb{R}, ℒ​f:[0,T]×ℝ++n×ℝm→ℝ\displaystyle\mathcal{L}f:[0,T]\times\mathbb{R}^{n}\_{++}\times\mathbb{R}^{m}\to\mathbb{R} is defined by

|  |  |  |
| --- | --- | --- |
|  | ℒ​f≔Ds​f⊤​r​(y)​s+Dy​f⊤​b~​(y)+12​Tr​[{Σ​Σ⊤}​(s,y)​D2​f],(t,s,y)∈[0,T]×ℝ++n×ℝm,\mathcal{L}f\coloneqq D\_{s}f^{\top}r(y)s+D\_{y}f^{\top}\tilde{b}(y)+\frac{1}{2}\mathrm{Tr}\left[\left\{\Sigma\Sigma^{\top}\right\}(s,y)D^{2}f\right],\quad(t,s,y)\in[0,T]\times\mathbb{R}^{n}\_{++}\times\mathbb{R}^{m}, |  |

where Σ​(s,y)≔(diag(s)⁡σ​(y)a​(y))∈ℝ(n+m)×n\displaystyle\Sigma(s,y)\coloneqq\begin{pmatrix}\operatorname\*{diag}(s)\sigma(y)\\
a(y)\end{pmatrix}\in\mathbb{R}^{(n+m)\times n}.

###### Theorem B.1.

Let Φ:ℝ++n→ℝ\displaystyle\Phi:\mathbb{R}^{n}\_{++}\to\mathbb{R} and u:[0,T]×ℝ++n×ℝm→ℝ\displaystyle u:[0,T]\times\mathbb{R}^{n}\_{++}\times\mathbb{R}^{m}\to\mathbb{R} be a solution of the Cauchy problem

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂tu+ℒ​u−r​(y)​u\displaystyle\displaystyle\partial\_{t}u+\mathcal{L}u-r(y)u | =0,\displaystyle\displaystyle=0, | o​n[0,T)×ℝ++n×ℝm,\displaystyle\displaystyle on\quad\left[0,T\right)\times\mathbb{R}^{n}\_{++}\times\mathbb{R}^{m}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | u​(T,s,y)\displaystyle\displaystyle u(T,s,y) | =Φ​(s),\displaystyle\displaystyle=\Phi(s), | o​nℝ++n×ℝm.\displaystyle\displaystyle on\quad\mathbb{R}^{n}\_{++}\times\mathbb{R}^{m}. |  |

1. (i)

   Let x≔u​(0,s0,y)\displaystyle x\coloneqq u(0,s\_{0},y) and π=(πt)t∈[0,T]\displaystyle\pi=(\pi\_{t})\_{t\in[0,T]} be a portfolio process satisfying

   |  |  |  |
   | --- | --- | --- |
   |  | πt⊤​σ​(Yt)=Ds​u⊤​diag(St)⁡σ​(Yt)+Dy​u⊤​a​(Yt),\pi\_{t}^{\top}\sigma(Y\_{t})=D\_{s}u^{\top}\operatorname\*{diag}(S\_{t})\sigma(Y\_{t})+D\_{y}u^{\top}a(Y\_{t}), |  |

   where Ds​u\displaystyle D\_{s}u and Dy​u\displaystyle D\_{y}u are evaluated at (t,St,Yt)\displaystyle(t,S\_{t},Y\_{t}). Then x\displaystyle x is the replicating cost and π\displaystyle\pi is the hedging portfolio. Indeed,

   |  |  |  |
   | --- | --- | --- |
   |  | Xtx,π=u​(t,St,Yt),t∈[0,T].X^{x,\pi}\_{t}=u(t,S\_{t},Y\_{t}),\qquad t\in[0,T]. |  |

   In particular,

   |  |  |  |
   | --- | --- | --- |
   |  | XTx,π=Φ​(ST).X^{x,\pi}\_{T}=\Phi(S\_{T}). |  |
2. (ii)

   Moreover, if (Ht​Xtx,π)t∈[0,T]\displaystyle(H\_{t}X^{x,\pi}\_{t})\_{t\in[0,T]} is a ℙ\displaystyle\mathbb{P}-martingale, then

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | u​(t,s,y)=𝔼ℚ​[exp⁡(−∫tTr​(Yv)​𝑑v)​Φ​(ST)|St=s,Yt=y].u(t,s,y)=\mathbb{E}^{\mathbb{Q}}\left[\left.\exp\left(-\int\_{t}^{T}r(Y\_{v})dv\right)\Phi\left(S\_{T}\right)\right|S\_{t}=s,Y\_{t}=y\right]. |  | (44) |

   In particular, the replicating cost x\displaystyle x is given by

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | x≔u​(0,s0,y)=𝔼ℚ​[exp⁡(−∫0Tr​(Yv)​𝑑v)​Φ​(ST)].x\coloneqq u(0,s\_{0},y)=\mathbb{E}^{\mathbb{Q}}\left[\exp\left(-\int\_{0}^{T}r(Y\_{v})dv\right)\Phi\left(S\_{T}\right)\right]. |  | (45) |

###### Proof.

By the Ito formula,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1St0​u​(t,St,Yt)\displaystyle\displaystyle\frac{1}{S^{0}\_{t}}u(t,S\_{t},Y\_{t}) | =u​(0,s0,y)+∫0t1Sv0​{(∂tu+ℒ​u−r​u)​(v,Sv,Yv)​d​v+(Ds​u⊤​diag(Sv)⁡σ​(Yv)+Dy​u⊤​a​(Yv))​d​Wvℚ}\displaystyle\displaystyle=u(0,s\_{0},y)+\int\_{0}^{t}\frac{1}{S^{0}\_{v}}\left\{\left(\partial\_{t}u+\mathcal{L}u-ru\right)(v,S\_{v},Y\_{v})dv+\left(D\_{s}u^{\top}\operatorname\*{diag}(S\_{v})\sigma(Y\_{v})+D\_{y}u^{\top}a(Y\_{v})\right)dW^{\mathbb{Q}}\_{v}\right\} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =u​(0,s0,y)+∫0t1Sv0​(Ds​u⊤​diag(Sv)⁡σ​(Yv)+Dy​u⊤​a​(Yv))​𝑑Wvℚ\displaystyle\displaystyle=u(0,s\_{0},y)+\int\_{0}^{t}\frac{1}{S^{0}\_{v}}\left(D\_{s}u^{\top}\operatorname\*{diag}(S\_{v})\sigma(Y\_{v})+D\_{y}u^{\top}a(Y\_{v})\right)dW^{\mathbb{Q}}\_{v} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =x+∫0t1Sv0​πv⊤​σ​(Yv)​𝑑Wvℚ\displaystyle\displaystyle=x+\int\_{0}^{t}\frac{1}{S^{0}\_{v}}\pi\_{v}^{\top}\sigma(Y\_{v})dW^{\mathbb{Q}}\_{v} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Xtx,πSt0,\displaystyle\displaystyle=\frac{X^{x,\pi}\_{t}}{S^{0}\_{t}}, |  |

which proves (i). If (Ht​Xtπ)t∈[0,T]\displaystyle(H\_{t}X^{\pi}\_{t})\_{t\in[0,T]} is a ℙ\displaystyle\mathbb{P}-martingale, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | u​(t,St,Yt)\displaystyle\displaystyle u(t,S\_{t},Y\_{t}) | =Xtx,π\displaystyle\displaystyle=X^{x,\pi}\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1Ht​𝔼t​[HT​XTx,π]\displaystyle\displaystyle=\frac{1}{H\_{t}}\mathbb{E}\_{t}\left[H\_{T}X^{x,\pi}\_{T}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝔼tℚ​[exp⁡(−∫tTr​(Yv)​𝑑v)​Φ​(ST)].\displaystyle\displaystyle=\mathbb{E}^{\mathbb{Q}}\_{t}\left[\exp\left(-\int\_{t}^{T}r(Y\_{v})dv\right)\Phi\left(S\_{T}\right)\right]. |  |

By the Markov property of (S,Y)\displaystyle(S,Y), we obtain ([44](https://arxiv.org/html/2512.00346v1#A2.E44 "In item (ii) ‣ Theorem B.1. ‣ Appendix B Appendix: Option pricing theory with stochastic factor models in complete markets ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) and ([45](https://arxiv.org/html/2512.00346v1#A2.E45 "In item (ii) ‣ Theorem B.1. ‣ Appendix B Appendix: Option pricing theory with stochastic factor models in complete markets ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")).
∎

## Appendix C Appendix: Relationship between stochastic control methods and martingale methods

In this appendix, we verify that the terminal wealth obtained via the dynamic programming approach matches the optimal terminal wealth derived from martingale duality methods. We prove the result in complete stochastic factor models given by ([2](https://arxiv.org/html/2512.00346v1#S2.E2 "In 2.1 Stochastic flow representation of optimal feedback functions ‣ 2 Main results ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")).

###### Theorem C.1.

Let V:[0,T]×(0,∞)×ℝm\displaystyle V:[0,T]\times(0,\infty)\times\mathbb{R}^{m} be a classical solution to the HJB equation. Let π^:[0,T]×(0,∞)×ℝm\displaystyle\hat{\pi}:[0,T]\times(0,\infty)\times\mathbb{R}^{m} be a candidate for optimal investment strategies. Furthermore, we assume that

|  |  |  |
| --- | --- | --- |
|  | limt↗TVx​(t,x,y)=U′​(x),(x,y)∈(0,∞)×ℝm\lim\_{t\nearrow T}V\_{x}(t,x,y)=U^{\prime}(x),\quad(x,y)\in(0,\infty)\times\mathbb{R}^{m} |  |

and (Ht​Xtx,π^)t∈[0,T]\displaystyle(H\_{t}X^{x,\hat{\pi}}\_{t})\_{t\in[0,T]} is a martingale for some x>0\displaystyle x>0.
Then

|  |  |  |
| --- | --- | --- |
|  | XTx,π^=I​(λ^​HT),X^{x,\hat{\pi}}\_{T}=I(\hat{\lambda}H\_{T}), |  |

and π^\displaystyle\hat{\pi} is the optimal feedback strategy.

###### Proof.

We rewrite the HJB equation as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt+r​(y)​x​Vx+b​(y)⊤​Dy​V+12​Tr​(a​a⊤​(y)​Dy​y2​V)−Vx​x2​|σ⊤​(y)​π^​(t,x,y)|2=0.V\_{t}+r(y)xV\_{x}+b(y)^{\top}D\_{y}V+\frac{1}{2}\mathrm{Tr}\left(aa^{\top}(y)D^{2}\_{yy}V\right)-\frac{V\_{xx}}{2}|\sigma^{\top}(y)\hat{\pi}(t,x,y)|^{2}=0. |  | (46) |

Differentiating ([46](https://arxiv.org/html/2512.00346v1#A3.E46 "In Appendix C Appendix: Relationship between stochastic control methods and martingale methods ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")) with respect to x\displaystyle x, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt​x+r​(y)​Vx+r​(y)​x​Vx​x+b​(y)⊤​Dy​Vx+12​Tr​(a​a⊤​(y)​Dy​y2​Vx)+π^⊤​σ​(θ​Vx​x+a⊤​Dy​Vx​x)+Vx​x​x2​|σ⊤​(y)​π^​(t,x,y)|2=0.\begin{multlined}V\_{tx}+r(y)V\_{x}+r(y)xV\_{xx}+b(y)^{\top}D\_{y}V\_{x}+\frac{1}{2}\mathrm{Tr}\left(aa^{\top}(y)D^{2}\_{yy}V\_{x}\right)\\ +\hat{\pi}^{\top}\sigma(\theta V\_{xx}+a^{\top}D\_{y}V\_{xx})+\frac{V\_{xxx}}{2}|\sigma^{\top}(y)\hat{\pi}(t,x,y)|^{2}=0.\end{multlined}V\_{tx}+r(y)V\_{x}+r(y)xV\_{xx}+b(y)^{\top}D\_{y}V\_{x}+\frac{1}{2}\mathrm{Tr}\left(aa^{\top}(y)D^{2}\_{yy}V\_{x}\right)\\ +\hat{\pi}^{\top}\sigma(\theta V\_{xx}+a^{\top}D\_{y}V\_{xx})+\frac{V\_{xxx}}{2}|\sigma^{\top}(y)\hat{\pi}(t,x,y)|^{2}=0. |  | (47) |

That is,

|  |  |  |
| --- | --- | --- |
|  | Vt​x+r​(y)​Vx+ℒπ^​Vx=0,V\_{tx}+r(y)V\_{x}+\mathcal{L}^{\hat{\pi}}V\_{x}=0, |  |

where ℒπ\displaystyle\mathcal{L}^{\pi} is a controlled generator:

|  |  |  |
| --- | --- | --- |
|  | ℒπ​f≔r​(y)​x​fx+b​(y)⊤​Dy​f+12​Tr​(a​a⊤​(y)​Dy​y2​f)+π⊤​σ​(y)​(θ​(y)​fx+a⊤​(y)​Dy​fx)+12​|σ⊤​(y)​π|2​fx​x=0.\mathcal{L}^{\pi}f\coloneqq r(y)xf\_{x}+b(y)^{\top}D\_{y}f+\frac{1}{2}\mathrm{Tr}\left(aa^{\top}(y)D\_{yy}^{2}f\right)+\pi^{\top}\sigma(y)\left(\theta(y)f\_{x}+a^{\top}(y)D\_{y}f\_{x}\right)+\frac{1}{2}|\sigma^{\top}(y)\pi|^{2}f\_{xx}=0. |  |

By the Ito formula,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Vx​(t,Xtx,π^,Yt)\displaystyle\displaystyle dV\_{x}(t,X^{x,\hat{\pi}}\_{t},Y\_{t}) | =(Vx​t+ℒπ^t​Vx)​d​t+{Vx​x​π^t⊤​σ​(Yt)+Dy​Vx⊤​a​(Yt)}​d​Wt\displaystyle\displaystyle=(V\_{xt}+\mathcal{L}^{\hat{\pi}\_{t}}V\_{x})dt+\left\{V\_{xx}\hat{\pi}^{\top}\_{t}\sigma(Y\_{t})+D\_{y}V\_{x}^{\top}a(Y\_{t})\right\}dW\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Vx​(−r​(Yt)​d​t−θ​(Yt)⊤​d​Wt).\displaystyle\displaystyle=V\_{x}\left(-r(Y\_{t})dt-\theta(Y\_{t})^{\top}dW\_{t}\right). |  |

Therefore,

|  |  |  |
| --- | --- | --- |
|  | Vx​(t,Xtx,π^,Yt)=Vx​(0,x,y)​Ht.V\_{x}(t,X^{x,\hat{\pi}}\_{t},Y\_{t})=V\_{x}(0,x,y)H\_{t}. |  |

Let t↗T\displaystyle t\nearrow T, then

|  |  |  |
| --- | --- | --- |
|  | U′​(XTx,π^)=Vx​(0,x,y)​HT,U^{\prime}(X^{x,\hat{\pi}}\_{T})=V\_{x}(0,x,y)H\_{T}, |  |

which leads to

|  |  |  |
| --- | --- | --- |
|  | XTx,π^=I​(Vx​(0,x,y)​HT).X^{x,\hat{\pi}}\_{T}=I\left(V\_{x}(0,x,y)H\_{T}\right). |  |

Because Ht​Xtx,π^\displaystyle H\_{t}X^{x,\hat{\pi}}\_{t} is a martingale,

|  |  |  |
| --- | --- | --- |
|  | x=𝔼​[HT​XTx,π^]=𝔼​[HT​I​(Vx​(0,x,y)​HT)]x=\mathbb{E}\left[H\_{T}X^{x,\hat{\pi}}\_{T}\right]=\mathbb{E}\left[H\_{T}I\left(V\_{x}(0,x,y)H\_{T}\right)\right] |  |

holds and λ^=Vx​(0,x,y)\displaystyle\hat{\lambda}=V\_{x}(0,x,y) by the uniqueness of λ^\displaystyle\hat{\lambda}. We have completed the proof.
∎

## Appendix D Appendix: Matrix Riccati equation

We recall some facts stated in [[21](https://arxiv.org/html/2512.00346v1#bib.bib21)] about matrix Riccati differential equations.
Let T>0,A∈ℝn×n,B∈ℝn×m,C∈ℝm×n\displaystyle T>0,\;A\in\mathbb{R}^{n\times n},\;B\in\mathbb{R}^{n\times m},\;C\in\mathbb{R}^{m\times n}.
We consider an n×n\displaystyle n\times n matrix solution P=P​(⋅;T):[0,T]→ℝn×n\displaystyle P=P(\cdot\;;T):[0,T]\to\mathbb{R}^{n\times n} of the Riccati differential equation

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | P˙​(t)−P​(t)​B​B⊤​P​(t)+A⊤​P​(t)+P​(t)​A+C⊤​C=0,t∈[0,T],\displaystyle\dot{P}(t)-P(t)BB^{\top}P(t)+A^{\top}P(t)+P(t)A+C^{\top}C=0,\quad t\in[0,T], |  | (48) |
|  |  | P​(T)=0.\displaystyle P(T)=0. |  |

First, we state the existence and uniqueness of ([48](https://arxiv.org/html/2512.00346v1#A4.E48 "In Appendix D Appendix: Matrix Riccati equation ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")).

###### Theorem D.1.

1. (i)

   There exists a nonnegative unique solution P:[0,T]→𝕊+n\displaystyle P:[0,T]\to\mathbb{S}^{n}\_{+} to ([48](https://arxiv.org/html/2512.00346v1#A4.E48 "In Appendix D Appendix: Matrix Riccati equation ‣ Convergence Rates of Turnpike Theorems for Portfolio Choice in Stochastic Factor Models")).
2. (ii)

   For any 0≤t1≤t2≤T\displaystyle 0\leq t\_{1}\leq t\_{2}\leq T,

   |  |  |  |
   | --- | --- | --- |
   |  | 0≤P​(t2)≤P​(t1)0\leq P(t\_{2})\leq P(t\_{1}) |  |

   holds.

Next, we state the asymptotic behaviors of the solution.

###### Definition D.1.

1. (i)

   The pair (A,B)\displaystyle(A,B) is said to be stabilizable if a matrix L∈ℝm×n\displaystyle L\in\mathbb{R}^{m\times n} exists such that A+B​L\displaystyle A+BL is stable (i.e., all its eigenvalues have negative real parts).
2. (ii)

   The pair (C,A)\displaystyle(C,A) is said to be detectable if a matrix F∈ℝn×m\displaystyle F\in\mathbb{R}^{n\times m} exists such that F​C+A\displaystyle FC+A is stable.

###### Theorem D.2.

1. (i)

   If (A,B)\displaystyle(A,B) is stabilizable, then there exists a finite nonnegative matrix P∞∈𝕊+n\displaystyle P\_{\infty}\in\mathbb{S}^{n}\_{+} such that

   |  |  |  |
   | --- | --- | --- |
   |  | limT↗∞P​(t;T)=P∞\lim\_{T\nearrow\infty}P(t;T)=P\_{\infty} |  |

   for any t\displaystyle t, and P∞\displaystyle P\_{\infty} satisfies the algebraic Riccati equation

   |  |  |  |
   | --- | --- | --- |
   |  | −P∞​B​B⊤​P∞+A⊤​P∞+P∞​A+C⊤​C=0.-P\_{\infty}BB^{\top}P\_{\infty}+A^{\top}P\_{\infty}+P\_{\infty}A+C^{\top}C=0. |  |
2. (ii)

   If (A,B)\displaystyle(A,B) is stabilizable and (C,A)\displaystyle(C,A) is detectable, then A−B​B⊤​P∞\displaystyle A-BB^{\top}P\_{\infty} is stable.

The following theorem is Lemma 4.4 in [[22](https://arxiv.org/html/2512.00346v1#bib.bib22)].

###### Theorem D.3.

Let K:[0,∞)→ℝn×n,g:[0,∞)→ℝn\displaystyle K:[0,\infty)\to\mathbb{R}^{n\times n},\;g:[0,\infty)\to\mathbb{R}^{n}, and f:[0,∞)→ℝn\displaystyle f:[0,\infty)\to\mathbb{R}^{n} be a solution of the ordinary differential equation

|  |  |  |
| --- | --- | --- |
|  | f˙​(t)=K​(t)​f​(t)+g​(t),f​(0)=0.\dot{f}(t)=K(t)f(t)+g(t),\quad f(0)=0. |  |

Suppose that K​(t)→K~∈ℝn×n\displaystyle K(t)\rightarrow\tilde{K}\in\mathbb{R}^{n\times n} and g​(t)→g~∈ℝn\displaystyle g(t)\rightarrow\tilde{g}\in\mathbb{R}^{n} as t↗∞\displaystyle t\nearrow\infty and K~\displaystyle\tilde{K} is a stable matrix. Then there exists f~=limt↗∞f​(t)\displaystyle\tilde{f}=\lim\_{t\nearrow\infty}f(t) that satisfies the equation

|  |  |  |
| --- | --- | --- |
|  | K~​f~+g~=0.\tilde{K}\tilde{f}+\tilde{g}=0. |  |

### Acknowledgement

This work was supported by JST SPRING, Grant Number JPMJSP2138.

## References

* [1]

  Ahn, D. H., Dittmar, R. F., & Gallant, A. R. (2002). Quadratic term structure models: Theory and evidence. The Review of financial studies, 15(1), 243-288.
* [2]

  Branger, N., Chen, A., Mahayni, A., & Nguyen, T. (2023). Optimal collective investment: an analysis of individual welfare. Mathematics and Financial Economics, 17(1), 101-125.
* [3]

  Bian, B., & Zheng, H. (2015). Turnpike property and convergence rate for an investment model with general utility functions. Journal of Economic Dynamics and Control, 51, 28-49.
* [4]

  Bian, B., & Zheng, H. (2019). Turnpike property and convergence rate for an investment and consumption model. Mathematics and Financial Economics, 13(2), 227-251.
* [5]

  Cox, J. C., & Huang, C. F. (1992). A continuous-time portfolio turnpike theorem. Journal of Economic Dynamics and Control, 16(3-4), 491-507.
* [6]

  Detemple, J. B., Garcia, R., & Rindisbacher, M. (2003). A Monte Carlo method for optimal portfolios. The journal of Finance, 58(1), 401-446.
* [7]

  Detemple, J., & Rindisbacher, M. (2010). Dynamic asset allocation: Portfolio decomposition formula and applications. The Review of Financial Studies, 23(1), 25-100.
* [8]

  Dorfman, R., Samuelson, P. A., & Solow, R. M. (1958). Linear programming and economic analysis. New York, McGraw-Hill.
* [9]

  Dybvig, P. H., Rogers, L. C. G., & Back, K. (1999). Portfolio turnpikes. The Review of Financial Studies, 12(1), 165-195.
* [10]

  Fukaya, R. (2005). Application of Stochastic Flows to Optimal Portfolio Strategies. Journal of mathematical sciences, the University of Tokyo, 12(3), 349-397.
* [11]

  Föllmer, H. & Schied, A. (2025). Stochastic Finance: An Introduction in Discrete Time. De Gruyter.
* [12]

  Geng, T., & Zariphopoulou, T. (2025). Temporal and spatial turnpikes in Ito-diffusion markets under forward performance criteria. Numerical Algebra, Control and Optimization, 15(1), 243-272.
* [13]

  Guasoni, P., Kardaras, C., Robertson, S., & Xing, H. (2014). Abstract, classic, and explicit turnpikes. Finance and stochastics, 18, 75-114.
* [14]

  Hakansson, N. H. (1974). Convergence to isoelastic utility and policy in multiperiod portfolio choice. Journal of Financial Economics, 1(3), 201-224.
* [15]

  Honda, T., & Kamimura, S. (2011). On the verification theorem of dynamic portfolio-consumption problems with stochastic market price of risk. Asia-Pacific Financial Markets, 18(2), 151-166.
* [16]

  Huberman, G., & Ross, S. (1983). Portfolio Turnpike Theorems, Risk Aversion, and Regularly Varying Utility Functions. Econometrica, 51(5), 1345-1361.
* [17]

  Huang, C. F., & Zariphopoulou, T. (1999). Turnpike behavior of long-term investments. Finance and Stochastics, 3, 15-34.
* [18]

  Jensen, B. A., & Nielsen, J. A. (2016). How suboptimal are linear sharing rules?. Annals of Finance, 12(2), 221-243.
* [19]

  Jin, X. (1998). Consumption and portfolio turnpike theorems in a continuous-time finance model. Journal of Economic Dynamics and Control, 22(7), 1001-1026.
* [20]

  Karatzas, I., & Shreve, S. E., (1998). Methods of mathematical finance (Vol. 39, pp. xvi+-407). New York: Springer.
* [21]

  Kucera, V. (1973). A review of the matrix Riccati equation. Kybernetika, 9(1), 42-61.
* [22]

  Kuroda, K., & Nagai, H. (2002). Risk-sensitive portfolio optimization on infinite time horizon. Stochastics and Stochastic Reports, 73(3-4), 309-331.
* [23]

  Karatzas, I., Ocone, D. L., & Li, J. (1991). An extension of Clark’s formula. Stochastics: An International Journal of Probability and Stochastic Processes, 37(3), 127-131.
* [24]

  Lakner, P. (1998). Optimal trading strategy for an investor: the case of partial information. Stochastic Processes and their Applications, 76(1), 77-97.
* [25]

  Leippold, M., & Wu, L. (2002). Asset pricing under the quadratic class. Journal of Financial and Quantitative Analysis, 37(2), 271-295.
* [26]

  Leland, H. (1972). On turnpike portfolios. In: Szego, G., Shell, K. (eds.) Mathematical Methods in Investment
  and Finance, p. 24. North-Holland, Amsterdam
* [27]

  Liptser, R. S., & Shiryaev, A. N. (2013). Statistics of random processes: I. General theory (Vol. 5). Springer Science & Business Media.
* [28]

  Liu, R., & Muhle-Karbe, J. (2013). Portfolio choice with stochastic investment opportunities: A User’s guide. arXiv preprint arXiv:1311.1715.
* [29]

  Mao, X. (2007). Stochastic differential equations and applications. Elsevier.
* [30]

  Merton, R. C. (1969). Lifetime portfolio selection under uncertainty: The continuous-time case. The review of Economics and Statistics, 247-257.
* [31]

  Merton, R. (1971). Optimum consumption and portfolio rules in a continuous-time model. Journal of Economic Theory, 3(4), 373-413.
* [32]

  Mossin, J. (1968). Optimal Multiperiod Portfolio Policies. The Journal of Business, 41(2), 215-229.
* [33]

  Nagai, H. (2003). Optimal strategies for risk-sensitive portfolio optimization problems for general factor models. SIAM journal on control and optimization, 41(6), 1779-1800.
* [34]

  Nualart, D. (2006). The Malliavin calculus and related topics. Berlin, Heidelberg: Springer Berlin Heidelberg.
* [35]

  Neumann, J. V. (1945). A model of general economic equilibrium. The Review of Economic Studies, 13(1), 1-9.
* [36]

  Ocone, D. L., & Karatzas, I. (1991). A generalized Clark representation formula, with application to optimal portfolios. Stochastics: An International Journal of Probability and Stochastic Processes, 34(3-4), 187-220.
* [37]

  Putschögl, W., & Sass, J. (2008). Optimal consumption and investment under partial information. Decisions in Economics and Finance, 31(2), 137-170.
* [38]

  Qin, L., & Linetsky, V. (2017). Long-term risk: A martingale approach. Econometrica, 85(1), 299-312.
* [39]

  Qin, L., & Linetsky, V. (2017). Long-term factorization of affine pricing kernels. Mathematics and Financial Economics, 11(4), 479-498.
* [40]

  Qin, L., & Linetsky, V. (2018). Long-term factorization in Heath-Jarrow-Morton models. Finance and Stochastics, 22(3), 621-641.
* [41]

  Ross, S. A. (1974). Portfolio turnpike theorems for constant policies. Journal of Financial Economics, 1(2), 171-198.
* [42]

  Robertson, S., & Xing, H. (2017). Long-term optimal investment in matrix valued factor models. SIAM Journal on Financial Mathematics, 8(1), 400-434.
* [43]

  Sass, J., & Haussmann, U. G. (2004). Optimizing the terminal wealth under partial information: The drift process as a continuous time Markov chain. Finance and Stochastics, 8(4), 553-577.
* [44]

  Sun, J., & Yong, J. (2020). Stochastic linear-quadratic optimal control theory: Open-loop and closed-loop solutions. Springer Nature.
* [45]

  Zariphopoulou, T. (2009). Optimal asset allocation in a stochastic factor model - an overview and open problems. In H. Albrecher, W. Runggaldier & W. Schachermayer (Ed.), Advanced Financial Modelling (pp. 427-456). Berlin, New York: De Gruyter.