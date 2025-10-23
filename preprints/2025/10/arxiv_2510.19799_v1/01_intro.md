---
authors:
- Ji Ma
- Albert Casella
doc_id: arxiv:2510.19799v1
family_id: arxiv:2510.19799
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 1 Introduction
url_abs: http://arxiv.org/abs/2510.19799v1
url_html: https://arxiv.org/html/2510.19799v1
venue: arXiv q-fin
version: 1
year: 2025
---

\useunder

\undefine@keynewfloatplacement\undefine@keynewfloatname\undefine@keynewfloatfileext\undefine@keynewfloatwithin

Integrating Transparent Models, LLMs, and Practitioner‑in‑the‑Loop:

A Case of Nonprofit Program Evaluation

Ji MA

LBJ School of Public Affairs, The University of Texas at Austin

Gradel Institute of Charity, University of Oxford

Albert CASELLA

Michael & Susan Dell Foundation

Public and nonprofit organizations often hesitate to adopt AI tools because most models are opaque even though standard approaches typically analyze aggregate patterns rather than offering actionable, case-level guidance. This study tests a practitioner-in-the-loop workflow that pairs transparent decision-tree models with large language models (LLMs) to improve predictive accuracy, interpretability, and the generation of practical insights. Using data from an ongoing college-success program, we build interpretable decision trees to surface key predictors. We then provide each tree’s structure to an LLM, enabling it to reproduce case-level predictions grounded in the transparent models. Practitioners participate throughout feature engineering, model design, explanation review, and usability assessment, ensuring that field expertise informs the analysis at every stage. Results show that integrating transparent models, LLMs, and practitioner input yields accurate, trustworthy, and actionable case-level evaluations, offering a viable pathway for responsible AI adoption in the public and nonprofit sectors. *(145 words)*

Keywords: program evaluation; practitioner‑in‑the‑loop; decision tree; large language model; case-level prediction; responsible AI

 

