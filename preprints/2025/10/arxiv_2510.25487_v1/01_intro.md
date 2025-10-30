---
authors:
- Jacopo Timini
doc_id: arxiv:2510.25487v1
family_id: arxiv:2510.25487
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'The Latin Monetary Union and Trade: A Closer Look11footnote 1I am deeply grateful
  to Christopher M. Meissner for sharing his database on monetary standards. I thank
  Teodoro D’Agostino for excellent research assistance in coding RICardo bilateral
  trade flows to standardized ISO codes. I also thank Rodolfo G. Campos, and Marc
  Badia-Miró for helpful comments and suggestions The views expressed in this paper
  are those of the authors and do therefore not necessarily reflect those of the Banco
  de España or the Eurosystem.'
url_abs: http://arxiv.org/abs/2510.25487v1
url_html: https://arxiv.org/html/2510.25487v1
venue: arXiv q-fin
version: 1
year: 2025
---


Jacopo Timini

(October 29, 2025)

###### Abstract

This paper reexamines the effects of the Latin Monetary Union (LMU) —a 19th century agreement among several European countries to standardize their currencies through a bimetallic system based on fixed gold and silver content–—on trade. Unlike previous studies, this paper adopts the latest advances in gravity modeling and a more rigorous approach to defining the control group by accounting for the diversity of currency regimes during the early years of the LMU. My findings suggest that the LMU had a positive effect on trade between its members until the early 1870s, when bimetallism was still considered a viable monetary system. These effects then faded, converging to zero. Results are robust to the inclusion of additional potential confounders, the use of various samples spanning different countries and trade data sources, and alternative methodological choices.

Keywords: Currency unions, Latin Monetary Union, international trade, gravity model.

JEL codes: F13, F14, F33, N73

## 1 Introduction

