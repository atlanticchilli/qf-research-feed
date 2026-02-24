---
authors:
- Wenxi Geng
- Dingyuan Liu
- Liya Li
- Yiqing Wang
doc_id: arxiv:2602.18895v1
family_id: arxiv:2602.18895
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Could Large Language Models work as Post-hoc Explainability Tools in Credit
  Risk Models?
url_abs: http://arxiv.org/abs/2602.18895v1
url_html: https://arxiv.org/html/2602.18895v1
venue: arXiv q-fin
version: 1
year: 2026
---


Wenxi Geng

Dingyuan Liu

Liya Li

Yiqing Wang
[woshilucy712@gmail.com](mailto:woshilucy712@gmail.com)

###### Abstract

Post-hoc explainability is central to credit risk model governance, yet widely used tools such as coefficient-based attributions and SHapley Additive exPlanations (SHAP) often produce numerical outputs that are difficult to communicate to non-technical stakeholders. This paper investigates whether large language models (LLMs) can serve as post-hoc explainability tools for credit risk predictions through in-context learning, focusing on two roles: translators and autonomous explainers.

In the translator role, the LLM is provided with instance-level information and a reference feature-importance ranking derived from an established explainer, and we evaluate whether it preserves the ranked structure. In the autonomous explainer role, we assess whether LLMs can independently infer feature-importance rankings that align with reference rankings, and examine the effect of different prompt designs on this alignment.

Using a personal lending dataset from LendingClub, we evaluate three commercial LLMs, including GPT-4-turbo, Claude Sonnet 4, and Gemini-2.0-Flash. Results provide strong evidence for the translator role: when reference rankings are provided under strict output constraints, LLMs almost always reproduce the correct top-KK feature set, with only rare deviations. In contrast, autonomous explanations show low alignment with model-based attributions. Few-shot prompting improves feature overlap for logistic regression but does not consistently benefit XGBoost, suggesting that LLMs have limited capacity to recover non-linear, interaction-driven reasoning from prompt cues alone.

Overall, our findings position LLMs as effective narrative interfaces grounded in auditable model attributions, rather than as substitutes for post-hoc explainers in credit risk model governance. Practitioners should leverage LLMs to bridge the communication gap between complex model outputs and regulatory or business stakeholders, while preserving the rigor and traceability required by credit risk governance frameworks.

###### keywords:

Large Language Model, Credit Risk Management , Machine Learning , Explainability AI

\affiliation

[author1]organization=Independent Researcher,
city=Charlton,
state=TX,
country=United States
\affiliation[author2]organization=University of North Carolina at Chapel Hill,city=Chapel Hill, North Carolina,
postcode=27599,
state=NC,
country=United States
\affiliation[author3]organization=Independent Researcher,
city=Houston,
state=TX,
country=United States
\affiliation[author4]organization=Independent Researcher,
city=Farmers Branch,
state=TX,
country=United States

## 1 Introduction

