---
authors:
- Demetrio Lacava
- Edoardo Otranto
doc_id: arxiv:2601.21447v1
family_id: arxiv:2601.21447
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Trade uncertainty impact on stock-bond correlations: Insights from conditional
  correlation models'
url_abs: http://arxiv.org/abs/2601.21447v1
url_html: https://arxiv.org/html/2601.21447v1
venue: arXiv q-fin
version: 1
year: 2026
---

10
20
22
44
2
3
6
4
4

b) Testing H0H\_{0} of constant correlations


LR
LM


CCC-PE vs CCC
STCC-TUE vs CCC
STCC-TUPE vs CCC-PE


192.6014
88.5000
22452240.0000


[18.3070]
[21.0261]
[36.4150]


c) Testing H0H\_{0} of constant stock-bond correlations


CCC-PE
STCC-TUE
STCC-TUPE

𝒲\mathcal{W}
131.9417
273.5868
509.8305


[9.4877]
[9.4877]
[15.5073]

d) Testing nested models


STCC-TUPE vs STCC-TUE
DCC-TUPE vs DCC
DCC-TUPE vs DCC-TUE

LR
215.0006
1321.2946
18.1816


[33.9244]
[9.4877]
[7.8147]


DCC-TUPE vs DCC-TUPEψ
DCC-TUPE vs DCC-PE
DCC-TUPEψ vs DCC-TUE

LR
3.6456
1158.3964
14.5360


[5.9915]
[5.9915]
[3.8415]


DCC-TUE vs DCC
DCC-PE vs DCC
DCC-TUPEψ vs DCC

LR
1303.1130
162.8982
1317.6490


[3.8415]
[5.9915]
[5.9915]

Finally, panel d) reports LR tests for nested specifications, assessing whether additional parameters significantly improve the model’s fit. In nearly all cases, the LR statistics exceed the 5% chi-squared critical values, showing that both STCC and DCC models provide a superior fit relative to their restricted versions. The only exception is DCC-TUPE versus DCC-TUPEψ, where the LR statistic (3.646) falls short of the 5% threshold (5.992). This suggests that the GARCH-like correlation dynamics are homogeneous across scenarios shaped by trade uncertainty and presidential regimes, while the exogenous TPU effect remains heterogeneous, confirming its key role in driving correlation dynamics.

### 4.2 Out-of-Sample Forecasting Comparison

