---
authors:
- Riddhi Kalsi
doc_id: arxiv:2510.16626v1
family_id: arxiv:2510.16626
is_current: true
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: 'Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages
  in France'
url_abs: http://arxiv.org/abs/2510.16626v1
url_html: https://arxiv.org/html/2510.16626v1
venue: arXiv q-fin
version: 1
year: 2025
---


Riddhi Kalsi
Sciences Po, Paris; riddhi.kalsi@sciencespo.fr

###### Abstract

\justify

This paper resolves the empirical puzzle in the public–private wage literature: why studies using similar data reach contradictory conclusions about wage premiums and penalties. Utilizing rich French administrative panel data (2012–2019), this study has two main contributions: first, it presents a set of new, intuitive yet previously undocumented stylized facts about wage dynamics, sectoral mobility, and gender differences across sectors. The results reveal that the modest hourly wage gaps conceal substantial disparities in lifetime earnings and employment stability. Women, in particular, gain a significant lifetime earnings advantage in the public sector, driven by higher retention, better-compensated part-time work, and more equitable annual hours compared to the private sector, where gender gaps remain larger, especially for those with higher education. In contrast, highly educated men experience a lifetime penalty in public employment due to rigid wage structures. By flexibly modeling sectoral transitions, transitions into and out of employment, and earnings heterogeneity using an Expectation-Maximization algorithm, this study shows that both premiums and penalties depend systematically on gender, education, and labor market experience. The analysis reveals that significant unobserved heterogeneity remains in wage dynamics. These findings unify prevailing narratives by providing a comprehensive, descriptive account of sectoral differences in transitions, part-time work and wages by gender.

††Acknowledgement: 
This work was supported by the European Research Council (grant reference ERC-2020-ADG-101018130) and the Agence Nationale de la Recherche (grant reference ANR-19-CE26-0007-01) awarded to Jean-Marc Robin.

