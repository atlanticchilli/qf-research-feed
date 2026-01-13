---
authors:
- Matthew Brigida
doc_id: arxiv:2601.07664v1
family_id: arxiv:2601.07664
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Crypto Pricing with Hidden Factors
url_abs: http://arxiv.org/abs/2601.07664v1
url_html: https://arxiv.org/html/2601.07664v1
venue: arXiv q-fin
version: 1
year: 2026
---


Matt Brigida
Algorand Foundation (matthew.brigida@algorand.foundation) and SUNY Polytechnic Institute

(January 12, 2026)

###### Abstract

We estimate risk premia in the cross-section of cryptocurrency returns using the Giglio–Xiu (2021) three-pass approach, allowing for omitted latent factors alongside observed stock-market and crypto-market factors. Using weekly data on a broad universe of large cryptocurrencies, we find that crypto expected returns load on both crypto-specific factors and selected equity-industry factors associated with technology and profitability, consistent with increased integration between crypto and traditional markets. In addition, we study non-tradable state variables capturing investor sentiment (Fear & Greed), speculative rotation (Altcoin Season Index), and security shocks (hacked value scaled by market capitalization), which are new to the literature. Relative to conventional Fama–MacBeth estimates, the latent-factor approach yields materially different premia for key factors, highlighting the importance of controlling for unobserved risks in crypto asset pricing.

*JEL Classification*: G12

Keywords: Cryptocurrency; Risk Premia; Crypto Factor Pricing

Preliminary draft. Please do not cite without permission.

Recently there has been rapid innovation in cryptocurrency markets, while the market has also increased dramatically in market capitalization. The market evolution is driven by innovation in the underlying technology, new uses for the technology such as decentralized finance, a significantly changing regulatory environment, and increasing interaction with traditional financial institutions. This environment leads to uncertainty about factors which have significant risk premia for cryptocurrencies. Moreover, a key question is how cryptocurrency risk premia compare to traditional assets.

