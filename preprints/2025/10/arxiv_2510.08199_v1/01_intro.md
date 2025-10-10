---
authors:
- Alice Di Bella
- Toni Seibold
- Tom Brown
- Massimo Tavoni
doc_id: arxiv:2510.08199v1
family_id: arxiv:2510.08199
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Pursuing decarbonization and competitiveness: a narrow corridor for European
  green industrial transformation'
url_abs: http://arxiv.org/abs/2510.08199v1
url_html: https://arxiv.org/html/2510.08199v1
venue: arXiv q-fin
version: 1
year: 2025
---


Alice Di Bella1,2,3,∗, Toni Seibold4, Tom Brown4, Massimo Tavoni1,2,3

(1 Department of Electronics, Information and Bioengineering, Politecnico di Milano, Milano, Italy
  
2 CMCC Foundation - Euro-Mediterranean Center on Climate Change, Italy
  
3 RFF-CMCC European Institute on Economics and the Environment, Italy
  
4 Department of Digital Transformation in Energy Systems, Institute of Energy Technology, Technische Universität Berlin, Berlin, Germany
  
\*Corresponding author. e-mail address: alice.dibella@cmcc.it
)

###### Abstract

Decarbonizing the industrial sector while maintaining competitiveness are two central objectives of European Union policy, but they can come into conflict. This study examines trade-offs between these goals across two divergent industrial development scenarios in Europe: one marked by a continued decline in industrial production, and another driven by competitiveness-enhancing policies that stimulate a resurgence of industrial activity. We use the open-source energy system model PyPSA-Eur, focusing on the most energy- and emission-intensive sectors: iron and steel, cement, methanol, ammonia, and high-value chemicals (HVCs, mainly plastics). We examine the price gap between domestically produced green industrial goods and low-carbon imported ones from non-European countries, and explore options such as intra-European relocation of production, selective import of intermediate green goods, and targeted government subsidies as reduced-impact alternatives to relocating the entire European industrial production outside of Europe. We find that deep industrial decarbonization in Europe is technically feasible, with a pivotal role for electrification. However, maintaining competitiveness is very sensitive to policy. Intra-European relocation of industrial production yields modest energy cost reductions and is constrained by economic, social, and infrastructural challenges. Strategically importing green intermediates significantly lowers system costs and carbon prices while preserving domestic production, employment, and competitiveness, serving as a crucial complement to Europe’s decarbonization. Subsidies are essential to prevent industrial relocation outside of Europe, but are not financially sustainable under strong reindustrialization; thus, government support needs to prioritize sectors such as ammonia and steel finishing, leveraging cost-effective imports of green methanol and Hot Briquetted Iron, and maintaining current production levels rather than pursuing the expansion of heavy industry in Europe.

Keywords industrial decarbonization, competitiveness, energy system modelling, PyPSA-Eur, European climate policies

## 1 Introduction

