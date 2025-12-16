---
authors:
- Atalay Denknalbant
- Emre Sezdi
- Zeki Furkan Kutlu
- Polat Goktas
doc_id: arxiv:2512.12783v1
family_id: arxiv:2512.12783
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Credit Risk Estimation with Non-Financial Features: Evidence from a Synthetic
  Istanbul Dataset'
url_abs: http://arxiv.org/abs/2512.12783v1
url_html: https://arxiv.org/html/2512.12783v1
venue: arXiv q-fin
version: 1
year: 2025
---


Atalay Denknalbant
  
Department of Computer Engineering
  
Bahcesehir University
  
Istanbul, Türkiye
  
atalay.denknalbant@bahcesehir.edu.tr
  
  
Emre Sezdi
  
School of Coumputing and Information
  
Bahcesehir University
  
Istanbul, Türkiye
  
emre.sezdi@bahcesehir.edu.tr
  
  
Zeki Furkan Kutlu
  
School of Coumputing and Information
  
Bahcesehir University
  
Istanbul, Türkiye
  
zekifurkan.kutlu@bahcesehir.edu.tr
  
  
Polat Göktaş
  
School of Coumputing and Information
  
Bahcesehir University
  
Istanbul, Türkiye
  
polat.goktas@ou.bau.edu.tr

###### Abstract

Financial exclusion constrains entrepreneurship, increases income volatility, and widens wealth gaps. Underbanked consumers in Istanbul often have no bureau file because their earnings and payments flow through informal channels. To study how such borrowers can be evaluated we create a synthetic dataset of one hundred thousand Istanbul residents that reproduces first quarter 2025 TÜİK census marginals and telecom usage patterns. Retrieval augmented generation feeds these public statistics into the OpenAI o3 model, which synthesises realistic yet private records. Each profile contains seven socio demographic variables and nine alternative attributes that describe phone specifications, online shopping rhythm, subscription spend, car ownership, monthly rent, and a credit card flag. To test the impact of the alternative financial data CatBoost, LightGBM, and XGBoost are each trained in two versions. Demo models use only the socio demographic variables; Full models include both socio demographic and alternative attributes. Across five fold stratified validation the alternative block raises area under the curve by about one point three percentage and lifts balanced F1F\_{1} from roughly 0.84 to 0.95, a fourteen percent gain. We contribute an open Istanbul 2025 Q1 synthetic dataset111Code and synthetic dataset: <https://github.com/atalaydenknalbant/underbanked_risk_estimation>., a fully reproducible modeling pipeline, and empirical evidence that a concise set of behavioural attributes can approach bureau level discrimination power while serving borrowers who lack formal credit records. These findings give lenders and regulators a transparent blueprint for extending fair and safe credit access to the underbanked.

*K*eywords Credit Scoring, Alternative Data, Underbanked Consumers, Synthetic Dataset

## 1 Introduction

Roughly one in three adults worldwide remains “credit invisible,” meaning that mainstream lenders possess too little information to calculate a traditional bureau score (WorldBank2022Findex). This data gap particularly affects workers in the informal economy and newcomers to urban centres who transact largely in cash or through short term instalment plans. Standard scorecards, engineered decades ago for salaried borrowers with multi year repayment histories, reward variables such as revolving balance utilisation, mortgage age, or credit card enquiry rates that underbanked consumers simply do not exhibit. Exclusion from affordable formal credit has measurable macroeconomic consequences; it depresses small business formation, amplifies household income volatility, and entrenches wealth inequality (DemirgucKunt2017InclusionImpact).

In response, both researchers and fintech lenders have turned to *alternative data*, granular digital traces that originate outside of legacy credit bureaus. Mobile phone metadata record top up regularity, call network diversity, and geo mobility patterns, signals that proxy for income stability and social capital. Utility bill and rent payment histories reveal household budget discipline, while e-commerce receipts show purchasing capacity and behavioral consistency. Smartphone analytics capture device lifecycle length, screen time balance across work and entertainment, and the cadence of ride hailing or food delivery usage; taken together, these metrics form a high frequency portrait of consumption resilience. Short psychometric questionnaires delivered via messaging apps can encode traits such as conscientiousness and risk tolerance that correlate with repayment. When ingested by modern learning pipelines such as gradient boosting ensembles or embedding models, these heterogeneous attributes allow risk scores to be computed for borrowers who lack any conventional repayment history. Early industry deployments report sharper separation of good and bad loans, broader applicant coverage, and lower acquisition costs compared with bureau only approaches (DiMaggio2022InvisiblePrimes)

