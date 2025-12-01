---
authors:
- Aviv Alpern
- Svetlozar Rachev
doc_id: arxiv:2511.21850v1
family_id: arxiv:2511.21850
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Black Litterman and ESG Portfolio OptimizationSubmitted to the editors DATE.
url_abs: http://arxiv.org/abs/2511.21850v1
url_html: https://arxiv.org/html/2511.21850v1
venue: arXiv q-fin
version: 1
year: 2025
---


Aviv Alpern
Bravo Risk Management
().
  
Svetlozar Rachev
Department of Applied Mathematics, Texas Tech University, Lubbock, TX
().

###### Abstract

We introduce a simple portfolio optimization strategy using ESG data with the Black-Litterman allocation framework. ESG scores are used as a bias for Stein shrinkage estimation of equilibrium risk premiums used in assigning Black-Litterman asset weights. Assets are modeled as multivariate affine normal-inverse Gaussian variables using CVaR as a risk measure. This strategy, though very simple, when employed with a soft turnover constraint is exceptionally successful. Portfolios are reallocated daily over a 4.7 year period, each with a different set of hyperparameters used for optimization. The most successful strategies have returns of approximately 40-45% annually.

###### keywords:

Black-Litterman, ESG, SRI, normal-inverse Gaussian, multivariate affine generalized hyperbolic, MAGH, portfolio optimization

## 1 Introduction

Socially responsible investing has become a common topic for research, specifically with interest in its application to asset allocation. Recently, many studies have worked to elucidate the impact of the components of ESG ratings on assets and firms. It’s suggested that positive indicators of these components are linked to reduced risk during periods of potential drawdowns [FM19, NV14, Paul17]. While there is no shortage of literature on the implications of ESG factors on risk and market behavior, we do not present this topic in depth and instead point the reader to Ielasi et al. [ICZ20] for a more comprehensive view. Here, we instead investigate a method for incorporating ESG scores in smart beta portfolio allocation.

A common method of asset allocation familiar to portfolio managers is the Black-Litterman (BL) model for incorporating investor’s market views [BL91]. This allows adjusting expected return of individual assets based on a portfolio manager’s belief of asset returns or relative performance between assets. We blend the BL model with ESG data, allowing both investor views and the ESG factor approach to directly affect the estimated mean of the distribution of portfolio returns. Under the original BL assumptions, the market is modeled using normal distributions which is known to underestimate the probability of unlikely events [Kim11, Mandelbrot63]. For incorporating the BL model views in calculating tail risk measures of elliptically contoured distributions, see Rosella et al. (2007) [stableBL]. Here, we only use BL to model expected returns, while using the normal-inverse Gaussian (NIG) to approximate tail-risk in the form of conditional value-at-risk (CVaR).

In our empirical analysis, we compare the performance of portfolios comprised of different levels of both risk aversion and ESG weighting. Each portfolio is analyzed over a 1175 day testing period (2017-2021), with 4 years of data used for model fitting. The performance is then compared using different reward risk ratios to quantify results.

## 2 Modern Portfolio Theory

### Black-Litterman

111For a in-depth explanation see Meucci (2010) [Meucci10], and , Rachev ST, Hsu JSJ, Bagasheva BS, Fabozzi FJ.Bayesian Methods in Finance [BMF]

For a universe of M assets, we begin by assuming that the observations of asset returns XX follow a normal distribution:

|  |  |  |  |
| --- | --- | --- | --- |
| (1) |  | X∼N​(μ,Σ)X\sim{N}(\mu,\Sigma) |  |

where μ∈ℛM\mu\in\mathcal{R}^{M} and Σ∈ℛM​x​M\Sigma\in\mathcal{R}^{MxM} are the multivariate mean and covariance respectively. It is common to use the sample covariance as an estimate for Σ\Sigma but we use another approach described in a latter section.

The parameters μ{\mu} and Σ{\Sigma} are themselves random variables. Thus, we don’t know their exact values. As suggested by Satchell and Scowcroft [SS2000] it is standard to apply the Bayesian approach of predictive inference and use the informative prior:

|  |  |  |  |
| --- | --- | --- | --- |
| (2) |  | μ∼N​(Π,τ​Σ).\mu\sim{N}(\Pi,\tau\Sigma). |  |

Here, the extra parameters Π\Pi and τ\tau come from the Capital Asset Pricing Model (CAPM). τ\tau represents the uncertainty of the accuracy of the CAPM assumption and Π\Pi is the equilibrium risk premium, defined as:

|  |  |  |  |
| --- | --- | --- | --- |
| (3) |  | Π=δ​Σ​ωe​q.{\Pi=\delta\Sigma\omega\_{eq}}. |  |

