---
authors:
- Hangyi Zhao
doc_id: arxiv:2602.06198v1
family_id: arxiv:2602.06198
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Insider Purchase Signals in Microcap Equities: Gradient Boosting Detection
  of Abnormal Returns'
url_abs: http://arxiv.org/abs/2602.06198v1
url_html: https://arxiv.org/html/2602.06198v1
venue: arXiv q-fin
version: 1
year: 2026
---


Hangyi Zhao
  
hyz0815@stanford.edu

(January 2025)

###### Abstract

This paper examines whether SEC Form 4 insider purchase filings predict abnormal returns in U.S. microcap stocks. The analysis covers 17,237 open-market purchases across 1,343 issuers from 2018 through 2024, restricted to market capitalizations between $30M and $500M. A gradient boosting classifier trained on insider identity, transaction history, and market conditions at disclosure achieves AUC of 0.70 on out-of-sample 2024 data. At an optimized threshold of 0.20, precision is 0.38 and recall is 0.69. The distance from the 52-week high dominates feature importance, accounting for 36% of predictive signal. A momentum pattern emerges in the data: transactions disclosed after price appreciation exceeding 10% yield the highest mean cumulative abnormal return (6.3%) and the highest probability of outperformance (36.7%). This contrasts with the simple mean-reversion intuition often applied to post-run-up entries. The result is robust to winsorization and holds across subsamples. These patterns are consistent with slower information incorporation in illiquid markets, where trend confirmation may filter for higher-conviction insider signals.

Keywords: Insider Trading, Form 4, Microcap Stocks, Abnormal Returns, Gradient Boosting

## 1 Introduction