*Correspondence*: JM, [maji@austin.utexas.edu](mailto:maji@austin.utexas.edu); AC, [albert.casella@dell.org](mailto:albert.casella@dell.org). *Funding*: The project is partly supported by (1) Michael & Susan Dell Foundation, (2) Academic Development Funds from the RGK Center, and computing resources through (3) the Texas Advanced Computing Center at UT Austin [[34](https://arxiv.org/html/2510.19799v1#biba.bibx11)] and (4) Dell Technologies (Client Memory Team and AI Initiative PoC Lead Engineer Wente Xiong). *Compliance with Ethical Standards*: The author declares that this study complies with required ethical standards. *Conflict of Interest*: The author declares no known conflict of interest.

## 1 Introduction

Predicting and monitoring project outcomes at the individual case level is critical for effective management, targeted interventions, and robust evaluation in the public and nonprofit sectors [[29](https://arxiv.org/html/2510.19799v1#biba.bibx6)]. Case-level analyses enable organizations to identify specific cases needing attention, allocate resources efficiently, and intervene promptly to prevent negative outcomes. However, traditional social scientists’ approaches to project evaluation have often focused on explanatory modeling at an aggregate level, seeking to understand underlying mechanisms rather than on predicting individual outcomes [[32](https://arxiv.org/html/2510.19799v1#biba.bibx9)]. This focus is valuable for building theories and informing program strategy, but often overlooks case-specific nuances and actionable insights for practitioners. Scholars and practitioners both often struggle to translate findings from explanatory models into specific, practical strategies for case management at the individual level.

Recently, scholars have shown increased interest in integrating explanatory and predictive modeling approaches to address these limitations. Machine learning (ML) and artificial intelligence (AI) methods have begun to permeate the nonprofit sector, enhancing predictive accuracy and providing actionable insights. For instance, [[46](https://arxiv.org/html/2510.19799v1#biba.bibx23)] employed random forest and gradient boosting algorithms to predict various performance dimensions (e.g., financial stability, service quality) of Canadian nonprofit sport organizations, revealing complex non-linear relationships and improving explanatory power beyond traditional linear regression. Similarly, [[31](https://arxiv.org/html/2510.19799v1#biba.bibx8)] applied random forest models to identify peer donors most likely to transition into organizational donors, achieving high predictive accuracy and informing targeted donor retention strategies.

Despite these advancements, two key challenges remain critical in order to apply academic research and advanced technologies in the nonprofit sector. (1) Models need to generate interpretable, actionable insights at the individual case level because practitioners require clear, specific guidance to effectively intervene. Without clear and actionable interpretations, predictive insights remain abstract and difficult to operationalize. (2) Predictive models need to ensure transparency because complex ML techniques often produce opaque decision-making processes despite achieving a high level of accuracy. This opacity could undermine the trust and acceptance of practitioners, particularly those who do not have many experiences with interpreting ML models. This may then limit their willingness to rely on model-driven decisions in sensitive and high-stake contexts, as has been discussed by [[40](https://arxiv.org/html/2510.19799v1#biba.bibx17)].

In response to these challenges, this study integrates transparent predictive modeling [[40](https://arxiv.org/html/2510.19799v1#biba.bibx17)] and case-level interpretation within a practitioner-in-the-loop workflow [[42](https://arxiv.org/html/2510.19799v1#biba.bibx19)], to identify students in a college scholarship program focused on who are at risk of not graduating on time (Section [2.1](https://arxiv.org/html/2510.19799v1#S2.SS1 "2.1 Data Source ‣ 2 Methods")). We first develop transparent decision-tree models to identify critical predictors and establish baseline predictive performance (Section [2.3.1](https://arxiv.org/html/2510.19799v1#S2.SS3.SSS1 "Predictive Model with Transparency: Decision Tree ‣ 2.3 Predictive and Explanatory Models ‣ 2 Methods")). We then use large language models (LLMs) to generate clear, case-specific explanations in natural language, which are directly informed by the transparent decision-tree models (Section [2.3.2](https://arxiv.org/html/2510.19799v1#S2.SS3.SSS2 "Case-Level Prediction and Interpretation: Large Language Model ‣ 2.3 Predictive and Explanatory Models ‣ 2 Methods")). Throughout the process, practitioners actively engaged in feature selection, model improvement, prompt engineering, and interpretation validation to ensure the analysis was consistently aligned with practical expertise and organizational needs (Section [2.4.2](https://arxiv.org/html/2510.19799v1#S2.SS4.SSS2 "Practitioner-in-the-Loop ‣ 2.4 Evaluation ‣ 2 Methods"); Figure [1](https://arxiv.org/html/2510.19799v1#S2.F1 "Figure 1 ‣ Practitioner-in-the-Loop ‣ 2.4 Evaluation ‣ 2 Methods")). Our results demonstrate that this integrated approach achieves strong predictive accuracy, and that augmenting LLM-generated explanations with a curated program knowledge base significantly improves their perceived safety and fairness, offering a responsible and practical model for AI adoption in the public and nonprofit sectors.

## 2 Methods

### 2.1 Data Source

The data originates from a longstanding scholarship program established in 2004 to support promising students with financial need and a determination to pursue higher education. The program systematically collects data through structured surveys administered to students each academic semester. These surveys gather data on student demographics, academic performance, financial circumstances, and personal challenges the student may be facing. Academic performance and student financial aid data are verified using university documentation. Responses are linearly aggregated into a simple risk score for each student, serving as a key predictor of whether the student is likely to need program assistance to graduate within four years of first enrollment (i.e. “on time”). Students identified as “at-risk” trigger interventions by project staff, who provide tailored support and resources to address the student’s specific needs. Currently, this system is managed by a small team case managers responsible for approximately 2,000 students. Given current staff capacity and a need to optimize program efficiency, the project requires enhanced predictive capabilities to identify at-risk students and enable more customized intervention plans.

While the dataset collected via surveys is comprehensive and accurate, it presents significant challenges for predictive modeling due to its highly imbalanced nature—approximately 75% of students in the dataset used for this study graduate within the targeted timeframe. Consequently, the primary monitoring goal of this project is to effectively identify students at risk of delayed graduation and provide personalized, case-level intervention strategies.

### 2.2 Measures

Outcome variable. The primary outcome is a binary indicator of on-time graduation, defined as completing a bachelor’s degree within four years of first enrollment. This measure aligns with the program’s core mission of supporting timely completion for its students.

Predictors. Drawing on prior studies [[37](https://arxiv.org/html/2510.19799v1#biba.bibx14), [38](https://arxiv.org/html/2510.19799v1#biba.bibx15), [33](https://arxiv.org/html/2510.19799v1#biba.bibx10), [35](https://arxiv.org/html/2510.19799v1#biba.bibx12), [41](https://arxiv.org/html/2510.19799v1#biba.bibx18)] and meetings with project case managers (Section [2.4.2](https://arxiv.org/html/2510.19799v1#S2.SS4.SSS2 "Practitioner-in-the-Loop ‣ 2.4 Evaluation ‣ 2 Methods")), we selected predictors associated with graduation outcomes in theory and in practice. These predictors fall into five thematic blocks: (1) demographic background, (2) pre-college academic profile, (3) time-varying academic progress, (4) financial circumstances, and (5) institutional context. [Table 1](https://arxiv.org/html/2510.19799v1#S2.T1 "Table 1 ‣ 2.2 Measures ‣ 2 Methods") lists every predictor, its survey label, and the expected directional relationship with on-time graduation.

Table 1: Predictors of On-Time Graduation

|  |  |  |  |
| --- | --- | --- | --- |
|  | Variable (survey label) | Data typea | Expected effectb |
| A. Demographic & Background (static) | | | |
|  | gender | Categorical | mixed |
|  | scholar\_ethnicity, scholar\_race | Categorical | mixed |
|  | citizenship | Categorical | + |
|  | has\_children | Categorical | – |
|  | numberotherdependents | Numeric | – |
| B. Pre-college Academic Profile (static) | | | |
|  | highschoolgpa\_pct | Numeric | + |
|  | readeracademicscore, readertotalscore | Numeric | + |
|  | finalacademicscore, finaltotalscore | Numeric | + |
| C. Academic Progress (panel) | | | |
|  | gpacumulativecurrent | Numeric | + |
|  | hoursattempted, hourscompleted | Numeric | + |
|  | creditstowardsdegree | Numeric | + |
|  | totalcreditsneeded | Numeric | – |
|  | enrollment (Full Time, Not Enrolled, Part Time) | Categorical | + |
|  | changed\_enrollment\_type | Categorical | – |
| D. Financial Circumstances (panel) | | | |
|  | costofattendance | Numeric | – |
|  | efcamount (Expected Family Contribution) | Numeric | + |
|  | grantaid | Numeric | + |
|  | loanamountoffered, loanamountaccepted | Numeric | mixed |
|  | totalloandebt | Numeric | – |
| E. Institutional Context (panel) | | | |
|  | collegesector (Public, Private Nonprofit, Private For-Profit) | Categorical | mixed |
|  | collegetype (2-yr, 4-yr, Mixed) | Categorical | mixed |
|  | areaofstudy (various) | Categorical | mixed |
|  | persistrateyoy\_any (Persist YOY, any enrollment) | Categorical | + |
|  | persistrateyoy\_ft2ft (Persist YOY, full-time only) | Categorical | + |

aNumerical values are converted to percentiles to reflect the position among peers.

b“+” = higher value likely increases probability of graduating on time; “–” = lowers probability; “mixed” = theoretically ambiguous or context-dependent.

### 2.3 Predictive and Explanatory Models

A distinct goal of this work was to better understand how the predictive model and interpretation can be effectively integrated into the workflow of a case manager. Thus, model selection did not necessarily focus on benchmarking various ML models, but rather testing the validity and utility of an integrated approach. To enhance predictive accuracy while preserving transparency, we implemented a decision-tree model because it is designed to clearly illustrate how input variables contribute to a final classification. For practical case-level decision-making, we integrate an LLM (i.e., GPT-o3) to convert model outputs into accessible, natural-language explanations tailored explicitly for case managers. The refinement and finalization of these models were embedded into a practitioner-in-the-loop workflow, ensuring that domain experts actively contributed throughout feature engineering, model design, and results interpretation.

#### Predictive Model with Transparency: Decision Tree

Decision tree models provide visual representations of how input features guide classification decisions. These models are inherently transparent, in that they explicitly identify key branching points based on feature thresholds to show the combinations of characteristics that place students at greater risk of delayed graduation. Compared ML models that may remain accurate but opaque (i.e. “black-box models”), decision trees are equipped to foster practitioner understanding and trust, making them particularly suitable for applied settings such as nonprofit program monitoring. As [[40](https://arxiv.org/html/2510.19799v1#biba.bibx17)] argues, when decisions carry significant real-world implications, interpretable models may be more appropriate compared to post-hoc explanations of opaque algorithms (e.g., neural networks). Moreover, evidence suggests that interpretable models often achieve comparable or even superior predictive performance relative to black-box methods [[26](https://arxiv.org/html/2510.19799v1#biba.bibx3)].

To select an optimal decision-tree model, we conducted a rigorous hyperparameter tuning process using a grid search approach (i.e., iterating all possible parametric combinations). Appendix LABEL:sec:grid\_search includes details of this process.

#### Case-Level Prediction and Interpretation: Large Language Model

We instruct the LLM to generate clear, case-specific explanations based on the decision tree model with case managers as the intended audience. Prompt engineering is central in this process and includes: (1) the structure of the trained decision tree, (2) the specific input data of the student, (3) the model’s prediction for the student, (4) the key predictors driving the prediction, and (5) potential intervention strategies to address areas of concern. This approach was structured to enable case managers to quickly interpret the results, identify critical issues, and effectively respond with student-specific interventions.

To establish a performance baseline, we also tested whether an LLM could predict a student’s risk status directly from their data, without relying on the decision tree model or program-specific knowledge. This *LLM-zero-shot* approach [[36](https://arxiv.org/html/2510.19799v1#biba.bibx13), [45](https://arxiv.org/html/2510.19799v1#biba.bibx22)] serves as a benchmark to evaluate the added value of our integrated decision-tree method. As shown in Table [3](https://arxiv.org/html/2510.19799v1#S3.T3 "Table 3 ‣ 3.2 Model Performance ‣ 3 Results") and Figure [2(b)](https://arxiv.org/html/2510.19799v1#S3.F2.sf2 "In Figure 2 ‣ 3.2 Model Performance ‣ 3 Results"), the decision tree model consistently outperforms the LLM-zero-shot approach across all cohort years on all performance metrics. This performance gap underscores the critical role of decision tree in improving predictive accuracy for this task.

### 2.4 Evaluation

#### Model Performance Metrics

To assess the predictive quality of the decision tree models, we adopted a suite of metrics that are robust to class imbalance. In this case, a naive model could achieve high overall accuracy by always predicting the majority class due to imbalance. In such cases, additional metrics are needed, specifically precision, recall, F1-score, and area under the receiver operating characteristic curve (AUC-ROC). Each of these metrics are defined below:

* •

  Precision quantifies the proportion of correctly identified at-risk students among all students flagged by the model, reflecting how actionable the alerts are for case managers.
* •

  Recall measures the share of truly at-risk students that the model successfully identifies, capturing the model’s ability to minimize missed interventions.
* •

  F1-score is the harmonic mean of precision and recall, providing a single summary that balances the costs of false positives and false negatives in an imbalanced setting.
* •

  AUC-ROC (Area under the Receiver Operating Characteristic Curve) evaluates discriminatory power across all possible classification thresholds, offering a threshold-independent view of model performance.

#### Practitioner-in-the-Loop

Quantitative scores alone are insufficient for deployment in a high-stakes, student-facing context, as the decision tree model output may not be practically useful for case managers and other front-line practitioners. In this project, we embedded a “practitioner-in-the-loop” approach (Figure [1](https://arxiv.org/html/2510.19799v1#S2.F1 "Figure 1 ‣ Practitioner-in-the-Loop ‣ 2.4 Evaluation ‣ 2 Methods")) at every major stage (research design, model validation, prompt engineering, and results interpretation) to help ensure that model results are appropriate. This approach treated practitioners as both knowledge generators and ultimate consumers, an approach advocated for in the nonprofit and research translation literature \autocites[144, Table 2]SalipanteManagersKnowledgeGenerators2003BonneyCanCitizenScience2016.

Figure 1: Practitioner-in-the-Loop Workflow

![Refer to caption](x1.png)

Feature and Framing Review (Figure [1](https://arxiv.org/html/2510.19799v1#S2.F1 "Figure 1 ‣ Practitioner-in-the-Loop ‣ 2.4 Evaluation ‣ 2 Methods")*a*): Adopting an abductive perspective [[43](https://arxiv.org/html/2510.19799v1#biba.bibx20)], the predictors used in the decision tree models were identified in collaboration with front-line staff. Program managers participated in multiple working sessions to review candidate predictors for face validity and potential bias. This step ensured that model inputs consistently aligned with both theoretical frameworks and practical experience.

Prompt Engineering Cycles (Figure [1](https://arxiv.org/html/2510.19799v1#S2.F1 "Figure 1 ‣ Practitioner-in-the-Loop ‣ 2.4 Evaluation ‣ 2 Methods")*b*): After the decision tree was finalized, we conducted iterative prompt-engineering sessions with case managers. Each session provided the LLM with: (1) the tree’s rule path for a given student, (2) the student’s data points, and (3) the model’s risk prediction. Case managers critiqued the generated explanations on clarity, relevance, and usability, leading to successive refinement of the prompt template.

Usability Assessment (Figure [1](https://arxiv.org/html/2510.19799v1#S2.F1 "Figure 1 ‣ Practitioner-in-the-Loop ‣ 2.4 Evaluation ‣ 2 Methods")*c*): In a final session, three case managers rated 30 anonymized LLM explanations on a 5-point Likert scale covering usefulness, transparency, and safety \autocitesWangUnderstandingUserExperience2024CalvanoLeveragingLargeLanguage2025QuttainahCostUsabilityCredibility2024HaoExploringCollaborativeDecisionmaking2024. Appendix LABEL:sec:usability\_assessment and LABEL:sec:usability\_questionnaire provide more details.

Together, the quantitative performance metrics and qualitative feedback from practitioners provide a comprehensive evaluation of the modeling pipeline.

## 3 Results

### 3.1 Descriptive Statistics

The panel is unbalanced and comprises 2,245 students followed across multiple years. The sample is comprised of students from multiple cohorts. Most (75.06%) students in the sample graduated within four years of first enrollment. [Table 2](https://arxiv.org/html/2510.19799v1#S3.T2 "Table 2 ‣ 3.1 Descriptive Statistics ‣ 3 Results") summarizes the descriptive statistics of key panel variables that consistently appear in the final decision trees of all cohort years. Cost of attendance averages hover around $34 k with substantial variability (SD ≈\approx $18–22 k) and a maximum of $128 k. Credits toward degree mirror a student’s academic progress, climbing sharply from a mean of 33.6 credits after the student’s first year to a mean of 114.5 credits in the student’s fourth year. Cumulative GPA remains remarkably stable after the student’s first year, centering on 3.26/4 for the first three years and dipping only slightly to 3.25/4 in the 4th year. Grant aid grows steadily from $11.8k to $17.2k, suggesting increased financial support as students advance, whereas total loan debt shows low means (≈\approx $1.4 k) and medians of zero each year, indicating that most students either incur no debt or rely primarily on grants and the scholarship provided by the program. Together, these figures depict a trajectory characterized by rising academic progress and grant aid with stable academic performance and limited reliance on loans.

Table 2: Key Descriptive Statistics by Cohort Year (Years 1–4)

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Cohort | Count | Mean | SD | Min | 50% | Max |
| Cost of attendance | | | | | | |
| 1 | 2 233 | 34 391.94 | 18 408.63 | 0.00 | 27 860.00 | 90 828.00 |
| 2 | 2 206 | 33 345.29 | 19 678.21 | 0.00 | 27 472.50 | 87 688.00 |
| 3 | 2 106 | 33 886.89 | 20 493.87 | 0.00 | 27 915.50 | 109 405.00 |
| 4 | 1 867 | 34 045.06 | 22 172.49 | 0.00 | 28 394.00 | 128 334.00 |
| Credits toward degree | | | | | | |
| 1 | 2 220 | 33.58 | 22.93 | 0.00 | 29.00 | 180.00 |
| 2 | 2 189 | 55.13 | 28.03 | 0.00 | 51.00 | 205.00 |
| 3 | 2 075 | 85.08 | 33.65 | 0.00 | 83.00 | 255.00 |
| 4 | 1 852 | 114.48 | 39.33 | 0.00 | 120.00 | 420.00 |
| GPA (cumulative) | | | | | | |
| 1 | 2 245 | 3.260 | 0.536 | 0.44 | 3.370 | 4.00 |
| 2 | 2 236 | 3.264 | 0.530 | 0.50 | 3.380 | 4.00 |
| 3 | 2 201 | 3.267 | 0.522 | 0.69 | 3.370 | 4.00 |
| 4 | 2 011 | 3.252 | 0.527 | 0.69 | 3.360 | 4.00 |
| Grant aid | | | | | | |
| 1 | 2 233 | 11 781.55 | 7 296.92 | 0.00 | 10 920.00 | 95 291.00 |
| 2 | 2 206 | 14 245.07 | 12 273.95 | 0.00 | 11 495.00 | 89 621.00 |
| 3 | 2 106 | 15 546.40 | 14 958.32 | 0.00 | 12 086.00 | 108 761.00 |
| 4 | 1 867 | 17 172.65 | 18 355.00 | 0.00 | 12 009.00 | 93 495.00 |
| Total loan debt | | | | | | |
| 1 | 1 449 | 1 382.15 | 4 608.48 | 0.00 | 0.00 | 60 684.00 |
| 2 | 1 449 | 1 382.15 | 4 608.48 | 0.00 | 0.00 | 60 684.00 |
| 3 | 1 424 | 1 351.59 | 4 572.04 | 0.00 | 0.00 | 60 684.00 |
| 4 | 1 265 | 1 380.36 | 4 691.60 | 0.00 | 0.00 | 60 684.00 |

### 3.2 Model Performance

As reported in [Table 3](https://arxiv.org/html/2510.19799v1#S3.T3 "Table 3 ‣ 3.2 Model Performance ‣ 3 Results"), the decision trees deliver strong and consistent classification results across cohort years. Overall accuracy ranges between 0.88 and 0.90 across cohort years. Precision for the minority “at-risk” class is high (0.78–0.86), while recall spans 0.68–0.73, yielding F1-scores between 0.74 and 0.78. In contrast, the majority “graduate on time” class demonstrates very high precision (0.90–0.92) and recall (0.94–0.96), producing F1-scores at or above 0.92. These patterns reflect the roughly 3:1 class imbalance: the models minimize false positives without severely sacrificing sensitivity.

Discriminatory power remains robust across cohort years, as illustrated by the ROC curves in [Figure 2](https://arxiv.org/html/2510.19799v1#S3.F2 "Figure 2 ‣ 3.2 Model Performance ‣ 3 Results"). The corresponding AUC values are 0.92 (cohort year 1), 0.91 (cohort year 2), 0.88 (cohort year 3), and 0.89 (cohort year 4), all comfortably surpassing the 0.80 benchmark for acceptable classification [[27](https://arxiv.org/html/2510.19799v1#biba.bibx4)] and well above random chance (i.e., 0.5). The modest dip for cohort year 3 aligns with its slightly lower AUC, yet the model still attains acceptable F1-score (0.77) and AUC (0.80).

These metrics indicate that the transparent decision-tree model provides reliable early-warning signals while keeping false alarms at a manageable level. This reliability is essential for practitioner workflows with limited intervention bandwidth. The visualizations of each tree structure are available at [Open Science Framework](https://osf.io/kfpej/?view_only=709ea028b2b0433c9c8ed2ed034c5c58),111<https://osf.io/kfpej/?view_only=709ea028b2b0433c9c8ed2ed034c5c58> where users can explore the exact splits that underpin each prediction.

Table 3: Model Performance Metrics by Cohort Year

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Cohort Year | Prediction | Precision | Recall | F1-score | #Case |
| 1 | At-risk | 0.78 (0.41) | 0.70 (0.72) | 0.74 (0.52) | 107 (46) |
| Graduate on time | 0.91 (0.89) | 0.94 (0.69) | 0.92 (0.78) | 333 (153) |
|  | Weighted Accuracy |  |  | 0.88 (0.72) | 440 (199) |
| 2 | At-risk | 0.86 (0.55) | 0.68 (0.84) | 0.76 (0.66) | 108 (61) |
| Graduate on time | 0.90 (0.91) | 0.96 (0.70) | 0.93 (0.79) | 334 (139) |
|  | Weighted Accuracy |  |  | 0.89 (0.75) | 442 (200) |
| 3 | At-risk | 0.81 (0.31) | 0.73 (0.87) | 0.77 (0.46) | 108 (37) |
| Graduate on time | 0.92 (0.95) | 0.95 (0.57) | 0.93 (0.71) | 334 (161) |
|  | Weighted Accuracy |  |  | 0.89 (0.66) | 442 (198) |
| 4 | At-risk | 0.84 (0.35) | 0.72 (0.85) | 0.78 (0.50) | 108 (47) |
| Graduate on time | 0.91 (0.92) | 0.96 (0.52) | 0.93 (0.67) | 335 (153) |
|  | Weighted Accuracy |  |  | 0.90 (0.63) | 443 (200) |

*Note*: Values in parentheses show the performance of the baseline *LLM-zero-shot* (GPT-o3) model, which predicts outcomes directly from student data without using the decision tree or program-specific knowledge.

![Refer to caption](x2.png)


(a) Decision Tree

![Refer to caption](x3.png)


(b) LLM-zero-shot (GPT-o3)

Figure 2: AUC-ROC Curves for Decision Tree and LLM-zero-shot Models Across Cohorts

### 3.3 Case‐Level Prediction and Interpretation

To translate model scores into actionable guidance, we employed an LLM which ingests the trained decision‐tree, the focal student’s data, and the predicted classification. The model was instructed to then produce a plain-language explanation targeted at case managers. The prompt template (Appendix LABEL:sec:llm\_prompts) instructed the LLM to (1) state the predicted class with its node-level probability, (2) walk through every split in the path using conversational comparisons (e.g., “GPA below 10th percentile”), (3) highlight the top five drivers in everyday terms, (4) flag borderline features that could flip the outcome, and (5) close with concise, adviser-oriented takeaways.

To leverage organizational expertise and enhance explanation quality, we experimented with two prompt variants: one that provides only the decision-tree path and student data (Appendix Figure LABEL:fig:llm\_prompt\_wo\_kb), and another that supplements this information with curated program knowledge distilled from case managers’ best practices (Appendix Figure LABEL:fig:llm\_prompt\_wt\_kb). The program knowledge encompasses established intervention strategies, including academic tutoring protocols, financial counseling frameworks, and mental health support resources, which the LLM can reference to generate more contextually appropriate and actionable recommendations. This in-context learning approach [[28](https://arxiv.org/html/2510.19799v1#biba.bibx5)] has been shown to enable LLMs to produce explanations that align model predictions with organizational expertise.

Appendix Figure LABEL:fig:llm\_output shows one anonymized output for a student in their third year with a predicted NoGrad4yr classification at 83% probability. The LLM first articulates the risk score, then lays out a four-node path that moves from “zero loan debt”—a potential proxy for working long hours to avoid debt—to “very low GPA,” concluding in a terminal node that historically contains 25 non-graduates versus 5 graduates. The explanation pinpoints low GPA, high cost of attendance, and modest remaining credits as the dominant risk factors, but also notes that the GPA is just below an actionable threshold for academic tutoring. Importantly, the final bullet list converts these insights into concrete adviser actions (e.g., “raise GPA one letter grade,” “explore additional grant aid or financial counseling to reduce cost pressure”), demonstrating how model logic is bridged to practice.

### 3.4 Usability Assessment

Thirty LLM-generated at-risk predictions (e.g., Appendix Figure LABEL:fig:llm\_output) were randomly selected from the full evaluation set, and rated by three case managers on a five-point Likert scale covering *usefulness*, *transparency*, and *safety* (Appendix Table LABEL:tab:usability\_metrics). Figure [3](https://arxiv.org/html/2510.19799v1#S3.F3 "Figure 3 ‣ 3.4 Usability Assessment ‣ 3 Results") summarizes the results. The means of all dimensions exceed 3.0, suggesting that the explanations are generally perceived as useful, transparent, and safe. Notably, the scores of *Fairness* (M​e​a​n=3.66,S​D=0.72Mean=3.66,SD=0.72) and *No Harm* (M​e​a​n=3.46,S​D=0.81Mean=3.46,SD=0.81) received relatively higher ratings compared to other dimensions, suggesting that case managers perceive these explanations as less likely to introduce bias or cause negative consequences, both of which are critical considerations for high-stakes student interventions.

![Refer to caption](x4.png)


Figure 3: Usability Test Results for LLM-Generated Explanations

To understand whether incorporating program knowledge (Appendix Figure LABEL:fig:llm\_prompt\_wt\_kb) improves explanation quality compared to using only the decision-tree path and student data (Appendix Figure LABEL:fig:llm\_prompt\_wo\_kb), we conducted a controlled comparison. LLM-generated explanations using the two variants of prompts were provided to case managers without the case managers knowing whether a specific explanation produced from a prompt with program knowledge. Since each case manager evaluated multiple explanations and specific student cases might inherently be easier or harder to interpret, we employed regression analysis to isolate the effect of program knowledge while controlling for potential confounding factors. Specifically, we ran separate regressions using the Likert scores on each dimension as outcome variables and a binary indicator of prompt type (with vs. without program knowledge) as the key predictor, controlling for fixed effects: case manager ID, student case ID, and cohort year, with standard errors clustered by case manager ID.

![Refer to caption](x5.png)

Figure 4: Usability Test Results: With vs. Without Program Knowledge

*Note*: Each point represents the estimated coefficient for “with program knowledge” (base group: without program knowledge) from separate regressions on each usability dimension (i.e., Y-axis = DVs). Error bars indicate 90% confidence intervals.

Figure [4](https://arxiv.org/html/2510.19799v1#S3.F4 "Figure 4 ‣ 3.4 Usability Assessment ‣ 3 Results") shows the regression results. Incorporating program knowledge significantly improved most dimensions, with the exception of “Clarity,” “Utility,” and “Time Saved.” The largest positive effect is on “No Harm” (β=0.93,p=0.02\beta=0.93,p=0.02), indicating that explanations with program knowledge are rated nearly a full point higher on the five-point scale for safety. This is followed by “Precision” (β=0.60,p<0.01\beta=0.60,p<0.01) and “Fairness” (β=0.54,p=0.02\beta=0.54,p=0.02), both showing substantial improvements of over half a scale point. These findings suggest that domain expertise enhances the trustworthiness and safety of AI-generated explanations rather than their operational efficiency.

Interestingly, feeding program knowledge does not appear to improve perceived time savings, perceived utility, or clarity. This pattern aligns with our practitioner-in-the-loop philosophy: while domain knowledge may not always accelerate decision-making or simplify explanations, it critically enhances the safety and fairness dimensions that practitioners value most when deploying AI in sensitive educational contexts. The results underscore that responsible AI adoption in the nonprofit sector requires not just technical accuracy but also the integration of contextual expertise to ensure ethical and trustworthy deployment.

## 4 Discussion

This study offers an example of integrating transparent predictive modeling with AI interpretation for case-level decision-making in a nonprofit scholarship program. We developed a decision-tree model to predict which students are at risk of delayed graduation and paired it with an LLM to produce actionable explanations for case managers. This approach addresses two common challenges in nonprofit analytics: the need for interpretable, actionable insights at the individual level and the need for trustworthy, transparent models in high-stakes contexts. We found that a simple, interpretable model provided sufficient predictive accuracy. When combined with an LLM, the model produced clear insights at the case-level. There are several lessons from this work that nonprofit organizations adopting AI may wish to consider.

##### Workflow with AI tools integrated.

A first lesson regards the importance of defining the role of AI within a project’s workflow, including the division of labor between AI and human practitioners. In this case, we integrated AI as a decision-support tool with a practitioner-in-the-loop framework integrated at onset. A decision tree model was intentionally chosen to maximize transparency, and the model remained highly accurate in its predictions. In our implementation, the AI components inform decisions, rather than direct them: the model flags at-risk students, and the LLM provides reasoning and suggestions, but case managers remain the ultimate decision-makers. This delineation ensures the appropriate use of AI while practitioners managed nuanced judgment and intervention planning. Further, case managers understood at the onset that the AI system was there to assist their expertise. This approach may facilitate buy-in and trust among staff new to using AI, as well as those wary of using it in a systematic way for decision-making. This case supports recent calls from [[26](https://arxiv.org/html/2510.19799v1#biba.bibx3)] and [[46](https://arxiv.org/html/2510.19799v1#biba.bibx23)] to consider practitioners as collaborators in the analytic process.

##### Knowledge base for AI, grounded in human expertise.

A second lesson centers on the value of establishing a *knowledge base* grounded in existing program expertise. Integrating staff knowledge into the model improved the relevance and actionability of LLM recommendations. When the LLM had access to program-specific knowledge, its explanations were rated significantly higher by case managers on dimensions of fairness, safety, and trust compared to explanations without that knowledge base. In practice, this meant the LLM suggestions aligned with empiric intervention strategies and avoided potentially insensitive or infeasible recommendations. Organizations interested in integrating LLM into their workflow may benefit from intentionally incorporating organizational knowledge into the model, as this helps ensure that insights align with context-specific reality and reinforces practitioner trust in model outputs.

##### Transparency over complexity.

Results support the use of transparent models when accuracy is sufficient and staff utility is a priority. These models can be sufficiently accurate and may be more appropriate than more sophisticated ensemble “black-box” models when the purpose pertains to high-stakes predictive tasks \autocitesChenInterpretableModelGlobally2018RudinStopExplainingBlack2019. Despite its simple structure, the model achieved strong predictive performance while offering clear logic for each prediction. For example, instead of simply telling a case manager that “Student Y has a 83% chance of not graduating on time,” the model might explain:

> “Student Y is at high risk because their GPA dropped below 2.5 this term while taking on extra work hours; similar cases who reduced work hours experienced improved academic outcomes. Consider adjusting this student’s workload via increased financial support or providing tutoring.”

In our case, the decision tree’s performance was within a few points of more complex algorithms used in similar contexts [[46](https://arxiv.org/html/2510.19799v1#biba.bibx23)], offering little practical incentive to incur the opacity of a more sophisticated approach. If a simpler model can achieve the needed accuracy, organizations should consider opting for transparency due to the potential dividends in staff acceptance and clarity. Moreover, using an interpretable model simplifies the task of diagnosing errors or biases, which is crucial for responsible AI use in social sector projects.

## References

* [1]
  Rick Bonney, Tina B. Phillips, Heidi L. Ballard and Jody W. Enck
  “Can Citizen Science Enhance Public Understanding of Science?”
  In *Public Understanding of Science* 25.1
  SAGE Publications Ltd, 2016, pp. 2–16
  DOI: [10.1177/0963662515607406](https://dx.doi.org/10.1177/0963662515607406)
* [2]
  Miriana Calvano et al.
  “Leveraging Large Language Models for Usability Testing: A Preliminary Study”
  In *Companion Proceedings of the 30th International Conference on Intelligent User Interfaces*
  Cagliari Italy: ACM, 2025, pp. 78–81
  DOI: [10.1145/3708557.3716341](https://dx.doi.org/10.1145/3708557.3716341)
* [3]
  Chaofan Chen et al.
  “An Interpretable Model with Globally Consistent Explanations for Credit Risk”
  arXiv, 2018
  DOI: [10.48550/arXiv.1811.12615](https://dx.doi.org/10.48550/arXiv.1811.12615)
* [4]
  Şeref Kerem Çorbacıoğlu and Gökhan Aksel
  “Receiver Operating Characteristic Curve Analysis in Diagnostic Accuracy Studies: A Guide to Interpreting the Area under the Curve Value”
  In *Turkish Journal of Emergency Medicine* 23.4, 2023, pp. 195–198
  DOI: [10.4103/tjem.tjem\_182\_23](https://dx.doi.org/10.4103/tjem.tjem_182_23)
* [5]
  Qingxiu Dong et al.
  “A Survey on In-context Learning”
  arXiv, 2024
  DOI: [10.48550/arXiv.2301.00234](https://dx.doi.org/10.48550/arXiv.2301.00234)
* [6]
  Allison H. Fine, Colette E. Thayer and Anne Coghlan
  “Program Evaluation Practice in the Nonprofit Sector”
  In *Nonprofit Management and Leadership* 10.3
  John Wiley & Sons, Ltd, 2000, pp. 331–339
  DOI: [10.1002/nml.10309](https://dx.doi.org/10.1002/nml.10309)
* [7]
  Xinyue Hao, Emrah Demir and Daniel Eyers
  “Exploring Collaborative Decision-Making: A Quasi-Experimental Study of Human and Generative AI Interaction”
  In *Technology in Society* 78, 2024, pp. 102662
  DOI: [10.1016/j.techsoc.2024.102662](https://dx.doi.org/10.1016/j.techsoc.2024.102662)
* [8]
  Laura Hesse
  “Using Machine Learning to Understand and Manage the Transformation of Peer Donors to Organizational Donors”
  In *Nonprofit Management and Leadership* n/a.n/a, 2025
  DOI: [10.1002/nml.21652](https://dx.doi.org/10.1002/nml.21652)
* [9]
  Jake M. Hofman et al.
  “Integrating Explanation and Prediction in Computational Social Science”
  In *Nature* 595.7866
  Nature Publishing Group, 2021, pp. 181–188
  DOI: [10.1038/s41586-021-03659-0](https://dx.doi.org/10.1038/s41586-021-03659-0)
* [10]
  Joan Hope
  “Boost First-Generation, Low-Income Student Attainment by Removing Barriers to Success”
  In *The Successful Registrar* 16.9, 2016, pp. 6–7
  DOI: [10.1002/tsr.30239](https://dx.doi.org/10.1002/tsr.30239)
* [11]
  Kate Keahey et al.
  “Lessons Learned from the Chameleon Testbed”
  In *2020 {}USENIX{} Annual Technical Conference ({}USENIX{} {}ATC{} 20)*, 2020, pp. 219–233
  URL: <https://www.usenix.org/conference/atc20/presentation/keahey>
* [12]
  Stacy Song Kehoe
  “Bridging the College Completion Gap with Comprehensive Support Systems: A Mixed-Methods Impact Evaluation of the Dell Scholars Program”
  In *ProQuest Dissertations and Theses*, 2017
  URL: <http://ezproxy.lib.utexas.edu/login?url=https://www.proquest.com/dissertations-theses/bridging-college-completion-gap-with/docview/2026720214/se-2?accountid=7118>
* [13]
  Takeshi Kojima et al.
  “Large Language Models Are Zero-Shot Reasoners”
  In *Advances in Neural Information Processing Systems* 35, 2022, pp. 22199–22213
  URL: <https://proceedings.neurips.cc/paper%5C_files/paper/2022/hash/8bb0d291acd4acf06ef112099c16f326-Abstract-Conference.html>
* [14]
  Lindsay C. Page and Judith Scott-Clayton
  “Improving College Access in the United States: Barriers and Policy Responses”
  In *Economics of Education Review* 51, Access to Higher Education, 2016, pp. 4–22
  DOI: [10.1016/j.econedurev.2016.02.009](https://dx.doi.org/10.1016/j.econedurev.2016.02.009)
* [15]
  Lindsay C. Page, Stacy S. Kehoe, Benjamin L. Castleman and Gumilang Aryo Sahadewo
  “More than Dollars for Scholars: The Impact of the Dell Scholars Program on College Access, Persistence, and Degree Attainment”
  In *Journal of Human Resources* 54.3
  University of Wisconsin Press, 2019, pp. 683–725
  DOI: [10.3368/jhr.54.3.0516.7935R1](https://dx.doi.org/10.3368/jhr.54.3.0516.7935R1)
* [16]
  Majdi Quttainah et al.
  “Cost, Usability, Credibility, Fairness, Accountability, Transparency, and Explainability Framework for Safe and Effective Large Language Models in Medical Education: Narrative Review and Qualitative Study”
  In *JMIR AI* 3.1
  JMIR Publications Inc., Toronto, Canada, 2024, pp. e51834
  DOI: [10.2196/51834](https://dx.doi.org/10.2196/51834)
* [17]
  Cynthia Rudin
  “Stop Explaining Black Box Machine Learning Models for High Stakes Decisions and Use Interpretable Models Instead”
  In *Nature Machine Intelligence* 1.5
  Nature Publishing Group, 2019, pp. 206–215
  DOI: [10.1038/s42256-019-0048-x](https://dx.doi.org/10.1038/s42256-019-0048-x)
* [18]
  Gumilang Aryo Sahadewo
  “Essays in the Economics of Education and Experimental Economics”
  In *ProQuest Dissertations and Theses*, 2017
  URL: <http://ezproxy.lib.utexas.edu/login?url=https://www.proquest.com/dissertations-theses/essays-economics-education-experimental/docview/2013162609/se-2?accountid=7118>
* [19]
  Paul Salipante and John D. Aram
  “Managers as Knowledge Generators: The Nature of Practitioner-Scholar Research in the Nonprofit Sector”
  In *Nonprofit Management and Leadership* 14.2, 2003, pp. 129–150
  DOI: [10.1002/nml.26](https://dx.doi.org/10.1002/nml.26)
* [20]
  Rachel Taylor, Nuttaneeya (Ann) Torugsa and Anthony Arundel
  “Leaping Into Real-World Relevance: An “Abduction” Process for Nonprofit Research”
  In *Nonprofit and Voluntary Sector Quarterly* 47.1
  SAGE Publications Inc, 2018, pp. 206–227
  DOI: [10.1177/0899764017718635](https://dx.doi.org/10.1177/0899764017718635)
* [21]
  Jiayin Wang et al.
  “Understanding User Experience in Large Language Model Interactions”
  arXiv, 2024
  DOI: [10.48550/arXiv.2401.08329](https://dx.doi.org/10.48550/arXiv.2401.08329)
* [22]
  Jason Wei et al.
  “Finetuned Language Models Are Zero-Shot Learners”
  arXiv, 2022
  DOI: [10.48550/arXiv.2109.01652](https://dx.doi.org/10.48550/arXiv.2109.01652)
* [23]
  Yanxiang Yang, Terri Byers and Joerg Koenigstorfer
  “A Machine-Learning Approach to Understanding Performance of Canadian Nonprofit Sport Organizations”
  In *Nonprofit Management and Leadership* n/a.n/a, 2025
  DOI: [10.1002/nml.21651](https://dx.doi.org/10.1002/nml.21651)

## References

* [24]
  Rick Bonney, Tina B. Phillips, Heidi L. Ballard and Jody W. Enck
  “Can Citizen Science Enhance Public Understanding of Science?”
  In *Public Understanding of Science* 25.1
  SAGE Publications Ltd, 2016, pp. 2–16
  DOI: [10.1177/0963662515607406](https://dx.doi.org/10.1177/0963662515607406)
* [25]
  Miriana Calvano et al.
  “Leveraging Large Language Models for Usability Testing: A Preliminary Study”
  In *Companion Proceedings of the 30th International Conference on Intelligent User Interfaces*
  Cagliari Italy: ACM, 2025, pp. 78–81
  DOI: [10.1145/3708557.3716341](https://dx.doi.org/10.1145/3708557.3716341)
* [26]
  Chaofan Chen et al.
  “An Interpretable Model with Globally Consistent Explanations for Credit Risk”
  arXiv, 2018
  DOI: [10.48550/arXiv.1811.12615](https://dx.doi.org/10.48550/arXiv.1811.12615)
* [27]
  Şeref Kerem Çorbacıoğlu and Gökhan Aksel
  “Receiver Operating Characteristic Curve Analysis in Diagnostic Accuracy Studies: A Guide to Interpreting the Area under the Curve Value”
  In *Turkish Journal of Emergency Medicine* 23.4, 2023, pp. 195–198
  DOI: [10.4103/tjem.tjem\_182\_23](https://dx.doi.org/10.4103/tjem.tjem_182_23)
* [28]
  Qingxiu Dong et al.
  “A Survey on In-context Learning”
  arXiv, 2024
  DOI: [10.48550/arXiv.2301.00234](https://dx.doi.org/10.48550/arXiv.2301.00234)
* [29]
  Allison H. Fine, Colette E. Thayer and Anne Coghlan
  “Program Evaluation Practice in the Nonprofit Sector”
  In *Nonprofit Management and Leadership* 10.3
  John Wiley & Sons, Ltd, 2000, pp. 331–339
  DOI: [10.1002/nml.10309](https://dx.doi.org/10.1002/nml.10309)
* [30]
  Xinyue Hao, Emrah Demir and Daniel Eyers
  “Exploring Collaborative Decision-Making: A Quasi-Experimental Study of Human and Generative AI Interaction”
  In *Technology in Society* 78, 2024, pp. 102662
  DOI: [10.1016/j.techsoc.2024.102662](https://dx.doi.org/10.1016/j.techsoc.2024.102662)
* [31]
  Laura Hesse
  “Using Machine Learning to Understand and Manage the Transformation of Peer Donors to Organizational Donors”
  In *Nonprofit Management and Leadership* n/a.n/a, 2025
  DOI: [10.1002/nml.21652](https://dx.doi.org/10.1002/nml.21652)
* [32]
  Jake M. Hofman et al.
  “Integrating Explanation and Prediction in Computational Social Science”
  In *Nature* 595.7866
  Nature Publishing Group, 2021, pp. 181–188
  DOI: [10.1038/s41586-021-03659-0](https://dx.doi.org/10.1038/s41586-021-03659-0)
* [33]
  Joan Hope
  “Boost First-Generation, Low-Income Student Attainment by Removing Barriers to Success”
  In *The Successful Registrar* 16.9, 2016, pp. 6–7
  DOI: [10.1002/tsr.30239](https://dx.doi.org/10.1002/tsr.30239)
* [34]
  Kate Keahey et al.
  “Lessons Learned from the Chameleon Testbed”
  In *2020 {}USENIX{} Annual Technical Conference ({}USENIX{} {}ATC{} 20)*, 2020, pp. 219–233
  URL: <https://www.usenix.org/conference/atc20/presentation/keahey>
* [35]
  Stacy Song Kehoe
  “Bridging the College Completion Gap with Comprehensive Support Systems: A Mixed-Methods Impact Evaluation of the Dell Scholars Program”
  In *ProQuest Dissertations and Theses*, 2017
  URL: <http://ezproxy.lib.utexas.edu/login?url=https://www.proquest.com/dissertations-theses/bridging-college-completion-gap-with/docview/2026720214/se-2?accountid=7118>
* [36]
  Takeshi Kojima et al.
  “Large Language Models Are Zero-Shot Reasoners”
  In *Advances in Neural Information Processing Systems* 35, 2022, pp. 22199–22213
  URL: <https://proceedings.neurips.cc/paper%5C_files/paper/2022/hash/8bb0d291acd4acf06ef112099c16f326-Abstract-Conference.html>
* [37]
  Lindsay C. Page, Stacy S. Kehoe, Benjamin L. Castleman and Gumilang Aryo Sahadewo
  “More than Dollars for Scholars: The Impact of the Dell Scholars Program on College Access, Persistence, and Degree Attainment”
  In *Journal of Human Resources* 54.3
  University of Wisconsin Press, 2019, pp. 683–725
  DOI: [10.3368/jhr.54.3.0516.7935R1](https://dx.doi.org/10.3368/jhr.54.3.0516.7935R1)
* [38]
  Lindsay C. Page and Judith Scott-Clayton
  “Improving College Access in the United States: Barriers and Policy Responses”
  In *Economics of Education Review* 51, Access to Higher Education, 2016, pp. 4–22
  DOI: [10.1016/j.econedurev.2016.02.009](https://dx.doi.org/10.1016/j.econedurev.2016.02.009)
* [39]
  Majdi Quttainah et al.
  “Cost, Usability, Credibility, Fairness, Accountability, Transparency, and Explainability Framework for Safe and Effective Large Language Models in Medical Education: Narrative Review and Qualitative Study”
  In *JMIR AI* 3.1
  JMIR Publications Inc., Toronto, Canada, 2024, pp. e51834
  DOI: [10.2196/51834](https://dx.doi.org/10.2196/51834)
* [40]
  Cynthia Rudin
  “Stop Explaining Black Box Machine Learning Models for High Stakes Decisions and Use Interpretable Models Instead”
  In *Nature Machine Intelligence* 1.5
  Nature Publishing Group, 2019, pp. 206–215
  DOI: [10.1038/s42256-019-0048-x](https://dx.doi.org/10.1038/s42256-019-0048-x)
* [41]
  Gumilang Aryo Sahadewo
  “Essays in the Economics of Education and Experimental Economics”
  In *ProQuest Dissertations and Theses*, 2017
  URL: <http://ezproxy.lib.utexas.edu/login?url=https://www.proquest.com/dissertations-theses/essays-economics-education-experimental/docview/2013162609/se-2?accountid=7118>
* [42]
  Paul Salipante and John D. Aram
  “Managers as Knowledge Generators: The Nature of Practitioner-Scholar Research in the Nonprofit Sector”
  In *Nonprofit Management and Leadership* 14.2, 2003, pp. 129–150
  DOI: [10.1002/nml.26](https://dx.doi.org/10.1002/nml.26)
* [43]
  Rachel Taylor, Nuttaneeya (Ann) Torugsa and Anthony Arundel
  “Leaping Into Real-World Relevance: An “Abduction” Process for Nonprofit Research”
  In *Nonprofit and Voluntary Sector Quarterly* 47.1
  SAGE Publications Inc, 2018, pp. 206–227
  DOI: [10.1177/0899764017718635](https://dx.doi.org/10.1177/0899764017718635)
* [44]
  Jiayin Wang et al.
  “Understanding User Experience in Large Language Model Interactions”
  arXiv, 2024
  DOI: [10.48550/arXiv.2401.08329](https://dx.doi.org/10.48550/arXiv.2401.08329)
* [45]
  Jason Wei et al.
  “Finetuned Language Models Are Zero-Shot Learners”
  arXiv, 2022
  DOI: [10.48550/arXiv.2109.01652](https://dx.doi.org/10.48550/arXiv.2109.01652)
* [46]
  Yanxiang Yang, Terri Byers and Joerg Koenigstorfer
  “A Machine-Learning Approach to Understanding Performance of Canadian Nonprofit Sport Organizations”
  In *Nonprofit Management and Leadership* n/a.n/a, 2025
  DOI: [10.1002/nml.21651](https://dx.doi.org/10.1002/nml.21651)

## References

* [47]
  Miriana Calvano et al.
  “Leveraging Large Language Models for Usability Testing: A Preliminary Study”
  In *Companion Proceedings of the 30th International Conference on Intelligent User Interfaces*
  Cagliari Italy: ACM, 2025, pp. 78–81
  DOI: [10.1145/3708557.3716341](https://dx.doi.org/10.1145/3708557.3716341)
* [48]
  Xinyue Hao, Emrah Demir and Daniel Eyers
  “Exploring Collaborative Decision-Making: A Quasi-Experimental Study of Human and Generative AI Interaction”
  In *Technology in Society* 78, 2024, pp. 102662
  DOI: [10.1016/j.techsoc.2024.102662](https://dx.doi.org/10.1016/j.techsoc.2024.102662)
* [49]
  Majdi Quttainah et al.
  “Cost, Usability, Credibility, Fairness, Accountability, Transparency, and Explainability Framework for Safe and Effective Large Language Models in Medical Education: Narrative Review and Qualitative Study”
  In *JMIR AI* 3.1
  JMIR Publications Inc., Toronto, Canada, 2024, pp. e51834
  DOI: [10.2196/51834](https://dx.doi.org/10.2196/51834)
* [50]
  Jiayin Wang et al.
  “Understanding User Experience in Large Language Model Interactions”
  arXiv, 2024
  DOI: [10.48550/arXiv.2401.08329](https://dx.doi.org/10.48550/arXiv.2401.08329)

## References

* [51]
  Miriana Calvano et al.
  “Leveraging Large Language Models for Usability Testing: A Preliminary Study”
  In *Companion Proceedings of the 30th International Conference on Intelligent User Interfaces*
  Cagliari Italy: ACM, 2025, pp. 78–81
  DOI: [10.1145/3708557.3716341](https://dx.doi.org/10.1145/3708557.3716341)
* [52]
  Xinyue Hao, Emrah Demir and Daniel Eyers
  “Exploring Collaborative Decision-Making: A Quasi-Experimental Study of Human and Generative AI Interaction”
  In *Technology in Society* 78, 2024, pp. 102662
  DOI: [10.1016/j.techsoc.2024.102662](https://dx.doi.org/10.1016/j.techsoc.2024.102662)
* [53]
  Majdi Quttainah et al.
  “Cost, Usability, Credibility, Fairness, Accountability, Transparency, and Explainability Framework for Safe and Effective Large Language Models in Medical Education: Narrative Review and Qualitative Study”
  In *JMIR AI* 3.1
  JMIR Publications Inc., Toronto, Canada, 2024, pp. e51834
  DOI: [10.2196/51834](https://dx.doi.org/10.2196/51834)
* [54]
  Jiayin Wang et al.
  “Understanding User Experience in Large Language Model Interactions”
  arXiv, 2024
  DOI: [10.48550/arXiv.2401.08329](https://dx.doi.org/10.48550/arXiv.2401.08329)

## Online Appendix

./msdf\_apdx.tex