δ\delta is a risk aversion parameter, which is the Sharpe ratio divided by the standard deviation, i.e. (RM−Rf)/σ2{(R\_{M}-R\_{f})}/{\sigma^{2}}, the expected asset return and risk free return being denoted by RMR\_{M} and RfR\_{f} respectively. As the name of the model suggests, the equilibrium portfolio weights ωe​q\omega\_{eq} are the relative market capitalization of the portfolio components.

### Market Views

Within this Bayesian framework, it follows that we should allow portfolio managers to input a priori beliefs into the model. These beliefs categorized as relative views: in which we say asset A is expected to outperform asset B by 5% or absolute views: in which we specify the expected return of asset C at the end of the year. For a full explanation and example of inserting market views see Meucci (2010) [Meucci10]. Our views are expressed through transformation of our original random variables μ\mu and Σ\Sigma giving the posterior mean, μ𝐁𝐋\mathbf{\mu\_{BL}}, and covariance matrix, 𝚺𝐁𝐋μ\mathbf{\Sigma\_{BL}^{\mu}}

|  |  |  |  |
| --- | --- | --- | --- |
| (4) |  | μB​L=((τ​Σ)−1+PT​Ω​P)−1​((τ​Σ)−1​π+PT​Ω​v){\mu\_{BL}=((\tau\Sigma)^{-1}+P^{T}\Omega P)^{-1}\hskip 2.84526pt((\tau\Sigma)^{-1}\pi+P^{T}\Omega v)} |  |

|  |  |  |  |
| --- | --- | --- | --- |
| (5) |  | ΣB​Lμ=((τ​Σ)−1+PT​Ω​P)−1{\Sigma\_{BL}^{\mu}=((\tau\Sigma)^{-1}+P^{T}\Omega P)^{-1}} |  |

If we are to write, P = (1, 0; -1, 1), v=(0.05,0)Tv=(0.05,0)^{T}, and Ω\Omega = diag(.0001, .01), then we are expressing that we believe (1) the the return of asset A to be 5% at the end of the year with a relatively high confidence and (2) that asset A and B are expected to have the same return with low confidence. As in any statistical model, the added hyperparameters (τ\tau, P, Ω\Omega, v), are far from trivial to designate which attests to the skill of the portfolio manager to do so.

### Risk Measure: CVaR

Under mean-variance portfolio optimization, we can find a closed-form solution to the portfolio providing the highest Sharpe ratio. In this case we use the above model to pick the portfolio weights that maximize the posterior mean subject to minimizing the risk implied by posterior variance. However, since we instead use CVaR as our risk metric, we use the method outlined by Rockafellar and Uryasev [cvar] defined below.

We start by defining value-at-risk (VaR), i.e. the return that defines the β\beta percentile of the loss function:

|  |  |  |  |
| --- | --- | --- | --- |
| (6) |  | V​a​Rβ=min⁡{A∈ℛ:Ψ​(ω,A)≥β}VaR\_{\beta}=\min\{A\in\mathcal{R}:\Psi(\omega,A)\geq\beta\} |  |

|  |  |  |  |
| --- | --- | --- | --- |
| (7) |  | Ψ​(ω,A)=∫f​(ω,x)≥Ap​(x)​𝑑x\Psi(\omega,A)=\int\_{f(\omega,x)\geq A}p(x)\hskip 2.84526ptdx |  |

Where the loss function, f​(ω,x)f(\omega,x), is the loss of a portfolio composed of asset vector x and weight vector ω\omega. The function Φ​(ω,A)\Phi(\omega,A) is the probability of the loss not exceeding threshold return of A. For a fixed portfolio and thus constant ω\omega, Φ​(ω,x)\Phi(\omega,x) is the cumulative distribution of the portfolio’s returns.

The VaR metric has itself been used to quantify portfolio risk. However, it is not a coherent risk measure [risk\_book] so it’s use is being curtailed in relevant literature. The distinctive property which VaR fails to meet is the subadditivity of risk between two or more assets. It’s possible for the VaR of two assets to be greater than that of the sum of each asset. What we would like is to expect that the hedging the investment reduces risk as opposed to increasing it. For more information on requirement of coherent risk measures see Artzner et al. [coherent\_risk]. The need for a coherent risk metric led to the development of CVaR which we can now define to be:

|  |  |  |  |
| --- | --- | --- | --- |
| (8) |  | C​V​a​Rβ=11−β​∫f​(ω,x)≥V​a​Rβf​(ω,x)​p​(x)​𝑑xCVaR\_{\beta}=\frac{1}{1-\beta}\int\_{f(\omega,x)\geq VaR\_{\beta}}f(\omega,x)\hskip 2.84526ptp(x)\hskip 2.84526ptdx |  |

