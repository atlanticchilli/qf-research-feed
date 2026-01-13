---
authors:
- O. Didkovskyi
- A. Vidali
- N. Jean
- G. Le Pera
doc_id: arxiv:2601.07588v1
family_id: arxiv:2601.07588
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Temporal-Aligned Meta-Learning for Risk Management: A Stacking Approach for
  Multi-Source Credit Scoring'
url_abs: http://arxiv.org/abs/2601.07588v1
url_html: https://arxiv.org/html/2601.07588v1
venue: arXiv q-fin
version: 1
year: 2026
---


O. Didkovskyi A. Vidali11footnotemark: 1, N. Jean, and G. Le Pera
Equal contributioncorresponding author: nicola.jean@illimity.com

###### Abstract

This paper presents a meta-learning framework for credit risk assessment of Italian Small and Medium Enterprises (SMEs) that explicitly addresses the temporal misalignment of credit scoring models.
The approach aligns financial statement reference dates with evaluation dates, mitigating bias arising from publication delays and asynchronous data sources.
It is based on a two-step temporal decomposition that at first estimates annual probabilities of default (PDs) anchored to balance-sheet reference dates (December 31st) through a static model. Then it models the monthly evolution of PDs using higher-frequency behavioral data.
Finally, we employ stacking-based architecture to aggregate multiple scoring systems, each capturing complementary aspects of default risk, into a unified predictive model.
In this way, first level model outputs are treated as learned representations that encode non-linear relationships in financial and behavioral indicators, allowing integration of new expert-based features without retraining base models.

This design provides a coherent and interpretable solution to challenges typical of low-default environments, including heterogeneous default definitions and reporting delays.
Empirical validation shows that the framework effectively captures credit risk evolution over time, improving temporal consistency and predictive stability relative to standard ensemble methods.

JEL Classification codes: C45, C55, G24
AMS Classification codes: 91G40

Keywords: Credit Risk, Rating Model, Corporate Scoring, Stacking, Artificial Intelligence, Machine Learning, XAI.

## 1 Introduction