This empirical puzzle stems from valuable but distinct methodological approaches and sample selection criteria to studying public-private wage differentials. Most studies fall into two distinct camps: those using fixed-effects regressions on hourly wages111[Bargain and Melly, [2008](https://arxiv.org/html/2510.16626v1#bib.bib1)] and more recent work [Bargain and Melly, [2008](https://arxiv.org/html/2510.16626v1#bib.bib1)] and those employing dynamic lifetime approaches on monthly or annual wages222[Beffy and Kamionka, [2010](https://arxiv.org/html/2510.16626v1#bib.bib2), Dickson et al., [2014](https://arxiv.org/html/2510.16626v1#bib.bib3)]. However, neither approach simultaneously incorporates the key elements that explain contradictory empirical findings. At its heart, the public-private wage gap question is: “For a given person, what is the effect of working in the public sector on their wage, compared to if they had worked in the private sector?". The epistemological problem is that we can never observe this counterfactual. We cannot see the same person in both sectors at the same time. Therefore, any statistical method is an attempt to construct a plausible counterfactual group to compare against.

The choice of method dictates the nature of that counterfactual and thus defines what we are actually claiming to know. Fixed effects regressions estimate the wage gap for people who switch sectors, averaging over switchers their wages before and after the sectoral change while controlling for innate, time-invariant traits. Lifetime earnings approaches with selection models estimate the expected gap for the entire population, using statistical techniques to simulate what a typical person would earn in either sector by accounting for job loss risk and the preexisting differences that lead people to choose one sector over the other.

The answer to this empirical conundrum thus lies in the methodology used. Fixed-effects studies on hourly wages, while controlling for unobserved heterogeneity, focus on hourly wages and miss the differential impact of hours worked—particularly relevant given women’s higher propensity for part-time work. Meanwhile, lifetime approaches account for job security through employment transitions but have either been limited to male-only samples, or have not allowed for free movement between the sectors. This study uses the former method only in section [2](https://arxiv.org/html/2510.16626v1#S2 "2 Stylized facts ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") and the latter for the main results due to its advantages in taking job stability and annual wages (as a result of heterogeneous labor supply) into account, and statistically modeling sectoral stayers as well as movers. It turns out, that allowing for sector switching in a lifetime earnings approach doesn’t make a big difference in estimating lifetime earnings in either sector as this study shows that sector-switching is relatively rare in the French context (in subsection [2.1](https://arxiv.org/html/2510.16626v1#S2.SS1 "2.1 Sector-switching is rare…but not random ‣ 2 Stylized facts ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France")). A note of caution here, the counterfactual lifetime earnings presented in this analysis assume that neither public nor private sector parameters (in terms of wages, employment, job retention and mobility) change. This gives the analysis a more descriptive rather than causal flavor.

This study makes three key contributions. First, I demonstrate that seemingly modest hourly wage gaps between public and private sectors mask profound disparities in lifetime earnings, with the public sector exhibiting gender gaps 13% lower than the private sector on average across earnings quantiles through better retention and compensation for part-time work—a mechanism overlooked in prior hourly wage comparisons. Second, the study builds on the current literature by simultaneously examining gender dynamics, unobserved heterogeneity333A critical issue in estimating the public-private wage gap is selection bias, which arises because public sector jobs often attract individuals with different preferences, skills, or motivations compared to those in the private sector. [Heckman and Singer, [1984](https://arxiv.org/html/2510.16626v1#bib.bib4)] famously introduced the selection correction technique, which allows researchers to account for such unobserved differences and has been extended and applied by [Beffy and Kamionka, [2010](https://arxiv.org/html/2510.16626v1#bib.bib2)] in looking at the public pay gap in France. For instance, public sector workers may have a stronger preference for job security or non-wage benefits like pensions, which can complicate comparisons with private sector employees who may prioritize higher pay or career mobility. Studies that fail to account for this selection bias risk over- or under-estimating the true wage differential.
  
Based on the above analysis, one could argue that there is self-selection of women into the public sector; that is, women prefer (or ”select” themselves) to be in the public sector wherever possible. Therefore, comparing these jobs held by women in the public sector to private sector employment will mechanically give a positive public premium as agents are rational. On looking more closely, one realizes that a priori there is no reason to assume that only women self-select into the public sector. With rational agents in society, we expect that any individual is selecting the sector most suitable for them. Hence, the same argument can be made for men’s self-selection to the public sector, and to that effect we should find similar public premia by gender and earnings percentiles, which is not the case in this setting as it is higher for women extensively and intensively. This is not a complete measure of self-selection but of the different outcomes women have compared to men.
, unrestricted sectoral mobility, and lifetime earnings. Women disproportionately sort into stable public roles due to both observable traits like education and latent factors shaping career trajectories444This is echoed in [Fougère and Pouget, [2003](https://arxiv.org/html/2510.16626v1#bib.bib5), Garibaldi et al., [2021](https://arxiv.org/html/2510.16626v1#bib.bib6), Gomes and Kuehn, [2025](https://arxiv.org/html/2510.16626v1#bib.bib7)]. Third, the analysis reveals a critical equity-efficiency trade-off: while the public sector insulates workers from volatility, it imposes lifetime earnings penalties on highly educated workers due to rigid wage structures. The core idea of this study is to provide a nuanced understanding of public-private earnings differences; that penalties or premiums are not universal features of either sector.

By utilizing a sequential Expectation-Maximization (EM) algorithm on French panel data that include men, women, full-time and part-time work, and allows for sector-switching, I find that public sector employment offers a significant lifetime earnings premium for women but imposes penalties for highly educated men. The methodology simultaneously estimates individual income trajectories, employment dynamics, and selection into sectors, allowing for unobserved heterogeneity in earnings patterns and sector choice. Considering lifetime values accounts for not just wage levels but also the security of income over an entire career, particularly in the face of job loss risk. [Garbinti et al., [2023](https://arxiv.org/html/2510.16626v1#bib.bib8)] highlight the importance of incorporating lifetime earnings into gender pay gap analyses, showing that short-term wage differences underestimate long-term disparities. [Guvenen et al., [2021](https://arxiv.org/html/2510.16626v1#bib.bib9)] further argue that income volatility and employment uncertainty significantly shape utility-based job preferences, particularly for risk-averse individuals who may select into the public sector for its greater stability.

This work unifies two main strands of literature on France. While [Bargain et al., [2018](https://arxiv.org/html/2510.16626v1#bib.bib10), Bargain and Melly, [2008](https://arxiv.org/html/2510.16626v1#bib.bib1)] report hourly wage penalties for educated workers, [Beffy and Kamionka, [2010](https://arxiv.org/html/2510.16626v1#bib.bib2), Dickson et al., [2014](https://arxiv.org/html/2510.16626v1#bib.bib3)] find lifetime premia using monthly earnings and accounting for selection. This paper shows that hourly wages mask profound lifetime disparities driven by part-time work and unobserved selection. France’s institutional features—centralized wage bargaining, regulated hours, and strong job protection—position it as a prototype of coordinated market economies where similar dynamics operate.

The public sector’s role as a mitigator of gender inequality is increasingly relevant as fiscal pressures and privatization debates intensify. The gender pay gap is a well-documented phenomenon, consistently showing that women earn less than men across various sectors and countries (for example, [Blau and Kahn, [2017](https://arxiv.org/html/2510.16626v1#bib.bib11), Goldin, [2014](https://arxiv.org/html/2510.16626v1#bib.bib12), Petersen and Morgan, [1995](https://arxiv.org/html/2510.16626v1#bib.bib13)], etc.). In high-income countries, the compatibility of women’s career and family goals, facilitated by family policy, cooperative fathers, favorable social norms, and flexible labor markets, has become key drivers of fertility and participation in the labor force [Bertrand et al., [2010](https://arxiv.org/html/2510.16626v1#bib.bib14)]. [Goldin, [2014](https://arxiv.org/html/2510.16626v1#bib.bib12)] argues that while gender convergence in labor market outcomes has progressed significantly, workplace flexibility remains a key obstacle, a factor that is particularly relevant in explaining the persistent gender wage gap between public and private sectors - similarly, this study echoes the disparities in compensated hours by gender. Extensive research has explored multiple dimensions of this disparity, including differences in occupation, industry, work experience, education, and discrimination. However, a crucial aspect that warrants further attention is the variation in gender pay gaps between the private and public sectors over a lifetime. This article contributes to the existing body of literature by demonstrating that the private sector imposes a larger gender pay gap when compared to the public sector when considering lifetime earnings. Prior work highlights shrinking gender wage gaps in countries with large public sectors [Ponthieux and Meurs, [2015](https://arxiv.org/html/2510.16626v1#bib.bib15)], but few studies examine lifetime earnings or part-time work comprehensively. This paper resolves existing contradictions by modeling annual earnings and incorporating part-time employment—critical for women, who constitute 75% of part-time workers in France.

This article proceeds as follows: Section [1](https://arxiv.org/html/2510.16626v1#S1 "1 Data ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") describes the data and briefly, some institutional context. Section [2](https://arxiv.org/html/2510.16626v1#S2 "2 Stylized facts ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") provides descriptive evidence and some stylized facts that support the statiscal model that is later specified in section [3](https://arxiv.org/html/2510.16626v1#S3 "3 Model ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"). Section [4](https://arxiv.org/html/2510.16626v1#S4 "4 Model Fit ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") presents the unobserved heterogeneity analysis along with model fit both in- and out-of-sample. Section [5](https://arxiv.org/html/2510.16626v1#S5 "5 Results: Public and Gender Premia in Lifetime Earnings ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") documents the main results. After a discussion on points for future research in section [6](https://arxiv.org/html/2510.16626v1#S6 "6 Discussion ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"), section [7](https://arxiv.org/html/2510.16626v1#S7 "7 Conclusion ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") concludes.

## 1 Data

### 1.1 Data description

This study uses the DADS-EDP tous salariés panel for 2012-2019, combining the DADS "all-employees" panel with the Échantillon Démographique Permanent (EDP). The DADS panel provides comprehensive employee and job information from annual employer declarations and state payroll files. The EDP adds demographic data from civil status records and surveys for individuals born on October 1st and 4th. The datasets are matched via registration index numbers, allowing education levels to be determined from survey responses.

A key development in the data is the integration of DSN (Déclaration Sociale Nominative) information starting in 2016, which streamlined social declarations for French companies 555[https://www.insee.fr/en/information/4195367?sommaire=4195376](INSEE%20-%20Understanding%20the%20Nominative%20Social%20Declaration%20(DSN)%20for%20Better%20Statistical%20Measurement). By 2017, the DSN became mandatory for most private sector companies, and by 2018, 99% of private companies had adopted it. This transition expanded the dataset’s scope to include both private and public sector employees, as well as employees of individual employers, enabling more comprehensive analysis of employment and wages across the French economy.

### 1.2 Sample selection and statistics

The panel used in this analysis consists of 276,514 individuals (training data) which is a randomly selected quarter of the larger sample consisting of 829,232 individuals (used to check for out-of-sample model fit). The latter is a random sample that is representative of the French working population. The sample size is purposely kept large to better inform the dynamic model of the heterogeneity in mobility and income over time. The total number of panel observations including spells of non-employment total 2,065,902. Individuals aged 18-60 who have completed their education prior to or during the observed time-periods are kept to avoid peculiarities (apprenticeship for young workers, and early retirement in the public sector, for example). Employment spells that total atleast 6 months or 180 days in a year are used for the analysis 666This construction includes employment spells across multiple employers within a sector, allowing for a more flexible approach than typical full-year, single-employer restrictions. If total employment in a year is less than 6 months, that year is coded as a non-employment spell. See Appendix [A.1](https://arxiv.org/html/2510.16626v1#A1.SS1 "A.1 Panel Construction ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") for further details on panel construction.. The log of real net annual wages or "salaire net fiscal en euros constants" is used throughout. Using real net wages provides a more accurate representation of workers’ purchasing power by accounting for all social contributions and eliminating inflation effects. This measure offers a standardized basis for comparison across sectors and time periods, reflecting the real economic situation of workers more effectively than gross salary figures.

Education is coded as a categorical variable with the three levels: high (some university qualification), medium (some vocational training post high school), and low (at most a high school degree). Table [A.1](https://arxiv.org/html/2510.16626v1#T1a "Table A.1 ‣ A.1 Panel Construction ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") tabulates this classification and and provides U.S. equivalents. In the sample, approximately 69% of individuals in the panel had a low education level, 16% medium, and 15% high.

Table 1: Descriptive Statistics by Employment Type and Sector

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | Full-time spells (79%) | | Part-time spells (21%) | |
|  |  | Public | Private | Public | Private |
| Employment share (%) | | 24 | 76 | 26 | 74 |
| Log real net annual wage | Mean | 10.19 | 10.14 | 9.58 | 9.32 |
| (sd) | (0.35) | (0.49) | (0.69) | (0.87) |
| Log real net hourly wage | Mean | 2.69 | 2.65 | 2.56 | 2.42 |
| (sd) | (0.32) | (0.42) | (0.32) | (0.41) |
| Demographics | | | | | |
| Share of Women (%) | | 61 | 36 | 84 | 77 |
| Low Education (%) | | 52 | 68 | 56 | 74 |
| Med Education (%) | | 21 | 17 | 23 | 14 |
| High Education (%) | | 28 | 15 | 21 | 12 |
| Ages ≤\leq 30 (%) | | 11 | 18 | 11 | 16 |
| Ages 31-45 (%) | | 41 | 43 | 44 | 39 |
| Ages 45+ (%) | | 49 | 39 | 44 | 45 |
| # panel observations | | 1,142,309 | | 299,721 | |
| # individuals | | 276,514 | | | |

Table [1](https://arxiv.org/html/2510.16626v1#T1 "Table 1 ‣ 1.2 Sample selection and statistics ‣ 1 Data ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") presents descriptive statistics for full-time and part-time employment spells, broken down by public and private sectors. Full-time employment accounts for 79% of spells, with a larger share in the private sector (76%) compared to the public sector (24%). Part-time employment constitutes 21% of spells, with similar sectoral proportions (26% public, 74% private). The mean log real net annual wage is slightly higher in the public sector than in private. This pattern persists for part-time workers, with mean log annual wages of 9.58 in the public sector and 9.32 in the private sector. Similarly, hourly wages are marginally higher in the public sector for both full-time and part-time workers.

Demographic differences are notable. Women dominate public sector employment (61% for full-time and 84% for part-time) compared to the private sector (36% and 77%, respectively). Public sector employees also exhibit higher levels of education, with 28% of full-time and 21% of part-time workers having high education, versus 15% and 12% in the private sector. Private sector workers tend to be younger, with 18% under 30 in full-time roles, compared to 11% in the public sector.

Women dominate part-time employment, accounting for 79% of part-time spells across both public and private sectors, which represents 17% of aggregate employment during the observed period. Among women’s employment spells, part-time work varies inversely with education level: 37% for low-educated, 28% for medium-educated, and 24% for highly educated women. This pattern suggests an inverse relationship between educational attainment and the propensity for part-time work among women.

## 2 Stylized facts

In these sub-sections, I present some novel evidence from the panel that motivates the estimation strategy presented in the next section. These nuances are key to understanding public-private differences and are seldom consolidated in a single narrative. The findings are intuitive, but are nonetheless important to quantify.

### 2.1 Sector-switching is rare…but not random

Table [2](https://arxiv.org/html/2510.16626v1#T2 "Table 2 ‣ 2.2 Women and men move differently in the labor market ‣ 2 Stylized facts ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") above highlights how rare sector-switching is, particularly when considering full-time employment. Year-on-year a mere 1.2% switch sectors in full-time jobs. In prior works on the subject leveraging fixed-effects, identification relies on the assumption that sector switching is random - more specifically, that changes in wage are orthogonal to switching sectors. This assumption appears plausible when examining hourly wage changes, as shown in figures [1(a)](https://arxiv.org/html/2510.16626v1#S2.F1.sf1 "In Figure 1 ‣ 2.1 Sector-switching is rare…but not random ‣ 2 Stylized facts ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") and [1(b)](https://arxiv.org/html/2510.16626v1#S2.F1.sf2 "In Figure 1 ‣ 2.1 Sector-switching is rare…but not random ‣ 2 Stylized facts ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") , where the wage distribution across sectors shows limited patterns of systematic variation among movers. The pre-trend of stayers and movers is similar. However, when analyzing annual wage changes, a different narrative emerges. Figures [1(c)](https://arxiv.org/html/2510.16626v1#S2.F1.sf3 "In Figure 1 ‣ 2.1 Sector-switching is rare…but not random ‣ 2 Stylized facts ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") and [1(d)](https://arxiv.org/html/2510.16626v1#S2.F1.sf4 "In Figure 1 ‣ 2.1 Sector-switching is rare…but not random ‣ 2 Stylized facts ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") suggest that sector switching is systematically associated with an increase in earnings in both directions (although a smaller increase when transitioning into the public sector). Here, we can observe a strong Ashenfelter dip in earnings for switchers. This pre-trend of falling wages for switchers whose earnings then increase on switching sectors suggests that sector-switching is not orthogonal to wages. This discrepancy between hourly and annual wages gives reason to revisit the assumption of randomness, as movers may be selecting sectors based on broader income considerations than hourly wage rates alone.

![Refer to caption](x1.png)


(a) Hourly Wage Changes - Public Sector Switchers and Stayers

![Refer to caption](x2.png)


(b) Hourly Wage Changes - Private Sector Switchers and Stayers

![Refer to caption](x3.png)


(c) Annual Wage Changes - Public Sector Switchers and Stayers

![Refer to caption](x4.png)


(d) Annual Wage Changes - Private Sector Switchers and Stayers

Figure 1: Distributions of Hourly and Annual Wage Changes

### 2.2 Women and men move differently in the labor market

Table [2](https://arxiv.org/html/2510.16626v1#T2 "Table 2 ‣ 2.2 Women and men move differently in the labor market ‣ 2 Stylized facts ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") presents transition probabilities across employment states, comparing non-employment, private, and public sector (full-time and part-time) employment segmented by gender777Note that these figures imply an inactivity rate of about one-third (referred to as non-employment in this study), and private:public sector employment ratio of approximately 75:25 as share of all employment. These figures are in line with national statistics published [here](https://www.insee.fr/fr/statistiques/3676623?sommaire=3696937) and [here](https://www.insee.fr/en/statistiques/4997371).. Key findings are: first, the higher persistence in employment status within both public and private sectors, as evidenced by high probabilities for remaining in the same employment type (e.g., 0.89 for private full-time and 0.93 for public full-time).

Table 2: Transition Probabilities (Aggregate, Men, Women)

| From/To | NE | Pvt FT | Pub FT | Pvt PT | Pub PT |
| --- | --- | --- | --- | --- | --- |
| Aggregate | | | | | |
| Non-employment (NE) | 0.82 | 0.11 | 0.02 | 0.04 | 0.01 |
| Private full-time (Pvt FT) | 0.08 | 0.89 | 0.002 | 0.03 | 0.0004 |
| Public full-time (Pub FT) | 0.02 | 0.006 | 0.93 | 0.0015 | 0.04 |
| Private part-time (Pvt PT) | 0.17 | 0.12 | 0.004 | 0.7 | 0.005 |
| Public part-time (Pub PT) | 0.10 | 0.01 | 0.13 | 0.01 | 0.75 |
| Total | 0.31 | 0.42 | 0.13 | 0.10 | 0.04 |

|  | Men | | | | | Women | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| From/To | NE | Pvt FT | Pub FT | Pvt PT | Pub PT | NE | Pvt FT | Pub FT | Pvt PT | Pub PT |
| NE | 0.83 | 0.13 | 0.01 | 0.02 | 0.005 | 0.81 | 0.08 | 0.02 | 0.06 | 0.02 |
| Pvt FT | 0.08 | 0.90 | 0.002 | 0.02 | 0.0003 | 0.09 | 0.86 | 0.003 | 0.05 | 0.001 |
| Pub FT | 0.02 | 0.006 | 0.95 | 0.001 | 0.02 | 0.03 | 0.006 | 0.92 | 0.002 | 0.05 |
| Pvt PT | 0.22 | 0.22 | 0.004 | 0.55 | 0.004 | 0.15 | 0.09 | 0.004 | 0.74 | 0.01 |
| Pub PT | 0.15 | 0.02 | 0.15 | 0.01 | 0.67 | 0.09 | 0.01 | 0.13 | 0.01 | 0.76 |
| Total | 0.31 | 0.53 | 0.10 | 0.05 | 0.01 | 0.31 | 0.31 | 0.16 | 0.16 | 0.06 |

Notably, men exhibit greater stability in private full-time roles (0.90) compared to women (0.86). Second, transition rates into part-time roles show a gender disparity: women are more than twice as likely as men to move into part-time jobs (0.05 vs. 0.02) from full-time positions in both sectors. They also remain in part-time roles more often, with less than half the probability of transitioning to private full-time jobs compared to men. Men are more likely to move from non-employment to private full-time roles, underscoring gender disparities in workforce re-entry.

#### 2.2.1 The Part-Time Paradox: Women’s Dominance in Flexible Work

A significant advantage of using the DADS data is that it allows us to observe the hours workers are compensated for, including paid time off. In other data sources, respondents are asked how many hours they work on average, or in that week, like in the Labor Force survey. In a study like this, where we want to be able to predict transitions and wages over a lifetime, having accurate and administrative records is crucial to avoid recall bias and measurement errors that can arise from self-reported data. This precision ensures a more reliable estimation of lifetime earnings trajectories and sectoral transitions, which are key to understanding long-term labor market dynamics.

Women’s labor supply significantly differs from men’s across public and private employment sectors, as evidenced by disparities in compensated hours captured through administrative data. Table [3](https://arxiv.org/html/2510.16626v1#T3 "Table 3 ‣ 2.2.1 The Part-Time Paradox: Women’s Dominance in Flexible Work ‣ 2.2 Women and men move differently in the labor market ‣ 2 Stylized facts ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") highlights key differences in average annual compensated hours between men and women across employment types. In both full-time public and private sectors, men consistently have more compensated hours on average than women, with the gap being more pronounced in the private sector. For example, in the full-time private sector, men are compensated for 63.57 more hours annually than women (roughly translates to two weeks), while in the public sector, this difference narrows to 20.65 hours. These trends suggest that the public sector offers more equitable compensation structures for women compared to the private sector.

Table 3: Gender Differences in Compensated Hours by Sector and Employment Type

|  |  | Observations | | Average Annual Hours | | Difference |
| --- | --- | --- | --- | --- | --- | --- |
| Type | Sector | Men | Women | Men | Women |  |
| Full-time | Private | 552,026 | 315,664 | 1,833.399 | 1,769.83 | 63.569\*\*\* |
|  | Public | 107,911 | 165,376 | 1,817.262 | 1,796.615 | 20.647\*\*\* |
| Part-time | Private | 51,769 | 170,255 | 1,111.697 | 1,226.44 | -114.743\*\*\* |
|  | Public | 10,546 | 64,053 | 1,110.931 | 1,287.2 | -176.27\*\*\* |

Note: The last column "Difference" is the difference in compensated hours between and women for each employment state and the \*s denote the significance of t-tests (with uneqal variances) for these differences.

Women’s labor supply patterns reveal a striking paradox across public and private employment sectors. Table [3](https://arxiv.org/html/2510.16626v1#T3 "Table 3 ‣ 2.2.1 The Part-Time Paradox: Women’s Dominance in Flexible Work ‣ 2.2 Women and men move differently in the labor market ‣ 2 Stylized facts ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") illustrates that while men consistently have more compensated hours on average in full-time roles, this trend reverses dramatically for part-time work. In the full-time private sector, men are compensated for 63.57 more hours annually than women. However, in part-time roles, women significantly outpace men in compensated hours, with the most pronounced difference in the public sector where women log 176.27 more hours annually than their male counterparts. This part-time paradox is further emphasized by the prevalence and persistence of part-time work among women: it accounts for 32% of women’s employment compared to just 9% for men, and women are less likely to transition out of these roles. These findings suggest that part-time work, particularly in the public sector, may be serving as a long-term strategy for women to balance work and other responsibilities, rather than a temporary state as it appears to be for men. Women’s compensation within part-time employment is higher both in terms of annual and hourly wages in the public sector. A breakdown by education levels further reveals that the patterns in compensated hours persist across all categories (with higher educational attainment mitigating the gender gap in hours), with the public sector showing smaller differences in full-time compensated hours between men and women and larger differences in part-time compensated hours.

### 2.3 Differences in earnings are larger in the private sector, especially for educated workers

The analysis of wage differentials in France reveals persistent pay gaps between men and women that are more pronounced in the private sector, particularly for highly educated workers. Using OLS regressions on log wages, women earn 14.3% less in annual wages and 14.7% less in hourly wages compared to men, controlling for other factors (Table [4](https://arxiv.org/html/2510.16626v1#T4 "Table 4 ‣ 2.3 Differences in earnings are larger in the private sector, especially for educated workers ‣ 2 Stylized facts ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France")). However, this gap narrows in the public sector, as evidenced by the positive interaction between female and full-time public sector employment (5.4% for annual wages and 3.8% for hourly wages) extracted from an alternate specification888Refer to table [A.3](https://arxiv.org/html/2510.16626v1#T3a "Table A.3 ‣ Income and non-employment Statistics ‣ A.2 Descriptives ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") in the appendix.. Figure [2](https://arxiv.org/html/2510.16626v1#S2.F2 "Figure 2 ‣ 2.3 Differences in earnings are larger in the private sector, especially for educated workers ‣ 2 Stylized facts ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") which graphs mean wages by sector and sex alludes to these differences in annual pay across the sectors by gender. The trajectory of men in the private sector is, for the most part, indistinguishable from those in the public sector as there is a significant overlap. Conversely, for women, there is no overlap in the public and private sector earnings as the public sector trajectory lies squarely above that of the private sector.

![Refer to caption](x5.png)


(a) Low Education

![Refer to caption](x6.png)


(b) High Education

Figure 2: Annual wage dispersion by sector, sex and sector, over experience




Table 4: Key Regression Results (Log Wages)

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | OLS | | Panel Fixed effects | | Panel Fixed Effects by Gender | | | |
| Variable | Annual | Hourly | Annual | Hourly | Men | Men | Women | Women |
|  | Wage | Wage | Wage | Wage | Annual | Hourly | Annual | Hourly |
| Female | -0.143\*\*\* | -0.147\*\*\* |  |  |  |  |  |  |
|  | (0.001) | (0.001) |  |  |  |  |  |  |
| Full-time Public | -0.025\*\*\* | -0.047\*\*\* | 0.087\*\*\* | 0.016\*\*\* | -0.013\*\*\* | -0.013\*\*\* | 0.148\*\*\* | 0.023\*\*\* |
|  | (0.001) | (0.001) | (0.003) | (0.001) | (0.004) | (0.002) | (0.004) | (0.002) |
| Part-time Private | -0.717\*\*\* | -0.157\*\*\* | -0.370\*\*\* | 0.059\*\*\* | -0.370\*\*\* | 0.097\*\*\* | -0.365\*\*\* | 0.035\*\*\* |
|  | (0.002) | (0.001) | (0.001) | (0.001) | (0.002) | (0.001) | (0.002) | (0.001) |
| Part-time Public | -0.546\*\*\* | -0.104\*\*\* | -0.221\*\*\* | 0.062\*\*\* | -0.470\*\*\* | 0.046\*\*\* | -0.129\*\*\* | 0.065\*\*\* |
|  | (0.002) | (0.001) | (0.003) | (0.001) | (0.005) | (0.003) | (0.004) | (0.002) |
| Medium Education | 0.300\*\*\* | 0.269\*\*\* |  |  |  |  |  |  |
|  | (0.001) | (0.001) |  |  |  |  |  |  |
| High Education | 0.545\*\*\* | 0.531\*\*\* |  |  |  |  |  |  |
|  | (0.001) | (0.001) |  |  |  |  |  |  |
| Experience (per decade) | 0.459\*\*\* | 0.308\*\*\* | -0.305\*\*\* | 0.536\*\*\* | 0.637\*\*\* | 0.460\*\*\* | 0.546\*\*\* | 0.355\*\*\* |
|  | (0.002) | (0.001) | (0.009) | (0.005) | (0.003) | (0.002) | (0.004) | (0.002) |
| Experience Squared | -0.082\*\*\* | -0.049\*\*\* | -0.081\*\*\* | -0.053\*\*\* | -0.107\*\*\* | -0.062\*\*\* | -0.074\*\*\* | -0.041\*\*\* |
|  | (0.000) | (0.000) | (0.001) | (0.000) | (0.001) | (0.000) | (0.001) | (0.000) |
| Observations | 1,441,964 | 1,437,538 | 1,441,964 | 1,437,538 | 725,048 | 722,229 | 716,916 | 715,309 |
| Number of individuals | 248,084 | 247,586 | 248,084 | 247,586 | 123,663 | 123,321 | 124,421 | 124,265 |
| Year fixed effects | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Rho |  |  | 0.938 | 0.925 | 0.870 | 0.901 | 0.828 | 0.898 |
| Standard errors in parentheses | | | | | | |  |  |
| \*\*\* p<0.01, \*\* p<0.05, \* p<0.1 | | | | | | |  |  |

Part-time employment significantly impacts wages, with substantial penalties observed. Part-time private sector workers earn 71.7% less in annual wages and 15.7% less in hourly wages relative to full-time private sector workers. However, public part-time employment appears to offer better wage outcomes than private part-time employment. The panel fixed effects regression results presented in Table [4](https://arxiv.org/html/2510.16626v1#T4 "Table 4 ‣ 2.3 Differences in earnings are larger in the private sector, especially for educated workers ‣ 2 Stylized facts ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") show that while both types of part-time work are associated with lower annual wages compared to full-time private sector work, the penalty is smaller for public part-time work (-12.9% for women) compared to private part-time work (-36.5% for women). The high rho indicates that most of the variance is due to individual fixed effects rather than idiosyncratic errors. Moreover, public part-time work is associated with modestly higher hourly wages (6.5% increase for women) compared to full-time private sector work, while private part-time work shows a smaller hourly wage premium (3.5% for women) - the slightly higher wage rates for part-time work is possibly a compensating differential.

Education plays a crucial role in wage determination, with higher education associated with substantial wage premia. Medium education increases wages by about 30%, while high education increases wages by approximately 54% compared to low education. However, the returns to education differ between sectors and genders. Experience contributes significantly to wage differentials, with wages increasing at a decreasing rate. The coefficient for experience (per decade) is 45.9% for annual wages and 30.8% for hourly wages, with negative squared terms indicating diminishing returns. The public sector shows slightly higher returns to experience, with an additional 1.4% increase per decade for annual wages. While the public sector appears to offer a more equitable environment, especially for women and those with more experience, substantial gender pay gaps persist across both sectors, particularly for highly educated workers in the private sector. The advantage of public sector employment is especially pronounced for part-time workers, offering better wage outcomes compared to private sector part-time employment.

## 3 Model

The methodology in this study adapts the framework developed in a seminal paper on the public pay gap in Britain Postel-Vinay and Turon [[2007](https://arxiv.org/html/2510.16626v1#bib.bib16)], later extended in Dickson et al. [[2014](https://arxiv.org/html/2510.16626v1#bib.bib3)]. The components directly borrowed from those papers are detailed in Appendix [A.3](https://arxiv.org/html/2510.16626v1#A1.SS3 "A.3 Model ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"). For clarity and readability, the main likelihood equations ([1](https://arxiv.org/html/2510.16626v1#S3.E1 "In 3.1 Structure ‣ 3 Model ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") and [2](https://arxiv.org/html/2510.16626v1#S3.E2 "In 3.1 Structure ‣ 3 Model ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France")) and the lifetime earnings equation ([5](https://arxiv.org/html/2510.16626v1#S5 "5 Results: Public and Gender Premia in Lifetime Earnings ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France")) are retained in the main text, even though they closely mirror those in the earlier work. Likewise, the model structure outlined in Section [3.1](https://arxiv.org/html/2510.16626v1#S3.SS1 "3.1 Structure ‣ 3 Model ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") follows a similar naming convention but differs in several key components.

The main methodological adaptation in this paper lies in the specification of the income process. Whereas the earlier studies used an AR2 framework with restrictive sample selection, log earnings here are modeled as a more flexible AR1 process. This approach avoids sample selection restrictions, captures the persistence of log wages, and allows for the influence of both stochastic noise and covariate-driven variation.

The resulting dynamic model jointly estimates income trajectories, employment dynamics, and sectoral choice, while incorporating unobserved heterogeneity. The details on the sequential EM used is detailed in section [A.4](https://arxiv.org/html/2510.16626v1#A1.SS4 "A.4 Estimating the mobility and income parameters using sequential EM ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"). Individuals are allowed to differ not only in their earnings levels and earnings mobility, but also in their propensity to enter non-employment or to work in the public sector, conditional on fixed characteristics such as labor market experience, education, and gender. These latent patterns give rise to distinct income and mobility classes within the data. Lifetime values of jobs are then constructed for each sector and analyzed comparatively across states, transition classes, earnings groups, and gender.

### 3.1 Structure

The data is structured as follows: For each individual i∈(1,…,N)i\in(1,...,N), we have a record of respective income flows, employment states, fixed characteristics, denoted by a vector 𝒙i=(𝒚i,𝑺i,𝒛iv,𝒛if)\boldsymbol{x}\_{i}=(\boldsymbol{y}\_{i},\boldsymbol{S}\_{i},\boldsymbol{z}\_{i}^{v},\boldsymbol{z}\_{i}^{f}) over a time period TiT\_{i}. Each boldface variable here represents a vector.

* •

  𝒚i=(yi​1,…,yi​Ti)\boldsymbol{y}\_{i}=(y\_{i1},...,y\_{iT\_{i}}) is the sequence of individual ii’s log income (real net annual wage) at each time period tt where t∈(1,2,,…,Ti)t\in(1,2,,...,T\_{i})
* •

  𝑺𝒊=(Si​1,…,Si​Ti)\boldsymbol{S\_{i}}=(S\_{i1},...,S\_{iT\_{i}}) short for state, records the sectoral state of the worker. The different states are defined as follows for a person ii in the tt​ht^{th} year:

  + –

    Si​t=0{S}\_{it}=0 : not employed.
  + –

    Si​t=1{S}\_{it}=1 : employed in a full-time private sector job.
  + –

    Si​t=2{S}\_{it}=2 : employed in a full-time public sector job.
  + –

    Si​t=3{S}\_{it}=3 : employed in a part-time private sector job.
  + –

    Si​t=4{S}\_{it}=4 : employed in a part-time public sector job.
* •

  𝒛iv=(zi​1v,…,zi​Tiv)\boldsymbol{z}^{v}\_{i}=(z^{v}\_{i1},...,z^{v}\_{iT\_{i}}) is the sequence of time-varying individual characteristics. In this analysis labor market experience over a decade (defined as the cumulative duration of employment of individual ii) and its square are considered. Note that conditional on the s​t​a​t​estate at time tt, zivz\_{i}^{v} is deterministic.
* •

  𝒛if\boldsymbol{z}^{f}\_{i} is the set of individual fixed characteristics. It includes highest academic qualification, labor market experience when first observed in the sample, and gender. 𝒛iv\boldsymbol{z}^{v}\_{i} is thus deterministic conditional on 𝒛if\boldsymbol{z}^{f}\_{i}.

In addition to observed individual heterogeneity captured by 𝒛iv\boldsymbol{z}^{v}\_{i} and 𝒛if\boldsymbol{z}^{f}\_{i}, there might exist certain unobserved individual characteristics which may influence wages or movement or selection into the various labor market states. Thus we should supplement the data vector 𝒙i\boldsymbol{x}\_{i} by appending a set 𝒌i\boldsymbol{k}\_{i} of such (time-invariant) unobserved characteristics.
The aim of the model is to simultaneously estimate transitions between the aforementioned labor market states and income trajectories within and between employment sectors. To this end, individual contributions to the c​o​m​p​l​e​t​ecomplete likelihood—i.e. the likelihood of (𝒙i,𝒌i)(\boldsymbol{x}\_{i},\boldsymbol{k}\_{i}), including unobserved variables is described as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒi​(𝒙i,𝒌i)=ℓi​(𝒚i|𝑺i,𝒛if,𝒌i)⋅ℓi​(𝑺i|𝒛if,𝒌i)⋅ℓi​(𝒌i|𝒛if)⋅ℓi​(𝒛if)\mathcal{L}\_{i}(\boldsymbol{x}\_{i},\boldsymbol{k}\_{i})=\ell\_{i}(\boldsymbol{y}\_{i}|\boldsymbol{S}\_{i},\boldsymbol{z}\_{i}^{f},\boldsymbol{k}\_{i})\cdot\ell\_{i}(\boldsymbol{S}\_{i}|\boldsymbol{z}\_{i}^{f},\boldsymbol{k}\_{i})\cdot\ell\_{i}(\boldsymbol{k}\_{i}|\boldsymbol{z}\_{i}^{f})\cdot\ell\_{i}(\boldsymbol{z}\_{i}^{f}) |  | (1) |

Through each individual decomposition in equation
([1](https://arxiv.org/html/2510.16626v1#S3.E1 "In 3.1 Structure ‣ 3 Model ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
, the aim is to capture the distribution of observed individual characteristics; the distribution of unobserved individual heterogeneity given observed characteristics; and the likelihood of individual earnings and labor market state trajectories given individual heterogeneity. Then, estimates are obtained from parameters by maximizing the sample log-likelihood

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∑i=1Nln⁡(∑kim=1Km∑kiy=1Kyℒi​(𝒙i,𝒌i))\ \sum\_{i=1}^{N}\ln\Bigg(\sum\_{k\_{i}^{m}=1}^{K^{m}}\sum\_{k\_{i}^{y}=1}^{K^{y}}\mathcal{L}\_{i}(\boldsymbol{x}\_{i},\boldsymbol{k}\_{i})\Bigg) |  | (2) |

The next sub-sections delve deeper into the individual components of the individual likelihood equation
([1](https://arxiv.org/html/2510.16626v1#S3.E1 "In 3.1 Structure ‣ 3 Model ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
 and elaborate on their implications and functional forms.

### 3.2 Unobserved heterogeneity

Starting from the third term of the likelihood function ℒi​(xi,ki)\mathcal{L}\_{i}(x\_{i},k\_{i}) given by equation
([1](https://arxiv.org/html/2510.16626v1#S3.E1 "In 3.1 Structure ‣ 3 Model ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
, two types of unobserved heterogeneity, ki=(kiy,kim)k\_{i}=(k\_{i}^{y},k\_{i}^{m}) is considered. This is motivated by the evidence presented in subsections [2.2](https://arxiv.org/html/2510.16626v1#S2.SS2 "2.2 Women and men move differently in the labor market ‣ 2 Stylized facts ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") and [2.3](https://arxiv.org/html/2510.16626v1#S2.SS3 "2.3 Differences in earnings are larger in the private sector, especially for educated workers ‣ 2 Stylized facts ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") that men and women move differently in the labor market and thus earn different wages.

* •

  kimk\_{i}^{m} : Transition class. This accounts for heterogeneity of individuals in terms of propensity to be in the different non-/employment states, SiS\_{i}. kimk\_{i}^{m} conditions the parameters related to employment and sectoral histories.
* •

  kiyk\_{i}^{y} : Income class. This accounts for heterogeneity in terms of income. kiyk\_{i}^{y} conditions the income parameters relating to individuals’ income process.

Both these heterogeneity classes are time-invariant random effects for an individual. The transition class, kimk\_{i}^{m} is conditional on the fixed individual characteristics and helps in modelling the selection of individuals into the various employment states, SiS\_{i}. kiyk\_{i}^{y} on the other hand, being time invariant as well, helps to increase the persistence of income ranks of an individual. In essence, we are using a finite mixture approach here to model unobserved heterogeneity of individuals, where each individual can belong to one of KmK^{m} transition classes and KyK^{y} income classes. The total number of possible classes is thus K=Km×Ky=12K=K^{m}\times K^{y}=12.

Details on estimation of unobserved heterogeneity, transition classes, and the number of classes chosen is presented in the appendix sections [A.3.1](https://arxiv.org/html/2510.16626v1#A1.SS3.SSS1 "A.3.1 Unobserved Heterogeneity ‣ A.3 Model ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") and [A.3.2](https://arxiv.org/html/2510.16626v1#A1.SS3.SSS2 "A.3.2 Transitions in labor market states and Transition classes: 𝐾^𝑚 ‣ A.3 Model ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France").

### 3.3 Income process and Income class: KyK^{y}

The first term of the individual likelihood equation
([1](https://arxiv.org/html/2510.16626v1#S3.E1 "In 3.1 Structure ‣ 3 Model ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
 models the likelihood of the individual’s income path over the years. Assume yi​ty\_{it}, the log-income of individual ii in year tt to be the realization of a first-order Markov process. The likelihood of an individual’s income trajectory can thus be expanded as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ​(y)=ℓ​(y1)⋅∏t=2Tℓ​(yt|yt−1)=ℓ​(y1)⋅∏t=2Tℓ​(yt,yt−1)ℓ​(yt−1)\ell(\textbf{y})=\ell(y\_{1})\cdot\prod\_{t=2}^{T}\ell(y\_{t}|y\_{t-1})\\ =\ell(y\_{1})\cdot\prod\_{t=2}^{T}\frac{\ell(y\_{t},y\_{t-1})}{\ell(y\_{t-1})} |  | (3) |

Now each of these yearly log-income streams, are assumed to be normal, and conditional on current labor market state and observed and unobserved heterogeneity.

yi​t|Si​t,zi​tv,zif,kiy∼𝒩​(μi​t,σi​t2)y\_{it}|S\_{it},z\_{it}^{v},z\_{i}^{f},k\_{i}^{y}\sim\mathcal{N}(\mu\_{it},\sigma^{2}\_{it})

with μi​t=μ​(Si​t,zi​tv,zif,kiy)\mu\_{it}=\mu(S\_{it},z\_{it}^{v},z\_{i}^{f},k\_{i}^{y}) and σi​t=σ​(Si​t,zi​tv,zif,kiy)\sigma\_{it}=\sigma(S\_{it},z\_{it}^{v},z\_{i}^{f},k\_{i}^{y})

We model the μi​t\mu\_{it} using an OLS regression of yi​ty\_{it} over the current labor market state and observed and unobserved heterogeneity.

|  |  |  |  |
| --- | --- | --- | --- |
|  | μ​(Si​t,zi​tv,zif,kiy)=(Si​tzi​tvzifkiySi​t∗kiy)′⋅μ\mu(S\_{it},z\_{it}^{v},z\_{i}^{f},k\_{i}^{y})=\begin{pmatrix}S\_{it}&z\_{it}^{v}&z\_{i}^{f}&k\_{i}^{y}&S\_{it}\*k\_{i}^{y}\end{pmatrix}^{\prime}\cdot\mu |  | (4) |

Here the ∗\* represents the interaction term of two variables.

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ​(Si​t,zi​tv,kiy)=exp⁡[(Si​tzi​tvkiySi​t∗kiy)′⋅σ]\sigma(S\_{it},z\_{it}^{v},k\_{i}^{y})=\sqrt{\exp\Bigg[\begin{pmatrix}S\_{it}&z\_{it}^{v}&k\_{i}^{y}&S\_{it}\*k\_{i}^{y}\end{pmatrix}^{\prime}\cdot\sigma\Bigg]} |  | (5) |

The functional form of σ​(⋅)\sigma(\cdot) constrains the standard deviation of the log-income yi​ty\_{it} to be positive. The effect of the fixed individual heterogeneity zifz\_{i}^{f} is subsumed through its link to kiyk\_{i}^{y}. Using yi​ty\_{it}, μ\mu and σ\sigma, the normalized log-income is constructed as yi​t~=yi​t−μi​tσi​t\tilde{y\_{it}}=\frac{y\_{it}-\mu\_{it}}{\sigma\_{it}}. Therefore, yi​t~∼𝒩​(0,1)\tilde{y\_{it}}\sim\mathcal{N}(0,1).

The pair (y~i​t,y~i,t−1)(\tilde{y}\_{it},\tilde{y}\_{i,t-1}) is a vector which follows a bivariate multinomial normal distribution. It has a covariance matrix τ¯i​t(2)\underline{\tau}\_{it}^{(2)} which can be expanded as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | τ¯i​t(2)=(1τi,t,t−1τi,t,t−11).\underline{\tau}\_{it}^{(2)}=\begin{pmatrix}1&\tau\_{i,t,t-1}\\ \tau\_{i,t,t-1}&1\end{pmatrix}. |  | (6) |

τ\tau is individual-specific and is allowed to vary with observed and unobserved heterogeneity and with employment s​t​a​t​estate at t​ and ​t−1t\text{ and }t-1. We therefore create a function, τ1​(⋅)\tau\_{1}(\cdot),

|  |  |  |  |
| --- | --- | --- | --- |
|  | τi,t,t−1=τ1​(Si​t,Si,t−1,zi​tv,zif,kiy,kim).\begin{split}\tau\_{i,t,t-1}=\tau\_{1}\big(S\_{it},S\_{i,t-1},z\_{it}^{v},z\_{i}^{f},k\_{i}^{y},k\_{i}^{m}\big).\end{split} |  | (7) |

The functional form of τ1​(⋅)\tau\_{1}(\cdot) is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | τ1​(Si​t,Si,t−1,zi​tv,kiy)=−1+2⋅Λ​[(Si​tSi,t−1zi​tvkiykimSi​t∗kiySi,t−1∗kiy)⋅ζ]\tau\_{1}(S\_{it},S\_{i,t-1},z\_{it}^{v},k\_{i}^{y})=-1+2\cdot\Lambda\Bigg[\begin{pmatrix}S\_{it}&S\_{i,t-1}&z\_{it}^{v}&k\_{i}^{y}&k\_{i}^{m}&S\_{it}\*k\_{i}^{y}&S\_{i,t-1}\*k\_{i}^{y}\end{pmatrix}\cdot\zeta\Bigg] |  | (8) |

Here Λ​(x)=(1+e−x)−1\Lambda(x)={(1+e^{-x})}^{-1}. The functional form of τ1​(⋅)\tau\_{1}(\cdot) includes a transformation in the form of −1+2⋅Λ​(⋅)-1+2\cdot\Lambda(\cdot). This constrains the correlation coefficient between normalized incomes at year t and t-1 to lie between [-1,1]. Likelihood of an individual’s income trajectory 𝐲𝐢\mathbf{y\_{i}} defined earlier in equation
([3](https://arxiv.org/html/2510.16626v1#S3.E3 "In 3.3 Income process and Income class: 𝐾^𝑦 ‣ 3 Model ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
 is:

|  |  |  |
| --- | --- | --- |
|  | ℓ​(y)=ℓ​(y1)⋅∏t=2Tℓ​(yt,yt−1)ℓ​(yt−1)\begin{split}\ell(\textbf{y})=\ell(y\_{1})\cdot\prod\_{t=2}^{T}\frac{\ell(y\_{t},y\_{t-1})}{\ell(y\_{t-1})}\\ \end{split} |  |

The numerator in this expression can be written as a joint density of a pair of normalized log-earnings, y~i​t=yi​t−μi​tσi​t\tilde{y}\_{it}=\frac{y\_{it}-\mu\_{it}}{\sigma\_{it}}

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ​(yt,yt−1)=1σt​σt−1⋅φ2​(y~i​t,y~i,t−1;τ¯i​t(2))\ell(y\_{t},y\_{t-1})=\dfrac{1}{\sigma\_{t}\sigma\_{t-1}}\cdot\varphi\_{2}\Big(\tilde{y}\_{it},\tilde{y}\_{i,t-1};\underline{\tau}\_{it}^{(2)}\Big) |  | (9) |

where φ2​(⋅;τ¯(2))\varphi\_{2}(\cdot;\underline{\tau}^{(2)}) is the bivariate normal pdf with mean 0 and covariance matrix τ¯(2)\underline{\tau}^{(2)}999Note that φ2​(⋅)\varphi\_{2}(\cdot) is defined as:

φn​(𝒀;Σ)=1(2​π)2​ΔΣ⋅e​x​p​(−12⋅(𝒀−𝝁)′​Σ−1​(𝒀−𝝁))\varphi\_{n}(\boldsymbol{Y};\Sigma)=\frac{\displaystyle 1}{\displaystyle\sqrt{(2\pi)^{2}\Delta\_{\Sigma}}}\cdot exp({-\frac{1}{2}\cdot(\boldsymbol{Y-\mu})^{\prime}\Sigma^{-1}(\boldsymbol{Y-\mu})})

(10)
. Substituting this expression to equation
([3](https://arxiv.org/html/2510.16626v1#S3.E3 "In 3.3 Income process and Income class: 𝐾^𝑦 ‣ 3 Model ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
 gives us:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓ​(y)=ℓ​(y1)⋅∏t=2Tℓ​(yt,yt−1)ℓ​(yt−1)=φ1​(y~1)σ1⋅(∏t=2Tφ2​(y~t,y~t−1;τt(2))φ1​(y~t−1)⋅∏t=2T1σt)=(∏t=1T1σt)⋅∏t=2Tφ2​(y~t,y~t−1;τt(2))∏t=2T−1φ1​(y~t)\begin{split}\ell(\textbf{y})=\ell(y\_{1})\cdot\prod\_{t=2}^{T}\frac{\ell(y\_{t},y\_{t-1})}{\ell(y\_{t-1})}\\ =\dfrac{\varphi\_{1}(\tilde{y}\_{1})}{\sigma\_{1}}\cdot\Bigg(\prod\_{t=2}^{T}\dfrac{\varphi\_{2}(\tilde{y}\_{t},\tilde{y}\_{t-1};\tau\_{t}^{(2)})}{\varphi\_{1}(\tilde{y}\_{t-1})}\cdot\prod\_{t=2}^{T}\dfrac{1}{\sigma\_{t}}\Bigg)\\ =\Bigg(\prod\_{t=1}^{T}\dfrac{1}{\sigma\_{t}}\Bigg)\cdot\frac{\displaystyle\prod\_{t=2}^{T}\varphi\_{2}(\tilde{y}\_{t},\tilde{y}\_{t-1};\tau\_{t}^{(2)})}{\displaystyle\prod\_{t=2}^{T-1}\varphi\_{1}(\tilde{y}\_{t})}\\ \end{split} |  | (11) |

With these specifications in place, normalized incomes are thus assumed to follow an AR(1) process:

|  |  |  |  |
| --- | --- | --- | --- |
|  | y~i​t=ρi​t⋅y~i,t−1+ϵi​t\tilde{y}\_{it}=\rho\_{it}\cdot\tilde{y}\_{i,t-1}+\epsilon\_{it} |  | (12) |

where the innovations ϵi​t\epsilon\_{it} are normal with mean 0 and serially uncorrelated.

### 3.4 Linking ρ\rho to τ\tau and σ2\sigma^{2}

Equation [12](https://arxiv.org/html/2510.16626v1#S3.E12 "In 3.3 Income process and Income class: 𝐾^𝑦 ‣ 3 Model ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") describes the AR(1) process for the normalized wage. We now resort to the standard relations between these parameters in a typical AR(1) process. We recall, in a first order autoregressive process, the autocovariance at lag 1,τ1\tau\_{1} is related to the σ\sigma and the autocorrelation coefficient ρ\rho as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | τ1=σ21−ρ2\tau\_{1}=\frac{\sigma^{2}}{1-\rho^{2}} |  | (13) |

Simplifying and solving for ρ\rho, we get

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ=−σ2+σ4+4​τ22​τ,\rho=\frac{-\sigma^{2}+\sqrt{\sigma^{4}+4\tau^{2}}}{2\tau}, |  | (14) |

Now that we have ρ\rho, we can recreate the income process based on the first wage and Equation [12](https://arxiv.org/html/2510.16626v1#S3.E12 "In 3.3 Income process and Income class: 𝐾^𝑦 ‣ 3 Model ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"). By substituting the equation for normalized log-wages into the AR(1) process, we can return to the original (unnormalized) process. Specifically, using y~i​t=yi​t−μi​tσi​t\tilde{y}\_{it}=\frac{y\_{it}-\mu\_{it}}{\sigma\_{it}}:

|  |  |  |  |
| --- | --- | --- | --- |
|  | yi​t=μi​t+σi​t⋅(ρi​t⋅yi,t−1−μi,t−1σi,t−1+ϵi​t).y\_{it}=\mu\_{it}+\sigma\_{it}\cdot\left(\rho\_{it}\cdot\frac{y\_{i,t-1}-\mu\_{i,t-1}}{\sigma\_{i,t-1}}+\epsilon\_{it}\right). |  | (15) |

This equation describes how log-wages at time tt depend on:

1. 1.

   The individual-specific mean μi​t\mu\_{it}, which reflects systematic factors such as experience, education, and sector,
2. 2.

   The deviation from the mean at the previous period, (yi,t−1−μi,t−1)(y\_{i,t-1}-\mu\_{i,t-1}), weighted by the persistence parameter ρ\rho,
3. 3.

   A stochastic noise term, σi​t⋅ϵi​t\sigma\_{it}\cdot\epsilon\_{it}, capturing unobserved factors.

This approach ensures that the model incorporates the underlying persistence of log-wages while accounting for the role of noise and covariate-driven variation.

## 4 Model Fit

### 4.1 Understanding the latent classes

The EM algorithm was run until convergence (distance of parameters <10−3<10^{-3}) in order to arrive at the final estimates of the κm\kappa^{m}, χ\chi, χ0\chi\_{0}, μ\mu, σ\sigma, ξ\xi, κy\kappa^{y} coefficients. These final estimates of the coefficients are reported in the appendix table
([A.9](https://arxiv.org/html/2510.16626v1#T9 "Table A.9 ‣ A.6 Estimated model parameters ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
 through
([A.13](https://arxiv.org/html/2510.16626v1#T13 "Table A.13 ‣ A.6 Estimated model parameters ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
.

The estimation procedure identifies distinct latent transition and income classes, capturing the heterogeneity in employment dynamics and wage trajectories across the public and private sectors. The classification reveals four transition classes (related to employment sector mobility) and three income classes (characterizing wage persistence and mobility), jointly shaping career outcomes. We first look at the mobility estimations for our panel data. The individuals in our panel are sorted into 4 transition classes. 42% individuals are sorted into the Transition class 0, around 4% in class 1, 47% in class 2 and 7% in class 3. Note that the order is meaningless. The transition classes have the distribution as in Table
(LABEL:tab:kmdist\_desc)
. Note that women are overrepresented in transition classes with higher public sector participation, as expected.

Table 5: Share of individuals by Sex, Education, Transition Class and Income Class

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Transition Class | Share of | Female share | Education | | |
| individuals | Low share | Med share | High share |
| 0 | 42% | 65% | 51% | 16% | 32% |
| 1 | 4% | 66% | 71% | 29% | 0% |
| 2 | 47% | 33% | 86% | 14% | 0% |
| 3 | 7% | 56% | 68% | 10% | 22% |
| Income Class | Share of | Female share | Education | | |
| individuals | Low share | Med share | High share |
| 0 | 8% | 40% | 60% | 13% | 26% |
| 1 | 32% | 57% | 72% | 17% | 11% |
| 2 | 60% | 47% | 69% | 15% | 16% |

Although the estimated latent transition classes differ markedly in their composition by sex, education, and age, the transition dynamics implied by the model are remarkably similar once these observed characteristics are conditioned on. In other words, the classes capture more the differences in who participates in different segments of the labor market rather than differences in how individuals move between employment states over time.

The patterns of sectoral persistence and transition—such as the high stability of full-time employment in both the public and private sectors, and the relatively frequent transitions from part-time to non-employment–are close across transition classes. However, there are differing propensities in the latent classes: specifically, those in transition class 0, km=0k^{m}=0, have a slightly higher propensity to go into public full-time roles, those in km=1k^{m}=1 to public part-time roles, those in km=2k^{m}=2 to private full-time roles and finally those in km=3k^{m}=3 to private part-time roles. This is evidenced by the multinomial logit parameters in table [A.9](https://arxiv.org/html/2510.16626v1#T9 "Table A.9 ‣ A.6 Estimated model parameters ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France").

Unobserved heterogeneity plays a fundamental role in explaining wage dynamics in our dataset. The latent income classification (kyk^{y}) uncovers distinct subpopulations characterized by different wage persistence and mobility regimes that go beyond observed demographics and labor market states. These income classes capture hidden variation in earnings trajectories that cannot be fully attributed to measured covariates like education, age, or sectoral affiliation.

The model’s goodness-of-fit notably improves with the introduction of these latent income classes, reflecting important wage heterogeneity within transition classes (kmk^{m}). For instance, the highest income class (ky=0k^{y}=0), comprising about 8% of individuals, is marked by stable high earnings and high education levels, while the largest income class (ky=2k^{y}=2, 60%) exhibits greater wage volatility and lower overall earnings.

![Refer to caption](x7.png)


Figure 3: Observed latent wage class distribution

Figure [3](https://arxiv.org/html/2510.16626v1#S4.F3 "Figure 3 ‣ 4.1 Understanding the latent classes ‣ 4 Model Fit ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") visually presents these distinct income distributions and highlights the stratification in wage stability and volatility across classes.

Taking a combined perspective on both income (kyk^{y}) and transition (kmk^{m}) latent classes, we observe layered unobserved heterogeneity: while the transition classes primarily capture compositional differences in employment states and demographics, the income classes reveal important heterogeneity in wage dynamics conditional on these employment patterns. This implies that unobserved heterogeneity in the model is multi-dimensional, affecting both employment transitions and wage mobility but through somewhat distinct latent structures.

This layered latent typology enriches our understanding of stratification and persistence mechanisms shaping the public-private wage gap and labor market careers. The detailed characterization of all twelve combined latent classes (ky×kmk^{y}\times k^{m}) is compiled in the appendix (Table [A.6](https://arxiv.org/html/2510.16626v1#T6 "Table A.6 ‣ A.5.1 Additional Tables and Figures for Model Fit and Unobserved Heterogeneity ‣ A.5 Model Fit ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France")), providing comprehensive insight into the interaction between employment stability and wage mobility across demographic groups.

While this paper employs a similar latent class framework to Dickson et al. [[2014](https://arxiv.org/html/2510.16626v1#bib.bib3)], the findings reveal less pronounced unobserved heterogeneity in mobility classes. This difference can be attributed to the broader and more heterogeneous sample used here, which includes both men and women across five employment states (adding part-time work in both sectors). The inclusion of gender as an observed covariate absorbs substantial variation in sectoral attachment and employment stability that, in a male-only sample, would appear as unobserved mobility heterogeneity. Moreover, the richer state space—incorporating part-time employment—introduces more fluid and overlapping transition patterns, making it difficult for latent mobility classes to capture sharp behavioral distinctions. In contrast, the income classes reveal meaningful unobserved heterogeneity in wage dynamics, consistent with prior findings, suggesting that while observed factors largely explain sectoral mobility, wage trajectories retain important latent structure even after controlling for demographics and employment states.

### 4.2 Prediction

As is customary, the statistical model’s goodness-of-fit and predictive power were first tested in-sample presented in subsection [4.2.1](https://arxiv.org/html/2510.16626v1#S4.SS2.SSS1 "4.2.1 In-sample ‣ 4.2 Prediction ‣ 4 Model Fit ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"). What has not been done in this particular literature thus far is the out-of-sample test with a data size three times as large as the training sample. This is presented in subsection [4.2.2](https://arxiv.org/html/2510.16626v1#S4.SS2.SSS2 "4.2.2 Out-of-sample ‣ 4.2 Prediction ‣ 4 Model Fit ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France").

#### 4.2.1 In-sample

Let individuals be assigned initial states for the first year that they appear in the panel, based on probabilities generated by equation
([20](https://arxiv.org/html/2510.16626v1#A1.E20 "In A.3.2 Transitions in labor market states and Transition classes: 𝐾^𝑚 ‣ A.3 Model ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
 conditioned on individual fixed characteristics. The method of probabilistic assignment is used so as to respect the probability distributions and not directly assign the state with the highest probability 101010Probabilistic assignment is chosen over deterministic assignment to prioritize accuracy. Results are exactly replicable as the set seed command was used. Moreover, the correlation between values generated by probabilistic assignment and deterministic assignment is, on average 0.7.. The probabilities from equation [19](https://arxiv.org/html/2510.16626v1#A1.E19 "In A.3.2 Transitions in labor market states and Transition classes: 𝐾^𝑚 ‣ A.3 Model ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") are used to assign the subsequent states, again employing probabilistic assignment. We can thus, test the goodness of fit and the predictive power of the model by checking year-on-year state transitions in the observed data and comparing it with the same transitions within the predicted data. We can observe quite similar patterns within these transitions as tabulated in Table [A.7](https://arxiv.org/html/2510.16626v1#T7 "Table A.7 ‣ A.5.1 Additional Tables and Figures for Model Fit and Unobserved Heterogeneity ‣ A.5 Model Fit ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") compared with the earlier descriptive table [2](https://arxiv.org/html/2510.16626v1#T2 "Table 2 ‣ 2.2 Women and men move differently in the labor market ‣ 2 Stylized facts ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"). The predictive strength is corroborated by the fact that the maximum distance between the observed and predicted transition probability matrices is 0.01 on aggregate.

Using the income process parameters, the log (real net annual) wages can be predicted. Once the simulation is done, we compare the simulated incomes to the observed incomes by comparing the observed and predicted wage densities as in figure [4](https://arxiv.org/html/2510.16626v1#S4.F4 "Figure 4 ‣ 4.2.1 In-sample ‣ 4.2 Prediction ‣ 4 Model Fit ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"). The predicted latent class composition is also tested: table LABEL:tab:kmdist\_desc is almost exactly replicated. Moreover, the income/wage class composition predicted as in figure [A.3](https://arxiv.org/html/2510.16626v1#A1.F3 "Figure A.3 ‣ A.5.1 Additional Tables and Figures for Model Fit and Unobserved Heterogeneity ‣ A.5 Model Fit ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") is very close to the observed figure [3](https://arxiv.org/html/2510.16626v1#S4.F3 "Figure 3 ‣ 4.1 Understanding the latent classes ‣ 4 Model Fit ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"). A word of caution here, the model slightly overpredicts full-time wages and slightly underpredicts part-time wages as shown in figure [A.4](https://arxiv.org/html/2510.16626v1#A1.F4 "Figure A.4 ‣ A.5.1 Additional Tables and Figures for Model Fit and Unobserved Heterogeneity ‣ A.5 Model Fit ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"). However, figure [4](https://arxiv.org/html/2510.16626v1#S4.F4 "Figure 4 ‣ 4.2.1 In-sample ‣ 4.2 Prediction ‣ 4 Model Fit ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") (below) and figure [A.3](https://arxiv.org/html/2510.16626v1#A1.F3 "Figure A.3 ‣ A.5.1 Additional Tables and Figures for Model Fit and Unobserved Heterogeneity ‣ A.5 Model Fit ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") (in the appendix) provide strong evidence for the predictive power of this model. The actual observed and predicted income distributions are a near exact match, including the small kink towards the left of the observed income distribution.

![Refer to caption](x8.png)


Figure 4: Observed and predicted wage densities

#### 4.2.2 Out-of-sample

To test the model’s robustness beyond the estimation sample, I applied the trained coefficients to a larger out-of-sample panel comprising 829,232 individuals and 6,194,037 observations (thrice the size of the in-sample panel used). In this prediction process, I retained only each individual’s first observed employment spell and used the estimated coefficients to simulate their subsequent (non-)employment trajectories and associated wages. This approach allows for assessing how well the model generalizes to a broader population while accounting for both observed and unobserved heterogeneity in labor market outcomes.

All the state transition and wage prediction results presented in the in-sample section [4.2.1](https://arxiv.org/html/2510.16626v1#S4.SS2.SSS1 "4.2.1 In-sample ‣ 4.2 Prediction ‣ 4 Model Fit ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") were also replicated for this larger panel and are included in the appendix [A.5.2](https://arxiv.org/html/2510.16626v1#A1.SS5.SSS2 "A.5.2 Prediction: Out-of-sample predictions of wages and transitions ‣ A.5 Model Fit ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"). The consistency of the predicted trends across samples reinforces the model’s validity in capturing employment mobility, wages, and sectoral differences over time.

## 5 Results: Public and Gender Premia in Lifetime Earnings

### Constructing Lifetime Earnings

Once the maximization problem is resolved and we have stable parameters of the income and job mobility parameters, simulations of employment and income trajectories for the individuals in the sample are carried out until retirement age. Assuming that, upon retiring (which is assumed to happen at age 60 denoted as TRT\_{R}), a given individual enjoys a residual value of VRV\_{R}, then the lifetime value as of experience level tt of an individual’s simulated future income trajectory ys≥ty\_{s\geq t} is written as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Vt​(ys≥t)=∑s=tTRβs−t⋅exp⁡(ys)+βTR−t⋅VRV\_{t}(y\_{s\geq t})=\sum^{T\_{R}}\_{s=t}\beta^{s-t}\cdot\exp(y\_{s})+\beta^{T\_{R}-t}\cdot V\_{R} |  | (16) |

where β∈(0,1)\beta\in(0,1) is the discount factor and exp⁡(yt)\exp(y\_{t}) is the projected real net annual wage that the individual earns from (log) income yty\_{t}. We could also interpret e​x​p​(yt)exp(y\_{t}) as the risk-neutral utility from earnings.
The log of the above VtV\_{t} - the log of the discounted sum of lifetime earnings (hereon referred as "lifetime earnings") under different pathways are calculated and compared sectorally. The discount factor β=0.95\beta=0.95 per annum, as is standard in the literature. The value of retirement is defined as VR=1−β221−β×R​R×eyTR−1V\_{R}=\frac{1-\beta^{22}}{1-\beta}\times RR\times e^{y\_{T\_{R}-1}} in both the scenarios. Assuming that after retirement, individuals receive a constant flow of income equal to RR times their last income in activity and discount this flow over a period of 22 years (time between average retirement age and average life expectancy which is 82 years, in France). The particular values of β=0.95\beta=0.95 and R​R=0.4RR=0.4 that were taken obviously condition the results described. A lower β\beta would clearly make lifetime values close to current income flows and would magnify the observed public-private pay gap (the private sector earnings being far more dispersed). An increase in R​RRR on the other hand, would only magnify the impact of the income gap at the time of retirement. For the main results presented in section [5](https://arxiv.org/html/2510.16626v1#S5 "5 Results: Public and Gender Premia in Lifetime Earnings ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"), the R​RRR used is 0.400.40 using the precedent set by Dickson et al. [[2014](https://arxiv.org/html/2510.16626v1#bib.bib3)]. For robustness, all the specifications to calculate the discounted sum of lifetime earnings were also estimated with an R​R=0.7RR=0.7 and separate rates for the public and private sectors: R​Rp​u​b=0.75RR\_{pub}=0.75 and R​Rp​v​t=0.71RR\_{pvt}=0.71. The results are largely consistent.

An implicit assumption in computing lifetime values, is that the prevailing economic environment is stationary and individuals anticipate aging and experiencing changes in their wage and job mobility given their current state and income level, but not the inherent model paramaters to be changing over their working life. Given the stability of the share of public sector employment and of the non-employment rate in France over the sample period, the sample time-period can be considered as an average state of the business cycle. The public premium is defined as the difference in log-lifetime values (referred to as "lifetime earnings" hereon) between the public and private sector. The ’whole sample, with selection’ graph relates to predicted ’raw’ differences, i.e. it plots the difference between quantiles of lifetime earnings among individuals effectively observed to hold public jobs in the initial period, and corresponding quantiles of lifetime earnings among workers observed to hold private jobs in the initial period. The whole sample graphs relate to predicted differences in lifetime earnings across sectors for all individuals in the sample, i.e. it compares income and lifetime values that each individual could potentially earn in either sector.

In this section, I present a series of insights that stem from comparing lifetime earnings111111Recall that ”lifetime earnings” refers to the log of the discounted sum of future earnings as defined in equation [16](https://arxiv.org/html/2510.16626v1#S5.E16 "In Constructing Lifetime Earnings ‣ 5 Results: Public and Gender Premia in Lifetime Earnings ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"). across sectors, by gender and education, with and without selection to offer a more holistic understanding of what we perceive as the public premium, first focusing on if there is one at all. Two broad sets of counterfactuals are considered: one, is to compare the "job-for-life" lifetime earnings wherein individuals (on aggregate, and by gender, by education, etc.) are assumed to hold either a public or private sector job in every period from the time they are first observed until age 60. Two, is to compare lifetime earnings "with mobility", meaning, people can transition into any of the 5 states (non-employment, full-time employment in private sector, in public sector, part-time employment in private and public sectors) until retirement based on the transition probabilities as per their observed (gender, education, experience) and unobserved factors (latent types). The first set of counterfactuals sheds light on what the earnings gap amount to over a lifetime ceteris paribus assuming that people are employed in every period, full-time in either sector. The second set ("with mobility") gives a more realistic and accurate picture as it estimates lifetime earnings "with mobility", taking transition patterns into account.

### 5.1 The Lifetime Public Sector Premium

A significant public sector premium exists in France, particularly for women, low-educated workers, and individuals over 45. This premium persists across most of the earnings distribution even after accounting for self-selection into sectors. An oft-encountered question here is if the public premium is just a result of selection. The short answer is no, as many studies confirm. But the selection effect indeed estimates higher and larger premia or penalties as the case may be as deconstructed herein. Figure [A.8](https://arxiv.org/html/2510.16626v1#A1.F8 "Figure A.8 ‣ A.7 Results: Figures ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") compares the counterfactual lifetime earnings from the "job-for-life" case with the counterfactual lifetime earnings wherein individuals, conditional on selection into either sector, transition freely across employment states. Of course, these transitions are informed by the patterns that are already captured from the model conditioned on observables and unobservables. Unsurprisingly, lifetime earnings are higher if individuals hold a full-time job in either sector in every period, but we know that is rare for everyone to experience. The losses in lifetime earnings is higher in private sector due to higher transitions into non-employment and worse part-time pay compared to the public sector.

Job-for-life case: potential lifetime earnings differences if everyone could hold a full-time job in every period.  With selection there is a positive public premium until the 46th percentile on aggregate. But even without selection, there is one until the 30th percentile. To understand how much of the premium we see is just a matter of selection, we must first quantify if there is a public premium "with selection" and then, if there is one "without" and for whom, if at all.

* •

  "with selection": What happens if those observed to be in public sector full-time jobs were forced to switch to the private sector instead?
    
  Main result: Is a public premium observed? Yes. For whom? Women (until the 69th percentile), Low educated workers (until the 60th percentile) and older workers (over 45) (until the 76th percentile).
* •

  "without selection": What happens if everyone in the sample is employed full-time in the public sector vs. the private sector?
    
  Main result: Is a public premium observed? Yes. For whom? Women (until the 38th percentile) Low educated workers (until the 38th percentile) and older workers (over 45) (until the 49th percentile).

Figure [A.8](https://arxiv.org/html/2510.16626v1#A1.F8 "Figure A.8 ‣ A.7 Results: Figures ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") illustrates the public premium in lifetime earnings for job-for-life counterfactuals, both with and without selection. The graph demonstrates that a public premium persists even when selection is eliminated, though to a lesser extent and for a smaller portion of the earnings distribution. With selection, the public premium extends up to the 46th percentile of the aggregate earnings distribution, while without selection, it reaches the 30th percentile. For women, the premium without selection is observed up to the 38th percentile, compared to the 69th percentile with selection. Similarly, for low-educated workers, the premium without selection persists up to the 38th percentile (versus 60th with selection), and for older workers over 45, it extends to the 49th percentile (compared to 76th with selection).

These findings underscore that while selection plays a significant role in amplifying the observed public premium, it is not the sole factor. The persistence of the premium even without selection indicates structural differences in compensation between the public and private sectors, particularly for certain demographic groups and at lower earnings and education levels. This analysis reinforces the conclusion that the public premium is not merely a result of selection, but reflects underlying differences in sectoral compensation structures. One might be tempted looking at figure [A.8](https://arxiv.org/html/2510.16626v1#A1.F8 "Figure A.8 ‣ A.7 Results: Figures ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") to compare the bars across categories, for example, comparing the premia for men vs. for women to see potentially if women have a higher public premium than men, but that would be misleading. The bars in figure [A.8](https://arxiv.org/html/2510.16626v1#A1.F8 "Figure A.8 ‣ A.7 Results: Figures ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") correspond to counterfactual earnings within that category (the percentage difference of lifetime earnings of low educated women first observed to be in the public sector from the lifetime earnings of low educated women if forced to be in the public sector give us the "with selection" red bar). To answer the question about gender premia by sector, we must compare the lifetime earnings of men and women (section [5.2](https://arxiv.org/html/2510.16626v1#S5.SS2 "5.2 Men benefit from a gender premium in both sectors ‣ 5 Results: Public and Gender Premia in Lifetime Earnings ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France")).

With mobility: true lifetime earnings differences show that losses in lifetime earnings higher in private sector. The estimated loss in earnings, calculated as the difference in (log) lifetime earnings of the job-for-life estimates and those with mobility, reveals that individuals initially observed in the private sector full-time experience greater income erosion due to higher transitions into non-employment and weaker part-time wage prospects. Converting these log differences into percentage terms, the lifetime earnings loss ranges from approximately 82% for the lowest quantiles to 5% for the highest quantiles in the private sector, whereas losses in the public sector are consistently lower (nearly half, throughout), ranging from 63% to 2%. This highlights the structural disadvantages faced by private-sector workers in earnings stability, emphasizing the role of sectoral labor mobility in shaping long-term economic outcomes. Of course, this effect is not gender-neutral either and the gaps are larger for women.

![Refer to caption](Graphs/loss_with_mobility_by_sector.png)


Figure 5: Loss in lifetime earnings with selection
  
Lifetime earnings percentage difference of job-for-life case and mobility case (the latter takes into account the probability of transitioning to non-employment or part-time work).

### 5.2 Men benefit from a gender premium in both sectors

Whether considering the job-for-life case in counterfactual lifetime earnings or the case with mobility, the takeaway remains that men benefit from a gender premium in both sectors. This comparison can be made in two ways: given selection into working full-time in either sector, the lifetime earnings quantiles of men and women can be compared sectorally. Alternatively, their lifetime earnings with mobility can be compared, again conditional on selection. Figure [6](https://arxiv.org/html/2510.16626v1#S5.F6 "Figure 6 ‣ 5.2 Men benefit from a gender premium in both sectors ‣ 5 Results: Public and Gender Premia in Lifetime Earnings ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") graphically depicts both these cases. As expected, the case that takes mobility into account (lines in the figure) produces higher gender gaps relative to the job for life case (area in the figure), particularly in the private sector. The public sector gender premium is almost always lower compared to private. A deeper dive into these differences by gender and by education categories reveals that on average, higher education lowers this gender premium that men benefit from in both sectors, even though glass ceilings exist in both sectors.

![Refer to caption](Graphs/gender_premium.png)


Figure 6: Gender premium in lifetime earnings

A particularly novel insight emerges when analyzing the distribution of lifetime earnings quantiles between men and women in each sector. The findings show that the male gender premium is present across the entire distribution but is more pronounced at higher earnings quantiles, especially in the private sector. This indicates that as earnings increase, men benefit from larger relative advantages, whereas women’s wages remain comparatively compressed, particularly in the public sector. Although much of the literature on gender pay gaps focuses on penalties faced by women, this study provides new quantitative evidence on the persistence of male wage advantages across the earnings distribution. Even in a labor market where public employment offers greater stability and wage regulation, men continue to systematically earn more than women at respective lifetime earnings quantiles, reinforcing cumulative gender inequalities over the career cycle.

### 5.3 Returns to education are lower in the public sector…

* •

  …for men and for women
  Figure [7](https://arxiv.org/html/2510.16626v1#S5.F7 "Figure 7 ‣ 5.3 Returns to education are lower in the public sector… ‣ 5 Results: Public and Gender Premia in Lifetime Earnings ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") illustrates that returns to education are consistently lower in the public sector compared to the private sector, for both men and women, across all lifetime earnings quantiles conditional on selection. The negative gap in lifetime earnings differences between public and private sector workers increases with education level, with highly educated workers experiencing the largest lifetime earnings penalty in the public sector.

  + –

    Among low-educated workers, differences between public and private sector earnings remain moderate, with some evidence of a public sector premium at the lowest quantiles. This suggests that for lower-income workers, public sector employment still offers some earnings security benefits, particularly in early career stages.
  + –

    However, for medium-educated workers, and even more so for highly educated workers, the public sector disadvantage becomes increasingly pronounced across the distribution, with lifetime earnings penalties widening at the upper quantiles. This suggests limited wage progression for highly skilled individuals in public sector jobs compared to their private sector counterparts.
  + –

    The penalty for highly educated workers is particularly severe for men, reinforcing the idea that private sector careers provide greater returns to education through steeper earnings trajectories over a lifetime.

  These findings confirm that while public employment provides stability, it does so at the cost of significantly lower lifetime earnings, especially for those with higher educational attainment.
* •

  …but job stability and transitions to public part-time reduces these penalties, particularly for women
  Despite the lower returns to education in the public sector, women, particularly those in the lower earnings quantiles, experience significant lifetime earnings advantages in the public sector when accounting for career stability and part-time transitions.

  + –

    The "With Mobility" panels in Figure 9 show that women, particularly low-educated women, benefit significantly from public sector job stability. The public sector mitigates earnings volatility, allowing for a smoother and more predictable lifetime earnings trajectory.
  + –

    The gap in lifetime earnings between public and private employment narrows significantly for women once sectoral transitions are considered, suggesting that career interruptions and part-time work are better accommodated in the public sector. This is particularly relevant for women with medium and low education levels, who benefit from higher wage stability when transitioning to public part-time work.

![Refer to caption](Graphs/lifetime_returns_to_educ.png)


Figure 7: Percentage difference of lifetime earnings in the public and private sectors by education levels and sex

These findings highlight a key gendered dynamic: while the private sector provides higher returns to education, the public sector acts as a critical stabilizing force for women, particularly in lower and middle-income categories. Public sector employment appears to buffer the income shocks associated with career breaks and transitions to part-time work, making it a more viable long-term option for many women, despite lower formal returns to education.

## 6 Discussion

The findings of this study demonstrate that the model successfully captures observed income trajectories and sectoral mobility patterns, providing a robust framework for analyzing lifetime earnings differentials between public and private sector workers. Notably, the model replicates the substantial earnings dispersion between men and women, particularly in the private sector, where wage trajectories exhibit greater volatility and gender disparities are more pronounced. However, while the model effectively accounts for sectoral differences in wage dynamics and transitions, institutional factors beyond direct wage earnings—such as pension schemes—remain an important avenue for future research. The French public and private sector pension systems differ significantly, with public sector workers typically benefiting from more stable retirement incomes. While these differences are not explicitly captured in this dataset, policy changes in pension structures could have significant implications for lifetime earnings differentials across sectors. Future research could extend this analysis by incorporating expected retirement benefits and pension wealth accumulation to provide a more comprehensive measure of lifetime earnings.

Another promising avenue for future work lies in the integration of fertility and household employment decisions into the modeling framework. Labor market outcomes are often shaped by household-level choices, particularly for women, whose career trajectories are more likely to be influenced by caregiving responsibilities. A dynamic approach that accounts for joint household decision-making and the impact of parental leave policies could offer deeper insights into the gendered effects of public versus private sector employment.

Finally, the findings suggest broader implications beyond the French labor market. The gendered lifetime public premium observed in this study is likely to be even more pronounced in developing economies, where public sector employment often provides one of the few stable career pathways. However, the extent of this effect will depend on institutional labor protections, the degree of informality in private sector employment, and access to social security systems. Future comparative research could test this hypothesis by analyzing cross-country differences in public-private earnings trajectories and gender disparities, particularly in economies where public employment is a critical employer for educated women.

By expanding on these dimensions—pension structures, household decision-making, and cross-country comparisons—future research can further refine our understanding of how sectoral employment choices shape lifetime earnings and economic inequalities across gender and educational backgrounds.

## 7 Conclusion

This study reveals how France’s labor market institutions—centralized wage bargaining, strong job protections, and regulated part-time work—shape lifetime earnings disparities between public and private sectors. By modeling unobserved heterogeneity and career transitions, I reconcile conflicting prior findings: while hourly wage analyses suggest penalties for educated workers, lifetime earnings reveal a public premium for women and low-skilled employees, driven by stability and part-time compensation. Yet this premium comes at a cost. Highly educated workers trade a part of their lifetime earnings in the public sector, reflecting rigid wage progression that stifles returns to education.

These results carry implications beyond France. As a prototype of coordinated market economies, France’s experience highlights the dual role of public sectors: mitigating gender inequality through stability while imposing ceilings on mobility. The results confirm the existence of a public premium in lifetime earnings, particularly for women, low-educated workers, and older employees. Even when accounting for selection effects, the public sector offers significant advantages to these groups in terms of income stability and reduced volatility. Policymakers in similar contexts (e.g., Scandinavia, Southern Europe) must weigh privatization’s risks—eroding gender equity gains—against the need to reform rigid wage structures. For developing economies, where public sectors often dominate formal employment, the findings underscore the potential of public jobs to reduce inequality.

Future research should extend this framework to incorporate pension benefits and household dynamics, deepening our understanding of how institutions shape lifetime disparities. By bridging the gaps between literature on gender, education, and sectoral choice, this study offers a blueprint for analyzing equity-efficiency trade-offs in labor markets globally.

## References

* Bargain and Melly [2008]

  Olivier Bargain and Blaise Melly.
  Public sector pay gap in france: new evidence using panel data.
  Technical report, IZA Discussion Papers, 2008.
* Beffy and Kamionka [2010]

  Magali Beffy and Thierry Kamionka.
  Public-private wage gaps: Is civil-servant human capital sector-specific?
  Working Paper 2010-55, CREST, 2010.
* Dickson et al. [2014]

  Matt Dickson, Fabien Postel-Vinay, and Hélène Turon.
  The lifetime earnings premium in the public sector: The view from europe.
  *Labour Economics*, 29:179–190, 2014.
  doi: 10.1016/j.labeco.2014.07.003.
* Heckman and Singer [1984]

  James J. Heckman and Burton Singer.
  A method for minimizing the impact of distributional assumptions in econometric models for duration data.
  *Econometrica*, 52(2):271–320, 1984.
  doi: 10.2307/1911491.
* Fougère and Pouget [2003]

  Denis Fougère and Julien Pouget.
  Who wants to be a ‘fonctionnaire’? the effects of individual wage differentials and unemployment probabilities on the queues for public sector jobs.
  Technical report, Mimeo, 2003.
* Garibaldi et al. [2021]

  Pietro Garibaldi, Pedro Gomes, and Thepthida Sopraseuth.
  Public employment redux.
  *Journal of Government and Economics*, 1:100003, 2021.
  ISSN 2667-3193.
  doi: https://doi.org/10.1016/j.jge.2021.100003.
  URL <https://www.sciencedirect.com/science/article/pii/S2667319321000033>.
* Gomes and Kuehn [2025]

  Pedro Gomes and Zoë Kuehn.
  You’re the one that i want! understanding the over-representation of women in the public sector.
  *American Economic Journal: Macroeconomics*, 2025.
* Garbinti et al. [2023]

  Bertrand Garbinti, Jonathan Goupille-Lebret, and Thomas Piketty.
  Gender inequalities in lifetime earnings: Evidence from france.
  *American Economic Journal: Applied Economics*, 15(1):1–35, 2023.
  doi: 10.1257/app.20220265.
* Guvenen et al. [2021]

  Fatih Guvenen, Fatih Karahan, Serdar Ozkan, and Jae Song.
  What do data on millions of u.s. workers reveal about life-cycle earnings risk?
  *Econometrica*, 89(5):2303–2339, 2021.
  doi: 10.3982/ECTA14884.
* Bargain et al. [2018]

  Olivier Bargain, Audrey Etienne, and Blaise Melly.
  Public sector wage gaps over the long-run: Evidence from panel administrative data.
  Discussion Paper 11924, IZA, 2018.
* Blau and Kahn [2017]

  Francine D. Blau and Lawrence M. Kahn.
  The gender wage gap: Extent, trends, and explanations.
  *Journal of Economic Literature*, 55(3):789–865, 2017.
  doi: 10.1257/jel.20160995.
* Goldin [2014]

  Claudia Goldin.
  A grand gender convergence: Its last chapter.
  *American Economic Review*, 104(4):1091–1119, 2014.
  doi: 10.1257/aer.104.4.1091.
* Petersen and Morgan [1995]

  Trond Petersen and Laurie A Morgan.
  Separate and unequal: Occupation-establishment sex segregation and the gender wage gap.
  *American Journal of Sociology*, 101(2):329–365, 1995.
* Bertrand et al. [2010]

  Marianne Bertrand, Claudia Goldin, and Lawrence F. Katz.
  Dynamics of the gender gap for young professionals in the financial and corporate sectors.
  *American Economic Journal: Applied Economics*, 2(3):228–255, July 2010.
  doi: None.
  URL <https://ideas.repec.org/a/aea/aejapp/v2y2010i3p228-55.html>.
* Ponthieux and Meurs [2015]

  Sophie Ponthieux and Dominique Meurs.
  Chapter 12 - gender inequality.
  In Anthony B. Atkinson and François Bourguignon, editors, *Handbook of Income Distribution*, volume 2, pages 981–1146. Elsevier, 2015.
  doi: 10.1016/B978-0-444-59428-0.00013-8.
* Postel-Vinay and Turon [2007]

  Fabien Postel-Vinay and Hélène Turon.
  The public pay gap in britain: Small differences that (don’t?) matter.
  *Economic Journal*, 117(523):F422–F442, 2007.
  doi: 10.1111/j.1468-0297.2007.02067.x.
* Bonhomme and Robin [2006]

  Stéphane Bonhomme and Jean-Marc Robin.
  Modeling individual earnings trajectories using copulas: France, 1990-2002.
  In Henning Bunzel, Bent J. Christensen, George R. Neumann, and Jean-Marc Robin, editors, *Structural Models of Wage and Employment Dynamics*, volume 275 of *Contributions to Economic Analysis*, pages 441–479. Elsevier, 2006.

## Appendix A Appendix

### A.1 Panel Construction

* •

  Keep observations of people aged 18-60 and atleast 3 observed spells (including non-employment).
* •

  Keep employment spells that are at least 6 months (180 days) in a year. Else, code as non-employment. Recall in DADS this employment durations include paid days/time off.
* •

  Non-employment is imputed for the two following cases:

  1. 1.

     if someone has missing years in between employment spells.
  2. 2.

     if someone who would be younger than 60 in 2019 vanishes from the panel.

  Every year from 2012-2019, about half of the non-employment spells have some non-employment compensation (chomage indemnisee).
* •

  In constructing a panel that has one spell per individual per year, the highest paying spell was kept (note only employment spells of atleast 6 months are kept).
* •

  Winsorize log net real annual earnings (variable s\_net) by state and year: cut and replace top and bottom 1%.
* •

  Note: Full-time hours in DADS is 1820 hours annually (this figure translates to a 35-hour workweek). This is because in DADS paid time off is also included in employment durations and in hours; so, 35-hour workweeks over the 52 weeks in a year gives us 35∗52=182035\*52=1820 hours annually.

Table A.1: Classification of French Degrees and U.S. Equivalents

| Category | Degree | U.S. Equivalent | Sample Classification |
| --- | --- | --- | --- |
| 1 | Aucun Diplôme déclaré | No Degree declared |  |
| 2 | CEP, DFEO | Elementary or Middle School |  |
| 3 | BEPC, BE, BEPS | High School |  |
| 4 | CAP, BEP, EFAA, BAA, BPA, FPA 1er | Vocational Technical School (Basic) |  |
| 5 | Baccalauréats technique et professionnel, brevet professionnel, autres brevets (BEA, BEC, BEH, BEI, BES, BATA), baccalauréat général, brevet supérieur, CFES | High school diploma (General or Technical/Vocational) | Low |
| 6 | Santé, BTS, DUT, DEST, DEUL, DEUS, DEUG | Associate’s degree or equivalent vocational degree | Medium |
| 7 | 2ème cycle, 3ème cycle, Grande école, CAPES, CAPET | Graduate School and Other Post-Secondary Education | High |

### A.2 Descriptives

#### Public Share of Employment

We observe that the public share of total employment in the sample remains fairly stable with an overall gradual increase of approximately 1.4% rising from a little under 23% close to 24.6% over the 8-year period. The slight but stable increase in the public share of employment is in-line with official INSEE statistics and corroborated in this sample panel.

#### A.2.1 Additional demographics in the Public and Private Sectors

Figure A.1: Share of women in the Public and Private Sectors over 2012-19

![Refer to caption](Graphs/sex_ratio_years.png)

The share of employment in both sectors is stable across the years observed. The public sector, including part-time and full-time work averages at 24.3%, with small deviations. Since this article focuses on the intersection with gender, the sex ratio in both sectors, by full-time status is of key importance. Women hold 60% of the full-time public sector jobs in contrast to the 39% in the private sector. Interestingly, the part-time work landscape is very different as most of these jobs are done by women. Over the years, the female share of part-time jobs rises in both sectors .

The stability of the sex ratio (of females to males) in the public and private sectors irrespective of part-time full-time worker status is captured by Figure [A.1](https://arxiv.org/html/2510.16626v1#A1.F1 "Figure A.1 ‣ A.2.1 Additional demographics in the Public and Private Sectors ‣ A.2 Descriptives ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") generated from the sample. In France, the sex ratio is roughly 65:35 in the public sector and 45:55 in private. Curiously, women’s earnings in the public sector is more compressed than that of men and also peaks later for the mean and above-mean income earners. The picture in the private sector by sex is even more grim. The dispersion of women’s earnings far exceeds that of men. The lowest decile earners across sex experience a significant fall in earnings towards retirement. However, the fall not only starts relatively earlier in women’s trajectories, but is far steeper across income percentiles. The below table depicts which sector, gender, and age group all the individuals observed in the panel (using their first spell) belong to:

Table A.2: Distribution of Education Levels by Sector, Sex and Age Groups at first observed spell

| Sex | Education | Public Sector | | | Private Sector | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Under 30 | 31-45 | Over 45 | Under 30 | 31-45 | Over 45 |
| Females | Low | 15 | 36 | 49 | 23 | 37 | 40 |
| Medium | 19 | 48 | 34 | 27 | 51 | 22 |
| High | 17 | 58 | 26 | 31 | 52 | 17 |
| Males | Low | 15 | 38 | 46 | 26 | 39 | 35 |
| Medium | 15 | 48 | 37 | 26 | 51 | 23 |
| High | 12 | 53 | 35 | 27 | 50 | 23 |

![Refer to caption](Graphs/wage_distribution_by_sec_sex.png)


Figure A.2:

#### Income and non-employment Statistics

The non-employment or inactivity remained mostly stable during this period at about 30%. Since it is imputed from the dataset it underestimates the rate for the first two years but catches up thereafter. Figure [A.2](https://arxiv.org/html/2510.16626v1#A1.F2 "Figure A.2 ‣ A.2.1 Additional demographics in the Public and Private Sectors ‣ A.2 Descriptives ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France") shows the income distribution of men and women in the public and private sectors over the whole sample. Recall that this includes part-time workers. There are many noteworthy points in this distribution : firstly, the dominance of males in the private sector and of females in the public sector is evident. Secondly, as expected, the spread of income is more dispersed in the private sector while it is relatively more compressed in the public sector. Thirdly, the private sector distribution of income of males to the right of the mean dominates that of women; implying that a higher number of men earn more than the average than do women: notice the blue bars to the right of the mean in the figure. This phenomenon is reversed in the public sector distributions where more women earn the mean and above mean incomes. But, since the public sector is relatively smaller than the private, the public distributions are much shorter than their private counterparts. This income distribution provides initial evidence for the average earnings of females being lower than for men in the private sector.

Table A.3: OLS regressions on real net wages - alternative specification

|  |  |  |
| --- | --- | --- |
| VARIABLES | Net annual | Net hourly |
| Pub FT | 0.100\*\*\* | -0.006 |
|  | (0.005) | (0.004) |
| Pvt PT | -0.636\*\*\* | -0.118\*\*\* |
|  | (0.018) | (0.010) |
| Pub PT | -0.443\*\*\* | -0.097\*\*\* |
|  | (0.009) | (0.005) |
| Female | -0.238\*\*\* | -0.171\*\*\* |
|  | (0.011) | (0.008) |
| Pub FT#1.female | 0.117\*\*\* | 0.059\*\*\* |
|  | (0.011) | (0.008) |
| Pvt PT#1.female | 0.117\*\*\* | 0.071\*\*\* |
|  | (0.028) | (0.016) |
| Pub PT#1.female | 0.337\*\*\* | 0.121\*\*\* |
|  | (0.013) | (0.009) |
| Experience (over a decade) | 0.374\*\*\* | 0.275\*\*\* |
|  | (0.002) | (0.001) |
| Experience over a decade squared | -0.065\*\*\* | -0.042\*\*\* |
|  | (0.000) | (0.000) |
| Medium educ | 0.288\*\*\* | 0.264\*\*\* |
|  | (0.001) | (0.001) |
| High educ | 0.537\*\*\* | 0.529\*\*\* |
|  | (0.001) | (0.001) |
| Constant | 9.498\*\*\* | 2.229\*\*\* |
|  | (0.006) | (0.004) |
| Observations | 1,389,551 | 1,385,227 |
| Adjusted R-squared | 0.454 | 0.387 |
| Year fixed effects | ✓ | ✓ |
| Contract x state x female fixed effects | ✓ | ✓ |
| Standard errors in parentheses | | |
| --- | --- | --- |
| \*\*\* p<0.01, \*\* p<0.05, \* p<0.1 | | |

### A.3 Model

This subsection lays out the equations that are similar in spirit to Postel-Vinay and Turon [[2007](https://arxiv.org/html/2510.16626v1#bib.bib16)] and Dickson et al. [[2014](https://arxiv.org/html/2510.16626v1#bib.bib3)] - the only difference being the data structure and the employment s​t​a​t​estate variable.

#### A.3.1 Unobserved Heterogeneity

The probability of an individual belonging in a particular class given their observed individual heterogeneity zifz\_{i}^{f} is given as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pr⁡{kiy,kim|zif}=Pr⁡{kiy|kim,zif}⋅Pr⁡{kim|zif}\ \Pr\{k\_{i}^{y},k\_{i}^{m}|z\_{i}^{f}\}=\Pr\{k\_{i}^{y}|k\_{i}^{m},z\_{i}^{f}\}\cdot\Pr\{k\_{i}^{m}|z\_{i}^{f}\} |  | (17) |

In this analysis, given four employment states, 4 transition classes & 3 income classes are settled upon after trying various other combinations, which give the best compromise between analytic efficiency and accuracy of model fit. Note that both kmk^{m} and kyk^{y} are categorical variables. Both components of
([17](https://arxiv.org/html/2510.16626v1#A1.E17 "In A.3.1 Unobserved Heterogeneity ‣ A.3 Model ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
 are expressed as multinomial logits with Ky=3K^{y}=3 and Km=4K^{m}=4 outcomes respectively. Based on a standard multinomial logit classification, the functional form of the probabilities of an individual belonging to these latent classes can be described as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pr⁡{kim=km∣zif}=exp⁡(zif⁣′​κkmm)∑k=1Kmexp⁡(zif⁣′​κkm),Pr⁡{kiy=ky∣kim,zif}=exp⁡((zifkim)′​κkyy)∑k=1Kyexp⁡((zifkim)′​κky),\begin{split}\Pr\{k\_{i}^{m}=k^{m}\mid z\_{i}^{f}\}=\frac{\exp\left(z\_{i}^{f\prime}\kappa^{m}\_{k^{m}}\right)}{\sum\_{k=1}^{K^{m}}\exp\left(z\_{i}^{f\prime}\kappa^{m}\_{k}\right)},\\ \Pr\{k\_{i}^{y}=k^{y}\mid k\_{i}^{m},z\_{i}^{f}\}=\frac{\exp\left(\begin{pmatrix}z\_{i}^{f}\\ k\_{i}^{m}\end{pmatrix}^{\!\prime}\kappa^{y}\_{k^{y}}\right)}{\sum\_{k=1}^{K^{y}}\exp\left(\begin{pmatrix}z\_{i}^{f}\\ k\_{i}^{m}\end{pmatrix}^{\!\prime}\kappa^{y}\_{k}\right)},\end{split} |  | (18) |

where kimk\_{i}^{m} takes the values 1, 2, 3 or 4 for an individual ii. Similarly, kiyk\_{i}^{y} takes the values 1, 2 or 3 for an individual ii. Here, κkm\kappa\_{k}^{m} and κky\kappa\_{k}^{y} are the vectors of coefficients of respective multinomial logits for the kt​hk^{th} outcome. Taking 1 as the base outcome in each multinomial logit, κ1m\kappa\_{1}^{m} and κ1y\kappa\_{1}^{y} are normalized to zero.

#### A.3.2 Transitions in labor market states and Transition classes: KmK^{m}

Moving on to the second component of the individual likelihood equation
([1](https://arxiv.org/html/2510.16626v1#S3.E1 "In 3.1 Structure ‣ 3 Model ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
, which encompasses the information in the model relating to the transitions between the various labor market states. Labor market states at year-t are assumed to depend on the individual’s previous labor market state and their observed and unobserved heterogeneity, i.e., it follows a conditional first-order Markov chain. As there are five possible states, the probability of the individual being in one of the five states is modeled as a multinomial logit where the explanatory variables are the previous labor market state and the individual’s unobserved and observed heterogeneity. Thus, at any given year (t > 1),

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pr⁡{Si,t=Ss|Si,t−1,zi,t−1v,zif,kim}=exp⁡((Si,t−1zi,t−1vzifkim)′​χSs)∑S=04exp⁡((Si,t−1zi,t−1vzifkim)′​χS)\ \Pr\{S\_{i,t}=S\_{s}|S\_{i,t-1},z\_{i,t-1}^{v},z\_{i}^{f},k\_{i}^{m}\}=\frac{\displaystyle\exp\Bigg(\begin{pmatrix}S\_{i,t-1}\\ z\_{i,t-1}^{v}\\ z\_{i}^{f}\\ k\_{i}^{m}\end{pmatrix}^{\prime}\chi\_{S\_{s}}\Bigg)}{\displaystyle\sum\_{S=0}^{4}\exp\Bigg(\begin{pmatrix}S\_{i,t-1}\\ z\_{i,t-1}^{v}\\ z\_{i}^{f}\\ k\_{i}^{m}\end{pmatrix}^{\prime}\chi\_{S}\Bigg)} |  | (19) |

This equation is valid for all years except for the first year as the first state is the initial value. The initial state is specified as being dependent only on the observed and unobserved heterogeneity and thus, similarly modeled as a multinomial logit:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pr⁡{Si,1=Ss|zif,kim}=exp⁡((zifkim)′​χSso)∑S=04exp⁡((zifkim)′​χSo)\ \Pr\{S\_{i,1}=S\_{s}|z\_{i}^{f},k\_{i}^{m}\}=\frac{\displaystyle\exp\bigg(\begin{pmatrix}z\_{i}^{f}\\ k\_{i}^{m}\end{pmatrix}^{\prime}\chi\_{S\_{s}}^{o}\bigg)}{\displaystyle\sum\_{S=0}^{4}\exp\bigg(\begin{pmatrix}z\_{i}^{f}\\ k\_{i}^{m}\end{pmatrix}^{\prime}\chi\_{S}^{o}\bigg)} |  | (20) |

[χs]s=0S−1[\chi\_{s}]\_{s=0}^{S-1} and [χso]s=0S−1[\chi\_{s}^{o}]\_{s=0}^{S-1} are the vectors of coefficients of the respective multinomial logits for the St​hS^{th} state outcome. χ0\chi\_{0} and χ0o\chi\_{0}^{o} are the base outcomes and normalized at zero.

Given these two specifications, we can now construct the (conditional) likelihood function of observing an individual’s employment state trajectory over the years as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℓi​(Si​t|zi​tv,zif,kim)=Pr⁡{Si​1|zif,kim}×∏t=2TiPr⁡{Si​t|Si,t−1,zi,t−1v,zif,kim}\ell\_{i}(S\_{it}|z\_{it}^{v},z\_{i}^{f},k\_{i}^{m})=\Pr\{S\_{i1}|z\_{i}^{f},k\_{i}^{m}\}\times\prod\_{t=2}^{T\_{i}}\Pr\{S\_{it}|S\_{i,t-1},z\_{i,t-1}^{v},z\_{i}^{f},k\_{i}^{m}\} |  | (21) |

### A.4 Estimating the mobility and income parameters using sequential EM

A sequential, limited information version of the EM algorithm inspired by Bonhomme and Robin [[2006](https://arxiv.org/html/2510.16626v1#bib.bib17)] is employed to obtain a consistent set of estimates. In the previous sections, one can see all the parameters of the model that need to be estimated. The entire list of parameters can be split into two:
Θm={(κkm)k=0Km−1,(χs)s=04,(χs0)s=04}\Theta^{m}=\big\{(\kappa\_{k}^{m})^{K^{m}-1}\_{k=0},(\chi\_{s})^{4}\_{s=0},(\chi^{0}\_{s})^{4}\_{s=0}\big\} and Θy={(κky)k=0Ky−1,μ,σ,ξ}\Theta^{y}=\big\{(\kappa\_{k}^{y})^{K^{y}-1}\_{k=0},\mu,\sigma,\xi\big\}. To recollect, we get the Θm\Theta^{m} parameters from the state mobility equations
([18](https://arxiv.org/html/2510.16626v1#A1.E18 "In A.3.1 Unobserved Heterogeneity ‣ A.3 Model ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
,
([19](https://arxiv.org/html/2510.16626v1#A1.E19 "In A.3.2 Transitions in labor market states and Transition classes: 𝐾^𝑚 ‣ A.3 Model ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
 and
([20](https://arxiv.org/html/2510.16626v1#A1.E20 "In A.3.2 Transitions in labor market states and Transition classes: 𝐾^𝑚 ‣ A.3 Model ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
; and we get the Θy\Theta^{y} parameters from the income process equations
([18](https://arxiv.org/html/2510.16626v1#A1.E18 "In A.3.1 Unobserved Heterogeneity ‣ A.3 Model ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
,
([4](https://arxiv.org/html/2510.16626v1#S3.E4 "In 3.3 Income process and Income class: 𝐾^𝑦 ‣ 3 Model ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
,
([5](https://arxiv.org/html/2510.16626v1#S3.E5 "In 3.3 Income process and Income class: 𝐾^𝑦 ‣ 3 Model ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
,
([8](https://arxiv.org/html/2510.16626v1#S3.E8 "In 3.3 Income process and Income class: 𝐾^𝑦 ‣ 3 Model ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
.
The structure of the complete individual likelihood equation
([1](https://arxiv.org/html/2510.16626v1#S3.E1 "In 3.1 Structure ‣ 3 Model ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
 means that it can be decomposed into two parts as shown below:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℒi​(𝐱i,ki;Θm,Θy)=ℒim​(𝐱i,kim;Θm)×ℒiy​(𝐱i,kim,kiy;Θy)\displaystyle\mathcal{L}\_{i}(\mathbf{x}\_{i},k\_{i};\Theta^{m},\Theta^{y})=\mathcal{L}\_{i}^{m}(\mathbf{x}\_{i},k\_{i}^{m};\Theta^{m})\times\mathcal{L}\_{i}^{y}(\mathbf{x}\_{i},k\_{i}^{m},k\_{i}^{y};\Theta^{y}) |  | (22) |
|  |  |  |
| --- | --- | --- |
|  | where ​ℒim​(𝐱i,kim;Θm)=ℓim​(𝐒i|𝐳iv,zif,kim;Θm)⋅Pr⁡{kim|zif;Θm}​, \displaystyle\text{where }\mathcal{L}\_{i}^{m}(\mathbf{x}\_{i},k\_{i}^{m};\Theta^{m})=\ell\_{i}^{m}\Big(\mathbf{S}\_{i}|\mathbf{z}\_{i}^{v},z\_{i}^{f},k\_{i}^{m};\Theta^{m}\Big)\cdot\Pr\Big\{k\_{i}^{m}|z\_{i}^{f};\Theta^{m}\Big\}\text{, } |  |
|  |  |  |
| --- | --- | --- |
|  | and ​ℒiy​(𝐱i,kim,kiy;Θy)=ℓiy​(𝐲i|Si,𝐳iv,zif,kim,kiy;Θy)⋅Pr⁡{kiy|kiy,zif;Θm}\displaystyle\text{and }\mathcal{L}\_{i}^{y}(\mathbf{x}\_{i},k\_{i}^{m},k\_{i}^{y};\Theta^{y})=\ell\_{i}^{y}\Big(\mathbf{y}\_{i}|S\_{i},\mathbf{z}\_{i}^{v},z\_{i}^{f},k\_{i}^{m},k\_{i}^{y};\Theta^{y}\Big)\cdot\Pr\Big\{k\_{i}^{y}|k\_{i}^{y},z\_{i}^{f};\Theta^{m}\Big\} |  |

This structure makes it easier to separate income sequences (𝐲𝐢)(\mathbf{y\_{i}}) and income classes (kiyk\_{i}^{y}) from the s​t​a​t​estate transition part of the likelihood function, ℒim​(𝐱i,kim;Θm)\mathcal{L}\_{i}^{m}(\mathbf{x}\_{i},k\_{i}^{m};\Theta^{m}). The parameters pertaining to the job mobility process and job transition classes can thus be recovered by separately considering the likelihood of observed job sector mobility: ∑i=1Nln⁡(∑kim=1Kmℒim​(𝐱i,kim;Θm))\sum\_{i=1}^{N}\ln\Big(\sum\_{k^{m}\_{i}=1}^{K^{m}}\mathcal{L}\_{i}^{m}(\mathbf{x}\_{i},k\_{i}^{m};\Theta^{m})\Big). The maximization can be achieved by applying the EM algorithm for finite mixtures. To make the process more efficient, the parameters for the s​t​a​t​estate transitions part of the likelihood equation are first estimated. This yields an initial estimate of Θ^m\hat{\Theta}^{m} for the mobility parameters. Then, Θm\Theta^{m} is fixed at Θ^m\hat{\Theta}^{m}, and the estimation proceeds to the income parameters Θy\Theta^{y}. After reaching a suitable convergence in terms of distance between the parameters from subsequent iterations, an initial estimate Θ^y\hat{\Theta}^{y} of Θy\Theta^{y} is obtained. Finally, using Θ^m\hat{\Theta}^{m} and Θ^y\hat{\Theta}^{y} as initial values, the complete likelihood function (given by equation
([1](https://arxiv.org/html/2510.16626v1#S3.E1 "In 3.1 Structure ‣ 3 Model ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
 and
([22](https://arxiv.org/html/2510.16626v1#A1.E22 "In A.4 Estimating the mobility and income parameters using sequential EM ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
) is estimated, allowing all parameters to vary, to arrive at the final estimates of all the mobility and income parameters.

#### A.4.1 Calibrating the initial job mobility parameters Θm\Theta^{m}

* •

  E-Step: For an initial value Θnm\Theta^{m}\_{n} of Θm\Theta^{m}, for each transition class km=1,…,Kmk^{m}=1,...,K^{m} and for each individual ii in the sample, the posterior probability that ii belongs to transition class kmk^{m} given 𝐱i\mathbf{x}\_{i} and Θnm\Theta^{m}\_{n} would be:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Pr⁡{kim=km|𝐱i;Θnm}=ℒim​(𝐱i,kim;Θnm)∑k=1Kmℒim​(𝐱i,kim;Θnm)\Pr\{k\_{i}^{m}=k^{m}|\mathbf{x}\_{i};\Theta^{m}\_{n}\}=\frac{\displaystyle\mathcal{L}\_{i}^{m}(\mathbf{x}\_{i},k\_{i}^{m};\Theta^{m}\_{n})}{\displaystyle\sum\_{k=1}^{K^{m}}\mathcal{L}\_{i}^{m}(\mathbf{x}\_{i},k\_{i}^{m};\Theta^{m}\_{n})} |  | (23) |

  These probabilities are calculated by estimating the likelihoods using using the functional forms of equations
  ([18](https://arxiv.org/html/2510.16626v1#A1.E18 "In A.3.1 Unobserved Heterogeneity ‣ A.3 Model ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
  ,
  ([19](https://arxiv.org/html/2510.16626v1#A1.E19 "In A.3.2 Transitions in labor market states and Transition classes: 𝐾^𝑚 ‣ A.3 Model ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
   and
  ([20](https://arxiv.org/html/2510.16626v1#A1.E20 "In A.3.2 Transitions in labor market states and Transition classes: 𝐾^𝑚 ‣ A.3 Model ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
  .
* •

  M-Step: We now update Θnm\Theta\_{n}^{m} into Θn+1m\Theta\_{n+1}^{m} by maximizing the following augmented sample log-likelihood, weighted by the E-Step equation above:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Θn+1m=arg​maxΘm​∑i=1N∑kim=1KmPr⁡{kim=k|𝐱i;Θnm}⋅ln⁡[ℒim​(𝐱i,kim;Θnm)]\Theta\_{n+1}^{m}=\operatorname\*{arg\,max}\_{\Theta^{m}}\sum\_{i=1}^{N}\sum\_{k\_{i}^{m}=1}^{K^{m}}\Pr\Big\{k\_{i}^{m}=k|\mathbf{x}\_{i};\Theta\_{n}^{m}\Big\}\cdot\ln\Big[\mathcal{L}\_{i}^{m}(\mathbf{x}\_{i},k\_{i}^{m};\Theta^{m}\_{n})\Big] |  | (24) |

  This maximization is carried out by creating 4 copies of out data set, one for each possible transition class that an individual can be in. Then we carry out weighted multinomial logits of kmk^{m}, S​t​a​t​eState, and S​t​a​t​ei​n​i​t​i​a​lState\_{initial} using equations
  ([18](https://arxiv.org/html/2510.16626v1#A1.E18 "In A.3.1 Unobserved Heterogeneity ‣ A.3 Model ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
  ,
  ([19](https://arxiv.org/html/2510.16626v1#A1.E19 "In A.3.2 Transitions in labor market states and Transition classes: 𝐾^𝑚 ‣ A.3 Model ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
   and
  ([20](https://arxiv.org/html/2510.16626v1#A1.E20 "In A.3.2 Transitions in labor market states and Transition classes: 𝐾^𝑚 ‣ A.3 Model ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
   weighing each copy of the data by its prior probability obtained in the E-step for the corresponding transition class kmk^{m}.

We continue iterations till the Euclidean distance between the coefficients in subsequent iterations falls below 10−310^{-3} as is standard in the literature. We can now use this initial estimate Θ^m\hat{\Theta}^{m} to calibrate the income process estimations in the next step.

#### A.4.2 Calibrating the income parameters Θy\Theta^{y}

* •

  E-Step: For an initial value Θny\Theta\_{n}^{y} of Θy\Theta^{y}, for each class index k=(km,ky)k=(k^{m},k^{y}), km=1,…,Km;ky=1,…,Kyk^{m}=1,...,K^{m};k^{y}=1,...,K^{y}, and for each individual ii in the sample, compute the posterior probability that ii belongs to transition class kmk^{m} and income class kyk^{y} given 𝐱i\mathbf{x}\_{i}, Θny\Theta\_{n}^{y} and Θ^m\hat{\Theta}^{m}:

  |  |  |  |  |
  | --- | --- | --- | --- |
  |  | Pr⁡{kim=km,kiy=ky|𝐱i;Θ^m,Θny}=ℒi​(𝐱i,km,ky;Θ^m,Θny)∑ℓm=1Km∑ℓy=1Kyℒi​(𝐱i,ℓm,ℓy;Θ^m,Θny)\Pr\Big\{k\_{i}^{m}=k^{m},k\_{i}^{y}=k^{y}|\mathbf{x}\_{i};\hat{\Theta}^{m},\Theta\_{n}^{y}\Big\}=\frac{\displaystyle\mathcal{L}\_{i}\Big(\mathbf{x}\_{i},k^{m},k^{y};\hat{\Theta}^{m},\Theta\_{n}^{y}\Big)}{\displaystyle\sum\_{\ell^{m}=1}^{K^{m}}\sum\_{\ell^{y}=1}^{K^{y}}\mathcal{L}\_{i}\Big(\mathbf{x}\_{i},\ell^{m},\ell^{y};\hat{\Theta}^{m},\Theta\_{n}^{y}\Big)} |  | (25) |
* •

  M-Step: In this step we update the μ,σ,ξ​ and ​κy\mu,\sigma,\xi\text{ and }\kappa^{y} coefficients. The following process is followed:

  1. 1.

     We first create 12 copies of our dataset. One for each kyk^{y} and kmk^{m} class combination that every individual can be in. Each class combination is weighted by the class probabilities obtained from equation
     ([25](https://arxiv.org/html/2510.16626v1#A1.E25 "In 1st item ‣ A.4.2 Calibrating the income parameters Θ^𝑦 ‣ A.4 Estimating the mobility and income parameters using sequential EM ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
     .
  2. 2.

     We then update the income mean parameter μ​(⋅)\mu(\cdot) using weighted OLS regressions of yi​ty\_{it} on (Si​t,zi​tv,zif,kiy)\Big(S\_{it},z\_{it}^{v},z\_{i}^{f},k\_{i}^{y}\Big), using the 12 class probabilities obtained from equation
     ([25](https://arxiv.org/html/2510.16626v1#A1.E25 "In 1st item ‣ A.4.2 Calibrating the income parameters Θ^𝑦 ‣ A.4 Estimating the mobility and income parameters using sequential EM ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
      in the E-Step as weights for each of the 12 copies of the data. The vector of coefficients of this regression thus becomes the updated μ^n+1​(⋅)\hat{\mu}^{n+1}(\cdot).
  3. 3.

     Similarly, the log squared residuals from the regression in step 2 are taken and regressed on (Si​t,zi​tv,zif,kiy)\Big(S\_{it},z\_{it}^{v},z\_{i}^{f},k\_{i}^{y}\Big), again using weighted OLS, to update income variance parameter σ^n+1​(⋅)\hat{\sigma}^{n+1}(\cdot).
  4. 4.

     Log income disturbances are updated as:

     |  |  |  |
     | --- | --- | --- |
     |  | y~i​tn+1=yi​t−μ^n+1​(Si​t,zi​tv,zif,kiy)σ^n+1​(Si​t,zi​tv,zif,kiy)\displaystyle\tilde{y}\_{it}^{n+1}=\frac{y\_{it}-\hat{\mu}\_{n+1}(S\_{it},z\_{it}^{v},z\_{i}^{f},k\_{i}^{y})}{\hat{\sigma}\_{n+1}(S\_{it},z\_{it}^{v},z\_{i}^{f},k\_{i}^{y})} |  |

     Next, we can generate the τi,t,t−1\tau\_{i,t,t-1} of y~i​t\tilde{y}\_{it} by taking into account all past income streams up until the year tt. So, for each year, the C​o​v​(y~i​tn+1,y~i,t−1n+1)Cov(\tilde{y}\_{it}^{n+1},\tilde{y}\_{i,t-1}^{n+1}) measure is expected to be the outcome of the τ1n+1​(⋅)\tau\_{1}^{n+1}(\cdot) function. Thus, we can update τ^1n+1​(⋅)\hat{\tau}\_{1}^{n+1}(\cdot) by taking the inverse functional form of τ1n+1\tau\_{1}^{n+1} that was given in
     ([8](https://arxiv.org/html/2510.16626v1#S3.E8 "In 3.3 Income process and Income class: 𝐾^𝑦 ‣ 3 Model ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
     . To do this, a new variable fi​tf\_{it} is defined such that:

     |  |  |  |
     | --- | --- | --- |
     |  | fi​t=l​n​(1+C​o​v​(y~i​tn+1,y~i,t−1n+1)1−C​o​v​(y~i​tn+1,y~i,t−1n+1))f\_{it}=ln\Bigg(\frac{\displaystyle 1+Cov(\tilde{y}\_{it}^{n+1},\tilde{y}\_{i,t-1}^{n+1})}{\displaystyle 1-Cov(\tilde{y}\_{it}^{n+1},\tilde{y}\_{i,t-1}^{n+1})}\Bigg) |  |

     We then regress fi​tf\_{it} on Si​t,Si,t−1,zi​tv,kim,kiy,Si​t∗kiy,Si,t−1∗kiyS\_{it},S\_{i,t-1},z\_{it}^{v},k\_{i}^{m},k\_{i}^{y},S\_{it}\*k\_{i}^{y},S\_{i,t-1}\*k\_{i}^{y}, again using equation
     ([25](https://arxiv.org/html/2510.16626v1#A1.E25 "In 1st item ‣ A.4.2 Calibrating the income parameters Θ^𝑦 ‣ A.4 Estimating the mobility and income parameters using sequential EM ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
      as weights. The vector of coefficients thus obtained is the updated ξn+1\xi^{n+1}.
  5. 5.

     Finally we can update the set of income class assignment parameters, (κky)k=0Ky−1\big(\kappa^{y}\_{k}\big)^{K^{y}-1}\_{k=0} by running a weighted multinomial logit regression of class indices on (zif,kim)\big(z\_{i}^{f},k\_{i}^{m}\big), again by using the
     ([25](https://arxiv.org/html/2510.16626v1#A1.E25 "In 1st item ‣ A.4.2 Calibrating the income parameters Θ^𝑦 ‣ A.4 Estimating the mobility and income parameters using sequential EM ‣ Appendix A Appendix ‣ Evaluating the Public Pay Gap: A Comparison of Public and Private Sector Wages in France"))
      as weights.

#### A.4.3 Likelihood Maximization

After obtaining the initial estimates of the Θm\Theta^{m} and Θy\Theta^{y} parameters separately, we then proceed to update the combined log-likelihood given by the equation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | likelihood: ​∏i=1N∏kim=1Km∏kiy=1Kyℒi​[𝐱i,(kim,kiy)]\displaystyle\text{likelihood: }\prod\_{i=1}^{N}\prod\_{k\_{i}^{m}=1}^{K^{m}}\prod\_{k\_{i}^{y}=1}^{K^{y}}\mathcal{L}\_{i}\Big[\mathbf{x}\_{i},(k\_{i}^{m},k\_{i}^{y})\Big] |  | (26) |
|  |  |  |  |
| --- | --- | --- | --- |
|  | log-likelihood: ​∑i=1Nln⁡(∑kim=1Km∑kiy=1Kyℒi​[𝐱i,(kim,kiy)])\displaystyle\text{log-likelihood: }\sum\_{i=1}^{N}\ln\Bigg(\sum\_{k\_{i}^{m}=1}^{K^{m}}\sum\_{k\_{i}^{y}=1}^{K^{y}}\mathcal{L}\_{i}\Big[\mathbf{x}\_{i},(k\_{i}^{m},k\_{i}^{y})\Big]\Bigg) |  | (27) |

We carry out this estimation using a similar methodology employed in the initialization phase.

### A.5 Model Fit

#### A.5.1 Additional Tables and Figures for Model Fit and Unobserved Heterogeneity

Table A.4: Demographic and Educational Composition by Transition Class (k​mkm)

| Transition | Female | Low ed | Med ed | High ed | Age <<31 | Age 31–45 | Age >>45 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| k​m=0km=0 | 0.65 | 0.51 | 0.16 | 0.32 | 0.25 | 0.43 | 0.32 |
| k​m=1km=1 | 0.66 | 0.71 | 0.29 | 0.00 | 0.32 | 0.40 | 0.28 |
| k​m=2km=2 | 0.33 | 0.86 | 0.14 | 0.00 | 0.32 | 0.39 | 0.29 |
| k​m=3km=3 | 0.56 | 0.68 | 0.10 | 0.22 | 0.23 | 0.41 | 0.36 |

Note: Means by class from the latent model output. Classes differ markedly in observed characteristics—e.g., gender and education—but overlap substantially across those dimensions, suggesting compositional clustering rather than latent behavioral types.




Table A.5: Transition Probabilities by Latent Transition Class (k​mkm) – Observed Data

| From/To | NE | Pvt FT | Pub FT | Pvt PT | Pub PT |
| --- | --- | --- | --- | --- | --- |
| Transition Class 0 | | | | | |
| NE | 0.81 | 0.10 | 0.02 | 0.05 | 0.01 |
| Pvt FT | 0.08 | 0.89 | 0.00 | 0.03 | 0.00 |
| Pub FT | 0.02 | 0.01 | 0.93 | 0.00 | 0.04 |
| Pvt PT | 0.15 | 0.12 | 0.00 | 0.72 | 0.01 |
| Pub PT | 0.08 | 0.01 | 0.14 | 0.01 | 0.76 |
| Transition Class 1 | | | | | |
| NE | 0.82 | 0.10 | 0.02 | 0.05 | 0.01 |
| Pvt FT | 0.09 | 0.88 | 0.00 | 0.03 | 0.00 |
| Pub FT | 0.03 | 0.01 | 0.92 | 0.00 | 0.05 |
| Pvt PT | 0.17 | 0.11 | 0.00 | 0.71 | 0.00 |
| Pub PT | 0.10 | 0.01 | 0.11 | 0.01 | 0.76 |
| Transition Class 2 | | | | | |
| NE | 0.83 | 0.11 | 0.01 | 0.04 | 0.01 |
| Pvt FT | 0.09 | 0.89 | 0.00 | 0.02 | 0.00 |
| Pub FT | 0.03 | 0.01 | 0.93 | 0.00 | 0.03 |
| Pvt PT | 0.19 | 0.13 | 0.00 | 0.67 | 0.00 |
| Pub PT | 0.12 | 0.01 | 0.13 | 0.01 | 0.72 |
| Transition Class 3 | | | | | |
| NE | 0.82 | 0.10 | 0.02 | 0.05 | 0.01 |
| Pvt FT | 0.08 | 0.89 | 0.00 | 0.03 | 0.00 |
| Pub FT | 0.02 | 0.00 | 0.93 | 0.00 | 0.04 |
| Pvt PT | 0.17 | 0.11 | 0.00 | 0.71 | 0.01 |
| Pub PT | 0.09 | 0.01 | 0.13 | 0.01 | 0.76 |

Note: Entries show the probability of remaining or moving between states from period tt to t+1t+1,
where NE = non-employment, Pvt FT = private full-time, Pub FT = public full-time, Pvt PT = private part-time, and Pub PT = public part-time.
Transition probabilities across the four latent transition classes (k​m=0km=0–33) show extremely similar magnitudes.
The persistence in key employment states (0.81–0.83 for non-employment, 0.88–0.89 for private full-time, and 0.92–0.93 for public full-time) varies by less than one percentage point across classes.
This similarity implies that the unobserved heterogeneity component (k​mkm) primarily reflects compositional differences in demographics and sectoral attachment rather than distinct behavioral adjustment regimes.




Table A.6: Summary of Latent Classes

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Latent Class | kyk^{y} | kmk^{m} | Class Size (%) | Female Share | Age Group | Educ. Level | Income Mobility | Labor Market Dynamics |
| 1 | 11 | 11 | 3.9% | 49.3% | 51.9% over 45 | Mixed | Upward (Q5: 35.9%) | High non-employment, mixed gender stability in Pvt FT, upward income mobility (Q5: 35.9%) |
| 2 | 11 | 22 | 0.1% | 50.9% | 54.7% over 45 | Low | Moderate (Q5: 20.4%) | High non-employment, women slower to transition to Pvt FT, moderate upward mobility (Q5: 20.4%) |
| 3 | 11 | 33 | 2.0% | 20.8% | 53.1% over 45 | Low | Moderate (Q5: 22.4%) | High non-employment, men stable in Pvt FT, moderate upward mobility (Q5: 22.4%) |
| 4 | 11 | 44 | 2.0% | 41.7% | Balanced | Mixed | Upward (Q5: 30.2%) | Balanced employment, more transitions to Pvt FT, upward mobility (Q5: 30.2%) |
| 5 | 22 | 11 | 13.8% | 71.1% | 42.7% over 45 | Low-Mid | Moderate (Q5: 23.9%) | Diverse transitions, more women shifting to Pvt PT, moderate income mobility (Q5: 23.9%) |
| 6 | 22 | 22 | 1.8% | 68.6% | Balanced | Low | Limited (Q5: 15.3%) | High non-employment, women remain in Pvt PT longer, limited upward mobility (Q5: 15.3%) |
| 7 | 22 | 33 | 12.4% | 36.7% | 41.5% over 45 | Low | Moderate (Q5: 18.2%) | Men stable in Pvt FT, limited transitions to Pvt PT, moderate income mobility (Q5: 18.2%) |
| 8 | 22 | 44 | 4.1% | 62.6% | 36.2% over 45 | Low | Limited (Q5: 19.4%) | High non-employment, women more likely to shift to Pvt PT, limited mobility (Q5: 19.4%) |
| 9 | 33 | 11 | 24.3% | 64.4% | 77.2% under 45 | Mixed | Upward (Q5: 25.5%) | Diverse transitions, women shift to/from public roles, upward income mobility (Q5: 25.5%) |
| 10 | 33 | 22 | 2.5% | 65.0% | 80.2% under 45 | Low-Mid | Limited (Q5: 13.1%) | High non-employment, younger workforce, women less upwardly mobile (Q5: 13.1%) |
| 11 | 33 | 33 | 32.2% | 32.4% | 77.6% under 45 | Low | Moderate (Q5: 14.4%) | Men stable in Pvt FT, fewer transitions to public roles, moderate mobility (Q5: 14.4%) |
| 12 | 33 | 44 | 1.1% | 55.9% | 83.3% under 45 | Mixed | Moderate (Q5: 20.1%) | Diverse transitions, balanced gender, younger workforce, moderate upward mobility (Q5: 20.1%) |




Table A.7: Predicted Transition Probabilities (Aggregate, Men, Women)

| From/To | NE | Pvt FT | Pub FT | Pvt PT | Pub PT |
| --- | --- | --- | --- | --- | --- |
| Aggregate | | | | | |
| Non-employment (NE) | 0.82 | 0.10 | 0.02 | 0.04 | 0.01 |
| Private full-time (Pvt FT) | 0.08 | 0.89 | 0.0025 | 0.03 | 0.0005 |
| Public full-time (Pub FT) | 0.02 | 0.01 | 0.93 | 0.0015 | 0.04 |
| Private part-time (Pvt PT) | 0.17 | 0.13 | 0.005 | 0.69 | 0.005 |
| Public part-time (Pub PT) | 0.09 | 0.01 | 0.14 | 0.01 | 0.74 |
| Total | 0.31 | 0.41 | 0.14 | 0.10 | 0.04 |

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Men | | | | | Women | | | | |
| From/To | NE | Pvt FT | Pub FT | Pvt PT | Pub PT | NE | Pvt FT | Pub FT | Pvt PT | Pub PT |
| NE | 0.84 | 0.11 | 0.015 | 0.03 | 0.005 | 0.82 | 0.09 | 0.02 | 0.06 | 0.02 |
| Pvt FT | 0.07 | 0.91 | 0.002 | 0.02 | 0.0003 | 0.09 | 0.86 | 0.003 | 0.05 | 0.001 |
| Pub FT | 0.03 | 0.007 | 0.94 | 0.001 | 0.02 | 0.02 | 0.005 | 0.93 | 0.002 | 0.05 |
| Pvt PT | 0.24 | 0.21 | 0.006 | 0.54 | 0.003 | 0.15 | 0.10 | 0.005 | 0.74 | 0.01 |
| Pub PT | 0.17 | 0.02 | 0.20 | 0.01 | 0.60 | 0.08 | 0.01 | 0.13 | 0.01 | 0.77 |
| Total | 0.32 | 0.52 | 0.11 | 0.04 | 0.01 | 0.31 | 0.31 | 0.17 | 0.15 | 0.06 |
| Max distance from observed: Aggregate=0.01 , Men=0.07 , Women=0.01 | | | | | | | | | |  |

![Refer to caption](x9.png)


Figure A.3: Predicted latent wage class distribution



![Refer to caption](Graphs/wages_obs_pred_pvt_ft.png)

![Refer to caption](Graphs/wages_obs_pred_pub_ft.png)

![Refer to caption](Graphs/wages_obs_pred_pvt_pt.png)

![Refer to caption](Graphs/wages_obs_pred_pub_pt.png)

Figure A.4: Wage Densities by employment state: Observed vs Predicted

#### A.5.2 Prediction: Out-of-sample predictions of wages and transitions

Transition probabilities

Table A.8: Transition Probabilities (Aggregate, Men, Women)

| From/To | NE | Pvt FT | Pub FT | Pvt PT | Pub PT |
| --- | --- | --- | --- | --- | --- |
| Aggregate | | | | | |
| Non-employment (NE) | 0.83 | 0.10 | 0.02 | 0.04 | 0.01 |
| Private full-time (Pvt FT) | 0.08 | 0.89 | 0.0024 | 0.03 | 0.0005 |
| Public full-time (Pub FT) | 0.02 | 0.01 | 0.93 | 0.0014 | 0.04 |
| Private part-time (Pvt PT) | 0.17 | 0.13 | 0.01 | 0.69 | 0.01 |
| Public part-time (Pub PT) | 0.09 | 0.01 | 0.14 | 0.01 | 0.74 |
| Total | 0.31 | 0.41 | 0.14 | 0.10 | 0.04 |

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Men | | | | | Women | | | | |
| From/To | NE | Pvt FT | Pub FT | Pvt PT | Pub PT | NE | Pvt FT | Pub FT | Pvt PT | Pub PT |
| NE | 0.84 | 0.11 | 0.02 | 0.03 | 0.01 | 0.82 | 0.09 | 0.02 | 0.06 | 0.02 |
| Pvt FT | 0.07 | 0.91 | 0.0019 | 0.02 | 0.0002 | 0.09 | 0.86 | 0.0034 | 0.05 | 0.0009 |
| Pub FT | 0.03 | 0.01 | 0.94 | 0.0011 | 0.02 | 0.02 | 0.0045 | 0.93 | 0.0015 | 0.05 |
| Pvt PT | 0.24 | 0.22 | 0.01 | 0.54 | 0.0033 | 0.14 | 0.10 | 0.0049 | 0.74 | 0.01 |
| Pub PT | 0.17 | 0.02 | 0.20 | 0.01 | 0.59 | 0.08 | 0.01 | 0.13 | 0.01 | 0.77 |
| Total | 0.32 | 0.52 | 0.11 | 0.04 | 0.01 | 0.31 | 0.31 | 0.17 | 0.15 | 0.06 |
| Max distance from observed: Aggregate=0.01 , Men=0.08 , Women=0.01 | | | | | | | | | |  |

Wage prediction fit

![Refer to caption](x10.png)


Figure A.5: Observed and predicted wage densities

![Refer to caption](x11.png)


Figure A.6: Observed and predicted wage densities by employment state

![Refer to caption](x12.png)


Figure A.7: Observed and predicted wage densities and wage classes

### A.6 Estimated model parameters

Table A.9: Parameters of unobserved mobility heterogeneity (mlogit models)

|  |  |  |  |
| --- | --- | --- | --- |
| Mobility heterogeneity: κim|zif\kappa\_{i}^{m}|z\_{i}^{f} | | | |
| κim=1\kappa\_{i}^{m}=1 | | | |
| female | -0.233 | first xp | -0.267 |
| educ=1 | 0.198 | constant | -1.361 |
| educ=2 | -20.756 |  |  |
| κim=2\kappa\_{i}^{m}=2 | | | |
| female | -1.581 | first xp | -0.263 |
| educ=1 | -0.626 | constant | 1.856 |
| educ=2 | -20.980 |  |  |
| κim=3\kappa\_{i}^{m}=3 | | | |
| female | -0.458 | first xp | 0.060 |
| educ=1 | -0.758 | constant | -1.307 |
| educ=2 | -0.679 |  |  |




Table A.10: Parameters of unobserved income heterogeneity (mlogit models)

|  |  |  |  |
| --- | --- | --- | --- |
| Income heterogeneity: κiy|κim,zif\kappa\_{i}^{y}|\kappa\_{i}^{m},z\_{i}^{f} | | | |
| κiy=1\kappa\_{i}^{y}=1 | | | |
| female | 0.752 | km=1 | 1.438 |
| educ=1 | -0.203 | km=2 | 0.535 |
| educ=2 | -0.968 | km=3 | -0.628 |
| first xp | -0.354 | constant | 1.835 |
| κiy=2\kappa\_{i}^{y}=2 |  |  |  |
| female | 0.535 | km=1 | 1.310 |
| educ=1 | -0.372 | km=2 | 0.984 |
| educ=2 | -0.497 | km=3 | -2.588 |
| first xp | -0.902 | constant | 3.312 |




Table A.11: Parameters of state mobility (mlogit models)

| Initial state selection: Pr{Si​1S\_{i1}} | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Si​1=1S\_{i1}=1 | | | | Si​1=3S\_{i1}=3 | | | |
| female | -0.609 | kmk^{m}=1 | -0.147 | female | 0.958 | kmk^{m}=1 | -0.203 |
| med educ | 0.653 | kmk^{m}=2 | 0.108 | med educ | 0.170 | kmk^{m}=2 | -0.197 |
| high educ | 0.695 | kmk^{m}=3 | -0.917 | high educ | 0.068 | kmk^{m}=3 | 0.596 |
| first xp | 0.600 | constant | -0.281 | first xp | 0.480 | constant | -1.912 |
| Si​1=2S\_{i1}=2 | | | | Si​1=4S\_{i1}=4 | | | |
| female | 0.233 | kmk^{m}=1 | -0.059 | female | 1.298 | kmk^{m}=1 | 0.004 |
| med educ | 1.175 | kmk^{m}=2 | -0.259 | med educ | 0.866 | kmk^{m}=2 | -0.381 |
| high educ | 1.635 | kmk^{m}=3 | -2.324 | high educ | 0.925 | kmk^{m}=3 | -0.440 |
| first xp | 0.958 | constant | -2.676 | first xp | 0.608 | constant | -3.715 |
| State selection parameters: Pr{Si​tS\_{it}} t>1 | | | | | | | |
| Si​t=1S\_{it}=1 | | | | Si​t=3S\_{it}=3 | | | |
| Si,t−1S\_{i,t-1}=1 | 3.119 | x​p2xp^{2} | -0.119 | Si,t−1S\_{i,t-1}=1 | 1.379 | x​p2xp^{2} | -0.059 |
| Si,t−1S\_{i,t-1}=2 | 0.231 | female | -0.264 | Si,t−1S\_{i,t-1}=2 | -0.587 | female | 0.731 |
| Si,t−1S\_{i,t-1}=3 | 1.391 | med educ | 0.370 | Si,t−1S\_{i,t-1}=3 | 3.282 | med educ | 0.175 |
| Si,t−1S\_{i,t-1}=4 | -0.171 | high educ | 0.439 | Si,t−1S\_{i,t-1}=4 | 0.368 | high educ | 0.134 |
| x​pi,t−1xp\_{i,t-1} | 1.675 | first xp | -1.545 | x​pi,t−1xp\_{i,t-1} | 0.984 | first xp | -0.819 |
| x​pi,t−1∗Si,t−1xp\_{i,t-1}\*S\_{i,t-1}=1 | 0.704 | kmk^{m}=1 | -0.110 | x​pi,t−1∗Si,t−1xp\_{i,t-1}\*S\_{i,t-1}=1 | 0.298 | kmk^{m}=1 | -0.110 |
| x​pi,t−1∗Si,t−1xp\_{i,t-1}\*S\_{i,t-1}=2 | 0.081 | kmk^{m}=2 | 0.024 | x​pi,t−1∗Si,t−1xp\_{i,t-1}\*S\_{i,t-1}=2 | 0.353 | kmk^{m}=2 | -0.144 |
| x​pi,t−1∗Si,t−1xp\_{i,t-1}\*S\_{i,t-1}=3 | 0.235 | kmk^{m}=3 | -0.601 | x​pi,t−1∗Si,t−1xp\_{i,t-1}\*S\_{i,t-1}=3 | 0.485 | kmk^{m}=3 | 0.183 |
| x​pi,t−1∗Si,t−1xp\_{i,t-1}\*S\_{i,t-1}=4 | -0.242 | constant | -2.065 | x​pi,t−1∗Si,t−1xp\_{i,t-1}\*S\_{i,t-1}=4 | 0.104 | constant | -3.506 |
| Si​t=2S\_{it}=2 | | | | Si​t=4S\_{it}=4 | | | |
| Si,t−1S\_{i,t-1}=1 | -0.270 | x​p2xp^{2} | -0.170 | Si,t−1S\_{i,t-1}=1 | -1.568 | x​p2xp^{2} | -0.124 |
| Si,t−1S\_{i,t-1}=2 | 5.307 | female | 0.261 | Si,t−1S\_{i,t-1}=2 | 3.686 | female | 0.947 |
| Si,t−1S\_{i,t-1}=3 | 0.237 | med educ | 0.494 | Si,t−1S\_{i,t-1}=3 | 0.363 | med educ | 0.462 |
| Si,t−1S\_{i,t-1}=4 | 2.930 | high educ | 0.769 | Si,t−1S\_{i,t-1}=4 | 4.669 | high educ | 0.447 |
| x​pi,t−1xp\_{i,t-1} | 1.063 | first xp | -0.906 | x​pi,t−1xp\_{i,t-1} | 1.254 | first xp | -0.936 |
| x​pi,t−1∗Si,t−1xp\_{i,t-1}\*S\_{i,t-1}=1 | 0.333 | kmk^{m}=1 | -0.023 | x​pi,t−1∗Si,t−1xp\_{i,t-1}\*S\_{i,t-1}=1 | 0.381 | kmk^{m}=1 | 0.018 |
| x​pi,t−1∗Si,t−1xp\_{i,t-1}\*S\_{i,t-1}=2 | 1.229 | kmk^{m}=2 | -0.130 | x​pi,t−1∗Si,t−1xp\_{i,t-1}\*S\_{i,t-1}=2 | 0.514 | kmk^{m}=2 | -0.296 |
| x​pi,t−1∗Si,t−1xp\_{i,t-1}\*S\_{i,t-1}=3 | -0.067 | kmk^{m}=3 | -1.058 | x​pi,t−1∗Si,t−1xp\_{i,t-1}\*S\_{i,t-1}=3 | 0.154 | kmk^{m}=3 | -0.125 |
| x​pi,t−1∗Si,t−1xp\_{i,t-1}\*S\_{i,t-1}=4 | 0.745 | constant | -4.010 | x​pi,t−1∗Si,t−1xp\_{i,t-1}\*S\_{i,t-1}=4 | 0.782 | constant | -5.101 |




Table A.12: Parameters of cross-sectional income means and standard deviations

| Income means: μ\mu | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Si​t=1S\_{it}=1 | 0 | x​pxp | 0.631 | Si​t×kyS\_{it}\times k^{y} | | | |
| Si​t=2S\_{it}=2 | -0.079 | x​p∗Si​t=2xp\*S\_{it}=2 | -0.055 | 1 1 | -1.061 | 3 1 | 1.075 |
| Si​t=3S\_{it}=3 | -3.031 | x​p∗Si​t=3xp\*S\_{it}=3 | 0.096 | 1 2 | -0.636 | 3 2 | 1.841 |
| Si​t=4S\_{it}=4 | -2.683 | x​p∗Si​t=4xp\*S\_{it}=4 | -0.018 | 2 1 | -0.416 | 4 1 | 1.828 |
| x​p2xp^{2} | -0.080 | female | -0.139 | 2 2 | -0.711 | 4 2 | 1.281 |
| med educ | 0.283 | high educ | 0.524 |  |  |  |  |
| first xp | -0.164 | constant | 10.182 |  |  |  |  |
| Income standard deviation: σ\sigma | | | | | | | |
| Si​t=2S\_{it}=2 | 0.085 | x​p2∗Si​t=1xp^{2}\*S\_{it}=1 | 0.076 | Si​t×kyS\_{it}\times k^{y} | | | |
| Si​t=3S\_{it}=3 | 1.842 | x​p2∗Si​t=2xp^{2}\*S\_{it}=2 | 0.187 | 1 1 | -0.348 | 3 1 | -0.582 |
| Si​t=4S\_{it}=4 | 2.082 | x​p2∗Si​t=3xp^{2}\*S\_{it}=3 | 0.122 | 1 2 | -0.224 | 3 2 | -0.632 |
| x​pxp | -0.590 | x​p2∗Si​t=4xp^{2}\*S\_{it}=4 | 0.259 | 2 1 | -0.432 | 4 1 | -1.552 |
| x​p∗Si​t=2xp\*S\_{it}=2 | -0.538 | first xp | 0.232 | 2 2 | -0.341 | 4 2 | -0.686 |
| x​p∗Si​t=3xp\*S\_{it}=3 | -0.327 | km=1k^{m}=1 | -0.006 |  |  |  |  |
| x​p∗Si​t=4xp\*S\_{it}=4 | -0.788 | km=2k^{m}=2 | -0.054 |  |  |  |  |
| km=3k^{m}=3 | 1.879 | female | -0.019 |  |  |  |  |
| med educ | -0.021 | high educ | 0.178 |  |  |  |  |
| constant | -3.524 |  |  |  |  |  |  |




Table A.13: Parameters of income mobility

| First-order income autocorrelation: τ1\tau\_{1} | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ky=1k^{y}=1 | -0.139 | Si,t−1=1S\_{i,t-1}=1 | 0.151 | ky×Si,tk^{y}\times S\_{i,t} | | x​pi,t−1×Si,t−1xp\_{i,t-1}\times S\_{i,t-1} | |
| ky=2k^{y}=2 | 0.008 | Si,t−1=2S\_{i,t-1}=2 | 0.131 | 1 2 | 0.077 | 1 | -0.019 |
| Si,t=2S\_{i,t}=2 | 0.019 | Si,t−1=3S\_{i,t-1}=3 | 0.149 | 1 3 | 0.126 | 2 | -0.057 |
| Si,t=3S\_{i,t}=3 | -0.066 | Si,t−1=4S\_{i,t-1}=4 | 0.096 | 1 4 | -0.110 | 3 | 0.039 |
| Si,t=4S\_{i,t}=4 | 0.204 | x​pi,t−1xp\_{i,t-1} | -0.610 | 2 2 | -0.069 | 4 | 0.008 |
| x​pxp | 0.717 | km=1k^{m}=1 | -0.033 | 2 3 | 0.068 |  | |
| x​p2xp^{2} | -0.017 | km=2k^{m}=2 | -0.035 | 2 4 | -0.186 |  | |
| constant | 0.310 | km=3k^{m}=3 | 0.194 |  | |  | |

### A.7 Results: Figures

![Refer to caption](Graphs/w_wo_selection_premia.png)


Figure A.8: Public premium in lifetime earnings: "job for life" counterfactuals with and without selection