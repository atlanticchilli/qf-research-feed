---
authors:
- The Anh Pham
- Bao Chan Nguyen
- Nguyet Nguyen Thi
doc_id: arxiv:2603.09219v1
family_id: arxiv:2603.09219
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating
  Overfitting in Quantitative Strategies'
url_abs: http://arxiv.org/abs/2603.09219v1
url_html: https://arxiv.org/html/2603.09219v1
venue: arXiv q-fin
version: 1
year: 2026
---


Nguyen Thi Nguyet
ds.nguyetnt@gmail.com
AlgoXpert Lab –
Algorithmic Trading, Quantitative Finance, AI & Data Science
  
<https://algoxpert.org/>
  
Corresponding author:admin@algoxpert.org

Nguyen Bao Chan
nguyenbaochan20042002@gmail.com
AlgoXpert Lab –
Algorithmic Trading, Quantitative Finance, AI & Data Science
  
<https://algoxpert.org/>
  
Corresponding author:admin@algoxpert.org

Pham The Anh
Founder & CEO, AlgoXpert
pta.forwork@gmail.com
AlgoXpert Lab –
Algorithmic Trading, Quantitative Finance, AI & Data Science
  
<https://algoxpert.org/>
  
Corresponding author:admin@algoxpert.org

###### Abstract

Transitioning a strategy from backtest to live operation is where many quantitative trading systems fail, primarily due to parameter overfitting, selection bias, and fragility under regime shifts. This paper proposes the AlgoXpert Alpha Research Framework—a standardized, decision-oriented protocol that evaluates strategies across three chronological stages: (i) In-Sample (IS), which prioritizes stable parameter regions (plateaus) over single optima; (ii) Walk-Forward Analysis (WFA) with rolling windows and purge gaps to mitigate information leakage, equipped with majority-pass and catastrophic-veto decision gates; and (iii) Out-of-Sample (OOS) holdout under strict parameter lock (no further tuning). The framework integrates a defense-in-depth architecture: structural (cliff veto), execution (spread/leverage guards), and equity protection (circuit breakers, kill switch). A case study on USDJPY M5 intraday illustrates the procedure for detecting overfitting through performance degradation and drawdown integrity under chronology. A post-validation report comparing four alpha variants (v1–v4) reveals rank reversal when switching the objective from maximizing Sharpe to minimizing MaxDD, underscoring the trade-off between risk-adjusted performance and tail-risk control.

Keywords: Alpha Research Framework; Walk-Forward Analysis; Purged Validation; Parameter Stability; Backtest Overfitting; Selection Bias; Execution-Aware Backtesting; Stress Testing; Kill Switch; Out-of-Sample Verification.

Disclaimer. For research purposes only; not investment advice. Past performance does not guarantee future results.

## 1 Introduction