which is the expected value of the loss of a portfolio when the loss exceeds V​a​RβVaR\_{\beta}.

The evaluation of the above equation can make its optimization nontrivial. However, Rockafellar & Uryasev show that instead we can optimize the function,

|  |  |  |  |
| --- | --- | --- | --- |
| (9) |  | Fβ​(ω,V​a​R)=V​a​R+11−β​∫x∈ℛN[f​(ω,x)−V​a​R]+​p​(x)​𝑑xF\_{\beta}(\omega,VaR)=VaR+\frac{1}{1-\beta}\int\_{x\in\mathcal{R}^{N}}[f(\omega,x)-VaR]^{+}\hskip 2.84526ptp(x)\hskip 2.84526ptdx |  |

with []+[\hskip 2.84526pt]^{+} denoting m​a​x​(0,g)max(0,g) for some function g. The above equation retains the convexity property we need and simplifies the optimization process and returns the global minimum. This result comes from the fact that

|  |  |  |  |
| --- | --- | --- | --- |
| (10) |  | C​V​a​Rβ=min⁡Fβ​(ω,V​a​R).CVaR\_{\beta}=\min F\_{\beta}(\omega,VaR). |  |

The minimization process just outlined leads to the definition of portfolio optimization process shown in [portmax]:

|  |  |  |  |
| --- | --- | --- | --- |
| (11) |  | ω=argmax𝜔​{α​ωT​μ𝐁𝐋−(1−α)​C​V​a​R}\omega=\underset{\omega}{\operatorname\*{argmax}}{\hskip 2.84526pt\{\alpha\hskip 1.99168pt\omega^{T}\hskip 1.99168pt\mathbf{\mu\_{BL}}-(1-\alpha)\hskip 2.84526ptCVaR\}} |  |

The risk aversion parameter, α∈[0,1]\alpha\in[0,1], is used to adjust the weighting of CVaR relative the the expected return. This way, the ability of the investor to assume risk is included in the portfolio choice.

### Risk Modeling: Heavy Tailed Distributions

The loss function,
  
