---
authors:
- Felix Reichel
doc_id: arxiv:2510.15617v1
family_id: arxiv:2510.15617
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Political Interventions to Reduce Single-Use Plastics (SUPs) and Price Effects:
  An Event Study for Austria and Germany'
url_abs: http://arxiv.org/abs/2510.15617v1
url_html: https://arxiv.org/html/2510.15617v1
venue: arXiv q-fin
version: 1
year: 2025
---


Felix Reichel
Department of Economics, Johannes Kepler University Linz

(October 2025)

###### Abstract

Single-use plastics (SUPs) create large environmental costs. After Directive (EU) 2019/904, Austria and Germany introduced producer charges and fund payments meant to cover clean-up work. Using a high-frequency panel of retail offer spells containing prices and a fixed-effects event study with two-way clustered standard errors, this paper measures how much these costs drive up consumer prices. We find clear price pass-through in Austria. When Austrian products are pooled, treated items are 13.01 index points higher than non-SUP controls within twelve months (DiD(12m); p<0.001p{<}0.001) and 19.42 points over the full post period (p<0.001p{<}0.001). By product, balloons show strong and lasting effects (DiD(12m)=13.43, p=0.007p{=}0.007; Full DiD=19.96, p<0.001p{<}0.001). Cups show mixed short-run movements (e.g., DiD(12m)=-22.73, p=0.096p{=}0.096) and a positive but imprecise full-period contrast.

Keywords: single-use plastics; environmental policy; extended producer responsibility; deposit–refund; price pass-through; event study; difference-in-differences; retail prices; Austria; Germany.
  
JEL codes: Q53; Q58; H23; C23; D12.

## 1 Introduction