In algorithmic trading, the gap between a seemingly compelling backtest alpha and a stable live system is where strategies most often fail. Three prevalent causes are: (i) excessive parameter optimization on finite data, causing the model to fit noise (overfitting) [[4](#bib.bib4)], (ii) testing numerous configurations or variants without proper controls, leading to selection bias [[5](#bib.bib5), [6](#bib.bib6)], and (iii) time-varying changes in volatility, liquidity, and execution costs that render strategies fragile under regime shifts. Accordingly, the objective of this paper is not to maximize “peak backtest” performance, but to standardize a deployment decision protocol that is reproducible and auditable: a strategy advances only upon passing clearly defined decision gates in strict chronological order.

### 1.1 Practical Gaps

In practice, many useful techniques exist—walk-forward analysis [[1](#bib.bib1)], parameter stability checks, stress testing, and data-leakage mitigation [[3](#bib.bib3)]. However, these are often applied in isolation, lacking an end-to-end protocol that translates research results into deployment decisions. This paper targets three core gaps and three secondary gaps:

* •

  Core Gap A – Parameter selection without “stability regions”: many pipelines still select a single optimum, whereas extreme points are typically sensitive and prone to breakdown under small perturbations; there is a lack of policies that prioritize stable plateaus and avoid cliff-type sensitivity regions.
* •

  Core Gap B – WFA without leakage control for stateful strategies: naïve train–test splitting can yield optimistic evaluations for stateful/path-dependent strategies [[3](#bib.bib3)], as indicator overlap and position state may “bleed” across boundaries, reducing the “blindness” of the forward test.
* •

  Core Gap C – Validation decoupled from execution and risk: many pipelines optimize the signal first, appending costs and guards as an afterthought [[9](#bib.bib9)], whereas operational failures often originate from microstructure friction (spread widening, adverse fills) and ill-timed leverage accumulation.
* •

  Secondary Gap 1 – Absence of deployment gates: explicit pass/fail checklists for the IS→\toWFA→\toOOS progression are rare.
* •

  Secondary Gap 2 – Safeguards without ablation: ablation studies that disable individual protection layers to measure their marginal contribution to tail-risk reduction are seldom conducted.
* •

  Secondary Gap 3 – Search transparency: descriptions of degrees of freedom (grid/trial sizes) and parameter-locking policies are frequently omitted, impeding assessment of selection bias and reproducibility.

### 1.2 Proposal and Contributions

We propose the AlgoXpert Alpha Research Framework, an IS–WFA–OOS pipeline oriented toward deployment decisions that aims to reduce overfitting and improve generalizability. Rather than maximizing “peak backtest” metrics, the framework prioritizes robustness across multiple validation stages. The main contributions are:

* •

  (C1) Stability-region parameter selection:
  instead of selecting a single optimum, we prioritize configurations within a “stable region” (plateau) and avoid sensitivity-prone “cliff” zones. The IS stability region is defined as:

  |  |  |  |
  | --- | --- | --- |
  |  | Ωs​t​a​b​l​e={θ∣S​R​(θ)≥0.9⋅S​Ro​p​t},\Omega\_{stable}=\{\theta\mid SR(\theta)\geq 0.9\cdot SR\_{opt}\}, |  |

  retaining configurations whose risk-adjusted Sharpe achieves at least 90% of the best observed IS configuration. Details on the search space, α\alpha selection, and cliff-veto criteria are provided in Section [3.2](#S3.SS2 "3.2 Strategy Class and Notation ‣ 3 Methods ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies").
* •

  (C2) Purged rolling walk-forward analysis:
  we design WFA with rolling windows and insert purge gaps between train and test segments to mitigate leakage and carryover effects, which is particularly important for stateful/path-dependent strategies (e.g., grid, trailing, inventory state). The protocol description and WFA schedule are detailed in Section [3.2](#S3.SS2 "3.2 Strategy Class and Notation ‣ 3 Methods ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies").
* •

  (C3) Defense-in-depth safeguards:
  execution and equity constraints are embedded directly into the pipeline (e.g., spread/leverage guards, circuit breakers, and kill switch). Additionally, the framework mandates stress testing by degrading execution assumptions (increasing spread/commission or simulating adverse fills) to assess resilience. Details on metrics and stress envelope are provided in Section [4.2](#S4.SS2 "4.2 Evaluation Metrics and Decision Gates ‣ 4 Empirical Study ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies").
* •

  (C4) Decision gates and checklists:
  the framework provides pass/fail criteria for the IS→\toWFA→\toOOS progression via decision gates that are pre-committed. At Stage II, gates are anchored to forward windows: each fold ii is deemed PASS only if the metric vector on Wit​e​s​tW\_{i}^{test} meets the minimum benchmark 𝐛\mathbf{b}; the entire WFA is PASS if the proportion of passing folds meets threshold qq (majority-pass), and FAIL immediately upon triggering the catastrophic veto (e.g., drawdown integrity breakdown or constraint violation 𝒞\mathcal{C}). The majority-pass + catastrophic-veto mechanism and fold-level evaluation procedure are described directly in Algorithm [1](#alg1 "Algorithm 1 ‣ Procedure summary. ‣ 3.4 Stage II: Purged Rolling Walk-Forward Analysis ‣ 3 Methods ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies").

  Beyond gate criteria, we additionally report train→\totest degradation diagnostics (e.g., resilience ratio) to illuminate failure modes; these diagnostics are not used for pass/fail decisions or tuning.

### 1.3 Scope and Assumptions

The framework focuses on time-series trading strategies, particularly stateful/path-dependent ones, where information leakage at train–test boundaries and carryover effects readily produce optimistic evaluations. The procedure adheres to chronology with pre-committed decision gates; train→\totest degradation diagnostics serve failure-mode analysis under a diagnostic-only principle (see Section [3.4](#S3.SS4 "3.4 Stage II: Purged Rolling Walk-Forward Analysis ‣ 3 Methods ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies")).

### 1.4 Paper Organization

Section [2](#S2 "2 Related Work ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies") surveys related work. Section [3](#S3 "3 Methods ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies") presents the IS–WFA–OOS protocol, purge/state-normalization mechanisms, and the safeguard architecture. Section [4](#S4 "4 Empirical Study ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies") illustrates the framework via a case study following chronology. Section [5](#S5 "5 Post-Validation Comparison of Alpha Variants ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies") provides a post-validation report for research and portfolio orientation. Section [6](#S6 "6 Discussion and Conclusion ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies") discusses deployment implications, limitations, and future directions.

## 2 Related Work

A strategy may achieve very high Sharpe or returns in backtesting solely because too many configurations, variants, or rules have been tested on the same dataset. As the number of trials increases, the probability of a “lucky hit” (false discovery) also increases, even when no genuine edge exists. Harvey et al. emphasize the risk of false discoveries in expected-return research as the number of hypotheses (factors/strategies) proliferates, necessitating multiple-testing controls [[5](#bib.bib5)]. From a practitioner’s perspective, Bailey et al. characterize backtest overfitting as a natural consequence of R&D pipelines with large degrees of freedom and performance-based strategy selection [[4](#bib.bib4)]. These results reinforce the argument that “peak backtest” is insufficient for deployment decisions without a protocol that limits overfitting and selection bias.

Even when a researcher reports only a single final strategy, results may still be biased because that strategy was selected after extensive experimentation (data snooping). White proposed the Reality Check to test the performance of “the best strategy in a candidate set” after data-snooping, rather than testing each strategy independently [[6](#bib.bib6)]. Hansen subsequently introduced the Superior Predictive Ability (SPA) test to increase power and reduce sensitivity to low-quality candidates in the comparison set [[7](#bib.bib7)]. These lines of work demonstrate that if one’s pipeline generates multiple candidates, the evaluation must account for the selection process rather than treating the result as a single-shot test.

A complementary strand adjusts popular metrics to avoid optimistic assessment. Bailey and López de Prado proposed the Deflated Sharpe Ratio (DSR) to correct the observed Sharpe for sample length, non-normality of returns, and selection bias from multiple trials [[8](#bib.bib8)]. The pragmatic message is: the “raw” Sharpe can be substantially inflated when the strategy is selected from a large search space; therefore one must either (i) reduce degrees of freedom, (ii) employ bias-corrected metrics/tests, or combine both.

WFA is a common practice in systematic strategy evaluation and is typically described as rolling train–forward testing over time [[1](#bib.bib1)]. However, temporal splitting alone does not guarantee elimination of all forms of leakage. For example, long indicator lookbacks cause overlap at train/test boundaries; or strategies with position management (grid, trailing, inventory) make current decisions dependent on the prior path. In such cases, the forward test may be less “blind” than expected, producing optimistic assessments. Therefore, WFA is truly useful for deployment decisions only when accompanied by leakage-control rules and explicit pass/fail gates, rather than serving merely as a performance report.

In finance, especially when labels/features overlap temporally, López de Prado emphasizes purging and embargo to reduce information leakage between train and test [[3](#bib.bib3)]. The intuition is to create a buffer around the cutoff point to mitigate serial correlation and overlap effects. This paper inherits that principle and translates it into a purge gap within rolling WFA, targeting both feature-level leakage (indicator overlap) and state-level leakage (state carryover) for path-dependent strategies.

The gap between backtest and live performance often originates from execution friction: spread widening, slippage, thin liquidity, and regime-dependent costs. The algorithmic trading and optimal execution literature demonstrates that observed performance depends heavily on cost/fill assumptions, necessitating stress testing under adverse scenarios (e.g., cost inflation, degraded fill quality) to identify the strategy’s “breaking point” [[9](#bib.bib9), [10](#bib.bib10)]. From a risk-management perspective, circuit breakers and kill switches are operational-level safeguards designed to limit losses during tail events or when market conditions deviate from model assumptions; they function as “emergency stops” rather than components of performance optimization.

In summary, the above research strands indicate that: (i) selection bias and multiple testing must be controlled at the process level, (ii) WFA requires leakage-mitigation mechanisms for stateful strategies, and (iii) evaluation must be execution-aware through stress testing and operational safeguards.

In contrast to work that focuses on proposing new alphas, this paper focuses on a deployable workflow: (i) parameter selection via stability regions rather than extreme points, (ii) purged rolling WFA for stateful strategies, (iii) stress testing under execution assumptions with operational safeguards, and (iv) auditable decision gates and checklists. The goal is to reduce selection bias, enhance reproducibility, and improve decision quality when transitioning from research to operations.

## 3 Methods

### 3.1 Overview of the Deployment Decision Protocol (IS→\toWFA→\toOOS)

X
Defense-in-depth (throughout)Structural  ||  Execution & Micro  ||  Equity protection
     Stress: costs, regime, time-shift, kill-switch
Ablation: Δ​ℳ​(g)\Delta\mathcal{M}(g)


Stage I: IS (Mapping)
  
Viability: S​Ro​p​t≥S​RminSR\_{opt}\!\geq\!SR\_{\min}
  
Stability ⇒Ωs​t​a​b​l​e\Rightarrow\Omega\_{stable}
  
Cliff veto + shortlist
G1IS


Stage II: Purged WFA
  
Rolling folds + purge gg
  
Forward metrics ℳt​e​s​t,i\mathcal{M}\_{test,i}
  
Majority-pass qq + veto
  
Lock θ⋆\theta^{\star}
G2WFA


Stage III: Strict OOS
  
No further tuning
  
Within-band vs WFA (diag)
  
DD integrity + feasibility
G3OOSΩs​t​a​b​l​e\Omega\_{stable}lock θ⋆\theta^{\star}verdict


DEPLOY

REFACTOR

REJECT
Policy A:  G1 fail →\to Refactor;  
G2/G3 fail →\to RejectPASSPASSPASSFAILFAILFAILSafeguards & stress tests applied throughout IS / WFA / OOS

Figure 1: IS→\toWFA→\toOOS deployment decision protocol with decision gates.

The goal of this work is to standardize a deployment decision protocol that reduces overfitting and selection bias in quantitative strategy R&D. The protocol enforces chronology and decision gates of the pass/fail type: a strategy advances only upon passing validation in strict chronological order.

As illustrated in Figure [1](#S3.F1 "Figure 1 ‣ 3.1 Overview of the Deployment Decision Protocol (IS→WFA→OOS) ‣ 3 Methods ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies"), the framework comprises three stages:
(i) IS performs stability mapping to identify Ωs​t​a​b​l​e\Omega\_{stable} (plateau) and discard cliff-sensitive configurations;
(ii) purged rolling WFA evaluates sequential adaptability through rolling folds with purge gap gg, accompanied by diagnostics (e.g., ηi\eta\_{i}) and gate/veto mechanisms to lock the final configuration θ⋆\theta^{\star};
(iii) strict OOS holdout provides the final validation under no further tuning. Pass/fail thresholds are pre-committed before opening OOS.

In parallel with the three stages, the protocol integrates defense-in-depth safeguards and a stress-test battery (execution/microstructure, equity protection), and defines ablation Δ​ℳ​(g)\Delta\mathcal{M}(g) to measure the marginal contribution of each safeguard.

##### Decision states.

The protocol returns one of three outcomes: Deploy (all gates passed), Reject (fail/veto), or Refactor (failure mode is structural in nature, requiring design changes rather than parameter tuning).

##### Branching policy (Policy A).

In this paper, we adopt Policy A for branching decisions:
*G1 fail ⇒\Rightarrow Refactor* (structural/design-level failure),
*G2 fail ⇒\Rightarrow Reject* (insufficient sequential adaptability), and
*G3 fail ⇒\Rightarrow Reject* (failed strict holdout).

### 3.2 Strategy Class and Notation

Consider a stateful, path-dependent algorithmic trading strategy, applicable to position-management paradigms such as trailing/grid/inventory. Market data are denoted D={xt}t=1TD=\{x\_{t}\}\_{t=1}^{T}, where xtx\_{t} may include bid/ask prices, spread, and other necessary microstructure variables. The strategy is parameterized by a vector θ∈Θ\theta\in\Theta and generates a sequence of trading decisions over time.

##### State and action.

At time tt, the strategy maintains an internal state sts\_{t} (e.g., open positions, grid level, trailing state, margin usage). Based on the observation xtx\_{t} and state sts\_{t}, the strategy produces an action at∈𝒜a\_{t}\in\mathcal{A} (open/close/adjust position, choose lot size, set/adjust stop/take-profit), while simultaneously updating the state:

|  |  |  |  |
| --- | --- | --- | --- |
|  | at=πθ​(xt,st),st+1=fθ​(st,xt,at),a\_{t}=\pi\_{\theta}(x\_{t},s\_{t}),\qquad s\_{t+1}=f\_{\theta}(s\_{t},x\_{t},a\_{t}), |  | (1) |

where πθ\pi\_{\theta} is the trading policy and fθf\_{\theta} describes the state dynamics. Making sts\_{t} explicit is important because, for path-dependent strategies, naïve temporal train/test splitting can introduce leakage at window boundaries (due to indicator/lookback overlap and position state “bleeding” across boundaries), making the forward test less “blind” than expected. This directly motivates the purged WFA design in Section [3.1](#S3.SS1 "3.1 Overview of the Deployment Decision Protocol (IS→WFA→OOS) ‣ 3 Methods ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies").

##### Execution and risk constraints.

Let 𝒞\mathcal{C} denote the set of execution/risk constraints (e.g., spread guard, leverage/DL limit, position count limit, circuit breakers/kill-switch). A parameter configuration θ\theta is considered feasible if, throughout the entire simulation, all generated actions satisfy these constraints:

|  |  |  |  |
| --- | --- | --- | --- |
|  | πθ​ feasible⇔(xt,st,at)⊧𝒞∀t.\pi\_{\theta}\text{ feasible}\iff(x\_{t},s\_{t},a\_{t})\models\mathcal{C}\quad\forall t. |  | (2) |

In our framework, 𝒞\mathcal{C} is enforced throughout IS/WFA/OOS and during stress tests, ensuring that the validation process is execution-aware rather than purely signal-optimized.

##### Equity curve and risk measures.

Let EtE\_{t} denote equity at time tt. The running peak through time tt is
Epeak​(t)=maxu≤t⁡EuE\_{\mathrm{peak}}(t)=\max\_{u\leq t}E\_{u}.
Equity-based drawdown at time tt is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | DDe​q​(t)=Epeak​(t)−EtEpeak​(t),MDDe​q=maxt⁡DDe​q​(t).\mathrm{DD}\_{eq}(t)=\frac{E\_{\mathrm{peak}}(t)-E\_{t}}{E\_{\mathrm{peak}}(t)},\qquad\mathrm{MDD}\_{eq}=\max\_{t}\mathrm{DD}\_{eq}(t). |  | (3) |

Performance and robustness measures (e.g., Sharpe, Calmar, recovery factor, worst-window loss, turnover/holding-time proxies) and their formal estimation/reporting procedures are presented in Section [4.2](#S4.SS2 "4.2 Evaluation Metrics and Decision Gates ‣ 4 Empirical Study ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies"). In the methods section, the above notation is used to describe the decision gates, particularly the “drawdown integrity” criterion in the OOS stage and the equity-protection layers in the safeguards.

### 3.3 Stage I: In-Sample Stability Mapping

The IS stage aims to produce a set of robust parameter candidates for WFA (Section [3.4](#S3.SS4 "3.4 Stage II: Purged Rolling Walk-Forward Analysis ‣ 3 Methods ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies")), rather than selecting a single backtest optimum [[4](#bib.bib4)]. Extreme points are typically sensitive to data noise, regime changes, and minor execution-assumption discrepancies; accordingly, the framework prioritizes “plateaus” (near-optimal but stable regions) and discards “cliffs” (sensitive zones where small parameter perturbations can cause performance collapse or drawdown spikes).

#### 3.3.1 Stability Region Ωs​t​a​b​l​e\Omega\_{stable} (Plateau Selection)

On the IS dataset, we perform a performance mapping over a finite search space (grid or trials with budget BB) to observe the topology of S​R​(θ)SR(\theta), while simultaneously tracking minimum tail-risk indicators (particularly MDDe​q​(θ)\mathrm{MDD}\_{eq}(\theta)). Let

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​Ro​p​t=maxθ∈Θ⁡S​R​(θ)SR\_{opt}=\max\_{\theta\in\Theta}SR(\theta) |  | (4) |

denote the best *observed* value in IS under budget BB (not to be interpreted as the true optimum).

##### Viability condition.

Stage I is considered viable only if

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​Ro​p​t≥S​Rmin>0.SR\_{opt}\geq SR\_{\min}>0. |  | (5) |

If this condition is not met, the strategy terminates with verdict Refactor (Policy A), rather than proceeding to plateau selection.

The stability region is defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ωs​t​a​b​l​e={θ∈Θ∣S​R​(θ)≥α⋅S​Ro​p​t},\Omega\_{stable}=\{\theta\in\Theta\mid SR(\theta)\geq\alpha\cdot SR\_{opt}\}, |  | (6) |

where α∈(0,1)\alpha\in(0,1) is the plateau threshold (default α=0.9\alpha=0.9; sensitivity analysis with respect to α\alpha is reported in Section [4.4](#S4.SS4 "4.4 Results Analysis ‣ 4 Empirical Study ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies")). Configurations outside Ωs​t​a​b​l​e\Omega\_{stable} are excluded due to markedly inferior performance or the risk of spurious selection under large degrees of freedom.

##### Trade-count feasibility filter.

To avoid configurations with high S​RSR but based on too few observations (unreliable and potentially lucky), we apply a minimum trade-count threshold in IS:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ntrades​(θ)≥Nmin.N\_{\text{trades}}(\theta)\geq N\_{\min}. |  | (7) |

Configurations failing this threshold are removed from Ωs​t​a​b​l​e\Omega\_{stable} before shortlisting.

##### Ranking within Ωs​t​a​b​l​e\Omega\_{stable}.

After plateau and feasibility filtering, ranking/shortlisting is performed within Ωs​t​a​b​l​e\Omega\_{stable}. Rather than maximizing S​RSR (which risks reverting to extreme-point selection), we prioritize criteria related to tail-risk and recovery (e.g., Calmar, recovery factor, worst-window loss), aiming to select candidates with reasonable risk characteristics before advancing to WFA.

#### 3.3.2 Cliff Filtering (Sensitivity Veto)

The objective of cliff filtering is to remove configurations that are “good but thin”: a very small parameter change causes sharp performance degradation or drawdown spikes. For each θ\theta, consider the neighborhood 𝒩​(θ)\mathcal{N}(\theta) consisting of adjacent points along each parameter dimension with displacement equal to one grid resolution step (e.g., ±1\pm 1 step), holding other dimensions fixed.

##### Performance cliff (Sharpe).

|  |  |  |  |
| --- | --- | --- | --- |
|  | CliffS​R(θ)=maxθ′∈𝒩​(θ)[SR(θ)−SR(θ′)]+,\mathrm{Cliff}\_{SR}(\theta)=\max\_{\theta^{\prime}\in\mathcal{N}(\theta)}\left[SR(\theta)-SR(\theta^{\prime})\right]\_{+}, |  | (8) |

where [z]+=max⁡(z,0)[z]\_{+}=\max(z,0) measures the worst-case Sharpe degradation under minimal perturbation.

##### Tail-risk cliff (equity drawdown).

|  |  |  |  |
| --- | --- | --- | --- |
|  | CliffD​D(θ)=maxθ′∈𝒩​(θ)[MDDe​q(θ′)−MDDe​q(θ)]+.\mathrm{Cliff}\_{DD}(\theta)=\max\_{\theta^{\prime}\in\mathcal{N}(\theta)}\left[\mathrm{MDD}\_{eq}(\theta^{\prime})-\mathrm{MDD}\_{eq}(\theta)\right]\_{+}. |  | (9) |

##### Rejection rule.

A configuration is rejected if it is sensitive under either criterion:

|  |  |  |  |
| --- | --- | --- | --- |
|  | θ​ is rejected if ​CliffS​R​(θ)>τS​RorCliffD​D​(θ)>τD​D.\theta\text{ is rejected if }\mathrm{Cliff}\_{SR}(\theta)>\tau\_{SR}\ \ \text{or}\ \ \mathrm{Cliff}\_{DD}(\theta)>\tau\_{DD}. |  | (10) |

In practice, cliff filtering is applied within Ωs​t​a​b​l​e\Omega\_{stable} to favor plateau regions with “thickness” (robustness) over thin peaks (fragility).

#### 3.3.3 Parameter Locking Policy

After Stage I, the framework applies a parameter locking policy to constrain degrees of freedom and reduce selection bias across subsequent time windows:

* •

  Lock time: locking occurs after completing plateau selection, feasibility filtering, and cliff veto, simultaneously finalizing a finite shortlist.
* •

  Locked dimensions: cliff-prone parameter dimensions or those governing high-risk behavior (e.g., core parameters or those increasing position/leverage accumulation) are fixed, or restricted to a very small pre-reported subset.
* •

  WFA degrees of freedom: during WFA, each fold may only re-select θi\theta\_{i} from the shortlist (or the locked subset), without re-opening the entire Θ\Theta or altering the strategy structure.

The shortlist size, search budget BB, α\alpha value, threshold NminN\_{\min}, and cliff thresholds (τS​R,τD​D)(\tau\_{SR},\tau\_{DD}) must be reported to allow readers to assess the degrees of freedom, selection bias, and reproducibility of the pipeline.

### 3.4 Stage II: Purged Rolling Walk-Forward Analysis

The WFA stage [[1](#bib.bib1)] is designed to test the sequential adaptability of the strategy: an alpha is considered deployable only if it maintains quality when shifted through time. For stateful/path-dependent strategies (grid/trailing/inventory), naïve train/test splitting can produce optimistic evaluations due to (i) lookback overlap at window boundaries, and (ii) state carryover [[3](#bib.bib3)]. Accordingly, we employ purged rolling WFA and impose pass/fail decision gates before opening OOS.

##### Procedure summary.

Algorithm [1](#alg1 "Algorithm 1 ‣ Procedure summary. ‣ 3.4 Stage II: Purged Rolling Walk-Forward Analysis ‣ 3 Methods ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies") describes the WFA in pseudocode, emphasizing restricted DoF, purge, state normalization, majority-pass gate, and catastrophic veto.

Algorithm 1  Purged rolling WFA with majority-pass gate and catastrophic veto.

0: Stability region/shortlist Ωs​t​a​b​l​e\Omega\_{stable}; schedule {(Wit​r​a​i​n,g,Wit​e​s​t)}i=1N\{(W\_{i}^{train},g,W\_{i}^{test})\}\_{i=1}^{N}; constraints 𝒞\mathcal{C};
forward benchmarks 𝐛\mathbf{b}; majority threshold qq; catastrophic veto rule.

0: WFA verdict PASS/FAIL and locked parameters θ⋆\theta^{\star} if PASS.

1: p​a​s​s←0pass\leftarrow 0, ℐ←∅\mathcal{I}\leftarrow\emptyset.

2: for i=1i=1 to NN do

3:  Optimize (restricted DoF): choose θi∈Ωs​t​a​b​l​e\theta\_{i}\in\Omega\_{stable} using only Wit​r​a​i​nW\_{i}^{train}.

4:  Purge: exclude the gap of length gg immediately after Wit​r​a​i​nW\_{i}^{train}.

5:  State normalization: reset strategy state at start of Wit​e​s​tW\_{i}^{test} (e.g., flat/no inventory).

6:  Forward test: run πθi\pi\_{\theta\_{i}} on Wit​e​s​tW\_{i}^{test} under 𝒞\mathcal{C}; compute ℳt​e​s​t,i\mathcal{M}\_{test,i}.

7:  if fold ii is not evaluable (data/simulation failure or insufficient forward sample) then

8:   continue

9:  end if

10:  ℐ←ℐ∪{i}\mathcal{I}\leftarrow\mathcal{I}\cup\{i\}.

11:  if catastrophic veto triggers on Wit​e​s​tW\_{i}^{test} then

12:   return FAIL.

13:  end if

14:  if ℳt​e​s​t,i⪰𝐛\mathcal{M}\_{test,i}\succeq\mathbf{b} then

15:   p​a​s​s←p​a​s​s+1pass\leftarrow pass+1.

16:  end if

17: end for

18: if |ℐ|=0|\mathcal{I}|=0 then

19:  return FAIL.

20: end if

21: if p​a​s​s/|ℐ|≥qpass/|\mathcal{I}|\geq q then

22:  Lock: select and lock θ⋆\theta^{\star} by a pre-committed rule; return PASS.

23: else

24:  return FAIL.

25: end if

#### 3.4.1 Rolling Fold Structure and Purge Gap gg

The WFA period is divided into NN folds according to a fixed, pre-defined schedule. Each fold ii consists of a training window, followed by a purge gap, and then an out-of-sample test window:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wit​r​a​i​n→purge gap ​g→Wit​e​s​t.W\_{i}^{train}\ \to\ \text{purge gap }g\ \to\ W\_{i}^{test}. |  | (11) |

The purge gap gg is a time segment excluded immediately after Wit​r​a​i​nW\_{i}^{train} to mitigate overlap/serial-dependence effects between train and test (especially when features have long lookbacks), and to reduce leakage risk from stateful strategies. For intraday data, gg is expressed in trading days or bars and is fixed across all folds to avoid result-dependent tuning.

##### Note on rolling schedule and purge/train overlap between folds.

In a consecutive rolling design, the purge gap of the preceding fold may overlap with the beginning of Wi+1t​r​a​i​nW\_{i+1}^{train}. This does not compromise the “blindness” of the forward test, since the critical condition to maintain is: *each* Wit​e​s​tW\_{i}^{test} is always separated from *its own* Wit​r​a​i​nW\_{i}^{train} by a purge gap immediately preceding it. In other words, the purge is defined by the *intra-fold train–test relationship*, not by the inter-fold distance.

#### 3.4.2 State Normalization Prior to Forward Testing

To control leakage from state carryover in path-dependent strategies, the forward test of each fold is evaluated under a normalized state assumption at the start of Wit​e​s​tW\_{i}^{test}. Specifically, at the test-window boundary, the strategy is reset to a canonical state (e.g., flat/no inventory, grid level = 0, trailing state reset, all internal counters/state variables reinitialized).

In terms of implementation, state normalization can be realized in one of two equivalent ways:
(i) run the Wit​e​s​tW\_{i}^{test} simulation as an independent session starting exactly at the test-window opening; or
(ii) force-close all positions and reinitialize internal state variables immediately before entering Wit​e​s​tW\_{i}^{test}.
The objective is to ensure that performance within Wit​e​s​tW\_{i}^{test} reflects temporal generalizability, rather than benefiting from accumulated state in prior segments.

#### 3.4.3 Re-Optimization Rule and Degrees-of-Freedom Constraints

Within each fold ii, configuration selection is permitted only within the controlled scope from Stage I:

|  |  |  |  |
| --- | --- | --- | --- |
|  | θi∈Ωs​t​a​b​l​e(or a locked shortlist from Stage I).\theta\_{i}\in\Omega\_{stable}\quad\text{(or a locked shortlist from Stage I)}. |  | (12) |

This rule ensures WFA does not degenerate into unconstrained optimization across multiple windows (which would inflate selection bias). Per the protocol, WFA is not permitted to (i) re-open the entire parameter space Θ\Theta, or (ii) alter the strategy structure. All permitted “degrees of freedom” (e.g., selection restricted to a shortlist of size KK; or only a subset of execution parameters may be adjusted) must be stated explicitly and held fixed across all folds.

Upon completing WFA, a final configuration θ⋆\theta^{\star} is selected according to a pre-committed rule, for example: the configuration with the best median-S​Rt​e​s​t,iSR\_{test,i} across valid folds, or selection based on risk criteria (Calmar/MDD) across test windows. Crucially, the rule for selecting θ⋆\theta^{\star} must be finalized before opening OOS.

#### 3.4.4 Per-Fold Forward Metrics and Gate Design Principles

For each fold ii, denote the Sharpe ratio on train and forward test:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​Rt​r​a​i​n,i:=S​R​(πθi;Wit​r​a​i​n),S​Rt​e​s​t,i:=S​R​(πθi;Wit​e​s​t),SR\_{train,i}:=SR(\pi\_{\theta\_{i}};W\_{i}^{train}),\qquad SR\_{test,i}:=SR(\pi\_{\theta\_{i}};W\_{i}^{test}), |  | (13) |

where S​R​(⋅)SR(\cdot) is defined and reported in detail in Section [4.2](#S4.SS2 "4.2 Evaluation Metrics and Decision Gates ‣ 4 Empirical Study ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies"). On the forward window, we simultaneously evaluate risk/feasibility metrics (e.g., MDDe​q,t​e​s​t,i\mathrm{MDD}\_{eq,test,i}, Calmart​e​s​t,i\mathrm{Calmar}\_{test,i}, trade density, and the degree of 𝒞\mathcal{C} violation).

##### Principles.

Decision gates are anchored to forward windows. Rationale: Wit​e​s​tW\_{i}^{test} constitutes the temporally “blind” test, and therefore the WFA pass/fail criteria are constructed primarily from metrics on Wit​e​s​tW\_{i}^{test} (benchmark-based).
Train metrics serve only operational and diagnostic roles. Metrics on Wit​r​a​i​nW\_{i}^{train} primarily support θi\theta\_{i} selection within restricted DoF; if needed, train→\totest indicators may be reported as diagnostics, but they do not constitute a tuning loop and are not primary gate conditions.

#### 3.4.5 WFA Decision Gate: Majority-Pass + Catastrophic Veto (Pre-committed)

Let 𝐛\mathbf{b} denote the minimum benchmark vector on the forward window (e.g., comprising Sharpe, drawdown, Calmar thresholds, and trade-density conditions), and q∈(0,1]q\in(0,1] the minimum proportion of folds that must meet the benchmark (pre-committed). A fold ii is deemed PASS on the forward window if:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℳt​e​s​t,i⪰𝐛,\mathcal{M}\_{test,i}\ \succeq\ \mathbf{b}, |  | (14) |

where ℳt​e​s​t,i\mathcal{M}\_{test,i} is the metric vector computed on Wit​e​s​tW\_{i}^{test}, and ⪰\succeq denotes “meets all thresholds.”

##### (1) Majority-pass persistence.

Let ℐ\mathcal{I} denote the set of evaluable folds (no data/simulation failures and meeting minimum evaluation conditions). The requirement is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 1|ℐ|​∑i∈ℐ𝕀​[ℳt​e​s​t,i⪰𝐛]≥q.\frac{1}{|\mathcal{I}|}\sum\_{i\in\mathcal{I}}\mathbb{I}\big[\mathcal{M}\_{test,i}\succeq\mathbf{b}\big]\ \geq\ q. |  | (15) |

##### (2) Catastrophic veto.

If any Wit​e​s​tW\_{i}^{test} exhibits a catastrophic violation according to the pre-committed veto rule (e.g., drawdown exceeding the integrity threshold, or kill-switch/leverage-cap violation per 𝒞\mathcal{C}), the entire WFA FAILs immediately.

##### (3) OOS is not opened upon WFA FAIL.

Following the decision-oriented principle, if WFA FAILs, the strategy does not proceed to OOS holdout (verdict: Reject or Refactor depending on failure mode). If WFA PASSes, the final parameters θ⋆\theta^{\star} are locked and the strategy advances to Stage III under no further tuning.

##### Train→\totest diagnostics (not used for gating).

Beyond gate criteria, we additionally report Δ​S​Ri:=S​Rt​e​s​t,i−S​Rt​r​a​i​n,i\Delta SR\_{i}:=SR\_{test,i}-SR\_{train,i} and resilience ratio ηi:=S​Rt​e​s​t,i/S​Rt​r​a​i​n,i\eta\_{i}:=SR\_{test,i}/SR\_{train,i} for failure-mode analysis. Overarching principle: diagnostics serve only post-hoc analysis and are not used as gate conditions or for tuning θ⋆\theta^{\star}.

## 4 Empirical Study

### 4.1 Experimental Design

The objective of the experimental design is to *operationalize* the IS→\toWFA→\toOOS protocol described in Section [3](#S3 "3 Methods ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies") on a minimal but auditable case study that respects chronology (no peeking) and introduces no additional degrees of freedom beyond what the protocol permits.

#### 4.1.1 Data, Market, and Execution Assumptions

##### Market and frequency.

The case study uses the USDJPY pair on the M5 timeframe. Backtests are run using the Every Tick simulation mode of MetaTrader 5, reflecting the tester’s tick-driven order-matching mechanism.

##### Data source and time span.

Data are sourced from broker Exness; the backtest period covers 01/01/2022–31/12/2025. Throughout the experiment, data are used in chronological order, and all decisions/estimates at each stage rely only on the data permitted for observation at that stage.

##### Capital and leverage assumptions.

The initial deposit is 100,000 with nominal leverage of 1:100. These settings are held fixed throughout IS/WFA/OOS to avoid confounding environmental changes with alpha quality changes.

##### Execution model and transaction costs.

The baseline setup uses an ideal execution model per the tester (no latency simulation; no adverse slippage beyond the default tick-driven mechanism). Spread/commission assumptions (if separately configured) are considered part of the backtest environment and must be documented under “Backtest Assumptions” to ensure reproducibility and proper inference scope. Results in the experimental section should therefore be interpreted as a baseline under simplified execution.

##### Execution-awareness and stress envelope (reporting scope).

Per the logic of Gap C, a complete deployment evaluation requires a stress-test battery (e.g., increased spread/commission, simulated adverse fills). However, in the current reporting version, the team has not conducted stress branches due to resource constraints; instead, we describe the stress envelope as a mandatory framework template and defer stress/ablation results to future versions (see discussion in Section [6](#S6 "6 Discussion and Conclusion ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies")).

#### 4.1.2 IS/WFA/OOS Splits and WFA Schedule (Rolling + Purge)

##### Time-ordered splits (no peeking).

The timeline is partitioned in strict chronological order to reflect deployment conditions:

* •

  In-Sample (IS): 01/01/2022–31/12/2023,
* •

  Walk-Forward Analysis (WFA): 01/01/2024–31/12/2024,
* •

  Out-of-Sample holdout (OOS): 01/01/2025–31/12/2025.

The operating principle is: after completing WFA and locking the final parameters θ⋆\theta^{\star}, no further optimization or tuning is performed when opening OOS (strict no-tuning).

##### Rolling WFA with fixed purge gap.

WFA is designed with rolling windows comprising 3 folds; each fold has the structure
Wit​r​a​i​n→g→Wit​e​s​tW\_{i}^{train}\to g\to W\_{i}^{test} with a fixed purge gap g=5g=5 trading days to mitigate leakage from overlap/lookback and carryover effects in stateful strategies. The WFA schedule is pre-defined and held constant throughout the report (Table [1](#S4.T1 "Table 1 ‣ Rolling WFA with fixed purge gap. ‣ 4.1.2 IS/WFA/OOS Splits and WFA Schedule (Rolling + Purge) ‣ 4.1 Experimental Design ‣ 4 Empirical Study ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies")).

Table 1: Rolling 3-fold WFA schedule (g=5g=5 trading days).

| Fold | Wit​r​a​i​nW\_{i}^{train} | Purge gg | Wit​e​s​tW\_{i}^{test} |
| --- | --- | --- | --- |
| 1 | 01/01/2024 – 31/03/2024 | 01/04 – 05/04 | 06/04 – 30/06/2024 |
| 2 | 01/04/2024 – 30/06/2024 | 01/07 – 05/07 | 06/07 – 30/09/2024 |
| 3 | 01/07/2024 – 30/09/2024 | 01/10 – 05/10 | 06/10/2024 – 31/12/2024 |

##### Stateful/path-dependent strategies and state normalization.

Consistent with the strategy definition in Section [3.2](#S3.SS2 "3.2 Strategy Class and Notation ‣ 3 Methods ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies"), each forward window Wit​e​s​tW\_{i}^{test} is evaluated with a normalized initial state at the start (e.g., flat/no inventory) to mitigate state carryover. This convention is a necessary condition for interpreting WFA as a temporal validation rather than a sequential concatenation susceptible to state “bleed-through.”

##### Degrees-of-freedom constraints in WFA.

Within each fold, parameter re-selection is permitted only within the controlled scope from Stage I (restricted DoF; shortlist/Ωs​t​a​b​l​e\Omega\_{stable}), and the θ⋆\theta^{\star} locking rule after WFA is pre-committed. Train→\totest diagnostics follow the principle stated in Section [3.4](#S3.SS4 "3.4 Stage II: Purged Rolling Walk-Forward Analysis ‣ 3 Methods ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies").

### 4.2 Evaluation Metrics and Decision Gates

#### 4.2.1 Notation and Return Conventions

Let EtE\_{t} denote equity at time tt (reflecting P&L under the bid/ask model and cost configuration of the backtest).
Throughout IS/WFA/OOS, we use a consistent return frequency to avoid discrepancies when comparing across stages.
Specifically, let the periodic return series be:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt=Et−Et−1Et−1,t=1,…,T,R\_{t}=\frac{E\_{t}-E\_{t-1}}{E\_{t-1}},\qquad t=1,\dots,T, |  | (16) |

where “period” may be daily (recommended for reporting, consistent with standard statistics) or per-bar/per-trade (if the internal reporting system uses that convention). When annualizing, use the factor KK equal to the number of periods per year under the chosen convention (e.g., K=252K=252 for daily returns).

#### 4.2.2 Primary Performance and Risk Metrics

##### CAGR (Compound Annual Growth Rate).

Let Es​t​a​r​tE\_{start} and Ee​n​dE\_{end} denote the equity at the beginning and end of the evaluation period; nn is the period length in years (under the same convention as KK):

|  |  |  |  |
| --- | --- | --- | --- |
|  | CAGR=(Ee​n​dEs​t​a​r​t)1n−1.\mathrm{CAGR}=\left(\frac{E\_{end}}{E\_{start}}\right)^{\frac{1}{n}}-1. |  | (17) |

##### Max drawdown (equity-based).

Let Epeak​(t)=maxu≤t⁡EuE\_{\mathrm{peak}}(t)=\max\_{u\leq t}E\_{u}, then:

|  |  |  |  |
| --- | --- | --- | --- |
|  | DDe​q​(t)=Epeak​(t)−EtEpeak​(t),MDDe​q=maxt⁡DDe​q​(t).\mathrm{DD}\_{eq}(t)=\frac{E\_{\mathrm{peak}}(t)-E\_{t}}{E\_{\mathrm{peak}}(t)},\qquad\mathrm{MDD}\_{eq}=\max\_{t}\mathrm{DD}\_{eq}(t). |  | (18) |

##### Return series from equity (equity-based).

Let EtE\_{t} denote equity (including unrealized P&L) at sampling point tt (e.g., daily or per M5 bar).
The return series is defined from equity:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Rt=ln⁡(EtEt−1)(or ​Rt=Et−Et−1Et−1​).R\_{t}=\ln\left(\frac{E\_{t}}{E\_{t-1}}\right)\quad\text{(or }R\_{t}=\frac{E\_{t}-E\_{t-1}}{E\_{t-1}}\text{).} |  | (19) |

Sharpe ratio (equity-based) [[12](#bib.bib12)].
Given {Rt}t=1T\{R\_{t}\}\_{t=1}^{T} and σR\sigma\_{R} the standard deviation of RtR\_{t}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​R=R¯−rfσR.SR=\frac{\overline{R}-r\_{f}}{\sigma\_{R}}. |  | (20) |

If annualized, S​Rann=S​R⋅KSR\_{\mathrm{ann}}=SR\cdot\sqrt{K}, where KK is the number of sampling periods per year
(e.g., K=252K=252 if RtR\_{t} is daily returns).

##### Calmar ratio.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Calmar=CAGRMDDe​q.\mathrm{Calmar}=\frac{\mathrm{CAGR}}{\mathrm{MDD}\_{eq}}. |  | (21) |

#### 4.2.3 Feasibility and Execution-Awareness

##### Trade density and sample thickness.

Let NtradesN\_{\mathrm{trades}} denote the number of trades (or round-turns per reporting convention) in the period; in addition to the total, report trades/day (over actual trading days) to flag cases of “good performance from infrequent trading.”

##### Break-even cost proxy per trade.

A pragmatic proxy for the maximum average “cost cushion” the strategy can absorb before breaking even:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Cm​a​x=∑iPiNtrades.C\_{max}=\frac{\sum\_{i}P\_{i}}{N\_{\mathrm{trades}}}. |  | (22) |

If Cm​a​xC\_{max} is less than the observed/assumed execution cost (spread+commission+slippage), the strategy is flagged as execution-fragile.

#### 4.2.4 Minimum Benchmarks and Decision Gates (Pre-committed)

Let 𝐛\mathbf{b} denote the minimum benchmark vector for PASS/FAIL (committed before opening OOS). In this case study, we use:

|  |  |  |
| --- | --- | --- |
|  | S​R≥2.0,Calmar≥1.5,MDDe​q<7%,trades/day≥5.SR\geq 2.0,\quad\mathrm{Calmar}\geq 1.5,\quad\mathrm{MDD}\_{eq}<7\%,\quad\text{trades/day}\geq 5. |  |

When reporting, if “trades/day” cannot be computed directly from logs, this should be noted explicitly and treated as an open item rather than assumed to pass.

##### Stage I (IS) — viability + shortlist.

IS PASS if 𝐛\mathbf{b} is met and Ntrades≥NminN\_{\mathrm{trades}}\geq N\_{\min} (minimum threshold to guard against thin-sample luck). Only then are plateau selection and cliff veto applied to produce the shortlist.

##### Stage II (WFA).

Fold-pass if metrics on Wit​e​s​tW\_{i}^{test} meet 𝐛\mathbf{b}; overall WFA follows majority-pass + catastrophic veto (Section [3.4](#S3.SS4 "3.4 Stage II: Purged Rolling Walk-Forward Analysis ‣ 3 Methods ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies")) with q=2/3q=2/3.

##### Stage III (OOS holdout).

Parameters are locked after WFA; verdict PASS if OOS metrics meet 𝐛\mathbf{b} under the same baseline execution.

#### 4.2.5 Degradation Diagnostics

Resilience ratio ηi\eta\_{i} and Δ​S​Ri\Delta SR\_{i} (defined in Section [3.4](#S3.SS4 "3.4 Stage II: Purged Rolling Walk-Forward Analysis ‣ 3 Methods ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies")) are reported following the diagnostic-only principle stated therein.

### 4.3 Experimental Results

#### 4.3.1 Stage I (IS): Benchmark Check and Viability

Over the IS period (01/01/2022–31/12/2023), the strategy achieved:
Sharpe =2.12=2.12, Calmar ≈1.69\approx 1.69, MaxDD (equity) =6.46%=6.46\%, N=2625N=2625 trades.
Per the benchmark vector 𝐛\mathbf{b} (Section [4.2](#S4.SS2 "4.2 Evaluation Metrics and Decision Gates ‣ 4 Empirical Study ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies")), the Sharpe/Calmar/MaxDD thresholds are met.
The trade-density criterion (trades/day) has not been directly reported; this is noted as a *reporting gap* to be addressed.

#### 4.3.2 Stage II (WFA): Forward-Window Results

Table [2](#S4.T2 "Table 2 ‣ 4.3.2 Stage II (WFA): Forward-Window Results ‣ 4.3 Experimental Results ‣ 4 Empirical Study ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies") summarizes metrics on Wit​e​s​tW\_{i}^{test} and gate status per pre-committed benchmarks. Train metrics serve internal audit only (diagnostic-only principle, Section [3.4](#S3.SS4 "3.4 Stage II: Purged Rolling Walk-Forward Analysis ‣ 3 Methods ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies")).

Aggregate WFA (mean across forward segments):
Sharpe =3.79=3.79, MaxDD =2.93%=2.93\%, Calmar =7.54=7.54.

Table 2: WFA results per fold on forward windows.

| Fold | S​Rt​e​s​t,iSR\_{test,i} | MDDt​e​s​t,i\mathrm{MDD}\_{test,i} | Calmart​e​s​t,i\mathrm{Calmar}\_{test,i} | Trades | Gate |
| --- | --- | --- | --- | --- | --- |
| 1 | 3.81 | 3.61% | 3.39 | 258 | PASS |
| 2 | 1.36 | 2.89% | 2.34 | 281 | FAIL |
| 3 | 6.20 | 2.30% | 16.89 | 318 | PASS |
| Mean | 3.79 | 2.93% | 7.54 | 286 | – |

##### Gate verdict.

Step 2 FAIL (Sharpe <2.0<2.0), Step 1 and Step 3 PASS. With q=2/3q=2/3, WFA concludes PASS; no fold triggers catastrophic veto (MDD<7%\mathrm{MDD}<7\%).

##### Audit note.

SR on W1t​r​a​i​nW\_{1}^{train} is strongly negative while W1t​e​s​tW\_{1}^{test} is high, possibly due to state normalization or train/test simulation-configuration differences. Per the diagnostic-only principle (Section [3.4](#S3.SS4 "3.4 Stage II: Purged Rolling Walk-Forward Analysis ‣ 3 Methods ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies")), train metrics do not affect the verdict.

#### 4.3.3 Stage III (OOS): One-Year Holdout and Verdict

On the OOS holdout (01/01/2025–31/12/2025) with θ⋆\theta^{\star} locked (Section [3.4](#S3.SS4 "3.4 Stage II: Purged Rolling Walk-Forward Analysis ‣ 3 Methods ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies")), the strategy achieved:
Sharpe =2.34=2.34, Calmar =3.01=3.01, MaxDD =4.21%=4.21\%, N=1374N=1374 trades.
Per 𝐛\mathbf{b}: Sharpe/Calmar/MaxDD pass. The trades/day criterion requires further cross-referencing.

### 4.4 Results Analysis

#### 4.4.1 Verdict Summary by Decision Gates (IS→\toWFA→\toOOS)

Per the protocol in Section [3.1](#S3.SS1 "3.1 Overview of the Deployment Decision Protocol (IS→WFA→OOS) ‣ 3 Methods ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies"), decisions are anchored to pre-committed decision gates. Under the current benchmarks (Sharpe ≥2.0\geq 2.0, Calmar ≥1.5\geq 1.5, MaxDD<7%<7\%, and minimum trade density), the case study shows:
(i) Stage I (IS) meets performance thresholds with sufficient trade count,
(ii) Stage II (WFA) achieves majority-pass on forward windows despite one fold failing on Sharpe,
and (iii) Stage III (OOS) recovers benchmark compliance under strict holdout (no tuning).
Therefore, *within the current simulation assumptions*, the alpha may be regarded as statistically gate-compliant through time. However, a “deploy” conclusion is valid only when execution assumptions are further verified via the stress envelope (see Section [4.4.5](#S4.SS4.SSS5 "4.4.5 Execution Limitations and Missing Stress Envelope ‣ 4.4 Results Analysis ‣ 4 Empirical Study ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies")).

#### 4.4.2 Stage I (IS): Viability and Sample Thickness

IS results (SR =2.12=2.12, Calmar ≈1.69\approx 1.69, MaxDD =6.46%=6.46\%, N=2625N=2625 trades) demonstrate that the strategy passes the minimum viability condition and is not based on a handful of observations (a common backtest-overfitting failure mode). In the framework’s logic (Section [3.3](#S3.SS3 "3.3 Stage I: In-Sample Stability Mapping ‣ 3 Methods ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies")), this is a necessary condition for advancing from “alpha idea” to “testable candidate.”

An important interpretive note: IS here is used to *lock the candidate space* (plateau/shortlist) rather than to demonstrate generalizability. Accordingly, in the experimental section, IS should be read as evidence that the strategy has a sufficiently strong signal under the stated cost/fill model, not as deployment evidence.

#### 4.4.3 Stage II (WFA): Sequential Adaptability and Regime Heterogeneity

WFA forward results show high average performance (SR =3.79=3.79, MaxDD =2.93%=2.93\%, Calmar =7.54=7.54), but fold-level decomposition reveals heterogeneity: Step 2 has forward SR =1.36=1.36 (below the Sharpe threshold), while Step 1 and Step 3 achieve SR =3.81=3.81 and =6.20=6.20, respectively. Under the majority-pass design (Section [3.4](#S3.SS4 "3.4 Stage II: Purged Rolling Walk-Forward Analysis ‣ 3 Methods ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies")), this case is interpreted as follows:

* •

  The signal is not absolutely stable across all time segments, but exhibits majority-window robustness (2/3 folds pass). This represents “meeting the minimum threshold for advancement” rather than “perfect stability.”
* •

  Step 2 serves as a regime-sensitivity indicator: this fold should be viewed as a natural stress-by-time (not cost stress), suggesting that the alpha may degrade under certain volatility/microstructure regimes.
* •

  No catastrophic veto: all forward windows maintain MaxDD below 7%7\%, hence no integrity-constraint veto is triggered. This reinforces the framework’s argument that tail-risk control must be prioritized alongside performance.

##### Audit flag: negative train SR at Step 1.

As noted in Section [4.3](#S4.SS3 "4.3 Experimental Results ‣ 4 Empirical Study ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies"), strongly negative SR on W1t​r​a​i​nW\_{1}^{train} (−4.81-4.81) while W1t​e​s​tW\_{1}^{test} is high warrants audit: (i) re-optimization mechanism, (ii) state normalization at the test boundary, and (iii) consistency in Sharpe definition between train/test. Recommendation: report fold-level forward metrics + gate as primary results; train metrics are for audit purposes.

#### 4.4.4 Stage III (OOS): Strict Holdout and Reasonable Degradation

OOS results (SR =2.34=2.34, Calmar =3.01=3.01, MaxDD =4.21%=4.21\%, N=1374N=1374 trades) meet the benchmark under strict no-tuning holdout, consistent with the selection-bias reduction objective.

Relative comparison through time:

* •

  OOS SR vs. IS: 2.342.34 vs. 2.122.12 shows no degradation, suggesting that performance is not merely a peak IS optimum.
* •

  OOS SR vs. WFA (forward mean): 2.342.34 is lower than 3.793.79, indicating performance normalization upon entering the holdout. This is a commonly observed pattern consistent with the “not maximizing peak backtest” thesis.
* •

  Drawdown integrity: OOS MaxDD (4.21%4.21\%) falls between IS (6.46%6.46\%) and WFA (2.93%2.93\%), implying that risk does not spike upon entering the holdout.

Overall, OOS results provide the strongest evidence in this paper for generalization under chronology, but must still be placed in the context of execution assumptions (see below).

#### 4.4.5 Execution Limitations and Missing Stress Envelope

All current results are produced under ideal execution assumptions (no latency, no adverse slippage beyond the MT5 tick model). Since the paper highlights Gap C, the absence of a stress envelope implies:

* •

  Time-robustness under the current cost model can be established,
* •

  but execution-robustness under microstructure/cost inflation cannot yet be concluded.

In the absence of time to re-run multiple batteries, the scientifically appropriate presentation is:
(i) explicitly state this as baseline validation with stress-testing as planned work,
(ii) retain the stress protocol as a template (without presenting results),
(iii) add a scope limitation statement at the end of the experimental section: “deployment-readiness requires passing a cost/slippage stress envelope; results herein should be interpreted under baseline MT5 assumptions.”

#### 4.4.6 Implications for Future Alpha Evaluation and Ranking

The WFA/OOS portion of the case study should be understood as a single validation unit for *one* alpha. For future multi-alpha leaderboards, the framework suggests a final ranking principle that is post-validation in nature: rank only alphas that have PASSed IS→\toWFA→\toOOS (and eventually the stress envelope), then compare using a pre-committed utility (e.g., prioritize MaxDD/Calmar over SR when the mandate is capital preservation). This clearly separates the deployment decision protocol from the research portfolio report (portfolio/roadmap), consistent with the spirit of the introduction.

## 5 Post-Validation Comparison of Alpha Variants

This section constitutes a post-validation report, not a step within the framework’s decision gates. The objective is to compare four alpha variants that have passed the IS→\toWFA→\toOOS pipeline under the same data setup and execution assumptions described in Section [4.1](#S4.SS1 "4.1 Experimental Design ‣ 4 Empirical Study ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies"), serving research orientation and capital allocation (portfolio view).

### 5.1 Comparison Protocol

Four candidates (v1–v4) are evaluated according to three principles:

1. 1.

   OOS-first ranking: primary ranking is based on OOS holdout (Sharpe, Calmar, MDDe​q\mathrm{MDD}\_{eq}), as this constitutes the strictest “blind” test [[1](#bib.bib1), [4](#bib.bib4)].
2. 2.

   WFA dispersion: S​R¯WFA\overline{SR}\_{\mathrm{WFA}} and inter-fold range measure stability across market regimes (diagnostic, not used for ranking).
3. 3.

   Diagnostic-only: train metrics and resilience ratio ηi\eta\_{i} serve analysis only; they are not used to modify rankings or parameters after θ⋆\theta^{\star} has been locked (Section [3.4](#S3.SS4 "3.4 Stage II: Purged Rolling Walk-Forward Analysis ‣ 3 Methods ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies")).

### 5.2 Stage-by-Stage Results

Table [3](#S5.T3 "Table 3 ‣ 5.2 Stage-by-Stage Results ‣ 5 Post-Validation Comparison of Alpha Variants ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies") summarizes Sharpe, Calmar, and MDDe​q\mathrm{MDD}\_{eq} across the three stages. Bold values indicate the leading candidate at OOS for each metric.

Table 3: Performance of four alphas across IS / WFA / OOS.

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Sharpe | | | Calmar | | | MaxDD (%) | | | Trades |
| Alpha | IS | WFA | OOS | IS | WFA | OOS | IS | WFA | OOS | (OOS) |
| v1 | 2.43 | 3.18 | 2.19 | 1.85 | 6.17 | 2.74 | 6.96 | 3.04 | 4.43 | 1 375 |
| v2 | 2.29 | 2.93 | 2.56 | 1.83 | 5.39 | 3.52 | 6.52 | 3.30 | 4.41 | 1 428 |
| v3 | 2.20 | 2.91 | 2.61 | 1.72 | 5.39 | 3.48 | 6.69 | 3.35 | 4.36 | 1 427 |
| v4 | 2.12 | 3.79 | 2.34 | 1.69 | 7.54 | 3.01 | 6.46 | 2.93 | 4.21 | 1 374 |

##### Key findings (OOS holdout).

* •

  Sharpe: v3 leads (2.61), followed by v2 (2.56); the difference is small and no statistical significance test has been conducted.
* •

  Calmar: v2 is highest (3.52). If a deployment threshold of CalmarOOS>3.0\mathrm{Calmar}\_{\mathrm{OOS}}>3.0 is applied, v1 (2.74) does not qualify.
* •

  MaxDD: v4 is lowest (4.21 %), demonstrating superior tail-risk control.
* •

  Control observation: v1 has the highest IS Sharpe but the weakest OOS—illustrating the risk of selecting alphas by IS peak [[4](#bib.bib4), [8](#bib.bib8)].

### 5.3 WFA Stability Diagnostics

Table [4](#S5.T4 "Table 4 ‣ 5.3 WFA Stability Diagnostics ‣ 5 Post-Validation Comparison of Alpha Variants ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies") presents S​Rt​e​s​t,iSR\_{test,i} across each forward fold along with the mean and range.

Table 4: Forward Sharpe by fold (WFA 3-fold).

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | S​Rt​e​s​t,iSR\_{test,i} | | |  |  |
| Alpha | Fold 1 | Fold 2 | Fold 3 | S​R¯WFA\overline{SR}\_{\mathrm{WFA}} | Range |
| v1 | 2.97 | 1.37 | 5.19 | 3.18 | 3.82 |
| v2 | 2.56 | 1.14 | 5.08 | 2.93 | 3.94 |
| v3 | 2.53 | 1.17 | 5.02 | 2.91 | 3.85 |
| v4 | 3.81 | 1.36 | 6.20 | 3.79 | 4.84 |

All four alphas are relatively weak in Fold 2 (S​R≈1.1SR\approx 1.1–1.41.4) and strong in Fold 3 (S​R≈5SR\approx 5–66), indicating a common regime dependence—this is precisely why rolling WFA is needed rather than relying on a single backtest (see Section [3.4](#S3.SS4 "3.4 Stage II: Purged Rolling Walk-Forward Analysis ‣ 3 Methods ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies")).

### 5.4 Equity-Path Diagnostics (OOS)

![Refer to caption](2603.09219v1/Equity_Alpha.png)


Figure 2: Normalized OOS equity (v1–v4).

Figure [2](#S5.F2 "Figure 2 ‣ 5.4 Equity-Path Diagnostics (OOS) ‣ 5 Post-Validation Comparison of Alpha Variants ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies") enables visual inspection of failure modes that aggregate statistics may obscure: (i) profit concentrated in a short segment, (ii) extended plateaus, or (iii) slow recovery after drawdown.

### 5.5 Trade-Off and Mandate-Dependent Recommendations

Ranking depends on the objective function:

* •

  Maximizing risk-adjusted return: v3 (Sharpe) or v2 (Calmar) are the leading candidates.
* •

  Capital preservation (tail-risk): v4 has the lowest MDDOOS\mathrm{MDD}\_{\mathrm{OOS}}; the trade-off is lower Sharpe/Calmar compared to v2/v3.

The rank reversal when switching from maximizing Sharpe to minimizing MaxDD reflects the fundamental trade-off between performance and tail-risk control [[8](#bib.bib8)], underscoring that *no single metric suffices* for alpha ranking—a multi-dimensional criterion set tied to a specific mandate is required.

### 5.6 Limitations of the Post-Validation Report

* •

  Results are based on ideal execution assumptions (Section [4.1.1](#S4.SS1.SSS1 "4.1.1 Data, Market, and Execution Assumptions ‣ 4.1 Experimental Design ‣ 4 Empirical Study ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies")); rankings may change under a cost/slippage stress envelope.
* •

  Comparing four variants from the same search process increases degrees of freedom at the research level; interpreting small differences between v2 and v3 requires supplementary tests (Deflated Sharpe [[8](#bib.bib8)], SPA [[7](#bib.bib7)], or HAC confidence intervals [[11](#bib.bib11)]).

## 6 Discussion and Conclusion

### 6.1 Practical Implications for Deployment and Governance

This paper treats deployment as an auditable decision rather than a backtest optimization outcome. Accordingly, the primary “deliverable” is not a single alpha but a standardized validation protocol that produces a PASS/FAIL verdict following IS→\toWFA→\toOOS chronology and pre-committed decision gates.

##### Minimum deployment checklist.

A strategy is deemed eligible for advancement only if it simultaneously satisfies:

* •

  Chronology & no-peeking: θ⋆\theta^{\star} locked after WFA; no tuning upon opening OOS (Section [3.4](#S3.SS4 "3.4 Stage II: Purged Rolling Walk-Forward Analysis ‣ 3 Methods ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies")).
* •

  Restricted DoF: WFA re-selects within Ωstable\Omega\_{\mathrm{stable}}/shortlist; Θ\Theta is not re-opened after Stage I (Section [3.3](#S3.SS3 "3.3 Stage I: In-Sample Stability Mapping ‣ 3 Methods ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies")).
* •

  Gate on forward windows: majority-pass + catastrophic veto (Section [3.4](#S3.SS4 "3.4 Stage II: Purged Rolling Walk-Forward Analysis ‣ 3 Methods ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies"), Algorithm [1](#alg1 "Algorithm 1 ‣ Procedure summary. ‣ 3.4 Stage II: Purged Rolling Walk-Forward Analysis ‣ 3 Methods ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies")).
* •

  Execution-aware reporting: execution assumptions are explicitly declared; results are interpreted within that context rather than defaulting to “deployable.”

##### Governance/audit: requirements for auditable research.

To reduce selection bias and enhance reproducibility, research should be accompanied by a minimum “evidence pack”:

* •

  Search transparency: description of search budget, grid/trial size, permitted parameter dimensions, and locking timing.
* •

  Artifact logging: backtest configuration, data version, seed (if applicable), and stage-by-stage results (IS/WFA/OOS) under a common metric standard.
* •

  Decision trace: explicit pass/fail rules (benchmark 𝐛\mathbf{b}, majority threshold qq, catastrophic veto) and failure-mode-to-verdict mapping (Reject vs. Refactor).

These requirements separate “attractive results” from “valid process,” making conclusions falsifiable: if OOS is opened and the gate fails, the strategy is eliminated without “rescue tuning.”

### 6.2 Limitations

Results should be interpreted in the context of the following limitations (see also Section [4.4.5](#S4.SS4.SSS5 "4.4.5 Execution Limitations and Missing Stress Envelope ‣ 4.4 Results Analysis ‣ 4 Empirical Study ‣ AlgoXpert Alpha Research Framework: A Rigorous IS–WFA–OOS Protocol for Mitigating Overfitting in Quantitative Strategies")):

* •

  Simplified execution: ideal execution assumed; latency/slippage not explicitly modeled—increases optimism risk for microstructure-sensitive strategies.
* •

  Single asset/broker: USDJPY M5 case study on MT5/Exness; transferability has not been verified.
* •

  Incomplete stress/ablation: stress envelope described as a template; current results constitute baseline validation.
* •

  Multi-alpha selection bias: comparing v1–v4 increases DoF at the research level; small differences require supplementary testing [[8](#bib.bib8), [7](#bib.bib7)].

### 6.3 Future Directions

Direct extensions to enhance deployability and scientific rigor include:

* •

  Multi-asset & multi-timescale validation: replicate the protocol across multiple FX pairs/assets and timeframes; report regime-conditional stability (trend/range, volatility regimes).
* •

  More realistic execution models: incorporate explicit latency/slippage models, cost-ladder stress envelopes (spread/commission/slippage inflation), and “point-of-failure” testing.
* •

  Portfolio-level governance: transition from single-alpha evaluation to portfolio selection/retention/exit processes (correlation, tail co-movement, risk budgeting), with post-deployment monitoring rules.
* •

  Pre-registration and selection-bias testing: pre-commit benchmarks, number of trials, and alpha selection criteria; apply appropriate tests/corrections for multiple hypothesis testing.
* •

  Live paper trading: add a paper/live-sim stage as a “deployment rehearsal” to verify microstructure assumptions before real capital allocation.

### 6.4 Conclusion

This paper proposes the AlgoXpert Alpha Research Framework, a decision-oriented IS–WFA–OOS protocol designed to reduce overfitting and improve robustness when transitioning from backtest to operations. The core contributions of the framework are (i) parameter selection via stability regions rather than extreme points, (ii) purged rolling WFA to mitigate leakage for stateful/path-dependent strategies, (iii) integrated defense-in-depth safeguards following an execution-aware approach, and (iv) auditable pass/fail decision gates.

Within the current illustrative scope, the framework is validated in the sense that the chronological validation procedure produces consistent and traceable decisions, while surfacing failure modes requiring audit (e.g., train–test discrepancies by fold) rather than concealing them behind aggregate statistics. Conversely, the framework should not be interpreted as a profit guarantee; simulation assumptions (particularly latency/slippage) and the completeness of stress testing/ablation are boundary conditions for deployability inference.

In summary, the primary value of the framework lies in standardizing the deployment decision process rather than maximizing “peak backtest”: an alpha advances only upon passing pre-committed decision gates, under declared execution assumptions, with degrees of freedom controlled to reduce selection bias.

## References

* [1]

  Robert Pardo.
  *The Evaluation and Optimization of Trading Strategies*.
  Wiley, 2nd edition, 2008.
* [2]

  David Aronson.
  *Evidence-Based Technical Analysis: Applying the Scientific Method and Statistical Inference to Trading Signals*.
  Wiley, 2006.
* [3]

  Marcos López de Prado.
  *Advances in Financial Machine Learning*.
  Wiley, 2018.
* [4]

  David H. Bailey, Jonathan M. Borwein, Marcos López de Prado, and Qiji Jim Zhu.
  The Probability of Backtest Overfitting.
  *Journal of Computational Finance*, 20(4):39–69, 2017.
* [5]

  Campbell R. Harvey, Yan Liu, and Heqing Zhu.
  … and the Cross-Section of Expected Returns.
  *Review of Financial Studies*, 29(1):5–68, 2016.
* [6]

  Halbert White.
  A Reality Check for Data Snooping.
  *Econometrica*, 68(5):1097–1126, 2000.
* [7]

  Peter R. Hansen.
  A Test for Superior Predictive Ability.
  *Journal of Business & Economic Statistics*, 23(4):365–380, 2005.
* [8]

  David H. Bailey and Marcos López de Prado.
  The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting, and Non-Normality.
  *Journal of Portfolio Management*, 40(5):94–107, 2014.
* [9]

  Robert Kissell.
  *The Science of Algorithmic Trading and Portfolio Management*.
  Academic Press/Elsevier, 2014.
* [10]

  Robert Almgren and Neil Chriss.
  Optimal Execution of Portfolio Transactions.
  *Journal of Risk*, 3(2):5–39, 2000.
* [11]

  Whitney K. Newey and Kenneth D. West.
  A Simple, Positive Semi-definite, Heteroskedasticity and Autocorrelation Consistent Covariance Matrix.
  *Econometrica*, 55(3):703–708, 1987.
* [12]

  William F. Sharpe.
  Mutual Fund Performance.
  *Journal of Business*, 39(1):119–138, 1966.

BETA