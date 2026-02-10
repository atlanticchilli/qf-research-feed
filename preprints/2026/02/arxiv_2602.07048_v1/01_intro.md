---
authors:
- Sumin Kim
- Minjae Kim
- Jihoon Kwon
- Yoon Kim
- Nicole Kagan
- Joo Won Lee
- Oscar Levy
- Alejandro Lopez-Lira
- Yongjae Lee
- Chanyeol Choi
doc_id: arxiv:2602.07048v1
family_id: arxiv:2602.07048
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction
  Markets'
url_abs: http://arxiv.org/abs/2602.07048v1
url_html: https://arxiv.org/html/2602.07048v1
venue: arXiv q-fin
version: 1
year: 2026
---


Sumin Kim1,∗,
Minjae Kim1,∗,
Jihoon Kwon1,∗,
Yoon Kim2,
Nicole Kagan3,
  
Joo Won Lee4,
Oscar Levy5,
Alejandro Lopez-Lira6,
Yongjae Lee7,
Chanyeol Choi1,∗∗
  
  
1LinqAlpha  2Massachusetts Institute of Technology  3Kalshi  
  
4Arrowpoint Investment Partners  5University of California, Berkeley 
  
6University of Florida 7UNIST
  
∗Equal Contribution.  ∗∗Corresponding author

###### Abstract

Prediction markets provide a unique setting where event-level time series are directly tied to natural-language descriptions, yet discovering robust lead–lag relationships remains challenging due to spurious statistical correlations.
We propose a hybrid two-stage causal screener to address this challenge: (i) a statistical stage that uses Granger causality to identify candidate leader–follower pairs from market-implied probability time series, and (ii) an LLM-based semantic stage that re-ranks these candidates by assessing whether the proposed direction admits a plausible economic transmission mechanism based on event descriptions.
Because causal ground truth is unobserved, we evaluate the ranked pairs using a fixed, signal-triggered trading protocol that maps relationship quality into realized profit and loss (PnL).
On Kalshi Economics markets, our hybrid approach consistently outperforms the statistical baseline.
Across rolling evaluations, the win rate increases from 51.4% to 54.5%.
Crucially, the average magnitude of losing trades decreases substantially from $\mathdollar649 to $\mathdollar347.
This reduction is driven by the LLM’s ability to filter out statistically fragile links that are prone to large losses, rather than relying on rare gains.
These improvements remain stable across different trading configurations, indicating that the gains are not driven by specific parameter choices.
Overall, the results suggest that LLMs function as *semantic risk managers* on top of statistical discovery, prioritizing lead–lag relationships that generalize under changing market conditions.

## 1 Introduction

