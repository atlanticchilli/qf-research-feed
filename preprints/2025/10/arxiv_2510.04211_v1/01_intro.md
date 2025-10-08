---
authors:
- Lesya Kolinets
- Vygintas Gontis
doc_id: arxiv:2510.04211v1
family_id: arxiv:2510.04211
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Panel regression for the GDP of the Central and Eastern European countries
  using time-varying coefficients
url_abs: http://arxiv.org/abs/2510.04211v1
url_html: https://arxiv.org/html/2510.04211v1
venue: arXiv q-fin
version: 1
year: 2025
---


Lesya Kolinets
Vilnius Gediminas Technical University (VILNIUS TECH), Lithuania.
  
ORCID: [0000-0002-7005-0519](https://orcid.org/0000-0002-7005-0519)
  
lesya.kolinets@vilniustech.lt

Vygintas Gontis
Corresponding author: vygintas@gontis.eu
Institute of Lithuanian Scientific Society, J. Basanavičiaus 6, Vilnius, Lithuania.
  
ORCID: [0000-0002-1859-1318](https://orcid.org/0000-0002-1859-1318)
Institute of Theoretical Physics and Astronomy, Vilnius University,
Saulėtekio al. 3, 10257 Vilnius, Lithuania

###### Abstract

The integration of Central and Eastern European (CEE) countries into the European Economic Area serves as a valuable experiment for the regional economic development theory. The long-lasting convergence of these economies with more advanced Western Europe exhibits a few standard features and varying policies implemented. Even the Baltic countries, which started from very similar starting positions, demonstrate their unique trajectories of development.
We employ a panel data regression model that allows coefficients to vary over time to compare the contributions of a few macroeconomic factors to the GDP growth of CEE countries. In particular, we regress the annual change of GDP per capita in PPP terms as a function of achieved GDP, price, trade, investment, and debt levels. Time-varying common slope coefficients in this approach describe the external economic environment in which countries implement their own policies. The panel consists of 11 Central and Eastern European countries (Bulgaria, Czechia, Estonia, Croatia, Latvia, Lithuania, Hungary, Poland, Romania, Slovenia, and Slovakia), which have been observed annually from 1995 to 2024. While the main selected factors of this investigation contribute to economic growth, in agreement with previous findings, the role of private debt appears vital in determining the pace of economic growth.

## 1 Introduction

Central and Eastern Europe (CEE) demonstrates one of the most rapid income catch-up episodes observed in the accession process to the EU and participation in global value chains, joining other organizations of economic cooperation [[1](https://arxiv.org/html/2510.04211v1#bib.bib1), [2](https://arxiv.org/html/2510.04211v1#bib.bib2)]. Nevertheless, the transformation of CEE countries remains heterogeneous, and the comparison of their economic success has exceptional value for the further development of economic growth theory. During transition, a key feature of CEE economies was the lack of domestic capital, technologies, and expertise. Gomulka [[3](https://arxiv.org/html/2510.04211v1#bib.bib3)] introduced and actively used the concept of Technological Frontier Area (TFA). He used TFA to explain the global economic ’duality’ of the 20th century: countries that were on the technological frontier (developed economies with high innovation capacity) and countries that remained outside it (including the countries of Central and Eastern Europe at the beginning of their transformation). Gomułka clearly states that Central and Eastern Europe started transitional reforms outside the TFA due to a lack of capital, technology, and knowledge, and that only integration into European markets and the attraction of foreign investment paved the way for convergence with the technological frontier. Nölke and Vliegenthart [[4](https://arxiv.org/html/2510.04211v1#bib.bib4)] characterised this model as a "dependent market economy, emphasising the central role of FDI in the transformation of the region. According to the Washington Consensus, these countries should primarily attract foreign direct investment (FDI), which is the primary driver of economic growth and the development of capitalist institutions [[5](https://arxiv.org/html/2510.04211v1#bib.bib5)].

Comparing economic growth and explaining observed diversity are challenges for theorists and practitioners. Economists aim to comprehend the variation in growth rates among different countries and across various historical periods within the same country or region. The comparison of the interwar years with the period of regained independence of the Baltic countries attracts the interest of researchers and policymakers [[6](https://arxiv.org/html/2510.04211v1#bib.bib6)]. The theory and practice of comparing economic development on a global scale are continually evolving through the efforts of various reputable research groups. Maddison‐style estimates of the evolution of the world economy are in permanent development by the Maddison Project Database (MPD) [[7](https://arxiv.org/html/2510.04211v1#bib.bib7)]. One should consider this in close connection with the theory and practice of real GDP comparisons across countries and over time, as outlined in the Penn World Tables (PWT) [[8](https://arxiv.org/html/2510.04211v1#bib.bib8)]. These leading sources of economic growth information are based on global comparisons of long-run GDP per capita estimates, converting national income estimates from a national currency basis to a common currency using purchasing power parities (PPPs). The primary worldwide data sources and smaller economic growth research and projection groups accept the methodology. Thus, the available data from various sources is comparable, and one can use sources such as the World Bank (WB) Data, International Monetary Fund’s World Economic Outlook (IMF WEO), OECD, Eurostat, and others. Economic growth modeling and long-term projections of the global economy using historical data extend to the year 2050 [[9](https://arxiv.org/html/2510.04211v1#bib.bib9)]. The International Monetary Fund’s World Economic Outlook Database, April 2025, provides the most reliable economic growth projections up to 2030.

Available data for comparing GDP per capita among CEE countries confirms rapid convergence with Western Europe [[1](https://arxiv.org/html/2510.04211v1#bib.bib1), [2](https://arxiv.org/html/2510.04211v1#bib.bib2)]. Nevertheless, the diversity of convergence speed raises many questions and requires more specific explanations. Recent research has explored a range of macroeconomic factors influencing GDP growth, including those highlighted in the CEE context: price level, foreign direct investment (FDI), trade openness, capital formation, and private and public debt. These studies typically employ multi-country panel regressions to identify robust growth determinants in both developed and developing economies.

The Penn–Balassa–Samuelson mechanism provides a structural rationale for including the Price Level Index in growth regressions for catching-up economies. Higher tradable-sector productivity raises wages across the economy, pushing up the prices of nontradables and the aggregate price level. Classic and subsequent empirical contributions for CEE document this channel and its link to real convergence [[10](https://arxiv.org/html/2510.04211v1#bib.bib10), [11](https://arxiv.org/html/2510.04211v1#bib.bib11), [12](https://arxiv.org/html/2510.04211v1#bib.bib12)]. Incorporating price levels helps identify whether observed growth is associated with healthy productivity-driven revaluation or with overheating that erodes competitiveness [[13](https://arxiv.org/html/2510.04211v1#bib.bib13)]. An empirical study by He [[14](https://arxiv.org/html/2510.04211v1#bib.bib14)] suggests that the growth-maximizing inflation rate may be relatively low ( 3–5%), beyond which the marginal effect on growth turns negative. To account for the impact of price level, we incorporate it into the model. This approach aligns with other growth analyses for EU and transition countries, which treat inflation as a key conditioning variable for sustainable growth [[15](https://arxiv.org/html/2510.04211v1#bib.bib15)]. Notably, a 2025 study on EU economies finds that high inflation (and especially inflation volatility) has an adverse impact on growth prospects [[16](https://arxiv.org/html/2510.04211v1#bib.bib16)]. Some studies examine price level convergence (the equalization of price indices between countries) alongside income convergence. They conclude that poorer EU countries often had lower price levels to begin with and experienced faster inflation as they caught up with more advanced [[17](https://arxiv.org/html/2510.04211v1#bib.bib17)]. The findings of Armendariz et al. [[12](https://arxiv.org/html/2510.04211v1#bib.bib12)] suggest that real price level appreciation is not inherently harmful, but becomes problematic when it exceeds productivity growth, creating a wedge that undermines competitiveness and slows down economic convergence. Thus, ensuring alignment between price levels and productivity is critical for sustaining long-term growth in open, export-driven economies.

It is widely accepted that FDI catalyzes economic growth. New empirical evidence confirms a positive FDI-growth nexus, especially when FDI brings technology and productivity gains. A study conducted on a sample of 90 middle-income countries over the period 1990–2020 shows that a 1% increase in foreign direct investment inflows is associated with an average GDP growth of 9.3% [[18](https://arxiv.org/html/2510.04211v1#bib.bib18)]. This positive effect of FDI is explained, in particular, by the transfer of modern technologies, managerial know-how, and growth in total factor productivity in recipient countries. Similar results have been obtained in studies on Central and Eastern European countries, where FDI inflows contributed to capital accumulation and productivity growth, which ensured the restructuring of industries and modernization of the economy [[19](https://arxiv.org/html/2510.04211v1#bib.bib19), [20](https://arxiv.org/html/2510.04211v1#bib.bib20)]. In Central Europe, FDI has been a key driver of manufacturing sector reform and productivity gains, which in turn have contributed to economic convergence processes with more developed EU economies. Moreover, panel data evidence from 11 CEE countries (2003–2016) suggests the FDI-growth relationship may be nonlinear, with diminishing returns at very high FDI levels [[21](https://arxiv.org/html/2510.04211v1#bib.bib21)]. It is important to note that the FDI-growth link can depend on the host country’s conditions.

Openness to trade is another key determinant of economic growth. Open economies benefit from specialization, efficiency gains, and the diffusion of innovation through trade. Empirical research reaffirms that trade liberalization and export orientation foster long-run growth by expanding market access and intensifying competitive pressures [[22](https://arxiv.org/html/2510.04211v1#bib.bib22), [23](https://arxiv.org/html/2510.04211v1#bib.bib23), [24](https://arxiv.org/html/2510.04211v1#bib.bib24)]. In the EU context, trade openness has been linked to higher productivity and income levels [[25](https://arxiv.org/html/2510.04211v1#bib.bib25)].

Gross Capital Formation (GCF) serves as a proxy for domestic investment in fixed assets and infrastructure. High level of capital formation leads to an increase in productivity that promotes economic growth [[26](https://arxiv.org/html/2510.04211v1#bib.bib26), [27](https://arxiv.org/html/2510.04211v1#bib.bib27)].
A study on OECD countries (2000–2020) finds a significant positive impact of domestic investment on GDP growth, with robust cointegration between gross fixed capital formation and GDP [[28](https://arxiv.org/html/2510.04211v1#bib.bib28)]. In fact, a long-term causality was confirmed – meaning increases in investment precede and help cause long-run increases in output. Nexus of capital formation and growth aligns with the standard Solow growth model and endogenous growth theories: more capital per worker raises productivity and potential output. Cross-country analyses show that the growth payoff from investment is generally high in high-income and emerging economies. For instance, a global panel study by Topçu [[29](https://arxiv.org/html/2510.04211v1#bib.bib29)] using data on 124 countries reports that in high-income countries, gross capital formation has a significant positive effect on economic growth. The same study finds that for middle-income countries, capital formation also supports growth.

Government debt assesses fiscal sustainability and its implications for growth. The relationship between public debt and economic growth is complex and often nonlinear. At moderate levels, debt can finance productive public investments in infrastructure, education, and other areas that support growth. However, excessive public debt tends to be detrimental to economic growth [[30](https://arxiv.org/html/2510.04211v1#bib.bib30), [31](https://arxiv.org/html/2510.04211v1#bib.bib31), [32](https://arxiv.org/html/2510.04211v1#bib.bib32)] and has a significantly adverse effect on growth [[33](https://arxiv.org/html/2510.04211v1#bib.bib33), [34](https://arxiv.org/html/2510.04211v1#bib.bib34)]. For example, a recent panel study of 127 developing countries (2012–2019) finds that public debt "is not friendly to economic growth" and in fact hinders growth, especially at higher quantiles of debt levels [[30](https://arxiv.org/html/2510.04211v1#bib.bib30)]. In the Baltic States, public debt levels have historically been relatively low (thanks to prudent fiscal policies), but debt is still a critical indicator to monitor. Including public debt in the analysis enables us to consider the potential impact of fiscal imbalances on economic growth. An inverse relationship is expected, whereby higher levels of public debt (especially in cases of excessive growth) are associated with slower economic growth. The expected inverse relationship is consistent with the argument that maintaining sound public finances and debt obligations at an acceptable level is a crucial factor for long-term growth.

Private debt, which encompasses the liabilities of households and non-financial corporations, is central to contemporary discussions on sustainable economic development. The experience of the global financial crisis, the subsequent credit expansions in emerging markets, and recent shocks, including the COVID-19 pandemic, have highlighted the need for a deeper understanding of how private debt interacts with key macroeconomic indicators.
A consistent empirical finding is that high public debt tends to be associated with slower economic growth [[30](https://arxiv.org/html/2510.04211v1#bib.bib30)]. Verner documents [[35](https://arxiv.org/html/2510.04211v1#bib.bib35)] that large private debt booms tend to yield more costs, financial instability, and misallocations than benefits for the real economy over time. These findings align with earlier evidence of a debt threshold beyond which credit harms growth. For example, one cross-country study using data up to 2021 estimates the threshold for total private debt at roughly 125–150% of GDP, above which additional debt has an adverse growth effect [[36](https://arxiv.org/html/2510.04211v1#bib.bib36)]. Dinh et al. [[37](https://arxiv.org/html/2510.04211v1#bib.bib37)], analyzing lower-middle-income countries, find that private sector credit expansion initially hinders growth; however, in the long run, credit to the private sector is among the drivers of growth. In their study, a high credit-to-GDP ratio initially predicted a slowdown (often due to financial instability or resource misallocation).
In contrast, over a longer horizon, the deepening of credit markets supported growth once economies adjusted. Overall, the nexus of private debt and economic growth is complex. While access to credit is vital for economic activity, an over-leveraged private sector debt can undermine growth through financial crises, debt overhang, and reduced future consumption.

The panel data regression model that allows coefficients to vary over time approach was introduced by Hastie and Tibshirani [[38](https://arxiv.org/html/2510.04211v1#bib.bib38)] in the context of varying-coefficient models and further developed by Fan and Zhang [[39](https://arxiv.org/html/2510.04211v1#bib.bib39)], among others, to allow regression coefficients to "vary systematically" with an index variable. Li, Chen, and Gao [[40](https://arxiv.org/html/2510.04211v1#bib.bib40)] propose nonparametric time-varying coefficient panel models with fixed effects. In their framework, the time-varying slopes are estimated using kernel-weighted least squares after controlling for fixed effects. Wang et al. [[41](https://arxiv.org/html/2510.04211v1#bib.bib41)] introduce a panel data model with time-varying interactive fixed effects, where both the regression coefficients and latent factor loadings can smoothly change over time. Their approach employs kernel smoothing techniques to estimate the time paths of coefficients consistently and provides asymptotic theory for inference on these evolving parameters. Such models are well-suited to macroeconomic panels where unobservable common factors (e.g., global shocks) and policy effects may shift gradually. Similarly, nonparametric and semiparametric varying-coefficient models have matured. Atak et al. [[42](https://arxiv.org/html/2510.04211v1#bib.bib42)] find that a model allowing homogeneous time-varying coefficients fits better than one with fixed coefficients.
Other contributions have extended varying-coefficient panels to accommodate latent group structures, clustering units with similar coefficient paths, and spatial effects. For example, Dong et al. [[43](https://arxiv.org/html/2510.04211v1#bib.bib43)] and Chang et al. [[44](https://arxiv.org/html/2510.04211v1#bib.bib44)] incorporate time-varying coefficients into spatial autoregressive panels.
Several studies have revisited convergence and growth models with time-varying parameters. Desli and Gkoulgkoutsika, in a continuation of their convergence research, construct a stochastic convergence index that varies over time, effectively measuring how the speed of convergence has changed in response to global economic events [[45](https://arxiv.org/html/2510.04211v1#bib.bib45)].

We employ the linear regression with varying coefficients (LRVC) method for analyzing CEE economic growth. In section [2](https://arxiv.org/html/2510.04211v1#S2 "2 The time-varying coefficient panel model ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients") we present the LRVC method. In Section [3](https://arxiv.org/html/2510.04211v1#S3 "3 Empirical data ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients"), we describe the data used and its sources, and in the following section [4](https://arxiv.org/html/2510.04211v1#S4 "4 Results ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients"), we provide our results. Finally, we discuss and conclude our research in the section [5](https://arxiv.org/html/2510.04211v1#S5 "5 Discussion and conclusions ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients").

## 2 The time-varying coefficient panel model

We employ a panel data regression model that allows coefficients to vary over time. In particular, we model GDP per capita (in purchasing power parity, or PPP, terms) as a function of several economic factors with time-varying slope coefficients. The panel consists of 11 Central and Eastern European countries (Bulgaria, Czechia, Estonia, Croatia, Latvia, Lithuania, Hungary, Poland, Romania, Slovenia, and Slovakia), which have been observed annually from 1995 to 2024.

A panel model with variable coefficients allows us to capture structural changes and the evolution of relationships over the period 1996–2024 [[42](https://arxiv.org/html/2510.04211v1#bib.bib42)]. Such an approach is essential for the transition economies of the CEE region, which have undergone significant transformations, including accession to the European Union in the 2000s and the global financial crisis of 2008. Transformation events have potentially changed the nature of the impact of key factors on economic growth, making the use of models with time-dependent parameters particularly relevant.

For the comparison of GDP dynamics among the CEE countries, we use a time-varying linear regression coefficient panel.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​yi,t=αt+∑j=1dβt−1,j​xi,t−1,j+ei,t,i=1,…,N,t=1,…,T\Delta y\_{i,t}=\alpha\_{t}+\sum\_{j=1}^{d}\beta\_{t-1,j}x\_{i,t-1,j}+e\_{i,t},\qquad i=1,...,N,\quad t=1,...,T |  | (1) |

where Δ​yi,t\Delta y\_{i,t} represents GDP/pc annual change in country ii, at year tt, 𝒙i,t−1\bm{x}\_{i,t-1} is the vector of dd regressed variables, and the vector 𝜷t={βt,1,…,βt,d}\bm{\beta}\_{t}=\{\beta\_{t,1},...,\beta\_{t,d}\} represents linear time-varying regression coefficients. The error process we denote as {ei,t}\{e\_{i,t}\}. In this research, we will use seven regressed variables: X1 - GDP per capita in PPP, X2 - Price level index, X3 - Accumulated foreign direct investment, X4 - Trade, X5 - Accumulated gross capital formation, X6 - Central Government debt, and X7 - Private debt. The data description follows. This data we use to get matrix 𝒙\bm{x}, for the eleven countries, 29 time steps {1995,….,2023}\{1995,....,2023\}, and seven, d=7d=7, economic growth financial components X​jXj. We use the same data of GDP per capita in PPP to calculate the matrix 𝚫​𝒚\bm{\Delta y} for the 29 time intervals from 1995 to 2024 and the selected 11 countries.

We can calculate the time-varying regression coefficients βt−1,j\beta\_{t-1,j} and the vector 𝜶t\bm{\alpha}\_{t} common to all countries using panel least squares estimation. These empirically defined regression parameters can be used to evaluate the regressed 𝚫​𝒚\bm{\Delta y}, error terms {ei,t}\{e\_{i,t}\}, and the contribution of all components X​jXj to the Δ​y\Delta y defined as Δ​yi,t,j\Delta y\_{i,t,j}

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ​yi,t,j=αtd+βt−1,j​xi,t−1,j,Δ​yi,t=∑j=1dΔ​yi,t,j.\Delta y\_{i,t,j}=\frac{\alpha\_{t}}{d}+\beta\_{t-1,j}x\_{i,t-1,j},\qquad\Delta y\_{i,t}=\sum\_{j=1}^{d}\Delta y\_{i,t,j}. |  | (2) |

For a country ii and component jj, we will plot the GDP component dynamics

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ​(t)=κi,t,j=G​D​P1995/d+∑τ=1996tΔ​yi,t,j,\kappa(t)=\kappa\_{i,t,j}=GDP\_{1995}/d+\sum\_{\tau=1996}^{t}\Delta y\_{i,t,j}, |  | (3) |

and the relative contribution of private debt to the GDP is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | γi​(t)=s​g​n​(κi,t,7)​κi,t,72/∑j=1dκi,t,j2.\gamma\_{i}(t)=sgn(\kappa\_{i,t,7})\kappa\_{i,t,7}^{2}/\sum\_{j=1}^{d}\kappa\_{i,t,j}^{2}. |  | (4) |

We use three different estimates of Δ​yi,t\Delta y\_{i,t} seeking to evaluate the accuracy of the modeling. Empirical one Δ​yi,te=xi,t,1−xi,t−1,1\Delta y\_{i,t}^{e}=x\_{i,t,1}-x\_{i,t-1,1}, regressed one Δ​yi,tr=Δ​yi,t\Delta y\_{i,t}^{r}=\Delta y\_{i,t} calculated from the Eq. ([1](https://arxiv.org/html/2510.04211v1#S2.E1 "In 2 The time-varying coefficient panel model ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients")), and full regressed Δ​yi,tf​r\Delta y\_{i,t}^{fr}, when we replace in calculation all empirical values of xi,t−1,1x\_{i,t-1,1} by the accumulated values of Δ​yi,t\Delta y\_{i,t} obtained in previous time steps of estimation. It is evident that the error term in Eq. ([1](https://arxiv.org/html/2510.04211v1#S2.E1 "In 2 The time-varying coefficient panel model ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients")) can be expressed as ei,t=Δ​yi,tr−Δ​yi,tee\_{i,t}=\Delta y\_{i,t}^{r}-\Delta y\_{i,t}^{e}. The results of these three estimates we will illustrate as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | G​D​P​D​a​t​a​(t)\displaystyle GDPData(t) | =G​D​P1995+∑τ=1996tΔ​yi,τe,\displaystyle=GDP\_{1995}+\sum\_{\tau=1996}^{t}\Delta y\_{i,\tau}^{e}, |  | (5) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | G​D​P​R​e​g​r.(t)\displaystyle GDPRegr.(t) | =G​D​P1995+∑τ=1996tΔ​yi,τr,\displaystyle=GDP\_{1995}+\sum\_{\tau=1996}^{t}\Delta y\_{i,\tau}^{r}, |  | (6) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | G​D​P​R​e​g​r.F​u​l​l​(t)\displaystyle GDPRegr.Full(t) | =G​D​P1995+∑τ=1996tΔ​yi,τf​r,\displaystyle=GDP\_{1995}+\sum\_{\tau=1996}^{t}\Delta y\_{i,\tau}^{fr}, |  | (7) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ei,ta=∑τ=1996tei,τ\displaystyle e\_{i,t}^{a}=\sum\_{\tau=1996}^{t}e\_{i,\tau} | =G​D​P​R​e​g​r.(t)−G​D​P​D​a​t​a​(t)\displaystyle=GDPRegr.(t)-GDPData(t) |  | (8) |

## 3 Empirical data

Central and Eastern European countries experience rapid economic convergence with the rest of Europe [[1](https://arxiv.org/html/2510.04211v1#bib.bib1), [2](https://arxiv.org/html/2510.04211v1#bib.bib2)]. The convergence process follows the Penn Effect, explained by the Balassa-Samuelson hypothesis. The effect is comparatively well expressed for the EU countries, as shown in Fig. [1](https://arxiv.org/html/2510.04211v1#S3.F1 "Figure 1 ‣ 3 Empirical data ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients").

![Refer to caption](priceGDP-1995.png)

![Refer to caption](priceGDP-2024.png)

Figure 1: The price index and GDP/pc PPS scatter plot for the EU countries in 1995 and 2024. Red - CEE countries except those in the Baltic region, green - Baltic countries, blue - the rest of the EU countries. The line exhibits the least squares trend for all EU countries.

Nevertheless, this crucial catch-up process for the EU project varies significantly from one CEE country to another. It is very illustrative to follow how the economic ranking of the CEE countries changes from 1995 to 2030, according to the International Monetary Fund’s projected data [[46](https://arxiv.org/html/2510.04211v1#bib.bib46)], as shown in Fig. [2](https://arxiv.org/html/2510.04211v1#S3.F2 "Figure 2 ‣ 3 Empirical data ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients"). The ranking of Lithuania changes from tenth to first, as other countries exhibit considerable variation in their rankings as well. We aim to investigate the contribution of achieved GDP, price level, and other macroeconomic factors to economic growth, explaining the variable behavior of CEE countries compared to the Penn effect trend and their economic growth ranking.

For the panel regression described in the section [2](https://arxiv.org/html/2510.04211v1#S2 "2 The time-varying coefficient panel model ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients") we use following regressed variables - economic growth factors:
X1 - Volume indices of real expenditure per capita (in PPS EU27 2020 100). This data is available at Eurostat. Purchasing power parities (PPPs), price level indices, and real expenditures for ESA 2010 aggregates.
X2 - Price level indices (EU27 2020 100). Purchasing power parities (PPPs), price level indices, and real expenditures for ESA 2010 aggregates.
X3 - Foreign direct investment, net inflows (% of GDP), World Bank data. The data we use was accumulated in the period considered.
X4 - Trade (% of GDP). Trade is the sum of exports and imports of goods and services. World Bank data.
X5 - Gross capital formation (% of GDP). Gross capital formation includes acquisitions, less disposals, of produced assets for fixed capital formation, inventories, or valuables. World Bank data. The data we use is accumulated in the period considered.
X6 - Central Government Debt, Government deficit/surplus, debt and associated data (% of GDP), ESTAT data.
X7 - Private sector debt, consolidated - % of GDP [tipspd20]. Consolidated non-financial corporations, households, and non-profit institutions serving households, as per ESTAT data.

![Refer to caption](CEE-ranks.png)


Figure 2: The GDP/pc PPP rank change of the Central and Eastern European countries.

In this study, we pay particular attention to the comparison of Baltic countries, as they began European integration from a very similar level of development and shared the same political heritage. The Baltic countries, which experienced a similar pace of development at the beginning of the period, exhibit some divergence in the last interval of time (after the economic crises), as seen in the first sub-figure of Fig. [3](https://arxiv.org/html/2510.04211v1#S3.F3 "Figure 3 ‣ 3 Empirical data ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients"). We do expect to reveal macroeconomic factors responsible for the observed divergence.

![Refer to caption](GDP-Baltic.png)

![Refer to caption](PrivDebt-Baltic.png)

Figure 3: The comparison of Baltic countries. The first sub-figure compares GDP per capita in PPS, and the second one compares private debt, % of GDP.

## 4 Results

Although contemporary economic research investigators utilize a vast amount of data and sophisticated research methods, this study restricted itself to only seven macroeconomic factors of economic growth, as described in the previous section, and eleven countries from Central and Eastern Europe. Such conscious restriction may be helpful for the reasonable interpretation of results. Indeed, all countries under investigation undergo similar political and economic transformations as they join the European Economic Area and share many standard features of development. Thus, the linear regression with varying coefficients, as described in Section [1](https://arxiv.org/html/2510.04211v1#S2.E1 "In 2 The time-varying coefficient panel model ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients"), may be productive in comparing the contributions to economic growth of the seven selected macroeconomic and financial factors.

Seeking to evaluate the accuracy of the linear regression with time-varying coefficients method for our investigation, we compare three time series as defined in equations ([5](https://arxiv.org/html/2510.04211v1#S2.E5 "In 2 The time-varying coefficient panel model ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients")), ([6](https://arxiv.org/html/2510.04211v1#S2.E6 "In 2 The time-varying coefficient panel model ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients")), ([7](https://arxiv.org/html/2510.04211v1#S2.E7 "In 2 The time-varying coefficient panel model ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients")), see three sub-figures for the Baltic countries in Fig. [4](https://arxiv.org/html/2510.04211v1#S4.F4 "Figure 4 ‣ 4 Results ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients"). Errors accumulate slightly in the case of Latvia, but regression for Estonia and Lithuania yields a very accurate replication of the empirical economic growth series. For the other CEE countries, the time series behave similarly; we will provide more information in the following table.

The primary purpose of this research is to evaluate the contribution of seven factors to economic growth. We calculate component contributions using Eq. ([3](https://arxiv.org/html/2510.04211v1#S2.E3 "In 2 The time-varying coefficient panel model ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients")); see the results for the Baltic countries in Fig. [5](https://arxiv.org/html/2510.04211v1#S4.F5 "Figure 5 ‣ 4 Results ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients"). From a macroeconomic perspective, prices are the primary driver of economic growth. The role of prices is consistent with the Penn effect. The primary opposing force of economic growth is the achieved level of economic development, which is consistent with neoclassical and other economic growth models. The contribution of other factors is considerably lower; nevertheless, foreign direct investment is one of the main forces of growth for all the countries considered. The positive contribution of trade is considerable as well, but can be comparable to capital formation. The role of Centr. Government debt fluctuates from negative to positive and is probably more related to the government’s economic policy.

![Refer to caption](regress-Estonia.png)

![Refer to caption](regress-Latvia.png)

![Refer to caption](regress-Lithuania.png)

Figure 4: The comparison of regressed GDP’s for the Baltic countries with statistical data.

The primary outcome of this consideration is a sufficiently high negative contribution of private debt, as one can see from Fig. [5](https://arxiv.org/html/2510.04211v1#S4.F5 "Figure 5 ‣ 4 Results ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients") and the table below. The different private debt developments in the Baltic countries, as shown in the second sub-figure of Fig. [3](https://arxiv.org/html/2510.04211v1#S3.F3 "Figure 3 ‣ 3 Empirical data ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients"), may serve as one possible explanation for the differences in economic development. Private debt’s negative contributions to the development of Baltic countries are directly related to the achieved level of private debt, as shown in Fig. [5](https://arxiv.org/html/2510.04211v1#S4.F5 "Figure 5 ‣ 4 Results ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients"). The differences in other factors’ contributions are considerably lower; thus, our research can serve as evidence of a very negative contribution of private debt to the development of Estonia and Latvia in comparison with Lithuania. The particular role of private debt is also evident in other CEE countries, as can be observed from the table.

![Refer to caption](comp-Estonia.png)

![Refer to caption](comp-Latvia.png)

![Refer to caption](comp-Lithuania.png)

Figure 5: The comparison of component contributions to the GDPs of the Baltic countries.




Table 1: The component jj contributions to the GDP in year 2024, κi,2024,j\kappa\_{i,2024,j}, for the all CEE countries considered. The order of columns is according to the average value of the contribution X​iXi. Two additional columns: of as contributions’ sum, Total, and accumulated error term 𝒆𝒊,𝒕=𝟐𝟎𝟐𝟒𝒂\bm{e\_{i,t=2024}^{a}}, see Eq. ([8](https://arxiv.org/html/2510.04211v1#S2.E8 "In 2 The time-varying coefficient panel model ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients")), are included.

| Country | X2 | Total | X3 | X4 | X5 | X6 | X7 | X1 | 𝒆𝒊,𝒕=𝟐𝟎𝟐𝟒𝒂\bm{e\_{i,t=2024}^{a}} |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bulgaria | 142.95142.95 | 64.2164.21 | 64.2864.28 | 16.616.6 | −2.52-2.52 | 5.765.76 | −84.68-84.68 | −78.17-78.17 | 1.791.79 |
| Czechia | 206.19206.19 | 85.4485.44 | 57.3157.31 | 20.1520.15 | 9.739.73 | 14.5914.59 | −52.66-52.66 | −169.87-169.87 | 5.565.56 |
| Estonia | 202.67202.67 | 76.2676.26 | 45.2245.22 | 21.4121.41 | 4.924.92 | 21.321.3 | −93.0-93.0 | −130.8-130.8 | −0.79-0.79 |
| Croatia | 202.67202.67 | 76.2676.26 | 45.2245.22 | 21.4121.41 | 4.924.92 | −1.41-1.41 | −79.96-79.96 | −116.59-116.59 | 0.740.74 |
| Latvia | 185.93185.93 | 77.77. | 47.5647.56 | 14.9314.93 | −5.32-5.32 | 9.189.18 | −75.76-75.76 | −99.51-99.51 | −6.-6. |
| Lithuania | 174.4174.4 | 86.4786.47 | 42.742.7 | 13.8313.83 | 6.236.23 | 8.668.66 | −39.18-39.18 | −120.17-120.17 | 1.531.53 |
| Hungary | 181.55181.55 | 78.978.9 | 81.4581.45 | 16.5116.51 | 5.945.94 | −9.5-9.5 | −70.52-70.52 | −126.51-126.51 | −1.9-1.9 |
| Poland | 173.8173.8 | 79.479.4 | 44.0344.03 | 17.4717.47 | 7.127.12 | −0.51-0.51 | −41.31-41.31 | −121.2-121.2 | −0.4-0.4 |
| Romania | 144.45144.45 | 78.1678.16 | 41.8241.82 | 17.1117.11 | 1.231.23 | 10.7610.76 | −42.74-42.74 | −94.48-94.48 | −0.16-0.16 |
| Slovenia | 247.96247.96 | 89.9489.94 | 39.3139.31 | 19.5419.54 | 9.299.29 | 8.798.79 | −66.22-66.22 | −168.73-168.73 | 1.061.06 |
| Slovakia | 195.14195.14 | 76.4276.42 | 45.245.2 | 13.5113.51 | 5.935.93 | 4.284.28 | −48.34-48.34 | −139.31-139.31 | −1.42-1.42 |

We examine the specific impact of private debt on the economic growth of CEE countries, particularly in the post-crisis period, as illustrated in Eq. ([4](https://arxiv.org/html/2510.04211v1#S2.E4 "In 2 The time-varying coefficient panel model ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients")), which plots the relative contribution of private debt (see Fig. [6](https://arxiv.org/html/2510.04211v1#S4.F6 "Figure 6 ‣ 4 Results ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients")).

![Refer to caption](rel-contr-debt.png)


Figure 6: The relative contribution of private debt to the development of CEE countries γi​(t)\gamma\_{i}(t) as defined in Eq. [4](https://arxiv.org/html/2510.04211v1#S2.E4 "In 2 The time-varying coefficient panel model ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients"). The order of the legends in this Figure is descending according to the values given in column X7 of the Table [1](https://arxiv.org/html/2510.04211v1#S4.T1 "Table 1 ‣ 4 Results ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients").

From our perspective, the private debt contribution presented in Fig. [6](https://arxiv.org/html/2510.04211v1#S4.F6 "Figure 6 ‣ 4 Results ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients") and Table [1](https://arxiv.org/html/2510.04211v1#S4.T1 "Table 1 ‣ 4 Results ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients") explains many peculiarities of CEE economic development dynamics, as reflected in the empirical data and visualized in Fig. [2](https://arxiv.org/html/2510.04211v1#S3.F2 "Figure 2 ‣ 3 Empirical data ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients") by the rank change of countries.

## 5 Discussion and conclusions

We investigated the dynamics of economic growth in Central and Eastern Europe from the perspective of long-range macroeconomic processes. In this study, we employ the widely accepted Purchasing Power Parity methodology for international comparison. We use data from recognized, publicly available sources, allowing our results to be easily replicated. This panel research is restricted to N=11N=11 countries that have experienced accession to the European Union and have very similar external conditions for development. A smaller panel of Baltic countries shares the same heritage of political transformations and serves as a more specific interest of ours. The conscious decision to restrict the number of countries affects our choice to limit the number of macroeconomic regressors to d=7d=7 for this panel investigation, as d<Nd<N is a method requirement.

Many previous studies and our results confirm the rapid convergence of CEE countries with historically more advanced Western Europe, although the pace of this convergence varies considerably among the countries investigated. We aim to identify the most reliable macroeconomic factors that distinguish the speed of economic growth and convergence. The Baltic countries, which had demonstrated very similar trajectories of development before the 2008 global financial crisis, later significantly changed their directions. The impact of World crises is quantitatively evident in our investigation, confirming the necessity to use regression with varying coefficients. The development of Lithuania, as projected by the IMF WEO data, raises our specific interest in finding a reasonable explanation for this success.

Despite the limited number of investigated regressors, our results appear reliable, as the regressed GDPs (see Fig. [4](https://arxiv.org/html/2510.04211v1#S4.F4 "Figure 4 ‣ 4 Results ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients") and Table [1](https://arxiv.org/html/2510.04211v1#S4.T1 "Table 1 ‣ 4 Results ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients")) reproduce empirical data with reasonable precision. It is evident that the regressors (predictors) in this study are not independent; for example, capital formation is likely to be influenced by credit availability and private debt. Despite possible predictor collinearity, the method provides us with some additional insight into the dynamics of GDP. One has to keep in mind the difficulties in separating the individual effects of these variables when interpreting the results. More extensive empirical analysis of World economic growth data would be helpful in the development of the method. Nevertheless, our study leads to some new insights on the diversity of economic growth in CEE countries, which are worth further investigation and discussion.

The regression with varying coefficients described in Section [2](https://arxiv.org/html/2510.04211v1#S2 "2 The time-varying coefficient panel model ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients") provides us the decomposition of Δ​yi,t\Delta y\_{i,t} time series into the sub-series Δ​yi,t,j\Delta y\_{i,t,j} of d=7d=7 components: Achieved level of GDP, Price level, FDI, Trade, Gross capital formation, Central government debt, Private debt. The decompositions for all countries under investigation are qualitatively similar; see the example of the Baltic countries in Fig. [5](https://arxiv.org/html/2510.04211v1#S4.F5 "Figure 5 ‣ 4 Results ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients"). Results confirm previous findings that FDI, international trade, and capital formation are the main drivers of development. The contribution of governmental debt fluctuates quantitatively around zero and appears most positive for Estonia, which has the lowest government debt level. Thus, we suggest interpreting the quantitative contribution of components just as a relative estimate in comparison with other panel countries. The main quantitative contributions to GDP growth come from the positive effects of the achieved price level and the adverse effects of the achieved GDP level. It is in agreement with the Penn effect [[13](https://arxiv.org/html/2510.04211v1#bib.bib13)] and the classical Solow growth model [[47](https://arxiv.org/html/2510.04211v1#bib.bib47)].

The contribution of private debt appears to be negative for all countries, fluctuating from the highest for Lithuania, Poland, and Romania to the lowest for Estonia. The fluctuations in private debt contributions are the most considerable, varying by more than twice. Thus, we consider private debt to be the main determining factor of economic growth in CEE countries. To quantify and visualize the contribution of private debt, we introduced the parameter γi​(t)\gamma\_{i}(t) in Eq. [4](https://arxiv.org/html/2510.04211v1#S2.E4 "In 2 The time-varying coefficient panel model ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients") and plotted the results in Fig. [6](https://arxiv.org/html/2510.04211v1#S4.F6 "Figure 6 ‣ 4 Results ‣ Panel regression for the GDP of the Central and Eastern European countries using time-varying coefficients"). The importance of private debt grew significantly after the global financial crisis in 2008 and has become a key factor in economic success in CEE. We consider this result to be the main finding of our research. We will continue our investigation of economic growth data by applying more advanced methods and extending the scope to include additional countries and regions. It would be reasonable to extend the proposed method using Principal Component Analysis (PCA), incorporating more countries and additional predictors. From our perspective, it is valuable to consider the role of private debt in the broader theories of economic growth.

## 6 Abbreviations

The following abbreviations are used in this manuscript:

|  |  |
| --- | --- |
| CEE | Central and Eastern Europe |
| ESTAT | Eurostat |
| EU | European Union |
| FDI | Foreign direct investment |
| IMF | International Monetary Fund |
| GCF | Gross capital formation |
| GDP | Gross domestic product |
| MPD | Madison Project Database |
| PPP | Purchasing power parity |
| PPS | Purchasing power standards |
| PWT | Penn World Tables |
| TFA | Technological Frontier Area |
| WB | World Bank |
| WEO | World Economic Outlook |

## References

* [1]

  A.-M. Holobiuc, Income convergence in the european union: National and regional
  dimensions, Eur. Fin. Acc. J. 15 (2) (2020) 45–65.
* [2]

  S. Alemu, B. Udvari, B. Kotosz, Income convergence in central and eastern
  europe: Evidence from cross-country panel data analysis, Acta Oecon. 74 (3)
  (2024) 329–357.
* [3]

  S. Gomułka, Transformacja i rozwój. Teoria i polityka gospodarcza,
  Wydawnictwo Naukowe PWN, Warszawa, Polska, 2016.
* [4]

  A. Nölke, A. Vliegenthart, Enlarging the varieties of capitalism: The
  emergence of dependent market economies in east central europe, World Polit.
  61 (4) (2009) 670–702.
* [5]

  P. Maszczyk, M. Próchniak, R. Rapacki, Development trajectories in central
  and eastern european countries in 2004–2023 – sources of the institutional
  comparative advantage and their evolution in patchwork capitalism, in: Report
  of the SGH Warsaw School of Economics and the Economic Forum 2024, SGH
  Publishing House, 2024, pp. 15–52.
* [6]

  Z. Norkus, Post-communist transformations in Baltic countries, Springer Nature
  Switzerland, Cham, 2023.
* [7]

  J. Bolt, J. L. van Zanden, Maddison‐style estimates of the evolution of the
  world economy: A new 2023 update, J. Econ. Surv. 39 (2) (2025) 631–671.
* [8]

  R. Feenstra, R. Inklaar, M. Timmer, The next generation of the penn world
  table, Tech. rep., National Bureau of Economic Research, Cambridge, MA (Jul.
  2013).
* [9]

  L. Fontagné, E. Perego, G. Santoni, Long-term macroeconomic projections of
  the world economy, Int. Econ. 172 (2022) 168–189.
* [10]

  A. LojschovÃ¡,
  [Estimating the impact of
  the balassa-samuelson effect in transition economies](https://ideas.repec.org/p/ihs/ihsesp/140.html), Economics Series 140,
  Institute for Advanced Studies (Oct 2003).
  [doi:None](http://dx.doi.org/None).
    
  URL <https://ideas.repec.org/p/ihs/ihsesp/140.html>
* [11]

  D. Mihaljek, M. Klau, [The
  balassa-samuelson effect in central europe: a disaggregated analysis](https://ideas.repec.org/p/bis/biswps/143.html), BIS
  Working Papers 143, Bank for International Settlements (Oct 2003).
  [doi:None](http://dx.doi.org/None).
    
  URL <https://ideas.repec.org/p/bis/biswps/143.html>
* [12]

  S. Armendariz, Competitiveness and productivity in the baltics, IMF Work. Pap.
  2025 (018) (2025) 1.
* [13]

  F. Hassan, The price of development: The Penn–Balassa–Samuelson effect
  revisited, J. Int. Econ. 102 (2016) 291–309.
* [14]

  Q. He, The inverted-u effect of inflation on growth: Cross-country evidence,
  Econ. Model. 128 (106501) (2023) 106501.
* [15]

  R. J. Barro,
  [Inflation
  and economic growth](https://ideas.repec.org/a/cuf/journl/y2013v14i1n6barro.html), Annals of Economics and Finance 14 (1) (2013) 121–144.
  [doi:None](http://dx.doi.org/None).
    
  URL <https://ideas.repec.org/a/cuf/journl/y2013v14i1n6barro.html>
* [16]

  A. Pappas, N. Boukas, Examining impact of inflation and inflation volatility on
  economic growth: Evidence from european union economies, Economies 13 (2)
  (2025) 31.
* [17]

  J. H. Rogers, Monetary union, price level convergence, and inflation: How close
  is europe to the USA?, J. Monet. Econ. 54 (3) (2007) 785–796.
* [18]

  H. T. P. Le, H. Pham, N. T. T. Do, K. D. Duong, Foreign direct investment,
  total factor productivity, and economic growth: evidence in middle-income
  countries, Humanit. Soc. Sci. Commun. 11 (1).
* [19]

  A. Acaravci, I. Ozturk,
  [Foreign
  direct investment, export and economic growth: Empirical evidence from new eu
  countries](https://ideas.repec.org/a/rjr/romjef/vy2012i2p52-67.html), Journal for Economic Forecasting 0 (2) (2012) 52–67.
  [doi:None](http://dx.doi.org/None).
    
  URL <https://ideas.repec.org/a/rjr/romjef/vy2012i2p52-67.html>
* [20]

  G. Popescu, FDI and economic growth in central and eastern europe,
  Sustainability 6 (11) (2014) 8149–8163.
* [21]

  S. C. Gherghina, L. N. Simionescu, O. S. Hudea, Exploring foreign direct
  investment–economic growth nexus—empirical evidence from central and
  eastern european countries, Sustainability 11 (19) (2019) 5421.
* [22]

  D. Rodrik, Populism and the economics of globalization, J. Int. Bus. Pol.
  1 (1-2) (2018) 12–33.
* [23]

  M. Dritsaki, Trade openness and economic growth: A panel data analysis of
  baltic countries, Asian Econ. Fin. Rev. 10 (3) (2020) 313–324.
* [24]

  M. J. Spahiu, B. J. Spahiu, The factors influencing gross domestic product
  growth in the post-pandemic period: The case of kosovo, J. Lib. Int. Aff.
  8 (2) (2022) 136–149.
* [25]

  A. Dornean, D.-C. Oanea, Impact of the economic crisis on FDI in central and
  eastern europe, Rev. Econ. Bus. Stud. 8 (2) (2015) 53–68.
* [26]

  N. Onyinye, O. Idenyi, A. Ifeyinwa, Effect of capital formation on economic
  growth in nigeria, Asian J. Econ. Bus. Account. 5 (1) (2017) 1–16.
* [27]

  A. Aslan, B. Altinoz, The impact of natural resources and gross capital
  formation on economic growth in the context of globalization: evidence from
  developing countries on the continent of europe, asia, africa, and america,
  Environ. Sci. Pollut. Res. Int. 28 (26) (2021) 33794–33805.
* [28]

  F. Morina, V. Misiri, F. Gashi, Long-term relationship between investment and
  economic growth: a cointegration analysis of OECD countries, Eur. J. Gov.
  Econ. 12 (2) (2023) 175–195.
* [29]

  E. Topcu, B. Altinoz, A. Aslan, Global evidence from the link between economic
  growth, natural resources, energy consumption, and gross capital formation,
  Resour. Policy 66 (101622) (2020) 101622.
* [30]

  Y. M. V. Mudayen, L. Arsyad, R. Pradiptyo, S. U. Setiastuti, Does public debt
  encourage economic growth? an application of quantile regressions to panel
  data for developing countries, Economies 13 (4) (2025) 113.
* [31]

  D. Asteriou, K. Pilbeam, C. E. Pratiwi, Public debt and economic growth: panel
  data evidence for asian countries, J. Econ. Fin. 45 (2) (2021) 270–287.
* [32]

  K. Musa, K. Sohag, J. Said, F. Ghapar, N. Ali, Public debt, governance, and
  growth in developing countries: An application of quantile via moments,
  Mathematics 11 (3) (2023) 650.
* [33]

  C. Reinhart, K. Rogoff,
  [Debt and growth
  revisited](https://ideas.repec.org/p/pra/mprapa/24376.html), MPRA Paper 24376, University Library of Munich, Germany (Aug
  2010).
  [doi:None](http://dx.doi.org/None).
    
  URL <https://ideas.repec.org/p/pra/mprapa/24376.html>
* [34]

  C. Checherita-Westphal, P. Rother, The impact of high government debt on
  economic growth and its channels: An empirical investigation for the euro
  area, Eur. Econ. Rev. 56 (7) (2012) 1392–1405.
* [35]

  E. Verner, Private debt booms and the real economy: Do the benefits outweigh
  the costs?, SSRN Electron. J.
* [36]

  Y. Gu, J. Guo, X. Liang, Y. Zhao, Does the debt-growth link differ across
  private and public debt? evidence from china, Econ. Model. 114 (105930)
  (2022) 105930.
* [37]

  T. T.-H. Dinh, D. H. Vo, Anh The Vo, T. C. Nguyen, Foreign direct investment
  and economic growth in the short run and long run: Empirical evidence from
  developing countries, J. Risk Fin. Manag. 12 (4) (2019) 176.
* [38]

  T. Hastie, R. Tibshirani, Varying-coefficient models, J. R. Stat. Soc. Series B
  Stat. Methodol. 55 (4) (1993) 757–779.
* [39]

  J. Fan, W. Zhang, Statistical estimation in varying coefficient models, Ann.
  Stat. 27 (5) (1999) 1491–1518.
* [40]

  D. Li, J. Chen, J. Gao, Non‐parametric time‐varying coefficient panel data
  models with fixed effects, Econom. J. 14 (3) (2011) 387–408.
* [41]

  X. Wang, S. Jin, Y. Li, J. Qian, L. Su, On time-varying panel data models with
  time-varying interactive fixed effects, J. Econom. 249 (105960) (2025)
  105960.
* [42]

  A. Atak, T. Y. Tao, Y. Zhang, Q. Zhou, Specification tests for time-varying
  coefficient panel data models, Econ. Theory (2023) 1–48.
* [43]

  C. Dong, J. Gao, B. Peng, Varying-coefficient panel data models with
  nonstationarity and partially observed factor structure, J. Bus. Econ. Stat.
  39 (3) (2021) 700–711.
* [44]

  H.-Y. Chang, X. Song, J. Yu, Trending time-varying coefficient spatial panel
  data models, SSRN Electron. J.
* [45]

  E. Desli, A. Gkoulgkoutsika, World economic convergence: Does the estimation
  methodology matter?, Econ. Model. 91 (2020) 138–147.
* [46]

  International Monetary Fund,
  [World
  economic outlook update, july 2025: Global economy: Tenuous resilience amid
  persistent uncertainty](https://www.imf.org/en/Publications/WEO/Issues/2025/07/29/world-economic-outlook-update-july-2025), pDF available via “Full Report” link (Jul.
  2025).
    
  URL <https://www.imf.org/en/Publications/WEO/Issues/2025/07/29/world-economic-outlook-update-july-2025>
* [47]

  C. Ertur, W. Koch, Growth, technological interdependence and spatial
  externalities: theory and evidence, J. Appl. Econ. (Chichester Engl.) 22 (6)
  (2007) 1033–1062.