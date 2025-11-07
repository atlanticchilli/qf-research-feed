---
authors:
- Dennis Thumm
doc_id: arxiv:2511.04361v1
family_id: arxiv:2511.04361
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Causal Regime Detection in Energy Markets With Augmented Time Series Structural
  Causal Models
url_abs: http://arxiv.org/abs/2511.04361v1
url_html: https://arxiv.org/html/2511.04361v1
venue: arXiv q-fin
version: 1
year: 2025
---


Dennis Thumm
  
Max-Planck-Institute for Intelligent Systems
  
Tuebingen, Germany
  
dennis.thumm@tuebingen.mpg.de
  
Asian Institute for Digital Finance
  
National University of Singapore
  
Singapore
  
dennis.thumm@u.nus.edu

###### Abstract

Energy markets exhibit complex causal relationships between weather patterns, generation technologies, and price formation, with regime changes occurring continuously rather than at discrete break points. Current approaches model electricity prices without explicit causal interpretation or counterfactual reasoning capabilities. We introduce Augmented Time Series Causal Models (ATSCM) for energy markets, extending counterfactual reasoning frameworks to multivariate temporal data with learned causal structure. Our approach models energy systems through interpretable factors (weather, generation mix, demand patterns), rich grid dynamics, and observable market variables. We integrate neural causal discovery to learn time-varying causal graphs without requiring ground truth DAGs. Applied to real-world electricity price data, ATSCM enables novel counterfactual queries such as "What would prices be under different renewable generation scenarios?".

## 1 Introduction

Energy markets exhibit intricate causal relationships between weather conditions, generation technologies, grid constraints, and price formation. Unlike traditional financial markets, electricity cannot be stored economically, creating immediate causal dependencies between supply, demand, and pricing ziel2018day. Current electricity price forecasting methods focus on prediction accuracy without providing causal interpretation or counterfactual reasoning capabilities lago2021forecasting.

Recent advances in counterfactual reasoning for high-dimensional data through Augmented Structural Causal Models (ASCM) enable principled causal inference in complex domains pan2024counterfactual; pan2025counterfactual. However, these frameworks assume static causal structures and cannot handle the temporal dependencies and regime changes inherent in energy systems.

We bridge this gap by introducing Augmented Time Series Causal Models (ATSCM) for energy markets, enabling counterfactual reasoning about alternative weather patterns, generation scenarios, and policy interventions. Our key contributions include:

* •

  A theoretical framework extending ASCM to multivariate temporal data with learned causal structure
* •

  A neural architecture modeling interpretable energy factors, complex grid dynamics, and market observations
* •

  Integration of causal discovery for time-varying DAG learning without ground truth requirements
* •

  Empirical validation on real electricity market data with interpretable counterfactual capabilities

## 2 Related Work

Causal Inference in Financial Markets. Causal data science has been applied to financial stress testing and risk management gao2018causal; rigana2024navigating. However, energy markets present unique challenges due to physical constraints, storage limitations, and renewable intermittency that require specialized treatment.

Electricity Price Forecasting. Traditional approaches focus on statistical methods (ARIMA, VAR) or machine learning models (LSTM, gradient boosting) for price prediction lago2021forecasting; ziel2018day. While achieving good predictive performance, these methods lack explicit causal interpretation and cannot answer counterfactual queries.

Counterfactual Reasoning. ASCM frameworks pan2024counterfactual; pan2025counterfactual enable counterfactual reasoning in high-dimensional spaces but assume static causal structures. Time series causal methods like TNCM-VAE thumm2025towards, SCIGAN bica2020estimatingthe and Causal Transformer melnychuk2022causal address temporal dynamics but do not handle regime changes in learned causal graphs.

## 3 Problem Formalization

### 3.1 Energy Market Causal Structure

Consider multivariate electricity market time series 𝐯t∈ℝd\mathbf{v}\_{t}\in\mathbb{R}^{d} capturing weather, generation, consumption, and pricing variables. Unlike structural breaks with discrete timing, energy markets exhibit continuous causal regime changes driven by weather patterns, policy shifts, renewable intermittency, and cross-border flows.