Real-world events rarely occur in isolation; information about one event
often changes expectations about what happens next.
For example, an inflation surprise can raise expectations of tighter
monetary policy.
These dependencies often manifest as *lead–lag* structure, where
movement in one event systematically precedes movement in another
(Bennett et al., [2022](https://arxiv.org/html/2602.07048v1#bib.bib1 "Lead–lag detection and network clustering for multivariate time series with an application to the us equity market")).

Identifying such structure from observational time series remains
challenging in practice.
Traditional statistical methods such as Granger causality can detect
directional predictability, but the resulting relationships are often
unstable over time and may not reflect meaningful underlying mechanisms
(Rossi and Wang, [2019](https://arxiv.org/html/2602.07048v1#bib.bib9 "Vector autoregressive-based granger causality tests in the presence of instabilities"); Phillips, [1986](https://arxiv.org/html/2602.07048v1#bib.bib10 "Understanding spurious regressions in econometrics")).
In large-scale settings, statistically significant lead–lag links
frequently fail to generalize out of sample and can induce substantial
losses when used in downstream decision-making.

Meanwhile, large language models (LLMs) have shown strong performance in
time-series forecasting tasks, including predicting future trajectories
from noisy observations (Gruver et al., [2023](https://arxiv.org/html/2602.07048v1#bib.bib18 "Large language models are zero-shot time series forecasters"); Jin et al., [2024](https://arxiv.org/html/2602.07048v1#bib.bib19 "Time-llm: time series forecasting by reprogramming large language models")).
However, these approaches typically focus on individual time series and
do not address whether relationships *between* events are
meaningful or robust.
This raises a distinct question:
*can LLMs help distinguish mechanistically plausible inter-event
relationships from brittle statistical correlations?*

Our key idea is to use LLMs as
*semantic filters* that evaluate the plausibility of statistically
identified lead–lag relationships.
We study this question in a prediction-market setting, where event-level
time series continue to update over time and relationships can be
evaluated on future, unseen periods under changing market conditions.

We implement a two-stage framework.
First, we apply Granger causality to identify candidate
leader–follower event pairs from market-implied probability time series(Statistical Approach).
Second, we use an LLM to re-rank these candidates based solely on the
events’ natural-language descriptions, prioritizing relationships that
admit a plausible real-world mechanism(Hybrid Approach).

Across 18 rolling evaluations on Kalshi Economics markets, LLM-based
semantic filtering consistently improves trading performance relative to
Granger screening alone.
At a 7-day holding horizon, total PnL more than doubles, driven mainly by a pronounced reduction in downside
risk.
These results suggest that LLMs act as robustness filters on top of
statistical discovery, helping to exclude fragile lead–lag relationships
that fail under changing market conditions.

## 2 Related Work

#### Limits of statistical significance in lead–lag discovery.

Lead–lag patterns, in which movements in one time series appear to precede those in another, are widely documented in economics and finance (Lo and MacKinlay, [1990](https://arxiv.org/html/2602.07048v1#bib.bib4 "An econometric analysis of nonsynchronous trading"); Hasbrouck, [1995](https://arxiv.org/html/2602.07048v1#bib.bib5 "One security, many markets: determining the contributions to price discovery")).
Motivated by these empirical regularities, a large body of work seeks to formalize directional relationships using statistical discovery tools such as Granger causality and related predictive tests (Granger, [1969](https://arxiv.org/html/2602.07048v1#bib.bib7 "Investigating causal relations by econometric models and cross-spectral methods"); Kinnear and Mazumdar, [2023](https://arxiv.org/html/2602.07048v1#bib.bib12 "Exact recovery of granger causality graphs with unconditional pairwise tests"); Chaudhry et al., [2017](https://arxiv.org/html/2602.07048v1#bib.bib3 "Uncertainty assessment and false discovery rate control in high-dimensional granger causal inference")).

However, even when statistically significant, many discovered lead–lag relationships remain fundamentally ambiguous and limited.
In large-scale settings, pairwise screening inevitably produces links that survive selection purely by chance, a concern long emphasized in the data-snooping and multiple-testing literature (Sullivan et al., [1999](https://arxiv.org/html/2602.07048v1#bib.bib11 "Data-snooping, technical trading rule performance, and the bootstrap")).
These issues are further exacerbated when relationships evolve over time or exhibit structural breaks, leading to instability in Granger-causal links across samples (Ventosa-Santaulària and Vera-Valdés, [2008](https://arxiv.org/html/2602.07048v1#bib.bib8 "Granger-causality in the presence of structural breaks"); Rossi and Wang, [2019](https://arxiv.org/html/2602.07048v1#bib.bib9 "Vector autoregressive-based granger causality tests in the presence of instabilities"); Phillips, [1986](https://arxiv.org/html/2602.07048v1#bib.bib10 "Understanding spurious regressions in econometrics")).
As a result, statistical significance alone provides limited guidance for distinguishing mechanistically meaningful inter-event relationships from brittle correlations.

To assess robustness, discovered relationships are therefore often evaluated using out-of-sample predictive performance or rolling evaluation schemes (Diebold and Mariano, [2002](https://arxiv.org/html/2602.07048v1#bib.bib13 "Comparing predictive accuracy"); Rossi, [2021](https://arxiv.org/html/2602.07048v1#bib.bib14 "Forecasting in the presence of instabilities: how we know whether models predict well and how to improve them")).
Yet even when validated out of sample, such evaluations provide limited guidance about whether an identified lead–lag direction corresponds to a coherent real-world transmission mechanism.

#### Semantic evaluation with LLMs and event-based settings.

Recent work has explored the use of large language models (LLMs) beyond traditional language tasks, including evaluating explanations, relationships, and counterfactuals expressed in natural language (Zheng et al., [2023](https://arxiv.org/html/2602.07048v1#bib.bib20 "Judging llm-as-a-judge with mt-bench and chatbot arena"); Yang et al., [2024](https://arxiv.org/html/2602.07048v1#bib.bib21 "A critical review of causal reasoning benchmarks for large language models"); Wang, [2024](https://arxiv.org/html/2602.07048v1#bib.bib22 "Causalbench: a comprehensive benchmark for evaluating causal reasoning capabilities of large language models")).
In these settings, LLMs are not used to infer causal structure from data, but rather to assess the coherence or plausibility of candidate relationships.
This perspective is particularly relevant for lead–lag analysis, where temporal ordering alone is insufficient to establish whether a relationship admits a meaningful real-world transmission mechanism.

Prediction markets provide a natural platform for this type of evaluation.
Each contract corresponds to a clearly defined event described in natural language and yields a time series of market-implied probabilities reflecting collective expectations (Wolfers and Zitzewitz, [2004](https://arxiv.org/html/2602.07048v1#bib.bib6 "Prediction markets"); Berg et al., [2008](https://arxiv.org/html/2602.07048v1#bib.bib2 "Prediction market accuracy in the long run")).
This structure enables the study of inter-event relationships while allowing discovered dependencies to be evaluated on future, unseen periods under changing market conditions.

## 3 Background

This section introduces the key concepts and notation underlying our
analysis of directional relationships between event-level time series.
Our objective is to study directional lead–lag relationships between event-level time series and establish a framework for evaluating their predictive relevance.

We formally define directional lead–lag
relationships in Section. [3.1](https://arxiv.org/html/2602.07048v1#S3.SS1 "3.1 Directional lead–lag relationships ‣ 3 Background ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets").
Section [3.2](https://arxiv.org/html/2602.07048v1#S3.SS2 "3.2 Time-series representation of prediction-market prices ‣ 3 Background ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets") describes pre-processing procedure of time-series data, and Section [3.3](https://arxiv.org/html/2602.07048v1#S3.SS3 "3.3 Directional predictability via Granger causality ‣ 3 Background ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets") introduces Granger causality as a statistical tool for operationalizing directional predictability.
Finally, Section [3.4](https://arxiv.org/html/2602.07048v1#S3.SS4 "3.4 Sign of co-movement ‣ 3 Background ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets") defines how to annotate discovered lead–lag relationships.

### 3.1 Directional lead–lag relationships

Let {xt}t=1T\{x\_{t}\}\_{t=1}^{T} and {yt}t=1T\{y\_{t}\}\_{t=1}^{T} be two real-valued time series
indexed by time tt.
We say that xx *leads* yy if past values of xtx\_{t} contain predictive
information about future values of yty\_{t} beyond what is contained in the
past of yty\_{t} itself.

Formally, xx leads yy if there exists a forecast horizon h>0h>0 such that

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[yt+h∣x1:t,y1:t]≠𝔼​[yt+h∣y1:t].\mathbb{E}\!\left[y\_{t+h}\mid x\_{1:t},y\_{1:t}\right]\neq\mathbb{E}\!\left[y\_{t+h}\mid y\_{1:t}\right]. |  |

This definition is directional and asymmetric: xx leading yy does not
imply that yy leads xx. Throughout this paper, we study ordered event pairs exhibiting directional lead–lag structure—also referred to as leader–follower pairs (L,F)(L,F).

### 3.2 Time-series representation of prediction-market prices

Prediction markets trade contracts whose payoff depends on the
realization of a future event.
For each event ii, the daily YES price forms an event-level time series
that reflects the market’s collective belief about the probability of
that event occurring.

Let pi,t∈[0,100]p\_{i,t}\in[0,100] denote the daily YES price (in percentage
points) of event ii at time tt.
To obtain an unbounded real-valued signal suitable for time-series
analysis, we apply the log-odds transformation

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓi,t=log⁡(pi,t100−pi,t),\ell\_{i,t}=\log\!\left(\frac{p\_{i,t}}{100-p\_{i,t}}\right), |  | (1) |

where ℓi,t∈ℝ\ell\_{i,t}\in\mathbb{R}.

This transformation mitigates boundary effects near 0 and 100100 and
renders price changes approximately additive, which facilitates
statistical modeling.

### 3.3 Directional predictability via Granger causality

To test lead–lag relationships, we require a statistical notion of
directional predictability.
We use Granger causality, which assesses whether incorporating the
lagged history of one series improves prediction of another beyond what
is explained by the target series’ own past.

Let {xt}t=1T\{x\_{t}\}\_{t=1}^{T} and {yt}t=1T\{y\_{t}\}\_{t=1}^{T} be two time series, and let
pp denote the chosen lag length in the autoregressive model.
Granger causality tests are typically formulated under the assumption
that the input series are approximately stationary.
In practice, stationarity is commonly assessed using unit-root tests
such as the Augmented Dickey–Fuller (ADF) test, which evaluates whether
a time series exhibits a unit root (i.e., behaves like a random walk).
When non-stationarity is detected, differencing is a common remedy
(Dickey and Fuller, [1979](https://arxiv.org/html/2602.07048v1#bib.bib15 "Distribution of the estimators for autoregressive time series with a unit root"); Said and Dickey, [1984](https://arxiv.org/html/2602.07048v1#bib.bib16 "Testing for unit roots in autoregressive-moving average models of unknown order"); Hamilton, [2020](https://arxiv.org/html/2602.07048v1#bib.bib17 "Time series analysis")).

A standard approach to testing Granger causality is to use vector
autoregressive (VAR) models, which capture linear dependencies between
multiple time series through their lagged values (Hamilton, [2020](https://arxiv.org/html/2602.07048v1#bib.bib17 "Time series analysis")).
In the bivariate case, yty\_{t} can be modeled with optional lags of xtx\_{t}
as

|  |  |  |  |
| --- | --- | --- | --- |
|  | yt=α0+∑k=1pαk​yt−k+∑k=1pβk​xt−k+εt,y\_{t}=\alpha\_{0}+\sum\_{k=1}^{p}\alpha\_{k}\,y\_{t-k}+\sum\_{k=1}^{p}\beta\_{k}\,x\_{t-k}+\varepsilon\_{t}, |  | (2) |

where εt\varepsilon\_{t} is a mean-zero error term.

The Granger test evaluates the null hypothesis
H0:β1=⋯=βp=0H\_{0}:\beta\_{1}=\cdots=\beta\_{p}=0, corresponding to the absence of directional predictability from xx to yy under lag length pp.
Rejection of H0H\_{0} indicates a lead–lag relationship from xx to yy.
Thus, Granger causality provides a testable proxy for the theoretical lead–lag definition in Section [3.1](https://arxiv.org/html/2602.07048v1#S3.SS1 "3.1 Directional lead–lag relationships ‣ 3 Background ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets").

### 3.4 Sign of co-movement

Beyond temporal direction, lead–lag relationships can be further
characterized by whether the two series tend to move in the same or
opposite directions.
For an ordered lead–lag (leader–follower) pair (L→F)(L\rightarrow F) with corresponding time series (xL,t,xF,t)(x\_{L,t},x\_{F,t}), we define the sign of co-movement as

|  |  |  |  |
| --- | --- | --- | --- |
|  | s=sgn​(corr​(xL,t,xF,t))∈{−1,+1},s=\mathrm{sgn}\!\left(\mathrm{corr}(x\_{L,t},x\_{F,t})\right)\in\{-1,+1\}, |  | (3) |

where corr​(⋅,⋅)\mathrm{corr}(\cdot,\cdot) denotes the Pearson correlation
coefficient. Here, s=+1s=+1 indicates aligned movement and s=−1s=-1 indicates opposing
movement, conditional on the identified lead–lag ordering.
This quantity is purely descriptive and does not imply any causal or structural interpretation.
It indicates whether increases in the leading series tend to be associated
with increases or decreases in the lagging series.

## 4 Methods

Recall that our study aims to assess whether LLMs can distinguish causal relationships that are mechanistically meaningful.
To assess this question, we compare two methods for ranking candidate causal relationships: a purely *statistical* approach, and a *hybrid* approach that applies LLM-based re-ranking on top of the statistical approach.
We evaluate each ranking using the same trading protocol, where investment performance reflects the reliability of the identified causal relationships.

In this section, we introduce the two ranking methods: *statistical* and *hybrid* (Section. [4.1](https://arxiv.org/html/2602.07048v1#S4.SS1 "4.1 Ranking Methods for Candidate Causal Relationships ‣ 4 Methods ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets")), and describe the trading protocol (Section. [4.2](https://arxiv.org/html/2602.07048v1#S4.SS2 "4.2 Trading-Based Evaluation of Ranking Methods ‣ 4 Methods ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets")).

### 4.1 Ranking Methods for Candidate Causal Relationships

![Refer to caption](ICLR_Figures/framework/framework.png)


Figure 1: 
Two-stage framework for leader–follower pair discovery in prediction markets. Stage 1 produces a candidate set of Top K directed pairs (K=100) ranked by Granger significance, and Stage 2 applies LLM-based semantic re-ranking to select the final Top M portfolio (M=20).

Figure [1](https://arxiv.org/html/2602.07048v1#S4.F1 "Figure 1 ‣ 4.1 Ranking Methods for Candidate Causal Relationships ‣ 4 Methods ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets") summarizes the two-stage causal filtering framework used in this study.
Starting from event-level prediction market price time series, the pipeline consists of
(i) a statistical filtering stage that identifies candidate leader–follower relationships based on time-series evidence,
and (ii) a semantic filtering stage that re-ranks these candidates using an LLM.
The two stages correspond to the *Statistical Approach* and *Hybrid Approach* described below, and both produce ranked lists of directed event pairs that are evaluated using the same trading protocol.

For each event ii, we obtain a daily price time series
𝒫i={pi,t}t=1T\mathcal{P}\_{i}=\{p\_{i,t}\}\_{t=1}^{T}, where pi,tp\_{i,t} denotes the market-implied price at time tt and TT is the length of the observation window.
From 𝒫i\mathcal{P}\_{i}, we construct a stationary market signal
𝒳i={xi,t}t=1T\mathcal{X}\_{i}=\{x\_{i,t}\}\_{t=1}^{T} by transforming prices into log-odds. Standard stationarity preprocessing is applied prior to Granger testing.

#### Statistical Approach.

Given a pair of events (i,j)(i,j), the statistical approach aims to determine whether there exists a directional lead–lag relationship between the two events based *purely on time-series evidence*.
To this end, we apply Granger causality tests to the stationary market series constructed from their daily price data.

For each unordered event pair {i,j}\{i,j\}, we evaluate both possible causal
directions, (i→j)(i\rightarrow j) and (j→i)(j\rightarrow i).
In each direction, we estimate vector autoregressive (VAR) models over multiple lag lengths and assess whether the lagged history of the candidate leader provides incremental predictive power for the follower beyond its own past.

We retain the direction exhibiting stronger statistical evidence of
directional predictability as the candidate causal relationship for the
event pair.
Finally, all candidate relationships are ranked by their statistical
strength, yielding an ordered list of directed leader–follower pairs
from strongest to weakest evidence of Granger-based predictability.

#### Hybrid Approach.

The hybrid approach takes as its starting point the set of candidate causal relationships identified by the statistical approach.
The role of the LLM is not to discover new relationships, but to re-rank these statistically validated candidates based on semantic and mechanism-level plausibility.
In doing so, the approach preserves statistical validity while adjusting priorities to favor relationships that have coherent economic interpretations.

Specifically, for each directed event pair retained by the statistical approach, we prompt a LLM with the event titles and descriptions and ask whether a plausible economic mechanism exists by which movement in the leader could precede movement in the follower.
The model evaluates the semantic coherence of the proposed causal direction and assigns a plausibility score, with higher scores indicating stronger mechanism-level support.

We then use these plausibility scores to re-rank the statistically screened candidate relationships.
The final hybrid ranking thus preserves the statistical validity ensured by Granger causality while prioritizing relationships that are also supported by coherent economic reasoning.

### 4.2 Trading-Based Evaluation of Ranking Methods

![Refer to caption](ICLR_Figures/trade/trade.png)


Figure 2: 
Signal-triggered trading protocol used to evaluate ranked lead-lag relationships from Figure [1](https://arxiv.org/html/2602.07048v1#S4.F1 "Figure 1 ‣ 4.1 Ranking Methods for Candidate Causal Relationships ‣ 4 Methods ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets"): leader price moves trigger follower trades, with direction determined by the Granger-induced trade sign and out-of-sample PnL used to evaluate the ranked pair list.

Since the ground truth of causal relationships is not directly observable, evaluating the quality of different relationship rankings is inherently challenging. To address this issue, we evaluate the ranking approaches based on trading performance.
The trading rule is intentionally designed to be simple and signal-driven: when a sufficiently large price movement occurs in a leader event, the strategy mechanically follows the corresponding follower.
Therefore, differences in realized trading performance can be attributed to differences in the quality of the underlying causal rankings. Figure [2](https://arxiv.org/html/2602.07048v1#S4.F2 "Figure 2 ‣ 4.2 Trading-Based Evaluation of Ranking Methods ‣ 4 Methods ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets") illustrates the resulting signal-based trade lifecycle, which we detail step by step below.

#### Step 1: leader-based trigger

Consider a directed event pair (L,F)(L,F), where LL denotes the leader event and FF the corresponding follower as identified by a causal ranking.
At each time tt, we monitor the daily price movement of the leader event and trigger a trading signal when the magnitude of the price change exceeds a predefined threshold. Formally, let pL,tp\_{L,t} denote the market-implied price (in percent) of the leader event at time tt. We define the one-day relative price change as
rL,t≜(pL,t−pL,t−1)/pL,t−1r\_{L,t}\triangleq(p\_{L,t}-p\_{L,t-1})/p\_{L,t-1}.
A trading signal is generated if |rL,t|>θ|r\_{L,t}|>\theta,
where θ\theta is a fixed threshold in decimal form.

#### Step 2: Follower Entry.

When a trading signal is generated for a leader–follower pair (L,F)(L,F) at time tt, we enter a position in the follower event at time t+1t+1.
We define the *Granger-induced trade direction* as

|  |  |  |
| --- | --- | --- |
|  | dt=sign​(rL,t)×s​(L→F),d\_{t}=\mathrm{sign}(r\_{L,t})\times s(L\rightarrow F), |  |

where s​(L→F)s(L\rightarrow F) is the sign of the identified Granger relationship.
If dt=+1d\_{t}=+1, we take exposure to an increase in the follower event probability (buy YES shares), and if dt=−1d\_{t}=-1, we take exposure to a decrease in the follower event probability (sell YES shares).
This construction follows directly from the lead–lag interpretation of the Granger sign described in Section [3.1](https://arxiv.org/html/2602.07048v1#S3.SS1 "3.1 Directional lead–lag relationships ‣ 3 Background ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets").

#### Step 3: Holding Period and Exit.

Once entered, the follower position is held for a fixed horizon of hh days and is exited mechanically at time t+h+1t+h+1.
The realized profit or loss is computed based on the change in the follower’s market-implied price over the holding period.

## 5 Experiments

### 5.1 Experimental Setup

#### Data and windows.

We use Kalshi prediction-market data in the Economics category spanning October 2021 to November 2025.
After filtering markets with insufficient activity or negligible price variation, we retain 554 event markets.
Evaluation follows a rolling-window protocol with 60-day training windows and 30-day testing windows, yielding 18 non-overlapping test periods.

#### Pipeline and hyperparameters.

Within each training window, we perform ADF unit-root testing and apply
first differencing when necessary prior to Granger analysis.
We then run pairwise Granger causality tests across all available markets.
For each event pair, we evaluate both causal directions and sweep lag
lengths L∈{1,2,3,4,5}L\in\{1,2,3,4,5\}, retaining the strongest statistical evidence
of directional predictability.
Because these optimal lag orders are short in market-implied probability dynamics, we treat the trading holding horizon hh as an independent evaluation parameter and report robustness across multiple horizons.
From these tests, we retain the top K=100K=100 directed pairs ranked by
statistical significance.
From this candidate set, we form a portfolio by selecting the top M=20M=20
directed pairs under two ranking conditions: the *statistical*
approach and the *hybrid* approach (see Section [4.1](https://arxiv.org/html/2602.07048v1#S4.SS1 "4.1 Ranking Methods for Candidate Causal Relationships ‣ 4 Methods ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets")). For the semantic re-ranking stage, we use GPT-5-nano as the LLM. Each trade is executed with position size of 100 per contract.

#### Evaluation settings and default configuration.

We evaluate trading performance using holding horizons h∈{1,3,5,7,10,14,21}h\in\{1,3,5,7,10,14,21\} days and report standard trading metrics including win rate, average win/loss per trade, and total PnL aggregated across test windows.
Unless otherwise specified, we report results under a default configuration consisting of a 7-day holding period, trades triggered when leader relative price change exceeds threshold θ=0\theta=0
(i.e., |rL,t|>0|r\_{L,t}|>0), and portfolios of size M=20M=20.

### 5.2 Results

#### LLM filtering yields substantial reductions in downside risk.

Table [3](https://arxiv.org/html/2602.07048v1#S5.T3 "Table 3 ‣ Loss reduction persists for distinct event pairs. ‣ 5.2 Results ‣ 5 Experiments ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets") reports the primary comparison between the statistical and hybrid approaches under the default evaluation setting.
LLM-based re-ranking leads to a substantial improvement in total PnL (+205%) accompanied by a modest increase in win rate.
This pattern indicates that the gains are not driven by a small number of outlier wins or aggressive upside bets.
Instead, the dominant driver of the performance improvement is a large reduction in average loss magnitude (46.5%),
highlighting enhanced downside control as the primary mechanism.

#### Loss reduction persists for distinct event pairs.

To examine whether the observed loss reduction is driven by trivial semantic overlap, we analyze performance composition under the default setting.
As shown in Table [3](https://arxiv.org/html/2602.07048v1#S5.T3 "Table 3 ‣ Loss reduction persists for distinct event pairs. ‣ 5.2 Results ‣ 5 Experiments ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets"), LLM filtering reduces average loss magnitude by 48.1% for different-event pairs (from $642 to $333), comparable to the reduction observed for same-event pairs (42.9%).
This indicates that the gains are not attributable to trivial event overlap, but persist for genuinely distinct event relationships.

Table 1: 
Trading-based evaluation summary.
We compare portfolios constructed under the *statistical approach* and the *hybrid approach* across rolling test windows.
Metrics include trade count, win rate, average win/loss per trade, and total PnL; performance gains are driven primarily by reductions in average loss magnitude.

|  |  |  |  |
| --- | --- | --- | --- |
| Metric | Statistical Approach | Hybrid Approach | Change |
| Win Rate | 51.4% | 54.5% | +3.1pp |
| Avg Win | $724 | $636 | -12% |
| Avg Loss | -$649 | -$347 | +46.5% |
| Total PnL | $4,100 | $12,500 | +205% |

Table 2: 
Comparison of downside losses across approaches under same-event and different-event settings.
Same-event pairs correspond to the same underlying real-world event with different thresholds or contract formulations, whereas different-event pairs correspond to genuinely distinct events.
We report average loss per trade; lower average loss indicates better downside control.

|  |  |  |
| --- | --- | --- |
| Method | Same-Event | Different-Event |
| Avg. Loss of Statistical Approach | -$700 | -$642 |
| Avg. Loss of Hybrid Approach | -$400 | -$333 |
| Loss Reduction | 42.9% | 48.1% |

Table 3: 
Win rate (WR) by the magnitude of leader movement, indicating which side outperforms in investment outcomes.
Here, the magnitude of leader movement is defined as the amount of change in the leader event’s price pp at a given time.
Win rates (WR) are reported for Statistical Apporach (Statistical WR) and Hybrid Approach(Hybrid WR) portfolios; Δ\Delta denotes the win-rate difference in percentage points.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Magnitude of leader movement (pt) | Statistical WR | Hybrid WR | Winner | Δ\Delta |
| 5–10 pt | 57.1% | 66.7% | LLM | +9.5pp |
| 10+ pt | 53.8% | 71.4% | LLM | +17.6pp |

#### Semantic filtering is most valuable during large leader moves.

We next examine performance by the magnitude of leader price changes.
As shown in Table [3](https://arxiv.org/html/2602.07048v1#S5.T3 "Table 3 ‣ Loss reduction persists for distinct event pairs. ‣ 5.2 Results ‣ 5 Experiments ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets"), semantic re-ranking delivers larger gains when leader markets experience larger discrete repricings.
For 5–10pt moves, win rate increases from 57.1% to 66.7% (+9.5pp),
and for moves exceeding 10pt, it rises from 53.8% to 71.4% (+17.6pp).
This pattern suggests that LLM filtering is particularly effective at mitigating regime-sensitive failures that arise during large market moves.

#### LLM rescues high-value relationships missed by Granger ranking.

Beyond aggregate performance gains, the semantic filtering stage surfaces economically coherent lead–lag relationships that would be excluded under purely statistical or surface-level semantic screening.
Table [4](https://arxiv.org/html/2602.07048v1#S5.T4 "Table 4 ‣ LLM rescues high-value relationships missed by Granger ranking. ‣ 5.2 Results ‣ 5 Experiments ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets") summarizes representative *LLM-only* trades that fall outside the Granger Top-MM portfolio by pp-value ranking, yet yield positive realized outcomes after LLM-based filtering.
Notably, the Japan Recession →\rightarrow U.S. GDP pair has a Granger rank of #71—far outside the Top-MM cutoff—yet is selected by the LLM based on a clear cross-border macroeconomic mechanism.
Despite exhibiting low surface-form similarity and weak Granger statistics, the LLM assigns a negative causal sign, reasoning that
*“recessions imply weaker domestic demand, and through cross-border trade, financial linkages, and policy spillovers, downturns in major economies tend to drag on aggregate growth.”*
Rather than relying on lexical or topical overlap, the LLM promotes such pairs by inferring latent economic transmission channels and assigning a consistent causal sign that translates into profitable trade directions.
These qualitative results illustrate that the LLM stage does not merely refine statistical rankings, but actively recovers structurally meaningful relationships that are brittle under both Granger-based ordering and lightweight embedding similarity.

Table 4: 
Representative pairs ranked low by the Statistical Approach but elevated by the Hybrid Approach.
SR = Statistical Rank (Granger pp-value); HR = Hybrid Rank (after LLM re-ranking).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Leader | Follower | SR | HR | PnL |
| China 2022 GDP Growth >>5% | World 2022 GDP Growth >>3% | #23 | #17 | +$1,100 |
| Japan 2026 Recession | US Q1 2025 GDP Growth >>2% | #71 | #5 | +$700 |
| US 2025 Oil Prod. >>14.5M bbl/day | Brazil 2025 Inflation >>5.5% | #24 | #15 | +$600 |
| India 2026 Recession | CRE Delinq. Q4 2024 >>3% | #51 | #3 | +$200 |




Table 5: 
Hold period ablation (trades with |Δ​pL,t|>0|\Delta p\_{L,t}|>0 only).
We report win rate and average loss for Statistical Approach versus Hybrid Approach portfolios as the holding horizon varies;
Loss Reduction is the relative decrease in average loss magnitude under Hybrid filtering.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Hold | Stat. WR | Hybrid WR | Stat. Avg Loss | Hybrid Avg Loss | Loss Reduction |
| 1d | 56.0% | 66.7% | -$536 | -$283 | 47.2% |
| 3d | 44.7% | 62.8% | -$773 | -$469 | 39.4% |
| 5d | 47.5% | 66.0% | -$745 | -$500 | 32.9% |
| 7d | 51.4% | 54.5% | -$649 | -$347 | 46.5% |
| 10d | 51.4% | 56.9% | -$497 | -$371 | 25.3% |
| 14d | 49.5% | 56.1% | -$661 | -$400 | 39.5% |
| 21d | 47.3% | 53.1% | -$973 | -$753 | 22.6% |
| Mean | ∼\sim50% | ∼\sim59% | -$689 | -$446 | 36.2% |

### 5.3 Robustness and Ablations

We assess the robustness of this loss-reduction behavior by varying the holding horizon while keeping all other evaluation settings fixed.
Table [5](https://arxiv.org/html/2602.07048v1#S5.T5 "Table 5 ‣ LLM rescues high-value relationships missed by Granger ranking. ‣ 5.2 Results ‣ 5 Experiments ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets") reports performance across holding periods ranging from 1 to 21 days.
Across all tested horizons, LLM filtering consistently reduces average loss magnitude relative to the statistical baseline.
The relative reduction in average loss ranges from 22.6% to 47.2%, with a mean reduction of 36.2% across holding periods.
This consistency indicates that the observed behavior is not driven by a particular choice of holding horizon, but reflects a stable enhancement in the robustness of the selected relationships.
While win rates vary with the holding period, the loss-reduction effect persists even when win-rate gains are modest, further supporting the interpretation that semantic filtering primarily improves downside control.

## 6 Conclusion

We introduced a dual-stage causal filtering framework for prediction markets, combining statistical lead–lag screening via Granger causality with LLM-based semantic verification.
Across rolling-window evaluations, LLM re-ranking consistently improves trading performance, with gains driven primarily by substantial reductions in average loss magnitude (downside risk) and accompanied by modest improvements in win rate. Taken together, these results suggest that LLMs can act as semantic risk managers on top of statistical discovery, prioritizing relationships that generalize more reliably under changing market conditions.

## References

* S. Bennett, M. Cucuringu, and G. Reinert (2022)
  Lead–lag detection and network clustering for multivariate time series with an application to the us equity market.
  Machine Learning 111,  pp. 4497–4538.
  External Links: [Document](https://dx.doi.org/10.1007/s10994-022-06250-4)
  Cited by: [§1](https://arxiv.org/html/2602.07048v1#S1.p1.1 "1 Introduction ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets").
* J. E. Berg, F. D. Nelson, and T. A. Rietz (2008)
  Prediction market accuracy in the long run.
  International Journal of Forecasting 24 (2),  pp. 285–300.
  Cited by: [§2](https://arxiv.org/html/2602.07048v1#S2.SS0.SSS0.Px2.p2.1 "Semantic evaluation with LLMs and event-based settings. ‣ 2 Related Work ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets").
* A. Chaudhry, P. Xu, and Q. Gu (2017)
  Uncertainty assessment and false discovery rate control in high-dimensional granger causal inference.
  In International Conference on Machine Learning,
   pp. 684–693.
  Cited by: [§2](https://arxiv.org/html/2602.07048v1#S2.SS0.SSS0.Px1.p1.1 "Limits of statistical significance in lead–lag discovery. ‣ 2 Related Work ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets").
* D. A. Dickey and W. A. Fuller (1979)
  Distribution of the estimators for autoregressive time series with a unit root.
  Journal of the American Statistical Association 74 (366),  pp. 427–431.
  External Links: [Document](https://dx.doi.org/10.1080/01621459.1979.10482531)
  Cited by: [§3.3](https://arxiv.org/html/2602.07048v1#S3.SS3.p2.3 "3.3 Directional predictability via Granger causality ‣ 3 Background ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets").
* F. X. Diebold and R. S. Mariano (2002)
  Comparing predictive accuracy.
  Journal of Business & economic statistics 20 (1),  pp. 134–144.
  Cited by: [§2](https://arxiv.org/html/2602.07048v1#S2.SS0.SSS0.Px1.p3.1 "Limits of statistical significance in lead–lag discovery. ‣ 2 Related Work ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets").
* C. W. Granger (1969)
  Investigating causal relations by econometric models and cross-spectral methods.
  Econometrica: journal of the Econometric Society,  pp. 424–438.
  Cited by: [§2](https://arxiv.org/html/2602.07048v1#S2.SS0.SSS0.Px1.p1.1 "Limits of statistical significance in lead–lag discovery. ‣ 2 Related Work ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets").
* N. Gruver, M. Finzi, S. Qiu, and A. G. Wilson (2023)
  Large language models are zero-shot time series forecasters.
  Advances in Neural Information Processing Systems 36,  pp. 19622–19635.
  Cited by: [§1](https://arxiv.org/html/2602.07048v1#S1.p3.1 "1 Introduction ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets").
* J. D. Hamilton (2020)
  Time series analysis.
   Princeton university press.
  Cited by: [§3.3](https://arxiv.org/html/2602.07048v1#S3.SS3.p2.3 "3.3 Directional predictability via Granger causality ‣ 3 Background ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets"),
  [§3.3](https://arxiv.org/html/2602.07048v1#S3.SS3.p3.2 "3.3 Directional predictability via Granger causality ‣ 3 Background ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets").
* J. Hasbrouck (1995)
  One security, many markets: determining the contributions to price discovery.
  The journal of Finance 50 (4),  pp. 1175–1199.
  Cited by: [§2](https://arxiv.org/html/2602.07048v1#S2.SS0.SSS0.Px1.p1.1 "Limits of statistical significance in lead–lag discovery. ‣ 2 Related Work ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets").
* M. Jin, S. Wang, L. Ma, Z. Chu, J. Zhang, X. Shi, P. Chen, Y. Liang, Y. Li, S. Pan, and Q. Wen (2024)
  Time-llm: time series forecasting by reprogramming large language models.
  In International Conference on Learning Representations, B. Kim, Y. Yue, S. Chaudhuri, K. Fragkiadaki, M. Khan, and Y. Sun (Eds.),
  Vol. 2024,  pp. 23857–23880.
  External Links: [Link](https://proceedings.iclr.cc/paper_files/paper/2024/file/680b2a8135b9c71278a09cafb605869e-Paper-Conference.pdf)
  Cited by: [§1](https://arxiv.org/html/2602.07048v1#S1.p3.1 "1 Introduction ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets").
* R. J. Kinnear and R. R. Mazumdar (2023)
  Exact recovery of granger causality graphs with unconditional pairwise tests.
  Network Science 11 (3),  pp. 431–457.
  Cited by: [§2](https://arxiv.org/html/2602.07048v1#S2.SS0.SSS0.Px1.p1.1 "Limits of statistical significance in lead–lag discovery. ‣ 2 Related Work ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets").
* A. W. Lo and A. C. MacKinlay (1990)
  An econometric analysis of nonsynchronous trading.
  Journal of Econometrics 45 (1-2),  pp. 181–211.
  Cited by: [§2](https://arxiv.org/html/2602.07048v1#S2.SS0.SSS0.Px1.p1.1 "Limits of statistical significance in lead–lag discovery. ‣ 2 Related Work ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets").
* OpenAI (2026)
  Compare models.
  Note: <https://platform.openai.com/docs/models/compare>Last accessed February 2, 2026
  Cited by: [§A.1](https://arxiv.org/html/2602.07048v1#A1.SS1.SSS0.Px1.p1.1 "Post-cutoff evaluation to mitigate lookahead bias. ‣ A.1 Additional Experiments ‣ Appendix A Appendix ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets").
* P. C. Phillips (1986)
  Understanding spurious regressions in econometrics.
  Journal of econometrics 33 (3),  pp. 311–340.
  Cited by: [§1](https://arxiv.org/html/2602.07048v1#S1.p2.1 "1 Introduction ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets"),
  [§2](https://arxiv.org/html/2602.07048v1#S2.SS0.SSS0.Px1.p2.1 "Limits of statistical significance in lead–lag discovery. ‣ 2 Related Work ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets").
* B. Rossi and Y. Wang (2019)
  Vector autoregressive-based granger causality tests in the presence of instabilities.
  The Stata Journal 19 (4),  pp. 883–899.
  External Links: [Document](https://dx.doi.org/10.1177/1536867X19893631)
  Cited by: [§1](https://arxiv.org/html/2602.07048v1#S1.p2.1 "1 Introduction ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets"),
  [§2](https://arxiv.org/html/2602.07048v1#S2.SS0.SSS0.Px1.p2.1 "Limits of statistical significance in lead–lag discovery. ‣ 2 Related Work ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets").
* B. Rossi (2021)
  Forecasting in the presence of instabilities: how we know whether models predict well and how to improve them.
  Journal of Economic Literature 59 (4),  pp. 1135–1190.
  Cited by: [§2](https://arxiv.org/html/2602.07048v1#S2.SS0.SSS0.Px1.p3.1 "Limits of statistical significance in lead–lag discovery. ‣ 2 Related Work ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets").
* S. E. Said and D. A. Dickey (1984)
  Testing for unit roots in autoregressive-moving average models of unknown order.
  Biometrika 71 (3),  pp. 599–607.
  Cited by: [§3.3](https://arxiv.org/html/2602.07048v1#S3.SS3.p2.3 "3.3 Directional predictability via Granger causality ‣ 3 Background ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets").
* R. Sullivan, A. Timmermann, and H. White (1999)
  Data-snooping, technical trading rule performance, and the bootstrap.
  The journal of Finance 54 (5),  pp. 1647–1691.
  Cited by: [§2](https://arxiv.org/html/2602.07048v1#S2.SS0.SSS0.Px1.p2.1 "Limits of statistical significance in lead–lag discovery. ‣ 2 Related Work ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets").
* D. Ventosa-Santaulària and J. E. Vera-Valdés (2008)
  Granger-causality in the presence of structural breaks.
  Economics Bulletin 3 (61).
  Cited by: [§2](https://arxiv.org/html/2602.07048v1#S2.SS0.SSS0.Px1.p2.1 "Limits of statistical significance in lead–lag discovery. ‣ 2 Related Work ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets").
* Z. Wang (2024)
  Causalbench: a comprehensive benchmark for evaluating causal reasoning capabilities of large language models.
  In Proceedings of the 10th SIGHAN Workshop on Chinese Language Processing (SIGHAN-10),
   pp. 143–151.
  Cited by: [§2](https://arxiv.org/html/2602.07048v1#S2.SS0.SSS0.Px2.p1.1 "Semantic evaluation with LLMs and event-based settings. ‣ 2 Related Work ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets").
* J. Wolfers and E. Zitzewitz (2004)
  Prediction markets.
  Journal of Economic Perspectives 18 (2),  pp. 107–126.
  Cited by: [§2](https://arxiv.org/html/2602.07048v1#S2.SS0.SSS0.Px2.p2.1 "Semantic evaluation with LLMs and event-based settings. ‣ 2 Related Work ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets").
* L. Yang, V. Shirvaikar, O. Clivio, and F. Falck (2024)
  A critical review of causal reasoning benchmarks for large language models.
  Note: arXiv
  External Links: 2407.08029,
  [Link](https://arxiv.org/abs/2407.08029)
  Cited by: [§2](https://arxiv.org/html/2602.07048v1#S2.SS0.SSS0.Px2.p1.1 "Semantic evaluation with LLMs and event-based settings. ‣ 2 Related Work ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets").
* L. Zheng, W. Chiang, Y. Sheng, S. Zhuang, Z. Wu, Y. Zhuang, Z. Lin, Z. Li, D. Li, E. Xing, et al. (2023)
  Judging llm-as-a-judge with mt-bench and chatbot arena.
  Advances in neural information processing systems 36,  pp. 46595–46623.
  Cited by: [§2](https://arxiv.org/html/2602.07048v1#S2.SS0.SSS0.Px2.p1.1 "Semantic evaluation with LLMs and event-based settings. ‣ 2 Related Work ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets").

## Appendix A Appendix

### A.1 Additional Experiments

In this appendix, we provide robustness analyses to examine whether the semantic re-ranking behavior we observe is stable under a post-cutoff evaluation setting and across different LLM model variants.

Table 6: Trading performance after training cutoff (entry date >> May 31, 2024).

|  |  |  |  |
| --- | --- | --- | --- |
| Metric | Statistical Approach | Hybrid Approach | Change |
| Win Rate | 61.8% | 62.1% | +0.3pp |
| Avg Win | $614 | $656 | +6.8% |
| Avg Loss | -$700 | -$418 | +40.3% |
| Total PnL | $3,800 | $7,200 | +89% |

#### Post-cutoff evaluation to mitigate lookahead bias.

To mitigate potential lookahead from an LLM’s pretraining knowledge, we evaluate our method on a post-cutoff dataset consisting only of test periods after May 31, 2024, based on the publicly documented training data cutoff of the LLM (OpenAI, [2026](https://arxiv.org/html/2602.07048v1#bib.bib23 "Compare models")). All other components of the pipeline are kept unchanged.

As shown in Table [6](https://arxiv.org/html/2602.07048v1#A1.T6 "Table 6 ‣ A.1 Additional Experiments ‣ Appendix A Appendix ‣ LLM as a Risk Manager: LLM Semantic Filtering for Lead–Lag Trading in Prediction Markets"), the hybrid approach continues to outperform the statistical baseline under post-cutoff evaluation. As in the main results, the average loss magnitude is reduced by 40.3% (from $700 to $418), yielding an 89% improvement in total PnL. These results reinforce the interpretation of the LLM as a semantic risk manager that systematically suppresses large downside losses by deprioritizing statistically fragile relationships.

#### Robustness across LLM model variants.

We further repeat the entire semantic re-ranking using an alternative model variant, GPT-5-mini, and observe the same loss-reduction behavior. This suggests that the risk-management effect is robust across model choices.

### A.2 Prompt Template for LLM-Based Semantic Filtering

We use a fixed prompt format across all candidate pairs to ensure consistent semantic scoring and to avoid pair-specific tuning.

![Refer to caption](plots/prompt_hybrid.png)


Figure 3: 
Prompt template used for LLM-based semantic filtering.
Given a directed leader–follower event pair, the model assesses whether a plausible economic transmission mechanism exists (beyond correlation), assigns a strength level, and predicts the expected sign of co-movement, returning a structured JSON output.