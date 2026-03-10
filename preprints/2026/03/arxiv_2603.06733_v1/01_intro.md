---
authors:
- Srikumar Nayak
doc_id: arxiv:2603.06733v1
family_id: arxiv:2603.06733
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian
  Uncertainty and Gradient Boosting'
url_abs: http://arxiv.org/abs/2603.06733v1
url_html: https://arxiv.org/html/2603.06733v1
venue: arXiv q-fin
version: 1
year: 2026
---


Srikumar Nayak

###### Abstract

Credit risk scoring must support high-stakes lending decisions where data distributions change over time, probability estimates must be reliable, and group-level fairness is required. While modern machine learning models improve default prediction accuracy, they often produce poorly calibrated scores under distribution shift and may create unfair outcomes when trained without explicit constraints. This paper proposes Calibrated Credit Intelligence (CCI), a deployment-oriented framework that combines (i) a Bayesian neural risk scorer to capture epistemic uncertainty and reduce overconfident errors, (ii) a fairness-constrained gradient boosting model to control group disparities while preserving strong tabular performance, and (iii) a shift-aware fusion strategy followed by post-hoc probability calibration to stabilize decision thresholds in later time periods. We evaluate CCI on the Home Credit Credit Risk Model Stability benchmark using a time-consistent split to reflect real-world drift. Compared with strong baselines (LightGBM, XGBoost, CatBoost, TabNet, and a standalone Bayesian neural model), CCI achieves the best overall trade-off between discrimination, calibration, stability, and fairness. In particular, CCI reaches an AUC-ROC of 0.912 and an AUC-PR of 0.438, improves operational performance with Recall@1%FPR = 0.509, and reduces calibration error (Brier score 0.087, ECE 0.015). Under temporal shift, CCI shows a smaller AUC-PR drop from early to late periods (0.017), and it lowers group disparities (demographic parity gap 0.046, equal opportunity gap 0.037) compared to unconstrained boosting. These results indicate that CCI produces risk scores that are accurate, reliable, and more equitable under realistic deployment conditions.

## I Introduction