Let 𝒢t\mathcal{G}\_{t} represent the time-varying directed acyclic graph (DAG) encoding causal relationships at time tt. A causal regime change occurs when:

|  |  |  |
| --- | --- | --- |
|  | 𝒢t≠𝒢t−1​ or ​ℳ​(t)≠ℳ​(t−1)\mathcal{G}\_{t}\neq\mathcal{G}\_{t-1}\text{ or }{\mathcal{M}}(t)\neq{\mathcal{M}}(t-1) |  |

where ℳ​(t){\mathcal{M}}(t) represents the causal mechanisms (functional relationships and noise distributions) governing the DAG at time tt, also known as Structural Causal Model (SCM) pearl2009causality.

### 3.2 ATSCM for Energy Markets

We extend ASCM pan2024counterfactual; pan2025counterfactual to temporal energy data through a three-level generative hierarchy with learned causal structure:

###### Definition 3.1 (Energy Market ATSCM)

An Energy Market ATSCM is a tuple ℳt=⟨Ut,{Wt,𝐈t,𝐕t},Ft,P​(Ut),𝒢t⟩\mathcal{M}^{t}=\langle U^{t},\{W^{t},\mathbf{I}^{t},\mathbf{V}^{t}\},F^{t},P(U^{t}),\mathcal{G}^{t}\rangle where:

1. 1.

   Wt∈ℝdWW^{t}\in\mathbb{R}^{d\_{W}} are interpretable energy factors: 
     
   Wt={weathert,generation\_mixt,demand\_patternt,market\_regimet}W^{t}=\{\text{weather}\_{t},\text{generation\\_mix}\_{t},\text{demand\\_pattern}\_{t},\text{market\\_regime}\_{t}\}
2. 2.

   𝐈t∈ℝdI\mathbf{I}^{t}\in\mathbb{R}^{d\_{I}} is a rich energy dynamics state capturing complex grid interactions, cross-border flows, merit order effects, and storage dynamics
3. 3.

   𝐕t∈ℝdV\mathbf{V}^{t}\in\mathbb{R}^{d\_{V}} represents observable market variables (prices, consumption, generation, weather measurements)
4. 4.

   𝒢t\mathcal{G}^{t} is the learned time-varying causal graph over {Wt,𝐈t,𝐕t}\{W^{t},\mathbf{I}^{t},\mathbf{V}^{t}\}
5. 5.

   Temporal evolution: Wt=fW​(Wt−1,𝐈t−1,UWt,𝒢t)W^{t}=f\_{W}(W^{t-1},\mathbf{I}^{t-1},U\_{W}^{t},\mathcal{G}^{t}), 𝐈t=fI​(Wt,𝐈t−1,UIt,𝒢t)\mathbf{I}^{t}=f\_{I}(W^{t},\mathbf{I}^{t-1},U\_{I}^{t},\mathcal{G}^{t}), 𝐕t=fV​(𝐈t,UVt)\mathbf{V}^{t}=f\_{V}(\mathbf{I}^{t},U\_{V}^{t})

This hierarchy enables modeling clear causal pathways (Weather →\rightarrow Renewable Generation →\rightarrow Net Load →\rightarrow Price) while capturing complex interactions through learned temporal dynamics.

### 3.3 Counterfactual Energy Scenarios

ATSCM enables novel counterfactual reasoning about energy markets:

###### Definition 3.2 (Energy Counterfactual Query)

Given observed market data 𝐯1:T\mathbf{v}^{1:T} and intervention d​o​(Wτ:T=w′)do(W\_{\tau:T}=w^{\prime}) on energy factors from time τ\tau, the energy counterfactual query is:

