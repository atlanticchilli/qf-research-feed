---
authors:
- Rui Ma
doc_id: arxiv:2602.11020v1
family_id: arxiv:2602.11020
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source
  Financial Imaging'
url_abs: http://arxiv.org/abs/2602.11020v1
url_html: https://arxiv.org/html/2602.11020v1
venue: arXiv q-fin
version: 1
year: 2026
---


Rui Ma
  
Awakening of Insects Co., Ltd.
  
R&D
  
Xi’an, Shaanxi, China
  
marui182@mails.ucas.ac.cn
  
[ORCID: 0009-0002-0118-8351](https://orcid.org/0009-0002-0118-8351); Alumnus of the University of Chinese Academy of Sciences (UCAS).

###### Abstract

We study same-source multi-view learning and adversarial robustness for next-day direction prediction with financial image representations.
On Shanghai Gold Exchange (SGE) spot gold data (2005–2025), we construct two window-aligned views from each rolling window: an OHLCV-rendered price/volume chart and a technical-indicator matrix.
To ensure reliable evaluation, we adopt leakage-resistant time-block splits with embargo and use Matthews correlation coefficient (MCC).
We find that results depend strongly on the label-noise regime: we apply an *ex-post* minimum-movement filter that discards samples with realized |rt+1|<τ|r\_{t+1}|<\tau to define evaluation subsets with reduced near-zero label ambiguity.
This induces a non-monotonic data–noise trade-off that can reveal predictive signal but eventually increases variance as sample size shrinks; the filter is used for offline benchmark construction rather than an inference-time decision rule.
In the stabilized subsets, fusion is regime dependent: early fusion by channel stacking can exhibit negative transfer, whereas late fusion with dual encoders and a fusion head provides the dominant clean-performance gains; cross-view consistency regularization has secondary, backbone-dependent effects.
We further evaluate test-time ℓ∞\ell\_{\infty} perturbations using FGSM and PGD under two threat scenarios—view-constrained attacks that perturb one view and joint attacks that perturb both—and observe severe vulnerability at tiny budgets with strong view asymmetry.
Late fusion consistently improves robustness under view-constrained attacks, but joint attacks remain challenging and can still cause substantial worst-case degradation.

## 1 Introduction

More views do not imply more robustness by default.
Short-horizon financial prediction is notoriously difficult due to non-stationarity, heavy noise, and the ease with which evaluation can become overly optimistic under improper temporal splitting.
At the same time, an increasingly common practical approach is to convert market time series into *image-like* representations—such as OHLCV/candlestick charts or technical-indicator matrices—so that convolutional models can exploit local spatial patterns and cross-variable structure.
While such “financial vision” pipelines have reported promising results, two issues remain insufficiently clarified under a controlled and leakage-resistant evaluation:
*(i) when and why fusing multiple representations helps when the views are derived from the same underlying series*, and
*(ii) how robust these single-view and fused predictors are under worst-case input perturbations, especially when the input consists of multiple aligned views*.

This paper addresses these questions in a *same-source* multi-view setting for next-day direction prediction on Shanghai Gold Exchange (SGE) spot gold (2005–2025).
From each rolling lookback window, we deterministically construct two aligned 2D views: an OHLCV-rendered price/volume view (ohlcv) and a technical-indicator matrix view (indic), both rendered to a common resolution and aligned to the same window end date.
Unlike multi-source fusion where synchronization and provenance differences can confound results, our same-source design isolates the roles of representation choice and fusion strategy.

A key practical complication in next-day direction prediction is that labels can be dominated by near-zero moves, making the task effectively ambiguous and encouraging spurious correlations.
To make this regime explicit, we introduce a *minimum-movement* threshold and construct evaluation subsets by discarding samples whose realized next-day return magnitude is below τ\tau.
Importantly, this filtering uses the *realized* rt+1r\_{t+1} and is therefore an *ex-post* dataset construction step; it is used only to define label-noise regimes/subsets for controlled analysis and robustness benchmarking, not as a deployable rule available at prediction time.
Within the two-view setting (both), we compare *early fusion* via channel stacking against *late fusion* via dual encoders with a fusion head, and further consider cross-view consistency regularization using temperature-scaled symmetric KL.
All models are evaluated under a leakage-resistant time-block split with embargo to mitigate temporal leakage from overlapping windows (López de Prado, [2018](https://arxiv.org/html/2602.11020v1#bib.bib1)), and we use Matthews correlation coefficient (MCC) as the primary metric.

Beyond clean accuracy, we examine adversarial robustness of these financial-image predictors.
Small ℓ∞\ell\_{\infty}-bounded perturbations are known to induce systematic failures in vision models (Goodfellow et al., [2015](https://arxiv.org/html/2602.11020v1#bib.bib2); Madry et al., [2018](https://arxiv.org/html/2602.11020v1#bib.bib3)), and multi-branch architectures introduce additional threat-model choices: an adversary may perturb a single input stream or perturb all streams jointly.
Using an explicit view–channel mapping, we define a *view-aligned* robustness protocol that supports (i) *view-constrained* attacks that perturb exactly one view and (ii) *joint* attacks that perturb both views, enabling fair comparisons between single-view baselines and two-view models (Yang et al., [2021](https://arxiv.org/html/2602.11020v1#bib.bib4)).
We emphasize that pixel-space perturbations on rendered views serve as a *representation-level stress test* of worst-case sensitivity for the chosen rendering and fusion design, rather than a claim about realistic perturbations in the underlying market or data-generation process.

Our experiments yield several practical findings.
First, learnability hinges on label stabilization: without minimum-movement filtering (small τ\tau), most configurations hover around chance-level MCC, while moderate filtering unlocks predictive signal; overly strict filtering reduces effective sample size and increases variance, producing a non-monotonic data–noise trade-off.
Second, fusion is regime dependent: early fusion can exhibit negative transfer under noisier operating points, whereas late fusion provides a more reliable default once labels stabilize and accounts for the main clean-performance gains.
Third, naturally trained models are highly vulnerable under tiny ℓ∞\ell\_{\infty} budgets, and robustness is strongly view dependent: perturbing the indicator view can be particularly destructive for certain backbones.
Finally, late fusion consistently improves robustness under view-constrained attacks by preserving an unperturbed evidence path, but coordinated joint attacks remain challenging and can still induce substantial worst-case degradation; diagnostics further suggest that consistency regularization primarily enforces logit-level alignment, while predictive signal is largely expressed through the feature-level fusion pathway rather than strong standalone branch classifiers.

#### Contributions.

* •

  A unified, leakage-resistant evaluation setup for same-source two-view prediction.
  Inspired by prior rendering schemes (e.g., Gao et al. ([2022](https://arxiv.org/html/2602.11020v1#bib.bib5))), we build aligned ohlcv/indic views from SGE gold spot data and combine embargoed time-block splitting with MCC-based evaluation.
  To explicitly study label-noise regimes, we additionally report results under an *ex-post* minimum-movement subset definition (min\_move) based on realized |rt+1||r\_{t+1}|.
* •

  Regime-dependent analysis of fusion under label stabilization.
  We show multi-view gains are regime dependent: early fusion may underperform in noisier regimes,
  while late fusion is a stable default once labels stabilize and accounts for the main clean-performance gains.
* •

  Multi-view threat scenarios and a view-aligned robustness protocol.
  We formalize view–channel mapping and evaluate both view-constrained attacks and
  joint ℓ∞\ell\_{\infty} attacks (FGSM/PGD) that perturb both views, enabling fair,
  view-aligned robustness comparisons to single-view baselines (cf. Yang et al. ([2021](https://arxiv.org/html/2602.11020v1#bib.bib4))).
* •

  Diagnostics for late fusion and consistency.
  We report branch-level diagnostics (agreement, temperature-scaled symmetric KL,
  branch-wise vs. fused MCC) to interpret robustness trends and distinguish logit-level alignment
  from fused predictive power.

#### Organization.

We first describe the data, multi-view construction, task, and evaluation metrics, and then present the threat model and view-aligned robustness protocol in Section [4](https://arxiv.org/html/2602.11020v1#S4 "4 Threat Model and Evaluation Protocol ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging").
Clean baselines and the role of label stabilization and fusion paradigms are reported in Section [6.1](https://arxiv.org/html/2602.11020v1#S6.SS1 "6.1 Clean Baselines ‣ 6 Results ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging"), followed by adversarial robustness results in Section [6.2](https://arxiv.org/html/2602.11020v1#S6.SS2 "6.2 Adversarial Robustness ‣ 6 Results ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging").
We conclude with discussion and implications in Section [7](https://arxiv.org/html/2602.11020v1#S7 "7 Discussion ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging").

#### Code availability.

Code will be released upon acceptance/publication at: <https://github.com/mrui166/same-source-financial-imaging-robustness>.

## 2 Related Work

### 2.1 Financial Image Representations and Multi-View Fusion for Market Prediction

A common line of work in market prediction converts financial time series into 2D visual representations so that convolutional models can exploit local spatial patterns and cross-variable structures.
Typical examples include candlestick-/OHLCV-style charts and chart-pattern based encodings, as well as indicator-driven matrices/heatmaps constructed from technical signals.
Beyond ad-hoc chart rendering, a more principled “time-series-to-image” family encodes temporal structure into images such as Gramian Angular Fields and Markov Transition Fields, enabling multi-channel image learning from a single sequence (Wang and Oates, [2015](https://arxiv.org/html/2602.11020v1#bib.bib6)).
In financial settings, such imaging ideas have been instantiated in different ways, including technical-indicator image grids for trading (Sezer and Ozbayoglu, [2020a](https://arxiv.org/html/2602.11020v1#bib.bib7)), bar-/chart-window image learners (Sezer and Ozbayoglu, [2020b](https://arxiv.org/html/2602.11020v1#bib.bib8); Jiang et al., [2023](https://arxiv.org/html/2602.11020v1#bib.bib9)), and candlestick-pattern imaging for CNN-based recognition (Chen and Tsai, [2020](https://arxiv.org/html/2602.11020v1#bib.bib10)).
Related work also considers incorporating cross-asset market structure via graph-enhanced predictors, e.g., a graph convolutional feature based CNN for stock trend prediction (Chen et al., [2021](https://arxiv.org/html/2602.11020v1#bib.bib11)).
Recent surveys often group multi-source fusion methods for financial market prediction by when fusion is applied—pre-model (early/data), mid-model, or post-model (late/decision)—and note that predictive performance can be sensitive to this choice (Mehrmolaei and Saniee Abadeh, [2025](https://arxiv.org/html/2602.11020v1#bib.bib12)).
Related strands also explore learning from different representations of the *same* underlying data, sometimes fusing them (e.g., feature-level fusion in hybrid CNN–RNN pipelines) (Kim and Kim, [2019](https://arxiv.org/html/2602.11020v1#bib.bib13)) or incorporating pattern-based representations such as candlesticks and sequence similarity (Liang et al., [2022](https://arxiv.org/html/2602.11020v1#bib.bib14)).

Within this landscape, our two-view construction follows the multi-view intuition that complementary representations can provide partially redundant evidence.
We therefore treat complementarity as an empirical question and explicitly analyze regime dependence under label-stabilization settings (via a minimum-movement threshold).
In particular, we adopt an OHLCV-rendered view that preserves price-action/volume cues and an indicator-matrix view that emphasizes trend/momentum signals; our same-source two-view design is inspired by prior multi-source image-integration approaches in financial forecasting (Gao et al., [2022](https://arxiv.org/html/2602.11020v1#bib.bib5)), while our focus is on the same-source case to remove cross-source alignment confounds.
We focus on a *same-source* setting where both views are deterministically derived from an aligned rolling window of a single market time series (SGE gold spot), which isolates the role of representation and fusion from confounding cross-source alignment issues.

A key practical takeaway from prior fusion work is that multi-view learning is not automatically beneficial: gains depend on whether the views are complementary and on careful representation alignment and fusion design (Baltrusaitis et al., [2019](https://arxiv.org/html/2602.11020v1#bib.bib15); Rahate et al., [2022](https://arxiv.org/html/2602.11020v1#bib.bib16)).
More broadly, financial forecasting pipelines are also prone to subtle time leakage (e.g., through rolling normalization, window overlap, or hyperparameter search) and selection effects from repeated backtests; protocol designs such as purged CV/embargo and diagnostics such as PBO/DSR have been advocated to diagnose and quantify these risks (López de Prado, [2018](https://arxiv.org/html/2602.11020v1#bib.bib1); Bailey et al., [2017](https://arxiv.org/html/2602.11020v1#bib.bib17); Bailey and López de Prado, [2014](https://arxiv.org/html/2602.11020v1#bib.bib18)). Related concerns about leakage undermining benchmark validity have also been discussed in other areas (e.g., benchmark reinforcement against memorization in LLM QA) (Fang et al., [2025](https://arxiv.org/html/2602.11020v1#bib.bib19)), reinforcing the general point that evaluation reliability depends on making leakage assumptions explicit.
Motivated by this, our study emphasizes a controlled comparison between early fusion (channel stacking) and late fusion (dual encoders with a fusion head), and interprets gains in an *evaluation-reliability–oriented* context of leakage-resistant time splits (Section [5.4](https://arxiv.org/html/2602.11020v1#S5.SS4 "5.4 Leakage-Resistant Time Split with Embargo ‣ 5 A Stable, Leakage-Resistant Training Baseline ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging")) and label-stabilization regimes (Section [5.3](https://arxiv.org/html/2602.11020v1#S5.SS3 "5.3 Stabilizing Labels with a Minimum-Movement Threshold ‣ 5 A Stable, Leakage-Resistant Training Baseline ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging")).
Many closely related financial-imaging papers report improvements under relatively controlled evaluation, whereas we center the analysis on *evaluation protocol choices* (e.g., leakage control, operating-point selection) and *fusion paradigms* as first-class factors that shape reliability.

### 2.2 Adversarial Robustness and Threat Models for Multi-View Inputs

Adversarial robustness has been extensively studied in vision, where small ℓ∞\ell\_{\infty}-bounded perturbations can induce systematic misclassification (Szegedy et al., [2014](https://arxiv.org/html/2602.11020v1#bib.bib20); Goodfellow et al., [2015](https://arxiv.org/html/2602.11020v1#bib.bib2)).
Canonical first-order attacks include FGSM (Goodfellow et al., [2015](https://arxiv.org/html/2602.11020v1#bib.bib2)) and multi-step PGD (Madry et al., [2018](https://arxiv.org/html/2602.11020v1#bib.bib3)), which have become standard stress tests for probing worst-case sensitivity under first-order adversaries.
Beyond generic vision benchmarks, a smaller but growing line of work considers adversarial sensitivity in *financial vision* models built on chart-like representations.
For example, Chen et al. study adversarial robustness of a deep convolutional candlestick learner built on Gramian Angular Fields (GAF) encodings and propose perturbation sampling/adversarial training to improve stability under structured perturbations of candlestick inputs (Chen et al., [2020](https://arxiv.org/html/2602.11020v1#bib.bib21)).
These studies are complementary to ours: they focus on candlestick-pattern classification and representation-specific attacks/defenses, whereas we evaluate next-day direction prediction under leakage-resistant time splits and explicitly compare view-constrained vs. joint threat models for same-source two-view fusion.
Beyond single-input settings, robustness questions also arise for multi-branch and multimodal models, where the threat model can be defined per input stream (single-source/view-constrained attacks), and where fusion architecture can modulate robustness and failure modes (Yang et al., [2021](https://arxiv.org/html/2602.11020v1#bib.bib4)).
In our setting, we evaluate an inference-time, white-box, untargeted FGSM/PGD threat model instantiated as raw pixel-space ℓ∞\ell\_{\infty}-bounded perturbations on rendered views, with optional standardized-space execution via budget conversion that preserves the underlying raw-space constraint.
We emphasize that this pixel-space threat model is a *representation-level stress test* of worst-case sensitivity for the chosen rendering and fusion design, rather than a claim about a realistic financial adversary operating in the underlying market or data-generation process.

Time-series settings introduce additional subtleties: perturbations can be defined either in the raw temporal domain or on downstream representations (e.g., rendered images), and the choice determines what “small” means and which invariances are being tested.
Prior work has instantiated adversarial attacks directly on time-series classifiers and shown that standard gradient-based methods can transfer to temporal signals (Fawaz et al., [2019](https://arxiv.org/html/2602.11020v1#bib.bib22)).
In financial pipelines, where inputs often undergo deterministic preprocessing (windowing, indicator computation, normalization), robustness evaluation therefore benefits from threat models that explicitly account for *where* perturbations are applied and *how* multi-view inputs are aligned.

Our work aligns with this perspective by treating pixel-space ℓ∞\ell\_{\infty} perturbations on rendered views as a representation-level stress test, and by formalizing the multi-view attack surface through view–channel mapping.
This enables (i) view-constrained perturbations that target exactly one view in two-view models and (ii) joint perturbations that attack both views, while maintaining a view-aligned comparison to single-view baselines.
Such protocols help disentangle robustness contributions from (a) the chosen representation, (b) early vs. late fusion, and (c) auxiliary alignment objectives (e.g., cross-view consistency), while reducing confounds from data-splitting artifacts or cross-source misalignment.

## 3 Problem Setup and Notation

### 3.1 Same-Source Data (SGE Gold Spot)

Source. Shanghai Gold Exchange (SGE), spot gold; data retrieved via Tushare (Tushare, [2025](https://arxiv.org/html/2602.11020v1#bib.bib23)).
  
Time range. 2005-09-26–2025-08-28.
  
Time zone normalization. All timestamps are converted from Shanghai time (UTC+8) to UTC.
  
Granularity. Trading-day level observations (non-trading days excluded; trading days follow the SGE calendar).
  
Fields. Price and trading activity information (OHLC and trading volume).
  
Preprocessing. We remove invalid records, sort the data chronologically, and construct rolling lookback windows. Both image views used in our experiments are generated from the same window and aligned to the same window end date.

### 3.2 Multi-View Construction

Motivated by the multi-view formulation in MODII (Gao et al., [2022](https://arxiv.org/html/2602.11020v1#bib.bib5)), we construct two complementary 2D image views from a single market data source: (i) an OHLCV-based price/volume view and (ii) a technical-indicator view. This multi-representation design enables CNNs to capture local temporal patterns and cross-variable structures.
Both views are constructed from the same reference day and aligned to the same 15-day lookback window.

#### OHLCV images.

Motivated by the OHLCV view used in MODII (Gao et al., [2022](https://arxiv.org/html/2602.11020v1#bib.bib5)), we construct an OHLCV image view (denoted as ohlcv) from the open, high, low, and close prices together with trading volume within a fixed lookback window of length Lohlcv=15L\_{\mathrm{ohlcv}}=15 trading days.
Each image is rendered on a black canvas at a fixed resolution of 256×256256\times 256 pixels.
The top region (75% of the height) depicts OHLC bars (high–low vertical strokes with open/close ticks), and we further highlight the intraday price interval by shading the open–close range in gray. This design is motivated by the interval-valued perspective that an interval observation can carry richer information (range and level/trend) than a point observation (Han et al., [2012](https://arxiv.org/html/2602.11020v1#bib.bib24)).
The bottom region (25% of the height) encodes volume as a bar chart, where volumes are normalized by a rolling percentile-based scaler (divided by the trailing 95th percentile computed from a fixed-length reference window) and clipped to [0,1][0,1].

#### Indicator images.

To complement the price view with trend and momentum cues beyond raw OHLCV, we construct an indicator-image view (indic) by converting recent technical-indicator trajectories into an image-like matrix.
We adopt a MODII-style construction pipeline (Gao et al., [2022](https://arxiv.org/html/2602.11020v1#bib.bib5)), which is conceptually related to earlier time-series-to-image conversions for financial trading (Sezer and Ozbayoglu, [2020a](https://arxiv.org/html/2602.11020v1#bib.bib7)).
Specifically, we compute a fixed set of N=15N=15 standard indicators over a lookback window of Lindic=15L\_{\mathrm{indic}}=15 trading days.
Indicator choices and parameters are fixed *a priori*; we do not search over indicator sets or tune parameters using validation/test performance.
For each sample, we stack the most recent LindicL\_{\mathrm{indic}} values of each indicator into a N×LindicN\times L\_{\mathrm{indic}} grayscale matrix (indicators on the vertical axis, time on the horizontal axis), and apply per-row min–max scaling to [0,255][0,255] within the current window.
We then reorder indicator rows using a correlation-based ranking computed on the training split and keep this order fixed for validation/test.
Finally, the 15×1515\times 15 matrix is upsampled with nearest-neighbor interpolation to a fixed 256×256256\times 256 canvas (to match the image encoder input size) and rendered as a grayscale image.

![Refer to caption](figs/ohlcv.png)

![Refer to caption](figs/indic.png)

Figure 1: Examples of ohlcv and indic constructed from a fixed lookback window of Lohlcv=Lindic=15L\_{\mathrm{ohlcv}}=L\_{\mathrm{indic}}=15 trading days.

### 3.3 View-to-Channel Mapping

For models that take both views as input (denoted as both), we concatenate the two images along the channel dimension.
Specifically, we map the OHLCV image view ohlcv to channel 0 (ch0) and the indicator image view indic to channel 1 (ch1).
Thus, each sample for a both model is represented as a two-channel input tensor
𝐱=[vohlcv;vindic]∈ℝ2×256×256\mathbf{x}=[v\_{\texttt{ohlcv}};v\_{\texttt{indic}}]\in\mathbb{R}^{2\times 256\times 256}.

We also consider single-view baselines that take only one view as input, denoted as ohlcv or indic.
In these cases, the input has a single channel 𝐱∈ℝ1×256×256\mathbf{x}\in\mathbb{R}^{1\times 256\times 256} and only ch0 exists (i.e., the provided view is always placed in ch0).
This convention is important for our robustness evaluation: *two-view models* allow perturbations to target ch0, ch1, or both channels, whereas *single-view models* can only be perturbed through ch0.
This view–channel mapping allows us to define *channel-constrained* perturbations that target a specific view in the two-view setting, while keeping comparisons with single-view baselines well-defined.

### 3.4 Task and Evaluation Metrics

#### Prediction target.

For each trading day tt, we form an input sample by extracting a lookback window of the past LL trading days,
{t−L+1,…,t}\{t-L+1,\dots,t\}, and predict the next-day directional movement at (t+1)(t+1).
We define the next-day simple return as

|  |  |  |  |
| --- | --- | --- | --- |
|  | rt+1=c​l​o​s​et+1−c​l​o​s​etc​l​o​s​et,yt=𝕀​(rt+1>0),r\_{t+1}=\frac{close\_{t+1}-close\_{t}}{close\_{t}},\qquad y\_{t}=\mathbb{I}\!\left(r\_{t+1}>0\right), |  | (1) |

where c​l​o​s​etclose\_{t} denotes the closing price on day tt and 𝕀​(⋅)\mathbb{I}(\cdot) is the indicator function.
Thus, the task is a binary classification problem with labels yt∈{0,1}y\_{t}\in\{0,1\}.

#### Matthews Correlation Coefficient (MCC).

We use MCC as the primary metric because it summarizes the full confusion matrix and remains informative under class imbalance (Matthews, [1975](https://arxiv.org/html/2602.11020v1#bib.bib25)).
MCC can be interpreted as a correlation between predicted and true labels, taking values in [−1,1][-1,1].

|  |  |  |  |
| --- | --- | --- | --- |
|  | MCC=T​P⋅T​N−F​P⋅F​N(T​P+F​P)​(T​P+F​N)​(T​N+F​P)​(T​N+F​N).\mathrm{MCC}=\frac{TP\cdot TN-FP\cdot FN}{\sqrt{(TP+FP)(TP+FN)(TN+FP)(TN+FN)}}. |  | (2) |

We report mean±\pmstd over multiple fixed random seeds (Appendix [C](https://arxiv.org/html/2602.11020v1#A3 "Appendix C Additional Evaluation Details ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging")).

## 4 Threat Model and Evaluation Protocol

We study adversarial robustness under *test-time adversarial perturbations* (evasion attacks).
Given a fixed trained model and an input sample, an adversary perturbs the input image(s) within a small budget to induce misclassification.

### 4.1 Threat Model

#### ℓ∞\ell\_{\infty}-bounded perturbations (defined in raw pixel space).

Let 𝐱raw∈[0,1]C×256×256\mathbf{x}\_{\mathrm{raw}}\in[0,1]^{C\times 256\times 256} denote the raw input after scaling 8-bit images to [0,1][0,1] (with C=1C=1 for single-view and C=2C=2 for two-view).
The adversary outputs 𝐱raw′=𝐱raw+𝜹\mathbf{x}^{\prime}\_{\mathrm{raw}}=\mathbf{x}\_{\mathrm{raw}}+\boldsymbol{\delta} subject to (Szegedy et al., [2014](https://arxiv.org/html/2602.11020v1#bib.bib20); Goodfellow et al., [2015](https://arxiv.org/html/2602.11020v1#bib.bib2); Madry et al., [2018](https://arxiv.org/html/2602.11020v1#bib.bib3))

|  |  |  |  |
| --- | --- | --- | --- |
|  | ‖𝜹‖∞≤ϵadv,‖𝜹‖∞≜maxi⁡|δi|.\|\boldsymbol{\delta}\|\_{\infty}\leq\epsilon\_{\mathrm{adv}},\qquad\|\boldsymbol{\delta}\|\_{\infty}\triangleq\max\_{i}|\delta\_{i}|. |  | (3) |

We evaluate budgets

|  |  |  |  |
| --- | --- | --- | --- |
|  | E={0,0.25255,0.5255,0.75255,1255},E=\left\{0,\ \frac{0.25}{255},\ \frac{0.5}{255},\ \frac{0.75}{255},\ \frac{1}{255}\right\}, |  | (4) |

where ϵadv=0\epsilon\_{\mathrm{adv}}=0 corresponds to clean evaluation.

#### Optional standardization.

Optionally, the model consumes a standardized input

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐱norm=(𝐱raw−𝝁)⊘𝝈,\mathbf{x}\_{\mathrm{norm}}=(\mathbf{x}\_{\mathrm{raw}}-\boldsymbol{\mu})\oslash\boldsymbol{\sigma}, |  | (5) |

with (𝝁,𝝈)(\boldsymbol{\mu},\boldsymbol{\sigma}) estimated on the training split.
The threat model remains defined in raw space; when attacks are executed in standardized space, we use the equivalent budgets

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϵnorm=ϵadv⊘𝝈,αnorm=α⊘𝝈,\epsilon\_{\mathrm{norm}}=\epsilon\_{\mathrm{adv}}\oslash\boldsymbol{\sigma},\qquad\alpha\_{\mathrm{norm}}=\alpha\oslash\boldsymbol{\sigma}, |  | (6) |

so that the underlying raw-space constraint in Eq. [3](https://arxiv.org/html/2602.11020v1#S4.E3 "In ℓ_∞-bounded perturbations (defined in raw pixel space). ‣ 4.1 Threat Model ‣ 4 Threat Model and Evaluation Protocol ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging") is preserved.
We clip perturbed inputs to the valid range [0,1][0,1] (or to
[(0−𝝁)⊘𝝈,(1−𝝁)⊘𝝈]\big[(0-\boldsymbol{\mu})\oslash\boldsymbol{\sigma},\ (1-\boldsymbol{\mu})\oslash\boldsymbol{\sigma}\big]
when operating in standardized space).

#### Attacks (untargeted CE).

We consider FGSM (one-step) (Goodfellow et al., [2015](https://arxiv.org/html/2602.11020v1#bib.bib2)) and PGD (multi-step with projection onto the ℓ∞\ell\_{\infty} ball) (Madry et al., [2018](https://arxiv.org/html/2602.11020v1#bib.bib3)).
Both attacks are *untargeted* and maximize the cross-entropy loss with respect to the true label,
thereby increasing the likelihood of misclassification.
FGSM performs a single update followed by clipping to the valid range.
PGD uses K=10K=10 iterations with step size α=ϵadv/K\alpha=\epsilon\_{\mathrm{adv}}/K and projection after each step; we disable random initialization (random\_start=False).
We note that disabling random start can underestimate worst-case PGD strength; we therefore interpret PGD results in this paper as a consistent, reproducible first-order stress test rather than an exhaustive maximization over random restarts.
Full attack hyperparameters are reported in Appendix [D](https://arxiv.org/html/2602.11020v1#A4 "Appendix D Attack Hyperparameters and Implementation Notes ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging").

### 4.2 Threat Scenarios and View-Aligned Protocol

Using the view–channel mapping (Section [3.3](https://arxiv.org/html/2602.11020v1#S3.SS3 "3.3 View-to-Channel Mapping ‣ 3 Problem Setup and Notation ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging")), we evaluate:

#### View-constrained perturbations.

For two-view inputs, the adversary perturbs exactly one channel (one view) (Yang et al., [2021](https://arxiv.org/html/2602.11020v1#bib.bib4)):

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜹=(δch0,𝟎)​(attack ohlcv)or𝜹=(𝟎,δch1)​(attack indic).\boldsymbol{\delta}=(\delta\_{\texttt{ch0}},\mathbf{0})\ \text{(attack {ohlcv})}\quad\text{or}\quad\boldsymbol{\delta}=(\mathbf{0},\delta\_{\texttt{ch1}})\ \text{(attack {indic})}. |  | (7) |

#### Joint perturbations.

For two-view inputs, the adversary perturbs both channels:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝜹=(δch0,δch1).\boldsymbol{\delta}=(\delta\_{\texttt{ch0}},\delta\_{\texttt{ch1}}). |  | (8) |

#### Fair comparison (view-aligned evaluation).

Single-view models have only one channel and place the provided view in ch0.
Therefore, we align comparisons by the *attacked view* rather than the channel index:
(i) ohlcv: single-view ohlcv attacked on ch0 vs. two-view both attacked on ch0;
(ii) indic: single-view indic attacked on ch0 vs. two-view both attacked on ch1.
Joint perturbations are evaluated only for two-view models.

### 4.3 Evaluation and Summary Metrics

We report robustness curves MCC​(ϵadv)\mathrm{MCC}(\epsilon\_{\mathrm{adv}}) for ϵadv∈E\epsilon\_{\mathrm{adv}}\in E (mean±\pmstd over random seeds), where binary predictions are obtained by thresholding the positive-class probability at 0.50.5 unless stated otherwise.
To summarize robustness across budgets, we report the worst-case degradation over nonzero budgets:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​(ϵadv)=MCC​(ϵadv)−MCC​(0),Δworst=minϵadv∈E,ϵadv>0⁡Δ​(ϵadv).\Delta(\epsilon\_{\mathrm{adv}})=\mathrm{MCC}(\epsilon\_{\mathrm{adv}})-\mathrm{MCC}(0),\qquad\Delta\_{\mathrm{worst}}=\min\_{\epsilon\_{\mathrm{adv}}\in E,\ \epsilon\_{\mathrm{adv}}>0}\Delta(\epsilon\_{\mathrm{adv}}). |  | (9) |

#### Diagnostic metrics for two-view models.

For late-fusion two-view models, we additionally report diagnostic statistics on the clean test set to interpret robustness trends.
Specifically, we measure (i) cross-branch agreement and symmetric KL between the two branch predictive distributions, and
(ii) branch-wise MCC (computed from each branch alone) versus the fused-head MCC.
These diagnostics are used for analysis only and do not affect model selection.

## 5 A Stable, Leakage-Resistant Training Baseline

We consider a set of learning and non-learning baselines to evaluate the effectiveness of our data-to-image representations under the same leakage-resistant time-block split protocol. All models perform binary classification for next-day direction prediction and output class logits/probabilities. Depending on the input mode, we use either a single image view (indic or ohlcv) or a two-view input (both) formed by channel-wise stacking after resizing to a common resolution.
Unless otherwise stated, all trainable baselines share the same optimization setup, and we select the best checkpoint based on the validation metric.

### 5.1 Model Architectures

#### Compact CNN baseline (Lite-CNN).

Our first baseline is a lightweight convolutional network adapted from the MODII framework (Gao et al., [2022](https://arxiv.org/html/2602.11020v1#bib.bib5)).
It follows a shallow CNN design with a small number of convolution and pooling stages to extract local visual patterns from the image representation, followed by a compact MLP classifier head.
In the two-view mode (both), we adopt early fusion by channel-wise stacking the two resized views as the input.
This model provides a lightweight literature baseline adapted from MODII, enabling a direct comparison under our evaluation protocol.

#### Pretrained ResNet-18 baseline (ResNet18-P).

To benchmark against a more expressive architecture, we employ a ResNet-18 backbone initialized with ImageNet pretrained weights (He et al., [2016](https://arxiv.org/html/2602.11020v1#bib.bib26); Deng et al., [2009](https://arxiv.org/html/2602.11020v1#bib.bib27)).
The first layer is adapted to support the required number of input channels in each input mode, while the remaining network structure is kept unchanged.
In the two-view mode (both), we adopt early fusion by channel-wise stacking the two resized views as the input.
This model offers an architecture-level comparison between shallow and deeper CNN backbones under identical settings.

#### Dual-view consistency variants (\*-cons).

In the two-view mode (both), we additionally consider dual-branch late-fusion variants for both backbones, denoted Lite-CNN-Cons and ResNet18-P-Cons.
Unlike the early-fusion Lite-CNN/ResNet18-P baselines, \*-cons uses dual-branch late fusion.
We report three settings for each: λ∈{0,0.5,1}\lambda\in\{0,0.5,1\}, where λ=0\lambda=0 disables the consistency term (fused-logit cross-entropy only) and λ>0\lambda>0 enables cross-view consistency regularization in Sec. [5.2](https://arxiv.org/html/2602.11020v1#S5.SS2 "5.2 Cross-view Consistency Regularization ‣ 5 A Stable, Leakage-Resistant Training Baseline ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging").
Unless otherwise stated, we fix T=2.0T=2.0.

#### Logistic Regression baseline (LogReg).

As a traditional machine-learning baseline, we apply logistic regression on flattened image features.
We standardize features and train a linear classifier, which quantifies the extent to which the task can be solved by linear decision boundaries on the constructed representations, without relying on hierarchical spatial feature extraction.

#### Majority-class (non-learning) baseline (Majority).

We include a non-learning baseline that predicts the single most frequent label computed from the *training* split.
Formally, let y⋆=arg⁡maxc⁡#​{i:yi=c,(xi,yi)∈𝒟train}y^{\star}=\arg\max\_{c}\#\{i:y\_{i}=c,\ (x\_{i},y\_{i})\in\mathcal{D}\_{\text{train}}\}; the predictor outputs y⋆y^{\star} for every input at evaluation time.
This baseline has no trainable parameters and serves as a strict lower bound (sanity check) to contextualize gains from learned models.

For reproducibility, implementation details of backbones and fusion heads are provided in Appendix [B](https://arxiv.org/html/2602.11020v1#A2 "Appendix B Model Architecture and Fusion Details ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging").

### 5.2 Cross-view Consistency Regularization

#### Motivation.

In the two-view setting (both), each sample provides two aligned image views that describe the same market state (e.g., indic and ohlcv) and share the same next-day direction label.
While the two views may emphasize different aspects of the input, their predictions should remain coherent.
We therefore introduce a consistency regularizer that encourages agreement between the two view-specific branch predictors.

#### Dual-branch predictors.

For a two-view input, we employ a dual-branch architecture.
Let the branch-specific predictors produce logits zaz\_{a} and zbz\_{b} from the two views, and let a fusion head produce fused logits zfz\_{f} from the concatenated branch features.
We use zfz\_{f} as the primary output for the supervised objective, while zaz\_{a} and zbz\_{b} are used to define the consistency term.

#### Temperature-scaled symmetric KL.

We define temperature-scaled predictive distributions (Hinton et al., [2015](https://arxiv.org/html/2602.11020v1#bib.bib28); Zhang et al., [2018](https://arxiv.org/html/2602.11020v1#bib.bib29))

|  |  |  |  |
| --- | --- | --- | --- |
|  | pa=softmax​(za/T),pb=softmax​(zb/T),p\_{a}=\mathrm{softmax}(z\_{a}/T),\qquad p\_{b}=\mathrm{softmax}(z\_{b}/T), |  | (10) |

where T>0T>0 is a temperature parameter.
Our consistency loss is a symmetric KL divergence:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒcons​(za,zb)=T22​[KL​(pa∥pb)+KL​(pb∥pa)],\mathcal{L}\_{\mathrm{cons}}(z\_{a},z\_{b})=\frac{T^{2}}{2}\Big[\mathrm{KL}(p\_{a}\,\|\,p\_{b})+\mathrm{KL}(p\_{b}\,\|\,p\_{a})\Big], |  | (11) |

where pa=softmax​(za/T)p\_{a}=\mathrm{softmax}(z\_{a}/T) and pb=softmax​(zb/T)p\_{b}=\mathrm{softmax}(z\_{b}/T).

#### Training objective.

For the dual-branch two-view model, given the ground-truth label y∈{0,1}y\in\{0,1\}, we optimize

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ=ℒCE​(zf,y)+λ​ℒcons​(za,zb),\mathcal{L}=\mathcal{L}\_{\mathrm{CE}}(z\_{f},y)+\lambda\,\mathcal{L}\_{\mathrm{cons}}(z\_{a},z\_{b}), |  | (12) |

where ℒCE\mathcal{L}\_{\mathrm{CE}} is the standard cross-entropy loss on the fused logits and λ≥0\lambda\geq 0 controls the strength of consistency regularization.

#### Implementation notes.

We compute the KL terms using numerically stable log\_softmax and softmax operations.
To verify that the regularizer indeed changes cross-view predictions, we monitor cross-branch agreement and symmetric KL on the clean test set.
We also report branch-wise MCC to distinguish whether gains (or failures) come from stronger branches or from the fusion head.

### 5.3 Stabilizing Labels with a Minimum-Movement Threshold

Next-day direction labels can be noisy when the realized price change is extremely small.
To explicitly study how label ambiguity affects fusion and robustness, we optionally construct *ex-post* evaluation subsets using a minimum-movement threshold τ\tau.
Specifically, for each sample ending at day tt, we compute the realized next-day return rt+1r\_{t+1} as in Eq. [1](https://arxiv.org/html/2602.11020v1#S3.E1 "In Prediction target. ‣ 3.4 Task and Evaluation Metrics ‣ 3 Problem Setup and Notation ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging") and discard the sample if |rt+1|<τ|r\_{t+1}|<\tau.
We evaluate τ∈{0, 0.002, 0.004, 0.006, 0.008, 0.010}\tau\in\{0,\,0.002,\,0.004,\,0.006,\,0.008,\,0.010\} (denoted as min\_move).

#### Protocol note (label-dependent selection).

Because inclusion depends on the *realized* |rt+1||r\_{t+1}|, min\_move is a label-dependent sample-selection step and therefore changes the task from unconditional next-day direction prediction to *direction prediction conditional on |rt+1|≥τ|r\_{t+1}|\geq\tau*.
This filtering cannot be applied as an inference-time rule and should not be interpreted as a deployable trading decision.
We use it solely to define controlled label-noise regimes for offline benchmarking of fusion behavior and adversarial robustness.
To ensure comparability across split variants, filtering is performed before splitting, and all split variants operate on the same subset definition.

### 5.4 Leakage-Resistant Time Split with Embargo

Since our inputs are constructed from overlapping sliding windows, proportional random splitting can introduce look-ahead leakage and overly optimistic evaluation; we therefore adopt a leakage-resistant time-block split with embargo for all models (López de Prado, [2018](https://arxiv.org/html/2602.11020v1#bib.bib1)).
Trading days are ordered in time and grouped into consecutive blocks of BB trading days (block\_size); the earliest blocks form the training set, followed by validation blocks, and the latest blocks form the test set.
Unless stated otherwise, we use a 70/15/15 split by blocks for train/validation/test.

To mitigate boundary leakage caused by overlapping windows across split boundaries, we apply an embargo of at least DembD\_{\mathrm{emb}} trading days (embargo\_days) around boundaries (López de Prado, [2018](https://arxiv.org/html/2602.11020v1#bib.bib1); Racine, [2000](https://arxiv.org/html/2602.11020v1#bib.bib30)).
In practice, we enforce the embargo at the block level by dropping K=⌈Demb/B⌉K=\lceil D\_{\mathrm{emb}}/B\rceil adjacent blocks to create a temporal gap of at least DembD\_{\mathrm{emb}} days (possibly larger due to block granularity).
To keep the test period as intact as possible, we apply a symmetric embargo at the train/validation boundary (dropping KK blocks from each side) and primarily drop validation-side blocks at the validation/test boundary.
Table [1](https://arxiv.org/html/2602.11020v1#S5.T1 "Table 1 ‣ 5.4 Leakage-Resistant Time Split with Embargo ‣ 5 A Stable, Leakage-Resistant Training Baseline ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging") summarizes the resulting sample sizes after alignment and min\_move filtering, as well as the additional sample reduction induced by the embargo under the same split configuration (block\_size=30, embargo\_days=20).
We report the corresponding split date ranges in the appendix.

Table 1: Impact of min\_move filtering and embargo under the time-block split protocol (block\_size=30, embargo\_days=20). *Aligned* denotes samples after filtering and view alignment, and *Used* denotes samples retained after applying the embargo split.

| min\_move | Aligned | Train/Val/Test | Used | Embargo Loss |
| --- | --- | --- | --- | --- |
| 0.000 | 4842 | 3390/660/702 | 4752 | 1.86% |
| 0.002 | 3666 | 2580/480/516 | 3576 | 2.45% |
| 0.004 | 2696 | 1890/330/386 | 2606 | 3.34% |
| 0.006 | 1989 | 1380/240/279 | 1899 | 4.52% |
| 0.008 | 1471 | 1050/150/181 | 1381 | 6.12% |
| 0.010 | 1054 | 750/90/124 | 964 | 8.54% |

### 5.5 Implementation Details

All trainable baselines are implemented in PyTorch and trained under a unified optimization and selection protocol unless stated otherwise.
We use AdamW and select the final checkpoint by the chosen validation objective (default: MCC at threshold 0.5)., reporting mean±\pmstd over multiple random seeds.

#### Data loading and normalization.

All images are resized to 256×256256\times 256 and loaded as tensors in [0,1][0,1].
When enabled (use\_norm), we apply per-channel standardization using (𝝁,𝝈)(\boldsymbol{\mu},\boldsymbol{\sigma}) estimated from the training split only, avoiding information leakage from validation/test.
Two-view inputs follow the view-to-channel mapping in Sec. [3.3](https://arxiv.org/html/2602.11020v1#S3.SS3 "3.3 View-to-Channel Mapping ‣ 3 Problem Setup and Notation ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging").

#### Training protocol and leakage control.

We apply min\_move filtering (as an offline subset definition) before splitting (Sec. [5.3](https://arxiv.org/html/2602.11020v1#S5.SS3 "5.3 Stabilizing Labels with a Minimum-Movement Threshold ‣ 5 A Stable, Leakage-Resistant Training Baseline ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging")) and use the leakage-resistant time-block split with embargo (Sec. [5.4](https://arxiv.org/html/2602.11020v1#S5.SS4 "5.4 Leakage-Resistant Time Split with Embargo ‣ 5 A Stable, Leakage-Resistant Training Baseline ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging")), keeping the *test time range* fixed across experimental comparisons (keep\_test\_intact=True).
Unless stated otherwise, we keep the training hyperparameters (e.g., batch size and dropout) fixed across model/configuration comparisons.

#### Early stopping.

We train for at most 40 epochs with early stopping (patience=8).
To ensure stable optimization across backbones, we use a model-dependent minimum training epoch:
min\_epoch=15 for Lite-CNN and Lite-CNN-cons, and min\_epoch=2 for ResNet18-P and ResNet18-P-cons.

#### Adversarial evaluation.

Adversarial evaluation is performed at test time only.
We consider FGSM (one-step) and PGD (untargeted cross-entropy), and for PGD we use K=10K=10 steps with α=ϵadv/K\alpha=\epsilon\_{\mathrm{adv}}/K and disable random initialization (random\_start=False).
We evaluate both view-constrained and joint perturbations under the view-aligned protocol in Sec. [4.2](https://arxiv.org/html/2602.11020v1#S4.SS2 "4.2 Threat Scenarios and View-Aligned Protocol ‣ 4 Threat Model and Evaluation Protocol ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging").

#### Reproducibility.

We fix random seeds for Python, NumPy, and PyTorch and log the full configuration of each run, including the selected checkpoint.

## 6 Results

### 6.1 Clean Baselines

![Refer to caption](x1.png)

![Refer to caption](x2.png)

Figure 2: Baseline MCC vs. minimum-movement threshold τ\tau (mean±\pmstd).
Top: Lite-CNN family. Bottom: ResNet18-P family.
Deep models are averaged over n=8n{=}8 random seeds; Majority and LogReg are run once (n=1n{=}1).

#### Setup and evaluation metric.

We compare a non-learning Majority baseline, a linear Logistic Regression (LogReg) baseline, and two CNN backbones (Lite-CNN and ResNet18-P) under three input modes: ohlcv, indic, and the dual-view both.
For both, the vanilla CNN baselines use *early fusion* via channel-wise stacking, whereas \*-cons variants use a dual-branch *late fusion* head and optionally add cross-view consistency regularization weighted by λ\lambda.
Throughout the paper, we use Matthews correlation coefficient (MCC) as the *primary and decision* metric, since it accounts for all four confusion-matrix entries (TP/TN/FP/FN) and penalizes degenerate “single-direction” predictors, avoiding superficially high accuracy that lacks genuine directional discriminative power.

#### Minimum-movement filtering defines the evaluation regime.

Figure [2](https://arxiv.org/html/2602.11020v1#S6.F2 "Figure 2 ‣ 6.1 Clean Baselines ‣ 6 Results ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging") shows that the minimum-movement threshold τ\tau (Sec. [5.3](https://arxiv.org/html/2602.11020v1#S5.SS3 "5.3 Stabilizing Labels with a Minimum-Movement Threshold ‣ 5 A Stable, Leakage-Resistant Training Baseline ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging")) largely determines whether the task is learnable *on the ex-post filtered subsets* defined by min\_move.
Without filtering or with weak filtering (τ∈{0,0.002,0.004}\tau\in\{0,0.002,0.004\}), most deep models hover around zero MCC (sometimes negative), indicating near-chance behavior on the full set.
As τ\tau increases to 0.0060.006 and 0.0080.008, performance improves sharply, consistent with restricting evaluation to subsets that exclude near-zero moves and thus reduce direction-label ambiguity.
Aggregating across all deep configurations (Lite-CNN/ResNet18-P and \*-cons, all input modes), the mean MCC rises from −0.002-0.002 at τ=0\tau=0 to 0.0820.082 at τ=0.006\tau=0.006 and peaks at 0.0920.092 at τ=0.008\tau=0.008, before dropping to 0.0300.030 at τ=0.010\tau=0.010.
The drop at τ=0.010\tau=0.010 aligns with the reduced effective sample size (Table [1](https://arxiv.org/html/2602.11020v1#S5.T1 "Table 1 ‣ 5.4 Leakage-Resistant Time Split with Embargo ‣ 5 A Stable, Leakage-Resistant Training Baseline ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging")), which increases variance and destabilizes training.
We stress that τ\tau is used here to define evaluation regimes ex post, not as an inference-time filtering rule.

#### Lite-CNN: single-view is more robust under weak filtering; dual-view becomes beneficial once labels stabilize.

Under weak filtering (τ=0.004\tau=0.004), indic already yields a clear positive signal for Lite-CNN (0.107292±0.0224770.107292\pm 0.022477), while both early fusion is negative (−0.020004±0.016396-0.020004\pm 0.016396), suggesting negative transfer when two noisy views are fused too early.
Once τ≥0.006\tau\geq 0.006, both becomes consistently positive and competitive (e.g., 0.088767±0.0426620.088767\pm 0.042662 at τ=0.006\tau=0.006, 0.107206±0.0466320.107206\pm 0.046632 at τ=0.008\tau=0.008), indicating that dual-view information is exploitable when labels are less noisy.
At τ=0.006\tau=0.006, ohlcv is also strong (0.109095±0.0390230.109095\pm 0.039023), implying that price-based visual patterns alone can be predictive after filtering.

#### Late fusion drives the main gain; consistency regularization yields modest, non-monotonic effects.

Switching from early fusion (lite-cnn | both) to dual-branch late fusion without consistency (λ=0\lambda=0) yields a large improvement at τ=0.006\tau=0.006 (from 0.088767±0.0426620.088767\pm 0.042662 to 0.127459±0.0359460.127459\pm 0.035946), indicating that the *architecture-level* change (separate encoders + fusion head) is the dominant factor in our setting.
Adding consistency regularization can help, but not monotonically and the gains are modest: at τ=0.006\tau=0.006, lite-cnn-cons peaks at λ=0.5\lambda=0.5 (0.129607±0.0264490.129607\pm 0.026449), while λ=1\lambda=1 is lower (0.120755±0.0294680.120755\pm 0.029468).
At τ=0.008\tau=0.008, λ=1\lambda=1 reaches 0.103269±0.0313870.103269\pm 0.031387, close to early fusion (0.107206±0.0466320.107206\pm 0.046632), suggesting that consistency appears to act largely as a regularizer, whose benefit is *τ\tau-dependent* and sensitive to the effective data regime induced by filtering.

#### ResNet18-P: early fusion underperforms; late fusion partially recovers but variance is higher.

ResNet18-P exhibits a different regime: dual-view early fusion is consistently weak (e.g., 0.042873±0.0613700.042873\pm 0.061370 at τ=0.008\tau=0.008), while single-view modes are stronger at the same threshold (indic: 0.108023±0.0401450.108023\pm 0.040145, ohlcv: 0.109101±0.0728300.109101\pm 0.072830).
Late fusion improves the dual-view setting (e.g., resnet18p-cons with λ=0.5\lambda=0.5 reaches 0.083423±0.0525840.083423\pm 0.052584 at τ=0.008\tau=0.008), but the ResNet family generally shows larger standard deviations, especially under strict filtering (e.g., resnet18p | both: 0.061769±0.1158980.061769\pm 0.115898 at τ=0.010\tau=0.010), consistent with sample-size-driven instability.

#### LogReg as a diagnostic baseline.

LogReg can be competitive at certain thresholds (e.g., ohlcv at τ=0.008\tau=0.008 achieves MCC=0.116126\mathrm{MCC}=0.116126), but its behavior is highly non-monotonic across τ\tau and input modes (e.g., both at τ=0.006\tau=0.006 yields MCC=−0.039129\mathrm{MCC}=-0.039129).
We therefore treat it primarily as a diagnostic indicator of partial linear separability after label stabilization.

#### Takeaways.

Across backbones, (i) label stabilization via min\_move is a prerequisite for learning in our setting; (ii) in the dual-view setting, late fusion is generally more *reliable* than early fusion on clean evaluation once labels stabilize; and (iii) consistency regularization can provide modest gains in some mid-noise regimes but is not reliably monotonic and requires careful tuning jointly with τ\tau.

Table 2: Representative MCC (mean±\pmstd) at key τ\tau values.
Deep models are averaged over n=8n{=}8 seeds. Full curves are in Fig. [2](https://arxiv.org/html/2602.11020v1#S6.F2 "Figure 2 ‣ 6.1 Clean Baselines ‣ 6 Results ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging").

| Model (input) | 𝝉=0.004\boldsymbol{\tau=0.004} | 𝝉=0.006\boldsymbol{\tau=0.006} | 𝝉=0.008\boldsymbol{\tau=0.008} |
| --- | --- | --- | --- |
| Lite-CNN (both, early fusion) | −0.020004±0.016396-0.020004\pm 0.016396 | 0.088767±0.0426620.088767\pm 0.042662 | 0.107206±0.046632\mathbf{0.107206\pm 0.046632} |
| Lite-CNN (indic) | 0.107292±0.022477\mathbf{0.107292\pm 0.022477} | 0.079303±0.0326780.079303\pm 0.032678 | 0.100279±0.0483220.100279\pm 0.048322 |
| Lite-CNN (ohlcv) | −0.003236±0.023789-0.003236\pm 0.023789 | 0.109095±0.0390230.109095\pm 0.039023 | 0.090707±0.0288930.090707\pm 0.028893 |
| Lite-CNN-Cons (both, λ=0\lambda=0) | −0.023262±0.034602-0.023262\pm 0.034602 | 0.127459±0.0359460.127459\pm 0.035946 | 0.100430±0.0344390.100430\pm 0.034439 |
| Lite-CNN-Cons (both, λ=0.5\lambda=0.5) | −0.015634±0.052001-0.015634\pm 0.052001 | 0.129607±0.026449\mathbf{0.129607\pm 0.026449} | 0.089973±0.0672090.089973\pm 0.067209 |
| Lite-CNN-Cons (both, λ=1\lambda=1) | −0.014013±0.034309-0.014013\pm 0.034309 | 0.120755±0.0294680.120755\pm 0.029468 | 0.103269±0.0313870.103269\pm 0.031387 |
| ResNet18-P (both, early fusion) | 0.012168±0.0306740.012168\pm 0.030674 | 0.017593±0.0440720.017593\pm 0.044072 | 0.042873±0.0613700.042873\pm 0.061370 |
| ResNet18-P (indic) | 0.055638±0.0478240.055638\pm 0.047824 | 0.082039±0.0399880.082039\pm 0.039988 | 0.108023±0.0401450.108023\pm 0.040145 |
| ResNet18-P (ohlcv) | −0.005656±0.059240-0.005656\pm 0.059240 | 0.018580±0.0547610.018580\pm 0.054761 | 0.109101±0.0728300.109101\pm 0.072830 |
| ResNet18-P-Cons (both, λ=0.5\lambda=0.5) | −0.003653±0.037078-0.003653\pm 0.037078 | 0.067112±0.0313880.067112\pm 0.031388 | 0.083423±0.0525840.083423\pm 0.052584 |

#### Choice of τ\tau for robustness evaluation.

All subsequent adversarial evaluations use τ=0.006\tau=0.006 as the default operating point.
At smaller thresholds (τ≤0.004\tau\leq 0.004), most configurations remain close to chance in MCC, making robustness comparisons less informative.
At larger thresholds (e.g., τ=0.010\tau=0.010), the reduced effective sample size can amplify variance across random seeds.
Thus, τ=0.006\tau=0.006 offers a practical balance between label stabilization and sufficient data for reliable robustness measurement.

### 6.2 Adversarial Robustness

#### Protocol and summary metrics.

We evaluate test-time evasion attacks under the ℓ∞\ell\_{\infty} threat model in Eq. ([3](https://arxiv.org/html/2602.11020v1#S4.E3 "In ℓ_∞-bounded perturbations (defined in raw pixel space). ‣ 4.1 Threat Model ‣ 4 Threat Model and Evaluation Protocol ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging")) using the main budget grid EE in Eq. ([4](https://arxiv.org/html/2602.11020v1#S4.E4 "In ℓ_∞-bounded perturbations (defined in raw pixel space). ‣ 4.1 Threat Model ‣ 4 Threat Model and Evaluation Protocol ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging")) (up to ϵadv=1/255\epsilon\_{\mathrm{adv}}=1/255).
Unless stated otherwise, all robustness results in this section use the default operating point τ=0.006\tau=0.006 (min\_move) selected in Sec. [6.1](https://arxiv.org/html/2602.11020v1#S6.SS1 "6.1 Clean Baselines ‣ 6 Results ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging").
We report robustness curves MCC​(ϵadv)\mathrm{MCC}(\epsilon\_{\mathrm{adv}}) (mean±\pmstd over random seeds), and summarize degradation by
Δworst\Delta\_{\mathrm{worst}} as defined in Eq. ([9](https://arxiv.org/html/2602.11020v1#S4.E9 "In 4.3 Evaluation and Summary Metrics ‣ 4 Threat Model and Evaluation Protocol ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging")).
We focus on PGD as the primary evaluation attack; FGSM is included as a weaker, single-step reference.

#### Summary of findings.

We find (i) rapid degradation under tiny budgets, (ii) strong view asymmetry, and (iii) a clear robustness advantage of late fusion under view-constrained attacks, while robustness under joint (two-view) attacks remains challenging.

![Refer to caption](x3.png)

![Refer to caption](x4.png)

![Refer to caption](x5.png)

Figure 3: Adversarial robustness curves for Lite-CNN family at τ=0.006\tau=0.006 (mean±\pmstd).
We report MCC​(ϵadv)\mathrm{MCC}(\epsilon\_{\mathrm{adv}}) under FGSM and PGD for (left) attacking the indic view,
(middle) attacking the ohlcv view, and (right) joint perturbations on both views.
Late fusion (\*-cons) degrades more gracefully than early fusion, especially under view-constrained attacks.



![Refer to caption](x6.png)

![Refer to caption](x7.png)

![Refer to caption](x8.png)

Figure 4: Adversarial robustness curves for ResNet18-P family at τ=0.006\tau=0.006 (mean±\pmstd).
We report MCC​(ϵadv)\mathrm{MCC}(\epsilon\_{\mathrm{adv}}) under FGSM and PGD for (left) attacking the indic view,
(middle) attacking the ohlcv view, and (right) joint perturbations on both views.
The family shows pronounced view sensitivity (indicator attacks are particularly destructive), and late fusion only partially mitigates this.

#### Overall vulnerability under tiny ℓ∞\ell\_{\infty} budgets.

Across architectures, naturally trained models can degrade substantially under pixel-space perturbations.
Even at ϵadv=0.25/255\epsilon\_{\mathrm{adv}}=0.25/255 (a quarter of an 8-bit intensity level), PGD often causes a pronounced MCC drop, and performance can become near-zero or negative as the budget increases toward 1/2551/255.
This confirms that pixel-space ℓ∞\ell\_{\infty} robustness is not obtained “for free” in our financial-image setting.

#### View sensitivity and view-aligned evaluation.

Using the view–channel mapping in Sec. [3.3](https://arxiv.org/html/2602.11020v1#S3.SS3 "3.3 View-to-Channel Mapping ‣ 3 Problem Setup and Notation ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging"), we compare (i) single-view models attacked on their sole channel and
(ii) two-view models attacked on the corresponding view channel (Sec. [4.2](https://arxiv.org/html/2602.11020v1#S4.SS2 "4.2 Threat Scenarios and View-Aligned Protocol ‣ 4 Threat Model and Evaluation Protocol ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging")).
The results reveal strong view dependence.
In particular, ResNet18-P exhibits extreme sensitivity when the indicator view is perturbed: very small budgets can already drive MCC close to the lower bound, suggesting a near-consistent label-flip behavior rather than a gradual attenuation of predictive signal.
In contrast, attacking the OHLCV view typically leads to a more gradual deterioration, highlighting asymmetric fragility across views.

#### Late fusion improves robustness under view-constrained attacks.

A consistent trend in the two-view setting is that dual-branch late fusion (\*-cons) degrades more gracefully than early fusion (channel stacking) under view-constrained attacks.
When only one view is perturbed, the unperturbed branch can still provide usable evidence, which mitigates worst-case collapse and yields a flatter robustness curve over EE.
This robustness advantage is especially visible when attacking the indicator channel, where late fusion maintains substantially higher MCC than early fusion over most of the budget range.

#### Joint perturbations remain challenging.

When the adversary perturbs both channels jointly, performance deteriorates more rapidly than in view-constrained settings, even for late fusion.
This indicates that redundancy across views provides meaningful protection against single-view corruption, but does not fully defend against worst-case joint perturbations.

#### Consistency regularization: secondary but non-negligible effects.

Within late-fusion models, increasing the consistency weight λ\lambda can further reduce degradation under view-constrained attacks in some settings, but the dominant robustness gain comes from the architectural shift from early fusion to late fusion.

*Model selection note:* while λ=0.5\lambda=0.5 is the clean-optimal setting at τ=0.006\tau=0.006 (Sec. [6.1](https://arxiv.org/html/2602.11020v1#S6.SS1 "6.1 Clean Baselines ‣ 6 Results ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging")), we report late-fusion robustness summaries with λ=1\lambda=1 by default because it yields slightly better robustness (including the 2/2552/255 stress test) at a small cost in clean MCC.
We therefore interpret consistency as a refinement on top of the late-fusion design rather than the primary driver.

Table 3: PGD robustness summary at τ=0.006\tau=0.006 (min\_move).
We report MCC at two representative budgets (0.25/2550.25/255 and 1/2551/255) and the worst-case drop Δworst\Delta\_{\mathrm{worst}} over nonzero budgets {0.25,0.5,0.75,1}/255\{0.25,0.5,0.75,1\}/255 (Eq. ([9](https://arxiv.org/html/2602.11020v1#S4.E9 "In 4.3 Evaluation and Summary Metrics ‣ 4 Threat Model and Evaluation Protocol ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging"))).
As an additional stress test, results at ϵadv=2/255\epsilon\_{\mathrm{adv}}=2/255 are reported in Appendix [E](https://arxiv.org/html/2602.11020v1#A5 "Appendix E Additional Stress Test at ϵ_adv=2/255 ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging").

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Model | Input | Attack (PGD) | MCC@0 | MCC@0.25/255 | MCC@1/255 | 𝚫𝐰𝐨𝐫𝐬𝐭\boldsymbol{\Delta\_{\mathrm{worst}}} |
| Lite-CNN | ohlcv | on ohlcv | 0.109 | 0.054 | -0.088 | -0.197 |
| Lite-CNN | indic | on indic | 0.079 | 0.024 | -0.186 | -0.265 |
| Lite-CNN | both (early) | on ohlcv (ch0) | 0.089 | 0.030 | -0.104 | -0.193 |
| Lite-CNN | both (early) | on indic (ch1) | 0.089 | 0.033 | -0.094 | -0.183 |
| Lite-CNN | both (early) | on both | 0.089 | -0.014 | -0.317 | -0.406 |
| Lite-CNN-Cons (λ=1\lambda{=}1) | both (late) | on ohlcv (ch0) | 0.121 | 0.081 | -0.029 | -0.150 |
| Lite-CNN-Cons (λ=1\lambda{=}1) | both (late) | on indic (ch1) | 0.121 | 0.113 | 0.084 | -0.037 |
| Lite-CNN-Cons (λ=1\lambda{=}1) | both (late) | on both | 0.121 | 0.071 | -0.072 | -0.192 |
| ResNet18-P | ohlcv | on ohlcv | 0.019 | -0.443 | -0.952 | -0.971 |
| ResNet18-P | indic | on indic | 0.082 | -0.999 | -1.000 | -1.082 |
| ResNet18-P-Cons (λ=1\lambda{=}1) | both (late) | on ohlcv (ch0) | 0.095 | -0.211 | -0.774 | -0.870 |
| ResNet18-P-Cons (λ=1\lambda{=}1) | both (late) | on indic (ch1) | 0.095 | -0.959 | -1.000 | -1.095 |
| ResNet18-P-Cons (λ=1\lambda{=}1) | both (late) | on both | 0.095 | -0.983 | -1.000 | -1.095 |

#### Stress test at ϵadv=2/255\epsilon\_{\mathrm{adv}}=2/255 (not in the main grid).

Although our main evaluation grid stops at 1/2551/255, we additionally evaluate a larger budget as a stress test.
Notably, under the indic-only attack (ch1), Lite-CNN-Cons maintains *positive mean* MCC at 2/2552/255 for both λ=0.5\lambda=0.5 and λ=1\lambda=1, with λ=1\lambda=1 being slightly stronger (Appendix [E](https://arxiv.org/html/2602.11020v1#A5 "Appendix E Additional Stress Test at ϵ_adv=2/255 ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging")).

#### Branch diagnostics for late-fusion two-view models (clean test, τ=0.006\tau=0.006).

To interpret robustness trends for \*-cons models, we inspect clean-test branch diagnostics that summarize
cross-branch alignment (agree\_ab, sym\_kl with T=2T{=}2) and branch-wise versus fused MCC
(Table [4](https://arxiv.org/html/2602.11020v1#S6.T4 "Table 4 ‣ Branch diagnostics for late-fusion two-view models (clean test, 𝜏=0.006). ‣ 6.2 Adversarial Robustness ‣ 6 Results ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging"); full results in Appendix [F](https://arxiv.org/html/2602.11020v1#A6 "Appendix F Full Branch Diagnostics for Late-Fusion Models ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging")).
For Lite-CNN-Cons, enabling consistency (λ>0\lambda>0) sharply increases alignment (higher agree\_ab, much lower sym\_kl),
yet branch-wise MCC remains near zero while fused-head MCC stays substantially higher.
This indicates that predictive signal is expressed primarily through the *feature-level late-fusion pathway* rather than strong standalone branch classifiers.
For ResNet18P-Cons, larger λ\lambda likewise improves alignment and is associated with higher fused MCC, but variance remains notable and robustness failures under indicator-view attacks persist.

Table 4: Compact clean-test diagnostics for late-fusion two-view models (τ=0.006\tau=0.006, T=2T=2).
Mean±\pmstd over n=8n{=}8 seeds. We report cross-branch alignment (agree\_ab, sym\_kl),
branch-wise MCC (mcc\_a/mcc\_b), and fused-head MCC (mcc\_fuse). Full diagnostics are in Appendix [F](https://arxiv.org/html/2602.11020v1#A6 "Appendix F Full Branch Diagnostics for Late-Fusion Models ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging").

| Model | 𝝀\boldsymbol{\lambda} | agree\_ab | sym\_kl | mcc\_a / mcc\_b | mcc\_fuse |
| --- | --- | --- | --- | --- | --- |
| Lite-CNN-Cons | 0 | 0.275090±0.2440570.275090\pm 0.244057 | 0.164898±0.1257510.164898\pm 0.125751 | 0.019377±0.061519/ 0.005906±0.0518560.019377\pm 0.061519\ /\ 0.005906\pm 0.051856 | 0.127459±0.0359460.127459\pm 0.035946 |
| Lite-CNN-Cons | 0.5 | 0.830197±0.1853330.830197\pm 0.185333 | 0.000195±0.0000980.000195\pm 0.000098 | 0.001488±0.053262/−0.001753±0.0765800.001488\pm 0.053262\ /\ -0.001753\pm 0.076580 | 0.129607±0.0264490.129607\pm 0.026449 |
| Lite-CNN-Cons | 1 | 0.803315±0.2055720.803315\pm 0.205572 | 0.000106±0.0000290.000106\pm 0.000029 | 0.006285±0.057660/−0.015335±0.0526860.006285\pm 0.057660\ /\ -0.015335\pm 0.052686 | 0.120755±0.0294680.120755\pm 0.029468 |
| ResNet18P-Cons | 0 | 0.439964±0.2473140.439964\pm 0.247314 | 0.074461±0.0656100.074461\pm 0.065610 | 0.014477±0.047350/ 0.000779±0.0383670.014477\pm 0.047350\ /\ 0.000779\pm 0.038367 | 0.048051±0.0566000.048051\pm 0.056600 |
| ResNet18P-Cons | 0.5 | 0.920251±0.1969210.920251\pm 0.196921 | 0.006523±0.0035180.006523\pm 0.003518 | −0.006042±0.012812/−0.002165±0.015076-0.006042\pm 0.012812\ /\ -0.002165\pm 0.015076 | 0.067112±0.0313880.067112\pm 0.031388 |
| ResNet18P-Cons | 1 | 0.931452±0.1632800.931452\pm 0.163280 | 0.003425±0.0013790.003425\pm 0.001379 | −0.002706±0.028186/ 0.009707±0.019310-0.002706\pm 0.028186\ /\ 0.009707\pm 0.019310 | 0.095146±0.0579330.095146\pm 0.057933 |

#### Takeaways.

Across all settings, we observe that pixel-space ℓ∞\ell\_{\infty} perturbations can severely degrade next-day direction prediction even at extremely small budgets.
Robustness is strongly view-dependent: perturbing the indicator view is particularly damaging for ResNet18-P, often leading to near-saturated failure already at ϵadv=0.25/255\epsilon\_{\mathrm{adv}}=0.25/255.
In the two-view regime, dual-branch late fusion consistently improves robustness under *view-constrained* attacks, supporting the intuition that an unperturbed branch can provide a partial evidence path.
However, *joint* perturbations remain challenging and can still induce large performance drops, indicating that cross-view redundancy alone does not guarantee worst-case robustness.
Within late-fusion models, increasing the consistency weight λ\lambda yields secondary but measurable gains in several view-constrained scenarios, while the dominant robustness improvement stems from the architectural shift from early to late fusion.

*Diagnostics.* Branch diagnostics (Table [4](https://arxiv.org/html/2602.11020v1#S6.T4 "Table 4 ‣ Branch diagnostics for late-fusion two-view models (clean test, 𝜏=0.006). ‣ 6.2 Adversarial Robustness ‣ 6 Results ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging"), Appendix [F](https://arxiv.org/html/2602.11020v1#A6 "Appendix F Full Branch Diagnostics for Late-Fusion Models ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging")) show that λ\lambda mainly enforces logit-level alignment across views, while its impact on fused performance is secondary and backbone-dependent.

## 7 Discussion

#### Learnability hinges on the label-noise regime, with a non-monotonic data–noise trade-off.

A central observation from the clean baselines is that next-day direction prediction is near chance on the full dataset and becomes measurably learnable only on *ex-post* evaluation subsets defined by the minimum-movement threshold (min\_move; Sec. [6.1](https://arxiv.org/html/2602.11020v1#S6.SS1 "6.1 Clean Baselines ‣ 6 Results ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging")), i.e., samples satisfying |rt+1|≥τ|r\_{t+1}|\geq\tau.
At small thresholds (τ≤0.004\tau\leq 0.004), performance remains near chance across architectures, consistent with direction labels being dominated by micro-moves and label ambiguity.
Increasing τ\tau reduces near-zero ambiguity and can reveal predictive signal *on the resulting filtered subset*, but overly strict filtering (τ≈0.010\tau\approx 0.010) reduces the effective sample size and increases seed-to-seed variance, leading to a non-monotonic regime in which additional “denoising” can harm reliability.
We emphasize that min\_move is a label-dependent subset definition rather than an inference-time filtering rule.
This highlights a practical mechanism: in financial-image settings, reported generalization and robustness trends should be interpreted jointly with the evaluation regime induced by such subset definitions, rather than as properties of a fixed unconditional prediction task.

#### Fusion is noise-regime dependent: early fusion can induce negative transfer under high label noise.

The dual-view setting exhibits a clear regime shift.
Under weak filtering, early fusion by channel stacking can underperform single-view models (and even become negative for Lite-CNN), suggesting that naively merging heterogeneous, noisy views encourages spurious correlations and negative transfer.
Once labels stabilize (τ≥0.006\tau\geq 0.006), dual-view learning becomes consistently beneficial and competitive, indicating that cross-view information is exploitable when the supervision signal is sufficiently reliable.
In this stabilized regime, dual-branch late fusion provides a more *reliable* default than early fusion on clean evaluation, consistent with the large clean MCC gains observed at τ=0.006\tau=0.006.
Overall, these results support a broader multimodal lesson: the relative advantage of multimodal fusion depends not only on model capacity, but also on the effective label-noise regime and the alignment between views.

#### Late fusion provides a robust evidence path under view-constrained corruption, but joint attacks remain challenging.

Across backbones, late fusion consistently improves robustness under *view-constrained* attacks (Sec. [6.2](https://arxiv.org/html/2602.11020v1#S6.SS2 "6.2 Adversarial Robustness ‣ 6 Results ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging")).
A natural interpretation is that, when only one view is perturbed, the unperturbed branch can still provide partial evidence, preventing worst-case collapse and yielding flatter robustness curves over the budget grid.
This robustness trend complements the clean-baseline finding that late fusion is a stronger and more reliable default than early fusion once labels stabilize.
However, *joint* perturbations remain challenging: when both channels are attacked simultaneously, redundancy across views is insufficient to guarantee worst-case robustness, and performance can degrade substantially even for late-fusion models.
This delineates the protection provided by multi-view redundancy: it helps against single-view corruption but does not substitute for robust training or stronger defenses against coordinated multi-view attacks.

#### View asymmetry reveals which information source is brittle under pixel-space perturbations.

A striking result is the strong view dependence of adversarial vulnerability, especially for ResNet18-P under indicator-view attacks where MCC can saturate near the lower bound at extremely small budgets (e.g., ϵadv=0.25/255\epsilon\_{\mathrm{adv}}=0.25/255), suggesting near-consistent label-flip behavior rather than a gradual attenuation of predictive signal.
In contrast, OHLCV-view attacks often yield a more gradual deterioration.
While both views are derived from the same underlying time series, their rendered representations and inductive biases differ, and the view-aligned evaluation protocol makes this asymmetry explicit.
More broadly, view-aligned robustness curves can be interpreted as a diagnostic of which information source (or rendering) is brittle, guiding both representation choices and defense priorities.

#### Consistency regularization: logit-level alignment is easy; improved robustness is conditional.

Branch diagnostics (Table [4](https://arxiv.org/html/2602.11020v1#S6.T4 "Table 4 ‣ Branch diagnostics for late-fusion two-view models (clean test, 𝜏=0.006). ‣ 6.2 Adversarial Robustness ‣ 6 Results ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging"), Appendix [F](https://arxiv.org/html/2602.11020v1#A6 "Appendix F Full Branch Diagnostics for Late-Fusion Models ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging")) help explain why consistency has modest, sometimes non-monotonic effects: increasing λ\lambda rapidly tightens cross-branch logit agreement and reduces mismatch (sym\_kl), yet branch-wise MCC stays near zero even when fused-head MCC is much higher, indicating that most predictive signal is carried by the fused late-fusion pathway rather than by standalone branch classifiers.
For Lite-CNN, stronger consistency can over-align branch logits without improving discriminability, consistent with its non-monotonic clean and robustness trends across λ\lambda. For ResNet18-P, larger λ\lambda improves fused performance in our setting but does not avert the saturated failure mode under indicator-view attacks. Although λ=0.5\lambda=0.5 is clean-optimal at τ=0.006\tau=0.006, we use λ=1\lambda=1 in robustness summaries because it yields slightly better robustness (including the 2/2552/255 stress test) at a small cost in clean MCC.
Overall, consistency regularization is best viewed as a secondary stabilizer whose optimal strength is backbone- and regime-dependent, and should be tuned jointly with the fusion design and the label-noise operating point.

#### Threat-model interpretation and limitations.

Our main robustness evaluation adopts a pixel-space ℓ∞\ell\_{\infty} threat model on rendered financial images.
This should be interpreted as a stress test of sensitivity to small input perturbations in the chosen representation, rather than a claim that real-world market adversaries directly manipulate pixels.
Nevertheless, the observed fragility at tiny budgets underscores that these models can rely on brittle, non-robust features in the image parameterization.
Several limitations follow.
First, robustness conclusions are specific to the rendering and view–channel mapping used here; alternative parameterizations (e.g., different indicator encodings or chart styles) may change the attack surface.
Second, the min\_move filter couples label stability with sample size, so robustness comparisons should be contextualized by the induced data regime.
Third, naturally trained models remain vulnerable to coordinated joint attacks; addressing worst-case robustness likely requires adversarial training, certified defenses, or representation-level constraints.
Finally, our PGD evaluation uses a deterministic setting without random restarts; stronger first-order baselines (e.g., multi-restart PGD) and ensemble attacks (e.g., AutoAttack) are natural extensions for future work to further probe worst-case robustness.

#### Implications and future directions.

The results suggest several actionable directions for robustness and multi-view learning under noisy financial supervision.
First, robustness evaluations should report the label-noise operating point explicitly (e.g., via τ\tau) and treat learnability as part of the experimental protocol.
Second, in our dual-view setting, late fusion is a reliable starting point—especially under single-view corruption—though it does not guarantee worst-case robustness under joint perturbations.
Third, diagnostics that separate logit-level alignment from fused predictive power can prevent over-interpreting agreement metrics as evidence of improved discriminability.
Future work should complement pixel-space attacks with pipeline-level stress tests that reflect realistic variability—including small window-boundary misalignment, missingness/imputation effects, and rendering/normalization differences—followed by re-rendering the views.
Benchmarks should also account for abrupt changes in market conditions that can shift the data distribution over short periods.
Finally, beyond representation-level attacks, adversarial or corrupted data/pipeline inputs may degrade reliability; deployments should therefore include lightweight safeguards such as data provenance checks, cross-view integrity checks (alignment, missingness, and abnormal divergence), and drift/anomaly monitoring.

## 8 Conclusion

We investigated same-source multi-view learning and adversarial robustness for next-day direction prediction on SGE gold spot data (2005–2025), using two deterministically constructed and window-aligned image views: an OHLCV-rendered price/volume chart (ohlcv) and a technical-indicator matrix view (indic).
This controlled setup isolates representation and fusion effects from cross-source alignment confounds.

Across leakage-resistant time-block splits with embargo, we find that both learnability and robustness trends depend strongly on the effective label-ambiguity regime induced by near-zero moves.
We therefore use an *ex-post* minimum-movement filter (min\_move), defined using the realized next-day return magnitude |rt+1||r\_{t+1}|, to construct evaluation subsets that exclude near-zero moves and reduce direction-label ambiguity.
This induces a non-monotonic data–noise trade-off: moderate τ\tau can make the conditional direction task on the resulting subset more learnable, while overly strict filtering reduces effective sample size and increases variance.
Importantly, min\_move is used for offline benchmark/subset definition and robustness analysis rather than as an inference-time decision rule.
In the filtered subsets (default τ=0.006\tau=0.006), fusion is strongly regime dependent: early fusion by channel stacking can suffer negative transfer under noisier operating points, whereas late fusion with dual encoders and a fusion head is a more reliable default and provides the dominant clean-performance gains; cross-view consistency regularization yields secondary, backbone- and regime-dependent improvements.

From a security/robustness perspective, naturally trained models are highly vulnerable to test-time pixel-space ℓ∞\ell\_{\infty} perturbations on rendered inputs, even at extremely small budgets.
Using an explicit view–channel mapping, we evaluated two multi-view threat scenarios: view-constrained attacks that perturb exactly one view and joint attacks that perturb both views.
Robustness is markedly view dependent; for some backbones, indicator-view perturbations can drive MCC toward its minimum possible values under tiny budgets.
Late fusion consistently improves robustness under view-constrained attacks by preserving an unperturbed evidence path, but joint perturbations remain challenging and can still cause substantial worst-case degradation, indicating that cross-view redundancy alone does not guarantee worst-case robustness.
Branch diagnostics suggest that consistency regularization primarily enforces logit-level alignment, while predictive signal is largely expressed through the feature-level fusion pathway rather than strong standalone branch classifiers.

Overall, our results highlight that (i) reported robustness trends in same-source financial imaging are highly sensitive to evaluation design—in particular, leakage-resistant time-block splits with embargo for overlapping windows and explicit reporting of operating points, including any *ex-post* subset definitions used to reduce near-zero-move label ambiguity—so these choices should be stated clearly to support reliable robustness assessment; (ii) the benefits of multi-view fusion are operating-point dependent, and can shift from negative transfer to consistent gains as label ambiguity is reduced; and (iii) robustness evaluation for multi-view inputs should distinguish view-constrained from joint attacks to properly characterize the attack surface.

## References

* López de Prado [2018]

  Marcos López de Prado.
  *Advances in Financial Machine Learning*.
  John Wiley & Sons, Inc., New Jersey, February 2018.
  ISBN 9781119482086.
  Print ISBN: 9781119482086 (ISBN-10: 1119482089).
* Goodfellow et al. [2015]

  Ian J. Goodfellow, Jonathon Shlens, and Christian Szegedy.
  Explaining and harnessing adversarial examples.
  In *International Conference on Learning Representations (ICLR)
  2015*, 2015.
  URL <https://arxiv.org/abs/1412.6572>.
  Poster.
* Madry et al. [2018]

  Aleksander Madry, Aleksandar Makelov, Ludwig Schmidt, Dimitris Tsipras, and
  Adrian Vladu.
  Towards deep learning models resistant to adversarial attacks.
  In *6th International Conference on Learning Representations
  (ICLR) 2018, Vancouver, BC, Canada, April 30–May 3, 2018, Conference Track
  Proceedings*. OpenReview.net, 2018.
  URL <https://openreview.net/forum?id=rJzIBfZAb>.
* Yang et al. [2021]

  Karren Yang, Wan-Yi Lin, Manash Barman, Filipe Condessa, and J. Zico Kolter.
  Defending multimodal fusion models against single-source adversaries.
  In *Proceedings of the IEEE/CVF Conference on Computer Vision
  and Pattern Recognition (CVPR)*, pages 3340–3349, June 2021.
  doi: 10.1109/CVPR46437.2021.00335.
  URL
  <https://openaccess.thecvf.com/content/CVPR2021/html/Yang_Defending_Multimodal_Fusion_Models_Against_Single-Source_Adversaries_CVPR_2021_paper.html>.
* Gao et al. [2022]

  Lijun Gao, Yuxin Jiang, Peigen Sheng, and Xianhua Wei.
  Convolutional neural network applied to gold price forecasting with
  an image integration methods based on multi-sources and heterogeneous data.
  *Journal of Systems Science and Mathematical Sciences*,
  42(11):3073–3093, 2022.
  doi: 10.12341/jssms22104.
* Wang and Oates [2015]

  Zhiguang Wang and Tim Oates.
  Imaging time-series to improve classification and imputation.
  In *Proceedings of the Twenty-Fourth International Joint
  Conference on Artificial Intelligence (IJCAI 2015)*, pages 3939–3945. AAAI
  Press, 2015.
  doi: 10.5555/2832747.2832798.
  URL <https://www.ijcai.org/Proceedings/15/Papers/553.pdf>.
* Sezer and Ozbayoglu [2020a]

  Omer Berat Sezer and Ahmet Murat Ozbayoglu.
  Financial trading model with stock bar chart image time series with
  deep convolutional neural networks.
  *Intelligent Automation & Soft Computing*, 26(2):323–334, 2020a.
  doi: 10.31209/2018.100000065.
  URL <https://www.techscience.com/iasc/v26n2/39939>.
* Sezer and Ozbayoglu [2020b]

  Omer Berat Sezer and Ahmet Murat Ozbayoglu.
  Financial trading model with stock bar chart image time series with
  deep convolutional neural networks.
  *Intelligent Automation & Soft Computing*, 26(2):323–334, 2020b.
  doi: 10.31209/2018.100000065.
  URL <https://www.techscience.com/iasc/v26n2/39939>.
* Jiang et al. [2023]

  Jingwen Jiang, Bryan T. Kelly, and Dacheng Xiu.
  (re-)imag(in)ing price trends.
  *The Journal of Finance*, 78(6):3193–3249,
  2023.
  doi: 10.1111/jofi.13268.
* Chen and Tsai [2020]

  Jun-Hao Chen and Yun-Cheng Tsai.
  Encoding candlesticks as images for patterns classification using
  convolutional neural networks.
  *Financial Innovation*, 6(1):26, 2020.
  doi: 10.1186/s40854-020-00187-0.
* Chen et al. [2021]

  Wei Chen, Manrui Jiang, Wei-Guo Zhang, and Zhensong Chen.
  A novel graph convolutional feature based convolutional neural
  network for stock trend prediction.
  *Information Sciences*, 556:67–94, may 2021.
  doi: 10.1016/j.ins.2020.12.068.
  URL <https://doi.org/10.1016/j.ins.2020.12.068>.
* Mehrmolaei and Saniee Abadeh [2025]

  Soheila Mehrmolaei and Mohammad Saniee Abadeh.
  A decade systematic review of fusion techniques in financial market
  prediction (2016–2025).
  *Computer Science Review*, 58:100813, 2025.
  doi: 10.1016/j.cosrev.2025.100813.
* Kim and Kim [2019]

  Tae Kim and Ha Yoon Kim.
  Forecasting stock prices with a feature fusion LSTM-CNN model using
  different representations of the same data.
  *PLOS ONE*, 14(2):e0212320, 2019.
  doi: 10.1371/journal.pone.0212320.
* Liang et al. [2022]

  Mengxia Liang, Shaocong Wu, Xiaolong Wang, and Qingcai Chen.
  A stock time series forecasting approach incorporating candlestick
  patterns and sequence similarity.
  *Expert Systems with Applications*, 205:117595, 2022.
  doi: 10.1016/j.eswa.2022.117595.
* Baltrusaitis et al. [2019]

  Tadas Baltrusaitis, Chaitanya Ahuja, and Louis-Philippe Morency.
  Multimodal machine learning: A survey and taxonomy.
  *IEEE Transactions on Pattern Analysis and Machine
  Intelligence*, 41(2):423–443, 2019.
  doi: 10.1109/TPAMI.2018.2798607.
* Rahate et al. [2022]

  Anil Rahate, Rahee Walambe, Sheela Ramanna, and Ketan Kotecha.
  Multimodal co-learning: Challenges, applications with datasets,
  recent advances and future directions.
  *Information Fusion*, 81:203–239, 2022.
  doi: 10.1016/j.inffus.2021.12.003.
* Bailey et al. [2017]

  David H. Bailey, Jonathan M. Borwein, Marcos López de Prado, and Qiji Jim
  Zhu.
  The probability of backtest overfitting.
  *Journal of Computational Finance*, 20(4):39–69, 2017.
  doi: 10.21314/JCF.2016.322.
* Bailey and López de Prado [2014]

  David H. Bailey and Marcos López de Prado.
  The deflated sharpe ratio: Correcting for selection bias, backtest
  overfitting, and non-normality.
  *The Journal of Portfolio Management*, 40(5):94–107, 2014.
  doi: 10.3905/jpm.2014.40.5.094.
* Fang et al. [2025]

  Yixiong Fang, Tianran Sun, Yuling Shi, Min Wang, and Xiaodong Gu.
  Lastingbench: Defend benchmarks against knowledge leakage.
  *arXiv preprint arXiv:2506.21614*, 2025.
* Szegedy et al. [2014]

  Christian Szegedy, Wojciech Zaremba, Ilya Sutskever, Joan Bruna, Dumitru Erhan,
  Ian Goodfellow, and Rob Fergus.
  Intriguing properties of neural networks.
  In *International Conference on Learning Representations
  (ICLR)*, 2014.
* Chen et al. [2020]

  Jun-Hao Chen, Samuel Yen-Chi Chen, Yun-Cheng Tsai, and Chih-Shiang Shur.
  Adversarial robustness of deep convolutional candlestick learner.
  *arXiv preprint arXiv:2006.03686*, May 2020.
  doi: 10.48550/arXiv.2006.03686.
  URL <https://arxiv.org/abs/2006.03686>.
* Fawaz et al. [2019]

  Hassan Ismail Fawaz, Germain Forestier, Jonathan Weber, Lhassane Idoumghar, and
  Pierre-Alain Muller.
  Adversarial attacks on deep neural networks for time series
  classification.
  *arXiv preprint arXiv:1903.07054*, 2019.
* Tushare [2025]

  Tushare.
  Tushare: Financial data interface.
  <https://tushare.pro/>, 2025.
  Accessed: 2025-08-28.
* Han et al. [2012]

  Ai Han, Yongmiao Hong, and Shouyang Wang.
  Autoregressive conditional models for interval-valued time series
  data (preliminary version).
  Technical report, Academy of Mathematics and Systems Science, Chinese
  Academy of Sciences, September 2012.
  Preliminary version.
* Matthews [1975]

  Brian W. Matthews.
  Comparison of the predicted and observed secondary structure of T4
  phage lysozyme.
  *Biochimica et Biophysica Acta (BBA) - Protein Structure*,
  405(2):442–451, 1975.
  doi: 10.1016/0005-2795(75)90109-9.
* He et al. [2016]

  Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.
  Deep residual learning for image recognition.
  In *Proceedings of the IEEE Conference on Computer Vision and
  Pattern Recognition (CVPR)*, pages 770–778, 2016.
  doi: 10.1109/CVPR.2016.90.
* Deng et al. [2009]

  Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, and Li Fei-Fei.
  Imagenet: A large-scale hierarchical image database.
  In *2009 IEEE Conference on Computer Vision and Pattern
  Recognition (CVPR)*, pages 248–255. IEEE, 2009.
  doi: 10.1109/CVPR.2009.5206848.
* Hinton et al. [2015]

  Geoffrey Hinton, Oriol Vinyals, and Jeff Dean.
  Distilling the knowledge in a neural network.
  *arXiv preprint arXiv:1503.02531*, 2015.
  URL <https://arxiv.org/abs/1503.02531>.
* Zhang et al. [2018]

  Ying Zhang, Tao Xiang, Timothy M. Hospedales, and Huchuan Lu.
  Deep mutual learning.
  In *Proceedings of the IEEE Conference on Computer Vision and
  Pattern Recognition (CVPR)*, pages 4320–4328, 2018.
  doi: 10.1109/CVPR.2018.00454.
* Racine [2000]

  Jeffrey Racine.
  Consistent cross-validatory model-selection for dependent data:
  hv-block cross-validation.
  *Journal of Econometrics*, 99(1):39–61,
  2000.
  doi: 10.1016/S0304-4076(00)00030-0.

## Appendix A Implementation Details for Input Parameterization

Table [5](https://arxiv.org/html/2602.11020v1#A1.T5 "Table 5 ‣ Threat model defined in raw space. ‣ Appendix A Implementation Details for Input Parameterization ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging") summarizes the input parameterization and normalization settings.

#### Raw input.

Each view is stored as an 8-bit grayscale image and loaded with ToTensor(), yielding a raw input
𝐱raw∈[0,1]C×256×256\mathbf{x}\_{\mathrm{raw}}\in[0,1]^{C\times 256\times 256},
where C=1C=1 for single-view and C=2C=2 for two-view models.

#### Optional per-channel standardization.

Optionally, we apply per-channel standardization

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐱norm=(𝐱raw−𝝁)⊘𝝈,\mathbf{x}\_{\mathrm{norm}}=(\mathbf{x}\_{\mathrm{raw}}-\boldsymbol{\mu})\oslash\boldsymbol{\sigma}, |  | (13) |

where (𝝁,𝝈)(\boldsymbol{\mu},\boldsymbol{\sigma}) are estimated by randomly sampling
min⁡(nnorm,|train|)\min(n\_{\text{norm}},|{\rm train}|) images from the training split (default nnorm=512n\_{\text{norm}}=512) without replacement,
computing per-channel statistics over N×H×WN\times H\times W, and clamping σ\sigma to be at least 10−610^{-6}.
When use\_norm is enabled, the model consumes 𝐱norm\mathbf{x}\_{\mathrm{norm}}; otherwise, it consumes 𝐱raw\mathbf{x}\_{\mathrm{raw}}.

#### Valid-range clipping.

Clipping is performed in the space where the attack is executed:
raw inputs are clipped to [0,1][0,1]; standardized inputs are clipped to
[(0−𝝁)⊘𝝈,(1−𝝁)⊘𝝈]\big[(0-\boldsymbol{\mu})\oslash\boldsymbol{\sigma},\ (1-\boldsymbol{\mu})\oslash\boldsymbol{\sigma}\big].

#### Threat model defined in raw space.

The threat model is always defined on 𝐱raw\mathbf{x}\_{\mathrm{raw}} with an ℓ∞\ell\_{\infty} constraint
‖𝜹‖∞≤ϵ\|\boldsymbol{\delta}\|\_{\infty}\leq\epsilon,
where ‖𝜹‖∞=maxi⁡|δi|\|\boldsymbol{\delta}\|\_{\infty}=\max\_{i}|\delta\_{i}|.
When the model consumes standardized inputs, we enforce the same underlying raw-space budget by converting

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϵnorm=ϵ⊘𝝈,αnorm=α⊘𝝈,\epsilon\_{\mathrm{norm}}=\epsilon\oslash\boldsymbol{\sigma},\qquad\alpha\_{\mathrm{norm}}=\alpha\oslash\boldsymbol{\sigma}, |  | (14) |

and then performing clipping/projection in the standardized space. This preserves the raw-space bound after mapping back.

Table 5: Input parameterization and normalization details used in our implementation.

|  |  |
| --- | --- |
| Item | Setting |
| Image storage | 8-bit grayscale per view |
| Load / scaling | ToTensor() ⇒𝐱raw∈[0,1]C×256×256\Rightarrow\mathbf{x}\_{\mathrm{raw}}\in[0,1]^{C\times 256\times 256} |
| Normalization (use\_norm) | 𝐱norm=(𝐱raw−μ)⊘σ\mathbf{x}\_{\mathrm{norm}}=(\mathbf{x}\_{\mathrm{raw}}-\mu)\oslash\sigma |
| μ,σ\mu,\sigma estimation | Randomly sample min⁡(nnorm,|train|)\min(n\_{\text{norm}},|{\rm train}|) training images without replacement (default nnorm=512n\_{\text{norm}}{=}512); compute per-channel mean/std over N×H×WN{\times}H{\times}W; clamp σ←max⁡(σ,10−6)\sigma\leftarrow\max(\sigma,10^{-6}) |
| Clipping (raw) | [0,1][0,1] |
| Clipping (norm) | [(0−μ)⊘σ,(1−μ)⊘σ]\big[(0-\mu)\oslash\sigma,(1-\mu)\oslash\sigma\big] |
| Threat model space | raw space; when attacking norm, use Eq. [14](https://arxiv.org/html/2602.11020v1#A1.E14 "In Threat model defined in raw space. ‣ Appendix A Implementation Details for Input Parameterization ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging") |

## Appendix B Model Architecture and Fusion Details

#### Notation.

All models output binary logits. For single-view inputs, C=1C{=}1; for two-view inputs, C=2C{=}2 where the two views are stacked channel-wise. In late-fusion models, the input is split as 𝐱a=𝐱[:,0:1]\mathbf{x}\_{a}=\mathbf{x}[:,0{:}1] and 𝐱b=𝐱[:,1:2]\mathbf{x}\_{b}=\mathbf{x}[:,1{:}2].

#### Lite-CNN.

Our Lite-CNN baseline is a compact CNN with three convolution blocks and two pooling operations, followed by a 2-layer MLP head. Concretely:
(1) Conv3×3​(C→16)\mathrm{Conv}\_{3\times 3}(C\!\rightarrow\!16) + ReLU;
(2) Conv3×3​(16→16)\mathrm{Conv}\_{3\times 3}(16\!\rightarrow\!16) + ReLU + MaxPool​(2,2)\mathrm{MaxPool}(2,2);
(3) Conv3×3​(16→32)\mathrm{Conv}\_{3\times 3}(16\!\rightarrow\!32) + ReLU + MaxPool​(3,3)\mathrm{MaxPool}(3,3);
then flatten and an MLP head Linear(⋅→256)→Dropout→Linear(256→128)→Linear(128→2)\mathrm{Linear}(\cdot\!\rightarrow\!256)\!\rightarrow\!\mathrm{Dropout}\!\rightarrow\!\mathrm{Linear}(256\!\rightarrow\!128)\!\rightarrow\!\mathrm{Linear}(128\!\rightarrow\!2).
The flatten dimension is inferred automatically from the input resolution (256×\times256).

#### ResNet18-P.

We use a ResNet-18 backbone initialized from ImageNet weights. The first convolution layer is adapted to accept C∈{1,2}C\in\{1,2\} channels by transforming the original 3-channel weights (e.g., averaging for C=1C{=}1, copying/truncating for C=2C{=}2), while keeping the rest of the architecture unchanged. We split the network into a *trunk* (up to global average pooling, producing a 512-d feature) and a *head* (Dropout + Linear(512→2)(512\!\rightarrow\!2)).

#### Late fusion with optional consistency (\*-Cons).

For two-view late fusion, we use two independent encoders (*branches*) that each process one view:
𝐟a=ga​(𝐱a)\mathbf{f}\_{a}=g\_{a}(\mathbf{x}\_{a}) and 𝐟b=gb​(𝐱b)\mathbf{f}\_{b}=g\_{b}(\mathbf{x}\_{b}).
The *fused head* predicts from concatenated features
𝐟=[𝐟a;𝐟b]\mathbf{f}=[\mathbf{f}\_{a};\mathbf{f}\_{b}] via Dropout + Linear(2​d→2)(2d\!\rightarrow\!2) (where d=128d{=}128 for Lite-CNN trunks and d=512d{=}512 for ResNet trunks).
Additionally, for consistency-regularized models, we attach lightweight *branch heads* (Linear(d→2)(d\!\rightarrow\!2)) that output auxiliary logits used only for the consistency term; the main task loss is computed on the fused logits.

Table 6: Implementation-level summary of model backbones and fusion heads.
Here CC is the number of input channels (1 for single-view; 2 for early-fusion two-view). For late fusion, each branch consumes one channel and the fused head operates on concatenated features.

| Component | Lite-CNN | ResNet18-P |
| --- | --- | --- |
| Single-view encoder (C=1C{=}1) | 33 conv blocks + pools; MLP head (256, 128) | ResNet-18 trunk (512-d) + Dropout + Linear(512→2)(512\!\rightarrow\!2) |
| Early fusion two-view (C=2C{=}2) | Same network with C=2C{=}2 at input (channel stacking) | Same network with C=2C{=}2 at input (adapted first conv) |
| Late fusion encoders (\*-Cons) | Two Lite-CNN trunks (C=1C{=}1 each), output d=128d{=}128 | Two ResNet-18 trunks (C=1C{=}1 each), output d=512d{=}512 |
| Fused head (\*-Cons) | Dropout + Linear(256→2)(256\!\rightarrow\!2) | Dropout + Linear(1024→2)(1024\!\rightarrow\!2) |
| Branch heads (for consistency) | Linear(128→2)(128\!\rightarrow\!2) for each branch | Dropout + Linear(512→2)(512\!\rightarrow\!2) for each branch |

## Appendix C Additional Evaluation Details

#### From probabilities to labels.

Unless stated otherwise, we obtain binary predictions by thresholding the predicted positive-class probability at 0.50.5 and compute MCC from the resulting confusion matrix.

#### Reporting.

We report mean±\pmstd over n=8n{=}8 runs with different random seeds.
Unless otherwise stated, the seed set is fixed to {1,2,3,4,5,6,7,8}\{1,2,3,4,5,6,7,8\} for all deep models to enable controlled comparisons across ablations.
For non-learning (Majority) and deterministic baselines (LogReg), we run once (n=1n{=}1) unless explicitly noted.

## Appendix D Attack Hyperparameters and Implementation Notes

#### Perturbation budgets.

Unless stated otherwise, perturbation budgets are defined in raw [0,1][0,1] pixel space under an ℓ∞\ell\_{\infty} constraint.
We follow the main text and evaluate ϵ∈E\epsilon\in E defined in Eq. (4), where ϵ=0\epsilon=0 corresponds to clean evaluation.
When sweeping budgets, we run the evaluation once per ϵ\epsilon.
Table [7](https://arxiv.org/html/2602.11020v1#A4.T7 "Table 7 ‣ PGD (multi-step). ‣ Appendix D Attack Hyperparameters and Implementation Notes ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging") summarizes the attack settings.

#### Loss and attack objective.

All attacks are *untargeted* and maximize the cross-entropy loss with respect to the true label:

|  |  |  |
| --- | --- | --- |
|  | max‖𝜹‖∞≤ϵ⁡ℒCE​(f​(𝐱+𝜹),y).\max\_{\|\boldsymbol{\delta}\|\_{\infty}\leq\epsilon}\ \mathcal{L}\_{\mathrm{CE}}\!\left(f(\mathbf{x}+\boldsymbol{\delta}),y\right). |  |

Here 𝐱\mathbf{x} denotes the raw [0,1][0,1] input; when the model consumes standardized inputs, we optimize in the standardized space using the converted budget in Eq. [14](https://arxiv.org/html/2602.11020v1#A1.E14 "In Threat model defined in raw space. ‣ Appendix A Implementation Details for Input Parameterization ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging").

#### FGSM (one-step).

FGSM is implemented as a single-step update followed by clipping to the valid input range.

#### PGD (multi-step).

PGD performs K=10K=10 iterative updates with step size α=ϵ/K\alpha=\epsilon/K and projects after each step to enforce the ℓ∞\ell\_{\infty} constraint.
We disable random initialization within the ℓ∞\ell\_{\infty} ball (random\_start=False).

Table 7: Attack settings used in our experiments. Budgets are defined in raw [0,1][0,1] space. When attacking standardized inputs, we convert (ϵ,α)(\epsilon,\alpha) using Eq. [14](https://arxiv.org/html/2602.11020v1#A1.E14 "In Threat model defined in raw space. ‣ Appendix A Implementation Details for Input Parameterization ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging").

| Attack | Objective | Budget | Steps KK | Step size α\alpha | Random init. |
| --- | --- | --- | --- | --- | --- |
| FGSM | untargeted CE (maximize) | ϵ∈E\epsilon\in E | 1 | α=ϵ\alpha=\epsilon | No |
| PGD | untargeted CE (maximize) | ϵ∈E\epsilon\in E | 10 | α=ϵ/10\alpha=\epsilon/10 | No |

## Appendix E Additional Stress Test at ϵadv=2/255\epsilon\_{\mathrm{adv}}=2/255

#### Why include 2/2552/255.

We exclude 2/2552/255 from the main budget grid to focus on imperceptible perturbations, but report it here as an additional stress test.

#### Key observation.

Under the indic-only PGD attack (ch1), Lite-CNN-Cons (λ=1\lambda=1) still remains above zero MCC at ϵadv=2/255\epsilon\_{\mathrm{adv}}=2/255 (mean±\pmstd over seeds).
Table [8](https://arxiv.org/html/2602.11020v1#A5.T8 "Table 8 ‣ Key observation. ‣ Appendix E Additional Stress Test at ϵ_adv=2/255 ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging") summarizes the results.

Table 8: PGD robustness stress test including ϵadv=2/255\epsilon\_{\mathrm{adv}}=2/255.
We report MCC at two representative budgets (0.25/2550.25/255 and 2/2552/255) and the worst-case drop Δworst\Delta\_{\mathrm{worst}} over nonzero budgets (Eq. ([9](https://arxiv.org/html/2602.11020v1#S4.E9 "In 4.3 Evaluation and Summary Metrics ‣ 4 Threat Model and Evaluation Protocol ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging"))).

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Model | Input | Attack (PGD) | MCC@0 | MCC@0.25/255 | MCC@2/255 | 𝚫𝐰𝐨𝐫𝐬𝐭\boldsymbol{\Delta\_{\mathrm{worst}}} |
| Lite-CNN | ohlcv | on ohlcv | 0.109 | 0.054 | -0.271 | -0.380 |
| Lite-CNN | indic | on indic | 0.079 | 0.024 | -0.450 | -0.529 |
| Lite-CNN | both (early) | on ohlcv (ch0) | 0.089 | 0.030 | -0.318 | -0.407 |
| Lite-CNN | both (early) | on indic (ch1) | 0.089 | 0.033 | -0.302 | -0.391 |
| Lite-CNN | both (early) | on both | 0.089 | -0.014 | -0.611 | -0.700 |
| Lite-CNN-Cons (λ=1\lambda{=}1) | both (late) | on ohlcv (ch0) | 0.121 | 0.081 | -0.199 | -0.319 |
| Lite-CNN-Cons (λ=1\lambda{=}1) | both (late) | on indic (ch1) | 0.121 | 0.113 | 0.048 | -0.073 |
| Lite-CNN-Cons (λ=1\lambda{=}1) | both (late) | on both | 0.121 | 0.071 | -0.278 | -0.398 |
| ResNet18-P | ohlcv | on ohlcv | 0.019 | -0.443 | -0.996 | -1.015 |
| ResNet18-P | indic | on indic | 0.082 | -0.999 | -1.000 | -1.082 |
| ResNet18-P-Cons (λ=1\lambda{=}1) | both (late) | on ohlcv (ch0) | 0.095 | -0.211 | -0.961 | -1.056 |
| ResNet18-P-Cons (λ=1\lambda{=}1) | both (late) | on indic (ch1) | 0.095 | -0.959 | -1.000 | -1.095 |
| ResNet18-P-Cons (λ=1\lambda{=}1) | both (late) | on both | 0.095 | -0.983 | -1.000 | -1.095 |

## Appendix F Full Branch Diagnostics for Late-Fusion Models

This section reports the full branch-level diagnostics for late-fusion models on the clean test set.
Tables [9](https://arxiv.org/html/2602.11020v1#A6.T9 "Table 9 ‣ Appendix F Full Branch Diagnostics for Late-Fusion Models ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging")–[11](https://arxiv.org/html/2602.11020v1#A6.T11 "Table 11 ‣ Appendix F Full Branch Diagnostics for Late-Fusion Models ‣ When Fusion Helps and When It Breaks: View-Aligned Robustness in Same-Source Financial Imaging") provide confidence, class-probability means, and branch-vs-fused MCC, respectively.

Table 9: Full clean-test confidence diagnostics for late-fusion two-view models (τ=0.006\tau=0.006, T=2T=2).
Mean±\pmstd over n=8n{=}8 seeds. conf\_\* denotes mean max-probability (branch confidences computed on temperature-scaled distributions with T=2T=2; fused confidence on softmax​(zf)\mathrm{softmax}(z\_{f})).

| Model | 𝝀\boldsymbol{\lambda} | conf\_a | conf\_b | conf\_f |
| --- | --- | --- | --- | --- |
| Lite-CNN-Cons | 0 | 0.627352±0.0702570.627352\pm 0.070257 | 0.554910±0.0207640.554910\pm 0.020764 | 0.917221±0.0074780.917221\pm 0.007478 |
| Lite-CNN-Cons | 0.5 | 0.508533±0.0045370.508533\pm 0.004537 | 0.506999±0.0038420.506999\pm 0.003842 | 0.913617±0.0051660.913617\pm 0.005166 |
| Lite-CNN-Cons | 1 | 0.507229±0.0047630.507229\pm 0.004763 | 0.507287±0.0054930.507287\pm 0.005493 | 0.913873±0.0074140.913873\pm 0.007414 |
| ResNet18P-Cons | 0 | 0.570899±0.0434810.570899\pm 0.043481 | 0.567578±0.0408660.567578\pm 0.040866 | 0.782159±0.0780040.782159\pm 0.078004 |
| ResNet18P-Cons | 0.5 | 0.605562±0.0658670.605562\pm 0.065867 | 0.611589±0.0660480.611589\pm 0.066048 | 0.802972±0.0565610.802972\pm 0.056561 |
| ResNet18P-Cons | 1 | 0.622989±0.0839760.622989\pm 0.083976 | 0.624896±0.0827310.624896\pm 0.082731 | 0.808066±0.0484490.808066\pm 0.048449 |




Table 10: Full clean-test positive-class probability means for late-fusion two-view models (τ=0.006\tau=0.006, T=2T=2).
Mean±\pmstd over n=8n{=}8 seeds. pos\_mean\_\* denotes the mean positive-class probability (branch means computed on temperature-scaled distributions with T=2T=2; fused mean on softmax​(zf)\mathrm{softmax}(z\_{f})).

| Model | 𝝀\boldsymbol{\lambda} | pos\_mean\_a | pos\_mean\_b | pos\_mean\_f |
| --- | --- | --- | --- | --- |
| Lite-CNN-Cons | 0 | 0.522772±0.1457850.522772\pm 0.145785 | 0.511727±0.0586620.511727\pm 0.058662 | 0.514203±0.0397760.514203\pm 0.039776 |
| Lite-CNN-Cons | 0.5 | 0.502299±0.0094590.502299\pm 0.009459 | 0.499700±0.0083710.499700\pm 0.008371 | 0.511911±0.0562430.511911\pm 0.056243 |
| Lite-CNN-Cons | 1 | 0.498687±0.0085870.498687\pm 0.008587 | 0.498635±0.0093670.498635\pm 0.009367 | 0.520245±0.0686960.520245\pm 0.068696 |
| ResNet18P-Cons | 0 | 0.549286±0.0659360.549286\pm 0.065936 | 0.513286±0.0744540.513286\pm 0.074454 | 0.455765±0.1332880.455765\pm 0.133288 |
| ResNet18P-Cons | 0.5 | 0.592447±0.0852770.592447\pm 0.085277 | 0.590547±0.0959680.590547\pm 0.095968 | 0.483531±0.1352930.483531\pm 0.135293 |
| ResNet18P-Cons | 1 | 0.564726±0.1396560.564726\pm 0.139656 | 0.564738±0.1408850.564738\pm 0.140885 | 0.482701±0.1697480.482701\pm 0.169748 |




Table 11: Branch-wise vs. fused MCC on clean test (τ=0.006\tau=0.006, threshold 0.50.5).
Mean±\pmstd over n=8n{=}8 seeds.

| Model | 𝝀\boldsymbol{\lambda} | mcc\_a | mcc\_b | mcc\_fuse |
| --- | --- | --- | --- | --- |
| Lite-CNN-Cons | 0 | 0.019377±0.0615190.019377\pm 0.061519 | 0.005906±0.0518560.005906\pm 0.051856 | 0.127459±0.0359460.127459\pm 0.035946 |
| Lite-CNN-Cons | 0.5 | 0.001488±0.0532620.001488\pm 0.053262 | −0.001753±0.076580-0.001753\pm 0.076580 | 0.129607±0.0264490.129607\pm 0.026449 |
| Lite-CNN-Cons | 1 | 0.006285±0.0576600.006285\pm 0.057660 | −0.015335±0.052686-0.015335\pm 0.052686 | 0.120755±0.0294680.120755\pm 0.029468 |
| ResNet18P-Cons | 0 | 0.014477±0.0473500.014477\pm 0.047350 | 0.000779±0.0383670.000779\pm 0.038367 | 0.048051±0.0566000.048051\pm 0.056600 |
| ResNet18P-Cons | 0.5 | −0.006042±0.012812-0.006042\pm 0.012812 | −0.002165±0.015076-0.002165\pm 0.015076 | 0.067112±0.0313880.067112\pm 0.031388 |
| ResNet18P-Cons | 1 | −0.002706±0.028186-0.002706\pm 0.028186 | 0.009707±0.0193100.009707\pm 0.019310 | 0.095146±0.0579330.095146\pm 0.057933 |