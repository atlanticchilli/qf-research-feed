---
authors:
- Adrian Odenweller
- Falko Ueckerdt
- Johannes Hampp
- Ivan Ramirez
- Felix Schreyer
- Robin Hasse
- Jarusch Muessel
- Chen Chris Gong
- Robert Pietzcker
- Tom Brown
- Gunnar Luderer
doc_id: arxiv:2510.04388v1
family_id: arxiv:2510.04388
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'REMIND-PyPSA-Eur: Integrating power system flexibility into sector-coupled
  energy transition pathways'
url_abs: http://arxiv.org/abs/2510.04388v1
url_html: https://arxiv.org/html/2510.04388v1
venue: arXiv q-fin
version: 1
year: 2025
---


Adrian Odenweller

Falko Ueckerdt

Johannes Hampp

Ivan Ramirez

Felix Schreyer

Robin Hasse

Jarusch Müßel

Chen Chris Gong

Robert Pietzcker

Tom Brown

Gunnar Luderer

###### Abstract

The rapid expansion of low-cost renewable electricity combined with end-use electrification in transport, industry, and buildings offers a promising path to deep decarbonisation. However, aligning variable supply with demand requires strategies for daily and seasonal balancing. Existing models either lack the wide scope required for long-term transition pathways or the spatio-temporal detail to capture power system variability and flexibility. Here, we combine the complementary strengths of REMIND, a long-term integrated assessment model, and PyPSA-Eur, an hourly energy system model, through a bi-directional, price-based and iterative soft coupling. REMIND provides pathway variables such as sectoral electricity demand, installed capacities, and costs to PyPSA-Eur, which returns optimised operational variables such as capacity factors, storage requirements, and relative prices. After sufficient convergence, this integrated approach jointly optimises long-term investment and short-term operation. We demonstrate the coupling for two Germany-focused scenarios, with and without demand-side flexibility, reaching climate neutrality by 2045. Our results confirm that a sector-coupled energy system with nearly 100% renewable electricity is technically possible and economically viable. Power system flexibility influences long-term pathways through price differentiation: supply-side market values vary by generation technology, while demand-side prices vary by end-use sector. Flexible electrolysers and smart-charging electric vehicles benefit from below-average prices, whereas less flexible heat pumps face almost twice the average price due to winter peak loads. Without demand-side flexibility, electricity prices increase across all end-users, though battery deployment partially compensates. Our approach therefore fully integrates power system dynamics into multi-decadal energy transition pathways.

Keywords: Integrated Assessment Modelling, Energy System Modelling, Power System Modelling, Transformation Pathways, Climate Mitigation Scenarios, Demand-side Management

## 1 Introduction

### 1.1 Background

Limiting global warming in line with the targets of the Paris Agreement requires a fundamental transition of the global energy system towards low-carbon energy sources[ipccClimateChange20222022, davisNetzeroEmissionsEnergy2018]. With plummeting costs and record growth of variable renewable energy (VRE) sources such as solar photovoltaics (PV) and wind power, renewable electricity is emerging as a central pillar to achieve a deep decarbonisation of the energy system[ieaWorldEnergyOutlook2024, ludererImpactDecliningRenewable2022]. In most parts of the world, renewables now have a lower levelised cost of electricity (LCOE) than the cheapest fossil fuel alternative[irenaRenewablePowerGeneration2025]. Simultaneously, rapid cost declines and unprecedented deployment of battery energy storage systems facilitate further integration of VREs[mallapragadaLongrunSystemValue2020]. As a result, global solar PV generation has doubled within just three years[emberGlobalElectricityReview2025]. Encouraged by these developments, at the 28th United Nations Climate Change Conference (COP28) the international community formalised the goal to triple global renewable energy capacity by 2030 as part of the UAE Consensus[unfcccReportConferenceParties2024], an ambition the International Energy Agency (IEA) has described as the “single most important lever to bring about the reduction in carbon dioxide (CO2) emissions needed by 2030”[ieaTriplingRenewablePower2023].

To achieve energy system decarbonisation, flexible end-use electrification is critical for cost-effective VRE integration. This increased linking of electricity supply with new electricity demands – referred to as sector coupling[ramsebnerSectorCouplingConcept2021] – involves meeting energy service demands across the transport, buildings and industry sectors as well as power-to-molecule conversion through renewable electricity. Although electricity currently accounts for only one-fifth of global final energy consumption[ieaWorldEnergyBalances2024], virtually all space heating and cooling[thomassenDecarbonisationEUHeating2021, rosenowHeatingGlobalHeat2022] and the majority of industrial processes[madedduCO2ReductionPotential2020, rosenowOpportunitiesHeatElectrification2025] can be electrified. With ongoing improvements in battery technologies, road transport is also set for widespread electrification, not just for passengers cars[hoekstraUnderestimatedPotentialBattery2019] but also for freight transport[linkRapidlyDecliningCosts2024]. Electricity is therefore positioned to become the dominant energy carrier in a future energy system. This trend becomes even more important as competing emissions abatement options continue to face challenges, exemplified by the sluggish deployment and high costs of carbon capture and storage[kazlouFeasibleDeploymentCarbon2024] and green hydrogen[odenwellerGreenHydrogenAmbition2025], as well as sustainability concerns about large-scale bioenergy use[jiaLandClimateInteractions2019]. However, sector coupling also leads to considerable operational and planning challenges for future power systems.