|  |  |  |
| --- | --- | --- |
|  | P∗(𝐕τ:T=𝐯′|𝐕1:T=𝐯1:T,do(Wτ:T=w′))P^{\*}(\mathbf{V}\_{\tau:T}=\mathbf{v}^{\prime}|\mathbf{V}^{1:T}=\mathbf{v}^{1:T},do(W\_{\tau:T}=w^{\prime})) |  |

This answers questions like: "What would electricity prices be if wind generation were 30% higher?" or "How would a nuclear plant shutdown affect cross-border electricity flows?"

## 4 Methodology

### 4.1 Neural Architecture

Our ATSCM architecture implements the three-level hierarchy for energy markets:

#### Level 1 - Energy Factors (WtW^{t}).

Domain-specific interpretable components:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Wt={weathert,generationt,demandt,markett}⊂ℝ27\displaystyle W^{t}=\{\text{weather}\_{t},\text{generation}\_{t},\text{demand}\_{t},\text{market}\_{t}\}\subset\mathbb{R}^{27} |  | (1) |

where weather factors include temperature, wind, and precipitation; generation factors capture nuclear, renewable, and conventional capacity; demand factors model consumption patterns and residual load; and market factors include commodity returns and cross-border exchanges.

#### Level 2 - Rich Energy Dynamics (𝐈t\mathbf{I}^{t}).

High-dimensional state capturing:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐈t=gI​(Wt,𝐈t−1,UIt,𝒢t;θI)\displaystyle\mathbf{I}^{t}=g\_{I}(W^{t},\mathbf{I}^{t-1},U\_{I}^{t},\mathcal{G}^{t};\theta\_{I}) |  | (2) |

This encodes merit order dynamics, grid constraints, renewable intermittency effects, storage optimization, and cross-country coupling mechanisms that determine price formation but are not directly observable.

#### Level 3 - Market Observations (𝐕t\mathbf{V}^{t}).

Observable electricity market variables:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝐕t=gV​(𝐈t,UVt;θV)∈ℝ35\displaystyle\mathbf{V}^{t}=g\_{V}(\mathbf{I}^{t},U\_{V}^{t};\theta\_{V})\in\mathbb{R}^{35} |  | (3) |

Including consumption, generation by source, weather measurements, commodity prices, and the target electricity price variations.

### 4.2 Causal Discovery Integration

Since ground truth causal graphs are unavailable in energy markets, we integrate neural causal discovery:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒢t=fd​i​s​c​o​v​e​r​y​(𝐕1:t,W1:t;θd​i​s​c)\displaystyle\mathcal{G}^{t}=f\_{discovery}(\mathbf{V}^{1:t},W^{1:t};\theta\_{disc}) |  | (4) |

using a differentiable DAG learning approach with temporal consistency constraints. The discovered graphs encode domain knowledge (weather influences renewables, generation affects prices) while learning time-varying relationships.

### 4.3 Training Objective

Our objective combines reconstruction, causal consistency, counterfactual realism, and causal discovery:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒ=ℒrecon+λ1​ℒcausal+λ2​ℒcounterfactual+λ3​ℒdiscovery\displaystyle\mathcal{L}=\mathcal{L}\_{\text{recon}}+\lambda\_{1}\mathcal{L}\_{\text{causal}}+\lambda\_{2}\mathcal{L}\_{\text{counterfactual}}+\lambda\_{3}\mathcal{L}\_{\text{discovery}} |  | (5) |

where ℒdiscovery\mathcal{L}\_{\text{discovery}} enforces DAG constraints, sparsity, and temporal stability of learned causal structures.

## 5 Conclusion

We introduced ATSCM for energy markets, the first framework enabling counterfactual reasoning about electricity price formation with learned causal structure. Our approach successfully models complex energy systems through interpretable factors while achieving competitive forecasting performance. The framework opens new possibilities for energy scenario analysis, policy evaluation, and risk management through principled counterfactual reasoning.

Future work includes empirical validation, extending to higher-frequency data, incorporating additional market mechanisms (auctions, reserves), and applications to renewable energy integration and grid stability analysis.