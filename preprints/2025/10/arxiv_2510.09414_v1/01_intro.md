---
authors:
- Michael Lindner
- Julian Geis
- Toni Seibold
- Tom Brown
doc_id: arxiv:2510.09414v1
family_id: arxiv:2510.09414
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'PyPSA-DE: Open-source German energy system model reveals savings from integrated
  planning'
url_abs: http://arxiv.org/abs/2510.09414v1
url_html: https://arxiv.org/html/2510.09414v1
venue: arXiv q-fin
version: 1
year: 2025
---


Michael Lindner, Julian Geis, Toni Seibold, Tom Brown

###### Abstract

Germany has set an ambitious target of reaching net zero greenhouse gas emissions by 2045. We explore how integrated cross-sectoral planning can reduce costs compared to existing national plans. Our new linear optimization model PyPSA-DE simulates the electricity and hydrogen transmission networks, as well as supply, demand, and storage in all sectors of the energy system in Germany and its neighboring countries with high spatial and temporal resolution.
While our new model shows strong electricity transmission grid development, total expansion is one third lower than in the national grid development plan, lowering costs by 92 billion €2020 to 191 billion €2020 and average grid tariffs by 7.5 €2020 / MWh.
These savings are mainly due to integrated planning and operation, a market design with regional prices, and a system-optimal usage of offshore wind.
PyPSA-DE is open-source and can readily be adapted to study related issues around the energy transition.

††publicationid: pubid: 

979-8-3315-1278-1/25/$31.00 © 2025 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses, in any current or future media, including reprinting/republishing this material for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of this work in other works. DOI: 10.1109/EEM64765.2025.11050093

## I Introduction