Corporate insiders must disclose open-market transactions in their firm’s equity within two business days via SEC Form 4 (SEC, [2002](https://arxiv.org/html/2602.06198v1#bib.bib11)). A large literature documents that such disclosures, particularly purchases, tend to precede positive abnormal returns (Lakonishok & Lee, [2001](https://arxiv.org/html/2602.06198v1#bib.bib10); Jeng et al., [2003](https://arxiv.org/html/2602.06198v1#bib.bib9); Cohen et al., [2012](https://arxiv.org/html/2602.06198v1#bib.bib4)). The economic intuition is straightforward: insiders possess private information about firm prospects, and their willingness to risk personal capital signals positive expectations. Most existing evidence, however, derives from large-cap and mid-cap stocks where analyst coverage is dense and price discovery is rapid.

This paper focuses on the microcap segment—stocks with market capitalizations between $30 million and $500 million. This setting is structurally distinct: sparse analyst coverage and low institutional ownership impede the rapid diffusion of public information, while wider bid-ask spreads create limits to arbitrage. These frictions suggest that insider signals in this segment may contain more unpriced information than their large-cap counterparts.

I study whether gradient boosting methods can extract actionable signals from Form 4 filings in this illiquid environment. Using a classifier trained on insider role, trading history, and market conditions at disclosure, I evaluate out-of-sample predictability on 2024 data. This paper makes three specific contributions:

* •

  Methodological application: I demonstrate that non-linear classifiers (XGBoost) outperform linear baselines in detecting abnormal returns in the noisy microcap data, improving AUC from 0.67 to 0.70.
* •

  Feature identification: I isolate “distance from 52-week high” as the dominant predictor of post-disclosure returns, superseding insider identity or transaction size.
* •

  Momentum finding: I document a counter-intuitive pattern where insider purchases disclosed into price strength outperform those disclosed into weakness, challenging standard mean-reversion heuristics in this asset class.

## 2 Related Work

### 2.1 Insider Trading and Information Content

Jaffe ([1974](https://arxiv.org/html/2602.06198v1#bib.bib8)) established that insiders earn abnormal returns on their trades. Seyhun ([1986](https://arxiv.org/html/2602.06198v1#bib.bib12)) showed that purchases are more informative than sales, as litigation risk discourages selling on negative private information. Lakonishok & Lee ([2001](https://arxiv.org/html/2602.06198v1#bib.bib10)) documented that the predictive content of insider purchases increases when multiple insiders buy simultaneously. Cohen et al. ([2012](https://arxiv.org/html/2602.06198v1#bib.bib4)) introduced a distinction between routine trades (calendar-driven, predictable) and opportunistic trades (irregular, information-driven), finding that only the latter predict returns. The present study extends this line of work to microcap stocks, where the opportunistic-routine distinction may be less relevant given sparse coverage and lower liquidity.

### 2.2 Machine Learning in Return Prediction

Gu et al. ([2020](https://arxiv.org/html/2602.06198v1#bib.bib7)) demonstrated that tree-based ensembles and neural networks outperform linear models in capturing cross-sectional return predictability. Chen et al. ([2024](https://arxiv.org/html/2602.06198v1#bib.bib2)) applied deep learning to fundamental and technical features with similar conclusions. However, applications to regulatory filings remain limited. To my knowledge, no prior work applies nonlinear classification to Form 4 signals specifically in the microcap segment, nor explicitly models the interaction between disclosure-window price dynamics and subsequent abnormal returns.

### 2.3 Microcap Market Structure

Microcap stocks exhibit higher idiosyncratic volatility, lower turnover, and wider spreads than larger equities (Fama & French, [1992](https://arxiv.org/html/2602.06198v1#bib.bib5)). Amihud ([2002](https://arxiv.org/html/2602.06198v1#bib.bib1)) showed that illiquidity commands a return premium. These structural features imply that public information may be incorporated more slowly, creating scope for systematic signal extraction from regulatory disclosures.

## 3 Data and Methodology

### 3.1 Sample Construction

The analysis integrates regulatory filings with market data. Insider transactions are sourced from SEC Form 4 filings (January 2018–December 2024), accessed via SEC EDGAR and parsed to extract transaction dates, prices, and insider roles. I focus on open-market purchases (transaction code “P”) to isolate active bullish signals.

Daily prices, volume, and adjustment factors are obtained from an institutional-grade market data vendor. To ensure point-in-time accuracy, all market capitalization and volume filters are applied using data available as of the transaction date. The sample is restricted to the microcap segment, defined here as issuers with market capitalizations between $30 million and $500 million. This range aligns with common industry definitions for the lower bound of investable equities where liquidity constraints and information asymmetry are most pronounced.

Data processing involves the following steps to ensure reproducibility:

1. 1.

   Ticker Matching: Parsed CUSIPs from Form 4 are mapped to permanent identifiers to handle ticker changes and mergers.
2. 2.

   Filters: I exclude filings with reporting lags exceeding 90 days to mitigate potential data entry errors or backdating anomalies. Transactions with value below $5,000 are removed to filter out noise and focus on economically motivated trades.
3. 3.

   Universe: The final investable universe requires a minimum average daily dollar volume (ADDV) of $200,000 over the trailing 30 days.

The final processed dataset contains 17,237 transactions across 1,343 distinct issuers. Code for data parsing and feature generation is available upon request.

### 3.2 Feature Construction

Features fall into four categories. Insider characteristics: An ordinal title score assigns CEO=5, CFO=4, COO=3, Director=2, Other=1. Transaction value in dollars is included directly. Trading history: A binary indicator flags whether the insider’s current purchase is the first in the preceding 12 months. The ratio of current transaction value to the insider’s historical average captures deviation from baseline behavior. Market conditions: Price deviation is defined as the percentage change from transaction price to disclosure price. Distance from the 52-week high and low, month-to-date return, 30-day annualized volatility, market capitalization, and average daily volume at filing are included. Sector: A binary indicator for biotechnology and pharmaceutical issuers.

### 3.3 Target Definition and Information Set

To strictly prevent look-ahead bias, the information set ℐt\mathcal{I}\_{t} at the time of prediction includes only data publicly available at the moment of disclosure. For a Form 4 filed on date tt, input features (e.g., volatility, distance from 52-week high) are calculated using closing prices up to tt.

The target variable represents the subsequent market response. I define the event window starting from t+1t+1 (the first trading day following disclosure) to ensure tradeability. The binary target is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | y=𝟏​{C​A​R[1,30]>10%}y=\mathbf{1}\{CAR\_{[1,30]}>10\%\} |  | (1) |

where C​A​R[1,30]CAR\_{[1,30]} denotes the cumulative abnormal return from trading day t+1t+1 through t+30t+30. This separation between the feature calculation window (tt and prior) and the target window (t+1t+1 forward) ensures that the model predicts future returns using only past information.

Abnormal returns are computed relative to the Fama-French three-factor model (Fama & French, [1993](https://arxiv.org/html/2602.06198v1#bib.bib6)):

|  |  |  |  |
| --- | --- | --- | --- |
|  | A​Rt=Rt−α^−β^M​K​T​(RM​K​T,t−Rf)−β^S​M​B⋅S​M​Bt−β^H​M​L⋅H​M​LtAR\_{t}=R\_{t}-\hat{\alpha}-\hat{\beta}\_{MKT}(R\_{MKT,t}-R\_{f})-\hat{\beta}\_{SMB}\cdot SMB\_{t}-\hat{\beta}\_{HML}\cdot HML\_{t} |  | (2) |

with factor loadings estimated over the 252 trading days preceding the event window. The 10% threshold is chosen to identify economically meaningful outperformance, corresponding to approximately the top decile of the empirical distribution of C​A​R[1,30]CAR\_{[1,30]} in the event sample.

### 3.4 Model and Evaluation

The primary model is gradient boosting (XGBoost), selected for its strong performance on tabular data with mixed feature types (Chen & Guestrin, [2016](https://arxiv.org/html/2602.06198v1#bib.bib3)). Logistic regression and random forest serve as baselines.

The sample is split temporally: 2018–2022 for training (11,609 observations), 2023 for validation (2,982), and 2024 for testing (2,646). Hyperparameters are tuned via time-series cross-validation on the training set to prevent look-ahead bias. Due to class imbalance, the classification threshold is optimized on the validation set to maximize F1 score, yielding an optimal threshold of 0.20.

Table 1: Sample Composition

| Statistic | Value |
| --- | --- |
| Total transactions | 17,237 |
| Unique issuers | 1,343 |
| Unique insiders | 5,421 |
| Positive class rate | 27.0% |
| Median transaction value | $27,000 |

## 4 Results

### 4.1 Classification Performance

Table 2 reports test set performance. XGBoost achieves an AUC of 0.70. While Random Forest shows comparable global AUC (0.69) and Logistic Regression performs slightly lower (0.67), XGBoost is selected as the primary model due to its superior handling of non-linear feature interactions and performance at the actionable decision threshold.

At the default threshold of 0.5, XGBoost is overly conservative with a recall of 0.17. The optimized threshold of 0.20 raises recall to 0.69 while maintaining precision of 0.38, yielding an F1 score of 0.49.

![Refer to caption](figures/roc_curves.png)


Figure 1: ROC curves for classification models on 2024 test set. XGBoost (AUC = 0.70) and Random Forest (AUC = 0.69) exhibit similar overall predictive power, slightly outperforming Logistic Regression (AUC = 0.67).




Table 2: Test Set Performance (2024, n=2,646)

The gap between validation AUC (0.74) and test AUC (0.70) indicates some temporal degradation, possibly reflecting regime differences between 2023 and 2024.

### 4.2 Feature Importance

Figure [2](https://arxiv.org/html/2602.06198v1#S4.F2 "Figure 2 ‣ 4.2 Feature Importance ‣ 4 Results ‣ 3.4 Model and Evaluation ‣ 3 Data and Methodology ‣ Insider Purchase Signals in Microcap Equities: Gradient Boosting Detection of Abnormal Returns") presents feature importance from the XGBoost model. Distance from the 52-week high dominates, with importance of 0.360—more than four times the next feature.

![Refer to caption](figures/feature_importance.png)


Figure 2: Feature importance from XGBoost model (measured by average gain). The distance from 52-week high accounts for 36% of the total predictive contribution, substantially exceeding all other features.

Month-to-date return (0.081), 30-day volatility (0.072), and market capitalization at filing (0.066) follow. Insider identity features (title score, transaction value) rank lower, suggesting that market conditions at disclosure carry more predictive weight than who is trading.

Table 3: Feature Importance (XGBoost)

### 4.3 Momentum in Price Deviation

Stratifying by price deviation at disclosure reveals a monotonic relationship with subsequent returns. Transactions where price fell between trade and disclosure yield mean CAR of 2.3% and outperformance probability of 22.6%. At the opposite extreme, transactions disclosed after price increases exceeding 10% yield mean CAR of 6.3% and outperformance probability of 36.7%.

Table 4: Abnormal Returns by Price Deviation at Disclosure

The difference between the lowest and highest buckets is statistically significant (t = −-5.13, p << 0.001). Winsorized means and medians confirm that the pattern is not driven by outliers: the median CAR in the highest bucket is 1.93%, and the winsorized mean is 5.44%. This momentum pattern contradicts the conventional wisdom that high price deviation signals should be avoided due to mean-reversion risk. In microcap stocks, price appreciation at disclosure appears to act as a confirmation signal rather than a warning sign. Statistical tests are based on transaction-level outcomes; clustering by issuer yields similar qualitative conclusions.

### 4.4 Robustness

Alternative return windows (20-day, 60-day) yield qualitatively similar patterns, though predictive power weakens at longer horizons. The model performs better in low-volatility environments (VIX << 20). Sector effects are modest: the biotech indicator has importance of 0.060, ranking 7th.

Figure [3](https://arxiv.org/html/2602.06198v1#S4.F3 "Figure 3 ‣ 4.4 Robustness ‣ 4 Results ‣ 3.4 Model and Evaluation ‣ 3 Data and Methodology ‣ Insider Purchase Signals in Microcap Equities: Gradient Boosting Detection of Abnormal Returns") displays model calibration. The model is reasonably calibrated in the 0.2–0.5 probability range where most predictions fall. The distribution of predicted probabilities concentrates between 0.15 and 0.40, indicating the model avoids extreme predictions.

![Refer to caption](figures/calibration.png)


Figure 3: Model calibration. Left: calibration curve showing actual vs. predicted positive rates. Right: distribution of predicted probabilities.

Figure [4](https://arxiv.org/html/2602.06198v1#S4.F4 "Figure 4 ‣ 4.4 Robustness ‣ 4 Results ‣ 3.4 Model and Evaluation ‣ 3 Data and Methodology ‣ Insider Purchase Signals in Microcap Equities: Gradient Boosting Detection of Abnormal Returns") shows the confusion matrix at the optimized threshold. The model correctly identifies 490 of 709 positive cases (0.69 recall) while generating 808 false positives among 1,937 negative cases (58% specificity).

![Refer to caption](figures/confusion_matrix.png)


Figure 4: Confusion matrix at optimized threshold (0.20).

## 5 Discussion

The prominence of distance-from-52-week-high is consistent with two non-exclusive mechanisms. One is behavioral/valuation: insiders may preferentially buy when prices are depressed relative to a recent reference point, consistent with a “buy low” motive. The other is mechanical: when a stock is far below its prior high, a fixed 10% outperformance threshold may simply be easier to reach over the subsequent window. These channels can be distinguished by future work examining whether the effect remains when the target is defined in risk-adjusted units or when returns are normalized by recent volatility.

The price-deviation result is more informative. Conventional heuristics treat large run-ups between trade and disclosure as a red flag. In this microcap sample, the data point in the opposite direction: purchases disclosed after appreciable price strength are followed by higher abnormal performance. This supports a “slow incorporation” hypothesis: early price movement may mark the start of an adjustment rather than its completion. A simple diagnostic is to compare the effect across liquidity buckets: if slow incorporation is key, the pattern should be strongest in the least liquid names; if selection dominates, the pattern should appear more uniformly across liquidity.

Implementation remains constrained by microcap trading frictions. A $50,000 position can represent a non-trivial share of typical daily volume, implying gradual entry and exposure to price impact. Even assuming a conservative effective spread of 2% and price impact of 1%, the mean CAR of 6.3% in the highest momentum bucket would be reduced to approximately 3.3%, though still positive. This highlights that while the signal is statistically robust, capacity is naturally limited.

Several limitations deserve emphasis. The backtest abstracts from realistic execution costs beyond the simple estimation above. It also does not model information leakage between transaction and disclosure, which may differ across venues and investor types. Finally, the sample spans the COVID-19 period and the subsequent recovery, so the strength of the documented relationships may vary across regimes.

## 6 Conclusion

This paper demonstrates that machine learning classifiers can extract actionable signals from Form 4 filings in the microcap segment, outperforming linear benchmarks in identifying 30-day abnormal returns. While market state variables—specifically distance from the 52-week high—carry the most weight, the relationship between price deviation and subsequent performance challenges conventional wisdom. Contrary to mean-reversion heuristics, I find that insider purchases disclosed into strength are more predictive than those disclosed into weakness.

These results suggest that in informationally sparse environments, price momentum may validate the quality of the insider’s signal rather than erode its value. Future work could fruitfully explore whether this effect persists in shorter intraday windows immediately following disclosure, or whether it reflects a broader interaction between liquidity constraints and information asymmetry.

## References

* Amihud [2002]

  Amihud, Y. (2002). Illiquidity and stock returns: cross-section and time-series effects. Journal of Financial Markets, 5(1), 31-56.
* Chen et al. [2024]

  Chen, L., Pelger, M., & Zhu, J. (2024). Deep learning in asset pricing. Management Science, 70(2), 714-750.
* Chen & Guestrin [2016]

  Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system.
  Proceedings of the 22nd ACM SIGKDD, 785-794.
* Cohen et al. [2012]

  Cohen, L., Malloy, C., & Pomorski, L. (2012). Decoding inside information.
  The Journal of Finance, 67(3), 1009-1043.
* Fama & French [1992]

  Fama, E. F., & French, K. R. (1992).
  The cross-section of expected stock returns. The Journal of Finance, 47(2), 427-465.
* Fama & French [1993]

  Fama, E. F., & French, K. R. (1993). Common risk factors in the returns on stocks and bonds.
  Journal of Financial Economics, 33(1), 3-56.
* Gu et al. [2020]

  Gu, S., Kelly, B., & Xiu, D. (2020).
  Empirical asset pricing via machine learning. The Review of Financial Studies, 33(5), 2223-2273.
* Jaffe [1974]

  Jaffe, J. F. (1974).
  Special information and insider trading. The Journal of Business, 47(3), 410-428.
* Jeng et al. [2003]

  Jeng, L. A., Metrick, A., & Zeckhauser, R. (2003). Estimating the returns to insider trading: A performance-evaluation perspective.
  Review of Economics and Statistics, 85(2), 453-471.
* Lakonishok & Lee [2001]

  Lakonishok, J., & Lee, I. (2001). Are insider trades informative?
  The Review of Financial Studies, 14(1), 79-111.
* SEC [2002]

  Securities and Exchange Commission. (2002).
  Final Rule: Ownership Reports and Trading by Officers, Directors, and Principal Security Holders. Release No. 34-46421.
* Seyhun [1986]

  Seyhun, H. N. (1986).
  Insiders’ profits, costs of trading, and market efficiency. Journal of Financial Economics, 16(2), 189-212.