f​(ω,x)f(\omega,x) in Eq ([7](https://arxiv.org/html/2511.21850v1#S2.E7 "Equation 7 ‣ Risk Measure: CVaR ‣ 2 Modern Portfolio Theory ‣ Black Litterman and ESG Portfolio OptimizationSubmitted to the editors DATE.") - [9](https://arxiv.org/html/2511.21850v1#S2.E9 "Equation 9 ‣ Risk Measure: CVaR ‣ 2 Modern Portfolio Theory ‣ Black Litterman and ESG Portfolio OptimizationSubmitted to the editors DATE.")) is dependent on the assumed distribution of asset returns. As discussed earlier, the normal distribution, assumed in the Black-Litterman model, is unable to accurately represent tail risk. To model tail-risk we use the normal-inverse Gaussian (NIG) distribution which has semi-heavy tails. Introduced by Barndorff-Nielsen in 1977 [GH1], the probability density function of NIG is:

|  |  |  |  |
| --- | --- | --- | --- |
| (12) |  | f​(x)=α​δ​𝐊𝟏​(α​δ2+(x−μ)2)π​δ2+(x−μ)2​e[δ​α2+β2+β​(x−μ)]f(x)=\frac{\alpha\delta\mathbf{K\_{1}}(\alpha\sqrt{\delta^{2}+(x-\mu)^{2}})}{\pi\sqrt{\delta^{2}+(x-\mu)^{2}}}e^{[\delta\sqrt{\alpha^{2}+\beta^{2}}+\beta(x-\mu)]} |  |

with parameters denoting

* α\alpha = tail-heaviness
* β\beta = asymmetry
* δ\delta = scale
* μ\mu = location

and 𝐊𝟏\mathbf{K\_{1}} representing the modified Bessel-function of the third kind. While the original paper gives the superclass of NIG, the class of generalized hyperbolic distributions, the special case of NIG is closed under convolution [GH2] making it useful for derivative pricing [magh3].

For the ease of fitting the distribution, we instead use a modification on the generalized hyperbolic distribution, namely the multivariate affine generalized hyperbolic (MAGH) distribution [MAGH1] with the process outlined by Fajardo & Farias [MAGH2]. Although, we specifically use the subclass multivariate affine NIG, we will continue to refer to this as MAGH. A multivariate random variable 𝐗∈ℛM\mathbf{X}\in\mathcal{R}^{M} is a MAGH random variable if

|  |  |  |  |
| --- | --- | --- | --- |
| (13) |  | 𝐗=𝐝𝐀𝐘+𝐦\mathbf{X\stackrel{{\scriptstyle d}}{{=}}AY+m} |  |

where 𝐘∈ℛM\mathbf{Y}\in\mathcal{R}^{M} is a vector of univariate generalized hyperbolic random variables, 𝐀∈ℛM×M\mathbf{A}\in\mathcal{R}^{M\times M} is a decomposition of a the covariance matrix 𝚺\mathbf{\Sigma} s.t. 𝐀𝐀𝐓=𝚺\mathbf{AA^{T}=\Sigma} and 𝐦∈ℛM\mathbf{m}\in\mathcal{R}^{M}. Note that 𝐘\mathbf{Y} itself is not a generalized hyperbolic distributed variable.

Now we have the required definitions and notation to describe our method of computing the optimal portfolio.

## 3 Methods

For a matrix of N observation of M assets, 𝐗∈ℛN×M\mathbf{X}\in\mathcal{R}^{N\times M} we weight the returns such that the i-th column of 𝐗\mathbf{X} is weighted as so:

|  |  |  |  |
| --- | --- | --- | --- |
| (14) |  | 𝐖𝐢=(1−λ)​𝐗𝐢+λ​ξi\mathbf{W\_{i}}=(1-\lambda)\mathbf{X\_{i}}+\lambda\xi\_{i} |  |

with the ESG score of the i-th asset denoted as ξi\xi\_{i}. This, in effect, gives the Stein shrinkage of the mean using ESG scores as the bias:

|  |  |  |  |
| --- | --- | --- | --- |
| (15) |  | mi=(1−λ)​μi+λ​ξim\_{i}=(1-\lambda)\mu\_{i}+\lambda\xi\_{i} |  |

where m is the expected mean of returns.

The transformation of the correlated data 𝐗\mathbf{X} onto the set of uncorrelated variables is achieved via the Cholesky decomposition of the sample covariance matrix. Writing the Cholesky decomposition of 𝚺\mathbf{\Sigma} as 𝐑\mathbf{R} s.t. 𝐑𝐓​𝐑=𝚺\mathbf{R^{T}R=\Sigma}, we get the relation

|  |  |  |  |
| --- | --- | --- | --- |
| (16) |  | 𝐁=C​h​o​l​(C​o​v​(𝐖))=(1−λ)​𝐑\mathbf{B}=Chol(Cov(\mathbf{W}))=(1-\lambda)\mathbf{R}\vskip-5.69054pt |  |

leading to

|  |  |  |  |
| --- | --- | --- | --- |
| (17) |  | 𝐲=(𝐰𝐁−𝟏−𝐦)​𝐃−𝟏𝐲=(𝐰𝐑−𝟏​11−λ−[(1−λ)​𝝁+λ​𝝃])​𝐃−𝟏\begin{split}\mathbf{y}&=\mathbf{(wB^{-1}-m)D^{-1}}\\ \mathbf{y}&=(\mathbf{wR^{-1}}\frac{1}{1-\lambda}-[(1-\lambda)\boldsymbol{\mu}+\lambda\hskip 1.42262pt\boldsymbol{\xi}])\mathbf{D^{-1}}\end{split} |  |

The matrix 𝐃\mathbf{D} is a diagonal matrix of the scale variables, δ\delta, of the marginal NIG distributions. Likewise, 𝝁\boldsymbol{\mu} is a row vector containing the location parameters of the marginals. The lower case representation, 𝐰∈ℛ1×M\mathbf{w}\in\mathcal{R}^{1\times M}, is to denote the M-dimensional random variable as opposed to the matrix of observations. The new variable introduced here, 𝐲∈ℛ1×M\mathbf{y}\in\mathcal{R}^{1\times M}, is a random vector where every variable has mean {0→\vec{0}} and diagonalized covariance matrix.

To calculate the marginal parameters μ\mu and δ\delta at time tt we use the autoregression model ARMA(1,1)-GARCH(1,1) [GARCH]:

|  |  |  |  |
| --- | --- | --- | --- |
| (18a) |  | 𝐗t=p+ϕ​𝐗t−1+θ​ϵt−1+ϵt\mathbf{X}\_{t}=p+\phi\hskip 1.42262pt\mathbf{X}\_{t-1}+\theta\hskip 1.42262pt\epsilon\_{t-1}+\epsilon\_{t} |  |
| (18b) |  | σt2=q+ϕ​ϵt−12+γ​σt−12\sigma^{2}\_{t}=q+\phi\hskip 1.42262pt\epsilon^{2}\_{t-1}+\gamma\hskip 1.42262pt\sigma^{2}\_{t-1} |  |

where the ϵ\epsilon is a error term at time tt, and μt=𝐗𝐭−ϵt\mu\_{t}=\mathbf{X\_{t}}-\epsilon\_{t}. The parameters of the model are fit using MLE under the assumption that the innovation series, ϵt\epsilon\_{t}, has a standard normal distribution. These models have shown to be successful proxies for calculating portfolio risk when used with a multitude of distributional assumptions on the innovations [kim16, kim2020portfolio, Kim11]. The consequence of using the autoregressive model, beyond capturing autocorrelation and volatility clustering in the data, is that we need only fit the NIG parameters α\alpha and β\beta on the innovations.

This process is used to calculated the portfolio CVaR, where the weighted probability densities supplies our loss function introduced in Eq ([7](https://arxiv.org/html/2511.21850v1#S2.E7 "Equation 7 ‣ Risk Measure: CVaR ‣ 2 Modern Portfolio Theory ‣ Black Litterman and ESG Portfolio OptimizationSubmitted to the editors DATE.")). It should be noted that NIG is only closed under convolution if the distributions being convolved have the same α\alpha and β\beta, which is not the case. The ’mixing’ of the random vector, 𝐲\mathbf{y}, by matrix 𝐁\mathbf{B} in Eq ([17](https://arxiv.org/html/2511.21850v1#S3.E17 "Equation 17 ‣ 3 Methods ‣ Black Litterman and ESG Portfolio OptimizationSubmitted to the editors DATE.")) leads to this the convolution. Therefore, there is no closed form solution to the distribution of 𝐰\mathbf{w} or the predicted distribution of returns ωT​𝐰\omega^{T}\mathbf{w}. Instead, we can approximate the distribution through properly scaling and mixing samples taken from, 𝐲\mathbf{y}. With this approximation, the objective function in Eq ([9](https://arxiv.org/html/2511.21850v1#S2.E9 "Equation 9 ‣ Risk Measure: CVaR ‣ 2 Modern Portfolio Theory ‣ Black Litterman and ESG Portfolio OptimizationSubmitted to the editors DATE.")) for a sample of qq observations becomes

|  |  |  |  |
| --- | --- | --- | --- |
| (19) |  | Fβ​(ω,V​a​Rβ)≈V​a​Rβ+1q​(1−β)​∑j=1q[ωT​𝐰j−V​a​rβ]+F\_{\beta}(\omega,VaR\_{\beta})\approx VaR\_{\beta}+\frac{1}{q(1-\beta)}\sum\_{j=1}^{q}[\omega^{T}\mathbf{w}\_{j}-Var\_{\beta}]^{+} |  |

where 𝐰j\mathbf{w}\_{j} is the transformation of the j-th observation of 𝐲\mathbf{y} as defined in Eq ([17](https://arxiv.org/html/2511.21850v1#S3.E17 "Equation 17 ‣ 3 Methods ‣ Black Litterman and ESG Portfolio OptimizationSubmitted to the editors DATE.")) [cvar].

We consider portfolios allocated from two different approaches: the standard mean-CVaR optimization and the Black Litterman 𝝁𝑩​𝑳\boldsymbol{\mu\_{BL}}-CVaR optimization. Instead of using the market capitalization from CAPM to weight our assets, we instead use the current Dow Jones composition weights of each asset. In this way the method for determining 𝝎e​q\boldsymbol{\omega}\_{eq} is similar to Eq ([14](https://arxiv.org/html/2511.21850v1#S3.E14 "Equation 14 ‣ 3 Methods ‣ Black Litterman and ESG Portfolio OptimizationSubmitted to the editors DATE.")):

|  |  |  |  |
| --- | --- | --- | --- |
| (20) |  | ωξ,i=ξi∑j=1MξjωC,i=Ci∑j=1MCj\omega\_{\xi,i}=\frac{\xi\_{i}}{\sum\_{j=1}^{M}\xi\_{j}}\hskip 25.60747pt\omega\_{C,i}=\frac{C\_{i}}{\sum\_{j=1}^{M}C\_{j}} |  |

|  |  |  |  |
| --- | --- | --- | --- |
| (21) |  | ωe​q,i=(1−λ)​ωC,i+λξ,i\omega\_{eq,i}=(1-\lambda)\omega\_{C,i}+\lambda\_{\xi,i} |  |

letting CiC\_{i} and ωe​q,i\omega\_{eq,i} be the Dow Jones weight and equilibrium weight for the i-th asset respectively.

At time t, we choose our portfolios weights to maximize:

|  |  |  |  |
| --- | --- | --- | --- |
| (22) |  | ωt=argmax𝜔​{α​ωT​Rt−(1−α)​C​V​a​Rt−ρ||ωt−ωt−1||1}\omega\_{t}=\underset{\omega}{\operatorname\*{argmax}}{\{\hskip 2.84526pt\alpha\hskip 1.99168pt\omega^{T}R\_{t}-(1-\alpha)CVaR\_{t}-\rho\hskip 1.99168pt\mathbf{||}\omega\_{t}-\omega\_{t-1}\mathbf{||}\_{1}\}} |  |

Here, RtR\_{t} is the predicted return of our assets at time t, and CVaR is calculated at the given level β\beta and induced by the weight vector ω\omega. The last term on the right hand side is a soft turnover constraint, ρ\rho, denoting the turnover penalty and ||⋅||1||\cdot||\_{1} being the L1L\_{1} vector norm.

The hyperparameters from Eq ([21](https://arxiv.org/html/2511.21850v1#S3.E21 "Equation 21 ‣ 3 Methods ‣ Black Litterman and ESG Portfolio OptimizationSubmitted to the editors DATE.") & [22](https://arxiv.org/html/2511.21850v1#S3.E22 "Equation 22 ‣ 3 Methods ‣ Black Litterman and ESG Portfolio OptimizationSubmitted to the editors DATE.")) that we test for our portfolios construction are λ=[0,0.25,0.5,0.7]\lambda=[0,0.25,0.5,0.7], α=0:0.1:1\alpha=0:0.1:1, and ρ=[5,10,15,20,30,40]×10−4\rho=[5,10,15,20,30,40]\times 10^{-4} with CVaR calculated at 95% and 99%.

## 4 Results

In total, we present results for 616 portfolio strategies. As the related figures and performance metrics are somewhat substantial, we introduce results and the relating discussion together to avoid an otherwise unclear presentation of disparate information. We leave the more general discussion of the findings to the later section.

### 4.1 Data

For our analysis we use daily Bloomberg data of the Dow Jones 30 between Jan 3, 2013 and Sep 3, 2021. However, of those 30, we only had data for 29. The asset missing from the data set was Dow Inc (DOW). The ESG data is yearly quotes from Robeco, released on the last trading day in December each year over the period from 2016 to 2020. The data set lacks ESG scores for Walt Disney (DIS) before 2019. Consequently DIS is not included in the portfolio for years without ESG data. Our benchmark is thusly an adjusted DJ index using it’s current asset weights, re-normalized so they add to 1 on the remaining 28 asset for the entire period. It should be noted that removing DIS and DOW from the benchmark severely increased it’s performance over the period, seeing that these two companies have been amongst the lowest earners of the DJ 30 in the last 5 years. For fitting our model we use a window size of 1007 returns over a period of 1175 days with our first asset return prediction on Jan 3, 2017. The initial portfolio weights for each strategy is composed of the weights defined in Eq ([21](https://arxiv.org/html/2511.21850v1#S3.E21 "Equation 21 ‣ 3 Methods ‣ Black Litterman and ESG Portfolio OptimizationSubmitted to the editors DATE.")).

To assess each portfolio strategy we use reward-risk ratios (RRR) listed in Cheridito & Kromer (2013) [RRR]. We utilize the Sortino, Gini, and STARR ratios which the display the four properties of monotonicity (M), quasi-concavity (Q), scale invariance (S), and distribution dependency (D) presented in the original paper. All reward-risk ratios are calculated using empirical distributions over the same window size used in training the model, stated above. While this can be sufficient to capture the behavior of the strategy of the period as a whole, to observe sensitivity to short-term market fluctuations would require using the parametric distribution for the predicted daily return. This, however, will be the subject of another paper allowing a more comprehensive evaluation of the performance of the model during different market periods.

### 4.2 Computational Results

The focus of this investigation is to introduce and assess a basic framework for using the Black-Litterman (BL) approach on an asset class with ESG data. Of course, the BL method is tailored for incorporating a portfolio managers views on the market, views that would be proprietary if even moderately successfully. We do not attempt to express market views and instead only present the basic structure of BL on top of CAPM. In this way, we have a simple bias for shrinkage estimation of mean returns. Even without imposing market views, the BL model outperforms the benchmark.

The performance metrics for each portfolios strategy with CVaR95 are shown in Table 2A. The standard mean-CVaR approach shown in Fig.[1](https://arxiv.org/html/2511.21850v1#A0.F1 "Figure 1 ‣ 5 Discussion ‣ Black Litterman and ESG Portfolio OptimizationSubmitted to the editors DATE.") and Table [2A](https://arxiv.org/html/2511.21850v1#A0.F2 "Figure 2A ‣ 5 Discussion ‣ Black Litterman and ESG Portfolio OptimizationSubmitted to the editors DATE.") was unsuccessful compared to the benchmark, having substantially lower returns and RRR. Strategies that had large ESG weights and α\alpha, specifically {λ=0.25,α≥0.9\lambda=0.25,\hskip 2.27621pt\alpha\geq 0.9}, {λ=0.5,α≥0.8\lambda=0.5,\hskip 2.27621pt\alpha\geq 0.8}, and {λ=0.75,α≥0.5\lambda=0.75,\hskip 2.27621pt\alpha\geq 0.5}, do not rebalance their portfolios at any time step. These strategies have the best performance out of all standard mean-CVaR approaches and slightly under perform the benchmark in both return and RRR. The relative success of these inert portfolios displays the utility of both the CAPM and ESG together.

For mean-CVaR portfolios with nonzero turnover, the degree of yearly turnover is associated with lower risk and lower reward. Portfolios with {λ=0,α≤0.5\lambda=0,\alpha\leq 0.5} and {λ=0.25,α≤0.4\lambda=0.25,\alpha\leq 0.4} have the lowest drawdowns of all employed strategies. However, the comparatively meager annual returns of 15-20% result in low RRR. Among these strategies, increased turnover is directly associated with lower returns. This is typical, as CVaR is sensitive to the data used in fitting. Moreover, the convergence of the distribution is dependent on the tails, converging asymptotically slower for heavier tails [CVaR\_sensitivity].

In contrast to the acceptable level of turnover observed for standard mean-CVaR portfolios with ρ=5×10−4\rho=5\times 10^{-4}, a majority of CVaR95 BL portfolios with the same constraint had excessive turnovers that made the strategies infeasible. The high turnover is a consequence of the overestimation of returns by the BL model leading to over-sensitivity of the optimal portfolio found in Eq ([22](https://arxiv.org/html/2511.21850v1#S3.E22 "Equation 22 ‣ 3 Methods ‣ Black Litterman and ESG Portfolio OptimizationSubmitted to the editors DATE.")) to the the conditional mean from ARMA [18a](https://arxiv.org/html/2511.21850v1#S3.E18.1 "Equation 18a ‣ Equation 18 ‣ 3 Methods ‣ Black Litterman and ESG Portfolio OptimizationSubmitted to the editors DATE."). Similar to the results in the mean-CVaR case, small α\alpha and large λ\lambda curtailed the excess turnover. However, the portfolios that had acceptable annual turnover ≤3\leq 3 still fail to approach the benchmark, the best of which having an annual return of ≈27%\approx 27\%. Generally this would be more than acceptable returns, although the benchmark returned over 31% annually and had higher RRR. The success of the benchmark can be attributed, at least in part, to the accommodating fed policy following the COVID related market crash of march 2020.

The sensitivity of the BL model could be remedied by adjusting the risk-aversion parameter from Eq ([3](https://arxiv.org/html/2511.21850v1#S2.E3 "Equation 3 ‣ Black-Litterman ‣ 2 Modern Portfolio Theory ‣ Black Litterman and ESG Portfolio OptimizationSubmitted to the editors DATE.")), however, we simply increase the turnover constraint. Of the BL strategies that had acceptable turnover, the largest portfolios returns were between 40-45% annually. These portfolios had high RRRs equal to or greater than the benchmark. These strategies worth noting are labeled and plotted against the benchmark in Fig. [1](https://arxiv.org/html/2511.21850v1#A0.F1 "Figure 1 ‣ 5 Discussion ‣ Black Litterman and ESG Portfolio OptimizationSubmitted to the editors DATE.").

The results for CVaR99 are listed in Tables 3A-3G. The performance compared with CVar95 was subpar. Strategies that had acceptable turnover rarely approach the benchmark. Many of the strategies that do, analogous to the CVaR95 case, have zero turnover. All zero-turnover strategies have performance metrics slightly below the benchmark. The highest performing portfolios are plotted in Fig. [1](https://arxiv.org/html/2511.21850v1#A0.F1 "Figure 1 ‣ 5 Discussion ‣ Black Litterman and ESG Portfolio OptimizationSubmitted to the editors DATE."). Across all CVaR99 portfolios, the RRR and drawdown ratio is not significantly higher than that of CVaR95. Points on the tail of a distribution become more sensitive to the observed window of data the distance from the mean increases [CVaR\_sensitivity]. Thus it can be hard to hedge against daily fat tailed risk for large percentiles. Consequently, the difficulty of the CVaR minimization problem can be exacerbated by illiquidity. Much of the utility of CVaR as a risk metric is to estimate the amount of cash required in a margin account to prevent a margin call.

## 5 Discussion

Our Black-Litterman ESG model performs exceptionally well compared to our benchmark, or any well-known composite indexes. Of course, we tested the model with many combinations of hyperparameters. It would be appropriate to cross validate the performance with an out-of-sample data set. However the ESG data for Robeco only goes back to the Dec 30, 2016, so there is not sufficient data to analyze the performance over. Additionally, the characteristics of the market over past 3 years have been very unique. Observing model behavior over only a small subset would be largely subject to the characteristics of the period.

One of the aforementioned properties of ESG strategies is the reduction of systematic risk during bear markets. We do not directly observe this. During the period of data used, we observe the market before, during, and after the 2020 COVID-19 market crash. As the crash is not an extended period of economic recession, the empirical reward-risk ratios calculated over 4 years is not sensitive enough express the behavior over the rather brief duration. Thus we do not observe any significant under or overperformance. This would be specific to the standard mean-CVaR as the performance of the BL ESG model would be highly sensitive to the views expressed, and thus the views should reflect the market at the given time. In our model, ESG ratings do not directly affect the tail risk of the distribution of predicted returns 222For more information on using views to get get a posterior estimate for CVaR see Giacometti et al. (2007) [stableBL]. Moreover, both the CAPM and ESG weights included in BL model are expressed on a yearly basis. Accordingly, during the relatively longer bull market period before and after the 2020 crash the BL ESG model clearly performs well above the benchmark as seen in Fig. [1](https://arxiv.org/html/2511.21850v1#A0.F1 "Figure 1 ‣ 5 Discussion ‣ Black Litterman and ESG Portfolio OptimizationSubmitted to the editors DATE.").

It would be of interest to examine the affects of different political events of the past 5 years on ESG based portfolios. Specifically the time period surrounding the UN climate change conferences and the change of presidential administration in the US. The Trump administration, in particular, had a large affect on the environmental policy in the country. One might expect that the performance of high ESG assets may change as a result of related legislation. This may be of greater scrutiny in later studies.

Additionally, the ESG data used here is yearly. Monthly data exists but is not in our data set. In both cases, the amount of data is relatively small. Giving an estimate for a prediction or uncertainty of such a time series can be nontrivial. Furthermore, the factors that feed into the ESG score provided by each data source are opaque. It may be of use to have a Black-Litterman type model applied to the expectation of ESG. A portfolio manager could then express their views as a result of external information and the certainty of those views compared to data itself. Thus, the certainty, especially for yearly data, can be changed as the time from data point is increases. Nevertheless, the utility of ESG in portfolio management is significant and current techniques would benefit from further research.

Appendix

![Refer to caption](horserace/comparative_horserace.jpg)

Fig. 1: Comparative plots of the best performing portfolios.



|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Total Return | Annual Return | Sharpe | Sortino | Gini | STARR | DDR |
| 1.4864 | 0.3187 | 0.0743 | 0.1057 | 0.1057 | 0.0288 | 4.538 |

  


Table 1: Performance metrics of the DJ 28 benchmark.




Table 2A: Tables 2A-2G display performance metrics of each portfolio strategy using CVaR95. In Table 1A the row label ’std’ denotes the standard mean-CVaR method of portfolio optimization as opposed to the BL method. The Sharpe, Sortino, Gini, and STARR ratios are daily averages, the drawdown ratio (DDR) is calculated using the return and max drawdown over the entire period, and the turnovers are yearly averages. The listed ρ\rho in the row labels is on the order of 1×10−41\times 10^{-4}. Color maps for each column, except turnovers, are a linear gradient between the min and max of each column across all rows of tables 1A-1G, yellow being the max. For turnovers, the color map is inverted and linear between 0 and 10, 0 being yellow and entries ≥\geq 10 being purple. The color map for all plots is shown beside figure 2A.

![Refer to caption](x1.png)
![Refer to caption](x2.png)


Table 2b:

![Refer to caption](x3.png)


Table 2c:

![Refer to caption](x4.png)


Table 2d:

![Refer to caption](x5.png)


Table 2e:

![Refer to caption](x6.png)


Table 2f:

![Refer to caption](x7.png)


Table 2g:




Table 3a: Tables 3A-3G display performance metrics of each portfolio strategy using CVaR99. Similar to the above tables linear gradients display the max and min of a column across the rows of all tables. The gradient for turnovers is in the same fashion as describe in Table 2A.

![Refer to caption](x8.png)


Table 3a:

![Refer to caption](x9.png)


Table 3b:

![Refer to caption](x10.png)


Table 3c:

![Refer to caption](x11.png)


Table 3d:

![Refer to caption](x12.png)


Table 3e:

![Refer to caption](x13.png)


Table 3f:

![Refer to caption](x14.png)


Table 3g: