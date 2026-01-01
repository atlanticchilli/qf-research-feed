---
authors:
- Lucas A. Souza
doc_id: arxiv:2512.24621v1
family_id: arxiv:2512.24621
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Forward-Oriented Causal Observables for Non-Stationary Financial Markets
url_abs: http://arxiv.org/abs/2512.24621v1
url_html: https://arxiv.org/html/2512.24621v1
venue: arXiv q-fin
version: 1
year: 2025
---


Lucas A. Souza
[lasouza@if.usp.br](mailto:lasouza@if.usp.br)

###### Abstract

We study short-horizon forecasting in financial time series under strict causal constraints, treating the market as a non-stationary stochastic system in which any predictive observable must be computable online from information available up to the decision time.
Rather than proposing a machine-learning predictor or a direct price-forecast model, we focus on *constructing* an interpretable causal signal from heterogeneous micro-features that encode complementary aspects of the dynamics (momentum, volume pressure, trend acceleration, and volatility-normalized price location).
The construction combines (i) causal centering, (ii) linear aggregation into a composite observable, (iii) causal stabilization via a one-dimensional Kalman filter, and (iv) an adaptive “forward-like” operator that mixes the composite signal with a smoothed causal derivative term.
The resulting observable is mapped into a transparent decision functional and evaluated through realized cumulative returns and turnover.
An application to high-frequency EURUSDT (1-minute) illustrates that causally constructed observables can exhibit substantial economic relevance in specific regimes, while degrading under subsequent regime shifts, highlighting both the potential and the limitations of causal signal design in non-stationary markets.

###### keywords:

Causality, Financial time series, Signal construction, Regime dependence, Kalman filtering, Non-stationarity

††journal: Physica A: Statistical Mechanics and its Applications

\affiliation

[aff1]
organization=São Paulo,
state=SP,
country=Brazil

## 1 Introduction and Related Literature

Financial markets can be viewed as complex stochastic systems, where collective dynamics, information flow, and feedback effects give rise to non-trivial temporal correlations and non-stationary behavior, a perspective long explored in statistical physics and nonlinear dynamics [schreiber2000, marschinski2002].
Within this framework, price dynamics emerge from the interaction of heterogeneous agents and exhibit noisy, nonlinear, and time-varying features that challenge equilibrium-based descriptions.
The application of tools from statistical physics to financial markets has revealed well-documented empirical regularities, including heavy-tailed return distributions, volatility clustering, and excess kurtosis [bouchaud2003theory, cont2000herd, mantegna1995].
Such emergent collective effects deviate markedly from the Gaussian benchmark and motivate modeling approaches that explicitly account for feedback mechanisms, clustering, and non-stationarity.

A central modeling question concerns the origin of large price moves and volatility bursts: to what extent are they driven by exogenous information shocks (e.g., macroeconomic news) versus endogenous dynamics arising from internal amplification mechanisms?
Recent empirical evidence supports a clear dynamical distinction between exogenous and endogenous jumps.
Exogenous events typically manifest as abrupt volatility spikes followed by power-law relaxation reminiscent of Omori’s law for earthquake aftershocks, whereas endogenous events are often preceded by a gradual build-up of volatility, consistent with self-exciting feedback mechanisms
[Lallouache2020, Marcaccioli\_2022].
This perspective naturally connects to the broader literature on endogenous market activity and reflexivity, in which self-exciting point processes—most notably Hawkes processes—provide a parsimonious mathematical framework to represent event clustering and cascading behavior [hawkes1971].

In parallel, the analysis of causality and information flow across market variables has become an important tool for studying short-horizon predictability in noisy environments.
Nonlinear dependence measures such as transfer entropy offer a principled way to quantify directed information flow between observables beyond linear correlation [schreiber2000, marschinski2002].
Building on these ideas, recent forecasting pipelines have combined causality-based covariates with modern sequence models to improve predictive performance in multivariate financial settings [berenguer2024].
Moreover, even at the microstructural level, physical constraints on information transmission impose irreducible limits on simultaneity across geographically separated trading venues, with direct implications for high-frequency trading and market regulation [Angel2014physicsAndFinancial].

Against this background, a strict practical constraint is often under-emphasized: any tradable predictive observable must be computed *online*, using exclusively information available up to the decision time.
In practice, seemingly innocuous steps—such as smoothing, normalization, or label and target construction—can introduce subtle look-ahead biases that materially inflate backtest performance.
While recent work has increasingly employed machine learning and statistical learning techniques to extract patterns from financial time series
[zahedi2015, rounaghi2015, roostaee2023, wood2024],
robustness under regime shifts remains a persistent challenge, including well-documented breakdowns of trend and momentum effects during market stress episodes [daniel2016].

Motivated by the need for signals that preserve strict causal validity while remaining economically meaningful, this paper focuses on engineering an interpretable composite observable from heterogeneous technical features, including momentum, volume pressure, trend acceleration, and volatility-normalized price location.
Rather than performing direct price prediction, we construct a causal signal stabilized via a one-dimensional Kalman filter [kalman1960] and introduce an adaptive forward-like operator that combines the filtered signal with a smoothed causal derivative component.
The resulting signal is evaluated through a transparent threshold-based decision rule applied to high-frequency EURUSDT (1-minute) data.

Empirically, we find that the proposed causal signal exhibits substantial economic relevance over specific market regimes.
However, its effectiveness is strongly regime-dependent and degrades following structural changes in the underlying dynamics.
These findings reinforce the non-stationary and adaptive nature of financial markets and motivate the methodological focus of this study on causal signal construction, filtering, and regime sensitivity under strict information constraints.

## 2 Methodology

This section formalizes the causal forecasting setup adopted in this study.
All signals, transformations, and decision rules are constructed under strict causal constraints, relying exclusively on information available up to time tt.
The focus is on signal design and causal filtering rather than on explicit price prediction.

### 2.1 Forecasting Under Causal Constraints

Under strict causality, forecasting at short horizons is constrained by the limited information content available at the decision time.
Signals must be constructed from contemporaneous and past observations only, while remaining sufficiently stable to support decisions and sufficiently responsive to reflect regime changes.
This tension between responsiveness and stability constitutes a central challenge in causal signal design.

A second challenge arises from the use of technical indicators and filtering operations.
Many standard preprocessing steps—such as smoothing, normalization, or target construction—implicitly rely on future information when applied naively.
In a causal setting, these operations must be reformulated so that no information beyond time tt enters the signal at any stage of construction.

Finally, economic relevance imposes an additional constraint.
A causally valid signal may exhibit appealing statistical properties while failing to translate into meaningful realized performance under a decision rule.
For this reason, the methodology emphasizes constructions that can be mapped into transparent decision functionals and evaluated through realized outcomes (returns and turnover), rather than relying solely on forecast error metrics.

### 2.2 Causal Signal Construction

We construct a predictive observable by aggregating heterogeneous sources of market information in a fully causal manner.
Rather than relying on a single indicator, we combine representative measures of momentum, volume pressure, trend acceleration, and volatility-normalized price location.

Each component captures a distinct informational dimension: relative strength (RSI), volume-adjusted momentum (MFI), trend acceleration (MACD difference) and volatility-normalized price position (BB %).
The indicators are not used as standalone trading rules, but as features entering a unified signal construction. Throughout the analysis, all indicator lookback windows and parameter ranges are fixed to conventional values widely adopted in the technical analysis literature and in market practice, with no optimization performed.

To ensure comparability across indicators and avoid look-ahead bias, each series is centered using a causal median operator:

|  |  |  |  |
| --- | --- | --- | --- |
|  | I~t(k)=It(k)−median⁡{Iτ(k):τ<t}.\tilde{I}\_{t}^{(k)}=I\_{t}^{(k)}-\operatorname{median}\{I\_{\tau}^{(k)}:\tau<t\}. |  | (1) |

The centered indicators are linearly combined into a raw composite signal:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℱ0​(t)=1K​∑k=1Kαk​I~t(k).\mathscr{F}\_{0}(t)=\frac{1}{K}\sum\_{k=1}^{K}\alpha\_{k}\tilde{I}\_{t}^{(k)}. |  | (2) |

As the present study employs four indicators, the aggregation takes the explicit form

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℱ0​(t)=14​(αMFI​I~t(MFI)+αRSI​I~t(RSI)+αBB%​I~t(BB%)+αMACD​I~t(MACD)),\mathscr{F}\_{0}(t)=\frac{1}{4}\Big(\alpha\_{\text{MFI}}\,\tilde{I}\_{t}^{(\text{MFI})}+\alpha\_{\text{RSI}}\,\tilde{I}\_{t}^{(\text{RSI})}+\alpha\_{\text{BB}\%}\,\tilde{I}\_{t}^{(\text{BB}\%)}+\alpha\_{\text{MACD}}\,\tilde{I}\_{t}^{(\text{MACD})}\Big), |  | (3) |