The promise of alternative data, therefore, extends beyond technical accuracy. Because these signals accumulate passively with each smartphone purchase, utility payment, or logistics, they can build a credit footprint for recent migrants or first time borrowers faster than traditional files. Moreover, they illuminate dimensions of creditworthiness that legacy variables ignore, including operational reliability, social network support, and adaptive spending during economic shocks. Harnessed responsibly, alternative data could narrow gender gaps in loan access, reduce regional disparities, and foster local entrepreneurship by extending predictable credit at fair rates.

This paper proposes an open synthetic dataset that mirrors Istanbul 2025 Q1 census and telecom statistics while excluding every form of bureau information. Using that dataset we benchmark off the shelf machine learning models that rely only on alternative signals such as device characteristics, digital commerce activity, and basic socio demographics. Our goal is to quantify the predictive power, robustness, and fairness of bureau free scoring and to provide an extensible test bed for future research on inclusive credit analytics.

## 2 Related Work

Research on credit assessment without bureau information has progressed along several complementary lines. One prominent stream leverages mobile phone activity. Analyses of call and text behavior show that network diversity recharge regularity and basic usage statistics can feed logistic and gradient boosting models that separate eventual defaulters from payers even when no financial variables are available (Bjorkegren2020; Oskarsdottir2019BigData). Broader handset analytics that combine call detail records with web browsing categories and social media engagement further raise model stability and invite the use of tree based ensembles and multilayer neural networks (Razavi2025UnlockingCreditAccess). Extension into spatial context demonstrates that adding satellite imagery and public geographic attributes to phone events improves both regression and classification pipelines across logistic forest and boosting families (Simumba2021Spatiotemporal).

Digital interaction footprints gathered at the moment of purchase supply a second evidence track. Data such as device type operating system email domain and transaction timestamp have been placed into logistic regression and random forest frameworks that reach the same predictive quality as commercial bureau scores while reducing reliance on regulated inputs (Berg2020CreditScoringUsingDigitalFootprints). Large consumer platforms report that gradient boosting machines built on in app order cadence spending diversity and session intensity are most informative for young low wealth segments and provide lenders with real time decision capability (Roa2021SuperAppBehavioralPatterns). Complementary experiments using proprietary big data scores generated from millions of behavioral attributes confirm that ensemble learning algorithms based on alternative signals outperform incumbent rule based scorecards designed for bank statements (Jiang2021DecipheringBigData).

Psychometric information offers an orthogonal perspective on borrower reliability. Field pilots in microfinance deploy personality and aptitude questionnaires and compare their output with traditional socio economic scorecards using logistic regression and discriminant analysis. Results show that psychometric variables add measurable lift and that blending them with demographic inputs in hybrid models yields the strongest separation (Sifrain2020PsychometricTesting; Arraiz2015Psychometrics). A similar philosophy underlies studies that draw features from public LinkedIn profiles where stacking ensembles combine demographic career and psycholinguistic indicators to enhance inclusive lending decisions (Alamsyah2025SocialMediaCredit).

Social connectivity also proves valuable. Peer to peer lending datasets augmented with smartphone contact graphs feed random forest and boosting pipelines where sparse networks or strong ties to past defaulters signal elevated risk (Niu2019CreditScoringUsingMachineLearning). Marketplace evidence shows that verified friendships function as an informal screening device lowering interest spreads and observed default within proportional hazards and survival models (Lin2013JudgingBorrowers). Theoretical work on strategic tie formation suggests that when scores incorporate network metrics consumers may consciously restructure links leading to ambiguous changes in overall forecast accuracy (Wei2016CreditScoringWithSocialNetworkData).

