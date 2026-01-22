---
authors:
- Tjeerd De Vries
doc_id: arxiv:2601.14852v1
family_id: arxiv:2601.14852
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation'
url_abs: http://arxiv.org/abs/2601.14852v1
url_html: https://arxiv.org/html/2601.14852v1
venue: arXiv q-fin
version: 1
year: 2026
---


Tjeerd De Vries
Department of Finance, HEC Paris. Email: [de-vries@hec.fr](mailto:de-vries@hec.fr). I thank Nikolay Kudrin, Evgenii Vladimirov, participants of the HEC Brownbag seminar, and especially Irina Zviadadze for helpful feedback.

###### Abstract

We propose a projection method to estimate risk-neutral moments from option prices. We derive a finite-sample bound implying that the projection estimator attains (up to a constant) the smallest pricing error within the span of traded option payoffs. This finite-sample optimality is not available for the widely used Carr–Madan approximation. Simulations show sizable accuracy gains for key quantities such as VIX and SVIX. We then extend the framework to multiple underlyings, deriving necessary and sufficient conditions under which simple options complete the market in higher dimensions, and providing estimators for joint moments. In our empirical application, we recover risk-neutral correlations and joint tail risk from FX options alone, addressing a longstanding measurement problem raised by [[53](https://arxiv.org/html/2601.14852v1#bib.bib68 "Options and efficiency")]. Our joint tail-risk measure predicts future joint currency crashes and identifies periods in which currency portfolios are particularly useful for hedging.

## 1 Introduction

Option prices provide real-time, forward-looking information about the state of the economy. Their tractability and informational content have made them central to a wide range of empirical applications, including forecasting the equity premium, predicting volatility, and measuring skewness and higher-order risk-neutral moments.111See, for example, [[7](https://arxiv.org/html/2601.14852v1#bib.bib101 "The crash of ’87: was it expected? evidence from options markets"), [47](https://arxiv.org/html/2601.14852v1#bib.bib67 "What is the expected return on the market?"), [41](https://arxiv.org/html/2601.14852v1#bib.bib83 "The quanto theory of exchange rates"), [55](https://arxiv.org/html/2601.14852v1#bib.bib99 "(Almost) model-free recovery"), [4](https://arxiv.org/html/2601.14852v1#bib.bib125 "Short-term market risks implied by weekly options")] for predicting the equity premium; [[16](https://arxiv.org/html/2601.14852v1#bib.bib86 "Option prices, implied price processes, and stochastic volatility"), [20](https://arxiv.org/html/2601.14852v1#bib.bib66 "Towards a theory of volatility trading"), [21](https://arxiv.org/html/2601.14852v1#bib.bib106 "Variance risk premiums"), [12](https://arxiv.org/html/2601.14852v1#bib.bib107 "Expected stock returns and variance risk premia"), [38](https://arxiv.org/html/2601.14852v1#bib.bib123 "The model-free implied volatility and its information content")] for volatility forecasting; and [[6](https://arxiv.org/html/2601.14852v1#bib.bib103 "Stock return characteristics, skew laws, and the differential pricing of individual equity options"), [22](https://arxiv.org/html/2601.14852v1#bib.bib104 "The conditional expected market return"), [40](https://arxiv.org/html/2601.14852v1#bib.bib105 "The skew risk premium in the equity index market")] for higher-order moment estimation. A widely used approach for extracting such quantities is the method of [[20](https://arxiv.org/html/2601.14852v1#bib.bib66 "Towards a theory of volatility trading")] (henceforth, CM), which expresses the risk-neutral expectation of a twice-differentiable payoff as a weighted integral over put and call prices. Because option prices are observed across a range of strikes on any given day, the integral can be approximated numerically, enabling the practical estimation of objects such as the VIX and other risk-neutral measures.

Given the substantial notional amounts traded in derivatives such as VIX options, accurate measurement of risk-neutral quantities is essential. Measurement error in these quantities can also distort inference about the informational content of option prices and their predictive power for future market outcomes. This paper proposes a new method for estimating risk-neutral quantities that improves significantly on the standard approach. Rather than approximating payoffs using a second-order Taylor expansion around the forward price, as in CM, we project the target payoff function onto the linear span of payoffs from traded instruments—specifically, puts, calls, and the underlying.

The approach generalizes the classical put-call parity identity, which arises from an exact replication of a constant payoff using a portfolio of the underlying, a put, and a call. In our framework, the constant function is just one element of a broader class of payoffs that can be projected onto this same payoff space. For any such projection, the risk-neutral expectation can be computed directly from observed option prices, yielding a tractable, model-free estimator.

This *projection-based approach* offers several advantages over the widely used method of CM. First, it allows for extrapolation beyond the range of observed strike prices, which is particularly important when option quotes do not extend sufficiently into the tails. This allows the researcher to incorporate prior beliefs about the relevant support of the risk-neutral distribution even when strikes are sparse in the tails. Effectively, the observed option payoffs are used to form the best approximation to the target payoff over the chosen domain. Moreover, the resulting estimate corresponds directly to an investable portfolio constructed from traded options, whereas common extensions of the CM formula rely on curve fitting and extrapolation to impute unobserved option prices (e.g., [[38](https://arxiv.org/html/2601.14852v1#bib.bib123 "The model-free implied volatility and its information content")]).

Second, the projection approach enjoys good finite-sample properties. In particular, we derive a bound which implies that the projection-based pricing error is, up to a constant, the smallest attainable among portfolios spanned by the traded option payoffs. An analogous guarantee is not available for the CM approach, even though it uses the same set of observed options. This finite-sample optimality complements our asymptotic results. In an idealized framework, we show that projection and CM converge at the same rate to the true risk-neutral expectation, and under strong assumptions they asymptotically assign the same portfolio weights. These equivalence results break down in realistic settings with irregular strike spacing and limited tail coverage. Simulations illustrate the resulting finite-sample gains, showing that projection yields substantially more accurate estimates of key quantities such as VIX and SVIX. This improvement is particularly relevant in our FX application, where only five strikes are available and quotes do not extend far into the tails.

Third, unlike the CM approach, the projection method can be used to estimate the full risk-neutral distribution. This is central to a large literature on recovering measures of risk aversion and pricing kernels.222See, for example, [[11](https://arxiv.org/html/2601.14852v1#bib.bib77 "Option-implied risk aversion estimates"), [37](https://arxiv.org/html/2601.14852v1#bib.bib72 "Recovering risk aversion from option prices and realized returns"), [2](https://arxiv.org/html/2601.14852v1#bib.bib102 "Nonparametric risk management and implied risk aversion"), [3](https://arxiv.org/html/2601.14852v1#bib.bib127 "Pricing of index options in incomplete markets")] for estimates of risk aversion; and [[36](https://arxiv.org/html/2601.14852v1#bib.bib69 "Recovering probability distributions from option prices"), [52](https://arxiv.org/html/2601.14852v1#bib.bib70 "Empirical pricing kernels"), [54](https://arxiv.org/html/2601.14852v1#bib.bib98 "The recovery theorem"), [53](https://arxiv.org/html/2601.14852v1#bib.bib68 "Options and efficiency"), [15](https://arxiv.org/html/2601.14852v1#bib.bib65 "Prices of state-contingent claims implicit in option prices"), [1](https://arxiv.org/html/2601.14852v1#bib.bib100 "Nonparametric estimation of state-price densities implicit in financial asset prices"), [31](https://arxiv.org/html/2601.14852v1#bib.bib75 "Estimating the implied risk‐neutral density for the us market portfolio"), [32](https://arxiv.org/html/2601.14852v1#bib.bib76 "Risk-neutral densities: a review"), [14](https://arxiv.org/html/2601.14852v1#bib.bib78 "Estimation of risk-neutral densities using positive convolution approximation"), [33](https://arxiv.org/html/2601.14852v1#bib.bib74 "Density approximations for multivariate affine jump-diffusion processes"), [45](https://arxiv.org/html/2601.14852v1#bib.bib73 "Pricing kernel monotonicity and conditional information"), [8](https://arxiv.org/html/2601.14852v1#bib.bib71 "An empirical test of pricing kernel monotonicity")] for estimates of the pricing kernel or risk-neutral density. Our estimator satisfies a key internal consistency condition: it exactly reproduces the observed option prices. This is not guaranteed by most existing approaches. Furthermore, unlike the classical method of [[15](https://arxiv.org/html/2601.14852v1#bib.bib65 "Prices of state-contingent claims implicit in option prices")], our approach does not require numerical differentiation of the option price surface. This is an important advantage, as estimating second derivatives is often unstable in practice due to the irregular spacing of strike prices.

Fourth, projection generalizes to higher dimensions. Prior work shows that options on individual stocks cannot pin down joint risk-neutral expectations [[48](https://arxiv.org/html/2601.14852v1#bib.bib84 "Options and the gamma knife"), [49](https://arxiv.org/html/2601.14852v1#bib.bib92 "Information in derivatives markets: forecasting prices with prices")]. We formalize this in Proposition [8](https://arxiv.org/html/2601.14852v1#Thmprop8 "Proposition 8 (Zero correlation). ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"), which proves the impossibility of identifying correlation from single-name options alone. To overcome this, we incorporate information from index options, which embed constraints on the joint distribution of the constituents’ returns.

In this more complicated setting, we derive necessary and sufficient conditions under which simple options complete the market for the payoff class we study. The key step is an equivalence: market completeness obtains precisely when ridge functions x→g​(w′​x)x\to g(w^{\prime}x) are dense in the uniform topology, and the latter question is well studied in approximation theory [[51](https://arxiv.org/html/2601.14852v1#bib.bib112 "Ridge functions"), e.g.,]. Ridge representations are also familiar in econometrics through projection pursuit [[34](https://arxiv.org/html/2601.14852v1#bib.bib119 "Projection pursuit regression")]: the difference here is that the directions ww are fixed by portfolio weights, whereas projection pursuit also optimizes over ww.

The density result for ridge functions (Theorem [2](https://arxiv.org/html/2601.14852v1#Thmthm2 "Theorem 2. ‣ 4.1 Identifying joint dependence from options on multiple portfolios ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) requires observations on infinitely many distinct portfolio options, or equivalently, an unbounded set of portfolio weights ww. In practice only a finite collection is observed. For example, options on the SPDR ETF together with its 11 sector funds yield 12 distinct weights {wj}j=112\left\{{w\_{j}}\right\}\_{j=1}^{12}. Estimating correlations or other measures of joint dependence therefore becomes an inverse problem: we seek to recover those quantities from the finite set of portfolio returns, i.e. from line projections in ℝd\mathbb{R}^{d}. Closely related problems arise in tomography and compressed sensing, where functionals of a distribution are reconstructed from line integrals [[18](https://arxiv.org/html/2601.14852v1#bib.bib120 "Robust uncertainty principles: exact signal reconstruction from highly incomplete frequency information"), e.g.,].

Despite the finite menu of portfolios, projection yields informative estimates of joint risk-neutral moments. We demonstrate this with the 11 SPDR sector ETFs, estimating the risk-neutral correlation matrix across sectors. To maximize information, we also use options on the value-weighted S&P500 and on an equally weighted sector portfolio; both are linear combinations of the sectors and thus provide additional information. The resulting projection estimator nests the CBOE Implied Correlation Index as the special case with equicorrelation (all pairwise correlations equal). In Monte Carlo simulation, the estimator attains lower mean-squared error than the Implied Correlation Index.

We also consider joint dependence estimation in FX returns, focusing on EUR/USD and GBP/USD. This setting is particularly clean because triangular parity introduces a traded cross rate, EUR/GBP, satisfying SEUR/GBP=SEUR/USD/SGBP/USDS\_{\text{EUR/GBP}}=S\_{\text{EUR/USD}}/S\_{\text{GBP/USD}}. Options on the cross therefore contain information about the joint risk-neutral distribution of the two leg returns. While we show that vanilla options do not complete the market for the two legs, our projection approach nevertheless recovers option-implied correlations with very high accuracy in simulations and allows accurate estimation of joint probabilities, addressing a longstanding measurement problem for return dependence.333See, for example, [[53](https://arxiv.org/html/2601.14852v1#bib.bib68 "Options and efficiency"), [48](https://arxiv.org/html/2601.14852v1#bib.bib84 "Options and the gamma knife"), [49](https://arxiv.org/html/2601.14852v1#bib.bib92 "Information in derivatives markets: forecasting prices with prices"), [13](https://arxiv.org/html/2601.14852v1#bib.bib121 "Option-implied dependence and correlation risk premium")] on estimating joint risk-neutral probabilities. These estimates can be used, for instance, to infer the option-implied variance of currency portfolios and to calibrate empirical models of joint currency risk (e.g., [[23](https://arxiv.org/html/2601.14852v1#bib.bib124 "Crash risk in currency returns")]).

Particular care is required when constructing portfolios that replicate joint-dependence measures because options on the cross rate are quoted in GBP, whereas options on the two dollar rates are quoted in USD. Valuing all payoffs under a common (USD) numéraire introduces a state-dependent conversion term, namely the pricing kernel that converts GBP-denominated payoffs into USD units. Our projection approach incorporates this numéraire-change term directly, yielding a portfolio that is fully implementable for a U.S. investor. This contrasts with existing approaches in the FX literature which effectively treat the conversion kernel as constant (e.g., [[50](https://arxiv.org/html/2601.14852v1#bib.bib126 "International correlation risk")]).

We estimate the forward-looking (risk-neutral) correlation between EUR/USD and GBP/USD to average about 0.7 over the sample, with pronounced time variation. The correlation reaches a local minimum around the June 2016 Brexit vote, near 0.2. A variance decomposition indicates that this decline is largely accounted for by a spike in the volatility of GBP/USD, with little contemporaneous change in EUR/USD volatility. We also estimate the risk-neutral probability that both monthly returns fall by at least 3%. This measure forecasts subsequent downside outcomes: in a predictive regression, its coefficient is statistically significant in-sample. Reduced-form evidence points to state dependence in risk compensation. In tranquil periods, the joint crash probability under the risk-neutral measure is below its physical counterpart, consistent with option portfolios providing hedge-like payoffs. During stress episodes (e.g., the 2008 financial crisis), the ordering reverses, implying higher compensation required for exposure to joint crash risk.

The rest of this paper is structured as follows. Section [2](https://arxiv.org/html/2601.14852v1#S2 "2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") reviews the CM approach and introduces the projection method. Section [3](https://arxiv.org/html/2601.14852v1#S3 "3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") derives the convergence properties of the projection approach and establishes an equivalence with risk-neutral density estimation. Section [4](https://arxiv.org/html/2601.14852v1#S4 "4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") extends the projection method to higher dimensions and shows how joint risk-neutral moments can be estimated. Section [5](https://arxiv.org/html/2601.14852v1#S5 "5 Simulation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") presents evidence on the finite-sample performance using Monte Carlo simulation, and Section [6](https://arxiv.org/html/2601.14852v1#S6 "6 Empirical application ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") presents the main empirical findings. Finally, Section [7](https://arxiv.org/html/2601.14852v1#S7 "7 Conclusion ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") concludes.

## 2 Estimating nonlinear payoffs using projection

In this section, we introduce the projection method to estimate risk-neutral moments. We first review [[20](https://arxiv.org/html/2601.14852v1#bib.bib66 "Towards a theory of volatility trading")] to benchmark our approach.

### 2.1 Carr-Madan approach

Let g​(ST)g(S\_{T}) denote a payoff at maturity TT as a function of the realized stock price STS\_{T}. Our object of interest is the conditional risk-neutral expectation 𝐄tQ​[g​(ST)]\mathbf{E}\_{t}^{Q}[g(S\_{T})]. The CM approach constructs a portfolio of puts and calls that replicates g​(ST)g(S\_{T}) state by state. By the law of one price, 𝐄tQ​[g​(ST)]\mathbf{E}\_{t}^{Q}[g(S\_{T})] equals the time-tt value of this replicating portfolio, which can be computed from observed option prices.

To implement this idea, CM start from a second-order Taylor expansion with integral remainder,

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(ST)\displaystyle g(S\_{T}) | =g​(Ft→T)+g′​(Ft→T)​(ST−Ft→T)\displaystyle=g(F\_{t\to T})+g^{\prime}(F\_{t\to T})(S\_{T}-F\_{t\to T}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +∫0Ft→Tg′′​(K)​(K−ST)+​d​K+∫Ft→T∞g′′​(K)​(ST−K)+​d​K,\displaystyle+\int\_{0}^{F\_{t\to T}}g^{\prime\prime}(K)\left(K-S\_{T}\right)^{+}\mathop{}\!\mathrm{d}K+\int\_{F\_{t\to T}}^{\infty}g^{\prime\prime}(K)\left(S\_{T}-K\right)^{+}\mathop{}\!\mathrm{d}K, |  | (1) |

where Ft→TF\_{t\to T} is the time-tt forward price for maturity TT. Using risk-neutral valuation, we obtain

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐄tQ​g​(ST)=g​(Ft→T)+Rf,t→T​∫0Ft→Tg′′​(K)​Pt→T​(K)​d​K+Rf,t→T​∫Ft→T∞g′′​(K)​Ct→T​(K)​d​K,\mathbf{E}\_{t}^{Q}g(S\_{T})=g(F\_{t\to T})+R\_{f,t\to T}\int\_{0}^{F\_{t\to T}}g^{\prime\prime}(K)P\_{t\to T}(K)\mathop{}\!\mathrm{d}K+R\_{f,t\to T}\int\_{F\_{t\to T}}^{\infty}g^{\prime\prime}(K)C\_{t\to T}(K)\mathop{}\!\mathrm{d}K, |  | (2) |

where Rf,t→TR\_{f,t\to T} is the gross risk-free rate from tt to TT, and Pt→T​(K)P\_{t\to T}(K) and Ct→T​(K)C\_{t\to T}(K) denote European put and call option prices with strike KK and maturity TT.

In practice, option prices are observed only at a discrete set of strikes, so the integrals in ([2](https://arxiv.org/html/2601.14852v1#S2.E2 "In 2.1 Carr-Madan approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) are approximated by a trapezoidal rule. For example, for observed put strikes K0<⋯<KJ≤Ft→TK\_{0}<\cdots<K\_{J}\leq F\_{t\to T},

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ∫0Ft→Tg′′​(K)​Pt→T​(K)​d​K≈∑j=0Jg′′​(Kj)​Pt→T​(Kj)​Δ​Kj,\displaystyle\int\_{0}^{F\_{t\to T}}g^{\prime\prime}(K)P\_{t\to T}(K)\mathop{}\!\mathrm{d}K\approx\sum\_{j=0}^{J}g^{\prime\prime}(K\_{j})P\_{t\to T}(K\_{j})\,\Delta K\_{j}, |  | (3) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​K0\displaystyle\Delta K\_{0} | ≔K1−K0,Δ​KJ≔KJ−KJ−1,Δ​Kj≔Kj+1−Kj−12​(1≤j≤J−1).\displaystyle\coloneqq K\_{1}-K\_{0},\quad\Delta K\_{J}\coloneqq K\_{J}-K\_{J-1},\quad\Delta K\_{j}\coloneqq\frac{K\_{j+1}-K\_{j-1}}{2}\ (1\leq j\leq J-1). |  |

This is the trapezoidal discretization used in the CBOE’s VIX methodology and in related model-free moment estimators. We refer to ([3](https://arxiv.org/html/2601.14852v1#S2.E3 "In 2.1 Carr-Madan approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) as the CM *approximation or discretization*, to distinguish it from the exact CM formula in ([2](https://arxiv.org/html/2601.14852v1#S2.E2 "In 2.1 Carr-Madan approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")). Before introducing our projection-based alternative, we illustrate how ([3](https://arxiv.org/html/2601.14852v1#S2.E3 "In 2.1 Carr-Madan approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) is used in two canonical applications.

###### Example 1 (Risk-neutral variance (SVIX)).

[[47](https://arxiv.org/html/2601.14852v1#bib.bib67 "What is the expected return on the market?")] derives a bound on the conditional expected market return using the risk-neutral variance:

|  |  |  |
| --- | --- | --- |
|  | 𝐄t​Rt→T−Rf,t→T≥1Rf,t→T​𝐕𝐚𝐫tQ​Rt→T,\mathbf{E}\_{t}R\_{t\to T}-R\_{f,t\to T}\geq\frac{1}{R\_{f,t\to T}}\mathbf{Var}\_{t}^{Q}R\_{t\to T}, |  |

where Rt→T=ST/StR\_{t\to T}=S\_{T}/S\_{t} is the return on the stock. To compute this bound from the data, it is necessary to calculate 𝐄tQ​ST2\mathbf{E}\_{t}^{Q}S\_{T}^{2}. The CM approximation can then be used with g​(ST)=ST2g(S\_{T})=S\_{T}^{2} and g′′​(ST)=2g^{\prime\prime}(S\_{T})=2.

###### Example 2 (Risk-neutral entropy (VIX)).

The VIX is a popular measure of market uncertainty and is defined by the risk-neutral entropy of returns [[47](https://arxiv.org/html/2601.14852v1#bib.bib67 "What is the expected return on the market?")]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | VIXt→T2=2T−t​(log⁡Rf,t→T−𝐄tQ​log⁡Rt→T).\mathrm{VIX}\_{t\to T}^{2}=\frac{2}{T-t}\left(\log R\_{f,t\to T}-\mathbf{E}\_{t}^{Q}\log R\_{t\to T}\right). |  | (4) |

Entropy, just like variance, is a measure of variability of a random variable. In this case it is necessary to calculate the expectation of a log\log-return, which can be accomplished with the CM approximation using g​(ST)=log⁡(ST)g(S\_{T})=\log(S\_{T}) and g′′​(ST)=−1/ST2g^{\prime\prime}(S\_{T})=-1/S\_{T}^{2}. [[16](https://arxiv.org/html/2601.14852v1#bib.bib86 "Option prices, implied price processes, and stochastic volatility")] further show that the VIX measures the risk-neutral expected volatility from time tt to t+Tt+T.

In addition to these examples, there are important settings in which the CM formula does not directly apply. The next two examples illustrate cases that are central for empirical work.

###### Example 3 (Risk-neutral distribution).

The estimation of the risk-neutral density is not covered by the CM formula because the payoff function necessary to calculate the PDF corresponds to a “discontinuous function”. However, [[15](https://arxiv.org/html/2601.14852v1#bib.bib65 "Prices of state-contingent claims implicit in option prices")] show that the risk-neutral CDF and PDF can be derived from

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ft→TQ​(K)\displaystyle F\_{t\to T}^{Q}(K) | =𝐄tQ​𝟙​({ST≤K})=1+Rf,t→T​∂∂K​Ct→T​(K)\displaystyle=\mathbf{E}\_{t}^{Q}\mathds{1}\left(\{S\_{T}\leq K\}\right)=1+R\_{f,t\to T}\frac{\partial}{\partial K}C\_{t\to T}(K) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ft→TQ​(K)\displaystyle f\_{t\to T}^{Q}(K) | =∂∂K​Ft→TQ​(K)=Rf,t→T​∂2∂K2​Ct→T​(K).\displaystyle=\frac{\partial}{\partial K}F\_{t\to T}^{Q}(K)=R\_{f,t\to T}\frac{\partial^{2}}{\partial K^{2}}C\_{t\to T}(K). |  |

These formulas are widely used to estimate risk-neutral densities and, when combined with additional information on physical probabilities, to infer pricing kernels and risk aversion. We will show that projection can also be used to estimate the risk-neutral distribution, thereby treating Examples [1](https://arxiv.org/html/2601.14852v1#Thmexmp1 "Example 1 (Risk-neutral variance (SVIX)). ‣ 2.1 Carr-Madan approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")–[3](https://arxiv.org/html/2601.14852v1#Thmexmp3 "Example 3 (Risk-neutral distribution). ‣ 2.1 Carr-Madan approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") in a unified manner.

###### Example 4 (Risk-neutral covariance and correlation).

For hedging purposes, it is often useful to estimate the risk-neutral covariance between two stock returns (see, e.g., [[46](https://arxiv.org/html/2601.14852v1#bib.bib122 "Countercyclical currency risk premia")]). In a different direction, the risk-neutral covariance between the market return and an individual stock also allows us to infer that stock’s equity premium when the representative investor has log utility ([[49](https://arxiv.org/html/2601.14852v1#bib.bib92 "Information in derivatives markets: forecasting prices with prices")]):

|  |  |  |
| --- | --- | --- |
|  | 𝐄t​Ri,t→T−Rf,t→T=1Rf,t→T​𝐂𝐨𝐯tQ(Ri,t→T,Rt→T).\mathbf{E}\_{t}R\_{i,t\to T}-R\_{f,t\to T}=\frac{1}{R\_{f,t\to T}}\mathop{\mathbf{Cov}}\nolimits\_{t}^{Q}\left(R\_{i,t\to T},R\_{t\to T}\right). |  |

In this case, the CM formula neither applies because it is inherently univariate. Generally, estimating a covariance from options remains an open problem.444In certain settings the covariance is identifiable from option prices, e.g., for quanto options [[41](https://arxiv.org/html/2601.14852v1#bib.bib83 "The quanto theory of exchange rates")], or one can estimate it by imposing additional constraints, such as maximizing entropy (see [[13](https://arxiv.org/html/2601.14852v1#bib.bib121 "Option-implied dependence and correlation risk premium")]).
Section [4](https://arxiv.org/html/2601.14852v1#S4 "4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") shows how the projection approach extends to the multivariate setting, allowing one to estimate these correlations.

It can also be of interest to estimate the joint risk-neutral distribution. However, there is no higher-dimensional analogue of [[15](https://arxiv.org/html/2601.14852v1#bib.bib65 "Prices of state-contingent claims implicit in option prices")]. We derive necessary and sufficient conditions on the option market that guarantee a unique multivariate risk-neutral measure. Although these conditions are typically not met in practice, the projection approach can nonetheless yield accurate approximations.

### 2.2 A simple illustration of the projection method

To illustrate the projection approach to estimating risk-neutral expectations of non-linear payoffs, consider the following simple example.

###### Example 5 (Projection approach).

Suppose the stock price at time TT can take four possible values: ST=[10,11,12,13]′S\_{T}=[10,11,12,13]^{\prime}. We aim to replicate the payoff of the squared stock value, ST2S\_{T}^{2}. Assume we can trade a risk-free asset with return Rf,t→TR\_{f,t\to T}, the stock itself, and a call option on the stock with strike K=12K=12. The squared stock value and the payoffs of the tradable assets, denoted by the matrix XX, are given by

|  |  |  |
| --- | --- | --- |
|  | ST2=(100121144169),X=(1100111011201131).S\_{T}^{2}=\begin{pmatrix}100\\ 121\\ 144\\ 169\end{pmatrix},\qquad X=\begin{pmatrix}1&10&0\\ 1&11&0\\ 1&12&0\\ 1&13&1\end{pmatrix}. |  |

Clearly the market in this example is not complete because the value of ST2S\_{T}^{2} cannot be replicated perfectly by a portfolio of tradable assets. To find a portfolio that comes closest to replicating ST2S\_{T}^{2}, a natural idea is to project ST2S\_{T}^{2} onto the space spanned by XX:

|  |  |  |
| --- | --- | --- |
|  | ST2≈X​β^,where ​β^=(X′​X)−1​X′​ST2.S\_{T}^{2}\approx X\hat{\beta},\quad\text{where }\hat{\beta}=\left(X^{\prime}X\right)^{-1}X^{\prime}S\_{T}^{2}. |  |

Because the prices of the tradable assets are observable, we can estimate the risk-neutral expectation of ST2S\_{T}^{2} via

|  |  |  |
| --- | --- | --- |
|  | 𝐄tQ​ST2≈[1,Ft→T,Rf,t→T​Ct→T​(12)]​β^.\mathbf{E}\_{t}^{Q}S\_{T}^{2}\approx[1,F\_{t\to T},R\_{f,t\to T}C\_{t\to T}(12)]\hat{\beta}. |  |

This approximation follows from risk-neutral pricing because Ft→T=𝐄tQ​[ST]F\_{t\to T}=\mathbf{E}\_{t}^{Q}[S\_{T}] and Ct→T​(12)=(1/Rf,t→T)​𝐄tQ​[max⁡(ST−12,0)]C\_{t\to T}(12)=(1/R\_{f,t\to T})\mathbf{E}\_{t}^{Q}[\max(S\_{T}-12,0)]. In general, the projection estimate will differ from the CM estimate, because in this example the CM approach always assigns a portfolio weight of 2 to the option, regardless of the strike price.

The projection approach also generalizes the familiar put–call parity. For example, if we replace ST2S\_{T}^{2} with the payoff of a put option, max⁡(12−ST,0)\max(12-S\_{T},0), the projection on XX yields zero error, thereby recovering the classical parity relation. By contrast, put–call parity is not covered by the CM formula because the payoff functions are not twice differentiable.

### 2.3 General projection approach

This section generalizes the example above and introduces notation. Let the observed (ordered) out-of-the-money put and call strikes be

|  |  |  |
| --- | --- | --- |
|  | 𝐊P≔[K1P,…,KnkPP]′,𝐊C≔[K1C,…,KnkCC]′,\mathbf{K}^{P}\coloneqq[K\_{1}^{P},\dots,K\_{n\_{k}^{P}}^{P}]^{\prime},\qquad\mathbf{K}^{C}\coloneqq[K\_{1}^{C},\dots,K\_{n\_{k}^{C}}^{C}]^{\prime}, |  |

with KnkPP≤Ft→TK\_{n\_{k}^{P}}^{P}\leq F\_{t\to T} and K1C>Ft→TK\_{1}^{C}>F\_{t\to T}, and define the total number of strikes by nk≔nkP+nkCn\_{k}\coloneqq n\_{k}^{P}+n\_{k}^{C}. Let

|  |  |  |
| --- | --- | --- |
|  | 𝐬≔[s1,…,sns]′\mathbf{s}\coloneqq[s\_{1},\dots,s\_{n\_{s}}]^{\prime} |  |

denote a researcher-chosen grid of stock prices at maturity TT. The choice of the endpoints (s1,sns)(s\_{1},s\_{n\_{s}}) amounts to a stance on the relevant support of the risk-neutral distribution; we discuss a data-driven choice in Section [6.1](https://arxiv.org/html/2601.14852v1#S6.SS1 "6.1 Empirical estimates of SVIX and VIX ‣ 6 Empirical application ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"). Importantly, this allows us to estimate risk-neutral expectations *even outside the range of observed strikes*.

Define the payoff design matrices for puts and calls on the grid 𝐬\mathbf{s} by

|  |  |  |
| --- | --- | --- |
|  | Xi​jP≔(KjP−si)+,Xi​jC≔(si−KjC)+,i=1,…,ns.X^{P}\_{ij}\coloneqq(K\_{j}^{P}-s\_{i})\_{+},\qquad X^{C}\_{ij}\coloneqq(s\_{i}-K\_{j}^{C})\_{+},\qquad i=1,\dots,n\_{s}. |  |

When it creates no confusion, we drop the superscripts PP and CC on strikes. Let 𝟏ns\mathbf{1}\_{n\_{s}} denote an nsn\_{s}-vector of ones and define the state-by-state payoff matrix

|  |  |  |
| --- | --- | --- |
|  | X≔[ 1ns𝐬XPXC]∈ℝns×(2+nk).X\coloneqq\bigl[\,\mathbf{1}\_{n\_{s}}\ \ \mathbf{s}\ \ X^{P}\ \ X^{C}\,\bigr]\in\mathbb{R}^{n\_{s}\times(2+n\_{k})}. |  |

If a put and a call share the same strike, including both is redundant given put–call parity and the presence of the bond and stock columns. Let Y∈ℝnsY\in\mathbb{R}^{n\_{s}} be the payoff evaluated on the grid, Yi≔g​(si)Y\_{i}\coloneqq g(s\_{i}). We compute the projection of YY onto the column span of XX:

|  |  |  |
| --- | --- | --- |
|  | Y=X​β^+ε^,β^≔(X′​X)−1​X′​Y.Y=X\widehat{\beta}+\widehat{\varepsilon},\qquad\widehat{\beta}\coloneqq(X^{\prime}X)^{-1}X^{\prime}Y. |  |

Equivalently, this yields the approximation

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(ST)≈β^1+β^2​ST+∑j=1nkPβ^jP​(Kj−ST)++∑j=1nkCβ^jC​(ST−Kj)+≕g^​(ST).g(S\_{T})\approx\hat{\beta}\_{1}+\hat{\beta}\_{2}S\_{T}+\sum\_{j=1}^{n\_{k}^{P}}\hat{\beta}\_{j}^{P}(K\_{j}-S\_{T})\_{+}+\sum\_{j=1}^{n\_{k}^{C}}\hat{\beta}\_{j}^{C}(S\_{T}-K\_{j})\_{+}\eqqcolon\hat{g}(S\_{T}). |  | (5) |

Taking risk-neutral expectations on both sides, we obtain a projection estimate of the risk-neutral expectation.

###### Definition 1 (Projection estimator).

Let XX collect terminal payoffs at TT (cash, the underlying, and options) evaluated on a state grid, and let β^\hat{\beta} be the OLS coefficient vector from projecting the target payoff YY on XX. Then the projection estimator is defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐄tQ​g^​(ST)≔β^1+β^2​Ft→T+Rf,t→T​(∑j=1nkPβ^jP​Pt→T​(Kj)+∑j=1nkCβ^jC​Ct→T​(Kj)).\mathbf{E}\_{t}^{Q}\hat{g}(S\_{T})\coloneqq\hat{\beta}\_{1}+\hat{\beta}\_{2}F\_{t\to T}+R\_{f,t\to T}\left(\sum\_{j=1}^{n\_{k}^{P}}\hat{\beta}\_{j}^{P}P\_{t\to T}(K\_{j})+\sum\_{j=1}^{n\_{k}^{C}}\hat{\beta}\_{j}^{C}C\_{t\to T}(K\_{j})\right). |  | (6) |

###### Remark 1 (Constrained least squares).

In some applications—such as estimating risk-neutral variance—it is natural to impose that the estimate be nonnegative. With very few options, the least-squares replicating portfolio implied by β^\hat{\beta} can produce a payoff that is negative over parts of the state space, which in turn can yield a negative variance estimate. In such cases, it is natural to require the replicating payoff to be nonnegative pointwise. This is achieved by solving the constrained least-squares problem

|  |  |  |
| --- | --- | --- |
|  | minβ⁡‖Y−X​β‖22subject toX​β≥0,\min\_{\beta}\ \|Y-X\beta\|\_{2}^{2}\quad\text{subject to}\quad X\beta\geq 0, |  |

where the inequality is interpreted componentwise on the chosen state grid. This convex quadratic program enforces a nonnegative replication in every state and, hence, a nonnegative variance estimate. Similarly, one may impose direct restrictions on the portfolio weights, for example, the componentwise bound β≥−c\beta\geq-c for some c>0c>0 to reflect borrowing constraints.

###### Remark 2 (Weighted least squares).

The replicating portfolio in ([5](https://arxiv.org/html/2601.14852v1#S2.E5 "In 2.3 General projection approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) penalizes deviations equally across states (stock prices). In applications it can be preferable to penalize errors more heavily near the forward price—where the risk-neutral measure places more mass–—and less heavily in the tails. This can be implemented via weighted least squares:

|  |  |  |
| --- | --- | --- |
|  | β^wls=(X′​W​X)−1​X′​W​y,\hat{\beta}\_{\mathrm{wls}}=(X^{\prime}WX)^{-1}X^{\prime}Wy, |  |

where W=diag​(w1,…,wns)W=\mathrm{diag}(w\_{1},\dots,w\_{n\_{s}}) collects state weights. The (infeasible) theoretically optimal choice sets weights proportional to the risk-neutral density, wi∝ft→TQ​(si)w\_{i}\propto f\_{t\to T}^{Q}(s\_{i}). A practical alternative is a Cauchy distribution centered at the forward price with a scale parameter proportional to the implied volatility.

###### Remark 3 (Redundancy of option-implied regressors).

Because the projection estimator is an OLS linear projection of the target payoff onto the span of the option basis functions, the Frisch–Waugh–Lovell theorem implies that adding any payoff that already lies in this span does not change the fitted values. For example, the CBOE VIX (Example [2](https://arxiv.org/html/2601.14852v1#Thmexmp2 "Example 2 (Risk-neutral entropy (VIX)). ‣ 2.1 Carr-Madan approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) corresponds to a log contract that is replicated from options. Hence adding log⁡(ST)\log(S\_{T}) as an additional basis element and using the VIX price does not improve the estimation of a general payoff. By contrast, if there were a genuinely tradable claim delivering the log payoff (or a variance claim) whose price were not implied by the options in the basis, then adding log⁡(ST)\log(S\_{T}) would enlarge the span and improve estimation. Notice that the CM formula does not provide a generic way to exploit information from non-option payoffs.

To illustrate the benefits of the replicating portfolio obtained by projection in ([5](https://arxiv.org/html/2601.14852v1#S2.E5 "In 2.3 General projection approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) relative to the CM discretization in ([3](https://arxiv.org/html/2601.14852v1#S2.E3 "In 2.1 Carr-Madan approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")), Figure [1](https://arxiv.org/html/2601.14852v1#S2.F1 "Figure 1 ‣ 2.3 General projection approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") plots both replicating portfolios for a nonlinear payoff. The projection-based portfolio is nearly indistinguishable from the true payoff across the entire domain, including outside the range of observed strikes. In contrast, the CM approximation replicates the payoff much less accurately, especially in the tails. The discrepancy arises because the CM formula relies on a Taylor expansion around the forward price (see ([2.1](https://arxiv.org/html/2601.14852v1#S2.Ex1 "2.1 Carr-Madan approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"))), and strike prices do not go far enough in the tails to yield an accurate approximation. As a result, the risk-neutral expectation can be estimated with substantial error.

![Refer to caption](x1.png)


Figure 1: Replication of cubic payoff. The figure shows the function g​(Rt→T)=(2/3)​Rt→T3−(37/40)​Rt→T2+(21/25)​Rt→Tg(R\_{t\to T})=(2/3)R\_{t\to T}^{3}-(37/40)R\_{t\to T}^{2}+(21/25)R\_{t\to T} (black), together with the projection-based portfolio (blue) and CM portfolio (red). The approximations are based on 15 strike prices drawn from a uniform distribution. Dashed vertical lines indicate the minimum and maximum strike values used.

### 2.4 Continuous-state limit

To implement the projection method, the researcher needs to choose a grid of possible future stock values, 𝐬\mathbf{s}. This is analogous to specifying the up and down states in the binomial option pricing model. Since the grid can be made arbitrarily fine, a natural question is what the discrete projection converges to as the mesh size tends to zero.

Throughout, we denote the set of basis functions used for portfolio replication by

|  |  |  |
| --- | --- | --- |
|  | ℱ2+nk={1,ST,(K1−ST)+,…,(KnkP−ST)+,(ST−K1)+,…,(ST−KnkC)+}.\mathcal{F}\_{2+n\_{k}}=\left\{{1,S\_{T},\left(K\_{1}-S\_{T}\right)^{+},\dots,\left(K\_{n\_{k}^{P}}-S\_{T}\right)^{+},\left(S\_{T}-K\_{1}\right)^{+},\dots,\left(S\_{T}-K\_{n\_{k}^{C}}\right)^{+}}\right\}. |  |

When convenient, we index the basis as ϕi∈ℱ2+nk\phi\_{i}\in\mathcal{F}\_{2+n\_{k}} for i=1,…,2+nki=1,\dots,2+n\_{k}. To derive the limiting value as maxi⁡|si+1−si|→0\max\_{i}\left\lvert s\_{i+1}-s\_{i}\right\rvert\to 0, we make the following assumption.

###### Assumption 1.

Let A=[amin,amax]A=[a\_{\min},a\_{\max}] be a compact interval in ℝ++\mathbb{R}\_{++} such that amin<K1Pa\_{\min}<K\_{1}^{P} and amax>KnkCCa\_{\max}>K\_{n\_{k}^{C}}^{C}, and all strike prices are unique. Moreover, g∈L2​(A)g\in L^{2}(A): ∫Ag​(S)2​d​S<∞\int\_{A}g(S)^{2}\mathop{}\!\mathrm{d}S<\infty.

Assumption [1](https://arxiv.org/html/2601.14852v1#Thmasmp1 "Assumption 1. ‣ 2.4 Continuous-state limit ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") guarantees that the projection estimator is well defined when nsn\_{s} is sufficiently large. In particular, because the strike prices are assumed to be unique, all basis functions are linearly independent over L2​(A)L^{2}(A). The next result establishes the continuous-grid limit. By slight abuse of notation, let β^ns\hat{\beta}\_{n\_{s}} denote the projection coefficients obtained from a grid of size nsn\_{s}.

###### Proposition 1.

Let Assumption [1](https://arxiv.org/html/2601.14852v1#Thmasmp1 "Assumption 1. ‣ 2.4 Continuous-state limit ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") hold and define an inner product on L2​(A)L^{2}(A) by

|  |  |  |
| --- | --- | --- |
|  | ⟨ϕi,ϕj⟩=∫Aϕi​(ST)​ϕj​(ST)​d​ST.\left\langle\phi\_{i},\phi\_{j}\right\rangle=\int\_{A}\phi\_{i}(S\_{T})\phi\_{j}(S\_{T})\mathop{}\!\mathrm{d}S\_{T}. |  |

If maxi⁡|si+1−si|→0\max\_{i}|s\_{i+1}-s\_{i}|\to 0 as ns→∞n\_{s}\to\infty, then β^ns→β^\hat{\beta}\_{n\_{s}}\to\hat{\beta}, where

|  |  |  |  |
| --- | --- | --- | --- |
|  | β^ns→[⟨ϕ1,ϕ1⟩…⟨ϕ1,ϕ2+nk⟩⋮⋱⋮⟨ϕ2+nk,ϕ1⟩…⟨ϕ2+nk,ϕ2+nk⟩]−1​[⟨ϕ1,g⟩⋮⟨ϕ2+nk,g⟩]≕β^.\hat{\beta}\_{n\_{s}}\to\begin{bmatrix}\left\langle\phi\_{1},\phi\_{1}\right\rangle&\dots&\left\langle\phi\_{1},\phi\_{2+n\_{k}}\right\rangle\\ \vdots&\ddots&\vdots\\ \left\langle\phi\_{2+n\_{k}},\phi\_{1}\right\rangle&\dots&\left\langle\phi\_{2+n\_{k}},\phi\_{2+n\_{k}}\right\rangle\end{bmatrix}^{-1}\begin{bmatrix}\left\langle\phi\_{1},g\right\rangle\\ \vdots\\ \left\langle\phi\_{2+n\_{k}},g\right\rangle\end{bmatrix}\eqqcolon\hat{\beta}. |  | (7) |

Moreover, β^\hat{\beta} solves the minimization problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | β^=arg​minβ∈ℝ2+nk​∫A(g​(ST)−∑j=12+nkβj​ϕj​(ST))2​d​ST.\hat{\beta}=\operatornamewithlimits{arg\,min}\_{\beta\in\mathbb{R}^{2+n\_{k}}}\int\_{A}\left(g(S\_{T})-\sum\_{j=1}^{2+n\_{k}}\beta\_{j}\phi\_{j}(S\_{T})\right)^{2}\mathop{}\!\mathrm{d}S\_{T}. |  | (8) |

Longer proofs are delegated to Appendix [A](https://arxiv.org/html/2601.14852v1#A1 "Appendix A Proofs ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"). The minimization property in ([8](https://arxiv.org/html/2601.14852v1#S2.E8 "In Proposition 1. ‣ 2.4 Continuous-state limit ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) states that β^\hat{\beta} minimizes the L2L^{2}-distance between g​(⋅)g(\cdot) and the basis functions. In this sense, the basis functions optimally replicate g​(⋅)g(\cdot) over the entire domain. This property is attractive because AA is allowed to be much wider than the range of available strike prices, which is beneficial if we believe the strikes only cover a limited range of the stock price’s support. The approach of [[20](https://arxiv.org/html/2601.14852v1#bib.bib66 "Towards a theory of volatility trading")] does not have this property. The continuous-state limit is also a convenient tool in some of the proofs. However, for practical computations we will mostly rely on the discrete approximation, as it is faster and numerically more stable.

## 3 Completeness, convergence, and distribution estimation

This section establishes conditions under which options complete the market and the risk-neutral measure is uniquely determined. We then derive the convergence rate of the projection estimator for risk-neutral expectations. Finally, we show how the same projection framework can be used to estimate the risk-neutral distribution.

### 3.1 Market completeness

Market completeness implies that every contingent claim can be hedged and, equivalently, that the risk-neutral measure is unique. As is well known, options complete the market for a single underlying security. For example, the CM portfolio in ([3](https://arxiv.org/html/2601.14852v1#S2.E3 "In 2.1 Carr-Madan approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) converges to the true risk-neutral moment under certain assumptions on the strike prices. We now establish the analogous result for projection. Specifically, if there is a portfolio of options, the risk-free asset, and the underlying stock that perfectly replicates the payoff g​(ST)g(S\_{T}), then projection will find it, as the following proposition shows.

###### Proposition 2.

Let A⊂ℝ+A\subset\mathbb{R}\_{+} be compact and let C​(A)C(A) denote the space of continuous functions on AA equipped with the sup norm ‖g‖=supx∈A|g​(x)|\left\lVert g\right\rVert=\sup\_{x\in A}|g(x)|. If the strikes {Kj}j=1nk\{K\_{j}\}\_{j=1}^{n\_{k}} satisfy

|  |  |  |
| --- | --- | --- |
|  | minj=1,…,nk⁡|x−Kj|→0for every ​x∈Aas ​nk→∞,\min\_{j=1,\dots,n\_{k}}|x-K\_{j}|\to 0\quad\text{for every }x\in A\qquad\text{as }n\_{k}\to\infty, |  |

then span⁡(ℱ2+nk)\operatorname{span}(\mathcal{F}\_{2+n\_{k}}) is dense in C​(A)C(A). Equivalently, for every g∈C​(A)g\in C(A) there exists fnk∈span⁡(ℱ2+nk)f\_{n\_{k}}\in\operatorname{span}(\mathcal{F}\_{2+n\_{k}}) such that ‖g−fnk‖∞→0\left\lVert g-f\_{n\_{k}}\right\rVert\_{\infty}\to 0.

Intuitively, the condition above means that strikes become dense in AA, which is necessary to replicate gg well in the tails. Proposition [2](https://arxiv.org/html/2601.14852v1#Thmprop2 "Proposition 2. ‣ 3.1 Market completeness ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") is a restatement of the classical fact that piecewise linear splines are dense in C​(A)C(A) (see, e.g., [[42](https://arxiv.org/html/2601.14852v1#bib.bib80 "Sur l’approximation des fonctions")]). It is also more general than the CM approximation, which requires additional smoothness (e.g., gg twice differentiable a.e.).

The replication property in Proposition [2](https://arxiv.org/html/2601.14852v1#Thmprop2 "Proposition 2. ‣ 3.1 Market completeness ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") connects to market completeness, which means that the risk-neutral measure is unique [[5](https://arxiv.org/html/2601.14852v1#bib.bib94 "Asset pricing and portfolio choice theory")]. When the prices of options are given and each contingent claim can be replicated, the risk-neutral measure is indeed uniquely pinned down.

###### Corollary 1 (Market completeness).

Let AA and the strikes be as in Proposition [2](https://arxiv.org/html/2601.14852v1#Thmprop2 "Proposition 2. ‣ 3.1 Market completeness ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"), and suppose absence of arbitrage. If two risk-neutral measures agree on the prices of all traded payoffs in span⁡(ℱ2+nk)\operatorname{span}(\mathcal{F}\_{2+n\_{k}}) for all nkn\_{k}, then they coincide on C​(A)C(A) in the limit, and therefore induce the same risk-neutral distribution on AA.

This result is closely related to the [[15](https://arxiv.org/html/2601.14852v1#bib.bib65 "Prices of state-contingent claims implicit in option prices")] formula from Example [3](https://arxiv.org/html/2601.14852v1#Thmexmp3 "Example 3 (Risk-neutral distribution). ‣ 2.1 Carr-Madan approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"). While that formula is theoretically elegant, its practical implementation can be challenging because recovering densities requires numerical differentiation of option prices, which is often unstable. For this reason, researchers and practitioners commonly use the CM approximation to compute risk-neutral expectations. However, the CM approximation is not designed for discontinuous payoffs such as indicator functions and therefore does not directly deliver estimates of the full risk-neutral distribution. In finite samples, this can lead to substantial differences between the risk-neutral expectation implied by [[15](https://arxiv.org/html/2601.14852v1#bib.bib65 "Prices of state-contingent claims implicit in option prices")] and that implied by the CM approximation, which is undesirable. As shown in Proposition [7](https://arxiv.org/html/2601.14852v1#Thmprop7 "Proposition 7 (Risk-neutral distribution). ‣ 3.3 Estimation of the risk-neutral CDF and PDF ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") below, the projection method provides a unified approach that closes this gap.

### 3.2 Convergence rate

In this section, we establish the rate at which the estimated risk-neutral expectation converges as a function of the number of strikes. From approximation theory, we expect the convergence rate to depend on the smoothness of the underlying function (see, e.g., [[19](https://arxiv.org/html/2601.14852v1#bib.bib96 "Spectral methods: fundamentals in single domains"), Chapter 5 ] or [[57](https://arxiv.org/html/2601.14852v1#bib.bib25 "Approximation theory and approximation practice"), Chapter 10 ]). To facilitate the comparison with the CM formula, we assume that the underlying function is twice continuously differentiable. The following proposition derives the convergence rate of the projection approach under this assumption.

###### Proposition 3.

Suppose g∈C2​[amin,amax]g\in C^{2}[a\_{\min},a\_{\max}] and that the risk-neutral density is square-integrable on AA: ∫aminamaxft→TQ​(x)2​d​x<∞\int\_{a\_{\min}}^{a\_{\max}}f\_{t\to T}^{Q}(x)^{2}\mathop{}\!\mathrm{d}x<\infty. Let Δ=maxj⁡Kj+1−Kj\Delta=\max\_{j}K\_{j+1}-K\_{j}, where the strikes are ordered amin<K1<K2<…,Knk<amaxa\_{\min}<K\_{1}<K\_{2}<\dots,K\_{n\_{k}}<a\_{\max}, and assume that Δ=O​(1/nk)\Delta=O(1/n\_{k}), K1−amin=O​(1/nk4/5)K\_{1}-a\_{\min}=O(1/n\_{k}^{4/5}), and amax−Knk=O​(1/nk4/5)a\_{\max}-K\_{n\_{k}}=O(1/n\_{k}^{4/5}). Then as nk→∞n\_{k}\to\infty

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐄tQ​[g​(ST)​𝟙​(ST∈A)]\displaystyle\mathbf{E}\_{t}^{Q}\left[g(S\_{T})\mathds{1}\left(S\_{T}\in A\right)\right] | =𝐄tQ​[g^​(ST)​𝟙​(ST∈A)]+O​(1nk2),\displaystyle=\mathbf{E}\_{t}^{Q}\left[\hat{g}(S\_{T})\mathds{1}\left(S\_{T}\in A\right)\right]+O\left(\frac{1}{n\_{k}^{2}}\right), |  |

where g^\hat{g} is the function estimated by ([5](https://arxiv.org/html/2601.14852v1#S2.E5 "In 2.3 General projection approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")).

Proposition [3](https://arxiv.org/html/2601.14852v1#Thmprop3 "Proposition 3. ‣ 3.2 Convergence rate ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") can be viewed as a quantitative version of the statement that options complete the market (Corollary [1](https://arxiv.org/html/2601.14852v1#Thmthm1 "Corollary 1 (Market completeness). ‣ 3.1 Market completeness ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")). For the CM formula, the integral representation can be approximated using the composite trapezoidal rule, which is the method employed by the CBOE to calculate the VIX. Under the same assumptions, the CM approximation with the trapezoidal rule attains the same convergence rate.

###### Proposition 4.

Let everything be as in Proposition [3](https://arxiv.org/html/2601.14852v1#Thmprop3 "Proposition 3. ‣ 3.2 Convergence rate ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"), and denote the CM replicating portfolio by

|  |  |  |  |
| --- | --- | --- | --- |
|  | g^CM​(ST)\displaystyle\hat{g}\_{\mathrm{CM}}(S\_{T}) | =g​(Ft→T)+g′​(Ft→T)​(ST−Ft→T)\displaystyle=g(F\_{t\to T})+g^{\prime}(F\_{t\to T})(S\_{T}-F\_{t\to T}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∑j:Kj≤Ft→TΔ​Kj​g′′​(Kj)​(Kj−ST)++∑j:Kj>Ft→TΔ​Kj​g′′​(Kj)​(ST−Kj)+.\displaystyle+\sum\_{j:K\_{j}\leq F\_{t\to T}}\Delta K\_{j}\,g^{\prime\prime}(K\_{j})\left(K\_{j}-S\_{T}\right)^{+}+\sum\_{j:K\_{j}>F\_{t\to T}}\Delta K\_{j}\,g^{\prime\prime}(K\_{j})\left(S\_{T}-K\_{j}\right)^{+}. |  |

where

|  |  |  |
| --- | --- | --- |
|  | Δ​Kj={Kj+1−Kj−12,j=2,…,nk−1K2−K1,j=1Knk−Knk−1,j=nk.\Delta K\_{j}=\begin{cases}\frac{K\_{j+1}-K\_{j-1}}{2},&j=2,\dots,n\_{k}-1\\ K\_{2}-K\_{1},&j=1\\ K\_{n\_{k}}-K\_{n\_{k}-1},&j=n\_{k}.\end{cases} |  |

Then, as nk→∞n\_{k}\to\infty

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐄tQ​[g​(ST)​𝟙​(ST∈A)]\displaystyle\mathbf{E}\_{t}^{Q}\left[g(S\_{T})\mathds{1}\left(S\_{T}\in A\right)\right] | =𝐄tQ​[g^CM​(ST)​𝟙​(ST∈A)]+O​(1nk2).\displaystyle=\mathbf{E}\_{t}^{Q}\left[\hat{g}\_{\mathrm{CM}}(S\_{T})\mathds{1}\left(S\_{T}\in A\right)\right]+O\left(\frac{1}{n\_{k}^{2}}\right). |  |

Because projection and the CM approximation attain the same convergence rate, it seems plausible that the coefficients are similar when there are lots of options in the market. In fact, under certain assumptions one can show that asymptotically the projection approach and the CM approximation attach the same weights to each option in the portfolio.

###### Proposition 5.

Let A=[amin,amax]A=[a\_{\min},a\_{\max}] and let amin<K1<⋯<Knk<amaxa\_{\min}<K\_{1}<\cdots<K\_{n\_{k}}<a\_{\max} be uniformly spaced with

|  |  |  |
| --- | --- | --- |
|  | h≔Ki−Ki−1(i=1,…,nk),K0≔amin,Knk+1≔amax.h\coloneqq K\_{i}-K\_{i-1}\quad(i=1,\dots,n\_{k}),\qquad K\_{0}\coloneqq a\_{\min},\quad K\_{n\_{k}+1}\coloneqq a\_{\max}. |  |

Assume g∈C4​(A)g\in C^{4}(A) and let g^\hat{g} be the L2​(A)L^{2}(A)-projection of gg onto
span​(ℱ2+nk)\mathrm{span}(\mathcal{F}\_{2+n\_{k}}),

|  |  |  |
| --- | --- | --- |
|  | g^​(x)=β^1+β^2​x+∑i=1nkγ^i​(x−Ki)+.\hat{g}(x)=\hat{\beta}\_{1}+\hat{\beta}\_{2}x+\sum\_{i=1}^{n\_{k}}\hat{\gamma}\_{i}(x-K\_{i})\_{+}. |  |

Then for interior indices i=2,…,nk−1i=2,\dots,n\_{k}-1,

|  |  |  |
| --- | --- | --- |
|  | γ^i=h​g′′​(Ki)⏟CM weight+O​(h3)as ​h→0,\hat{\gamma}\_{i}=\underbrace{h\,g^{\prime\prime}(K\_{i})}\_{\text{CM weight}}+O(h^{3})\qquad\text{as }h\to 0, |  |

where the O​(h3)O(h^{3}) term is uniform in i=2,…,nk−1i=2,\dots,n\_{k}-1. Moreover, at the boundary one has

|  |  |  |
| --- | --- | --- |
|  | γ^1=h​g′′​(K1)⏟CM weight+O​(h2),γ^nk=h​g′′​(Knk)⏟CM weight+O​(h2),as ​h→0.\hat{\gamma}\_{1}=\underbrace{h\,g^{\prime\prime}(K\_{1})}\_{\text{CM weight}}+O(h^{2}),\qquad\hat{\gamma}\_{n\_{k}}=\underbrace{h\,g^{\prime\prime}(K\_{n\_{k}})}\_{\text{CM weight}}+O(h^{2}),\qquad\text{as }h\to 0. |  |

This result may appear surprising at first because the projection method seems global, in the sense that each coefficient estimate depends on the full set of strikes. However, results from the series regression literature suggest that it depends on the number of basis functions: when the number of strikes is small the estimator is effectively global, whereas as the strike grid becomes dense the projection behaves increasingly like a local method (see, e.g., [[35](https://arxiv.org/html/2601.14852v1#bib.bib129 "Econometrics"), Section 20.7 ]).

Why, then, prefer the projection method? First, the results above are asymptotic and may not accurately describe the finite-sample behavior that is relevant in practice. Second, Proposition [5](https://arxiv.org/html/2601.14852v1#Thmprop5 "Proposition 5. ‣ 3.2 Convergence rate ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") relies on idealized assumptions, such as a uniformly spaced strike grid and a mesh that becomes dense all the way to the endpoints of AA. When either assumption fails, as is typical in option data, the asymptotic approximation in Proposition [5](https://arxiv.org/html/2601.14852v1#Thmprop5 "Proposition 5. ‣ 3.2 Convergence rate ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") need not hold, and the implied portfolio weights can differ substantially from those obtained by a CM type approximation.

It is therefore desirable to derive a finite-sample bound that does not rely on these assumptions. The next proposition provides an exact finite-sample bound on the projection error.

###### Proposition 6.

Let g∈C​(0,∞)g\in C(0,\infty), A=[amin,amax]A=[a\_{\min},a\_{\max}] with amin<K1<…​Knk<amaxa\_{\min}<K\_{1}<\dots K\_{n\_{k}}<a\_{\max}, and let g^\hat{g} be the L2​(A)L^{2}(A)-projection of gg onto ℱ2+nk\mathcal{F}\_{2+n\_{k}}. Suppose that 𝐄tQ​|g​(ST)|<∞\mathbf{E}\_{t}^{Q}\left\lvert g(S\_{T})\right\rvert<\infty, 𝐄tQ​ST<∞\mathbf{E}\_{t}^{Q}S\_{T}<\infty, and that

|  |  |  |
| --- | --- | --- |
|  | 𝐄tQ​[(|g​(ST)|+|g^​(ST)|)​𝟙​(ST∉A)]≤ε.\mathbf{E}\_{t}^{Q}\left[\left(\left\lvert g(S\_{T})\right\rvert+\left\lvert\hat{g}(S\_{T})\right\rvert\right)\mathds{1}\left(S\_{T}\notin A\right)\right]\leq\varepsilon. |  |

Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | |𝐄tQ​g​(ST)−𝐄tQ​g^​(ST)|≤ε+4​dist⁡(g,ℱ2+nk),\left\lvert\mathbf{E}\_{t}^{Q}g(S\_{T})-\mathbf{E}\_{t}^{Q}\hat{g}(S\_{T})\right\rvert\leq\varepsilon+4\operatorname{dist}(g,\mathcal{F}\_{2+n\_{k}}), |  | (9) |

where

|  |  |  |
| --- | --- | --- |
|  | dist⁡(g,ℱ2+nk)=inf{maxx∈A⁡|g−f|:f∈ℱ2+nk}.\operatorname{dist}(g,\mathcal{F}\_{2+n\_{k}})=\inf\left\{{\max\_{x\in A}\left\lvert g-f\right\rvert:f\in\mathcal{F}\_{2+n\_{k}}}\right\}. |  |

If the support of STS\_{T} is contained in AA, then ([9](https://arxiv.org/html/2601.14852v1#S3.E9 "In Proposition 6. ‣ 3.2 Convergence rate ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) holds with ε=0\varepsilon=0.

The tail assumption effectively says that AA, which can be chosen by the researcher, covers most of the support of STS\_{T} and that the contribution of the risk-neutral moment outside AA is small. The main message of Proposition [6](https://arxiv.org/html/2601.14852v1#Thmprop6 "Proposition 6. ‣ 3.2 Convergence rate ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") is that the estimation error is controlled by how well gg is spanned by the *given* option basis functions (together with the constant and linear payoffs). For example, suppose the only option payoff observed is a call option with strike KK, and let g​(ST)=(K−ST)+g(S\_{T})=\left(K-S\_{T}\right)^{+}. Using the identity

|  |  |  |
| --- | --- | --- |
|  | (K−ST)+=(ST−K)++K−ST,\left(K-S\_{T}\right)^{+}=\left(S\_{T}-K\right)^{+}+K-S\_{T}, |  |

the put payoff lies in the span of ℱ2+nk\mathcal{F}\_{2+n\_{k}}. Hence, dist⁡(g,ℱ2+nk)=0\operatorname{dist}(g,\mathcal{F}\_{2+n\_{k}})=0, and the estimation error is zero. This exactly recovers put–call parity and illustrates that the bound is genuinely finite-sample: it only uses the actually traded payoff(s), without any asymptotic market completeness assumption.

A clean substitute for the CM approximation appears unlikely, though we do not have a formal proof. Under the stated assumptions, no analogue of Proposition [6](https://arxiv.org/html/2601.14852v1#Thmprop6 "Proposition 6. ‣ 3.2 Convergence rate ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") can hold for CM, since the formula relies on second derivatives of gg and thus defines an unbounded operator with respect to the sup-norm.555Even if the assumptions were strengthened to, say, g∈C2​(0,∞)g\in C^{2}(0,\infty), a finite-sample bound in the spirit of Proposition [6](https://arxiv.org/html/2601.14852v1#Thmprop6 "Proposition 6. ‣ 3.2 Convergence rate ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") still appears unlikely, because the operator that sends gg to ∑ig′′​(Ki)​(Ki+1−Ki)\sum\_{i}g^{\prime\prime}(K\_{i})\,(K\_{i+1}-K\_{i}) is unbounded as a linear functional on (C(A),∥⋅∥∞)(C(A),\|\cdot\|\_{\infty}); one can construct sequences of bump functions with ‖g‖∞\|g\|\_{\infty} bounded but ∑ig′′​(Ki)​(Ki+1−Ki)\sum\_{i}g^{\prime\prime}(K\_{i})(K\_{i+1}-K\_{i}) diverging. In sum, the projection error is well controlled in finite samples and leads to a notion of finite sample near-optimality, while a clean substitute for CM is not available. The simulation results in Section [5](https://arxiv.org/html/2601.14852v1#S5 "5 Simulation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") also confirm this.

### 3.3 Estimation of the risk-neutral CDF and PDF

The convergence rate and error bound derived above are valid when the function is twice differentiable, or merely continuous. However, the projection method need not be restricted to such functions. A primary motivation to broaden the class of estimable functions comes from estimating the risk-neutral distribution, which requires approximating indicator functions. Since we are ultimately interested in the risk-neutral expectation of a function, the averaging inherent in the expectation operator suggests that the projection approach can still estimate the risk-neutral distribution reliably, even when gg is not smooth.

More precisely, consider g​(ST)=𝟙​(ST≤x)g(S\_{T})=\mathds{1}\left(S\_{T}\leq x\right), which is used to compute the risk-neutral CDF: Ft→TQ​(x)=𝐄tQ​𝟙​(ST≤x)F\_{t\to T}^{Q}(x)=\mathbf{E}\_{t}^{Q}\mathds{1}\left(S\_{T}\leq x\right). In this case, the projection estimates obtained in ([7](https://arxiv.org/html/2601.14852v1#S2.E7 "In Proposition 1. ‣ 2.4 Continuous-state limit ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) will also depend on xx, because

|  |  |  |
| --- | --- | --- |
|  | ⟨ϕj,𝟙(⋅≤x)⟩=∫Aϕj(ST)𝟙(ST≤x)dST=∫aminxϕj(ST)dST.\left\langle\phi\_{j},\mathds{1}\left(\cdot\leq x\right)\right\rangle=\int\_{A}\phi\_{j}(S\_{T})\mathds{1}\left(S\_{T}\leq x\right)\mathop{}\!\mathrm{d}S\_{T}=\int\_{a\_{\min}}^{x}\phi\_{j}(S\_{T})\mathop{}\!\mathrm{d}S\_{T}. |  |

We will let β^​(x)\hat{\beta}(x) denote the coefficient estimate corresponding to the function ⟨ϕj,𝟙(⋅≤x)⟩\left\langle\phi\_{j},\mathds{1}\left(\cdot\leq x\right)\right\rangle. The risk-neutral CDF is then simply estimated by

|  |  |  |  |
| --- | --- | --- | --- |
|  | F^t→TQ​(x)=β^1​(x)+β^2​(x)​Ft→T+Rf,t→T​(∑j=1nkPβ^jP​(x)​Pt→T​(Kj)+∑j=1nkCβ^jC​(x)​Ct→T​(Kj)).\hat{F}\_{t\to T}^{Q}(x)=\hat{\beta}\_{1}(x)+\hat{\beta}\_{2}(x)F\_{t\to T}+R\_{f,t\to T}\left(\sum\_{j=1}^{n\_{k}^{P}}\hat{\beta}\_{j}^{P}(x)P\_{t\to T}(K\_{j})+\sum\_{j=1}^{n\_{k}^{C}}\hat{\beta}\_{j}^{C}(x)C\_{t\to T}(K\_{j})\right). |  | (10) |

The following proposition shows that F^t→TQ​(x)\hat{F}\_{t\to T}^{Q}(x) obtained in this way satisfies many of the natural CDF requirements.

###### Proposition 7 (Risk-neutral distribution).

Let Assumption [1](https://arxiv.org/html/2601.14852v1#Thmasmp1 "Assumption 1. ‣ 2.4 Continuous-state limit ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") hold. Then:

1. (i)

   The estimated CDF satisfies the natural boundary limits

   |  |  |  |
   | --- | --- | --- |
   |  | limx→amin+F^t→TQ​(x)=0,andlimx→amax−F^t→TQ​(x)=1.\lim\_{x\to a\_{\min}^{+}}\hat{F}\_{t\to T}^{Q}(x)=0,\quad\text{and}\quad\lim\_{x\to a\_{\max}^{-}}\hat{F}\_{t\to T}^{Q}(x)=1. |  |
2. (ii)

   F^t→TQ​(x)\hat{F}\_{t\to T}^{Q}(x) is continuously differentiable on the interior of AA, with density estimate f^t→TQ=(F^t→TQ)′\hat{f}\_{t\to T}^{Q}=(\hat{F}\_{t\to T}^{Q})^{\prime}; moreover, f^t→TQ\hat{f}\_{t\to T}^{Q} is piecewise linear.
3. (iii)

   (Moment consistency) The estimated value of a nonlinear contract in ([6](https://arxiv.org/html/2601.14852v1#S2.E6 "In Definition 1 (Projection estimator). ‣ 2.3 General projection approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) equals the moment implied by the estimated distribution:

   |  |  |  |
   | --- | --- | --- |
   |  | 𝐄tQ​[g^​(ST)​𝟙​(ST∈A)]=∫Ag​(x)​d​F^t→TQ​(x).\mathbf{E}\_{t}^{Q}\left[\hat{g}(S\_{T})\mathds{1}\left(S\_{T}\in A\right)\right]=\int\_{A}g(x)\mathop{}\!\mathrm{d}\hat{F}\_{t\to T}^{Q}(x). |  |

Property [(iii)](https://arxiv.org/html/2601.14852v1#S3.I1.i3 "item (iii) ‣ Proposition 7 (Risk-neutral distribution). ‣ 3.3 Estimation of the risk-neutral CDF and PDF ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") is the most important: for any finite set of strikes, the estimated risk-neutral distribution produces the same moment as obtained by directly approximating gg.666That is, using the estimate in ([6](https://arxiv.org/html/2601.14852v1#S2.E6 "In Definition 1 (Projection estimator). ‣ 2.3 General projection approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")). This moment-consistency is typically not guaranteed by existing risk-neutral density estimators. In particular, the value of a nonlinear contract computed from a density estimate will almost never coincide with the estimate given by the CM method. The CM approach is often used in applications where the full risk-neutral distribution is not of primary interest, as it is empirically more robust (see, e.g., [[47](https://arxiv.org/html/2601.14852v1#bib.bib67 "What is the expected return on the market?")]). This discrepancy between density-implied moments and CM-implied moments calls into question the accuracy of the density estimate. By construction, the projection approach avoids this issue and yields a density that is consistent with any moment obtained by direct projection. Furthermore, our density estimator requires only mild assumptions on the underlying distribution: it is sufficient for the first moment of the stock price to exist.

Despite these desirable properties, the projection-based CDF estimate need not be monotone. In simulations, violations of monotonicity occur mainly in the extreme tails, where sparse strike coverage makes the distribution hard to estimate. A remedy is to apply the rearrangement approach of [[25](https://arxiv.org/html/2601.14852v1#bib.bib61 "Inference on counterfactual distributions")], which amounts to sorting the estimated CDF values on the grid to enforce monotonicity. In fact, [[24](https://arxiv.org/html/2601.14852v1#bib.bib97 "Improving point and interval estimators of monotone functions by rearrangement")] show that, unless the original estimate is already monotone, the rearranged CDF has better finite-sample properties.

## 4 Completeness in multiple asset markets and joint dependence

It is of great interest to generalize the projection approach to higher dimensions. For example, the risk-premium of an individual return can often be related to its risk-neutral covariance with the market return (see Example [4](https://arxiv.org/html/2601.14852v1#Thmexmp4 "Example 4 (Risk-neutral covariance and correlation). ‣ 2.1 Carr-Madan approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")). The key challenge is that the claim paying S1,T​S2,TS\_{1,T}S\_{2,T} is not traded; hence 𝐄tQ​(S1,T​S2,T)\mathbf{E}\_{t}^{Q}(S\_{1,T}S\_{2,T}) needs to be identified from tradable options.

A naive extension of the univariate approach is to consider a projection of g​(S1,T,S2,T)=S1,T​S2,Tg(S\_{1,T},S\_{2,T})=S\_{1,T}S\_{2,T} onto

|  |  |  |  |
| --- | --- | --- | --- |
|  | g^​(S1,T,S2,T)=β^0\displaystyle\hat{g}\left(S\_{1,T},S\_{2,T}\right)=\hat{\beta}\_{0} | +β^1​S1,T+∑j=1nkPβ^1,jP​(Kj−S1,T)++∑j=1nkCβ^1,jC​(S1,T−Kj)+\displaystyle+\hat{\beta}\_{1}S\_{1,T}+\sum\_{j=1}^{n\_{k}^{P}}\hat{\beta}\_{1,j}^{P}\left(K\_{j}-S\_{1,T}\right)^{+}+\sum\_{j=1}^{n\_{k}^{C}}\hat{\beta}\_{1,j}^{C}\left(S\_{1,T}-K\_{j}\right)^{+} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +β^2​S2,T+∑j=1nkPβ^2,jP​(Kj−S2,T)++∑j=1nkCβ^2,jC​(S2,T−Kj)+.\displaystyle+\hat{\beta}\_{2}S\_{2,T}+\sum\_{j=1}^{n\_{k}^{P}}\hat{\beta}\_{2,j}^{P}\left(K\_{j}-S\_{2,T}\right)^{+}+\sum\_{j=1}^{n\_{k}^{C}}\hat{\beta}\_{2,j}^{C}\left(S\_{2,T}-K\_{j}\right)^{+}. |  | (11) |

Notice that the strike prices can be different across assets and basis functions, but we suppress this dependence for notational clarity. The risk-neutral expectation of each of the basis functions is known, and thus provides a way to estimate 𝐄tQ​S1,T​S2,T\mathbf{E}\_{t}^{Q}S\_{1,T}S\_{2,T}. However, the next proposition shows that this separable specification cannot capture dependence: the implied correlation is always zero.

###### Proposition 8 (Zero correlation).

Assume that the support of S1,TS\_{1,T} and S2,TS\_{2,T} be defined on compact intervals with midpoints equal to 𝐄tQ​S1,T=F1,t→T\mathbf{E}\_{t}^{Q}S\_{1,T}=F\_{1,t\to T} and 𝐄tQ​S2,T=F2,t→T\mathbf{E}\_{t}^{Q}S\_{2,T}=F\_{2,t\to T} respectively. Let the projection of S1,T​S2,TS\_{1,T}S\_{2,T} be defined by g^\hat{g} in ([11](https://arxiv.org/html/2601.14852v1#S4.E11 "In 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")), then

|  |  |  |
| --- | --- | --- |
|  | 𝐄tQ​[g^​(S1,T,S2,T)]=(𝐄tQ​S1,T)​(𝐄tQ​S2,T).\mathbf{E}\_{t}^{Q}\left[\hat{g}(S\_{1,T},S\_{2,T})\right]=\left(\mathbf{E}\_{t}^{Q}S\_{1,T}\right)\left(\mathbf{E}\_{t}^{Q}S\_{2,T}\right). |  |

Intuitively, options on the individual stocks are sufficient to identify the marginal distributions, but not the joint distribution. To estimate a nonzero correlation, the basis must include nonlinear terms that depend on both assets or incorporate multi-asset instruments such as basket options.

To incorporate additional information that depends on the joint distribution of returns, options on the S&P500 can be used. As [[39](https://arxiv.org/html/2601.14852v1#bib.bib108 "Too-systemic-to-fail: what option markets imply about sector-wide government guarantees")] noted, there are eleven sector ETFs that also have options available, and whose weighted returns sum to the S&P500 return:

|  |  |  |
| --- | --- | --- |
|  | ∑i=111wi,t​Ri,t→T=Rt→T,\sum\_{i=1}^{11}w\_{i,t}R\_{i,t\to T}=R\_{t\to T}, |  |

where wi,tw\_{i,t} and Ri,t→TR\_{i,t\to T} denote the weight and realized return on sector ETF ii, and Rt→TR\_{t\to T} represents the return on the market portfolio. Thus, options on the S&P500 reveal information about the joint distribution of returns. In combination with options on the individual sectors, they allow more precise inference about correlations. Nevertheless, the information conveyed by options on the market index and on the sectors is limited: with three or more sectors, correlations cannot be identified from these derivatives alone. We establish this non-identification result below.

### 4.1 Identifying joint dependence from options on multiple portfolios

We are looking for an extension of Proposition [2](https://arxiv.org/html/2601.14852v1#Thmprop2 "Proposition 2. ‣ 3.1 Market completeness ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") that is valid in higher dimensions. In particular, we would like to understand when option payoffs are rich enough to approximate multivariate contingent claims, and how the set of available portfolios governs what can be learned about joint dependence. Suppose, as in practice, that there are dd sectors (or stocks) that span the market return:777When dealing with sectors, there are thus d=11d=11 sectors spanning the S&P500 return. When dealing with individual returns, there are d=500d=500 returns spanning the S&P500 return.

|  |  |  |
| --- | --- | --- |
|  | ∑i=1dwi,t​Ri,t→T=Rt→T.\sum\_{i=1}^{d}w\_{i,t}R\_{i,t\to T}=R\_{t\to T}. |  |

Assume now that for each sector, as well as for the market return, the assumptions of Proposition [2](https://arxiv.org/html/2601.14852v1#Thmprop2 "Proposition 2. ‣ 3.1 Market completeness ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") hold, so that any continuous function of the sector return (or market return), can be uniformly approximated by options. By combining the options on each of the sectors and on the market return in a portfolio, we thus conclude that the set of option payoff functions span the space

|  |  |  |
| --- | --- | --- |
|  | ℳ​(Ω)≔span⁡{x↦f​(a′​x):a∈Ω,f∈C​(ℝ)},\mathcal{M}(\Omega)\coloneqq\operatorname{span}\Bigl\{\,x\mapsto f(a^{\prime}x)\ :\ a\in\Omega,\ f\in C(\mathbb{R})\Bigr\}, |  |

where Ω⊂ℝd\Omega\subset\mathbb{R}^{d} is the set of available portfolio directions. In our baseline setting,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ω={e1,…,ed,wt},wt=(w1,t,…,wd,t)′,\Omega=\{e\_{1},\dots,e\_{d},\ w\_{t}\},\qquad w\_{t}=(w\_{1,t},\dots,w\_{d,t})^{\prime}, |  | (12) |

where eie\_{i} corresponds to the iith basis vector in ℝd\mathbb{R}^{d} (i.e. it gives full weight to sector ii). Functions of the form f​(a′​x)f(a^{\prime}x) are known as *ridge functions* in the approximation theory literature [[51](https://arxiv.org/html/2601.14852v1#bib.bib112 "Ridge functions")]. Thus, the question of multivariate spanning by simple options can be phrased as a question about when ridge functions with directions in Ω\Omega are dense (in the uniform topology on compact sets). The following result by [[58](https://arxiv.org/html/2601.14852v1#bib.bib109 "Approximation of continuous functions by superpositions of plane waves")] provides necessary and sufficient conditions (see also [[44](https://arxiv.org/html/2601.14852v1#bib.bib110 "Fundamentality of ridge functions")]):

###### Theorem 2.

ℳ​(Ω)\mathcal{M}(\Omega) is dense in C​(ℝd)C(\mathbb{R}^{d}) in the topology of uniform convergence on compacta if and only if no non-trivial homogeneous polynomial vanishes on Ω\Omega.888A polynomial in several variables is homogeneous if all monomials have the same total degree.

In the special case d=2d=2, for the set of option payoffs to be dense Theorem [2](https://arxiv.org/html/2601.14852v1#Thmthm2 "Theorem 2. ‣ 4.1 Identifying joint dependence from options on multiple portfolios ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") requires Ω\Omega to contain an infinite number of pairwise linearly independent vectors. This result is related to [[53](https://arxiv.org/html/2601.14852v1#bib.bib68 "Options and efficiency")] and [[48](https://arxiv.org/html/2601.14852v1#bib.bib84 "Options and the gamma knife"), Result 2 ], but is stronger, because the condition is necessary and sufficient. Furthermore, Theorem [2](https://arxiv.org/html/2601.14852v1#Thmthm2 "Theorem 2. ‣ 4.1 Identifying joint dependence from options on multiple portfolios ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") applies to any d≥1d\geq 1, not just to the case d=2d=2. In applications, we therefore cannot hope to approximate the price of *every* multivariate contingent claim arbitrarily well, since we only observe the finite set of twelve direction vectors in ([12](https://arxiv.org/html/2601.14852v1#S4.E12 "In 4.1 Identifying joint dependence from options on multiple portfolios ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) associated with the d=11d=11 sector portfolios. Nevertheless, it is still possible to approximate the payoff of an arbitrary claim using projection on the sector and market option payoff functions. Furthermore, Theorem [2](https://arxiv.org/html/2601.14852v1#Thmthm2 "Theorem 2. ‣ 4.1 Identifying joint dependence from options on multiple portfolios ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") suggests that better approximations can be obtained if we also consider options on a portfolio of sectors, where the weights are different from the market portfolio. Recently, options were introduced on an equally weighted sector portfolio (called “EQL”). This additional variation can allow us to obtain better estimates of the sector correlations.

### 4.2 Identification of risk-neutral covariances and correlations

Theorem [2](https://arxiv.org/html/2601.14852v1#Thmthm2 "Theorem 2. ‣ 4.1 Identifying joint dependence from options on multiple portfolios ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") suggests that it is impossible to identify the price of an *arbitrary* claim using options, unless we observe an infinite number of different portfolio options.

However, in specific cases, such as the covariance in two dimensions, it is possible to obtain positive results. Furthermore, in higher dimensions, one can still approximate the covariance well even if it is not strictly identified. Focusing on two dimensions first, and letting Rt→T=w1,t​R1,t→T+w2,t​R2,t→TR\_{t\to T}=w\_{1,t}R\_{1,t\to T}+w\_{2,t}R\_{2,t\to T}, the following identity obtains:

|  |  |  |
| --- | --- | --- |
|  | R1,t→T​Rt→T=12​w1,t​Rt→T2+w1,t2​R1,t→T2−w2,t22​w1,t​R2,t→T2.R\_{1,t\to T}R\_{t\to T}=\frac{1}{2w\_{1,t}}R\_{t\to T}^{2}+\frac{w\_{1,t}}{2}R\_{1,t\to T}^{2}-\frac{w\_{2,t}^{2}}{2w\_{1,t}}R\_{2,t\to T}^{2}. |  |

The prices of each of the payoffs on the right-hand side can be inferred from options on the market index, sector 1, and sector 2, respectively. Hence, in this case, the covariance between any of the returns can be identified from option prices.999This is unsurprising, since 𝐕𝐚𝐫tQ​Rt→T=w1,t2​𝐕𝐚𝐫tQ​R1,t→T+w2,t2​𝐕𝐚𝐫tQ​R2,t→T+2​w1,t​w2,t​𝐂𝐨𝐯tQ(R1,t→T,R2,t→T)\mathbf{Var}\_{t}^{Q}R\_{t\to T}=w\_{1,t}^{2}\mathbf{Var}\_{t}^{Q}R\_{1,t\to T}+w\_{2,t}^{2}\mathbf{Var}\_{t}^{Q}R\_{2,t\to T}+2w\_{1,t}w\_{2,t}\mathop{\mathbf{Cov}}\nolimits\_{t}^{Q}\left(R\_{1,t\to T},R\_{2,t\to T}\right) and because each individual variance is identified from option prices, the covariance must also be identifiable.

Generally, the question of identifying the price of a payoff thus depends on whether there is an exact algebraic identity linking the payoff function and a linear combination of ridge functions. It is useful to have a simple algebraic condition that determines whether such a separable identity holds. [[27](https://arxiv.org/html/2601.14852v1#bib.bib111 "On nonlinear functions of linear combinations")] derived the following necessary and sufficient condition for a function g​(x,y)g(x,y) to admit a representation of the form

|  |  |  |
| --- | --- | --- |
|  | g​(x,y)=∑i=1rgi​(ai​x+bi​y)g(x,y)=\sum\_{i=1}^{r}g\_{i}(a\_{i}x+b\_{i}y) |  |

In this case, the following differential identity is necessary and sufficient:

|  |  |  |
| --- | --- | --- |
|  | ∏i=1r(bi​∂∂x−ai​∂∂y)​[g]=0.\prod\_{i=1}^{r}\left(b\_{i}\frac{\partial}{\partial x}-a\_{i}\frac{\partial}{\partial y}\right)[g]=0. |  |

When d≥3d\geq 3, the situation becomes more involved. Necessary and sufficient conditions were derived by [[44](https://arxiv.org/html/2601.14852v1#bib.bib110 "Fundamentality of ridge functions")], although they are not straightforward to verify in practice. For completeness, we state their result in Appendix [A.10](https://arxiv.org/html/2601.14852v1#A1.SS10 "A.10 Sufficient conditions for ridge representation and the proof of Proposition 9 ‣ Appendix A Proofs ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") and provide a more elementary argument showing why correlations in dimensions d≥3d\geq 3 cannot be identified solely from options on the individual sectors and the market portfolio. The following Proposition summarizes this result.

###### Proposition 9 (Non-replication).

Let d≥3d\geq 3. Fix i∈{1,…,d}i\in\left\{{1,\dots,d}\right\} and a weight vector w∈ℝdw\in\mathbb{R}^{d} such that there exist two distinct indices j,k≠ij,k\neq i with wj≠0w\_{j}\neq 0 and wk≠0w\_{k}\neq 0. Consider the function class

|  |  |  |
| --- | --- | --- |
|  | ℱ={∑z=1dgz​(xz)+h​(w⋅x):gz,h∈C​(ℝ)}.\mathcal{F}=\left\{{\sum\_{z=1}^{d}g\_{z}(x\_{z})+h(w\cdot x):g\_{z},h\in C(\mathbb{R})}\right\}. |  |

Then the polynomial g​(x)=xi​(w⋅x)g(x)=x\_{i}(w\cdot x) is not in ℱ\mathcal{F}. Consequently, no static portfolio formed from European options on each single return xzx\_{z} and on the market return w⋅xw\cdot x can replicate the payoff xi​(w⋅x)x\_{i}(w\cdot x).

### 4.3 Projection and equicorrelation

Given that vanilla options on the individual sectors and the market portfolio do not, in general, identify the full matrix of pairwise correlations, one must introduce additional structure. A common approach is to impose equicorrelation. We show that this equicorrelation estimator can be interpreted as a replicating portfolio, and then use projection to generalize it: the projection step chooses portfolio weights that are optimal (in an L2L^{2} sense) for estimating heterogeneous covariances and correlations. In this section we assume that no dividends are paid, although it is straightforward to incorporate them at the cost of slightly heavier notation.101010Under this assumption, 𝐄tQ​Ri,t→T=Rf,t→T\mathbf{E}\_{t}^{Q}R\_{i,t\to T}=R\_{f,t\to T}. If we include dividends, then 𝐄tQ​Ri,t→T=Fi,t→T/St\mathbf{E}\_{t}^{Q}R\_{i,t\to T}=F\_{i,t\to T}/S\_{t}.

The equicorrelation estimator of [[29](https://arxiv.org/html/2601.14852v1#bib.bib113 "Dynamic equicorrelation")] assumes that the correlation between any two assets is the same. In that case, the correlation estimate can be written as

|  |  |  |
| --- | --- | --- |
|  | ρ^t=𝐕𝐚𝐫tQ​(Rt→T)−∑j=1dwj,t2​𝐕𝐚𝐫tQ​(Rj,t→T)2​∑1≤i<j≤dwi,t​wj,t​𝐕𝐚𝐫tQ​(Ri,t→T)​𝐕𝐚𝐫tQ​(Rj,t→T).\hat{\rho}\_{t}=\frac{\mathbf{Var}\_{t}^{Q}(R\_{t\to T})-\sum\_{j=1}^{d}w\_{j,t}^{2}\mathbf{Var}\_{t}^{Q}(R\_{j,t\to T})}{2\sum\_{1\leq i<j\leq d}w\_{i,t}w\_{j,t}\sqrt{\mathbf{Var}\_{t}^{Q}(R\_{i,t\to T})\mathbf{Var}\_{t}^{Q}(R\_{j,t\to T})}}. |  |

This formula is also used by the CBOE to construct its implied correlation index. It is useful to reinterpret this as a portfolio replication problem. The target payoff is

|  |  |  |
| --- | --- | --- |
|  | (Ri,t→T−Rf,t→T)​(Rj,t→T−Rf,t→T)𝐕𝐚𝐫tQ​(Ri,t→T)​𝐕𝐚𝐫tQ​(Rj,t→T),\frac{(R\_{i,t\to T}-R\_{f,t\to T})(R\_{j,t\to T}-R\_{f,t\to T})}{\sqrt{\mathbf{Var}\_{t}^{Q}(R\_{i,t\to T})\mathbf{Var}\_{t}^{Q}(R\_{j,t\to T})}}, |  |

and the basis functions are the quadratic payoffs

|  |  |  |
| --- | --- | --- |
|  | (Rt→T−Rf,t→T)2and(Rj,t→T−Rf,t→T)2,for ​j=1,…,d\left(R\_{t\to T}-R\_{f,t\to T}\right)^{2}\quad\text{and}\quad\left(R\_{j,t\to T}-R\_{f,t\to T}\right)^{2},\quad\text{for }j=1,\dots,d |  |

Viewed this way, the replicating portfolio is the same for all i≠ji\neq j, with weights proportional to a weighted average of sector-specific standard deviations.

The projection approach allows us to optimize and generalize these features. For shorthand, let xk:=Rk,t→T−Rf,t→Tx\_{k}:=R\_{k,t\to T}-R\_{f,t\to T} and xM:=Rt→T−Rf,t→Tx\_{M}:=R\_{t\to T}-R\_{f,t\to T} denote the excess returns on asset kk and on the market, respectively. Let x=[x1,…,xd]′x=[x\_{1},\dots,x\_{d}]^{\prime}, so that xM=w⋅xx\_{M}=w\cdot x, where ww is the vector of market weights. To generalize the equicorrelation estimator, we seek the *optimal* replicating portfolio for xi​xjx\_{i}x\_{j}, which directly targets the risk-neutral covariance between returns ii and jj.111111Working with covariance instead of correlation involves no loss of generality, since the equicorrelation estimator maps directly to a replicating portfolio for xi​xjx\_{i}x\_{j}.

First, consider the continuous-state analogue. Let A=A1×⋯×Ad⊂ℝdA=A\_{1}\times\cdots\times A\_{d}\subset\mathbb{R}^{d} be compact. We seek univariate functions g1,…,gd,gM∈C​(ℝ)g\_{1},\dots,g\_{d},g\_{M}\in C(\mathbb{R}) that minimize

|  |  |  |
| --- | --- | --- |
|  | ∫A(xi​xj−∑k=1dgk​(xk)−gM​(xM))2​d​x,\int\_{A}\Bigl(x\_{i}x\_{j}-\sum\_{k=1}^{d}g\_{k}(x\_{k})-g\_{M}(x\_{M})\Bigr)^{2}\mathop{}\!\mathrm{d}x, |  |

where xM=w′​xx\_{M}=w^{\prime}x. Rather than solving this infinite-dimensional problem directly, we approximate it by restricting attention to low-degree polynomial payoffs. This is motivated by two considerations: (i) polynomials are dense in C​(A)C(A) (Stone–Weierstrass); and (ii) higher-order risk-neutral moments are empirically difficult to estimate. The following result implies that we can restrict attention to quadratic and quartic terms, because the coefficients on odd moments are zero.

###### Proposition 10 (Odd-moment orthogonality).

Fix i≠ji\neq j. Let ℱ={1,x12,…,xd2,xM2}\mathcal{F}=\left\{{1,x\_{1}^{2},\dots,x\_{d}^{2},x\_{M}^{2}}\right\}, and let Π^ℱ​[xi​xj]\widehat{\Pi}\_{\mathcal{F}}[x\_{i}x\_{j}] be the L2L^{2}-projection onto ℱ\mathcal{F} under the inner product ⟨f,g⟩=∫Af​(x)​g​(x)​d​x\left\langle f,g\right\rangle=\int\_{A}f(x)g(x)\mathop{}\!\mathrm{d}x, where A=A1×…​AdA=A\_{1}\times\dots A\_{d}, and Ai=[amini,amaxi]A\_{i}=[a\_{\min}^{i},a\_{\max}^{i}] is symmetric around 0. Define the residual function by

|  |  |  |
| --- | --- | --- |
|  | ε^i​j=xi​xj−Π^ℱ​[xi​xj].\hat{\varepsilon}\_{ij}=x\_{i}x\_{j}-\widehat{\Pi}\_{\mathcal{F}}[x\_{i}x\_{j}]. |  |

Then for every odd integer n≥1n\geq 1,

|  |  |  |
| --- | --- | --- |
|  | ⟨ε^i​j,xkn⟩=0for all ​k∈{1,…,d,M}.\left\langle\hat{\varepsilon}\_{ij},x\_{k}^{n}\right\rangle=0\quad\text{for all }k\in\left\{{1,\dots,d,M}\right\}. |  |

###### Remark 4.

In practice, the interval for each excess return will typically not have 0 as midpoint, because options data are skewed and there tends to be more information going further in the left-tail. Nevertheless, the midpoint of each interval will be close to 0, and we find in simulation that the projection coefficients of odd moments still tend to be negligible in that case.

In contrast to odd-moments, the projection coefficients of even degree will generally not vanish, and including these monomials will generally decrease the approximation error. Compared to the equicorrelation estimator, we thus gain generality in that we incorporate not only variance but also the 4th moment (a measure of tail-thickness), and the portfolio weights are allowed to differ for each pair of assets, thus allowing to estimate the correlation between an arbitrary pair of assets, instead of assuming all correlations are the same.

Projecting xi​xjx\_{i}x\_{j} on the subspace

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℱ={1,x12,…,xd2,x14,…,xd4,xM2,xM4}\mathcal{F}=\left\{{1,x\_{1}^{2},\dots,x\_{d}^{2},x\_{1}^{4},\dots,x\_{d}^{4},x\_{M}^{2},x\_{M}^{4}}\right\} |  | (13) |

also circumvents the computational burden of projecting xi​xjx\_{i}x\_{j} directly onto the full set of option payoffs. The latter would require minimizing an objective that depends on an 1111-dimensional integral and a large number of parameters. A discretized OLS approach is likewise infeasible: with 10001000 grid points per return, the state grid would contain 1000111000^{11} rows.

Instead, we first project xi​xjx\_{i}x\_{j} onto ℱ\mathcal{F} and then project each resulting power payoff onto the corresponding univariate option basis. This two-step procedure yields the same result as projecting directly onto the smallest subspace, because for orthogonal projections onto nested subspaces one has ΠF​g=ΠF​ΠG​g\Pi\_{F}\,g=\Pi\_{F}\,\Pi\_{G}\,g whenever F⊆GF\subseteq G (with respect to the same inner product).

Moreover, the projection of xi​xjx\_{i}x\_{j} onto ℱ\mathcal{F} can be derived in closed form, and the subsequent projection of a monomial such as xk2x\_{k}^{2} onto option payoffs that depend only on asset kk is a one-dimensional problem, which can be solved using the method in Section [2.3](https://arxiv.org/html/2601.14852v1#S2.SS3 "2.3 General projection approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"). Based on the projection coefficient on the subspace in ([13](https://arxiv.org/html/2601.14852v1#S4.E13 "In 4.3 Projection and equicorrelation ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")), we define an estimator of the covariance by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐂𝐨𝐯^i​j,tQ≔𝐄tQ​Π^ℱ​[xi​xj]\displaystyle\widehat{\mathop{\mathbf{Cov}}\nolimits}\_{ij,t}^{Q}\coloneqq\mathbf{E}\_{t}^{Q}\widehat{\Pi}\_{\mathcal{F}}[x\_{i}x\_{j}] | =β^0,i​j+∑k=1d[β^k,i​j​𝐕𝐚𝐫tQ​(Rk,t→T)+γ^k,i​j​𝐄tQ​(Rk,t→T−Rf,t→T)4]\displaystyle=\hat{\beta}\_{0,ij}+\sum\_{k=1}^{d}\left[\hat{\beta}\_{k,ij}\mathbf{Var}\_{t}^{Q}(R\_{k,t\to T})+\hat{\gamma}\_{k,ij}\mathbf{E}\_{t}^{Q}\left(R\_{k,t\to T}-R\_{f,t\to T}\right)^{4}\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +β^M,i​j​𝐕𝐚𝐫tQ​Rt→T+γ^M,i​j​𝐄tQ​(Rt→T−Rf,t→T)4.\displaystyle+\hat{\beta}\_{M,ij}\mathbf{Var}\_{t}^{Q}R\_{t\to T}+\hat{\gamma}\_{M,ij}\mathbf{E}\_{t}^{Q}\left(R\_{t\to T}-R\_{f,t\to T}\right)^{4}. |  | (14) |

Because we can identify the risk-neutral variance, for consistency, it is desirable that the covariance estimator satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐕𝐚𝐫tQ​Rt→T=∑i=1dwi2​𝐕𝐚𝐫tQ​Ri,t→T+2​∑1≤i<j≤dwi​wj​𝐂𝐨𝐯^i​j,tQ.\mathbf{Var}\_{t}^{Q}R\_{t\to T}=\sum\_{i=1}^{d}w\_{i}^{2}\mathbf{Var}\_{t}^{Q}R\_{i,t\to T}+2\sum\_{1\leq i<j\leq d}w\_{i}w\_{j}\widehat{\mathop{\mathbf{Cov}}\nolimits}\_{ij,t}^{Q}. |  | (15) |

The next proposition shows that the addition formula holds whenever the projection space contains all univariate quadratic terms.

###### Proposition 11.

Let ℱ\mathcal{F} be a function space such that {x12,…,xd2,xM2}⊂ℱ\left\{{x\_{1}^{2},\dots,x\_{d}^{2},x\_{M}^{2}}\right\}\subset\mathcal{F}. Define the covariance estimator based on ℱ\mathcal{F} by

|  |  |  |
| --- | --- | --- |
|  | 𝐂𝐨𝐯^i​j,tQ=𝐄tQ​Π^ℱ​[xi​xj].\widehat{\mathop{\mathbf{Cov}}\nolimits}\_{ij,t}^{Q}=\mathbf{E}\_{t}^{Q}\widehat{\Pi}\_{\mathcal{F}}[x\_{i}x\_{j}]. |  |

Then, ([15](https://arxiv.org/html/2601.14852v1#S4.E15 "In 4.3 Projection and equicorrelation ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) holds.

###### Remark 5.

Motivated by the empirical setting, the results above extend to the case with multiple index portfolios. Suppose there are two index returns
xM,1=w1⋅xx\_{M,1}=w\_{1}\cdot x and xM,2=w2⋅xx\_{M,2}=w\_{2}\cdot x with corresponding options. Then Proposition [10](https://arxiv.org/html/2601.14852v1#Thmprop10 "Proposition 10 (Odd-moment orthogonality). ‣ 4.3 Projection and equicorrelation ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") holds verbatim for each index. Likewise, Proposition [11](https://arxiv.org/html/2601.14852v1#Thmprop11 "Proposition 11. ‣ 4.3 Projection and equicorrelation ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") holds simultaneously provided the projection space contains all univariate quadratic terms, including xM,12x\_{M,1}^{2} and xM,22x\_{M,2}^{2}; under this condition, ([15](https://arxiv.org/html/2601.14852v1#S4.E15 "In 4.3 Projection and equicorrelation ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) holds for each weight vector wℓw\_{\ell} (ℓ=1,2\ell=1,2), with the variance on the left-hand side taken for the corresponding portfolio.

### 4.4 Completeness in FX markets

We now extend the above results to foreign-exchange options. Let S1,TS\_{1,T} denote the EUR/USD exchange rate, S2,TS\_{2,T} the GBP/USD rate, and S3,TS\_{3,T} the EUR/GBP rate at maturity TT. By triangular no-arbitrage, S3,T=S1,T/S2,TS\_{3,T}=S\_{1,T}/S\_{2,T}. Hence, options on EUR/GBP reveal joint information not captured by options on EUR/USD and GBP/USD, which only reveal the marginal distribution. Incorporating this additional source of variation is thus expected to yield a better estimate of the covariance and correlation. Throughout we use the convention that S1S\_{1} and S2S\_{2} are quoted in USD, while S3S\_{3} is in GBP units.121212This convention is the same as for the Bloomberg options data that we use in Section [6.2](https://arxiv.org/html/2601.14852v1#S6.SS2 "6.2 Dependence in FX forward returns ‣ 6 Empirical application ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").

With Rf,t→TR\_{f,t\to T} and Rf,t→T£R\_{f,t\to T}^{\pounds} denoting the US and UK gross risk-free rates, the European call prices are

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ci,t→T$​(K)\displaystyle C\_{i,t\to T}^{\mathdollar}(K) | =1Rf,t→T​𝐄tQ$​(Si,T−K)+,i=1,2,\displaystyle=\frac{1}{R\_{f,t\to T}}\mathbf{E}\_{t}^{Q^{\mathdollar}}\left(S\_{i,T}-K\right)^{+},\quad i=1,2, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Ct→T£​(K)\displaystyle C\_{t\to T}^{\pounds}(K) | =1Rf,t→T£​𝐄tQ£​(S3,T−K)+,\displaystyle=\frac{1}{R\_{f,t\to T}^{\pounds}}\mathbf{E}\_{t}^{Q^{\pounds}}\left(S\_{3,T}-K\right)^{+}, |  |

where Q$Q^{\mathdollar} and Q£Q^{\pounds} are the risk-neutral measures using the US and UK money-market accounts as numéraires, respectively. This distinction is needed because EUR/GBP options are GBP-quoted.

Using the change of numéraire result [[56](https://arxiv.org/html/2601.14852v1#bib.bib117 "Stochastic calculus for finance ii: continuous-time models"), Chapter 9], it follows that the Radon-Nikodym derivative between the two risk-neutral measures is given by

|  |  |  |
| --- | --- | --- |
|  | d​Q$d​Q£|ℱT/d​Q$d​Q£|ℱt=Rf,t→TRf,t→T£​S2,tS2,T,\frac{\mathop{}\!\mathrm{d}Q^{\mathdollar}}{\mathop{}\!\mathrm{d}Q^{\pounds}}\bigg|\_{\mathcal{F}\_{T}}\bigg/\frac{\mathop{}\!\mathrm{d}Q^{\mathdollar}}{\mathop{}\!\mathrm{d}Q^{\pounds}}\bigg|\_{\mathcal{F}\_{t}}=\frac{R\_{f,t\to T}}{R\_{f,t\to T}^{\pounds}}\frac{S\_{2,t}}{S\_{2,T}}, |  |

where ℱt\mathcal{F}\_{t} denotes the information set up to time tt. Using this result, we obtain the following expression for a judicious choice of payoff function under Q$Q^{\mathdollar}

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐄tQ$​[S2,T​(S1,TS2,T−K)+]\displaystyle\mathbf{E}\_{t}^{Q^{\mathdollar}}\left[S\_{2,T}\left(\frac{S\_{1,T}}{S\_{2,T}}-K\right)^{+}\right] | =Rf,t→TRf,t→T£​S2,t​𝐄tQ£​[(S3,T−K)+]\displaystyle=\frac{R\_{f,t\to T}}{R\_{f,t\to T}^{\pounds}}S\_{2,t}\mathbf{E}\_{t}^{Q^{\pounds}}\left[\left(S\_{3,T}-K\right)^{+}\right] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =Rf,t→T​S2,t​Ct→T£​(K).\displaystyle=R\_{f,t\to T}S\_{2,t}C\_{t\to T}^{\pounds}(K). |  |

Hence, the reason we consider this specific type of payoff is that the right-hand side involves quantities that are all observed in the market. Notice how the change of numéraire ensures that the quantity on the right is in dollar units, because S2,tS\_{2,t} converts GBP prices to USD.
A key advantage of projection is that it can incorporate the state-dependent change of numéraire kernel when combining options quoted in different currencies, yielding a theoretically consistent USD-denominated replicating portfolio. By contrast, much of the existing FX literature effectively ignores this state dependence (or treats the conversion kernel as approximately constant) when extracting dependence measures from option prices (e.g., [[50](https://arxiv.org/html/2601.14852v1#bib.bib126 "International correlation risk")]). Further, it is possible to obtain the expected value of EUR/USD and GBP/USD under the USD risk-neutral measure because

|  |  |  |
| --- | --- | --- |
|  | 𝐄tQ$​S1,T=Rf,t→TRf,t→T€​S1,t=F1,t→T,𝐄tQ$​S2,T=Rf,t→TRf,t→T£​S2,t=F2,t→T,\mathbf{E}\_{t}^{Q^{\mathdollar}}S\_{1,T}=\frac{R\_{f,t\to T}}{R\_{f,t\to T}^{\text{€}}}S\_{1,t}=F\_{1,t\to T},\quad\mathbf{E}\_{t}^{Q^{\mathdollar}}S\_{2,T}=\frac{R\_{f,t\to T}}{R\_{f,t\to T}^{\pounds}}S\_{2,t}=F\_{2,t\to T}, |  |

where Fi,t→TF\_{i,t\to T} denotes the TT-maturity forward FX rate for pair i=1,2i=1,2.

The foregoing discussion suggests a way to obtain the covariance and correlation between EUR/USD and GBP/USD. Namely, project the function

|  |  |  |
| --- | --- | --- |
|  | (S1,T−F1,t→T)​(S2,T−F2,t→T)\left(S\_{1,T}-F\_{1,t\to T}\right)\left(S\_{2,T}-F\_{2,t\to T}\right) |  |

on basis functions of the form

|  |  |  |
| --- | --- | --- |
|  | 1,S1,T,(S1,T−K)+,S2,T,(S2,T−K)+,S2,T​(S1,TS2,T−K)+.1,\ S\_{1,T},\left(S\_{1,T}-K\right)^{+},S\_{2,T},\ \left(S\_{2,T}-K\right)^{+},\ S\_{2,T}\left(\frac{S\_{1,T}}{S\_{2,T}}-K\right)^{+}. |  |

Upon taking risk-neutral expectations using the US money market as numéraire, all expectations of the basis functions reduce to market observables: constant, forward levels, USD call prices multiplied by a known discount factor, and EUR/GBP call prices multiplied by known discount and FX conversion factors. In particular,

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐂𝐨𝐯tQ$(S1,T,S2,T)\displaystyle\mathop{\mathbf{Cov}}\nolimits\_{t}^{Q^{\mathdollar}}(S\_{1,T},S\_{2,T}) | =𝐄tQ$​(S1,T−F1,t→T)​(S2,T−F2,t→T)\displaystyle=\mathbf{E}\_{t}^{Q^{\mathdollar}}\left(S\_{1,T}-F\_{1,t\to T}\right)\left(S\_{2,T}-F\_{2,t\to T}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≈β^0+β^1,1​F1,t→T+Rf,t→T​∑j=1nkβ^1,j+1​C1,t→T$​(Kj)\displaystyle\approx\hat{\beta}\_{0}+\hat{\beta}\_{1,1}F\_{1,t\to T}+R\_{f,t\to T}\sum\_{j=1}^{n\_{k}}\hat{\beta}\_{1,j+1}C\_{1,t\to T}^{\mathdollar}(K\_{j}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +β^2,1​F2,t→T+Rf,t→T​∑j=1nkβ^2,j+1​C2,t→T$​(Kj)\displaystyle+\hat{\beta}\_{2,1}F\_{2,t\to T}+R\_{f,t\to T}\sum\_{j=1}^{n\_{k}}\hat{\beta}\_{2,j+1}C\_{2,t\to T}^{\mathdollar}(K\_{j}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +F2,t→T​Rf,t→T£​∑j=1nkβ^3,j​Ct→T£​(Kj).\displaystyle+F\_{2,t\to T}R\_{f,t\to T}^{\pounds}\sum\_{j=1}^{n\_{k}}\hat{\beta}\_{3,j}C\_{t\to T}^{\pounds}(K\_{j}). |  |

The number of options and the strike grids generally differ across currencies; we omit this from the notation to avoid clutter.

If options on all three bilateral rates are available and, for each rate, the assumptions of Proposition [2](https://arxiv.org/html/2601.14852v1#Thmprop2 "Proposition 2. ‣ 3.1 Market completeness ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") hold, then static portfolios in these options can uniformly approximate any payoff of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(S1,T,S2,T)=g1​(S1,T)+g2​(S2,T)+S2,T⋅g3​(S1,TS2,T),g(S\_{1,T},S\_{2,T})\;=\;g\_{1}(S\_{1,T})\;+\;g\_{2}(S\_{2,T})\;+\;S\_{2,T}\cdot g\_{3}\!\left(\frac{S\_{1,T}}{S\_{2,T}}\right), |  | (16) |

with gig\_{i} continuous. This function class, however, is not universal on C​(A)C(A) for a compact A⊂ℝ++2A\subset\mathbb{R}\_{++}^{2} with nonempty interior. In particular, the function g​(x,y)=x​yg(x,y)=xy cannot be represented by the display above. Thus, the covariance of exchange rates is not strictly identified from vanillas on the three bilateral rates alone. Nevertheless, we find in simulations that projecting S1,T​S2,TS\_{1,T}S\_{2,T} onto the class ([16](https://arxiv.org/html/2601.14852v1#S4.E16 "In 4.4 Completeness in FX markets ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) yields highly accurate approximations of the covariance and correlation. In our empirical application, we exploit this observation to estimate conditional risk-neutral correlations between exchange rates.

## 5 Simulation

### 5.1 Univariate projection

To illustrate the benefits of the projection based approach, we consider the problem of approximating the value of the SVIX and VIX discussed in Examples [1](https://arxiv.org/html/2601.14852v1#Thmexmp1 "Example 1 (Risk-neutral variance (SVIX)). ‣ 2.1 Carr-Madan approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")–[2](https://arxiv.org/html/2601.14852v1#Thmexmp2 "Example 2 (Risk-neutral entropy (VIX)). ‣ 2.1 Carr-Madan approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"). The Monte-Carlo experiment randomly draws strike prices from a uniform grid with cardinality {10,20,…,130}\left\{{10,20,\dots,130}\right\}. We also consider the case where the strike grid is equally spaced.131313In our implementation, AA covers 99.8% of the distribution’s support, while observed strikes extend only into the 5% tail. Thus Proposition [5](https://arxiv.org/html/2601.14852v1#Thmprop5 "Proposition 5. ‣ 3.2 Convergence rate ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") does not apply, and CM and projection weights can differ substantially. This allows us to study the approximation error as a function of the number of strikes available in the market. In addition, we also consider a design where the number of strikes is fixed, but the range of the strike prices is increasing to cover a bigger part of the distribution’s support.

Based on the strikes, we obtain the corresponding call and put option prices from either the [[10](https://arxiv.org/html/2601.14852v1#bib.bib20 "The pricing of options and corporate liabilities")] model or the stochastic volatility and jump (SVCJ) model of [[30](https://arxiv.org/html/2601.14852v1#bib.bib82 "The impact of jumps in volatility and returns")]. The latter model incorporates jumps in both the return and volatility dynamics which makes estimation more challenging relative to Black-Scholes. More details on the simulation and calibration of these models are given in Appendix [C](https://arxiv.org/html/2601.14852v1#A3 "Appendix C Details on simulation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"). The accuracy of the approximation for each number of strikes is measured by the relative error,

|  |  |  |
| --- | --- | --- |
|  | Relative error=|SVIX^−SVIX|SVIX,\text{Relative error}=\frac{\left\lvert\widehat{\text{SVIX}}-\text{SVIX}\right\rvert}{\text{SVIX}}, |  |

where SVIX^\widehat{\text{SVIX}} is the SVIX estimate obtained by either CM or the projection method. The relative error for VIX is defined analogously.

Figure [2](https://arxiv.org/html/2601.14852v1#S5.F2 "Figure 2 ‣ 5.1 Univariate projection ‣ 5 Simulation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") illustrates the results. Panels [2(a)](https://arxiv.org/html/2601.14852v1#S5.F2.sf1 "In Figure 2 ‣ 5.1 Univariate projection ‣ 5 Simulation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")–[2(d)](https://arxiv.org/html/2601.14852v1#S5.F2.sf4 "In Figure 2 ‣ 5.1 Univariate projection ‣ 5 Simulation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") show convergence as the number of strikes increases, while the strike range remains fixed at 90% of the support. When the strike grid is equally spaced, the relative errors of both methods are roughly half as large as when the strikes are drawn uniformly at random, but both designs convey the same message. The convergence of the CM method is gradual and levels off at a relative error of about 10%. By contrast, the projection approach stabilizes already around 20 strikes, at which point its relative error is roughly an order of magnitude smaller. At 130 strikes, the relative error remains close to 2% in all cases. Moreover, for nearly all strike counts, the projection estimate is pointwise closer to SVIX/VIX than the CM estimate. Because both methods underestimate SVIX/VIX due to the limited strike range, the projection estimate—being closer to the truth—is almost always larger than the corresponding CM estimate. In the empirical application in Section [6.1](https://arxiv.org/html/2601.14852v1#S6.SS1 "6.1 Empirical estimates of SVIX and VIX ‣ 6 Empirical application ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"), we find the same behavior in actual data.

The strike range appears more important for the convergence rate of the projection approach, as shown in Panels [2(e)](https://arxiv.org/html/2601.14852v1#S5.F2.sf5 "In Figure 2 ‣ 5.1 Univariate projection ‣ 5 Simulation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") and [2(f)](https://arxiv.org/html/2601.14852v1#S5.F2.sf6 "In Figure 2 ‣ 5.1 Univariate projection ‣ 5 Simulation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"). In this case, convergence is much faster as the strike range increases while the number of strikes is held fixed at nk=30n\_{k}=30. This result can be understood via the proof of Proposition [3](https://arxiv.org/html/2601.14852v1#Thmprop3 "Proposition 3. ‣ 3.2 Convergence rate ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"), which shows that the error arising from the tails converges to zero faster than the error induced by strike spacing. When the strike range covers almost the entire support, the relative projection error is close to zero and roughly 63 times smaller than for CM.

By contrast, the CM approach shows little improvement when the strike range increases. As the range widens while the number of strikes remains fixed, the average strike spacing becomes larger, which offsets the benefit of better tail coverage because the accuracy of the integral approximation deteriorates as the spacing increases.141414In unreported simulations, we replace the trapezoidal rule in the CM approximation by Simpson’s rule. The numerical results are very similar in all cases and the projection method continues to dominate.

![Refer to caption](x2.png)


(a) Black-Scholes model (equal)

![Refer to caption](x3.png)


(b) SVCJ model (equal)

![Refer to caption](x4.png)


(c) Black-Scholes model

![Refer to caption](x5.png)


(d) SVCJ model

![Refer to caption](x6.png)


(e) Black-Scholes model

![Refer to caption](x7.png)


(f) SVCJ model

Figure 2: MSE of approximation. The figure shows the convergence rate as a function of the number of strikes (upper and middle panels) and as a function of the strike range (bottom panels). In the top panels, the strike grid is equally spaced, while in the middle panels the strikes are uniformly distributed.

### 5.2 Multivariate projection for exchange rates

We simulate exchange-rate outcomes under the risk-neutral measure from a bivariate normal distribution:

|  |  |  |
| --- | --- | --- |
|  | [S1,TS2,T]∼𝖭​([11],[0.120.1⋅0.05⋅ρ0.1⋅0.05⋅ρ0.052]).\begin{bmatrix}S\_{1,T}\\ S\_{2,T}\end{bmatrix}\sim\mathsf{N}\left(\begin{bmatrix}1\\ 1\end{bmatrix},\begin{bmatrix}0.1^{2}&0.1\cdot 0.05\cdot\rho\\ 0.1\cdot 0.05\cdot\rho&0.05^{2}\end{bmatrix}\right). |  |

In each Monte Carlo iteration, we draw the correlation independently as ρ∼𝖴𝗇𝗂𝖿​(−1,1)\rho\sim\mathsf{Unif}(-1,1). For the option inputs, we take five strikes each on S1,TS\_{1,T}, S2,TS\_{2,T}, and S1,T/S2,TS\_{1,T}/S\_{2,T}. The strikes are evenly spaced between the 5th and 95th percentiles of the respective marginal distributions. This choice mirrors OTC FX practice: quotes out to the 5-delta call and 95-delta put (under forward-delta conventions) roughly correspond to the 5th and 95th percentiles for 1-month tenors. The approximation grid is taken to be equally spaced between the 2nd and 98th percentiles of each variable; for two-dimensional quantities we use the tensor product of the univariate grids.

We then project the payoff (S1,T−1)​(S2,T−1)(S\_{1,T}-1)(S\_{2,T}-1) onto the span of the payoffs

|  |  |  |
| --- | --- | --- |
|  | 1,S1,T,(S1,T−K1)+,S2,T,(S2,T−K2)+,S2,T​(S1,T/S2,T−K3)+,1,\quad S\_{1,T},\quad\left(S\_{1,T}-K\_{1}\right)^{+},\quad S\_{2,T},\quad\left(S\_{2,T}-K\_{2}\right)^{+},\quad S\_{2,T}\left(S\_{1,T}/S\_{2,T}-K\_{3}\right)^{+}, |  |

with strikes {K1,K2,K3}\{K\_{1},K\_{2},K\_{3}\} generated as above. To recover the correlation, we also estimate the standard deviations by projecting (S1,T−1)2(S\_{1,T}-1)^{2} onto the constant function, S1,TS\_{1,T}, and options on S1,TS\_{1,T} (and analogously for S2,TS\_{2,T}).

In addition, we consider a setting where S2,TS\_{2,T} is generated as above and then perturbed to S~2,T=S2,T+0.1​S1,T3\tilde{S}\_{2,T}=S\_{2,T}+0.1S\_{1,T}^{3}. S~2,T\tilde{S}\_{2,T} is further normalized so that the mean is 1. We estimate the correlation between S1,TS\_{1,T} and S~2,T\tilde{S}\_{2,T} to introduce nonlinear dependence and verify that our results are not driven by the normality assumption.

The upper panels in Figure [3](https://arxiv.org/html/2601.14852v1#S5.F3 "Figure 3 ‣ 5.2 Multivariate projection for exchange rates ‣ 5 Simulation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") report results from 1,000 Monte Carlo simulations. In both panels, the projection approach recovers the true correlation with high accuracy: the scatter points lie nearly on the 45∘45^{\circ} line. This is encouraging because the correlation is not exactly identifiable within the restricted function class (see Section [4.4](https://arxiv.org/html/2601.14852v1#S4.SS4 "4.4 Completeness in FX markets ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")). We conclude that projection delivers an excellent approximation to the true correlation in the FX setting, irrespective of the underlying distribution of the data.

In the bottom panels, we use the same generated data to estimate the joint probability that both returns are below a certain threshold, which can be interpreted as a measure of joint tail risk. Specifically, we estimate 𝐏​(S1,T≤0.95,S2,T≤0.95)\mathbf{P}(S\_{1,T}\leq 0.95,S\_{2,T}\leq 0.95), by projecting the payoff

|  |  |  |
| --- | --- | --- |
|  | 𝟙​(S1,T≤0.95)​𝟙​(S2,T≤0.95)\mathds{1}\left(S\_{1,T}\leq 0.95\right)\mathds{1}\left(S\_{2,T}\leq 0.95\right) |  |

onto the basis functions. The bottom panels of Figure [3](https://arxiv.org/html/2601.14852v1#S5.F3 "Figure 3 ‣ 5.2 Multivariate projection for exchange rates ‣ 5 Simulation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") report fitted versus true probabilities. The estimates line up closely with the 45∘45^{\circ} line—albeit slightly less tightly than for the correlation results—indicating that the projection method recovers joint tail probabilities with high accuracy.

![Refer to caption](x8.png)


(a) Multivariate normal

![Refer to caption](x9.png)


(b) Nonlinear dependence

![Refer to caption](x10.png)


(c) Multivariate normal

![Refer to caption](x11.png)


(d) Nonlinear dependence

Figure 3: Estimated correlation and joint tail risk in exchange-rate markets.
Each point is one of 1,000 Monte Carlo simulations. Top: true correlation versus its projection-based estimate. Bottom: true joint left-tail probability 𝐏​(S1,T≤0.95,S2,T≤0.95)\mathbf{P}(S\_{1,T}\leq 0.95,S\_{2,T}\leq 0.95) versus its projection-based estimate.

### 5.3 Multivariate projection for sector ETFs

Finally, we evaluate the covariance estimator in ([4.3](https://arxiv.org/html/2601.14852v1#S4.Ex50 "4.3 Projection and equicorrelation ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) for the eleven sector ETFs using a simple factor structure under the risk-neutral measure. Let X∈ℝ11X\in\mathbb{R}^{11} denote log-returns and R=exp⁡(X)R=\exp(X) the corresponding gross returns. We simulate

|  |  |  |
| --- | --- | --- |
|  | X=B​f+ε,f∼𝖭​(0,diag⁡(σ1,f2,σ2,f2)),ε∼𝖭​(0,diag⁡(σ12,…,σ112)),f⟂ε,X=Bf+\varepsilon,\qquad f\sim\mathsf{N}\!\bigl(0,\operatorname{diag}(\sigma\_{1,f}^{2},\sigma\_{2,f}^{2})\bigr),\quad\varepsilon\sim\mathsf{N}\!\bigl(0,\operatorname{diag}(\sigma\_{1}^{2},\ldots,\sigma\_{11}^{2})\bigr),\quad f\perp\varepsilon, |  |

with B∈ℝ11×2B\in\mathbb{R}^{11\times 2}. Hence

|  |  |  |
| --- | --- | --- |
|  | 𝐕𝐚𝐫tQ​(X)=B​diag⁡(σ12,σ22)​B′+diag⁡(σ12,…,σ112).\mathbf{Var}\_{t}^{Q}(X)\;=\;B\,\operatorname{diag}(\sigma\_{1}^{2},\sigma\_{2}^{2})\,B^{\prime}\;+\;\operatorname{diag}(\sigma\_{1}^{2},\ldots,\sigma\_{11}^{2}). |  |

The factor structure captures systematic risk and cross-sectional correlation. We set the gross-return means to one and winsorize RR at [0.4, 1.5][0.4,\,1.5] componentwise. Entries of BB are drawn iid from 𝖴𝗇𝗂𝖿​[−0.4,1]\mathsf{Unif}[-0.4,1].

We run 1,000 Monte Carlo simulations. In each run we compute the mean squared error (MSE) between the vector of true pairwise correlations and the estimated correlations. As a benchmark, we include the equicorrelation estimator. Table [1](https://arxiv.org/html/2601.14852v1#S5.T1 "Table 1 ‣ 5.3 Multivariate projection for sector ETFs ‣ 5 Simulation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") reports summary statistics: the projection-based estimator attains lower MSE across the distribution. We also report the correlation between the true correlation vector and the projection-based estimate within each run; the average is about 20%, indicating that the projection approach captures meaningful cross-sectional heterogeneity. By construction, the equicorrelation estimator does not capture such heterogeneity, as it imposes a common correlation across all pairs.

|  | Min | Median | Max | Mean | Std. dev. |
| --- | --- | --- | --- | --- | --- |
| Equicorrelation | 0.0231 | 0.1361 | 0.3860 | 0.1436 | 0.0472 |
| Projection correlation | 0.0253 | 0.1259 | 0.3312 | 0.1284 | 0.0408 |

Table 1: Summary statistics of MSE. This table summarizes, across 1,000 Monte Carlo simulations, the distribution of the MSE for the equicorrelation estimator and the projection-based correlation estimator in ([4.3](https://arxiv.org/html/2601.14852v1#S4.Ex50 "4.3 Projection and equicorrelation ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")).

## 6 Empirical application

### 6.1 Empirical estimates of SVIX and VIX

According to the simulation results, the projection approach compares favorably to the CM formula especially when the number of observed option prices is small. When the number of observed options is large it is a priori not so clear whether a more refined approximation yields economically different results. To investigate the benefits of the projection approach in the latter case, we estimate the SVIX and VIX from Examples [1](https://arxiv.org/html/2601.14852v1#Thmexmp1 "Example 1 (Risk-neutral variance (SVIX)). ‣ 2.1 Carr-Madan approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")–[2](https://arxiv.org/html/2601.14852v1#Thmexmp2 "Example 2 (Risk-neutral entropy (VIX)). ‣ 2.1 Carr-Madan approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") using both methods. The calculation of both indexes requires options on the S&P500, which is one of the most liquid option markets worldwide. The SVIX and VIX thus stand a natural test case.

The options data on the SP500 are coming from OptionMetrics and span the period January 4, 1996 until July 20, 2023. Several data cleaning procedures are applied before each volatility index is calculated. The procedure is almost identical to CBOE’s method when it calculates the VIX. A detailed description of our procedure is included in Appendix [B](https://arxiv.org/html/2601.14852v1#A2 "Appendix B Option data preprocessing ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").

First, consider the SVIX defined by

|  |  |  |  |
| --- | --- | --- | --- |
|  | SVIXt→T2=1T−t​𝐕𝐚𝐫tQ​(Rt→TRf,t→T).\mathrm{SVIX}\_{t\to T}^{2}=\frac{1}{T-t}\mathbf{Var}\_{t}^{Q}\left(\frac{R\_{t\to T}}{R\_{f,t\to T}}\right). |  | (17) |

[[47](https://arxiv.org/html/2601.14852v1#bib.bib67 "What is the expected return on the market?")] derives conditions under which the conditional equity premium satisfies

|  |  |  |
| --- | --- | --- |
|  | 1T−t​(𝐄t​Rt→T−Rf,t→T)≥Rf,t→T​SVIXt→T2.\frac{1}{T-t}\left(\mathbf{E}\_{t}R\_{t\to T}-R\_{f,t\to T}\right)\geq R\_{f,t\to T}\mathrm{SVIX}\_{t\to T}^{2}. |  |

In fact, when running the regression

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1T−t​(𝐄t​Rt→T−Rf,t→T)=β0+β1​Rf,t→T​SVIXt→T2+εT,\frac{1}{T-t}\left(\mathbf{E}\_{t}R\_{t\to T}-R\_{f,t\to T}\right)=\beta\_{0}+\beta\_{1}R\_{f,t\to T}\mathrm{SVIX}\_{t\to T}^{2}+\varepsilon\_{T}, |  | (18) |

[[47](https://arxiv.org/html/2601.14852v1#bib.bib67 "What is the expected return on the market?"), [49](https://arxiv.org/html/2601.14852v1#bib.bib92 "Information in derivatives markets: forecasting prices with prices")] cannot reject the null hypothesis that β0=0\beta\_{0}=0 and β1=1\beta\_{1}=1, thus suggesting that the lower bound is tight. This conclusion is particularly interesting as it gives a model-free way to measure the equity premium in real time. Given its importance, we reassess this claim by using our projection method to measure SVIXt→T2\mathrm{SVIX}\_{t\to T}^{2}. Table [2](https://arxiv.org/html/2601.14852v1#S6.T2 "Table 2 ‣ 6.1 Empirical estimates of SVIX and VIX ‣ 6 Empirical application ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") shows the results. For each prediction horizon, the difference between the CM and projection method are very small, suggesting that in very liquid option markets it is immaterial which method is used.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | 30 days | | 90 days | | 180 days | |
|  | Projection | CM | Projection | CM | Projection | CM |
| β0\beta\_{0} | 0.002(0.0407)\underset{(0.0407)}{0.002} | 0.005(0.0400)\underset{(0.0400)}{0.005} | −0.002(0.0512)\underset{(0.0512)}{-0.002} | −0.005(0.0504)\underset{(0.0504)}{-0.005} | −0.046(0.0361)\underset{(0.0361)}{-0.046} | −0.052(0.0365)\underset{(0.0365)}{-0.052} |
| β1\beta\_{1} | 1.434(1.0160)\underset{(1.0160)}{1.434} | 1.493(1.0816)\underset{(1.0816)}{1.493} | 1.395(1.2693)\underset{(1.2693)}{1.395} | 1.589(1.3602)\underset{(1.3602)}{1.589} | 2.455(0.7914)\underset{(0.7914)}{2.455} | 2.865(0.8371)\underset{(0.8371)}{2.865} |
| R2R^{2} (%) | 1.12 | 1.08 | 2.09 | 2.35 | 6.91 | 7.94 |
| # obs | 6932 | 6932 | 6865 | 6865 | 6745 | 6745 |

Table 2: Equity premium regression. This table reports estimates from regression ([18](https://arxiv.org/html/2601.14852v1#S6.E18 "In 6.1 Empirical estimates of SVIX and VIX ‣ 6 Empirical application ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) for return horizons of 30, 90, and 180 days. Newey–West standard errors, using a bandwidth equal to the number of trading days in the horizon, are reported in parentheses below the coefficients.

In addition to SVIX, we also estimate the VIX. Figure [4](https://arxiv.org/html/2601.14852v1#S6.F4 "Figure 4 ‣ 6.1 Empirical estimates of SVIX and VIX ‣ 6 Empirical application ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") plots the time series of the difference between the two VIX estimates; the solid orange line is its 60-day moving average, which remains positive throughout, consistent with the simulation. The largest gaps occur early in the sample when option coverage is sparser. We mark the 20 largest differences with blue dots, which can reach close to 8 percentage points. Such a gap is economically significant: portfolios with hundreds of VIX futures contracts can experience multi-million-dollar P&L swings. The single largest peak occurs on March 2, 2009, at the height of the global financial crisis. On that day, the projection-implied VIX is 52%, while the CM approximation yields 44%. During periods of heightened uncertainty, risk-neutral mass shifts to the left tail, which amplifies entropy because log⁡(x)\log(x) decays steeply near zero (see ([4](https://arxiv.org/html/2601.14852v1#S2.E4 "In Example 2 (Risk-neutral entropy (VIX)). ‣ 2.1 Carr-Madan approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"))). In such episodes the CM method—linearized around the risk-free rate–—can be inaccurate, whereas the projection method remains reliable because it approximates log⁡(x)\log(x) well over the entire domain. In line with this intuition, the largest measurement differences cluster around the dot-com bust (2000), the global financial crisis (2008), and COVID-19 (2020).

![Refer to caption](x12.png)


Figure 4: VIX estimate. This figure shows the projection VIX estimate minus the VIX estimate obtained by CM. The solid orange line denotes the 60-day moving average of this difference. The blue dots indicate the 20 largest observed differences.

### 6.2 Dependence in FX forward returns

This section estimates risk-neutral correlations using the method of Section [4.4](https://arxiv.org/html/2601.14852v1#S4.SS4 "4.4 Completeness in FX markets ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") in the FX setting.

#### 6.2.1 Data collection

From Bloomberg we obtain daily end-of-day composite (OTC) quotes for money-market deposit rates at 1 month EUR, USD and GBP. We also retrieve daily spot FX rates and construct 1 month forwards for EUR/USD, GBP/USD and EUR/GBP via covered interest parity.

For FX options, we use Bloomberg’s OTC constant-maturity implied volatilities at 1M and 3M. Each day we observe the standard smile pillars: the ATM delta-neutral volatility and the 10- and 25-delta risk reversals (RR) and butterflies (BF), quoted under the spot-delta, premium-included convention. When fixed-delta call/put vols are not directly provided, we recover them from ATM, RR and BF via the standard identities. We then map quotes to strikes and compute option prices using the Garman–Kohlhagen model, the reference model with respect to which the implied volatilities are quoted.151515Using the Garman–Kohlhagen formula in this step simply converts implied volatilities into option prices and does not impose Garman–Kohlhagen as the true pricing model. Our sample spans July 2008 to April 2023 and contains 3,721 trading days. Finally, returns on each currency are defined relative to the forward price: Ri,t→T=Si,T/Fi,t→TR\_{i,t\to T}=S\_{i,T}/F\_{i,t\to T}. Thus, by construction, 𝐄tQ​Ri,t→T=1\mathbf{E}\_{t}^{Q}R\_{i,t\to T}=1.

#### 6.2.2 Correlation estimates

Panel [5(a)](https://arxiv.org/html/2601.14852v1#S6.F5.sf1 "In Figure 5 ‣ 6.2.2 Correlation estimates ‣ 6.2 Dependence in FX forward returns ‣ 6 Empirical application ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") reports the 1-month forward-looking risk-neutral correlation between the EUR/USD and GBP/USD exchange rates. As expected, almost all estimates lie below one; the few instances slightly above one are consistent with small measurement noise, as in our simulations. The sample-average correlation is about 0.7, in line with the view that major exchange rates co-move due to a handful of common risk factors. The lowest estimate–about 0.2–occurs just before the Brexit referendum, on June 9–10, 2016. Panel [5(b)](https://arxiv.org/html/2601.14852v1#S6.F5.sf2 "In Figure 5 ‣ 6.2.2 Correlation estimates ‣ 6.2 Dependence in FX forward returns ‣ 6 Empirical application ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") indicates that the decline in correlation is driven primarily by a sharp increase in GBP/USD volatility.

The high frequency of option quotes also lets us zoom in on short-lived episodes. One stands out: a sharp decline in the 1-month risk-neutral correlation between December 12, 2012 and February 14, 2013, from nearly one to roughly 0.4. As the right panel of Figure [5](https://arxiv.org/html/2601.14852v1#S6.F5 "Figure 5 ‣ 6.2.2 Correlation estimates ‣ 6.2 Dependence in FX forward returns ‣ 6 Empirical application ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") shows, this drop was not accompanied by a spike in the (annualized) volatilities, pointing to a genuine change in dependence rather than a level-volatility effect. Several contemporaneous developments are consistent with this interpretation: unexpectedly weak UK Q4-2012 GDP (weighing on GBP) alongside improving euro-area conditions such as the tightening peripheral spreads and the first LTRO repayments, which would have supported EUR. We therefore view this episode as a period in which currency-specific risks dominated shared USD drivers, temporarily depressing the implied correlation.

![Refer to caption](x13.png)


(a) Correlation

![Refer to caption](x14.png)


(b) Volatility

![Refer to caption](x15.png)


(c) Joint crash probability

![Refer to caption](x16.png)


(d) Joint crash probability (smoothed)

Figure 5: Daily risk-neutral correlation, volatility, and crash risk (30-day horizon).
Panels (a)–(d) plot: (a) the 30-day risk-neutral correlation between EUR/USD and GBP/USD;
(b) the corresponding annualized 30-day risk-neutral standard deviations for each exchange rate;
(c) the 30-day joint crash probability under independence (pEUR​pGBPp\_{\text{EUR}}\,p\_{\text{GBP}}) and under the option-implied dependence structure;
(d) the option-implied (dependent) crash probability alongside the physical crash probability estimated from OLS. The estimates in this last panel are smoothed using a 30-day moving average.

#### 6.2.3 Tail probability estimates

Second, we examine the joint risk-neutral crash probability, defined as the probability that both EUR/USD and GBP/USD monthly returns are less than 3%. The estimate from our projection approach is shown in red in Panel [5(c)](https://arxiv.org/html/2601.14852v1#S6.F5.sf3 "In Figure 5 ‣ 6.2.2 Correlation estimates ‣ 6.2 Dependence in FX forward returns ‣ 6 Empirical application ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") (labeled “dependent”). For comparison, we also plot the independence benchmark (labeled “independent”), obtained by multiplying the estimated marginal crash probabilities. The figure shows that accounting for dependence is crucial: the joint (dependent) probability is typically well above the independence benchmark, especially during periods of market stress.

To evaluate the informativeness of the joint risk-neutral crash probability, we estimate the forecasting model

|  |  |  |  |
| --- | --- | --- | --- |
|  | Crasht→T=β0+β1​RiskNeutralProbt→T+εt→T,\texttt{Crash}\_{t\to T}=\beta\_{0}+\beta\_{1}\texttt{RiskNeutralProb}\_{t\to T}+\varepsilon\_{t\to T}, |  | (19) |

where CrashT=𝟙​(R1,t→T≤0.97)​𝟙​(R2,t→T≤0.97)\texttt{Crash}\_{T}=\mathds{1}\left(R\_{1,t\to T}\leq 0.97\right)\mathds{1}\left(R\_{2,t\to T}\leq 0.97\right). The regressor is either the dependent (option-implied) joint crash probability or the independence benchmark (product of marginal crash probabilities). Results appear in Table [3](https://arxiv.org/html/2601.14852v1#S6.T3 "Table 3 ‣ 6.2.3 Tail probability estimates ‣ 6.2 Dependence in FX forward returns ‣ 6 Empirical application ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"). The dependent joint probability is a significant predictor, and the associated R2R^{2} is substantially larger than for the independence benchmark. If physical and risk-neutral crash probabilities coincided at each date, the restriction [β0,β1]=[0,1][\beta\_{0},\beta\_{1}]=[0,1] would hold; the bottom row reports the pp-value of this Wald test, which is not rejected only for the dependent regressor. We also report an out-of-sample R2R^{2}, RO​O​S2R\_{OOS}^{2}, defined as

|  |  |  |
| --- | --- | --- |
|  | RO​O​S2=1−∑T(Crasht→T−Crash^t→T)2∑T(Crasht→T−Crash¯t→T)2,R\_{OOS}^{2}=1-\frac{\sum\_{T}(\texttt{Crash}\_{t\to T}-\widehat{\texttt{Crash}}\_{t\to T})^{2}}{\sum\_{T}(\texttt{Crash}\_{t\to T}-\overline{\texttt{Crash}}\_{t\to T})^{2}}, |  |

where forecasts are Crash^t→T=RiskNeutralProbt→T\widehat{\texttt{Crash}}\_{t\to T}=\texttt{RiskNeutralProb}\_{t\to T}, and Crash¯t→T\overline{\texttt{Crash}}\_{t\to T} is the historical prevailing crash probability computed using an expanding window that begins after 1,000 historical observations are available. This design avoids any in-sample bias and yields a strict out-of-sample evaluation. In both specifications RO​O​S2R\_{OOS}^{2} is positive, with larger values when using the dependent covariate, indicating that risk-neutral probabilities outperform the prevailing-mean benchmark.

The last column of Table [3](https://arxiv.org/html/2601.14852v1#S6.T3 "Table 3 ‣ 6.2.3 Tail probability estimates ‣ 6.2 Dependence in FX forward returns ‣ 6 Empirical application ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") includes both predictors; the incremental R2R^{2} gain is modest, and the coefficient on the independence benchmark enters with the opposite sign. We conclude that the option-implied (dependent) joint crash probability performs markedly better, providing evidence that it helps forecast joint physical tail risk.

Panel [5(d)](https://arxiv.org/html/2601.14852v1#S6.F5.sf4 "In Figure 5 ‣ 6.2.2 Correlation estimates ‣ 6.2 Dependence in FX forward returns ‣ 6 Empirical application ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") plots the inferred physical joint crash probability based on the regression with the dependent (option-implied) covariate, alongside the risk-neutral series; both are smoothed for readability. The figure illustrates a time-varying premium for joint crash risk. During turbulent periods (e.g., the Global Financial Crisis), the risk-neutral probability exceeds the physical estimate, consistent with a positive compensation for bearing joint tail risk. In contrast, in calmer markets the ordering often reverses—the physical probability exceeds the risk-neutral one—suggesting that currency exposures may provide a hedging benefit and earn a negative tail-risk premium. Overall, the evidence points to currencies serving as tail-risk hedges in normal times, but commanding compensation during stress episodes.

This evidence is consistent with the structural explanation of [[46](https://arxiv.org/html/2601.14852v1#bib.bib122 "Countercyclical currency risk premia")].
They argue that, in times of stress when the marginal utility of wealth is high, U.S. investors
who are long foreign currencies are exposed to the risk that the dollar appreciates.
Consequently, the conditional expected return on such a strategy should be high.
In contrast, during normal times the strategy behaves more like a hedge: investors bear the risk
of a dollar depreciation following a positive shock to the U.S. pricing kernel, so the conditional expected return is low or even negative.

|  |  |  |  |
| --- | --- | --- | --- |
|  | (1) | (2) | (3) |
| Constant (β0)(\beta\_{0}) | 0.042(0.0171)\underset{(0.0171)}{0.042} | 0.032(0.0182)\underset{(0.0182)}{0.032} | 0.031(0.0178)\underset{(0.0178)}{0.031} |
| Independent | 1.350(0.8585)\underset{(0.8585)}{1.350} |  | −1.380(1.8274)\underset{(1.8274)}{-1.380} |
| Dependent |  | 0.652(0.3497)\underset{(0.3497)}{0.652} | 1.176(0.7555)\underset{(0.7555)}{1.176} |
| R2R^{2}(%) | 0.94 | 1.33 | 1.45 |
| RO​O​S2R\_{OOS}^{2}(%) | 2.70 | 3.75 |  |
| pp-value (const=0=0, slope=1=1) | 0.00 | 0.16 |  |

Table 3: OLS estimates of ([19](https://arxiv.org/html/2601.14852v1#S6.E19 "In 6.2.3 Tail probability estimates ‣ 6.2 Dependence in FX forward returns ‣ 6 Empirical application ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")). Each column reports a different forecasting model. Newey–West standard errors (20 trading-day lag) are shown beneath the coefficients. The bottom row reports the pp-value of the Wald test on the joint restriction [β0,β1]=[0,1][\beta\_{0},\beta\_{1}]=[0,1].

## 7 Conclusion

This paper introduces a new approach to estimating risk-neutral expectations from option prices. The core idea is to project the target payoff function onto the space spanned by observed option payoffs and the underlying asset. Like the method of [[20](https://arxiv.org/html/2601.14852v1#bib.bib66 "Towards a theory of volatility trading")], the resulting estimate is a linear combination of option prices and the underlying. However, the projection approach makes optimal use of the available strike prices to minimize the approximation error. We show that this method much better finite sample properties. Simulation results confirm this advantage: the projection method delivers approximation errors that are orders of magnitude smaller.

We extend the projection approach to higher dimensions and, using approximation-theoretic tools (ridge functions), derive necessary and sufficient conditions under which simple options complete multiple asset markets. Although these conditions are rarely satisfied exactly in practice, we show that projection still estimates joint risk-neutral expectations robustly—most notably for risk-neutral covariances/correlations in the FX setting. Thus, projection provides a unified framework for estimating risk-neutral quantities not only for a single asset but also in the multi-asset case.

In our first empirical application, we revisit the regression of [[47](https://arxiv.org/html/2601.14852v1#bib.bib67 "What is the expected return on the market?")], which relates expected returns to SVIX. Because SVIX is computed from a large cross-section of option prices, the CM and projection methods yield similar estimates, and the regression results are similar. However, we do find notable differences in the estimated VIX: the projection method can diverge from the CBOE’s value by as much as 88 percentage points, reflecting sensitivity to the choice of approximation method.

The second application, FX, provides a clean setting for multivariate estimation.
In simulations, the projection estimator recovers the true correlation with near-zero error.
In the data, we estimate the conditional 1-month risk-neutral correlation between EUR/USD and
GBP/USD returns, which averages around 0.7. Thanks to the high frequency and forward-looking
nature of option quotes, we detect a notable shift in this correlation at the end of 2012.
We interpret this as a genuine change in dependence: bearish U.K. news contrasted with more
bullish euro-area developments that temporarily weakened the co-movement between the two USD majors.

Relatedly, we also estimate the joint risk-neutral crash probability and find that it forecasts
future realized crashes. Furthermore, when comparing the risk-neutral crash probability to the
physical probability inferred from an OLS regression, we find that the risk-neutral probability
is higher during crises but generally lower outside these periods. We interpret this as
data-driven evidence that U.S. investors in portfolios of foreign currencies demand crash
compensation in bad times, but value these positions as a hedge in normal market conditions.

{refcontext}

[sorting=nyt]

## References

* [1]
  Y. Aït-Sahalia and A. W. Lo (1998)
  Nonparametric estimation of state-price densities implicit in financial asset prices.
  Journal of Finance 53 (2),  pp. 499–547.
  External Links: [Document](https://dx.doi.org/10.1111/0022-1082.215228)
  Cited by: [footnote 2](https://arxiv.org/html/2601.14852v1#footnote2 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [2]
  Y. Aït-Sahalia and A. W. Lo (2000)
  Nonparametric risk management and implied risk aversion.
  Journal of Econometrics 94 (1-2),  pp. 9–51.
  External Links: [Document](https://dx.doi.org/10.1016/S0304-4076%2899%2900016-0)
  Cited by: [footnote 2](https://arxiv.org/html/2601.14852v1#footnote2 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [3]
  C. Almeida and G. Freire (2022)
  Pricing of index options in incomplete markets.
  Journal of Financial Economics 144 (1),  pp. 174–205.
  External Links: [Document](https://dx.doi.org/10.1016/j.jfineco.2021.05.041)
  Cited by: [footnote 2](https://arxiv.org/html/2601.14852v1#footnote2 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [4]
  T. G. Andersen, N. Fusari, and V. Todorov (2017)
  Short-term market risks implied by weekly options.
  Journal of Finance 72 (3),  pp. 1335–1386.
  External Links: [Document](https://dx.doi.org/10.1111/jofi.12486)
  Cited by: [footnote 1](https://arxiv.org/html/2601.14852v1#footnote1 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [5]
  K. Back (2017)
  Asset pricing and portfolio choice theory.
  second edition, Oxford University Press.
  Cited by: [§3.1](https://arxiv.org/html/2601.14852v1#S3.SS1.p3.1 "3.1 Market completeness ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [6]
  G. Bakshi, N. Kapadia, and D. Madan (2003)
  Stock return characteristics, skew laws, and the differential pricing of individual equity options.
  Review of Financial Studies 16 (1),  pp. 101–143.
  External Links: [Document](https://dx.doi.org/10.1093/rfs/16.1.0101)
  Cited by: [footnote 1](https://arxiv.org/html/2601.14852v1#footnote1 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [7]
  D. S. Bates (1991)
  The crash of ’87: was it expected? evidence from options markets.
  Journal of Finance 46 (3),  pp. 1009–1044.
  External Links: [Document](https://dx.doi.org/10.1111/j.1540-6261.1991.tb03775.x)
  Cited by: [footnote 1](https://arxiv.org/html/2601.14852v1#footnote1 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [8]
  B. K. Beare and L. D. W. Schmidt (2016)
  An empirical test of pricing kernel monotonicity.
  Journal of Applied Econometrics 31 (2),  pp. 338–356.
  Cited by: [footnote 2](https://arxiv.org/html/2601.14852v1#footnote2 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [9]
  P. Billingsley (1999)
  Convergence of probability measures.
  second edition, John Wiley & Sons.
  Cited by: [§A.3](https://arxiv.org/html/2601.14852v1#A1.SS3.1.p1.10 "Proof. ‣ A.3 Proof of Corollary 1 ‣ Appendix A Proofs ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [10]
  F. Black and M. Scholes (1973)
  The pricing of options and corporate liabilities.
  Journal of Political Economy 81 (3),  pp. 637–654.
  External Links: [Document](https://dx.doi.org/10.1086/260062)
  Cited by: [Appendix C](https://arxiv.org/html/2601.14852v1#A3.p1.8 "Appendix C Details on simulation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [§5.1](https://arxiv.org/html/2601.14852v1#S5.SS1.p2.2 "5.1 Univariate projection ‣ 5 Simulation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [11]
  R. R. Bliss and N. Panigirtzoglou (2004)
  Option-implied risk aversion estimates.
  Journal of Finance 59 (1),  pp. 407–446.
  External Links: [Document](https://dx.doi.org/10.1111/j.1540-6261.2004.00637.x)
  Cited by: [footnote 2](https://arxiv.org/html/2601.14852v1#footnote2 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [12]
  T. Bollerslev, G. Tauchen, and H. Zhou (2009)
  Expected stock returns and variance risk premia.
  Review of Financial Studies 22 (11),  pp. 4463–4492.
  External Links: [Document](https://dx.doi.org/10.1093/rfs/hhp008)
  Cited by: [footnote 1](https://arxiv.org/html/2601.14852v1#footnote1 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [13]
  O. Bondarenko and C. Bernard (2024)
  Option-implied dependence and correlation risk premium.
  Journal of Financial and Quantitative Analysis 59 (7),  pp. 3139–3189.
  External Links: [Document](https://dx.doi.org/10.1017/S0022109023000960)
  Cited by: [footnote 3](https://arxiv.org/html/2601.14852v1#footnote3 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [footnote 4](https://arxiv.org/html/2601.14852v1#footnote4 "In Example 4 (Risk-neutral covariance and correlation). ‣ 2.1 Carr-Madan approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [14]
  O. Bondarenko (2003)
  Estimation of risk-neutral densities using positive convolution approximation.
  Journal of Econometrics 116 (1),  pp. 85–112.
  External Links: [Document](https://dx.doi.org/10.1016/S0304-4076%2803%2900104-0)
  Cited by: [footnote 2](https://arxiv.org/html/2601.14852v1#footnote2 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [15]
  D. T. Breeden and R. H. Litzenberger (1978)
  Prices of state-contingent claims implicit in option prices.
  Journal of Business,  pp. 621–651.
  Cited by: [§1](https://arxiv.org/html/2601.14852v1#S1.p6.1 "1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [§3.1](https://arxiv.org/html/2601.14852v1#S3.SS1.p4.1 "3.1 Market completeness ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [Example 3](https://arxiv.org/html/2601.14852v1#Thmexmp3.p1.1 "Example 3 (Risk-neutral distribution). ‣ 2.1 Carr-Madan approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [Example 4](https://arxiv.org/html/2601.14852v1#Thmexmp4.p2.1 "Example 4 (Risk-neutral covariance and correlation). ‣ 2.1 Carr-Madan approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [footnote 2](https://arxiv.org/html/2601.14852v1#footnote2 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [16]
  M. Britten-Jones and A. Neuberger (2000)
  Option prices, implied price processes, and stochastic volatility.
  Journal of Finance 55 (2),  pp. 839–866.
  External Links: [Document](https://dx.doi.org/10.1111/0022-1082.00228)
  Cited by: [Example 2](https://arxiv.org/html/2601.14852v1#Thmexmp2.p1.5 "Example 2 (Risk-neutral entropy (VIX)). ‣ 2.1 Carr-Madan approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [footnote 1](https://arxiv.org/html/2601.14852v1#footnote1 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [17]
  M. Broadie, M. Chernov, and M. Johannes (2007)
  Model specification and risk premia: evidence from futures options.
  Journal of Finance 62 (3),  pp. 1453–1490.
  External Links: [Document](https://dx.doi.org/10.1111/j.1540-6261.2007.01241.x)
  Cited by: [Appendix C](https://arxiv.org/html/2601.14852v1#A3.p1.7 "Appendix C Details on simulation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [18]
  E. J. Candès, J. Romberg, and T. Tao (2006)
  Robust uncertainty principles: exact signal reconstruction from highly incomplete frequency information.
  IEEE Transactions on Information Theory 52 (2),  pp. 489–509.
  Cited by: [§1](https://arxiv.org/html/2601.14852v1#S1.p9.3 "1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [19]
  C. Canuto, M. Y. Hussaini, A. Quarteroni, and T. A. Zang (2006)
  Spectral methods: fundamentals in single domains.
   Springer.
  Cited by: [§3.2](https://arxiv.org/html/2601.14852v1#S3.SS2.p1.1 "3.2 Convergence rate ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [20]
  P. Carr and D. Madan (2001)
  Towards a theory of volatility trading.
  In Handbooks in Mathematical Finance: Option Pricing, Interest Rates and Risk Management,
   pp. 458–476.
  Cited by: [§1](https://arxiv.org/html/2601.14852v1#S1.p1.1 "1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [§2.4](https://arxiv.org/html/2601.14852v1#S2.SS4.p4.5 "2.4 Continuous-state limit ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [§2](https://arxiv.org/html/2601.14852v1#S2.p1.1 "2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [§7](https://arxiv.org/html/2601.14852v1#S7.p1.1 "7 Conclusion ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [footnote 1](https://arxiv.org/html/2601.14852v1#footnote1 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [21]
  P. Carr and L. Wu (2009)
  Variance risk premiums.
  Review of Financial Studies 22 (3),  pp. 1311–1341.
  External Links: [Document](https://dx.doi.org/10.1093/rfs/hhn038)
  Cited by: [footnote 1](https://arxiv.org/html/2601.14852v1#footnote1 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [22]
  F. Chabi-Yo and J. Loudis (2020)
  The conditional expected market return.
  Journal of Financial Economics 137 (3),  pp. 752–786.
  External Links: [Document](https://dx.doi.org/10.1016/j.jfineco.2020.03.009)
  Cited by: [footnote 1](https://arxiv.org/html/2601.14852v1#footnote1 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [23]
  M. Chernov, J. Graveline, and I. Zviadadze (2018)
  Crash risk in currency returns.
  Journal of Financial and Quantitative Analysis 53 (1),  pp. 137–170.
  Cited by: [§1](https://arxiv.org/html/2601.14852v1#S1.p11.4 "1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [24]
  V. Chernozhukov, I. Fernández-Val, and A. Galichon (2009)
  Improving point and interval estimators of monotone functions by rearrangement.
  Biometrika 96 (3),  pp. 559–575.
  External Links: [Document](https://dx.doi.org/10.1093/biomet/asp030)
  Cited by: [§3.3](https://arxiv.org/html/2601.14852v1#S3.SS3.p4.1 "3.3 Estimation of the risk-neutral CDF and PDF ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [25]
  V. Chernozhukov, I. Fernández-Val, and B. Melly (2013)
  Inference on counterfactual distributions.
  Econometrica 81 (6),  pp. 2205–2268.
  Cited by: [§3.3](https://arxiv.org/html/2601.14852v1#S3.SS3.p4.1 "3.3 Estimation of the risk-neutral CDF and PDF ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [26]
  C. de Boor (2001)
  A practical guide to splines.
  Revised edition, Applied Mathematical Sciences, Vol. 27, Springer-Verlag.
  Cited by: [§A.6](https://arxiv.org/html/2601.14852v1#A1.SS6.2.p2.10 "Proof. ‣ A.6 Proof of Proposition 5 ‣ Appendix A Proofs ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [§A.7](https://arxiv.org/html/2601.14852v1#A1.SS7.1.p1.3 "Proof. ‣ A.7 Proof of Proposition 6 ‣ Appendix A Proofs ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [27]
  P. Diaconis and M. Shahshahani (1984)
  On nonlinear functions of linear combinations.
  SIAM Journal on Scientific and Statistical Computing 5 (1),  pp. 175–191.
  Cited by: [§4.2](https://arxiv.org/html/2601.14852v1#S4.SS2.p3.1 "4.2 Identification of risk-neutral covariances and correlations ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [28]
  M. Embree (2010)
  Numerical analysis i.
  Note: Lecture notes, Rice UniversityPages 1–207
  Cited by: [§A.4](https://arxiv.org/html/2601.14852v1#A1.SS4.1.p1.3 "Proof. ‣ A.4 Proof of Proposition 3 ‣ Appendix A Proofs ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [29]
  R. F. Engle and B. Kelly (2012)
  Dynamic equicorrelation.
  Journal of Business & Economic Statistics 30 (2),  pp. 212–228.
  Cited by: [§4.3](https://arxiv.org/html/2601.14852v1#S4.SS3.p2.2 "4.3 Projection and equicorrelation ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [30]
  B. Eraker, M. Johannes, and N. Polson (2003)
  The impact of jumps in volatility and returns.
  Journal of Finance 58 (3),  pp. 1269–1300.
  External Links: [Document](https://dx.doi.org/10.1111/1540-6261.00566)
  Cited by: [Appendix C](https://arxiv.org/html/2601.14852v1#A3.p1.8 "Appendix C Details on simulation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [§5.1](https://arxiv.org/html/2601.14852v1#S5.SS1.p2.2 "5.1 Univariate projection ‣ 5 Simulation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [31]
  S. Figlewski (2010-03)
  Estimating the implied risk‐neutral density for the us market portfolio.
  In Volatility and Time Series Econometrics: Essays in Honor of Robert Engle,
  External Links: [Document](https://dx.doi.org/10.1093/acprof%3Aoso/9780199549498.003.0015)
  Cited by: [footnote 2](https://arxiv.org/html/2601.14852v1#footnote2 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [32]
  S. Figlewski (2018)
  Risk-neutral densities: a review.
  Annual Review of Financial Economics 10 (1),  pp. 329–359.
  External Links: [Document](https://dx.doi.org/10.1146/annurev-financial-110217-022944)
  Cited by: [footnote 2](https://arxiv.org/html/2601.14852v1#footnote2 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [33]
  D. Filipović, E. Mayerhofer, and P. Schneider (2013)
  Density approximations for multivariate affine jump-diffusion processes.
  Journal of Econometrics 176 (2),  pp. 93–111.
  External Links: [Document](https://dx.doi.org/j.jeconom.2012.12.003)
  Cited by: [footnote 2](https://arxiv.org/html/2601.14852v1#footnote2 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [34]
  J. H. Friedman and W. Stuetzle (1981)
  Projection pursuit regression.
  Journal of the American Statistical Association 76 (376),  pp. 817–823.
  Cited by: [§1](https://arxiv.org/html/2601.14852v1#S1.p8.3 "1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [35]
  B. E. Hansen (2022)
  Econometrics.
   Princeton University Press.
  Cited by: [§3.2](https://arxiv.org/html/2601.14852v1#S3.SS2.p4.1 "3.2 Convergence rate ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [36]
  J. C. Jackwerth and M. Rubinstein (1996)
  Recovering probability distributions from option prices.
  Journal of Finance 51 (5),  pp. 1611–1631.
  Cited by: [footnote 2](https://arxiv.org/html/2601.14852v1#footnote2 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [37]
  J. C. Jackwerth (2000)
  Recovering risk aversion from option prices and realized returns.
  Review of Financial Studies 13 (2),  pp. 433–451.
  Cited by: [footnote 2](https://arxiv.org/html/2601.14852v1#footnote2 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [38]
  G. J. Jiang and Y. S. Tian (2005)
  The model-free implied volatility and its information content.
  Review of Financial Studies 18 (4),  pp. 1305–1342.
  Cited by: [§1](https://arxiv.org/html/2601.14852v1#S1.p4.1 "1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [footnote 1](https://arxiv.org/html/2601.14852v1#footnote1 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [39]
  B. Kelly, H. Lustig, and S. Van Nieuwerburgh (2016)
  Too-systemic-to-fail: what option markets imply about sector-wide government guarantees.
  American Economic Review 106 (6),  pp. 1278–1319.
  External Links: [Document](https://dx.doi.org/10.1257/aer.20120389)
  Cited by: [§4](https://arxiv.org/html/2601.14852v1#S4.p4.5 "4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [40]
  R. Kozhan, A. Neuberger, and P. Schneider (2013)
  The skew risk premium in the equity index market.
  Review of Financial Studies 26 (9),  pp. 2174–2203.
  External Links: [Document](https://dx.doi.org/10.1093/rfs/hht039)
  Cited by: [footnote 1](https://arxiv.org/html/2601.14852v1#footnote1 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [41]
  L. Kremens and I. Martin (2019)
  The quanto theory of exchange rates.
  American Economic Review 109 (3),  pp. 810–843.
  External Links: [Document](https://dx.doi.org/10.1257/aer.20180019)
  Cited by: [footnote 1](https://arxiv.org/html/2601.14852v1#footnote1 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [footnote 16](https://arxiv.org/html/2601.14852v1#footnote16 "In B.1 ETF options and conversion of American option price ‣ Appendix B Option data preprocessing ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [footnote 4](https://arxiv.org/html/2601.14852v1#footnote4 "In Example 4 (Risk-neutral covariance and correlation). ‣ 2.1 Carr-Madan approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [42]
  H. Lebesgue (1898)
  Sur l’approximation des fonctions.
  Bulletin des Sciences Mathématiques 22 (10),  pp. 278–287.
  Cited by: [§A.2](https://arxiv.org/html/2601.14852v1#A1.SS2.p1.1 "A.2 Proof of Proposition 2 ‣ Appendix A Proofs ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [§3.1](https://arxiv.org/html/2601.14852v1#S3.SS1.p2.4 "3.1 Market completeness ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [43]
  O. Ledoit and M. Wolf (2003)
  Improved estimation of the covariance matrix of stock returns with an application to portfolio selection.
  Journal of Empirical Finance 10 (5),  pp. 603–621.
  External Links: [Document](https://dx.doi.org/10.1016/S0927-5398%2803%2900007-0)
  Cited by: [§D.1](https://arxiv.org/html/2601.14852v1#A4.SS1.p2.2 "D.1 ETF correlation ‣ Appendix D Correlations between sector ETFs and the market portfolio ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [44]
  V.Y. Lin and A. Pinkus (1993)
  Fundamentality of ridge functions.
  Journal of Approximation Theory 75 (3),  pp. 295–311.
  External Links: [Document](https://dx.doi.org/10.1006/jath.1993.1104)
  Cited by: [§A.10](https://arxiv.org/html/2601.14852v1#A1.SS10.p1.8 "A.10 Sufficient conditions for ridge representation and the proof of Proposition 9 ‣ Appendix A Proofs ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [§4.1](https://arxiv.org/html/2601.14852v1#S4.SS1.p2.7 "4.1 Identifying joint dependence from options on multiple portfolios ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [§4.2](https://arxiv.org/html/2601.14852v1#S4.SS2.p4.2 "4.2 Identification of risk-neutral covariances and correlations ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [Proposition 12](https://arxiv.org/html/2601.14852v1#Thmprop12 "Proposition 12 ([44]). ‣ A.10 Sufficient conditions for ridge representation and the proof of Proposition 9 ‣ Appendix A Proofs ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [45]
  M. Linn, S. Shive, and T. Shumway (2017-08)
  Pricing kernel monotonicity and conditional information.
  Review of Financial Studies 31 (2),  pp. 493–531.
  External Links: [Document](https://dx.doi.org/10.1093/rfs/hhx095)
  Cited by: [footnote 2](https://arxiv.org/html/2601.14852v1#footnote2 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [46]
  H. Lustig, N. Roussanov, and A. Verdelhan (2014)
  Countercyclical currency risk premia.
  Journal of Financial Economics 111 (3),  pp. 527–553.
  Cited by: [§6.2.3](https://arxiv.org/html/2601.14852v1#S6.SS2.SSS3.p5.1 "6.2.3 Tail probability estimates ‣ 6.2 Dependence in FX forward returns ‣ 6 Empirical application ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [Example 4](https://arxiv.org/html/2601.14852v1#Thmexmp4.p1.1 "Example 4 (Risk-neutral covariance and correlation). ‣ 2.1 Carr-Madan approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [47]
  I. Martin (2017)
  What is the expected return on the market?.
  Quarterly Journal of Economics 132 (1),  pp. 367–433.
  Cited by: [§3.3](https://arxiv.org/html/2601.14852v1#S3.SS3.p3.1 "3.3 Estimation of the risk-neutral CDF and PDF ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [§6.1](https://arxiv.org/html/2601.14852v1#S6.SS1.p3.3 "6.1 Empirical estimates of SVIX and VIX ‣ 6 Empirical application ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [§6.1](https://arxiv.org/html/2601.14852v1#S6.SS1.p3.5 "6.1 Empirical estimates of SVIX and VIX ‣ 6 Empirical application ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [§7](https://arxiv.org/html/2601.14852v1#S7.p3.1 "7 Conclusion ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [Example 1](https://arxiv.org/html/2601.14852v1#Thmexmp1.p1.5 "Example 1 (Risk-neutral variance (SVIX)). ‣ 2.1 Carr-Madan approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [Example 2](https://arxiv.org/html/2601.14852v1#Thmexmp2.p1.6 "Example 2 (Risk-neutral entropy (VIX)). ‣ 2.1 Carr-Madan approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [footnote 1](https://arxiv.org/html/2601.14852v1#footnote1 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [footnote 16](https://arxiv.org/html/2601.14852v1#footnote16 "In B.1 ETF options and conversion of American option price ‣ Appendix B Option data preprocessing ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [48]
  I. Martin (2018)
  Options and the gamma knife.
  Journal of Portfolio Management 44 (6),  pp. 47–55.
  External Links: [Document](https://dx.doi.org/10.3905/jpm.2018.44.6.047)
  Cited by: [§1](https://arxiv.org/html/2601.14852v1#S1.p7.1 "1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [§4.1](https://arxiv.org/html/2601.14852v1#S4.SS1.p3.5 "4.1 Identifying joint dependence from options on multiple portfolios ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [footnote 3](https://arxiv.org/html/2601.14852v1#footnote3 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [49]
  I. Martin (2025)
  Information in derivatives markets: forecasting prices with prices.
  Annual Review of Financial Economics.
  External Links: ISSN 1941-1367,
  [Document](https://dx.doi.org/10.1146/annurev-financial-082123-105811)
  Cited by: [§D.3](https://arxiv.org/html/2601.14852v1#A4.SS3.p5.4 "D.3 Conditional covariance and correlation estimates of the technology sector ‣ Appendix D Correlations between sector ETFs and the market portfolio ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [§1](https://arxiv.org/html/2601.14852v1#S1.p7.1 "1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [§6.1](https://arxiv.org/html/2601.14852v1#S6.SS1.p3.3 "6.1 Empirical estimates of SVIX and VIX ‣ 6 Empirical application ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [Example 4](https://arxiv.org/html/2601.14852v1#Thmexmp4.p1.1 "Example 4 (Risk-neutral covariance and correlation). ‣ 2.1 Carr-Madan approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [footnote 3](https://arxiv.org/html/2601.14852v1#footnote3 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [50]
  P. Mueller, A. Stathopoulos, and A. Vedolin (2017)
  International correlation risk.
  Journal of Financial Economics 126 (2),  pp. 270–299.
  External Links: [Document](https://dx.doi.org/10.1016/j.jfineco.2016.09.012)
  Cited by: [§1](https://arxiv.org/html/2601.14852v1#S1.p12.1 "1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [§4.4](https://arxiv.org/html/2601.14852v1#S4.SS4.p4.1 "4.4 Completeness in FX markets ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [51]
  A. Pinkus (2015)
  Ridge functions.
  Vol. 205, Cambridge University Press.
  Cited by: [§1](https://arxiv.org/html/2601.14852v1#S1.p8.3 "1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [§4.1](https://arxiv.org/html/2601.14852v1#S4.SS1.p2.7 "4.1 Identifying joint dependence from options on multiple portfolios ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [52]
  J. V. Rosenberg and R. F. Engle (2002)
  Empirical pricing kernels.
  Journal of Financial Economics 64 (3),  pp. 341–372.
  External Links: [Document](https://dx.doi.org/10.1016/S0304-405X%2802%2900128-9)
  Cited by: [footnote 2](https://arxiv.org/html/2601.14852v1#footnote2 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [53]
  S. A. Ross (1976)
  Options and efficiency.
  Quarterly Journal of Economics 90 (1),  pp. 75–89.
  Cited by: [§4.1](https://arxiv.org/html/2601.14852v1#S4.SS1.p3.5 "4.1 Identifying joint dependence from options on multiple portfolios ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [footnote 2](https://arxiv.org/html/2601.14852v1#footnote2 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [footnote 3](https://arxiv.org/html/2601.14852v1#footnote3 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation](https://arxiv.org/html/2601.14852v1#id1.id1 "Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [54]
  S. A. Ross (2015)
  The recovery theorem.
  Journal of Finance 70 (2),  pp. 615–648.
  External Links: [Document](https://dx.doi.org/10.1111/jofi.12092)
  Cited by: [footnote 2](https://arxiv.org/html/2601.14852v1#footnote2 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [55]
  P. Schneider and F. Trojani (2019)
  (Almost) model-free recovery.
  Journal of Finance 74 (1),  pp. 323–370.
  External Links: [Document](https://dx.doi.org/10.1111/jofi.12737)
  Cited by: [footnote 1](https://arxiv.org/html/2601.14852v1#footnote1 "In 1 Introduction ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [56]
  S. E. Shreve (2004)
  Stochastic calculus for finance ii: continuous-time models.
  Vol. 11, Springer.
  Cited by: [§4.4](https://arxiv.org/html/2601.14852v1#S4.SS4.p3.4 "4.4 Completeness in FX markets ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [57]
  L. N. Trefethen (2018)
  Approximation theory and approximation practice.
  Extended edition, Society for Industrial and Applied Mathematics, Philadelphia, PA.
  External Links: [Document](https://dx.doi.org/10.1137/1.9781611975949)
  Cited by: [§3.2](https://arxiv.org/html/2601.14852v1#S3.SS2.p1.1 "3.2 Convergence rate ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [58]
  B. A. Vostrecov and M. A. Kreines (1961)
  Approximation of continuous functions by superpositions of plane waves.
  In Doklady Akademii Nauk SSSR,
  Vol. 140,  pp. 1237–1240.
  Cited by: [§4.1](https://arxiv.org/html/2601.14852v1#S4.SS1.p2.7 "4.1 Identifying joint dependence from options on multiple portfolios ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").
* [59]
  H. White (1980)
  A heteroskedasticity-consistent covariance matrix estimator and a direct test for heteroskedasticity.
  Econometrica 48 (4),  pp. 817–838.
  External Links: [Document](https://dx.doi.org/10.2307/1912934)
  Cited by: [Table 5](https://arxiv.org/html/2601.14852v1#A4.T5 "In D.2 Incorporating time series information ‣ Appendix D Correlations between sector ETFs and the market portfolio ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"),
  [Table 5](https://arxiv.org/html/2601.14852v1#A4.T5.18.5.5 "In D.2 Incorporating time series information ‣ Appendix D Correlations between sector ETFs and the market portfolio ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").

## Appendix A Proofs

### A.1 Proof of Proposition [1](https://arxiv.org/html/2601.14852v1#Thmprop1 "Proposition 1. ‣ 2.4 Continuous-state limit ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")

###### Proof.

The normal equations yield X′​X​β^ns=X′​YX^{\prime}X\hat{\beta}\_{n\_{s}}=X^{\prime}Y. The (i,j)(i,j)-element of X′​XX^{\prime}X and the iith element of X′​YX^{\prime}Y are given by

|  |  |  |
| --- | --- | --- |
|  | (X′​X)i​j=∑z=1nsϕi​(sz)​ϕj​(sz),(X′​Y)i=∑z=1nsϕi​(sz)​g​(sz).(X^{\prime}X)\_{ij}=\sum\_{z=1}^{n\_{s}}\phi\_{i}(s\_{z})\phi\_{j}(s\_{z}),\quad(X^{\prime}Y)\_{i}=\sum\_{z=1}^{n\_{s}}\phi\_{i}(s\_{z})g(s\_{z}). |  |

Assuming that the grid is equally spaced with length m​(ns)=(amax−amin)/nsm(n\_{s})=(a\_{\max}-a\_{\min})/n\_{s}, it follows by the Riemann sum approximation that as ns→∞n\_{s}\to\infty

|  |  |  |
| --- | --- | --- |
|  | m​(ns)​(X′​X)i​j→∫Aϕi​(ST)​ϕj​(ST)​d​ST,m​(ns)​(X′​Y)i→∫Aϕi​(ST)​g​(ST)​d​ST.m(n\_{s})(X^{\prime}X)\_{ij}\to\int\_{A}\phi\_{i}(S\_{T})\phi\_{j}(S\_{T})\mathop{}\!\mathrm{d}S\_{T},\quad m(n\_{s})(X^{\prime}Y)\_{i}\to\int\_{A}\phi\_{i}(S\_{T})g(S\_{T})\mathop{}\!\mathrm{d}S\_{T}. |  |

The proof continues to hold if the grid in not equally spaced but the mesh goes to zero. The associated Gram matrix is invertible because the basis functions are linearly independent in L2​(A)L^{2}(A), so the solution to the normal equations exists and is unique if nsn\_{s} is sufficiently large.

The proof that β^\hat{\beta} also solves the minimization problem follows immediately from the first order conditions

|  |  |  |
| --- | --- | --- |
|  | (∫Aϕ​(ST)​ϕ​(ST)′​d​ST)​β^=∫Ag​(ST)​ϕ​(ST)​d​ST,\left(\int\_{A}\phi(S\_{T})\phi(S\_{T})^{\prime}\mathop{}\!\mathrm{d}S\_{T}\right)\hat{\beta}=\int\_{A}g(S\_{T})\phi(S\_{T})\mathop{}\!\mathrm{d}S\_{T}, |  |

where ϕ​(ST)=[ϕ1​(ST),…,ϕ2+nk​(ST)]′\phi(S\_{T})=[\phi\_{1}(S\_{T}),\dots,\phi\_{2+n\_{k}}(S\_{T})]^{\prime}.
∎

### A.2 Proof of Proposition [2](https://arxiv.org/html/2601.14852v1#Thmprop2 "Proposition 2. ‣ 3.1 Market completeness ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")

The following proof is well known (see [[42](https://arxiv.org/html/2601.14852v1#bib.bib80 "Sur l’approximation des fonctions")]), but we include it for completeness and because the assumption on the strikes results in some slight modifications of the original proof. The proof below is presented for call options, but applies verbatim to put options as well.

###### Proof.

Let g∈C​(A)g\in C(A). Because gg is continuous on a compact set it is uniformly continuous: for every ε>0\varepsilon>0 there exists a δ>0\delta>0 (independent of xx), such that sup|x−y|<δ|g​(x)−g​(y)|<ε\sup\_{\left\lvert x-y\right\rvert<\delta}\left\lvert g(x)-g(y)\right\rvert<\varepsilon. Let amin=x1<x2<⋯<xn=amaxa\_{\min}=x\_{1}<x\_{2}<\dots<x\_{n}=a\_{\max} be a partition of AA such that xj+1−xj<δ​∀jx\_{j+1}-x\_{j}<\delta\ \forall j, where amin=min⁡(A)a\_{\min}=\min(A) and amax=max⁡(A)a\_{\max}=\max(A). On each interval [xj,xj+1][x\_{j},x\_{j+1}] construct a linear function g~j​(x)=aj​x+bj\tilde{g}\_{j}(x)=a\_{j}x+b\_{j} such that g~j​(xj)=g​(xj)\tilde{g}\_{j}(x\_{j})=g(x\_{j}) and g~j​(xj+1)=g​(xj+1)\tilde{g}\_{j}(x\_{j+1})=g(x\_{j+1}). For every xc∈(xj,xj+1)x\_{c}\in(x\_{j},x\_{j+1}) it follows that

|  |  |  |
| --- | --- | --- |
|  | |g​(xc)−g~j​(xc)|≤|g​(xc)−g​(xj)|+|g​(xj)−g~j​(xc)|<2​ε,\left\lvert g(x\_{c})-\tilde{g}\_{j}(x\_{c})\right\rvert\leq\left\lvert g(x\_{c})-g(x\_{j})\right\rvert+\left\lvert g(x\_{j})-\tilde{g}\_{j}(x\_{c})\right\rvert<2\varepsilon, |  |

because

|  |  |  |
| --- | --- | --- |
|  | |g​(xj)−g~j​(xc)|=|xc−xjxj+1−xj|​|g​(xj+1)−g​(xj)|.\left\lvert g(x\_{j})-\tilde{g}\_{j}(x\_{c})\right\rvert=\left\lvert\frac{x\_{c}-x\_{j}}{x\_{j+1}-x\_{j}}\right\rvert\left\lvert g(x\_{j+1})-g(x\_{j})\right\rvert. |  |

Since xcx\_{c} is arbitrary, it follows that supx∈[xj,xj+1]|g​(x)−g~j​(x)|<2​ε\sup\_{x\in[x\_{j},x\_{j+1}]}|g(x)-\tilde{g}\_{j}(x)|<2\varepsilon. Now, define the polygonal function

|  |  |  |  |
| --- | --- | --- | --- |
|  | g~​(x)=∑j=1n−2g~j​(x)​𝟙​(x∈[xj,xj+1))+g~n−1​(x)​𝟙​(x∈[xn−1,xn]).\tilde{g}(x)=\sum\_{j=1}^{n-2}\tilde{g}\_{j}(x)\mathds{1}\left(x\in[x\_{j},x\_{j+1})\right)+\tilde{g}\_{n-1}(x)\mathds{1}\left(x\in[x\_{n-1},x\_{n}]\right). |  | (20) |

From the construction above it follows that g~\tilde{g} is continuous and supx∈A|g​(x)−g~​(x)|<2​ε\sup\_{x\in A}|g(x)-\tilde{g}(x)|<2\varepsilon. We claim that the polygonal function constructed in this way can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | g~​(x)=β1+∑j=1n−1βj+1​(x−xj)+.\tilde{g}(x)=\beta\_{1}+\sum\_{j=1}^{n-1}\beta\_{j+1}\left(x-x\_{j}\right)^{+}. |  | (21) |

To see this, proceed inductively. On [x1,x2][x\_{1},x\_{2}], ([20](https://arxiv.org/html/2601.14852v1#A1.E20 "In Proof. ‣ A.2 Proof of Proposition 2 ‣ Appendix A Proofs ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) can be written as

|  |  |  |
| --- | --- | --- |
|  | g~​(x)=a1​x+b1=a1​(x−x1)++b~1,\tilde{g}(x)=a\_{1}x+b\_{1}=a\_{1}\left(x-x\_{1}\right)^{+}+\tilde{b}\_{1}, |  |

where b~1=b1+a1​x1\tilde{b}\_{1}=b\_{1}+a\_{1}x\_{1}. On [x1,x3][x\_{1},x\_{3}], we can write

|  |  |  |
| --- | --- | --- |
|  | g~​(x)=a1​(x−x1)++b~1+a~2​(x−x2)++b~2,\tilde{g}(x)=a\_{1}\left(x-x\_{1}\right)^{+}+\tilde{b}\_{1}+\tilde{a}\_{2}\left(x-x\_{2}\right)^{+}+\tilde{b}\_{2}, |  |

where

|  |  |  |
| --- | --- | --- |
|  | a1+a~2=a2andb~2=b2+a1​x1,a\_{1}+\tilde{a}\_{2}=a\_{2}\quad\text{and}\quad\tilde{b}\_{2}=b\_{2}+a\_{1}x\_{1}, |  |

which can be solved for to obtain a~2,b~2\tilde{a}\_{2},\tilde{b}\_{2}. Continuing inductively, we obtain ([21](https://arxiv.org/html/2601.14852v1#A1.E21 "In Proof. ‣ A.2 Proof of Proposition 2 ‣ Appendix A Proofs ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")). It remains to show that g~\tilde{g} can be uniformly approximated by a function of the form

|  |  |  |
| --- | --- | --- |
|  | g~nk​(x)=β1+∑j=1nk−1βj+1​(x−Kj)+,\tilde{g}\_{n\_{k}}(x)=\beta\_{1}+\sum\_{j=1}^{n\_{k}-1}\beta\_{j+1}\left(x-K\_{j}\right)^{+}, |  |

where KjK\_{j} is among the observed call option strike prices. But this can be achieved if nkn\_{k} is large enough. Specifically, let nkn\_{k} be large enough such that maxj=1,…,n−1⁡|xj−Kj|<ε\max\_{j=1,\dots,n-1}\left\lvert x\_{j}-K\_{j}\right\rvert<\varepsilon. By assumption such nkn\_{k} can always be found since {Kj}j=1nk\left\{{K\_{j}}\right\}\_{j=1}^{n\_{k}} is dense in AA as nk→∞n\_{k}\to\infty. Considering that

|  |  |  |
| --- | --- | --- |
|  | supx∈A|(x−xj)+−(x−Kj)+|<ε,\sup\_{x\in A}\left\lvert\left(x-x\_{j}\right)^{+}-\left(x-K\_{j}\right)^{+}\right\rvert<\varepsilon, |  |

it follows by another application of the triangle inequality that

|  |  |  |
| --- | --- | --- |
|  | supx∈A|g​(x)−g~nk​(x)|<3​ε.\sup\_{x\in A}\left\lvert g(x)-\tilde{g}\_{n\_{k}}(x)\right\rvert<3\varepsilon. |  |

∎

### A.3 Proof of Corollary [1](https://arxiv.org/html/2601.14852v1#Thmthm1 "Corollary 1 (Market completeness). ‣ 3.1 Market completeness ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")

###### Proof.

According to [[9](https://arxiv.org/html/2601.14852v1#bib.bib95 "Convergence of probability measures"), Theorem 1.2 ], a probability measure 𝐏\mathbf{P} on a metric space is completely determined by the expected values 𝐄​f​(X)\mathbf{E}f(X), for all bounded, uniformly continuous functions ff, where X∼𝐏X\sim\mathbf{P}. Proposition [2](https://arxiv.org/html/2601.14852v1#Thmprop2 "Proposition 2. ‣ 3.1 Market completeness ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") shows there is a sequence of functions fnk∈span⁡(ℱ2+nk)f\_{n\_{k}}\in\operatorname{span}(\mathcal{F}\_{2+n\_{k}}) converging uniformly to ff. Because AA is compact and f,fnkf,f\_{n\_{k}} are continuous (hence bounded), the dominated convergence theorem shows that 𝐄​f​(X)\mathbf{E}f(X) is pinned down uniquely for every bounded, uniformly continuous ff.
∎

### A.4 Proof of Proposition [3](https://arxiv.org/html/2601.14852v1#Thmprop3 "Proposition 3. ‣ 3.2 Convergence rate ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")

###### Proof.

Without loss of generality, we assume that all strike prices correspond to call options. We start by deriving an error bound on the piecewise linear polynomial, denoted by g~\tilde{g}, that interpolates the points

|  |  |  |
| --- | --- | --- |
|  | {(amin,g​(amin)),(Kj,g​(Kj))j=1nk,(amax,g​(amax))}.\left\{{(a\_{\min},g(a\_{\min})),(K\_{j},g(K\_{j}))\_{j=1}^{n\_{k}},(a\_{\max},g(a\_{\max}))}\right\}. |  |

Letting g~j\tilde{g}\_{j} denote the interpolating polynomial on [Kj,Kj+1][K\_{j},K\_{j+1}], it follows from standard results in approximation theory (e.g., [[28](https://arxiv.org/html/2601.14852v1#bib.bib85 "Numerical analysis i"), Lecture 11 ]) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxx∈[Kj,Kj+1]⁡|g​(x)−g~j​(x)|\displaystyle\max\_{x\in[K\_{j},K\_{j+1}]}\left\lvert g(x)-\tilde{g}\_{j}(x)\right\rvert | ≤(maxξ∈[Kj,Kj+1]⁡|g′′​(ξ)|2)​(maxx∈[Kj,Kj+1]⁡(x−Kj)​(Kj+1−x))\displaystyle\leq\left(\max\_{\xi\in[K\_{j},K\_{j+1}]}\frac{\left\lvert g^{\prime\prime}(\xi)\right\rvert}{2}\right)\left(\max\_{x\in[K\_{j},K\_{j+1}]}(x-K\_{j})(K\_{j+1}-x)\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | ≤‖g′‖∞​18​(Kj+1−Kj)2,\displaystyle\leq\left\lVert g^{\prime}\right\rVert\_{\infty}\frac{1}{8}\left(K\_{j+1}-K\_{j}\right)^{2}, |  | (22) |

where ‖g′‖∞=maxξ∈[amax,amin]⁡|g′′​(ξ)|\left\lVert g^{\prime}\right\rVert\_{\infty}=\max\_{\xi\in[a\_{\max},a\_{\min}]}\left\lvert g^{\prime\prime}(\xi)\right\rvert. Hence,

|  |  |  |
| --- | --- | --- |
|  | ∫KjKj+1(g​(x)−g~j​(x))2​d​x≤164​‖g′‖∞2​(Kj+1−Kj)5.\int\_{K\_{j}}^{K\_{j+1}}\left(g(x)-\tilde{g}\_{j}(x)\right)^{2}\mathop{}\!\mathrm{d}x\leq\frac{1}{64}\left\lVert g^{\prime}\right\rVert\_{\infty}^{2}\left(K\_{j+1}-K\_{j}\right)^{5}. |  |

Since g~\tilde{g} equals g~j​(x)\tilde{g}\_{j}(x) on [Kj,Kj+1)[K\_{j},K\_{j+1}), it follows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫K1Knk(g​(x)−g~​(x))2​d​x\displaystyle\int\_{K\_{1}}^{K\_{n\_{k}}}\left(g(x)-\tilde{g}(x)\right)^{2}\mathop{}\!\mathrm{d}x | =∑j=1nk−1∫KjKj+1(g​(x)−g~j​(x))2​d​x\displaystyle=\sum\_{j=1}^{n\_{k}-1}\int\_{K\_{j}}^{K\_{j+1}}\left(g(x)-\tilde{g}\_{j}(x)\right)^{2}\mathop{}\!\mathrm{d}x |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤nk64​‖g′‖∞2​Δ5\displaystyle\leq\frac{n\_{k}}{64}\left\lVert g^{\prime}\right\rVert\_{\infty}^{2}\Delta^{5} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =O​(1/nk4),\displaystyle=O(1/n\_{k}^{4}), |  | (23) |

where in the last line we used that Δ=O​(1/nk)\Delta=O(1/n\_{k}). Applying ([22](https://arxiv.org/html/2601.14852v1#A1.E22 "In Proof. ‣ A.4 Proof of Proposition 3 ‣ Appendix A Proofs ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) again on [Knk,amax][K\_{n\_{k}},a\_{\max}] renders the estimate

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxx∈[Knk,amax]⁡|g​(x)−g~​(x)|≤‖g′‖∞​18​(amax−Knk)2.\max\_{x\in[K\_{n\_{k}},a\_{\max}]}\left\lvert g(x)-\tilde{g}(x)\right\rvert\leq\left\lVert g^{\prime}\right\rVert\_{\infty}\frac{1}{8}\left(a\_{\max}-K\_{n\_{k}}\right)^{2}. |  | (24) |

A similar bound can be derived on [amin,K1][a\_{\min},K\_{1}]. From the proof of Proposition [2](https://arxiv.org/html/2601.14852v1#Thmprop2 "Proposition 2. ‣ 3.1 Market completeness ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") we know that g~​(x)\tilde{g}(x) can be written in the form

|  |  |  |
| --- | --- | --- |
|  | g~​(x)=β1+β2​x+∑j=1nkβ2+j​(x−Kj)+.\tilde{g}(x)=\beta\_{1}+\beta\_{2}x+\sum\_{j=1}^{n\_{k}}\beta\_{2+j}\left(x-K\_{j}\right)^{+}. |  |

Then we can bound the estimation error as follows

|  |  |  |
| --- | --- | --- |
|  | |𝐄tQ​[g​(ST)​𝟙​(ST∈A)]−𝐄tQ​[g^​(ST)​𝟙​(ST∈A)]|\displaystyle\left\lvert\mathbf{E}\_{t}^{Q}\left[g(S\_{T})\mathds{1}\left(S\_{T}\in A\right)\right]-\mathbf{E}\_{t}^{Q}\left[\hat{g}(S\_{T})\mathds{1}\left(S\_{T}\in A\right)\right]\right\rvert |  |
|  |  |  |
| --- | --- | --- |
|  | =|∫aminamax(g​(x)−g^​(x))​ft→TQ​(x)​d​x|\displaystyle=\left\lvert\int\_{a\_{\min}}^{a\_{\max}}\left(g(x)-\hat{g}(x)\right)f\_{t\to T}^{Q}(x)\mathop{}\!\mathrm{d}x\right\rvert |  |
|  |  |  |
| --- | --- | --- |
|  | ≤∫aminamax|g​(x)−g^​(x)|​ft→TQ​(x)​d​x\displaystyle\leq\int\_{a\_{\min}}^{a\_{\max}}\left\lvert g(x)-\hat{g}(x)\right\rvert f\_{t\to T}^{Q}(x)\mathop{}\!\mathrm{d}x |  |
|  |  |  |
| --- | --- | --- |
|  | ≤(∫aminamax(g​(x)−g^​(x))2​d​x)1/2​(∫aminamaxft→TQ​(x)2​d​x)1/2\displaystyle\leq\left(\int\_{a\_{\min}}^{a\_{\max}}\left(g(x)-\hat{g}(x)\right)^{2}\mathop{}\!\mathrm{d}x\right)^{1/2}\left(\int\_{a\_{\min}}^{a\_{\max}}f\_{t\to T}^{Q}(x)^{2}\mathop{}\!\mathrm{d}x\right)^{1/2} |  |
|  |  |  |
| --- | --- | --- |
|  | ≤(∫aminamax(g​(x)−g~​(x))2​d​x)1/2​(∫aminamaxft→TQ​(x)2​d​x)1/2\displaystyle\leq\left(\int\_{a\_{\min}}^{a\_{\max}}\left(g(x)-\tilde{g}(x)\right)^{2}\mathop{}\!\mathrm{d}x\right)^{1/2}\left(\int\_{a\_{\min}}^{a\_{\max}}f\_{t\to T}^{Q}(x)^{2}\mathop{}\!\mathrm{d}x\right)^{1/2} |  |
|  |  |  |
| --- | --- | --- |
|  | =(∫aminamaxft→TQ(x)2dx)1/2(∫aminK1(g(x)−g~(x))2dx\displaystyle=\left(\int\_{a\_{\min}}^{a\_{\max}}f\_{t\to T}^{Q}(x)^{2}\mathop{}\!\mathrm{d}x\right)^{1/2}\bigg(\int\_{a\_{\min}}^{K\_{1}}\left(g(x)-\tilde{g}(x)\right)^{2}\mathop{}\!\mathrm{d}x |  |
|  |  |  |
| --- | --- | --- |
|  | +∫K1Knk(g(x)−g~(x))2dx+∫Knkamax(g(x)−g~(x))2dx)1/2\displaystyle+\int\_{K\_{1}}^{K\_{n\_{k}}}\left(g(x)-\tilde{g}(x)\right)^{2}\mathop{}\!\mathrm{d}x+\int\_{K\_{n\_{k}}}^{a\_{\max}}\left(g(x)-\tilde{g}(x)\right)^{2}\mathop{}\!\mathrm{d}x\bigg)^{1/2} |  |
|  |  |  |
| --- | --- | --- |
|  | ≕(∫aminamaxft→TQ​(x)2​d​x)1/2​(B1+B2+B3)1/2,\displaystyle\eqqcolon\left(\int\_{a\_{\min}}^{a\_{\max}}f\_{t\to T}^{Q}(x)^{2}\mathop{}\!\mathrm{d}x\right)^{1/2}\left(B\_{1}+B\_{2}+B\_{3}\right)^{1/2}, |  |

where we successively used the Cauchy-Schwarz inequality combined with the square-integrability of ft→TQf\_{t\to T}^{Q}, and the minimization property of g^\hat{g}. From ([23](https://arxiv.org/html/2601.14852v1#A1.E23 "In Proof. ‣ A.4 Proof of Proposition 3 ‣ Appendix A Proofs ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")), we know that B2=O​(Δ4)=O​(1/nk4)B\_{2}=O(\Delta^{4})=O(1/n\_{k}^{4}). Moreover, by ([24](https://arxiv.org/html/2601.14852v1#A1.E24 "In Proof. ‣ A.4 Proof of Proposition 3 ‣ Appendix A Proofs ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) and the assumption that amax−Knk=O​(1/nk4/5)a\_{\max}-K\_{n\_{k}}=O(1/n\_{k}^{4/5}), B3B\_{3} is of order O​(amax−Knk)5=O​(1/nk4)O(a\_{\max}-K\_{n\_{k}})^{5}=O(1/n\_{k}^{4}). Analogous reasoning yields B1=O​(K1−amin)5=O​(1/nk4)B\_{1}=O(K\_{1}-a\_{\min})^{5}=O(1/n\_{k}^{4}).

∎

### A.5 Proof of Proposition [4](https://arxiv.org/html/2601.14852v1#Thmprop4 "Proposition 4. ‣ 3.2 Convergence rate ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")

###### Proof.

Over AA, the CM Taylor expansion in ([2.1](https://arxiv.org/html/2601.14852v1#S2.Ex1 "2.1 Carr-Madan approach ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | g​(x)\displaystyle g(x) | =g​(Ft→T)+g′​(Ft→T)​(x−Ft→T)\displaystyle=g(F\_{t\to T})+g^{\prime}(F\_{t\to T})\left(x-F\_{t\to T}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫aminFt→Tg′′​(K)​(K−x)+​d​K+∫Knkamaxg′′​(K)​(x−K)+​d​K.\displaystyle+\int\_{a\_{\min}}^{F\_{t\to T}}g^{\prime\prime}(K)\left(K-x\right)^{+}\mathop{}\!\mathrm{d}K+\int\_{K\_{n\_{k}}}^{a\_{\max}}g^{\prime\prime}(K)\left(x-K\right)^{+}\mathop{}\!\mathrm{d}K. |  |

We will focus on the case x≤Ft→Tx\leq F\_{t\to T} (the case x>Ft→Tx>F\_{t\to T} is identical). The integral is discretized using the trapezoidal rule, which is known to satisfy

|  |  |  |
| --- | --- | --- |
|  | ∑j:Kj≤Ft→TΔ​Kj​g′′​(Kj)​(Kj−ST)+=∫K1Ft→Tg′′​(K)​(K−x)+​d​K+O​(1nk2),\sum\_{j:K\_{j}\leq F\_{t\to T}}\Delta K\_{j}\,g^{\prime\prime}(K\_{j})\left(K\_{j}-S\_{T}\right)^{+}=\int\_{K\_{1}}^{F\_{t\to T}}g^{\prime\prime}(K)\left(K-x\right)^{+}\mathop{}\!\mathrm{d}K+O\left(\frac{1}{n\_{k}^{2}}\right), |  |

uniformly in xx. Hence, for x∈[K1,Ft→T]x\in[K\_{1},F\_{t\to T}], we obtain

|  |  |  |
| --- | --- | --- |
|  | maxx∈[K1,Ft→T]⁡|g​(x)−g^CM​(x)|=O​(1nk2).\max\_{x\in[K\_{1},F\_{t\to T}]}\left\lvert g(x)-\hat{g}\_{\mathrm{CM}}(x)\right\rvert=O\left(\frac{1}{n\_{k}^{2}}\right). |  |

For x∈[amin,K1]x\in[a\_{\min},K\_{1}], we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | |g​(x)−g^CM​(x)|\displaystyle\left\lvert g(x)-\hat{g}\_{\mathrm{CM}}(x)\right\rvert | =|∫xK1g′′​(K)​(K−x)​d​K|\displaystyle=\left\lvert\int\_{x}^{K\_{1}}g^{\prime\prime}(K)(K-x)\mathop{}\!\mathrm{d}K\right\rvert |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤‖g′′‖∞​12​(K1−x)2.\displaystyle\leq\left\lVert g^{\prime\prime}\right\rVert\_{\infty}\frac{1}{2}\left(K\_{1}-x\right)^{2}. |  |

Analogous reasoning yields a similar bound for x>Ft→Tx>F\_{t\to T}. The same reasoning at the end of Proposition [3](https://arxiv.org/html/2601.14852v1#Thmprop3 "Proposition 3. ‣ 3.2 Convergence rate ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") then finally gives

|  |  |  |
| --- | --- | --- |
|  | |∫aminamax(g​(x)−g^CM​(x))​ft→TQ​(x)​d​x|\displaystyle\left\lvert\int\_{a\_{\min}}^{a\_{\max}}\left(g(x)-\hat{g}\_{\mathrm{CM}}(x)\right)f\_{t\to T}^{Q}(x)\mathop{}\!\mathrm{d}x\right\rvert |  |
|  |  |  |
| --- | --- | --- |
|  | ≤(∫aminamaxft→TQ(x)2dx)1/2(∫aminK1(g(x)−g^CM(x))2dx\displaystyle\leq\left(\int\_{a\_{\min}}^{a\_{\max}}f\_{t\to T}^{Q}(x)^{2}\mathop{}\!\mathrm{d}x\right)^{1/2}\bigg(\int\_{a\_{\min}}^{K\_{1}}\left(g(x)-\hat{g}\_{\mathrm{CM}}(x)\right)^{2}\mathop{}\!\mathrm{d}x |  |
|  |  |  |
| --- | --- | --- |
|  | +∫K1Knk(g(x)−g^CM(x))2dx+∫Knkamax(g(x)−g^CM(x))2dx)1/2\displaystyle+\int\_{K\_{1}}^{K\_{n\_{k}}}\left(g(x)-\hat{g}\_{\mathrm{CM}}(x)\right)^{2}\mathop{}\!\mathrm{d}x+\int\_{K\_{n\_{k}}}^{a\_{\max}}\left(g(x)-\hat{g}\_{\mathrm{CM}}(x)\right)^{2}\mathop{}\!\mathrm{d}x\bigg)^{1/2} |  |
|  |  |  |
| --- | --- | --- |
|  | =(O​(K1−amin)5+O​(1nk4)+O​(amax−Knk)5)1/2\displaystyle=\left(O\left(K\_{1}-a\_{\min}\right)^{5}+O\left(\frac{1}{n\_{k}^{4}}\right)+O\left(a\_{\max}-K\_{n\_{k}}\right)^{5}\right)^{1/2} |  |
|  |  |  |
| --- | --- | --- |
|  | =O​(1nk2).\displaystyle=O\left(\frac{1}{n\_{k}^{2}}\right). |  |

∎

### A.6 Proof of Proposition [5](https://arxiv.org/html/2601.14852v1#Thmprop5 "Proposition 5. ‣ 3.2 Convergence rate ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")

###### Proof.

Let P​LPL denote the space of continuous piecewise linear functions on this knot sequence. It is standard that (e.g. using the proof of Proposition [2](https://arxiv.org/html/2601.14852v1#Thmprop2 "Proposition 2. ‣ 3.1 Market completeness ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"))

|  |  |  |
| --- | --- | --- |
|  | P​L=span​(ℱ2+nk)=span​{1,x,(x−K1)+,…,(x−Knk)+}.PL=\mathrm{span}\bigl(\mathcal{F}\_{2+n\_{k}}\bigr)=\mathrm{span}\{1,x,(x-K\_{1})\_{+},\dots,(x-K\_{n\_{k}})\_{+}\}. |  |

Equivalently, P​LPL is spanned by the nodal tent functions {φi}i=0nk+1\{\varphi\_{i}\}\_{i=0}^{n\_{k}+1} defined by

|  |  |  |
| --- | --- | --- |
|  | φi​(Kj)=δi​j,supp​(φi)=[Ki−1,Ki+1],\varphi\_{i}(K\_{j})=\delta\_{ij},\qquad\mathrm{supp}(\varphi\_{i})=[K\_{i-1},K\_{i+1}], |  |

(where φ0,φnk+1\varphi\_{0},\varphi\_{n\_{k}+1} are the boundary hats). In particular, any s∈P​Ls\in PL can be written uniquely as

|  |  |  |
| --- | --- | --- |
|  | s​(x)=∑i=0nk+1αi​φi​(x),αi=s​(Ki).s(x)=\sum\_{i=0}^{n\_{k}+1}\alpha\_{i}\varphi\_{i}(x),\qquad\alpha\_{i}=s(K\_{i}). |  |

Let g∈C4​(A)g\in C^{4}(A) and let g^\hat{g} be its L2​(A)L^{2}(A)-projection onto P​LPL. Write g^​(x)=∑i=0nk+1αi​φi​(x)\hat{g}(x)=\sum\_{i=0}^{n\_{k}+1}\alpha\_{i}\varphi\_{i}(x) and define

|  |  |  |
| --- | --- | --- |
|  | bi≔∫Aφi​(x)​g​(x)​d​x,Mi​j≔∫Aφi​(x)​φj​(x)​d​x.b\_{i}\coloneqq\int\_{A}\varphi\_{i}(x)g(x)\mathop{}\!\mathrm{d}x,\qquad M\_{ij}\coloneqq\int\_{A}\varphi\_{i}(x)\varphi\_{j}(x)\mathop{}\!\mathrm{d}x. |  |

Then the normal equations are M​α=bM\alpha=b. For interior indices i=1,…,nki=1,\dots,n\_{k} (away from the boundary),
the matrix entries on a uniform grid are

|  |  |  |
| --- | --- | --- |
|  | Mi​i=2​h3,Mi,i±1=h6,Mi​j=0​ if ​|i−j|>1,M\_{ii}=\frac{2h}{3},\qquad M\_{i,i\pm 1}=\frac{h}{6},\qquad M\_{ij}=0\ \text{ if }|i-j|>1, |  |

so the interior normal equations read (see also [[26](https://arxiv.org/html/2601.14852v1#bib.bib128 "A practical guide to splines"), p.34 ])

|  |  |  |  |
| --- | --- | --- | --- |
|  | h6​αi−1+2​h3​αi+h6​αi+1=bi,i=1,…,nk.\frac{h}{6}\alpha\_{i-1}+\frac{2h}{3}\alpha\_{i}+\frac{h}{6}\alpha\_{i+1}=b\_{i},\qquad i=1,\dots,n\_{k}. |  | (25) |

Define yi≔bi/hy\_{i}\coloneqq b\_{i}/h and the discrete operator 𝒯\mathcal{T} by

|  |  |  |
| --- | --- | --- |
|  | (𝒯​α)i≔16​αi−1+23​αi+16​αi+1.(\mathcal{T}\alpha)\_{i}\coloneqq\frac{1}{6}\alpha\_{i-1}+\frac{2}{3}\alpha\_{i}+\frac{1}{6}\alpha\_{i+1}. |  |

Then ([25](https://arxiv.org/html/2601.14852v1#A1.E25 "In Proof. ‣ A.6 Proof of Proposition 5 ‣ Appendix A Proofs ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) is equivalently

|  |  |  |  |
| --- | --- | --- | --- |
|  | (𝒯​α)i=yi,i=1,…,nk.(\mathcal{T}\alpha)\_{i}=y\_{i},\qquad i=1,\dots,n\_{k}. |  | (26) |

Step 1 (expansion of yiy\_{i}).
For interior ii, the hat function satisfies φi​(Ki+u)=1−|u|/h\varphi\_{i}(K\_{i}+u)=1-|u|/h for u∈[−h,h]u\in[-h,h], hence

|  |  |  |
| --- | --- | --- |
|  | bi=∫Ki−1Ki+1g​(x)​φi​(x)​d​x=∫−hhg​(Ki+u)​(1−|u|h)​d​u.b\_{i}=\int\_{K\_{i-1}}^{K\_{i+1}}g(x)\varphi\_{i}(x)\mathop{}\!\mathrm{d}x=\int\_{-h}^{h}g(K\_{i}+u)\Bigl(1-\frac{|u|}{h}\Bigr)\mathop{}\!\mathrm{d}u. |  |

Expanding g​(Ki+u)g(K\_{i}+u) around u=0u=0 and using symmetry (odd moments vanish), we obtain

|  |  |  |
| --- | --- | --- |
|  | bih=yi=g​(Ki)+h212​g′′​(Ki)+O​(h4),i=1,…,nk,\frac{b\_{i}}{h}=y\_{i}=g(K\_{i})+\frac{h^{2}}{12}g^{\prime\prime}(K\_{i})+O(h^{4}),\qquad i=1,\dots,n\_{k}, |  |

where the O​(h4)O(h^{4}) term is uniform in ii.

Step 2 (candidate solution).
Define the candidate sequence

|  |  |  |  |
| --- | --- | --- | --- |
|  | α~i≔g​(Ki)−h212​g′′​(Ki).\tilde{\alpha}\_{i}\coloneqq g(K\_{i})-\frac{h^{2}}{12}g^{\prime\prime}(K\_{i}). |  | (27) |

A Taylor expansion yields, for interior ii,

|  |  |  |
| --- | --- | --- |
|  | (𝒯​α~)i=α~i+h26​α~′′​(Ki)+O​(h4).(\mathcal{T}\tilde{\alpha})\_{i}=\tilde{\alpha}\_{i}+\frac{h^{2}}{6}\tilde{\alpha}^{\prime\prime}(K\_{i})+O(h^{4}). |  |

Since α~′′​(K)=g′′​(K)−h212​g(4)​(K)\tilde{\alpha}^{\prime\prime}(K)=g^{\prime\prime}(K)-\frac{h^{2}}{12}g^{(4)}(K), this implies

|  |  |  |
| --- | --- | --- |
|  | (𝒯​α~)i=g​(Ki)+h212​g′′​(Ki)+O​(h4).(\mathcal{T}\tilde{\alpha})\_{i}=g(K\_{i})+\frac{h^{2}}{12}g^{\prime\prime}(K\_{i})+O(h^{4}). |  |

Combining with Step 1 gives the residual

|  |  |  |
| --- | --- | --- |
|  | ri≔(𝒯​α~)i−yi=O​(h4),i=1,…,nk.r\_{i}\coloneqq(\mathcal{T}\tilde{\alpha})\_{i}-y\_{i}=O(h^{4}),\qquad i=1,\dots,n\_{k}. |  |

The operator 𝒯\mathcal{T} corresponds to a tridiagonal Toeplitz matrix on interior indices, and is strictly diagonally dominant. Hence 𝒯\mathcal{T} is uniformly invertible on interior indices and ‖𝒯−1‖≤C\|\mathcal{T}^{-1}\|\leq C for a constant CC independent of hh. Therefore, solving ([26](https://arxiv.org/html/2601.14852v1#A1.E26 "In Proof. ‣ A.6 Proof of Proposition 5 ‣ Appendix A Proofs ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) and using 𝒯​α=y\mathcal{T}\alpha=y,

|  |  |  |
| --- | --- | --- |
|  | α−α~=𝒯−1​(y−𝒯​α~)=−𝒯−1​r,\alpha-\tilde{\alpha}=\mathcal{T}^{-1}(y-\mathcal{T}\tilde{\alpha})=-\mathcal{T}^{-1}r, |  |

so αi−α~i=O​(h4)\alpha\_{i}-\tilde{\alpha}\_{i}=O(h^{4}) for interior ii. In particular,

|  |  |  |  |
| --- | --- | --- | --- |
|  | αi=g​(Ki)−h212​g′′​(Ki)+O​(h4),i=1,…,nk.\alpha\_{i}=g(K\_{i})-\frac{h^{2}}{12}g^{\prime\prime}(K\_{i})+O(h^{4}),\qquad i=1,\dots,n\_{k}. |  | (28) |

Step 3 (translate to option basis).
Write the same projected spline in the option payoff basis,

|  |  |  |
| --- | --- | --- |
|  | g^​(x)=β^1+β^2​x+∑i=1nkγ^i​(x−Ki)+.\hat{g}(x)=\hat{\beta}\_{1}+\hat{\beta}\_{2}x+\sum\_{i=1}^{n\_{k}}\hat{\gamma}\_{i}\left(x-K\_{i}\right)^{+}. |  |

For x≠Kix\neq K\_{i}, differentiating gives

|  |  |  |
| --- | --- | --- |
|  | g^′​(x)=β^2+∑j:Kj<xγ^j,\hat{g}^{\prime}(x)=\hat{\beta}\_{2}+\sum\_{j:K\_{j}<x}\hat{\gamma}\_{j}, |  |

hence γ^i\hat{\gamma}\_{i} is the jump in slope at KiK\_{i}. Let

|  |  |  |
| --- | --- | --- |
|  | pi≔αi+1−αih(the slope of g^ on [Ki,Ki+1]).p\_{i}\coloneqq\frac{\alpha\_{i+1}-\alpha\_{i}}{h}\quad\text{(the slope of $\hat{g}$ on $[K\_{i},K\_{i+1}]$)}. |  |

Then the jump in slope at KiK\_{i} is

|  |  |  |
| --- | --- | --- |
|  | γ^i=pi−pi−1=αi+1−2​αi+αi−1h.\hat{\gamma}\_{i}=p\_{i}-p\_{i-1}=\frac{\alpha\_{i+1}-2\alpha\_{i}+\alpha\_{i-1}}{h}. |  |

A Taylor expansion yields αi+1−2​αi+αi−1=h2​α′′​(Ki)+O​(h4)\alpha\_{i+1}-2\alpha\_{i}+\alpha\_{i-1}=h^{2}\alpha^{\prime\prime}(K\_{i})+O(h^{4}), hence

|  |  |  |
| --- | --- | --- |
|  | γ^i=h​α′′​(Ki)+O​(h3).\hat{\gamma}\_{i}=h\,\alpha^{\prime\prime}(K\_{i})+O(h^{3}). |  |

Using ([28](https://arxiv.org/html/2601.14852v1#A1.E28 "In Proof. ‣ A.6 Proof of Proposition 5 ‣ Appendix A Proofs ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")), we have α′′​(Ki)=g′′​(Ki)+O​(h2)\alpha^{\prime\prime}(K\_{i})=g^{\prime\prime}(K\_{i})+O(h^{2}), and therefore

|  |  |  |
| --- | --- | --- |
|  | γ^i=h​g′′​(Ki)+O​(h3),i=2,…,nk−1,\hat{\gamma}\_{i}=h\,g^{\prime\prime}(K\_{i})+O(h^{3}),\qquad i=2,\dots,n\_{k}-1, |  |

i.e. for interior strikes the leading-order term of the projection coefficient in the truncated power basis is
h​g′′​(Ki)h\,g^{\prime\prime}(K\_{i}).

The slower convergence rate at the boundary coefficient γ^1\hat{\gamma}\_{1} follows because the kernel function ϕ0\phi\_{0} is one sided, so odd moments under the kernel function no longer vanish. The same observation applies to γ^nk\hat{\gamma}\_{n\_{k}}.
∎

### A.7 Proof of Proposition [6](https://arxiv.org/html/2601.14852v1#Thmprop6 "Proposition 6. ‣ 3.2 Convergence rate ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")

###### Proof.

The space spanned by ℱ2+nk\mathcal{F}\_{2+n\_{k}} is equal to the span of the B-spline basis functions of order 2 with knots at amin<K1<⋯<Knk<amaxa\_{\min}<K\_{1}<\dots<K\_{n\_{k}}<a\_{\max}. In particular, this implies that the L2​(A)L^{2}(A)-projections concur. [[26](https://arxiv.org/html/2601.14852v1#bib.bib128 "A practical guide to splines"), Theorem 12 in Chapter 2 ] then shows that

|  |  |  |
| --- | --- | --- |
|  | maxx∈A⁡|g​(x)−g^​(x)|≤4​dist⁡(g,ℱ2+nk).\max\_{x\in A}\left\lvert g(x)-\hat{g}(x)\right\rvert\leq 4\operatorname{dist}(g,\mathcal{F}\_{2+n\_{k}}). |  |

Consequently,

|  |  |  |  |
| --- | --- | --- | --- |
|  | |𝐄tQ​g​(ST)−𝐄tQ​g^​(ST)|\displaystyle\left\lvert\mathbf{E}\_{t}^{Q}g(S\_{T})-\mathbf{E}\_{t}^{Q}\hat{g}(S\_{T})\right\rvert | ≤∫0∞|g​(x)−g^​(x)|​ft→TQ​(x)​d​x\displaystyle\leq\int\_{0}^{\infty}\left\lvert g(x)-\hat{g}(x)\right\rvert f\_{t\to T}^{Q}(x)\mathop{}\!\mathrm{d}x |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∫0amin|g​(x)−g^​(x)|​ft→TQ​(x)​d​x+∫aminamax|g​(x)−g^​(x)|​ft→TQ​(x)​d​x\displaystyle=\int\_{0}^{a\_{\min}}\left\lvert g(x)-\hat{g}(x)\right\rvert f\_{t\to T}^{Q}(x)\mathop{}\!\mathrm{d}x+\int\_{a\_{\min}}^{a\_{\max}}\left\lvert g(x)-\hat{g}(x)\right\rvert f\_{t\to T}^{Q}(x)\mathop{}\!\mathrm{d}x |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +∫amax∞|g​(x)−g^​(x)|​ft→TQ​(x)​d​x\displaystyle+\int\_{a\_{\max}}^{\infty}\left\lvert g(x)-\hat{g}(x)\right\rvert f\_{t\to T}^{Q}(x)\mathop{}\!\mathrm{d}x |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝐄tQ​[(|g​(ST)|+|g^​(ST)|)​𝟙​(ST∉A)]+4​dist⁡(g,ℱ2+nk)\displaystyle\leq\mathbf{E}\_{t}^{Q}\left[\left(\left\lvert g(S\_{T})\right\rvert+\left\lvert\hat{g}(S\_{T})\right\rvert\right)\mathds{1}\left(S\_{T}\notin A\right)\right]+4\operatorname{dist}(g,\mathcal{F}\_{2+n\_{k}}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤ε+4​dist⁡(g,ℱ2+nk).\displaystyle\leq\varepsilon+4\operatorname{dist}(g,\mathcal{F}\_{2+n\_{k}}). |  |

Notice that 𝐄tQ​ST<∞\mathbf{E}\_{t}^{Q}S\_{T}<\infty implies that 𝐄tQ​|g^​(ST)|<∞\mathbf{E}\_{t}^{Q}\left\lvert\hat{g}(S\_{T})\right\rvert<\infty, since g^\hat{g} is a piecewise linear function of STS\_{T}, and therefore has at most linear growth.
∎

### A.8 Proof of Proposition [7](https://arxiv.org/html/2601.14852v1#Thmprop7 "Proposition 7 (Risk-neutral distribution). ‣ 3.3 Estimation of the risk-neutral CDF and PDF ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")

###### Proof.

Part [(i)](https://arxiv.org/html/2601.14852v1#S3.I1.i1 "item (i) ‣ Proposition 7 (Risk-neutral distribution). ‣ 3.3 Estimation of the risk-neutral CDF and PDF ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") follows immediately from the continuous-state problem ([8](https://arxiv.org/html/2601.14852v1#S2.E8 "In Proposition 1. ‣ 2.4 Continuous-state limit ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")), as 𝟙​(ST≤amin)≡0\mathds{1}\left(S\_{T}\leq a\_{\min}\right)\equiv 0 and 𝟙​(ST≤amax)≡1\mathds{1}\left(S\_{T}\leq a\_{\max}\right)\equiv 1. Since the approximating function class contains the constant function, it follows that the solution to ([8](https://arxiv.org/html/2601.14852v1#S2.E8 "In Proposition 1. ‣ 2.4 Continuous-state limit ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) in both cases is β=0\beta=0 and [β1,β2,…,β2+nk]=[1,0,…,0][\beta\_{1},\beta\_{2},\dots,\beta\_{2+n\_{k}}]=[1,0,\dots,0] respectively.

Part [(ii)](https://arxiv.org/html/2601.14852v1#S3.I1.i2 "item (ii) ‣ Proposition 7 (Risk-neutral distribution). ‣ 3.3 Estimation of the risk-neutral CDF and PDF ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"): We need to establish differentiability of β^​(x)\hat{\beta}(x). The risk-neutral distribution can easily be derived from ([7](https://arxiv.org/html/2601.14852v1#S2.E7 "In Proposition 1. ‣ 2.4 Continuous-state limit ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) and ([10](https://arxiv.org/html/2601.14852v1#S3.E10 "In 3.3 Estimation of the risk-neutral CDF and PDF ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")). In particular, from ([7](https://arxiv.org/html/2601.14852v1#S2.E7 "In Proposition 1. ‣ 2.4 Continuous-state limit ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) we deduce that

|  |  |  |
| --- | --- | --- |
|  | ∂∂x​β^​(x)=[⟨ϕ1,ϕ1⟩…⟨ϕ1,ϕ2+nk⟩⋮⋱⋮⟨ϕ2+nk,ϕ1⟩…⟨ϕ2+nk,ϕ2+nk⟩]−1​[1x⋮ϕj​(x)⋮ϕ2+nk​(x)].\frac{\partial}{\partial x}\hat{\beta}(x)=\begin{bmatrix}\left\langle\phi\_{1},\phi\_{1}\right\rangle&\dots&\left\langle\phi\_{1},\phi\_{2+n\_{k}}\right\rangle\\ \vdots&\ddots&\vdots\\ \left\langle\phi\_{2+n\_{k}},\phi\_{1}\right\rangle&\dots&\left\langle\phi\_{2+n\_{k}},\phi\_{2+n\_{k}}\right\rangle\end{bmatrix}^{-1}\begin{bmatrix}1\\ x\\ \vdots\\ \phi\_{j}(x)\\ \vdots\\ \phi\_{2+n\_{k}}(x)\end{bmatrix}. |  |

Each component of ∂∂x​β^​(x)\frac{\partial}{\partial x}\hat{\beta}(x) is therefore a piecewise linear function due to the structure of the basis functions. The final claim then follows because a linear combination of piecewise linear functions is piecewise linear.

Part [(iii)](https://arxiv.org/html/2601.14852v1#S3.I1.i3 "item (iii) ‣ Proposition 7 (Risk-neutral distribution). ‣ 3.3 Estimation of the risk-neutral CDF and PDF ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"): By the Gram-Schmidt process, we can assume that {ϕi}i=12+nk\left\{{\phi\_{i}}\right\}\_{i=1}^{2+n\_{k}} is an orthonormal basis w.r.t. the inner product ⟨ϕi,ϕj⟩=∫Aϕi​(x)​ϕj​(x)​d​x\left\langle\phi\_{i},\phi\_{j}\right\rangle=\int\_{A}\phi\_{i}(x)\phi\_{j}(x)\mathop{}\!\mathrm{d}x. This integral is finite because all basis functions are continuous and AA is compact. Hence, for x∈Ax\in A the risk-neutral CDF and PDF can be expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | F^t→TQ​(x)\displaystyle\hat{F}\_{t\to T}^{Q}(x) | =∑j=12+nk⟨𝟙​(ST≤x),ϕj​(ST)⟩​𝐄tQ​ϕj​(ST)\displaystyle=\sum\_{j=1}^{2+n\_{k}}\left\langle\mathds{1}\left(S\_{T}\leq x\right),\phi\_{j}(S\_{T})\right\rangle\mathbf{E}\_{t}^{Q}\phi\_{j}(S\_{T}) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | f^t→TQ​(x)\displaystyle\hat{f}\_{t\to T}^{Q}(x) | =∂∂x​F^t→TQ​(x)=∑j=12+nkϕj​(x)​𝐄tQ​ϕj​(ST).\displaystyle=\frac{\partial}{\partial x}\hat{F}\_{t\to T}^{Q}(x)=\sum\_{j=1}^{2+n\_{k}}\phi\_{j}(x)\mathbf{E}\_{t}^{Q}\phi\_{j}(S\_{T}). |  | (29) |

Notice that 𝐄tQ​ϕj​(ST)\mathbf{E}\_{t}^{Q}\phi\_{j}(S\_{T}) is now a linear combination of put and call option prices due to the Gram-Schmidt process. It follows from ([29](https://arxiv.org/html/2601.14852v1#A1.E29 "In Proof. ‣ A.8 Proof of Proposition 7 ‣ Appendix A Proofs ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫Ag​(x)​d​F^t→TQ​(x)\displaystyle\int\_{A}g(x)\mathop{}\!\mathrm{d}\hat{F}\_{t\to T}^{Q}(x) | =∑j=12+nk𝐄tQ​[ϕj​(ST)]​∫Ag​(x)​ϕj​(x)​d​x\displaystyle=\sum\_{j=1}^{2+n\_{k}}\mathbf{E}\_{t}^{Q}\left[\phi\_{j}(S\_{T})\right]\int\_{A}g(x)\phi\_{j}(x)\mathop{}\!\mathrm{d}x |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑j=12+nk𝐄tQ​[ϕj​(ST)]​⟨g,ϕj⟩\displaystyle=\sum\_{j=1}^{2+n\_{k}}\mathbf{E}\_{t}^{Q}\left[\phi\_{j}(S\_{T})\right]\left\langle g,\phi\_{j}\right\rangle |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝐄tQ​g^​(ST).\displaystyle=\mathbf{E}\_{t}^{Q}\hat{g}(S\_{T}). |  |

The last line follows because, under the Gram-Schmidt process, β^j\hat{\beta}\_{j} from ([7](https://arxiv.org/html/2601.14852v1#S2.E7 "In Proposition 1. ‣ 2.4 Continuous-state limit ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) equals ⟨g,ϕj⟩\left\langle g,\phi\_{j}\right\rangle since ⟨ϕi,ϕj⟩=δi​j\left\langle\phi\_{i},\phi\_{j}\right\rangle=\delta\_{ij} by orthonormality.
∎

### A.9 Proof of Proposition [8](https://arxiv.org/html/2601.14852v1#Thmprop8 "Proposition 8 (Zero correlation). ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")

###### Proof.

To simplify notation in the proof, we let xx denote stock 1 (S1,TS\_{1,T}) and yy denotes stock 2 (S2,TS\_{2,T}). Similarly, the support of both stock will be denoted by the intervals [x1,xn][x\_{1},x\_{n}] and [y1,yn][y\_{1},y\_{n}]. By a straightforward extension of Equation ([8](https://arxiv.org/html/2601.14852v1#S2.E8 "In Proposition 1. ‣ 2.4 Continuous-state limit ‣ 2 Estimating nonlinear payoffs using projection ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")), g^\hat{g} solves the approximation problem

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫x1xn∫y1yn(x​y−g^​(x,y))2​d​y​d​x.\int\_{x\_{1}}^{x\_{n}}\int\_{y\_{1}}^{y\_{n}}\left(xy-\hat{g}(x,y)\right)^{2}\mathop{}\!\mathrm{d}y\mathop{}\!\mathrm{d}x. |  | (30) |

We first solve a simpler problem where the function x​yxy is projected on

|  |  |  |
| --- | --- | --- |
|  | g^​(x,y)=β^0+β^1​x+β^2​y.\hat{g}(x,y)=\hat{\beta}\_{0}+\hat{\beta}\_{1}x+\hat{\beta}\_{2}y. |  |

The first order conditions for the (simplified) approximation problem ([30](https://arxiv.org/html/2601.14852v1#A1.E30 "In Proof. ‣ A.9 Proof of Proposition 8 ‣ Appendix A Proofs ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) imply

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | | | | |
|  | ∫x1xn∫y1ynx​y−β^0−β^1​x−β^2​y​d​y​d​x\displaystyle\int\_{x\_{1}}^{x\_{n}}\int\_{y\_{1}}^{y\_{n}}xy-\hat{\beta}\_{0}-\hat{\beta}\_{1}x-\hat{\beta}\_{2}y\mathop{}\!\mathrm{d}y\mathop{}\!\mathrm{d}x | =0\displaystyle=0 |  | (31a) |
|  | ∫x1xn∫y1ynx​(x​y−β^0−β^1​x−β^2​y)​d​y​d​x\displaystyle\int\_{x\_{1}}^{x\_{n}}\int\_{y\_{1}}^{y\_{n}}x\left(xy-\hat{\beta}\_{0}-\hat{\beta}\_{1}x-\hat{\beta}\_{2}y\right)\mathop{}\!\mathrm{d}y\mathop{}\!\mathrm{d}x | =0\displaystyle=0 |  | (31b) |
|  | ∫x1xn∫y1yny​(x​y−β^0−β^1​x−β^2​y)​d​y​d​x\displaystyle\int\_{x\_{1}}^{x\_{n}}\int\_{y\_{1}}^{y\_{n}}y\left(xy-\hat{\beta}\_{0}-\hat{\beta}\_{1}x-\hat{\beta}\_{2}y\right)\mathop{}\!\mathrm{d}y\mathop{}\!\mathrm{d}x | =0.\displaystyle=0. |  | (31c) |

Now define the constants

|  |  |  |  |
| --- | --- | --- | --- |
|  | x¯\displaystyle\bar{x} | =1xn−x1​∫x1xnx​d​x=(xn+x1)/2=𝐄tQ​S1,T\displaystyle=\frac{1}{x\_{n}-x\_{1}}\int\_{x\_{1}}^{x\_{n}}x\mathop{}\!\mathrm{d}x=(x\_{n}+x\_{1})/2=\mathbf{E}\_{t}^{Q}S\_{1,T} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | y¯\displaystyle\bar{y} | =1yn−y1​∫y1yny​d​y=(yn+y1)/2=𝐄tQ​S2,T\displaystyle=\frac{1}{y\_{n}-y\_{1}}\int\_{y\_{1}}^{y\_{n}}y\mathop{}\!\mathrm{d}y=(y\_{n}+y\_{1})/2=\mathbf{E}\_{t}^{Q}S\_{2,T} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | x¯​y¯\displaystyle\bar{x}\bar{y} | =1xn−x1​1yn−y1​∫x1xn∫y1ynx​y​d​y​d​x\displaystyle=\frac{1}{x\_{n}-x\_{1}}\frac{1}{y\_{n}-y\_{1}}\int\_{x\_{1}}^{x\_{n}}\int\_{y\_{1}}^{y\_{n}}xy\mathop{}\!\mathrm{d}y\mathop{}\!\mathrm{d}x |  |

The fact that x¯\bar{x} and y¯\bar{y} are equal to the risk-neutral expectations of the first and second stock follows from the assumption. The first constraint in ([31](https://arxiv.org/html/2601.14852v1#A1.E31 "In Proof. ‣ A.9 Proof of Proposition 8 ‣ Appendix A Proofs ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) forces

|  |  |  |
| --- | --- | --- |
|  | β^0=x¯​y¯−β^1​x¯−β^2​y¯.\hat{\beta}\_{0}=\bar{x}\bar{y}-\hat{\beta}\_{1}\bar{x}-\hat{\beta}\_{2}\bar{y}. |  |

The second and third constraints can thus be expressed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫x1xn∫y1yn(x−x¯)​[x​y−x¯​y¯−β^1​(x−x¯)−β^2​(y−y¯)]​d​y​d​x\displaystyle\int\_{x\_{1}}^{x\_{n}}\int\_{y\_{1}}^{y\_{n}}(x-\bar{x})\left[xy-\bar{x}\bar{y}-\hat{\beta}\_{1}(x-\bar{x})-\hat{\beta}\_{2}(y-\bar{y})\right]\mathop{}\!\mathrm{d}y\mathop{}\!\mathrm{d}x | =0\displaystyle=0 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫x1xn∫y1yn(y−y¯)​[x​y−x¯​y¯−β^1​(x−x¯)−β^2​(y−y¯)]​d​y​d​x\displaystyle\int\_{x\_{1}}^{x\_{n}}\int\_{y\_{1}}^{y\_{n}}(y-\bar{y})\left[xy-\bar{x}\bar{y}-\hat{\beta}\_{1}(x-\bar{x})-\hat{\beta}\_{2}(y-\bar{y})\right]\mathop{}\!\mathrm{d}y\mathop{}\!\mathrm{d}x | =0.\displaystyle=0. |  |

From here, we readily obtain the solution

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | | | | |
|  | β^1\displaystyle\hat{\beta}\_{1} | =∫x1xn∫y1yn(x−x¯)​(x​y−x¯​y¯)​d​y​d​x∫x1xn∫y1yn(x−x¯)2​d​y​d​x=y¯\displaystyle=\frac{\int\_{x\_{1}}^{x\_{n}}\int\_{y\_{1}}^{y\_{n}}(x-\bar{x})(xy-\bar{x}\bar{y})\,\mathop{}\!\mathrm{d}y\mathop{}\!\mathrm{d}x}{\int\_{x\_{1}}^{x\_{n}}\int\_{y\_{1}}^{y\_{n}}(x-\bar{x})^{2}\,\mathop{}\!\mathrm{d}y\mathop{}\!\mathrm{d}x}=\bar{y} |  | (32a) |
|  | β^2\displaystyle\hat{\beta}\_{2} | =∫x1xn∫y1yn(y−y¯)​(x​y−x¯​y¯)​d​y​d​x∫x1xn∫y1yn(y−y¯)2​d​y​d​x=x¯\displaystyle=\frac{\int\_{x\_{1}}^{x\_{n}}\int\_{y\_{1}}^{y\_{n}}(y-\bar{y})(xy-\bar{x}\bar{y})\,\mathop{}\!\mathrm{d}y\mathop{}\!\mathrm{d}x}{\int\_{x\_{1}}^{x\_{n}}\int\_{y\_{1}}^{y\_{n}}(y-\bar{y})^{2}\,\mathop{}\!\mathrm{d}y\mathop{}\!\mathrm{d}x}=\bar{x} |  | (32b) |
|  | β^0\displaystyle\hat{\beta}\_{0} | =−x¯​y¯\displaystyle=-\bar{x}\bar{y} |  | (32c) |

Finally we verify that adding a put or call option basis function yields a coefficient of zero. To see this, without loss of generality, we focus on a basis function of the form (x−K)+\left(x-K\right)^{+}. Using the first order conditions, it is sufficient to show that

|  |  |  |
| --- | --- | --- |
|  | ∫x1xn∫y1yn(x−K)+​(x​y−β^0−β^1​x−β^2​y)​d​y​d​x=0,\int\_{x\_{1}}^{x\_{n}}\int\_{y\_{1}}^{y\_{n}}\left(x-K\right)^{+}\left(xy-\hat{\beta}\_{0}-\hat{\beta}\_{1}x-\hat{\beta}\_{2}y\right)\mathop{}\!\mathrm{d}y\mathop{}\!\mathrm{d}x=0, |  |

where β^0,β^1\hat{\beta}\_{0},\hat{\beta}\_{1} and β^2\hat{\beta}\_{2} are given by ([32a](https://arxiv.org/html/2601.14852v1#A1.E32.1 "In 32 ‣ Proof. ‣ A.9 Proof of Proposition 8 ‣ Appendix A Proofs ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) – ([32c](https://arxiv.org/html/2601.14852v1#A1.E32.3 "In 32 ‣ Proof. ‣ A.9 Proof of Proposition 8 ‣ Appendix A Proofs ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")). Notice that x​y−β^0−β^1​x−β^2​y=(x−x¯)​(y−y¯)xy-\hat{\beta}\_{0}-\hat{\beta}\_{1}x-\hat{\beta}\_{2}y=(x-\bar{x})(y-\bar{y}). So the integral can be written as

|  |  |  |
| --- | --- | --- |
|  | ∫x1xn(x−K)+​(x−x¯)​d​x​∫y1yny−y¯​d​y=0.\int\_{x\_{1}}^{x\_{n}}\left(x-K\right)^{+}(x-\bar{x})\mathop{}\!\mathrm{d}x\int\_{y\_{1}}^{y\_{n}}y-\bar{y}\mathop{}\!\mathrm{d}y=0. |  |

∎

### A.10 Sufficient conditions for ridge representation and the proof of Proposition [9](https://arxiv.org/html/2601.14852v1#Thmprop9 "Proposition 9 (Non-replication). ‣ 4.2 Identification of risk-neutral covariances and correlations ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")

For completeness, we state the result of [[44](https://arxiv.org/html/2601.14852v1#bib.bib110 "Fundamentality of ridge functions")], giving necessary and sufficient conditions for ridge representation to hold. To state the result, some additional terminology is necessary. A polynomial p​(x1,…,xd)p(x\_{1},\dots,x\_{d}) can be associated to the differential operator p​(∂∂x1,…,∂∂xd)p(\frac{\partial}{\partial x\_{1}},\dots,\frac{\partial}{\partial x\_{d}}). Let P​(a1,…,ar)P(a^{1},\dots,a^{r}) be the set of polynomials which vanish on all lines {λ​ai,λ∈ℝ}\left\{{\lambda a^{i},\lambda\in\mathbb{R}}\right\}. Let QQ be the set of polynomials q​(x1,…,xd)q(x\_{1},\dots,x\_{d}) such that p​(∂∂x1,…,∂∂xd)​q=0p(\frac{\partial}{\partial x\_{1}},\dots,\frac{\partial}{\partial x\_{d}})q=0 for all p∈P​(a1,…,ar)p\in P(a^{1},\dots,a^{r}).

###### Proposition 12 ([[44](https://arxiv.org/html/2601.14852v1#bib.bib110 "Fundamentality of ridge functions")]).

Let a1,…,ara^{1},\dots,a^{r} be pairwise linearly independent vectors in ℝd\mathbb{R}^{d}. A function g∈C​(ℝd)g\in C(\mathbb{R}^{d}) can be expressed in the form

|  |  |  |
| --- | --- | --- |
|  | g​(x)=∑i=1rgi​(ai⋅x)g(x)=\sum\_{i=1}^{r}g\_{i}(a^{i}\cdot x) |  |

if and only if gg belongs to the closure of the linear span of Q.

In many practical situations, a more elementary argument suffices to show that a function cannot be written as a ridge combination with given directions aia^{i}. For example, in the case d=3d=3, the following reasoning shows that g​(x)=x1​(w′​x)g(x)=x\_{1}(w^{\prime}x) cannot be expressed as

|  |  |  |
| --- | --- | --- |
|  | g​(x)=g1​(x1)+g2​(x2)+g3​(x3)+g4​(w′​x).g(x)=g\_{1}(x\_{1})+g\_{2}(x\_{2})+g\_{3}(x\_{3})+g\_{4}(w^{\prime}x). |  |

Suppose, by contradiction, that such a representation exists. Then, by differentiating twice, we have ∂2g∂x2​∂x3=0\frac{\partial^{2}g}{\partial x\_{2}\partial x\_{3}}=0. However, ∂2gi∂x2​∂x3\frac{\partial^{2}g\_{i}}{\partial x\_{2}\partial x\_{3}} for i=1,…,3i=1,\dots,3, while ∂2g4∂x2​∂x3=w2​w3​g4′′​(w′​x)\frac{\partial^{2}g\_{4}}{\partial x\_{2}\partial x\_{3}}=w\_{2}w\_{3}g\_{4}^{\prime\prime}(w^{\prime}x). This implies that g4g\_{4} must be affine, but this cannot possibly hold since g​(x)g(x) contains the cross terms x1​x2x\_{1}x\_{2} and x1​x3x\_{1}x\_{3}. This proves Proposition [9](https://arxiv.org/html/2601.14852v1#Thmprop9 "Proposition 9 (Non-replication). ‣ 4.2 Identification of risk-neutral covariances and correlations ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") in case d=3d=3. Notice that we tacitly assume the most favorable scenario where options complete the market for each asset (e.g. using the same assumptions as in Proposition [2](https://arxiv.org/html/2601.14852v1#Thmprop2 "Proposition 2. ‣ 3.1 Market completeness ‣ 3 Completeness, convergence, and distribution estimation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")), so that each gig\_{i} can be estimated with arbitrary accuracy.

The argument generalizes directly to d≥3d\geq 3, thus showing that in higher dimensions it is not possible to perfectly estimate the risk-neutral covariance or correlation of sector ii with the market portfolio.

### A.11 Proof of Proposition [10](https://arxiv.org/html/2601.14852v1#Thmprop10 "Proposition 10 (Odd-moment orthogonality). ‣ 4.3 Projection and equicorrelation ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")

###### Proof.

Let β^\hat{\beta} denote the projection coefficients obtained from the quadratic projection. We need to show that

|  |  |  |
| --- | --- | --- |
|  | ∫A(xi​xj−β^0−∑r=1dβ^r​xr2−β^M​xM2)​xkn​d​x=0,\int\_{A}\left(x\_{i}x\_{j}-\hat{\beta}\_{0}-\sum\_{r=1}^{d}\hat{\beta}\_{r}x\_{r}^{2}-\hat{\beta}\_{M}x\_{M}^{2}\right)x\_{k}^{n}\mathop{}\!\mathrm{d}x=0, |  |

for odd n∈ℕn\in\mathbb{N}, and k∈{1,…,d,M}k\in\left\{{1,\dots,d,M}\right\}. Because each xrnx\_{r}^{n} and xMnx\_{M}^{n} are symmetric around Rf,t→TR\_{f,t\to T}, it follows that β^0​∫Axkn​d​x=0\hat{\beta}\_{0}\int\_{A}x\_{k}^{n}\mathop{}\!\mathrm{d}x=0 for k={1,…,d,M}k=\left\{{1,\dots,d,M}\right\}.

Next suppose that k∈{1,…,d}k\in\left\{{1,\dots,d}\right\}. Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫Axi​xj​xkn​d​x=0.\displaystyle\int\_{A}x\_{i}x\_{j}x\_{k}^{n}\mathop{}\!\mathrm{d}x=0. |  | (33) |

This holds because the integral factors and it always contains an odd moment which vanishes. Using the same reasoning, it follows that

|  |  |  |
| --- | --- | --- |
|  | ∫A∑r=1dβ^r​xr2​xkn​d​x=0.\int\_{A}\sum\_{r=1}^{d}\hat{\beta}\_{r}x\_{r}^{2}x\_{k}^{n}\mathop{}\!\mathrm{d}x=0. |  |

Now we handle the excess market return. Note that because ∑r=1dwr=1\sum\_{r=1}^{d}w\_{r}=1, it follows that

|  |  |  |
| --- | --- | --- |
|  | xM2=∑r=1dwr2​xr2+2​∑1≤j1<j2≤dwj1​wj2​xj1​xj2.x\_{M}^{2}=\sum\_{r=1}^{d}w\_{r}^{2}x\_{r}^{2}+2\sum\_{1\leq j\_{1}<j\_{2}\leq d}w\_{j\_{1}}w\_{j\_{2}}x\_{j\_{1}}x\_{j\_{2}}. |  |

Then, using identical reasoning as before we get

|  |  |  |
| --- | --- | --- |
|  | ∫AxM2​xkn​d​x=0.\int\_{A}x\_{M}^{2}x\_{k}^{n}\mathop{}\!\mathrm{d}x=0. |  |

Suppose now that k=Mk=M (the market return). Ordering the indices i1,…,ini\_{1},\dots,i\_{n} as j1<⋯<jmj\_{1}<\dots<j\_{m} for some 1≤m≤n1\leq m\leq n with each jrj\_{r} occurring with multiplicity ara\_{r}, we then obtain that for n∈ℕn\in\mathbb{N}

|  |  |  |  |
| --- | --- | --- | --- |
|  | (∑i=1dwi​xi)n=∑1≤j1<⋯<jm≤dcn,a1,…​am​wj1a1​xj1a1​…​wjmam​xjmam\left(\sum\_{i=1}^{d}w\_{i}x\_{i}\right)^{n}=\sum\_{1\leq j\_{1}<\dots<j\_{m}\leq d}c\_{n,a\_{1},\dots a\_{m}}w\_{j\_{1}}^{a\_{1}}x\_{j\_{1}}^{a\_{1}}\dots w\_{j\_{m}}^{a\_{m}}x\_{j\_{m}}^{a\_{m}} |  | (34) |

where 1≤m≤n1\leq m\leq n, a1,…,ama\_{1},\dots,a\_{m} are positive integers adding up to nn, and cn,a1,…​amc\_{n,a\_{1},\dots a\_{m}} is the multinomial coefficient

|  |  |  |
| --- | --- | --- |
|  | cn,a1,…​am=n!a1!​…​am!.c\_{n,a\_{1},\dots a\_{m}}=\frac{n!}{a\_{1}!\dots a\_{m}!}. |  |

From the identity ([34](https://arxiv.org/html/2601.14852v1#A1.E34 "In Proof. ‣ A.11 Proof of Proposition 10 ‣ Appendix A Proofs ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")), it follows that for odd n≥3n\geq 3

|  |  |  |
| --- | --- | --- |
|  | ∫Axi​xj​xMn​d​x=0.\int\_{A}x\_{i}x\_{j}x\_{M}^{n}\mathop{}\!\mathrm{d}x=0. |  |

The identity holds by splitting cases. The only way for the integral to be non-zero is if the summand in ([34](https://arxiv.org/html/2601.14852v1#A1.E34 "In Proof. ‣ A.11 Proof of Proposition 10 ‣ Appendix A Proofs ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) contains even powers of xix\_{i} and xjx\_{j}. But if that is the case, then there must be at least one odd power of xkx\_{k} for some k≠i,jk\neq i,j. As shown at the beginning of the proof, the integral of an odd power of xkx\_{k} is zero.

Similar reasoning shows that

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫Axi2​xMn​d​x=0,\int\_{A}x\_{i}^{2}x\_{M}^{n}\mathop{}\!\mathrm{d}x=0, |  | (35) |

because the only reason the integral cannot vanish is when ([34](https://arxiv.org/html/2601.14852v1#A1.E34 "In Proof. ‣ A.11 Proof of Proposition 10 ‣ Appendix A Proofs ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) contains even powers of xix\_{i}. But then by implication there must be at least one odd moment of xkx\_{k} in the product, whose integral vanishes. Because the overall integral factors as a product we conclude ([35](https://arxiv.org/html/2601.14852v1#A1.E35 "In Proof. ‣ A.11 Proof of Proposition 10 ‣ Appendix A Proofs ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")).

Finally, the fact that ∫AxM2​xMn​d​x=0\int\_{A}x\_{M}^{2}x\_{M}^{n}\mathop{}\!\mathrm{d}x=0 follows again because xMn+2x\_{M}^{n+2} is an odd function.

∎

### A.12 Proof of Proposition [11](https://arxiv.org/html/2601.14852v1#Thmprop11 "Proposition 11. ‣ 4.3 Projection and equicorrelation ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")

###### Proof.

We start from the identity

|  |  |  |
| --- | --- | --- |
|  | xM2=∑k=1dwk2​xk2+2​∑1≤i<j≤dwi​wj​xi​xj.x\_{M}^{2}=\sum\_{k=1}^{d}w\_{k}^{2}x\_{k}^{2}+2\sum\_{1\leq i<j\leq d}w\_{i}w\_{j}x\_{i}x\_{j}. |  |

Because ℱ\mathcal{F} contains the quadratic monomials, and because the projection operator Π^ℱ\widehat{\Pi}\_{\mathcal{F}} is linear and idempotent, it follows that

|  |  |  |
| --- | --- | --- |
|  | xM2=∑k=1dwk2​xk2+2​∑1≤i<j≤dwi​wj​Π^ℱ​[xi​xj].x\_{M}^{2}=\sum\_{k=1}^{d}w\_{k}^{2}x\_{k}^{2}+2\sum\_{1\leq i<j\leq d}w\_{i}w\_{j}\widehat{\Pi}\_{\mathcal{F}}[x\_{i}x\_{j}]. |  |

Taking risk-neutral expectations on both sides then completes the proof.
∎

### A.13 Proof of Proposition [13](https://arxiv.org/html/2601.14852v1#Thmprop13 "Proposition 13. ‣ D.2 Incorporating time series information ‣ Appendix D Correlations between sector ETFs and the market portfolio ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")

###### Proof.

By the spectral theorem, write Q​D​Q′=𝐄​(Mt→T​XT​XT′)QDQ^{\prime}=\mathbf{E}\left(M\_{t\to T}X\_{T}X\_{T}^{\prime}\right). Since 𝐄​(Mt→T​XT​XT′)\mathbf{E}\left(M\_{t\to T}X\_{T}X\_{T}^{\prime}\right) is positive definite by assumption, it follows that all eigenvalues on the diagonal of DD are positive. Hence,

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖bQ−b‖22\displaystyle\left\lVert b^{Q}-b\right\rVert\_{2}^{2} | =𝐄​(Mt→T​XT​eT)′​Q​D−2​Q′​𝐄​(Mt→T​XT​eT)\displaystyle=\mathbf{E}\left(M\_{t\to T}X\_{T}e\_{T}\right)^{\prime}QD^{-2}Q^{\prime}\mathbf{E}\left(M\_{t\to T}X\_{T}e\_{T}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =𝐄​((Mt→T−1)​XT​eT)′​Q​D−2​Q′​𝐄​((Mt→T−1)​XT​eT)\displaystyle=\mathbf{E}\left((M\_{t\to T}-1)X\_{T}e\_{T}\right)^{\prime}QD^{-2}Q^{\prime}\mathbf{E}\left((M\_{t\to T}-1)X\_{T}e\_{T}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤1λmin2​‖𝐄​((Mt→T−1)​XT​eT)‖22\displaystyle\leq\frac{1}{\lambda\_{\min}^{2}}\left\lVert\mathbf{E}\left((M\_{t\to T}-1)X\_{T}e\_{T}\right)\right\rVert\_{2}^{2} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤1λmin2​(1+∑i=12𝐄​[Ri,t→T4]1/2)​𝐄​((Mt→T−1)4)1/2​σ2.\displaystyle\leq\frac{1}{\lambda\_{\min}^{2}}\left(1+\sum\_{i=1}^{2}\mathbf{E}\left[R\_{i,t\to T}^{4}\right]^{1/2}\right)\mathbf{E}\left((M\_{t\to T}-1)^{4}\right)^{1/2}\sigma^{2}. |  |

In the third line we use that for y=Q′​𝐄​((Mt→T−1)​XT​eT)y=Q^{\prime}\mathbf{E}\left((M\_{t\to T}-1)X\_{T}e\_{T}\right),

|  |  |  |
| --- | --- | --- |
|  | y′​y=𝐄​((Mt→T−1)​XT​eT)′​𝐄​((Mt→T−1)​XT​eT),andy′​D−2​y≤(1/λmin2)​y′​y.y^{\prime}y=\mathbf{E}\left((M\_{t\to T}-1)X\_{T}e\_{T}\right)^{\prime}\mathbf{E}\left((M\_{t\to T}-1)X\_{T}e\_{T}\right),\quad\text{and}\quad y^{\prime}D^{-2}y\leq(1/\lambda\_{\min}^{2})y^{\prime}y. |  |

The final inequality follows by repeated application of the Cauchy-Schwarz inequality:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐄​((Mt→T−1)​Ri,t→T​eT)2\displaystyle\mathbf{E}\left((M\_{t\to T}-1)R\_{i,t\to T}e\_{T}\right)^{2} | ≤𝐄​((Mt→T−1)2​Ri,t→T2)​𝐄​(eT2)\displaystyle\leq\mathbf{E}\left((M\_{t\to T}-1)^{2}R\_{i,t\to T}^{2}\right)\mathbf{E}(e\_{T}^{2}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≤𝐄​((Mt→T−1)4)1/2​𝐄​(Ri,t→T4)1/2​𝐄​(eT2).\displaystyle\leq\mathbf{E}\left((M\_{t\to T}-1)^{4}\right)^{1/2}\mathbf{E}\left(R\_{i,t\to T}^{4}\right)^{1/2}\mathbf{E}(e\_{T}^{2}). |  |

∎

### A.14 Proof of Proposition [14](https://arxiv.org/html/2601.14852v1#Thmprop14 "Proposition 14. ‣ D.2 Incorporating time series information ‣ Appendix D Correlations between sector ETFs and the market portfolio ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")

###### Proof.

Because ee is independent of returns and the SDF it follows that

|  |  |  |
| --- | --- | --- |
|  | 𝐕𝐚𝐫tQ​(R3,t→T)−b12​𝐕𝐚𝐫tQ​(R1,t→T)−b22​𝐕𝐚𝐫tQ​(R2,t→T)≥2​b1​b2​𝐂𝐨𝐯tQ(R1,t→T,R2,t→T).\mathbf{Var}\_{t}^{Q}(R\_{3,t\to T})-b\_{1}^{2}\mathbf{Var}\_{t}^{Q}\left(R\_{1,t\to T}\right)-b\_{2}^{2}\mathbf{Var}\_{t}^{Q}\left(R\_{2,t\to T}\right)\geq 2b\_{1}b\_{2}\mathop{\mathbf{Cov}}\nolimits\_{t}^{Q}\left(R\_{1,t\to T},R\_{2,t\to T}\right). |  |

If b1​b2<0b\_{1}b\_{2}<0, then 𝐂𝐨𝐯tQ(R1,t→T,R2,t→T)≥𝐂𝐨𝐯^tQ​(R1,t→T,R2,t→T)\mathop{\mathbf{Cov}}\nolimits\_{t}^{Q}\left(R\_{1,t\to T},R\_{2,t\to T}\right)\geq\widehat{\mathop{\mathbf{Cov}}\nolimits}\_{t}^{Q}\left(R\_{1,t\to T},R\_{2,t\to T}\right). Clearly the inequality reverses if b1​b2>0b\_{1}b\_{2}>0.
∎

## Appendix B Option data preprocessing

We use SP500 option data from OptionMetrics, covering the period January 4, 1996 to July 20, 2023. Following the CBOE procedure, we discard all in-the-money put and call options, as well as any option with a bid price of zero. When there are two consecutive strikes with a bid price equal to zero, all options with higher strikes (for calls) or lower strikes (for puts) are discarded. For each remaining option, the price is defined as the average of the bid and ask prices. In total, this filtering yields 11.738 million option prices. The risk-free rate for each return horizon is obtained from the zero-coupon yield curve dataset provided by OptionMetrics.

### B.1 ETF options and conversion of American option price

Options on SPY, XLK, and SPXT are recorded as American in OptionMetrics. To estimate the risk-neutral volatility, we first convert these quotes to European-equivalent prices. For each option we compute the Black–Scholes price using the forward price and implied volatility reported by OptionMetrics; this conversion accounts for dividends via the forward.161616As in [[47](https://arxiv.org/html/2601.14852v1#bib.bib67 "What is the expected return on the market?"), [41](https://arxiv.org/html/2601.14852v1#bib.bib83 "The quanto theory of exchange rates")], we assume dividends are known in advance and paid at time TT.

After this conversion, our preprocessing for SPY is identical to Section [B](https://arxiv.org/html/2601.14852v1#A2 "Appendix B Option data preprocessing ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"). For XLK and SPXT, by contrast, in-the-money options are often liquid, so we retain both in- and out-of-the-money quotes. Furthermore, we discard only options with zero bid prices, rather than also truncating the strike range after two consecutively observed zero-bid options.

## Appendix C Details on simulation

In the Monte-Carlo simulation, we use two different models to generate option prices. In both cases the time to maturity is 1 year. The first model is the standard [[10](https://arxiv.org/html/2601.14852v1#bib.bib20 "The pricing of options and corporate liabilities")] model with a risk-free rate of 5% and volatility of 20%. The simulation of the stochastic volatility jump (SVCJ) model is based on [[30](https://arxiv.org/html/2601.14852v1#bib.bib82 "The impact of jumps in volatility and returns")]. In their setup, the log asset price follows

|  |  |  |
| --- | --- | --- |
|  | (d​log⁡Std​Vt)=(μκ​(θ−Vt−))​d​t+Vt−​(10ρ​σv1−ρ2​σv)​d​Wt+(ξyξv)​d​Nt,\begin{pmatrix}\mathop{}\!\mathrm{d}\log S\_{t}\\ \mathop{}\!\mathrm{d}V\_{t}\end{pmatrix}=\begin{pmatrix}\mu\\ \kappa\left(\theta-V\_{t-}\right)\end{pmatrix}\mathop{}\!\mathrm{d}t+\sqrt{V\_{t-}}\begin{pmatrix}1&0\\ \rho\sigma\_{v}&\sqrt{1-\rho^{2}}\sigma\_{v}\end{pmatrix}\mathop{}\!\mathrm{d}W\_{t}+\begin{pmatrix}\xi^{y}\\ \xi^{v}\end{pmatrix}\mathop{}\!\mathrm{d}N\_{t}, |  |

where Vt−=lims↑tVsV\_{t-}=\lim\_{s\uparrow t}V\_{s} denotes the left limit, WtW\_{t} is a standard two-dimensional Brownian motion, NtN\_{t} is a Poisson process with intensity λ\lambda, and ξy,ξv\xi^{y},\xi^{v} are the jump sizes in returns and volatility. These jump sizes are correlated and have distributions ξv∼exp⁡(μv)\xi^{v}\sim\exp(\mu\_{v}) and ξy|ξv∼𝖭​(μy+ρJ​ξv,σy2)\xi^{y}|\xi^{v}\sim\mathsf{N}\left(\mu\_{y}+\rho\_{J}\xi^{v},\sigma\_{y}^{2}\right). For simulation, we only need to calibrate the model under the risk-neutral measure. The risk-neutral parameters are taken from [[17](https://arxiv.org/html/2601.14852v1#bib.bib89 "Model specification and risk premia: evidence from futures options")] and are summarized in Table [4](https://arxiv.org/html/2601.14852v1#A3.T4 "Table 4 ‣ Appendix C Details on simulation ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").

| Parameter | Value |
| --- | --- |
| κ\kappa | 0.05700.0570 |
| θ\theta | 0.00620.0062 |
| ρ\rho | −0.4838-0.4838 |
| σv\sigma\_{v} | 0.08000.0800 |
| μv\mu\_{v} | 0.22130.2213 |
| μy\mu\_{y} | −0.0539-0.0539 |
| ρJ\rho\_{J} | 0.00000.0000 |
| σy\sigma\_{y} | 0.05780.0578 |
| λ\lambda | 1.51201.5120 |
| rr | 0.05000.0500 |

Table 4: SVCJ model calibration

## Appendix D Correlations between sector ETFs and the market portfolio

In this section, we present empirical estimates from several settings in which options on the market portfolio and its constituents are used to estimate risk-neutral correlations.

### D.1 ETF correlation

The first application considers the estimation of risk-neutral correlations for the eleven sector ETFs following the approach of Section [4.3](https://arxiv.org/html/2601.14852v1#S4.SS3 "4.3 Projection and equicorrelation ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"). The tickers and their sectors are listed in Appendix Table [6](https://arxiv.org/html/2601.14852v1#A5.T6 "Table 6 ‣ Appendix E Additional tables ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"). In addition, we use two portfolios written on sector returns: (i) SPY, which tracks the S&P500 and is a value-weighted combination of sector returns, and (ii) EQL, which is an equal-weighted average of the sector returns. In light of Theorem [2](https://arxiv.org/html/2601.14852v1#Thmthm2 "Theorem 2. ‣ 4.1 Identifying joint dependence from options on multiple portfolios ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"), this additional variation in portfolio weights enhances spanning and improves correlation estimation. Because options on EQL were introduced only in April 2023, the resulting time series is relatively short. Throughout, the correlation horizon is 30 days.

Since options are available on all sector ETFs and on the portfolio ETFs, we estimate correlations using ([4.3](https://arxiv.org/html/2601.14852v1#S4.Ex50 "4.3 Projection and equicorrelation ‣ 4 Completeness in multiple asset markets and joint dependence ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")). Owing to the high dimensionality (55 pairwise correlations per date), some raw estimates fall outside [−1,1][-1,1], and the corresponding correlation matrix need not be positive definite. To address this, we shrink the estimated correlation matrix toward the equicorrelation matrix, which is always well behaved. Such shrinkage is known to improve accuracy (see, e.g., [[43](https://arxiv.org/html/2601.14852v1#bib.bib51 "Improved estimation of the covariance matrix of stock returns with an application to portfolio selection")]). We choose the shrinkage intensity so that the smallest eigenvalue of the estimated correlation matrix is at least 10−310^{-3}.

Figure [6](https://arxiv.org/html/2601.14852v1#A4.F6 "Figure 6 ‣ D.1 ETF correlation ‣ Appendix D Correlations between sector ETFs and the market portfolio ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") reports the correlations for Finance & Technology and Finance & Energy. Both series exhibit substantial time variation, with values roughly between 0 and 0.6. The figure also shows pronounced cross-sectional heterogeneity: in the early sample, Finance & Energy appears more correlated, whereas in the latter half Finance & Technology is higher.

![Refer to caption](x17.png)


Figure 6: Risk-neutral correlations. Estimated correlations for Finance & Technology and Finance & Energy.

### D.2 Incorporating time series information

We present an additional approach that makes it possible to estimate conditional covariances and correlations using information from the time-series of returns. The idea is to find a third asset which is closely spanned by the returns of asset 1 and 2. If all three assets have options available, it becomes possible to estimate a nonzero correlation because the third asset effectively serves as a basket option.

More precisely, consider the projection of a third asset on the returns of assets one and two under the physical measure

|  |  |  |  |
| --- | --- | --- | --- |
|  | R3,t→T=b0+b1​R1,t→T+b2​R2,t→T+eT,R\_{3,t\to T}=b\_{0}+b\_{1}R\_{1,t\to T}+b\_{2}R\_{2,t\to T}+e\_{T}, |  | (36) |

where by definition 𝐄​(eT)=0,𝐂𝐨𝐯(R1,t→T,eT)=0\mathbf{E}(e\_{T})=0,\mathop{\mathbf{Cov}}\nolimits(R\_{1,t\to T},e\_{T})=0 and 𝐂𝐨𝐯(R2,t→T,eT)=0\mathop{\mathbf{Cov}}\nolimits(R\_{2,t\to T},e\_{T})=0. This relation may mechanically hold with e≡0e\equiv 0 if, for example, the return of asset 3 corresponds to a fund that only invests in assets and 1 and 2. More realistically, the linear relationship may have some error eTe\_{T} whose variance is very small, so that the R2R^{2} of a regression in ([36](https://arxiv.org/html/2601.14852v1#A4.E36 "In D.2 Incorporating time series information ‣ Appendix D Correlations between sector ETFs and the market portfolio ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) is very close to 1. An empirical example of such a case is given in Example [6](https://arxiv.org/html/2601.14852v1#Thmexmp6 "Example 6. ‣ D.2 Incorporating time series information ‣ Appendix D Correlations between sector ETFs and the market portfolio ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") below.

The upshot is that if ([36](https://arxiv.org/html/2601.14852v1#A4.E36 "In D.2 Incorporating time series information ‣ Appendix D Correlations between sector ETFs and the market portfolio ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) holds with zero error, then the exact same relation should hold under QQ because the physical and risk-neutral measures are equivalent. Even when ([36](https://arxiv.org/html/2601.14852v1#A4.E36 "In D.2 Incorporating time series information ‣ Appendix D Correlations between sector ETFs and the market portfolio ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")) holds with some small error, the same relation should continue to be a good approximation under QQ. To see this algebraically, let XT=[1,R1,t→T,R2,t→T]′X\_{T}=[1,R\_{1,t\to T},R\_{2,t\to T}]^{\prime} and let Mt→TM\_{t\to T} denote the SDF that prices the three returns, then it follows from the least squares solution that the projection coefficient under QQ is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | bQ\displaystyle b^{Q} | =𝐄​(Mt→T​XT​XT′)−1​𝐄​(Mt→T​XT​R3,t→T)\displaystyle=\mathbf{E}\left(M\_{t\to T}X\_{T}X\_{T}^{\prime}\right)^{-1}\mathbf{E}\left(M\_{t\to T}X\_{T}R\_{3,t\to T}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =b+𝐄​(Mt→T​XT​XT′)−1​𝐄​(Mt→T​XT​eT).\displaystyle=b+\mathbf{E}\left(M\_{t\to T}X\_{T}X\_{T}^{\prime}\right)^{-1}\mathbf{E}\left(M\_{t\to T}X\_{T}e\_{T}\right). |  |

Clearly, if eT=0e\_{T}=0 for all TT, then bQ=bb^{Q}=b. More generally, bQ=bb^{Q}=b if eTe\_{T} is truly idiosyncratic so that eT⟂[XT′,Mt→T]′e\_{T}\perp[X\_{T}^{\prime},M\_{t\to T}]^{\prime}. Another equality case occurs in the (counterfactual) case when the world is risk-neutral, so that Mt→T≡1M\_{t\to T}\equiv 1. In the more realistic case when the world is not risk-neutral and the error term is non-degenerate with variance σ2=𝐕𝐚𝐫​(eT)\sigma^{2}=\mathbf{Var}(e\_{T}), we can still bound the difference between the physical and risk-neutral projection coefficient.

###### Proposition 13.

Suppose that 𝐄​(Mt→T​XT​XT′)\mathbf{E}\left(M\_{t\to T}X\_{T}X\_{T}^{\prime}\right) is a positive definite matrix and denote its smallest eigenvalue by λmin\lambda\_{\min}. Furthermore, assume that 𝐄​Mt→T4<∞\mathbf{E}M\_{t\to T}^{4}<\infty and 𝐄​Ri,t→T4<∞\mathbf{E}R\_{i,t\to T}^{4}<\infty for i=1,2i=1,2. Then,

|  |  |  |
| --- | --- | --- |
|  | ‖bQ−b‖22≤1λmin2​(1+∑i=12𝐄​[Ri,t→T4]1/2)​𝐄​[(Mt→T−1)4]1/2​σ2.\left\lVert b^{Q}-b\right\rVert\_{2}^{2}\leq\frac{1}{\lambda\_{\min}^{2}}\left(1+\sum\_{i=1}^{2}\mathbf{E}\left[R\_{i,t\to T}^{4}\right]^{1/2}\right)\mathbf{E}\left[(M\_{t\to T}-1)^{4}\right]^{1/2}\sigma^{2}. |  |

Hence, the risk-neutral projection coefficient is close to its physical counterpart if the world is close to risk-neutral as measured by the fourth central moment of the SDF, or if the projection error variance is small. The latter condition is obviously more relevant in practice.

If the projection error variance is small, and if options are available on the three returns, then it becomes possible to estimate the conditional risk-neutral correlation between R1,t→TR\_{1,t\to T} and R2,t→TR\_{2,t\to T}. Specifically, under the asymptotics where σ→0\sigma\to 0 as T→∞T\to\infty it follows that171717The error term O​(σ)O(\sigma) follows immediately from the Cauchy-Schwarz inequality applied to 𝐂𝐨𝐯tQ(Ri,t→T,eT)\mathop{\mathbf{Cov}}\nolimits\_{t}^{Q}(R\_{i,t\to T},e\_{T}). Strictly speaking, the notation for the conditional moments should also depend on TT, as we are working with a triangular array, but this dependence is suppressed to avoid cluttering the derivation.

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐕𝐚𝐫tQ​(R3,t→T)\displaystyle\mathbf{Var}\_{t}^{Q}(R\_{3,t\to T}) | =𝐕𝐚𝐫tQ​(b1​R1,t→T+b2​R2,t→T)+O​(σ)\displaystyle=\mathbf{Var}\_{t}^{Q}\left(b\_{1}R\_{1,t\to T}+b\_{2}R\_{2,t\to T}\right)+O(\sigma) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =b12​𝐕𝐚𝐫tQ​(R1,t→T)+b22​𝐕𝐚𝐫tQ​(R2,t→T)+2​b1​b2​𝐂𝐨𝐯tQ(R1,t→T,R2,t→T)+O​(σ).\displaystyle=b\_{1}^{2}\mathbf{Var}\_{t}^{Q}\left(R\_{1,t\to T}\right)+b\_{2}^{2}\mathbf{Var}\_{t}^{Q}\left(R\_{2,t\to T}\right)+2b\_{1}b\_{2}\mathop{\mathbf{Cov}}\nolimits\_{t}^{Q}\left(R\_{1,t\to T},R\_{2,t\to T}\right)+O(\sigma). |  |

Ignoring the error induced by the projection volatility, we obtain the feasible approximation

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐂𝐨𝐯tQ(R1,t→T,R2,t→T)\displaystyle\mathop{\mathbf{Cov}}\nolimits\_{t}^{Q}\left(R\_{1,t\to T},R\_{2,t\to T}\right) | ≈𝐕𝐚𝐫tQ​(R3,t→T)−b12​𝐕𝐚𝐫tQ​(R1,t→T)−b22​𝐕𝐚𝐫tQ​(R2,t→T)2​b1​b2\displaystyle\approx\frac{\mathbf{Var}\_{t}^{Q}(R\_{3,t\to T})-b\_{1}^{2}\mathbf{Var}\_{t}^{Q}\left(R\_{1,t\to T}\right)-b\_{2}^{2}\mathbf{Var}\_{t}^{Q}\left(R\_{2,t\to T}\right)}{2b\_{1}b\_{2}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ≕𝐂𝐨𝐯^tQ​(R1,t→T,R2,t→T).\displaystyle\eqqcolon\widehat{\mathop{\mathbf{Cov}}\nolimits}\_{t}^{Q}\left(R\_{1,t\to T},R\_{2,t\to T}\right). |  |

The bias of the covariance estimate can be signed if we assume that the error term is idiosyncratic.

###### Proposition 14.

Suppose the error term is independent of the SDF and returns, i.e. eT⟂[XT′,Mt→T]′e\_{T}\perp[X\_{T}^{\prime},M\_{t\to T}]^{\prime}, then

|  |  |  |
| --- | --- | --- |
|  | {𝐂𝐨𝐯^tQ​(R1,t→T,R2,t→T)≤𝐂𝐨𝐯tQ(R1,t→T,R2,t→T)ifb1​b2<0𝐂𝐨𝐯^tQ​(R1,t→T,R2,t→T)≥𝐂𝐨𝐯tQ(R1,t→T,R2,t→T)ifb1​b2>0.\begin{cases}\widehat{\mathop{\mathbf{Cov}}\nolimits}\_{t}^{Q}\left(R\_{1,t\to T},R\_{2,t\to T}\right)\leq\mathop{\mathbf{Cov}}\nolimits\_{t}^{Q}\left(R\_{1,t\to T},R\_{2,t\to T}\right)&\text{if}\quad b\_{1}b\_{2}<0\\ \widehat{\mathop{\mathbf{Cov}}\nolimits}\_{t}^{Q}\left(R\_{1,t\to T},R\_{2,t\to T}\right)\geq\mathop{\mathbf{Cov}}\nolimits\_{t}^{Q}\left(R\_{1,t\to T},R\_{2,t\to T}\right)&\text{if}\quad b\_{1}b\_{2}>0.\end{cases} |  |

In anticipation of the empirical application, we illustrate how these results can be applied in the example below. There we find that b1​b2<0b\_{1}b\_{2}<0, so that the estimated covariance is expected to underestimate the true covariance, provided the error term is idiosynchratic.

###### Example 6.

The ProShares S&P500 ex-Technology ETF (SPXT) tracks the performance of the S&P500 excluding the technology sector. In contrast, the Technology Select Sector SPDR Fund (XLK) tracks only technology stocks within the S&P500, while the SPDR S&P500 ETF (SPY) tracks the full index. We therefore expect SPXT returns to be closely spanned by returns on SPY and XLK:

|  |  |  |
| --- | --- | --- |
|  | Rt→TSPXT=b0+b1​Rt→TSPY+b2​Rt→TXLK+eT.R\_{t\to T}^{\text{SPXT}}=b\_{0}+b\_{1}R\_{t\to T}^{\text{SPY}}+b\_{2}R\_{t\to T}^{\text{XLK}}+e\_{T}. |  |

Figure [7](https://arxiv.org/html/2601.14852v1#A4.F7 "Figure 7 ‣ D.2 Incorporating time series information ‣ Appendix D Correlations between sector ETFs and the market portfolio ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") confirms this, with scatter points lying close to the 45-degree line. Regression results in Table [5](https://arxiv.org/html/2601.14852v1#A4.T5 "Table 5 ‣ D.2 Incorporating time series information ‣ Appendix D Correlations between sector ETFs and the market portfolio ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") show an adjusted R2R^{2} near 1, and both regressors are individually significant. The estimated weight on SPY exceeds 1, while the weight on XLK is negative, consistent with SPXT having no exposure to technology return shocks. As a further check that the projection coefficients are close to their risk-neutral counterparts bQb^{Q}, note that under QQ, if the projection error is uncorrelated with the SDF, the asset pricing equation implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1\displaystyle 1 | =𝐄​[Mt→T​Rt→TSPXT]=b0​𝐄​[Mt→T]+b1​𝐄​[Mt→T​Rt→TSPY]+b2​𝐄​[Mt→T​Rt→TXLK]\displaystyle=\mathbf{E}\left[M\_{t\to T}R\_{t\to T}^{\text{SPXT}}\right]=b\_{0}\mathbf{E}\left[M\_{t\to T}\right]+b\_{1}\mathbf{E}\left[M\_{t\to T}R\_{t\to T}^{\text{SPY}}\right]+b\_{2}\mathbf{E}\left[M\_{t\to T}R\_{t\to T}^{\text{XLK}}\right] |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =b0​𝐄​(1Rf,t→T)+b1+b2.\displaystyle=b\_{0}\mathbf{E}\left(\frac{1}{R\_{f,t\to T}}\right)+b\_{1}+b\_{2}. |  | (37) |

The bottom row in Table [5](https://arxiv.org/html/2601.14852v1#A4.T5 "Table 5 ‣ D.2 Incorporating time series information ‣ Appendix D Correlations between sector ETFs and the market portfolio ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") shows that this restriction on the coefficients cannot be rejected.

![Refer to caption](x18.png)


Figure 7: SPXT return projection. The figure shows a scatter plot of the SPXT return (y-axis) and the predicted SPXT return (x-axis) obtained from the projection Rt→TSPXT=b0+b1​Rt→TSPY+b2​Rt→TXLK+eTR\_{t\to T}^{\text{SPXT}}=b\_{0}+b\_{1}R\_{t\to T}^{\text{SPY}}+b\_{2}R\_{t\to T}^{\text{XLK}}+e\_{T}.



|  |  |
| --- | --- |
| Intercept | 0.029(0.0191)\underset{(\text{0.0191})}{\text{0.029}} |
| RSPYR^{\text{SPY}} | 1.267(0.0425)\underset{(\text{0.0425})}{\text{1.267}} |
| RXLKR^{\text{XLK}} | -0.297(0.0336)\underset{(\text{0.0336})}{\text{-0.297}} |
| Adj. R2R^{2} (%) | 95.78 |
| # obs | 118 |
| Heteroscedasticity test (pp-value) | 0.220 |
| Restriction test (pp-value) | 0.572 |

Table 5: Technology stock regression. This table shows estimates of the regression Rt→TSPXT=b0+b1​Rt→TSPY+b2​Rt→TXLK+eTR\_{t\to T}^{\text{SPXT}}=b\_{0}+b\_{1}R\_{t\to T}^{\text{SPY}}+b\_{2}R\_{t\to T}^{\text{XLK}}+e\_{T}, where RSPXTR^{\text{SPXT}} denotes the monthly return of the ETF that invests in the SP500 excluding technology, RSPYR^{\text{SPY}} is the return on the ETF that tracks the SP500, and RXLKR^{\text{XLK}} denotes the return on the ETF that only tracks the technology sector. The bottom two rows denote pp-values of the [[59](https://arxiv.org/html/2601.14852v1#bib.bib93 "A heteroskedasticity-consistent covariance matrix estimator and a direct test for heteroskedasticity")] heteroscedasticity test, and the linear restriction test on the coefficients in ([6](https://arxiv.org/html/2601.14852v1#A4.Ex31 "Example 6. ‣ D.2 Incorporating time series information ‣ Appendix D Correlations between sector ETFs and the market portfolio ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")). The time period is from October 2015 until July 2025.

### D.3 Conditional covariance and correlation estimates of the technology sector

Example [6](https://arxiv.org/html/2601.14852v1#Thmexmp6 "Example 6. ‣ D.2 Incorporating time series information ‣ Appendix D Correlations between sector ETFs and the market portfolio ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") shows that the return on a portfolio of technology stocks is closely spanned by the market portfolio and a portfolio excluding technology stocks (SPXT). We exploit this observation to estimate conditional covariances between the technology sector and the market portfolio. This is feasible because options data are available for all three ETFs. SPY and XLK have long option histories, whereas SPXT options have only been listed since March 2022. Although this period is short, the daily frequency of our estimates still allows us to uncover meaningful dynamics. Moreover, this setting provides an ideal test for the projection method, since options on SPXT are relatively scarce, making an accurate estimation approach essential when only few contracts are observed.

Since all three tickers have American-style options, we first convert their prices to European option prices before estimating the risk-neutral variance.181818That is, we remove the early-exercise premium. XLK and SPXT options also differ from SPY in that in-the-money contracts are far more common and liquid. Owing to these differences, we use a different data preprocessing procedure than in Section [6.1](https://arxiv.org/html/2601.14852v1#S6.SS1 "6.1 Empirical estimates of SVIX and VIX ‣ 6 Empirical application ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"). The details are in Appendix [B.1](https://arxiv.org/html/2601.14852v1#A2.SS1 "B.1 ETF options and conversion of American option price ‣ Appendix B Option data preprocessing ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation").

Subsequently, we estimate the risk-neutral variance of each of the tickers at each time period tt. We use an expanding window until time tt to estimate the physical projection coefficients

|  |  |  |
| --- | --- | --- |
|  | RT1,T2SPXT=b0,t+b1,t​RT1,T2SPY+b2,t​RT1,T2XLK+eT2,T2≤t.R\_{T\_{1},T\_{2}}^{\text{SPXT}}=b\_{0,t}+b\_{1,t}R\_{T\_{1},T\_{2}}^{\text{SPY}}+b\_{2,t}R\_{T\_{1},T\_{2}}^{\text{XLK}}+e\_{T\_{2}},\quad T\_{2}\leq t. |  |

The expanding window is used to make the correlation estimates feasible in real time.191919SPXT began trading in October 2015, while options were introduced in March 2022. Hence, the initial projection estimates are based on 6.5 years of data, which amounts to roughly 78 monthly return observations. Evidence from Table [5](https://arxiv.org/html/2601.14852v1#A4.T5 "Table 5 ‣ D.2 Incorporating time series information ‣ Appendix D Correlations between sector ETFs and the market portfolio ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") suggest that these coefficients are close to their risk-neutral counterpart. The conditional covariance and correlation are finally estimated by

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐂𝐨𝐯^tQ​(Rt→TSPY,Rt→TXLK)\displaystyle\widehat{\mathop{\mathbf{Cov}}\nolimits}\_{t}^{Q}\left(R\_{t\to T}^{\text{SPY}},R\_{t\to T}^{\text{XLK}}\right) | =𝐕𝐚𝐫tQ​(Rt→TSPXT)−b1,t2​𝐕𝐚𝐫tQ​(Rt→TSPY)−b2,t2​𝐕𝐚𝐫tQ​(Rt→TXLK)2​b1,t​b2,t\displaystyle=\frac{\mathbf{Var}\_{t}^{Q}(R\_{t\to T}^{\text{SPXT}})-b\_{1,t}^{2}\mathbf{Var}\_{t}^{Q}\left(R\_{t\to T}^{\text{SPY}}\right)-b\_{2,t}^{2}\mathbf{Var}\_{t}^{Q}\left(R\_{t\to T}^{\text{XLK}}\right)}{2b\_{1,t}b\_{2,t}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝐂𝐨𝐫𝐫^tQ​(Rt→TSPY,Rt→TXLK)\displaystyle\widehat{\mathbf{Corr}}\_{t}^{Q}\left(R\_{t\to T}^{\text{SPY}},R\_{t\to T}^{\text{XLK}}\right) | =𝐂𝐨𝐯^tQ​(Rt→TSPY,Rt→TXLK)𝐕𝐚𝐫tQ​(Rt→TSPY)​𝐕𝐚𝐫tQ​(Rt→TXLK).\displaystyle=\frac{\widehat{\mathop{\mathbf{Cov}}\nolimits}\_{t}^{Q}\left(R\_{t\to T}^{\text{SPY}},R\_{t\to T}^{\text{XLK}}\right)}{\sqrt{\mathbf{Var}\_{t}^{Q}\left(R\_{t\to T}^{\text{SPY}}\right)\mathbf{Var}\_{t}^{Q}\left(R\_{t\to T}^{\text{XLK}}\right)}}. |  | (38) |

Figure [8](https://arxiv.org/html/2601.14852v1#A4.F8 "Figure 8 ‣ D.3 Conditional covariance and correlation estimates of the technology sector ‣ Appendix D Correlations between sector ETFs and the market portfolio ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation") presents the results of these estimates. The upper panels use the projection method, while the lower panels use the CM formula to estimate all risk-neutral quantities. The correlation estimates indicate that the projection method delivers much more reliable results, as the estimates remain within the theoretical range [−1,1][-1,1].202020The figure reports a 15-day backward-looking moving average. While the projection method occasionally produces point estimates slightly above 1, such instances are rare. In contrast, the CM formula yields point estimates that are almost always outside [−1,1][-1,1], as is also apparent in the moving average plot. This finding is encouraging because our approach to back out the correlation does not impose the Cauchy–Schwarz inequality.

The difficulty of obtaining reliable correlation estimates can be illustrated by the denominator in ([38](https://arxiv.org/html/2601.14852v1#A4.E38 "In D.3 Conditional covariance and correlation estimates of the technology sector ‣ Appendix D Correlations between sector ETFs and the market portfolio ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation")): its reciprocal has an average value of about 211, while the average risk-neutral variance of SPXT is around 0.0040.004. A mere 1% measurement error in the latter can therefore change the estimated correlation by roughly 0.08. In this setting, accurate estimation of the risk-neutral variance is crucial—something the projection method achieves, but the CM method does not, due to the scarcity of options available on SPXT.

Our method therefore provides confidence that the risk-neutral correlation, and hence the covariance, are well estimated. We can interpret this risk-neutral covariance using the general framework of [[49](https://arxiv.org/html/2601.14852v1#bib.bib92 "Information in derivatives markets: forecasting prices with prices")], who shows how it links to the forward-looking equity premium:

|  |  |  |
| --- | --- | --- |
|  | 𝐄t​Rt→TXLK−Rf,t→T=1Rf,t→T​𝐂𝐨𝐯tQ(Rt→TXLK,Rt→TSPY)−𝐂𝐨𝐯t(Rt→TXLK,Rt→TSPY​MT).\mathbf{E}\_{t}R\_{t\to T}^{\text{XLK}}-R\_{f,t\to T}=\frac{1}{R\_{f,t\to T}}\mathop{\mathbf{Cov}}\nolimits\_{t}^{Q}\left(R\_{t\to T}^{\text{XLK}},R\_{t\to T}^{\text{SPY}}\right)-\mathop{\mathbf{Cov}}\nolimits\_{t}\left(R\_{t\to T}^{\text{XLK}},R\_{t\to T}^{\text{SPY}}M\_{T}\right). |  |

If Rt→TSPYR\_{t\to T}^{\text{SPY}} captures most of the variation in Mt→TM\_{t\to T}, the physical covariance term will be small. For a log-utility investor, this term is exactly zero since Mt→T∝1/Rt→TSPYM\_{t\to T}\propto 1/R\_{t\to T}^{\text{SPY}}. Under this perspective, the risk-neutral covariance, scaled by the risk-free rate, serves as a good proxy for the unobserved conditional equity premium on the technology index.

This is shown in Panel [8(a)](https://arxiv.org/html/2601.14852v1#A4.F8.sf1 "In Figure 8 ‣ D.3 Conditional covariance and correlation estimates of the technology sector ‣ Appendix D Correlations between sector ETFs and the market portfolio ‣ Beyond Carr–Madan: A Projection Approach to Risk-Neutral Moment Estimation"). Despite the relatively short sample, the figure shows notable dynamics: the equity premium is high—around 10%—early in the sample, but declines steadily from late 2022 onward. We speculate that the rally around October 2022 reflects sharply lower tech valuations following Federal Reserve rate hikes,212121<https://www.nasdaq.com/articles/stock-market-news-for-oct-10-2022> with XLK reaching its lowest post-COVID valuation during the broader tech selloff. In contrast, by July 2023 tech stocks had staged a strong rally, fueled by advances in AI and optimism over easing inflation,222222<https://www.nasdaq.com/articles/stock-market-news-for-jul-14-2023> leading to a lower forward-looking equity premium as investors demanded less compensation to hold technology stocks.

![Refer to caption](x19.png)


(a) Risk-neutral covariance

![Refer to caption](x20.png)


(b) Risk-neutral correlation

![Refer to caption](x21.png)


(c) Risk-neutral covariance (CM)

![Refer to caption](x22.png)


(d) Risk-neutral correlation (CM)

Figure 8: Conditional covariance and correlation of the technology index with the market portfolio (30-day). Risk-neutral covariance and correlation between SPY and XLK (technology index ETF), smoothed using a 15-day backward-looking moving average. The upper panels report estimates based on the projection method; the lower panels use the CM formula. In both cases the covariance estimate is annualized and scaled by the risk-free rate.

## Appendix E Additional tables

| Ticker | Sector tracked |
| --- | --- |
| XLB | Materials |
| XLE | Energy |
| XLF | Financials |
| XLI | Industrials |
| XLK | Information Technology |
| XLP | Consumer Staples |
| XLU | Utilities |
| XLV | Health Care |
| XLY | Consumer Discretionary |
| XLC | Communication Services |
| XLRE | Real Estate |

Table 6: Select Sector SPDR ETFs.