---
authors:
- Sungwoo Kang
doc_id: arxiv:2601.05716v1
family_id: arxiv:2601.05716
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'When the Rules Change: Adaptive Signal Extraction via Kalman Filtering and
  Markov-Switching Regimes'
url_abs: http://arxiv.org/abs/2601.05716v1
url_html: https://arxiv.org/html/2601.05716v1
venue: arXiv q-fin
version: 1
year: 2026
---


Sungwoo Kang
  
Department of Electrical and Computer Engineering, Korea University, Seoul 02841, Republic of Korea
  
krml919@korea.ac.kr

(January 9, 2026)

###### Abstract

Static linear models of order flow assume constant parameters, failing precisely when they are needed most: during periods of market stress and structural change. This paper proposes a dynamic, state-dependent framework for order flow signal extraction that adapts to shifting market conditions in the Korean stock market. Using daily transaction data from 2020–2024 covering 2,439 stocks and 2.79 million stock-day observations, we implement three complementary methodologies: (1) an Adaptive Kalman Filter where measurement noise variance is explicitly coupled to market volatility; (2) a three-state Markov-Switching model identifying Bull, Normal, and Crisis regimes; and (3) an Asymmetric Response Function capturing differential investor reactions to positive versus negative shocks. We find that foreign investor predictive power increases 8.9-fold during crisis periods relative to bull markets (βc​r​i​s​i​s=0.00204\beta\_{crisis}=0.00204 vs. βb​u​l​l=0.00023\beta\_{bull}=0.00023), while individual investors exhibit momentum-chasing behavior with 6.3 times stronger response to positive shocks. The integrated “All-Weather” strategy provides modest drawdown reduction during extreme market events, though challenges remain in the post-COVID high-rate environment.

Keywords: Order Flow, Kalman Filter, Regime Switching, Investor Heterogeneity, Market Microstructure

JEL Classification: G12, G14, G15, C32

## 1 Introduction

