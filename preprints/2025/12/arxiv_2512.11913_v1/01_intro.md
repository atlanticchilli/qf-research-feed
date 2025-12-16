---
authors:
- Chorok Lee
doc_id: arxiv:2512.11913v1
family_id: arxiv:2512.11913
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Not All Factors Crowd Equally: Modeling, Measuring, and Trading on Alpha Decay'
url_abs: http://arxiv.org/abs/2512.11913v1
url_html: https://arxiv.org/html/2512.11913v1
venue: arXiv q-fin
version: 1
year: 2025
---


Chorok Lee
  
KAIST
  
choroklee@kaist.ac.kr

###### Abstract

We derive a specific functional form for factor alpha decay—hyperbolic decay α​(t)=K/(1+λ​t)\alpha(t)=K/(1+\lambda t)—from a game-theoretic equilibrium model, and test it against linear and exponential alternatives. Using eight Fama-French factors (1963–2024), we find: (1) Hyperbolic decay fits mechanical factors. Momentum exhibits clear hyperbolic decay (R2=0.65R^{2}=0.65), outperforming linear (0.51) and exponential (0.61) baselines—validating the equilibrium foundation. (2) Not all factors crowd equally. Mechanical factors (momentum, reversal) fit the model; judgment-based factors (value, quality) do not—consistent with a signal-ambiguity taxonomy paralleling Hua and Sun’s “barriers to entry.” (3) Crowding accelerated post-2015. Out-of-sample, the model over-predicts remaining alpha (0.30 vs. 0.15), correlating with factor ETF growth (ρ=−0.63\rho=-0.63). (4) Average returns are efficiently priced. Crowding-based factor selection fails to generate alpha (Sharpe: 0.22 vs. 0.39 factor momentum benchmark). (5) Crowding predicts tail risk. Out-of-sample (2001–2024), crowded reversal factors show 1.7–1.8×\times higher crash probability (bottom decile returns), while crowded momentum shows lower crash risk (0.38×\times, p=0.006p=0.006). Our findings extend equilibrium crowding models (DeMiguel et al.) to temporal dynamics and show that crowding predicts crashes, not means—useful for risk management, not alpha generation.

Keywords: factor investing, alpha decay, crowding, game theory, market efficiency

## 1 Introduction

The momentum factor returned approximately 10% annually in the 1990s. Today, that figure is closer to 2%. What happened?