In this analysis we determine factors which affect cryptocurrency returns in the cross-section, and estimate their risk premia. We first focus on commonly employed stock market factors, with their crypto market analogues. [[10](https://arxiv.org/html/2601.07664v1#bib.bib11 "Risks and returns of cryptocurrency")] find evidence that Bitcoin, Ethereum, and Ripple exhibit virtually no exposure to common stock market factors, currency returns, or commodity returns. This suggests cryptocurrency premia are not explained by standard risk factors, but are instead, driven by crypto-specific factors. Further, [[9](https://arxiv.org/html/2601.07664v1#bib.bib4 "Common risk factors in cryptocurrency")] find that cryptocurrency market, size, and momentum factors suffice to explain the cross-section of cryptocurrency returns. We hypothesize, however, the lack of correlation with traditional assets is more pronounced in earlier periods, and have since become more correlated.

In related research, [[2](https://arxiv.org/html/2601.07664v1#bib.bib10 "Crypto risk premia")] estimate risk premia for a set of crypto and stock market factors using the [[8](https://arxiv.org/html/2601.07664v1#bib.bib8 "Asset pricing with omitted factors")] latent factor model. They find evidence that macro risk is priced in cryptocurrencies. Specifically, cryptocurrencies whose returns have a negative correlation with macro risk offer higher expected returns.

[[7](https://arxiv.org/html/2601.07664v1#bib.bib7 "What is the expected return on bitcoin? extracting the term structure of returns from options prices")] and [[1](https://arxiv.org/html/2601.07664v1#bib.bib5 "Risk premia in the bitcoin market")] estimate risk premia in the Bitcoin market. [[7](https://arxiv.org/html/2601.07664v1#bib.bib7 "What is the expected return on bitcoin? extracting the term structure of returns from options prices")] find an option-implied estimate of Bitcoin’s expected return of nearly 80% per annum over the period from 2018 to 2020. This premium is significantly higher than that of equities or gold. [[1](https://arxiv.org/html/2601.07664v1#bib.bib5 "Risk premia in the bitcoin market")] use a pricing kernel approach to estimate an annual Bitcoin risk premium of 66%. This implies investors demand very high compensation for bearing Bitcoin’s volatility and tail risk. Interestingly, they find the shape of the Bitcoin pricing kernel differs from equities, specifically that the contribution of downside risk to the total premium is smaller for Bitcoin than for stocks

In the next section we describe how we constructed our data set of cryptocurrencies, as well as our factor portfolios and non-portfolio factors. Section 2 summarizes our empirical methods and results. Section 3 concludes.

## 1 Data

Our cryptocurrency data set is comprised of weekly returns over a sample period from January 1, 2023 through December 31, 2024. We gather returns for any non-stablecoin cryptocurrency that was in the top 100 cryptocurrencies by market cap at any point in our sample period. This sample construction is designed to ensure our estimates are not affected by a survivorship bias.

Using this method our sample contains 253 unique cryptocurrencies, which comprises over 97% of the total crypto market capitalization. We do not attempt a wider sample because of poor price discovery for extremely low market capitalization cryptocurrencies. Cryptocurrency prices were gathered via the Coinmarketcap Application Programming Interface. Data on the US dollar amount hacked was provided by DeFiLlama111<https://defillama.com/>. Bitcoin implied volatility data is from the CVX website222<https://thecvx.com/api/chart>.

The Altcoin Season Index is from the CoinMarketCap website and measures the relative performance of altcoins relative to Bitcoin. All cryptocurrencies other than Bitcoin are referred to as *altcoins*. The Fear & Greed index is also from CoinMarketCap and is a measure of market sentiment.

Stock factor data was downloaded from Kenneth French’s website333<http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html>. In addition to standard Fama-French factors, we include industry factors because B​a​n​k​sBanks, I​n​s​u​rInsur, and F​i​nFin industries may function as substitutes for crypto investment. Also, the S​o​f​t​wSoftw and C​h​i​p​sChips industry factors function as supply factors, because computing resources are needed to validate transactions on blockchains. Further, many tech investors also invest in crypto, which induces a correlation between the sectors.

### 1.1 Crypto Factor Construction

Below we describe how we construct each crypto factor. Factor construction follows the methods used by [[5](https://arxiv.org/html/2601.07664v1#bib.bib6 "Common risk factors in the returns on stocks and bonds")]. To construct crypto market returns, we compute the weekly value-weighted return on the aggregate crypto market using total market capitalization from CoinMarketCap444<https://coinmarketcap.com/>, and subtract the risk-free rate to obtain excess returns.

To construct the TVL factor we first scale TVL by market cap which affords a proportion of market cap which is locked. Then, for a given week tt, we rank assets by TVL / Market Cap in week t−1t-1. We then create a value-weighted long-short portfolio which buys the top 25% of coins by TVL and sells the bottom 25%. The return on this portfolio over week tt is the factor realization for week tt. This high-minus-low TVL portfolio is denoted as T​V​LTVL in tables below. Given evidence that TVL factor returns are spanned by the crypto market portfolio ([[3](https://arxiv.org/html/2601.07664v1#bib.bib12 "The surprising irrelevance of total-value-locked on cryptocurrency returns")]), we orthogonalize TVL with respect to crypto market returns.

To calculate the momentum factor over week tt we calculate the cumulative return for each cryptocurrency over weeks t−5t-5 to t−1t-1. We then sort the cryptocurrencies and create a long-short portfolio which buys the currencies in the top 25% of cumulative return, and sells the currencies in the bottom 25%. The return on this portfolio over week tt is our crypto momentum factor for week tt. We repeat this procedure for all weeks in our sample.

To construct the SMB factor for week tt we sort all cryptocurrencies by size in week t−1t-1. We then create a long-short portfolio which buys the bottom 25% of coins by size and shorts the top 25%. The return on this portfolio over week tt, less the risk free rate, is the factor realization for week tt.

Hacks is scaled by market cap, and the Fear and Greed and Altseason indices are converted to percent change. The CVX volatility index is maintained in levels. We then convert each non-tradeable factor into its residual component via an AR(1) model.

### 1.2 Descriptive Statistics

Descriptive statistics for our sample are in tables [1](https://arxiv.org/html/2601.07664v1#S1.T1 "Table 1 ‣ 1.2 Descriptive Statistics ‣ 1 Data ‣ Crypto Pricing with Hidden Factors"), [2](https://arxiv.org/html/2601.07664v1#S1.T2 "Table 2 ‣ 1.2 Descriptive Statistics ‣ 1 Data ‣ Crypto Pricing with Hidden Factors"), [3](https://arxiv.org/html/2601.07664v1#S1.T3 "Table 3 ‣ 1.2 Descriptive Statistics ‣ 1 Data ‣ Crypto Pricing with Hidden Factors"), and [4](https://arxiv.org/html/2601.07664v1#S1.T4 "Table 4 ‣ 1.2 Descriptive Statistics ‣ 1 Data ‣ Crypto Pricing with Hidden Factors") below. Crypto excess market returns are on average 1.43% per week over the sample, which is substantially above the stock market’s 0.36% weekly return. Crypto market returns are also substantially right-skewed, and have over 3 times the standard deviation of stock market returns. However, crypto market returns have markedly lower kurtosis than stock market returns (2.05 versus 6.01 respectively).

The crypto small-minus-big long-short portfolio has a very large -10% average weekly return over the sample, with a exceptionally large (in absolute value) minimum weekly return of -206%. The median return is approximately -0.93%, showing the negative skew to crypto SMB returns. The estimated skewness of the crypto SMB portfolio is -4.26. The maximum weekly return was 18.54%. This is evidence of the stronger performance of larger cryptocurrencies, particularly Bitcoin. Lastly, the portfolio exhibits substantial kurtosis.

The crypto momentum portfolio has a lower weekly mean return than the crypto market (at 0.68%), and a slightly higher standard deviation than crypto market returns. The crypto momentum portfolio has a slightly larger median return than the crypto market however.

Table 1: Tradeable Factor Sample Descriptive Statistics: There are 105 weekly observations. Data ranges from Jan. 1, 2023 to Dec. 31 2024. RCR\_{C} is the excess return on the crypto market, and RSR\_{S} is the excess stock market returns. S​M​BSSMB\_{S}, H​M​LSHML\_{S}, and M​o​mSMom\_{S} are weekly Fama-French factors for Small-minus-Big, High-minus-Low, and Momentum respectively. M​o​mCMom\_{C} and S​M​BCSMB\_{C} are long-short crypto momentum and small-minus-big portfolios.

|  | RCR\_{C} | RSR\_{S} | S​M​BSSMB\_{S} | H​M​LSHML\_{S} | M​o​mSMom\_{S} | M​o​mCMom\_{C} | S​M​BCSMB\_{C} | T​V​LTVL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mean | 1.43 | 0.36 | -0.13 | -0.18 | 0.05 | 0.68 | -10.04 | 0.03 |
| std | 6.35 | 1.91 | 1.72 | 1.45 | 1.81 | 7.68 | 33.46 | 5.91 |
| min | -15.42 | -5.75 | -4.03 | -4.43 | -5.33 | -30.14 | -206.53 | -14.25 |
| 25% | -1.89 | -0.64 | -1.11 | -1.11 | -0.92 | -4.54 | -6.41 | -3.36 |
| 50% | 0.24 | 0.45 | -0.27 | -0.37 | 0.17 | 0.55 | -0.93 | -0.48 |
| 75% | 5.72 | 1.50 | 0.77 | 0.63 | 0.98 | 4.33 | 2.18 | 2.37 |
| max | 18.69 | 5.66 | 5.26 | 3.46 | 4.62 | 24.93 | 18.54 | 19.95 |




Table 2: Tradeable Factor Skewness and Kurtosis: There are 105 weekly observations. Data ranges from Jan. 1, 2023 to Dec. 31 2024. Kurtosis is calculated using Fisher’s definition, where the kurtosis of a normal distribution is 0. RCR\_{C} is the excess return on the crypto market, and RSR\_{S} is the excess stock market returns. S​M​BSSMB\_{S}, H​M​LSHML\_{S}, and M​o​mSMom\_{S} are weekly Fama-French factors for Small-minus-Big, High-minus-Low, and Momentum respectively. M​o​mCMom\_{C} and S​M​BCSMB\_{C} are long-short crypto momentum and small-minus-big portfolios.

|  | RCR\_{C} | RSR\_{S} | S​M​BCSMB\_{C} | S​M​BSSMB\_{S} | M​o​mCMom\_{C} | M​o​mSMom\_{S} | H​M​LSHML\_{S} |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Skewness | -0.45 | -0.18 | -4.26 | -0.04 | -0.09 | -1.27 | 0.44 |
| Kurtosis | 2.05 | 6.01 | 21.79 | 1.13 | 2.54 | 8.80 | 3.72 |




Table 3: Tradeable Factor Sample Descriptive Statistics: There are 105 weekly observations. Data ranges from Jan. 1, 2023 to Dec. 31 2024. R​M​WRMW and C​M​WCMW denote the Fama-French corporate profitability and investment strategy factors respectively.

|  | RMW | CMA |
| --- | --- | --- |
| count | 105.00 | 105.00 |
| mean | 0.05 | -0.23 |
| std | 1.08 | 0.94 |
| min | -2.09 | -2.65 |
| 25% | -0.66 | -0.91 |
| 50% | 0.13 | -0.20 |
| 75% | 0.70 | 0.37 |
| max | 2.65 | 2.88 |




Table 4: Non-tradeable factors. There are 105 weekly observations. Data ranges from Jan. 1, 2023 to Dec. 31 2024. H​a​c​k​sHacks is the US Dollar amount of crypto hacked in a given week, divided by the total crypto market cap (also in US Dollars) that week. A​l​t​s​e​a​s​o​nAltseason is the weekly percent change in the CoinmarketCap Altseason index, and F​e​a​r/G​r​e​e​dFear/Greed is the weekly percent change in CoinmarketCap’s Fear and Greed index. C​V​XCVX is a cryptocurrency implied volatility index (<https://www.thecvx.com/>).

|  | Hacks | Altseason | Fear/Greed | C​V​XCVX |
| --- | --- | --- | --- | --- |
| mean | 0.00 | 2.99 | 0.18 | 0.01 |
| std | 0.00 | 23.45 | 1.85 | 0.14 |
| min | 0.00 | -40.98 | -5.28 | -0.30 |
| 25% | 0.00 | -11.33 | -0.92 | -0.10 |
| 50% | 0.00 | 1.37 | 0.18 | -0.00 |
| 75% | 0.00 | 13.11 | 1.14 | 0.10 |
| max | 0.02 | 84.85 | 4.88 | 0.46 |

## 2 Method and Results

Theory on cryptocurrency pricing is still in its infancy, and so there is little guidance on factors which will affect prices. Given the likelihood of unobserved factors when building factor models of cryptocurrencies, we use the [[8](https://arxiv.org/html/2601.07664v1#bib.bib8 "Asset pricing with omitted factors")] latent factor model. This model allows us to estimate risk premia while controlling for unobserved factors.

*Giglio-Xiu*

This latent factor model method extends the classical Fama-MacBeth two-step regression framework by explicitly incorporating unobservable factors into the estimation of risk premia. While the original Fama-MacBeth procedure estimates risk premia for observed factors through cross-sectional regressions, Giglio and Xiu adapt this method by first using dimension reduction (principal component analysis) to identify latent factors from the covariance structure of asset returns.

Let ri,tr\_{i,t} denote the excess return on cryptocurrency i=1,…,Nti=1,\dots,N\_{t} in week t=1,…,Tt=1,\dots,T (note since the panel is unbalanced, NtN\_{t} varies by week).

|  |  |  |  |
| --- | --- | --- | --- |
|  | ri,t=αi+βi⊤​ut+εi,t,r\_{i,t}\;=\;\alpha\_{i}\;+\;\beta\_{i}^{\top}u\_{t}\;+\;\varepsilon\_{i,t}, |  | (1) |

where ut∈ℝKu\_{t}\in\mathbb{R}^{K} are latent common factors and βi\beta\_{i} are asset-specific loadings.

*Pass 1:* We estimate utu\_{t} by principal components on the T×NT\times N panel of excess returns, yielding u^t\widehat{u}\_{t}.
Let gt∈ℝLg\_{t}\in\mathbb{R}^{L} be the vector of LL observed factor realizations.

*Pass 2:* We estimate the mapping from latent factors to observed factors using

|  |  |  |  |
| --- | --- | --- | --- |
|  | gt=a+Λ​u^t+et,g\_{t}\;=\;a\;+\;\Lambda\widehat{u}\_{t}\;+\;e\_{t}, |  | (2) |

which yields Λ^∈ℝL×K\widehat{\Lambda}\in\mathbb{R}^{L\times K}.

*Pass 3:* We estimate the latent factor prices of risk γ∈ℝK\gamma\in\mathbb{R}^{K} from cross-sectional regressions and map them into prices of risk for the observed factors,

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ^g=Λ^​γ^∈ℝL.\widehat{\lambda}\_{g}\;=\;\widehat{\Lambda}\,\widehat{\gamma}\;\in\;\mathbb{R}^{L}. |  | (3) |

Given the short weekly sample and potential time-series dependence, inference is obtained via a block bootstrap over time. Specifically, we resample the time index using overlapping blocks of length *b* weeks drawing blocks with replacement and concatenating them until a bootstrap sample of length *T* is formed. This preserves short-run dependence and volatility clustering at the weekly frequency. For each bootstrap replication we recompute the full three-pass estimator on the resampled data and obtain risk-premia for each observed factor, as well as empirical p-values.

We estimate the model on an unbalanced panel using 7 latent factors chosen via the Bai-Ng Information Criteria. We estimate the latent factors on the unbalanced panel by repeatedly filling in missing weekly returns with values implied by a K-factor structure (while keeping the observed returns unchanged) until the filled-in matrix stabilizes, and then applying standard PCA to that completed return matrix. Bootstrap p-values are computed using the recentered (two-sided) statistic
p=Pr∗⁡(|λ∗−λ^|≥|λ^|)p=\Pr^{\*}\!\left(\left|\lambda^{\*}-\hat{\lambda}\right|\geq\left|\hat{\lambda}\right|\right), using a moving block bootstrap with 1000 repetitions and a block size of 8.

*Fama-Macbeth*

We use a standard [[6](https://arxiv.org/html/2601.07664v1#bib.bib9 "Risk, return, and equilibrium: empirical tests")] estimation procedure, and [[11](https://arxiv.org/html/2601.07664v1#bib.bib1 "On the estimation of beta-pricing models")] adjusted standard errors. For an exposition of the method see [[4](https://arxiv.org/html/2601.07664v1#bib.bib13 "Asset pricing: revised edition")].

### 2.1 Latent Factor Model Results

Results from estimating the [[8](https://arxiv.org/html/2601.07664v1#bib.bib8 "Asset pricing with omitted factors")] model over a 2023-2024 sample period are in table [5](https://arxiv.org/html/2601.07664v1#S2.T5 "Table 5 ‣ 2.1 Latent Factor Model Results ‣ 2 Method and Results ‣ Crypto Pricing with Hidden Factors") below. These results attempt to control for unobserved factors. For comparison and robustness, we also include results from estimating the factor model using the Fama-Macbeth method.

Consistent with all previous models, crypto market returns have a positive and significant risk premium. The estimated risk premia of 0.471% per week which is an annualized risk premium of 24.5%. Over the same period The Fama-Macbeth method estimates a weekly risk premium of 0.164%, for an annualized risk premium of 8.5%. The difference in risk premia between the two methods is substantial, and highlights the importance of including latent factors in crypto pricing models. As an additional reference, [[2](https://arxiv.org/html/2601.07664v1#bib.bib10 "Crypto risk premia")] used the [[8](https://arxiv.org/html/2601.07664v1#bib.bib8 "Asset pricing with omitted factors")] method to estimate risk premia in the crypto market, and their estimate crypto market risk premia was an annualized 26%. So while they used a wider dataset over an earlier sample period including many small cryptocurrencies, we estimate a very similar crypto market risk premium.

Similarly, both the latent factor model and Fama-Macbeth estimate a significantly negative risk premia on the crypto size (SMB) factor (as does [[2](https://arxiv.org/html/2601.07664v1#bib.bib10 "Crypto risk premia")]). The crypto SMB factor has an annualized risk-premium of -70.2%. This is evidence for a preference in crypto markets for larger cryptocurrencies. However, it also may reflect the destruction of capital in small-cap crypto (rug pulls, failed projects). Similar to the results on crypto market returns, however, there is a substantial variation in the risk premia estimates. Note the negative risk premia is opposite of that of the stock market size effect, where the risk premium on S​M​BSMB is typically positive, signifying a market preference for smaller stocks.

The latent model shows significant positive risk premia on the Software stock portfolio. This is consistent with a class of investor which invests across the technology and crypto sectors, though the relationship can also be due to similar reactions to macroeconomic shocks. The Fama-Macbeth results also have a significantly positive risk premia on the Software sector, however it also estimates significantly positive premia on the Finance and Insurance sectors. The latent factor model also estimates positive and significant risk premia for overall stock market returns and stock market profitability factors.

There is also evidence for significant change in expected returns given a shock to the Fear & Greed index. This highlights the time-varying behavioral factors may affect cryptocurrency prices. There is evidence that shocks to the Altseason index may affect expected returns in the Fama-French specification, however it is insignificant in the latent factor model, indicating a correlation with the latent factor. Shocks to the amount hacked are insignificant. Notably, our sample ends prior to the $1.5 billion Bybit hack (which occurred Feb 21, 2025).

Interestingly, the Fama-MacBeth method indicates weak evidence that TVL is priced (10% level), while the [[8](https://arxiv.org/html/2601.07664v1#bib.bib8 "Asset pricing with omitted factors")] latent factor model (after accounting for latent common components and related dependence) finds TVL’s incremental risk price is not distinguishable from zero at conventional levels. The difference is consistent with TVL proxying for broad latent risk in the cross-section. Ultimately, evidence for a distinct TVL price of risk is marginal and not robust to latent-factor controls. Our results complement previous research ([[3](https://arxiv.org/html/2601.07664v1#bib.bib12 "The surprising irrelevance of total-value-locked on cryptocurrency returns")]) which showed TVL is spanned by the market portfolio, by showing TVL loads on latent factors rather than carrying independent risk premia.

Table 5: Giglio and Xiu Latent Factor and Fama-MacBeth Model Results. The weekly sample ranges from 2023-01-02 to 2024-12-31, for a sample of all cryptocurrencies which were in the top 100 cryptocurrencies by market cap over the period. The sample contains 253 cryptocurrencies. RCR\_{C} is the excess return on the crypto market, and RSR\_{S} is the excess stock market returns. S​M​BSSMB\_{S}, H​M​LSHML\_{S}, and M​o​mSMom\_{S} are weekly Fama-French factors for Small-minus-Big, High-minus-Low, and Momentum respectively. M​o​mCMom\_{C} and S​M​BCSMB\_{C} are long-short crypto momentum and small-minus-big portfolios. H​a​c​k​sHacks is the proportion of crypto market cap which was hacked each week. A​l​t​s​e​a​s​o​nAltseason and F​e​a​r​a​n​d​G​r​e​e​dFear\ and\ Greed are Altcoin and Fear & Greed Indices respectively. \*\*\*, \*\*, and \* denote significance at the 1%, 5%, and 10% levels respectively.

|  | Giglio-Xiu Latent | p-value |  | Fama-MacBeth | p-value |
| --- | --- | --- | --- | --- | --- |
| S​M​BCSMB\_{C} | -1.345∗∗∗ | 0.008 |  | -0.083∗∗∗ | 0.000 |
| Softw | 0.071∗ | 0.056 |  | 0.026∗∗∗ | 0.003 |
| F​e​a​r​a​n​d​G​r​e​e​dFear\ and\ Greed | -0.051∗ | 0.058 |  | -0.009∗∗ | 0.026 |
| RCR\_{C} | 0.471∗ | 0.062 |  | 0.112∗∗∗ | 0.000 |
| RSR\_{S} | 0.064∗ | 0.066 |  | 0.005 | 0.157 |
| R​M​WSRMW\_{S} | -0.033∗ | 0.068 |  | -0.006∗ | 0.056 |
| T​V​LTVL | 0.339 | 0.114 |  | 0.025∗ | 0.075 |
| S​M​BSSMB\_{S} | 0.046 | 0.152 |  | 0.005 | 0.247 |
| A​l​t​s​e​a​s​o​nAltseason | 0.475 | 0.240 |  | 0.052∗∗ | 0.036 |
| Fin | 0.033 | 0.366 |  | 0.008∗ | 0.065 |
| Banks | 0.034 | 0.366 |  | 0.011∗ | 0.082 |
| Chips | 0.033 | 0.404 |  | 0.010 | 0.242 |
| Insur | 0.021 | 0.424 |  | 0.015∗∗ | 0.016 |
| M​o​mSMom\_{S} | 0.024 | 0.523 |  | 0.001 | 0.857 |
| H​M​LSHML\_{S} | 0.020 | 0.601 |  | -0.000 | 0.967 |
| C​M​ASCMA\_{S} | -0.011 | 0.667 |  | -0.002 | 0.539 |
| Util | -0.021 | 0.669 |  | 0.001 | 0.908 |
| RlEst | 0.006 | 0.863 |  | 0.005 | 0.505 |
| M​o​mCMom\_{C} | -0.033 | 0.877 |  | 0.001 | 0.959 |
| Gold | -0.007 | 0.879 |  | -0.016 | 0.219 |
| CVX | 0.003 | 0.899 |  | 0.000 | 0.930 |
| H​a​c​k​sHacks | 0.000 | 0.931 |  | 0.000 | 0.397 |

## 3 Conclusion

Across 2023–2024, the evidence supports a view of crypto as increasingly intertwined with traditional equity risks rather than as a fully segmented asset class. In addition to pricing crypto-native exposures (market and size), the latent-factor estimates show that equity-market components are priced in the cross-section of crypto returns: the Software equity industry portfolio carries a positive risk premium, and overall stock market returns and the Robust Minus Weak (R​M​WSRMW\_{S}) stock profitability factor are also priced. This pattern is consistent with a shared investor base and common “risk-on/risk-off” channels linking technology equities and crypto assets.

We also estimate factors risk premia for the amount of crypto hacked, the altseason index, and the crypto fear & greed index. These factors are new to the literature. We find no evidence that hacks are a priced factor, limited evidence that the altseason index is priced, and greater evidence that fear and greed index demonstrates explanatory power for cryptocurrency returns. These latter results underscore the still-developing nature of crypto markets where sentiment and behavioral elements may play a substantial role.

Lastly, we shed light on the impact of crypto factors. The large size effect points to a substantial preference for larger cryptocurrencies. It also possibly reveals the effect of rug pulls and failed projects in lost capital. Our results with respect to TVL complements previous research and finds TVL loads on latent factors rather than being a source of independent risk premia.

Based on our results, there are a number of avenues for future research. First, given we have found evidence that stock factors are important for cryptocurrency markets, it is likely that factor relationships, and estimates of these relationships, may continue to shift over time. Moreover, given the relatively short history of cryptocurrency markets, factor estimates may change with additional data. Thus, future research testing for regime switching may be fruitful. Secondly, exploring the transmission mechanisms between traditional financial markets and cryptocurrencies would provide valuable insights into the economic foundations of the observed risk premia, and would assist in risk management. Lastly, liquidity considerations and market microstructure effects, particularly related to the construction of the sample of cryptocurrency returns, may affect risk premia estimates.

## References

* [1]
  C. Almeida, M. Grith, R. Miftachov, and Z. Wang (2024)
  Risk premia in the bitcoin market.
  arXiv preprint arXiv:2410.15195.
  Cited by: [Crypto Pricing with Hidden Factors](https://arxiv.org/html/2601.07664v1#p7.1 "Crypto Pricing with Hidden Factors").
* [2]
  N. Borri, D. Massacci, M. Rubin, and D. Ruzzi (2022)
  Crypto risk premia.
  SSRN Electronic Journal.
  External Links: ISSN 1556-5068,
  [Document](https://dx.doi.org/10.2139/ssrn.4154627),
  [Link](http://dx.doi.org/10.2139/ssrn.4154627)
  Cited by: [§2.1](https://arxiv.org/html/2601.07664v1#S2.SS1.p2.1 "2.1 Latent Factor Model Results ‣ 2 Method and Results ‣ Crypto Pricing with Hidden Factors"),
  [§2.1](https://arxiv.org/html/2601.07664v1#S2.SS1.p3.1 "2.1 Latent Factor Model Results ‣ 2 Method and Results ‣ Crypto Pricing with Hidden Factors"),
  [Crypto Pricing with Hidden Factors](https://arxiv.org/html/2601.07664v1#p6.1 "Crypto Pricing with Hidden Factors").
* [3]
  M. Brigida (2025)
  The surprising irrelevance of total-value-locked on cryptocurrency returns.
  Economics Letters 257,  pp. 112673.
  External Links: ISSN 0165-1765,
  [Document](https://dx.doi.org/https%3A//doi.org/10.1016/j.econlet.2025.112673),
  [Link](https://www.sciencedirect.com/science/article/pii/S0165176525005105)
  Cited by: [§1.1](https://arxiv.org/html/2601.07664v1#S1.SS1.p2.5 "1.1 Crypto Factor Construction ‣ 1 Data ‣ Crypto Pricing with Hidden Factors"),
  [§2.1](https://arxiv.org/html/2601.07664v1#S2.SS1.p6.1 "2.1 Latent Factor Model Results ‣ 2 Method and Results ‣ Crypto Pricing with Hidden Factors").
* [4]
  J. H. Cochrane (2005)
  Asset pricing: revised edition.
   Princeton University Press, Princeton, NJ.
  External Links: ISBN 978-0691121376
  Cited by: [§2](https://arxiv.org/html/2601.07664v1#S2.p11.1 "2 Method and Results ‣ Crypto Pricing with Hidden Factors").
* [5]
  E. F. Fama and K. R. French (1993)
  Common risk factors in the returns on stocks and bonds.
  Journal of financial economics 33 (1),  pp. 3–56.
  Cited by: [§1.1](https://arxiv.org/html/2601.07664v1#S1.SS1.p1.1 "1.1 Crypto Factor Construction ‣ 1 Data ‣ Crypto Pricing with Hidden Factors").
* [6]
  E. F. Fama and J. D. MacBeth (1973-05)
  Risk, return, and equilibrium: empirical tests.
  Journal of Political Economy 81 (3),  pp. 607–636.
  External Links: ISSN 1537-534X,
  [Document](https://dx.doi.org/10.1086/260061),
  [Link](http://dx.doi.org/10.1086/260061)
  Cited by: [§2](https://arxiv.org/html/2601.07664v1#S2.p11.1 "2 Method and Results ‣ Crypto Pricing with Hidden Factors").
* [7]
  S. Foley, S. Li, H. Malloch, and J. Svec (2022)
  What is the expected return on bitcoin? extracting the term structure of returns from options prices.
  Economics Letters 210,  pp. 110196.
  Cited by: [Crypto Pricing with Hidden Factors](https://arxiv.org/html/2601.07664v1#p7.1 "Crypto Pricing with Hidden Factors").
* [8]
  S. Giglio and D. Xiu (2021-07)
  Asset pricing with omitted factors.
  Journal of Political Economy 129 (7),  pp. 1947–1990.
  External Links: ISSN 1537-534X,
  [Document](https://dx.doi.org/10.1086/714090),
  [Link](http://dx.doi.org/10.1086/714090)
  Cited by: [§2.1](https://arxiv.org/html/2601.07664v1#S2.SS1.p1.1 "2.1 Latent Factor Model Results ‣ 2 Method and Results ‣ Crypto Pricing with Hidden Factors"),
  [§2.1](https://arxiv.org/html/2601.07664v1#S2.SS1.p2.1 "2.1 Latent Factor Model Results ‣ 2 Method and Results ‣ Crypto Pricing with Hidden Factors"),
  [§2.1](https://arxiv.org/html/2601.07664v1#S2.SS1.p6.1 "2.1 Latent Factor Model Results ‣ 2 Method and Results ‣ Crypto Pricing with Hidden Factors"),
  [§2](https://arxiv.org/html/2601.07664v1#S2.p1.1 "2 Method and Results ‣ Crypto Pricing with Hidden Factors"),
  [Crypto Pricing with Hidden Factors](https://arxiv.org/html/2601.07664v1#p6.1 "Crypto Pricing with Hidden Factors").
* [9]
  Y. Liu, A. Tsyvinski, and X. Wu (2022)
  Common risk factors in cryptocurrency.
  The Journal of Finance 77 (2),  pp. 1133–1177.
  Cited by: [Crypto Pricing with Hidden Factors](https://arxiv.org/html/2601.07664v1#p5.1 "Crypto Pricing with Hidden Factors").
* [10]
  Y. Liu and A. Tsyvinski (2020-09)
  Risks and returns of cryptocurrency.
  The Review of Financial Studies 34 (6),  pp. 2689–2727.
  External Links: ISSN 1465-7368,
  [Document](https://dx.doi.org/10.1093/rfs/hhaa113),
  [Link](http://dx.doi.org/10.1093/rfs/hhaa113)
  Cited by: [Crypto Pricing with Hidden Factors](https://arxiv.org/html/2601.07664v1#p5.1 "Crypto Pricing with Hidden Factors").
* [11]
  J. Shanken (1992-01)
  On the estimation of beta-pricing models.
  Review of Financial Studies 5 (1),  pp. 1–33.
  External Links: ISSN 1465-7368,
  [Document](https://dx.doi.org/10.1093/rfs/5.1.1),
  [Link](http://dx.doi.org/10.1093/rfs/5.1.1)
  Cited by: [§2](https://arxiv.org/html/2601.07664v1#S2.p11.1 "2 Method and Results ‣ Crypto Pricing with Hidden Factors").