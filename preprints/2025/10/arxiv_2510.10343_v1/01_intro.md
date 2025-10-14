---
authors:
- Giorgia Rensi
- Pietro Rossi
- Marco Bianchetti
doc_id: arxiv:2510.10343v1
family_id: arxiv:2510.10343
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Learning the Exact SABR Model
url_abs: http://arxiv.org/abs/2510.10343v1
url_html: https://arxiv.org/html/2510.10343v1
venue: arXiv q-fin
version: 1
year: 2025
---


Giorgia Rensi
Department of Statistical Sciences \csq@thequote@oinit\csq@thequote@oopenPaolo Fortunati\csq@thequote@oclose, University of Bologna, Italy

Pietro Rossi
Department of Statistical Sciences \csq@thequote@oinit\csq@thequote@oopenPaolo Fortunati\csq@thequote@oclose, University of Bologna, Italy
Prometeia S.p.a., Bologna, Italy
Corresponding author, Pietro Rossi

Marco Bianchetti
Department of Statistical Sciences \csq@thequote@oinit\csq@thequote@oopenPaolo Fortunati\csq@thequote@oclose, University of Bologna, Italy
Market and Financial Risk Management, Intesa Sanpaolo, Milan, Italy

(October 11, 2025)

###### Abstract

The SABR model is a cornerstone of interest rate volatility modeling, but its practical application relies heavily on the analytical approximation by Hagan et al., whose accuracy deteriorates for high volatility, long maturities, and out-of-the-money options, admitting arbitrage. While machine learning approaches have been proposed to overcome these limitations, they have often been limited by simplified SABR dynamics or a lack of systematic validation against the full spectrum of market conditions.

We develop a novel SABR DNN, a specialized Artificial Deep Neural Network (DNN) architecture that learns the true SABR stochastic dynamics using an unprecedented large training dataset (more than 200 million points) of interest rate Cap/Floor volatility surfaces, including very long maturities (30Y) and extreme strikes consistently with market quotations. Our dataset is obtained via high-precision unbiased Monte Carlo simulation of a special scaled shifted-SABR stochastic dynamics, which allows dimensional reduction without any loss of generality.
Our SABR DNN provides arbitrage-free calibration of real market volatility surfaces and Caps/Floors prices for any maturity and strike with negligible computational effort and without retraining across business dates.

Our results fully address the gaps in the previous machine learning SABR literature in a systematic and self-consistent way, and can be extended to cover any interest rate European options in different rate tenors and currencies, thus establishing a comprehensive functional SABR framework that can be adopted for daily trading and risk management activities.

JEL classifications: C45, C63, G12, G13.

Keywords: stochastic volatility; SABR, Hagan, model calibration; volatility surface; interest rate derivatives; Cap; Floor; Monte Carlo simulation; machine learning in finance; deep neural network.

Acknowledgements: M.B. acknowledges fruitful discussions with many colleagues at international conferences and at Risk Management, Financial Engineering and Trading Desks of Intesa Sanpaolo.

Disclaimer: the views expressed here are those of the authors and do not represent the opinions of their employers. They are not responsible for any use that may be made of these contents.

## 1 Introduction

### 1.1 Machine Learning in Pricing Model Calibration

The daily market risk management routine of banks dealing with large portfolios of financial instruments requires substantial computational resources to run a number of tasks: model calibration, instrument pricing and hedging, risk measurement, risk analyses, and reporting.
All the pricing measures used in this context depend on market variables and must be recalculated once the market moves significantly, even in real-time in the most complex situations.
Risk measures add another layer of complexity, since they are typically based on risk scenarios which require multiple model calibrations and portfolio valuations.
Hence, the quantitative finance community is continuously developing, on the one side, sophisticated models to properly manage complex portfolios and, on the other side, efficient algorithms to contain the required computational effort. The trade-off between these two competing objectives drives model selection, typically limiting the choice to less sophisticated models and approximate numerical techniques compatible with the available computational budget.

