---
authors:
- Miguel Alves Pereira
doc_id: arxiv:2510.04726v1
family_id: arxiv:2510.04726
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Predictive economics: Rethinking economic methodology with machine learning'
url_abs: http://arxiv.org/abs/2510.04726v1
url_html: https://arxiv.org/html/2510.04726v1
venue: arXiv q-fin
version: 1
year: 2025
---


Miguel Alves Pereira
[miguelalvespereira@tecnico.ulisboa.pt](mailto:miguelalvespereira@tecnico.ulisboa.pt)
CEGIST, Instituto Superior Técnico, Universidade de Lisboa, Av. Rovisco Pais 1, 1049-001 Lisboa, Portugal

###### Abstract

This article proposes predictive economics as a distinct analytical perspective within economics, grounded in machine learning and centred on predictive accuracy rather than causal identification. Drawing on the instrumentalist tradition (Friedman), the explanation-prediction divide (Shmueli), and the contrast between modelling cultures (Breiman), we formalise prediction as a valid epistemological and methodological objective. Reviewing recent applications across economic subfields, we show how predictive models contribute to empirical analysis, particularly in complex or data-rich contexts. This perspective complements existing approaches and supports a more pluralistic methodology - one that values out-of-sample performance alongside interpretability and theoretical structure.

###### keywords:

Predictive economics , Machine learning , Forecasting , Causal inference , Economic methodology

††journal: arXiv

{highlights}

Introduces predictive economics as a distinct analytical perspective

Frames prediction as a valid aim in economic modelling and policy design

Reviews machine learning applications across major economic subfields

Explores trade-offs between accuracy, interpretability, and structure

Advocates methodological pluralism centred on empirical performance

## 1 Introduction

The evolution of economics has long been shaped by advances in analytical tools. While theory and causal inference have dominated recent decades, the growing adoption of machine learning (ML) is prompting a shift in how economists engage with data and assess empirical models. Unlike traditional forecasting, ML-based prediction emphasises out-of-sample performance, accommodates high-dimensional settings, and informs decisions even in the absence of strong structural assumptions.

This article proposes the formalisation of predictive economics as a distinct perspective within economic methodology. Rooted in the instrumentalist tradition (Friedman), the explanation-prediction divide (Shmueli), and the contrast between modelling cultures (Breiman), this view holds that predictive accuracy is a valid scientific goal in its own right. ML’s empirical success across micro, macro, and policy applications invites a broader methodological pluralism - one that treats prediction not as subordinate to explanation, but as complementary and policy-relevant.

We clarify key distinctions between forecasting, explanation, and prediction in the ML sense, and review selected applications across economic subfields. These examples illustrate how predictive tools enhance empirical analysis, particularly where complexity, data abundance, or weak priors challenge traditional econometric techniques. We conclude by reflecting critically on the limits of this approach and its implications for the discipline’s epistemological foundations.

## 2 Prediction, forecasting, and explanation: A methodological reappraisal

The growing use of ML in economics has reignited longstanding debates about the purpose and evaluation of empirical models. Clarifying the distinction between forecasting, explanation, and prediction (in the ML sense) is essential for methodological clarity.

Forecasting typically refers to projecting future values, especially in macroeconomic or financial contexts, using parametric time series models under structural assumptions. While technically a form of prediction, it remains narrow in scope. In contrast, predictive modelling in the ML tradition spans time series, cross-sectional, and high-dimensional settings, prioritising empirical accuracy over structural coherence.

ML tools such as regularisation, cross-validation, and ensembles optimise out-of-sample performance and reduce overfitting. However, these models often do not yield interpretable parameters or testable mechanisms, departing from conventional econometric practice.