A growing body of evidence documents the decay of factor premia following academic publication. McLean and Pontiff (McLean and Pontiff, [2016](https://arxiv.org/html/2512.11913v1#bib.bib1)) found that approximately 50% of anomaly alpha disappears post-publication, consistent with investors learning from research and arbitraging away returns. Yet while the existence of decay is well-established, its mechanics remain poorly understood. Do all factors decay similarly? Can we predict the rate of decay? And crucially—can we profit from this knowledge?

We address these questions through a game-theoretic model of factor crowding. The core insight is simple: when NN agents discover and trade the same profitable signal, they compete for a fixed “alpha capacity” KK. In Nash equilibrium, each agent earns αi=K/N\alpha\_{i}=K/N. As agents discover the signal over time, aggregate alpha decays hyperbolically:

|  |  |  |  |
| --- | --- | --- | --- |
|  | α​(t)=K1+λ​t\alpha(t)=\frac{K}{1+\lambda t} |  | (1) |

where λ\lambda is the rate of strategy discovery.

This model yields four testable predictions, which we evaluate using data on eight Fama-French factors from 1963–2024:

1. Hyperbolic decay fits better than alternatives. For momentum, our model achieves R2=0.65R^{2}=0.65, outperforming linear decay (0.51) and exponential decay (0.61). The improvement validates the game-theoretic foundation.

2. Not all factors crowd equally. The model fits “mechanical” factors—those with unambiguous, easily replicated signals like momentum (“buy recent winners”)—but fails for “judgment” factors like value, where the signal (“what is cheap?”) admits multiple interpretations.

3. Crowding accelerated post-2015. Training on 1995–2015 and predicting 2016–2024, the model over-estimates remaining alpha (0.30 predicted vs. 0.15 actual). This over-prediction correlates with factor ETF volume growth (ρ=−0.63\rho=-0.63), suggesting that democratization of factor investing through ETFs accelerated crowding beyond historical rates.

4. Crowding is detectable but efficiently priced. We construct a real-time crowding signal based on prediction residuals. While the signal correctly identifies that 7 of 8 factors are systematically crowded, factor timing strategies based on the signal fail to outperform naive benchmarks (Sharpe: 0.22 vs. 0.39 for factor momentum).

This last finding—a negative result—is itself informative. It suggests that crowding, once established, is incorporated into prices quickly enough that public signals offer no trading advantage. The signal’s value lies in regime detection (identifying when factor investing faces headwinds) rather than alpha generation.

Our contributions are: (1) a game-theoretic model that explains why alpha decays and predicts its functional form; (2) empirical validation distinguishing mechanical from judgment factors; (3) evidence that post-2015 crowding acceleration correlates with ETF growth; and (4) an honest evaluation showing that crowding signals, while informative, do not generate trading alpha.

## 2 Related Work

Post-publication decay. McLean and Pontiff (McLean and Pontiff, [2016](https://arxiv.org/html/2512.11913v1#bib.bib1)) documented that returns to 97 characteristics decline by approximately 58% after publication. Falck et al. (Falck et al., [2021](https://arxiv.org/html/2512.11913v1#bib.bib6)) extend this to 72 factors, finding publication year explains 30% of Sharpe decay variance. These papers document that decay happens; we model why and derive a specific functional form.

Game-theoretic models. DeMiguel et al. (DeMiguel et al., [2021](https://arxiv.org/html/2512.11913v1#bib.bib2)) develop an equilibrium model where competition erodes factor profits, showing profits scale with the number of investors. Our work differs in focus: they study cross-sectional equilibrium (how factors interact); we study temporal dynamics (how alpha decays over time) and derive a testable decay functional form they do not consider.

Crowding and predictability. Kang et al. (Kang et al., [2021](https://arxiv.org/html/2512.11913v1#bib.bib3)) show that CFTC position-based crowding measures predict commodity factor returns. We test whether model-implied crowding predicts equity factor returns and find it does not—suggesting market structure differences between commodities (with observable positioning) and equities (where crowding must be inferred).

Heterogeneous crowding. Hua and Sun (Hua and Sun, [2024](https://arxiv.org/html/2512.11913v1#bib.bib4)) study heterogeneous crowding vulnerability, attributing differences to “barriers to entry.” Our mechanical-judgment taxonomy parallels this intuition but operationalizes it through model fit: mechanical factors exhibit hyperbolic decay; judgment factors do not.

Crowding and tail risk. Barroso, Edelen, and Karehnke (Barroso et al., [2022](https://arxiv.org/html/2512.11913v1#bib.bib5)) find that momentum crowding is associated with lower crash risk, concluding that “crowding does not generate tail risk when arbitrageurs rationally condition on feedback.” We confirm their momentum result but reveal factor-specific heterogeneity: reversal factors show the opposite pattern, with crowding predicting elevated crash probability.

Our contribution. We make three contributions: (1) derive hyperbolic decay α​(t)=K/(1+λ​t)\alpha(t)=K/(1+\lambda t) from game-theoretic equilibrium, outperforming linear and exponential alternatives for mechanical factors; (2) show that average returns are efficiently priced—crowding-based factor selection fails; (3) demonstrate heterogeneous tail risk across factor types, extending Barroso et al.’s momentum-only analysis to show that reversal factors exhibit opposite tail risk dynamics.

## 3 Model

### 3.1 Setup

Consider N​(t)N(t) agents who have discovered a profitable signal at time tt. Each agent is small relative to the market but collectively they affect prices through market impact.

Let the signal predict excess return rr with edge α0\alpha\_{0} when undiscovered. Total alpha capacity is K=α0/2K=\alpha\_{0}/2. Agents trade quantity qiq\_{i} and face linear price impact Δ​P=γ​∑iqi\Delta P=\gamma\sum\_{i}q\_{i}, where γ\gamma is Kyle’s lambda.

### 3.2 Single-Period Nash Equilibrium

Each agent maximizes expected profit:

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxqi⁡𝔼​[qi⋅(r−γ​∑j=1Nqj)]\max\_{q\_{i}}\mathbb{E}\left[q\_{i}\cdot\left(r-\gamma\sum\_{j=1}^{N}q\_{j}\right)\right] |  | (2) |

Taking first-order conditions and imposing symmetry (qi=q∗q\_{i}=q^{\*} for all ii):

|  |  |  |  |
| --- | --- | --- | --- |
|  | q∗=α02​γ​Nq^{\*}=\frac{\alpha\_{0}}{2\gamma N} |  | (3) |

Substituting back, equilibrium alpha per agent is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | αi=α02​N=KN\alpha\_{i}=\frac{\alpha\_{0}}{2N}=\frac{K}{N} |  | (4) |

Result 1: Alpha per agent decays as 1/N1/N—hyperbolic in the number of discoverers.

### 3.3 Dynamic Model with Entry

Agents discover the signal according to a Poisson process with rate λ\lambda. The expected number at time tt is 𝔼​[N​(t)]=λ​t\mathbb{E}[N(t)]=\lambda t. Substituting into the equilibrium condition:

|  |  |  |  |
| --- | --- | --- | --- |
|  | α​(t)=K1+λ​t\alpha(t)=\frac{K}{1+\lambda t} |  | (5) |

This is our hyperbolic decay model (Equation [1](https://arxiv.org/html/2512.11913v1#S1.E1 "In 1 Introduction ‣ Not All Factors Crowd Equally: Modeling, Measuring, and Trading on Alpha Decay")). The key distinction from exponential decay (K​e−λ​tKe^{-\lambda t}) is that hyperbolic decay is slower initially but has a heavier tail—alpha persists longer but at lower levels.

### 3.4 Why Hyperbolic, Not Exponential?

Table 1: Decay models and their assumptions

| Model | Assumption | Decay Form |
| --- | --- | --- |
| Nash (ours) | Compete for fixed KK | K/(1+λ​t)K/(1+\lambda t) |
| Learning | Price incorporation | K​e−λ​tKe^{-\lambda t} |
| Ad hoc | None | K−b​tK-bt |

The hyperbolic form arises specifically from the 1/N1/N profit-splitting in Nash equilibrium. Alternative assumptions yield different forms (Table [1](https://arxiv.org/html/2512.11913v1#S3.T1 "Table 1 ‣ 3.4 Why Hyperbolic, Not Exponential? ‣ 3 Model ‣ Not All Factors Crowd Equally: Modeling, Measuring, and Trading on Alpha Decay")). We test these alternatives empirically.

## 4 Empirical Analysis

### 4.1 Data

We use monthly returns for eight factors from Kenneth French’s data library (1963–2024): market (MKT), size (SMB), value (HML), profitability (RMW), investment (CMA), momentum (Mom), short-term reversal (ST\_Rev), and long-term reversal (LT\_Rev). Our alpha proxy is the rolling 36-month Sharpe ratio.

### 4.2 Model Fit and Baseline Comparison

Table [2](https://arxiv.org/html/2512.11913v1#S4.T2 "Table 2 ‣ 4.2 Model Fit and Baseline Comparison ‣ 4 Empirical Analysis ‣ Not All Factors Crowd Equally: Modeling, Measuring, and Trading on Alpha Decay") reports R2R^{2} for each model-factor combination, fitting on positive Sharpe observations from 1995–2024.

Table 2: Model comparison: In-sample R2R^{2} (1995–2024). Bold indicates best fit.

| Factor | Hyperbolic | Linear | Exponential |
| --- | --- | --- | --- |
| Mom | 0.65 | 0.51 | 0.61 |
| LT\_Rev | 0.30 | 0.26 | 0.29 |
| ST\_Rev | 0.15 | 0.14 | 0.15 |
| SMB | 0.10 | 0.17 | 0.13 |
| MKT | 0.07 | 0.07 | 0.07 |
| HML | 0.05 | 0.07 | 0.06 |
| RMW | 0.05 | 0.05 | 0.05 |
| CMA | 0.01 | 0.01 | 0.01 |

For momentum, hyperbolic decay achieves R2=0.65R^{2}=0.65, outperforming linear (0.51) by 27% and exponential (0.61) by 7%. Long-term reversal also shows a clear hyperbolic pattern (R2=0.30R^{2}=0.30). However, judgment-based factors (HML, RMW, CMA) show poor fits across all models (R2<0.10R^{2}<0.10).

Figure [1](https://arxiv.org/html/2512.11913v1#S4.F1 "Figure 1 ‣ 4.2 Model Fit and Baseline Comparison ‣ 4 Empirical Analysis ‣ Not All Factors Crowd Equally: Modeling, Measuring, and Trading on Alpha Decay") illustrates this contrast visually. For momentum (left panel), the hyperbolic curve tracks the rolling Sharpe ratio’s decline from ∼\sim1.5 in the mid-1990s to ∼\sim0.25 today. For value (right panel), no model captures the erratic pattern—the factor oscillates without systematic decay.

![Refer to caption](figures/icaif_fig1_model_fit.png)


Figure 1: Model fit comparison: Momentum (mechanical) exhibits clear hyperbolic decay (R2=0.65R^{2}=0.65); Value (judgment) shows no systematic decay pattern (R2=0.05R^{2}=0.05).

### 4.3 Mechanical vs. Judgment Taxonomy

We propose a taxonomy based on signal ambiguity:

Mechanical factors have unambiguous signals:

* •

  Momentum: “Buy stocks with high past returns”
* •

  Reversal: “Buy stocks with low recent returns”

Judgment factors require interpretation:

* •

  Value: “What is cheap?” (book/market? earnings?)
* •

  Quality: “What is quality?” (ROE? accruals?)

The hypothesis is that mechanical factors crowd quickly because the replication path is clear, while judgment factors crowd diffusely because different investors implement different versions.

Figure [2](https://arxiv.org/html/2512.11913v1#S4.F2 "Figure 2 ‣ 4.3 Mechanical vs. Judgment Taxonomy ‣ 4 Empirical Analysis ‣ Not All Factors Crowd Equally: Modeling, Measuring, and Trading on Alpha Decay") shows R2R^{2} by factor type. Mechanical factors achieve mean R2=0.37R^{2}=0.37; judgment factors achieve mean R2=0.04R^{2}=0.04—an order of magnitude lower.

![Refer to caption](figures/icaif_fig3_taxonomy.png)


Figure 2: Model fit by factor type. Mechanical factors fit hyperbolic decay; judgment factors do not.

### 4.4 Out-of-Sample Prediction

We train on 1995–2015 and predict 2016–2024. For momentum:

* •

  Direction: Correct—model predicts continued decay
* •

  Magnitude: Over-predicted (mean 0.30 vs. actual 0.15)
* •

  RMSE: 0.19

The systematic over-prediction is informative. A model trained on 1995–2015 captures that era’s equilibrium decay rate. The over-prediction post-2015 suggests crowding accelerated beyond historical rates.

### 4.5 ETF Correlation

To test whether ETF proliferation explains the acceleration, we correlate the cumulative prediction residual with factor ETF trading volume (2013–2024).

Finding: Pearson ρ=−0.63\rho=-0.63 (p<0.001p<0.001).

The negative correlation indicates that as ETF volume grows, the model increasingly over-predicts remaining alpha (Figure [3](https://arxiv.org/html/2512.11913v1#S4.F3 "Figure 3 ‣ 4.5 ETF Correlation ‣ 4 Empirical Analysis ‣ Not All Factors Crowd Equally: Modeling, Measuring, and Trading on Alpha Decay")).

![Refer to caption](figures/icaif_fig2_etf_correlation.png)


Figure 3: Cumulative residual vs. factor ETF volume. Correlation ρ=−0.63\rho=-0.63 suggests ETF growth accelerated crowding.

## 5 Can We Trade on Crowding?

### 5.1 Signal Construction

We construct a real-time crowding signal:

1. 1.

   Fit hyperbolic model on expanding window (min 120 months)
2. 2.

   Compute predicted Sharpe for current period
3. 3.

   Residual = Actual −- Predicted
4. 4.

   Negative residual ⇒\Rightarrow crowding accelerated

### 5.2 Signal Properties

Across 8 factors (2006–2024):

* •

  Mean residual: −0.41-0.41 (systematic over-prediction)
* •

  7 of 8 factors have negative mean residual
* •

  Only RMW shows slight uncrowding (+0.07+0.07)

### 5.3 Trading Strategies

We test three strategies (Table [3](https://arxiv.org/html/2512.11913v1#S5.T3 "Table 3 ‣ 5.3 Trading Strategies ‣ 5 Can We Trade on Crowding? ‣ Not All Factors Crowd Equally: Modeling, Measuring, and Trading on Alpha Decay")):

Table 3: Strategy performance (2017–2025)

| Strategy | Sharpe |
| --- | --- |
| Factor Momentum | 0.39 |
| Crowding-Timed | 0.22 |
| Equal Weight | 0.17 |

Factor momentum (0.39) outperforms both crowding-timed (0.22) and equal weight (0.17). While crowding-timed marginally beats equal weight, the improvement is economically insignificant and fails to match the simple factor momentum benchmark.

### 5.4 Why Doesn’t the Signal Work?

Three hypotheses:

H1: Contemporaneous, not predictive. The signal tells you factors are crowded but doesn’t predict which will underperform next.

H2: Efficiently priced. Market participants already incorporate crowding information.

H3: Insufficient dispersion. When 7/8 factors show the same signal, there’s no differentiation to exploit.

Our evidence is most consistent with H2—crowding is observable but efficiently priced.

## 6 Utilization: Tail Risk Prediction

If crowding does not predict average returns, what can practitioners do with crowding information? We hypothesize that crowding predicts tail risk—the probability of extreme losses—even when it fails to predict mean returns.

### 6.1 Intuition: The Crowded Exit Problem

When many investors hold the same position, average returns may be efficiently priced. However, in stress scenarios, crowded positions face correlated liquidation—everyone exits simultaneously, amplifying losses. This suggests crowding should predict crash probability, not average returns.

### 6.2 Out-of-Sample Test

We establish thresholds using training data (1980–2000) only:

* •

  Crowding threshold: training-period median residual per factor
* •

  Crash threshold: training-period 10th percentile of returns

We then apply these thresholds to out-of-sample data (2001–2024) and compute crash probabilities conditional on crowding state.

Table 4: Tail risk by crowding state (OOS 2001–2024)

| Factor | P(crash||crowded) | P(crash||uncrowded) | Ratio | p-value |
| --- | --- | --- | --- | --- |
| ST\_Rev | 16.9% | 9.2% | 1.84 | 0.078 |
| MKT | 15.0% | 8.9% | 1.68 | 0.215 |
| LT\_Rev | 19.4% | 11.8% | 1.65 | 0.095 |
| CMA | 8.6% | 6.7% | 1.30 | 0.677 |
| SMB | 8.0% | 7.3% | 1.10 | 0.773 |
| Mom | 10.9% | 28.2% | 0.38 | 0.006 |

### 6.3 Heterogeneous Tail Risk

The results reveal factor-specific patterns that reflect the underlying economic mechanisms:

Reversal factors (ST\_Rev, LT\_Rev) show elevated crash risk when crowded (1.65–1.84×\times). The mechanism: reversal strategies bet on mean reversion—buying recent losers, selling recent winners. When many investors crowd into this contrarian bet, they are collectively positioned against the prevailing trend. If the trend continues rather than reverses, all contrarian positions lose simultaneously, generating a crash. Crowded reversal represents coordinated wrong-way risk.

Momentum shows the opposite pattern: crowded momentum has lower crash probability (0.38×\times, p=0.006p=0.006). The mechanism: momentum strategies ride existing trends—buying recent winners. Crowded momentum means many investors are reinforcing the trend, which tends to sustain rather than reverse it. Here, crowding is a sign of trend strength, not vulnerability. This confirms Barroso et al.’s (Barroso et al., [2022](https://arxiv.org/html/2512.11913v1#bib.bib5)) finding that momentum crowding does not generate tail risk.

Key insight: The tail risk relationship depends on whether the strategy follows or fights the trend:

* •

  Trend-following (momentum): Crowding confirms trend strength →\rightarrow lower crash risk
* •

  Mean-reverting (reversal): Crowding bets against trend →\rightarrow higher crash risk if trend continues

Pooled result: Across all factors, crowded states show 18% higher crash probability (13.4% vs. 11.3%). Five of eight factors show ratio >1>1.

### 6.4 Implications

Crowding predicts tail risk, not average returns:

* •

  Position sizing: Reduce exposure to crowded reversal factors
* •

  Stop-losses: Tighter thresholds on crowded positions
* •

  Factor-specific: Momentum crowding is benign; reversal crowding is dangerous

This finding reconciles efficient pricing of average returns with actionable risk information—crowding matters for the tails, not the mean.

## 7 Discussion

Implications for practitioners. (1) Mechanical factors crowd fastest—monitor capacity. (2) Abandon crowding-based factor selection—average returns are efficiently priced. (3) Use crowding for tail risk management: reduce exposure to crowded reversal factors, but note that momentum crowding is benign.

Implications for researchers. Our results distinguish between efficient pricing of average returns and predictability of tail risk. This separation—crowding predicts crashes, not means—offers a framework for future work on factor risk management.

Limitations. Only 8 factors (more factors would strengthen results). US equities only. Tail risk significance is marginal for individual factors (p≈0.08p\approx 0.08–0.100.10) though directionally consistent (5/8 factors). Momentum’s opposite pattern requires further investigation.

## 8 Conclusion

We developed a game-theoretic model of factor crowding that explains why alpha decays, predicts its functional form, and distinguishes mechanical from judgment factors. The model fits momentum well (R2=0.65R^{2}=0.65) and reveals accelerated crowding post-2015 correlating with ETF growth.

Our central finding: crowding predicts tail risk, not average returns. Cross-sectional factor timing fails—average returns are efficiently priced. However, out-of-sample (2001–2024), crowded reversal factors show 1.7–1.8×\times higher crash probability, while crowded momentum shows lower crash risk (0.38×\times).

The key insight: crowding is tail risk information, not return information. It tells you about crash probability, not expected returns—and this relationship is factor-specific.

For practitioners: use crowding for position sizing and stop-loss calibration on reversal factors; momentum crowding is benign. For researchers: the separation between efficiently priced means and predictable tails offers a framework for factor risk management.

> “Crowding doesn’t tell you where the market is going. It tells you how hard you’ll hit the ground if it falls.”

## References

* McLean and Pontiff [2016]

  R. D. McLean and J. Pontiff.
  Does academic research destroy stock return predictability?
  Journal of Finance, 71(1):5–32, 2016.
* DeMiguel et al. [2021]

  V. DeMiguel, A. Martin-Utrera, and R. Uppal.
  What alleviates crowding in factor investing?
  Journal of Finance, forthcoming, 2021.
* Kang et al. [2021]

  W. Kang, K. G. Rouwenhorst, and K. Tang.
  Crowding and factor returns.
  Working paper, Yale School of Management, 2021.
* Hua and Sun [2024]

  R. Hua and C. Sun.
  Dynamics of factor crowding.
  Working paper, SSRN 5023380, 2024.
* Barroso et al. [2022]

  P. Barroso, R. M. Edelen, and P. Karehnke.
  Crowding and tail risk in momentum returns.
  Journal of Financial and Quantitative Analysis, 57(4):1313–1342, 2022.
* Falck et al. [2021]

  A. Falck, A. Rej, and D. Thesmar.
  Why and how systematic strategies decay.
  CFM Working Paper, 2021.
* Kyle [1985]

  A. S. Kyle.
  Continuous auctions and insider trading.
  Econometrica, 53(6):1315–1335, 1985.
* Arnott et al. [2016]

  R. Arnott, N. Beck, V. Kalesnik, and J. West.
  How can smart beta go horribly wrong?
  Research Affiliates Working Paper, 2016.
* Jegadeesh and Titman [1993]

  N. Jegadeesh and S. Titman.
  Returns to buying winners and selling losers.
  Journal of Finance, 48(1):65–91, 1993.
* Fama and French [1993]

  E. F. Fama and K. R. French.
  Common risk factors in the returns on stocks and bonds.
  Journal of Financial Economics, 33(1):3–56, 1993.