---
authors:
- Ilias Aarab
doc_id: arxiv:2512.20460v2
family_id: arxiv:2512.20460
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: The Aligned Economic Index & the State-Switching Model
url_abs: http://arxiv.org/abs/2512.20460v2
url_html: https://arxiv.org/html/2512.20460v2
venue: arXiv q-fin
version: 2
year: 2025
---


Ilias Aarab

(June 2019)

###### Abstract

A growing empirical literature suggests that equity-premium predictability is state dependent, with much of the forecasting power concentrated around recessionary periods [Henkel2011, DanglHalling2012, Devpura2018]. I study U.S. stock return predictability across economic regimes and document strong evidence of time-varying expected returns across both expansionary and contractionary states. I contribute in two ways. First, I introduce a state-switching predictive regression in which the market state is defined in real time using the slope of the yield curve. Relative to the standard one-state predictive regression, the state-switching specification increases both in-sample and out-of-sample performance for the set of popular predictors considered by [WelchGoyal2008], improving the out-of-sample performance of most predictors in economically meaningful ways. Second, I propose a new aggregate predictor, the Aligned Economic Index, constructed via partial least squares (PLS). Under the state-switching model, the Aligned Economic Index exhibits statistically and economically significant predictive power in sample and out of sample, and it outperforms widely used benchmark predictors and alternative predictor-combination methods.

JEL codes: G12, G17, E44, C22, C53

###### keywords:

return predictability; regime switching; partial least squares; equity premium

## 1 Introduction

A large body of work studies whether stock returns are predictable using valuation ratios and macroeconomic indicators (e.g., [FamaFrench1988, CampbellShiller1988, KandelStambaugh1996, Guo2006, Lewellen2004, PolkThompsonVuolteenaho2006]). [WelchGoyal2008] show, however, that many prominent predictive regressions fail to deliver reliable out-of-sample gains relative to simple benchmarks. Two recurrent explanations are model uncertainty, the correct specification is unknown ex ante. and parameter instability, which makes estimates sensitive to the sample period.

Over the past decades, several approaches have been proposed to mitigate these issues, including economically motivated restrictions [PanPettenuzzoWang2020], combinations of multiple predictors [Huang2015], regime-shift specifications [HammerschmidLohre2018], and new predictors [Jiang2019]. While these methods often improve forecasting performance, their gains are frequently concentrated in recessionary episodes, with weaker results in expansions.

A key mechanism behind this pattern is that investors may rely on different information sets and forecasting rules across states. [CujeanHasler2017] provide an equilibrium framework in which agents switch attention and forecasting models over time, and [Devpura2018] document predictor-dependent time variation in return predictability. Motivated by these findings, I use a simple state-dependent predictive regression in which slope coefficients are allowed to change across market states. The resulting state-switching model delivers stronger and more stable predictive performance across both expansionary and recessionary periods than the conventional one-state specification.

## 2 Data

The aggregate stock market return is the excess return on the S&P 500 index: the continuously compounded log return (including dividends) minus the risk-free rate, proxied by the three-month Treasury bill. Working with excess returns focuses attention on the predictability of the (real) equity risk premium rather than on variation driven mechanically by the level of short-term interest rates.

I use updated data from [WelchGoyal2008] covering January 1950 to December 2017. The predictor set includes the 14 popular variables in [WelchGoyal2008], supplemented with the corporate bond premium and the lagged equity premium, for a total of 16 series.222The predictors are: dividend–price ratio (log), dividend yield (log), earnings–price ratio (log), dividend–payout ratio (log), equity premium volatility, book-to-market ratio, net equity expansion, Treasury bill rate, long-term yield, long-term return, term spread, default yield spread, default return spread, inflation, lagged equity premium, and the corporate bond premium. The data can be retrieved from Amit Goyal’s web page (www.hec.unil.ch/agoyal/); variable definitions are provided in [WelchGoyal2008].
Following common practice, I focus on the post-war period. From an investor-relevance perspective, this emphasizes modern market dynamics. From a statistical perspective, [Lewellen2004] argues that pre-1945 data have markedly different properties (e.g., unusually high volatility and persistence in some predictors), which can distort inference. I also exclude 1945–1949 because dividend policies during and immediately after World War II were unusually volatile, potentially affecting the behavior of dividend-based predictors [Frankfurter1997]. Finally, based on preliminary analysis on the first years of data, the baseline sample used throughout is January 1960 to December 2017 (696 monthly observations).