where the coefficients αk\alpha\_{k} are fixed scaling constants chosen to account for the typical magnitude of each indicator.

Figure [1](https://arxiv.org/html/2512.24621v1#S2.F1 "Figure 1 ‣ 2.2 Causal Signal Construction ‣ 2 Methodology ‣ Forward-Oriented Causal Observables for Non-Stationary Financial Markets") illustrates the intermediate stages of the causal signal construction using a representative 1-minute EURUSDT excerpt.
The figure displays the indicator components after causal centering and the resulting composite ℱ0​(t)\mathscr{F}\_{0}(t).
Because the raw aggregation remains sensitive to high-frequency fluctuations, a causal smoothing step based on a one-dimensional Kalman filter is applied, yielding a stabilized indicator-level observable that serves as an intermediate building block for the final predictive signal.
The Kalman filter parameters are fixed to q=0.01q=0.01 and r=0.1r=0.1; further implementation details are provided in [B](https://arxiv.org/html/2512.24621v1#A2 "Appendix B Kalman Filter ‣ Forward-Oriented Causal Observables for Non-Stationary Financial Markets").
The dependence of the resulting signal on the Kalman filter parameters is acknowledged, but not explored systematically in this work.

![Refer to caption](x1.png)


Figure 1: Causal construction of the composite observable. The causally centered indicators are linearly aggregated into the raw composite signal ℱ0\mathscr{F}\_{0} and subsequently smoothed via a one-dimensional Kalman filter. The linear scaling coefficients (α\alpha) are indicated in the figure.

### 2.3 Approximate Forward Operator

The raw composite signal ℱ0​(t)\mathscr{F}\_{0}(t) is fully causal and constructed exclusively from information available up to time tt.
While ℱ0​(t)\mathscr{F}\_{0}(t) captures contemporaneous structure, it does not necessarily yield economically meaningful performance when mapped directly into positions over short horizons.
Figure [2](https://arxiv.org/html/2512.24621v1#S2.F2 "Figure 2 ‣ 2.3 Approximate Forward Operator ‣ 2 Methodology ‣ Forward-Oriented Causal Observables for Non-Stationary Financial Markets") illustrates this behavior in a representative interval, where ℱ0​(t)\mathscr{F}\_{0}(t) underperforms compared to forward-shifted versions.

![Refer to caption](x2.png)


Figure 2: Cumulative returns for the raw signal ℱ0​(t)\mathscr{F}\_{0}(t) and its forward-shifted versions, illustrating that advancing the signal in time produces larger cumulative gains.

Motivated by this empirical observation, we introduce a causal transformation that injects forward-oriented structure while preserving online computability.
Specifically, we define

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℱ​(t)=c1​(t)​ℱ0​(t)+2​c2​(t)​∂tℱ0~​(t),\mathscr{F}(t)=c\_{1}(t)\,\mathscr{F}\_{0}(t)+2c\_{2}(t)\,\widetilde{\partial\_{t}\mathscr{F}\_{0}}(t), |  | (4) |

where ∂tℱ0~​(t)\widetilde{\partial\_{t}\mathscr{F}\_{0}}(t) denotes a smoothed causal approximation
(moving average with span 4) of the first derivative ℱ0′​(t)\mathscr{F}^{\prime}\_{0}(t).
In practice, the derivative is computed via a causal finite-difference estimate,
followed by a short-span moving-average smoothing (span equal to four observations),
which mitigates high-frequency oscillations while preserving local anticipatory structure. The numerical factor 22 multiplying the derivative term is a fixed scaling constant,
introduced to balance the typical magnitudes of ℱ0​(t)\mathscr{F}\_{0}(t) and
∂tℱ0~​(t)\widetilde{\partial\_{t}\mathscr{F}\_{0}}(t) and kept constant throughout the analysis.

The inclusion of a derivative-based term is motivated by its ability to encode local forward tendency.
In smooth dynamical systems, the first derivative provides local information about the direction of evolution; for a sinusoid, the derivative corresponds to a phase-shifted signal.
While financial time series are neither deterministic nor periodic,
this analogy motivates the use of derivative information as a local
forward proxy under causality constraints, particularly in transition
regions where ℱ0​(t)\mathscr{F}\_{0}(t) fluctuates around zero and directional
information becomes most relevant.

The mixing coefficients c1​(t)c\_{1}(t) and c2​(t)c\_{2}(t) are made state-dependent through ℱ0​(t)\mathscr{F}\_{0}(t).
When |ℱ0​(t)||\mathscr{F}\_{0}(t)| is large, indicating a persistent regime, greater weight is assigned to ℱ0​(t)\mathscr{F}\_{0}(t) itself.
When ℱ0​(t)\mathscr{F}\_{0}(t) is near zero, derivative information becomes relatively more informative.
Accordingly,

|  |  |  |  |
| --- | --- | --- | --- |
|  | c1​(t)=tanh⁡(|ℱ0​(t)|),c2​(t)=1−tanh⁡(|ℱ0​(t)2|).c\_{1}(t)=\tanh\!\left(\lvert\mathscr{F}\_{0}(t)\rvert\right),\qquad c\_{2}(t)=1-\tanh\!\left(\left\lvert\frac{\mathscr{F}\_{0}(t)}{2}\right\rvert\right). |  | (5) |

Given the guiding observable ℱ​(t)\mathscr{F}(t), the remaining step is to specify how it is translated into an actionable decision functional. We therefore proceed to define the decision rule and state update mechanism used in the empirical analysis.

### 2.4 Decision Rule and State Update

Given the guiding signal ℱ​(t)\mathscr{F}(t), we specify a transparent state-based decision rule with a neutral zone controlled by a threshold θ>0\theta>0.

Let st=ℱ​(t)s\_{t}=\mathscr{F}(t) denote the signal value at time tt.
The state variable pt∈{0,1}p\_{t}\in\{0,1\} indicates whether the system is in the “active” (invested/long) state or in the “inactive” (flat) state, respectively.
State updates follow a two-state hysteresis rule:

|  |  |  |  |
| --- | --- | --- | --- |
|  | pt={1,if ​pt−1=0​ and ​st>θ,0,if ​pt−1=1​ and ​st<−θ,pt−1,otherwise.p\_{t}=\begin{cases}1,&\text{if }p\_{t-1}=0\text{ and }s\_{t}>\theta,\\ 0,&\text{if }p\_{t-1}=1\text{ and }s\_{t}<-\theta,\\ p\_{t-1},&\text{otherwise}.\end{cases} |  | (6) |

This prevents rapid switching when the signal fluctuates around zero and ensures that state changes occur only when the signal crosses sufficiently strong positive or negative levels.

To preserve strict causality in the evaluation, the realized state applied at time tt is pt−1p\_{t-1} (one-step delay).
Denoting the simple return of the underlying asset by

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt=Pt−Pt−1Pt−1,r\_{t}=\frac{P\_{t}-P\_{t-1}}{P\_{t-1}}, |  | (7) |

the realized response is computed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt=pt−1​rt.R\_{t}=p\_{t-1}\,r\_{t}. |  | (8) |

Cumulative performance is reported via the compounded return series

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt=V0​∏τ=1t(1+Rτ),V\_{t}=V\_{0}\prod\_{\tau=1}^{t}(1+R\_{\tau}), |  | (9) |

with V0V\_{0} normalized to one.
The buy-and-hold benchmark is computed analogously using rtr\_{t} in place of RtR\_{t}.

Trading activity is quantified by counting state changes. Define

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​pt=|pt−pt−1|,\Delta p\_{t}=|p\_{t}-p\_{t-1}|, |  | (10) |

and total activity up to time tt by ∑τ=1tΔ​pτ\sum\_{\tau=1}^{t}\Delta p\_{\tau}.

## 3 Experimental Results

This section reports empirical results for the EURUSDT exchange rate at the 1-minute frequency.
Importantly, all results in this section are computed without transaction costs.
This isolates the intrinsic economic relevance of the proposed causal observable from market frictions; the implications of even minimal fees are discussed in the concluding section.

Prior to computing any indicators, the raw price series is filtered to retain only active Forex trading hours (local time).
Saturdays are removed entirely, as well as Sundays before 18:00 and Fridays after 18:00.
This avoids distortions caused by weekend closures and illiquid periods and ensures that all indicators entering ℱ0​(t)\mathscr{F}\_{0}(t) and ℱ​(t)\mathscr{F}(t) are computed from contiguous market activity.

Figure [3](https://arxiv.org/html/2512.24621v1#S3.F3 "Figure 3 ‣ 3 Experimental Results ‣ Forward-Oriented Causal Observables for Non-Stationary Financial Markets") compares the cumulative returns induced by the proposed decision rule when applied to the forward-oriented causal observable ℱ​(t)\mathscr{F}(t) and to the raw composite signal ℱ0​(t)\mathscr{F}\_{0}(t), alongside a buy-and-hold benchmark.
The lower panel reports cumulative trading activity.
The threshold value θ=0.06\theta=0.06 was chosen as a representative scale of the signal fluctuations, corresponding to a moderate percentile of the empirical distribution of ℱ​(t)\mathscr{F}(t), and was kept fixed throughout the analysis; no parameter tuning or performance-based optimization was performed.

The figure reveals a pronounced regime dependence.
During the period from 2023 to approximately September 2024, the ℱ\mathscr{F}-based rule exhibits strong cumulative growth relative to buy-and-hold, whereas performance partially retraces and subsequently fluctuates around a near-plateau in the later period.
This behavior is quantified in Table [1](https://arxiv.org/html/2512.24621v1#S3.T1 "Table 1 ‣ 3 Experimental Results ‣ Forward-Oriented Causal Observables for Non-Stationary Financial Markets"), which highlights the contrast between early growth and subsequent degradation, accompanied by sustained—and even increasing—trading activity in the second subperiod (around 10310^{3} trades per month).
The persistence of high turnover despite diminishing gains indicates that the causal observable continues to trigger frequent state changes even as its incremental economic relevance deteriorates.

Importantly, Fig. [3](https://arxiv.org/html/2512.24621v1#S3.F3 "Figure 3 ‣ 3 Experimental Results ‣ Forward-Oriented Causal Observables for Non-Stationary Financial Markets") also shows that applying the same decision rule directly to the raw composite signal ℱ0​(t)\mathscr{F}\_{0}(t) results in substantially weaker growth and earlier saturation.
While ℱ0​(t)\mathscr{F}\_{0}(t) captures contemporaneous market structure, it lacks forward-oriented content.
This contrast demonstrates that the derivative-based component is essential: a purely smoothed or delayed version of ℱ0​(t)\mathscr{F}\_{0}(t) does not introduce additional predictive structure, whereas the causal derivative contributes local directional information, particularly around regime transition regions.

Two empirical features are noteworthy. First, the induced dynamics exhibit substantial outperformance relative to buy-and-hold during extended intervals, most visibly throughout 2023 and up to approximately September 2024.
Second, from late 2024 onward, the cumulative performance partially retraces and then fluctuates around a near-plateau, while trading activity remains elevated. This combination of high turnover and limited incremental gains is consistent with the view that a fixed causal construction can become misaligned with the prevailing regime in a non-stationary environment.

![Refer to caption](x3.png)


Figure 3: Performance induced by applying the same threshold-based decision rule to the forward-oriented causal observable ℱ​(t)\mathscr{F}(t) and to the raw composite signal ℱ0​(t)\mathscr{F}\_{0}(t) for EURUSDT at the 1-minute frequency.
The upper panel shows cumulative returns relative to buy-and-hold, while the lower panel reports the cumulative number of state changes (trades).
The threshold is fixed at θ=0.06\theta=0.06 for both signals.




Table 1: Incremental performance and activity metrics computed separately within each subperiod, with the cumulative return curve normalized to V0=1V\_{0}=1 at the beginning of each regime. End equity VV denotes the final value.

| Period | End VV | Cum. ret. (%) | MDD (%) | Trades/mo |
| --- | --- | --- | --- | --- |
| 2023–Sep 2024 | 3.14 | 214 | -4 | 959 |
| Post-Sep 2024 | 2.74 | -13 | -17 | 1117 |

## 4 Summary and Conclusion

We proposed a transparent framework for constructing short-horizon predictive observables under strict causal constraints.
The methodology emphasizes signal engineering: (i) causal centering of heterogeneous indicator-level features, (ii) linear aggregation into a composite observable ℱ0​(t)\mathscr{F}\_{0}(t), (iii) causal stabilization via a one-dimensional Kalman filter, and (iv) an adaptive forward-like operator that combines ℱ0​(t)\mathscr{F}\_{0}(t) with a smoothed causal derivative term.
A key message is that economically relevant structure can be extracted without resorting to black-box predictors, provided causality is enforced and evaluation is disciplined.

In high-frequency EURUSDT, the induced dynamics show strong outperformance relative to buy-and-hold from 2023 through approximately September 2024, followed by a pronounced plateau thereafter.
This pattern is consistent with regime-dependent relevance in a non-stationary environment and motivates explicit mechanisms for regime adaptivity.
Importantly, results are intentionally reported without transaction costs to isolate intrinsic signal effects. Given the high turnover, even small frictions would materially reduce net performance, so the reported outcomes should be interpreted as evidence of predictive structure under idealized conditions rather than as an execution-ready trading strategy.

Future work naturally follows three directions: (i) friction-aware evaluation (spreads, slippage, latency) and turnover control;
(ii) explicit regime adaptivity via change detection and time-varying thresholds or mixing functions c1​(t),c2​(t)c\_{1}(t),c\_{2}(t); and
(iii) generalizing the forward operator to a small causal basis of local features (multi-scale differences, short moving averages, or compact state-space augmentations), as well as a systematic investigation of the role of filtering choices and Kalman parameter sensitivity, while preserving interpretability and strict online computability.
These extensions keep the central philosophy intact: causal construction first, model complexity later.

## Appendix A Technical Indicators

This appendix documents the technical indicators employed in the construction.
All indicators rely exclusively on information available up to time tt, ensuring strict causality, n line with classical definitions of technical indicators in financial time series (see, e.g., [murphy1999technical]).

### A.1 Relative Strength Index (RSI)

The Relative Strength Index (RSI) is used as a bounded momentum measure and is defined [wilder1978] as

|  |  |  |  |
| --- | --- | --- | --- |
|  | RSIt=100​(1−11+GtLt),\text{RSI}\_{t}=100\left(1-\frac{1}{1+\frac{G\_{t}}{L\_{t}}}\right), |  | (11) |

where GtG\_{t} and LtL\_{t} denote average gains and losses, respectively.

### A.2 Money Flow Index (MFI)

The Money Flow Index (MFI) is a volume-weighted momentum indicator defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | MFIt=100​(1−11+Positive Money FlowNegative Money Flow).\text{MFI}\_{t}=100\left(1-\frac{1}{1+\frac{\text{Positive Money Flow}}{\text{Negative Money Flow}}}\right). |  | (12) |

### A.3 Moving Average Convergence Divergence (MACD Difference)

The MACD difference captures short-term trend acceleration [appel1979]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | MACD Difft=(EMAfast​(t)−EMAslow​(t))−Signalt.\text{MACD Diff}\_{t}=\bigl(\text{EMA}\_{\text{fast}}(t)-\text{EMA}\_{\text{slow}}(t)\bigr)-\text{Signal}\_{t}. |  | (13) |

### A.4 Bollinger Band Percent (BB%)

The Bollinger Band Percent (BB%) provides a volatility-adjusted measure of price location:

|  |  |  |  |
| --- | --- | --- | --- |
|  | BB%t=Pt−(μt−k​σt)(μt+k​σt)−(μt−k​σt).\text{BB\%}\_{t}=\frac{P\_{t}-(\mu\_{t}-k\sigma\_{t})}{(\mu\_{t}+k\sigma\_{t})-(\mu\_{t}-k\sigma\_{t})}. |  | (14) |

## Appendix B Kalman Filter

To reduce high-frequency noise while preserving strict causality, the composite signal is smoothed using a one-dimensional Kalman filter [kalman1960].
The latent state follows a random-walk model,

|  |  |  |  |
| --- | --- | --- | --- |
|  | xt=xt−1+wt,wt∼𝒩​(0,q),x\_{t}=x\_{t-1}+w\_{t},\qquad w\_{t}\sim\mathscr{N}(0,q), |  | (15) |

and observations are noisy measurements,

|  |  |  |  |
| --- | --- | --- | --- |
|  | zt=xt+vt,vt∼𝒩​(0,r).z\_{t}=x\_{t}+v\_{t},\qquad v\_{t}\sim\mathscr{N}(0,r). |  | (16) |

The filter is implemented recursively using information available up to time tt only, initialized with x0=z0x\_{0}=z\_{0}, and no backward smoothing is applied.