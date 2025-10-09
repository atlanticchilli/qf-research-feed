---
authors:
- Jinho Cha
- Eunchan D. Cha
- Emily Yoo
- Hyoshin Song
doc_id: arxiv:2510.06379v1
family_id: arxiv:2510.06379
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Modeling ROI in Chronic Disease Management: A Simulation-Based Framework Integrating
  Patient Adherence and Policy Timing'
url_abs: http://arxiv.org/abs/2510.06379v1
url_html: https://arxiv.org/html/2510.06379v1
venue: arXiv q-fin
version: 1
year: 2025
---


[jcha@GwinnettTech.edu](mailto:jcha@GwinnettTech.edu)
  
\fnmE.D. \surCha
  
\fnmEmily \surYoo
  
\fnmH. \surSong
\*
[
[
[

###### Abstract

Background: Chronic diseases impose a sustained burden on healthcare systems through progressive deterioration and long-term costs. Although adherence-enhancing interventions are widely promoted, their return on investment (ROI) remains uncertain, particularly under heterogeneous patient behavior and socioeconomic variation.

Methods: We developed a simulation-based framework integrating disease progression, time-varying adherence, and policy timing. Cumulative healthcare costs were modeled over a 10-year horizon using continuous-time stochastic formulations calibrated with Medical Expenditure Panel Survey (MEPS) data stratified by income. ROI was estimated across adherence gains (δ\delta) and policy costs (γ\gamma).

Results: Early and adaptive interventions yielded the highest ROI by sustaining adherence and slowing progression. ROI exceeded 20% when δ≥0.20\delta\geq 0.20 and γ≤1.5\gamma\leq 1.5, whereas low-impact or high-cost policies failed to break even. Subgroup analyses showed a 32% ROI gap between the lowest and highest income strata, with projected savings of $312 per patient versus baseline. Sensitivity tests confirmed robustness under stochastic adherence and inflation variability.

Conclusions: The framework offers a transparent, adaptable tool for evaluating cost-effective adherence strategies. By linking behavioral effectiveness with fiscal feasibility, it supports design of robust and equitable chronic disease policies. Reported ROI values represent conservative lower bounds, and extensions incorporating DALYs and QALYs illustrate scalability toward health outcome integration.

###### keywords:

Return on investment, Chronic disease, Simulation modeling, Policy timing, Patient adherence, Economic evaluation, Health equity

## 1 Introduction

Chronic diseases—such as diabetes, cardiovascular disorders, and chronic respiratory conditions—account for more than 70% of global deaths annually, disproportionately affecting low-income and aging populations [[1](https://arxiv.org/html/2510.06379v1#bib.bib1)]. In the United States, chronic care represents over 85% of total health expenditure [[2](https://arxiv.org/html/2510.06379v1#bib.bib2)]. As this burden intensifies, developing efficient and equitable strategies for resource allocation has become a central challenge in sustainable public health management.

Traditional cost-modeling approaches, including actuarial tables, regression-based risk models, and Markov chains, have long guided expenditure projections and risk forecasting [[3](https://arxiv.org/html/2510.06379v1#bib.bib3), [4](https://arxiv.org/html/2510.06379v1#bib.bib4), [5](https://arxiv.org/html/2510.06379v1#bib.bib5), [6](https://arxiv.org/html/2510.06379v1#bib.bib6)]. While valuable for population-level planning, these models rely on static covariates and linear assumptions that overlook dynamic feedback among disease progression, behavioral adherence, and policy timing, limiting their ability to capture complex real-world interactions.

Recent advances in simulation-based modeling address this gap by incorporating system dynamics, feedback loops, and behavioral economics into public health evaluation [[7](https://arxiv.org/html/2510.06379v1#bib.bib7), [8](https://arxiv.org/html/2510.06379v1#bib.bib8), [9](https://arxiv.org/html/2510.06379v1#bib.bib9)]. Yet most frameworks still analyze components—such as disease severity [[10](https://arxiv.org/html/2510.06379v1#bib.bib10)], patient adherence [[11](https://arxiv.org/html/2510.06379v1#bib.bib11)], or behavioral nudges [[12](https://arxiv.org/html/2510.06379v1#bib.bib12)]—in isolation, with stochastic variation in patient behavior often underrepresented [[13](https://arxiv.org/html/2510.06379v1#bib.bib13)].

The economic and clinical burden of chronic diseases has been widely studied across diverse modeling paradigms. Time-series, multivariate regression, and actuarial models remain standard for expenditure forecasting [[7](https://arxiv.org/html/2510.06379v1#bib.bib7), [14](https://arxiv.org/html/2510.06379v1#bib.bib14)], but lack adaptability to evolving behavioral and policy contexts. Simulation approaches such as Markov models, system dynamics, and agent-based models (ABMs) address these limitations by representing nonlinear interactions, stochasticity, and feedback [[15](https://arxiv.org/html/2510.06379v1#bib.bib15), [16](https://arxiv.org/html/2510.06379v1#bib.bib16), [17](https://arxiv.org/html/2510.06379v1#bib.bib17), [18](https://arxiv.org/html/2510.06379v1#bib.bib18)]. ABMs can further embed social norms, adherence rules, and local interactions absent in conventional models [[19](https://arxiv.org/html/2510.06379v1#bib.bib19), [20](https://arxiv.org/html/2510.06379v1#bib.bib20), [5](https://arxiv.org/html/2510.06379v1#bib.bib5), [6](https://arxiv.org/html/2510.06379v1#bib.bib6)]. Hybrid frameworks combining system dynamics and ABMs enable real-time representation of service delivery, disease trajectories, and cost propagation [[21](https://arxiv.org/html/2510.06379v1#bib.bib21), [22](https://arxiv.org/html/2510.06379v1#bib.bib22), [3](https://arxiv.org/html/2510.06379v1#bib.bib3), [4](https://arxiv.org/html/2510.06379v1#bib.bib4)]. Despite such progress, few studies integrate patient-level feedback or temporally activated policy levers to assess ROI over long horizons [[23](https://arxiv.org/html/2510.06379v1#bib.bib23), [24](https://arxiv.org/html/2510.06379v1#bib.bib24)], and most cost-effectiveness analyses remain outcome-centric—focused on QALY or DALY metrics—rather than adherence-driven ROI dynamics.

Parallel developments in machine learning (ML) and predictive analytics have enhanced healthcare cost modeling. Using clinical, demographic, and behavioral data from electronic health records and claims databases, ML models can accurately forecast expenditures [[25](https://arxiv.org/html/2510.06379v1#bib.bib25), [26](https://arxiv.org/html/2510.06379v1#bib.bib26), [27](https://arxiv.org/html/2510.06379v1#bib.bib27), [28](https://arxiv.org/html/2510.06379v1#bib.bib28), [29](https://arxiv.org/html/2510.06379v1#bib.bib29)]. They identify key cost drivers such as depression, LDL levels, and comorbidities, while informing risk-based policy design—e.g., prioritizing adherence reminders for high-risk patients [[30](https://arxiv.org/html/2510.06379v1#bib.bib30), [31](https://arxiv.org/html/2510.06379v1#bib.bib31)]. Yet these models are primarily predictive rather than mechanistic, limiting transparency and scenario comparability for policy evaluation.

Adherence remains central to both health outcomes and healthcare costs. Poor medication adherence increases hospitalizations and mortality [[32](https://arxiv.org/html/2510.06379v1#bib.bib32), [33](https://arxiv.org/html/2510.06379v1#bib.bib33)], whereas modest improvements yield substantial long-term savings [[34](https://arxiv.org/html/2510.06379v1#bib.bib34)]. However, most adherence models assume uniform behavioral responses, overlooking heterogeneity linked to socioeconomic status, mental health, and provider engagement [[35](https://arxiv.org/html/2510.06379v1#bib.bib35), [36](https://arxiv.org/html/2510.06379v1#bib.bib36)]. Such behavioral variation underscores the need for frameworks that explicitly model heterogeneity and temporal adherence dynamics.

Emerging policy simulation models have begun to explore the timing and persistence of intervention effects. Microsimulation and dynamic cohort studies show that early behavioral interventions can markedly reduce downstream costs, particularly in high-risk subgroups [[37](https://arxiv.org/html/2510.06379v1#bib.bib37), [38](https://arxiv.org/html/2510.06379v1#bib.bib38)], whereas delayed or generic programs often yield diminishing returns [[39](https://arxiv.org/html/2510.06379v1#bib.bib39)]. Adaptive policy approaches that trigger interventions based on evolving risk or adherence trajectories have been proposed to improve efficiency [[40](https://arxiv.org/html/2510.06379v1#bib.bib40)]. These trends reflect a broader movement toward precision health policy—linking individual behavioral data to population-scale economic evaluation.

Nonetheless, key research gaps remain. Few frameworks jointly model disease progression, adherence dynamics, and policy activation within a unified simulation structure. Continuous-time formulations enabling flexible scenario exploration are rare, and stochastic behavioral variation is often simplified. Moreover, integration of nationally representative datasets such as MEPS and NHANES remains limited [[41](https://arxiv.org/html/2510.06379v1#bib.bib41), [42](https://arxiv.org/html/2510.06379v1#bib.bib42)]. Addressing these limitations requires models that are mathematically tractable, interpretable, and empirically grounded.

Building on recent advances in health economics and behavioral simulation [[43](https://arxiv.org/html/2510.06379v1#bib.bib43), [44](https://arxiv.org/html/2510.06379v1#bib.bib44), [24](https://arxiv.org/html/2510.06379v1#bib.bib24)], we propose a modular, ROI-focused framework that integrates adherence dynamics, disease progression, and policy timing into a continuous-time simulation calibrated to empirical data. The model links behavioral economics and healthcare-cost dynamics to yield interpretable, policy-relevant insights.

Our contributions are threefold. First, we present a unified framework bridging behavioral economics with health-cost modeling. Second, we identify nonlinear ROI thresholds to optimize intervention timing and intensity. Third, we demonstrate empirical validity and adaptability across income-stratified populations using MEPS and NHANES data. The remainder of this paper outlines the model formulation (Section [2](https://arxiv.org/html/2510.06379v1#S2 "2 Model Formulation ‣ Modeling ROI in Chronic Disease Management: A Simulation-Based Framework Integrating Patient Adherence and Policy Timing")), intervention scenarios and simulation results (Sections [3](https://arxiv.org/html/2510.06379v1#S3 "3 Intervention Scenarios ‣ Modeling ROI in Chronic Disease Management: A Simulation-Based Framework Integrating Patient Adherence and Policy Timing")–[4](https://arxiv.org/html/2510.06379v1#S4 "4 Results ‣ Modeling ROI in Chronic Disease Management: A Simulation-Based Framework Integrating Patient Adherence and Policy Timing")), and policy implications (Section [5](https://arxiv.org/html/2510.06379v1#S5 "5 Discussion ‣ Modeling ROI in Chronic Disease Management: A Simulation-Based Framework Integrating Patient Adherence and Policy Timing")). Extended derivations, robustness tests, and parameter tables are provided in the Supplementary Appendices.

## 2 Model Formulation

This section introduces the core structure of our policy evaluation model, integrating disease progression, behavioral adaptation, and policy cost into a unified cost function. All subsequent intervention scenarios in Section [3](https://arxiv.org/html/2510.06379v1#S3 "3 Intervention Scenarios ‣ Modeling ROI in Chronic Disease Management: A Simulation-Based Framework Integrating Patient Adherence and Policy Timing") are grounded in this mathematical framework.

### 2.1 Model Structure: Cumulative Cost Function

Cumulative cost was defined as the discounted sum of instantaneous costs over time,
C​(t)=C0+∫0te−ρ​s​c​(s)​𝑑sC(t)=C\_{0}+\int\_{0}^{t}e^{-\rho s}c(s)\,ds, where ρ\rho is the continuous discount rate.
Instantaneous cost c​(s)c(s) combines four components—disease burden, adherence effort, policy expenditure, and an optional health–outcome term:

|  |  |  |  |
| --- | --- | --- | --- |
|  | c​(s)=α​Dmax1+e−k​(s−s0)+β​A​(s)2+γ​P​(s)+λ​H​(s).c(s)=\frac{\alpha D\_{\max}}{1+e^{-k(s-s\_{0})}}+\beta A(s)^{2}+\gamma P(s)+\lambda H(s). |  | (1) |

This compact formulation provides the structural basis for all policy scenarios.
Detailed definitions and parameter values are listed in Supplementary Appendix E.
Figure [1](https://arxiv.org/html/2510.06379v1#S2.F1 "Figure 1 ‣ 2.1 Model Structure: Cumulative Cost Function ‣ 2 Model Formulation ‣ Modeling ROI in Chronic Disease Management: A Simulation-Based Framework Integrating Patient Adherence and Policy Timing") illustrates the relative contribution of each component under an Early Adherence scenario.

![Refer to caption](Fig1.png)


Figure 1: Instantaneous cost c​(s)c(s) decomposition under an Early Adherence scenario.
Total cost (black) is composed of disease burden (blue), adherence term (green),
and policy expenditure (orange). The dotted line indicates the discount factor e−ρ​se^{-\rho s} (scaled).

### 2.2 Parameter Definitions and Calibration

Table [1](https://arxiv.org/html/2510.06379v1#S2.T1 "Table 1 ‣ 2.2 Parameter Definitions and Calibration ‣ 2 Model Formulation ‣ Modeling ROI in Chronic Disease Management: A Simulation-Based Framework Integrating Patient Adherence and Policy Timing") lists key model parameters, their roles, and data sources.
Parameters were estimated using MEPS and NHANES data (2015–2023), with policy costs benchmarked to CDC program reports.

Table 1: Model parameters and empirical sources.

| Parameter | Definition | Source / Notes |
| --- | --- | --- |
| C0C\_{0} | Baseline annual cost per patient | MEPS 2015–2023 |
| ρ\rho | Discount rate (3%) | US Panel on Cost-Effectiveness |
| Dmax,k,s0D\_{\max},k,s\_{0} | Disease progression parameters | NHANES prevalence curves |
| α\alpha | Disease cost multiplier | MEPS calibration |
| A0,δA\_{0},\delta | Baseline adherence and policy shift | NHANES medication-use data |
| τ\tau | Policy start time | Intervention year |
| β\beta | Adherence cost weight (β<0\beta<0 indicates savings) | Calibrated value |
| P​(s),γP(s),\gamma | Policy cost function and scale | CDC/NIH program benchmarks |

### 2.3 Stochastic Behavior Modeling

Adherence gain δ\delta was modeled as a random variable from a Beta distribution fitted to MEPS adherence data.
Each simulation drew δ\delta and propagated it through the cost model to obtain distributions of total cost and ROI.
A binary alternative (high vs. low responders, probability pp) was tested using NHANES subgroup prevalence.

### 2.4 Simulation Design

Simulations were run in Python (NumPy/SciPy) over a 10-year horizon.
Inputs were drawn from MEPS (cost, adherence) and NHANES (disease burden, comorbidity).
Four cases were compared: (i) no policy, (ii) deterministic adherence shift, (iii) stochastic Beta uptake, and (iv) subgroup heterogeneity.
Outcomes included cumulative cost C​(t)C(t), ROI, and payback time (years to net savings).

### 2.5 Scenario Integration

All intervention scenarios (Section [3](https://arxiv.org/html/2510.06379v1#S3 "3 Intervention Scenarios ‣ Modeling ROI in Chronic Disease Management: A Simulation-Based Framework Integrating Patient Adherence and Policy Timing")) use the same structural model, differing only in policy timing (τ\tau), adherence response (δ\delta), and cost intensity (γ,P​(s)\gamma,P(s)).
This uniform design ensures that observed differences in outcomes reflect policy configuration rather than model specification.

## 3 Intervention Scenarios

To assess the cost-effectiveness and behavioral dynamics of chronic care policies,
we simulated six policy scenarios differing in intervention timing, adherence response,
and policy cost intensity (Table [2](https://arxiv.org/html/2510.06379v1#S3.T2 "Table 2 ‣ 3 Intervention Scenarios ‣ Modeling ROI in Chronic Disease Management: A Simulation-Based Framework Integrating Patient Adherence and Policy Timing")).
These configurations span realistic contrasts—from proactive early engagement to inefficient, high-cost programs—
and were calibrated using MEPS and NHANES data on chronic disease and treatment adherence
[[41](https://arxiv.org/html/2510.06379v1#bib.bib41), [42](https://arxiv.org/html/2510.06379v1#bib.bib42)].

All scenarios share a unified cost framework:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ci​(s)=α​Dmax1+e−k​(s−s0)+β​Ai​(s)2+γi​Pi​(s),c\_{i}(s)=\frac{\alpha D\_{\max}}{1+e^{-k(s-s\_{0})}}+\beta A\_{i}(s)^{2}+\gamma\_{i}P\_{i}(s), |  | (2) |

where Ai​(s)A\_{i}(s) represents adherence behavior and Pi​(s)P\_{i}(s) denotes policy expenditure for scenario ii.
Cumulative cost is obtained as C​(t)=C0+∫0te−ρ​s​ci​(s)​𝑑sC(t)=C\_{0}+\int\_{0}^{t}e^{-\rho s}c\_{i}(s)\,ds.
Economic performance was summarized by the return on investment (ROI),
defined as ROI = (Cbaseline−Cpolicy)/Cpolicy(C\_{\text{baseline}}-C\_{\text{policy}})/C\_{\text{policy}}.

Table 2: Policy scenario configurations.

| Scenario | Start (τ\tau) | Adherence Δ​δ\Delta\delta | Cost (γ\gamma) | Description |
| --- | --- | --- | --- | --- |
| Baseline | – | 0 | 0 | Natural progression; reference benchmark. |
| Early Adherence | 2 | +0.3 | 1.5 | Early proactive engagement. |
| Delayed Intervention | 5 | +0.3 | 1.5 | Late reactive response. |
| Regressive Adherence | 2 | +0.3→0 | 1.2 | Behavioral decay over time. |
| Adaptive Nudges | varies | +0.3 (stepwise) | 2.0 | Dynamic re-engagement to sustain adherence. |
| Low-Impact Policy | 2 | +0.05 | 3.0 | High spending, minimal behavioral change. |

Parameter values are illustrative, calibrated to MEPS/NHANES (2015–2023).

These six scenarios form the basis for the simulation results in Section [4](https://arxiv.org/html/2510.06379v1#S4 "4 Results ‣ Modeling ROI in Chronic Disease Management: A Simulation-Based Framework Integrating Patient Adherence and Policy Timing"),
allowing outcome differences to be directly attributed to policy design rather than model specification.
Detailed scenario-specific cost formulations (ci​(s)c\_{i}(s)) and adherence trajectories
are provided in Supplementary Appendix E for full mathematical reference.

—

### 3.1 Scenario 1: Baseline (No Intervention)

In the absence of intervention, adherence remains constant A​(s)=A0A(s)=A\_{0} and policy cost is zero P​(s)=0P(s)=0.
This represents natural disease progression and serves as the counterfactual benchmark for ROI comparisons.

—

### 3.2 Scenario 2: Early Adherence Activation

An early intervention begins at τ=2\tau=2 years, producing a discrete increase in adherence
A​(s)=A0+δ​I​(s−τ)A(s)=A\_{0}+\delta I(s-\tau) with cost P​(s)=I​(s−τ)P(s)=I(s-\tau).
This captures early-stage programs such as digital reminders or education campaigns.
By improving adherence before major disease progression, early activation achieves sustained cost reduction over time.

—

### 3.3 Scenario 3: Delayed Intervention

A reactive policy starts later (τ=5\tau=5), using the same adherence shift A​(s)=A0+δ​I​(s−5)A(s)=A\_{0}+\delta I(s-5).
Because improvement begins after disease burden has accumulated, total savings are limited.
This highlights the diminishing benefit of delayed responses in chronic-care management.

—

### 3.4 Scenario 4: Regressive Adherence

Adherence initially rises but decays exponentially without reinforcement,
A​(s)=A0+δ​e−θ​(s−τ)​I​(s−τ)A(s)=A\_{0}+\delta e^{-\theta(s-\tau)}I(s-\tau).
One-time incentives or static nudges yield short-lived gains, and both cost savings and health improvements erode as behavior returns toward baseline.

—

### 3.5 Scenario 5: Adaptive Nudges

This model introduces feedback-based re-engagement.
Whenever adherence drops below a threshold AthreshA\_{\text{thresh}}, additional nudges are activated, increasing A​(s)A(s) and incurring extra policy cost proportional to the number of activations.
Appropriate threshold calibration maintains stable adherence and positive ROI,
demonstrating that adaptive strategies can achieve long-term efficiency if properly tuned.

—

### 3.6 Scenario 6: High-Cost, Low-Impact Policy

Here, adherence gains are minimal (δ≪1)(\delta\ll 1) despite large expenditures (γ≫1)(\gamma\gg 1).
A​(s)=A0+δ​I​(s−τ)A(s)=A\_{0}+\delta I(s-\tau) and P​(s)=I​(s−τ)P(s)=I(s-\tau) represent an inefficient policy with weak behavioral change.
Such imbalance between cost intensity and behavioral efficacy results in negative ROI and poor cost-effectiveness.

—

### 3.7 Summary Insight

Across all simulations, early or adaptive interventions yield the strongest and most sustainable cost-effectiveness,
while delayed, decaying, or inefficient policies show limited or negative returns.
These findings emphasize that timing, sustained engagement, and economic balance
are key to maximizing policy value in chronic care systems.

## 4 Results

All results presented here are based on ROI defined in terms of direct healthcare
expenditures (λ=0\lambda=0 in Equation [1](https://arxiv.org/html/2510.06379v1#S2.E1 "In 2.1 Model Structure: Cumulative Cost Function ‣ 2 Model Formulation ‣ Modeling ROI in Chronic Disease Management: A Simulation-Based Framework Integrating Patient Adherence and Policy Timing")). Broader outcomes such as
QALYs, DALYs, or societal productivity effects were not part of the primary analysis.
Exploratory extensions with nonzero λ\lambda (Sections [4](https://arxiv.org/html/2510.06379v1#S4 "4 Results ‣ Modeling ROI in Chronic Disease Management: A Simulation-Based Framework Integrating Patient Adherence and Policy Timing"), Supplementary Appendix E)
provide illustrative examples, but a full integration of health-adjusted outcomes
remains beyond the scope of this study.

### 4.1 Scenario-Based Simulation Outcomes

The simulation model produced distinct outcomes across the baseline and six intervention scenarios, revealing clear trade-offs in clinical progression, adherence behavior, and long-term costs over a 10-year horizon.

#### 4.1.1 Baseline and Intervention Comparisons

The flat baseline scenario produced a mean 10-year discounted cost of $3953.07, whereas the Early Adherence intervention reduced this to $3602.26, yielding an average ROI of 9.7%. Figure [2](https://arxiv.org/html/2510.06379v1#S4.F2 "Figure 2 ‣ 4.1.1 Baseline and Intervention Comparisons ‣ 4.1 Scenario-Based Simulation Outcomes ‣ 4 Results ‣ Modeling ROI in Chronic Disease Management: A Simulation-Based Framework Integrating Patient Adherence and Policy Timing") illustrates clear divergence between baseline and intervention trajectories, confirming that early engagement achieves substantial long-term savings.

ROI in this study reflects direct healthcare expenditures only; broader effects such as avoided hospitalizations, QALYs, DALYs, or productivity gains were excluded. Accordingly, all reported ROI values should be viewed as conservative lower bounds of intervention value.

![Refer to caption](Fig2.png)


Figure 2: Baseline vs. Early Adherence intervention: Distribution of 10-year discounted healthcare costs across 10,000 Monte Carlo simulations. The baseline yielded a mean cost of $3953.07, while the Early Adherence case reduced this to $3602.26 (ROI = 9.7%).

Policy interventions shifted these cost trajectories through adherence dynamics. Early and adaptive strategies provided the greatest cost containment and disease mitigation, whereas delayed, regressive, and low-impact approaches remained near baseline, indicating limited effectiveness.

#### 4.1.2 Disease Severity and Adherence Trajectories

Clinical outcomes diverged substantially across scenarios (Figure [3](https://arxiv.org/html/2510.06379v1#S4.F3 "Figure 3 ‣ 4.1.2 Disease Severity and Adherence Trajectories ‣ 4.1 Scenario-Based Simulation Outcomes ‣ 4 Results ‣ Modeling ROI in Chronic Disease Management: A Simulation-Based Framework Integrating Patient Adherence and Policy Timing")).
Early or adaptive adherence improvements reduced year-10 severity below 0.70,
whereas weak or unsustained engagement left severity above 0.87.
Including a decaying baseline reveals that assuming constant adherence can overstate incremental benefits and highlights the need for realistic counterfactuals.

![Refer to caption](Fig3.png)


Figure 3: Disease severity trajectories under policy scenarios with flat vs. decaying baseline adherence.
Early Adherence and Adaptive Nudges lower final severity below 0.70, while Delayed,
Regressive, and Low-Impact interventions show minimal change.
The decay baseline illustrates that constant-adherence assumptions may inflate incremental benefits.

Differences in severity reflect adherence behavior over time (Figure [4](https://arxiv.org/html/2510.06379v1#S4.F4 "Figure 4 ‣ 4.1.2 Disease Severity and Adherence Trajectories ‣ 4.1 Scenario-Based Simulation Outcomes ‣ 4 Results ‣ Modeling ROI in Chronic Disease Management: A Simulation-Based Framework Integrating Patient Adherence and Policy Timing")).
Early and adaptive policies maintained adherence above 0.8, supporting long-term control,
whereas regressive and low-impact designs eroded quickly, dropping below 0.4 by year 10.
Again, comparisons with a decaying baseline confirm that constant-adherence assumptions can exaggerate intervention value.

![Refer to caption](Fig4.png)


Figure 4: Adherence trajectories A​(s)A(s) across scenarios with flat vs. decaying baselines.
Early Adherence and Adaptive Nudges sustain adherence above 0.8,
while Regressive and Low-Impact designs decline toward baseline levels.
The decay baseline underscores that constant-adherence assumptions can exaggerate policy effects.

Overall, sustained adherence drives superior clinical outcomes:
interventions fostering consistent engagement achieve better control,
whereas late or decaying impacts yield little change.
Both intervention timing and baseline choice therefore critically shape ROI estimates.

#### 4.1.3 Cost Trajectories Across Scenarios

Figure [5](https://arxiv.org/html/2510.06379v1#S4.F5 "Figure 5 ‣ 4.1.3 Cost Trajectories Across Scenarios ‣ 4.1 Scenario-Based Simulation Outcomes ‣ 4 Results ‣ Modeling ROI in Chronic Disease Management: A Simulation-Based Framework Integrating Patient Adherence and Policy Timing") shows 10-year cumulative discounted
cost trajectories across scenarios, benchmarked against flat and decaying baselines.
Interventions with upfront investment—especially Early Adherence and
Adaptive Nudges—incurred higher early costs but subsequently flattened
expenditure growth, ending near $3900–4000 by year 10.
Thus, early, durable engagement mitigates clinical progression and prevents long-term
cost escalation.

![Refer to caption](Fig5.png)


Figure 5: Ten-year cumulative discounted cost trajectories across scenarios, benchmarked
against both flat and decaying baselines. Early Adherence and Adaptive Nudges flatten
long-run costs to $3900–4000 by year 10, while Delayed, Regressive, and Low-Impact
policies stay near or above baseline. Including a decaying baseline shows that constant
adherence may overstate savings. ROI values reflect direct healthcare expenditures only.

By contrast, the Low-Impact Policy incurred the highest cumulative cost
(¿$4600) despite minimal adherence or severity improvement.
Delayed and regressive interventions produced intermediate results, driven by timing
and adherence decay. Mapping these to ROI thresholds shows that cost containment
depends on early, sustained adherence gains; weaker designs often fail to break even.
Although ROI can be briefly positive in the Regressive scenario, discounting of future
costs limits long-run benefit, underscoring the role of time-discounting in ROI evaluation.

Policies achieving strong, early adherence lower long-term costs, whereas late or weak
interventions offer limited benefit.
Baseline choice (flat vs. decay) further shows that conservative assumptions reduce
incremental gains, reinforcing the need for comprehensive economic evaluation.

#### 4.1.4 ROI Landscape and Cost-Effectiveness Frontier

To assess the cost-effectiveness of adherence-based policies,
return on investment (ROI) is defined as the relative cost savings over
a 10-year horizon compared with the baseline (no intervention):

|  |  |  |  |
| --- | --- | --- | --- |
|  | ROI​(δ,γ)=(Cbaseline−Cpolicy​(δ,γ)Cpolicy​(δ,γ))×100,\text{ROI}(\delta,\gamma)=\left(\frac{C\_{\text{baseline}}-C\_{\text{policy}}(\delta,\gamma)}{C\_{\text{policy}}(\delta,\gamma)}\right)\times 100, |  | (3) |

where CbaselineC\_{\text{baseline}} is the cumulative cost without policy and
Cpolicy​(δ,γ)C\_{\text{policy}}(\delta,\gamma) the cost under a design defined by
adherence gain δ\delta and unit cost γ\gamma.
Positive ROI denotes net savings; negative values indicate excess cost.

Figure [6](https://arxiv.org/html/2510.06379v1#S4.F6 "Figure 6 ‣ 4.1.4 ROI Landscape and Cost-Effectiveness Frontier ‣ 4.1 Scenario-Based Simulation Outcomes ‣ 4 Results ‣ Modeling ROI in Chronic Disease Management: A Simulation-Based Framework Integrating Patient Adherence and Policy Timing") depicts the ROI design space.
The left panel shows a heatmap of ROI values across (δ,γ)(\delta,\gamma),
and the right panel the cost-effectiveness frontier relating ROI to total cost.
Together they highlight trade-offs between behavioral effectiveness and cost intensity.
Early Adherence and Adaptive Nudges occupy ROI-positive regions,
whereas high-cost or low-impact designs fall below the break-even line.

![Refer to caption](Fig6.png)


Figure 6: ROI landscape across policy designs.
Left: ROI heatmap over adherence gains (δ\delta) and policy costs (γ\gamma).
Right: Cost-effectiveness frontier showing ROI vs. total discounted cost.
Early Adherence and Adaptive Nudges remain ROI-positive, while costly or weak
designs fall below ROI = 0. ROI reflects direct healthcare expenditures only.

To illustrate the extensibility of the λ​H​(s)\lambda H(s) term, we examined how incorporating
health-adjusted outcomes (e.g., DALYs or QALYs) affects ROI estimates.
Assuming that each avoided DALY is valued at $50,000, and that the
Early Adherence policy averts 0.05 DALYs per patient
(corresponding to an additional monetized benefit of approximately $2,500),
the resulting ROI increases from 9.7% to roughly 15%.
This simplified example demonstrates how translating health gains into fiscal terms
can substantially enhance perceived economic value.
In the present study, however, we set λ=0\lambda=0, restricting ROI to direct healthcare
expenditures. A conservative QALY-based sensitivity example is provided in
Supplementary Appendix B.

![Refer to caption](Fig7.png)


Figure 7: Stochastic ROI outcomes across policy design space (N=10,000 simulations).
(a) Mean ROI heatmap across adherence gains (δ\delta) and costs (γ\gamma).
(b) Contour plot with ROI thresholds (−5%-5\%, 0%0\%, +5%+5\%) separating
negative, break-even, and positive-return regions.

#### 4.1.5 Stability of ROI Across Adherence Gains

A key reviewer concern was that ROI appeared large without clear break-even interpretation.
We therefore examine ROI stability as adherence gains (δ\delta) vary and identify the maximum policy cost (γ∗\gamma^{\*}) yielding non-negative ROI.

![Refer to caption](Fig8.png)


Figure 8: ROI dynamics across adherence gains (δ\delta) and policy costs (γ\gamma).
Left: ROI declines with rising cost, remaining positive over a wider range for higher δ\delta.
Center: Break-even threshold γ∗\gamma^{\*} for each δ\delta (ROI = 0).
Right: ROI slope with respect to γ\gamma, showing high-δ\delta interventions are less sensitive to inefficiency.

Figure [8](https://arxiv.org/html/2510.06379v1#S4.F8 "Figure 8 ‣ 4.1.5 Stability of ROI Across Adherence Gains ‣ 4.1 Scenario-Based Simulation Outcomes ‣ 4 Results ‣ Modeling ROI in Chronic Disease Management: A Simulation-Based Framework Integrating Patient Adherence and Policy Timing") shows three key patterns:
(1) ROI falls quickly as costs rise, but declines more slowly for larger δ\delta;
(2) the break-even cost γ∗\gamma^{\*} increases steeply with δ\delta, so small adherence gains unlock much larger feasible budgets;
(3) ROI sensitivity stabilizes for high δ\delta, indicating greater robustness to inefficiency.

##### Break-Even Thresholds.

Numerical estimates clarify the trade-off between adherence gain and policy cost.
When the adherence improvement is substantial (δ=0.25\delta=0.25), ROI exceeds 45% at low cost and remains positive until the unit cost approaches γ∗≈1,900\gamma^{\*}\!\approx\!1{,}900.
For moderate gains (δ=0.15\delta=0.15), the break-even point occurs near γ∗≈1,200\gamma^{\*}\!\approx\!1{,}200, while weaker interventions (δ=0.10\delta=0.10) turn negative once γ≥800\gamma\!\geq\!800, indicating limited fiscal tolerance.
Accordingly, community programs costing roughly $700–$1,000 per person remain financially viable only when δ≥0.15\delta\!\geq\!0.15.

These results illustrate a practical, reverse-engineering approach: for any target adherence gain, policymakers can infer the maximum allowable cost γ∗\gamma^{\*} that maintains ROI at or above zero. This defines a clear feasibility zone linking behavioral impact with fiscal discipline.
Interventions falling outside this region—those combining low adherence improvement with high implementation cost—should be redesigned or deprioritized. The ROI surface demonstrates that aligning adherence impact (δ\delta) with cost discipline (γ\gamma) is critical for sustaining both effectiveness and financial viability.

### 4.2 Advanced Design-Space Exploration

To extend the two-dimensional ROI heatmap analysis, ROI was modeled as a continuous function of adherence improvement (δ\delta) and unit policy cost (γ\gamma).
Figure [9](https://arxiv.org/html/2510.06379v1#S4.F9 "Figure 9 ‣ 4.2 Advanced Design-Space Exploration ‣ 4 Results ‣ Modeling ROI in Chronic Disease Management: A Simulation-Based Framework Integrating Patient Adherence and Policy Timing") presents a unified visualization combining a 3D surface and a 2D contour map, capturing the nonlinear interactions that define policy efficiency.
Threshold contours at ROI = 0%, 50%, and 100% delineate the transition from break-even to progressively higher return zones, making cost-effectiveness boundaries clearly visible.
The surface illustrates that ROI is not a linear function of either adherence or cost but is instead shaped by strong threshold and inflection effects.
In particular, policies with moderate implementation cost (γ≈1.5\gamma\approx 1.5) are most sensitive—small behavioral shifts in adherence can move them abruptly across the efficiency boundary between positive and negative ROI regions.

![Refer to caption](Fig9.png)


Figure 9: Advanced design-space exploration of ROI.
(a) 3D surface of ROI across (δ,γ)(\delta,\gamma) with contours at ROI = 0%, 50%, and 100%.
(b) ROI contour map showing the break-even frontier (black) and efficiency bands
at 50% (green) and 100% (orange).
These visualizations illustrate how small shifts in δ\delta or γ\gamma can move
interventions across critical efficiency boundaries.

Across the design space, three patterns emerge.
First, the efficient policy band appears as a narrow corridor where moderate costs combine with meaningful adherence gains; within this zone, ROI consistently exceeds 50–100%, identifying the most robust and economically sustainable strategies.
Second, a high degree of design sensitivity is observed: even slight reductions in δ\delta or increases in γ\gamma rapidly drive ROI into negative territory, emphasizing the importance of precise cost control and sustained behavioral impact.
Third, implementation vulnerability characterizes policies operating near the break-even frontier (ROI = 0%), where small deviations in either direction can determine fiscal success or failure.

Figure [9](https://arxiv.org/html/2510.06379v1#S4.F9 "Figure 9 ‣ 4.2 Advanced Design-Space Exploration ‣ 4 Results ‣ Modeling ROI in Chronic Disease Management: A Simulation-Based Framework Integrating Patient Adherence and Policy Timing") provides a strategic framework for understanding how behavioral effectiveness and implementation cost jointly determine economic viability.
Rather than evaluating isolated scenarios, policymakers can use this multidimensional surface to locate resilient, high-value regions of the design space—those that remain cost-effective under uncertainty.
Such a perspective supports evidence-based decision-making and adaptive policy refinement, particularly for chronic disease programs that rely on sustained adherence behavior to achieve long-term health and fiscal outcomes.

### 4.3 Robustness Analysis

To verify reliability, we performed robustness checks under alternative assumptions and parameter shifts, testing ROI consistency when (1) adherence dynamics include noise, (2) policy costs vary, and (3) disease progression accelerates.

#### 4.3.1 Stochastic Adherence Dynamics

Uncertainty in behavioral response was modeled by introducing stochasticity into
the adherence parameter δ\delta, treated as a truncated normal variable
𝒩​(δ,σ2)\mathcal{N}(\delta,\sigma^{2}) within [0,1][0,1].
This captures heterogeneity in motivation and persistence, acknowledging that identical interventions rarely yield uniform adherence.

Figure [10](https://arxiv.org/html/2510.06379v1#S4.F10 "Figure 10 ‣ 4.3.1 Stochastic Adherence Dynamics ‣ 4.3 Robustness Analysis ‣ 4 Results ‣ Modeling ROI in Chronic Disease Management: A Simulation-Based Framework Integrating Patient Adherence and Policy Timing") shows stochastic ROI distributions across ten representative policy designs
(δ∈{0.25,0.30,0.35,0.40}\delta\in\{0.25,0.30,0.35,0.40\}; γ∈{0.8,0.9,1.0}\gamma\in\{0.8,0.9,1.0\}; N=2000N=2000).
Red dashed lines mark mean ROI values.

![Refer to caption](Fig10.png)


Figure 10: Stochastic ROI distributions across ten policy designs
(2,000 simulations). Robust cases (δ≥0.30\delta\geq 0.30, γ≤0.9\gamma\leq 0.9)
maintain positive returns; fragile designs (δ=0.25\delta=0.25, γ=1.0\gamma=1.0)
shift leftward, producing negative ROI.

Three key patterns emerge:

1. 1.

   Robust ROI: Higher adherence (δ≥0.30\delta\geq 0.30) yields mostly positive ROI, with realization rates of 70–90% when γ≤0.9\gamma\leq 0.9.
2. 2.

   Fragile ROI: Low δ\delta or inflated γ\gamma produces negative, left-shifted distributions.
3. 3.

   Downside risk: Even near break-even, large downside variability highlights fiscal fragility.

Viewed holistically, Figure [10](https://arxiv.org/html/2510.06379v1#S4.F10 "Figure 10 ‣ 4.3.1 Stochastic Adherence Dynamics ‣ 4.3 Robustness Analysis ‣ 4 Results ‣ Modeling ROI in Chronic Disease Management: A Simulation-Based Framework Integrating Patient Adherence and Policy Timing") underscores the value of the ROI-efficient zone.
Under stochastic variability, high-impact, cost-efficient designs remain stable, whereas weak policies fall into negative-return regimes.
The full stochastic grid across δ∈[0.20,0.40]\delta\in[0.20,0.40] and γ∈[0.5,1.5]\gamma\in[0.5,1.5] is presented in Supplementary Appendix A.

#### 4.3.2 Inflated Policy Costs

Because ROI estimates may appear optimistic if costs are underestimated,
we tested the impact of inflating per-unit implementation costs on ROI outcomes.

Figure [11](https://arxiv.org/html/2510.06379v1#S4.F11 "Figure 11 ‣ 4.3.2 Inflated Policy Costs ‣ 4.3 Robustness Analysis ‣ 4 Results ‣ Modeling ROI in Chronic Disease Management: A Simulation-Based Framework Integrating Patient Adherence and Policy Timing") (left) presents mean ROI across 55 combinations
of adherence gain (δ\delta) and policy cost (γ\gamma).
Marker shape denotes δ\delta, size the probability of positive ROI, and color
ROI sign (green = ROI>0>0, red = ROI≤0\leq 0).
Designs with δ≥0.30\delta\!\geq 0.30 retain a >70>70% chance of positive ROI at moderate costs,
while low-gain or high-cost designs rapidly shift into negative-return zones.

The right panel compares five representative policies.
Under inflation, Early Adherence and Adaptive Nudges lose only
5–7 points yet remain ROI-positive;
Regressive and Low-Impact designs, already near break-even,
become unviable. The Delayed case shows smaller but still partial returns.

![Refer to caption](Fig11.png)


Figure 11: ROI sensitivity under 20% cost inflation.
Left: Mean ROI across 55 (δ,γ)(\delta,\gamma) scenarios
(shape = δ\delta, color = ROI sign, size = positive-rate).
Right: Five representative designs—robust
(Early Adherence, Adaptive Nudges) remain ROI-positive;
fragile (Regressive, Low-Impact) collapse below zero.

ROI robustness depends on both behavioral impact and cost resilience.
High-δ\delta, moderate-γ\gamma designs stay viable under inflation,
whereas fragile ones fail.
Policymakers should favor interventions that remain ROI-positive across
realistic cost scenarios to ensure near-term efficiency and long-term fiscal sustainability.

#### 4.3.3 Accelerated Disease Progression

To model faster disease worsening, we shortened progression intervals by 15%,
representing earlier complications or comorbid decline.
This raises baseline costs as patients reach severe states sooner,
but also increases the relative value of timely interventions.

Figure [12](https://arxiv.org/html/2510.06379v1#S4.F12 "Figure 12 ‣ 4.3.3 Accelerated Disease Progression ‣ 4.3 Robustness Analysis ‣ 4 Results ‣ Modeling ROI in Chronic Disease Management: A Simulation-Based Framework Integrating Patient Adherence and Policy Timing") compares baseline ROI (gray) and accelerated ROI (blue)
across ten (δ,γ)(\delta,\gamma) combinations.
Early Adherence and Adaptive Nudges improve ROI under urgency,
while Regressive and Low-Impact designs deteriorate;
Delayed interventions show limited but positive gains.

![Refer to caption](Fig12.png)


Figure 12: ROI outcomes under accelerated disease progression (15% shorter intervals).
Each subplot shows baseline ROI (gray) vs. accelerated ROI (blue) for five policy designs
across ten (δ,γ)(\delta,\gamma) combinations.
Timely, high-impact interventions (Early Adherence, Adaptive Nudges) retain or improve ROI,
while fragile, high-cost designs (Regressive, Low-Impact) lose viability.

Accelerated progression serves as a stress test of policy resilience.
Robust, early interventions preserve or enhance ROI,
whereas fragile designs collapse as costs rise.
This underscores the ROI-efficient zone and the high value of early, scalable actions
when clinical deterioration accelerates.

### 4.4 Policy Implications from Simulation Results

Simulation results highlight four key design principles.
First, early and high-impact interventions implemented before clinical decline consistently achieve the greatest ROI and long-term savings.
Second, ROI declines sharply once policy cost (γ\gamma) exceeds critical thresholds, underscoring the need for efficiency and cost discipline.
Third, only specific combinations of adherence gain (δ\delta) and cost (γ\gamma) yield positive ROI, defining a narrow zone of economically feasible designs.
Finally, interventions with minimal adherence improvement (δ<0.1\delta<0.1) rarely generate savings, even when inexpensive.
Together, these findings delineate actionable thresholds and design regions for sustainable, cost-effective behavioral policies, providing the empirical foundation for the Discussion.

## 5 Discussion

As healthcare systems face mounting pressures from chronic disease burdens and constrained budgets, the need for economically viable, behavior-focused interventions has never been more urgent. This study introduces a simulation-based evaluation framework for quantifying the return on investment (ROI) of adherence-enhancing interventions—tools often deployed with high expectations but limited ex-ante justification. By capturing the dynamic interplay among behavior, disease progression, and cost, our model bridges the gap between theoretical health economics and practical policy design.

### 5.1 Key Insights: Design Timing and Efficiency Drive ROI

Across all scenarios and sensitivity analyses, one insight stands out: timing and delivery efficiency matter as much as the magnitude of behavioral change. The Early Adherence and Adaptive Nudges policies consistently outperform others, generating the highest ROI under both deterministic and stochastic conditions. This outcome stems from two reinforcing mechanisms: (1) compounding health gains from early behavioral change and (2) the scalability and lower unit cost of early-phase interventions.

The model also reveals a nonlinear ROI response to policy cost (γ\gamma). While modest investments remain cost-effective, exceeding a critical threshold triggers rapid ROI declines, indicating that even well-designed programs can become economically fragile under fiscal constraints. Figure [9](https://arxiv.org/html/2510.06379v1#S4.F9 "Figure 9 ‣ 4.2 Advanced Design-Space Exploration ‣ 4 Results ‣ Modeling ROI in Chronic Disease Management: A Simulation-Based Framework Integrating Patient Adherence and Policy Timing") highlights robust combinations of adherence gain (δ\delta) and cost (γ\gamma) yielding positive returns, enabling policymakers to anticipate sustainable intervention conditions.

### 5.2 Theoretical Contributions: Behavior–Disease Modeling

Three theoretical advances emerge from this framework.
First, behavioral adherence is modeled as a tunable design parameter (δ\delta), allowing continuous policy refinement and flexible interpretation of intervention effects.
Second, adherence dynamics are integrated with disease progression, enabling simultaneous evaluation of clinical and economic outcomes—an advance over models that treat these domains separately.
Third, policy robustness is evaluated through stochastic simulation rather than local sensitivity analysis, allowing stability assessment under behavioral and clinical uncertainty.
Together, these contributions expand the methodological foundation for intervention modeling and support a dynamic, context-aware approach to behavioral policy evaluation.

### 5.3 Policy and System-Level Relevance: A Scalable Decision Tool

The proposed framework offers practical utility for policymakers confronting growing chronic disease burdens and challenges in maintaining adherence. With minimal data needs and a modular structure, it is adaptable across both high-capacity and resource-limited systems. It enables assessment of intervention effectiveness before large-scale implementation, identification of cost-feasible configurations under fiscal uncertainty, and more efficient allocation of limited resources toward interventions yielding favorable ROI. Beyond its technical value, the framework enhances transparency by linking behavioral dynamics with cost-effectiveness, promoting evidence-based prioritization, operational efficiency, and public trust in preventive health programs.

### 5.4 Limitations and Future Directions

While the model provides a structured, extensible framework for evaluating adherence-focused ROI, several conceptual and practical limitations remain.
First, behavioral dynamics are represented by a single policy parameter (δ\delta), oversimplifying individual variability and evolving adherence patterns. The deterministic disease component also limits the model’s ability to capture random events or multimorbidity. Although cost parameters were empirically calibrated, spatial heterogeneity and macroeconomic factors such as inflation are not modeled.

Future research should incorporate population heterogeneity and adaptive feedback via agent-based or dynamic models. Linking simulation outputs to administrative claims or electronic health records could enable empirical validation and facilitate real-world application.

A key methodological limitation is that ROI reflects only direct healthcare expenditures (λ=0\lambda=0). Broader outcomes—such as QALYs, DALYs, or productivity gains—were excluded, making reported ROI values conservative, cost-based estimates. Supplementary Appendix B illustrates how small health gains increase ROI when monetized; future studies should operationalize the extensible λ​H​(s)\lambda H(s) term to incorporate cost-per-QALY and other socio-economic outcomes.

Finally, our ROI stability analysis (Figure [9](https://arxiv.org/html/2510.06379v1#S4.F9 "Figure 9 ‣ 4.2 Advanced Design-Space Exploration ‣ 4 Results ‣ Modeling ROI in Chronic Disease Management: A Simulation-Based Framework Integrating Patient Adherence and Policy Timing")) shows that even modest adherence gains substantially expand feasible cost ranges before ROI turns negative. High-impact designs remain robust under fiscal constraints, whereas low-impact interventions become fragile as costs rise. This underscores the need to align behavioral effectiveness with cost discipline when designing scalable chronic care policies.

In practice, the modeled scenarios correspond to real-world programs: Early Adherence represents proactive interventions such as pharmacist counseling or SMS reminders; Adaptive Nudges reflect mHealth platforms with behavior-triggered incentives; and Delayed, Regressive, and Low-Impact cases parallel reactive or short-lived initiatives. Situating these archetypes within a unified economic framework helps policymakers prioritize early, durable, and cost-efficient designs for sustainable population health outcomes.

## 6 Conclusion

This paper introduces a unified simulation framework for evaluating the return on investment (ROI) of behavioral interventions in chronic disease management. By coupling adherence dynamics with disease progression and cost modeling, the framework captures the interplay between behavior and outcomes—moving beyond static cost-effectiveness analyses to offer a scalable, policy-oriented decision tool.

Simulation results yield three actionable insights. Early-stage interventions consistently generate the highest ROI, leveraging compounding health improvements and lower deployment costs. Second, economic viability hinges not only on behavioral effectiveness but also on the delivery mechanism’s efficiency—especially in budget-constrained environments. Third, well-structured policies can retain performance under stochastic variation in adherence, disease progression, and cost inflation, emphasizing the importance of robustness in policy design.

Conceptually, the model reframes behavioral change as a controllable design parameter rather than a fixed input—opening the door to proactive, optimized intervention strategies. Methodologically, it replaces traditional closed-form metrics with simulation-guided trade-off maps, offering intuitive visualizations that support data-informed decision-making. Practically, the framework is lightweight and modular, enabling rapid assessment of policy options before committing to costly real-world implementation.

In a healthcare landscape increasingly shaped by chronic conditions and resource limitations,
this approach offers a timely bridge between behavioral science and health economics.
By equipping decision-makers with interpretable and adaptable tools, it enables smarter, faster,
and more accountable policy design. While the framework provides actionable insights,
its ROI estimates remain conservative, as broader outcomes such as QALYs, DALYs,
and societal benefits were acknowledged conceptually but not fully implemented in the main analysis.
Nevertheless, an exploratory QALY-based extension in Supplementary Appendix B demonstrates how the
λ​H​(s)\lambda H(s) term can be operationalized to incorporate health-adjusted outcomes.
Accordingly, ROI values reported here should be viewed as lower-bound, cost-based estimates.
Extending the framework to explicitly include QALYs, DALYs, and societal effects
remains an important direction for future research.

## Declarations

Ethics approval
  
Not applicable. This study did not involve human subjects or identifiable data. The analysis was conducted using synthetic data generated via simulation and publicly available datasets (MEPS, NHANES) which do not require ethics committee approval.

Consent to participate
  
Not applicable. This research did not involve any primary data collection or participation of individuals.

Consent for publication
  
Not applicable. This study contains no individual data or images that require consent for publication.

Data availability
  
The datasets generated and/or analyzed during the current study, along with all simulation code, are publicly available at: <https://www.kaggle.com/datasets/ancientapplez/modeling-roi-in-chronic-disease-management>

Competing interests
  
The authors declare that they have no competing interests.

Funding
  
No funding was received for this study.

Author Contributions
  
Jinho Cha (J.C.) conceived the study, designed the methodology, developed the simulation framework, performed formal analyses, and drafted the manuscript.
Eunchan D. Cha (E.D.C.) contributed to policy scenario design, sensitivity analyses, validation, figure preparation, and assisted with manuscript revision.
Eunji Yoo (E.Y.) provided data preprocessing, programming support, figure preparation, and contributed to manuscript editing.
Hyunsuk Song (H.S.) conducted literature review, subgroup and robustness analyses, figure preparation, and assisted with manuscript refinement.
All authors read and approved the final manuscript.

Acknowledgements
  
Not applicable.

## References

* \bibcommenthead
* World Health Organization [2018]

  World Health Organization:
  Noncommunicable diseases country profiles 2018.
  Technical report,
  World Health Organization
  (2018).
  Accessed 2025-06-15.
  <https://www.who.int/nmh/publications/ncd-profiles-2018/en/>
* Centers for Disease Control and Prevention [2022]

  Centers for Disease Control and Prevention:
  Chronic Diseases in America.
  <https://www.cdc.gov/chronicdisease/resources/infographic/chronic-diseases.htm>.
  Accessed 2025-06-15
  (2022)
* Thorpe et al. [2004]

  Thorpe, K.E.,
  Florence, C.S.,
  Joski, P.:
  Which medical conditions account for the rise in health care spending?
  Health Aff
  23(4),
  4–4374445
  (2004)
  <https://doi.org/10.1377/hlthaff.w4.437>
* Zhang et al. [2017]

  Zhang, Y.,
  Baik, S.H.,
  Fendrick, A.M.,
  Baicker, K.:
  Long-term effects of value-based insurance design on health care utilization and expenditures.
  Am J Manag Care
  23(6),
  190–196
  (2017)
* Taylor et al. [2013]

  Taylor, M.J.,
  McNicholas, C.,
  Nicolay, C.,
  Darzi, A.,
  Bell, D.,
  Reed, J.E.:
  Systematic review of the application of the plan–do–study–act method to improve quality in healthcare.
  BMJ Qual Saf
  23(4),
  290–298
  (2013)
  <https://doi.org/10.1136/bmjqs-2013-001862>
* Russell et al. [2009]

  Russell, L.B.,
  Sinha, A.,
  Schmier, J.K.,
  Ahmed, F.,
  Rousculp, M.D.:
  Preparing for responsible public health decision making: a framework for integrating the economic evaluation of vaccination programs.
  Vaccine
  27(43),
  5886–5893
  (2009)
  <https://doi.org/10.1016/j.vaccine.2009.07.112>
* Milstein et al. [2011]

  Milstein, B.,
  Homer, J.B.,
  Briss, P.A.,
  Burton, D.,
  Pechacek, T.F.:
  Why behavioral and environmental interventions are needed to improve health at lower cost.
  Health Aff
  30(5),
  823–832
  (2011)
  <https://doi.org/10.1377/hlthaff.2010.1116>
* Best et al. [2012]

  Best, A.,
  Greenhalgh, T.,
  Lewis, S.,
  Saul, J.E.,
  Carroll, S.,
  Bitz, J.:
  Large-system transformation in health care: a realist review.
  Milbank Q
  90(3),
  421–456
  (2012)
  <https://doi.org/10.1111/j.1468-0009.2012.00670.x>
* Hunter et al. [2017]

  Hunter, D.J.,
  Erskine, J.,
  Small, A.,
  McGovern, T.,
  Hicks, C.,
  Whitty, P.:
  Doing transformational change in the english nhs in the era of health care reform.
  J Health Organ Manag
  29(1),
  10–24
  (2017)
  <https://doi.org/10.1108/JHOM-01-2016-0018>
* Tappenden et al. [2004]

  Tappenden, P.,
  Chilcott, J.,
  Eggington, S.,
  Oakley, J.,
  McCabe, C.:
  The cost-effectiveness of interferon beta and glatiramer acetate in the management of multiple sclerosis.
  Health Technol Assess
  8(27),
  –1248
  (2004)
  <https://doi.org/10.3310/hta8270>
* Cutler and Everett [2010]

  Cutler, D.M.,
  Everett, W.:
  Thinking outside the pillbox—medication adherence as a priority for health care reform.
  N Engl J Med
  362(17),
  1553–1555
  (2010)
  <https://doi.org/10.1056/NEJMp1002305>
* Thaler and Sunstein [2008]

  Thaler, R.H.,
  Sunstein, C.R.:
  Nudge: Improving Decisions About Health, Wealth, and Happiness.
  Yale University Press,
  New Haven
  (2008)
* Berwick et al. [2008]

  Berwick, D.M.,
  Nolan, T.W.,
  Whittington, J.:
  The triple aim: care, health, and cost.
  Health Aff
  27(3),
  759–769
  (2008)
  <https://doi.org/10.1377/hlthaff.27.3.759>
* Hunter and Fineberg [2017]

  Hunter, D.J.,
  Fineberg, H.V.:
  Convergence to common purpose in global health.
  N Engl J Med
  377(10),
  942–944
  (2017)
  <https://doi.org/10.1056/NEJMp1707572>
* Yang et al. [2013]

  Yang, W.,
  Dall, T.,
  Halder, P.,
  Gallo, P.,
  Kowal, S.,
  Hogan, P.:
  Economic costs of diabetes in the u.s. in 2012.
  Diabetes Care
  36(4),
  1033–1046
  (2013)
  <https://doi.org/10.2337/dc12-2625>
* Freeman and Yearwood [2019]

  Freeman, R.,
  Yearwood, M.:
  Modeling healthcare policy impacts using agent-based simulation: a case study of chronic disease care coordination.
  Health Syst
  8(2),
  79–91
  (2019)
  <https://doi.org/10.1080/20476965.2018.1490877>
* El-Sayed et al. [2012]

  El-Sayed, A.M.,
  Scarborough, P.,
  Seemann, L.,
  Galea, S.:
  Social network analysis and agent-based modeling in social epidemiology.
  Epidemiol Perspect Innov
  9(1),
  1
  (2012)
  <https://doi.org/10.1186/1742-5573-9-1>
* Galea et al. [2010]

  Galea, S.,
  Riddle, M.,
  Kaplan, G.A.:
  Causal thinking and complex system approaches in epidemiology.
  Int J Epidemiol
  39(1),
  97–106
  (2010)
  <https://doi.org/10.1093/ije/dyp296>
* Auchincloss and Diez Roux [2008]

  Auchincloss, A.H.,
  Diez Roux, A.V.:
  A new tool for epidemiology: the usefulness of dynamic-agent models in understanding place effects on health.
  Am J Epidemiol
  168(1),
  1–8
  (2008)
  <https://doi.org/10.1093/aje/kwn118>
* Gonzalez-Parra and Martcheva [2012]

  Gonzalez-Parra, G.,
  Martcheva, M.:
  A model of influenza with vaccination and antiviral treatment.
  J Theor Biol
  295,
  29–36
  (2012)
  <https://doi.org/10.1016/j.jtbi.2011.11.019>
* Atkinson et al. [2015]

  Atkinson, J.A.,
  Page, A.,
  Wells, R.,
  Milat, A.,
  Wilson, A.:
  A modelling tool for policy analysis to support the design of efficient and effective policy responses for complex public health problems.
  Implement Sci
  10,
  26
  (2015)
  <https://doi.org/10.1186/s13012-015-0221-5>
* Lee and Patel [2025]

  Lee, S.,
  Patel, R.:
  Modeling behavioral health intervention returns under policy constraints: A microsimulation approach.
  BMC Public Health
  25(1),
  118
  (2025)
  <https://doi.org/10.1186/s12889-025-01901-z>
* Sullivan et al. [2021]

  Sullivan, T.,
  Hwang, T.,
  Staib, A.,
  Sullivan, M.:
  Equity and the learning health system: future directions for public health research.
  Public Health Res Pract
  31(3),
  3132111
  (2021)
  <https://doi.org/10.17061/phrp3132111>
* Gupta et al. [2025]

  Gupta, R.,
  Taylor, G.,
  Kim, J.H.:
  Simulated roi estimation in public health intervention using multi-level policy switching models.
  J Public Health Manag Pract
  31(1),
  88–96
  (2025)
  <https://doi.org/10.1097/PHH.0000000000001500>
* Tran et al. [2025]

  Tran, E.T.,
  Chandrasekar, R.,
  Martinez, L.:
  Healthcare cost prediction for heterogeneous patient profiles using deep neural networks.
  Artif Intell Med
  137,
  102671
  (2025)
  <https://doi.org/10.1016/j.artmed.2025.102671>
* Patel and Chen [2025]

  Patel, A.,
  Chen, D.:
  The role of machine learning in reducing healthcare costs through medication adherence modeling.
  Health Econ Rev
  15(1),
  22
  (2025)
  <https://doi.org/10.1186/s13561-025-00429-7>
* Nguyen and Larson [2025]

  Nguyen, S.,
  Larson, B.:
  Impact of mental health on chronic conditions and cost implications: Leveraging data to predict risk.
  J Ment Health Chronic Care
  11(2),
  88–101
  (2025)
  <https://doi.org/10.1080/20469047.2025.1122345>
* Xu et al. [2021]

  Xu, Y.,
  Wang, Y.,
  Xu, X.:
  Predicting mortality risk using machine learning in nhanes: Application to cardiovascular and all-cause mortality.
  BMC Med Inform Decis Mak
  21(1),
  13
  (2021)
  <https://doi.org/10.1186/s12911-021-01536-9>
* Hoehn et al. [2021]

  Hoehn, R.S.,
  Sullivan, P.G.,
  Koroukian, S.M.:
  Machine learning algorithms for mortality prediction in nhanes: performance and explainability.
  J Biomed Inform
  113,
  103652
  (2021)
  <https://doi.org/10.1016/j.jbi.2020.103652>
* Chen et al. [2023]

  Chen, H.,
  Li, C.,
  Huang, C.:
  Application of interpretable machine learning to predict frailty and mortality in nhanes adults.
  Sci Rep
  13,
  1–11
  (2023)
  <https://doi.org/10.1038/s41598-023-28128-7>
* Rasheed et al. [2022]

  Rasheed, J.,
  Qayyum, A.,
  Gohar, M., et al.:
  Explainable machine learning for healthcare using shap: A review.
  IEEE Rev Biomed Eng
  15,
  312–327
  (2022)
  <https://doi.org/10.1109/RBME.2021.3093116>
* Ho et al. [2006]

  Ho, P.M.,
  Rumsfeld, J.S.,
  Masoudi, F.A., et al.:
  Effect of medication nonadherence on hospitalization and mortality among patients with diabetes mellitus.
  Arch Intern Med
  166(17),
  1836–1841
  (2006)
  <https://doi.org/10.1001/archinte.166.17.1836>
* Sokol et al. [2005]

  Sokol, M.C.,
  McGuigan, K.A.,
  Verbrugge, R.R.,
  Epstein, R.S.:
  Impact of medication adherence on hospitalization risk and healthcare cost.
  Med Care
  43(6),
  521–530
  (2005)
  <https://doi.org/10.1097/01.mlr.0000163641.86870.af>
* Cutler et al. [2018]

  Cutler, R.L.,
  Fernandez-Llimos, F.,
  Frommer, M., et al.:
  Economic impact of medication non-adherence by disease groups: a systematic review.
  BMJ Open
  8(1),
  016982
  (2018)
  <https://doi.org/10.1136/bmjopen-2017-016982>
* Kane et al. [2013]

  Kane, J.M.,
  Kishimoto, T.,
  Correll, C.U.:
  Non-adherence to medication in patients with psychotic disorders: epidemiology, contributing factors and management strategies.
  World Psychiatry
  12(3),
  216–226
  (2013)
  <https://doi.org/10.1002/wps.20060>
* Zullig and Bosworth [2015]

  Zullig, L.L.,
  Bosworth, H.B.:
  Engaging patients to optimize medication adherence.
  Clin Ther
  37(1),
  25–34
  (2015)
  <https://doi.org/10.1016/j.clinthera.2014.11.017>
* van Baal et al. [2016]

  Baal, P.H.,
  Meltzer, D.O.,
  Brouwer, W.B.:
  Future costs, fixed healthcare budgets, and the decision rule to adopt new health technologies.
  Health Econ
  25(2),
  237–248
  (2016)
  <https://doi.org/10.1002/hec.3133>
* Bilinski et al. [2020]

  Bilinski, A.,
  Emanuel, E.J.,
  Salomon, J.A.:
  Covid-19 and excess all-cause mortality in the us and 18 comparison countries.
  JAMA
  324(20),
  2100–2102
  (2020)
  <https://doi.org/10.1001/jama.2020.20717>
* Kim et al. [2020]

  Kim, D.D.,
  Silver, M.C.,
  Kunst, N.,
  Cohen, J.T.,
  Ollendorf, D.A.,
  Neumann, P.J.:
  Perspective and costing in cost-effectiveness analysis, 1974–2018.
  Pharmacoeconomics
  38,
  1135–1145
  (2020)
  <https://doi.org/10.1007/s40273-020-00930-2>
* Choi et al. [2023]

  Choi, J.,
  Shin, S.,
  Kim, J.:
  Adaptive policy modeling for time-sensitive intervention planning in population health.
  Health Policy
  127(1),
  1–9
  (2023)
  [https://doi.org/%\*\*\*\*␣bmc.bbl␣Line␣650␣\*\*\*\*10.1016/j.healthpol.2022.10.004](https://doi.org/%****%20bmc.bbl%20Line%20650%20****10.1016/j.healthpol.2022.10.004)
* U.S. Agency for Healthcare Research and Quality (AHRQ) [2023]

  U.S. Agency for Healthcare Research and Quality (AHRQ):
  Medical Expenditure Panel Survey (MEPS), 2015–2023 Data.
  <https://meps.ahrq.gov/mepsweb/>.
  Accessed September 2025
  (2023)
* Centers for Disease Control and Prevention (CDC) [2022]

  Centers for Disease Control and Prevention (CDC):
  National Health and Nutrition Examination Survey (NHANES), 2015–2022 Cycle.
  <https://www.cdc.gov/nchs/nhanes/>.
  Accessed September 2025
  (2022)
* Simonsen et al. [2024]

  Simonsen, M.,
  Rossing, P.,
  Heerspink, H.J.L., et al.:
  Modeling individualized intervention effects in chronic disease progression.
  JAMA Netw Open
  7(3),
  241233
  (2024)
  <https://doi.org/10.1001/jamanetworkopen.2024.1233>
* Evans et al. [2021]

  Evans, D.,
  Tandon, A.,
  Murray, C.J.L.:
  Policy modeling for sustainable health financing: tools and frameworks.
  Health Syst Reform
  7(2),
  1908791
  (2021)
  <https://doi.org/10.1080/23288604.2021.1908791>