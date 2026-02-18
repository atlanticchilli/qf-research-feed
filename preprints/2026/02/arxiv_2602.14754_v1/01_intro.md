---
authors:
- Chen Tang
- Jiaqi Liu
doc_id: arxiv:2602.14754v1
family_id: arxiv:2602.14754
is_current: false
taxonomy:
  alpha_families: []
  asset_classes: []
  horizons: []
  themes: []
title: A-H Premium and the Shanghai-Hong Kong Stock Connect
url_abs: http://arxiv.org/abs/2602.14754v1
url_html: https://arxiv.org/html/2602.14754v1
venue: arXiv q-fin
version: 1
year: 2026
---

Chen Tang
  
Australian National University
  
  
Jiaqi Liu
  
Australian National University

###### Abstract

This paper examines how the Shanghai-Hong Kong Stock Connect (SHHK) affects the A-H share price premium and whether the policy impact depends on market efficiency. Using monthly data for 67 Shanghai-listed A-H dual-listed firms from January 2011 to May 2019, we estimate a dynamic panel model with two-step system GMM to account for premium persistence and potential endogeneity. Market efficiency is proxied by trading-friction measures derived from daily high-low price ranges. We find that the implementation of SHHK is associated with an average 18.4% increase in the A-H premium. However, this effect is heterogeneous. The marginal policy impact is stronger for firms operating in less efficient markets and weaker for those with higher efficiency, indicating that pre-existing trading frictions condition the policy outcome. We find no significant response at the announcement stage. Placebo tests and alternative efficiency measures confirm the robustness of the efficiency-dependent effect. Overall, the results highlight the role of the information environment in shaping liberalization outcomes.

Keywords: A-H premium; Stock Connect; market efficiency; capital market liberalization; cross-listed firms

JEL Classification: G14; G15; G18

## 1 Introduction

In 1993, Tsingtao Brewery listed on both the Shanghai Stock Exchange and the Hong Kong Stock Exchange, which is the first A-H dual listed firm.111A-shares are China-based company stocks traded in RMB on Shanghai or Shenzhen stock exchanges. H-shares are stocks of mainland firms listed in Hong Kong, traded in HKD. After that, more and more mainland companies have started to dual-list on both the A-share market and the H-share market. After the past three decades, over 100 companies have successfully completed their A-H dual listing and financing.

