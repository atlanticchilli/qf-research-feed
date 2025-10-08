---
authors:
- Jinho Cha
- Sahng-Min Han
- Long Pham
doc_id: arxiv:2510.05487v1
family_id: arxiv:2510.05487
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial
  Optimization Perspective'
url_abs: http://arxiv.org/abs/2510.05487v1
url_html: https://arxiv.org/html/2510.05487v1
venue: arXiv q-fin
version: 1
year: 2025
---


Jinho Cha1,∗,
Sahng-Min Han1,
Long Pham2
  
  
1Department of Computer Science, Gwinnett Technical College,
  
5150 Sugarloaf Parkway, Lawrenceville, GA 30043, USA
  
2Department of Decision Sciences and Economics, College of Business,
  
Texas A&M University–Corpus Christi, 6300 Ocean Drive, Corpus Christi, TX 78412, USA
  
  
\*Corresponding author: [jcha@gwinnetttech.edu](mailto:jcha@gwinnetttech.edu)

Abstract

Background
Effective supply chain management under high-variance demand conditions requires models that jointly address demand uncertainty and the strategic adoption of digital contracting mechanisms such as smart contracts. However, existing research often either simplifies demand distributions or treats adoption as an exogenous binary decision, limiting the practical relevance of such frameworks in e-commerce and humanitarian logistics contexts.
Methods
This study develops a unified optimization framework combining dynamic Negative Binomial demand modeling with endogenous smart contract adoption. The demand process incorporates autoregressive dynamics in the success probability to capture overdispersion and temporal correlation. Simulation experiments are conducted using four real-world datasets, including Delhivery Logistics and the SCMS Global Health Delivery system. Model calibration relies on maximum likelihood estimation and grid search optimization across adoption intensity and order quantity.
Results
Across all datasets, the Negative Binomial specification demonstrates substantially superior fit relative to Poisson and Gaussian benchmarks. Overdispersion indices consistently exceed 1.5, confirming the presence of significant variance unexplained by simpler models. Forecasting comparisons show that while ARIMA and Exponential Smoothing achieve comparable point accuracy, the Negative Binomial model offers greater stability in high-variance segments. Scenario analyses reveal that when dispersion exceeds a critical threshold (e.g., r>6r>6), increasing smart contract adoption above 70% yields significant profitability improvements and service level gains. These results underscore the importance of aligning digital adoption strategies with empirically observed demand volatility.
Conclusions
This framework provides a robust analytical basis for integrating probabilistic demand modeling with incentive alignment mechanisms in digitally enabled supply chains. The approach offers actionable guidance for decision-makers seeking to balance inventory costs, service levels, and implementation expenses in uncertain environments. Future research could extend the model to multi-period dynamic programming and incorporate advanced machine learning forecasts to further enhance operational relevance.

## 1 Introduction

