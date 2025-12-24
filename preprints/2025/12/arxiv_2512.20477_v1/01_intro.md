---
authors:
- Ilias Aarab
doc_id: arxiv:2512.20477v1
family_id: arxiv:2512.20477
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Switching between states and the COVID-19 turbulence
url_abs: http://arxiv.org/abs/2512.20477v1
url_html: https://arxiv.org/html/2512.20477v1
venue: arXiv q-fin
version: 1
year: 2025
---


Ilias Aarab

(November 2020)

###### Abstract

In [Aarab2020AlignedEconomicIndexStateSwitching], I examine U.S. stock return predictability across economic regimes and document evidence of time-varying expected returns across market states in the long run. The analysis introduces a state-switching specification in which the market state is proxied by the slope of the yield curve, and proposes an Aligned Economic Index built from the popular predictors of [welch\_goyal\_2008] (augmented with bond and equity premium measures). The Aligned Economic Index under the state-switching model exhibits statistically and economically meaningful in-sample (R2=5.9%R^{2}=5.9\%) and out-of-sample (Roos2=4.12%R^{2}\_{\text{oos}}=4.12\%) predictive power across both recessions and expansions, while outperforming a range of widely used predictors. In this work, I examine the added value for professional practitioners by computing the economic gains for a mean-variance investor and find substantial added benefit of using the new index under the state switching model across all market states. The Aligned Economic Index can thus be implemented on a consistent real-time basis. These findings are crucial for both academics and practitioners as expansions are much longer-lived than recessions. Finally, I extend the empirical exercises by incorporating data through September 2020 and document sizable gains from using the Aligned Economic Index, relative to more traditional approaches, during the COVID-19 market turbulence.

JEL codes: G12, G17, E44, C22, C53

###### keywords:

return predictability; regime switching; partial least squares; equity premium

## 1 Introduction

A large literature studies whether aggregate stock returns are predictable (e.g. [fama\_french\_1988], [campbell\_shiller\_stock\_prices\_1988], [kandel\_stambaugh\_1996], [guo\_2002], [lewellen\_2004], and [polk\_thompson\_vuolteenaho\_2006]). However, [welch\_goyal\_2008] show that many time-varying forecasting models fail to deliver reliable out-of-sample improvements for market timing based on ex-ante information. Two recurring challenges are model uncertainty (the appropriate specification is unknown ex ante) and parameter instability (estimates vary strongly across sample periods), both of which can materially degrade real-time performance.

In response, more recent work has proposed approaches that explicitly address these issues, including economically motivated restrictions [pan\_pettenuzzo\_wang\_2018], forecast combinations [huang\_jiang\_tu\_zhou\_2015], regime-shift specifications [hammerschmid\_lohre\_2018], and new predictors [jiang\_lee\_martin\_zhou\_2019]. While these contributions often report economically meaningful in-sample and out-of-sample predictability, performance is frequently concentrated in specific episodes, most notably recessions, rather than being robust across the business cycle.

This state dependence is consistent with evidence and theory suggesting that investors process information differently across regimes. For example, [cujean\_hasler\_2017] develop an equilibrium model in which investors rely on different forecasting rules and respond to different types of news depending on the prevailing state. [devpura\_kumar\_sunila\_2018] formally test for time-varying predictability and find that it is both time-varying and predictor-dependent.

Motivated by these findings, [Aarab2020AlignedEconomicIndexStateSwitching] proposes a simple state-dependent predictive regression in which coefficients are allowed to differ across market states. The state is proxied by the slope of the yield curve: an inversion corresponds to a down state, while a positive slope corresponds to an up state. The model is combined with a single, interpretable predictor, an Aligned Economic Index, constructed from the fundamental predictors of [welch\_goyal\_2008] and supplemented by bond- and equity-premium information.222The 16 fundamental variables are the dividend-price ratio (log), dividend yield (log), earnings-price ratio (log), dividend-payout ratio (log), equity risk premium volatility, book-to-market ratio, net equity expansion, Treasury bill rate, long-term yield, long-term return, term spread, default yield spread, default return spread, inflation, lagged equity premium, and the corporate bond premium. The data can be retrieved from Amit Goyal’s web page at <http://www.hec.unil.ch/agoyal/>. A detailed description is provided in [welch\_goyal\_2008].

The index is constructed using the partial least squares (PLS) approach introduced by [wold\_1975] and refined by [kelly\_pruitt\_2013, kelly\_pruitt\_2015]. [Aarab2020AlignedEconomicIndexStateSwitching] shows that the resulting Aligned Economic Index (EPLSE^{\text{PLS}}) outperforms other combination approaches, such as principal components (EPCAE^{\text{PCA}}) and the forecast-combination approach of [rapach\_strauss\_zhou\_2010], as well as a range of widely used predictors.