Credit risk assessment remains a core challenge for financial institutions, requiring the synthesis of multiple information sources that describe different facets of a borrower’s financial health [[11](https://arxiv.org/html/2601.07588v1#bib.bib7 "Quantitative risk management: concepts, techniques and tools")].
Modern credit scoring must capture non-linear relationships between indicators [[1](https://arxiv.org/html/2601.07588v1#bib.bib27 "Credit risk analysis using machine and deep learning models"), [8](https://arxiv.org/html/2601.07588v1#bib.bib33 "Consumer credit-risk models via machine-learning algorithms"), [2](https://arxiv.org/html/2601.07588v1#bib.bib72 "Mercati, infrastrutture e sistemi di pagamento: approfondimenti n. 73")], integrate heterogeneous data (financial statements, bureau records, expert indicators, macro variables),
and respect the temporal characteristics and reporting delays inherent to each source.

A specific but widespread operational problem is the temporal misalignment:
data used for scoring are often referenced to different dates than the evaluation (application or monitoring) date.
For example, annual balance sheets dated December 31 may only become available six months later; therefore, a model trained to predict default within one year of the balance-sheet date is, at evaluation time, predicting over a horizon that has already been partially observed.
This mismatch systematically biases risk estimates and is particularly consequential for Small and Medium Enterprises (SMEs), where information asymmetry and sparse reporting amplify sensitivity to stale data [[6](https://arxiv.org/html/2601.07588v1#bib.bib36 "Forecasting bankruptcy for smes using hazard function: to what extent does size matter?")].
Existing multi-source fusion and temporal models handle feature fusion but typically assume aligned reference points and thus do not directly address this reference-to-evaluation date gap [[3](https://arxiv.org/html/2601.07588v1#bib.bib69 "Credit risk prediction for smes based on multi-view learning with hierarchical attention mechanism"), [13](https://arxiv.org/html/2601.07588v1#bib.bib70 "Credit risk assessment using the factorization machine model with feature interactions"), [15](https://arxiv.org/html/2601.07588v1#bib.bib65 "A deep learning approach for credit scoring of peer-to-peer lending using attention mechanism LSTM"), [9](https://arxiv.org/html/2601.07588v1#bib.bib63 "Temporal fusion transformers for interpretable multi-horizon time series forecasting")].

We approach this problem by combining two complementary base models that capture different risk perspectives:

* •

  CRD Model [[12](https://arxiv.org/html/2601.07588v1#bib.bib30 "Machine learning approach for credit scoring")]: Leverages balance sheet data, providing comprehensive financial indicators but updated annually with 3-9 month publication lags.
* •

  Behavioral Model (BHV) [[4](https://arxiv.org/html/2601.07588v1#bib.bib59 "Cross-domain behavioral credit modeling: transferability from private to central data")]: Utilizes Central Credit Register data, capturing borrower payment patterns and credit utilization with monthly updates but lacking the granularity of accounting statements.

These models display complementary asymmetries: CRD is deep but stale; BHV is timely but incomplete, yet neither alone resolves the temporal alignment problem.

Thus we propose a two-step framework that explicitly models the temporal gap between data reference dates and evaluation dates.
First, a static model is created to estimate annual PD anchored to December 31st using balance sheet data.
After, a dynamic model is trained on outputs of the static model to captures monthly PD evolution by integrating behavioral updates through temporal aggregation and meta-learning.
This approach yields PIT-consistent scores for both origination and monitoring and avoids full retraining when adding new indicators.

Our main contributions are:

1. 1.

   A temporal decomposition that separates static annual assessment from dynamic monthly evolution and explicitly tackles temporal misalignment between data sources.
2. 2.

   A point-in-time consistency methodology for aligning multi-frequency sources to common reference dates, producing PIT-adjusted PD estimates.
3. 3.

   A modular meta-learning architecture that integrates base-model embeddings and allows new indicators to be added without revalidating underlying models.

The remainder of the paper is organized as follows. Section 2 describes the dataset and data-availability constraints. Section 3 defines targets and preprocessing. Section 4 details the modeling framework, including the static anchor model, dynamic update mechanism, and the meta-learner. Section 5 presents empirical results and validation metrics. Section 6 discusses limitations, operational considerations, and future work.

## 2 Dataset

Our analysis utilizes multiple data sources covering Italian SMEs, with the focus to the companies within the illimity bank’s portfolio, including both direct debtors and participants in joint ventures.
These sources are (i) Balance sheet data of the illimity debtors, (ii) Central Credit Register Data (CR) [[14](https://arxiv.org/html/2601.07588v1#bib.bib52 "Circular no. 139. central credit register")],
(iii) Expert-Based Indicators that may be created from both internal and external data.
CR data represents the bottleneck in our framework as it is only available for companies within the internal portfolio.

Table 1: Dataset Overview

| Data Source | Period | Update Frequency | Sample Size | Lag |
| --- | --- | --- | --- | --- |
| Balance Sheets | 2017-2023 | Annual | 18,454 | 3-9 months |
| Central Credit Register | 2017-2024 | Monthly | 18,454 | 2 months |
| Expert Indicators | 2017-2024 | Variable | 18,454 | 2 months |

### 2.1 On data processing

A fundamental challenge arises from the time required to process information by external agencies.
Balance sheets for December 31st become available 3-9 months later;
CR data has a 2-month lag; internal data provides near real-time updates.
Figure [1](https://arxiv.org/html/2601.07588v1#S2.F1 "Figure 1 ‣ 2.1 On data processing ‣ 2 Dataset ‣ Temporal-Aligned Meta-Learning for Risk Management: A Stacking Approach for Multi-Source Credit Scoring") illustrates how this creates systematic temporal misalignment where the CRD model’s 12-month prediction horizon extends beyond target period.

![Refer to caption](images/temporal_misalignment_example.png)


Figure 1: Temporal misalignment: December 31st balance sheets published 6 months later create a prediction gap with the 12-month horizon

### 2.2 Point-in-Time Consistency

To address temporal misalignment we introduce point-in-time consistency:
identifying the latest information related to the reference period being modeled.
It ensures that the predictions are based on data that characterize the situation at the decision point.

Given that balance sheets represent the situation as of December 31st, the proposed consistency describes an ideal scenario wherein for each December 31st,
the model estimates probability of default for the next year using CR data aligned with this date.

### 2.3 Features

The meta-learner’s base features are standardized logit-transformed PDs from established models:

* •

  l​o​g​i​t​(P​Db​h​v)∗logit(PD\_{bhv})^{\*} - standardized behavioral score
* •

  l​o​g​i​t​(P​Dc​r​d)∗logit(PD\_{crd})^{\*} - standardized CRD score

where the logit transformation and standardization is applied to ensure consistent scaling across different probability ranges.

For dynamic model we adopt exponentially weighted moving average of P​Db​h​vPD\_{bhv} to account for dynamics of monthly behavioral PDs.
The parameter α\alpha is calibrated on internal data.

## 3 Target

We indicate default event as one of the following indicators: default rettificato (Bank of Italy system-level definition), Orbis bankruptcy target, and the internal default flag.
Then manual validation corrects classification inconsistencies: companies in bankruptcy or liquidation proceedings confirmed through manual inspection are added as defaults, while false positives are removed

### 3.1 Static Model Target

The static target identifies at least one month within the next 12 months where the default occurs, starting from December 31st (balance sheet reference dates).

### 3.2 Dynamic Model Target

The dynamic target is the interpolated static prediction between consecutive December 31st anchor points.
Static model predictions are interpolated exponentially with parameter within the score space.
Exponential interpolation (rather than linear) reflects credit risk dynamics where deterioration typically accelerates as companies approach distress.
Figure [2](https://arxiv.org/html/2601.07588v1#S3.F2 "Figure 2 ‣ 3.2 Dynamic Model Target ‣ 3 Target ‣ Temporal-Aligned Meta-Learning for Risk Management: A Stacking Approach for Multi-Source Credit Scoring") demonstrates the effect of different k values on the interpolation curve between anchor points.
Positive k values create convex curves with gradual initial transitions and accelerating changes near the next anchor, while negative values produce the opposite pattern.

![Refer to caption](images/k_interpolation_plot.png)


Figure 2: Exponential interpolation with k=3 selected through backtesting

## 4 Modeling

We employ logistic regression as the meta-learner, treating base-model PD outputs as learned representations encoding distinct temporal views of risk.
This modular abstraction preserves interpretability while enabling temporal alignment and integration of new indicators without retraining base models.

### 4.1 Static Model Architecture

Logistic regression trained on December 31st-aligned data combines standardized logit-transformed probabilities with turnover class indicators:

|  |  |  |
| --- | --- | --- |
|  | l​o​g​i​t​(p)=β0+β1⋅l​o​g​i​t​(P​Db​h​v)∗+β2⋅l​o​g​i​t​(P​Dc​r​d)∗+∑k∈{micro, small, medium}γk⋅It​u​r​n​o​v​e​r,klogit(p)=\beta\_{0}+\beta\_{1}\cdot logit(PD\_{bhv})^{\*}+\beta\_{2}\cdot logit(PD\_{crd})^{\*}+\sum\_{k\in\{\text{micro, small, medium}\}}\gamma\_{k}\cdot I\_{turnover,k} |  |

where pp is the predicted 12-month default probability, and large company size serves as the reference level.

Table [2](https://arxiv.org/html/2601.07588v1#S4.T2 "Table 2 ‣ 4.1 Static Model Architecture ‣ 4 Modeling ‣ Temporal-Aligned Meta-Learning for Risk Management: A Stacking Approach for Multi-Source Credit Scoring") reports the estimated coefficients.

Table 2: Static Model Logistic Regression Coefficients

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Variable | Coefficient | Std. Error | z-value | P-value |
| Intercept | −5.1478-5.1478 | 0.133 | -38.73 | 0.000 |
| l​o​g​i​t​(P​Dc​r​d)∗logit(PD\_{crd})^{\*} (crd\_pd) | 0.9770 | 0.042 | 23.28 | 0.000 |
| l​o​g​i​t​(P​Db​h​v)∗logit(PD\_{bhv})^{\*} (bhv\_pd) | 0.5839 | 0.029 | 19.95 | 0.000 |
| C(crd\_size)[medium] | 0.3173 | 0.167 | 1.90 | 0.057 |
| C(crd\_size)[micro] | 1.1503 | 0.159 | 7.22 | 0.000 |
| C(crd\_size)[small] | 0.5730 | 0.156 | 3.66 | 0.000 |
| Model Statistics: McFadden R2R^{2} = 0.338, Nagelkerke R2R^{2} = 0.366, KS = 0.652 | | | | |
| --- | --- | --- | --- | --- |

### 4.2 Dynamic Model Architecture

Figure [3](https://arxiv.org/html/2601.07588v1#S4.F3 "Figure 3 ‣ 4.2 Dynamic Model Architecture ‣ 4 Modeling ‣ Temporal-Aligned Meta-Learning for Risk Management: A Stacking Approach for Multi-Source Credit Scoring") illustrates the temporal alignment concept underlying the dynamic model, showing how CRD model outputs (anchored at December 31st) and behavioral scores are integrated at the evaluation point to produce the fusion prediction.

![Refer to caption](images/fusion_prediction_example.png)


Figure 3: Fusion architecture combining static balance sheet assessment with dynamic behavioral updates at evaluation point

The dynamic model uses EWMA behavioral scores with the same equation structure as the statics model.

|  |  |  |
| --- | --- | --- |
|  | l​o​g​i​t​(p^t+k)=β0+β1⋅l​o​g​i​t​(P​Db​h​v)k∗+β2⋅l​o​g​i​t​(P​Dc​r​d)∗+∑s∈{micro, small, medium}γs⋅It​u​r​n​o​v​e​r,slogit(\hat{p}\_{t+k})=\beta\_{0}+\beta\_{1}\cdot logit(PD\_{bhv})\_{k}^{\*}+\beta\_{2}\cdot logit(PD\_{crd})^{\*}+\sum\_{s\in\{\text{micro, small, medium}\}}\gamma\_{s}\cdot I\_{turnover,s} |  |

Table [3](https://arxiv.org/html/2601.07588v1#S4.T3 "Table 3 ‣ 4.2 Dynamic Model Architecture ‣ 4 Modeling ‣ Temporal-Aligned Meta-Learning for Risk Management: A Stacking Approach for Multi-Source Credit Scoring") presents coefficients (R2=0.952R^{2}=0.952, 149,353 observations).

Table 3: Dynamic Model OLS Regression Coefficients

| Variable | Coefficient | Std. Error | t-value | P-value |
| --- | --- | --- | --- | --- |
| Intercept | −4.9864-4.9864 | 0.002 | -2962.3 | 0.000 |
| l​o​g​i​t​(P​Dc​r​d)∗logit(PD\_{crd})^{\*} (crd\_pd) | 0.9960 | 0.001 | 933.2 | 0.000 |
| l​o​g​i​t​(P​Db​h​v)∗logit(PD\_{bhv})^{\*} (bhv\_pd\_ewma) | 0.7913 | 0.001 | 743.5 | 0.000 |
| C(crd\_size)[medium] | 0.2992 | 0.003 | 118.9 | 0.000 |
| C(crd\_size)[micro] | 1.1362 | 0.003 | 374.2 | 0.000 |
| C(crd\_size)[small] | 0.5612 | 0.003 | 221.9 | 0.000 |

### 4.3 Rating Assignment and Meta-Learning Integration

The goal of the enriched system is to provide rating classes comparable to established credit rating systems.
Therefore, we map continuous PD predictions to categorical ratings using the CRD rating scale.
To ensure proper calibration across company size segments, we apply size-specific delta shifts that adjust the predicted PDs before rating assignment.
These delta shifts account for systematic differences in default behavior and data quality across size categories.

Table 4: Delta Shift Values by Company Size

| Size Category | Delta Shift |
| --- | --- |
| Micro | -2.004 |
| Small | -1.251 |
| Medium | -0.688 |
| Large | +0.178 |

### 4.4 Validation Strategies

To ensure the model’s applicability across the entire banking unit and its robustness under different scenarios, we employ multiple validation perspectives.
We cover temporal, cross-sectional, and bootstrap dimensions.
Each validation strategy addresses specific aspects of model performance and generalization

## 5 Results

Table [5](https://arxiv.org/html/2601.07588v1#S5.T5 "Table 5 ‣ 5 Results ‣ Temporal-Aligned Meta-Learning for Risk Management: A Stacking Approach for Multi-Source Credit Scoring") demonstrates clear performance gains from temporal alignment. The Static Fusion model achieves AUC=0.900, outperforming CRD (0.833) and BHV (0.808) baselines.

Table 5: Static Model Performance Metrics

| Model | AUC | F-measure | Recall | Specificity |
| --- | --- | --- | --- | --- |
| Fusion Static | 0.900 | 0.821 | 0.820 | 0.822 |
| Behavioral (baseline) | 0.808 | 0.721 | 0.662 | 0.818 |
| CRD (baseline) | 0.833 | 0.689 | 0.591 | 0.882 |

The model demonstrates robust performance across different company size segments, with particularly strong results for medium and large enterprises as shown in Table [6](https://arxiv.org/html/2601.07588v1#S5.T6 "Table 6 ‣ 5 Results ‣ Temporal-Aligned Meta-Learning for Risk Management: A Stacking Approach for Multi-Source Credit Scoring").

Table 6: Performance Metrics by Company Size

| Size | Count | Default Rate | AUC | Avg. Precision | F-measure | Recall | Specificity |
| --- | --- | --- | --- | --- | --- | --- | --- |
| micro | 2,275 | 0.0615 | 0.882 | 0.421 | 0.741 | 0.907 | 0.597 |
| small | 4,781 | 0.0316 | 0.882 | 0.439 | 0.782 | 0.801 | 0.758 |
| medium | 4,894 | 0.0206 | 0.903 | 0.428 | 0.829 | 0.802 | 0.867 |
| large | 6,504 | 0.0134 | 0.871 | 0.242 | 0.801 | 0.736 | 0.908 |

The dynamic model maintains strong performance across temporal horizons (Table [7](https://arxiv.org/html/2601.07588v1#S5.T7 "Table 7 ‣ 5 Results ‣ Temporal-Aligned Meta-Learning for Risk Management: A Stacking Approach for Multi-Source Credit Scoring")), with QWK ranging from 0.772 (6-month ahead) to 0.951 (12-month ahead).

Table 7: Dynamic Model Performance Across Time Horizons

| Time Horizon | Quadratic Weighted Kappa |
| --- | --- |
| 1-month ahead | 0.910 |
| 3-month ahead | 0.849 |
| 6-month ahead | 0.772 |
| 12-month ahead | 0.951 |

Figure [4](https://arxiv.org/html/2601.07588v1#S5.F4 "Figure 4 ‣ 5 Results ‣ Temporal-Aligned Meta-Learning for Risk Management: A Stacking Approach for Multi-Source Credit Scoring") illustrates fusion rating integration across all company sizes.

![Refer to caption](images/fusion_ratings_frontier_by_size.png)


Figure 4: Fusion rating frontier by company size

## 6 Discussion

#### Limitations

The dynamic model assumes smooth risk evolution between balance sheet assessments.
While sudden economic shocks may violate this assumption,
high-frequency behavioral data through EWMA captures rapid quality changes.
Balance sheet annual updates create a practical constraint: between publications (potentially 18 months),
only behavioral components drive prediction changes.
The adjusted default definition may not perfectly capture institution-specific defaults,
particularly for complex multi-bank relationships.

#### Choice of Meta-Learner

We selected logistic regression over Random Forest [[5](https://arxiv.org/html/2601.07588v1#bib.bib19 "Stochastic gradient boosting")] after several experiments showed no significant AUC or log-loss improvements. The simpler approach preserves modularity and interpretability, aligning with our temporal decomposition contribution.

#### Generalizability

While developed for Italian SMEs, the framework applies broadly to markets with heterogeneous data sources and publication delays.
Parameters (α\alpha, k, delta shifts) are market-specific, but the static-dynamic architectural decomposition generalizes.
Markets with complete data availability (e.g., US) may benefit less; emerging markets could see larger improvements.

#### Implications for Credit Risk Practice

Our framework challenges the conventional wisdom that more frequent model updates necessarily improve risk assessment.
By explicitly modeling temporal dynamics rather than repeatedly retraining on misaligned data, we achieve superior performance with lower operational complexity.

#### Explainability

The framework provides interpretability through meta-model coefficients (component importance), delta shifts (size-based attribution), and marginal effects.
SHAP analysis [[10](https://arxiv.org/html/2601.07588v1#bib.bib11 "A unified approach to interpreting model predictions")] in hierarchical stacking requires careful decomposition; we rely primarily on coefficient interpretation and marginal effects [[7](https://arxiv.org/html/2601.07588v1#bib.bib58 "Bridging human cognition and ai: a framework for explainable decision-making systems")].

## 7 Conclusion

This paper demonstrates that temporal misalignment in credit data sources is a fundamental challenge requiring architectural innovation.
By decomposing risk assessment into static anchoring and dynamic evolution, we transform the liability of asynchronous data into an asset—leveraging each source’s temporal characteristics.
Obtained evidences validate this approach: explicit temporal modeling yields both statistical improvements and operational advantages in both credit origination and portfolio monitoring.

The three key innovations—temporal decomposition, point-in-time consistency, and modular meta-learning—collectively address a gap that existing multi-view and temporal architectures have overlooked: the operational reality of asynchronous data availability.

## Acknowledgements

We would like to thank Claudio Nordio, Risk Officer, for supporting this work and research. We are also grateful to Lorenzo Giada for assessing our approach and providing valuable suggestions that improved this paper.

## References

* [1]
  P. M. Addo, D. Guegan, and B. Hassani (2018)
  Credit risk analysis using machine and deep learning models.
  Risks 6 (2),  pp. 38.
  Cited by: [§1](https://arxiv.org/html/2601.07588v1#S1.p1.1 "1 Introduction ‣ Temporal-Aligned Meta-Learning for Risk Management: A Stacking Approach for Multi-Source Credit Scoring").
* [2]
  Banca d’Italia (2026)
  Mercati, infrastrutture e sistemi di pagamento: approfondimenti n. 73.
  Technical report
  Technical Report 73, Mercati, infrastrutture e sistemi di pagamento – Approfondimenti, Banca d’Italia.
  Note: Accessed: 2026-01-11
  External Links: [Link](https://www.bancaditalia.it/pubblicazioni/mercati-infrastrutture-e-sistemi-di-pagamento/approfondimenti/2026-073/N.73-MISP.pdf)
  Cited by: [§1](https://arxiv.org/html/2601.07588v1#S1.p1.1 "1 Introduction ‣ Temporal-Aligned Meta-Learning for Risk Management: A Stacking Approach for Multi-Source Credit Scoring").
* [3]
  Z. Chen, H. Chen, Q. Tong, Y. Liu, and X. Zhu (2025)
  Credit risk prediction for smes based on multi-view learning with hierarchical attention mechanism.
  Annals of Operations Research,  pp. 1–32.
  Cited by: [§1](https://arxiv.org/html/2601.07588v1#S1.p2.1 "1 Introduction ‣ Temporal-Aligned Meta-Learning for Risk Management: A Stacking Approach for Multi-Source Credit Scoring").
* [4]
  O. Didkovskyi, N. Jean, G. Le Pera, and C. Nordio (2024)
  Cross-domain behavioral credit modeling: transferability from private to central data.
  Available at SSRN 4698905.
  Cited by: [2nd item](https://arxiv.org/html/2601.07588v1#S1.I1.i2.p1.1 "In 1 Introduction ‣ Temporal-Aligned Meta-Learning for Risk Management: A Stacking Approach for Multi-Source Credit Scoring").
* [5]
  J. H. Friedman (2002)
  Stochastic gradient boosting.
  Computational statistics & data analysis 38 (4),  pp. 367–378.
  Cited by: [§6](https://arxiv.org/html/2601.07588v1#S6.SS0.SSS0.Px2.p1.1 "Choice of Meta-Learner ‣ 6 Discussion ‣ Temporal-Aligned Meta-Learning for Risk Management: A Stacking Approach for Multi-Source Credit Scoring").
* [6]
  J. Gupta, A. Gregoriou, and J. Healy (2015)
  Forecasting bankruptcy for smes using hazard function: to what extent does size matter?.
  Review of Quantitative Finance and Accounting 45,  pp. 845–869.
  Cited by: [§1](https://arxiv.org/html/2601.07588v1#S1.p2.1 "1 Introduction ‣ Temporal-Aligned Meta-Learning for Risk Management: A Stacking Approach for Multi-Source Credit Scoring").
* [7]
  N. Jean and G. L. Pera (2025)
  Bridging human cognition and ai: a framework for explainable decision-making systems.
  arXiv preprint arXiv:2509.02388.
  Cited by: [§6](https://arxiv.org/html/2601.07588v1#S6.SS0.SSS0.Px5.p1.1 "Explainability ‣ 6 Discussion ‣ Temporal-Aligned Meta-Learning for Risk Management: A Stacking Approach for Multi-Source Credit Scoring").
* [8]
  A. E. Khandani, A. J. Kim, and A. W. Lo (2010)
  Consumer credit-risk models via machine-learning algorithms.
  Journal of Banking & Finance 34 (11),  pp. 2767–2787.
  Cited by: [§1](https://arxiv.org/html/2601.07588v1#S1.p1.1 "1 Introduction ‣ Temporal-Aligned Meta-Learning for Risk Management: A Stacking Approach for Multi-Source Credit Scoring").
* [9]
  B. Lim, S. Ö. Arık, N. Loeff, and T. Pfister (2021)
  Temporal fusion transformers for interpretable multi-horizon time series forecasting.
  International Journal of Forecasting 37 (4),  pp. 1748–1764.
  External Links: [Document](https://dx.doi.org/10.1016/j.ijforecast.2021.03.012)
  Cited by: [§1](https://arxiv.org/html/2601.07588v1#S1.p2.1 "1 Introduction ‣ Temporal-Aligned Meta-Learning for Risk Management: A Stacking Approach for Multi-Source Credit Scoring").
* [10]
  S. M. Lundberg and S. Lee (2017)
  A unified approach to interpreting model predictions.
  In Advances in neural information processing systems,
   pp. 4765–4774.
  Cited by: [§6](https://arxiv.org/html/2601.07588v1#S6.SS0.SSS0.Px5.p1.1 "Explainability ‣ 6 Discussion ‣ Temporal-Aligned Meta-Learning for Risk Management: A Stacking Approach for Multi-Source Credit Scoring").
* [11]
  A. J. McNeil, R. Frey, P. Embrechts, et al. (2005)
  Quantitative risk management: concepts, techniques and tools.
  Vol. 3, Princeton university press Princeton.
  Cited by: [§1](https://arxiv.org/html/2601.07588v1#S1.p1.1 "1 Introduction ‣ Temporal-Aligned Meta-Learning for Risk Management: A Stacking Approach for Multi-Source Credit Scoring").
* [12]
  A. R. Provenzano, D. Trifirò, A. Datteo, L. Giada, N. Jean, A. Riciputi, G. L. Pera, M. Spadaccino, L. Massaron, and C. Nordio (2020)
  Machine learning approach for credit scoring.
  arXiv preprint arXiv:2008.01687.
  Cited by: [1st item](https://arxiv.org/html/2601.07588v1#S1.I1.i1.p1.1 "In 1 Introduction ‣ Temporal-Aligned Meta-Learning for Risk Management: A Stacking Approach for Multi-Source Credit Scoring").
* [13]
  J. Quan and X. Sun (2024)
  Credit risk assessment using the factorization machine model with feature interactions.
  Humanities and Social Sciences Communications 11 (1),  pp. 1–10.
  Cited by: [§1](https://arxiv.org/html/2601.07588v1#S1.p2.1 "1 Introduction ‣ Temporal-Aligned Meta-Learning for Risk Management: A Stacking Approach for Multi-Source Credit Scoring").
* [14]
  The Bank of Italy (1991)
  Circular no. 139. central credit register.
  External Links: [Link](https://www.bancaditalia.it/compiti/vigilanza/normativa/archivio-norme/circolari/c139/)
  Cited by: [§2](https://arxiv.org/html/2601.07588v1#S2.p1.1 "2 Dataset ‣ Temporal-Aligned Meta-Learning for Risk Management: A Stacking Approach for Multi-Source Credit Scoring").
* [15]
  C. Wang, D. Han, Q. Liu, and S. Luo (2019)
  A deep learning approach for credit scoring of peer-to-peer lending using attention mechanism LSTM.
  IEEE Access 7,  pp. 2161–2168.
  External Links: [Document](https://dx.doi.org/10.1109/ACCESS.2018.2887138)
  Cited by: [§1](https://arxiv.org/html/2601.07588v1#S1.p2.1 "1 Introduction ‣ Temporal-Aligned Meta-Learning for Risk Management: A Stacking Approach for Multi-Source Credit Scoring").