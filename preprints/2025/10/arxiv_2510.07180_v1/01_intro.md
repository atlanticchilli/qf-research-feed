---
authors:
- Masahiro Kato
- Kentaro Baba
- Hibiki Kaibuchi
- Ryo Inokuchi
doc_id: arxiv:2510.07180v1
family_id: arxiv:2510.07180
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Bayesian Portfolio Optimization by Predictive Synthesis
url_abs: http://arxiv.org/abs/2510.07180v1
url_html: https://arxiv.org/html/2510.07180v1
venue: arXiv q-fin
version: 1
year: 2025
---


Masahiro Kato
  
Kentaro Baba
  
Hibiki Kaibuchi
  
Ryo Inokuchi

###### Abstract

Portfolio optimization is a critical task in investment. Most existing portfolio optimization methods require information on the distribution of returns of the assets that make up the portfolio. However, such distribution information is usually unknown to investors. Various methods have been proposed to estimate distribution information, but their accuracy greatly depends on the uncertainty of the financial markets. Due to this uncertainty, a model that could well predict the distribution information at one point in time may perform less accurately compared to another model at a different time. To solve this problem, we investigate a method for portfolio optimization based on Bayesian predictive synthesis (BPS), one of the Bayesian ensemble methods for meta-learning. We assume that investors have access to multiple asset return prediction models. By using BPS with dynamic linear models to combine these predictions, we can obtain a Bayesian predictive posterior about the mean rewards of assets that accommodate the uncertainty of the financial markets. In this study, we examine how to construct mean-variance portfolios and quantile-based portfolios based on the predicted distribution information.

## I Introduction

Portfolio optimization is a critical challenge in investment, where the goal is to hold multiple financial assets in an appropriate allocation to achieve desirable asset management for investors.

