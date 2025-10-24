---
authors:
- Semere Gebresilassie
- Mulue Gebreslasie
- Minglian Lin
doc_id: arxiv:2510.20047v1
family_id: arxiv:2510.20047
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Multivariate Variance Swap Using Generalized Variance Method for Stochastic
  Volatility models
url_abs: http://arxiv.org/abs/2510.20047v1
url_html: https://arxiv.org/html/2510.20047v1
venue: arXiv q-fin
version: 1
year: 2025
---


Semere Gebresilassie 111Department of Computing and Data Science, Wentworth Institute of Technology, Email: habtemicaels@wit.edu,  Mulue Gebreslasie 222Department of Mathematics, North Dakota State University, Email: mulue.gebreslasie@ndsu.edu,  Minglian Lin 333Department of Mathematical Sciences, The University of Texas at El Paso, El Paso, Texas 79968, USA, Email: mlin2@utep.edu

(October 22, 2025)

###### Abstract

This paper develops a novel framework for modeling the variance swap of multi-asset portfolios by employing the generalized variance approach, which utilizes the determinant of the covariance matrix of the underlying assets. By specifying the distribution of the log returns of the underlying assets under the Heston and Barndorff-Nielsen and Shephard (BNS) stochastic volatility frameworks, we derive closed-form solutions for the realized variance through the computation of the covariance generalization of multi-assets. To evaluate the robustness of the proposed model, we conduct simulations using nine different assets generated via the quantmod package. For a three-asset portfolio, analytical expressions for the multivariate variance swap are obtained under both the Heston and BNS models. Numerical experiments further demonstrate the effectiveness of the proposed model through parameter testing, calibration, and validation.

Keywords: Multivariate swap, Lévy process, Generalized variance method, Heston model, Barndorff-Nielsen and Shephard model.

## 1 Introduction

A financial security is a financial contract whose value at maturity is determined by the price process of the underlying asset. A derivative is a financial security whose value/price is derived from one or more underlying assets. There are four types of derivatives: options, forwards, futures and swaps. A swap is a financial derivative in which two counter parties agree to trade future cash flows, with the size of the cash flow decided at the start of the deal.
  
