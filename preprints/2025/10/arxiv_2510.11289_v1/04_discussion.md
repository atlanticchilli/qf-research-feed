---
authors:
- Miloš Ciganović
- Elena Scola Gagliardi
- Massimiliano Tancioni
doc_id: arxiv:2510.11289v1
family_id: arxiv:2510.11289
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe
  thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco
  Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi
  Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants
  at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics,
  the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III
  Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is
  based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions
  drawn from the data lies entirely with the authors. This paper uses data from the
  Eurosystem Household Finance and Consumption Survey. We acknowledge financial support
  from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.
url_abs: http://arxiv.org/abs/2510.11289v1
url_html: https://arxiv.org/html/2510.11289v1
venue: arXiv q-fin
version: 1
year: 2025
---


Miloš Ciganović
Department of Economics and Law, Sapienza University of Rome. Emails:
  
milos.ciganovic@uniroma1.it
  
elena.scolagagliardi@uniroma1.it
  
massimiliano.tancioni@uniroma1.it
  
Elena Scola Gagliardi0
  
Massimiliano Tancioni0

(October, 2025)

###### Abstract

We estimate the dynamic distributional effects of financial shocks in the Euro Area using survey-based microdata on personal incomes. We find that positive financial shocks increase inequality, with heterogeneity across different income groups. Much of the response emerges in the tails of the income distribution. By decomposing individual incomes into financial and labor components, we identify two distinct transmission mechanisms: financial income inequality rises, likely due to differences in asset holdings. In contrast, labor income inequality increases through a skill premium channel. We then consider a nonlinear model framework, distinguishing the sign of the shock, allowing us to document the presence of asymmetric effects. While positive shocks lead to income disparities, adverse shocks have the opposite effect. Notably, middle-income groups are only affected following a negative shock, highlighting differential vulnerabilities across the income distribution.

Keywords: Income Inequality; Financial Shocks; Asymmetric Effects; Euro Area; Distribution.

JEL codes: D31; E32; G10; C32; C33.

## 1 Introduction