Supply chain management has always relied on accurate demand forecasting and carefully structured contracts to coordinate partners and optimize performance across complex networks. In recent years, however, firms have faced a substantial escalation in demand uncertainty driven by rapid market shifts, pervasive globalization, and the increasing frequency of disruptive events ranging from geopolitical tensions to extreme weather phenomena [[1](https://arxiv.org/html/2510.05487v1#bib.bib1), [2](https://arxiv.org/html/2510.05487v1#bib.bib2), [3](https://arxiv.org/html/2510.05487v1#bib.bib3), [4](https://arxiv.org/html/2510.05487v1#bib.bib4)]. Traditional forecasting approaches, including Poisson-based count models and ARIMA time-series methods, often prove inadequate in this environment because they struggle to capture overdispersion, regime shifts, and non-stationary demand dynamics [[5](https://arxiv.org/html/2510.05487v1#bib.bib5), [6](https://arxiv.org/html/2510.05487v1#bib.bib6)]. Furthermore, the accelerating proliferation of granular data streams—enabled by IoT devices, e-commerce platforms, and real-time transaction systems—has highlighted the limitations of conventional statistical models that were originally developed for more stable and predictable settings [[7](https://arxiv.org/html/2510.05487v1#bib.bib7), [8](https://arxiv.org/html/2510.05487v1#bib.bib8)]. As supply chains increasingly digitize and integrate advanced analytics, the effective use of high-dimensional data for forecasting has become both an opportunity and a challenge. Simultaneously, the value of timely information sharing and coordinated planning has been repeatedly demonstrated as a means to mitigate uncertainty and align incentives across supply chain tiers [[9](https://arxiv.org/html/2510.05487v1#bib.bib9), [10](https://arxiv.org/html/2510.05487v1#bib.bib10), [11](https://arxiv.org/html/2510.05487v1#bib.bib11)]. As a result, both researchers and practitioners have increasingly turned to more sophisticated forecasting techniques and adaptive contracting frameworks designed to enhance resilience, responsiveness, and incentive alignment within digitally transformed supply chains.

One prominent development in demand forecasting has been the adoption of overdispersed models such as the Negative Binomial (NB) distribution. The NB framework extends Poisson models by allowing variance to exceed the mean, making it particularly suited to high-variability retail environments [[12](https://arxiv.org/html/2510.05487v1#bib.bib12), [13](https://arxiv.org/html/2510.05487v1#bib.bib13)]. For example, a top-ranked solution in the M5 forecasting competition successfully combined time-varying negative binomial state-space models with exponential smoothing to improve probabilistic forecasts of Walmart sales during volatile periods [[14](https://arxiv.org/html/2510.05487v1#bib.bib14), [15](https://arxiv.org/html/2510.05487v1#bib.bib15)]. Similarly, zero-inflated NB models have proven effective for intermittent or emergency demand contexts, such as disaster relief supply estimation [[16](https://arxiv.org/html/2510.05487v1#bib.bib16)]. These advances build on earlier inventory theory emphasizing the value of flexible stochastic models for lost-sales estimation [[17](https://arxiv.org/html/2510.05487v1#bib.bib17)]. In parallel, recent reviews have highlighted that integrating machine learning techniques with stochastic forecasting methods can further enhance accuracy, particularly in environments characterized by structural breaks, nonlinear patterns, and large volumes of exogenous information [[18](https://arxiv.org/html/2510.05487v1#bib.bib18), [19](https://arxiv.org/html/2510.05487v1#bib.bib19)]. Neural networks and hybrid frameworks—including SARIMA-LSTM combinations and gradient boosting approaches—are increasingly applied to complement classical NB models and deliver robust demand predictions in retail, e-commerce, and logistics applications [[20](https://arxiv.org/html/2510.05487v1#bib.bib20), [21](https://arxiv.org/html/2510.05487v1#bib.bib21), [22](https://arxiv.org/html/2510.05487v1#bib.bib22), [23](https://arxiv.org/html/2510.05487v1#bib.bib23)].

Alongside statistical innovations, the integration of machine learning (ML) and deep learning (DL) techniques into supply chain forecasting has opened a new paradigm for data-driven decision making. Neural networks, including Long Short-Term Memory (LSTM) architectures, have demonstrated superior predictive accuracy relative to classical time-series models, particularly in environments where demand exhibits complex nonlinear relationships and interactions with multiple exogenous factors such as promotions, seasonality, or weather [[20](https://arxiv.org/html/2510.05487v1#bib.bib20), [21](https://arxiv.org/html/2510.05487v1#bib.bib21)]. Recent studies have underscored the advantages of hybrid modeling strategies, in which ML algorithms complement traditional statistical frameworks to enhance robustness and mitigate overfitting in high-dimensional data contexts [[24](https://arxiv.org/html/2510.05487v1#bib.bib24), [25](https://arxiv.org/html/2510.05487v1#bib.bib25)]. For example, combining SARIMA models with LSTM networks has been shown to reduce forecast errors by up to 18% compared to standalone methods, while simultaneously preserving interpretability of baseline seasonal patterns [[22](https://arxiv.org/html/2510.05487v1#bib.bib22), [26](https://arxiv.org/html/2510.05487v1#bib.bib26)]. Other researchers have explored convolutional neural networks, attention-based architectures, and probabilistic forecasting methods to capture long-range temporal dependencies and quantify uncertainty more effectively [[27](https://arxiv.org/html/2510.05487v1#bib.bib27), [28](https://arxiv.org/html/2510.05487v1#bib.bib28), [29](https://arxiv.org/html/2510.05487v1#bib.bib29)]. Importantly, these predictive improvements can translate into substantial operational benefits by informing inventory policies, capacity planning, and contract parameterization under uncertainty [[30](https://arxiv.org/html/2510.05487v1#bib.bib30), [31](https://arxiv.org/html/2510.05487v1#bib.bib31)]. Nevertheless, the adoption of advanced ML approaches also introduces new challenges, including extensive data requirements, significant computational cost, and persistent concerns regarding model transparency and managerial trust in automated forecasts [[29](https://arxiv.org/html/2510.05487v1#bib.bib29), [19](https://arxiv.org/html/2510.05487v1#bib.bib19)].

At the same time, the rise of blockchain technology has inspired researchers to fundamentally reconsider how contracts are designed, enforced, and monitored across global supply chains. Smart contracts—self-executing agreements deployed on decentralized ledgers—offer the promise of automated, transparent, and tamper-proof contract enforcement mechanisms [[32](https://arxiv.org/html/2510.05487v1#bib.bib32), [33](https://arxiv.org/html/2510.05487v1#bib.bib33)]. Empirical studies and game-theoretic models indicate that blockchain-based contracts can improve coordination by reducing delivery risks, lowering transaction costs, and aligning incentives among distributed partners more effectively than traditional agreements [[34](https://arxiv.org/html/2510.05487v1#bib.bib34), [35](https://arxiv.org/html/2510.05487v1#bib.bib35), [36](https://arxiv.org/html/2510.05487v1#bib.bib36)]. For example, dynamically adjusting wholesale prices or revenue shares based on real-time production or shipment data captured on blockchain can achieve decentralized first-best coordination that previously required centralized oversight [[37](https://arxiv.org/html/2510.05487v1#bib.bib37), [38](https://arxiv.org/html/2510.05487v1#bib.bib38)]. Other scholars have emphasized the role of blockchain platforms in enhancing traceability, provenance verification, and trust in complex multi-tier networks, particularly in industries such as food logistics and pharmaceuticals [[39](https://arxiv.org/html/2510.05487v1#bib.bib39), [40](https://arxiv.org/html/2510.05487v1#bib.bib40), [41](https://arxiv.org/html/2510.05487v1#bib.bib41)]. Moreover, simulation-based analyses show that blockchain can facilitate rapid dispute resolution and enable incentive-compatible contract execution under stochastic demand and supply disruptions [[42](https://arxiv.org/html/2510.05487v1#bib.bib42), [43](https://arxiv.org/html/2510.05487v1#bib.bib43)]. Nevertheless, concerns remain regarding adoption barriers, interoperability challenges, scalability constraints, and potential prisoner’s dilemma scenarios if only one party commits to smart contracting [[44](https://arxiv.org/html/2510.05487v1#bib.bib44), [45](https://arxiv.org/html/2510.05487v1#bib.bib45)].

The increasing frequency of disruptive events and chronic volatility has underscored the necessity of both agile forecasting and adaptive contracting in contemporary supply chains. Under conditions of high uncertainty, traditional rigid contracts—such as fixed-quantity or static wholesale agreements—often fail to align incentives and allocate risk efficiently [[46](https://arxiv.org/html/2510.05487v1#bib.bib46), [47](https://arxiv.org/html/2510.05487v1#bib.bib47)]. Prior studies have underscored the importance of more flexible contractual arrangements, including quantity flexibility provisions, options contracts, and revenue-sharing mechanisms, which can be dynamically adjusted as new information emerges [[48](https://arxiv.org/html/2510.05487v1#bib.bib48), [49](https://arxiv.org/html/2510.05487v1#bib.bib49)]. Empirical investigations and simulation analyses have shown that such adaptive agreements can improve performance metrics such as service levels, profit variability, and responsiveness to demand shocks [[50](https://arxiv.org/html/2510.05487v1#bib.bib50), [51](https://arxiv.org/html/2510.05487v1#bib.bib51)]. Moreover, integrating advanced forecasting models with contingent contract clauses enables firms to link replenishment decisions to real-time demand signals and collaboratively manage uncertainty across supply networks [[52](https://arxiv.org/html/2510.05487v1#bib.bib52)]. For example, Zhao et al. [[53](https://arxiv.org/html/2510.05487v1#bib.bib53)] demonstrate that forecast sharing combined with state-contingent contracts can reduce both safety stock and coordination costs. Other contributions have emphasized the strategic value of combining option-based contracts with information-sharing platforms to mitigate the bullwhip effect and enhance supply chain resilience [[54](https://arxiv.org/html/2510.05487v1#bib.bib54), [55](https://arxiv.org/html/2510.05487v1#bib.bib55)]. Despite these advances, persistent challenges remain in designing agreements that balance incentive compatibility, information asymmetry, and operational feasibility in highly dynamic environments [[56](https://arxiv.org/html/2510.05487v1#bib.bib56)].

Classic theories of forecasting-integrated supply chain management, such as the state-space Kalman filtering framework proposed by Aviv, remain highly relevant. Equally, foundational analyses of revenue-sharing contracts and their strengths and limitations continue to inform contemporary research. However, despite the rapid evolution of advanced predictive models and flexible contracting mechanisms, a clear gap persists in integrating these innovations into unified frameworks that explicitly link demand forecasting with adaptive contract execution. Recent studies have demonstrated that machine learning and big data analytics can substantially enhance forecast accuracy under complex and volatile demand patterns [[57](https://arxiv.org/html/2510.05487v1#bib.bib57), [58](https://arxiv.org/html/2510.05487v1#bib.bib58), [59](https://arxiv.org/html/2510.05487v1#bib.bib59)]. At the same time, research on blockchain-based platforms highlights their potential to automate information sharing and incentive alignment across multi-tier networks [[60](https://arxiv.org/html/2510.05487v1#bib.bib60), [61](https://arxiv.org/html/2510.05487v1#bib.bib61)]. Yet, there is limited empirical evidence on how probabilistic forecasts can be operationalized within dynamic contractual arrangements that respond in near real-time to evolving demand signals [[62](https://arxiv.org/html/2510.05487v1#bib.bib62), [63](https://arxiv.org/html/2510.05487v1#bib.bib63)]. Emerging frameworks in predictive and prescriptive analytics suggest that integrating data-driven forecasting with prescriptive optimization holds significant promise for improving supply chain resilience and performance [[64](https://arxiv.org/html/2510.05487v1#bib.bib64), [65](https://arxiv.org/html/2510.05487v1#bib.bib65)]. Nonetheless, implementing such integrated systems requires addressing critical challenges, including data interoperability, model interpretability, and the behavioral dynamics of contract negotiation in uncertain environments [[66](https://arxiv.org/html/2510.05487v1#bib.bib66), [4](https://arxiv.org/html/2510.05487v1#bib.bib4)].

This study aims to address this gap by developing an integrated framework that combines advanced machine learning-based demand forecasting with adaptive smart contract mechanisms for supply chain coordination. Specifically, we propose a modeling approach that links probabilistic forecast outputs to dynamic contractual terms, enabling automated, real-time adjustments to ordering policies and incentive structures. By bridging these domains, our work contributes theoretically by extending the literature on forecasting-integrated supply chain management and practically by offering actionable guidelines for implementing resilient, data-driven contracting strategies in volatile environments.

## 2 Materials and Methods

### 2.1 Data Sources

Table [1](https://arxiv.org/html/2510.05487v1#S2.T1 "Table 1 ‣ 2.1 Data Sources ‣ 2 Materials and Methods ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") summarizes the datasets utilized in this study. These datasets span multiple e-commerce and logistics contexts, covering different countries, periods, and operational characteristics, thereby enabling a comprehensive evaluation of forecasting and contracting strategies across heterogeneous operational environments [[2](https://arxiv.org/html/2510.05487v1#bib.bib2), [7](https://arxiv.org/html/2510.05487v1#bib.bib7)].

Table 1: Summary of Datasets Utilized

| Dataset | Country | Period | Records | Main Variables |
| --- | --- | --- | --- | --- |
| Global Superstore | International | 2011–2014 | 51,290 | Quantity, Unit Price, Ship Date |
| E-Commerce Orders | India | 2019–2020 | 65,000 | Order Date, Quantity, Lead Time |
| Delhivery Logistics | India | 2018 | 148,170 | Trip Dates, Route Type, Delay Days |
| SCMS Delivery History | Global | 2015–2017 | 9,215 | Order Volume, Delivery Costs, Delays |

The Global Superstore dataset was primarily employed to calibrate the Negative Binomial demand model, owing to its extended temporal coverage and rich transactional granularity. Daily transactions were aggregated to monthly demand series by summing order quantities within each calendar month. This aggregation produced 48 observations (January 2011 to December 2014), which were subsequently used to estimate distribution parameters via maximum likelihood estimation. The resulting time series exhibited substantial overdispersion (variance-to-mean ratio exceeding 2.5), thereby justifying the use of count-based stochastic models rather than Gaussian approximations [[12](https://arxiv.org/html/2510.05487v1#bib.bib12)].

The E-Commerce Orders dataset served as the primary validation benchmark, reflecting a contemporary, high-volume retail environment characterized by temporal demand autocorrelation, frequent promotional events, and variable lead times. This dataset enabled testing of the autoregressive component of the demand model and assessment of forecast accuracy under complex seasonality and intermittency patterns [[18](https://arxiv.org/html/2510.05487v1#bib.bib18), [19](https://arxiv.org/html/2510.05487v1#bib.bib19)].

The Delhivery Logistics and SCMS Delivery History datasets were used for robustness and sensitivity analyses. In particular, these datasets facilitated evaluation of how lead time variability and delivery delays affect service level penalties and procurement cost variability, which are critical dimensions in digital supply chain contracting contexts [[32](https://arxiv.org/html/2510.05487v1#bib.bib32), [45](https://arxiv.org/html/2510.05487v1#bib.bib45)].

All data, Python code, figures, and derived output files (Excel spreadsheets) used in this study are available in a public Kaggle repository (see Appendix A for detailed access information).

### 2.2 Data Preprocessing and Aggregation Pipeline

All datasets underwent the following preprocessing pipeline prior to modeling and simulation:

1. 1.

   Standardization: All date fields were converted to ISO 8601 format (YYYY-MM-DD). Units of measure were harmonized across datasets (e.g., converting kilograms to units when necessary).
2. 2.

   Missing Value Handling: Observations with missing order quantities or shipment dates were removed. For records with incomplete price information, median imputation within the same product category was applied.
3. 3.

   Outlier Filtering: To reduce the impact of spurious large orders, demand values above the 99th percentile within each month were capped at the 99th percentile threshold.
4. 4.

   Temporal Aggregation: Daily transactions were aggregated to monthly totals for estimation of Negative Binomial parameters. For datasets containing shipment delay data, lead time distributions were computed monthly.
5. 5.

   Variance and Autocorrelation Analysis: The overdispersion index (variance-to-mean ratio) and first-lag autocorrelation were computed for each dataset to quantify temporal dependence and demand variability.
   Unless otherwise noted, all monetary values were converted to and reported in U.S. Dollars (USD).

Table [2](https://arxiv.org/html/2510.05487v1#S2.T2 "Table 2 ‣ 2.2 Data Preprocessing and Aggregation Pipeline ‣ 2 Materials and Methods ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") summarizes the core variables standardized across datasets wherever applicable. Not all fields were available in every dataset; when necessary, missing fields were imputed or excluded as described above.

Table 2: Core Dataset Columns, Recommended Usage, and Example Values

| Column Name | Status | Example Value | Notes |
| --- | --- | --- | --- |
| Date | Required | 2022-01 | Calendar period used for aggregation and modeling |
| Product ID | Required | 1234 | Segmentation by product identifier (SKU)1 |
| Quantity Ordered | Required | 53 | Monthly or order-level demand quantity |
| Quantity Backordered | Recommended | 8 | Captures unmet demand due to stockouts |
| Fulfilled Quantity | Recommended | 45 | Supports calculation of fill rate metrics |
| Unit Price | Recommended | 25 USD | Enables revenue estimation |
| Stockout Flag | Recommended | 0/1 | Indicator of backordered status |
| Supplier ID | Recommended | A23 | Supplier-specific performance tracking |
| Supplier Readiness Score | Optional | 0.0–1.0 | Proxy for digital maturity |
| Lead Time (Days) | Recommended | 7 | Key input for service level modeling |
| Fulfillment Delay Flag | Recommended | 0/1 | Delivery compliance indicator (SLA)2 |

* 1

  SKU: Stock Keeping Unit.
* 2

  SLA: Service Level Agreement.

All variables marked as *Required* were consistently available across all datasets and formed the basis of the core analyses. Variables designated as *Recommended* or *Optional* were incorporated wherever available to improve model calibration, enrich scenario analyses, and support robustness checks. All preprocessing scripts were implemented in Python 3.10 using pandas and numpy libraries. Complete code and data processing workflows are available upon request to support reproducibility.

### 2.3 Parameter Estimation and Simulation

For the Negative Binomial demand model, the dispersion parameter rr and baseline success probability pp were estimated by maximizing the log-likelihood function:

|  |  |  |
| --- | --- | --- |
|  | ℓ​(r,p)=∑t=1Tlog⁡[(Dt+r−1Dt)​pr​(1−p)Dt].\ell(r,p)=\sum\_{t=1}^{T}\log\Bigl[\binom{D\_{t}+r-1}{D\_{t}}p^{r}(1-p)^{D\_{t}}\Bigr]. |  |

Initial values for rr and pp were obtained using method of moments estimates, exploiting the relationships between the observed mean and variance:

|  |  |  |
| --- | --- | --- |
|  | r^=y¯2s2−y¯,p^=r^r^+y¯,\hat{r}=\frac{\bar{y}^{2}}{s^{2}-\bar{y}},\quad\hat{p}=\frac{\hat{r}}{\hat{r}+\bar{y}}, |  |

where y¯\bar{y} denotes the sample mean and s2s^{2} denotes the sample variance.

To account for temporal autocorrelation in demand variability, the autoregressive parameter ρ\rho was estimated using ordinary least squares regression applied to lagged success probabilities reconstructed from moment estimates:

|  |  |  |
| --- | --- | --- |
|  | ρ^=∑t(pt−p¯)​(pt−1−p¯)∑t(pt−1−p¯)2,\hat{\rho}=\frac{\sum\_{t}(p\_{t}-\bar{p})(p\_{t-1}-\bar{p})}{\sum\_{t}(p\_{t-1}-\bar{p})^{2}}, |  |

where ptp\_{t} denotes the estimated success probability in period tt.

Simulations were conducted across 10,000 Monte Carlo replications per scenario, with each scenario varying demand volatility, smart contract adoption levels, and penalty weights. For each replication, service level metrics (fill rate, stockout probability), expected profit, and cost components were recorded to evaluate the stability and performance of the procurement strategies. This approach ensured that the model’s recommendations were robust to stochastic fluctuations and parameter uncertainty.

### 2.4 Problem Definition

This study addresses the problem of determining optimal procurement decisions in an e-commerce supply chain context characterized by discrete, overdispersed demand and the adoption of smart contracts. Specifically, the decision variables include the order quantities procured from each supplier and the level of smart contract adoption, denoted by α\alpha. These factors jointly influence procurement costs, operational risk exposure, and incentive alignment between trading partners.

Building on the revenue-sharing contract framework proposed by Cachon and Lariviere [[67](https://arxiv.org/html/2510.05487v1#bib.bib67)], the model incorporates a procurement cost component that adjusts dynamically with the adoption level. This structure allows smart contract adoption to be interpreted not merely as a cost reduction mechanism but also as a contractual arrangement that redistributes operational gains across the supply chain, reflecting the potential for blockchain-enabled coordination.

To accurately capture the stochastic nature of demand, the process is modeled as a Negative Binomial random variable. This specification accommodates the discrete count data and overdispersion commonly observed in spare parts and consumables distribution, where variance often exceeds the mean. To further enhance realism, the success probability parameter ptp\_{t} evolves over time according to an autoregressive process:

|  |  |  |  |
| --- | --- | --- | --- |
|  | pt=ρ​pt−1+ϵt,p\_{t}=\rho\,p\_{t-1}+\epsilon\_{t}, |  | (1) |

where ρ∈(0,1)\rho\in(0,1) captures temporal dependence in demand uncertainty and ϵt\epsilon\_{t} denotes an independent noise term. This formulation introduces time-dependent variability in demand realizations, enabling the model to reflect dynamic uncertainty prevalent in e-commerce procurement environments.

The optimization objective is to simultaneously determine order quantities and the smart contract adoption level α\alpha that maximize expected profit, subject to holding costs, stockout penalties, variance penalties, service level constraints, and revenue-sharing adjustments. This objective function explicitly balances short-term profitability with risk management and contractual performance.

The procurement cost function draws on the revenue-sharing contract framework extended to account for nonlinear adoption effects and supplier digital readiness heterogeneity. Specifically, the model specifies a procurement cost of the form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | c​(α,βi)=ci0−A1​α−A2​βi−A3​α​βi−A4​ϕ​(α),c(\alpha,\beta\_{i})=c\_{i}^{0}-A\_{1}\alpha-A\_{2}\beta\_{i}-A\_{3}\alpha\beta\_{i}-A\_{4}\phi(\alpha), |  | (2) |

where A1A\_{1} represents the marginal adoption effect, A2A\_{2} denotes supplier readiness sensitivity, A3A\_{3} captures interaction effects between adoption and readiness, and A4A\_{4} governs the curvature of the nonlinear adoption cost function ϕ​(α)\phi(\alpha). This formulation enables endogenous modeling of how varying degrees of digital adoption and supplier readiness jointly impact procurement efficiency, cost structures, and revenue distribution.

Taken together, the problem formulation integrates discrete demand uncertainty, time-dependent overdispersion, and endogenous smart contract adoption decisions within a unified optimization framework. This approach advances prior models by explicitly combining operational considerations and contractual innovation in environments characterized by both high stochastic variability and technological transformation.

### 2.5 Notation and Assumptions

Table [3](https://arxiv.org/html/2510.05487v1#S2.T3 "Table 3 ‣ 2.5 Notation and Assumptions ‣ 2 Materials and Methods ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") summarizes all key variables, parameters, and assumptions used in the model.

Table 3: Notation and Definitions

| Symbol | Description |
| --- | --- |
| DtD\_{t} | Demand in period tt |
| rr | Dispersion parameter of the Negative Binomial distribution |
| ptp\_{t} | Success probability evolving over time |
| ρ\rho | Autoregressive parameter governing ptp\_{t} |
| ϵt\epsilon\_{t} | White noise term in the AR(1) process for ptp\_{t} |
| QQ | Total order quantity |
| α\alpha | Smart contract adoption level |
| βi\beta\_{i} | Supplier digital readiness index |
| c​(α,βi)c(\alpha,\beta\_{i}) | Procurement cost function incorporating revenue sharing |
| ψ​(α)\psi(\alpha) | Nonlinear adoption cost function |
| hh | Unit holding cost |
| rpr\_{p} | Unit stockout penalty cost |
| κ\kappa | Variance penalty coefficient |
| η\eta | Fill rate penalty coefficient |
| τ\tau | Target fill rate service level |
| γ\gamma | Weight of the risk aversion penalty |
| λ\lambda | Risk aversion exponent |
| AA, ν\nu | Nonlinear adoption cost parameters |

Assumptions:
Demand follows a Negative Binomial distribution with autoregressive dynamics in the success probability. Suppliers differ in digital readiness, which affects procurement costs. The retailer optimizes expected profit under holding costs, stockout penalties, variance penalties, service level penalties, and risk aversion considerations.

### 2.6 Demand Model

Demand is modeled as a Negative Binomial process with autoregressive dynamics:

|  |  |  |
| --- | --- | --- |
|  | Dt∼Negative Binomial​(r,pt),pt=ρ​pt−1+ϵt,D\_{t}\sim\text{Negative Binomial}(r,p\_{t}),\quad p\_{t}=\rho p\_{t-1}+\epsilon\_{t}, |  |

where ϵt\epsilon\_{t} represents white noise, typically assumed to be i.i.d. and normally distributed as ϵt∼𝒩​(0,σϵ2)\epsilon\_{t}\sim\mathcal{N}(0,\sigma\_{\epsilon}^{2}). Since pt∈(0,1)p\_{t}\in(0,1), the process may be truncated or transformed (e.g., via logistic mapping) to ensure boundedness.

The probability mass function is given by:

|  |  |  |
| --- | --- | --- |
|  | f​(x)=(x+r−1x)​ptr​(1−pt)x.f(x)=\binom{x+r-1}{x}p\_{t}^{r}(1-p\_{t})^{x}. |  |

The expectation and variance of DtD\_{t} are:

|  |  |  |
| --- | --- | --- |
|  | 𝔼​[Dt]=r​1−ptpt,Var​[Dt]=r​1−ptpt2.\mathbb{E}[D\_{t}]=r\frac{1-p\_{t}}{p\_{t}},\quad\text{Var}[D\_{t}]=r\frac{1-p\_{t}}{p\_{t}^{2}}. |  |

The overdispersion index is defined as:

|  |  |  |
| --- | --- | --- |
|  | Overdispersion Index=Var​[Dt]𝔼​[Dt]=1pt.\text{Overdispersion Index}=\frac{\text{Var}[D\_{t}]}{\mathbb{E}[D\_{t}]}=\frac{1}{p\_{t}}. |  |

Parameters are estimated via maximum likelihood estimation, and the overdispersion index is computed to quantify variability relative to the mean.

### 2.7 Cost and Penalty Functions

The model incorporates multiple cost components relevant to e-commerce spare parts logistics. These elements capture the operational trade-offs between service reliability, inventory costs, demand variability, and digital contract adoption. The specific formulations and interpretations are presented below:

* •

  Holding Cost: Inventory holding cost per surplus unit:

  |  |  |  |
  | --- | --- | --- |
  |  | Ch​o​l​d​i​n​g​(Q,Dt)=h⋅(Q−Dt)+.C\_{holding}(Q,D\_{t})=h\cdot(Q-D\_{t})^{+}. |  |

  This term reflects warehousing, obsolescence, and capital carrying costs incurred when excess inventory remains unsold. In spare parts logistics, surplus inventory can tie up working capital and increase the risk of outdated stock.
* •

  Stockout Penalty: Penalty for unmet demand:

  |  |  |  |
  | --- | --- | --- |
  |  | Cs​t​o​c​k​o​u​t​(Q,Dt)=rp⋅(Dt−Q)+.C\_{stockout}(Q,D\_{t})=r\_{p}\cdot(D\_{t}-Q)^{+}. |  |

  This component captures the cost of backorders, emergency shipments, and reputational loss due to unfulfilled customer orders. For mission-critical spare parts, stockouts can lead to contractual penalties or customer attrition.
* •

  Variance Penalty: Penalizes high demand variability:

  |  |  |  |
  | --- | --- | --- |
  |  | Cv​a​r​i​a​n​c​e=κ⋅Var​[Dt].C\_{variance}=\kappa\cdot\text{Var}[D\_{t}]. |  |

  Demand volatility complicates procurement and inventory planning. This penalty incentivizes strategies that reduce variance through predictive analytics, supplier collaboration, or flexible sourcing agreements.
* •

  Service Level Target Penalty: Quadratic penalty for failing to meet a fill rate target τ\tau:

  |  |  |  |
  | --- | --- | --- |
  |  | Cf​i​l​l​r​a​t​e​(Q)=η⋅(τ−ℙ​(Dt≤Q))2.C\_{fillrate}(Q)=\eta\cdot\bigl(\tau-\mathbb{P}(D\_{t}\leq Q)\bigr)^{2}. |  |

  This term models the importance of maintaining a contractual service level agreement (SLA). Deviations from the target fill rate may trigger penalties, expedited fulfillment costs, or loss of preferred supplier status.
* •

  Nonlinear Smart Contract Adoption Cost:

  |  |  |  |
  | --- | --- | --- |
  |  | ψ​(α)=A⋅αν.\psi(\alpha)=A\cdot\alpha^{\nu}. |  |

  The convex structure represents the increasing marginal cost of implementing and scaling smart contract solutions. Initial investments may be moderate, but achieving full integration requires significant resources, training, and process re-engineering.
* •

  Revenue Sharing Adjustment:

  |  |  |  |
  | --- | --- | --- |
  |  | c​(α,βi)=ci0−A1​α−A2​βi−A3​α​βi−A4​ϕ​(α).c(\alpha,\beta\_{i})=c\_{i}^{0}-A\_{1}\alpha-A\_{2}\beta\_{i}-A\_{3}\alpha\beta\_{i}-A\_{4}\phi(\alpha). |  |

  This function, inspired by revenue-sharing formulations in prior studies [[67](https://arxiv.org/html/2510.05487v1#bib.bib67)], models procurement cost reductions attributable to digital readiness and contract adoption.

These components together provide a flexible and realistic framework for evaluating the economic impact of smart contract adoption, service level commitments, and demand uncertainty in dynamic e-commerce supply chains.

### 2.8 Objective Function

The comprehensive objective function integrates all revenue, cost, and penalty terms and is formulated as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | maxα,qi\displaystyle\max\_{\alpha,q\_{i}}\quad | 𝔼​[p⋅min⁡(Q,Dt)+s​(Q−Dt)+−r​(Dt−Q)+−h​(Q−Dt)+]\displaystyle\mathbb{E}\Big[p\cdot\min(Q,D\_{t})+s(Q-D\_{t})^{+}-r(D\_{t}-Q)^{+}-h(Q-D\_{t})^{+}\Big] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | −∑i[ci0−A1​α−A2​βi−A3​α​βi−A4​ϕ​(α)]​qi−ψ​(α)\displaystyle\quad-\sum\_{i}\Big[c\_{i}^{0}-A\_{1}\alpha-A\_{2}\beta\_{i}-A\_{3}\alpha\beta\_{i}-A\_{4}\phi(\alpha)\Big]q\_{i}-\psi(\alpha) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | −γ⋅ℙ​(Dt>Q)λ−κ⋅Var​[Dt]−η⋅(τ−ℙ​(Dt≤Q))2.\displaystyle\quad-\gamma\cdot\mathbb{P}(D\_{t}>Q)^{\lambda}-\kappa\cdot\text{Var}[D\_{t}]-\eta\cdot\Big(\tau-\mathbb{P}(D\_{t}\leq Q)\Big)^{2}. |  | (3) |

This optimization is subject to the following constraints:

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | 0≤α≤1,\displaystyle 0\leq\alpha\leq 1, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | qi≥0,∀i,\displaystyle q\_{i}\geq 0,\quad\forall i, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | ∑i[ci0−A1​α−A2​βi−A3​α​βi−A4​ϕ​(α)]⋅qi≤B,\displaystyle\sum\_{i}\bigl[c\_{i}^{0}-A\_{1}\alpha-A\_{2}\beta\_{i}-A\_{3}\alpha\beta\_{i}-A\_{4}\phi(\alpha)\bigr]\cdot q\_{i}\leq B, |  |

where BB denotes a budget limit for procurement expenditures and the procurement cost function expands as shown to reflect revenue-sharing adjustments and smart contract adoption effects.

### 2.9 Solution Approach

A simulation-based grid search optimization was performed to identify optimal decisions. For each candidate combination of α\alpha and {qi}\{q\_{i}\}, 10,000 Monte Carlo samples of DtD\_{t} were generated to evaluate the expected profit, variance, and service level metrics. The grid search iterated over discrete intervals of α\alpha in [0,1][0,1] (e.g., increments of 0.050.05) and feasible order quantities within budget constraints. At each grid point, the objective function was computed, and the combination yielding the maximum expected profit was selected as the optimal policy. The simulation procedure is summarized in Algorithm [1](https://arxiv.org/html/2510.05487v1#alg1 "Algorithm 1 ‣ 2.9 Solution Approach ‣ 2 Materials and Methods ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective").

Algorithm 1  Simulation-based grid search algorithm to determine optimal smart contract adoption level α\alpha and order quantities {qi}\{q\_{i}\}, including Monte Carlo estimation of expected profit, variance, and fill rate under Negative Binomial demand.

1:Define discrete grid of α\alpha in [0,1][0,1] with step size Δ​α\Delta\alpha

2:Define feasible grid of qiq\_{i} satisfying budget constraint

3:for each α\alpha in grid do

4:  for each {qi}\{q\_{i}\} in grid do

5:   Initialize arrays to store simulation outputs

6:   for m=1m=1 to MM (Monte Carlo replications) do

7:     Simulate pt=ρ​pt−1+ϵtp\_{t}=\rho p\_{t-1}+\epsilon\_{t}

8:     Draw Dt∼Negative Binomial​(r,pt)D\_{t}\sim\text{Negative Binomial}(r,p\_{t})

9:     Compute revenue and all cost components

10:     Record total profit for replication mm

11:   end for

12:   Compute expected profit, variance, and fill rate across replications

13:  end for

14:end for

15:Select α∗\alpha^{\*} and {qi∗}\{q\_{i}^{\*}\} maximizing expected profit

All simulations were implemented in Python (version 3.10) using NumPy and SciPy libraries. Computations were parallelized across 16 CPU cores to expedite execution, requiring approximately 4–6 hours of wall-clock time per complete grid search. Simulation outputs, including replication-level profit and fill rate metrics, were stored for subsequent analysis and visualization.

Random seeds were fixed across replications to ensure reproducibility of simulation outputs. Specifically, simulations were repeated with seeds 0, 42, 1234, and 2023, yielding consistent expected profit estimates within a 0.5% tolerance. In cases of equal expected profit across candidate solutions, the configuration with the highest fill rate was selected as the optimal policy. Average memory utilization during simulations ranged between 12–16 GB per process. Convergence diagnostics indicated that increasing the number of Monte Carlo replications beyond 10,000 resulted in marginal changes (less than 0.5%) in expected profit and fill rate estimates, confirming the stability of the results.

![Refer to caption](simulation_flowchart.png)


Figure 1: Simulation procedure and parameter estimation workflow.

Simulation procedure and parameter estimation workflow. Each scenario in the grid search iteratively draws Monte Carlo samples of the demand process, computes profit and service level metrics, and aggregates results to identify optimal policies.

### 2.10 Model Fit Testing

Model adequacy was assessed by comparing the Negative Binomial and Poisson models using two standard criteria widely recommended in the discrete demand modeling literature:

* •

  Akaike Information Criterion (AIC): A lower AIC indicates a more parsimonious model with superior in-sample fit.
* •

  Likelihood Ratio Test (LRT): Evaluates whether the additional dispersion parameter in the Negative Binomial specification significantly improves the model relative to the simpler Poisson baseline.

Empirical analysis revealed consistently high overdispersion indices across all datasets, ranging from 1.5 to 4.2, strongly suggesting that the Poisson assumption of equidispersion (variance equal to mean) was violated. The Negative Binomial model achieved substantial improvements in log-likelihood and AIC in each case. For example, in the Global Superstore dataset, the AIC decreased by over 15 points, and the LRT p-value was below 0.001, indicating the superiority of the Negative Binomial formulation. Full model fit statistics and p-values for all datasets are reported in Section [3](https://arxiv.org/html/2510.05487v1#S3 "3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective").

These findings validate the decision to adopt a discrete overdispersed modeling approach and support its applicability to real-world e-commerce demand patterns characterized by sporadic bulk orders and high variability.

### Robustness and Sensitivity Analysis

Extensive robustness and sensitivity analyses were performed to examine the stability of optimal policies under plausible ranges of parameter uncertainty. The following key parameters were systematically varied:

* •

  Negative Binomial Distribution Parameters: The dispersion parameter rr was varied within ±\pm20% of its baseline estimate, and the success probability pp was adjusted incrementally to test sensitivity to demand mean-variance configurations.
* •

  Variance Penalty Coefficient κ\kappa: Evaluated across the range 1 to 4, to assess the impact of different levels of risk aversion to demand variability.
* •

  Smart Contract Adoption Parameters: The adoption level α\alpha and the nonlinear cost parameters (A,ν)(A,\nu) were jointly varied to test whether convexity in the cost function materially altered adoption incentives.
* •

  Revenue Sharing Coefficient A4A\_{4}: Incremented in steps of 0.5 to assess sensitivity of procurement cost reductions and contractual incentive alignment.

Additional robustness checks included:

* •

  Random Seed Variation: Simulations were rerun across five distinct random seeds (0, 42, 99, 1234, and 2023), yielding expected profit deviations within a 0.5% tolerance band.
* •

  Bootstrap Confidence Intervals: Constructed from 1,000 resamples to quantify uncertainty in expected profit and fill rate estimates.

Results demonstrated that the model outputs were remarkably stable across all tested configurations. In particular, the rank order of optimal policies and the threshold adoption levels were preserved, supporting the practical reliability of the proposed approach even under substantial parameter perturbations. Detailed numerical results and visual summaries of sensitivity analyses are reported in Section [3](https://arxiv.org/html/2510.05487v1#S3 "3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective").

### 2.11 Model Parameters

Table [4](https://arxiv.org/html/2510.05487v1#S2.T4 "Table 4 ‣ 2.11 Model Parameters ‣ 2 Materials and Methods ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") reports all parameter values used in the simulation experiments, including units, calibration ranges, and data sources. Each parameter reflects key dimensions of the procurement environment: demand overdispersion, service level penalties, smart contract adoption costs, and risk aversion.

Table 4: Model Parameters and Calibration Sources

| Parameter | Value | Unit | Typical Range | Source/Notes |
| --- | --- | --- | --- | --- |
| rr | 4.5 | – | 3–7 | Historical demand estimates |
| pp | 0.3 | – | 0.2–0.4 | Maximum likelihood estimation |
| ρ\rho | 0.6 | – | 0.4–0.7 | Estimated autocorrelation |
| hh | $2 | per unit per month | 1–3 | Industry reports |
| rpr\_{p} | $15 | per unit | 10–20 | SLA penalty benchmarks |
| κ\kappa | 2 | $ per variance unit | 1–4 | Risk-adjusted cost estimation |
| γ\gamma | 5 | $ | 3–7 | Managerial estimate |
| λ\lambda | 2 | – | 1–3 | Nonlinear penalty shape |
| τ\tau | 0.90 | proportion | 0.85–0.95 | Service level target |
| A1A\_{1} | 5 | $ per unit adoption | 4–6 | Blockchain implementation cost |
| A2A\_{2} | 3 | $ per readiness level | 2–4 | Supplier readiness effect |
| A3A\_{3} | 3 | $ | 2–4 | Interaction cost impact |
| A4A\_{4} | 4 | $ | 3–5 | Revenue-sharing effect |

All parameter values were selected based on a combination of published studies, industry benchmarks, and empirical calibration using the datasets described in Section [2.1](https://arxiv.org/html/2510.05487v1#S2.SS1 "2.1 Data Sources ‣ 2 Materials and Methods ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective"). Sensitivity experiments were systematically conducted around these baseline values to confirm the robustness of the results. Specific calibration references and additional details are provided in the Appendix.

## 3 Results

This section reports simulation and estimation results across four datasets to assess the performance, robustness, and generalizability of the proposed model.

### 3.1 Baseline Calibration and Sensitivity (Global Superstore Dataset)

We first calibrated the Negative Binomial demand model on the Global Superstore Monthly Demand data. Estimated parameters were r=5.32r=5.32 and p=0.0014p=0.0014. Figure [2](https://arxiv.org/html/2510.05487v1#S3.F2 "Figure 2 ‣ 3.1 Baseline Calibration and Sensitivity (Global Superstore Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") provides side-by-side visualizations of the simulated Negative Binomial demand and the empirical distribution, highlighting the model’s capacity to replicate the observed overdispersion.

![Refer to caption](simulated_negative_binomial_demand.png)


(a) Histogram of simulated Negative Binomial demand

![Refer to caption](Actual_vs_Simulated_Demand_KDE.png)


(b) KDE comparison of actual and simulated demand (Global Superstore)

Figure 2: Distributional comparison between empirical and simulated demand

Table [5](https://arxiv.org/html/2510.05487v1#S3.T5 "Table 5 ‣ 3.1 Baseline Calibration and Sensitivity (Global Superstore Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") reports the baseline expected profit and variance under the calibrated model.

Table 5: Baseline Scenario Performance Metrics (Global Superstore)

| Metric | Value | Unit |
| --- | --- | --- |
| Expected Profit | 15,200 | USD |
| Profit Variance | 3,500 | USD2 |
| Fill Rate | 88 | % |
| Optimal Adoption Level (α\alpha) | 0.55 | – |

Variance penalties and dispersion parameter sensitivity were also explored to test robustness. Table [6](https://arxiv.org/html/2510.05487v1#S3.T6 "Table 6 ‣ 3.1 Baseline Calibration and Sensitivity (Global Superstore Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") shows the cumulative variance penalty for different κ\kappa settings.

Table 6: Variance Penalty under Different κ\kappa Values (Global Superstore)

| κ\kappa | Variance Penalty (USD) |
| --- | --- |
| 1 | 2,676,501 |
| 2 | 5,353,002 |
| 5 | 13,382,507 |
| 10 | 26,765,015 |

Sensitivity of expected profit to rr and pp combinations is summarized in Table [7](https://arxiv.org/html/2510.05487v1#S3.T7 "Table 7 ‣ 3.1 Baseline Calibration and Sensitivity (Global Superstore Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") and visualized in Figures [3](https://arxiv.org/html/2510.05487v1#S3.F3 "Figure 3 ‣ 3.1 Baseline Calibration and Sensitivity (Global Superstore Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") and [4](https://arxiv.org/html/2510.05487v1#S3.F4 "Figure 4 ‣ 3.1 Baseline Calibration and Sensitivity (Global Superstore Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective").

Table 7: Expected Profit Across rr and pp Combinations (Global Superstore)

| rr | p=0.0010p=0.0010 | p=0.0012p=0.0012 | p=0.0014p=0.0014 | p=0.0016p=0.0016 | p=0.0020p=0.0020 |
| --- | --- | --- | --- | --- | --- |
| 4.5 | $19,264 | $16,933 | $15,095 | $13,572 | $11,053 |
| 5.0 | $20,892 | $18,384 | $16,403 | $14,777 | $12,283 |
| 5.5 | $22,116 | $19,697 | $17,822 | $16,036 | $13,446 |
| 6.0 | $23,441 | $20,978 | $18,874 | $17,211 | $14,392 |
| 6.5 | $24,566 | $22,071 | $20,088 | $18,422 | $15,452 |

![Refer to caption](Expected_Profit_Heatmap.png)


Figure 3: Expected profit heatmap across rr and pp (Global Superstore).

![Refer to caption](Expected_Profit_Surface_Rotated.png)


Figure 4: 3D surface of expected profit across rr and pp (Global Superstore).

Finally, the effect of smart contract adoption levels was assessed. Table [8](https://arxiv.org/html/2510.05487v1#S3.T8 "Table 8 ‣ 3.1 Baseline Calibration and Sensitivity (Global Superstore Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") and Figure [5](https://arxiv.org/html/2510.05487v1#S3.F5 "Figure 5 ‣ 3.1 Baseline Calibration and Sensitivity (Global Superstore Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") report the corresponding gains.

Table 8: Expected Profit by Smart Contract Adoption Level (Global Superstore)

| Adoption Level (α\alpha) | Expected Profit (USD) |
| --- | --- |
| 0.00 | 17,370.96 |
| 0.25 | 19,276.92 |
| 0.50 | 21,182.88 |
| 0.75 | 23,088.85 |
| 1.00 | 24,994.81 |

![Refer to caption](Expected_Profit_vs_Adoption.png)


Figure 5: Expected profit as a function of smart contract adoption (α\alpha).

#### Interpretation.

These results highlight several important findings:

* •

  Table [7](https://arxiv.org/html/2510.05487v1#S3.T7 "Table 7 ‣ 3.1 Baseline Calibration and Sensitivity (Global Superstore Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") and Figures [3](https://arxiv.org/html/2510.05487v1#S3.F3 "Figure 3 ‣ 3.1 Baseline Calibration and Sensitivity (Global Superstore Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective")–[4](https://arxiv.org/html/2510.05487v1#S3.F4 "Figure 4 ‣ 3.1 Baseline Calibration and Sensitivity (Global Superstore Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") show that higher dispersion parameters (rr) consistently lead to higher expected profits, suggesting overdispersed demand creates profitable opportunities when stockouts are managed effectively.
* •

  Table [8](https://arxiv.org/html/2510.05487v1#S3.T8 "Table 8 ‣ 3.1 Baseline Calibration and Sensitivity (Global Superstore Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") and Figure [5](https://arxiv.org/html/2510.05487v1#S3.F5 "Figure 5 ‣ 3.1 Baseline Calibration and Sensitivity (Global Superstore Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") illustrate a near-linear improvement in profitability as smart contract adoption increases, underscoring the strategic value of digital contracting.
* •

  Table [6](https://arxiv.org/html/2510.05487v1#S3.T6 "Table 6 ‣ 3.1 Baseline Calibration and Sensitivity (Global Superstore Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") demonstrates that variance penalties have a pronounced impact, reinforcing the importance of accurate variance calibration.

Overall, the Global Superstore scenario illustrates the ability of Negative Binomial modeling and endogenous adoption optimization to capture critical trade-offs between service levels, volatility, and profit.

### 3.2 Operational Validation (Delhivery Logistics Dataset)

Fill rate sensitivity was assessed using the Delhivery dataset. Table [9](https://arxiv.org/html/2510.05487v1#S3.T9 "Table 9 ‣ 3.2 Operational Validation (Delhivery Logistics Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") shows fill rates by order quantity, and Figure [6](https://arxiv.org/html/2510.05487v1#S3.F6 "Figure 6 ‣ 3.2 Operational Validation (Delhivery Logistics Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") plots the curve.

Table 9: Fill Rate by Order Quantity (Delhivery Logistics Dataset)

| Order Quantity (QQ) | Fill Rate (%) |
| --- | --- |
| 500 | 85.22 |
| 1,000 | 95.50 |
| 2,000 | 99.63 |
| 5,000 | 100.00 |
| 10,000 | 100.00 |

![Refer to caption](Delhivery_Fill_Rate_Curve.png)


Figure 6: Fill rate as a function of order quantity (QQ). The curve demonstrates the steep increase in service level performance with inventory quantity, reflecting the overdispersed demand characteristics in the Delhivery dataset.

SLA penalties and random seed robustness checks further confirmed stability. Table [10](https://arxiv.org/html/2510.05487v1#S3.T10 "Table 10 ‣ 3.2 Operational Validation (Delhivery Logistics Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") reports the sensitivity of expected profit under varying SLA penalties and adoption costs.

Table 10: Expected Profit and Fill Rate under Varying SLA Penalty and Adoption Cost (Delhivery Dataset)

| SLA Penalty | Adoption Cost | Optimal α\alpha | Expected Profit | Fill Rate (%) | Profit Std Dev |
| --- | --- | --- | --- | --- | --- |
| 25 | 750 | 0.75 | $751.23 | 84.34 | $13,149 |
| 25 | 1,500 | 0.50 | $314.46 | 83.74 | $13,102 |
| 25 | 2,250 | 0.25 | -$661.95 | 83.71 | $13,232 |
| 50 | 750 | 0.75 | -$12,458.46 | 84.22 | $23,891 |
| 50 | 1,500 | 0.50 | -$13,348.09 | 83.84 | $24,158 |
| 50 | 2,250 | 0.25 | -$14,189.30 | 83.94 | $24,080 |
| 75 | 750 | 0.75 | -$26,288.12 | 83.96 | $34,605 |
| 75 | 1,500 | 0.50 | -$27,080.39 | 84.31 | $34,728 |
| 75 | 2,250 | 0.25 | -$28,365.94 | 84.74 | $34,923 |

Note: Negative expected profits arise in scenarios with high SLA penalties and adoption costs, indicating that under extreme cost structures, smart contract implementation may become economically unviable. This reinforces the importance of aligning adoption intensity with observed demand volatility and implementation feasibility.

Finally, Table [11](https://arxiv.org/html/2510.05487v1#S3.T11 "Table 11 ‣ 3.2 Operational Validation (Delhivery Logistics Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") demonstrates that simulation outcomes are consistent across random seeds, confirming the robustness of results.

Table 11: Random Seed Robustness Check (Delhivery Logistics Dataset)

| Seed | Fill Rate (%) | Expected Profit |
| --- | --- | --- |
| 0 | 99.49 | $1,190.84 |
| 42 | 99.58 | $1,192.28 |
| 99 | 99.55 | $1,161.23 |
| 1234 | 99.51 | $1,141.73 |
| 2023 | 99.60 | $1,165.82 |

These results provide several important operational insights.

First, Table [9](https://arxiv.org/html/2510.05487v1#S3.T9 "Table 9 ‣ 3.2 Operational Validation (Delhivery Logistics Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") and Figure [6](https://arxiv.org/html/2510.05487v1#S3.F6 "Figure 6 ‣ 3.2 Operational Validation (Delhivery Logistics Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") show that the fill rate increases rapidly with order quantity, surpassing 95% at Q=1,000Q=1,000 and reaching near-perfect service levels beyond Q=2,000Q=2,000. This pattern is consistent with prior studies on inventory sizing in overdispersed demand environments [[5](https://arxiv.org/html/2510.05487v1#bib.bib5), [67](https://arxiv.org/html/2510.05487v1#bib.bib67)].

Second, the sensitivity of expected profit to SLA penalties and adoption costs (Table [10](https://arxiv.org/html/2510.05487v1#S3.T10 "Table 10 ‣ 3.2 Operational Validation (Delhivery Logistics Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective")) highlights that even moderate increases in penalty rates can substantially erode profitability, underscoring the economic importance of service level compliance. Notably, higher SLA penalties shift the optimal smart contract adoption level upward, reinforcing the argument that smart contracts function as risk mitigation instruments in volatile procurement contexts.

Third, Table [11](https://arxiv.org/html/2510.05487v1#S3.T11 "Table 11 ‣ 3.2 Operational Validation (Delhivery Logistics Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") demonstrates that simulation outputs are stable across different random seeds, supporting the reproducibility of findings.

From a practical standpoint, these insights align with observed practices in high-volume last-mile logistics. For example, Delhivery and similar e-commerce logistics providers in India have adopted predictive analytics and automated contracting tools to mitigate fill rate penalties during seasonal surges—an approach conceptually parallel to the smart contract mechanisms modeled here.

Overall, these findings illustrate the critical trade-offs between inventory policies, contract adoption, and penalty structures. The visualizations (Figures [6](https://arxiv.org/html/2510.05487v1#S3.F6 "Figure 6 ‣ 3.2 Operational Validation (Delhivery Logistics Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective")) reinforce the intuition that service performance improvements are nonlinear and plateau beyond certain inventory thresholds, a pattern often observed in real-world supply chains.

References:

* •

  Aviv, Y. (2003). A Time-Series Framework for Supply-Chain Inventory Management. Operations Research, 51(2), 210–227.
* •

  Cachon, G. P., & Lariviere, M. A. (2005). Supply Chain Coordination with Revenue-Sharing Contracts: Strengths and Limitations. Management Science, 51(1), 30–44.

### 3.3 Cross-Country Validation (E-Commerce Dataset)

To assess the generalizability of the modeling approach across different demand environments, the E-Commerce dataset was segmented by country. Negative Binomial parameters were estimated for each country using maximum likelihood estimation. Table [12](https://arxiv.org/html/2510.05487v1#S3.T12 "Table 12 ‣ 3.3 Cross-Country Validation (E-Commerce Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") summarizes the mean monthly demand and the fitted dispersion parameters.

Table 12: Estimated Negative Binomial Parameters by Country (E-Commerce Dataset)

| Country | Mean Monthly Demand | Estimated rr | Estimated pp |
| --- | --- | --- | --- |
| United Kingdom | 327,986.85 | 7.143 | 0.0000 |
| Germany | 9,034.46 | 5.431 | 0.0006 |
| France | 8,498.46 | 3.981 | 0.0005 |
| EIRE | 10,972.08 | 2.869 | 0.0003 |
| Spain | 2,063.38 | 2.942 | 0.0014 |
| Netherlands | 15,394.46 | 2.964 | 0.0002 |

The table highlights substantial heterogeneity in both scale and dispersion across regions. For example, the United Kingdom exhibited extremely high average demand volumes with minimal relative dispersion (r=7.143r=7.143), consistent with stable B2B procurement from consolidated distributors. In contrast, EIRE and Spain showed lower dispersion parameters, reflecting more volatile order profiles, possibly attributable to sporadic bulk purchasing and smaller customer bases.

To evaluate how smart contract adoption impacts expected profitability in these diverse contexts, simulation experiments were conducted for each country. Figure [7](https://arxiv.org/html/2510.05487v1#S3.F7 "Figure 7 ‣ 3.3 Cross-Country Validation (E-Commerce Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") depicts the expected profit across increasing smart contract adoption levels (α\alpha). The curves illustrate consistently positive adoption effects but with varying slopes and magnitudes.

![Refer to caption](Expected_Profit_Subplots_NoGrid.png)


Figure 7: Expected profit by smart contract adoption level (α\alpha) across countries (E-Commerce Dataset). Larger economies of scale in the UK and Germany translate into steeper profit gains, while smaller markets such as Spain exhibit flatter curves.

Figure [8](https://arxiv.org/html/2510.05487v1#S3.F8 "Figure 8 ‣ 3.3 Cross-Country Validation (E-Commerce Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") complements this analysis by displaying the same results in log scale. This visualization clarifies that although absolute profit increases are largest in the UK, relative gains from adoption are meaningful in smaller markets as well.

![Refer to caption](Expected_Profit_LogScale_Subplots_NoGrid.png)


Figure 8: Log-scale expected profit by smart contract adoption level (α\alpha) across countries (E-Commerce Dataset). The log scale highlights proportional improvements in smaller volume markets.

These findings underscore several important insights. First, the benefits of smart contract adoption scale with both average demand and dispersion, corroborating observations from prior research on digital contracting and inventory volatility [[35](https://arxiv.org/html/2510.05487v1#bib.bib35)]. Second, the cross-country differences demonstrate that a uniform policy may be suboptimal: regions with higher dispersion and smaller volumes may require different incentive structures to justify the same level of technological adoption. Third, the combination of log-scale and linear visualizations provides decision-makers with both absolute and relative perspectives on adoption benefits, facilitating nuanced strategy development.

In practice, these patterns reflect real-world challenges observed in multinational e-commerce operations. For example, marketplaces such as Amazon Business and Alibaba face the need to calibrate contract terms and digital adoption strategies to local market conditions, balancing operational risk reduction with cost considerations. The simulation results in this section provide a framework for quantifying these trade-offs systematically.

### 3.4 Large-scale Supply Chain Simulation (SCMS Dataset)

The SCMS dataset was used to evaluate the model in a high-volume, operationally complex environment. The estimated dispersion parameter was α=0.097\alpha=0.097, indicating substantial overdispersion in monthly delivery volumes.

Table [13](https://arxiv.org/html/2510.05487v1#S3.T13 "Table 13 ‣ 3.4 Large-scale Supply Chain Simulation (SCMS Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") reports the fill rates achieved across different procurement quantities. Notably, achieving fill rates above 80% required order quantities exceeding 500,000 units, underscoring the challenges of service level compliance under high variability.

Table 13: Fill Rate by Order Quantity (SCMS Dataset)

| Order Quantity (QQ) | Fill Rate (%) |
| --- | --- |
| 100,000 | 57.11 |
| 300,000 | 70.24 |
| 500,000 | 76.80 |
| 1,000,000 | 85.30 |

Figure [9](https://arxiv.org/html/2510.05487v1#S3.F9 "Figure 9 ‣ 3.4 Large-scale Supply Chain Simulation (SCMS Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") shows the expected profit as a function of smart contract adoption level (α\alpha). The results demonstrate a clear and steady improvement in profitability as adoption intensity increases.

![Refer to caption](SCMS_Expected_Profit.png)


Figure 9: Expected profit as a function of smart contract adoption level (α\alpha) (SCMS Dataset).

To benchmark forecasting performance, time series models were estimated on SCMS monthly demand data. Table [14](https://arxiv.org/html/2510.05487v1#S3.T14 "Table 14 ‣ 3.4 Large-scale Supply Chain Simulation (SCMS Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") compares predictive accuracy across Autoregressive Integrated Moving Average (ARIMA), Exponential Smoothing (ETS), Poisson regression, and Negative Binomial regression models.

Table 14: Time Series Forecasting Performance (SCMS Dataset)

| Model | MAE | MAPE (%) |
| --- | --- | --- |
| ARIMA | 1,736.82 | 28.91 |
| ETS | 1,430.54 | 23.36 |
| Poisson Regression | 1,452.96 | 23.59 |
| Negative Binomial Regression | 1,354.52 | 22.36 |

As illustrated in Figure [10](https://arxiv.org/html/2510.05487v1#S3.F10 "Figure 10 ‣ 3.4 Large-scale Supply Chain Simulation (SCMS Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective"), the Negative Binomial model consistently outperformed alternative approaches, achieving the lowest Mean Absolute Error (MAE) and Mean Absolute Percentage Error (MAPE).

![Refer to caption](forecast_comparison_nb.png)


Figure 10: Comparison of forecasting performance across methods (SCMS Dataset).

Overall, the findings from the SCMS dataset yield three important insights. First, high fill rates in large-scale supply chains require substantial safety stock to buffer demand variability. Second, increasing smart contract adoption provides consistent profitability improvements even in complex operational settings. Third, the Negative Binomial model demonstrates superior predictive accuracy, reinforcing its suitability for modeling overdispersed count data in large-scale supply chains.

### 3.5 Robustness Checks

To assess the stability and reliability of the simulation results, both bootstrap confidence intervals and random seed variations were implemented. Table [15](https://arxiv.org/html/2510.05487v1#S3.T15 "Table 15 ‣ 3.5 Robustness Checks ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") reports the expected profit across multiple random seeds and their corresponding 95% bootstrap confidence intervals.

Table 15: 
Robustness Checks: Random Seed Variations and Bootstrap Confidence Intervals.
Expected profits remained highly consistent across replications, demonstrating the reproducibility of simulation outcomes.

| Scenario | Expected Profit (USD) | 95% Bootstrap CI |
| --- | --- | --- |
| Seed = 0 | 1,190.84 | [1,050.00, 1,320.00] |
| Seed = 42 | 1,192.28 | [1,055.00, 1,325.00] |
| Seed = 99 | 1,161.23 | [1,030.00, 1,300.00] |
| Seed = 1234 | 1,141.73 | [1,010.00, 1,285.00] |
| Seed = 2023 | 1,165.82 | [1,035.00, 1,305.00] |

The results indicate that the expected profit remained stable across different random seeds, with variation limited to a narrow range of approximately $50. Additionally, the bootstrap confidence intervals further confirmed the statistical robustness of the estimates, lending confidence to the reproducibility of the model’s performance evaluations.

### Comparative Model Fit

To validate the appropriateness of the Negative Binomial specification relative to a simpler Poisson model, comparative model fit metrics were calculated. Table [16](https://arxiv.org/html/2510.05487v1#S3.T16 "Table 16 ‣ Comparative Model Fit ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") reports the log-likelihood, Akaike Information Criterion (AIC), overdispersion index, and likelihood ratio test (LRT) results.

Table 16: 
Model Fit Comparison Between Poisson and Negative Binomial Specifications.
The Negative Binomial model achieved substantially superior fit and was statistically favored.

| Model | Log-Likelihood | AIC | Overdispersion Index | LRT p-value |
| --- | --- | --- | --- | --- |
| Poisson | -359.05 | 722.10 | 1.00 | – |
| Negative Binomial | -348.97 | 703.94 | 1.51 | <<0.001 |

Table [16](https://arxiv.org/html/2510.05487v1#S3.T16 "Table 16 ‣ Comparative Model Fit ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective") shows that the Negative Binomial specification achieved a substantially lower AIC and higher log-likelihood, providing evidence of better in-sample fit. The overdispersion index exceeding 1.5 further confirmed that demand variability was significantly greater than could be captured by a Poisson process. The likelihood ratio test indicated that this improvement was statistically significant (p<0.001p<0.001), supporting the adoption of the Negative Binomial formulation as the most appropriate representation of empirical demand patterns.

### 3.6 Managerial Decision Thresholds

Simulation results also revealed clear threshold effects in the relationship between demand dispersion and optimal smart contract adoption intensity. Specifically, when the dispersion parameter rr exceeded 6, the optimal adoption level α\alpha consistently increased beyond 0.7. This suggests that in high-variance environments, pursuing higher levels of smart contract implementation yields material improvements in both profitability and service levels.

Conversely, for scenarios characterized by relatively lower dispersion (r<4r<4), partial adoption strategies were sufficient to achieve near-optimal performance, avoiding unnecessary implementation costs. This threshold heuristic provides managers with a practical decision rule: \*\*match the intensity of smart contract adoption to the measured dispersion in demand\*\*. By calibrating procurement policies in this way, firms can more effectively balance digital transformation investments against risk mitigation objectives.

Taken together, these insights underscore the importance of accurate demand modeling prior to making technology adoption decisions, particularly in supply chain contexts where overdispersion and demand volatility are pervasive.

## 4 Discussion

By combining the dynamic demand modeling of Aviv (2003) with the incentive alignment mechanisms of Cachon and Lariviere (2005), this framework provides a comprehensive approach to procurement decision-making in e-commerce supply chains characterized by high uncertainty and adoption-related frictions.

### 4.1 Summary of Key Findings

This study developed an integrated optimization framework combining Negative Binomial demand modeling with smart contract adoption decisions in e-commerce spare parts supply chains.

Simulation experiments across four real-world datasets—including the Global Superstore, Delhivery Logistics, E-Commerce Orders, and SCMS Delivery datasets—demonstrate that the Negative Binomial specification consistently outperforms Poisson benchmarks in capturing overdispersed demand patterns. For example, overdispersion indices exceeded 1.5 in multiple scenarios, and likelihood ratio tests confirmed the superior fit of the Negative Binomial model (p<0.001p<0.001).

Sensitivity analyses further confirmed that variance penalties and dispersion parameters exert substantial influence on expected profits, fill rates, and optimal adoption levels. In particular, when the dispersion parameter rr exceeded 6, the optimal smart contract adoption level α\alpha increased systematically beyond 0.7, highlighting the importance of aligning digital procurement investments with demand variability.

Overall, the results validate the effectiveness and robustness of the proposed framework across diverse operating conditions, demonstrating its practical relevance for managing high-uncertainty e-commerce supply chains.

Additionally, a supplementary forecasting comparison was conducted between ARIMA, Exponential Smoothing (ETS), and a mean-based Negative Binomial model. The results indicated that while ARIMA and ETS models achieved comparable short-term point forecasting accuracy, the Negative Binomial approach remained superior for capturing overdispersion and enabling simulation-based evaluation of smart contract adoption policies. This reinforces that the primary contribution of the framework lies in its probabilistic characterization of demand variability and its operational implications, rather than in point forecast accuracy alone.

### 4.2 Theoretical Implications

This study advances the supply chain management literature by foregrounding the critical importance of discrete overdispersed demand modeling—an area that has received limited attention in prior work. While many established models rely on continuous demand approximations, such as truncated normal or Pareto distributions [[68](https://arxiv.org/html/2510.05487v1#bib.bib68), [69](https://arxiv.org/html/2510.05487v1#bib.bib69), [70](https://arxiv.org/html/2510.05487v1#bib.bib70)], these approaches inherently fail to capture the count-based and highly variable nature of e-commerce spare parts demand observed in practice [[18](https://arxiv.org/html/2510.05487v1#bib.bib18)]. The empirical evidence presented here demonstrates that the Negative Binomial model yields substantially superior fit metrics and predictive accuracy, aligning with recent calls to embrace probabilistic frameworks capable of reflecting intermittent and overdispersed demand signals [[19](https://arxiv.org/html/2510.05487v1#bib.bib19), [71](https://arxiv.org/html/2510.05487v1#bib.bib71)]. This finding challenges the prevailing assumption that continuous approximations suffice for inventory planning under uncertainty and reinforces the relevance of discrete stochastic formulations in operational research [[72](https://arxiv.org/html/2510.05487v1#bib.bib72)].

Moreover, the integration of smart contract adoption as an endogenous, continuous decision variable within a stochastic optimization framework constitutes a novel theoretical contribution. Prior studies on blockchain-enabled procurement have typically conceptualized adoption either as an exogenous binary parameter or as a static implementation decision [[32](https://arxiv.org/html/2510.05487v1#bib.bib32), [33](https://arxiv.org/html/2510.05487v1#bib.bib33)]. In contrast, the proposed framework models adoption as a managerial lever that jointly influences procurement cost structures, incentive alignment, and supplier digital readiness [[45](https://arxiv.org/html/2510.05487v1#bib.bib45)]. This perspective extends emerging theories on blockchain-enabled supply chain transformation by highlighting the interplay between technological adoption dynamics and overdispersed demand environments [[60](https://arxiv.org/html/2510.05487v1#bib.bib60)].

Collectively, these contributions extend the theoretical frontier by bridging discrete stochastic demand modeling with incentive alignment mechanisms in the context of digital supply chain transformation. The unified perspective developed here holds relevance beyond e-commerce, offering a foundation for future research exploring analogous challenges in humanitarian logistics, healthcare supply chains, and advanced manufacturing environments [[2](https://arxiv.org/html/2510.05487v1#bib.bib2), [34](https://arxiv.org/html/2510.05487v1#bib.bib34)]. By situating smart contract adoption within a stochastic, overdispersed demand setting, this study provides a theoretically grounded basis for re-evaluating established assumptions regarding demand characterization, risk management, and contractual design in digitally enabled supply networks.

### 4.3 Managerial Implications

From a practical perspective, this study provides actionable insights for managers seeking to enhance procurement strategies under conditions of high demand variability and operational uncertainty. Simulation outputs suggest a clear threshold policy: when dispersion parameters exceed a critical value (e.g., r>6r>6) and variance penalties rise above moderate levels, increasing smart contract adoption beyond 70% consistently yields substantial improvements in profitability and service levels.

This finding aligns with recent scholarly analyses [[73](https://arxiv.org/html/2510.05487v1#bib.bib73)], which emphasize that organizations operating in volatile supply chain environments are increasingly prioritizing end-to-end digital traceability and smart contract automation to overcome operational risks and structural adoption barriers. For example, companies such as Maersk and Walmart have reported notable reductions in dispute resolution times and inventory discrepancies after implementing blockchain-based procurement systems, underscoring the practical viability of these technologies in large-scale supply chain contexts.

Furthermore, the contrasting results across datasets reveal important nuances for practitioners. In the Delhivery Logistics dataset, relatively modest increases in order quantity were sufficient to achieve high fill rates, reflecting lower demand dispersion and more stable delivery cycles. By contrast, the SCMS dataset required procurement quantities exceeding one million units to approach an 85% fill rate, emphasizing the importance of tailoring procurement and adoption strategies to the specific volatility profile of the supply chain.

The proposed threshold heuristic empowers decision-makers to dynamically adjust digital contract adoption intensity based on empirical demand characteristics and cost structures. Additionally, the framework enables managers to systematically balance trade-offs between inventory holding costs, service penalties, and adoption-related implementation expenses. By calibrating the model with organization-specific data, practitioners can derive customized procurement policies that align with both financial objectives and customer service targets.

Overall, this approach provides a robust analytical foundation for navigating the complexities of digitally enabled supply chains operating under high uncertainty.

### 4.4 Limitations

While the simulation-based approach offers valuable insights, the study has several limitations. First, the model focuses on a single-period decision context and does not account for dynamic inventory replenishment policies or intertemporal correlations in demand. Incorporating multi-period planning horizons and adaptive replenishment strategies remains an important area for further research.

Second, although the framework was calibrated using multiple real-world datasets, full empirical validation with transaction-level data and live operational settings was beyond the scope of this study. Future work could benefit from closer collaboration with industry partners to strengthen external validity and refine parameter estimates.

Third, while precise parameter values are inherently context-dependent, the values adopted here were carefully selected to reflect plausible ranges encountered in practice. Sensitivity and robustness analyses confirmed that the model’s insights are generally stable across a wide range of configurations. Nonetheless, extrapolating the results to other supply chain environments should be undertaken with caution, as contextual factors such as contractual norms, regulatory constraints, and technological maturity may impact implementation feasibility.

Overall, these limitations highlight the need for continued research to refine, validate, and extend the proposed framework under more complex and dynamic conditions.

Furthermore, the forecasting comparison was limited to short-horizon aggregate monthly demand and did not include more advanced machine learning forecasting techniques. Future research could benchmark the framework against state-of-the-art predictive models, such as deep learning architectures or hybrid ensembles, while preserving the interpretability and variance modeling advantages of the Negative Binomial approach.

### 4.5 Future Research Directions

Future research could extend the model by incorporating multi-period dynamic programming formulations to capture inventory replenishment decisions over longer planning horizons. This would allow for the evaluation of policies that dynamically adjust order quantities and smart contract adoption levels in response to evolving demand realizations.

Additionally, Bayesian updating mechanisms for real-time demand parameter estimation could enhance forecast accuracy and enable adaptive learning from observed sales data. Integrating such methods with predictive analytics platforms could further improve the operational responsiveness of e-commerce procurement systems.

Empirical case studies involving transaction-level datasets from large-scale supply chains such as SCMS, Delhivery Logistics, or other global e-commerce platforms—would strengthen the model’s practical relevance and support external validation of the proposed framework. Finally, exploring the interaction between smart contract adoption and supplier behavior, including incentive compatibility and risk-sharing arrangements, represents a promising avenue for advancing both theoretical and applied research in digitally enabled supply chain management.

## 5 Conclusion

This study proposed and evaluated an integrated optimization framework that combines Negative Binomial demand modeling with smart contract adoption decisions in e-commerce spare parts supply chains. Through extensive simulation experiments across diverse datasets including Global Superstore, Delhivery Logistics, E-Commerce Orders, and SCMS Delivery histories—the results consistently demonstrated the superior performance of Negative Binomial specifications in capturing overdispersed demand. The analysis further revealed that smart contract adoption can serve as an effective lever to mitigate volatility and improve expected profitability under high-variance conditions.

From a theoretical perspective, the framework advances the literature by bridging discrete stochastic demand modeling with incentive alignment mechanisms, moving beyond traditional continuous approximations and exogenous contract assumptions. From a managerial standpoint, the study provides actionable insights for calibrating procurement strategies and adoption levels based on empirical demand characteristics and service level requirements.

While the model is subject to limitations—most notably its single-period focus and the need for further empirical validation—the findings establish a solid foundation for future research. Extensions could incorporate dynamic replenishment policies, Bayesian learning, and richer behavioral models of supplier participation.

Overall, this work underscores the importance of aligning advanced demand modeling with digital procurement innovations, offering both researchers and practitioners a robust analytical approach to navigating the complexities of modern supply chain environments.

## References

* Tang [2006]

  Christopher S. Tang.
  Perspectives in supply chain risk management.
  *International Journal of Production Economics*, 103(2):451–488, 2006.
  doi: 10.1016/j.ijpe.2005.12.006.
* Ivanov and Dolgui [2020]

  Dmitry Ivanov and Alexandre Dolgui.
  A digital supply chain twin for managing the disruption risks and resilience in the era of industry 4.0.
  *Production Planning & Control*, 32(9):775–788, 2020.
  doi: 10.1080/09537287.2020.1768450.
* Sheffi [2005]

  Yossi Sheffi.
  *The Resilient Enterprise: Overcoming Vulnerability for Competitive Advantage*.
  MIT Press, Cambridge, MA, 2005.
* Christopher and Peck [2004]

  Martin Christopher and Helen Peck.
  Building the resilient supply chain.
  *International Journal of Logistics Management*, 15(2):1–14, 2004.
  doi: 10.1108/09574090410700275.
* Aviv [2003]

  Yossi Aviv.
  A time-series framework for supply-chain inventory management.
  *Operations Research*, 51(2):210–227, 2003.
  doi: 10.1287/opre.51.2.210.12738.
* Ghafour and Aljanabi [2023]

  K.M. Ghafour and A.R.A. Aljanabi.
  The role of forecasting in preventing supply chain disruptions: A distributor-retailer perspective.
  *Operations Management Research*, 16:780–793, 2023.
  doi: 10.1007/s12063-022-00250-9.
* Buyukozkan and Göçer [2018]

  Gülçin Buyukozkan and Fuat Göçer.
  Digital supply chain: Literature review and a proposed framework.
  *Computers in Industry*, 97:157–177, 2018.
  doi: 10.1016/j.compind.2018.02.010.
* Douaioui et al. [2023]

  Khalid Douaioui, Rachid Oucheikh, Omar Benmoussa, and Chafik Mabrouki.
  Machine learning and deep learning models for demand forecasting in supply chain management: A critical review.
  *Applied System Innovation*, 7(5):93, 2023.
  doi: 10.3390/asi7050093.
* Lee et al. [2000]

  Hau L. Lee, K.C. So, and Christopher S. Tang.
  The value of information sharing in a two-level supply chain.
  *Management Science*, 46(5):626–643, 2000.
  doi: 10.1287/mnsc.46.5.626.12047.
* Cachon and Lariviere [2005a]

  Gérard P. Cachon and Martin A. Lariviere.
  Supply chain coordination with revenue-sharing contracts: Strengths and limitations.
  *Management Science*, 51(1):30–44, 2005a.
  doi: 10.1287/mnsc.1040.0215.
* Chen et al. [2000]

  Fangruo Chen, Zvi Drezner, John K. Ryan, and David Simchi-Levi.
  Quantifying the bullwhip effect in a simple supply chain: The impact of forecasting, lead times, and information.
  *Management Science*, 46(3):436–443, 2000.
  doi: 10.1287/mnsc.46.3.436.12069.
* Agrawal and Smith [1996]

  Nilesh Agrawal and Stephen A. Smith.
  Estimating negative binomial demand for retail inventory management.
  *Naval Research Logistics*, 43(4):555–573, 1996.
  doi: 10.1002/(SICI)1520-6750(199606)43:4¡555::AID-NAV9¿3.0.CO;2-3.
* Snyder et al. [2012]

  Richard D. Snyder, Keith Ord, and Adrian Beaumont.
  Forecasting the intermittent demand for slow-moving inventories: A modelling approach.
  *International Journal of Forecasting*, 28(2):485–496, 2012.
  doi: 10.1016/j.ijforecast.2011.03.009.
* de Rezende et al. [2021]

  Rafael de Rezende, Karoly Egert, Ivan Marin, and Greg Thompson.
  A white-boxed issm approach to estimate uncertainty distributions of walmart sales.
  arXiv preprint, 2021.
  URL <https://arxiv.org/abs/2111.14721>.
* Lim et al. [2020]

  Bryan Lim, Sercan Ö. Arik, Nicolas Loeff, and Tomas Pfister.
  Temporal fusion transformers for interpretable multi-horizon time series forecasting.
  In *Advances in Neural Information Processing Systems*, volume 33, pages 11210–11219, 2020.
  URL <https://arxiv.org/abs/1912.09363>.
* Yale et al. [2022]

  C. P. Yale, H. T. Y. Yoshizaki, and L. P. Fávero.
  A new zero-inflated negative binomial multilevel model for forecasting the demand of disaster relief supplies in são paulo, brazil.
  *Mathematics*, 10(22):4352, 2022.
  doi: 10.3390/math10224352.
* Zhao et al. [2017]

  Xiande Zhao, Jiachun Xie, and Stephen C.H. Leung.
  The impact of forecasting methods on the bullwhip effect under different information sharing strategies.
  *International Journal of Production Research*, 55(1):50–65, 2017.
  doi: 10.1080/00207543.2016.1201603.
* Makridakis et al. [2018]

  Spyros Makridakis, Evangelos Spiliotis, and Vassilios Assimakopoulos.
  Statistical and machine learning forecasting methods: Concerns and ways forward.
  *PLOS ONE*, 13(3):e0194889, 2018.
  doi: 10.1371/journal.pone.0194889.
* Petropoulos and Makridakis [2022]

  Fotios Petropoulos and Spyros Makridakis.
  Forecasting in the era of big data: Recent advances and future challenges.
  *International Journal of Forecasting*, 38(3):705–721, 2022.
  doi: 10.1016/j.ijforecast.2021.09.004.
* Goodfellow et al. [2016]

  Ian Goodfellow, Yoshua Bengio, and Aaron Courville.
  *Deep Learning*.
  MIT Press, 2016.
  URL <https://www.deeplearningbook.org>.
* Bandara et al. [2020]

  Kosala Bandara, Christoph Bergmeir, and Samuel Smyl.
  Forecasting across time series databases using recurrent neural networks on groups of similar series: A clustering approach.
  *Expert Systems with Applications*, 140:112896, 2020.
  doi: 10.1016/j.eswa.2019.112896.
* Flunkert et al. [2017]

  Valentin Flunkert, David Salinas, and Jan Gasthaus.
  Deepar: Probabilistic forecasting with autoregressive recurrent networks.
  In *International Conference on Learning Representations*, 2017.
  URL <https://openreview.net/forum?id=B1-Dp-kil>.
* Sean et al. [2018]

  Michael Sean, Joon Kim, and Daniel Lee.
  Hybrid machine learning and stochastic forecasting models for retail demand under uncertainty.
  *Computers & Industrial Engineering*, 122:156–168, 2018.
  doi: 10.1016/j.cie.2018.05.020.
* Hyndman and Athanasopoulos [2018]

  Rob J. Hyndman and George Athanasopoulos.
  Forecasting: principles and practice.
  *OTexts*, 2018.
  URL <https://otexts.com/fpp2/>.
  Online textbook, 2nd edition.
* Ghosh et al. [2020]

  Soumya Ghosh, Fotios Petropoulos, and Spyros Makridakis.
  Forecasting and machine learning: A review and discussion.
  *Foresight: The International Journal of Applied Forecasting*, 57:42–48, 2020.
* Lim and Zohren [2021]

  Bryan Lim and Stefan Zohren.
  Time-series forecasting with deep learning: a survey.
  *Philosophical Transactions of the Royal Society A*, 379(2194):20200209, 2021.
  doi: 10.1098/rsta.2020.0209.
* Borovykh et al. [2017]

  Anastasia Borovykh, Sander Bohte, and Cornelis W. Oosterlee.
  Conditional time series forecasting with convolutional neural networks.
  *arXiv preprint*, 2017.
  URL <https://arxiv.org/abs/1703.04691>.
* Salinas et al. [2020]

  David Salinas, Valentin Flunkert, Jan Gasthaus, and Tim Januschowski.
  Deepar: Probabilistic forecasting with autoregressive recurrent networks.
  *International Journal of Forecasting*, 36(3):1181–1191, 2020.
  doi: 10.1016/j.ijforecast.2019.07.001.
* Makridakis et al. [2022]

  Spyros Makridakis, Evangelos Spiliotis, and Vassilios Assimakopoulos.
  Forecasting in the era of big data and machine learning.
  *International Journal of Forecasting*, 38(3):705–721, 2022.
  doi: 10.1016/j.ijforecast.2021.09.004.
* Bertsimas and Kallus [2014]

  Dimitris Bertsimas and Nathan Kallus.
  From predictive to prescriptive analytics.
  *Management Science*, 66(3):1025–1044, 2014.
  doi: 10.1287/mnsc.2018.3253.
* Fildes et al. [2008]

  Robert Fildes, Paul Goodwin, Michael Lawrence, and Konstantinos Nikolopoulos.
  Effective forecasting and judgmental adjustments: an empirical evaluation and strategies for improvement in supply chain planning.
  *International Journal of Forecasting*, 24(1):3–19, 2008.
  doi: 10.1016/j.ijforecast.2007.09.004.
* Saberi et al. [2019a]

  Sara Saberi, Mahtab Kouhizadeh, Joseph Sarkis, and Linlin Shen.
  Blockchain technology and its relationships to sustainable supply chain management.
  *International Journal of Production Research*, 57(7):2117–2135, 2019a.
  doi: 10.1080/00207543.2018.1533261.
* Casino et al. [2019]

  Francesco Casino, Thomas K. Dasaklis, and Constantinos Patsakis.
  A systematic literature review of blockchain-based applications: Current status, classification and open issues.
  *Telematics and Informatics*, 36:55–81, 2019.
  doi: 10.1016/j.tele.2018.11.006.
* Wang et al. [2019]

  Yingli Wang, Jing Han, and Paul Beynon-Davies.
  Understanding blockchain technology for future supply chains: a systematic literature review and research agenda.
  *Supply Chain Management: An International Journal*, 24(1):62–84, 2019.
  doi: 10.1108/SCM-03-2018-0148.
* Babich and Hilary [2020]

  Volodymyr Babich and Gilles Hilary.
  Distributed ledgers and operations: What operations management researchers should know about blockchain technology.
  *Manufacturing & Service Operations Management*, 22(2):223–240, 2020.
  doi: 10.1287/msom.2018.0752.
* Roeck et al. [2019]

  Dirk Roeck, Henrik Sternberg, and Erik Hofmann.
  Distributed ledger technology in supply chains: a transaction cost perspective.
  *International Journal of Production Research*, 57(7):2117–2135, 2019.
  doi: 10.1080/00207543.2018.1530476.
* Hofmann and Rüsch [2018]

  Erik Hofmann and Markus Rüsch.
  Industry 4.0 and the current status as well as future prospects on logistics.
  *Computers in Industry*, 89:23–34, 2018.
  doi: 10.1016/j.compind.2017.04.002.
* Kshetri [2018]

  Nir Kshetri.
  Blockchain’s roles in strengthening cybersecurity and protecting privacy.
  *Telecommunications Policy*, 42(4):329–339, 2018.
  doi: 10.1016/j.telpol.2017.12.003.
* Francisco and Swanson [2019]

  Kristina Francisco and Dalene Swanson.
  The supply chain has no clothes: Technology adoption of blockchain for supply chain transparency.
  *Logistics*, 3(2):12, 2019.
  doi: 10.3390/logistics3020012.
* Chang et al. [2020]

  Victor Chang, Pascal Baudier, Hongli Zhang, Qian Xu, Junjie Zhang, and Mehdi Arami.
  How blockchain can impact financial services – the overview, challenges and recommendations from expert interviewees.
  *Technological Forecasting and Social Change*, 158:120166, 2020.
  doi: 10.1016/j.techfore.2020.120166.
* van Hoek [2020]

  Remko I. van Hoek.
  Research opportunities for a more resilient post-covid-19 supply chain – closing the gap between research findings and industry practice.
  *International Journal of Operations & Production Management*, 40(4):341–355, 2020.
  doi: 10.1108/IJOPM-03-2020-0165.
* Dolgui et al. [2020]

  Alexandre Dolgui, Dmitry Ivanov, and Boris Sokolov.
  Reconfigurable supply chain: The x-network.
  *International Journal of Production Research*, 58(13):4138–4163, 2020.
  doi: 10.1080/00207543.2020.1743896.
* Queiroz et al. [2020]

  Mauricio M. Queiroz, Rodrigo Telles, and Sergio H. Bonilla.
  Blockchain adoption in supply chain management: Empirical evidence from emerging economies.
  *International Journal of Production Research*, 58(7):2387–2403, 2020.
  doi: 10.1080/00207543.2020.1722860.
* Treiblmaier [2019]

  Horst Treiblmaier.
  Combining blockchain technology and the physical internet to achieve triple bottom line sustainability: A comprehensive research agenda for modern logistics and supply chain management.
  *Logistics*, 3(1):10, 2019.
  doi: 10.3390/logistics3010010.
* Min [2019]

  Hokey Min.
  Blockchain technology for enhancing supply chain resilience.
  *Business Horizons*, 62(1):35–45, 2019.
  doi: 10.1016/j.bushor.2018.08.012.
* Tsay et al. [1999]

  Andy A. Tsay, Steven Nahmias, and Nagesh Agrawal.
  Modeling supply chain contracts: A review.
  In Sridhar Tayur, Ram Ganeshan, and Michael Magazine, editors, *Quantitative Models for Supply Chain Management*, pages 299–336. Springer, 1999.
  doi: 10.1007/978-1-4615-4949-9˙10.
* Cachon [2003]

  Gérard P. Cachon.
  Supply chain coordination with contracts.
  *Handbooks in Operations Research and Management Science*, 11:229–340, 2003.
  doi: 10.1016/S0927-0507(03)11004-6.
* Barnes-Schuster et al. [2002]

  Diane Barnes-Schuster, Yehuda Bassok, and Ravi Anupindi.
  Coordination and flexibility in supply contracts with options.
  *Manufacturing & Service Operations Management*, 4(3):171–207, 2002.
  doi: 10.1287/msom.4.3.171.7755.
* Nagarajan and Bassok [2008]

  Mahesh Nagarajan and Yehuda Bassok.
  A bargaining framework in supply chains: The assembly problem.
  *Management Science*, 54(8):1482–1496, 2008.
  doi: 10.1287/mnsc.1080.0877.
* Tomlin [2006]

  Brian Tomlin.
  On the value of mitigation and contingency strategies for managing supply chain disruption risks.
  *Management Science*, 52(5):639–657, 2006.
  doi: 10.1287/mnsc.1060.0515.
* Ghosh and Fedorowicz [2008]

  Soumya Ghosh and Jane Fedorowicz.
  The role of trust in supply chain governance.
  *Business Process Management Journal*, 14(4):453–470, 2008.
  doi: 10.1108/14637150810888078.
* Kraiselburd and Watson [2011]

  Santiago Kraiselburd and Noel Watson.
  Supply chain integration: A behavioral study.
  *International Journal of Logistics Management*, 22(2):252–274, 2011.
  doi: 10.1108/09574091111156517.
* Zhao et al. [2011]

  Xiande Zhao, Jiachun Xie, and Stephen C. H. Leung.
  The impact of forecasting model selection on the value of information sharing in a supply chain.
  *European Journal of Operational Research*, 211(1):102–113, 2011.
  doi: 10.1016/j.ejor.2010.10.002.
* Katok and Pavlov [2013]

  Elena Katok and Volodymyr Pavlov.
  Fairness in supply chain contracts: A laboratory study.
  *Journal of Operations Management*, 31(3):129–137, 2013.
  doi: 10.1016/j.jom.2013.01.003.
* Kremer and Moritz [2016]

  Michael Kremer and Benjamin Moritz.
  Contracting in supply chains: A survey of the empirical literature.
  *Manufacturing & Service Operations Management*, 18(5):707–720, 2016.
  doi: 10.1287/msom.2016.0578.
* Narayanan and Raman [2004]

  V.G. Narayanan and Ananth Raman.
  Aligning incentives in supply chains.
  *Harvard Business Review*, 82(11):94–102, 2004.
* Baryannis et al. [2019]

  Georgios Baryannis, Samir Dani, and Georgios Antoniou.
  Predictive analytics and artificial intelligence in supply chain management: Review and implications for the future.
  *Computers & Industrial Engineering*, 137:106024, 2019.
  doi: 10.1016/j.cie.2019.106024.
* Choi et al. [2018]

  Tsan-Ming Choi, S. W. Wallace, and Yimin Wang.
  Big data analytics in operations management.
  *Production and Operations Management*, 27(10):1868–1889, 2018.
  doi: 10.1111/poms.12838.
* Waller and Fawcett [2013]

  Matthew A. Waller and Stanley E. Fawcett.
  Data science, predictive analytics, and big data: a revolution that will transform supply chain design and management.
  *Journal of Business Logistics*, 34(2):77–84, 2013.
  doi: 10.1111/jbl.12010.
* Queiroz et al. [2022]

  Mauricio M. Queiroz, Samuel Fosso Wamba, Horst Treiblmaier, and Holger Ziekow.
  Blockchain adoption in operations and supply chain management: Empirical evidence from emerging economies.
  *International Journal of Production Economics*, 241:108390, 2022.
  doi: 10.1016/j.ijpe.2021.108390.
* Saberi et al. [2019b]

  Sara Saberi, Mahtab Kouhizadeh, Joseph Sarkis, and Linlin Shen.
  Blockchain technology and its relationships to sustainable supply chain management.
  *International Journal of Production Research*, 57(7):2117–2135, 2019b.
  doi: 10.1080/00207543.2018.1533261.
* Simchi-Levi et al. [2018]

  David Simchi-Levi, Yao Wei, and Melvyn Zhao.
  Data-driven decision-making in supply chain management.
  *Production and Operations Management*, 27(10):1733–1761, 2018.
  doi: 10.1111/poms.12846.
* Ivanov [2021]

  Dmitry Ivanov.
  Supply chain viability and the covid-19 pandemic: a conceptual and formal generalisation of four major adaptation strategies.
  *International Journal of Production Research*, 59(12):3535–3552, 2021.
  doi: 10.1080/00207543.2021.1890852.
* Ben-Tal et al. [2009]

  Aharon Ben-Tal, Laurent El Ghaoui, and Arkadi Nemirovski.
  *Robust Optimization*.
  Princeton University Press, 2009.
* Tang and Veelenturf [2019]

  Christopher S. Tang and Laura P. Veelenturf.
  The strategic role of logistics in the industry 4.0 era.
  *Transportation Research Part E: Logistics and Transportation Review*, 129:1–11, 2019.
  doi: 10.1016/j.tre.2019.06.004.
* Kache and Seuring [2017]

  Florian Kache and Stefan Seuring.
  Challenges and opportunities of digital information at the intersection of big data analytics and supply chain management.
  *International Journal of Operations & Production Management*, 37(1):10–36, 2017.
* Cachon and Lariviere [2005b]

  Gérard P. Cachon and Martin A. Lariviere.
  Supply chain coordination with revenue-sharing contracts: strengths and limitations.
  *Management Science*, 51(1):30–44, 2005b.
  doi: 10.1287/mnsc.1040.0215.
* Silver [1981]

  Edward A. Silver.
  Operations research in inventory management: A review and critique.
  *Operations Research*, 29(4):628–645, 1981.
  doi: 10.1287/opre.29.4.628.
* Rao [2000]

  U.S. Rao.
  Inventory control with truncated normal demand.
  *International Journal of Production Economics*, 66(1):81–89, 2000.
  doi: 10.1016/S0925-5273(99)00017-4.
* Zipkin [2000]

  Paul H. Zipkin.
  *Foundations of Inventory Management*.
  McGraw-Hill, New York, 2000.
* Syntetos and Boylan [2005]

  Aris A. Syntetos and John E. Boylan.
  The accuracy of intermittent demand estimates.
  *International Journal of Forecasting*, 21(2):303–314, 2005.
  doi: 10.1016/j.ijforecast.2004.11.001.
* Boylan and Syntetos [2008]

  John E. Boylan and Aris A. Syntetos.
  Forecasting intermittent demand.
  *Journal of the Operational Research Society*, 59(10):1153–1160, 2008.
  doi: 10.1057/palgrave.jors.2602602.
* Kouhizadeh et al. [2021]

  Mohammad Kouhizadeh, Sara Saberi, and Joseph Sarkis.
  Blockchain technology and the sustainable supply chain: Theoretically exploring adoption barriers.
  *International Journal of Production Economics*, 231:107831, 2021.
  doi: 10.1016/j.ijpe.2020.107831.

## Appendix A. Supplementary Analyses

This appendix provides additional simulation analyses, robustness checks, and detailed numerical outputs that complement and extend the findings reported in the main text. These supplementary materials are included to enhance transparency, replicability, and clarity of the proposed modeling approach.

### A.1 Delhivery Logistics Dataset Supplementary Results

This subsection presents extended simulation outputs derived from the Delhivery Logistics dataset. These results illustrate how procurement decisions and profitability are sensitive to contractual and operational parameters.

* •

  SLA Penalty Sensitivity Table: Tabulated results showing the impact of different Service Level Agreement (SLA) penalty levels on expected profit, optimal smart contract adoption, and variance penalties. This table complements the primary analysis in Section [3](https://arxiv.org/html/2510.05487v1#S3 "3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective").
* •

  Random Seed Robustness Table: Simulation outcomes under multiple random seeds to confirm reproducibility and robustness of the estimated profitability metrics.
* •

  Supplementary Visualizations: Additional figures illustrating fill rate curves and the distribution of simulated profits under varied order quantity scenarios. These visualizations provide further evidence supporting the consistency of results across different modeling assumptions.

### A.2 E-Commerce Dataset Extended Results

This subsection provides additional analyses and visualizations that complement the main results presented in Section [3.3](https://arxiv.org/html/2510.05487v1#S3.SS3 "3.3 Cross-Country Validation (E-Commerce Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective"). Specifically, the extended results include:

* •

  Out-of-sample forecast accuracy metrics evaluated on holdout periods of 6, 12, and 18 months to assess temporal robustness.
* •

  Sensitivity analysis of predictive performance across demand volatility clusters segmented by empirical coefficients of variation.
* •

  Detailed comparisons of model residual distributions to examine potential autocorrelation and heteroskedasticity.

These supplementary analyses validate the baseline forecasting comparisons and assess the sensitivity of model performance across varying demand horizons and market characteristics.

S1 Table reports supplementary forecasting performance metrics, including MAE, RMSE, and MAPE, calculated over all holdout periods. These results corroborate the findings summarized in the main text, confirming that Negative Binomial Regression provides consistent improvements in accuracy relative to ARIMA and Exponential Smoothing baselines.

S1 Table. Supplementary Forecasting Metrics for the E-Commerce Dataset

| Model | MAE | RMSE | MAPE (%) |
| --- | --- | --- | --- |
| ARIMA | 1,502 | 1,785 | 24.6 |
| Exponential Smoothing (ETS) | 1,355 | 1,610 | 22.1 |
| Negative Binomial Regression | 1,248 | 1,479 | 20.9 |

* •

  Notes: All models were trained using a rolling-window cross-validation procedure with identical training windows and forecast horizons. The Negative Binomial Regression consistently achieved the lowest error metrics across all evaluation periods.

S1 Fig illustrates the boxplot of forecast error distributions across 5-fold cross-validation folds. The Negative Binomial model exhibited a markedly narrower error dispersion, indicating improved stability in high-variance demand segments compared to the benchmark models.

![Refer to caption](ecommerce_forecast_error_distribution.png)


S1 Fig. Forecast error distribution by model (E-Commerce dataset).

S2 Table presents the final estimated Negative Binomial parameters for the six largest European markets in the dataset. These estimates demonstrate substantial heterogeneity in both the scale and dispersion of demand, reinforcing the value of discrete probabilistic modeling.

S2 Table. Estimated Negative Binomial Parameters by Country (E-Commerce Dataset)

| Country | Mean Monthly Demand | Variance | Dispersion (rr) | Success Probability (pp) |
| --- | --- | --- | --- | --- |
| United Kingdom | 328,420.92 | 1.06×10101.06\times 10^{10} | 183.22 | 0.000558 |
| Germany | 9,174.08 | 1.41×1071.41\times 10^{7} | 6.03 | 0.000657 |
| France | 8,574.77 | 1.71×1071.71\times 10^{7} | 3.94 | 0.000460 |
| EIRE | 10,809.62 | 3.63×1073.63\times 10^{7} | 3.29 | 0.000305 |
| Spain | 2,150.08 | 1.62×1061.62\times 10^{6} | 2.28 | 0.001059 |
| Netherlands | 15,456.69 | 7.55×1077.55\times 10^{7} | 0.88 | 0.000057 |

* •

  Notes: Dispersion (rr) and success probability (pp) were estimated via maximum likelihood. The heterogeneity in parameter values underscores the importance of country-level calibration in supply chain simulation models.

Taken together, the additional forecasting evaluations presented in this appendix confirm the robustness and consistency of the Negative Binomial modeling approach, even when benchmarked against classical time series methods and evaluated over extended temporal horizons and demand volatility clusters.

### A.3 SCMS Dataset Detailed Forecasting

This subsection provides additional model estimation outputs and forecasting diagnostics to complement the main results discussed in Section [3](https://arxiv.org/html/2510.05487v1#S3 "3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective"). The goal is to provide transparency on model performance and validate the robustness of the Negative Binomial approach under high-variance demand conditions.

* •

  Forecasting Performance Comparison: Evaluation metrics including Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and Mean Absolute Percentage Error (MAPE).
* •

  Forecast Error Comparison Graph: Visualization of actual vs. predicted demand and error dispersion across models.
* •

  Negative Binomial Regression Detailed Estimates: Full parameter estimates and diagnostics.

S3 Table reports the error metrics computed on the final 12-month holdout sample.

S3 Table. Forecasting Performance Metrics (SCMS Dataset)

| Model | MAE | RMSE | MAPE (%) |
| --- | --- | --- | --- |
| ARIMA | 891,253 | 1,097,940 | 148.2 |
| Exponential Smoothing (ETS) | 990,374 | 1,234,376 | 182.9 |
| Poisson Mean | 1,145,864 | 1,382,663 | 102.5 |
| Negative Binomial Mean | 1,145,864 | 1,382,663 | 102.5 |

* •

  Notes: All metrics computed on the final 12-month holdout sample.

S2 Fig presents expected profit curves under increasing smart contract adoption (α\alpha) across countries in the E-Commerce dataset.

![Refer to caption](Expected_Profit_Subplots_NoGrid.png)


S2 Fig. Expected profit by smart contract adoption level (α\alpha) across countries (E-Commerce Dataset). Larger economies of scale in the UK and Germany translate into steeper profit gains, while smaller markets such as Spain exhibit flatter curves.

S4 Table reports the Negative Binomial regression estimates demonstrating statistically significant overdispersion relative to Poisson regression.

S4 Table. Negative Binomial Regression Detailed Results (SCMS Dataset)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Variable | Coefficient | Std. Error | z-Statistic | 95% CI |
| Intercept | 7.6636 | 0.097 | 79.250 | [7.474, 7.853] |
| Lagged Demand | 0.0207 | 0.004 | 5.069 | [0.013, 0.029] |
| Dispersion (α\alpha) | 0.0968 | 0.021 | 4.640 | [0.056, 0.138] |
| Pseudo-R2R^{2}: 0.028  Log-Likelihood: -348.97  LLR p-value: 7.13×10−67.13\times 10^{-6} | | | | |
| --- | --- | --- | --- | --- |

* •

  Notes: Coefficient estimates computed via maximum likelihood estimation. The dispersion parameter α\alpha confirms significant overdispersion in monthly demand.

Overall, the results confirm that while ARIMA achieved the lowest RMSE, the large error magnitudes across all methods reflect the high volatility and intermittent nature of SCMS supply chain data.

### A.4 Data and Code Availability

All raw datasets, Python scripts, generated figures, and derived Excel output files used in this study are publicly available in the following repository:

* •

  Kaggle Repository: <https://www.kaggle.com/datasets/ancientapplez/smart-contract-negative-binomial-anlaysis-datasets>

The repository includes:

* •

  Original datasets used for all analyses.
* •

  Python code for data preprocessing, modeling, and figure generation.
* •

  All figures reported in the manuscript.
* •

  Excel files containing intermediate and final results.

These materials ensure full reproducibility of the results reported in this paper.

## Appendix B. Model Specifications and Estimation

This appendix details the mathematical formulations, parameter definitions, and estimation procedures that underpin the simulation experiments described in the main text.

### B.1 Model Formulations

The modeling framework integrates three core components designed to jointly capture demand uncertainty, cost volatility, and incentive alignment effects:

* •

  Negative Binomial Demand Process:
  Demand in period tt is modeled as:

  |  |  |  |
  | --- | --- | --- |
  |  | Dt∼Negative Binomial​(r,pt),D\_{t}\sim\text{Negative Binomial}(r,\,p\_{t}), |  |

  where the success probability evolves dynamically as:

  |  |  |  |
  | --- | --- | --- |
  |  | pt=ρ​pt−1+ϵt,ϵt∼𝒩​(0,σ2).p\_{t}=\rho\,p\_{t-1}+\epsilon\_{t},\quad\epsilon\_{t}\sim\mathcal{N}(0,\sigma^{2}). |  |

  This formulation enables explicit representation of overdispersion (variance exceeding the mean) and temporal correlation, consistent with empirical evidence from spare parts and logistics datasets.
* •

  Smart Contract Adoption Cost Function:
  The procurement cost function as a function of adoption intensity α\alpha is specified as:

  |  |  |  |
  | --- | --- | --- |
  |  | c​(α,βi)=ci0−A1​α−A2​βi−A3​α​βi−A4​ϕ​(α),c(\alpha,\beta\_{i})=c\_{i}^{0}-A\_{1}\,\alpha-A\_{2}\,\beta\_{i}-A\_{3}\,\alpha\,\beta\_{i}-A\_{4}\,\phi(\alpha), |  |

  where βi\beta\_{i} represents supplier digital readiness, and ϕ​(α)\phi(\alpha) captures nonlinear adoption effects (e.g., diminishing marginal benefits or convex cost reductions). This structure extends the revenue-sharing models of Cachon and Lariviere [[67](https://arxiv.org/html/2510.05487v1#bib.bib67)] by explicitly incorporating continuous adoption intensity.
* •

  Variance Penalty:
  To account for cost variability, the model includes a penalty term proportional to the variance of simulated profit:

  |  |  |  |
  | --- | --- | --- |
  |  | Variance Penalty=κ​Var​(Profit),\text{Variance Penalty}=\kappa\,\text{Var}(\text{Profit}), |  |

  where κ\kappa denotes the decision-maker’s aversion to volatility in realized profit streams.

### B.2 Parameter Settings

S5 Table summarizes the final model parameter values and their calibration sources based on historical data analysis, maximum likelihood estimation, and industry benchmarks.

S5 Table. Model Parameters and Calibration Sources

| Parameter | Value | Unit | Source and Rationale |
| --- | --- | --- | --- |
| rr | 4.5 | – | Estimated from historical demand overdispersion |
| pp | 0.3 | – | Maximum likelihood estimate (MLE) |
| ρ\rho | 0.6 | – | Lag-1 autocorrelation estimate |
| hh | $2 | per unit | Industry benchmarks for holding costs |
| κ\kappa | 2 | USD per variance unit | Managerial input (risk-adjusted cost) |
| τ\tau | 0.90 | proportion | Service level target from SLA agreements |
| A1A\_{1} | 5 | USD per unit | Blockchain adoption cost studies |
| A2A\_{2} | 3 | USD per readiness level | Supplier readiness surveys |
| A3A\_{3} | 3 | USD | Interaction cost estimates |
| A4A\_{4} | 4 | USD | Revenue-sharing empirical estimates |

*Note:* Parameter ranges were also tested in sensitivity analyses as reported in Section [3](https://arxiv.org/html/2510.05487v1#S3 "3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective").

### B.3 Simulation Configuration

All simulation experiments were conducted under the following configuration settings:

* •

  Number of Monte Carlo replications per scenario: 10,000
* •

  Random seeds tested: 0, 42, 1234, 2023
* •

  Software environment: Python 3.10 using NumPy and SciPy libraries
* •

  Computational setup: Simulations parallelized across 16 CPU cores
* •

  Average memory utilization: 12–16 GB per process

### B.4 Additional Notes

* •

  The dynamic Negative Binomial process was initialized using the empirical mean and variance of observed demand time series.
* •

  All simulation outputs were validated for convergence by comparing results across multiple random seeds and replications.
* •

  For transparency, complete simulation code and raw output files are provided in the supplementary repository accompanying this article.

## Appendix C. Mathematical Proofs

This section provides formal derivations and sketches of the theoretical propositions cited in the main text. Detailed proofs can be made available upon request.

### C.1 Proposition 1: Monotonicity of the Overdispersion Index

Statement:
The overdispersion index of the Negative Binomial distribution,

|  |  |  |
| --- | --- | --- |
|  | O​D=VarianceMean=1+Meanr,OD=\frac{\text{Variance}}{\text{Mean}}=1+\frac{\text{Mean}}{r}, |  |

is monotonically decreasing in the dispersion parameter rr.

Proof Sketch:
Since the derivative with respect to rr is

|  |  |  |
| --- | --- | --- |
|  | ∂O​D∂r=−Meanr2,\frac{\partial OD}{\partial r}=-\frac{\text{Mean}}{r^{2}}, |  |

which is always negative, the function is strictly decreasing in rr for all r>0r>0.

### C.2 Proposition 2: Sensitivity of Expected Profit to Dispersion

Statement:
Higher dispersion parameters rr lead to an increase in expected profit under the assumed profit function and penalty structure.

Proof Outline:

* •

  As rr increases, the variance-to-mean ratio decreases.
* •

  This reduces the expected penalty term proportional to variance.
* •

  Simulations confirm that expected profit increases monotonically with rr, as summarized in Table [7](https://arxiv.org/html/2510.05487v1#S3.T7 "Table 7 ‣ 3.1 Baseline Calibration and Sensitivity (Global Superstore Dataset) ‣ 3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective").

A full derivation combining analytical sensitivity and simulation validation is available in the supplementary repository.

## Appendix D.Additional Robustness Checks

This section reports extended robustness checks to demonstrate the stability and reproducibility of the simulation results.

### D.1 Random Seed Robustness Table

S6 Table shows expected profit and fill rate metrics computed under multiple random seeds, demonstrating minimal variability across simulations.

S6 Table. Random Seed Robustness Results

| Seed | Expected Profit (USD) | Fill Rate (%) |
| --- | --- | --- |
| 0 | 1,190.84 | 99.49 |
| 42 | 1,192.28 | 99.58 |
| 99 | 1,161.23 | 99.55 |
| 1234 | 1,141.73 | 99.51 |
| 2023 | 1,165.82 | 99.60 |

The variations are within a narrow band (<4%<4\%), indicating stable estimates across random seeds.

### D.2 Bootstrap Confidence Intervals

S7 Table reports bootstrap confidence intervals (BCI) for expected profit and fill rate based on 1,000 resamples.

S7 Table. Bootstrap Confidence Intervals

| Metric | Mean Estimate | 2.5% Quantile | 97.5% Quantile |
| --- | --- | --- | --- |
| Expected Profit | $1,180.00 | $1,050.00 | $1,300.00 |
| Fill Rate (%) | 99.55 | 98.90 | 99.85 |

These intervals further confirm the robustness of the simulation outcomes presented in Section [3](https://arxiv.org/html/2510.05487v1#S3 "3 Results ‣ Smart Contract Adoption under Discrete Overdispersed Demand: A Negative Binomial Optimization Perspective").

## Appendix E.Monthly Demand Data

This section reports example observations from the monthly aggregated demand series used in model calibration.

### E.1 Sample Monthly Demand Table

S8 Table shows a subset of the monthly aggregated demand data used in the simulation calibration. The full 48-month dataset is available upon request.

S8 Table. Sample of Monthly Aggregated Demand

| Year-Month | Quantity Ordered |
| --- | --- |
| 2011-01 | 1,463 |
| 2011-02 | 1,224 |
| 2011-03 | 1,836 |
| 2011-04 | 2,020 |
| 2011-05 | 2,013 |
| 2011-06 | 3,112 |
| 2011-07 | 1,774 |
| 2011-08 | 3,035 |
| 2011-09 | 3,707 |
| 2011-10 | 2,727 |

*Note: The full monthly time series is available in the supplementary data repository or upon request.*

—

## Appendix F.Additional Figures

This section presents supplementary visualizations referenced in the Results and Discussion sections.

### F.1 Tornado Diagram

S3 Fig presents the tornado diagram summarizing how variations in key model parameters influence expected profit in the SCMS dataset.

![Refer to caption](tornado_diagram.png)


S3 Fig. Sensitivity tornado diagram showing the influence of key parameters on expected profit. The length of each bar indicates the magnitude of impact when the parameter varies by ±10% from its baseline value, while other parameters are held constant. Estimates are based on 10,000 Monte Carlo replications using the SCMS dataset.

S9 Table reports the absolute change in expected profit resulting from ±10% variations in key model parameters. These results complement the S5 Fig tornado diagram and quantify the sensitivity of simulation outcomes to parameter uncertainty.

S9 Table. Sensitivity of Expected Profit to ±10% Parameter Variations

| Parameter | Impact on Expected Profit (USD) |
| --- | --- |
| Dispersion parameter (rr) | +641.34 |
| Success probability (pp) | +1,396.48 |
| Variance penalty (κ\kappa) | +555.79 |
| Smart contract adoption (α\alpha) | +155.04 |
| Revenue-sharing coefficient (A4A\_{4}) | +229.64 |

* •

  Notes: Impacts represent the absolute change in expected profit when each parameter is varied by ±10% relative to the baseline. Estimates are derived from 10,000 Monte Carlo replications using the SCMS dataset.

### F.2 Forecast Error Comparison Graph

The forecasting error analysis was conducted using the SCMS dataset. All models were trained on historical monthly demand observations from January 2012 through December 2014. Predictions were then generated for a 12-month holdout period spanning January to December 2015.

S4 Fig visualizes the comparative accuracy of the four forecasting approaches, displaying both the trajectories of actual versus predicted demand and the distribution of forecast errors.

![Refer to caption](forecast_error_comparison.png)


S4 Fig. Forecasting error comparison across ARIMA, Exponential Smoothing (ETS), Poisson regression, and Negative Binomial regression. Solid lines represent actual demand over the holdout period, while dashed lines indicate model predictions. The shaded areas highlight the magnitude of prediction errors by method.

S10 Table reports quantitative accuracy metrics (MAE, MAPE) for four forecasting models applied to the SCMS dataset. These results complement the visual comparison shown in S4 Fig.

S10 Table. Forecasting Performance Metrics (SCMS Dataset)

| Model | MAE | MAPE (%) |
| --- | --- | --- |
| ARIMA | 1,736.82 | 28.91 |
| Exponential Smoothing (ETS) | 1,430.54 | 23.36 |
| Poisson Regression | 1,452.96 | 23.59 |
| Negative Binomial Regression | 1,354.52 | 22.36 |

* •

  Notes: MAE = Mean Absolute Error. MAPE = Mean Absolute Percentage Error. Lower values indicate better predictive performance.
* •

  All models were trained on identical historical windows and evaluated on the same holdout sample to ensure comparability.
* •

  The Negative Binomial model incorporated an explicit overdispersion parameter, enhancing its fit to the high-variance characteristics of SCMS demand data.

Overall, the results confirm that the Negative Binomial regression consistently achieved the lowest error metrics, underscoring its suitability for forecasting overdispersed, high-variability demand patterns typical of large-scale humanitarian supply chains.

### F.3 Scenario Simulation Result Graphs

S6 Fig displays simulation outcomes examining how expected profit and its variability evolve as smart contract adoption increases under different order quantities (QQ).

![Refer to caption](scenario_simulation_results.png)


S6 Fig. Scenario simulation results showing the relationship between smart contract adoption level (α\alpha) and expected profit for four order quantity (QQ) scenarios. The shaded area denotes the interquartile range (25th–75th percentile) of simulated profits over 10,000 Monte Carlo replications. Curves represent median expected profit trajectories for each QQ.

Interpretation:

* •

  Increasing α\alpha from 0 to 1 consistently improves expected profit across all QQ levels, with gains ranging from approximately $20 to $25.
* •

  Higher order quantities (Q=1,000,000Q=1,000,000) exhibit larger profit variability, reflecting the amplification of overdispersion risk at scale.
* •

  The interquartile ranges illustrate that adoption not only increases profit but also mitigates downside volatility.

Data Source and Methodology: Simulations were based on the SCMS Delivery History Dataset. Demand was modeled as a Negative Binomial distribution (r=4.5r=4.5, p=0.3p=0.3). Each scenario was replicated 10,000 times to compute central tendencies and variability.

## Appendix G.Supplementary Regression Diagnostics

This section reports additional convergence diagnostics and regression outputs not included in the main text.

### G.1 Negative Binomial Model Fit Log

Below we provide the estimation log and key outputs for the Negative Binomial regression applied to the SCMS dataset. This output documents convergence diagnostics and supports the transparency of model calibration procedures.

```
Optimization terminated successfully.
Current function value: 8.308711
Iterations: 86
Function evaluations: 159
Gradient evaluations: 62
Covariance Type: nonrobust
Pseudo R-squared: 0.02807
```

This log confirms that the estimation converged successfully and that overdispersion was statistically significant.

```
NegativeBinomial Regression Results
==============================================================================
Dep. Variable:                 Demand   No. Observations:                   42
Model:               NegativeBinomial   Df Residuals:                       40
Method:                           MLE   Df Model:                            1
Date:                Sun, 06 Jul 2025   Pseudo R-squ.:                 0.02807
Time:                        01:04:39   Log-Likelihood:                -348.97
converged:                       True   LL-Null:                       -359.05
Covariance Type:            nonrobust   LLR p-value:                 7.129e-06
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          7.6636      0.097     79.250      0.000       7.474       7.853
x1             0.0207      0.004      5.069      0.000       0.013       0.029
alpha          0.0968      0.021      4.640      0.000       0.056       0.138
==============================================================================
Estimated alpha (dispersion parameter): 0.0968
```

This output demonstrates that the Negative Binomial model converged reliably and estimated a statistically significant dispersion parameter, supporting the appropriateness of using this distribution rather than the Poisson alternative.