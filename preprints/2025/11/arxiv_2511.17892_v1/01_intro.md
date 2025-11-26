---
authors:
- Xiang Gao
- Cody Hyndman
doc_id: arxiv:2511.17892v1
family_id: arxiv:2511.17892
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM
  Constraints
url_abs: http://arxiv.org/abs/2511.17892v1
url_html: https://arxiv.org/html/2511.17892v1
venue: arXiv q-fin
version: 1
year: 2025
---


Xiang Gao111Department of Mathematics and Statistics,
Concordia University,
1455 Boulevard de Maisonneuve Ouest,
Montréal, Québec,
Canada H3G 1M8.
 and  Cody Hyndman11footnotemark: 1 222Corresponding Author: cody.hyndman@concordia.ca

(November 3, 2025)

###### Abstract

We develop an arbitrage-free deep learning framework for yield curve and bond price forecasting based on the Heath-Jarrow-Morton (HJM) term-structure model and a dynamic Nelson-Siegel parameterization of forward rates. Our approach embeds a no-arbitrage drift restriction into a neural state-space architecture by combining Kalman, extended Kalman, and particle filters with recurrent neural networks (LSTM/CLSTM), and introduces an explicit arbitrage error regularization (AER) term during training. The model is applied to U.S. Treasury and corporate bond data, and its performance is evaluated for both yield-space and price-space predictions at 1-day and 5-day horizons. Empirically, arbitrage regularization leads to its strongest improvements at short maturities, particularly in 5-day-ahead forecasts, increasing market-consistency as measured by bid-ask hit rates and reducing dollar-denominated prediction errors.

Keywords: arbitrage-free modeling, yield curve forecasting, HJM framework, dynamic Nelson–Siegel, Kalman filter, particle filter, neural networks, LSTM, fixed-income term structure.

Mathematics Subject Classification (2000):
Primary: 91G30; Secondary: 65C30, 60H30

## 1 Introduction