Under the law of one price, the prices of dual-listed shares should be equal after adjusting for exchange rates, otherwise the arbitrage opportunity exists. However, this implication is violated in the case of Chinese A–H dual-listed firms, commonly referred to as the AH premium. Shares of the same company traded in the A-share market and the H-share market frequently exhibit persistent price differentials. Early evidence by Bailey, ([1994](https://arxiv.org/html/2602.14754v1#bib.bib2)) documents that domestically listed shares are often priced at a premium relative to their internationally listed counterparts. Extending this insight to the Chinese context, Chan and Kwok, ([2005](https://arxiv.org/html/2602.14754v1#bib.bib6)) analyzed A-shares, B-shares and H-shares of Chinese firms and find that A share prices are higher than B share or H shares. Besides, Li et al., ([2006](https://arxiv.org/html/2602.14754v1#bib.bib16)) also studied A-H dual listing firms and concludes that A-H dual-listed companies mostly shows a significant premium of A shares to H shares.

On 10 April 2014, the China Securities Regulatory Commission and the Securities and Futures commission jointly approved the pilot framework for the Shanghai–Hong Kong Stock Connect (SHHK Stock Connect, hereafter), establishing an institutional mechanism for cross-border equity trading between the Shanghai and Hong Kong markets. The programme was jointly implemented by the Shanghai Stock Exchange, Hong Kong Stock Exchange, China Securities Depository and Clearing Corporation Limited, and Hong Kong Securities Clearing Company Limited, with trading formally commencing on 17 November 2014. As the first formal link between Mainland China’s and Hong Kong’s equity markets, the SHHK Stock Connect marked a critical step in China’s gradual capital-market liberalization. By enabling mutual market access for domestic and international investors within a regulated framework, the scheme deepened financial integration between the two markets and advanced the two-way opening of China’s capital account. In doing so, it reinforced the international roles of Shanghai and Hong Kong as major financial centers and contributed to the outward-oriented development of China’s capital markets. Additionally, by expanding cross-border market access, SHHK Stock Connect can affect the AH premium through changes in trading frictions and arbitrage capacity. After the opening of SHHK Stock Connect program, there are more and more studies regarding the A-H dual listings’ share prices. Chan and Kwok, ([2016](https://arxiv.org/html/2602.14754v1#bib.bib7)) employ VECM to analyze the A-H share price premium and find that the Shanghai–Hong Kong Stock Connect announcement led to a significant reduction in the equilibrium AH premium, while in the post-implementation period, the AH premium is widen sharply. Hui and Chan, ([2018](https://arxiv.org/html/2602.14754v1#bib.bib14)) select 12 representative dual-listed companies in Shanghai and Hong Kong and find that after the implementation of the SHHK Stock Connect, AH premium significantly increased. However, some papers provide different perspectives. Fan and Wang, ([2017](https://arxiv.org/html/2602.14754v1#bib.bib12)) introduce corporate governance as a mechanism to explain the AH premium. Combined with market segmentation hypothesis, they find that the opening of SHHK Stock Connect significantly narrows the gap between AH share prices. Similarly, according to Pan and Chi, ([2021](https://arxiv.org/html/2602.14754v1#bib.bib19)), they use generalized method of moments (GMM) to analyze 56 Shanghai and Hong Kong dual-listing firms and find that SHHK Stock Connect can significantly reduce the AH share price premium.

Existing research are more focused on the average effect of SHHK Stock Connect and the conclusion is mixed. Building on the theoretical framework of market liberalization, there are some research emphasizing that the impact of policy shocks is not uniform across all securities. Bekaert et al., ([2005](https://arxiv.org/html/2602.14754v1#bib.bib3)) finds that the effect of liberalization depends on pre-existing financial development and institutional quality. This heterogeneity is further supported by Mitton, ([2006](https://arxiv.org/html/2602.14754v1#bib.bib18)), who demonstrates that the positive impacts of opening a stock market are significantly stronger for specific firms depending on their individual characteristics and ”investability”. Bond et al., ([2012](https://arxiv.org/html/2602.14754v1#bib.bib4)) argue that market prices can affect real outcomes through a feedback effect channel: when prices are more informative for real decision-making, economic actions that rely on market signals can respond more effectively, whereas limited informativeness weakens such transmission. Taken together, the mixed findings suggest that the impact of SHHK Stock Connect may have different effects across AH dual listing’s shares. Motivated by this possibility, our study examines not only the average effect of SHHK Stock Connect on the AH premium but also whether the policy impact varies systematically with A and H share market efficiency.

This paper makes three contributions. First, we show that the effect of SHHK Stock Connect on the AH premium is heterogeneous, which helps explain the mixed findings that focus on average effects. Second, following Meng et al., ([2023](https://arxiv.org/html/2602.14754v1#bib.bib17)) and Corwin and Schultz, ([2012](https://arxiv.org/html/2602.14754v1#bib.bib8)), we proxy market efficiency using a trading-frictions measure implied by high–low price ranges, and find that policy effects vary systematically with pre-policy market frictions. Third, we estimate the policy–premium relation in a dynamic panel framework that accounts for the strong persistence of the AH premium, and support the main results with placebo timing tests and alternative friction proxies.

## 2 Data and Methodology

### 2.1 Sample data

The sample period spans from January 2011 to May 2019, covering a total of 101 months. In line with Allen et al., ([2024](https://arxiv.org/html/2602.14754v1#bib.bib1)), we choose May 2019 as the end of our sample period to avoid Anti-ELAB movement222Anti-ELAB refers to Anti-Extradition Law Amendment Bill Movement in Hong Kong and Covid-19 epidemic effect. We employ monthly data rather than daily data for two primary reasons. First, daily observations are more sensitive to short-term fluctuations and transitory shocks, which may generate unreasonably high or low values and introduce excessive noise into the analysis. Second, trading calendars differ between the A-share and H-share markets, particularly due to differences in public holidays across mainland China and Hong Kong. For example, on a given calendar day, trading in the A-share market may correspond to the second trading day of the week, whereas trading in the H-share market may represent the first trading day following a holiday. Market sentiment can differ substantially under such circumstances, and directly comparing daily prices across the two markets may therefore lead to biased estimates. To mitigate this issue, we aggregate daily observations to the monthly level by taking the average of all daily observations within each month. To identify the effect of the Shanghai–Hong Kong Stock Connect (SHHK), we restrict our sample to firms that completed A–H dual listings prior to the implementation of the SHHK program and whose A-shares are listed on the Shanghai Stock Exchange. Additionally, we also exclude the firm-month observations with missing values. Finally, we obtained 6,462 firm-month observations and 67 unique AH dual-listed firms. Appendix A lists the company name, A-share listing date and code, and H-share listing date and code for all sample firms.
A-share and H-share price data are obtained from the Wind Financial Terminal. Other share-related variables and firm-level characteristics come from the Choice database.

### 2.2 Variable construction

Following Fan and Wang, ([2017](https://arxiv.org/html/2602.14754v1#bib.bib12)), we define the A-H share premium as the ratio of the A-share price to its corresponding H-share price after adjusting for exchange rate differences. In line with Fan and Wang, ([2017](https://arxiv.org/html/2602.14754v1#bib.bib12)); Pan and Chi, ([2021](https://arxiv.org/html/2602.14754v1#bib.bib19)), we include the lagged premium term, Premt−1\text{Prem}\_{t-1}, to account for potential autocorrelation in the dependent variable. To capture the effect of the SHHK Stock Connect, we construct a binary indicator that equals one for observations after November 2014 and zero otherwise.

To evaluate the efficiency of A-share market and H-share market, we use daily highest and lowest price to estimate the bid-ask spread as proposed by Corwin and Schultz, ([2012](https://arxiv.org/html/2602.14754v1#bib.bib8)). Following the literature, we construct the following equations to calculate the daily bid-ask spread.

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​{∑j=01[ln⁡(Ht+j0Lt+j0)]2}=2​k1​σH​L2+4​k2​σH​L​ln⁡(2+S2−S)+2​[ln⁡(2+S2−S)]2,\mathbb{E}\left\{\sum\_{j=0}^{1}\left[\ln\!\left(\frac{H^{0}\_{t+j}}{L^{0}\_{t+j}}\right)\right]^{2}\right\}=2k\_{1}\sigma\_{HL}^{2}+4k\_{2}\sigma\_{HL}\ln\!\left(\frac{2+S}{2-S}\right)+2\left[\ln\!\left(\frac{2+S}{2-S}\right)\right]^{2}, |  | (1) |

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔼​{[ln⁡(Ht,t+10Lt,t+10)]2}=2​k1​σH​L2+2​2​k2​σH​L​ln⁡(2+S2−S)+[ln⁡(2+S2−S)]2,\mathbb{E}\left\{\left[\ln\!\left(\frac{H^{0}\_{t,t+1}}{L^{0}\_{t,t+1}}\right)\right]^{2}\right\}=2k\_{1}\sigma\_{HL}^{2}+2\sqrt{2}k\_{2}\sigma\_{HL}\ln\!\left(\frac{2+S}{2-S}\right)+\left[\ln\!\left(\frac{2+S}{2-S}\right)\right]^{2}, |  | (2) |

where SS denotes the bid-ask spread; Ht+j0H^{0}\_{t+j} and Lt+j0L^{0}\_{t+j} are the
daily highest and lowest prices of a stock at the trading day of t+jt+j ,
respectively; Ht,t+10H^{0}\_{t,t+1} and Lt,t+10L^{0}\_{t,t+1} are the daily highest and lowest
prices, respectively, of a stock observed on two consecutive trading days tt and t+1t+1;
σH​L\sigma\_{HL} denotes volatility; and k1k\_{1} and k2k\_{2} are coefficients.

Equation (1) is a one-day range of the spread (SS) at the time of t+jt+j. Equation (2) is a two-day range of the spread (SS) from the time of tt to t+1t+1.

Additionally, in order to make the process easier and in line with Corwin and Schultz, ([2012](https://arxiv.org/html/2602.14754v1#bib.bib8)), we define following:

|  |  |  |  |
| --- | --- | --- | --- |
|  | β=𝔼​{∑j=01[ln⁡(Ht+j0Lt+j0)]2},γ=𝔼​{[ln⁡(Ht,t+10Lt,t+10)]2}.\beta=\mathbb{E}\left\{\sum\_{j=0}^{1}\left[\ln\!\left(\frac{H^{0}\_{t+j}}{L^{0}\_{t+j}}\right)\right]^{2}\right\},\qquad\gamma=\mathbb{E}\left\{\left[\ln\!\left(\frac{H^{0}\_{t,t+1}}{L^{0}\_{t,t+1}}\right)\right]^{2}\right\}. |  | (3) |

Solving Equations (1) and Equation (2), we can obtain the spread (SS) equation, which is our closed form equation.

|  |  |  |  |
| --- | --- | --- | --- |
|  | S=2​(eα−1)1+eα.S=\frac{2\left(e^{\alpha}-1\right)}{1+e^{\alpha}}. |  | (4) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | α=2​β−β3−2​2−γ3−2​2.\alpha=\frac{\sqrt{2\beta}-\sqrt{\beta}}{3-2\sqrt{2}}-\sqrt{\frac{\gamma}{3-2\sqrt{2}}}. |  | (5) |

After calculating the daily spread, we take monthly average to match the frequency of other variables333For negative daily bid–ask spread estimates (SS), we follow Corwin and Schultz, ([2012](https://arxiv.org/html/2602.14754v1#bib.bib8)) and set negative values to zero prior to calculating monthly averages. This approach provides more accurate estimates than either retaining negative spread observations or excluding them from the sample.. In line with Meng et al., ([2023](https://arxiv.org/html/2602.14754v1#bib.bib17)), we use the negative of the of bid/ask spreads to proxy for market efficiency. In other words, there is a negative relationship between bid/ask spread and market efficiency. In addition, we construct an aggregate efficiency measure, E​f​f​b​o​t​hEffboth, by summing the A-share and H-share market efficiency proxies to capture the overall information environment of A-H dual listed firms 444It is worth noting that E​f​f​b​o​t​hEffboth is strictly negative in our sample by construction. Values closer to zero indicate higher market efficiency, while more negative values correspond to lower efficiency..

Regarding control variables, given the different liquidity conditions in the A-share and H-share markets, we proxy for relative liquidity using the firm-level relative turnover ratio measured at the monthly frequency (Lee et al.,, [2001](https://arxiv.org/html/2602.14754v1#bib.bib15)). Consistent with Chakravarty et al., ([1998](https://arxiv.org/html/2602.14754v1#bib.bib5)), firm size is proxied by market capitalization. As the distribution of market capitalization is positively skewed, we take its natural logarithm to mitigate the influence of extreme observations.555Market capitalization is calculated as the aggregate value of all shares listed across different stock exchanges and is adjusted for exchange rate differences. Firm size is further included to account for differences in information asymmetry, as larger firms are generally associated with lower levels of asymmetric information.

We include an indicator variable, *SOE*, which equals one if the firm is state-owned and zero otherwise. Following Chan and Kwok, ([2005](https://arxiv.org/html/2602.14754v1#bib.bib6)), we control for relative share demand by including the ratio of the number of floating A-shares to the number of floating H-shares.

Finally, to capture relative monetary conditions between the two markets, we construct a relative interest rate variable, *Interest rate*, defined as the ratio of the three-month Shanghai Interbank Offered Rate (SHIBOR) to the three-month Hong Kong Interbank Offered Rate (HIBOR).

![Refer to caption](Figure_1.jpg)


Figure 1: Trend of AH premium from Jan 2011 to May 2019

### 2.3 Regression model

In this paper, we employ the generalized method of moments (GMM) rather than the traditional fixed-effects estimator. This approach has two main advantages. First, it allows us to control for serial correlation in the dependent variable by including its lagged value. Second, it helps mitigate potential endogeneity concerns by introducing internal instrumental variables.

To test our hypothesis, we propose following regression framework:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Premi​t=αi+β​Premi,t−1+θ​SHHKPolicyt+γ′​Xi​t+εi​t.\text{Prem}\_{it}=\alpha\_{i}+\beta\,\text{Prem}\_{i,t-1}+\theta\,\text{SHHKPolicy}\_{t}+\gamma^{\prime}X\_{it}+\varepsilon\_{it}. |  | (6) |

where the P​r​e​mi,tPrem\_{i,t} is the AH share price premium for share ii at month tt, which is calculated as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Premi,t=Pi​tAPi​tH×HKD/CNYt−1.\text{Prem}\_{i,t}=\frac{P^{A}\_{it}}{P^{H}\_{it}\times\text{HKD/CNY}\_{t}}-1. |  | (7) |

,
Following Domowitz et al., ([1997](https://arxiv.org/html/2602.14754v1#bib.bib9)) and Fan and Wang, ([2017](https://arxiv.org/html/2602.14754v1#bib.bib12)), we control the lagged term P​r​e​mi,t−1Prem\_{i,t-1} to reduce the effect of autocorrelation.
S​H​H​K​P​o​l​i​c​ytSHHKPolicy\_{t} is an indicator that equals to one if the time is after November 2014 and 0 otherwise. Xi​tX\_{it} denotes a kk-dimensional vector of control variables.

## 3 Empirical results

Table 1 lists the descriptive statistics for main variables used in the regression model, including the mean value, max value, min value, standard deviation and number of observations, respectively. We can see that the mean value of the premium is 68.3% which is consistent with previous research.

Table 1: Descriptive Statistics

| Variable | Mean | Max | Min | Median | SD | N |
| --- | --- | --- | --- | --- | --- | --- |
| Prem | 0.683 | 7.759 | -0.346 | 0.462 | 0.832 | 6,462 |
| SHHKPolicy | 0.558 | 1.000 | 0.000 | 1.000 | 0.497 | 6,462 |
| Effboth | -0.015 | -0.002 | -0.067 | -0.014 | 0.006 | 6,462 |
| Turnover | 2.009 | 120.209 | 0.012 | 1.035 | 3.429 | 6,462 |
| SOE | 0.919 | 1.000 | 0.000 | 1.000 | 0.273 | 6,462 |
| Demand | 2.928 | 48.046 | 0.040 | 2.614 | 1.951 | 6,462 |
| Size | 25.028 | 28.555 | 21.262 | 24.906 | 1.456 | 6,462 |
| Interest rate | 9.020 | 23.380 | 1.355 | 9.095 | 5.414 | 6,462 |

We first test Hypothesis 1, which examines the effect of the SHHK Stock Connect on the A-H share price premium. Table 2 reports the baseline dynamic panel regression results. Column (1) only includes the lagged premium and the SHHK Stock Connect indicator. The coefficient on S​H​H​K​P​o​l​i​c​ySHHKPolicy is positive and statistically significant at the 1% level, indicating that the introduction of the Stock Connect is associated with an increase in the A-H share price premium.

Columns (2) to (6) progressively incorporate additional firm-level control variables, with Column (6) representing the full specification. Across all specifications, the estimated coefficient on S​H​H​K​P​o​l​i​c​ySHHKPolicy remains positive and significant at 1% level. In the full model, the coefficient on S​H​H​K​P​o​l​i​c​ySHHKPolicy is 0.184, implying that, holding other variables constant, the implementation of the SHHK Stock Connect is associated with an average increase of approximately 18.4% in the A-H share price premium for a given pair of dual-listed shares.
The baseline regression results present an average effect of the SHHK Stock Connect on the A-H share price premium. However, the economic mechanisms under this effect remain unclear. If SHHK Stock Connect operates by alleviating market frictions and improving information transmission, its impact should be more pronounced in less efficient markets. This motivates our analysis of efficiency-dependent effects in the next subsection.

Table 2: Baseline Effect of the SHHK Stock Connect on the A-H Share Price Premium

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | AH Premium | AH Premium | AH Premium | AH Premium | AH Premium | AH Premium |
|  | (1) | (2) | (3) | (4) | (5) | (6) |
| Lagged Premium | 0.727∗∗∗ | 0.676∗∗∗ | 0.677∗∗∗ | 0.676∗∗∗ | 0.693∗∗∗ | 0.694∗∗∗ |
|  | (0.130) | (0.144) | (0.142) | (0.142) | (0.136) | (0.136) |
| SHHKPolicy | 0.184∗∗∗ | 0.145∗∗∗ | 0.144∗∗∗ | 0.147∗∗∗ | 0.180∗∗∗ | 0.184∗∗∗ |
|  | (0.017) | (0.025) | (0.024) | (0.023) | (0.022) | (0.022) |
| Turnover |  | 0.025 | 0.025∗ | 0.024∗ | 0.017∗∗ | 0.017∗∗ |
|  |  | (0.015) | (0.015) | (0.014) | (0.009) | (0.009) |
| SOE |  |  | 0.055 | 0.053 | 0.030 | 0.030 |
|  |  |  | (0.059) | (0.062) | (0.050) | (0.049) |
| Demand |  |  |  | -0.012 | -0.005 | -0.005 |
|  |  |  |  | (0.014) | (0.012) | (0.012) |
| Size |  |  |  |  | -0.075∗ | -0.075∗ |
|  |  |  |  |  | (0.044) | (0.043) |
| Interest rate |  |  |  |  |  | 0.002 |
|  |  |  |  |  |  | (0.002) |
| Observations | 6363 | 6363 | 6363 | 6363 | 6363 | 6363 |
| AR(2) pp-value | 0.315 | 0.912 | 0.915 | 0.891 | 0.797 | 0.758 |
| Hansen Test pp-value | 0.548 | 0.416 | 0.417 | 0.425 | 0.462 | 0.469 |

* •

  Notes: This table reports dynamic panel estimates of the effect of the SHHK Stock Connect on the A-H share price premium. Columns (1)–(6) sequentially add firm-level control variables to the baseline specification. All models are estimated using two-step system GMM. The lagged dependent variable is instrumented using its own lags dated t−2t-2 and t−3t-3 in the differenced equation. Firm and year fixed effects are included. Robust two-step standard errors are reported in parentheses.
* •

  ∗∗∗, ∗∗, and ∗ denote statistical significance at the 1%, 5%, and 10% levels, respectively.

### 3.1 Market Efficiency and the Effects of the SHHK Stock Connect

Market efficiency plays a central role in determining how quickly asset prices reflect available information (Fama,, [1970](https://arxiv.org/html/2602.14754v1#bib.bib10), [1991](https://arxiv.org/html/2602.14754v1#bib.bib11)). In the context of cross-listed shares, cross-market frictions and information-based barriers can impede arbitrage and contribute to deviations from price parity across trading venues (Gagnon and Andrew Karolyi,, [2010](https://arxiv.org/html/2602.14754v1#bib.bib13)). More generally, when limits to arbitrage, trading frictions, or institutional constraints are present, prices of economically equivalent securities may deviate from parity and fail to converge quickly (Shleifer and Vishny,, [1997](https://arxiv.org/html/2602.14754v1#bib.bib20); Gagnon and Andrew Karolyi,, [2010](https://arxiv.org/html/2602.14754v1#bib.bib13)).

Meng et al., ([2023](https://arxiv.org/html/2602.14754v1#bib.bib17)) finds that the SHHK Stock Connect increases the A share market efficiency of AH dual listing firms through stock price informational efficiency and corporate governance. Motivated by their research, we test whether the effect of the SHHK Stock Connect on the A-H share price premium depends on market efficiency. We construct the following model:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Premi​t=αi+β1​Premi,t−1+β2​SHHKPolicyt+β3​Effbotht+β4​SHHKPolicy × Effbotht+γ′​Xi​t+εi​t\text{Prem}\_{it}=\alpha\_{i}+\beta\_{1}\text{Prem}\_{i,t-1}+\beta\_{2}\text{SHHKPolicy}\_{t}+\beta\_{3}\text{Effboth}\_{t}+\beta\_{4}\text{SHHKPolicy $\times$ Effboth}\_{t}+\gamma^{\prime}X\_{it}+\varepsilon\_{it} |  | (8) |

where the P​r​e​mi,tPrem\_{i,t} is the AH share price premium for share ii at month tt. Follow Domowitz et al., ([1997](https://arxiv.org/html/2602.14754v1#bib.bib9)) and Fan and Wang, ([2017](https://arxiv.org/html/2602.14754v1#bib.bib12)), we control the lagged term P​r​e​mi,t−1Prem\_{i,t-1} to reduce the effect of autocorrelation.

Table 3 reports the regression results. Interestingly, after considering the interaction term between the Stock Connect indicator and market efficiency (S​H​H​K​P​o​l​i​c​y×E​f​f​b​o​t​hSHHKPolicy\times Effboth) and efficiency for both market (E​f​f​b​o​t​hEffboth), the coefficient of S​H​H​K​P​o​l​i​c​ySHHKPolicy becomes negative and statistically significant. The reason is that coefficient on S​H​H​K​P​o​l​i​c​ySHHKPolicy no longer captures the average policy effect, but rather the effect evaluated at E​f​f​b​o​t​h=0Effboth=0. Since E​f​f​b​o​t​hEffboth is strictly negative in our sample, this coefficient should not be interpreted in isolation.
In this model, the marginal effect of SHHK Stock Connect is:

|  |  |  |
| --- | --- | --- |
|  | ∂p​r​e​m∂S​H​H​K​P​o​l​i​c​y=β2+β4​E​f​f​b​o​t​h,\frac{\partial prem}{\partial SHHKPolicy}=\beta\_{2}+\beta\_{4}Effboth, |  |

so that, under our scaling where E​f​f​b​o​t​h<0Effboth<0 and values closer to zero indicate higher efficiency, the estimated policy effect increases as E​f​f​b​o​t​hEffboth becomes more negative (i.e., as efficiency declines). Consequently, the Stock Connect is associated with a larger change in the AH premium for firms operating under less efficient market conditions than for those with higher efficiency. Overall, the results in Table 3 support an efficiency-dependent policy effect both statistically and economically.

Table 3: Efficiency-Dependent Effects of the SHHK Stock Connect

|  |  |
| --- | --- |
|  | AH Premium |
|  | (1) |
| Lagged Premium | 0.633\*\*\* |
|  | (0.081) |
| SHHKPolicy | −0.490∗∗-0.490^{\*\*} |
|  | (0.196) |
| Effboth | 39.554\*\* |
|  | (15.105) |
| SHHKPolicy ×\times Effboth | −45.900∗⁣∗∗-45.900^{\*\*\*} |
|  | (14.584) |
| Turnover | 0.022\*\*\* |
|  | (0.007) |
| SOE | 0.021 |
|  | (0.045) |
| Demand | −0.009-0.009 |
|  | (0.011) |
| Firm Size | −0.108∗⁣∗∗-0.108^{\*\*\*} |
|  | (0.031) |
| Interest Rate | 0.007\*\*\* |
|  | (0.002) |
| Observations | 6,363 |
| AR(2) pp-value | 0.211 |
| Hansen Test pp-value | 0.780 |

* •

  Notes: This table reports dynamic panel estimates examining how market efficiency conditions the effect of the SHHK Stock Connect on the AH price premium. E​f​f​b​o​t​hEffboth measures overall market efficiency across the A- and H-share markets, with higher values (less negative) indicating greater efficiency. The interaction term allows the policy effect to vary with market efficiency. The model is estimated using two-step system GMM. Lagged dependent variables and potentially endogenous regressors are instrumented using their own lags dated t−2t-2 and t−3t-3. Firm and year fixed effects are included. Robust standard errors are reported in parentheses.
* •

  ∗∗∗, ∗∗, and ∗ denote statistical significance at the 1%, 5%, and 10% levels, respectively.

### 3.2 Robustness check

In this subsection, we employ several robustness checks to make our result more reliable. Firstly, we examine whether the initial policy announcement generated an immediate pricing response. Specifically, we use April 2014 as an alternative event date, motivated by Premier Li Keqiang’s statement on 10 April 2014 regarding the establishment of a Shanghai-Hong Kong stock market connectivity mechanism.666On 10 April 2014, Premier Li Keqiang stated that China would actively create conditions to establish a Shanghai-Hong Kong stock exchanges connectivity mechanism to promote further two-way opening-up and the healthy development of the mainland and Hong Kong capital markets. Table 4 reports GMM estimates across specifications in Columns (1)-(6), where control variables are sequentially added and Column (6) presents the full model. Across all columns, the estimated coefficient on A​n​n​o​u​n​c​e​m​e​n​tAnnouncement is close to zero and statistically insignificant, suggesting no economically meaningful change in the AH premium around the announcement date at the monthly frequency. A potential interpretation is that the announcement did not immediately relax the trading, settlement, or capital-account constraints that limit cross-market arbitrage; consequently, any convergence forces induced by the policy were unlikely to materialize until implementation.

Table 4: Announcement Effect of the SHHK Stock Connect on the A-H Share Price Premium

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | AH Premium | AH Premium | AH Premium | AH Premium | AH Premium | AH Premium |
|  | (1) | (2) | (3) | (4) | (5) | (6) |
| Lagged Premium | 0.788∗∗∗ | 0.725∗∗∗ | 0.726∗∗∗ | 0.726∗∗∗ | 0.748∗∗∗ | 0.748∗∗∗ |
|  | (0.115) | (0.125) | (0.124) | (0.126) | (0.115) | (0.115) |
| Announcement | 0.001 | -0.008 | -0.008 | -0.007 | 0.004 | 0.004 |
|  | (0.019) | (0.022) | (0.022) | (0.021) | (0.015) | (0.017) |
| Turnover |  | 0.023∗ | 0.023∗ | 0.022∗ | 0.016∗∗ | 0.016∗∗ |
|  |  | (0.013) | (0.013) | (0.012) | (0.007) | (0.007) |
| SOE |  |  | 0.048 | 0.046 | 0.027 | 0.027 |
|  |  |  | (0.048) | (0.051) | (0.039) | (0.039) |
| Demand |  |  |  | -0.009 | -0.004 | -0.004 |
|  |  |  |  | (0.012) | (0.009) | (0.009) |
| Size |  |  |  |  | -0.060∗ | -0.060∗ |
|  |  |  |  |  | (0.036) | (0.036) |
| Interest rate |  |  |  |  |  | -0.000 |
|  |  |  |  |  |  | (0.002) |
| Observations | 6363 | 6363 | 6363 | 6363 | 6363 | 6363 |
| AR(2) pp-value | 0.152 | 0.621 | 0.627 | 0.596 | 0.449 | 0.452 |
| Hansen Test pp-value | 0.522 | 0.404 | 0.405 | 0.413 | 0.442 | 0.441 |

* •

  Notes: This table reports dynamic panel estimates of the effect of the announcement of SHHK Stock Connect on the A-H share price premium. Columns (1)–(6) sequentially add firm-level control variables to the baseline specification. All models are estimated using two-step system GMM. The lagged dependent variable is instrumented using its own lags dated t−2t-2 and t−3t-3 in the difference equation. Firm and year fixed effects are included. Robust two-step standard errors are reported in parentheses.
* •

  ∗∗∗, ∗∗, and ∗ denote statistical significance at the 1%, 5%, and 10% levels, respectively.

Table 5 examines whether the announcement of the SHHK Stock Connect has an efficiency-dependent effect on the A-H price premium. The coefficient on A​n​n​o​u​n​c​e​m​e​n​tAnnouncement is negative but statistically insignificant (−0.217-0.217), suggesting no significant change in the AH premium around the announcement date. More importantly, the interaction term A​n​n​o​u​n​c​e​m​e​n​tAnnouncement ×\times E​f​f​b​o​t​hEffboth is also statistically insignificant (−14.471-14.471), providing no evidence that the announcement effect varies systematically with market efficiency. Consistent with these results, the main effect of E​f​f​b​o​t​hEffboth is not statistically different from zero in this specification. Overall, Table 5 indicates that the announcement itself and the interaction with market efficiency are unlikely to generate a measurable impact on the AH premium.

Table 5: Efficiency-Dependent Effects of the announcement of SHHK Stock Connect

|  | AH Premium |
| --- | --- |
|  | (1) |
| Lagged Premium | 0.678∗∗∗ |
|  | (0.092) |
| Announcement | -0.217 |
|  | (0.203) |
| Effboth | 13.023 |
|  | (13.283) |
| Announcement ×\times Effboth | -14.471 |
|  | (13.547) |
| Turnover | 0.021∗∗∗ |
|  | (0.006) |
| SOE | 0.026 |
|  | (0.039) |
| Demand | -0.005 |
|  | (0.009) |
| Size | -0.087∗∗ |
|  | (0.033) |
| Interest rate | 0.001 |
|  | (0.002) |
| Observations | 6,363 |
| AR(2) pp-value | 0.298 |
| Hansen Test pp-value | 0.778 |

* •

  Notes: This table reports dynamic panel estimates examining how market efficiency conditions the effect of the announcement of SHHK Stock Connect on the AH price premium. E​f​f​b​o​t​hEffboth measures overall market efficiency across the A- and H-share markets, with higher values (less negative) indicating greater efficiency. The interaction term allows the policy effect to vary with market efficiency. The model is estimated using two-step system GMM. Lagged dependent variables and potentially endogenous regressors are instrumented using their own lags dated t−2t-2 and t−3t-3. Firm and year fixed effects are included. Robust standard errors are reported in parentheses.
* •

  ∗∗∗, ∗∗, and ∗ denote statistical significance at the 1%, 5%, and 10% levels, respectively.

According to Meng et al., ([2023](https://arxiv.org/html/2602.14754v1#bib.bib17)), we use an alternative market efficiency proxy, E​f​f​b​o​t​h​2Effboth2, as a robustness check. Specifically, for each trading day dd we compute the relative high-low spread as

|  |  |  |  |
| --- | --- | --- | --- |
|  | S2=Pdh​i​g​h−Pdl​o​w(Pdh​i​g​h+Pdl​o​w)/2,S\_{2}=\frac{P^{high}\_{d}-P^{low}\_{d}}{\left(P^{high}\_{d}+P^{low}\_{d}\right)/2}, |  | (9) |

and then take the month average of this daily measure. Similar to our previous definition regarding market efficiency, we use the negative spread to be a proxy for market efficiency. That is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | E​f​f2=−S2,Eff\_{2}=-S\_{2}, |  | (10) |

For A share market and H share market, we calculate the E​f​f2Eff\_{2} separately and then add them up as an alternative proxy for overall market efficiency (E​F​F​b​o​t​h​2EFFboth2). Table 6 presents our regression results for third robustness check.
Even though S​H​H​K​P​o​l​i​c​ySHHKPolicy is not statistically significant, the sign of coefficient is negative. The interaction term S​H​H​K​P​o​l​i​c​y×E​f​f​b​o​t​h​2SHHKPolicy\times Effboth2 is negatively significant at 5% level. So, in general, this result is consistent with the result shown in Table 3.

Table 6: Efficiency-Dependent Effects of the SHHK Stock Connect using alternative efficiency measurement

|  |  |
| --- | --- |
|  | AH Premium |
|  | (1) |
| Lagged Premium | 0.796∗∗∗ |
|  | (0.066) |
| SHHKPolicy | -0.130 |
|  | (0.111) |
| Effboth2 | 2.370 |
|  | (1.638) |
| SHHKPolicy ×\times Effboth2 | -4.504∗∗ |
|  | (1.859) |
| Turnover | 0.011∗∗ |
|  | (0.004) |
| SOE | 0.033 |
|  | (0.031) |
| Demand | 0.000 |
|  | (0.006) |
| Size | -0.042∗∗ |
|  | (0.020) |
| Interest rate | 0.006∗∗∗ |
|  | (0.001) |
| Observations | 6363 |
| AR(2) pp-value | 0.406 |
| Hansen Test pp-value | 0.272 |

* •

  Notes: This table reports dynamic panel estimates examining how market efficiency conditions the effect of the SHHK Stock Connect on the AH price premium. E​f​f​b​o​t​h​2Effboth2 measures overall market efficiency across the A- and H-share markets, with higher values (less negative) indicating greater efficiency. The interaction term allows the policy effect to vary with market efficiency. The model is estimated using two-step system GMM. Lagged dependent variables and potentially endogenous regressors are instrumented using their own lags dated t−2t-2 and t−3t-3. Firm and year fixed effects are included. Robust standard errors are reported in parentheses.
* •

  ∗∗∗, ∗∗, and ∗ denote statistical significance at the 1%, 5%, and 10% levels, respectively.

The SHHK Stock Connect was launched in November, 2014, to further test whether the effect comes from SHHK Stock Connect and assess the robustness of our previous findings, we conduct a placebo test by assigning the implementation of the SHHK Stock Connect to a later date. Specifically, we assume that the policy was introduced two years after its actual launch and construct a binary indicator, F​a​k​e​P​o​l​i​c​yFakePolicy, which equals one for observations after November 2016 and zero otherwise.

Table 7 reports the placebo regression results for the effect of SHHK Stock Connect on share price premium. In contrast to the baseline estimates, the coefficient on F​a​k​e​P​o​l​i​c​yFakePolicy is positive but insignificant across all columns. This finding suggests that share price premium is not driven by common time trend, the SHHK stock policy does affect the premium. Next step, we conducted the placebo test regarding whether there is an efficiency dependent effects of the SHHK Stock Connect. Table 8 reports a placebo test in which the SHHK Stock Connect is assumed to have been implemented two years later, in November 2016. The key coefficient of interest is the interaction term between the placebo policy indicator and market efficiency, F​a​k​e​P​o​l​i​c​y×E​f​f​b​o​t​hFakePolicy\times Effboth.

The interaction term F​a​k​e​P​o​l​i​c​y×E​f​f​b​o​t​hFakePolicy\times Effboth is statistically insignificant, indicating that when the policy timing is artificially shifted, market efficiency does not systematically condition the relationship between the placebo policy and the AH price premium. This result suggests that the efficiency-dependent effect documented in the previous analysis is not driven by common time trends or spurious correlations, but is instead specific to the actual implementation of the SHHK Stock Connect.

Table 7: Placebo

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | AH Premium | AH Premium | AH Premium | AH Premium | AH Premium | AH Premium |
|  | (1) | (2) | (3) | (4) | (5) | (6) |
| Lagged Premium | 0.790∗∗∗ | 0.725∗∗∗ | 0.726∗∗∗ | 0.727∗∗∗ | 0.751∗∗∗ | 0.751∗∗∗ |
|  | (0.118) | (0.126) | (0.125) | (0.128) | (0.117) | (0.118) |
| FakePolicy | 0.013 | 0.000 | 0.001 | 0.001 | 0.011 | 0.011 |
|  | (0.030) | (0.036) | (0.036) | (0.036) | (0.031) | (0.032) |
| Turnover |  | 0.023∗ | 0.023∗ | 0.022∗ | 0.016∗∗ | 0.016∗∗ |
|  |  | (0.013) | (0.013) | (0.012) | (0.007) | (0.007) |
| SOE |  |  | 0.049 | 0.047 | 0.027 | 0.027 |
|  |  |  | (0.047) | (0.050) | (0.039) | (0.038) |
| Demand |  |  |  | -0.009 | -0.004 | -0.004 |
|  |  |  |  | (0.011) | (0.009) | (0.009) |
| Size |  |  |  |  | -0.059 | -0.059 |
|  |  |  |  |  | (0.036) | (0.036) |
| Interest rate |  |  |  |  |  | -0.000 |
|  |  |  |  |  |  | (0.002) |
| Observations | 6363 | 6363 | 6363 | 6363 | 6363 | 6363 |
| AR(2) pp-value | 0.158 | 0.615 | 0.621 | 0.589 | 0.450 | 0.452 |
| Hansen Test pp-value | 0.527 | 0.402 | 0.403 | 0.412 | 0.445 | 0.445 |

* •

  Notes: This table reports placebo tests in which the SHHK Stock Connect is assumed to have been implemented two years later, in November 2016. F​a​k​e​P​o​l​i​c​yFakePolicy is a binary indicator equal to one for observations after the placebo date and zero otherwise. The dependent variable is the monthly AH price premium. The model is estimated using two-step system GMM. Lagged dependent variables are instrumented using their own lags dated t−2t-2 and t−3t-3. Firm and year fixed effects are included. Robust standard errors are reported in parentheses.
* •

  ∗∗∗, ∗∗, and ∗ denote statistical significance at the 1%, 5%, and 10% levels, respectively.




Table 8: Efficiency-Dependent Effects of the SHHK Stock Connect using alternative efficiency measurement

|  |  |
| --- | --- |
|  | AH Premium |
|  | (1) |
| Lagged Premium | 0.680∗∗∗ |
|  | (0.103) |
| FakePolicy | 0.150 |
|  | (0.127) |
| Effboth | -1.852 |
|  | (4.273) |
| FakePolicy ×\times Effboth | 11.928 |
|  | (10.301) |
| Turnover | 0.019∗∗∗ |
|  | (0.006) |
| SOE | 0.026 |
|  | (0.042) |
| Demand | -0.007 |
|  | (0.009) |
| Size | -0.080∗∗ |
|  | (0.032) |
| Interest rate | -0.001 |
|  | (0.002) |
| Observations | 6363 |
| AR(2) pp-value | 0.466 |
| Hansen Test pp-value | 0.849 |

* •

  Notes: This table reports placebo tests in which the SHHK Stock Connect is assumed to have been implemented two years later, in November 2016. F​a​k​e​P​o​l​i​c​yFakePolicy is a binary indicator equal to one for observations after the placebo date and zero otherwise. The dependent variable is the monthly AH price premium. The model is estimated using two-step system GMM. Lagged dependent variables are instrumented using their own lags dated t−2t-2 and t−3t-3. Firm and year fixed effects are included. Robust standard errors are reported in parentheses.
* •

  ∗∗∗, ∗∗, and ∗ denote statistical significance at the 1%, 5%, and 10% levels, respectively.

## 4 Conclusion and Limitation

This study examines how the Shanghai–Hong Kong Stock Connect affects the A–H share price premium and whether the policy impact varies with market efficiency. Our findings are as follows: Firstly, the implementation of the Shanghai–Hong Kong Stock Connect significantly increases the AH premium by 18.4% on average. Second, the effect is heterogeneous and depends on the overall market efficiency. When we interact the policy indicator with market-efficiency measure, the marginal policy effect becomes pronounced for firms operating under lower market efficiency conditions, which increases the AH premium; on the other hand, the SHHK Stock Connect can reduce the AH premium for the dual-listing firms operating in higher market efficiency. Finally, we find no evidence of a premium response at the announcement stage. When April 2014 is used as an announcement event date, the announcement indicator and its interaction with efficiency are statistically insignificant, suggesting that the AH premium is unlikely to change prior to the implementation of the SHHK Stock Connect. This study also has two limitations. First, our sample is restricted to A–H firms whose A-shares are listed in Shanghai, so the evidence should be interpreted as specific to SHHK-eligible firms and may not generalise to Shenzhen-listed dual-listed firms. So, in the future, we may expand the sample to incorporate Shenzhen-listed A–H firms and examine whether the Shenzhen–Hong Kong Stock Connect exhibits a similar pattern. Second, while we find the Shanghai Hong Kong Stock Connect has different effects across firms, the mechanism explaining why the premium increases remains underdeveloped. Future research could introduce more direct channel variables, such as northbound and southbound holdings shares.

## References

* Allen et al., (2024)

  Allen, F., Qian, J. q., Shan, C., and Zhu, J. L. (2024).
  Dissecting the Long-Term Performance of the Chinese Stock Market.
  The Journal of Finance, 79(2):993–1054.
  \_eprint: https://onlinelibrary.wiley.com/doi/pdf/10.1111/jofi.13312.
* Bailey, (1994)

  Bailey, W. (1994).
  Risk and return on China’s new stock markets: Some preliminary evidence.
  Pacific-Basin Finance Journal, 2(2):243–260.
* Bekaert et al., (2005)

  Bekaert, G., Harvey, C. R., and Lundblad, C. (2005).
  Does financial liberalization spur growth?
  Journal of Financial Economics, 77(1):3–55.
* Bond et al., (2012)

  Bond, P., Edmans, A., and Goldstein, I. (2012).
  The Real Effects of Financial Markets.
  Annual Review of Financial Economics, 4(1):339–360.
* Chakravarty et al., (1998)

  Chakravarty, S., Sarkar, A., and Wu, L. (1998).
  Information asymmetry, market segmentation and the pricing of cross-listed shares: theory and evidence from Chinese A and B shares.
  Journal of International Financial Markets, Institutions and Money, 8(3):325–356.
* Chan and Kwok, (2005)

  Chan, K. and Kwok, J. K. (2005).
  Market Segmentation and Share Price Premium: Evidence from Chinese Stock Markets.
  Journal of Emerging Market Finance, 4(1):43–61.
* Chan and Kwok, (2016)

  Chan, M. K. and Kwok, S. S. (2016).
  Capital account liberalization and dynamic price discovery: evidence from Chinese cross-listed stocks.
  Applied Economics, 48(6):517–535.
* Corwin and Schultz, (2012)

  Corwin, S. A. and Schultz, P. (2012).
  A Simple Way to Estimate Bid‐Ask Spreads from Daily High and Low Prices.
  The Journal of Finance, 67(2):719–760.
* Domowitz et al., (1997)

  Domowitz, I., Glen, J., and Madhavan, A. (1997).
  Market Segmentation and Stock Prices: Evidence from an Emerging Market.
  The Journal of Finance, 52(3):1059–1085.
  \_eprint: https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1540-6261.1997.tb02725.x.
* Fama, (1970)

  Fama, E. F. (1970).
  Efficient Capital Markets: A Review of Theory and Empirical Work.
  The Journal of Finance, 25(2):383–417.
* Fama, (1991)

  Fama, E. F. (1991).
  Efficient Capital Markets: II.
  The Journal of Finance, 46(5):1575–1617.
  \_eprint: https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1540-6261.1991.tb04636.x.
* Fan and Wang, (2017)

  Fan, Q. and Wang, T. (2017).
  The impact of Shanghai–Hong Kong Stock Connect policy on A-H share price premium.
  Finance Research Letters, 21:222–227.
* Gagnon and Andrew Karolyi, (2010)

  Gagnon, L. and Andrew Karolyi, G. (2010).
  Multi-market trading and arbitrage.
  Journal of Financial Economics, 97(1):53–80.
* Hui and Chan, (2018)

  Hui, E. C. and Chan, K. K. K. (2018).
  Does the Shanghai–Hong Kong Stock Connect significantly affect the A-H premium of the stocks?
  Physica A: Statistical Mechanics and its Applications, 492:207–214.
* Lee et al., (2001)

  Lee, C. F., Chen, G.-m., and Rui, O. M. (2001).
  Stock Returns and Volatility on China’s Stock Markets.
  Journal of Financial Research, 24(4):523–543.
  \_eprint: https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1475-6803.2001.tb00829.x.
* Li et al., (2006)

  Li, Y., Yan, D., and Greco, J. (2006).
  Market segmentation and price differentials between A shares and H shares in the Chinese stock markets.
  Journal of Multinational Financial Management, 16(3):232–248.
* Meng et al., (2023)

  Meng, Y., Xiong, L., Xiao, L., and Bai, M. (2023).
  The effect of overseas investors on local market efficiency: evidence from the Shanghai/Shenzhen–Hong Kong Stock Connect.
  Financial Innovation, 9(1):42.
* Mitton, (2006)

  Mitton, T. (2006).
  Stock market liberalization and operating performance at the firm level.
  Journal of Financial Economics, 81(3):625–647.
* Pan and Chi, (2021)

  Pan, J. and Chi, J. (2021).
  How Does the Shanghai-Hong Kong Stock Connect Policy Impact the A-H Share Premium?
  Emerging Markets Finance and Trade, 57(7):1912–1928.
* Shleifer and Vishny, (1997)

  Shleifer, A. and Vishny, R. W. (1997).
  The Limits of Arbitrage.
  The Journal of Finance, 52(1):35–55.
  \_eprint: https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1540-6261.1997.tb03807.x.

## 5 Appendix

Table 9: A-H Dual-Listed Firms

| A-share Code | H-share Code | Firm Name | A-listing Date | H-listing Date |
| --- | --- | --- | --- | --- |
| 600011.SH | 0902.HK | HPI | 2001-12-06 | 1998-01-21 |
| 600012.SH | 0995.HK | ANHUI EXPRESSWAY | 2003-01-07 | 1996-11-13 |
| 600016.SH | 1988.HK | CMBC | 2000-12-19 | 2009-11-26 |
| 600026.SH | 1138.HK | COSCO SHIPPING Energy | 2002-05-23 | 1994-11-11 |
| 600027.SH | 1071.HK | HDPI | 2005-02-03 | 1999-06-30 |
| 600028.SH | 0386.HK | Sinopec Corp. | 2001-08-08 | 2000-10-19 |
| 600029.SH | 1055.HK | CSN | 2003-07-25 | 1997-07-31 |
| 600030.SH | 6030.HK | CITIC Securities Co., Ltd. | 2003-01-06 | 2011-10-06 |
| 600036.SH | 3968.HK | CM Bank | 2002-04-09 | 2006-09-22 |
| 600115.SH | 0670.HK | CEA | 1997-11-05 | 1997-02-05 |
| 600188.SH | 1171.HK | Yankuang Energy | 1998-07-01 | 1998-04-01 |
| 600196.SH | 2196.HK | Fosun Pharma | 1998-08-07 | 2012-10-30 |
| 600332.SH | 0874.HK | GYBYS | 2001-02-06 | 1997-10-30 |
| 600362.SH | 0358.HK | JCCL | 2002-01-11 | 1997-06-12 |
| 600377.SH | 0177.HK | Jiangsu Expressway | 2001-01-16 | 1997-06-27 |
| 600548.SH | 0548.HK | SZEW | 2001-12-25 | 1997-03-12 |
| 600585.SH | 0914.HK | ACC | 2002-02-07 | 1997-10-21 |
| 600600.SH | 0168.HK | Tsingtao Brewery | 1993-08-27 | 1993-07-15 |
| 600685.SH | 0317.HK | COMEC | 1993-10-28 | 1993-08-06 |
| 600688.SH | 0338.HK | SPC | 1993-11-08 | 1993-07-26 |
| 600775.SH | 0553.HK | NPEC | 1996-11-18 | 1996-05-02 |
| 600808.SH | 0323.HK | MAS C.L. | 1994-01-06 | 1993-11-03 |
| 600837.SH | 6837.HK | Haitong Securities | 1994-02-24 | 2012-04-27 |
| 600860.SH | 0187.HK | Jingcheng Machinery | 1994-05-06 | 1993-08-06 |
| 600871.SH | 1033.HK | SSC | 1995-04-11 | 1994-03-29 |
| 600874.SH | 1065.HK | TCEPC | 1995-06-30 | 1994-05-17 |
| 600875.SH | 1072.HK | DEC | 1995-10-10 | 1994-06-06 |
| 600876.SH | 1108.HK | Triumph New Energy | 1995-10-31 | 1994-07-08 |
| 601005.SH | 1053.HK | CISC | 2007-02-28 | 1997-10-17 |
| 601038.SH | 0038.HK | First Tractor | 2012-08-08 | 1997-06-23 |
| 601088.SH | 1088.HK | China Shenhua | 2007-10-09 | 2005-06-15 |
| 601107.SH | 0107.HK | Sichuan Expressway | 2009-07-27 | 1997-10-07 |
| 601111.SH | 0753.HK | Air China | 2006-08-18 | 2004-12-15 |
| 601186.SH | 1186.HK | CRCC | 2008-03-10 | 2008-03-13 |
| 601238.SH | 2238.HK | GAC Group | 2012-03-29 | 2010-08-30 |
| 601288.SH | 1288.HK | Agricultural Bank of China | 2010-07-15 | 2010-07-16 |
| 601318.SH | 2318.HK | Ping An | 2007-03-01 | 2004-06-24 |
| 601328.SH | 3328.HK | Bank of Communications | 2007-05-15 | 2005-06-23 |
| 601333.SH | 0525.HK | Guangshen Railway | 2006-12-22 | 1996-05-14 |
| 601336.SH | 1336.HK | NCI | 2011-12-16 | 2011-12-15 |
| 601390.SH | 0390.HK | China Railway | 2007-12-03 | 2007-12-07 |
| 601398.SH | 1398.HK | ICBC | 2006-10-27 | 2006-10-27 |
| 601588.SH | 0588.HK | Beijing North Star | 2006-10-16 | 1997-05-14 |
| 601600.SH | 2600.HK | Chalco | 2007-04-30 | 2001-12-12 |
| 601601.SH | 2601.HK | CPIC | 2007-12-25 | 2009-12-23 |
| 601607.SH | 2607.HK | Shanghai Pharma | 1994-03-24 | 2011-05-20 |
| 601618.SH | 1618.HK | MCC | 2009-09-21 | 2009-09-24 |
| 601628.SH | 2628.HK | China Life | 2007-01-09 | 2003-12-18 |
| 601633.SH | 2333.HK | Great Wall Motor | 2011-09-28 | 2003-12-15 |
| 601717.SH | 0564.HK | ZCZL | 2010-08-03 | 2012-12-05 |
| 601727.SH | 2727.HK | Shanghai Electric | 2008-12-05 | 2005-04-28 |
| 601766.SH | 1766.HK | CRRC | 2008-08-18 | 2008-08-21 |
| 601800.SH | 1800.HK | CCCC | 2012-03-09 | 2006-12-15 |
| 601808.SH | 2883.HK | COSL | 2007-09-28 | 2002-11-20 |
| 601818.SH | 6818.HK | CEB Bank | 2010-08-18 | 2013-12-20 |
| 601857.SH | 0857.HK | PetroChina | 2007-11-05 | 2000-04-07 |
| 601866.SH | 2866.HK | COSCO Shipping Development | 2007-12-12 | 2004-06-16 |
| 601880.SH | 2880.HK | Liaoning Port | 2010-12-06 | 2006-04-28 |
| 601898.SH | 1898.HK | China Coal Energy | 2008-02-01 | 2006-12-19 |
| 601899.SH | 2899.HK | Zijin Mining | 2008-04-25 | 2003-12-23 |
| 601919.SH | 1919.HK | COSCO Shipping Holdings | 2007-06-26 | 2005-06-30 |
| 601939.SH | 0939.HK | CCB | 2007-09-25 | 2005-10-27 |
| 601988.SH | 3988.HK | Bank of China | 2006-07-05 | 2006-06-01 |
| 601991.SH | 0991.HK | Datang Power | 2006-12-20 | 1997-03-21 |
| 601992.SH | 2009.HK | BBMG | 2011-03-01 | 2009-07-29 |
| 601998.SH | 0998.HK | CNCB | 2007-04-27 | 2007-04-27 |
| 603993.SH | 3993.HK | CMOC | 2012-10-09 | 2007-04-26 |