This study focuses on a practitioner-oriented question: how much economic value does the Aligned Economic Index deliver when used to guide real-time portfolio allocation? To answer this question, I quantify the gains for a mean-variance investor and compare them to standard benchmarks.

## 2 Data

The aggregate stock market return is measured as the excess return: the continuously compounded log return on the S&P 500 index (including dividends) minus the risk-free rate (proxied by the three-month Treasury bill). By focusing on excess returns, I net out inflation and the level of interest rates, thereby targeting predictability of the real risk premia.

I use the updated dataset of [welch\_goyal\_2008] covering 14 widely used fundamental predictors from January 1950 to September 2020, supplemented by bond- and equity-premium measures.

The focus on the post-war sample is motivated by both economic relevance and statistical considerations. First, from an investor’s perspective, it is natural to evaluate predictability in more recent decades: a forecasting model is more compelling if it performs reliably out of sample over the modern period, regardless of its earlier performance [welch\_goyal\_2008]. Second, [lewellen\_2004] argues that predictive regressions should be estimated using data after World War II, since pre-1945 return dynamics and predictor properties differ markedly (e.g. the extreme volatility of the 1930s affects both the variance and persistence of multiple predictors). I also exclude 1945–1949 because dividend policies around the war era were unusually volatile, which may distort the behavior of dividend-based predictors [frankfurter\_1997]. Finally, reserving the first decade for initial experimentation, the main empirical results use January 1960 to September 2020 (729 months), capturing the initial impact of the COVID-19 turbulence.

All data are monthly, and the analysis focuses on the one-month forecasting horizon. First, the state indicators considered here (e.g. business cycle expansions and recessions) typically persist for several months, so longer-horizon regressions may mechanically mix regimes within the forecasting window and blur state-specific behavior. Second, [cochrane\_2011] notes that short-horizon predictability often implies stronger predictability at longer horizons, with related evidence in, for example, [huang\_jiang\_tu\_zhou\_2015] and [rapach\_strauss\_zhou\_2016].

To implement regime shifts in real time, I construct an ex-ante state indicator based on the yield-curve slope. This avoids reliance on the NBER recession indicator, which is determined ex post and is therefore not directly usable in a real-time allocation rule.333The NBER recession indicator can be retrieved from the Federal Reserve Bank of St. Louis. [sander\_2018] shows that real-time recession classification can be unreliable, and that misclassifying turning points can lead to substantial losses. Specifically, the slope is measured as the 10-year Treasury yield minus the 3-month Treasury bill rate (secondary market).

## 3 Asset allocation exercise

To provide a direct measure of the forecasting value of the Aligned Economic Index for economic agents, I evaluate its economic value in a mean-variance portfolio choice problem. The key question is whether the predictive model delivers better investment guidance than a standard baseline forecast.

Consider an investor with a one-month horizon who chooses portfolio weights to maximize expected utility of terminal wealth Wt+1W\_{t+1} conditional on information available at time tt. Following [campbell\_thompson\_2008], [neely\_rapach\_tu\_zhou\_2014], [rapach\_strauss\_zhou\_2016], and [sander\_2018], I assume mean-variance preferences in the spirit of [markowitz\_1952]. The investor allocates between the S&P 500 index and U.S. Treasury bills (or a combination of both). The investor’s objective is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ut=𝔼t​(Rt+1p)−γ2​Vart​(Rt+1p),U\_{t}\;=\;\mathbb{E}\_{t}\!\left(R^{p}\_{t+1}\right)\;-\;\frac{\gamma}{2}\,\mathrm{Var}\_{t}\!\left(R^{p}\_{t+1}\right), |  | (1) |

where Rt+1pR^{p}\_{t+1} is the simple444For the asset-allocation analysis, I forecast the simple excess return (rather than the log excess return used in [Aarab2020AlignedEconomicIndexStateSwitching]). portfolio return in month t+1t+1, and γ\gamma is the coefficient of relative risk aversion.