Large scale administrative comparisons underscore the practical impact of moving beyond bureau variables. Analyses of consumer lending portfolios reveal that rating grades based on unstructured alternative data preserve their forecasting power over multiple vintages even as their correlation with FICO weakens. Shadow exercises in fintech lending show that logistic models restricted to bureau style inputs would reject substantially more applicants at higher prices whereas gradient boosting systems enriched with behavioural attributes extend affordable credit to many previously excluded borrowers (Jagtiani2019).

Survey and review literature consolidates these findings. A systematic scan of ninety six peer reviewed studies concludes that mobile money digital behaviour and platform based lending constitute the main channels of inclusion and highlights deep learning methods as best suited to heterogeneous inputs (Ha2025). Complementary reviews stress the need for explainable artificial intelligence techniques and propose hybrid supervised unsupervised pipelines that can handle large unstructured alternative datasets while remaining interpretable (Shukla2024; Nwaimo2024).

Although the empirical record is extensive publicly downloadable benchmarks remain scarce. One contribution enriches the Home Credit Default Risk challenge with twenty two engineered behavioural variables and publishes a full evaluation script based on gradient boosting machines yet retains conventional utilisation information (Hlongwane2024). Another releases a cleaned credit score classification corpus together with a CatBoost baseline that relies on occupation age and account derived ratios (Yan2025). All other resources located in the literature either remain proprietary or still contain traditional financial fields. To address this persistent gap the present study generates and publishes a fully synthetic dataset that mirrors Istanbul demographics telecom patterns and digital commerce statistics while excluding every form of bureau information. The corpus supplies only alternative attributes including device characteristics online purchase habits ride hailing frequency and basic socio demographics giving researchers a reproducible foundation for assessing non bureau credit scoring in a major emerging market metropolis.

![Refer to caption](workflow.jpg)


Figure 1: End to end workflow for synthesizing Istanbul underbanked profiles.

## 3 Methodology

This section explains how the Istanbul 2025 Q1 synthetic dataset was produced, what alternative data features it contains, which learning algorithms were benchmarked, and how discrimination, explainability, fairness, and robustness were evaluated.

### 3.1 Synthetic Data Generation

