---
authors:
- Luka Draganić
- Leonarda Srdelić
- Marwil J. Davila-Fernandez
doc_id: arxiv:2511.02973v1
family_id: arxiv:2511.02973
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Extreme events and public debt dynamics: Lessons from Croatia’s experienceThe
  opinions expressed in this publication are those of the authors. We are grateful
  to Leonardo Martinez for his careful reading and suggestions for improvement. A
  special thanks goes to Daniele Tavani for insightful correspondence on earlier drafts
  of the article. The usual caveats apply.'
url_abs: http://arxiv.org/abs/2511.02973v1
url_html: https://arxiv.org/html/2511.02973v1
venue: arXiv q-fin
version: 1
year: 2025
---


Luka Draganić
*Institute of Public Finance, Croatia*

Leonarda Srdelić


Marwil J. Davila-Fernandez
*Colorado State University, United States*

(November 2025)

###### Abstract

Using Croatian data and the IMF’s Natural Disaster Debt Dynamic Tool, this paper assesses how public debt adjusts to extreme events in a small open economy. We compare debt paths under baseline and stress scenarios, the latter simulating a major earthquake in 2025. Croatia provides a unique setting for evaluating post-disaster recovery in countries recently incorporated into the European Union. Our benchmark projections, which assume moderate economic growth and a broadly neutral fiscal stance, suggest the debt-to-GDP ratio will gradually decline to below 55% by 2040. In contrast, in the disaster scenario, we document a sharp short-term increase and a persistent upward shift in the debt trajectory, reaching 75% of GDP. Deterministic and stochastic simulations allow us to assess the distribution of potential outcomes. It is shown that, in the absence of shocks, public debt is on a sustainable downward path, but a severe natural disaster could reverse this trend and keep it elevated for years. Our findings highlight the importance of fiscal buffers that are critical for creating space to absorb shocks. The paper innovates by integrating natural disaster stress-testing into public debt analysis, with implications for fiscal risk management and policy planning. While we focus on Croatia, the mechanisms we uncover have broader implications for small open economies exposed to extreme events.

Keywords: Public debt sustainability, Natural disasters, Fiscal risk, Stochastic simulations, Croatia.

JEL: J11; O41; O52.

## 1 Introduction