All data are monthly and the baseline forecasting horizon is one month ahead. This horizon is well suited for studying state dependence: business-cycle states typically last several months, so longer-horizon regressions may mechanically average over multiple states and blur regime effects. Moreover, short-horizon predictability can translate into longer-horizon predictability under standard present-value logic [Cochrane2011, Huang2015, RapachRinggenbergZhou2016].

To define market states in real time, I construct an ex-ante indicator based on the slope of the yield curve (the term spread), computed as the 10-year Treasury yield minus the 3-month Treasury bill rate. In contrast to NBER recession dates, which are assigned ex post,333NBER recession dates can be retrieved from the Federal Reserve Bank of St. Louis (FRED). Because these dates are determined ex post, they are not directly usable for real-time forecasting exercises. the yield-curve slope is observable at the time forecasts are formed and is widely viewed as a leading indicator.

## 3 Methodology

### 3.1 Return predictability and switching between states

Under the expectations hypothesis, the term spread reflects the difference between the current short rate and expected future short rates over a longer horizon. When the spread narrows, investors may be more uncertain about future economic conditions and require higher compensation for risk. The yield curve therefore summarizes aspects of macroeconomic sentiment and risk compensation [Wright2006].

The slope of the Treasury yield curve is often treated as an early-warning indicator for downturns: inversions have historically preceded several U.S. recessions. Motivated by this, I define the market state at month tt as a *down state* if the yield curve was flat or inverted at any point in the preceding τ\tau months:

|  |  |  |  |
| --- | --- | --- | --- |
|  | St={1,if tmst−i≤0​ for some ​i∈{1,…,τ},0,otherwise,S\_{t}=\begin{cases}1,&\text{if }\text{tms}\_{t-i}\leq 0\text{ for some }i\in\{1,\dots,\tau\},\\ 0,&\text{otherwise},\end{cases} |  | (1) |

where StS\_{t} is the state indicator and tmst−i\text{tms}\_{t-i} is the term spread (10-year minus 3-month), as in, e.g., [FamaFrench1989, WelchGoyal2008]. The parameter τ\tau controls how long a down state persists after a (near-)inversion. To reduce the risk of in-sample overfitting and data-snooping concerns emphasized by [WelchGoyal2008], I fix τ\tau rather than optimizing it. In the baseline results, I set τ=9\tau=9 months.444Using τ\tau between 3 and 12 months leaves the main findings unchanged. This choice is short enough to avoid mechanically locking the economy into long down states, while remaining consistent with the average duration of recessionary episodes observed in the data.

### 3.2 The state-switching model

I extend the standard predictive regression by allowing slope coefficients to differ across states, as in [Boyd2005, Sander2018]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt+1=(β0+δ0​St)+β1​St​xt+γ1​(1−St)​xt+εt+1,R\_{t+1}=(\beta\_{0}+\delta\_{0}S\_{t})+\beta\_{1}S\_{t}x\_{t}+\gamma\_{1}(1-S\_{t})x\_{t}+\varepsilon\_{t+1}, |  | (2) |

where Rt+1R\_{t+1} is the excess return on the S&P 500 at month t+1t+1, xtx\_{t} is a lagged predictor observed at month tt, and εt+1\varepsilon\_{t+1} is the disturbance term. When β1=γ1\beta\_{1}=\gamma\_{1}, the model collapses to the conventional one-state predictive regression.

Out-of-sample forecasts are formed recursively:

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt+1|t=(b0+d0​St)+b1​St​xt+g1​(1−St)​xt,r\_{t+1|t}=(b\_{0}+d\_{0}S\_{t})+b\_{1}S\_{t}x\_{t}+g\_{1}(1-S\_{t})x\_{t}, |  | (3) |

where (b0,d0,b1,g1)(b\_{0},d\_{0},b\_{1},g\_{1}) are OLS estimates of (β0,δ0,β1,γ1)(\beta\_{0},\delta\_{0},\beta\_{1},\gamma\_{1}) computed using only information available up to time tt. Specifically, for each forecast origin tt, I regress {Rs+1}s=Mt−1\{R\_{s+1}\}\_{s=M}^{t-1} on {1,Ss,Ss​xs,(1−Ss)​xs}s=Mt−1\{1,S\_{s},S\_{s}x\_{s},(1-S\_{s})x\_{s}\}\_{s=M}^{t-1}, where MM is the start of the out-of-sample period. This recursive procedure avoids look-ahead bias by construction.

Combining complementary information from multiple predictors can yield strong forecasting performance across different market states. However, as shown by [WelchGoyal2008], estimating a multivariate “kitchen-sink” regression typically leads to poor out-of-sample performance due to parameter instability and overfitting. To address this, I aggregate information from the 16 predictors in a more parsimonious way by constructing an aligned economic index.

The economic intuition is that investors may shift attention across fundamentals and macro indicators depending on market conditions. Consistent with this view, changes in investor attention and information processing have been linked to return dynamics [BarberOdeanZhu2009, DaEngelbergGao2011].

### 3.3 The Aligned Economic Index

A standard approach to summarize many predictors is principal component analysis (PCA), which reduces dimensionality by extracting common factors that explain maximal predictor variance [StockWatson2002, Jolliffe2002]. When predictors are noisy proxies and idiosyncratic components are correlated across series, however, PCA factors may be contaminated by common noise and become less useful for forecasting [BoivinNg2006]. Partial least squares (PLS) provides an alternative: it constructs components that explicitly maximize covariance with the forecast target (here, future excess returns), rather than explaining total predictor variance [GeladiKowalski1986]. This targeted dimension reduction is well suited to forecasting settings in which much predictor variation may be irrelevant for prediction [KellyPruitt2015]. Appendix [A](https://arxiv.org/html/2512.20460v2#A1 "Appendix A Construction of the Aligned Economic Index ‣ The Aligned Economic Index & the State-Switching Model") describes the construction of the Aligned Economic Index in detail.

![Refer to caption](figs/fig1.png)


Figure 1: The Aligned Economic Index and the equity premium. The upper panel depicts the Aligned Economic Index EP​L​SE^{PLS}; the lower panel shows the normalized equity premium. The sample period is January 1960 to December 2017. Vertical bars denote NBER-dated recessions.

Figure [1](https://arxiv.org/html/2512.20460v2#S3.F1 "Figure 1 ‣ 3.3 The Aligned Economic Index ‣ 3 Methodology ‣ The Aligned Economic Index & the State-Switching Model") plots the Aligned Economic Index (upper panel) and the normalized equity premium (lower panel) over January 1960 to December 2017. The gray bars indicate NBER recessions. If the index contains forecasting information about the risk premium, the two series should comove at business-cycle frequencies.

The figure suggests substantial comovement. Both series drop sharply early in the sample, rise during subsequent recoveries, and display heightened volatility around major market stress episodes (e.g., the late-1987 crash and the 2007–2009 financial crisis). The index is also noticeably less persistent than several classical valuation ratios, suggesting that small-sample bias concerns emphasized by [Stambaugh1999] are less acute for this predictor.

## 4 Empirical Results

Table [1](https://arxiv.org/html/2512.20460v2#S4.T1 "Table 1 ‣ 4 Empirical Results ‣ The Aligned Economic Index & the State-Switching Model") reports predictive regression results using the Aligned Economic Index. Panel A estimates the conventional one-state model using EP​L​SE^{PLS}. Panel B estimates the state-switching model in Equation ([2](https://arxiv.org/html/2512.20460v2#S3.E2 "In 3.2 The state-switching model ‣ 3 Methodology ‣ The Aligned Economic Index & the State-Switching Model")). For comparison, I also report results for two alternative predictor-combination methods: (i) a PCA-based factor EP​C​AE^{PCA},555I retain only the first principal component. In unreported results, including additional factors consistently reduces out-of-sample performance in both the one-state and state-switching specifications. and (ii) the forecast-combination (FC) approach of [Rapach2010], denoted EF​CE^{FC}.

If return predictability is time varying and predictor dependent [Devpura2018], one would expect that allowing coefficients to switch across states should improve performance relative to the one-state specification, and that the magnitude of the gains may differ across combination methods.

Table 1: Forecasting the market excess return with predictor-combination methods

| Panel A: One-state model | | | | |
| --- | --- | --- | --- | --- |
| Predictor | β1\beta\_{1} | t-stat | R¯2\bar{R}^{2} | Roos2R^{2}\_{\text{oos}} |
| EP​L​SE^{PLS} | 0.05\*\*\* | 4.38 | 4.65 | 2.60\*\*\* |
| EP​C​AE^{PCA} | 0.20\*\* | 1.96 | 0.61 | 0.31 |
| EF​CE^{FC} | 0.13 | 0.84 | -0.08 | 1.18\* |

| Panel B: State-switching model | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Predictor | δ0\delta\_{0} | t-stat | β1\beta\_{1} | t-stat | γ1\gamma\_{1} | t-stat | R¯2\bar{R}^{2} | Roos2R^{2}\_{\text{oos}} |
| EP​L​SE^{PLS} | -0.27\*\*\* | -2.51 | 0.03\*\*\* | 3.46 | 0.06\*\*\* | 3.68 | 5.90 | 4.12\*\*\* |
| EP​C​AE^{PCA} | -0.01\*\*\* | -2.54 | 0.17 | 1.27 | 0.25\*\* | 1.97 | 1.65 | 1.58\*\*\* |
| EF​CE^{FC} | -1.22\*\*\* | -2.43 | 0.24 | 0.85 | 0.15 | 0.81 | 1.02 | 2.64\*\*\* |

This table reports one-month-ahead forecasts of the market excess return using EP​L​SE^{PLS}, EP​C​AE^{PCA}, and EF​CE^{FC}. Panel A estimates the standard one-state predictive regression. Panel B estimates the state-switching model in Equation ([2](https://arxiv.org/html/2512.20460v2#S3.E2 "In 3.2 The state-switching model ‣ 3 Methodology ‣ The Aligned Economic Index & the State-Switching Model")). In Panel B, St=1S\_{t}=1 when the yield curve was flat or inverted at least once in the preceding nine months, and St=0S\_{t}=0 otherwise. R¯2\bar{R}^{2} is the in-sample adjusted R2R^{2} over January 1960 to December 2017. Roos2R^{2}\_{\text{oos}} is the out-of-sample R2R^{2} of [CampbellThompson2008], using the first 20 years as the initial estimation window and January 1980 to December 2017 as the evaluation period. t-statistics are Newey–West. Statistical significance for Roos2R^{2}\_{\text{oos}} is based on the MSFE-adjusted statistic of [ClarkWest2007]. \*\*\*, \*\* and \* indicate significance at the 1%, 5%, and 10% levels, respectively.

Panel A shows that both EP​L​SE^{PLS} and EP​C​AE^{PCA} have significant in-sample predictive power. The adjusted R¯2\bar{R}^{2} of EP​L​SE^{PLS} (4.65%) is notably larger than that of EP​C​AE^{PCA} (0.61%), indicating that EP​L​SE^{PLS} explains a larger share of one-month-ahead variation in the equity premium. The forecast-combination predictor EF​CE^{FC} has weak in-sample performance in this specification. Out of sample, EP​C​AE^{PCA} yields a positive but small Roos2R^{2}\_{\text{oos}} (0.31%) that is not statistically significant and falls below the 0.50% economic threshold discussed by [CampbellThompson2008]. In contrast, EF​CE^{FC} achieves a higher Roos2R^{2}\_{\text{oos}} (1.18%), consistent with the forecasting gains reported by [Rapach2010], while EP​L​SE^{PLS} performs best with Roos2=2.60%R^{2}\_{\text{oos}}=2.60\%.

Panel B turns to the state-switching model. Two patterns stand out. First, the state intercept shift δ0\delta\_{0} is statistically significant (Newey–West t-statistics around 2.5) across all three predictors, supporting the relevance of yield-curve-based regimes. Second, both R¯2\bar{R}^{2} and Roos2R^{2}\_{\text{oos}} increase relative to the one-state model for all three predictor-combination methods. All three predictors now produce statistically significant Roos2R^{2}\_{\text{oos}} values that comfortably exceed the [CampbellThompson2008] 0.50% threshold. Among them, EP​L​SE^{PLS} remains the strongest performer, with R¯2=5.90%\bar{R}^{2}=5.90\% and Roos2=4.12%R^{2}\_{\text{oos}}=4.12\%.

Table 2: Forecasting the market excess return across different states

|  | Expansions/Recessions | | | | Up/Down states | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Predictor | R¯exp2\bar{R}^{2}\_{\text{exp}} | R¯rec2\bar{R}^{2}\_{\text{rec}} | Roos,exp2R^{2}\_{\text{oos,exp}} | Roos,rec2R^{2}\_{\text{oos,rec}} | R¯up2\bar{R}^{2}\_{\text{up}} | R¯down2\bar{R}^{2}\_{\text{down}} | Roos,up2R^{2}\_{\text{oos,up}} | Roos,down2R^{2}\_{\text{oos,down}} |
| Panel A: One-state model | | | | | | | | |
| EP​L​SE^{PLS} | 0.57 | 14.49 | 1.45\*\* | 5.99\*\*\* | 5.51 | 2.83 | 4.31\*\*\* | -7.86 |
| EP​C​AE^{PCA} | -0.70 | 4.26 | -1.36 | 5.24\*\*\* | 0.57 | 1.27 | 0.05 | 1.88 |
| EF​CE^{FC} | 0.03 | 0.14 | 0.77 | 2.38\*\*\* | 0.06 | 0.07 | 1.24\*\* | 0.80 |
| Panel B: State-switching model | | | | | | | | |
| EP​L​SE^{PLS} | 1.01 | 19.13 | 1.71\*\* | 11.21\*\*\* | 6.06 | 6.98 | 4.51\*\*\* | 1.68\*\* |
| EP​C​AE^{PCA} | -0.60 | 8.50 | 0.00 | 6.23\*\*\* | 0.92 | 5.18 | 0.67\*\* | 7.12\*\*\* |
| EF​CE^{FC} | 0.02 | 4.92 | 2.19\*\*\* | 3.95\*\*\* | 0.40 | 4.29 | 2.03\*\*\* | 6.36\*\*\* |

This table reports state-by-state forecasting performance for the one-state predictive regression (Panel A) and the state-switching model in Equation ([2](https://arxiv.org/html/2512.20460v2#S3.E2 "In 3.2 The state-switching model ‣ 3 Methodology ‣ The Aligned Economic Index & the State-Switching Model")) (Panel B). EP​L​SE^{PLS}, EP​C​AE^{PCA}, and EF​CE^{FC} denote the PLS-based Aligned Economic Index, the PCA-based factor, and the forecast-combination predictor, respectively. R¯exp2\bar{R}^{2}\_{\text{exp}} and R¯rec2\bar{R}^{2}\_{\text{rec}} are in-sample adjusted R2R^{2} computed within NBER expansions and recessions. R¯up2\bar{R}^{2}\_{\text{up}} and R¯down2\bar{R}^{2}\_{\text{down}} are in-sample adjusted R2R^{2} computed within yield-curve up and down states as defined by StS\_{t}. Roos,⁣⋅2R^{2}\_{\text{oos,}\cdot} denotes the [CampbellThompson2008] out-of-sample R2R^{2} computed within each state, using 1960–1979 as the initial estimation window and 1980–2017 as the evaluation period. Statistical significance for Roos2R^{2}\_{\text{oos}} is based on the [ClarkWest2007] MSFE-adjusted statistic. \*\*\*, \*\* and \* indicate significance at the 1%, 5%, and 10% levels.

Although EP​L​SE^{PLS} is a strong predictor of excess monthly returns when looking at the entire sample period, it is interesting to further evaluate its performance during certain market states. Table [2](https://arxiv.org/html/2512.20460v2#S4.T2 "Table 2 ‣ 4 Empirical Results ‣ The Aligned Economic Index & the State-Switching Model") reports the results across different market states. Panel A shows the forecasting performance using the conventional one-state univariate model, while panel B reports findings using the state switching model. The left part of Panel A shows the in-sample and out-of-sample performance of the one-state model across expansions and recessions. Both EP​L​SE^{PLS} and EP​C​AE^{PCA} can forecast, in-sample, the equity premium during recessions, however only EP​L​SE^{PLS} is able to generate a positive adjusted R¯2\bar{R}^{2} during expansions. Looking at the out-of-sample performance, both EP​C​AE^{PCA} and EF​CE^{FC} produce significant positive Roos2R^{2}\_{\text{oos}} values during recessions, but fail to do so during expansions, with EP​C​AE^{PCA} even failing to outperform the benchmark model of the historical mean. These findings are in line with the conclusions of [Henkel2011] and [DanglHalling2012]: return predictability only exists during recessionary periods. In contrast, the newly formed aligned economic index can significantly predict the equity premium during recessions and expansions. EP​L​SE^{PLS} has an Roos2R^{2}\_{\text{oos}} of 5.99% during recessions and an Roos,exp2R^{2}\_{\text{oos,exp}} of 1.45% during expansions, both significant at the 5% level or stronger. This confirms that using combined information of the predictors in an efficient way leads to improvement across different states. The right part of Panel A shows the same statistics across up and down states as defined by the state indicator based on the inversion of the yield curve (as defined in Equation ([1](https://arxiv.org/html/2512.20460v2#S3.E1 "In 3.1 Return predictability and switching between states ‣ 3 Methodology ‣ The Aligned Economic Index & the State-Switching Model"))). All three models produce positive in-sample R¯2\bar{R}^{2} across both states, with EP​L​SE^{PLS} outperforming the models substantially across both states. The out-of-sample results are less clear. First, EP​C​AE^{PCA} fails to significantly outperform the benchmark model during an upstate and during a downstate. Thus, EP​C​AE^{PCA} is only able to capture predictability during parts of the recessionary periods that do not overlap with the downstate periods. Secondly, both EP​L​SE^{PLS} and EF​CE^{FC} outperform, significantly on the 5% level or stronger, the naïve benchmark model during an upstate but fail to do so during a downstate with EP​L​SE^{PLS} even generating a negative Roos,down2R^{2}\_{\text{oos,down}} of -7.86%. A downstate is initiated whenever the yield curve inverts, which generally happens right before the start of a recession. Thus, with the one-state model EP​L​SE^{PLS} fails to predict the equity premium right before the start of a recession. These findings are in line with [Sander2018] who shows that estimating the start of a recession inaccurately can lead to large economic consequences. In short, even though EP​L​SE^{PLS} outperforms the other two combination methods across different states, it still fails to outperform the naïve benchmark model around the start of a recession in the one-state model.

Moving on to the state switching model in panel B of Table [2](https://arxiv.org/html/2512.20460v2#S4.T2 "Table 2 ‣ 4 Empirical Results ‣ The Aligned Economic Index & the State-Switching Model"), we see substantial performance gains across different states. First the in-sample performance of all three combination methods are further enhanced within the state switching model, however in line with panel A only EP​L​SE^{PLS} is able to generate performance gains exceeding 1% across all states. More noteworthy, the out-of-sample performance is substantially affected by the state switching model. EP​C​AE^{PCA} is able to significantly forecast the equity premium during recessions, up states and down states. During expansions however both EP​C​AE^{PCA} and the benchmark model predict, on average, the equity premium with the same capacity producing an Roos2R^{2}\_{\text{oos}} of zero. In contrast, both EP​L​SE^{PLS} and EF​CE^{FC} can significantly, on the 5% level or stronger, predict the equity premium during expansions, recessions, up states and down states. EP​L​SE^{PLS} generates Roos2R^{2}\_{\text{oos}} values of respectively 1.71% and 1.68% during expansions and down states, while producing Roos2R^{2}\_{\text{oos}} values of respectively 11.21% and 4.51% during recessions and up states. All of the values thus exceed the economic threshold of 0.50% of [CampbellThompson2008] meaning that an investor using the state switching model with EP​L​SE^{PLS} would make consistent substantial gains across the different market states. The main difference with the one-state model is the fact that EP​L​SE^{PLS} is now able to predict the equity premium during the recessionary turning points as well, with the inversion of the yield curve (i.e. a down state) helping to time the right moment to change slope coefficients. Interestingly, the forecast combination method EF​CE^{FC} exhibits the same overall behavior as EP​L​SE^{PLS}. EF​CE^{FC} generates Roos2R^{2}\_{\text{oos}} values of respectively 2.19% and 6.36% during expansions and down states, while producing Roos2R^{2}\_{\text{oos}} values of respectively 3.95% and 2.03% during recessions and up states. Thus both EP​L​SE^{PLS} and EF​CE^{FC} are able to consistently outperform the naïve benchmark model across all market states, with EP​L​SE^{PLS} yielding the overall greatest performance. In the next section I further analyze the relationship between EP​L​SE^{PLS} and EF​CE^{FC}.

### 4.1 EP​L​SE^{PLS} versus EF​CE^{FC}

Over the out-of-sample period (January 1980 to December 2017), the forecasts implied by EP​L​SE^{PLS} and EF​CE^{FC} are strongly correlated (about 65%). The correlation rises further within down states, suggesting that both methods capture a similar component of risk-premium variation when turning-point risk is elevated.

![Refer to caption](figs/fig2.png)


Figure 2: Excess market return forecasts of EP​L​SE^{PLS} and EF​CE^{FC}, January 1980 to December 2017. The orange line shows the out-of-sample forecast based on EP​L​SE^{PLS}, the blue line the forecast based on EF​CE^{FC}, and the green line the realized excess market return. Vertical bars denote NBER-dated recessions.

Figure [2](https://arxiv.org/html/2512.20460v2#S4.F2 "Figure 2 ‣ 4.1 𝐸^{𝑃⁢𝐿⁢𝑆} versus 𝐸^{𝐹⁢𝐶} ‣ 4 Empirical Results ‣ The Aligned Economic Index & the State-Switching Model") compares the two forecast series to realized returns. Forecasts based on EP​L​SE^{PLS} are more volatile than those based on EF​CE^{FC}, while realized excess returns are most volatile. This difference is intuitive: PLS is a targeted method that loads more heavily on predictor components that covary with returns, whereas EF​CE^{FC} averages across many individual predictive regressions, which mechanically smooths forecasts [Rapach2010]. The higher responsiveness of EP​L​SE^{PLS} can be beneficial in environments where predictability is time varying.

![Refer to caption](figs/fig3.png)


Figure 3: Weights of EP​L​SE^{PLS} and EF​CE^{FC} on fundamental variables, January 1980 to December 2017. The figure shows time-varying PLS weights for the 16 variables (DP, DY, EP, DE, SVAR, BM, NTIS, TBL, LTY, LTR, TMS, DFY, DFR, INFL, e​R​meRm, e​B​meBm). EF​CE^{FC} assigns equal weights of 6.25%. Vertical bars denote NBER-dated recessions.

Figure [3](https://arxiv.org/html/2512.20460v2#S4.F3 "Figure 3 ‣ 4.1 𝐸^{𝑃⁢𝐿⁢𝑆} versus 𝐸^{𝐹⁢𝐶} ‣ 4 Empirical Results ‣ The Aligned Economic Index & the State-Switching Model") shows that EP​L​SE^{PLS} places time-varying weight on the underlying predictors, with relatively large average weights on equity premium volatility, the Treasury bill rate, and the long-term yield. Weight variation is more pronounced around regime transitions, consistent with state-dependent and time-varying predictability [Devpura2018]. In contrast, EF​CE^{FC} uses constant equal weights, which helps explain its smoother forecast path.

## 5 Concluding remarks

This paper studies return predictability using a real-time state-switching predictive regression and a new PLS-based aggregate predictor. The state-switching model uses the slope of the yield curve to define market regimes and generally improves the predictive performance of widely used predictors in sample and out of sample. The Aligned Economic Index EP​L​SE^{PLS} aggregates information from the [WelchGoyal2008] predictor set (augmented with two additional series) using a targeted dimension-reduction approach. Empirically, EP​L​SE^{PLS} delivers strong and robust forecasting performance, and its gains are especially pronounced when combined with the state-switching specification. Importantly, the resulting framework yields statistically significant and economically meaningful out-of-sample improvements across both expansionary and recessionary regimes, making it a practical alternative to one-state predictive regressions whose performance is often concentrated in recessions.

\addappheadtotoc

## Appendix A Construction of the Aligned Economic Index

Assume the risk premium can be decomposed into a conditional expectation and an innovation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt+1=𝔼t​[Rt+1]+ξt+1,R\_{t+1}=\mathbb{E}\_{t}[R\_{t+1}]+\xi\_{t+1}, |  | (4) |

where 𝔼t​[Rt+1]\mathbb{E}\_{t}[R\_{t+1}] is driven by an unobservable latent factor FtF\_{t}. Suppose

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼t​[Rt+1]=α0+α1​Ft.\mathbb{E}\_{t}[R\_{t+1}]=\alpha\_{0}+\alpha\_{1}F\_{t}. |  | (5) |

Combining ([4](https://arxiv.org/html/2512.20460v2#A1.E4 "In Appendix A Construction of the Aligned Economic Index ‣ The Aligned Economic Index & the State-Switching Model"))–([5](https://arxiv.org/html/2512.20460v2#A1.E5 "In Appendix A Construction of the Aligned Economic Index ‣ The Aligned Economic Index & the State-Switching Model")) yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt+1=α0+α1​Ft+ξt+1.R\_{t+1}=\alpha\_{0}+\alpha\_{1}F\_{t}+\xi\_{t+1}. |  | (6) |

Next, assume predictors follow a factor structure:

|  |  |  |  |
| --- | --- | --- | --- |
|  | xi,t=δi,0+δi,1​Ft+δi,2​Yt+ηi,t,i=1,…,N,x\_{i,t}=\delta\_{i,0}+\delta\_{i,1}F\_{t}+\delta\_{i,2}Y\_{t}+\eta\_{i,t},\quad i=1,\dots,N, |  | (7) |

where xi,tx\_{i,t} is predictor ii, YtY\_{t} is a common noise component, and ηi,t\eta\_{i,t} is idiosyncratic noise. PCA extracts linear combinations of xi,tx\_{i,t} that explain total predictor variance, potentially loading on YtY\_{t} and reducing forecasting usefulness. PLS instead targets the component most related to the forecast target.

In the first step, run NN time-series regressions of each lagged predictor on the realized risk premium (used as an instrument for the latent factor):

|  |  |  |  |
| --- | --- | --- | --- |
|  | xi,t−1=ϕi,0+ϕi,1​Rt+νi,t,t=1,…,T.x\_{i,t-1}=\phi\_{i,0}+\phi\_{i,1}R\_{t}+\nu\_{i,t},\quad t=1,\dots,T. |  | (8) |

Taking conditional expectations gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼t​[xi,t−1]=ϕi,0+ϕi,1​𝔼t​[Rt].\mathbb{E}\_{t}[x\_{i,t-1}]=\phi\_{i,0}+\phi\_{i,1}\mathbb{E}\_{t}[R\_{t}]. |  | (9) |

Using 𝔼t​[Rt]=α0+α1​Ft−1\mathbb{E}\_{t}[R\_{t}]=\alpha\_{0}+\alpha\_{1}F\_{t-1} implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | xi,t−1=ϕi,0+ϕi,1​(α0+α1​Ft−1)+error.x\_{i,t-1}=\phi\_{i,0}+\phi\_{i,1}(\alpha\_{0}+\alpha\_{1}F\_{t-1})+\text{error}. |  | (10) |

Thus ϕi,1\phi\_{i,1} captures how predictor ii loads on a rotation of the latent factor, while filtering out the unpredictable innovation component.

In the second step, for each tt, run a cross-sectional regression of {xi,t}i=1N\{x\_{i,t}\}\_{i=1}^{N} on the estimated first-stage loadings:

|  |  |  |  |
| --- | --- | --- | --- |
|  | xi,t=ϕ0,t+Ft​ϕi+φi,t,i=1,…,N,x\_{i,t}=\phi\_{0,t}+F\_{t}\phi\_{i}+\varphi\_{i,t},\quad i=1,\dots,N, |  | (11) |

where ϕi\phi\_{i} denotes the estimated loading from the first stage. The fitted value yields the PLS factor estimate, which I denote by the Aligned Economic Index EtP​L​S≡FtP​L​SE\_{t}^{PLS}\equiv F\_{t}^{PLS}.

Finally, I use EtP​L​SE\_{t}^{PLS} as the predictor in the state-switching regression:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼t​[Rt+1]=(β0+δ0​St)+β1​St​EtP​L​S+γ1​(1−St)​EtP​L​S+εt+1.\mathbb{E}\_{t}[R\_{t+1}]=(\beta\_{0}+\delta\_{0}S\_{t})+\beta\_{1}S\_{t}E\_{t}^{PLS}+\gamma\_{1}(1-S\_{t})E\_{t}^{PLS}+\varepsilon\_{t+1}. |  | (12) |

Following [KellyPruitt2015], the second-stage factor estimate is a consistent estimator of the latent component relevant for forecasting. For the out-of-sample analysis, index weights and factor estimates are computed recursively using only information available up to the forecast-formation date.