Do currency unions boost trade between their members? This question has driven hundreds of papers and generated more than 3000 estimates of the Euro’s effect on trade alone (Polák, [2019](https://arxiv.org/html/2510.25487v1#bib.bib48)). While most studies focus on the post-World War II period, a growing body of research has turned to earlier monetary arrangements. In this context, the present paper reexamines the Latin Monetary Union (LMU)—a 19th century agreement among several European countries to standardize their currencies through a bimetallic system based on fixed gold and silver content—–and its effects on trade, by incorporating the latest advances in gravity modeling and explicitly accounting for the diverse landscape of European currency regimes during the early years of the LMU.

Despite economic theory and historical accounts providing many reasons why the LMU should have facilitated trade between its members, at least during its early years, the results of previous scholarly efforts have been elusive at best.
The key theoretical benefit of a currency union by adopting a common currency, countries remove the need for currency conversion, which reduces transaction costs and uncertainty in cross-border pricing (Micco et al., [2003](https://arxiv.org/html/2510.25487v1#bib.bib43)). Although the LMU did not have a common currency, it allowed coins issued by one member state to circulate freely and be accepted at face value in others by aligning the weight, fineness, and denomination of gold and silver coins.

The value added by the LMU laid in its ability to restore order to the bimetallic systems of its member states and to institutionalize such monetary framework, thereby helping to stabilize expectations regarding the maintenance of coinage standards. These standards had been repeatedly disrupted by fluctuations in the relative prices of gold and silver around the mid-19th century, which had triggered recurrent unilateral—–and thus uncoordinated—–adjustments to national monetary systems (Einaudi, [2000](https://arxiv.org/html/2510.25487v1#bib.bib19)). However, around the mid-1870s, the credibility of bimetallism collapsed (Flandreau and Oosterlinck, [2012](https://arxiv.org/html/2510.25487v1#bib.bib26); Meissner, [2015](https://arxiv.org/html/2510.25487v1#bib.bib41)), marked by a steep drop in silver’s value. This undermined the very basis of the LMU: the fixed gold-to-silver ratio became untenable, forcing members to limit and later suspend free silver coinage (1873-1874). As investors were quickly pricing in the world predominance of the gold standard, the LMU eventually kept trying to adapt to a changing world. However, later reforms only further signaled its emerging weaknesses. Although the LMU officially ended in 1927, the Union had become dysfunctional much earlier (Gillard, [2017](https://arxiv.org/html/2510.25487v1#bib.bib29)).

Previous studies suggest that the LMU’s effects on trade were either negligible or, at best, modest (Flandreau, [2000](https://arxiv.org/html/2510.25487v1#bib.bib25); Timini, [2018](https://arxiv.org/html/2510.25487v1#bib.bib50)), a finding that contrasts sharply with the consistently positive trade effects attributed to other pre-WWI fixed exchange-rate regimes, such as the gold standard (López-Córdova and Meissner, [2003](https://arxiv.org/html/2510.25487v1#bib.bib37); Estevadeordal et al., [2003](https://arxiv.org/html/2510.25487v1#bib.bib21); Mitchener et al., [2010](https://arxiv.org/html/2510.25487v1#bib.bib44); Badia-Miró et al., [2025](https://arxiv.org/html/2510.25487v1#bib.bib4)). Studies on the gold standard have adopted theory-consistent specifications of gravity models, incorporating the latest advances in the literature, and have adopted a more rigorous approach in defining the control group by accounting for other existing currency regimes. This consideration, however, is especially important during the early years of the LMU, when silver, bimetallic, and gold standards coexisted.222From the mid-1870s onward, alternative regimes became secondary, and most countries were either on gold or on paper. Therefore the control group for gold standard estimates, whose sample usually start around 1870, is not sensible to the inclusion of other currency standards as controls, as shown in Badia-Miró et al. ([2025](https://arxiv.org/html/2510.25487v1#bib.bib4)).

In this paper, I reassess the trade effects of the LMU using the latest advances in gravity models and a more precise definition of the control group that reflects the diversity of currency regimes in its early years.
My findings suggest that the LMU increased trade between its members by approximately 30%, in its early years (1865-1873), coinciding with the period when bimetallism was still considered a viable monetary system. These effects then started fading, rapidly converging to zero by the end of the 1870s.
Results are robust across a range of specifications, including the inclusion of additional potential confounders, the use of various samples spanning different countries and trade data sources, and alternative methodological choices.

## 2 Historical context

The LMU was established in 1865 by France, Belgium, Italy, and Switzerland, later joined by Greece in 1868. These countries agreed upon a ‘‘monetary convention’’ aimed at harmonizing their monetary legislation, thereby remedying the ‘‘inconveniences’’ caused by differing coinage systems in cross-border transactions, as stated in the convention itself.

Indeed, in the mid-19th century, fluctuations in the relative prices of gold and silver prompted repeated and uncoordinated adjustments to national monetary systems. These changes undermined previous efforts to harmonize currencies across Europe, and sparked doubts on the duration of coinage standards. The value added by the LMU laid in its capacity to restore order to these bimetallic systems by institutionalizing a shared monetary framework. In other words, the LMU provided a stronger guarantee that member countries would not unilaterally debase its coinage or alter its standards, which had been a persistent concern in earlier years. Through this structure, the LMU may have helped to stabilize expectations regarding its members’ maintenance of coinage standards and reduced the frequency of disruptive national interventions (Einaudi, [2000](https://arxiv.org/html/2510.25487v1#bib.bib19)).

More precisely, the LMU required that gold and silver coins should be minted according to uniform standards of weight, fineness, and denomination. The convention defined one monetary unit as either 4.5 grams of fine silver or 0.29 grams of fine gold, reflecting a fixed gold-to-silver ratio of 15.5:1. This arrangement harmonized the coinage systems of member states: gold coins and the highest silver denomination—–the 5-franc piece—–were minted with 90% fineness, while smaller silver denominations were struck at 83.5%.333The reduced silver content in smaller denominations was a deliberate policy to discourage arbitrage and the melting of coins for bullion, a common issue in bimetallic systems.
All member states committed to adhering strictly to these standards in their coin production. In practice, this meant that the French franc, Belgian franc, Italian lira, and Swiss franc were equivalent in value and metal content, making them interchangeable.444While it standardized the weight, fineness, and denomination of gold and silver coins of its member states—allowing them to circulate freely at face value—it did not establish a central monetary authority or a unified monetary policy. Each member retained sovereignty over its own minting and fiscal decisions, which meant that monetary coordination was limited to coin specifications rather than broader economic governance. Therefore, despite its name, it was a coinage union rather than a full monetary union (Einaudi, [2001](https://arxiv.org/html/2510.25487v1#bib.bib20))

Any LMU member’s coins circulated freely in all other LMU countries, with public offices, banks and individuals potentially accepting coins from other LMU members at face value.
A French merchant, for instance, could accept payment in Italian lire, Belgian or Swiss francs with more confidence that those coins would hold the same value as domestic French francs and could be exchanged back home.

This ‘‘interoperability’’ was backed by each government’s commitment to honor the others’ money. Public offices (such as national treasuries and mints) were obliged to accept gold coins and large silver 5-franc pieces from any member country without discrimination, just as they would accept their own coinage.555Smaller denomination silver coins, which were essentially token coinage, were subject to some limits in cross-border circulation to prevent overflow of small change: foreign subsidiary coins had to be accepted by government treasuries only up to a fixed amount (often 100 francs in total per payment). Beyond that threshold, a treasury could refuse excess foreign small coins, encouraging their repatriation.
Central banks—or other issuing institutions—in member countries, such as the Banque de France, also played an important role, by absorbing inflows of coins while maintaining convertibility and managing specie (gold and silver) reserves.
In this way, the LMU architecture was designed to reduce transaction costs among its members, which is, in principle, expected to have a positive impact on trade.666Currency unions are generally expected to influence member economies through two main channels. The first is the trade channel, which operates via reduced transaction costs, exchange rate stability, and increased price transparency—–factors that typically promote greater cross-border trade. The second is the financial channel, which involves deeper financial integration, improved capital mobility, and potentially lower risk premiums due to shared monetary frameworks. This paper focuses exclusively on the trade channel. Bordo and Rockoff ([1996](https://arxiv.org/html/2510.25487v1#bib.bib11)) and Bae and Bailey ([2011](https://arxiv.org/html/2510.25487v1#bib.bib5)) analyze the financial channel for the gold standard and the LMU respectively.

The arrangement worked relatively smoothly in the early years. However, LMU’s stability depended on each member upholding the agreed standards and on the external economic conditions. In particular, one key issue was bimetallism itself. Indeed, during the early 1870s, the silver’s market price fell relative to gold.777Fendel and Maurer ([2015](https://arxiv.org/html/2510.25487v1#bib.bib23)) list many reasons why silver depreciated with respect to gold, including an increase in silver supply, coming both from production and the move away from silver of some major countries (e.g. Germany), and changing preferences in the use of different monetary standards. They also provide an in-depth description of the LMU institutional structure.
As the fixed legal ratio between gold and silver remain unchanged, this meant that the legal ratio diverged from the market ratio. As silver became overvalued in legal terms, individuals could profitably bring silver bullion to the mint, have it coined into legal tender, and then exchange those coins for gold at face value. This arbitrage opportunity favored the minting and circulation of silver coins while gold coins were hoarded, exported, or withdrawn from banks. The result was a growing dominance of silver in everyday transactions and a significant depletion of gold reserves.

It was these imbalances that first prompted France to suspend free silver coinage in late 1873, after which the other LMU countries followed suit in early 1874. This was achieved by introducing quotas on silver coinage, a move that has been described as the end of the credibility of bimetallism (Flandreau and Oosterlinck, [2012](https://arxiv.org/html/2510.25487v1#bib.bib26)). A few years later—in late 1876 in France, and in 1878 for all LMU countries—the minting of new silver coins was finally halted. The LMU however maintained the legal tender status of existing large silver coins already in circulation. This situation became known as "limping gold standard" (Bordo and Jonung, [2000](https://arxiv.org/html/2510.25487v1#bib.bib10); Fendel and Maurer, [2015](https://arxiv.org/html/2510.25487v1#bib.bib23)).
In such context, therefore these existing large silver coins became a liability, unequally distributed among LMU members, as France ‘‘held much more coin issued from the Mints of Belgium and Switzerland, and to some extent Italy, than was held by these Governments of the French coins’’ (New York Times, [1885](https://arxiv.org/html/2510.25487v1#bib.bib46), as cited in [Timini](https://arxiv.org/html/2510.25487v1#bib.bib50), [2018](https://arxiv.org/html/2510.25487v1#bib.bib50)).

To address this issue, LMU members agreed to amend the original convention by introducing a ‘‘liquidation clause’’: in the event of the dissolution of the LMU, each member state was obligated to repurchase its own large silver coins held by other members at face value. Willis ([1901](https://arxiv.org/html/2510.25487v1#bib.bib54)), one of the most famous LMU contemporary analyst suggested that ‘‘the ratification of the treaty of 1885 really meant the abrogation of the Latin Union’’.
Since 1885 onward, there has been broad consensus on the little relevance of the LMU, despite it being formally dissolved only in 1927.

## 3 Methodology and Data

### 3.1 Methodology

My analysis of the LMU effects on trade relies on gravity trade theory. As it is well-known (Head and Mayer, [2014](https://arxiv.org/html/2510.25487v1#bib.bib33); Yotov et al., [2016](https://arxiv.org/html/2510.25487v1#bib.bib56)), gravity theory predicts that trade flows between two countries depend on their economic size (relative to the world) and the existing trade costs between them, and with the rest of the world.
More formally, this can be written as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xi​j=Yi​EjY​(τi​jΩi​Πj)−θX\_{ij}=\frac{Y\_{i}E\_{j}}{Y}(\frac{\tau\_{ij}}{\Omega\_{i}\Pi\_{j}})^{-\theta} |  | (1) |

Xi​j≥0X\_{ij}\geq 0 denote international trade flows from country ii (the exporter) to country jj (the importer).888While ideally I would like to include both domestic and international trade data in my main specification, I have to face important data restrictions for at least one country (Switzerland), out of five LMU members: there is no sufficient data to compute domestic trade flows during the early years of the Union. Given the focus of the paper on the evolution through time of the LMU trade effects, and the few countries that composed the Union, this can introduce a bias. Therefore, I prefer to adopt a conservative approach and estimate my main specification with international trade only, while later checking the robustness of the results to the inclusion of domestic trade. When including domestic trade, the case i=ji=j denotes domestic trade flows and i≠ji\neq j denotes international trade flows. Moreover, in this case, the literature (Bergstrand et al., [2015](https://arxiv.org/html/2510.25487v1#bib.bib9)) suggests to include an additional term in Equation [5](https://arxiv.org/html/2510.25487v1#S3.E5 "In 3.1 Methodology ‣ 3 Methodology and Data ‣ The Latin Monetary Union and Trade: A Closer Look11footnote 1I am deeply grateful to Christopher M. Meissner for sharing his database on monetary standards. I thank Teodoro D’Agostino for excellent research assistance in coding RICardo bilateral trade flows to standardized ISO codes. I also thank Rodolfo G. Campos, and Marc Badia-Miró for helpful comments and suggestions The views expressed in this paper are those of the authors and do therefore not necessarily reflect those of the Banco de España or the Eurosystem.") such as ζt​bi​j\zeta\_{t}b\_{ij}, identifying the ease of trading internationally versus trading domestically over time. This is a standard approach for disentangling the effect of trade globalization from the effect of other trade policy or monetary standard variables.
The term Yi≡∑jXi​jY\_{i}\equiv\sum\_{j}X\_{ij} represents production in country ii, while Ej≡∑iXi​jE\_{j}\equiv\sum\_{i}X\_{ij} represents expenditure in country jj.

As demonstrated by Anderson and van Wincoop ([2003](https://arxiv.org/html/2510.25487v1#bib.bib3)), structural gravity models also satisfy two additional conditions:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ωi−θ=∑j(τi​jΠj)−θ​EjY\Omega\_{i}^{-\theta}=\sum\_{j}(\frac{\tau\_{ij}}{\Pi\_{j}})^{-\theta}\frac{E\_{j}}{Y} |  | (2) |

and

|  |  |  |  |
| --- | --- | --- | --- |
|  | Πj−θ=∑i(τi​jΩi)−θ​YiY\Pi\_{j}^{-\theta}=\sum\_{i}(\frac{\tau\_{ij}}{\Omega\_{i}})^{-\theta}\frac{Y\_{i}}{Y} |  | (3) |

The term Ωi\Omega\_{i} represents outward multilateral resistance and is specific to exporting country ii, capturing its access to potential export markets. Conversely, Πj\Pi\_{j} denotes inward multilateral resistance, reflecting the degree of competition that trade flows from any origin face in destination country jj. Higher values of either term are associated with lower bilateral trade flows, which is why they are referred to as ‘‘multilateral resistance terms’’. The remaining component, τi​j\tau\_{ij}, captures all pair-specific trade costs.

Exploiting the multiplicative structure of gravity models, and extending it to a panel setting with an additive error term, it is possible to reformulate Equation [7](https://arxiv.org/html/2510.25487v1#A2.E7 "In Appendix B Theoretical Appendix ‣ The Latin Monetary Union and Trade: A Closer Look11footnote 1I am deeply grateful to Christopher M. Meissner for sharing his database on monetary standards. I thank Teodoro D’Agostino for excellent research assistance in coding RICardo bilateral trade flows to standardized ISO codes. I also thank Rodolfo G. Campos, and Marc Badia-Miró for helpful comments and suggestions The views expressed in this paper are those of the authors and do therefore not necessarily reflect those of the Banco de España or the Eurosystem.") in a log-linearized form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xi​j​t=exp⁡(ln⁡Yi​t+ln⁡Ej​t−ln⁡Yt−θ​ln⁡τi​j​t+θ​ln⁡Ωi​t+θ​ln⁡Πj​t+εi​j​t).X\_{ijt}=\exp\left(\ln Y\_{it}+\ln E\_{jt}-\ln Y\_{t}-\theta\ln\tau\_{ijt}+\theta\ln\Omega\_{it}+\theta\ln\Pi\_{jt}+\varepsilon\_{ijt}\right). |  | (4) |

In Equation [4](https://arxiv.org/html/2510.25487v1#S3.E4 "In 3.1 Methodology ‣ 3 Methodology and Data ‣ The Latin Monetary Union and Trade: A Closer Look11footnote 1I am deeply grateful to Christopher M. Meissner for sharing his database on monetary standards. I thank Teodoro D’Agostino for excellent research assistance in coding RICardo bilateral trade flows to standardized ISO codes. I also thank Rodolfo G. Campos, and Marc Badia-Miró for helpful comments and suggestions The views expressed in this paper are those of the authors and do therefore not necessarily reflect those of the Banco de España or the Eurosystem."), ln⁡τi​j​t\ln\tau\_{ijt} is the only term that varies jointly by exporter and importer. All other terms depend solely on either the exporter or the importer. As a result, they can be collapsed into exporter-time and importer-time dummy variables, and absorbed in the estimation procedures by the corresponding fixed effects. These are the standard way of controlling for ‘‘multilateral trade resistances,’’ as defined by Anderson and van Wincoop ([2003](https://arxiv.org/html/2510.25487v1#bib.bib3)). They also absorb all variables that vary at the exporter-time and importer-time level, such as GDP, GDP per capita, a country openness to trade, etc.

As the true vector of trade costs is not available to researchers, in gravity models the term ln⁡τi​j​t\ln\tau\_{ijt} is specified using observable proxies. In this case, trade costs ln⁡τi​j​t\ln\tau\_{ijt} are defined as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | −θ​ln⁡τi​j​t=βL​M​U​L​M​Ui​j​t+βG​S​G​Si​j​t+γ′​O​t​h​e​r​M​Si​j​t+βT​A​T​Ai​j​t+ψi​j.-\theta\ln\tau\_{ijt}=\beta\_{LMU}{LMU}\_{ijt}+\beta\_{GS}{GS}\_{ijt}+\gamma^{\prime}{OtherMS}\_{ijt}+\beta\_{TA}{TA}\_{ijt}+\psi\_{ij}. |  | (5) |

The term L​M​Ui​j​t{LMU}\_{ijt} is my main (dummy) variable of interest, and identifies country-pairs pertaining to the LMU at time t. In a similar fashion, the term G​Si​j​t{GS}\_{ijt} controls for pairs where countries are both on gold standard. The vector of controls O​t​h​e​r​M​Si​j​t{OtherMS}\_{ijt} identifies country pairs sharing the same monetary standard (other than gold or the LMU). Inspired by López-Córdova and Meissner ([2003](https://arxiv.org/html/2510.25487v1#bib.bib37)); Mitchener et al. ([2010](https://arxiv.org/html/2510.25487v1#bib.bib44)); Badia-Miró et al. ([2025](https://arxiv.org/html/2510.25487v1#bib.bib4)), this corresponds to a set of dummy variables which are equal to one if both countries are on silver, on a bimetallic standard other than the LMU, or on paper. The term T​Ai​j​t{TA}\_{ijt} is a dummy variable that identifies trade agreements. As recently demonstrated by Timini ([2023](https://arxiv.org/html/2510.25487v1#bib.bib51)), trade agreements played a significant role in shaping trade during the 1860s and 1870s. It is therefore important to consider them as a potential confounding factor. The term ψi​j\psi\_{ij} corresponds to directional country pair fixed effects, and mirrors the Baier and Bergstrand ([2007](https://arxiv.org/html/2510.25487v1#bib.bib6)) approach to control for endogeneity in gravity models. In this case, these fixed also absorb time invariant bilateral trade costs.

In this first approximation, I will identify the L​M​Ui​j​t{LMU}\_{ijt} effects in different periods, identified using the historical narrative detailed in the "Historical context" section, and following Timini ([2018](https://arxiv.org/html/2510.25487v1#bib.bib50)), by adapting the sample length. I will therefore exploit three different samples, ending at 1873, 1885, and 1913 respectively.

Despite being grounded on the historical narrative, in fact, the exact dates of these cuts is somewhat exogenously imposed by the researcher. Therefore, this can let the reader with doubts on whether the LMU trade effects really change around those years. To further address this issue, I will allow the coefficient of the LMU variable to vary over time in another specification. Furthermore, such specification will also serve to verify whether there are identifiable pre-trends on trade between LMU members, by backtracking the LMU variable to t-3. The time span is mostly dictated by the limited pre-LMU window available in the dataset, that constrains further backward extension. Given the short time period, pre-trends resulting from this exercise may also capture some anticipatory behavior, as negotiations and signatures usually precede the entry into force of an agreement.999The gravity literature is not unanimous on the number of years that should be checked before a trade agreement or a currency union enters into force, but it suggests that often some effects can be detected before formal implementation due to anticipation, rather than endogeneity. Recent contributions by Egger et al. ([2022](https://arxiv.org/html/2510.25487v1#bib.bib17)) and Nagengast and Yotov ([2025](https://arxiv.org/html/2510.25487v1#bib.bib45)) support this view, suggesting that the effects of trade agreements may begin up to three years prior to their official entry into force.

Given sample length, reference years are, in this case, 1860 and 1861. Given the focus on a single currency union, the LMU, this is similar to running an event study that spans from t-3 to t+48.
In this sense, this corresponds to specify the vector of trade costs in the following form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | −θ​ln⁡τi​j​t=∑t=18621913βt​L​M​Ui​j​t⋅𝕀{t=T}+βG​S​G​Si​j​t+γ′​O​t​h​e​r​M​Si​j​t+βT​A​T​Ai​j​t+ψi​j.-\theta\ln\tau\_{ijt}=\sum\_{t=1862}^{1913}\beta\_{t}{LMU}\_{ijt}\cdot\mathbb{I}\_{\{t=T\}}+\beta\_{GS}{GS}\_{ijt}+\gamma^{\prime}{OtherMS}\_{ijt}+\beta\_{TA}{TA}\_{ijt}+\psi\_{ij}. |  | (6) |

where ⋅𝕀{cond}\cdot\mathbb{I}\_{\{\textit{cond}\}} denotes an indicator function that takes the value one if the condition cond is satisfied and zero otherwise.
In this case, the LMU variable starts three years earlier for each member, so to be able to identify the effects during the 1862-1864 period.

All estimations are performed following standard practice: I use Poisson pseudo maximum likelihood (PPML), as originally proposed by Santos Silva and Tenreyro ([2006](https://arxiv.org/html/2510.25487v1#bib.bib49)). This method provides consistent parameter estimates and trade cost elasticities in the presence of zero trade flows and heteroskedasticity. As is standard practice, I use nominal trade data, following the recommendation of Baldwin and Taglioni ([2007](https://arxiv.org/html/2510.25487v1#bib.bib8)), who argue that importer-year and exporter-year fixed effects adequately control for cross-country inflation differentials. Deflating the data using CPI would introduce unnecessary noise—an issue likely to be even more pronounced when working with 19th-century trade records denominated in pounds, which would require applying the (reconstructed) Great Britain CPI deflator.

### 3.2 Data

In my main specification, I use data on gross international trade flows from version 4 of the TRADHIST database by Foquin and Hugot ([2016](https://arxiv.org/html/2510.25487v1#bib.bib27)). In some robustness checks, I also use the well-known historical trade database, RICardo (Dedinger and Girard, [2017](https://arxiv.org/html/2510.25487v1#bib.bib15)), to verify the robustness of the results. TRADHIST database compiles historical bilateral trade flows of goods taken from various sources, including both primary sources and other trade databases, such as RICardo itself. Trade flows are nominal and are expressed in British pound sterling.101010TRADHIST also allows researchers to compute domestic trade flows directly. Although domestic trade flows are not readily available from historical statistics, they can be constructed using TRADHIST as the difference between nominal Gross Domestic Product (GDP) and nominal total exports. Ideally, I would rely on gross total output statistics. However, these data do not exist for a large enough number of countries and years during our period of analysis. Therefore, GDP-based calculations are the best possible viable alternative. Importantly, a recent study by Campos et al. ([2021](https://arxiv.org/html/2510.25487v1#bib.bib14)) shows that in well specified gravity models, exporter-time, importer-time, and pair fixed effects make the discrepancy between GDP (a measure of value added) and output (a gross measure) relatively unimportant in estimating many bilateral trade costs proxies, such as trade agreements or currency unions.

I follow the literature and identify gold standard membership using Officer ([2020](https://arxiv.org/html/2510.25487v1#bib.bib47)). Silver, bimetallic, and paper pairs (other than LMU countries) are identified using information on country currency standards contained in Meissner ([2024](https://arxiv.org/html/2510.25487v1#bib.bib42)) and Meissner ([2001](https://arxiv.org/html/2510.25487v1#bib.bib40)). As in Flandreau ([2000](https://arxiv.org/html/2510.25487v1#bib.bib25)) and Timini ([2018](https://arxiv.org/html/2510.25487v1#bib.bib50)), LMU member states include: Belgium, France, Switzerland, and Italy from 1865, with Greece joining in 1868.

The sample includes 37 countries and territories (see Table [A.1](https://arxiv.org/html/2510.25487v1#A1.T1 "Table A.1 ‣ Appendix A Summary statistics ‣ The Latin Monetary Union and Trade: A Closer Look11footnote 1I am deeply grateful to Christopher M. Meissner for sharing his database on monetary standards. I thank Teodoro D’Agostino for excellent research assistance in coding RICardo bilateral trade flows to standardized ISO codes. I also thank Rodolfo G. Campos, and Marc Badia-Miró for helpful comments and suggestions The views expressed in this paper are those of the authors and do therefore not necessarily reflect those of the Banco de España or the Eurosystem.") in the Appendix for more details), and covers the period from 1860 to 1913.

## 4 Results

### 4.1 Main results

Figure [1](https://arxiv.org/html/2510.25487v1#S4.F1 "Figure 1 ‣ 4.1 Main results ‣ 4 Results ‣ The Latin Monetary Union and Trade: A Closer Look11footnote 1I am deeply grateful to Christopher M. Meissner for sharing his database on monetary standards. I thank Teodoro D’Agostino for excellent research assistance in coding RICardo bilateral trade flows to standardized ISO codes. I also thank Rodolfo G. Campos, and Marc Badia-Miró for helpful comments and suggestions The views expressed in this paper are those of the authors and do therefore not necessarily reflect those of the Banco de España or the Eurosystem.") reports the effects of the LMU on trade, derived from the baseline estimation framework. Panel (a) reproduces the results already available in the literature (Flandreau, [2000](https://arxiv.org/html/2510.25487v1#bib.bib25); Timini, [2018](https://arxiv.org/html/2510.25487v1#bib.bib50)), for different samples, 1860-1873, 1860-1885, and 1860-1913. Compared to both country pairs that did not share a common monetary standard (other than gold) and those that shared a different one, such as countries using silver or a bimetallic standard (other than the LMU), the LMU has only a small and statistically insignificant effect on trade.

However, when these other standards are explicitly accounted for (see Panel (b)), therefore adopting a more rigorous approach to defining the control group and correcting for an omitted variable bias, estimates of the LMU effect change drastically. This is particularly relevant for the early years of the LMU (until 1873), a period where many different currency regimes coexisted. The estimates suggest that the LMU increased trade between its members by approximately 30% compared to country pairs that did not share a monetary standard. This control group is comparable to those employed in the majority of studies analyzing gold standard or 20thcentury currency unions. It allows a cleaner comparison of the LMU effect with respect to other country pairs that did not share the same monetary standard. These were indeed the country pairs exposed to those risks, such as exchange rate fluctuations, that the LMU was supposed to mitigate.

Figure [2](https://arxiv.org/html/2510.25487v1#S4.F2 "Figure 2 ‣ 4.1 Main results ‣ 4 Results ‣ The Latin Monetary Union and Trade: A Closer Look11footnote 1I am deeply grateful to Christopher M. Meissner for sharing his database on monetary standards. I thank Teodoro D’Agostino for excellent research assistance in coding RICardo bilateral trade flows to standardized ISO codes. I also thank Rodolfo G. Campos, and Marc Badia-Miró for helpful comments and suggestions The views expressed in this paper are those of the authors and do therefore not necessarily reflect those of the Banco de España or the Eurosystem.") shows the results of the estimation procedure using the trade costs specification reported in Equation [6](https://arxiv.org/html/2510.25487v1#S3.E6 "In 3.1 Methodology ‣ 3 Methodology and Data ‣ The Latin Monetary Union and Trade: A Closer Look11footnote 1I am deeply grateful to Christopher M. Meissner for sharing his database on monetary standards. I thank Teodoro D’Agostino for excellent research assistance in coding RICardo bilateral trade flows to standardized ISO codes. I also thank Rodolfo G. Campos, and Marc Badia-Miró for helpful comments and suggestions The views expressed in this paper are those of the authors and do therefore not necessarily reflect those of the Banco de España or the Eurosystem."). In this way, I go beyond the partition of periods ‘‘exogenously’’ imposed by the researcher, and I am able to portray the evolution of the LMU trade effect over time. There are at least four important points to note. First, between its creation in 1865 and the suspension of free silver coinage in late 1873 and early 1874, the LMU had positive and significant effects on trade among its members. Second, these effects started to fade at least from 1873 onward. This coincides with the point at which bimetallism stopped being considered a viable monetary system. By around 1878, the year in which the
minting of new silver coins was finally stopped throughout the LMU, they had approached zero.
Third, from a trade perspective, the LMU was already dead well before the time of the 1885 reform—what Willis ([1901](https://arxiv.org/html/2510.25487v1#bib.bib54)) suggested was the de facto ‘‘abrogation of the Latin Union’’.
Fourth, these findings also suggest that the specification implemented in the paper plausibly captures endogeneity well. The coefficients reported for 1862-1864 (three year window before the entry into force of the LMU) show a small and non statistically significant coefficient.111111Although the coefficient for 1864 is twice as large as those for 1862 and 1863, this pattern is common in studies of trade agreements and currency unions, where effects often precede formal implementation due to anticipatory behavior, as negotiations and signatures typically occur one to three years before entry into force. Recent contributions by Egger et al. ([2022](https://arxiv.org/html/2510.25487v1#bib.bib17)) and Nagengast and Yotov ([2025](https://arxiv.org/html/2510.25487v1#bib.bib45)) support this view, suggesting that the effects of trade agreements may begin up to three years prior to their official entry into force. While the limited pre-LMU window in the dataset constrains further backward extension—–at least without unbalancing the dataset as observations for key countries, including LMU members, such as Italy, do not exist before the 1860s–—the already small and non-statistically significant coefficients for 1862 and 1863 are reassuring.

![Refer to caption](x1.png)


(a) Without controlling for other monetary standards

  
![Refer to caption](x2.png)


(b) Controlling for other monetary standards



Figure 1: LMU trade effects with different control groups

Note: The figures show point estimates (blue dots) and 95% confidence intervals (grey lines). Standard errors are clustered by country pair. Estimations use data from the TRADHIST database. Both panels are based on regressions that specify the vector of trade costs based on Equation [5](https://arxiv.org/html/2510.25487v1#S3.E5 "In 3.1 Methodology ‣ 3 Methodology and Data ‣ The Latin Monetary Union and Trade: A Closer Look11footnote 1I am deeply grateful to Christopher M. Meissner for sharing his database on monetary standards. I thank Teodoro D’Agostino for excellent research assistance in coding RICardo bilateral trade flows to standardized ISO codes. I also thank Rodolfo G. Campos, and Marc Badia-Miró for helpful comments and suggestions The views expressed in this paper are those of the authors and do therefore not necessarily reflect those of the Banco de España or the Eurosystem."). The top panel (‘‘Without controlling for other monetary standards’’) shows results from estimations that excludes the term 𝛄′​𝐎​𝐭​𝐡​𝐞​𝐫​𝐌​𝐒i​j​t\bm{\gamma}^{\prime}\bm{OtherMS}\_{ijt}. The bottom panel (‘‘Controlling for other monetary standards’’) shows results from estimations that includes the term 𝛄′​𝐎​𝐭​𝐡​𝐞​𝐫​𝐌​𝐒i​j​t\bm{\gamma}^{\prime}\bm{OtherMS}\_{ijt}.



![Refer to caption](x3.png)

Figure 2: The Latin Monetary Union trade effects

Note: The figure shows the estimated coefficient of the LMU over time (β^t\hat{\beta}\_{t}) and 95% confidence intervals. The estimation uses the trade costs specification reported in Equation [6](https://arxiv.org/html/2510.25487v1#S3.E6 "In 3.1 Methodology ‣ 3 Methodology and Data ‣ The Latin Monetary Union and Trade: A Closer Look11footnote 1I am deeply grateful to Christopher M. Meissner for sharing his database on monetary standards. I thank Teodoro D’Agostino for excellent research assistance in coding RICardo bilateral trade flows to standardized ISO codes. I also thank Rodolfo G. Campos, and Marc Badia-Miró for helpful comments and suggestions The views expressed in this paper are those of the authors and do therefore not necessarily reflect those of the Banco de España or the Eurosystem."). Standard errors are clustered by directional country pairs.

This paper reinterprets and expands on the initial findings of Flandreau and Oosterlinck ([2012](https://arxiv.org/html/2510.25487v1#bib.bib26)) and Flandreau ([1996](https://arxiv.org/html/2510.25487v1#bib.bib24)). While they emphasize the impact of the suspension of free silver coinage in 1873-74 on the viability of bimetallism, this paper suggests that these events also had significant consequences for trade among LMU members. More broadly, these results fit well with the existing literature, suggesting two key findings. First, to ensure a correct estimation of the LMU effects on trade, it is crucial to have a rigorous identification of the control group. When adopting a strategy similar to the one used by the literature analyzing the gold standard and contemporary currency unions, I find that the LMU increased trade between its members in its early years. Secondly, these findings imply that the effects observed were not ‘‘special’’—–they were comparable to those observed under other monetary standards among the participating countries.

Finally, at first glance, these findings may seem at odds with the results presented in the working paper by Vicquéry ([2021](https://arxiv.org/html/2510.25487v1#bib.bib52)). However, the apparent discrepancy stems from a difference in scope, which limits the direct comparability of the two studies. Indeed, Vicquéry ([2021](https://arxiv.org/html/2510.25487v1#bib.bib52)) focuses exclusively on the effects of the LMU on trade between some Italian pre-unitary states and other LMU members before and after Italian unification, using a database that only captures maritime trade and ends in 1869, thereby limiting the analysis to four years after the creation of the LMU.

### 4.2 Robustness tests

Results are robust across a range of specifications, including the consideration of additional potential confounders, the use of alternative methodological choices, various samples spanning different countries, and trade data sources. Importantly, given that the study concerns a currency union designed to facilitate the unrestricted circulation of coins across national borders, I also explore here how the observed results are not driven by underlying specie flows.

More in detail, in the spirit of Gowa and Hicks ([2013](https://arxiv.org/html/2510.25487v1#bib.bib31)), Gowa and Hicks ([2017](https://arxiv.org/html/2510.25487v1#bib.bib32)), and Karlsson and Hedberg ([2021](https://arxiv.org/html/2510.25487v1#bib.bib36)), I additionally control for military alliances between two countries, and for whether two countries are at war with each other.121212More precisely, data on military alliances are based on Gibler ([2009](https://arxiv.org/html/2510.25487v1#bib.bib28)) and are codified as a dummy variable equal to one if two countries (the exporter and the importer) have a defense pact in force at time t, and zero otherwise. In the database, a defense pact is defined as “the highest level of military commitment, requiring alliance members to come to each other’s aid militarily if attacked by a third party”. Interstate dyadic war data are based on Maoz et al. ([2019](https://arxiv.org/html/2510.25487v1#bib.bib38)), and are codified as a dummy variable equal to one if two countries (the exporter and the importer) are at war with each other at time t, and zero otherwise.

I then experiment with different methodological choices, such as including both international and domestic trade in the left-hand side variable (Yotov, [2022](https://arxiv.org/html/2510.25487v1#bib.bib55)), consider the LMU as non-overlapping to the gold standard,131313This means that when the LMU dummy is equal to one, the gold standard variable is always set equal to zero. correcting for possible biases in the estimating procedure (Weidner and Zylkin, [2021](https://arxiv.org/html/2510.25487v1#bib.bib53)), and testing alternative clustering strategies as suggested by Egger and Tarlea ([2015](https://arxiv.org/html/2510.25487v1#bib.bib18)).

I also test whether the results are sensitive to the sample or trade data used. I therefore adapt the countries included in the sample according to the previous literature on trade during the first globalizaton (López-Córdova and Meissner, [2003](https://arxiv.org/html/2510.25487v1#bib.bib37); Timini, [2018](https://arxiv.org/html/2510.25487v1#bib.bib50), [2023](https://arxiv.org/html/2510.25487v1#bib.bib51)).141414Additionally, I also as test other restrictions e.g. focusing on European countries only, excluding Germany, European countries and the US only I then use RICardo (Dedinger and Girard, [2017](https://arxiv.org/html/2510.25487v1#bib.bib15)) as an alternative database for sourcing information on bilateral trade flows.151515As suggested by the literature on the first globalization, I use import-based trade data, as they tend to be more reliable—given the stronger incentives for a correct register of trade (customs collection purposes).

Figure [3](https://arxiv.org/html/2510.25487v1#S4.F3 "Figure 3 ‣ 4.2 Robustness tests ‣ 4 Results ‣ The Latin Monetary Union and Trade: A Closer Look11footnote 1I am deeply grateful to Christopher M. Meissner for sharing his database on monetary standards. I thank Teodoro D’Agostino for excellent research assistance in coding RICardo bilateral trade flows to standardized ISO codes. I also thank Rodolfo G. Campos, and Marc Badia-Miró for helpful comments and suggestions The views expressed in this paper are those of the authors and do therefore not necessarily reflect those of the Banco de España or the Eurosystem.") reports robustness test results for the sample 1865-1873. The estimated coefficient ranges from 0.21 to 0.41, indicating a trade increase of between +23% and +50% depending on the specification used.

Figure [4](https://arxiv.org/html/2510.25487v1#S4.F4 "Figure 4 ‣ 4.2 Robustness tests ‣ 4 Results ‣ The Latin Monetary Union and Trade: A Closer Look11footnote 1I am deeply grateful to Christopher M. Meissner for sharing his database on monetary standards. I thank Teodoro D’Agostino for excellent research assistance in coding RICardo bilateral trade flows to standardized ISO codes. I also thank Rodolfo G. Campos, and Marc Badia-Miró for helpful comments and suggestions The views expressed in this paper are those of the authors and do therefore not necessarily reflect those of the Banco de España or the Eurosystem.") reports robustness test results for regressions that allow the LMU coefficient to vary over time. The Figure displays the coefficients and confidence intervals from the main regressions, and then report coefficients from all robustness tests.161616In this case, the Weidner and Zylkin ([2021](https://arxiv.org/html/2510.25487v1#bib.bib53)) methodology is not implemented as it does not allow for multiple coefficients of interest in the same regression. Also, results from alternative clustering strategies (Egger and Tarlea, [2015](https://arxiv.org/html/2510.25487v1#bib.bib18)) are not reported as—obviously and by construction—coefficients are identical to the main specification, i.e. only standard errors change. Quite nicely, practically all coefficients from the robustness tests fall within the confidence intervals of the coefficient of the main regressions. One exception is the RICardo-based regression, where the distribution of coefficients over time is more noisy. However, point estimates tend to be larger (and not smaller), falling above the confidence intervals (for the coefficient estimated in the main regression) for the period 1865-1873. Therefore, one possible interpretation is that the estimates based on the main specification are a lower bound. However, it is also possible that this more noisy distribution and the larger coefficients are dictated by a lower number of pre-LMU observations.

Finally, while historical (as well as contemporary) trade statistics record commodity flows, these often include specie movements. Nevertheless, the interpretation of the role of specie flows remains underexplored. The ambiguity lies in whether specie was actively traded as a commodity or passively moved to settle imbalances in the current or capital accounts. While this distinction is hopefully of second order importance in most cases—especially when studying trade policy issues, or other forms of trade integration—it could be a more prominent issue for the study of the LMU, as it was explicitly designed to facilitate the unrestricted circulation of coins across national borders.

Ideally, to make sure that my main results are not driven by specie flows, I would like to have access to cross-country bilateral trade data for commodity trade only. This means having access to detailed bilateral trade statistics at the product level for many countries in the world, and being able to disentangle commodity trade from specie trade flows.171717Technically, as most historical trade databases have been compiled using SITC Rev. 2 classification, this implies to exclude items 96 and 97 at the SITC 2-digit level.
There are only a few countries for which such database is available, and, to the best of my knowledge, Italy is the only one for which such database is granted public access, covering the period 1862-1939.

Therefore, as a second-best strategy to support the statement that my main results are not driven by underlying specie flows, I use Italian product-level data (Federico et al., [2012](https://arxiv.org/html/2510.25487v1#bib.bib22)), and check that specie flows are not an important component of trade flows among LMU members for the period 1865-1873, i.e. when I find positive and significant results of the LMU on trade. Reassuringly, specie flows correspond to less than 0.8% of total bilateral trade flows between Italy and other LMU members.
This is further confirmed by a set of regressions explicitly identifying trade data that include specie flows.181818This consist in adding to my baseline specification, for the period 1865-1873, a dummy equal to one when trade data sources explicitly acknowledge the inclusion of species and bullions in trade data, on the basis of the information provided by Dedinger and Girard ([2017](https://arxiv.org/html/2510.25487v1#bib.bib15)) in the RICardo database. Given that the source is linked to the RICardo database, I run two different regressions where the trade flow variable is respectively based on the information contained in TRADHIST and RICardo. The estimated LMU coefficient corresponds to 0.255 and 0.279 respectively, and is always significant at the 5% level.

![Refer to caption](x4.png)

Figure 3: Robustness tests

Note: The figures show point estimates and 95% confidence intervals. Standard errors are clustered by country pair. Estimations use data from the TRADHIST database. The panel is based on regressions that specify the vector of trade costs based on Equation [5](https://arxiv.org/html/2510.25487v1#S3.E5 "In 3.1 Methodology ‣ 3 Methodology and Data ‣ The Latin Monetary Union and Trade: A Closer Look11footnote 1I am deeply grateful to Christopher M. Meissner for sharing his database on monetary standards. I thank Teodoro D’Agostino for excellent research assistance in coding RICardo bilateral trade flows to standardized ISO codes. I also thank Rodolfo G. Campos, and Marc Badia-Miró for helpful comments and suggestions The views expressed in this paper are those of the authors and do therefore not necessarily reflect those of the Banco de España or the Eurosystem."). See text for more details. Standard errors are clustered by directional country pairs.



![Refer to caption](x5.png)

Figure 4: Robustness tests (LMU effect over time)

Note: The figures show point estimates and 95% confidence intervals for the main specification. Standard errors are clustered by country pair. Light gray lines report coefficient estimates of the robustness tests described in the text, based on regressions that specify the vector of trade costs based on Equation [6](https://arxiv.org/html/2510.25487v1#S3.E6 "In 3.1 Methodology ‣ 3 Methodology and Data ‣ The Latin Monetary Union and Trade: A Closer Look11footnote 1I am deeply grateful to Christopher M. Meissner for sharing his database on monetary standards. I thank Teodoro D’Agostino for excellent research assistance in coding RICardo bilateral trade flows to standardized ISO codes. I also thank Rodolfo G. Campos, and Marc Badia-Miró for helpful comments and suggestions The views expressed in this paper are those of the authors and do therefore not necessarily reflect those of the Banco de España or the Eurosystem."). See text for more details. Standard errors are clustered by directional country pairs.

### 4.3 Extension: Core - Periphery (or the LMU’s heterogeneous trade effects)

Previous contributions analyzed the possible existence of heterogeneity in the LMU trade effects across its members using econometric methods. Timini ([2018](https://arxiv.org/html/2510.25487v1#bib.bib50)) focuses on differences in trade flows between France and other members, and those involving other members only. He does so by splitting the LMU dummy in two separate dummies. Vicquéry ([2021](https://arxiv.org/html/2510.25487v1#bib.bib52)), instead, looks separately at the bilateral flows between each LMU members and some Italian pre-unitary states.
The heterogeneous effects of different trade agreements or currency unions have been assessed in literature using gravity models also for the post-WWII period (Baier et al., [2019](https://arxiv.org/html/2510.25487v1#bib.bib7); Glick and Rose, [2016](https://arxiv.org/html/2510.25487v1#bib.bib30)), though authors often acknowledge the limitations of such extensions.191919If applying the econometric strategy suggested by Timini ([2018](https://arxiv.org/html/2510.25487v1#bib.bib50)) to my data, however, results are similar to those of Timini ([2018](https://arxiv.org/html/2510.25487v1#bib.bib50)) and available upon request.
As noted by Baier et al. ([2019](https://arxiv.org/html/2510.25487v1#bib.bib7)), such disaggregation can dilute the identification strategy and compromise the robustness of the estimates: the more granular the estimate obtained—i.e. the fewer data points and countries involved in generating it—the wider the confidence bands of the coefficient, the higher the likelihood of incurring in an omitted variable bias or reverse causality.

Here, I therefore evaluate whether the LMU trade effects were heterogeneous across countries exploiting the LMU-wide econometric estimates discussed in Section [4.1](https://arxiv.org/html/2510.25487v1#S4.SS1 "4.1 Main results ‣ 4 Results ‣ The Latin Monetary Union and Trade: A Closer Look11footnote 1I am deeply grateful to Christopher M. Meissner for sharing his database on monetary standards. I thank Teodoro D’Agostino for excellent research assistance in coding RICardo bilateral trade flows to standardized ISO codes. I also thank Rodolfo G. Campos, and Marc Badia-Miró for helpful comments and suggestions The views expressed in this paper are those of the authors and do therefore not necessarily reflect those of the Banco de España or the Eurosystem."), derived from Equation [5](https://arxiv.org/html/2510.25487v1#S3.E5 "In 3.1 Methodology ‣ 3 Methodology and Data ‣ The Latin Monetary Union and Trade: A Closer Look11footnote 1I am deeply grateful to Christopher M. Meissner for sharing his database on monetary standards. I thank Teodoro D’Agostino for excellent research assistance in coding RICardo bilateral trade flows to standardized ISO codes. I also thank Rodolfo G. Campos, and Marc Badia-Miró for helpful comments and suggestions The views expressed in this paper are those of the authors and do therefore not necessarily reflect those of the Banco de España or the Eurosystem."), within a model-based approach, grounded in trade theory. There are two main reasons for preferring this approach. First, the model extends beyond partial equilibrium bilateral trade effects to assess the effects within a general equilibrium framework. By doing so, it also accounts for possible trade diversion effects, and therefore allows to calculate with more precision the total (and not only the bilateral) trade gains. Second, as it is based on LMU-wide estimates, it also minimizes the concerns noted in the previous paragraphs.

One of the beauties of this class of general equilibrium models—often referred to as ‘‘universal gravity’’ models (Allen et al., [2020](https://arxiv.org/html/2510.25487v1#bib.bib1))—is that it allows to capture heterogeneous trade effects across countries even when a uniform reduction in trade costs across all country pairs within a currency union (or a trade agreement) is used. Indeed, the ‘‘universal gravity’’ is a powerful framework for economists seeking to understand how trade flows respond to changes in trade costs. When used in counterfactual simulations—–such as changing trade barriers within the LMU—–the model shows how trade between countries adjusts based on the structure of existing trade relationships. Crucially, it does this in a transparent and data-driven way: the size of country-level effects depends on how much countries involved in trade costs reductions already trade with each other. If two countries are major trading partners, a reduction in trade costs will lead to a large increase in their total trade; if their trade is minimal to begin with, the effect will be modest. This intuitive mechanism makes the model especially appealing for historical analysis, as it allows researchers to isolate the impact of trade cost changes within a rigorous yet tractable framework, without needing to model preferences, technologies, or other more complex dynamics.202020For the details of the model, see Appendix [B](https://arxiv.org/html/2510.25487v1#A2 "Appendix B Theoretical Appendix ‣ The Latin Monetary Union and Trade: A Closer Look11footnote 1I am deeply grateful to Christopher M. Meissner for sharing his database on monetary standards. I thank Teodoro D’Agostino for excellent research assistance in coding RICardo bilateral trade flows to standardized ISO codes. I also thank Rodolfo G. Campos, and Marc Badia-Miró for helpful comments and suggestions The views expressed in this paper are those of the authors and do therefore not necessarily reflect those of the Banco de España or the Eurosystem.").

Therefore, building on this framework, it is possible to implement counterfactual simulations. The baseline consists of observed trade flows recorded in the database, i.e. the actual transactions that occurred between 1865 and 1873.212121As the model is a static model, I use the average of the flows between those years. The counterfactual calculates what trade would have taken place had Belgium, France, Greece, Italy, and Switzerland not joined the LMU. The difference between these two measures reveals the part of trade attributable to the LMU.

The simulation exercise requires only four key inputs: a complete and square bilateral trade matrix for a chosen baseline year,
a specified change in trade costs, and two elasticity parameters—the trade elasticity and the supply elasticity. The former (trade elasticity) tells us how much trade between countries increases or decreases in response to a change in trade costs, while the latter (supply elasticity) reflects how producers adjust their output when export prices change.222222I run the counterfactual simulation using the ge\_gravity2 command (Campos et al., [2025](https://arxiv.org/html/2510.25487v1#bib.bib13)). This command allows users to compute counterfactual trade flows in a large class of general equilibrium trade models in Stata.

Therefore, for the bilateral trade matrix, I build upon the one employed in partial equilibrium estimations.232323To obtain a complete and square bilateral trade matrix I first set to zero missing trade data for the first year of the database, 1860. Second, I interpolate (and extrapolate) existing trade data. Third, I take the average of the resulting trade flows between 1865 and 1873. This strategy is unlikely to distort the results of the general equilibrium trade model used. Indeed, in this class of trade models, what fundamentally drives outcomes are relative trade costs and trade shares, not the absolute levels of trade flows. As long as the relative structure of trade flows is preserved (meaning which countries trade more or less with each other), the model can recover meaningful counterfactuals. Setting missing flows to zero in 1860 and interpolating data helps ensure completeness without necessarily introducing artificial asymmetries. Moreover, by averaging over a nine-year period 1865–1873, it is possible to smooth out short-term noise and capture a representative pattern of trade relationships.. The change in trade costs is derived by making use of the structural estimates obtained in partial equilibrium, under the standard assumption of symmetry.242424See, for example, Mayer et al. ([2019](https://arxiv.org/html/2510.25487v1#bib.bib39)). This means that I treat the effects of joining and leaving the LMU as mirror images—the effect of the LMU had on reducing trade costs is assumed to be equal in size and opposite in sign to the effect of not being there. More precisely, this means that the change in bilateral trade costs in the counterfactual world without the LMU is given by

|  |  |  |
| --- | --- | --- |
|  | τ^i​j​t={exp⁡(−β^1/θ),if i and j both identify LMU members,1,otherwise.\hat{\tau}\_{ijt}=\begin{cases}\exp\left(-\hat{\beta}\_{1}/\theta\right),&\text{if $i$ and $j$ both identify LMU members,}\\ 1,&\text{otherwise.}\end{cases} |  |

Trade and supply elasticities are calibrated based on values commonly used in the international trade literature. Specifically, I set the trade elasticity, θ\theta, to 5, similar to the value contained in the famous meta-analysis by Head and Mayer ([2014](https://arxiv.org/html/2510.25487v1#bib.bib33)). The supply elasticity is set to 1.24.252525However, since the text only discusses counterfactual results for trade, the choice of supply elasticity is less relevant, as this parameter is particularly important for welfare. This value has been computed by Campos et al. ([2023](https://arxiv.org/html/2510.25487v1#bib.bib12)) using statistics from Huo et al. ([2023](https://arxiv.org/html/2510.25487v1#bib.bib35)), and positions my calibration between the benchmarks established by Eaton and Kortum ([2002](https://arxiv.org/html/2510.25487v1#bib.bib16)) and Alvarez and Lucas ([2007](https://arxiv.org/html/2510.25487v1#bib.bib2)).262626Trade deficits are also an integral ingredient of the model to solve counterfactual simulations. As explained in Head and Mayer ([2022](https://arxiv.org/html/2510.25487v1#bib.bib34)), there is no fully satisfying way to model trade deficits in a static model. A common assumption in the literature, which I also adopt in this paper, is that trade deficits are fully exogenous and therefore constant. Another possible assumption, often referred to as “multiplicative” assumption in the literature, is that trade deficits increase automatically with income (though not necessarily at the same rate). While these assumptions are theoretically different, changing them produces very similar results. Therefore, the choice is not particularly relevant in practical terms.

The results of the general equilibrium model are shown in Figure [5](https://arxiv.org/html/2510.25487v1#S4.F5 "Figure 5 ‣ 4.3 Extension: Core - Periphery (or the LMU’s heterogeneous trade effects) ‣ 4 Results ‣ The Latin Monetary Union and Trade: A Closer Look11footnote 1I am deeply grateful to Christopher M. Meissner for sharing his database on monetary standards. I thank Teodoro D’Agostino for excellent research assistance in coding RICardo bilateral trade flows to standardized ISO codes. I also thank Rodolfo G. Campos, and Marc Badia-Miró for helpful comments and suggestions The views expressed in this paper are those of the authors and do therefore not necessarily reflect those of the Banco de España or the Eurosystem."). The Figure shows the proportion of international trade among LMU members that the model attributes to the LMU (‘‘LMU-driven’’). The simulation shows that the LMU was an important positive factor for all its members. However, it also shows that its effects were uneven across countries. While France stands out in absolute terms (panel a), the relative trade gains (panel b) of France (7.3%) and Greece (7.6%) were between a half and two-thirds the size of those of Switzerland (11.4%) and Italy (12.1%). Belgium stands somewhere in the middle (9.6%).

![Refer to caption](x6.png)


(a) Levels, millions (£)

![Refer to caption](x7.png)


(b) % of total trade

Figure 5: LMU-driven trade increase by country

Note: The simulations use the quantitative trade model described in this section for a trade elasticity of 5 and a supply elasticity of 1.24.

## 5 Conclusions

The LMU was a 19th century agreement among several European countries to standardize their currencies through a bimetallic system based on fixed gold and silver content.
In this paper, I analyze its effects on trade using state-of-the-art gravity techniques and, crucially, accounting for the diversity of currency regimes during the early years of the LMU—therefore addressing a potential source of omitted variable bias.

The evidence presented in this paper suggests that the LMU had a meaningful, though short-lived, impact on trade among its members. In the initial phase following its establishment (1865–1873), when bimetallism remained a credible monetary arrangement, trade among its members increased by approximately 30%. These effects then started rapidly fading, converging to zero by the end of the 1870s, when new silver coin minting ceased across the LMU. A model-based assessment suggests that, between 1865 and 1873, the LMU raised total international trade by an average of 9.6%, though the gains were uneven: Switzerland and Italy experienced the largest relative gains, followed by Belgium, Greece, and France.

Similar methods could be applied in future research to examine the impact of other historically important exchange rate regimes or trade policy choices on trade.

## References

* Allen et al. (2020)

  Allen, T., C. Arkolakis, and Y. Takahashi (2020): ‘‘Universal Gravity,’’ *Journal of Political Economy*, 128, 393–433.
* Alvarez and Lucas (2007)

  Alvarez, F. and R. J. Lucas (2007): ‘‘General equilibrium analysis of the Eaton-Kortum model of international trade,’’ *Journal of Monetary Economics*, 54, 1726–1768.
* Anderson and van Wincoop (2003)

  Anderson, J. E. and E. van Wincoop (2003): ‘‘Gravity with Gravitas: A Solution to the Border Puzzle,’’ *American Economic Review*, 93, 170–192.
* Badia-Miró et al. (2025)

  Badia-Miró, M., R. Campos, and J. Timini (2025): ‘‘The Gold Standard and International Trade,’’ .
* Bae and Bailey (2011)

  Bae, K.-H. and W. Bailey (2011): ‘‘The Latin Monetary Union: Some evidence on Europe’s failed common currency,’’ *Review of Development Finance*, 1, 131–149.
* Baier and Bergstrand (2007)

  Baier, S. L. and J. H. Bergstrand (2007): ‘‘Do Free Trade Agreements Actually Increase Members’ International Trade?’’ *Journal of International Economics*, 71, 72–95.
* Baier et al. (2019)

  Baier, S. L., Y. V. Yotov, and T. Zylkin (2019): ‘‘On the widely differing effects of free trade agreements: Lessons from twenty years of trade integration,’’ *Journal of International Economics*, 116, 206–226.
* Baldwin and Taglioni (2007)

  Baldwin, R. and D. Taglioni (2007): ‘‘Trade Effects of the Euro: a Comparison of Estimators,’’ *Journal of Economic Integration*, 22, 780–818.
* Bergstrand et al. (2015)

  Bergstrand, J. H., M. Larch, and Y. V. Yotov (2015): ‘‘Economic integration agreements, border effects, and distance elasticities in the gravity equation,’’ *European Economic Review*, 78, 307–327.
* Bordo and Jonung (2000)

  Bordo, M. D. and L. Jonung (2000): *Lessons for EMU from the History of Monetary Unions*, London: Institute of Economic Affairs.
* Bordo and Rockoff (1996)

  Bordo, M. D. and H. Rockoff (1996): ‘‘The Gold Standard as a "Good Housekeeping Seal of Approval",’’ *The Journal of Economic History*, 56, 389–428.
* Campos et al. (2023)

  Campos, R. G., D. Furceri, J. Estefania-Flores, and J. Timini (2023): ‘‘Geopolitical Fragmentation and Trade,’’ *Journal of Comparative Economics*, 51, 1289–1315.
* Campos et al. (2025)

  Campos, R. G., I. Reggio, and J. Timini (2025): ‘‘ge\_gravity2: a command to solve universal gravity models,’’ *The Stata Journal*, forthcoming.
* Campos et al. (2021)

  Campos, R. G., J. Timini, and E. Vidal (2021): ‘‘Structural gravity and trade agreements: Does the measurement of domestic trade matter?’’ *Economics Letters*, 208.
* Dedinger and Girard (2017)

  Dedinger, B. and P. Girard (2017): ‘‘Exploring trade globalization in the long run: The RICardo project,’’ *Historical Methods: A Journal of Quantitative and Interdisciplinary History*, 50, 30–48.
* Eaton and Kortum (2002)

  Eaton, J. and S. Kortum (2002): ‘‘Technology, Geography, and Trade,’’ *Econometrica*, 70, 1741–1779.
* Egger et al. (2022)

  Egger, P. H., M. Larch, and Y. V. Yotov (2022): ‘‘Gravity Estimations with Interval Data: Revisiting the Impact of Free Trade Agreements,’’ *Economica*, 89, 44–61.
* Egger and Tarlea (2015)

  Egger, P. H. and F. Tarlea (2015): ‘‘Multi-way clustering estimation of standard errors in gravity models,’’ *Economics Letters*, 134, 144–147.
* Einaudi (2000)

  Einaudi, L. (2000): ‘‘From the Franc to the ‘Europe’: Great Britain, Germany and the attempted transformation of the Latin Monetary Union into a European Monetary Union,’’ *Economic History Review*, 53, 284–308.
* Einaudi (2001)

  ——— (2001): *Money and Politics, European Monetary Unification and the Gold Standard (1865-73)*, Oxford University Press, Oxford.
* Estevadeordal et al. (2003)

  Estevadeordal, A., B. Frantz, and A. M. Taylor (2003): ‘‘The Rise and Fall of World Trade, 1870–1939,’’ *The Quarterly Journal of Economics*, 118, 359–407.
* Federico et al. (2012)

  Federico, G., S. Natoli, G. Tattara, and M. Vasta (2012): *Il commercio estero italiano, 1862-1950*, Collana storica della Banca d’Italia – Serie “Statistiche storiche, vol. IV, Roma-Bari: Laterza.
* Fendel and Maurer (2015)

  Fendel, R. and D. Maurer (2015): ‘‘Does European History Repeat Itself ? : Lessons from the Latin Monetary Union for the European Monetary Union,’’ *Journal of Economic Integration*, 30, 93–120.
* Flandreau (1996)

  Flandreau, M. (1996): ‘‘The French Crime of 1873: An Essay on the Emergence of the International Gold Standard, 1870–1880,’’ *The Journal of Economic History*, 56, 862–897.
* Flandreau (2000)

  ——— (2000): ‘‘The economics and politics of monetary unions: a reassessment of the Latin Monetary Union, 1865–71,’’ *Financial History Review*, 7, 25–44.
* Flandreau and Oosterlinck (2012)

  Flandreau, M. and K. Oosterlinck (2012): ‘‘Was the emergence of the international gold standard expected? Evidence from Indian Government securities,’’ *Journal of Monetary Economics*, 59, 649–669.
* Foquin and Hugot (2016)

  Foquin, M. and J. Hugot (2016): ‘‘Two Centuries of Bilateral Trade and Gravity Data: 1827-2014,’’ Working Papers 2016-14, CEPII.
* Gibler (2009)

  Gibler, D. (2009): *International Military Alliances, 1648-2008*, Congressional Quarterly Press.
* Gillard (2017)

  Gillard, L. (2017): *L’Union latine, une expérience de souverainetés monétaires partagées (1865-1926)*, Classiques Garnier, Paris.
* Glick and Rose (2016)

  Glick, R. and A. K. Rose (2016): ‘‘Currency unions and trade: A post-EMU reassessment,’’ *European Economic Review*, 87, 78–91.
* Gowa and Hicks (2013)

  Gowa, J. and R. Hicks (2013): ‘‘Politics, Institutions, and Trade: Lessons of the Interwar Era,’’ *International Organization*, 67, 439–467.
* Gowa and Hicks (2017)

  ——— (2017): ‘‘Commerce and Conflict: New Data about the Great War,’’ *British Journal of Political Science*, 47, 653–674.
* Head and Mayer (2014)

  Head, K. and T. Mayer (2014): ‘‘Gravity Equations: Workhorse,Toolkit, and Cookbook,’’ in *Handbook of International Economics*, ed. by G. Gopinath, . Helpman, and K. Rogoff, Elsevier, vol. 4 of *Handbook of International Economics*, chap. 0, 131–195.
* Head and Mayer (2022)

  ——— (2022): ‘‘Welfare effects of Balkan trade liberalization through the lens of structural gravity,’’ Tech. rep., mimeo.
* Huo et al. (2023)

  Huo, Z., A. A. Levchenko, and N. Pandalai-Nayar (2023): ‘‘International Comovement in the Global Production Network,’’ *Review of Economic Studies*, forthcoming.
* Karlsson and Hedberg (2021)

  Karlsson, L. and P. Hedberg (2021): ‘‘War and trade in the peaceful century: the impact of interstate wars on bilateral trade flows during the first wave of globalization, 1830â€“1913,’’ *Economic History Review*, 74, 809–830.
* López-Córdova and Meissner (2003)

  López-Córdova, J. E. and C. M. Meissner (2003): ‘‘Exchange-Rate Regimes and International Trade: Evidence from the Classical Gold Standard Era,’’ *American Economic Review*, 93, 344–353.
* Maoz et al. (2019)

  Maoz, Z., P. L. Johnson, J. Kaplan, F. Ogunkoya, and A. P. Shreve (2019): ‘‘The Dyadic Militarized Interstate Disputes (MIDs) Dataset Version 3.0: Logic, Characteristics, and Comparisons to Alternative Datasets,’’ *Journal of Conflict Resolution*, 63, 811–835.
* Mayer et al. (2019)

  Mayer, T., V. Vicard, S. Zignago, and B. Javorcik (2019): ‘‘The cost of non-Europe, revisited,’’ *Economic Policy*, 34, 145–199.
* Meissner (2001)

  Meissner, C. M. (2001): ‘‘The World Order: The Emergence of an International Monetary System, 1850 to 1913,’’ Ph.D. thesis, University of California Berkeley.
* Meissner (2015)

  ——— (2015): ‘‘The Limits of Bimetallism,’’ in *Federal Reserve Policy Seen Through the Lens of Economic History: Essays to Commemorate the Federal Reserve System’s Centennial*, ed. by O. Humpage, Cambridge: Cambridge University Press, 194–216.
* Meissner (2024)

  ——— (2024): *One From the Many: The Global Economy Since 1850*, Oxford University Press, Oxford.
* Micco et al. (2003)

  Micco, A., E. Stein, and G. Ordoñez (2003): ‘‘The currency union effect on trade: early evidence from EMU [‘A theoretical foundation for the gravity equation’],’’ *Economic Policy*, 18, 315–356.
* Mitchener et al. (2010)

  Mitchener, K. J., M. Shizume, and M. D. Weidenmier (2010): ‘‘Why did Countries Adopt the Gold Standard? Lessons from Japan,’’ *The Journal of Economic History*, 70, 27–56.
* Nagengast and Yotov (2025)

  Nagengast, A. J. and Y. V. Yotov (2025): ‘‘Staggered Difference-in-Differences in Gravity Settings: Revisiting the Effects of Trade Agreements,’’ *American Economic Journal: Applied Economics*, 17, 271–296.
* New York Times (1885)

  New York Times (1885): ‘‘The Check to Bimetallism,’’ New York Times, published on November 24.
* Officer (2020)

  Officer, L. H. (2020): ‘‘Gold Standard,’’ Tech. rep., eh.net.
* Polák (2019)

  Polák, P. (2019): ‘‘The Euro’S Trade Effect: A Meta‐Analysis,’’ *Journal of Economic Surveys*, 33, 101–124.
* Santos Silva and Tenreyro (2006)

  Santos Silva, J. M. C. and S. Tenreyro (2006): ‘‘The Log of Gravity,’’ *The Review of Economics and Statistics*, 88, 641–658.
* Timini (2018)

  Timini, J. (2018): ‘‘Currency unions and heterogeneous trade effects: the case of the Latin Monetary Union,’’ *European Review of Economic History*, 22, 322–348.
* Timini (2023)

  ——— (2023): ‘‘Revisiting the ‘Cobden-Chevalier network’ trade and welfare effects,’’ *Explorations in Economic History*, 89.
* Vicquéry (2021)

  Vicquéry, R. (2021): ‘‘The Common Currency Effect on International Trade: Evidence from an Accidental Monetary Union,’’ Working Papers 856, Banque de France.
* Weidner and Zylkin (2021)

  Weidner, M. and T. Zylkin (2021): ‘‘Bias and consistency in three-way gravity models,’’ *Journal of International Economics*, 132.
* Willis (1901)

  Willis, H. P. (1901): *History of the Latin Monetary Union*, Chicago: University of Chicago Press.
* Yotov (2022)

  Yotov, Y. V. (2022): ‘‘On the Role of Domestic Trade Flows for Estimating the Gravity Model of Trade,’’ *Contemporary Economic Policy*, 40, 526–540.
* Yotov et al. (2016)

  Yotov, Y. V., R. Piermartini, J. A. Monteiro, and M. Larch (2016): *An Advanced Guide to Trade Policy Analysis: The Structural Gravity Model*, WTO/UNCTAD.

## Appendix A Summary statistics

Table A.1: Countries included in the sample: ISO codes

| ARG | AUS | AUT | BEL | BGR | BRA |
| --- | --- | --- | --- | --- | --- |
| CAN | CHE | CHL | CHN | COL | CUB |
| DEU | DNK | EGY | ESP | FIN | FRA |
| GBR | GRC | IDN | IND | ITA | JPN |
| KOR | MEX | NLD | NOR | NZL | PHL |
| PRT | RUS | SWE | TWN | URY | USA |
| ZAF |  |  |  |  |  |

## Appendix B Theoretical Appendix

In this Appedix, I describe a simplified version of the model used in Section [4.3](https://arxiv.org/html/2510.25487v1#S4.SS3 "4.3 Extension: Core - Periphery (or the LMU’s heterogeneous trade effects) ‣ 4 Results ‣ The Latin Monetary Union and Trade: A Closer Look11footnote 1I am deeply grateful to Christopher M. Meissner for sharing his database on monetary standards. I thank Teodoro D’Agostino for excellent research assistance in coding RICardo bilateral trade flows to standardized ISO codes. I also thank Rodolfo G. Campos, and Marc Badia-Miró for helpful comments and suggestions The views expressed in this paper are those of the authors and do therefore not necessarily reflect those of the Banco de España or the Eurosystem."), with labor as the onyl factor of production.

Let Xi​j≥0X\_{ij}\geq 0 denote the value of trade flows from country ii (exporter) to country jj (importer). The case i=ji=j denotes intra-national (domestic) trade and i≠ji\neq j international trade. In a standard structural gravity system, bilateral flows satisfy

|  |  |  |  |
| --- | --- | --- | --- |
|  | Xi​j=Yi​EjY​(τi​jΩi​Πj)−θ,X\_{ij}\;=\;\frac{Y\_{i}\,E\_{j}}{Y}\left(\frac{\tau\_{ij}}{\Omega\_{i}\,\Pi\_{j}}\right)^{-\theta}, |  | (7) |

where Yi≡∑jXi​jY\_{i}\equiv\sum\_{j}X\_{ij} is production (income) in ii, Ej≡∑iXi​jE\_{j}\equiv\sum\_{i}X\_{ij} is expenditure in jj, and Y≡∑iYi=∑jEjY\equiv\sum\_{i}Y\_{i}=\sum\_{j}E\_{j} is world income. Structural gravity further imposes the multilateral resistance (MR) conditions

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ωi−θ=∑j(τi​jΠj)−θ​EjY,\Omega\_{i}^{-\theta}\;=\;\sum\_{j}\left(\frac{\tau\_{ij}}{\Pi\_{j}}\right)^{-\theta}\frac{E\_{j}}{Y}, |  | (8) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | Πj−θ=∑i(τi​jΩi)−θ​YiY,\Pi\_{j}^{-\theta}\;=\;\sum\_{i}\left(\frac{\tau\_{ij}}{\Omega\_{i}}\right)^{-\theta}\frac{Y\_{i}}{Y}, |  | (9) |

where Ωi\Omega\_{i} is the outward MR term (exporter ii’s access to destination markets) and Πj\Pi\_{j} is the inward MR term (the extent of competitive supply facing importers in jj). Higher trade costs τi​j\tau\_{ij} (tariffs and non-tariff barriers, geography, culture, etc.) reduce Xi​jX\_{ij}; MR terms summarize the general-equilibrium influence of all partners on each bilateral flow. So far, this part is a brief overview of the information previously outlined in the main text, from Equation [7](https://arxiv.org/html/2510.25487v1#A2.E7 "In Appendix B Theoretical Appendix ‣ The Latin Monetary Union and Trade: A Closer Look11footnote 1I am deeply grateful to Christopher M. Meissner for sharing his database on monetary standards. I thank Teodoro D’Agostino for excellent research assistance in coding RICardo bilateral trade flows to standardized ISO codes. I also thank Rodolfo G. Campos, and Marc Badia-Miró for helpful comments and suggestions The views expressed in this paper are those of the authors and do therefore not necessarily reflect those of the Banco de España or the Eurosystem.") to Equation [9](https://arxiv.org/html/2510.25487v1#A2.E9 "In Appendix B Theoretical Appendix ‣ The Latin Monetary Union and Trade: A Closer Look11footnote 1I am deeply grateful to Christopher M. Meissner for sharing his database on monetary standards. I thank Teodoro D’Agostino for excellent research assistance in coding RICardo bilateral trade flows to standardized ISO codes. I also thank Rodolfo G. Campos, and Marc Badia-Miró for helpful comments and suggestions The views expressed in this paper are those of the authors and do therefore not necessarily reflect those of the Banco de España or the Eurosystem.").

Define import shares

|  |  |  |  |
| --- | --- | --- | --- |
|  | λi​j≡Xi​jEj=YiY​(τi​jΩi​Πj)−θ,\lambda\_{ij}\;\equiv\;\frac{X\_{ij}}{E\_{j}}\;=\;\frac{Y\_{i}}{Y}\left(\frac{\tau\_{ij}}{\Omega\_{i}\,\Pi\_{j}}\right)^{-\theta}, |  | (10) |

so that ∑iλi​j=1\sum\_{i}\lambda\_{ij}=1 and λi​i\lambda\_{ii} measures ii’s home share.

#### Hat algebra.

For any variable xx, let x^≡x′/x\widehat{x}\equiv x^{\prime}/x denote the change between a counterfactual (′) and the benchmark. From ([7](https://arxiv.org/html/2510.25487v1#A2.E7 "In Appendix B Theoretical Appendix ‣ The Latin Monetary Union and Trade: A Closer Look11footnote 1I am deeply grateful to Christopher M. Meissner for sharing his database on monetary standards. I thank Teodoro D’Agostino for excellent research assistance in coding RICardo bilateral trade flows to standardized ISO codes. I also thank Rodolfo G. Campos, and Marc Badia-Miró for helpful comments and suggestions The views expressed in this paper are those of the authors and do therefore not necessarily reflect those of the Banco de España or the Eurosystem.")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | X^i​j=Y^i​E^j​τ^i​j−θ​Ω^iθ​Π^jθ.\widehat{X}\_{ij}\;=\;\widehat{Y}\_{i}\;\widehat{E}\_{j}\;\widehat{\tau}\_{ij}^{-\theta}\;\widehat{\Omega}\_{i}^{\theta}\;\widehat{\Pi}\_{j}^{\theta}. |  | (11) |

#### Model structure and the share sufficient statistic.

In the workhorse quantitative models (Armington, Eaton–Kortum, Melitz, etc.), with inelastic labor as the only factor, the change in import shares depends only on wages and bilateral trade costs. The standard Dekle–Eaton–Kortum share change is

|  |  |  |  |
| --- | --- | --- | --- |
|  | λ^i​j=(w^i)−θ​τ^i​j−θ∑kλk​j​(w^k)−θ​τ^k​j−θ.\widehat{\lambda}\_{ij}\;=\;\frac{\left(\widehat{w}\_{i}\right)^{-\theta}\;\widehat{\tau}\_{ij}^{-\theta}}{\sum\limits\_{k}\lambda\_{kj}\,\left(\widehat{w}\_{k}\right)^{-\theta}\;\widehat{\tau}\_{kj}^{-\theta}}. |  | (12) |

#### Market clearing and the wage fixed point.

With labor as the only factor, Yi=wi​LiY\_{i}=w\_{i}L\_{i} and Y^i=w^i\widehat{Y}\_{i}=\widehat{w}\_{i} when LiL\_{i} is fixed. Market clearing implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | w^i=1Yi​∑jXi​j′=1Yi​∑jλi​j′​Ej′=1Yi​∑jλi​j​λ^i​j​Ej′,\displaystyle\widehat{w}\_{i}\;=\;\frac{1}{Y\_{i}}\sum\_{j}X\_{ij}^{\prime}\;=\;\frac{1}{Y\_{i}}\sum\_{j}\lambda\_{ij}^{\prime}\,E\_{j}^{\prime}\;=\;\frac{1}{Y\_{i}}\sum\_{j}\lambda\_{ij}\,\widehat{\lambda}\_{ij}\,E\_{j}^{\prime}, |  | (13) |

where we used Xi​j′=λi​j′​Ej′X\_{ij}^{\prime}=\lambda\_{ij}^{\prime}E\_{j}^{\prime} and λi​j′=λi​j​λ^i​j\lambda\_{ij}^{\prime}=\lambda\_{ij}\widehat{\lambda}\_{ij}.

In general, expenditure does not equal production because there are trade deficits. A trade deficit is defined by Ej=Yj+DjE\_{j}=Y\_{j}+D\_{j} and Ej′=Yj​Y^j+Dj​D^jE\_{j}^{\prime}=Y\_{j}\hat{Y}\_{j}+D\_{j}\hat{D}\_{j}. There are two alternative assumptions that are commonly made to deal with the evolution of trade deficits. The first consists in the deficit to be ‘‘additive’’. This means that the deficit remains constant and D^j=1\hat{D}\_{j}=1. The second consists in the deficit to be ‘‘multiplicative’’. This means that the deficit evolves in proportion to GDP, so that D^j=Y^j\hat{D}\_{j}=\hat{Y}\_{j}.
In the first case, Ej′=Yj​Y^j+Dj=Yj​w^j+DjE\_{j}^{\prime}=Y\_{j}\hat{Y}\_{j}+D\_{j}=Y\_{j}\hat{w}\_{j}+D\_{j}, and in the second case Ej′=Ej​Y^j=Ej​w^jE\_{j}^{\prime}=E\_{j}\hat{Y}\_{j}=E\_{j}\hat{w}\_{j}.

In practical terms, the two assumptions are similar for counterfactual results, as in most cases, numbers obtained with one or the other option tend to be very similar. For the purpose of this demonstration, let trade deficits evolve *multiplicatively* with GDP, so Ej′=Ej​w^jE\_{j}^{\prime}=E\_{j}\,\widehat{w}\_{j}. Substituting ([12](https://arxiv.org/html/2510.25487v1#A2.E12 "In Model structure and the share sufficient statistic. ‣ Appendix B Theoretical Appendix ‣ The Latin Monetary Union and Trade: A Closer Look11footnote 1I am deeply grateful to Christopher M. Meissner for sharing his database on monetary standards. I thank Teodoro D’Agostino for excellent research assistance in coding RICardo bilateral trade flows to standardized ISO codes. I also thank Rodolfo G. Campos, and Marc Badia-Miró for helpful comments and suggestions The views expressed in this paper are those of the authors and do therefore not necessarily reflect those of the Banco de España or the Eurosystem.")) and Ej′E\_{j}^{\prime} into ([13](https://arxiv.org/html/2510.25487v1#A2.E13 "In Market clearing and the wage fixed point. ‣ Appendix B Theoretical Appendix ‣ The Latin Monetary Union and Trade: A Closer Look11footnote 1I am deeply grateful to Christopher M. Meissner for sharing his database on monetary standards. I thank Teodoro D’Agostino for excellent research assistance in coding RICardo bilateral trade flows to standardized ISO codes. I also thank Rodolfo G. Campos, and Marc Badia-Miró for helpful comments and suggestions The views expressed in this paper are those of the authors and do therefore not necessarily reflect those of the Banco de España or the Eurosystem.")) gives the fixed-point system for wages:

|  |  |  |  |
| --- | --- | --- | --- |
|  | w^i=1Yi​∑jλi​j​(w^i)−θ​τ^i​j−θ∑kλk​j​(w^k)−θ​τ^k​j−θ​Ej​w^j.\widehat{w}\_{i}\;=\;\frac{1}{Y\_{i}}\sum\_{j}\lambda\_{ij}\,\frac{\left(\widehat{w}\_{i}\right)^{-\theta}\,\widehat{\tau}\_{ij}^{-\theta}}{\sum\limits\_{k}\lambda\_{kj}\,\left(\widehat{w}\_{k}\right)^{-\theta}\,\widehat{\tau}\_{kj}^{-\theta}}\;E\_{j}\,\widehat{w}\_{j}. |  | (14) |

Because of Walras’ Law, ([14](https://arxiv.org/html/2510.25487v1#A2.E14 "In Market clearing and the wage fixed point. ‣ Appendix B Theoretical Appendix ‣ The Latin Monetary Union and Trade: A Closer Look11footnote 1I am deeply grateful to Christopher M. Meissner for sharing his database on monetary standards. I thank Teodoro D’Agostino for excellent research assistance in coding RICardo bilateral trade flows to standardized ISO codes. I also thank Rodolfo G. Campos, and Marc Badia-Miró for helpful comments and suggestions The views expressed in this paper are those of the authors and do therefore not necessarily reflect those of the Banco de España or the Eurosystem.")) is homogeneous of degree zero in {w^i}\{\widehat{w}\_{i}\} and requires a normalization (we keep the nominal world output constant across scenarios, as in Baier et al., 2019).

#### Recovering other variables.

Once {w^i}\{\widehat{w}\_{i}\} are solved from ([14](https://arxiv.org/html/2510.25487v1#A2.E14 "In Market clearing and the wage fixed point. ‣ Appendix B Theoretical Appendix ‣ The Latin Monetary Union and Trade: A Closer Look11footnote 1I am deeply grateful to Christopher M. Meissner for sharing his database on monetary standards. I thank Teodoro D’Agostino for excellent research assistance in coding RICardo bilateral trade flows to standardized ISO codes. I also thank Rodolfo G. Campos, and Marc Badia-Miró for helpful comments and suggestions The views expressed in this paper are those of the authors and do therefore not necessarily reflect those of the Banco de España or the Eurosystem.")), the remaining objects follow:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Y^i=w^i,\displaystyle\widehat{Y}\_{i}=\widehat{w}\_{i}, | E^i=w^i,\displaystyle\widehat{E}\_{i}=\widehat{w}\_{i}, |  | (15) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | λ^i​j​ from ([12](https://arxiv.org/html/2510.25487v1#A2.E12 "In Model structure and the share sufficient statistic. ‣ Appendix B Theoretical Appendix ‣ The Latin Monetary Union and Trade: A Closer Look11footnote 1I am deeply grateful to Christopher M. Meissner for sharing his database on monetary standards. I thank Teodoro D’Agostino for excellent research assistance in coding RICardo bilateral trade flows to standardized ISO codes. I also thank Rodolfo G. Campos, and Marc Badia-Miró for helpful comments and suggestions The views expressed in this paper are those of the authors and do therefore not necessarily reflect those of the Banco de España or the Eurosystem.")),\displaystyle\widehat{\lambda}\_{ij}\text{ from \eqref{eq:lambda\_hat\_DEK}}, | X^i​j=λ^i​j​E^j.\displaystyle\widehat{X}\_{ij}\;=\;\widehat{\lambda}\_{ij}\,\widehat{E}\_{j}. |  | (16) |

When needed, inward MR changes can be recovered directly from baseline import shares:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Π^j−θ=∑kλk​j​(w^k)−θ​τ^k​j−θ.\widehat{\Pi}\_{j}^{-\theta}\;=\;\sum\_{k}\lambda\_{kj}\,\left(\widehat{w}\_{k}\right)^{-\theta}\,\widehat{\tau}\_{kj}^{-\theta}. |  | (17) |

(An explicit closed-form for Ω^i\widehat{\Omega}\_{i} is not required for computing ([16](https://arxiv.org/html/2510.25487v1#A2.E16 "In Recovering other variables. ‣ Appendix B Theoretical Appendix ‣ The Latin Monetary Union and Trade: A Closer Look11footnote 1I am deeply grateful to Christopher M. Meissner for sharing his database on monetary standards. I thank Teodoro D’Agostino for excellent research assistance in coding RICardo bilateral trade flows to standardized ISO codes. I also thank Rodolfo G. Campos, and Marc Badia-Miró for helpful comments and suggestions The views expressed in this paper are those of the authors and do therefore not necessarily reflect those of the Banco de España or the Eurosystem.")).)

#### Welfare.

Under standard CES preferences used in structural gravity, welfare changes are given by the change in real income, G^i=E^i/P^i\widehat{G}\_{i}=\widehat{E}\_{i}/\widehat{P}\_{i}, with the price index change pinned down by the inward MR. Using the structure above and the multiplicative deficit assumption, one obtains the familiar sufficient statistic

|  |  |  |  |
| --- | --- | --- | --- |
|  | G^i=λ^i​i−1/θ.\widehat{G}\_{i}\;=\;\widehat{\lambda}\_{ii}^{-1/\theta}. |  | (18) |