Public debt sustainability is a central concern for small open economies, especially those that have recently undergone significant fiscal adjustments. In this context, natural disasters pose substantial fiscal risks by suddenly widening deficits and adding to debt. Climate change is projected to increase the frequency and severity of weather- and climate-related hazards, thereby amplifying these fiscal risks [[49](https://arxiv.org/html/2511.02973v1#biba.bibx20)]. Ensuring that debt remains on a sustainable path requires not only sound economic growth and fiscal discipline in normal times but also resilience to rare but impactful events such as earthquakes, as well as to the growing risks of climate-induced natural disasters.

Empirical evidence on the macroeconomic impact of natural disasters remains mixed [[41](https://arxiv.org/html/2511.02973v1#biba.bibx12), [57](https://arxiv.org/html/2511.02973v1#biba.bibx28), [32](https://arxiv.org/html/2511.02973v1#biba.bibx3), [45](https://arxiv.org/html/2511.02973v1#biba.bibx16)]. Some studies identify adverse effects on output, while others point to heterogeneous outcomes depending on the type, severity, and context of the event. For instance, [[42](https://arxiv.org/html/2511.02973v1#biba.bibx13)] show that the GDP growth response differs across disaster types (droughts, floods, earthquakes, and storms), with developing countries generally experiencing stronger negative impacts than advanced economies. They also find that severe disasters have disproportionately larger effects than moderate ones, and that sectoral responses vary, with agriculture often more exposed. [[54](https://arxiv.org/html/2511.02973v1#biba.bibx25)] broadly confirms these findings. His analysis adds another layer by highlighting how country-specific characteristics, such as stronger institutions, higher literacy, greater fiscal capacity, and more robust financial buffers, significantly shape resilience.

Along similar lines, [[46](https://arxiv.org/html/2511.02973v1#biba.bibx17)] examine disaster impacts using a counterfactual GDP approach and highlights the roles of hazard, asset exposure, and vulnerability. Their medium-term time horizon, up to five years post-disaster, shows that while average impacts may appear modest, they intensify with larger shocks. More recently, [[36](https://arxiv.org/html/2511.02973v1#biba.bibx7)] adopt a structural quantile VAR framework to assess how climate-related natural disasters affect the entire predictive distribution of output growth and inflation. They find that disasters significantly shift forecast distributions, with a sharp increase in downside risks to growth and upside risks to inflation, effects that persist through higher conditional volatility and skewness. By contrast, using a synthetic control methodology, [[34](https://arxiv.org/html/2511.02973v1#biba.bibx5)] argue that even extremely large disasters do not systematically reduce long-term economic growth once political shocks are separated from natural ones. Their results suggest that it is often the political aftermath, such as revolutions following disasters, rather than the disasters themselves, that drives persistent economic losses.

We provide new evidence on how natural disasters affect public debt sustainability in a small open economy. Drawing on Croatian data, we analyse the dynamic effects of an earthquake on the debt trajectory by using the International Monetary Fund’s (IMF) Natural Disaster Debt Dynamic Tool (ND-DDT) [[30](https://arxiv.org/html/2511.02973v1#biba.bibx1)]. After rapid public debt accumulation during the global financial crisis and the prolonged recession that followed, Croatia stabilised and reduced its debt in the late 2010s.111Following its separation from the former Yugoslavia, Croatia undertook a series of reforms to foster private-sector growth and attract foreign investment. The country joined the World Trade Organisation (WTO) in 2000, the Central European Free Trade Agreement (CEFTA) in 2003, and the European Union (EU) in 2013. As the last country to join the union, its experience is particularly relevant to understanding possible development alternatives for the region. However, the twin shocks of the COVID-19 pandemic and a devastating earthquake in 2020 highlighted the vulnerability of public finances to large exogenous shocks. We construct a baseline scenario that reflects expected economic conditions and policies, alongside a stress scenario in which an earthquake strikes in 2025. The latter is calibrated using historical evidence on disaster impacts, drawing in particular on the 2020 Zagreb earthquake as documented in the Emergency Events Database (EM-DAT), to derive plausible shocks to GDP and government finances. To ensure robustness, the stress tests are simulated using four complementary methods.

First, we apply shocks only in the initial period. These shocks are calibrated to the 1st percentile of the historical distribution to capture extreme tail risk and assess the system’s resilience to a one-off severe event. Second, we model repeated shocks over the entire projection horizon. Here, the shocks are calibrated to the 5th percentile rather than the 1st. This avoids the implausible assumption of an extreme disaster hitting every year, while still imposing sufficient severity to test fiscal vulnerability. Third, we estimate dynamic responses of macro-fiscal variables via local projections [[50](https://arxiv.org/html/2511.02973v1#biba.bibx21)]. For GDP, we rely on impulse responses with 95% confidence intervals, reflecting the need for robust inference on a key macroeconomic variable. For the primary balance, we use point estimates, as fiscal outcomes are more volatile and subject to discretionary policy changes. Finally, we employ quantile regressions to capture heterogeneous effects across the distribution of outcomes. In this case, we focus on the median quantile, which highlights the typical or average response of the economy. This contrasts with the more extreme tail scenarios from the previous approaches, and ensures that the analysis also incorporates central tendencies rather than only worst-case outcomes.

In addition, we employ a probabilistic simulation in the form of a fan chart to capture the uncertainty surrounding debt outcomes. Following the approach of [[35](https://arxiv.org/html/2511.02973v1#biba.bibx6)], debt projection fan charts are generated through Monte Carlo simulations, which incorporate stochastic shocks to key macroeconomic and fiscal variables. By integrating these elements, our study offers a comprehensive risk analysis of public debt under both typical conditions and extreme shocks. The results indicate that an earthquake shock would place Croatia’s debt ratio on a significantly higher and more persistent trajectory compared to the baseline, highlighting the critical role of fiscal buffers and resilience policies in safeguarding debt sustainability.

Our contribution to the literature is twofold. We provide an in-depth case study of public debt dynamics in a small open economy like Croatia, incorporating the often-neglected risk of natural disasters into debt sustainability assessments. While previous studies have examined Croatia’s fiscal consolidation and debt trends, our analysis explicitly quantifies how a disaster scenario would alter the debt path and key indicators, including the risk of breaching the EU’s 60% of GDP Maastricht threshold. Moreover, the paper highlights the crucial role of fiscal buffers and pre-disaster fiscal space in mitigating the long-term impact of shocks. By doing so, it aligns with and extends broader findings that countries with stronger initial fiscal positions are better able to absorb disaster costs without jeopardising growth.

The remainder of the paper is structured as follows. Section 2 provides background on Croatia’s public debt trends and its exposure to natural disasters. Section 3 outlines the methodology, including the debt dynamics model and data sources. Section 4 presents the results under the baseline and disaster scenarios, as well as a stochastic risk analysis. Section 5 concludes with key findings, policy implications for fiscal sustainability, and suggestions for future research.

## 2 Background

### 2.1 Trends and structure of Croatia’s public debt

The dynamics of Croatia’s general government debt between 2000 and 2024 can be divided into several distinct phases, reflecting macroeconomic conditions, fiscal policy measures, and institutional changes (for an overview of the growth performance in this country and its relationship with international trade, see Srdelic & Davila-Fernandez, \citeyearSrdelicDavila24). In nominal terms, debt increased from €8.5 billion in 2000 to €49.3 billion in 2024. The central government accounted for the predominant share throughout the period, rising from €8.1 billion to €48.3 billion. Local government debt grew gradually, from €0.22 billion to €1.15 billion, while the debt of social security funds ceased after 2004. Government guarantees fluctuated more markedly, reaching close to €2 billion in the mid-2000s before declining to below €1 billion in later years. Fig. [1](https://arxiv.org/html/2511.02973v1#S2.F1 "Figure 1 ‣ 2.1 Trends and structure of Croatia’s public debt ‣ 2 Background ‣ Extreme events and public debt dynamics: Lessons from Croatia’s experienceThe opinions expressed in this publication are those of the authors. We are grateful to Leonardo Martinez for his careful reading and suggestions for improvement. A special thanks goes to Daniele Tavani for insightful correspondence on earlier drafts of the article. The usual caveats apply."), panel (a), reports the main trends.

Figure 1: Overview of general government debt dynamics, composition and risks, 2000–2024.

a) Trajectories of public debt in billion euros and % of GDP

![Refer to caption](graphics/Picture2.png)

b) General gov. deficit, debt change, and SFA

![Refer to caption](graphics/Picture8.png)

Sources: Eurostat, Croatian National Bank.

In relation to GDP, the debt ratio was stable at around 35–40% in the pre-crisis years, between 2000-2008, supported by steady growth and moderate deficits. The global financial crisis and subsequent recession in 2009 marked a turning point. A sharp fall in GDP, coupled with declining revenues and countercyclical spending, led to a rapid increase in the debt ratio to 48% of GDP. This upward trend continued in the following years, with the ratio reaching 57% in 2010, 63% in 2011, 69% in 2012, and 79% in 2014. The peak was recorded in 2015–2016, at 83% of GDP.

The introduction of the Excessive Deficit Procedure (EDP) in 2014 initiated a period of fiscal consolidation. From 2015 onwards, primary balances turned positive, expenditure control was reinforced, and revenues strengthened. Between 2016 and 2019, fiscal adjustment was supported by both restraint on the expenditure side and robust tax receipts, reflecting cyclical recovery as well as policy efforts to improve revenue performance. As a result, the debt ratio declined to 71% of GDP by 2019. Empirical analysis such as [[40](https://arxiv.org/html/2511.02973v1#biba.bibx11)] indicate that fiscal consolidation under the EDP delivered measurable improvements in fiscal outcomes, although the measures were assessed as less favourable to growth compared with alternative policy scenarios.

The COVID-19 pandemic in 2020 reversed these gains. The deficit widened substantially due to emergency fiscal support and a contraction in economic activity. The impact was more severe in Croatia, given its strong dependence on value-added tax, which accounts for more than half of total tax revenues. Lockdowns significantly reduced consumption and, thereby, VAT revenues. In addition, two major 2020 earthquakes, one in Zagreb in March and the other in Petrinja in December, created additional fiscal pressures, requiring large-scale public expenditure on emergency relief and reconstruction. Together with precautionary borrowing in an environment of heightened uncertainty, these factors raised the debt ratio to 86% of GDP. From 2021 onwards, public debt resumed a downward trajectory, supported by economic recovery, stronger fiscal revenues, and the effect of inflation on nominal GDP. The ratio declined to 78% in 2021, 69% in 2022, 62% in 2023, and 58% in 2024, thereby returning below the Maastricht reference value of 60%.

An important technical aspect of public debt dynamics is the divergence between the annual deficit and the change in debt. In principle, the government deficit in a given year should correspond to an equivalent increase in debt, while a surplus should reduce debt. In practice, however, debt developments are also shaped by operations outside the annual budget balance. This difference is captured by the Stock–Flow Adjustment (SFA), which records transactions and accounting operations that affect the debt stock without being part of the reported deficit [[43](https://arxiv.org/html/2511.02973v1#biba.bibx14)]. Typical examples include the assumption of state-owned enterprise debt, the provision of loans to public entities, or the government’s net acquisition of financial assets. Valuation changes and debt reclassifications are also included, while in the past, exchange rate movements influenced the value of foreign-currency-denominated debt. This has changed in 2023, as Croatia’s public debt is now entirely denominated in euros.

Croatia’s experience illustrates the relevance of these adjustments. In 2010 and especially in 2013, the debt ratio increased by significantly more than the deficit, reflecting sizeable SFA of 2.1% and 5.5% of GDP respectively (see panel b). These were related to balance-sheet operations and financial transactions not captured in the fiscal balance. Conversely, during the consolidation years 2014–2016, negative SFA contributed to a faster reduction in debt than implied by the headline deficit. The pandemic shock in 2020 again highlighted this mechanism: while the deficit amounted to 7.2% of GDP, the debt ratio rose by 9.8%, with SFA contributing 2.6% of GDP due to precautionary borrowing and other debt-increasing operations. More recently, in 2024, the situation was reversed: despite a deficit of 2.4% of GDP, the debt ratio rose by only 1.2%, as negative SFA of –1.2% reduced debt accumulation. Such trajectories are reported in Fig. [1](https://arxiv.org/html/2511.02973v1#S2.F1 "Figure 1 ‣ 2.1 Trends and structure of Croatia’s public debt ‣ 2 Background ‣ Extreme events and public debt dynamics: Lessons from Croatia’s experienceThe opinions expressed in this publication are those of the authors. We are grateful to Leonardo Martinez for his careful reading and suggestions for improvement. A special thanks goes to Daniele Tavani for insightful correspondence on earlier drafts of the article. The usual caveats apply."), panel (b).

Taken together, these results show that debt dynamics cannot be explained solely by the fiscal balance. Stock–flow adjustments, including financial transactions, reclassifications and other balance-sheet operations, have at times played a decisive role in shaping the debt trajectory. For this reason, a comprehensive assessment of debt developments requires attention to both the structure and the sources of change, not only the observed trends. This perspective is particularly important for positioning and for the debt projections presented in the next part of the paper.

The structure of Croatia’s central government debt is dominated by long-term instruments, particularly long-term securities, which increased from €5.3 billion in 2000 to more than €32 billion in 2024, see Fig. [2](https://arxiv.org/html/2511.02973v1#S2.F2 "Figure 2 ‣ 2.1 Trends and structure of Croatia’s public debt ‣ 2 Background ‣ Extreme events and public debt dynamics: Lessons from Croatia’s experienceThe opinions expressed in this publication are those of the authors. We are grateful to Leonardo Martinez for his careful reading and suggestions for improvement. A special thanks goes to Daniele Tavani for insightful correspondence on earlier drafts of the article. The usual caveats apply."), panel (a). This reflects a clear policy orientation towards extending maturities and reducing refinancing risk. Long-term loans remain an important component, although their relative weight has declined as reliance on securities expanded. By contrast, short-term instruments—both securities and loans—play a minor and more variable role, serving primarily for liquidity management. Cash and deposits are negligible throughout the period. Overall, this evolution reflects a deliberate shift towards greater stability through long-term market financing, in line with prudent debt management practices.

Figure 2: Structure and risk profile of the public debt portfolio, 2000–2024.

a) Structure by financial instrument

![Refer to caption](graphics/Picture3.png)

b) Fixed vs. variable rate debt

![Refer to caption](graphics/Picture5.png)

c) Foreign debt

![Refer to caption](graphics/Picture7.png)

d) Structure of public debt by creditor residency

![Refer to caption](graphics/Picture4.png)

e) Domestic debt by instrument

![Refer to caption](graphics/Picture6.png)

Sources: Eurostat, Ministry of Finance, Croatian Bureau of Statistics, Croatian National Bank.

A further important aspect of the debt structure is interest rate exposure. Croatia has substantially reduced its vulnerability to interest rate risk by shifting from variable- to fixed-rate borrowing, see Fig. [2](https://arxiv.org/html/2511.02973v1#S2.F2 "Figure 2 ‣ 2.1 Trends and structure of Croatia’s public debt ‣ 2 Background ‣ Extreme events and public debt dynamics: Lessons from Croatia’s experienceThe opinions expressed in this publication are those of the authors. We are grateful to Leonardo Martinez for his careful reading and suggestions for improvement. A special thanks goes to Daniele Tavani for insightful correspondence on earlier drafts of the article. The usual caveats apply."), panel (b). Between 2013 and 2023, the share of fixed-rate debt increased from 80.6% to 94.6%, while variable-rate debt declined from 19.4% to just 5.4%. This active debt management strategy has enhanced the predictability of debt servicing costs and provided protection in periods of rising euro area interest rates. With most of the portfolio locked in at fixed coupons, the fiscal impact of recent increases in market yields has remained contained.

The domestic and external composition of debt has also changed significantly. On the domestic side, central government debt is increasingly concentrated in long-term securities, which rose from €1.9 billion in 2000 to nearly €24.9 billion in 2024, as indicated in Fig. [2](https://arxiv.org/html/2511.02973v1#S2.F2 "Figure 2 ‣ 2.1 Trends and structure of Croatia’s public debt ‣ 2 Background ‣ Extreme events and public debt dynamics: Lessons from Croatia’s experienceThe opinions expressed in this publication are those of the authors. We are grateful to Leonardo Martinez for his careful reading and suggestions for improvement. A special thanks goes to Daniele Tavani for insightful correspondence on earlier drafts of the article. The usual caveats apply."), panel (c). Long-term loans remain secondary but stable, while short-term instruments are used flexibly for liquidity purposes. On the external side, debt consists mainly of securities and loans, see Fig. [2](https://arxiv.org/html/2511.02973v1#S2.F2 "Figure 2 ‣ 2.1 Trends and structure of Croatia’s public debt ‣ 2 Background ‣ Extreme events and public debt dynamics: Lessons from Croatia’s experienceThe opinions expressed in this publication are those of the authors. We are grateful to Leonardo Martinez for his careful reading and suggestions for improvement. A special thanks goes to Daniele Tavani for insightful correspondence on earlier drafts of the article. The usual caveats apply."), panel (d). Securities rose from €3.4 billion in 2000 to a peak above €9 billion in 2015, before stabilising around €7.4 billion in 2024. Loans increased steadily, from €2 billion in 2000 to €7.4 billion in 2024. This mix illustrates a balanced approach between market issuance and borrowing from international lenders, providing flexibility and diversification of financing sources. Finally, the creditor base has shifted markedly over time. In the early 2000s, foreign creditors held the majority of Croatia’s public debt. By 2024, however, domestic investors had become predominant, reflecting greater issuance on the local market and a strategic reduction in external exposure. Fig. [2](https://arxiv.org/html/2511.02973v1#S2.F2 "Figure 2 ‣ 2.1 Trends and structure of Croatia’s public debt ‣ 2 Background ‣ Extreme events and public debt dynamics: Lessons from Croatia’s experienceThe opinions expressed in this publication are those of the authors. We are grateful to Leonardo Martinez for his careful reading and suggestions for improvement. A special thanks goes to Daniele Tavani for insightful correspondence on earlier drafts of the article. The usual caveats apply."), panel (e) reports this transformation. This shift has strengthened financial stability by lowering vulnerability to exchange rate movements and rollover pressures, and by anchoring debt sustainability more firmly in domestic financial markets.

### 2.2 Natural disasters

Although Croatia is not among the most disaster-prone countries globally, it has experienced several significant natural disasters in recent decades. Table 1 summarises major disaster events that had measurable economic and human impacts. The most severe were the two earthquakes in 2020. The Zagreb earthquake in March 2020 caused damage estimated at around 11.7% of GDP and directly affected roughly 2% of the population. Nine months later, the December 2020 Petrinja earthquake caused damage equivalent to about 10.7% of GDP, affecting nearly 3.7% of the population. These events were unprecedented in Croatia’s recent history in terms of scale. Other disasters include floods, storms, droughts and extreme temperatures. For instance, a major storm in the Zadar region in 2017 caused damage equal to 0.3% of GDP, while an extreme heat wave in 2000 is estimated to have cost about 1.1% of GDP. Floods such as those of 2010 and 2014, as well as periodic droughts, have had more modest nationwide effects, though locally they can be very destructive. An example is the 2014 river flooding in eastern Croatia that inundated large areas of Vukovar–Srijem county. These figures suggest that natural disasters, while infrequent, can impose a heavy toll on the economy and public finances. The government often must increase spending for emergency response and reconstruction while economic disruptions reduce tax revenues. This combination poses a threat to fiscal stability.

Crucially, Croatia’s experience in 2020 showed that a major disaster can occur concurrently with other crises, in this case, the COVID-19 emergency, amplifying fiscal stress. This underlines why incorporating disaster scenarios into fiscal planning is important. In the analysis that follows, the 2020 earthquakes serve as a reference point for the “worst-case” shock magnitude applied in our stress tests. As detailed below, we calibrate a scenario to mirror the fiscal and macroeconomic fallout of a disaster comparable to those earthquakes, and examine the implications for the public debt path.

Table 1: Disasters in Croatia with measurable GDP and population impact.

| Year | Disaster Type | Location | Damage to GDP (%) | Affected Population (%) |
| --- | --- | --- | --- | --- |
| 2020 | Earthquake | Zagreb | 11.69 | 1.95 |
| 2020 | Earthquake | Sisak, Petrinja, Glina, Hrvatska Kostajnica, Zagreb county, Karlovac county | 10.70 | 3.69 |
| 2017 | Storm | Zadar region, Bibinje, Sukošan, Biograd na Moru, Nin | 0.29 | 0.08 |
| 2000 | Extreme temperature | Zagreb, Split, Osijek, Rijeka | 1.08 | 0.01 |
| 2010 | Flood | Slavonski Brod, Vinkovci | 0.14 | 0.01 |
| 2014 | Flood | Vukovar-Srijem County | 0.00 | 0.17 |
| 2023 | Storm | Brod-Posavina and Vukovar-Srijem Counties; Vinkovci | 0.00 | 0.16 |
| 2003 | Drought | Nationwide (20 counties) | 0.94 | – |
| 2005 | Wildfire | Dubrovnik-Neretva, Lika-Senj | 0.06 | – |

Source: EM-DAT, The International Disaster Database (2024).

## 3 Methodology

This study employs a debt-dynamics framework based on the IMF’s Natural Disaster Debt Dynamic Tool (ND-DDT) approach [[30](https://arxiv.org/html/2511.02973v1#biba.bibx1)]. The ND-DDT framework evaluates a country’s capacity to service debt under a baseline scenario and alternative stress scenarios. It projects the trajectory of the public debt-to-GDP ratio using projections of key macro-fiscal variables and policy targets. In our application to Croatia, we construct two scenarios: (a) a baseline scenario reflecting expected macroeconomic conditions and current policies, and (b) a natural-disaster shock scenario to assess how a severe adverse event would alter debt dynamics. The disaster scenario combines four complementary approaches, two stochastic and two econometric.

The stochastic component of the analysis consists of two configurations. The first, known as the distribution for period tt, introduces a one-off shock applied only in the initial year, capturing the immediate macro-fiscal effects of a single severe event. The second configuration, the distribution for each period, allows shocks to occur stochastically in every projection year, with their magnitudes drawn from the empirical distribution of historical disaster impacts. Both configurations are calibrated at the 5th percentile, corresponding to the lower tail of the distribution of macro-fiscal effects, which represents the worst 5% of observed disaster outcomes. This calibration ensures that the simulated earthquake scenario reflects a rare but plausible tail-risk event. Together, the two stochastic setups simulate how disaster-induced shocks to real GDP growth and the primary balance propagate through debt dynamics, providing a probabilistic assessment of fiscal vulnerability under extreme conditions.

The econometric component extends this framework to capture structural and cross-country dimensions of disaster impacts. Two methods are employed for this purpose. The first is the local projection approach of [[50](https://arxiv.org/html/2511.02973v1#biba.bibx21)], which estimates the dynamic, multi-period response of macro-fiscal variables to a disaster shock calibrated at the 95th percentile. This upper-tail calibration represents extreme but empirically observed adverse events, while the inclusion of an interaction term with the adaptive capacity index allows the model to quantify how institutional and economic resilience moderate the post-disaster adjustment. The second method, quantile regression [[51](https://arxiv.org/html/2511.02973v1#biba.bibx22)], captures heterogeneous effects of disasters across the conditional distribution of outcomes. By focusing on upper quantiles (τ=0.95\tau=0.95), this approach identifies how severe shocks affect countries in high-debt or high-vulnerability states, complementing the average responses estimated by local projections.

### 3.1 Baseline debt dynamics

The evolution of the debt-to-GDP ratio dtd\_{t} is governed by the standard debt accounting equation [[47](https://arxiv.org/html/2511.02973v1#biba.bibx18), [31](https://arxiv.org/html/2511.02973v1#biba.bibx2)]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​dt=dt−dt−1=it−(1+gt)​(πt)(1+gt)​(1+πt)​dt−1−gt(1+gt)​(1+πt)​dt−1−p​bt+o​ft,\Delta d\_{t}=d\_{t}-d\_{t-1}=\frac{i\_{t}-(1+g\_{t})(\pi\_{t})}{(1+g\_{t})(1+\pi\_{t})}d\_{t-1}-\frac{g\_{t}}{(1+g\_{t})(1+\pi\_{t})}d\_{t-1}-pb\_{t}+of\_{t}, |  | (1) |

where iti\_{t} is the average nominal interest rate on debt, gtg\_{t} is real GDP growth, πt\pi\_{t} is the GDP deflator inflation rate, p​btpb\_{t} is the primary budget balance, o​ftof\_{t} represents other debt-creating flows such as stock-flow adjustments or statistical discrepancies, and Δ\Delta is the difference operator. Notice that p​bt>0pb\_{t}>0 denotes a surplus while p​bt<0pb\_{t}<0 denotes a deficit. Since Croatia has no public debt denominated in a currency other than the euro, exchange-rate terms do not appear in the equation. Equation ([1](https://arxiv.org/html/2511.02973v1#S3.E1 "In 3.1 Baseline debt dynamics ‣ 3 Methodology ‣ Extreme events and public debt dynamics: Lessons from Croatia’s experienceThe opinions expressed in this publication are those of the authors. We are grateful to Leonardo Martinez for his careful reading and suggestions for improvement. A special thanks goes to Daniele Tavani for insightful correspondence on earlier drafts of the article. The usual caveats apply.")) states that changes in the debt ratio are driven by four components: (a) interest payments on existing debt, (b) the dilution effect of real GDP growth and inflation, (c) the fiscal stance captured by the primary balance, and (d) other debt-creating flows. Together, these elements fully account for the factors determining public debt dynamics.

The baseline scenario for Croatia uses macro-fiscal projections from official and international sources. Real GDP growth, inflation, and interest rate assumptions are taken from the IMF’s World Economic Outlook and national forecasts, reflecting expectations of moderate growth and stable financing conditions. Fiscal projections (revenues, expenditures, and the primary balance) are based on Croatia’s medium-term fiscal plan and IMF assessments, assuming gradual fiscal consolidation. The baseline therefore represents a continuation of current policies under normal macroeconomic conditions.

### 3.2 Natural-disaster shock calibration

To assess the impact of a natural disaster, we introduce exogenous shocks that focus on two channels: economic growth (gtg\_{t}) and the primary balance (p​btpb\_{t}). The other variables are held at their baseline levels. In Appendix [A](https://arxiv.org/html/2511.02973v1#A1 "Appendix A Appendix ‣ Extreme events and public debt dynamics: Lessons from Croatia’s experienceThe opinions expressed in this publication are those of the authors. We are grateful to Leonardo Martinez for his careful reading and suggestions for improvement. A special thanks goes to Daniele Tavani for insightful correspondence on earlier drafts of the article. The usual caveats apply."), we explore the possibility of these shocks also affecting inflation and the interest rate. The magnitude and persistence of the shocks to gtg\_{t} and p​btpb\_{t} are calibrated using historical disaster data from EM-DAT and IMF vintage projections. The calibration is anchored to the 2020 Zagreb earthquake, which caused estimated economic damages of about 11.7% of GDP and affected approximately 2% of the population. This event provides a relevant benchmark for Croatia, combining substantial physical destruction with observable fiscal pressure in a euro-area context. The baseline fiscal position prior to the shock is set at –1.1 % of GDP, consistent with Croatia’s pre-disaster fiscal balance in the ND-DDT configuration. The adaptive capacity term (Ai,tA\_{i,t}) corresponds to the ND adaptive ability index (0.438), capturing the degree to which Croatia’s institutional and fiscal resilience mitigates the impact of natural disasters.

Formally, the disaster shock is implemented as an exogenous deviation from the baseline projections starting in 2026, affecting only the real activity and fiscal balance channels. Let shs\_{h} denote the deviation applied at horizon hh relative to the baseline projection. The shock-adjusted variables are thus expressed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | gt+h=gt+hbase+shg,p​bt+h=p​bt+hbase+shp​b,h=0,1,…,5.\begin{aligned} g\_{t+h}&=g^{\text{base}}\_{t+h}+s^{g}\_{h},\\ pb\_{t+h}&=pb^{\text{base}}\_{t+h}+s^{pb}\_{h},\end{aligned}\hskip 18.49988pth=0,1,\ldots,5. |  | (2) |

For illustration, the vectors below present the output under the distribution for period tt configuration. In this case, the model generates a sequence of shocks to real GDP growth and the primary balance corresponding to the 5th percentile of the empirical distribution of earthquake-related impacts:

|  |  |  |
| --- | --- | --- |
|  | 𝐬𝐡𝐠={−3.0,−12.5,−5.2,−2.2,−1.2,−0.2}𝐬𝐡𝐩𝐛={−2.5,−0.9,0.1,0.8,0.1,0.3},\mathbf{s\_{h}^{\,g}}=\{-3.0,-12.5,-5.2,-2.2,-1.2,-0.2\}\hskip 18.49988pt\mathbf{s\_{h}^{\,pb}}=\{-2.5,-0.9,0.1,0.8,0.1,0.3\}, |  |

where each element shis\_{h}^{i} for i={g,p​b}i=\{g,pb\} represents the annual deviation from the baseline in percentage points of GDP at horizon hh. These values describe the temporal propagation of the shock. An initial contraction in output and deterioration in the fiscal balance followed by a gradual recovery.

### 3.3 Stochastic configuration of shocks

In the stochastic ND-DDT simulations, two configurations are used. The first, distribution for period tt, applies a one-time shock:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​h​o​c​kt+h={sh,h=0,0,h>0,Shock\_{t+h}=\begin{cases}s\_{h},&h=0,\\ 0,&h>0,\end{cases} |  | (3) |

while the second, distribution for each period, allows for shocks in every projection year:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​h​o​c​kt+h∼F​(μ,σ2),∀h≥0,Shock\_{t+h}\sim F(\mu,\sigma^{2}),\qquad\forall h\geq 0, |  | (4) |

where F​(μ,σ2)F(\mu,\sigma^{2}) denotes the empirical distribution of disaster impacts. Both configurations are calibrated at the 5th percentile, corresponding to the lower tail of the empirical distribution of historical macro-fiscal effects. The 5th percentile captures the worst 5% of observed outcomes. They are rare but plausible events with significant macroeconomic and fiscal consequences. This tail calibration ensures that the earthquake scenario reflects a severe yet empirically grounded stress event.

### 3.4 Econometric analysis of disaster impacts

While the ND-DDT simulations provide a probabilistic range of debt outcomes under stochastic shocks, they do not explicitly capture structural heterogeneity across countries or the moderating role of adaptive capacity. To address this issue, we complement the stochastic simulations with econometric approaches that estimate the propagation of disaster shocks and their dependence on country-specific characteristics.

First, the local projection method [[50](https://arxiv.org/html/2511.02973v1#biba.bibx21)] is used to estimate the dynamic response of key macro-fiscal variables to a disaster shock:

|  |  |  |  |
| --- | --- | --- | --- |
|  | yi,t+h−yi,t−1=αi,h+βh​N​Di,t(95)+γh​(N​Di,t(95)×Ai,t)+δh′​Xi,t−1+εi,t+h,y\_{i,t+h}-y\_{i,t-1}=\alpha\_{i,h}+\beta\_{h}ND^{(95)}\_{i,t}+\gamma\_{h}\big(ND^{(95)}\_{i,t}\times A\_{i,t}\big)+\delta\_{h}^{\prime}X\_{i,t-1}+\varepsilon\_{i,t+h}, |  | (5) |

where N​Di,t(95)ND^{(95)}\_{i,t} represents a disaster shock in the 95th percentile of severity, Ai,tA\_{i,t} is an index of adaptive capacity, and Xi,t−1X\_{i,t-1} is a vector of lagged control variables. The coefficient αi,h\alpha\_{i,h} is the intercept, βh\beta\_{h} traces the impulse response of variable yy at horizon hh, γh\gamma\_{h} captures how the response is moderated by adaptive capacity, and δh′\delta\_{h}^{\prime} is the vector of coefficients associated with our control variables. Finally, εi,t+h\varepsilon\_{i,t+h} is the error term.

Second, quantile regression analysis [[51](https://arxiv.org/html/2511.02973v1#biba.bibx22)] is used to examine heterogeneous effects across the conditional distribution of outcomes:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Qτ​(yt∣Xt)=ατ+βτ​N​Dt(95)+γτ​(N​Dt(95)×At)+δτ′​Xt,Q\_{\tau}(y\_{t}\mid X\_{t})=\alpha\_{\tau}+\beta\_{\tau}ND^{(95)}\_{t}+\gamma\_{\tau}(ND^{(95)}\_{t}\times A\_{t})+\delta\_{\tau}^{\prime}X\_{t}, |  | (6) |

where Qτ​(yt∣Xt)Q\_{\tau}(y\_{t}\mid X\_{t}) denotes the τ\tau-th conditional quantile of the dependent variable. Estimation at upper quantiles (τ=0.95\tau=0.95) captures high-risk states such as periods of elevated debt or weak fiscal positions. Coefficients ατ\alpha\_{\tau}, βτ\beta\_{\tau}, γτ\gamma\_{\tau}, and δτ′\delta\_{\tau}^{\prime} have equivalent interpretation to our previous case.

Both econometric approaches use the 95th percentile, corresponding to the upper tail of the empirical distribution of disaster impacts. This reflects the most severe, yet empirically observed, adverse outcomes. The use of both distributional tails, the 5th percentile for stochastic ND-DDT simulations and the 95th percentile for econometric estimation, ensures that the framework systematically explores extreme but plausible shocks from both empirical and analytical perspectives.

### 3.5 Stochastic debt simulations

Finally, stochastic simulations evaluate the uncertainty around debt outcomes. The vector of shocks to key macro-fiscal variables Zt=(gt,it,πt,p​bt)Z\_{t}=(g\_{t},i\_{t},\pi\_{t},pb\_{t}) is drawn from a multivariate normal distribution:

|  |  |  |
| --- | --- | --- |
|  | Zt∼𝒩​(μ,Σ),Z\_{t}\sim\mathcal{N}(\mu,\Sigma), |  |

where μ\mu denotes historical means and Σ\Sigma the covariance matrix estimated from past data. Monte Carlo simulations (10,000 iterations) produce a fan chart of debt paths, illustrating the range of possible debt outcomes under macro-fiscal uncertainty and situating the disaster scenario within that probabilistic context.

### 3.6 Data

The analysis covers the period from 2015 to 2030, combining historical data (2015–2024) with projections (2025–2030). All debt indicators refer to the general government gross debt as a percentage of GDP. Historical debt figures are sourced from the Croatian National Bank (CNB) and Ministry of Finance official statistics, which are aligned with Eurostat definitions. GDP and fiscal data (e.g. real GDP growth, GDP deflator, budget balances) come from the CNB, the Croatian Bureau of Statistics, and the IMF’s databases.

Table 2 lists the key variables and their sources. The nominal effective interest rate on public debt is computed from Ministry of Finance data on government securities, using a weighted average of interest rates on outstanding debt instruments. All historical interest rates and debt figures in Croatian kuna have been converted to euros at the fixed exchange rate upon Croatia’s entry into the euro area in 2023. Real GDP growth rates are taken from CNB and Eurostat, while inflation (GDP deflator) is from the World Bank’s World Development Indicators. The primary balance (as % of GDP) uses IMF and Ministry of Finance data, and for future years, we incorporate targets from Croatia’s Medium-Term Fiscal Plan (extended to 2029).

For the other debt-creating flows, we utilise Eurostat’s reported SFA for past years. This includes items such as the net accumulation of financial assets, payments of called guarantees, or other transactions not in the deficit. In our projections, we assume that other debt-creating flows continue at roughly the average historical contribution. They are only a small positive addition to debt annually. This is a simplifying assumption given uncertainty about one-off operations. Essentially, we are assuming no major privatisations, no one-off debt reductions, and no large extra-budgetary borrowing beyond what recent trends suggest.

All projections from 2025 onward are conditioned on the macroeconomic assumptions of moderate growth and low interest rates. Real GDP is assumed to grow around 3–4% in 2024–2025 as the post-pandemic rebound continues, stabilising around 2.5% annually in the late 2020s. The medium-term GDP deflator inflation is projected to ease to around 2%, consistent with Eurozone price stability. Interest costs on debt are expected to rise gradually as global financial conditions normalise, but Croatia’s successful euro adoption and improved credit ratings help contain borrowing costs. The primary fiscal balance in the baseline is roughly in equilibrium, with small deficits of less than 1% of GDP in the mid-2020s, approaching 0 by 2028. These assumptions underpin the baseline scenario. Deviations from them under stress are outlined in the next section.

Table 2: List of Variables, Definitions, and Sources

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Variable | Description | Time Period | Unit of Measurement | Source |
| Historical data |  |  |  |  |
| dtd\_{t} | Stock of total gross public debt | 2015 - 2024 | % of GDP | CNB – General government debt |
| itdi^{d}\_{t} | Nominal effective interest rate on public debt | 2015 - 2024 | % | Ministry of Finance - Government bond issue data |
| πt\pi\_{t} | GDP deflator inflation | 2015 - 2024 | % | World Bank – World Development Indicators |
| gtg\_{t} | Real GDP growth | 2015 - 2024 | % | CNB – Main macroeconomic indicators |
| p​btpb\_{t} | Primary balance | 2015 - 2024 | % of GDP | IMF database |
| o​ftof\_{t} | Other net debt-creating flows | 2015 - 2024 | % of GDP | Eurostat SFA |
| Projection data |  |  |  |  |
| itdi^{d}\_{t} | Nominal effective interest rate on public debt | 2025 - 2029 | % | IMF database |
| πt\pi\_{t} | GDP deflator inflation | 2025 - 2029 | % | IMF database |
| gtg\_{t} | Real GDP growth | 2025 - 2029 | % | IMF database |
| p​btpb\_{t} | Primary balance | 2025 - 2028 | % of GDP | National Medium-term Fiscal Structural Plan for 2025-2028 |
| o​ftof\_{t} | Other net debt-creating flows | 2025 - 2028 | % of GDP | average of previous years |

## 4 Results

### 4.1 Baseline Debt Dynamics and Risk Analysis

Under the baseline scenario, Croatia’s public debt is on a gently declining trajectory. After peaking at around 87.7% of GDP in 2020, the debt ratio fell to about 63.0% by 2023, reflecting a robust post-pandemic economic rebound and fiscal consolidation. This downward trend is projected to continue, with debt dropping below the 60% Maastricht threshold in 2024 and reaching roughly 56% of GDP by 2030, as shown in Fig. [3](https://arxiv.org/html/2511.02973v1#S4.F3 "Figure 3 ‣ 4.1 Baseline Debt Dynamics and Risk Analysis ‣ 4 Results ‣ Extreme events and public debt dynamics: Lessons from Croatia’s experienceThe opinions expressed in this publication are those of the authors. We are grateful to Leonardo Martinez for his careful reading and suggestions for improvement. A special thanks goes to Daniele Tavani for insightful correspondence on earlier drafts of the article. The usual caveats apply.").

Figure 3: Croatia’s Public Sector Debt Dynamics, Baseline Scenario, 2024–2040

![Refer to caption](graphics/graphics_final/3_fan_chart.png)


Source: Authors’ calculation.

These favourable debt dynamics are driven mainly by sustained economic growth and relatively low effective interest rates, which together create a favourable interest-growth differential depicted in Fig. [4](https://arxiv.org/html/2511.02973v1#S4.F4 "Figure 4 ‣ 4.1 Baseline Debt Dynamics and Risk Analysis ‣ 4 Results ‣ Extreme events and public debt dynamics: Lessons from Croatia’s experienceThe opinions expressed in this publication are those of the authors. We are grateful to Leonardo Martinez for his careful reading and suggestions for improvement. A special thanks goes to Daniele Tavani for insightful correspondence on earlier drafts of the article. The usual caveats apply."). In the initial years of the projection, real GDP growth exceeds the real interest rate on public debt, allowing inflation and growth to gradually erode the debt ratio even in the absence of large primary surpluses. This outcome aligns with the [[39](https://arxiv.org/html/2511.02973v1#biba.bibx10)] Macroeconomic Developments and Outlook report, which notes that real GDP growth is expected to stay above 3% through 2026 while inflation falls to about 3.6% and interest rates remain modest. Such an environment enables economic growth to reduce the debt ratio even with a roughly neutral primary balance.

Figure 4: Individual Contributions to Public Debt, 2017–2031

![Refer to caption](graphics/graphics_final/4_DCF_baseline.png)


Source: Authors’ calculation.

On the fiscal side, the baseline assumes an approximately neutral primary balance over the medium term. After the pandemic-related deficits of 2020–2022, the primary balance is projected to remain close to zero from 2025 onward, with modest deficits of about 0.5–1% of GDP in the mid-2020s and a gradual convergence toward balance by the end of the decade. This trajectory implies that fiscal policy is not expected to generate substantial debt-reducing surpluses, but neither will it exert significant upward pressure on the debt ratio beyond those small deficits. Such expectation is consistent with the findings of [[44](https://arxiv.org/html/2511.02973v1#biba.bibx15)], who showed that Croatia’s debt-to-GDP ratio is closely linked to its primary balance position. Additionally, the projected primary deficits take into account anticipated increases in budget expenditures (for instance, higher defence-related costs noted in the Croatian National Bank’s, \citeyearCNBFinStab, Financial Stability Report).

Other debt-related flows outside the primary balance, such as stock-flow adjustments and off-budget transactions, add a small amount to debt each year on the order of 0.5–0.8% of GDP. These additional flows may slightly slow the pace of debt reduction in the baseline scenario, but they are not large enough to derail the overall downward trend. However, as illustrated by the fan chart in Fig. [3](https://arxiv.org/html/2511.02973v1#S4.F3 "Figure 3 ‣ 4.1 Baseline Debt Dynamics and Risk Analysis ‣ 4 Results ‣ Extreme events and public debt dynamics: Lessons from Croatia’s experienceThe opinions expressed in this publication are those of the authors. We are grateful to Leonardo Martinez for his careful reading and suggestions for improvement. A special thanks goes to Daniele Tavani for insightful correspondence on earlier drafts of the article. The usual caveats apply."), considerable uncertainty surrounds this baseline trajectory. Stochastic simulations generate a range of possible debt outcomes around the central forecast, highlighting the risks to debt dynamics. By 2030, Croatia’s debt-to-GDP ratio could plausibly end up well below or above the baseline projection, depending on how macroeconomic conditions evolve. In favourable scenarios (e.g. higher growth, lower interest rates, and no major shocks), debt could fall faster. The 10th-percentile outcome shows the debt ratio around 50% of GDP by 2030. Conversely, under adverse conditions, with low growth, rising borrowing costs, or other crises, the debt ratio could approach 70% by 2030. While the baseline forecasts debt in the mid-50s per cent of GDP, there is roughly a one-in-ten chance that by 2030 the debt ratio will be 10–15 percentage points lower than this (under very optimistic assumptions), and a one-in-ten chance it will be 10–15 points higher (on our severe downside scenario).

The fan chart shows that achieving the baseline debt reduction depends on avoiding major negative shocks. Still, several downside risks could materially alter the debt path. Key risk factors include (i) a possible recession, which would shrink GDP and thereby raise the debt ratio; (ii) surges in interest rates, increasing debt servicing costs; (iii) or financial-sector distress requiring public intervention, adding to the debt stock. Notably, even without any natural disaster, such macro-fiscal shocks could cause the debt trajectory to deviate upwards. For instance, if economic growth disappoints or new fiscal pressures emerge, the debt ratio could stagnate or even increase later in the decade, rather than fall as projected under the baseline. The baseline scenario unrealistically assumes no major surprises. Thus, maintaining debt on a downward course is not automatic.

### 4.2 Natural Disaster Scenario

To examine how a large shock could alter the debt trajectory, we now turn to a stress scenario in which a severe natural disaster strikes Croatia in early 2025. Because debt dynamics are reported on an annual basis, the effects of this shock first appear in the 2026 data. This scenario is calibrated to approximate the economic fallout of the 2020 earthquakes, serving as an illustrative “worst-case” event. Compared with the baseline, this shock produces a pronounced increase in the public debt-to-GDP ratio. The magnitude, timing, and persistence of the debt build-up vary substantially across different modelling approaches. While under the baseline scenario (no disaster), the public debt-to-GDP ratio would be about 55.4% by 2031, a one-off natural disaster shock raises the debt ratio to roughly 71.7% in 2031. If a similar shock were to occur every year, the debt ratio would climb to around 73.2% of GDP. Increases are more modest in our econometric estimates. The debt ratio in 2031 converges to 67.4% using the local projection approach and 67.2% under the quantile regression scenario, as indicated in Fig. [5](https://arxiv.org/html/2511.02973v1#S4.F5 "Figure 5 ‣ 4.2 Natural Disaster Scenario ‣ 4 Results ‣ Extreme events and public debt dynamics: Lessons from Croatia’s experienceThe opinions expressed in this publication are those of the authors. We are grateful to Leonardo Martinez for his careful reading and suggestions for improvement. A special thanks goes to Daniele Tavani for insightful correspondence on earlier drafts of the article. The usual caveats apply.").

Figure 5: Gross Nominal Public Debt in Alternative Scenarios

![Refer to caption](graphics/graphics_final/5_scenarios.png)


Source: Authors’ calculation. Econometric for pre-disaster fiscal balance –1.1 % of GDP, adaptive capacity = 0.44

In the one-off disaster shock scenario, the debt ratio rises sharply in the year of the event (2026), increasing by nearly eight percentage points of GDP relative to the baseline. The initial deterioration reflects a deep short-term recession and a surge in the fiscal deficit as public spending on reconstruction accelerates while revenues fall. Although partial recovery occurs in the following years, the debt ratio stabilises at a structurally higher level, remaining well above the baseline throughout the projection horizon. By 2031, the debt-to-GDP ratio converges to around 71.7 %, about 16 percentage points above the no-disaster path. In the repeated-shocks configuration, where similar shocks occur each year, the compounding of fiscal and output effects leads to a further increase in debt, reaching about 73.2 % of GDP by 2031, see Fig. [6](https://arxiv.org/html/2511.02973v1#S4.F6 "Figure 6 ‣ 4.2 Natural Disaster Scenario ‣ 4 Results ‣ Extreme events and public debt dynamics: Lessons from Croatia’s experienceThe opinions expressed in this publication are those of the authors. We are grateful to Leonardo Martinez for his careful reading and suggestions for improvement. A special thanks goes to Daniele Tavani for insightful correspondence on earlier drafts of the article. The usual caveats apply.").

Figure 6: Croatia Public Sector Debt Dynamics, 2026–2031

a) Distribution for period t 
  
![Refer to caption](graphics/graphics_final/6_DCF_distribution_for_period_t.png)

b) Distribution for each period 
  
![Refer to caption](graphics/graphics_final/6_DCF_each_period.png)

c) Local projection 
  
![Refer to caption](graphics/graphics_final/6_DCF_local.png)

d) Quantile projection 
  
![Refer to caption](graphics/graphics_final/6_DCF_quantile.png)

Source: Authors’ calculation.

For both scenarios, the primary deficit is the dominant driver of rising debt year after year. Fiscal shortfalls of a few per cent of GDP persist annually, consistently adding to the debt stock. Positive economic growth provides only a partial counterweight: while annual growth helps reduce the debt ratio, it is insufficient to fully offset the ongoing deficits. Consequently, the debt ratio ratchets upward over time. Real interest costs and other debt-creating flows are secondary factors: interest payments add only modestly to debt, and stock-flow adjustments contribute roughly 0.5% of GDP to the debt annually. The defining feature here is its cumulative persistence. Even by 2031, the debt ratio is still rising and has not stabilised. Thus, serial shocks (or equivalently, a prolonged period of expansionary fiscal policy) produce a larger overall increase in debt than a one-time shock, albeit through a slower, stepwise build-up. This indicates that sustained primary deficits can drive substantial debt accumulation, especially when economic growth is insufficient to outpace debt accumulation.

Scenarios based on econometric projections of shocks yield intermediate outcomes, characterised by delayed peaks and partial reversions. Under the local projection approach, the debt impact unfolds over two years. The debt ratio rises modestly in the initial shock year and then peaks in 2027 with an annual increase of about 4% of GDP. This pattern reflects a lagged effect in which the impacts of fiscal deterioration and other shocks fully materialise only after one year. Thereafter, mean reversion sets in. As the economy recovers and fiscal policy tightens, the annual changes in the debt ratio diminish and turn slightly negative by 2030–2031. Most of the earlier debt build-up is unwound by the end of the projection horizon. The 2027 peak is driven by a temporary worsening of the primary balance, coupled with an output rebound that year, which moderates (but does not fully offset) the fiscal deterioration. In subsequent years, improving primary balances and above-trend economic growth generate sustained debt reduction, bringing the debt trajectory back toward the baseline.

The quantile regression scenario, representing a median event, shows a smoother debt surge but still a partial correction only. The debt ratio jumps by nearly 5% of GDP in 2027, followed by an incomplete adjustment in subsequent years. Although economic growth bounces back strongly and provides sustained debt relief, persistent fiscal deficits prevent the debt ratio from fully returning to the baseline path. By 2031, the debt ratio remains elevated above the baseline, indicating that a severe shock can leave a lasting legacy. This outcome is consistent with historical evidence: for example, [[33](https://arxiv.org/html/2511.02973v1#biba.bibx4)] and [[53](https://arxiv.org/html/2511.02973v1#biba.bibx24)] find that disaster-related output losses are rarely fully offset by subsequent recoveries [[52](https://arxiv.org/html/2511.02973v1#biba.bibx23)], often leaving economies permanently smaller than their pre-shock trend. In line with that evidence, our model shows that while growth resumes after 2027 and helps to reduce debt, the adjustment is gradual. The shock’s effects leave the debt ratio stabilised at a higher plateau than before.

### 4.3 Improved adaptive capacity and pre-disaster fiscal position

Fig. [7](https://arxiv.org/html/2511.02973v1#S4.F7 "Figure 7 ‣ 4.3 Improved adaptive capacity and pre-disaster fiscal position ‣ 4 Results ‣ Extreme events and public debt dynamics: Lessons from Croatia’s experienceThe opinions expressed in this publication are those of the authors. We are grateful to Leonardo Martinez for his careful reading and suggestions for improvement. A special thanks goes to Daniele Tavani for insightful correspondence on earlier drafts of the article. The usual caveats apply.") presents the evolution of gross public debt for the natural disaster scenario using the local projection and quantile regression approaches. All simulations are calibrated to a 95th-percentile disaster shock, representing a severe but empirically observed adverse event. The distinction between the solid and dashed trajectories reflects differences in the assumed pre-disaster fiscal position and adaptive capacity. Solid lines assume an initial fiscal balance of −1.1%-1.1\% of GDP and an adaptive capacity index of 0.430.43, consistent with Croatia’s 2023 ND-GAIN data. Dashed red and blue lines assume a stronger fiscal position of +3%+3\% of GDP and higher adaptive capacity (AC = 0), representing a counterfactual setting in which fiscal buffers and institutional resilience are enhanced prior to the shock.

Figure 7: Gross Nominal Public Debt in Alternative Scenarios

![Refer to caption](graphics/graphics_final/7_scenarios.png)


Source: Authors’ calculation. Improved pre-disaster fiscal balance +3 % of GDP and adaptive capacity = 0.




Figure 8: Croatia Public Sector Debt Dynamics in Alternative Scenarios, 2026–2031

a) Local projection 
  
![Refer to caption](graphics/graphics_final/8_DCF_local.png)

b) Local projection with PB and AC improved 
  
![Refer to caption](graphics/graphics_final/8_DCF_local_pb_and_ac.png)

c) Quantile projection 
  
![Refer to caption](graphics/graphics_final/8_DCF_quantile.png)

d) Quantile projection with PB and AC improved 
  
![Refer to caption](graphics/graphics_final/8_DCF_quantile_pb_and_ac.png)

Source: Authors’ calculation.

In the local projection configuration, the model captures the gradual propagation of the disaster shock through time, reflecting the lagged nature of fiscal responses and post-disaster reconstruction. In the simplest format (solid red), it exhibits a pronounced and persistent increase in public debt, peaking around three years after the shock before stabilising. Under improved fiscal and adaptive conditions (dashed red), the increase in debt remains but is significantly attenuated, and the path flattens earlier. This indicates that fiscal surpluses and institutional resilience mitigate the amplitude and persistence of debt deterioration but do not fully offset the fiscal consequences of a severe natural disaster.

In the quantile regression configuration, which emphasises heterogeneity across the conditional distribution of outcomes (upper quantiles τ=0.95\tau=0.95), the solid blue trajectory shows a steep initial rise in debt immediately following the disaster, consistent with the dynamics of highly indebted or vulnerable states. When stronger fiscal and adaptive conditions are introduced (dashed blue), the debt ratio initially declines slightly before rising modestly and converging toward the baseline path. This short-term decline reflects the effect of fiscal buffers: a pre-disaster surplus enables partial absorption of the shock without immediate debt accumulation, while adaptive capacity supports faster recovery of output and revenues.

The differing shapes of the dashed trajectories stem from the underlying econometric mechanisms. The local projection model captures dynamic adjustment and persistence in the post-disaster fiscal path, whereas the quantile regression highlights cross-sectional asymmetries, showing that economies with greater fiscal and institutional resilience face smaller and shorter-lived debt increases, even under extreme shocks. Quantitatively, both improved configurations (dashed lines) reduce the post-shock peak of the debt ratio by approximately 3–4 percentage points relative to their respective baselines and shorten the return to a stabilising trajectory by about two years.

Overall, these results highlight the role of fiscal space and adaptive capacity in moderating post-disaster debt dynamics. A higher pre-disaster primary surplus and stronger institutional resilience substantially reduce the magnitude and persistence of debt accumulation following a 95th-percentile event. From a policy standpoint, this stresses the importance of maintaining fiscal buffers and investing in adaptive capacity as integral components of disaster-risk management and debt sustainability strategies.

Across all of these scenarios, two broad conclusions emerge. First, fiscal balances are the main determinant of debt dynamics. In every stress case, the primary deficit is the single largest contributor to rising debt, especially in crisis years when deficits widen sharply, see Fig.[8](https://arxiv.org/html/2511.02973v1#S4.F8 "Figure 8 ‣ 4.3 Improved adaptive capacity and pre-disaster fiscal position ‣ 4 Results ‣ Extreme events and public debt dynamics: Lessons from Croatia’s experienceThe opinions expressed in this publication are those of the authors. We are grateful to Leonardo Martinez for his careful reading and suggestions for improvement. A special thanks goes to Daniele Tavani for insightful correspondence on earlier drafts of the article. The usual caveats apply."). Meanwhile, economic growth plays a dual role: in normal times and recovery periods, it is the main force reducing the debt ratio, but during recessions, its contractionary effect greatly amplifies debt burdens. These findings align with empirical evidence that large debt surprises most often stem from fiscal slippages and weaker-than-expected growth.

Second, the timing and persistence of debt pressures depend on the nature of the shock. A one-off shock creates an immediate but temporary spike in debt, whereas protracted or repeated shocks cause sustained debt accumulation that is far more difficult to reverse. Intermediate cases, such as the local projection or quantile scenarios, suggest that debt can overshoot and then partially revert. The extent of that correction hinges on the strength of post-shock fiscal consolidation and economic recovery. In our projections, interest rate effects remain small because economic growth outpaces borrowing costs over the period. However, this favourable interest-growth differential could erode if debt remains high or interest rates rise. Overall, these results underscore that debt trajectories are highly sensitive to shock size, shock persistence, and the policy response. Strong economic growth and credible fiscal consolidation are crucial for stabilising debt after a shock, whereas large or repeated shocks can push public debt to a persistently higher path.

## 5 Conclusions

This paper has examined the sustainability of public debt in a small open economy, such as Croatia, that is subject to severe natural disasters. Using the IMF’s Natural Disaster Debt Dynamic Tool, the analysis combined a baseline trajectory with a set of stress scenarios and stochastic simulations to evaluate the scale and persistence of debt deviations under different shock structures. Three main conclusions follow. First, in the absence of major shocks, Croatia’s debt-to-GDP ratio is projected to decline gradually over the medium term, falling below the EU’s 60 per cent reference threshold and stabilising in the mid-50s range by 2030. This benign baseline confirms the role of steady growth and moderate fiscal discipline in maintaining a sustainable debt trajectory, though it also shows that the pace of reduction is modest and vulnerable to slippages.

Second, a severe natural disaster can derail this trajectory. Stress scenarios reveal pronounced increases in debt, with the timing and persistence of pressures varying by shock type. A single, short-lived disaster produces an abrupt one-year surge, whereas repeated or drawn-out shocks yield a more chronic build-up that persists across the projection horizon. Intermediate outcomes emerge under econometric specifications: debt peaks with a lag and then partly reverts as growth rebounds and fiscal policy consolidates. Yet in tail-risk cases, the adjustment is incomplete, leaving the debt ratio on a permanently higher plateau. These findings echo broader evidence that disaster-related output losses are rarely fully recouped, leaving economies smaller relative to their pre-shock path [[33](https://arxiv.org/html/2511.02973v1#biba.bibx4), [53](https://arxiv.org/html/2511.02973v1#biba.bibx24), [52](https://arxiv.org/html/2511.02973v1#biba.bibx23)]. In line with this literature, the Croatian simulations indicate that even with a growth rebound, the debt burden stabilises only slowly and does not fully return to baseline.

Third, the decomposition of debt dynamics highlights that fiscal balances are the main driver of debt increases. Economic growth plays a dual role, mitigating debt in recoveries but amplifying it in recession years. Interest costs and stock-flow adjustments remain secondary within the horizon considered, but would become more significant if debt remained high or financing conditions tightened. The main policy implication is that preserving fiscal discipline and sustaining growth are essential to safeguard debt sustainability. Conversely, fiscal slippages or weak recoveries translate directly into accelerating debt ratios.

A further implication concerns the design of fiscal frameworks in disaster-prone economies. Maintaining adequate buffers during tranquil periods provides critical space to absorb shocks. Entering the 2020 twin shocks with debt near 75 per cent of GDP, Croatia was left with little headroom. A more prudent medium-term anchor closer to 50 per cent would strengthen resilience. Such buffers can be reinforced not only through small surpluses but also through dedicated instruments. [[55](https://arxiv.org/html/2511.02973v1#biba.bibx26)] stresses the value of “rainy day” or stabilisation funds that can be drawn upon without recourse to new borrowing, while the IMF’s (\citeyearIMFECCU) Eastern Caribbean Currency Union analysis points to the usefulness of contingency funds and parametric insurance to secure rapid financing after disasters. Integrating such arrangements into Croatia’s fiscal strategy would limit the impact of extreme events on debt and complement conventional consolidation policies.

The Croatian case illustrates a general principle for fiscal policy in the context of disaster risk. While the baseline outlook may appear favourable, resilience depends on preparing for low-probability, high-impact events. Strengthening fiscal space, institutional preparedness, and risk-sharing mechanisms during normal times enhances the ability to withstand shocks without jeopardising sustainability. The analysis presented here quantifies the scale of potential debt deviations and provides an analytical foundation for embedding disaster risk considerations into debt management frameworks.

## Appendix A Appendix

The calibration of our natural-disaster shock scenario focused on economic growth (gtg\_{t}) and the primary balance (p​btpb\_{t}). Still, the reader might wonder if these are indeed the only two critical channels through which public debt is affected. At least two additional transmission mechanisms deserve closer examination: the interest rate (iti\_{t}) and inflation (πt\pi\_{t}). This Appendix reports our econometric findings using local projections and quantile regressions, allowing for simultaneous shocks in all four variables. The magnitude and persistence of disturbances rely on historical disaster data from EM-DAT and IMF vintage projections. As before, our exercise is anchored to the 2020 Zagreb earthquake.

After an extreme event such as an earthquake, economic agents may anticipate that the government will implement an expansionary fiscal policy to finance reconstruction and relief efforts. A change in risk perception following the disaster could increase the liquidity premium on government securities, affecting borrowing costs. However, if the Central Bank responds to the emergency with an expansionary monetary policy, nominal interest rates may actually decline. This seems to have been the case in Croatia after the 2020 earthquakes [[58](https://arxiv.org/html/2511.02973v1#biba.bibx29)].222Moreover, the Croatian National Bank (CNB) permitted credit institutions to apply the flexible treatment to exposures to debtors affected by the earthquakes in Zagreb and Pokuplje in March and December 2020, respectively. The CNB extended the application of the preferential treatment to include also the moratoria granted after 1 October 2020 to clients hit by the COVID-19 pandemic until the end of March 2021, with the maximum duration of the moratorium being nine months. A similar approach is also applied to clients affected by the earthquake (CNB, \citeyearCNB2021). Regarding inflation, natural disasters typically act as negative supply shocks, generating upward pressure on prices. Nonetheless, such extreme events are also demand shocks. If post-disaster, households and firms reduce spending and save more as precautionary savings, consumption will fall. The resulting fall in aggregate demand can offset or even dominate the supply-side pressures, potentially leading to a temporary decline in inflation.

Fig. [A.1](https://arxiv.org/html/2511.02973v1#A1.F1 "Figure A.1 ‣ Appendix A Appendix ‣ Extreme events and public debt dynamics: Lessons from Croatia’s experienceThe opinions expressed in this publication are those of the authors. We are grateful to Leonardo Martinez for his careful reading and suggestions for improvement. A special thanks goes to Daniele Tavani for insightful correspondence on earlier drafts of the article. The usual caveats apply.") shows that for the quantile regressions in blue, public debt converges to 63-67% of GDP, a value close to what was reported in Fig. [7](https://arxiv.org/html/2511.02973v1#S4.F7 "Figure 7 ‣ 4.3 Improved adaptive capacity and pre-disaster fiscal position ‣ 4 Results ‣ Extreme events and public debt dynamics: Lessons from Croatia’s experienceThe opinions expressed in this publication are those of the authors. We are grateful to Leonardo Martinez for his careful reading and suggestions for improvement. A special thanks goes to Daniele Tavani for insightful correspondence on earlier drafts of the article. The usual caveats apply."). However, improving PB and AC results in significantly higher debt, as shown by the dashed blue line, which rises to 159% in 2027, then stabilises at 111% of GDP by the end of the period. Similarly, as indicated by the red lines, local projections suggest a strong increase in debt, reaching almost 150% of GDP in 2028. During the next five years, a gradual decline is followed to 138%. When improved PB and AC are applied, the dynamic is maintained, with a 10 percentage-point increase.

Figure A.1: Gross Nominal Public Debt in Alternative Scenarios

![Refer to caption](graphics/graphics_final/A1.png)


Source: Authors’ calculation. Improved pre-disaster fiscal balance +3 % of GDP and adaptive capacity = 0.

To understand the large difference between results delivered by the two methods, it is useful to look at an approximation of Eq. ([1](https://arxiv.org/html/2511.02973v1#S3.E1 "In 3.1 Baseline debt dynamics ‣ 3 Methodology ‣ Extreme events and public debt dynamics: Lessons from Croatia’s experienceThe opinions expressed in this publication are those of the authors. We are grateful to Leonardo Martinez for his careful reading and suggestions for improvement. A special thanks goes to Daniele Tavani for insightful correspondence on earlier drafts of the article. The usual caveats apply.")), that is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​dt≈(it−πt−gt)​dt−1−p​bt+o​ft\Delta d\_{t}\approx(i\_{t}-\pi\_{t}-g\_{t})d\_{t-1}-pb\_{t}+of\_{t} |  | (A.1) |

where it−πt−gti\_{t}-\pi\_{t}-g\_{t} is a debt stock amplification term. This component makes the effect state-dependent and multiplicative, producing a dynamic amplification. Local projections explicitly capture persistence, cumulative effects and feedback over time. Our data indicates that both iti\_{t} and πt\pi\_{t} were negatively impacted, but inflation fell more than interest rates, thus resulting in an increase of the amplification term, which was captured in our local projection and improved quantile regressions. Fig. [A.2](https://arxiv.org/html/2511.02973v1#A1.F2 "Figure A.2 ‣ Appendix A Appendix ‣ Extreme events and public debt dynamics: Lessons from Croatia’s experienceThe opinions expressed in this publication are those of the authors. We are grateful to Leonardo Martinez for his careful reading and suggestions for improvement. A special thanks goes to Daniele Tavani for insightful correspondence on earlier drafts of the article. The usual caveats apply.") disaggregates the main contributors to the increase in the debt ratio captured in this scenario. The major grey parts of the columns indicate that the real interest rate is the main contributor through the iti\_{t} and πt\pi\_{t} difference. No other component gets closer to their impact.

Figure A.2: Croatia Public Sector Debt Dynamics in Alternative Scenarios, 2026–2031

a) Local projection 
  
![Refer to caption](graphics/graphics_final/A2_DCF_local.png)

b) Local projection with PB and AC improved 
  
![Refer to caption](graphics/graphics_final/A2_DCF_local_pb_and_ac.png)

c) Quantile projection 
  
![Refer to caption](graphics/graphics_final/A2_DCF_quantile.png)

d) Quantile projection with PB and AC improved 
  
![Refer to caption](graphics/graphics_final/A2_DCF_quantile_pb_and_ac.png)

Source: Authors’ calculation.

While the estimated local projection coefficients capture statistically significant relationships between composite climate shocks and macroeconomic variables, the empirical results for the GDP deflator and the effective interest rate should be interpreted with caution. The econometric estimates suggest a stronger disinflationary response (and consequently higher real debt burden) with improved adaptive capacity, which is contrary to the expected relationship. However, inflation dynamics are particularly difficult to generalise across countries, and the cross-country elasticities may not accurately reflect the Croatian context.

Similarly, movements in the effective interest rate on local currency debt are constrained by the structure of outstanding debt, as the rate represents an average cost heavily influenced by past borrowing conditions. Given the low volatility of Croatian interest rates and their nominal character, these results are unlikely to meaningfully translate into country-specific implications. For both inflation and interest rates, it may therefore be more informative to rely on national estimates or to perform a comparative static analysis as a robustness check, for example, assessing the change in the debt path if inflation decreases by 1 percentage point or if the interest rate rises by 50 basis points.

Empirical LP specification for Croatia

|  |  |  |  |
| --- | --- | --- | --- |
|  | yi,t+h−yi,t−1=αi,h+βh​Shocki,t+h+γ1​h​(onseti,t×Damagei,t)+γ2​h​(onseti,t×A​Ei,t)+γ3​h​(onseti,t×NDcapacityi,t)+γ4​h​(onseti,t×f​bi,t)+δ1​h​yi,t−1+δ2​h​f​bi,t−1+δ3​h​ExtraND1995i,t−1+εi,t+h\begin{aligned} y\_{i,t+h}-y\_{i,t-1}=\;&\alpha\_{i,h}+\beta\_{h}\text{Shock}\_{i,t+h}\\ &+\gamma\_{1h}(\text{onset}\_{i,t}\times\text{Damage}\_{i,t})+\gamma\_{2h}(\text{onset}\_{i,t}\times AE\_{i,t})+\gamma\_{3h}(\text{onset}\_{i,t}\times\text{NDcapacity}\_{i,t})\\ &+\gamma\_{4h}(\text{onset}\_{i,t}\times fb\_{i,t})+\delta\_{1h}y\_{i,t-1}+\delta\_{2h}fb\_{i,t-1}+\delta\_{3h}\text{ExtraND1995}\_{i,t-1}+\varepsilon\_{i,t+h}\end{aligned} |  | (A.2) |

Note: The equation is equivalent to Eq. (3) and was estimated separately for each horizon h=0,1,2h=0,1,2, corresponding to contemporaneous (L.L.), one-year-ahead (F.F.), and two-year-ahead (F​2.F2.) responses.

*Variable definitions:*
yi,t+hy\_{i,t+h} denotes the macroeconomic indicator of interest (GDP growth, GDP deflator, effective interest rate, or fiscal balance), expressed as deviation from trend between periods t−1t-1 and t+ht+h. Parameter
αi,h\alpha\_{i,h} represents country fixed effects.
Shocki,t+h\text{Shock}\_{i,t+h} is the contemporaneous climate shock intensity, measured as the standardised deviation in the occurrence or magnitude of climate-related disasters.
onseti,t\text{onset}\_{i,t} is a dummy variable equal to 1 in the year a climate disaster occurs and 0 otherwise.
Damagei,t\text{Damage}\_{i,t} measures the physical intensity of the disaster, expressed as the share of population affected or the estimated loss relative to GDP.
A​Ei,tAE\_{i,t} is a dummy variable equal to 1 for advanced economies (according to IMF classification) and 0 otherwise.
NDcapacityi,t\text{NDcapacity}\_{i,t} captures the climate policy and institutional capacity, reflecting a country’s ability to design and implement mitigation and adaptation strategies.
Variable f​bi,tfb\_{i,t} represents the overall fiscal balance as a per cent of GDP; yi,t−1y\_{i,t-1} is the lagged dependent variable, controlling for persistence in the macroeconomic outcome; f​bi,t−1fb\_{i,t-1} is the lagged fiscal balance, capturing fiscal inertia and prior fiscal stance.
ExtraND1995i,t−1\text{ExtraND1995}\_{i,t-1} indicates whether a country had an established national disaster policy framework or institutional arrangement since 1995. Finally, εi,t+h\varepsilon\_{i,t+h} is the error term. Tables A.1-A.8 report our local projection estimates.

Table A.1: Change in GDP growth

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ\Delta GDP growth, deviation from trend | | |
|  | t=0t=0 | t=1t=1 | t=2t=2 |
| lcompshock | 6.160 |  |  |
|  | (1.886) |  |  |
| F.lcompshock |  | 8.101 |  |
|  |  | (2.201) |  |
| F2.lcompshock |  |  | 8.998 |
|  |  |  | (2.080) |
| onset | 0.160 | 1.480 | 1.972 |
|  | (2.493) | (2.846) | (2.604) |
| onset\*damage | -0.031 | 0.018 | -0.032 |
|  | (0.007) | (0.018) | (0.021) |
| onset\*AE | 0.364 | -0.569 | -0.570 |
|  | (1.465) | (1.496) | (1.386) |
| Growtht-1 | 0.299 | 0.106 | 0.070 |
|  | (0.027) | (0.023) | (0.022) |
| onset\*fb | 0.070 | 0.131 | 0.155 |
|  | (0.111) | (0.079) | (0.066) |
| L.fb | 0.029 | 0.032 | 0.013 |
|  | (0.012) | (0.015) | (0.013) |
| onset\*NDCapacity | -0.879 | -2.202 | -0.788 |
|  | (3.994) | (5.270) | (4.649) |
| L.extraND1995 | 4.634 | 10.487 | 9.040 |
|  | (3.922) | (4.820) | (5.082) |
| Constant | -1.206 | -5.445 | -3.244 |
|  | (2.312) | (2.968) | (2.980) |
| Observations | 4 321 | 4 151 | 3 984 |
| R2R^{2} | 0.199 | 0.132 | 0.123 |
| Number of countries | 172 | 172 | 172 |

*Notes:* Local projections in a scenario with f​b2024=−1.1fb\_{2024}=-1.1 and N​D​C​a​p​a​c​i​t​y2024=0.4NDCapacity\_{2024}=0.4. Coefficients estimated on a panel of 172 countries. Variables not relevant for Croatia (storm, flood, drought, Small Island, LIDC) are excluded. Standard errors in parentheses. Scenario corresponds to an initial primary balance f​b2024=−1.1fb\_{2024}=-1.1 (per cent of GDP) and climate policy and institutional capacity N​D​C​a​p​a​c​i​t​y2024=0.4NDCapacity\_{2024}=0.4, which enter the specification through the interaction terms onset\*fb and onset\*NDCapacity.
  
Standard error for prediction: t=0t=0: 0.7268, t=1t=1: 0.8652, t=2t=2: 0.9034.




Table A.2: Change in primary balance

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ\Delta primary balance, deviation from trend | | |
|  | t=0t=0 | t=1t=1 | t=2t=2 |
| lcompshock | 13.566 |  |  |
|  | (4.163) |  |  |
| F.lcompshock |  | 35.889 |  |
|  |  | (5.211) |  |
| F2.lcompshock |  |  | 34.052 |
|  |  |  | (4.661) |
| onset | 0.527 | 2.785 | 0.242 |
|  | (2.447) | (2.398) | (2.396) |
| onset\*damage | -0.001 | 0.010 | -0.020 |
|  | (0.014) | (0.010) | (0.015) |
| onset\*AE | -0.444 | -2.744 | -0.975 |
|  | (1.326) | (1.413) | (1.434) |
| pbt-1 | 0.985 | 0.698 | 0.613 |
|  | (0.183) | (0.111) | (0.137) |
| onset\*fb | 0.165 | 0.159 | 0.135 |
|  | (0.091) | (0.125) | (0.135) |
| L.fb | -0.534 | -0.438 | -0.490 |
|  | (0.182) | (0.118) | (0.156) |
| onset\*NDCapacity | 0.859 | -2.943 | 0.542 |
|  | (3.961) | (4.116) | (4.094) |
| L.extraND1995 | 2.255 | 1.813 | -1.871 |
|  | (6.506) | (8.312) | (10.530) |
| Constant | -3.592 | -3.035 | -2.158 |
|  | (3.815) | (4.791) | (6.054) |
| Observations | 4 390 | 4 223 | 4 054 |
| R2R^{2} | 0.324 | 0.237 | 0.166 |
| Number of countries | 170 | 170 | 170 |

*Notes:* Local projections in a scenario with f​b2024=−1.1fb\_{2024}=-1.1 and N​D​C​a​p​a​c​i​t​y2024=0.4NDCapacity\_{2024}=0.4. Coefficients estimated on a panel of 170 countries. Variables not relevant for Croatia (storm, flood, drought, Small Island, LIDC) are excluded. Standard errors in parentheses. Scenario corresponds to an initial primary balance f​b2024=−1.1fb\_{2024}=-1.1 (per cent of GDP) and climate policy and institutional capacity N​D​C​a​p​a​c​i​t​y2024=0.4NDCapacity\_{2024}=0.4, which enter the specification through the interaction terms onset\*fb and onset\*NDCapacity.
  
Standard error for prediction: t=0t=0: 1.260, t=1t=1: 1.479, t=2t=2: 1.843.




Table A.3: Change in effective interest rate on local currency debt

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ\Delta effective interest rate (LC), deviation from trend | | |
|  | t=0t=0 | t=1t=1 | t=2t=2 |
| lcompshock | 12.440 |  |  |
|  | (13.358) |  |  |
| F.lcompshock |  | 23.842 |  |
|  |  | (20.239) |  |
| F2.lcompshock |  |  | 35.566 |
|  |  |  | (28.851) |
| onset | -1.119 | 1.093 | 6.017 |
|  | (0.950) | (1.695) | (3.682) |
| onset\*damage | 0.419 | 2.839 | 4.296 |
|  | (0.971) | (1.325) | (2.333) |
| onset\*AE | -1.119 | 1.093 | 6.017 |
|  | (0.950) | (1.695) | (3.682) |
| int\_lct-1 | 0.592 | 0.246 | -0.135 |
|  | (0.044) | (0.012) | (0.056) |
| onset\*fb | 0.381 | -0.172 | -0.425 |
|  | (0.150) | (0.416) | (0.354) |
| L.fb | -0.195 | -0.304 | -0.281 |
|  | (0.156) | (0.232) | (0.186) |
| onsetNDextra | -1.639 | -1.718 | 8.585 |
|  | (3.420) | (4.388) | (7.207) |
| L.extraND1995 | 5.932 | 10.435 | 13.170 |
|  | (4.935) | (7.562) | (9.974) |
| Constant | -1.982 | -2.092 | -2.052 |
|  | (3.072) | (4.630) | (6.020) |
| Observations | 2 216 | 2 099 | 1 983 |
| R2R^{2} | 0.404 | 0.129 | 0.091 |
| Number of countries | 118 | 118 | 118 |

*Notes:* Local projections in a scenario with f​b2024=−1.1fb\_{2024}=-1.1 and N​D​C​a​p​a​c​i​t​y2024=0.4NDCapacity\_{2024}=0.4). Coefficients estimated on a panel of 118 countries. Variables not relevant for Croatia (storm, flood, drought, Small Island, LIDC) are excluded. Standard errors in parentheses. Scenario corresponds to an initial primary balance f​b2024=−1.1fb\_{2024}=-1.1 (per cent of GDP) and climate policy and institutional capacity N​D​C​a​p​a​c​i​t​y2024=0.4NDCapacity\_{2024}=0.4, which enter the specification through the interaction terms onset\*fb and onset\*NDCapacity.
  
Standard error for prediction: t=0t=0: 1.1787, t=1t=1: 1.6230, t=2t=2: 1.8689.




Table A.4: Change in GDP deflator

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ\Delta GDP deflator, deviation from trend | | |
|  | t=0t=0 | t=1t=1 | t=2t=2 |
| lcompshock | -13.764 |  |  |
|  | (11.370) |  |  |
| F.lcompshock |  | -10.856 |  |
|  |  | (10.797) |  |
| F2.lcompshock |  |  | -1.603 |
|  |  |  | (15.248) |
| onset | -17.113 | -11.527 | 9.858 |
|  | (16.026) | (12.234) | (7.451) |
| onset\*damage | 0.064 | 0.040 | 0.025 |
|  | (0.044) | (0.025) | (0.023) |
| onset\*AE | 3.992 | 6.665 | -0.527 |
|  | (6.416) | (4.952) | (3.481) |
| gdpdeflatort-1 | 0.512 | 0.437 | 0.203 |
|  | (0.108) | (0.050) | (0.088) |
| onset\*fb | -0.747 | 0.041 | 0.144 |
|  | (0.446) | (0.173) | (0.244) |
| L.fb | -0.044 | -0.058 | -0.049 |
|  | (0.052) | (0.062) | (0.057) |
| onsetNDextra | 30.607 | 20.690 | -22.103 |
|  | (30.274) | (22.555) | (13.425) |
| L.extraND1995 | 0.746 | -3.941 | 4.915 |
|  | (9.835) | (11.793) | (13.883) |
| Constant | 11.883 | 9.389 | 15.802 |
|  | (7.234) | (6.708) | (9.806) |
| Observations | 4 348 | 4 177 | 4 006 |
| R2R^{2} | 0.357 | 0.270 | 0.129 |
| Number of countries | 170 | 170 | 170 |

*Notes:* Local projections in a scenario with f​b2024=−1.1fb\_{2024}=-1.1 and N​D​C​a​p​a​c​i​t​y2024=0.4NDCapacity\_{2024}=0.4). Coefficients estimated on a panel of up to 170 countries. Variables not relevant for Croatia (storm, flood, drought, Small Island, LIDC) are excluded. Standard errors in parentheses. Scenario corresponds to an initial fiscal balance f​b2024=−1.1fb\_{2024}=-1.1 (percent of GDP) and climate policy and institutional capacity N​D​C​a​p​a​c​i​t​y2024=0.4NDCapacity\_{2024}=0.4, which enter the specification through the interaction terms onset\*fb and onset\*NDCapacity.
  
Standard error for prediction: t=0t=0: 2.379, t=1t=1: 2.436, t=2t=2: 2.830.




Table A.5: Change in GDP growth

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ\Delta GDP growth, deviation from trend | | |
|  | t=0t=0 | t=1t=1 | t=2t=2 |
| lcompshock | 6.160 |  |  |
|  | (1.886) |  |  |
| F.lcompshock |  | 8.101 |  |
|  |  | (2.201) |  |
| F2.lcompshock |  |  | 8.998 |
|  |  |  | (2.080) |
| onset | 0.160 | 1.480 | 1.972 |
|  | (2.493) | (2.846) | (2.604) |
| onset\*damage | -0.031 | 0.018 | -0.032 |
|  | (0.007) | (0.018) | (0.021) |
| onset\*AE | 0.364 | -0.569 | -0.570 |
|  | (1.465) | (1.496) | (1.386) |
| Growtht-1 | 0.299 | 0.106 | 0.070 |
|  | (0.027) | (0.023) | (0.022) |
| onset\*fb | 0.070 | 0.131 | 0.155 |
|  | (0.111) | (0.079) | (0.066) |
| L.fb | 0.029 | 0.032 | 0.013 |
|  | (0.012) | (0.015) | (0.013) |
| onset\*NDCapacity | -0.879 | -2.202 | -0.788 |
|  | (3.994) | (5.270) | (4.649) |
| L.extraND1995 | 4.634 | 10.487 | 9.040 |
|  | (3.922) | (4.820) | (5.082) |
| Constant | -1.206 | -5.445 | -3.244 |
|  | (2.312) | (2.968) | (2.980) |
| Observations | 4 321 | 4 151 | 3 984 |
| R2R^{2} | 0.199 | 0.132 | 0.123 |
| Number of countries | 172 | 172 | 172 |

*Notes:* Local projections in a scenario with f​b2024=3fb\_{2024}=3 and N​D​C​a​p​a​c​i​t​y2024=0NDCapacity\_{2024}=0). Coefficients estimated on a panel of 172 countries. Variables not relevant for Croatia (storm, flood, drought, Small Island, LIDC) are excluded. Standard errors in parentheses. Scenario assumes policy buffer f​b2024=+3fb\_{2024}=+3 and adaptive capacity N​D​C​a​p​a​c​i​t​y2024=0NDCapacity\_{2024}=0.
  
Standard error for prediction: t=0t=0: 0.727, t=1t=1: 0.865, t=2t=2: 0.903.




Table A.6: Change in primary balance

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ\Delta primary balance, deviation from trend | | |
|  | t=0t=0 | t=1t=1 | t=2t=2 |
| lcompshock | 13.566 |  |  |
|  | (4.163) |  |  |
| F.lcompshock |  | 35.889 |  |
|  |  | (5.211) |  |
| F2.lcompshock |  |  | 34.052 |
|  |  |  | (4.661) |
| onset | 0.527 | 2.785 | 0.242 |
|  | (2.447) | (2.398) | (2.396) |
| onset\*damage | -0.001 | 0.010 | -0.020 |
|  | (0.014) | (0.010) | (0.015) |
| onset\*AE | -0.444 | -2.744 | -0.975 |
|  | (1.326) | (1.413) | (1.434) |
| pbt-1 | 0.985 | 0.698 | 0.613 |
|  | (0.183) | (0.111) | (0.137) |
| onset\*fb | 0.165 | 0.159 | 0.135 |
|  | (0.091) | (0.125) | (0.135) |
| L.fb | -0.534 | -0.438 | -0.490 |
|  | (0.182) | (0.118) | (0.156) |
| onset\*NDCapacity | 0.859 | -2.943 | 0.542 |
|  | (3.961) | (4.116) | (4.094) |
| L.extraND1995 | 2.255 | 1.813 | -1.871 |
|  | (6.506) | (8.312) | (10.530) |
| Constant | -3.592 | -3.035 | -2.158 |
|  | (3.815) | (4.791) | (6.054) |
| Observations | 4 390 | 4 223 | 4 054 |
| R2R^{2} | 0.324 | 0.237 | 0.166 |
| Number of countries | 170 | 170 | 170 |

*Notes:* Local projections in a scenario with f​b2024=3fb\_{2024}=3 and N​D​C​a​p​a​c​i​t​y2024=0NDCapacity\_{2024}=0). Coefficients estimated on a panel of 170 countries. Variables not relevant for Croatia (storm, flood, drought, Small Island, LIDC) are excluded. Standard errors in parentheses. The scenario assumes a policy buffer of f​b2024=3fb\_{2024}=3 and an adaptive capacity of N​D​C​a​p​a​c​i​t​y2024=0NDCapacity\_{2024}=0.
  
Standard error for prediction: t=0t=0: 1.260, t=1t=1: 1.479, t=2t=2: 1.843.




Table A.7: Change in effective interest rate on local currency debt

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ\Delta effective interest rate (LC), deviation from trend | | |
|  | t=0t=0 | t=1t=1 | t=2t=2 |
| lcompshock | 12.440 |  |  |
|  | (13.358) |  |  |
| F.lcompshock |  | 23.842 |  |
|  |  | (20.239) |  |
| F2.lcompshock |  |  | 35.566 |
|  |  |  | (28.851) |
| onset | -1.119 | 1.093 | 6.017 |
|  | (0.950) | (1.695) | (3.682) |
| onset\*damage | 0.419 | 2.839 | 4.296 |
|  | (0.971) | (1.325) | (2.333) |
| onset\*AE | -1.119 | 1.093 | 6.017 |
|  | (0.950) | (1.695) | (3.682) |
| int\_lct-1 | 0.592 | 0.246 | -0.135 |
|  | (0.044) | (0.012) | (0.056) |
| onset\*fb | 0.381 | -0.172 | -0.425 |
|  | (0.150) | (0.416) | (0.354) |
| L.fb | -0.195 | -0.304 | -0.281 |
|  | (0.156) | (0.232) | (0.186) |
| onsetNDextra | -1.639 | -1.718 | 8.585 |
|  | (3.420) | (4.388) | (7.207) |
| L.extraND1995 | 5.932 | 10.435 | 13.170 |
|  | (4.935) | (7.562) | (9.974) |
| Constant | -1.982 | -2.092 | -2.052 |
|  | (3.072) | (4.630) | (6.020) |
| Observations | 2 216 | 2 099 | 1 983 |
| R2R^{2} | 0.404 | 0.129 | 0.091 |
| Number of countries | 118 | 118 | 118 |

*Notes:* Local projections in a scenario with f​b2024=3fb\_{2024}=3 and N​D​C​a​p​a​c​i​t​y2024=0NDCapacity\_{2024}=0). Coefficients estimated on a panel of 118 countries. Variables not relevant for Croatia (storm, flood, drought, Small Island, LIDC) are excluded. Standard errors in parentheses. The scenario assumes a policy buffer of f​b2024=3fb\_{2024}=3 and an adaptive capacity of N​D​C​a​p​a​c​i​t​y2024=0NDCapacity\_{2024}=0.
  
Standard error for prediction: t=0t=0: 1.179, t=1t=1: 1.623, t=2t=2: 1.869.




Table A.8: Change in GDP deflator

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ\Delta GDP deflator, deviation from trend | | |
|  | t=0t=0 | t=1t=1 | t=2t=2 |
| lcompshock | -13.764 |  |  |
|  | (11.370) |  |  |
| F.lcompshock |  | -10.856 |  |
|  |  | (10.797) |  |
| F2.lcompshock |  |  | -1.603 |
|  |  |  | (15.248) |
| onset | -17.113 | -11.527 | 9.858 |
|  | (16.026) | (12.234) | (7.451) |
| onset\*damage | 0.064 | 0.040 | 0.025 |
|  | (0.044) | (0.025) | (0.023) |
| onset\*AE | 3.992 | 6.665 | -0.527 |
|  | (6.416) | (4.952) | (3.481) |
| gdpdeflatort-1 | 0.512 | 0.437 | 0.203 |
|  | (0.108) | (0.050) | (0.088) |
| onset\*fb | -0.747 | 0.041 | 0.144 |
|  | (0.446) | (0.173) | (0.244) |
| L.fb | -0.044 | -0.058 | -0.049 |
|  | (0.052) | (0.062) | (0.057) |
| onsetNDextra | 30.607 | 20.690 | -22.103 |
|  | (30.274) | (22.555) | (13.425) |
| L.extraND1995 | 0.746 | -3.941 | 4.915 |
|  | (9.835) | (11.793) | (13.883) |
| Constant | 11.883 | 9.389 | 15.802 |
|  | (7.234) | (6.708) | (9.806) |
| Observations | 4 348 | 4 177 | 4 006 |
| R2R^{2} | 0.357 | 0.270 | 0.129 |
| Number of countries | 170 | 170 | 170 |

*Notes:* Local projections in a scenario with f​b2024=3fb\_{2024}=3 and N​D​C​a​p​a​c​i​t​y2024=0NDCapacity\_{2024}=0). Coefficients estimated on a panel of 170 countries. Variables not relevant for Croatia (storm, flood, drought, Small Island, LIDC) are excluded. Standard errors in parentheses. The scenario assumes a policy buffer of f​b2024=3fb\_{2024}=3 and an adaptive capacity of N​D​C​a​p​a​c​i​t​y2024=0NDCapacity\_{2024}=0.
  
Standard error for prediction: t=0t=0: 2.379, t=1t=1: 2.436, t=2t=2: 2.830.

## References

* [1]
  S. Acosta-Ormaechea, L. Martinez and J. Restrepo
  “A Guide and Tool for Projecting Public Gross Financing Needs” Available at IMF website, 2025
  URL: <https://www.imf.org/-/media/Files/Publications/TNM/2025/English/TNMEA2025001.ashx>
* [2]
  Santiago Acosta-Ormaechea and Leonardo Martinez
  “A Guide and Tool for Projecting Public Debt and Fiscal Adjustment Paths with Local- and Foreign-Currency Debt” Available at IMF eLibrary, 2021
  DOI: [10.5089/9781513577289.005](https://dx.doi.org/10.5089/9781513577289.005)
* [3]
  A. Bates, G. Guannel and L. Quinones
  “Hurricanes make headlines, but chronic utility failure drives energy (in)security in the U.S. Virgin Islands”
  In *Energy Policy* 195, 2024, pp. 114320
  DOI: [10.1016/j.enpol.2024.114320](https://dx.doi.org/10.1016/j.enpol.2024.114320)
* [4]
  Tamim Bayoumi and Douglas Laxton
  “Macroeconomic Resilience to Natural Disasters”
  In *IMF Working Paper*, 2021
  URL: <https://www.elibrary.imf.org/view/journals/001/2021/234/article-A001-en.xml>
* [5]
  Eduardo Cavallo, Sebastian Galiani, Ilan Noy and Juan Pantano
  “Catastrophic Natural Disasters and Economic Growth”
  In *Review of Economics and Statistics* 95.5, 2013, pp. 1549–1561
  DOI: [10.1162/REST\_a\_00413](https://dx.doi.org/10.1162/REST_a_00413)
* [6]
  Oya Celasun, Xavier Debrun and Jonathan D. Ostry
  “Primary Surplus Behavior and Risks to Fiscal Sustainability in Emerging Market Countries: A “Fan-Chart” Approach”
  In *IMF Staff Papers* 53.3
  International Monetary Fund, 2007, pp. 401–425
  URL: <https://www.imf.org/External/Pubs/FT/staffp/2006/04/pdf/celasun.pdf>
* [7]
  Sulkhan Chavleishvili and Emanuel Moench
  “Natural disasters as macroeconomic tail risks”
  In *Journal of Econometrics* 247, 2025, pp. 105914
  DOI: [10.1016/j.jeconom.2024.105914](https://dx.doi.org/10.1016/j.jeconom.2024.105914)
* [8]
   Croatian National Bank
  “Macroprudential Diagnostics”, 2021
  URL: <https://www.hnb.hr/c/document_library/get_file?uuid=3d451468-6695-3c63-883a-d9034aa98840&groupId=20182&p_auth=wXmtUhZ6>
* [9]
   Croatian National Bank
  “Financial Stability 26”, 2025
  URL: <https://www.hnb.hr/c/document_library/get_file?uuid=f7daec4b-6d1a-1190-b5f6-c7dcb1359dd0&groupId=20182&p_auth=HtSfWp0r>
* [10]
   Croatian National Bank
  “Macroeconomic Developments and Outlook”, 2025
  URL: <https://www.hnb.hr/c/document_library/get_file?uuid=b80ea79c-1fd4-3ebc-77cd-3ac49811b712&groupId=20182&p_auth=HtSfWp0r#page=65.17>
* [11]
  M. Deskar-Škrbić and D. Milutinović
  “Design of fiscal consolidation packages and model-based fiscal multipliers in Croatia”
  In *Public Sector Economics* 45.1, 2021, pp. 1–61
  DOI: [https://doi.org/10.3326/pse.45.1.1](https://dx.doi.org/https://doi.org/10.3326/pse.45.1.1)
* [12]
  A. Evgenidis, M. Hamano and W. Vermeulen
  “Economic consequences of follow-up disasters: Lessons from the 2011 Great East Japan Earthquake”
  In *Energy Economics* 104, 2021, pp. 105559
  DOI: [10.1016/j.eneco.2021.105559](https://dx.doi.org/10.1016/j.eneco.2021.105559)
* [13]
  T. Fomby, Y. Ikeda and N.. Loayza
  “The growth aftermath of natural disasters”
  In *Journal of Applied Econometrics* 28.3, 2013, pp. 412–434
  URL: <https://www.jstor.org/stable/43907505>
* [14]
  D. Galinec and T. Kandžija
  “The Impact of Stock-flow Adjustments on Changes in Croatian General Government Debt Level”
  In *Journal of Economy and Business*
  Mostar Faculty of Economics, 2018, pp. 214–227
  DOI: [10.46458/27121097.2018.SI.214](https://dx.doi.org/10.46458/27121097.2018.SI.214)
* [15]
  A.. Grosu
  “Public Debt Sustainability in Post-200 EU Member States With Euro Adoption: A Penalized Spline Regression Approach”
  In *Revista Economică* 77.1, 2025, pp. 69–84
  DOI: [10.56043/reveco-2025-0006](https://dx.doi.org/10.56043/reveco-2025-0006)
* [16]
  K. Guo et al.
  “Energy trade stability of China: Policy options with increasing climate risks”
  In *Energy Policy* 184, 2024, pp. 113858
  DOI: [10.1016/j.enpol.2023.113858](https://dx.doi.org/10.1016/j.enpol.2023.113858)
* [17]
  Stefan Hochrainer
  “Assessing the macroeconomic impacts of natural disasters: Are there any?”
  In *Policy Research Working Paper Series*, 2009
  URL: <https://pure.iiasa.ac.at/id/eprint/9010/1/XO-09-035.pdf>
* [18]
   International Monetary Fund
  “Staff Guidance Note for Public Debt Sustainability Analysis in Market-Access Countries” IMF Policy Paper, 2013
  URL: <https://www.imf.org/external/np/pp/eng/2013/050913.pdf>
* [19]
   International Monetary Fund
  “Eastern Caribbean Currency Union: Regional Disaster Resilience Strategy”, 2019
  URL: <https://www.bing.com/ck/a?!&&p=0e05d44ae0b60e12d1769d7117db1d5e936d63ee90b05fb904f7cdf0c78ba070JmltdHM9MTc1ODQ5OTIwMA&ptn=3&ver=2&hsh=4&fclid=2b9f6261-92e6-69c9-36a8-740893be68ad&psq=International+Monetary+Fund.+(2019a).+Eastern+caribbean+currency+union%3a+Regional+disaster+resilience+strategy&u=a1aHR0cHM6Ly93d3cuaW1mLm9yZy8tL21lZGlhL0ZpbGVzL1B1YmxpY2F0aW9ucy9DUi8yMDE5LzFFQ0NFQTIwMTkwMDIuYXNoeA>
* [20]
   IPCC
  “Summary for Policymakers”
  In *Climate Change 2021: The Physical Science Basis. Contribution of Working Group I to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change*
  Cambridge, UKNew York, NY, USA: Cambridge University Press, 2021, pp. 3–32
  DOI: [10.1017/9781009157896.001](https://dx.doi.org/10.1017/9781009157896.001)
* [21]
  Ò. Jordà
  “Estimation and Inference of Impulse Responses by Local Projections”
  In *American Economic Review* 95.1, 2005, pp. 161–182
  DOI: [10.1257/0002828053828518](https://dx.doi.org/10.1257/0002828053828518)
* [22]
  Roger Koenker and Gilbert Bassett
  “Regression Quantiles”
  In *Econometrica* 46.1, 1978, pp. 33–50
  URL: <https://www.econometricsociety.org/publications/econometrica/1978/01/01/regression-quantiles>
* [23]
  Ricardo Marto, Chris Papageorgiou and Vladimir Klyuev
  “Building Resilience to Natural Disasters: An Application to Small Developing States”, 2019
  URL: <https://www.bing.com/ck/a?!&&p=46f0fb92bdfcb2a484fb9c8c7235d3b2128d785a892bffca79354af9fca48ec3JmltdHM9MTc1ODQ5OTIwMA&ptn=3&ver=2&hsh=4&fclid=2b9f6261-92e6-69c9-36a8-740893be68ad&psq=Ricardo+Marto+and+Chris+Papageorgiou+and+Vladimir+Klyuev+Building+Resilience+to+Natural+Disasters%3a+An+Application+to+Small+Developing+States%7d%2c&u=a1aHR0cHM6Ly93d3cuaW1mLm9yZy9-L21lZGlhL0ZpbGVzL1B1YmxpY2F0aW9ucy9XUC8yMDE3L3dwMTcyMjMuYXNoeA>
* [24]
  Ha Minh Nguyen, Alan Feng and Mercedes Garcia-Escribano
  “Understanding the Macroeconomic Effects of Natural Disasters”, 2025
  URL: <https://www.bing.com/ck/a?!&&p=e4ad0749e7c01c72bf1560f9bcf48440fd538d5a7b65e9cf712a8dce45572385JmltdHM9MTc1ODQ5OTIwMA&ptn=3&ver=2&hsh=4&fclid=2b9f6261-92e6-69c9-36a8-740893be68ad&psq=nguyen%2c+H.%2c+%26+colleagues.+(2025).+Natural+disasters%2c+output+losses%2c+and+debt+d&u=a1aHR0cHM6Ly93d3cuaW1mLm9yZy8tL21lZGlhL0ZpbGVzL1B1YmxpY2F0aW9ucy9XUC8yMDI1L0VuZ2xpc2gvd3BpZWEyMDI1MDQ2LXByaW50LXBkZi5hc2h4>
* [25]
  Ilan Noy
  “The macroeconomic consequences of disasters”
  In *Journal of Development Economics* 88.2, 2009, pp. 221–231
  DOI: [10.1016/j.jdeveco.2008.02.005](https://dx.doi.org/10.1016/j.jdeveco.2008.02.005)
* [26]
   OECD and The World Bank
  “Fiscal Resilience to Natural Disasters: Lessons from Country Experiences”, 2019
  DOI: [10.1787/27a4198a-en](https://dx.doi.org/10.1787/27a4198a-en)
* [27]
  L. Srdelic and M. Davila-Fernandez
  “International trade and economic growth in Croatia”
  In *Structural Change and Economic Dynamics* 68.1, 2024, pp. 240–258
  DOI: [10.1016/j.strueco.2023.10.018](https://dx.doi.org/10.1016/j.strueco.2023.10.018)
* [28]
  K. Taniguchi
  “Why Fukushima? A diachronic and multilevel comparative institutional analysis of a nuclear disaster”
  In *Energy Policy* 167, 2022, pp. 113049
  DOI: [10.1016/j.enpol.2022.113049](https://dx.doi.org/10.1016/j.enpol.2022.113049)
* [29]
   Vujčić, B.
  “From Pandemics to the Unconventional Monetary Policy in EMs: The Case of Croatia”
  In *Real and Financial Sectors in Post-Pandemic Central and Eastern Europe: The Impact of Economic, Monetary, and Fiscal Policy*
  Switzerland: Springer, 2022, pp. 1–9
  DOI: [10.1007/978-3-030-99850-9\_1](https://dx.doi.org/10.1007/978-3-030-99850-9_1)

## References

* [30]
  S. Acosta-Ormaechea, L. Martinez and J. Restrepo
  “A Guide and Tool for Projecting Public Gross Financing Needs” Available at IMF website, 2025
  URL: <https://www.imf.org/-/media/Files/Publications/TNM/2025/English/TNMEA2025001.ashx>
* [31]
  Santiago Acosta-Ormaechea and Leonardo Martinez
  “A Guide and Tool for Projecting Public Debt and Fiscal Adjustment Paths with Local- and Foreign-Currency Debt” Available at IMF eLibrary, 2021
  DOI: [10.5089/9781513577289.005](https://dx.doi.org/10.5089/9781513577289.005)
* [32]
  A. Bates, G. Guannel and L. Quinones
  “Hurricanes make headlines, but chronic utility failure drives energy (in)security in the U.S. Virgin Islands”
  In *Energy Policy* 195, 2024, pp. 114320
  DOI: [10.1016/j.enpol.2024.114320](https://dx.doi.org/10.1016/j.enpol.2024.114320)
* [33]
  Tamim Bayoumi and Douglas Laxton
  “Macroeconomic Resilience to Natural Disasters”
  In *IMF Working Paper*, 2021
  URL: <https://www.elibrary.imf.org/view/journals/001/2021/234/article-A001-en.xml>
* [34]
  Eduardo Cavallo, Sebastian Galiani, Ilan Noy and Juan Pantano
  “Catastrophic Natural Disasters and Economic Growth”
  In *Review of Economics and Statistics* 95.5, 2013, pp. 1549–1561
  DOI: [10.1162/REST\_a\_00413](https://dx.doi.org/10.1162/REST_a_00413)
* [35]
  Oya Celasun, Xavier Debrun and Jonathan D. Ostry
  “Primary Surplus Behavior and Risks to Fiscal Sustainability in Emerging Market Countries: A “Fan-Chart” Approach”
  In *IMF Staff Papers* 53.3
  International Monetary Fund, 2007, pp. 401–425
  URL: <https://www.imf.org/External/Pubs/FT/staffp/2006/04/pdf/celasun.pdf>
* [36]
  Sulkhan Chavleishvili and Emanuel Moench
  “Natural disasters as macroeconomic tail risks”
  In *Journal of Econometrics* 247, 2025, pp. 105914
  DOI: [10.1016/j.jeconom.2024.105914](https://dx.doi.org/10.1016/j.jeconom.2024.105914)
* [37]
   Croatian National Bank
  “Macroprudential Diagnostics”, 2021
  URL: <https://www.hnb.hr/c/document_library/get_file?uuid=3d451468-6695-3c63-883a-d9034aa98840&groupId=20182&p_auth=wXmtUhZ6>
* [38]
   Croatian National Bank
  “Financial Stability 26”, 2025
  URL: <https://www.hnb.hr/c/document_library/get_file?uuid=f7daec4b-6d1a-1190-b5f6-c7dcb1359dd0&groupId=20182&p_auth=HtSfWp0r>
* [39]
   Croatian National Bank
  “Macroeconomic Developments and Outlook”, 2025
  URL: <https://www.hnb.hr/c/document_library/get_file?uuid=b80ea79c-1fd4-3ebc-77cd-3ac49811b712&groupId=20182&p_auth=HtSfWp0r#page=65.17>
* [40]
  M. Deskar-Škrbić and D. Milutinović
  “Design of fiscal consolidation packages and model-based fiscal multipliers in Croatia”
  In *Public Sector Economics* 45.1, 2021, pp. 1–61
  DOI: [https://doi.org/10.3326/pse.45.1.1](https://dx.doi.org/https://doi.org/10.3326/pse.45.1.1)
* [41]
  A. Evgenidis, M. Hamano and W. Vermeulen
  “Economic consequences of follow-up disasters: Lessons from the 2011 Great East Japan Earthquake”
  In *Energy Economics* 104, 2021, pp. 105559
  DOI: [10.1016/j.eneco.2021.105559](https://dx.doi.org/10.1016/j.eneco.2021.105559)
* [42]
  T. Fomby, Y. Ikeda and N.. Loayza
  “The growth aftermath of natural disasters”
  In *Journal of Applied Econometrics* 28.3, 2013, pp. 412–434
  URL: <https://www.jstor.org/stable/43907505>
* [43]
  D. Galinec and T. Kandžija
  “The Impact of Stock-flow Adjustments on Changes in Croatian General Government Debt Level”
  In *Journal of Economy and Business*
  Mostar Faculty of Economics, 2018, pp. 214–227
  DOI: [10.46458/27121097.2018.SI.214](https://dx.doi.org/10.46458/27121097.2018.SI.214)
* [44]
  A.. Grosu
  “Public Debt Sustainability in Post-200 EU Member States With Euro Adoption: A Penalized Spline Regression Approach”
  In *Revista Economică* 77.1, 2025, pp. 69–84
  DOI: [10.56043/reveco-2025-0006](https://dx.doi.org/10.56043/reveco-2025-0006)
* [45]
  K. Guo et al.
  “Energy trade stability of China: Policy options with increasing climate risks”
  In *Energy Policy* 184, 2024, pp. 113858
  DOI: [10.1016/j.enpol.2023.113858](https://dx.doi.org/10.1016/j.enpol.2023.113858)
* [46]
  Stefan Hochrainer
  “Assessing the macroeconomic impacts of natural disasters: Are there any?”
  In *Policy Research Working Paper Series*, 2009
  URL: <https://pure.iiasa.ac.at/id/eprint/9010/1/XO-09-035.pdf>
* [47]
   International Monetary Fund
  “Staff Guidance Note for Public Debt Sustainability Analysis in Market-Access Countries” IMF Policy Paper, 2013
  URL: <https://www.imf.org/external/np/pp/eng/2013/050913.pdf>
* [48]
   International Monetary Fund
  “Eastern Caribbean Currency Union: Regional Disaster Resilience Strategy”, 2019
  URL: <https://www.bing.com/ck/a?!&&p=0e05d44ae0b60e12d1769d7117db1d5e936d63ee90b05fb904f7cdf0c78ba070JmltdHM9MTc1ODQ5OTIwMA&ptn=3&ver=2&hsh=4&fclid=2b9f6261-92e6-69c9-36a8-740893be68ad&psq=International+Monetary+Fund.+(2019a).+Eastern+caribbean+currency+union%3a+Regional+disaster+resilience+strategy&u=a1aHR0cHM6Ly93d3cuaW1mLm9yZy8tL21lZGlhL0ZpbGVzL1B1YmxpY2F0aW9ucy9DUi8yMDE5LzFFQ0NFQTIwMTkwMDIuYXNoeA>
* [49]
   IPCC
  “Summary for Policymakers”
  In *Climate Change 2021: The Physical Science Basis. Contribution of Working Group I to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change*
  Cambridge, UKNew York, NY, USA: Cambridge University Press, 2021, pp. 3–32
  DOI: [10.1017/9781009157896.001](https://dx.doi.org/10.1017/9781009157896.001)
* [50]
  Ò. Jordà
  “Estimation and Inference of Impulse Responses by Local Projections”
  In *American Economic Review* 95.1, 2005, pp. 161–182
  DOI: [10.1257/0002828053828518](https://dx.doi.org/10.1257/0002828053828518)
* [51]
  Roger Koenker and Gilbert Bassett
  “Regression Quantiles”
  In *Econometrica* 46.1, 1978, pp. 33–50
  URL: <https://www.econometricsociety.org/publications/econometrica/1978/01/01/regression-quantiles>
* [52]
  Ricardo Marto, Chris Papageorgiou and Vladimir Klyuev
  “Building Resilience to Natural Disasters: An Application to Small Developing States”, 2019
  URL: <https://www.bing.com/ck/a?!&&p=46f0fb92bdfcb2a484fb9c8c7235d3b2128d785a892bffca79354af9fca48ec3JmltdHM9MTc1ODQ5OTIwMA&ptn=3&ver=2&hsh=4&fclid=2b9f6261-92e6-69c9-36a8-740893be68ad&psq=Ricardo+Marto+and+Chris+Papageorgiou+and+Vladimir+Klyuev+Building+Resilience+to+Natural+Disasters%3a+An+Application+to+Small+Developing+States%7d%2c&u=a1aHR0cHM6Ly93d3cuaW1mLm9yZy9-L21lZGlhL0ZpbGVzL1B1YmxpY2F0aW9ucy9XUC8yMDE3L3dwMTcyMjMuYXNoeA>
* [53]
  Ha Minh Nguyen, Alan Feng and Mercedes Garcia-Escribano
  “Understanding the Macroeconomic Effects of Natural Disasters”, 2025
  URL: <https://www.bing.com/ck/a?!&&p=e4ad0749e7c01c72bf1560f9bcf48440fd538d5a7b65e9cf712a8dce45572385JmltdHM9MTc1ODQ5OTIwMA&ptn=3&ver=2&hsh=4&fclid=2b9f6261-92e6-69c9-36a8-740893be68ad&psq=nguyen%2c+H.%2c+%26+colleagues.+(2025).+Natural+disasters%2c+output+losses%2c+and+debt+d&u=a1aHR0cHM6Ly93d3cuaW1mLm9yZy8tL21lZGlhL0ZpbGVzL1B1YmxpY2F0aW9ucy9XUC8yMDI1L0VuZ2xpc2gvd3BpZWEyMDI1MDQ2LXByaW50LXBkZi5hc2h4>
* [54]
  Ilan Noy
  “The macroeconomic consequences of disasters”
  In *Journal of Development Economics* 88.2, 2009, pp. 221–231
  DOI: [10.1016/j.jdeveco.2008.02.005](https://dx.doi.org/10.1016/j.jdeveco.2008.02.005)
* [55]
   OECD and The World Bank
  “Fiscal Resilience to Natural Disasters: Lessons from Country Experiences”, 2019
  DOI: [10.1787/27a4198a-en](https://dx.doi.org/10.1787/27a4198a-en)
* [56]
  L. Srdelic and M. Davila-Fernandez
  “International trade and economic growth in Croatia”
  In *Structural Change and Economic Dynamics* 68.1, 2024, pp. 240–258
  DOI: [10.1016/j.strueco.2023.10.018](https://dx.doi.org/10.1016/j.strueco.2023.10.018)
* [57]
  K. Taniguchi
  “Why Fukushima? A diachronic and multilevel comparative institutional analysis of a nuclear disaster”
  In *Energy Policy* 167, 2022, pp. 113049
  DOI: [10.1016/j.enpol.2022.113049](https://dx.doi.org/10.1016/j.enpol.2022.113049)
* [58]
   Vujčić, B.
  “From Pandemics to the Unconventional Monetary Policy in EMs: The Case of Croatia”
  In *Real and Financial Sectors in Post-Pandemic Central and Eastern Europe: The Impact of Economic, Monetary, and Fiscal Policy*
  Switzerland: Springer, 2022, pp. 1–9
  DOI: [10.1007/978-3-030-99850-9\_1](https://dx.doi.org/10.1007/978-3-030-99850-9_1)