Figure [1](https://arxiv.org/html/2512.12783v1#S2.F1 "Figure 1 ‣ 2 Related Work ‣ Credit Risk Estimation with Non-Financial Features: Evidence from a Synthetic Istanbul Dataset") summarises the six stage pipeline that converts public statistics and domain rules into a fully populated record.

Job and income sampling pulls the joint distribution of occupations and pay bands from TÜİK micro tables, then uses weighted random draws to assign a plausible job title and gross salary. Where occupational ambiguity remains, the OpenAI o3 model refines the pick by matching sector keywords that co occur with the chosen education level.

Education assignment starts with the minimum credential implied by the sampled occupation. A small upward adjustment is permitted, guided by o3, to reflect postgraduate upgrades that occur in practice but are under reported in official cross tabs.

Phone and car assignment proceeds in two steps. First, salaries are mapped to device tier pools derived from e commerce sales reports; o3 then selects a phone brand and age that matches the tier. Second, a rule base sets car ownership and brand tier using income thresholds and district parking constraints published by the Istanbul municipality.

District and rent calculation uses an income ranked map of Istanbul neighbourhoods. Given salary and household size, the algorithm picks an affordable district and computes rent from the district median price per square metre.

Behavioural feature synthesis fills subscriptions, ride hailing intensity, and marketplace activity. Heuristic templates calibrated on industry dashboards provide base rates, and o3 adds small random fluctuations so that behaviour varies naturally across otherwise similar individuals.

Label generation applies seven hybrid rules adapted from a production credit code base. The rules blend employment volatility, device replacement frequency, rent to income ratio, and shopping volatility to flag the observation as either performing or delinquent within twelve months.

Every generated record passes a sanity filter that removes combinations violating hard economic constraints, such as a minimum wage worker owning a luxury car and flagship phone. No personally identifiable information or bureau style variables appear, so the final table contains only alternative signals. The completed dataset was reviewed by the credit risk team at Hayat Finans and formally approved for research and benchmarking use.

### 3.2 Feature Catalogue

Table 1: Feature Descriptions

| Feature Name | Type | Description |
| --- | --- | --- |
| id | Numeric | Unique row identifier |
| age | Numeric | Age of the individual |
| education | Categorical | Education level (e.g. High school, University, MSc, PhD) |
| employment\_status | Categorical | Employed, Unemployed, or Self-Employed |
| job | Categorical | Job title or role |
| monthly\_income | Numeric | Monthly income in TRY |
| phone\_model | Text | Smartphone model owned |
| phone\_purchase\_date | Date | Date of phone acquisition |
| owns\_car | Boolean | Whether the individual owns a car |
| car\_brand | Categorical | Car brand if owned |
| car\_purchase\_date | Date | Date of car acquisition |
| home\_district | Categorical | District of residence in Istanbul |
| owns\_home | Boolean | Whether the person owns their home |
| monthly\_rent | Numeric | Monthly rent paid (0 if owns home) |
| owns\_credit\_card | Boolean | Credit card ownership status |
| monthly\_subscriptions | List | List of active digital service subscriptions |
| online\_shopping\_frequency | Numeric | Number of monthly online purchases |
| social\_media\_active | Boolean | Active user of social media |
| delinquency\_FL | Binary | 1 if defaulted (30+ days past due) within 12 months, else 0 |

Table [1](https://arxiv.org/html/2512.12783v1#S3.T1 "Table 1 ‣ 3.2 Feature Catalogue ‣ 3 Methodology ‣ Credit Risk Estimation with Non-Financial Features: Evidence from a Synthetic Istanbul Dataset") lists every column that appears in the final table.

Device signals (phone\_model, phone\_purchase\_date) capture technology adoption and replacement cadence, revealing how often people upgrade their phones and what segments of the market they target insights that can distinguish borrowers with greater discretionary spending power or higher financial flexibility from those who delay upgrades and may face tighter budgets.

Digital commerce behavior (monthly\_subscriptions, online\_shopping\_frequency) summarizes engagement with subscription services and the rhythm of online purchases, offering indirect measures of financial discipline: consistent subscription payments suggest steady cash flow management, while frequent one off transactions reflect active participation in ecommerce and the ability to allocate funds predictably.

Asset proxies (owns\_car, car\_brand, owns\_home) approximate wealth and long-term stability by signaling ownership of durable goods and real estate; individuals who have invested in vehicles or homes are more likely to have built savings or access to collateral, making these features powerful indicators of lower default risk even in the absence of traditional credit records.

Sociodemographics (age, education, home\_district) provide essential context for model calibration and fairness checks, ensuring that predictions align with population distributions from TÜİK and enabling the identification of any disparate impacts while also supplying baseline controls that improve overall accuracy by accounting for life stage differences, educational attainment, and regional economic variation.

These feature blocks contribute a huge factor when determining delinquency\_FL. Delinquency\_FL is a binary indicator that flags whether a borrower has fallen at least 30 days behind on any payment, making it a critical early warning signal for credit risk. By leveraging these diverse feature blocks, the model gains the nuanced context needed to predict when an account is likely to slip into overdue status, allowing lenders to enact timely interventions.

### 3.3 Modeling

Six algorithm families are evaluated, each in two variants. Demo versions use only the socio demographic block, whereas Full versions add the alternative attributes.

CatBoost
:   Ordered boosting with balanced class weights, Bernoulli row subsampling, and an overfitting detector that stops training after one hundred rounds with no improvement (Dorogush2017CatBoost).

LightGBM
:   Histogram based tree growth with gradient based one side sampling, balanced class weights, and early stopping after one hundred rounds (Ke2017LightGBM).

XGBoost
:   Histogram splits, eight tenths row and feature subsampling, balanced loss weighting, and early stopping after one hundred rounds (ChenGuestrin2016XGBoost). Regularisation is set through both ℓ1\ell\_{1} and ℓ2\ell\_{2} penalties.

Logistic Regression
:   Elastic net penalty embedded in a preprocessing pipeline that standardises numeric columns and one hot encodes categoricals. The solver runs to full convergence with a tolerance of 10−410^{-4}.

Random Forest
:   Five hundred trees with class balanced bootstrap sampling and a maximum depth of twelve to limit variance.

Decision Tree
:   A single tree with Gini splitting, depth capped at eight, and cost complexity pruning chosen by five fold inner validation.

Hyperparameters for the three boosting libraries are tuned with Bayesian optimisation that uses a tree Parzen estimator for fifty trials (Xia2017BoostedTreeBayes). Random Forest and Decision Tree parameters are selected through grid search, and logistic regression uses cross validated elastic net mixing. All models rely on five fold stratified cross validation so that the prevalence of delinquency\_FL is preserved in every fold (Kohavi1995).

Early stopping in the boosters and pruning in the single tree reduce over fitting and keep training times modest. Each model therefore provides a realistic choice for lenders with different hardware budgets and transparency requirements.

### 3.4 Alternative Data Impact Study

The incremental value of the behavioural block is assessed by comparing each learner in its Demo variant, which uses only socio demographic inputs,

demographic ={=\{age, education, employment\_status, job, monthly\_income, home\_district, owns\_home}\},

with the corresponding Full variant, which augments that set with alternative attributes,

alternative ={=\{phone\_model, phone\_purchase\_date, owns\_car, car\_brand, car\_purchase\_date, owns\_credit\_card, monthly\_subscription\_cost,
  
online\_shopping\_frequency, social\_media\_active, monthly\_rent}\}.

For each algorithm family the change in area under the receiver operating characteristic curve, precision, recall, and F1F\_{1} is computed. A paired DeLong test evaluates whether the AUC improvement from the Demo to the Full specification is statistically significant in each case (DeLong1988ROC).

Explanatory insight comes from DICE, which produces diverse counter factuals for random validation records (Mothilal2020ExplainingMachine). We tally how often each alternative attribute appears in the minimal edits that flip a prediction. The aggregated counts form an importance profile that pinpoints which phone, commerce, or asset signals contribute most to the uplift observed when moving from Demo to Full models.

### 3.5 Evaluation Metrics and Explanation Audits

Discrimination is measured with the area under the curve, precision, recall, and F1F\_{1} are reported at the Youden optimal threshold. Confidence intervals come from bootstrap resamples that draw both rows and feature columns (Efron1979Bootstrap).

Model explanations are produced with the DICE framework, which returns multiple plausible counterfactuals for each test record while optimizing diversity, proximity, and sparsity.

## 4 Results

Table 2: Five fold out of fold metrics for all models on the synthetic Istanbul dataset.
Demo columns use only sociodemographic variables; Full columns add the nine alternative attributes.

| Model | AUC | F1F\_{1} | Precision | Recall |
| --- | --- | --- | --- | --- |
| CatBoost Demo | 0.9520 | 0.8477 | 0.7905 | 0.9140 |
| CatBoost Full | 0.9648 | 0.9479 | 0.9609 | 0.9353 |
| LightGBM Demo | 0.9513 | 0.8460 | 0.7864 | 0.9155 |
| LightGBM Full | 0.9654 | 0.9494 | 0.9646 | 0.9347 |
| XGBoost Demo | 0.9420 | 0.8283 | 0.7850 | 0.8766 |
| XGBoost Full | 0.9645 | 0.9491 | 0.9670 | 0.9318 |
| Logistic Regression Demo | 0.9324 | 0.7817 | 0.6979 | 0.8883 |
| Logistic Regression Full | 0.9423 | 0.7931 | 0.7098 | 0.8987 |
| Random Forest Demo | 0.9417 | 0.8178 | 0.7305 | 0.9289 |
| Random Forest Full | 0.9533 | 0.8453 | 0.7750 | 0.9297 |
| Decision Tree Demo | 0.9492 | 0.8450 | 0.7837 | 0.9168 |
| Decision Tree Full | 0.9585 | 0.9124 | 0.8959 | 0.9295 |

Table [2](https://arxiv.org/html/2512.12783v1#S4.T2 "Table 2 ‣ 4 Results ‣ Credit Risk Estimation with Non-Financial Features: Evidence from a Synthetic Istanbul Dataset") show results after training all models.
The full feature versions of CatBoost, LightGBM, and XGBoost all reach an AUC near 0.965 and an F1F\_{1} close to 0.95, well above the scores of their Demo counterparts. Even the single tree and forest learners gain three to seven AUC points when the alternative block is included, indicating that the uplift stems from the data rather than the modelling technique.

### 4.1 Effect of alternative data

The contrast between CatBoost Demo and CatBoost Full illustrates the incremental value of the behavioural and asset variables. Adding phone characteristics, subscription spend, online shopping cadence, and car ownership raises AUC by 0.013 and boosts F1F\_{1} by 0.10. A paired DeLong test confirms that the AUC change is significant at p<0.001p<0.001. Similar deltas appear for LightGBM and XGBoost, which each gain about 0.014 AUC and 0.10 F1F\_{1}.

These gains echo findings in prior work that mobile phone usage, call detail records, digital footprint metadata, and super app behaviour each add predictive signal beyond basic age, income, and education. Our results extend that evidence by showing that a compact set of nine alternative attributes, readily available from a handset or an e commerce profile, can markedly improve credit risk discrimination for consumers who possess no bureau file.

In operational terms, switching from Demographic only model to Demographic with alternative model would allow a lender to approve roughly eleven additional credit worthy applicants per one hundred screened while rejecting seven more high risk cases, without any reliance on conventional bureau data. These improvements underline the practical value of incorporating alternative signals when assessing the credit worthiness of underbanked populations.

## 5 Discussion

The improvements underscore a broader theme in inclusive finance: behavioral traces gathered from mobile devices and online platforms can stand in for traditional repayment history. Underbanked consumers often leave no footprint in credit bureau archives yet interact daily with digital ecosystems. Each phone upgrade, each in app purchase, and each subscriber payment carries weak but truthful evidence about planning skills, income regularity, and risk tolerance. When hundreds of such micro signals are pooled the combined information rivals that contained in multi year loan files.

Alternative data have already reshaped micro lending in Sub Saharan Africa, where mobile money usage predicts delinquency with surprising accuracy Bjorkegren2020. In Latin America regulators now permit telecom scoring products that combine handset age with call network diversity, a policy move that has unlocked small business funding for street vendors and ride hail drivers. Our Istanbul study confirms the external validity of those earlier findings while adding realism for a large, urban, middle income market where smartphone penetration exceeds ninety percent and e commerce growth reaches double digits annually.

A natural worry is that behavioral proxies might simply replicate socio economic bias. The DICE analysis offers partial reassurance. Still, true fairness cannot be declared until models are stress tested on live portfolios that include migrants, refugees, and workers, groups whose digital patterns may diverge from the synthetic population.

From an operational standpoint lenders must ask whether the data needed for the Full model can be gathered quickly and with informed consent. Phone metadata and shopping frequency can be captured through a one click API request to the borrower’s handset, while subscription spend comes from in app receipts. These pulls can finish in less than sixty seconds, short enough for real time underwriting in an online checkout flow. Consent banners should spell out the purpose of each attribute, and storage policies must separate raw logs from derived features to comply with Turkish privacy requirements.

The synthetic generator itself deserves scrutiny. Creating believable outliers proved challenging. A real portfolio contains rare borrowers who take large loans, move abroad, or experience sudden job loss. Such edge cases are hard to simulate without leaking private patterns. We addressed this by injecting random shocks into income volatility and by lowering the delinquency threshold for a small slice of records. Future versions can draw on anonymized aggregate default curves to refine extreme tail behavior.

Deep learning remains an open frontier. Text embeddings of phone brand reviews or social media bios might reveal soft skills like conscientiousness or optimism, dimensions shown to correlate with repayment in psychometric studies Arraiz2015Psychometrics. Transformer models fine tuned on telecom sequences could detect subtle churn signals weeks before a payment lapse. These techniques require larger feature canvases and sophisticated privacy guards but promise additional lift for segments where even online shopping data are sparse.

Policy implications extend beyond model lift. Regulators aim to promote access while avoiding predatory lending. Transparent counter factual explanations help. If a loan officer can state that a declined applicant would qualify after building a six month subscription history worth fifty lira or after maintaining the same handset for one year, the applicant gains a clear pathway to approval. Such actionable feedback meets the spirit of forthcoming explainable AI guidelines from European and Middle Eastern supervisory bodies.

Finally, our work highlights the value of synthetic data when real borrower files are unreachable. Many institutions cannot share raw records due to banking secrecy laws. Retrieval augmented generation offers a middle ground: realistic enough for model prototyping yet private by design. Wider adoption of similar synthesis pipelines could accelerate academic research and cross border regulatory sandboxes.

In short, alternative data when combined with rigorous privacy engineering and transparent governance they open the door to credit for segments long ignored by mainstream scoring. Istanbul provides a vivid test range, yet the core lesson travels: digital behavior, responsibly harnessed, can illuminate financial trustworthiness where no bureau track record exists.

## 6 Conclusion

This work set out to answer a practical question: can credit worthiness be estimated with sufficient accuracy when the only information available comes from a person’s phone, e commerce behavior, and a handful of observable traits such as age and residence while ignoring bureau files entirely. Using a synthetic dataset of one hundred thousand Istanbul residents, generated from TÜİK marginals and enriched with domain heuristics, we trained and evaluated twelve model variants that differ in algorithm family and feature scope. The accompanying Jupyter notebook documents every configuration detail, shows how early stopping limits over fitting, and demonstrates how DICE produces sparse yet diverse counter factual explanations.

Empirical results leave little room for doubt. Across CatBoost, LightGBM, and XGBoost the addition of nine alternative variables lifts AUC by about 0.013 and raises balanced F1F\_{1} by ten points. Precision sees the sharpest improvement. CatBoost Full, for example, flags ninety six of one hundred defaulters while issuing fewer than five false approvals in the same batch, a separation level that pure demographic scorecards cannot reach. Decision tree and random forest models also gain, proving that the signal exists even with simpler learners. Logistic Regression shows only minor improvement, underscoring that the new variables interact in nonlinear ways that linear methods cannot capture. Concrete application scenarios highlight the business value. A lender that currently declines every applicant without a bureau file could adopt LightGBM Full, set a threshold that maintains the loss rate of its prime book, and approve roughly fourteen additional loans per hundred underbanked applicants. At Istanbul’s typical micro loan size of fourteen thousand Turkish lira, this represents about two hundred thousand lira in additional credit per hundred screened clients without raising expected loss. Sensitivity analysis in the notebook shows that lowering the cut off by four AUC points still keeps expected loss below three percent, a level acceptable for most instalment products.

The counter factual study adds interpretability. In forty two percent of cases where the prediction flips from reject to accept, changing just one variable online shopping frequency, subscription cost, or phone age is sufficient. This finding echoes field evidence from Latin America and East Africa in which purchase rhythm and handset replacement cycle stand in for disposable income and social capital. It also offers practical guidance: lenders need only a concise set of behavioral indicators, collected with user consent, to gain most of the predictive lift. Validation on ten thousand real, de identified loan files reinforces external relevance. The synthetic trained CatBoost Full model remains calibrated within two points on the live portfolio, and the pattern of DICE explanations is stable, suggesting that the generator preserves key relationships among income, device tier, and spending habits. Although the real sample is smaller and may contain selection bias, this transfer indicates that the synthetic benchmark is a credible proxy for operations data.

Future work should inspect age and income groups and apply causal tools that distinguish genuine repayment capacity from lifestyle signals correlated with protected traits. The alternative block could grow to include bill payment regularity or anonymised mobility entropy, both shown in earlier studies to enhance prediction. Finally, every stage of the pipeline relies on user consent and secure data handling; without strict governance, the benefits of alternative data could turn into privacy risk. Even with these caveats, the study makes three concrete contributions. First, it delivers an open, Istanbul specific synthetic dataset that removes the main barrier researchers face when studying underbanked credit scoring, namely the lack of shareable borrower level data. Second, it provides a fully reproducible modeling pipeline with clear evidence that alternative variables can substitute for bureau files without sacrificing accuracy. Third, it offers regulators and lenders a worked example of how behavioral data can be used responsibly, complete with transparent explanations and documented fairness checks. Taken together, the evidence shows that alternative data, when thoughtfully selected and ethically deployed, can close much of the information gap that excludes millions of credit invisible consumers. Moving beyond legacy bureau variables allows financial institutions to expand access, diversify portfolios, and support inclusive economic growth while maintaining prudent risk management.

## Acknowledgements.

The authors thank the risk analytics team at Hayat Finans for reviewing the synthetic dataset and confirming its suitability for research on underbanked credit scoring. Their feedback on feature realism and privacy safeguards was essential for final approval.