However, the repeated calculations described above are typically quite self-similar: most of the time large portfolios have a limited daily turnover and market data inputs change smoothly. Furthermore, the most relevant inputs are typically limited to a subset of market points (e.g. forward and volatility), trade parameters (e.g. maturity and strike), pricing model parameters (e.g. 1 for Black-Scholes, 4 for SABR, 5 for Heston, etc.) and risk model parameters (e.g. market risk historical series).
Clearly, this context offers an ideal setting for supervised machine learning techniques, where all the necessary input and output information can be encoded into a labeled dataset, which is used to train appropriate algorithms and learn the relevant pricing or risk function.
In particular, deep neural networks (DNNs) are designed to approximate unknown functions y=f​(x)y=f(x) that are available only through sample pairs of given input and output data {x,y}\{x,y\} using a mapping y^=f^​(x,w)\hat{y}=\hat{f}(x,w) where the parameters ww are calibrated to minimize some distance ‖y^−y‖\|\hat{y}-y\|. This task is feasible thanks to the universal approximation theorem [[11](https://arxiv.org/html/2510.10343v1#bib.bibx11)], [[21](https://arxiv.org/html/2510.10343v1#bib.bibx21)], also including function derivatives [[22](https://arxiv.org/html/2510.10343v1#bib.bibx22)] (provided that the activation function is smooth), with a maximum of three node layers [[12](https://arxiv.org/html/2510.10343v1#bib.bibx12)]. See the classic textbook [[15](https://arxiv.org/html/2510.10343v1#bib.bibx15)] for more details about Deep (Artificial) Neural Networks.

These interesting properties of DNNs are particularly useful in the case of *pricing model calibration*, which can be described as a inverse optimization problem: given a set of nm​k​tn\_{mkt} quoted plain-vanilla financial instruments, each characterized by a set of contract parameters θ𝒞∈ℝn\theta^{\mathcal{C}}\in\mathbb{R}^{n} and market price Vmkt​(θ𝒞)V^{\textit{mkt}}(\theta^{\mathcal{C}}) (e.g. European options characterized by maturity and strike, θ𝒞={T,K}∈ℝ2\theta^{\mathcal{C}}=\{T,K\}\in\mathbb{R}^{2}), and a pricing model ℳ\mathcal{M} depending on a set of model parameters θℳ∈ℝm\theta^{\mathcal{M}}\in\mathbb{R}^{m} which produces model prices Vℳ​(θ𝒞,θℳ)V^{\mathcal{M}}(\theta^{\mathcal{C}},\theta^{\mathcal{M}}), the model calibration amounts to estimate the model parameters θ^ℳ\hat{\theta}^{\mathcal{M}} such that model prices match market prices, Vℳ​(θ𝒞,θ^ℳ)≃Vmkt​(θ𝒞)V^{\mathcal{M}}(\theta^{\mathcal{C}},\hat{\theta}^{\mathcal{M}})\simeq V^{\textit{mkt}}(\theta^{\mathcal{C}}).
Both model and market prices are typically expressed as discrete two-dimensional implied volatility surfaces of maturities and strikes111In the case of interest rate Swaptions we have a three-dimensional cube of underlying swap tenors, maturities and strikes, θ𝒞∈ℝ3\theta^{\mathcal{C}}\in\mathbb{R}^{3}. Also interest rate Caps/Floors written on different IBOR tenors may be viewed as a volatility cube. Since Caplets/Floorlets may be viewed as Swaptions on a single-period Swap, the two cubes are interconnected. Volatilities are conventionally implied using normal or lognormal models, a.k.a. Bachelier or Black models, respectively, and appropriate numerical procedures. See e.g. [[9](https://arxiv.org/html/2510.10343v1#bib.bibx9)] for further details.
Note that we use the same notation θ𝒞\theta^{\mathcal{C}} to denote contract parameters both in case of a single contract, with θ𝒞∈ℝn\theta^{\mathcal{C}}\in\mathbb{R}^{n}, and in case of an entire market dataset of nm​k​tn\_{mkt} instruments, trusting on the clarity of the context., σℳ​(θ𝒞,θℳ),σmkt​(θ𝒞)\sigma^{\mathcal{M}}(\theta^{\mathcal{C}},\theta^{\mathcal{M}}),\sigma^{\textit{mkt}}(\theta^{\mathcal{C}}).
The numerical estimation procedure requires, in principle, a m−m-dimensional global optimization algorithm which computes nm​k​tn\_{mkt} prices in nsn\_{s} iterations until some convergence criteria is met, thus calling the ℳ−\mathcal{M}-model pricing function at least nm​k​t×nsn\_{mkt}\times n\_{s} times222Actually, population-based global optimization algorithms, such as Genetic Algorithms or Particle Swarm Optimization, consider multiple possible solutions nr∈ℕn\_{r}\in\mathbb{N} at each iteration, leading to nm​k​t×ns×nrn\_{mkt}\times n\_{s}\times n\_{r} calls of the pricing function..
Once the model is calibrated, it may be used to price other financial instruments consistently with the market plain-vanillas, which work as the natural hedges.
In principle, the model must be recalibrated after each significant market movement for real-time pricing applications, or to compute scenario-based risk measures, e.g. historical Value at Risk.
Clearly, this approach is feasible only when the pricing function
Vℳ​(θ𝒞,θℳ)V^{\mathcal{M}}(\theta^{\mathcal{C}},\theta^{\mathcal{M}})
can be computed using exact or approximated (semi)analytical formulas, a case occurring only for the simplest pricing models ℳ\mathcal{M}. If this condition is not met, one must resort to expensive numerical methods such as Monte Carlo simulation or PDE solution, which typically make the problem unfeasible in practice. This is known as the model calibration bottleneck.

A relatively recent stream of research (see e.g. [[3](https://arxiv.org/html/2510.10343v1#bib.bibx3)] and refs. therein) explores a DNN-based approach to model calibration, where the “online” calibration illustrated above is substituted by an “offline” pre-processing procedure, in which an appropriate DNN is trained on a large precomputed set of model prices Vℳ​(𝜽𝒞,𝜽ℳ)V^{\mathcal{M}}(\bm{\theta}^{\mathcal{C}},\bm{\theta}^{\mathcal{M}})
obtained via some numerical procedure (e.g. Monte Carlo simulation) using a large set of contract and model parameters {𝜽𝒞,𝜽ℳ}\{\bm{\theta}^{\mathcal{C}},\bm{\theta}^{\mathcal{M}}\} selected within appropriate domains.
In this way, the DNN “learns” the exact model pricing function
VNN​(𝜽𝒞,𝜽ℳ,w)≃Vℳ​(𝜽𝒞,𝜽ℳ)V^{\textit{NN}}(\bm{\theta}^{\mathcal{C}},\bm{\theta}^{\mathcal{M}},w)\simeq V^{\mathcal{M}}(\bm{\theta}^{\mathcal{C}},\bm{\theta}^{\mathcal{M}}),
where ww are the network weights, and the corresponding implied volatilities
σNN​(𝜽𝒞,𝜽ℳ,w)≃σℳ​(𝜽𝒞,𝜽ℳ)\sigma^{\textit{NN}}(\bm{\theta}^{\mathcal{C}},\bm{\theta}^{\mathcal{M}},w)\simeq\sigma^{\mathcal{M}}(\bm{\theta}^{\mathcal{C}},\bm{\theta}^{\mathcal{M}}),
in a wide variety of market situations, corresponding to the many different model and contract parameter values used to generate the training set.
Once the offline step is executed, the online step amounts to calibrate the model ℳ\mathcal{M} to market prices using the DNN, i.e. to estimate the model parameters θ^ℳ\hat{\theta}^{\mathcal{M}} such that VNN​(θ𝒞,θ^ℳ,w)≃Vmkt​(θ𝒞)V^{\textit{NN}}(\theta^{\mathcal{C}},\hat{\theta}^{\mathcal{M}},w)\simeq V^{\textit{mkt}}(\theta^{\mathcal{C}}),
a task that typically takes very short times thanks to the pure algebraic mathematical structure of the DNN.
Clearly, the production of the training set and the offline DNN training procedure is computationally expensive, but, provided that the training set is large enough to represent a sufficient variety of market volatility surfaces, it is not necessary to update it, except in the event of market regime changes.

### 1.2 The SABR Model

The SABR (Stochastic Alpha Beta Rho) is one of the most popular models in finance. It assumes a CEV (Constant Elasticity of Variance) stochastic dynamics of single forward quantities, i.e. rates or prices, with a correlated lognormal stochastic volatility. It was originally introduced by [[16](https://arxiv.org/html/2510.10343v1#bib.bibx16)] and later extended by [[17](https://arxiv.org/html/2510.10343v1#bib.bibx17)] to accommodate negative forwards.
The reasons behind the extraordinary success of the SABR model, despite the complexity of its stochastic dynamics, are the following.

* •

  Parsimony: the shifted-SABR stochastic dynamics depends on 5 parameters with a simple and transparent financial interpretation. In particular, the β\beta parameter allows the model to interpolate between normal (β=0\beta=0) and lognormal (β=1\beta=1) dynamics.
* •

  Analytical approximation: there exists a simple analytical approximation (a.k.a. Hagan et al. formula) of normal or lognormal SABR volatility implied in European option prices, which was originally derived in [[16](https://arxiv.org/html/2510.10343v1#bib.bibx16)] using singular perturbation techniques, and later improved in [[33](https://arxiv.org/html/2510.10343v1#bib.bibx33)] and [[17](https://arxiv.org/html/2510.10343v1#bib.bibx17)]. This approximation allows to price European options depending on a single forward rate simply using either the Bachelier (normal) or the Black (lognormal) analytical formulas (see e.g. [[9](https://arxiv.org/html/2510.10343v1#bib.bibx9)] for further details), even if the SABR dynamics is, in general, neither normal nor lognormal.
* •

  Calibration and performance: the two previous properties allow fast and precise calibration of the SABR model to fit typical volatility skew and smile shapes encountered on the market. The global optimization problem of volatility skew/smile calibration is, in principle, five-dimensional, but it may be reduced by fixing the shift parameter to some conventional value and by leveraging the β\beta parameter redundancy. The resulting three-dimensional problem may be managed by using standard numerical techniques, i.e. smart parameter guess and local Levenberg-Marquardt algorithms, as suggested e.g. by [[14](https://arxiv.org/html/2510.10343v1#bib.bibx14)].
* •

  Greeks and hedging: the Hagan et al. formula also allows to use either analytical formulas for greeks, making hedging and risk management immediate. Furthermore, contrary to local volatility models, the SABR stochastic volatility nature allows to capture the correct smile dynamics333when the underlying increases/decreases, the smile shifts to higher/lower prices. and provides more accurate and robust hedging, as discussed in the original paper [[16](https://arxiv.org/html/2510.10343v1#bib.bibx16)] and in more detail in [[18](https://arxiv.org/html/2510.10343v1#bib.bibx18)].

Thanks to the properties discussed above, the SABR model *plus* the Hagan et al. approximation became soon the most widely used approach to calibrate the interest rate volatility smile and to price the corresponding European options, i.e. interest rate Caps, Floors, Swaptions. The model is also used to price Constant Maturity Swaps (CMS) and CMS European options, where the convexity adjustment depends on the full volatility smile.
Since, as shown in tab. [7](https://arxiv.org/html/2510.10343v1#A1.T7 "Table 7 ‣ A.1 Trading Volumes for OTC Derivatives ‣ Appendix A Market Data ‣ Learning the Exact SABR Model") in app. [A.1](https://arxiv.org/html/2510.10343v1#A1.SS1 "A.1 Trading Volumes for OTC Derivatives ‣ Appendix A Market Data ‣ Learning the Exact SABR Model"), interest rate options are the most traded options on the market, we may conclude that the SABR model is one of the most important model used by global financial markets.

Clearly, the SABR model also has a few limitations, as discussed below.

* •

  Single forward model: the SABR model refers to the volatility smile of a single forward. For example, each single forward rate entering in a Cap/Floor requires a different SABR model with its own SABR parameters and calibration to the corresponding volatility smile. The European Swaptions cube requires a different SABR model for each ATM swaption.
* •

  Complex dynamics: the Monte Carlo simulation of the SABR stochastic volatility dynamics is not straightforward; see e.g. [[7](https://arxiv.org/html/2510.10343v1#bib.bibx7)]. The same happens when solving the corresponding PDE. As a consequence, the model calibration to market implied volatility surface is extremely time consuming and prone to numerical approximations. Even more complex is the calculation of Greeks and hedging.
* •

  Approximation accuracy: the accuracy of the Hagan et al. analytical approximation deteriorates for high volatilities, long maturities and out-of-the-money options, yielding negative densities in the distribution’s tails for realistic parameter values. As a consequence, the model allow volatility arbitrages and produce inconsistent prices for financial products depending on the wings of the volatility smile, such as deep out-of-the-money options and constant maturity swaps and options.
* •

  Parameter redundancy: as discussed in [[16](https://arxiv.org/html/2510.10343v1#bib.bibx16)], parameters β\beta and ρ\rho affect the volatility smile in a similar way, leading to some level of redundancy and to the possibility of fixing one of them to some specific value, e.g. β=0\beta=0 in low rates environments, or the Solomonic CIR choice β=0.5\beta=0.5. This is not actually a limitation of the model, since β\beta commands the smile wings and can be used to calibrate smile-dependent instruments such as Constant Maturity Swaps and options, as described by [[32](https://arxiv.org/html/2510.10343v1#bib.bibx32)]. A more sophisticated approach is explored in [[37](https://arxiv.org/html/2510.10343v1#bib.bibx37)], which take into account at the same time both the traditional smile calibration and the hedging performance.

The limitations of the SABR model discussed above have given rise to a whole strand of literature; see e.g. the introduction in [[19](https://arxiv.org/html/2510.10343v1#bib.bibx19)] and [[28](https://arxiv.org/html/2510.10343v1#bib.bibx28)] for excellent reviews.
One possible approach to overcome the shortcoming of Hagan et al. analytical approximation while preserving fast calibration performances consists in using machine learning algorithms based directly on the SABR stochastic dynamics, as discussed in the next section.

### 1.3 Machine Learning for SABR

To the best of our knowledge, the first published application of machine learning techniques to the SABR model dates back to [[31](https://arxiv.org/html/2510.10343v1#bib.bibx31)]. In this seminal paper, a lognormal (β=1\beta=1) SABR model is used to generate a dataset of exact implied volatility surfaces up to short maturities (2Y) and 10 strikes, on a grid of SABR parameters α,ρ,ν\alpha,\rho,\nu, both randomly and regularly sampled, using either moment-matching analytical integration or numerical PDE solution with finite-difference method (FDM). Then, a single-layer ANN is trained on the dataset and carefully tested, showing good precision and much better performance.
In [[25](https://arxiv.org/html/2510.10343v1#bib.bibx25)] is taken an approach similar to [[31](https://arxiv.org/html/2510.10343v1#bib.bibx31)], generating a large dataset of volatility surfaces via GPU-assisted MC simulation instead of FDM444Even using GPUs, their dataset generation took 1 month.. They find that DNNs trained on this dataset achieve a very high calibration accuracy and argue that large training sets allow DNNs to filter out random errors caused by MC, while DNNs fail to rectify systematic biases caused by FDM.
Also [[29](https://arxiv.org/html/2510.10343v1#bib.bibx29)] take a similar approach, improving the ANN training by using Hagan et al. approximate volatilities as control variates.
[[13](https://arxiv.org/html/2510.10343v1#bib.bibx13)] extends the control variate approach by using more sophisticated SABR versions from [[1](https://arxiv.org/html/2510.10343v1#bib.bibx1)] for long maturities and from [[2](https://arxiv.org/html/2510.10343v1#bib.bibx2)] for negative forwards.
[[24](https://arxiv.org/html/2510.10343v1#bib.bibx24)] introduces a Derivative-Constrained Neural Network (DCNN) that incorporates price sensitivities in the objective function and allows to generate smooth volatility surfaces respecting no-arbitrage conditions. The DCNN is trained on sparse volatility surfaces generated by the SABR model using Hagan et al. approximation with varying parameters.
Finally, [[35](https://arxiv.org/html/2510.10343v1#bib.bibx35)] solve the backward Kolmogorov equation for the cumulative probability function and train a DNN to learn the corresponding transition probability density function (TPDF). They test different models, including SABR, and benchmark the ANN pricing accuracy against MC simulations using 100 SABR parameter sets for short maturities (0.25,0.5,0.75, 1.0 years, see their tab. 7).

Different but related approaches are taken by a number of authors. In particular, we cite [[10](https://arxiv.org/html/2510.10343v1#bib.bibx10)], who calibrate SABR-like Local Stochastic Volatility models using ANNs to identify the leverage function and GANs (Generative Adversarial Networks) to identify the loss function. MC simulation with Euler discretization and Black-Scholes delta hedge variance reduction is used to generate option prices on a fixed grid of 4 short maturities (up to 1Y) and 20 evenly spaced strikes.
We also cite [[30](https://arxiv.org/html/2510.10343v1#bib.bibx30)], who uses a looking up and interpolation algorithm on a dense dataset of option values computed by Monte Carlo (MC) simulation with Euler discretization on a fixed grid of SABR parameter values (with constant β\beta).

Many other papers do not specifically discuss the SABR model, but take more general approaches that could be applied to SABR, see e.g. the original proposal in [[4](https://arxiv.org/html/2510.10343v1#bib.bibx4)], further elaborated in [[23](https://arxiv.org/html/2510.10343v1#bib.bibx23)].

### 1.4 Our Contribution

The literature cited in the previous section [1.3](https://arxiv.org/html/2510.10343v1#S1.SS3 "1.3 Machine Learning for SABR ‣ 1 Introduction ‣ Learning the Exact SABR Model"), presents a number of limitations, which we list below.
i) The original Hagan et al. approximation [[16](https://arxiv.org/html/2510.10343v1#bib.bibx16)] is used instead of the more advanced version by [[17](https://arxiv.org/html/2510.10343v1#bib.bibx17)], which allows a better performance.
ii) The full shifted-SABR dynamics is reduced to the lognormal case by fixing β=1\beta=1 to simplify the numerical solutions.
iii) The volatility surface is limited to short maturities and/or fixed strike ranges, without addressing the regions where the Hagan et al. approximation is less accurate.
iv) Do not systematically consider real market data and/or the most diffused interest rate instruments traded on the market.
v) The datasets used for DNN training and/or the DNN structure and/or the training procedure are not fully specified in all the necessary details, thus preventing a complete understanding and reproducibility of the results.

Although the limitations listed above are scattered across different papers, to the best of our knowledge, no single work where all of them are addressed together for the specific SABR model in a systematic and self-consistent way.
In this paper, we aim to cover these gaps by combining all the key elements and establish a comprehensive and functional SABR framework that practitioners can adopt in their daily trading and risk management activity on interest rate options.
Specifically, we contribute to this research field with the following elements.

1. 1.

   We consider real market data on different business dates for the most traded interest rate derivatives, i.e. EURIBOR Caps and Floors555As discussed in sec. [4](https://arxiv.org/html/2510.10343v1#S4 "4 Conclusions and Directions of Future Work ‣ Learning the Exact SABR Model"), the same approach described in this paper can be applied to Caps/Floors on overnight rates and to Swaptions. We note that Swaptions depend on a single forward swap rate, while Caps/Floors are more complex since each option depends on multiple forward rates, one for each Caplet/Floorlet., taking into account the entire volatility surface quoted on the market up to very long maturities (30Y) and extreme strikes (14 points from -1.5% to 10%, including the ATM)666The market strike grid changed in the past to accommodate negative strikes, but remained stable following the return to positive interest rates in 2022., and different EURIBOR tenors (i.e. 3M and 6M).
2. 2.

   We consider the full shifted-SABR stochastic dynamics (without any usage of the Hagan et al. approximation), taking into account possible negative forward rates. In particular, the β\beta parameter is not fixed (as done e.g. in [[31](https://arxiv.org/html/2510.10343v1#bib.bibx31)]), but is calibrated together with the other model parameters, preserving the full flexibility of the original SABR formulation.
   Caplet/Floorlet model prices are generated using high-precision unbiased Monte Carlo simulation of the scaled shifted-SABR dynamics X​(t):=F¯​(t)/F¯0X(t):=\bar{F}(t)/\bar{F}\_{0}, thus reducing the number of parameters without loss of generality.
3. 3.

   Since DNN performances depend crucially on data, we deserve particular importance to the initial offline generation of a very large dataset of interest rate volatility surfaces (more than 200 million points) for EUR Caplets/Floorlets consistent with market quotations.
   To this scope, we adapt to the SABR model the random grid approach proposed by [[3](https://arxiv.org/html/2510.10343v1#bib.bibx3)], introducing two differences: first, we consider a different SABR model for each maturity, consistently with the SABR assumptions in the previous section; second, we select a strike grid independent of maturity, in line with EUR market conventions where Caps and Floors are quoted on a fixed strike grid across all maturities.
4. 4.

   We develop and optimize a DNN architecture specific for Caps and Floors and we train it on the dataset described above, reaching a very good level of precision.
   We check that our DNNs, with a single training, are able to calibrate different market volatility surfaces quoted on different business dates with the same very good precision and performance. As a consequence, they are robust with respect to evolving markets, and do not need retraining, at least in the absence of market regime shifts leading to configurations significantly different from those included in the training dataset.
5. 5.

   Using our DNNs, we challenge the latest version of Hagan et al. analytical approximation developed in [[17](https://arxiv.org/html/2510.10343v1#bib.bibx17)] for the Shifted-SABR model, by computing the distance between the implied volatilities obtained via Monte Carlo simulation using the two corresponding calibrated parameters. This approach allows us to precisely measure how much, in real market situations, the Hagan et al. approximation accuracy deteriorates in specific regions of the volatility surface, particularly for medium-long maturities and out-of-the-money strikes.

The rest of the paper is organized as follows.
Section [2](https://arxiv.org/html/2510.10343v1#S2 "2 Theoretical Framework ‣ Learning the Exact SABR Model") presents the theoretical framework, introducing the financial instruments involved, the SABR model, its scaled Monte Carlo simulation, and the DNN-based SABR calibration approach proposed in this research. Additional details are reported in App. [A](https://arxiv.org/html/2510.10343v1#A1 "Appendix A Market Data ‣ Learning the Exact SABR Model") and [B](https://arxiv.org/html/2510.10343v1#A2 "Appendix B SABR Details ‣ Learning the Exact SABR Model").
Section [3](https://arxiv.org/html/2510.10343v1#S3 "3 Numerical Results ‣ Learning the Exact SABR Model") describes in detail the numerical implementation and results of our methodology, including the generation of the training, validation, and test datasets (sec. [3.1](https://arxiv.org/html/2510.10343v1#S3.SS1 "3.1 Datasets ‣ 3 Numerical Results ‣ Learning the Exact SABR Model")), the DNN construction, optimization and training (sec. [3.2](https://arxiv.org/html/2510.10343v1#S3.SS2 "3.2 DNNs Setup and Training ‣ 3 Numerical Results ‣ Learning the Exact SABR Model")), and the calibration results, comparing the DNN performance with that of the Hagan et al. approximation (sec. [3.3](https://arxiv.org/html/2510.10343v1#S3.SS3 "3.3 Volatility Smile Calibration ‣ 3 Numerical Results ‣ Learning the Exact SABR Model")). Additional details are reported in app. [C](https://arxiv.org/html/2510.10343v1#A3 "Appendix C Dataset Details ‣ Learning the Exact SABR Model"), [D](https://arxiv.org/html/2510.10343v1#A4 "Appendix D DNN Details ‣ Learning the Exact SABR Model"), and [E](https://arxiv.org/html/2510.10343v1#A5 "Appendix E Calibration Details ‣ Learning the Exact SABR Model").
Section [4](https://arxiv.org/html/2510.10343v1#S4 "4 Conclusions and Directions of Future Work ‣ Learning the Exact SABR Model") concludes the paper, summarizing the main findings and outlining potential directions for future research.

## 2 Theoretical Framework

### 2.1 Financial Instruments

In this paper we focus on interest rate Cap/Floor European options. In particular, we select Caps/Floors on EURIBOR typical of the EUR market. Nevertheless, our results do not depend on the specific underlying rate or payoff, and could be easily extended to other instruments, e.g. EURIBOR Swaptions and Caps/Floors/Swaptions on compounded overnight rates typical of other markets (e.g. SOFR for USD, SONIA for GBP, etc.).

A Cap/Floor is a portfolio of Caplets/Floorlets, i.e. call/put options with payoff at cash flow date TiT\_{i} given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | cf​(Ti;Ti−1,Ti,K,ω)=Max​{ω​[L​(Ti−1,Ti)−K]}​τ​(Ti−1,Ti),\textit{cf}(T\_{i};T\_{i-1},T\_{i},K,\omega)=\textit{Max}\left\{\omega\left[L(T\_{i-1},T\_{i})-K\right]\right\}\tau(T\_{i-1},T\_{i}), |  | (1) |

where L​(Ti−1,Ti)L(T\_{i-1},T\_{i}) is a realized IBOR rate fixed at Ti−1T\_{i-1} and referred to the time interval [Ti−1,Ti][T\_{i-1},T\_{i}], a.k.a. the rate tenor (e.g. 6 months), τ​(Ti−1,Ti)\tau(T\_{i-1},T\_{i}) is the year fraction consistent with the rate tenor, KK is the strike, and ω=±1\omega=\pm 1 for Caplets/Floorlets, respectively.
The undiscounted price at time t<Ti−1t<T\_{i-1} (before the IBOR fixing date) of Caplets/Floorlets and the price of Caps/Floors is given by the expectations

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | cf​(t;Ti−1,Ti,K,ω)\displaystyle\textit{cf}(t;T\_{i-1},T\_{i},K,\omega) | =𝔼tQdTi​{Max​{ω​[L​(Ti−1,Ti)−K]}}​τ​(Ti−1,Ti),\displaystyle=\mathbb{E}\_{t}^{Q\_{d}^{T\_{i}}}\left\{\textit{Max}\left\{\omega\left[L(T\_{i-1},T\_{i})-K\right]\right\}\right\}\tau(T\_{i-1},T\_{i}), |  | (2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | CF​(t;𝐓𝐧,K,ω)\displaystyle\textit{CF}(t;\mathbf{T\_{n}},K,\omega) | =∑i=i0​(t)nPd​(t;Ti)​cf​(t;Ti−1,Ti,K,ω),\displaystyle=\sum\_{i=i\_{0}(t)}^{n}P\_{d}(t;T\_{i})\textit{cf}(t;T\_{i-1},T\_{i},K,\omega), |  | (3) |

where 𝐓𝐧={T0,⋯​Tn}\mathbf{T\_{n}}=\left\{T\_{0},\cdots T\_{n}\right\} is the Cap/Floor schedule777The Cap/Floor schedule is consistent with the rate tenor, e.g. semi-annual on IBOR6M, quarterly on IBOR3M, etc., otherwise the pricing formulas would include a convexity adjustment, which is not common on the market and beyond the scope of this paper. for maturity TnT\_{n}, i0​(t)i\_{0}(t) indexes the current time interval such that t∈[Ti0​(t)−1;Ti0​(t)]t\in\left[T\_{i\_{0}(t)-1};T\_{i\_{0}(t)}\right], the expectation is taken under the forward measure QdTiQ\_{d}^{T\_{i}} associated with the discounting numeraire Pd​(t;Ti)P\_{d}(t;T\_{i}), given the information available at time tt. Notice that we have shifted the discount factor Pd​(t;Ti)P\_{d}(t;T\_{i}) from Caplets/Floorlets to Caps/Floors for later convenience, in order to avoid discounting rates in the DNN.
Real Caps/Floors quoted on the market are further characterized by a number of details that we report in app. [A.2](https://arxiv.org/html/2510.10343v1#A1.SS2 "A.2 Caps/Floors Market Quotations ‣ Appendix A Market Data ‣ Learning the Exact SABR Model").

The corresponding IBOR forward rate observed at time t<Ti−1t<T\_{i-1} is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Fi​(t):=F​(t;Ti−1,Ti):=𝔼tQdTi​[L​(Ti−1,Ti)].F\_{i}(t):=F(t;T\_{i-1},T\_{i}):=\mathbb{E}\_{t}^{Q\_{d}^{T\_{i}}}\left[L(T\_{i-1},T\_{i})\right]. |  | (4) |

Forward rate models assume that the IBOR forward rate in eq. ([4](https://arxiv.org/html/2510.10343v1#S2.E4 "In 2.1 Financial Instruments ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model")) is the fundamental quantity whose stochastic dynamics must be modeled to compute the prices in eqs. ([2](https://arxiv.org/html/2510.10343v1#S2.E2 "In 2.1 Financial Instruments ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model")) and ([3](https://arxiv.org/html/2510.10343v1#S2.E3 "In 2.1 Financial Instruments ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model")). This is obviously not the only possible choice; see e.g. [[6](https://arxiv.org/html/2510.10343v1#bib.bibx6)] for details on interest rate modeling approaches.

For the purpose of DNN training discussed in the following sec. [2.4](https://arxiv.org/html/2510.10343v1#S2.SS4 "2.4 Learning SABR with DNNs ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model"), the contract parameters for Caplets/Floorlets are given by θCF={T,K}\theta^{\textit{CF}}=\left\{T,K\right\}, where TT is the contract fixing date and KK is the strike.

### 2.2 Scaled Shifted-SABR Model

The SABR888The name SABR given in the original paper by Hagan et al. [[16](https://arxiv.org/html/2510.10343v1#bib.bibx16)] stands for “Stochastic Alpha Beta Rho”, where the stochastic forward and volatility processes were denoted by F^\hat{F} and α^\hat{\alpha}, respectively, and the parameter associated with the initial volatility value was denoted by α=α^​(0)\alpha=\hat{\alpha}(0). In this paper we adopt a lighter notation, denoting the two stochastic processes simply by F​(t)F(t) and σ​(t)\sigma(t), and keeping the initial volatility parameter as α=σ​(0)\alpha=\sigma(0). stochastic dynamics of the forward rate Fi​(t)F\_{i}(t) in eq. ([4](https://arxiv.org/html/2510.10343v1#S2.E4 "In 2.1 Financial Instruments ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model")) and of its volatility, denoted by σi​(t)\sigma\_{i}(t), is given, dropping the index ii, in [[16](https://arxiv.org/html/2510.10343v1#bib.bibx16)] as

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​F¯​(t)=σ​(t)​F¯β​(t)​d​W​(t),F¯​(0):=F¯0=F0+λ,\displaystyle d\bar{F}(t)=\sigma(t)\bar{F}^{\beta}(t)dW(t),\hskip 14.22636pt\bar{F}(0):=\bar{F}\_{0}=F\_{0}+\lambda, |  | (5) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​σ​(t)=ν​σ​(t)​d​Z​(t),σ​(0)=α,\displaystyle d\sigma(t)=\nu\sigma(t)dZ(t),\hskip 42.67912pt\sigma(0)=\alpha, |  | (6) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​W​(t)​d​Z​(t)=ρ​d​t,\displaystyle dW(t)dZ(t)=\rho dt, |  | (7) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | F¯​(t)=F​(t)+λ,\displaystyle\bar{F}(t)=F(t)+\lambda, |  | (8) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | F0∈ℝ+,α∈ℝ+,β∈[0;1],ρ∈[−1;1],ν∈ℝ+,λ∈ℝ+,\displaystyle F\_{0}\in\mathbb{R}^{+},\alpha\in\mathbb{R}^{+},\beta\in[0;1],\rho\in[-1;1],\nu\in\mathbb{R}^{+},\lambda\in\mathbb{R}^{+}, |  | (9) |

where F¯​(t)\bar{F}(t) is the shifted forward rate, and the processes {W​(t)}t\{W(t)\}\_{t} and {Z​(t)}t\{Z(t)\}\_{t} are two QdTQ\_{d}^{T} Brownian motions associated to the discounting zero coupon bond Pd​(t;T)P\_{d}(t;T) as numeraire.
The SABR model, for each forward rate F​(t)F(t), is characterized by 6 model parameters
θSABR={F0,α,β,ρ,ν,λ}\theta^{\textit{SABR}}=\left\{F\_{0},\alpha,\beta,\rho,\nu,\lambda\right\},
i.e., respectively, the initial forward rate level, the initial volatility level, the CEV elasticity, the correlation between the forward rate and its volatility, the volatility of volatility, and the rate shift, which bounds the forward rate to −λ-\lambda, ensuring that F¯0∈ℝ+\bar{F}\_{0}\in\mathbb{R}^{+}.
The Hagan et al. analytical approximation of the SABR implied volatility for European options is reported in app. [B.1](https://arxiv.org/html/2510.10343v1#A2.SS1 "B.1 Hagan et al. Approximation ‣ Appendix B SABR Details ‣ Learning the Exact SABR Model").

As discussed in the following sec. [2.4](https://arxiv.org/html/2510.10343v1#S2.SS4 "2.4 Learning SABR with DNNs ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model"), the SABR model and Caplet/Floorlet contract parameters
{θSABR,θCF}\left\{\theta^{\textit{SABR}},\theta^{\textit{CF}}\right\} are used as DNN input variables.
In order to enhance the network’s ability to learn the relationships between the output and the input values, we reduce the number of SABR model parameters.
First, according to common market practice, we set the shift parameter λ\lambda to a fixed value, large enough to handle negative forward rates.
Secondly, we rescale the shifted-SABR process to X​(t):=F¯​(t)F¯0X(t):=\frac{\bar{F}(t)}{\bar{F}\_{0}} and σ^​(t):=σ​(t)​F¯​(t)β−1\hat{\sigma}(t):=\sigma(t)\bar{F}(t)^{\beta-1}, leading to the scaled shifted-SABR Model

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​X​(t)=σ^​(t)​Xβ​(t)​d​W​(t),X​(0)=1,\displaystyle dX(t)=\hat{\sigma}(t)X^{\beta}(t)dW(t),\hskip 14.22636ptX(0)=1, |  | (10) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | dσ^(t)=νσ^(t)dZ(t),σ^(0)=αF¯0β−1=:α^,\displaystyle d\hat{\sigma}(t)=\nu\hat{\sigma}(t)dZ(t),\hskip 42.67912pt\hat{\sigma}(0)=\alpha\bar{F}\_{0}^{\beta-1}=:\hat{\alpha}, |  | (11) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​W​(t)​d​Z​(t)=ρ​d​t.\displaystyle dW(t)dZ(t)=\rho dt. |  | (12) |

Consistently, we also rescale the Caplet/Floorlet shifted strike to K^=K¯F¯0\hat{K}=\frac{\bar{K}}{\bar{F}\_{0}}.
The proof is provided in app. [B.3](https://arxiv.org/html/2510.10343v1#A2.SS3 "B.3 Derivation of the Scaled Shifted-SABR Model ‣ Appendix B SABR Details ‣ Learning the Exact SABR Model").
Finally, we set999Note that we denote always with θSABR,θCF\theta^{\textit{SABR}},\theta^{\textit{CF}} different combinations of model and contract parameters, e.g. scaled and not-scaled, hoping that the difference will be clear depending on the context.
θSABR={α^,β,ρ,ν}\theta^{\textit{SABR}}=\left\{\hat{\alpha},\beta,\rho,\nu\right\} and θCF={T,K^}\theta^{\textit{CF}}=\left\{T,\hat{K}\right\}.
Note that we do not further reduce the model parameters by fixing β=1\beta=1 as done in some previous papers, e.g. [[31](https://arxiv.org/html/2510.10343v1#bib.bibx31)].

### 2.3 SABR Monte Carlo

A possible approach to circumvent the limitations of [[17](https://arxiv.org/html/2510.10343v1#bib.bibx17)] analytical approximation is to directly simulate the SABR dynamics in eqs. ([5](https://arxiv.org/html/2510.10343v1#S2.E5 "In 2.2 Scaled Shifted-SABR Model ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model"))-([9](https://arxiv.org/html/2510.10343v1#S2.E9 "In 2.2 Scaled Shifted-SABR Model ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model")) using Monte Carlo. This approach is not straightforward, since it requires the joint simulation of the stochastic volatility process ([6](https://arxiv.org/html/2510.10343v1#S2.E6 "In 2.2 Scaled Shifted-SABR Model ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model")), the simulation of the integrated variance (conditional on the volatility process), and the simulation of the underlying CEV process ([5](https://arxiv.org/html/2510.10343v1#S2.E5 "In 2.2 Scaled Shifted-SABR Model ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model")) (conditional on the volatility and integrated variance processes). Furthermore, an absorbing boundary must be included in the MC simulation to deal with the non-null probability of the underlying CEV process to touch zero for β∈(0,1)\beta\in(0,1). All of these elements lead to computationally expensive simulation that reduces the actual usefulness of the Monte Carlo approach.

In this paper we adopt a simple log-Euler discretization scheme of the SABR model dynamics. Although more refined discretization schemes exist in the literature, such as the approaches proposed by [[8](https://arxiv.org/html/2510.10343v1#bib.bibx8)] and [[7](https://arxiv.org/html/2510.10343v1#bib.bibx7)], their additional complexity does not offer significant advantages for our purposes. Moreover, our framework is independent of the specific MC discretization scheme, ensuring that our results remain valid and replicable under different discretization schemes.
Since the two Brownian motions W​(t),Z​(t)W(t),Z(t) in eq. ([5](https://arxiv.org/html/2510.10343v1#S2.E5 "In 2.2 Scaled Shifted-SABR Model ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model"))-([9](https://arxiv.org/html/2510.10343v1#S2.E9 "In 2.2 Scaled Shifted-SABR Model ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model")) are correlated, we introduce the following transformation

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​W​(t)=ρ​d​Z~​(t)+ρ^​d​W~​(t),\displaystyle dW(t)=\rho d\tilde{Z}(t)+\hat{\rho}d\tilde{W}(t), |  | (13) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Z​(t)=d​Z~​(t),\displaystyle dZ(t)=d\tilde{Z}(t), |  | (14) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ^=1−ρ2,\displaystyle\hat{\rho}=\sqrt{1-\rho^{2}}, |  | (15) |

where now W~​(t),Z~​(t)\tilde{W}(t),\tilde{Z}(t) are independent Brownian motions.
Applying the log-transformation to both the forward rate and volatility processes and introducing the Euler exponential discretization, leads to the following shifted-SABR model’s discretization scheme,

|  |  |  |  |
| --- | --- | --- | --- |
|  | F¯​(tj+1)=F¯​(tj)​exp⁡{−12​σ2​(tj)​F¯2​β−2​(tj)​Δ+σ​(tj)​F¯β−1​(tj)​Δ​[ρ​ζZ~+ρ^​ζW~]},\displaystyle\bar{F}(t\_{j+1})=\bar{F}(t\_{j})\exp\left\{-\frac{1}{2}\sigma^{2}(t\_{j})\bar{F}^{2\beta-2}(t\_{j})\Delta+\sigma(t\_{j})\bar{F}^{\beta-1}(t\_{j})\sqrt{\Delta}\left[\rho\zeta\_{\tilde{Z}}+\hat{\rho}\zeta\_{\tilde{W}}\right]\right\}, |  | (16) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | σ​(tj+1)=σ​(tj)​exp⁡{−12​ν2​Δ+ν​Δ​ζZ~},\displaystyle\sigma(t\_{j+1})=\sigma(t\_{j})\exp\left\{-\frac{1}{2}\nu^{2}\Delta+\nu\sqrt{\Delta}\zeta\_{\tilde{Z}}\right\}, |  | (17) |

where j∈[0,n]⊂ℕj\in[0,n]\subset\mathbb{N}, {t0,…,tn}\{t\_{0},\dots,t\_{n}\} is the regular grid of discretization dates with t0=0,tn=Ti−1t\_{0}=0,t\_{n}=T\_{i-1} (the underlying rate fixing date), Δ=tj+1−tj\Delta=t\_{j+1}-t\_{j} is a constant time step, and ζZ~,ζW~∼N​(0,1)\zeta\_{\tilde{Z}},\zeta\_{\tilde{W}}\sim N(0,1) are standard normal random variables.
Finally, scaling the process F¯​(t)\bar{F}(t) to X​(t)=F¯​(t)/F¯0X(t)=\bar{F}(t)/\bar{F}\_{0} as discussed in sec. [2.2](https://arxiv.org/html/2510.10343v1#S2.SS2 "2.2 Scaled Shifted-SABR Model ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model") and app. [B.3](https://arxiv.org/html/2510.10343v1#A2.SS3 "B.3 Derivation of the Scaled Shifted-SABR Model ‣ Appendix B SABR Details ‣ Learning the Exact SABR Model") lead to the following scaled shifted-SABR discretization scheme,

|  |  |  |  |
| --- | --- | --- | --- |
|  | X​(tj+1)=X​(tj)​exp⁡{−12​σ^2​(tj)​X2​β−2​(tj)​Δ+σ^​(tj)​Xβ−1​(tj)​Δ​[ρ​ζZ~+ρ^​ζW~]},\displaystyle X(t\_{j+1})=X(t\_{j})\exp\left\{-\frac{1}{2}\hat{\sigma}^{2}(t\_{j})X^{2\beta-2}(t\_{j})\Delta+\hat{\sigma}(t\_{j})X^{\beta-1}(t\_{j})\sqrt{\Delta}\left[\rho\zeta\_{\tilde{Z}}+\hat{\rho}\zeta\_{\tilde{W}}\right]\right\}, |  | (18) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | σ^​(tj+1)=σ^​(tj)​exp⁡{−12​ν2​Δ+ν​Δ​ζZ~},\displaystyle\hat{\sigma}(t\_{j+1})=\hat{\sigma}(t\_{j})\exp\left\{-\frac{1}{2}\nu^{2}\Delta+\nu\sqrt{\Delta}\zeta\_{\tilde{Z}}\right\}, |  | (19) |

which we used in practice to produce the datasets described in the following sec. [3.1](https://arxiv.org/html/2510.10343v1#S3.SS1 "3.1 Datasets ‣ 3 Numerical Results ‣ Learning the Exact SABR Model").

In order to avoid that the CEV forward rate process reaches zero during the MC simulation, we set an absorbing boundary at 10−1410^{-14} to ensure that, in case the shifted forward rate reaches the boundary, it remains there for the rest of the simulation.

### 2.4 Learning SABR with DNNs

As discussed in sec. [1](https://arxiv.org/html/2510.10343v1#S1 "1 Introduction ‣ Learning the Exact SABR Model"), an increasing number of studies explore machine learning algorithms to address the calibration of stochastic volatility models using a DNN approach, which we formalize below in the context of SABR model applied to Caps/Floors.
Unlike the previous literature, we split and formalize our algorithm into a three-stage approach, to give the appropriate importance to the initial dataset generation stage, matching the general idea that DNN performances depend crucially on data.

1. 1.

   Offline dataset generation.
   We sample a large collection of NσN\_{\sigma} SABR model parameter sets θSABR={F0,α,β,ρ,ν}\theta^{\textit{SABR}}=\{F\_{0},\alpha,\beta,\rho,\nu\} using appropriate parameter ranges that cover different market situations.
   For each set θSABR\theta^{\textit{SABR}}, we sample a set of NT×NKN\_{T}\times N\_{K} contract parameters θCF={T,K}\theta^{\textit{CF}}=\{T,K\} forming a surface with NTN\_{T} dates and NKN\_{K} strikes, consistent with the date and strike ranges observed in market quotations.
   For each point in each surface, we compute the corresponding Caplet/Floorlet price using the scaled shifted-SABR Monte Carlo simulation described in sec. [2.3](https://arxiv.org/html/2510.10343v1#S2.SS3 "2.3 SABR Monte Carlo ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model"), and the shifted-lognormal implied volatility
   σMC​(θSABR,θCF)\sigma^{\textit{MC}}(\theta^{\textit{SABR}},\theta^{\textit{CF}})
   by inverting the shifted-Black formula.
   The results is a large dataset of NσN\_{\sigma} shifted-lognormal implied volatility surfaces of dimension NT×NKN\_{T}\times N\_{K} including, in total, Nt​o​t=Nσ×NT×NKN\_{tot}=N\_{\sigma}\times N\_{T}\times N\_{K} volatility points, consistent with the shifted-SABR stochastic dynamics in eqs. ([5](https://arxiv.org/html/2510.10343v1#S2.E5 "In 2.2 Scaled Shifted-SABR Model ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model"))–([9](https://arxiv.org/html/2510.10343v1#S2.E9 "In 2.2 Scaled Shifted-SABR Model ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model")) and market quotations.
   Note that we do not use the Hagan et al. approximation for dataset construction.
2. 2.

   Offline DNN Setup and Training.
   We set up three Deep Neural Networks (DNNs) dedicated to short, medium, and long maturities.
   The DNNs considered here are feed-forward networks, similar to e.g. [[23](https://arxiv.org/html/2510.10343v1#bib.bibx23)] and [[3](https://arxiv.org/html/2510.10343v1#bib.bibx3)].
   The key characteristic of their topology is that each node in a given layer is connected to all nodes in the subsequent layer, whereas vertical connections between nodes within the same layer or backward from a layer to a previous layer are not allowed. In these DNNs data flows uni-directionally, from the input nodes to the output nodes, without any feedback loops.
   Denoting with θs:={θsSABR,θsCF},s=1,…,Nt​o​t\theta\_{s}:=\{\theta\_{s}^{\textit{SABR}},\theta\_{s}^{\textit{CF}}\},s=1,\dots,N\_{tot} the total set of parameters associated to a single Monte Carlo implied volatility σMC​(θs)\sigma^{\textit{MC}}(\theta\_{s}), the DNNs are trained to learn the implied volatility map
   θs→σMC​(θs)\theta\_{s}\rightarrow\sigma^{\textit{MC}}(\theta\_{s}) by finding the optimal DNNs’ weights w^\hat{w} that solve the optimization problem

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | w^=arg⁡min𝑤​1Nt​o​t​∑s=1Nt​o​t[σDNN​(θs,w)−σMC​(θs)]2.\hat{w}=\underset{w}{\arg\min}\sqrt{\frac{1}{N\_{tot}}\sum\_{s=1}^{N\_{tot}}\left[\sigma^{\textit{DNN}}(\theta\_{s},w)-\sigma^{\textit{MC}}(\theta\_{s})\right]^{2}}. |  | (20) |
3. 3.

   Online calibration to market data.
   Given the trained DNN, we can now, at any time tt, calibrate the shifted-SABR model parameters to the market volatility surface

   |  |  |  |
   | --- | --- | --- |
   |  | σMkt​(t;Ti,Kj),i=1,…,NT,j=1,…,NK(smile by smile)\displaystyle\sigma^{\textit{Mkt}}(t;T\_{i},K\_{j}),\;i=1,\dots,N\_{T},j=1,\dots,N\_{K}\quad\textit{(smile by smile)} |  |

   quoted at time tt, considering the trained DNN as a substitute of the actual pricing function, by solving the NTN\_{T} optimization problems

   |  |  |  |  |
   | --- | --- | --- | --- |
   |  | θ^iSABR,DNN​(t)=arg⁡minθiSABR​1NK​∑j=1NKξj​[σDNN​(θiSABR,Ti,Kj,w^)−σMkt​(t;Ti,Kj)]2,i=1,…,NT,\hat{\theta}\_{i}^{\textit{SABR,DNN}}(t)=\underset{\theta\_{i}^{\textit{SABR}}}{\arg\min}\sqrt{\frac{1}{N\_{K}}\sum\_{j=1}^{N\_{K}}\xi\_{j}\left[\sigma^{\textit{DNN}}(\theta\_{i}^{\textit{SABR}},T\_{i},K\_{j},\hat{w})-\sigma^{\textit{Mkt}}(t;T\_{i},K\_{j})\right]^{2}},i=1,\dots,N\_{T}, |  | (21) |

   where ξj\xi\_{j} denotes the Black vega sensitivity associated with the jj-th strike in the smile section, normalized with respect to the total vega sensitivity of the smile section.

We show in fig. [1](https://arxiv.org/html/2510.10343v1#S2.F1 "Figure 1 ‣ 2.4 Learning SABR with DNNs ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model") the flowchart corresponding to the three-stage approach described above.

Step 1: Offline dataset generation

•

Sample a collection of NσN\_{\sigma} SABR model parameter sets θSABR\theta^{\text{SABR}}.
•

For each set θSABR\theta^{\text{SABR}}, sample a surface of NT×NKN\_{T}\times N\_{K} contract parameters θCF\theta^{\text{CF}}.
•

For each point in each surface, compute the corresponding shifted-lognormal implied volatility using Monte Carlo simulation.
Output: dataset of shifted-lognormal implied volatility surfaces including approximately a total of Ntot=Nσ×NT×NKN\_{\text{tot}}=N\_{\sigma}\times N\_{T}\times N\_{K} volatility points.

Step 2: Offline DNN Setup and Training

•

Set up three DNNs dedicated to short, medium, and long maturities.
•

Train and optimize the DNNs by solving the optimization problem in eq. ([20](https://arxiv.org/html/2510.10343v1#S2.E20 "In item 2 ‣ 2.4 Learning SABR with DNNs ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model")).
Output: three DNNs which replicate the dataset.

Step 3: Online calibration to market data

•

Calibrate the SABR model parameters to the market volatility surface
quoted at time tt, by solving the NTN\_{T} optimization problems in eq. ([21](https://arxiv.org/html/2510.10343v1#S2.E21 "In item 3 ‣ 2.4 Learning SABR with DNNs ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model")).
Output: a SABR parameter set {θ^iSABR,DNN​(t)}i=1NT\{\hat{\theta}\_{i}^{\text{SABR,DNN}}(t)\}\_{i=1}^{N\_{T}} which replicates the market volatility surface at time tt.


Figure 1: Flow chart of the SABR DNN calibration methodology.

The results of the SABR DNN calibration may be compared with the results of the “classic” SABR calibration, based on the Hagan et al. approximation discussed in app. [B.1](https://arxiv.org/html/2510.10343v1#A2.SS1 "B.1 Hagan et al. Approximation ‣ Appendix B SABR Details ‣ Learning the Exact SABR Model"), obtained by the NTN\_{T} optimization problems

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ^iSABR,Hagan​(t)=arg⁡minθiSABR​1NK​∑j=1NKξj​[σHagan​(t;θiSABR,Ti,Kj)−σMkt​(t;Ti,Kj)]2,i=1,…,NT.\hat{\theta}\_{i}^{\textit{SABR,Hagan}}(t)=\underset{\theta\_{i}^{\textit{SABR}}}{\arg\min}\sqrt{\frac{1}{N\_{K}}\sum\_{j=1}^{N\_{K}}\xi\_{j}\left[\sigma^{\textit{Hagan}}(t;\theta\_{i}^{\textit{SABR}},T\_{i},K\_{j})-\sigma^{\textit{Mkt}}(t;T\_{i},K\_{j})\right]^{2}},i=1,\dots,N\_{T}. |  | (22) |

The massive numerical calculation of shifted-lognormal volatilities implied from Monte Carlo prices of a large dataset including deep in/out of the money options and high uncertainty scenarios requires careful consideration and specific techniques to reduce the Monte Carlo error and avoid numerical problems (see e.g. [[9](https://arxiv.org/html/2510.10343v1#bib.bibx9)] sec. 4, and refs. therein).
In this context, we prefer the bisection algorithm applied to Floorlet prices.
Specifically, we always compute both Caplet and Floorlet MC prices, and we select the option with the smallest MC error; if the option is a Floorlet, we proceed with bisection, else if the option is a Caplet, we compute the price of the corresponding Floorlet via the call-put parity and then use bisection.
In this way, we ensure consistency in the volatility implication process, as the same inversion formula is always applied. Floorlets are preferred because, as shown in app. [C.2](https://arxiv.org/html/2510.10343v1#A3.SS2 "C.2 Monte Carlo Error Analysis ‣ Appendix C Dataset Details ‣ Learning the Exact SABR Model"), in low–uncertainty scenarios, the smallest MC pricing error typically occurs for out–of–the–money options, whereas, in high–uncertainty scenarios, put options tend to have a smaller MC error due to the natural upper bound on their payoff.
This approach ensures that the implied volatility calculation is always based on the most accurate MC price, thus reducing the implied volatility MC error propagated from the MC price.

The generation of a large dataset (we will see in sec. [3.1](https://arxiv.org/html/2510.10343v1#S3.SS1 "3.1 Datasets ‣ 3 Numerical Results ‣ Learning the Exact SABR Model") that Nt​o​tN\_{tot} is huge, more than 200 million volatilities) and the training procedure are time-consuming processes that can take hours or days, depending on the available computational resources and model complexity. However, this process is conducted offline, meaning that it is performed once and for all. Subsequently, the trained DNNs are used to address very fast all necessary calibration tasks, even in real time.

## 3 Numerical Results

In this section we report our numerical results following the three-stage approach illustrated in the previous sec. [2.4](https://arxiv.org/html/2510.10343v1#S2.SS4 "2.4 Learning SABR with DNNs ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model").

### 3.1 Datasets

We built three distinct datasets spanning short, medium and long Caplet/Floorlet maturities up to 30 years, according to the EUR market quotations, as described below.

#### Training Sets:

the SABR model parameters θSABR={F0,α,β,ρ,ν}\theta^{\textit{SABR}}=\{F\_{0},\alpha,\beta,\rho,\nu\} were sampled from a uniform distribution using Latin Hypercube Sampling (LHS) within the predefined ranges reported in tab. [1](https://arxiv.org/html/2510.10343v1#S3.T1 "Table 1 ‣ Training Sets: ‣ 3.1 Datasets ‣ 3 Numerical Results ‣ Learning the Exact SABR Model").

| Training | Fixing | F0F\_{0} | λ\lambda | α\alpha | β\beta | ρ\rho | ν\nu | NσN\_{\sigma} |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| set # | date (y) |
| 1 | [0.25,4)[0.25,4) | [1%,5%][1\%,5\%] | 3% | [0.001,0.2] | [0.1,0.9] | [-0.8,0.6] | [0.05,1.6] | 2202^{20} |
| 2 | [4,10.5)[4,10.5) | [1%,5%][1\%,5\%] | 3% | [0.001,0.2] | [0.1,0.9] | [-0.8,0.6] | [0.05,1.2] | 2182^{18} |
| 3 | [10.5,30][10.5,30] | [1%,5%][1\%,5\%] | 3% | [0.001,0.2] | [0.05,0.9] | [-0.8,0.6] | [0.05,1.2] | 2182^{18} |

Table 1: SABR model parameters’ ranges and number of samples for each data subset. For each sample is generated an entire volatility surface, as explained below. The total dataset includes Nσtot=220+218+218N^{\textit{tot}}\_{\sigma}=2^{20}+2^{18}+2^{18} volatility surfaces.

The parameters’ ranges were selected so as to generate a training set spanning a sufficiently wide range of values, enabling an effective and robust calibration of the SABR model in different market conditions, while at the same time avoiding excessively broad ranges that could lead to the inclusion of unrealistic parameter values.
The initial forward rate F0F\_{0} was centered around market-observed values, i.e. EURIBOR6M forward rates, and the range was extended to include all levels the rate may reasonably assume under the prevailing economic conditions. The shift parameter was fixed to λ=3%\lambda=3\%, consistently with market quotations for EUR Caps/Floors which include negative strikes (see app. [A.2](https://arxiv.org/html/2510.10343v1#A1.SS2 "A.2 Caps/Floors Market Quotations ‣ Appendix A Market Data ‣ Learning the Exact SABR Model")).
The parameters F0F\_{0} and α\alpha are then rescaled as discussed in sec. [2.2](https://arxiv.org/html/2510.10343v1#S2.SS2 "2.2 Scaled Shifted-SABR Model ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model").
The ranges for the remaining SABR model parameters reported in tab. [1](https://arxiv.org/html/2510.10343v1#S3.T1 "Table 1 ‣ Training Sets: ‣ 3.1 Datasets ‣ 3 Numerical Results ‣ Learning the Exact SABR Model") were determined using the following empirical iterative procedure.

1. 1.

   Start with a suitable small but realistic guess of the parameters’ ranges.
2. 2.

   Generate the corresponding dataset as described below in this section.
3. 3.

   Train, validate and test the DNNs as described in sec. [3.2](https://arxiv.org/html/2510.10343v1#S3.SS2 "3.2 DNNs Setup and Training ‣ 3 Numerical Results ‣ Learning the Exact SABR Model").
4. 4.

   Using the DNNs, calibrate the SABR parameters to market data as described in sec. [3.3](https://arxiv.org/html/2510.10343v1#S3.SS3 "3.3 Volatility Smile Calibration ‣ 3 Numerical Results ‣ Learning the Exact SABR Model").
5. 5.

   Check if the resulting SABR parameters lie close to the boundaries of their respective ranges.
6. 6.

   Adjust the parameters’ ranges and repeat the previous steps until the final result is stable.

We observe in tab. [1](https://arxiv.org/html/2510.10343v1#S3.T1 "Table 1 ‣ Training Sets: ‣ 3.1 Datasets ‣ 3 Numerical Results ‣ Learning the Exact SABR Model") that the number of sampled SABR parameter sets NσN\_{\sigma} is higher for dataset #1, which corresponds to shorter maturities. This is because the Monte Carlo shifted-Black implied volatilities for shorter maturities exhibit a greater MC error. Consequently, more data are required in dataset #1 for DNN training to overcome this noise. The SABR parameters’ ranges determined according to the procedure above are consistent with the parameters’ term structures reported in app. [E](https://arxiv.org/html/2510.10343v1#A5 "Appendix E Calibration Details ‣ Learning the Exact SABR Model"), a confirmation that the empirical iterative procedure outlined above was effective.

Given the SABR parameter sets θlSABR,l=1,…,Nσ\theta^{\textit{SABR}}\_{l},l=1,\dots,N\_{\sigma}, we must associate the contract parameters
θCF={T,K}\theta^{\textit{CF}}=\{T,K\}. We built, for each set θlSABR\theta^{\textit{SABR}}\_{l}, an entire shifted-Black volatility surface including NTN\_{T} dates ×NK\times N\_{K} strikes.
The dates {Tl,i}i=1NT\{T\_{l,i}\}\_{i=1}^{N\_{T}} were sampled uniformly and randomly, with each Tl,iT\_{l,i} selected from a corresponding ii-th sub-interval of the total time span of each dataset, shown in tab. [2](https://arxiv.org/html/2510.10343v1#S3.T2 "Table 2 ‣ Training Sets: ‣ 3.1 Datasets ‣ 3 Numerical Results ‣ Learning the Exact SABR Model").

| Training set # | Fixing date intervals [Tm​i​n,Tm​a​x][T\_{min},T\_{max}] | NTN\_{T} |
| --- | --- | --- |
| 1 | [2m,5m) ∪\cup [5m,8m) ∪\cup [8m,1y) ∪\cup [1y, 1y4m) ∪\cup | 10 |
| [1y4m,1y6m) ∪\cup [1y6m,1y11m) ∪\cup [1y11m,2y5m) ∪\cup |
| [2y5m,2y11m)∪\cup [2y11m,3y5m)∪\cup [3y5m,3y11m] |
| 2 | [3y10m,4y6m) ∪\cup [4y6m,5y2m) ∪\cup [5y2m,5y10m) ∪\cup [5y10m,6y6m) ∪\cup | 10 |
| [6y6m,7y2m) ∪\cup[7y2m,7y10m) ∪\cup [7y10m,8y6m)∪\cup [8y6m,9y2m) ∪\cup |
| [9y2m,9y10m)∪\cup [9y10m,10y6m] |
| 3 | [10y5m,11y5m) ∪\cup [11y5m,12y5m) ∪\cup [12y5m, 13y5m) ∪\cup [13y5m,14y5m) ∪\cup | 20 |
| [14y5m,15y5m) ∪\cup [15y5m,16y5m) ∪\cup [16y5m,17y5m) ∪\cup [17y5m,18y5m) ∪\cup |
| [18y5m,19y5m) ∪\cup [19y5m,20y5m) ∪\cup [20y5m,21y5m) ∪\cup [21y5m,22y5m) ∪\cup |
| [22y5m,23y5m) ∪\cup [23y5m,24y5m) ∪\cup [24y5m,25y5m) ∪\cup [25y5m,26y5m)∪\cup |
| [26y5m,27y5m) ∪\cup [27y5m,28y5m) ∪\cup [28y5m,29y5m) ∪\cup [29y5m,30y5m] |

Table 2: Time sub-intervals for each dataset time span. Dates are expressed in months (m) and years (y). As stated immediately below eq. ([17](https://arxiv.org/html/2510.10343v1#S2.E17 "In 2.3 SABR Monte Carlo ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model")) in sec. [2.3](https://arxiv.org/html/2510.10343v1#S2.SS3 "2.3 SABR Monte Carlo ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model"), these time intervals refer to fixing dates of the forward rate, the final point where the SABR Monte Carlo simulation stops. The maximum fixing date (30y5m) is larger than the maximum fixing date quoted on the market (29y6m, see tab. [6](https://arxiv.org/html/2510.10343v1#A1.F6 "Figure 6 ‣ A.2 Caps/Floors Market Quotations ‣ Appendix A Market Data ‣ Learning the Exact SABR Model")), to facilitate the DNN training.

We note that, although the sub-intervals were consistent across all parameter sets within a dataset, the actual sampled dates are different, since the selection is performed independently for each set. This procedure ensures that the sample dates are well spread throughout the entire date range.
We also note that NTN\_{T} is increased to 20 for dataset #3, to adequately cover its larger time span with respect to datasets #1 and #2, and ensure a consistent training precision of the corresponding DNN, as described in the next section.

The strikes were sampled in a similar way: for each SABR parameter set θlSABR,l=1,…,Nσ\theta^{\textit{SABR}}\_{l},l=1,\dots,N\_{\sigma} and for each date {Tl,i}i=1NT\{T\_{l,i}\}\_{i=1}^{N\_{T}}, we sampled NKN\_{K} scaled moneyness {K^l,i,j}j=1NK\{\hat{K}\_{l,i,j}\}\_{j=1}^{N\_{K}}, where K^=K¯/F¯0=(K+λ)/(F0+λ)\hat{K}=\bar{K}/\bar{F}\_{0}=(K+\lambda)/(F\_{0}+\lambda) as discussed in sec. [2.2](https://arxiv.org/html/2510.10343v1#S2.SS2 "2.2 Scaled Shifted-SABR Model ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model"), uniformly and randomly from three fixed sub-intervals, shared across all datasets, as defined in tab. [3](https://arxiv.org/html/2510.10343v1#S3.T3 "Table 3 ‣ Training Sets: ‣ 3.1 Datasets ‣ 3 Numerical Results ‣ Learning the Exact SABR Model"). The ranges were selected according to both market quotations, which feature a fixed strike grid, and the ranges selected for the initial forward rate F0F\_{0}. Also in this case, the actual strike values differ between pairs, since sampling is performed independently for each pair.

| Training set # | K^\hat{K} interval | # NKN\_{K} |
| --- | --- | --- |
| Any | [0.15,0.70)[0.15,0.70) | 4 |
| [0.70,1.50)[0.70,1.50) | 5 |
| [1.50,3.50][1.50,3.50] | 4 |

Table 3: Scaled moneyness sub-intervals common to all datasets in tab. [2](https://arxiv.org/html/2510.10343v1#S3.T2 "Table 2 ‣ Training Sets: ‣ 3.1 Datasets ‣ 3 Numerical Results ‣ Learning the Exact SABR Model"), and the corresponding number of sample values. The total number of values sampled for each maturity is thus NK=13N\_{K}=13.

For each point the prices of the corresponding Caplet/Floorlet options were estimated using the Monte Carlo simulation described in sec. [2.3](https://arxiv.org/html/2510.10343v1#S2.SS3 "2.3 SABR Monte Carlo ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model"), with MC parameters as in the following tab. [4](https://arxiv.org/html/2510.10343v1#S3.T4 "Table 4 ‣ Training Sets: ‣ 3.1 Datasets ‣ 3 Numerical Results ‣ Learning the Exact SABR Model"), where we also summarize the characteristics of the training sets.
Finally, for each price, its corresponding shifted-Black implied volatility was computed as described in sec. [2.4](https://arxiv.org/html/2510.10343v1#S2.SS4 "2.4 Learning SABR with DNNs ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model").

| Training | NσN\_{\sigma} | Fixing date | NTN\_{T} | K^\hat{K} | NKN\_{K} | NM​CN\_{MC} | ΔM​C\Delta\_{MC} |
| --- | --- | --- | --- | --- | --- | --- | --- |
| set # | interval (y) | interval | (days) |
| 1 | 2202^{20} | [0.25,4) | 10 | [0.15,3.5] | 13 | 2182^{18} | 0.5 |
| 2 | 2182^{18} | [4,10.5) | 10 | [0.15,3.5] | 13 | 2182^{18} | 1 |
| 3 | 2182^{18} | [10.5,30] | 20 | [0.15,3.5] | 13 | 2182^{18} | 3 |

Table 4: Summary of parameters used to generate the training sets.

We note that while the number of MC paths is the same for each dataset, the MC time step increases for medium and longer maturities (associated to subsets #2 and #3), to balance efficiency with precision of the dataset generation process.

In conclusion, the total training set consists of Nσtot=220+218+218=1,572,864N^{\textit{tot}}\_{\sigma}=2^{20}+2^{18}+2^{18}=1,572,864 random grid surfaces, totaling 220×10×13+218×10×13+218×20×13=238,551,0402^{20}\times 10\times 13+2^{18}\times 10\times 13+2^{18}\times 20\times 13=238,551,040 points.
Actually, the number of volatility points available in the dataset is slightly smaller, since we dropped any combination of market and model parameters giving prices with a time value below the threshold of 10−1310^{-13}. This accounts roughly for 1%1\% of the total training set (≈2.4\approx 2.4 million points excluded).
Furthermore, 20% of the training set is used as validation set, see below.

#### Validation Sets:

regarding the validation sets, they were built by randomly sampling 20% data points from the corresponding training sets.
Therefore, the total number of data points in the validation set is approximately 47,710,208.

#### Test Sets:

in addition to the three training sets described above, it is essential to independently generate their corresponding test sets, which are used to evaluate a posteriori the performance of the DNN using out of sample data.
Accordingly, we generated three test sets in a way similar to the training sets, using the θSABR\theta^{\textit{SABR}} parameters’ ranges of tab. [1](https://arxiv.org/html/2510.10343v1#S3.T1 "Table 1 ‣ Training Sets: ‣ 3.1 Datasets ‣ 3 Numerical Results ‣ Learning the Exact SABR Model"), setting Nσ=210N\_{\sigma}=2^{10}. Unlike the training set, we sampled NTN\_{T} dates uniformly throughout the entire date range, without using the sub-intervals shown in tab. [2](https://arxiv.org/html/2510.10343v1#S3.T2 "Table 2 ‣ Training Sets: ‣ 3.1 Datasets ‣ 3 Numerical Results ‣ Learning the Exact SABR Model"), and a single strike per date.
In this way we obtain a random selection of points within a volatility surface, less regular than the training set and well-suited for testing the DNNs completely out of sample.
The total number of data points across the three test sets is 210×10×1+210×10×1+210×20×1=40,9602^{10}\times 10\times 1+2^{10}\times 10\times 1+2^{10}\times 20\times 1=40,960. Also in this case the actual number of volatility points available for testing is slightly smaller, since we dropped configurations giving prices with a time value below the threshold of 10−1310^{-13}.

### 3.2 DNNs Setup and Training

We set up three distinct DNNs to cover the entire maturity domain of the Caplets/Floorlets quoted on the market, corresponding to the short (#1), medium (#2) and long (#3) maturity datasets shown in tab. [1](https://arxiv.org/html/2510.10343v1#S3.T1 "Table 1 ‣ Training Sets: ‣ 3.1 Datasets ‣ 3 Numerical Results ‣ Learning the Exact SABR Model"). Their detailed structure is reported in the following tab. [5](https://arxiv.org/html/2510.10343v1#S3.T5 "Table 5 ‣ 3.2 DNNs Setup and Training ‣ 3 Numerical Results ‣ Learning the Exact SABR Model").

|  |  |  |  |
| --- | --- | --- | --- |
| Parameter | DNN 1 | DNN 2 | DNN 3 |
| Training set | #1 | #2 | #3 |
| Test set | #4 | #5 | #6 |
| Maturity range (y) | [0.25,4)[0.25,4) | [4,10.5)[4,10.5) | [10.5,30][10.5,30] |
| Moneyness range | [0.15,3.5][0.15,3.5] | | |
| Inputs | {α^,β,ρ,ν,T,K^}\{\hat{\alpha},\beta,\rho,\nu,T,\hat{K}\} | | |
| Output | σSLNDNN​(α^,β,ρ,ν,T,K^)=σSLNDNN​(α,β,ρ,ν,T,K)\sigma^{\textit{DNN}}\_{\textit{SLN}}(\hat{\alpha},\beta,\rho,\nu,T,\hat{K})=\sigma^{\textit{DNN}}\_{\textit{SLN}}(\alpha,\beta,\rho,\nu,T,K) | | |
| Input layer nodes | 6 | | |
| Hidden layers | 5 | | |
| Hidden nodes per layer | 64 | | |
| Hidden activation function | ELU | | |
| Output layer nodes | 1 | | |
| Output activation function | Linear | | |
| Loss function | RMSE | | |
| Optimizer | ADAM | | |
| Max number of epochs | 500 | | |
| Early stopping patient (epochs) | 50 | | |
| Mini batches | YES | | |

Table 5: Summary of DNNs characteristics. DNN parameters following the maturity range (moneyness range and below) are common to all the three DNNs.

The input layer has 6 nodes to accommodate the model parameters θSABR={α^,β,ρ,ν}\theta^{\textit{SABR}}=\{\hat{\alpha},\beta,\rho,\nu\} and the contract parameters θCF={T,K^}\theta^{\textit{CF}}=\{T,\hat{K}\} (the DNNs’ input features).
The output layer consists of a single node representing the shifted-Black implied volatility σSLNDNN\sigma^{\textit{DNN}}\_{\textit{SLN}} with a shift parameter λ=3%\lambda=3\% consistent with the input data. The linear activation function is used to get the output, since if the neural network is learning properly, it should naturally produce positive implied volatilities, without the need to explicitly enforce it.
The DNNs’ input data are standardized using the StandardScaler from scikit-learn, which transforms each input feature to have zero mean and unit variance, to allow faster convergence and greater efficiency.
The DNNs’ architecture was optimized empirically, checking that reducing the number of hidden layers or nodes per layer led to a worse performance, while increasing them had little or no effect.

To evaluate the accuracy of the three DNNs to approximate the shifted-SABR model, it is essential to assess their performance on both training, validation, and test sets.
We show in tab. [6](https://arxiv.org/html/2510.10343v1#S3.T6 "Table 6 ‣ 3.2 DNNs Setup and Training ‣ 3 Numerical Results ‣ Learning the Exact SABR Model") and fig. [2](https://arxiv.org/html/2510.10343v1#S3.F2 "Figure 2 ‣ 3.2 DNNs Setup and Training ‣ 3 Numerical Results ‣ Learning the Exact SABR Model") the numerical results of this procedure for our three DNNs together. Specifically, the results reported for the training procedure include their validation using the validation set.
More details on individual DNNs are reported in app. [D](https://arxiv.org/html/2510.10343v1#A4 "Appendix D DNN Details ‣ Learning the Exact SABR Model").

| Training Set | | | Test Set |
| --- | --- | --- | --- |
| |Δ​σ|>1%|\Delta\sigma|>1\% | |Δ​σ|>5%|\Delta\sigma|>5\% | RMSE | RMSE |
| 1% | 0.26% | 0.28% | 0.25% |

Table 6: Numerical results of training and test procedure for the three combined DNNs. Δ​σ=σSLNDNN−σSLNMC\Delta\sigma=\sigma^{\textit{DNN}}\_{\textit{SLN}}-\sigma^{\textit{MC}}\_{\textit{SLN}} denotes the DNN shifted-Black volatility approximation error.



![Refer to caption](Figures/Train_datashader.png)

![Refer to caption](Figures/Test_scatter.png)

Figure 2: Combined scatter plots for the training (left) and test (right) aggregate results of the three DNNs. More results are reported in app. [D](https://arxiv.org/html/2510.10343v1#A4 "Appendix D DNN Details ‣ Learning the Exact SABR Model"). We note in both panels that most of the data lie in the “reasonable” region below ∼75%\sim 75\%. Few higher data, up to 400%, occasionally appear because of the random generation of SABR parameters discussed in the previous sec. [3.1](https://arxiv.org/html/2510.10343v1#S3.SS1 "3.1 Datasets ‣ 3 Numerical Results ‣ Learning the Exact SABR Model"), which may produce “strange” combinations leading to extreme volatilities. We did not discarded such data from the training set to let the DNNs learn also extreme combinations, not encountered in calibrations of real market data.

We observe in tab. [6](https://arxiv.org/html/2510.10343v1#S3.T6 "Table 6 ‣ 3.2 DNNs Setup and Training ‣ 3 Numerical Results ‣ Learning the Exact SABR Model") that both training and test performances in terms of RMSE are quite good with respect to the typical volatility bid-ask spread observed on the EUR Cap/Floor market (≈0.25%\approx 0.25\% for the most liquid options).
The DNN volatility approximation error Δ​σ\Delta\sigma shown in tab. [6](https://arxiv.org/html/2510.10343v1#S3.T6 "Table 6 ‣ 3.2 DNNs Setup and Training ‣ 3 Numerical Results ‣ Learning the Exact SABR Model") was estimated by a post-training sample analysis. We find that the largest discrepancies are associated with short maturities and extreme strikes, where the MC SABR volatilities show the largest MC errors (defined as the ratio between three MC standard deviations and the shifted-Black vega sensitivity, see app. [E](https://arxiv.org/html/2510.10343v1#A5 "Appendix E Calibration Details ‣ Learning the Exact SABR Model")), and that SABR DNN volatilities fall within the MC errors.
To further check the DNN error, we recalculated the MC SABR volatilities with a larger number of MC scenarios, i.e. NM​C=220N\_{MC}=2^{20}, finding lower DNN errors. We conclude that our DNNs consistently learnt the MC SABR volatilities even in the most difficult cases.

The test plot in fig. [2](https://arxiv.org/html/2510.10343v1#S3.F2 "Figure 2 ‣ 3.2 DNNs Setup and Training ‣ 3 Numerical Results ‣ Learning the Exact SABR Model") (right panel) shows that there is no overfitting. The training plot (left panel), however, shows some mismatch between predicted and actual values for the smallest volatilities. This is actually expected, since data in the training and test sets are subject to Monte Carlo error. If the training scatter plots were a perfect line, they would indicate that the DNNs are overfitting the data by fitting even the MC errors. Instead, as observed above, we observe that the DNNs act as filters, extracting true information while discarding noise, which is reflected in the halo observed around the noisier points.
A closer inspection of these points reveals that they correspond mainly to short maturities and extreme strikes, with the highest MC errors.

### 3.3 Volatility Smile Calibration

Having built the datasets and trained the DNNs, we are now ready to use them to calibrate the SABR model parameters to market quotes, i.e. to solve the optimization problem in eq. ([21](https://arxiv.org/html/2510.10343v1#S2.E21 "In item 3 ‣ 2.4 Learning SABR with DNNs ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model")).
In order to compare the DNN results with those obtained with the “classic” Hagan et al. approximation, we also solve the corresponding optimization problem in eq. ([22](https://arxiv.org/html/2510.10343v1#S2.E22 "In 2.4 Learning SABR with DNNs ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model")).
The numerical solution of the calibration problem is influenced by the initial guess of the SABR parameters in eqs. ([21](https://arxiv.org/html/2510.10343v1#S2.E21 "In item 3 ‣ 2.4 Learning SABR with DNNs ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model")) and ([22](https://arxiv.org/html/2510.10343v1#S2.E22 "In 2.4 Learning SABR with DNNs ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model")). We opted for the simple approach of Random Search, considering a large number (300) of initial parameter sets generated randomly and uniformly using Latin Hypercube sampling and the parameters ranges reported in tab. [1](https://arxiv.org/html/2510.10343v1#S3.T1 "Table 1 ‣ Training Sets: ‣ 3.1 Datasets ‣ 3 Numerical Results ‣ Learning the Exact SABR Model"). For each initial sample, a local solution of the optimization problem was found using the L-BFGS-B algorithm available in scipy.optimize.minimize, and the best SABR parameter set was identified as the one associated with the minimum value of the objective function.

![Refer to caption](Figures/SABR_DNN_maturity_1.5055.png)

![Refer to caption](Figures/SABR_Hagan_maturity_1.5055.png)

![Refer to caption](Figures/SABR_DNN_maturity_1.5055.png)

![Refer to caption](Figures/SABR_DNN_maturity_1.5055.png)

![Refer to caption](Figures/SABR_DNN_maturity_30.0151.png)

![Refer to caption](Figures/SABR_Hagan_maturity_30.0151.png)

Figure 3: Shifted-SABR model calibrations for short (1.5y), medium (10y) and long (30y) maturities. Black crosses: market data. Blue lines: SABR DNN smile (left) obtained from the SABR parameters calibrated with SABR DNN, and SABR Hagan smile (right) obtained from the SABR parameters calibrated with Hagan et al. approximation.
Red lines: MC SABR DNN smile (left) obtained by MC simulations using the SABR parameters calibrated with SABR DNN, MC SABR Hagan smile (right) obtained by MC simulations using the SABR parameters calibrated with Hagan et al. approximation. High precision MC simulations performed with 2242^{24} scenarios and time steps as in tab. [4](https://arxiv.org/html/2510.10343v1#S3.T4 "Table 4 ‣ Training Sets: ‣ 3.1 Datasets ‣ 3 Numerical Results ‣ Learning the Exact SABR Model"). MC errors not shown being negligible. The numerical values corresponding to the smiles depicted in the figure and the respective calibrated parameters are provided in app. [E](https://arxiv.org/html/2510.10343v1#A5 "Appendix E Calibration Details ‣ Learning the Exact SABR Model").

We show in fig. [3](https://arxiv.org/html/2510.10343v1#S3.F3 "Figure 3 ‣ 3.3 Volatility Smile Calibration ‣ 3 Numerical Results ‣ Learning the Exact SABR Model") the calibration results for three selected short, medium and long maturities, of the Caplet/Floorlet shifted-Black volatility surface derived from EUR Caps/Floors on EURIBOR6M quoted on the over-the-counter (OTC) market as of 30/08/2024 (see app. [A.2](https://arxiv.org/html/2510.10343v1#A1.SS2 "A.2 Caps/Floors Market Quotations ‣ Appendix A Market Data ‣ Learning the Exact SABR Model")).
We observe in fig. [3](https://arxiv.org/html/2510.10343v1#S3.F3 "Figure 3 ‣ 3.3 Volatility Smile Calibration ‣ 3 Numerical Results ‣ Learning the Exact SABR Model") that both the SABR DNN and SABR Hagan smiles closely match the market smile across all three time horizons. This indicates that both approaches work as effective interpolators of market smiles, i.e. are able to find (different) SABR parameter sets which effectively fit the same market volatilities.
However, our objective is to assess the DNN performance in calibrating the “true” model-implied volatility smiles associated with the shifted-SABR model, provided by the unbiased Monte Carlo simulation of the shifted-SABR dynamics. To this end, we compare the SABR DNN and SABR Hagan smiles with those obtained from the MC simulations based on the respective calibrated SABR parameters. The discrepancy between these smiles measures how much the two calibration methodologies are consistent with the true shifted-SABR model. Fig. [3](https://arxiv.org/html/2510.10343v1#S3.F3 "Figure 3 ‣ 3.3 Volatility Smile Calibration ‣ 3 Numerical Results ‣ Learning the Exact SABR Model") clearly shows that, as the maturity increases, the SABR DNN and MC SABR DNN smiles remain nearly identical, while SABR Hagan smile becomes increasingly inconsistent with the “true” MC SABR Hagan smile, as expected.

A more detailed analysis of the volatility smile differences is shown in fig. [4](https://arxiv.org/html/2510.10343v1#S3.F4 "Figure 4 ‣ 3.3 Volatility Smile Calibration ‣ 3 Numerical Results ‣ Learning the Exact SABR Model") below, which plots the term structure of the Root Mean Square (relative) Distances (RMSD)

|  |  |  |  |
| --- | --- | --- | --- |
|  | RMSD​(Ti)=1NK​∑j=1NK[σ​(Ti,Kj)σM​C​(Ti,Kj)−1]2.\textit{RMSD}(T\_{i})=\sqrt{\frac{1}{N\_{K}}\sum\_{j=1}^{N\_{K}}\left[\frac{\sigma(T\_{i},K\_{j})}{\sigma^{MC}(T\_{i},K\_{j})}-1\right]^{2}}. |  | (23) |

We observe that, as the maturity increases, the RMSD remains nearly constant for the SABR DNN approach, while diverges for the SABR Hagan approach. More specifically, the right-hand panel shows that the effect is caused essentially by the lowest quoted strike, reaching values higher than those observed in the left-hand panel, while the highest strike works well. This finding confirms that the accuracy of Hagan et al. approximation decreases with increasing maturity and decreasing strikes, as expected.

![Refer to caption](Figures/RMSD_percentage.png)

![Refer to caption](Figures/RMSD_high_low_percentage.png)

Figure 4: Left panel: root mean square distance (RMSD) plots for both SABR DNN and SABR Hagan smiles as a function of maturity, considering all strikes together. Right panel: focus on the lowest and highest quoted strikes (-1.5% and 10%, respectively).

Further evidence is shown in fig. [5](https://arxiv.org/html/2510.10343v1#S3.F5 "Figure 5 ‣ 3.3 Volatility Smile Calibration ‣ 3 Numerical Results ‣ Learning the Exact SABR Model"), which reports a granular 3D comparison between SABR DNN and SABR Hagan volatilities as a function of both maturity and strike, using the absolute relative volatility difference (ARD)

|  |  |  |  |
| --- | --- | --- | --- |
|  | ARD​(Ti,Kj)=|σ​(Ti,Kj)σM​C​(Ti,Kj)−1|.\textit{ARD}(T\_{i},K\_{j})=\left|\frac{\sigma(T\_{i},K\_{j})}{\sigma^{MC}(T\_{i},K\_{j})}-1\right|. |  | (24) |

We observe on the left-hand side that the ARD for the SABR DNN approach is nearly constant across maturities and strikes, with a significantly lower magnitude compared to the right-hand side, where the ARD for the SABR Hagan et al. approximation sharply increases with increasing maturity and decreasing strike, reaching approximately 10%10\% in the worst corner (larger maturities, lower strikes).

![Refer to caption](Figures/3D_SABR_DNN.png)

  


(a) SABR DNN vs MC SABR DNN.

![Refer to caption](Figures/3D_SABR_HAGAN.png)

(b) SABR Hagan vs MC SABR Hagan.

Figure 5: 3D graphs depicting the absolute relative difference (ARD) between SABR DNN and MC SABR DNN smiles (left-hand panel) and between SABR Hagan and MC SABR Hagan smiles (right-hand panel).

The discussion so far regarded the pricing precision of Caplets/Floorlets, whose prices are obtained from Caps/Floors market quotations using the volatility stripping procedure described in app. [A.2](https://arxiv.org/html/2510.10343v1#A1.SS2 "A.2 Caps/Floors Market Quotations ‣ Appendix A Market Data ‣ Learning the Exact SABR Model"). We further checked that Caps/Floors, being portfolios of Caplets/Floorlets, are priced within the same precision, once we exclude the further uncertainty introduced by the volatility stripping procedure. We notice that our SABR DNN prices equally well also ATM Caps/Floors, which were not considered in the volatility smile calibration discussed at the beginning of this section.

We checked our results using other market datasets on different dates, finding consistent results (not reported here to avoid redundancy). Overall, these results confirm that the proposed SABR DNN methodology is consistent with the exact shifted-SABR model, and helps to quantify the increasing inaccuracy of Hagan et al. approximation.

### 3.4 Computational Performances

Finally, it is worth to make a remark on the computational time required by the proposed SABR DNN calibration approach.

The datasets generation discussed in sec. [3.1](https://arxiv.org/html/2510.10343v1#S3.SS1 "3.1 Datasets ‣ 3 Numerical Results ‣ Learning the Exact SABR Model") constitutes a high-performance computing task: given the ranges for
model and contract parameters
{θSABR,θCF}={α^,β,ρ,ν,T,K^}\left\{\theta^{\textit{SABR}},\theta^{\textit{CF}}\right\}=\left\{\hat{\alpha},\beta,\rho,\nu,T,\hat{K}\right\} reported in tab. [1](https://arxiv.org/html/2510.10343v1#S3.T1 "Table 1 ‣ Training Sets: ‣ 3.1 Datasets ‣ 3 Numerical Results ‣ Learning the Exact SABR Model"),
the process of datasets generation required approximately 25,000–30,000 CPU hours, parallelized on 256 CPUs (4 AMD EPYC 7003 processors with 64 cores, 3 GHz each).
Also the DNN training discussed in sec. [3.2](https://arxiv.org/html/2510.10343v1#S3.SS2 "3.2 DNNs Setup and Training ‣ 3 Numerical Results ‣ Learning the Exact SABR Model") is not a trivial task, because of the large datasets used. Although the DNNs sizes were contained (see tab. [5](https://arxiv.org/html/2510.10343v1#S3.T5 "Table 5 ‣ 3.2 DNNs Setup and Training ‣ 3 Numerical Results ‣ Learning the Exact SABR Model")), the training process took ≈1.5\approx 1.5 GPU hours for each of the three DNNs considered.
Taking into account also the empirical hyperparameter tuning described in sec. [3.2](https://arxiv.org/html/2510.10343v1#S3.SS2 "3.2 DNNs Setup and Training ‣ 3 Numerical Results ‣ Learning the Exact SABR Model"), where roughly 3-4 combinations were tested for each network, the total training time for each DNN took ≈5\approx 5 GPU hours.
However, these processes are conducted offline once and for all, after which the DNNs are ready to be used.

Contrary to the previous steps, once the datasets are available and the DNNs are trained, the online calibration of the SABR model on the market volatility surface, given the algebraic math of the DNNs, is extremely fast regardless of the hardware used, requiring less than a second per smile.

In conclusion, the proposed SABR DNN approach allows accurate and fast online calibration of market volatility surfaces while preserving a high computational efficiency.

### 3.5 Practical Use of SABR DNN for Caps/Floors

The typical usage of the “classic” SABR model with the Hagan et al. approximation for Caps/Floors is described in app. [B.2](https://arxiv.org/html/2510.10343v1#A2.SS2 "B.2 Practical Use of SABR for Caps/Floors ‣ Appendix B SABR Details ‣ Learning the Exact SABR Model").
The SABR DNN discussed in the previous sections allows to completely avoid the Hagan et al. approximation not only in the calibration phase, but also for any pricing purpose. In fact, the SABR DNN allows to compute the shifted-Black implied volatility σS​L​NDNN​(T,K)\sigma\_{SLN}^{\textit{DNN}}(T,K) for any maturity TT and strike KK using a two-dimensional interpolation scheme based on the SABR DNN in the strike dimension and on interpolation of variances in the maturity dimension using eq. ([26](https://arxiv.org/html/2510.10343v1#A1.E26 "In A.2 Caps/Floors Market Quotations ‣ Appendix A Market Data ‣ Learning the Exact SABR Model")).
Then, the price of Caplet/Floorlet for maturity TT and strike KK is computed using the shifted-lognormal (Black) pricing formula, eq. ([39](https://arxiv.org/html/2510.10343v1#A2.E39 "In B.1 Hagan et al. Approximation ‣ Appendix B SABR Details ‣ Learning the Exact SABR Model")).
Finally, the Cap/Floor price is obtained as the sum of discounted Caplets/Floorlets as in eq. ([3](https://arxiv.org/html/2510.10343v1#S2.E3 "In 2.1 Financial Instruments ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model")).
We notice that the pricing procedure above is separately applied to each single Caplet/Floorlet included in a Cap/Floor, using the appropriate SABR parameters for each Caplet/Floorlet maturity and the corresponding short, medium, or long maturity DNN.

Thanks to its pricing and computational performances, the SABR DNN is particularly suitable for situations requiring repeated pricing calls, e.g. pricing of large Caps/Floors portfolios, market and counterparty risk measurement (VaR, stressed VaR, Expected Shortfall, Expected Exposure, etc. even based on Monte Carlo simulations), stress testing, what if analyses, etc.

## 4 Conclusions and Directions of Future Work

### 4.1 Conclusions

In this paper, we develop and test SABR DNN, a SABR model based on specific Deep Neural Networks (DNNs) trained offline on a very large dataset of interest rate Caplets/Floorlets volatility surfaces consistent with Cap/Floor market quotations. We then use them to calibrate online real market quotations and as a general-purpose Cap/Floor pricer.

Since DNN performances depend crucially on data, we give particular importance to the initial offline generation of a very large dataset of interest rate volatility surfaces (more than 200 million points) for EUR Caplets/Floorlets including very long maturities (16 points from 1Y to 30Y) and extreme strikes (14 points from -1.5% to 10%, including the ATM), consistently with market quotations.
To this scope, we adapt to the SABR model the random grid approach proposed by [[3](https://arxiv.org/html/2510.10343v1#bib.bibx3)], taking into account the single-forward nature of SABR (i.e. requiring a different set of SABR parameters for each maturity), and selecting a strike grid independent of maturity.

We generate model prices using high-precision unbiased Monte Carlo simulation of the full shifted-SABR stochastic dynamics (without any usage of the Hagan et al. approximation), taking into account possible negative forward rates. In particular, the β\beta parameter is not fixed (as done e.g. in [[31](https://arxiv.org/html/2510.10343v1#bib.bibx31)]), but it is calibrated together with the other model parameters, preserving the full flexibility of the original SABR formulation. We still reduce the problem dimensionality recurring to a scaled version of the full SABR dynamics.

We develop, train and optimize offline a SABR DNN architecture specific for Caps and Floors, reaching a very good level of precision. We find that our SABR DNN acts as a filter, extracting true information from the dataset while discarding the noise related to Monte Carlo error.
Once trained, our SABR DNN is able to calibrate online the SABR model parameters to real market volatility surfaces quoted on different business dates with very high precision and computational performance.
We note that our SABR DNN “knows” only the forward rate fixing date, not the EURIBOR tenor nor the Caplet/Floorlet maturity date. Hence, once trained, it is able to calibrate Caplet/Floorlet volatilities on any IBOR tenor.
We conclude that our SABR DNN is robust and can be used in any pricing-intensive situation such as in real-time pricing of large Caps/Floors portfolios, market and counterparty risk measurement, stress testing, what if analyses, etc.

Furthermore, using our SABR DNN, we challenge the latest version of Hagan et al. analytical approximation [[17](https://arxiv.org/html/2510.10343v1#bib.bibx17)] precisely measuring how much it deteriorates in specific regions of the market volatility surface. The same approach can be adopted to challenge any other SABR approximation. Interestingly, the term structures of the SABR parameters obtained from the SABR DNN calibration display richer shapes than those coming from the Hagan et al. approximation, reflecting the ability of the SABR DNN to learn the “exact” SABR implied volatility function.

In conclusion, our results fully address the gaps in the previous machine learning SABR literature in a systematic and self-consistent way, establishing a comprehensive and functional SABR framework that can be adopted by practitioners for daily trading and risk management activities on Cap/Floor options.

### 4.2 Directions of Future Work

The SABR DNN approach described in this paper can be further developed, experimented, and adapted in a number of ways.

Regarding the coverage of the interest rate market, first of all one may consider the EUR Swaptions cube, characterized by one additional dimension beyond maturity and strike, i.e. the underlying IRS tenor, which presents a more difficult task for the SABR DNN.
Second, one may consider to join the previous datasets and train the SABR DNN on all possible EUR Caps, Floors and Swaptions together. This step would be very interesting to check the capability of the SABR DNN approach to price consistently any EUR interest rate European option and to detect possible inconsistencies and arbitrage opportunities between the different sections of the market.
Third, one may consider Caps/Floors/Swaptions on overnight rates, typical of e.g. USD or GBP markets101010After the financial benchmark reform, LIBORs were dismissed and LIBOR markets moved to overnight compounded rates..
The fourth and last step would be to join the previous cases and consider IR options on different rates and currencies.

The high performance of the SABR DNN calibration enables its test in those cases where multiple SABR model recalibrations are required. A typical example in the context of market risk management would be the calibration of historical or Monte Carlo volatility scenarios encountered in the calculation of market and counterparty risk measurement.
Further test could be to challenge possible SABR enhancements, such as e.g. those proposed by [[19](https://arxiv.org/html/2510.10343v1#bib.bibx19)] and [[20](https://arxiv.org/html/2510.10343v1#bib.bibx20)], using the approach suggested in sec. [3.3](https://arxiv.org/html/2510.10343v1#S3.SS3 "3.3 Volatility Smile Calibration ‣ 3 Numerical Results ‣ Learning the Exact SABR Model"), fig. [3](https://arxiv.org/html/2510.10343v1#S3.F3 "Figure 3 ‣ 3.3 Volatility Smile Calibration ‣ 3 Numerical Results ‣ Learning the Exact SABR Model").

Regarding the DNNs themselves, one may consider more sophisticated network structures and training strategies. For example, one may introduce control variates in the DNN training, as described e.g. by [[29](https://arxiv.org/html/2510.10343v1#bib.bibx29)] and [[13](https://arxiv.org/html/2510.10343v1#bib.bibx13)]. Furthermore, one may consider Derivative-Constrained Neural Networks (DCNNs), including derivatives in the objective function to generate smooth volatility surfaces and incorporate no-arbitrage conditions111111See e.g. [[26](https://arxiv.org/html/2510.10343v1#bib.bibx26)] for no-arbitrage conditions on the Swaption volatility cube., as suggested in [[24](https://arxiv.org/html/2510.10343v1#bib.bibx24)].

## References

* [1]
  Alexander Antonov, Michael Konikov and Michael Spector
  “SABR spreads its wings”
  In *Risk*, 2013, pp. 68–73
* [2]
  Alexander Antonov, Michael Konikov and Michael Spector
  “The free boundary SABR: natural extension to negative rates”
  In *Risk*, 2015, pp. 68–73
* [3]
  Fabio Baschetti, Giacomo Bormetti and Pietro Rossi
  “Deep calibration with random grids”
  In *Quantitative Finance* 24.9
  Routledge, 2024, pp. 1263–1285
  DOI: [10.1080/14697688.2024.2332375](https://dx.doi.org/10.1080/14697688.2024.2332375)
* [4]
  Christian Bayer and Benjamin Stemper
  “Deep calibration of rough stochastic volatility models”
  In *Arxiv*, 2018
  DOI: [10.48550/arXiv.1810.03399](https://dx.doi.org/10.48550/arXiv.1810.03399)
* [5]
   Bloomberg Quantitative Analytics
  “Bloomberg Volatility Cube”, 2018
* [6]
  Damiano Brigo and Fabio Mercurio
  “Interest Rate Models — Theory and Practice: With Smile, Inflation and Credit”
  Springer, 2006
  DOI: [10.1007/978-3-540-34604-3](https://dx.doi.org/10.1007/978-3-540-34604-3)
* [7]
  Ning Cai, Yingda Song and Nan Chen
  “Exact simulation of the SABR model”
  In *Operations Research* 65(4), 2017, pp. 931–951
  DOI: [10.1287/opre.2017.1617](https://dx.doi.org/10.1287/opre.2017.1617)
* [8]
  Bin Chen, Cornelis Oosterlee and Hans van der Weide
  “A low-bias simulation scheme for the SABR stochastic volatility model”
  In *International Journal of Theoretical and Applied Finance (IJTAF)* 15, 2012, pp. 1250016–1
  DOI: [10.1142/S0219024912500161](https://dx.doi.org/10.1142/S0219024912500161)
* [9]
  Jaehyuk Choi, Minsuk Kwak, Chyng Wen Tee and Yumeng Wang
  “A Black–Scholes user’s guide to the Bachelier model”
  In *Journal of Futures Markets* 42.5, 2022, pp. 959–980
  DOI: [10.1002/fut.22315](https://dx.doi.org/10.1002/fut.22315)
* [10]
  Christa Cuchiero, Wahid Khosrawi and Josef Teichmann
  “A Generative Adversarial Network Approach to Calibration of Local Stochastic Volatility Models”
  In *Risks* 8.4, 2020
  DOI: [10.3390/risks8040101](https://dx.doi.org/10.3390/risks8040101)
* [11]
  George V. Cybenko
  “Approximation by superpositions of a sigmoidal function”
  In *Mathematics of Control, Signals and Systems* 2, 1989, pp. 303–314
* [12]
  Ronen Eldan and Ohad Shamir
  “The power of depth for feedforward neural networks”
  In *Conference on learning theory*, 2016, pp. 907–940
  PMLR
* [13]
  Hideharu Funahashi
  “SABR equipped with AI wings”
  In *Quantitative Finance* 23.2
  Routledge, 2023, pp. 229–249
  DOI: [10.1080/14697688.2022.2150561](https://dx.doi.org/10.1080/14697688.2022.2150561)
* [14]
  Pierre Gauthier and Pierre-Yves Henri Rivaille
  “Fitting the Smile, Smart Parameters for SABR and Heston”
  In *SSRN*, 2009
  DOI: [10.2139/ssrn.1496982](https://dx.doi.org/10.2139/ssrn.1496982)
* [15]
  Ian Goodfellow, Yoshua Bengio and Aaron Courville
  “Deep Learning”
  The MIT Press, 2016
  URL: <http://www.deeplearningbook.org>
* [16]
  Patrick Hagan, Deep Kumar, Andrew Lesniewski and Diana Woodward
  “Managing Smile Risk”
  In *Wilmott Magazine* 1, 2002, pp. 84–108
* [17]
  Patrick Hagan, Deep Kumar, Andrew Lesniewski and Diana Woodward
  “Universal Smiles”
  In *Wilmott* 2016, 2016, pp. 40–55
  DOI: [10.1002/wilm.10523](https://dx.doi.org/10.1002/wilm.10523)
* [18]
  Patrick S. Hagan and Andrew S. Lesniewski
  “Bartlett’s Delta in the SABR Model”
  In *Wilmott* 2019, 2019, pp. 54–61
  DOI: [10.1002/wilm.10763](https://dx.doi.org/10.1002/wilm.10763)
* [19]
  Patrick S. Hagan, Andrew S. Lesniewski and Diana E. Woodward
  “Managing Vol Surfaces”
  In *Wilmott* 2018, 2018, pp. 24–43
  DOI: [10.1002/wilm.10643](https://dx.doi.org/10.1002/wilm.10643)
* [20]
  Pierre Henry-Labordere
  “SABR Model”
  In *Encyclopedia of Quantitative Finance*
  John Wiley & Sons, Ltd, 2010
  DOI: [10.1002/9780470061602.eqf08012](https://dx.doi.org/10.1002/9780470061602.eqf08012)
* [21]
  Kurt Hornik, Maxwell Stinchcombe and Halbert White
  “Multilayer feedforward networks are universal approximators”
  In *Neural Networks* 2.5, 1989, pp. 359–366
  DOI: [10.1016/0893-6080(89)90020-8](https://dx.doi.org/10.1016/0893-6080(89)90020-8)
* [22]
  Kurt Hornik, Maxwell Stinchcombe and Halbert White
  “Universal approximation of an unknown mapping and its derivatives using multilayer feedforward networks”
  In *Neural Networks* 3.5, 1990, pp. 551–560
  DOI: [10.1016/0893-6080(90)90005-6](https://dx.doi.org/10.1016/0893-6080(90)90005-6)
* [23]
  Blanka Horvath, Aitor Muguruza and Mehdi Tomas
  “Deep learning volatility: a deep neural network perspective on pricing and calibration in (rough) volatility models”
  In *Quantitative Finance* 21.1
  Taylor & Francis, 2020, pp. 11–27
  DOI: [10.1080/14697688.2020.1817974](https://dx.doi.org/10.1080/14697688.2020.1817974)
* [24]
  Kentaro Hoshisashi, Carolyn E. Phelan and Paolo Barucca
  “No-Arbitrage Deep Calibration for Volatility Smile and Skewness”
  In *Arxiv*, 2024
  DOI: [10.48550/arXiv.2310.16703](https://dx.doi.org/10.48550/arXiv.2310.16703)
* [25]
  Jaegi Jeon, Kyunghyun Park and Jeonggyu Huh
  “Extensive networks would eliminate the demand for pricing formulas”
  In *Knowledge-Based Systems* 237, 2022, pp. 107918
  DOI: [10.1016/j.knosys.2021.107918](https://dx.doi.org/10.1016/j.knosys.2021.107918)
* [26]
  Simon Johnson and Bereshad Nonas
  “Arbitrage-Free Construction of the Swaption Cube”
  In *Wilmott Journal* 1, 2009, pp. 137–143
  DOI: [10.1002/wilj.11](https://dx.doi.org/10.1002/wilj.11)
* [27]
  Joerg Kienitz
  “Transforming Volatility - Multi Curve Cap and Swaption Volatilities”
  In *SSRN*, 2013
  DOI: [10.2139/ssrn.2204702](https://dx.doi.org/10.2139/ssrn.2204702)
* [28]
  Joerg Kienitz
  “Stochastic volatility – A story of two decades of SABR and Wilmott Magazine”
  In *Wilmott* 2022
  Wilmott Magazine, Ltd, 2022, pp. 24–26
  DOI: [10.54946/wilm.11040](https://dx.doi.org/10.54946/wilm.11040)
* [29]
  Joerg Kienitz, Sarp Kaya Acar, Qian Liang and Nikolai Nowaczyk
  “The CV Makes the Difference–Control Variates for Neural Networks”
  In *SSRN*, 2020
  DOI: [10.2139/ssrn.3527314](https://dx.doi.org/10.2139/ssrn.3527314)
* [30]
  Mahir Lokvancic
  “Machine learning SABR model of stochastic volatility with lookup table”
  In *SSRN*, 2020
  DOI: [10.2139/ssrn.3589367](https://dx.doi.org/10.2139/ssrn.3589367)
* [31]
  William A. McGhee
  “An artificial neural network representation of the SABR stochastic volatility model”
  In *Journal of Computational Finance* 25.2, 2021
  DOI: [10.21314/JCF.2021.007](https://dx.doi.org/10.21314/JCF.2021.007)
* [32]
  Fabio Mercurio and Andrea Pallavicini
  “Smiling at convexity”
  In *Risk*, 2006, pp. 64–69
* [33]
  Jan Obloj
  “Fine-tune your smile: Correction to Hagan et al.”
  In *Wilmott*, 2008
  DOI: [10.48550/arXiv.0708.0998](https://dx.doi.org/10.48550/arXiv.0708.0998)
* [34]
  “OTC Derivatives Statistics”, 2025
  Bank of International Settlements
  URL: <https://data.bis.org/topics/OTC_DER/tables-and-dashboards>
* [35]
  Haozhe Su, M.. Tretyakov and David P. Newton
  “Deep Learning of Transition Probability Densities for Stochastic Asset Models with Applications in Option Pricing”
  In *Management Science* 71.4, 2025, pp. 2922–2952
  DOI: [10.1287/mnsc.2022.01448](https://dx.doi.org/10.1287/mnsc.2022.01448)
* [36]
  Tao L. Wu
  “Pricing and Hedging the Smile with SABR: Evidence from the Interest Rate Caps Market”
  In *Journal of Futures Markets* 32.8, 2012, pp. 773–791
  DOI: [10.1002/fut.21552](https://dx.doi.org/10.1002/fut.21552)
* [37]
  Mengfei Zhang and Frank J. Fabozzi
  “On the Estimation of the SABR Model’s Beta Parameter: The Role of Hedging in Determining the Beta Parameter”
  In *Journal of Derivatives* 24, 2016, pp. 48–57
  DOI: [10.3905/jod.2016.24.1.048](https://dx.doi.org/10.3905/jod.2016.24.1.048)

## Appendix A Market Data

### A.1 Trading Volumes for OTC Derivatives

We report in tab. [7](https://arxiv.org/html/2510.10343v1#A1.T7 "Table 7 ‣ A.1 Trading Volumes for OTC Derivatives ‣ Appendix A Market Data ‣ Learning the Exact SABR Model") data on trading volumes for OTC derivatives, supporting the SABR model relevance in global financial markets discussed in sec. [1.2](https://arxiv.org/html/2510.10343v1#S1.SS2 "1.2 The SABR Model ‣ 1 Introduction ‣ Learning the Exact SABR Model").

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Notional Amounts | | Gross Market Value | |
|  | 2023-S2 | 2024-S2 | 2023-S2 | 2024-S2 |
| All contracts | 667,058 | 699,476 | 18,122 | 17,615 |
| Interest rate contracts | 529,813 | 548,341 | 12,783 | 11,364 |
| FRAs | 56,023 | 55,105 | 403 | 367 |
| Swaps | 425,277 | 446,419 | 11,628 | 10,581 |
| Options | 48,288 | 46,156 | 698 | 600 |
| Other products | 224 | 205 | 54 | 36 |
| Foreign exchange contracts | 118,004 | 130,093 | 4,197 | 4,874 |
| Outright forwards and forex swaps | 67,797 | 72,827 | 2,196 | 2,553 |
| Currency swaps | 36,184 | 38,071 | 1,767 | 1,979 |
| Options | 13,999 | 19,171 | 234 | 324 |
| Other products | 24 | 24 | - | 18 |
| Equity-linked contracts | 7,783 | 8,901 | 582 | 662 |
| Forwards and swaps | 3,830 | 4,673 | 61 | 68 |
| Options | 3,954 | 4,226 | 324 | 332 |
| Commodity contracts | 2,203 | 2,208 | 301 | 257 |
| Forwards and swaps | 1,647 | 1,824 | - | - |
| Options | 556 | 383 | - | - |
| Credit derivatives | 8,708 | 9,229 | 209 | 213 |
| Other derivatives | 546 | 505 | 50 | 61 |

Table 7: Notional Amounts and Gross Market Values of OTC derivatives traded in the two semesters of 2024. Data in USD billions. Interest rate options result to be the most traded options on the market (600 $bln in S2-2024). Source: [[34](https://arxiv.org/html/2510.10343v1#bib.bibx34)], table DS.1 and DS.2.

### A.2 Caps/Floors Market Quotations

We report here a brief description of over-the-counter (OTC) market quotations for EUR Caps and Floors. As of 30/08/2024, the market quoted a surface of Cap/Floor prices including NT=16N\_{T}=16 maturities and NK=13N\_{K}=13 strikes (plus one ATM strike) as shown in fig. [6](https://arxiv.org/html/2510.10343v1#A1.F6 "Figure 6 ‣ A.2 Caps/Floors Market Quotations ‣ Appendix A Market Data ‣ Learning the Exact SABR Model").

![Refer to caption](Figures/QuotedCapsFloors.png)


Figure 6: An example of market quotations of EUR Cap/Floor prices as of 30/08/2024. Nominal amount = 10,000€. Empty values correspond to negligible prices. Rows for maturities 1Y, 18M, 2Y correspond to options on EURIBOR3M with quarterly cash flows, the other rows to options on EURIBOR6M with semiannual cash flows. The first column reports the option final maturity, i.e. the last cash flow date. At-the-money (ATM) columns reports ATM strikes, lying all between 2% and 3%, and prices. The ATM strike is the equilibrium strike which makes Cap and Floor prices equal. Strike columns between -1.5% and 2% show out-of-the-money (OTM) Floors, columns between 3% and 10% show OTM Caps. Conventionally, the first Caplet/Floorlet is not included in the Cap/Floor, since the underlying rate is already fixed. For example, the Cap 10Y includes 19 Caplets with maturity dates
{t1=1​Y,t2=1.5​Y,⋯,t19=10​Y}\{t\_{1}=1Y,t\_{2}=1.5Y,\cdots,t\_{19}=10Y\}. To take into account possible negative rates, the market conventionally assumes a forward rate shift λ=3%\lambda=3\% to compute shifted-lognormal implied volatilities.

Also other quotations are available, e.g. interest rate Futures Options quoted on exchanges.
The corresponding Caplet/Floorlet prices can be obtained through a procedure called volatility stripping (see e.g. [[5](https://arxiv.org/html/2510.10343v1#bib.bibx5)]), which leverages on the recursive Cap/Floor pricing formula,

|  |  |  |  |
| --- | --- | --- | --- |
|  | CF​(t;𝐓𝐢,K,ω)−CF​(t;𝐓𝐢−𝟏,K,ω)=∑tk>Ti−1TiPd​(t;tk)​cf​(t;tk−1,tk,K,ω),\textit{CF}(t;\mathbf{T\_{i}},K,\omega)-\textit{CF}(t;\mathbf{T\_{i-1}},K,\omega)=\sum\_{t\_{k}>T\_{i-1}}^{T\_{i}}P\_{d}(t;t\_{k})\textit{cf}(t;t\_{k-1},t\_{k},K,\omega), |  | (25) |

where Pd​(t;tk)P\_{d}(t;t\_{k}) is the discount factor121212In our definition eq. ([2](https://arxiv.org/html/2510.10343v1#S2.E2 "In 2.1 Financial Instruments ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model")) Caplet/Floorlet prices are not discounted. for date tkt\_{k}, Caplets/Floorlets on the right-hand side cover the time intervals
[tk−1,tk]⊂[Ti−1,Ti][t\_{k-1},t\_{k}]\subset[T\_{i-1},T\_{i}], and some interpolation scheme is required to fill the gaps.
A common scheme is linear interpolation of variances, i.e.

|  |  |  |  |
| --- | --- | --- | --- |
|  | v​(T,K)=tk−Ttk−tk−1​v​(tk−1,K)+T−tk−1tk−tk−1​v​(tk,K),wherev​(T,K)=σ2​(T,K)​(T−t)\displaystyle v(T,K)=\frac{t\_{k}-T}{t\_{k}-t\_{k-1}}v(t\_{k-1},K)+\frac{T-t\_{k-1}}{t\_{k}-t\_{k-1}}v(t\_{k},K),\quad\text{where}\quad v(T,K)=\sigma^{2}(T,K)(T-t) |  | (26) |

where T∈[tk−1,tk]T\in[t\_{k-1},t\_{k}] are Caplet/Floorlet fixing (not maturity) dates, and K∈{K1,⋯,KNK}K\in\{K\_{1},\cdots,K\_{N\_{K}}\}.
For example, from the quoted prices of two Caps on EURIBOR6M with maturities 9Y and 10Y, one may obtain the price of two Caplets insisting on [9Y,9.5Y] and [9.5Y,10Y] by interpolating the Caplet variance at 9Y (the fixing date of the first Caplet) between the Caplet variances at 8.5Y (available from the previous stripping step) and 9.5Y (the fixing date of the second Caplet).
The resulting Caplet/Floorlet surface has a semi-annual maturity grid with NT′=60N^{\prime}\_{T}=60 rows (a.k.a. smile sections), according to the EURIBOR6M tenor, and NK=14N\_{K}=14 strike columns, including the ATM.
Implied volatility surfaces for other EURIBOR tenors, i.e. 1M, 3M and 12M, require more sophisticated construction algorithms, see e.g. [[6](https://arxiv.org/html/2510.10343v1#bib.bibx6)], [[27](https://arxiv.org/html/2510.10343v1#bib.bibx27)] for further details.

We note that the volatility stripping procedure, based on interpolations and other modelling hypotheses (for non-quoted IBOR tenors), introduces a further level of uncertainty on Caplet/Floorlet prices with respect to Cap/Floor quotations.
Caps/Floors on overnight rates, typical of other markets (e.g. USD on SOFR, GBP on SONIA, etc.) have simpler structures, including one single Caplet/Floorlet per year and one single tenor, leading to less Caplet/Floorlet price uncertainty.

## Appendix B SABR Details

In this appendix we report some details regarding the shifted-SABR model used in this paper.

### B.1 Hagan et al. Approximation

The Hagan et al. analytical approximation of the SABR implied volatility was originally published in [[16](https://arxiv.org/html/2510.10343v1#bib.bibx16)] and improved in [[33](https://arxiv.org/html/2510.10343v1#bib.bibx33)].
The most recent version for the shifted-SABR model used in this paper was introduced in [[17](https://arxiv.org/html/2510.10343v1#bib.bibx17)], where the shifted-SABR implied normal volatility σNS​A​B​R\sigma\_{N}^{SABR} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | σNSABR​(t;T,F¯,K¯,θ)=ν​(K¯−F¯)​Z​(z)Y​(z),F≠K,\displaystyle\sigma\_{N}^{\textit{SABR}}(t;T,\bar{F},\bar{K},\theta)=\nu(\bar{K}-\bar{F})\frac{Z(z)}{Y(z)},\;F\neq K, |  | (27) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | z:=να¯​{K¯1−β−F¯1−β1−βfor​β≠1,ln​K¯F¯for​β=1,Z​(z):={1+Θ​(z)​τ​(t,T)for​Θ​(z)≥0,[1−Θ​(z)​τ​(t,T)]−1for​Θ​(z)<0,\displaystyle z:=\frac{\nu}{\bar{\alpha}}\left\{\begin{array}[]{ll}\frac{\bar{K}^{1-\beta}-\bar{F}^{1-\beta}}{1-\beta}&\text{for}\hskip 5.69046pt\beta\neq 1,\\ \mathrm{ln}\frac{\bar{K}}{\bar{F}}&\text{for}\hskip 5.69046pt\beta=1,\\ \end{array}\right.\hskip 14.22636ptZ(z):=\left\{\begin{array}[]{ll}1+\Theta(z)\tau(t,T)&\text{for}\hskip 5.69046pt\Theta(z)\geq 0,\\ \left[1-\Theta(z)\tau(t,T)\right]^{-1}&\text{for}\hskip 5.69046pt\Theta(z)<0,\\ \end{array}\right. |  | (32) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Θ​(z):=ν224​[−1+3​z+ρ−ρ​E​(z)Y​(z)​E​(z)]+α¯2​Δ06​[1−ρ2+(z+ρ)​E​(z)−ρY​(z)],\displaystyle\Theta(z):=\frac{\nu^{2}}{24}\left[-1+3\frac{z+\rho-\rho E(z)}{Y(z)E(z)}\right]+\frac{\bar{\alpha}^{2}\Delta\_{0}}{6}\left[1-\rho^{2}+\frac{(z+\rho)E(z)-\rho}{Y(z)}\right], |  | (33) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Y​(z):=ln⁡z+ρ+E​(z)1+ρ,E​(z):=1+2​ρ​z+z2,\displaystyle Y(z):=\ln\frac{z+\rho+E(z)}{1+\rho},\hskip 14.22636ptE(z):=\sqrt{1+2\rho z+z^{2}}, |  | (34) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | α¯:=α​[1+14​α​β​ρ​ν​F¯β−1​τ​(t,T)],Δ0:=−β​(2−β)8​F¯2−2​β,\displaystyle\bar{\alpha}:=\alpha\left[1+\frac{1}{4}\alpha\beta\rho\nu\bar{F}^{\beta-1}\tau(t,T)\right],\hskip 14.22636pt\Delta\_{0}:=-\frac{\beta(2-\beta)}{8\bar{F}^{2-2\beta}}, |  | (35) |

where tt is the valuation time, TT the forward rate fixing date (not the option’s maturity date), τ​(t,T)\tau(t,T) the year fraction for the time interval [t,T][t,T] (time to fixing), F¯:=F¯​(t)\bar{F}:=\bar{F}(t) and K¯\bar{K} are the shifted forward rate at pricing time tt and the shifted strike, respectively, and θ={α,β,ρ,ν}\theta=\{\alpha,\beta,\rho,\nu\} stands for the four SABR parameters131313Note that we keep here a generic valuation time tt instead of setting t=0t=0, consistently with Caplet/Floorlet and Caps/Floors pricing expressions in sec. [2.1](https://arxiv.org/html/2510.10343v1#S2.SS1 "2.1 Financial Instruments ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model"), and we denote with F:=F​(t)F:=F(t) the initial forward rate at time t<Tt<T. Instead in the SABR dynamics in eqs. ([5](https://arxiv.org/html/2510.10343v1#S2.E5 "In 2.2 Scaled Shifted-SABR Model ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model")) – ([9](https://arxiv.org/html/2510.10343v1#S2.E9 "In 2.2 Scaled Shifted-SABR Model ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model")) we denote the initial forward rate at time t=0t=0 by F​(0)=F0F(0)=F\_{0}..
For ATM options with F=KF=K we have

|  |  |  |  |
| --- | --- | --- | --- |
|  | σNSABR​(t;T,F¯,F¯,θ)=α¯​F¯β​ZATM,ΘATM:=ν224​(2−3​ρ2)+α¯2​Δ03,F=K.\displaystyle\sigma\_{N}^{\textit{SABR}}(t;T,\bar{F},\bar{F},\theta)=\bar{\alpha}\bar{F}^{\beta}Z\_{\textit{ATM}},\quad\Theta\_{\textit{ATM}}:=\frac{\nu^{2}}{24}(2-3\rho^{2})+\frac{\bar{\alpha}^{2}\Delta\_{0}}{3},\quad F=K. |  | (36) |

The shifted-SABR implied shifted-lognormal volatility can be implied from shifted-SABR prices using numerical inversion. Alternatively, one can use the approximated conversion formula for F≠KF\neq K

|  |  |  |  |
| --- | --- | --- | --- |
|  | σL​NSABR​(t;T,F¯,K¯,θ)=σNSABR​(t;T,F¯,K¯,θ)​ln​F¯K¯F¯−K¯​[1+σNSABR​(t;T,F¯,F¯,θ)2​τ​(t,T)24​F¯​K¯],\sigma\_{LN}^{\textit{SABR}}(t;T,\bar{F},\bar{K},\theta)=\sigma\_{N}^{\textit{SABR}}(t;T,\bar{F},\bar{K},\theta)\frac{\mathrm{ln}\frac{\bar{F}}{\bar{K}}}{\bar{F}-\bar{K}}\left[1+\frac{\sigma^{\textit{SABR}}\_{N}(t;T,\bar{F},\bar{F},\theta)^{2}\tau(t,T)}{24\bar{F}\bar{K}}\right], |  | (37) |

while for ATM options with F=KF=K, the approximation remains the one derived in [[16](https://arxiv.org/html/2510.10343v1#bib.bibx16)],

|  |  |  |  |
| --- | --- | --- | --- |
|  | σL​NSABR​(t;T,F¯,F¯,θ)=αF¯1−β​{1+[α2​(1−β)224​F¯2−2​β+α​β​ρ​ν4​F¯1−β+ν2​2−3​ρ224]​τ​(t,T)}.\sigma\_{LN}^{\textit{SABR}}(t;T,\bar{F},\bar{F},\theta)=\frac{\alpha}{\bar{F}^{1-\beta}}\left\{1+\left[\frac{\alpha^{2}(1-\beta)^{2}}{24\bar{F}^{2-2\beta}}+\frac{\alpha\beta\rho\nu}{4\bar{F}^{1-\beta}}+\nu^{2}\frac{2-3\rho^{2}}{24}\right]\tau(t,T)\right\}. |  | (38) |

Once the shifted-SABR implied volatility has been obtained using the Hagan et al. approximation, the (undiscounted) price of European Caplet/Floorlet options in eq. ([2](https://arxiv.org/html/2510.10343v1#S2.E2 "In 2.1 Financial Instruments ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model")) is simply given by either the shifted-lognormal (Black) or the normal (Bachelier) formulas141414For the sake of simplicity, in this paper we do not use the further corrections proposed in [[17](https://arxiv.org/html/2510.10343v1#bib.bibx17)] (secs. 1.4 and 1.5), but our framework is fully general and they could be easily included.,

|  |  |  |  |
| --- | --- | --- | --- |
|  | cf​(t;Ti−1,Ti,K,ω)\displaystyle\textit{cf}(t;T\_{i-1},T\_{i},K,\omega) | =𝔼tQdTi​{Max​{ω​[L​(Ti−1,Ti)−K]}}​τ​(Ti−1,Ti)\displaystyle=\mathbb{E}\_{t}^{Q\_{d}^{T\_{i}}}\left\{\textit{Max}\left\{\omega\left[L(T\_{i-1},T\_{i})-K\right]\right\}\right\}\tau(T\_{i-1},T\_{i}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =Black[F¯i(t),Ti,K¯,vL​NSABR(t;Ti−1),ω]τ(Ti−1,Ti)]\displaystyle=\textit{Black}\left[\bar{F}\_{i}(t),T\_{i},\bar{K},v\_{LN}^{\textit{SABR}}(t;T\_{i-1}),\omega]\tau(T\_{i-1},T\_{i})\right] |  | (39) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =Bach[F¯i(t),Ti,K¯,vNSABR(t;Ti−1),ω]τ(Ti−1,Ti)],\displaystyle=\textit{Bach}\left[\bar{F}\_{i}(t),T\_{i},\bar{K},v\_{N}^{\textit{SABR}}(t;T\_{i-1}),\omega]\tau(T\_{i-1},T\_{i})\right], |  | (40) |

where the SABR variances vxSABR​(t;T)v\_{x}^{\textit{SABR}}(t;T) are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | vxSABR​(t;T)=vxSABR​(t;T,F¯,K¯,θ)=σxSABR​(t;T,F¯,K¯,θ)2​τ​(t,T).v\_{x}^{\textit{SABR}}(t;T)=v\_{x}^{\textit{SABR}}(t;T,\bar{F},\bar{K},\theta)=\sigma\_{x}^{\textit{SABR}}(t;T,\bar{F},\bar{K},\theta)^{2}\tau(t,T). |  | (41) |

### B.2 Practical Use of SABR for Caps/Floors

We describe here the typical application of the SABR model with the Hagan et al. approximation to the Cap/Floor market, based on the following steps.

1. 1.

   Volatility stripping: from market prices of Caps/Floors obtain the corresponding Caplet/Floorlet normal or shifted-lognormal implied volatility NT×NKN\_{T}\times N\_{K} surface using the volatility stripping procedure discussed in app. [A.2](https://arxiv.org/html/2510.10343v1#A1.SS2 "A.2 Caps/Floors Market Quotations ‣ Appendix A Market Data ‣ Learning the Exact SABR Model") before.
2. 2.

   Shifted-SABR calibration: for each smile section (i.e. maturity row tk,k=1,⋯,NTt\_{k},k=1,\cdots,N\_{T}) in the Caplet/Floorlet volatility surface, corresponding to forward rate Fk​(t):=F​(t;tk−1,tk)F\_{k}(t):=F(t;t\_{k-1},t\_{k}), calibrate a separate shifted-SABR model using the Hagan et al. approximate eq. discussed in app. [B.1](https://arxiv.org/html/2510.10343v1#A2.SS1 "B.1 Hagan et al. Approximation ‣ Appendix B SABR Details ‣ Learning the Exact SABR Model") before, and obtain the corresponding SABR parameters {αk,βk,ρk,νk}\{\alpha\_{k},\beta\_{k},\rho\_{k},\nu\_{k}\}.
3. 3.

   Market repricing check: given the set of SABR parameters {αk,βk,ρk,νk}k=1NT\{\alpha\_{k},\beta\_{k},\rho\_{k},\nu\_{k}\}\_{k=1}^{N\_{T}}, reprice the market Caps/Floors and check the difference with respect to their corresponding market prices, to estimate and monitor the repricing error deriving from the numerical procedures used for volatility stripping and SABR calibration.
4. 4.

   Pricing: estimate the implied volatility σ​(T,K)\sigma(T,K) for any off-grid maturity TT and strike KK using a two-dimensional interpolation scheme based on the Hagan et al. approximate formula in the strike dimension and on interpolation of variances in the maturity dimension using formula ([26](https://arxiv.org/html/2510.10343v1#A1.E26 "In A.2 Caps/Floors Market Quotations ‣ Appendix A Market Data ‣ Learning the Exact SABR Model")).
   Finally, price Caplets/Floorlets and Caps/Floors with any maturity TT and strike KK from the corresponding implied volatilities using the normal or shifted-lognormal pricing formulas.

We note that the Hagan et al. approximation is used both in the calibration and pricing phases.
An extensive analysis of SABR performance with Caps/Floors can be found in [[36](https://arxiv.org/html/2510.10343v1#bib.bibx36)].

### B.3 Derivation of the Scaled Shifted-SABR Model

We derive here the scaled shifted-SABR model reported in sec. [2.2](https://arxiv.org/html/2510.10343v1#S2.SS2 "2.2 Scaled Shifted-SABR Model ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model"), eqs. [10](https://arxiv.org/html/2510.10343v1#S2.E10 "In 2.2 Scaled Shifted-SABR Model ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model")-[12](https://arxiv.org/html/2510.10343v1#S2.E12 "In 2.2 Scaled Shifted-SABR Model ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model").
We start from the forward rate dynamics in eq. ([5](https://arxiv.org/html/2510.10343v1#S2.E5 "In 2.2 Scaled Shifted-SABR Model ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model")) and we introduce the scaled stochastic process defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | X​(t):=F¯​(t)F¯0.X(t):=\frac{\bar{F}(t)}{\bar{F}\_{0}}. |  | (42) |

The corresponding dynamics of X​(t)X(t) and σ^​(t)\hat{\sigma}(t) can be derived by applying Itô’s Lemma,

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​X​(t)=σ^​(t)​X​(t)β​d​W​(t),X​(0)=1,\displaystyle dX(t)=\hat{\sigma}(t)X(t)^{\beta}dW(t),\quad X(0)=1, |  | (43) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | σ^​(t):=σ​(t)​F¯0β−1,\displaystyle\hat{\sigma}(t):=\sigma(t)\bar{F}\_{0}^{\beta-1}, |  | (44) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | d​σ^​(t)=F¯0β−1​ν​σ​(t)​d​Z​(t)=ν​σ^​(t)​d​Z​(t),σ^​(0)=α​F¯0β−1:=α^.\displaystyle d\hat{\sigma}(t)=\bar{F}\_{0}^{\beta-1}\nu\sigma(t)dZ(t)=\nu\hat{\sigma}(t)dZ(t),\quad\hat{\sigma}(0)=\alpha\bar{F}\_{0}^{\beta-1}:=\hat{\alpha}. |  | (45) |

We observe that the scaled volatility dynamics has the same form of the original volatility dynamics in the shifted-SABR model in eq. ([6](https://arxiv.org/html/2510.10343v1#S2.E6 "In 2.2 Scaled Shifted-SABR Model ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model")).
Consequently, the shifted-lognormal implied volatility of a Caplet/Floorlet with contract parameters
θCF={T,K¯}\theta^{\textit{CF}}=\left\{T,\bar{K}\right\} and model parameters
θSABR={F¯0,α,β,ρ,ν}\theta^{\textit{SABR}}=\left\{\bar{F}\_{0},\alpha,\beta,\rho,\nu\right\}
coincides with the shifted-lognormal implied volatility of a Caplet/Floorlet with contract parameters
θCF={T,K^=K¯F¯0}\theta^{\textit{CF}}=\left\{T,\hat{K}=\frac{\bar{K}}{\bar{F}\_{0}}\right\} and model parameters
θSABR={1,α^=αF¯0β−1,β,ρ,ν}\theta^{\textit{SABR}}=\left\{1,\hat{\alpha}=\alpha\bar{F}\_{0}^{\beta-1},\beta,\rho,\nu\right\}.
The prices of the two options differ by a multiplicative deterministic factor F¯0\bar{F}\_{0}, but the associated shifted-lognormal implied volatilities coincide, since they are related to the price through the shifted-Black formula.

## Appendix C Dataset Details

In this appendix, we report some results that can serve as benchmarks for future research, as well as details regarding the analysis we conducted on the Monte Carlo pricing error.

### C.1 Benchmark Caplet/Floorlet Prices

In this section we provide two samples of Caplet/Floorlet prices151515For the sake of simplicity, we omit the year fraction τ​(Ti−1,Ti)\tau(T\_{i-1},T\_{i}) in eq. ([2](https://arxiv.org/html/2510.10343v1#S2.E2 "In 2.1 Financial Instruments ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model")). computed by Monte Carlo simulation as described in sec. [2.3](https://arxiv.org/html/2510.10343v1#S2.SS3 "2.3 SABR Monte Carlo ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model") and using the SABR dynamics defined in ([18](https://arxiv.org/html/2510.10343v1#S2.E18 "In 2.3 SABR Monte Carlo ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model")) and ([19](https://arxiv.org/html/2510.10343v1#S2.E19 "In 2.3 SABR Monte Carlo ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model")).
In tab. [8](https://arxiv.org/html/2510.10343v1#A3.T8 "Table 8 ‣ C.1 Benchmark Caplet/Floorlet Prices ‣ Appendix C Dataset Details ‣ Learning the Exact SABR Model") we show the two parameter sets used in the simulation, and in the two tables [9](https://arxiv.org/html/2510.10343v1#A3.T9 "Table 9 ‣ C.1 Benchmark Caplet/Floorlet Prices ‣ Appendix C Dataset Details ‣ Learning the Exact SABR Model") and [10](https://arxiv.org/html/2510.10343v1#A3.T10 "Table 10 ‣ C.1 Benchmark Caplet/Floorlet Prices ‣ Appendix C Dataset Details ‣ Learning the Exact SABR Model") we report the corresponding option prices.
These results can serve as benchmarks for future research in this field.

| Case | F0F\_{0} | α\alpha | β\beta | ρ\rho | ν\nu | λ\lambda | NM​CN\_{MC} | ΔM​C\Delta\_{MC} (days) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I | 1 | 0.1178 | 0.8738 | -0.0702 | 0.5010 | 3% | 2202^{20} | 0.5 |
| II | 1 | 0.1822 | 0.3044 | 0.1243 | 0.3127 | 3% | 2202^{20} | 0.5 |

Table 8: Shifted-SABR parameters used to compute the MC prices reported in the following tabs. [9](https://arxiv.org/html/2510.10343v1#A3.T9 "Table 9 ‣ C.1 Benchmark Caplet/Floorlet Prices ‣ Appendix C Dataset Details ‣ Learning the Exact SABR Model") and [10](https://arxiv.org/html/2510.10343v1#A3.T10 "Table 10 ‣ C.1 Benchmark Caplet/Floorlet Prices ‣ Appendix C Dataset Details ‣ Learning the Exact SABR Model").



| Maturity (y) | Strike (K) | Floorlet price | Caplet price |
| --- | --- | --- | --- |
| 2 | 0.5 | 0.00063 ±\pm 0.00006 | 0.50045 ±\pm 0.00057 |
| 0.6 | 0.00177 ±\pm 0.00005 | 0.40159 ±\pm 0.00056 |
| 0.7 | 0.00476 ±\pm 0.00009 | 0.30458 ±\pm 0.00054 |
| 0.8 | 0.01249 ±\pm 0.00014 | 0.21231 ±\pm 0.00051 |
| 0.9 | 0.03132 ±\pm 0.00022 | 0.13114 ±\pm 0.00045 |
| 1.0 | 0.07070 ±\pm 0.00031 | 0.07052 ±\pm 0.00038 |
| 1.1 | 0.13494 ±\pm 0.00040 | 0.03476 ±\pm 0.00030 |
| 1.2 | 0.21742 ±\pm 0.00046 | 0.01724 ±\pm 0.00023 |
| 1.3 | 0.30925 ±\pm 0.00050 | 0.00907 ±\pm 0.00018 |
| 1.4 | 0.40530 ±\pm 0.00052 | 0.00511 ±\pm 0.00015 |
| 10 | 0.5 | 0.02865 ±\pm 0.00030 | 0.52680 ±\pm 0.00349 |
| 0.6 | 0.04096 ±\pm 0.00038 | 0.43911 ±\pm 0.00347 |
| 0.7 | 0.05776 ±\pm 0.00046 | 0.35590 ±\pm 0.00346 |
| 0.8 | 0.08130 ±\pm 0.00055 | 0.27944 ±\pm 0.00344 |
| 0.9 | 0.11498 ±\pm 0.00064 | 0.21312 ±\pm 0.00342 |
| 1.0 | 0.16260 ±\pm 0.00073 | 0.16074 ±\pm 0.00340 |
| 1.1 | 0.22549 ±\pm 0.00081 | 0.12357 ±\pm 0.00337 |
| 1.2 | 0.30054 ±\pm 0.00088 | 0.09868 ±\pm 0.00335 |
| 1.3 | 0.38368 ±\pm 0.00093 | 0.08183 ±\pm 0.00333 |
| 1.4 | 0.47181 ±\pm 0.00098 | 0.06995 ±\pm 0.00332 |

Table 9: Monte Carlo Caplet/Floorlet prices (undiscounted and without the year fraction in eq. ([2](https://arxiv.org/html/2510.10343v1#S2.E2 "In 2.1 Financial Instruments ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model"))) obtained using case I parameters in tab. [8](https://arxiv.org/html/2510.10343v1#A3.T8 "Table 8 ‣ C.1 Benchmark Caplet/Floorlet Prices ‣ Appendix C Dataset Details ‣ Learning the Exact SABR Model"). The Monte Carlo errors are computed as three standard deviations. We note that the strike KK is equal to the moneyness K/F0K/F\_{0} since in this case F0=1F\_{0}=1.



| Maturity (y) | Strike (K) | Floorlet price | Caplet price |
| --- | --- | --- | --- |
| 2 | 0.5 | 0.00256 ±\pm 0.00007 | 0.50234 ±\pm 0.00079 |
| 0.6 | 0.00643 ±\pm 0.00011 | 0.40620 ±\pm 0.00077 |
| 0.7 | 0.01493 ±\pm 0.00016 | 0.31470 ±\pm 0.00073 |
| 0.8 | 0.03166 ±\pm 0.00024 | 0.23143 ±\pm 0.00068 |
| 0.9 | 0.06081 ±\pm 0.00034 | 0.16059 ±\pm 0.00060 |
| 1.0 | 0.10538 ±\pm 0.00044 | 0.10515 ±\pm 0.00051 |
| 1.1 | 0.16571 ±\pm 0.00053 | 0.06549 ±\pm 0.00042 |
| 1.2 | 0.23953 ±\pm 0.00061 | 0.03930 ±\pm 0.00034 |
| 1.3 | 0.32327 ±\pm 0.00067 | 0.02304 ±\pm 0.00026 |
| 1.4 | 0.41359 ±\pm 0.00071 | 0.01336 ±\pm 0.00020 |
| 10 | 0.5 | 0.05966 ±\pm 0.00044 | 0.56085 ±\pm 0.00198 |
| 0.6 | 0.08183 ±\pm 0.00053 | 0.48303 ±\pm 0.00193 |
| 0.7 | 0.11008 ±\pm 0.00063 | 0.41128 ±\pm 0.00187 |
| 0.8 | 0.14556 ±\pm 0.00074 | 0.34677 ±\pm 0.00181 |
| 0.9 | 0.18917 ±\pm 0.00084 | 0.29036 ±\pm 0.00174 |
| 1.0 | 0.24118 ±\pm 0.00094 | 0.24237 ±\pm 0.00167 |
| 1.1 | 0.30127 ±\pm 0.00103 | 0.20246 ±\pm 0.00160 |
| 1.2 | 0.36860 ±\pm 0.00112 | 0.16979 ±\pm 0.00154 |
| 1.3 | 0.44208 ±\pm 0.00120 | 0.14327 ±\pm 0.00147 |
| 1.4 | 0.52059 ±\pm 0.00127 | 0.12178 ±\pm 0.00141 |

Table 10: As in tab. [9](https://arxiv.org/html/2510.10343v1#A3.T9 "Table 9 ‣ C.1 Benchmark Caplet/Floorlet Prices ‣ Appendix C Dataset Details ‣ Learning the Exact SABR Model"), using case II parameters in tab. [8](https://arxiv.org/html/2510.10343v1#A3.T8 "Table 8 ‣ C.1 Benchmark Caplet/Floorlet Prices ‣ Appendix C Dataset Details ‣ Learning the Exact SABR Model").

### C.2 Monte Carlo Error Analysis

As seen in the benchmark prices in tabs. [9](https://arxiv.org/html/2510.10343v1#A3.T9 "Table 9 ‣ C.1 Benchmark Caplet/Floorlet Prices ‣ Appendix C Dataset Details ‣ Learning the Exact SABR Model") and [10](https://arxiv.org/html/2510.10343v1#A3.T10 "Table 10 ‣ C.1 Benchmark Caplet/Floorlet Prices ‣ Appendix C Dataset Details ‣ Learning the Exact SABR Model"), we observe that Monte Carlo pricing errors are systematically smaller for out–of–the–money (OTM) short term (2Y) options. This is explained by the fact that, when an option is OTM, most simulated payoffs are zero, with only a small fraction being positive and close to zero, leading to a low variance in the payoff distribution. Since the MC error scales with the payoff’s standard deviation, OTM options exhibit smaller errors than in–the–money (ITM) options.
However, this observation does not hold for longer maturity options (10Y), where ITM Floorlet options systematically exhibit lower Monte Carlo errors. This effect occurs when volatility of volatility ν\nu, initial volatility α\alpha, correlation ρ\rho, and/or time to maturity assume higher values, i.e. in higher-uncertainty scenarios, and can be explained by the asymmetric nature of MC price paths: upward price movements are theoretically unlimited, as the forward rate can rise without bound, whereas downward price movements are limited, since the forward rate cannot fall below the rate shift λ\lambda. As a consequence, we have the following more complex behaviour of the MC price simulation.

* •

  Caplets: some MC price paths of OTM Caplets may occasionally end up deep ITM, when the forward rate rises significantly. These rare but very large payoffs create a long right tail in the payoff distribution, increasing its MC error.
* •

  Floorlets: their payoff is capped by the (shifted) strike, because the forward rate cannot fall below the shift λ\lambda. Even in higher-uncertainty scenarios, MC price paths of OTM Floorlets are limited, leading to lower MC errors compared to the corresponding Caplets.

This behaviour can be analytically examined in the limit case of the shifted-Black model, where the Caplet/Floorlet variances (undiscounted and omitting the year fraction in eq. ([2](https://arxiv.org/html/2510.10343v1#S2.E2 "In 2.1 Financial Instruments ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model"))) are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Var(t;T,F¯,K¯,v,ω)=𝔼tℚT[max[ω(F¯(T)−K¯);0]2]−𝔼tℚT[max[ω(F¯(T)−K¯);0]]2=F¯2​(t)​ev​Φ​(ω​d0)+K¯2​Φ​(ω​d−)−2​F¯​(t)​K¯​Φ​(ω​d+)−[F¯​(t)​Φ​(ω​d+)−K¯​Φ​(ω​d−)]2=F¯2​(t)​ev​Φ​(ω​d0)−F¯​(t)​K¯​Φ​(ω​d+)−K¯​ω​V​(t;T,F¯,K¯,v,ω)−V​(t;T,F¯,K¯,v,ω)2,\textit{Var}(t;T,\bar{F},\bar{K},v,\omega)=\mathbb{E}\_{t}^{\mathbb{Q}\_{T}}\left[\max\left[\omega\left(\bar{F}(T)-\bar{K}\right);0\right]^{2}\right]-\mathbb{E}\_{t}^{\mathbb{Q}\_{T}}\left[\max\left[\omega\left(\bar{F}(T)-\bar{K}\right);0\right]\right]^{2}\\ =\bar{F}^{2}(t)e^{v}\Phi(\omega d\_{0})+\bar{K}^{2}\Phi(\omega d\_{-})-2\bar{F}(t)\bar{K}\Phi(\omega d\_{+})-\left[\bar{F}(t)\Phi(\omega d\_{+})-\bar{K}\Phi(\omega d\_{-})\right]^{2}\\ =\bar{F}^{2}(t)e^{v}\Phi(\omega d\_{0})-\bar{F}(t)\bar{K}\Phi(\omega d\_{+})-\bar{K}\omega V(t;T,\bar{F},\bar{K},v,\omega)-V(t;T,\bar{F},\bar{K},v,\omega)^{2}, |  | (46) |

where ℚT\mathbb{Q}\_{T}, is the T−T-forward probability measure, σ\sigma is the shifted-lognormal volatility, v=σ2​(T−t)v=\sigma^{2}(T-t) its associated variance, Φ​(x)\Phi(x) is the standard normal cumulated distribution function, ω=±1\omega=\pm 1 for Caplets/Floorlets, respectively, and

|  |  |  |  |
| --- | --- | --- | --- |
|  | V​(t;T,F¯,K¯,v,ω)=ω​[F¯​(t)​Φ​(ω​d+)−K¯​Φ​(ω​d−)],d±=ln⁡(F¯​(t)K¯)±12​vv,d0=d−+2​v.V(t;T,\bar{F},\bar{K},v,\omega)=\omega\left[\bar{F}(t)\Phi(\omega d\_{+})-\bar{K}\Phi(\omega d\_{-})\right],\quad d\_{\pm}=\frac{\ln\left(\frac{\bar{F}(t)}{\bar{K}}\right)\pm\frac{1}{2}v}{\sqrt{v}},\quad d\_{0}=d\_{-}+2\sqrt{v}. |  | (47) |

From eq. ([46](https://arxiv.org/html/2510.10343v1#A3.E46 "In C.2 Monte Carlo Error Analysis ‣ Appendix C Dataset Details ‣ Learning the Exact SABR Model")) we observe that, for large variance vv, some terms cancel each other and we are left with

|  |  |  |  |
| --- | --- | --- | --- |
|  | Var​(t;T,F¯,K¯,v,ω)​≈v→∞​F¯​(t)2​ev​Φ​(ω​32​v),\displaystyle\textit{Var}(t;T,\bar{F},\bar{K},v,\omega)\underset{v\rightarrow\infty}{\approx}\bar{F}(t)^{2}e^{v}\Phi\left(\omega\frac{3}{2}\sqrt{v}\right), |  | (48) |

which is always larger for Caplets (ω=1\omega=1) than for Floorlets (ω=−1\omega=-1).

We show in tab. [12](https://arxiv.org/html/2510.10343v1#A3.T12 "Table 12 ‣ C.2 Monte Carlo Error Analysis ‣ Appendix C Dataset Details ‣ Learning the Exact SABR Model") the Monte Carlo Caplet/Floorlet prices computed as described in sec. [2.3](https://arxiv.org/html/2510.10343v1#S2.SS3 "2.3 SABR Monte Carlo ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model") in the limit of shifted-Black case using the parameters listed in tab. [11](https://arxiv.org/html/2510.10343v1#A3.T11 "Table 11 ‣ C.2 Monte Carlo Error Analysis ‣ Appendix C Dataset Details ‣ Learning the Exact SABR Model"), along with their analytical variances obtained from eq. ([46](https://arxiv.org/html/2510.10343v1#A3.E46 "In C.2 Monte Carlo Error Analysis ‣ Appendix C Dataset Details ‣ Learning the Exact SABR Model")).

| T (y) | F0F\_{0} | λ\lambda | α\alpha | β\beta | ρ\rho | ν\nu | NM​CN\_{MC} | ΔM​C\Delta\_{MC} (days) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 1 | 3% | see tab. [12](https://arxiv.org/html/2510.10343v1#A3.T12 "Table 12 ‣ C.2 Monte Carlo Error Analysis ‣ Appendix C Dataset Details ‣ Learning the Exact SABR Model") | 1 | 0 | 0 | 2202^{20} | 0.5 |

Table 11: Shifted-SABR parameters corresponding to the limit case of shifted-Black, used to compute the MC prices reported in tab. [12](https://arxiv.org/html/2510.10343v1#A3.T12 "Table 12 ‣ C.2 Monte Carlo Error Analysis ‣ Appendix C Dataset Details ‣ Learning the Exact SABR Model"). The parameter α\alpha corresponds to σ\sigma in eq. ([46](https://arxiv.org/html/2510.10343v1#A3.E46 "In C.2 Monte Carlo Error Analysis ‣ Appendix C Dataset Details ‣ Learning the Exact SABR Model")), its values are reported directly in tab. [12](https://arxiv.org/html/2510.10343v1#A3.T12 "Table 12 ‣ C.2 Monte Carlo Error Analysis ‣ Appendix C Dataset Details ‣ Learning the Exact SABR Model").

As discussed above, we observe that for lower values of α\alpha the OTM options always show lower MC errors and analytical variances. As the value of α\alpha increases, the Caplet variances increase more than the Floorlet variances, leading to a situation where the Floorlet MC error and variance are always lower with respect to the Caplet ones. We note that, in this limit case, the effect increases with option’s time to maturity, since the variance depends on α2​(T−t)\alpha^{2}(T-t).

| α\alpha | Strike (K) | MC Floorlet price | MC Caplet price | Floorlet variance | Caplet variance |
| --- | --- | --- | --- | --- | --- |
| 0.1 | 0.7 | 0.00030±0.000010.00030\pm 0.00001 | 0.30026±0.000430.30026\pm 0.00043 | 0.00002 | 0.02123 |
| 0.8 | 0.00361±0.000050.00361\pm 0.00005 | 0.20357±0.000410.20357\pm 0.00041 | 0.00029 | 0.01967 |
| 0.9 | 0.01904±0.000130.01904\pm 0.00013 | 0.11900±0.000360.11900\pm 0.00036 | 0.00190 | 0.01501 |
| 1.0 | 0.05806±0.000230.05806\pm 0.00023 | 0.05802±0.000270.05802\pm 0.00027 | 0.00614 | 0.00855 |
| 1.1 | 0.12344±0.000320.12344\pm 0.00032 | 0.02340±0.000180.02340\pm 0.00018 | 0.01202 | 0.00362 |
| 1.2 | 0.20796±0.000380.20796\pm 0.00038 | 0.00792±0.000100.00792\pm 0.00010 | 0.01693 | 0.00120 |
| 1.3 | 0.30235±0.000410.30235\pm 0.00041 | 0.00231±0.000050.00231\pm 0.00005 | 0.01970 | 0.00033 |
| 0.3 | 0.7 | 0.04281±0.000260.04281\pm 0.00026 | 0.34263±0.001210.34263\pm 0.00121 | 0.00811 | 0.17180 |
| 0.8 | 0.07566±0.000370.07566\pm 0.00037 | 0.27548±0.001140.27548\pm 0.00114 | 0.01588 | 0.15165 |
| 0.9 | 0.11929±0.000480.11929\pm 0.00048 | 0.21912±0.001060.21912\pm 0.00106 | 0.02668 | 0.13021 |
| 1.0 | 0.17298±0.000590.17298\pm 0.00059 | 0.17280±0.000970.17280\pm 0.00097 | 0.04005 | 0.10929 |
| 1.1 | 0.23559±0.000690.23559\pm 0.00069 | 0.13541±0.000880.13541\pm 0.00088 | 0.05518 | 0.09009 |
| 1.2 | 0.30581±0.000780.30581\pm 0.00078 | 0.10563±0.000790.10563\pm 0.00079 | 0.07119 | 0.07324 |
| 1.3 | 0.38232±0.000870.38232\pm 0.00087 | 0.08214±0.000710.08214\pm 0.00071 | 0.08727 | 0.05893 |
| 0.5 | 0.7 | 0.11993±0.000500.11993\pm 0.00050 | 0.41948±0.002180.41948\pm 0.00218 | 0.02901 | 0.55848 |
| 0.8 | 0.16827±0.000610.16827\pm 0.00061 | 0.36783±0.002110.36783\pm 0.00211 | 0.04376 | 0.52047 |
| 0.9 | 0.22340±0.000730.22340\pm 0.00073 | 0.32295±0.002030.32295\pm 0.00203 | 0.06122 | 0.48240 |
| 1.0 | 0.28448±0.000830.28448\pm 0.00083 | 0.28403±0.001950.28403\pm 0.00195 | 0.08089 | 0.44533 |
| 1.1 | 0.35074±0.000940.35074\pm 0.00094 | 0.25029±0.001870.25029\pm 0.00187 | 0.10225 | 0.40992 |
| 1.2 | 0.42144±0.001040.42144\pm 0.00104 | 0.22100±0.001790.22100\pm 0.00179 | 0.12480 | 0.37658 |
| 1.3 | 0.49598±0.001130.49598\pm 0.00113 | 0.19553±0.001720.19553\pm 0.00172 | 0.14810 | 0.34550 |

Table 12: Monte Carlo Caplet/Floorlet prices (undiscounted and without the year fraction in eq. ([2](https://arxiv.org/html/2510.10343v1#S2.E2 "In 2.1 Financial Instruments ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model"))) obtained using the parameters reported in tab. [11](https://arxiv.org/html/2510.10343v1#A3.T11 "Table 11 ‣ C.2 Monte Carlo Error Analysis ‣ Appendix C Dataset Details ‣ Learning the Exact SABR Model"). The Monte Carlo errors are computed as three standard deviations. The last two columns show the analytical variances computed using eq. ([46](https://arxiv.org/html/2510.10343v1#A3.E46 "In C.2 Monte Carlo Error Analysis ‣ Appendix C Dataset Details ‣ Learning the Exact SABR Model")), which (dividing by the number of MC scenarios in tab. [11](https://arxiv.org/html/2510.10343v1#A3.T11 "Table 11 ‣ C.2 Monte Carlo Error Analysis ‣ Appendix C Dataset Details ‣ Learning the Exact SABR Model") and taking the square root) agree to high accuracy with the estimated MC errors in cols. Caplet and Floorlet price.

## Appendix D DNN Details

In this appendix we report more details about the three DNNs discussed in sec. [3.2](https://arxiv.org/html/2510.10343v1#S3.SS2 "3.2 DNNs Setup and Training ‣ 3 Numerical Results ‣ Learning the Exact SABR Model"). The following figs. [7](https://arxiv.org/html/2510.10343v1#A4.F7 "Figure 7 ‣ Appendix D DNN Details ‣ Learning the Exact SABR Model"), [8](https://arxiv.org/html/2510.10343v1#A4.F8 "Figure 8 ‣ Appendix D DNN Details ‣ Learning the Exact SABR Model"), and [9](https://arxiv.org/html/2510.10343v1#A4.F9 "Figure 9 ‣ Appendix D DNN Details ‣ Learning the Exact SABR Model") show the scatter plots for training and test sets of the three DNNs.
The graphs below confirm the findings discussed in sec. [3.2](https://arxiv.org/html/2510.10343v1#S3.SS2 "3.2 DNNs Setup and Training ‣ 3 Numerical Results ‣ Learning the Exact SABR Model"). In particular, fig. [7](https://arxiv.org/html/2510.10343v1#A4.F7 "Figure 7 ‣ Appendix D DNN Details ‣ Learning the Exact SABR Model") shows that, for the training set, there is a larger and more concentrated region where the discrepancies between the DNN-implied volatilities and those in the training data are more pronounced. By contrast, in figs. [8](https://arxiv.org/html/2510.10343v1#A4.F8 "Figure 8 ‣ Appendix D DNN Details ‣ Learning the Exact SABR Model") and [9](https://arxiv.org/html/2510.10343v1#A4.F9 "Figure 9 ‣ Appendix D DNN Details ‣ Learning the Exact SABR Model") this region is noticeably smaller. These results support the conclusions of sec. [3.2](https://arxiv.org/html/2510.10343v1#S3.SS2 "3.2 DNNs Setup and Training ‣ 3 Numerical Results ‣ Learning the Exact SABR Model"), namely that the most significant deviations were associated with noisier data points, which predominantly correspond to short maturities and extreme strikes.

![Refer to caption](Figures/Train_datashader4Y.png)

![Refer to caption](Figures/Test_scatter4Y.png)

Figure 7: Scatter plots for the training and test sets of the short term DNN.



![Refer to caption](Figures/Train_datashader10Y.png)

![Refer to caption](Figures/Test_scatter10Y.png)

Figure 8: Scatter plots for the training and test sets of the medium term DNN.



![Refer to caption](Figures/Train_datashader30Y.png)

![Refer to caption](Figures/Test_scatter30Y.png)

Figure 9: Scatter plots for the training and test sets of the long term DNN.

## Appendix E Calibration Details

In this appendix we report additional details on smile calibration discussed in sec. [3.3](https://arxiv.org/html/2510.10343v1#S3.SS3 "3.3 Volatility Smile Calibration ‣ 3 Numerical Results ‣ Learning the Exact SABR Model").
We show in tab. [13](https://arxiv.org/html/2510.10343v1#A5.T13 "Table 13 ‣ Appendix E Calibration Details ‣ Learning the Exact SABR Model") the shifted-SABR parameters calibrated using both our DNNs and the “classic” Hagan et al. approximation and for the three market smiles displayed in fig. [3](https://arxiv.org/html/2510.10343v1#S3.F3 "Figure 3 ‣ 3.3 Volatility Smile Calibration ‣ 3 Numerical Results ‣ Learning the Exact SABR Model").

Furthermore, we show in tab. [14](https://arxiv.org/html/2510.10343v1#A5.T14 "Table 14 ‣ Appendix E Calibration Details ‣ Learning the Exact SABR Model") the numerical results associated with these three smiles. The implied volatility were calculated as discussed in sec. [2.4](https://arxiv.org/html/2510.10343v1#S2.SS4 "2.4 Learning SABR with DNNs ‣ 2 Theoretical Framework ‣ Learning the Exact SABR Model"). In particular, the MC volatility error is defined as the ratio between the MC pricing error (three standard deviations) and the shifted–Black vega sensitivity.

Finally, we show in fig. [10](https://arxiv.org/html/2510.10343v1#A5.F10 "Figure 10 ‣ Appendix E Calibration Details ‣ Learning the Exact SABR Model") the term structure of the calibrated values of the shifted-SABR model parameters. As discussed in sec. [3.3](https://arxiv.org/html/2510.10343v1#S3.SS3 "3.3 Volatility Smile Calibration ‣ 3 Numerical Results ‣ Learning the Exact SABR Model"), to ensure the robustness of the calibration, we repeated the calibration procedure using many random initializations of the SABR parameters and verified that the resulting term structure is stable.
We observe relatively smooth term structures for all the parameters, with no significant discontinuities. This feature is desirable to deal smoothly with Caplets/Floorlets insisting on adjacent forwards.
Interestingly, the term structures obtained by the DNN calibration display richer shapes than those associated with the Hagan et al. approximation, reflecting the ability of the DNN to learn the more complex “exact” SABR implied volatility function.

| Maturity (y) | Methodology | F0F\_{0} | α\alpha | β\beta | ρ\rho | ν\nu | λ\lambda |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.5 | SABR Hagan | 2.28% | 0.0225 | 0.3510 | -0.1232 | 0.8969 | 3% |
| SABR DNN | 2.28% | 0.0214 | 0.3337 | -0.1339 | 0.9074 | 3% |
| 10 | SABR Hagan | 2.66% | 0.0209 | 0.3369 | 0.1572 | 0.2758 | 3% |
| SABR DNN | 2.66% | 0.0122 | 0.1431 | 0.2569 | 0.2841 | 3% |
| 30 | SABR Hagan | 1.56% | 0.0172 | 0.3343 | 0.1262 | 0.1730 | 3% |
| SABR DNN | 1.56% | 0.0077 | 0.0500 | 0.1642 | 0.2155 | 3% |

Table 13: Calibrated SABR parameters θSABR={α,β,ρ,ν}\theta^{\textit{SABR}}=\{\alpha,\beta,\rho,\nu\} using both methodologies for the three market smiles shown in fig. [3](https://arxiv.org/html/2510.10343v1#S3.F3 "Figure 3 ‣ 3.3 Volatility Smile Calibration ‣ 3 Numerical Results ‣ Learning the Exact SABR Model"). The table also reports the (fixed) values for the forward rate F0F\_{0} and the shift λ\lambda.



| Maturity (y) | Strike (K) | DNN | MC\_DNN | Market | MC\_Hagan | Hagan |
| --- | --- | --- | --- | --- | --- | --- |
| 1.5 | -0.015 | 50.78% | 50.80% ±\pm 0.09% | 50.71% | 50.12% ±\pm 0.09% | 51.12% |
| -0.01 | 42.64% | 42.63% ±\pm 0.07% | 42.63% | 42.09% ±\pm 0.07% | 42.64% |
| 0.00 | 30.85% | 30.93% ±\pm 0.04% | 30.87% | 30.58% ±\pm 0.04% | 30.76% |
| 0.005 | 26.30% | 26.43% ±\pm 0.03% | 26.33% | 26.16% ±\pm 0.03% | 26.25% |
| 0.01 | 22.44% | 22.57% ±\pm 0.03% | 22.43% | 22.36% ±\pm 0.02% | 22.41% |
| 0.015 | 19.21% | 19.33% ±\pm 0.02% | 19.20% | 19.19% ±\pm 0.02% | 19.22% |
| 0.02 | 16.85% | 16.92% ±\pm 0.02% | 16.86% | 16.86% ±\pm 0.02% | 16.90% |
| 0.03 | 16.15% | 16.07% ±\pm 0.01% | 16.14% | 16.08% ±\pm 0.01% | 16.11% |
| 0.04 | 18.27% | 18.23% ±\pm 0.01% | 18.29% | 18.24% ±\pm 0.01% | 18.25% |
| 0.05 | 20.62% | 20.60% ±\pm 0.01% | 20.64% | 20.61% ±\pm 0.01% | 20.63% |
| 0.06 | 22.71% | 22.73% ±\pm 0.02% | 22.72% | 22.73% ±\pm 0.02% | 22.77% |
| 0.07 | 24.53% | 24.58% ±\pm 0.03% | 24.51% | 24.57% ±\pm 0.03% | 24.65% |
|  | 0.10 | 28.89% | 28.92% ±\pm 0.06% | 28.66% | 28.90% ±\pm 0.06% | 29.07% |
| 10 | -0.015 | 27.68% | 27.72% ±\pm 0.02% | 27.67% | 26.46% ±\pm 0.02% | 27.78% |
| -0.01 | 24.29% | 24.41% ±\pm 0.02% | 24.27% | 23.42% ±\pm 0.02% | 24.22% |
| 0.0 | 19.73% | 19.93% ±\pm 0.02% | 19.76% | 19.30% ±\pm 0.02% | 19.70% |
| 0.005 | 18.20% | 18.39% ±\pm 0.01% | 18.22% | 17.88% ±\pm 0.01% | 18.19% |
| 0.01 | 17.02% | 17.19% ±\pm 0.01% | 17.03% | 16.76% ±\pm 0.01% | 17.03% |
| 0.015 | 16.16% | 16.29% ±\pm 0.01% | 16.14% | 15.92% ±\pm 0.01% | 16.16% |
| 0.02 | 15.54% | 15.64% ±\pm 0.01% | 15.51% | 15.32% ±\pm 0.01% | 15.54% |
| 0.03 | 14.85% | 14.98% ±\pm 0.01% | 14.85% | 14.69% ±\pm 0.01% | 14.87% |
| 0.04 | 14.72% | 14.84% ±\pm 0.01% | 14.73% | 14.58% ±\pm 0.01% | 14.72% |
| 0.05 | 14.85% | 14.96% ±\pm 0.02% | 14.87% | 14.74% ±\pm 0.02% | 14.85% |
| 0.06 | 15.11% | 15.20% ±\pm 0.02% | 15.12% | 15.02% ±\pm 0.02% | 15.10% |
| 0.07 | 15.41% | 15.47% ±\pm 0.01% | 15.41% | 15.33% ±\pm 0.01% | 15.40% |
|  | 0.10 | 16.28% | 16.29% ±\pm 0.01% | 16.24% | 16.28% ±\pm 0.01% | 16.30% |
| 30 | -0.015 | 22.80% | 22.88% ±\pm 0.01% | 23.03% | 20.44% ±\pm 0.01% | 23.07% |
| -0.01 | 20.41% | 20.55% ±\pm 0.01% | 20.37% | 18.49% ±\pm 0.01% | 20.33% |
| 0.00 | 17.19% | 17.39% ±\pm 0.01% | 17.09% | 15.97% ±\pm 0.01% | 17.07% |
| 0.005 | 16.10% | 16.32% ±\pm 0.01% | 16.06% | 15.14% ±\pm 0.01% | 16.06% |
| 0.01 | 15.31% | 15.49% ±\pm 0.01% | 15.30% | 14.52% ±\pm 0.01% | 15.31% |
| 0.015 | 14.75% | 14.86% ±\pm 0.01% | 14.74% | 14.06% ±\pm 0.01% | 14.75% |
| 0.02 | 14.31% | 14.41% ±\pm 0.01% | 14.33% | 13.73% ±\pm 0.01% | 14.35% |
| 0.03 | 13.79% | 13.86% ±\pm 0.01% | 13.84% | 13.34% ±\pm 0.01% | 13.84% |
| 0.04 | 13.60% | 13.61% ±\pm 0.01% | 13.61% | 13.19% ±\pm 0.01% | 13.60% |
| 0.05 | 13.53% | 13.53% ±\pm 0.01% | 13.53% | 13.15% ±\pm 0.01% | 13.51% |
| 0.06 | 13.51% | 13.54% ±\pm 0.02% | 13.51% | 13.19% ±\pm 0.02% | 13.50% |
| 0.07 | 13.54% | 13.59% ±\pm 0.01% | 13.54% | 13.26% ±\pm 0.02% | 13.53% |
|  | 0.10 | 13.73% | 13.81% ±\pm 0.01% | 13.69% | 13.52% ±\pm 0.01% | 13.72% |

Table 14: Shifted-lognormal implied volatility smiles for the maturities displayed in fig. [3](https://arxiv.org/html/2510.10343v1#S3.F3 "Figure 3 ‣ 3.3 Volatility Smile Calibration ‣ 3 Numerical Results ‣ Learning the Exact SABR Model").



![Refer to caption](Figures/alpha_betacalibrated.png)

(a) α\alpha parameter

![Refer to caption](Figures/beta_betacalibrated.png)

(b) β\beta parameter

![Refer to caption](Figures/rho_betacalibrated.png)

(c) ρ\rho parameter

![Refer to caption](Figures/nu_betacalibrated.png)

(d) ν\nu parameter

Figure 10: Term structures of the four SABR parameters calibrated according to the two methodologies.