There are several approaches to understanding the risk of a portfolio. The mean-variance approach, one of the most classical criteria, was proposed by Markowitz and is also known as the Markowitz portfolio ([Markowitz1952,](https://arxiv.org/html/2510.07180v1#bib.bib8) ; [Markowitz1959,](https://arxiv.org/html/2510.07180v1#bib.bib9) ; [Markowitz2000,](https://arxiv.org/html/2510.07180v1#bib.bib10) ). In the mean-variance approach, the portfolio’s variance is considered as the risk, and financial assets are allocated considering the trade-off between the portfolio’s expected value and variance. The quantile-based approach is also influential, where Value at Risk (VaR) and Conditional VaR (CVaR) are used as risk metrics. [Rockafellar2000OptimizationOC](https://arxiv.org/html/2510.07180v1#bib.bib15)  proposed constructing a portfolio by minimizing CVaR using linear programming. Moreover, the risk parity approach is a favored approach among investors, where assets are allocated so that the ratios of the variances of the financial assets’ returns become the portfolio’s risk.

Optimization of portfolios based on these criteria often requires information about the distribution of asset returns. For example, constructing a mean-variance portfolio requires the input of estimated means and variances of asset returns. Similarly, the quantile-based approach needs the shape of the distribution, and the risk parity approach requires the covariance matrix. This information on distributions is usually unknown to investors and needs to be estimated from data. Since the construction of portfolios depends on the input distribution information, estimation errors in this information can affect the portfolio composition and sometimes significantly degrade its performance [Chopra1993](https://arxiv.org/html/2510.07180v1#bib.bib4) .

Many difficulties in estimating information about the distribution of asset returns from data are due to market uncertainties. When the target time series is non-stationary or access is limited to data of a small sample size, the difficulty of estimating information about the distribution increases, making it challenging to construct portfolios.

This study adopts a Bayesian approach to tackle this issue. Firstly, we assume the existence of experts with their own predictions of asset returns. Then, we use Bayesian Predictive Synthesis (BPS), one of the Bayesian ensemble methods, to integrate these predictions ([mcalinn2019dynamic,](https://arxiv.org/html/2510.07180v1#bib.bib12) ; [mcalinn2020multivariate,](https://arxiv.org/html/2510.07180v1#bib.bib11) ). Bayesian Predictive Synthesis is a general framework that includes Bayesian model averaging as a special case. Following [mcalinn2019dynamic](https://arxiv.org/html/2510.07180v1#bib.bib12)  and [mcalinn2020multivariate](https://arxiv.org/html/2510.07180v1#bib.bib11) , this paper uses dynamic linear models, which are considered suitable for time series prediction. As a result of BPS, we obtain a predictive distribution for each asset return. Under this predictive distribution, we can evaluate the portfolio under each weight 𝒘\bm{w}. By optimizing the evaluation value for 𝒘\bm{w}, we can select appropriate weights. Among various criteria for weight selection, we consider the mean-variance approach, the quantile-based approach, and the risk parity approach.

The contribution of this study lies in investigating the outcomes when using practically significant portfolio selection criteria under the posterior predictive distribution obtained by BPS. The BPS of mean-variance portfolios has been explored from the perspective of quadratic utility maximization by [tallman2023bayesian](https://arxiv.org/html/2510.07180v1#bib.bib17) . This study further empirically considers the use of constrained optimization. Moreover, to our knowledge, the use of BPS in the quantile-based and risk parity approaches has not been thoroughly investigated. This study examines what outcomes can be obtained when using BPS for such portfolio construction methods.

## II Problem Setting

In this section, we formalize the problem of portfolio optimization. We consider optimizing a portfolio consisting of KK types of financial assets over TT periods, allowing for changes in the portfolio’s composition.

### II-A Asset Returns

Let Xa,t∈ℝX\_{a,t}\in\mathbb{R} be the return of a financial asset a∈[K]≔{1,2,…,K}a\in[K]\coloneqq\{1,2,\dots,K\} in period tt. The return vector for KK types of financial assets is denoted as

|  |  |  |
| --- | --- | --- |
|  | 𝑿t=(X1,t,X2,t,…,XK,t)⊤.\bm{X}\_{t}=\big(X\_{1,t},X\_{2,t},\dots,X\_{K,t}\big)^{\top}. |  |

Here, let 𝒙t\bm{x}\_{t} be the realized value of 𝑿t\bm{X}\_{t}. Also, let 𝑿s:t={𝑿s,𝑿s+1,…,𝑿t}\bm{X}\_{s:t}=\{\bm{X}\_{s},\bm{X}\_{s+1},\dots,\bm{X}\_{t}\} be the set of asset returns from period ss to tt, with its realized values denoted as 𝒙s:t\bm{x}\_{s:t}.

### II-B Portfolio

Define the set of portfolio weights as ΔK≔{z∈[0,1]K∣∑i=1Kzi=1}\Delta^{K}\coloneqq\{z\in[0,1]^{K}\mid\sum^{K}\_{i=1}z\_{i}=1\}. For simplicity, short selling is not allowed. Investors hold assets based on certain weights 𝒘∈ΔK\bm{w}\in\Delta^{K} and receive their returns. The return of a portfolio under the weights 𝒘∈ΔK\bm{w}\in\Delta^{K} can be written as

|  |  |  |
| --- | --- | --- |
|  | Rt​(𝒘)=𝒘⊤​𝑿t.\displaystyle R\_{t}(\bm{w})=\bm{w}^{\top}\bm{X}\_{t}. |  |

We construct a portfolio by choosing a desirable 𝒘\bm{w} under a suitable criterion. For simplicity, we assume that changing the portfolio’s composition at each time does not incur any costs.

### II-C Portfolio Selection Criteria

In this study, we consider constructing portfolios under the Bayesian posterior predictive distribution obtained through BPS. Specifically, we focus on three approaches: mean-variance portfolios, quantile-based portfolios, and risk-parity portfolios, using the posterior predictive distribution.

## III BPS

This section discusses obtaining the posterior predictive distribution of asset returns based on BPS. The method follows [mcalinn2020multivariate](https://arxiv.org/html/2510.07180v1#bib.bib11) .

### III-A Experts

To construct a portfolio, we need to input information about the distribution of asset returns 𝑿t\bm{X}\_{t}. In this study, we assume the existence of JJ experts who provide predictive distributions for the mean of 𝑿t\bm{X}\_{t}. Investors can construct portfolios based on these predictive distributions.

Let the state about the assets’ mean rewards prediction of an expert j∈[J]j\in[J] at time tt be denoted by the KK-dimensional vector 𝒛t​j≔(zt​1​j,zt​2​j,…,zt​K​j)⊤\bm{z}\_{tj}\coloneqq\big(z\_{t1j},z\_{t2j},\dots,z\_{tKj}\big)^{\top}. In this paper, each state zt​a​jz\_{taj} represents the prediction of expert j∈[J]j\in[J] for the price of asset a∈[K]a\in[K] in period tt. Also, let

|  |  |  |
| --- | --- | --- |
|  | 𝒛t≔(𝒛t​1,…,𝒛t​J).\bm{z}\_{t}\coloneqq\big(\bm{z}\_{t1},\dots,\bm{z}\_{tJ}\big). |  |

The predictive distribution of the state 𝒛t​j\bm{z}\_{tj} of expert jj is denoted by ht​j​(𝒛)h\_{tj}(\bm{z}). Let the set of predictive distributions for each asset and each expert in period tt be Ht≔(ht​j)j∈[J]H\_{t}\coloneqq(h\_{tj})\_{j\in[J]}. Also, let the set of predictive distributions up to period tt be H1:t=(Hs)s=1tH\_{1:t}=(H\_{s})^{t}\_{s=1}.

BPS is a method for integrating these experts’ predictive distributions to construct a new predictive distribution.

### III-B Modeling Portfolio Returns

Assume that the asset return vector follows a multivariate normal distribution

|  |  |  |
| --- | --- | --- |
|  | 𝑿t∣𝝁,Σ∼𝒩​(𝝁,Σ),\displaystyle\bm{X}\_{t}\mid\bm{\mu},\Sigma\sim\mathcal{N}\big(\bm{\mu},\Sigma\big), |  |

where 𝒩​(𝝁,Σ)\mathcal{N}\big(\bm{\mu},\Sigma\big) is a multivariate normal distribution with a mean vector 𝝁\bm{\mu} and a covariance matrix Σ\Sigma.
Under this assumption, the return of the portfolio follows a normal distribution

|  |  |  |
| --- | --- | --- |
|  | Rt​(𝒘)∣𝝁,Σ∼𝒩​(𝒘⊤​𝝁,𝒘⊤​Σ​𝒘).\displaystyle R\_{t}(\bm{w})\mid\bm{\mu},\Sigma\sim\mathcal{N}\big(\bm{w}^{\top}\bm{\mu},\bm{w}^{\top}\Sigma\bm{w}\big). |  |

Let 𝝁t\bm{\mu}\_{t} and Σt\Sigma\_{t} denote 𝝁\bm{\mu} and Σ\Sigma given by posterior samples, respectively. Then, the posterior density of the portfolio return p​(rt​(𝒘)∣𝒙1:(t−1),ℋ1:t)p\big(r\_{t}(\bm{w})\mid\bm{x}\_{1:(t-1)},\mathcal{H}\_{1:t}\big) under the observation of asset returns and the predictive model ℋ1:t\mathcal{H}\_{1:t} of experts is given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | p​(rt​(𝒘)∣𝒙1:(t−1),ℋ1:t)\displaystyle p\big(r\_{t}(\bm{w})\mid\bm{x}\_{1:(t-1)},\mathcal{H}\_{1:t}\big) |  | (1) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≔∫p​(rt​(𝒘)∣𝝁t,Σt,𝒙1:(t−1),ℋ1:t)\displaystyle\coloneqq\int p\big(r\_{t}(\bm{w})\mid\bm{\mu}\_{t},\Sigma\_{t},\bm{x}\_{1:(t-1)},\mathcal{H}\_{1:t}\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×p​(𝝁t,Σt∣𝒙1:(t−1),ℋ1:t)​d​Φt.\displaystyle\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \times p\big(\bm{\mu}\_{t},\Sigma\_{t}\mid\bm{x}\_{1:(t-1)},\mathcal{H}\_{1:t}\big)\mathrm{d}\Phi\_{t}. |  |

### III-C Synthesis Function

From ([1](https://arxiv.org/html/2510.07180v1#S3.E1 "Equation 1 ‣ III-B Modeling Portfolio Returns ‣ III BPS ‣ Bayesian Portfolio Optimization by Predictive Synthesis")), to calculate the posterior density p​(rt​(𝒘)∣𝒙1:(t−1),ℋ1:t)p\big(r\_{t}(\bm{w})\mid\bm{x}\_{1:(t-1)},\mathcal{H}\_{1:t}\big), it is sufficient to specify p​(rt​(𝒘)∣𝝁t,Σt,𝒙1:(t−1),ℋ1:t)p\big(r\_{t}(\bm{w})\mid\bm{\mu}\_{t},\Sigma\_{t},\bm{x}\_{1:(t-1)},\mathcal{H}\_{1:t}\big) and p​(𝝁t,Σt∣𝒙1:(t−1),ℋ1:t)p\big(\bm{\mu}\_{t},\Sigma\_{t}\mid\bm{x}\_{1:(t-1)},\mathcal{H}\_{1:t}\big).

First, we model p​(rt​(𝒘)∣𝝁t,Σt,𝒙1:(t−1),ℋ1:t)p\big(r\_{t}(\bm{w})\mid\bm{\mu}\_{t},\Sigma\_{t},\bm{x}\_{1:(t-1)},\mathcal{H}\_{1:t}\big). We consider a model where the effects of observed data 𝒙1:(t−1)\bm{x}\_{1:(t-1)} are only reflected in the parameters 𝝁t\bm{\mu}\_{t} and Σt\Sigma\_{t}. That is,

|  |  |  |
| --- | --- | --- |
|  | p​(rt​(𝒘)∣𝝁t,Σt,𝒙1:(t−1),ℋ1:t)=p​(rt​(𝒘)∣𝝁t,Σt,ℋ1:t).p\big(r\_{t}(\bm{w})\mid\bm{\mu}\_{t},\Sigma\_{t},\bm{x}\_{1:(t-1)},\mathcal{H}\_{1:t}\big)=p\big(r\_{t}(\bm{w})\mid\bm{\mu}\_{t},\Sigma\_{t},\mathcal{H}\_{1:t}\big). |  |

As addressed in this study, there is uncertainty in estimating the parameters 𝝁t\bm{\mu}\_{t} and Σt\Sigma\_{t}. We consider obtaining these parameters by integrating the predictive distributions of experts represented by H1:tH\_{1:t}, as

|  |  |  |
| --- | --- | --- |
|  | p​(rt​(𝒘)∣𝝁t,Σt,ℋ1:t)\displaystyle p\big(r\_{t}(\bm{w})\mid\bm{\mu}\_{t},\Sigma\_{t},\mathcal{H}\_{1:t}\big) |  |
|  |  |  |
| --- | --- | --- |
|  | ≔∫αt​(rt​(𝒘)∣𝒛t,𝝁t,Σt)​∏j∈[J]ht​j​(𝒛t,j)​d​𝒛t,j,\displaystyle\coloneqq\int\alpha\_{t}\big(r\_{t}(\bm{w})\mid\bm{z}\_{t},\bm{\mu}\_{t},\Sigma\_{t}\big)\prod\_{j\in[J]}h\_{tj}(\bm{z}\_{t,j})\mathrm{d}\bm{z}\_{t,j}, |  |

where αt:ℝ×ℝ×ℝ×ℝK×K→ℝ\alpha\_{t}:\mathbb{R}\times\mathbb{R}\times\mathbb{R}\times\mathbb{R}^{K\times K}\to\mathbb{R} is called the *synthesis function*. By changing the definition of this synthesis function, various models can be treated as a form of BPS. For example, Bayesian model averaging is included as a special case [hoeting1999bayesian](https://arxiv.org/html/2510.07180v1#bib.bib7) ; [geweke2011optimal](https://arxiv.org/html/2510.07180v1#bib.bib6) ; [aastveit2018combined](https://arxiv.org/html/2510.07180v1#bib.bib1) .

#### Dynamic Linear Models

Various definitions can be given to the synthesis function αt\alpha\_{t}, but in this study, we focus on *dynamic linear models* following [mcalinn2019dynamic](https://arxiv.org/html/2510.07180v1#bib.bib12)  and [mcalinn2020multivariate](https://arxiv.org/html/2510.07180v1#bib.bib11) , as

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝑿t=𝝁t+𝝂t,𝝂t∼𝒩​(0,𝑽t),\displaystyle\bm{X}\_{t}=\bm{\mu}\_{t}+\bm{\nu}\_{t},\qquad\bm{\nu}\_{t}\sim\mathcal{N}(0,\bm{V}\_{t}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝝁t=F​(𝒛t)​𝜷t,\displaystyle\bm{\mu}\_{t}=F(\bm{z}\_{t})\bm{\beta}\_{t}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | 𝜷t=𝜷t−1+𝝎t,𝝎t∼𝒩​(0,𝑾t).\displaystyle\bm{\beta}\_{t}=\bm{\beta}\_{t-1}+\bm{\omega}\_{t},\qquad\bm{\omega}\_{t}\sim\mathcal{N}(0,\bm{W}\_{t}). |  | (2) |

Here,

|  |  |  |
| --- | --- | --- |
|  | F​(𝒛t)≔(1𝒇t​1⊤0𝟎⊤⋯⋯​0𝟎⊤0𝟎⊤1𝒇t​2⊤⋮⋮⋱⋮0𝟎⊤⋯⋯⋯1𝒇t​K⊤),\displaystyle F(\bm{z}\_{t})\coloneqq\begin{pmatrix}1&\bm{f}^{\top}\_{t1}&0&\bm{0}^{\top}&\cdots&\cdots 0&\bm{0}^{\top}\\ 0&\bm{0}^{\top}&1&\bm{f}^{\top}\_{t2}&&&\vdots\\ \vdots&&&&\ddots&&\vdots\\ 0&\bm{0}^{\top}&\cdots&\cdots&\cdots&1&\bm{f}^{\top}\_{tK}\end{pmatrix}, |  |

where 𝒇t​k⊤≔(zt​k​1,zt​k​2,…,zt​k​J)\bm{f}^{\top}\_{tk}\coloneqq(z\_{tk1},z\_{tk2},\dots,z\_{tkJ}) is a J×1J\times 1 vector representing the predictions of JJ experts for the return of asset kk. Also, 𝜷t\bm{\beta}\_{t} is a (J+1)×K(J+1)\times K vector. Recall that zt​j=(𝒛t​1,…,𝒛t​J)z\_{tj}=\big(\bm{z}\_{t1},\dots,\bm{z}\_{tJ}\big) is generated from ht​j​(zt​j)h\_{tj}(z\_{tj}).

This model is a type of state space model and is considered suitable for modeling time series data, as addressed in this study. Let the set of parameters of the dynamic linear model be Φt≔(𝜷t,𝑽t,𝑾t)\Phi\_{t}\coloneqq\big(\bm{\beta}\_{t},\bm{V}\_{t},\bm{W}\_{t}\big). Then, the synthesis function can be rewritten as

|  |  |  |
| --- | --- | --- |
|  | αt​(rt​(𝒘)∣𝒛t,𝝁t,Σt)=αt​(rt​(𝒘)∣𝒛t,Φt).\displaystyle\alpha\_{t}\big(r\_{t}(\bm{w})\mid\bm{z}\_{t},\bm{\mu}\_{t},\Sigma\_{t}\big)=\alpha\_{t}\big(r\_{t}(\bm{w})\mid\bm{z}\_{t},\Phi\_{t}\big). |  |

Under this dynamic linear model, the time-varying coefficient 𝜷t\bm{\beta}\_{t} follows a random walk defined by ([2](https://arxiv.org/html/2510.07180v1#S3.E2 "Equation 2 ‣ Dynamic Linear Models ‣ III-C Synthesis Function ‣ III BPS ‣ Bayesian Portfolio Optimization by Predictive Synthesis")). Here,
𝑾t\bm{W}\_{t} is defined via a standard single discount factor specification (Section 6.3 in [WestHarrison1997book2](https://arxiv.org/html/2510.07180v1#bib.bib18) ; Section 4.3 in [Prado2010](https://arxiv.org/html/2510.07180v1#bib.bib13) ), using a state evolution discount factor e∈(0,1]e\in(0,1]. Moreover, the residual variance εt\varepsilon\_{t} follows a standard beta-gamma random walk volatility model (Section 10.8 in [WestHarrison1997book2](https://arxiv.org/html/2510.07180v1#bib.bib18) ; Section 4.3 in [Prado2010](https://arxiv.org/html/2510.07180v1#bib.bib13) ), with εt=εt−1​δ/γt\varepsilon\_{t}=\varepsilon\_{t-1}\delta/\gamma\_{t} for some discount factor δ∈(0,1]\delta\in(0,1] and where γt\gamma\_{t} are beta distributed innovations, independent over time and independent of νs\nu\_{s} and η1,r,…,ηJ,r\eta\_{1,r},\dots,\eta\_{J,r} for all t,s,rt,s,r. Given choices of discount factors underlying these two components, and a (conjugate normal/inverse-gamma) prior for (w0,0,w1,0,…,wJ,0,ν0)(w\_{0,0},w\_{1,0},\ldots,w\_{J,0},\nu\_{0}) at t=0,t=0, the model is specified.

### III-D Posterior Predictive Distribution

As a result of this Bayesian modeling, we can obtain the posterior predictive distribution as

|  |  |  |
| --- | --- | --- |
|  | p​(rt​(𝒘)∣𝒙1:(t−1),ℋ1:t)≔\displaystyle p\big(r\_{t}(\bm{w})\mid\bm{x}\_{1:(t-1)},\mathcal{H}\_{1:t}\big)\coloneqq |  |
|  |  |  |
| --- | --- | --- |
|  | ∫p​(rt​(𝒘)∣𝒙1:(t−1),Φt,ℋ1:t)​p​(Φt∣𝒙1:(t−1),ℋ1:t)​𝑑Φt,\displaystyle\int p\big(r\_{t}(\bm{w})\mid\bm{x}\_{1:(t-1)},\Phi\_{t},\mathcal{H}\_{1:t}\big)p\big(\Phi\_{t}\mid\bm{x}\_{1:(t-1)},\mathcal{H}\_{1:t}\big)d\Phi\_{t}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | p​(rt​(𝒘)∣𝒙1:(t−1),Φt,ℋ1:t)≔p​(rt​(𝒘)∣Φt,ℋ1:t)\displaystyle p\big(r\_{t}(\bm{w})\mid\bm{x}\_{1:(t-1)},\Phi\_{t},\mathcal{H}\_{1:t}\big)\coloneqq p\big(r\_{t}(\bm{w})\mid\Phi\_{t},\mathcal{H}\_{1:t}\big) |  |
|  |  |  |
| --- | --- | --- |
|  | =∫αt​(rt​(𝒘)∣𝒛t,Φt)​∏j∈[J]ht​j​(𝒛t,j)​d​𝒛t,j.\displaystyle=\int\alpha\_{t}\big(r\_{t}(\bm{w})\mid\bm{z}\_{t},\Phi\_{t}\big)\prod\_{j\in[J]}h\_{tj}(\bm{z}\_{t,j})\mathrm{d}\bm{z}\_{t,j}. |  |

We can obtain the information required for portfolio optimization from this posterior predictive distribution. For example, the expectation of some function g:ℝ→ℝg:\mathbb{R}\to\mathbb{R} can be calculated as

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[g​(Rt​(𝒘))∣𝒙1:(t−1),ℋ1:t]\displaystyle\mathbb{E}\left[g(R\_{t}(\bm{w}))\mid\bm{x}\_{1:(t-1)},\mathcal{H}\_{1:t}\right] |  |
|  |  |  |
| --- | --- | --- |
|  | =∫∫∫g​(rt​(𝒘))​αt​(rt∣𝒛t,Φt)\displaystyle=\int\int\int g(r\_{t}(\bm{w}))\alpha\_{t}\big(r\_{t}\mid\bm{z}\_{t},\Phi\_{t}\big) |  |
|  |  |  |
| --- | --- | --- |
|  | ∏j∈[J]ht​j​(zt,j)​p​(Φt∣𝒙1:(t−1),ℋ1:t)​d​rt​(𝒘)​d​zt,j​d​Φt.\displaystyle\ \ \ \prod\_{j\in[J]}h\_{tj}(z\_{t,j})p\big(\Phi\_{t}\mid\bm{x}\_{1:(t-1)},\mathcal{H}\_{1:t}\big)\mathrm{d}r\_{t}(\bm{w})\mathrm{d}z\_{t,j}\mathrm{d}\Phi\_{t}. |  |

In BPS, since the posterior distribution cannot be obtained analytically, it is computed by simulation using Markov Chain Monte Carlo (MCMC). The details of MCMC are described in [mcalinn2020multivariate](https://arxiv.org/html/2510.07180v1#bib.bib11) .

## IV Bayesian Portfolio

Here, we introduce portfolio optimization based on the predictive distribution obtained through BPS.

### IV-A Mean-Variance Portfolio

First, we discuss the mean-variance approach based on the Bayesian posterior predictive distribution. [Bauder2021](https://arxiv.org/html/2510.07180v1#bib.bib5)  proposes a method for constructing a portfolio independent of unknown parameters by expressing the parameters of the asset return distribution as a function of observed data under appropriate modeling. Additionally, [tallman2023bayesian](https://arxiv.org/html/2510.07180v1#bib.bib17)  proposes a mean-variance approach based on multivariate BPS. In this section, based on these prior studies, we examine the mean-variance approach utilizing BPS.

#### Constrained Optimization.

As a method to construct a mean-variance portfolio, we consider a constrained optimization problem characterized by the posterior mean 𝔼​[Rt​(𝒘)∣𝒙1:(t−1),ℋ1:t]\mathbb{E}\left[R\_{t}(\bm{w})\mid\bm{x}\_{1:(t-1)},\mathcal{H}\_{1:t}\right] and the posterior variance Var​[Rt​(𝒘)∣𝒙1:(t−1),ℋ1:t]\mathrm{Var}\left[R\_{t}(\bm{w})\mid\bm{x}\_{1:(t-1)},\mathcal{H}\_{1:t}\right] at each period tt, conditioned on 𝒙1:(t−1)\bm{x}\_{1:(t-1)} and H1:tH\_{1:t}. Namely, the weights 𝒘MV\bm{w}^{\mathrm{MV}} of the mean-variance portfolio are defined as the solution to the optimization problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒘MV∈arg​min𝒘∈ΔK\displaystyle\bm{w}^{\mathrm{MV}}\in\operatorname\*{arg\,min}\_{\bm{w}\in\Delta^{K}} | Var​[Rt​(𝒘)∣𝒙1:(t−1),ℋ1:t]\displaystyle\ \ \ \mathrm{Var}\left[R\_{t}(\bm{w})\mid\bm{x}\_{1:(t-1)},\mathcal{H}\_{1:t}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | s.t.\displaystyle\mathrm{s.t.} | 𝔼​[Rt​(𝒘)∣𝒙1:(t−1),ℋ1:t]≥η,\displaystyle\ \ \ \mathbb{E}\left[R\_{t}(\bm{w})\mid\bm{x}\_{1:(t-1)},\mathcal{H}\_{1:t}\right]\geq\eta, |  |

where η>0\eta>0 is the mean constraint.

#### Expected Quadratic Utility Maximization.

The quadratic utility function of an investor operating a portfolio with weights 𝒘∈ΔK\bm{w}\in\Delta^{K} is defined as

|  |  |  |
| --- | --- | --- |
|  | U​(𝒘)≔\displaystyle U(\bm{w})\coloneqq |  |
|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Rt​(𝒘)∣𝒙1:(t−1),ℋ1:t]−γ2​𝔼​[Rt2​(𝒘)∣𝒙1:(t−1),ℋ1:t],\displaystyle\mathbb{E}\left[R\_{t}(\bm{w})\mid\bm{x}\_{1:(t-1)},\mathcal{H}\_{1:t}\right]-\frac{\gamma}{2}\mathbb{E}\left[R\_{t}^{2}(\bm{w})\mid\bm{x}\_{1:(t-1)},\mathcal{H}\_{1:t}\right], |  |

and the weights 𝒘\bm{w} of the mean-variance portfolio maximize the expected value of this quadratic utility. In Bayesian mean-variance portfolios, using the posterior mean, the weights 𝒘~MV\widetilde{\bm{w}}^{\mathrm{MV}} of the mean-variance portfolio can be given as

|  |  |  |
| --- | --- | --- |
|  | 𝒘~MV∈arg​max𝒘∈ΔK⁡𝔼​[U​(𝒘)∣𝒙1:(t−1),ℋ1:t].\displaystyle\widetilde{\bm{w}}^{\mathrm{MV}}\in\operatorname\*{arg\,max}\_{\bm{w}\in\Delta^{K}}\mathbb{E}\left[U(\bm{w})\mid\bm{x}\_{1:(t-1)},\mathcal{H}\_{1:t}\right]. |  |

The solution to the constrained optimization problem is known to correspond to the solution of this expected quadratic utility maximization problem under suitable conditions. [tallman2023bayesian](https://arxiv.org/html/2510.07180v1#bib.bib17)  in particular discusses the BPS-based mean-variance portfolio from the perspective of expected quadratic utility maximization.

### IV-B Quantile-Based Portfolio

Next, we consider a quantile-based portfolio using the Bayesian posterior predictive distribution obtained through BPS. In this study, we adopt the Bayesian quantile-based risk metric defined by [bodnar2020bayesian](https://arxiv.org/html/2510.07180v1#bib.bib2) .

#### VaR and CVaR.

Define a loss function ℓ:ℝ→ℝ\ell:\mathbb{R}\to\mathbb{R} for the portfolio return R​(𝒘)R(\bm{w}), and denote L​(𝒘)≔ℓ​(R​(𝒘))L(\bm{w})\coloneqq\ell(R(\bm{w})). In this paper, we set L​(𝒘)=−R​(𝒘)L(\bm{w})=-R(\bm{w}). Here, let FL​(𝒘),t−1F\_{L(\bm{w}),t-1} be the cumulative density function of L​(R​(𝒘))L(R(\bm{w})). Then, the Bayesian VaR that evaluates the loss incurred within a certain probability using the posterior distribution is defined as

|  |  |  |
| --- | --- | --- |
|  | VaRβ,t−1​(L​(𝒘))≔infl∈ℝ{FL​(𝒘),t−1​(l)≥β},\displaystyle\mathrm{VaR}\_{\beta,t-1}\big(L(\bm{w})\big)\coloneqq\inf\_{l\in\mathbb{R}}\Big\{F\_{L(\bm{w}),t-1}(l)\geq\beta\Big\}, |  |

where β∈(0,1)\beta\in(0,1) represents the quantile. Similarly, the CVaR, which represents the average loss when the portfolio return loss exceeds a certain probability level β\beta, is defined as

|  |  |  |
| --- | --- | --- |
|  | CVaRβ,t−1​(L​(𝒘))\displaystyle\mathrm{CVaR}\_{\beta,t-1}\big(L(\bm{w})\big) |  |
|  |  |  |
| --- | --- | --- |
|  | ≔𝔼​[L​(𝒘)∣L​(𝒘)≥VaRβ,t−1​(L​(𝒘)),𝒙1:(t−1),ℋ1:t].\displaystyle\coloneqq\mathbb{E}\Big[L(\bm{w})\mid L(\bm{w})\geq\mathrm{VaR}\_{\beta,t-1}(L(\bm{w})),\bm{x}\_{1:(t-1)},\mathcal{H}\_{1:t}\Big]. |  |

This definition of CVaR is based on [Bodnar2021](https://arxiv.org/html/2510.07180v1#bib.bib3)  and includes the result of Proposition 6 in [Rockafeller2002](https://arxiv.org/html/2510.07180v1#bib.bib16)  as a special case. [bodnar2020bayesian](https://arxiv.org/html/2510.07180v1#bib.bib2)  discusses methods for constructing portfolios using the Bayesian VaR and CVaR defined in this way.

#### Quantile-Based Portfolio on Returns.

Extending the concepts of VaR and CVaR, we can also consider a portfolio based on the quantiles of returns. Similarly to VaR, define the Value-of-Return (VoR) as

|  |  |  |
| --- | --- | --- |
|  | VoRα,t−1​(R​(𝒘))≔infr∈ℝ{FR​(𝒘),t−1​(r)≥α},\displaystyle\mathrm{VoR}\_{\alpha,t-1}\Big(R(\bm{w})\Big)\coloneqq\inf\_{r\in\mathbb{R}}\Big\{F\_{R(\bm{w}),t-1}(r)\geq\alpha\Big\}, |  |

where FR​(𝒘),t−1F\_{R(\bm{w}),t-1} is the cumulative density function of R​(R​(𝒘))R(R(\bm{w})). Then, we define the Conditional VoR (CVoR) as

|  |  |  |
| --- | --- | --- |
|  | CVoRα,t−1​(R​(𝒘))≔𝔼​[R​(𝒘)∣R​(𝒘)≥VoRα​(R​(𝒘))].\displaystyle\mathrm{CVoR}\_{\alpha,t-1}\Big(R(\bm{w})\Big)\coloneqq\mathbb{E}\Big[R(\bm{w})\mid R(\bm{w})\geq\mathrm{VoR}\_{\alpha}(R(\bm{w}))\Big]. |  |

#### Portfolio Optimization.

Following [Bodnar2021](https://arxiv.org/html/2510.07180v1#bib.bib3) , we use VaR or VoR to obtain the portfolio weights 𝒘Q\bm{w}^{\mathrm{Q}} by solving

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | 𝒘Q∈max𝒘∈ΔK⁡CVoRα,t−1​(R​(𝒘))\displaystyle\bm{w}^{\mathrm{Q}}\in\max\_{\bm{w}\in\Delta^{K}}\mathrm{CVoR}\_{\alpha,t-1}(R(\bm{w})) |  | (3) |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | VaRβ,t−1​(L​(𝒘))≤v0,\displaystyle\mathrm{VaR}\_{\beta,t-1}\big(L(\bm{w})\big)\leq v\_{0}, |  |

where v0∈ℝv\_{0}\in\mathbb{R} is the maximum loss an investor is willing to bear under risk.

In addition, portfolio optimization in [bodnar2020bayesian](https://arxiv.org/html/2510.07180v1#bib.bib2)  considers an objective function defined as

|  |  |  |
| --- | --- | --- |
|  | Q​(𝒘)≔−R​(𝒘)+qα​𝒘⊤​Σt​𝒘,\displaystyle Q(\bm{w})\coloneqq-R\big(\bm{w}\big)+q\_{\alpha}\sqrt{\bm{w}^{\top}\Sigma\_{t}\bm{w}}, |  |

where qαq\_{\alpha} is an indicator depending on VaR or CVaR. For example, using the α\alpha quantile of the standard deviation zαz\_{\alpha} to relate to VaR, set qα=zαq\_{\alpha}=z\_{\alpha}, and to relate to CVaR, set qα=exp⁡(−zα2/2)(1−α)​2​πq\_{\alpha}=\frac{\exp\big(-z^{2}\_{\alpha}/2\big)}{(1-\alpha)\sqrt{2\pi}}. [bodnar2020bayesian](https://arxiv.org/html/2510.07180v1#bib.bib2)  learns weights by optimizing this objective function.

### IV-C Risk Parity Portfolio

The weights of a risk parity portfolio are given so that the risk contributions of each asset comprising the portfolio are equal [qian2006financial](https://arxiv.org/html/2510.07180v1#bib.bib14) . In this paper, we define a risk parity portfolio using the posterior predictive distribution. First, calculate the marginal risk contribution (MRC) of asset a∈[K]a\in[K] to the portfolio as

|  |  |  |
| --- | --- | --- |
|  | MRCa=12​∂Var​(R​(𝒘)∣𝒙1:(t−1),ℋ1:t)∂wa=∑b∈[K]Σa,b,t−1​wb,\displaystyle\mathrm{MRC}\_{a}=\frac{1}{2}\frac{\partial\mathrm{Var}\big(R(\bm{w})\mid\bm{x}\_{1:(t-1)},\mathcal{H}\_{1:t}\big)}{\partial w\_{a}}=\sum\_{b\in[K]}\Sigma\_{a,b,t-1}w\_{b}, |  |

where Σa,b,t−1\Sigma\_{a,b,t-1} is the variance-covariance matrix of the asset return’s posterior distribution. Then, the risk contribution (RC) is

|  |  |  |
| --- | --- | --- |
|  | RCa​(𝒘)=wa​MRCa/Var​(R​(𝒘)∣𝒙1:(t−1),ℋ1:t).\displaystyle\mathrm{RC}\_{a}(\bm{w})=w\_{a}\mathrm{MRC}\_{a}/\mathrm{Var}\big(R(\bm{w})\mid\bm{x}\_{1:(t-1)},\mathcal{H}\_{1:t}\big). |  |

A portfolio with equal risk contributions for each asset is called a risk parity portfolio. The weights 𝒘RP\bm{w}^{\mathrm{RP}} of a risk parity portfolio are obtained by solving

|  |  |  |
| --- | --- | --- |
|  | 𝒘RP∈arg​min𝒘∈ΔK​∑a∈[K]∑b∈[K](RCa​(𝒘)−RCb​(𝒘))2.\displaystyle\bm{w}^{\mathrm{RP}}\in\operatorname\*{arg\,min}\_{\bm{w}\in\Delta^{K}}\sum\_{a\in[K]}\sum\_{b\in[K]}\left(\mathrm{RC}\_{a}(\bm{w})-\mathrm{RC}\_{b}(\bm{w})\right)^{2}. |  |

## V Experiments

In this study, we construct two empirical studies in the US and Japanese markets. In each market, we use 1010 types of stocks listed in Tables [I](https://arxiv.org/html/2510.07180v1#S5.T1 "Table I ‣ V Experiments ‣ Bayesian Portfolio Optimization by Predictive Synthesis") and [II](https://arxiv.org/html/2510.07180v1#S5.T2 "Table II ‣ V Experiments ‣ Bayesian Portfolio Optimization by Predictive Synthesis").

We use the stock prices of each company from January 1, 2008, to December 31, 2019. Returns are calculated monthly. Data from 2008 to 2010 is used only for learning the parameters, and the portfolio’s performance is tested using data from 2011 to 2019. Parameter estimation continues sequentially after 2011. The reason for not using all data before 2011 is to allow the posterior distribution of BPS to converge in advance.

TABLE I: US stock data

| Company | Industry |
| --- | --- |
| Apple Inc. | Technology |
| Microsoft Corp. | Technology |
| Amazon.com Inc. | Consumer Discretionary |
| Alphabet Inc. | Communication Services |
| Berkshire Hathaway Inc. | Financials (Diversified Holdings) |
| Johnson & Johnson | Health Care |
| Walmart Inc. | Consumer Staples (Retail) |
| ExxonMobil Corp. | Energy (Oil and Gas) |
| Procter & Gamble Co. | Consumer Staples (Consumer Goods) |
| Intel Corp. | Technology (Semiconductors) |




TABLE II: Japanese stock data

| Company | Industry |
| --- | --- |
| Toyota Motor | Automotive |
| SoftBank Group | Telecommunication & IT |
| Keyence | Electronic Equipment |
| Nidec Corporation | Electrical Equipment |
| Nintendo | Entertainment |
| Tokyo Electron | Semiconductor Manufacturing Equipment |
| Fast Retailing | Retail (Apparel) |
| Tokio Marine Holdings | Insurance |
| Astellas Pharma | Pharmaceuticals |
| Seven & i Holdings | Retail (General) |

![Refer to caption](x1.png)


Figure 1: Experimental results with US stocks. The yy-axis in the figures represents the cumulative returns, while the xx-axis represents the months and years. The left figure compares the proposed method with the equally weighted portfolio (denoted as Uniform), and the right figure compares the proposed method with the results obtained using sample means and AR models to predict returns.

![Refer to caption](x2.png)


Figure 2: Experimental results with Japanese stocks. The yy-axis in the figures represents the cumulative returns, while the xx-axis represents the months and years. The left figure compares the proposed method with the equally weighted portfolio (denoted as Uniform), and the right figure compares the proposed method with the results obtained using sample means and AR models to predict returns.

### V-A Experts

In BPS, multiple predictive models for asset returns 𝑿t\bm{X}\_{t} are treated as experts, and their predictions are integrated. In this paper, 𝑿t\bm{X}\_{t} is predicted using the following methods:

* •

  The sample mean of the past 1 year (M​e​a​nt​[1]Mean\_{t}[1]).
* •

  The sample mean of the past 3 years (M​e​a​nt​[3]Mean\_{t}[3]).
* •

  An AR(1)(1) regression model using samples from the past 3 years (A​Rt​(1)AR\_{t}(1)).
* •

  An AR(2)(2) regression model using samples from the past 3 years (A​Rt​(2)AR\_{t}(2)).
* •

  An AR(3)(3) regression model using samples from the past 3 years (A​Rt​(3)AR\_{t}(3)).

### V-B Portfolio Construction Methods

In this experiment, in addition to the mean-variance portfolio, the quantile-based (VoR) portfolio, and the risk-parity portfolio mentioned above, we use an equally weighted portfolio (setting w1=⋯=wK=1Kw\_{1}=\cdots=w\_{K}=\frac{1}{K}, denoted as Uniform) to test the performance of the portfolios. Furthermore, we also investigate the results when replacing the parameters with those estimated not by the Bayesian posterior distribution but by the sample means and AR models mentioned above. The Bayesian portfolio construction method based on BPS is denoted as BPPS (Bayesian Portfolio optimization by Predictive Synthesis). The BPPS based on the mean-variance portfolio is denoted as BPPS-MV, the BPPS based on the quantile portfolio is denoted as BPPS-VoR, and the BPPS based on the risk-parity portfolio is denoted as BPPS-RP.

BPPS-MV. In BPPS-MV, we construct the mean-variance efficient portfolios and then choose a portfolio with the highest Sharpe ratio.

BPPS-VoR. In BPPS-VoR, we construct portfolios by solving the constrained problem in ([3](https://arxiv.org/html/2510.07180v1#S4.E3 "Equation 3 ‣ Portfolio Optimization. ‣ IV-B Quantile-Based Portfolio ‣ IV Bayesian Portfolio ‣ Bayesian Portfolio Optimization by Predictive Synthesis")). We set α=0.05\alpha=0.05, β=0.95\beta=0.95, and v0=−0.1v\_{0}=-0.1. The loss function is the negative of the return. We solve the constrained problem by adding the penalty for violating the constraint to the objective as max𝒘∈ΔK⁡{CVoRα,t−1​(R​(𝒘))−λ​max⁡{0,VaRβ,t−1​(L​(𝒘))−v0}}\max\_{\bm{w}\in\Delta^{K}}\big\{\mathrm{CVoR}\_{\alpha,t-1}(R(\bm{w}))-\lambda\max\big\{0,\mathrm{VaR}\_{\beta,t-1}\big(L(\bm{w})\big)-v\_{0}\big\}\big\}, where we set λ=10\lambda=10.

### V-C Experimental Results

The experiments report the cumulative returns when operating the portfolio from January 1, 2008, to December 31, 2019. It is assumed that the portfolio’s composition can be changed monthly and that there are no costs associated with these changes.

We show the results with US stocks in Figure [1](https://arxiv.org/html/2510.07180v1#S5.F1 "Figure 1 ‣ V Experiments ‣ Bayesian Portfolio Optimization by Predictive Synthesis") and those with Japanese stocks in Figure [2](https://arxiv.org/html/2510.07180v1#S5.F2 "Figure 2 ‣ V Experiments ‣ Bayesian Portfolio Optimization by Predictive Synthesis").

In each of Figure [1](https://arxiv.org/html/2510.07180v1#S5.F1 "Figure 1 ‣ V Experiments ‣ Bayesian Portfolio Optimization by Predictive Synthesis") and Figure [2](https://arxiv.org/html/2510.07180v1#S5.F2 "Figure 2 ‣ V Experiments ‣ Bayesian Portfolio Optimization by Predictive Synthesis"), the left figure compares the proposed method with the equally weighted portfolio (Uniform), while the right figure compares the proposed method with the results when using sample means and AR models to predict returns. In the right figure, a mean-variance portfolio is used when using sample means and AR models. In that case, the variance is calculated using the variance of returns from the past 3 years. For all mean-variance portfolios, the portfolio on the efficient frontier with the highest Sharpe ratio is selected.

The experimental results show that BPPS performs well overall during the evaluation period without significant drops in performance. Although BPPS-MV experiences a significant performance drop towards the end in the Japanese market, it otherwise demonstrated higher performance than existing single prediction models or performed comparably to the best model among them. It is notable that our algorithm, despite using some models with empirically poor performance, minimally feels the impact of these inferior models, indicating the robustness of the BPPS approach.

In the US market, both BPPS-MV and BPPS-VoR show good performance. Remarkably, BPPS-VoR demonstrates the best performance and maintained high stability.

Until around June 2017 in the Japanese market, the fact that BPPS does not significantly drop in returns compared to other methods suggests that the state transition of BPS functioned well. Interestingly, the performance of BPPS-MV and BPPS-VoR reverses between 2013 and 2014. Although BPPS continues to show good performance, the reversal indicates that there are state transitions that BPS cannot fully capture. Moreover, BPPS-MV shows good performance until around June 2017 but then experiences a significant drop in performance. We expect that solving these issues could further improve performance.

At least according to our results, BPPS-VoR is consistently showing high performance. We believe that using Bayesian algorithms to assess quantiles in the posterior distribution is well-suited for portfolio optimization. Thus, our proposed BPS-based algorithm not only provides practical performance but also offers academic insights.

## VI Conclusion

This study introduced a method for optimizing portfolios based on the posterior predictive distribution obtained through BPS to address the uncertainty of the asset return distribution in portfolio optimization. By integrating the multiple experts’ predictions of asset returns using dynamic linear models, we constructed predictive distributions that capture the uncertainty of time series data. Then, we developed mean-variance portfolios, quantile-based portfolios, and risk-parity portfolios utilizing the posterior predictive distribution. Through experiments using stock price data, we confirmed the effectiveness of the methods tested in this paper.

## References

* [1]

  Knut Are Aastveit, Francesco Ravazzolo, and Herman K Van Dijk.
  Combined density nowcasting in an uncertain economic environment.
  Journal of Business & Economic Statistics, 36(1):131–145,
  2018.
* [2]

  Taras Bodnar, Mathias Lindholm, Vilhelm Niklasson, and Erik ThorsÃ©n.
  Bayesian quantile-based portfolio selection, 2020.
* [3]

  Taras Bodnar, Mathias Lindholm, Erik Thorsén, and Joanna Tyrcha.
  Quantile-based optimal portfolio selection.
  Computational Management Science, 18(3):299–324, Jul 2021.
* [4]

  Vijay Chopra and William Ziemba.
  The effect of errors in means, variances, and covariances on optimal
  portfolio choice.
  Journal of Portfolio Management, 19:6–11, 12 1993.
* [5]

  Nestor Parolya David Bauder, Taras Bodnar and Wolfgang Schmid.
  Bayesian meanâvariance analysis: optimal portfolio
  selection under parameter uncertainty.
  Quantitative Finance, 21(2):221–242, 2021.
* [6]

  John Geweke and Gianni Amisano.
  Optimal prediction pools.
  Journal of Econometrics, 164(1):130–141, 2011.
* [7]

  Jennifer A Hoeting, David Madigan, Adrian E Raftery, and Chris T Volinsky.
  Bayesian model averaging: a tutorial.
  Statistical science, pages 382–401, 1999.
* [8]

  Harry Markowitz.
  Portfolio selection.
  The Journal of Finance, 1952.
* [9]

  Harry Markowitz.
  Portfolio selection: efficient diversification of investments.
  Yale university press, 1959.
* [10]

  Harry M Markowitz and G Peter Todd.
  Mean-Variance Analysis in Portfolio Choice and Capital Markets,
  volume 66.
  John Wiley & Sons, 2000.
* [11]

  Kenichiro McAlinn, Knut Are Aastveit, Jouchi Nakajima, and Mike West.
  Multivariate bayesian predictive synthesis in macroeconomic
  forecasting.
  Journal of the American Statistical Association,
  115(531):1092–1110, 2020.
* [12]

  Kenichiro McAlinn and Mike West.
  Dynamic bayesian predictive synthesis in time series forecasting.
  Journal of econometrics, 210(1):155–169, 2019.
* [13]

  R. Prado and M. West.
  Time Series: Modelling, Computation & Inference.
  Chapman & Hall/CRC Press, 2010.
* [14]

  Edward E Qian.
  On the financial interpretation of risk contribution: Risk budgets do
  add up.
  Journal of Investment Management, 2006.
* [15]

  R. Tyrrell Rockafellar and Stanislav Uryasev.
  Optimization of conditional value-at risk.
  Journal of Risk, 3:21–41, 2000.
* [16]

  R.Tyrrell Rockafellar and Stanislav Uryasev.
  Conditional value-at-risk for general loss distributions.
  Journal of Banking & Finance, 26(7):1443–1471, 2002.
* [17]

  Emily Tallman and Mike West.
  Bayesian predictive decision synthesis, 2023.
* [18]

  M. West and P. J. Harrison.
  Bayesian Forecasting & Dynamic Models.
  Springer Verlag, 2nd edition, 1997.