---
authors:
- Dmitry Lesnik
- Tobias Schaefer
doc_id: arxiv:2510.26627v1
family_id: arxiv:2510.26627
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Probabilistic Rule Models as Diagnostic Layers: Interpreting Structural Concept
  Drift in Post-Crisis Finance'
url_abs: http://arxiv.org/abs/2510.26627v1
url_html: https://arxiv.org/html/2510.26627v1
venue: arXiv q-fin
version: 1
year: 2025
---


Dmitry Lesnik
Stratyfy Inc., New York, New York, USA

Tobias Schäfer
Stratyfy Inc., New York, New York, USA
Department of Mathematics, College of Staten Island, Staten Island, NY, USA & Physics Program, CUNY Graduate Center, NY, USA

###### Abstract

Machine learning models used for high-stakes predictions in domains like credit risk face critical degradation due to concept drift, requiring robust and transparent adaptation mechanisms. We propose an architecture, where a dedicated correction layer is employed to efficiently capture systematic shifts in predictive scores when a model becomes outdated. The key element of this architecture is the design of a correction layer using Probabilistic Rule Models (PRMs) based on Markov Logic Networks, which guarantees intrinsic interpretability through symbolic, auditable rules. This structure transforms the correction layer from a simple scoring mechanism into a powerful diagnostic tool capable of isolating and explaining the fundamental changes in borrower riskiness. We illustrate this diagnostic capability using Fannie Mae mortgage data, demonstrating how the interpretable rules extracted by the correction layer successfully explain the structural impact of the 2008 financial crisis on specific population segments, providing essential insights for portfolio risk management and regulatory compliance.

## 1 Introduction

Machine learning models, particularly those used for high-stakes decisions in regulated domains like credit risk, rely on the core assumption that past data can predict future outcomes. However, this stability is often undermined by concept drift—a change in the statistical properties of the target variable due to shifts in economic, political, or market environments. When a model M1M\_{1} becomes obsolete, continuous monitoring and full model retraining are standard practice, resulting in a new model, M2M\_{2}. Crucially, generating M2M\_{2} alone fails to isolate and explain what specific systematic changes occurred in the underlying concept, a major deficiency in environments demanding regulatory auditability and policy insight.

To address this challenge, we introduce a structured architecture rooted in Transfer Learning principles. Transfer Learning is a well-established paradigm aimed at leveraging knowledge learned from a data source to facilitate efficient adaptation in a related, but different, target domain. This approach, for instance, is critically valuable for analyzing financial time series, which are inherently prone to concept drift that affects forecasting accuracy, making models quickly obsolete.