Germany has set an ambitious target of reaching net zero emissions by 2045. This long-term commitment is underpinned by laws addressing specific sectors of the energy system, such as build-out targets for renewable energy sources (RES), the phase-out of coal power, a ban on fossil boilers in individual heating, investments into a new hydrogen transmission grid and ambitious plans for power grid expansion, to name just a few. While the implemented measures are projected by the German federal environmental agency (UBA) to significantly reduce emissions, they are not deemed sufficient to reach net-zero [[1](https://arxiv.org/html/2510.09414v1#bib.bibx1)].
Against this backdrop we have developed PyPSA-DE - the first open-source cross-sectoral high-resolution model of the German energy system. It allows for an integrated planning of the whole energy system, uncovering synergies arising from sector-coupling that may help to achieve climate neutrality in a cost-optimal way. While the model already represents a wide-range of policies and technology options, the fully open-source publication of its input data and modeling workflow ensures that it can be readly adapted by diverse actors to study the impact of new political interventions or technological innovations. In this conference paper, the default modeling assumptions of PyPSA-DE are outlined and selected modeling results and their implications for the German energy transition are discussed.

## II Methods

We developed PyPSA-DE on the basis of the widely used European energy system model PyPSA-Eur [[2](https://arxiv.org/html/2510.09414v1#bib.bibx2), [3](https://arxiv.org/html/2510.09414v1#bib.bibx3), [4](https://arxiv.org/html/2510.09414v1#bib.bibx4)] to resolve the German system in high spatial, temporal and sectoral detail. PyPSA-DE simulates supply, demand, storage and transmission networks to cover energy and non-energy demand in the electricity, heating, transport, agriculture, waste and industry sectors. In 5-year steps with myopic foresight from 2020 to 2045, PyPSA-DE builds a linear optimization problem to minimize total system costs of the energy system infrastructure in Germany and its neighboring countries, with variable spatial and temporal resolution across full weather years. Among other things, PyPSA-DE computes a cost-optimal allocation of renewables in regional scope, cross-border trade of electricity and renewable fuels, expansion of hydrogen and electricity networks, and adaptation of different heating and thermal energy storage technologies in district as well as individual heating. The grid is modeled with an optimal linearized power flow with piecewise linear losses, an approach found to agree well with the full load flow calculation [[5](https://arxiv.org/html/2510.09414v1#bib.bibx5)]. The base networks is extracted from openstreetmaps and validated against official data [[6](https://arxiv.org/html/2510.09414v1#bib.bibx6)].

The new model PyPSA-DE implements Germany-specific policies such as the nuclear and coal phase-out laws, or the net-zero target for 2045, as well as EU-wide regulations and CO2 emissions budgets. PyPSA-DE augments the PyPSA-EUR dataset with several Germany-specific data sources, including the national grid development plans for electricity [[7](https://arxiv.org/html/2510.09414v1#bib.bibx7)] and hydrogen [[8](https://arxiv.org/html/2510.09414v1#bib.bibx8)], and the register of power and gas units in Germany [[9](https://arxiv.org/html/2510.09414v1#bib.bibx9)].
Furthermore, the model has been validated against historical data of the German electricity system for 2020.
While PyPSA-DE can be configured in many different ways, the results discussed in this article were obtained for a net-zero scenario, with 3-hourly resolution and 49 regions (30 regions for Germany, and 19 regions for the European neighbors).

## III Results

### III-A Expansion of renewable energy sources and CO2 emissions.

The model results indicate that the electricity sector, will become the backbone of the future energy system in Germany, and that the electricity supply will be dominated by renewable energy sources (RES). These are predominantly expanded where the expected yields are highest, e.g., for onshore wind in the North of Germany, see [Figure 1](https://arxiv.org/html/2510.09414v1#S3.F1 "In III-A Expansion of renewable energy sources and CO2 emissions. ‣ III Results ‣ PyPSA-DE: Open-source German energy system model reveals savings from integrated planning"). Only after land use constraints are hit for that technology, are less profitable sites in the South utilized. Average wholesale electricity prices are expected to slightly decrease from their current high point and to stabilize from 2030 onwards at around 80€/MWh. The total investment needs for the German electricity system in the period 2025-2045 exceed 730 billion €2020, of which the largest share (around 60%, or 425 billion €2020) goes to the expansion of wind and solar, followed by investments into the transmission grid, which total 191 billion €2020 in PyPSA-DE. A detailed representation of the electricity distribution grid is outside the scope of the model, but recent studies estimate investment needs of a magnitude similar to that of the transmission grid [[10](https://arxiv.org/html/2510.09414v1#bib.bibx10), [11](https://arxiv.org/html/2510.09414v1#bib.bibx11)], so that the real total will be even greater than 730 billion euros2020.

![Refer to caption](elec-transmission-DE-total-expansion-2045_eng.png)


Figure 1: Installed capacities of renewable energy sources (RES) and batteries, and transmission grid expansion for the year 2045 using historical weather data from 2019. Offshore wind is shown at its grid connection point. The installed capacities follow the renewable potential, with onshore wind found predominantly in the North and solar power found predominantly in the South.

### III-B Backup generation and flexibility.

[Figure 2](https://arxiv.org/html/2510.09414v1#S3.F2 "In III-B Backup generation and flexibility. ‣ III Results ‣ PyPSA-DE: Open-source German energy system model reveals savings from integrated planning") shows an example electricity balance of the decarbonized energy system in 2045 for the month of January, which contains a period with low RES generation. During this week-long event the backup power plants (68 GW of hydrogen and 19 GW of older unabated natural gas plants) are running at capacity, supplemented by power imports from the neighboring countries. In general, the integration into the European electricity system proves to be vital for balancing, with gross electricity exchange exceeding by far the net imports. During the low-RES event the production of hydrogen, which usually absorbs the excess power in wind-rich periods, is halted. Aside from providing temporal flexibility to the system, the electrolysis in Germany has another vital role, namely integrating offshore wind energy, without the need for expensive underground DC cables111Cheaper, overhead DC cables have faced considerable public opposition, such that, the German parliament mandated that all future DC project shall be underground.. As a consequence the electrolysis is predominantly situated near the coast.

![Refer to caption](x1.png)


Figure 2: Electricity balance for the month of January for the year 2045. During the event of low renewable energy generation (19th to 26th), hydrogen and gas backup power plants step in, supplemented by electricity imports.

Using the methodology of Artelys [[12](https://arxiv.org/html/2510.09414v1#bib.bibx12)] we can assess the flexibility needs at different time scales (daily and weekly). The methodology works by quantifying deviations of the residual load from means taken over periods of different lengths, then adjusting the residual load by the contribution of each flexibility technology. Taking the daily flexibility as an example, the positive deviation of the residual load from its daily average is quantified, then as the contribution of batteries or demand-side management is added to the residual load, the deviation is measured again. Eventually once all technologies are considered, the residual load drops to zero, since the system is balanced, and the exercise is complete.

[Figure 6](https://arxiv.org/html/2510.09414v1#Ax1.F6 "In Additional figures ‣ PyPSA-DE: Open-source German energy system model reveals savings from integrated planning") shows which flexibility resources provide this flexibility. At the daily scale the needs rise by a factor 10 betweeen 2020 and 2045, primarily to integrate solar fluctuations, and are met by a mix of electric vehicle charging management and stationary batteries. At the weekly scale the needs grow by a factor 5, supplied mainly by trade and electrolysis.

### III-C Integrated planning with regional prices saves on transmission costs.

While the model shows strong transmission grid development, especially in the period 2025-2035, it identifies the potential to reduce grid development by up to one third compared to the national grid development plan (NDP) [[7](https://arxiv.org/html/2510.09414v1#bib.bibx7)], lowering costs by 92 billion €2020 to 191 billion €2020. These savings are mainly due to a fully integrated planning and operation, which promotes the system-friendly location and dispatch of flexibility technologies like electrolysis and utility-scale batteries, as well as due to cost-optimal usage of offshore wind resources and regional price zones. While the NDP expands the grid to remove congestion arising from the market dispatch of a single bidding zone, leading to substantial grid expansion, we use regional prices to manage congestion within Germany. Regional prices help the system to dispatch local assets to manage congestion, leading to less expansion as well as congestion rents that lower the grid tariffs charged to consumers. Furthermore regional prices allow the market to guide the electrolysis capacities to the coast, where they can absorb offshore wind power (see [Figure 3](https://arxiv.org/html/2510.09414v1#S3.F3 "In III-C Integrated planning with regional prices saves on transmission costs. ‣ III Results ‣ PyPSA-DE: Open-source German energy system model reveals savings from integrated planning")) - a result that was also found by [[13](https://arxiv.org/html/2510.09414v1#bib.bibx13)].

The lower grid development reduces grid tariffs by 7.5 €/MWh on average compared to the NDP plan. Due to the regional prices, there are variations in the wholesale price from region to region, but because of the lower grid tariffs, the end consumer prices reduce in all regions, varying from 3.5 €/MWh in the south down to 14.2 €/MWh in the north near the coast (see [Figure 4](https://arxiv.org/html/2510.09414v1#S3.F4 "In III-C Integrated planning with regional prices saves on transmission costs. ‣ III Results ‣ PyPSA-DE: Open-source German energy system model reveals savings from integrated planning")). A recent study on locational prices in GB led to a similar conclusion, finding lower consumer prices in all regions [[14](https://arxiv.org/html/2510.09414v1#bib.bibx14)].

As a linear model, PyPSA-DE has to make certain simplifying assumptions, e.g., the complete, non-linear load flow is approximated with a linear load flow, with piecewise linear losses [[5](https://arxiv.org/html/2510.09414v1#bib.bibx5)]. The linear load flow is solved with a computationally efficient cycle-based formulation [[15](https://arxiv.org/html/2510.09414v1#bib.bibx15)], implemented in the python package PyPSA [[16](https://arxiv.org/html/2510.09414v1#bib.bibx16)]. Furthermore, based on [[17](https://arxiv.org/html/2510.09414v1#bib.bibx17)], the N−1N-1 criterium is approximated by restricting the maximal line loading to 70%. New lines are not build as discrete units, but optimized continuously and discretized in a further step as soon as a certain maximum loading is exceeded [[5](https://arxiv.org/html/2510.09414v1#bib.bibx5)]. Because of such simplifications, our model is not a substitute for the full grid planning of the network operators, but it is indicative how an integrated planning approach with regional price signals can reduce costs.

![Refer to caption](h2_transmission_DE_production_2045_eng.png)

![Refer to caption](h2_transmission_DE_consumption_2045_eng.png)

Figure 3: Expansion of the hydrogen grid until 2045, shown together with locations of H2 production (left) and H2 demand (right). The electrolysis is placed primarily near the coastline to help with the integration of offshore wind resources and thus save on expensive DC projects.

![Refer to caption](x2.png)


Figure 4: Comparison of the average wholesale electricity price plus average grid tariffs in 2045. Left: scenario with a single bidding zone and grid expansion according to the national grid development plan (NEP), Right: scenario with regional price zones and reduced grid development according to PyPSA-DE. In the PyPSA scenario all end users benefit from a lower average electricity price, despite price differences between the regional zones.

### III-D Hydrogen infrastructure.

Next to the expansion of the electricity grid, the model constructs a hydrogen pipeline network that connects electrolysis, hydrogen imports from neighboring countries and large-scale consumers in the industry sector, as well as in e-fuel production and backup power generation. Following the approach in [[3](https://arxiv.org/html/2510.09414v1#bib.bibx3)] pipelines are modeled as linear transport links, without explicit consideration of gas flow physics. We find that the official network development plans [[8](https://arxiv.org/html/2510.09414v1#bib.bibx8)] are sufficient for the transport demand in 2045. Even a hydrogen network with less transport capacity might be enough to serve a comparatively low total hydrogen demand of 191 TWh, unlocking potential cost savings. In particular, with 130 TWh, the largest share of hydrogen is produced domestically, highlighting the importance of electrolysis for the electricity system, which serves as a source of flexibility (see [Figure 6](https://arxiv.org/html/2510.09414v1#Ax1.F6 "In Additional figures ‣ PyPSA-DE: Open-source German energy system model reveals savings from integrated planning")) and helps integrate offshore wind resources (see [Figure 3](https://arxiv.org/html/2510.09414v1#S3.F3 "In III-C Integrated planning with regional prices saves on transmission costs. ‣ III Results ‣ PyPSA-DE: Open-source German energy system model reveals savings from integrated planning")).

## IV Conclusion

Until now much of the energy system planning has been done in separate silos for electricity, natural gas and hydrogen. By pursuing an integrated cross-sectoral planning approach, as well as considering changes to the market structure like regional pricing, we were able to identify significant cost savings. Regional prices allow the system to manage congestion with flexibility, electrolysers can be placed at the coast to absorb offshore wind, and many of the planned long HVDC cables from North to South can be avoided.

By publishing our model online under an open-source license [[18](https://arxiv.org/html/2510.09414v1#bib.bibx18)] we hope to inspire its further use by other researchers. It is already being adapted to study further pressing topics of the Germany energy transition, e.g., the impact of decarbonization on the industry sector, price-formation in an all-renewable energy system, and the benefits of thermal energy storage. Furthermore, it may serve as a prototype for building similar country specific open-source models within Europe on the basis of PyPSA-Eur. In the context of the Ariadne project, PyPSA-DE is provides an important independent contribution to research on German energy policy [[19](https://arxiv.org/html/2510.09414v1#bib.bibx19)].

## References

* [1]
  Ralph O. Harthan et al.
  “Technischer Anhang der Treibhausgas-Projektionen 2024 für Deutschland (Projektionsbericht 2024)”, Treibhausgas-Projektionen für Deutschland, 2024, pp. 303
  URL: <https://www.umweltbundesamt.de/publikationen/technischer-anhang-der-treibhausgas-projektionen>
* [2]
  Jonas Hoersch, Fabian Hofmann, David Schlachtberger and Tom Brown
  “PyPSA-Eur: An open optimisation model of the European transmission system”
  In *Energy Strategy Reviews* 22, 2018, pp. 207–215
  DOI: [10.1016/j.esr.2018.08.012](https://dx.doi.org/10.1016/j.esr.2018.08.012)
* [3]
  Fabian Neumann, Elisabeth Zeyen, Marta Victoria and Tom Brown
  “The potential role of a hydrogen network in Europe”
  In *Joule* 7, 2023, pp. 1–25
  DOI: [10.1016/j.joule.2023.06.016](https://dx.doi.org/10.1016/j.joule.2023.06.016)
* [4]
  Marta Victoria, Elisabeth Zeyen and Tom Brown
  “Speed of technological transformations required in Europe to achieve different climate goals”
  In *Joule* 6.5, 2022, pp. 1066–1086
  DOI: [10.1016/j.joule.2022.04.016](https://dx.doi.org/10.1016/j.joule.2022.04.016)
* [5]
  Fabian Neumann, Veit Hagenmeyer and Tom Brown
  “Assessments of linear power flow and transmission loss approximations in coordinated capacity expansion problems”
  In *Applied Energy* 314
  Elsevier, 2022, pp. 118859
* [6]
  Bobby Xiong et al.
  “Modelling the high-voltage grid using open data for Europe and beyond”
  In *Scientific Data* 12.1
  Nature Publishing Group, 2025, pp. 1–22
* [7]
   Bundesnetzagentur
  “Bedarfsermittlung 2023-2037/2045 Bestätigung Netzentwicklungsplan Strom”, 2024
* [8]
   Bundesnetzagentur
  “Genehmigung eines Wasserstoff Kernnetzes”, 2024
* [9]
   Bundesnetzagentur
  “Marktstammdatenregister (MaStR)” accessed on April 10, 2025, 2025
  URL: <https://www.marktstammdatenregister.de>
* [10]
  Fraunhofer ISI, consentec and ifeu
  “Langfristszenarien für die Transformation des Energiesystems in Deutschland - Stromnetze”, 2024
  URL: <https://langfristszenarien.de/enertile-explorer-wAssets/docs/LFS3_O45-Szen_Cons_BMWK_LFS3_Webinar_20240702.pdf>
* [11]
  Energie & Management
  “Verteilnetzausbau kostet bis 2033 rund 110 Milliarden Euro”, 2024
  URL: <https://www.energie-und-management.de/nachrichten/technik/detail/verteilnetzausbau-kostet-bis-2033-rund-110-milliarden-euro-219768>
* [12]
   Artelys
  “Artelys Crystal Super Grid - KPI documentation”, 2023
  URL: <https://www.artelys.com/app/docs/supergrid/kpiDoc.html#flexibility-needs-wh>
* [13]
  Frederik Vom Scheidt et al.
  “Integrating hydrogen in single-price electricity systems: The effects of spatial economic signals”
  In *Energy Policy* 161, 2022, pp. 112727
  DOI: [10.1016/j.enpol.2021.112727](https://dx.doi.org/10.1016/j.enpol.2021.112727)
* [14]
  FTI Consulting and Energy Systems Catapult
  “Assessment of locational wholesale electricity market design options in GB”, 2023
  URL: <https://www.fticonsulting.com/uk/insights/videos-and-podcasts/assessment-locational-wholesale-electricity-market-design-options>
* [15]
  Jonas Hörsch, Henrik Ronellenfitsch, Dirk Witthaut and Tom Brown
  “Linear optimal power flow using cycle flows”
  In *Electric Power Systems Research* 158
  Elsevier, 2018, pp. 126–135
* [16]
  T. Brown, J. Hörsch and D. Schlachtberger
  “PyPSA: Python for Power System Analysis”
  In *Journal of Open Research Software* 6.4, 2018
  DOI: [10.5334/jors.188](https://dx.doi.org/10.5334/jors.188)
* [17]
  Amin Shokri Gazafroudi, Fabian Neumann and Tom Brown
  “Topology-based approximations for N - 1 contingency constraints in power transmission networks”
  In *International Journal of Electrical Power & Energy Systems* 137, 2022, pp. 107702
  DOI: [10.1016/j.ijepes.2021.107702](https://dx.doi.org/10.1016/j.ijepes.2021.107702)
* [18]
  Michael Lindner et al.
  “PyPSA-DE: An Open Model of the German Energy System” Accessed: 2025-01-28, 2025
  URL: <https://github.com/PyPSA/pypsa-de>
* [19]
  Gunnar Luderer et al.
  “Die Energiewende kosteneffizient gestalten: Szenarien zur Klimaneutralität 2045”, 2025
  DOI: [10.48485/pik.2025.003](https://dx.doi.org/10.48485/pik.2025.003)

## Additional figures

(see next pages)

![Refer to caption](x3.png)


Figure 5: Investment needs for the electricitry transmission grid until 2045 according to the NEP, and potential savings according to the PyPSA-DE methodology, differentiated by enabling assumption and affected grid components.



![Refer to caption](flexibility.png)

![Refer to caption](flexibility_carriers.png)

Figure 6: Top: Total daily, weekly and yearly flexibility needs for each model year. Bottom: Technologies that cover the daily and weekly flexibility needs. To compute the flexibility needs the method of Artelys is used
 [[12](https://arxiv.org/html/2510.09414v1#bib.bibx12)].