The relationship between order flow and returns is among the most studied phenomena in market microstructure (Kyle,, [1985](https://arxiv.org/html/2601.05716v1#bib.bib15); Glosten and Milgrom,, [1985](https://arxiv.org/html/2601.05716v1#bib.bib6)). A fundamental premise of this literature is that informed traders reveal private information through their trading activity, generating a contemporaneous and predictive relationship between net buying pressure and subsequent price movements. However, an implicit assumption underlies much of this research: that the parameters governing this relationship remain stable across market conditions.

This assumption is empirically untenable. During the COVID-19 crash of March 2020, volatility indices rose to levels not seen since the 2008 financial crisis, correlations across asset classes converged toward unity, and liquidity evaporated precisely when it was needed most. Static regression coefficients estimated during tranquil periods provide dangerous guidance during such episodes. A model that worked “on average” becomes a liability when the VIX exceeds 40.

This paper addresses this limitation by developing a dynamic, state-dependent framework for order flow analysis that explicitly adapts to changing market conditions. Our approach rests on three methodological pillars:

First, we implement an Adaptive Kalman Filter that treats the “true informed signal” as a hidden state obscured by noise trading. Unlike standard implementations, we make measurement noise variance heteroskedastic, explicitly coupling it to realized market volatility. When volatility spikes, the Kalman gain automatically decreases, causing the model to discount high-volume panic trading as noise rather than signal.

Second, we employ a Three-State Markov-Switching Model to identify discrete market regimes—Bull, Normal, and Crisis—each with distinct return dynamics and order flow relationships. This allows parameters to “snap” to new equilibria rather than merely drift, capturing the qualitative changes in market behavior during stress periods.

Third, we estimate Asymmetric Response Functions that capture how different investor types react to positive versus negative shocks. This reveals behavioral heterogeneity that static models obscure: foreign investors act as contrarian liquidity providers during crashes, while retail investors engage in momentum-chasing behavior that amplifies market movements.

Using daily transaction data from the Korean stock market spanning 2020–2024, we document several key findings. Foreign investor order flow exhibits dramatically higher predictive power during crisis regimes (β=0.00204\beta=0.00204, t=19.23t=19.23) compared to bull markets (β=0.00023\beta=0.00023, t=7.81t=7.81)—an 8.9-fold increase. Individual investors display asymmetric responses to market shocks, with response coefficients to positive shocks (β+=0.000089\beta^{+}=0.000089) far exceeding those to negative shocks (β−=0.000014\beta^{-}=0.000014), consistent with momentum-chasing behavior. The integrated strategy incorporating all three methodologies provides modest improvement in maximum drawdown during crisis periods, though overall sample performance remains challenging in the post-COVID environment.

Our contribution is methodological and empirical. Methodologically, we demonstrate how state-space models can be adapted to financial applications where parameter stability cannot be assumed. Empirically, we document systematic patterns in how different investor classes respond to market conditions, with implications for understanding price discovery and market stability.

The remainder of this paper is organized as follows. Section 2 reviews related literature. Section 3 presents our methodological framework. Section 4 describes the data. Section 5 presents empirical results. Section 6 discusses robustness checks. Section 7 concludes.

## 2 Literature Review

### 2.1 Order Flow and Price Discovery

The theoretical foundation for order flow analysis rests on models of asymmetric information (Kyle,, [1985](https://arxiv.org/html/2601.05716v1#bib.bib15); Glosten and Milgrom,, [1985](https://arxiv.org/html/2601.05716v1#bib.bib6); Easley and O’Hara,, [1987](https://arxiv.org/html/2601.05716v1#bib.bib5)). In Kyle’s framework, informed traders strategically split orders to minimize price impact while uninformed noise traders provide liquidity. The market maker observes aggregate order flow and updates prices to reflect the expected information content, generating a positive relationship between order imbalance and returns.

Empirical work has extensively documented this relationship across markets and frequencies (Hasbrouck,, [1991](https://arxiv.org/html/2601.05716v1#bib.bib11); Chordia et al.,, [2002](https://arxiv.org/html/2601.05716v1#bib.bib4); Lee and Ready,, [1991](https://arxiv.org/html/2601.05716v1#bib.bib16)). Studies of investor heterogeneity find that different trader types exhibit distinct information content (Barber and Odean,, [2008](https://arxiv.org/html/2601.05716v1#bib.bib2); Griffin et al.,, [2003](https://arxiv.org/html/2601.05716v1#bib.bib7); Kaniel et al.,, [2008](https://arxiv.org/html/2601.05716v1#bib.bib14)), with institutional investors generally exhibiting superior performance relative to retail traders.

### 2.2 Regime-Switching in Financial Markets

Regime-switching models have a long history in financial econometrics, originating with Hamilton, ([1989](https://arxiv.org/html/2601.05716v1#bib.bib10)) analysis of business cycle dynamics. Applications to asset returns include Ang and Bekaert, ([2002](https://arxiv.org/html/2601.05716v1#bib.bib1)) study of international equity correlations and Guidolin and Timmermann, ([2006](https://arxiv.org/html/2601.05716v1#bib.bib9)) analysis of portfolio allocation under regime uncertainty.

In market microstructure, Hasbrouck and Seppi, ([2001](https://arxiv.org/html/2601.05716v1#bib.bib12)) documents how liquidity conditions vary across market states, while Chordia et al., ([2001](https://arxiv.org/html/2601.05716v1#bib.bib3)) show that liquidity dries up precisely during stress periods when it is most needed. Our contribution extends this literature by explicitly modeling how order flow–return relationships shift across regimes.

### 2.3 Behavioral Asymmetries

Behavioral finance documents systematic asymmetries in investor reactions to gains versus losses (Kahneman and Tversky,, [1979](https://arxiv.org/html/2601.05716v1#bib.bib13); Shefrin and Statman,, [1985](https://arxiv.org/html/2601.05716v1#bib.bib18)). The disposition effect—holding losers too long while selling winners too quickly—has been documented across markets and investor types (Odean,, [1998](https://arxiv.org/html/2601.05716v1#bib.bib17); Grinblatt and Keloharju,, [2001](https://arxiv.org/html/2601.05716v1#bib.bib8)).

Our asymmetric response framework connects to this literature by documenting differential reactions to positive and negative market shocks at the daily frequency, revealing that retail investors exhibit momentum-chasing behavior while foreign investors provide contrarian liquidity.

## 3 Methodology

### 3.1 Adaptive Kalman Filter

We model the relationship between observed order flow and the “true” informed signal using a state-space representation. Let StS\_{t} denote the observed market-cap normalized order flow at time tt and θt\theta\_{t} the latent informed signal. The state equation describes the evolution of the informed signal:

|  |  |  |  |
| --- | --- | --- | --- |
|  | θt=ϕ​θt−1+ηt,ηt∼N​(0,Qt)\theta\_{t}=\phi\theta\_{t-1}+\eta\_{t},\quad\eta\_{t}\sim N(0,Q\_{t}) |  | (1) |

where ϕ\phi is the persistence parameter and QtQ\_{t} is the state noise variance.

The measurement equation links observed flow to the latent signal:

|  |  |  |  |
| --- | --- | --- | --- |
|  | St=θt+ϵt,ϵt∼N​(0,Rt)S\_{t}=\theta\_{t}+\epsilon\_{t},\quad\epsilon\_{t}\sim N(0,R\_{t}) |  | (2) |

Our key innovation is making the measurement noise variance RtR\_{t} heteroskedastic and explicitly coupled to market conditions:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt=R0⋅(σtσ¯)γR\_{t}=R\_{0}\cdot\left(\frac{\sigma\_{t}}{\bar{\sigma}}\right)^{\gamma} |  | (3) |

where σt\sigma\_{t} is realized volatility, σ¯\bar{\sigma} is average volatility, and γ>0\gamma>0 is a sensitivity parameter.

This specification implies that during high-volatility periods, measurement noise increases, reducing the Kalman gain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Kt=Pt|t−1Pt|t−1+RtK\_{t}=\frac{P\_{t|t-1}}{P\_{t|t-1}+R\_{t}} |  | (4) |

where Pt|t−1P\_{t|t-1} is the predicted state variance. When RtR\_{t} rises during stress periods, KtK\_{t} falls, causing the filtered estimate to discount recent observations more heavily.

### 3.2 Markov-Switching Regime Model

We specify a three-state Markov-switching model for market returns:

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt=μst+σst​ϵt,st∈{1,2,3}r\_{t}=\mu\_{s\_{t}}+\sigma\_{s\_{t}}\epsilon\_{t},\quad s\_{t}\in\{1,2,3\} |  | (5) |

where sts\_{t} follows a first-order Markov chain with transition matrix 𝐏\mathbf{P}. The three regimes correspond to:

* •

  Regime 1 (Bull): High mean return, low volatility
* •

  Regime 2 (Normal): Near-zero mean, moderate volatility
* •

  Regime 3 (Crisis): Negative mean, high volatility

We estimate regime-conditional predictive regressions:

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt+1=αst+βst​Stf​i​l​t​e​r​e​d+εt+1r\_{t+1}=\alpha\_{s\_{t}}+\beta\_{s\_{t}}S\_{t}^{filtered}+\varepsilon\_{t+1} |  | (6) |

allowing the order flow–return relationship to vary across market states.

### 3.3 Asymmetric Response Function

To capture differential investor reactions to positive versus negative shocks, we estimate:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​St(i)=α(i)+β(i)+⋅𝟏​[rt−1>k​σ]⋅|rt−1|+β(i)−⋅𝟏​[rt−1<−k​σ]⋅|rt−1|+ϵt\Delta S\_{t}^{(i)}=\alpha^{(i)}+\beta^{(i)+}\cdot\mathbf{1}[r\_{t-1}>k\sigma]\cdot|r\_{t-1}|+\beta^{(i)-}\cdot\mathbf{1}[r\_{t-1}<-k\sigma]\cdot|r\_{t-1}|+\epsilon\_{t} |  | (7) |

where ii indexes investor type, kk is the shock threshold (set to 2 standard deviations), and 𝟏​[⋅]\mathbf{1}[\cdot] is the indicator function.

The asymmetry ratio β−/β+\beta^{-}/\beta^{+} captures whether investors respond more strongly to negative shocks (ratio >1>1) or positive shocks (ratio <1<1).

### 3.4 Integrated Strategy

We combine the three components into an “All-Weather” strategy:

1. 1.

   Apply Kalman filtering to smooth the order flow signal
2. 2.

   Condition position sizing on regime probabilities, reducing exposure during crisis states
3. 3.

   Apply asymmetric stop-loss rules based on shock response patterns

## 4 Data

### 4.1 Sample Description

Our sample consists of daily trading data from the Korea Exchange (KRX) spanning January 2020 through December 2024. The data includes transaction records disaggregated by investor type: foreign institutional, domestic institutional, and individual investors.

We focus on common stocks in the KOSPI and KOSDAQ markets, excluding ETFs, REITs, and other derivatives. After applying standard filters for data quality and requiring minimum trading activity, our final sample comprises 2,439 unique stocks and 2,788,940 stock-day observations.

### 4.2 Variable Construction

Following the literature on informed trading (Chordia et al.,, [2002](https://arxiv.org/html/2601.05716v1#bib.bib4)), we construct market-cap normalized order flow as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | StM​C,(i)=B​u​yt(i)−S​e​l​lt(i)M​C​A​Pt−1S\_{t}^{MC,(i)}=\frac{Buy\_{t}^{(i)}-Sell\_{t}^{(i)}}{MCAP\_{t-1}} |  | (8) |

where B​u​yt(i)Buy\_{t}^{(i)} and S​e​l​lt(i)Sell\_{t}^{(i)} denote buy and sell volume in Korean Won for investor type ii, and M​C​A​Pt−1MCAP\_{t-1} is lagged market capitalization.

This normalization ensures that order flow is comparable across stocks of different sizes and has the interpretation of the fraction of market cap being net acquired by investor type ii.

### 4.3 Summary Statistics

Table [1](https://arxiv.org/html/2601.05716v1#S4.T1 "Table 1 ‣ 4.3 Summary Statistics ‣ 4 Data ‣ When the Rules Change: Adaptive Signal Extraction via Kalman Filtering and Markov-Switching Regimes") presents summary statistics for our main variables. The average market-cap normalized foreign flow is slightly negative (−0.0023%-0.0023\%), indicating net selling over the sample period. Individual investor flow is positive on average (+0.0084%+0.0084\%), consistent with these investors being net buyers during the period. Daily returns average 0.03%0.03\% with substantial cross-sectional and time-series variation (standard deviation 3.5%3.5\%).

Table 1: Data Summary Statistics

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Variable | Mean | Std | Min | Max |
| Observations | 2,788,940 |  |  |  |
| Unique stocks | 2,439 |  |  |  |
| Unique dates | 1,231 |  |  |  |
| Sf​o​rM​CS^{MC}\_{for} | -0.000023 | 0.001661 | -0.009012 | 0.007834 |
| Si​n​sM​CS^{MC}\_{ins} | -0.000036 | 0.000849 | -0.005496 | 0.004473 |
| Si​n​dM​CS^{MC}\_{ind} | 0.000084 | 0.001838 | -0.008763 | 0.011589 |
| RtR\_{t} | 0.030% | 3.506% | -38.18% | 300.77% |
| Vol ratio | 0.869 | 0.524 | 0.000 | 3.841 |

## 5 Empirical Results

### 5.1 Kalman Filter Performance

Table [2](https://arxiv.org/html/2601.05716v1#S5.T2 "Table 2 ‣ 5.1 Kalman Filter Performance ‣ 5 Empirical Results ‣ When the Rules Change: Adaptive Signal Extraction via Kalman Filtering and Markov-Switching Regimes") reports the predictive performance of raw versus Kalman-filtered order flow signals. We estimate panel regressions of future returns on current order flow:

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt+h=α+β​St+εt+hr\_{t+h}=\alpha+\beta S\_{t}+\varepsilon\_{t+h} |  | (9) |

for horizons h∈{1,5,20}h\in\{1,5,20\} days.

The Kalman filter provides consistent, albeit modest, improvements in predictive tt-statistics and R2R^{2} values. For foreign investors, the improvement in tt-statistics ranges from 0.18%0.18\% at the 1-day horizon to 0.21%0.21\% at the 20-day horizon. The improvement increases with forecast horizon, suggesting the filter is more effective at extracting persistent information content.

Table 2: Kalman Filter Predictive Improvement

| Investor | Horizon | tr​a​wt\_{raw} | tf​i​l​t​e​r​e​dt\_{filtered} | Rr​a​w2R^{2}\_{raw} | Rf​i​l​t​e​r​e​d2R^{2}\_{filtered} | Improvement |
| --- | --- | --- | --- | --- | --- | --- |
| Foreign | Rt+1R\_{t+1} | 29.15 | 29.21 | 0.030% | 0.031% | 0.2% |
|  | Rt+5R\_{t+5} | 13.22 | 13.24 | 0.006% | 0.006% | 0.2% |
|  | Rt+20R\_{t+20} | 9.14 | 9.16 | 0.003% | 0.003% | 0.2% |
| Institutional | Rt+1R\_{t+1} | 20.22 | 20.21 | 0.015% | 0.015% | -0.0% |
|  | Rt+5R\_{t+5} | 1.62 | 1.61 | 0.000% | 0.000% | -0.1% |
|  | Rt+20R\_{t+20} | -6.14 | -6.14 | 0.001% | 0.001% | 0.0% |
| Individual | Rt+1R\_{t+1} | -25.82 | -25.85 | 0.024% | 0.024% | 0.1% |
|  | Rt+5R\_{t+5} | -11.60 | -11.62 | 0.005% | 0.005% | 0.2% |
|  | Rt+20R\_{t+20} | -7.00 | -7.02 | 0.002% | 0.002% | 0.2% |

Figure [1](https://arxiv.org/html/2601.05716v1#S5.F1 "Figure 1 ‣ 5.1 Kalman Filter Performance ‣ 5 Empirical Results ‣ When the Rules Change: Adaptive Signal Extraction via Kalman Filtering and Markov-Switching Regimes") illustrates the relationship between Kalman gain and market volatility. The gain remains high (above 0.99) across all volatility conditions, indicating that the raw signals already contain substantial information content. However, the gain does decline slightly during high-volatility periods, consistent with the intended noise-reduction mechanism.

![Refer to caption](x1.png)


Figure 1: Kalman Gain versus Market Volatility

### 5.2 Regime Identification

Table [3](https://arxiv.org/html/2601.05716v1#S5.T3 "Table 3 ‣ 5.2 Regime Identification ‣ 5 Empirical Results ‣ When the Rules Change: Adaptive Signal Extraction via Kalman Filtering and Markov-Switching Regimes") presents the characteristics of the three identified market regimes. The Bull regime (528 days, 43% of sample) features high daily returns (+0.154%+0.154\%), low volatility (0.54%), and exceptional risk-adjusted performance (Sharpe ratio 4.50). The Normal regime (598 days, 49%) exhibits near-zero returns (−0.034%-0.034\%) with moderate volatility (1.24%). The Crisis regime (95 days, 8%) shows strongly negative returns (−0.223%-0.223\%) and high volatility (3.87%).

Table 3: Markov-Switching Regime Characteristics

| Regime | Days | Mean Return | Volatility | Sharpe | Foreign Flow |
| --- | --- | --- | --- | --- | --- |
| Bull | 528 | 0.154% | 0.54% | 4.50 | -0.0027% |
| Normal | 598 | -0.034% | 1.24% | -0.44 | -0.0040% |
| Crisis | 95 | -0.223% | 3.87% | -0.92 | 0.0100% |

The critical finding is the regime-conditional variation in foreign investor predictive power. During Bull periods, the foreign flow coefficient is β=0.00023\beta=0.00023 (t=7.81t=7.81). This increases to β=0.00064\beta=0.00064 (t=21.15t=21.15) in Normal regimes and rises dramatically to β=0.00204\beta=0.00204 (t=19.23t=19.23) during Crisis periods—an 8.9-fold increase relative to Bull markets.

This pattern suggests that foreign investors possess (or reveal) superior information precisely when markets are most stressed. One interpretation is that during crises, noise trading by retail investors increases, making the relative information advantage of foreign institutions more pronounced.

![Refer to caption](x2.png)


Figure 2: Time Series of Regime Probabilities

Figure [2](https://arxiv.org/html/2601.05716v1#S5.F2 "Figure 2 ‣ 5.2 Regime Identification ‣ 5 Empirical Results ‣ When the Rules Change: Adaptive Signal Extraction via Kalman Filtering and Markov-Switching Regimes") displays the time series of regime probabilities. The COVID-19 crash of March 2020 is clearly identified as a Crisis period, as are several subsequent stress episodes. The model identifies 130 crisis days (10.6% of the sample) with probability exceeding the 30% threshold.

### 5.3 Asymmetric Response Functions

Table [4](https://arxiv.org/html/2601.05716v1#S5.T4 "Table 4 ‣ 5.3 Asymmetric Response Functions ‣ 5 Empirical Results ‣ When the Rules Change: Adaptive Signal Extraction via Kalman Filtering and Markov-Switching Regimes") reports the asymmetric response coefficients by investor type. All three investor groups exhibit statistically significant asymmetric responses to market shocks (Wald test p<0.001p<0.001 in all cases).

Table 4: Asymmetric Response Coefficients

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Investor Type | β+\beta^{+} | t​(β+)t(\beta^{+}) | β−\beta^{-} | t​(β−)t(\beta^{-}) | Ratio | p-value |
| Foreign | -0.000035\*\*\* | (-12.02) | 0.000070\*\*\* | (22.60) | -2.02 | 0.0000 |
| Institutional | -0.000021\*\*\* | (-10.57) | -0.000045\*\*\* | (-20.24) | 2.21 | 0.0000 |
| Individual | 0.000089\*\*\* | (22.61) | 0.000014\*\*\* | (3.36) | 0.16 | 0.0000 |
| ∗∗∗p<0.01, ∗∗p<0.05, ∗p<0.10 | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |

Foreign investors display contrarian behavior: they sell after positive shocks (β+=−0.000035\beta^{+}=-0.000035) and buy after negative shocks (β−=+0.000070\beta^{-}=+0.000070). The asymmetry ratio of −2.02-2.02 indicates buying intensity after crashes is approximately twice the selling intensity after rallies.

Individual investors exhibit the opposite pattern: strong buying after positive shocks (β+=+0.000089\beta^{+}=+0.000089) and weak selling after negative shocks (β−=+0.000014\beta^{-}=+0.000014). The asymmetry ratio of 0.160.16 reveals momentum-chasing behavior—retail investors “chase” rallies while being reluctant to sell during declines.

![Refer to caption](x3.png)


Figure 3: Asymmetric Response Patterns by Investor Type

### 5.4 Integrated Strategy Performance

Table [5](https://arxiv.org/html/2601.05716v1#S5.T5 "Table 5 ‣ 5.4 Integrated Strategy Performance ‣ 5 Empirical Results ‣ When the Rules Change: Adaptive Signal Extraction via Kalman Filtering and Markov-Switching Regimes") compares the performance of three portfolio construction approaches: (1) Static Raw using unfiltered order flow, (2) Kalman Filtered using smoothed signals, and (3) All-Weather incorporating regime-based position sizing.

Table 5: Portfolio Performance Comparison

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Investor | Strategy | Return | Sharpe | Calmar | Max DD |
| Foreign | Static Raw | -10.47% | -0.477 | -0.154 | -68.2% |
|  | Kalman Filtered | -10.36% | -0.472 | -0.152 | -68.3% |
|  | All Weather | -10.08% | -0.500 | -0.151 | -66.8% |
| Institutional | Static Raw | 58.75% | 2.240 | 17.760 | -3.3% |
|  | Kalman Filtered | 17.32% | 1.033 | 0.542 | -31.9% |
|  | All Weather | 14.74% | 0.940 | 0.454 | -32.5% |
| Individual | Kalman Filtered | -44.11% | -2.155 | -0.488 | -90.4% |
|  | All Weather | -45.32% | -2.396 | -0.500 | -90.6% |

For foreign investor-based strategies, the All-Weather approach provides modest improvement in maximum drawdown (−66.8%-66.8\% vs. −68.2%-68.2\%), though overall returns remain negative in this challenging sample period. The most notable finding is the strong performance during the COVID crisis period specifically: as shown in the robustness analysis, the 2020 subsample achieves a Sharpe ratio of 1.08 and Calmar ratio of 0.92.

![Refer to caption](x4.png)


Figure 4: Cumulative Returns: Raw vs. Filtered vs. All-Weather

Figure [4](https://arxiv.org/html/2601.05716v1#S5.F4 "Figure 4 ‣ 5.4 Integrated Strategy Performance ‣ 5 Empirical Results ‣ When the Rules Change: Adaptive Signal Extraction via Kalman Filtering and Markov-Switching Regimes") displays cumulative returns for the three strategies. The All-Weather strategy outperforms during the March 2020 crash, consistent with the regime-detection mechanism reducing exposure during crisis periods. However, this advantage is partially offset by underperformance during the 2021–2023 period.

## 6 Robustness

Table [6](https://arxiv.org/html/2601.05716v1#S6.T6 "Table 6 ‣ 6 Robustness ‣ When the Rules Change: Adaptive Signal Extraction via Kalman Filtering and Markov-Switching Regimes") presents a comprehensive set of robustness checks.

Table 6: Robustness Checks

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Category | Specification | Sharpe | Calmar | N |
| Panel A: Subperiod Analysis | | | | |
| Subperiod | 2020 (COVID Crisis) | 1.081 | 0.924 | 248 |
| Subperiod | 2021 (Recovery) | -0.982 | -0.529 | 248 |
| Subperiod | 2022 (Rate Hikes) | -2.056 | -0.948 | 246 |
| Subperiod | 2023 (Calm) | -1.315 | -1.040 | 245 |
| Subperiod | 2024 (Recent) | 0.652 | 0.604 | 243 |
| Panel B: Size Quintile Analysis | | | | |
| Size | Q1 | 2.753 | 2.103 | 1207 |
| Size | Q2 | 0.135 | 0.049 | 1230 |
| Size | Q3 | 0.378 | 0.204 | 1230 |
| Size | Q4 | -0.076 | -0.028 | 1230 |
| Size | Q5 | -0.221 | -0.087 | 1230 |
| Panel C: Bootstrap Confidence Intervals (95%) | | | | |
| Bootstrap | Sharpe 95% CI | [-1.445, 0.559] |  |  |
| Bootstrap | Calmar 95% CI |  | [-0.377, 0.375] |  |

Subperiod Analysis: Performance varies substantially across calendar years. The strategy performs well during high-volatility periods (2020: Sharpe 1.08; 2024: Sharpe 0.65) but poorly during the low-volatility, low-return period of 2021–2023 characterized by global rate hikes.

Size Quintile Analysis: A pronounced small-cap effect emerges, with the smallest quintile (Q1) achieving a Sharpe ratio of 2.75 versus −0.22-0.22 for the largest quintile (Q5). This suggests that order flow signals contain more exploitable information in smaller, less liquid stocks.

Bootstrap Confidence Intervals: Bootstrap analysis (1,000 iterations) yields 95% confidence intervals of [−1.45,+0.56][-1.45,+0.56] for Sharpe ratio and [−0.38,+0.38][-0.38,+0.38] for Calmar ratio. The inclusion of zero in both intervals indicates that while the methodology provides valuable insights into market dynamics, claims of robust alpha generation require caution.

Parameter Sensitivity: Kalman filter parameters (ϕ\phi, QQ, λ\lambda) exhibit reasonable stability across specification choices, with Kalman gain varying by less than 0.1% across the tested parameter ranges.

## 7 Discussion and Conclusion

### 7.1 Summary of Findings

This paper develops a dynamic, state-dependent framework for analyzing order flow–return relationships in the Korean stock market. Our three-pillar approach—Adaptive Kalman Filtering, Markov-Switching Regimes, and Asymmetric Response Functions—reveals systematic patterns that static models obscure.

The central finding is that foreign investor predictive power increases dramatically during crisis periods. The regime-conditional coefficient rises from 0.00023 in Bull markets to 0.00204 in Crisis periods, an 8.9-fold increase. This suggests that either (a) foreign investors possess superior information that becomes more valuable during stress, or (b) noise trading by retail investors increases during crises, making the relative signal strength of foreign flow more pronounced.

Individual investors exhibit momentum-chasing behavior, with response coefficients to positive shocks exceeding those to negative shocks by a factor of 6.3. This asymmetry is consistent with behavioral biases documented in the literature and contributes to understanding why retail participation often amplifies rather than dampens market volatility.

### 7.2 Implications

For Practitioners: The methodology provides a framework for adaptive signal processing that automatically discounts noisy observations during stress periods. While overall sample performance is challenging, the strong results during the COVID crisis period (Sharpe 1.08) demonstrate the value of regime-conditional positioning during extreme events.

For Regulators: The finding that foreign investors provide informed liquidity during crises has implications for market stability discussions. Policies that restrict foreign participation during stress periods may inadvertently remove stabilizing forces from the market.

For Researchers: The regime-dependent variation in coefficient magnitudes underscores the importance of allowing for parameter instability in microstructure studies. Estimates from tranquil periods may substantially understate the true information content of order flow during stressed conditions.

### 7.3 Limitations

Several limitations merit acknowledgment. First, the sample period (2020–2024) represents an unusual macroeconomic environment characterized by the COVID shock, unprecedented monetary policy, and subsequent normalization. Results may not generalize to different market conditions.

Second, while the methodology successfully identifies market regimes and asymmetric responses, translating these insights into profitable trading strategies remains challenging. Transaction costs, execution slippage, and the forward-looking nature of regime identification all present implementation hurdles.

Third, our focus on the Korean market, while providing clean investor-type classification, limits generalizability to other markets where such classification is unavailable or constructed differently.

### 7.4 Conclusion

Static models of market microstructure assume stable relationships that empirically fail during stress periods—precisely when accurate models are most needed. This paper demonstrates that explicitly modeling regime-dependence and asymmetric responses yields richer understanding of how different investor classes interact with market conditions.

The paper’s primary contribution is methodological: demonstrating how state-space techniques can be adapted to capture dynamic relationships in financial markets. The empirical findings—particularly the 8.9-fold increase in foreign investor predictive power during crises—provide new evidence on information heterogeneity and its market-condition dependence.

Future research might extend this framework to higher-frequency data, investigate the sources of foreign investor information advantage, or apply similar techniques to other markets with investor-type classification. Understanding when and why order flow relationships change remains central to both academic research and practical market analysis.

## References

* Ang and Bekaert, (2002)

  Ang, A. and Bekaert, G. (2002).
  International asset allocation with regime shifts.
  Review of Financial Studies, 15(4):1137–1187.
* Barber and Odean, (2008)

  Barber, B. M. and Odean, T. (2008).
  All that glitters: The effect of attention and news on the buying
  behavior of individual and institutional investors.
  Review of Financial Studies, 21(2):785–818.
* Chordia et al., (2001)

  Chordia, T., Roll, R., and Subrahmanyam, A. (2001).
  Market liquidity and trading activity.
  Journal of Finance, 56(2):501–530.
* Chordia et al., (2002)

  Chordia, T., Roll, R., and Subrahmanyam, A. (2002).
  Order imbalance, liquidity, and market returns.
  Journal of Financial Economics, 65(1):111–130.
* Easley and O’Hara, (1987)

  Easley, D. and O’Hara, M. (1987).
  Price, trade size, and information in securities markets.
  Journal of Financial Economics, 19(1):69–90.
* Glosten and Milgrom, (1985)

  Glosten, L. R. and Milgrom, P. R. (1985).
  Bid, ask and transaction prices in a specialist market with
  heterogeneously informed traders.
  Journal of Financial Economics, 14(1):71–100.
* Griffin et al., (2003)

  Griffin, J. M., Harris, J. H., and Topaloglu, S. (2003).
  The dynamics of institutional and individual trading.
  Journal of Finance, 58(6):2285–2320.
* Grinblatt and Keloharju, (2001)

  Grinblatt, M. and Keloharju, M. (2001).
  What makes investors trade?
  Journal of Finance, 56(2):589–616.
* Guidolin and Timmermann, (2006)

  Guidolin, M. and Timmermann, A. (2006).
  An econometric model of nonlinear dynamics in the joint distribution
  of stock and bond returns.
  Journal of Applied Econometrics, 21(1):1–22.
* Hamilton, (1989)

  Hamilton, J. D. (1989).
  A new approach to the economic analysis of nonstationary time series
  and the business cycle.
  Econometrica, 57(2):357–384.
* Hasbrouck, (1991)

  Hasbrouck, J. (1991).
  Measuring the information content of stock trades.
  Journal of Finance, 46(1):179–207.
* Hasbrouck and Seppi, (2001)

  Hasbrouck, J. and Seppi, D. J. (2001).
  Common factors in prices, order flows, and liquidity.
  Journal of Financial Economics, 59(3):383–411.
* Kahneman and Tversky, (1979)

  Kahneman, D. and Tversky, A. (1979).
  Prospect theory: An analysis of decision under risk.
  Econometrica, 47(2):263–291.
* Kaniel et al., (2008)

  Kaniel, R., Saar, G., and Titman, S. (2008).
  Individual investor trading and stock returns.
  Journal of Finance, 63(1):273–310.
* Kyle, (1985)

  Kyle, A. S. (1985).
  Continuous auctions and insider trading.
  Econometrica, 53(6):1315–1335.
* Lee and Ready, (1991)

  Lee, C. and Ready, M. J. (1991).
  Inferring trade direction from intraday data.
  Journal of Finance, 46(2):733–746.
* Odean, (1998)

  Odean, T. (1998).
  Are investors reluctant to realize their losses?
  Journal of Finance, 53(5):1775–1798.
* Shefrin and Statman, (1985)

  Shefrin, H. and Statman, M. (1985).
  The disposition to sell winners too early and ride losers too long:
  Theory and evidence.
  Journal of Finance, 40(3):777–790.

## Appendix A Additional Figures

![Refer to caption](x5.png)


Figure 5: Comparison of Filtered versus Raw Order Flow Signal

![Refer to caption](x6.png)


Figure 6: Kalman Filter Method Comparison

![Refer to caption](x7.png)


Figure 7: Regime Characteristics by Market State

![Refer to caption](x8.png)


Figure 8: Asymmetric Response to Market Shocks

![Refer to caption](x9.png)


Figure 9: Drawdown Comparison Across Strategies

![Refer to caption](x10.png)


Figure 10: Sharpe Ratio by Market Regime