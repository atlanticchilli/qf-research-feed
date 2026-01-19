---
authors:
- Sultan Amed
- Tanmay Sen
- Sayantan Banerjee
doc_id: arxiv:2601.11134v1
family_id: arxiv:2601.11134
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'FSL-BDP: Federated Survival Learning with Bayesian Differential Privacy for
  Credit Risk Modeling'
url_abs: http://arxiv.org/abs/2601.11134v1
url_html: https://arxiv.org/html/2601.11134v1
venue: arXiv q-fin
version: 1
year: 2026
---


Sultan Amed
Corresponding author. Email: ef21sultanamed@iimidr.ac.in
OM & QT Area, Indian Institute of Management Indore, M.P. 453556, India.

Tanmay Sen
SQC & OR Unit, Indian Statistical Institute Kolkata, W.B. 700108, India

Sayantan Banerjee
OM & QT Area, Indian Institute of Management Indore, M.P. 453556, India.

###### Abstract

Credit risk models are a critical decision-support tool for financial institutions, yet tightening data-protection rules (e.g., GDPR, CCPA) increasingly prohibit cross-border sharing of borrower data, even as these models benefit from cross-institution learning. Traditional default prediction suffers from two limitations: binary classification ignores default timing, treating early defaulters (high loss) equivalently to late defaulters (low loss), and centralized training violates emerging regulatory constraints. We propose a Federated Survival Learning framework with Bayesian Differential Privacy (FSL-BDP) that models time-to-default trajectories without centralizing sensitive data. The framework provides Bayesian (data-dependent) differential privacy (DP) guarantees while enabling institutions to jointly learn risk dynamics. Experiments on three real-world credit datasets (LendingClub, SBA, Bondora) show that federation fundamentally alters the relative effectiveness of privacy mechanisms. While classical DP performs better than Bayesian DP in centralized settings, the latter benefits substantially more from federation (+7.0% vs +1.4%), achieving near parity of non-private performance and outperforming classical DP in the majority of participating clients. This ranking reversal yields a key decision-support insight: privacy mechanism selection should be evaluated in the target deployment architecture, rather than centralized benchmarks. These findings provide actionable guidance for practitioners designing privacy-preserving decision support systems in regulated, multi-institutional environments.

Keywords: Federated Learning, Survival Analysis, Bayesian Differential Privacy, Credit Scoring, Time-to-Default, Digital Lending

## 1 Introduction