Credit risk scoring is a core decision process in lending, where errors can lead to direct financial loss, regulatory issues, and unfair outcomes for applicants. In recent years, machine learning models have shown strong predictive power for default prediction, but their practical value depends on more than raw accuracy. In particular, financial institutions must account for *model risk*, meaning that the model should remain reliable across time, portfolios, and changing economic conditions, and its performance should be judged using risk-aware evaluation rather than only headline metrics [[1](#bib.bib10 "Measuring the model risk-adjusted performance of machine learning algorithms in credit default prediction")]. This is especially important because credit data often contains temporal structure (e.g., multiple timestamps for borrower behavior and repayment patterns), and boosting models have been widely used to exploit such structure effectively [[15](#bib.bib14 "Credit risk modeling on data with two timestamps in peer-to-peer lending by gradient boosting")]. However, even strong boosting models can produce overconfident probabilities, and overconfidence becomes dangerous when the data distribution shifts or when the model is applied to groups that are under-represented in the training data.
  
At the same time, decisioning systems are increasingly expected to provide *uncertainty* and *fairness* guarantees. Uncertainty quantification helps estimate when the model may be wrong, reducing misclassification risk by enabling safer policies such as manual review for high-uncertainty cases [[10](#bib.bib12 "Misclassification risk and uncertainty quantification in deep classifiers")]. In parallel, fair credit scoring has become a major research and policy topic because algorithmic decisions can create or amplify group-level disparities if fairness is not explicitly controlled [[9](#bib.bib13 "Algorithmic decision making methods for fair credit scoring")]. Recent work in financial learning also shows that uncertainty-aware modeling is useful beyond classification, including portfolio decision-making, reinforcing the broader value of uncertainty signals for robust financial decisions [[3](#bib.bib15 "Uncertainty-aware reinforcement learning for portfolio optimization")]. Motivated by these needs, our work proposes a calibrated, uncertainty-aware, and fairness-controlled credit scoring pipeline that is designed for time-based evaluation and stable probability outputs under distribution shift.
  
Our research contributions are as follows:

* •

  We propose CCI, a unified credit scoring framework that jointly targets discrimination, calibration, fairness, and stability under temporal distribution shift.
* •

  We integrate a Bayesian neural scorer to provide uncertainty-aware default probabilities and explicit signals for risk-sensitive decisioning.
* •

  We incorporate fairness-constrained gradient boosting to control group-level gaps while maintaining strong predictive performance.
* •

  We apply post-hoc calibration and time-consistent evaluation to produce reliable probabilities and stable operating thresholds for real deployment.

The structure of this paper is as follows: Section [II](#S2 "II Related Work ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting") reviews related work; Section [III](#S3 "III Methodology ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting") describes the dataset and preprocessing with the proposed method; Section [IV](#S4 "IV Results and Discussion ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting") reports experimental results and analysis; and Section [V](#S5 "V Conclusion ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting") concludes the paper with future research directions.

## II Related Work

Credit risk modeling has a long history in statistical learning, where logistic regression remains a strong baseline due to its simplicity and regulatory acceptance, but recent work shows that non-linear effects can be added to improve accuracy without losing the structure of classical scoring [[2](#bib.bib2 "Machine learning for credit scoring: improving logistic regression with non-linear decision-tree effects")]. In practice, tree-based methods and ensembles often provide higher predictive power on structured financial data, including boosted attention-based LightGBM designs for digital finance [[13](#bib.bib4 "Hybrid boosted attention-based lightgbm framework for enhanced credit risk assessment in digital finance")] and CatBoost-based ensemble approaches for financial risk prediction [[8](#bib.bib5 "Enhancing financial risk prediction for listed companies: a catboost-based ensemble learning approach")]. Recent applied studies also report competitive performance using common boosting and deep tabular models in combined pipelines (e.g., LightGBM, XGBoost, TabNet, and imbalance-handling strategies), highlighting that careful preprocessing and evaluation protocols strongly influence final results [[14](#bib.bib6 "Advanced user credit risk prediction model using lightgbm, xgboost and tabnet with smoteenn")].
  
A major difficulty for real-world credit scoring is that data distributions change over time due to economic conditions, policy changes, or portfolio shifts. This has motivated transfer learning and domain adaptation methods to reduce performance drop when the target domain differs from the training domain [[11](#bib.bib1 "Credit risk modeling using transfer learning and domain adaptation")]. Temporal effects are also increasingly studied directly, such as spatio-temporal risk modeling for mortgage default probabilities and portfolio behavior [[6](#bib.bib9 "A spatio-temporal machine learning model for mortgage credit risk: default probabilities and loan portfolios")]. Along with shift robustness, hybrid architectures have been explored to combine the strengths of boosting and deep learning, for example a two-stage design that uses XGBoost followed by a graph-based neural network to capture additional structure in credit data [[7](#bib.bib3 "A two-stage hybrid credit risk prediction model based on xgboost and graph-based deep neural network")]. These directions show that strong accuracy on static splits is not enough; models must remain stable when the operating environment changes.
  
In parallel, recent work has focused on *decision trustworthiness*, especially uncertainty and fairness. Bayesian neural networks have been applied in lending settings to produce probabilistic predictions with uncertainty that can support safer decisioning under ambiguity [[4](#bib.bib7 "Investment decision making for large-scale peer-to-peer lending data: a bayesian neural network approach")]. Fairness-aware learning for boosting models has also been studied, showing practical ways to control group-level ranking or outcome gaps while maintaining utility [[12](#bib.bib8 "Toward fairness-aware gradient boosting decision trees for ranking")]. Motivated by these findings, our work aligns these goals in a single deployment-oriented framework: we combine a Bayesian neural scorer for uncertainty-aware risk estimation [[4](#bib.bib7 "Investment decision making for large-scale peer-to-peer lending data: a bayesian neural network approach")], a fairness-constrained gradient boosting component for controlled group behavior [[12](#bib.bib8 "Toward fairness-aware gradient boosting decision trees for ranking")], and a time-consistent stability evaluation aligned with shift-aware modeling [[11](#bib.bib1 "Credit risk modeling using transfer learning and domain adaptation"), [6](#bib.bib9 "A spatio-temporal machine learning model for mortgage credit risk: default probabilities and loan portfolios")]. This integration addresses the common gap where accuracy, calibration, shift robustness, and fairness are often treated as separate problems rather than solved together in one credit scoring pipeline.

## III Methodology

### III-A Dataset

In this research, we utilize the Home Credit, Credit Risk Model Stability dataset, released through a public Kaggle competition. The dataset is organized as a *base table* (train\_base) and a large collection of *feature tables* derived from multiple internal and external sources, provided in both CSV and Parquet formats. The base table contains one row per loan application (unique key case\_id) and includes the decision date (date\_decision), a week index (WEEK\_NUM), a month index (MONTH), and the binary default label target. The week index is designed for stability evaluation and enables time-consistent validation because the test period continues sequentially after the training weeks. The remaining feature tables contain attributes at different aggregation depths (some tables are already one-row-per-case\_id, while others contain multiple rows per case and require aggregation), and some sources are split across multiple files that must be unioned before feature construction [[5](#bib.bib11 "Home credit - credit risk model stability")].

#### III-A1 Preprocessing

Let the base table define the supervised learning set

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒟={(idi,di,wi,yi)}i=1N,\mathcal{D}=\left\{\left(\mathrm{id}\_{i},\,\mathrm{d}\_{i},\,w\_{i},\,y\_{i}\right)\right\}\_{i=1}^{N}, |  | (1) |

where idi\mathrm{id}\_{i} is case\_id, di\mathrm{d}\_{i} is the decision date, wiw\_{i} is WEEK\_NUM, and yi∈{0,1}y\_{i}\in\{0,1\} is the default indicator (Eq. ([1](#S3.E1 "In III-A1 Preprocessing ‣ III-A Dataset ‣ III Methodology ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting"))). For each auxiliary table 𝒯(m)\mathcal{T}^{(m)} (e.g., previous applications, credit bureau, person-level, tax registry), we first union all parts that belong to the same source (e.g., \_0, \_1 file splits), and then aggregate to one feature vector per case. Formally, let 𝐮r(m)\mathbf{u}\_{r}^{(m)} be the raw feature vector for record rr in table 𝒯(m)\mathcal{T}^{(m)}, and define the record set for case ii as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛi(m)={r∈𝒯(m):id​(r)=idi}.\mathcal{R}\_{i}^{(m)}=\left\{r\in\mathcal{T}^{(m)}:\ \mathrm{id}(r)=\mathrm{id}\_{i}\right\}. |  | (2) |

We produce a fixed-length aggregated representation using a small set of stable pooling operators 𝒜={mean,max,min,sum,last}\mathcal{A}=\{\mathrm{mean},\mathrm{max},\mathrm{min},\mathrm{sum},\mathrm{last}\} applied feature-wise:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐚i(m)=Γ(m)​({𝐮r(m)}r∈ℛi(m)),Γ(m)≜⨁g∈𝒜g​(⋅),\mathbf{a}\_{i}^{(m)}=\Gamma^{(m)}\!\left(\{\mathbf{u}\_{r}^{(m)}\}\_{r\in\mathcal{R}\_{i}^{(m)}}\right),\qquad\Gamma^{(m)}\triangleq\bigoplus\_{g\in\mathcal{A}}g(\cdot), |  | (3) |

where ⊕\oplus denotes concatenation across aggregators (Eq. ([3](#S3.E3 "In III-A1 Preprocessing ‣ III-A Dataset ‣ III Methodology ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting"))). After aggregation, all sources are merged into a single case-level feature vector

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐱i=[𝐛i;𝐚i(1);𝐚i(2);⋯;𝐚i(M)]∈ℝd,\mathbf{x}\_{i}=\left[\mathbf{b}\_{i};\ \mathbf{a}\_{i}^{(1)};\ \mathbf{a}\_{i}^{(2)};\ \cdots;\ \mathbf{a}\_{i}^{(M)}\right]\in\mathbb{R}^{d}, |  | (4) |

where 𝐛i\mathbf{b}\_{i} contains base fields (excluding yiy\_{i}) and MM is the number of feature-table groups (Eq. ([4](#S3.E4 "In III-A1 Preprocessing ‣ III-A Dataset ‣ III Methodology ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting"))).

##### Time-consistent split (distribution shift control).

To evaluate robustness under temporal distribution shift, we avoid random splits and instead use a chronological split based on wiw\_{i}. For a cut week w⋆w^{\star}, we define

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒟train={(𝐱i,yi,wi):wi≤w⋆},𝒟test={(𝐱i,yi,wi):wi>w⋆}.\mathcal{D}\_{\mathrm{train}}=\left\{(\mathbf{x}\_{i},y\_{i},w\_{i}):w\_{i}\leq w^{\star}\right\},\qquad\\ \mathcal{D}\_{\mathrm{test}}=\left\{(\mathbf{x}\_{i},y\_{i},w\_{i}):w\_{i}>w^{\star}\right\}. |  | (5) |

All preprocessing statistics (imputation values, encoding maps, scaling parameters) are estimated only on 𝒟train\mathcal{D}\_{\mathrm{train}} and then applied to 𝒟test\mathcal{D}\_{\mathrm{test}}, which prevents leakage across time and aligns evaluation with Eq. ([5](#S3.E5 "In Time-consistent split (distribution shift control). ‣ III-A1 Preprocessing ‣ III-A Dataset ‣ III Methodology ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting")).

##### Missing values and indicators.

Let xi​jx\_{ij} denote the jj-th feature of case ii. We create a missingness indicator

|  |  |  |  |
| --- | --- | --- | --- |
|  | mi​j={1,if ​xi​j​is observed,0,otherwise,m\_{ij}=\begin{cases}1,&\text{if }x\_{ij}\ \text{is observed},\\ 0,&\text{otherwise},\end{cases} |  | (6) |

and append 𝐦i=[mi​1,…,mi​d]\mathbf{m}\_{i}=[m\_{i1},\dots,m\_{id}] to the model input so that missingness itself can be informative (Eq. ([6](#S3.E6 "In Missing values and indicators. ‣ III-A1 Preprocessing ‣ III-A Dataset ‣ III Methodology ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting"))). For numerical variables, we use train-only median imputation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | xi​j′=mi​j​xi​j+(1−mi​j)​median𝒟train​(x⋅j),x^{\prime}\_{ij}=m\_{ij}\,x\_{ij}+(1-m\_{ij})\,\mathrm{median}\_{\mathcal{D}\_{\mathrm{train}}}(x\_{\cdot j}), |  | (7) |

which is robust to heavy-tailed financial attributes (Eq. ([7](#S3.E7 "In Missing values and indicators. ‣ III-A1 Preprocessing ‣ III-A Dataset ‣ III Methodology ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting"))). For categorical variables, missing tokens are mapped to a dedicated UNK category using a train-built vocabulary.

##### Categorical encoding and numeric scaling.

Because we use both gradient boosting and Bayesian neural models later, we apply a consistent and stable encoding step. For each categorical field ci​jc\_{ij}, we use frequency encoding computed on the training set:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϕj​(c)=∑i∈𝒟train𝕀​[ci​j=c]|𝒟train|,xi​j′←ϕj​(ci​j),\phi\_{j}(c)=\frac{\sum\_{i\in\mathcal{D}\_{\mathrm{train}}}\mathbb{I}[c\_{ij}=c]}{|\mathcal{D}\_{\mathrm{train}}|},\qquad x^{\prime}\_{ij}\leftarrow\phi\_{j}(c\_{ij}), |  | (8) |

where 𝕀​[⋅]\mathbb{I}[\cdot] is an indicator function (Eq. ([8](#S3.E8 "In Categorical encoding and numeric scaling. ‣ III-A1 Preprocessing ‣ III-A Dataset ‣ III Methodology ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting"))). For numerical stability in probabilistic modeling, we standardize continuous features using train-only moments:

|  |  |  |  |
| --- | --- | --- | --- |
|  | x^i​j=xi​j′−μjσj+ε,μj=𝔼𝒟train​[x⋅j′],σj=Var𝒟train​(x⋅j′),\hat{x}\_{ij}=\frac{x^{\prime}\_{ij}-\mu\_{j}}{\sigma\_{j}+\varepsilon},\qquad\mu\_{j}=\mathbb{E}\_{\mathcal{D}\_{\mathrm{train}}}[x^{\prime}\_{\cdot j}],\quad\sigma\_{j}=\sqrt{\mathrm{Var}\_{\mathcal{D}\_{\mathrm{train}}}(x^{\prime}\_{\cdot j})}, |  | (9) |

with a small ε>0\varepsilon>0 to avoid division by zero (Eq. ([9](#S3.E9 "In Categorical encoding and numeric scaling. ‣ III-A1 Preprocessing ‣ III-A Dataset ‣ III Methodology ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting"))). The final learning input for each case is thus [𝐱^i;𝐦i]\left[\hat{\mathbf{x}}\_{i};\mathbf{m}\_{i}\right], which preserves both scaled values and missingness patterns defined by Eq. ([6](#S3.E6 "In Missing values and indicators. ‣ III-A1 Preprocessing ‣ III-A Dataset ‣ III Methodology ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting")).

Home Credit
Base + Feature Tables

Preprocess
(merge, encode, split)

BNN Risk Scorer
μbnn,uepi\mu\_{\mathrm{bnn}},\,u\_{\mathrm{epi}}

Fair-GBDT
μgbdt\mu\_{\mathrm{gbdt}}

Fusion
s~​(𝐱)\tilde{s}(\mathbf{x})

Calibration
s^​(𝐱)\hat{s}(\mathbf{x})

Shift Check
DshiftD\_{\mathrm{shift}}

Fairness Audit
ΔDP,ΔEO\Delta\_{\mathrm{DP}},\Delta\_{\mathrm{EO}}

Explainability
(SHAP)

Figure 1: CCI pipeline: preprocessing feeds a Bayesian scorer and a fairness-constrained booster; their outputs are fused under shift checks and then calibrated for reliable risk probabilities.

### III-B Proposed Method: Calibrated Credit Intelligence (CCI)

CCI follows the compact pipeline in Fig. [1](#S3.F1 "Figure 1 ‣ Categorical encoding and numeric scaling. ‣ III-A1 Preprocessing ‣ III-A Dataset ‣ III Methodology ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting"): we first build a time-consistent feature set, then compute uncertainty-aware risk from the BNN and fairness-controlled risk from the GBDT, fuse both scores using shift validation, and finally calibrate the output probability for stable decision thresholds.

Input: 
𝒟train,𝒟val,𝒟test\mathcal{D}\_{\mathrm{train}},\mathcal{D}\_{\mathrm{val}},\mathcal{D}\_{\mathrm{test}} (time split);
ai∈𝒜a\_{i}\!\in\!\mathcal{A};
σ0\sigma\_{0};
Eb,ηb,SE\_{\mathrm{b}},\eta\_{\mathrm{b}},S;
Eg,ηg,ΔmaxE\_{\mathrm{g}},\eta\_{\mathrm{g}},\Delta\_{\max};
TcalT\_{\mathrm{cal}}

Output: s^​(𝐱)\hat{s}(\mathbf{x}), (uepi,uale)(u\_{\mathrm{epi}},u\_{\mathrm{ale}}), fairness metrics

// Step 1: Train Bayesian Neural Risk Scorer (BNN)

Initialize variational parameters λ←λ0\lambda\leftarrow\lambda\_{0} for qλ​(𝐖)q\_{\lambda}(\mathbf{W})

for *e←1e\leftarrow 1 to EbE\_{\mathrm{b}}* do

Sample mini-batch ℬ⊂𝒟train\mathcal{B}\subset\mathcal{D}\_{\mathrm{train}}

λ←λ−ηb​∇λℒELBO​(ℬ;λ,σ0)\lambda\leftarrow\lambda-\eta\_{\mathrm{b}}\nabla\_{\lambda}\mathcal{L}\_{\mathrm{ELBO}}(\mathcal{B};\lambda,\sigma\_{0})

// Step 2: Train fairness-constrained Gradient Boosting model (GBDT)

Initialize tree ensemble parameters Ω←Ω0\Omega\leftarrow\Omega\_{0}

for *t←1t\leftarrow 1 to EgE\_{\mathrm{g}}* do

Ω←Ω+ηg⋅FitTree​(𝒟train,Ω,Δmax)\Omega\leftarrow\Omega+\eta\_{\mathrm{g}}\cdot\mathrm{FitTree}(\mathcal{D}\_{\mathrm{train}},\Omega,\Delta\_{\max})

// Step 3: Validate distribution shift and select fusion weight

Dshift←DriftTest​(𝒟train,𝒟val)D\_{\mathrm{shift}}\leftarrow\mathrm{DriftTest}(\mathcal{D}\_{\mathrm{train}},\mathcal{D}\_{\mathrm{val}})

β←SelectWeight​(Dshift,𝒟val)\beta\leftarrow\mathrm{SelectWeight}(D\_{\mathrm{shift}},\mathcal{D}\_{\mathrm{val}})

// Step 4: Fused risk score + uncertainty (val/test)

foreach *𝐱\mathbf{x} in 𝒟val∪𝒟test\mathcal{D}\_{\mathrm{val}}\cup\mathcal{D}\_{\mathrm{test}}* do

Draw {𝐖(s)}s=1S∼qλ​(𝐖)\{\mathbf{W}^{(s)}\}\_{s=1}^{S}\sim q\_{\lambda}(\mathbf{W})

μbnn​(𝐱)←1S​∑s=1Sp​(y=1∣𝐱,𝐖(s))\mu\_{\mathrm{bnn}}(\mathbf{x})\leftarrow\frac{1}{S}\sum\_{s=1}^{S}p(y=1\mid\mathbf{x},\mathbf{W}^{(s)})

uepi​(𝐱)←Vars​(p​(y=1∣𝐱,𝐖(s)))u\_{\mathrm{epi}}(\mathbf{x})\leftarrow\mathrm{Var}\_{s}\!\left(p(y=1\mid\mathbf{x},\mathbf{W}^{(s)})\right)

uale​(𝐱)←1S​∑s=1Sμ(s)​(𝐱)​(1−μ(s)​(𝐱))u\_{\mathrm{ale}}(\mathbf{x})\leftarrow\frac{1}{S}\sum\_{s=1}^{S}\mu^{(s)}(\mathbf{x})\!\left(1-\mu^{(s)}(\mathbf{x})\right)

μgbdt​(𝐱)←Sigmoid​(fΩ​(𝐱))\mu\_{\mathrm{gbdt}}(\mathbf{x})\leftarrow\mathrm{Sigmoid}\!\left(f\_{\Omega}(\mathbf{x})\right)

s~​(𝐱)←β​μgbdt​(𝐱)+(1−β)​μbnn​(𝐱)\tilde{s}(\mathbf{x})\leftarrow\beta\,\mu\_{\mathrm{gbdt}}(\mathbf{x})+(1-\beta)\,\mu\_{\mathrm{bnn}}(\mathbf{x})

// Step 5: Post-hoc calibration on validation weeks

Fit TcalT\_{\mathrm{cal}} on 𝒟val\mathcal{D}\_{\mathrm{val}} via NLL minimization

s^​(𝐱)←Calibrate​(s~​(𝐱);Tcal)\hat{s}(\mathbf{x})\leftarrow\mathrm{Calibrate}(\tilde{s}(\mathbf{x});T\_{\mathrm{cal}})

// Step 6: Fairness audit and explanation

Compute ΔDP,ΔEO,ΔTPR,ΔFPR\Delta\_{\mathrm{DP}},\Delta\_{\mathrm{EO}},\Delta\_{\mathrm{TPR}},\Delta\_{\mathrm{FPR}} on 𝒟val,𝒟test\mathcal{D}\_{\mathrm{val}},\mathcal{D}\_{\mathrm{test}}

Generate explanations: Attr​(𝐱)←SHAP​(fΩ,𝐱)\mathrm{Attr}(\mathbf{x})\leftarrow\mathrm{SHAP}\!\left(f\_{\Omega},\mathbf{x}\right)

return s^​(⋅)\hat{s}(\cdot), (uepi,uale)(u\_{\mathrm{epi}},u\_{\mathrm{ale}}), fairness report

Algorithm 1 CCI: Calibrated Credit Intelligence with Bayesian Neural Risk Scoring under Distribution Shift and Fairness-Constrained Gradient Boosting

Algorithm [1](#algorithm1 "In III-B Proposed Method: Calibrated Credit Intelligence (CCI) ‣ III Methodology ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting") describes our Calibrated Credit Intelligence (CCI) pipeline, designed for credit risk scoring under distribution shift, with explicit calibration, fairness control, and interpretable uncertainty. We work with a time-ordered dataset 𝒟train={(𝐱i,yi,wi,ai)}i=1N\mathcal{D}\_{\mathrm{train}}=\{(\mathbf{x}\_{i},y\_{i},w\_{i},a\_{i})\}\_{i=1}^{N} where 𝐱i∈ℝd\mathbf{x}\_{i}\in\mathbb{R}^{d} is the feature vector, yi∈{0,1}y\_{i}\in\{0,1\} is the default label, wiw\_{i} is the week index (used for time-consistent splits), and ai∈𝒜a\_{i}\in\mathcal{A} is a sensitive attribute used only for fairness audit and constraint checking. The main output is a calibrated probability score s^​(𝐱)∈(0,1)\hat{s}(\mathbf{x})\in(0,1) representing P​(y=1∣𝐱)P(y=1\mid\mathbf{x}).
  
The first component is a Bayesian neural network (BNN) that provides both a risk estimate and uncertainty. Instead of learning a single weight vector, the BNN learns a distribution over weights using a variational approximation qλ​(𝐖)q\_{\lambda}(\mathbf{W}) parameterized by λ\lambda. Training is performed by minimizing a negative evidence lower bound (ELBO), which balances data fit and regularization toward a prior p​(𝐖)p(\mathbf{W}):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒELBO​(λ)=−𝔼qλ​(𝐖)​[∑i∈𝒟trainlog⁡p​(yi∣𝐱i,𝐖)]+KL​(qλ​(𝐖)∥p​(𝐖)).\mathcal{L}\_{\mathrm{ELBO}}(\lambda)=-\mathbb{E}\_{q\_{\lambda}(\mathbf{W})}\!\Big[\sum\_{i\in\mathcal{D}\_{\mathrm{train}}}\log p(y\_{i}\mid\mathbf{x}\_{i},\mathbf{W})\Big]+\mathrm{KL}\!\left(q\_{\lambda}(\mathbf{W})\,\|\,p(\mathbf{W})\right). |  | (10) |

Eq. ([10](#S3.E10 "In III-B Proposed Method: Calibrated Credit Intelligence (CCI) ‣ III Methodology ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting")) is important for two reasons: it prevents overfitting through the KL term, and it enables meaningful uncertainty estimates because the prediction depends on sampled weights rather than fixed weights. After training, we compute the BNN predictive mean using SS Monte Carlo samples:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μbnn​(𝐱)=1S​∑s=1Sp​(y=1∣𝐱,𝐖(s)),𝐖(s)∼qλ​(𝐖),\mu\_{\mathrm{bnn}}(\mathbf{x})=\frac{1}{S}\sum\_{s=1}^{S}p(y=1\mid\mathbf{x},\mathbf{W}^{(s)}),\qquad\mathbf{W}^{(s)}\sim q\_{\lambda}(\mathbf{W}), |  | (11) |

where Eq. ([11](#S3.E11 "In III-B Proposed Method: Calibrated Credit Intelligence (CCI) ‣ III Methodology ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting")) produces the uncertainty-aware risk estimate by averaging across different plausible parameter settings.
  
The second component is a gradient boosting decision tree model (GBDT), which is strong for structured credit data and often remains stable under moderate feature noise. However, pure accuracy optimization can lead to unfair decisions across sensitive groups. For this reason, we train the GBDT using a fairness-regularized objective:

|  |  |  |  |
| --- | --- | --- | --- |
|  | minΩ⁡ℒgbdt​(Ω)=ℒpred​(Ω)+λfair⋅max⁡(0,Δ​(Ω)−Δmax),\min\_{\Omega}\ \mathcal{L}\_{\mathrm{gbdt}}(\Omega)=\mathcal{L}\_{\mathrm{pred}}(\Omega)+\lambda\_{\mathrm{fair}}\cdot\max\big(0,\ \Delta(\Omega)-\Delta\_{\max}\big), |  | (12) |

where Ω\Omega denotes the boosting parameters, ℒpred\mathcal{L}\_{\mathrm{pred}} is the standard prediction loss (e.g., log-loss), Δ​(Ω)\Delta(\Omega) is a fairness gap metric computed on a validation subset, and Δmax\Delta\_{\max} is the allowed tolerance (Eq. ([12](#S3.E12 "In III-B Proposed Method: Calibrated Credit Intelligence (CCI) ‣ III Methodology ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting"))). In simple terms, Eq. ([12](#S3.E12 "In III-B Proposed Method: Calibrated Credit Intelligence (CCI) ‣ III Methodology ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting")) keeps the model accurate while discouraging solutions that exceed an acceptable fairness gap. In our experiments, we track fairness using group-based metrics such as demographic parity difference and equalized odds difference, computed from the predicted labels at an operating threshold.
  
Credit risk is affected by economic cycles and policy changes, so the data distribution changes over time. We therefore use a time-consistent split and measure shift between training weeks and validation weeks. We denote a generic drift score as DshiftD\_{\mathrm{shift}}, computed from feature distributions and/or score distributions:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dshift=DriftTest​(𝒟train,𝒟val).D\_{\mathrm{shift}}=\mathrm{DriftTest}\big(\mathcal{D}\_{\mathrm{train}},\mathcal{D}\_{\mathrm{val}}\big). |  | (13) |

Eq. ([13](#S3.E13 "In III-B Proposed Method: Calibrated Credit Intelligence (CCI) ‣ III Methodology ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting")) is used to guide how much we trust each model in later weeks, because the best model in earlier weeks may not be the best model after a distribution shift.
  
Instead of selecting a single model, we combine the BNN and the fairness-constrained GBDT using a convex fusion:

|  |  |  |  |
| --- | --- | --- | --- |
|  | s~​(𝐱)=β​μgbdt​(𝐱)+(1−β)​μbnn​(𝐱),β∈[0,1],\tilde{s}(\mathbf{x})=\beta\,\mu\_{\mathrm{gbdt}}(\mathbf{x})+(1-\beta)\,\mu\_{\mathrm{bnn}}(\mathbf{x}),\qquad\beta\in[0,1], |  | (14) |

where μgbdt​(𝐱)\mu\_{\mathrm{gbdt}}(\mathbf{x}) is the GBDT probability and μbnn​(𝐱)\mu\_{\mathrm{bnn}}(\mathbf{x}) is the BNN predictive mean (Eq. ([14](#S3.E14 "In III-B Proposed Method: Calibrated Credit Intelligence (CCI) ‣ III Methodology ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting"))). The key idea is simple: when validation indicates stronger shift, we can reduce reliance on the component that becomes uncertain or unstable. To make this behavior explicit, we compute uncertainty from the BNN samples. A practical measure of epistemic uncertainty is the variance of predicted probabilities:

|  |  |  |  |
| --- | --- | --- | --- |
|  | uepi​(𝐱)=Vars​(p​(y=1∣𝐱,𝐖(s))),u\_{\mathrm{epi}}(\mathbf{x})=\mathrm{Var}\_{s}\Big(p(y=1\mid\mathbf{x},\mathbf{W}^{(s)})\Big), |  | (15) |

where higher values of Eq. ([15](#S3.E15 "In III-B Proposed Method: Calibrated Credit Intelligence (CCI) ‣ III Methodology ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting")) mean the model is less confident because different plausible parameters disagree. This uncertainty can be used for monitoring, triage, and risk policy decisions (e.g., sending high-uncertainty cases to manual review).
  
Credit decision pipelines need reliable probabilities, not only good ranking. We therefore apply post-hoc calibration on the validation weeks. We use temperature scaling, where the uncalibrated score s~​(𝐱)\tilde{s}(\mathbf{x}) is mapped to a calibrated probability:

|  |  |  |  |
| --- | --- | --- | --- |
|  | s^​(𝐱)=σ​(logit​(s~​(𝐱))Tcal),logit​(p)=log⁡p1−p,\hat{s}(\mathbf{x})=\sigma\!\left(\frac{\mathrm{logit}(\tilde{s}(\mathbf{x}))}{T\_{\mathrm{cal}}}\right),\qquad\mathrm{logit}(p)=\log\frac{p}{1-p}, |  | (16) |

and the temperature TcalT\_{\mathrm{cal}} is chosen to minimize negative log-likelihood on 𝒟val\mathcal{D}\_{\mathrm{val}} (Eq. ([16](#S3.E16 "In III-B Proposed Method: Calibrated Credit Intelligence (CCI) ‣ III Methodology ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting"))). This step improves calibration metrics such as the Brier score and makes thresholds more stable over time.
  
Finally, we quantify fairness on both validation and test weeks using group-based gaps computed across sensitive groups a∈𝒜a\in\mathcal{A}. For example, demographic parity difference can be written as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ΔDP=maxa∈𝒜⁡P​(y^=1∣a)−mina∈𝒜⁡P​(y^=1∣a),\Delta\_{\mathrm{DP}}=\max\_{a\in\mathcal{A}}\ P(\hat{y}=1\mid a)\ -\ \min\_{a\in\mathcal{A}}\ P(\hat{y}=1\mid a), |  | (17) |

where y^=𝕀​(s^​(𝐱)≥δ)\hat{y}=\mathbb{I}(\hat{s}(\mathbf{x})\geq\delta) is the decision at threshold δ\delta (Eq. ([17](#S3.E17 "In III-B Proposed Method: Calibrated Credit Intelligence (CCI) ‣ III Methodology ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting"))). We also generate feature-level explanations for individual predictions using additive attribution on the boosting component, because tree-based models offer strong, stable explanations in practice. This provides a clear audit trail for why a particular risk score was produced, which is important for operational review and compliance.

In our proposed work, CCI builds a credit scoring pipeline that is designed for real deployment: a BNN provides uncertainty-aware risk estimates (Eq. ([10](#S3.E10 "In III-B Proposed Method: Calibrated Credit Intelligence (CCI) ‣ III Methodology ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting"))–Eq. ([15](#S3.E15 "In III-B Proposed Method: Calibrated Credit Intelligence (CCI) ‣ III Methodology ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting"))), a fairness-constrained GBDT provides strong and controllable tabular performance (Eq. ([12](#S3.E12 "In III-B Proposed Method: Calibrated Credit Intelligence (CCI) ‣ III Methodology ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting"))), both are fused into a robust score under distribution shift (Eq. ([14](#S3.E14 "In III-B Proposed Method: Calibrated Credit Intelligence (CCI) ‣ III Methodology ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting"))), and the final output is calibrated for reliable probability decisions (Eq. ([16](#S3.E16 "In III-B Proposed Method: Calibrated Credit Intelligence (CCI) ‣ III Methodology ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting"))) while being audited for fairness and explained in a simple, actionable way (Eq. ([17](#S3.E17 "In III-B Proposed Method: Calibrated Credit Intelligence (CCI) ‣ III Methodology ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting"))).

## IV Results and Discussion

### IV-A Experimental Protocol and Metrics

We evaluate models using a time-consistent split (train on earlier weeks, validate on later weeks, test on future weeks) to reflect real deployment under distribution shift. We report (i) discrimination (AUC-ROC, AUC-PR), (ii) operational performance (Recall@1%FPR), (iii) calibration quality (Brier score and Expected Calibration Error, ECE), (iv) stability under shift (early vs. late period AUC-PR), and (v) fairness gaps computed across sensitive groups using demographic parity difference ΔDP\Delta\_{\mathrm{DP}} and equal opportunity difference ΔEO\Delta\_{\mathrm{EO}}. All results are reported as mean ±\pm standard deviation over multiple runs with different random seeds and the same tuning budget per model.

### IV-B Main Comparison Results

Table [I](#S4.T1 "TABLE I ‣ IV-B Main Comparison Results ‣ IV Results and Discussion ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting") compares CCI against strong tabular baselines and uncertainty-aware models. CCI achieves the best overall trade-off: it improves AUC-PR and Recall@1%FPR while also reducing calibration error (Brier and ECE). This outcome supports the main design goal of producing risk scores that remain accurate and reliable under temporal shift, rather than only optimizing ranking on a static split.

TABLE I: Main results on Home Credit (Model Stability). Higher is better for AUC-ROC/AUC-PR/Recall@1%FPR (↑\uparrow), and lower is better for Brier/ECE (↓\downarrow). Values are mean ±\pm std over repeated runs.

| Model | AUC-ROC ↑\uparrow | AUC-PR ↑\uparrow | Recall@1%FPR ↑\uparrow | Brier ↓\downarrow | ECE ↓\downarrow |
| --- | --- | --- | --- | --- | --- |
| Logistic Regression [[2](#bib.bib2 "Machine learning for credit scoring: improving logistic regression with non-linear decision-tree effects")] | 0.865±0.0030.865\pm 0.003 | 0.332±0.0040.332\pm 0.004 | 0.410±0.0050.410\pm 0.005 | 0.102±0.0010.102\pm 0.001 | 0.032±0.0020.032\pm 0.002 |
| XGBoost [[7](#bib.bib3 "A two-stage hybrid credit risk prediction model based on xgboost and graph-based deep neural network")] | 0.892±0.0020.892\pm 0.002 | 0.401±0.0030.401\pm 0.003 | 0.468±0.0040.468\pm 0.004 | 0.095±0.0010.095\pm 0.001 | 0.024±0.0010.024\pm 0.001 |
| LightGBM [[13](#bib.bib4 "Hybrid boosted attention-based lightgbm framework for enhanced credit risk assessment in digital finance")] | 0.898±0.0020.898\pm 0.002 | 0.413±0.0030.413\pm 0.003 | 0.482±0.0030.482\pm 0.003 | 0.092±0.0010.092\pm 0.001 | 0.022±0.0010.022\pm 0.001 |
| CatBoost [[8](#bib.bib5 "Enhancing financial risk prediction for listed companies: a catboost-based ensemble learning approach")] | 0.899±0.0020.899\pm 0.002 | 0.418±0.0030.418\pm 0.003 | 0.487±0.0030.487\pm 0.003 | 0.091±0.0010.091\pm 0.001 | 0.021±0.0010.021\pm 0.001 |
| TabNet [[14](#bib.bib6 "Advanced user credit risk prediction model using lightgbm, xgboost and tabnet with smoteenn")] | 0.890±0.0020.890\pm 0.002 | 0.405±0.0030.405\pm 0.003 | 0.471±0.0040.471\pm 0.004 | 0.094±0.0010.094\pm 0.001 | 0.023±0.0010.023\pm 0.001 |
| BNN (uncertainty) [[4](#bib.bib7 "Investment decision making for large-scale peer-to-peer lending data: a bayesian neural network approach")] | 0.888±0.0020.888\pm 0.002 | 0.398±0.0040.398\pm 0.004 | 0.459±0.0040.459\pm 0.004 | 0.093±0.0010.093\pm 0.001 | 0.020±0.0010.020\pm 0.001 |
| Fair-GBDT [[12](#bib.bib8 "Toward fairness-aware gradient boosting decision trees for ranking")] | 0.896±0.0020.896\pm 0.002 | 0.409±0.0030.409\pm 0.003 | 0.476±0.0040.476\pm 0.004 | 0.091±0.0010.091\pm 0.001 | 0.020±0.0010.020\pm 0.001 |
| CCI (Ours) | 0.912±0.002\mathbf{0.912\pm 0.002} | 0.438±0.002\mathbf{0.438\pm 0.002} | 0.509±0.003\mathbf{0.509\pm 0.003} | 0.087±0.001\mathbf{0.087\pm 0.001} | 0.015±0.001\mathbf{0.015\pm 0.001} |

### IV-C Stability Under Distribution Shift

To directly test stability, we compare AUC-PR on an earlier validation period and a later future period. Table [II](#S4.T2 "TABLE II ‣ IV-C Stability Under Distribution Shift ‣ IV Results and Discussion ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting") shows that CCI has the smallest drop from early to late weeks, which indicates better robustness to temporal changes. This is consistent with the model design: fusion reduces sensitivity to shifts, and calibration on later weeks improves probability reliability when the data distribution moves.

TABLE II: Stability under temporal shift (AUC-PR). Smaller drop from early to late indicates better robustness.

| Model | Early AUC-PR ↑\uparrow | Late AUC-PR ↑\uparrow | Drop ↓\downarrow |
| --- | --- | --- | --- |
| LightGBM [[13](#bib.bib4 "Hybrid boosted attention-based lightgbm framework for enhanced credit risk assessment in digital finance")] | 0.426 | 0.392 | 0.034 |
| Fair-GBDT [[12](#bib.bib8 "Toward fairness-aware gradient boosting decision trees for ranking")] | 0.422 | 0.392 | 0.030 |
| CCI (Ours) | 0.448 | 0.431 | 0.017 |

### IV-D Fairness Results

Table [III](#S4.T3 "TABLE III ‣ IV-D Fairness Results ‣ IV Results and Discussion ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting") reports group fairness gaps. The fairness-constrained boosting stage reduces demographic parity and equal opportunity gaps compared to unconstrained boosting, and CCI preserves most of this fairness improvement while also increasing AUC-PR and Recall@1%FPR. This supports the claim that fairness control can be added without fully sacrificing detection quality when the constraint is applied with a clear tolerance and validated on later weeks.

TABLE III: Fairness metrics (lower is better). Values are mean ±\pm std across runs.

| Model | 𝚫𝐃𝐏\boldsymbol{\Delta\_{\mathrm{DP}}} ↓\downarrow | 𝚫𝐄𝐎\boldsymbol{\Delta\_{\mathrm{EO}}} ↓\downarrow |
| --- | --- | --- |
| LightGBM | 0.083±0.0040.083\pm 0.004 | 0.066±0.0040.066\pm 0.004 |
| BNN | 0.078±0.0040.078\pm 0.004 | 0.063±0.0040.063\pm 0.004 |
| Fair-GBDT | 0.052±0.0030.052\pm 0.003 | 0.041±0.0030.041\pm 0.003 |
| CCI (Ours) | 0.046±0.003\mathbf{0.046\pm 0.003} | 0.037±0.003\mathbf{0.037\pm 0.003} |

Figure [2](#S4.F2 "Figure 2 ‣ IV-D Fairness Results ‣ IV Results and Discussion ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting") summarizes AUC-PR across all compared models. Figure [3](#S4.F3 "Figure 3 ‣ IV-D Fairness Results ‣ IV Results and Discussion ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting") shows that CCI produces probabilities closer to observed default frequencies, which explains the lower ECE and Brier values reported in Table [I](#S4.T1 "TABLE I ‣ IV-B Main Comparison Results ‣ IV Results and Discussion ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting"). Figure [4](#S4.F4 "Figure 4 ‣ IV-D Fairness Results ‣ IV Results and Discussion ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting") visualizes stability across the evaluation weeks and confirms the reduced drop reported in Table [II](#S4.T2 "TABLE II ‣ IV-C Stability Under Distribution Shift ‣ IV Results and Discussion ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting"). Finally, Figure [5](#S4.F5 "Figure 5 ‣ IV-D Fairness Results ‣ IV Results and Discussion ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting") highlights the fairness–accuracy trade-off: models with the best AUC-PR often have larger fairness gaps, while CCI stays near the top in AUC-PR and among the lowest in demographic parity gap.

![Refer to caption](2603.06733v1/p2_fig_bar_aucpr.png)


Figure 2: AUC-PR comparison across baselines and CCI (values aligned with Table [I](#S4.T1 "TABLE I ‣ IV-B Main Comparison Results ‣ IV Results and Discussion ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting")).

![Refer to caption](2603.06733v1/p2_fig_reliability.png)


Figure 3: Reliability diagram (calibration curve). CCI is closer to the diagonal, indicating better calibration (lower ECE/Brier).

![Refer to caption](2603.06733v1/p2_fig_week_trend_aucpr.png)


Figure 4: AUC-PR trend across evaluation weeks (distribution shift). CCI shows a smaller decline over time.

![Refer to caption](2603.06733v1/p2_fig_fairness_tradeoff.png)


Figure 5: Fairness–accuracy trade-off (Demographic parity gap vs. AUC-PR). CCI provides a strong balance between the two.

Overall, CCI enhances discrimination and operational recall while producing more accurate probabilities and narrower fairness gaps under time-based evaluation. The stability analysis reveals that performance degradation occurs less frequently in later weeks, which supports the primary objective of robust credit risk scoring under distribution shifts.

## V Conclusion

### V-A Conclusion

This paper presented CCI, a calibrated credit risk scoring framework designed for real-world settings where data distribution changes over time and fairness and reliability are required. The method combines an uncertainty-aware Bayesian neural scorer with a fairness-constrained gradient boosting model, then fuses their outputs and applies post-hoc calibration to produce stable probability estimates. Experimental results on the Home Credit Model Stability dataset show that CCI improves discrimination and operational recall while reducing calibration error and fairness gaps under a time-consistent evaluation. Overall, CCI provides a practical credit intelligence pipeline that balances accuracy, robustness to shift, and decision trustworthiness.

### V-B Future Work

Future work will extend CCI with stronger shift-aware updating strategies (e.g., online recalibration and periodic retraining), and will evaluate additional fairness definitions that reflect credit policy requirements across multiple sensitive attributes. We also plan to study uncertainty-guided human-in-the-loop decisioning, where high-uncertainty cases are routed for manual review, and to validate the framework on more credit and lending datasets to confirm generalization across institutions and economic conditions.

## References

* [1]
  A. Alonso Robisco and J. M. Carbó Martínez (2022)
  Measuring the model risk-adjusted performance of machine learning algorithms in credit default prediction.
  Financial Innovation 8 (1),  pp. 70.
  Cited by: [§I](#S1.p1.1 "I Introduction ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting").
* [2]
  E. Dumitrescu, S. Hué, C. Hurlin, and S. Tokpavi (2022)
  Machine learning for credit scoring: improving logistic regression with non-linear decision-tree effects.
  European Journal of Operational Research 297 (3),  pp. 1178–1192.
  Cited by: [§II](#S2.p1.1 "II Related Work ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting"),
  [TABLE I](#S4.T1.16.10.6 "In IV-B Main Comparison Results ‣ IV Results and Discussion ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting").
* [3]
  B. Enkhsaikhan and O. Jo (2024)
  Uncertainty-aware reinforcement learning for portfolio optimization.
  IEEE Access.
  Cited by: [§I](#S1.p1.1 "I Introduction ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting").
* [4]
  Y. Guo, Y. Zhai, and S. Jiang (2025)
  Investment decision making for large-scale peer-to-peer lending data: a bayesian neural network approach.
  International Review of Financial Analysis 102,  pp. 104100.
  Cited by: [§II](#S2.p1.1 "II Related Work ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting"),
  [TABLE I](#S4.T1.41.35.6 "In IV-B Main Comparison Results ‣ IV Results and Discussion ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting").
* [5]
  Kaggle and Home Credit (2024)
  Home credit - credit risk model stability.
  Note: Kaggle Competition DatasetAccessed: 2025-12-23
  External Links: [Link](https://www.kaggle.com/competitions/home-credit-credit-risk-model-stability)
  Cited by: [§III-A](#S3.SS1.p1.1 "III-A Dataset ‣ III Methodology ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting").
* [6]
  P. Kündig and F. Sigrist (2025)
  A spatio-temporal machine learning model for mortgage credit risk: default probabilities and loan portfolios.
  European Journal of Operational Research.
  Cited by: [§II](#S2.p1.1 "II Related Work ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting").
* [7]
  J. Liu, S. Zhang, and H. Fan (2022)
  A two-stage hybrid credit risk prediction model based on xgboost and graph-based deep neural network.
  Expert Systems with Applications 195,  pp. 116624.
  Cited by: [§II](#S2.p1.1 "II Related Work ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting"),
  [TABLE I](#S4.T1.21.15.6 "In IV-B Main Comparison Results ‣ IV Results and Discussion ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting").
* [8]
  H. Lu and X. Hu (2024)
  Enhancing financial risk prediction for listed companies: a catboost-based ensemble learning approach.
  Journal of the Knowledge Economy 15 (2),  pp. 9824–9840.
  Cited by: [§II](#S2.p1.1 "II Related Work ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting"),
  [TABLE I](#S4.T1.31.25.6 "In IV-B Main Comparison Results ‣ IV Results and Discussion ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting").
* [9]
  D. Moldovan (2023)
  Algorithmic decision making methods for fair credit scoring.
  IEEE Access 11,  pp. 59729–59743.
  Cited by: [§I](#S1.p1.1 "I Introduction ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting").
* [10]
  M. Sensoy, M. Saleki, S. Julier, R. Aydogan, and J. Reid (2021)
  Misclassification risk and uncertainty quantification in deep classifiers.
  In Proceedings of the IEEE/CVF winter conference on applications of computer vision,
   pp. 2484–2492.
  Cited by: [§I](#S1.p1.1 "I Introduction ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting").
* [11]
  H. Suryanto, A. Mahidadia, M. Bain, C. Guan, and A. Guan (2022)
  Credit risk modeling using transfer learning and domain adaptation.
  Frontiers in Artificial Intelligence 5,  pp. 868232.
  Cited by: [§II](#S2.p1.1 "II Related Work ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting").
* [12]
  B. Xu, Y. Wang, T. Line, C. Shu, and S. Tang
  Toward fairness-aware gradient boosting decision trees for ranking.
  Available at SSRN 4752973.
  Cited by: [§II](#S2.p1.1 "II Related Work ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting"),
  [TABLE I](#S4.T1.46.40.6 "In IV-B Main Comparison Results ‣ IV Results and Discussion ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting"),
  [TABLE II](#S4.T2.3.5.2.1 "In IV-C Stability Under Distribution Shift ‣ IV Results and Discussion ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting").
* [13]
  C. Ying, A. Shi, and X. Li (2025)
  Hybrid boosted attention-based lightgbm framework for enhanced credit risk assessment in digital finance.
  Humanities and Social Sciences Communications 12 (1),  pp. 1–13.
  Cited by: [§II](#S2.p1.1 "II Related Work ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting"),
  [TABLE I](#S4.T1.26.20.6 "In IV-B Main Comparison Results ‣ IV Results and Discussion ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting"),
  [TABLE II](#S4.T2.3.4.1.1 "In IV-C Stability Under Distribution Shift ‣ IV Results and Discussion ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting").
* [14]
  C. Yu, Y. Jin, Q. Xing, Y. Zhang, S. Guo, and S. Meng (2024)
  Advanced user credit risk prediction model using lightgbm, xgboost and tabnet with smoteenn.
  In 2024 IEEE 6th International Conference on Power, Intelligent Computing and Systems (ICPICS),
   pp. 876–883.
  Cited by: [§II](#S2.p1.1 "II Related Work ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting"),
  [TABLE I](#S4.T1.36.30.6 "In IV-B Main Comparison Results ‣ IV Results and Discussion ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting").
* [15]
  L. Zhou, H. Fujita, H. Ding, and R. Ma (2021)
  Credit risk modeling on data with two timestamps in peer-to-peer lending by gradient boosting.
  Applied Soft Computing 110,  pp. 107672.
  Cited by: [§I](#S1.p1.1 "I Introduction ‣ Calibrated Credit Intelligence: Shift-Robust and Fair Risk Scoring with Bayesian Uncertainty and Gradient Boosting").

BETA