What are the effects of financial shocks on income inequality? What are their transmission mechanisms? Due to the recent dynamics of inequality observed in developed economies and its intricate links with the business cycle [[132](https://arxiv.org/html/2510.11289v1#biba.bibx64)], the topic has garnered growing interest among researchers and policymakers [[89](https://arxiv.org/html/2510.11289v1#biba.bibx21)].
  
The inequality literature addresses financial factors as key contributors to these developments (i.a. [[91](https://arxiv.org/html/2510.11289v1#biba.bibx23)]). Existing studies in this field have explored the relationship between inequality and specific financial dimensions, yielding mixed results [[90](https://arxiv.org/html/2510.11289v1#biba.bibx22)]. The specific domains addressed by this literature are assimilable under three perspectives: the role of financial development (i.a. [[114](https://arxiv.org/html/2510.11289v1#biba.bibx46), [136](https://arxiv.org/html/2510.11289v1#biba.bibx68)]), of financial liberalization (i.a. [[102](https://arxiv.org/html/2510.11289v1#biba.bibx34)]),111As noted by [[69](https://arxiv.org/html/2510.11289v1#biba.bibx1)], financial liberalization and financial development are conceptually distinct. The former refers to a reduction in government intervention and a greater role for market forces. In contrast, the latter captures the expansion of financial activity [[90](https://arxiv.org/html/2510.11289v1#biba.bibx22)]. and of banking crises (i.a. [[75](https://arxiv.org/html/2510.11289v1#biba.bibx7)]).
  
Turning to the macroeconomic literature, the interest in the role of financial shocks has focused mainly on standard macroeconomic endpoints [[105](https://arxiv.org/html/2510.11289v1#biba.bibx37), [127](https://arxiv.org/html/2510.11289v1#biba.bibx59), [122](https://arxiv.org/html/2510.11289v1#biba.bibx54), [128](https://arxiv.org/html/2510.11289v1#biba.bibx60), [83](https://arxiv.org/html/2510.11289v1#biba.bibx15), [104](https://arxiv.org/html/2510.11289v1#biba.bibx36), [103](https://arxiv.org/html/2510.11289v1#biba.bibx35), [81](https://arxiv.org/html/2510.11289v1#biba.bibx13)], leaving their role in affecting the distributional dynamics nearly unexplored. Recent contributions in the macro literature have examined how financial frictions can amplify the distributional consequences of monetary policy shocks [[84](https://arxiv.org/html/2510.11289v1#biba.bibx16), [97](https://arxiv.org/html/2510.11289v1#biba.bibx29)].
  
Our paper contributes to filling the apparent gap between the inequality and macro literature by examining the effects of financial shocks on income inequality and their transmission mechanics in the Euro Area. To the best of our knowledge, no study has yet isolated the direct impact of unexpected variations in stock prices on measures of inequality. Moreover, the focus on the European macroeconomy, which remains relatively under-explored, can offer new and potentially challenging results for the consolidated macro literature [[71](https://arxiv.org/html/2510.11289v1#biba.bibx3)].
  
Figure [1](https://arxiv.org/html/2510.11289v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.") presents unconditional evidence of a positive correlation between share prices and income inequality in the Eurozone. Although suggestive at best, this association motivates our focus on the implications for inequality of idiosyncratic stock market movements.

![Refer to caption](Figures/Unconditional_evidence.png)

Figure 1: Share Prices and Income Inequality in the Euro Area: Unconditional Evidence

The figure shows the scatter plot of income inequality and share prices in the Eurozone (grey dots). The fitted linear trend (black solid line) indicates a positive association.

The existing empirical literature suggests that transitioning from unconditional correlations to a conditional analysis can be challenging when the shock of interest originates in the financial sector. Even if there is little dispute about the fact that observed movements in stock prices explain a relevant fraction of macroeconomic fluctuations, financial shocks are indistinguishable from uncertainty shocks with standard identification methods ([[79](https://arxiv.org/html/2510.11289v1#biba.bibx11), [83](https://arxiv.org/html/2510.11289v1#biba.bibx15), [103](https://arxiv.org/html/2510.11289v1#biba.bibx35), [120](https://arxiv.org/html/2510.11289v1#biba.bibx52)]). Their simultaneity precludes the recourse to contemporaneous exclusion restrictions, and - absent specific financial measures for the Euro Area countries - credible set (sign)-based restrictions are hardly conceivable for shocks that tend to affect the economy in the same direction ([[83](https://arxiv.org/html/2510.11289v1#biba.bibx15), [120](https://arxiv.org/html/2510.11289v1#biba.bibx52), [81](https://arxiv.org/html/2510.11289v1#biba.bibx13)]). Moreover, identification methods based on quantitative restrictions ([[83](https://arxiv.org/html/2510.11289v1#biba.bibx15), [87](https://arxiv.org/html/2510.11289v1#biba.bibx19)]) might fail because the magnitude of the stock price responses or its conditional variances are not necessarily maximized by the own (financial) shock ([[81](https://arxiv.org/html/2510.11289v1#biba.bibx13)]).
  
We address these empirical identification issues by adopting a simple two-step modelling approach, which involves controlling for uncertainty in the second step only. In the first step, we recover the structural shocks using a panel vector autoregressive methodology (P-SVAR) identified with sign restrictions. In the second step, we include the (possibly confounded) financial shock in a set of [[111](https://arxiv.org/html/2510.11289v1#biba.bibx43)]’s panel local projections (P-LPs) to recover the impulse responses of interest.222Such a two-step strategy resembles that recently adopted by [[99](https://arxiv.org/html/2510.11289v1#biba.bibx31)] and [[118](https://arxiv.org/html/2510.11289v1#biba.bibx50)]. The P-SVAR is identified with the baseline sign restrictions proposed in [[103](https://arxiv.org/html/2510.11289v1#biba.bibx35)], distinguishing the "uncertainty-confounded" financial shocks from the other sources of macroeconomic variability. We thus include contemporaneous and lagged measures of financial and macroeconomic uncertainty available at the EU country level in the control set of the second step P-LPs.333We consider two measures of uncertainty and financial market volatility: the smoothed World Uncertainty Index developed by [[70](https://arxiv.org/html/2510.11289v1#biba.bibx2)], and the Country-Level Index of Financial Stress (CLIFS) constructed by the European Central Bank (ECB).
  
The baseline results indicate that financial shocks increase income inequality in the Euro Area. This finding contrasts with the evidence for the United States on the cyclicality of inequality [[109](https://arxiv.org/html/2510.11289v1#biba.bibx41)]. However, it aligns with recent evidence of procyclical inequality in Europe — Norway [[78](https://arxiv.org/html/2510.11289v1#biba.bibx10)] and Germany [[95](https://arxiv.org/html/2510.11289v1#biba.bibx27)] — specifying that financial shocks primarily drive such pro-cyclicality. This result highlights the importance of distinguishing between different sources of business cycle fluctuations when examining their role in the distributional dynamics.
  
To better understand the conditional distributional dynamics, we then focus the analysis on specific segments of the income distribution.444Recent macroeconomic literature has increasingly emphasized the role of agent heterogeneity and distributional considerations, primarily due to their policy relevance. A prominent example is the growing body of research on Heterogeneous Agent New Keynesian (HANK) models, which explicitly account for household heterogeneity in studying macroeconomic dynamics. See, for instance, [[113](https://arxiv.org/html/2510.11289v1#biba.bibx45)]. Understanding these dynamics is essential, as macroeconomic shocks may have disparate effects across specific segments of the income distribution, necessitating targeted government interventions and prompting public support for economic policy. We utilize survey data from the European Union Statistics on Income and Living Conditions (EU-SILC) to examine the conditional dynamics of interquintile Gini indices, assessing how the income distribution is affected by financial shocks. The quintile-specific results show that the effects of financial shocks are more pronounced at the tails of the income distribution.
  
To shed further light on the transmission mechanisms, we decompose individual income into labor and financial components, allowing us to track how inequality in each responds to financial shocks. While this distinction has attracted growing attention in the study of aggregate macroeconomic shocks — particularly in the monetary policy literature (see, e.g., [[72](https://arxiv.org/html/2510.11289v1#biba.bibx4), [73](https://arxiv.org/html/2510.11289v1#biba.bibx5)]) — it remains largely unexplored in the context of financial shocks. We document that a key channel through which financial shocks influence income inequality is the unequal distribution of financial asset holdings. This result aligns with the financial development literature, which distinguishes between the extensive margin — referring to access to financial markets — and the intensive margin, which captures the depth of participation within them. If a financial shock expands market access (i.e., affects the extensive margin), it may reduce inequality. Conversely, if its benefits accrue primarily to those already integrated into financial markets (i.e., affect the intensive margin), inequality may increase. By focusing on positive financial incomes, we provide evidence consistent with a mechanism operating through the intensive margin.
  
A more nuanced question is whether financial shocks also affect labor income inequality, and through which mechanisms. We find that labor income inequality responds positively to financial shocks over medium-term horizons. While multiple (and not mutually exclusive) factors may underlie this relationship, we provide evidence for one specific channel, related to an evident pro-cyclicality of top earners’ incomes within the distribution. In particular, positive financial shocks lead to higher remuneration for senior executives and top management, thereby contributing to greater labor income inequality. Furthermore, drawing on the International Labour Organization (ILO) classification of occupational tasks (ISCO-08) available in our dataset, we show that this effect is conceivable through the lens of a skill premium: financial shocks disproportionately increase the wages of high-skilled workers relative to those of low-skilled workers.
  
To align our analysis with the theoretical and empirical macro literature [[82](https://arxiv.org/html/2510.11289v1#biba.bibx14), [76](https://arxiv.org/html/2510.11289v1#biba.bibx8)] on the emergence of asymmetric effects from positive and negative financial shocks, we then emphasize the effects of adverse (negative) financial shocks. From the nonlinear estimates, we show that positive and negative financial shocks affect inequality in opposite directions: while positive shocks increase inequality, negative shocks lead to a gradual and persistent decline. When decomposing inequality using interquintile Gini indices, we find that the middle of the income distribution is also significantly affected following a negative financial shock.
  
These results are robust to several control dimensions. Specifically, we test the dependence of results on the peculiar identifying assumptions, first removing the uncertainty controls from the LPs and then considering a standard recursive identification scheme for the P-SVAR, with the stock price variable ordered last as the fastest-moving variable. We then test the relevance of movements in stock prices originating in the the credit sector ([[117](https://arxiv.org/html/2510.11289v1#biba.bibx49), [112](https://arxiv.org/html/2510.11289v1#biba.bibx44)]), where credit shocks are separated from financial shocks considering a variant of the sign restrictions strategy in [[103](https://arxiv.org/html/2510.11289v1#biba.bibx35)], based on a magnitude restriction. Concerning the inequality endpoint, we consider the response of incomes in the 90th and 95th percentiles as an alternative to the Gini index. Finally, we test robustness to changes in the time and sectional dimensions of the sample. We first exclude the covid-19 period (thus reducing the temporal dimension to 2019:4) and then remove Latvia and the Netherlands from the sample, as they have experienced extreme financial shocks. Results remain qualitatively unchanged across all the control dimensions.
  
Our paper relates to two separate streams of literature: the extensive literature on inequality, specifically addressing the role of financial factors, and the emerging macroeconomic literature, which examines the impact of macroeconomic shocks on distributional dynamics.
  
From the first perspective, a closely related contribution is [[106](https://arxiv.org/html/2510.11289v1#biba.bibx38)], who link the rise in United States income concentration to high-net-worth individuals earning excess returns on early-stage private investments. While their focus differs, their findings complement ours by showing how individual portfolio choices, driven by economic conditions, can shape income trajectories and distributional outcomes. These results align with our previous findings that financial shocks exacerbate disparities in financial income. More broadly, our work contributes to the literature on financial development and inequality (e.g., [[90](https://arxiv.org/html/2510.11289v1#biba.bibx22)]) and echoes the intensive margin mechanism emphasized in [[108](https://arxiv.org/html/2510.11289v1#biba.bibx40)].
  
From the second perspective, we relate to several recent studies in the macro literature. [[72](https://arxiv.org/html/2510.11289v1#biba.bibx4)] document how monetary policy shocks affect different income groups in Sweden, with responses shaped by income composition and heterogeneity. Notably, they find that expansionary shocks tend to affect both low- and high-income individuals more than those in the middle of the distribution — a pattern consistent with our findings. Similarly, [[73](https://arxiv.org/html/2510.11289v1#biba.bibx5)] study the effects of monetary policy on income, wealth, and consumption in Denmark, emphasizing the importance of distinguishing income components. These studies, like ours, highlight the importance of distinguishing between labor and financial income to gain a deeper understanding of the transmission of macroeconomic shocks. This reasoning also aligns with [[107](https://arxiv.org/html/2510.11289v1#biba.bibx39)], who show that the income composition is a key determinant of who gains or loses following aggregate shocks. Finally, [[93](https://arxiv.org/html/2510.11289v1#biba.bibx25)] demonstrate that unexpected monetary easing increases labor income inequality between high- and low-skilled workers in the United States. We view this as complementary to our interpretation of labor income responses to financial shocks through the lens of the skill premium.
  
The remainder of the paper proceeds as follows. Sections [2](https://arxiv.org/html/2510.11289v1#S2 "2 Data ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.") and [3](https://arxiv.org/html/2510.11289v1#S3 "3 Empirical strategy ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.") outline the data and the empirical strategy adopted in the analyses. Section [4](https://arxiv.org/html/2510.11289v1#S4 "4 The effects of financial shocks on income inequality ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.") presents the main results. Section [5](https://arxiv.org/html/2510.11289v1#S5 "5 The asymmetric response of inequality to financial shocks ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.") focuses on the asymmetric inequality implications of financial shocks, and Section [6](https://arxiv.org/html/2510.11289v1#S6 "6 Conclusions ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.") concludes.

## 2 Data

We consider quarterly data for a panel of Euro Area countries over the period 2006:1–2023:4.555Countries included in our sample are: Austria (AT), Belgium (BE), Germany (DE), Estonia (EE), Greece (EL), Spain (ES), Finland (FI), France (FR), Italy (IT), Lithuania (LT), Luxembourg (LU), Latvia (LV), Netherlands (NL), Portugal (PT), Slovenia (SI), and Slovakia (SK).  The analysis exploits the cross-sectional and time series information contained in two types of data: (i) Microdata for income-related variables, and (ii) macroeconomic time series.

### 2.1 Microdata-based income and inequality measures

To construct our inequality measures, we use microdata from the EU-SILC survey, which provides harmonized cross-sectional and longitudinal data on income, poverty, and living conditions across EU member states.
  
The analysis considers both an aggregate measure of income inequality in the Euro Area and inequality measures across specific segments of the income distribution (quintiles). Furthermore, we distinguish between financial and labor income inequality and specific segments of the ILO’s classification of tasks, the latter to identify the skill specificities in the transmission of financial shocks to labor income inequality.
  
We construct our income variable based on the definition of market income provided in the Methodological Guidelines and Description of EU-SILC Target Variables issued by the European Commission (2023 version). Accordingly, to better capture income inequality, we use the equivalised version of income by applying the modified OECD equivalence scale. This procedure involves computing total household income and then dividing it by an equivalence factor that reflects household composition. The equivalence factor assigns a weight of 1.0 to the first adult, 0.5 to the second adult, and to each additional person aged 14 or over, and 0.3 to a child under the age of 14. Based on this definition of individual income, we compute Gini indices by country, as well as the other inequality measures. We then distinguish between financial and labor income. To capture the intensive margin, we consider only positive values of income.
  
To investigate the role of the skill premium, we construct a skill-based income measure defined as the ratio of the average annual income of high-skilled workers to that of low-skilled workers. Skill levels follow the ILO definition, based on the ISCO classification of occupations. The reference version is ISCO-08. This framework assigns skill levels ranging from 1 (lowest) to 4 (highest). We define high-skilled workers as those in levels 3 or 4, which correspond to the following occupational groups: Managers, Legislators, Professionals, and Technicians and Associate Professionals. We consider only individuals of working age (15–64 years) in this section.

### 2.2 Macroeconomic aggregates

In addition to income-related variables, we use six macroeconomic time series in the baseline model estimates: GDP, GDP deflator, investment-to-output ratio, stock prices, interest rates, and financial deepening. Data are primarily sourced from the Eurostat Database, further described in the Data Section (Appendix [A](https://arxiv.org/html/2510.11289v1#A1 "Appendix A Data ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.")).

## 3 Empirical strategy

To provide empirical evidence on the effects of financial shocks on income inequality, we employ a two-step methodology [[99](https://arxiv.org/html/2510.11289v1#biba.bibx31), [118](https://arxiv.org/html/2510.11289v1#biba.bibx50)]. The first step involves recovering the country-specific structural shocks of interest from a (pooled) P-SVAR. In contrast, the second focuses on estimating the impulse responses using a panel version of the LP method, as described by [[111](https://arxiv.org/html/2510.11289v1#biba.bibx43)]. In the first step, we identify the financial shock, along with all other shocks, following the baseline strategy adopted in [[103](https://arxiv.org/html/2510.11289v1#biba.bibx35)]. In the second step, P-LPs, the confounding effects stemming from changes in uncertainty are controlled for by including macroeconomic and uncertainty measures in the set of controls, along with section- and time-specific effects.
  
The first reason for adopting the two-step method is the impossibility of separating the financial shock from uncertainty with set-based restrictions in the absence of country-level data on the external finance premium. A second reason is the simplicity of the LP methodology: LPs rely on a single regression estimation where the dependent variable is the specific inequality measure at different horizons, thereby minimizing the number of parameters to be estimated. A third reason for our approach stems from considerations about the variance-bias trade-off characterizing the choice between LPs and VARs, with bias being the primary concern when dealing with structural estimates [[116](https://arxiv.org/html/2510.11289v1#biba.bibx48)]. Consequently, coverage probability issues related to confidence intervals construction are avoided [[125](https://arxiv.org/html/2510.11289v1#biba.bibx57)]. A more formal description of our baseline two-step strategy is given below.

### 3.1 Identification

Recent literature indicates that movements in stock prices are often accompanied by significant changes in uncertainty measures [[79](https://arxiv.org/html/2510.11289v1#biba.bibx11)]. As long as financial and uncertainty shocks tend to affect the macroeconomy and financial indicators simultaneously and in the same direction, it is unclear whether standard identification methods based on exclusion and/or set (sign) restrictions can be defended on theoretical or statistical grounds ([[83](https://arxiv.org/html/2510.11289v1#biba.bibx15), [120](https://arxiv.org/html/2510.11289v1#biba.bibx52), [81](https://arxiv.org/html/2510.11289v1#biba.bibx13)]).
  
In the context of set-based restrictions, financial shocks and uncertainty shocks are separable by assuming that the response of the external finance premium relative to uncertainty is higher for uncertainty shocks with respect to adverse financial shocks ([[131](https://arxiv.org/html/2510.11289v1#biba.bibx63), [103](https://arxiv.org/html/2510.11289v1#biba.bibx35)]). Unfortunately, such a strategy is not viable in our setting, as an off-the-shelf measure of the excess bond premium is not available for the European countries considered in the analysis, unlike uncertainty measures.
  
Alternative identification methods based on quantitative restrictions, as max share penalties ([[83](https://arxiv.org/html/2510.11289v1#biba.bibx15)]; [[87](https://arxiv.org/html/2510.11289v1#biba.bibx19)]), magnitude inequality constraints ([[119](https://arxiv.org/html/2510.11289v1#biba.bibx51)]), or heteroskedasticity-based restrictions ([[121](https://arxiv.org/html/2510.11289v1#biba.bibx53)]), cannot be considered safe alternative strategies, since stock price responses or variance magnitudes are not necessarily larger for idiosyncratic sources of variability ([[81](https://arxiv.org/html/2510.11289v1#biba.bibx13)]).
  
For these reasons, we address the empirical identification issue with the simple two-step modelling approach sketched above, which involves controlling for country-specific uncertainty in the second step only.
  
We borrow the identification strategy of financial shocks from the work of [[103](https://arxiv.org/html/2510.11289v1#biba.bibx35)], that provides a general characterization of financial shocks based on sign restrictions on the impact effects matrix [[96](https://arxiv.org/html/2510.11289v1#biba.bibx28), [85](https://arxiv.org/html/2510.11289v1#biba.bibx17), [126](https://arxiv.org/html/2510.11289v1#biba.bibx58), [134](https://arxiv.org/html/2510.11289v1#biba.bibx66), [101](https://arxiv.org/html/2510.11289v1#biba.bibx33)] consistent with most financial innovations studied in the macroeconomic literature: a positive financial shock is a demand shock leading to an increase in all variables in the PVAR. Such a shock differs from a general demand shock in that it assumes a pro-cyclical investment-to-output ratio response, and from an investment-specific shock in that the latter generates a negative response of the stock price index. The opposite sign of the responses of the macro variables to interest rate changes separates the monetary policy shock from the financial shock (Table [1](https://arxiv.org/html/2510.11289v1#S3.T1 "Table 1 ‣ 3.1 Identification ‣ 3 Empirical strategy ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program."))666We present the identification scheme for clarity purposes only. A more detailed exposition of the set-based identification scheme can be found in the source paper. The results obtained from the P-SVAR are available upon request from the authors. Details on the model specification are provided in Appendix [B](https://arxiv.org/html/2510.11289v1#A2 "Appendix B PVAR Specification ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.")..

Table 1: Identification Scheme ([[103](https://arxiv.org/html/2510.11289v1#biba.bibx35)])

|  | Supply | Demand | Monetary | Investment | Financial |
| --- | --- | --- | --- | --- | --- |
| GDP | + | + | + | + | + |
| Prices | −- | + | + | + | + |
| Interest rate |  | + | −- | + | + |
| Investment/output |  | −- |  | + | + |
| Stock prices | + |  |  | −- | + |

The table describes set-based restrictions imposed at impact for different variables (rows) in response to the shocks (columns). A blank space indicates an unrestricted response.

### 3.2 P-LP-based impulse responses

Once the possibly "contaminated" financial shocks are recovered from the P-SVAR, impulse responses are directly estimated through lag-augmented P-LPs [[130](https://arxiv.org/html/2510.11289v1#biba.bibx62)], including the contemporaneous and lagged values of the macroeconomic and financial uncertainty measures as controls. The P-LPs also consider controls for section and time-invariant confounding factors. Specifically, we adopt the Two-Way Mundlak (TWM) approach [[135](https://arxiv.org/html/2510.11289v1#biba.bibx67)] to the Two-Way Fixed Effects estimator.
  
Let εi,t\varepsilon\_{i,t} be the country-specific financial shock series, identified within the P-SVAR. The h=0,1,…,Hh=0,1,...,H periods ahead impulse response function for the outcome variables of interest yi,ty\_{i,t} (measures of income inequality) is obtained considering the following P-LP specification:

|  |  |  |  |
| --- | --- | --- | --- |
|  | yi,t+h=βh​εi,t+∑l=1pγh,l​Xi,t−l+∑l=0pψh,l​Ui,t−l+ϑ​x¯i+ρ​x¯t+vi,t+h,y\_{i,t+h}=\beta\_{h}\varepsilon\_{i,t}\ +\sum\_{l=1}^{p}{\gamma\_{h,l}X\_{i,t-l}}+\sum\_{l=0}^{p}{\psi\_{h,l}U\_{i,t-l}}+\vartheta\bar{x}\_{i}+\rho\bar{x}\_{t}+v\_{i,t+h}, |  | (1) |

where βh\beta\_{h} are the impulse response parameters of interest, Xi,t−lX\_{i,t-l} is a vector of controls including lags of the outcome and shock variable together with the lags of all the variables included in the P-SVAR, and Ui,t−lU\_{i,t-l} contains the contemporaneous and lagged uncertainty controls.777We fix the order of lag pp to four. We have verified that results are robust to changes in the lag order. Given that the time-evolving degree of financialization may act as a relevant source of cross-country heterogeneity, we also include in the controls set Xi,t−lX\_{i,t-l} a measure of financial deepening, defined as the ratio of total financial sector assets to GDP.888Previous studies assessing the effects of financial deepening have typically relied on narrower indicators, such as the ratio of money to GDP [[115](https://arxiv.org/html/2510.11289v1#biba.bibx47)], or quasi-money to GDP [[123](https://arxiv.org/html/2510.11289v1#biba.bibx55)]. However, to better capture the overall size of the financial system, we adopt a broader indicator that includes a wider range of financial instruments. The variables x¯i\bar{x}\_{i} and x¯t\bar{x}\_{t} denote the TWM unit and time effects.
  
With this starting specification, the P-LP closely resembles the equation of interest in the P-SVAR, ensuring the consistency of the P-LP with the P-SVAR [[124](https://arxiv.org/html/2510.11289v1#biba.bibx56), [125](https://arxiv.org/html/2510.11289v1#biba.bibx57)].
  
The equivalent within transformation of the P-LP is the following:

|  |  |  |  |
| --- | --- | --- | --- |
|  | y¨i,t+h=βh​ε¨i,t+∑l=1pγh,l​X¨i,t−l+∑l=0pψh,l​U¨i,t−l+vi,t+h,\ddot{y}\_{i,t+h}=\beta\_{h}\ddot{\varepsilon}\_{i,t}+\sum\_{l=1}^{p}{\gamma\_{h,l}}\ddot{X}\_{i,t-l}+\sum\_{l=0}^{p}{\psi\_{h,l}}\ddot{U}\_{i,t-l}+v\_{i,t+h}, |  | (2) |

where double-dotted letters represent double demeaned variables. More specifically, the generic variable x¨\ddot{x} is defined as x¨i,t=xi,t+x¯i,t−x¯i−x¯t\ddot{x}\_{i,t}=x\_{i,t}+\bar{x}\_{i,t}-\bar{x}\_{i}-\bar{x}\_{t}, where xi,tx\_{i,t} is the original variable, and x¯i,t\bar{x}\_{i,t} is its overall mean. Since the pooled P-SVAR already controls for the sectional variability through section-specific constant terms, the structural shocks (ε¨i,t\ddot{\varepsilon}\_{i,t}) enter only in a time-demeaned form.
  
To account for potential correlation among residuals, standard errors are adjusted considering the [[94](https://arxiv.org/html/2510.11289v1#biba.bibx26)] method. The maximum autocorrelation window (mm) is set to h+1h+1, with hh being the horizon of the impulse response function [[111](https://arxiv.org/html/2510.11289v1#biba.bibx43), [133](https://arxiv.org/html/2510.11289v1#biba.bibx65)].999For robustness, we consider other maximum autocorrelation window values. Specifically, we consider m=p+1m=p+1, with pp being the number of lags, and m=p+h+1m=p+h+1.

## 4 The effects of financial shocks on income inequality

This section provides baseline empirical evidence on how financial shocks affect income inequality in the Euro Area. We present results at both the aggregate level and for specific segments of the income distribution. Furthermore, we examine the underlying drivers of the responses by decomposing income into financial and labor components, allowing us to investigate the roles of two key potential transmission mechanisms: financial asset holdings and the skill premium.
  
Figure [2](https://arxiv.org/html/2510.11289v1#S4.F2 "Figure 2 ‣ 4 The effects of financial shocks on income inequality ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.") displays the country-level time series of financial shocks estimated with the P-SVAR in the first step of our empirical strategy. Each line represents one of the Euro Area countries included in the sample. The shocks fluctuate around zero, consistent with their interpretation of unexpected financial disturbances.
  
The country-specific shocks effectively capture the significant episodes of financial market volatility. A clear, common pattern emerges around 2008–2009, coinciding with the Global Financial Crisis, where many countries experienced large adverse shocks. A second wave of higher dispersion occurs during 2020–2021, consistent with the financial market turbulence triggered by the covid-19 pandemic.
  
While most countries exhibit moderate variation, some display more pronounced patterns. In particular, Latvia (orange) and the Netherlands (green) stand out for the magnitude of their shocks over specific periods.101010Results remain qualitatively unchanged when these two countries are excluded from the analysis (Figure [17](https://arxiv.org/html/2510.11289v1#A4.F17 "Figure 17 ‣ D.5 Subsample estimates: excluding extreme financial shocks ‣ Appendix D Robustness ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program."), Appendix [D.5](https://arxiv.org/html/2510.11289v1#A4.SS5 "D.5 Subsample estimates: excluding extreme financial shocks ‣ Appendix D Robustness ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.")).
  
Overall, the estimated country-specific shocks validate the identification strategy and reflect meaningful variations in financial conditions at the country level.

![Refer to caption](x1.png)

Figure 2: Financial shocks series

Country-level time series of financial shocks in the Euro Area, identified as in Table [1](https://arxiv.org/html/2510.11289v1#S3.T1 "Table 1 ‣ 3.1 Identification ‣ 3 Empirical strategy ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.").

### 4.1 Financial shocks and income inequality. Baseline results

Figure [3](https://arxiv.org/html/2510.11289v1#S4.F3 "Figure 3 ‣ 4.1 Financial shocks and income inequality. Baseline results ‣ 4 The effects of financial shocks on income inequality ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.") displays the response of the income Gini index after a one-standard-deviation positive financial shock occurs. The solid black line shows the estimated impulse response. Shaded areas denote confidence intervals—68% in dark gray, 90% in light gray.
  
The Gini index rises on impact and continues to increase over time, peaking at 0.14 percentage points by the end of the third year, indicating that a positive financial shock - associated with rising share prices - leads to an increase in income inequality. This basic finding aligns with the evidence of pro-cyclical inequality in Europe, recently documented for Norway by [[78](https://arxiv.org/html/2510.11289v1#biba.bibx10)] and for Germany by [[95](https://arxiv.org/html/2510.11289v1#biba.bibx27)]. From this perspective, our result confirms the apparent contrast with evidence from the United States, indicating a counter-cyclical behavior of inequality.
  
To assess whether our main result reflects the effects of general aggregate demand shocks or is specific to financial shocks, we also examine the responses of inequality to other shocks identified in the S-PVAR. Results show that in the Euro Area, financial shocks are the primary source of the observed pro-cyclicality. In contrast, other demand shocks have neutral or even equalizing effects (Appendix [C](https://arxiv.org/html/2510.11289v1#A3 "Appendix C Additional results ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.")).111111The result for the generic demand shock (second column of Table [1](https://arxiv.org/html/2510.11289v1#S3.T1 "Table 1 ‣ 3.1 Identification ‣ 3 Empirical strategy ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.")) is in the Appendix [C](https://arxiv.org/html/2510.11289v1#A3 "Appendix C Additional results ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program."), Figure [10](https://arxiv.org/html/2510.11289v1#A3.F10 "Figure 10 ‣ Appendix C Additional results ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program."). Due to space constraints, the remaining IRFs are available upon request. We thank Francesco Furlanetto for suggesting this exercise and for highlighting its relevance and connection to the literature. Please note that, since the shock of interest here is not financial, the measures of uncertainty are not considered among the control variables. This result highlights the importance of the composition of business cycle shocks in shaping the inequality–cycle relationship across countries.

![Refer to caption](x2.png)

Figure 3: Income inequality responses in the Euro Area

The figure illustrates the response of income inequality following a one-standard-deviation positive financial shock. Full lines are point estimates; shaded areas indicate 90% and 68% confidence bands computed from panel HAC standard errors.

Figures [12](https://arxiv.org/html/2510.11289v1#A4.F12 "Figure 12 ‣ D.1 Not including uncertainity controls ‣ Appendix D Robustness ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.") and [13](https://arxiv.org/html/2510.11289v1#A4.F13 "Figure 13 ‣ D.2 Alternative identification strategy: recursive ‣ Appendix D Robustness ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.") in the Appendix ([D.1](https://arxiv.org/html/2510.11289v1#A4.SS1 "D.1 Not including uncertainity controls ‣ Appendix D Robustness ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.") and [D.2](https://arxiv.org/html/2510.11289v1#A4.SS2 "D.2 Alternative identification strategy: recursive ‣ Appendix D Robustness ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.")) show that the main findings hold when removing the uncertainty controls from the P-LP and when using a recursive (Cholesky) identification, where the ordering of the variables follows that of Table [1](https://arxiv.org/html/2510.11289v1#S3.T1 "Table 1 ‣ 3.1 Identification ‣ 3 Empirical strategy ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program."). The results of the robustness checks considering alternative measures of the distribution 121212The choice of the 90th and 95th percentiles as alternative measures of inequality is motivated by recent studies documenting that income inequality dynamics are strictly related to top end dynamics [[129](https://arxiv.org/html/2510.11289v1#biba.bibx61)]. and alternative samples (excluding the covid-19 period and omitting countries for which the financial shock series is particularly volatile) are summarized in the robustness checks section of Appendix ([D](https://arxiv.org/html/2510.11289v1#A4 "Appendix D Robustness ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.")).

### 4.2 Segments of the income distribution

Do different segments of the income distribution respond differently to a financial shock? Figure [4](https://arxiv.org/html/2510.11289v1#S4.F4 "Figure 4 ‣ 4.2 Segments of the income distribution ‣ 4 The effects of financial shocks on income inequality ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.") presents the impulse responses of inequality across specific segments of the distribution.131313For space considerations, we report only the first, third, and fifth quintiles. The responses of the second and fourth quintiles closely resemble those of the third. Specifically, we consider interquintile Gini indices.141414To gain insight into both the variability and the average effects, we also examined the responses of average income by quintile. For visibility purposes, the results are available upon request. This approach enables us to identify where in the income distribution the effects are most pronounced.

![Refer to caption](x3.png)

![Refer to caption](x4.png)

![Refer to caption](x5.png)

Figure 4: Impulse responses to financial shocks: interquintile inequality

The figure displays the impulse responses of interquintile inequality for each income quintile following a one-standard-deviation financial shock. Solid lines represent point estimates; shaded areas denote 90% and 68% confidence bands computed from panel HAC standard errors.

Following a positive financial shock, we observe heterogeneous effects across the income distribution. Interquintile Gini indices more significantly in the first and fifth quintiles. In the bottom quintile (first), the response is characterized by a temporary increase in inequality. In contrast, the top quintile (fifth) experience an increase in the Gini index at longer horizons. Overall, the tails of the income distribution are more affected by financial shocks than middle-income counterparts.
  
This result aligns with previous research, which, although it did not directly address financial shocks, has shown that the tails of the income distribution are more sensitive to macroeconomic shocks than middle-income groups. For instance, [[72](https://arxiv.org/html/2510.11289v1#biba.bibx4)] find that monetary policy shocks generate a U-shaped pattern in the total income response, meaning they have significantly larger effects on incomes at the tails of the distribution compared to the middle-income groups.
  
Concerning the mechanisms behind these distributional patterns, the response at the top of the income distribution is likely due to differences in financial asset holdings and to the role of the skill composition in shaping labor market outcomes. In contrast, the dynamics at the bottom of the distribution might reflect the specific composition of individuals in this segment. In particular, we are looking at very low income levels, characterized by low elasticity to financial shocks. However, some of these individuals may still be indirectly affected by such shocks. For instance, part of their income may stem from precarious or marginal jobs loosely tied to financial or real estate market activity, which tend to be sensitive to financial conditions. In such cases, even in the absence of job losses, a compression of already low incomes may occur. Clearly, individuals within the first quintile are heterogeneous, and some may still benefit—albeit marginally—from the shock, for example, through intergenerational transfers or financial income held by other household members. These internal differences can lead to a widening of income dispersion within the quintile. We directly explore the empirical relevance of these mechanisms in the next section.

### 4.3 The role of financial and labor income components

The results from the previous section show that positive financial shocks increase income inequality, and the distributional effects are more pronounced at the tails of the income distribution.
  
To understand the transmission mechanics behind such a heterogeneous response, it is necessary to disentangle the relative contributions of different income components. Our data enable us to decompose individual income into financial and labor income components, allowing us to quantify the responses of financial and labor income inequality to the financial shock. Notably, while the distinction between financial and labor income channels has gained increasing attention in the study of macroeconomic shocks—particularly in the monetary policy literature (see, e.g., [[72](https://arxiv.org/html/2510.11289v1#biba.bibx4), [73](https://arxiv.org/html/2510.11289v1#biba.bibx5)])—it remains largely unexplored in the context of financial shocks.

![Refer to caption](x6.png)

![Refer to caption](x7.png)

Figure 5: Financial (left) and labor (right) income inequality responses

The figure illustrates the response of inequality for financial and labor incomes following a one-standard-deviation positive financial shock. Full lines are point estimates; shaded areas indicate 90% and 68% confidence bands computed from panel HAC standard errors.

Figure [5](https://arxiv.org/html/2510.11289v1#S4.F5 "Figure 5 ‣ 4.3 The role of financial and labor income components ‣ 4 The effects of financial shocks on income inequality ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.") provides evidence on the relevance of financial shocks for both income components. The left panel displays the impulse response of financial income inequality, while the right panel shows the response of labor income inequality.
  
Following a positive financial shock, financial income inequality rises, peaking at approximately 0.32 percentage points after one year, before gradually declining at longer horizons. By contrast, the response of labor income is less immediate but equally significant: labor income inequality persists over time, stabilizing at around 0.12 percentage points after two years.
  
The first result, concerning financial income, appears straightforward and intuitive. It might reflect the distribution of financial asset holdings: when a positive financial shock occurs, share prices rise, leading to higher returns for individuals with financial income—returns that are larger for those with greater financial holdings. In this sense, the financial shock acts as an amplifier of the pre-existing uneven distribution of financial assets along the income distribution. To provide supporting evidence for this mechanism, Figure [6](https://arxiv.org/html/2510.11289v1#S4.F6 "Figure 6 ‣ 4.3 The role of financial and labor income components ‣ 4 The effects of financial shocks on income inequality ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.") displays the share of financial income held across income distribution in our sample.151515Using a consistent sample, we compare the distribution of financial income in the Euro Area for a specific year based on EU-SILC and ECB’s Household Finance and Consumption Survey (HFCS) data, in order to assess potential underreporting of financial income in our sample. This concern has been raised in the context of United States survey data, where studies [[80](https://arxiv.org/html/2510.11289v1#biba.bibx12)] have documented that financial income is underestimated. The relevant figures are in Appendix [F](https://arxiv.org/html/2510.11289v1#A6 "Appendix F Comparison of financial holdings in EU-SILC and HFCS data ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program."). The two distributions have a similar shape: Both are highly right-skewed.

![Refer to caption](Figures/Impulse_responses/Decomposing_income/Financial_income/Share_of_financial_income_held.png)

Figure 6: Financial income distribution in the Euro Area (2023)

The figure displays the share of total financial income held by each individual, with individuals ranked according to their position in the overall income distribution. Top earners (in the 99th percentile) are excluded from the graphical representation for clarity and visibility purposes.

Since financial income captures only individuals who actively participate in financial markets, this result complements the broader literature on financial development and income inequality (see, e.g., [[90](https://arxiv.org/html/2510.11289v1#biba.bibx22)]). Specifically, it aligns with the notion of the intensive margin emphasized in previous studies ([[108](https://arxiv.org/html/2510.11289v1#biba.bibx40)]). While much of the existing literature focuses on financial development — understood as the expansion of financial activity — we interpret our findings as consistent with the view that positive financial shocks benefit those already integrated into financial markets.
  
In this context, the results in [[106](https://arxiv.org/html/2510.11289v1#biba.bibx38)] are not only complementary to our findings but also an integral part of the broader narrative. The complementarity element stands out in emphasizing how portfolio allocation decisions (i.e., financial income allocation) shape individual income trajectories and, consequently, influence distributional outcomes. Furthermore, the results in [[106](https://arxiv.org/html/2510.11289v1#biba.bibx38)] extend the comprehension of the mechanism we document: while we show that a positive financial shock raises share prices and amplifies financial income inequality, [[106](https://arxiv.org/html/2510.11289v1#biba.bibx38)] find, using United States data, that differences in portfolio composition are crucial. Specifically, they find that wealthier individuals have access to more profitable investment opportunities, thereby reinforcing inequality through returns heterogeneity.
  
A less immediate result concerns labor income inequality. First, labor income responds to financial shocks; second, its response appears to be persistent over time. We interpret this as related to the type of occupations held by workers. The suggested underlying mechanism is that a positive financial shock, by boosting share prices, disproportionately benefits the compensation of individuals in top occupations or those who hold equity stakes in their companies. To provide some rough evidence for this channel, we rely on the ISCO-08 occupational classification developed by the ILO, which categorizes workers based on their job tasks, thereby allowing us to distinguish between high-skilled and low-skilled workers. The fundamental conjecture here is that companies’ equity stakes are held mainly by high-skilled workers. This mechanism would be coherent with [[88](https://arxiv.org/html/2510.11289v1#biba.bibx20)]’s idea that the manner in which firms reward individuals for their labor contributes significantly to observed levels of income inequality.

![Refer to caption](x8.png)

Figure 7: The effects of financial shocks on the skill premium

The figure shows the response of the skill premium to a one-standard-deviation positive financial shock. The solid line represents point estimates, while the shaded areas denote 90% and 68% confidence bands computed from panel HAC standard errors.

Figure [7](https://arxiv.org/html/2510.11289v1#S4.F7 "Figure 7 ‣ 4.3 The role of financial and labor income components ‣ 4 The effects of financial shocks on income inequality ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.") presents the estimated effects of a financial shock on the skill premium, defined as the log ratio between high-skilled and low-skilled workers’ wages. The results provide supporting evidence for the proposed mechanism.161616Results for high-skilled and low-skilled workers are presented in Figure [11](https://arxiv.org/html/2510.11289v1#A3.F11 "Figure 11 ‣ Appendix C Additional results ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.") (Appendix [C](https://arxiv.org/html/2510.11289v1#A3 "Appendix C Additional results ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.")). Following a positive financial shock, wages increase for high-skilled workers, but not for low-skilled workers. Additional evidence on hours worked reveals unclear variations, suggesting that the observed effects are attributable to changes in compensation rather than to alternative explanations, such as technological displacement. We interpret this result as complementary to recent macroeconomic evidence. While the mechanism is novel in the context of financial shocks, the notion that aggregate shocks can have unequal effects across skill groups is consistent with prior research. For example, [[93](https://arxiv.org/html/2510.11289v1#biba.bibx25)] show that unexpected monetary policy easing widens inequality between high- and low-skilled workers.

## 5 The asymmetric response of inequality to financial shocks

In this section, we examine the potential asymmetric effects of positive and negative financial shocks on income inequality. This focus is motivated by recent macroeconomic literature highlighting the importance of such nonlinearities with respect to financial shocks (e.g. [[82](https://arxiv.org/html/2510.11289v1#biba.bibx14), [76](https://arxiv.org/html/2510.11289v1#biba.bibx8)]) and by the policy relevance of understanding the distinct impact of negative shocks.
  
There are at least two reasons—although not necessarily exhaustive—why adverse financial shocks are of particular concern for policymakers. First, they pose a serious threat to the financial stability. A negative financial shock typically depresses asset prices, increases banking sector stress, and can trigger a credit crunch, thereby evolving into a systemic risk for financial stability. Second, financial market fluctuations have substantial implications for the real economy. A large body of literature has documented the macroeconomic effects of financial shocks (i.a. [[105](https://arxiv.org/html/2510.11289v1#biba.bibx37), [127](https://arxiv.org/html/2510.11289v1#biba.bibx59), [128](https://arxiv.org/html/2510.11289v1#biba.bibx60), [83](https://arxiv.org/html/2510.11289v1#biba.bibx15), [103](https://arxiv.org/html/2510.11289v1#biba.bibx35)]). In both cases—threats to financial stability and to the real economy—there might be arguments for policy intervention, whether by financial stability authorities or by national governments through macroprudential policies or fiscal stimulus plans. Moreover, in contrast to positive financial shocks—where policymakers might face a trade-off between stimulating investment and containing inequality—negative shocks naturally prompt intervention to stabilize the economy, thereby offering an opportunity to design policies that simultaneously address both macroeconomic stabilization and distributional concerns.

### 5.1 Separating positive and negative financial shocks

To distinguish between positive and negative financial shocks, we draw on the idea that both have similar implications for second moments. This concept connects to the financial literature on sign asymmetries. For instance, [[98](https://arxiv.org/html/2510.11289v1#biba.bibx30)] build on the fact that negative shocks to stock prices tend to generate larger increases in volatility than positive shocks of similar magnitude. A related notion is adopted by [[100](https://arxiv.org/html/2510.11289v1#biba.bibx32)], who, despite focusing on the relationship between news and uncertainty, highlight the existence of asymmetric effects on uncertainty—conceptually close to the notion of volatility.
  
Building on these notions, we extend the baseline identification scheme by introducing an additional variable to explicitly capture financial market volatility, following an approach similar to that adopted by [[118](https://arxiv.org/html/2510.11289v1#biba.bibx50)], who separate negative and positive temperature shocks trough the variance of the vapor pressure. We approximate the financial market volatility with the ECB’s CLIFS. We impose the condition that both positive and negative financial shocks affect financial market volatility positively on impact, thereby distinguishing between the two types of shocks. While we remain agnostic about the relative magnitude of their effects on the variance, the impulse responses show that the impact response of financial volatility is approximately twice as large following a negative financial shock, consistent with the findings in the financial literature.171717To save space and for clarity of exposition, the results from the first step estimates are available upon request. The updated identification scheme is summarized in Table [3](https://arxiv.org/html/2510.11289v1#A5.T3 "Table 3 ‣ Appendix E Nonlinear framework ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.") of the Appendix ([E](https://arxiv.org/html/2510.11289v1#A5 "Appendix E Nonlinear framework ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.")). The reason why we do not consider a more standard approach, tackling this nonlinearity directly in the LP,181818The literature has increasingly focused on how to best model various forms of nonlinearities, with particular attention to sign asymmetries. Other notable contributions in this area include [[77](https://arxiv.org/html/2510.11289v1#biba.bibx9)] and [[86](https://arxiv.org/html/2510.11289v1#biba.bibx18)]. is that by introducing the sign nonlinearity in the P-LP only, we would have identified the shock in a linear P-SVAR framework and then estimated its effects nonlinearly, which may not be methodologically sound, as pointed-out in [[76](https://arxiv.org/html/2510.11289v1#biba.bibx8)].191919Since we identify the financial shock without considering the outcome variable in the P-SVAR (and hence no linear or nonlinear relationship is assumed between the two), we still use this alternative nonlinear specification as a robustness check. The specification in this case is ([[133](https://arxiv.org/html/2510.11289v1#biba.bibx65)]):

yi,t+h=βh+​max⁡[0,εi,t]+βh−​min⁡[0,εi,t]+∑l=1pγh,l​Xi,t−l+∑l=0pψh,l​Ui,t−l+ϑ​x¯i+ρ​x¯t+vi,t+h,y\_{i,t+h}=\beta^{+}\_{h}\max[0,\varepsilon\_{i,t}]+\beta^{-}\_{h}\min[0,\varepsilon\_{i,t}]+\sum\_{l=1}^{p}{\gamma\_{h,l}X\_{i,t-l}}+\sum\_{l=0}^{p}{\psi\_{h,l}U\_{i,t-l}}+\vartheta\bar{x}\_{i}+\rho\bar{x}\_{t}+v\_{i,t+h},

(3)
where βh+\beta^{+}\_{h} and βh−\beta^{-}\_{h} are the coefficients of interest for the positive and negative shocks, respectively.
  
The asymmetry is robust to the alternative specification. Regarding the separate responses, the positive shock effect is confirmed under this specification, while the response to a negative shock remains insignificant.

### 5.2 Results

Figure [8](https://arxiv.org/html/2510.11289v1#S5.F8 "Figure 8 ‣ 5.2 Results ‣ 5 The asymmetric response of inequality to financial shocks ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.") presents the estimated effects of positive (left panel) and negative (right panel) financial shocks on income inequality in the Euro Area. Following a positive financial shock, inequality rises, suggesting a permanent increase in inequality, consistent with the undistinguished positive shock dynamics displayed in Figure [3](https://arxiv.org/html/2510.11289v1#S4.F3 "Figure 3 ‣ 4.1 Financial shocks and income inequality. Baseline results ‣ 4 The effects of financial shocks on income inequality ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program."). In contrast, negative financial shocks generate an initially unclear response that turns negative over longer horizons. This pattern underscores the presence of pronounced asymmetries in the distributional effects of financial shocks.
  
Such a "sign effect" has been emphasized theoretically by [[82](https://arxiv.org/html/2510.11289v1#biba.bibx14)] and documented empirically by [[76](https://arxiv.org/html/2510.11289v1#biba.bibx8)]. Our findings confirm this asymmetry, albeit in the context of income inequality. The main differences between positive and negative financial shocks lie in both the sign and the timing of their effects on inequality. Regarding the sign, this asymmetry is consistent with the operation of the previously discussed “inequality amplifier” mechanism. A positive financial shock tends to magnify existing disparities over time by reinforcing cumulative gains among high-income and high-wealth individuals. In contrast, a negative financial shock leads to a reduction in inequality, as wealthier households typically experience proportionally larger losses.
  
In terms of dynamics, the persistent decline in inequality observed at longer horizons likely reflects the slow adjustment process that follows financial downturns. After a market collapse, the most exposed agents suffer losses that are not easily reversible, requiring a longer period to rebuild their portfolios. This persistence may also be associated with deleveraging phases and heightened risk aversion that typically follow adverse financial episodes, both contributing to a protracted redistribution of wealth and income. Finally, the lagged adjustment suggests that the redistributive effects of financial downturns may also reflect the sluggish response of labor market conditions.

![Refer to caption](x9.png)

![Refer to caption](x10.png)

Figure 8: The asymmetric distributional effects of financial shocks

The figure shows the response of income inequality to a one-standard-deviation positive (left) and negative (right) financial shock. The solid line represents point estimates, while the shaded areas denote 90% and 68% confidence bands computed from panel HAC standard errors.



![Refer to caption](x11.png)

![Refer to caption](x12.png)

![Refer to caption](x13.png)

![Refer to caption](x14.png)

![Refer to caption](x15.png)

![Refer to caption](x16.png)

![Refer to caption](x17.png)

![Refer to caption](x18.png)

![Refer to caption](x19.png)

![Refer to caption](x20.png)

Figure 9: IRFs across quintiles: positive (left) vs. negative Shocks (right)

The figure shows the response of income inequality in different quintiles to a one-standard-deviation positive (left column) and negative (right column) financial shock. The solid line represents point estimates, while the shaded areas denote 90% and 68% confidence bands computed from panel HAC standard errors.

Turning to the heterogeneity across income segments (Figure [9](https://arxiv.org/html/2510.11289v1#S5.F9 "Figure 9 ‣ 5.2 Results ‣ 5 The asymmetric response of inequality to financial shocks ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.")) we find that after positive financial shocks, the tails of the income distribution respond more strongly, consistent with our earlier evidence. In particular, the dynamics for the top quintile resemble the aggregate pattern shown in Figure [8](https://arxiv.org/html/2510.11289v1#S5.F8 "Figure 8 ‣ 5.2 Results ‣ 5 The asymmetric response of inequality to financial shocks ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program."), though with a less pronounced amplitude — inequality initially rises, then declines before increasing again. Adverse financial shocks reveal new and asymmetric patterns. First, income inequality within the top quintile decreases significantly, consistent with the idea that top-income individuals are more exposed to financial market losses. Here, the inequality amplification mechanism previously documented works in reverse: a negative shock compresses relative distances within the quintile. Second, we find that inequality increases within middle-income groups (second and third quintiles). Credit market frictions likely drive this result: when financial conditions tighten, households that rely more heavily on credit see their disposable income squeezed, while others remain less affected. Sectoral differences may also play a role, as some jobs are more sensitive to financial shocks than others. In addition, the structure of household income, such as dual earners or access to financial buffers, can further amplify intra-group dispersion. Lastly, the absence of a positive and significant response in the bottom quintile may reflect both the limited exposure to financial markets and the presence of collective bargaining or minimum income schemes, which help stabilize low-end earnings. This latter result aligns with the insights of [[110](https://arxiv.org/html/2510.11289v1#biba.bibx42)], who emphasize the role of government redistribution in protecting the lower end of the distribution. We interpret the result for the first quintile as complementary to this vision. Moreover, our findings are broadly consistent with the evidence provided by [[107](https://arxiv.org/html/2510.11289v1#biba.bibx39)], who show that income composition is a key predictor of which households benefit or lose following aggregate shocks. This finding is particularly relevant to our results, as it highlights how differences in household balance sheets contribute to explaining why middle-income groups are responsive to such shocks.

## 6 Conclusions

This paper has examined the effects of financial shocks on income inequality in the Euro Area, contributing to a growing literature at the intersection of macroeconomics, finance, and inequality. Using a two-step empirical approach combining structural panel vector autoregressions and panel local projections, we document that financial shocks increase income inequality, with substantial heterogeneity across income quintiles. Much of the increase in inequality is explained by the responsiveness observed at the tails of the distribution. By decomposing income into labor and financial components, we uncover distinct distributional channels: financial shocks amplify inequality through the intensive margin of financial income, while also increasing labor income inequality via higher compensation at the top of the income distribution. These findings highlight the varied transmission mechanisms linking financial shocks to inequality, underscoring the importance of considering both income composition and labor heterogeneity.
  
We find that adverse financial shocks have a larger impact on income inequality than positive shocks, even if the persistence profile of the effects indicates that positive shocks trigger longer-lasting inequality effects. Notably, adverse financial shocks significantly affect the distributional pattern of middle-income groups, highlighting differentiated vulnerabilities across the income distribution. From a policy perspective, our results suggest that financial shocks exacerbate existing inequalities, raising important considerations for the design of financial stability, redistribution, and social protection policies.
  
While our analysis focuses on intensive margins, an important direction for future research is to investigate the role of extensive margins in shaping the inequality effects of financial shocks—both through access to financial income and through labor market participation, particularly in relation to unemployment dynamics. Similarly, investigating how differences in portfolio allocation and wealth inequality mediate the transmission of financial shocks could provide further insights into the distributional consequences of financial instability.

## References

* [1]
  Abdul Abiad, Nienke Oomes and Kenichi Ueda
  “The quality effect: Does financial liberalization improve the allocation of capital?”
  In *Journal of Development Economics* 87.2, 2008, pp. 270–282
  DOI: [https://doi.org/10.1016/j.jdeveco.2007.12.002](https://dx.doi.org/https://doi.org/10.1016/j.jdeveco.2007.12.002)
* [2]
  Hites Ahir, Nicholas Bloom and Davide Furceri
  “The World Uncertainty Index”, 2022
* [3]
  Carlo Altavilla et al.
  “A research program on monetary policy for Europe”
  In *Journal of Monetary Economics* 147
  Elsevier, 2024, pp. 103673
* [4]
  Niklas Amberg, Thomas Jansson, Mathias Klein and Anna Rogantini Picco
  “Five facts about the distributional income effects of monetary policy shocks”
  In *American Economic Review: Insights* 4.3
  American Economic Association 2014 Broadway, Suite 305, Nashville, TN 37203, 2022, pp. 289–304
* [5]
  Asger Lau Andersen, Niels Johannesen, Mia Jørgensen and José-Luis Peydró
  “Monetary policy and inequality”
  In *The Journal of Finance* 78.5
  Wiley Online Library, 2023, pp. 2945–2989
* [6]
  Jonas Arias, Juan Francisco Rubio-Ramirez and Daniel F Waggoner
  “Inference based on SVARs identified with sign and zero restrictions: Theory and applications”
  FRB Atlanta Working Paper, 2014
* [7]
  Anthony B Atkinson and Salvatore Morelli
  “Economic crises and inequality”
  In *UNDP-HDRO occasional papers*, 2011
* [8]
  Regis Barnichon, Christian Matthes and Alexander Ziegenbein
  “Are the effects of financial market disruptions big or small?”
  In *Review of Economics and Statistics* 104.3
  MIT Press One Rogers Street, Cambridge, MA 02142-1209, USA journals-info …, 2022, pp. 557–570
* [9]
  Nadav Ben Zeev
  “Identification of sign-dependency of impulse responses”, 2019
* [10]
  Drago Bergholt, Francesco Furlanetto and Lorenzo Mori
  “Inequality and Risk: Facts and Implications from Consumption Transactions”, 2024
* [11]
  Nicholas Bloom
  “The impact of uncertainty shocks”
  In *Econometrica* 77.3
  Wiley Online Library, 2009, pp. 623–685
* [12]
  Peter J Brady and Steven Bass
  “Comparing the current population survey to income tax data”
  In *Available at SSRN 4025470*, 2021
* [13]
  Marco Brianti
  “Financial Shocks, Uncertainty Shocks, and Corporate Liquidity”
  In *Journal of Applied Econometrics*
  Wiley Online Library, 2025
* [14]
  Markus K Brunnermeier and Yuliy Sannikov
  “A macroeconomic model with a financial sector”
  In *American Economic Review* 104.2
  American Economic Association 2014 Broadway, Suite 305, Nashville, TN 37203, 2014, pp. 379–421
* [15]
  Dario Caldara and Edward Herbst
  “Monetary policy, real activity, and credit spreads: Evidence from Bayesian proxy SVARs”
  In *American Economic Journal: Macroeconomics* 11.1
  American Economic Association 2014 Broadway, Suite 305, Nashville, TN 37203-2425, 2019, pp. 157–192
* [16]
  Dario Caldara, Cristina Fuentes-Albero, Simon Gilchrist and Egon Zakrajšek
  “The macroeconomic impact of financial and uncertainty shocks”
  In *European Economic Review* 88
  Elsevier, 2016, pp. 185–207
* [17]
  Fabio Canova and Gianni De Nicolo
  “Monetary disturbances matter for business fluctuations in the G-7”
  In *Journal of Monetary Economics* 49.6
  Elsevier, 2002, pp. 1131–1159
* [18]
  Tomás Caravello and Pedro Martinez-Bruera
  “Disentangling Sign and Size Non-linearities”
  In *Available at SSRN 4704050*, 2024
* [19]
  Andrea Carriero and Alessio Volpicella
  “Max share identification of multiple shocks: An application to uncertainty and financial conditions”
  In *Journal of Business & Economic Statistics* 43.1
  Taylor & Francis, 2025, pp. 1–13
* [20]
  JA Cobb
  “How firms shape income inequality: Stakeholder power, executive decision making, and the structuring of employment relationships”
  In *Academy of Management Review* 41.2
  Academy of Management Briarcliff Manor, NY, 2016, pp. 324–348
* [21]
  E Dabla-Norris
  “Causes and Consequences of Income Inequality: A Global Perspective”, 2015
* [22]
  Jakob De Haan and Jan-Egbert Sturm
  “Finance and income inequality: A review and new evidence”
  In *European Journal of Political Economy* 50
  Elsevier, 2017, pp. 171–195
* [23]
  Asli Demirgüç-Kunt and Ross Levine
  “Finance and inequality: Theory and evidence”
  In *Annu. Rev. Financ. Econ.* 1.1
  Annual Reviews, 2009, pp. 287–318
* [24]
  Alistair Dieppe, Romain Legrand and Björn Van Roye
  “The Bayesian estimation, analysis and regression (BEAR) toolbox: Technical guide”
  In *Technical Document, BEAR Toolbox, European Central Bank*, 2018
* [25]
  Juan J Dolado, Gergo Motyovszki and Evi Pappa
  “Monetary policy and inequality under labor market frictions and capital-skill complementarity”
  In *American Economic Journal: Macroeconomics* 13.2
  American Economic Association 2014 Broadway, Suite 305, Nashville, TN 37203-2425, 2021, pp. 292–332
* [26]
  John C. Driscoll and Aart C. Kraay
  “Consistent Covariance Matrix Estimation with Spatially Dependent Panel Data”
  In *The Review of Economics and Statistics* 80.4
  The MIT Press, 1998, pp. 549–560
  URL: <http://www.jstor.org/stable/2646837>
* [27]
  Stephanie Ettmeier, Chi Hyun Kim and Frank Schorfheide
  “Distributional Effects of Aggregate Shocks: Functional vs. Panel Approaches” PDF available at <https://www.stephanieettmeier.com/_files/ugd/709433_dba833c9c22148e991527cf366c9b31e.pdf>, 2024
* [28]
  Jon Faust
  “The robustness of identified VAR conclusions about money”
  In *Carnegie-Rochester conference series on public policy* 49, 1998, pp. 207–244
  Elsevier
* [29]
  Francesco Ferlaino
  “Does the financial accelerator accelerate inequalities?”
  In *Available at SSRN 4845237*, 2024
* [30]
  Nuno B Ferreira, Rui Menezes and Diana A Mendes
  “Asymmetric conditional volatility in international stock markets”
  In *Physica A: Statistical Mechanics and its Applications* 382.1
  Elsevier, 2007, pp. 73–80
* [31]
  Mario Forni, Luca Gambetti and Luca Sala
  “News, uncertainty and economic fluctuations (no news is good news)”
  In *RECENT WORKING PAPER SERIES*
  Dipartimento di Economia Marco Biagi–Università di Modena e Reggio Emilia, 2017
* [32]
  Mario Forni, Luca Gambetti, Nicolò Maffei-Faccioli and Luca Sala
  “Nonlinear transmission of financial shocks: Some new evidence”
  In *Journal of Money, Credit and Banking* 56.1
  Wiley Online Library, 2024, pp. 5–33
* [33]
  Renee Fry and Adrian Pagan
  “Sign restrictions in structural vector autoregressions: A critical review”
  In *Journal of Economic Literature* 49.4
  American Economic Association, 2011, pp. 938–960
* [34]
  Davide Furceri and Mr Prakash Loungani
  “Capital account liberalization and inequality”
  International Monetary Fund, 2015
* [35]
  Francesco Furlanetto, Francesco Ravazzolo and Samad Sarferaz
  “Identification of financial factors in economic fluctuations”
  In *The Economic Journal* 129.617
  Oxford University Press, 2019, pp. 311–337
* [36]
  Luca Gambetti and Alberto Musso
  “Loan supply shocks and the business cycle”
  In *Journal of Applied Econometrics* 32.4
  Wiley Online Library, 2017, pp. 764–782
* [37]
  Simon Gilchrist, Vladimir Yankov and Egon Zakrajšek
  “Credit market shocks and economic fluctuations: Evidence from corporate bond and stock markets”
  In *Journal of Monetary Economics* 56.4
  Elsevier, 2009, pp. 471–493
* [38]
  Ararat Gocmen, Clara Martínez-Toledano and Vrinda Mittal
  “Private Capital Markets and Inequality”
  In *Available at SSRN 5166981*, 2025
* [39]
  Nils Gornemann, Keith Kuester and Makoto Nakajima
  “Doves for the rich, hawks for the poor? distributional consequences of systematic monetary policy”, 2021
* [40]
  Jeremy Greenwood and Boyan Jovanovic
  “Financial development, growth, and the distribution of income”
  In *Journal of Political Economy* 98.5, Part 1
  The University of Chicago Press, 1990, pp. 1076–1107
* [41]
  Fatih Guvenen, Serdar Ozkan and Jae Song
  “The nature of countercyclical income risk”
  In *Journal of Political Economy* 122.3
  University of Chicago Press Chicago, IL, 2014, pp. 621–660
* [42]
  Jonathan Heathcote, Fabrizio Perri and Giovanni L Violante
  “Unequal we stand: An empirical analysis of economic inequality in the United States, 1967–2006”
  In *Review of Economic Dynamics* 13.1
  Elsevier, 2010, pp. 15–51
* [43]
  Òscar Jordà
  “Estimation and inference of impulse responses by local projections”
  In *American Economic Review* 95.1
  American Economic Association, 2005, pp. 161–182
* [44]
  A. Justiniano, G. Primiceri and A. Tambalotti
  “Household leveraging and deleveraging”
  In *Review of Economic Dynamics* 18.1, 2015, pp. 3–20
* [45]
  Greg Kaplan and Giovanni L Violante
  “Microeconomic heterogeneity and macroeconomic shocks”
  In *Journal of Economic Perspectives* 32.3
  American Economic Association 2014 Broadway, Suite 305, Nashville, TN 37203-2418, 2018, pp. 167–194
* [46]
  Vivien Kappel
  “The effects of financial development on income inequality and poverty”
  In *CER-ETH-Center of Economic Research at ETH Zurich, Working Paper*, 2010
* [47]
  Hongyi Li, Lyn Squire and Heng-fu Zou
  “Explaining international and intertemporal variations in income inequality”
  In *The Economic Journal* 108.446
  Wiley Online Library, 1998, pp. 26–43
* [48]
   Li, M. Plagborg-Møller and C.K. Wolf
  “Local projections vs. vars: Lessons from thousands of DGPs”
  In *Journal of Econometrics*
  Elsevier, 2024, pp. 1–22
* [49]
  Z. Liu, P. Wang and T. Zha
  “Land price dynamics and macroeconomic fluctuation”
  In *Econometrica* 81.3, 2013, pp. 1147–1184
* [50]
  Francesco Simone Lucidi, Marta Maria Pisa and Massimiliano Tancioni
  “The effects of temperature shocks on energy prices and inflation in the Euro Area”
  In *European Economic Review* 166
  Elsevier, 2024, pp. 104771
* [51]
  Sydney C. Ludvigson, Sai Ma and Serena Ng
  “Shock Restricted Structural Vector-Autoregressions”
  In *NBER Working Paper No. w23225*, 2018
* [52]
  Sydney C Ludvigson, Sai Ma and Serena Ng
  “Uncertainty and business cycles: exogenous impulse or endogenous response?”
  In *American Economic Journal: Macroeconomics* 13.4
  American Economic Association 2014 Broadway, Suite 305, Nashville, TN 37203-2425, 2021, pp. 369–410
* [53]
  Helmut Lütkepohl, Mika Meitz, Aleksei Netšunajev and Pentti Saikkonen
  “Testing identification via heteroskedasticity in structural vector autoregressive models”
  In *The Econometrics Journal* 24.1, 2021, pp. 1–22
* [54]
  Roland Meeks
  “Do credit market shocks drive output fluctuations? Evidence from corporate spreads and defaults”
  In *Journal of Economic Dynamics and Control* 36.4
  Elsevier, 2012, pp. 568–584
* [55]
  Branko Milanovic
  “Can we discern the effect of globalization on income distribution? Evidence from household surveys”
  In *The World Bank Economic Review* 19.1
  Oxford University Press, 2005, pp. 21–44
* [56]
  José Luis Montiel Olea and Mikkel Plagborg-Møller
  “Local projection inference is simpler and more robust than you think”
  In *Econometrica* 89.4
  Wiley Online Library, 2021, pp. 1789–1823
* [57]
  José Luis Montiel Olea, Mikkel Plagborg-Møller, Eric Qian and Christian K Wolf
  “Double Robustness of Local Projections and Some Unpleasant VARithmetic”, 2024
* [58]
  Gert Peersman
  “What caused the early millennium slowdown? Evidence based on vector autoregressions”
  In *Journal of Applied Econometrics* 20.2
  Wiley Online Library, 2005, pp. 185–207
* [59]
  Gert Peersman
  “Bank lending shocks and the euro area business cycle”
  Faculteit Economie en Bedrijfskunde, Univ. Gent, 2011
* [60]
  Gert Peersman and WB Wagner
  “Shocks to bank lending, risk-taking, securitization, and their role for US business cycle fluctuations”, 2014
* [61]
  Thomas Piketty, Emmanuel Saez and Gabriel Zucman
  “Distributional National Accounts: Methods and Estimates for the United States\*”
  In *The Quarterly Journal of Economics* 133.2, 2017, pp. 553–609
  DOI: [10.1093/qje/qjx043](https://dx.doi.org/10.1093/qje/qjx043)
* [62]
  Mikkel Plagborg-Møller and Christian K Wolf
  “Local projections and VARs estimate the same impulse responses”
  In *Econometrica* 89.2
  Wiley Online Library, 2021, pp. 955–980
* [63]
  M. Shin and M. Zhong
  “A New Approach to Identifying the Real Effects of Uncertainty Shocks”
  In *Journal of Business & Economic Statistics* 38.2, 2018, pp. 367–379
  DOI: [10.1080/07350015.2018.1506342](https://dx.doi.org/10.1080/07350015.2018.1506342)
* [64]
  Joseph E Stiglitz
  “Macroeconomic fluctuations, inequality, and human development”
  In *Macroeconomics and human development*
  Routledge, 2015, pp. 31–58
* [65]
  Silvana Tenreyro and Gregory Thwaites
  “Pushing on a String: US Monetary Policy Is Less Powerful in Recessions”
  In *American Economic Journal: Macroeconomics* 8.4, 2016, pp. 43–74
  DOI: [10.1257/mac.20150016](https://dx.doi.org/10.1257/mac.20150016)
* [66]
  Harald Uhlig
  “What are the effects of monetary policy on output? Results from an agnostic identification procedure”
  In *Journal of Monetary Economics* 52.2
  Elsevier, 2005, pp. 381–419
* [67]
  Jeffrey M Wooldridge
  “Two-way fixed effects, the two-way Mundlak regression, and difference-in-differences estimators”
  In *Available at SSRN 3906345*, 2021
* [68]
  Ruixin Zhang and Sami Ben Naceur
  “Financial development, inequality, and poverty: Some international evidence”
  In *International Review of Economics & Finance* 61
  Elsevier, 2019, pp. 1–16

## References

* [69]
  Abdul Abiad, Nienke Oomes and Kenichi Ueda
  “The quality effect: Does financial liberalization improve the allocation of capital?”
  In *Journal of Development Economics* 87.2, 2008, pp. 270–282
  DOI: [https://doi.org/10.1016/j.jdeveco.2007.12.002](https://dx.doi.org/https://doi.org/10.1016/j.jdeveco.2007.12.002)
* [70]
  Hites Ahir, Nicholas Bloom and Davide Furceri
  “The World Uncertainty Index”, 2022
* [71]
  Carlo Altavilla et al.
  “A research program on monetary policy for Europe”
  In *Journal of Monetary Economics* 147
  Elsevier, 2024, pp. 103673
* [72]
  Niklas Amberg, Thomas Jansson, Mathias Klein and Anna Rogantini Picco
  “Five facts about the distributional income effects of monetary policy shocks”
  In *American Economic Review: Insights* 4.3
  American Economic Association 2014 Broadway, Suite 305, Nashville, TN 37203, 2022, pp. 289–304
* [73]
  Asger Lau Andersen, Niels Johannesen, Mia Jørgensen and José-Luis Peydró
  “Monetary policy and inequality”
  In *The Journal of Finance* 78.5
  Wiley Online Library, 2023, pp. 2945–2989
* [74]
  Jonas Arias, Juan Francisco Rubio-Ramirez and Daniel F Waggoner
  “Inference based on SVARs identified with sign and zero restrictions: Theory and applications”
  FRB Atlanta Working Paper, 2014
* [75]
  Anthony B Atkinson and Salvatore Morelli
  “Economic crises and inequality”
  In *UNDP-HDRO occasional papers*, 2011
* [76]
  Regis Barnichon, Christian Matthes and Alexander Ziegenbein
  “Are the effects of financial market disruptions big or small?”
  In *Review of Economics and Statistics* 104.3
  MIT Press One Rogers Street, Cambridge, MA 02142-1209, USA journals-info …, 2022, pp. 557–570
* [77]
  Nadav Ben Zeev
  “Identification of sign-dependency of impulse responses”, 2019
* [78]
  Drago Bergholt, Francesco Furlanetto and Lorenzo Mori
  “Inequality and Risk: Facts and Implications from Consumption Transactions”, 2024
* [79]
  Nicholas Bloom
  “The impact of uncertainty shocks”
  In *Econometrica* 77.3
  Wiley Online Library, 2009, pp. 623–685
* [80]
  Peter J Brady and Steven Bass
  “Comparing the current population survey to income tax data”
  In *Available at SSRN 4025470*, 2021
* [81]
  Marco Brianti
  “Financial Shocks, Uncertainty Shocks, and Corporate Liquidity”
  In *Journal of Applied Econometrics*
  Wiley Online Library, 2025
* [82]
  Markus K Brunnermeier and Yuliy Sannikov
  “A macroeconomic model with a financial sector”
  In *American Economic Review* 104.2
  American Economic Association 2014 Broadway, Suite 305, Nashville, TN 37203, 2014, pp. 379–421
* [83]
  Dario Caldara, Cristina Fuentes-Albero, Simon Gilchrist and Egon Zakrajšek
  “The macroeconomic impact of financial and uncertainty shocks”
  In *European Economic Review* 88
  Elsevier, 2016, pp. 185–207
* [84]
  Dario Caldara and Edward Herbst
  “Monetary policy, real activity, and credit spreads: Evidence from Bayesian proxy SVARs”
  In *American Economic Journal: Macroeconomics* 11.1
  American Economic Association 2014 Broadway, Suite 305, Nashville, TN 37203-2425, 2019, pp. 157–192
* [85]
  Fabio Canova and Gianni De Nicolo
  “Monetary disturbances matter for business fluctuations in the G-7”
  In *Journal of Monetary Economics* 49.6
  Elsevier, 2002, pp. 1131–1159
* [86]
  Tomás Caravello and Pedro Martinez-Bruera
  “Disentangling Sign and Size Non-linearities”
  In *Available at SSRN 4704050*, 2024
* [87]
  Andrea Carriero and Alessio Volpicella
  “Max share identification of multiple shocks: An application to uncertainty and financial conditions”
  In *Journal of Business & Economic Statistics* 43.1
  Taylor & Francis, 2025, pp. 1–13
* [88]
  JA Cobb
  “How firms shape income inequality: Stakeholder power, executive decision making, and the structuring of employment relationships”
  In *Academy of Management Review* 41.2
  Academy of Management Briarcliff Manor, NY, 2016, pp. 324–348
* [89]
  E Dabla-Norris
  “Causes and Consequences of Income Inequality: A Global Perspective”, 2015
* [90]
  Jakob De Haan and Jan-Egbert Sturm
  “Finance and income inequality: A review and new evidence”
  In *European Journal of Political Economy* 50
  Elsevier, 2017, pp. 171–195
* [91]
  Asli Demirgüç-Kunt and Ross Levine
  “Finance and inequality: Theory and evidence”
  In *Annu. Rev. Financ. Econ.* 1.1
  Annual Reviews, 2009, pp. 287–318
* [92]
  Alistair Dieppe, Romain Legrand and Björn Van Roye
  “The Bayesian estimation, analysis and regression (BEAR) toolbox: Technical guide”
  In *Technical Document, BEAR Toolbox, European Central Bank*, 2018
* [93]
  Juan J Dolado, Gergo Motyovszki and Evi Pappa
  “Monetary policy and inequality under labor market frictions and capital-skill complementarity”
  In *American Economic Journal: Macroeconomics* 13.2
  American Economic Association 2014 Broadway, Suite 305, Nashville, TN 37203-2425, 2021, pp. 292–332
* [94]
  John C. Driscoll and Aart C. Kraay
  “Consistent Covariance Matrix Estimation with Spatially Dependent Panel Data”
  In *The Review of Economics and Statistics* 80.4
  The MIT Press, 1998, pp. 549–560
  URL: <http://www.jstor.org/stable/2646837>
* [95]
  Stephanie Ettmeier, Chi Hyun Kim and Frank Schorfheide
  “Distributional Effects of Aggregate Shocks: Functional vs. Panel Approaches” PDF available at <https://www.stephanieettmeier.com/_files/ugd/709433_dba833c9c22148e991527cf366c9b31e.pdf>, 2024
* [96]
  Jon Faust
  “The robustness of identified VAR conclusions about money”
  In *Carnegie-Rochester conference series on public policy* 49, 1998, pp. 207–244
  Elsevier
* [97]
  Francesco Ferlaino
  “Does the financial accelerator accelerate inequalities?”
  In *Available at SSRN 4845237*, 2024
* [98]
  Nuno B Ferreira, Rui Menezes and Diana A Mendes
  “Asymmetric conditional volatility in international stock markets”
  In *Physica A: Statistical Mechanics and its Applications* 382.1
  Elsevier, 2007, pp. 73–80
* [99]
  Mario Forni, Luca Gambetti, Nicolò Maffei-Faccioli and Luca Sala
  “Nonlinear transmission of financial shocks: Some new evidence”
  In *Journal of Money, Credit and Banking* 56.1
  Wiley Online Library, 2024, pp. 5–33
* [100]
  Mario Forni, Luca Gambetti and Luca Sala
  “News, uncertainty and economic fluctuations (no news is good news)”
  In *RECENT WORKING PAPER SERIES*
  Dipartimento di Economia Marco Biagi–Università di Modena e Reggio Emilia, 2017
* [101]
  Renee Fry and Adrian Pagan
  “Sign restrictions in structural vector autoregressions: A critical review”
  In *Journal of Economic Literature* 49.4
  American Economic Association, 2011, pp. 938–960
* [102]
  Davide Furceri and Mr Prakash Loungani
  “Capital account liberalization and inequality”
  International Monetary Fund, 2015
* [103]
  Francesco Furlanetto, Francesco Ravazzolo and Samad Sarferaz
  “Identification of financial factors in economic fluctuations”
  In *The Economic Journal* 129.617
  Oxford University Press, 2019, pp. 311–337
* [104]
  Luca Gambetti and Alberto Musso
  “Loan supply shocks and the business cycle”
  In *Journal of Applied Econometrics* 32.4
  Wiley Online Library, 2017, pp. 764–782
* [105]
  Simon Gilchrist, Vladimir Yankov and Egon Zakrajšek
  “Credit market shocks and economic fluctuations: Evidence from corporate bond and stock markets”
  In *Journal of Monetary Economics* 56.4
  Elsevier, 2009, pp. 471–493
* [106]
  Ararat Gocmen, Clara Martínez-Toledano and Vrinda Mittal
  “Private Capital Markets and Inequality”
  In *Available at SSRN 5166981*, 2025
* [107]
  Nils Gornemann, Keith Kuester and Makoto Nakajima
  “Doves for the rich, hawks for the poor? distributional consequences of systematic monetary policy”, 2021
* [108]
  Jeremy Greenwood and Boyan Jovanovic
  “Financial development, growth, and the distribution of income”
  In *Journal of Political Economy* 98.5, Part 1
  The University of Chicago Press, 1990, pp. 1076–1107
* [109]
  Fatih Guvenen, Serdar Ozkan and Jae Song
  “The nature of countercyclical income risk”
  In *Journal of Political Economy* 122.3
  University of Chicago Press Chicago, IL, 2014, pp. 621–660
* [110]
  Jonathan Heathcote, Fabrizio Perri and Giovanni L Violante
  “Unequal we stand: An empirical analysis of economic inequality in the United States, 1967–2006”
  In *Review of Economic Dynamics* 13.1
  Elsevier, 2010, pp. 15–51
* [111]
  Òscar Jordà
  “Estimation and inference of impulse responses by local projections”
  In *American Economic Review* 95.1
  American Economic Association, 2005, pp. 161–182
* [112]
  A. Justiniano, G. Primiceri and A. Tambalotti
  “Household leveraging and deleveraging”
  In *Review of Economic Dynamics* 18.1, 2015, pp. 3–20
* [113]
  Greg Kaplan and Giovanni L Violante
  “Microeconomic heterogeneity and macroeconomic shocks”
  In *Journal of Economic Perspectives* 32.3
  American Economic Association 2014 Broadway, Suite 305, Nashville, TN 37203-2418, 2018, pp. 167–194
* [114]
  Vivien Kappel
  “The effects of financial development on income inequality and poverty”
  In *CER-ETH-Center of Economic Research at ETH Zurich, Working Paper*, 2010
* [115]
  Hongyi Li, Lyn Squire and Heng-fu Zou
  “Explaining international and intertemporal variations in income inequality”
  In *The Economic Journal* 108.446
  Wiley Online Library, 1998, pp. 26–43
* [116]
   Li, M. Plagborg-Møller and C.K. Wolf
  “Local projections vs. vars: Lessons from thousands of DGPs”
  In *Journal of Econometrics*
  Elsevier, 2024, pp. 1–22
* [117]
  Z. Liu, P. Wang and T. Zha
  “Land price dynamics and macroeconomic fluctuation”
  In *Econometrica* 81.3, 2013, pp. 1147–1184
* [118]
  Francesco Simone Lucidi, Marta Maria Pisa and Massimiliano Tancioni
  “The effects of temperature shocks on energy prices and inflation in the Euro Area”
  In *European Economic Review* 166
  Elsevier, 2024, pp. 104771
* [119]
  Sydney C. Ludvigson, Sai Ma and Serena Ng
  “Shock Restricted Structural Vector-Autoregressions”
  In *NBER Working Paper No. w23225*, 2018
* [120]
  Sydney C Ludvigson, Sai Ma and Serena Ng
  “Uncertainty and business cycles: exogenous impulse or endogenous response?”
  In *American Economic Journal: Macroeconomics* 13.4
  American Economic Association 2014 Broadway, Suite 305, Nashville, TN 37203-2425, 2021, pp. 369–410
* [121]
  Helmut Lütkepohl, Mika Meitz, Aleksei Netšunajev and Pentti Saikkonen
  “Testing identification via heteroskedasticity in structural vector autoregressive models”
  In *The Econometrics Journal* 24.1, 2021, pp. 1–22
* [122]
  Roland Meeks
  “Do credit market shocks drive output fluctuations? Evidence from corporate spreads and defaults”
  In *Journal of Economic Dynamics and Control* 36.4
  Elsevier, 2012, pp. 568–584
* [123]
  Branko Milanovic
  “Can we discern the effect of globalization on income distribution? Evidence from household surveys”
  In *The World Bank Economic Review* 19.1
  Oxford University Press, 2005, pp. 21–44
* [124]
  José Luis Montiel Olea and Mikkel Plagborg-Møller
  “Local projection inference is simpler and more robust than you think”
  In *Econometrica* 89.4
  Wiley Online Library, 2021, pp. 1789–1823
* [125]
  José Luis Montiel Olea, Mikkel Plagborg-Møller, Eric Qian and Christian K Wolf
  “Double Robustness of Local Projections and Some Unpleasant VARithmetic”, 2024
* [126]
  Gert Peersman
  “What caused the early millennium slowdown? Evidence based on vector autoregressions”
  In *Journal of Applied Econometrics* 20.2
  Wiley Online Library, 2005, pp. 185–207
* [127]
  Gert Peersman
  “Bank lending shocks and the euro area business cycle”
  Faculteit Economie en Bedrijfskunde, Univ. Gent, 2011
* [128]
  Gert Peersman and WB Wagner
  “Shocks to bank lending, risk-taking, securitization, and their role for US business cycle fluctuations”, 2014
* [129]
  Thomas Piketty, Emmanuel Saez and Gabriel Zucman
  “Distributional National Accounts: Methods and Estimates for the United States\*”
  In *The Quarterly Journal of Economics* 133.2, 2017, pp. 553–609
  DOI: [10.1093/qje/qjx043](https://dx.doi.org/10.1093/qje/qjx043)
* [130]
  Mikkel Plagborg-Møller and Christian K Wolf
  “Local projections and VARs estimate the same impulse responses”
  In *Econometrica* 89.2
  Wiley Online Library, 2021, pp. 955–980
* [131]
  M. Shin and M. Zhong
  “A New Approach to Identifying the Real Effects of Uncertainty Shocks”
  In *Journal of Business & Economic Statistics* 38.2, 2018, pp. 367–379
  DOI: [10.1080/07350015.2018.1506342](https://dx.doi.org/10.1080/07350015.2018.1506342)
* [132]
  Joseph E Stiglitz
  “Macroeconomic fluctuations, inequality, and human development”
  In *Macroeconomics and human development*
  Routledge, 2015, pp. 31–58
* [133]
  Silvana Tenreyro and Gregory Thwaites
  “Pushing on a String: US Monetary Policy Is Less Powerful in Recessions”
  In *American Economic Journal: Macroeconomics* 8.4, 2016, pp. 43–74
  DOI: [10.1257/mac.20150016](https://dx.doi.org/10.1257/mac.20150016)
* [134]
  Harald Uhlig
  “What are the effects of monetary policy on output? Results from an agnostic identification procedure”
  In *Journal of Monetary Economics* 52.2
  Elsevier, 2005, pp. 381–419
* [135]
  Jeffrey M Wooldridge
  “Two-way fixed effects, the two-way Mundlak regression, and difference-in-differences estimators”
  In *Available at SSRN 3906345*, 2021
* [136]
  Ruixin Zhang and Sami Ben Naceur
  “Financial development, inequality, and poverty: Some international evidence”
  In *International Review of Economics & Finance* 61
  Elsevier, 2019, pp. 1–16

## Appendix

## Appendix A Data

GDP is log of real GDP obtained from the European Union Statistical Office (Eurostat) Database; Prices is log GDP deflator from Eurostat; Investment/output is log of investments (Eurostat) over GDP; Stock prices is log of share prices index from the Organisation for Economic Co-Operation and Development (OECD) Database; Interest rate is the short-term interest rate from OECD; Gini index is Gini coefficient of gross market income (percentage) computed from European Union Statistics on Income and Living Conditions (EU-SILC) survey; P90 is the 90th income percentile computed from EU-SILC; P95 is the 95th income percentile computed from EU-SILC; Financial deepening is the ratio between financial assets and GDP expressed in percentage points (Eurostat); CLIFS is the Country-Level Index of Financial Stress from the European Central Bank (ECB); Skill premium is defined as the wage ratio between high-skilled and low-skilled workers in working age, and is constructed using data from EU-SILC; Uncertainity index is the smoothed version of the World Uncertainity Index by [[70](https://arxiv.org/html/2510.11289v1#biba.bibx2)].202020The Uncertainty Index was not available for Estonia and Luxembourg. For Estonia, we imputed the value using the average of the available data for the other Baltic countries (Latvia and Lithuania); for Luxembourg, we used the average of Belgium and the Netherlands. The same approach was applied to impute the missing CLIFS data for Estonia.
  
Data are collected on a quarterly basis. For the outcome variables (Gini index, P90, and P95), which are only available at annual frequency, we apply a standard linear interpolation to get the quarterly figures. This imputation method assumes a uniform quarterly rate of change between annual data points, which aligns with the slow-moving nature of the variables, where intra-annual fluctuations are less common.212121Figure [19](https://arxiv.org/html/2510.11289v1#A4.F19 "Figure 19 ‣ D.7 Alternative interpolation method ‣ Appendix D Robustness ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.") in the Appendix shows that the increase in income inequality following a financial shock is robust to the method used for converting data to quarterly frequency. As a robustness check, we employ a flat interpolation method, assigning the annual value uniformly across all quarters. The CLIFS variable is available at the monthly frequency; to align it with the quarterly frequency of the other series, we compute the quarterly average. GDP, Prices, Investment/output, and Stock prices are multiplied by 100.

## Appendix B PVAR Specification

Our panel VAR specification follows a pooled panel approach, meaning that the only panel feature is that the dataset comprises observations coming from different units (countries). For clarity and consistency with standard practice, we present the VAR directly in its vectorized form:

|  |  |  |  |
| --- | --- | --- | --- |
|  | y=x¯​β+ϵy=\bar{x}\beta+\epsilon |  | (4) |

The parameters of interest are β\beta and Σc\Sigma\_{c} (the unit residual covariance matrix), the former including section-specific constants. Given that the structure is essentially that of a VAR, standard Bayesian estimation techniques for the posterior distribution can be applied. We adopt a traditional Normal–Wishart prior setup, in which β\beta is assumed to follow a multivariate normal distribution and Σc\Sigma\_{c} an inverse Wishart distribution, resulting in corresponding posterior distributions. Parameter values follow the conventional choices documented in [[92](https://arxiv.org/html/2510.11289v1#biba.bibx24)].
  
The implementation of sign restrictions follows the methodology developed by [[74](https://arxiv.org/html/2510.11289v1#biba.bibx6)], and draws are generated through Gibbs sampling. We use a total of 2,000 iterations, with a burn-in of 1,000.
  
Under these settings, the estimation of the baseline model (Table [1](https://arxiv.org/html/2510.11289v1#S3.T1 "Table 1 ‣ 3.1 Identification ‣ 3 Empirical strategy ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.")) completes in approximately one hour, while the nonlinear extension (Table [3](https://arxiv.org/html/2510.11289v1#A5.T3 "Table 3 ‣ Appendix E Nonlinear framework ‣ Disentangling the Distributional Effects of Financial Shocks in the Euro AreaWe thank Dario Bonciani, Cristiano Cantore, Juan José Dolado, Luca Fanelli, Francesco Furlanetto, Carlo Galli, Francesco Lucidi, Lorenzo Mori, Salvatore Nisticò, Evi Pappa, Valeria Patella, Michele Raitano, Luca Riva, Emircan Yurdagul, and all participants at the 5th Sailing the Macro Workshop, the 9th International PhD Meeting in Economics, the Macro-Metrics Sapienza Reading Group, the Macro-Working Progress Carlos III Reading Group, and the Manic Mondays Seminars for helpful comments. This paper is based on data from Eurostat, EU-SILC, 2024. The responsibility for all conclusions drawn from the data lies entirely with the authors. This paper uses data from the Eurosystem Household Finance and Consumption Survey. We acknowledge financial support from the Sapienza University of Rome under the Avvio alla Ricerca 2024 funding program.")) requires around five days.222222Computations are performed on a machine equipped with an Intel(R) Xeon(R) W5-3435X 3.10 GHz processor and 64 GB of RAM.

## Appendix C Additional results

![Refer to caption](x21.png)

Figure 10: The effects of demand shocks on income inequality

The figure shows the response of income inequality after a one-standard-deviation positive generic demand shock occurs. Full lines are point estimates; shaded areas indicate 90% and 68% confidence bands computed from panel HAC standard errors.



![Refer to caption](x22.png)

![Refer to caption](x23.png)

![Refer to caption](x24.png)

![Refer to caption](x25.png)

Figure 11: Skilled vs. unskilled: IRFs to a financial shock of weekly hours and wages

The figure shows the responses of wages (first line) and hours worked per week (second line) for high-skilled (left) and low-skilled (right) workers, after a one-standard-deviation positive financial shock. The solid line represents point estimates, while the shaded areas denote 90% and 68% confidence bands computed from panel HAC standard errors.

## Appendix D Robustness

### D.1 Not including uncertainity controls

![Refer to caption](x26.png)

Figure 12: The effects of financial shocks on income inequality

The figure shows the response of income inequality after a one-standard-deviation positive financial shock occurs not considering the uncertainty controls. Full lines are point estimates; shaded areas indicate 90% and 68% confidence bands computed from panel HAC standard errors.

### D.2 Alternative identification strategy: recursive

![Refer to caption](x27.png)

Figure 13: The effects of financial shocks on income inequality: recursive (Cholesky) identification

The figure shows the response of income inequality to a one-standard-deviation positive financial shock identified using a recursive ordering, with the share price variable placed last. The solid line represents point estimates, while the shaded areas denote the 90% and 68% confidence bands, computed using panel HAC standard errors.

### D.3 Alternative inequality measures

![Refer to caption](x28.png)

Figure 14: The effects of financial shocks on the 90th percentile

The figure shows the response of the 90th percentile to a one-standard-deviation positive financial shock. The solid line represents point estimates, while the shaded areas denote 90% and 68% confidence bands computed from panel HAC standard errors.



![Refer to caption](x29.png)

Figure 15: The effects of financial shocks on the 95th percentile

The figure shows the response of the 95th percentile to a one-standard-deviation positive financial shock. The solid line represents point estimates, while the shaded areas denote 90% and 68% confidence bands computed from panel HAC standard errors.

### D.4 Subsample estimates: excluding the after covid-19 period

![Refer to caption](x30.png)

Figure 16: The effects of financial shocks on income inequality

The figure shows the response of income inequality to a one-standard-deviation positive financial shock. The solid line represents point estimates, while the shaded areas denote 90% and 68% confidence bands computed from panel HAC standard errors. The sample ends in 2019Q4.

### D.5 Subsample estimates: excluding extreme financial shocks

![Refer to caption](x31.png)

Figure 17: The effects of financial shocks on income inequality

The figure shows the response of income inequality to a one-standard-deviation financial shock. The solid line represents point estimates, while the shaded areas denote 90% and 68% confidence bands computed from panel HAC standard errors. Latvia and the Netherlands are excluded from the sample.

### D.6 Credit shock

Table 2: Sign Restrictions

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Supply | Demand | Monetary | Investment | Financial | Credit |
| GDP | + | + | + | + | + | + |
| Prices | −- | + | + | + | + | + |
| Interest rate |  | + | −- | + | + | + |
| Investment/output |  | −- |  | + | + | + |
| Stock prices | + |  |  | −- | + | + |
| Credit/Stock prices |  |  |  |  | - | + |

Signs represent imposed set-based restrictions at impact. A blank space indicates an unrestricted response.



![Refer to caption](x32.png)

Figure 18: The effects of credit shocks on income inequality

The figure shows the response of income inequality to a one-standard-deviation credit shock. The solid line represents point estimates, while the shaded areas denote 90% and 68% confidence bands computed from panel HAC standard errors.

### D.7 Alternative interpolation method

![Refer to caption](x33.png)

Figure 19: Income inequality response using flat interpolation

The figure displays the response of income inequality to a one-standard-deviation positive financial shock, with the series converted to quarterly frequency using flat interpolation. The solid line represents the point estimate, while the shaded area indicates 68% and 90% confidence intervals computed from panel HAC standard errors.

## Appendix E Nonlinear framework

Table 3: Sign Restrictions

|  | Supply | Demand | Monetary | Investment | Financial (positive) | Financial (negative) |
| --- | --- | --- | --- | --- | --- | --- |
| GDP | + | + | + | + | + | - |
| Prices | −- | + | + | + | + | - |
| Interest rate |  | + | −- | + | + | - |
| Investment/output |  | −- |  | + | + | - |
| Stock prices | + |  |  | −- | + | - |
| Stock price volatility |  |  |  |  | + | + |

Signs represent imposed set-based restrictions at impact. A blank space indicates an unrestricted response.

### E.1 Alternative nonlinear specification

![Refer to caption](x34.png)

Figure 20: The asymmetric distributional effects of financial shocks

The figure shows the response of income inequality to a one-standard-deviation positive (black) and negative (blue) financial shock. The solid line represents point estimates, while the shaded areas denote 68% confidence bands computed from panel HAC standard errors. The nonlinearity here is modeled as in [[133](https://arxiv.org/html/2510.11289v1#biba.bibx65)].

## Appendix F Comparison of financial holdings in EU-SILC and HFCS data

To compare the distribution of financial income across the two datasets and assess potential underreporting in EU-SILC, we focus on the year 2017, which is available in both data sources, and on the same set of countries used in the primary analysis (excluding Lithuania, which is not considered in the HFCS).
  
The construction of the financial income variable was carried out as consistently as possible across datasets, following the definitions provided in the Methodological Guidelines and Description of EU-SILC Target Variables issued by the European Commission (2023 version).
  
In the ECB dataset (HFCS), the relevant variable is “Gross Income from Financial Investment” (HG0410).

![Refer to caption](Appendix/Income_distribution/Financial_income_holdings_EU_SILC.png)

Figure 21: Financial income distribution in the Euro Area (2017) - EU-SILC

The figure shows the share of total financial income held by each individual, with individuals ranked according to their position in the overall income distribution. Top earners (those in the 99th percentile) are excluded from the graphical representation for visibility purposes. The underlying data are from the EU-SILC survey.



![Refer to caption](Appendix/Income_distribution/Financial_income_holdings_ECB.png)

Figure 22: Financial income distribution in the Euro Area (2017) - HFCS

The figure shows the share of total financial income held by each individual, with individuals ranked according to their position in the overall income distribution. Top earners (those in the 99th percentile) are excluded from the graphical representation for visibility purposes. The underlying data are from the HFCS survey.