On EU beaches, plastics account for 80–85% of litter items; about half of those plastic items are single-use plastics (EU,, [2019](https://arxiv.org/html/2510.15617v1#bib.bib6)). Cities and towns carry much of this load. Street sweeping and waste collection tied to plastic trash run into billions of euros each year, costs often shouldered by the public purse (EU,, [2019](https://arxiv.org/html/2510.15617v1#bib.bib6)).

COVID-19 confounding. The COVID-19 pandemic and its recovery phase generated broad supply and demand shocks and generalized inflation. To avoid mistaking those shifts for policy effects, we stress—and revisit across sections—that proper control groups are crucial and that controls that are not direct substitutes for treated SUP items are, in general, better during such periods. Environmental policy internalizes these external costs through taxes, fees, and producer responsibility so that buyers and sellers face closer-to-social prices (Fullerton and Metcalf,, [2001](https://arxiv.org/html/2510.15617v1#bib.bib12)). Under imperfect competition, the degree of price pass-through depends on demand curvature, cost shares, and market conduct (Weyl and Fabinger,, [2013](https://arxiv.org/html/2510.15617v1#bib.bib11)). Evidence from excise and sales taxes shows that pass-through to retail prices is often substantial (Marion and Muehlegger,, [2011](https://arxiv.org/html/2510.15617v1#bib.bib8); Besley and Rosen,, [1999](https://arxiv.org/html/2510.15617v1#bib.bib2)), and small levies on plastic bags have produced large consumption responses (Convery et al.,, [2007](https://arxiv.org/html/2510.15617v1#bib.bib5); Homonoff,, [2018](https://arxiv.org/html/2510.15617v1#bib.bib7)). Deposit–refund systems are a related design used to curb litter and improve collection (Walls,, [2011](https://arxiv.org/html/2510.15617v1#bib.bib10)).

Member states in the EU moved on several fronts after Directive (EU) 2019/904: bans for selected items, labels, and producer responsibility rules (EU,, [2019](https://arxiv.org/html/2510.15617v1#bib.bib6)). Austria and Germany implemented different but comparable schemes that finance clean-up and reporting. This paper asks a narrow question inside that broader effort: do these upstream charges reach the shelf? If so, relative prices should move in favor of non-SUP alternatives.

We use monthly price data for items linked to SUP rules and close comparators outside those rules in both Austria and Germany. The design is an event study with product and retailer fixed effects.

## 2 Policy Background

Background is the EU Directive (EU) 2019/904 which aims to cut the damage from specific plastic products by pushing producers and buyers to face clean-up costs and by reducing items that are hard to collect (EU,, [2019](https://arxiv.org/html/2510.15617v1#bib.bib6)). Member states received latitude on the exact toolkit.

### 2.1 Austria: Producer Charges and Reporting (Treatment Year 2022)

Austria relies on producer charges tied to quantities sold and a digital reporting portal. Since 2023, producers report volumes through ARA Online. In 2022, Austria added product-based charges reflecting cleanup costs:

* •

  Food packaging, beverage cups, plastic wraps: €225 per ton
* •

  Tobacco products with plastic filters: €450 per ton

Micro-enterprises or very small quantities can opt for a €13 flat payment (BMK,, [2024](https://arxiv.org/html/2510.15617v1#bib.bib3)). Revenues support local waste crews, litter prevention, and upgrades to collection and sorting.

### 2.2 Germany: Single-Use Plastics Fund Act (EWKFondsG, 2024)

Germany runs a central fund. The Einwegkunststofffondsgesetz took effect on January 1, 2024. Producers register in DIVID and pay per product and weight. The Federal Environment Agency (UBA) manages inflows and distributes money to municipalities for street cleaning, bin maintenance, and disposal tied to SUPs (UBA,, [2024](https://arxiv.org/html/2510.15617v1#bib.bib9)). Item-specific fees mirror documented cleanup burdens.

## 3 Data and Methodology

#### Data coverage.

The working dataset is a monthly product–retailer panel spanning January 2020 to May 2025 built from high-frequency offer spells. For each product ii and retailer jj, we observe prices in month tt. Items include products treated under SUP rules (e.g., balloons, to-go plastic cups) and non-SUP controls. Precise construction and control selection are detailed in Appendix [A](https://arxiv.org/html/2510.15617v1#A1 "Appendix A The data pipeline, sample, and control selection ‣ Political Interventions to Reduce Single-Use Plastics (SUPs) and Price Effects: An Event Study for Austria and Germany").

#### Aggregation and index.

Raw quotes are aggregated to product–retailer–month (i,j,t)(i,j,t). Let p¯i​j​t\overline{p}\_{ijt} be the average price in month tt and define the base month as February 2022 (t=0t=0). We form a product–retailer specific index

|  |  |  |
| --- | --- | --- |
|  | Pi​j​t≡100×p¯i​j​tp¯i​j​0,t∈[−24,36].P\_{ijt}\equiv 100\times\frac{\overline{p}\_{ijt}}{\overline{p}\_{ij0}}\,,\qquad t\in[-24,36]. |  |

Our preferred outcome is the level index Yi​j​t=Pi​j​tY\_{ijt}=P\_{ijt} (percent of the February 2022 level). Event time is et=t−0=te\_{t}=t-0=t and we bin to 3-month steps b∈{…,−6,−3,0,3,6,…}b\in\{\ldots,-6,-3,0,3,6,\ldots\} via bint=⌊et/3⌋⋅3\text{bin}\_{t}=\lfloor e\_{t}/3\rfloor\cdot 3 with bin 0 as the reference.

#### Event-study specification.

For each group g∈{SUP,Non-SUP}g\in\{\text{SUP},\text{Non-SUP}\} we run the following regression on the corresponding subsample (treated and control are *estimated separately*):

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yi​j​t=∑b∈ℬ∖{0}βb(g)​ 1​{bint=b}+αi+δj+εi​j​t,Y\_{ijt}=\sum\_{b\in\mathcal{B}\setminus\{0\}}\beta^{(g)}\_{b}\,\mathbf{1}\{\text{bin}\_{t}=b\}\;+\;\alpha\_{i}\;+\;\delta\_{j}\;+\;\varepsilon\_{ijt}, |  | (1) |

where αi\alpha\_{i} are product fixed effects, δj\delta\_{j} are retailer fixed effects, and ℬ\mathcal{B} is the set of 3-month event bins from −24-24 to +36+36. The reference category is bin 0 (February 2022), so βb(g)\beta^{(g)}\_{b} measure changes relative to that month. We do not include time fixed effects. Standard errors are two-way clustered by product and retailer (Cameron et al.,, [2011](https://arxiv.org/html/2510.15617v1#bib.bib4)).

#### Windowed DiD summaries.

For communication, we report “DiD” summaries as simple averages of post- and pre-event bin coefficients within symmetric windows and then take the difference:

|  |  |  |
| --- | --- | --- |
|  | DiD(g)​(w)≡1|ℬw+|​∑b∈ℬw+βb(g)−1|ℬw−|​∑b∈ℬw−βb(g),\mathrm{DiD}^{(g)}(w)\equiv\frac{1}{|\mathcal{B}^{+}\_{w}|}\sum\_{b\in\mathcal{B}^{+}\_{w}}\beta^{(g)}\_{b}\;-\;\frac{1}{|\mathcal{B}^{-}\_{w}|}\sum\_{b\in\mathcal{B}^{-}\_{w}}\beta^{(g)}\_{b},\quad |  |

|  |  |  |
| --- | --- | --- |
|  | ℬw−={−w,−w+3,…,−3},\mathcal{B}^{-}\_{w}=\{-w,-w+3,\ldots,-3\},\; |  |

|  |  |  |
| --- | --- | --- |
|  | ℬw+={3,6,…,w}.\mathcal{B}^{+}\_{w}=\{3,6,\ldots,w\}. |  |

We report w∈{6,12}w\in\{6,12\} months and a “Full” contrast averaging over all b<0b<0 and all b>0b>0. These are linear combinations of ([1](https://arxiv.org/html/2510.15617v1#S3.E1 "In Event-study specification. ‣ 3 Data and Methodology ‣ Political Interventions to Reduce Single-Use Plastics (SUPs) and Price Effects: An Event Study for Austria and Germany")) coefficients; figures display 90% CIs for the individual bins, and we annotate DiD values accordingly.

#### Design choices and checks.

Treated vs. control contrasts rely on proximity of products in function and use while guarding against substitution and common shocks. The pattern in pre-event bins provides a visual parallel-paths check; we also report placebo models on non-SUP items. Details on sample building and control selection logic appear in Appendix [A](https://arxiv.org/html/2510.15617v1#A1 "Appendix A The data pipeline, sample, and control selection ‣ Political Interventions to Reduce Single-Use Plastics (SUPs) and Price Effects: An Event Study for Austria and Germany").

## 4 Results

The results chapter mixes pictures and tables. Figures display the binned coefficients. Tables print the underlying values for two cases: balloons and the full pooled Austria sample. Throughout, we note the potential for COVID-19–related inflation to confound price movements and rely on the control design (using non-direct substitutes) to reduce this risk.

### 4.1 Balloons (Austria)

![Refer to caption](4dabd46b-460a-48b6-9b51-72cc65691d84.png)


Figure 1: Figure 1 — Balloons: SUP vs. Non-SUP (event study, 3-month bins). Notes: event time relative to February 2022; fixed effects by product and retailer; two-way clustered standard errors. Controls are chosen to avoid direct substitutes to limit COVID-19 inflation confounding.

Balloons offer a clean story. Before the policy window, treated and control series sit near baseline. After the window opens, the treated series edges higher relative to controls. The gap aligns with the DiD summaries: the 12-month contrast is positive and the full-period contrast grows further. Given COVID-19–era inflation, relying on non-substitute controls helps ensure these contrasts are less likely to be artifacts of generalized price increases.

Table 1: Balloons: Treated vs. Control (Event-Study Coefficients)

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Treated | | | | Control | | | |
| Event Bin | Est. | SE | t | p | Est. | SE | t | p |
| -24 | -33.48∗∗ | 7.85 | -4.27 | 0.01 | 2.12 | 5.35 | 0.40 | 0.69 |
| -21 | -27.29∗ | 7.45 | -3.67 | 0.01 | 1.55 | 5.67 | 0.27 | 0.79 |
| -18 | -27.22∗ | 7.93 | -3.43 | 0.01 | -2.88 | 2.67 | -1.08 | 0.28 |
| -15 | -23.89∗ | 7.36 | -3.25 | 0.02 | -2.74 | 2.27 | -1.21 | 0.23 |
| -12 | -28.42∗∗ | 7.53 | -3.78 | 0.01 | -3.92∗ | 1.76 | -2.22 | 0.03 |
| -9 | -26.30∗ | 7.26 | -3.62 | 0.01 | -3.49. | 1.80 | -1.94 | 0.06 |
| -6 | -17.09 | 12.24 | -1.40 | 0.21 | 5.94 | 9.28 | 0.64 | 0.52 |
| -3 | -6.53 | 7.36 | -0.89 | 0.41 | -2.49∗∗ | 0.85 | -2.92 | 0.00 |
| 3 | -3.32 | 2.89 | -1.15 | 0.29 | 4.14∗∗ | 1.54 | 2.69 | 0.01 |
| 6 | -0.37 | 2.59 | -0.14 | 0.89 | 7.13∗∗ | 2.15 | 3.32 | 0.00 |
| 9 | -1.36 | 2.63 | -0.52 | 0.62 | 8.97∗∗∗ | 2.44 | 3.67 | 0.00 |
| 12 | -0.31 | 4.81 | -0.06 | 0.95 | 10.22∗∗∗ | 2.67 | 3.83 | 0.00 |
| 15 | -0.92 | 4.83 | -0.19 | 0.85 | 10.95∗∗∗ | 2.73 | 4.01 | 0.00 |
| 18 | 4.22 | 9.56 | 0.44 | 0.67 | 17.84∗ | 6.98 | 2.55 | 0.01 |
| 21 | 2.74 | 10.02 | 0.27 | 0.79 | 13.95∗∗∗ | 3.27 | 4.26 | 0.00 |
| 24 | -1.91 | 6.73 | -0.28 | 0.79 | 24.60∗ | 11.86 | 2.07 | 0.04 |
| 27 | 5.54 | 7.18 | 0.77 | 0.47 | 15.68∗∗∗ | 2.97 | 5.29 | 0.00 |
| 30 | 5.91. | 2.79 | 2.12 | 0.08 | 15.61∗∗∗ | 2.98 | 5.24 | 0.00 |
| 33 | 13.58 | 10.89 | 1.25 | 0.26 | 16.51∗∗∗ | 3.43 | 4.81 | 0.00 |
| Observations | 1,443 | | | | 69,473 | | | |
| RMSE | 19.00 | | | | 146.20 | | | |
| Adj. R2 | 0.56 | | | | 0.88 | | | |
| Within R2 | 0.18 | | | | 0.00 | | | |

* •

  OLS with product and retailer fixed effects. SEs clustered by product and retailer. Significance: ∗∗∗ p<.01p{<}.01, ∗∗ p<.05p{<}.05, ∗ p<.10p{<}.10, . p<.15p{<}.15.

### 4.2 To-Go Cups (Austria)

![Refer to caption](ae816902-64f7-46aa-9126-40aa54e6ee2b.png)


Figure 2: Figure 2 — Cups: SUP vs. Non-SUP (event study, 3-month bins). Notes: event time relative to February 2022; fixed effects by product and retailer; two-way clustered standard errors.

Cups move in a way shoppers recognize. Prices in the treated series jump and stay higher than controls through multiple bins. Several post-event estimates clear standard thresholds for statistical difference. Categories with fewer immediate substitutes tend to show faster pass-through, consistent with incidence theory (Weyl and Fabinger,, [2013](https://arxiv.org/html/2510.15617v1#bib.bib11)) and evidence from commodity taxes (Marion and Muehlegger,, [2011](https://arxiv.org/html/2510.15617v1#bib.bib8)).

### 4.3 Austria: Within-Country SUP vs. Non-SUP

![Refer to caption](f5909f55-881e-4cc2-a2a5-3de806380f4e.png)


Figure 3: Figure 3 — Austria: SUP vs. Non-SUP (event study, 3-month bins). Notes: event time relative to February 2022; fixed effects by product and retailer; two-way clustered standard errors. Control selection avoids direct substitutes to reduce COVID-19 confounding.

Pooling Austrian items tells a simple story. The treated series rises relative to similar non-SUP goods once producer charges start to bite. Windowed DiD summaries for six and twelve months are positive and meaningful. Because COVID-19 drove broad inflation, this contrast relies on controls that are not direct substitutes.

Table 2: Austria: Treated vs. Control (Event-Study Coefficients)

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Treated | | | | Control | | | |
| Event Bin | Est. | SE | t | p | Est. | SE | t | p |
| -24 | -25.75∗∗ | 7.12 | -3.62 | 0.01 | -18.94 | 5.13 | -3.69 | 0.17 |
| -21 | -21.80∗∗ | 6.06 | -3.60 | 0.01 | -11.04 | 1.91 | -5.79 | 0.11 |
| -18 | -22.71∗∗ | 6.52 | -3.48 | 0.01 | -11.61∗∗ | 0.12 | -98.64 | 0.01 |
| -15 | -19.33∗ | 6.48 | -2.98 | 0.02 | -12.03∗∗ | 0.11 | -106.31 | 0.01 |
| -12 | -22.26∗∗ | 6.84 | -3.25 | 0.01 | -11.15 | 1.77 | -6.29 | 0.10 |
| -9 | -21.53∗∗ | 6.13 | -3.51 | 0.01 | -8.70 | 2.39 | -3.64 | 0.17 |
| -6 | -14.49 | 9.22 | -1.57 | 0.15 | -9.39∗ | 0.36 | -26.01 | 0.02 |
| -3 | -4.80 | 5.80 | -0.83 | 0.43 | -4.61 | 1.11 | -4.16 | 0.15 |
| 3 | -5.04. | 2.35 | -2.15 | 0.06 | 0.43 | 0.32 | 1.33 | 0.41 |
| 6 | -3.46 | 3.09 | -1.12 | 0.29 | 2.01 | 3.84 | 0.52 | 0.69 |
| 9 | -2.20 | 2.85 | -0.77 | 0.46 | 5.29 | 1.72 | 3.08 | 0.20 |
| 12 | -1.47 | 3.86 | -0.38 | 0.71 | 11.62 | 3.67 | 3.16 | 0.19 |
| 15 | -1.52 | 2.85 | -0.53 | 0.61 | 9.41. | 1.39 | 6.77 | 0.09 |
| 18 | 3.01 | 7.43 | 0.41 | 0.69 | 9.88. | 0.99 | 9.99 | 0.06 |
| 21 | 2.61 | 6.78 | 0.38 | 0.71 | 10.33 | 1.79 | 5.78 | 0.11 |
| 24 | -0.72 | 3.66 | -0.20 | 0.85 | 10.54. | 1.48 | 7.11 | 0.09 |
| 27 | 3.45 | 5.03 | 0.69 | 0.51 | 10.78 | 1.99 | 5.42 | 0.12 |
| 30 | 4.57∗∗∗ | 0.88 | 5.22 | 0.00 | 11.38 | 2.68 | 4.24 | 0.15 |
| 33 | 6.73 | 8.21 | 0.82 | 0.43 | 9.50∗ | 0.71 | 13.31 | 0.05 |
| Observations | 1,781 | | | | 765 | | | |
| RMSE | 18.40 | | | | 5.02 | | | |
| Adj. R2 | 0.57 | | | | 0.90 | | | |
| Within R2 | 0.14 | | | | 0.71 | | | |

* •

  OLS with product and retailer fixed effects. SEs clustered by product and retailer. Significance: ∗∗∗ p<.01p{<}.01, ∗∗ p<.05p{<}.05, ∗ p<.10p{<}.10, . p<.15p{<}.15.

### 4.4 Cross-Country Sample: SUP vs. Non-SUP

![Refer to caption](8608daae-ad1c-46e4-afc4-eb32c2dc501e.png)


Figure 4: Figure 4 — Cross-Country Sample (Austria and Germany): SUP vs. Non-SUP (event study, 3-month bins). Notes: event time relative to February 2022; fixed effects by product and retailer; two-way clustered standard errors. We emphasize non-direct-substitute controls to lessen COVID-19–related inflation confounding across countries.

The cross-country sample adds variation in timing and enforcement between Austria (2022) and Germany (2024). Short-run swings are larger and less precise. When all post bins are averaged, the contrast turns positive, and country splits point to Austria as the main driver.

## 5 Discussion and Policy Implications

Price signals show up when the charge is clear and Austria’s ARA Online and Germany’s DIVID improve monitoring (BMK,, [2024](https://arxiv.org/html/2510.15617v1#bib.bib3); UBA,, [2024](https://arxiv.org/html/2510.15617v1#bib.bib9)). The magnitudes align with theory and with other environmental charges where modest per-unit prices moved behavior, such as bag levies and deposit–refunds (Convery et al.,, [2007](https://arxiv.org/html/2510.15617v1#bib.bib5); Homonoff,, [2018](https://arxiv.org/html/2510.15617v1#bib.bib7); Walls,, [2011](https://arxiv.org/html/2510.15617v1#bib.bib10)).

Distributional incidence and substitution margins matter. Flat per-unit charges can be regressive if lower-income households consume more of the targeted items; complementary policies (reusable alternatives, information, or targeted vouchers) can ease burdens while preserving incentives (Fullerton and Metcalf,, [2001](https://arxiv.org/html/2510.15617v1#bib.bib12)).

On control groups during COVID-19. Because the pandemic pushed up prices broadly and re-shaped supply chains, proper control groups are vital. Controls that are not direct substitutes for treated SUP items are, in general, better in this setting because direct substitutes can be simultaneously affected by substitution away from treated goods and by shared shocks, risking bias in the contrasts.

#### Limitations.

We do not observe quantities, so we cannot trace welfare or litter outcomes directly. Future work can pair prices with volumes and municipality-level litter metrics to measure elasticities and environmental returns.

## 6 Conclusion

Producer charges aimed at SUPs show up in retail prices in Austria, both at the product level and in pooled samples. The full sample including Germany’s fund shows a slower and less precise signal in the short run, consistent with its design and timing. Our empirical approach uses two-way clustering for inference, with product and retailer fixed effects and 3-month event-time bins anchored at February 2022. A plausible suggestion for future research is to quantify changes in quantities, substitution to reusables and net environmental benefits.

## Statements and Declarations

Funding: None.

Conflicts of interest: The author declares no conflicts of interest.

Data and code availability: Aggregated tables and replication code will be made available upon request; raw price microdata are subject to platform licensing.

Ethical approval: Not applicable.

## References

* Angrist and Pischke, (2009)

  Angrist, J. D. and Pischke, J.-S. (2009).
  Mostly Harmless Econometrics: An Empiricist’s Companion.
  Princeton University Press, Princeton, NJ.
* Besley and Rosen, (1999)

  Besley, T. J. and Rosen, H. S. (1999).
  Sales taxes and prices: An empirical analysis.
  National Tax Journal, 52(2), 157–178.
  doi:10.1086/NTJ41789387.
* BMK, (2024)

  Bundesministerium für Klimaschutz (2024).
  Geschäftszeichen 2024-0.729.355.
* Cameron et al., (2011)

  Cameron, A. C., Gelbach, J. B., and Miller, D. L. (2011).
  Robust inference with multiway clustering.
  Journal of Business & Economic Statistics, 29(2), 238–249.
  doi:10.1198/jbes.2010.07136.
* Convery et al., (2007)

  Convery, F., McDonnell, S., and Ferreira, S. (2007).
  The most popular tax in Europe? Lessons from the Irish plastic bags levy.
  Environmental & Resource Economics, 38(1), 1–11.
  doi:10.1007/s10640-006-9059-2.
* EU, (2019)

  European Union (2019).
  Directive (EU) 2019/904 of the European Parliament and of the Council of 5 June 2019 on the reduction of the impact of certain plastic products on the environment.
  OJ L 155, 12.6.2019, 1–19.
* Homonoff, (2018)

  Homonoff, T. A. (2018).
  Can small incentives have large effects? The impact of taxes versus bonuses on disposable bag use.
  American Economic Journal: Economic Policy, 10(4), 177–210.
  doi:10.1257/pol.20150261.
* Marion and Muehlegger, (2011)

  Marion, J. and Muehlegger, E. (2011).
  Fuel tax incidence and supply conditions.
  Journal of Public Economics, 95(9–10), 1202–1212.
  doi:10.1016/j.jpubeco.2011.04.003.
* UBA, (2024)

  Umweltbundesamt (UBA) (2024).
  Onlineplattform DIVID des Einwegkunststofffonds gestartet (Pressemitteilung, 2. April 2024).
* Walls, (2011)

  Walls, M. (2011).
  Deposit–refund systems in practice and theory.
  Resources for the Future Discussion Paper 11-47, Washington, DC.
* Weyl and Fabinger, (2013)

  Weyl, E. G. and Fabinger, M. (2013).
  Pass-through as an economic tool: Principles of incidence under imperfect competition.
  Journal of Political Economy, 121(3), 528–583.
  doi:10.1086/670401.
* Fullerton and Metcalf, (2001)

  Fullerton, D. and Metcalf, G. E. (2001).
  Environmental controls, scarcity rents, and pre-existing distortions.
  Journal of Public Economics, 80(2), 249–267.
  doi:10.1016/S0047-2727(00)00087-6.

## Appendix A The data pipeline, sample, and control selection

### A.1 Notation and operators

We formalize the data pipeline with Codd’s relational algebra.
Selection: σ\sigma, projection: π\pi, rename: ρ\rho, (theta-)join: ⋈\bowtie, natural join: ⋈\bowtie, left outer join: denoted from now on as LOJ, grouping/aggregation: γ\gamma, attribute extension (add derived attributes): μ\mu. We write months and weeks as integers; the event anchor is February 2022, denoted m0=2022-02m\_{0}{=}\text{2022-02}.

#### Helper functions.

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | unix\_to\_week​(t​s),unix\_to\_month​(t​s),months\_between​(x,y),\displaystyle\texttt{unix\\_to\\_week}(ts),\quad\texttt{unix\\_to\\_month}(ts),\quad\texttt{months\\_between}(x,y), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | sup​(n​a​m​e): TRUE iff ​n​a​m​e​ILIKE​p​ for some pattern ​p∈𝒫.\displaystyle\texttt{sup}(name):\text{ TRUE iff }name\ \texttt{ILIKE}\ p\text{ for some pattern }p\in\mathcal{P}. |  |

#### Base relations (as abbreviated).

|  |  |  |
| --- | --- | --- |
|  | Prod​(prod\_id,n​a​m​e,b​o​r​n​\_​t​s,…)product metadataOff​(offer\_id,prod\_id,ret\_id,t​s,p​r​i​c​e,…)offers (high-frequency)Clk​(prod\_id,ret\_id,t​s,c​l​i​c​k​s,…)click logs (high-frequency)Ret​(ret\_id,r​e​t​\_​n​a​m​e,t​s,…)retailer attributes over time\begin{array}[]{ll}\textbf{Prod}(\textit{prod\\_id},\ name,\ born\\_ts,\ \ldots)&\text{product metadata}\\ \textbf{Off}(\textit{offer\\_id},\ \textit{prod\\_id},\ \textit{ret\\_id},\ ts,\ price,\ \ldots)&\text{offers (high-frequency)}\\ \textbf{Clk}(\textit{prod\\_id},\ \textit{ret\\_id},\ ts,\ clicks,\ \ldots)&\text{click logs (high-frequency)}\\ \textbf{Ret}(\textit{ret\\_id},\ ret\\_name,\ ts,\ \ldots)&\text{retailer attributes over time}\end{array} |  |

### A.2 Cohort and event window

Let T∗=1,577,836,800T^{\ast}{=}1{,}577{,}836{,}800 (Unix; 2020-01-01). Products born after T∗T^{\ast}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Prod+:=σborn\_ts>T∗​(Prod).\textbf{Prod}^{+}\;:=\;\sigma\_{\text{born\\_ts}>T^{\ast}}(\textbf{Prod}). |  | (2) |

Attach time variables to offers and clicks:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Offt\displaystyle\textbf{Off}^{t} | :=μweek=unix\_to\_week​(t​s),month=unix\_to\_month​(t​s),e=months\_between​(month,m0)​(Off),\displaystyle=\mu\_{\ \text{week}=\texttt{unix\\_to\\_week}(ts),\ \text{month}=\texttt{unix\\_to\\_month}(ts),\ \text{e}=\texttt{months\\_between}(\text{month},m\_{0})}(\textbf{Off}), |  | (3) |
|  | Clkt\displaystyle\textbf{Clk}^{t} | :=μweek=unix\_to\_week​(t​s),month=unix\_to\_month​(t​s),e=months\_between​(month,m0)​(Clk).\displaystyle=\mu\_{\ \text{week}=\texttt{unix\\_to\\_week}(ts),\ \text{month}=\texttt{unix\\_to\\_month}(ts),\ \text{e}=\texttt{months\\_between}(\text{month},m\_{0})}(\textbf{Clk}). |  |

Keep event months in [−24,36][-24,36] and cohort products:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Offw​i​n\displaystyle\textbf{Off}^{win} | :=σ−24≤e≤36​(Offt)⋈prod\_idπprod\_id​(Prod+),\displaystyle=\sigma\_{-24\leq\text{e}\leq 36}(\textbf{Off}^{t})\ \bowtie\_{\text{prod\\_id}}\ \pi\_{\text{prod\\_id}}(\textbf{Prod}^{+}), |  | (4) |
|  | Clkw​i​n\displaystyle\textbf{Clk}^{win} | :=σ−24≤e≤36​(Clkt)⋈prod\_idπprod\_id​(Prod+).\displaystyle=\sigma\_{-24\leq\text{e}\leq 36}(\textbf{Clk}^{t})\ \bowtie\_{\text{prod\\_id}}\ \pi\_{\text{prod\\_id}}(\textbf{Prod}^{+}). |  |

### A.3 Stable retailer snapshot (last observation)

Let t⋆​(ret\_id)t^{\star}(\text{ret\\_id}) be the last timestamp in Ret for a retailer:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Retm​a​x\displaystyle\textbf{Ret}^{max} | :=γret\_id​(max⁡(t​s)→t⋆)​(Ret),\displaystyle=\gamma\_{\text{ret\\_id}}\big(\max(ts)\rightarrow t^{\star}\big)(\textbf{Ret}), |  | (5) |
|  | Rets​n​a​p\displaystyle\textbf{Ret}^{snap} | :=πret\_id,r​e​t​\_​n​a​m​e,…​(Retm​a​x⋈Ret.r​e​t​\_​i​d=Retm​a​x.r​e​t​\_​i​d∧Ret.t​s=t⋆Ret).\displaystyle=\pi\_{\text{ret\\_id},\ ret\\_name,\ \ldots}\Big(\textbf{Ret}^{max}\ \bowtie\_{\textbf{Ret}.ret\\_id=\textbf{Ret}^{max}.ret\\_id\ \wedge\ \textbf{Ret}.ts=t^{\star}}\ \textbf{Ret}\Big). |  |

### A.4 Treatment and controls

Define the SUP predicate via the pattern set 𝒫\mathcal{P} in Tbl. [3](https://arxiv.org/html/2510.15617v1#A1.T3 "Table 3 ‣ A.4 Treatment and controls ‣ Appendix A The data pipeline, sample, and control selection ‣ Political Interventions to Reduce Single-Use Plastics (SUPs) and Price Effects: An Event Study for Austria and Germany").

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ProdS​U​P\displaystyle\textbf{Prod}^{SUP} | :=σsup​(n​a​m​e)​(Prod+),\displaystyle=\sigma\_{\texttt{sup}(name)}(\textbf{Prod}^{+}), |  | (6) |
|  | Prodn​o​n\displaystyle\textbf{Prod}^{non} | :=πprod\_id​(Prod+)−πprod\_id​(ProdS​U​P),\displaystyle=\pi\_{\text{prod\\_id}}(\textbf{Prod}^{+})\;-\;\pi\_{\text{prod\\_id}}(\textbf{Prod}^{SUP}), |  |
|  | Prods​t​r​i​c​t\displaystyle\textbf{Prod}^{strict} | :=σn​a​m​e​ILIKE%​graphics card%​(Prodn​o​n⋈Prod).\displaystyle=\sigma\_{\ name\ \texttt{ILIKE}\ \%\text{graphics card}\%}\big(\textbf{Prod}^{non}\ \bowtie\ \textbf{Prod}\big). |  |

Table 3: SUP keyword classes (examples of ILIKE patterns).

| Category | Example patterns |
| --- | --- |
| Beverage cups | %to-go becher%, %einwegbecher%, %kunststoffbecher%, |
|  | %getränkebecher% |
| Food containers | %takeaway box%, %kunststoffschale% |
| Films & wraps | %verpackungsfolie%, %plastikfolie% |
| Plastic carrier bags | %plastiktüte%, %einwegtragetasche% |
| Wet wipes | %feuchttuch%, %hygienetuch% |
| Balloons | %luftballon%, %partyballon%, %heliumballon% |

### A.5 Monthly aggregation and index

Aggregate to (i=prod\_id,j=ret\_id,t=month)(i{=}\text{prod\\_id},j{=}\text{ret\\_id},t{=}\text{month}):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Pbar | :=γprod\_id,ret\_id,month​(avg​(p​r​i​c​e)→p¯)​(Offw​i​n),\displaystyle=\gamma\_{\text{prod\\_id},\ \text{ret\\_id},\ \text{month}}\big(\mathrm{avg}(price)\rightarrow\overline{p}\big)(\textbf{Off}^{win}), |  | (7) |
|  | Csum | :=γprod\_id,ret\_id,month​(sum​(c​l​i​c​k​s)→c​l​k)​(Clkw​i​n).\displaystyle=\gamma\_{\text{prod\\_id},\ \text{ret\\_id},\ \text{month}}\big(\mathrm{sum}(clicks)\rightarrow clk\big)(\textbf{Clk}^{win}). |  |

Attach event bins (b:=⌊e/3⌋b{:=}\lfloor e/3\rfloor):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Pmon | :=μe=months\_between​(month,m0),b=⌊e/3⌋​(Pbar),\displaystyle=\mu\_{\ e=\texttt{months\\_between}(\text{month},m\_{0}),\ b=\lfloor e/3\rfloor}(\textbf{Pbar}), |  | (8) |
|  | Cmon | :=μe=months\_between​(month,m0),b=⌊e/3⌋​(Csum).\displaystyle=\mu\_{\ e=\texttt{months\\_between}(\text{month},m\_{0}),\ b=\lfloor e/3\rfloor}(\textbf{Csum}). |  |

Compute base prices at m0m\_{0} and form an index:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | BaseP | :=πprod\_id,ret\_id,p¯→p¯0​σmonth=m0​(Pmon),\displaystyle=\pi\_{\text{prod\\_id},\ \text{ret\\_id},\ \overline{p}\rightarrow\overline{p}\_{0}}\ \sigma\_{\text{month}=m\_{0}}(\textbf{Pmon}), |  | (9) |
|  | IndexAll | :=μP=100⋅p¯/p¯0​(Pmon​LOJ(prod\_id,ret\_id)​BaseP).\displaystyle=\mu\_{P=100\cdot\overline{p}/\overline{p}\_{0}}\Big(\textbf{Pmon}\ \text{LOJ}\_{(\text{prod\\_id},\text{ret\\_id})}\ \textbf{BaseP}\Big). |  |

### A.6 Data analysis sample splits

Join clicks and retailer snapshot:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ObsCore:=(IndexAll​LOJ(prod\_id,ret\_id,month)​Cmon)​LOJret\_id​Rets​n​a​p.\textbf{ObsCore}\;:=\;\big(\textbf{IndexAll}\ \text{LOJ}\_{(\text{prod\\_id},\text{ret\\_id},\text{month})}\ \textbf{Cmon}\big)\ \text{LOJ}\_{\text{ret\\_id}}\ \textbf{Ret}^{snap}. |  | (10) |

This is the analysis table (plastics\_regulation\_obs).

Define treated and control panels passed to estimation:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ObsT\displaystyle\textbf{Obs}^{T} | :=ObsCore⋈prod\_idπprod\_id​(ProdS​U​P),\displaystyle=\textbf{ObsCore}\ \bowtie\_{\text{prod\\_id}}\ \pi\_{\text{prod\\_id}}(\textbf{Prod}^{SUP}), |  | (11) |
|  | ObsC\displaystyle\textbf{Obs}^{C} | :=ObsCore⋈prod\_idπprod\_id​(Prodn​o​n),\displaystyle=\textbf{ObsCore}\ \bowtie\_{\text{prod\\_id}}\ \pi\_{\text{prod\\_id}}(\textbf{Prod}^{non}), |  |
|  | ObsS\displaystyle\textbf{Obs}^{S} | :=ObsCore⋈prod\_idπprod\_id​(Prods​t​r​i​c​t).\displaystyle=\textbf{ObsCore}\ \bowtie\_{\text{prod\\_id}}\ \pi\_{\text{prod\\_id}}(\textbf{Prod}^{strict}). |  |

Export the variables used in estimation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | πprod\_id,ret\_id,r​e​t​\_​n​a​m​e,month,e,b,P,log⁡P,c​l​k​(⋅).\pi\_{\ \text{prod\\_id},\ \text{ret\\_id},\ ret\\_name,\ \text{month},\ e,\ b,\ P,\ \log P,\ clk\ }(\cdot). |  | (12) |

### A.7 Estimation procedure

For each sample (treated or control), the regression estimated in R is

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yi​j​t∼∑b≠0𝟏​{bt=b}|FEi+FEj,clusters: ​(i,j),Y\_{ijt}\sim\sum\_{b\neq 0}\mathbf{1}\{b\_{t}=b\}\;\Big|\;\text{FE}\_{i}+\text{FE}\_{j},\quad\text{clusters: }(i,j), |  | (13) |

corresponding to fixest::feols( Y ~ i(event\_bin, ref=0) | prod\_id+ret\_name, cluster ~ prod\_id+ret\_name). We report figures for Y=PY=P (level index) with 90%90\% CIs and windowed DiD contrasts (6M, 12M, full post–pre) as linear combinations of bin coefficients.

### A.8 Timing and interpretation

Producer charges in Austria begin in 2022; Germany’s fund begins in 2024. Because P=100⋅p¯/p¯0P=100\cdot\overline{p}/\overline{p}\_{0} with base m0=m\_{0}{=}February 2022, bin coefficients βb\beta\_{b} are percentage-point deviations from that base month.