### 1.2 Challenges for power systems and long-term models

With increasingly high shares of VRE sources and newly electrified end-use sectors, maintaining the balance between supply and demand at each location and time becomes increasingly challenging[zhengStrategiesClimateresilientGlobal2025]. Weather-dependent renewable generation creates periods of both surplus and scarcity, including extended low-wind, low-solar periods known as “Dunkelflaute” that can last several days or weeks[kittelMeasuringDunkelflauteHow2024]. However, the electrification of transport through electric vehicles[schillPowerSystemImpacts2015], buildings via heat pumps[bloessPowertoheatRenewableEnergy2018], industry[rosenowOpportunitiesHeatElectrification2025] as well as flexible electrolysers[ruhnauHowFlexibleElectricity2022] also introduces new demand patterns that offer unprecedented opportunities for demand-side management and system flexibility. Successfully harnessing these flexibility potentials, combined with energy storage[victoriaRoleStorageTechnologies2019, schillElectricityStorageRenewable2020], transmission grid expansion[brownSynergiesSectorCoupling2018], and dispatchable backup capacity[sepulvedaRoleFirmLowCarbon2018], is essential to ensure reliable electricity supply while maximising both the integration of VREs and the electrification of end-uses.

The challenges and opportunities of flexible power systems are not well represented in long-term integrated assessment models (IAMs) that are regularly used to inform policymakers about national, regional and global energy transition pathways for mitigating climate change. Fundamentally, due to numerical complexity, models cannot have both (i) the wide scope required for cross-sectoral long-term mitigation scenarios (modelled in IAMs) as well as (ii) the high spatio-temporal detail required for power systems operations (modelled in Energy System Models, ESMs)[ringkjobReviewModellingTools2018]. This creates an inherent trade-off: Models that capture global economic interactions and multi-decadal transition dynamics across all sectors necessarily sacrifice the spatial and temporal resolution required to represent hourly power system dynamics. Vice versa, models that provide high spatio-temporal detail typically focus on shorter time horizons on a regional scope. Yet, developing robust transformation pathways requires bridging these scales in order to combine long-term planning with short-term operations, thereby leveraging the complementary strengths of IAMs and ESMs (Figure [1](https://arxiv.org/html/2510.04388v1#S1.F1 "Figure 1 ‣ 1.2 Challenges for power systems and long-term models ‣ 1 Introduction ‣ REMIND-PyPSA-Eur: Integrating power system flexibility into sector-coupled energy transition pathways")).

![Refer to caption](x1.png)


Figure 1: Complementary strengths of the Integrated Assessment Model REMIND and the Energy System Model PyPSA-Eur (stylised). REMIND features a wide scope, providing intertemporally optimal transformation pathways over several decades for all economic sectors, but has a low spatio-temporal resolution. PyPSA-Eur features high granularity, enabling a detailed analysis of storage, transmission and infrastructure, but is constrained in temporal and regional scope.

IAMs like REMIND capture the broad scope and long-term perspective required for climate policy analysis by covering all greenhouse gases including energy, land and carbon dioxide removal (CDR) options and all energy sectors, linked to a representation of the macro-economy, within a global scope. This comprehensive approach enables exploration of cross-sectoral transformation scenarios until the end of the century, subject to different global and regional climate targets and policies. However, as IAMs have a very low spatio-temporal resolution they cannot represent hourly power system dynamics explicitly.

ESMs like PyPSA-Eur feature strengths that are mostly complementary to IAMs, particularly high spatio-temporal detail. This enables endogenous optimisation of dispatch, investment, storage, transmission, and demand-side flexibility for future power systems. However, due to the associated numerical complexity, ESMs typically run at a country or regional level for a single future target year or employ myopic pathway optimisation without the interdecadal foresight essential for long-term planning. Moreover, demand is typically price-inelastic and fuel costs are exogenous.

### 1.3 Previous approaches for representing power systems in long-term models

Various approaches have been developed in recent studies to bridge these scales by enhancing the modelling of short-term power system variations in long-term models. These can be split into (i) approaches that are based on simplified parametrisations of power system dynamics in long-term models and (ii) approaches that establish a soft-link between long-term and short-term models with varying levels of integration. An overview of the strengths and challenges of different approaches is available in [collinsIntegratingShortTerm2017].

Early versions of simplified parametrisations often relied on exogenous assumptions for critical variables such as backup capacities[sullivanImpactsConsideringElectric2013], with some approaches even imposing hard upper bounds for VREs[pietzckerSystemIntegrationWind2017]. Alternative approaches used representative days or integration costs, inspired by the system LCOE concept[ueckerdtSystemLCOEWhat2013], in order to represent the economic costs of variability[hirthIntegrationCostsRevisited2015]. A concerted effort within the ADVANCE project in 2017[ludererAssessmentWindSolar2017] led to the widespread adoption of residual load duration curves (RLDCs) across IAMs. These RLDCs were based on hourly ESM results and parametrised for 8 world regions[ueckerdtDecarbonizingGlobalPower2017]. Their integration into IAMs led to a dramatic increase of VREs in scenarios, from 38% to 62% on average, highlighting the critical role of appropriately representing variability in long-term models[pietzckerSystemIntegrationWind2017]. More recently, this line of research has been reinvigorated by [gotskeFirstStepsBridging2025], who use the sector-coupled PyPSA-Eur model to analyse the effect of imposed VRE shares on key power system metrics, an approach introduced in earlier studies[ueckerdtDecarbonizingGlobalPower2017, scholzApplicationHighdetailEnergy2017]. However, these reduced-form approaches only address supply-side variability, but often neglect demand-side flexibility.

In order to address these shortcomings, several studies have contributed towards soft-linking long-term energy models with short-term ESMs, ranging from unidirectional, to manual bidirectional, to automated bidirectional approaches (Table [1.3](https://arxiv.org/html/2510.04388v1#S1.SS3 "1.3 Previous approaches for representing power systems in long-term models ‣ 1 Introduction ‣ REMIND-PyPSA-Eur: Integrating power system flexibility into sector-coupled energy transition pathways")). However, key research gaps remain. First, the majority of approaches are either unidirectional (no feedback) or require manual bidirectional coupling with typically only a single iteration, limiting the ability of fully combining long-term planning with short-term operations. Second, most studies have a limited temporal scope and resolution, coupling only a few selected years and often using rolling horizons instead of full foresight. Third, most studies only use a single aggregated demand profile, precluding the critical analysis of evolving demand patterns from ongoing end-use electrification. Fourth, only very few studies model demand-side flexibility, or limit flexibility to electrolysers. Fifth, all studies except [gongBidirectionalCouplingLongterm2023] only import selected parameters, often related to backup capacities, from the ESM into the long-term model, whereas full model harmonisation requires a comprehensive parameter exchange. Lastly, so far, no study has incorporated a price-based coupling for both the supply side and the demand side, which is crucial to fully integrate the impact of hourly power system economics into long-term investment decisions.

Table 1: Review of soft-coupling approaches between long-term models and short-term energy system models.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | Power system modelling | | | |
| Publication | Long-term model | Short-term ESM | Coupling scope | Long-term model to ESMa | ESM to long-term modelb | Resolution & foresight | Electricity storage | Sectoral demandc | Demand flexibility |
| Unidirectional coupling | | | | | | | | | |
| [deaneSoftlinkingPowerSystems2012] (\citeyeardeaneSoftlinkingPowerSystems2012) [deaneSoftlinkingPowerSystems2012] | TIMES | PLEXOS | Ireland; 2020 | Total demand, capacities, costs | - | 1 node;   30-min (1-day RH) | PHS | - | - |
| [deaneAssessingPowerSystem2015] (\citeyeardeaneAssessingPowerSystem2015) [deaneAssessingPowerSystem2015] | TIMES (MONET) | PLEXOS | Italy; 2030 | Total demand, capacities, costs, intra-regional trade | - | 6 nodes; hourly (foresight ?) | PHS | - | - |
| [collinsAddingValueEU2017] (\citeyearcollinsAddingValueEU2017) [collinsAddingValueEU2017] | PRIMES | PLEXOS | EU-28; 2030 | Total demand, capacities, costs, VRE CFs | - | 28 countries (nodes ?);   hourly (foresight ?) | PHS | - | Stylised (10% peak intra-day) |
| [pavicevicPotentialSectorCoupling2020] (\citeyearpavicevicPotentialSectorCoupling2020) [pavicevicPotentialSectorCoupling2020] | JRC-EU-TIMES | Dispa-SET | EU-28; 2050 | Sectoral demand, capacities, costs | - | 28 nodes;   hourly (1-day RH) | PHS, BESS, V2G | EVs, heating | EVs, heating |
| [younisScrutinizingIntermittencyRenewable2022] (\citeyearyounisScrutinizingIntermittencyRenewable2022) [younisScrutinizingIntermittencyRenewable2022] | TIMES-CO-BBE | PowerPlan (simulation) | Colombia; 2050 | Total demand, capacities, costs | - | 5 zones; hourly (no optimisation) | - | - | - |
| [beresWillHydrogenSynthetic2024] (\citeyearberesWillHydrogenSynthetic2024) [beresWillHydrogenSynthetic2024] | JRC-EU-TIMES | PLEXOS | EU-27; 2050 | Sectoral demand, costs, max. CCS/bio | - | 27 nodes;   hourly (foresight ?) |  |  |  |