Imagine the base model, M1M\_{1} was trained at an initial time t1t\_{1} on source data (X1,y1)(X\_{1},y\_{1}) where X1X\_{1} is the input data and y1y\_{1} is the corresponding output. When the environment shifts and a new model M2M\_{2} trained on new data (X2,y2)(X\_{2},y\_{2}) at time t2>t1t\_{2}>t\_{1} is required, we construct a correction layer, CC. This model CC is designed to function as an efficient, specialized adaptation layer such that M1M\_{1} and CC applied together on X2X\_{2} replicate (or at least approximate) the outcomes y2y\_{2}. Figure [1](https://arxiv.org/html/2510.26627v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Probabilistic Rule Models as Diagnostic Layers: Interpreting Structural Concept Drift in Post-Crisis Finance") illustrates this basic setup, positioning the correction layer C as the bridge between models M1M\_{1} and M2M\_{2}.

![Refer to caption](flow_chart.png)

Figure 1: Basic idea of the correction layer as an intermediate model between models M1M\_{1} and M2M\_{2}.

The core utility of creating this intermediate model CC lies in its interpretability: by focusing CC on the residual difference between the pre-shift and post-shift models, we transform the correction layer into a powerful diagnostic tool. First, assuming an interpretable modeling approach, the differential model CC can yield transparent insight into the precise driving forces that contribute to the systematic differences between M1M\_{1} and M2M\_{2}. Second, these insights, together with the model CC, can be used for scenario analysis. The latter is in particular of interest in cases where a major structural event happened between the time t1t\_{1} and t2t\_{2}. In the example that we are going to discuss in this article, this major event will be the financial crisis of 2008.

The structure of the article is as follows. We first present background on probabilistic rule models (PRMs) and how they were built in the context of our application. Then we turn our attention to the specific construction of the correction layer based on PRMs. A main advantage of our approach lies in the fact that even in situations where the originating models M1M\_{1} and M2M\_{2} are black-box models, the fact that we are building the correction based on PRMs (which are entirely interpretable) allows us to draw insights into details of the difference of the two models. In the following section we demonstrate explicitly how to construct a PRM-based correction layer using Fannie Mae housing data [[1](https://arxiv.org/html/2510.26627v1#bib.bib1)]. The basic idea of this example is to consider a model M1M\_{1} trained on data from 2006 and then a model M2M\_{2} trained on data 2010. Given the financial crisis from 2008, we expect these models to be significantly different. Based on this, we construct a correction layer CC such that the model M1M\_{1} together with the correction layer approximates the model M2M\_{2}. We then analyze the performance of the correction layer and illustrate how to use the correction layer to gain insights into the changes that affected the creditworthiness of particular customer segments. A conclusion summarizes the main results of the paper.

## 2 Probabilistic Rule Models

### 2.1 Markov Logic and Rules

In this paper, we will base the construction of the correction layer, the intermediate model CC described above, using the framework of probabilistic rules. While, in principle, many different modeling approaches can be used for the construction of the correction layer, Probabilistic Rule Models (PRMs) have a great many advantages, particularly in environments requiring high transparency. PRMs are founded on
Markov Logic Networks (MLNs), which successfully combine the robustness of statistical learning (via Markov Random Fields) with the interpretability of logical rules. This architectural choice—grounded in Markov Logic [[2](https://arxiv.org/html/2510.26627v1#bib.bib2), [3](https://arxiv.org/html/2510.26627v1#bib.bib3)], Markov random fields [[4](https://arxiv.org/html/2510.26627v1#bib.bib4), [5](https://arxiv.org/html/2510.26627v1#bib.bib5), [6](https://arxiv.org/html/2510.26627v1#bib.bib6), [7](https://arxiv.org/html/2510.26627v1#bib.bib7)], and probabilistic graphical models [[8](https://arxiv.org/html/2510.26627v1#bib.bib8)] —enables PRMs to maintain strong predictive accuracy while offering intrinsic interpretability. This intrinsic quality, where the rules themselves constitute the explanation, is a key requirement for lenders in creditworthiness and finance. Unlike post-hoc explainability methods (e.g., LIME or SHAP), the PRM model provides direct, symbolic, and auditable logic, which is often considered indispensable for high-stakes decisions [[9](https://arxiv.org/html/2510.26627v1#bib.bib9)] where regulatory validation is paramount. We note that PRMs have also been successfully applied in other areas where interpretability is indispensable, for instance in healthcare [[10](https://arxiv.org/html/2510.26627v1#bib.bib10)].

In a nutshell, PRM consists of a set of logical formulas (rules) (R1,R2,…,Rm)(R\_{1},R\_{2},\ldots,R\_{m}) and corresponding weighting factors (ψ1,…,ψm)(\psi\_{1},\ldots,\psi\_{m}), defined on a set of binary variables (x1,x2,…,xn)(x\_{1},x\_{2},\ldots,x\_{n}). In our formulation, 0<ψi<10<\psi\_{i}<1, though other equivalent formulations are possible.

PRMs model a joined probability distribution over {xi}\{x\_{i}\} and, hence, belong to the class of generative models. Propositional Markov Logic
defines the probability of an evidence vector 𝐱\mathbf{x} as

|  |  |  |
| --- | --- | --- |
|  | P​(𝐱)=1Z​∏iϕi​(𝐱)P(\mathbf{x})=\frac{1}{Z}\,\prod\_{i}\phi\_{i}(\mathbf{x}) |  |

where ϕi\phi\_{i} are called potential functions, defined as

|  |  |  |
| --- | --- | --- |
|  | ϕi​(𝐱)={ψiif ​𝐱​ satisfies ​Ri,1−ψiif ​𝐱​ falsifies ​Ri.\phi\_{i}(\mathbf{x})=\begin{cases}\psi\_{i}&\text{if }\mathbf{x}\text{ satisfies }R\_{i},\\ 1-\psi\_{i}&\text{if }\mathbf{x}\text{ falsifies }R\_{i}.\end{cases} |  |

Here ZZ is the normalization factor:

|  |  |  |
| --- | --- | --- |
|  | Z=∑j∏iϕi​(𝐱j)Z=\sum\_{j}\prod\_{i}\phi\_{i}(\mathbf{x}^{j}) |  |

where the summation goes over all possible assignments of truth values.

Markov Logic framework can be applied for predictive analytics, such as credit risk or fraud predictions. In a typical machine learning task, all variables are split into a set of input (explanatory) variables {𝐞i}\{\mathbf{e}\_{i}\} and one or more target variables yy: 𝐱=(𝐞,y)\mathbf{x}=(\mathbf{e},y). In credit risk example, the target variable can be a default on a loan, and explanatory variables may include credit score, credit history, debt-to-income ratio, etc. The goal of predictive analytics is predicting probability of the target variable given the evidence of explanatory variables P​(y=1|𝐞)P(y=1|\mathbf{e}).

In lending, PRM usually consists of association rules of the form

|  |  |  |
| --- | --- | --- |
|  | Ri:(ek1∧ek2∧…)⇒ywith weight ψiR\_{i}:\quad(e\_{k\_{1}}\wedge e\_{k\_{2}}\wedge\ldots)\,\Rightarrow\,y\quad\text{with weight }\psi\_{i} |  |

To the set of association rules, we will be adding an “intercept” rule:

|  |  |  |
| --- | --- | --- |
|  | R0:ywith weight ​ψ0R\_{0}:\,\,y\quad\text{with weight }\psi\_{0} |  |

The intercept rule ensures the correct a-priori probability of the target variable (provided, the model is well-calibrated).

Most commonly, single-factor rules of the type x⇒yx\Rightarrow y, or two-factor rules (x1∧x2)⇒y(x\_{1}\wedge x\_{2})\Rightarrow y are used. We say that the rule is *shallow* if it has one factor in the premise.

We say that an association rule *triggers* if the l.h.s. (the premise of the logical implication) asserts true. Rules that do not trigger, also do not contribute to the probability of the target variable. Triggered rules with ψ>0.5\psi>0.5 increase the probability, whereas rules with ψ<0.5\psi<0.5 decrease the probability.

Often, in context of lending, it is common to use points notation instead of probabilistic weighting factors (for instance point-based scorecard approach [[11](https://arxiv.org/html/2510.26627v1#bib.bib11)]). For the sake of convenience, below instead of weighting factors ψ\psi we will be using points pp defined as

|  |  |  |
| --- | --- | --- |
|  | pi=−a​ln⁡(ψi1−ψi)\displaystyle p\_{i}=-a\,\ln\left(\frac{\psi\_{i}}{1-\psi\_{i}}\right) |  |

The negative sign is chosen such that points have a positive connotation. Positive points increase, whereas negative points decrease the repayment probability. Here aa is an arbitrary scaling factor.

The application of PRM in context of lending is illustrated schematically in figure [2](https://arxiv.org/html/2510.26627v1#S2.F2 "Figure 2 ‣ 2.1 Markov Logic and Rules ‣ 2 Probabilistic Rule Models ‣ Probabilistic Rule Models as Diagnostic Layers: Interpreting Structural Concept Drift in Post-Crisis Finance"). From the set of rules, using probabilistic logic, a score is computed. In particular, this score can be a probability of default (or repayment). Then, based on the chosen threshold, the lending decision can be made.

![Refer to caption](PRE_Diagram.jpg)

Figure 2: Basic structure of a particular implementation of a workflow with probabilistic rule model. In the case considered here, all rules are found from analyzing the given input data although, in general, rules can also be added by domain experts.

Let’s consider an example rule in PRM:

|  |  |  |
| --- | --- | --- |
|  | cscore <706⇒−1.98​ points\text{cscore }<706\qquad\Rightarrow\quad-1.98\,\text{ points} |  |

An intuitive interpretation of this rule is as follows: The rule indicates that if triggered (the variable “cscore” refers to the applicant’s FICO score), i.e., a customer satisfies the conditions in the premise “FICO score below 706”, the creditworthiness score will change by a certain level that is determined during calibration of the model and this level is characterized by the number of points added or subtracted.

Notice the difference between probabilistic rules framework and a typical rigid rules based decisioning algorithm (usually implemented with a business rule engine – BRE). A BRE-model consist of a set of the so-called knock-out logical rules: whenever a rule triggers, it demands the target variable to be 1, leading to an automatic rejection of a loan. In probabilistic framework, every rule contributes to the overall score, but every negative rule may be offset by other positive rules, leading to a much more accurate probability assessment, and more informed decision.

### 2.2 Implementation and Calibration

Building a PRM model includes the following steps:

1. 1.

   Data discretization. Since logic framework is only applicable to a binary data, all continuous variables have to be discretized. Sometimes binning of categorical variables is also required, especially for high cardinality variables. After discretization, one hot encoding can be used to convert the raw data into a binary format.

   The finer the discretization, the more accurate will be the PRM model. However, depending on the concrete application, it might be preferable to trade-off marginal accuracy increase in favour of model’s simplicity and interpretability.
2. 2.

   Rule mining. There is a variety of available techniques to find a set of predictive rules. One can use association rule mining [[12](https://arxiv.org/html/2510.26627v1#bib.bib12), [13](https://arxiv.org/html/2510.26627v1#bib.bib13), [14](https://arxiv.org/html/2510.26627v1#bib.bib14)], extract rules from a decision tree or construct rules manually based on domain expertize. This is where the approach demonstrates
   its great flexibility.
3. 3.

   Calibration. Once the rules are designed, the weighting factors (or points) have to be determined based on the historical training set, such that the model’s output can be interpreted as a real-world probability of the target variable. A PRM model can also be used as a regressor. In this case the target variable in the training set can be continuous, and the model output is interpreted as an estimate of the continuous variable, as opposed to the probability of a binary target variable.

   Model calibration can be performed using gradient descent in combination with an appropriate choice of objective function. In this research we used L-BFGS algorithm [[15](https://arxiv.org/html/2510.26627v1#bib.bib15)] for the gradient descent implementation. For the classification mode, we use a regularized cross-entropy objective, and for the regression mode we use the regularized least squares objective:

   |  |  |  |
   | --- | --- | --- |
   |  | L=∑(yi−y^i)2+λ​∑j=1m(ψj−0.5)2L=\sum(y\_{i}-\hat{y}\_{i})^{2}+\lambda\sum\_{j=1}^{m}(\psi\_{j}-0.5)^{2} |  |

   where y^i\hat{y}\_{i} are model predictions, and yiy\_{i} are the ground truth values.

We are now ready to discuss the particular PRM implementation as a correction layer, used in the application presented in this article.

## 3 Building a Correction Layer with Probabilistic Rule Models

Let us focus on mortgage default prediction models utilizing housing data. In a typical credit risk PRM model, the target variable, yy, denotes loan default status: y=1y=1 signifies “default” and y=0y=0 signifies “repayment.” The input data, XX, comprises features such as annual income, FICO credit score, home insurance characteristics, and geographical area. Hyper-parameter tuning is often necessary to optimize model performance. A typical PRM comprises 10 to 30 single- or two-factor association rules.

Constructing a correction layer using a PRM involves a similar approach, but with a different output variable. This layer aims to reconcile the discrepancies between models M1M\_{1} and M2M\_{2}. Therefore, the output variable is not binary but represents the score difference between M1M\_{1} and M2M\_{2}.

Here are all the necessary steps in detail:

1. 1.

   Build models M1M\_{1} and M2M\_{2}. Model M1M\_{1} is created using data (X1,y1)(X\_{1},y\_{1}), and M2M\_{2} is created using data (X2,y2)(X\_{2},y\_{2}) where the different data sets correspond to different time windows. Datasets are split into train and test chunks for validation.
2. 2.

   Combine the data sets (X1,y1)(X\_{1},y\_{1}) and (X2,y2)(X\_{2},y\_{2}) to create the data set data (Xc,yc)(X\_{c},y\_{c}), which will be the basis for creating the correction layer. This step is essential in the context of Transfer Learning, as this mixed dataset is used for rule mining to mitigate the effect of population drift and capture the stable, generalized rule structure that holds across both the source and target domains.
3. 3.

   Use the data (Xc,yc)(X\_{c},y\_{c}) for rule mining. The rules (R0,R1,…,Rm)(R\_{0},R\_{1},\ldots,R\_{m}) of this model form the basis of the correction layer. Then the model is calibrated on (X2,z)(X\_{2},z), where the new output variable zz represents the score difference of M2M\_{2} and M1M\_{1} where the scoring of both models is done on the dataset X2X\_{2}. The variable zz explicitly defines the residual error that the correction layer CC must learn, allowing CC to efficiently focus its learning capacity exclusively on the non-stationary components introduced by the concept drift, which is a key goal of this interpretable adaptation layer.
4. 4.

   To assess the effectiveness of the correction layer, apply M1M\_{1} to X2X\_{2}, then apply the correction layer CC to X2X\_{2} and add the scores. This combination approximates the scores obtained by M2M\_{2} applied to X2X\_{2}.

## 4 Pre- and Postcrisis Mortgage Data

### 4.1 Building the Correction Layer

In this section, we construct the correction layer for the Fannie Mae housing data for the years 2006 and 2010, and use the interpretable nature of the PRM model to gain insights into the impact of the 2008 financial crisis on different population groups.

The choice of the pre-crisis (2006) and post-crisis (2010) temporal split is deliberate. The 2008 financial crisis resulted from a structural boom-and-bust cycle characterized by loose credit standards and a complex, opaque securitization process, leading to an abrupt, system-wide shift in borrower risk profiles and market dynamics. This event represents an extreme test for concept drift mitigation, mirroring the dynamic, non-stationary environments that regulated entities like Fannie Mae must now manage, often requiring several risk model updates annually.

Using the pre-crisis data from the second quarter 2006 as input data (X1,y1)(X\_{1},y\_{1}) we build a model M1M\_{1} to predict defaults. Then, we built the second model M2M\_{2} on post-crisis data, using the data from the second quarter of the year 2010. In both cases we chose to employ XGBoost, but we could have chosen any other modeling approach as well. After having both models in place, we trained a PRM CC by applying the approach outlined above. There is a lot of freedom and choice about how to set up the PRM in order to create a correction layer – in particular in terms of the rule depth and the number of rules considered. In this case study, we chose to train a model with 15+1 rules and allowing only for single factors in each rule. The last rule R-16 is the intercept rule. The complete set of rules alongside the corresponding points is represented in the Appendix in table  [1](https://arxiv.org/html/2510.26627v1#Sx1.T1 "Table 1 ‣ Appendix ‣ Probabilistic Rule Models as Diagnostic Layers: Interpreting Structural Concept Drift in Post-Crisis Finance").

### 4.2 Effectiveness of the Correction Layer

Performance of the correction layer model was tested on a holdout test set sampled from 2010 data. Measurement of AUC demonstrated a good convergence of the combination M1M\_{1} + correction layer to the M2M\_{2} model performance. In the figure [3](https://arxiv.org/html/2510.26627v1#S4.F3 "Figure 3 ‣ 4.2 Effectiveness of the Correction Layer ‣ 4 Pre- and Postcrisis Mortgage Data ‣ Probabilistic Rule Models as Diagnostic Layers: Interpreting Structural Concept Drift in Post-Crisis Finance") we plotted the learning curve which shows how AUC depends on the number of rules in the correction layer. Further improvement can be achieved by refining the discretization and increasing the number and the depth of the rules.

However, we emphasize that achieving statistically significant equivalence with the fully retrained model (M2M\_{2}) is not the primary objective of this architecture. For our goal—to diagnose the specific nature of the concept drift by extracting interpretable rules—a “good enough” performance that demonstrates strong convergence (as shown by the AUC and default rate alignment) is sufficient. The primary utility is the insight derived from the rules.

![Refer to caption](learning_curve.png)

Figure 3: Correction layer performance as a function of number of rules.

Another illustration of the correction layer performance is shown in figure [4](https://arxiv.org/html/2510.26627v1#S4.F4 "Figure 4 ‣ 4.2 Effectiveness of the Correction Layer ‣ 4 Pre- and Postcrisis Mortgage Data ‣ Probabilistic Rule Models as Diagnostic Layers: Interpreting Structural Concept Drift in Post-Crisis Finance"). There we plotted the average default rate in 2010 data for 5 FICO bands, from low to high, alongside models predictions. We see that the 2006 model significantly underestimates the default rate for low-FICO band, but in combination with correction layer, it closely matches the observed probabilities.

![Refer to caption](default_rate_vs_fico_bars.png)

Figure 4: Effectiveness of the correction layer: When the correction layer scores are added to the predictions of M1M\_{1},
the combined score is very close to the predictions of M2M\_{2}.

### 4.3 Insights from the Correction Layer

Let’s illustrate the diagnostic insights these rules can uncover by examining specific systematic changes captured by the correction layer CC. The overall probability of default between 2006 and 2010 dropped significantly (from 2.88% to 0.58%). However, this massive reduction is primarily explained by population drift—banks introduced much stricter credit policies in an attempt to reduce the overall risk of their portfolios, removing high-risk applicants. Crucially, the changed economic reality also altered the underlying creditworthiness of people even with the same parameters. The correction layer is uniquely effective at isolating this structural shift.

For instance, let us examine the first rule R-01 (see Table [1](https://arxiv.org/html/2510.26627v1#Sx1.T1 "Table 1 ‣ Appendix ‣ Probabilistic Rule Models as Diagnostic Layers: Interpreting Structural Concept Drift in Post-Crisis Finance")):

|  |  |  |
| --- | --- | --- |
|  | cscore <706⇒−1.98​ points\text{cscore }<706\qquad\Rightarrow\quad-1.98\,\text{ points} |  |

Here, the variable *cscore* represents the average FICO credit score of the borrower and co-borrower. Negative points indicate decreasing probability of repayment (increased probability of default). The interpretation of these rules is straightforward, the results, however, might be surprising: A reduction of points means that the 2006 model overestimates the creditworthiness of a candidate in the low credit-score band if applied in 2010 reality.

The underpins the diagnostic value of the correction layer CC, in this particular example focusing on the rule R-01: The result—that borrowers in the lower-middle FICO band (below 706) experienced a relative drop in creditworthiness—might appear counter-intuitive, but the PRM rule serves as an interpretable diagnosis of structural market failure. This finding is consistent with the results of other academic studies of the crisis, in particular the suggestion that the securitization process, which underpinned the housing boom, led to reduced screening effort primarily for loans with relatively high FICO scores (Prime/Alt-A) because these were easier to securitize and sell [[16](https://arxiv.org/html/2510.26627v1#bib.bib16)]. The underperformance of these ostensibly safer segments meant that post-crisis, the risk of borrowers just below the prime threshold (FICO <706<706) increased relative to the new standard. The correction layer captures this specific shift: the M1M\_{1} model, which relied on pre-crisis screening norms, underestimated the true risk of this sub-population in the new regime. This insight is also confirmed by direct measurement of model predictions: the actual default rate of people with FICO <706<706 in 2010 is 2.77%, which is close to what the model M2M\_{2} predicts (2.79%). The prediction of model M1M\_{1} for this group gives 2.4% chances of default, which indicates that the model M1M\_{1} underestimates the riskiness of this group in the environment of the year 2010. Figure [4](https://arxiv.org/html/2510.26627v1#S4.F4 "Figure 4 ‣ 4.2 Effectiveness of the Correction Layer ‣ 4 Pre- and Postcrisis Mortgage Data ‣ Probabilistic Rule Models as Diagnostic Layers: Interpreting Structural Concept Drift in Post-Crisis Finance") confirms this observation as well.

By looking at other rules of the correction layer, it is easy to see the overall impact of the financial crisis on the population. Each single-factor rule defines a cluster of population that triggers that rule, and a corresponding points attribution indicates what was the impact of the financial crisis on this population group. For instance, the rule R-13 shows that borrowers with relatively high debt-to-income ratio are also more likely to default in 2010 than the model M1M\_{1} would expect. On the other hand, the rule R-14 shows that if the loan to value (LTV) is relatively small, defaults are now less likely to occur in comparison with the predictions of the 2006 model. However, notice that LTV characterises the loan terms and not the customer. Therefore, this rule provides limited insight into the financial crisis’ impact on the population.

In some cases, the insight provided by a rule could be discovered by a direct statistical measurement. In other situations, direct statistical discovery might be much more complicated because rules almost never trigger in isolation or due to population drift. Let’s have a look again at the rule R-01 which describes the impact on the low FICO score band. We already know that this group of population has been negatively affected by the financial crisis. However, just by comparing the default rates in that group, we observe that it has dropped from 6.36% in 2006 to 2.77% in 2010, which could yield a misleading conclusion.

The reason for this potentially misleading result lies in the separation of drift effects. The observed drop in the raw default rate is the outcome of two countervailing forces: First, the stringent post-crisis underwriting policies (population drift) ensured that the remaining applicants in the low-FICO cluster possessed significantly better attributes than their pre-crisis counterparts, thereby reducing the raw default rate. Second, the fundamental deterioration of the economy (concept drift) inherently increased the true probability of default for any individual with FICO score below 706. The naive statistical comparison (6.36% →\rightarrow 2.77%) cannot isolate these two effects, failing to reveal what would happen to a low-FICO borrower if all other attributes were held constant. The interpretable correction layer resolves this diagnostic dilemma: The FICO rule (R-01) reveals the pure deterioration of creditworthiness, while the impact of all other stabilizing attributes is encoded in other specific rules, and the overall base rate change is reflected in the Intercept Rule (R-16).

To address this limitation and statistically isolate the effect of concept drift, analysts must examine much more specific clusters where the values of most attributes are “fixed.” This process attempts to compare “exactly the same” loan segments across the 2006 and 2010 environments. However, the drawback of this brute-force approach is significant: the number of required groups grows exponentially as more attributes are fixed, causing the number of cases falling into each group to drop exponentially. Consequently, the statistical analysis quickly becomes highly noisy or completely impossible due to data scarcity within these narrow pockets of the population.

How could one identify good pockets of population, which would be informative for the detailed portfolio analysis (such as in the current work, but not only)? The intrinsic interpretability of the PRM-based correction layer provides the direct answer to this question. By design, probabilistic rules automatically identify the most significant and structurally robust combinations of features that contribute to the systematic divergence between the two models.

### 4.4 Rules clustering

To better understand the factors that drove the impact of the financial crisis, it is instructive to examine smaller segments of the population that trigger specific combinations of rules, which we refer to as rules clusters. Each rules cluster naturally defines a corresponding cluster of the population, consisting of those individuals who trigger all the rules in question.

Often, banks are interested in groups of customers that are similar according to a specified metric. Typically, the similarity is defined in feature space. The PRM framework, in contrast, offers a powerful diagnostic lens by defining similarity based on the underlying, structural changes in credit risk captured by the correction layer: PRMs offer a different way to look at clients by considering customers similar if they trigger a similar set of rules. This idea can be combined with a cluster analysis of the rules
themselves in order to figure out first frequent combination of rules. If the rules fire frequently together, they are good candidates to form a cluster.

We can assess a quality of a cluster by comparing the default probability predicted by the cluster rules with the observed probability. If those probabilities closely match, this means that the rules defining the cluster are sufficient to predict the expected default rate in that group. If predicted and observed probabilities differ significantly, the cluster has to be refined by splitting it into sub-clusters, each triggering some additional rules.

Examples of frequent rule combinations in our data set are (R-01, R-03) and (R-01, R-07). The first pair considers borrowers with a low FICO Score (rule R-01) who also have no co-borrowers (rule R-03).
The second rule concerns borrowers with a low FICO Score and specifying the property type as “Single-Family”. The following graphs [5](https://arxiv.org/html/2510.26627v1#S4.F5 "Figure 5 ‣ 4.4 Rules clustering ‣ 4 Pre- and Postcrisis Mortgage Data ‣ Probabilistic Rule Models as Diagnostic Layers: Interpreting Structural Concept Drift in Post-Crisis Finance") and [6](https://arxiv.org/html/2510.26627v1#S4.F6 "Figure 6 ‣ 4.4 Rules clustering ‣ 4 Pre- and Postcrisis Mortgage Data ‣ Probabilistic Rule Models as Diagnostic Layers: Interpreting Structural Concept Drift in Post-Crisis Finance") show that the correction layer allows to predict the scores for these two customer segments. The statistical picture is also in-line with the expected effect of these two clusters, since all three rules R-01, R-03 and R-06 have negative associated points, which means a drop in creditworthiness.

![Refer to caption](cluster_1_3.png)

Figure 5: Score comparison for the customer segment corresponding to the (R1,R3)(R\_{1},R\_{3})-cluster, considering single borrowers (R3R\_{3}) with a FICO Score of less than 706 (R1R\_{1}).



![Refer to caption](cluster_1_7.png)

Figure 6: Score comparison for the customer segment corresponding to the (R1,R7)(R\_{1},R\_{7})-cluster, consisting of applicants with a FICO Score of less than 706 (R1R\_{1}) and with a Single Family property type (R3R\_{3}).

### 4.5 Preparing for the Future: Scenario Analysis

Identifying the client base for which the changes due to the crisis were most prominent is only one application of the insights provided by the analysis of the data based on the correction layer. This process directly illustrates the benefits of our interpretably designed Transfer Learning approach. The fact that a combination of the pre-crisis model M1M\_{1} and the correction layer CC approximate the post-crisis model M2M\_{2} also can be used for scenario analysis: In a future scenario where a similar crisis is anticipated, the combination of a current model and the correction layer can mimic this future scenario which allows, for instance, for a detailed risk analysis for the case that the crisis should happen.

This scenario analysis capability is significantly enhanced by the intrinsic interpretability of the PRM correction layer. It allows risk managers to utilize the derived rules (such as R-01 and R-13) to perform informed simulations. Rather than relying solely on a simple correlation-based model, experts can adjust the weights or premises of the correction rules based on their expectations for a future economic regime—for example, anticipating whether new regulations will intensify the effects on specific DTI brackets (R-13) or alter the screening standards for Prime/Alt-A borrowers (R-01). Moreover, this scenario analysis can be overlaid with a predictive model of the likelihood of the crisis (e.g., a recession) to happen. Such an analysis is common when performing a stress test of a portfolio to evaluate its performance if a recession might occur in the future. Furthermore, the rule-based structure allows for the direct simulation of macroeconomic factor changes. For instance, experts can modify the points associated with rules related to loan purpose or credit score (R-01) to simulate the precise impact of rising unemployment rates, or adjust interest-rate related rules (R-06) to model the systemic effects of sharp central bank rate hikes. This fine-tuned, factor-specific approach drastically improves the utility of stress testing.

## 5 Conclusion

In this article, we presented an example of how to build a correction layer based on probabilistic rule models (PRMs) to analyze the difference of mortgage data from 2006 and mortgage data from 2010. The interpretable nature of the correction layer enabled us to gain detailed, sometimes counter-intuitive insights about several customer segments which help to assess portfolio risks more accurately. Crucially, this insight is able to isolate the impact of population drift (changes in the applicant pool due to stricter underwriting) from the impact on creditworthiness (true changes in riskiness, or concept drift), which would be otherwise extremely difficult to do with brute-force statistical analysis.

We established the property of the correction layer CC given by M1+C≈M2M\_{1}+C\approx M\_{2} as a vital design element of the strategy leveraging Transfer Learning principles for efficient and transparent model adaptation. The use of PRMs guarantees intrinsic interpretability, moving the correction layer beyond mere predictive convergence and transforming it into a diagnostic tool. By isolating the systematic shift between the pre-crisis and post-crisis lending regimes, the rules extracted by the correction layer successfully explained specific changes in borrower riskiness, which were shown to be consistent with external academic findings on the structural impact of securitization and reduced screening standards. This capability—providing auditable, symbolic explanations for concept drift—is paramount for maintaining robust risk management and regulatory compliance in high-stakes financial applications.

## Appendix

The following table lists the complete set of rules of the correction layer for the Fannie Mae housing data:

Table 1: Complete set of rules of the correction layer for the Fannie Mae housing data

| Rule Identifier | Rule Definition | Points |
| --- | --- | --- |
| R-01 | cscore <706<706 | -1.98 |
| R-02 | orig\_rate ≥6\geq 6 | -0.97 |
| R-03 | num\_bo <2<2 | -0.11 |
| R-04 | loan\_term ≥360\geq 360 | 0.47 |
| R-05 | purpose in [“U”, “P”] | 0.7 |
| R-06 | orig\_rate in [5.25, 6) | -2.92 |
| R-07 | prop\_type = “SF” | -1.05 |
| R-08 | purpose = “C” | -0.18 |
| R-09 | insurance\_pct ≥9\geq 9 | 1.50 |
| R-10 | comb\_ltv ≥80\geq 80 | -0.91 |
| R-11 | state = “area1” | 0.26 |
| R-12 | occupancy\_type = “P” | -0.4 |
| R-13 | dti ≥43\geq 43 | -0.87 |
| R-14 | comb\_ltv <55<55 | 0.33 |
| R-15 | ltv in [78, 80) | -0.76 |
| R-16 | - | 1.71 |

Remark 1: The rules in this table are sorted by the rule’s impact, which is a combination of the associated points and a coverage, where the latter is defined as a percentage of the population that triggers the rule. In this table, the last rule R-16 is the intercept rule. In indicates the so-called basepoints, responsible for making the a-priori probability of the target variable match the observed default rate.

Remark 2: The data used for building the models, as well as the full description of variables is freely available on Fannie Mae portal [[1](https://arxiv.org/html/2510.26627v1#bib.bib1)]. For the sake of the reader’s convenience, and since we shortened some variable names, below is a brief description of variables whose meaning might not be obvious:

* •

  cscore: an average credit score of the borrower and co-borrower.
* •

  orig\_rate: an interest rate at origination.
* •

  purpose: Cash-Out Refinance = C, Refinance = R, Purchase = P,
    
  Refinance-Not Specified = U.
* •

  occupancy\_type: Principal = P; Second = S; Investor = I; Unknown = U.
* •

  prop\_type: condominium = CO; co-operative = CP; Planned Urban Development = PU; manufactured home = MH; single-family home = SF.
* •

  num\_bo: Number of Borrowers.
* •

  state: property state. In this work we grouped the states into 4 large categories. In particular, area1 = [“NV”, “AZ”, “CA”, “FL”, “MI”].

## References

* [1]

  FannieMae.
  Fannie Mae Single-Family Loan Performance Data.
  <https://capitalmarkets.fanniemae.com/>, 2024.
* [2]

  N.J. Nilsson.
  Probabilistic logic.
  Artificial Intelligence, 28:71–87, 1986.
* [3]

  M. Richardson and P. Domingos.
  Markov logic networks. mach learn 62, 107–136.
  Mach. Learn., 62:107–136, 2006.
* [4]

  J. Pearl.
  Probabilistic reasoning in intelligent systems: Networks of
  plausible inference.
  Morgan Kaufmann, 1988.
* [5]

  C. Wang, N. Komodakis, and N. Paragios N.
  Markov random field modeling, inference & learning in computer
  vision & image understanding: A survey.
  Computer Vision and Image Understanding, 117:1610–1627, 2013.
* [6]

  D. Venugopal and V. Gogate.
  Evidence-based clustering for scalable inference in markov logic.
  In T. Calders, F. Esposito, E. Hüllermeier, and R. Meo, editors,
  Machine Learning and Knowledge Discovery in Databases, pages 258–273.
  Springer, Berlin, 2014.
* [7]

  S.H. Bach, M. Broecheler, B. Huang, and L. Getoor.
  Hinge-loss markov random fields and probabilistic soft logic.
  Journal of Machine Learning Research, 18:1–67, 2017.
* [8]

  D. Koller and N. Friedman.
  Probabilistic graphical models: principles and techniques.
  Cambridge, MA, MIT Press, 2009.
* [9]

  C. Rudin.
  Stop explaining black box machine learning models for high stakes
  decisions and use interpretable models instead.
  Nat. Mach. Intell., 1:206–215, 2019.
* [10]

  P.F. D’Haese, V. Finomore, D. Lesnik, L. Kornhauser, T. Schaefer, P.E. Konrad,
  S. Hodder, C. Marsh, and A.R. Rezai.
  Prediction of viral symptoms using wearable technology and artificial
  intelligence: A pilot study in healthcare workers.
  PLoS ONE, 16:e0257997, 2021.
* [11]

  R.A. Anderson.
  Credit Intelligence & Modelling: Many Paths through the Forest
  of Credit Rating and Scoring.
  Oxford University Press, 2021.
* [12]

  R. Agrawal, T. Imieliński, and A. Swami.
  Mining association rules between sets of items in large databases.
  In SIGMOD ’93: Proceedings of the 1993 ACM SIGMOD international
  conference on Management of data, pages 207 – 216. 1993.
* [13]

  C. Silverstein, S. Brin, and R. Motwani.
  Beyond market baskets: Generalizing association rules to dependence
  rules.
  Data Mining and Knowledge Discovery, 2:39–68, 1998.
* [14]

  M. Narvekar and S.F. Syed.
  An optimized algorithm for association rule mining using fp tree.
  Procedia Computer Science, 45:101–110, 2015.
* [15]

  R. Fletcher.
  Practical Methods of Optimization.
  John Wiley & Sons, 1987.
* [16]

  Juan Ospina and Harald Uhlig.
  Mortgage-backed securities and the financial crisis of 2008: A post
  mortem.
  Working Paper w24509, National Bureau of Economic Research (NBER),
  2018.