Understanding the movement of a market is critical in the financial sector in order to correctly hedge and speculate on the underlying asset. Volatility and variance swaps are forward contracts on realized volatility and variance of the underlying stock respectively. In a stock market volatility and variance of stock are good indicators for many reasons such as the future fluctuation of the stock price. Investors or traders have an insight on future fluctuation of the stock price. Therefore, volatility and variance swaps provide investors with tools to hedge against or speculate on fluctuations in stock price volatility.
  
  
Most of the literature has focused on pricing volatility and variance swaps for a single asset, with several studies conducted in this area under various stochastic volatility models. The classical [[6](https://arxiv.org/html/2510.20047v1#bib.bib6)] formula assumed the volatility of a stock is constant. However, such an assumptions for financial model is not consistent for pricing financial derivatives in a stock market. To address this limitation, the stochastic volatility framework was introduced and has been further refined by financial researchers to reduce model risk and improve pricing accuracy. In [[20](https://arxiv.org/html/2510.20047v1#bib.bib20)], a new probabilistic approach using the Heston model was proposed to study volatility, variance, covariance and correlation swaps for financial markets. The impact of discrete sampling on the valuation of options on realized variance in the Heston model is investigated in [[19](https://arxiv.org/html/2510.20047v1#bib.bib19)], which establishes analytical methodology for pricing and hedging options on realized variance in the Heston model supplemented with jumps in asset returns and variance. [[16](https://arxiv.org/html/2510.20047v1#bib.bib16)] studied variance and volatility swap, and introduced the pricing strategies for some popular models (like Black-Scholes model, Merton jump diffusion model, Heston model, 3/2 model, and GARCH models). They have estimated the various parameters in the models using option-based or price-based approach, and concluded that Black-Scholes model, Merton jump diffusion, and GARCH models didn’t perform well for pricing variance and volatility swap. In some diffusion based models the volatility is driven by a Brownian motion, which can be correlated with the underlying asset; such models account the different ”stylized facts”. Non-Gaussian processes of Ornstein-Uhlenbeck (OU) type offer the possibility of capturing important distribution deviations from Gaussianity and for flexible modeling of dependence structure [[1](https://arxiv.org/html/2510.20047v1#bib.bib1), [2](https://arxiv.org/html/2510.20047v1#bib.bib2)]. The non-Gaussian OU stochastic volatility model was used by [[3](https://arxiv.org/html/2510.20047v1#bib.bib3)] to study volatility and variance swaps. [[9](https://arxiv.org/html/2510.20047v1#bib.bib9)] developed analytical solution for pricing volatility and variance swaps for Barndorff-Nielsen and Shephard (BNS) process driven financial markets. [[8](https://arxiv.org/html/2510.20047v1#bib.bib8)] modeled variance and volatility swap using the superposition of BNS type model. Analytical formulas for the arbitrage free prices for the weighted variance and weighted volatility swap is conducted by [[13](https://arxiv.org/html/2510.20047v1#bib.bib13)] under the frame work of the BNS type stochastic volatility model. All the aforementioned authors focused on pricing volatility and variance swaps for a single underlying asset. However, in today’s complex financial transaction’s investors often diversify their portfolios accross multiple assets to minimize the risk of the unobserved financial crisis. This motivates the development of multivariate variance swap, which allow contracts to be based on the joint behavior of two or more assets. [[4](https://arxiv.org/html/2510.20047v1#bib.bib4)] and [[5](https://arxiv.org/html/2510.20047v1#bib.bib5)] proposed methods for pricing generalized variance swap in financial markets with Markov-modulated volatilities and in the multi-asset setting using the Barndorff–Nielsen and Shephard (BNS) model. Their approach utilized the trace and maximum Eigenvalue of the asset return covariance matrix as measures of portfolio variability. The authors concluded that the maximum eigenvalue provides a more informative measure than the trace based swap, as it not only captures the variances but also incorporates the covariances among asset returns. In our study, we adopt the same multi-asset stochastic volatility framework, although various studies such as [[14](https://arxiv.org/html/2510.20047v1#bib.bib14), [15](https://arxiv.org/html/2510.20047v1#bib.bib15)] propose alternative formulations based on Lévy-driven asset dynamics.
  
  
The Generalized Variance of n-dimensional random vector variable XX is defined as the determinant of its variance-covariance matrix introduced by [[22](https://arxiv.org/html/2510.20047v1#bib.bib22)]. [[11](https://arxiv.org/html/2510.20047v1#bib.bib11)] proposed the generalized variance metric to measure the composite multivariate degree of inequality (dispersion)
of any multidimensional cloud. This research proposal focuses on formulating the multiasset stochastic volatility dynamics under both the Heston and Barndorff–Nielsen–Shephard (BNS) models. We define the generalized variance method based on the covariance structure of asset returns and propose a method to price the multivariate variance swap accordingly. Although the framework is applicable to any nn asset portfolio, we illustrate our approach using a subset of 9 selected stocks, grouped into three portfolios of 3 assets each, to highlight how pricing varies across different asset combinations.
  
  
The rest of the paper is organized as follows. In Section [2](https://arxiv.org/html/2510.20047v1#S2 "2 Variance swap and the portfolio return covariance matrix ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models"), we provide a brief overview of the variance swap, the multivariate variance swap, and the portfolio return covariance matrix. In sections [3](https://arxiv.org/html/2510.20047v1#S3 "3 Multivariate variance swap for Heston model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models") and [4](https://arxiv.org/html/2510.20047v1#S4 "4 Multivariate swap for Barndorff-Nielsen and Shephard model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models"), we derive the multivariate variance swap for the multi-asset dynamics of Heston model and BNS model respectively. In Section [5](https://arxiv.org/html/2510.20047v1#S5 "5 Model Fitting and Parameter Estimation ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models"), we provide the numerical results of the model fitting and parameter estimation for multivariate variance swap. Figures, tables, and correlation matrix are discussed under this section. Finally, a brief conclusion is provided in Section [6](https://arxiv.org/html/2510.20047v1#S6 "6 Conclusion ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models"), and some additional derivations are included in the Appendix.

## 2 Variance swap and the portfolio return covariance matrix

###### Definition 2.1.

A *variance swap* is a forward contract on the future realized variance of an underlying asset.

The payoff at expiration TT is

|  |  |  |
| --- | --- | --- |
|  | N​(σR2−Kvar),N(\sigma\_{R}^{2}-K\_{\text{var}}), |  |

where NN is the notional amount, σR2\sigma\_{R}^{2} is the realized variance, and KvarK\_{\text{var}} is the variance strike price.
Calculating realized variance in discrete and continuous time have the following formulas:

* •

  In discrete time,

  |  |  |  |
  | --- | --- | --- |
  |  | σRd2=nT​(n−1)​∑i=1n(Ri−R¯)2,\sigma^{2}\_{R\_{d}}=\frac{n}{T(n-1)}\sum\_{i=1}^{n}\left(R\_{i}-\bar{R}\right)^{2}, |  |

  where
  Ri=log⁡(Si+1Si)R\_{i}=\log\big(\frac{S\_{i+1}}{S\_{i}}\big), R¯\bar{R} is mean of the log returns,
  nn is the number of log return observations,
  SiS\_{i} is the price of the underlying asset at time tit\_{i},
  and nT\frac{n}{T} is the annualization factor if the maturity TT is assumed in years.
* •

  In continuous time,

  |  |  |  |
  | --- | --- | --- |
  |  | σRc2=limn→∞nT​(n−1)​∑i=1n(log⁡(Si+1Si))2=1T​∫0Tσt2​𝑑t,\sigma^{2}\_{R\_{c}}=\lim\_{n\to\infty}\frac{n}{T(n-1)}\sum\_{i=1}^{n}\left(\log\left(\frac{S\_{i+1}}{S\_{i}}\right)\right)^{2}=\frac{1}{T}\int\_{0}^{T}\sigma^{2}\_{t}dt, |  |

    

  where σt2\sigma^{2}\_{t} is the variance over an infinitesimal time period tt.

###### Definition 2.2.

A *multivariate variance swap* is a forward contract on the future realized variance of a portfolio consisting of multiple underlying assets.

To price the multivariate variance swap, we need to construct the covariance matrix of the returns (i.e portofolio return covariance matrix). Assume that r1,r2,r3,…,rnr\_{1},r\_{2},r\_{3},...,r\_{n} be the dynamics of the log returns of the given stochastic volatility model. Hence, the portfolio return covariance matrix is given by

|  |  |  |
| --- | --- | --- |
|  | Σ=(Var​(r1)Cov​(r1,r2)⋯Cov​(r1,rn)Cov​(r2,r1)Var​(r2)⋯Cov​(r2,rn)⋮⋮⋱⋮Cov​(rn,r1)Cov​(rn,r2)⋯Var​(rn)).\Sigma=\begin{pmatrix}\text{Var}\left(r\_{1}\right)&\text{Cov}\left(r\_{1},r\_{2}\right)&\cdots&\text{Cov}\left(r\_{1},r\_{n}\right)\\ \text{Cov}\left(r\_{2},r\_{1}\right)&\text{Var}\left(r\_{2}\right)&\cdots&\text{Cov}\left(r\_{2},r\_{n}\right)\\ \vdots&\vdots&\ddots&\vdots\\ \text{Cov}\left(r\_{n},r\_{1}\right)&\text{Cov}\left(r\_{n},r\_{2}\right)&\cdots&\text{Var}\left(r\_{n}\right)\end{pmatrix}. |  |

The instantaneous variance of the multi-asset dynamics is given by the determinant of the covariance matrix of the log-returns dynamics. Hence, to price a multivariate variance swap using the generalized variance method, we compute the determinant Σ\Sigma (i.e., |Σ||\Sigma|) to obtain the instantaneous variance of the portfolio return.
The price Pv​a​rP\_{var} of a multivariate variance swap with strike price KvarK\_{\text{var}} is

|  |  |  |
| --- | --- | --- |
|  | Pv​a​r=𝔼⁡[e−r​T​(σR2−Kvar)],P\_{var}=\operatorname{\mathbb{E}}\left[e^{-rT}\left(\sigma\_{R}^{2}-K\_{\text{var}}\right)\right], |  |

where

|  |  |  |
| --- | --- | --- |
|  | σR2=1T​∫0T|Σ|​𝑑t.\sigma\_{R}^{2}=\frac{1}{T}\int\_{0}^{T}|\Sigma|\,dt. |  |

## 3 Multivariate variance swap for Heston model

In this section, we introduce the multivariate Heston model and derive the corresponding expression for the variance swap using the generalized variance approach.
We assume that the price process of nn assets, denoted by
St=(St1,St2,…,Stn),S\_{t}=(S\_{t}^{1},S\_{t}^{2},\ldots,S\_{t}^{n}),
follows a multivariate extension of the Heston stochastic volatility model.
This framework allows us to capture both the individual dynamics of each asset and the correlation structure among their volatilities.
The formal formulation of the multivariate Heston model and the corresponding multivariate variance swap is presented below.

### 3.1 Multivariate Heston model

Let (Ω,ℱ,{ℱt},P)(\Omega,\mathcal{F},\{\mathcal{F}\_{t}\},P) be a probability space with filtration ℱt\mathcal{F}\_{t}, t∈[0,T]t\in[0,T]. [[20](https://arxiv.org/html/2510.20047v1#bib.bib20)] assumes that the underlying asset StS\_{t} operates in a risk-neutral world, with the following dynamics:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​StSt=rt​d​t+σt​d​Bt,d​σt2=k​(θ2−σt2)​d​t+γ​σt​d​Wt,σ02>0,\begin{split}\frac{dS\_{t}}{S\_{t}}&=r\_{t}dt+\sigma\_{t}dB\_{t},\\ d\sigma\_{t}^{2}&=k(\theta^{2}-\sigma\_{t}^{2})dt+\gamma\sigma\_{t}dW\_{t},\quad\sigma\_{0}^{2}>0,\end{split} |  | (3.1) |

where rtr\_{t} is a deterministic interest rate, σ0\sigma\_{0} and θ\theta are the initial and long-term volatilities, k>0k>0 is the reversion speed, γ>0\gamma>0 is the volatility of volatility, and BtB\_{t} and WtW\_{t} are independent standard Wiener processes.
  
  
The variance σt2\sigma\_{t}^{2} follows a Cox-Ingersoll-Ross process, as shown in the second part of equation ([3.1](https://arxiv.org/html/2510.20047v1#S3.E1 "In 3.1 Multivariate Heston model ‣ 3 Multivariate variance swap for Heston model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")). The change-of-time method is discussed in [[12](https://arxiv.org/html/2510.20047v1#bib.bib12)] and [[20](https://arxiv.org/html/2510.20047v1#bib.bib20)] applied the change-of-time method to solve this process, and its solution for σt2\sigma\_{t}^{2} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | σt2=e−k​t​(σ02−θ2+W~​(ϕt−1))+θ2.\sigma\_{t}^{2}=e^{-kt}\left(\sigma\_{0}^{2}-\theta^{2}+\tilde{W}(\phi^{-1}\_{t})\right)+\theta^{2}. |  | (3.2) |

[[20](https://arxiv.org/html/2510.20047v1#bib.bib20)] state that W~​(t)\tilde{W}(t) is an ℱt\mathcal{F}\_{t}-measurable one-dimensional Wiener process, and ϕt−1\phi^{-1}\_{t} is the inverse function of ϕt\phi\_{t}, where

|  |  |  |
| --- | --- | --- |
|  | ϕt=γ−1​∫0t{eκ​ϕs​(σ02−θ02+W~​(t)+θ2​e2​κ​ϕs)}−1​𝑑s\phi\_{t}=\gamma^{-1}\int^{t}\_{0}\{e^{\kappa\phi\_{s}}(\sigma^{2}\_{0}-\theta^{2}\_{0}+\tilde{W}(t)+\theta^{2}e^{2\kappa\phi\_{s}})\}^{-1}ds |  |

such that W~​(ϕt−1)\tilde{W}(\phi^{-1}\_{t}) is a random process with

|  |  |  |
| --- | --- | --- |
|  | 𝔼⁡[W~​(ϕt−1)]=0.\operatorname{\mathbb{E}}[\tilde{W}(\phi^{-1}\_{t})]=0. |  |

Thus from equation([3.2](https://arxiv.org/html/2510.20047v1#S3.E2 "In 3.1 Multivariate Heston model ‣ 3 Multivariate variance swap for Heston model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")) we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼⁡[σt2]=e−k​t​(σ02−θ2)+θ2.\operatorname{\mathbb{E}}[\sigma\_{t}^{2}]=e^{-kt}(\sigma\_{0}^{2}-\theta^{2})+\theta^{2}. |  | (3.3) |

  

For nn stock price processes StiS^{i}\_{t}, where i=1,2,3,…,ni=1,2,3,\dots,n, the multiple stock following Heston model is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​StiSti=μti​d​t+σti​d​Bti,d​(σi)t2=ki​(θi2−(σi)t2)​d​t+γi​σti​d​Wti,(σi)02>0,\begin{split}\frac{dS^{i}\_{t}}{S^{i}\_{t}}&=\mu^{i}\_{t}dt+\sigma^{i}\_{t}dB^{i}\_{t},\\ d(\sigma^{i})^{2}\_{t}&=k\_{i}(\theta\_{i}^{2}-(\sigma^{i})^{2}\_{t})dt+\gamma\_{i}\sigma^{i}\_{t}dW^{i}\_{t},\quad(\sigma^{i})^{2}\_{0}>0,\end{split} |  | (3.4) |

where, for i=1,2,3,…,ni=1,2,3,...,n, μti\mu^{i}\_{t} is a deterministic function, and ki,θi,γi>0k\_{i},\theta\_{i},\gamma\_{i}>0 are the reversion speed, long-term volatility, and volatility of volatility, respectively. The correlation of the stock prices is
[Btl,Btm]=cl​m​(t)​d​t,[B^{l}\_{t},B^{m}\_{t}]=c\_{lm}(t)\,dt,
where cl​m​(t)c\_{lm}(t) is a deterministic function of time t for l,m∈{1,2,3,…,n}l,m\in\{1,2,3,...,n\}. At fixed time tt, cl​m​(t)c\_{lm}(t) can be calculated using stock price data and be regarded as a constant cl​mc\_{lm}. The wiener processes WtiW^{i}\_{t} in the squared volatility process are independent of each other for i=1,2,3,…,ni=1,2,3,...,n, and BtiB^{i}\_{t} are independent of WtiW^{i}\_{t}.

### 3.2 Multivariate variance swap using generalized variance method for Heston model

For simplicity, we begin by working with three stocks and then generalize the results to nn stocks, assuming that the stocks follow the Heston model. The 3×33\times 3 portfolio return covariance matrix for the Heston model equation ([3.4](https://arxiv.org/html/2510.20047v1#S3.E4 "In 3.1 Multivariate Heston model ‣ 3 Multivariate variance swap for Heston model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ1=((σ1)t2c12​σt1​σt2c13​σt1​σt3c21​σt2​σt1(σ2)t2c23​σt2​σt3c31​σt3​σt1c32​σt3​σt2(σ3)t2).\displaystyle\Sigma\_{1}=\begin{pmatrix}(\sigma^{1})\_{t}^{2}&c\_{12}\sigma^{1}\_{t}\sigma^{2}\_{t}&c\_{13}\sigma^{1}\_{t}\sigma^{3}\_{t}\\ c\_{21}\sigma^{2}\_{t}\sigma^{1}\_{t}&(\sigma^{2})\_{t}^{2}&c\_{23}\sigma^{2}\_{t}\sigma^{3}\_{t}\\ c\_{31}\sigma^{3}\_{t}\sigma^{1}\_{t}&c\_{32}\sigma^{3}\_{t}\sigma^{2}\_{t}&(\sigma^{3})\_{t}^{2}\end{pmatrix}. |  | (3.5) |

Now, we need to compute σR2\sigma^{2}\_{R}, where σR2\sigma^{2}\_{R} denotes the realized variance computed from the determinant of the portfolio covariance matrix Σ1\Sigma\_{1}. It is defined as the average of the instantaneous variance in the period [0,T], which is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | σR2=1T​∫0T|Σ1|​𝑑t.\sigma\_{R}^{2}=\frac{1}{T}\int^{T}\_{0}|\Sigma\_{1}|dt. |  | (3.6) |

  

In Appendix [A](https://arxiv.org/html/2510.20047v1#A1 "Appendix A Appendix: Calculations of |Σ₁| and |Σ₂| ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models"), we obtain the determinant of ([3.5](https://arxiv.org/html/2510.20047v1#S3.E5 "In 3.2 Multivariate variance swap using generalized variance method for Heston model ‣ 3 Multivariate variance swap for Heston model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")) as below

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Σ1|=|C|​∏i=13(σti)2,\displaystyle|\Sigma\_{1}|=|C|\prod\_{i=1}^{3}(\sigma^{i}\_{t})^{2}, |  | (3.7) |

where C=(cl​m)1≤l,m≤3C=(c\_{lm})\_{1\leq l,m\leq 3} is the correlation matrix of stock prices calculated by the stock price data.
By the independence of (σti)2(\sigma^{i}\_{t})^{2}, i=1,2,3i=1,2,3, we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼⁡[|Σ1|]=|C|​∏i=13𝔼⁡[(σti)2].\displaystyle\operatorname{\mathbb{E}}[|\Sigma\_{1}|]=|C|\prod\_{i=1}^{3}\operatorname{\mathbb{E}}[(\sigma^{i}\_{t})^{2}]. |  | (3.8) |

We notice that the 3-dimensional case of ([3.3](https://arxiv.org/html/2510.20047v1#S3.E3 "In 3.1 Multivariate Heston model ‣ 3 Multivariate variance swap for Heston model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")) is

|  |  |  |
| --- | --- | --- |
|  | 𝔼⁡[(σti)2]=e−ki​t​((σ0i)2−θi2)+θi2,i=1,2,3.\displaystyle\operatorname{\mathbb{E}}[(\sigma^{i}\_{t})^{2}]=e^{-k\_{i}t}\big((\sigma^{i}\_{0})^{2}-\theta\_{i}^{2}\big)+\theta\_{i}^{2},\quad i=1,2,3. |  |

Using the above equation, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∏i=13𝔼⁡[(σti)2]\displaystyle\prod\_{i=1}^{3}\operatorname{\mathbb{E}}[(\sigma^{i}\_{t})^{2}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle=\ | e−(k3+k2+k1)​t​((σ03)2−θ32)​((σ02)2−θ22)​((σ01)2−θ12)+e−(k3+k2)​t​((σ03)2−θ32)​((σ02)2−θ22)​θ12\displaystyle e^{-(k\_{3}+k\_{2}+k\_{1})t}\big((\sigma^{3}\_{0})^{2}-\theta\_{3}^{2}\big)\big((\sigma^{2}\_{0})^{2}-\theta\_{2}^{2}\big)\big((\sigma^{1}\_{0})^{2}-\theta\_{1}^{2}\big)+e^{-(k\_{3}+k\_{2})t}\big((\sigma^{3}\_{0})^{2}-\theta\_{3}^{2}\big)\big((\sigma^{2}\_{0})^{2}-\theta\_{2}^{2}\big)\theta\_{1}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +e−(k3+k1)​t​((σ03)2−θ32)​((σ01)2−θ12)​θ22+e−(k2+k1)​t​((σ02)2−θ22)​((σ01)2−θ12)​θ32\displaystyle+e^{-(k\_{3}+k\_{1})t}\big((\sigma^{3}\_{0})^{2}-\theta\_{3}^{2}\big)\big((\sigma^{1}\_{0})^{2}-\theta\_{1}^{2}\big)\theta\_{2}^{2}+e^{-(k\_{2}+k\_{1})t}\big((\sigma^{2}\_{0})^{2}-\theta\_{2}^{2}\big)\big((\sigma^{1}\_{0})^{2}-\theta\_{1}^{2}\big)\theta\_{3}^{2} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +e−k3​t​((σ03)2−θ32)​θ22​θ12+e−k2​t​((σ02)2−θ22)​θ32​θ12+e−k1​t​((σ01)2−θ12)​θ32​θ22+θ32​θ22​θ12.\displaystyle+e^{-k\_{3}t}\big((\sigma^{3}\_{0})^{2}-\theta\_{3}^{2}\big)\theta\_{2}^{2}\theta\_{1}^{2}+e^{-k\_{2}t}\big((\sigma^{2}\_{0})^{2}-\theta\_{2}^{2}\big)\theta\_{3}^{2}\theta\_{1}^{2}+e^{-k\_{1}t}\big((\sigma^{1}\_{0})^{2}-\theta\_{1}^{2}\big)\theta\_{3}^{2}\theta\_{2}^{2}+\theta\_{3}^{2}\theta\_{2}^{2}\theta\_{1}^{2}. |  | (3.9) |

###### Theorem 3.1.

The arbitrage free price of the multivariate variance swap for St1,St2,S^{1}\_{t},S^{2}\_{t}, and St3S^{3}\_{t}, assuming they follow the Heston model and using the generalized variance method, is given by:

|  |  |  |
| --- | --- | --- |
|  | Pv​a​r=e−r​T​𝔼⁡[σR2]−e−r​T​Kvar.P\_{var}=e^{-rT}\operatorname{\mathbb{E}}[\sigma\_{R}^{2}]-e^{-rT}K\_{\text{var}}. |  |

###### Proof.

The expected value of equation ([3.6](https://arxiv.org/html/2510.20047v1#S3.E6 "In 3.2 Multivariate variance swap using generalized variance method for Heston model ‣ 3 Multivariate variance swap for Heston model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")) applying equations ([3.8](https://arxiv.org/html/2510.20047v1#S3.E8 "In 3.2 Multivariate variance swap using generalized variance method for Heston model ‣ 3 Multivariate variance swap for Heston model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")) and ([3.9](https://arxiv.org/html/2510.20047v1#S3.E9 "In 3.2 Multivariate variance swap using generalized variance method for Heston model ‣ 3 Multivariate variance swap for Heston model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")) gives that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼⁡[σR2]\displaystyle\operatorname{\mathbb{E}}[\sigma\_{R}^{2}] | =1T​∫0T𝔼⁡[|Σ1|]​𝑑t\displaystyle=\frac{1}{T}\int^{T}\_{0}\operatorname{\mathbb{E}}[|\Sigma\_{1}|]dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =|C|T[(1−e−(k3+k2+k1)​Tk3+k2+k1)((σ03)2−θ32)((σ02)2−θ22)((σ01)2−θ12)\displaystyle=\frac{|C|}{T}\bigg[\Big(1-\frac{e^{-(k\_{3}+k\_{2}+k\_{1})T}}{k\_{3}+k\_{2}+k\_{1}}\Big)\big((\sigma^{3}\_{0})^{2}-\theta\_{3}^{2}\big)\big((\sigma^{2}\_{0})^{2}-\theta\_{2}^{2}\big)\big((\sigma^{1}\_{0})^{2}-\theta\_{1}^{2}\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−e−(k3+k2)​Tk3+k2)​((σ03)2−θ32)​((σ02)2−θ22)​θ12\displaystyle\qquad\quad+\Big(1-\frac{e^{-(k\_{3}+k\_{2})T}}{k\_{3}+k\_{2}}\Big)\big((\sigma^{3}\_{0})^{2}-\theta\_{3}^{2}\big)\big((\sigma^{2}\_{0})^{2}-\theta\_{2}^{2}\big)\theta\_{1}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−e−(k3+k1)​Tk3+k1)​((σ03)2−θ32)​((σ01)2−θ12)​θ22\displaystyle\qquad\quad+\Big(1-\frac{e^{-(k\_{3}+k\_{1})T}}{k\_{3}+k\_{1}}\Big)\big((\sigma^{3}\_{0})^{2}-\theta\_{3}^{2}\big)\big((\sigma^{1}\_{0})^{2}-\theta\_{1}^{2}\big)\theta\_{2}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−e−(k2+k1)​Tk2+k1)​((σ02)2−θ22)​((σ01)2−θ12)​θ32\displaystyle\qquad\quad+\Big(1-\frac{e^{-(k\_{2}+k\_{1})T}}{k\_{2}+k\_{1}}\Big)\big((\sigma^{2}\_{0})^{2}-\theta\_{2}^{2}\big)\big((\sigma^{1}\_{0})^{2}-\theta\_{1}^{2}\big)\theta\_{3}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +(1−e−k3​Tk3)​((σ03)2−θ32)​θ22​θ12+(1−e−k2​Tk2)​((σ02)2−θ22)​θ32​θ12\displaystyle\qquad\quad+\Big(1-\frac{e^{-k\_{3}T}}{k\_{3}}\Big)\big((\sigma^{3}\_{0})^{2}-\theta\_{3}^{2}\big)\theta\_{2}^{2}\theta\_{1}^{2}+\Big(1-\frac{e^{-k\_{2}T}}{k\_{2}}\Big)\big((\sigma^{2}\_{0})^{2}-\theta\_{2}^{2}\big)\theta\_{3}^{2}\theta\_{1}^{2} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +(1−e−k1​Tk1)((σ01)2−θ12)θ32θ22+Tθ32θ22θ12].\displaystyle\qquad\quad+\Big(1-\frac{e^{-k\_{1}T}}{k\_{1}}\Big)\big((\sigma^{1}\_{0})^{2}-\theta\_{1}^{2}\big)\theta\_{3}^{2}\theta\_{2}^{2}+T\theta\_{3}^{2}\theta\_{2}^{2}\theta\_{1}^{2}\bigg]. |  | (3.10) |

So the theorem uses equation ([3.10](https://arxiv.org/html/2510.20047v1#S3.E10 "In 3.2 Multivariate variance swap using generalized variance method for Heston model ‣ 3 Multivariate variance swap for Heston model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")) to complete the proof.
∎

## 4 Multivariate swap for Barndorff-Nielsen and Shephard model

In this section, we introduce the multi-asset Barndorff-Nielsen and Shephard (BNS) model and derive its variance swap using the generalized variance method. The BNS framework is particularly well suited for capturing discontinuities in asset prices through its incorporation of jumps in the volatility process. By extending the model to a multi-asset setting, we account for both individual stock dynamics and shared jump risk across assets. The generalized variance approach, based on the determinant of the return covariance matrix, provides a tractable means of quantifying instantaneous portfolio variance under the BNS dynamics. The formal structure and derivation of the variance swap under this model are outlined below.

### 4.1 Multivariate BNS model

Consider a financial market with a risk-free asset yielding a constant return rate rr and two stocks traded up to a fixed exercise date TT. Barndorff-Nielsen and Shephard [[2](https://arxiv.org/html/2510.20047v1#bib.bib2)] [[1](https://arxiv.org/html/2510.20047v1#bib.bib1)] modeled the stock price process S={St}t≥0S=\{S\_{t}\}\_{t\geq 0} on a filtered probability space (Ω,ℱ,{ℱt}0≤t≤T,P)(\Omega,\mathcal{F},\{\mathcal{F}\_{t}\}\_{0\leq t\leq T},P), carrying a standard Brownian motion WtW\_{t} and an independent, positive, non-decreasing Lévy process Zλ​tZ\_{\lambda t}. The dynamics are

|  |  |  |  |
| --- | --- | --- | --- |
|  | St\displaystyle S\_{t} | =S0​eXt,\displaystyle=S\_{0}e^{X\_{t}}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Xt\displaystyle dX\_{t} | =(μ+β​σt2)​d​t+σt​d​Wt+ρ​d​Zλ​t,\displaystyle=(\mu+\beta\sigma\_{t}^{2})dt+\sigma\_{t}dW\_{t}+\rho dZ\_{\lambda t}, |  | (4.1) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​σt2\displaystyle d\sigma\_{t}^{2} | =−λ​σt2​d​t+d​Zλ​t,σ02>0,\displaystyle=-\lambda\sigma\_{t}^{2}dt+dZ\_{\lambda t},\quad\sigma\_{0}^{2}>0, |  | (4.2) |

where μ,β,ρ,λ∈ℝ\mu,\beta,\rho,\lambda\in\mathbb{R}, λ>0\lambda>0, and ρ≤0\rho\leq 0 represents the leverage effect. The process ZtZ\_{t} is a subordinator (a Lévy process with non-decreasing paths and no Gaussian component), referred to as the background driving Lévy process (BDLP). The filtration ℱt\mathcal{F}\_{t} is the augmentation of the filtration generated by (W,Z)(W,Z).
  
  
Non-Gaussian Ornstein-Uhlenbeck processes, driven by subordinators, can model properties such as heavy-tailed log-returns, aggregational Gaussianity, and volatility clustering [[2](https://arxiv.org/html/2510.20047v1#bib.bib2)].
Following [[17](https://arxiv.org/html/2510.20047v1#bib.bib17)], the BDLP ZZ satisfies

* •

  ZZ has no deterministic drift, and its Lévy measure has density w​(x)w(x). The cumulant transform is:

  |  |  |  |
  | --- | --- | --- |
  |  | κ​(θ)=log⁡𝔼⁡[eθ​Z1]=∫ℝ+(eθ​x−1)​w​(x)​𝑑x,\kappa(\theta)=\log\operatorname{\mathbb{E}}[e^{\theta Z\_{1}}]=\int\_{\mathbb{R}\_{+}}(e^{\theta x}-1)w(x)\,dx, |  |

  where it exists.
* •

  Let θ^=sup{θ∈ℝ:κ​(θ)<+∞}\hat{\theta}=\sup\{\theta\in\mathbb{R}:\kappa(\theta)<+\infty\}, then θ^>0\hat{\theta}>0.
* •

  limθ→θ^κ​(θ)=+∞\lim\_{\theta\to\hat{\theta}}\kappa(\theta)=+\infty.

  

Under an equivalent martingale measure (EMM), as in [[17](https://arxiv.org/html/2510.20047v1#bib.bib17)] and [[10](https://arxiv.org/html/2510.20047v1#bib.bib10)], the dynamics ([4.1](https://arxiv.org/html/2510.20047v1#S4.E1 "In 4.1 Multivariate BNS model ‣ 4 Multivariate swap for Barndorff-Nielsen and Shephard model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")) and ([4.2](https://arxiv.org/html/2510.20047v1#S4.E2 "In 4.1 Multivariate BNS model ‣ 4 Multivariate swap for Barndorff-Nielsen and Shephard model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")) become:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Xt\displaystyle dX\_{t} | =bt​d​t+σt​d​Wt+ρ​d​Zλ​t,\displaystyle=b\_{t}dt+\sigma\_{t}dW\_{t}+\rho dZ\_{\lambda t}, |  | (4.3) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​σt2\displaystyle d\sigma\_{t}^{2} | =−λ​σt2​d​t+d​Zλ​t,σ02>0,\displaystyle=-\lambda\sigma\_{t}^{2}dt+dZ\_{\lambda t},\quad\sigma\_{0}^{2}>0, |  | (4.4) |

where

|  |  |  |
| --- | --- | --- |
|  | bt=r−λ​κ​(ρ)−12​σt2,b\_{t}=r-\lambda\kappa(\rho)-\frac{1}{2}\sigma\_{t}^{2}, |  |

and WtW\_{t} and ZtZ\_{t} are a Brownian motion and Lévy process, respectively, under the EMM.
The solution to ([4.4](https://arxiv.org/html/2510.20047v1#S4.E4 "In 4.1 Multivariate BNS model ‣ 4 Multivariate swap for Barndorff-Nielsen and Shephard model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")) is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σt2=e−λ​t​σ02+∫0te−λ​(t−s)​𝑑Zλ​s,\sigma\_{t}^{2}=e^{-\lambda t}\sigma\_{0}^{2}+\int\_{0}^{t}e^{-\lambda(t-s)}dZ\_{\lambda s}, |  | (4.5) |

where σt2\sigma\_{t}^{2} is strictly positive and bounded below by e−λ​t​σ02e^{-\lambda t}\sigma\_{0}^{2}. The instantaneous variance of the log-return from ([4.3](https://arxiv.org/html/2510.20047v1#S4.E3 "In 4.1 Multivariate BNS model ‣ 4 Multivariate swap for Barndorff-Nielsen and Shephard model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")) is (σt2+ρ2​λ​Var​[Z1])​d​t(\sigma\_{t}^{2}+\rho^{2}\lambda\text{Var}[Z\_{1}])dt.
  
  
For nn stocks with log-returns d​XtidX^{i}\_{t} for i∈{1,2,3,…,n}i\in\{1,2,3,...,n\}, the multi-stock follows BNS model is given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​Xti\displaystyle dX^{i}\_{t} | =bti​d​t+(σi)t​d​Bti+ρi​d​Zλ​t∗\displaystyle=b^{i}\_{t}dt+(\sigma^{i})\_{t}dB^{i}\_{t}+\rho\_{i}dZ^{\*}\_{\lambda t} |  | (4.6) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | d​(σi)t2\displaystyle d(\sigma^{i})^{2}\_{t} | =−λ​(σi)t2​d​t+d​Zλ​ti,(σi)02>0\displaystyle=-\lambda(\sigma^{i})^{2}\_{t}dt+dZ^{i}\_{\lambda t},\quad(\sigma^{i})^{2}\_{0}>0 |  | (4.7) |

where BtiB^{i}\_{t} are Wiener processes with [Btl,Btm]=cl​m​(t)​d​t,[B^{l}\_{t},B^{m}\_{t}]=c\_{lm}(t)\,dt,
where cl​m​(t)c\_{lm}(t) is a deterministic function of time t for l,m∈{1,2,3,…,n}l,m\in\{1,2,3,...,n\}, and ZtiZ^{i}\_{t} are independent Lévy processes.
At fixed time tt, cl​m​(t)c\_{lm}(t) are the same values as in Heston model.

### 4.2 Multivariate variance swap using generalized variance method for BNS model

We consider three stocks assuming that the stocks follow the BNS model. The 3×33\times 3 portfolio return covariance matrix for the BNS model equation ([4.6](https://arxiv.org/html/2510.20047v1#S4.E6 "In 4.1 Multivariate BNS model ‣ 4 Multivariate swap for Barndorff-Nielsen and Shephard model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ2=((σ1)t2+ρ12​λ​Var​[Z1∗]c12​σt1​σt2+ρ1​ρ2​λ​Var​[Z1∗]c13​σt1​σt3+ρ1​ρ3​λ​Var​[Z1∗]c21​σt2​σt1+ρ2​ρ1​λ​Var​[Z1∗](σ2)t2+ρ22​λ​Var​[Z1∗]c23​σt2​σt3+ρ2​ρ3​λ​Var​[Z1∗]c31​σt3​σt1+ρ3​ρ1​λ​Var​[Z1∗]c32​σt3​σt2+ρ3​ρ2​λ​Var​[Z1∗](σ3)t2+ρ32​λ​Var​[Z1∗]).\displaystyle\Sigma\_{2}=\begin{pmatrix}(\sigma^{1})\_{t}^{2}+\rho\_{1}^{2}\lambda\text{Var}[Z\_{1}^{\*}]&c\_{12}\sigma^{1}\_{t}\sigma^{2}\_{t}+\rho\_{1}\rho\_{2}\lambda\text{Var}[Z\_{1}^{\*}]&c\_{13}\sigma^{1}\_{t}\sigma^{3}\_{t}+\rho\_{1}\rho\_{3}\lambda\text{Var}[Z\_{1}^{\*}]\\ c\_{21}\sigma^{2}\_{t}\sigma^{1}\_{t}+\rho\_{2}\rho\_{1}\lambda\text{Var}[Z\_{1}^{\*}]&(\sigma^{2})\_{t}^{2}+\rho\_{2}^{2}\lambda\text{Var}[Z\_{1}^{\*}]&c\_{23}\sigma^{2}\_{t}\sigma^{3}\_{t}+\rho\_{2}\rho\_{3}\lambda\text{Var}[Z\_{1}^{\*}]\\ c\_{31}\sigma^{3}\_{t}\sigma^{1}\_{t}+\rho\_{3}\rho\_{1}\lambda\text{Var}[Z\_{1}^{\*}]&c\_{32}\sigma^{3}\_{t}\sigma^{2}\_{t}+\rho\_{3}\rho\_{2}\lambda\text{Var}[Z\_{1}^{\*}]&(\sigma^{3})\_{t}^{2}+\rho\_{3}^{2}\lambda\text{Var}[Z\_{1}^{\*}]\end{pmatrix}. |  | (4.8) |

Similar to equation ([3.6](https://arxiv.org/html/2510.20047v1#S3.E6 "In 3.2 Multivariate variance swap using generalized variance method for Heston model ‣ 3 Multivariate variance swap for Heston model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")), we also need to compute the realized variance σR2\sigma^{2}\_{R} defined as the average of the instantaneous variance in the period [0,T][0,T], which is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | σR2=1T​∫0T|Σ2|​𝑑t.\displaystyle\sigma\_{R}^{2}=\frac{1}{T}\int^{T}\_{0}|\Sigma\_{2}|dt. |  | (4.9) |

In Appendix [A](https://arxiv.org/html/2510.20047v1#A1 "Appendix A Appendix: Calculations of |Σ₁| and |Σ₂| ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models"), we obtain the determinant of ([4.8](https://arxiv.org/html/2510.20047v1#S4.E8 "In 4.2 Multivariate variance swap using generalized variance method for BNS model ‣ 4 Multivariate swap for Barndorff-Nielsen and Shephard model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")) as below

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |Σ2|=\displaystyle|\Sigma\_{2}|= |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |C|∏i=13(σti)2+λVar[Z1∗]|C|(δ11ρ12(σt3)2(σt2)2+δ22ρ22(σt3)2(σt1)2+δ33ρ32(σt2)2(σt1)2\displaystyle|C|\prod\_{i=1}^{3}(\sigma^{i}\_{t})^{2}+\lambda\text{Var}[Z\_{1}^{\*}]|C|\Big(\delta\_{11}\rho\_{1}^{2}(\sigma^{3}\_{t})^{2}(\sigma^{2}\_{t})^{2}+\delta\_{22}\rho\_{2}^{2}(\sigma^{3}\_{t})^{2}(\sigma^{1}\_{t})^{2}+\delta\_{33}\rho\_{3}^{2}(\sigma^{2}\_{t})^{2}(\sigma^{1}\_{t})^{2} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +2δ21ρ2ρ1(σt3)2σt2σt1+2δ31ρ3ρ1σt3(σt2)2σt1+2δ32ρ3ρ2σt3σt2(σt1)2),\displaystyle\qquad\qquad\qquad\qquad\qquad\qquad+2\delta\_{21}\rho\_{2}\rho\_{1}(\sigma^{3}\_{t})^{2}\sigma^{2}\_{t}\sigma^{1}\_{t}+2\delta\_{31}\rho\_{3}\rho\_{1}\sigma^{3}\_{t}(\sigma^{2}\_{t})^{2}\sigma^{1}\_{t}+2\delta\_{32}\rho\_{3}\rho\_{2}\sigma^{3}\_{t}\sigma^{2}\_{t}(\sigma^{1}\_{t})^{2}\Big), |  | (4.10) |

where (δi​j)1≤i,j≤3=C−1(\delta\_{ij})\_{1\leq i,j\leq 3}=C^{-1} can be also calculated by the stock price data.
Based on our construction in equation ([4.7](https://arxiv.org/html/2510.20047v1#S4.E7 "In 4.1 Multivariate BNS model ‣ 4 Multivariate swap for Barndorff-Nielsen and Shephard model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")) where the variance processes are driven by independent processes,
we have

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼⁡[|Σ2|]=\displaystyle\operatorname{\mathbb{E}}[|\Sigma\_{2}|]= |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |C|∏i=13𝔼[(σti)2]+λVar[Z1∗]|C|(δ11ρ12𝔼[(σt3)2]𝔼[(σt2)2]+δ22ρ22𝔼[(σt3)2]𝔼[(σt1)2]\displaystyle|C|\prod\_{i=1}^{3}\operatorname{\mathbb{E}}[(\sigma^{i}\_{t})^{2}]+\lambda\text{Var}[Z\_{1}^{\*}]|C|\Big(\delta\_{11}\rho\_{1}^{2}\operatorname{\mathbb{E}}[(\sigma^{3}\_{t})^{2}]\operatorname{\mathbb{E}}[(\sigma^{2}\_{t})^{2}]+\delta\_{22}\rho\_{2}^{2}\operatorname{\mathbb{E}}[(\sigma^{3}\_{t})^{2}]\operatorname{\mathbb{E}}[(\sigma^{1}\_{t})^{2}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +δ33​ρ32​𝔼⁡[(σt2)2]​𝔼⁡[(σt1)2]+2​δ21​ρ2​ρ1​𝔼⁡[(σt3)2]​𝔼⁡[σt2]​𝔼⁡[σt1]\displaystyle\qquad\qquad\qquad\qquad\qquad\qquad\quad+\delta\_{33}\rho\_{3}^{2}\operatorname{\mathbb{E}}[(\sigma^{2}\_{t})^{2}]\operatorname{\mathbb{E}}[(\sigma^{1}\_{t})^{2}]+2\delta\_{21}\rho\_{2}\rho\_{1}\operatorname{\mathbb{E}}[(\sigma^{3}\_{t})^{2}]\operatorname{\mathbb{E}}[\sigma^{2}\_{t}]\operatorname{\mathbb{E}}[\sigma^{1}\_{t}] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +2δ31ρ3ρ1𝔼[σt3]𝔼[(σt2)2]𝔼[σt1]+2δ32ρ3ρ2𝔼[σt3]𝔼[σt2]𝔼[(σt1)2]).\displaystyle\qquad\qquad\qquad\qquad\qquad\qquad\quad+2\delta\_{31}\rho\_{3}\rho\_{1}\operatorname{\mathbb{E}}[\sigma^{3}\_{t}]\operatorname{\mathbb{E}}[(\sigma^{2}\_{t})^{2}]\operatorname{\mathbb{E}}[\sigma^{1}\_{t}]+2\delta\_{32}\rho\_{3}\rho\_{2}\operatorname{\mathbb{E}}[\sigma^{3}\_{t}]\operatorname{\mathbb{E}}[\sigma^{2}\_{t}]\operatorname{\mathbb{E}}[(\sigma^{1}\_{t})^{2}]\Big). |  | (4.11) |

From equation ([4.5](https://arxiv.org/html/2510.20047v1#S4.E5 "In 4.1 Multivariate BNS model ‣ 4 Multivariate swap for Barndorff-Nielsen and Shephard model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")), we compute the expectation of the variance process:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼⁡[σt2]\displaystyle\operatorname{\mathbb{E}}[\sigma\_{t}^{2}] | =e−λ​t​𝔼⁡[σ02]+∫0te−λ​(t−s)​𝔼⁡[d​Zλ​s]\displaystyle=e^{-\lambda t}\operatorname{\mathbb{E}}[\sigma\_{0}^{2}]+\int\_{0}^{t}e^{-\lambda(t-s)}\operatorname{\mathbb{E}}[dZ\_{\lambda s}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =e−λ​t​σ02+∫0te−λ​(t−s)​κ1​λ​𝑑s\displaystyle=e^{-\lambda t}\sigma\_{0}^{2}+\int\_{0}^{t}e^{-\lambda(t-s)}\ \kappa\_{1}\lambda ds |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =e−λ​t​(σ02−κ1)+κ1,\displaystyle=e^{-\lambda t}(\sigma\_{0}^{2}-\kappa\_{1})+\kappa\_{1}, |  | (4.12) |

where κ1\kappa\_{1} is the 1st cumulant of the subordinator driving the variance process, i.e. the mean of jump size, which can be calculated by the stock price data.
In the 3-dimensional case, we have

|  |  |  |
| --- | --- | --- |
|  | 𝔼⁡[(σti)2]=e−λ​t​((σ0i)2−κ1i)+κ1i,i=1,2,3.\displaystyle\operatorname{\mathbb{E}}[(\sigma\_{t}^{i})^{2}]=e^{-\lambda t}\big((\sigma\_{0}^{i})^{2}-\kappa\_{1}^{i}\big)+\kappa\_{1}^{i},\quad i=1,2,3. |  |

Using the above equation, we obtain the followings:

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∏i=13𝔼​[(σti)2]\displaystyle\prod\_{i=1}^{3}\mathbb{E}[(\sigma\_{t}^{i})^{2}] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle=\ | e−3​λ​t​((σ01)2−κ11)​((σ02)2−κ12)​((σ03)2−κ13)\displaystyle e^{-3\lambda t}\big((\sigma\_{0}^{1})^{2}-\kappa\_{1}^{1}\big)\big((\sigma\_{0}^{2})^{2}-\kappa\_{1}^{2}\big)\big((\sigma\_{0}^{3})^{2}-\kappa\_{1}^{3}\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +e−2​λ​t[κ11((σ02)2−κ12)((σ03)2−κ13)+κ12((σ01)2−κ11)((σ03)2−κ13)\displaystyle+e^{-2\lambda t}\Big[\kappa\_{1}^{1}\big((\sigma\_{0}^{2})^{2}-\kappa\_{1}^{2}\big)\big((\sigma\_{0}^{3})^{2}-\kappa\_{1}^{3}\big)+\kappa\_{1}^{2}\big((\sigma\_{0}^{1})^{2}-\kappa\_{1}^{1}\big)\big((\sigma\_{0}^{3})^{2}-\kappa\_{1}^{3}\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +κ13((σ01)2−κ11)((σ02)2−κ12)]\displaystyle\qquad\qquad+\kappa\_{1}^{3}\big((\sigma\_{0}^{1})^{2}-\kappa\_{1}^{1}\big)\big((\sigma\_{0}^{2})^{2}-\kappa\_{1}^{2}\big)\Big] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +e−λ​t​[κ11​κ12​((σ03)2−κ13)+κ11​κ13​((σ02)2−κ12)+κ12​κ13​((σ01)2−κ11)]+κ11​κ12​κ13,\displaystyle+e^{-\lambda t}\Big[\kappa\_{1}^{1}\kappa\_{1}^{2}\big((\sigma\_{0}^{3})^{2}-\kappa\_{1}^{3}\big)+\kappa\_{1}^{1}\kappa\_{1}^{3}\big((\sigma\_{0}^{2})^{2}-\kappa\_{1}^{2}\big)+\kappa\_{1}^{2}\kappa\_{1}^{3}\big((\sigma\_{0}^{1})^{2}-\kappa\_{1}^{1}\big)\Big]+\kappa\_{1}^{1}\kappa\_{1}^{2}\kappa\_{1}^{3}, |  | (4.13) |

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​[(σt3)2]​𝔼​[(σt2)2]\displaystyle\mathbb{E}\big[(\sigma\_{t}^{3})^{2}\big]\mathbb{E}\big[(\sigma\_{t}^{2})^{2}\big] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle=\ | e−2​λ​t​((σ03)2−κ13)​((σ02)2−κ12)+e−λ​t​[κ13​((σ02)2−κ12)+κ12​((σ03)2−κ13)]+κ13​κ12,\displaystyle e^{-2\lambda t}\big((\sigma\_{0}^{3})^{2}-\kappa\_{1}^{3}\big)\big((\sigma\_{0}^{2})^{2}-\kappa\_{1}^{2}\big)+e^{-\lambda t}\Big[\kappa\_{1}^{3}\big((\sigma\_{0}^{2})^{2}-\kappa\_{1}^{2}\big)+\kappa\_{1}^{2}\big((\sigma\_{0}^{3})^{2}-\kappa\_{1}^{3}\big)\Big]+\kappa\_{1}^{3}\kappa\_{1}^{2}, |  | (4.14) |

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​[(σt3)2]​𝔼​[(σt1)2]\displaystyle\mathbb{E}\big[(\sigma\_{t}^{3})^{2}\big]\mathbb{E}\big[(\sigma\_{t}^{1})^{2}\big] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle=\ | e−2​λ​t​((σ03)2−κ13)​((σ01)2−κ11)+e−λ​t​[κ13​((σ01)2−κ11)+κ11​((σ03)2−κ13)]+κ13​κ11,\displaystyle e^{-2\lambda t}\big((\sigma\_{0}^{3})^{2}-\kappa\_{1}^{3}\big)\big((\sigma\_{0}^{1})^{2}-\kappa\_{1}^{1}\big)+e^{-\lambda t}\Big[\kappa\_{1}^{3}\big((\sigma\_{0}^{1})^{2}-\kappa\_{1}^{1}\big)+\kappa\_{1}^{1}\big((\sigma\_{0}^{3})^{2}-\kappa\_{1}^{3}\big)\Big]+\kappa\_{1}^{3}\kappa\_{1}^{1}, |  | (4.15) |

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 𝔼​[(σt2)2]​𝔼​[(σt1)2]\displaystyle\mathbb{E}\big[(\sigma\_{t}^{2})^{2}\big]\mathbb{E}\big[(\sigma\_{t}^{1})^{2}\big] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle=\ | e−2​λ​t​((σ02)2−κ12)​((σ01)2−κ11)+e−λ​t​[κ12​((σ01)2−κ11)+κ11​((σ02)2−κ12)]+κ12​κ11.\displaystyle e^{-2\lambda t}\big((\sigma\_{0}^{2})^{2}-\kappa\_{1}^{2}\big)\big((\sigma\_{0}^{1})^{2}-\kappa\_{1}^{1}\big)+e^{-\lambda t}\Big[\kappa\_{1}^{2}\big((\sigma\_{0}^{1})^{2}-\kappa\_{1}^{1}\big)+\kappa\_{1}^{1}\big((\sigma\_{0}^{2})^{2}-\kappa\_{1}^{2}\big)\Big]+\kappa\_{1}^{2}\kappa\_{1}^{1}. |  | (4.16) |

###### Theorem 4.1.

The arbitrage free price of the multivariate variance swap for St1,St2,S^{1}\_{t},S^{2}\_{t}, and St3S^{3}\_{t}, assuming they follow the BNS model and using the generalized variance method, is given by:

|  |  |  |
| --- | --- | --- |
|  | Pv​a​r=e−r​T​𝔼⁡[σR2]−e−r​T​Kvar.P\_{var}=e^{-rT}\operatorname{\mathbb{E}}[\sigma\_{R}^{2}]-e^{-rT}K\_{\text{var}}. |  |

###### Proof.

We firstly compute the variance of the process ([4.5](https://arxiv.org/html/2510.20047v1#S4.E5 "In 4.1 Multivariate BNS model ‣ 4 Multivariate swap for Barndorff-Nielsen and Shephard model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")) as below

|  |  |  |  |
| --- | --- | --- | --- |
|  | Var​[σt2]\displaystyle\text{Var}[\sigma\_{t}^{2}] | =0+∫0t(e−λ​(t−s))2​Var​[d​Zλ​s]+0\displaystyle=0+\int\_{0}^{t}\big(e^{-\lambda(t-s)}\big)^{2}\ \text{Var}[dZ\_{\lambda s}]+0 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0te−2​λ​(t−s)​κ2​λ​𝑑s\displaystyle=\int\_{0}^{t}e^{-2\lambda(t-s)}\ \kappa\_{2}\lambda ds |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =κ22​(1−e−2​λ​t),\displaystyle=\frac{\kappa\_{2}}{2}\left(1-e^{-2\lambda t}\right), |  | (4.17) |

where κ2\kappa\_{2} is the 2nd cumulant of the subordinator driving the variance process, i.e. the variance of jump size, which can be also calculated by the stock price data.
Then, a useful estimate approximation regarding the expected value of realized volatility is obtained in [[7](https://arxiv.org/html/2510.20047v1#bib.bib7)] and is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[σt]=𝔼⁡[σt2]≈𝔼⁡[σt2]−Var​[σt2]8​(𝔼⁡[σt2])3/2.\displaystyle\mathbb{E}[\sigma\_{t}]=\operatorname{\mathbb{E}}[\sqrt{\sigma^{2}\_{t}}]\approx\sqrt{\operatorname{\mathbb{E}}[\sigma^{2}\_{t}]}-\frac{\text{Var}[\sigma^{2}\_{t}]}{8(\operatorname{\mathbb{E}}[\sigma^{2}\_{t}])^{3/2}}. |  | (4.18) |

The absolute error of such approximation is less than or equal to μ316​(𝔼⁡[σt2])5/2\frac{\mu\_{3}}{16(\operatorname{\mathbb{E}}[\sigma^{2}\_{t}])^{5/2}}, where μ3\mu\_{3} is the 3rd central moment of σt2\sigma^{2}\_{t}.
In the 3-dimensional case, we substitute ([4.2](https://arxiv.org/html/2510.20047v1#S4.Ex9 "4.2 Multivariate variance swap using generalized variance method for BNS model ‣ 4 Multivariate swap for Barndorff-Nielsen and Shephard model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")) and ([4.2](https://arxiv.org/html/2510.20047v1#S4.Ex20 "4.2 Multivariate variance swap using generalized variance method for BNS model ‣ 4 Multivariate swap for Barndorff-Nielsen and Shephard model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")) into ([4.18](https://arxiv.org/html/2510.20047v1#S4.E18 "In 4.2 Multivariate variance swap using generalized variance method for BNS model ‣ 4 Multivariate swap for Barndorff-Nielsen and Shephard model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")) and obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[σti]≈e−λ​t​((σ0i)2−κ1i)+κ1i−κ2i​(1−e−2​λ​t)16​(e−λ​t​((σ0i)2−κ1i)+κ1i)3/2,i=1,2,3,\displaystyle\mathbb{E}[\sigma\_{t}^{i}]\approx\sqrt{e^{-\lambda t}\big((\sigma\_{0}^{i})^{2}-\kappa\_{1}^{i}\big)+\kappa\_{1}^{i}}-\frac{\kappa^{i}\_{2}(1-e^{-2\lambda t})}{16\big(e^{-\lambda t}\big((\sigma\_{0}^{i})^{2}-\kappa\_{1}^{i}\big)+\kappa\_{1}^{i}\big)^{3/2}},\quad i=1,2,3, |  | (4.19) |

whose absolute error is less than or equal to μ316​(e−λ​t​((σ0i)2−κ1i)+κ1i)5/2\frac{\mu\_{3}}{16(e^{-\lambda t}((\sigma\_{0}^{i})^{2}-\kappa\_{1}^{i})+\kappa\_{1}^{i})^{5/2}} for each ii.
  
  
The expected value of equation ([4.9](https://arxiv.org/html/2510.20047v1#S4.E9 "In 4.2 Multivariate variance swap using generalized variance method for BNS model ‣ 4 Multivariate swap for Barndorff-Nielsen and Shephard model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")) applying equations ([4.2](https://arxiv.org/html/2510.20047v1#S4.Ex6 "4.2 Multivariate variance swap using generalized variance method for BNS model ‣ 4 Multivariate swap for Barndorff-Nielsen and Shephard model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")), ([4.2](https://arxiv.org/html/2510.20047v1#S4.Ex12 "4.2 Multivariate variance swap using generalized variance method for BNS model ‣ 4 Multivariate swap for Barndorff-Nielsen and Shephard model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")), ([4.2](https://arxiv.org/html/2510.20047v1#S4.Ex16 "4.2 Multivariate variance swap using generalized variance method for BNS model ‣ 4 Multivariate swap for Barndorff-Nielsen and Shephard model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")), ([4.2](https://arxiv.org/html/2510.20047v1#S4.Ex17 "4.2 Multivariate variance swap using generalized variance method for BNS model ‣ 4 Multivariate swap for Barndorff-Nielsen and Shephard model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")), ([4.2](https://arxiv.org/html/2510.20047v1#S4.Ex18 "4.2 Multivariate variance swap using generalized variance method for BNS model ‣ 4 Multivariate swap for Barndorff-Nielsen and Shephard model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")), ([4.19](https://arxiv.org/html/2510.20047v1#S4.E19 "In 4.2 Multivariate variance swap using generalized variance method for BNS model ‣ 4 Multivariate swap for Barndorff-Nielsen and Shephard model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")), and Var​[Z1∗]=κ2∗\text{Var}[Z\_{1}^{\*}]=\kappa\_{2}^{\*} gives that

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼⁡[σR2]\displaystyle\operatorname{\mathbb{E}}[\sigma\_{R}^{2}] | =1T​∫0T𝔼⁡[|Σ2|]​𝑑t\displaystyle=\frac{1}{T}\int\_{0}^{T}\operatorname{\mathbb{E}}[|\Sigma\_{2}|]dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =|C|T[E0+λκ2∗(δ11ρ12E1+δ22ρ22E2+δ33ρ32E3\displaystyle=\frac{|C|}{T}\Big[E\_{0}+\lambda\kappa\_{2}^{\*}\big(\delta\_{11}\rho\_{1}^{2}E\_{1}+\delta\_{22}\rho\_{2}^{2}E\_{2}+\delta\_{33}\rho\_{3}^{2}E\_{3} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +2δ21ρ2ρ1E4+2δ31ρ3ρ1E5+2δ32ρ3ρ2E6)],\displaystyle\qquad\qquad\qquad\qquad+2\delta\_{21}\rho\_{2}\rho\_{1}E\_{4}+2\delta\_{31}\rho\_{3}\rho\_{1}E\_{5}+2\delta\_{32}\rho\_{3}\rho\_{2}E\_{6}\big)\Big], |  | (4.20) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | E0\displaystyle E\_{0} | =∫0T∏i=13𝔼​[(σti)2]​d​t\displaystyle=\int\_{0}^{T}\prod\_{i=1}^{3}\mathbb{E}[(\sigma\_{t}^{i})^{2}]dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1−e−3​λ​T3​λ​((σ01)2−κ11)​((σ02)2−κ12)​((σ03)2−κ13)\displaystyle=\frac{1-e^{-3\lambda T}}{3\lambda}\big((\sigma\_{0}^{1})^{2}-\kappa\_{1}^{1}\big)\big((\sigma\_{0}^{2})^{2}-\kappa\_{1}^{2}\big)\big((\sigma\_{0}^{3})^{2}-\kappa\_{1}^{3}\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +1−e−2​λ​T2​λ[κ11((σ02)2−κ12)((σ03)2−κ13)+κ12((σ01)2−κ11)((σ03)2−κ13)\displaystyle\quad+\frac{1-e^{-2\lambda T}}{2\lambda}\Big[\kappa\_{1}^{1}\big((\sigma\_{0}^{2})^{2}-\kappa\_{1}^{2}\big)\big((\sigma\_{0}^{3})^{2}-\kappa\_{1}^{3}\big)+\kappa\_{1}^{2}\big((\sigma\_{0}^{1})^{2}-\kappa\_{1}^{1}\big)\big((\sigma\_{0}^{3})^{2}-\kappa\_{1}^{3}\big) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +κ13((σ01)2−κ11)((σ02)2−κ12)]\displaystyle\qquad\qquad\qquad\quad+\kappa\_{1}^{3}\big((\sigma\_{0}^{1})^{2}-\kappa\_{1}^{1}\big)\big((\sigma\_{0}^{2})^{2}-\kappa\_{1}^{2}\big)\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +1−e−λ​Tλ​[κ11​κ12​((σ03)2−κ13)+κ11​κ13​((σ02)2−κ12)+κ12​κ13​((σ01)2−κ11)]+T​κ11​κ12​κ13,\displaystyle\quad+\frac{1-e^{-\lambda T}}{\lambda}\Big[\kappa\_{1}^{1}\kappa\_{1}^{2}\big((\sigma\_{0}^{3})^{2}-\kappa\_{1}^{3}\big)+\kappa\_{1}^{1}\kappa\_{1}^{3}\big((\sigma\_{0}^{2})^{2}-\kappa\_{1}^{2}\big)+\kappa\_{1}^{2}\kappa\_{1}^{3}\big((\sigma\_{0}^{1})^{2}-\kappa\_{1}^{1}\big)\Big]+T\kappa\_{1}^{1}\kappa\_{1}^{2}\kappa\_{1}^{3}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | E1=\displaystyle E\_{1}= | ∫0T𝔼​[(σt3)2]​𝔼​[(σt2)2]​𝑑t\displaystyle\int\_{0}^{T}\mathbb{E}\big[(\sigma\_{t}^{3})^{2}\big]\mathbb{E}\big[(\sigma\_{t}^{2})^{2}\big]dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle=\ | 1−e−2​λ​T2​λ​((σ03)2−κ13)​((σ02)2−κ12)+1−e−λ​Tλ​[κ13​((σ02)2−κ12)+κ12​((σ03)2−κ13)]\displaystyle\frac{1-e^{-2\lambda T}}{2\lambda}\big((\sigma\_{0}^{3})^{2}-\kappa\_{1}^{3}\big)\big((\sigma\_{0}^{2})^{2}-\kappa\_{1}^{2}\big)+\frac{1-e^{-\lambda T}}{\lambda}\Big[\kappa\_{1}^{3}\big((\sigma\_{0}^{2})^{2}-\kappa\_{1}^{2}\big)+\kappa\_{1}^{2}\big((\sigma\_{0}^{3})^{2}-\kappa\_{1}^{3}\big)\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +T​κ13​κ12,\displaystyle+T\kappa\_{1}^{3}\kappa\_{1}^{2}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | E2=\displaystyle E\_{2}= | ∫0T𝔼​[(σt3)2]​𝔼​[(σt1)2]​𝑑t\displaystyle\int\_{0}^{T}\mathbb{E}\big[(\sigma\_{t}^{3})^{2}\big]\mathbb{E}\big[(\sigma\_{t}^{1})^{2}\big]dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle=\ | 1−e−2​λ​T2​λ​((σ03)2−κ13)​((σ01)2−κ11)+1−e−λ​Tλ​[κ13​((σ01)2−κ11)+κ11​((σ03)2−κ13)]\displaystyle\frac{1-e^{-2\lambda T}}{2\lambda}\big((\sigma\_{0}^{3})^{2}-\kappa\_{1}^{3}\big)\big((\sigma\_{0}^{1})^{2}-\kappa\_{1}^{1}\big)+\frac{1-e^{-\lambda T}}{\lambda}\Big[\kappa\_{1}^{3}\big((\sigma\_{0}^{1})^{2}-\kappa\_{1}^{1}\big)+\kappa\_{1}^{1}\big((\sigma\_{0}^{3})^{2}-\kappa\_{1}^{3}\big)\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +T​κ13​κ11,\displaystyle+T\kappa\_{1}^{3}\kappa\_{1}^{1}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | E3=\displaystyle E\_{3}= | ∫0T𝔼​[(σt2)2]​𝔼​[(σt1)2]​𝑑t\displaystyle\int\_{0}^{T}\mathbb{E}\big[(\sigma\_{t}^{2})^{2}\big]\mathbb{E}\big[(\sigma\_{t}^{1})^{2}\big]dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle=\ | 1−e−2​λ​T2​λ​((σ02)2−κ12)​((σ01)2−κ11)+1−e−λ​Tλ​[κ12​((σ01)2−κ11)+κ11​((σ02)2−κ12)]\displaystyle\frac{1-e^{-2\lambda T}}{2\lambda}\big((\sigma\_{0}^{2})^{2}-\kappa\_{1}^{2}\big)\big((\sigma\_{0}^{1})^{2}-\kappa\_{1}^{1}\big)+\frac{1-e^{-\lambda T}}{\lambda}\Big[\kappa\_{1}^{2}\big((\sigma\_{0}^{1})^{2}-\kappa\_{1}^{1}\big)+\kappa\_{1}^{1}\big((\sigma\_{0}^{2})^{2}-\kappa\_{1}^{2}\big)\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +T​κ12​κ11,\displaystyle+T\kappa\_{1}^{2}\kappa\_{1}^{1}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | E4\displaystyle E\_{4} | =∫0T𝔼⁡[(σt3)2]​𝔼⁡[σt2]​𝔼⁡[σt1]​𝑑t\displaystyle=\int\_{0}^{T}\operatorname{\mathbb{E}}[(\sigma^{3}\_{t})^{2}]\operatorname{\mathbb{E}}[\sigma^{2}\_{t}]\operatorname{\mathbb{E}}[\sigma^{1}\_{t}]dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≈∫0T[e−λ​t​((σ03)2−κ13)+κ13]\displaystyle\approx\int\_{0}^{T}\Big[e^{-\lambda t}\big((\sigma\_{0}^{3})^{2}-\kappa\_{1}^{3}\big)+\kappa\_{1}^{3}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×[e−λ​t​((σ02)2−κ12)+κ12−κ22​(1−e−2​λ​t)16​(e−λ​t​((σ02)2−κ12)+κ12)3/2]\displaystyle\qquad\quad\times\Bigg[\sqrt{e^{-\lambda t}\big((\sigma\_{0}^{2})^{2}-\kappa\_{1}^{2}\big)+\kappa\_{1}^{2}}-\frac{\kappa^{2}\_{2}(1-e^{-2\lambda t})}{16\big(e^{-\lambda t}\big((\sigma\_{0}^{2})^{2}-\kappa\_{1}^{2}\big)+\kappa\_{1}^{2}\big)^{3/2}}\Bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×[e−λ​t​((σ01)2−κ11)+κ11−κ21​(1−e−2​λ​t)16​(e−λ​t​((σ01)2−κ11)+κ11)3/2]​d​t,\displaystyle\qquad\quad\times\Bigg[\sqrt{e^{-\lambda t}\big((\sigma\_{0}^{1})^{2}-\kappa\_{1}^{1}\big)+\kappa\_{1}^{1}}-\frac{\kappa^{1}\_{2}(1-e^{-2\lambda t})}{16\big(e^{-\lambda t}\big((\sigma\_{0}^{1})^{2}-\kappa\_{1}^{1}\big)+\kappa\_{1}^{1}\big)^{3/2}}\Bigg]dt, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | E5\displaystyle E\_{5} | =∫0T𝔼⁡[σt3]​𝔼⁡[(σt2)2]​𝔼⁡[σt1]​𝑑t\displaystyle=\int\_{0}^{T}\operatorname{\mathbb{E}}[\sigma^{3}\_{t}]\operatorname{\mathbb{E}}[(\sigma^{2}\_{t})^{2}]\operatorname{\mathbb{E}}[\sigma^{1}\_{t}]dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≈∫0T[e−λ​t​((σ03)2−κ13)+κ13−κ23​(1−e−2​λ​t)16​(e−λ​t​((σ03)2−κ13)+κ13)3/2]\displaystyle\approx\int\_{0}^{T}\Bigg[\sqrt{e^{-\lambda t}\big((\sigma\_{0}^{3})^{2}-\kappa\_{1}^{3}\big)+\kappa\_{1}^{3}}-\frac{\kappa^{3}\_{2}(1-e^{-2\lambda t})}{16\big(e^{-\lambda t}\big((\sigma\_{0}^{3})^{2}-\kappa\_{1}^{3}\big)+\kappa\_{1}^{3}\big)^{3/2}}\Bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×[e−λ​t​((σ02)2−κ12)+κ12]\displaystyle\qquad\quad\times\Big[e^{-\lambda t}\big((\sigma\_{0}^{2})^{2}-\kappa\_{1}^{2}\big)+\kappa\_{1}^{2}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×[e−λ​t​((σ01)2−κ11)+κ11−κ21​(1−e−2​λ​t)16​(e−λ​t​((σ01)2−κ11)+κ11)3/2]​d​t,\displaystyle\qquad\quad\times\Bigg[\sqrt{e^{-\lambda t}\big((\sigma\_{0}^{1})^{2}-\kappa\_{1}^{1}\big)+\kappa\_{1}^{1}}-\frac{\kappa^{1}\_{2}(1-e^{-2\lambda t})}{16\big(e^{-\lambda t}\big((\sigma\_{0}^{1})^{2}-\kappa\_{1}^{1}\big)+\kappa\_{1}^{1}\big)^{3/2}}\Bigg]dt, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | E6\displaystyle E\_{6} | =∫0T𝔼⁡[σt3]​𝔼⁡[σt2]​𝔼⁡[(σt1)2]​𝑑t\displaystyle=\int\_{0}^{T}\operatorname{\mathbb{E}}[\sigma^{3}\_{t}]\operatorname{\mathbb{E}}[\sigma^{2}\_{t}]\operatorname{\mathbb{E}}[(\sigma^{1}\_{t})^{2}]dt |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≈∫0T[e−λ​t​((σ03)2−κ13)+κ13−κ23​(1−e−2​λ​t)16​(e−λ​t​((σ03)2−κ13)+κ13)3/2]\displaystyle\approx\int\_{0}^{T}\Bigg[\sqrt{e^{-\lambda t}\big((\sigma\_{0}^{3})^{2}-\kappa\_{1}^{3}\big)+\kappa\_{1}^{3}}-\frac{\kappa^{3}\_{2}(1-e^{-2\lambda t})}{16\big(e^{-\lambda t}\big((\sigma\_{0}^{3})^{2}-\kappa\_{1}^{3}\big)+\kappa\_{1}^{3}\big)^{3/2}}\Bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×[e−λ​t​((σ02)2−κ12)+κ12−κ22​(1−e−2​λ​t)16​(e−λ​t​((σ02)2−κ12)+κ12)3/2]\displaystyle\qquad\quad\times\Bigg[\sqrt{e^{-\lambda t}\big((\sigma\_{0}^{2})^{2}-\kappa\_{1}^{2}\big)+\kappa\_{1}^{2}}-\frac{\kappa^{2}\_{2}(1-e^{-2\lambda t})}{16\big(e^{-\lambda t}\big((\sigma\_{0}^{2})^{2}-\kappa\_{1}^{2}\big)+\kappa\_{1}^{2}\big)^{3/2}}\Bigg] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ×[e−λ​t​((σ01)2−κ11)+κ11]​d​t.\displaystyle\qquad\quad\times\Big[e^{-\lambda t}\big((\sigma\_{0}^{1})^{2}-\kappa\_{1}^{1}\big)+\kappa\_{1}^{1}\Big]dt. |  |

Finally, the theorem uses equation ([4.2](https://arxiv.org/html/2510.20047v1#S4.Ex22 "4.2 Multivariate variance swap using generalized variance method for BNS model ‣ 4 Multivariate swap for Barndorff-Nielsen and Shephard model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")) to complete the proof.
∎

## 5 Model Fitting and Parameter Estimation

This section presents numerical results, model calibration, and parameter testing procedures. For the purpose of model calibration, nine stocks were selected using the “quantmod” package [[18](https://arxiv.org/html/2510.20047v1#bib.bib18)] in R [[21](https://arxiv.org/html/2510.20047v1#bib.bib21)], covering the period from January 1, 2021, to January 1, 2024. The mean, variance, and kurtosis of the 9 assets can be also found in appendix [B](https://arxiv.org/html/2510.20047v1#A2 "Appendix B Appendix: Summary Statistics ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models"). These stocks were then randomly reshuffled into three groups, each consisting of three stocks, to evaluate the robustness and precision of the proposed model in different combinations of assets. The log-returns of the daily closing prices were computed for each stock. Subsequently, the covariance matrix of the log-returns was estimated at 10-day time intervals, and the determinant of each covariance matrix was calculated to capture the joint variability and dependency structure among the selected assets over time. The correlation matrix of Coca-Cola, Apple, and Tesla, the correlation matrix for Google, Microsoft, and Meta, and the correlation matrix for J.P. Morgan, Nvidia, and Amazon are in Figure [2](https://arxiv.org/html/2510.20047v1#S5.F2 "Figure 2 ‣ 5 Model Fitting and Parameter Estimation ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models").

![Refer to caption](x1.png)


(a) KO, AAPL,TSLA

![Refer to caption](x2.png)


(b) GOOGL, MSFT, META,

![Refer to caption](x3.png)


(c) JPM, NVDA, AMZN

Figure 1: Grouped histogram of 9 stocks over the period 2021–2024.

Figure [1](https://arxiv.org/html/2510.20047v1#S5.F1 "Figure 1 ‣ 5 Model Fitting and Parameter Estimation ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models") presents histograms of the log-return distributions of the three stocks grouped together for analysis. The histograms reveal that all underlying assets display similar distributional patterns, suggesting that their return behaviors share comparable statistical characteristics. This similarity in log-return distributions implies that the assets may respond to market factors in a consistent manner, which provides a reasonable basis for conducting a joint variance swap analysis.

![Refer to caption](x4.png)


(a) KO, AAPL,TSLA

![Refer to caption](x5.png)


(b) GOOGL, MSFT, META,

![Refer to caption](x6.png)


(c) JPM, NVDA, AMZN

Figure 2: Grouped correlations of 9 stocks over the period 2021–2024.

Figure [2](https://arxiv.org/html/2510.20047v1#S5.F2 "Figure 2 ‣ 5 Model Fitting and Parameter Estimation ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models") illustrates the correlation matrix among the three underlying assets considered in this analysis. The correlation heatmap indicates that the assets are generally moderately to weakly correlated with one another, except for META and Google, which exhibit a relatively strong positive correlation with a coefficient of 0.72. This suggests that META and Google tend to move in similar directions more frequently compared to the other asset pairs.

![Refer to caption](x7.png)


(a) KO, AAPL,TSLA

![Refer to caption](x8.png)


(b) GOOGL, MSFT, META,

![Refer to caption](x9.png)


(c) JPM, NVDA, AMZN

Figure 3: Grouped cumulative returns of 9 stocks over the period 2021–2024.

Figure [3](https://arxiv.org/html/2510.20047v1#S5.F3 "Figure 3 ‣ 5 Model Fitting and Parameter Estimation ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models") illustrates the cumulative returns of the closing prices for the nine selected assets, grouped as follows: the left panel presents Coca-Cola, Apple, and Tesla; the middle panel displays Google, Microsoft, and Meta; and the right panel includes JPMorgan, Nvidia, and Amazon. The figure clearly shows that the cumulative return distributions of these assets vary substantially. Some assets, such as Tesla and Nvidia, exhibit high volatility, whereas others, like J.P. Morgan, demonstrate relatively stable performance. The rationale for selecting this diverse set of covariates is to evaluate the robustness and generalization capability of the model’s predictive accuracy across assets with different volatility and market behaviors.

![Refer to caption](x10.png)


(a) KO, AAPL, TSLA

![Refer to caption](x11.png)


(b) GOOGL, MSFT, META

![Refer to caption](x12.png)


(c) JPM, NDVA, AMZN

Figure 4: Realized vs Fitted Multivariate Variance Swap under Heston and BNS Models

Figure [4](https://arxiv.org/html/2510.20047v1#S5.F4 "Figure 4 ‣ 5 Model Fitting and Parameter Estimation ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models") presents the realized variance of the covariance matrix along with the fitted results obtained from the Heston and BNS models. A nonlinear least squares (NLS) estimator was employed in R for parameter calibration and model validation. The estimation results indicate that all parameters in both the Heston and BNS models were statistically significant, with pp-values on the order of 2.6×10−162.6\times 10^{-16}, confirming the overall robustness and suitability of the fitted models.
  
  
Based on these findings, both the Heston and BNS models demonstrated strong performance in capturing and predicting the determinant of the realized variance. However, the BNS model outperformed the Heston model in several key aspect it achieved higher predictive accuracy, reduced the mean squared error, and exhibited faster convergence. Quantitatively, the BNS model was able to explain approximately 40% more of the variation in the data that the Heston model fails to capture. Hence, on average, the BNS model provided about a 40% improvement in performance over the standard Heston model.
  
  
Multiple error metrics are employed to evaluate the performance and accuracy of our models, including the Absolute Percentage Error (APE), Average Absolute Error (AAE), Average Relative Percentage Error (ARPE), and Root Mean Square Error (RMSE). These metrics provide a comprehensive assessment of model goodness-of-fit by capturing different aspects of prediction error both in magnitude and variability. The formal definitions of these error measures, as summarized in Tables [1](https://arxiv.org/html/2510.20047v1#S5.T1 "Table 1 ‣ 5 Model Fitting and Parameter Estimation ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models") and [2](https://arxiv.org/html/2510.20047v1#S5.T2 "Table 2 ‣ 5 Model Fitting and Parameter Estimation ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models"), are expressed as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | APE | =1σ¯R2​∑i=1n|σR2​(ti)−σ^R2​(ti)|n,\displaystyle=\frac{1}{\bar{\sigma}\_{R}^{2}}\sum\_{i=1}^{n}\frac{|\sigma\_{R}^{2}(t\_{i})-\hat{\sigma}\_{R}^{2}(t\_{i})|}{n}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | AAE | =1n​∑i=1n|σR2​(ti)−σ^R2​(ti)|,\displaystyle=\frac{1}{n}\sum\_{i=1}^{n}|\sigma\_{R}^{2}(t\_{i})-\hat{\sigma}\_{R}^{2}(t\_{i})|, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | ARPE | =1n​∑i=1n|σR2​(ti)−σ^R2​(ti)|σR2​(ti),\displaystyle=\frac{1}{n}\sum\_{i=1}^{n}\frac{|\sigma\_{R}^{2}(t\_{i})-\hat{\sigma}\_{R}^{2}(t\_{i})|}{\sigma\_{R}^{2}(t\_{i})}, |  |

|  |  |  |  |
| --- | --- | --- | --- |
|  | RMSE | =1n​∑i=1n(σR2​(ti)−σ^R2​(ti))2.\displaystyle=\sqrt{\frac{1}{n}\sum\_{i=1}^{n}\Big(\sigma\_{R}^{2}(t\_{i})-\hat{\sigma}\_{R}^{2}(t\_{i})\Big)^{2}}. |  |

Table 1: Error measurement when Heston model is implemented.

| Covariate | RMSE | APE | AAE | ARPE |
| --- | --- | --- | --- | --- |
| KO, AAPL, TSLA | 0.2528 | 0.0003 | <0.0001 | 0.0003 |
| GOOGL, MSFT, META | 0.3231 | 0.0004 | <0.0001 | 0.0006 |
| JPM, NVDA, AMZN | 10.1830 | 0.0003 | <0.0001 | 0.0003 |




Table 2: Error measurement when BNS model is implemented.

| Covariate | RMSE | APE | AAE | ARPE |
| --- | --- | --- | --- | --- |
| KO, AAPL, TSLA | 0.1708 | 0.0002 | <0.0001 | 0.0001 |
| GOOGL, MSFT, META | 0.1704 | <0.0001 | <0.0001 | 0.0001 |
| JPM, NVDA, AMZN | 0.1088 | 0.0002 | <0.0001 | 0.0002 |

Tables [1](https://arxiv.org/html/2510.20047v1#S5.T1 "Table 1 ‣ 5 Model Fitting and Parameter Estimation ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models") and [2](https://arxiv.org/html/2510.20047v1#S5.T2 "Table 2 ‣ 5 Model Fitting and Parameter Estimation ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models") present the numerical error calculations for the realized variance of the multi-asset determinant covariate matrices. The reported error metrics provide a quantitative comparison between the models, highlighting their relative predictive performance. As shown in these tables, the BNS model consistently demonstrates lower error values across all measures, indicating a superior fit and improved accuracy compared to the standard Heston model. This result suggests that the BNS framework captures the underlying market dynamics more effectively, particularly in modeling volatility and cross-asset relationships.

## 6 Conclusion

In this paper, we introduced a generalized variance method to compute the instantaneous variance of the log-returns for multi-stock dynamics under both the Heston and Barndorff-Nielsen–Shephard (BNS) models. This method is based on the computation of the determinant of the portfolio return covariance matrix, providing a more tractable approach for estimating the realized variance of selected stocks in our numerical analysis.

We selected nine stocks and randomly reshuffled them into three groups, each containing three distinct stocks. The fitted models from both the Heston and BNS frameworks showed a strong agreement with the empirical realized variance over the selected time horizons. Notably, the BNS model demonstrated an superior fit, capturing approximately 40% more of the variance in the data that the Heston model failed to explain. Meanwhile, the BNS model demonstrated lower errors indicating an improved accuracy compared to the Heston model.
This aligns with our expectations, as the BNS model is capable of capturing jumps more effectively in the underlying asset dynamics.

## Appendix A Appendix: Calculations of |Σ1||\Sigma\_{1}| and |Σ2||\Sigma\_{2}|

If the 3-dimensional covariance matrix for Heston model is given by ([3.5](https://arxiv.org/html/2510.20047v1#S3.E5 "In 3.2 Multivariate variance swap using generalized variance method for Heston model ‣ 3 Multivariate variance swap for Heston model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")), it is trivial that (σi)t2=σti​σti(\sigma^{i})\_{t}^{2}=\sigma^{i}\_{t}\sigma^{i}\_{t}, i=1,2,3i=1,2,3. Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ1=D​C​D,\displaystyle\Sigma\_{1}=DCD, |  | (A.1) |

where C=(cl​m)1≤l,m≤3C=(c\_{lm})\_{1\leq l,m\leq 3} is the correlation matrix of stock prices which can be calculated using stock price data, and D=diag​(σt1,σt2,σt3)D=\text{diag}(\sigma^{1}\_{t},\sigma^{2}\_{t},\sigma^{3}\_{t}).
Hence, |Σ1|=|C|​|D|2|\Sigma\_{1}|=|C||D|^{2} gives equation ([3.7](https://arxiv.org/html/2510.20047v1#S3.E7 "In 3.2 Multivariate variance swap using generalized variance method for Heston model ‣ 3 Multivariate variance swap for Heston model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")).
  
  
If the 3-dimensional covariance matrix for BNS model is given by ([4.8](https://arxiv.org/html/2510.20047v1#S4.E8 "In 4.2 Multivariate variance swap using generalized variance method for BNS model ‣ 4 Multivariate swap for Barndorff-Nielsen and Shephard model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")), then

|  |  |  |
| --- | --- | --- |
|  | Σ2=Σ1+λ​Var​[Z1∗]​ρ​ρ⊤,\displaystyle\Sigma\_{2}=\Sigma\_{1}+\lambda\text{Var}[Z\_{1}^{\*}]\rho\rho^{\top}, |  |

where ρ=(ρ1,ρ2,ρ3)⊤\rho=(\rho\_{1},\rho\_{2},\rho\_{3})^{\top}.
By the matrix determinant lemma,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |Σ2|=|Σ1+(λ​Var​[Z1∗]​ρ)​ρ⊤|=|Σ1|​(1+λ​Var​[Z1∗]​ρ⊤​Σ1−1​ρ).\displaystyle|\Sigma\_{2}|=|\Sigma\_{1}+(\lambda\text{Var}[Z\_{1}^{\*}]\rho)\rho^{\top}|=|\Sigma\_{1}|\ (1+\lambda\text{Var}[Z\_{1}^{\*}]\rho^{\top}\Sigma\_{1}^{-1}\rho). |  | (A.2) |

We notice that, at fixed time tt, the correlation matrix C​(t)C(t) of stock prices can be calculated using stock price data and be regarded as a constant matrix CC.
Simultaneously, C−1C^{-1} can be also calculated using the same stock price data.
Therefore, we denote C−1=(δi​j)1≤i,j≤3C^{-1}=(\delta\_{ij})\_{1\leq i,j\leq 3}.
By equation ([A.1](https://arxiv.org/html/2510.20047v1#A1.E1 "In Appendix A Appendix: Calculations of |Σ₁| and |Σ₂| ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")), we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | Σ1−1=D−1​C−1​D−1=(δ11(σt1)2δ12σt1​σt2δ13σt1​σt3δ21σt2​σt1δ22(σt2)2δ23σt2​σt3δ31σt3​σt1δ32σt3​σt2δ33(σt3)2).\displaystyle\Sigma\_{1}^{-1}=D^{-1}C^{-1}D^{-1}=\begin{pmatrix}\frac{\delta\_{11}}{(\sigma^{1}\_{t})^{2}}&\frac{\delta\_{12}}{\sigma^{1}\_{t}\sigma^{2}\_{t}}&\frac{\delta\_{13}}{\sigma^{1}\_{t}\sigma^{3}\_{t}}\\ \frac{\delta\_{21}}{\sigma^{2}\_{t}\sigma^{1}\_{t}}&\frac{\delta\_{22}}{(\sigma^{2}\_{t})^{2}}&\frac{\delta\_{23}}{\sigma^{2}\_{t}\sigma^{3}\_{t}}\\ \frac{\delta\_{31}}{\sigma^{3}\_{t}\sigma^{1}\_{t}}&\frac{\delta\_{32}}{\sigma^{3}\_{t}\sigma^{2}\_{t}}&\frac{\delta\_{33}}{(\sigma^{3}\_{t})^{2}}\end{pmatrix}. |  | (A.3) |

Finally, we obtain |Σ2||\Sigma\_{2}| in equation ([4.2](https://arxiv.org/html/2510.20047v1#S4.Ex4 "4.2 Multivariate variance swap using generalized variance method for BNS model ‣ 4 Multivariate swap for Barndorff-Nielsen and Shephard model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")) using ([3.7](https://arxiv.org/html/2510.20047v1#S3.E7 "In 3.2 Multivariate variance swap using generalized variance method for Heston model ‣ 3 Multivariate variance swap for Heston model ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")), ([A.2](https://arxiv.org/html/2510.20047v1#A1.E2 "In Appendix A Appendix: Calculations of |Σ₁| and |Σ₂| ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")), and ([A.3](https://arxiv.org/html/2510.20047v1#A1.E3 "In Appendix A Appendix: Calculations of |Σ₁| and |Σ₂| ‣ Multivariate Variance Swap Using Generalized Variance Method for Stochastic Volatility models")).

## Appendix B Appendix: Summary Statistics

Table 3: Summary statistics of the nine assets.

| Closing Price | Mean | Variance | Kurtosis |
| --- | --- | --- | --- |
| Ko.Close | 0.1095 | 0.0061 | -0.6261 |
| APPL.Close | 1.2061 | 0.0236 | -0.9089 |
| TSLA.Close | 1.0150 | 0.0522 | 0.1955 |
| GOOGL.Close | 1.3819 | 0.0403 | -1.1390 |
| MSFT.Closee | 1.3148 | 0.0343 | -0.8078 |
| META.Close | 0.9457 | 0.0849 | -1.1963 |
| JPM.Close | 1.1330 | 0.0162 | -0.6844 |
| NVDA.Close | 1.8961 | 0.7287 | -0.4353 |
| AMZN.Close | 0.8679 | 0.0297 | -1.1495 |

## References

* [1]
   Ole E Barndorff-Nielsen and Neil Shephard. “Modelling by Lévy processess for financial econometrics”. In: Levy processes: theory and applications (2001), pp. 283-318.
* [2]
   Ole E Barndorff-Nielsen and Neil Shephard. “Non-Gaussian Ornstein–Uhlenbeck-based models and some of their uses in financial economics”. In: Journal of the Royal Statistical Society: Series B (Statistical Methodology) 63.2 (2001), pp. 167-241.
* [3]
   Fred Espen Benth, Martin Groth, and Rodwell Kufakunesu. “Valuing Volatility and Variance Swaps for a Non-Gaussian Ornstein–Uhlenbeck Stochastic Volatility Model”. In: Applied Mathematical Finance 14.4 (2007), pp. 347-363.
* [4]
   Subhojit Biswas and Diganta Mukherjee. “A proposal for multi-asset generalized
  variance swaps”. In: Annals of Financial Economics 14.04 (2019), p. 1950019.
* [5]
   Subhojit Biswas, Diganta Mukherjee, and Indranil SenGupta. “Multi-asset generalized variance swaps in Barndorff-Nielsen and Shephard model”. In: International Journal of Financial Engineering 7.04 (2020), p. 2050051.
* [6]
   Fischer Black and Myron Scholes. “The Pricing of Options and Corporate Liabilities”. In: The Journal of Political Economy 81.3 (1973), pp. 637-654.
* [7]
   Oliver Brockhaus and Douglas Long. “Volatility swaps made simple”. In: RISK-
  LONDON-RISK MAGAZINE LIMITED- 13.1 (2000), pp. 92-95.
* [8]
   Semere Habtemicael, Musie Ghebremichael, and Indranil SenGupta. “Volatility and variance swap using superposition of the Barndorff-Nielsen and Shephard type Lévy processes”. In: Sankhya B 81 (2019), pp. 75-92.
* [9]
   Semere Habtemicael and Indranil Sengupta. “Pricing covariance swaps for Barndorff-Nielsen and Shephard process driven financial markets”. In: Annals of Financial Economics 11.03 (2016), p. 1650012.
* [10]
   Semere Kidane Habtemicael. “Modeling Financial Swaps and Geophysical data Using the Barndorff-Nielsen and Shephard Model”. In: (2015).
* [11]
   Ottó Hajdu. “A New Generalized Variance Approach for Measuring Multidimensional Inequality and Poverty”. In: Social Indicators Research 158.3 (2021), pp. 839-861.
* [12]
   Nobuyuki Ikeda and Shinzo Watanabe. Stochastic differential equations and diffusion processes. Vol. 24. Elsevier, 2014.
* [13]
   Aziz Issaka. “Variance swaps, volatility swaps, hedging and bounds under multifactor Heston stochastic volatility model”. In: Stochastic Analysis and Applications 38.5 (2020), pp. 856-874.
* [14]
   Minglian Lin and Indranil SenGupta. “Analysis of optimal portfolio on finite and small-time horizons for a stochastic volatility market model”. In: SIAM Journal on Financial Mathematics 12.4 (2021), pp. 1596-1624.
* [15]
   Minglian Lin, Indranil SenGupta, and William Wilson. “Estimation of VaR with jump process: Application in corn and soybean markets”. In: Applied Stochastic Models in Business and Industry 40.5 (2024), pp. 1337-1354.
* [16]
   Joakim Marklund and Olle Karlsson. Volatility derivatives–variance and volatility
  swaps. 2015.
* [17]
   Elisa Nicolato and Emmanouil Venardos. “Option pricing in stochastic volatility models of the Ornstein-Uhlenbeck type”. In: Mathematical Finance: An International Journal of Mathematics, Statistics and Financial Economics 13.4 (2003), pp. 445-466.
* [18]
   Jeffrey A. Ryan and Joshua M. Ulrich. quantmod: Quantitative Financial Modelling
  Framework. <https://CRAN.R-project.org/package=quantmod>. R package version 0.4, 2025.
* [19]
   Artur Sepp. “Pricing options on realized variance in the heston model with jumps in returns and volatility-part ii: An approximate distribution of discrete variance”. In: Journal of Computational Finance 16.2 (2012), pp. 3-32.
* [20]
   Anatoliy Swishchuk. “Modeling of variance and volatility swaps for financial markets with stochastic volatilities”. In: WILMOTT magazine 2 (2004), pp. 64-72.
* [21]
   R Core Team. R: A Language and Environment for Statistical Computing. <https://www.r-project.org/>. R Foundation for Statistical Computing, 2025.
* [22]
   Samuel S Wilks. “Certain generalizations in the analysis of variance”. In: Biometrika 24.3/4 (1932), pp. 471-494.