No-arbitrage modeling remains central to fixed-income analytics, underpinning the pricing of bonds and term structure derivatives as well as risk management. The Heath–Jarrow–Morton (HJM) framework formalizes this by specifying no-arbitrage conditions for the entire forward-rate curve [[26](https://arxiv.org/html/2511.17892v1#bib.bib26)]. Recent work extends HJM to overnight-rate markets with scheduled jumps, providing tractable arbitrage-free specifications that account for stochastic discontinuities [[21](https://arxiv.org/html/2511.17892v1#bib.bib21)]. In empirical implementations, the Nelson–Siegel (NS) and dynamic Nelson–Siegel (DNS) families [[40](https://arxiv.org/html/2511.17892v1#bib.bib40), [14](https://arxiv.org/html/2511.17892v1#bib.bib14)] offer parsimonious, interpretable representations widely used for forecasting. At the same time, imposing strict no-arbitrage can sometimes degrade predictive accuracy in empirical settings [[8](https://arxiv.org/html/2511.17892v1#bib.bib8)], highlighting a long-standing tension between economic consistency and out-of-sample performance.

A key step toward reconciling this tension is the arbitrage-regularization framework of Kratsios and Hyndman [[34](https://arxiv.org/html/2511.17892v1#bib.bib34)], which learns the *closest* arbitrage-free model to a given factor model within a generalized HJM setting by augmenting the learning objective with an arbitrage penalty. Specializing to term structure models, they derive a tractable penalty and show how to implement it with neural networks, providing a principled machine-learning route to no-arbitrage. Our approach is directly inspired by Kratsios and Hyndman [[34](https://arxiv.org/html/2511.17892v1#bib.bib34)]: we operationalize arbitrage-regularization as a training penalty in a filter-based deep sequence-forecasting architecture and evaluate horizon- and maturity-specific gains.

Recent advances in machine learning (ML) complement parametric term structure models. Deep architectures have been developed for multi-curve forecasting, including interval/quantile predictions [[46](https://arxiv.org/html/2511.17892v1#bib.bib46)], for yield-curve extrapolation at long maturities [[1](https://arxiv.org/html/2511.17892v1#bib.bib1)], and for DNS-style structures embedded within neural networks [[35](https://arxiv.org/html/2511.17892v1#bib.bib35), [31](https://arxiv.org/html/2511.17892v1#bib.bib31)]. Parallel work refines DNS with time-varying decay parameters, conditional heteroskedasticity, and macroeconomic factors [[7](https://arxiv.org/html/2511.17892v1#bib.bib7)], while tree-based regime switching layered on DNS captures macroeconomic state dependence [[3](https://arxiv.org/html/2511.17892v1#bib.bib3)]. To address interpretability, explainable deep models such as LSTM–LagLasso deliver competitive bond-yield forecasts [[41](https://arxiv.org/html/2511.17892v1#bib.bib41)]. In environments with policy constraints, smooth shadow-rate DNS variants extend DNS to zero-lower bound (ZLB) or effective lower bound (ELB) regimes while preserving its attractive structure [[42](https://arxiv.org/html/2511.17892v1#bib.bib42)]. For multi-curve settings more broadly, recent geometric results characterize consistency and conditions for finite-dimensional realizations in HJM [[23](https://arxiv.org/html/2511.17892v1#bib.bib23)], offering guidance for factor design across curves.

A parallel line of research integrates arbitrage considerations directly into ML objectives. In option pricing and volatility modelling, arbitrage-aware generators produce risk-neutral or arbitrage-free surfaces by design, including risk-neutral generative networks and arbitrage-free volatility generators [[50](https://arxiv.org/html/2511.17892v1#bib.bib50), [49](https://arxiv.org/html/2511.17892v1#bib.bib49)]. For interest rates, recent risk-neutral autoencoder approaches model the forward-rate manifold under no-arbitrage [[38](https://arxiv.org/html/2511.17892v1#bib.bib38), [39](https://arxiv.org/html/2511.17892v1#bib.bib39)]. Relatedly, real-world (physical-measure) HJM formulations analyze market viability and local-martingale deflators across multiple term structures [[22](https://arxiv.org/html/2511.17892v1#bib.bib22)], while roll-over risk has been modeled via stochastic control to endogenously generate spreads even outside the classical no-arbitrage paradigm [[20](https://arxiv.org/html/2511.17892v1#bib.bib20)]. Looking forward, data-driven (neural) HJM schemes aim at arbitrage-consistent curve generation and forecasting, including scheduled jumps [[11](https://arxiv.org/html/2511.17892v1#bib.bib11)].

Hybrid filtering–and–learning designs have likewise matured. Classical Kalman, extended Kalman, and particle filters remain effective for sequential state estimation and can be fused with learned components to capture nonlinearities and time variation. Recent neural-augmented filters such as KalmanNet [[45](https://arxiv.org/html/2511.17892v1#bib.bib45)] and Bayesian KalmanNet [[13](https://arxiv.org/html/2511.17892v1#bib.bib13)] demonstrate how deep networks can assist or replace parts of the state-space framework while preserving the inductive bias of filtering. This perspective directly motivates our use of filter-based recurrent neural networks (RNNs) to learn dynamic parameters and latent factors while maintaining a transparent state-space backbone. These results highlight the importance of enforcing financial structure within deep learning architectures for fixed-income forecasting.

#### Contributions:

We combine filter-based sequential models with deep learning and enforce no-arbitrage via an explicit training penalty, then evaluate horizon- and maturity-specific gains on U.S. Treasuries and corporate bonds. Our contributions are:

* •

  Arbitrage metric and training signal. We operationalize no-arbitrage via the *Accumulated Excess Return (AER)* penalty Λ​(p)\Lambda(p) on a fixed tenor grid, using it both as a training regularizer and an ex post diagnostic.
* •

  Price-space and yield-space forecasting. We forecast *prices* directly (EKF/PF) and *yields* (KF), comparing pathways and trade-offs.
* •

  Architecture for dynamic parameters. A convolutional-LSTM compresses per-bond panels and a residual LSTM learns time-varying observation noise, enabling end-to-end learning of (κ,θ,σ)(\kappa,\theta,\sigma) within a filter-based RNN.
* •

  Robust errors and stable PF. We model observation errors with multivariate generalized Gaussian noise and use EKF-assisted importance sampling with systematic resampling.
* •

  Headline empirical finding. Arbitrage-regularization delivers the largest gains at the short end (notably 5-day-ahead), materially improving bid–ask hit rates while maintaining competitive MAE/RMSPE.
* •

  Practical implementation. Differentiable KF/EKF/PF components are implemented for end-to-end training, with guidance on accuracy–runtime trade-offs.
* •

  Scope. In corporate-bond experiments, credit is absorbed into the latent state (rather than modeling a separate spread factor ξt\xi\_{t}), focusing on arbitrage-consistent rate dynamics.

#### Organization:

Section [2](https://arxiv.org/html/2511.17892v1#S2 "2 Arbitrage-free pricing framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") presents the arbitrage-free pricing framework and its DNS realization. Section [3](https://arxiv.org/html/2511.17892v1#S3 "3 Forecasting framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") details our Kalman, extended Kalman, and particle filter forecasting schemes. Section [4](https://arxiv.org/html/2511.17892v1#S4 "4 Dynamic parameterization by Recurrent Neural Networks ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") introduces the deep architecture for dynamic parameterization and arbitrage-aware training. Section [5](https://arxiv.org/html/2511.17892v1#S5 "5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") reports empirical results and robustness checks; Section [6](https://arxiv.org/html/2511.17892v1#S6 "6 Conclusion ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") concludes. An appendix contains technical implementation details.

## 2 Arbitrage-free pricing framework

The no-arbitrage term structure literature builds upon the theoretical structure introduced by Heath et al. [[26](https://arxiv.org/html/2511.17892v1#bib.bib26)]. Ang and Piazzesi [[2](https://arxiv.org/html/2511.17892v1#bib.bib2)] studied affine no-arbitrage term structure models which preclude arbitrage opportunities between the dynamic evolution of the yield curve factors and the yields at different maturity segments. Interest rate forecasting as in Diebold and Li [[14](https://arxiv.org/html/2511.17892v1#bib.bib14)] shows good out-of-sample performance using the no-arbitrage approach. Christensen et al. [[8](https://arxiv.org/html/2511.17892v1#bib.bib8)] demonstrates that the no-arbitrage approach downgrades the performance when the model is restricted to preclude arbitrage opportunities.

### 2.1 HJM forward rate model

The HJM framework specifies the joint evolution of the entire forward-rate curve so that discounted bond prices are martingales, providing an economically consistent starting point for forecasting and pricing. The Heath-Jarrow-Morton (HJM) model [[26](https://arxiv.org/html/2511.17892v1#bib.bib26)] provides a powerful framework in modeling instantaneous forward rates and fixed income assets in an arbitrage-free setting. The theoretical form of the HJM model allows infinite-dimensional combinations of risk factors while finite-dimensional representations or projections lead to implementable models. Given that affine term-structure is widely applied in dynamic models, we consider finite-dimensional affine structure and the arbitrage-free condition under the risk-neutral measure ℚ\mathbb{Q}

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​f​(t,τ)=μ​(t,τ)​d​t+∑i=1dηi​(t,τ)​d​Wi​(t),df\left(t,\tau\right)=\mu\left(t,\tau\right)dt+\sum\_{i=1}^{d}\eta\_{i}\left(t,\tau\right)dW\_{i}(t), |  | (2.1) |

where τ\tau is the tenor from time tt to maturity TT, Wi​(t)W\_{i}(t) for i=1,2,…,di=1,2,\dots,d are independent standard Brownian motions, μ∈ℝ\mu\in\mathbb{R} is the drift term and ηi∈ℝ\eta\_{i}\in\mathbb{R} for i=1,2,…,di=1,2,\dots,d are risk factors. Intuitively, the model represents the entire forward curve as a small set of latent risk factors with loadings that vary by maturity, and rules out arbitrage by ensuring the expected excess return of any zero-coupon bond is zero. We assume that ([2.1](https://arxiv.org/html/2511.17892v1#S2.E1 "In 2.1 HJM forward rate model ‣ 2 Arbitrage-free pricing framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints")) is separable in tt and τ\tau and has a finite-dimensional representation by the following affine structure

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(t,τ)=βτ​Xt,f(t,\tau)=\beta\_{\tau}X\_{t}, |  | (2.2) |

for a deterministic loading parameter βτ∈ℝ1×d\beta\_{\tau}\in\mathbb{R}^{1\times d} and a dynamic process Xt∈ℝd×1X\_{t}\in\mathbb{R}^{d\times 1} containing the risk factors. We assume the loading parameter is chosen such that the corresponding yield curves are in the class of Nelson-Siegel term structure models and risk arises only from the time varying process XtX\_{t}.

Next, we determine the realization of the forward rate process in finite space and the specification of the volatility term.
Finite-dimensional realizations require the drift and volatility to lie in the tangent space of the forward-rate manifold (see Björk and Svensson). Different volatility specifications recover familiar models (e.g., Ho–Lee with constant volatility, Hull–White with exponentially decaying volatility). Empirically, Principal Component Analysis (PCA) reveals that three factors explain most variation in U.S. yields (see, e.g., [[36](https://arxiv.org/html/2511.17892v1#bib.bib36)]).
The first factor (’level’) accounts for 80–90% of variation; the second (’slope’) moves short and long rates in opposite directions and explains most of the remainder; the third (’curvature’) captures hump-shaped movements.
Therefore, we consider a three-factor model for XtX\_{t} with cross-variable interaction instead of independent variables.
For overnight-rate and multi-curve markets, recent HJM extensions incorporate scheduled jumps and multiple term structures while retaining no-arbitrage (e.g., [[21](https://arxiv.org/html/2511.17892v1#bib.bib21), [23](https://arxiv.org/html/2511.17892v1#bib.bib23)]); our single-curve setup follows the classic HJM tradition but the forecasting ideas carry over.

Calibration of the forward rate model requires that the initial forward curve is based off on empirically observed forward rates. We implement the calibration under a machine learning framework where the observations may be sequentially batched into many subsets.
In the following section, we introduce the loading parameter βτ\beta\_{\tau} in exponential space and specify the risk variable XtX\_{t} as a mean-reverting process which we test in a later section. We define XtX\_{t} as extended Vašíček process

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Xt=κt​(θt−Xt)​d​t+σt​d​Wt,dX\_{t}=\kappa\_{t}\left(\theta\_{t}-X\_{t}\right)dt+\sigma\_{t}dW\_{t}, |  | (2.3) |

where κt\kappa\_{t}, θt\theta\_{t} and σt\sigma\_{t} are functions which depend on XtX\_{t}. Equation ([2.3](https://arxiv.org/html/2511.17892v1#S2.E3 "In 2.1 HJM forward rate model ‣ 2 Arbitrage-free pricing framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints")) is the factor model and the risk factor XtX\_{t} is the state variable. The dynamics of the forward rate model ff defined in ([2.2](https://arxiv.org/html/2511.17892v1#S2.E2 "In 2.1 HJM forward rate model ‣ 2 Arbitrage-free pricing framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints")) with state variable XtX\_{t} defined in ([2.3](https://arxiv.org/html/2511.17892v1#S2.E3 "In 2.1 HJM forward rate model ‣ 2 Arbitrage-free pricing framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints")) is also mean-reverting process

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​f​(t,τ)=\displaystyle df(t,\tau)= | −d​βτd​τ​Xt​d​t+βτ​d​Xt=κ¯​(t,τ)​(θ¯​(t,τ)−Xt)​d​t+σt​βτ​d​Wt,\displaystyle-\frac{d\beta\_{\tau}}{d\tau}X\_{t}dt+\beta\_{\tau}dX\_{t}=\bar{\kappa}(t,\tau)\left(\bar{\theta}(t,\tau)-X\_{t}\right)dt+\sigma\_{t}\beta\_{\tau}dW\_{t}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | κ¯​(t,τ)=(βτ​κt+d​βτd​τ),and ​θ¯​(t,τ)=(βτ​κt+d​βτd​τ)−1​βτ​κt​θt.\bar{\kappa}(t,\tau)=\left(\beta\_{\tau}\kappa\_{t}+\frac{d\beta\_{\tau}}{d\tau}\right),\ \mbox{and }\ \bar{\theta}(t,\tau)=\left(\beta\_{\tau}\kappa\_{t}+\frac{d\beta\_{\tau}}{d\tau}\right)^{-1}\beta\_{\tau}\kappa\_{t}\theta\_{t}. |  |

From the affine forward rate specification ([2.2](https://arxiv.org/html/2511.17892v1#S2.E2 "In 2.1 HJM forward rate model ‣ 2 Arbitrage-free pricing framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints")) we obtain the short rate

|  |  |  |
| --- | --- | --- |
|  | r​(t)=β0​Xt,r\left(t\right)=\beta\_{0}X\_{t}, |  |

and the value of zero-coupon bond P​V​(t,τ)PV(t,\tau) which pays one dollar at time T=t+τT=t+\tau is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​V​(t,τ)=exp⁡(−∫0τf​(t,s)​𝑑s)=exp⁡(−Bτ​Xt),PV(t,\tau)=\exp\left(-\int\_{0}^{\tau}f(t,s)ds\right)=\exp\left(-B\_{\tau}X\_{t}\right), |  | (2.4) |

where Bτ=∫0τβu​𝑑uB\_{\tau}=\int\_{0}^{\tau}\beta\_{u}du.

We denote by Λ​(t,τ)\Lambda(t,\tau) the instantaneous excess return of a τ\tau-maturity zero-coupon bond over the money-market account. No-arbitrage requires Λ​(t,τ)=0\Lambda(t,\tau)=0 for all maturities.
The relative bond price

|  |  |  |
| --- | --- | --- |
|  | Z​(t,τ)=−exp⁡(∫0tr​(s)​𝑑s)​P​V​(t,τ)Z\left(t,\tau\right)={-\exp{\left(\int\_{0}^{t}r(s)ds\right)}}{PV(t,\tau)} |  |

representing the bond’s excess value over the risk-free investment follows the dynamics

|  |  |  |
| --- | --- | --- |
|  | d​Z​(t,τ)=Λ​(t,τ)​Z​(t,τ)​d​t−σt​Bτ​Z​(t,τ)​d​Wt,{dZ\left(t,\tau\right)}=\Lambda\left(t,\tau\right){Z\left(t,\tau\right)}dt-\sigma\_{t}B\_{\tau}{Z\left(t,\tau\right)}dW\_{t}, |  |

where
Λ​(t,τ)=12​Bτ​Σt​Bτ⊤−Bτ​κt​(θt−Xt)+(βτ−β0)​Xt\Lambda\left(t,\tau\right)=\frac{1}{2}B\_{\tau}\Sigma\_{t}B^{\top}\_{\tau}-B\_{\tau}\kappa\_{t}\left(\theta\_{t}-X\_{t}\right)+\left(\beta\_{\tau}-\beta\_{0}\right)X\_{t}
and
Σt=σt​σt⊤.\Sigma\_{t}=\sigma\_{t}\sigma\_{t}^{\top}.
Building on the arbitrage-regularization approach of Kratsios and Hyndman [[34](https://arxiv.org/html/2511.17892v1#bib.bib34)], we later penalize deviations of Λ​(t,τ)\Lambda(t,\tau) from zero over a fixed tenor grid. Note that Λ​(t,τ)\Lambda\left(t,\tau\right) defines the instantaneous excess return on the bond above the risk free rate and Heath et al. [[26](https://arxiv.org/html/2511.17892v1#bib.bib26)] proves that there exists a unique market price of risk such that the forward rate model is arbitrage-free. Therefore, the condition Λ​(t,τ)=0\Lambda\left(t,\tau\right)=0 determines risk neutral pricing measure and precludes arbitrage opportunities. We summarize these facts in the following theorem.

###### Theorem 2.1.

Suppose the forward rate model has an affine structure given by f​(t,τ)=βτ​Xtf(t,\tau)=\beta\_{\tau}X\_{t}
and a mean-reverting state variable defined by

|  |  |  |
| --- | --- | --- |
|  | d​Xt=κt​(θt−Xt)​d​t+σt​d​Wt,dX\_{t}=\kappa\_{t}\left(\theta\_{t}-X\_{t}\right)dt+\sigma\_{t}dW\_{t}, |  |

where βτ∈ℝ1×d\beta\_{\tau}\in\mathbb{R}^{1\times d}, Xt∈ℝd×1X\_{t}\in\mathbb{R}^{d\times 1},
κt​(Xt):ℝd×1→ℝd×d\kappa\_{t}\left(X\_{t}\right):\mathbb{R}^{d\times 1}\rightarrow\mathbb{R}^{d\times d},
θt​(Xt):ℝd×1→ℝd×1\theta\_{t}\left(X\_{t}\right):\mathbb{R}^{d\times 1}\rightarrow\mathbb{R}^{d\times 1}, and
σt​(Xt):ℝd×1→ℝd×d\sigma\_{t}\left(X\_{t}\right):\mathbb{R}^{d\times 1}\rightarrow\mathbb{R}^{d\times d}.
If, for all t≥0t\geq 0 and τ≥0\tau\geq 0, the equation

|  |  |  |
| --- | --- | --- |
|  | Λ​(t,τ)=12​Bτ​Σt​Bτ⊤−Bτ​κt​(θt−Xt)+(βτ−β0)​Xt=0\Lambda(t,\tau)=\frac{1}{2}B\_{\tau}\Sigma\_{t}B^{\top}\_{\tau}-B\_{\tau}\kappa\_{t}\left(\theta\_{t}-X\_{t}\right)+\left(\beta\_{\tau}-\beta\_{0}\right)X\_{t}=0 |  |

holds, then f​(t,τ)f(t,\tau) is an arbitrage-free forward rate model under risk-neutral measure ℚ\mathbb{Q}.

The following is a standard result in stochastic calculus which we use to obtain our discretized model.

###### Proposition 2.2.

Suppose XtX\_{t} evolves as mean-reverting process with time-dependent parameter given by equation ([2.3](https://arxiv.org/html/2511.17892v1#S2.E3 "In 2.1 HJM forward rate model ‣ 2 Arbitrage-free pricing framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints")). Then ([2.3](https://arxiv.org/html/2511.17892v1#S2.E3 "In 2.1 HJM forward rate model ‣ 2 Arbitrage-free pricing framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints")) with initial condition X0X\_{0} has a unique solution XtX\_{t} given by

|  |  |  |
| --- | --- | --- |
|  | Xt=e−∫0tκu​𝑑u​X0+∫0te−∫utκv​𝑑v​κu​θu​𝑑u+∫0te−∫utκv​𝑑v​σu​𝑑Wu,X\_{t}=e^{-\int\_{0}^{t}\kappa\_{u}du}X\_{0}+\int\_{0}^{t}e^{-\int\_{u}^{t}\kappa\_{v}dv}\kappa\_{u}\theta\_{u}du+\int\_{0}^{t}e^{-\int\_{u}^{t}\kappa\_{v}dv}\sigma\_{u}dW\_{u}, |  |

where the mean and variance of XtX\_{t} are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​[XT|ℱt]\displaystyle\mathbb{E}\left[X\_{T}|\mathcal{F}\_{t}\right] | =e−∫tTκu​𝑑u​Xt+∫tTe−∫uTκv​𝑑v​κu​θu​𝑑u,\displaystyle=e^{-\int\_{t}^{T}\kappa\_{u}du}X\_{t}+\int\_{t}^{T}e^{-\int\_{u}^{T}\kappa\_{v}dv}\kappa\_{u}\theta\_{u}du, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Var​[XT|ℱt]\displaystyle\text{Var}\left[X\_{T}|\mathcal{F}\_{t}\right] | =∫tTe−∫uTκv​𝑑v​Σu​e−∫uTκv⊤​𝑑v​𝑑u.\displaystyle=\int\_{t}^{T}e^{-\int\_{u}^{T}\kappa\_{v}dv}\Sigma\_{u}e^{-\int\_{u}^{T}\kappa\_{v}^{\top}dv}du. |  |

### 2.2 Dynamic Nelson-Siegel term structure

We specialize the HJM loading to the Nelson–Siegel family, which represents forward and yield curves via three economically interpretable factors—level (long-run rate), slope (short-long differential), and curvature (medium-term hump). This three-factor structure aligns with classic PCA evidence in U.S. yields, where a parallel shift (level), steepness (slope), and curvature account for the vast majority of variation [[36](https://arxiv.org/html/2511.17892v1#bib.bib36)].

Choosing different loading parameters βτ\beta\_{\tau}, we can generate forward rate curves by ([2.2](https://arxiv.org/html/2511.17892v1#S2.E2 "In 2.1 HJM forward rate model ‣ 2 Arbitrage-free pricing framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints")) that give different shapes of the term structure. Similar to the prediction framework introduced by Diebold et al. [[15](https://arxiv.org/html/2511.17892v1#bib.bib15), [16](https://arxiv.org/html/2511.17892v1#bib.bib16)], where they introduced the dynamic Nelson-Siegel term structure and modeled the factors using auto-regressive processes, we apply dynamic Nelson-Siegel term structure within the framework of the arbitrage-free forward rate model. We define the loading parameter βτ\beta\_{\tau} as a three-dimensional vector basis for some constant λ∈ℝ+\lambda\in\mathbb{R}^{+} by

|  |  |  |
| --- | --- | --- |
|  | βτ=(β1​(τ),β2​(τ),β3​(τ))=(1,e−λ​τ,λ​τ​e−λ​τ),\beta\_{\tau}=\left(\beta\_{1}(\tau),\beta\_{2}(\tau),\beta\_{3}(\tau)\right)=\left(1,\,e^{-\lambda\tau},\,\lambda\tau e^{-\lambda\tau}\right), |  |

In this d=3d=3–dimensional parameterization of the forward rate, the factors Xt=(X1​(t),X2​(t),X3​(t))⊤X\_{t}=(X\_{1}(t),X\_{2}(t),X\_{3}(t))^{\top} control the long-run level X1​(t)X\_{1}(t), the short-versus-long-rate slope X2​(t)X\_{2}(t), and the localized curvature X3​(t)X\_{3}(t), giving the DNS model its interpretability for policy and risk applications. The Nelson–Siegel term structure space NS​(τ)\mathrm{NS}(\tau) is spanned by the exponential-polynomial basis βτ\beta\_{\tau} with decay parameter λ\lambda,

|  |  |  |
| --- | --- | --- |
|  | 𝒩​𝒮​(τ)=Span​{(1,e−λ​τ,λ​τ​e−λ​τ)|for some ​λ∈ℝ+}.\mathcal{NS}(\tau)=\text{Span}\left\{\left.\left(1,~e^{-\lambda\tau},~\lambda\tau e^{-\lambda\tau}\right)\right|\text{for some }\lambda\in\mathbb{R}^{+}\right\}. |  |

As shown by Björk and Svensson [[4](https://arxiv.org/html/2511.17892v1#bib.bib4)], as long as the drift and volatility of the forward rate process lie in 𝒩​𝒮​(τ)\mathcal{NS}(\tau), whose tangent space is itself, then the forward rate process will evolve in 𝒩​𝒮​(τ)\mathcal{NS}(\tau). For some three-dimensional state vector Xt=(X1​(t),X2​(t),X3​(t))⊤X\_{t}=\left(X\_{1}(t),~X\_{2}(t),~X\_{3}(t)\right)^{\top}, the forward rate model f​(t,τ)∈𝒩​𝒮​(τ)f(t,\tau)\in\mathcal{NS}(\tau)

|  |  |  |
| --- | --- | --- |
|  | f​(t,τ)=βτ​Xt=X1​(t)+e−λ​τ​X2​(t)+λ​τ​e−λ​τ​X3​(t),f(t,\tau)=\beta\_{\tau}X\_{t}=X\_{1}(t)+e^{-\lambda\tau}X\_{2}(t)+\lambda\tau e^{-\lambda\tau}X\_{3}(t), |  |

defines the dynamic Nelson-Siegel yield model with the zero-coupon bond yields given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | y​(t,τ)=−log⁡PV​(t,τ)τ=Bττ​Xt=X1​(t)+X2​(t)​(1−e−λ​τλ​τ)+X3​(t)​(1−e−λ​τλ​τ−e−λ​τ),y(t,\tau)=-\frac{\log\text{PV}(t,\tau)}{\tau}=\frac{B\_{\tau}}{\tau}X\_{t}=X\_{1}(t)+X\_{2}(t)\left(\frac{1-e^{-\lambda\tau}}{\lambda\tau}\right)+X\_{3}(t)\left(\frac{1-e^{-\lambda\tau}}{\lambda\tau}-e^{-\lambda\tau}\right), |  | (2.5) |

where

|  |  |  |
| --- | --- | --- |
|  | Bτ=∫0τβu​𝑑u=(τ,1−e−λ​τλ,1−e−λ​τλ−τ​e−λ​τ)B\_{\tau}=\int\_{0}^{\tau}\beta\_{u}du=\left(\tau,\frac{1-e^{-\lambda\tau}}{\lambda},\frac{1-e^{-\lambda\tau}}{\lambda}-\tau e^{-\lambda\tau}\right) |  |

are the factor loadings.
In empirical studies of the time series of yields, using the above factor loadings, as in Diebold and Li [[14](https://arxiv.org/html/2511.17892v1#bib.bib14)], avoids the multicollinearity present in the original Nelson and Siegel [[40](https://arxiv.org/html/2511.17892v1#bib.bib40)] specification.
The term structure space can be expanded to include additional loading terms and different decay parameters so that we can also interpret the forward rate process as the Svensson [[48](https://arxiv.org/html/2511.17892v1#bib.bib48)] term structure model with four state variables:

|  |  |  |
| --- | --- | --- |
|  | 𝒮​𝒱​(τ)=Span​{(1,e−λ1​τ,λ1​τ​e−λ1​τ,λ2​τ​e−λ2​τ)|for some ​λ1,λ2∈ℝ+}.\mathcal{SV}(\tau)=\text{Span}\left\{\left.\left(1,~e^{-\lambda\_{1}\tau},~\lambda\_{1}\tau e^{-\lambda\_{1}\tau},~\lambda\_{2}\tau e^{-\lambda\_{2}\tau}\right)\right|\text{for some }\lambda\_{1},\lambda\_{2}\in\mathbb{R}^{+}\right\}. |  |

Allowing time-varying or multiple decay parameters can improve fit and forecasts, as in [[7](https://arxiv.org/html/2511.17892v1#bib.bib7)]), but we retain a constant decay parameter λ\lambda for parsimony.

In order to preclude arbitrage opportunities in the dynamic Nelson-Siegel yield model ([2.5](https://arxiv.org/html/2511.17892v1#S2.E5 "In 2.2 Dynamic Nelson-Siegel term structure ‣ 2 Arbitrage-free pricing framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints")) Theorem [2.1](https://arxiv.org/html/2511.17892v1#S2.Thmtheorem1 "Theorem 2.1. ‣ 2.1 HJM forward rate model ‣ 2 Arbitrage-free pricing framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") requires Λ​(t,τ)=0\Lambda(t,\tau)=0 for all t≥0t\geq 0 and τ≥0\tau\geq 0. Intuitively, Λ​(t,τ)\Lambda(t,\tau) is the model-implied instantaneous excess return of a bond over the risk-free benchmark. Because the set of observed maturities changes from day to day, evaluating Λ​(t,τ)\Lambda(t,\tau) only at those maturities yields a time-varying objective. We therefore fix a tenor grid from 3 months to 30 years and define the accumulated excess return (AER) penalty as the time–tenor average pp-norm of Λ​(t,τ)\Lambda(t,\tau) over this grid:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λ(p)=1n​∑i=1n‖Λ​(t)​(ti,Tj)‖p=1n​∑i=1n(1m​∑j=1m|Λ​(t)​(ti,Tj)|p)1p.\Lambda^{(p)}=\frac{1}{n}\sum\_{i=1}^{n}\left\|\Lambda(t)(t\_{i},T\_{j})\right\|\_{p}=\frac{1}{n}\sum\_{i=1}^{n}\left({\frac{1}{m}\sum\_{j=1}^{m}\left|\Lambda(t)(t\_{i},T\_{j})\right|^{p}}\right)^{\frac{1}{p}}. |  | (2.6) |

We use AER both during training as a regularizer and, ex post, as a diagnostic of arbitrage consistency [[34](https://arxiv.org/html/2511.17892v1#bib.bib34)].
When p=2p=2 the AER quantifies the average over the set of days tit\_{i} the root mean square (RMS) distance of the objectives (yields or prices) to the arbitrage-free values over the selected maturities TjT\_{j} for i=1,…,ni=1,\ldots,n and j=1,…,mj=1,\ldots,m.

Moving from risk-free bond prices or yields to corporate bond prices or yields requires additional modelling of credit risk. Although reduced-form credit spreads ξt\xi\_{t} can be added explicitly (e.g., see Ejsing et al. [[19](https://arxiv.org/html/2511.17892v1#bib.bib19)]), in our corporate-bond prediction applications we shall absorb credit into the latent state for tractability.
That is, since our interest is to study the arbitrage-free pricing and forecasting problem, we simply assume the dd risk factors XtX\_{t} include credit risk when we apply the model to corporate data instead of modeling it separately. This keeps the focus on arbitrage-consistent rate dynamics while allowing issuer-level heterogeneity to load through XtX\_{t}.

Next, we consider the application of the affine term structure in pricing coupon bonds. Assume the coupon bond periodically pays cic\_{i} at time τi\tau\_{i} up to mm total payments and has value Y​(t,τ)Y(t,\tau) given by the arbitrage-free Nelson-Siegel model ([2.5](https://arxiv.org/html/2511.17892v1#S2.E5 "In 2.2 Dynamic Nelson-Siegel term structure ‣ 2 Arbitrage-free pricing framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints"))

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y^​(t,τ)=∑i=1mci​e−τi​y​(τi)=∑i=1mci​e−Bτi​Xt.\hat{Y}(t,\tau)=\sum\_{i=1}^{m}c\_{i}e^{-\tau\_{i}y\left(\tau\_{i}\right)}=\sum\_{i=1}^{m}c\_{i}e^{-B\_{\tau\_{i}}X\_{t}}. |  | (2.7) |

From equation ([2.7](https://arxiv.org/html/2511.17892v1#S2.E7 "In 2.2 Dynamic Nelson-Siegel term structure ‣ 2 Arbitrage-free pricing framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints")), we can extract the yield curve and the state variables from observations. The observations that we used are the daily closing bond prices. We choose the coupon bonds whose tenors are greater than 3 months and less than 30 years. The state variable XtX\_{t} can be extracted by minimizing the mean square error (MSE) between the observation YY and the model value Y^\hat{Y}

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xt=arg​minXt∈ℝd⁡1n​∑i=1n|Y​(t,τi)−Y^​(t,τi)|2,X\_{t}=\operatorname\*{arg\,min}\_{X\_{t}\in\mathbb{R}^{d}}\frac{1}{n}\sum\_{i=1}^{n}\left|Y(t,\tau\_{i})-\hat{Y}(t,\tau\_{i})\right|^{2}, |  | (2.8) |

using standard methods such as linear estimators with smoothing penalties. This DNS parameterization provides a finite-dimensional HJM realization, enabling direct enforcement of arbitrage constraints via Λ​(t,τ)\Lambda(t,\tau).

### 2.3 Data and estimation result

Raw data were obtained from FINRA-TRACE supplemented by proprietary Treasury data feed from a commercial vendor. Our data comprise daily clean prices, yields to maturity, coupon rates/frequencies, instrument type, convertibility/callability flags, and issue/maturity dates for U.S. Treasuries and corporate bonds from 2017–2019. We retain fixed-coupon, non-callable, non-convertible bonds with remaining time-to-maturity between 3 months and 30 years, yield-to-maturity under 700 bps, and an absolute YTM–coupon difference under 500 bps.
Because the cross-section varies by day, we sample a fixed panel per day balanced across tenor buckets: approximately 14 short-term (0–2 year) maturity, 45 medium-term (2–10 years), and 9 long-term (10–30 y) Treasuries. Trading dates with insufficient observations are dropped, amounting to approximately 1–3We select the decay parameter λ\lambda by a grid search minimizing out-of-sample RMSE over a rolling validation window and keep it fixed across the sample for stability. We then fit the daily coupon bonds using the Nelson-Siegel model ([2.5](https://arxiv.org/html/2511.17892v1#S2.E5 "In 2.2 Dynamic Nelson-Siegel term structure ‣ 2 Arbitrage-free pricing framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints")) to obtain the state variables of Xi​(t)X\_{i}(t) for i=1,2,3i=1,2,3 with the optimal value of decay parameter fixed at λ=0.4488779759\lambda=0.4488779759. Figure [2.2](https://arxiv.org/html/2511.17892v1#S2.F2 "Figure 2.2 ‣ 2.3 Data and estimation result ‣ 2 Arbitrage-free pricing framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") shows the yield surface and Figure [2.2](https://arxiv.org/html/2511.17892v1#S2.F2 "Figure 2.2 ‣ 2.3 Data and estimation result ‣ 2 Arbitrage-free pricing framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") shows the paths of three state variables.

Figure 2.1: Treasury yield curves from 2017 to 2019

![Refer to caption](x1.png)

Figure 2.2: State variables of Treasury from 2017 to 2019

![Refer to caption](x2.png)




Table 2.1: U.S. Treasuries yields (in %\%)

| date | 3M | 6M | 9M | 12M | 15M | 18M | … | 120M | 180M | 240M | 300M | 360M |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1/9/2017 | 0.735 | 0.822 | 0.906 | 0.987 | 1.066 | 1.143 | … | 2.532 | 2.798 | 2.938 | 3.024 | 3.081 |
| 1/10/2017 | 0.648 | 0.745 | 0.839 | 0.929 | 1.016 | 1.100 | … | 2.541 | 2.806 | 2.946 | 3.031 | 3.088 |
| 1/11/2017 | 0.672 | 0.768 | 0.861 | 0.950 | 1.035 | 1.117 | … | 2.535 | 2.794 | 2.932 | 3.015 | 3.071 |
| 1/12/2017 | 0.695 | 0.785 | 0.873 | 0.958 | 1.039 | 1.118 | … | 2.531 | 2.797 | 2.939 | 3.024 | 3.082 |
| 1/13/2017 | 0.702 | 0.791 | 0.879 | 0.963 | 1.045 | 1.124 | … | 2.547 | 2.817 | 2.960 | 3.047 | 3.105 |
| … |  |  |  |  |  |  |  |  |  |  |  |  |




Table 2.2: Statistics of state variables

| Factor | Mean | Std | Min. | Max. | Correlation | | | ADF | P-value |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X1​(t)X\_{1}(t) | 0.03120 | 0.0030 | 0.0221 | 0.0362 | 1 | -0.541 | 0.430 | -1.601 | 0.483 |
| X2​(t)X\_{2}(t) | -0.0098 | 0.0093 | -0.0310 | 0.0041 | - | 1 | -0.353 | -2.345 | 0.157 |
| X3​(t)X\_{3}(t) | -0.0163 | 0.0111 | -0.0366 | 0.0049 | - | - | 1 | -1.321 | 0.619 |

Table [2.1](https://arxiv.org/html/2511.17892v1#S2.T1 "Table 2.1 ‣ 2.3 Data and estimation result ‣ 2 Arbitrage-free pricing framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") presents the daily yields data extracted from the U.S. Treasuries data set. Table [2.2](https://arxiv.org/html/2511.17892v1#S2.T2 "Table 2.2 ‣ 2.3 Data and estimation result ‣ 2 Arbitrage-free pricing framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") shows the backtested result of the state variables using the Augmented Dickey-Fuller (ADF) test to validate the mean-reversion assumption. ADF test statistics and p-values do not reject a unit root in X​(t)X(t), indicating non-stationarity in levels. However, over finite forecasting horizons, locally mean-reverting dynamics remain a reasonable approximation. This assumption is sufficient for the sequential filtering procedures employed in the following sections.

## 3 Forecasting framework

This section presents three sequential filtering approaches for forecasting bond yields and prices given model parameters (κt,θt,σt)\left(\kappa\_{t},\theta\_{t},\sigma\_{t}\right). Section [3.1](https://arxiv.org/html/2511.17892v1#S3.SS1 "3.1 Yield forecasting using the Kalman filter ‣ 3 Forecasting framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") treats yields with a linear state–space model and the Kalman filter (KF). Sections [3.2](https://arxiv.org/html/2511.17892v1#S3.SS2 "3.2 Price forecasting using the extended Kalman filter ‣ 3 Forecasting framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints")-[3.3](https://arxiv.org/html/2511.17892v1#S3.SS3 "3.3 Price forecasting using the particle filter ‣ 3 Forecasting framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") forecast bond prices with nonlinear filters, the extended Kalman filter (EKF) and a particle filter (PF). We then outline how Section [4](https://arxiv.org/html/2511.17892v1#S4 "4 Dynamic parameterization by Recurrent Neural Networks ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") endows these parameters with data-driven dynamics via deep networks (see, e.g., [[46](https://arxiv.org/html/2511.17892v1#bib.bib46)]; [[32](https://arxiv.org/html/2511.17892v1#bib.bib32)]).

### 3.1 Yield forecasting using the Kalman filter

We begin with a linear‐Gaussian specification so that yields admit a standard Kalman update, providing a transparent baseline for later nonlinear price-space filters.

Consider the yields yt=(y1,⋯,ym)y\_{t}=\left(y\_{1},\cdots,y\_{m}\right) at time tt observed for fixed tenors τ1,⋯,τm\tau\_{1},\cdots,\tau\_{m}. We assume that the noise between the observations and the state model ([2.5](https://arxiv.org/html/2511.17892v1#S2.E5 "In 2.2 Dynamic Nelson-Siegel term structure ‣ 2 Arbitrage-free pricing framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints")) is Gaussian with mean zero and variance UtU\_{t}

|  |  |  |  |
| --- | --- | --- | --- |
|  | y​(t,τ)=Bττ​Xt+ϵt,y(t,\tau)=\frac{B\_{\tau}}{\tau}X\_{t}+\epsilon\_{t}, |  | (3.1) |

where 𝔼​[ϵt]=0\mathbb{E}\left[\epsilon\_{t}\right]=0 and Var​[ϵt]=Ut\text{Var}\left[\epsilon\_{t}\right]=U\_{t}. It is difficult to calculate the conditional expectation and variance of XtX\_{t} directly using Proposition [2.2](https://arxiv.org/html/2511.17892v1#S2.Thmtheorem2 "Proposition 2.2. ‣ 2.1 HJM forward rate model ‣ 2 Arbitrage-free pricing framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") if the state variable is non-scalar and the parameters κt\kappa\_{t}, θt\theta\_{t} and σt\sigma\_{t} are matrices. Therefore, we make a simplification by assuming that the time increment Δ​tk=tk+1−tk\Delta t\_{k}=t\_{k+1}-t\_{k} is constant and κt\kappa\_{t}, θt\theta\_{t}, and σt\sigma\_{t} are piecewise constant functions for t∈[tk,tk+1)t\in[t\_{k},t\_{k+1}) and all k≥0k\geq 0. By abuse of notation write
κk=κtk\kappa\_{k}=\kappa\_{t\_{k}}, θk=θtk\theta\_{k}=\theta\_{t\_{k}}, and σk=σtk\sigma\_{k}=\sigma\_{t\_{k}} for the constant values over the intervals; ℱk=ℱtk\mathcal{F}\_{k}=\mathcal{F}\_{t\_{k}} for the observation filtration; and Xk=XtkX\_{k}=X\_{t\_{k}} for the discretized state process. Then, by Proposition [2.2](https://arxiv.org/html/2511.17892v1#S2.Thmtheorem2 "Proposition 2.2. ‣ 2.1 HJM forward rate model ‣ 2 Arbitrage-free pricing framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints"), we obtain the following approximations

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼​[Xk+1|ℱk]\displaystyle\mathbb{E}\left[X\_{k+1}|\mathcal{F}\_{k}\right] | =e−κk​Δ​t​Xk+(I−e−κk​Δ​t)​θk,\displaystyle=e^{-\kappa\_{k}\Delta t}X\_{k}+\left(I-e^{-\kappa\_{k}\Delta t}\right)\theta\_{k}, |  | (3.2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Var​[Xk+1|ℱk]\displaystyle\text{Var}\left[X\_{k+1}|\mathcal{F}\_{k}\right] | =∫tktk+1e−κu​(tk+1−u)​σu​σu⊤​e−κu⊤​(tk+1−u)​𝑑u=∫tktk+1e−κk​(tk+1−u)​Σk​e−κk⊤​(tk+1−u)​𝑑u.\displaystyle=\int\_{t\_{k}}^{t\_{k+1}}e^{-\kappa\_{u}(t\_{k+1}-u)}\sigma\_{u}\sigma\_{u}^{\top}e^{-\kappa\_{u}^{\top}(t\_{k+1}-u)}\,du=\int\_{t\_{k}}^{t\_{k+1}}e^{-\kappa\_{k}(t\_{k+1}-u)}\Sigma\_{k}e^{-\kappa\_{k}^{\top}(t\_{k+1}-u)}du. |  | (3.3) |

We denote ([3.3](https://arxiv.org/html/2511.17892v1#S3.E3 "In 3.1 Yield forecasting using the Kalman filter ‣ 3 Forecasting framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints")) as Qk=Var​[Xk+1|ℱk]Q\_{k}=\text{Var}\left[X\_{k+1}|\mathcal{F}\_{k}\right] and the computation of QkQ\_{k} can be simplified using the diagonalization of the matrix κk=Ek​Vk​Ek−1\kappa\_{k}=E\_{k}V\_{k}E^{-1}\_{k},
where EkE\_{k} is the (d×d)(d\times d) matrix with the eigenvectors κk\kappa\_{k}, and VkV\_{k} is the diagonal matrix consisting of the dd eigenvalues ζk\zeta^{k} of κk\kappa\_{k}. The integral in ([3.3](https://arxiv.org/html/2511.17892v1#S3.E3 "In 3.1 Yield forecasting using the Kalman filter ‣ 3 Forecasting framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints")) can be simplified to

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qk=Ek​(∫tktk+1e−Vk​(tk+1−u)​Ωk​e−Vk⊤​(tk+1−u)​𝑑t)​Ek⊤​d​u,Q\_{k}=E\_{k}\left(\int\_{t\_{k}}^{t\_{k+1}}e^{-V\_{k}(t\_{k+1}-u)}\Omega\_{k}e^{-V^{\top}\_{k}(t\_{k+1}-u)}dt\right)E^{\top}\_{k}du, |  | (3.4) |

where Ωk=Ek−1​Σk​Ek−⊤=(ωi,jk)i,j\Omega\_{k}=E^{-1}\_{k}\Sigma\_{k}E^{-\top}\_{k}=\left(\omega\_{i,j}^{k}\right)\_{i,j}. The (i,j)(i,j)-th entry of the integral in ([3.4](https://arxiv.org/html/2511.17892v1#S3.E4 "In 3.1 Yield forecasting using the Kalman filter ‣ 3 Forecasting framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints")) can be simplified to

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ii,jk\displaystyle I^{k}\_{i,j} | =∫tktk+1(e−Vk​(tk+1−u)​Ωk​e−Vk⊤​(tk+1−u))i,j​𝑑u=∫tktk+1e−ζik​(tk+1−u)​(ωi,jk)​e−ζjk​(tk+1−u)​𝑑u\displaystyle=\int\_{t\_{k}}^{t\_{k+1}}\left(e^{-V\_{k}(t\_{k+1}-u)}\Omega\_{k}e^{-V^{\top}\_{k}(t\_{k+1}-u)}\right)\_{i,j}\,du=\int\_{t\_{k}}^{t\_{k+1}}e^{-\zeta\_{i}^{k}(t\_{k+1}-u)}\,(\omega\_{i,j}^{k})\,e^{-\zeta\_{j}^{k}(t\_{k+1}-u)}\,du |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ={ωi,jζik+ζjk​(1−e−(ζik+ζjk)​Δ​t),if ​ζi≠−ζjωi,jk​Δ​tif ​ζik=−ζjk.\displaystyle=\begin{cases}\frac{\omega\_{i,j}}{\zeta\_{i}^{k}+\zeta\_{j}^{k}}\left(1-e^{-\left(\zeta\_{i}^{k}+\zeta\_{j}^{k}\right)\Delta t}\right),&\text{if }\zeta\_{i}\neq-\zeta\_{j}\\ \omega\_{i,j}^{k}\Delta t&\mbox{if }\zeta\_{i}^{k}=-\zeta\_{j}^{k}\end{cases}. |  |

In empirical implementations, if |ζik+ζjk|<ϵ|\zeta\_{i}^{k}+\zeta\_{j}^{k}|<\epsilon, for some small tolerance ϵ>0\epsilon>0 we would use the second case of the integral approximation.
Alternatively, stable and efficient implementations could employ a Schur decomposition or a Van Loan block exponential to form the conditional variance estimate.
Nevertheless, in the remainder of this study, we shall estimate QkQ\_{k} by

|  |  |  |
| --- | --- | --- |
|  | Qk=E​[(ωi,jζi+ζj​(1−e−(ζi+ζj)​Δ​t))i,j]​ET.Q\_{k}=E\left[\left(\frac{\omega\_{i,j}}{\zeta\_{i}+\zeta\_{j}}\left(1-e^{-\left(\zeta\_{i}+\zeta\_{j}\right)\Delta t}\right)\right)\_{i,j}\right]E^{T}. |  |

Equations ([3.1](https://arxiv.org/html/2511.17892v1#S3.E1 "In 3.1 Yield forecasting using the Kalman filter ‣ 3 Forecasting framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints")) and ([3.2](https://arxiv.org/html/2511.17892v1#S3.E2 "In 3.1 Yield forecasting using the Kalman filter ‣ 3 Forecasting framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints")) give the state and observation equations

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xk+1=\displaystyle X\_{k+1}= | Dk+Ak​Xk+wk,\displaystyle D\_{k}+A\_{k}X\_{k}+w\_{k}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | yk+1=\displaystyle y\_{k+1}= | Mk+1​Xk+1+ϵk,\displaystyle M\_{k+1}X\_{k+1}+\epsilon\_{k}, |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ak=\displaystyle A\_{k}= | e−κk​Δ​t,Dk=(I−e−κk​Δ​t)​θk,Mk=[B1​(τ1k)τ1k,B2k​(τ1)τ1k,B3​(τ1k)τ1k⋮⋮⋮B1​(τmk)τmk,B2​(τmk)τmk,B3​(τmk)τmk],\displaystyle e^{-\kappa\_{k}\Delta t},\quad D\_{k}=\left(I-e^{-\kappa\_{k}\Delta t}\right)\theta\_{k},\quad M\_{k}=\left[\begin{matrix}\frac{B\_{1}\left(\tau\_{1}^{k}\right)}{\tau\_{1}^{k}},&~\frac{B\_{2}^{k}\left(\tau\_{1}\right)}{\tau\_{1}^{k}},&~\frac{B\_{3}\left(\tau\_{1}^{k}\right)}{\tau\_{1}^{k}}\\ \vdots&\vdots&\vdots\\ \frac{B\_{1}\left(\tau\_{m}^{k}\right)}{\tau\_{m}^{k}},&~\frac{B\_{2}\left(\tau\_{m}^{k}\right)}{\tau\_{m}^{k}},&~\frac{B\_{3}\left(\tau\_{m}^{k}\right)}{\tau\_{m}^{k}}\end{matrix}\right], |  |

and τmk\tau\_{m}^{k} is the maximum tenor from tkt\_{k} among all the observations.
The noise terms wkw\_{k} and ϵk\epsilon\_{k} are assumed to be independent Gaussian with mean zero and covariance QkQ\_{k} and UkU\_{k}, respectively.
The prediction step of the Kalman filter is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | X^k|k−1\displaystyle\hat{X}\_{k|k-1} | =Ak−1​X^k−1|k−1+Dk−1,\displaystyle=A\_{k-1}\hat{X}\_{k-1|k-1}+D\_{k-1}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | P^k|k−1\displaystyle\hat{P}\_{k|k-1} | =Ak−1​P^k−1|k−1​Ak−1T+Qk−1,\displaystyle=A\_{k-1}\hat{P}\_{k-1|k-1}A^{T}\_{k-1}+Q\_{k-1}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | y^k\displaystyle\hat{y}\_{k} | =Mk​X^k∣k−1,\displaystyle=M\_{k}\hat{X}\_{k\mid k-1}, |  |

and the update step is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | X^k|k\displaystyle\hat{X}\_{k|k} | =X^k|k−1+Kk​vk,\displaystyle=\hat{X}\_{k|k-1}+K\_{k}v\_{k}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | P^k|k\displaystyle\hat{P}\_{k|k} | =P^k|k−1−Kk​Mk​P^k|k−1,\displaystyle=\hat{P}\_{k|k-1}-K\_{k}M\_{k}\hat{P}\_{k|k-1}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | vk\displaystyle v\_{k} | =yk−y^k,\displaystyle=y\_{k}-\hat{y}\_{k}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Fk\displaystyle F\_{k} | =Mk​P^k|k−1​MkT+Uk−1,\displaystyle=M\_{k}\hat{P}\_{k|k-1}M^{T}\_{k}+U\_{k-1}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Kk\displaystyle K\_{k} | =P^k|k−1​MkT​Fk−1.\displaystyle=\hat{P}\_{k|k-1}M^{T}\_{k}F\_{k}^{-1}. |  |

### 3.2 Price forecasting using the extended Kalman filter

To forecast prices directly, rather than yields, we shall replace the linear measurement with a nonlinear bond-pricing map and employ the extended Kalman filter (EKF).
A related alternative for nonlinear measurement functions is the unscented Kalman filter (UKF), but we do not use it in this paper.

The observations Yk=(P​Vk(1),…,P​Vk(n))Y\_{k}=\left(PV\_{k}^{(1)},\dots,PV\_{k}^{(n)}\right) contain nn prices of coupon bonds and each observation is defined from ([2.7](https://arxiv.org/html/2511.17892v1#S2.E7 "In 2.2 Dynamic Nelson-Siegel term structure ‣ 2 Arbitrage-free pricing framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints")) as

|  |  |  |
| --- | --- | --- |
|  | Y^​(Xt,t)=∑j=1mcτj​e−Bτj​Xt=Cτ​exp⁡(−Bτ​Xt),\hat{Y}(X\_{t},t)=\sum\_{j=1}^{m}c\_{\tau\_{j}}e^{-B\_{\tau\_{j}}X\_{t}}=C\_{\tau}\exp\left(-B\_{\tau}X\_{t}\right), |  |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cτ\displaystyle C\_{\tau} | =(cτ1,cτ2,⋯,cτm)∈ℝ1×m,\displaystyle=\left(c\_{\tau\_{1}},c\_{\tau\_{2}},\cdots,c\_{\tau\_{m}}\right)\in\mathbb{R}^{1\times m}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Bτ\displaystyle B\_{\tau} | =(Bτ1,Bτ2,⋯,Bτm)T∈ℝm×3.\displaystyle=\left(B\_{\tau\_{1}},B\_{\tau\_{2}},\cdots,B\_{\tau\_{m}}\right)^{T}\in\mathbb{R}^{m\times 3}. |  |

The extended Kalman filter (see Christensen et al. [[8](https://arxiv.org/html/2511.17892v1#bib.bib8)]) by the following system

|  |  |  |  |
| --- | --- | --- | --- |
|  | X^k|k−1\displaystyle\hat{X}\_{k|k-1} | =Ak​X^k−1|k−1+Dk,\displaystyle=A\_{k}\hat{X}\_{k-1|k-1}+D\_{k}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | P^k|k−1\displaystyle\hat{P}\_{k|k-1} | =Ak​P^k−1|k−1​AkT+Qk,\displaystyle=A\_{k}\hat{P}\_{k-1|k-1}A\_{k}^{T}+Q\_{k}, |  | (3.5) |

and measurement process

|  |  |  |  |
| --- | --- | --- | --- |
|  | X^k|k\displaystyle\hat{X}\_{k|k} | =X^k|k−1+Kk​vk,\displaystyle=\hat{X}\_{k|k-1}+K\_{k}v\_{k}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | P^k|k\displaystyle\hat{P}\_{k|k} | =P^k|k−1−Kk​Mk​P^k|k−1,\displaystyle=\hat{P}\_{k|k-1}-K\_{k}M\_{k}\hat{P}\_{k|k-1}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | vk\displaystyle v\_{k} | =Yk−Y^​(X^k|k−1,tk),\displaystyle=Y\_{k}-\hat{Y}(\hat{X}\_{k|k-1},t\_{k}), |  | (3.6) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Fk\displaystyle F\_{k} | =Mk​P^k|k−1​MkT+Uk,\displaystyle=M\_{k}\hat{P}\_{k|k-1}M^{T}\_{k}+U\_{k}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Kk\displaystyle K\_{k} | =P^k|k−1​MkT​Fk−1,\displaystyle=\hat{P}\_{k|k-1}M\_{k}^{T}F\_{k}^{-1}, |  |

where the Jacobian matrix MkM\_{k} is calculated by

|  |  |  |
| --- | --- | --- |
|  | Mk=∂Y^​(X,t)∂X|.(X^k,tk)M\_{k}=\frac{\partial\hat{Y}(X,t)}{\partial X}\left|{}\_{(\hat{X}\_{k},t\_{k})}\right.. |  |

We linearize the measurement function around the current prediction; the Jacobian MkM\_{k} captures local sensitivity.

Instead of maximizing the log-likelihood, we directly minimize the prediction error

|  |  |  |
| --- | --- | --- |
|  | L​(t)=1n​vkT​vk,L(t)=\frac{1}{n}v\_{k}^{T}v\_{k}, |  |

and we optionally add the arbitrage penalty ([2.6](https://arxiv.org/html/2511.17892v1#S2.E6 "In 2.2 Dynamic Nelson-Siegel term structure ‣ 2 Arbitrage-free pricing framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints")) as a regularizer, yielding

|  |  |  |
| --- | --- | --- |
|  | L​(t)=1n​vkT​vk+λ​Λ(p).L(t)=\frac{1}{n}v\_{k}^{T}v\_{k}+\lambda\,\Lambda^{(p)}. |  |

### 3.3 Price forecasting using the particle filter

Finally, we consider a simulation-based alternative to the EKF, particle filtering, for bond-price prediction. Relative to the EKF, particle filtering (PF) dispenses with functional linearization and Jacobians, accommodating stronger nonlinearities and non-Gaussian errors. The trade-off is higher computation costs due to Monte-Carlo sampling and resampling (PF scales with the particle count; we use systematic resampling when effective sample size falls below a threshold). Relatedly, Christoffersen et al. [[9](https://arxiv.org/html/2511.17892v1#bib.bib9)] apply EKF and PF to yield-curve prediction with LIBOR, swap, and cap data.

In the PF, each state X​(t)=(X1​(t),X2​(t),X3​(t))⊤X(t)=\left(X\_{1}(t),X\_{2}(t),X\_{3}(t)\right)^{\top} of a 3-dimensional vector can be viewed as a particle.
We use an EKF-assisted importance distribution: for each particle, a local EKF measurement update produces (μk(i),Pk(i))(\mu\_{k}^{(i)},P\_{k}^{(i)}), yielding a Gaussian proposal
q​(Xk∣Xk−1(i),Yk)=𝒩​(μk(i),Pk(i))q(X\_{k}\mid X\_{k-1}^{(i)},Y\_{k})=\mathcal{N}(\mu\_{k}^{(i)},P\_{k}^{(i)}),
which lowers weight variance relative to a bootstrap proposal; see [[44](https://arxiv.org/html/2511.17892v1#bib.bib44)] for a closely related EKF-based importance design. Implementation proceeds by (i) initializing particles from the training-data priors, (ii) propagating via the state dynamics, (iii) updating particle weights using the measurement density, and (iv) systematic resampling when degeneracy is detected. Detailed algorithmic settings (proposal choice, resampling schedule, and effective sample size threshold) are deferred to Appendix [A](https://arxiv.org/html/2511.17892v1#A1 "Appendix A Particle filtering implementation ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints"). We introduce the general sequential Monte Carlo method then we add importance sampling from the measurement equations of the EKF into the PF (see, e.g., [[44](https://arxiv.org/html/2511.17892v1#bib.bib44)]).

Because price errors exhibit heavy tails and occasional outliers, we model observation noise with a multivariate generalized Gaussian distribution (MGGD), which nests Gaussian and Laplace cases and improves robustness (see, e.g., [[43](https://arxiv.org/html/2511.17892v1#bib.bib43)]).
For the prediction errors, we assume a different distribution instead of the multivariate Gaussian. Suppose the marginal densities of observation YtY\_{t} given the state XtX\_{t} can be measured by some distribution ℳ\mathcal{M}

|  |  |  |
| --- | --- | --- |
|  | Yt|Xt∼ℳ​(Yt|Y^​(Xt,t)).Y\_{t}\left|X\_{t}\right.\sim\mathcal{M}(Y\_{t}\left|\hat{Y}\left(X\_{t},t\right)\right.). |  |

In applications, we shall assume ℳ\mathcal{M} is a multivariate generalized Gaussian distribution (MGGD). Following the definition given by Pascal et al. [[43](https://arxiv.org/html/2511.17892v1#bib.bib43)] the nn-dimensional MGGD density is

|  |  |  |  |
| --- | --- | --- | --- |
|  | q​(x|x¯)=|U|−12​Cp,n​exp⁡(−[(x−x¯)T​U−1​(x−x¯)]p2​mp),q(x\left|\bar{x}\right.)=\left|U\right|^{-\frac{1}{2}}C\_{p,n}\exp\left(-\frac{\left[\left(x-\bar{x}\right)^{T}U^{-1}\left(x-\bar{x}\right)\right]^{p}}{2m^{p}}\right), |  | (3.7) |

where pp is the shape parameter and mm is the scale parameter, U∈ℝn×nU\in\mathbb{R}^{n\times n} is the covariance matrix, and

|  |  |  |
| --- | --- | --- |
|  | Cp,n=p​(21p​π​m)−n2​Γ​(n2)/Γ​(n2​p)C\_{p,n}=\left.p\left(2^{\frac{1}{p}}\pi m\right)^{-\frac{n}{2}}\Gamma\left(\frac{n}{2}\right)\right/\Gamma\left(\frac{n}{2p}\right) |  |

is a normalization constant.
In particular, if p=0.5p=0.5, equation ([3.7](https://arxiv.org/html/2511.17892v1#S3.E7 "In 3.3 Price forecasting using the particle filter ‣ 3 Forecasting framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints")) gives the multivariate Laplace distribution and p=1p=1 gives the multivariate Gaussian distribution. In our model, we treat the MGGD shape and scale parameters as hyperparameters.

Of the three filtering methods the KF offers speed and transparency when a linear yield-measurement is adequate. The EKF enables direct price-space updates but relies on local linearization. The PF handles stronger nonlinearities and heavy-tailed errors at greater computational cost. In Section [4](https://arxiv.org/html/2511.17892v1#S4 "4 Dynamic parameterization by Recurrent Neural Networks ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") we show how learned, time-varying (κt,θt,σt)(\kappa\_{t},\theta\_{t},\sigma\_{t}) further improves all three by aligning parameter dynamics with the data consistent with modern arbitrage-aware term-structure frameworks (see, e.g., [[21](https://arxiv.org/html/2511.17892v1#bib.bib21)]).

## 4 Dynamic parameterization by Recurrent Neural Networks

We use a filter-aware RNN composed of: (i) an *input block* that compresses cross-sectional information; (ii) a *state block* that outputs time-varying parameters (κt,θt,σt)(\kappa\_{t},\theta\_{t},\sigma\_{t}); (iii) a *residual block* that models observation-noise dynamics; and (iv) a differentiable *filter block* (KF/EKF/PF) that closes the loop. The model is trained end-to-end by backpropagating through the filter block.

### 4.1 Input layer

Since the data are different for the linear model (yield model) and the nonlinear model (price model), we have different input layers.

#### Yield-space (linear) model.

We train on yield panels arranged as a 3D tensor S×T×FS\times T\times F (samples ×\times time ×\times features), where each time step is a 1×F1\times F vector. We use yields at F=23F=23 fixed tenors τ∈{3,6,…,360}\tau\in\{3,6,\dots,360\} months to match the cross-sectional coverage. We use the extracted yields as inputs and predict the yields as the model output. To match the proportion of traded bonds in each term bucket there are 8 tenors in the short-term (0-2 year) bucket differing by 3 months
(3,6,…,24)(3,6,\ldots,24), 11 tenors in the mid-term bucket (2-10 year) differing by 6 months between 30 months and 60 months, then by 12 months until 120 months (30,36,…,60,72,84,…,120)(30,36,\ldots,60,72,84,\ldots,120), and 4 long-term tenors (180,240,300,360)(180,240,300,360) differing by 60 months.

The input layer is a two-layer LSTM that processes the time dimension and outputs hidden states (ct,ht)(c\_{t},h\_{t}); implementation details are given in Appendix [B](https://arxiv.org/html/2511.17892v1#A2 "Appendix B LSTM architecture ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints"), equation ([B](https://arxiv.org/html/2511.17892v1#A2.Ex2 "Appendix B LSTM architecture ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints")).

#### Price-space (nonlinear) model.

The per-day input is an N×FN\times F panel (bonds ×\times features). We first apply a *convolutional–LSTM (CLSTM)* to compress cross-sectional features into HH channels, then feed the result into an LSTM for temporal dynamics. Derivations and kernel-size choices are detailed in Appendix [C](https://arxiv.org/html/2511.17892v1#A3 "Appendix C CLSTM architecture ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints"). From the input layer, we obtain the final output from the input layer as a vector ctI∈ℝ1×Hc^{I}\_{t}\in\mathbb{R}^{1\times H} and pass it to the state layer.

### 4.2 State layer

Suppose we have an output ctI∈ℝ1×Hc^{I}\_{t}\in\mathbb{R}^{1\times H} from the input layer and consider it as the input for the state layer. We simply connect the output of the input layer to three dense layers κ\kappa, θ\theta and σ\sigma in the state layer

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | κ​(ctI):[0,T]×ℝ1×H\displaystyle\kappa(c^{I}\_{t}):[0,T]\times\mathbb{R}^{1\times H} | →ℝd×d,\displaystyle\rightarrow\mathbb{R}^{d\times d},~ |  | κ=aκ​(𝒲κ⋅𝒸𝓉ℐ+𝒷κ),\displaystyle\kappa=a\_{\kappa}\left(\mathpzc{W}\_{\kappa}\cdot c^{I}\_{t}+\mathpzc{b}\_{\kappa}\right), |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | θ​(ctI):[0,T]×ℝ1×H\displaystyle\theta(c^{I}\_{t}):[0,T]\times\mathbb{R}^{1\times H} | →ℝd,\displaystyle\rightarrow\mathbb{R}^{d}, |  | θ=aθ​(𝒲θ⋅𝒸𝓉ℐ+𝒷θ),\displaystyle\theta=a\_{\theta}\left(\mathpzc{W}\_{\theta}\cdot c^{I}\_{t}+\mathpzc{b}\_{\theta}\right), |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | σ​(ctI):[0,T]×ℝ1×H\displaystyle\sigma(c^{I}\_{t}):[0,T]\times\mathbb{R}^{1\times H} | →ℝd×d,\displaystyle\rightarrow\mathbb{R}^{d\times d},~ |  | σ=aσ​(𝒲σ⋅𝒸𝓉ℐ+𝒷σ),\displaystyle\sigma=a\_{\sigma}\left(\mathpzc{W}\_{\sigma}\cdot c^{I}\_{t}+\mathpzc{b}\_{\sigma}\right), |  |

where the operator (⋅)(\cdot) is tensor product. The kernels are
𝒲κ∈ℝℋ×𝒹×𝒹\mathpzc{W}\_{\kappa}\in\mathbb{R}^{H\times d\times d},
𝒲θ∈ℝℋ×𝒹\mathpzc{W}\_{\theta}\in\mathbb{R}^{H\times d},
𝒲σ∈ℝℋ×𝒹×𝒹\mathpzc{W}\_{\sigma}\in\mathbb{R}^{H\times d\times d},
the biases are
𝒷κ∈ℝ𝒹×𝒹\mathpzc{b}\_{\kappa}\in\mathbb{R}^{d\times d},
𝒷θ∈ℝ𝒹\mathpzc{b}\_{\theta}\in\mathbb{R}^{d},
𝒷σ∈ℝ𝒹×𝒹\mathpzc{b}\_{\sigma}\in\mathbb{R}^{d\times d},
and the activation functions are
aκ​(x)=xa\_{\kappa}(x)=x,
aθ​(x)=tanh⁡(x)a\_{\theta}(x)=\tanh(x),
aσ​(x)=tanh⁡(x)a\_{\sigma}(x)=\tanh(x).

### 4.3 Residual layer

Each time we obtain predicted values Y^t\hat{Y}\_{t} we analyze the residual values et=|Yt−Y^t|e\_{t}=\left|Y\_{t}-\hat{Y}\_{t}\right| and estimate the covariance matrix. We normalize residuals via batch normalization (B​NBN), pass them through an LSTM (LRL\_{R}), and map the hidden state to utu\_{t} with a dense layer (DRD\_{R}). The equations in the residual layer are

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | e¯t=\displaystyle\bar{e}\_{t}= | BN​(et),\displaystyle\text{BN}(e\_{t}), |  | (batch normalization) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (ctR,htR)=\displaystyle(c^{R}\_{t},h^{R}\_{t})= | LR​(e¯t,(ct−1R,ht−1R)),\displaystyle L\_{R}\left(\bar{e}\_{t},\left(c^{R}\_{t-1},h^{R}\_{t-1}\right)\right), |  | (LSTM) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ut=\displaystyle u\_{t}= | DR​(ctR).\displaystyle D\_{R}\left(c^{R}\_{t}\right). |  | (dense layer) |

### 4.4 Filter block

Given (κt,θt,σt,ut)(\kappa\_{t},\theta\_{t},\sigma\_{t},u\_{t}), the *filter block* performs a differentiable KF/EKF/PF update to produce state and prediction updates. We train *end-to-end* by backpropagating through this filter block (cf. KalmanNet and Bayesian KalmanNet). We obtain the final prediction Y^T\hat{Y}\_{T} after feeding the sequential data through the fully connected RNN networks and calculate the values of the arbitrage-free penalties Λ(p)\Lambda^{(p)} using the sequential states (Xt,κt,θt,σt)\left(X\_{t},\kappa\_{t},\theta\_{t},\sigma\_{t}\right). The model weights, including all the weights 𝔚\mathfrak{W} and biases 𝔟\mathfrak{b} in each layer, will be trained to minimize a weighted sum of prediction error and the arbitrage penalty Λ(p)\Lambda^{(p)}.

Each RNN unit comprises these four cells; stacking units across time yields the overall architecture (Figure [4.3](https://arxiv.org/html/2511.17892v1#S4.F3 "Figure 4.3 ‣ 4.4 Filter block ‣ 4 Dynamic parameterization by Recurrent Neural Networks ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints")).

Figure 4.3: Recurrent Neural Networks

![Refer to caption](x3.png)

### 4.5 Objective function

Our training objective combines squared prediction error with an arbitrage-regularization term (AER) weighted by λ\lambda:

|  |  |  |
| --- | --- | --- |
|  | L​(ϑ)=1n​∑i=1n∥Yi−Y^i∥2+λ​Λ(p).L(\vartheta)=\frac{1}{n}\sum\_{i=1}^{n}\lVert Y\_{i}-\widehat{Y}\_{i}\rVert^{2}+\lambda\,\Lambda^{(p)}. |  |

We optimize LL via gradient-based learning with early stopping on a rolling validation window.

Section [5](https://arxiv.org/html/2511.17892v1#S5 "5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") details hyper-parameters, training splits, and ablations (AER on/off, Gaussian vs MGGD, EKF-assisted vs bootstrap PF), and discusses accuracy–runtime trade-offs.

## 5 Empirical Results

We evaluate our arbitrage-regularized forecasting framework on daily U.S. Treasuries and a panel of corporate bonds (2017–2019), at horizons of *1-day* and *5-day*-ahead. We first describe the dataset and the chronological 80/20 split, then define the evaluation metrics—*MAE* (bps and dollars), *RMSE*, and *MPPE* (percent)—and a bid–ask *hit rate* computed at three spread levels ($​0.10\mathdollar 0.10, $​0.25\mathdollar 0.25, $​0.50\mathdollar 0.50). As a baseline, we reprice bonds using the last observed yield curve (*p*ersistence benchmark). We then compare three filters: (i) *KF* in yield-space (prices via repricing), (ii) *EKF* in price- and yield-space, and (iii) a *PF* in price-space, each trained with and without the AER penalty (λ∈{0,1}\lambda\in\{0,1\}). Results are reported separately for Treasuries and corporates, followed by runtime/practicality notes and robustness checks (AER sensitivity, Gaussian vs. MGGD errors, EKF-assisted vs. bootstrap PF).

### 5.1 Data and Splits

We apply our arbitrage-free prediction models on daily U.S. Treasury bills, notes, and bond data (≥60\geq 60 daily observations) and coupon bonds for 1212 corporate bond issuers
(≈\approx10-30 daily observations) over the period 2017 to 2019. Data come from FINRA-TRACE plus a proprietary Treasury feed. Each observation includes price, tenor, coupon rate, and payment frequency. This uses far fewer features than Ganguli and Dunnmon [[24](https://arxiv.org/html/2511.17892v1#bib.bib24)], allowing us to isolate the effects of arbitrage-free regularization and other modeling choices. We use an 80/20 chronological split (2017–2019) with the first 80% for training/validation and the final 20% held out for testing.

### 5.2 Metrics and Benchmarks

We organize the data into monthly sequences of T=20T=20 trading days, producing hh-day-ahead predictions (h∈{1,5}h\in\{1,5\}). We report MAE (bps) for yields, MAE (dollars) for prices, RMSPE, and MPPE (percentage). The hit rate is computed at three spread levels: $0.10, $0.25, and $0.50 where

|  |  |  |  |
| --- | --- | --- | --- |
|  | hit rate (spread)=1N​T​∑i=1T∑j=1N𝟏{|Y​(ti,τj)−Y^​(ti,τj)|≤spread}\text{hit rate (spread)}=\frac{1}{NT}\sum\_{i=1}^{T}\sum\_{j=1}^{N}\mathbf{1}\_{\left\{\left|Y(t\_{i},\tau\_{j})-\hat{Y}(t\_{i},\tau\_{j})\right|\leq\text{spread}\right\}} |  | (5.1) |

is the average over the included tenors and observations for a maturity bucket. Generally, if the price predictions are within bid-ask spreads we would consider them as market-consistent predictions. To compare the hit rate, we include a persistence benchmark as a baseline where we hold the last observed yield curve fixed (no-change) and reprice the bonds. Other measures of prediction accuracy could be used, including volume-weighted or duration-weighted performance measures (e.g., see, [[29](https://arxiv.org/html/2511.17892v1#bib.bib29)]), but the hit rate defined above provides a crude measure of the degree to which bonds are priced “correctly” relative to each other [[5](https://arxiv.org/html/2511.17892v1#bib.bib5)].

For h=5h=5, we index trading days t=0,1,2,…t=0,1,2,\ldots (after removing non-trading days) and form five nonoverlapping subsequences ("offsets”)
𝒯r={t:t≡r(mod5)}\mathcal{T}\_{r}=\{\,t:\ t\equiv r\pmod{5}\,\} for r∈{0,1,2,3,4}r\in\{0,1,2,3,4\}.
Each offset contains every fifth trading day (e.g., t,t+5,t+10,…t,t+5,t+10,\ldots), so a time tt and its hh-day-ahead target t+5t+5 do not overlap with examples from other offsets; we pool the five offsets for estimation. Offsets are defined by trading-day indices—not calendar weekdays—so they remain valid in holiday weeks.
Separately, to compare forecasting results across maturities, we report yields at 3, 12, 36, 60, 120, 240, and 360 months, and group price results into 0–2 year, 2–10 year, and 10–30 year tenor buckets. We evaluate KF (yields; prices via bond repricing), EKF (yields and prices), and PF (prices; yields inferred from priced bonds) assisted machine learning models, each with AER on/off (λ∈{0,1}\lambda\in\{0,1\}).

### 5.3 Main Results (UST)

Table 5.3: Testing result of U.S. Treasuries: yield prediction error (in bps)

| Model | MAPE | | RMSPE | | STDV | | MAPE | | RMSPE | | STDV | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Maturities | 1-day | 5-day | 1-day | 5-day | 1-day | 5-day | 1-day | 5-day | 1-day | 5-day | 1-day | 5-day |
| KF (λ\lambda=0) |  |  |  |  |  |  | KF (λ\lambda=1) |  |  |  |  |  |
| 3M | 3.22 | 9.04 | 4.30 | 10.96 | 4.26 | 9.18 | 3.18 | 5.61 | 4.20 | 7.11 | 4.18 | 7.1 |
| 1Y | 3.17 | 10.3 | 4.20 | 13.25 | 4.17 | 12.07 | 3.23 | 6.3 | 4.26 | 8.19 | 4.22 | 8.13 |
| 3Y | 3.75 | 12.38 | 4.89 | 16.45 | 4.88 | 16.02 | 3.82 | 8.29 | 5.01 | 11.17 | 4.96 | 11.06 |
| 5Y | 3.88 | 11.39 | 5.02 | 15.07 | 5.02 | 14.93 | 3.93 | 8.51 | 5.16 | 11.43 | 5.12 | 11.42 |
| 10Y | 3.72 | 8.49 | 4.73 | 11.13 | 4.73 | 11.11 | 3.85 | 8.29 | 4.92 | 11.14 | 4.91 | 10.83 |
| 20Y | 3.70 | 9.4 | 4.72 | 12.55 | 4.71 | 12.25 | 3.84 | 9.55 | 4.91 | 12.78 | 4.91 | 11.54 |
| 30Y | 3.74 | 10.82 | 4.83 | 14.36 | 4.83 | 13.94 | 3.91 | 10.55 | 5.02 | 13.87 | 5.01 | 12.22 |
| EKF (λ\lambda=0) |  |  |  |  |  |  | EKF (λ\lambda=1) |  |  |  |  |  |
| 3M | 3.69 | 6.66 | 4.92 | 8.19 | 4.72 | 8.14 | 4.47 | 6.68 | 5.87 | 8.38 | 5.79 | 8.35 |
| 1Y | 3.40 | 6.53 | 4.57 | 8.27 | 4.48 | 8.27 | 3.88 | 6.64 | 5.19 | 8.41 | 5.14 | 8.33 |
| 3Y | 3.96 | 8.45 | 5.24 | 11.09 | 5.24 | 11.07 | 4.09 | 8.71 | 5.44 | 11.2 | 5.42 | 11.1 |
| 5Y | 4.18 | 9.25 | 5.43 | 11.93 | 5.43 | 11.88 | 4.25 | 9.45 | 5.51 | 12.1 | 5.50 | 12.03 |
| 10Y | 4.03 | 8.91 | 5.11 | 11.44 | 5.11 | 11.36 | 3.98 | 9.18 | 5.07 | 11.78 | 5.06 | 11.77 |
| 20Y | 3.91 | 8.36 | 4.99 | 11.02 | 4.98 | 10.91 | 3.81 | 8.77 | 4.84 | 11.51 | 4.83 | 11.51 |
| 30Y | 3.94 | 8.29 | 5.07 | 11.06 | 5.05 | 10.95 | 3.81 | 8.71 | 4.88 | 11.61 | 4.86 | 11.6 |
| PF (λ\lambda=0) |  |  |  |  |  |  | PF (λ\lambda=1) |  |  |  |  |  |
| 3M | 4.83 | 8.33 | 6.24 | 10.19 | 6.21 | 9.81 | 4.97 | 7.18 | 6.40 | 9.13 | 6.37 | 9.13 |
| 1Y | 4.01 | 7.66 | 5.07 | 9.89 | 5.05 | 9.78 | 4.04 | 7.47 | 5.21 | 9.44 | 5.19 | 9.35 |
| 3Y | 3.97 | 9.23 | 5.15 | 12.06 | 5.15 | 12.06 | 3.94 | 9.6 | 5.10 | 12.08 | 5.09 | 11.86 |
| 5Y | 4.15 | 9.57 | 5.34 | 12.55 | 5.34 | 12.54 | 4.10 | 10.02 | 5.23 | 12.59 | 5.23 | 12.4 |
| 10Y | 4.01 | 9.16 | 5.05 | 11.86 | 5.05 | 11.86 | 3.94 | 9.14 | 4.94 | 11.59 | 4.94 | 11.54 |
| 20Y | 3.93 | 9.07 | 5.01 | 11.88 | 5.00 | 11.84 | 3.85 | 8.33 | 4.85 | 11.02 | 4.84 | 11.02 |
| 30Y | 4.01 | 9.3 | 5.13 | 12.22 | 5.12 | 12.15 | 3.89 | 8.16 | 4.94 | 11.1 | 4.92 | 11.08 |




Table 5.4: Testing result of U.S. Treasuries: mean absolute prediction error and mean percentage prediction error

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | MAPE (bps) | | MAPE (dollar) | | hit rate (≤$​0.10\leq\mathdollar 0.10) | | MPPE (%\%) by tenor bucket | | | | | |
|  | 0∼20\sim 2 (years) | | 2∼102\sim 10 (years) | | 10∼1510\sim 15 (years) | |
|  | 1-day | 5-day | 1-day | 5-day | 1-day | 5-day | 1-day | 5-day | 1-day | 5-day | 1-day | 5-day |
| Benchmark | 3.54 | 6.98 | 0.165 | 0.283 | 54.8%\% | 42.58%\% | 0.065 | 0.085 | 0.157 | 0.32 | 0.683 | 1.439 |
| KF(λ\lambda=0) | 3.58 | 10.45 | 0.172 | 0.443 | 54.5%\% | 32.66%\% | 0.065 | 0.114 | 0.159 | 0.452 | 0.684 | 1.747 |
| EKF(λ\lambda=0) | 1.95 | 8.11 | 0.181 | 0.354 | 54.1%\% | 38.82%\% | 0.066 | 0.087 | 0.168 | 0.343 | 0.725 | 1.533 |
| PF(λ\lambda=0) | 1.95 | 8.85 | 0.180 | 0.373 | 53.5%\% | 37.55%\% | 0.065 | 0.091 | 0.167 | 0.362 | 0.722 | 1.614 |
| KF(λ\lambda=1) | 3.67 | 7.96 | 0.175 | 0.363 | 54.4%\% | 40.30%\% | 0.065 | 0.086 | 0.161 | 0.325 | 0.708 | 1.741 |
| EKF(λ\lambda=1) | 1.95 | 8.32 | 0.181 | 0.364 | 52.6%\% | 38.76%\% | 0.065 | 0.09 | 0.168 | 0.399 | 0.741 | 1.673 |
| PF(λ\lambda=1) | 1.95 | 8.76 | 0.178 | 0.371 | 54.0%\% | 36.31%\% | 0.067 | 0.096 | 0.157 | 0.365 | 0.693 | 1.58 |

For U.S. treasuries we report the mean absolute prediction error (MAPE), root mean square prediction error (RMSPE) and mean percentage prediction error (MPPE) of the yields (bps) and prices (dollars) in 1-day-ahead and 5-day-ahead predictions for the testing-set in Tables [5.3](https://arxiv.org/html/2511.17892v1#S5.T3 "Table 5.3 ‣ 5.3 Main Results (UST) ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") and [5.4](https://arxiv.org/html/2511.17892v1#S5.T4 "Table 5.4 ‣ 5.3 Main Results (UST) ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints"). Yield forecasting using the dynamic Nelson-Siegel model shows small variation in prediction errors from the short-term maturities to long-term maturities. Yield prediction errors are less than 4.94.9 bps in 11-day-ahead forecasting and less than 1111 bps in 55-day-ahead forecasting. The price prediction errors are less than 2020 cents in 1-day-ahead forecasting and less than 4040 cents in 5-day ahead forecasting. Arbitrage-free regularization has significant impact on the yield data for the KF-based model but does not influence the price model with EKF-based or PF-based models. It is important to distinguish between yield-space and price-space forecasting: the AER penalty primarily improves yield-space predictions (KF), while having limited influence when forecasting directly in price-space (EKF and PF). Forecasting performance improvement with arbitrage-free regularization results are presented in Table [5.3](https://arxiv.org/html/2511.17892v1#S5.T3 "Table 5.3 ‣ 5.3 Main Results (UST) ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints"). For the KF-based model and 5-day-ahead forecasting horizon the prediction error for 3-month to 5- year maturities are significantly decreased. Forecasting performance of the long-tenor bonds are less accurate than that of the short-tenor bonds. Forecast errors are larger at long maturities, plausibly reflecting data sparsity; future work will augment the panel with additional long-tenor observations and post-pandemic data.

In Figure [4(b)](https://arxiv.org/html/2511.17892v1#S5.F4.sf2 "In Figure 5.4 ‣ 5.3 Main Results (UST) ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints"), we show the average excess return (AER) obtained from the evolution of forward rate curves that indicates the excess rate of the bond prices over the risk-free prices. The AER theoretically improves the soundness of the model and minimizes arbitrage opportunities in the dynamics of forward rate curves. The value of the AER shown in Figure [4(b)](https://arxiv.org/html/2511.17892v1#S5.F4.sf2 "In Figure 5.4 ‣ 5.3 Main Results (UST) ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") is obtained from the trained model with arbitrage-free regularization (λ=1\lambda=1). The trained models without arbitrage regularization (λ=0\lambda=0) have very high AER values which are not comparable. Among the three models, the AER for the KF model is significantly lower than the AER for the EKF and PF, particularly on the training set. We use panel-specific y-axis scales in Figure 5.4 to highlight the shape of each model’s loss across maturities. The KF model has relatively stable AER across maturities in both the training and test sets, while the EKF and PF vary over maturities. In absolute terms, the magnitude of the AER is highest for the EKF at longer maturities, whereas the PF exhibits the largest AER at short maturities. From the perspective of models, the consistency and the minimum value of AER provided by the Kalman filter across the training result and the testing result indicates that forecasting in the yield-space with arbitrage-free regularization is more robust than the nonlinear filter models forecasting in the price-space. This is consistent with the stronger stability of arbitrage-regularized dynamics when forecasting in yield-space under the linear state–space representation.

Figure 5.4: U.S. Treasuries: Average Excess Return (%) by tenor for KF, EKF, PF 1-day-ahead predictions

(a) Training Set AER

![Refer to caption](x4.png)

(b) Test Set AER

![Refer to caption](x5.png)

(c) Training Set |AER|

![Refer to caption](x6.png)

(d) Test Set |AER|

![Refer to caption](x7.png)

Sensitivity to the arbitrage penalty λ\lambda, error-model choices (Gaussian vs. MGGD), and PF settings is reported in Section [5.5](https://arxiv.org/html/2511.17892v1#S5.SS5 "5.5 Robustness and Sensitivity ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints"). Therefore, we considered only the cases λ=0\lambda=0 (AER off) and λ=1\lambda=1 (AER on). We next consider the prediction performance of the models applied to corporate bond data similarly.

### 5.4 Main Results (Corporates)

We next apply our models to the credit spreads over treasuries for 10 corporate issuers and examine forecasting performance. Table [5.5](https://arxiv.org/html/2511.17892v1#S5.T5 "Table 5.5 ‣ 5.4 Main Results (Corporates) ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") shows the 55-day-ahead forecasting results on data from ten corporate bond issuers with the predicted corporate spread calculated by subtracting the predicted Treasury yield from the predicted corporate yield and comparing to the observed value. For the forecasting results of corporate data, we show the predicted spread errors (predicted corporate yields −- predicted Treasury yields) are less than 1414 bps in 55-day-ahead forecasting. Since credit risk factors are not included, and the corporate data contains only around 10 to 30 daily bonds, the forecasting performance of corporate data is not comparable to that of Treasury data. In the case of corporates the yield data contains seems to contain more information than the corporate bond prices and we find that the KF model significantly outperforms the EKF and PF models.

In related work, other models incorporating credit risk factors such as Duffie [[18](https://arxiv.org/html/2511.17892v1#bib.bib18)] show prediction errors around 100100 basis points on short-term corporate bond yields and around 99 basis points on long-term. Duffee [[17](https://arxiv.org/html/2511.17892v1#bib.bib17)] investigates 161 firm’s bonds on monthly basis and shows the RMSE forecasting yield error in 34.5634.56 bps for 6-month maturity and 7.777.77 bps for 30-year maturities, using the Kalman filter and a CIR model as interest rate in 11-month-ahead forecasting. However, Duffee [[17](https://arxiv.org/html/2511.17892v1#bib.bib17)] does not provide the out-of-sample tests. Ganguli and Dunnmon [[24](https://arxiv.org/html/2511.17892v1#bib.bib24)] study corporate-bond forecasting with a 61-feature trade-level dataset and report results using a weighted error metric (WEPS); because the metric and features differ from ours, we do not compare levels. As noted in Diebold and Li [[14](https://arxiv.org/html/2511.17892v1#bib.bib14)], there is a persistent discrepancy between actual bond prices and the prices estimated from term structure models for the Treasury bonds. We do not smooth the observed prices so the discrepancy in the corporate bonds would be much larger than the Treasury bonds due to credit risk and/or liquidity problem.

Table 5.5: Testing result of 5-day-ahead forecasting: spread error (bps) and price error (dollar)

Ticker
MAPE
STDV
MPE
hit rate
Ticker
MAPE
STDV
MPE
hit rate

Model
Spread
Price
Spread
Price
%\%
≤$​0.25\leq\mathdollar 0.25
Model
Spread
Price
Spread
Price
%\%
≤$​0.25\leq\mathdollar 0.25


AAPL






AAPL


KF (λ\lambda=0)
5.27
0.241
2.54
0.353
0.231
68.1%\%
KF (λ\lambda=1)
6.7
0.246
3.02
0.359
0.348
59.7%\%

EKF (λ\lambda=0)
11.47
0.397
5.08
0.635
0.379
52.9%\%
EKF (λ\lambda=1)
10.52
0.355
3.51
0.523
0.341
53.0%\%

PF (λ\lambda=0)
10.4
0.259
3.44
0.386
0.248
65.8%\%
PF (λ\lambda=1)
9.44
0.351
2.58
0.533
0.288
60.6%\%

C






C


KF (λ\lambda=0)
9.93
0.447
2.92
0.713
0.404
45.5%\%
KF (λ\lambda=1)
9.34
0.449
1.92
0.704
0.390
46.0%\%

EKF (λ\lambda=0)
10.66
0.454
3.27
0.726
0.411
43.8%\%
EKF (λ\lambda=1)
13
0.491
5.06
0.793
0.408
45.3%\%

PF (λ\lambda=0)
11.05
0.49
2.44
0.816
0.440
45.1%\%
PF (λ\lambda=1)
14.03
0.534
6.45
0.898
0.412
44.1%\%

DIS






DIS


KF (λ\lambda=0)
7.83
0.365
3.46
0.847
0.341
62.0%\%
KF (λ\lambda=1)
11.76
0.369
3.48
0.587
0.334
62.5%\%

EKF (λ\lambda=0)
11.24
0.372
4.81
0.67
0.351
53.2%\%
EKF (λ\lambda=1)
11.02
0.394
3.94
0.757
0.352
55.2%\%

PF (λ\lambda=0)
11.33
0.383
4.44
0.721
0.358
54.7%\%
PF (λ\lambda=1)
9.61
0.382
3.52
0.812
0.363
54.0%\%

GS






GS


KF (λ\lambda=0)
8.75
0.426
2.89
0.615
0.388
47.2%\%
KF (λ\lambda=1)
8.66
0.428
1.71
0.604
0.402
45.6%\%

EKF (λ\lambda=0)
9.16
0.437
1.96
0.649
0.402
47.3%\%
EKF (λ\lambda=1)
10.81
0.434
2.72
0.658
0.402
48.0%\%

PF (λ\lambda=0)
10.24
0.433
3.06
0.653
0.397
47.7%\%
PF (λ\lambda=1)
11.03
0.475
2.94
0.727
0.400
47.1%\%

JNJ






JNJ


KF (λ\lambda=0)
7.38
0.454
3.78
0.706
0.412
47.0%\%
KF (λ\lambda=1)
8.06
0.429
3.46
0.645
0.400
47.4%\%

EKF (λ\lambda=0)
10.61
0.54
6.13
0.879
0.496
40.4%\%
EKF (λ\lambda=1)
10.21
0.541
3.58
0.882
0.518
42.0%\%

PF (λ\lambda=0)
9.96
0.578
4.01
0.937
0.527
41.6%\%
PF (λ\lambda=1)
11.01
0.607
3.9
1.012
0.475
41.9%\%

JPM






JPM


KF (λ\lambda=0)
6.46
0.346
1.77
0.616
0.307
58.7%\%
KF (λ\lambda=1)
8.49
0.45
4.12
0.914
0.324
55.9%\%

EKF (λ\lambda=0)
10.07
0.473
3.95
0.909
0.412
52.1%\%
EKF (λ\lambda=1)
11.31
0.508
3.38
0.96
0.398
48.3%\%

PF (λ\lambda=0)
10.62
0.491
3.58
0.914
0.429
50.9%\%
PF (λ\lambda=1)
12.63
0.482
4.97
0.926
0.430
50.0%\%

MSFT






MSFT


KF (λ\lambda=0)
5.62
0.343
2.77
0.492
0.325
52.5%\%
KF (λ\lambda=1)
8.34
0.448
4.96
0.807
0.331
52.3%\%

EKF (λ\lambda=0)
10.56
0.441
3.37
0.653
0.419
45.9%\%
EKF (λ\lambda=1)
9.9
0.429
2.84
0.662
0.434
43.4%\%

PF (λ\lambda=0)
11.6
0.393
4.14
0.594
0.373
50.1%\%
PF (λ\lambda=1)
10.84
0.433
3.6
0.67
0.406
47.4%\%

T






T


KF (λ\lambda=0)
9.41
0.45
5.62
1.022
0.398
57.1%\%
KF (λ\lambda=1)
10.26
0.407
5.11
0.85
0.370
59.6%\%

EKF (λ\lambda=0)
10.56
0.489
4.59
0.951
0.440
49.8%\%
EKF (λ\lambda=1)
14.14
0.611
5
1.057
0.431
48.7%\%

PF (λ\lambda=0)
12.81
0.389
5.31
0.75
0.353
57.5%\%
PF (λ\lambda=1)
14.04
0.53
6.55
1.032
0.361
57.5%\%

UNH






UNH


KF (λ\lambda=0)
8.34
0.404
3.63
0.881
0.377
54.2%\%
KF (λ\lambda=1)
10.15
0.433
5.18
0.909
0.343
55.5%\%

EKF (λ\lambda=0)
9.23
0.364
4.18
0.588
0.344
53.4%\%
EKF (λ\lambda=1)
11.68
0.376
4.65
0.615
0.361
53.1%\%

PF (λ\lambda=0)
10.96
0.378
3.09
0.744
0.353
56.5%\%
PF (λ\lambda=1)
10.34
0.371
3.89
0.602
0.349
57.0%\%

WFC






WFC


KF (λ\lambda=0)
7.03
0.368
2.82
0.778
0.330
68.0%\%
KF (λ\lambda=1)
10.64
0.442
3.72
0.878
0.337
66.5%\%

EKF (λ\lambda=0)
12.14
0.56
3.38
1.117
0.501
55.8%\%
EKF (λ\lambda=1)
13.25
0.562
2.8
1.166
0.592
53.8%\%

PF (λ\lambda=0)
12.77
0.538
3.34
1.029
0.487
54.5%\%
PF (λ\lambda=1)
13.71
0.583
3.52
1.12
0.560
50.2%\%




Figure 5.5: Training result of U.S. Treasuries: Model loss

![Refer to caption](x8.png)

### 5.5 Robustness and Sensitivity

#### Training dynamics.

Figure [5.5](https://arxiv.org/html/2511.17892v1#S5.F5 "Figure 5.5 ‣ 5.4 Main Results (Corporates) ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") reports training and test losses. The loss curves are stable with early stopping and show no overfitting for the horizons considered.

#### Arbitrage-penalty sensitivity.

We show the forecasting results of the bond prices using the model with Kalman filter by varying the value of the penalty (λ\lambda) in Table [5.6](https://arxiv.org/html/2511.17892v1#S5.T6 "Table 5.6 ‣ Arbitrage-penalty sensitivity. ‣ 5.5 Robustness and Sensitivity ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") where we train the models to reach almost the same MSE and compare the hit rate. The MAE shows the mean absolute forecasting error of bond prices in dollars. We can see that the arbitrage-free regularization significantly improves the forecasting performance in 55-day-ahead forecasting. The arbitrage-free penalty with λ=1\lambda=1 shows the best training MSE with overall the best hit rates. Increasing the value of λ\lambda leads to increasing computational cost since the regularization term will dominate the target function and the training process takes longer to decrease the loss function.

Table 5.6: Sensitivity to Arbitrage Penalty: U.S. Treasuries KF-Based Model (test set)

penalty
MAE
MSE
hit rate ($0.10)
hit rate ($0.25)
hit rate ($0.50)

(λ)(\lambda)
1-day
5-day
1-day
5-day
1-day
5-day
1-day
5-day
1-day
5-day


0
0.1717
0.4428
0.1067
0.8084
54.46%\%
32.66%\%
83.40%\%
58.25%\%
93.43%\%
75.32%\%

0.01
0.1709
0.4244
0.1043
0.9193
54.68%\%
34.85%\%
83.18%\%
61.37%\%
93.58%\%
77.95%\%

0.1
0.1712
0.4079
0.1054
0.8071
54.91%\%
37.16%\%
83.11%\%
63.21%\%
93.50%\%
80.08%\%

0.5
0.1960
0.4429
0.1859
1.2945
54.02%\%
39.55%\%
82.99%\%
65.26%\%
92.11%\%
79.97%\%

1
0.1750
0.3630
0.1136
0.6886
54.43%\%
40.30%\%
83.40%\%
66.77%\%
93.03%\%
83.14%\%

1.5
0.2119
0.4392
0.2724
1.4783
54.49%\%
39.46%\%
82.46%\%
65.79%\%
91.89%\%
81.25%\%

10
0.1956
0.4173
0.1750
1.1795
52.87%\%
40.94%\%
81.54%\%
67.44%\%
92.55%\%
82.36%\%

In Figure [5.6](https://arxiv.org/html/2511.17892v1#S5.F6 "Figure 5.6 ‣ Arbitrage-penalty sensitivity. ‣ 5.5 Robustness and Sensitivity ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") and [5.7](https://arxiv.org/html/2511.17892v1#S5.F7 "Figure 5.7 ‣ Arbitrage-penalty sensitivity. ‣ 5.5 Robustness and Sensitivity ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints"), we show the hh-day-ahead forecasting of state variables X​(t)=(X1​(t),X2​(t),X3​(t))⊤X(t)=(X\_{1}(t),X\_{2}(t),X\_{3}(t))^{\top} comparing to the observed state variables on a daily basis as short-term, mid-term and long-term levels. In Figure [5.6](https://arxiv.org/html/2511.17892v1#S5.F6 "Figure 5.6 ‣ Arbitrage-penalty sensitivity. ‣ 5.5 Robustness and Sensitivity ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") showing the 1-day-ahead forecasting, the difference between the forecasted result and observed results are undiscernible. However, in Figure [5.7](https://arxiv.org/html/2511.17892v1#S5.F7 "Figure 5.7 ‣ Arbitrage-penalty sensitivity. ‣ 5.5 Robustness and Sensitivity ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") showing the 5-day-ahead forecasting, we see that the forecasted result with arbitrage regularization (AR) is closer to the observed results. The forecasted paths of state variables for the EKF-based model shows more oscillation than the forecasted paths obtained using the PF-based model.

Figure 5.6: U.S. Treasuries: path of state variables of 1-day-ahead forecasting

![Refer to caption](x9.png)



Figure 5.7: U.S. Treasuries: path of state variables of 5-day-ahead forecasting

![Refer to caption](x10.png)



Figure 5.8: U.S. Treasuries: yield curves of 1-day-ahead forecasting

![Refer to caption](x11.png)



Figure 5.9: U.S. Treasuries: yield curves of 5-day-ahead forecasting

![Refer to caption](x12.png)

Figure [5.8](https://arxiv.org/html/2511.17892v1#S5.F8 "Figure 5.8 ‣ Arbitrage-penalty sensitivity. ‣ 5.5 Robustness and Sensitivity ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") and Figure [5.9](https://arxiv.org/html/2511.17892v1#S5.F9 "Figure 5.9 ‣ Arbitrage-penalty sensitivity. ‣ 5.5 Robustness and Sensitivity ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") present two examples of predicted yield curves: the left one is an increasing yield curve from the training set and the right one is an inverted humped yield curve from the testing set. From Figure [5.8](https://arxiv.org/html/2511.17892v1#S5.F8 "Figure 5.8 ‣ Arbitrage-penalty sensitivity. ‣ 5.5 Robustness and Sensitivity ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") and Figure [5.9](https://arxiv.org/html/2511.17892v1#S5.F9 "Figure 5.9 ‣ Arbitrage-penalty sensitivity. ‣ 5.5 Robustness and Sensitivity ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints"), we can see that the forecasted yield curves with the restriction of arbitrage-free regularization show higher accuracy and this effect is more obvious in 55-day-ahead forecasting.

Figures [5.10](https://arxiv.org/html/2511.17892v1#S5.F10 "Figure 5.10 ‣ Arbitrage-penalty sensitivity. ‣ 5.5 Robustness and Sensitivity ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") and [5.11](https://arxiv.org/html/2511.17892v1#S5.F11 "Figure 5.11 ‣ Arbitrage-penalty sensitivity. ‣ 5.5 Robustness and Sensitivity ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") show the variation of the state parameters: κt\kappa\_{t}, θt\theta\_{t} and σt\sigma\_{t} obtained from the yield prediction and bond price prediction models using the Kalman filter with and without arbitrage-free regularization. Visual inspection suggests regime dependence without AER and stabilization with AER. A formal test (e.g., Markov-switching or Bai–Perron tests) is beyond scope of this paper but left for future work.

Figure 5.10: U.S. Treasuries: state parameters (Kalman filter)

![Refer to caption](x13.png)



Figure 5.11: U.S. Treasuries: State parameters (Kalman filter + arbitrage regularization)

![Refer to caption](x14.png)



Figure 5.12: U.S. Treasuries: Q-Q plot (price error) of 1-day-ahead forecasting

![Refer to caption](figures/qqplot_price.jpg)



Figure 5.13: U.S. Treasuries: yield error distribution of 1-day-ahead forecasting

![Refer to caption](figures/yield_error_dist_testing.jpg)



Figure 5.14: U.S. Treasuries: QQ-plot (yield error) of 1-day-ahead forecasting

![Refer to caption](figures/qqplot_yield.jpg)

Error model. Results are qualitatively similar under Gaussian and MGGD error specifications; heavier tails tend to favor the PF at short maturities. Figures [5.12](https://arxiv.org/html/2511.17892v1#S5.F12 "Figure 5.12 ‣ Arbitrage-penalty sensitivity. ‣ 5.5 Robustness and Sensitivity ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints")-[5.14](https://arxiv.org/html/2511.17892v1#S5.F14 "Figure 5.14 ‣ Arbitrage-penalty sensitivity. ‣ 5.5 Robustness and Sensitivity ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") and [5.17](https://arxiv.org/html/2511.17892v1#S5.F17 "Figure 5.17 ‣ Particle filter settings. ‣ 5.5 Robustness and Sensitivity ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") fit the 1-day-ahead prediction errors of Treasury yields and bond prices with several candidate distributions and report the corresponding Q–Q plots. Figure [5.17](https://arxiv.org/html/2511.17892v1#S5.F17 "Figure 5.17 ‣ Particle filter settings. ‣ 5.5 Robustness and Sensitivity ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") shows that bond-price prediction errors exhibit excess kurtosis, which is mitigated when the arbitrage penalty is active. Figure [5.12](https://arxiv.org/html/2511.17892v1#S5.F12 "Figure 5.12 ‣ Arbitrage-penalty sensitivity. ‣ 5.5 Robustness and Sensitivity ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") indicates that fat tails are pronounced for the nonlinear price-space models, while Figure [5.13](https://arxiv.org/html/2511.17892v1#S5.F13 "Figure 5.13 ‣ Arbitrage-penalty sensitivity. ‣ 5.5 Robustness and Sensitivity ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") shows that yield errors have relatively low kurtosis, again improved by arbitrage regularization. Comparing the PF results in Figures [5.12](https://arxiv.org/html/2511.17892v1#S5.F12 "Figure 5.12 ‣ Arbitrage-penalty sensitivity. ‣ 5.5 Robustness and Sensitivity ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") and [5.17](https://arxiv.org/html/2511.17892v1#S5.F17 "Figure 5.17 ‣ Particle filter settings. ‣ 5.5 Robustness and Sensitivity ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints"), we find that the MGGD can accommodate both excess-kurtosis and low-kurtosis regimes, with the remaining challenge primarily related to tail thickness. For the excess-kurtosis behavior in the PF, a nonparametric observation model could be considered, while for fat tails more generally, jump-diffusion dynamics (as in Brigo et al. [[6](https://arxiv.org/html/2511.17892v1#bib.bib6)]) provide a natural extension.

#### Runtime and Implementation.

The run times for the three filter-assisted machine learning models are very different: the KF model runs in a couple of minutes, the EKF takes a few seconds to finish 1 epoch depending on the number of daily observations, and the training time of the PF increases exponentially as the number of particles increase which can take a few hours with 300 particles.333We run our models on Google Colab around 30∼\sim60 epochs which shows the optimal result without significant bias.

#### Particle filter settings.

Forecast accuracy is stable across reasonable particle counts; runtime scales with particle number and resampling schedule. The effective sample size (ESS) shown in Figures [5.15](https://arxiv.org/html/2511.17892v1#S5.F15 "Figure 5.15 ‣ Particle filter settings. ‣ 5.5 Robustness and Sensitivity ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") and [5.16](https://arxiv.org/html/2511.17892v1#S5.F16 "Figure 5.16 ‣ Particle filter settings. ‣ 5.5 Robustness and Sensitivity ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") presents the variance of the particles over the maximum number of particles (300). The value of ESS is between 0 and 100%100\% and the threshold in adaptive resampling is usually at 50%50\%. In other words, if the ESS is less than half of the total number of particles (ESS < N/2N/2), then the particle filter is considered inefficient and resampling is necessary. In our application, we run systematic resampling at every time step instead of an adaptive method and examine the efficiency of the particle filter using the ESS. In Figure [5.15](https://arxiv.org/html/2511.17892v1#S5.F15 "Figure 5.15 ‣ Particle filter settings. ‣ 5.5 Robustness and Sensitivity ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints"), we vary the arbitrage regularization parameter on or off (λ=0,1\lambda=0,1) and compare the ESS with MGGD shape parameter p=1.5p=1.5. The small initial value of ESS in the first step is due to the inexact initial particles which are sampled from the sample means of the estimated state variables and are not exactly the accurate initials for the forward rate curve. The result in Figure [5.15](https://arxiv.org/html/2511.17892v1#S5.F15 "Figure 5.15 ‣ Particle filter settings. ‣ 5.5 Robustness and Sensitivity ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints") shows the ESS of the particles stays above 85%85\% in the training set and decays to 60%60\% in the testing set over time, which also indicates that the particle filter does not suffer from serious degeneracy. In Figure [5.16](https://arxiv.org/html/2511.17892v1#S5.F16 "Figure 5.16 ‣ Particle filter settings. ‣ 5.5 Robustness and Sensitivity ‣ 5 Empirical Results ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints"), we vary pp, the shape parameter of the MGGD distribution, and compare the ESS with arbitrage regularization on (λ=1\lambda=1). We observe that the MGGD with p=0.62p=0.62 has much higher ESS in the later time steps and the ESS is not decaying in the testing set. Later, we show that the optimal value of pp is around 0.620.62 in the error distribution of the predicted bond prices. Therefore, we conclude that the particle filter with multivariate generalized Gaussian distribution is very efficient and stable for bond prices forecasting in both training and testing data.

Figure 5.15: U.S. Treasuries: Effective sample size with different regularization parameter λ\lambda

![Refer to caption](x15.png)



Figure 5.16: U.S. Treasuries: Effective sample size with different shape parameter pp

![Refer to caption](x16.png)



Figure 5.17: U.S.Treasuries: Price error distribution of 1-day-ahead forecasting

![Refer to caption](figures/price_error_dist_testing.jpg)

## 6 Conclusion

We develop an arbitrage-aware forecasting framework that combines state-space filters (KF/EKF/PF) with a deep architecture for time-varying parameters and an explicit no-arbitrage training penalty (AER). Empirically, AER delivers the largest gains at short maturities and at the 5-day horizon, improving bid–ask hit rates while keeping MAE/RMSE competitive (Section 5). Methodologically, the approach bridges HJM/AFNS with neural time-series encoders (LSTM/CLSTM) and differentiable filtering modules, using AER both as a training signal and an ex post diagnostic of arbitrage consistency (cf. [[34](https://arxiv.org/html/2511.17892v1#bib.bib34)]).

Looking ahead, we see three natural extensions: (i) adapting the framework to post-LIBOR overnight-rate curves with expected jumps (e.g., [[21](https://arxiv.org/html/2511.17892v1#bib.bib21)]); (ii) evaluating data-assisted filters—such as KalmanNet-style estimators—within our framework without altering the rest of the methodology [[45](https://arxiv.org/html/2511.17892v1#bib.bib45), [12](https://arxiv.org/html/2511.17892v1#bib.bib12), [47](https://arxiv.org/html/2511.17892v1#bib.bib47)], and attention-based state-estimation methods with theoretical guarantees (e.g., Horváth et al. [[28](https://arxiv.org/html/2511.17892v1#bib.bib28)]); and (iii) pairing AER with arbitrage-consistent neural-SDE or other generative models for scenario analysis (e.g., [[10](https://arxiv.org/html/2511.17892v1#bib.bib10)]). Because parameters are learned by gradient-based optimization under a no-arbitrage penalty, the method is suitable for day-to-day pricing, model monitoring, and risk-aware short- to medium-horizon forecasts, with the strongest gains observed at the 5-day horizon. In this context, the empirical analysis is intentionally confined to the pre-COVID period 2017–2019 in order to avoid structural breaks associated with the pandemic and subsequent monetary policy regime shifts. While this limits regime coverage, it allows for a controlled evaluation of arbitrage-free regularization under comparatively stable market conditions. Importantly, the proposed methodology is independent of any particular market environment and can be directly applied to more volatile or stressed periods when comparable data become available. Incorporating term-structure derivatives and macroeconomic features into estimation is also a natural extension for deeper empirical study.

We implemented Kalman, extended Kalman, and particle filters in TensorFlow and integrated a forward–rate term-structure model into a neural encoder to forecast bond prices. The arbitrage-regularization penalty (AER) is embedded in a Nelson–Siegel–type forward-rate specification and calibrated on time series of coupon bonds under a strong no-arbitrage requirement. The forward-rate model can be extended to the four-parameter Svensson family (and higher orders) while retaining the same no-arbitrage regularization.
Our empirical analysis evaluates both yields and prices, with the most pronounced improvements under arbitrage regularization observed in price-based metrics, particularly 5-day-ahead hit rates and dollar-denominated MAE.
The combination of a theoretically motivated term-structure model with a multi-layer neural architecture (LSTM/CLSTM) produces accurate forecasts. The AER penalty quantifies departures from no-arbitrage and serves as an ex post diagnostic in addition to improving fit. We find that incorporating AER *does not inherently degrade* forecast accuracy; rather, its effect depends on horizon and maturity.

For practical use, different filters trade accuracy for computation. A *KF* in yield-space is fastest but requires extracting yields from prices. An *EKF* in price-space offers a good accuracy–runtime balance. A *PF* in price-space with MGGD observation noise and systematic resampling is the most computationally demanding but accommodates non-Gaussian residuals. In our data, the empirical price-error distribution is markedly non-Gaussian; PF performance improves as the MGGD shape approaches Laplace, consistent with heavier-tailed noise.

The arbitrage penalty derived from the forward-rate model is compatible with a range of fixed-income pricing models. Its implementation adds modest computational overhead, and its benefits are most visible in the settings emphasized here. As noted by Christensen et al. [[8](https://arxiv.org/html/2511.17892v1#bib.bib8)] and Diebold and Li [[14](https://arxiv.org/html/2511.17892v1#bib.bib14)], no-arbitrage models remain approximations; even when absence of arbitrage is enforced in theory, small violations can appear in empirical implementations. The periodic behavior we observe in AER across maturities suggests uses in portfolio monitoring and risk management; future work can quantify AER further to flag potential over- or under-valuation. Heavy-tail features may also be modeled via mean-reverting dynamics with jumps. The flexibility of our neural encoder and the dynamic parameterization create a platform for studying classical no-arbitrage theory with richer data and extensions (e.g., Svensson curves, derivatives, macroeconomic factors).

These results demonstrate that enforcing financial structure within deep learning architectures can significantly improve the stability, interpretability, and realism of fixed-income forecasts.

## References

* Akiyama and Matsuyama [2025]

  S. Akiyama and N. Matsuyama.
  Yield curve extrapolation with machine learning.
  *ASTIN Bulletin*, 55(1):76–96, 2025.
* Ang and Piazzesi [2003]

  A. Ang and M. Piazzesi.
  A no-arbitrage vector autoregression of term structure dynamics with
  macroeconomic and latent variables.
  *Journal of Monetary Economics*, 50(4):745–787, 2003.
* Bie et al. [2024]

  S. Bie, F. X. Diebold, J. He, and J. Li.
  Machine learning and the yield curve: Tree-based macroeconomic regime
  switching.
  Available at arXiv, 2024.
  URL <https://arxiv.org/abs/2408.12863>.
* Björk and Svensson [2001]

  T. Björk and L. Svensson.
  On the existence of finite-dimensional realizations for nonlinear
  forward rate models.
  *Mathematical Finance*, 11(2):205–243,
  2001.
* Bliss [1997]

  R. R. Bliss.
  Testing term structure estimation methods.
  *Advances in Futures and Options Research*, 9:197–231, 1997.
* Brigo et al. [2007]

  D. Brigo, A. Dalessandro, M. Neugebauer, and F. Triki.
  A stochastic processes toolkit for risk management.
  Available at SSRN, 2007.
  URL <https://ssrn.com/abstract=1109160>.
* Caldeira et al. [2025]

  J. F. Caldeira, M. O. Silva, R. d. S. Bueno, and J. M. García-João.
  Forecasting the yield curve: The role of additional and time-varying
  decay parameters, conditional heteroscedasticity, and macroeconomic factors.
  *Journal of Time Series Analysis*, 46(1):e6214, 2025.
* Christensen et al. [2011]

  J. H. Christensen, F. X. Diebold, and G. D. Rudebusch.
  The affine arbitrage-free class of Nelson–Siegel term structure
  models.
  *Journal of Econometrics*, 164(1):4–20,
  2011.
* Christoffersen et al. [2014]

  P. Christoffersen, C. Dorion, K. Jacobs, and L. Karoui.
  Nonlinear Kalman filtering in affine term structure models.
  *Management Science*, 60(9):2248–2268,
  2014.
* Cohen et al. [2023]

  S. N. Cohen, C. Reisinger, and S. Wang.
  Arbitrage-free neural-SDE market models.
  *Applied Mathematical Finance*, 30(1):1–46,
  2023.
* Cuchiero et al. [2024]

  C. Cuchiero, C. Fontana, and A. Gnoatto.
  Deep learning of data-driven Heath–Jarrow–Morton models.
  Abstract, 4th Italian Meeting on Probability and Mathematical
  Statistics, 2024.
  URL <https://probabilityrome2024.it/pr2024/papers/370/>.
* Dahan et al. [2023]

  Y. Dahan, G. Revach, J. Dunik, and N. Shlezinger.
  Bayesian kalmannet: Quantifying uncertainty in deep learning
  augmented Kalman filter, 2023.
  arXiv:2309.03058.
* Dahan et al. [2025]

  Y. Dahan, G. Revach, N. Shlezinger, R. J. G. van Sloun, and Y. C. Eldar.
  Bayesian KalmanNet: Quantifying uncertainty in deep
  learning-augmented Kalman filters.
  Available at arXiv, 2025.
  URL <https://arxiv.org/abs/2309.03058>.
* Diebold and Li [2006]

  F. X. Diebold and C. Li.
  Forecasting the term structure of government bond yields.
  *Journal of Econometrics*, 130(2):337–364,
  2006.
* Diebold et al. [2006]

  F. X. Diebold, G. D. Rudebusch, and S. B. Aruoba.
  The macroeconomy and the yield curve: a dynamic latent factor
  approach.
  *Journal of Econometrics*, 131(1-2):309–338, 2006.
* Diebold et al. [2008]

  F. X. Diebold, C. Li, and V. Z. Yue.
  Global yield curve dynamics and interactions: a dynamic
  Nelson–Siegel approach.
  *Journal of Econometrics*, 146(2):351–363,
  2008.
* Duffee [1999]

  G. R. Duffee.
  Estimating the price of default risk.
  *The Review of Financial Studies*, 12(1):197–226, 1999.
* Duffie [2005]

  D. Duffie.
  Credit risk modeling with affine processes.
  *Journal of Banking & Finance*, 29(11):2751–2802, 2005.
* Ejsing et al. [2012]

  J. Ejsing, M. Grothe, and O. Grothe.
  Liquidity and credit risk premia in government bond yields.
  ECB, Working Paper. No. 1440, 2012.
  URL <https://ssrn.com/abstract=2065975>.
* Fontana et al. [2023]

  C. Fontana, S. Pavarana, and W. J. Runggaldier.
  A stochastic control perspective on term structure models with
  roll-over risk.
  *Finance and Stochastics*, 27(4):903–932,
  2023.
* Fontana et al. [2024a]

  C. Fontana, Z. Grbac, and T. Schmidt.
  Term structure modeling with overnight rates beyond stochastic
  continuity.
  *Mathematical Finance*, 34(1):151–189,
  2024a.
* Fontana et al. [2024b]

  C. Fontana, E. Platen, and S. Tappe.
  Real-world models for multiple term structures: A unifying HJM
  semimartingale framework.
  Available at arXiv, 2024b.
  URL <https://arxiv.org/abs/2411.01983>.
* Fontana et al. [2025]

  C. Fontana, G. Lanaro, and A. Murgoci.
  The geometry of multi-curve interest rate models.
  *Quantitative Finance*, 25(2):323–342,
  2025.
* Ganguli and Dunnmon [2017]

  S. Ganguli and J. Dunnmon.
  Machine learning for better models for predicting bond prices.
  Available at arXiv, 2017.
  URL <https://arxiv.org/abs/1705.01142>.
* Gao [2021]

  X. Gao.
  *Stochastic control, numerical methods, and machine learning in
  finance and insurance*.
  PhD thesis, Concordia University, March 2021.
  URL <https://spectrum.library.concordia.ca/id/eprint/988412/>.
* Heath et al. [1992]

  D. Heath, R. Jarrow, and A. Morton.
  Bond pricing and the term structure of interest rates: A new
  methodology for contingent claims valuation.
  *Econometrica: Journal of the Econometric Society*, pages
  77–105, 1992.
* Hochreiter and Schmidhuber [1997]

  S. Hochreiter and J. Schmidhuber.
  Long short-term memory.
  *Neural Computation*, 9(8):1735–1780, 1997.
* Horváth et al. [2025]

  B. Horváth, A. Kratsios, Y. Limmer, and X. Yang.
  Transformers can solve non-linear and non-Markovian filtering
  problems in continuous time for conditionally Gaussian signals.
  Available at arXiv, 2025.
  URL <https://arxiv.org/abs/2310.19603>.
* Jankowitsch et al. [2011]

  R. Jankowitsch, A. Nashikkar, and M. G. Subrahmanyam.
  Price dispersion in OTC markets: A new measure of liquidity.
  *Journal of Banking & Finance*, 35(2):343–357, 2011.
* Javaheri et al. [2003]

  A. Javaheri, D. Lautier, and A. Galli.
  Filtering in finance.
  *Wilmott*, 3:67–83, 2003.
* Jo et al. [2025]

  H. Jo, Y. Ahn, M. J. Kim, and B.-G. Jang.
  Advancing yield curve forecasting: Deep learning Nelson–Siegel
  models and macroeconomic insights.
  Available at SSRN, 2025.
  URL <https://ssrn.com/abstract=5228495>.
* Kauffmann et al. [2022]

  P. C. Kauffmann, H. H. Takada, A. T. Terada, and J. M. Stern.
  Learning forecast-efficient yield curve factor decompositions with
  neural networks.
  *Econometrics*, 10(2), 2022.
* Kitagawa [1996]

  G. Kitagawa.
  Monte Carlo filter and smoother for non-Gaussian nonlinear
  state space models.
  *Journal of Computational and Graphical Statistics*, 5(1):1–25, 1996.
* Kratsios and Hyndman [2020]

  A. Kratsios and C. B. Hyndman.
  Deep arbitrage-free learning in a generalized HJM framework via
  arbitrage-regularization.
  *Risks*, 8(2):40, 2020.
* Lee [2023]

  S.-H. Lee.
  Yield curve forecasting using deep learning Nelson–Siegel model.
  Available at SSRN, May 2023.
  URL <https://ssrn.com/abstract=4447541>.
* Litterman and Scheinkman [1991]

  R. Litterman and J. Scheinkman.
  Common factors affecting bond returns.
  *Journal of Fixed Income*, 1(1):54–61,
  1991.
* Liu [2008]

  J. S. Liu.
  *Monte Carlo Strategies in Scientific Computing*.
  Springer, New York, NY, 2008.
* Lyashenko et al. [2024a]

  A. Lyashenko, F. Mercurio, and A. Sokol.
  Autoencoder-based risk-neutral model for interest rates.
  Available at SSRN, 2024a.
  URL <https://ssrn.com/abstract=4836728>.
* Lyashenko et al. [2024b]

  A. Lyashenko, F. Mercurio, and A. Sokol.
  Machine learning for interest rates: Using auto-encoders for the
  risk-neutral modeling of yield curves.
  Available at SSRN, 2024b.
  URL <https://ssrn.com/abstract=4967989>.
* Nelson and Siegel [1987]

  C. R. Nelson and A. F. Siegel.
  Parsimonious modeling of yield curves.
  *Journal of Business*, 60(4):473–489, 1987.
* Nunes et al. [2025]

  M. Nunes, E. Gerding, F. McGroarty, M. Niranjan, and G. Sermpinis.
  Deep learning for bond yield forecasting: The LSTM–LagLasso.
  *International Journal of Finance & Economics*, pages 1–15,
  2025.
  In press.
* Opschoor and van der Wel [2025]

  A. Opschoor and M. van der Wel.
  A smooth shadow-rate dynamic Nelson–Siegel model for yields at
  the zero lower bound.
  *Journal of Business & Economic Statistics*, 43(2):298–311, 2025.
* Pascal et al. [2013]

  F. Pascal, L. Bombrun, J.-Y. Tourneret, and Y. Berthoumieu.
  Parameter estimation for multivariate generalized Gaussian
  distributions.
  *IEEE Transactions on Signal Processing*, 61(23):5960–5971, 2013.
* Pogorelsky et al. [2022]

  B. Pogorelsky, K. Michaelson, and R. Zanetti.
  Particle filter with LMMSE importance sampling.
  In *Proceedings of the 2022 25th International Conference on
  Information Fusion (FUSION)*. IEEE, 2022.
* Revach et al. [2022]

  G. Revach, N. Shlezinger, X. Ni, A. L. Escoriza, R. J. G. van Sloun, and Y. C.
  Eldar.
  KalmanNet: Neural network aided Kalman filtering for partially
  known dynamics.
  *IEEE Transactions on Signal Processing*, 70:1532–1547, 2022.
* Richman and Scognamiglio [2024]

  R. Richman and S. Scognamiglio.
  Multiple yield curve modeling and forecasting using deep learning.
  *ASTIN Bulletin*, 54(3):463–494, 2024.
* Shlezinger and Eldar [2023]

  N. Shlezinger and Y. C. Eldar.
  Model-based deep learning.
  *Foundations and Trends in Signal Processing*, 17(4):291–416, 2023.
* Svensson [1994]

  L. E. Svensson.
  Estimating and interpreting forward interest rates: Sweden 1992-1994.
  Technical report, National Bureau of Economic Research, 1994.
* Vuletić and Cont [2025]

  M. Vuletić and R. Cont.
  VolGAN: A generative model for arbitrage-free implied volatility
  surfaces.
  *Applied Mathematical Finance*, 31(4):203–238, 2025.
* Xian et al. [2024]

  Z. Xian, X. Yan, C. H. Leung, and Q. Wu.
  Risk-neutral generative networks.
  Available at arXiv, 2024.
  URL <https://arxiv.org/abs/2405.17770>.

## Appendix A Particle filtering implementation

The conditional expected value of XtX\_{t} from the previous state Xt−1X\_{t-1} given observations Y1:t−1=y1:t−1Y\_{1:t-1}=y\_{1:t-1} is denoted as the posterior distribution p​(Xt|Y1:t−1)p(X\_{t}\left|Y\_{1:{t-1}}\right.). The calculation of the expectation is estimated by Monte Carlo sampling

|  |  |  |
| --- | --- | --- |
|  | 𝔼𝕡​[f​(X)]=f​(X1)+f​(X2)+⋯+f​(XN)N.\mathbb{E}^{\mathbb{p}}\left[f(X)\right]=\frac{f(X\_{1})+f(X\_{2})+\cdots+f(X\_{N})}{N}. |  |

In practice, it is difficult to sample from the posterior distribution p​(Xk|Y1:k)p(X\_{k}\left|Y\_{1:k}\right.). We assume that we can sample from some prior distribution q​(Xk|Y1:k)q(X\_{k}\left|Y\_{1:k}\right.) called the importance distribution, then we can estimate the conditional expectation through the following steps

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼𝕡​[f​(Xt)|Y1:t]=\displaystyle\mathbb{E}^{\mathbb{p}}\left[f(X\_{t})\left|Y\_{1:t}\right.\right]= | ∫f​(Xt)​p​(Xt|Y1:t)​𝑑Xt\displaystyle\int f(X\_{t})p(X\_{t}|Y\_{1:t})dX\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∫f​(Xt)​p​(Xt|Y1:t)q​(Xt|Y1:t)​q​(Xt|Y1:t)​𝑑Xt\displaystyle\int f(X\_{t})\frac{p(X\_{t}|Y\_{1:t})}{q(X\_{t}|Y\_{1:t})}q(X\_{t}|Y\_{1:t})dX\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 1p​(Y1:t)​∫f​(Xt)​p​(Y1:t|Xt)​p​(Xt)q​(Xt|Y1:t)​q​(Xt|Y1:t)​𝑑Xt\displaystyle\frac{1}{p(Y\_{1:t})}\int f(X\_{t})\frac{p(Y\_{1:t}|X\_{t})p(X\_{t})}{q(X\_{t}|Y\_{1:t})}q(X\_{t}|Y\_{1:t})dX\_{t} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∫f​(Xt)​wt​(Xt)​q​(Xt|Y1:t)​𝑑Xt∫wt​(Xt)​q​(Xt|Y1:t)​𝑑Xt\displaystyle\frac{\int f(X\_{t})w\_{t}(X\_{t})q(X\_{t}|Y\_{1:t})dX\_{t}}{\int w\_{t}(X\_{t})q(X\_{t}|Y\_{1:t})dX\_{t}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | =\displaystyle= | 𝔼q​[wt​(Xt)​f​(Xt)|Y1:t]𝔼q​[wt​(Xt)|Y1:t],\displaystyle\frac{\mathbb{E}^{q}\left[w\_{t}(X\_{t})f(X\_{t})|Y\_{1:t}\right]}{\mathbb{E}^{q}\left[w\_{t}(X\_{t})|Y\_{1:t}\right]}, |  | (A.1) |

where

|  |  |  |
| --- | --- | --- |
|  | wt​(Xt)=p​(Y1:t|Xt)​p​(Xt)q​(Xt|Y1:t).w\_{t}(X\_{t})=\frac{p(Y\_{1:t}|X\_{t})p(X\_{t})}{q(X\_{t}|Y\_{1:t})}. |  |

The calculation of ([A](https://arxiv.org/html/2511.17892v1#A1.Ex2 "Appendix A Particle filtering implementation ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints")) can be estimated by sampling {Xt(i)}∼q​(Xt|Y1:t)\{X\_{t}^{(i)}\}\sim q(X\_{t}|Y\_{1:t}) for i=1,⋯,Ni=1,\cdots,N. That is,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼ℚ​[f​(Xt)|Y1:t]=\displaystyle\mathbb{E}^{\mathbb{Q}}\left[f(X\_{t})\left|Y\_{1:t}\right.\right]= | 𝔼q​[wt​(Xt)​f​(Xt)|Y1:t]𝔼q​[wt​(Xt)|Y1:t]\displaystyle\frac{\mathbb{E}^{q}\left[w\_{t}(X\_{t})f(X\_{t})\left|Y\_{1:t}\right.\right]}{\mathbb{E}^{q}\left[w\_{t}(X\_{t})\left|Y\_{1:t}\right.\right]} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | 1N​∑i=1Nwt​(Xt(i))​f​(Xt(i))1N​∑i=1Nwt​(Xt(i))\displaystyle\frac{\frac{1}{N}\sum\_{i=1}^{N}w\_{t}(X\_{t}^{(i)})f(X\_{t}^{(i)})}{\frac{1}{N}\sum\_{i=1}^{N}w\_{t}(X\_{t}^{(i)})} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | =\displaystyle= | ∑i=1Nw^t​(Xt(i))​f​(Xt(i)),\displaystyle\sum\_{i=1}^{N}\hat{w}\_{t}(X\_{t}^{(i)})f(X\_{t}^{(i)}), |  |

where w^t\hat{w}\_{t} are normalized weights

|  |  |  |
| --- | --- | --- |
|  | w^t​(Xt(i))=wt​(Xt(i))∑i=1Nwt​(Xt(i)).\hat{w}\_{t}(X\_{t}^{(i)})=\frac{w\_{t}(X\_{t}^{(i)})}{\sum\_{i=1}^{N}w\_{t}(X\_{t}^{(i)})}. |  |

Suppose the prior distribution q​(⋅)q(\cdot) satisfies the Markov property, then we can rewrite wkw\_{k} as a recursive identity

|  |  |  |
| --- | --- | --- |
|  | wt(i)=wt−1(i)​p​(Yt|Xt(i))​p​(Xt(i)|Xt−1(i))q​(Xt(i)|Xt−1(i),Y1:t).w\_{t}^{(i)}=w\_{t-1}^{(i)}\frac{p\left(Y\_{t}\big|X\_{t}^{(i)}\right)p\left(X\_{t}^{(i)}\big|X\_{t-1}^{(i)}\right)}{q\left(X\_{t}^{(i)}\big|X\_{t-1}^{(i)},Y\_{1:t}\right)}. |  |

If we choose the prior distribution q​(Xt|Xt−1,Y1:t)=p​(Xt|Xt−1)q\left(X\_{t}\big|X\_{t-1},Y\_{1:t}\right)=p\left(X\_{t}\big|X\_{t-1}\right) which is also widely used, we obtain the simple recursion

|  |  |  |
| --- | --- | --- |
|  | wt(i)=wt−1(i)​p​(Yt|Xt(i)).w\_{t}^{(i)}=w\_{t-1}^{(i)}p\left(Y\_{t}\big|X\_{t}^{(i)}\right). |  |

This choice of prior distribution does not incorporate the most recent observations YtY\_{t}, so it is inefficient. Javaheri et al. [[30](https://arxiv.org/html/2511.17892v1#bib.bib30)] propose using the extended Kalman filter to obtain the posterior information from the observations. The following distribution with prior mean X^k−1|k−1\hat{X}\_{k-1|k-1} and posterior covariance Pk−1P\_{k-1} from the extended Kalman filter

|  |  |  |
| --- | --- | --- |
|  | q​(Xk|Xk−1,Y1:k)=𝒩​(Xk|g​(X^k−1|k−1),Pk−1),q\left(X\_{k}\big|X\_{k-1},Y\_{1:k}\right)=\mathcal{N}\left(X\_{k}\left|g(\hat{X}\_{k-1|k-1}),P\_{k-1}\right.\right), |  |

gives one way to implement the importance sampling in particle filter.

Standard importance sampling suffers the variance explosion problem since some particles may have increasingly large weights and others have very small weights. The variance of weights increases exponentially with respect the number of particles. This degeneration problem decreases the effectiveness of particles and increases variance of the weights. To address this problem, a resampling step is introduced into the recursive procedure. The resampling is equivalent to resample each particle in such a way that their offspring ot=(ot[1],⋯,ot[N])o\_{t}=\left(o^{[1]}\_{t},\cdots,o^{[N]}\_{t}\right) follows a multinomial distribution with parameter vector (N,w^t)\left(N,\hat{w}\_{t}\right) and each particle is distributed with equally probability of 1/N1/N. The resampled distribution is an unbiased estimation of the original particle distribution. As a consequence, resampling carries the computational efforts to retain the particles in dense probability mass by precluding the particles of low weights with high probability. The most widely-used resampling method is systematic resampling introduced by Kitagawa [[33](https://arxiv.org/html/2511.17892v1#bib.bib33)] which we introduce in the algorithm.

On the other hand, resampling also has disadvantages. There could be the situation that a particle having a low weight could have a high weight at the next time and if this happens then resampling could be wasteful. Another immediate effect of resampling is some extra noise being introduced. One way we need resampling to control variance of weights and one way we do not want introduce additional variance. However, a controlled variance of weights benefits more from the additional variance noise after resampling. In practice, it is more sensible to resample only when the variance of the normalized weights reaches some threshold. The commonly used threshold (see Liu [[37](https://arxiv.org/html/2511.17892v1#bib.bib37)]) is the Effective Sample Size (ESS)

|  |  |  |
| --- | --- | --- |
|  | ESS=(∑i=1N(w^t(i))2)−1.\text{ESS}=\left(\sum\_{i=1}^{N}\left(\hat{w}^{(i)}\_{t}\right)^{2}\right)^{-1}. |  |

The ESS takes values between 11 and NN and resampling is usually done when ESS is below N/2N/2. This method is called adaptive resampling. In our application we do not apply the adaptive method but we examine the efficiency of our model by investigating the ESS after the training.

Sequential importance resampling (SIR) particle filter

* At time k=0k=0
* 1.

  Sample initial X0(i)X^{(i)}\_{0} from the initial states

  |  |  |  |
  | --- | --- | --- |
  |  | X0(i)=X^0+P^0​W(i),X^{(i)}\_{0}=\hat{X}\_{0}+\hat{P}\_{0}W^{(i)}, |  |

  where P0=P^0​P^0TP\_{0}=\hat{P}\_{0}\hat{P}\_{0}^{T} is the prior covariance matrix and W(i)W^{(i)} is standard Gaussian random number.
* 2.

  Update weights by initial observations and resampling to obtain equally distributed particles {X0(i),w0(i)=1/N}\{X^{(i)}\_{0},w\_{0}^{(i)}=1/N\}.
* From time k≥1k\geq 1
* 1.

  Importance sampling:

  From the measurement and updating equations given by ([3.2](https://arxiv.org/html/2511.17892v1#S3.Ex18 "3.2 Price forecasting using the extended Kalman filter ‣ 3 Forecasting framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints")) and ([3.2](https://arxiv.org/html/2511.17892v1#S3.Ex19 "3.2 Price forecasting using the extended Kalman filter ‣ 3 Forecasting framework ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints")) in EKF, we obtain the posterior particles along with the posterior covariance

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | X^k−1|k−1(i)=\displaystyle\hat{X}^{(i)}\_{k-1|k-1}= | Xk−1(i)+Kk−1​vk−1(i),\displaystyle X^{(i)}\_{k-1}+K\_{k-1}v^{(i)}\_{k-1}, |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Pk−1|k−1(i)=\displaystyle P^{(i)}\_{k-1|k-1}= | Pk−1(i)−Kk−1​Mk−1​Pk−1(i),\displaystyle P^{(i)}\_{k-1}-K\_{k-1}M\_{k-1}P^{(i)}\_{k-1}, |  |

  then we sample particles from the posterior space

  |  |  |  |
  | --- | --- | --- |
  |  | Xk(i)=Ak−1​X^k−1|k−1(i)+Dk−1+Pk(i)​W(i),\displaystyle X^{(i)}\_{k}=A\_{k-1}\hat{X}^{(i)}\_{k-1|k-1}+D\_{k-1}+\sqrt{P^{(i)}\_{k}}W^{(i)}, |  |

  where

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Pk(i)\displaystyle P^{(i)}\_{k} | =Ak−1T​Pk−1|k−1(i)​Ak−1+Qk−1,\displaystyle=A^{T}\_{k-1}P^{(i)}\_{k-1|k-1}A\_{k-1}+Q\_{k-1}, |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | vk−1i\displaystyle v^{i}\_{k-1} | =Yk−1−Y^​(tk−1,Xk−1(i)),\displaystyle=Y\_{k-1}-\hat{Y}(t\_{k-1},~X^{(i)}\_{k-1}), |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Fk−1\displaystyle F\_{k-1} | =Mk−1​Pk|k−1(i)​Mk−1T+Uk−1,\displaystyle=M\_{k-1}P^{(i)}\_{k|k-1}M^{T}\_{k-1}+U\_{k-1}, |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Kk−1\displaystyle K\_{k-1} | =Pk−1(i)​Mk−1T​Fk−1−1,\displaystyle=P^{(i)}\_{k-1}M\_{k-1}^{T}F\_{k-1}^{-1}, |  |
  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Mk−1\displaystyle M\_{k-1} | =∂Y^∂X|X=Xk−1(i).\displaystyle=\left.\frac{\partial\hat{Y}}{\partial X}\right|\_{X={X}^{(i)}\_{k-1}}. |  |
* 2.

  Update weights:

  |  |  |  |
  | --- | --- | --- |
  |  | wk(i)=wk−1(i)​p​(Yk|Xk(i))​p​(Xk(i)|Xk−1(i))q​(Xk(i)|xk−1(i),Y1:k),w\_{k}^{(i)}=w^{(i)}\_{k-1}\frac{p\left(Y\_{k}\big|X\_{k}^{(i)}\right)p\left(X\_{k}^{(i)}\big|X\_{k-1}^{(i)}\right)}{q\left(X\_{k}^{(i)}\big|x\_{k-1}^{(i)},Y\_{1:k}\right)}, |  |

  where

  |  |  |  |
  | --- | --- | --- |
  |  | p​(Yk|Xk(i))=ℳ​(Yk|Y^​(Xk(i)),Uk),\displaystyle p\left(Y\_{k}\big|X\_{k}^{(i)}\right)=\mathcal{M}\left(Y\_{k}\left|\hat{Y}(X\_{k}^{(i)}),U\_{k}\right.\right), |  |
  |  |  |  |
  | --- | --- | --- |
  |  | p​(Xk(i)|Xk−1(i))=𝒩​(Xk(i)|g​(Xk−1(i)),Qk−1),\displaystyle p\left(X\_{k}^{(i)}\big|X\_{k-1}^{(i)}\right)=\mathcal{N}\left(X\_{k}^{(i)}\left|g(X^{(i)}\_{k-1}),Q\_{k-1}\right.\right), |  |
  |  |  |  |
  | --- | --- | --- |
  |  | q​(Xk(i)|Xk−1(i),Y1:k)=𝒩​(Xk(i)|g​(Xk−1|k−1(i)),Pk(i)).\displaystyle q\left(X\_{k}^{(i)}\big|X\_{k-1}^{(i)},Y\_{1:k}\right)=\mathcal{N}\left(X\_{k}^{(i)}\left|g(X^{(i)}\_{k-1|k-1}),P^{(i)}\_{k}\right.\right). |  |

  Calculate normalized weights

  |  |  |  |
  | --- | --- | --- |
  |  | w¯k(i)=wk(i)∑i=1Nwk(i).\bar{w}\_{k}^{(i)}=\frac{w\_{k}^{(i)}}{\sum\_{i=1}^{N}w\_{k}^{(i)}}. |  |
* 3.

  Systematic Resampling from {w¯k(i),Xk(i),Pk(i)}\left\{\bar{w}^{(i)}\_{k},X^{(i)}\_{k},P^{(i)}\_{k}\right\} to obtain equally weighted particle sample {1N,Xk(i),Pk(i)}\left\{\frac{1}{N},X^{(i)}\_{k},P^{(i)}\_{k}\right\}

  + i.

    Set sk(i)=i−1+s~kNs^{(i)}\_{k}=\frac{i-1+\tilde{s}\_{k}}{N} with s~k∼𝒰​[0,1]\tilde{s}\_{k}\sim\mathcal{U}[0,1] for i=1,⋯,Ni=1,\cdots,N.
  + ii.

    Then set the number of particles equal to the offspring

    |  |  |  |
    | --- | --- | --- |
    |  | ok(i)=|{sk(j):∑n=1i−1w¯k(n)≤sk(j)≤∑n=1iw¯k(n)}|,o^{(i)}\_{k}=\left|\left\{s^{(j)}\_{k}:\sum\_{n=1}^{i-1}\bar{w}^{(n)}\_{k}\leq s^{(j)}\_{k}\leq\sum\_{n=1}^{i}\bar{w}^{(n)}\_{k}\right\}\right|, |  |

    which is the number of sk(j)s^{(j)}\_{k} that locates in [∑n=1i−1w¯k(n),∑n=1iw¯k(n)]\left[\sum\_{n=1}^{i-1}\bar{w}^{(n)}\_{k},\sum\_{n=1}^{i}\bar{w}^{(n)}\_{k}\right].

## Appendix B LSTM architecture

In this appendix we follow the standard formulation of Hochreiter and Schmidhuber [[27](https://arxiv.org/html/2511.17892v1#bib.bib27)]. The LSTM block takes as inputs xx and the output ct−1c\_{t-1} and hidden state ht−1h\_{t-1} from previous LSTM block and generates updated values of ctc\_{t} and hth\_{t} correspondingly:

|  |  |  |
| --- | --- | --- |
|  | (ct,ht)=L​(x,(ct−1,ht−1)).(c\_{t},h\_{t})=L(x,(c\_{t-1},h\_{t-1})). |  |

The equations of the LSTM are composed of the following four dense layers each serving a different purpose

|  |  |  |  |
| --- | --- | --- | --- |
|  | ft\displaystyle f\_{t} | =ag​(𝒲𝒻​𝓍+𝒲𝒻′​𝒽𝓉−1+𝒷𝒻),\displaystyle=a\_{g}\left(\mathpzc{W}\_{f}x+\mathpzc{W}^{\prime}\_{f}h\_{t-1}+\mathpzc{b}\_{f}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | it\displaystyle i\_{t} | =ag​(𝒲𝒾​𝓍+𝒲𝒾′​𝒽𝓉−1+𝒷𝒾),\displaystyle=a\_{g}\left(\mathpzc{W}\_{i}x+\mathpzc{W}^{\prime}\_{i}h\_{t-1}+\mathpzc{b}\_{i}\right), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ot\displaystyle o\_{t} | =ag​(𝒲ℴ​𝓍+𝒲ℴ′​𝒽𝓉−1+𝒷ℴ)\displaystyle=a\_{g}\left(\mathpzc{W}\_{o}x+\mathpzc{W}^{\prime}\_{o}h\_{t-1}+\mathpzc{b}\_{o}\right) |  | (B.1) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | c~t\displaystyle\tilde{c}\_{t} | =ac​(𝒲𝒸​𝓍+𝒲𝒸′​𝒽𝓉−1+𝒷𝒸),\displaystyle=a\_{c}\left(\mathpzc{W}\_{c}x+\mathpzc{W}^{\prime}\_{c}h\_{t-1}+\mathpzc{b}\_{c}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ct\displaystyle c\_{t} | =ft∘ct−1+it∘c~t,\displaystyle=f\_{t}\circ c\_{t-1}+i\_{t}\circ\tilde{c}\_{t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ht\displaystyle h\_{t} | =ot∘ah​(ct),\displaystyle=o\_{t}\circ a\_{h}\left(c\_{t}\right), |  |

where the operator ∘\circ denotes the Hadamard product (element-wise product). In each LSTM cell, we have four gates (or layers):
ftf\_{t}, iti\_{t}, oto\_{t} are the forget, input, and output gates; hth\_{t} is the hidden layer; ctc\_{t} is the cell state. The activation functions used are

|  |  |  |  |
| --- | --- | --- | --- |
|  | ag​(x)\displaystyle a\_{g}(x) | =11+e−x,\displaystyle=\frac{1}{1+e^{-x}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ac​(x)\displaystyle a\_{c}(x) | =tanh⁡(x),\displaystyle=\tanh(x), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ah​(x)\displaystyle a\_{h}(x) | =tanh⁡(x).\displaystyle=\tanh(x). |  |

For Xt∈ℝNX\_{t}\in\mathbb{R}^{N} with feature size NN and the predefined hidden units HH, the model weights and biases are predefined by

|  |  |  |
| --- | --- | --- |
|  | 𝒲,𝒲′∈ℝℋ×𝒩, and ​𝒷∈ℝℋ.\mathpzc{W},\mathpzc{W}^{\prime}\in\mathbb{R}^{H\times N},\text{ and }\mathpzc{b}\in\mathbb{R}^{H}. |  |

The input layer of the linear model (yield-space) with two connected LSTM L1L\_{1} and L2L\_{2} at time step tt with input YtY\_{t} can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | (ctI1,htI1)\displaystyle\left(c^{I\_{1}}\_{t},h^{I\_{1}}\_{t}\right) | =L1​(Yt,(ct−1I1,ht−1I1)),\displaystyle=L\_{1}\left(Y\_{t},\left(c^{I\_{1}}\_{t-1},h^{I\_{1}}\_{t-1}\right)\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (ctI2,htI2)\displaystyle\left(c^{I\_{2}}\_{t},h^{I\_{2}}\_{t}\right) | =L2​(ctI1,(ct−1I2,ht−1I2)),\displaystyle=L\_{2}\left(c^{I\_{1}}\_{t},\left(c^{I\_{2}}\_{t-1},h^{I\_{2}}\_{t-1}\right)\right), |  |

where ctI=ctI2c^{I}\_{t}=c^{I\_{2}}\_{t} is the output from input layer.

## Appendix C CLSTM architecture

The nonlinear model (price-space) is trained with the price data in a 44-dimensional tensor with a size of S×T×N×FS\times T\times N\times F where NN is the number of bonds and F=4F=4 is the feature size. The input data at each time step is then a N×FN\times F matrix that cannot be fed into a standard LSTM.
Hence, we apply a convolutional-LSTM (CLSTM) to decrease the input dimension from N×FN\times F to 1×H1\times H for an integer hyperparameter HH. We then connect it to the standard LSTM. The CLSTM is usually applied for image processing but we can consider our input as an image of single channel N×F×1N\times F\times 1 and use the convolution operation to obtain a vector output of any size HH. The compact forms of equations of the CLSTM are similar to the standard LSTM ([B](https://arxiv.org/html/2511.17892v1#A2.Ex2 "Appendix B LSTM architecture ‣ Arbitrage-Free Bond and Yield Curve Forecasting with Neural Filters under HJM Constraints")) but using convolution instead of matrix product

We first apply a convolutional–LSTM (CLSTM) to compress per-time-step cross-sectional features into HH channels, then feed the result into an LSTM for temporal dynamics.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ft=\displaystyle f\_{t}= | ag​(𝒲𝒻∗𝓍+𝒲𝒻′∗𝒽𝓉−1+𝒷𝒻),\displaystyle a\_{g}\left(\mathpzc{W}\_{f}\ast x+\mathpzc{W}^{\prime}\_{f}\ast h\_{t-1}+\mathpzc{b}\_{f}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | it=\displaystyle i\_{t}= | ag​(𝒲𝒾∗𝓍+𝒲𝒾′∗𝒽𝓉−1+𝒷𝒾),\displaystyle a\_{g}\left(\mathpzc{W}\_{i}\ast x+\mathpzc{W}^{\prime}\_{i}\ast h\_{t-1}+\mathpzc{b}\_{i}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ot=\displaystyle o\_{t}= | ag​(𝒲ℴ∗𝓍+𝒲ℴ′∗𝒽𝓉−1+𝒷ℴ),\displaystyle a\_{g}\left(\mathpzc{W}\_{o}\ast x+\mathpzc{W}^{\prime}\_{o}\ast h\_{t-1}+\mathpzc{b}\_{o}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | c~t=\displaystyle\tilde{c}\_{t}= | ac​(𝒲𝒸∗𝓍+𝒲𝒸′∗𝒽𝓉−1+𝒷𝒸),\displaystyle a\_{c}\left(\mathpzc{W}\_{c}\ast x+\mathpzc{W}^{\prime}\_{c}\ast h\_{t-1}+\mathpzc{b}\_{c}\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ct=\displaystyle c\_{t}= | ft∘ct−1+it∘c~t,\displaystyle f\_{t}\circ c\_{t-1}+i\_{t}\circ\tilde{c}\_{t}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ht=\displaystyle h\_{t}= | ot∘ah​(ct),\displaystyle o\_{t}\circ a\_{h}\left(c\_{t}\right), |  |

where the operator (∗)(\ast) denotes the convolution operation. The kernel of the convolution LSTM is defined by

|  |  |  |
| --- | --- | --- |
|  | 𝒲,𝒲′∈ℝ𝒦𝒲×𝒦ℋ×𝒦𝒟,\mathpzc{W},\mathpzc{W}^{\prime}\in\mathbb{R}^{K\_{W}\times K\_{H}\times K\_{D}}, |  |

with KWK\_{W} as width, KHK\_{H} as height and KDK\_{D} as depth. The convolution of 𝒲∈ℝKW×KH×KD\mathcal{W}\in\mathbb{R}^{K\_{W}\times K\_{H}\times K\_{D}} and x∈ℝN×F×1x\in\mathbb{R}^{N\times F\times 1} is a tensor of dimension

|  |  |  |
| --- | --- | --- |
|  | dim​(𝒲∗𝓍)=(⌊N+2​p−KWsW+1⌋,⌊F+2​p−KHsH+1⌋,KD),\text{dim}\left(\mathpzc{W}\ast x\right)=\left(\left\lfloor\frac{N+2p-K\_{W}}{s\_{W}}+1\right\rfloor,\left\lfloor\frac{F+2p-K\_{H}}{s\_{H}}+1\right\rfloor,K\_{D}\right), |  |

where pp is the size of padding typically set to 0, (sW,sH)\left(s\_{W},s\_{H}\right) is the size of stride, and the operator ⌊⋅⌋\lfloor\cdot\rfloor takes the integer part. To reduce the dimension of the input and obtain HH-dimensional vector output, we set stride size (sW,sH)=(1,1)(s\_{W},s\_{H})=(1,1) and kernel size (KW,KH,KD)=(⌊NH⌋,F,1)\left(K\_{W},K\_{H},K\_{D}\right)=\left(\lfloor\frac{N}{H}\rfloor,F,1\right) for some hyper-parameters H<NH<N, and eventually obtain an output with a size of (H,1,1)(H,1,1) which can be compressed to 1×H1\times H. We then connect it to a standard LSTM. The input layer for the nonlinear model (price-space) consisting of a CLSTM LcL\_{c} and a standard LSTM LL is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yt∈ℝN×F\displaystyle Y\_{t}\in\mathbb{R}^{N\times F} | :→Yt′∈ℝN×F×1,\displaystyle:\rightarrow Y\_{t}^{\prime}\in\mathbb{R}^{N\times F\times 1}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (ctIc,htIc)=\displaystyle\left(c^{I\_{c}}\_{t},h^{I\_{c}}\_{t}\right)= | Lc​(Yt′,(ct−1Ic,ht−1Ic)),\displaystyle L\_{c}\left(Y^{\prime}\_{t},\left(c^{I\_{c}}\_{t-1},h^{I\_{c}}\_{t-1}\right)\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ctIc∈ℝH×1×1\displaystyle c^{I\_{c}}\_{t}\in\mathbb{R}^{H\times 1\times 1} | :→ct′∈ℝ1×H,\displaystyle:\rightarrow c^{\prime}\_{t}\in\mathbb{R}^{1\times H}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | (ctI,htI)=\displaystyle\left(c^{I}\_{t},h^{I}\_{t}\right)= | L​(ct′,(ct−1I,ht−1I)).\displaystyle L\left(c^{\prime}\_{t},\left(c^{I}\_{t-1},h^{I}\_{t-1}\right)\right). |  |