I compute the optimal portfolio weights implied by ([1](https://arxiv.org/html/2512.20477v1#S3.E1 "In 3 Asset allocation exercise ‣ Switching between states and the COVID-19 turbulence")) using (i) forecasts generated by the Aligned Economic Index under either a one-state regression or a state-switching regression, and (ii) a benchmark model based on the historical mean. I then summarize economic value using differences in certainty-equivalent returns (CERs). As discussed in [rapach\_strauss\_zhou\_2016], the CER gain can be interpreted as the annualized portfolio management fee an investor would be willing to pay to access the predictive information relative to the historical-mean benchmark. Appendix [A](https://arxiv.org/html/2512.20477v1#A1 "Appendix A Asset allocation optimization ‣ Switching between states and the COVID-19 turbulence") provides the full derivation and implementation details.

## 4 Methodology

For each predictor-combination method (PLS, PCA, and forecast combination), I compute out-of-sample certainty-equivalent return (CER) gains. Following [Aarab2020AlignedEconomicIndexStateSwitching], I produce out-of-sample forecasts in a monthly sample from 1980:01 to 2020:09, beginning after a 20-year training period.555All index weights are estimated recursively using only information available up to the forecast formation date tt, so the procedure avoids look-ahead bias. Each month, I estimate the first two conditional moments of the portfolio return series and compute optimal portfolio weights by maximizing ([1](https://arxiv.org/html/2512.20477v1#S3.E1 "In 3 Asset allocation exercise ‣ Switching between states and the COVID-19 turbulence")). With regard risk preferences, I follow [huang\_jiang\_tu\_zhou\_2015] and set γ=3\gamma=3.666[Aarab2020AlignedEconomicIndexStateSwitching] also reports results for γ=5\gamma=5 in their work; and show that the qualitative conclusions remain unchanged. Following [johnson\_2017], I impose leverage limits (up to 50%) and rule out short selling, yielding realistic portfolio constraints.777Short selling by financial institutions has been partially restricted in many countries after the 2008 global financial crisis [bensoussan\_wong\_yam\_yung\_2014].

In addition, I restrict month-to-month portfolio adjustment by requiring that the risky-asset position cannot more than double (or be reduced by more than half) from one month to the next, which helps stabilize weights given the well-known sensitivity of mean-variance allocations to return forecasts [barbara\_j\_2015].

I compute CER gains relative to the historical-mean benchmark and annualize them by multiplying by 1,200, so they can be interpreted as annual percentage management fees. I also report results net of proportional transaction costs of 50 basis points (bps) per transaction.

As an additional benchmark, I consider a buy-and-hold investor who purchases the market at the start of the out-of-sample period and holds it without rebalancing through the end of the sample.

Finally, I evaluate state dependence by reporting CER gains separately across expansions, recessions, and yield-curve up/down states, mirroring the state-based evaluation in [Aarab2020AlignedEconomicIndexStateSwitching]. Statistical significance is assessed by testing H0:Δ​CER≤0H\_{0}:\Delta\mathrm{CER}\leq 0 against HD:Δ​CER>0H\_{D}:\Delta\mathrm{CER}>0 using the bootstrap procedure of [mccracken\_valente\_2018].

## 5 Empirical results

### 5.1 The one-state regression model

Table [1](https://arxiv.org/html/2512.20477v1#S5.T1 "Table 1 ‣ 5.2 The state switching model ‣ 5 Empirical results ‣ Switching between states and the COVID-19 turbulence") depicts the main results. The upper part of Panel A displays results for the one-state regression models, while the lower part depicts results under the state-switching model. The second column presents the difference in CER gains (Δ​CER\Delta\mathrm{CER}) without transaction costs, while column five reports the difference in CER gains net of transaction costs. I also report additional portfolio performance measures. Column 3 shows the monthly Sharpe ratio, computed as the mean portfolio return in excess of the risk-free rate divided by the standard deviation of the excess portfolio return. Column 4 reports relative average monthly turnover, where monthly turnover is defined as the percentage of wealth rebalanced at the end of the month. Relative average turnover is computed as average turnover divided by the average turnover of the investor who uses the historical-average forecast.

There are several noteworthy observations. First, the CER for the portfolio based on the historical-average forecast is 7.56% for January 1980 to September 2020. The Δ​CER\Delta\mathrm{CER} values of all three combination methods are positive under the one-state regression model; however, only EPLSE^{\text{PLS}} has a Δ​CER\Delta\mathrm{CER} that is significantly different from zero at the 10% level (or stronger). In line with these positive certainty-equivalent gains, the Sharpe ratios of the forecasting models all exceed that of the historical average (0.13), with EPLSE^{\text{PLS}} and EFCE^{\text{FC}} yielding the highest ratio of 0.16. Average turnover is 2.09% for the historical-average portfolio. Portfolios based on the forecasting models turn over approximately three to four times more often than the historical-average portfolio. After accounting for transaction costs, these relatively high turnover rates reduce Δ​CER\Delta\mathrm{CER} gains: values turn negative for EPCAE^{\text{PCA}} and EFCE^{\text{FC}}, and none of the forecasting models produces a statistically significant Δ​CER\Delta\mathrm{CER} different from zero net of costs.

When looking across different states, the historical-average model produces substantial Δ​CER\Delta\mathrm{CER} gains during expansions and up states of 13.00% and 10.74%, respectively, but yields negative gains across recessions and down states of -17.46% and -1.08%. As expected, the historical-average model is unable to quickly adapt to sharp drops in equity returns during recessions and down states.

The forecasting models exhibit the reversed behavior across market states. All three models fail to generate significant Δ​CER\Delta\mathrm{CER} gains during expansions, with EPCAE^{\text{PCA}} and EFCE^{\text{FC}} even failing to outperform the benchmark model. In contrast, during recessions all three models produce statistically significant Δ​CER\Delta\mathrm{CER} values at the 5% level (or stronger), with EPCAE^{\text{PCA}} yielding the highest gains of 5.82%.

Lastly, note that in great contrast to the three forecasting models, the simple buy-and-hold strategy yields significant Δ​CER\Delta\mathrm{CER} gains of 1.51% over the full sample period. Moreover, buy-and-hold produces positive Δ​CER\Delta\mathrm{CER} values across expansions (although not significantly), recessions, and up states. During down states, however, buy-and-hold underperforms the historical-average model and produces Δ​CER\Delta\mathrm{CER} gains of -3.90%.

In conclusion, none of the forecasting models can significantly outperform the naive historical benchmark once transaction costs are imposed, with any positive Δ​CER\Delta\mathrm{CER} gains concentrated around recessions. More surprisingly, among the considered approaches the buy-and-hold strategy yields the highest Δ​CER\Delta\mathrm{CER} value and is the only one to outperform the historical-average forecast over the full sample, but it still fails to do so across all market states. These results echo the earlier findings of [henkel\_martin\_nardari\_2011]: the short-horizon performance of aggregate return predictors such as the dividend yield and the short rate appears negligible during business-cycle expansions but sizable during contractions.

### 5.2 The state switching model

These results, however, change drastically under the state-switching models (lower part of Table [1](https://arxiv.org/html/2512.20477v1#S5.T1 "Table 1 ‣ 5.2 The state switching model ‣ 5 Empirical results ‣ Switching between states and the COVID-19 turbulence")). First, the Δ​CER\Delta\mathrm{CER} values of all three combination methods are significantly positive and economically substantial under the state-switching model, with EPLSE^{\text{PLS}} yielding the highest performance of 6.09%. In line with these high Δ​CER\Delta\mathrm{CER} gains, the state-switching models generate considerably higher monthly Sharpe ratios than the historical-average benchmark (0.13), with EPLSE^{\text{PLS}} generating the highest ratio of 0.25, almost double that of the benchmark. After netting transaction costs of 50 bps per transaction, all three models still produce large CER gains in excess of the benchmark model, and all are significantly different from zero at the 5% level (or stronger). More specifically, EPLSE^{\text{PLS}} still yields the highest performance gains net of transaction costs, with Δ​CER=5.54%\Delta\mathrm{CER}=5.54\%, implying that a mean-variance investor would be willing to pay an annual management fee of up to 5.54% to access the forecasts generated by the aligned, state-switching economic index rather than using the naive historical average.

The improvement from the one-state regression models to the state-switching models is substantial. The average Sharpe ratio increases from 0.15 (the average across the one-state models) to 0.23 under the state-switching model. The average net-of-transaction-costs CER gain increases from -0.03% under the one-state model to 4.42% under the state-switching model. This confirms the earlier finding of [Aarab2020AlignedEconomicIndexStateSwitching] that combining the complementary information in the predictors delivers the best performance when regression coefficients are allowed to vary across states. Most noticeably, the buy-and-hold strategy outperforms the one-state forecasting strategies but fails to do so once state switching is introduced. All three state-switching models generate CER gains far exceeding those of buy-and-hold, with EPLSE^{\text{PLS}} producing gains that are almost four times larger than those of buy-and-hold.

The improvement under state switching is also evident across states. First, consistent with the one-state regression results, all three state-switching models significantly outperform the historical average during recessions. Second, while the one-state models fail to outperform the benchmark during expansions, the state-switching models all exhibit positive CER gains, with both EPLSE^{\text{PLS}} and EFCE^{\text{FC}} (CER gains of 0.89% and 1.26%, respectively) significantly outperforming the historical average at the 5% level (or stronger).

Across down states, all three models outperform the historical average, with CER gains ranging from 7.09% (EPCAE^{\text{PCA}}) up to 9.59% (EFCE^{\text{FC}}). Note how both EPLSE^{\text{PLS}} and EFCE^{\text{FC}} under the state-switching model consistently outperform the historical average across all market states. In contrast, even the buy-and-hold strategy cannot significantly outperform the historical average during expansions and generates a negative value of -3.90% during down states (i.e. yield-curve inversions, which most often occur shortly before recessions). These findings mirror the out-of-sample Roos2R^{2}\_{\text{oos}} results in [Aarab2020AlignedEconomicIndexStateSwitching]: under the state-switching model, both EPLSE^{\text{PLS}} and EFCE^{\text{FC}} consistently outperform the naive benchmark across market states, with EPLSE^{\text{PLS}} delivering the strongest overall performance.

Table 1: Asset allocation results

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Overall | | | | Across states (cost = 50bps) | | | |
| Predictor | Δ\DeltaCER | SR | Rel. avg. turnover | Δ\DeltaCER (50bps) | Δ\DeltaCERexp{}\_{\text{exp}} | Δ\DeltaCERrec{}\_{\text{rec}} | Δ\DeltaCERup{}\_{\text{up}} | Δ\DeltaCERdown{}\_{\text{down}} |
| HA | 7.65 | 0.13 | 2.47 | 7.5 | 13.00 | -17.46 | 10.74 | -1.08 |
| Buy & hold | 1.35\*\* | 0.16 | 0.00 | 1.51\*\* | 1.10 | 4.09\*\* | 2.39\*\* | -3.90 |
| One-state model | | | | | | | | |
| EPLSE^{\text{PLS}} | 1.17\* | 0.16 | 5.42 | 0.52 | 0.30 | 5.58\*\*\* | 0.93 | -2.00 |
| EPCAE^{\text{PCA}} | 0.54 | 0.14 | 8.65 | -0.59 | -1.17 | 5.82\*\*\* | 0.38 | 1.46\*\* |
| EFCE^{\text{FC}} | 1.16 | 0.16 | 8.93 | -0.03 | -0.89 | 2.44\*\* | -0.02 | 4.28\*\* |
| State switching model | | | | | | | | |
| EPLSE^{\text{PLS}} | 6.09\*\*\* | 0.25 | 4.76 | 5.54\*\* | 0.89\*\* | 18.66\*\*\* | 2.02\*\* | 9.27\*\*\* |
| EPCAE^{\text{PCA}} | 4.45\*\* | 0.22 | 6.82 | 3.58\*\* | 0.20 | 23.81\*\*\* | 0.46 | 7.09\*\*\* |
| EFCE^{\text{FC}} | 4.71\*\*\* | 0.22 | 4.70 | 4.15\*\*\* | 1.26\*\* | 2.92\*\*\* | 1.50\*\* | 9.59\*\*\* |

* •

  This table reports portfolio performance measures for an investor with mean-variance preferences and relative risk-aversion coefficient of three who monthly allocates between equities and risk-free bills using either an historical average (HA) or predictive regression equity risk premium forecast. The predictors are the aligned economic index constructed with the PLS-method EPLSE^{\text{PLS}}, the predictor index based on the PCA-method EPCAE^{\text{PCA}} and the predictor based on the forecast combination approach EFCE^{\text{FC}} under either the traditional one-state regression model or the state switching model. The Δ\DeltaCER statistic is the annualized certainty equivalent return gain for an investor who uses the predictive regression forecast instead of the historical average forecast; for the historical average forecast, the table reports the CER level. Δ\DeltaCER statistics are also reported separately across different states. Δ\DeltaCERexp{}\_{\text{exp}}, Δ\DeltaCERrec{}\_{\text{rec}}, Δ\DeltaCERup{}\_{\text{up}}, Δ\DeltaCERdown{}\_{\text{down}} are respectively the CER return gains across expansions, recessions, up states and down states. Relative average turnover is the average turnover for the portfolio based on the predictive regression forecast divided by the average turnover for the portfolio based on the historical average forecast; for the historical average forecast, the table reports the average turnover level. The “cost = 50bps” statistic is the CER gain assuming a proportional transactions cost of 50 basis points per transaction. Statistical significance for Δ\DeltaCER is based on the p-value of the bootstrap procedure of [mccracken\_valente\_2018] for testing the null H0:Δ​CER≤0H\_{0}:\Delta\mathrm{CER}\leq 0 against the alternative HD:Δ​CER>0H\_{D}:\Delta\mathrm{CER}>0. \*\*\*, \*\* and \* indicate significance at the 1%, 5%, and 10% levels, respectively.

## 6 Equity weights and cumulative wealth exercise

To better understand the portfolio dynamics implied by the different models, Figure [1](https://arxiv.org/html/2512.20477v1#S6.F1 "Figure 1 ‣ 6 Equity weights and cumulative wealth exercise ‣ Switching between states and the COVID-19 turbulence") plots the equity weights over time. The upper panel shows the one-state models, and the lower panel shows the state-switching models.

In the one-state models, equity weights are highly volatile, especially for EPCAE^{\text{PCA}} and EFCE^{\text{FC}}, consistent with the higher turnover reported in Table [1](https://arxiv.org/html/2512.20477v1#S5.T1 "Table 1 ‣ 5.2 The state switching model ‣ 5 Empirical results ‣ Switching between states and the COVID-19 turbulence"). More importantly, all three one-state predictors (EPLSE^{\text{PLS}}, EPCAE^{\text{PCA}}, and EFCE^{\text{FC}}) fail to reduce equity exposure in advance of recessions. For example, at the onset of the subprime crisis all three models are fully invested with equity weights near 150%. Only after the recession begins do they start reducing exposure, and they do so in a volatile manner, reaching their lowest weights near the end of the recession (roughly 39% for EPLSE^{\text{PLS}}, 27% for EFCE^{\text{FC}}, and 16% for EPCAE^{\text{PCA}}). In other words, the one-state models adjust too slowly around turning points, remaining heavily exposed during the most adverse period and thereby generating poor CER performance. A similar pattern emerges during the initial COVID-19 market turbulence in early 2020: the models start the episode with substantial equity exposure and then reduce it erratically, ending with average equity weights around 50% by September 2020, which contributes to sizable portfolio drawdowns. This is consistent with [sander\_2018], who emphasizes that misclassifying turning points can be costly.

The lower panel of Figure [1](https://arxiv.org/html/2512.20477v1#S6.F1 "Figure 1 ‣ 6 Equity weights and cumulative wealth exercise ‣ Switching between states and the COVID-19 turbulence") shows that state-switching models generate much smoother and more timely adjustments around recessions. The models begin reducing equity exposure before recessions, reach low exposure near the start of recessions, and then gradually increase exposure as conditions improve. For instance, ahead of the subprime crisis the models reduce equity weights from about 150% at the end of 2006 to near 0% by the end of 2007, and then rebuild exposure during the recession, reaching local highs near the end of the recession (approximately 130% for EPLSE^{\text{PLS}}, 80% for EPCAE^{\text{PCA}}, and 70% for EFCE^{\text{FC}}). During the COVID-19 episode, yield-curve inversions in late 2019 and again in early 2020 trigger gradual de-risking, leaving equity weights in the safe single digits by September 2020. As a result, the risky-asset share is materially reduced during the height of the turbulence.

Across expansions, state-switching models can appear more responsive than one-state models and often take larger equity positions. This behavior is consistent with state-dependent slopes: when the model assigns higher expected premia in up states, it rationally tilts more aggressively toward risky assets. By contrast, one-state regressions estimate a single average slope across regimes, which tends to imply more conservative allocations.

![Refer to caption](figs/fig1a.png)


(a) One-state regression model.

![Refer to caption](figs/fig1b.png)


(b) State-switching model.

Figure 1: Asset allocation results, equity weights, January 1980 to September 2020. The upper panel delineates the equity weight for a mean-variance investor with relative risk aversion coefficient of three who optimally allocates across equities and the risk-free asset using a predictive regression excess return forecast based on the one-state regression model of the aligned economic index constructed with the PLS-method EPLSE^{\text{PLS}}, the predictor index based on the PCA-method EPCAE^{\text{PCA}} or the predictor based on the forecast combination approach EFCE^{\text{FC}}. The bottom panel corresponds to the same statistics but assumes return forecasts based on the state switching model. The indices, regression coefficients and equity weights are estimated recursively based on information up to the period of forecast formation period tt alone. The vertical bars correspond to NBER-dated recessions. The dashed vertical red line indicates the last quarter of 2019.

As a robustness check and to illustrate the magnitude of the economic gains implied by the state-switching aligned economic index, I also report a cumulative wealth simulation.

Specifically, I consider eight mean-variance investors with identical preferences who each invest an initial wealth of $1 in a portfolio consisting of T-bills, the market index, or a combination of both. Each investor follows one of the previously discussed strategies (historical-average benchmark, buy-and-hold, EPLS/EPCA/EFCE^{\text{PLS}}/E^{\text{PCA}}/E^{\text{FC}} under the one-state model, and EPLS/EPCA/EFCE^{\text{PLS}}/E^{\text{PCA}}/E^{\text{FC}} under the state-switching model). The investors allocate from January 1980 through September 2020 using the optimal weights implied by each strategy and reinvest proceeds throughout. All investors have risk aversion coefficient γ=3\gamma=3.

Figure [2](https://arxiv.org/html/2512.20477v1#S6.F2 "Figure 2 ‣ 6 Equity weights and cumulative wealth exercise ‣ Switching between states and the COVID-19 turbulence") plots cumulative wealth. The upper panel shows the one-state models. Consistent with Figure [1](https://arxiv.org/html/2512.20477v1#S6.F1 "Figure 1 ‣ 6 Equity weights and cumulative wealth exercise ‣ Switching between states and the COVID-19 turbulence"), investors experience large drawdowns at the start of recessions because they do not reduce equity exposure quickly enough. The buy-and-hold investor consistently outperforms other one-state strategies during expansions, reaching a terminal wealth of $102 by September 2020. By contrast, investors using one-state forecasting models end with terminal wealth near $40, similar to the historical-average investor ($38). These outcomes mirror Table [1](https://arxiv.org/html/2512.20477v1#S5.T1 "Table 1 ‣ 5.2 The state switching model ‣ 5 Empirical results ‣ Switching between states and the COVID-19 turbulence"): among one-state strategies, buy-and-hold performs best and is the only strategy that clearly outperforms the historical-average benchmark.

The lower panel shows cumulative wealth under state switching. All three state-switching strategies are considerably more resilient around recessionary turning points, with far smaller drawdowns. During the COVID-19 turbulence, for example, one-state strategies, the historical-average benchmark, and buy-and-hold all experience pronounced declines, while state-switching strategies remain comparatively stable. Over the full sample, state-switching strategies also accumulate substantially more wealth: terminal wealth reaches $325 for EPLSE^{\text{PLS}}, $197 for EFCE^{\text{FC}}, and $174 for EPCAE^{\text{PCA}}, far exceeding buy-and-hold ($102) and the historical-average benchmark ($38). The outperformance is particularly visible in long expansions. After the 2008 recession, for instance, the EPLSE^{\text{PLS}} investor increases wealth from $91 to $325 (257%), compared to $36 to $102 (183%) for buy-and-hold, highlighting the value of the state-switching aligned economic index beyond short recession episodes.

![Refer to caption](figs/fig2a.png)


(a) One-state models.

![Refer to caption](figs/fig2b.png)


(b) State-switching models.

Figure 2: Asset allocation results, cumulative wealth, January 1980 to September 2020. The upper panel shows cumulative wealth for a mean-variance investor with relative risk aversion coefficient of three who allocates between equities and the risk-free asset using predictive-regression excess return forecasts based on one-state models: PLS (EPLSE^{\text{PLS}}), PCA (EPCAE^{\text{PCA}}), forecast combination (EFCE^{\text{FC}}), the historical average (HA), or buy-and-hold. The bottom panel reports cumulative wealth under the corresponding state-switching models. Indices, regression coefficients, and equity weights are estimated recursively using only information available at the forecast-formation period tt. Vertical bars correspond to NBER-dated recessions. The dashed vertical red line marks the last quarter of 2019.

## 7 Concluding remarks

This article evaluates the economic value of a regime-switching return-prediction model that combines state dependence with a new Aligned Economic Index. Consistent with the evidence in [Aarab2020AlignedEconomicIndexStateSwitching], I find that using EPLSE^{\text{PLS}} within the state-switching framework delivers economically large and statistically significant certainty-equivalent return gains for a mean-variance investor across market states, and outperforms all considered alternatives, including buy-and-hold. These findings matter for practitioners because expansions are long-lived relative to recessions: unlike many predictors whose gains are concentrated in contractions, the state-switching Aligned Economic Index delivers value that is more robust across the business cycle and can be implemented on a consistent real-time basis.

\addappheadtotoc

## Appendix A Asset allocation optimization

Consider an economic agent with an investment horizon of one month that wishes to maximize expected utility of terminal wealth Wt+1W\_{t+1} conditional on information up to time tt. Following [campbell\_thompson\_2008], [neely\_rapach\_tu\_zhou\_2014], [rapach\_strauss\_zhou\_2016], and [sander\_2018], I assume mean-variance preferences as in [markowitz\_1952]. The investor can allocate between the S&P 500 index and U.S. Treasury bills (or a combination). The utility function is given in ([1](https://arxiv.org/html/2512.20477v1#S3.E1 "In 3 Asset allocation exercise ‣ Switching between states and the COVID-19 turbulence")).

Let Rt+1rR^{r}\_{t+1} and Rt+1fR^{f}\_{t+1} denote the return on the risky asset (S&P 500) and the risk-free asset (T-bills) at time t+1t+1, respectively. Let ωt\omega\_{t} denote the share invested in the risky asset. The portfolio return is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt+1p=ωt​Rt+1r+(1−ωt)​Rt+1f.R^{p}\_{t+1}\;=\;\omega\_{t}R^{r}\_{t+1}+(1-\omega\_{t})R^{f}\_{t+1}. |  | (2) |

Rearranging,

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt+1p=Rt+1f+ωt​Rt+1e,R^{p}\_{t+1}\;=\;R^{f}\_{t+1}+\omega\_{t}R^{e}\_{t+1}, |  | (3) |

where Rt+1e=Rt+1r−Rt+1fR^{e}\_{t+1}=R^{r}\_{t+1}-R^{f}\_{t+1} is the excess return.

The investor solves

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxωt⁡𝔼t​(Rt+1p)−γ2​Vart​(Rt+1p).\max\_{\omega\_{t}}\ \mathbb{E}\_{t}\!\left(R^{p}\_{t+1}\right)-\frac{\gamma}{2}\,\mathrm{Var}\_{t}\!\left(R^{p}\_{t+1}\right). |  | (4) |

Following [johnson\_2017], I assume that Rt+1fR^{f}\_{t+1} is observed at the end of month tt, so the conditional moments satisfy:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | 𝔼t​(Rt+1p)\displaystyle\mathbb{E}\_{t}(R^{p}\_{t+1}) | =Rt+1f+ωt​𝔼t​(Rt+1e),\displaystyle=R^{f}\_{t+1}+\omega\_{t}\,\mathbb{E}\_{t}(R^{e}\_{t+1}), |  | (5) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vart​(Rt+1p)\displaystyle\mathrm{Var}\_{t}(R^{p}\_{t+1}) | =ωt2​Vart​(Rt+1e).\displaystyle=\omega\_{t}^{2}\,\mathrm{Var}\_{t}(R^{e}\_{t+1}). |  | (6) |

The first-order condition yields

|  |  |  |  |
| --- | --- | --- | --- |
|  | ωt∗=𝔼t​(Rt+1e)γ​Vart​(Rt+1e).\omega\_{t}^{\*}\;=\;\frac{\mathbb{E}\_{t}(R^{e}\_{t+1})}{\gamma\,\mathrm{Var}\_{t}(R^{e}\_{t+1})}. |  | (7) |

Because the conditional mean and variance are unknown, they must be estimated. I estimate the conditional mean using the predictive regression forecast from the Aligned Economic Index:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼t​(Rt+1e)=r^t+1|t,\mathbb{E}\_{t}(R^{e}\_{t+1})\;=\;\widehat{r}\_{t+1|t}, |  | (8) |

where r^t+1|t\widehat{r}\_{t+1|t} is the one-step-ahead forecast produced recursively using only information available at time tt.

To allow for time-varying volatility, I follow [campbell\_thompson\_2008] and estimate Vart​(Rt+1e)\mathrm{Var}\_{t}(R^{e}\_{t+1}) using a five-year rolling window of historical excess returns:

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ^t+1|t2=1N−1​∑i=t−N+1t(Rie−Re¯t)2,N=12×5=60.\widehat{\sigma}^{2}\_{t+1|t}\;=\;\frac{1}{N-1}\sum\_{i=t-N+1}^{t}\left(R^{e}\_{i}-\overline{R^{e}}\_{t}\right)^{2},\qquad N=12\times 5=60. |  | (9) |

Thus, the estimated optimal weight is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ω^t∗=r^t+1|tγ​σ^t+1|t2.\widehat{\omega}\_{t}^{\*}\;=\;\frac{\widehat{r}\_{t+1|t}}{\gamma\,\widehat{\sigma}^{2}\_{t+1|t}}. |  | (10) |

The realized portfolio return is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt+1p=Rt+1f+ω^t∗​Rt+1e.R^{p}\_{t+1}\;=\;R^{f}\_{t+1}+\widehat{\omega}\_{t}^{\*}\,R^{e}\_{t+1}. |  | (11) |

From these returns, the certainty-equivalent return (CER) is

|  |  |  |  |
| --- | --- | --- | --- |
|  | CER=𝔼​(Rt+1p)−γ2​Var​(Rt+1p),\mathrm{CER}\;=\;\mathbb{E}\!\left(R^{p}\_{t+1}\right)-\frac{\gamma}{2}\,\mathrm{Var}\!\left(R^{p}\_{t+1}\right), |  | (12) |

which I estimate using unconditional moments of realized portfolio returns. Using unconditional moments is conservative because it requires the estimated conditional moments to be consistent with subsequent return distributions [johnson\_2017].

For the benchmark, I compute the same allocation rule but replace the predictive mean with the historical mean up to time tt:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ω^t∗,0=r¯tγ​σ^t+1|t2,\widehat{\omega}^{\*,0}\_{t}\;=\;\frac{\overline{r}\_{t}}{\gamma\,\widehat{\sigma}^{2}\_{t+1|t}}, |  | (13) |

where r¯t\overline{r}\_{t} is the sample mean up to month tt.888Using identical variance estimates ensures that differences in CER gains reflect differences in expected return estimates.

The benchmark CER is

|  |  |  |  |
| --- | --- | --- | --- |
|  | CER0=𝔼​(Rt+1f+ω^t∗,0​Rt+1e)−γ2​Var​(Rt+1f+ω^t∗,0​Rt+1e).\mathrm{CER}\_{0}\;=\;\mathbb{E}\!\left(R^{f}\_{t+1}+\widehat{\omega}^{\*,0}\_{t}R^{e}\_{t+1}\right)-\frac{\gamma}{2}\,\mathrm{Var}\!\left(R^{f}\_{t+1}+\widehat{\omega}^{\*,0}\_{t}R^{e}\_{t+1}\right). |  | (14) |

Finally, the CER gain is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​CER=CER−CER0.\Delta\mathrm{CER}\;=\;\mathrm{CER}-\mathrm{CER}\_{0}. |  | (15) |

As in [rapach\_strauss\_zhou\_2016], Δ​CER\Delta\mathrm{CER} can be interpreted as the annualized management fee an investor would be willing to pay for the predictive information embedded in the regression forecast relative to the historical-average forecast.