The European Union (EU) aims for climate neutrality by 2050, requiring significant and accelerated reductions in greenhouse gas (GHG) emissions across all economic sectors [[1](https://arxiv.org/html/2510.08199v1#bib.bibx1)]. Existing industrial processes are often incompatible with a low-carbon trajectory, making the sector critical for decarbonization [[2](https://arxiv.org/html/2510.08199v1#bib.bibx2)]. To support this transition, the EU has introduced policies such as the Net-Zero Industry Act and the Clean Industrial Deal [[3](https://arxiv.org/html/2510.08199v1#bib.bibx3), [4](https://arxiv.org/html/2510.08199v1#bib.bibx4)]. Simultaneously, the EU seeks to strengthen industrial production to boost resilience, autonomy, and global competitiveness. The Draghi Report [[5](https://arxiv.org/html/2510.08199v1#bib.bibx5)] warns that high energy costs, regulatory complexity, and slower innovation risk eroding competitiveness. Policies now aim to expand capacity, foster innovation, and secure strategic supply chains. The Clean Industrial Deal links competitiveness with decarbonization, positioning sustainability as an economic driver [[4](https://arxiv.org/html/2510.08199v1#bib.bibx4)].

EU27 emitted 600 Mtons of CO2 (approximately 20% of total EU GHG emissions) in the industrial sector alone in 2021, mainly in three sectors: iron and steel (22%), chemicals (21%), and non-metallic minerals (including cement and glass) (32%) [[6](https://arxiv.org/html/2510.08199v1#bib.bibx6), [7](https://arxiv.org/html/2510.08199v1#bib.bibx7)]. These sectors are considered “hard-to-abate” because of their high energy intensity, dependence on fossil fuels to provide high-temperature heat and serve as feedstocks, and the limited availability of mature low-carbon alternatives. Reducing production levels can contribute to lowering GHG emissions [[7](https://arxiv.org/html/2510.08199v1#bib.bibx7)], but electrification remains a central strategy for decarbonizing industrial energy use [[8](https://arxiv.org/html/2510.08199v1#bib.bibx8), [9](https://arxiv.org/html/2510.08199v1#bib.bibx9)]. Nonetheless, electricity cannot fully replace fossil fuels as feedstocks, such as in iron ore reduction or plastics production, where green hydrogen provides a low-carbon, though inefficient, alternative [[10](https://arxiv.org/html/2510.08199v1#bib.bibx10), [11](https://arxiv.org/html/2510.08199v1#bib.bibx11)]. Combined with carbonaceous feedstocks, green H2 enables synthetic fuels, while carbon capture and storage (CCS) allows decarbonization of processes like cement production that cannot rely solely on electricity [[12](https://arxiv.org/html/2510.08199v1#bib.bibx12), [13](https://arxiv.org/html/2510.08199v1#bib.bibx13)].

Sourcing energy carriers and industrial goods from regions with abundant renewables and lower costs may improve decarbonization economics [[14](https://arxiv.org/html/2510.08199v1#bib.bibx14), [15](https://arxiv.org/html/2510.08199v1#bib.bibx15), [16](https://arxiv.org/html/2510.08199v1#bib.bibx16)]. Such regions can produce green hydrogen, electricity-intensive commodities, and other low-carbon products more cheaply. While this could reduce global emissions, it risks Europe’s industrial competitiveness, sovereignty, and energy security, potentially causing job losses, regional decline, and dependence on foreign suppliers. Domestic capacity erosion could also weaken innovation and strategic autonomy. A compromise is trading intermediate products (e.g., Hot Briquetted Iron, methanol, ammonia), which lowers costs while keeping value creation in renewable-scarce regions [[17](https://arxiv.org/html/2510.08199v1#bib.bibx17)].

In this context, this study explores how European industries can simultaneously pursue deep decarbonization while preserving their competitiveness in global markets. We examine the role of key decarbonization technologies, namely green hydrogen, electrification, and CCS, in reducing emissions from industrial processes. The analysis assesses how the costs of European green industrial goods compare to those of imported alternatives. To identify reduced-impact pathways for reconciling climate and industrial policy objectives, three potential strategies are evaluated: (i) the relocation of industrial activities within Europe to optimise production and infrastructure; (ii) the selective import of intermediates goods, allowing Europe to retain parts of its industrial base while leveraging international supply chains; and (iii) targeted government subsidies to equalize production costs with those in countries benefiting from greater renewable energy availability. To summarise, this study wants to address the following research questions:

* •

  How can European industries reduce emissions while preserving competitiveness in global markets?
* •

  What is the role of relocation of industrial activities within Europe, and intermediate green goods imports in shaping less disruptive industrial transition pathways to Net-Zero?
* •

  To what extent can targeted subsidies help retain green industrial production in Europe?

## 2 Literature Review

Energy system models (ESMs) are valuable for analyzing industrial decarbonization, assessing technologies, sector interactions, and emission reductions [[18](https://arxiv.org/html/2510.08199v1#bib.bibx18), [19](https://arxiv.org/html/2510.08199v1#bib.bibx19), [20](https://arxiv.org/html/2510.08199v1#bib.bibx20), [21](https://arxiv.org/html/2510.08199v1#bib.bibx21), [22](https://arxiv.org/html/2510.08199v1#bib.bibx22), [23](https://arxiv.org/html/2510.08199v1#bib.bibx23), [24](https://arxiv.org/html/2510.08199v1#bib.bibx24)]. Madeddu et al. [[22](https://arxiv.org/html/2510.08199v1#bib.bibx22)] assess eleven industrial sectors, showing that 78% of energy demand can be electrified with existing technologies. Raillard-Cazanove et al. [[23](https://arxiv.org/html/2510.08199v1#bib.bibx23)] study steel, chemicals, cement, and glass in six countries, highlighting that captured CO2 is stored rather than reused due to costly e-fuel deployment. Modeling hard-to-abate sectors faces challenges such as data scarcity and high cost uncertainties [[25](https://arxiv.org/html/2510.08199v1#bib.bibx25)], and many studies lack transparency and accessible data [[26](https://arxiv.org/html/2510.08199v1#bib.bibx26)].

A large body of literature focuses on analysing the European energy transition in general using comprehensive bottom-up modelling approaches [[27](https://arxiv.org/html/2510.08199v1#bib.bibx27), [28](https://arxiv.org/html/2510.08199v1#bib.bibx28), [29](https://arxiv.org/html/2510.08199v1#bib.bibx29), [30](https://arxiv.org/html/2510.08199v1#bib.bibx30)]. Some studies suggests that decarbonization can be pursued more cost-effectively through increased imports of energy carriers and industrial goods from regions with abundant renewable resources, particularly green H2 [[31](https://arxiv.org/html/2510.08199v1#bib.bibx31), [32](https://arxiv.org/html/2510.08199v1#bib.bibx32), [33](https://arxiv.org/html/2510.08199v1#bib.bibx33), [34](https://arxiv.org/html/2510.08199v1#bib.bibx34), [35](https://arxiv.org/html/2510.08199v1#bib.bibx35), [36](https://arxiv.org/html/2510.08199v1#bib.bibx36)], synthetic hydrogen fuels [[37](https://arxiv.org/html/2510.08199v1#bib.bibx37), [38](https://arxiv.org/html/2510.08199v1#bib.bibx38), [33](https://arxiv.org/html/2510.08199v1#bib.bibx33), [39](https://arxiv.org/html/2510.08199v1#bib.bibx39)], renewable electricity [[40](https://arxiv.org/html/2510.08199v1#bib.bibx40), [41](https://arxiv.org/html/2510.08199v1#bib.bibx41), [42](https://arxiv.org/html/2510.08199v1#bib.bibx42), [36](https://arxiv.org/html/2510.08199v1#bib.bibx36), [43](https://arxiv.org/html/2510.08199v1#bib.bibx43)] , or steel [[15](https://arxiv.org/html/2510.08199v1#bib.bibx15), [44](https://arxiv.org/html/2510.08199v1#bib.bibx44), [14](https://arxiv.org/html/2510.08199v1#bib.bibx14)]. Neumann et al. [[14](https://arxiv.org/html/2510.08199v1#bib.bibx14)] develop a relevant study combining a global energy supply chain model with PyPSA-Eur, a detailed European energy system model used in this study as well, to assess how various levels and types of energy imports affect Europe’s infrastructure needs for achieving Net-Zero emissions. Authors show that importing renewable energy and steel can reduce Europe’s infrastructure build-out, lowering costs by 1-10%. The findings suggest that strategic import policies, particularly for hydrogen and derivatives, can ease Europe’s infrastructure constraints, though maintaining some domestic production remains beneficial.

Building upon the work of Neumann et al. [[14](https://arxiv.org/html/2510.08199v1#bib.bibx14)], this study extends the PyPSA-Eur framework by shifting the focus from system-level requirements to the industrial sector. A more detailed representation of industrial processes is incorporated, including type, location, and construction year of existing plants. Furthermore, we conduct the analysis for the entire transition pathway to Net-Zero within a myopic framework, rather than restricting it to a single future year. Unlike Neumann et al., who emphasize the expansion of transmission and storage infrastructure, this work identifies policy-relevant strategies to decarbonize European industry while maintaining competitiveness. Novel aspects include alternative industrial trajectories, imports of green intermediates, intra-European relocation, and government subsidies, providing insights relevant to policymakers and industry beyond standard cost optimization.

Despite extensive research, key questions remain on balancing deep emissions reductions with European industrial competitiveness. Technologies like green hydrogen, electrification, and CCS are central to decarbonization but may raise production costs compared to low-cost imports. While imports help meet demand, overreliance risks deindustrialization and lost domestic value. Strategies to reconcile decarbonization with competitiveness include intra-European relocation, trade of intermediate green precursors, and targeted subsidies. This study extends PyPSA-Eur to model plant-level processes, infrastructure, and alternative production pathways, enabling detailed assessment of policy-relevant decarbonization options.

## 3 Methods

### 3.1 Model development

The ESM employed in this study is PyPSA-Eur, an open-source, high-resolution modelling tool developed to explore cost-optimal decarbonisation pathways for the European energy system. For a comprehensive description, readers are referred to the official model documentation [[45](https://arxiv.org/html/2510.08199v1#bib.bibx45)], and the GitHub repository [[46](https://arxiv.org/html/2510.08199v1#bib.bibx46)]. PyPSA-Eur, open-source and widely used [[28](https://arxiv.org/html/2510.08199v1#bib.bibx28), [47](https://arxiv.org/html/2510.08199v1#bib.bibx47), [48](https://arxiv.org/html/2510.08199v1#bib.bibx48)], enables integrated analyses of electricity, heating, transport, industry, agriculture, shipping, and aviation. It was chosen for its detailed power grid representation and ability to capture inter-sector interactions. The model performs high-resolution linear optimization to minimize system costs, optimizing investments and operations across generation, storage, conversion, and transmission.

Industrial modelling in PyPSA-Eur, detailed in Victoria et al. [[28](https://arxiv.org/html/2510.08199v1#bib.bibx28)], use JRC-IDEES data [[7](https://arxiv.org/html/2510.08199v1#bib.bibx7)] to estimate energy demands and process emissions per unit output, with exogenous assumptions on low-carbon technology uptake. Production volumes are held constant until 2050, yielding predetermined electricity, hydrogen, biomass, and oil demands. Neumann et al. [[14](https://arxiv.org/html/2510.08199v1#bib.bibx14)] extended the model to include material imports and Electric Arc Furnaces for steel, but their greenfield 2050 optimization ignores the spatial distribution and operational status of existing plants.

While the current framework of PyPSA-Eur captures industrial energy demand, this study requires a more detailed representation of sectors and technologies. By modelling specific processes and techno-economic parameters, the model endogenously determines least-cost technology and fuel mixes, optimizes production levels, and achieves economy-wide Net-Zero emissions cost-effectively. If decarbonization of a sector is costly, mitigation can shift to other sectors or use negative emissions without prior assumptions. To this end, PyPSA-Eur was extended to represent five key sectors, iron and steel, cement, ammonia, methanol, and High Value Chemicals (HVCs), which account for nearly two-thirds of EU27 industrial CO2 emissions [[7](https://arxiv.org/html/2510.08199v1#bib.bibx7)]. The technical design of these sectors within the PyPSA-Eur model extension is detailed in Section [A.1](https://arxiv.org/html/2510.08199v1#A1.SS1 "A.1 Industrial sectors modelling ‣ Appendix A Supplementary Materials ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation").

Additionally, this study integrates climate-adjusted weather projections into PyPSA-Eur. Standard PyPSA-Eur uses ERA5 (2013) and SARAH-3 data for wind and solar generation [[49](https://arxiv.org/html/2510.08199v1#bib.bibx49)], but climate change affects renewable generation, demand, and infrastructure. We use a dataset from Antonini et al. [[50](https://arxiv.org/html/2510.08199v1#bib.bibx50)], which combines historical ERA5 data (1940–2023) with CMIP5 EURO-CORDEX projections (2006–2100) under RCP 2.6, 4.5, and 8.5. It provides country-level time series for wind, solar, and hydropower across the EU27 (excluding Cyprus and Malta), UK, Norway, Switzerland, and Serbia, incorporating multiple climate models to capture uncertainty.

### 3.2 Parameters and assumptions

Common assumptions

A consistent set of parameters is applied across all scenarios. The PyPSA-Eur model is operated in myopic mode with a three-hourly temporal resolution for the years 2030, 2040, and 2050 using Gurobi solver. The model spans 39 nodes across 34 European countries, covering all EU27 Member States (excluding Cyprus and Malta), United Kingdom, Switzerland, Norway, Albania, Bosnia and Herzegovina, Montenegro, North Macedonia, Serbia, and Kosovo. Each country is represented by at least one node. The modelling framework follows a brownfield approach, incorporating existing power and heating generation, transmission infrastructure, industrial hubs, enhanced in this study with data on existing plants added to the original PyPSA-Eur model. Renewable generation from onshore and offshore wind, and solar PV can expand based on land eligibility via atlite, while hydropower is fixed and nuclear may increase if cost-optimal. Electricity storage includes pumped hydro, batteries, and hydrogen systems (electrolysers, tanks, fuel cells). Power and methane grids use SciGRID\_gas [[51](https://arxiv.org/html/2510.08199v1#bib.bibx51)] and OpenStreetMap [[52](https://arxiv.org/html/2510.08199v1#bib.bibx52)]. Grid expansion is allowed, but line use is capped at 70% to approximate N-1 security. Due to delays in hydrogen pipeline deployment [[53](https://arxiv.org/html/2510.08199v1#bib.bibx53), [54](https://arxiv.org/html/2510.08199v1#bib.bibx54)], H2 infrastructure is excluded, and each node meets demand via local production. A robustness analysis considers repurposing existing gas pipelines or investing in new ones (Supplementary Fig. [A.3](https://arxiv.org/html/2510.08199v1#A1.F3 "Figure A.3 ‣ A.3 Robustness check on hydrogen infrastructure ‣ Appendix A Supplementary Materials ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation")). Technology costs are updated for each optimisation year using the Technology-Data package [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)]. Weather-dependent resources are derived from year- and country-specific climate projections developed by Antonini et al. [[50](https://arxiv.org/html/2510.08199v1#bib.bibx50)], from CNRM-CERFACS-CM5 global model and downscaled with th CNRM-ALADIN63 regional model, based on the RCP 4.5 scenario. Sustainable biomass is capped at 1,372 TWh/a (JRC-ENSPRESO [[56](https://arxiv.org/html/2510.08199v1#bib.bibx56)]), with no imports. CO2 removal via Bio-Energy CCS (BECCS) and Direct Air Capture (DAC) is limited to 50 MtCO2/a in 2030, 250 MtCO2/a in 2040, and 400 MtCO2/a in 2050, in line with EU targets and IAM projections [[57](https://arxiv.org/html/2510.08199v1#bib.bibx57), [58](https://arxiv.org/html/2510.08199v1#bib.bibx58)].

Scenarios framework

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Climate Target | | Relocation | Intermediate Imports |
| Industrial Production | \cellcolor base\_reg\_deindustrial No Climate Policy   Deindustrial   No Relocation  No Interm. Imports | \cellcolor policy\_reg\_deindustrial Climate Policy   Deindustrial   No Relocation  No Interm. Imports | \cellcolor policy\_eu\_deindustrial Climate Policy   Deindustrial   Relocation within Europe   No Interm. Imports | \cellcolor import\_policy\_reg\_deindustrial Climate Policy   Deindustrial  No Relocation   Intermediate Imports |
|  | \cellcolor base\_reg\_maintain No Climate Policy   Stabilization   No Relocation   No Interm. Imports | \cellcolor policy\_reg\_maintain Climate Policy   Stabilization   No Relocation   No Interm. Imports | \cellcolor white | \cellcolor white |
|  | \cellcolor base\_reg\_regain No Climate Policy  Reindustrial   No Relocation   No Interm. Imports | \cellcolor policy\_reg\_regain Climate Policy   Reindustrial   No Relocation   No Interm. Imports | \cellcolor policy\_eu\_regain Climate Policy   Reindustrial   Relocation within Europe   No Interm. Imports | \cellcolor import\_policy\_reg\_regain Climate Policy   Reindustrial   No Relocation   Intermediate Imports |

Table 1: Scenario matrix combining climate targets and industrial production trends, relocation within Europe and intermediate imports.

Different scenarios are illustrated in Table [1](https://arxiv.org/html/2510.08199v1#S3.T1 "Table 1 ‣ 3.2 Parameters and assumptions ‣ 3 Methods ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation"). In No Climate Policy scenarios, the system is cost-optimized without GHG targets, though renewable investments may occur if economically advantageous. Climate Policy scenarios implement EU targets: 55% GHG reduction by 2030, 90% by 2040, and Net-Zero by 2050 [[59](https://arxiv.org/html/2510.08199v1#bib.bibx59), [60](https://arxiv.org/html/2510.08199v1#bib.bibx60), [61](https://arxiv.org/html/2510.08199v1#bib.bibx61)], with all GHG expressed in CO2 equivalents. Sectoral assumptions differ: land transport is fully electrified, methanol meets 50% of shipping demand (boosting industrial methanol production), and aviation uses synthetic kerosene via Fischer-Tropsch synthesis.

The second scenario differentiation concerns industrial production. European industry has declined due to high energy costs, ageing infrastructure, and global competition [[62](https://arxiv.org/html/2510.08199v1#bib.bibx62), [63](https://arxiv.org/html/2510.08199v1#bib.bibx63), [64](https://arxiv.org/html/2510.08199v1#bib.bibx64)], prompting policies like RePowerEU [[65](https://arxiv.org/html/2510.08199v1#bib.bibx65)], the Clean Industrial Deal [[4](https://arxiv.org/html/2510.08199v1#bib.bibx4)], and the CBAM [[66](https://arxiv.org/html/2510.08199v1#bib.bibx66)] to support competitiveness and the green transition. To capture uncertainty, three trajectories are considered: Continued Decline (continued decline), Reindustrialization (annual growth), and Stabilization (stable output). These scenarios refer to domestic production; in Continued Decline, reduced output is assumed offset by imports, raising questions about the carbon intensity of foreign goods, while Reindustrialization may reduce import reliance and create exports. Changes in domestic consumption are not explicitly modelled, and a full assessment of trade-related emissions is beyond this study’s scope.

To model the rate of change in industrial production, historical trends are extrapolated by replicating each sector’s annual absolute change, based on linear interpolation between the earliest and latest available data (2023 for most sectors, 2022 for cement and plastics, 2021 for methanol) as shown in Eq. [1](https://arxiv.org/html/2510.08199v1#S3.E1 "In 3.2 Parameters and assumptions ‣ 3 Methods ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation").

|  |  |  |  |
| --- | --- | --- | --- |
|  | Annual production change=|Annual productionlatest data year−Annual productionfirst available year|latest data year−first available year\text{Annual production change}=\frac{|\text{Annual production}\_{\text{latest data year}}-\text{Annual production}\_{\text{first available year}}|}{\text{latest data year}-\text{first available year}} |  | (1) |

Table 2: Historical annual production changes for each subsector

|  |  |  |
| --- | --- | --- |
| Subsector | Annual production change [Mt/year] | Source |
| Iron and steel | 2.6 | Word Steel Association [[67](https://arxiv.org/html/2510.08199v1#bib.bibx67)] |
| Cement | 1.9 | Cembureau [[68](https://arxiv.org/html/2510.08199v1#bib.bibx68)] |
| Ammonia | 0.32 | Eurostat [[69](https://arxiv.org/html/2510.08199v1#bib.bibx69)] |
| Methanol | 0.09 | Eurostat [[69](https://arxiv.org/html/2510.08199v1#bib.bibx69)] |
| Plastics | 0.63 | Plastics Europe [[70](https://arxiv.org/html/2510.08199v1#bib.bibx70)] |

In Table [2](https://arxiv.org/html/2510.08199v1#S3.T2 "Table 2 ‣ 3.2 Parameters and assumptions ‣ 3 Methods ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation") values for each sector are detailed. Figure [1](https://arxiv.org/html/2510.08199v1#S3.F1 "Figure 1 ‣ 3.2 Parameters and assumptions ‣ 3 Methods ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation") shows historical production (dots) and projected trajectories for each sector under the three production scenarios. Her, methanol values reflect industrial demand only, but under Climate Policy, the model has an additional shipping demand of 7 Mt in 2030, 16 Mt in 2040, and 23 Mt in 2050.

![Refer to caption](figures/production_projections_with_full_historical.png)


Figure 1: Industrial production trajectory within the geographical scope of the model, EU27 (without Cyprus and Malta), UK, Switzerland, Norway, Albania, Bosnia and Herzegovina, Montenegro, North Macedonia, Serbia, and Kosovo, for the five industrial goods considered in the study, in the Continued Decline, Stabilization, and Reindustrialization scenarios. Note that methanol production data exhibit an irregular trend, which may be attributable to inconsistencies or gaps in reporting rather than to underlying structural changes in the sector.

The analysis also explores two additional scenario dimensions under Climate Policy for both Continued Decline and Reindustrialization. The first examines intra-European relocation of industrial production. In No Relocation scenarios, production remains fixed, reflecting inertia due to infrastructure, labour, supply chains, and regional policies. In Relocation within Europe scenarios, the model optimizes plant locations for cost-effectiveness, capturing a potential ”renewables pull” where industries move to regions with abundant low-cost renewable energy [[17](https://arxiv.org/html/2510.08199v1#bib.bibx17), [16](https://arxiv.org/html/2510.08199v1#bib.bibx16)].

The second dimension examines imports of intermediate green goods under Climate Policy for both Continued Decline and Reindustrialization. This strategy retains high-value industrial segments in Europe while outsourcing energy-intensive stages to regions with lower renewable costs [[71](https://arxiv.org/html/2510.08199v1#bib.bibx71), [17](https://arxiv.org/html/2510.08199v1#bib.bibx17), [14](https://arxiv.org/html/2510.08199v1#bib.bibx14)]. Imports considered include green methanol and ammonia for 2040 and 2050, using literature-based average prices [[14](https://arxiv.org/html/2510.08199v1#bib.bibx14), [72](https://arxiv.org/html/2510.08199v1#bib.bibx72)], and green Hot Briquetted Iron for EAF at 395 EUR/ton [[15](https://arxiv.org/html/2510.08199v1#bib.bibx15)]. These feedstocks also serve as low-carbon fuels in other sectors.

Government subsidies calculations

This paper examines how targeted subsidies can prevent the relocation of green industries in the face of lower-cost international imports. Subsidy requirements are quantified, for each commodity cc in scenario ss and year yy, by multiplying its production volume Qc,s,yQ\_{c,s,y} by the difference between PyPSA-Eur weighted average marginal prices and green import prices from the literature [[14](https://arxiv.org/html/2510.08199v1#bib.bibx14), [72](https://arxiv.org/html/2510.08199v1#bib.bibx72)] (Eq. [2](https://arxiv.org/html/2510.08199v1#S3.E2 "In 3.2 Parameters and assumptions ‣ 3 Methods ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation")).

|  |  |  |  |
| --- | --- | --- | --- |
|  | Sc,s,y=(pc,s,yPyPSA-Eur−pc,s,yGreen Imports)⋅Qc,s,y,S\_{c,s,y}=\bigl(p\_{c,s,y}^{\text{{PyPSA-Eur}}}-p\_{c,s,y}^{\text{{Green Imports}}}\bigr)\cdot Q\_{c,s,y}, |  | (2) |

Green industrial products from outside Europe are assumed to be available from 2040 (also as in Figure [3](https://arxiv.org/html/2510.08199v1#S4.F3 "Figure 3 ‣ 4.1 Decarbonisation and competitiveness ‣ 4 Results and discussion ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation")); thus, subsidies are not applied in 2030. The average annual subsidy for commodity cc in scenario ss (2035–2055) is computed as the weighted mean over representative years, with each year representing a decade, yielding Eq. [3](https://arxiv.org/html/2510.08199v1#S3.E3 "In 3.2 Parameters and assumptions ‣ 3 Methods ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation").

|  |  |  |  |
| --- | --- | --- | --- |
|  | S¯c,s=1020​∑y∈{2040,2050}Sc,s,y,\overline{S}\_{c,s}=\frac{10}{20}\sum\_{y\in\{2040,2050\}}S\_{c,s,y}, |  | (3) |

## 4 Results and discussion

### 4.1 Decarbonisation and competitiveness

Technology portfolios

Figure [2](https://arxiv.org/html/2510.08199v1#S4.F2 "Figure 2 ‣ 4.1 Decarbonisation and competitiveness ‣ 4 Results and discussion ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation") shows technological pathways optimized by PyPSA-Eur across scenarios (as a reference historical production is in dots in Figure [1](https://arxiv.org/html/2510.08199v1#S3.F1 "Figure 1 ‣ 3.2 Parameters and assumptions ‣ 3 Methods ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation")). The first column depicts the No Climate Policy scenario at Stabilization production. Climate Policy scenarios are split into Continued Decline, Stabilization, and Reindustrialization, with methanol rising to meet maritime fuel demand. All optimizations assume No Relocation and No Intermediate Goods imports.

Model results show that European industrial decarbonization is primarily driven by electrification and green hydrogen, which is expected to expand across sectors (Figure [A.1](https://arxiv.org/html/2510.08199v1#A1.F1 "Figure A.1 ‣ A.2 Extra indicators for energy sectors ‣ Appendix A Supplementary Materials ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation")), while reliance on CCS remains limited. For steel, ammonia, and methanol, the transition to green hydrogen occurs in 2040, under more stringent decarbonization targets (-90% GHG). Steam Methane Reforming (SMR) with CCS remains in use in 2030, as captured CO2 can be repurposed in other processes. In the Reindustrialization scenario, plastics increasingly use sequestered CO2 for Fischer-Tropsch synthesis, reaching  25% of production by 2050, while biomass remains limited due to competing demands. Cement emissions are mitigated via DAC and BECCS rather than CCS, highlighting a shift toward atmospheric carbon removal, although the absence of a dedicated CO2 infrastructure network might impact this outcome. Overall production levels minimally affect technology choices, except in plastics, where limited CO2 storage at higher outputs favours Fischer-Tropsch processes.

![Refer to caption](figures/european_production_stacked_wmaintain.png)


Figure 2: Production of industrial goods in four scenarios: the first column represent the scenario with No Climate Policy and Stabilization of industrial production, the other three columns show scenarios implementing the EU Climate Policies, spanning from Continued Decline, to Stabilization and then Reindustrialization. Rows indicate the different industrial sectors and the technologies available in the model are depicted in the legend.

Prices of industrial goods

Figure [3](https://arxiv.org/html/2510.08199v1#S4.F3 "Figure 3 ‣ 4.1 Decarbonisation and competitiveness ‣ 4 Results and discussion ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation") shows average European industrial commodity prices, weighted by production, for all Climate Policy scenarios and three production levels. Prices are derived from Lagrange (Karush-Kuhn-Tucker or KKT) multipliers λn,t\lambda\_{\textit{n},\textit{t}}, representing marginal costs by region and time, with 2020 values included for comparison (steel [[73](https://arxiv.org/html/2510.08199v1#bib.bibx73)], cement [[74](https://arxiv.org/html/2510.08199v1#bib.bibx74)], ammonia [[75](https://arxiv.org/html/2510.08199v1#bib.bibx75)], methanol [[76](https://arxiv.org/html/2510.08199v1#bib.bibx76)], plastics [[77](https://arxiv.org/html/2510.08199v1#bib.bibx77)]).

The Figure compares European industrial commodity prices with imported low-carbon goods, assumed produced using renewable electricity in regions with abundant land and energy, after meeting domestic demand. Comparisons are shown for 2040 and 2050 (-90% and Net-Zero emissions), with import price ranges indicated by the gray band [[14](https://arxiv.org/html/2510.08199v1#bib.bibx14), [72](https://arxiv.org/html/2510.08199v1#bib.bibx72)]. Lower costs occur in renewable-rich regions (e.g., hydrogen in the Maghreb, steel in Australia), while higher costs arise from additional processing (e.g., hydrogen liquefaction). Cement is excluded because its low energy density makes transport prohibitively expensive [[68](https://arxiv.org/html/2510.08199v1#bib.bibx68)].

Decarbonization raises industrial production costs, peaking around 2040, then declining by 2050 as investments stabilize. Modelling myopic transition pathways captures how investment timing affects final prices. Cost increases stem from capital investments in low-carbon technologies, especially hydrogen electrolysers, and higher energy use. Fully decarbonized sectors like steel, ammonia, and methanol rely on green hydrogen, driving up electricity needs despite similar power prices to No Climate Policy scenarios (see Figure [A.2](https://arxiv.org/html/2510.08199v1#A1.F2 "Figure A.2 ‣ A.2 Extra indicators for energy sectors ‣ Appendix A Supplementary Materials ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation")). In harder-to-abate sectors, such as cement and plastics, costs are mainly driven by carbon pricing. For plastics and methanol, emissions can be priced either at the point of release (excluding embedded carbon, as the dotted lines in the Figure) or including embedded carbon, with the latter raising product costs and strengthening decarbonization incentives.

European industrial commodity prices are compared with literature-based import cost ranges for low-carbon goods from renewable-rich regions outside of Europe. Results show plastics remain within import price ranges, even when accounting for end-of-life carbon costs. Steel remains competitive only under Continued Decline, while ammonia and methanol do so also under Stabilization, as lower production volumes ease marginal cost pressures. Overall competitiveness depends on domestic production trends and uncertain green import costs ranges, which vary with transport, infrastructure, and capital expenses.

![Refer to caption](figures/commodity_prices.png)


Figure 3: Prices of industrial goods, average across European countries and time steps, for different scenarios. Dotted lines for methanol and plastics represent a price when no carbon price on End Of Life (EOL) emissions is applied.

### 4.2 Industrial relocation and green intermediates trade

Neumann et al. explore scenarios where all commodities are produced in regions with optimal renewable and land resources [[14](https://arxiv.org/html/2510.08199v1#bib.bibx14)], a shift that could disrupt European value chains and employment. To mitigate such risks, we assess two moderate strategies:

1. 1.

   allowing full industrial relocation within Europe to optimize resource use;
2. 2.

   enabling imports of low-carbon intermediates (HBI, ammonia, and methanol) from outside Europe to balance logistics and supply security.

Relocation within Europe

We analyse how allowing full industrial relocation within Europe affects annual system costs, industrial electricity expenditures, and the spatial distribution of plants. The Continued Decline and Reindustrialization scenarios are each examined with and without Relocation within Europe. Figure [4](https://arxiv.org/html/2510.08199v1#S4.F4 "Figure 4 ‣ 4.2 Industrial relocation and green intermediates trade ‣ 4 Results and discussion ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation") compares (a) the 2024 baseline distribution of industrial activity (steel, cement, ammonia, methanol, HVCs), (b) the resulting geographical distribution of total production in the scenarios, and (c) changes in industrial electricity spending.

In the Relocation within Europe scenarios, production concentrates in Spain, the UK, and Nordic countries with abundant renewables, the “renewable pull” effect [[17](https://arxiv.org/html/2510.08199v1#bib.bibx17), [16](https://arxiv.org/html/2510.08199v1#bib.bibx16)]. This relocation lowers industrial energy expenditures across all cases (panel c), emphasizing the importance of access to low-cost renewables for competitiveness. However, the model optimizes solely on cost, omitting factors such as social and economic relocation costs, supply chain disruptions, and infrastructure needs. Thus, although intra-European relocation yields moderate reductions in industrial energy costs, these benefits alone would not justify major disruptions to existing supply chains. This is especially true since PyPSA-Eur omits hidden costs, including socio-economic impacts, supply chain disruptions, and necessary infrastructure investments

![Refer to caption](figures/combined_layout_totsyscost.png)


Figure 4: (a) Total industrial production levels across European countries in 2024, showing current capacity distribution. (b) Projected industrial production trajectories for 2030, 2040, and 2050 under four scenarios: Continued Decline (two top rows) with No relocation within Europe and with Relocation within Europe, Reindustrialization (two bottom rows), again with No relocation within Europe and with Relocation within Europe. Color scale represents total industrial production in Gtons/a. (c) Industry expenditures for electricity for all commodities, across the four scenarios for 2030, 2040, and 2050, in billion euros per year. Boxes contain the difference between Relocation within Europe and No Relocation and the percentage change with respect to the No Relocation scenario, computed as
Δ​C%=CR​e​l​o​c−CN​o​R​e​l​o​cCN​o​R​e​l​o​c⋅100\Delta C\_{\%}=\frac{C\_{Reloc}-C\_{No\ Reloc}}{C\_{No\ Reloc}}\cdot 100.

Import of intermediate goods

We evaluate the impact of importing green intermediates, HBI, ammonia, and methanol, from outside Europe from 2040, on European industrial technologies and system costs. Figure [5](https://arxiv.org/html/2510.08199v1#S4.F5 "Figure 5 ‣ 4.2 Industrial relocation and green intermediates trade ‣ 4 Results and discussion ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation") presents technology shares (panel a) and annual system costs with carbon prices (panel b) for Continued Decline and Reindustrialization, with No Intermediate Imports shares shown in Figure [2](https://arxiv.org/html/2510.08199v1#S4.F2 "Figure 2 ‣ 4.1 Decarbonisation and competitiveness ‣ 4 Results and discussion ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation").

Importing green intermediates significantly shapes the European industrial technology mix, especially around 2040. Steel production uses imported HBI alongside EAFs, though scrap-based EAF remains more cost-effective, while ammonia and methanol shift almost entirely to imports by 2050, reducing domestic green hydrogen demand by 25% (Figure [A.1](https://arxiv.org/html/2510.08199v1#A1.F1 "Figure A.1 ‣ A.2 Extra indicators for energy sectors ‣ Appendix A Supplementary Materials ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation")). This strategy lowers annual system costs from 2040 onward and reduces the carbon price, allowing Europe to retain final-stage industrial activity while easing cost pressures through low-carbon imports.

![Refer to caption](figures/combined_production_prices_labeled.png)


Figure 5: (a) Projected industrial production trajectories for 2030, 2040, and 2050 under two scenarios, both with Intermediate Imports: Continued Decline and Reindustrialization. (b) Annual system costs (bnEUR/a) shown in the left-hand graph, and carbon prices (EUR/tCO2) for the two previous scenarios, along with the corresponding values for the No Intermediate Imports case. Boxes contain the difference between Intermediate Import and No Intermediate Imports and the percentage change with respect to the No Intermediate Imports scenario, computed as
Δ​C%=CI​m​p​o​r​t−CN​o​I​m​p​o​r​tCN​o​I​m​p​o​r​t⋅100\Delta C\_{\%}=\frac{C\_{Import}-C\_{No\ Import}}{C\_{No\ Import}}\cdot 100.

### 4.3 Governments’ subsidies

Governments may subsidize industries transitioning to Net-Zero to prevent relocation outside of Europe driven by the ”renewable pull” effect from renewable-rich countries abroad. Our results indicate that the required financial support varies markedly across sectors and scenarios.

Figure [6](https://arxiv.org/html/2510.08199v1#S4.F6 "Figure 6 ‣ 4.3 Governments’ subsidies ‣ 4 Results and discussion ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation") shows the average annual subsidies (in bnEUR/a) needed for steel, cement, ammonia, methanol, and plastics industries to not relocate outside of Europe, considering the period from 2035 to 2055. They are calculated with the formulas Eq. [2](https://arxiv.org/html/2510.08199v1#S3.E2 "In 3.2 Parameters and assumptions ‣ 3 Methods ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation") and Eq. [3](https://arxiv.org/html/2510.08199v1#S3.E3 "In 3.2 Parameters and assumptions ‣ 3 Methods ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation") in Section [3.2](https://arxiv.org/html/2510.08199v1#S3.SS2 "3.2 Parameters and assumptions ‣ 3 Methods ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation") across four policy scenarios: Continued Decline, both with and without Intermediate Imports, same for Reindustrialization.

For context, total energy subsidies in the EU27 amounted to 213 bnEUR in 2021, before the energy crisis [[78](https://arxiv.org/html/2510.08199v1#bib.bibx78)]. The Clean Industrial Deal aims to mobilize €100 billion in funding, equivalent to about 5bnEUR/a over two decades of reduced competitiveness [[4](https://arxiv.org/html/2510.08199v1#bib.bibx4)]. In contrast, the highest-subsidy case in this study, Reindustrialization with No Intermediate Imports, would require approximately 235 bnEUR/yr, a level of financial support that would be unsustainable if directed solely toward industry.

The plastics sector could reasonably be excluded from subsidy schemes, as its high subsidy needs arise primarily from large production volumes rather than elevated prices, which generally remain within international import price ranges (Figure [3](https://arxiv.org/html/2510.08199v1#S4.F3 "Figure 3 ‣ 4.1 Decarbonisation and competitiveness ‣ 4 Results and discussion ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation")). Methanol production appears economically more favourable in renewable-rich regions, whereas ammonia could remain competitive within Europe given its moderate subsidy requirements. For green steel, competitiveness could be maintained by importing green HBI intermediates and/or avoiding aggressive reindustrialization. Consequently, policy efforts should prioritize sustaining current industrial capacity rather than expanding it, while encouraging strategic imports of green HBI, methanol, and ammonia.

A share of the required funding could derive from EU ETS and CBAM revenues, provided sufficient allocations are made to the Social Climate Fund to ensure a just transition. Alternatively, regulatory measures, such as limiting imports, could achieve comparable outcomes to subsidies by shifting part of the cost burden from governments to consumers. Similarly, implementing import tariffs would yield comparable effects, transferring the cost burden from governments to consumers.

![Refer to caption](figures/total_subsidies_single_row_2040.png)


Figure 6: Average annual subsidy requirements [bnEUR/a] for the five industrial sectors under four policy scenarios: Continued Decline, with and without Intermediate Imports, Reindustrialization with and with No Intermediate Imports.

## 5 Conclusions

This study analyses Europe’s industrial decarbonization pathways and their competitiveness impacts using an extended high-resolution PyPSA-Eur model. Scenarios explore different industrial production levels, intra-European relocation, intermediate green imports, and targeted subsidies, assessing technical feasibility, costs, and global competitiveness to inform resilient decarbonization strategies.

Our results show that Europe can achieve deep industrial decarbonization by 2050, driven mainly by electrification and green hydrogen for steel, ammonia, and methanol, with cement relying on DAC/BECCS and plastics using CDR alongside fossil and Fischer–Tropsch pathways. Maintaining global competitiveness is feasible if Europe avoids aggressive reindustrialization. While decarbonization initially raises costs due to capital and energy demands, these stabilize after 2040. However, steel remains relatively uncompetitive, whereas plastics compare favourably with import price ranges, which themselves are subject to significant uncertainty.

To reconcile decarbonization with competitiveness, this study examines complementary strategies: intra-European relocation of production, selective imports of energy-intensive green intermediates, and targeted government subsidies. Intra-European relocation modestly reduces energy costs via a “renewable pull”; however, unaccounted economic, social, and infrastructural factors limit its practical feasibility. Importing green intermediates plays a strategic role in Europe’s industrial decarbonization, reducing system costs and carbon prices while preserving downstream production, employment, and competitiveness, making international trade a valuable complement to domestic decarbonization efforts. Targeted government subsidies are essential to prevent the relocation of industries outside of Europe, but under Reindustrialization they become economically unfeasible if applied to all sectors. While plastics would require substantial support due to their large production volume and high embedded carbon, and thus high implicit carbon costs, their competitiveness with international import prices suggests they can be excluded from subsidy programs. A resilient and practical strategy restricts government support to key sectors such as steel finishing and ammonia, while allowing cost-advantageous imports of methanol and HBI from renewable-rich regions and maintaining existing industrial production levels rather than pursuing expansion.

Limitations and future research directions

This study has some limitations that open opportunities for future research. We don’t consider the possibility to replace today’s plastics primary production with higher recycling rates and we omit biomass-based methanol, to maintain tractable CO2 accounting and for the sake of simplicity. Including these pathways in future analyses would expand decarbonization options, and enable a more comprehensive assessment of interactions with other low-carbon strategies. This study’s technology portfolio is not fully comprehensive, omitting CCS at NG-DRI-EAF steel plants, clinker-to-output improvements in cement, and other measures requiring more detailed modelling. It also excludes CO2 transport and storage infrastructure, which could affect CCS and CDR adoption, while costs for emerging CDR and DAC technologies remain highly uncertain. Despite these gaps, major low-carbon options are captured, and future work incorporating sensitivities and CO2 infrastructure could refine assessments of industrial decarbonization pathways. The analysis also omits potential geopolitical shocks and their effects on commodity and technology costs, particularly for clean energy technologies dependent on concentrated critical raw materials. Future work incorporating cost sensitivities and supply chain risks would help evaluate the robustness of decarbonization pathways under market and geopolitical uncertainties.

## 6 Acknowledgements

A. Di Bella was funded by the European Union - NextGenerationEU, Mission 4, Component 2, in the framework of the GRINS -Growing Resilient, INclusive and Sustainable project (GRINS PE00000018 – CUP C83C22000890001).
T. Seibold gratefully acknowledges funding from the Kopernikus-Ariadne project by the German Federal Ministry of Research, Technology and Space (Bundesministerium für Forschung, Technologie und Raumfahrt, BMFTR), grant number 03SFK5R0-2.
The views and opinions expressed are solely those of the authors and do not necessarily reflect those of the European Union, nor can the European Union be held responsible for them.

Data availability
  
The code to reproduce the experiments is available at https://github.com/cerealice/pypsa-eur-adb/tree/industry\_project and is stored in a Zenodo repository https://zenodo.org/records/17305060.

CRediT authorship contribution statement
  
A. Di Bella: Conceptualization, Data curation, Formal analysis, Investigation, Methodology, Software, Visualization, Writing – original draft, Writing – review & editing.

T. Seibold: Data curation, Formal analysis, Software, Writing – review & editing.

T. Brown and M. Tavoni: Writing – review & editing, Conceptualization, Project administration.

Declaration of competing interest
  
The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence
the work reported in this paper.

Declaration of generative AI and AI-assisted technologies in the writing process
  
During the preparation of this work the authors used ChatGPT in order to improve the language of this paper. After using this tool, the authors reviewed and edited the content as needed and take full responsibility for the content of the published article.

## Appendix A Supplementary Materials

### A.1 Industrial sectors modelling

Here, we provide a detailed description of the implementation of various industrial sectors within PyPSA-Eur. It is important to note that all these industrial technologies operate at generally high temperatures. Consequently, a minimum partial load constraint, specific to each technology, is incorporated to account for their limited operational flexibility. This constraint influences the model outcomes, as these plants are required to operate continuously, even at low output levels and at times with high electricity prices.

Iron and steel

The predominant methods for steel production today are primary production from iron ore and secondary production from recycled scrap. The Blast Furnace–Basic Oxygen Furnace (BF-BOF) process, commonly referred to as Integrated Steelmaking, involves the reduction of iron ore using coke and coal, resulting in substantial CO2 emissions. A more energy-efficient and less carbon-intensive alternative is the Direct Reduced Iron-Electric Arc Furnace (DRI-EAF) process, where iron ore is reduced using natural gas before being melted in an EAF. Hydrogen has the potential to serve as a reducing agent in the DRI process, but it is currently not used industrially due to its higher cost compared to natural gas. The secondary production route, based on scrap-fed electric arc furnaces, melts recycled steel scrap using electricity and thereby achieves substantially lower emissions than primary steelmaking, as it avoids the direct reduction stage. Recent EU policy developments underscore the strategic importance of steel scrap, with measures to retain greater volumes within Europe [[79](https://arxiv.org/html/2510.08199v1#bib.bibx79)], yet current data on EU27 availability—around 112 Mt in 2018—remain limited in their resolution by quality class, which is essential for aligning scrap supply with specific steel product requirements [[80](https://arxiv.org/html/2510.08199v1#bib.bibx80)]. In our model, the scrap-EAF route is represented using the market price of steel scrap in Europe of 302.5 EUR/ton [[81](https://arxiv.org/html/2510.08199v1#bib.bibx81)]. Due to both its economic attractiveness and its environmental benefits, the share of scrap-based production is expected to increase to the maximum technically feasible level. To capture this dynamic, we impose an upper bound on scrap use as a percentage of total steel production. Estimates in the literature diverge on this limit, with some studies adopting more conservative assumptions (e.g., 75% by 2050 in Transition Asia [[82](https://arxiv.org/html/2510.08199v1#bib.bibx82)]) and others suggesting higher potential (e.g., 90% by 2050 in Pehl et al. [[83](https://arxiv.org/html/2510.08199v1#bib.bibx83)]). The constraint reflects the fact that scrap availability and quality limit full substitution, as recycled steel may contain impurities that restrict its use in high-grade applications. We base the growth in scrap use in EAFs on historical trends in Europe, where the share of scrap in total steel production increased from 52% in 2014 to 58% in 2022 [[61](https://arxiv.org/html/2510.08199v1#bib.bibx61)]. Extrapolating this trajectory yields an upper limit of 83% by 2050, which we cap at 75% to stay conservative, which is reached around 2040. Incorporating steel scrap utilization as a decarbonization pathway is highly relevant, as previous studies show it can directly affect the demand for green hydrogen in steel production [[84](https://arxiv.org/html/2510.08199v1#bib.bibx84), [85](https://arxiv.org/html/2510.08199v1#bib.bibx85)].

Other steel-making processes exist but are less commonly used. The Smelting Reduction (SR) process converts iron ore directly into liquid iron using coal in a single-step process. Open Hearth Furnaces (OHF), which have largely been phased out in most regions, still account for 19% of steel production in Ukraine [[86](https://arxiv.org/html/2510.08199v1#bib.bibx86)]. Biomass-based reduction, utilizing charcoal as a substitute for fossil-based coke, is also employed, particularly in Brazil [[87](https://arxiv.org/html/2510.08199v1#bib.bibx87)]. An emerging technology in steel production is Molten Oxide Electrolysis (MOE), which directly converts iron ore into molten iron through electrolysis, eliminating the need for carbon-based reducing agents; however, this method remains in early research and development stages.
In 2023, Europe’s steel production reached approximately 170 million tonnes (126 inside EU), using for around 55% the BF-BOF route and for 45% the Electric Arc Route. Of the latter, only 1% of the production of iron employs DRI, while the rest uses scrap as a feedstock to the electric arc [[86](https://arxiv.org/html/2510.08199v1#bib.bibx86), [67](https://arxiv.org/html/2510.08199v1#bib.bibx67), [88](https://arxiv.org/html/2510.08199v1#bib.bibx88)]. The most effective strategies for decarbonizing the steel sector involve transitioning from BF-BOF production to either Scrap-EAF or Hydrogen-based DRI-EAF (H2-DRI-EAF), both of which relying on renewable electricity, either for direct use in the electric arc furnace and for hydrogen production via electrolysis. An alternative approach is the implementation of carbon capture technologies, such as Top Gas Recycling (TGR), within existing BF-BOF plants, retrofitting facilities to capture and sequester carbon emissions. To summarize, the steel-making processes included in the model are BF-BOF, DRI-EAF fuelled with natural gas or hydrogen, scrap-EAF and retrofitting BF-BOF plants with TGR.

Cement

Cement production is a highly energy-intensive process and a major contributor to global CO2 emissions, primarily due to both fuel combustion and the chemical decomposition of limestone (calcination). The predominant method of cement manufacturing (80% worldwide) is the dry clinker production process, in which limestone and other raw materials are heated in a rotary kiln at temperatures exceeding 1400°C to form clinker, the key binding agent in cement [[89](https://arxiv.org/html/2510.08199v1#bib.bibx89)]. The wet process, now largely phased out due to its larger energy demands, was initially developed for its simpler pre-processing, especially for raw materials with high moisture content. EU27 cement production reached approximately 161 million tonnes in 2023, with the vast majority manufactured using the dry clinker route [[90](https://arxiv.org/html/2510.08199v1#bib.bibx90)]. Several strategies have been proposed to mitigate CO2 emissions in cement production, including reducing the cement-to-clinker ratio by using supplementary cementitious materials (SCMs) like fly ash or calcined clay, improving energy efficiency in clinker production, implementing CCS, and electrifying the clinker production process with renewable electricity [[91](https://arxiv.org/html/2510.08199v1#bib.bibx91), [92](https://arxiv.org/html/2510.08199v1#bib.bibx92)]. The cement production process considered in the model is limited to traditional dry clinker production, with the potential for retrofitting with CCS. The electrification of cement production processes currently depends on plasma technologies or indirect electrification via hydrogen [[93](https://arxiv.org/html/2510.08199v1#bib.bibx93)]. However, due to the low maturity of these technologies, they are excluded from the scope of this study.

Chemicals

The chemical sectors developed in PyPSA-Eur include methanol, ammonia, and ethylene, the latter serving as a proxy for production of all types of plastics. Currently, methanol is mainly produced through a methanol synthesis process, employing syngas generated via steam methane reforming (SMR). Ammonia production, predominantly via the Haber-Bosch process, also relies on natural gas for hydrogen production, while ethylene is produced via steam cracking of hydrocarbons, which is a highly energy-intensive process that involves the decomposition of naphtha.

Efforts to reduce emissions in these sectors focus on several strategies. For ammonia synthesis, the electrification of hydrogen production for the Haber-Bosch process is considered the most viable solution, as it would allow keeping existing production capacities. Similarly, methanol can be synthesized from green hydrogen, but achieving a fully renewable process requires CO2 inputs derived from carbon capture and utilization (CCU) or from biomass. In this study, the biomass pathway is omitted for simplicity, as the sustainable biomass potential within Europe [[56](https://arxiv.org/html/2510.08199v1#bib.bibx56)] is largely allocated to BECCS and biomass Combined Heat and Power (CHP) generation. Ethylene and other HVCs can be produced from naphtha of various origins, all serving as feedstock for steam cracking facilities. The model considers fossil-derived naphtha, biomass-to-liquid naphtha, and synthetic naphtha generated via CCU through the Fischer–Tropsch process. Another pathway for HVCs synthesis is the conversion of methanol to olefins, which is not included for simplicity.

The model accounts for emissions from methanol utilization and the end-of-life degradation of HVCs in landfills, thereby incentivize process decarbonization. These emissions are also incorporated into the commodity price through the application of the carbon price. Plastic recycling represents another possible mitigation pathway; however, it has not been included in the model, both to maintain simplicity in the accounting of CO2 emissions, since recycling alters the timing and location of carbon release, and because recycling is inherently limited by material degradation and cannot be sustained indefinitely [[94](https://arxiv.org/html/2510.08199v1#bib.bibx94)]. Nevertheless, its importance is acknowledged, with 8.7 Mt of plastics recycled in Europe in 2022 [[95](https://arxiv.org/html/2510.08199v1#bib.bibx95)], and it should be incorporated in future analyses.

Data on the location, type, and age of existing plants are obtained from the Global Energy Monitor [[96](https://arxiv.org/html/2510.08199v1#bib.bibx96)], the Spatial Finance Initiative [[97](https://arxiv.org/html/2510.08199v1#bib.bibx97)], and the Supplementary Materials of Neuwirth et al. [[24](https://arxiv.org/html/2510.08199v1#bib.bibx24)]. Iron ore cost assumptions are detailed in [[98](https://arxiv.org/html/2510.08199v1#bib.bibx98)], while the cost of limestone is taken from [[74](https://arxiv.org/html/2510.08199v1#bib.bibx74)] and set at 35 million EUR per kilotonne of limestone. Table [A.1](https://arxiv.org/html/2510.08199v1#A1.T1 "Table A.1 ‣ A.1 Industrial sectors modelling ‣ Appendix A Supplementary Materials ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation") in Supplementary Material provides an overview of the technical parameters included in this extension of PyPSA-Eur. These comprehend energy inputs, emission factors, capital expenditure (CAPEX), operational expenditure (OPEX) where available, and assumed lifetimes. The table also indicates the sources for each parameter, which were cross-checked against values reported in the literature to ensure consistency within typical ranges. While the majority of parameters are drawn from Technology Data [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)], more specific sources are specified when available.

Table A.1: Detailed technical and cost parameters for steel and cement sectors by technology.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Sector | Technology | Parameter | Value (year) | Unit | Reference |
| Steel | BF-BOF | Iron input | 1.8 | kt iron/kt steel | [[23](https://arxiv.org/html/2510.08199v1#bib.bibx23)] |
| Coal input | 6342 | MWhth/kt steel | [[23](https://arxiv.org/html/2510.08199v1#bib.bibx23)] |
| Electricity input | 194 | MWh/kt steel | [[23](https://arxiv.org/html/2510.08199v1#bib.bibx23)] |
| Emission factor | 1760 | tCO2/kt of steel | [[23](https://arxiv.org/html/2510.08199v1#bib.bibx23)] |
| CAPEX | 871.85 | milEUR/kt steel | [[98](https://arxiv.org/html/2510.08199v1#bib.bibx98)] |
| OPEX | 123.67 | milEUR/kt steel | [[98](https://arxiv.org/html/2510.08199v1#bib.bibx98)] |
| Lifetime | 25 | years | [[23](https://arxiv.org/html/2510.08199v1#bib.bibx23)] |
| NG DRI-EAF | Iron input | 1.36 | kt iron/kt steel | [[99](https://arxiv.org/html/2510.08199v1#bib.bibx99)] |
| NG input | 2803 | MWhth/kt steel | [[99](https://arxiv.org/html/2510.08199v1#bib.bibx99)] |
| Electricity input | 554 | MWh/kt steel | [[99](https://arxiv.org/html/2510.08199v1#bib.bibx99)] |
| Emission factor | 565 | tCO2/kt steel | [[99](https://arxiv.org/html/2510.08199v1#bib.bibx99)] |
| CAPEX | 698.34 | milEUR/kt steel/a | [[98](https://arxiv.org/html/2510.08199v1#bib.bibx98)] |
| OPEX | 118.27 | milEUR/kt steel/a | [[98](https://arxiv.org/html/2510.08199v1#bib.bibx98)] |
| Lifetime | 40 | years | [[98](https://arxiv.org/html/2510.08199v1#bib.bibx98)] |
| H2 DRI-EAF | Iron input | 1.39 | kt iron/kt steel | [[99](https://arxiv.org/html/2510.08199v1#bib.bibx99)] |
| H2 input | 2211 | MWhth/kt steel | [[99](https://arxiv.org/html/2510.08199v1#bib.bibx99)] |
| Electricity input | 611 | MWh/kt steel | [[99](https://arxiv.org/html/2510.08199v1#bib.bibx99)] |
| Emission factor | 76 | tCO2/kt steel | [[99](https://arxiv.org/html/2510.08199v1#bib.bibx99)] |
| CAPEX | 698.34 | milEUR/kt steel/a | [[98](https://arxiv.org/html/2510.08199v1#bib.bibx98)] |
| OPEX | 118.27 | milEUR/kt steel/a | [[98](https://arxiv.org/html/2510.08199v1#bib.bibx98)] |
| Lifetime | 40 | years | [[98](https://arxiv.org/html/2510.08199v1#bib.bibx98)] |
| Scrap-EAF | Scrap price | 280 | milEUR/kt scrap | [[99](https://arxiv.org/html/2510.08199v1#bib.bibx99)] |
| Electricity input | 640 | MWh/kt steel | [[98](https://arxiv.org/html/2510.08199v1#bib.bibx98)] |
| Direct emission factor | 0 | tCO2/kt steel |  |
| CAPEX | 210 | milEUR/kt steel/a | [[98](https://arxiv.org/html/2510.08199v1#bib.bibx98)] |
| OPEX | 63 | milEUR/kt steel/a | [[98](https://arxiv.org/html/2510.08199v1#bib.bibx98)] |
| Lifetime | 40 | years | [[98](https://arxiv.org/html/2510.08199v1#bib.bibx98)] |
| Retrofit TGR on BF-BOF | Electricity input | 0.107 (2030), 0.095 (2040), 0.093 (2050) | MWh/tCO2 | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
| Capture rate | 90 (2030), 95 (2040, 2050) | % | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
| CAPEX | 297 (2030), 251 (2040), 205 (2050) | EUR/tCO2 | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
|  | Lifetime | 25 | years | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
| Cement | Cement Plant | Limestone input | 1.28 | kt limestone/kt cement | [[100](https://arxiv.org/html/2510.08199v1#bib.bibx100)] |
| NG input | 1900 | MWhht{}\_{t}h/kt cement | [[100](https://arxiv.org/html/2510.08199v1#bib.bibx100)] |
| Emission factor | 500 | tCO2/kt cement | [[100](https://arxiv.org/html/2510.08199v1#bib.bibx100)] |
| CAPEX | 263 | milEUR/kt cement | ETSAP |
| Lifetime | 25 | years | [[23](https://arxiv.org/html/2510.08199v1#bib.bibx23)] |
| Retrofit TGR on cement plant | Electricity input | 0.107 (2030), 0.095 (2040), 0.093 (2050) | MWh/tCO2 | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
| Capture rate | 90 (2030), 95 (2040, 2050) | % | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
| CAPEX | 297 (2030), 251 (2040), 205 (2050) | EUR/tCO2 | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
| Lifetime | 25 | years | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
| Ammonia | Haber-Bosch | Electricity input | 0.2473 | MWhle{}\_{e}l/MWh NH3 | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
| H2 input | 1.1484 | MWhht{}\_{t}h/MWh NH3 | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
| CAPEX | 166.67 (2030), 136.32 (2040), 104.51 (2050) | EUR/MWh NH3/a | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
| OPEX | 0.0225 | EUR/MWh NH3 | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
| Lifetime | 30 | years | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
| Methanol | Methanolisation | Electricity input | 0.271 | MWhle{}\_{e}l/MWh methanol | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
| H2 input | 1.138 | MWhht{}\_{t}h/MWh methanol | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
| EOL emissions | 0.248 | t CO2/MWh methanol | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
| CAPEX | 80.33 (2030), 69.83 (2040), 59.33 (2050) | EUR/MWh methanol/a | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
| Lifetime | 20 | years | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
| HVCs | Naphtha steam cracker | Naphtha input | 28806 | MWh naphtha/kt HVC | [[23](https://arxiv.org/html/2510.08199v1#bib.bibx23)] |
| Electricity input | 135 | MWhle{}\_{e}l/kt HVC | [[23](https://arxiv.org/html/2510.08199v1#bib.bibx23)] |
| H2 output | 0.699 | MWh H2/kt HVC | [[23](https://arxiv.org/html/2510.08199v1#bib.bibx23)] |
| EOL emissions | 0.2571 | t CO2/MWh naphtha | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
| CAPEX | 1817 | milEUR/kt HVC | [[77](https://arxiv.org/html/2510.08199v1#bib.bibx77)] |
| Lifetime | 30 | years | [[23](https://arxiv.org/html/2510.08199v1#bib.bibx23)] |
| Bio-naphtha production | Biomass input | 0.3833 (2030), 0.4167 (2040), 0.45 (2050) | MWh biomass/MWh naphtha | [[101](https://arxiv.org/html/2510.08199v1#bib.bibx101)] |
| CO2 in biomass | 0.0979 (2030), 0.1072 (2040), 0.1157 (2050) | t CO2/MWh biomass | [[101](https://arxiv.org/html/2510.08199v1#bib.bibx101)] |
| CAPEX | 3118.43 | milEUR/MW | [[102](https://arxiv.org/html/2510.08199v1#bib.bibx102)] |
| Lifetime | 25 | years | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
| Fischer-Tropsch | H2 input | 1.252 | MWh H2/MWh naphtha | [[103](https://arxiv.org/html/2510.08199v1#bib.bibx103)] |
| CO2 input | 0.2571 | t CO2/MWh naphtha | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
| CAPEX | 703.726 | milEUR/MW | [[103](https://arxiv.org/html/2510.08199v1#bib.bibx103)] |
| Lifetime | 20 | years | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
| Hydrogen | Electrolysers | Electricity input | 0.6217 (2030), 0.6532 (2040), 0.6994 (2050) | MWhle{}\_{e}l/MWh H2 | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
| CAPEX | 1500 (2030), 1200 (2040), 1000 (2050) | milEUR/MW | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
| Lifetime | 25 | years | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
| Steam Methane Reformer | NG input | 0.76 | MWh NG/MWh H2 | [[104](https://arxiv.org/html/2510.08199v1#bib.bibx104)] |
| Emission factor | 0.198 | t CO2/MWh NG | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
| CAPEX | 396.87 | milEUR/MW H2 | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
| Lifetime | 30 | years | [[104](https://arxiv.org/html/2510.08199v1#bib.bibx104)] |
| Steam Methane Reformer + CC | NG input | 0.69 | MWh NG/MWh H2 | [[104](https://arxiv.org/html/2510.08199v1#bib.bibx104)] |
| CO2 out | 10 | % | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
| CO2 captured | 90 | % | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
| CAPEX | 417.97 | milEUR/MW H2 | [[55](https://arxiv.org/html/2510.08199v1#bib.bibx55)] |
| Lifetime | 30 | years | [[104](https://arxiv.org/html/2510.08199v1#bib.bibx104)] |

### A.2 Extra indicators for energy sectors

To complement Figure [2](https://arxiv.org/html/2510.08199v1#S4.F2 "Figure 2 ‣ 4.1 Decarbonisation and competitiveness ‣ 4 Results and discussion ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation") and Figure [5](https://arxiv.org/html/2510.08199v1#S4.F5 "Figure 5 ‣ 4.2 Industrial relocation and green intermediates trade ‣ 4 Results and discussion ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation"), we examine the role of hydrogen production across the scenarios. Hydrogen produced via electrolysis is classified as either green or grey, depending on the carbon intensity of the electricity used: it is considered grey when generated using electricity from CO2-emitting sources, and green when produced from low-carbon electricity. From 2040 onwards, green hydrogen becomes a key element of the industrial decarbonisation pathway. In the Reindustrialization scenarios, our estimates reach almost twice the level projected by Hydrogen Europe (35 Mtons by 2040 [[105](https://arxiv.org/html/2510.08199v1#bib.bibx105)]), but production is reduced if Intermediates Imports are allowed. The Continued Decline scenarios maintain a more comparable European hydrogen generation. As a reference, the European Commission has set a target of 10 Mtons by 2030 [[64](https://arxiv.org/html/2510.08199v1#bib.bibx64)].

![Refer to caption](figures/hydrogen_pies.png)


Figure A.1: Hydrogen production in five scenarios: the first column represent the scenario with No Climate Policy and Stabilization of industrial production; the two columns in the middle show scenarios implementing the EU Climate Policies for Continued Decline and Reindustrialization, with No Intermediate Imports; the two columns on the right represent Climate Policies for Continued Decline and Reindustrialization, with Intermediate Imports. The radius of each pie chart is proportional to the total quantity indicated above it, while the segment shares represent the contribution of each production technology.

In Figure [A.2](https://arxiv.org/html/2510.08199v1#A1.F2 "Figure A.2 ‣ A.2 Extra indicators for energy sectors ‣ Appendix A Supplementary Materials ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation"), we present key energy system indicators to provide insight into the underlying dynamics of the modelled scenarios. The panel on the left displays the average electricity price, represented by the Lagrange multipliers λn,t\lambda\_{n,t}, which correspond to the marginal cost of producing electricity in region nn at time step tt. We report the annual European average electricity price for each future year in the pathway (2030, 2040, and 2050), denoted as e​l​p​r​i​c​eE​U,y​e​a​relprice\_{EU,year}. This value is computed as a weighted average over all regions and time steps, as defined in Equation [A.1](https://arxiv.org/html/2510.08199v1#A1.E1 "In A.2 Extra indicators for energy sectors ‣ Appendix A Supplementary Materials ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation"), where e​l​p​r​i​c​en,telprice\_{n,t} and Pn,tP\_{n,t} are respectively the Lagrange multiplier for electricity and the power production in nation nn and timestep tt, with Δ​t\Delta t is the timestep, in this case of 3 hours.

|  |  |  |  |
| --- | --- | --- | --- |
|  | e​l​p​r​i​c​e¯E​U,y​e​a​r=∑nN∑tTe​l​p​r​i​c​en,t⋅Pn,t⋅Δ​t∑nN∑tTPn,t⋅Δ​t\overline{elprice}\_{EU,year}=\frac{\sum\_{n}^{N}\sum\_{t}^{T}elprice\_{n,t}\cdot P\_{n,t}\cdot\Delta t}{\sum\_{n}^{N}\sum\_{t}^{T}P\_{n,t}\cdot\Delta t} |  | (A.1) |

The central panel illustrates the share of electricity generated from low-carbon sources for each simulated year. In this context, ”green electricity” refers to electricity produced from technologies that do not emit CO2 during operation. These include reservoir hydro, Run-of-River (RoR), solar PV , on- and off- shore wind, biomass, and nuclear technologies, as modelled in the system.

The share of green electricity, denoted as selec,ygreens^{\text{green}}\_{\text{elec},y} in year yy, is defined as the ratio of total electricity generated by green sources to the total electricity generation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​U​s​h​a​r​eg​r​e​e​n​e​l​e​c=∑tT∑g∈GgreenPg,t⋅Δ​t∑g∈GPg,t⋅Δ​tEUshare\_{greenelec}=\sum\_{t}^{T}\frac{\sum\limits\_{g\in G\_{\text{green}}}P\_{g,t}\cdot\Delta t}{\sum\limits\_{g\in G}P\_{g,t}\cdot\Delta t} |  | (A.2) |

Where:

Pg,tP\_{g,t} is the power output of generator gg at time tt

GgreenG\_{\text{green}} is the set of green (non-emitting) generators

GG is the set of all generators

TyT\_{y} is the set of time steps in year yy

Δ​t\Delta t is the duration of each time step (can be omitted if uniform)

The panel on the right displays the CO2 price, which, in a linear energy system optimisation model, arises as the shadow price (or dual variable) associated with the constraint on total allowable CO2 emissions. The model seeks to minimize total system costs subject to technical, economic, and environmental constraints, including a cap on cumulative CO2 emissions. For a detailed description of the objective function and the implementation of the CO2 constraint in PyPSA-Eur, refer to [[28](https://arxiv.org/html/2510.08199v1#bib.bibx28)]. From an economic perspective, the CO2 price μC​O2​L​i​m​i​t\mu\_{CO\_{2}Limit} represents the marginal cost of tightening the CO2 emissions constraint. It quantifies the increase in total system cost resulting from a one-unit decrease (e.g., one tonne) in the permissible CO2 emissions:

|  |  |  |  |
| --- | --- | --- | --- |
|  | μC​O2​L​i​m​i​t=∂System Cost∂C​O2​L​i​m​i​t\mu\_{CO\_{2}Limit}=\frac{\partial\text{System Cost}}{\partial CO\_{2}Limit} |  | (A.3) |

Electricity prices do not increase significantly in the Climate Policy scenarios (as in Figure [A.2](https://arxiv.org/html/2510.08199v1#A1.F2 "Figure A.2 ‣ A.2 Extra indicators for energy sectors ‣ Appendix A Supplementary Materials ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation")). This is primarily because the decarbonization of the power sector remains relatively consistent even in the No Climate Policy cases, driven by the projected low costs of solar PV and wind turbines in the coming decades. The graphs present only the average price across time and model nodes, as we found the inclusion of price volatility to add limited additional insights. Indeed, the variation in volatility across scenarios is negligible, likely reflecting the consistently high penetration of renewable energy technologies in each case. In the Climate Policy scenarios, electricity generation is almost entirely based on renewable sources by 2030. In contrast, under the No Climate Policy, the share of renewable electricity stabilizes around 85%, meaning that fossil-fuel-based generation is still required during peak demand periods. The third graphs reports the carbon prices, representing the required cost of CO2 emissions to achieve the emission reduction targets in an economically efficient manner. In practice, they reflect the price level necessary to increase the marginal costs of emitting technologies sufficiently to incentivize the adoption and deployment of zero-emission alternatives.

![Refer to caption](figures/electricity_share_cprice.png)


Figure A.2: Evolution of key energy system indicators under different policy and industrialization scenarios. Left: electricity price, averaged across regions and timesteps [EUR/MWh]. Center: Share of green electricity in total supply [%]. Right: CO2 price [EUR/ton of CO2] (note that scenarios with No Climate Policy have no carbon price). The scenarios compare pathways with and without Climate Policy, as well as differing industrialization trends (Continued Decline vs. Reindustrialization).

### A.3 Robustness check on hydrogen infrastructure

Figure [A.3](https://arxiv.org/html/2510.08199v1#A1.F3 "Figure A.3 ‣ A.3 Robustness check on hydrogen infrastructure ‣ Appendix A Supplementary Materials ‣ Pursuing decarbonization and competitiveness: a narrow corridor for European green industrial transformation") shows that the presence or absence of a hydrogen transmission grid has only a modest effect on time-averaged European prices for industrial commodities. In 2040, a slight reduction in production costs is observed for hydrogen-intensive products such as ammonia, methanol, and steel. The average cost of hydrogen itself remains largely unchanged, as lower electricity expenditures when using the grid are offset by the capital costs of pipeline infrastructure. While the grid could provide marginal benefits for hydrogen-dependent commodities, the pace and uncertainty of hydrogen market and infrastructure development make it a challenging option to rely upon for industrial decarbonisation strategies.

![Refer to caption](figures/commodity_prices_h2.png)


Figure A.3: Prices of industrial goods, average across European countries and time steps, for different scenarios: Continued Decline with No H2 Grid and with H2 Grid, Reindustrialization with No H2 Grid and with H2 Grid. The scenarios with No H2 Grid are the part of the Main Scenarios, the others are compared for a robustness check.

## References

* [1]
  “European Climate Law”
  URL: <https://climate.ec.europa.eu/eu-action/european-climate-law_en>
* [2]
  “Europe – Countries & Regions”
  In *IEA*
  URL: <https://www.iea.org/regions/europe/emissions>
* [3]
  “Net-Zero Industry Act - European Commission”
  URL: <https://commission.europa.eu/strategy-and-policy/priorities-2019-2024/european-green-deal/green-deal-industrial-plan/net-zero-industry-act_en>
* [4]
  “Clean Industrial Deal - European Commission”
  URL: <https://commission.europa.eu/topics/eu-competitiveness/clean-industrial-deal_en>
* [5]
  “EU competitiveness: Looking ahead - European Commission”
  URL: <https://commission.europa.eu/topics/eu-competitiveness/eu-competitiveness-looking-ahead_en>
* [6]
  “EEA greenhouse gases — data viewer”, 2024
  URL: <https://www.eea.europa.eu/en/analysis/maps-and-charts/greenhouse-gases-viewer-data-viewers>
* [7]
  Máté Rózsai et al.
  “JRC-IDEES-2021: the Integrated Database of the European Energy System – Data update and technical documentation” ISBN: 9789268161548 ISSN: 1831-9424
  In *JRC Publications Repository*, 2024
  DOI: [10.2760/614599](https://dx.doi.org/10.2760/614599)
* [8]
  Ryan Jones et al.
  “Electrification and the Future of Electricity Markets: Transitioning to a Low-Carbon Energy System”
  In *IEEE Power and Energy Magazine* 16.4, 2018, pp. 79–89
  DOI: [10.1109/MPE.2018.2823479](https://dx.doi.org/10.1109/MPE.2018.2823479)
* [9]
  Gunnar Luderer et al.
  “Residual fossil CO2 emissions in 1.5–2 °C pathways” Publisher: Nature Publishing Group
  In *Nature Climate Change* 8.7, 2018, pp. 626–633
  DOI: [10.1038/s41558-018-0198-6](https://dx.doi.org/10.1038/s41558-018-0198-6)
* [10]
  Chao Chen, Yangsiyu Lu and Rene Banares-Alcantara
  “Direct and indirect electrification of chemical industry using methanol production as a case study”
  In *Applied Energy* 243, 2019, pp. 71–90
  DOI: [10.1016/j.apenergy.2019.03.184](https://dx.doi.org/10.1016/j.apenergy.2019.03.184)
* [11]
  Max Wei, Colin A. McMillan and Stephane Rue du Can
  “Electrification of Industry: Potential, Challenges and Outlook”
  In *Current Sustainable/Renewable Energy Reports* 6.4, 2019, pp. 140–148
  DOI: [10.1007/s40518-019-00136-1](https://dx.doi.org/10.1007/s40518-019-00136-1)
* [12]
  Otavio Cavalett et al.
  “Paving the way for sustainable decarbonization of the European cement industry” Publisher: Nature Publishing Group
  In *Nature Sustainability* 7.5, 2024, pp. 568–580
  DOI: [10.1038/s41893-024-01320-y](https://dx.doi.org/10.1038/s41893-024-01320-y)
* [13]
  Timo Gerres, José Pablo Chaves Ávila, Pedro Linares Llamas and Tomás Gómez San Román
  “A review of cross-sector decarbonisation potentials in the European energy intensive industry”
  In *Journal of Cleaner Production* 210, 2019, pp. 585–601
  DOI: [10.1016/j.jclepro.2018.11.036](https://dx.doi.org/10.1016/j.jclepro.2018.11.036)
* [14]
  Fabian Neumann, Johannes Hampp and Tom Brown
  “Green energy and steel imports reduce Europe’s net-zero infrastructure needs” Publisher: Nature Publishing Group
  In *Nature Communications* 16.1, 2025, pp. 5302
  DOI: [10.1038/s41467-025-60652-1](https://dx.doi.org/10.1038/s41467-025-60652-1)
* [15]
  Hilton Trollip, Bryce McCall and Chris Bataille
  “How green primary iron production in South Africa could help global decarbonization” Publisher: Taylor & Francis \_eprint: https://doi.org/10.1080/14693062.2021.2024123
  In *Climate Policy* 22.2, 2022, pp. 236–247
  DOI: [10.1080/14693062.2021.2024123](https://dx.doi.org/10.1080/14693062.2021.2024123)
* [16]
  Sascha Samadi, Andreas Fischer and Stefan Lechtenböhmer
  “The renewables pull effect: How regional differences in renewable energy costs could influence where industrial production is located in the future”
  In *Energy Research & Social Science* 104, 2023, pp. 103257
  DOI: [10.1016/j.erss.2023.103257](https://dx.doi.org/10.1016/j.erss.2023.103257)
* [17]
  Philipp C. Verpoort, Lukas Gast, Anke Hofmann and Falko Ueckerdt
  “Impact of global heterogeneity of renewable energy supply on heavy industrial production and green value chains” Publisher: Nature Publishing Group
  In *Nature Energy* 9.4, 2024, pp. 491–503
  DOI: [10.1038/s41560-024-01492-z](https://dx.doi.org/10.1038/s41560-024-01492-z)
* [18]
  Tianming Shao et al.
  “China’s industrial decarbonization in the context of carbon neutrality: A sub-sectoral analysis based on integrated modelling”
  In *Renewable and Sustainable Energy Reviews* 170, 2022, pp. 112992
  DOI: [10.1016/j.rser.2022.112992](https://dx.doi.org/10.1016/j.rser.2022.112992)
* [19]
  Raymond R Tan, Maria Victoria Migo-Sumagang and Kathleen B Aviso
  “Recent trends in optimization models for industrial decarbonization”
  In *Current Opinion in Chemical Engineering* 48, 2025, pp. 101118
  DOI: [10.1016/j.coche.2025.101118](https://dx.doi.org/10.1016/j.coche.2025.101118)
* [20]
  Huan Wang and Wenying Chen
  “Modelling deep decarbonization of industrial energy consumption under 2-degree target: Comparing China, India and Western Europe”
  In *Applied Energy* 238, 2019, pp. 1563–1572
  DOI: [10.1016/j.apenergy.2019.01.131](https://dx.doi.org/10.1016/j.apenergy.2019.01.131)
* [21]
  Benjamin K. Sovacool, Frank W. Geels and Marfuga Iskandarova
  “Industrial clusters for deep decarbonization” Publisher: American Association for the Advancement of Science
  In *Science* 378.6620, 2022, pp. 601–604
  DOI: [10.1126/science.add0402](https://dx.doi.org/10.1126/science.add0402)
* [22]
  Silvia Madeddu et al.
  “The CO2 reduction potential for the European industry via direct electrification of heat supply (power-to-heat)” Publisher: IOP Publishing
  In *Environmental Research Letters* 15.12, 2020, pp. 124004
  DOI: [10.1088/1748-9326/abbd02](https://dx.doi.org/10.1088/1748-9326/abbd02)
* [23]
  Quentin Raillard–Cazanove, Antoine Rogeau and Robin Girard
  “Decarbonisation modelling for key industrial sectors focusing on process changes in a cost-optimised pathway”
  In *Applied Energy* 382, 2025, pp. 125206
  DOI: [10.1016/j.apenergy.2024.125206](https://dx.doi.org/10.1016/j.apenergy.2024.125206)
* [24]
  Marius Neuwirth, Tobias Fleiter and René Hofmann
  “Modelling the market diffusion of hydrogen-based steel and basic chemical production in Europe – A site-specific approach”
  In *Energy Conversion and Management* 322, 2024, pp. 119117
  DOI: [10.1016/j.enconman.2024.119117](https://dx.doi.org/10.1016/j.enconman.2024.119117)
* [25]
  Daniele Groppi et al.
  “Energy modelling challenges for the full decarbonisation of hard-to-abate sectors”
  In *Renewable and Sustainable Energy Reviews* 209, 2025, pp. 115103
  DOI: [10.1016/j.rser.2024.115103](https://dx.doi.org/10.1016/j.rser.2024.115103)
* [26]
  Yohannes A. Alamerew and Eric Masanet
  “Evaluation of industrial decarbonization energy system models for policymaking: literature gaps and research recommendations”
  In *Procedia CIRP* 116, 30th CIRP Life Cycle Engineering Conference, 2023, pp. 666–671
  DOI: [10.1016/j.procir.2023.02.112](https://dx.doi.org/10.1016/j.procir.2023.02.112)
* [27]
  T. Brown et al.
  “Synergies of sector coupling and transmission reinforcement in a cost-optimised, highly renewable European energy system”
  In *Energy* 160, 2018, pp. 720–739
  DOI: [10.1016/j.energy.2018.06.222](https://dx.doi.org/10.1016/j.energy.2018.06.222)
* [28]
  Marta Victoria, Elisabeth Zeyen and Tom Brown
  “Speed of technological transformations required in Europe to achieve different climate goals” Publisher: Elsevier
  In *Joule* 6.5, 2022, pp. 1066–1086
  DOI: [10.1016/j.joule.2022.04.016](https://dx.doi.org/10.1016/j.joule.2022.04.016)
* [29]
  Gondia S. Seck et al.
  “Hydrogen and the decarbonization of the energy system in europe in 2050: A detailed model-based analysis”
  In *Renewable and Sustainable Energy Reviews* 167, 2022, pp. 112779
  DOI: [10.1016/j.rser.2022.112779](https://dx.doi.org/10.1016/j.rser.2022.112779)
* [30]
  Bryn Pickering, Francesco Lombardi and Stefan Pfenninger
  “Diversity of options to eliminate fossil fuels and reach carbon neutrality across the entire European energy system”
  In *Joule* 6.6, 2022, pp. 1253–1276
  DOI: [10.1016/j.joule.2022.05.009](https://dx.doi.org/10.1016/j.joule.2022.05.009)
* [31]
  Manuel Wetzel, Hans Christian Gils and Valentin Bertsch
  “Green energy carriers and energy sovereignty in a climate neutral European energy system”
  In *Renewable Energy* 210, 2023, pp. 591–603
  DOI: [10.1016/j.renene.2023.04.015](https://dx.doi.org/10.1016/j.renene.2023.04.015)
* [32]
  Nicolas Wolf, Michelle Antje Tanneberger and Michael Höck
  “Levelized cost of hydrogen production in Northern Africa and Europe in 2050: A Monte Carlo simulation for Germany, Norway, Spain, Algeria, Morocco, and Egypt” Publisher: Elsevier BV
  In *International Journal of Hydrogen Energy* 69, 2024, pp. 184–194
  DOI: [10.1016/j.ijhydene.2024.04.319](https://dx.doi.org/10.1016/j.ijhydene.2024.04.319)
* [33]
  Mahdi Fasihi, Dmitrii Bogdanov and Christian Breyer
  “Long-Term Hydrocarbon Trade Options for the Maghreb Region and Europe—Renewable Energy Based Synthetic Fuels for a Net Zero Emissions World” Number: 2 Publisher: Multidisciplinary Digital Publishing Institute
  In *Sustainability* 9.2, 2017, pp. 306
  DOI: [10.3390/su9020306](https://dx.doi.org/10.3390/su9020306)
* [34]
  “Global Hydrogen Trade to Meet the 1.5°C Climate Goal: Part II”, 2022
  URL: <https://www.irena.org/publications/2022/Apr/Global-hydrogen-trade-Part-II>
* [35]
  Florian Egli et al.
  “Mapping the cost competitiveness of African green hydrogen imports to Europe” Publisher: Nature Publishing Group
  In *Nature Energy* 10.6, 2025, pp. 750–761
  DOI: [10.1038/s41560-025-01768-y](https://dx.doi.org/10.1038/s41560-025-01768-y)
* [36]
  Bob Zwaan, Sam Lamboo and Francesco Dalla Longa
  “Timmermans’ dream: An electricity and hydrogen partnership between Europe and North Africa”
  In *Energy Policy* 159, 2021, pp. 112613
  DOI: [10.1016/j.enpol.2021.112613](https://dx.doi.org/10.1016/j.enpol.2021.112613)
* [37]
  Fabian Carels, Lucas Sens and Martin Kaltschmitt
  “Synthetic natural gas as a green hydrogen carrier – Technical, economic and environmental assessment of several supply chain concepts”
  In *Energy Conversion and Management* 321, 2024, pp. 118940
  DOI: [10.1016/j.enconman.2024.118940](https://dx.doi.org/10.1016/j.enconman.2024.118940)
* [38]
  Jonas Egerer, Veronika Grimm, Kiana Niazmand and Philipp Runge
  “The economics of global green ammonia trade – “Shipping Australian wind and sunshine to Germany””
  In *Applied Energy* 334, 2023, pp. 120662
  DOI: [10.1016/j.apenergy.2023.120662](https://dx.doi.org/10.1016/j.apenergy.2023.120662)
* [39]
  Tansu Galimova, Mahdi Fasihi, Dmitrii Bogdanov and Christian Breyer
  “Feasibility of green ammonia trading via pipelines and shipping: Cases of Europe, North Africa, and South America”
  In *Journal of Cleaner Production* 427, 2023, pp. 139212
  DOI: [10.1016/j.jclepro.2023.139212](https://dx.doi.org/10.1016/j.jclepro.2023.139212)
* [40]
  Kaifeng Yu and Paul Son
  “Review of trans-Mediterranean power grid interconnection: A regional roadmap towards energy sector decarbonization”
  In *Global Energy Interconnection* 6.1, 2023, pp. 115–126
  DOI: [10.1016/j.gloei.2023.02.010](https://dx.doi.org/10.1016/j.gloei.2023.02.010)
* [41]
  Franz Trieb, Christoph Schillings, Thomas Pregger and Marlene O’Sullivan
  “Solar electricity imports from the Middle East and North Africa to Europe”
  In *Energy Policy* 42, 2012, pp. 341–353
  DOI: [10.1016/j.enpol.2011.11.091](https://dx.doi.org/10.1016/j.enpol.2011.11.091)
* [42]
  Lina Reichenberg, Fredrik Hedenus, Niclas Mattsson and Vilhelm Verendel
  “Deep decarbonization and the supergrid – Prospects for electricity transmission between Europe and China”
  In *Energy* 239, 2022, pp. 122335
  DOI: [10.1016/j.energy.2021.122335](https://dx.doi.org/10.1016/j.energy.2021.122335)
* [43]
  Mokhtar Benasla et al.
  “The transition towards a sustainable energy system in Europe: What role can North Africa’s solar resources play?”
  In *Energy Strategy Reviews* 24, 2019, pp. 1–13
  DOI: [10.1016/j.esr.2019.01.007](https://dx.doi.org/10.1016/j.esr.2019.01.007)
* [44]
  Gabriel Lopez et al.
  “Towards defossilised steel: Supply chain options for a green European steel industry”
  In *Energy* 273, 2023, pp. 127236
  DOI: [10.1016/j.energy.2023.127236](https://dx.doi.org/10.1016/j.energy.2023.127236)
* [45]
  “PyPSA-Eur: A Sector-Coupled Open Optimisation Model of the European Energy System — PyPSA-Eur”
  URL: <https://pypsa-eur.readthedocs.io/en/latest/>
* [46]
  Tom Brown et al.
  “PyPSA-Eur: An open sector-coupled optimisation model of the European energy system” original-date: 2017-10-11T23:54:41Z, 2025
  URL: <https://github.com/PyPSA/pypsa-eur>
* [47]
  Fabian Neumann, Elisabeth Zeyen, Marta Victoria and Tom Brown
  “The Potential Role of a Hydrogen Network in Europe” arXiv:2207.05816 [physics]
  In *Joule* 7.8, 2023, pp. 1793–1817
  DOI: [10.1016/j.joule.2023.06.016](https://dx.doi.org/10.1016/j.joule.2023.06.016)
* [48]
  Fabian Neumann, Johannes Hampp and Tom Brown
  “Energy Imports and Infrastructure in a Carbon-Neutral European Energy System” arXiv:2404.03927 [physics]
  arXiv, 2024
  DOI: [10.48550/arXiv.2404.03927](https://dx.doi.org/10.48550/arXiv.2404.03927)
* [49]
  Hans Hersbach et al.
  “The ERA5 global reanalysis” \_eprint: https://rmets.onlinelibrary.wiley.com/doi/pdf/10.1002/qj.3803
  In *Quarterly Journal of the Royal Meteorological Society* 146.730, 2020, pp. 1999–2049
  DOI: [10.1002/qj.3803](https://dx.doi.org/10.1002/qj.3803)
* [50]
  Enrico G.. Antonini et al.
  “Weather- and climate-driven power supply and demand time series for European countries”
  Zenodo, 2024
  URL: <https://zenodo.org/records/13938926>
* [51]
  Adam Pluta et al.
  “SciGRID\_gas – Data Model of the European Gas Transport Network” arXiv:2201.08827 [physics]
  arXiv, 2022
  DOI: [10.48550/arXiv.2201.08827](https://dx.doi.org/10.48550/arXiv.2201.08827)
* [52]
  “OpenStreetMap”
  In *OpenStreetMap*
  URL: <https://www.openstreetmap.org/>
* [53]
  “Renewable hydrogen in the EU: 98% of projects remain unimplemented - Strategic Energy Europe” Section: Europe, 2025
  URL: <https://strategicenergy.eu/renewable-hydrogen-eu/>
* [54]
  La Redazione
  “EU hydrogen targets: why 2030 goals may not be achievable”
  In *Rinnovabili*, 2025
  URL: <https://www.rinnovabili.net/policy-and-affairs/environmental-policies/eu-hydrogen-targets-why-2030-goals-may-not-be-achievable/>
* [55]
   lisazeyen et al.
  “PyPSA/technology-data: v0.11.0”
  Zenodo, 2025
  DOI: [10.5281/ZENODO.3994163](https://dx.doi.org/10.5281/ZENODO.3994163)
* [56]
  “Joint Research Centre Data Catalogue - ENSPRESO - an open data, EU-28 wide, transparent a… - European Commission”
  URL: <https://data.jrc.ec.europa.eu/collection/id-00138>
* [57]
  “Industrial Carbon Management - European Commission”
  URL: <https://climate.ec.europa.eu/eu-action/industrial-carbon-management_en>
* [58]
  “Recommendations for the EU Industrial Carbon Management Strategy”
  In *Clean Air Task Force*
  URL: <https://www.catf.us/resource/recommendations-eu-industrial-carbon-management-strategy/>
* [59]
  “Fit for 55”, 2023
  URL: <https://www.consilium.europa.eu/en/policies/green-deal/fit-for-55-the-eu-plan-for-a-green-transition/>
* [60]
  “Scientific advice for the determination of an EU-wide 2040 climate target and a greenhouse gas budget for 2030–2050”, 2023
  URL: <https://climate-advisory-board.europa.eu/reports-and-publications/scientific-advice-for-the-determination-of-an-eu-wide-2040>
* [61]
  “European Steel in Figures 2024”
  URL: <https://www.eurofer.eu/publications/brochures-booklets-and-factsheets/european-steel-in-figures-2024>
* [62]
  “Thefutureof”
  URL: <https://commission.europa.eu/document/download/97e481fd-2dc3-412d-be4c-f152a8232961_en?filename=The%20future%20of%20European%20competitiveness%20_%20A%20competitiveness%20strategy%20for%20Europe.pdf>
* [63]
  “Competitiveness compass - European Commission”
  URL: <https://commission.europa.eu/topics/eu-competitiveness/competitiveness-compass_en>
* [64]
  “EU Commission unveils 2024 state aid scoreboard – Regfollower”
  URL: <https://regfollower.com/eu-commission-unveils-2024-state-aid-scoreboard/>
* [65]
  “REPowerEU”, 2022
  URL: <https://commission.europa.eu/strategy-and-policy/priorities-2019-2024/european-green-deal/repowereu-affordable-secure-and-sustainable-energy-europe_en>
* [66]
  “Carbon Border Adjustment Mechanism - European Commission”
  URL: <https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism_en>
* [67]
  “World Steel”
  In *worldsteel.org*
  URL: <https://worldsteel.org/>
* [68]
  “Cembureau”
  URL: <https://cembureau.eu/>
* [69]
  “[ds-056121] Total production”
  URL: <https://ec.europa.eu/eurostat/databrowser/view/ds-056121/legacyMultiFreq/table?lang=en&category=prom>
* [70]
  “Plastics – the fast Facts 2023 • Plastics Europe”
  In *Plastics Europe*
  URL: <https://plasticseurope.org/knowledge-hub/plastics-the-fast-facts-2023/>
* [71]
  “Reconciling the European Union’s clean industrialisation goals with those of the Global South”
  In *Bruegel — The Brussels-based economic think tank*, 2025
  URL: <https://www.bruegel.org/policy-brief/reconciling-european-unions-clean-industrialisation-goals-those-global-south>
* [72]
  Changlong Wang et al.
  “Green steel: Synergies between the Australian iron ore industry and the production of green hydrogen”
  In *International Journal of Hydrogen Energy* 48.83, 2023, pp. 32277–32293
  DOI: [10.1016/j.ijhydene.2023.05.041](https://dx.doi.org/10.1016/j.ijhydene.2023.05.041)
* [73]
  “Europe HRC steel-to-raw materials spread rises on steel prices”
  In *S&P Global Commodity Insights*, 2021
  URL: <https://www.spglobal.com/commodity-insights/en/news-research/latest-news/metals/030121-europe-hrc-steel-to-raw-materials-spread-rises-on-steel-prices>
* [74]
  “Cement costs and energy economics? - Thunder Said Energy”
  URL: <https://thundersaidenergy.com/downloads/cement-costs-and-energy-economics/>
* [75]
  “Ammonia Prices, News, Monitor, Market Analysis & Demand”
  URL: <https://www.chemanalyst.com/Pricing-data/ammonia-37>
* [76]
  Felix Schorn et al.
  “Methanol as a renewable energy carrier: An assessment of production and transportation costs for selected global locations”
  In *Advances in Applied Energy* 3, 2021, pp. 100050
  DOI: [10.1016/j.adapen.2021.100050](https://dx.doi.org/10.1016/j.adapen.2021.100050)
* [77]
  “Simplified levelised cost of petrochemicals for selected feedstocks and regions, 2017 – Charts – Data & Statistics”
  In *IEA*
  URL: <https://www.iea.org/data-and-statistics/charts/simplified-levelised-cost-of-petrochemicals-for-selected-feedstocks-and-regions-2017>
* [78]
  “Energy subsidies report shows progress in 2023 - European Commission”
  URL: <https://energy.ec.europa.eu/news/energy-subsidies-report-shows-progress-2023-2025-01-29_en>
* [79]
  “Commission introduces surveillance of imports and exports of metal scrap - European Commission”
  URL: <https://taxation-customs.ec.europa.eu/news/commission-introduces-surveillance-imports-and-exports-metal-scrap-2025-07-23_en>
* [80]
  Marcus Otti and Sebastian Zwickl-Bernhard
  “Net-zero emissions in the energy-intensive industrial sector by 2040: Insights from a country with ambitious national renewable policies”
  In *Energy Strategy Reviews* 60, 2025, pp. 101748
  DOI: [10.1016/j.esr.2025.101748](https://dx.doi.org/10.1016/j.esr.2025.101748)
* [81]
  GMK Center
  “The global scrap market showed overwhelming stability in July”, 2025-07
  URL: <https://gmk.center/en/posts/the-global-scrap-market-showed-overwhelming-stability-in-july/>
* [82]
   ta-team
  “Scrap Steel Explainer : A guide on scrap steel types, their limitations, and related market dynamics”
  In *Transition Asia*, 2023
  URL: <https://transitionasia.org/scrap-steel-explainer/>
* [83]
  Michaja Pehl, Felix Schreyer and Gunnar Luderer
  “Modelling long-term industry energy demand and CO2{}\_{\textrm{2}} emissions in the system context using REMIND (version 3.1.0)” Publisher: Copernicus GmbH
  In *Geoscientific Model Development* 17.5, 2024, pp. 2015–2038
  DOI: [10.5194/gmd-17-2015-2024](https://dx.doi.org/10.5194/gmd-17-2015-2024)
* [84]
  Steve Pye et al.
  “Regional uptake of direct reduction iron production using hydrogen under climate policy”
  In *Energy and Climate Change* 3, 2022, pp. 100087
  DOI: [10.1016/j.egycc.2022.100087](https://dx.doi.org/10.1016/j.egycc.2022.100087)
* [85]
  Takuma Watari and Benjamin McLellan
  “Global demand for green hydrogen-based steel: Insights from 28 scenarios”
  In *International Journal of Hydrogen Energy* 79, 2024, pp. 630–635
  DOI: [10.1016/j.ijhydene.2024.06.423](https://dx.doi.org/10.1016/j.ijhydene.2024.06.423)
* [86]
   Joint Research Centre (European Commission) and Julian Somers
  “Technologies to decarbonise the EU steel industry”
  Publications Office of the European Union, 2022
  URL: <https://data.europa.eu/doi/10.2760/069150>
* [87]
  Lorenzo Rinaldi, Debora Ghezzi, Emanuela Colombo and Matteo Vincenzo Rocco
  “Assessing environmental and market implications of steel decarbonisation strategies: a hybrid input-output model for the European union” Publisher: IOP Publishing
  In *Environmental Research Letters* 19.7, 2024, pp. 074059
  DOI: [10.1088/1748-9326/ad5bf1](https://dx.doi.org/10.1088/1748-9326/ad5bf1)
* [88]
  Annika Boldrini, Derck Koolen, Wina Crijns-Graus and Machteld Broek
  “The impact of decarbonising the iron and steel industry on European power and hydrogen systems”
  In *Applied Energy* 361, 2024, pp. 122902
  DOI: [10.1016/j.apenergy.2024.122902](https://dx.doi.org/10.1016/j.apenergy.2024.122902)
* [89]
  “The Global Cement Challenge”, 2024
  URL: <https://rhg.com/research/the-global-cement-challenge/>
* [90]
  “Key Facts & Figures”
  URL: <https://cembureau.eu/about-our-industry/key-facts-figures/>
* [91]
  Mónica Antunes et al.
  “Alternative Clinker Technologies for Reducing Carbon Emissions in Cement Industry: A Critical Review”
  In *Materials* 15.1, 2021, pp. 209
  DOI: [10.3390/ma15010209](https://dx.doi.org/10.3390/ma15010209)
* [92]
  Aamar Danish, M Usama Salim and Talha Ahmed
  “Trends and developments in green cement “A sustainable approach””, 1990
* [93]
  Sebastian Quevedo Parra and Matteo C. Romano
  “Decarbonization of cement production by electrification”
  In *Journal of Cleaner Production* 425, 2023, pp. 138913
  DOI: [10.1016/j.jclepro.2023.138913](https://dx.doi.org/10.1016/j.jclepro.2023.138913)
* [94]
  Arpan D. Patel, Zoé O.. Schyns, Thomas W. Franklin and Michael P. Shaver
  “Defining quality by quantifying degradation in the mechanical recycling of polyethylene” Publisher: Nature Publishing Group
  In *Nature Communications* 15.1, 2024, pp. 8733
  DOI: [10.1038/s41467-024-52856-8](https://dx.doi.org/10.1038/s41467-024-52856-8)
* [95]
  Plastics Europe
  “The Circular Economy for Plastics: A European Analysis”
  URL: <https://plasticseurope.org/wp-content/uploads/2024/03/CEreport_executivesummary_2024.pdf>
* [96]
  “Global Steel Plant Tracker”
  In *Global Energy Monitor*, 2023
  URL: <https://globalenergymonitor.org/projects/global-steel-plant-tracker/>
* [97]
  “GeoAsset Databases - UK Centre for Greening Finance and Investment (CGFI)”
  URL: <https://www.cgfi.ac.uk/spatial-finance-initiative/geoasset-project/geoasset-databases/>
* [98]
  “mpp-steel-model/mppsteel/data/import\_data/CAPEX OPEX Per Technology.xlsx at 9eca52db92bd2d9715f30e98ccaaf36677fdb516 · missionpossiblepartnership/mpp-steel-model”
  In *GitHub*
  URL: <https://github.com/missionpossiblepartnership/mpp-steel-model/blob/9eca52db92bd2d9715f30e98ccaaf36677fdb516/mppsteel/data/import_data/CAPEX%20OPEX%20Per%20Technology.xlsx>
* [99]
  Yannik Graupner, Christian Weckenborg and Thomas S. Spengler
  “Low-carbon primary steelmaking using direct reduction and electric arc furnaces: Prospective environmental impact assessment”
  In *Procedia CIRP* 116, 30th CIRP Life Cycle Engineering Conference, 2023, pp. 696–701
  DOI: [10.1016/j.procir.2023.02.117](https://dx.doi.org/10.1016/j.procir.2023.02.117)
* [100]
  Xiaoteng Ma, Wei Shao and Zheng Cui
  “Energy and thermodynamic analysis of a typical cement production system based on experimental and simulated investigations”
  In *Case Studies in Thermal Engineering* 38, 2022, pp. 102357
  DOI: [10.1016/j.csite.2022.102357](https://dx.doi.org/10.1016/j.csite.2022.102357)
* [101]
  M. Millinger et al.
  “Are biofuel mandates cost-effective? - An analysis of transport fuels and biomass usage to achieve emissions targets in the European energy system”
  In *Applied Energy* 326, 2022, pp. 120016
  DOI: [10.1016/j.apenergy.2022.120016](https://dx.doi.org/10.1016/j.apenergy.2022.120016)
* [102]
  M. Millinger, J. Ponitka, O. Arendt and D. Thrän
  “Competitiveness of advanced and conventional biofuels: Results from least-cost modelling of biofuel competition in Germany”
  In *Energy Policy* 107, 2017, pp. 394–402
  DOI: [10.1016/j.enpol.2017.05.013](https://dx.doi.org/10.1016/j.enpol.2017.05.013)
* [103]
  “The future cost of electricity-based synthetic fuels”
  URL: <https://www.agora-energiewende.org/publications/the-future-cost-of-electricity-based-synthetic-fuels-2>
* [104]
  “The global scrap market showed overwhelming stability in July”
  In *GMK*
  URL: <https://gmk.center/en/posts/the-global-scrap-market-showed-overwhelming-stability-in-july/>
* [105]
  Peter Collins
  “Hydrogen Europe”
  In *Hydrogen Europe*, 2024
  URL: <https://hydrogeneurope.eu/hydrogen-is-key-building-block-2040-targets/>