Rapid technological advances have enabled FinTech lenders to become major participants in the U.S. personal-loan market alongside traditional institutions. By 2022, FinTech-owned loans accounted for approximately 14% of personal loans in the United States (Flagg and Hannon, [2023](https://arxiv.org/html/2602.18895v1#bib.bib1 "FinTech-issued personal loans in the us")). This rapid growth has been driven in large part by the adoption of advanced machine learning (ML) models that streamline underwriting processes, improve predictive performance, and enhance predictive accuracy. Despite these advantages, the increasing reliance on complex and opaque ML models raises significant regulatory and risk management concerns. Regulatory frameworks such as the Equal Credit Opportunity Act (ECOA) (Act, [2018](https://arxiv.org/html/2602.18895v1#bib.bib18 "Equal credit opportunity act")) and the Fair Credit Reporting Act (FCRA) (Act, [2009](https://arxiv.org/html/2602.18895v1#bib.bib19 "Fair credit reporting act")) require lenders to provide clear exemptions for adverse credit decisions. Beyond regulatory compliance, explainability plays a critical role in fostering customer trust (Jennett et al., [2012](https://arxiv.org/html/2602.18895v1#bib.bib20 "Adding insult to injury: consumer experiences of being denied credit")), allowing internal auditing(Bulyga et al., [2020](https://arxiv.org/html/2602.18895v1#bib.bib21 "Transparency of credit institutions")), and supporting risk management practices (Aziz and Dowling, [2019](https://arxiv.org/html/2602.18895v1#bib.bib22 "Machine learning and ai for risk management")).

To mitigate the opacity of ML models, financial institutions commonly adopt post-hoc explainable AI (XAI) methods such as SHapley Additive exPlanations (SHAP) and Local Interpretable Model-agnostic Explanations (LIME) (Lundberg and Lee, [2017](https://arxiv.org/html/2602.18895v1#bib.bib7 "A unified approach to interpreting model predictions"); Ribeiro et al., [2016](https://arxiv.org/html/2602.18895v1#bib.bib8 "” Why should i trust you?” explaining the predictions of any classifier")). These techniques quantify feature-level contributions by decomposing model predictions into additive attribution components. While effective at identifying important features, such methods primarily provide numerical outputs-such as feature importance ranking or contribution values which are difficult to interpret and operationalize in decision-making process. Furthermore, these mathematical outputs lack the flexibility to incorporate domain-specific knowledge or generate contextual narratives that align with how credit analysts reason about lending decisions.

Recent advances in large language models (LLMs) offer a potential pathway to bridge this interpretability gap. LLMs have demonstrated remarkable capabilities in nature language understanding, reasoning, and generation in high-stake domains. Unlike traditional XAI approaches, LLMs may translate feature-level attributions into coherent, domain-informed explanations expressed in natural language. In principle, this capability positions LLMs as promising candidates for serving as narrative interfaces that renders ML-based credit decisions more transparent and accessible to diverse stakeholders. However, whether LLMs can reliably perform such translation tasks—and whether they can autonomously generate explanations that align with model-grounded attributions—remains an open empirical question.

In this paper, we investigate the potential of LLMs as post-hoc explainers for credit risk predictions through in-context learning (ICL), focusing on the following research questions:

* 1.

  RQ1 (LLM as Translator): To what extent can large language models accurately preserve feature-importance rankings when generating natural-language explanations, given reference attributions produced by established XAI methods (e.g., SHAP or logistic regression coefficients)? Specifically, can LLMs maintain the integrity of the ranked structure embedded in model-based explanations?
* 2.

  RQ2 (LLM as Autonomous Explainer): To what extent can large language models autonomously infer feature-importance rankings that align with model-based reference explanations (e.g., SHAP or logistic regression), when such rankings are not provided as inputs and how does few-shot prompting influence this alignment?

We find that, in a controlled setting where reference rankings are provided, LLMs almost always preserve the correct Top-KK feature set, with only rare deviations. In contrast, when reference rankings are not supplied, alignment with model-based explanations is generally low. Few-shot prompting improves alignment for the logistic regression but does not consistently enhance performance for XGBoost, suggesting that LLMs struggle to recover nonlinear, interaction-driven reasoning from prompt cues alone. Overall, these results indicate that LLMs are best positioned as narrative interfaces grounded in auditable attribution rankings, rather than as substitutes for post-hoc explainers in credit lending model risk management. This distinction underscores the importance of maintaining formal attribution methods as the primary source of explanatory accountability.

The remainder of the paper is organized as follows. Section 2 reviews the related literature on explainable AI and the use of LLMs in financial applications. Section 3 describes the experimental design, including data processing, baseline model training, prompt engineering strategies, and evaluation metrics. Section 4 presents the empirical results for both research questions. Section 5 concludes with a discussion of implications and directions for future research.

## 2 Literature Review

Credit scoring has historically relied on transparent models such as logistic regression and rule-based decision trees due to their interpretability, ease of validation, and compatibility with regulatory requirements (Thomas, [2000](https://arxiv.org/html/2602.18895v1#bib.bib23 "A survey of credit and behavioural scoring: forecasting financial risk of lending to consumers")). In recent years, machine learning models—including support vector machines (SVMs) and neural networks (NNs)—have been increasingly applied to credit risk modeling because of their ability to capture nonlinear relationships and achieve superior predictive performance (Baesens et al., [2003](https://arxiv.org/html/2602.18895v1#bib.bib25 "Benchmarking state-of-the-art classification algorithms for credit scoring"); Lessmann et al., [2015](https://arxiv.org/html/2602.18895v1#bib.bib24 "Benchmarking state-of-the-art classification algorithms for credit scoring: an update of research")). Despite their predictive advantages, the complexity and black-box nature of these models introduce substantial challenges for interpretability, validation, and regulatory compliance.

To address these challenges, post-hoc explainability AI (XAI) methods such as SHAP and LIME have been widely adopted to interpret black-box credit models and generate feature-based explanations for regulatory and adverse action notices (Misheva et al., [2021](https://arxiv.org/html/2602.18895v1#bib.bib26 "Explainable ai in credit risk management")). By estimating marginal feature contributions, those methods provide a practical mechanism for attributing predictions to input variables. However, their results are primarily numerical—such as feature importance scores or contribution values— and may lack semantic clarity. As a result, they can be difficult for non-technical stakeholders to interpret and may not fully support human-centered decision processes (Tambwekar and Gombolay, [2023](https://arxiv.org/html/2602.18895v1#bib.bib27 "Towards reconciling usability and usefulness of explainable ai methodologies")).

Recent advances in large language models (LLMs) have demonstrated strong capabilities in generating coherent, context-aware natural language explanations across high-stakes domains, including healthcare, education, and legal applications (Cascella et al., [2023](https://arxiv.org/html/2602.18895v1#bib.bib28 "Evaluating the feasibility of chatgpt in healthcare: an analysis of multiple clinical and research scenarios"); Han et al., [2024](https://arxiv.org/html/2602.18895v1#bib.bib29 "LLM-as-a-tutor in efl writing education: focusing on evaluation of student-llm interaction"); Siino et al., [2025](https://arxiv.org/html/2602.18895v1#bib.bib30 "Exploring llms applications in law: a literature review on current legal nlp approaches")). This linguistic and reasoning capability suggests that LLMs could potentially serve as explanatory interfaces between complex machine learning models and non-technical stakeholders, enhancing communicative effectiveness and transparency.

Kroeger et al. (Kroeger et al., [2023](https://arxiv.org/html/2602.18895v1#bib.bib31 "Are large language models post hoc explainers?")) examined the feasibility of using LLMs as post-hoc explainers by evaluating their ability to reproduce feature-importance rankings. However, their experimental design relied on synthetic feature representations lacking domain-specific semantic content, thereby primarily assessing symbolic ranking reproduction rather than explanations grounded in real-world decision contexts. Mohanty et al. (Mohanty et al., [2025](https://arxiv.org/html/2602.18895v1#bib.bib32 "IMPACT: an interactive multi-disease prevention and counterfactual treatment system using explainable ai and a multimodal llm")) further demonstrated that LLMs, when guided by few-shot prompting, can reproduce attribution patterns similar to classical post-hoc methods in a multi-disease prevention setting.

Despite these emerging findings, the literature does not yet provide a systematic understanding of how LLM-based explanations behave in the credit risk domain. In particular, it remains unclear whether LLMs can reliably preserve structured feature-importance rankings when reference explanations are explicitly provided, or whether they can autonomously infer such structures in the absence of reference attributions. These two settings correspond to distinct deployment scenarios for LLM-based explanation systems in credit risk management and directly motivate our investigation of LLMs as translators versus autonomous explainers.

## 3 Methods

![Refer to caption](workflow.png)


Figure 1: Overall framework of the proposed LLM-based attribution study

Figure [1](https://arxiv.org/html/2602.18895v1#S3.F1 "Figure 1 ‣ 3 Methods ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?") summarizes the overall framework of this study. We first train two baseline credit risk models—logistic regression and XGBoost—and derive model-grounded reference attributions (logistic regression coefficient-based contributions and SHAP values for XGBoost), which are converted into feature-importance rankings. These reference rankings and/or model outputs are then provided to LLMs to address RQ1 and RQ2.

For RQ1, LLMs are evaluated as translators conditioned on the reference ranking. For RQ2, we evaluate both zero-shot and few-shot prompting configurations. In both settings, LLM-generated feature rankings are subsequently compared with the reference rankings to quantify alignment and consistency. The following subsections describe each step in detail.

### 3.1 Data Structure and Cleaning

This study utilizes a proprietary consumer loan dataset issued by LendingClub (Devlin, [2016](https://arxiv.org/html/2602.18895v1#bib.bib33 "Lending club loan data 2007–11")), which contains anonymized information on borrower characteristics, loan contract terms,credit bureau attributes, and loan performance outcomes for loans originated between 2007 and 2011.

To ensure suitability for predictive modeling and explainability analysis, a systematic data pre-processing pipeline was applied. First, variables with all missing values or zero variance are excluded, as they provide no discriminatory power for modeling. Second, categorical features exhibiting sparse or excessively granular levels are consolidated into economically conceptual coherent groups based on their underlying semantic interpretation, thereby reducing dimensionality while preserving information content. Third, features that were either unrelated to loan performance or recorded after loan origination are dropped to prevent data leakage and ensure temporal validity of the predictive model.

Categorical variables were also encoded according to their measurement scales. Ordinal categorical variables, such as credit grade, are mapped to integer encoding that preserve their inherent ranking structure and economic ordering. Nominal categorical variables are transformed through one-hot encoding to avoid imposing artificial ordinal relationships among category levels. These encoding strategies support both predictive performance and the interpretability of subsequent post-hoc explanations.

Following these pre-processing procedures, the final modeling dataset comprises 39,239 loan applicants with 24 independent features. The target variable is a binary indicator of loan outcome, where loans classified as Charged Off are labeled as 1 and loans classified as Fully Paid are labeled as 0.

For notational clarity in subsequent sections, we formalize the problem setup as follow: Let {(xi,yi)}i=1N\{(x\_{i},y\_{i})\}\_{i=1}^{N} denote the complete loan dataset, where N=39,239N=39,239, input vector xi∈ℝmx\_{i}\in\mathbb{R}^{m} with m=24m=24 represents the independent feature vector for loan ii, and yi∈{0,1}y\_{i}\in\{0,1\} is the corresponding binary outcome. A predictive model f​(⋅)f(\cdot) maps the independent feature vector of each loan to a probability of default: pi=f​(xi)p\_{i}=f(x\_{i}).

### 3.2 Baseline Prediction Model

The predictive task is formulated as a binary classification problem, in which the model f​(⋅)f(\cdot) estimates the probability that a loan will default. To provide prediction backbone for subsequent post-hoc explainability analysis, we train two representative credit risk models: logistic regression and eXtreme Gradient Boosting (XGBoost) (Chen, [2016](https://arxiv.org/html/2602.18895v1#bib.bib2 "XGBoost: a scalable tree boosting system")).

Logistic regression serves as an inherently interpretable baseline model, offering coefficient-based attributions that directly reflect linear feature contributions. In contrast, XGBoost represents a state-of-the-art tree-based ensemble method capable of capturing nonlinear relationships and complex feature interactions, and is widely adopted in industry practice. The inclusion of both models enables a comparative evaluation of LLM behavior across linear and nonlinear predictive structures.

Following data pre-processing and variable selection, the logistic regression model was calibrated by tuning of the L2 regularization hyperparameter λ\lambda. The area under the Precision-Recall Curve (PR-AUC) (Davis and Goadrich, [2006](https://arxiv.org/html/2602.18895v1#bib.bib15 "The relationship between precision-recall and roc curves")) was adopted as the optimization criterion to better capture model performance on the minority class under severe class imbalance inherent in the dataset. For the XGBoost model, hyperparameter tuning was performed using stratified five-fold cross-validation, with PR-AUC serving as the evaluation metric. This evaluation choice ensures consistent performance assessment across both linear and nonlinear modeling frameworks.

All models were trained on the preprocessed dataset described in Section [3.1](https://arxiv.org/html/2602.18895v1#S3.SS1 "3.1 Data Structure and Cleaning ‣ 3 Methods ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?"). The data were randomly partitioned into training and test subsets using a 70:3070:30 split ratio, stratified by the target variable to maintain class distribution. Model fitting was performed exclusively on the training subset, while all subsequent explainability analyses were conducted on the held-out test set to ensure that explanations reflect model behavior on previously unseen observations and avoid overfitting-induced bias in attribution patterns.

Model performance was evaluated using three complementary metrics, each capturing distinct aspects of predictive quality under imbalanced classification settings.

* 1.

  PR-AUC: The area under the Precision–Recall curve evaluates the model’s ability to correctly rank minority-class observations by capturing the precision–recall trade-off across all decision thresholds. Unlike the area under the Receiver Operating Characteristic curve (AUROC), PR-AUC is more informative under class imbalance, as it explicitly emphasizes performance on the positive (default) class. Accordingly, PR-AUC is adopted as the primary metric for assessing discriminatory performance in this study.
* 2.

  Macro-averaged F1-score (Sokolova and Lapalme, [2009](https://arxiv.org/html/2602.18895v1#bib.bib16 "A systematic analysis of performance measures for classification tasks")): Computed as the unweighted average of class-specific F1-scores, this metric assigns equal importance to both majority and minority classes. It provides a balanced evaluation of classification performance and mitigates the dominance of the majority class in aggregate accuracy measures.
* 3.

  Kolmogorov–Smirnov (KS) Statistic (Thomas et al., [2017](https://arxiv.org/html/2602.18895v1#bib.bib17 "Credit scoring and its applications")): The KS statistic measures the maximum vertical distance between the cumulative distribution functions of predicted risk scores for the positive and negative classes. Widely used in credit risk modeling, it quantifies the model’s discriminatory power. Higher KS values indicate stronger separation between classes and thus superior model discrimination.

### 3.3 Reference Explainability Methods

Given the distinct characteristics of logistic regression and XGBoost, we adopt model-specific explanation approaches to construct benchmark references for comparison with LLM-generated outputs.

For the logistic regression model specified in Equation [1](https://arxiv.org/html/2602.18895v1#S3.E1 "In 3.3 Reference Explainability Methods ‣ 3 Methods ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?"), the regression coefficients β\beta provide a natural and interpretable measure of feature influence under a linear log-odds specification. Instance-specific feature contribution is quantified by the product βj​xi​j\beta\_{j}x\_{ij}, which combines the estimated coefficient (βj\beta\_{j}) with the corresponding feature value (xi​jx\_{ij}) for each observation ii. The sign of this product indicates the directional effect of the feature on predicted default risk, where positive value increases the log-odds of default and negative value decreases it. The magnitude reflects the strength of the contribution to the linear predictor. The overall prediction is obtained by summing these contributions across all mm features and adding the intercept term. This additive decomposition provides a complete and exact attribution of the model’s prediction to individual features.

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡(1−pipi)=β0+∑j=1mβj​xi​j\log\!\left(\frac{1-p\_{i}}{p\_{i}}\right)=\beta\_{0}+\sum\_{j=1}^{m}\beta\_{j}x\_{ij} |  | (1) |

For the XGBoost model, we employ SHAP to decompose model output into feature-level contributions for each instance. SHAP is a unified framework grounded in cooperative game theory that assigns each feature an importance value given a particular prediction. While the SHAP methodology details is beyond the scope of this paper, we provide the key formulation below for completeness.

For each instance ii, we define the SHAP attribution vector ϕi=(ϕi​1,…,ϕi​m)\boldsymbol{\phi}\_{i}=(\phi\_{i1},\ldots,\phi\_{im}), where ϕi​j\phi\_{ij} represents the signed contribution of feature jj to the model output for observation ii, relative to a baseline ϕ0\phi\_{0}. SHAP satisfies an additive decomposition of the model output,

|  |  |  |  |
| --- | --- | --- | --- |
|  | f​(𝐱i)=ϕ0+∑j=1mϕi​j,f(\mathbf{x}\_{i})=\phi\_{0}+\sum\_{j=1}^{m}\phi\_{ij}, |  | (2) |

where f​(𝐱i)f(\mathbf{x}\_{i}) denotes the model output. Similar to the logistic regression, the sign of ϕi​j\phi\_{ij} indicates whether feature jj increases or decreases the predicted default risk relative to the baseline expectation, while its magnitude quantifies the strength of that contribution.

Both βj​xi​j\beta\_{j}x\_{ij} and ϕi​j\phi\_{ij} are computed in the encoded feature space used by the predictive models. To ensure interpretability at the original feature level, we subsequently aggregate attributions for each categorical feature by grouping its one-hot components. For a categorical feature gg with one-hot encoded components indexed by 𝒥​(g)\mathcal{J}(g), the grouped local contribution is defined as ∑j∈𝒥​(g)ϕi​j​ or ​∑j∈𝒥​(g)βj​xi​j\sum\_{j\in\mathcal{J}(g)}\phi\_{ij}\text{ or }\sum\_{j\in\mathcal{J}(g)}\beta\_{j}x\_{ij}, dependent on the model algorithm. This aggregation ensures that feature importance rankings are evaluated at the semantically meaningful variable level rather than at the level of encoded dummy variables.

### 3.4 LLM-based Post-hoc Explainability

In-context learning (ICL) (Brown et al., [2020](https://arxiv.org/html/2602.18895v1#bib.bib3 "Language models are few-shot learners")) refers to the ability of large language models to perform tasks by conditioning on task instructions or demonstration examples provided directly within the prompt, without requiring parameter updates or additional fine-tuning. This capability enables LLMs to generate explanations under different prompting strategies, including zero-shot settings with task instructions only and few-shot settings augmented with demonstration examples.

To address the two research questions and to evaluate LLM performance under different prompting configurations, we employ three widely used commercial LLMs: GPT-4-turbo, Claude-Sonnet-4.5, and Gemini-2.0-Flash. All models are accessed via the LiteLLM framework (version 1.81.3), which provides a unified interface for model invocation and experiment management.To enhance reproducibility and reduce stochastic variation across runs, the temperature parameter is fixed at 0 for all models. This setting allows controlled sampling while maintaining consistency across experimental conditions.

All experiments are conducted in Python (version 3.12.12) using standard scientific computing libraries, including pandas (2.2.2), NumPy (2.0.2), scikit-learn (1.6.1), SHAP (0.50.0), XGBoost (3.1.3), and Optuna (4.6.0), within the Google Colab environment.The prompt templates used in all experiments are available from the corresponding author upon request.

#### 3.4.1 RQ1: LLM as Translator

RQ1 evaluates whether LLMs can generate faithful post-hoc explanations when instance-level feature attributions are explicitly provided within the prompt. Importantly, RQ1 does not assess the model’s ability to independently infer feature importance from raw input variables. Rather, it isolates a more fundamental capability that is essential for credit risk applications: the ability of an LLM to faithfully preserve and reproduce a specified attribution structure under conditions of minimal ambiguity.
This controlled setting enables a direct assessment of structural fidelity between the reference attributions and the LLM-generated explanations. The experimental procedure is formalized as follows.

Algorithm for RQ1: LLM as Translator
For each instance (xi,yi)(x\_{i},y\_{i}) and a trained baseline predictive model f​(⋅)f(\cdot), we implement the following procedure:

1.

Step 1: Instance-Level Information Preparation:
For each instance ii, we construct a structured input consisting of the feature vector 𝐱i\mathbf{x}\_{i}, the observed outcome yiy\_{i}, the predicted probability pi=f​(𝐱i)p\_{i}=f(\mathbf{x}\_{i}), and a reference ranked feature set 𝒯i\mathcal{T}\_{i} derived from the baseline model’s explanation mechanism. The set 𝒯i\mathcal{T}\_{i} represents the model-grounded attribution structure that the LLM is expected to reproduce.
2.

Step 2 Prompt Construction with Strict Output Constraints: We design a structured prompting protocol that explicitly constrains the LLM’s output format. In particular, the prompt instructs the LLM to return a ranked list of features drawn from the original input space. No additional inferred feature or external knowledge are permitted, ensuring that the task is framed as controlled reproduction rather than independent feature inference.
3.

Step 3 LLM Invocation and Explanation Generation: Using the constructed prompt, we query the LLM to generate an instance-specific ranked feature 𝒯i^\hat{\mathcal{T}\_{i}} for each instance. This procedure is repeated for each of the three LLMs under identical experimental conditions to enable consistent comparison of reproduction fidelity across models.
4.

Step 4 Instance-level Alignment Evaluation: The LLM-generated ranking 𝒯i^\hat{\mathcal{T}\_{i}} is compared against the reference set 𝒯i\mathcal{T}\_{i} at multiple top-KK cutoffs. Ranking-based alignment metrics, described below, are used to quantify how accurately the LLM preserves both the feature set and relative importance ordering provided in the prompt.

This algorithm evaluates whether an LLM can faithfully reproduce a reference explanation when the attribution structure is explicitly supplied and sources of ambiguity are minimized. T

To quantify LLM performance under this controlled setting, we consider two complementary metrics:

* 1.

  Top-KK Feature Overlap: This metric measures the proportion of features shared between the LLM-generated and reference top-KK feature sets, as formalized in formula [3](https://arxiv.org/html/2602.18895v1#S3.E3 "In item 1 ‣ 3.4.1 RQ1: LLM as Translator ‣ 3.4 LLM-based Post-hoc Explainability ‣ 3 Methods ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?"). It captures whether the same top-K features are identified, regardless of their relative ordering.

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Overlap​@​Ki=|T^i(K)∩Ti(K)|K\mathrm{Overlap@K}\_{i}=\frac{\left|\hat{T}\_{i}^{(K)}\cap T\_{i}^{(K)}\right|}{K} |  | (3) |

  where Ti(K)T\_{i}^{(K)} denotes the top-KK features from the reference and T^i(K)\hat{T}\_{i}^{(K)} is the corresponding LLM-generated set for the instance ii.
* 2.

  Kendall’s τ\tau coefficient (Kendall, [1938](https://arxiv.org/html/2602.18895v1#bib.bib14 "A new measure of rank correlation")): measures the degree of pairwise concordance between the reference ranking 𝒯i^\hat{\mathcal{T}\_{i}} and the LLM-generated ranking 𝒯i\mathcal{T}\_{i}. Unlike the overlap metric, Kendall’s τ\tau is sensitive to the relative ordering of features and therefore captures fine-grained ranking consistency beyond mere set membership agreement.

#### 3.4.2 RQ2 LLM as Autonomous Explainer

RQ2 examines whether LLMs can autonomously generate meaningful feature-importance rankings in the absence of explicit reference guidance. This capability is particularly relevant for practical deployment scenarios in which LLMs function as standalone explanation tools or where model-based attribution rankings are not directly accessible.

In addition, RQ2 evaluates the impact of in-context learning (ICL) strategies by comparing the quality of LLM-generated explanations under zero-shot and few-shot prompting configurations. This analysis assesses whether demonstration-based prompting improves alignment with model-grounded explanations when structural guidance is not explicitly provided.

Algorithm for RQ2: LLM as Autonomous Explainer
For each instance (xi,yi)(x\_{i},y\_{i}) and a trained baseline predictive model f​(⋅)f(\cdot), we implement the following procedure:

1.

Step 1: Instance-Level Information Preparation:
For each instance ii, we construct a structured input consisting of the feature vector 𝐱i\mathbf{x}\_{i}, the observed outcome yiy\_{i}, and the predicted probability pi=f​(𝐱i)p\_{i}=f(\mathbf{x}\_{i}). Unlike RQ1, no reference attribution ranking is provided at this stage.
2.

Step 2 Prompt Construction with ICL Strategy Variation: Following the output format constraints established in RQ1, we construct prompts under two distinct in-context learning configurations:


(a)

Zero-shot Setting: The prompt contains only the instance information and task instructions, without any demonstration examples.
(b)

Few-shot Setting: Besides the instance information and task instructions, the prompt also includes two demonstration examples along with their reference feature rankings derived from the baseline model’s explanation mechanism.
3.

Step 3 LLM Invocation and Ranking Generation: Using the constructed prompt, we query the LLM to generate a ranked feature 𝒯i^\hat{\mathcal{T}\_{i}} for each instance. The process is repeated across all three LLMs under zero-shot and few-shot configurations.
4.

Step 4 Instance-level Alignment Evaluation: The LLM-generated ranking 𝒯i^\hat{\mathcal{T}\_{i}} is compared against the reference ranking 𝒯i\mathcal{T}\_{i} at multiple top-KK cutoffs using the same metrics described in Section [3.4.1](https://arxiv.org/html/2602.18895v1#S3.SS4.SSS1 "3.4.1 RQ1: LLM as Translator ‣ 3.4 LLM-based Post-hoc Explainability ‣ 3 Methods ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?")

This procedure evaluates whether LLMs can independently generate feature-importance rankings that align with model-grounded reference explanations in the absence of explicit attribution guidance. By systematically comparing zero-shot and few-shot configurations, we assess the extent to which demonstration examples enhance the LLM’s capacity to identify relevant features and approximate the underlying importance structure of the predictive model.

## 4 Results

### 4.1 Baseline Model Performance

To evaluate the predictive performance of the baseline models, we consider several key metrics, including PR-AUC, macro-averaged F1-score, and KS statistics as described in Section [3.2](https://arxiv.org/html/2602.18895v1#S3.SS2 "3.2 Baseline Prediction Model ‣ 3 Methods ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?"). Table [1](https://arxiv.org/html/2602.18895v1#S4.T1 "Table 1 ‣ 4.1 Baseline Model Performance ‣ 4 Results ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?") below, reports the validation sample performance of the logistic and XGBoost models.

The logistic regression model achieves a PR-AUC of 0.270.27 and a KS statistics of 28.9%28.9\%, indicating limited discriminatory power in separating defaulted from paid-off accounts. In contrast, the XGBoost model demonstrates substantially stronger predictive performance, with a higher PR-AUC of 0.38 and a higher KS statistics of 40.4%40.4\%, reflecting improved ranking and class separation capabilities.

Table 1: Key Metrics of Logistic and XGBoost Classification

| Model | PR-AUC | Macro-averaged F1-score | KS |
| --- | --- | --- | --- |
| Logistic | 0.27 | 0.46 | 28.79 |
| XGBoost | 0.38 | 0.63 | 40.4 |

### 4.2 LLM Performance

#### 4.2.1 RQ1: LLM as Translator

We evaluate RQ1 to examine whether LLMs can faithfully translate instance-level reference explanations 𝒯i\mathcal{T}\_{i} when attribution information is explicitly provided and prompt ambiguity is minimized.
Due to computational and budgetary constraints, the evaluation is conducted on a subset of 200 observations randomly selected from the test set.

To ensure balanced representation across prediction outcomes, the sample is stratified to include 50 instances from each prediction category: true positives, true negatives, false positives, and false negatives. This design enables a comprehensive assessment of explanation fidelity across correctly and incorrectly classified cases.

We observe that the Top-KK feature overlap (Overlap​@​Ki\mathrm{Overlap@K}\_{i}) equals one for the vast majority of instances, regardless of the choice of baseline model or LLM model. This indicates that LLM-generated explanations exhibit substantial alignment with the reference rankings in terms of identifying the top-KK influential features.

Given that the mean and median of Overlap​@​K\mathrm{Overlap@K} is near 1, we refrain from reporting summary measures, and focus on instances where perfect overlap is not achieved, analyzing their frequency and severity. As shown in Table [2](https://arxiv.org/html/2602.18895v1#S4.T2 "Table 2 ‣ 4.2.1 RQ1: LLM as Translator ‣ 4.2 LLM Performance ‣ 4 Results ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?"), only four instances exhibit Overlap​@​K<1\mathrm{Overlap@K}<1 across all experimental settings. Considering that the analysis is conducted on 200 samples at each LLM model, these deviations are rare and also limited in magnitude, suggesting that LLM failures in reproducing the reference feature set under the controlled setting are infrequent.

Table 2: Instance with Non-perfect Overlap​@​K\mathrm{Overlap@K}

| Base Model | LLM Model | Metric | Number | Mean (min,max) |
| --- | --- | --- | --- | --- |
| Logistic | gpt-4-turbo | Overlap​@​K15\mathrm{Overlap@K}\_{15} | 1 | 0.93 (0.93,0.93) |
| Logistic | gpt-4-turbo | Overlap​@​K20\mathrm{Overlap@K}\_{20} | 1 | 0.95 (0.95,0.95) |
| XGBoost | claude-sonnet-4 | Overlap​@​K5\mathrm{Overlap@K}\_{5} | 1 | 0.8 (0.8,0.8) |
| XGBoost | claude-sonnet-4 | Overlap​@​K10\mathrm{Overlap@K}\_{10} | 2 | 0.9 (0.9,0.9) |

As KK increases, discrepancies in the relative ordering between LLM-generated and reference rankings become more pronounced, as reported in Table [3](https://arxiv.org/html/2602.18895v1#S4.T3 "Table 3 ‣ 4.2.1 RQ1: LLM as Translator ‣ 4.2 LLM Performance ‣ 4 Results ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?"). The table lists both the number of instances and the corresponding range of Kendall’s τ\tau coefficient for which the metric is less than one under each setting. The trend indicates reduced consistency in reproducing finer-grained importance structures beyond the top features. We further observe heterogeneity in ranking stability across different LLM models. In particular, model claude-sonnet-4 exhibits less stable ranking outputs compared with the other models, as reflected by a larger number of instances with imperfect Kendall’s τ\tau in both Logistic Model and XGBoost model.

Table 3: Number (mean) of Non-perfect Kendall’s τ\tau coefficient

| Base Model | LLM Model | TopK5\mathrm{TopK}\_{5} | TopK10\mathrm{TopK}\_{10} | TopK15\mathrm{TopK}\_{15} | TopK20\mathrm{TopK}\_{20} |
| --- | --- | --- | --- | --- | --- |
| Logistic | gpt-4-turbo | 0 | 0 | 1 (0.98) | 3 (0.96) |
| claude-sonnet-4 | 2 (0.8) | 5(0.95) | 7 (0.98) | 9(0.98) |
| gemini-2.0-flash | 0 | 0 | 0 | 1 (0.98) |
| XGBoost | gpt-4-turbo | 0 | 1 (0.95) | 2(0.96) | 4(0.97) |
| claude-sonnet-4 | 0 | 1(0.95) | 3 (0.98) | 3 (0.98) |
| gemini-2.0-flash | 0 | 0 | 1(0.98) | 1(0.98) |

Overall, these findings suggest that LLMs are capable of acting as effective translators in this highly controlled prompting setting, particularly when explanations are restricted to a small number of key features, such as the top four factors commonly considered in adverse action explanations.

#### 4.2.2 RQ2

Similarly, RQ2 is evaluated on the same subset of 200 observations to ensure comparability across experimental settings. This analysis examines whether LLMs can function as substitutes for model-based attribution methods (e.g., SHAP or coefficient-based contributions in logistic regression) when generating feature-importance rankings autonomously.

Due to token-length constraints imposed by the LLM interfaces, the generated explanations are restricted to the top 10 ranked features. Accordingly, alignment evaluation focuses on the Top-10 feature set for each instance.

Table [4](https://arxiv.org/html/2602.18895v1#S4.T4 "Table 4 ‣ 4.2.2 RQ2 ‣ 4.2 LLM Performance ‣ 4 Results ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?") and Table [5](https://arxiv.org/html/2602.18895v1#S4.T5 "Table 5 ‣ 4.2.2 RQ2 ‣ 4.2 LLM Performance ‣ 4 Results ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?") report the Overlap​@​K\mathrm{Overlap@K} results, including the minimum, maximum, and median values at K∈3,5,10K\in{3,5,10} under both zero-shot and few-shot prompting schemes for the logistic regression and XGBoost models. Across all combinations of LLMs and prompt templates, the average Top-KK overlap remains relatively low.

For example, among the 200 evaluation instances, GPT-4-turbo under the zero-shot setting achieves a maximum overlap of only one feature when compared with the logistic regression reference explanations. Although the absolute number of overlapping features increases as KK increases, the corresponding overlap proportion remains modest. This pattern suggests a systematic divergence between LLM-generated rankings and model-based attributions.

One plausible explanation is the fundamental difference in how feature importance is derived. Post-hoc explainers compute attributions directly from the internal structure of the predictive model—either through coefficient-based linear decomposition or SHAP-based additive contributions. In contrast, LLMs approximate feature importance based solely on prompt-level information and learned statistical associations from pretraining. Without access to model parameters or the exact decision structure, LLM-generated rankings rely on surface-level correlations rather than model-grounded reasoning, limiting their ability to faithfully recover the true attribution structure.

In the logistic regression setting, few-shot prompting generally leads to higher overlap compared with zero-shot prompting across all three LLMs. However, the magnitude of improvement for Gemini-2.0 is smaller relative to the other models, which may be attributable to the lightweight variant employed in our experiments and its comparatively constrained reasoning capacity.

In contrast, for the XGBoost model, few-shot prompting does not consistently improve performance over the zero-shot configuration. One possible explanation is the greater structural complexity of XGBoost as a tree-based ensemble model. Even when exemplar contexts include SHAP-based attribution inputs, there is limited evidence that LLMs are able to internalize or reconstruct the model-specific reasoning mechanism implied by such non-linear and interaction-driven structures.

Table 4: Mean (min,max) of Overlap​@​K\mathrm{Overlap@K} for Logistic Model at different KK

| Logistic Model | | Overlap​@​K3\mathrm{Overlap@K}\_{3} | Overlap​@​K5\mathrm{Overlap@K}\_{5} | Overlap​@​K10\mathrm{Overlap@K}\_{10} |
| --- | --- | --- | --- | --- |
| Zero-shot | gpt-4-turbo | 0.14 (0,0.33) | 0.19 (0,0.6) | 0.44 (0.2,0.7) |
|  | claude-sonnet-4 | 0.11 (0,0.67) | 0.18 (0, 0.6) | 0.41 (0, 0.7) |
|  | gemini-2.0-flash | 0.16 (0,0.33) | 0.29 (0,0.6) | 0.48 (0.2,0.7) |
| Few-shot | gpt-4-turbo | 0.39 (0, 1) | 0.51 (0, 1) | 0.58 (0.2, 0.9) |
|  | claude-sonnet-4 | 0.46 (0,1) | 0.65 (0, 1) | 0.68 (0.4, 0.9) |
|  | gemini-2.0-flash | 0.18 (0,0.67) | 0.47 (0, 0.8) | 0.6 (0.3, 0.8) |




Table 5: Mean (min,max) of Overlap​@​K\mathrm{Overlap@K} for XgBoost Model at different KK

| XgBoost Model | | Overlap​@​K3\mathrm{Overlap@K}\_{3} | Overlap​@​K5\mathrm{Overlap@K}\_{5} | Overlap​@​K10\mathrm{Overlap@K}\_{10} |
| --- | --- | --- | --- | --- |
| Zero-shot | gpt-4-turbo | 0.23 (0,0.67) | 0.26 (0,0.6) | 0.39 (0.2,0.7) |
|  | claude-sonnet-4 | 0.23 (0,0.67) | 0.28 (0, 0.6) | 0.45 (0, 0.6) |
|  | gemini-2.0-flash | 0.22 (0,0.37) | 0.28 (0,0.6) | 0.46 (0,0.8) |
| Few-shot | gpt-4-turbo | 0.19 (0, 0.67) | 0.19 (0, 0.6) | 0.31 (0.1, 0.6) |
|  | claude-sonnet-4 | 0.22 (0,0.33) | 0.28 (0, 0.4) | 0.45 (0.2, 0.7) |
|  | gemini-2.0-flash | 0.21 (0,0.67) | 0.21 (0, 0.6) | 0.39 (0.1, 0.7) |

## 5 Conclusions

This study evaluates whether large language models (LLMs) can serve as post-hoc explainability tools for credit risk models, addressing two research questions: whether LLMs can faithfully reproduce feature-importance rankings when reference attributions are provided (RQ1), and whether they can autonomously generate aligned feature-importance rankings without access to such references (RQ2). Using logistic regression and XGBoost as baseline classifiers and comparing LLM-generated outputs against coefficient-based and SHAP-based reference rankings, we assess ranking alignment through Top-KK feature overlap and Kendall’s τ\tau on a balanced subset of 200 test instances.

Our results indicate that LLMs can be reliable translators under a controlled prompting design. When the reference ranking is supplied and the output is format-constrained, LLM-generated explanations always preserve the correct top-KK feature set, with only a handful of imperfect overlap cases. However, as the number of ranked features increases, relative ordering stability declines, reflected in a growing proportion of instances with imperfect Kendall’s τ\tau. This pattern suggests that LLMs are better suited to communicating a limited set of salient drivers—such as those typically included in adverse action notices—than at reproducing fine-grained rank positions across longer feature lists.

In contrast, our findings do not support the use of LLMs as autonomous explainers that can replace model-based post-hoc methods. Across both baseline models, Top-KK overlap between LLM-generated rankings and reference explanations remains generally low. This result reflects a fundamental distinction: post-hoc explainers derive attributions directly from the learned model structure, whereas LLMs infer importance from prompt-level statistical patterns without access to internal parameters or decision pathways. Few-shot prompting improves alignment in the logistic regression settings but does not consistently enhance performance for XGBoost, suggesting that demonstration examples alone are insufficient for LLMs to reconstruct nonlinear, interaction-driven reasoning inherent in tree-based ensembles.

Several limitations motivate future research. First, the evaluation is conducted on a relatively small sample due to computational cost constraints and focuses on rank alignment rather than user-centered outcomes. Second, we do not test robustness to prompt perturbations, distribution shifts, or adversarially crafted inputs, which are relevant in real credit operations. Third, while alignment with post-hoc attributions is informative, alignment does not guarantee that explanations are faithful, actionable, or legally sufficient—particularly for complex models such as XGBoost. Future research should therefore integrate human-in-the-loop evaluation frameworks, compliance-oriented assessment criteria, and systematic analyses of explanation stability and hallucination risk under real-world deployment constraints.

Taken together, our findings suggest a potential division of labor in high-stakes credit decision contexts. LLMs may be better positioned to restate established attribution rankings rather than to replace formal explanation algorithms. In practical model risk management workflows, LLMs could be deployed downstream of model-specific post-hoc explainers as a translation interface to render technical attributions into more accessible, human-readable narratives. Nevertheless, the faithfulness, stability, and regulatory adequacy of such translated explanations remain subject to further empirical validation before operational deployment can be justified.

## Acknowledgments

During the preparation of this manuscript, the authors used ChatGPT 5.2 for the purposes of manuscript polishing only. The authors have reviewed and edited the output and take full responsibility for the content of this publication.

## References

* E. C. O. Act (2018)
  Equal credit opportunity act.
  Women in the American Political System: An Encyclopedia of Women as Voters, Candidates, and Office Holders 2,  pp. 129.
  Cited by: [§1](https://arxiv.org/html/2602.18895v1#S1.p1.1 "1 Introduction ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?").
* F. C. R. Act (2009)
  Fair credit reporting act.
  Flood Disaster Protection Act and Financial Institute.
  Cited by: [§1](https://arxiv.org/html/2602.18895v1#S1.p1.1 "1 Introduction ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?").
* S. Aziz and M. Dowling (2019)
  Machine learning and ai for risk management.
  Disrupting finance,  pp. 33–50.
  Cited by: [§1](https://arxiv.org/html/2602.18895v1#S1.p1.1 "1 Introduction ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?").
* B. Baesens, T. Van Gestel, S. Viaene, M. Stepanova, J. Suykens, and J. Vanthienen (2003)
  Benchmarking state-of-the-art classification algorithms for credit scoring.
  Journal of the operational research society 54 (6),  pp. 627–635.
  Cited by: [§2](https://arxiv.org/html/2602.18895v1#S2.p1.1 "2 Literature Review ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?").
* T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell, et al. (2020)
  Language models are few-shot learners.
  Advances in neural information processing systems 33,  pp. 1877–1901.
  Cited by: [§3.4](https://arxiv.org/html/2602.18895v1#S3.SS4.p1.1 "3.4 LLM-based Post-hoc Explainability ‣ 3 Methods ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?").
* R. P. Bulyga, A. A. Sitnov, L. V. Kashirskaya, and I. V. Safonova (2020)
  Transparency of credit institutions.
  Entrepreneurship and Sustainability Issues 7 (4),  pp. 3158.
  Cited by: [§1](https://arxiv.org/html/2602.18895v1#S1.p1.1 "1 Introduction ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?").
* M. Cascella, J. Montomoli, V. Bellini, and E. Bignami (2023)
  Evaluating the feasibility of chatgpt in healthcare: an analysis of multiple clinical and research scenarios.
  Journal of medical systems 47 (1),  pp. 33.
  Cited by: [§2](https://arxiv.org/html/2602.18895v1#S2.p3.1 "2 Literature Review ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?").
* T. Chen (2016)
  XGBoost: a scalable tree boosting system.
  Cornell University.
  Cited by: [§3.2](https://arxiv.org/html/2602.18895v1#S3.SS2.p1.1 "3.2 Baseline Prediction Model ‣ 3 Methods ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?").
* J. Davis and M. Goadrich (2006)
  The relationship between precision-recall and roc curves.
  In Proceedings of the 23rd international conference on Machine learning,
   pp. 233–240.
  Cited by: [§3.2](https://arxiv.org/html/2602.18895v1#S3.SS2.p3.1 "3.2 Baseline Prediction Model ‣ 3 Methods ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?").
* J. Devlin (2016)
  Lending club loan data 2007–11.
  Note: data.worldData set
  External Links: [Link](https://data.world/jaypeedevlin/lending-club-loan-data-2007-11)
  Cited by: [§3.1](https://arxiv.org/html/2602.18895v1#S3.SS1.p1.1 "3.1 Data Structure and Cleaning ‣ 3 Methods ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?").
* J. N. Flagg and S. M. Hannon (2023)
  FinTech-issued personal loans in the us.
  Cited by: [§1](https://arxiv.org/html/2602.18895v1#S1.p1.1 "1 Introduction ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?").
* J. Han, H. Yoo, J. Myung, M. Kim, H. Lim, Y. Kim, T. Y. Lee, H. Hong, J. Kim, S. Ahn, et al. (2024)
  LLM-as-a-tutor in efl writing education: focusing on evaluation of student-llm interaction.
  In Proceedings of the 1st Workshop on Customizable NLP: Progress and Challenges in Customizing NLP for a Domain, Application, Group, or Individual (CustomNLP4U),
   pp. 284–293.
  Cited by: [§2](https://arxiv.org/html/2602.18895v1#S2.p3.1 "2 Literature Review ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?").
* C. Jennett, S. Brostoff, M. Malheiros, and M. A. Sasse (2012)
  Adding insult to injury: consumer experiences of being denied credit.
  International Journal of Consumer Studies 36 (5),  pp. 549–555.
  Cited by: [§1](https://arxiv.org/html/2602.18895v1#S1.p1.1 "1 Introduction ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?").
* M. G. Kendall (1938)
  A new measure of rank correlation.
  Biometrika 30 (1-2),  pp. 81–93.
  Cited by: [item 2](https://arxiv.org/html/2602.18895v1#S3.I3.i2.p1.4 "In 3.4.1 RQ1: LLM as Translator ‣ 3.4 LLM-based Post-hoc Explainability ‣ 3 Methods ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?").
* N. Kroeger, D. Ley, S. Krishna, C. Agarwal, and H. Lakkaraju (2023)
  Are large language models post hoc explainers?.
  Cited by: [§2](https://arxiv.org/html/2602.18895v1#S2.p4.1 "2 Literature Review ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?").
* S. Lessmann, B. Baesens, H. Seow, and L. C. Thomas (2015)
  Benchmarking state-of-the-art classification algorithms for credit scoring: an update of research.
  European journal of operational research 247 (1),  pp. 124–136.
  Cited by: [§2](https://arxiv.org/html/2602.18895v1#S2.p1.1 "2 Literature Review ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?").
* S. M. Lundberg and S. Lee (2017)
  A unified approach to interpreting model predictions.
  In Advances in Neural Information Processing Systems,
  Vol. 30,  pp. 4765–4774.
  Cited by: [§1](https://arxiv.org/html/2602.18895v1#S1.p2.1 "1 Introduction ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?").
* B. H. Misheva, J. Osterrieder, A. Hirsa, O. Kulkarni, and S. F. Lin (2021)
  Explainable ai in credit risk management.
  arXiv preprint arXiv:2103.00949.
  Cited by: [§2](https://arxiv.org/html/2602.18895v1#S2.p2.1 "2 Literature Review ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?").
* P. K. Mohanty, S. A. J. Francis, R. K. Barik, K. H. K. Reddy, D. S. Roy, and M. J. Saikia (2025)
  IMPACT: an interactive multi-disease prevention and counterfactual treatment system using explainable ai and a multimodal llm.
  PeerJ Computer Science 11,  pp. e2839.
  Cited by: [§2](https://arxiv.org/html/2602.18895v1#S2.p4.1 "2 Literature Review ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?").
* M. T. Ribeiro, S. Singh, and C. Guestrin (2016)
  ” Why should i trust you?” explaining the predictions of any classifier.
  In Proceedings of the 22nd ACM SIGKDD international conference on knowledge discovery and data mining,
   pp. 1135–1144.
  Cited by: [§1](https://arxiv.org/html/2602.18895v1#S1.p2.1 "1 Introduction ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?").
* M. Siino, M. Falco, D. Croce, and P. Rosso (2025)
  Exploring llms applications in law: a literature review on current legal nlp approaches.
  IEEE Access.
  Cited by: [§2](https://arxiv.org/html/2602.18895v1#S2.p3.1 "2 Literature Review ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?").
* M. Sokolova and G. Lapalme (2009)
  A systematic analysis of performance measures for classification tasks.
  Information processing & management 45 (4),  pp. 427–437.
  Cited by: [item 2](https://arxiv.org/html/2602.18895v1#S3.I1.i2.p1.1 "In 3.2 Baseline Prediction Model ‣ 3 Methods ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?").
* P. Tambwekar and M. Gombolay (2023)
  Towards reconciling usability and usefulness of explainable ai methodologies.
  arXiv preprint arXiv:2301.05347.
  Cited by: [§2](https://arxiv.org/html/2602.18895v1#S2.p2.1 "2 Literature Review ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?").
* L. C. Thomas (2000)
  A survey of credit and behavioural scoring: forecasting financial risk of lending to consumers.
  International journal of forecasting 16 (2),  pp. 149–172.
  Cited by: [§2](https://arxiv.org/html/2602.18895v1#S2.p1.1 "2 Literature Review ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?").
* L. Thomas, J. Crook, and D. Edelman (2017)
  Credit scoring and its applications.
   SIAM.
  Cited by: [item 3](https://arxiv.org/html/2602.18895v1#S3.I1.i3.p1.1 "In 3.2 Baseline Prediction Model ‣ 3 Methods ‣ Could Large Language Models work as Post-hoc Explainability Tools in Credit Risk Models?").