The out-of-sample analysis relies on a rolling window scheme with a fixed estimation sample of 2,049 observations and 60 out-of-sample forecasts per iteration. The window is rolled forward by 60 observations each time, yielding 10 estimation–forecasting periods and a total of 600 out-of-sample forecasts. Model comparison is conducted using the MCS procedure (Hansen et al., [2011](https://arxiv.org/html/2601.21447v1#bib.bib22)), which identifies, for a given significance level and loss function, the set of best models with similar forecasting performance.
We consider two loss functions. First, the Q​L​i​k​eQLike loss, which is consistent according to Patton ([2011](https://arxiv.org/html/2601.21447v1#bib.bib24)), defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qlike=1Th∑τ=1Th(ln|𝐇^τ|+trace(𝐇^τ−1𝐂τ),Qlike=\frac{1}{T\_{h}}\sum\_{\tau=1}^{T\_{h}}\left(ln|\mathbf{\hat{H}\_{\tau}}|+trace(\mathbf{\hat{H}\_{\tau}}^{-1}\mathbf{C}\_{\tau}\right), |  | (8) |

where 𝐇^τ\hat{\mathbf{H}}\_{\tau} denotes the forecasted covariance matrix, 𝐂τ=𝒓τ′​𝒓τ\mathbf{C}\_{\tau}=\bm{r}\_{\tau}^{\prime}\bm{r}\_{\tau} is the realized covariance proxy, and ThT\_{h} is the number of forecasts.
Second, we consider an economic loss function based on the Global Minimum Variance (G​M​VGMV) portfolio (Engle and Colacito, [2006](https://arxiv.org/html/2601.21447v1#bib.bib16)), constructed from forecasted covariances as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | G​M​V=1Th​∑τ=1Th(𝒗^τ′​𝐇^τ​𝒗^τ),GMV=\frac{1}{T\_{h}}\sum\_{\tau=1}^{T\_{h}}\left(\hat{\bm{v}}^{\prime}\_{\tau}\mathbf{\hat{H}\_{\tau}}\hat{\bm{v}}\_{\tau}\right), |  | (9) |

with 𝒗^τ=n​𝐇^τ−1​𝐣n/(𝐣n′​𝐇^τ−1​𝐣n)\hat{\bm{v}}\_{\tau}=\sqrt{n}\hat{\mathbf{H}}\_{\tau}^{-1}\mathbf{j}\_{n}/\big(\mathbf{j}^{\prime}\_{n}\hat{\mathbf{H}}\_{\tau}^{-1}\mathbf{j}\_{n}\big), where 𝐣n\mathbf{j}\_{n} is a vector of ones.

Table 9: Model Confidence Set with Q​l​i​k​eQlike and G​M​VGMV as loss functions. The first row represents the first model removed, down to the best performing model in the last row.Set of superior models and associated p-values in bold.

TRT\_{R}

TS​QT\_{SQ}

Q​l​i​k​eQlike
G​M​VGMV

Q​l​i​k​eQlike
G​M​VGMV


Model
p-value
Model
p-value

Model
p-value
Model
p-value

DCC
0.0000
STCC-TUE
0.0000

DCC
0.0000
STCC-TUE
0.0000

DCC-PE
0.0000
DCC-TUPE
0.0000

DCC-PE
0.0000
DCC-TUPE
0.0000

CCC
0.0000
DCC-TUPEψ
0.0000

CCC
0.0000
DCC-TUPEψ
0.0000

STCC-TUPE
0.0000
DCC-TUE
0.0000

STCC-TUPE
0.0000
DCC-TUE
0.0000

CCC-PE
0.0000
STCC-TUPE
0.0000

CCC-PE
0.0000
STCC-TUPE
0.0006

STCC-TUE
0.0000
CCC-PE
0.0000

STCC-TUE
0.0000
CCC-PE
0.0006

DCC-TUE
0.0009
CCC
0.0000

DCC-TUE
0.0057
CCC
0.0006

DCC-TUPE
0.2309
DCC
0.926

DCC-TUPE
0.2292
DCC
0.9274

DCC-TUPEψ

DCC-PE


DCC-TUPEψ

DCC-PE

Table [9](https://arxiv.org/html/2601.21447v1#S4.T9 "Table 9 ‣ 4.2 Out-of-Sample Forecasting Comparison ‣ 4 Evaluating Competitive Models ‣ Trade uncertainty impact on stock-bond correlations: Insights from conditional correlation models") reports the MCS p-values, highlighting in bold the models included in the superior set. Results are consistent across both test statistics, the Range (TRT\_{R}) and Semi-Quadratic (TS​QT\_{SQ}).555See Hansen et al. ([2011](https://arxiv.org/html/2601.21447v1#bib.bib22)) for details about these statistics. First, the CCC model is systematically excluded, confirming that constant correlations are too restrictive even out-of-sample. Second, DCC specifications dominate STCC alternatives. Under the Q​L​i​k​eQLike loss, accounting for both trade uncertainty and political effects is crucial, as the DCC-TUPE and DCC-TUPEψ deliver the strongest forecasting performance. Under the G​M​VGMV loss, the DCC with political effects emerges as the best model, although the simpler DCC performs comparably well.

## 5 Concluding Remarks

We argue that the correlation between U.S. stocks and bonds is influenced by trade uncertainty and the political cycle. To investigate this, we extend the most widely used conditional correlation models (CCC, STCC, DCC) to incorporate two proxies for these effects: the TPU index to capture trade uncertainty, and a presidential dummy to distinguish Republican from Democratic terms. Our multivariate analysis considers four major U.S. stock market indices and 10-year Treasury bonds.

We proceed by gradually increasing model flexibility, starting from the CCC benchmark with constant correlations and no external effects, up to the DCC-TUPE, which combines a GARCH-type dynamic structure with both sources of variation. By presenting estimation results alongside each model, we show how fit and interpretability improve as flexibility increases. Out-of-sample analysis further confirms the superior performance of DCC models, particularly those that account for both effects.
Our findings indicate that stock–bond correlations rise in periods of high trade uncertainty and during Republican administrations, which often introduced trade shocks such as new tariffs. Correlations shift from strongly positive values in times of high uncertainty – especially under Republican administrations – to zero or even negative values during periods of low uncertainty. In contrast, correlations among stock indices remain persistently high and largely unaffected by these factors.
These results highlight the importance of monitoring stock–bond correlations. High correlations imply similar behavior across the two asset classes, undermining the role of bonds as portfolio stabilizers.

In conclusion, the recent development of multivariate models for conditional correlations opens avenues for further research. For instance, the VDCC class of models proposed by Bauwens and Otranto ([2016](https://arxiv.org/html/2601.21447v1#bib.bib5)), originally designed to capture the impact of volatility on financial correlations, could be extended to this framework. In this sense, our analysis points to a promising line of inquiry that may be pursued with alternative methodological tools. Finally, by focusing on individual stocks rather than equity indices, it would be possible to further investigate the impact of TPU at the firm level, with the possibility of detecting asymmetric and heterogeneous responses.

### Conflicts of interest

The authors declare that they have no competing interests.

### Funding

Financial support is acknowledged by Otranto: Italian PRIN 2022 grant (20223725WE) “Methodological and computational issues in large-scale time series models for economics and finance”. The views and opinions expressed are solely those of the authors and do not necessarily reflect those of the EU, nor can the EU be held responsible for them.

### Data availability

The data underlying this article are available upon request

### Author contributions statement

D.L: Writing – Original Draft, Methodology, Investigation, Conceptualization, Formal analysis, Data Curation, Validation.
E.O: Writing – Review & Editing, Supervision, Methodology, Conceptualization, Validation, Formal analysis, Funding acquisition.

## References

* Aielli (2013)

  G. P. Aielli.
  Dynamic conditional correlation: on properties and estimation.
  *Journal of Business & Economic Statistics*, 31(3):282–299, 2013.
* Andersson et al. (2008)

  M. Andersson, E. Krylova, and S. Vähämaa.
  Why does the correlation between stock and bond returns vary over
  time?
  *Applied Financial Economics*, 18(2):139–151, 2008.
* Baele et al. (2010)

  L. Baele, G. Bekaert, and K. Inghelbrecht.
  The determinants of stock and bond return comovements.
  *The Review of Financial Studies*, 23(6):2374–2428, 2010.
* Baker et al. (2016)

  S. R. Baker, N. Bloom, and S. J. Davis.
  Measuring economic policy uncertainty.
  *The Quarterly Journal of Economics*, 131(4):1593–1636, 2016.
* Bauwens and Otranto (2016)

  L. Bauwens and E. Otranto.
  Modeling the dependence of conditional correlations on market
  volatility.
  *Journal of Business & Economic Statistics*, 34(2):254–268, 2016.
* Bauwens et al. (2006)

  L. Bauwens, S. Laurent, and J. V. K. Rombouts.
  Multivariate GARCH models: a survey.
  *Journal of Applied Econometrics*, 21:79–109, 2006.
* Bekaert et al. (2010)

  G. Bekaert, E. Engstrom, and S. R. Grenadier.
  Stock and bond returns with moody investors.
  *Journal of Empirical Finance*, 17(5):867–894, 2010.
* Bloom (2009)

  N. Bloom.
  The impact of uncertainty shocks.
  *Econometrica*, 77(3):623–685, 2009.
* Bollerslev (1990)

  T. Bollerslev.
  Modelling the coherence in short-run nominal exchange rates: a
  multivariate generalized arch model.
  *The Review of Economics and Statistics*, 72(3):498–505, 1990.
* Bollerslev et al. (1988)

  T. Bollerslev, R. F. Engle, and J. M. Wooldridge.
  A capital asset pricing model with time-varying covariances.
  *Journal of Political Economy*, 96:116–131, 1988.
* Brogaard and Detzel (2015)

  J. Brogaard and A. Detzel.
  The asset-pricing implications of government economic policy
  uncertainty.
  *Management Science*, 61(1):3–18, 2015.
* Caldara et al. (2020)

  D. Caldara, M. Iacoviello, P. Molligo, A. Prestipino, and A. Raffo.
  The economic effects of trade policy uncertainty.
  *Journal of Monetary Economics*, 109:38–59, 2020.
* Chiang et al. (2009)

  T. C. Chiang, H.-C. Yu, and M.-C. Wu.
  Statistical properties, dynamic conditional correlation and scaling
  analysis: Evidence from dow jones and nasdaq high-frequency data.
  *Physica A: Statistical Mechanics and its Applications*,
  388(8):1555–1570, 2009.
* Connolly et al. (2005)

  R. Connolly, C. Stivers, and L. Sun.
  Stock market uncertainty and the stock-bond return relation.
  *Journal of Financial and Quantitative Analysis*, 40(1):161–194, 2005.
* Demirer and Gupta (2018)

  R. Demirer and R. Gupta.
  Presidential cycles and time-varying bond–stock market correlations:
  Evidence from more than two centuries of data.
  *Economics Letters*, 167:36–39, 2018.
* Engle and Colacito (2006)

  R. Engle and R. Colacito.
  Testing and valuing dynamic correlations for asset allocation.
  *Journal of Business & Economic Statistics*, 24(2):238–253, 2006.
* Engle and Kroner (1995)

  R. Engle and F. K. Kroner.
  Multivariate simultaneous generalized arch.
  *Econometric Theory*, 11:122–150, 1995.
* Engle (2002)

  R. F. Engle.
  New frontiers for ARCH models.
  *Journal of Applied Econometrics*, 17:425–446, 2002.
* Fang et al. (2017)

  L. Fang, H. Yu, and L. Li.
  The effect of economic policy uncertainty on the long-term
  correlation between US stock and bond markets.
  *Economic Modelling*, 66:139–145, 2017.
* Fang et al. (2018)

  L. Fang, B. Chen, H. Yu, and C. Xiong.
  The effect of economic policy uncertainty on the long-run correlation
  between crude oil and the US stock markets.
  *Finance Research Letters*, 24:56–63, 2018.
* Glosten et al. (1993)

  L. R. Glosten, R. Jagannanthan, and D. E. Runkle.
  On the relation between the expected value and the volatility of the
  nominal excess return on stocks.
  *The Journal of Finance*, 48(5):1779–1801,
  1993.
* Hansen et al. (2011)

  P. R. Hansen, A. Lunde, and J. M. Nason.
  The model confidence set.
  *Econometrica*, 79(2):453–497, 2011.
* Pastor and Veronesi (2012)

  L. Pastor and P. Veronesi.
  Uncertainty about government policy and stock prices.
  *The Journal of Finance*, 67(4):1219–1264,
  2012.
* Patton (2011)

  A. J. Patton.
  Volatility forecast comparison using imperfect volatility proxies.
  *Journal of Econometrics*, 160(1):246 –
  256, 2011.
  ISSN 0304-4076.
* Silvennoinen and Teräsvirta (2009)

  A. Silvennoinen and T. Teräsvirta.
  Modeling multivariate autoregressive conditional heteroskedasticity
  with the double smooth transition conditional correlation garch model.
  *Journal of Financial Econometrics*, 7(4):373–411, 2009.
* Silvennoinen and Teräsvirta (2015)

  A. Silvennoinen and T. Teräsvirta.
  Modeling conditional correlations of asset returns: A smooth
  transition approach.
  *Econometric Reviews*, 34(1-2):174–197,
  2015.
* White (1980)

  H. White.
  A heteroskedasticity-consistent covariance matrix estimator and a
  direct test for heteroskedasticity.
  *Econometrica*, 48(4):817–38, 1980.
* Yilmazkuday (2023)

  H. Yilmazkuday.
  Covid-19 effects on the S&P 500 index.
  *Applied Economics Letters*, 30(1):7–13,
  2023.
* Yilmazkuday (2024)

  H. Yilmazkuday.
  Geopolitical risk and stock prices.
  *European Journal of Political Economy*, 83:102553,
  2024.
* Yilmazkuday (2025)

  H. Yilmazkuday.
  US tariffs and stock prices.
  *Finance Research Letters*, 83:107708, 2025.