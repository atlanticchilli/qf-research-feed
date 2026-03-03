---
authors:
- Harrison Katz
doc_id: arxiv:2603.00422v1
family_id: arxiv:2603.00422
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 1 Introduction
url_abs: http://arxiv.org/abs/2603.00422v1
url_html: https://arxiv.org/html/2603.00422v1
venue: arXiv q-fin
version: 1
year: 2026
---

Title:


Content selection saved. Describe the issue below:

Description:

[License: CC BY 4.0](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2603.00422v1[stat.AP] 28 Feb 2026

Coupled Supply and Demand Forecasting
  
in Platform Accommodation Markets
  
Harrison E. Katz
  
Finance Data Science & Strategy, Airbnb Inc., San Francisco, CA, USA

harrison.katz@airbnb.com

###### Abstract

Tourism demand forecasting is methodologically mature, but it typically treats accommodation supply as fixed or exogenous. In platform-mediated short-term rentals, supply is elastic, decision-driven, and co-evolves with demand through pricing, information design, and interventions. I reframe the core issue as endogenous stock-out censoring: realized booked nights satisfy Bk,t≤min⁡(Dk,t,Sk,t)B\_{k,t}\leq\min(D\_{k,t},S\_{k,t}), so booking models that ignore supply learn a regime-specific ceiling and become fragile under policy changes and supply shocks. This narrated review synthesizes work from tourism forecasting, revenue management, two-sided market economics, and Bayesian time-series methods; develops a three-part coupling framework (behavioral, informational, intervention); and illustrates the identification failure with a toy simulation. I conclude with a focused research agenda for jointly forecasting supply, demand, and their compositions.
  
Keywords: Tourism forecasting; Two-sided markets; Compositional time series; Platform economics; Coupled systems; Censored demand; Supply forecasting

## 1 Introduction

Tourism forecasting has a long tradition of modeling demand as a destination-level time series (arrivals, spending, hotel nights) with methods organized around econometric specifications, univariate time series, and a growing body of machine learning (Song and Li, [2008](#bib.bib75 "Tourism demand modelling and forecasting—a review of recent research"); Song et al., [2019](#bib.bib76 "A review of research on tourism demand forecasting")). Two widely cited syntheses survey the post-2000 period and track the evolution of methods and evidence across five decades. This review is narrower and explicitly forward-looking: it targets forecasting in accommodation markets where supply and demand are coupled by design, especially platform-mediated short-term rentals.

The crucial shift is that “capacity” is no longer slow-moving and near-fixed (as in most hotel markets), but elastic at multiple margins: host entry and exit, listing activation and deactivation, and day-level availability decisions. Empirically, peer-to-peer platforms exhibit greater supply-side flexibility than hotels, with effective capacity that can expand or contract at the margins of host entry, listing activation, and calendar availability; the largest competitive effects concentrate in peak-demand periods when this incremental flexibility matters most (Farronato and Fradkin, [2022](#bib.bib33 "The welfare effects of peer entry: the case of Airbnb and the accommodation industry"); Zervas et al., [2017](#bib.bib88 "The rise of the sharing economy: estimating the impact of Airbnb on the hotel industry")). From a theory standpoint, two-sided market economics provides the backbone for why forecasting demand alone is incomplete in such settings: platforms internalize cross-side externalities via pricing, matching, governance, and information design (Rochet and Tirole, [2003](#bib.bib68 "Platform competition in two-sided markets"); Weyl, [2010](#bib.bib85 "A price theory of multi-sided platforms"); Armstrong, [2006](#bib.bib7 "Competition in two-sided markets")).

A second motivation is that the post-2020 environment made structural breaks and regime change unavoidable in tourism and hospitality time series. That reality pushes modern forecasting toward methods that (i) represent time variation and discontinuities, (ii) remain probabilistically calibrated under intervention and drift, and (iii) encode constraints (such as nonnegativity and shares summing to one) by construction rather than by post-hoc adjustment.

These concerns are not purely methodological. Destination managers, tourism boards, and policymakers rely on accommodation forecasts to allocate budgets, plan infrastructure, and evaluate regulatory interventions. When those forecasts are built on models that treat supply as fixed, they produce misleading signals: a city that introduces a short-term rental registration rule and then observes declining bookings may wrongly conclude that tourism demand has fallen, when in fact the binding constraint has shifted from demand to supply. The coupling framework developed here provides the conceptual tools to avoid such misdiagnosis.

The paper makes three contributions. First, it develops a coupling framework (behavioral, informational, and intervention coupling) that explains why independent supply and demand forecasts are fragile under policy changes, supply regime shifts, and platform intervention, even when they may perform adequately for short-horizon extrapolation in stable environments. Second, it demonstrates the resulting identification failure through a simulation showing that demand-only forecasters systematically over-predict after supply shocks while coupled forecasters do not. Third, it outlines a five-problem research agenda whose resolution would constitute the core of a coupled forecasting research program for platform markets. A detailed survey of the methodological building blocks for coupled forecasting is provided in the Supplementary Material.

### Notation and forecasting targets

Platform accommodation data have a natural two-dimensional time structure: a stay date ss (the night a guest occupies a listing) and a booking date bb (the date the reservation is made), with lead time ℓ=s−b\ell=s-b. Throughout the paper, tt indexes stay-date periods (weeks or months) and all variables are aggregated over lead times unless otherwise noted.

Let DtD\_{t} denote latent demand intent: the number of listing-nights that guests would book for stay dates in period tt if inventory were unconstrained and matching were frictionless. Let StS\_{t} denote effective supply: the number of listing-nights made available by hosts for stay dates in period tt, defined as physical availability (active listing, unblocked night, not already reserved). Price (PtP\_{t}) and platform visibility/ranking (RtR\_{t}) are treated as separate covariates that influence both DtD\_{t} and StS\_{t} but are not inventory in the same units as bookings. Let BtB\_{t} denote realized booked nights (the number of listing-nights that result in a completed reservation). Measurement issues affecting the construction of StS\_{t}, BtB\_{t}, and demand proxies from external data sources are discussed in the Supplementary Material.

Within a segment kk narrow enough that listings are close substitutes, realized booked nights satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bk,t≤min⁡(Dk,t,Sk,t),B\_{k,t}\leq\min(D\_{k,t},\;S\_{k,t}), |  | (1) |

with equality under perfect within-segment matching and no cross-segment substitution. Here Dk,tD\_{k,t} denotes demand intent at prevailing prices and platform exposure: it is not a deep structural primitive but the quantity of listing-nights that guests would book in segment kk given the prices PtP\_{t} and ranking RtR\_{t} they actually face, if inventory were unconstrained. Changes in PtP\_{t} or RtR\_{t} shift Dk,tD\_{k,t}; the inequality captures only the additional constraint imposed by physical availability Sk,tS\_{k,t}. Aggregating across segments, Bt=∑kBk,t≤∑kmin⁡(Dk,t,Sk,t)B\_{t}=\sum\_{k}B\_{k,t}\leq\sum\_{k}\min(D\_{k,t},S\_{k,t}). The gap reflects matching frictions (search costs, preference heterogeneity, booking abandonment). A derived summary is the matching efficiency mt:=Bt/min⁡(Dt,St)≤1m\_{t}:=B\_{t}/\min(D\_{t},S\_{t})\leq 1. Under perfect substitutability within the entire market, mt=1m\_{t}=1 and Bt=min⁡(Dt,St)B\_{t}=\min(D\_{t},S\_{t}). This stylized single-segment benchmark is used in several places for expositional clarity, with the understanding that matching frictions strengthen rather than weaken the coupling argument. Note that mtm\_{t} is a conceptual quantity: because DtD\_{t} is latent and StS\_{t} is measured with error, mtm\_{t} is not directly observable and must be estimated from fitted model components or bounded from observable proxies.

The primary forecasting targets are:

1. 1.

   Realized booked nights BtB\_{t}: directly observed; the primary operational forecast target. Measured in listing-nights (not reservation counts). Success metric: out-of-sample point accuracy (MAE, MASE) and distributional calibration (CRPS).
2. 2.

   Latent demand DtD\_{t}: not directly observed; inferred from BtB\_{t} and supply proxies. The uncensored demand level is needed for counterfactual analysis, policy evaluation, and capacity planning. Success metric: structural adequacy and coherence with the observed BtB\_{t} constraint.
3. 3.

   Available supply StS\_{t}: partially observed through scrapes, platform dashboards, or internal records. Treated here as “inventory” when scalar and “supply” when referring to the broader distributional object (composition by host type, price tier, location). Success metric: out-of-sample accuracy and measurement fidelity.

The remainder of the paper is organized as follows. Section [2](#S2 "2 Tourism demand forecasting since 2019") reviews tourism demand forecasting since the Song et al. ([2019](#bib.bib76 "A review of research on tourism demand forecasting")) synthesis. Section [3](#S3 "3 Platform accommodation markets and the supply-side gap") reviews platform accommodation markets, two-sided foundations, and the supply-side forecasting gap. Section [4](#S4 "4 The coupling problem") develops the coupling argument, using the censoring formulation to clarify when and why decoupled forecasts fail, and provides a simulation-based demonstration. Section [5](#S5 "5 Research agenda") presents the research agenda with explicit identification assumptions and evaluation designs. Section [7](#S7 "7 Conclusion") concludes.

## 2 Tourism demand forecasting since 2019

The post-2019 demand-forecasting literature is best read as incremental progress on a mature methodological core, plus a major diversification of data sources and evaluation settings. The most efficient framing is to position the Song et al. ([2019](#bib.bib76 "A review of research on tourism demand forecasting")) review as the methodological baseline and then note extensions along six frontiers.

Benchmark baselines and combination. A persistent finding is that simple methods remain competitive. Exponential smoothing, ARIMA, and naïve benchmarks continue to perform well against more complex alternatives (Athanasopoulos et al., [2011](#bib.bib9 "The tourism forecasting competition")). Forecast combination has emerged as both a practical baseline and a research focus (Bates and Granger, [1969](#bib.bib15 "The combination of forecasts"); Timmermann, [2006](#bib.bib79 "Forecast combinations")), with Song et al. ([2021](#bib.bib74 "Bayesian bootstrap aggregation for tourism demand forecasting")) demonstrating that bagging-based combination stabilizes accuracy in both normal and disrupted periods. Notably, combination gains arise precisely when individual models disagree, which is the expected condition when an omitted supply ceiling binds intermittently.

Deep learning. A common pattern combines decomposition with neural sequence models to mitigate overfitting (Zhang et al., [2021](#bib.bib89 "Tourism demand forecasting: a decomposed deep learning approach")). Recurrent architectures are widely applied for longer-horizon forecasting (Salinas et al., [2020](#bib.bib71 "DeepAR: probabilistic forecasting with autoregressive recurrent networks")), while Transformer-based models have gained traction for capturing long-range dependencies (Lim et al., [2021](#bib.bib59 "Temporal Fusion Transformers for interpretable multi-horizon time series forecasting")). The appeal is the ability to capture nonlinear seasonality and abrupt level shifts without explicit structural specification; the limitation is sample requirements and limited interpretability. For coupled forecasting, the deeper concern is that flexible architectures can fit censored patterns during training without representing the censoring mechanism, making them vulnerable to the same regime-shift failures that affect simpler models (Section [4.5](#S4.SS5 "4.5 A simulation-based demonstration ‣ 4 The coupling problem")).

Alternative data and nowcasting. Search intensity proxies, web traffic, mobility signals, and transaction data now appear routinely as leading indicators (Sun et al., [2019](#bib.bib77 "Forecasting tourist arrivals with machine learning and internet search index"); Li et al., [2021](#bib.bib56 "Review of tourism forecasting research with internet data")). A representative recent design uses point-of-sale card transactions to forecast daily tourism demand while integrating search trends, holidays, and weather (Grau-Escolano et al., [2026](#bib.bib37 "Daily tourism demand forecasting via card transactions: a multi-source, interpretable, framework for diverse destinations and markets")). The value of alternative data is most apparent during structural breaks, when traditional econometric covariates often weaken in predictive power. From the coupling perspective, these demand-intent proxies are especially valuable because they measure DtD\_{t} before the supply ceiling censors it into BtB\_{t}; the gap between intent signals and realized bookings is itself a diagnostic for when coupling binds (Section [5](#S5 "5 Research agenda")).

Mixed-frequency modeling. Many fast signals arrive at daily or weekly frequency while core tourism targets remain monthly or quarterly. The MIDAS framework (Ghysels et al., [2004](#bib.bib35 "The MIDAS touch: mixed data sampling regression models")) and its deep-learning variants bridge this mismatch (Hu et al., [2025](#bib.bib40 "Tourism forecasting by mixed-frequency machine learning")). This is especially relevant for coupled forecasting, because supply-side signals are inherently high-frequency while demand targets are often reported at lower aggregation levels.

Bayesian and ensemble approaches. Bayesian structural time series (Brodersen et al., [2015](#bib.bib19 "Inferring causal impact using Bayesian structural time-series models")) and Bayesian global VAR models (Assaf et al., [2019](#bib.bib8 "Modeling and forecasting regional tourism demand using the Bayesian global vector autoregressive (BGVAR) model")) have been applied to tourism spillover analysis and arrival forecasting, with the latter demonstrating that cross-country demand linkages improve multi-step-ahead accuracy.

Competitions and crisis evaluation. The tourism forecasting competition tradition (Athanasopoulos et al., [2011](#bib.bib9 "The tourism forecasting competition")) provided large-scale benchmarks. During COVID-19, the competition format encouraged scenario thinking and explicit judgmental adjustments (Li et al., [2022](#bib.bib57 "Tourism forecasting competition in the time of COVID-19")). The pandemic exposed a fundamental vulnerability of purely extrapolative methods and accelerated interest in methods that can incorporate external information and expert judgment. The coupling perspective sharpens this lesson: COVID-19 was simultaneously a demand shock (travel restrictions), a supply shock (host exit, regulatory tightening), and a compositional shock (redistribution across origins, lead times, and listing types). Methods that model only the demand margin cannot distinguish these channels.

Despite the breadth and depth of this literature, a consistent feature of tourism demand forecasting that targets arrivals or bookings is that demand is modeled as a standalone object, largely abstracting from endogenous capacity constraints relative to the revenue-management tradition. The demand forecasting toolkit is sophisticated and continues to improve, but its problem formulation is unchanged from the hotel era: predict arrivals given economic fundamentals and perhaps some leading indicators. This formulation becomes a substantive limitation in platform accommodation, where the supply environment is endogenous to the demand being forecasted.

## 3 Platform accommodation markets and the supply-side gap

### 3.1 Two-sided foundations

A two-sided market is an economic environment in which an intermediary facilitates interactions between two distinct user groups and participation decisions are interdependent across groups (Rochet and Tirole, [2006](#bib.bib69 "Two-sided markets: a progress report")). The defining feature for forecasting is that platform decisions jointly shape both sides of the market. The demand-side participation level depends on expected supply-side participation and vice versa, so equilibrium quantities are determined by a fixed point rather than by independent supply and demand curves.

The modern definition emphasizes that two-sidedness is the empirical and theoretical relevance of the price structure: how charges are allocated across sides affects transaction volume, not only the overall price level (Rochet and Tirole, [2006](#bib.bib69 "Two-sided markets: a progress report")). In platform accommodation, coupling operates through both price instruments (commission splits, service fees, host-side pricing recommendations, subsidies) and non-price design choices (search ranking, cancellation policy, review systems, UX). The foundational models show that platforms face intertwined tasks of choosing an overall price level and how to split it across sides, with the profit-maximizing structure internalizing cross-group effects (Rochet and Tirole, [2003](#bib.bib68 "Platform competition in two-sided markets"); Armstrong, [2006](#bib.bib7 "Competition in two-sided markets"); Weyl, [2010](#bib.bib85 "A price theory of multi-sided platforms")).

The operational extension makes the coupling dynamic. Cachon et al. ([2017](#bib.bib20 "The role of surge pricing on a service platform with self-scheduling capacity")) show how state-dependent prices and wages improve capacity utilization in on-demand settings with self-scheduling providers. Bai et al. ([2019](#bib.bib12 "Coordinating supply and demand on an on-demand service platform with impatient customers")) incorporate endogenous supply and demand with waiting-time effects. Lian and van Ryzin ([2021](#bib.bib58 "Optimal growth in two-sided markets")) model platform growth as evolving stocks of supply and demand, with optimal policies involving front-loaded subsidies that deliberately shift the coupling.

### 3.2 Platform accommodation: pricing, supply dynamics, and regulation

The platform accommodation literature most relevant to coupled forecasting centers on pricing dynamics, supply dynamics, and regulatory intervention. On competitive impacts, Zervas et al. ([2017](#bib.bib88 "The rise of the sharing economy: estimating the impact of Airbnb on the hotel industry")) use difference-in-differences to estimate effects of Airbnb expansion on hotel performance. On pricing, heterogeneity by host type and professionalization means that host pricing rules are a behavioral channel coupling demand shocks into supply responses (Abrate and Viglia, [2022](#bib.bib3 "Dynamic pricing in Airbnb: individual vs professional hosts"); Casamatta et al., [2022](#bib.bib22 "Host type and pricing on Airbnb: seasonality and strategies")).

On supply dynamics, Fan et al. ([2023](#bib.bib32 "Exit and transition: exploring the survival status of Airbnb listings in a time of professionalization")) model exit and transition dynamics of Airbnb listings, showing that supply composition evolves through multiple event types. Farronato and Fradkin ([2022](#bib.bib33 "The welfare effects of peer entry: the case of Airbnb and the accommodation industry")) estimate a structural model of competition between peer hosts and hotels and show that welfare gains from peer entry concentrate where hotel capacity is constrained. Regulation has created a large quasi-experimental literature, with studies of city-specific restrictions showing measurable supply impacts and heterogeneous host responses (Koster et al., [2021](#bib.bib52 "Short-term rentals and the housing market: quasi-experimental evidence from Airbnb in Los Angeles"); Duso et al., [2024](#bib.bib29 "Airbnb and rental markets: evidence from Berlin"); Robertson et al., [2024](#bib.bib67 "Airbnb in the city: assessing short-term rental regulation in Bordeaux"); Bibler et al., [2025](#bib.bib16 "How do short-term rental regulations affect market outcomes? Evidence from San Francisco’s Airbnb registration requirement")).

### 3.3 The supply-side forecasting gap

The limited depth of rigorous supply-side forecasting is itself a key finding. Accommodation supply has been modeled in simultaneous equation systems for hotel markets (Qu et al., [2002](#bib.bib65 "A simultaneous equations model of the hotel room supply and demand in Hong Kong"); Tsai et al., [2006](#bib.bib80 "Examining the hotel room supply and demand in Las Vegas: a simultaneous equations model")), but these treat supply as endogenous to explanation, not as a forecast target with out-of-sample evaluation. In the short-term rental sector, Lee and Lin ([2023](#bib.bib55 "Market forecast for the sharing economy, using Airbnb in US cities and in Taipei as an example")) fit diffusion models to Airbnb listing data, one of the few studies that treats supply growth as an explicit forecasting object.

The measurement problem is equally important. Because platforms do not release granular activity data, studies rely on scraped calendars, listing snapshots, or proprietary vendors. Wang et al. ([2024](#bib.bib83 "Enhancing our understanding of short-term rental activity: a daily scrape-based approach for Airbnb listings")) demonstrate how daily calendar scrapes can be translated into interpretable activity measures. This measurement layer is directly connected to forecasting feasibility, because supply forecasting requires consistent, high-frequency state variables that the field has not yet standardized.

## 4 The coupling problem

The preceding sections document two facts. First, the demand forecasting literature is methodologically mature. Second, the supply side of accommodation markets remains thin as a forecasting target. This section argues that the separation of demand forecasting from supply forecasting is not merely an organizational gap. In platform-mediated accommodation markets, it produces forecasts that are fragile under policy changes, supply regime shifts, and platform intervention.

Using the notation from Section [1](#S1 "1 Introduction"), the core observation is that realized bookings are bounded: Bk,t≤min⁡(Dk,t,Sk,t)B\_{k,t}\leq\min(D\_{k,t},S\_{k,t}) (Equation [1](#S1.E1 "In Notation and forecasting targets ‣ 1 Introduction")), with derived matching efficiency mt≤1m\_{t}\leq 1. A model that forecasts BtB\_{t} without conditioning on StS\_{t} is fitting a constrained and friction-affected outcome without representing the constraint or the friction. Such a model may achieve adequate predictive performance during stable periods when the supply ceiling and matching efficiency are approximately constant. But it is not structurally adequate: it cannot answer counterfactual questions, it will fail when the supply regime shifts, and its parameters are not policy-invariant. The distinction between predictive adequacy (a model forecasts well in the current regime) and structural adequacy (a model remains valid under counterfactuals and regime change) is central to the argument that follows.

The coupling operates through three distinct mechanisms.

### 4.1 Behavioral coupling: policies propagate across sides

Two-sided market theory establishes that platforms optimally set prices and rules by internalizing cross-group externalities (Rochet and Tirole, [2003](#bib.bib68 "Platform competition in two-sided markets")). In practice, this means that policy changes nominally targeting one side inevitably affect the other. When a platform modifies cancellation rules, pricing recommendations, search ranking, or commission structures, the behavioral responses of both guests and hosts shift jointly, not independently.

Consider a well-documented example: the introduction of flexible cancellation or refund policies on short-term rental platforms. Jia et al. ([2021](#bib.bib41 "Platform as a rule-maker: evidence from Airbnb’s cancellation policies")) study Airbnb’s introduction of a 48-hour full-refund grace period and find that reservations increased, with effects decomposable into higher prices and higher occupancy. However, the same policy change propagates to the supply side. Lower commitment costs increase cancellation rates, altering the host experience. Hosts respond heterogeneously: professional operators absorb the volatility, while casual hosts, more sensitive to income variability, may reduce participation or exit.

The forecasting implication is direct. A demand model trained on pre-policy data will mis-forecast in the post-policy environment, not because demand fundamentals changed, but because the supply composition shifted in response to the same policy. Any platform intervention that alters incentives on one side will reshape participation and behavior on the other. Surge pricing creates feedback between demand signals and supply availability (Cachon et al., [2017](#bib.bib20 "The role of surge pricing on a service platform with self-scheduling capacity")). Changes to search ranking algorithms determine which listings are visible, effectively filtering the supply set. Behavioral coupling means that the marginal distribution of demand is not stable when supply-side conditions change, and vice versa. Critically, these platform interventions are chosen endogenously as functions of observed imbalance signals, not imposed exogenously; this endogeneity motivates the intervention-coupling problem below.

### 4.2 Informational coupling: the missing ceiling

The most fundamental form of coupling is mechanical: realized bookings cannot exceed available supply. Under the stylized benchmark, Bt=min⁡(Dt,St)B\_{t}=\min(D\_{t},S\_{t}). This ceiling is less problematic in traditional hotel markets, where room supply is physical, known, and approximately constant.

In platform accommodation markets, this ceiling is neither observable nor constant. The available inventory on any given night is the result of host-level decisions (listing activation, calendar availability, minimum-stay requirements) that aggregate into a time-varying, endogenous supply surface. Host pricing decisions do not change the inventory count StS\_{t} as defined here (a listing-night is either available or not), but they do affect which portion of StS\_{t} is demanded at prevailing prices; price is thus a covariate that modulates the demand-side conversion rate, not a component of the physical supply measure.

This creates a specific informational problem for demand forecasting. For accommodation-focused targets in markets and periods where inventory binds, the observed outcome is censored by available supply. The censoring structure is stock-out censoring (Tobin, [1958](#bib.bib92 "Estimation of relationships for limited dependent variables")): the analyst observes BtB\_{t} but not DtD\_{t} when Dt>StD\_{t}>S\_{t}, and the censoring threshold StS\_{t} is itself stochastic and endogenous. If the model does not include supply state variables, it is doing one of two things. Either it is implicitly assuming St→∞S\_{t}\to\infty, in which case it will over-forecast in supply-tight markets. Or it is fitting to historically observed BtB\_{t} values that were already constrained by the prevailing supply environment, in which case it has learned the shape of the censoring mechanism without representing it, and it will fail when the supply regime changes.

The informational problem is compounded by a measurement problem. The demand side benefits from decades of convergence on well-defined targets: tourist arrivals, overnight stays, expenditures. No equivalent consensus exists for platform supply. Some studies count listings (Zervas et al., [2017](#bib.bib88 "The rise of the sharing economy: estimating the impact of Airbnb on the hotel industry")), others measure spatial penetration (Quattrone et al., [2018](#bib.bib66 "Analyzing and predicting the spatial penetration of Airbnb in U.S. cities")), others estimate entry and exit flows (Fan et al., [2023](#bib.bib32 "Exit and transition: exploring the survival status of Airbnb listings in a time of professionalization"); Kolleck and Teubner, [2025](#bib.bib51 "How ratings shape the supply on sharing economy platforms: a longitudinal cohort study on listing survival on Airbnb")). The relevant supply forecast target is distributional: a characterization of available inventory by host type, location, price tier, and temporal availability pattern. Compositional time series methods (Aitchison, [1986](#bib.bib5 "The statistical analysis of compositional data"); Katz et al., [2024](#bib.bib44 "A Bayesian Dirichlet auto-regressive moving average model for forecasting lead times")) are designed for this class of target, but the forecasting literature has not yet framed the supply problem in compositional terms.

### 4.3 Intervention coupling: endogenous regime change

The third form of coupling arises because platforms and regulators intervene in accommodation markets, and these interventions are endogenous responses to observed supply-demand conditions that alter the structural relationship between the two sides.

External regulation provides the most visible examples. City-level short-term rental regulations affect supply directly by constraining the feasible listing set (Koster et al., [2021](#bib.bib52 "Short-term rentals and the housing market: quasi-experimental evidence from Airbnb in Los Angeles"); Duso et al., [2024](#bib.bib29 "Airbnb and rental markets: evidence from Berlin"); Robertson et al., [2024](#bib.bib67 "Airbnb in the city: assessing short-term rental regulation in Bordeaux"); Bibler et al., [2025](#bib.bib16 "How do short-term rental regulations affect market outcomes? Evidence from San Francisco’s Airbnb registration requirement")). From a forecasting perspective, the critical observation is that the post-regulation relationship between supply and demand differs from the pre-regulation relationship. A demand model trained on pre-regulation data is not merely out-of-date; it is estimating parameters that describe a relationship that no longer holds.

Platform design changes constitute a second, less observable class of intervention. Platform mechanisms such as search ranking, pricing recommendations, matching algorithms, and commission structures are periodically updated in response to observed market conditions. This creates a form of policy endogeneity familiar from the macroeconomics literature (Lucas, [1976](#bib.bib60 "Econometric policy evaluation: a critique")): the historical relationship between supply and demand partly reflects past platform decisions, and those decisions are themselves functions of market state variables.

External shocks introduce a third variant. Pandemics, natural disasters, and exchange rate movements do not affect supply and demand symmetrically. They redistribute: some origin markets collapse while others grow; some listing types exit while others enter; lead-time distributions compress or stretch (Katz et al., [2025](#bib.bib48 "Lead times in flux: analyzing Airbnb booking dynamics during global upheavals (2018–2022)")). These are compositional changes: changes in shape, not merely level. Standard structural break tools that detect level shifts in scalar time series miss the directionality and dimensionality of the disruption. Katz ([2026](#bib.bib43 "Directional-shift Dirichlet ARMA models for compositional time series with structural break intervention")) proposes a Bayesian Dirichlet ARMA model with a directional-shift intervention mechanism for this class of problem.

For analytical clarity, it is useful to distinguish three types of structural breaks in coupled systems: (i) demand shocks that shift DtD\_{t} while leaving StS\_{t} initially unchanged; (ii) supply shocks that shift StS\_{t} while leaving DtD\_{t} initially unchanged; and (iii) platform intervention shocks that simultaneously alter the coupling relationship between DtD\_{t} and StS\_{t}. Standard break detection methods are best suited to type (i) and (ii) breaks. Type (iii) breaks, which manifest as changes in coupling parameters rather than in either marginal series, require multivariate extensions discussed in the research agenda.

### 4.4 Synthesis

Behavioral, informational, and intervention coupling are distinct mechanisms, but they compound. A platform introduces a policy change (behavioral coupling) that alters supply composition. The demand model does not observe the new supply ceiling (informational coupling). The platform detects the resulting imbalance and intervenes again (intervention coupling), further altering the relationship. The feedback is recursive.

I argue that in platform accommodation markets with elastic, decision-driven supply and frequent interventions, methods which treat supply as exogenous or absent face a structural limitation. The omitted variable (StS\_{t}) is correlated with demand drivers, and the resulting parameter estimates are biased for causal and counterfactual purposes. For short-horizon extrapolation in stable supply environments, the bias may be small and decoupled forecasts may perform adequately. But for any task that requires policy invariance, counterfactual reasoning, or robustness to supply regime shifts, the limitation is fundamental.

Table [1](#S4.T1 "Table 1 ‣ 4.4 Synthesis ‣ 4 The coupling problem") summarizes the three coupling layers, their observable proxies, the failure modes they create for decoupled forecasters, and the corresponding research directions proposed in Section [5](#S5 "5 Research agenda").

Table 1: Coupling framework: layers, diagnostics, failure modes, and research directions.

| Coupling layer | Observable proxies | Failure mode (decoupled model) | Research direction |
| --- | --- | --- | --- |
| Behavioral (Sec. [4.1](#S4.SS1 "4.1 Behavioral coupling: policies propagate across sides ‣ 4 The coupling problem")) | Host exit/entry rates; pricing rule changes; cancellation policy shifts | Parameters trained pre-policy are invalid post-policy; cross-side propagation missed | Elasticity asymmetry diagnostic (§[5](#S5 "5 Research agenda")) |
| Informational (Sec. [4.2](#S4.SS2 "4.2 Informational coupling: the missing ceiling ‣ 4 The coupling problem")) | Search-to-booking gap; occupancy rates; calendar availability | Systematic over-prediction when supply binds; censoring unrepresented | Moving ceiling; search-to-booking gap; variance decomposition (§[5](#S5 "5 Research agenda")) |
| Intervention (Sec. [4.3](#S4.SS3 "4.3 Intervention coupling: endogenous regime change ‣ 4 The coupling problem")) | Regulation dates; platform A/B tests; commission changes | Regime-specific parameters applied across regimes; Lucas critique | Causal forecasting under unobservable intervention (§[5](#S5 "5 Research agenda")) |

### 4.5 A simulation-based demonstration

The following toy model illustrates the core failure mode. A market is observed over T=200T=200 periods with endogenous supply that responds to lagged demand. Realized bookings are Bt=min⁡(Dt,St)B\_{t}=\min(D\_{t},S\_{t}). In the first 150 periods, supply is sufficiently high that the constraint rarely binds. At t=151t=151, a regulation shock permanently reduces the supply intercept, simulating a registration requirement that removes casual hosts. Full model specification is given in the Supplementary Material.

A demand-only forecaster fits an AR(1) to {B1,…,B150}\{B\_{1},\ldots,B\_{150}\} and extrapolates forward. Because the supply constraint rarely bound during training, the fitted model approximates the uncensored demand process. After the supply shock, the demand-only forecast continues to predict Bt≈50B\_{t}\approx 50, while realized bookings drop to Bt≈35B\_{t}\approx 35–4040 because supply now binds. A coupled forecaster that conditions on StS\_{t} detects the supply shift and adjusts.

![Refer to caption](2603.00422v1/x1.png)


Figure 1: Simulation-based demonstration. (a) A single run: latent demand DtD\_{t}, inventory StS\_{t}, realized bookings BtB\_{t}, and the two forecast models over the test period. The supply intercept drops at t=151t=151. (b) Post-shock forecast errors. The demand-only model exhibits a persistent positive bias; the coupled model tracks the new ceiling.




Table 2: Simulation results: demand-only vs. coupled forecaster (500 Monte Carlo replications).

|  | Pre-shock (t=131t=131–150150) | | Post-shock (t=151t=151–200200) | |
| --- | --- | --- | --- | --- |
| Model | RMSE | Mean bias | RMSE | Mean bias |
| Demand-only AR(1) | 5.1 | −0.3-0.3 | 13.4 | +11.8+11.8 |
| Coupled min⁡(D^t,S^t)\min(\hat{D}\_{t},\hat{S}\_{t}) | 5.2 | −0.2-0.2 | 5.4 | +0.4+0.4 |

Table [2](#S4.T2 "Table 2 ‣ 4.5 A simulation-based demonstration ‣ 4 The coupling problem") summarizes results across 500 Monte Carlo replications. The coupled model reduces post-shock RMSE by approximately 60% and eliminates the systematic positive bias, while matching pre-shock accuracy. Two features merit emphasis. First, the demand-only model was accurate during the training regime; the problem is not poor model fitting but fitted parameters that describe a relationship that no longer holds. Second, the failure is undetectable by standard residual diagnostics during training and manifests only out of sample when conditions change. This is the operational content of the distinction between predictive and structural adequacy.

## 5 Research agenda

The coupling problem implies that forecasting in platform accommodation markets requires methods that jointly model supply and demand, respect endogenous constraints, and remain valid under intervention. While individual building blocks exist in adjacent literatures (revenue management, structural IO, marketplace design), they have not been assembled into an integrated forecasting framework for platform accommodation. Before presenting the open problems, it is useful to map the relevant methodological traditions and their connections to the coupling layers identified above. A more detailed technical survey is provided in the Supplementary Material.

### 5.1 Methodological landscape

Four bodies of work bear directly on the coupling problem, each addressing a different facet.

Tourism demand forecasting provides the baseline toolkit: econometric models, exponential smoothing, machine learning, and forecast combination (Song et al., [2019](#bib.bib76 "A review of research on tourism demand forecasting"); Song and Li, [2008](#bib.bib75 "Tourism demand modelling and forecasting—a review of recent research")). This literature excels at modeling demand as a standalone time series and has converged on rigorous evaluation protocols. Its limitation, from the coupling perspective, is that supply enters either as a fixed background condition or not at all. When the supply ceiling is approximately constant, this omission is benign; when it shifts, the toolkit produces forecasts that are predictively adequate in-sample but structurally fragile out-of-sample (Section [4.5](#S4.SS5 "4.5 A simulation-based demonstration ‣ 4 The coupling problem")).

Revenue management and unconstrained demand estimation addresses a closely related problem: recovering latent demand from sales data censored by finite capacity (Talluri and van Ryzin, [2004](#bib.bib78 "The theory and practice of revenue management")). EM algorithms, booking-curve detruncation, and Bayesian data augmentation are well-developed for hotel settings where the capacity constraint is scalar and observable. The key assumption that breaks in platform markets is that the censoring threshold is fixed and known. When inventory is decision-driven and stochastic, these methods require extension to endogenous, high-dimensional supply surfaces (see Supplementary Material, Section [S3](#A3 "Appendix S3 Methodological building blocks")).

Two-sided market economics explains why the coupling exists. Foundational models (Rochet and Tirole, [2003](#bib.bib68 "Platform competition in two-sided markets"); Armstrong, [2006](#bib.bib7 "Competition in two-sided markets"); Weyl, [2010](#bib.bib85 "A price theory of multi-sided platforms")) show that equilibrium quantities in platform markets are determined by a fixed point across sides, not by independent supply and demand schedules. Operational extensions model dynamic capacity utilization (Cachon et al., [2017](#bib.bib20 "The role of surge pricing on a service platform with self-scheduling capacity")), endogenous entry with waiting-time effects (Bai et al., [2019](#bib.bib12 "Coordinating supply and demand on an on-demand service platform with impatient customers")), and growth-stage subsidies that deliberately shift the coupling (Lian and van Ryzin, [2021](#bib.bib58 "Optimal growth in two-sided markets")). These models are structural and explanatory; they have not been operationalized as forecasting systems, but they provide the economic logic that a coupled forecasting framework must encode.

Causal and intervention inference supplies the tools for evaluating what happens when coupling relationships change. Bayesian structural time series (Brodersen et al., [2015](#bib.bib19 "Inferring causal impact using Bayesian structural time-series models")), synthetic control (Abadie et al., [2010](#bib.bib1 "Synthetic control methods for comparative case studies: estimating the effect of California’s tobacco control program"), [2015](#bib.bib2 "Comparative politics and the synthetic control method")), and difference-in-differences designs are standard for retrospective policy evaluation. The deeper connection is to the Lucas critique (Lucas, [1976](#bib.bib60 "Econometric policy evaluation: a critique")): parameters estimated under one policy regime are not invariant to policy change, which is precisely what intervention coupling creates. Extending these tools from retrospective evaluation to prospective forecasting under unobserved intervention is the hardest open problem identified below.

Compositional time series methods round out the toolkit. Many platform forecasting targets are compositional: supply shares by host type, demand shares by origin market, lead-time allocations across booking horizons (Aitchison, [1986](#bib.bib5 "The statistical analysis of compositional data"); Katz et al., [2024](#bib.bib44 "A Bayesian Dirichlet auto-regressive moving average model for forecasting lead times")). The coupling argument established that shocks redistribute mass across components rather than simply shifting a scalar level. Methods that respect simplex constraints, model time-varying volatility, and detect directional structural breaks on the simplex are necessary building blocks for representing the redistributive channel through which coupling operates.

Each tradition solves part of the problem. Tourism forecasting models demand well but ignores the supply constraint. Revenue management handles the constraint but assumes it is fixed. Two-sided economics explains the coupling but does not forecast. Causal inference evaluates past interventions but does not project forward. Compositional methods represent distributional targets but have not been integrated with supply-demand coupling. The remainder of this section identifies five open problems whose resolution would connect these building blocks into an integrated framework. The problems are ordered from the most immediately actionable to the most methodologically challenging.

### 5.2 The search-to-booking gap as a supply constraint signal

In accommodation platforms, guests search before they book, and the temporal profile of search activity differs from that of booking activity. The search-to-booking gap is defined here as the divergence between demand intent proxies (searches, listing views, wishlists) and realized bookings, measured at the distributional level across lead times, locations, or price segments. This gap is informative about the difference between latent demand DtD\_{t} and realized bookings BtB\_{t}: when the gap widens, it signals that supply constraints, matching frictions, or price misalignment are preventing demand intent from converting to transactions. This signal has not been formalized as a forecasting input. Search volume data are used as leading indicators of aggregate arrivals (Sun et al., [2019](#bib.bib77 "Forecasting tourist arrivals with machine learning and internet search index"); Li et al., [2021](#bib.bib56 "Review of tourism forecasting research with internet data")), but the informational content of the conversion margin is discarded. The gap can be quantified using compositional distance measures on paired lead-time distributions; see the Supplementary Material for technical details.

### 5.3 Demand forecasting under an endogenous supply ceiling

Section [4.2](#S4.SS2 "4.2 Informational coupling: the missing ceiling ‣ 4 The coupling problem") established that realized demand is bounded by available supply and that this ceiling is time-varying and endogenous. The open problem is to build a demand forecasting framework that explicitly incorporates this constraint.

This has precedent. In labor economics, Barnichon and Nekarda ([2012](#bib.bib14 "The ins and outs of forecasting unemployment")) forecast the unemployment rate by modeling the flows that govern the stock. The simultaneous equation tradition (Haavelmo, [1943](#bib.bib39 "The statistical implications of a system of simultaneous equations"); Zellner and Theil, [1962](#bib.bib87 "Three-stage least squares: simultaneous estimation of simultaneous equations")) provides identification strategies for jointly determined systems. A promising direction is a two-equation system where the demand equation conditions on a latent supply state and the supply equation conditions on a demand signal, with the constraint that realized bookings are bounded by both.

The central identification challenge is that DtD\_{t} and StS\_{t} are not separately identified from Bt≤min⁡(Dt,St)B\_{t}\leq\min(D\_{t},S\_{t}) without instruments or structural assumptions. Candidate instrument classes include: (i) regulation shocks that constrain supply; (ii) host-side fee or commission changes; (iii) weather or events in origin markets that shift demand; and (iv) timing assumptions exploiting the fact that supply decisions precede demand realization for a given stay date. Each class requires exclusion restrictions that are plausibly violated on platforms. The honest assessment is that clean instruments are rare in this setting, and research designs should state exclusion restrictions explicitly, propose falsification tests, and consider partial identification bounds (Athey and Imbens, [2017](#bib.bib10 "The state of applied econometrics: causality and policy evaluation")).

### 5.4 Decomposing demand variance into exogenous and endogenous components

In a coupled system with fast feedback, observed demand variance has two components: genuine exogenous uncertainty and endogenous oscillation from coupling. A testable formulation fits a demand-only model and measures residual variance, then fits a coupled model with supply state variables and measures the reduction. If the reduction is economically meaningful, coupling is a quantitatively important source of recoverable forecast error. The connection to existing methodology is through time-varying volatility models (Katz and Weiss, [2025](#bib.bib49 "A Bayesian Dirichlet auto-regressive conditional heteroskedasticity model for forecasting currency shares")). The open question is whether volatility clusters are partly endogenous to supply-demand feedback.

### 5.5 Price elasticity asymmetry as a coupling diagnostic

Not all markets are equally coupled. When supply and demand respond to price signals with comparable elasticity, the system equilibrates quickly and independent forecasts may suffice. When one side is substantially more elastic, persistent imbalances arise and coupling effects are strongest. A research design would estimate time-varying supply and demand elasticities for a panel of platform markets, construct an asymmetry index, and test whether periods of high asymmetry correspond to periods of poor relative performance of independent forecasts via Diebold and Mariano ([1995](#bib.bib27 "Comparing predictive accuracy")) tests.

### 5.6 Causal forecasting under unobservable platform intervention

The most challenging problem is also the most consequential. Section [4.3](#S4.SS3 "4.3 Intervention coupling: endogenous regime change ‣ 4 The coupling problem") argued that platforms intervene endogenously. Standard causal tools (difference-in-differences, synthetic control (Abadie et al., [2010](#bib.bib1 "Synthetic control methods for comparative case studies: estimating the effect of California’s tobacco control program"), [2015](#bib.bib2 "Comparative politics and the synthetic control method")), Bayesian structural time series (Brodersen et al., [2015](#bib.bib19 "Inferring causal impact using Bayesian structural time-series models"))) require knowing when the intervention occurred. Structural break detection (Bai and Perron, [2003](#bib.bib11 "Computation and analysis of multiple structural change models"); Killick et al., [2012](#bib.bib50 "Optimal detection of changepoints with a linear computational cost")) can identify when the process changed but cannot distinguish exogenous shocks from endogenous platform responses.

Two directions are promising. First, break detection methods operating on the coupling relationship itself, parameterized through time-varying elasticities or the correlation structure of residuals, rather than individual series. Bayesian change-point methods (Fearnhead, [2006](#bib.bib34 "Exact and efficient Bayesian inference for multiple changepoint problems"); Adams and MacKay, [2007](#bib.bib4 "Bayesian online changepoint detection")) provide the inferential machinery but require extension to multivariate, coupled settings with compositional constraints. Second, forecasting methods explicitly robust to unobserved intervention: bounding forecast uncertainty to account for possible coupling changes, related to conformal prediction (Romano et al., [2019](#bib.bib70 "Conformalized quantile regression"); Barber et al., [2021](#bib.bib13 "Predictive inference with the jackknife+")) but under the non-stationarity that endogenous intervention creates.

### 5.7 Summary and prioritization

The five problems are not independent. The search-to-booking gap provides a measurable mismatch signal. The moving ceiling formalizes this mismatch as a constraint. The variance decomposition quantifies the coupling mechanism’s contribution to forecast error. The elasticity diagnostic identifies when coupling is strongest. Causal forecasting under unobservable intervention addresses the deepest methodological obstacle.

A researcher entering this agenda would do well to begin with the supply measurement problem that underlies several formulations. Without canonical supply state variables that can be measured consistently across markets, the ceiling cannot be estimated, the variance cannot be decomposed, and the coupling cannot be parameterized. The payoff is substantial. Methods developed for platform accommodation will generalize to other platform markets (ride-sharing, labor platforms, e-commerce marketplaces) where similar coupling dynamics are present but less well documented.

### 5.8 A minimal empirical design

To make the agenda concrete, this subsection sketches a feasible empirical test of the coupling hypothesis. The design requires one city with a well-documented supply shock, one intent proxy, and a standard forecasting evaluation.

Setting. A city that introduced a short-term rental registration requirement with a known effective date. Candidate cities include San Francisco, Barcelona, and Amsterdam, all of which have documented regulation events in the literature (Bibler et al., [2025](#bib.bib16 "How do short-term rental regulations affect market outcomes? Evidence from San Francisco’s Airbnb registration requirement"); Duso et al., [2024](#bib.bib29 "Airbnb and rental markets: evidence from Berlin"); Overwater and Yorke-Smith, [2022](#bib.bib82 "Agent-based simulation of short-term peer-to-peer rentals: evidence from the Amsterdam housing market")).

Supply construction. StS\_{t} is constructed from daily calendar scrapes as the count of available listing-nights for a 30-day forward stay-date window, following the transparent scrape-based pipeline of Wang et al. ([2024](#bib.bib83 "Enhancing our understanding of short-term rental activity: a daily scrape-based approach for Airbnb listings")).

Evaluation. Two forecasting models are compared out of sample over the post-regulation period: (i) a demand-only AR model trained on pre-regulation BtB\_{t}, and (ii) a coupled model that forecasts B^t=min⁡(D^t,S^t)\hat{B}\_{t}=\min(\hat{D}\_{t},\hat{S}\_{t}), where S^t\hat{S}\_{t} is a simple inventory nowcast. Accuracy is compared via Diebold and Mariano ([1995](#bib.bib27 "Comparing predictive accuracy")) tests on MAE. If the coupled model significantly outperforms after the supply shock but not before, this constitutes evidence that coupling matters when regimes change, consistent with the simulation in Section [4.5](#S4.SS5 "4.5 A simulation-based demonstration ‣ 4 The coupling problem").

Data access. The supply-side construction and evaluation can be replicated with publicly available calendar data from Inside Airbnb (Inside Airbnb, [2024](#bib.bib93 "Inside Airbnb: adding data to the debate")). A scalar search-to-booking ratio can be constructed from Google Trends (Google, [2024](#bib.bib94 "Google Trends")). The full lead-time compositional gap requires platform-internal search logs. If proprietary platform data are available, the same design can be executed with exact booking counts, lead-time-tagged searches, and richer inventory signals; the public-scrape version establishes a replicable baseline.

## 6 Implications for destination management and tourism policy

The coupling framework has direct implications for practitioners who rely on accommodation forecasts for planning and resource allocation.

Destination managers and tourism boards. Organizations that forecast visitor volumes to plan infrastructure, staffing, and marketing should recognize that booking data from platform sources reflect supply conditions as much as demand conditions. A city that observes declining Airbnb bookings after introducing a registration requirement is not necessarily experiencing reduced tourism demand; it may be observing the mechanical effect of a supply contraction on a censored outcome. Conflating the two leads to misallocated marketing budgets and incorrect assessments of destination competitiveness. The search-to-booking gap (Section [5.2](#S5.SS2 "5.2 The search-to-booking gap as a supply constraint signal ‣ 5 Research agenda")) offers a practical diagnostic: if search intent remains stable while bookings decline, the binding constraint is supply, not demand.

Regulatory impact assessment. Cities considering short-term rental regulations should anticipate that supply-side interventions propagate to the demand side through behavioral coupling. A registration rule that removes casual hosts does not simply reduce supply by the number of removed listings; it alters the composition of remaining supply (skewing toward professional operators), shifts the price distribution, and changes the demand-side experience. Pre-regulation booking forecasts are unreliable guides to post-regulation outcomes precisely because the coupling relationship has changed. Regulatory impact assessments that use pre-regulation demand trends to project post-regulation bookings will systematically overestimate lost tourism revenue if they do not account for supply-side adjustment.

Platform operators. Forecasting systems that support earnings guidance, treasury operations, and capacity planning are vulnerable to the same coupling failures described here. When platforms modify pricing algorithms, commission structures, or cancellation policies, demand forecasts trained on pre-change data will mis-predict in the post-change environment. Operationally, this means that forecast models should include supply state variables as inputs and that forecast accuracy should be monitored conditional on recent platform interventions, not just unconditionally.

## 7 Conclusion

The central argument of this paper is that in platform-mediated accommodation markets with elastic supply and frequent intervention, supply and demand cannot be forecasted independently when the goal is policy-invariant, counterfactual-capable, or structurally robust prediction. The capacity ceiling is time-varying and endogenous to demand. Platform interventions alter the structural relationship between the two sides. Behavioral responses to policy changes propagate across sides through cross-group externalities. Decoupled forecasts may perform adequately for short-horizon extrapolation in stable environments, but they are fragile precisely when forecasts matter most: under policy changes, supply regime shifts, and platform intervention.

The tourism demand forecasting literature has produced a mature and sophisticated toolkit for predicting arrivals, spending, and stays. This toolkit was developed for a world in which supply was effectively fixed and the censoring mechanism was approximately constant. In platform accommodation, the censoring threshold itself is elastic, decision-driven, and coupled to demand by design. I argue that the methods work; the problem formulation needs updating.

The research agenda outlined in Section [5](#S5 "5 Research agenda") offers a path forward. Its core is a conceptual reframing: from forecasting demand given fixed capacity to jointly modeling a coupled system in which both sides co-evolve under endogenous intervention. The methodological building blocks exist but have not been assembled for this purpose. The five open problems identified here constitute the work plan for that assembly.

While this paper focuses on platform accommodation, the coupling problem generalizes. Ride-sharing platforms face analogous supply-demand feedback through surge pricing and driver repositioning. Labor platforms mediate elastic, decision-driven supply with endogenous matching interventions. E-commerce marketplaces manage seller entry, inventory visibility, and algorithmic ranking that jointly shape both sides of the transaction. In each setting, forecasting one side without the other produces structurally fragile predictions. The accommodation market is a natural starting point because the data infrastructure, regulatory variation, and academic literature are most developed, but the methods proposed here are designed for the broader class of coupled platform markets.

Supplementary Material

This supplement provides technical details supporting the main text. Appendix [S1](#A1 "Appendix S1 Measurement and data sources") describes data measurement issues. Appendix [S2](#A2 "Appendix S2 Simulation specification") gives the full simulation specification. Appendix [S3](#A3 "Appendix S3 Methodological building blocks") surveys the methodological building blocks for coupled forecasting. Appendix [S4](#A4 "Appendix S4 Search-to-booking distance metrics") formalizes the search-to-booking distance metrics.

## Appendix S1 Measurement and data sources

Inventory StS\_{t} is typically constructed from calendar scrapes or platform dashboards. The primary measurement problems are: (i) distinguishing blocked dates (host-side unavailability) from booked dates (guest-side demand), since both appear as “not available” in a calendar scrape; (ii) handling minimum-stay rules, which make individual nights conditionally available depending on booking length; (iii) accounting for multi-night bookings, which occupy consecutive listing-nights but represent a single demand event; and (iv) sampling bias, since scrape frequency and coverage vary across vendors, and inactive or stealth listings inflate raw counts (Wang et al., [2024](#bib.bib83 "Enhancing our understanding of short-term rental activity: a daily scrape-based approach for Airbnb listings")). The conceptual object StS\_{t} is defined as inventory available at any posted price; PtP\_{t} and RtR\_{t} then filter which portion of that inventory is exposed to demand under specific search conditions.

Demand intent proxies (searches, listing views, wishlists) are available on platform dashboards but generally not in public data. Credit-card aggregates and Google Trends provide partial substitutes at coarser granularity (Grau-Escolano et al., [2026](#bib.bib37 "Daily tourism demand forecasting via card transactions: a multi-source, interpretable, framework for diverse destinations and markets"); Sun et al., [2019](#bib.bib77 "Forecasting tourist arrivals with machine learning and internet search index")). The gap between these proxies and the conceptual DtD\_{t} is itself informative (see the research agenda in the main text).

For external researchers, an honest assessment of data availability is: StS\_{t} can be constructed from calendar scrapes, but with measurement error from the blocked-versus-booked ambiguity; BtB\_{t} can be approximated from occupancy changes, but not perfectly; DtD\_{t} is latent even with platform-internal data, because search intent is not equivalent to booking intent. PtP\_{t} and RtR\_{t} are partially observable from listing pages but may not reflect the prices or rankings actually displayed to searchers. This measurement gap is itself a research problem (see the main text).

## Appendix S2 Simulation specification

The simulation in Section 4 of the main text uses the following data-generating process. Latent demand follows an AR(1) process: Dt=50+0.7​(Dt−1−50)+εtDD\_{t}=50+0.7(D\_{t-1}-50)+\varepsilon^{D}\_{t}, with εtD∼N​(0,52)\varepsilon^{D}\_{t}\sim N(0,5^{2}). Supply is endogenous and responds to lagged demand with noise: St=40+0.3​Dt−1+εtSS\_{t}=40+0.3D\_{t-1}+\varepsilon^{S}\_{t}, with εtS∼N​(0,32)\varepsilon^{S}\_{t}\sim N(0,3^{2}). Realized bookings are Bt=min⁡(Dt,St)B\_{t}=\min(D\_{t},S\_{t}). In the first 150 periods (training), supply is sufficiently high that the constraint rarely binds. At t=151t=151, a regulation shock permanently reduces the supply intercept from 40 to 25, simulating a registration requirement that removes a portion of casual hosts.

The two forecasters are defined as follows.

Demand-only: fit an AR(1) to {B1,…,B150}\{B\_{1},\ldots,B\_{150}\} and produce one-step-ahead forecasts B^t=μ^+ϕ^​(Bt−1−μ^)\hat{B}\_{t}=\hat{\mu}+\hat{\phi}(B\_{t-1}-\hat{\mu}).

Coupled: fit an AR(1) to {B1,…,B150}\{B\_{1},\ldots,B\_{150}\} for a latent demand proxy D^t\hat{D}\_{t}, and separately fit a regression St=α+β​Dt−1+ηtS\_{t}=\alpha+\beta D\_{t-1}+\eta\_{t} to the observable supply series; then forecast B^t=min⁡(D^t,S^t)\hat{B}\_{t}=\min(\hat{D}\_{t},\hat{S}\_{t}). In the simulation, both StS\_{t} and BtB\_{t} are observed; in practice, StS\_{t} would be a noisy proxy from calendar scrapes.

Results are reported in Table 1 of the main text (500 Monte Carlo replications). The demand-only model achieves pre-shock RMSE of 5.1 and post-shock RMSE of 13.4 with mean bias +11.8+11.8. The coupled model achieves pre-shock RMSE of 5.2 and post-shock RMSE of 5.4 with mean bias +0.4+0.4, a roughly 60% reduction in post-shock RMSE with elimination of the systematic positive bias.

## Appendix S3 Methodological building blocks

This appendix surveys the methods most relevant to constructing a coupled forecasting framework. The building blocks span five areas: compositional and constrained forecasting, unconstrained demand estimation and censoring, causal inference under intervention, regime-change detection, and uncertainty quantification. None of these was developed specifically for the platform accommodation problem, but together they constitute the toolkit from which a coupled forecasting framework can be assembled.

### S3.1 Compositional and constrained forecasting

Many quantities relevant to coupled forecasting are compositional: market shares by guest origin, supply shares by host type, lead-time allocations across booking horizons, and currency-mix shares all must sum to one and lie on the simplex. The simplex constraint implies that raw shares are negatively correlated by construction (an increase in one component mechanically decreases others), which motivates log-ratio transformations that map compositions to unconstrained Euclidean space. Standard time series methods that ignore these constraints can produce incoherent forecasts: predicted shares that exceed unity or take negative values (Aitchison, [1986](#bib.bib5 "The statistical analysis of compositional data"); Pawlowsky-Glahn et al., [2015](#bib.bib63 "Modeling and analysis of compositional data")).

Two core modeling strategies have emerged. The first is transform-based: apply a log-ratio transformation (additive, centered, or isometric) to map the simplex to unconstrained Euclidean space (Egozcue et al., [2003](#bib.bib30 "Isometric logratio transformations for compositional data analysis")), then fit standard multivariate models. Early work by Brunsdon and Smith ([1998](#bib.bib98 "The time series analysis of compositional data")) demonstrated the viability of ARIMA modeling on log-ratio-transformed compositions, and Kynčlová et al. ([2015](#bib.bib53 "Modeling compositional time series with vector autoregressive models")) extended this to VAR models for multivariate compositional series. Barceló-Vidal et al. ([2011](#bib.bib97 "Compositional VARIMA time series")) develop compositional VARIMA models within the Aitchison geometry, providing a general autoregressive-moving-average framework on the simplex. Snyder et al. ([2017](#bib.bib73 "Forecasting compositional time series: a state space approach")) develop a state-space formulation for compositional time series using the log-ratio approach, and Mills ([2010](#bib.bib103 "Forecasting compositional time series")) provides a practical overview of forecasting methods for compositional data. Transform-based methods benefit from the full arsenal of Euclidean time series tools, but they can obscure interpretability and may perform poorly when shares approach zero (Coenders and Ferrer-Rosell, [2020](#bib.bib25 "Compositional data analysis in tourism: review and future directions")). The zero problem is non-trivial in practice; Martín-Fernández et al. ([2012](#bib.bib101 "Model-based replacement of rounded zeros in compositional data: classical and robust approaches")) develop model-based replacement strategies for rounded zeros, and Martín-Fernández et al. ([2015](#bib.bib102 "Bayesian-multiplicative treatment of count zeros in compositional data sets")) propose Bayesian-multiplicative treatments for count zeros in compositional data.

The second strategy models compositions directly on the simplex. The Bayesian tradition is particularly well developed. Quintana and West ([1988](#bib.bib104 "Time series analysis of compositional data")) introduce dynamic linear models for compositional time series using a logistic-normal formulation, and Cargnoni et al. ([1997](#bib.bib99 "Bayesian forecasting of multinomial time series through conditionally Gaussian dynamic models")) extend this to multinomial forecasting through conditionally Gaussian dynamic models, demonstrating posterior inference for market-share evolution. Grunwald et al. ([1993](#bib.bib38 "Time series of continuous proportions")) propose Bayesian state-space models for continuous proportions using the Dirichlet distribution, and Zheng and Chen ([2017](#bib.bib90 "Dirichlet ARMA models for compositional time series")) develop frequentist Dirichlet ARMA models. The logistic-normal distribution (Aitchison, [1986](#bib.bib5 "The statistical analysis of compositional data"); Aitchison and Shen, [1980](#bib.bib96 "Logistic-normal distributions: some properties and uses")) accommodates richer covariance structures on the simplex, at the cost of a less tractable normalizing constant. Dynamic multinomial logit models treat compositional observations as arising from category-level utility processes with time-varying parameters, connecting naturally to discrete-choice demand models in the Berry et al. ([1995](#bib.bib17 "Automobile prices in market equilibrium")) tradition. Ravishanker et al. ([2001](#bib.bib105 "Compositional time series analysis of mortality proportions")) apply compositional time series methods to mortality proportions, illustrating the broader applicability of these techniques to demographic and social science data. For count-based compositions, Dirichlet-multinomial models provide overdispersed multinomial inference with conjugate updating (Pawlowsky-Glahn et al., [2015](#bib.bib63 "Modeling and analysis of compositional data")). A practical concern in applied settings is whether to model shares alone or jointly with their totals; Coenders et al. ([2017](#bib.bib100 "When relative and absolute information matter: compositional predictor with a total in generalized linear models")) address this by incorporating a compositional predictor with a total in generalized linear models. Each distributional family involves different tradeoffs: Dirichlet models enforce simplex constraints automatically but impose limited covariance flexibility; logistic-normal models offer richer dependence but lose conjugacy; transform-based approaches are computationally convenient but can behave poorly at the simplex boundary.

Within the Dirichlet family, Bayesian Dirichlet ARMA (BDARMA) models combine the Dirichlet likelihood with VARMA dynamics on the mean parameters after an additive log-ratio transformation (Katz et al., [2024](#bib.bib44 "A Bayesian Dirichlet auto-regressive moving average model for forecasting lead times")). Extensions address time-varying volatility through a Dirichlet ARCH component (Katz and Weiss, [2025](#bib.bib49 "A Bayesian Dirichlet auto-regressive conditional heteroskedasticity model for forecasting currency shares")), structural breaks via a directional-shift intervention mechanism (Katz, [2026](#bib.bib43 "Directional-shift Dirichlet ARMA models for compositional time series with structural break intervention")), and density forecast calibration through a centered-innovation formulation (Katz, [2025](#bib.bib42 "Centered-innovation MA for Dirichlet ARMA in compositional time-series forecasting")). Software implementation is available in the darma R package (Katz and Wilson, [2024](#bib.bib95 "Darma: Bayesian Dirichlet ARMA models for compositional time series")).

For coupled forecasting, compositional modeling is often necessary for coherence and interpretability because the supply forecast target is itself distributional. The composition of available inventory by host type, price tier, or location is a simplex-valued object that evolves over time. The coupling argument established that supply constraints and platform interventions redistribute demand across components (origins, lead times, listing types) rather than simply shifting a scalar level. A forecasting framework that cannot represent redistributive shocks on the simplex will miss the primary mechanism through which coupling operates.

### S3.2 Unconstrained demand estimation and demand censoring

The censoring formulation Bt≤min⁡(Dt,St)B\_{t}\leq\min(D\_{t},S\_{t}) connects the platform forecasting problem to a mature literature on unconstrained demand estimation in revenue management and demand censoring in inventory systems. In hotel revenue management, observed room sales are censored by available capacity, and recovering the latent demand distribution is a prerequisite for optimal pricing and allocation (Talluri and van Ryzin, [2004](#bib.bib78 "The theory and practice of revenue management")). The statistical problem is classical: the forecaster observes a truncated or censored outcome and must infer the parameters of the uncensored distribution. Standard approaches include expectation-maximization algorithms for censored Poisson or normal demand (Talluri and van Ryzin, [2004](#bib.bib78 "The theory and practice of revenue management")), booking curve detruncation methods that project partial booking curves to their uncensored completions (Schwartz, [1997](#bib.bib91 "Monitoring the accuracy of a hotel forecasting system"); Weatherford and Bodily, [1992](#bib.bib84 "A taxonomy and research overview of perishable-asset revenue management")), and Bayesian formulations that place priors on both the demand parameters and the censoring probability.

The platform accommodation setting introduces three complications that go beyond the classical problem. First, the censoring threshold StS\_{t} is not fixed or known; it is time-varying, endogenous to demand signals, and must itself be estimated or forecast. Second, the censoring is high-dimensional: supply constraints bind differently across listing types, locations, price tiers, and dates, so the relevant censoring mechanism operates on a compositional supply surface rather than a scalar capacity limit. Third, the censoring threshold responds to the same market conditions that drive demand, creating simultaneity that standard censored-demand estimators do not address. A concrete platform-specific example illustrates the difficulty: a host who observes strong demand may block weekend dates for personal use, or impose a three-night minimum stay that eliminates short-trip demand. Hotels also use close-outs and length-of-stay controls, but these decisions are centralized within the firm and typically observable to its revenue management system. In peer-to-peer platforms, thousands of heterogeneous hosts adjust availability rules idiosyncratically, making the effective censoring threshold stochastic and substantially harder to measure or forecast than in the hotel setting. These complications constitute the primary novelty of the platform censoring problem relative to the hotel revenue management baseline. A further practical difficulty is that external scrape-based supply proxies are noisy: calendar scrapes typically cannot distinguish “booked” from “blocked” nights without inference (see Appendix [S1](#A1 "Appendix S1 Measurement and data sources")), so any estimate of StS\_{t} from public data carries measurement error that propagates into the censoring correction. Platform-internal data can separate booked and blocked states directly.

The connection is nonetheless valuable. Methodologically, it provides a well-understood starting point: the tools for censored likelihood estimation, EM algorithms for incomplete data, and Bayesian data augmentation for latent demand are directly applicable as building blocks. Conceptually, it clarifies what is and is not new in the platform setting. The existence of a supply constraint on observed demand is not new; the hotel literature has handled this for decades. What is new is the endogeneity, dimensionality, and decision-driven nature of the constraint itself.

### S3.3 Causal inference meets forecasting

Coupling is often policy-mediated, which makes causal inference tools directly relevant to forecasting in platform markets. The practical toolkit includes three families.

Bayesian structural time series (BSTS), operationalized in the CausalImpact framework (Brodersen et al., [2015](#bib.bib19 "Inferring causal impact using Bayesian structural time-series models")), provide counterfactual prediction when intervention timing is known. BSTS models fit a state-space model to pre-intervention data and project it forward, using the discrepancy between the projection and the observed post-intervention outcome as an estimate of causal impact. This approach is natural for evaluating the effect of regulation or platform policy changes on accommodation metrics, but it requires a clean pre-period and known intervention timing, conditions that are often violated when platforms intervene continuously.

Synthetic control methods (Abadie et al., [2010](#bib.bib1 "Synthetic control methods for comparative case studies: estimating the effect of California’s tobacco control program"), [2015](#bib.bib2 "Comparative politics and the synthetic control method")) formalize counterfactual construction from a donor pool of untreated units. In the accommodation context, markets where regulation was introduced can be compared to synthetic control markets constructed from markets without the regulation. The method is powerful for single, discrete interventions but less suited to the continuous, overlapping interventions that characterize platform design changes.

Difference-in-differences designs are common in platform policy evaluation, including studies of cancellation policy effects (Jia et al., [2021](#bib.bib41 "Platform as a rule-maker: evidence from Airbnb’s cancellation policies")) and regulation impacts (Koster et al., [2021](#bib.bib52 "Short-term rentals and the housing market: quasi-experimental evidence from Airbnb in Los Angeles"); Duso et al., [2024](#bib.bib29 "Airbnb and rental markets: evidence from Berlin")). However, they inherit risks when treatment timing and heterogeneity interact with dynamic feedback, precisely the conditions that coupling creates. The broader literature on causality and policy evaluation (Athey and Imbens, [2017](#bib.bib10 "The state of applied econometrics: causality and policy evaluation")) provides the methodological standards that coupled forecasting must meet, including attention to heterogeneous treatment effects, staggered adoption, and interference between units.

For the research agenda, the gap is not the absence of causal tools but their integration with forecasting. Existing causal methods evaluate interventions retrospectively; the coupled forecasting problem requires causal reasoning prospectively, forecasting what will happen under interventions that have not yet occurred or that are unobservable.

### S3.4 Regime change and structural breaks

The post-2020 period made structural breaks unavoidable in tourism time series, and the accommodation sector was among the most severely affected. Point forecasts trained on stable regimes failed catastrophically, and the recovery exhibited heterogeneous trajectories across markets, segments, and metrics.

The classical approach to multiple structural breaks is the Bai and Perron ([2003](#bib.bib11 "Computation and analysis of multiple structural change models")) framework, which estimates break timing and regime-specific parameters in regression structures. For algorithmic change-point detection with computational efficiency, the PELT algorithm (Killick et al., [2012](#bib.bib50 "Optimal detection of changepoints with a linear computational cost")) provides optimal segmentation in linear time under certain penalty structures. Both approaches operate on scalar or low-dimensional time series and detect level or trend shifts.

Bayesian change-point models offer a probabilistic alternative. Fearnhead ([2006](#bib.bib34 "Exact and efficient Bayesian inference for multiple changepoint problems")) develops exact Bayesian inference for multiple change-points, while Adams and MacKay ([2007](#bib.bib4 "Bayesian online changepoint detection")) propose Bayesian online change-point detection (BOCPD) for sequential settings. The Bayesian framework is attractive for forecasting because it produces posterior probabilities over change-point locations, which can be propagated into prediction uncertainty. Tourism applications include structural break dating for arrivals series (Cró and Martins, [2017](#bib.bib26 "Structural breaks in international tourism demand: are they caused by crises or disasters?")) and Markov-switching models for demand cycles (Botha and Saayman, [2022](#bib.bib18 "Forecasting tourism demand cycles: a Markov-switching approach")).

For platform accommodation, a key limitation of standard break detection is that it operates on scalar series and detects level shifts. The coupling argument implies that shocks redistribute mass across components rather than simply shifting a mean. The pandemic did not just reduce bookings; it shifted origin mixes, compressed lead-time distributions, altered host type compositions, and changed spatial patterns (Katz et al., [2025](#bib.bib48 "Lead times in flux: analyzing Airbnb booking dynamics during global upheavals (2018–2022)"); Yang et al., [2021](#bib.bib86 "A review of early COVID-19 research in tourism")). These are compositional changes that require break detection on the simplex. The directional-shift DARMA framework (Katz, [2026](#bib.bib43 "Directional-shift Dirichlet ARMA models for compositional time series with structural break intervention")) addresses this gap by parameterizing a structural break as a direction of change on the simplex, an amplitude, and a logistic timing function, while maintaining the Dirichlet likelihood throughout.

### S3.5 Adjacent approaches for joint modeling

Several methodological traditions outside tourism forecasting address the problem of jointly modeling multiple endogenous variables and can serve as templates or components for coupled supply-demand forecasting.

Simultaneous equation models. The econometric tradition of simultaneous equation estimation (Haavelmo, [1943](#bib.bib39 "The statistical implications of a system of simultaneous equations"); Zellner and Theil, [1962](#bib.bib87 "Three-stage least squares: simultaneous estimation of simultaneous equations")) directly addresses the identification problem in jointly determined systems. Three-stage least squares extends single-equation instrumental variables to entire systems, exploiting cross-equation covariance and allowing cross-equation parameter restrictions.

Structural equilibrium models. In industrial organization, Berry et al. ([1995](#bib.bib17 "Automobile prices in market equilibrium")) develop an empirical framework for differentiated product markets that jointly models demand (discrete choice with consumer heterogeneity) and supply (firm first-order conditions from price competition). Farronato and Fradkin ([2022](#bib.bib33 "The welfare effects of peer entry: the case of Airbnb and the accommodation industry")) apply a related structural approach to the Airbnb–hotel competition setting.

Multi-task learning. From the machine learning side, Caruana ([1997](#bib.bib21 "Multitask learning")) frames multitask learning as inductive transfer: learning tasks in parallel with a shared representation can improve generalization because additional task signals act as a regularizing bias. Modern probabilistic deep forecasting models (Salinas et al., [2020](#bib.bib71 "DeepAR: probabilistic forecasting with autoregressive recurrent networks"); Lim et al., [2021](#bib.bib59 "Temporal Fusion Transformers for interpretable multi-horizon time series forecasting")) implement multi-task logic at scale.

Agent-based models. Agent-based modeling provides mechanism exploration through simulation of micro-level agent rules and the resulting macro-level dynamics (Lux and Marchesi, [1999](#bib.bib61 "Scaling and criticality in a stochastic multi-agent model of a financial market"); LeBaron, [2006](#bib.bib54 "Agent-based computational finance")). In the platform accommodation context, Vinogradov et al. ([2020](#bib.bib81 "An agent-based modelling approach to housing market regulations and Airbnb-induced tourism")) use ABM to simulate Airbnb supply growth under alternative regulatory regimes in Norwegian municipalities, and Overwater and Yorke-Smith ([2022](#bib.bib82 "Agent-based simulation of short-term peer-to-peer rentals: evidence from the Amsterdam housing market")) model the interaction between short-term rentals, housing prices, and residential displacement in Amsterdam.

Joint forecasting in adjacent domains. In electricity markets, Maciejowska and Nitka ([2024](#bib.bib62 "Multiple split approach: multidimensional probabilistic forecasting of electricity markets")) show that the largest accuracy gains appear when forecasting functions of jointly distributed quantities. In labor markets, Barnichon and Nekarda ([2012](#bib.bib14 "The ins and outs of forecasting unemployment")) forecast the unemployment rate by modeling the labor force flows that govern the stock, offering a transferable template for platform accommodation where bookings are the constrained intersection of supply availability and demand intent.

### S3.6 Uncertainty quantification

Uncertainty quantification is harder under coupling because forecast errors across targets are correlated and state-dependent.

For comparing point forecast accuracy, the Diebold and Mariano ([1995](#bib.bib27 "Comparing predictive accuracy")) framework remains standard. For interval forecasts, Christoffersen ([1998](#bib.bib24 "Evaluating interval forecasts")) conditional coverage tests detect clustered violations, an important diagnostic when coupling creates correlated forecast misses. For probability integral transform (PIT) evaluation, Diebold et al. ([1998](#bib.bib28 "Evaluating density forecasts with applications to financial risk management")) show that marginal calibration can appear satisfactory while the joint dynamics are misspecified, a warning directly relevant to coupled systems where marginal supply and demand forecasts may look well-calibrated while the joint distribution is wrong.

For density forecasts, Gneiting and Raftery ([2007](#bib.bib36 "Strictly proper scoring rules, prediction, and estimation")) establish the framework of proper scoring rules that reward sharpness subject to calibration. In multivariate settings, however, standard energy scores have limited sensitivity to misspecified dependence structures (Pinson and Tastu, [2013](#bib.bib64 "Discussion of the role of improper scoring rules in energy forecasting")). Scheuerer and Hamill ([2015](#bib.bib72 "Variogram-based proper scoring rules for probabilistic forecasts of multivariate quantities")) propose variogram-based proper scoring rules that are explicitly sensitive to the dependence between forecast components. For coupled supply-demand forecasting, dependence-sensitive scores are essential because joint forecast errors propagate across sides.

Conformal prediction provides distribution-free coverage guarantees under exchangeability assumptions (Romano et al., [2019](#bib.bib70 "Conformalized quantile regression"); Barber et al., [2021](#bib.bib13 "Predictive inference with the jackknife+")). For coupled systems, the challenge is that exchangeability is precisely what endogenous intervention violates. Developing conformal-style guarantees under the non-stationarity created by platform coupling is an open problem.

Recent work on tail calibration (Allen et al., [2025](#bib.bib6 "Tail calibration of probabilistic forecasts")) demonstrates that “calibrated on average” is insufficient for decision contexts dominated by tail risk. This is especially relevant when coupling amplifies extreme outcomes.

## Appendix S4 Search-to-booking distance metrics

The search-to-booking gap (Section [5.2](#S5.SS2 "5.2 The search-to-booking gap as a supply constraint signal ‣ 5 Research agenda")) can be quantified by treating both the search lead-time distribution and the booking lead-time distribution as compositional objects on the simplex. Let 𝐩tsearch\mathbf{p}^{\text{search}}\_{t} denote the search lead-time composition and 𝐩tbook\mathbf{p}^{\text{book}}\_{t} the booking lead-time composition in period tt.

The Aitchison distance between the two compositions is

|  |  |  |
| --- | --- | --- |
|  | dA​(𝐩tsearch,𝐩tbook)=‖clr​(𝐩tsearch)−clr​(𝐩tbook)‖2,d\_{A}(\mathbf{p}^{\text{search}}\_{t},\mathbf{p}^{\text{book}}\_{t})=\|\text{clr}(\mathbf{p}^{\text{search}}\_{t})-\text{clr}(\mathbf{p}^{\text{book}}\_{t})\|\_{2}, |  |

where clr is the centered log-ratio transformation (Aitchison, [1986](#bib.bib5 "The statistical analysis of compositional data")). The Aitchison distance is preferred for compositions because it is scale-invariant and subcompositionally coherent; note that the clr transformation requires strictly positive components, so zero lead-time bins must be handled via small pseudocounts or multiplicative zero replacement before transformation.

Alternatively, the normalized L1L\_{1} distance used in Katz et al. ([2025](#bib.bib48 "Lead times in flux: analyzing Airbnb booking dynamics during global upheavals (2018–2022)")) avoids the zero problem at the cost of losing the geometric properties of the Aitchison framework.

The distributional fitting framework of Katz et al. ([2026](#bib.bib46 "Distributional fitting and tail analysis of lead-time compositions: nights vs. revenue on Airbnb")) provides the parametric machinery for modeling these compositions over time. The open problem is extending these tools to paired compositions and interpreting their divergence as a constraint indicator within a demand forecasting system.

Computing lead-time compositions requires internal search logs in which queries are tagged with intended stay dates (e.g., check-in/check-out fields or calendar interactions). Google Trends provides only a scalar index of search intensity over calendar time and cannot deliver lead-time distributions without strong additional assumptions; it is therefore suitable as a proxy for aggregate demand intent but not for the distributional gap measure.

## References

* A. Abadie, A. Diamond, and J. Hainmueller (2010)
  Synthetic control methods for comparative case studies: estimating the effect of California’s tobacco control program.
  Journal of the American Statistical Association 105 (490),  pp. 493–505.
  External Links: [Document](https://dx.doi.org/10.1198/jasa.2009.ap08746)
  Cited by: [§S3.3](#A3.SS3.p3.1 "S3.3 Causal inference meets forecasting ‣ Appendix S3 Methodological building blocks"),
  [§5.1](#S5.SS1.p5.1 "5.1 Methodological landscape ‣ 5 Research agenda"),
  [§5.6](#S5.SS6.p1.1 "5.6 Causal forecasting under unobservable platform intervention ‣ 5 Research agenda").
* A. Abadie, A. Diamond, and J. Hainmueller (2015)
  Comparative politics and the synthetic control method.
  American Journal of Political Science 59 (2),  pp. 495–510.
  External Links: [Document](https://dx.doi.org/10.1111/ajps.12116)
  Cited by: [§S3.3](#A3.SS3.p3.1 "S3.3 Causal inference meets forecasting ‣ Appendix S3 Methodological building blocks"),
  [§5.1](#S5.SS1.p5.1 "5.1 Methodological landscape ‣ 5 Research agenda"),
  [§5.6](#S5.SS6.p1.1 "5.6 Causal forecasting under unobservable platform intervention ‣ 5 Research agenda").
* G. Abrate and G. Viglia (2022)
  Dynamic pricing in Airbnb: individual vs professional hosts.
  Journal of Business Research 141,  pp. 191–201.
  External Links: [Document](https://dx.doi.org/10.1016/j.jbusres.2021.12.012)
  Cited by: [§3.2](#S3.SS2.p1.1 "3.2 Platform accommodation: pricing, supply dynamics, and regulation ‣ 3 Platform accommodation markets and the supply-side gap").
* R. P. Adams and D. J. C. MacKay (2007)
  Bayesian online changepoint detection.
  arXiv preprint arXiv:0710.3742.
  Cited by: [§S3.4](#A3.SS4.p3.1 "S3.4 Regime change and structural breaks ‣ Appendix S3 Methodological building blocks"),
  [§5.6](#S5.SS6.p2.1 "5.6 Causal forecasting under unobservable platform intervention ‣ 5 Research agenda").
* J. Aitchison and S. M. Shen (1980)
  Logistic-normal distributions: some properties and uses.
  Biometrika 67 (2),  pp. 261–272.
  External Links: [Document](https://dx.doi.org/10.1093/biomet/67.2.261)
  Cited by: [§S3.1](#A3.SS1.p3.1 "S3.1 Compositional and constrained forecasting ‣ Appendix S3 Methodological building blocks").
* J. Aitchison (1986)
  The statistical analysis of compositional data.
   Chapman & Hall.
  Cited by: [§S3.1](#A3.SS1.p1.1 "S3.1 Compositional and constrained forecasting ‣ Appendix S3 Methodological building blocks"),
  [§S3.1](#A3.SS1.p3.1 "S3.1 Compositional and constrained forecasting ‣ Appendix S3 Methodological building blocks"),
  [Appendix S4](#A4.p2.2 "Appendix S4 Search-to-booking distance metrics"),
  [§4.2](#S4.SS2.p4.1 "4.2 Informational coupling: the missing ceiling ‣ 4 The coupling problem"),
  [§5.1](#S5.SS1.p6.1 "5.1 Methodological landscape ‣ 5 Research agenda").
* S. Allen, J. Koh, J. Segers, and J. Ziegel (2025)
  Tail calibration of probabilistic forecasts.
  Journal of the American Statistical Association 120,  pp. 2796–2808.
  External Links: [Document](https://dx.doi.org/10.1080/01621459.2025.2506194)
  Cited by: [§S3.6](#A3.SS6.p5.1 "S3.6 Uncertainty quantification ‣ Appendix S3 Methodological building blocks").
* M. Armstrong (2006)
  Competition in two-sided markets.
  RAND Journal of Economics 37 (3),  pp. 668–691.
  External Links: [Document](https://dx.doi.org/10.1111/j.1756-2171.2006.tb00037.x)
  Cited by: [§1](#S1.p2.1 "1 Introduction"),
  [§3.1](#S3.SS1.p2.1 "3.1 Two-sided foundations ‣ 3 Platform accommodation markets and the supply-side gap"),
  [§5.1](#S5.SS1.p4.1 "5.1 Methodological landscape ‣ 5 Research agenda").
* A. G. Assaf, G. Li, H. Song, and M. G. Tsionas (2019)
  Modeling and forecasting regional tourism demand using the Bayesian global vector autoregressive (BGVAR) model.
  Journal of Travel Research 58 (5),  pp. 795–811.
  External Links: [Document](https://dx.doi.org/10.1177/0047287518759226)
  Cited by: [§2](#S2.p6.1 "2 Tourism demand forecasting since 2019").
* G. Athanasopoulos, R. J. Hyndman, H. Song, and D. C. Wu (2011)
  The tourism forecasting competition.
  International Journal of Forecasting 27 (3),  pp. 822–844.
  External Links: [Document](https://dx.doi.org/10.1016/j.ijforecast.2010.04.009)
  Cited by: [§2](#S2.p2.1 "2 Tourism demand forecasting since 2019"),
  [§2](#S2.p7.1 "2 Tourism demand forecasting since 2019").
* S. Athey and G. W. Imbens (2017)
  The state of applied econometrics: causality and policy evaluation.
  Journal of Economic Perspectives 31 (2),  pp. 3–32.
  External Links: [Document](https://dx.doi.org/10.1257/jep.31.2.3)
  Cited by: [§S3.3](#A3.SS3.p4.1 "S3.3 Causal inference meets forecasting ‣ Appendix S3 Methodological building blocks"),
  [§5.3](#S5.SS3.p3.3 "5.3 Demand forecasting under an endogenous supply ceiling ‣ 5 Research agenda").
* J. Bai, K. C. So, C. S. Tang, X. Chen, and H. Wang (2019)
  Coordinating supply and demand on an on-demand service platform with impatient customers.
  Manufacturing & Service Operations Management 21 (3),  pp. 556–570.
  External Links: [Document](https://dx.doi.org/10.1287/msom.2018.0707)
  Cited by: [§3.1](#S3.SS1.p3.1 "3.1 Two-sided foundations ‣ 3 Platform accommodation markets and the supply-side gap"),
  [§5.1](#S5.SS1.p4.1 "5.1 Methodological landscape ‣ 5 Research agenda").
* J. Bai and P. Perron (2003)
  Computation and analysis of multiple structural change models.
  Journal of Applied Econometrics 18 (1),  pp. 1–22.
  External Links: [Document](https://dx.doi.org/10.1002/jae.659)
  Cited by: [§S3.4](#A3.SS4.p2.1 "S3.4 Regime change and structural breaks ‣ Appendix S3 Methodological building blocks"),
  [§5.6](#S5.SS6.p1.1 "5.6 Causal forecasting under unobservable platform intervention ‣ 5 Research agenda").
* R. F. Barber, E. J. Candès, A. Ramdas, and R. J. Tibshirani (2021)
  Predictive inference with the jackknife+.
  Annals of Statistics 49 (1),  pp. 486–507.
  External Links: [Document](https://dx.doi.org/10.1214/20-AOS1965)
  Cited by: [§S3.6](#A3.SS6.p4.1 "S3.6 Uncertainty quantification ‣ Appendix S3 Methodological building blocks"),
  [§5.6](#S5.SS6.p2.1 "5.6 Causal forecasting under unobservable platform intervention ‣ 5 Research agenda").
* C. Barceló-Vidal, L. Aguilar, and J. A. Martín-Fernández (2011)
  Compositional VARIMA time series.
  In Compositional Data Analysis: Theory and Applications, V. Pawlowsky-Glahn and A. Buccianti (Eds.),
   pp. 87–103.
  External Links: [Document](https://dx.doi.org/10.1002/9781119976462.ch7)
  Cited by: [§S3.1](#A3.SS1.p2.1 "S3.1 Compositional and constrained forecasting ‣ Appendix S3 Methodological building blocks").
* R. Barnichon and C. J. Nekarda (2012)
  The ins and outs of forecasting unemployment.
  Brookings Papers on Economic Activity 43 (2),  pp. 83–131.
  External Links: [Document](https://dx.doi.org/10.1353/eca.2012.0018)
  Cited by: [§S3.5](#A3.SS5.p6.1 "S3.5 Adjacent approaches for joint modeling ‣ Appendix S3 Methodological building blocks"),
  [§5.3](#S5.SS3.p2.1 "5.3 Demand forecasting under an endogenous supply ceiling ‣ 5 Research agenda").
* J. M. Bates and C. W. J. Granger (1969)
  The combination of forecasts.
  Operational Research Quarterly 20 (4),  pp. 451–468.
  External Links: [Document](https://dx.doi.org/10.1057/jors.1969.103)
  Cited by: [§2](#S2.p2.1 "2 Tourism demand forecasting since 2019").
* S. Berry, J. Levinsohn, and A. Pakes (1995)
  Automobile prices in market equilibrium.
  Econometrica 63 (4),  pp. 841–890.
  External Links: [Document](https://dx.doi.org/10.2307/2171802)
  Cited by: [§S3.1](#A3.SS1.p3.1 "S3.1 Compositional and constrained forecasting ‣ Appendix S3 Methodological building blocks"),
  [§S3.5](#A3.SS5.p3.1 "S3.5 Adjacent approaches for joint modeling ‣ Appendix S3 Methodological building blocks").
* A. J. Bibler, K. F. Teltser, and M. J. Tremblay (2025)
  How do short-term rental regulations affect market outcomes? Evidence from San Francisco’s Airbnb registration requirement.
  Real Estate Economics 53 (4),  pp. 841–868.
  External Links: [Document](https://dx.doi.org/10.1111/1540-6229.12537)
  Cited by: [§3.2](#S3.SS2.p2.1 "3.2 Platform accommodation: pricing, supply dynamics, and regulation ‣ 3 Platform accommodation markets and the supply-side gap"),
  [§4.3](#S4.SS3.p2.1 "4.3 Intervention coupling: endogenous regime change ‣ 4 The coupling problem"),
  [§5.8](#S5.SS8.p2.1 "5.8 A minimal empirical design ‣ 5 Research agenda").
* I. Botha and A. Saayman (2022)
  Forecasting tourism demand cycles: a Markov-switching approach.
  International Journal of Tourism Research 24 (6),  pp. 759–774.
  External Links: [Document](https://dx.doi.org/10.1002/jtr.2543)
  Cited by: [§S3.4](#A3.SS4.p3.1 "S3.4 Regime change and structural breaks ‣ Appendix S3 Methodological building blocks").
* K. H. Brodersen, F. Gallusser, J. Koehler, N. Remy, and S. L. Scott (2015)
  Inferring causal impact using Bayesian structural time-series models.
  Annals of Applied Statistics 9 (1),  pp. 247–274.
  External Links: [Document](https://dx.doi.org/10.1214/14-AOAS788)
  Cited by: [§S3.3](#A3.SS3.p2.1 "S3.3 Causal inference meets forecasting ‣ Appendix S3 Methodological building blocks"),
  [§2](#S2.p6.1 "2 Tourism demand forecasting since 2019"),
  [§5.1](#S5.SS1.p5.1 "5.1 Methodological landscape ‣ 5 Research agenda"),
  [§5.6](#S5.SS6.p1.1 "5.6 Causal forecasting under unobservable platform intervention ‣ 5 Research agenda").
* T. M. Brunsdon and T. M. F. Smith (1998)
  The time series analysis of compositional data.
  Journal of Official Statistics 14 (3),  pp. 237–253.
  Cited by: [§S3.1](#A3.SS1.p2.1 "S3.1 Compositional and constrained forecasting ‣ Appendix S3 Methodological building blocks").
* G. P. Cachon, K. M. Daniels, and R. Lobel (2017)
  The role of surge pricing on a service platform with self-scheduling capacity.
  Manufacturing & Service Operations Management 19 (3),  pp. 368–384.
  External Links: [Document](https://dx.doi.org/10.1287/msom.2017.0618)
  Cited by: [§3.1](#S3.SS1.p3.1 "3.1 Two-sided foundations ‣ 3 Platform accommodation markets and the supply-side gap"),
  [§4.1](#S4.SS1.p3.1 "4.1 Behavioral coupling: policies propagate across sides ‣ 4 The coupling problem"),
  [§5.1](#S5.SS1.p4.1 "5.1 Methodological landscape ‣ 5 Research agenda").
* C. Cargnoni, P. Müller, and M. West (1997)
  Bayesian forecasting of multinomial time series through conditionally Gaussian dynamic models.
  Journal of the American Statistical Association 92 (438),  pp. 640–647.
  External Links: [Document](https://dx.doi.org/10.1080/01621459.1997.10474015)
  Cited by: [§S3.1](#A3.SS1.p3.1 "S3.1 Compositional and constrained forecasting ‣ Appendix S3 Methodological building blocks").
* R. Caruana (1997)
  Multitask learning.
  Machine Learning 28,  pp. 41–75.
  External Links: [Document](https://dx.doi.org/10.1023/A%3A1007379606734)
  Cited by: [§S3.5](#A3.SS5.p4.1 "S3.5 Adjacent approaches for joint modeling ‣ Appendix S3 Methodological building blocks").
* G. Casamatta, S. Giannoni, D. Brunstein, and J. Jouve (2022)
  Host type and pricing on Airbnb: seasonality and strategies.
  Tourism Management 88,  pp. 104433.
  External Links: [Document](https://dx.doi.org/10.1016/j.tourman.2021.104433)
  Cited by: [§3.2](#S3.SS2.p1.1 "3.2 Platform accommodation: pricing, supply dynamics, and regulation ‣ 3 Platform accommodation markets and the supply-side gap").
* P. F. Christoffersen (1998)
  Evaluating interval forecasts.
  International Economic Review 39 (4),  pp. 841–862.
  External Links: [Document](https://dx.doi.org/10.2307/2527341)
  Cited by: [§S3.6](#A3.SS6.p2.1 "S3.6 Uncertainty quantification ‣ Appendix S3 Methodological building blocks").
* G. Coenders and B. Ferrer-Rosell (2020)
  Compositional data analysis in tourism: review and future directions.
  Tourism Analysis 25 (1),  pp. 153–168.
  External Links: [Document](https://dx.doi.org/10.3727/108354220X15758301241594)
  Cited by: [§S3.1](#A3.SS1.p2.1 "S3.1 Compositional and constrained forecasting ‣ Appendix S3 Methodological building blocks").
* G. Coenders, J. A. Martín-Fernández, and B. Ferrer-Rosell (2017)
  When relative and absolute information matter: compositional predictor with a total in generalized linear models.
  Statistical Modelling 17 (6),  pp. 494–512.
  External Links: [Document](https://dx.doi.org/10.1177/1471082X17710398)
  Cited by: [§S3.1](#A3.SS1.p3.1 "S3.1 Compositional and constrained forecasting ‣ Appendix S3 Methodological building blocks").
* S. Cró and A. M. Martins (2017)
  Structural breaks in international tourism demand: are they caused by crises or disasters?.
  Tourism Management 63,  pp. 3–9.
  External Links: [Document](https://dx.doi.org/10.1016/j.tourman.2017.05.009)
  Cited by: [§S3.4](#A3.SS4.p3.1 "S3.4 Regime change and structural breaks ‣ Appendix S3 Methodological building blocks").
* F. X. Diebold, T. A. Gunther, and A. S. Tay (1998)
  Evaluating density forecasts with applications to financial risk management.
  International Economic Review 39 (4),  pp. 863–883.
  External Links: [Document](https://dx.doi.org/10.2307/2527342)
  Cited by: [§S3.6](#A3.SS6.p2.1 "S3.6 Uncertainty quantification ‣ Appendix S3 Methodological building blocks").
* F. X. Diebold and R. S. Mariano (1995)
  Comparing predictive accuracy.
  Journal of Business & Economic Statistics 13 (3),  pp. 253–263.
  External Links: [Document](https://dx.doi.org/10.1080/07350015.1995.10524599)
  Cited by: [§S3.6](#A3.SS6.p2.1 "S3.6 Uncertainty quantification ‣ Appendix S3 Methodological building blocks"),
  [§5.5](#S5.SS5.p1.1 "5.5 Price elasticity asymmetry as a coupling diagnostic ‣ 5 Research agenda"),
  [§5.8](#S5.SS8.p4.3 "5.8 A minimal empirical design ‣ 5 Research agenda").
* T. Duso, C. Michelsen, M. Schäfer, and K. D. Tran (2024)
  Airbnb and rental markets: evidence from Berlin.
  Regional Science and Urban Economics 106,  pp. 104007.
  External Links: [Document](https://dx.doi.org/10.1016/j.regsciurbeco.2024.104007)
  Cited by: [§S3.3](#A3.SS3.p4.1 "S3.3 Causal inference meets forecasting ‣ Appendix S3 Methodological building blocks"),
  [§3.2](#S3.SS2.p2.1 "3.2 Platform accommodation: pricing, supply dynamics, and regulation ‣ 3 Platform accommodation markets and the supply-side gap"),
  [§4.3](#S4.SS3.p2.1 "4.3 Intervention coupling: endogenous regime change ‣ 4 The coupling problem"),
  [§5.8](#S5.SS8.p2.1 "5.8 A minimal empirical design ‣ 5 Research agenda").
* J. J. Egozcue, V. Pawlowsky-Glahn, G. Mateu-Figueras, and C. Barceló-Vidal (2003)
  Isometric logratio transformations for compositional data analysis.
  Mathematical Geology 35 (3),  pp. 279–300.
  External Links: [Document](https://dx.doi.org/10.1023/A%3A1023818214614)
  Cited by: [§S3.1](#A3.SS1.p2.1 "S3.1 Compositional and constrained forecasting ‣ Appendix S3 Methodological building blocks").
* N. Fan, S. Lai, Z. Fan, and Y. Chen (2023)
  Exit and transition: exploring the survival status of Airbnb listings in a time of professionalization.
  Tourism Management 95,  pp. 104665.
  External Links: [Document](https://dx.doi.org/10.1016/j.tourman.2022.104665)
  Cited by: [§3.2](#S3.SS2.p2.1 "3.2 Platform accommodation: pricing, supply dynamics, and regulation ‣ 3 Platform accommodation markets and the supply-side gap"),
  [§4.2](#S4.SS2.p4.1 "4.2 Informational coupling: the missing ceiling ‣ 4 The coupling problem").
* C. Farronato and A. Fradkin (2022)
  The welfare effects of peer entry: the case of Airbnb and the accommodation industry.
  American Economic Review 112 (6),  pp. 1782–1817.
  External Links: [Document](https://dx.doi.org/10.1257/aer.20180260)
  Cited by: [§S3.5](#A3.SS5.p3.1 "S3.5 Adjacent approaches for joint modeling ‣ Appendix S3 Methodological building blocks"),
  [§1](#S1.p2.1 "1 Introduction"),
  [§3.2](#S3.SS2.p2.1 "3.2 Platform accommodation: pricing, supply dynamics, and regulation ‣ 3 Platform accommodation markets and the supply-side gap").
* P. Fearnhead (2006)
  Exact and efficient Bayesian inference for multiple changepoint problems.
  Statistics and Computing 16,  pp. 203–213.
  External Links: [Document](https://dx.doi.org/10.1007/s11222-006-8450-8)
  Cited by: [§S3.4](#A3.SS4.p3.1 "S3.4 Regime change and structural breaks ‣ Appendix S3 Methodological building blocks"),
  [§5.6](#S5.SS6.p2.1 "5.6 Causal forecasting under unobservable platform intervention ‣ 5 Research agenda").
* E. Ghysels, P. Santa-Clara, and R. Valkanov (2004)
  The MIDAS touch: mixed data sampling regression models.
  CIRANO Working Papers 2004s-20.
  Cited by: [§2](#S2.p5.1 "2 Tourism demand forecasting since 2019").
* T. Gneiting and A. E. Raftery (2007)
  Strictly proper scoring rules, prediction, and estimation.
  Journal of the American Statistical Association 102 (477),  pp. 359–378.
  External Links: [Document](https://dx.doi.org/10.1198/016214506000001437)
  Cited by: [§S3.6](#A3.SS6.p3.1 "S3.6 Uncertainty quantification ‣ Appendix S3 Methodological building blocks").
* Google (2024)
  Google Trends.
  Note: Accessed 2026-02-01
  External Links: [Link](https://trends.google.com)
  Cited by: [§5.8](#S5.SS8.p5.1 "5.8 A minimal empirical design ‣ 5 Research agenda").
* J. Grau-Escolano, S. A. Clavé, and J. Borràs (2026)
  Daily tourism demand forecasting via card transactions: a multi-source, interpretable, framework for diverse destinations and markets.
  Information Technology & Tourism 28 (1),  pp. 1–29.
  External Links: [Document](https://dx.doi.org/10.1007/s40558-025-00350-2)
  Cited by: [Appendix S1](#A1.p2.1 "Appendix S1 Measurement and data sources"),
  [§2](#S2.p4.2 "2 Tourism demand forecasting since 2019").
* G. K. Grunwald, A. E. Raftery, and P. Guttorp (1993)
  Time series of continuous proportions.
  Journal of the Royal Statistical Society: Series B 55 (1),  pp. 103–116.
  Cited by: [§S3.1](#A3.SS1.p3.1 "S3.1 Compositional and constrained forecasting ‣ Appendix S3 Methodological building blocks").
* T. Haavelmo (1943)
  The statistical implications of a system of simultaneous equations.
  Econometrica 11 (1),  pp. 1–12.
  External Links: [Document](https://dx.doi.org/10.2307/1905714)
  Cited by: [§S3.5](#A3.SS5.p2.1 "S3.5 Adjacent approaches for joint modeling ‣ Appendix S3 Methodological building blocks"),
  [§5.3](#S5.SS3.p2.1 "5.3 Demand forecasting under an endogenous supply ceiling ‣ 5 Research agenda").
* M. Hu, H. Li, H. Song, X. Li, and R. Law (2025)
  Tourism forecasting by mixed-frequency machine learning.
  Tourism Management 106,  pp. 105004.
  External Links: [Document](https://dx.doi.org/10.1016/j.tourman.2024.105004)
  Cited by: [§2](#S2.p5.1 "2 Tourism demand forecasting since 2019").
* Inside Airbnb (2024)
  Inside Airbnb: adding data to the debate.
  Note: Accessed 2026-02-01
  External Links: [Link](http://insideairbnb.com)
  Cited by: [§5.8](#S5.SS8.p5.1 "5.8 A minimal empirical design ‣ 5 Research agenda").
* J. Jia, G. Z. Jin, and L. Wagman (2021)
  Platform as a rule-maker: evidence from Airbnb’s cancellation policies.
  NBER Working Paper
  Technical Report 28878, National Bureau of Economic Research.
  Cited by: [§S3.3](#A3.SS3.p4.1 "S3.3 Causal inference meets forecasting ‣ Appendix S3 Methodological building blocks"),
  [§4.1](#S4.SS1.p2.1 "4.1 Behavioral coupling: policies propagate across sides ‣ 4 The coupling problem").
* H. Katz, K. T. Brusch, and R. E. Weiss (2024)
  A Bayesian Dirichlet auto-regressive moving average model for forecasting lead times.
  International Journal of Forecasting 40 (4),  pp. 1556–1567.
  External Links: [Document](https://dx.doi.org/10.1016/j.ijforecast.2024.01.004)
  Cited by: [§S3.1](#A3.SS1.p4.1 "S3.1 Compositional and constrained forecasting ‣ Appendix S3 Methodological building blocks"),
  [§4.2](#S4.SS2.p4.1 "4.2 Informational coupling: the missing ceiling ‣ 4 The coupling problem"),
  [§5.1](#S5.SS1.p6.1 "5.1 Methodological landscape ‣ 5 Research agenda").
* H. E. Katz, J. Needleman, and L. Medina (2026)
  Distributional fitting and tail analysis of lead-time compositions: nights vs. revenue on Airbnb.
  arXiv preprint arXiv:2601.12175.
  Cited by: [Appendix S4](#A4.p4.1 "Appendix S4 Search-to-booking distance metrics").
* H. Katz, E. Savage, and P. Coles (2025)
  Lead times in flux: analyzing Airbnb booking dynamics during global upheavals (2018–2022).
  Annals of Tourism Research Empirical Insights 6 (2),  pp. 100185.
  External Links: [Document](https://dx.doi.org/10.1016/j.annale.2025.100185)
  Cited by: [§S3.4](#A3.SS4.p4.1 "S3.4 Regime change and structural breaks ‣ Appendix S3 Methodological building blocks"),
  [Appendix S4](#A4.p3.1 "Appendix S4 Search-to-booking distance metrics"),
  [§4.3](#S4.SS3.p4.1 "4.3 Intervention coupling: endogenous regime change ‣ 4 The coupling problem").
* H. Katz and R. E. Weiss (2025)
  A Bayesian Dirichlet auto-regressive conditional heteroskedasticity model for forecasting currency shares.
  International Journal of Forecasting.
  Note: Forthcoming. arXiv:2507.14132
  Cited by: [§S3.1](#A3.SS1.p4.1 "S3.1 Compositional and constrained forecasting ‣ Appendix S3 Methodological building blocks"),
  [§5.4](#S5.SS4.p1.1 "5.4 Decomposing demand variance into exogenous and endogenous components ‣ 5 Research agenda").
* H. Katz and S. Wilson (2024)
  Darma: Bayesian Dirichlet ARMA models for compositional time series.
  Note: R package version 0.1.0
  External Links: [Link](https://github.com/harrisonekatz/darma)
  Cited by: [§S3.1](#A3.SS1.p4.1 "S3.1 Compositional and constrained forecasting ‣ Appendix S3 Methodological building blocks").
* H. Katz (2025)
  Centered-innovation MA for Dirichlet ARMA in compositional time-series forecasting.
  arXiv preprint arXiv:2510.18903.
  Cited by: [§S3.1](#A3.SS1.p4.1 "S3.1 Compositional and constrained forecasting ‣ Appendix S3 Methodological building blocks").
* H. Katz (2026)
  Directional-shift Dirichlet ARMA models for compositional time series with structural break intervention.
  arXiv preprint arXiv:2601.16821.
  Cited by: [§S3.1](#A3.SS1.p4.1 "S3.1 Compositional and constrained forecasting ‣ Appendix S3 Methodological building blocks"),
  [§S3.4](#A3.SS4.p4.1 "S3.4 Regime change and structural breaks ‣ Appendix S3 Methodological building blocks"),
  [§4.3](#S4.SS3.p4.1 "4.3 Intervention coupling: endogenous regime change ‣ 4 The coupling problem").
* R. Killick, P. Fearnhead, and I. A. Eckley (2012)
  Optimal detection of changepoints with a linear computational cost.
  Journal of the American Statistical Association 107 (500),  pp. 1590–1598.
  External Links: [Document](https://dx.doi.org/10.1080/01621459.2012.737745)
  Cited by: [§S3.4](#A3.SS4.p2.1 "S3.4 Regime change and structural breaks ‣ Appendix S3 Methodological building blocks"),
  [§5.6](#S5.SS6.p1.1 "5.6 Causal forecasting under unobservable platform intervention ‣ 5 Research agenda").
* A. S. Kolleck and T. Teubner (2025)
  How ratings shape the supply on sharing economy platforms: a longitudinal cohort study on listing survival on Airbnb.
  Information Systems Management 42 (2),  pp. 103–119.
  External Links: [Document](https://dx.doi.org/10.1080/10580530.2024.2339234)
  Cited by: [§4.2](#S4.SS2.p4.1 "4.2 Informational coupling: the missing ceiling ‣ 4 The coupling problem").
* H. R. A. Koster, J. van Ommeren, and N. Volkhausen (2021)
  Short-term rentals and the housing market: quasi-experimental evidence from Airbnb in Los Angeles.
  Journal of Urban Economics 124,  pp. 103356.
  External Links: [Document](https://dx.doi.org/10.1016/j.jue.2021.103356)
  Cited by: [§S3.3](#A3.SS3.p4.1 "S3.3 Causal inference meets forecasting ‣ Appendix S3 Methodological building blocks"),
  [§3.2](#S3.SS2.p2.1 "3.2 Platform accommodation: pricing, supply dynamics, and regulation ‣ 3 Platform accommodation markets and the supply-side gap"),
  [§4.3](#S4.SS3.p2.1 "4.3 Intervention coupling: endogenous regime change ‣ 4 The coupling problem").
* P. Kynčlová, P. Filzmoser, and K. Hron (2015)
  Modeling compositional time series with vector autoregressive models.
  Journal of Forecasting 34 (4),  pp. 303–314.
  External Links: [Document](https://dx.doi.org/10.1002/for.2336)
  Cited by: [§S3.1](#A3.SS1.p2.1 "S3.1 Compositional and constrained forecasting ‣ Appendix S3 Methodological building blocks").
* B. LeBaron (2006)
  Agent-based computational finance.
  In Handbook of Computational Economics,
  Vol. 2,  pp. 1187–1233.
  External Links: [Document](https://dx.doi.org/10.1016/S1574-0021%2805%2902024-1)
  Cited by: [§S3.5](#A3.SS5.p5.1 "S3.5 Adjacent approaches for joint modeling ‣ Appendix S3 Methodological building blocks").
* H. Lee and C. Lin (2023)
  Market forecast for the sharing economy, using Airbnb in US cities and in Taipei as an example.
  International Journal of Hospitality & Tourism Administration 24 (5),  pp. 776–789.
  External Links: [Document](https://dx.doi.org/10.1080/15256480.2022.2055693)
  Cited by: [§3.3](#S3.SS3.p1.1 "3.3 The supply-side forecasting gap ‣ 3 Platform accommodation markets and the supply-side gap").
* H. Li, H. Song, M. Witt, and G. Li (2022)
  Tourism forecasting competition in the time of COVID-19.
  Annals of Tourism Research 93,  pp. 103368.
  External Links: [Document](https://dx.doi.org/10.1016/j.annals.2022.103368)
  Cited by: [§2](#S2.p7.1 "2 Tourism demand forecasting since 2019").
* X. Li, R. Law, G. Xie, and S. Wang (2021)
  Review of tourism forecasting research with internet data.
  Tourism Management 83,  pp. 104245.
  External Links: [Document](https://dx.doi.org/10.1016/j.tourman.2020.104245)
  Cited by: [§2](#S2.p4.2 "2 Tourism demand forecasting since 2019"),
  [§5.2](#S5.SS2.p1.2 "5.2 The search-to-booking gap as a supply constraint signal ‣ 5 Research agenda").
* Z. Lian and G. van Ryzin (2021)
  Optimal growth in two-sided markets.
  Management Science 67 (11),  pp. 6862–6879.
  External Links: [Document](https://dx.doi.org/10.1287/mnsc.2020.3832)
  Cited by: [§3.1](#S3.SS1.p3.1 "3.1 Two-sided foundations ‣ 3 Platform accommodation markets and the supply-side gap"),
  [§5.1](#S5.SS1.p4.1 "5.1 Methodological landscape ‣ 5 Research agenda").
* B. Lim, S. Ö. Arık, N. Loeff, and T. Pfister (2021)
  Temporal Fusion Transformers for interpretable multi-horizon time series forecasting.
  International Journal of Forecasting 37 (4),  pp. 1748–1764.
  External Links: [Document](https://dx.doi.org/10.1016/j.ijforecast.2021.03.012)
  Cited by: [§S3.5](#A3.SS5.p4.1 "S3.5 Adjacent approaches for joint modeling ‣ Appendix S3 Methodological building blocks"),
  [§2](#S2.p3.1 "2 Tourism demand forecasting since 2019").
* R. E. Lucas (1976)
  Econometric policy evaluation: a critique.
  Carnegie-Rochester Conference Series on Public Policy 1,  pp. 19–46.
  External Links: [Document](https://dx.doi.org/10.1016/S0167-2231%2876%2980003-6)
  Cited by: [§4.3](#S4.SS3.p3.1 "4.3 Intervention coupling: endogenous regime change ‣ 4 The coupling problem"),
  [§5.1](#S5.SS1.p5.1 "5.1 Methodological landscape ‣ 5 Research agenda").
* T. Lux and M. Marchesi (1999)
  Scaling and criticality in a stochastic multi-agent model of a financial market.
  Nature 397,  pp. 498–500.
  External Links: [Document](https://dx.doi.org/10.1038/17290)
  Cited by: [§S3.5](#A3.SS5.p5.1 "S3.5 Adjacent approaches for joint modeling ‣ Appendix S3 Methodological building blocks").
* K. Maciejowska and W. Nitka (2024)
  Multiple split approach: multidimensional probabilistic forecasting of electricity markets.
  arXiv preprint arXiv:2407.07795.
  Cited by: [§S3.5](#A3.SS5.p6.1 "S3.5 Adjacent approaches for joint modeling ‣ Appendix S3 Methodological building blocks").
* J. A. Martín-Fernández, K. Hron, M. Templ, P. Filzmoser, and J. Palarea-Albaladejo (2012)
  Model-based replacement of rounded zeros in compositional data: classical and robust approaches.
  Computational Statistics and Data Analysis 56 (9),  pp. 2688–2704.
  External Links: [Document](https://dx.doi.org/10.1016/j.csda.2012.02.012)
  Cited by: [§S3.1](#A3.SS1.p2.1 "S3.1 Compositional and constrained forecasting ‣ Appendix S3 Methodological building blocks").
* J. A. Martín-Fernández, K. Hron, M. Templ, P. Filzmoser, and J. Palarea-Albaladejo (2015)
  Bayesian-multiplicative treatment of count zeros in compositional data sets.
  Statistical Modelling 15 (2),  pp. 134–158.
  External Links: [Document](https://dx.doi.org/10.1177/1471082X14535524)
  Cited by: [§S3.1](#A3.SS1.p2.1 "S3.1 Compositional and constrained forecasting ‣ Appendix S3 Methodological building blocks").
* T. C. Mills (2010)
  Forecasting compositional time series.
  Quality and Quantity 44 (4),  pp. 673–690.
  External Links: [Document](https://dx.doi.org/10.1007/s11135-009-9229-8)
  Cited by: [§S3.1](#A3.SS1.p2.1 "S3.1 Compositional and constrained forecasting ‣ Appendix S3 Methodological building blocks").
* A. Overwater and N. Yorke-Smith (2022)
  Agent-based simulation of short-term peer-to-peer rentals: evidence from the Amsterdam housing market.
  Environment and Planning B: Urban Analytics and City Science 49 (1),  pp. 223–240.
  External Links: [Document](https://dx.doi.org/10.1177/23998083211000747)
  Cited by: [§S3.5](#A3.SS5.p5.1 "S3.5 Adjacent approaches for joint modeling ‣ Appendix S3 Methodological building blocks"),
  [§5.8](#S5.SS8.p2.1 "5.8 A minimal empirical design ‣ 5 Research agenda").
* V. Pawlowsky-Glahn, J. J. Egozcue, and R. Tolosana-Delgado (2015)
  Modeling and analysis of compositional data.
   Wiley.
  Cited by: [§S3.1](#A3.SS1.p1.1 "S3.1 Compositional and constrained forecasting ‣ Appendix S3 Methodological building blocks"),
  [§S3.1](#A3.SS1.p3.1 "S3.1 Compositional and constrained forecasting ‣ Appendix S3 Methodological building blocks").
* P. Pinson and J. Tastu (2013)
  Discussion of the role of improper scoring rules in energy forecasting.
  International Journal of Forecasting 29 (4),  pp. 689–691.
  Cited by: [§S3.6](#A3.SS6.p3.1 "S3.6 Uncertainty quantification ‣ Appendix S3 Methodological building blocks").
* H. Qu, P. Xu, and A. Tan (2002)
  A simultaneous equations model of the hotel room supply and demand in Hong Kong.
  International Journal of Hospitality Management 21 (4),  pp. 455–462.
  External Links: [Document](https://dx.doi.org/10.1016/S0278-4319%2802%2900031-2)
  Cited by: [§3.3](#S3.SS3.p1.1 "3.3 The supply-side forecasting gap ‣ 3 Platform accommodation markets and the supply-side gap").
* G. Quattrone, A. Greatorex, D. Quercia, L. Capra, and M. Musolesi (2018)
  Analyzing and predicting the spatial penetration of Airbnb in U.S. cities.
  EPJ Data Science 7,  pp. 31.
  External Links: [Document](https://dx.doi.org/10.1140/epjds/s13688-018-0156-6)
  Cited by: [§4.2](#S4.SS2.p4.1 "4.2 Informational coupling: the missing ceiling ‣ 4 The coupling problem").
* J. M. Quintana and M. West (1988)
  Time series analysis of compositional data.
  In Bayesian Statistics 3, J. M. Bernardo, M. H. DeGroot, D. V. Lindley, and A. F. M. Smith (Eds.),
   pp. 747–756.
  Cited by: [§S3.1](#A3.SS1.p3.1 "S3.1 Compositional and constrained forecasting ‣ Appendix S3 Methodological building blocks").
* N. Ravishanker, D. K. Dey, and M. Iyengar (2001)
  Compositional time series analysis of mortality proportions.
  Communications in Statistics: Theory and Methods 30 (11),  pp. 2281–2291.
  External Links: [Document](https://dx.doi.org/10.1081/STA-100107685)
  Cited by: [§S3.1](#A3.SS1.p3.1 "S3.1 Compositional and constrained forecasting ‣ Appendix S3 Methodological building blocks").
* C. Robertson, S. Dejean, and R. Suire (2024)
  Airbnb in the city: assessing short-term rental regulation in Bordeaux.
  The Annals of Regional Science 72 (2),  pp. 647–682.
  External Links: [Document](https://dx.doi.org/10.1007/s00168-023-01215-4)
  Cited by: [§3.2](#S3.SS2.p2.1 "3.2 Platform accommodation: pricing, supply dynamics, and regulation ‣ 3 Platform accommodation markets and the supply-side gap"),
  [§4.3](#S4.SS3.p2.1 "4.3 Intervention coupling: endogenous regime change ‣ 4 The coupling problem").
* J. Rochet and J. Tirole (2003)
  Platform competition in two-sided markets.
  Journal of the European Economic Association 1 (4),  pp. 990–1029.
  External Links: [Document](https://dx.doi.org/10.1162/154247603322493212)
  Cited by: [§1](#S1.p2.1 "1 Introduction"),
  [§3.1](#S3.SS1.p2.1 "3.1 Two-sided foundations ‣ 3 Platform accommodation markets and the supply-side gap"),
  [§4.1](#S4.SS1.p1.1 "4.1 Behavioral coupling: policies propagate across sides ‣ 4 The coupling problem"),
  [§5.1](#S5.SS1.p4.1 "5.1 Methodological landscape ‣ 5 Research agenda").
* J. Rochet and J. Tirole (2006)
  Two-sided markets: a progress report.
  RAND Journal of Economics 37 (3),  pp. 645–667.
  External Links: [Document](https://dx.doi.org/10.1111/j.1756-2171.2006.tb00036.x)
  Cited by: [§3.1](#S3.SS1.p1.1 "3.1 Two-sided foundations ‣ 3 Platform accommodation markets and the supply-side gap"),
  [§3.1](#S3.SS1.p2.1 "3.1 Two-sided foundations ‣ 3 Platform accommodation markets and the supply-side gap").
* Y. Romano, E. Patterson, and E. Candès (2019)
  Conformalized quantile regression.
  In Advances in Neural Information Processing Systems,
  Vol. 32.
  Cited by: [§S3.6](#A3.SS6.p4.1 "S3.6 Uncertainty quantification ‣ Appendix S3 Methodological building blocks"),
  [§5.6](#S5.SS6.p2.1 "5.6 Causal forecasting under unobservable platform intervention ‣ 5 Research agenda").
* D. Salinas, V. Flunkert, J. Gasthaus, and T. Januschowski (2020)
  DeepAR: probabilistic forecasting with autoregressive recurrent networks.
  International Journal of Forecasting 36 (3),  pp. 1181–1191.
  External Links: [Document](https://dx.doi.org/10.1016/j.ijforecast.2019.07.001)
  Cited by: [§S3.5](#A3.SS5.p4.1 "S3.5 Adjacent approaches for joint modeling ‣ Appendix S3 Methodological building blocks"),
  [§2](#S2.p3.1 "2 Tourism demand forecasting since 2019").
* M. Scheuerer and T. M. Hamill (2015)
  Variogram-based proper scoring rules for probabilistic forecasts of multivariate quantities.
  Monthly Weather Review 143,  pp. 1321–1334.
  External Links: [Document](https://dx.doi.org/10.1175/MWR-D-14-00269.1)
  Cited by: [§S3.6](#A3.SS6.p3.1 "S3.6 Uncertainty quantification ‣ Appendix S3 Methodological building blocks").
* Z. Schwartz (1997)
  Monitoring the accuracy of a hotel forecasting system.
  International Journal of Hospitality Management 16 (3),  pp. 325–330.
  External Links: [Document](https://dx.doi.org/10.1016/S0278-4319%2897%2900019-0)
  Cited by: [§S3.2](#A3.SS2.p1.1 "S3.2 Unconstrained demand estimation and demand censoring ‣ Appendix S3 Methodological building blocks").
* R. D. Snyder, J. K. Ord, A. B. Koehler, K. R. McLauren, and A. N. Beaumont (2017)
  Forecasting compositional time series: a state space approach.
  International Journal of Forecasting 33 (2),  pp. 502–512.
  External Links: [Document](https://dx.doi.org/10.1016/j.ijforecast.2016.11.008)
  Cited by: [§S3.1](#A3.SS1.p2.1 "S3.1 Compositional and constrained forecasting ‣ Appendix S3 Methodological building blocks").
* H. Song and G. Li (2008)
  Tourism demand modelling and forecasting—a review of recent research.
  Tourism Management 29 (2),  pp. 203–220.
  External Links: [Document](https://dx.doi.org/10.1016/j.tourman.2007.07.016)
  Cited by: [§1](#S1.p1.1 "1 Introduction"),
  [§5.1](#S5.SS1.p2.1 "5.1 Methodological landscape ‣ 5 Research agenda").
* H. Song, A. Liu, G. Li, and X. Liu (2021)
  Bayesian bootstrap aggregation for tourism demand forecasting.
  International Journal of Tourism Research 23 (5),  pp. 914–924.
  External Links: [Document](https://dx.doi.org/10.1002/jtr.2451)
  Cited by: [§2](#S2.p2.1 "2 Tourism demand forecasting since 2019").
* H. Song, R. T. R. Qiu, and J. Park (2019)
  A review of research on tourism demand forecasting.
  Annals of Tourism Research 75,  pp. 338–362.
  External Links: [Document](https://dx.doi.org/10.1016/j.annals.2018.12.001)
  Cited by: [§1](#S1.SSx1.p5.1 "Notation and forecasting targets ‣ 1 Introduction"),
  [§1](#S1.p1.1 "1 Introduction"),
  [§2](#S2.p1.1 "2 Tourism demand forecasting since 2019"),
  [§5.1](#S5.SS1.p2.1 "5.1 Methodological landscape ‣ 5 Research agenda").
* S. Sun, Y. Wei, K. Tsui, and S. Wang (2019)
  Forecasting tourist arrivals with machine learning and internet search index.
  Tourism Management 70,  pp. 1–10.
  External Links: [Document](https://dx.doi.org/10.1016/j.tourman.2018.07.010)
  Cited by: [Appendix S1](#A1.p2.1 "Appendix S1 Measurement and data sources"),
  [§2](#S2.p4.2 "2 Tourism demand forecasting since 2019"),
  [§5.2](#S5.SS2.p1.2 "5.2 The search-to-booking gap as a supply constraint signal ‣ 5 Research agenda").
* K. T. Talluri and G. J. van Ryzin (2004)
  The theory and practice of revenue management.
   Springer.
  Cited by: [§S3.2](#A3.SS2.p1.1 "S3.2 Unconstrained demand estimation and demand censoring ‣ Appendix S3 Methodological building blocks"),
  [§5.1](#S5.SS1.p3.1 "5.1 Methodological landscape ‣ 5 Research agenda").
* A. Timmermann (2006)
  Forecast combinations.
  In Handbook of Economic Forecasting, G. Elliott, C. W. J. Granger, and A. Timmermann (Eds.),
  Vol. 1,  pp. 135–196.
  External Links: [Document](https://dx.doi.org/10.1016/S1574-0706%2805%2901004-9)
  Cited by: [§2](#S2.p2.1 "2 Tourism demand forecasting since 2019").
* J. Tobin (1958)
  Estimation of relationships for limited dependent variables.
  Econometrica 26 (1),  pp. 24–36.
  External Links: [Document](https://dx.doi.org/10.2307/1907382)
  Cited by: [§4.2](#S4.SS2.p3.6 "4.2 Informational coupling: the missing ceiling ‣ 4 The coupling problem").
* M. C. Tsai, B. Kang, R. J. Yeh, and E. Suh (2006)
  Examining the hotel room supply and demand in Las Vegas: a simultaneous equations model.
  International Journal of Hospitality Management 25 (3),  pp. 517–524.
  External Links: [Document](https://dx.doi.org/10.1016/j.ijhm.2005.01.004)
  Cited by: [§3.3](#S3.SS3.p1.1 "3.3 The supply-side forecasting gap ‣ 3 Platform accommodation markets and the supply-side gap").
* E. Vinogradov, B. Leick, and B. K. Kivedal (2020)
  An agent-based modelling approach to housing market regulations and Airbnb-induced tourism.
  Tourism Management 77,  pp. 104004.
  External Links: [Document](https://dx.doi.org/10.1016/j.tourman.2019.104004)
  Cited by: [§S3.5](#A3.SS5.p5.1 "S3.5 Adjacent approaches for joint modeling ‣ Appendix S3 Methodological building blocks").
* Y. Wang, M. Livingston, D. McArthur, and N. Bailey (2024)
  Enhancing our understanding of short-term rental activity: a daily scrape-based approach for Airbnb listings.
  PLOS ONE.
  External Links: [Document](https://dx.doi.org/10.1371/journal.pone.0298131)
  Cited by: [Appendix S1](#A1.p1.4 "Appendix S1 Measurement and data sources"),
  [§3.3](#S3.SS3.p2.1 "3.3 The supply-side forecasting gap ‣ 3 Platform accommodation markets and the supply-side gap"),
  [§5.8](#S5.SS8.p3.1 "5.8 A minimal empirical design ‣ 5 Research agenda").
* L. R. Weatherford and S. E. Bodily (1992)
  A taxonomy and research overview of perishable-asset revenue management.
  Operations Research 40 (5),  pp. 831–844.
  External Links: [Document](https://dx.doi.org/10.1287/opre.40.5.831)
  Cited by: [§S3.2](#A3.SS2.p1.1 "S3.2 Unconstrained demand estimation and demand censoring ‣ Appendix S3 Methodological building blocks").
* E. G. Weyl (2010)
  A price theory of multi-sided platforms.
  American Economic Review 100 (4),  pp. 1642–1672.
  External Links: [Document](https://dx.doi.org/10.1257/aer.100.4.1642)
  Cited by: [§1](#S1.p2.1 "1 Introduction"),
  [§3.1](#S3.SS1.p2.1 "3.1 Two-sided foundations ‣ 3 Platform accommodation markets and the supply-side gap"),
  [§5.1](#S5.SS1.p4.1 "5.1 Methodological landscape ‣ 5 Research agenda").
* Y. Yang, C. X. Zhang, and J. M. Rickly (2021)
  A review of early COVID-19 research in tourism.
  Tourism Management 87,  pp. 104405.
  External Links: [Document](https://dx.doi.org/10.1016/j.tourman.2021.104405)
  Cited by: [§S3.4](#A3.SS4.p4.1 "S3.4 Regime change and structural breaks ‣ Appendix S3 Methodological building blocks").
* A. Zellner and H. Theil (1962)
  Three-stage least squares: simultaneous estimation of simultaneous equations.
  Econometrica 30 (1),  pp. 54–78.
  External Links: [Document](https://dx.doi.org/10.2307/1911287)
  Cited by: [§S3.5](#A3.SS5.p2.1 "S3.5 Adjacent approaches for joint modeling ‣ Appendix S3 Methodological building blocks"),
  [§5.3](#S5.SS3.p2.1 "5.3 Demand forecasting under an endogenous supply ceiling ‣ 5 Research agenda").
* G. Zervas, D. Proserpio, and J. W. Byers (2017)
  The rise of the sharing economy: estimating the impact of Airbnb on the hotel industry.
  Journal of Marketing Research 54 (5),  pp. 687–705.
  External Links: [Document](https://dx.doi.org/10.1509/jmr.15.0204)
  Cited by: [§1](#S1.p2.1 "1 Introduction"),
  [§3.2](#S3.SS2.p1.1 "3.2 Platform accommodation: pricing, supply dynamics, and regulation ‣ 3 Platform accommodation markets and the supply-side gap"),
  [§4.2](#S4.SS2.p4.1 "4.2 Informational coupling: the missing ceiling ‣ 4 The coupling problem").
* Y. Zhang, G. Li, B. Muskat, R. Law, and Y. Yang (2021)
  Tourism demand forecasting: a decomposed deep learning approach.
  Journal of Travel Research 60 (5),  pp. 981–997.
  External Links: [Document](https://dx.doi.org/10.1177/0047287520919522)
  Cited by: [§2](#S2.p3.1 "2 Tourism demand forecasting since 2019").
* T. Zheng and R. Chen (2017)
  Dirichlet ARMA models for compositional time series.
  Journal of Multivariate Analysis 158,  pp. 31–46.
  External Links: [Document](https://dx.doi.org/10.1016/j.jmva.2017.03.006)
  Cited by: [§S3.1](#A3.SS1.p3.1 "S3.1 Compositional and constrained forecasting ‣ Appendix S3 Methodological building blocks").

BETA