This divide reflects what Breiman [[2001](https://arxiv.org/html/2510.04726v1#bib.bib5)] termed the “two cultures”: one centred on stochastic models for inference, the other on algorithms for prediction. Economics has long prioritised the former, favouring theoretical structure and causal identification. Yet ML increasingly challenges this stance, particularly in settings with limited prior knowledge or complex nonlinear relationships.

The distinction is also epistemological. As Shmueli [[2010](https://arxiv.org/html/2510.04726v1#bib.bib20)] notes, explanatory models aim to uncover causal mechanisms, whereas predictive models focus on accurate anticipation. Conflating these aims may compromise both: interpretable models may generalise poorly, and highly predictive models can defy explanation.

Some economists view prediction and explanation as complementary. ML methods can support causal inference by adjusting for confounding or uncovering heterogeneity [Athey & Imbens, [2019](https://arxiv.org/html/2510.04726v1#bib.bib2)]. Others regard prediction as a distinct scientific aim. Friedman [[1953](https://arxiv.org/html/2510.04726v1#bib.bib11)], in an instrumentalist spirit, argued that predictive accuracy should be the principal test of a model’s value - an idea reinvigorated by ML’s empirical success.

## 3 Applications of predictive modelling in economics

The conceptual foundations outlined above have led to a growing literature demonstrating the value of predictive modelling in economics. This section reviews selected contributions across microeconomics, macroeconomics, and related fields, highlighting how ML is reshaping empirical practice, particularly where data abundance, model complexity, and the need for out-of-sample accuracy challenge traditional econometric tools.

### 3.1 Microeconomics

Microeconomics has seen some of the earliest and most extensive applications of ML, enabled by high-frequency, high-dimensional data. Predictive tools have been deployed across domains, including production analysis, demand estimation, industrial organisation, and targeted interventions.

#### Production theory and efficiency analysis

Esteve et al. [[2020](https://arxiv.org/html/2510.04726v1#bib.bib10)] propose Efficiency Analysis Trees (EAT), which adapt decision tree algorithms to estimate production frontiers while preserving economic axioms such as free disposability. In contrast to traditional nonparametric methods like Data Envelopment Analysis or Free Disposal Hull, which may overfit, EAT employs pruning and cross-validation to enhance generalisability, reducing mean squared error by 13-70% in simulations. Random Forest variants further support benchmarking, particularly in health care, while maintaining consistency with production theory.

#### Demand and supply estimation

Bajari et al. [[2015](https://arxiv.org/html/2510.04726v1#bib.bib3)] demonstrate that ensemble methods incorporating rich regressors outperform standard econometric models in predicting consumer demand using scanner data. These approaches better capture behavioural heterogeneity and support pricing and regulatory analysis. On the supply side, ML improves firm-level forecasts of output and costs, especially in non-linear settings such as energy markets.

#### Industrial organisation and market outcomes

Predictive models have been used to estimate market entry, competition, and collusion, and to inform auction design by forecasting bidder valuations and optimising reserve prices. While these models allow for more realistic simulations under weak structural assumptions, concerns remain regarding their robustness under regime shifts, underscoring the importance of integrating predictive performance with economic insight.

#### Game theory and experimental economics

Reinforcement learning models simulate adaptive strategies in repeated games, while classification algorithms predict convergence and identify behavioural types in laboratory settings. Data-driven approaches to mechanism design are also emerging, enabling the simulation of alternative allocation rules with attention to empirical outcomes.

#### Market failures and policy targeting

ML has supported risk assessment in credit and insurance markets, addressing adverse selection. In criminal justice, Kleinberg et al. [[2015](https://arxiv.org/html/2510.04726v1#bib.bib14), [2018](https://arxiv.org/html/2510.04726v1#bib.bib13)] report that predictive models outperform judges in forecasting recidivism, informing pre-trial release decisions. In labour and education, profiling methods enhance targeting of interventions, though these gains raise questions around fairness, accountability, and strategic response.

### 3.2 Macroeconomics

Macroeconomics has long focused on forecasting, particularly through time-series models. ML introduces tools capable of capturing non-linearities and handling high-dimensional datasets, enhancing predictions of GDP, inflation, unemployment, and other aggregates. These gains, however, depend on data quality, model calibration, and the structural features of the economic environment.

#### Forecasting macroeconomic indicators

Coulombe et al. [[2022](https://arxiv.org/html/2510.04726v1#bib.bib8)] show that ML models, especially tree-based methods and neural networks, outperform classical approaches in non-linear, high-dimensional contexts, particularly at long horizons and near turning points. Factor models in the tradition of Stock-Watson remain effective but often benefit from regularisation or ensemble integration. Cross-validation and hyperparameter tuning frequently improve performance over conventional model selection, though advantages are clearest when structural assumptions are weak or non-linearities matter.

#### Nowcasting and high-frequency prediction

ML has also proven useful in nowcasting, where high-frequency indicators help anticipate near-term conditions. Hall [[2018](https://arxiv.org/html/2510.04726v1#bib.bib12)] find that ML models outperform standard benchmarks and expert forecasts in short-term unemployment prediction. Incorporating alternative data sources, such as search queries and sentiment indicators, further improves nowcasts of labour and consumer activity [Choi & Varian, [2012](https://arxiv.org/html/2510.04726v1#bib.bib7)]. Einav & Levin [[2014](https://arxiv.org/html/2510.04726v1#bib.bib9)] offer a broader perspective on how these tools are reshaping empirical strategies in macroeconomics.

#### Context dependency and structural stability

ML gains tend to be modest in stable environments, where traditional forecast combinations or penalised regressions perform adequately. During disruptions, such as the COVID-19 shock, ML adapts more rapidly due to flexible retraining. Nonetheless, performance can deteriorate under structural breaks, particularly when models lack economic guidance or fail to capture behavioural feedback.

#### Macroeconomic risk and explainability

ML is increasingly applied to macro-financial forecasting. Neghab et al. [[2025](https://arxiv.org/html/2510.04726v1#bib.bib18)] predict the CAD-USD exchange rate using deep learning alongside SHapley Additive exPlanations (SHAP), illustrating how predictive accuracy and interpretability can align. These tools help uncover evolving drivers, such as oil prices, offering potential bridges between prediction and economic reasoning.

#### Hybrid approaches and institutional uptake

Some central banks are experimenting with ML-based nowcasts to support or adjust Dynamic Stochastic General Equilibrium models. This hybrid usage reflects a cautious but growing institutional interest in ML, not as a replacement for structural modelling, but as a complementary source of empirical insight.

### 3.3 Other subfields

The predictive turn extends beyond micro and macroeconomics, shaping empirical strategies in labour, public, international, and development economics. These applications illustrate how ML enhances targeting and decision-making, particularly when conventional data or models are limited.

#### Labour economics

ML methods support employment forecasting and programme design. Cengiz et al. [[2022](https://arxiv.org/html/2510.04726v1#bib.bib6)] employ survival models to predict unemployment duration more effectively than Cox models, improving the prioritisation of support. They also use ML in minimum wage studies to predict which workers are most affected, refining treatment assignments. Predictive profiling has improved recruitment and intervention targeting, though concerns over algorithmic fairness and bias underscore the need for ongoing scrutiny.

#### Public economics and policy

Public agencies increasingly adopt ML to guide enforcement and service delivery. Tax authorities use supervised models to detect likely evasion; Battaglini et al. [[2025](https://arxiv.org/html/2510.04726v1#bib.bib4)] report notable compliance gains. The U.S. Internal Revenue Service employs hybrid ML models in real time to flag potential fraud, yielding substantial savings. Outside taxation, ML supports poverty mapping and welfare targeting using non-traditional data, such as satellite imagery. Predictive tools also inform urban inspections, though these applications raise transparency and accountability concerns.

#### International economics

In international settings, ML is used to forecast exchange rates, trade flows, and sovereign risk. Pfahler [[2021](https://arxiv.org/html/2510.04726v1#bib.bib19)] and Neghab et al. [[2025](https://arxiv.org/html/2510.04726v1#bib.bib18)] show that deep learning methods modestly improve accuracy, with tools like SHAP aiding interpretability, for instance, in isolating oil prices’ influence on exchange rate movements. ML also supports export prediction, trade anomaly detection, and early warning systems for financial and geopolitical crises.

#### Other domains

ML contributes to forecasting in finance (returns, volatility, credit risk), health economics (costs, utilisation), education (dropout risk), and environmental policy (energy demand, climate conditions). Across these areas, predictive models support more efficient targeting and resource allocation, reinforcing the case for predictive economics as a pragmatic, data-driven complement to traditional approaches.

### 3.4 Limits and critical reflections

The breadth of applications reviewed above suggests that ML-based prediction enhances performance in settings marked by complexity, high dimensionality, or limited theoretical structure. In microeconomics, predictive models have improved measurement and targeting, extending empirical reach without supplanting economic reasoning. In macroeconomics, their strengths are clearest in nowcasting and non-linear dynamics, though integration with domain expertise remains essential.

Nonetheless, the predictive turn warrants caution. Sceptics argue that forecasting accuracy may be insufficient for sound policy design. The Lucas [[1976](https://arxiv.org/html/2510.04726v1#bib.bib15)] critique remains pertinent: models that ignore structural relationships risk failure under regime change, particularly when agents adapt strategically. Black-box algorithms also raise ethical and epistemological concerns, especially in domains such as justice, health, and welfare, where opacity may erode accountability and fairness. These limitations do not invalidate predictive methods but highlight the need for methodological restraint and contextual awareness.

Viewed in this light, predictive modelling complements rather than replaces traditional approaches. It introduces a pragmatic, data-driven lens focused on accuracy and actionable insight. When combined judiciously with theory and causal analysis, it enriches the economist’s toolkit, broadening its relevance without discarding its foundations.

## 4 Conclusion

The adoption of ML methods across economics marks a conceptual shift that motivates the articulation of predictive economics as a distinct analytical perspective. This approach centres predictive accuracy, especially out-of-sample performance, as a valid scientific and policy-relevant objective, rather than treating it as subordinate to explanation.

The notion of “prediction policy problems” proposed by Kleinberg et al. [[2015](https://arxiv.org/html/2510.04726v1#bib.bib14)] exemplifies this shift: the goal is to forecast individual outcomes for actionable decisions, not to estimate structural parameters. From surgery outcomes to recidivism risk, ML models provide useful insights without relying on strong assumptions. These applications challenge the traditional econometric hierarchy and support methodological pluralism.

Recent contributions [Mullainathan & Spiess, [2017](https://arxiv.org/html/2510.04726v1#bib.bib17), Kleinberg et al., [2018](https://arxiv.org/html/2510.04726v1#bib.bib13)] show that tasks like credit scoring, admissions, and audit selection are inherently predictive. In this light, empirical regularities can guide decisions even when full explanations are lacking. Prioritising predictive success over parameter interpretability reflects an instrumentalist view of model value.

Scholars such as Varian [[2014](https://arxiv.org/html/2510.04726v1#bib.bib21)] and Athey [[2018](https://arxiv.org/html/2510.04726v1#bib.bib1)] further emphasise how prediction enables personalisation, real-time policy, and improved targeting. While related notions appear in foresight literature [van der Merwe, [2011](https://arxiv.org/html/2510.04726v1#bib.bib16)], this paper formalises the concept within economic methodology.

Predictive economics complements, rather than displaces, theory and causal analysis. By recognising prediction as a legitimate aim, it expands the economist’s methodological repertoire and offers a pragmatic response to the demands of data-rich, decision-oriented contexts.

## Acknowledgements

Miguel Alves Pereira would like to thank the Portuguese Foundation for Science and Technology for supporting this research via project UIDB/00097/2025. His views (and any errors) are his own responsibility.

## References

* Athey [2018]

  Athey, S. (2018).
  The impact of machine learning on economics.
  In The Economics of Artificial Intelligence: An Agenda (pp. 507–547).
  National Bureau of Economic Research, Inc.
* Athey & Imbens [2019]

  Athey, S., & Imbens, G. W. (2019).
  Machine learning methods that economists should know about.
  Annual Review of Economics, 11, 685–725. doi:[10.1146/annurev-economics-080217-053433](http://dx.doi.org/10.1146/annurev-economics-080217-053433).
* Bajari et al. [2015]

  Bajari, P., Nekipelov, D., Ryan, S. P., & Yang, M. (2015).
  Machine learning methods for demand estimation.
  American Economic Review, 105, 481–485. doi:[10.1257/aer.p20151021](http://dx.doi.org/10.1257/aer.p20151021).
* Battaglini et al. [2025]

  Battaglini, M., Guiso, L., Lacava, C., Miller, D. L., & Patacchini, E. (2025).
  Refining public policies with machine learning: The case of tax auditing.
  Journal of Econometrics, 249, 105847. doi:[10.1016/j.jeconom.2024.105847](http://dx.doi.org/10.1016/j.jeconom.2024.105847).
* Breiman [2001]

  Breiman, L. (2001).
  Statistical modeling: The two cultures (with comments and a rejoinder by the author).
  Statistical Science, 16, 199–231. doi:[10.1214/ss/1009213726](http://dx.doi.org/10.1214/ss/1009213726).
* Cengiz et al. [2022]

  Cengiz, D., Dube, A., Lindner, A., & Zentler-Munro, D. (2022).
  Seeing beyond the trees: Using machine learning to estimate the impact of minimum wages on labor market outcomes.
  Journal of Labor Economics, 40, S203–S247. doi:[10.1086/718497](http://dx.doi.org/10.1086/718497).
* Choi & Varian [2012]

  Choi, H., & Varian, H. (2012).
  Predicting the present with google trends.
  Economic Record, 88, 2–9. doi:[10.1111/j.1475-4932.2012.00809.x](http://dx.doi.org/10.1111/j.1475-4932.2012.00809.x).
* Coulombe et al. [2022]

  Coulombe, P. G., Leroux, M., Stevanovic, D., & Surprenant, S. (2022).
  How is machine learning useful for macroeconomic forecasting?
  Journal of Applied Econometrics, 37, 880–901. doi:[10.1002/jae.2910](http://dx.doi.org/10.1002/jae.2910).
* Einav & Levin [2014]

  Einav, L., & Levin, J. (2014).
  Economics in the age of big data.
  Science, 346, 1243089. doi:[10.1126/science.1243089](http://dx.doi.org/10.1126/science.1243089).
* Esteve et al. [2020]

  Esteve, M., Aparicio, J., Rabasa, A., & Rodriguez-Sala, J. J. (2020).
  Efficiency analysis trees: A new methodology for estimating production frontiers through decision trees.
  Expert Systems with Applications, 162, 113783. URL: <https://linkinghub.elsevier.com/retrieve/pii/S0957417420306072>. doi:[10.1016/j.eswa.2020.113783](http://dx.doi.org/10.1016/j.eswa.2020.113783).
* Friedman [1953]

  Friedman, M. (1953).
  The methodology of positive economics.
  In Essays in Positive Economics (pp. 3–43).
  University of Chicago Press.
* Hall [2018]

  Hall, A. S. (2018).
  Machine learning approaches to macroeconomic forecasting.
  The Federal Reserve Bank of Kansas City Economic Review, 103, 5–32. doi:[10.18651/ER/4q18smalterhall](http://dx.doi.org/10.18651/ER/4q18smalterhall).
* Kleinberg et al. [2018]

  Kleinberg, J., Lakkaraju, H., Leskovec, J., Ludwig, J., & Mullainathan, S. (2018).
  Human decisions and machine predictions.
  The Quarterly Journal of Economics, 133, 237–293. doi:[10.1093/qje/qjx032](http://dx.doi.org/10.1093/qje/qjx032).
* Kleinberg et al. [2015]

  Kleinberg, J., Ludwig, J., Mullainathan, S., & Obermeyer, Z. (2015).
  Prediction policy problems.
  American Economic Review, 105, 491–495. doi:[10.1257/aer.p20151023](http://dx.doi.org/10.1257/aer.p20151023).
* Lucas [1976]

  Lucas, R. (1976).
  Econometric policy evaluation: A critique.
  In K. Brunner, & A. Meltzer (Eds.), The Phillips Curve and Labor Markets (pp. 19–46).
  Elsevier volume 1.
* van der Merwe [2011]

  van der Merwe, J. (2011).
  Future of the south african mining industry and the roles of the saimm and the universities.
  Journal of the Southern African Institute of Mining and Metallurgy, 111, 581–592.
* Mullainathan & Spiess [2017]

  Mullainathan, S., & Spiess, J. (2017).
  Machine learning: An applied econometric approach.
  Journal of Economic Perspectives, 31, 87–106. doi:[10.1257/jep.31.2.87](http://dx.doi.org/10.1257/jep.31.2.87).
* Neghab et al. [2025]

  Neghab, D. P., Cevik, M., Wahab, M. I. M., & Basar, A. (2025).
  Explaining exchange rate forecasts with macroeconomic fundamentals using interpretive machine learning.
  Computational Economics, 65, 1857–1899. doi:[10.1007/s10614-024-10617-1](http://dx.doi.org/10.1007/s10614-024-10617-1).
* Pfahler [2021]

  Pfahler, J. F. (2021).
  Exchange rate forecasting with advanced machine learning methods.
  Journal of Risk and Financial Management, 15, 2. doi:[10.3390/jrfm15010002](http://dx.doi.org/10.3390/jrfm15010002).
* Shmueli [2010]

  Shmueli, G. (2010).
  To explain or to predict?
  Statistical Science, 25, 289–310. doi:[10.1214/10-STS330](http://dx.doi.org/10.1214/10-STS330).
* Varian [2014]

  Varian, H. R. (2014).
  Big data: New tricks for econometrics.
  Journal of Economic Perspectives, 28, 3–28. doi:[10.1257/jep.28.2.3](http://dx.doi.org/10.1257/jep.28.2.3).