Rapid and sustained growth in digital lending has transformed global credit markets, expanding speed, accessibility, and financial inclusion to populations that were historically underserved. Recent data from the World Bank’s Global Findex 2025 indicates that 79% of adults globally held a financial account in 2024, up from 51% in 2011 [worldbank2025findex](https://arxiv.org/html/2601.11134v1#bib.bib1) . This expansion has been largely driven by digital platforms that lower barriers for unbanked and underbanked consumers, a trend further supported by mobile and fintech innovations in regions such as Sub-Saharan Africa and South Asia, where mobile money has substantially increased women’s access to financial tools ([klapper2024digital,](https://arxiv.org/html/2601.11134v1#bib.bib2) ; [worldbank2024ssa,](https://arxiv.org/html/2601.11134v1#bib.bib3) ). Peer-to-peer platforms such as LendingClub [zhang2020credit](https://arxiv.org/html/2601.11134v1#bib.bib4) ; [serrano2016use](https://arxiv.org/html/2601.11134v1#bib.bib5) ; [jagtiani2019roles](https://arxiv.org/html/2601.11134v1#bib.bib6) ; [lyocsa2022default](https://arxiv.org/html/2601.11134v1#bib.bib7)  in the United States and Bondora [lyocsa2022default](https://arxiv.org/html/2601.11134v1#bib.bib7) ; [domotor2023peer](https://arxiv.org/html/2601.11134v1#bib.bib8)  in Europe illustrate how low-cost, data-driven systems are reshaping retail lending, improving financial inclusion while introducing new challenges for risk management. The rise in granular data collection and application of artificial intelligence has further accelerated this shift, with credit scoring remaining central to financial decision-making [kowsar2023credit](https://arxiv.org/html/2601.11134v1#bib.bib9) . Credit scoring models serve as the core decision support artifact in lending operations, directly influencing approval rates, pricing strategies, portfolio risk management, and regulatory capital calculations. As such, advances in credit risk modeling constitute contributions to the decision support systems domain with immediate practical relevance.

Digital lending relies on automated credit decision engines. As illustrated in Figure [1](https://arxiv.org/html/2601.11134v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ FSL-BDP: Federated Survival Learning with Bayesian Differential Privacy for Credit Risk Modeling"), the credit assessment process begins with basic eligibility checks including minimum acceptance criteria (e.g., age, prior default history, jurisdictional requirements). The system then performs deduplication to determine whether the applicant is an existing customer or a new applicant. Existing customers with strong internal credit scores may be processed via straight-through processing, while others undergo further assessment including fraud screening, income estimation, and computation of credit risk measures such as probability of default (PD), loss given default (LGD), and exposure at default (EAD). Among these, PD models exert the greatest influence on loan approvals, credit risk management, and portfolio monitoring, ultimately affecting financial stability [acemoglu2015systemic](https://arxiv.org/html/2601.11134v1#bib.bib10) . Accurate default risk assessment supports both institutional soundness and systemic resilience [khurram2025systemic](https://arxiv.org/html/2601.11134v1#bib.bib11) ; [baesens2023boosting](https://arxiv.org/html/2601.11134v1#bib.bib12) .

![Refer to caption](Fig/UWE_5.png)


Figure 1: AI driven end-to-end credit decision engine

Historically, PD scoring has been dominated by scorecards and logistic regression, valued for interpretability and regulatory acceptance [baesens2014analytics](https://arxiv.org/html/2601.11134v1#bib.bib13) ; [baesens2023boosting](https://arxiv.org/html/2601.11134v1#bib.bib12) . Modern systems increasingly adopt machine learning and deep learning to improve predictive accuracy and capture nonlinear pattern [baesens2023boosting](https://arxiv.org/html/2601.11134v1#bib.bib12) ; [zhao2015investigation](https://arxiv.org/html/2601.11134v1#bib.bib14) ; [mahbobi2023credit](https://arxiv.org/html/2601.11134v1#bib.bib15) . Recent studies also demonstrate that alternative data sources such as telecom usage, utility payments, and online spending strengthen credit risk models, particularly for thin-file borrowers [djeundje2021enhancing](https://arxiv.org/html/2601.11134v1#bib.bib16) ; [cornelli2023fintech](https://arxiv.org/html/2601.11134v1#bib.bib17) . Despite such progress, classical PD models face structural limitations. Most are framed as binary classification [koutanaei2015hybrid](https://arxiv.org/html/2601.11134v1#bib.bib18) ; [fernandes2016spatial](https://arxiv.org/html/2601.11134v1#bib.bib19) ; [croux2020important](https://arxiv.org/html/2601.11134v1#bib.bib20) , where target variables are defined within a fixed observation horizon (e.g., 90 days past due within 12 months [choy2011markov](https://arxiv.org/html/2601.11134v1#bib.bib21) ; [brezigar2021modeling](https://arxiv.org/html/2601.11134v1#bib.bib22) ). Both academic research and industry practice typically ignore default timing, failing to distinguish early from late defaulters. For example, as shown in Figure [2](https://arxiv.org/html/2601.11134v1#S1.F2 "Figure 2 ‣ 1 Introduction ‣ FSL-BDP: Federated Survival Learning with Bayesian Differential Privacy for Credit Risk Modeling"), a rule that defines default as “90 DPD ever in 12 months” would label C3 and C5 as defaults but ignore C8, where the borrower defaults after the 12-month window. Early repayment cases like C1 are also commonly excluded from training, which removes useful behavioral signals. Current approaches fail to account for profitability because they treat C3 and C5 as equivalent despite meaningful differences in default timing. This issue is more pronounced in small-ticket, short-tenor loans, where LGD and EAD models are rarely used. These weaknesses reduce both decision accuracy and economic interpretability ([bellotti2009support,](https://arxiv.org/html/2601.11134v1#bib.bib23) ; [dirick2017time,](https://arxiv.org/html/2601.11134v1#bib.bib24) ). To address these challenges, this paper investigates two research questions:
(Q1) How can decision support systems distinguish early defaulters from late defaulters to enable risk-adjusted pricing and provisioning decisions that reflect differential loss severity across loan tenure? and (Q2) How can we model defaults beyond the traditional observation
window, overcoming the truncation limitations of classification-based PD models?

![Refer to caption](Fig/Loan_Tenure_Survival_view.jpg)


Figure 2: Time-to-event over loan tenure

Additionally, data protection regulations are reshaping the lending landscape. Privacy, data-residency, and responsible-AI rules increasingly limit cross-border and cross-institutional movement of borrower data. Frameworks such as GDPR in Europe [horobets2025artificial](https://arxiv.org/html/2601.11134v1#bib.bib25) , CCPA in the United States [varma2025federated](https://arxiv.org/html/2601.11134v1#bib.bib26) , and supervisory guidance from authorities including the EBA and MAS [tan2023data](https://arxiv.org/html/2601.11134v1#bib.bib27)  constrain the central storage of sensitive attributes. As a result, consolidating data at a central hub is increasingly infeasible, even when larger pooled datasets would improve model quality. This creates fundamental challenges for financial institutions that require richer, more accurate models while complying with strict privacy and security requirements. Hence, we investigate two additional research questions: (Q3) How can federated architectures enable collaborative decision support across institutions by learning repayment patterns across multiple geographies without exchanging raw data, while maintaining privacy and data security? and (Q4) Under realistic non-IID client distributions and privacy controls, can a federated survival approach meet predefined performance and calibration thresholds, without unacceptable degradation relative to a centralized benchmark?

Federated learning offers a promising response to the data-sharing constraints, as it trains models where data reside and aggregates only model updates rather than raw observations [mcmahan2017communication](https://arxiv.org/html/2601.11134v1#bib.bib28) . Building on this rationale, we propose a Federated Survival Learning (FSL) framework that models time-to-default and trains collaboratively across institutions while keeping raw data local. The survival formulation preserves timing information and handles censoring naturally. The federated architecture enables cross-silo learning that respects data-residency constraints. We further strengthen the framework with Bayesian differential privacy mechanisms to bound information leakage under data-dependent privacy guarantees.

Despite progress in federated learning for classification-based credit scoring [shingi2020federated](https://arxiv.org/html/2601.11134v1#bib.bib29) ; [wang2024novel](https://arxiv.org/html/2601.11134v1#bib.bib30) ; [li2024dynamic](https://arxiv.org/html/2601.11134v1#bib.bib31) , no prior work has addressed federated survival analysis with formal privacy guarantees for time-to-default modeling. This paper bridges three research streams: (i) credit scoring and ML-based decision support, (ii) survival analysis for risk modeling, and (iii) federated and privacy-preserving machine learning. The key contributions are as follows:

* •

  We adopt a survival-based credit risk formulation that distinguishes early and late defaulters, allowing the model to capture how default risk evolves over time.
* •

  We develop a federated survival learning framework, FSL-BDP, that enables collaborative model training across multiple financial institutions and geographic regions while providing Bayesian privacy guarantees through Bayesian Differential Privacy (BDP). The framework perturbs client-level gradient information using a Bayesian privacy accounting mechanism, thereby reducing inferential privacy risks such as membership and attribute inference attacks. FSL-BDP is explicitly designed to operate under realistic non-IID data distributions that arise naturally in cross-institutional credit datasets. To the best of our knowledge, this study represents the first application of Bayesian Differential Privacy within a Federated survival analysis setting.
* •

  We evaluate FSL-BDP on three real-world credit risk datasets, namely, LendingClub, SBA, and Bondora, using both in-time (ITV) and out-of-time (OOT) validation under federated, privacy-constrained, and natural non-IID settings. The results show that BDP provides a better privacy-utility trade-off than classical DP and fundamentally alters the relative effectiveness of privacy mechanisms. This indicates that privacy mechanism selection should be evaluated in the target deployment architecture rather than on centralized benchmarks.

We emphasize that our privacy guarantees are based on Bayesian Differential Privacy, which provides distribution-dependent protection rather than worst-case guarantees. While this distinction is important for regulatory interpretation, BDP has been shown to offer substantially improved utility in complex FL settings.

The remainder of this paper is organized as follows. Section [2](https://arxiv.org/html/2601.11134v1#S2 "2 Related Work ‣ FSL-BDP: Federated Survival Learning with Bayesian Differential Privacy for Credit Risk Modeling") reviews related work on credit scoring, survival analysis, federated learning, and privacy-preserving methods. Section [3](https://arxiv.org/html/2601.11134v1#S3 "3 Methodologies ‣ FSL-BDP: Federated Survival Learning with Bayesian Differential Privacy for Credit Risk Modeling") details the proposed methodology, including the Federated Survival Learning framework and optimization techniques. Section [4](https://arxiv.org/html/2601.11134v1#S4 "4 Experimental Setup ‣ FSL-BDP: Federated Survival Learning with Bayesian Differential Privacy for Credit Risk Modeling") describes the experimental design and datasets. Section [5](https://arxiv.org/html/2601.11134v1#S5 "5 Experimental Results and Analysis ‣ FSL-BDP: Federated Survival Learning with Bayesian Differential Privacy for Credit Risk Modeling") reports the empirical results, while Section [6](https://arxiv.org/html/2601.11134v1#S6 "6 Discussion ‣ FSL-BDP: Federated Survival Learning with Bayesian Differential Privacy for Credit Risk Modeling") discusses the findings, managerial implications, and directions for future research. We finally present the conclusions in Section [7](https://arxiv.org/html/2601.11134v1#S7 "7 Conclusion ‣ FSL-BDP: Federated Survival Learning with Bayesian Differential Privacy for Credit Risk Modeling").

## 2 Related Work

The rapid growth of digital lending has been extensively
documented [cornelli2023fintech](https://arxiv.org/html/2601.11134v1#bib.bib17) ; [suryono2019peer](https://arxiv.org/html/2601.11134v1#bib.bib32) , alongside the continued expansion of data-driven decision-making and AI in lending [kowsar2023credit](https://arxiv.org/html/2601.11134v1#bib.bib9) ; [sadok2022artificial](https://arxiv.org/html/2601.11134v1#bib.bib33) ; [cao2020ai](https://arxiv.org/html/2601.11134v1#bib.bib34) . Credit scoring has been central to lending decisions for decades [baesens2023boosting](https://arxiv.org/html/2601.11134v1#bib.bib12) ; [baesens2014analytics](https://arxiv.org/html/2601.11134v1#bib.bib13) ; [klimowicz2021concept](https://arxiv.org/html/2601.11134v1#bib.bib35)  and has evolved significantly over the past three to four decades. The field began with expert-assigned scorecards ([clauser1995scoring,](https://arxiv.org/html/2601.11134v1#bib.bib36) ; [mays1995handbook,](https://arxiv.org/html/2601.11134v1#bib.bib37) ), progressed through traditional statistical models such as logistic regression, and advanced to tree-based ensembles machine learning ([li2020comparative,](https://arxiv.org/html/2601.11134v1#bib.bib38) ; [wang2011comparative,](https://arxiv.org/html/2601.11134v1#bib.bib39) ) (e.g., AdaBoost, XGBoost ([qin2021xgboost,](https://arxiv.org/html/2601.11134v1#bib.bib40) ), LightGBM ([lextrait2023scaling,](https://arxiv.org/html/2601.11134v1#bib.bib41) ), random forests ([zhang2018novel,](https://arxiv.org/html/2601.11134v1#bib.bib42) ; [arora2020bolasso,](https://arxiv.org/html/2601.11134v1#bib.bib43) )) and deep learning ([zhang2020deep,](https://arxiv.org/html/2601.11134v1#bib.bib44) ) to capture high-dimensional, nonlinear borrower signals. Substantial recent literature suggests that predictive lift now more
often arises from stronger feature engineering [stevenson2021value](https://arxiv.org/html/2601.11134v1#bib.bib45) ; [boughaci2018new](https://arxiv.org/html/2601.11134v1#bib.bib46) ; [koutanaei2015hybrid](https://arxiv.org/html/2601.11134v1#bib.bib18) , calibrated probability estimates,
and rigorous validation rather than from model complexity alone. Regulators and risk functions increasingly expect transparent reasoning artifacts such as SHAP and LIME explanations [chen2024interpretable](https://arxiv.org/html/2601.11134v1#bib.bib47) , alongside fairness considerations [moldovan2023algorithmic](https://arxiv.org/html/2601.11134v1#bib.bib48) ; [kozodoi2022fairness](https://arxiv.org/html/2601.11134v1#bib.bib49)  and accuracy measures. Surveys and empirical work also document growing reliance on alternative data such as rent and utilities, telco, and e-commerce spend to score thin-file borrowers and promote inclusion ([djeundje2021enhancing,](https://arxiv.org/html/2601.11134v1#bib.bib16) ; [oskarsdottir2019value,](https://arxiv.org/html/2601.11134v1#bib.bib50) ; [fernandes2016spatial,](https://arxiv.org/html/2601.11134v1#bib.bib19) ), while cautioning about drift, disparate impact, and operational risks, including data privacy, in large-scale deployment [amed2025pdx](https://arxiv.org/html/2601.11134v1#bib.bib51) . A common pattern in prior credit scoring research is framing default prediction as a binary classification task [lessmann2015benchmarking](https://arxiv.org/html/2601.11134v1#bib.bib52) ; [moscato2021benchmark](https://arxiv.org/html/2601.11134v1#bib.bib53) , estimating the likelihood of default (e.g., 30+/60+/90+ days past due) within a fixed observation window. This formulation overlooks the time-to-default dimension that lenders need to distinguish early from late defaulters, motivating survival-based approaches.

Table 1: Summary of related work in credit scoring, survival analysis, and federated learning

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Study | Class. | Surv. | Fed. | Privacy | Non-IID | Domain |
| Credit Scoring (Classification) | | | | | | |
| Hsieh et al. (2010) [hsieh2010data](https://arxiv.org/html/2601.11134v1#bib.bib54) | ✓ | – | – | – | – | Credit |
| Lessmann et al. (2015) [lessmann2015benchmarking](https://arxiv.org/html/2601.11134v1#bib.bib52) | ✓ | – | – | – | – | Credit |
| Papouskova et al. (2019) [papouskova2019two](https://arxiv.org/html/2601.11134v1#bib.bib55) | ✓ | – | – | – | – | Credit |
| Gunnarsson et al. (2021) [gunnarsson2021deep](https://arxiv.org/html/2601.11134v1#bib.bib56) | ✓ | – | – | – | – | Credit |
| Survival Analysis (Centralized) | | | | | | |
| Dirick et al. (2017) [dirick2017time](https://arxiv.org/html/2601.11134v1#bib.bib24) | – | ✓ | – | – | – | Credit |
| Xia et al. (2021) [xia2021dynamic](https://arxiv.org/html/2601.11134v1#bib.bib57) | – | ✓ | – | – | – | Credit |
| Bai et al. (2022) [bai2022gradient](https://arxiv.org/html/2601.11134v1#bib.bib58) | – | ✓ | – | – | – | Credit |
| Blumenstock et al. (2022) [blumenstock2022deep](https://arxiv.org/html/2601.11134v1#bib.bib59) | – | ✓ | – | – | – | Credit |
| Medina-Olivares et al. (2023) [medina2023joint](https://arxiv.org/html/2601.11134v1#bib.bib60) | – | ✓ | – | – | – | Credit |
| Federated Credit Scoring | | | | | | |
| Shingi et al. (2020) [shingi2020federated](https://arxiv.org/html/2601.11134v1#bib.bib29) | ✓ | – | ✓ | – | – | Credit |
| He et al. (2023) [he2023privacy](https://arxiv.org/html/2601.11134v1#bib.bib61) | ✓ | – | ✓ | – | – | Credit |
| Wang et al. (2024) [wang2024novel](https://arxiv.org/html/2601.11134v1#bib.bib30) | ✓ | – | ✓ | – | – | Credit |
| Li et al. (2024) [li2024dynamic](https://arxiv.org/html/2601.11134v1#bib.bib31) | ✓ | – | ✓ | – | – | Credit |
| Federated Survival Learning | | | | | | |
| Andreux et al. (2020) [andreux2020federated](https://arxiv.org/html/2601.11134v1#bib.bib62) | – | ✓ | ✓ | – | – | Health |
| Rahman et al. (2023) [rahman2023fedpseudo](https://arxiv.org/html/2601.11134v1#bib.bib63) | – | ✓ | ✓ | – | ✓ | Health |
| Archetti et al. (2023) [archetti2023federated](https://arxiv.org/html/2601.11134v1#bib.bib64) | – | ✓ | ✓ | – | – | Health |
| Wen et al. (2025) [wen2025federated](https://arxiv.org/html/2601.11134v1#bib.bib65) | – | ✓ | ✓ | Classical | – | Health |
| Veeraragavan et al. (2025) [veeraragavan2024differentially](https://arxiv.org/html/2601.11134v1#bib.bib66) | – | ✓ | ✓ | Classical | – | Health |
| This work (FSL-BDP) | – | ✓ | ✓ | BDP | ✓ | Credit |

Notes: Class. = Classification; Surv. = Survival analysis; Fed. = Federated learning; BDP = Bayesian differential privacy. ✓\checkmark = work present; – = work absent. To our knowledge, this work is the first to combine federated survival analysis with Bayesian differential privacy for credit risk modeling.

Survival analysis has been extensively used in medicine since the middle of the last century, with major advances including the Kaplan–Meier estimator and Cox’s proportional hazards model [kaplan1958nonparametric](https://arxiv.org/html/2601.11134v1#bib.bib67) ; [cox1972regression](https://arxiv.org/html/2601.11134v1#bib.bib68) . Narain [narain1992survival](https://arxiv.org/html/2601.11134v1#bib.bib69)  first introduced survival models to credit risk, highlighting their ability to estimate not only whether but also when a borrower will default. Subsequent work applied Cox proportional hazards and accelerated failure time models to capture borrower-specific risk over time [dirick2017time](https://arxiv.org/html/2601.11134v1#bib.bib24) ; [hassan2018modeling](https://arxiv.org/html/2601.11134v1#bib.bib70) . More flexible specifications include spline-based hazards for nonlinear effects [luo2016spline](https://arxiv.org/html/2601.11134v1#bib.bib71)  and mixture-cure models that distinguish likely defaulters from borrowers who are unlikely to default within the loan horizon [tong2012mixture](https://arxiv.org/html/2601.11134v1#bib.bib72) . Recent studies further advanced performance using boosted tree-based survival methods [xia2021dynamic](https://arxiv.org/html/2601.11134v1#bib.bib57) ; [bai2022gradient](https://arxiv.org/html/2601.11134v1#bib.bib58)  and neural survival networks for time-to-default modeling [blumenstock2022deep](https://arxiv.org/html/2601.11134v1#bib.bib59) . Joint models combining longitudinal behavioral data with survival outcomes have also been proposed [medina2023joint](https://arxiv.org/html/2601.11134v1#bib.bib60) . Despite these advantages, survival analysis is still less commonly adopted in production credit scoring systems, and most existing implementations assume centralized training, raising data-privacy concerns under tightening regulatory requirements.

The foundational work on federated learning (FL) originated at Google, where models were trained locally on mobile devices and aggregated using Federated Averaging (FedAvg) [mcmahan2017communication](https://arxiv.org/html/2601.11134v1#bib.bib28) ; [hard2018federated](https://arxiv.org/html/2601.11134v1#bib.bib73) . Since then, FL has emerged as a prominent paradigm in privacy-sensitive domains such as healthcare and finance, enabling multi-institution collaboration without centralizing raw data. In credit risk, Shingi [shingi2020federated](https://arxiv.org/html/2601.11134v1#bib.bib29)  demonstrated federated logistic regression for credit scoring, while Wang et al. [wang2024novel](https://arxiv.org/html/2601.11134v1#bib.bib30)  proposed federated knowledge transfer combining fine-tuning and knowledge distillation. Li et al. [li2024dynamic](https://arxiv.org/html/2601.11134v1#bib.bib31)  introduced dynamic receptive fields for federated credit assessment. As summarized in Table [1](https://arxiv.org/html/2601.11134v1#S2.T1 "Table 1 ‣ 2 Related Work ‣ FSL-BDP: Federated Survival Learning with Bayesian Differential Privacy for Credit Risk Modeling"), existing federated learning research in credit risk is largely confined to classification-based probability-of-default models and typically lacks formal privacy guarantees, while survival-based and privacy-aware federated approaches have seen limited adoption in financial risk modeling, leaving time-to-default learning under realistic non-IID financial data largely unexplored.

Differential privacy (DP) has become the standard for providing formal privacy guarantees in machine learning, with DP-SGD [abadi2016deep](https://arxiv.org/html/2601.11134v1#bib.bib74)  offering a principled mechanism for private gradient-based optimization. However, DP-SGD introduces a substantial privacy–utility trade-off: worst-case noise calibration required to satisfy (ε,δ)(\varepsilon,\delta)-DP can significantly degrade model performance, particularly under strict privacy budgets [wei2020federated](https://arxiv.org/html/2601.11134v1#bib.bib75) ; [triastcyn2019federated](https://arxiv.org/html/2601.11134v1#bib.bib76) . Bayesian differential privacy (BDP) has been proposed to address this limitation by leveraging data-dependent privacy accounting rather than worst-case bounds, enabling tighter privacy guarantees with reduced noise injection [triastcyn2019federated](https://arxiv.org/html/2601.11134v1#bib.bib76) ; [triastcyn2020bayesian](https://arxiv.org/html/2601.11134v1#bib.bib77) . Triastcyn and Faltings [triastcyn2019federated](https://arxiv.org/html/2601.11134v1#bib.bib76)  demonstrated the benefits of BDP in federated image classification, showing improved utility retention relative to classical DP-SGD. However, BDP has thus far been studied primarily in classification tasks on image data, and its application to survival analysis, particularly for time-to-default modeling in credit risk, has not been examined.

Our work addresses this gap by integrating Bayesian differential privacy with federated survival learning, employing leave-one-out gradient estimation and pairwise Rényi divergence to achieve strong privacy guarantees while preserving predictive utility. To our knowledge, this is the first study to apply Bayesian differential privacy to survival analysis, and the first to do so in the context of federated credit risk modeling.

## 3 Methodologies

This section presents the proposed federated survival analysis framework with Bayesian differential privacy (BDP) guarantees. We begin with centralized survival modeling as a baseline, then progressively introduce federated learning and privacy-preserving mechanisms, culminating in our novel Bayesian DP approach to model time-to-default for credit risk assessment.

### 3.1 Problem Formulation

Consider a federated credit risk setting with KK participating institutions (clients), where the kk-th client possesses a local dataset 𝒟k={(𝐱i(k),ti(k),δi(k))}i=1nk\mathcal{D}\_{k}=\{(\mathbf{x}\_{i}^{(k)},t\_{i}^{(k)},\delta\_{i}^{(k)})\}\_{i=1}^{n\_{k}}, where 𝐱i(k)∈ℝd\mathbf{x}\_{i}^{(k)}\in\mathbb{R}^{d} denotes the dd-dimensional borrower covariate vector at client kk, ti(k)∈ℝ+t\_{i}^{(k)}\in\mathbb{R}^{+} represents the observed time-to-default or censoring, and δi(k)∈{0,1}\delta\_{i}^{(k)}\in\{0,1\} is the event indicator, where δi(k)=1\delta\_{i}^{(k)}=1 indicates default occurrence and δi(k)=0\delta\_{i}^{(k)}=0 denotes right censoring.

The global dataset comprises N=∑k=1KnkN=\sum\_{k=1}^{K}n\_{k} observations, where nkn\_{k} is number of observations at client k. The objective is to learn a global survival model fθ:ℝd→[0,1]Tf\_{\theta}:\mathbb{R}^{d}\to[0,1]^{T} that predicts discrete-time survival probabilities at TT time intervals, while providing formal differential privacy guarantees for individual-level data.

We establish baseline using discrete-time survival analysis with neural networks, following the framework of ([kvamme2019time,](https://arxiv.org/html/2601.11134v1#bib.bib78) ; [gensheimer2019scalable,](https://arxiv.org/html/2601.11134v1#bib.bib79) ) for both centralized and federated learning.

### 3.2 Discrete-Time Survival Likelihood

Since loan repayments occur monthly, we model time in discrete form using TT ordered, left-closed and right-open intervals,

|  |  |  |
| --- | --- | --- |
|  | 0=τ0<τ1<⋯<τT<∞.0=\tau\_{0}<\tau\_{1}<\cdots<\tau\_{T}<\infty. |  |

Let hl(k)​(𝐱)h\_{l}^{(k)}(\mathbf{x}) denote the discrete-time hazard probability for a borrower
at client kk in interval (τl−1,τl](\tau\_{l-1},\tau\_{l}], defined as

|  |  |  |
| --- | --- | --- |
|  | hl(k)​(𝐱)=P​(t∈(τl−1,τl]​∣t>​τl−1,𝐱,k),l=1,…,T.h\_{l}^{(k)}(\mathbf{x})=P\!\left(t\in(\tau\_{l-1},\tau\_{l}]\mid t>\tau\_{l-1},\mathbf{x},k\right),\qquad l=1,\ldots,T. |  |

This formulation does not impose the proportional hazards assumption and allows for flexible,
time-varying default dynamics. The corresponding survival function up to the end of interval ll is

|  |  |  |
| --- | --- | --- |
|  | Sl(k)​(𝐱)=P​(t>τl∣𝐱)=∏j=1l(1−hj(k)​(𝐱)).S\_{l}^{(k)}(\mathbf{x})=P(t>\tau\_{l}\mid\mathbf{x})=\prod\_{j=1}^{l}\big(1-h\_{j}^{(k)}(\mathbf{x})\big). |  |

#### Individual Likelihood:

Let jj denote the interval such that t∈(τj−1,τj]t\in(\tau\_{j-1},\tau\_{j}]. If an uncensored individual experiences the event in interval jj, the likelihood is

|  |  |  |
| --- | --- | --- |
|  | ℒ=hj(k)​(𝐱)​∏l=1j−1(1−hl(k)​(𝐱)).\mathcal{L}=h\_{j}^{(k)}(\mathbf{x})\prod\_{l=1}^{j-1}\big(1-h\_{l}^{(k)}(\mathbf{x})\big). |  |

For a right-censored individual with censoring occurring in interval jj, the likelihood is

|  |  |  |
| --- | --- | --- |
|  | ℒ=∏l=1j(1−hl(k)​(𝐱)).\mathcal{L}=\prod\_{l=1}^{j}\big(1-h\_{l}^{(k)}(\mathbf{x})\big). |  |

#### Likelihood Representation:

For computational convenience, each individual is represented using two binary vectors:
𝐬surv∈{0,1}T\mathbf{s}^{\text{surv}}\in\{0,1\}^{T} and 𝐬fail∈{0,1}T\mathbf{s}^{\text{fail}}\in\{0,1\}^{T}.
The vector 𝐬surv\mathbf{s}^{\text{surv}} indicates the intervals through which the individual has survived, and 𝐬fail\mathbf{s}^{\text{fail}} indicates the interval in which failure occurs.

For an uncensored individual with event time t∈(τl−1,τl]t\in(\tau\_{l-1},\tau\_{l}],

|  |  |  |
| --- | --- | --- |
|  | slsurv={1,t≥τl,0,otherwise,slfail={1,τl−1≤t<τl,0,otherwise.s^{\text{surv}}\_{l}=\begin{cases}1,&t\geq\tau\_{l},\\ 0,&\text{otherwise},\end{cases}\hskip 18.49988pts^{\text{fail}}\_{l}=\begin{cases}1,&\tau\_{l-1}\leq t<\tau\_{l},\\ 0,&\text{otherwise}.\end{cases} |  |

For a right-censored individual with censoring time tt, the survival indicator vector
𝐬surv\mathbf{s}^{\text{surv}} is defined using the midpoint convention:

|  |  |  |
| --- | --- | --- |
|  | slsurv={1,if ​t≥τi−1+τi2,0,otherwise,slfail=0.s^{\text{surv}}\_{l}=\begin{cases}1,&\text{if }t\geq\dfrac{\tau\_{i-1}+\tau\_{i}}{2},\\ 0,&\text{otherwise},\end{cases}\hskip 18.49988pts^{\text{fail}}\_{l}=0. |  |

Using this representation, the individual log-likelihood can be written compactly as

|  |  |  |  |
| --- | --- | --- | --- |
|  | log⁡ℒ=∑l=1T[slsurv​log⁡(1−hl(k)​(𝐱))+slfail​log⁡hl(k)​(𝐱)].\log\mathcal{L}=\sum\_{l=1}^{T}\left[s^{\text{surv}}\_{l}\log\big(1-h\_{l}^{(k)}(\mathbf{x})\big)+s^{\text{fail}}\_{l}\log h\_{l}^{(k)}(\mathbf{x})\right]. |  | (1) |

The total loss is obtained by summing the negative log-likelihood in
Eq. ([1](https://arxiv.org/html/2601.11134v1#S3.E1 "In Likelihood Representation: ‣ 3.2 Discrete-Time Survival Likelihood ‣ 3 Methodologies ‣ FSL-BDP: Federated Survival Learning with Bayesian Differential Privacy for Credit Risk Modeling")) over all individuals and is minimized using stochastic or mini-batch
gradient descent.

#### Neural Network Architecture:

We parameterize the client-specific discrete-time hazard function using a neural network:

|  |  |  |  |
| --- | --- | --- | --- |
|  | hl(k)​(𝐱;θ)=σ​(fl​(𝐱;θ)),l=1,…,T,h\_{l}^{(k)}(\mathbf{x};\theta)=\sigma\!\left(f\_{l}(\mathbf{x};\theta)\right),\qquad l=1,\ldots,T, |  | (2) |

where σ​(⋅)\sigma(\cdot) denotes the sigmoid activation function, ensuring
hl(k)​(𝐱;θ)∈(0,1)h\_{l}^{(k)}(\mathbf{x};\theta)\in(0,1).

Specifically, we employ a feed-forward neural network whose output layer has TT units,
each corresponding to one discrete time interval:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐡(k)​(𝐱;θ)=σ​(𝐖L​ϕL−1​(𝐖L−1​ϕL​2​(⋯​ϕ1​(𝐖1​𝐱+𝐛1)​⋯)+𝐛L−1)+𝐛L),\mathbf{h}^{(k)}(\mathbf{x};\theta)=\sigma\!\left(\mathbf{W}\_{L}\,\phi\_{L-1}\!\left(\mathbf{W}\_{L-1}\,\phi\_{L2}\!\left(\cdots\phi\_{1}(\mathbf{W}\_{1}\mathbf{x}+\mathbf{b}\_{1})\cdots\right)+\mathbf{b}\_{L-1}\right)+\mathbf{b}\_{L}\right), |  | (3) |

where θ={𝐖l,𝐛l}l=1L\theta=\{\mathbf{W}\_{l},\mathbf{b}\_{l}\}\_{l=1}^{L} denotes the shared network parameters,
ϕl​(⋅)\phi\_{l}(\cdot) is the activation function of the ll-th hidden layer (e.g., SELU),
and σ​(⋅)\sigma(\cdot) is applied element-wise to ensure valid hazard probabilities.
The ll-th output node corresponds to the conditional hazard probability
hl(k)​(𝐱;θ)h\_{l}^{(k)}(\mathbf{x};\theta) for interval (τl−1,τl](\tau\_{l-1},\tau\_{l}].

![Refer to caption](x1.png)


Figure 3: Federated Differential Privacy

### 3.3 Federated Learning

Traditional centralized machine learning requires aggregating all client data on a single server, which is often infeasible in credit risk modeling due to strict privacy, security, and regulatory constraints. Federated Learning (FL), introduced by [mcmahan2017communication](https://arxiv.org/html/2601.11134v1#bib.bib28) ; [hard2018federated](https://arxiv.org/html/2601.11134v1#bib.bib73) , addresses these challenges by enabling collaborative model training without sharing raw data. In FL, each client locally trains a survival model on its private credit portfolio and transmits only model updates to a central server. The server aggregates these updates typically via weighted averaging to obtain a global model, which is then redistributed to clients for the next training round. This iterative process preserves data locality while enabling collective learning across distributed institutions. The standard FL architecture with differential privacy is illustrated in Figure [3](https://arxiv.org/html/2601.11134v1#S3.F3 "Figure 3 ‣ Neural Network Architecture: ‣ 3.2 Discrete-Time Survival Likelihood ‣ 3 Methodologies ‣ FSL-BDP: Federated Survival Learning with Bayesian Differential Privacy for Credit Risk Modeling").

In real-world credit risk modeling, borrower populations, default dynamics, and censoring mechanisms vary substantially across financial institutions and geographic regions. As a result, the client-level datasets
{𝒟k}k=1K\{\mathcal{D}\_{k}\}\_{k=1}^{K} are generally *non-independently and identically distributed (non-IID)*. We assume that, for each client kk, the observed triples
(𝐱i(k),ti(k),δi(k))(\mathbf{x}\_{i}^{(k)},t\_{i}^{(k)},\delta\_{i}^{(k)}), i=1,…,nki=1,\ldots,n\_{k},
are independently drawn from a client-specific joint distribution

|  |  |  |
| --- | --- | --- |
|  | (𝐱(k),t(k),δ(k))∼𝒫k,(\mathbf{x}^{(k)},t^{(k)},\delta^{(k)})\sim\mathcal{P}\_{k}, |  |

where, in general,

|  |  |  |
| --- | --- | --- |
|  | 𝒫k≠𝒫j​for ​k≠j.\mathcal{P}\_{k}\neq\mathcal{P}\_{j}\qquad\text{for }k\neq j. |  |

Under this setting, the local survival risk at client kk is defined as

|  |  |  |
| --- | --- | --- |
|  | ℒk​(θ)=𝔼(𝐱(k),t(k),δ(k))∼𝒫k​[ℓ​(𝐱(k),t(k),δ(k);θ)],\mathcal{L}\_{k}(\theta)=\mathbb{E}\_{(\mathbf{x}^{(k)},t^{(k)},\delta^{(k)})\sim\mathcal{P}\_{k}}\left[\ell\big(\mathbf{x}^{(k)},t^{(k)},\delta^{(k)};\theta\big)\right], |  |

while the global federated objective minimizes a mixture risk

|  |  |  |
| --- | --- | --- |
|  | ℒ​(θ)=∑k=1Kπk​ℒk​(θ),πk=nk∑j=1Knj.\mathcal{L}(\theta)=\sum\_{k=1}^{K}\pi\_{k}\mathcal{L}\_{k}(\theta),\qquad\pi\_{k}=\frac{n\_{k}}{\sum\_{j=1}^{K}n\_{j}}. |  |

This formulation explicitly acknowledges that federated survival learning optimizes a shared model across heterogeneous credit populations, rather than assuming identical data-generating processes across clients.

### 3.4 Differential Privacy

Although Federated Learning keeps raw credit data localized at client institutions, it does not fully eliminate privacy risks. In particular, sensitive information may still be inferred from the model updates transmitted to the central server, for example, through gradient leakage or membership inference attacks [dwork2014algorithmic](https://arxiv.org/html/2601.11134v1#bib.bib80) ; [wei2020federated](https://arxiv.org/html/2601.11134v1#bib.bib75) . Therefore, formal privacy guarantees are required when training federated survival models on sensitive time-to-event credit data. Differential Privacy provides such guarantees by quantifying how much the output of a learning algorithm changes when a single data point in the training dataset is modified [abadi2016deep](https://arxiv.org/html/2601.11134v1#bib.bib74) .

###### Definition 3.1 ((ϵ,δ\epsilon,\delta)-Differential Privacy [abadi2016deep](https://arxiv.org/html/2601.11134v1#bib.bib74) )

A randomized mechanism ℳ:𝒟→ℛ\mathcal{M}:\mathcal{D}\to\mathcal{R} satisfies (ϵ,δ)(\epsilon,\delta)-differential privacy if for all neighboring datasets 𝒟,𝒟′\mathcal{D},\mathcal{D}^{\prime} differing in one record, and for all measurable sets S⊆ℛS\subseteq\mathcal{R}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | P​(ℳ​(𝒟)∈S)≤eϵ⋅P​(ℳ​(𝒟′)∈S)+δ.P(\mathcal{M}(\mathcal{D})\in S)\leq e^{\epsilon}\cdot P(\mathcal{M}(\mathcal{D}^{\prime})\in S)+\delta. |  | (4) |

Here, ϵ>0\epsilon>0 controls the strength of the privacy guarantee, with smaller values implying stronger privacy protection, while δ≥0\delta\geq 0 denotes the probability of privacy failure and is typically required to be negligible, often less than 1/|𝒟|1/|\mathcal{D}| [dwork2014algorithmic](https://arxiv.org/html/2601.11134v1#bib.bib80) . Setting δ=0\delta=0 recovers pure ϵ\epsilon-differential privacy.

To enforce DP in deep neural networks, including survival models trained in federated settings, DP-SGD [abadi2016deep](https://arxiv.org/html/2601.11134v1#bib.bib74)  modifies standard stochastic gradient descent by clipping per-sample gradients and injecting Gaussian noise. Specifically, for a mini-batch of size LL, the sanitized gradient at iteration rr is computed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐠𝐫~​(𝐱𝐢)=1L​(∑i=1L𝐠𝐫​(𝐱𝐢)max⁡(1,‖𝐠𝐫​(𝐱𝐢)‖2C)+𝒩​(0,σ2​C2​𝐈)),i=1,2,⋯,L,\mathbf{\tilde{g\_{r}}(x\_{i})}=\frac{1}{L}\Bigg(\sum\_{i=1}^{L}\frac{\mathbf{g\_{r}(x\_{i})}}{\max\left(1,\frac{||\mathbf{g\_{r}(x\_{i})}||\_{2}}{C}\right)}+\mathcal{N}(0,\sigma^{2}C^{2}\mathbf{I})\Bigg),~i=1,2,\cdots,L, |  | (5) |

where CC is the gradient clipping threshold and σ\sigma controls the noise magnitude. Each training iteration thus satisfies differential privacy, and the overall privacy budget across RR federated rounds is obtained via composition.

#### Privacy Accounting via Moments Accountant:

The privacy loss incurred during training accumulates across optimization steps.
Let RR denote the total number of optimization steps at which differential privacy is enforced
(e.g., local DP-SGD updates across federated training rounds), and let
q=B/nkq=B/n\_{k} be the subsampling rate, where BB is the mini-batch size and nkn\_{k} is the
dataset size at a given client.
Following the moments accountant framework ([abadi2016deep,](https://arxiv.org/html/2601.11134v1#bib.bib74) ; [geyer2017differentially,](https://arxiv.org/html/2601.11134v1#bib.bib81) ),
which can be equivalently expressed using Rényi Differential Privacy (RDP)
([mironov2017renyi,](https://arxiv.org/html/2601.11134v1#bib.bib82) ), we track the cumulative privacy loss throughout training.

#### Rényi Differential Privacy (RDP) ([mironov2017renyi,](https://arxiv.org/html/2601.11134v1#bib.bib82) ):

Under Poisson subsampling with rate qq, the Gaussian mechanism with noise scale σ\sigma
satisfies RDP at order α>1\alpha>1.
After RR compositions, the total RDP budget is bounded by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϵα​(R)≤R⋅α​q22​σ2+O​(R​q3),\epsilon\_{\alpha}(R)\leq R\cdot\frac{\alpha q^{2}}{2\sigma^{2}}+O(Rq^{3}), |  | (6) |

where higher-order terms become negligible for small subsampling rates.
The final (ϵ,δ)(\epsilon,\delta)-differential privacy guarantee is obtained via

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϵ=minα>1⁡{ϵα​(R)+log⁡(1/δ)α−1},\epsilon=\min\_{\alpha>1}\left\{\epsilon\_{\alpha}(R)+\frac{\log(1/\delta)}{\alpha-1}\right\}, |  | (7) |

which yields a tighter privacy bound than classical composition rules.
This privacy accounting mechanism forms the foundation upon which we build our Bayesian differential privacy (BDP) [triastcyn2020bayesian](https://arxiv.org/html/2601.11134v1#bib.bib77)  enhanced federated survival learning (FSL-BDP) framework for credit risk modeling.

### 3.5 Bayesian Differential Privacy Framework

Bayesian Differential Privacy (BDP) [triastcyn2020bayesian](https://arxiv.org/html/2601.11134v1#bib.bib77)  refines classical differential
privacy by measuring privacy loss in terms of posterior distributions over model parameters,
rather than worst-case differences in algorithm outputs.
Specifically, BDP quantifies how much an adversary’s posterior belief about the model parameters
can change after observing the output of a learning algorithm, given a prior belief and an
assumed data-generating distribution.

Unlike standard differential privacy, which enforces uniform guarantees over all possible
datasets, BDP assumes that data points are drawn i.i.d. from an underlying distribution.
This enables tighter, data-dependent privacy guarantees that are particularly well suited
to complex learning models. As a consequence, (ϵμ,δμ)(\epsilon\_{\mu},\delta\_{\mu})-BDP guarantees should be interpreted as average-case or high-probability bounds under the assumed data generating distribution, and are not equivalent to the worst-case (ϵ,δ)(\epsilon,\delta)-DP guarantees.

To the best of our knowledge, BDP has not been applied to federated survival analysis,
where privacy is critical due to sensitive time-to-event data and heterogeneous client populations.

###### Definition 3.2 (Bayesian Differential Privacy [triastcyn2020bayesian](https://arxiv.org/html/2601.11134v1#bib.bib77) )

A randomized learning algorithm 𝒜\mathcal{A} satisfies
(ϵμ,δμ)(\epsilon\_{\mu},\delta\_{\mu})-Bayesian Differential Privacy if for any two neighboring datasets
𝒟\mathcal{D} and 𝒟′\mathcal{D}^{\prime} differing in one sample drawn from μ​(x)\mu(x),
the privacy loss random variable

|  |  |  |
| --- | --- | --- |
|  | L​(θ;𝒟,𝒟′)=log⁡p​(θ∣𝒟)p​(θ∣𝒟′)L(\theta;\mathcal{D},\mathcal{D}^{\prime})=\log\frac{p(\theta\mid\mathcal{D})}{p(\theta\mid\mathcal{D}^{\prime})} |  |

satisfies

|  |  |  |  |
| --- | --- | --- | --- |
|  | Prθ∼𝒜​(𝒟)⁡[L​(θ;𝒟,𝒟′)≤ϵμ]≥1−δμ.\Pr\_{\theta\sim\mathcal{A}(\mathcal{D})}\left[L(\theta;\mathcal{D},\mathcal{D}^{\prime})\leq\epsilon\_{\mu}\right]\geq 1-\delta\_{\mu}. |  | (8) |

This formulation aligns naturally with federated survival learning, where privacy guarantees
are enforced at the model-parameter level while accommodating censored time-to-event data
and heterogeneous client distributions. The i.i.d. assumption applies locally within each client,
while allowing client-specific data-generating processes across the federation.

Algorithm 1  Federated Survival Learning with Bayesian Differential Privacy (FSL-BDP)

1:Number of clients KK; client datasets {𝒟k}k=1K\{\mathcal{D}\_{k}\}\_{k=1}^{K};
communication rounds RR; local epochs EE; client participation rate pp;
Bayesian DP parameters (σ,C,Λ,β,γ)(\sigma,C,\Lambda,\beta,\gamma)

2:Final global survival model θglobal(R)\theta\_{\text{global}}^{(R)};
per-client cumulative Bayesian DP guarantees {(ϵk,δk)}k=1K\{(\epsilon\_{k},\delta\_{k})\}\_{k=1}^{K}

3:Server: Initialize global model θglobal(0)\theta\_{\text{global}}^{(0)}

4:Initialize cumulative privacy costs:
ϵk←0,δk←0,∀k\epsilon\_{k}\leftarrow 0,\ \delta\_{k}\leftarrow 0,\ \forall k

5:for r=0r=0 to R−1R-1 do

6:  Server: Sample participating clients

|  |  |  |
| --- | --- | --- |
|  | 𝒮t∼Uniform​({1,…,K},⌊p​K⌋)\mathcal{S}\_{t}\sim\mathrm{Uniform}\big(\{1,\ldots,K\},\lfloor pK\rfloor\big) |  |

7:  Server: Broadcast global model θglobal(r)\theta\_{\text{global}}^{(r)} to all k∈𝒮rk\in\mathcal{S}\_{r}

8:  for each client k∈𝒮tk\in\mathcal{S}\_{t} in parallel do

9:   Initialize local model:
θk(r)←θglobal(r)\theta\_{k}^{(r)}\leftarrow\theta\_{\text{global}}^{(r)}

10:   

|  |  |  |
| --- | --- | --- |
|  | θk(r+1),(ϵk(r),δk(r))←BayesianDP\_Train​(θk(r),𝒟k,E,σ,C,Λ,β,γ)\theta\_{k}^{(r+1)},\,(\epsilon\_{k}^{(r)},\delta\_{k}^{(r)})\leftarrow\textsc{BayesianDP\\_Train}\big(\theta\_{k}^{(r)},\mathcal{D}\_{k},E,\sigma,C,\Lambda,\beta,\gamma\big) |  |

⊳\triangleright Bayesian DP-SGD, Alg. [2](https://arxiv.org/html/2601.11134v1#alg2 "Algorithm 2 ‣ Privacy Accounting: ‣ 3.5 Bayesian Differential Privacy Framework ‣ 3 Methodologies ‣ FSL-BDP: Federated Survival Learning with Bayesian Differential Privacy for Credit Risk Modeling")

11:   Update cumulative privacy:

|  |  |  |
| --- | --- | --- |
|  | ϵk←ϵk+ϵk(r),δk←δk+δk(r)\epsilon\_{k}\leftarrow\epsilon\_{k}+\epsilon\_{k}^{(r)},\qquad\delta\_{k}\leftarrow\delta\_{k}+\delta\_{k}^{(r)} |  |

12:   Upload privatized local model θk(r+1)\theta\_{k}^{(r+1)} to server

13:  end for

14:  Server: Aggregate received models (post-processing):

|  |  |  |
| --- | --- | --- |
|  | θglobal(r+1)=∑k∈𝒮r|𝒟k|∑j∈𝒮r|𝒟j|​θk(r+1)\theta\_{\text{global}}^{(r+1)}=\sum\_{k\in\mathcal{S}\_{r}}\frac{|\mathcal{D}\_{k}|}{\sum\_{j\in\mathcal{S}\_{r}}|\mathcal{D}\_{j}|}\,\theta\_{k}^{(r+1)} |  |

15:end for

16:return
θglobal(R)\theta\_{\text{global}}^{(R)},
{(ϵk,δk)}k=1K\{(\epsilon\_{k},\delta\_{k})\}\_{k=1}^{K}

#### Privacy Accounting:

Following ([triastcyn2020bayesian,](https://arxiv.org/html/2601.11134v1#bib.bib77) ), privacy loss is quantified by comparing the
distributions of noisy model updates produced by neighboring datasets that differ
in a single data point drawn from the underlying data-generating distribution.
Rather than relying on worst-case sensitivity, Bayesian Differential Privacy estimates
privacy loss by evaluating the Rényi divergence between the induced distributions
of model parameters (or gradients) under data inclusion and exclusion.

In practice, this is implemented by approximating the distributions of per-sample
(or sub-sampled) gradients and computing the corresponding Bayesian Rényi divergence
at order λ>1\lambda>1. Privacy loss is accumulated across local optimization steps
and federated communication rounds using Rényi composition. The accumulated Bayesian
Rényi privacy cost is then converted into an (ϵμ,δμ)(\epsilon\_{\mu},\delta\_{\mu}) guarantee
using the Bayesian DP tail bound of ([triastcyn2020bayesian,](https://arxiv.org/html/2601.11134v1#bib.bib77) ), given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | ϵμ​(λ)=Ctot​(λ)−log⁡βλ,δμ=β+γ,\epsilon\_{\mu}(\lambda)=\frac{C\_{\mathrm{tot}}(\lambda)-\log\beta}{\lambda},\hskip 18.49988pt\delta\_{\mu}=\beta+\gamma, |  | (9) |

where β\beta denotes the privacy failure probability, Ctot​(λ)C\_{\mathrm{tot}}(\lambda) denotes cumulative privacy cost, and γ\gamma accounts for
the Monte-Carlo estimation error. The final privacy level is obtained by minimizing
ϵμ​(λ)\epsilon\_{\mu}(\lambda) over λ>1\lambda>1. The Bayesian Differential privacy algorithm is given in Algorithm [2](https://arxiv.org/html/2601.11134v1#alg2 "Algorithm 2 ‣ Privacy Accounting: ‣ 3.5 Bayesian Differential Privacy Framework ‣ 3 Methodologies ‣ FSL-BDP: Federated Survival Learning with Bayesian Differential Privacy for Credit Risk Modeling").

Overall, Bayesian Differential Privacy enables tighter, data-aware privacy accounting
in federated learning and is particularly well suited for heterogeneous and non-IID
survival data.

Algorithm 2  Bayesian Differential Privacy: Bayesian DP-SGD

1:Dataset 𝒟k={xi}i=1nk\mathcal{D}\_{k}=\{x\_{i}\}\_{i=1}^{n\_{k}};
data-generating prior μ​(x)\mu(x);
initial parameters θ0\theta\_{0};
learning rate η\eta;
noise multiplier σ\sigma;
clipping norm CC;
batch size BB;
iterations EE;
Rényi orders Λ\Lambda;
Monte-Carlo samples MM;
estimator failure probability γ\gamma;
privacy failure probability β\beta

2:Final parameters θE\theta\_{E};
Bayesian DP guarantee (ϵμ,δμ=β+γ)(\epsilon\_{\mu},\delta\_{\mu}=\beta+\gamma)

3:Initialize model parameters θ←θ0\theta\leftarrow\theta\_{0}

4:for λ∈Λ\lambda\in\Lambda do

5:  Initialize cumulative privacy cost Ctot​(λ)←0C\_{\mathrm{tot}}(\lambda)\leftarrow 0

6:end for

7:for e=1e=1 to EE do

8:  Sample mini-batch Be⊂DB\_{e}\subset D uniformly without replacement

9:  Compute per-sample gradients {gi​(θ)}i∈Be\{g\_{i}(\theta)\}\_{i\in B\_{e}}

10:  Clip gradients: g¯i←gi/max⁡(1,‖gi‖2C)\bar{g}\_{i}\leftarrow g\_{i}/\max\!\left(1,\frac{\|g\_{i}\|\_{2}}{C}\right)

11:  Compute averaged gradient: ge←1|Bt|​∑i∈Beg¯ig\_{e}\leftarrow\frac{1}{|B\_{t}|}\sum\_{i\in B\_{e}}\bar{g}\_{i}

12:  Sample noise ξe∼𝒩​(0,σ2​C2​I)\xi\_{e}\sim\mathcal{N}(0,\sigma^{2}C^{2}I)

13:  Update parameters: θ←θ−η​(ge+ξe)\theta\leftarrow\theta-\eta(g\_{e}+\xi\_{e})

14:// Monte-Carlo Bayesian Sensitivity Estimation

15:  for m=1m=1 to MM do

16:   Sample alternative data point x′⁣(m)∼μx^{\prime(m)}\sim\mu

17:   Construct neighboring batch Be(m)B\_{e}^{(m)} by replacing one element of BeB\_{e} with x′⁣(m)x^{\prime(m)}

18:   Compute clipped averaged gradient ge(m)g\_{e}^{(m)}

19:   Compute squared deviation: Δe(m)←‖ge−ge(m)‖22\Delta\_{e}^{(m)}\leftarrow\|g\_{e}-g\_{e}^{(m)}\|\_{2}^{2}

20:  end for

21:// Bayesian Privacy Accounting

22:  Set subsampling rate q←BNq\leftarrow\frac{B}{N}

23:  for λ∈Λ\lambda\in\Lambda do

24:   for m=1m=1 to MM do

25:      Compute left privacy cost:ce,L​e​f​t(m)​(λ)←log⁡𝔼K∼Bin​(λ+1,q)​[exp⁡(K2−K2​σ2​Δe(m))]c\_{e,Left}^{(m)}(\lambda)\leftarrow\log\mathbb{E}\_{K\sim\mathrm{Bin}(\lambda+1,q)}\left[\exp\!\left(\frac{K^{2}-K}{2\sigma^{2}}\Delta\_{e}^{(m)}\right)\right]

26:      Compute right privacy cost: ce,R​i​g​h​t(m)​(λ)←log⁡𝔼K∼Bin​(λ,q)​[exp⁡(K2+K2​σ2​Δe(m))]c\_{e,Right}^{(m)}(\lambda)\leftarrow\log\mathbb{E}\_{K\sim\mathrm{Bin}(\lambda,q)}\left[\exp\!\left(\frac{K^{2}+K}{2\sigma^{2}}\Delta\_{e}^{(m)}\right)\right]

27:      Set per-sample cost:

|  |  |  |
| --- | --- | --- |
|  | c^e(m)​(λ)←max⁡{ce,L​e​f​t(m)​(λ),ce,R​i​g​h​t(m)​(λ)}\hat{c}\_{e}^{(m)}(\lambda)\leftarrow\max\{c\_{e,Left}^{(m)}(\lambda),c\_{e,Right}^{(m)}(\lambda)\} |  |

28:   end for

29:   Compute high-probability upper bound: c^e​(λ)←UCB1−γ​({c^e(m)​(λ)}m=1M)\hat{c}\_{e}(\lambda)\leftarrow\mathrm{UCB}\_{1-\gamma}\big(\{\hat{c}\_{e}^{(m)}(\lambda)\}\_{m=1}^{M}\big)

30:   Accumulate privacy cost:

|  |  |  |
| --- | --- | --- |
|  | Ctot​(λ)←Ctot​(λ)+c^e​(λ)C\_{\mathrm{tot}}(\lambda)\leftarrow C\_{\mathrm{tot}}(\lambda)+\hat{c}\_{e}(\lambda) |  |

31:  end for

32:end for

33:// Final Bayesian Differential Privacy Guarantee

34:for λ∈Λ\lambda\in\Lambda do

35:  Compute privacy bound: ϵμ​(λ)←Ctot​(λ)−log⁡βλ\epsilon\_{\mu}(\lambda)\leftarrow\frac{C\_{\mathrm{tot}}(\lambda)-\log\beta}{\lambda}

36:end for

37:Select optimal privacy level: ϵμ←minλ∈Λ⁡ϵμ​(λ)\epsilon\_{\mu}\leftarrow\min\_{\lambda\in\Lambda}\epsilon\_{\mu}(\lambda)

38:return θT\theta\_{T}, (ϵμ,δμ=β+γ)(\epsilon\_{\mu},\delta\_{\mu}=\beta+\gamma)

  

\*Note: In practice, this bound UCB1−γ\mathrm{UCB}\_{1-\gamma} can be obtained using a Bayesian posterior quantile.

In the remainder of this paper, classical (ϵ,δ)(\epsilon,\delta)-DP is used as a baseline, while our proposed framework employs Bayesian differential privacy with parameters (ϵμ,δμ)(\epsilon\_{\mu},\delta\_{\mu}).

### 3.6 Federated Survival Learning with Bayesian Differential Privacy

In this section, we adapt federated learning with Bayesian Differential Privacy
([triastcyn2020bayesian,](https://arxiv.org/html/2601.11134v1#bib.bib77) ) to a credit risk survival analysis framework,
providing tighter, data-aware privacy bounds than standard federated learning
with classical differential privacy.
Algorithm [1](https://arxiv.org/html/2601.11134v1#alg1 "Algorithm 1 ‣ 3.5 Bayesian Differential Privacy Framework ‣ 3 Methodologies ‣ FSL-BDP: Federated Survival Learning with Bayesian Differential Privacy for Credit Risk Modeling") summarizes the complete training
procedure for federated survival learning under Bayesian Differential Privacy,
highlighting the interaction between local survival optimization,
posterior-based privacy accounting, and global model aggregation. Bayesian privacy guarantees are enforced at the client level during local
optimization, while federated aggregation constitutes post-processing and does
not incur additional privacy loss.

## 4 Experimental Setup

This section describes the experiments for our proposed FSL credit risk estimation model. We outline the datasets, the objective function and target definition, the performance metrics, and the training and validation setup.

### 4.1 Dataset Description

We evaluate FSL-BDP on three real-world credit datasets spanning different lending contexts, geographies, and default dynamics. Table [2](https://arxiv.org/html/2601.11134v1#S4.T2 "Table 2 ‣ 4.1 Dataset Description ‣ 4 Experimental Setup ‣ FSL-BDP: Federated Survival Learning with Bayesian Differential Privacy for Credit Risk Modeling") summarizes key characteristics of the used datasets. These datasets present realistic decision support challenges spanning different lending contexts. LendingClub involves consumer credit decisions requiring rapid, automated assessment at scale. SBA involves small business lending with longer horizons, government guarantees, and different risk dynamics. Bondora spans multiple European countries with heterogeneous regulatory environments and borrower populations. Each context demands different decision support considerations from real-time scoring to long-horizon provisioning, making this a comprehensive evaluation of FSL-BDP’s practical applicability.

* •

  LendingClub: The first dataset is drawn from LendingClub, a major U.S. peer-to-peer lending platform widely used in credit risk research [zhang2020credit](https://arxiv.org/html/2601.11134v1#bib.bib4) ; [serrano2016use](https://arxiv.org/html/2601.11134v1#bib.bib5) ; [jagtiani2019roles](https://arxiv.org/html/2601.11134v1#bib.bib6) ; [lyocsa2022default](https://arxiv.org/html/2601.11134v1#bib.bib7) ; [croux2020important](https://arxiv.org/html/2601.11134v1#bib.bib20) ; [papouskova2019two](https://arxiv.org/html/2601.11134v1#bib.bib55) . The dataset include approximately 150 features spanning application information, credit bureau summaries, borrower demographics, and repayment behavior. The event indicator is derived from the loan\_status field confirming charge-off or default, with default defined as occurring within a 24-month observation window from loan origination.
* •

  SBA Dataset: The second dataset is drawn from the U.S. Small Business Administration (SBA) loan program, which comprises government-guaranteed loans to small businesses and is widely used in credit risk research [li2018should](https://arxiv.org/html/2601.11134v1#bib.bib83) ; [glennon2005measuring](https://arxiv.org/html/2601.11134v1#bib.bib84) . The data include loan terms, guarantee characteristics, borrower attributes (industry, firm age, employment), and macroeconomic indicators. The event indicator is defined using the ChgOffDate field, with default observed within a 48-month window from origination. Given the long tenure of SBA loans, the extended observation window ensures a sufficient event rate for survival modeling.
* •

  Bondora: The third dataset is drawn from Bondora, a leading European peer-to-peer lending platform ([bondora\_site,](https://arxiv.org/html/2601.11134v1#bib.bib85) ; [lyocsa2022default,](https://arxiv.org/html/2601.11134v1#bib.bib7) ; [mondal2023predicting,](https://arxiv.org/html/2601.11134v1#bib.bib86) ; [domotor2023peer,](https://arxiv.org/html/2601.11134v1#bib.bib8) ; [bone2024improving,](https://arxiv.org/html/2601.11134v1#bib.bib87) ). The dataset contains borrower demographic characteristics, financial attributes, and loan-level transactional information. The event indicator is constructed from the ActiveLateLastPaymentCategory field, where an event is defined as reaching 90+ days past due within a 24-month observation window from loan origination.

Standard preprocessing steps were applied: date features were transformed into days-from-reference, columns prone to data leakage (e.g., funded\_amnt, int\_rate) were removed, missing values were imputed with zeros, categorical variables were one-hot encoded with infrequent categories grouped, and standardization was applied to the training set only to prevent leakage.

Table 2: Dataset Statistics

|  |  |  |  |
| --- | --- | --- | --- |
| Characteristic | LendingClub | SBA | Bondora |
| Total observations | 1,660,791 | 753,258 | 218,559 |
| Number of features | 59 | 33 | 37 |
| Default rate | 12.8% | 4.5% | 32.5% |
| Observation window | 24 months | 48 months | 24 months |
| Federated Partitioning | | | |
| Number of clients (KK) | 27 states | 32 states | 3 countries |
| Min client size | 20,327 | 8,244 | 25,916 |
| Max client size | 229,389 | 114,088 | 124,349 |
| Mean client size | 54,938 | 26,175 | 72,761 |
| Data Splits | | | |
| Train/Test/OOT (’K) | 978/244/438 | 502/125/126 | 127/32/59 |
| Train/Test window | 2013-2016 | 1985-2006 | 2013-2018 |
| OOT window | 2017 | 2007-2011 | 2019- Sep 2022 |

![Refer to caption](Fig/LC_survival_curves.jpg)


Figure 4: Survival Curve – LendingClub P2P Dataset

![Refer to caption](Fig/SBA_survival_curves.jpg)


Figure 5: Survival Curve – SBA Loan Dataset

![Refer to caption](Fig/Bondora_survival_curves.jpg)


Figure 6: Survival Curve – Bondora Dataset

### 4.2 Performance Evaluation Metrics

We evaluated each model’s performance using two established survival analysis metrics: the concordance index for discrimination ability and the integrated Brier score for prediction accuracy. Both metrics are computed on held-out test sets to ensure unbiased performance estimation.

#### Concordance Index (C-index)

The concordance index measures the model’s ability to correctly rank subjects according to their survival risk [steck2007ranking](https://arxiv.org/html/2601.11134v1#bib.bib88) . For time-dependent predictions, we employ the time-dependent C-index [antolini2005time](https://arxiv.org/html/2601.11134v1#bib.bib89) , which evaluates discrimination at specific time horizons while accounting for censoring. At evaluation time t∗t^{\*}, consider all admissible pairs (i,j)(i,j) where subject ii experienced an event before t∗t^{\*} (Ti≤t∗,δi=1T\_{i}\leq t^{\*},\delta\_{i}=1) and subject jj was still at risk (Tj>TiT\_{j}>T\_{i}). The pair is concordant if the model correctly predicts lower survival probability for subject ii:

|  |  |  |  |
| --- | --- | --- | --- |
|  | C​(t∗)=∑i,j𝟙​(Ti≤t∗,δi=1,Tj>Ti)⋅𝟙​(S^​(Ti∣𝐱i)<S^​(Ti∣𝐱j))∑i,j𝟙​(Ti≤t∗,δi=1,Tj>Ti),C(t^{\*})=\frac{\sum\_{i,j}\mathbbm{1}(T\_{i}\leq t^{\*},\delta\_{i}=1,T\_{j}>T\_{i})\cdot\mathbbm{1}(\hat{S}(T\_{i}\mid\mathbf{x}\_{i})<\hat{S}(T\_{i}\mid\mathbf{x}\_{j}))}{\sum\_{i,j}\mathbbm{1}(T\_{i}\leq t^{\*},\delta\_{i}=1,T\_{j}>T\_{i})}, |  | (10) |

where S^​(t∣𝐱)\hat{S}(t\mid\mathbf{x}) is the predicted survival probability at time tt for covariates 𝐱\mathbf{x}, TiT\_{i} is the observed time, δi\delta\_{i} is the event indicator, and 𝟙​(⋅)\mathbbm{1}(\cdot) denotes the indicator function. The C-index ranges from 0.5 (random discrimination) to 1.0 (perfect discrimination). Values above 0.7 indicate acceptable discrimination; values above 0.8 indicate strong predictive ability. We report the mean C-index across evaluation time points 𝒯eval\mathcal{T}\_{\text{eval}}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | C¯=1|𝒯eval|​∑t∗∈𝒯evalC​(t∗).\bar{C}=\frac{1}{|\mathcal{T}\_{\text{eval}}|}\sum\_{t^{\*}\in\mathcal{T}\_{\text{eval}}}C(t^{\*}). |  | (11) |

#### Integrated Brier Score (IBS)

The Brier score quantifies prediction accuracy by measuring the mean squared error between predicted survival probabilities and observed outcomes [graf1999assessment](https://arxiv.org/html/2601.11134v1#bib.bib90) . Unlike the C-index, which only evaluates ranking, the Brier score assesses both discrimination and calibration. For survival data with censoring, we use the inverse probability of censoring weighting (IPCW) to obtain unbiased estimates. At evaluation time t∗t^{\*}, the censoring-adjusted Brier score is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | BS​(t∗)=1n​∑i=1n[𝟙​(Ti≤t∗,δi=1)G^​(Ti)​S^​(t∗∣𝐱i)2+𝟙​(Ti>t∗)G^​(t∗)​(1−S^​(t∗∣𝐱i))2],\text{BS}(t^{\*})=\frac{1}{n}\sum\_{i=1}^{n}\left[\frac{\mathbbm{1}(T\_{i}\leq t^{\*},\delta\_{i}=1)}{\hat{G}(T\_{i})}\hat{S}(t^{\*}\mid\mathbf{x}\_{i})^{2}+\frac{\mathbbm{1}(T\_{i}>t^{\*})}{\hat{G}(t^{\*})}(1-\hat{S}(t^{\*}\mid\mathbf{x}\_{i}))^{2}\right], |  | (12) |

where G^​(t)\hat{G}(t) is the Kaplan-Meier estimate of the censoring distribution, computed on the training data with reversed event indicators. The integrated Brier score aggregates performance across the evaluation time range [tmin,tmax][t\_{\min},t\_{\max}]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | IBS=1tmax−tmin​∫tmintmaxBS​(t)​𝑑t.\text{IBS}=\frac{1}{t\_{\max}-t\_{\min}}\int\_{t\_{\min}}^{t\_{\max}}\text{BS}(t)\,dt. |  | (13) |

In practice, we approximate this integral using the trapezoidal rule over discrete evaluation times 𝒯eval={t1,…,tm}\mathcal{T}\_{\text{eval}}=\{t\_{1},\ldots,t\_{m}\}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | IBS≈1tm−t1​∑k=1m−1BS​(tk)+BS​(tk+1)2⋅(tk+1−tk).\text{IBS}\approx\frac{1}{t\_{m}-t\_{1}}\sum\_{k=1}^{m-1}\frac{\text{BS}(t\_{k})+\text{BS}(t\_{k+1})}{2}\cdot(t\_{k+1}-t\_{k}). |  | (14) |

The IBS ranges from 0 (perfect prediction) to 1, with lower values indicating better overall accuracy. The IBS provides a comprehensive performance measure as it penalizes both poor discrimination and miscalibration.

![Refer to caption](Fig/experiment_design.png)


Figure 7: Experiment design overview

### 4.3 Implementation Details

We implemented FSL-BDP in PyTorch 2.0 to simulate a federated scenario with one central server and KK participating clients, executed on NVIDIA T4 GPUs. Unlike prior federated credit scoring studies that rely on artificial client partitions through random sampling [shingi2020federated](https://arxiv.org/html/2601.11134v1#bib.bib29) ; [wang2024novel](https://arxiv.org/html/2601.11134v1#bib.bib30) ; [li2024dynamic](https://arxiv.org/html/2601.11134v1#bib.bib31) , we partition datasets according to natural geographic boundaries: LendingClub and SBA by U.S. states (27 and 32 clients), Bondora by European countries (3 clients). This yields organically heterogeneous distributions reflecting real cross-regional variation in default behavior, as shown in Figures [4](https://arxiv.org/html/2601.11134v1#S4.F4 "Figure 4 ‣ 4.1 Dataset Description ‣ 4 Experimental Setup ‣ FSL-BDP: Federated Survival Learning with Bayesian Differential Privacy for Credit Risk Modeling"), [5](https://arxiv.org/html/2601.11134v1#S4.F5 "Figure 5 ‣ 4.1 Dataset Description ‣ 4 Experimental Setup ‣ FSL-BDP: Federated Survival Learning with Bayesian Differential Privacy for Credit Risk Modeling"), and [6](https://arxiv.org/html/2601.11134v1#S4.F6 "Figure 6 ‣ 4.1 Dataset Description ‣ 4 Experimental Setup ‣ FSL-BDP: Federated Survival Learning with Bayesian Differential Privacy for Credit Risk Modeling"). Following industry practice, each client’s data is split into training (80%), in-time testing (20%), and out-of-time validation with data samples outside training window to stress test model robustness.

The survival model employs a six-layer feed-forward network (Input→\rightarrow128→\rightarrow64→\rightarrow64→\rightarrow32→\rightarrow32→\rightarrowTT) with SELU activations and sigmoid output to ensure hazard probabilities hj​(x)∈(0,1)h\_{j}(x)\in(0,1) across TT discrete time intervals. Training uses Adam optimizer (η=0.001\eta=0.001), batch size B=32B=32, and the negative log-likelihood loss for discrete-time survival (Equation [1](https://arxiv.org/html/2601.11134v1#S3.E1 "In Likelihood Representation: ‣ 3.2 Discrete-Time Survival Likelihood ‣ 3 Methodologies ‣ FSL-BDP: Federated Survival Learning with Bayesian Differential Privacy for Credit Risk Modeling")). The federated protocol, illustrated in Figure [7](https://arxiv.org/html/2601.11134v1#S4.F7 "Figure 7 ‣ Integrated Brier Score (IBS) ‣ 4.2 Performance Evaluation Metrics ‣ 4 Experimental Setup ‣ FSL-BDP: Federated Survival Learning with Bayesian Differential Privacy for Credit Risk Modeling"), runs R=10R=10 communication rounds with full client participation, where each client performs E=5E=5 local epochs before uploading privatized updates for weighted FedAvg aggregation.

For differential privacy, we set gradient clipping threshold C=1.0C=1.0 and calibrate noise multiplier σ\sigma to achieve target budgets ε∈{0.5,1.0,2.0,10.0}\varepsilon\in\{0.5,1.0,2.0,10.0\} with δ=10−5\delta=10^{-5}. The Bayesian DP mechanism employs leave-one-out gradient estimation with M=10M=10 sub-batches per batch; clients with insufficient data (nk<100n\_{k}<100) fall back to analytical DP with closed-form guarantees.

All experiments use fixed random seeds (seed = 42) with deterministic CUDA settings for reproducibility. Results are averaged over 5 independent runs with standard deviations reported in Table [3](https://arxiv.org/html/2601.11134v1#S5.T3 "Table 3 ‣ 5.1 Overall Performance Comparison ‣ 5 Experimental Results and Analysis ‣ FSL-BDP: Federated Survival Learning with Bayesian Differential Privacy for Credit Risk Modeling").

## 5 Experimental Results and Analysis

This section presents experimental results for FSL-BDP across three credit datasets. We examine: (i) performance under centralized and federated training with different privacy settings, (ii) convergence behavior, (iii) the model’s ability to distinguish early from late defaulters, (iv) calibration of predicted survival curves, and (v) client-level variation in performance.

### 5.1 Overall Performance Comparison

We compare discrimination and calibration performance across centralized and federated learning settings under three privacy regimes: no privacy (No-DP), Classical Differential Privacy (DP), and Bayesian Differential Privacy (BDP). Performance is evaluated using the concordance index (C-index) and integrated Brier score (IBS) on both in-time-test(Test) sets and out-of-time (OOT) validation sets, with detailed results summarized in Table [3](https://arxiv.org/html/2601.11134v1#S5.T3 "Table 3 ‣ 5.1 Overall Performance Comparison ‣ 5 Experimental Results and Analysis ‣ FSL-BDP: Federated Survival Learning with Bayesian Differential Privacy for Credit Risk Modeling").

Table 3: Performance Comparison Across Datasets and Testing Scenarios. Results are reported for centralized and federated training under no privacy, classical differential privacy (DP), and Bayesian differential privacy (BDP)

| Dataset | Scenario | Test CI | Test IBS | OOT CI | OOT IBS |
| --- | --- | --- | --- | --- | --- |
| LendingClub | Centralized (No DP) | 0.674 ±\pm 0.009 | 0.055 ±\pm 0.007 | 0.642 ±\pm 0.011 | 0.054 ±\pm 0.008 |
| Centralized (Classical DP) | 0.610 ±\pm 0.011 | 0.063 ±\pm 0.008 | 0.598 ±\pm 0.013 | 0.137 ±\pm 0.018 |
| Centralized (BDP) | 0.562 ±\pm 0.011 | 0.062 ±\pm 0.008 | 0.563 ±\pm 0.010 | 0.125 ±\pm 0.015 |
| Federated (No DP) | 0.667 ±\pm 0.011 | 0.056 ±\pm 0.007 | 0.644 ±\pm 0.011 | 0.131 ±\pm 0.017 |
| Federated (Classical DP) | 0.633 ±\pm 0.013 | 0.063 ±\pm 0.008 | 0.615 ±\pm 0.012 | 0.139 ±\pm 0.018 |
| Federated (BDP) | 0.638 ±\pm 0.012 | 0.059 ±\pm 0.007 | 0.618 ±\pm 0.011 | 0.132 ±\pm 0.017 |
| Bondora | Centralized (No DP) | 0.610 ±\pm 0.037 | 0.139 ±\pm 0.050 | 0.542 ±\pm 0.002 | 0.265 ±\pm 0.073 |
| Centralized (Classical DP) | 0.576 ±\pm 0.031 | 0.175 ±\pm 0.069 | 0.511 ±\pm 0.007 | 0.465 ±\pm 0.055 |
| Centralized (BDP) | 0.550 ±\pm 0.029 | 0.153 ±\pm 0.056 | 0.505 ±\pm 0.005 | 0.428 ±\pm 0.050 |
| Federated (No DP) | 0.602 ±\pm 0.037 | 0.177 ±\pm 0.111 | 0.529 ±\pm 0.008 | 0.306 ±\pm 0.057 |
| Federated (Classical DP) | 0.576 ±\pm 0.019 | 0.210 ±\pm 0.116 | 0.517 ±\pm 0.006 | 0.476 ±\pm 0.030 |
| Federated (BDP) | 0.582 ±\pm 0.021 | 0.176 ±\pm 0.093 | 0.515 ±\pm 0.005 | 0.436 ±\pm 0.023 |
| SBA | Centralized (No DP) | 0.748 ±\pm 0.034 | 0.019 ±\pm 0.007 | 0.639 ±\pm 0.047 | 0.089 ±\pm 0.036 |
| Centralized (Classical DP) | 0.696 ±\pm 0.044 | 0.020 ±\pm 0.008 | 0.596 ±\pm 0.056 | 0.096 ±\pm 0.041 |
| Centralized (BDP) | 0.692 ±\pm 0.036 | 0.020 ±\pm 0.008 | 0.612 ±\pm 0.053 | 0.094 ±\pm 0.039 |
| Federated (No DP) | 0.738 ±\pm 0.041 | 0.019 ±\pm 0.007 | 0.631 ±\pm 0.044 | 0.077 ±\pm 0.033 |
| Federated (Classical DP) | 0.699 ±\pm 0.047 | 0.021 ±\pm 0.008 | 0.576 ±\pm 0.057 | 0.099 ±\pm 0.042 |
| Federated (BDP) | 0.704 ±\pm 0.043 | 0.020 ±\pm 0.008 | 0.598 ±\pm 0.056 | 0.095 ±\pm 0.040 |

* •

  Note: CI = Concordance Index (higher is better); IBS = Integrated Brier Score (lower is better). Metrics reported as mean ±\pm std.

Three patterns emerge from the results. First, federated learning without privacy constraints performs comparably to centralized training. Across all datasets, the C-index drop from federation is less than 1% in both test and out-of-time validation. This validates, survival-based models for credit scoring can be trained collaboratively without meaningful loss in discrimination, even with heterogeneous client data. Second, under privacy constraints, Bayesian DP outperforms Classical DP in federated settings. Federated BDP achieves higher C-index and lower IBS than federated Classical DP across all datasets. However, the ranking reverses in centralized training, where Classical DP performs better. Privacy mechanism rankings from centralized benchmarks do not transfer reliably to federated deployments. Third, Bayesian DP shows better temporal stability. In out-of-time validation, federated BDP degrades less than Classical DP across all datasets. For credit risk applications, stability under distribution shift affects provisioning and capital decisions.

### 5.2 Convergence Analysis and Training Dynamics

We analyze training dynamics to understand how different privacy mechanisms affect optimization stability in centralized and federated survival learning. Convergence behavior is evaluated using training loss and C-index trajectories over multiple epochs on the LendingClub dataset, with results illustrated in figure [8](https://arxiv.org/html/2601.11134v1#S5.F8 "Figure 8 ‣ 5.2 Convergence Analysis and Training Dynamics ‣ 5 Experimental Results and Analysis ‣ FSL-BDP: Federated Survival Learning with Bayesian Differential Privacy for Credit Risk Modeling").

Under centralized training, Classical DP shows unstable convergence at strict privacy budgets. Training loss increases over epochs, and discrimination approaches random performance. Fixed worst-case noise appears to disrupt gradient directions enough to prevent effective optimization. In comparison, Bayesian DP shows stable loss reduction and maintains higher discrimination under the same privacy constraints, indicating that data-dependent noise calibration better preserves informative gradients during training.

Federated learning further alters these dynamics. Under federation, both privacy mechanisms demonstrate improved stability, with Bayesian DP benefiting the most. At comparable privacy levels, federated Bayesian DP converges faster, reaches lower training loss, and retains a larger fraction of non-private performance than its centralized counterpart. This pattern is consistent with the presence of implicit regularization induced by client-level gradient aggregation, which moderates noise effects across heterogeneous data partitions. Overall, the results indicate that convergence properties observed under centralized training do not directly translate to federated settings, and that federated architectures can materially improve the stability of privacy-preserving survival learning.

![Refer to caption](x2.png)


Figure 8: Convergence analysis comparing privacy mechanisms across learning paradigms on LendingClub data.
Panels (a) and (b) show centralized learning; panels (c) and (d) show federated learning.
The No-DP baseline (blue circles) achieves the highest C-Index but requires data centralization.
Classical DP (dashed lines, squares) exhibits degraded convergence and increasing loss, particularly at strict privacy budgets (ε≤1.0\varepsilon\leq 1.0).
Bayesian DP (solid lines, triangles) demonstrates superior stability with lower loss and competitive discrimination performance, suggesting the proposed FSL-BDP framework’s effectiveness in preserving model utility under Bayesian privacy guarantees.

![Refer to caption](Fig/Results/fig2_survival_curves_by_timing_modified.png)


Figure 9: Survival Analysis Captures Heterogeneous Default Timing

### 5.3 Distinguishing Early and Late Defaulters

Figure [9](https://arxiv.org/html/2601.11134v1#S5.F9 "Figure 9 ‣ 5.2 Convergence Analysis and Training Dynamics ‣ 5 Experimental Results and Analysis ‣ FSL-BDP: Federated Survival Learning with Bayesian Differential Privacy for Credit Risk Modeling") shows that the survival formulation captures heterogeneity in default timing not observable under binary classification. Survival curves differ across borrower segments, with distinct temporal trajectories.Early defaulters show steep declines in survival probability, with mean predicted default at 5.4 months. Late defaulters maintain high survival probability longer, with mean predicted default at 20.3 months. Binary models would label both groups similarly, but their economic implications differ: early defaults occur before substantial principal repayment, resulting in higher losses.

This temporal resolution has direct implications for credit risk management and regulatory reporting. The survival framework enables month-by-month hazard estimates that support IFRS 9 lifetime expected credit loss calculations: ECL=∑t=1Tht​(x)⋅LGD​(t)⋅EAD​(t)\text{ECL}=\sum\_{t=1}^{T}h\_{t}(x)\cdot\text{LGD}(t)\cdot\text{EAD}(t), where both exposure and loss severity vary over time. In contrast, conventional classification models produce a single risk score without timing information and therefore cannot support loss provisioning or monitoring processes that depend on the evolution of risk over the loan life. These results illustrate how survival-based modeling provides risk signals that are both economically interpretable and operationally relevant.

![Refer to caption](x3.png)


Figure 10: Cross-dataset client-level analysis (LendingClub: 27 clients, SBA: 32 clients, Bondora: 3 clients).
(a) Ranking reversal is consistent across all three datasets: Classical DP outperforms BDP in centralized training (red bars), but BDP outperforms Classical DP in federated settings (green bars).
(b) BDP benefits substantially more from federation (+7.0% average) than Classical DP (+1.4%), with Classical DP showing negative federation effect on Bondora.
(c) Client-level win rates confirm BDP’s advantage: 20/27 (74%) on LendingClub, 17/32 (53%) on SBA, 2/3 (67%) on Bondora.
(d) Summary statistics show BDP wins 39/62 clients overall (p=0.028p=0.028), with 5×\times higher federation boost.

![Refer to caption](x4.png)


Figure 11: Actual vs Predicted Survival Curves on LendingClub Test Data.

### 5.4 Model Calibration: Actual vs. Predicted Survival Curves

We evaluate the calibration of FSL-BDP by comparing predicted survival curves against non-parametric Kaplan-Meier estimates on the LendingClub test data, both at the aggregated level and across 27 state-level clients, illustrated in figure [11](https://arxiv.org/html/2601.11134v1#S5.F11 "Figure 11 ‣ 5.3 Distinguishing Early and Late Defaulters ‣ 5 Experimental Results and Analysis ‣ FSL-BDP: Federated Survival Learning with Bayesian Differential Privacy for Credit Risk Modeling") .

At the aggregate level, the predicted survival curve closely follows the Kapla-Meier estimate over the full 24-month horizon, capturing the gradual decline in survival probability without systematic over- or underestimation. This indicates that the model provides well-calibrated survival probabilities at the portfolio level. More importantly, the client-level panels show that FSL-BDP adapts effectively to heterogeneous regional risk profiles while learning a single global model. States with higher observed default risk, such as Nevada and Arizona, exhibit steeper survival declines, whereas lower-risk states, including North Carolina and Washington, display flatter trajectories. In each case, the predicted curves remain within the Kaplan–Meier confidence bands, indicating consistent calibration across clients with differing risk characteristics.

Quantitative calibration results support these visual findings. Bayesian DP achieves an integrated Brier score of 0.059, improving upon Classical DP (0.063) and approaching the non-private baseline (0.056). This suggests that Bayesian privacy preserves probability estimation accuracy more effectively than Classical DP under federated training. Reliable calibration is essential in regulated credit risk applications, where Basel III/IV and IFRS 9 require accurate probability estimates for capital adequacy and lifetime loss provisioning. By maintaining both discrimination and calibration under Bayesian privacy guarantees, FSL-BDP addresses a key practical constraint in deploying privacy-preserving models within regulated financial environments.

### 5.5 Client-Level Performance Analysis

Figure [10](https://arxiv.org/html/2601.11134v1#S5.F10 "Figure 10 ‣ 5.3 Distinguishing Early and Late Defaulters ‣ 5 Experimental Results and Analysis ‣ FSL-BDP: Federated Survival Learning with Bayesian Differential Privacy for Credit Risk Modeling") presents client-level performance comparisons across all three datasets and highlights a consistent empirical pattern. While Classical DP achieves higher performance than Bayesian DP under centralized training, this ordering reverses under federated learning across LendingClub, SBA, and Bondora.

The magnitude of this reversal is substantial. When transitioning from centralized to federated training, Bayesian DP exhibits a markedly larger performance gain than Classical DP. Averaged across datasets, Bayesian DP improves by 7.0%, whereas Classical DP improves by only 1.4%. This contrast is most pronounced for LendingClub and Bondora, where Classical DP shows limited or negative change under federation, while Bayesian DP consistently improves.

Client-level comparisons further confirm the robustness of this pattern. Across all datasets, Bayesian DP outperforms Classical DP in 39 of 62 clients. Dataset-specific win rates are 74% for LendingClub, 53% for SBA, and 67% for Bondora. A binomial test indicates that this difference is statistically significant (p=0.028p=0.028), suggesting that the observed advantage of Bayesian DP under federated training is unlikely to be due to random variation.

## 6 Discussion

In this section, we discuss our methodological contributions, practical implications, and, finally, limitations and further research directions.

### 6.1 Methodological Contributions

This study introduces FSL-BDP, a framework for privacy-preserving federated survival learning in credit risk. It enables multiple institutions to train models collaboratively without sharing raw data. Unlike prior federated approaches that use binary classification, FSL-BDP models time-to-default, distinguishing early from late defaulters. This temporal information is relevant for credit monitoring and lifetime risk assessment.

To our knowledge, this is the first application of Bayesian differential privacy to federated survival analysis. The proposed leave-one-out gradient estimation with data-dependent privacy accounting delivers practical (ε,δ)(\varepsilon,\delta) guarantees than classical worst-case differential privacy while preserving calibration and predictive utility under realistic constraints. A key finding is that privacy mechanism rankings reverse under federation: Classical DP performs better centralized, but Bayesian DP performs better federated. This suggests that privacy mechanisms should be evaluated in the intended deployment architecture, not inferred from centralized benchmarks. The insight applies broadly to privacy-preserving distributed learning beyond credit risk modeling.

### 6.2 Practical Implications

The framework addresses a key constraint in credit risk management: institutions value cross-lender learning but face regulatory, competitive, and reputational barriers to data sharing. FSL-BDP enables collaborative model development without exposing raw borrower data. By limiting information in gradient exchanges, the framework reduces exposure to membership and attribute inference attacks common in federated settings. Our results show that federation without privacy constraints retains over 99% of centralized performance. Under privacy constraints, Bayesian DP improves 7.0% on average when moving from centralized to federated training, compared to only 1.4% for Classical DP.

Smaller clients benefit proportionally more from federation, suggesting the framework is particularly valuable for regional lenders with limited individual portfolios. From a regulatory standpoint, calibration results indicate that probability estimates remain valid for regulatory reporting under strict privacy budgets. The temporal granularity supports Basel capital adequacy calculations alongside provisioning requirements, providing risk managers with outputs aligned to existing compliance workflows.

### 6.3 Limitations and Further Research

This study has limitations that suggest directions for future work. First, we assume full client participation in every communication round. Production deployments face partial participation, client dropout, and asynchronous updates, particularly across institutions with heterogeneous infrastructure. How these dynamics interact with Bayesian privacy accounting remains unexplored. Second, out-of-time performance degrades in some datasets, reflecting known challenges in maintaining model accuracy under distribution shift. Continuous monitoring and periodic retraining are standard practice in centralized credit modeling [amed2025pdx](https://arxiv.org/html/2601.11134v1#bib.bib51) , but extending these to federated settings is difficult when privacy budgets constrain update frequency. Developing federated monitoring, retraining, and budget management mechanisms within a federated machine learning operations framework is therefore an important research direction. Third, the framework assumes horizontal federation with a shared feature space. Many credit risk applications involve vertically partitioned data, with complementary features held by banks, e-commerce platforms, or telecom providers. Extending FSL-BDP to vertical or hybrid federation would require more complex feature alignment and secure aggregation mechanisms while maintaining computational efficiency for real-time decisioning.

Beyond technical extensions, our findings raise open questions at the intersection of analytics, governance, and economics. How should ownership, accountability, and auditability be defined for models trained collaboratively across institutional and regulatory boundaries? What are the cost-benefit tradeoffs between federated and centralized architectures as portfolio size and organizational complexity scale? Under what conditions does federated aggregation systematically strengthen or weaken different privacy mechanisms? Addressing these questions is essential for translating privacy-preserving federated learning from experimental settings into production decision support systems.

## 7 Conclusion

This study addresses the challenge of building privacy-preserving decision support systems that model time-to-default across multiple institutions while protecting borrower data through Bayesian differential privacy. The results show that federated survival learning retains near non-private performance under strict privacy budgets, enabling collaborative training without exposing sensitive data. Unlike binary classification, the survival formulation provides temporal risk estimates that directly support operational decisions: loan approval based on expected default timing, risk-adjusted pricing, and IFRS 9 lifetime loss provisioning. A key finding for decision support system design is that privacy mechanism performance depends on deployment architecture. Bayesian DP outperforms Classical DP under federation, reversing rankings observed in centralized settings. Practitioners building privacy-preserving decision support systems should therefore evaluate mechanisms in their intended deployment environment rather than rely on centralized benchmarks. This insight generalizes to other multi-institutional contexts such as fraud detection, healthcare analytics, and supply chain risk, where data sovereignty constraints preclude centralization but collaborative learning remains valuable.

## References

* [1]

  World Bank.
  The global findex database 2025: Connectivity and financial inclusion
  in the digital economy, 2025.
* [2]

  Leora Klapper.
  Digital finance boosting women’s financial inclusion in sub-saharan
  africa: Emerging evidence.
  Africa in Focus (Brookings Institution), 2024.
* [3]

  World Bank.
  The impact of mobile money in sub-saharan africa.
  Global Findex Regional Note (Sub-Saharan Africa), 2024.
* [4]

  Weiguo Zhang, Chao Wang, Yue Zhang, and Junbo Wang.
  Credit risk evaluation model with textual features from loan
  descriptions for p2p lending.
  Electronic Commerce Research and Applications, 42:100989, 2020.
* [5]

  Carlos Serrano-Cinca and Begoña Gutiérrez-Nieto.
  The use of profit scoring as an alternative to credit scoring systems
  in peer-to-peer (p2p) lending.
  Decision Support Systems, 89:113–122, 2016.
* [6]

  Julapa Jagtiani and Catharine Lemieux.
  The roles of alternative data and machine learning in fintech
  lending: Evidence from the lendingclub consumer platform.
  Financial Management, 48(4):1009–1029, 2019.
* [7]

  Štefan Lyócsa, Petra Vašaničová, Branka
  Hadji Misheva, and Marko Dávid Vateha.
  Default or profit scoring credit systems? evidence from european and
  us peer-to-peer lending markets.
  Financial Innovation, 8(1):32, 2022.
* [8]

  Barbara Dömötör, Ferenc Illés, and Tímea Ölvedi.
  Peer-to-peer lending: Legal loan sharking or altruistic investment?
  analyzing platform investments from a credit risk perspective.
  Journal of International Financial Markets, Institutions and
  Money, 86:101801, 2023.
* [9]

  Md Masud Kowsar, Mohammad Mohiuddin, and Hosne Ara Mohna.
  Credit decision automation in commercial banks: a review of ai and
  predictive analytics in loan assessment.
  American Journal of Interdisciplinary Studies, 4(04):01–26,
  2023.
* [10]

  Daron Acemoglu, Asuman Ozdaglar, and Alireza Tahbaz-Salehi.
  Systemic risk and stability in financial networks.
  American Economic Review, 105(2):564–608, 2015.
* [11]

  Aamina Khurram, Abdullah Iqbal, and Vasileios Pappas.
  Systemic risk: new evidence from alternative financial systems.
  Review of Quantitative Finance and Accounting, pages 1–25,
  2025.
* [12]

  Bart Baesens and Kristien Smedts.
  Boosting credit risk models.
  The British Accounting Review, page 101241, 2023.
* [13]

  Bart Baesens.
  Analytics in a big data world: The essential guide to data
  science and its applications.
  John Wiley & Sons, 2014.
* [14]

  Zongyuan Zhao, Shuxiang Xu, Byeong Ho Kang, Mir Md Jahangir Kabir, Yunling Liu,
  and Rainer Wasinger.
  Investigation and improvement of multi-layer perceptron neural
  networks for credit scoring.
  Expert Systems with Applications, 42(7):3508–3516, 2015.
* [15]

  Mohammad Mahbobi, Salman Kimiagari, and Marriappan Vasudevan.
  Credit risk classification: an integrated predictive accuracy
  algorithm using artificial and deep neural networks.
  Annals of Operations Research, 330(1):609–637, 2023.
* [16]

  Viani B Djeundje, Jonathan Crook, Raffaella Calabrese, and Mona Hamid.
  Enhancing credit scoring with alternative data.
  Expert Systems with Applications, 163:113766, 2021.
* [17]

  Giulio Cornelli, Jon Frost, Leonardo Gambacorta, P Raghavendra Rau, Robert
  Wardrop, and Tania Ziegler.
  Fintech and big tech credit: Drivers of the growth of digital
  lending.
  Journal of Banking & Finance, 148:106742, 2023.
* [18]

  Fatemeh Nemati Koutanaei, Hedieh Sajedi, and Mohammad Khanbabaei.
  A hybrid data mining model of feature selection algorithms and
  ensemble learning classifiers for credit scoring.
  Journal of Retailing and Consumer Services, 27:11–23, 2015.
* [19]

  Guilherme Barreto Fernandes and Rinaldo Artes.
  Spatial dependence in credit risk and its improvement in credit
  scoring.
  European Journal of Operational Research, 249(2):517–524,
  2016.
* [20]

  Christophe Croux, Julapa Jagtiani, Tarunsai Korivi, and Milos Vulanovic.
  Important factors determining fintech loan default: Evidence from a
  lendingclub consumer platform.
  Journal of Economic Behavior & Organization, 173:270–296,
  2020.
* [21]

  Murphy Choy and Ma Nang Laik.
  A markov chain approach to determine the optimal performance period
  and bad definition for credit scorecard.
  Journal of social science and management, 1(6):227–234, 2011.
* [22]

  Arjana Brezigar-Masten, Igor Masten, and Matjaž Volk.
  Modeling credit risk with a tobit model of days past due.
  Journal of Banking & Finance, 122:105984, 2021.
* [23]

  Tony Bellotti and Jonathan Crook.
  Support vector machines for credit scoring and discovery of
  significant features.
  Expert Systems with Applications, 36(2):3302–3308, 2009.
* [24]

  Lore Dirick, Gerda Claeskens, and Bart Baesens.
  Time to default in credit scoring using survival analysis: a
  benchmark study.
  Journal of the Operational Research Society, 68(6):652–665,
  2017.
* [25]

  Nadiia Horobets, Oleg Reznik, Vasyl Maliyk, Ivan Vyhivskyi, and Liliia
  Bobrishova.
  Artificial intelligence technologies in banking: challenges and
  opportunities for anti-money laundering in the context of eu regulatory
  initiatives.
  Journal of Money Laundering Control, 2025.
* [26]

  Santhosh Chitraju Gopal Varma and Bhushan Chaudhari.
  Federated learning in financial data privacy: A secure ai framework
  for banking applications.
  International Journal of Emerging Trends in Computer Science and
  Information Technology, pages 101–110, 2025.
* [27]

  Si Ying Tan, Araz Taeihagh, and Devyani Pande.
  Data sharing in disruptive technologies: lessons from adoption of
  autonomous systems in singapore.
  Policy Design and Practice, 6(1):57–78, 2023.
* [28]

  Brendan McMahan, Eider Moore, Daniel Ramage, Seth Hampson, and Blaise Aguera
  y Arcas.
  Communication-efficient learning of deep networks from decentralized
  data.
  In Artificial intelligence and statistics, pages 1273–1282.
  PMLR, 2017.
* [29]

  Geet Shingi.
  A federated learning based approach for loan defaults prediction.
  In 2020 International Conference on Data Mining Workshops
  (ICDMW), pages 362–368. IEEE, 2020.
* [30]

  Zhongyi Wang, Jin Xiao, Lu Wang, and Jianrong Yao.
  A novel federated learning approach with knowledge transfer for
  credit scoring.
  Decision Support Systems, 177:114084, 2024.
* [31]

  Ruiheng Li, Yue Cao, Yuhang Shu, Jia Guo, Binghua Shi, Jiaojiao Yu, Yi Di,
  Qiankun Zuo, and Hao Tian.
  A dynamic receptive field and improved feature fusion approach for
  federated learning in financial credit risk assessment.
  Scientific Reports, 14(1):26515, 2024.
* [32]

  Ryan Randy Suryono, Betty Purwandari, and Indra Budi.
  Peer to peer (p2p) lending problems and potential solutions: A
  systematic literature review.
  Procedia Computer Science, 161:204–214, 2019.
* [33]

  Hicham Sadok, Fadi Sakka, and Mohammed El Hadi El Maknouzi.
  Artificial intelligence and bank credit analysis: A review.
  Cogent Economics & Finance, 10(1):2023262, 2022.
* [34]

  Longbing Cao.
  Ai in finance: A review.
  Available at SSRN 3647625, 2020.
* [35]

  Aleksy Klimowicz and Krzysztof Spirzewski.
  Concept of peer-to-peer lending and application of machine learning
  in credit scoring.
  Journal of Banking and Financial Economics, (2 (16):25–55,
  2021.
* [36]

  Brian E Clauser, Raja G Subhiyah, Ronald J Nungester, Douglas R Ripkey,
  Stephen G Clyman, and Danette McKinley.
  Scoring a performance-based assessment by modeling the judgments of
  experts.
  Journal of Educational Measurement, 32(4):397–415, 1995.
* [37]

  Elizabeth Mays.
  Handbook of credit scoring.
  Global Professional Publishi, 1995.
* [38]

  Yiheng Li and Weidong Chen.
  A comparative performance assessment of ensemble learning for credit
  scoring.
  Mathematics, 8(10):1756, 2020.
* [39]

  Gang Wang, Jinxing Hao, Jian Ma, and Hongbing Jiang.
  A comparative assessment of ensemble learning for credit scoring.
  Expert systems with applications, 38(1):223–230, 2011.
* [40]

  Chao Qin, Yunfeng Zhang, Fangxun Bao, Caiming Zhang, Peide Liu, and Peipei Liu.
  Xgboost optimized by adaptive particle swarm optimization for credit
  scoring.
  Mathematical Problems in Engineering, 2021(1):6655510, 2021.
* [41]

  Bastien Lextrait.
  Scaling up smes’ credit scoring scope with lightgbm.
  Applied Economics, 55(9):925–943, 2023.
* [42]

  Xingzhi Zhang, Yan Yang, and Zhurong Zhou.
  A novel credit scoring model based on optimized random forest.
  In 2018 IEEE 8th annual computing and communication workshop and
  conference (CCWC), pages 60–65. IEEE, 2018.
* [43]

  Nisha Arora and Pankaj Deep Kaur.
  A bolasso based consistent feature selection enabled random forest
  classification algorithm: An application to credit risk assessment.
  Applied Soft Computing, 86:105936, 2020.
* [44]

  Zaimei Zhang, Kun Niu, and Yan Liu.
  A deep learning based online credit scoring model for p2p lending.
  IEEE Access, 8:177307–177317, 2020.
* [45]

  Matthew Stevenson, Christophe Mues, and Cristián Bravo.
  The value of text for small business default prediction: A deep
  learning approach.
  European Journal of Operational Research, 295(2):758–771,
  2021.
* [46]

  Dalila Boughaci and Abdullah AK Alkhawaldeh.
  A new variable selection method applied to credit scoring.
  Algorithmic Finance, 7(1-2):43–52, 2018.
* [47]

  Yujia Chen, Raffaella Calabrese, and Belen Martin-Barragan.
  Interpretable machine learning for imbalanced credit scoring
  datasets.
  European Journal of Operational Research, 312(1):357–372,
  2024.
* [48]

  Darie Moldovan.
  Algorithmic decision making methods for fair credit scoring.
  IEEE Access, 11:59729–59743, 2023.
* [49]

  Nikita Kozodoi, Johannes Jacob, and Stefan Lessmann.
  Fairness in credit scoring: Assessment, implementation and profit
  implications.
  European Journal of Operational Research, 297(3):1083–1094,
  2022.
* [50]

  María Óskarsdóttir, Cristián Bravo, Carlos Sarraute, Jan
  Vanthienen, and Bart Baesens.
  The value of big data for credit scoring: Enhancing financial
  inclusion using mobile phone data and social network analytics.
  Applied Soft Computing, 74:26–39, 2019.
* [51]

  Sultan Amed, Chan Yu Hang, and Sayantan Banerjee.
  Pdx–adaptive credit risk forecasting model in digital lending using
  machine learning operations.
  arXiv preprint arXiv:2512.22305, 2025.
* [52]

  Stefan Lessmann, Bart Baesens, Hsin-Vonn Seow, and Lyn C Thomas.
  Benchmarking state-of-the-art classification algorithms for credit
  scoring: An update of research.
  European journal of operational research, 247(1):124–136,
  2015.
* [53]

  Vincenzo Moscato, Antonio Picariello, and Giancarlo Sperlí.
  A benchmark of machine learning approaches for credit score
  prediction.
  Expert Systems with Applications, 165:113986, 2021.
* [54]

  Nan-Chen Hsieh and Lun-Ping Hung.
  A data driven ensemble classifier for credit scoring analysis.
  Expert systems with Applications, 37(1):534–545, 2010.
* [55]

  Monika Papouskova and Petr Hajek.
  Two-stage consumer credit risk modelling using heterogeneous ensemble
  learning.
  Decision support systems, 118:33–45, 2019.
* [56]

  Björn Rafn Gunnarsson, Seppe Vanden Broucke, Bart Baesens, María
  Óskarsdóttir, and Wilfried Lemahieu.
  Deep learning for credit scoring: Do or don’t?
  European Journal of Operational Research, 295(1):292–305,
  2021.
* [57]

  Yufei Xia, Lingyun He, Yinguo Li, Yating Fu, and Yixin Xu.
  A dynamic credit scoring model based on survival gradient boosting
  decision tree approach.
  Technological and Economic Development of Economy,
  27(1):96–119, 2021.
* [58]

  Miaojun Bai, Yan Zheng, and Yun Shen.
  Gradient boosting survival tree with applications in credit scoring.
  Journal of the Operational Research Society, 73(1):39–55,
  2022.
* [59]

  Gabriel Blumenstock, Stefan Lessmann, and Hsin-Vonn Seow.
  Deep learning for survival and competing risk modelling.
  Journal of the Operational Research Society, 73(1):26–38,
  2022.
* [60]

  Victor Medina-Olivares, Raffaella Calabrese, Jonathan Crook, and Finn Lindgren.
  Joint models for longitudinal and discrete survival data in credit
  scoring.
  European Journal of Operational Research, 307(3):1457–1473,
  2023.
* [61]

  Haoran He, Zhao Wang, Hemant Jain, Cuiqing Jiang, and Shanlin Yang.
  A privacy-preserving decentralized credit scoring method based on
  multi-party information.
  Decision Support Systems, 166:113910, 2023.
* [62]

  Mathieu Andreux, Andre Manoel, Romuald Menuet, Charlie Saillard, and Chloé
  Simpson.
  Federated survival analysis with discrete-time cox models.
  arXiv preprint arXiv:2006.08997, 2020.
* [63]

  Md Mahmudur Rahman and Sanjay Purushotham.
  Fedpseudo: Privacy-preserving pseudo value-based deep learning models
  for federated survival analysis.
  In Proceedings of the 29th ACM SIGKDD Conference on Knowledge
  Discovery and Data Mining, pages 1999–2009, 2023.
* [64]

  Alberto Archetti and Matteo Matteucci.
  Federated survival forests.
  In 2023 International Joint Conference on Neural Networks
  (IJCNN), pages 1–9. IEEE, 2023.
* [65]

  Gang Wen and Limin Li.
  Federated transfer learning with differential privacy for multi-omics
  survival analysis.
  Briefings in Bioinformatics, 26(2), 2025.
* [66]

  Narasimha Raghavan Veeraragavan, Sai Praneeth Karimireddy, and Jan Franz
  Nygård.
  A differentially private kaplan-meier estimator for
  privacy-preserving survival analysis.
  arXiv preprint arXiv:2412.05164, 2024.
* [67]

  Edward L Kaplan and Paul Meier.
  Nonparametric estimation from incomplete observations.
  Journal of the American statistical association,
  53(282):457–481, 1958.
* [68]

  David R Cox.
  Regression models and life-tables.
  Journal of the Royal Statistical Society: Series B
  (Methodological), 34(2):187–202, 1972.
* [69]

  B Narain.
  Survival analysis and the credit-granting decision. w: L. thomas, j.
  crook i d. edelman (red.), credit scoring and credit control (s. 109–122),
  1992.
* [70]

  M Kabir Hassan, Jennifer Brodmann, Blake Rayfield, and Makeen Huda.
  Modeling credit risk in credit unions using survival analysis.
  International Journal of Bank Marketing, 36(3):482–495, 2018.
* [71]

  Sirong Luo, Xiao Kong, and Tingting Nie.
  Spline based survival model for credit risk modeling.
  European Journal of Operational Research, 253(3):869–879,
  2016.
* [72]

  Edward NC Tong, Christophe Mues, and Lyn C Thomas.
  Mixture cure models in credit scoring: If and when borrowers default.
  European Journal of Operational Research, 218(1):132–139,
  2012.
* [73]

  Andrew Hard, Kanishka Rao, Rajiv Mathews, Swaroop Ramaswamy, Françoise
  Beaufays, Sean Augenstein, Hubert Eichner, Chloé Kiddon, and Daniel
  Ramage.
  Federated learning for mobile keyboard prediction.
  arXiv preprint arXiv:1811.03604, 2018.
* [74]

  Martin Abadi, Andy Chu, Ian Goodfellow, H Brendan McMahan, Ilya Mironov, Kunal
  Talwar, and Li Zhang.
  Deep learning with differential privacy.
  In Proceedings of the 2016 ACM SIGSAC conference on computer and
  communications security, pages 308–318, 2016.
* [75]

  Kang Wei, Jun Li, Ming Ding, Chuan Ma, Howard H Yang, Farhad Farokhi, Shi Jin,
  Tony QS Quek, and H Vincent Poor.
  Federated learning with differential privacy: Algorithms and
  performance analysis.
  IEEE transactions on information forensics and security,
  15:3454–3469, 2020.
* [76]

  Aleksei Triastcyn and Boi Faltings.
  Federated learning with bayesian differential privacy.
  In 2019 IEEE International Conference on Big Data (Big Data),
  pages 2587–2596. IEEE, 2019.
* [77]

  Aleksei Triastcyn and Boi Faltings.
  Bayesian differential privacy for machine learning.
  In International Conference on Machine Learning, pages
  9583–9592. PMLR, 2020.
* [78]

  Håvard Kvamme, Ørnulf Borgan, and Ida Scheel.
  Time-to-event prediction with neural networks and cox regression.
  Journal of machine learning research, 20(129):1–30, 2019.
* [79]

  Michael F Gensheimer and Balasubramanian Narasimhan.
  A scalable discrete-time survival model for neural networks.
  PeerJ, 7:e6257, 2019.
* [80]

  Cynthia Dwork, Aaron Roth, et al.
  The algorithmic foundations of differential privacy.
  Foundations and trends® in theoretical computer
  science, 9(3–4):211–407, 2014.
* [81]

  Robin C Geyer, Tassilo Klein, and Moin Nabi.
  Differentially private federated learning: A client level
  perspective.
  arXiv preprint arXiv:1712.07557, 2017.
* [82]

  Ilya Mironov.
  Rényi differential privacy.
  In 2017 IEEE 30th computer security foundations symposium
  (CSF), pages 263–275. IEEE, 2017.
* [83]

  Min Li, Amy Mickel, and Stanley Taylor.
  “should this loan be approved or denied?”: A large dataset with
  class assignment guidelines.
  Journal of Statistics Education, 26(1):55–66, 2018.
* [84]

  Dennis Glennon and Peter Nigro.
  Measuring the default risk of small business loans: A survival
  analysis approach.
  Journal of Money, Credit and Banking, pages 923–947, 2005.
* [85]

  Bondora : European p2p lending platform.
  <https://www.bondora.com/en>, 2025.
* [86]

  Sampurna Mondal, Sahil K Shah, and Vidya Kumbhar.
  Predicting credit risk in european p2p lending: A case study of
  “bondora” using supervised machine learning techniques.
  In 2023 4th IEEE Global Conference for Advancement in Technology
  (GCAT), pages 1–6. IEEE, 2023.
* [87]

  Gero Friedrich Bone-Winkel and Felix Reichenbach.
  Improving credit risk assessment in p2p lending with explainable
  machine learning survival analysis.
  Digital Finance, 6(3):501–542, 2024.
* [88]

  Harald Steck, Balaji Krishnapuram, Cary Dehing-Oberije, Philippe Lambin, and
  Vikas C Raykar.
  On ranking in survival analysis: Bounds on the concordance index.
  Advances in neural information processing systems, 20, 2007.
* [89]

  Laura Antolini, Patrizia Boracchi, and Elia Biganzoli.
  A time-dependent discrimination index for survival data.
  Statistics in medicine, 24(24):3927–3944, 2005.
* [90]

  Erika Graf, Claudia Schmoor, Willi Sauerbrei, and Martin Schumacher.
  Assessment and comparison of prognostic classification schemes for
  survival data.
  Statistics in medicine, 18(17-18):2529–2545, 1999.